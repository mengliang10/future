---
layout: page
title: Autonomous Vehicles
subtitle: Full self-driving, lidar sensors, autonomous trucking, and the end of human-piloted transport.
category: Sector
permalink: /sectors/autonomous/
---

<div class="callout callout-info">
  <span class="callout-icon">&#128664;</span>
  <span>Waymo is running 150,000+ autonomous rides per week in four US cities. Aurora launched commercial driverless trucking in Texas. The technology works in constrained environments. Scaling is now the question.</span>
</div>

## Why This Sector Matters

Full self-driving is the most consequential automation event in transport history. The global taxi and truck driving market represents ~$4T in annual wages. When autonomous systems are demonstrably safer, cheaper, and available 24/7, the displacement is inevitable — not speculative. The sensor cost curve has dropped 10× in five years: a lidar unit that cost $75,000 in 2017 costs $500–1,000 today. Waymo proved safety at city scale. Tesla is proving vision-only viability at consumer scale. Aurora proved commercial viability in interstate trucking. The race is now for deployment speed, not basic functionality.

---

## Technology Nodes

| Technology | Confidence | Est. Year |
|---|---|---|
| [Adaptive Cruise Control (ACC)](/future/tech/adaptive-cruise-control-acc/) | <span class="conf-badge conf-confirmed">Confirmed</span> | Deployed |
| [ADAS Level 2 (Partial Automation)](/future/tech/adas-level-2-partial-automation/) | <span class="conf-badge conf-confirmed">Confirmed</span> | Deployed |
| [AV Sensor Fusion (Cam+LiDAR+Radar)](/future/tech/av-sensor-fusion-camlidarradar/) | <span class="conf-badge conf-confirmed">Confirmed</span> | Deployed |
| [High-Definition Mapping (HD Map)](/future/tech/high-definition-mapping-hd-map/) | <span class="conf-badge conf-confirmed">Confirmed</span> | Deployed |
| [ADAS Level 3 (Conditional Highway)](/future/tech/adas-level-3-conditional-highway/) | <span class="conf-badge conf-confident">Confident</span> | — |
| [Robotaxi (Geofenced Operation)](/future/tech/robotaxi-geofenced-operation/) | <span class="conf-badge conf-confident">Confident</span> | — |
| [Solid-State LiDAR](/future/tech/solid-state-lidar/) | <span class="conf-badge conf-confident">Confident</span> | 2025 |
| [Autonomous Trucking (Highway ODD)](/future/tech/autonomous-trucking-highway-odd/) | <span class="conf-badge conf-confident">Confident</span> | 2025 |
| [Robotaxi (Full City, No Safety Driver)](/future/tech/robotaxi-full-city-no-safety-driver/) | <span class="conf-badge conf-confident">Confident</span> | 2027 |
| [Full Self-Driving Level 4 (Urban)](/future/tech/full-self-driving-level-4-urban/) | <span class="conf-badge conf-confident">Confident</span> | 2028 |
| [eVTOL Air Taxi](/future/tech/evtol-air-taxi/) | <span class="conf-badge conf-confident">Confident</span> | 2028 |
| [V2X Vehicle-to-Everything Comms](/future/tech/v2x-vehicle-to-everything-comms/) | <span class="conf-badge conf-researching">Researching</span> | 2030 |
| [Zero-Accident Transport Network](/future/tech/zero-accident-transport-network/) | <span class="conf-badge conf-speculative">Speculative</span> | 2042 |

---

## Sub-Themes

<div class="accordion-item">
  <button class="accordion-toggle open" onclick="toggleAcc(this)">
    Full Self-Driving — Waymo vs Tesla <span class="acc-arrow" style="transform:rotate(180deg);">&#9660;</span>
  </button>
  <div class="accordion-body open">
    <p>Waymo and Tesla represent two fundamentally different philosophical bets. Waymo uses sensor redundancy (lidar + cameras + radar + HD maps) to build a safety-first system validated in limited geographies. Tesla uses cameras only, using the largest labelled-driving-data fleet on earth (6M+ cars) to train a neural network that generalises across any road. Waymo is safer in known geographies; Tesla's approach scales globally without per-city HD map costs. Both approaches are being validated simultaneously — they will likely coexist across different use cases and markets.</p>
    <p>Waymo's commercial service (Alphabet subsidiary) is not separately listed. The equity access is through GOOGL. Tesla's FSD is a $15B+ revenue optionality sitting inside an EV manufacturer that the market is pricing at near-zero today.</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/tsla/" style="color:inherit">TSLA</a></span> <span class="ticker-badge"><a href="/future/stocks/googl/" style="color:inherit">GOOGL</a></span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    Autonomous Trucking — The Commercial Prize <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>Aurora Innovation launched commercial driverless trucking on Interstate 45 (Dallas-Houston) in April 2024 — the first commercial deployment of driverless Class 8 trucks in history. The highway-only, point-to-point operational domain (ODD) is simpler than urban driving: fewer variables, predictable routes, and an enormous commercial prize ($700B US trucking market). Aurora's fleet includes partnerships with Uber Freight and FedEx. The risk is that Aurora needs capital to scale, is pre-profit, and the path from 10 trucks to 1,000 trucks involves significant capex and regulatory complexity across multiple states.</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/uber/" style="color:inherit">UBER</a></span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    LiDAR & Sensors — Commodity Pressure and Survival <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>LiDAR hardware is commoditising faster than anyone predicted. Luminar (LAZR) has design wins with Volvo and Mercedes for highway ADAS. Innoviz (INVZ) ships in BMW vehicles. But solid-state LiDAR from Chinese manufacturers (Hesai, RoboSense — both listed in Hong Kong) is now at $100–200/unit, compressing the economics for US-listed LiDAR names. Mobileye (MBLY) is the dominant ADAS chip supplier, with its EyeQ series in 800+ vehicle models — a more defensible position than hardware-only sensor vendors. The investable LiDAR thesis requires a specific OEM design win at mass-production volumes; otherwise it's a race to the bottom on hardware margins.</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/mbly/" style="color:inherit">MBLY</a></span> <span class="ticker-badge"><a href="/future/stocks/lazr/" style="color:inherit">LAZR</a></span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    eVTOL Air Taxis — The Decade-Long Build <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>Joby Aviation (JOBY), Archer Aviation (ACHR), and Lilium (restructured) are building FAA-certified electric vertical takeoff and landing aircraft for urban air mobility. Joby received its Part 135 air carrier certificate and is targeting commercial operations in 2025–2026. The market opportunity is genuine — a $1T urban air mobility market by 2040 — but the execution risk is severe. Battery energy density, FAA certification pathways, charging infrastructure, and noise regulations in dense urban areas are all unsolved at scale. These are 2028–2030 revenue stories, not 2025 stories, and will require continuous capital raises before profitability.</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/joby/" style="color:inherit">JOBY</a></span></div>
  </div>
</div>

---

## Key Stocks

| Ticker | Company | Role | Confidence |
|--------|---------|------|------------|
| [TSLA](/stocks/TSLA/) | Tesla | Vision-only FSD + robotaxi | <span class="conf-badge conf-confident">Confident</span> |
| [GOOGL](/stocks/GOOGL/) | Alphabet (Waymo) | Robotaxi at city scale | <span class="conf-badge conf-confident">Confident</span> |
| [MBLY](/stocks/MBLY/) | Mobileye | ADAS chips + SuperVision | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [LAZR](/stocks/LAZR/) | Luminar Technologies | LiDAR for OEM ADAS | <span class="conf-badge conf-researching">Researching</span> |
| [UBER](/stocks/UBER/) | Uber | AV fleet aggregator | <span class="conf-badge conf-confident">Confident</span> |
| [JOBY](/stocks/JOBY/) | Joby Aviation | eVTOL air taxi | <span class="conf-badge conf-researching">Researching</span> |

---

## Causal Signals

- **Regulatory milestones** — NHTSA exemptions from Federal Motor Vehicle Safety Standards, state-level driverless permits, and FAA Part 135 certificates are discrete catalysts. Waymo's permit expansions into new cities (Phoenix → Atlanta, etc.) move the stock.
- **Disengagement data** — California DMV annual AV disengagement reports are the only independently verified safety metric for AV performance. Fewer disengagements per mile is the signal. Waymo leads by orders of magnitude.
- **LiDAR cost curve** — when solid-state LiDAR consistently hits below $200/unit from multiple suppliers, the economic case for sensor-redundant ADAS becomes compelling for mid-market OEMs. Track annual component pricing from CES announcements.
- **Tesla FSD subscription attach rate and miles driven** — disclosed quarterly. Rising attach rate and declining insurance costs per mile are the leading indicators that FSD is becoming commercially viable rather than a supervised system.

<script>
function toggleAcc(btn) {
  const body = btn.nextElementSibling;
  const isOpen = body.classList.contains('open');
  btn.classList.toggle('open', !isOpen);
  body.classList.toggle('open', !isOpen);
}
</script>
