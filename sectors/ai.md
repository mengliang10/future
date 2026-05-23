---
layout: page
title: Artificial Intelligence
subtitle: Foundation models, AI chips, inference infrastructure, and the race to AGI.
category: Sector
permalink: /sectors/ai/
---

<div class="callout callout-info">
  <span class="callout-icon">&#129302;</span>
  <span>AI is the largest technology investment cycle in history. This page tracks the stocks, companies, and milestones defining it.</span>
</div>

## Why This Sector Matters

Artificial Intelligence is no longer a research project — it is the primary driver of capital allocation across the entire technology sector. Data centre buildout, chip design, power infrastructure, and software monetisation all trace back to AI demand. The stocks in this sector span the full stack: from the chips that run inference, to the cloud platforms selling access, to the application layer building on top.

---

## Technology Nodes

| Technology | Stage | Year | Confidence |
|---|---|---|---|
| GPU Compute Cluster | Volume production | Ongoing | <span class="conf-badge conf-confirmed">Confirmed</span> |
| Chain-of-Thought Reasoning | Volume production | Ongoing | <span class="conf-badge conf-confirmed">Confirmed</span> |
| LLM GPT-4 Class (~1T params) | Volume production | Ongoing | <span class="conf-badge conf-confirmed">Confirmed</span> |
| AI Hardware ASIC (TPU/NPU) | Volume production | Ongoing | <span class="conf-badge conf-confirmed">Confirmed</span> |
| Cloud Hyperscaler Infrastructure | Volume production | Ongoing | <span class="conf-badge conf-confirmed">Confirmed</span> |
| AI Software Engineering Agent | Early commercial | 2026 | <span class="conf-badge conf-confident">Confident</span> |
| Autonomous AI Agent | Early commercial | 2025 | <span class="conf-badge conf-confident">Confident</span> |
| AI Inference at Edge | Early commercial | 2025 | <span class="conf-badge conf-confident">Confident</span> |
| AI Formal Mathematical Reasoning | Prototype | 2026 | <span class="conf-badge conf-researching">Researching</span> |
| Robotics Foundation Model | Prototype | 2026 | <span class="conf-badge conf-researching">Researching</span> |
| Artificial General Intelligence | Basic research | 2028+ | <span class="conf-badge conf-speculative">Speculative</span> |

---

## Sub-Themes

<div class="accordion-item">
  <button class="accordion-toggle open" onclick="toggleAcc(this)">
    Foundation Models &amp; Inference <span class="acc-arrow" style="transform:rotate(180deg);">&#9660;</span>
  </button>
  <div class="accordion-body open">
    <p>GPT-4 class models are now infrastructure. The competition has shifted from model capability to inference cost — who can serve the same output token at lowest cost. Chain-of-thought reasoning (o-series, Claude extended thinking) is becoming the baseline expectation, increasing compute requirements per useful output by 5-15x.</p>
    <p>The long-term question: does inference commoditise, compressing model provider margins? The evidence so far says no — efficiency gains are absorbed by expanded usage. Every time inference cost drops 10x, usage increases 50x. NVIDIA benefits from both scenarios.</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/nvda/" style="color:inherit">NVDA</a></span> <span class="ticker-badge"><a href="/future/stocks/msft/" style="color:inherit">MSFT</a></span> <span class="ticker-badge"><a href="/future/stocks/googl/" style="color:inherit">GOOGL</a></span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    AI Software Agents <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>AI coding agents move from demo to production in 2026. GitHub Copilot Workspace, Cursor, and enterprise custom agents built on Claude and GPT-4o are live in production. Controlled enterprise studies show 20-40% productivity gains for specific task categories. The bottleneck to full autonomy is formal reasoning — AI that can verify its own work. DeepMind (AlphaProof) is the leading research effort here. When this advances to commercial deployment, it unlocks six downstream technology categories simultaneously.</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/msft/" style="color:inherit">MSFT</a></span> <span class="ticker-badge"><a href="/future/stocks/pltr/" style="color:inherit">PLTR</a></span> <span class="ticker-badge"><a href="/future/stocks/googl/" style="color:inherit">GOOGL</a></span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    AI Chips &amp; Custom Silicon <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>NVIDIA dominates with H100/H200/Blackwell (80%+ AI accelerator share). AMD MI300X is the only credible GPU alternative at scale. Custom silicon from Google (TPU), Amazon (Trainium), and Microsoft (Maia) is eroding NVIDIA's share at the hyperscaler level — but adoption has been slower than bears expected. CUDA ecosystem switching costs are measured in years of developer retraining, not months.</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/nvda/" style="color:inherit">NVDA</a></span> <span class="ticker-badge"><a href="/future/stocks/amd/" style="color:inherit">AMD</a></span> <span class="ticker-badge"><a href="/future/stocks/avgo/" style="color:inherit">AVGO</a></span> <span class="ticker-badge"><a href="/future/stocks/mrvl/" style="color:inherit">MRVL</a></span></div>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    Enterprise AI Applications <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>Enterprise SaaS is embedding AI across workflows (ServiceNow, Salesforce, Adobe). AI-native companies targeting vertical markets (Palantir for government/defence, Recursion for drug discovery). Monetisation models vary: seat pricing (GitHub Copilot), usage pricing (Azure AI), outcome-based (Palantir AIP). The companies with proprietary data and existing customer relationships have the most durable positions.</p>
    <div style="margin-top:0.75rem;"><span class="ticker-badge"><a href="/future/stocks/pltr/" style="color:inherit">PLTR</a></span> <span class="ticker-badge"><a href="/future/stocks/now/" style="color:inherit">NOW</a></span> <span class="ticker-badge"><a href="/future/stocks/msft/" style="color:inherit">MSFT</a></span></div>
  </div>
</div>

---

## Key Stocks

| Ticker | Company | Role | Confidence |
|--------|---------|------|------------|
| [NVDA](/stocks/NVDA/) | NVIDIA | GPU infrastructure | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [MSFT](/stocks/MSFT/) | Microsoft | AI platform + GitHub | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [GOOGL](/stocks/GOOGL/) | Alphabet | Gemini + DeepMind + GCP | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [META](/stocks/META/) | Meta | Llama + AI infra | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [PLTR](/stocks/PLTR/) | Palantir | Enterprise AI agents | <span class="conf-badge conf-confident">Confident</span> |
| [IBM](/stocks/IBM/) | IBM | Quantum + enterprise AI | <span class="conf-badge conf-confident">Confident</span> |

---

## Causal Signals

- **Hyperscaler capex → GPU demand**: Azure, AWS, and GCP revenue growth are the leading indicator for NVIDIA order flows. Monitor quarterly cloud earnings.
- **USD strength (DXY) → US tech earnings**: Dollar strength suppresses reported international revenues for MSFT, GOOGL, NVDA. A weak dollar environment amplifies earnings without operational change.
- **HY credit spreads → value/growth rotation**: Spread compression historically amplifies value factor returns. AI infrastructure stocks (high multiple) are most exposed to any reversal.

<a href="{{ '/roadmap/now-2028/' | relative_url }}" class="btn btn-outline" style="margin-top:1.5rem; display:inline-flex;">View Full Roadmap &rarr;</a>

<script>
function toggleAcc(btn) {
  const body = btn.nextElementSibling;
  const isOpen = body.classList.contains('open');
  btn.classList.toggle('open', !isOpen);
  body.classList.toggle('open', !isOpen);
}
</script>
