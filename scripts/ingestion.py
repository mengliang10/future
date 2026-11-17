#!/usr/bin/env python3
"""Private evidence inbox. Standard library only; never modifies site pages."""
import argparse
from datetime import datetime, timezone, timedelta
import hashlib
import html
import json
import os
from pathlib import Path
import re
import sqlite3
from urllib.parse import urlencode, urlsplit, urlunsplit, parse_qsl
from urllib.request import Request, urlopen


def now():
    return datetime.now(timezone.utc).isoformat()


def canonical(url):
    p = urlsplit(url.strip())
    if p.scheme not in ('http', 'https') or not p.netloc:
        raise ValueError('Evidence requires an HTTP(S) source URL')
    query = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True)
             if not k.lower().startswith('utm_') and k.lower() not in ('fbclid', 'gclid')]
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path or '/', urlencode(sorted(query)), ''))


def connect(root):
    root = Path(root)
    for folder in ('ingest', 'staging', 'database'):
        (root / folder).mkdir(parents=True, exist_ok=True)
    # Reuse the empty consolidated DB without touching existing graph databases.
    db = sqlite3.connect(root / 'future_research_consolidated.db', timeout=30)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA foreign_keys=ON')
    db.executescript('''
    CREATE TABLE IF NOT EXISTS inbox_evidence (
      id TEXT PRIMARY KEY, url TEXT UNIQUE NOT NULL, title TEXT NOT NULL,
      published_at TEXT, collected_at TEXT NOT NULL, source TEXT NOT NULL,
      excerpt TEXT NOT NULL, raw_path TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS inbox_origins (
      evidence_id TEXT REFERENCES inbox_evidence(id), source TEXT, source_id TEXT,
      collected_at TEXT NOT NULL, PRIMARY KEY(evidence_id,source,source_id));
    CREATE TABLE IF NOT EXISTS inbox_proposals (
      id TEXT PRIMARY KEY REFERENCES inbox_evidence(id), target_page TEXT NOT NULL DEFAULT '',
      claim TEXT NOT NULL DEFAULT '', replacement TEXT NOT NULL DEFAULT '',
      status TEXT NOT NULL DEFAULT 'new' CHECK(status IN
        ('new','reviewed','approved','rejected','published')), updated_at TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS inbox_reviews (
      id INTEGER PRIMARY KEY, evidence_id TEXT NOT NULL REFERENCES inbox_evidence(id),
      old_status TEXT, new_status TEXT, note TEXT NOT NULL, changed_at TEXT NOT NULL);
    ''')
    return db


def ingest(db, root, records, source):
    added = 0
    for item in records:
        url = canonical(item['url'])
        identity = hashlib.sha256(url.encode()).hexdigest()
        raw = Path(root) / 'ingest' / (identity + '.json')
        timestamp = now()
        title = str(item.get('title') or url)
        excerpt = html.unescape(re.sub('<[^>]+>', ' ', str(item.get('content') or item.get('excerpt') or '')))
        excerpt = re.sub(r'\s+', ' ', excerpt).strip()[:3000]
        # Only article evidence is persisted, not the complete Miniflux API response.
        payload = {key: item.get(key) for key in ('url','title','published_at','content','excerpt','id') if key in item}
        if not raw.exists():
            temporary = raw.with_suffix('.tmp')
            temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
            temporary.replace(raw)
        with db:
            result = db.execute('INSERT OR IGNORE INTO inbox_evidence VALUES (?,?,?,?,?,?,?,?)',
                (identity, url, title, item.get('published_at'), timestamp, source,
                 excerpt, str(raw.relative_to(root))))
            added += result.rowcount
            db.execute('INSERT OR IGNORE INTO inbox_origins VALUES (?,?,?,?)',
                (identity, source, str(item.get('id') or url), timestamp))
            db.execute('INSERT OR IGNORE INTO inbox_proposals(id,updated_at) VALUES (?,?)', (identity, timestamp))
    return added


def export_queue(db, root):
    rows = [dict(row) for row in db.execute('''SELECT e.*,p.target_page,p.claim,p.replacement,p.status,p.updated_at
        FROM inbox_evidence e JOIN inbox_proposals p USING(id) ORDER BY e.collected_at DESC,e.id''')]
    destination = Path(root) / 'staging' / 'review-queue.json'
    temporary = destination.with_suffix('.tmp')
    temporary.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    temporary.replace(destination)
    return rows


def load_config(path):
    values = {}
    if Path(path).exists():
        for line in Path(path).read_text().splitlines():
            if '=' in line and not line.lstrip().startswith('#'):
                key, value = line.split('=', 1)
                values[key.strip()] = value.strip().strip('\"\'')
    return {key: os.environ.get(key, values.get(key, '')) for key in ('MINIFLUX_BASE_URL','MINIFLUX_API_KEY')}


class NoRedirect(__import__('urllib.request', fromlist=['HTTPRedirectHandler']).HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None  # Do not forward the API token to a redirected host.


def miniflux(config, days, category=None):
    from urllib.request import build_opener
    base = config['MINIFLUX_BASE_URL'].rstrip('/')
    token = config['MINIFLUX_API_KEY']
    if not base or not token:
        raise ValueError('Configure MINIFLUX_BASE_URL and MINIFLUX_API_KEY')
    parsed = urlsplit(base)
    if parsed.scheme != 'https' and not (parsed.scheme == 'http' and parsed.hostname in ('localhost','127.0.0.1','::1')):
        raise ValueError('Use HTTPS for remote Miniflux connections')
    if parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError('Miniflux base URL must not contain credentials, query or fragment')
    if base.endswith('/v1'):
        base = base[:-3]
    cutoff = int((datetime.now(timezone.utc) - timedelta(days=days)).timestamp())
    offset = 0
    opener = build_opener(NoRedirect())
    while True:
        params = {'after': cutoff, 'order':'id', 'direction':'asc', 'limit':100, 'offset':offset}
        if category is not None:
            params['category_id'] = category
        request = Request(base + '/v1/entries?' + urlencode(params), headers={'X-Auth-Token':token, 'Accept':'application/json'})
        with opener.open(request, timeout=30) as response:
            entries = json.load(response)['entries'] or []
        if not entries:
            return
        yield entries
        offset += len(entries)
        if len(entries) < 100:
            return


def review(db, args):
    row = db.execute('SELECT * FROM inbox_proposals WHERE id=?', (args.id,)).fetchone()
    if row is None:
        raise ValueError('Unknown evidence ID; use the full ID from review-queue.json')
    transitions = {'new':{'reviewed','rejected'}, 'reviewed':{'approved','rejected'},
                   'approved':{'published','reviewed','rejected'}, 'rejected':{'new'}, 'published':set()}
    if args.status not in transitions[row['status']]:
        raise ValueError('Invalid status transition: ' + row['status'] + ' -> ' + args.status)
    target = args.target if args.target is not None else row['target_page']
    claim = args.claim if args.claim is not None else row['claim']
    replacement = args.replacement if args.replacement is not None else row['replacement']
    if target:
        path = Path(target)
        if path.is_absolute() or '..' in path.parts or not path.parts or path.parts[0] not in ('_stocks','_tech','_data','sectors','roadmap'):
            raise ValueError('Target must be a relative published-content path')
    if args.status in ('approved','published') and not all((target, claim, replacement, args.note)):
        raise ValueError('Approval requires target, claim, replacement and review note')
    with db:
        db.execute('UPDATE inbox_proposals SET target_page=?,claim=?,replacement=?,status=?,updated_at=? WHERE id=?',
                   (target, claim, replacement, args.status, now(), args.id))
        db.execute('INSERT INTO inbox_reviews(evidence_id,old_status,new_status,note,changed_at) VALUES (?,?,?,?,?)',
                   (args.id,row['status'],args.status,args.note,now()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1] / 'research')
    commands = parser.add_subparsers(dest='command', required=True)
    mf = commands.add_parser('miniflux')
    mf.add_argument('--days',type=int,default=7)
    mf.add_argument('--category',type=int)
    mf.add_argument('--config',default=str(Path.home()/'.config/environment.d/miniflux.conf'))
    imp = commands.add_parser('import-json')
    imp.add_argument('file',type=Path)
    imp.add_argument('--source',required=True)
    commands.add_parser('queue')
    rev = commands.add_parser('review')
    rev.add_argument('id')
    rev.add_argument('status', choices=['new','reviewed','approved','rejected','published'])
    rev.add_argument('--target')
    rev.add_argument('--claim')
    rev.add_argument('--replacement')
    rev.add_argument('--note',default='')
    args = parser.parse_args()
    if args.command == 'miniflux' and args.days < 1:
        parser.error('--days must be positive')
    args.root = args.root.resolve()
    db = connect(args.root)
    try:
        if args.command == 'miniflux':
            count = 0
            for page in miniflux(load_config(args.config),args.days,args.category):
                count += ingest(db,args.root,page,'miniflux')
            print('New evidence:',count)
        elif args.command == 'import-json':
            records = json.loads(args.file.read_text())
            if not isinstance(records,list):
                raise ValueError('Expected a JSON array of article records')
            print('New evidence:',ingest(db,args.root,records,args.source))
        elif args.command == 'review':
            review(db,args)
        rows = export_queue(db,args.root)
        print('Evidence in queue:',len(rows))
    finally:
        db.close()


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        # Exception messages from network services may contain private URLs.
        if isinstance(error, ValueError):
            raise SystemExit(str(error))
        raise SystemExit('Ingestion failed (' + type(error).__name__ + '); no site content was changed')
