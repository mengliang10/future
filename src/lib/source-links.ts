import {url} from "./base";
import {records} from './catalogue';

const SECTOR_MIGRATION: Record<string, string> = {
  'ai': 'applied-ai',
  'semiconductors': 'semiconductors',
  'hardware': 'semiconductors',
  'cyber': 'cybersecurity',
  'blockchain': 'blockchain',
  'biotech': 'drugs-biotech',
  'bci': 'bci',
  'robotics': 'robotics',
  'autonomous': 'autonomous',
  'space': 'space',
  'xr': 'spatial-computing',
  'quantum': 'quantum',
  'energy': 'energy',
  'software': 'ai-agents-software',
  'marketing': 'applied-ai',
  'memory': 'memory',
  'materials': 'materials-physics',
  // Map old official sectors if linked
  'information-technology': 'semiconductors',
  'financials': 'blockchain',
  'health-care': 'drugs-biotech',
  'consumer-discretionary': 'spatial-computing',
  'communication-services': 'applied-ai',
  'industrials': 'robotics',
  'consumer-staples': 'applied-ai',
  'real-estate': 'applied-ai',
  'utilities': 'energy'
};

export async function sourceLinks(html: string): Promise<string> {
  const [tech, companies, sectors] = await Promise.all([
    records('technologies'),
    records('companies'),
    records('sectors')
  ]);
  const techIds = new Set(tech.map(t => t.id));
  const companyIds = new Set(companies.map(c => c.id));
  const sectorIds = new Set(sectors.map(s => s.id));

  html = html
    .replace(/<form\b[^>]*action="[^"]*REPLACE_WITH_YOUR_FORM_ID"[\s\S]*?<\/form>/gi, '<p><a href="mailto:mengliang.online@gmail.com">Email the author ↗</a></p>')
    .replace(/<div class="callout callout-info"[^>]*>[\s\S]*?Powered by[\s\S]*?<\/div>/g, '');

  // Resolve legacy root-relative images against the GitHub Pages /future/ base.
  html = html.replace(/src="(\/[^"]*)"/g, (_whole, src) => {
    const clean = src.replace(/^\/future(?=\/)/, '');
    return `src="${url(clean).replaceAll('&', '&amp;')}"`;
  });

  return html.replace(/href="(\/[^"]*)"/g, (whole, href) => {
    let dest = href.replace(/^\/future\//, '/');

    if (dest.startsWith('/roadmap/')) {
      const slug = dest.split('/')[2];
      dest = slug ? `/read/roadmap--${slug}/` : '/roadmaps/';
    } else if (dest === '/tech/') {
      dest = '/explore/';
    } else if (dest === '/stocks/' || dest === '/companies/') {
      dest = '/companies/';
    } else if (/^\/(stocks|companies)\//.test(dest)) {
      const id = dest.split('/')[2].toLowerCase();
      dest = companyIds.has(id) ? `/companies/${id}/` : `/companies/?q=${encodeURIComponent(id)}`;
    } else if (dest.startsWith('/sectors/')) {
      const parts = dest.split('/').filter(Boolean);
      const sectorSlug = parts[1];
      if (sectorSlug) {
        if (sectorIds.has(sectorSlug)) {
          dest = `/sectors/${sectorSlug}/`;
        } else if (SECTOR_MIGRATION[sectorSlug]) {
          dest = `/sectors/${SECTOR_MIGRATION[sectorSlug]}/`;
        } else {
          dest = '/sectors/';
        }
      } else {
        dest = '/sectors/';
      }
    } else if (dest.startsWith('/tech/')) {
      const id = dest.split('/')[2];
      if (techIds.has(id)) {
        dest = `/tech/${id}/`;
      } else {
        const candidates = tech.filter(t => t.id.startsWith(id + '-') || t.id.endsWith('-' + id) || t.id.includes(id));
        if (candidates.length === 1) {
          dest = `/tech/${candidates[0].id}/`;
        } else {
          dest = `/explore/?q=${encodeURIComponent(id.replaceAll('-', ' '))}`;
        }
      }
    } else if (['/blog/', '/blog'].includes(dest)) {
      dest = '/research/';
    } else if (dest === '/about/') {
      dest = '/read/about/';
    } else if (dest === '/contact/') {
      dest = '/read/contact/';
    } else if (dest === '/scifi/') {
      dest = '/read/scifi--index/';
    }

    return `href="${url(dest).replaceAll('&', '&amp;')}"`;
  });
}
