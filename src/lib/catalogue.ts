import {getCollection} from 'astro:content';
export const records=async name=>(await getCollection(name)).map(entry=>({...entry.data,id:entry.id}));
export const label=value=>String(value||'Not recorded').replaceAll('_',' ').replace(/\b\w/g,c=>c.toUpperCase());
export const slug=value=>String(value).toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');
export const dateLabel=value=>value?new Intl.DateTimeFormat('en-SG',{dateStyle:'medium',timeZone:'UTC'}).format(new Date(value)):'Not reviewed';
export const provenanceLabel=status=>status==='imported-unreviewed'?'Imported · Not revalidated':'Editorial brief · Sources cited';
