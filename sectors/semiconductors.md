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
    <p><strong>Investment angle:</strong> TSMC pricing power increases with each node generation. Advanced node wafer prices are 2-3x mature node prices. The Arizona fabs add CHIPS Act subsidies ($6.6B) and geopolitical de-risking premium to the thesis. <span class="ticker-badge"><a href="/future/stocks/tsm/" style="color:inherit">TSM</a></span></p>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    EUV Lithography <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>ASML is the only company in the world that manufactures EUV lithography machines. Without ASML, there is no 3nm, 2nm, or 1.4nm production. Each EUV machine (NXE:3800) costs ~€200M. The next generation High-NA EUV (EXE:5000) — required for A14 and beyond — costs over €350M per unit. ASML's order book extends through 2026.</p>
    <p><strong>Investment angle:</strong> This is a legal monopoly protected by physics. High-NA EUV transitions the machine from a capital good to a platform — new optics, new process chemistry, new software. ASML captures more value per chip generation than any other capital equipment company. <span class="ticker-badge"><a href="/future/stocks/asml/" style="color:inherit">ASML</a></span></p>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    Advanced Packaging <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>CoWoS (Chip-on-Wafer-on-Substrate) packages GPU dies and HBM memory on a silicon interposer. Every NVIDIA H100, H200, and B200 requires CoWoS. TSMC holds an effective monopoly on advanced AI packaging. CoWoS capacity is the supply constraint that determines how many AI accelerators can ship — not die yields.</p>
    <p>The next generation is SoIC-X (wafer-on-wafer stacking without interposers) — pilot production targeted 2027, doubling effective transistor density versus CoWoS chiplets.</p>
    <p><strong>Investment angle:</strong> TSMC packaging revenue is growing faster than wafer revenue. AMAT and LRCX supply wafer bonding and deposition equipment for packaging. <span class="ticker-badge"><a href="/future/stocks/tsm/" style="color:inherit">TSM</a></span> <span class="ticker-badge"><a href="/future/stocks/amat/" style="color:inherit">AMAT</a></span> <span class="ticker-badge"><a href="/future/stocks/lrcx/" style="color:inherit">LRCX</a></span></p>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    HBM Memory <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>High Bandwidth Memory (HBM3E) delivers over 1TB/s bandwidth by stacking DRAM dies on the same interposer as the GPU. Each B200 GPU ships with 192GB HBM3E across 8 stacks. SK Hynix currently dominates HBM supply; Micron (MU) is qualifying to take meaningful share in 2025-2026. HBM margins are significantly better than commodity DRAM — a successful HBM3E qualification is a multi-year revenue and margin catalyst.</p>
    <p><strong>Investment angle:</strong> Micron is the value play on HBM — DRAM cycle turning up with an AI-specific premium. SK Hynix is not listed in the US. <span class="ticker-badge"><a href="/future/stocks/mu/" style="color:inherit">MU</a></span></p>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    Fabless Design <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>NVIDIA, AMD, Qualcomm, Broadcom, Marvell, and ARM design chips but outsource manufacturing to TSMC. This is where the most value is created in the stack — design IP compounds while manufacturing is outsourced. NVIDIA's CUDA software stack is as much a competitive advantage as its chip architecture — switching costs are measured in years of developer retraining.</p>
    <p><strong>Investment angle:</strong> NVIDIA is the primary beneficiary. AMD MI300X is the only credible GPU competitor at scale. ARM's royalty model scales with every chip shipped regardless of architecture outcome. <span class="ticker-badge"><a href="/future/stocks/nvda/" style="color:inherit">NVDA</a></span> <span class="ticker-badge"><a href="/future/stocks/amd/" style="color:inherit">AMD</a></span> <span class="ticker-badge"><a href="/future/stocks/arm/" style="color:inherit">ARM</a></span> <span class="ticker-badge"><a href="/future/stocks/avgo/" style="color:inherit">AVGO</a></span></p>
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
| [MRVL](/stocks/MRVL/) | Marvell | ASICs, photonics | <span class="conf-badge conf-confident">Confident</span> |
| [INTC](/stocks/INTC/) | Intel | IDM, x86, foundry | <span class="conf-badge conf-researching">Researching</span> |

---

## Causal Signals

Research from the macro pipeline identifies semiconductor-relevant causal chains:

- **TSMC CoWoS capacity → AI accelerator supply**: CoWoS capacity is the binding constraint on AI GPU availability. Quarterly TSMC CoWoS capacity announcements are the clearest leading indicator for NVIDIA supply.
- **WFE orders → Semiconductor capex cycle**: ASML bookings are the 12-month leading indicator for the broader chip equipment cycle (AMAT, LRCX, KLAC).
- **HBM ASP → Memory cycle**: HBM is to this memory upcycle what DDR4 was to the 2017-2018 server memory cycle — a premium product driving margin expansion while the commodity DRAM market is irrelevant.

<script>
function toggleAcc(btn) {
  const body = btn.nextElementSibling;
  const isOpen = body.classList.contains('open');
  btn.classList.toggle('open', !isOpen);
  body.classList.toggle('open', !isOpen);
}
</script>
