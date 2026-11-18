from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
from collections import Counter
import json,hashlib
root=Path('dist');broken=Counter();sourceissues=[];pages=0
for p in root.rglob('*.html'):
 pages+=1;s=BeautifulSoup(p.read_text(),'html.parser')
 for a in s.select('a[href]'):
  u=urlsplit(a['href'])
  if u.scheme or u.netloc or not u.path or not u.path.startswith('/'):continue
  target=root/unquote(u.path).lstrip('/')
  if not target.exists():broken[u.path]+=1
manifest=json.loads(Path('qa/import-manifest.json').read_text())
for entry in manifest['records']:
 if not entry.get('source'):continue
 original=Path('source/original')/entry['source'];download=Path('public/source')/entry['source']
 if not download.exists() or hashlib.sha256(download.read_bytes()).hexdigest()!=entry['sourceHash']:sourceissues.append(entry['source'])
report={'htmlPages':pages,'brokenInternalPaths':dict(broken),'originalDownloadHashMismatches':sourceissues,'sourceCommit':manifest['sourceCommit']}
Path('qa/site-audit.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));raise SystemExit(bool(broken or sourceissues))
