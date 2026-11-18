import glob, json, os, re
from collections import Counter

TECH_CATEGORIES = [
    {
        "id": "semiconductors",
        "title": "Semiconductors & Process Nodes",
        "short": "Semiconductors",
        "icon": "▧",
        "color": "#2563eb",
        "pale": "#eff6ff",
        "businessQuestion": "Which foundry constraints and packaging bottlenecks limit the next silicon generation?",
        "investorQuestion": "Where does gross margin accrue between lithography monopolies, fabs, and fabless designers?"
    },
    {
        "id": "memory",
        "title": "Memory & Storage Architectures",
        "short": "Memory",
        "icon": "▦",
        "color": "#0284c7",
        "pale": "#f0f9ff",
        "businessQuestion": "How does memory bandwidth scaling decouple compute performance from cost?",
        "investorQuestion": "Which memory architectures (HBM, 3D NAND, CXL) capture structural pricing premiums?"
    },
    {
        "id": "quantum",
        "title": "Quantum Computing & Sensing",
        "short": "Quantum",
        "icon": "◎",
        "color": "#9333ea",
        "pale": "#faf5ff",
        "businessQuestion": "What computational problems achieve genuine quantum utility before full error correction?",
        "investorQuestion": "Which qubit modality and cryogenic stack offers the lowest cost per logical qubit?"
    },
    {
        "id": "drugs-biotech",
        "title": "Drugs, Biotech & Longevity",
        "short": "Drugs & Biotech",
        "icon": "⌁",
        "color": "#db2777",
        "pale": "#fdf2f8",
        "businessQuestion": "How does generative molecular design compress clinical trial cycle time and failure rates?",
        "investorQuestion": "Who owns target exclusivity and intellectual property in AI-generated biologics?"
    },
    {
        "id": "llms-models",
        "title": "LLM Models & Generative AI",
        "short": "LLMs & Models",
        "icon": "✳",
        "color": "#4f46e5",
        "pale": "#eef2ff",
        "businessQuestion": "How do reasoning models and synthetic data generation alter enterprise software cost?",
        "investorQuestion": "Where does economic rent settle: foundational model weights, specialized fine-tunes, or apps?"
    },
    {
        "id": "robotics",
        "title": "Robotics & Embodied AI",
        "short": "Robotics",
        "icon": "⌘",
        "color": "#ea580c",
        "pale": "#fff7ed",
        "businessQuestion": "When do general-purpose humanoid actuators achieve payback against human wage parity?",
        "investorQuestion": "Which hardware subsystem (actuators, harmonics, sensors, vision-language-action models) holds pricing power?"
    },
    {
        "id": "bci",
        "title": "Brain–Computer Interfaces",
        "short": "BCI",
        "icon": "⌇",
        "color": "#e11d48",
        "pale": "#fff1f2",
        "businessQuestion": "What medical indications clear regulatory pathways before consumer neural telemetry arrives?",
        "investorQuestion": "Can non-invasive signal acquisition achieve clinical fidelity without implant risk?"
    },
    {
        "id": "energy",
        "title": "Energy & Power Systems",
        "short": "Energy & Power",
        "icon": "⚡",
        "color": "#059669",
        "pale": "#ecfdf5",
        "businessQuestion": "How quickly can baseload clean energy (SMRs, fusion, grid batteries) meet data center load growth?",
        "investorQuestion": "Which energy producers command premium long-term power purchase agreements (PPAs)?"
    },
    {
        "id": "autonomous",
        "title": "Autonomous Vehicles & Mobility",
        "short": "Autonomous & AV",
        "icon": "⇢",
        "color": "#0d9488",
        "pale": "#f0fdfa",
        "businessQuestion": "What sensor fusion mix delivers commercial safety verification at mass scale?",
        "investorQuestion": "How does robotaxi fleet economics reshape automotive OEM unit sales and software subscriptions?"
    },
    {
        "id": "space",
        "title": "Space Economy & Aerospace",
        "short": "Space",
        "icon": "↗",
        "color": "#0369a1",
        "pale": "#f0f9ff",
        "businessQuestion": "How does sub-$100/kg launch pricing unlock manufacturing and orbital compute?",
        "investorQuestion": "Which satellite constellations generate recurring terrestrial connectivity revenues?"
    },
    {
        "id": "cybersecurity",
        "title": "Cybersecurity & Zero Trust",
        "short": "Cybersecurity",
        "icon": "◇",
        "color": "#d97706",
        "pale": "#fffbeb",
        "businessQuestion": "How do automated agent exploits force transition to continuous cryptanalytic architectures?",
        "investorQuestion": "Which security platforms consolidate enterprise spend across identity, network, and endpoints?"
    },
    {
        "id": "blockchain",
        "title": "Blockchain & Web3",
        "short": "Blockchain",
        "icon": "⬡",
        "color": "#ca8a04",
        "pale": "#fefce8",
        "businessQuestion": "What settlement efficiency gains justify moving physical assets and bank deposits on-chain?",
        "investorQuestion": "Where does value accrue: base settlement layers, execution rollups, or regulated issuers?"
    },
    {
        "id": "spatial-computing",
        "title": "Spatial Computing & XR",
        "short": "Spatial & XR",
        "icon": "◈",
        "color": "#c026d3",
        "pale": "#fdf4ff",
        "businessQuestion": "What optical and display breakthrough enables all-day consumer smart glasses wearability?",
        "investorQuestion": "Which component makers dominate micro-OLED, optical waveguides, and spatial sensor pipelines?"
    },
    {
        "id": "ai-agents-software",
        "title": "AI Agents & Software Engineering",
        "short": "AI Agents",
        "icon": "⌥",
        "color": "#6366f1",
        "pale": "#eef2ff",
        "businessQuestion": "How does autonomous code generation and verification compress software engineering overhead?",
        "investorQuestion": "Do developer tools convert seat-based software licences into work-completed compute billings?"
    },
    {
        "id": "ai-infrastructure",
        "title": "AI Infrastructure & Compute",
        "short": "AI Infrastructure",
        "icon": "⌂",
        "color": "#0891b2",
        "pale": "#ecfeff",
        "businessQuestion": "What thermal density and cluster networking limits dictate gigawatt-scale data center design?",
        "investorQuestion": "Who captures sustained margin: custom accelerator designers, server integrators, or optical transceivers?"
    },
    {
        "id": "materials-physics",
        "title": "Advanced Materials & Physics",
        "short": "Materials & Physics",
        "icon": "❖",
        "color": "#475569",
        "pale": "#f8fafc",
        "businessQuestion": "How does AI-accelerated crystal and catalyst discovery shorten materials commercialization?",
        "investorQuestion": "Which specialty material formulations hold un-commoditized supply chain positions?"
    },
    {
        "id": "applied-ai",
        "title": "Applied AI & Emerging Tech",
        "short": "Applied AI",
        "icon": "≋",
        "color": "#16a34a",
        "pale": "#f0fdf4",
        "businessQuestion": "What practical workflows deliver measurable productivity before market saturation?",
        "investorQuestion": "Which domain-specific workflows erect sustainable data moats against generic frontier models?"
    }
]

def categorize_technology(d):
    sc = d.get('sourceCategory', '')
    title = (d.get('title') or '').lower()
    slug = d.get('id', '').lower()
    summary = (d.get('summary') or '').lower()
    text = f"{title} {slug} {summary}"

    # 1. Quantum Computing
    if sc in ['Quantum', 'Quantum Computing'] or any(w in text for w in [
        'qubit', 'quantum', 'neutral-atom', 'ionq', 'quantum-computing', 'quantum computing', 
        'superconducting-qubit', 'quantum sensing', 'topological qubit', 'photonic qubit', 'trapped-ion'
    ]):
        return 'quantum'

    # 2. Memory & Advanced Storage
    if any(w in text for w in [
        'hbm', 'dram', '3d nand', '3d-nand', 'nand flash', 'cxl memory', 'memory bandwidth', 
        'memory-pooled', 'optical storage', 'dna data storage', 'dna storage', 'storage class memory', 
        'phase-change memory', 'rram', 'mram', 'ferroelectric', 'memory semiconductor', 'memory-storage',
        'solid-state storage', 'flash memory'
    ]):
        return 'memory'

    # 3. Semiconductors & Process Nodes
    if sc in ['Semiconductors', 'Hardware'] or any(w in text for w in [
        'semiconductor', 'process node', 'transistor', 'gaafet', 'finfet', 'euv', 'lithography', 
        'hybrid bonding', 'cowos', 'advanced packaging', 'chiplet', 'wafer', 'photonic chip', 
        'silicon photonics', 'asic', 'tpu', 'npu', 'interconnect', 'spintronics', 'gallium nitride',
        'silicon carbide', 'metrology', 'backside power', 'interposer', 'wfe', '18a', '14a', 'tsmc',
        'foundry', 'sub-nanometer', 'high-na', 'packaging', 'chip design', 'chipbook', 'fab'
    ]):
        return 'semiconductors'

    # 4. Drugs, Biotech & Longevity
    if sc in ['Biotech', 'Biotech & Healthcare'] or any(w in text for w in [
        'drug', 'mrna', 'crispr', 'gene editing', 'gene therapy', 'cancer', 'car-t', 'protein design',
        'clinical trials', 'antibody', 'genom', 'longevity', 'aging reversal', 'cell therapy', 
        'biomarker', 'vaccine', 'molecular', 'in-vivo', 'proteomics', 'sequencing', 'therapeutics',
        'therapeutic', 'disease', 'xenotransplantation', 'rna', 'biological', 'microbiome',
        'biotech', 'immune response', 'tissue-regeneration'
    ]):
        return 'drugs-biotech'

    # 5. LLMs, Foundation Models & Generative AI
    if any(w in text for w in [
        'llm', 'language model', 'gpt', 'transformer architecture', 'reasoning model', 'foundation model', 
        'multimodal model', 'diffusion model', 'world model', 'generative ai', 'prompt', 'text-to-',
        'context window', 'synthetic data training', 'distillation', 'chain-of-thought', 'rlhf',
        'decoding', 'chatbot', 'token generation', 'claude', 'deepseek', 'open-weight model', 'gpt-4'
    ]):
        return 'llms-models'

    # 6. Brain-Computer Interfaces (BCI) & Neurotech
    if sc == 'BCI' or any(w in text for w in [
        'bci', 'neural interface', 'brain-computer', 'neuralink', 'neural decoding', 'eeg', 
        'electrocorticography', 'neurotechnology', 'brain-to-text', 'gut-brain', 'invasive-bci'
    ]):
        return 'bci'

    # 7. Robotics & Physical Automation
    if sc in ['Robotics', 'Robotics & Automation'] or any(w in text for w in [
        'humanoid', 'robot', 'robotic', 'actuator', 'bipedal', 'manipulator', 'embodied ai', 
        'factory automation', 'quadruped', 'dexterous', 'robotic arm'
    ]):
        return 'robotics'

    # 8. Autonomous Systems & Mobility
    if sc == 'Autonomous' or any(w in text for w in [
        'autonomous vehicle', 'robotaxi', 'full self-driving', 'fsd', 'lidar', 'adas', 
        'sensor fusion', 'vehicle-to-everything', 'v2x', 'wayve', 'self-driving', 'zero-accident'
    ]):
        return 'autonomous'

    # 9. Energy & Power Systems
    if sc == 'Energy Tech' or any(w in text for w in [
        'fusion', 'nuclear', 'reactor', 'battery', 'solar', 'grid', 'hydrogen', 'geothermal', 
        'smr', 'clean energy', 'perovskite', 'electrocatalysis', 'power demand', 'waste heat', 
        'energy storage', 'sodium-ion', 'solid-state battery'
    ]):
        return 'energy'

    # 10. Space & Aerospace
    if sc == 'Space Tech' or any(w in text for w in [
        'satellite', 'rocket', 'launch', 'lunar', 'orbit', 'space station', 'starship', 'mars', 
        'propulsion', 'spacecraft', 'leo constellation', 'tiangong', 'in-space manufacturing'
    ]):
        return 'space'

    # 11. Cybersecurity & Zero Trust
    if sc == 'Cybersecurity' or any(w in text for w in [
        'cybersecurity', 'zero trust', 'cryptography', 'post-quantum crypto', 'ransomware', 
        'threat detection', 'xdr', 'edr', 'homomorphic encryption', 'vulnerability', 'endpoint detection'
    ]):
        return 'cybersecurity'

    # 12. Blockchain & Web3
    if sc in ['Blockchain', 'Blockchain & Crypto'] or any(w in text for w in [
        'blockchain', 'ethereum', 'smart contract', 'zero-knowledge', 'zk-rollup', 'defi', 
        'tokeniz', 'web3', 'cryptocurrency', 'bitcoin', 'rwa'
    ]):
        return 'blockchain'

    # 13. Spatial Computing & XR
    if sc == 'XR' or any(w in text for w in [
        'augmented reality', 'virtual reality', 'mixed reality', 'smart glasses', 'spatial computing', 
        'headset', 'microled display', 'oled display', 'optics', 'ar glasses', 'vr headset', 'display panel'
    ]):
        return 'spatial-computing'

    # 14. AI Agents & Software Engineering
    if any(w in text for w in [
        'agent', 'workflow', 'software engineer', 'developer tool', 'automation platform', 
        'copilot', 'coding', 'code generation', 'verification', 'rtl verification'
    ]):
        return 'ai-agents-software'

    # 15. Advanced Materials & Physics
    if any(w in text for w in [
        'material', 'superconductor', 'catalysis', 'crystal', 'graphene', '2d materials', 
        'magnetic', 'nanoparticle', 'metamaterial', 'spectroscopy'
    ]):
        return 'materials-physics'

    # 16. AI Infrastructure & Compute
    if any(w in text for w in [
        'compute', 'datacenter', 'data center', 'cluster', 'networking', 'megawatt', 
        'stargate', 'rack', 'supercomputer'
    ]):
        return 'ai-infrastructure'

    return 'applied-ai'

def categorize_company(d):
    cid = d.get('id', '').lower()
    title = (d.get('title') or '').lower()
    sc = d.get('sourceCategory', '').lower()
    meta_cats = " ".join([c.lower() for c in d.get('sourceMeta', {}).get('categories', [])])
    
    # Specific ID mappings
    if cid in ['1x.pvt', 'agibot.pvt', 'figure.pvt', 'unitree.pvt', 'doosan-robotics.kr', 'fanuc.jp', 'abb', 'sym', 'rok', 'cgnx', 'ter']:
        return 'robotics'
    if cid in ['isrg']:
        return 'drugs-biotech'
    if cid in ['tsla', 'mbly', 'aur', 'lazr', 'hesai.us']:
        return 'autonomous'
    if cid in ['joby', 'rklb', 'asts', 'lunr', 'spacex.us', 'blue-origin.us', 'blue.pvt', 'relativity.us', 'ula.us', 'firefly.us', 'ispace.jp', 'astroscale.jp', 'ohb.de', 'avio.it', 'ariane-group.fr', 'bksy', 'pl.us', 'viasat.us', 'irdm.us']:
        return 'space'
    if cid in ['ionq', 'rgti', 'd-wave', 'quantinuum.us', 'psiquantum.us', 'alice-bob.fr', 'atom-computing.us', 'photonic-inc.ca', 'xanadu.ca', 'iqm.fi', 'quantum-machines.il', 'zurich-instruments.ch', 'bluefors.fi', 'oxford-instruments.uk', 'montana-instruments.us']:
        return 'quantum'
    if cid in ['mu', 'wdc', 'sk-hynix.kr', 'kioxia.jp', 'samsung-electronics.kr']:
        return 'memory'
    if cid in ['crwd', 's', 'panw', 'zs', 'net', 'ftnt', 'cybr', 'tenable.us', 'rapid7.us', 'varonis.us', 'qualys.us']:
        return 'cybersecurity'
    if cid in ['coin', 'mstr', 'mara', 'clsk', 'hut', 'bitfarms.ca', 'cipher.us', 'iris-energy.us', 'core-scientific.us']:
        return 'blockchain'
    if cid in ['anth.pvt', 'openai.pvt', 'deepseek.pvt', 'cohere.ca', 'mistral.fr']:
        return 'llms-models'
    if cid in ['pltr', 'crm', 'now', 'ddog', 'path', 'c3.ai', 'appian.us']:
        return 'ai-agents-software'
    if cid in ['vrt', 'smci', 'anet', 'dell', 'hpe', 'schneider-electric.fr', 'etn', 'pwr']:
        return 'ai-infrastructure'
    if cid in ['ceg', 'vst', 'nee', 'smr', 'oklo.us', 'ccj', 'gev', 'fslr', 'enphase.us', 'nrg', 'terrapower.us', 'x-energy.us', 'helion.us', 'commonwealth-fusion.us', 'type-one-energy.us', 'first-light-fusion.uk', 'general-fusion.ca', 'tokamak-energy.uk', 'realta-fusion.us', 'zap-energy.us']:
        return 'energy'

    text = f"{title} {cid} {sc} {meta_cats}"

    # Quantum
    if 'quantum' in text or 'qubit' in text:
        return 'quantum'

    # Memory
    if any(w in text for w in ['hbm', 'dram', 'nand', 'memory']):
        return 'memory'

    # Drugs & Biotech
    if any(w in text for w in ['pharma', 'biotech', 'biopharma', 'crispr', 'mrna', 'therapeutics', 'cancer', 'novartis', 'roche', 'pfizer', 'moderna', 'biontech', 'illumina', 'regeneron', 'vertex', 'genomics', 'drug discovery', 'biology', 'cell therapy']):
        return 'drugs-biotech'

    # BCI
    if any(w in text for w in ['bci', 'neuralink', 'brain-computer', 'neural interface', 'synchron', 'blackrock neuro']):
        return 'bci'

    # Robotics
    if any(w in text for w in ['robotics', 'humanoid', 'automation', 'yaskawa', 'kuka']):
        return 'robotics'

    # Autonomous
    if any(w in text for w in ['autonomous vehicle', 'robotaxi', 'lidar', 'mobileye', 'waymo']):
        return 'autonomous'

    # Energy
    if any(w in text for w in ['nuclear', 'smr', 'fusion', 'clean energy', 'battery', 'uranium', 'solar', 'power generation', 'power']):
        return 'energy'

    # Space
    if any(w in text for w in ['satellite', 'rocket', 'launch', 'aerospace', 'space']):
        return 'space'

    # Cyber
    if any(w in text for w in ['cybersecurity', 'security', 'threat detection']):
        return 'cybersecurity'

    # Crypto / Blockchain
    if any(w in text for w in ['crypto', 'blockchain', 'bitcoin']):
        return 'blockchain'

    # Spatial Computing
    if any(w in text for w in ['augmented reality', 'virtual reality', 'microled', 'oled display', 'display panel']):
        return 'spatial-computing'

    # Semiconductors
    if any(w in text for w in ['semiconductor', 'foundry', 'lithography', 'wafer', 'chiplet', 'packaging', 'metrology', 'tsmc', 'asml', 'kla', 'lam', 'applied materials']):
        return 'semiconductors'

    # Materials
    if any(w in text for w in ['materials', 'chemical', 'shin-etsu', 'sumco', 'air liquide', 'linde']):
        return 'materials-physics'

    return 'applied-ai'

# Main generation
def main():
    root = "/media/ml/Storage1/The Future Tomorrow"
    sectors_dir = os.path.join(root, "src/content/sectors")
    
    # 1. Write sector JSON files
    print(f"Writing {len(TECH_CATEGORIES)} sector files to {sectors_dir}...")
    for cat in TECH_CATEGORIES:
        path = os.path.join(sectors_dir, f"{cat['id']}.json")
        data = {
            "id": cat["id"],
            "title": cat["title"],
            "short": cat["short"],
            "aliases": [cat["short"], cat["title"]],
            "businessQuestion": cat["businessQuestion"],
            "investorQuestion": cat["investorQuestion"]
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    # Remove old official sectors that are not in TECH_CATEGORIES
    active_ids = {c["id"] for c in TECH_CATEGORIES}
    for old_file in glob.glob(os.path.join(sectors_dir, "*.json")):
        basename = os.path.basename(old_file)[:-5]
        if basename not in active_ids:
            print(f"Removing old sector file: {basename}.json")
            os.remove(old_file)

    # 2. Update technologies
    tech_files = glob.glob(os.path.join(root, "src/content/technologies/*.json"))
    print(f"Updating {len(tech_files)} technology files with Future Tech categories...")
    tech_counts = Counter()
    for f in tech_files:
        with open(f, "r", encoding="utf-8") as tf:
            d = json.load(tf)
        cat = categorize_technology(d)
        d["sector"] = cat
        tech_counts[cat] += 1
        with open(f, "w", encoding="utf-8") as tf:
            json.dump(d, tf, indent=2)

    print("\nTechnologies assigned:")
    for cid, cnt in tech_counts.most_common():
        print(f"  {cnt:3d}  {cid}")

    # 3. Update companies
    comp_files = glob.glob(os.path.join(root, "src/content/companies/*.json"))
    print(f"\nUpdating {len(comp_files)} company files with Future Tech categories...")
    comp_counts = Counter()
    for f in comp_files:
        with open(f, "r", encoding="utf-8") as cf:
            d = json.load(cf)
        cat = categorize_company(d)
        d["sector"] = cat
        comp_counts[cat] += 1
        with open(f, "w", encoding="utf-8") as cf:
            json.dump(d, cf, indent=2)

    print("\nCompanies assigned:")
    for cid, cnt in comp_counts.most_common():
        print(f"  {cnt:3d}  {cid}")

    print("\nDone generating Future Tech taxonomy!")

if __name__ == "__main__":
    main()
