---
layout: page
title: Advanced Semiconductors
subtitle: Foundries, fabless design, EUV lithography, advanced packaging, and the global chip supply chain.
category: Sector
permalink: /sectors/semiconductors/
---

<div class="callout callout-info">
  <span class="callout-icon">&#128421;</span>
  <span>Semiconductors are the oil of the 21st century. Every AI model, every autonomous vehicle, every connected device runs on chips — and TSMC and ASML are the two most irreplaceable companies in the world.</span>
</div>

## Why This Sector Matters

The semiconductor industry underpins every technology on this site. It is the most capital-intensive, technically complex, and geopolitically sensitive industry in the world. Three companies — TSMC, ASML, and NVIDIA — between them control the chokepoints for the entire AI infrastructure buildout.

---

## Node Roadmap

| Node | Status | Year | Key Player | Confidence |
|------|--------|------|-----------|------------|
| 3nm (N3E) | Volume production | 2023 | TSMC | <span class="conf-badge conf-confirmed">Confirmed</span> |
| 2nm (N2) | Volume production | 2025 | TSMC | <span class="conf-badge conf-confirmed">Confirmed</span> |
| High-NA EUV | Pilot at TSMC/Intel | 2025 | ASML | <span class="conf-badge conf-confident">Confident</span> |
| 1.4nm (A14) | Risk production | 2026 | TSMC | <span class="conf-badge conf-confident">Confident</span> |
| 1nm (A10/A10P) | Development | 2027–2028 | TSMC, Intel | <span class="conf-badge conf-researching">Researching</span> |
| Wafer-on-Wafer 3D | Pilot | 2027 | TSMC SoIC-X | <span class="conf-badge conf-researching">Researching</span> |
| Sub-1nm | Research phase | 2030+ | All | <span class="conf-badge conf-speculative">Speculative</span> |

---

## Sub-Themes

<div class="accordion-item">
  <button class="accordion-toggle open" onclick="toggleAcc(this)">
    Foundries <span class="acc-arrow" style="transform:rotate(180deg);">&#9660;</span>
  </button>
  <div class="accordion-body open">
    <p>TSMC manufactures over 90% of the world's most advanced chips (below 5nm). Samsung and Intel Foundry are the only credible challengers at leading-edge nodes, but both trail TSMC by at least one generation on yield. The TSMC Arizona fabs (Fab 21 Phase 1: N4, Phase 2: N2) are the first advanced node production on US soil since 2001.</p>
    <p>The transition to 2nm (GAA/NanoSheet) and High-NA EUV is the most expensive technical hurdle in foundry history. Foundries are no longer competing on price — they compete on yield. Intel 18A (RibbonFET GAA) is the wildcard: a success unlocks Intel Foundry as a credible third option; continued yield struggles confirm TSMC's permanent premium.</p>
    <p><strong>Investment angle:</strong> TSMC pricing power increases with each node generation. Advanced node wafer prices are 2-3x mature node prices. The Arizona fabs add CHIPS Act subsidies ($6.6B) and geopolitical de-risking premium to the thesis. Intel 18A client announcements are the binary catalyst for INTC. <span class="ticker-badge"><a href="/future/stocks/tsm/" style="color:inherit">TSM</a></span> <span class="ticker-badge"><a href="/future/stocks/intc/" style="color:inherit">INTC</a></span></p>
  <div class="roadmap-leader-box"><span class="roadmap-leader-label">Leader:</span> <span class="race-badge race-lead"><a href="/future/stocks/tsm/" style="color:inherit">TSM</a> &middot; 95%</span> <span class="roadmap-rivals-sep">vs <a href="/future/stocks/intc/">INTC</a> 80%</span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    EUV Lithography <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>ASML is the only company in the world that manufactures EUV lithography machines. Without ASML, there is no 3nm, 2nm, or 1.4nm production. Each EUV machine (NXE:3800) costs ~€200M. The next generation High-NA EUV (EXE:5000) — required for A14 and beyond — costs over €350M per unit. ASML's order book extends through 2026.</p>
    <p>WFE (Wafer Fab Equipment) TAM is shifting from pure logic into packaging equipment as advanced packaging complexity increases. AMAT and LRCX supply critical etch/deposition tools for both logic shrink and TSV (through-silicon via) packaging. KLAC process control improves yield — every percentage point of yield improvement at N2 is worth hundreds of millions in wafer revenue.</p>
    <p><strong>Investment angle:</strong> This is a legal monopoly protected by physics. High-NA EUV transitions the machine from a capital good to a platform. ASML bookings are the 12-month leading indicator for the entire WFE cycle. <span class="ticker-badge"><a href="/future/stocks/asml/" style="color:inherit">ASML</a></span> <span class="ticker-badge"><a href="/future/stocks/amat/" style="color:inherit">AMAT</a></span> <span class="ticker-badge"><a href="/future/stocks/lrcx/" style="color:inherit">LRCX</a></span> <span class="ticker-badge"><a href="/future/stocks/klac/" style="color:inherit">KLAC</a></span></p>
  <div class="roadmap-leader-box"><span class="roadmap-leader-label">Leader:</span> <span class="race-badge race-supply"><a href="/future/stocks/asml/" style="color:inherit">ASML</a> &middot; 90%</span> <span class="roadmap-rivals-sep">vs <a href="/future/stocks/amat/">AMAT</a> 78% &middot; <a href="/future/stocks/klac/">KLAC</a> 75% &middot; <a href="/future/stocks/lrcx/">LRCX</a> 75% &middot; +3 more</span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    Advanced Packaging <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>CoWoS (Chip-on-Wafer-on-Substrate) packages GPU dies and HBM memory on a silicon interposer. Every NVIDIA H100, H200, and B200 requires CoWoS. TSMC holds an effective monopoly on advanced AI packaging. CoWoS capacity is the supply constraint that determines how many AI accelerators can ship — not die yields.</p>
    <p>The next generation is SoIC-X (wafer-on-wafer stacking without interposers) — pilot production targeted 2027, doubling effective transistor density versus CoWoS chiplets. Moore's Law 2.0: performance is now driven by packaging (vertical stacking) rather than just transistor shrink. Dark silicon — cooling limits on active transistors — is the new physics boundary replacing gate length.</p>
    <p><strong>Investment angle:</strong> TSMC packaging revenue is growing faster than wafer revenue. AMAT and LRCX supply wafer bonding and deposition equipment for packaging. <span class="ticker-badge"><a href="/future/stocks/tsm/" style="color:inherit">TSM</a></span> <span class="ticker-badge"><a href="/future/stocks/amat/" style="color:inherit">AMAT</a></span> <span class="ticker-badge"><a href="/future/stocks/lrcx/" style="color:inherit">LRCX</a></span></p>
  <div class="roadmap-leader-box"><span class="roadmap-leader-label">Leader:</span> <span class="race-badge race-lead"><a href="/future/stocks/tsm/" style="color:inherit">TSM</a> &middot; 99%</span> <span class="roadmap-rivals-sep">vs <a href="/future/stocks/amat/">AMAT</a> 78% &middot; <a href="/future/stocks/lrcx/">LRCX</a> 75% &middot; +4 more</span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    HBM &amp; Memory Stack <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>High Bandwidth Memory (HBM3E) delivers over 1TB/s bandwidth by stacking DRAM dies on the same interposer as the GPU. Each B200 GPU ships with 192GB HBM3E across 8 stacks. SK Hynix currently dominates HBM supply; Micron is qualifying to take meaningful share in 2025–2026. HBM margins are significantly better than commodity DRAM — a successful HBM3E qualification is a multi-year revenue and margin catalyst.</p>
    <p>Below HBM in the memory hierarchy: DDR5 (system memory — AI servers require 4x the capacity of traditional servers), then enterprise NVMe SSD (QLC NAND replacing HDDs in the data centre), then cold HDD storage. The AI-driven shift is raising the floor on pricing across all tiers.</p>
    <p><strong>Trading signal:</strong> SK Hynix HBM3E yield issues create pricing power asymmetry. Watch Micron inventory levels — peak inventory followed by decline is the generational buy signal. Samsung HBM3E NVIDIA certification is the binary catalyst for the laggard discount to close.</p>
    <p><strong>Investment angle:</strong> Micron is the value play on HBM. WDC HDD/Flash business split is a value-unlock catalyst. <span class="ticker-badge"><a href="/future/stocks/mu/" style="color:inherit">MU</a></span> <span class="ticker-badge"><a href="/future/stocks/ter/" style="color:inherit">TER</a></span></p>
  <div class="roadmap-leader-box"><span class="roadmap-leader-label">Leader:</span> <span class="race-badge race-mono"><a href="/future/stocks/mu/" style="color:inherit">MU</a> &middot; 82%</span> <span class="roadmap-rivals-sep">no rivals identified</span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    Fabless Design &amp; Custom Silicon <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>NVIDIA, AMD, Qualcomm, Broadcom, Marvell, and ARM design chips but outsource manufacturing to TSMC. This is where the most value is created in the stack — design IP compounds while manufacturing is outsourced. NVIDIA's CUDA software stack is as much a competitive advantage as its chip architecture — switching costs are measured in years of developer retraining.</p>
    <p>Architecture comparison (flagship AI accelerators): NVIDIA Blackwell B200 (TSMC 4NP, 1600mm², 208B transistors), AMD Instinct MI300X (TSMC 5/6nm, 1000mm², 153B transistors), Intel Gaudi 3 (TSMC 5nm). RISC-V vs ARM battle is the key long-term design IP contest — ARM holds mobile dominance, RISC-V is the open-source challenger for edge and embedded.</p>
    <p><strong>Investment angle:</strong> NVIDIA is the primary beneficiary. AMD MI300X is the only credible GPU competitor at scale. ARM's royalty model scales with every chip shipped regardless of architecture outcome. Companies iterating on silicon yearly (like NVIDIA) trade at permanent multiple premiums over 2-year cycle players. <span class="ticker-badge"><a href="/future/stocks/nvda/" style="color:inherit">NVDA</a></span> <span class="ticker-badge"><a href="/future/stocks/amd/" style="color:inherit">AMD</a></span> <span class="ticker-badge"><a href="/future/stocks/arm/" style="color:inherit">ARM</a></span> <span class="ticker-badge"><a href="/future/stocks/avgo/" style="color:inherit">AVGO</a></span></p>
  <div class="roadmap-leader-box"><span class="roadmap-leader-label">Leader:</span> <span class="race-badge race-lead"><a href="/future/stocks/nvda/" style="color:inherit">NVDA</a> &middot; 90%</span> <span class="roadmap-rivals-sep">vs <a href="/future/stocks/arm/">ARM</a> 80% &middot; <a href="/future/stocks/avgo/">AVGO</a> 70% &middot; <a href="/future/stocks/amd/">AMD</a> 65% &middot; +2 more</span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    AI Networking &amp; Silicon Photonics <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>As GPU clusters scale from 8K to 100K+ GPUs, networking becomes the AI backplane. Tail latency — the slowest link in the cluster — determines training throughput. The core debate: InfiniBand (NVIDIA/Mellanox, tightly coupled to the GPU stack) vs Ultra Ethernet (Arista/Broadcom, open standard gaining share). 800G optical transceivers are today's bottleneck; 1.6T is the next inflection.</p>
    <p>Silicon photonics (co-packaged optics, CPO) reduces power by ~30% vs pluggable optics. LPO (Linear Drive Pluggable Optics) is the intermediate step — Marvell is the leading DSP supplier. The shift from pluggable → CPO is a platform change, not just an upgrade, and reshuffles the optical supply chain.</p>
    <p><strong>Investment angle:</strong> Networking is a leading indicator for GPU build-outs — switch orders predict GPU revenue one quarter ahead. Arista is the AI-Ethernet pure-play. Broadcom captures value as switch silicon king. <span class="ticker-badge"><a href="/future/stocks/anet/" style="color:inherit">ANET</a></span> <span class="ticker-badge"><a href="/future/stocks/avgo/" style="color:inherit">AVGO</a></span> <span class="ticker-badge"><a href="/future/stocks/mrvl/" style="color:inherit">MRVL</a></span></p>
  <div class="roadmap-leader-box"><span class="roadmap-leader-label">Leader:</span> <span class="race-badge race-lead"><a href="/future/stocks/avgo/" style="color:inherit">AVGO</a> &middot; 88%</span> <span class="roadmap-rivals-sep">vs <a href="/future/stocks/mrvl/">MRVL</a> 78% &middot; +6 more</span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    AI Infrastructure Hardware <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>The software-dominant era of zero interest rates is giving way to a capex supercycle. Building AI requires physical infrastructure at unprecedented scale: custom servers, ultra-high-bandwidth networking, and massive storage systems. As racks move from 15kW to 100kW+ (GB200 NVL72), power density forces liquid and immersion cooling to become standard — a specialist industrial moat.</p>
    <p><strong>AI Servers:</strong> SMCI (Super Micro) is the fastest-growing AI server ODM with liquid-cooled rack specialisation. Dell is winning hyperscaler AI rack contracts. HPE repositioning toward AI infrastructure. Server design cycle times are compressing — integrators that qualify new GPU architectures fastest win disproportionate share.</p>
    <p><strong>Storage:</strong> AI training generates and requires massive storage throughput. Pure Storage (PSTG) and NetApp (NTAP) positioned for AI-adjacent storage growth. Traditional HDDs (STX, WDC) being displaced by flash in AI workloads at the hot tier.</p>
    <p><strong>Power &amp; Cooling:</strong> Vertiv (VRT) and Eaton hold specialist moats on high-density power distribution and liquid cooling. Power delivery is the binding constraint for new data centre builds in 2025–2027. Utility stocks (VST, CEG) are secondary beneficiaries of data centre load growth. <span class="ticker-badge"><a href="/future/stocks/nvda/" style="color:inherit">NVDA</a></span> <span class="ticker-badge"><a href="/future/stocks/vst/" style="color:inherit">VST</a></span> <span class="ticker-badge"><a href="/future/stocks/ceg/" style="color:inherit">CEG</a></span></p>
  <div class="roadmap-leader-box"><span class="roadmap-leader-label">Leader:</span> <span class="race-badge race-lead"><a href="/future/stocks/ceg/" style="color:inherit">CEG</a> &middot; 95%</span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    GPU Pricing Index <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>The GPU squeeze is bifurcating by architecture. Blackwell (B200/GB200) remains in structural deficit with zero spot availability and significant MSRP premiums. Hopper (H100/H200) has become liquid — spot rental rates declined ~20% MoM through 2025 as supply caught up with training demand. AMD MI300X availability is scaling with moderate pricing.</p>

    | Architecture | Availability | Trend | Signal |
    |---|---|---|---|
    | NVIDIA Blackwell | Structural deficit | Premium to MSRP | Long NVDA |
    | NVIDIA Hopper H100/H200 | Fully liquid | -20% spot rental | Neutral renters |
    | AMD MI300X | Scaling | Stable | Long AMD (value) |

    <p>The cost to generate 1M tokens is dropping exponentially — a bearish signal for "dumb" compute providers and bullish for AI-native applications that capture the margin freed up by lower input costs. Watch H100 spot rates: below $1.50/hr signals the compute-as-a-service trade is fully repriced.</p>
    <p><strong>Rotation signal:</strong> When GPU lead times drop below 12 weeks, rotate from hardware layer into the software layer deploying those models. <span class="ticker-badge"><a href="/future/stocks/nvda/" style="color:inherit">NVDA</a></span> <span class="ticker-badge"><a href="/future/stocks/amd/" style="color:inherit">AMD</a></span></p>
  <div class="roadmap-leader-box"><span class="roadmap-leader-label">Leader:</span> <span class="race-badge race-lead"><a href="/future/stocks/nvda/" style="color:inherit">NVDA</a> &middot; 90%</span> <span class="roadmap-rivals-sep">vs <a href="/future/stocks/amd/">AMD</a> 65% &middot; +4 more</span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    Global Fab Geography <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>Where chips are made is as important as how they are made. Taiwan produces ~90% of advanced logic today. The CHIPS Act is driving the first meaningful geographic diversification in decades. TSMC Arizona (Fab 21) runs N4 (Phase 1) and N2 (Phase 2, 2026). Intel has fabs in Oregon (leading-edge R&D), Arizona (Chandler manufacturing), and New Mexico (back-end). Samsung's Pyeongtaek mega-site holds the highest single-location advanced capacity outside Taiwan.</p>
    <p>Japan is building a second node via Rapidus (2nm, targeting 2027 volume) and TSMC Kumamoto (N16/N12, already in production). The Kumamoto partnership with Sony creates a captive image sensor supply chain. Any "on-schedule" milestone from Rapidus or TSMC Arizona Phase 2 is a de-risking event for the entire supply chain.</p>
    <p>China is targeting mature node dominance (28nm+) via SMIC, CXMT, and YMTC — supplying the EV/industrial/consumer electronics market with surplus capacity that suppresses mature node ASPs globally. Export controls on advanced tooling (ASML EUV, AMAT CVD) are the primary constraint on China's path to leading-edge. <span class="ticker-badge"><a href="/future/stocks/tsm/" style="color:inherit">TSM</a></span> <span class="ticker-badge"><a href="/future/stocks/asml/" style="color:inherit">ASML</a></span> <span class="ticker-badge"><a href="/future/stocks/intc/" style="color:inherit">INTC</a></span></p>
  <div class="roadmap-leader-box"><span class="roadmap-leader-label">Leader:</span> <span class="race-badge race-supply"><a href="/future/stocks/asml/" style="color:inherit">ASML</a> &middot; 95%</span> <span class="roadmap-rivals-sep">vs <a href="/future/stocks/tsm/">TSM</a> 85% &middot; <a href="/future/stocks/intc/">INTC</a> 70% &middot; +1 more</span></div>
  </div>
</div>

---

## Key Stocks

| Ticker | Company | Role | Stage |
|--------|---------|------|-------|
| [TSM](/stocks/TSM/) | TSMC | Leading-edge foundry | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [ASML](/stocks/ASML/) | ASML | EUV monopoly | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [NVDA](/stocks/NVDA/) | NVIDIA | Fabless GPU/AI | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [AMD](/stocks/AMD/) | AMD | Fabless GPU/CPU | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [AMAT](/stocks/AMAT/) | Applied Materials | WFE equipment | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [LRCX](/stocks/LRCX/) | Lam Research | Etch/CVD equipment | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [KLAC](/stocks/KLAC/) | KLA Corp | Process control | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [MU](/stocks/MU/) | Micron | HBM/DRAM/NAND | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [ARM](/stocks/ARM/) | ARM Holdings | ISA royalties | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [AVGO](/stocks/AVGO/) | Broadcom | Custom ASICs, networking | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [ANET](/stocks/ANET/) | Arista Networks | AI-Ethernet switching | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [MRVL](/stocks/MRVL/) | Marvell | ASICs, photonics | <span class="conf-badge conf-confident">Confident</span> |
| [VST](/stocks/VST/) | Vistra Energy | Data centre power | <span class="conf-badge conf-confident">Confident</span> |
| [CEG](/stocks/CEG/) | Constellation Energy | Nuclear power for AI | <span class="conf-badge conf-confident">Confident</span> |
| [INTC](/stocks/INTC/) | Intel | IDM, x86, foundry | <span class="conf-badge conf-researching">Researching</span> |

---

## Causal Signals

- **TSMC CoWoS capacity → AI accelerator supply**: CoWoS capacity is the binding constraint on AI GPU availability. Quarterly TSMC CoWoS capacity announcements are the clearest leading indicator for NVIDIA supply.
- **ASML bookings → WFE cycle**: ASML bookings are the 12-month leading indicator for the broader chip equipment cycle (AMAT, LRCX, KLAC).
- **HBM ASP → Memory cycle**: HBM is to this memory upcycle what DDR4 was to the 2017-2018 server memory cycle — premium product driving margin expansion while commodity DRAM is irrelevant.
- **Switch orders → GPU revenue (lead indicator)**: Networking equipment orders precede GPU cluster deployments by one quarter. ANET order trends are an early signal for NVDA data centre revenue.
- **GPU lead times → hardware/software rotation**: Lead times below 12 weeks signal compute supply has caught up; rotate from hardware (NVDA, AMAT) into the software layer (cloud, SaaS).

<script>
function toggleAcc(btn) {
  const body = btn.nextElementSibling;
  const isOpen = body.classList.contains('open');
  btn.classList.toggle('open', !isOpen);
  body.classList.toggle('open', !isOpen);
}
</script>
