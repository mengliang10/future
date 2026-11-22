from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, unquote
import posixpath
from collections import Counter
import json, hashlib

root = Path('dist')
broken = Counter()
sourceissues = []
pages = 0
assets_checked = 0
external_urls = set()
base = '/future'

for p in root.rglob('*.html'):
    pages += 1
    s = BeautifulSoup(p.read_text(encoding='utf-8', errors='ignore'), 'html.parser')
    for element in s.select('[href], [src]'):
        raw = element.get('href') or element.get('src')
        if not raw or not isinstance(raw, str):
            continue
        parsed = urlsplit(raw)
        if parsed.scheme in ('https', 'http') or parsed.netloc:
            external_urls.add(raw)
            continue
        if parsed.scheme or not parsed.path:
            continue
        if element.name != 'a':
            assets_checked += 1
        # Links relative to the current HTML document are legal and must resolve.
        if parsed.path.startswith('/'):
            if parsed.path != base and not parsed.path.startswith(base + '/'):
                broken[raw] += 1
                continue
            rel = parsed.path[len(base):].lstrip('/')
        else:
            rel = posixpath.normpath(posixpath.join(p.relative_to(root).parent.as_posix(), parsed.path))
        rel = unquote(rel)
        if rel == '..' or rel.startswith('../'):
            broken[raw] += 1
            continue
        target = root / rel
        if target.is_dir():
            target = target / 'index.html'
        elif not target.exists() and not target.suffix:
            html = root / (rel + '.html')
            index = root / rel / 'index.html'
            target = html if html.exists() else index
        if not target.is_file():
            broken[raw] += 1
manifest = json.loads(Path('qa/import-manifest.json').read_text())
for entry in manifest['records']:
    if not entry.get('source'):
        continue
    original = Path('source/original') / entry['source']
    download = Path('public/source') / entry['source']
    if not download.exists() or hashlib.sha256(download.read_bytes()).hexdigest() != entry['sourceHash']:
        sourceissues.append(entry['source'])

report = {
    'htmlPages': pages,
    'assetReferencesChecked': assets_checked,
    'externalLinksInventoried': len(external_urls),
    'externalLinks': sorted(external_urls),
    'brokenInternalPaths': dict(broken),
    'originalDownloadHashMismatches': sourceissues,
    'sourceCommit': manifest['sourceCommit']
}

Path('qa/site-audit.json').write_text(json.dumps(report, indent=2))
print(json.dumps(report, indent=2))
raise SystemExit(bool(broken or sourceissues))
