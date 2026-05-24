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

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    AI Cloud TCO &amp; Unit Economics <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>For hyperscalers, the transition from general-purpose compute to AI factories is a CapEx arms race. TCO is the only metric that matters for long-term margin preservation. GPU silicon is ~60% of AI server TCO; power and cooling ~15%; networking (InfiniBand/Ethernet) ~15%; storage and DRAM ~10%.</p>
    <p>As racks move from 15kW to 100kW+ (GB200 NVL72), cooling becomes a specialist industrial moat — Vertiv and Eaton are the key beneficiaries. Utilisation rates are shifting toward "inference-first" architectures to increase monetisation frequency versus long training runs. NVIDIA's GB200 provides a 25x reduction in TCO versus H100 for large-scale LLM inference — this is why Blackwell is in structural deficit despite its price premium.</p>
    <p>CSPs are signalling uncapped AI spending (Meta, Microsoft Q4 2024 earnings calls). Any dip in hyperscaler share prices due to elevated CapEx is a buying opportunity for the hardware layer — the spending is structural, not cyclical.</p>
    <p><strong>Rotation signal:</strong> Monitor the spread between NVIDIA supply and cloud demand. If GPU lead times drop below 12 weeks, rotate from hardware into the software layer deploying those models. <span class="ticker-badge"><a href="/future/stocks/nvda/" style="color:inherit">NVDA</a></span> <span class="ticker-badge"><a href="/future/stocks/msft/" style="color:inherit">MSFT</a></span> <span class="ticker-badge"><a href="/future/stocks/amzn/" style="color:inherit">AMZN</a></span> <span class="ticker-badge"><a href="/future/stocks/googl/" style="color:inherit">GOOGL</a></span></p>
  </div>
</div>

<div class="accordion-item">
  <button class="accordion-toggle" onclick="toggleAcc(this)">
    Software Monetisation Layer <span class="acc-arrow">&#9660;</span>
  </button>
  <div class="accordion-body">
    <p>While hardware and chips get the headlines, long-term AI value will accrue to software companies that embed it into workflows, sell access at scale, and defend moats through data network effects. The core question for every software stock: does AI accelerate your growth, or does it commoditise your product?</p>
    <p><strong>AI-Enhanced SaaS:</strong> ServiceNow, Salesforce, Adobe, Workday embedding AI copilots into workflows — now linked to ROI stories, not just feature releases. These companies have proprietary data and entrenched customer relationships that make AI a multiplier, not a threat.</p>
    <p><strong>Data &amp; Analytics:</strong> Snowflake Cortex, Databricks Unity Catalog, MongoDB Atlas Vector Search, Datadog AI Monitoring. The infrastructure layer for AI-ready data pipelines. Vector databases are becoming a standard component of every AI application stack.</p>
    <p><strong>Developer Tools:</strong> Atlassian, GitLab. GitHub Copilot and AI code generation are simultaneously a threat to incumbent tooling and an opportunity for platforms that can own the full dev lifecycle. AI coding agents (see above) will reshape how software is built — toolchain owners who adapt fastest win.</p>
    <p><strong>Cloud Platforms:</strong> AWS Bedrock, Azure OpenAI Service, GCP Vertex AI capture the vast majority of AI workload spend. The three hyperscalers are simultaneously infrastructure providers and model distributors — a structural advantage that smaller cloud providers cannot replicate. <span class="ticker-badge"><a href="/future/stocks/msft/" style="color:inherit">MSFT</a></span> <span class="ticker-badge"><a href="/future/stocks/googl/" style="color:inherit">GOOGL</a></span> <span class="ticker-badge"><a href="/future/stocks/amzn/" style="color:inherit">AMZN</a></span> <span class="ticker-badge"><a href="/future/stocks/pltr/" style="color:inherit">PLTR</a></span> <span class="ticker-badge"><a href="/future/stocks/net/" style="color:inherit">NET</a></span></p>
  </div>
</div>

---

## Key Stocks

| Ticker | Company | Role | Confidence |
|--------|---------|------|------------|
| [NVDA](/stocks/NVDA/) | NVIDIA | GPU infrastructure | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [MSFT](/stocks/MSFT/) | Microsoft | Azure AI + GitHub Copilot | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [GOOGL](/stocks/GOOGL/) | Alphabet | Gemini + DeepMind + GCP Vertex | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [AMZN](/stocks/AMZN/) | Amazon | AWS Bedrock + Trainium | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [META](/stocks/META/) | Meta | Llama + AI infra | <span class="conf-badge conf-confirmed">Confirmed</span> |
| [PLTR](/stocks/PLTR/) | Palantir | Enterprise AI agents (AIP) | <span class="conf-badge conf-confident">Confident</span> |
| [NOW](/stocks/NOW/) | ServiceNow | AI workflow automation | <span class="conf-badge conf-confident">Confident</span> |
| [NET](/stocks/NET/) | Cloudflare | AI edge inference + security | <span class="conf-badge conf-confident">Confident</span> |
| [IBM](/stocks/IBM/) | IBM | Quantum + enterprise AI | <span class="conf-badge conf-confident">Confident</span> |
| [RXRX](/stocks/RXRX/) | Recursion | AI drug discovery | <span class="conf-badge conf-researching">Researching</span> |

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
