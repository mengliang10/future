from pathlib import Path
import json,sys,re
from markdown_it import MarkdownIt
if len(sys.argv)!=3 or sys.argv[1] not in ['technologies','companies'] or not re.fullmatch(r'[a-z0-9._-]+',sys.argv[2]):raise SystemExit('Usage: python3 scripts/render-notes.py technologies stable-id')
p=Path('src/content')/sys.argv[1]/(sys.argv[2]+'.json');record=json.loads(p.read_text());record['bodyHtml']=MarkdownIt('commonmark',{'html':True}).enable('table').render(record['bodyMarkdown']);p.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n');print(p)
