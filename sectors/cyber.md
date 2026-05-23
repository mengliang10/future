---
layout: page
title: Cybersecurity
subtitle: The permanent arms race — AI-native defence platforms winning at scale in an expanding attack surface.
category: Sector
permalink: /sectors/cyber/
---

<div class="callout callout-info">
  <span class="callout-icon">&#128274;</span>
  <span>Cyber is one of the most durable growth sectors: every new device, AI agent, and connected infrastructure expands the attack surface. Spending never has a down cycle — only a budget reallocation toward more effective platforms.</span>
</div>

## Why This Sector Matters

AI has restructured the economics of both offence and defence. Attackers now generate novel malware variants in minutes with LLMs. Defenders use AI to detect behavioural anomalies in milliseconds across millions of endpoints. The platform consolidation era has arrived: CISOs who once managed 30+ point security products are now buying 3–5 platforms that do everything. CrowdStrike, Palo Alto, and Zscaler are the platform consolidators — winning on breadth, AI quality, and the economic argument that fewer vendors means lower total cost. The post-quantum cryptography migration adds a mandatory 5–7 year infrastructure upgrade cycle on top of the secular growth.

---

## Technology Nodes

| Technology | Confidence | Est. Year |
|---|---|---|
| [Public Key Cryptography (RSA/ECC)](/future/tech/public-key-cryptography-rsaecc/) | <span class="conf-badge conf-confirmed">Confirmed</span> | Deployed |
| [TLS/SSL Encrypted Transport](/future/tech/tlsssl-encrypted-transport/) | <span class="conf-badge conf-confirmed">Confirmed</span> | Deployed |
| [EDR (Endpoint Detection & Response)](/future/tech/edr-endpoint-detection-response/) | <span class="conf-badge conf-confirmed">Confirmed</span> | Deployed |
| [Hardware Security Module (HSM)](/future/tech/hardware-security-module-hsm/) | <span class="conf-badge conf-confirmed">Confirmed</span> | Deployed |
| [Zero Trust Security Architecture](/future/tech/zero-trust-security-architecture/) | <span class="conf-badge conf-confident">Confident</span> | 2019 |
| [Confidential Computing (TEE)](/future/tech/confidential-computing-tee/) | <span class="conf-badge conf-confident">Confident</span> | 2019 |
| [XDR (Extended Detection & Response)](/future/tech/xdr-extended-detection-response/) | <span class="conf-badge conf-confident">Confident</span> | 2024 |
| [SASE (Secure Access Service Edge)](/future/tech/sase-secure-access-service-edge/) | <span class="conf-badge conf-confident">Confident</span> | 2025 |
| [AI-Driven Threat Detection](/future/tech/ai-driven-threat-detection/) | <span class="conf-badge conf-confident">Confident</span> | 2026 |
| [Homomorphic Encryption (Practical)](/future/tech/homomorphic-encryption-practical/) | <span class="conf-badge conf-researching">Researching</span> | 2030 |
| [Secure Multi-Party Computation](/future/tech/secure-multi-party-computation/) | <span class="conf-badge conf-researching">Researching</span> | 2030 |
| [Quantum Key Distribution Network](/future/tech/quantum-key-distribution-network/) | <span class="conf-badge conf-speculative">Speculative</span> | — |
| [AI-Autonomous Security Operations Centre](/future/tech/ai-autonomous-security-operations-centre/) | <span class="conf-badge conf-speculative">Speculative</span> | — |

---

## Sub-Themes

<div class="accordion-item">
  <button class="accordion-toggle open" onclick="toggleAcc(this)">
    Platform Consolidation — CrowdStrike, Palo Alto, Zscaler <span class="acc-arrow" style="transform:rotate(180deg);">&#9660;</span>
  </button>
  <div class="accordion-body open">
    <p>Enterprise security is consolidating from 30+ point products to 3–5 integrated platforms. The economics drive this: a single-vendor XDR + SASE + identity platform is 30–40% cheaper in total cost of ownership than the equivalent point-solution stack, with faster detection and response. CrowdStrike (CRWD) won endpoint; its Falcon platform now extends to cloud workloads, identity, and data. Palo Alto (PANW) is the broadest consolidator — NGFW hardware + Prisma SASE + Cortex AI — and has explicitly guided to 15–20% incremental revenue from platformisation. The metric to watch: net retention rate (NRR). CRWD at 120%+ NRR means every customer expands by 20% per year without new logos.</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/crwd/" style="color:inherit">CRWD</a></span> <span class="ticker-badge"><a href="/future/stocks/panw/" style="color:inherit">PANW</a></span> <span class="ticker-badge"><a href="/future/stocks/zs/" style="color:inherit">ZS</a></span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    Identity & Zero Trust — Okta and the Identity Perimeter <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>Zero trust replaces the castle-and-moat model with an identity-centric model: every user, device, and application must authenticate every request, continuously. Okta (OKTA) is the dominant identity-as-a-service vendor with 19,000+ enterprise customers. The 2023 breach (Cloudflare, BeyondTrust data exposed) damaged trust and slowed growth — but the zero-trust mandate has not changed. CyberArk (CYBR) specialises in privileged access management — controlling the keys that attackers most want to steal. When a breach occurs, it is almost always through compromised credentials: identity is the attack surface that matters most.</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/okta/" style="color:inherit">OKTA</a></span> <span class="ticker-badge"><a href="/future/stocks/cybr/" style="color:inherit">CYBR</a></span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    AI-Native Security — SentinelOne and the Autonomous SOC <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>SentinelOne (S) built its platform AI-first rather than retrofitting AI onto a rules-based system. Its Purple AI automates threat investigation and response — what previously took a security analyst 30 minutes is summarised in 30 seconds. The autonomous SOC (where AI handles Tier-1 and Tier-2 alert triage with zero human intervention) is 2–3 years away, but the direction is clear. The risk for S is that CrowdStrike and Palo Alto have larger customer bases to cross-sell AI into, and will close the AI quality gap faster than S can close the customer base gap.</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/s/" style="color:inherit">S</a></span> <span class="ticker-badge"><a href="/future/stocks/net/" style="color:inherit">NET</a></span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    Post-Quantum Cryptography Migration — Mandated Infrastructure Upgrade <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>NIST's four finalised PQC algorithms create a federal mandate with a 2030 deadline for classified systems. Every enterprise with government contracts or regulated data follows the same clock. This is a $50–100B forced infrastructure upgrade: every TLS certificate, VPN connection, encrypted storage system, and HSM must be re-keyed with quantum-resistant algorithms. The benefit flows to the platforms already embedded in enterprise security stacks — CrowdStrike, Palo Alto, Okta, and Cloudflare are all updating their encryption layers. There is no "do nothing" option: attackers are collecting encrypted data today to decrypt when quantum computers arrive ("harvest now, decrypt later").</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/panw/" style="color:inherit">PANW</a></span> <span class="ticker-badge"><a href="/future/stocks/net/" style="color:inherit">NET</a></span> <span class="ticker-badge"><a href="/future/stocks/ibm/" style="color:inherit">IBM</a></span></div>
  </div>
</div>

---

## Key Stocks

| Ticker | Company | Role | Confidence |
|--------|---------|------|------------|
| [CRWD](/stocks/CRWD/) | CrowdStrike | Endpoint XDR platform leader | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [PANW](/stocks/PANW/) | Palo Alto Networks | Broadest platform consolidator | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [ZS](/stocks/ZS/) | Zscaler | Cloud-native SASE | <span class="conf-badge conf-confident">Confident</span> |
| [OKTA](/stocks/OKTA/) | Okta | Identity platform | <span class="conf-badge conf-confident">Confident</span> |
| [NET](/stocks/NET/) | Cloudflare | Edge network + Zero Trust mesh | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [CYBR](/stocks/CYBR/) | CyberArk | Privileged access management | <span class="conf-badge conf-confident">Confident</span> |
| [S](/stocks/S/) | SentinelOne | AI-native XDR | <span class="conf-badge conf-confident">Confident</span> |

---

## Causal Signals

- **Major breach events** are catalysts for the entire sector — they elevate security budgets at the C-suite level and drive procurement conversations with every named vendor's sales force. Boards approve cyber spending after breaches; sales cycles shorten.
- **NRR (Net Retention Rate)** is the single most important metric for platform cyber companies. CRWD at 120%+ means existing customers expand their spending by 20% per year. NRR declining toward 110% signals pricing pressure or churn risk.
- **Federal procurement cycles** — the US federal cybersecurity budget (CISA, DoD, NSF) creates procurement floors for platform vendors with FedRAMP authorisation. Watch the annual NDAA for cybersecurity appropriation levels.
- **AI threat escalation** — as AI-generated phishing, deepfake social engineering, and AI-written malware proliferate, security vendors who have AI-powered defence ship quarterly product updates that justify price increases. AI threat volume is a structural tailwind for the sector.

<script>
function toggleAcc(btn) {
  const body = btn.nextElementSibling;
  const isOpen = body.classList.contains('open');
  btn.classList.toggle('open', !isOpen);
  body.classList.toggle('open', !isOpen);
}
</script>
