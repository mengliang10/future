import {getCollection} from 'astro:content';
export const records=async name=>(await getCollection(name)).map(entry=>({...entry.data,id:entry.id,...(name==='technologies' ? {title: displayTitle(entry.data.title)} : {})}));
export const label=value=>String(value||'Not recorded').replaceAll('_',' ').replace(/\b\w/g,c=>c.toUpperCase());
export const slug=value=>String(value).toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');
export const dateLabel=value=>value?new Intl.DateTimeFormat('en-SG',{dateStyle:'medium',timeZone:'UTC'}).format(new Date(value)):'Not reviewed';
export const provenanceLabel=status=>status==='imported-unreviewed'?'Imported · Not revalidated':'Editorial brief · Sources cited';

const TITLE_ACRONYMS: Record<string, string> = {
  Ai: 'AI', Ml: 'ML', Qc: 'QC', Hpc: 'HPC', Gpu: 'GPU', Cpu: 'CPU', Api: 'API', Llm: 'LLM',
  Bci: 'BCI', Dna: 'DNA', Rna: 'RNA', Mrna: 'mRNA', Hbm: 'HBM', Soc: 'SoC', Asic: 'ASIC',
  Fpga: 'FPGA', Dram: 'DRAM', Sram: 'SRAM', Iot: 'IoT', Lidar: 'LiDAR'
};
/** Splits compact imported titles such as "NeutralAtomQuantum" for display only. */
export const displayTitle = (value: unknown): string => {
  const raw = String(value || '');
  // Normalize imported word-separated titles, including mixed case and numeric tokens.
  // Keep established technical compounds and model identifiers intact.
  const protectedTerms = /\b(?:Wi-Fi|Li-Fi|X-Rays?|T-Cells?|B-Cells?|E-Commerce|E-SIM|E-Ink|P-Type|N-Type|COVID-19|GPT-\d+(?:\.\d+)?|[A-Z]{2,}-\d+[A-Za-z0-9]*|\d+-bit|\d+-nm)\b/gi;
  const saved: string[] = [];
  const masked = raw.replace(protectedTerms, term => `\uE000${saved.push(term)-1}\uE001`);
  const text = masked.replace(/(?<=[\p{L}\p{N}])-+(?=[\p{L}\p{N}])/gu,' ')
    .replace(/\uE000(\d+)\uE001/g, (_, i) => saved[Number(i)])
    .replace(/\s+/g,' ').trim();
  if (!text || text.includes(' ') || text.length < 14) return text;
  return text
    .replace(/([a-z0-9])([A-Z])/g, '$1 $2')
    .split(' ')
    .map((word) => TITLE_ACRONYMS[word] || word)
    .join(' ');
};
