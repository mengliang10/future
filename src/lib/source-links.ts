import {url} from "./base";
import {records} from './catalogue';

const SECTOR_MIGRATION: Record<string, string> = {
  'ai': 'information-technology',
  'semiconductors': 'information-technology',
  'hardware': 'information-technology',
  'cyber': 'information-technology',
  'blockchain': 'financials',
  'biotech': 'health-care',
  'bci': 'health-care',
  'robotics': 'industrials',
  'autonomous': 'consumer-discretionary',
  'space': 'industrials',
  'xr': 'information-technology',
  'quantum': 'information-technology',
  'software': 'information-technology',
  'marketing': 'communication-services'
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

  // Build title lookup for intelligent tech link resolution
  const techTitleMap = new Map<string, string>();
  for (const t of tech) {
    if (t.title) {
      techTitleMap.set(t.title.trim().toLowerCase(), t.id);
    }
  }

  html = html
    .replace(/<form\b[^>]*action="[^"]*REPLACE_WITH_YOUR_FORM_ID"[\s\S]*?<\/form>/gi, '<p><a href="mailto:mengliang.online@gmail.com">Email the author ↗</a></p>')
    .replace(/<div class="callout callout-info"[^>]*>[\s\S]*?Powered by[\s\S]*?<\/div>/g, '');

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
        // Try to find if there's a close candidate with prefixes/suffixes
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
