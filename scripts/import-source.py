"""Reproducible Jekyll import. Existing editorial records are never overwritten without --refresh."""
from pathlib import Path
from collections import Counter
import re,json,yaml,hashlib,shutil,subprocess,sys
from markdown_it import MarkdownIt
root=Path(__file__).resolve().parents[1];source=root/'source/original';out=root/'src/content';refresh='--refresh' in sys.argv
md=MarkdownIt('commonmark',{'html':True}).enable('table')
sectors={
 'ai':('AI & Computing',['AI & Cloud','AI Tech','Hardware','Connectivity']),
 'semiconductors':('Semiconductors',['Semiconductors']),
 'quantum':('Quantum Computing',['Quantum','Quantum Computing']),
 'robotics':('Robotics & Automation',['Robotics','Robotics & Automation']),
 'energy':('Energy',['Energy Tech']),
 'biotech':('Biotech & Health',['Biotech','Biotech & Healthcare']),
 'space':('Space',['Space Tech']),
 'cyber':('Cybersecurity',['Cybersecurity']),
 'autonomous':('Autonomous Systems',['Autonomous']),
 'blockchain':('Blockchain',['Blockchain','Blockchain & Crypto']),
 'xr':('Spatial Computing',['XR']),
 'bci':('Brain–Computer Interfaces',['BCI']),
 'marketing':('Marketing Technology',['Marketing Tech']),
 'policy':('Policy & Society',['Regulatory & Policy','Societal & Labour']),
 'markets':('Financial Infrastructure',['Financial Markets'])}
aliases={alias:key for key,(_,names) in sectors.items() for alias in names}
warnings=[];imported=[]
def split(p):
 text=p.read_text();parts=text.split('---',2)
 if len(parts)<3:return {},text
 try:data=yaml.safe_load(parts[1]) or {}
 except yaml.YAMLError:
  # Only source frontmatter has unquoted scalar colons. Preserve original download.
  lines=[]
  for line in parts[1].splitlines():
   if re.match(r'^[A-Za-z_]+: ',line):
    k,v=line.split(':',1);v=v.strip()
    if ': ' in v and not v.startswith(('"',"'",'[','{')):line=k+': '+json.dumps(v)
   lines.append(line)
  data=yaml.safe_load('\n'.join(lines)) or {};warnings.append(str(p.relative_to(source)))
 return data,parts[2].strip()
def text(value):return '' if value is None else str(value)
def clean_body(body):
 body=body.replace('\\n##','\n\n##')
 body=re.sub(r'\{\{\s*[\'\"]([^\'\"]+)[\'\"]\s*\|\s*relative_url\s*\}\}',lambda m:m[1],body)
 body=re.sub(r'<script\b[\s\S]*?</script>','',body,flags=re.I)
 body=re.sub(r'\{%\s*(for|if|unless)\b[\s\S]*?\{%\s*end(?:for|if|unless)\s*%\}','',body)
 body=re.sub(r'\{[%{][\s\S]*?[%}]\}','',body)
 body=body.replace('/future/','/').replace('/stocks/','/companies/')
 return body
def write(folder,id,data):
 dest=out/folder/(id+'.json');dest.parent.mkdir(parents=True,exist_ok=True)
 if not dest.exists() or refresh:dest.write_text(json.dumps(data,indent=2,ensure_ascii=False,default=str)+'\n')
 imported.append({'kind':folder,'id':id,'source':data.get('sourcePath'),'sourceHash':data.get('sourceHash')})
tech=[];companies=[]
for kind,folder in [('technologies','_tech'),('companies','_stocks')]:
 for p in sorted((source/folder).glob('*.md')):
  data,body=split(p);id=p.stem
  category=data.get('category') or data.get('sector') or next(iter(data.get('categories',[])),'Unclassified')
  sector=aliases.get(category,'other')
  entry={'id':id,'title':text(data.get('title') or data.get('name') or id.replace('-',' ').title()),'summary':text(data.get('subtitle')),'sector':sector,'sourceCategory':category,'sourcePath':str(p.relative_to(source)),'sourceHash':hashlib.sha256(p.read_bytes()).hexdigest(),'bodyHtml':md.render(clean_body(body)),'bodyMarkdown':body,'sourceMeta':data,'evidenceStatus':'imported-unreviewed','reviewedAt':None}
  if kind=='technologies':
   entry.update(stage=text(data.get('stage') or data.get('status') or 'unclassified'),confidenceLabel=text(data.get('confidence_label') or 'Not classified'),estimate=text(data.get('est_year_range') or data.get('est_year') or 'Not recorded'),estimateYear=data.get('est_year') if isinstance(data.get('est_year'),int) else None,sourceCount=data.get('source_count'),companies=[str(t).lower() for t in data.get('stocks',[])],businessMeaning='',investmentLens='')
   tech.append(entry)
  else:
   symbol=text(data.get('symbol') or data.get('ticker') or id.upper());entry.update(symbol=symbol,exchange=text(data.get('exchange') or ('Private' if '.PVT' in symbol.upper() else 'Not recorded')),private='.PVT' in symbol.upper(),businessMeaning='',investmentLens='');companies.append(entry)
  write(kind,id,entry)
  dest=root/'public/source'/folder/p.name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
if any(x['sector']=='other' for x in tech):sectors['other']=('Other research',[])
for id,(title,sourceAliases) in sectors.items():
 write('sectors',id,{'id':id,'title':title,'aliases':sourceAliases,'businessQuestion':'Which operational constraint could this technology remove, and what would adoption cost?','investorQuestion':'Who could capture the value, what must be funded first, and what evidence would change the thesis?'})
# Preserve all other narrative/source pages, and render supported narrative without Jekyll scripts.
seen=set()
for p in sorted(source.rglob('*.md')):
 if any(x in p.parts for x in ['.git','_tech','_stocks','enhancements']):continue
 relative=str(p.relative_to(source));id=relative.removesuffix('.md').replace('/','--')
 if relative=='README.md':continue
 data,body=split(p)
 write('articles',id,{'id':id,'title':text(data.get('title') or p.stem.replace('-',' ').title()),'summary':text(data.get('subtitle') or data.get('description')),'sourcePath':relative,'sourceHash':hashlib.sha256(p.read_bytes()).hexdigest(),'bodyHtml':md.render(clean_body(body)),'sourceMeta':data})
 dest=root/'public/source'/relative;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
# Deck manifests contain stable content references; no copied statistics.
for sector in sectors:
 ids=[e['id'] for e in tech if e['sector']==sector]
 for start in range(0,len(ids),12):
  volume=start//12+1;id=f'{sector}-{volume:02}'
  write('decks',id,{'id':id,'title':f'{sectors[sector][0]} — Briefing {volume:02}','sector':sector,'mode':'evergreen','added':'2026-11-16','blocks':['reading-framework','evidence-check'],'technologies':ids[start:start+12]})
# Shared reusable slide text is itself a stable update target.
for id,title,points in [
 ('reading-framework','Read the signal. Ask the next question.',['What is the technology and which constraint does it address?','Business lens: adoption cost, workflow change and measurable usefulness.','Investor lens: value capture, capital required and evidence that could change a thesis.']),
 ('evidence-check','An estimate is a question to investigate.',['Technology stages and timelines are imported research claims, not independently revalidated here.','A source count is not proof of source quality or a probability of success.','Use the original notes, verify primary evidence, and record the date of your review.'])]:
 write('blocks',id,{'id':id,'title':title,'points':points})
assets=root/'public/data';assets.mkdir(parents=True,exist_ok=True)
shutil.copy2(source/'assets/data/stocks.json',assets/'market-snapshot.json')
for p in (source/'_data').glob('*'):
 dest=root/'public/source-data'/p.name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=source,text=True).strip()
report={'sourceCommit':commit,'importedAt':'2026-11-16','counts':dict(Counter(r['kind'] for r in imported)),'frontmatterRepairs':warnings,'records':imported,'notes':'Imported content preserved; claims not fact-checked. JSON is editable canonical source; rerun without --refresh preserves local changes.'}
(root/'qa').mkdir(exist_ok=True);(root/'qa/import-manifest.json').write_text(json.dumps(report,indent=2));print(json.dumps(report['counts']));print('Frontmatter scalar quoting repairs:',len(warnings))
