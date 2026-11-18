import {url} from "./base";
import {records} from './catalogue';
export async function sourceLinks(html){
const [tech,companies]=await Promise.all([records('technologies'),records('companies')]);const techIds=new Set(tech.map(t=>t.id)),companyIds=new Set(companies.map(c=>c.id));
html=html.replace(/<form\b[^>]*action="[^"]*REPLACE_WITH_YOUR_FORM_ID"[\s\S]*?<\/form>/gi,'<p><a href="mailto:mengliang.online@gmail.com">Email the author ↗</a></p>').replace(/<div class="callout callout-info"[^>]*>[\s\S]*?Powered by[\s\S]*?<\/div>/g,'');
return html.replace(/href="(\/[^"]*)"/g,(whole,href)=>{let dest=href.replace(/^\/future\//,'/');
if(dest.startsWith('/roadmap/')){const slug=dest.split('/')[2];dest=slug?`/read/roadmap--${slug}/`:'/roadmaps/';}
else if(dest==='/tech/')dest='/explore/';
else if(dest==='/stocks/'||dest==='/companies/')dest='/companies/';
else if(/^\/(stocks|companies)\//.test(dest)){const id=dest.split('/')[2].toLowerCase();dest=companyIds.has(id)?`/companies/${id}/`:`/companies/?q=${encodeURIComponent(id)}`;}
else if(dest.startsWith('/tech/')){const id=dest.split('/')[2];if(!techIds.has(id))dest=`/explore/?q=${encodeURIComponent(id.replaceAll('-',' '))}`;}
else if(dest==='/sectors/hardware/')dest='/sectors/ai/';
else if(['/blog/','/blog'].includes(dest))dest='/research/';
else if(dest==='/about/')dest='/read/about/';else if(dest==='/contact/')dest='/read/contact/';else if(dest==='/scifi/')dest='/read/scifi--index/';
return `href="${url(dest).replaceAll('&','&amp;')}"`;});
}
