import fs from 'node:fs';import path from 'node:path';
const args=process.argv.slice(2);const flag=name=>args[args.indexOf(name)+1];
if(!args.includes('--collection')||!args.includes('--id')||!args.includes('--patch')){console.log('Usage: npm run update -- --collection technologies --id stable-id --patch patch.json [--apply]');process.exit(1);}
const kind=flag('--collection'),id=flag('--id');if(!['technologies','companies','blocks','sectors'].includes(kind)||!/^[a-z0-9._-]+$/.test(id))throw Error('Invalid update target');
const file=path.join('src/content',kind,id+'.json');const current=JSON.parse(fs.readFileSync(file));const patch=JSON.parse(fs.readFileSync(flag('--patch')));for(const key of ['id','sourcePath','sourceHash','sourceMeta','bodyMarkdown','bodyHtml'])if(key in patch)throw Error(`Use the source/notes authoring workflow to change ${key}`);
for(const key of Object.keys(patch))if(!(key in current))throw Error(`Unknown field: ${key}`);
const decks=fs.readdirSync('src/content/decks').map(file=>JSON.parse(fs.readFileSync('src/content/decks/'+file)));
const affected=decks.filter(d=>d.mode!=='snapshot'&&(kind==='technologies'?d.technologies.includes(id):kind==='blocks'?d.blocks.includes(id):kind==='sectors'?d.sector===id:false));
const report={target:`${kind}:${id}`,fields:Object.keys(patch),affectedDecks:affected.map(d=>d.id),snapshotDecksUnaffected:decks.filter(d=>d.mode==='snapshot').length,applied:args.includes('--apply')};
if(report.applied){fs.mkdirSync('source/edit-history',{recursive:true});const stamp=new Date().toISOString().replaceAll(':','-');fs.writeFileSync(`source/edit-history/${kind}-${id}-${stamp}.json`,JSON.stringify(current,null,2));fs.writeFileSync(file,JSON.stringify({...current,...patch},null,2)+'\n');}console.log(JSON.stringify(report,null,2));
