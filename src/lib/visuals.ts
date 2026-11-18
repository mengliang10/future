export interface VisualConfig {
  color: string;
  pale: string;
  icon: string;
  short: string;
  weight?: string;
  change?: string;
}

// 1. Future Tech Visuals (Used across Explore, Roadmaps, Sectors, Index, Tags, Records)
export const techVisuals: Record<string, VisualConfig> = {
  'semiconductors': {color:'#2563eb', pale:'#eff6ff', icon:'▧', short:'Semiconductors'},
  'memory': {color:'#0284c7', pale:'#f0f9ff', icon:'▦', short:'Memory'},
  'quantum': {color:'#9333ea', pale:'#faf5ff', icon:'◎', short:'Quantum'},
  'drugs-biotech': {color:'#db2777', pale:'#fdf2f8', icon:'⌁', short:'Drugs & Biotech'},
  'llms-models': {color:'#4f46e5', pale:'#eef2ff', icon:'✳', short:'LLMs & Models'},
  'robotics': {color:'#ea580c', pale:'#fff7ed', icon:'⌘', short:'Robotics'},
  'bci': {color:'#e11d48', pale:'#fff1f2', icon:'⌇', short:'BCI'},
  'energy': {color:'#059669', pale:'#ecfdf5', icon:'⚡', short:'Energy & Power'},
  'autonomous': {color:'#0d9488', pale:'#f0fdfa', icon:'⇢', short:'Autonomous & AV'},
  'space': {color:'#0369a1', pale:'#f0f9ff', icon:'↗', short:'Space'},
  'cybersecurity': {color:'#d97706', pale:'#fffbeb', icon:'◇', short:'Cybersecurity'},
  'blockchain': {color:'#ca8a04', pale:'#fefce8', icon:'⬡', short:'Blockchain'},
  'spatial-computing': {color:'#c026d3', pale:'#fdf4ff', icon:'◈', short:'Spatial & XR'},
  'ai-agents-software': {color:'#6366f1', pale:'#eef2ff', icon:'⌥', short:'AI Agents'},
  'ai-infrastructure': {color:'#0891b2', pale:'#ecfeff', icon:'⌂', short:'AI Infrastructure'},
  'materials-physics': {color:'#475569', pale:'#f8fafc', icon:'❖', short:'Materials & Physics'},
  'applied-ai': {color:'#16a34a', pale:'#f0fdf4', icon:'≋', short:'Applied AI'}
};

// 2. Official Stock Sectors (Dedicated solely to Presentations Studio)
export const officialStockSectors: Record<string, VisualConfig> = {
  'information-technology': {color:'#3b82f6',pale:'#eff6ff',icon:'▧',short:'Info Tech',weight:'34%',change:'0.77%'},
  'financials': {color:'#059669',pale:'#ecfdf5',icon:'⌁',short:'Financials',weight:'12%',change:'1.87%'},
  'health-care': {color:'#ec4899',pale:'#fdf2f8',icon:'♥',short:'Health Care',weight:'11%',change:'1.37%'},
  'consumer-discretionary': {color:'#f59e0b',pale:'#fffbeb',icon:'◈',short:'Cons. Discretionary',weight:'10%',change:'0.56%'},
  'communication-services': {color:'#8b5cf6',pale:'#f5f3ff',icon:'↝',short:'Comm Services',weight:'9%',change:'1.30%'},
  'industrials': {color:'#d97706',pale:'#fffbe6',icon:'⌘',short:'Industrials',weight:'8%',change:'0.55%'},
  'consumer-staples': {color:'#84cc16',pale:'#f7fee7',icon:'⚘',short:'Cons. Staples',weight:'6%',change:'1.06%'},
  'energy': {color:'#10b981',pale:'#ecfdf5',icon:'↯',short:'Energy',weight:'4%',change:'0.53%'},
  'materials': {color:'#64748b',pale:'#f1f5f9',icon:'❖',short:'Materials',weight:'2%',change:'1.17%'},
  'real-estate': {color:'#06b6d4',pale:'#ecfeff',icon:'⌂',short:'Real Estate',weight:'2%',change:'1.40%'},
  'utilities': {color:'#14b8a6',pale:'#f0fdfa',icon:'⚡',short:'Utilities',weight:'2%',change:'1.60%'}
};

export const officialSectorsOrder = [
  'information-technology',
  'financials',
  'health-care',
  'consumer-discretionary',
  'communication-services',
  'industrials',
  'consumer-staples',
  'energy',
  'materials',
  'real-estate',
  'utilities'
];

export const futureTechOrder = [
  'semiconductors',
  'memory',
  'quantum',
  'drugs-biotech',
  'llms-models',
  'robotics',
  'bci',
  'energy',
  'autonomous',
  'space',
  'cybersecurity',
  'blockchain',
  'spatial-computing',
  'ai-agents-software',
  'ai-infrastructure',
  'materials-physics',
  'applied-ai'
];

export const visualFor = (id: string): VisualConfig => {
  return techVisuals[id] || officialStockSectors[id] || {color:'#718099', pale:'#eff2f7', icon:'◦', short:id, weight:'—', change:'—'};
};

export const officialVisualFor = (id: string): VisualConfig => {
  return officialStockSectors[id] || {color:'#718099', pale:'#eff2f7', icon:'◦', short:id, weight:'—', change:'—'};
};

export const horizons = [
  {id:'through-2028',label:'Through 2028',short:'≤2028',description:'Near-term source estimates',color:'#528b84'},
  {id:'2029-2030',label:'2029–2030',short:'2029–30',description:'The next source-estimated window',color:'#5677be'},
  {id:'2031-2040',label:'2031–2040',short:'2031–40',description:'Longer development windows',color:'#896ac0'},
  {id:'2041-2050',label:'2041–2050',short:'2041–50',description:'Long-range source estimates',color:'#b4778d'},
  {id:'beyond-2050',label:'Beyond 2050',short:'2051+',description:'Distant source estimates',color:'#ba8b52'},
  {id:'unspecified',label:'No recorded year',short:'No year',description:'No numeric year in the source record',color:'#85909f'}
];

export function horizonFor(year: number | null | undefined) {
  if(year===null||year===undefined)return 'unspecified';
  if(year<=2028)return 'through-2028';
  if(year<=2030)return '2029-2030';
  if(year<=2040)return '2031-2040';
  if(year<=2050)return '2041-2050';
  return 'beyond-2050';
}

export const stageGroup = (stage: string) =>
  ['basic_research','proof_of_concept'].includes(stage)?'research':
  ['prototype','prototyping','pilot'].includes(stage)?'development':
  ['early_commercial','mass_production','early_adoption'].includes(stage)?'commercial':'other';
