import fs from 'node:fs';import cp from 'node:child_process';import assert from 'node:assert/strict';
const target='src/content/blocks/reading-framework.json',original=fs.readFileSync(target,'utf8'),patch='qa/shared-update-patch.json',marker='QA shared content propagation check';let report;
function build(){const result=cp.spawnSync('npm',['run','build'],{encoding:'utf8'});fs.writeFileSync('qa/update-build.log',result.stdout+result.stderr);if(result.status!==0)throw Error('Build failed; see qa/update-build.log');}
try{
 fs.writeFileSync(patch,JSON.stringify({title:marker}));const update=cp.spawnSync('node',['scripts/update-record.mjs','--collection','blocks','--id','reading-framework','--patch',patch,'--apply'],{encoding:'utf8'});assert.equal(update.status,0);const change=JSON.parse(update.stdout);build();
 for(const id of change.affectedDecks)assert(fs.readFileSync(`dist/presentations/${id}/index.html`,'utf8').includes(marker),id);
 const snapshot='ai-01-snapshot-2026-11-16';assert(!fs.readFileSync(`dist/presentations/${snapshot}/index.html`,'utf8').includes(marker));report={sharedDecksUpdated:change.affectedDecks.length,snapshotPreserved:true,restored:true};
}finally{fs.writeFileSync(target,original);fs.rmSync(patch,{force:true});build();}
fs.writeFileSync('qa/shared-update-verification.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report));
