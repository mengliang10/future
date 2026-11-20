#!/usr/bin/env python3
"""Author the 11 official stock-sector briefing decks.

Each deck replaces the generic placeholder slide list with 13 authored slides and
five inline SVG diagrams (impact map, exposure bars, supply-chain products,
technology stack, adoption timeline). Run from the project root:

    python3 scripts/build-sector-briefing-decks.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DECKS = ROOT / "src/content/decks"

def impact(quadrants):
    return {"kind": "impact", "quadrants": quadrants}

def bars(caption, rows):
    return {"kind": "bars", "caption": caption,
            "bars": [{"label": l, "pct": p} for l, p in rows]}

def chain(caption, stages, note):
    return {"kind": "chain", "caption": caption,
            "stages": [{"label": l, "products": p} for l, p in stages], "note": note}

def stack(layers):
    return {"kind": "stack",
            "layers": [{"label": l, "note": n, "items": i} for l, n, i in layers]}

def timeline(ms):
    return {"kind": "timeline",
            "milestones": [{"year": y, "label": l, "detail": d, "lane": lane} for y, l, d, lane in ms]}

def table(head, rows):
    return {"head": head, "rows": rows}

SECTORS = [
{
 "deck": "information-technology-01",
 "title": "Information Technology — How future technology reshapes the sector",
 "thesis": "The sector sells compute, software and the people who wire them together. AI changes all three at once: it expands the compute bill, compresses the software seat, and automates the integration work that services firms bill by the hour. The question is not whether demand grows, but which layer captures the surplus when compute is scarce and code is cheap.",
 "econ": "Four very different businesses sit inside one sector label: cyclical capital equipment, low-margin hardware assembly, high-gross-margin software, and people-based services.",
 "econBullets": [
   "Semiconductors earn on unit volume and node leadership; utilisation and depreciation dominate the cycle.",
   "Hardware assembly earns thin spreads and is valued on cash conversion, not growth.",
   "Software earns 75–90% gross margins on seats and maintenance, with low marginal cost per user.",
   "IT services earn on billable headcount; utilisation and pyramid leverage set the margin.",
   "Cloud infrastructure sits between: capital-hungry, but with usage-based revenue that compounds."
 ],
 "impact": impact([
   {"label": "New revenue, contested", "items": ["Accelerators, HBM and networking sold into AI clusters", "Inference capacity resold as a metered service", "Custom silicon programmes for hyperscalers"]},
   {"label": "New revenue, durable", "items": ["Agent platforms that charge per completed task", "Data and evaluation layers that models cannot commoditise", "Security and governance for machine identities"]},
   {"label": "Cost takeout, fast", "items": ["Coding assistants reduce engineering hours per release", "Automated support deflects tier-one tickets", "AI-assisted EDA and yield analysis shorten cycles"]},
   {"label": "Structural cost shift", "items": ["Fab and packaging capex per wafer starts to rise again", "Power and cooling become a siting constraint", "Depreciation schedules lengthen the payback on AI fleets"]}
 ]),
 "bars": bars("Directional exposure of each pool to the AI shift", [
   ("AI-related compute and networking spend", 45),
   ("Software maintenance and seat revenue", 35),
   ("Services revenue priced on headcount", 60),
   ("Hardware assembly margin", 20),
   ("On-premise refresh budget", 30)
 ]),
 "chain": chain("Upstream materials → fabricated silicon → systems → platforms → enterprise workflows",
   [("Materials & tools", ["EUV photoresist", "300mm wafers", "Advanced packaging substrate", "Ultra-pure gases"]),
    ("Fabrication & memory", ["2nm logic die", "HBM4 stacks", "CoWoS packaging", "Power delivery chips"]),
    ("Systems", ["GPU racks", "Optical interconnect", "Liquid cooling", "Custom accelerators"]),
    ("Platforms", ["Frontier model APIs", "Open-weight models", "Vector and eval services", "Sovereign clouds"]),
    ("Workflows", ["Coding agents", "Support agents", "Analyst copilots", "Design and simulation"])],
   "The scarce links are packaging, memory bandwidth and power — not the model itself. That is where pricing power currently sits."),
 "clusters": [
   {"title": "Compute and packaging", "body": "Demand is moving from chips to systems: rack-scale design, memory bandwidth and thermal limits decide who can ship.",
    "items": ["2nm and gate-all-around ramps", "HBM4 and hybrid bonding", "Co-packaged optics", "Liquid cooling at rack scale"]},
   {"title": "Models and agents", "body": "Capability is converging across labs, so distribution, evaluation and cost per task become the differentiators.",
    "items": ["Mixture-of-experts serving", "Long-context retrieval", "Agent orchestration and tool use", "Open-weight commoditisation"]},
   {"title": "Software economics", "body": "Per-seat pricing weakens when agents do the work; vendors experiment with consumption and outcome pricing.",
    "items": ["Outcome-based pricing", "Usage-based infrastructure", "AI-native application rebuilds", "Maintenance revenue erosion"]}
 ],
 "stack": stack([
   ("Physical", "Fabs, power, water", ["Wafer capacity", "Advanced packaging", "Substations", "Cooling plant"]),
   ("Compute", "Silicon and interconnect", ["GPUs and TPUs", "HBM stacks", "Optical links", "DPUs and NICs"]),
   ("Models", "Training and serving", ["Frontier APIs", "Open weights", "Fine-tunes", "Evaluation suites"]),
   ("Products", "Where users pay", ["Coding agents", "Copilots", "Data platforms", "Security tools"])
 ]),
 "timeline": timeline([
   (2026, "Inference cost falls again", "Serving efficiency improves faster than prices", 0),
   (2027, "Agent platforms mature", "Tool use and evaluation become standard", 0),
   (2028, "2nm volume ramp", "Packaging and memory remain the bottleneck", 1),
   (2029, "Co-packaged optics", "Optical I/O moves inside the rack", 1),
   (2031, "Hybrid quantum pilots", "Niche optimisation alongside classical HPC", 2),
   (2033, "Angstrom-era limits", "New transistor and materials choices", 2)
 ]),
 "table": table(["P&L line", "Mechanism", "Timing", "Proof point"], [
   ["Cloud capex", "AI clusters absorb a rising share of infrastructure spend", "Now → 2028", "Capex guidance vs depreciation life"],
   ["Software revenue", "Seats shrink, consumption and agents grow", "2026 → 2029", "Net revenue retention by pricing model"],
   ["Services margin", "Delivery automation cuts billable hours", "Now → 2027", "Utilisation and revenue per head"],
   ["Silicon content", "More accelerators, memory and optics per system", "Now → 2029", "Content per rack, not units"],
   ["Memory pricing", "HBM tightness spills into conventional DRAM", "Cyclical", "Contract prices and capacity adds"]
 ]),
 "gain": [
   "Owners of scarce capacity: leading-edge fabs, HBM suppliers, advanced packaging and optical interconnect.",
   "Platforms with proprietary data and distribution, because model capability alone is converging.",
   "Software vendors that can meter work rather than seats without losing gross margin.",
   "Services firms that productise delivery and redeploy headcount to higher-value programmes.",
   "Power-adjacent suppliers: electrical equipment, cooling and grid interconnection."
 ],
 "exposed": [
   "Resellers and assemblers with no IP, squeezed between component costs and customer budgets.",
   "Seat-based software with shallow workflow lock-in as agents absorb routine tasks.",
   "Services firms whose revenue is a function of junior headcount.",
   "Legacy on-premise hardware refresh cycles that lose budget to AI infrastructure.",
   "Late followers in leading-edge logic with insufficient scale and yield learning."
 ],
 "watch": [
   "<strong>Memory contract pricing</strong> — the cleanest read on whether AI demand is real or pre-built.",
   "<strong>Depreciation lives</strong> — shorter useful lives would signal an asset-heavy bubble, longer lives the opposite.",
   "<strong>Software net revenue retention</strong> split by pricing model, not blended.",
   "<strong>Agent completion rates</strong> in production, not benchmark scores.",
   "<strong>Export-control scope</strong> and its effect on addressable market for accelerators."
 ],
 "research": "This deck synthesises the technology records linked below. Each record carries its own confidence label and source path; none of the scenario language here is a forecast or a price target."
},
{
 "deck": "financials-01",
 "title": "Financials — How future technology reshapes the sector",
 "thesis": "Banks, insurers and asset managers are information processors with a licence. AI attacks the cost of processing and the value of intermediation at the same time. The near-term prize is a lower cost/income ratio; the strategic risk is that payments, advice and underwriting get embedded in someone else's agent interface.",
 "econ": "Revenue comes from spread, fees and float; cost comes from people, legacy systems and regulation. Small changes in either line move returns on equity enormously.",
 "econBullets": [
   "Net interest income is a spread business: deposit beta and loan pricing matter more than volume.",
   "Fee pools — payments, advisory, asset management, insurance underwriting — carry higher multiples than spread income.",
   "Cost/income ratios of 50–65% leave large absolute cost bases exposed to automation.",
   "Capital and liquidity rules cap leverage, so efficiency and fee mix drive returns.",
   "Trust, distribution and licences are the moat; neither is easily automated."
 ],
 "impact": impact([
   {"label": "New revenue, contested", "items": ["Embedded finance inside agent interfaces", "Tokenised funds and private credit wrappers", "Usage-priced risk and compliance APIs"]},
   {"label": "New revenue, durable", "items": ["Proprietary data sold as underwriting signals", "Wealth advice for mass-affluent segments", "Cross-border payment rails with FX spread"]},
   {"label": "Cost takeout, fast", "items": ["Contact-centre deflection and agent assist", "KYC, reconciliation and reporting automation", "Claims triage and document extraction"]},
   {"label": "Structural cost shift", "items": ["Legacy core replacement becomes urgent", "Model risk and audit costs rise", "Fraud and deepfake defence spending"]}
 ]),
 "bars": bars("Directional share of each pool exposed to automation or disintermediation", [
   ("Back-office processing cost", 55),
   ("Retail payments fee pool", 40),
   ("Underwriting and claims handling", 50),
   ("Advisory and asset-management fees", 30),
   ("Compliance and reporting cost", 45)
 ]),
 "chain": chain("Deposits and data → risk engines → products → rails → client interface",
   [("Deposits & data", ["Core ledger", "Transaction data", "KYC profiles", "Collateral records"]),
    ("Risk & pricing", ["Credit models", "Fraud scoring", "Actuarial engines", "Market risk"]),
    ("Products", ["Cards and loans", "Deposits and funds", "Insurance policies", "Tokenised assets"]),
    ("Rails", ["Card networks", "ACH and RTP", "Stablecoin settlement", "Tokenised deposits"]),
    ("Interface", ["Mobile app", "Advisor desktop", "Embedded partner", "AI assistant"])],
   "The interface is where margin migrates. If an assistant owns the customer, the bank becomes a licensed balance-sheet utility behind it."),
 "clusters": [
   {"title": "Agentic distribution", "body": "Customers delegate shopping and admin to assistants, so products must be discoverable and transactable by machine.",
    "items": ["Agentic checkout and mandates", "API product catalogues", "Real-time pricing", "Identity and consent"]},
   {"title": "Tokenised rails", "body": "Stablecoins and tokenised deposits compress settlement from days to seconds and create new deposit substitutes.",
    "items": ["Stablecoin regulation", "Tokenised bank deposits", "Tokenised money-market funds", "24/7 settlement"]},
   {"title": "Risk automation", "body": "Underwriting and fraud move from annual review to continuous scoring, with model governance as the constraint.",
    "items": ["Alternative-data credit", "Deepfake and fraud detection", "Claims automation", "Model risk management"]}
 ],
 "stack": stack([
   ("Core", "Ledgers and capital", ["Core banking", "Policy admin", "Fund accounting", "Capital reporting"]),
   ("Data", "Records and signals", ["Transaction data", "Market data", "Alt-data", "Audit trails"]),
   ("Models", "Decisioning", ["Credit models", "Fraud models", "Actuarial models", "Advisory agents"]),
   ("Interface", "Where clients act", ["Mobile app", "Advisor tools", "Embedded APIs", "Agent endpoints"])
 ]),
 "timeline": timeline([
   (2026, "Stablecoin rules bite", "Licensed issuance and reserve rules", 0),
   (2027, "Tokenised deposits pilot", "Bank-issued settlement tokens", 0),
   (2028, "Agentic checkout scales", "Machine-initiated payments with mandates", 1),
   (2029, "Tokenised funds mainstream", "Same-day settlement for funds", 1),
   (2031, "Continuous underwriting", "Real-time risk pricing in embedded channels", 2),
   (2033, "Post-quantum migration", "Cryptography replacement reaches core systems", 2)
 ]),
 "table": table(["P&L line", "Mechanism", "Timing", "Proof point"], [
   ["Operating cost", "Back-office and contact-centre automation", "Now → 2028", "Cost/income trajectory ex-restructuring"],
   ["Payment fees", "Stablecoins and agentic rails bypass card economics", "2026 → 2030", "Fee yield per transaction"],
   ["Deposit funding", "Tokenised funds compete for idle cash", "2027 → 2030", "Deposit beta and mix"],
   ["Credit losses", "Faster data but correlated model behaviour", "Continuous", "Vintage loss curves vs models"],
   ["Compliance cost", "More models to validate, more fraud to police", "Now → 2030", "Risk spend as share of revenue"]
 ]),
 "gain": [
   "Scaled banks with clean data and the capital to rebuild cores — efficiency gains compound into ROE.",
   "Networks, exchanges and custodians that own rails and can tokenise settlement.",
   "Insurers with proprietary claims data that improves pricing faster than peers.",
   "Asset managers distributing through platforms and agents rather than branches.",
   "Specialist risk and compliance vendors selling into every institution."
 ],
 "exposed": [
   "Branch-heavy retail banks with thin fee income and slow core replacement.",
   "Monoline card issuers and processors if agentic rails reduce interchange.",
   "Commission-based advisors whose value is product access rather than advice.",
   "Small insurers with homogeneous underwriting and no data advantage.",
   "Crypto-native intermediaries that lose the compliance arbitrage."
 ],
 "watch": [
   "<strong>Deposit beta</strong> as tokenised cash substitutes become usable for payments.",
   "<strong>Interchange economics</strong> in agent-initiated transactions.",
   "<strong>Cost/income</strong> net of restructuring and vendor spend.",
   "<strong>Model inventory</strong> disclosed to regulators — a proxy for real deployment.",
   "<strong>Quantum migration timelines</strong> for core cryptography."
 ],
 "research": "The linked records cover payments, tokenisation, regulation and AI decisioning. Read them before extrapolating any single cost or fee number in this deck."
},
{
 "deck": "health-care-01",
 "title": "Health Care — How future technology reshapes the sector",
 "thesis": "Health care is a data-rich, decision-poor industry. The binding constraints are trial cost, regulatory evidence and reimbursement, not ideas. AI and automation shorten the path from target to patient, but only companies that generate defensible clinical evidence convert that speed into margin.",
 "econ": "Value accrues at different points: pharma earns on protected pricing and patent life, medtech on installed base and procedures, providers on volume and payer mix, payers on medical loss ratio.",
 "econBullets": [
   "Pharma gross margins are high, but R&D intensity and patent cliffs set the cycle.",
   "Medtech earns on procedure volume and consumables attached to capital equipment.",
   "Providers run thin margins, sensitive to labour cost and payer mix.",
   "Payers earn on the spread between premiums and medical spend.",
   "Reimbursement decisions, not technical feasibility, determine commercial timing."
 ],
 "impact": impact([
   {"label": "New revenue, contested", "items": ["AI-discovered assets entering clinical trials", "Companion diagnostics for targeted therapy", "Consumer wearables and remote monitoring"]},
   {"label": "New revenue, durable", "items": ["Biological data platforms licensed to pharma", "Surgical robotics with recurring instruments", "Manufacturing capacity for cell and gene therapy"]},
   {"label": "Cost takeout, fast", "items": ["Trial site selection and patient matching", "Prior authorisation and claims automation", "Documentation and coding support"]},
   {"label": "Structural cost shift", "items": ["Autonomous labs raise fixed-cost intensity", "Cyber and privacy liability grows", "Personalised manufacturing loses scale economics"]}
 ]),
 "bars": bars("Directional share of each cost or revenue pool exposed to the technology shift", [
   ("Phase II–III trial cost", 45),
   ("Discovery and preclinical chemistry", 35),
   ("Manufacturing cost of goods", 30),
   ("Claims administration and prior auth", 50),
   ("Sales and marketing spend", 20)
 ]),
 "chain": chain("Target discovery → preclinical → clinical → manufacturing → care delivery",
   [("Discovery", ["Biological foundation models", "Protein design", "Perturbation datasets", "Autonomous labs"]),
    ("Preclinical", ["Organoids", "In-silico toxicology", "Biomarker panels", "Lab automation"]),
    ("Clinical", ["Digital twins", "Decentralised trials", "Adaptive designs", "Real-world evidence"]),
    ("Manufacturing", ["Single-use bioreactors", "Cell and gene therapy", "Continuous processing", "Cold chain"]),
    ("Delivery", ["Diagnostics", "Surgical robotics", "Remote monitoring", "Care agents"])],
   "Each stage produces a product the next stage depends on. The weakest link is evidence generation, not molecule generation."),
 "clusters": [
   {"title": "Discovery and design", "body": "Models propose molecules and proteins faster than wet labs can validate them; the bottleneck moves downstream.",
    "items": ["Protein structure and design", "Generative chemistry", "Perturbation atlases", "Autonomous experimentation"]},
   {"title": "Clinical and evidence", "body": "Trials get cheaper at the margin but regulatory acceptance of digital endpoints is the gating item.",
    "items": ["Digital twins in trials", "Decentralised recruitment", "Real-world evidence", "Adaptive trial designs"]},
   {"title": "Care delivery", "body": "Automation addresses administrative waste first because it needs no clinical approval.",
    "items": ["Ambient documentation", "Prior-auth agents", "Remote patient monitoring", "Surgical robotics"]}
 ],
 "stack": stack([
   ("Biology", "Wet-lab reality", ["Assays", "Organoids", "Bioreactors", "Clinical sites"]),
   ("Data", "The raw material", ["Genomics", "Imaging", "EHR records", "Real-world cohorts"]),
   ("Models", "Prediction and design", ["Protein models", "Chemistry models", "Risk models", "Care agents"]),
   ("Products", "Approved and reimbursed", ["Drugs", "Devices", "Diagnostics", "Care programmes"])
 ]),
 "timeline": timeline([
   (2026, "AI-designed molecules in clinic", "First wave of model-originated candidates", 0),
   (2027, "Protein design enters trials", "De-novo binders with developable properties", 0),
   (2028, "Autonomous labs scale", "Closed-loop design-build-test cycles", 1),
   (2029, "Digital twins in trials", "Control-arm augmentation for select indications", 1),
   (2031, "In-silico evidence accepted", "Regulators accept modelling for narrow claims", 2),
   (2034, "Personalised manufacturing", "Point-of-care cell therapy at cost", 2)
 ]),
 "table": table(["P&L line", "Mechanism", "Timing", "Proof point"], [
   ["R&D expense", "Fewer failed programmes per approved asset", "2027 → 2032", "Phase transition rates"],
   ["Trial cost", "Better recruitment and remote monitoring", "Now → 2029", "Cost per randomised patient"],
   ["COGS", "Higher titre and continuous processing", "Now → 2028", "Gross margin by product"],
   ["Administrative cost", "Prior auth and coding automation", "Now → 2027", "Claims denial rate"],
   ["Pricing", "Evidence-based contracts and outcomes pricing", "2028 → 2032", "Net price realisation"]
 ]),
 "gain": [
   "Biotechs with proprietary datasets and a credible clinical pipeline, not just model access.",
   "CROs and lab-services firms that industrialise automation and shorten cycle times.",
   "Medtech with installed bases that can attach software and consumables.",
   "Manufacturers with capacity in biologics, cell and gene therapy.",
   "Diagnostics companies that own reimbursement pathways."
 ],
 "exposed": [
   "Me-too drug portfolios facing price pressure and faster generic entry.",
   "CROs that sell hours rather than faster enrolment.",
   "Hospitals reliant on fee-for-service administration without automation.",
   "Distributors and middlemen whose value is information asymmetry.",
   "Consumer health apps without clinical evidence or payer coverage."
 ],
 "watch": [
   "<strong>Phase transition rates</strong> for AI-originated assets, not press releases.",
   "<strong>Reimbursement decisions</strong> for digital diagnostics and remote monitoring.",
   "<strong>Trial cycle times</strong> and cost per patient at large sponsors.",
   "<strong>Manufacturing utilisation</strong> in cell and gene therapy.",
   "<strong>Regulatory guidance</strong> on model-generated evidence."
 ],
 "research": "The linked records span discovery platforms, trials, manufacturing and care delivery. Confidence labels differ sharply across them; treat speculative records as optionality, not base case."
},
{
 "deck": "consumer-discretionary-01",
 "title": "Consumer Discretionary — How future technology reshapes the sector",
 "thesis": "Discretionary spending is a contest for attention and convenience. Agents and AR collapse the distance between intent and purchase, while robotics and autonomy attack the two biggest cost lines: labour and fulfilment. Brands keep pricing power only where taste, status or service cannot be delegated to software.",
 "econ": "Revenue is cyclical and promotion-driven; cost is dominated by labour, rent, inventory and marketing. Small changes in markdown or fulfilment cost swing operating margin.",
 "econBullets": [
   "Retail earns on gross margin and inventory turns, not headline sales.",
   "Store economics depend on four-wall sales per square foot and payroll.",
   "Autos earn on mix, financing and after-sales; capex is model-cycle driven.",
   "Marketplaces earn take rate and advertising, with logistics as the moat.",
   "Hospitality and travel earn on occupancy and revenue per available room."
 ],
 "impact": impact([
   {"label": "New revenue, contested", "items": ["Agent-referred traffic and commissions", "AR try-on conversion uplift", "In-car digital services"]},
   {"label": "New revenue, durable", "items": ["Proprietary loyalty and first-party data", "Membership and resale programmes", "Experiential retail and hospitality"]},
   {"label": "Cost takeout, fast", "items": ["Demand forecasting and markdown optimisation", "Customer-service agents", "Warehouse task automation"]},
   {"label": "Structural cost shift", "items": ["Robotic fulfilment becomes table stakes", "Last-mile autonomy changes delivery economics", "Store estate must be re-purposed"]}
 ]),
 "bars": bars("Directional share of each pool exposed to technology-driven change", [
   ("Store labour cost", 45),
   ("Marketing and customer acquisition", 40),
   ("Fulfilment and last-mile cost", 50),
   ("Inventory markdown loss", 35),
   ("Marketplace take rate", 25)
 ]),
 "chain": chain("Inputs → manufacturing → fulfilment → marketplace → consumer interface",
   [("Inputs", ["Textiles and components", "Batteries and motors", "Packaging", "Food ingredients"]),
    ("Manufacturing", ["Contract assembly", "EV platforms", "Private-label production", "Additive parts"]),
    ("Fulfilment", ["Automated warehouses", "Robotic picking", "Autonomous delivery", "Returns processing"]),
    ("Marketplace", ["Agent product feeds", "Dynamic pricing", "Live commerce", "Resale platforms"]),
    ("Interface", ["AI shopping agents", "AR try-on", "In-car commerce", "Social storefronts"])],
   "The product families that matter are machine-readable catalogues, AR assets and autonomous delivery capacity — not another app."),
 "clusters": [
   {"title": "Agentic commerce", "body": "If an assistant chooses the product, brands compete on structured data, availability and price transparency.",
    "items": ["Product feed standards", "Agent payment mandates", "Dynamic pricing", "Reviews and trust signals"]},
   {"title": "Physical automation", "body": "Robotics moves from prototypes to unit economics in warehouses and, later, stores.",
    "items": ["Robotic picking", "Autonomous forklifts", "Drone and robot delivery", "Store replenishment"]},
   {"title": "Spatial and in-car", "body": "AR try-on and vehicle software create new surfaces for discovery and transactions.",
    "items": ["AR try-on", "Virtual staging", "In-car app stores", "Gesture interfaces"]}
 ],
 "stack": stack([
   ("Physical", "Stores, fleets, robots", ["Store estate", "Warehouses", "Delivery fleet", "Charging"]),
   ("Data", "Demand and identity", ["POS data", "Loyalty IDs", "Inventory", "Pricing signals"]),
   ("Models", "Prediction and agents", ["Forecasting", "Recommendation", "Shopping agents", "Pricing engines"]),
   ("Interfaces", "Where the sale happens", ["Marketplace app", "AR try-on", "In-car screen", "Voice assistant"])
 ]),
 "timeline": timeline([
   (2026, "Agent shopping pilots", "Assistants complete checkout with mandates", 0),
   (2027, "AR try-on at scale", "Returns fall for apparel categories", 0),
   (2028, "Robotic fulfilment standard", "Large DCs automate picking", 1),
   (2029, "Autonomous ride-hailing", "Driverless fleets in multiple cities", 1),
   (2031, "Humanoid store labour", "Limited tasks in back-of-house", 2),
   (2033, "Ambient commerce", "Purchases embedded in glasses and vehicles", 2)
 ]),
 "table": table(["P&L line", "Mechanism", "Timing", "Proof point"], [
   ["Gross margin", "Forecasting and markdown discipline", "Now → 2028", "Promotion depth and sell-through"],
   ["Payroll", "Self-checkout and task automation", "Now → 2029", "Sales per labour hour"],
   ["Fulfilment cost", "Robotics and route optimisation", "2027 → 2030", "Cost per order"],
   ["Marketing", "Agent referrals replace paid acquisition", "2027 → 2031", "CAC by channel"],
   ["Capex", "Autonomy and EV fleet renewal", "2028 → 2033", "Fleet utilisation and residual values"]
 ]),
 "gain": [
   "Marketplaces with logistics density and rich product data.",
   "Brands with genuine pricing power and direct customer relationships.",
   "Off-price and value formats as consumers delegate routine purchases.",
   "Autonomous fleet operators and the suppliers that equip them.",
   "Warehouse automation vendors with proven unit economics."
 ],
 "exposed": [
   "Mall-based retail with high fixed rents and undifferentiated assortment.",
   "DTC brands dependent on paid social acquisition.",
   "Franchised auto dealers facing direct-to-consumer and agentic pricing.",
   "Low-margin apparel exposed to returns and markdowns.",
   "Delivery networks without automation or density."
 ],
 "watch": [
   "<strong>Agent-referred conversion</strong> and whether it carries a commission.",
   "<strong>Return rates</strong> after AR try-on adoption.",
   "<strong>Fulfilment cost per order</strong> as robotics scales.",
   "<strong>Store closures</strong> versus conversion to fulfilment nodes.",
   "<strong>Robotaxi utilisation</strong> and safety incident rates."
 ],
 "research": "The linked records cover retail, autonomy, robotics and spatial interfaces. Commercial timing depends on local regulation and unit economics, not demo videos."
},
{
 "deck": "communication-services-01",
 "title": "Communication Services — How future technology reshapes the sector",
 "thesis": "This sector sells connectivity, attention and content. AI lowers the cost of producing content and raises the value of distribution and first-party data. Networks become software-defined and capex-heavy, while the interface to the customer moves from apps to assistants that summarise, recommend and block advertising.",
 "econ": "Telecom is a capital-intensive utility with ARPU and churn as the key variables. Media and platforms earn on advertising yield and subscriptions, with content cost as the swing factor.",
 "econBullets": [
   "Mobile and broadband ARPU grows slowly; churn and acquisition cost decide profitability.",
   "Network capex is lumpy and regulated returns depend on utilisation.",
   "Advertising earns on impressions, targeting and measurement.",
   "Content businesses carry high fixed costs and hit-driven revenue.",
   "Bundling reduces churn but compresses margin per service."
 ],
 "impact": impact([
   {"label": "New revenue, contested", "items": ["AI-generated content licensing", "Personalised advertising", "Edge compute and private 5G"]},
   {"label": "New revenue, durable", "items": ["Direct-to-device satellite coverage", "Bundled security and identity", "Enterprise connectivity and SASE"]},
   {"label": "Cost takeout, fast", "items": ["Network automation and energy optimisation", "AI customer care", "Programmatic ad operations"]},
   {"label": "Structural cost shift", "items": ["Spectral and fibre capex rises", "Content production cheapens but discovery tightens", "Trust and safety costs scale with synthetic media"]}
 ]),
 "bars": bars("Directional share of each pool exposed to automation or substitution", [
   ("Network operating cost", 40),
   ("Content production cost", 35),
   ("Advertising inventory and targeting", 55),
   ("Customer care cost", 45),
   ("Field operations and maintenance", 50)
 ]),
 "chain": chain("Spectrum and fibre → network → content and data → platforms → subscribers and advertisers",
   [("Resources", ["Spectrum", "Fibre", "Data centres", "Satellite capacity"]),
    ("Network", ["5G and fixed wireless", "Optical transport", "Edge nodes", "Network software"]),
    ("Content & data", ["Studios", "Sports rights", "First-party data", "Ad tech"]),
    ("Platforms", ["Streaming apps", "Messaging", "Search and social", "Agent interfaces"]),
    ("Customers", ["Subscribers", "Advertisers", "Enterprises", "Wholesale"])],
   "Connectivity is the commodity; identity, data and the interface carry the margin."),
 "clusters": [
   {"title": "Network automation", "body": "Self-optimising networks cut energy and field visits, the two largest opex lines.",
    "items": ["AI RAN optimisation", "Predictive maintenance", "Energy management", "Private 5G"]},
   {"title": "Synthetic media", "body": "Production cost collapses, but rights, provenance and trust become the scarce assets.",
    "items": ["AI dubbing and localisation", "Virtual production", "Content provenance", "Licensing deal structures"]},
   {"title": "Agentic interfaces", "body": "Assistants intermediate search, messaging and shopping, threatening ad inventory and app distribution.",
    "items": ["AI search summaries", "Agent messaging", "Identity and consent", "Measurement standards"]}
 ],
 "stack": stack([
   ("Physical", "Spectrum, fibre, towers", ["Macro sites", "Fibre plant", "Submarine cable", "Satellites"]),
   ("Network", "Transport and edge", ["5G core", "Optical transport", "Edge compute", "Wi-Fi offload"]),
   ("Data", "Audiences and content", ["First-party data", "Content library", "Ad exchanges", "Measurement"]),
   ("Products", "What customers buy", ["Mobile plans", "Broadband", "Streaming", "Ad campaigns"])
 ]),
 "timeline": timeline([
   (2026, "AI search summaries", "Referral traffic to publishers falls", 0),
   (2027, "Autonomous network ops", "Closed-loop optimisation in live networks", 0),
   (2028, "Edge inference", "Low-latency AI at cell sites", 1),
   (2029, "Direct-to-device satellite", "Coverage beyond terrestrial networks", 1),
   (2031, "Agent-first interfaces", "Messaging becomes transaction surface", 2),
   (2033, "6G standards", "Sensing and AI native air interface", 2)
 ]),
 "table": table(["P&L line", "Mechanism", "Timing", "Proof point"], [
   ["Network opex", "Automation and energy efficiency", "Now → 2028", "Opex per site and per terabyte"],
   ["Capex", "Edge and fibre build-out", "2026 → 2030", "Capex-to-sales and utilisation"],
   ["Advertising", "Targeting and synthetic creative", "Now → 2029", "CPM and conversion by format"],
   ["Content cost", "AI production and localisation", "2026 → 2029", "Cost per hour of original content"],
   ["Churn", "Bundling and service quality", "Continuous", "Postpaid churn and ARPU"]
 ]),
 "gain": [
   "Fibre and fixed-wireless operators with dense, owned infrastructure.",
   "Platforms with first-party identity and measured advertising outcomes.",
   "IP owners whose libraries become training and licensing assets.",
   "Network software and edge vendors selling automation into every carrier.",
   "Satellite operators offering direct-to-device coverage."
 ],
 "exposed": [
   "Linear broadcasters and pay-TV bundles losing reach and pricing.",
   "Publishers dependent on search referral traffic.",
   "Mobile virtual network operators without differentiation.",
   "Ad-tech intermediaries disintermediated by platforms' own agents.",
   "Content studios without owned IP or production scale."
 ],
 "watch": [
   "<strong>Search referral traffic</strong> to publisher sites after AI summaries.",
   "<strong>ARPU and churn</strong> net of bundling discounts.",
   "<strong>Network energy per terabyte</strong> as a proxy for automation success.",
   "<strong>Direct-to-device commercial launches</strong> and pricing.",
   "<strong>Licensing revenue</strong> from content used in model training."
 ],
 "research": "The links below are the source records for connectivity, advertising, satellite and synthetic media claims. Timelines are source estimates, not commitments."
},
{
 "deck": "industrials-01",
 "title": "Industrials — How future technology reshapes the sector",
 "thesis": "Industrials sell uptime, throughput and safety. Labour scarcity is the forcing function: automation, autonomy and digital twins improve output per worker without requiring new demand. The winners own the installed base and the service relationship; the losers sell interchangeable metal.",
 "econ": "Revenue is project- and backlog-driven, with aftermarket service carrying much higher margins than original equipment. Working capital and execution risk decide cash conversion.",
 "econBullets": [
   "Original equipment is cyclical and competitive; aftermarket parts and service earn the margin.",
   "Backlog visibility matters, but book-to-bill and cancellation rates matter more.",
   "Labour is a large share of both manufacturing and field service cost.",
   "Project businesses carry execution and warranty risk.",
   "Electrical equipment demand is increasingly set by grid and data-centre capex."
 ],
 "impact": impact([
   {"label": "New revenue, contested", "items": ["Autonomous inspection drones", "Robotics-as-a-service", "Digital twin software"]},
   {"label": "New revenue, durable", "items": ["Aftermarket service contracts with sensors", "Grid and data-centre electrical equipment", "Defence autonomy and counter-drone systems"]},
   {"label": "Cost takeout, fast", "items": ["Predictive maintenance", "Remote commissioning", "Automated quality inspection"]},
   {"label": "Structural cost shift", "items": ["Factories re-tool around robotics", "Field service shifts from hours to outcomes", "Cyber exposure grows with connected assets"]}
 ]),
 "bars": bars("Directional share of each pool exposed to automation or new demand", [
   ("Field service labour cost", 50),
   ("Aftermarket revenue", 35),
   ("Project engineering hours", 40),
   ("Cost of unplanned downtime", 45),
   ("Inspection and QA labour", 55)
 ]),
 "chain": chain("Materials → components → machines → automation systems → service and operations",
   [("Materials", ["Specialty steel", "Bearings", "Power electronics", "Sensors"]),
    ("Components", ["Servo drives", "Hydraulics", "Gearboxes", "Controllers"]),
    ("Machines", ["Robot arms", "CNC tools", "Turbines", "Electrical switchgear"]),
    ("Systems", ["Automation cells", "Digital twins", "Fleet software", "Safety systems"]),
    ("Operations", ["Predictive maintenance", "Autonomous inspection", "Outcome contracts", "Remote operations"])],
   "The future product is not a machine; it is a machine plus the software and service contract that guarantees uptime."),
 "clusters": [
   {"title": "Robotics and automation", "body": "Falling sensor and actuator costs move automation into high-mix, low-volume work.",
    "items": ["Collaborative robots", "Vision-guided picking", "Autonomous mobile robots", "Humanoid pilots"]},
   {"title": "Digital twins", "body": "Simulation shortens commissioning and supports outcome-based service contracts.",
    "items": ["Plant simulation", "Predictive maintenance", "Remote commissioning", "Asset performance management"]},
   {"title": "Electrification", "body": "Grid and data-centre build-out pulls through switchgear, transformers and cooling.",
    "items": ["Grid equipment", "Data-centre cooling", "Power distribution", "Energy management"]}
 ],
 "stack": stack([
   ("Physical", "Machines and sites", ["Robots", "Machine tools", "Turbines", "Switchgear"]),
   ("Sensing", "What gets measured", ["Vibration", "Thermal", "Vision", "LiDAR"]),
   ("Software", "Control and prediction", ["PLC and SCADA", "Digital twins", "Fleet orchestration", "Maintenance models"]),
   ("Service", "Where margin sits", ["Uptime contracts", "Remote support", "Parts networks", "Retrofits"])
 ]),
 "timeline": timeline([
   (2026, "Cobot cost crossover", "Smaller factories automate", 0),
   (2027, "Digital twins standard", "Commissioning shifts to simulation", 0),
   (2028, "Autonomous inspection", "Drones and robots replace confined-space work", 1),
   (2030, "Humanoids in logistics", "Limited repetitive tasks", 1),
   (2032, "Lights-out plants", "High-volume lines run unattended", 2),
   (2035, "Outcome-based service", "Uptime sold per unit of output", 2)
 ]),
 "table": table(["P&L line", "Mechanism", "Timing", "Proof point"], [
   ["Service revenue", "Sensors convert parts sales into contracts", "Now → 2029", "Attach rate and recurring share"],
   ["Labour cost", "Automation in production and inspection", "Now → 2030", "Output per employee"],
   ["Warranty cost", "Prediction reduces failures", "2027 → 2031", "Claims per installed unit"],
   ["Backlog quality", "Automation shortens project cycles", "2026 → 2029", "Book-to-bill and cancellations"],
   ["Capex", "Reshoring and electrification", "2026 → 2032", "Capacity utilisation"]
 ]),
 "gain": [
   "Automation OEMs with service networks and software attach.",
   "Electrical equipment makers exposed to grid and data-centre spend.",
   "Defence primes with autonomy, sensing and munitions capacity.",
   "Distributors that become technical service providers.",
   "Industrial software vendors selling simulation and maintenance."
 ],
 "exposed": [
   "Labour-intensive contractors without automation.",
   "Component makers with no IP and price-only competition.",
   "Machine builders that refuse to sell software or service.",
   "Aerospace suppliers with single-programme concentration.",
   "Businesses with connected assets but weak cyber controls."
 ],
 "watch": [
   "<strong>Aftermarket share</strong> of total revenue and its margin.",
   "<strong>Output per employee</strong> in automated plants.",
   "<strong>Robot orders</strong> outside automotive, the historical core.",
   "<strong>Grid equipment lead times</strong> as a demand signal.",
   "<strong>Autonomy certification</strong> for inspection and defence use."
 ],
 "research": "Linked records cover robotics, industrial software, electrification and autonomy. The commercial risk is integration cost, not component availability."
},
{
 "deck": "consumer-staples-01",
 "title": "Consumer Staples — How future technology reshapes the sector",
 "thesis": "Staples are a volume business with thin margins and powerful distribution. Technology matters when it changes input cost, waste or shelf productivity. The biggest long-run shifts are biological production of ingredients, AI-driven forecasting, and retail media turning shelf space into an advertising business.",
 "econ": "Revenue grows slowly with population and price. Gross margin depends on commodity inputs, packaging and manufacturing efficiency; distribution and trade spend absorb much of the rest.",
 "econBullets": [
   "Volume growth is low; price/mix and market share drive reported growth.",
   "Commodity inputs swing gross margin, often with a lag to pricing.",
   "Trade promotion and shelf space are the main competitive currencies.",
   "Distribution density determines cost per case.",
   "Retail media and private label are reshaping retailer economics."
 ],
 "impact": impact([
   {"label": "New revenue, contested", "items": ["Personalised nutrition", "Retail media networks", "Direct subscription bundles"]},
   {"label": "New revenue, durable", "items": ["Precision-fermented ingredients", "Health-positioned reformulations", "Private-label premium tiers"]},
   {"label": "Cost takeout, fast", "items": ["Demand forecasting and waste reduction", "Automated palletising and picking", "Trade-spend optimisation"]},
   {"label": "Structural cost shift", "items": ["Biological production replaces some agriculture", "Packaging regulation raises cost", "Distribution automation becomes necessary"]}
 ]),
 "bars": bars("Directional share of each pool exposed to technology-driven change", [
   ("Commodity input cost", 50),
   ("Distribution and logistics", 40),
   ("Trade promotion spend", 35),
   ("Manufacturing waste", 25),
   ("Retail media profit pool", 20)
 ]),
 "chain": chain("Inputs → processing → manufacturing → distribution → household",
   [("Inputs", ["Agricultural commodities", "Precision fermentation", "Packaging", "Flavours"]),
    ("Processing", ["Milling and refining", "Cold chain", "Sterilisation", "Ingredient blends"]),
    ("Manufacturing", ["Automated lines", "Robotic palletising", "Quality vision", "Flexible batch"]),
    ("Distribution", ["Route optimisation", "Automated DCs", "Dark stores", "Returns"]),
    ("Household", ["Retail media", "Subscription", "Personalised packs", "Refill systems"])],
   "The product families to watch are ingredients made by fermentation, intelligent packaging and the data layer that connects shelf to factory."),
 "clusters": [
   {"title": "Biological inputs", "body": "Precision fermentation and cellular agriculture target the most expensive molecules, not whole foods.",
    "items": ["Precision fermentation", "Enzyme engineering", "Alternative proteins", "Upcycled inputs"]},
   {"title": "Supply-chain intelligence", "body": "Forecasting and dynamic replenishment cut waste and working capital in perishable categories.",
    "items": ["Demand sensing", "Automated replenishment", "Cold-chain monitoring", "Trade-spend optimisation"]},
   {"title": "Retail media", "body": "Retailers monetise first-party purchase data, changing the balance of power with brands.",
    "items": ["Sponsored search", "In-store retail media", "Measurement", "Loyalty pricing"]}
 ],
 "stack": stack([
   ("Physical", "Farms and factories", ["Agriculture", "Fermentation", "Packaging lines", "Distribution"]),
   ("Data", "Shelf and supply", ["POS data", "Loyalty", "Supply signals", "Waste tracking"]),
   ("Models", "Forecast and price", ["Demand forecasting", "Price elasticity", "Assortment", "Media targeting"]),
   ("Products", "What households buy", ["Food and beverage", "Household goods", "Private label", "Subscriptions"])
 ]),
 "timeline": timeline([
   (2026, "AI forecasting standard", "Waste and stockouts fall in perishables", 0),
   (2027, "Fermented ingredients scale", "Cost parity in selected molecules", 0),
   (2029, "Autonomous distribution", "Robotic DCs in dense markets", 1),
   (2031, "Personalised nutrition", "Data-driven packs at scale", 1),
   (2033, "Regenerative supply chains", "Verified low-carbon inputs", 2),
   (2035, "Closed-loop packaging", "Refill and reuse economics work", 2)
 ]),
 "table": table(["P&L line", "Mechanism", "Timing", "Proof point"], [
   ["COGS", "Fermented inputs and yield improvement", "2027 → 2032", "Cost per kilogram at scale"],
   ["Waste", "Forecasting and cold-chain control", "Now → 2028", "Shrink as share of sales"],
   ["Trade spend", "Measurement and targeted promotion", "Now → 2029", "Promotion ROI"],
   ["Distribution", "Route and DC automation", "2027 → 2031", "Cost per case"],
   ["Gross margin", "Mix shift to health and private label", "Continuous", "Price/mix contribution"]
 ]),
 "gain": [
   "Scale manufacturers with data-driven supply chains and strong private-label positions.",
   "Ingredient-tech companies with cost parity and regulatory approval.",
   "Discounters and club formats with efficient logistics.",
   "Retailers building media networks on first-party data.",
   "Packaging companies with recyclable or refillable formats."
 ],
 "exposed": [
   "Premium brands with no functional differentiation.",
   "Small distributors without automation or density.",
   "Sugar- and salt-heavy portfolios facing regulation and reformulation cost.",
   "Single-ingredient suppliers exposed to fermentation substitution.",
   "Retailers without loyalty data or media capability."
 ],
 "watch": [
   "<strong>Volume versus price</strong> split in reported growth.",
   "<strong>Fermentation cost curves</strong> for the top three molecules.",
   "<strong>Shrink and waste</strong> as a share of sales.",
   "<strong>Private-label share</strong> by category.",
   "<strong>Retail media revenue</strong> and its margin contribution."
 ],
 "research": "Linked records cover food tech, supply chains, retail media and materials. Cost-parity claims should be checked at commercial scale, not lab scale."
},
{
 "deck": "energy-01",
 "title": "Energy — How future technology reshapes the sector",
 "thesis": "Energy is a capital allocation business with commodity price exposure. Technology improves recovery, reduces downtime and shortens the learning curve on new capacity, but it rarely escapes the price cycle. The new demand source is data centres and electrification, which pulls gas, grid and nuclear into the same investment conversation.",
 "econ": "Revenue is price times volume; cost is lifting cost, royalties and capex. Reserve life and decline rates determine terminal value, and refining or LNG spreads add a second, cyclical margin.",
 "econBullets": [
   "Upstream economics depend on lifting cost and decline rates, not headline production.",
   "Integrated majors smooth the cycle with refining, chemicals and trading.",
   "LNG earns on contracted spreads and liquefaction utilisation.",
   "Oilfield services are cyclical, with utilisation and pricing power in tight markets.",
   "Cost of capital and reserve life drive valuation more than near-term prices."
 ],
 "impact": impact([
   {"label": "New revenue, contested", "items": ["Gas and LNG for data-centre load", "Geothermal and storage projects", "Carbon-accounting services"]},
   {"label": "New revenue, durable", "items": ["Low-cost barrel replacement", "Power and hedging products", "Maintenance and digital services"]},
   {"label": "Cost takeout, fast", "items": ["AI seismic interpretation", "Drilling automation", "Predictive maintenance on rotating equipment"]},
   {"label": "Structural cost shift", "items": ["Methane monitoring becomes mandatory", "Water and emissions capex rises", "Cyber risk in operational technology"]}
 ]),
 "bars": bars("Directional share of each pool exposed to automation or demand shift", [
   ("Drilling and completion cost", 45),
   ("Facility downtime", 40),
   ("Seismic and subsurface interpretation", 35),
   ("Refinery energy cost", 30),
   ("Methane leak exposure", 25)
 ]),
 "chain": chain("Subsurface → extraction → processing and LNG → transport → power and industrial demand",
   [("Subsurface", ["Seismic data", "Reservoir models", "Well designs", "Completion fluids"]),
    ("Extraction", ["Automated rigs", "Artificial lift", "Sand and chemicals", "Water handling"]),
    ("Processing", ["Gas plants", "Refineries", "LNG trains", "Petrochemicals"]),
    ("Transport", ["Pipelines", "LNG carriers", "Storage", "Trading desks"]),
    ("Demand", ["Data-centre power", "Industrial heat", "Transport fuels", "Grid balancing"])],
   "The new customer is a data centre signing a long-term power contract; that changes which molecules and assets are strategic."),
 "clusters": [
   {"title": "Subsurface intelligence", "body": "Better imaging and faster interpretation lower finding cost in mature basins.",
    "items": ["AI seismic inversion", "Reservoir simulation", "Well placement", "Core analysis"]},
   {"title": "Operational automation", "body": "Autonomous rigs and predictive maintenance cut non-productive time, the largest controllable cost.",
    "items": ["Automated drilling", "Remote operations", "Digital twins", "Methane monitoring"]},
   {"title": "Power convergence", "body": "Gas, geothermal and storage compete to serve firm data-centre load.",
    "items": ["Gas turbines", "Geothermal", "Battery storage", "Behind-the-meter power"]}
 ],
 "stack": stack([
   ("Resources", "Rock and molecules", ["Reservoirs", "Gas fields", "Solar and wind", "Uranium"]),
   ("Assets", "Where capex lands", ["Rigs", "Refineries", "LNG trains", "Turbines"]),
   ("Operations", "How uptime is won", ["Sensors", "Automation", "Digital twins", "Trading"]),
   ("Markets", "How value is captured", ["PPAs", "LNG contracts", "Hedging", "Capacity payments"])
 ]),
 "timeline": timeline([
   (2026, "AI-assisted drilling", "Well planning compressed", 0),
   (2027, "Autonomous rigs", "Remote operations at scale", 0),
   (2028, "Methane rules tighten", "Monitoring becomes auditable", 1),
   (2030, "Gas-for-data-centre deals", "Long-term power contracts signed", 1),
   (2032, "Geothermal scale-up", "Drilling cost curves improve", 2),
   (2035, "Industrial heat decarbonised", "Electric and hydrogen routes compete", 2)
 ]),
 "table": table(["P&L line", "Mechanism", "Timing", "Proof point"], [
   ["Lifting cost", "Automation and energy efficiency", "Now → 2029", "Cost per barrel ex-royalties"],
   ["Uptime", "Predictive maintenance", "Now → 2028", "Non-productive time"],
   ["Finding cost", "Better subsurface models", "2026 → 2030", "Reserve replacement cost"],
   ["LNG margin", "Contract structure and utilisation", "Continuous", "Contracted vs spot mix"],
   ["Emissions cost", "Methane and carbon pricing", "2027 → 2032", "Intensity per barrel"]
 ]),
 "gain": [
   "Low-cost operators with long reserve life and disciplined capex.",
   "Gas and LNG producers positioned for power demand.",
   "Oilfield services with automation and international exposure.",
   "Geothermal and storage developers with repeatable cost curves.",
   "Power marketers and traders who can structure long-dated contracts."
 ],
 "exposed": [
   "High-cost offshore projects with long paybacks.",
   "Refiners without feedstock flexibility or low-carbon options.",
   "Coal-heavy portfolios facing demand and financing pressure.",
   "Service companies with ageing fleets and no digital offering.",
   "Operators with weak methane monitoring and regulatory exposure."
 ],
 "watch": [
   "<strong>Lifting cost per barrel</strong> through the cycle.",
   "<strong>Gas contract prices</strong> linked to data-centre load.",
   "<strong>Non-productive time</strong> as automation proof.",
   "<strong>Methane intensity</strong> disclosures and audits.",
   "<strong>Reserve replacement</strong> at current finding costs."
 ],
 "research": "Linked records cover drilling, LNG, geothermal, storage and methane. Commodity prices dominate near-term results; technology changes the cost curve slowly."
},
{
 "deck": "materials-01",
 "title": "Materials — How future technology reshapes the sector",
 "thesis": "Materials companies turn energy, ore and chemistry into specified inputs. Future demand is concentrated in a handful of new product families — battery materials, semiconductor-grade chemicals, rare earths and recycled feedstock — where qualification cycles are long and purity is the moat. Technology changes both the demand mix and the cost of producing it.",
 "econ": "Revenue is volume times spread over raw material. Utilisation, energy cost and feedstock access decide margin, and qualification locks in customers for years.",
 "econBullets": [
   "Commodity producers are price takers; specialty producers earn on specification and qualification.",
   "Energy is a large and volatile cost line in refining and smelting.",
   "Ore grade decline raises unit costs over time.",
   "Of take agreements and vertical integration secure demand for new materials.",
   "Permitting and environmental compliance set the pace of capacity additions."
 ],
 "impact": impact([
   {"label": "New revenue, contested", "items": ["Battery-grade lithium and nickel", "Rare earth magnets", "Semiconductor precursors"]},
   {"label": "New revenue, durable", "items": ["Qualified specialty chemicals", "Recycled feedstock with traceability", "Low-carbon steel and aluminium"]},
   {"label": "Cost takeout, fast", "items": ["AI process control", "Predictive maintenance", "Automated assay and sorting"]},
   {"label": "Structural cost shift", "items": ["Energy contracts decide competitiveness", "Water and tailings liabilities rise", "Circularity regulation changes feedstock"]}
 ]),
 "bars": bars("Directional share of each pool exposed to demand or cost disruption", [
   ("Refining and smelting energy cost", 35),
   ("Mining grade and dilution exposure", 40),
   ("Battery material demand pool", 50),
   ("Recycled feedstock share", 20),
   ("Semiconductor materials purity premium", 30)
 ]),
 "chain": chain("Ore and feedstock → refining → precursor and specialty chemicals → components → OEM",
   [("Mining", ["Lithium concentrate", "Nickel matte", "Rare earth ore", "Copper concentrate"]),
    ("Refining", ["Battery-grade salts", "Separated rare earths", "Electronic-grade gases", "Alumina"]),
    ("Precursors", ["Cathode active material", "Magnets", "Photoresist", "Silicon wafers"]),
    ("Components", ["Battery cells", "Motors", "Chips", "Structural parts"]),
    ("OEM", ["EVs", "Turbines", "Data centres", "Consumer devices"])],
   "The products with pricing power are the qualified intermediates, not the ore. That is where new capacity is being built."),
 "clusters": [
   {"title": "Battery materials", "body": "Chemistry shifts between LFP, high-nickel and sodium-ion change which intermediates matter.",
    "items": ["Lithium refining", "Cathode active material", "Sodium-ion", "Recycling"]},
   {"title": "Semiconductor materials", "body": "Node transitions raise purity requirements and consume more specialty gases and photoresists.",
    "items": ["Electronic-grade gases", "Photoresist", "CMP slurries", "Ultra-pure metals"]},
   {"title": "Circularity", "body": "Recycling becomes a feedstock strategy as much as an environmental one.",
    "items": ["Battery recycling", "Scrap sorting", "Traceability", "Low-carbon smelting"]}
 ],
 "stack": stack([
   ("Resources", "Ore and energy", ["Mines", "Power contracts", "Water", "Gas supply"]),
   ("Processing", "Refining and purity", ["Hydrometallurgy", "Separation", "Distillation", "Smelting"]),
   ("Specification", "Qualification", ["Battery grade", "Electronic grade", "Aerospace grade", "Medical grade"]),
   ("Products", "Sold into OEMs", ["CAM", "Magnets", "Wafers", "Structural alloys"])
 ]),
 "timeline": timeline([
   (2026, "Rare-earth diversification", "New separation capacity outside China", 0),
   (2027, "Battery recycling scales", "Closed-loop feedstock for cell makers", 0),
   (2028, "Sodium-ion commercial", "Cost-sensitive storage and entry vehicles", 1),
   (2030, "Green steel premiums", "Low-carbon steel in automotive supply", 1),
   (2032, "Deep-sea and tailings recovery", "New supply with higher scrutiny", 2),
   (2035, "Molecular recycling", "Plastic feedstock loops at scale", 2)
 ]),
 "table": table(["P&L line", "Mechanism", "Timing", "Proof point"], [
   ["Realised price", "Product mix shifts to qualified grades", "2026 → 2032", "Spread over benchmark"],
   ["Energy cost", "Process electrification and PPAs", "Now → 2030", "Cost per tonne"],
   ["Yield", "AI process control and sorting", "Now → 2028", "Recovery rate"],
   ["Feedstock cost", "Recycling and offtake", "2027 → 2033", "Share of recycled input"],
   ["Compliance cost", "Water, tailings and carbon", "Continuous", "Provision per tonne"]
 ]),
 "gain": [
   "Diversified miners with permits and low-cost ore bodies.",
   "Refiners with cheap power and qualified battery or electronic grades.",
   "Specialty chemical makers with long qualification locks.",
   "Recyclers with traceable feedstock and OEM contracts.",
   "Low-carbon steel and aluminium producers with premium offtake."
 ],
 "exposed": [
   "Single-asset miners with high costs and short reserve life.",
   "Commodity chemical producers without specification advantage.",
   "High-cost aluminium smelters reliant on expensive power.",
   "Processors with water or tailings liabilities.",
   "Suppliers that fail qualification for new node or cell chemistries."
 ],
 "watch": [
   "<strong>Battery-grade price spreads</strong> versus benchmark carbonate.",
   "<strong>Qualification announcements</strong> with tier-one OEMs.",
   "<strong>Energy contracts</strong> and their duration.",
   "<strong>Recycled input share</strong> in new cathode contracts.",
   "<strong>Permit timelines</strong> for new refining capacity."
 ],
 "research": "Linked records cover battery materials, rare earths, semiconductor chemicals and recycling. Qualification, not resource size, is the commercial gate."
},
{
 "deck": "real-estate-01",
 "title": "Real Estate — How future technology reshapes the sector",
 "thesis": "Real estate is a lease on a use case. Technology creates one enormous new use case — data centres — and erodes another — commodity offices. The sector's return depends less on construction technology than on power access, tenant credit and the ability to re-let space to machine and logistics workloads.",
 "econ": "Returns come from rent, occupancy and cap-rate movement. Development earns a spread over cost; asset management earns on lease spreads and retention; leverage amplifies both.",
 "econBullets": [
   "Net operating income is rent minus operating cost; occupancy and lease spreads drive it.",
   "Cap rates translate NOI into value and move with rates and risk appetite.",
   "Development margin is the spread between yield on cost and exit cap rate.",
   "Data centres earn on power density and contracted escalators.",
   "Office and retail face obsolescence risk that shows up in leasing spreads first."
 ],
 "impact": impact([
   {"label": "New revenue, contested", "items": ["Powered land and shell leases", "Flexible logistics and dark stores", "Life-science conversion"]},
   {"label": "New revenue, durable", "items": ["Hyperscale data-centre leases", "Grid-connected industrial parks", "Mixed-use residential"]},
   {"label": "Cost takeout, fast", "items": ["AI leasing and underwriting", "Building energy management", "Automated property management"]},
   {"label": "Structural cost shift", "items": ["Power interconnection becomes the binding constraint", "Construction labour and materials stay expensive", "Insurance and climate adaptation costs rise"]}
 ]),
 "bars": bars("Directional share of each asset pool exposed to demand change", [
   ("Office lease rollover", 45),
   ("Development cost inflation", 40),
   ("Property management operating cost", 30),
   ("Data-centre power constraint", 60),
   ("Retail footfall exposure", 35)
 ]),
 "chain": chain("Land and power → development → asset management → leasing → occupier",
   [("Land & power", ["Powered land", "Substations", "Water rights", "Fibre routes"]),
    ("Development", ["Modular construction", "Cooling systems", "Shell and core", "Fit-out"]),
    ("Assets", ["Data centres", "Logistics sheds", "Offices", "Residential"]),
    ("Operations", ["Smart buildings", "Energy contracts", "Lease management", "Maintenance"]),
    ("Occupiers", ["Hyperscalers", "3PLs", "Enterprises", "Households"])],
   "Power, not floor space, is the scarce product. Land without interconnection is optionality, not an asset."),
 "clusters": [
   {"title": "Data-centre demand", "body": "AI training and inference raise power density and make pre-leasing with credit tenants the norm.",
    "items": ["Hyperscale campuses", "Edge sites", "Liquid cooling", "Behind-the-meter power"]},
   {"title": "Construction technology", "body": "Modular and robotic construction addresses labour scarcity, but adoption is slow and local.",
    "items": ["Modular volumetric", "3D-printed components", "Robotic fit-out", "Digital twins"]},
   {"title": "Asset intelligence", "body": "Sensors and AI leasing tools improve NOI at the margin; they do not fix a bad location.",
    "items": ["Smart building controls", "Space analytics", "Automated leasing", "Energy optimisation"]}
 ],
 "stack": stack([
   ("Land", "Site and power", ["Zoning", "Interconnection", "Water", "Fibre"]),
   ("Building", "Shell and systems", ["Structure", "Cooling", "Electrical", "Controls"]),
   ("Operations", "NOI and leases", ["Lease admin", "Energy", "Maintenance", "Security"]),
   ("Occupiers", "Who pays rent", ["Hyperscalers", "Logistics", "Offices", "Residents"])
 ]),
 "timeline": timeline([
   (2026, "Data-centre pre-leasing", "Powered shells leased before completion", 0),
   (2027, "Power premium pricing", "Interconnection value capitalised", 0),
   (2028, "Construction robotics", "Modular and robotic fit-out at scale", 1),
   (2030, "Smart building baseline", "Energy optimisation standard in leases", 1),
   (2032, "Office conversions", "Obsolescent stock converted or written down", 2),
   (2035, "Grid-constrained growth", "New supply tied to generation build", 2)
 ]),
 "table": table(["P&L line", "Mechanism", "Timing", "Proof point"], [
   ["Rent growth", "Lease spreads to data and logistics tenants", "Now → 2030", "Signed rent versus in-place"],
   ["Occupancy", "Office obsolescence versus conversions", "2026 → 2032", "Leasing velocity by submarket"],
   ["Development cost", "Modular and robotics adoption", "2028 → 2033", "Cost per square metre"],
   ["Operating cost", "Energy and building automation", "Now → 2029", "Opex per square metre"],
   ["Cap rate", "Risk premium by asset type", "Continuous", "Transaction yields"]
 ]),
 "gain": [
   "Landlords with powered, interconnected sites near demand.",
   "Logistics owners with infill locations and modern clear heights.",
   "Operators able to pre-lease to credit hyperscalers.",
   "Developers with modular construction capability.",
   "Asset managers with data and leasing technology."
 ],
 "exposed": [
   "Commodity offices in secondary locations with long lease rolls.",
   "Secondary malls and retail parks losing anchor tenants.",
   "Highly leveraged developments with rate-sensitive refinancing.",
   "Owners without grid access competing for data-centre tenants.",
   "Buildings with poor energy performance facing regulatory capex."
 ],
 "watch": [
   "<strong>Interconnection queues</strong> and MW secured, not hectares owned.",
   "<strong>Signed lease spreads</strong> by asset type.",
   "<strong>Office leasing velocity</strong> in core submarkets.",
   "<strong>Construction cost per square metre</strong>.",
   "<strong>Cap-rate divergence</strong> between data/logistics and office."
 ],
 "research": "Linked records cover data centres, construction, building technology and energy. Site-level power contracts matter more than sector-level narratives."
},
{
 "deck": "utilities-01",
 "title": "Utilities — How future technology reshapes the sector",
 "thesis": "Utilities earn a regulated return on capital. The technology story is a demand story: data centres and electrification turn a low-growth sector into a capacity-build sector. Whoever can add firm, clean generation and interconnect it fastest earns a growing rate base; whoever cannot faces cost inflation and stranded assets.",
 "econ": "Revenue is rate base times allowed return, plus pass-through fuel cost. Load growth, capex and allowed ROE drive earnings; weather and outages drive variance.",
 "econBullets": [
   "Regulated returns are set on rate base, so capex growth is earnings growth if allowed.",
   "Load growth has been near zero for a decade; data centres change that.",
   "Fuel and purchased power are largely pass-through, but lag and hedging create risk.",
   "Grid capex is rising faster than sales, pressuring customer bills.",
   "Merchant generators earn on spark spreads and capacity prices."
 ],
 "impact": impact([
   {"label": "New revenue, contested", "items": ["Large-load tariffs for data centres", "Behind-the-meter generation deals", "Green tariffs and RECs"]},
   {"label": "New revenue, durable", "items": ["Rate-base growth from grid and storage", "Regulated transmission investment", "Nuclear life extensions"]},
   {"label": "Cost takeout, fast", "items": ["AI grid optimisation", "Predictive maintenance", "Automated field service"]},
   {"label": "Structural cost shift", "items": ["Interconnection and transmission queues lengthen", "Storm and wildfire hardening capex rises", "Customer bills become political"]}
 ]),
 "bars": bars("Directional share of each pool exposed to the demand and technology shift", [
   ("Load growth from data centres", 55),
   ("Grid and transmission capex", 50),
   ("Operations and maintenance cost", 30),
   ("Peak capacity margin", 40),
   ("Interconnection queue delay", 45)
 ]),
 "chain": chain("Fuel and resource → generation → transmission → distribution → customer and DER",
   [("Fuel", ["Gas supply", "Uranium", "Solar and wind", "Hydro"]),
    ("Generation", ["Gas turbines", "SMRs", "Storage", "Nuclear uprates"]),
    ("Transmission", ["HV lines", "Substations", "Transformers", "HVDC"]),
    ("Distribution", ["Feeders", "Smart meters", "DER orchestration", "EV charging"]),
    ("Customers", ["Data centres", "Industry", "Households", "Aggregators"])],
   "Firm capacity and interconnection rights are the products in shortest supply. Storage and SMRs are the option value on top."),
 "clusters": [
   {"title": "Firm clean capacity", "body": "Nuclear uprates, SMRs and gas with carbon capture compete for the same data-centre contracts.",
    "items": ["SMRs", "Nuclear uprates", "Gas turbines", "Geothermal"]},
   {"title": "Grid and storage", "body": "Storage shifts from energy arbitrage to capacity and reliability services.",
    "items": ["Grid-scale batteries", "Transmission", "Transformers", "DER aggregation"]},
   {"title": "Grid intelligence", "body": "AI forecasting and automation reduce outage time and defer capex.",
    "items": ["Load forecasting", "Predictive maintenance", "Outage automation", "Virtual power plants"]}
 ],
 "stack": stack([
   ("Assets", "Physical system", ["Generation", "Substations", "Poles and wires", "Meters"]),
   ("Control", "Grid operations", ["SCADA", "EMS and DMS", "Protection", "Markets"]),
   ("Data", "Forecast and price", ["Load data", "Weather", "DER telemetry", "Market prices"]),
   ("Customers", "Load and flexibility", ["Data centres", "EVs", "Heat pumps", "Storage"])
 ]),
 "timeline": timeline([
   (2026, "Large-load tariffs", "Data-centre connection rules formalised", 0),
   (2027, "Storage build-out", "Capacity contracts replace arbitrage", 0),
   (2028, "AI grid operations", "Forecasting and outage automation at scale", 1),
   (2030, "First SMRs online", "FOAK costs and schedules tested", 1),
   (2032, "DER markets mature", "Aggregated flexibility priced", 2),
   (2035, "Transmission build-out", "New corridors relieve queues", 2)
 ]),
 "table": table(["P&L line", "Mechanism", "Timing", "Proof point"], [
   ["Rate base", "Data-centre and grid capex", "Now → 2032", "Capex approved in rate cases"],
   ["Allowed ROE", "Regulatory outcomes", "Each rate case", "Settled returns"],
   ["O&M cost", "Automation and predictive maintenance", "Now → 2029", "O&M per customer"],
   ["Capacity revenue", "Tight margins and storage", "2027 → 2033", "Capacity prices"],
   ["Bad debt", "Customer bill affordability", "2026 → 2030", "Arrears and disconnections"]
 ]),
 "gain": [
   "Regulated utilities in data-centre corridors with constructive regulators.",
   "Independent power producers with firm gas or nuclear capacity.",
   "Grid equipment makers and transmission developers.",
   "Storage operators with capacity contracts.",
   "Nuclear operators with licences and sites."
 ],
 "exposed": [
   "Merchant renewable generators without storage or contracts.",
   "Utilities in shrinking load regions with rising fixed costs.",
   "Coal-heavy fleets facing retirement capex.",
   "Developers stuck behind interconnection queues.",
   "Utilities with wildfire or storm liability exposure."
 ],
 "watch": [
   "<strong>Approved rate-base growth</strong> in each jurisdiction.",
   "<strong>Interconnection queue duration</strong> and withdrawal rates.",
   "<strong>Data-centre contracts</strong> with creditworthy counterparties.",
   "<strong>Capacity prices</strong> in tight markets.",
   "<strong>Customer arrears</strong> as bills rise."
 ],
 "research": "Linked records cover nuclear, storage, grid software and demand. Regulatory treatment of data-centre cost allocation is the single largest variable."
}
]

index = {d["deck"]: d for d in SECTORS}
for path in sorted(DECKS.glob("*.json")):
    deck = json.loads(path.read_text())
    data = index.get(deck["id"])
    if not data:
        continue
    deck["title"] = data["title"]
    deck["slides"] = [
        {"kind": "statement", "eyebrow": "01 · The thesis", "title": "The technology is not the story. The cost line is.",
         "body": data["thesis"]},
        {"kind": "points", "eyebrow": "02 · Sector economics", "title": "What this sector actually sells",
         "body": data["econ"], "bullets": data["econBullets"]},
        {"kind": "diagram", "eyebrow": "03 · Impact map", "title": "Where the impact lands",
         "body": "Two axes matter: how soon the effect reaches reported numbers, and whether it lands on revenue or on cost and capital.",
         "diagram": data["impact"]},
        {"kind": "diagram", "eyebrow": "04 · Exposure", "title": "How much of the sector is actually exposed",
         "diagram": data["bars"]},
        {"kind": "diagram", "eyebrow": "05 · Supply chain", "title": "The future products in the chain",
         "body": "Each stage is a product family that has to exist for the next one to work. This is where the spend lands.",
         "diagram": data["chain"]},
        {"kind": "columns", "eyebrow": "06 · Technology clusters", "title": "Three shifts to underwrite",
         "columns": data["clusters"]},
        {"kind": "diagram", "eyebrow": "07 · The stack", "title": "The stack underneath the sector",
         "diagram": data["stack"]},
        {"kind": "diagram", "eyebrow": "08 · Timing", "title": "When it reaches the numbers",
         "diagram": data["timeline"]},
        {"kind": "table", "eyebrow": "09 · Line by line", "title": "Where the money actually moves",
         "table": data["table"]},
        {"kind": "points", "eyebrow": "10 · Winners", "title": "Who gains",
         "bullets": data["gain"]},
        {"kind": "points", "eyebrow": "11 · Exposure", "title": "Who is exposed",
         "bullets": data["exposed"]},
        {"kind": "points", "eyebrow": "12 · Signposts", "title": "What to watch next",
         "body": "Signposts are chosen so that each one can falsify part of the thesis within four quarters.",
         "bullets": data["watch"]},
        {"kind": "research", "eyebrow": "13 · Evidence", "title": "Read the research behind this deck",
         "body": data["research"],
         "footnote": "Scenario synthesis compiled 19 November 2026. Directional shares and timelines are analytical judgements, not measured statistics or forecasts. Each technology record carries its own confidence label and source path."}
    ]
    path.write_text(json.dumps(deck, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {path.name}: {len(deck['slides'])} slides")
