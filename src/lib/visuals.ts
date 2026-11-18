export const sectorVisuals={
 ai:{color:'#5365d9',pale:'#eff0ff',icon:'✳',short:'AI & Computing'},
 semiconductors:{color:'#278b9e',pale:'#e8f6fa',icon:'▧',short:'Semiconductors'},
 quantum:{color:'#9664c5',pale:'#f3ecfc',icon:'◎',short:'Quantum'},
 robotics:{color:'#d07845',pale:'#fff0e6',icon:'⌘',short:'Robotics'},
 energy:{color:'#38967b',pale:'#e8f6ed',icon:'↯',short:'Energy'},
 biotech:{color:'#cd6889',pale:'#fcecf2',icon:'⌁',short:'Biotech & Health'},
 space:{color:'#637cbd',pale:'#edf1fb',icon:'↗',short:'Space'},
 cyber:{color:'#b48331',pale:'#fcf3e1',icon:'◇',short:'Cybersecurity'},
 autonomous:{color:'#358e9d',pale:'#e9f5f7',icon:'⇢',short:'Autonomous'},
 blockchain:{color:'#858443',pale:'#f5f4e5',icon:'⬡',short:'Blockchain'},
 xr:{color:'#a65fa0',pale:'#f8ecf7',icon:'◈',short:'Spatial Computing'},
 bci:{color:'#b76966',pale:'#fbefed',icon:'⌇',short:'Brain Interfaces'},
 marketing:{color:'#bf7042',pale:'#fff0e7',icon:'↝',short:'Marketing Tech'},
 policy:{color:'#678879',pale:'#edf3ef',icon:'≋',short:'Policy & Society'},
 markets:{color:'#657ec3',pale:'#edf1fb',icon:'⌁',short:'Financial Infrastructure'}
};
export const visualFor=(id)=>sectorVisuals[id]||{color:'#718099',pale:'#eff2f7',icon:'◦',short:id};
export const horizons=[
 {id:'through-2028',label:'Through 2028',short:'≤2028',description:'Near-term source estimates',color:'#528b84'},
 {id:'2029-2030',label:'2029–2030',short:'2029–30',description:'The next source-estimated window',color:'#5677be'},
 {id:'2031-2040',label:'2031–2040',short:'2031–40',description:'Longer development windows',color:'#896ac0'},
 {id:'2041-2050',label:'2041–2050',short:'2041–50',description:'Long-range source estimates',color:'#b4778d'},
 {id:'beyond-2050',label:'Beyond 2050',short:'2051+',description:'Distant source estimates',color:'#ba8b52'},
 {id:'unspecified',label:'No recorded year',short:'No year',description:'No numeric year in the source record',color:'#85909f'}
];
export function horizonFor(year){if(year===null||year===undefined)return 'unspecified';if(year<=2028)return 'through-2028';if(year<=2030)return '2029-2030';if(year<=2040)return '2031-2040';if(year<=2050)return '2041-2050';return 'beyond-2050';}
export const stageGroup=stage=>['basic_research','proof_of_concept'].includes(stage)?'research':['prototype','prototyping','pilot'].includes(stage)?'development':['early_commercial','mass_production','early_adoption'].includes(stage)?'commercial':'other';
