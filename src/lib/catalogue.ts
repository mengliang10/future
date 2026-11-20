import {getCollection} from 'astro:content';
export const records=async name=>(await getCollection(name)).map(entry=>({...entry.data,id:entry.id}));
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
  const text = String(value || '');
  if (!text || text.includes(' ') || text.length < 14) return text;
  return text
    .replace(/([a-z0-9])([A-Z])/g, '$1 $2')
    .split(' ')
    .map((word) => TITLE_ACRONYMS[word] || word)
    .join(' ');
};
