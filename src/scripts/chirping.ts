let events:AbortController;
function init(){events?.abort();events=new AbortController();const {signal}=events;
const button=document.querySelector<HTMLButtonElement>('.menu-button')!,sidebar=document.querySelector<HTMLElement>('.site-sidebar')!,nav=document.querySelector('#primary-nav')!,mask=document.querySelector<HTMLButtonElement>('.sidebar-mask')!;
const close=(focus=false)=>{sidebar.classList.remove('is-open');nav.classList.remove('open');mask.hidden=true;button.setAttribute('aria-expanded','false');document.body.classList.remove('nav-open');if(focus)button.focus();};
button.addEventListener('click',()=>{if(sidebar.classList.contains('is-open'))close();else{sidebar.classList.add('is-open');nav.classList.add('open');mask.hidden=false;button.setAttribute('aria-expanded','true');document.body.classList.add('nav-open');}},{signal});
mask.addEventListener('click',()=>close(true),{signal});sidebar.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>close(),{signal}));
const theme=document.querySelector<HTMLButtonElement>('[data-theme-toggle]');
if(theme){
const updateTheme=()=>{const isDark=document.documentElement.dataset.theme==='dark';theme.setAttribute('aria-pressed',String(isDark));theme.setAttribute('aria-checked',String(isDark));};updateTheme();
theme.addEventListener('click',()=>{const value=document.documentElement.dataset.theme==='dark'?'light':'dark';document.documentElement.dataset.theme=value;try{localStorage.setItem('future-theme',value);}catch{}updateTheme();},{signal});
}
document.addEventListener('keydown',event=>{if(event.key==='Escape')close(true);if(event.key==='/'&&!event.ctrlKey&&!event.metaKey&&!['INPUT','TEXTAREA','SELECT'].includes((event.target as HTMLElement).tagName)){event.preventDefault();document.querySelector<HTMLInputElement>('#global-search')?.focus();}if(event.key==='Tab'&&sidebar.classList.contains('is-open')){const targets=[...sidebar.querySelectorAll<HTMLElement>('a,button')];const first=targets[0],last=targets.at(-1);if(event.shiftKey&&document.activeElement===first){event.preventDefault();last?.focus();}else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}}},{signal});
}
document.addEventListener('astro:page-load',init);init();
