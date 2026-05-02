---
layout: default
title: Home
---

<section class="hero">
  <div class="hero-left">
    <p class="hero-eyebrow">Future Trends &mdash; Powered by Data</p>
    <h1 class="hero-title">The future of technology &amp; AI &mdash; today.</h1>
    <p class="hero-sub">Precise, actionable intelligence on semiconductors, AI, quantum computing, and the technologies shaping tomorrow. Linked to stocks, roadmaps, and real money.</p>
    <div class="hero-actions">
      <a href="{{ '/stocks/' | relative_url }}" class="btn btn-primary">View All Stocks</a>
      <a href="{{ '/sectors/ai/' | relative_url }}" class="btn btn-outline">Explore AI Sector</a>
    </div>
  </div>
  <div class="hero-right">
    <div class="top-movers">
      <div class="top-movers-header">
        <h3>Top Movers</h3>
        <span class="live-badge">LIVE</span>
      </div>
      <div id="top-movers-list">
        <div id="movers-loading">Loading stock data&hellip;</div>
      </div>
      <div class="mover-row" style="padding:0.5rem 1.1rem; border-top:1px solid var(--border);">
        <span style="font-size:0.7rem; color:var(--text-3); grid-column:1/-1;" id="movers-updated"></span>
      </div>
    </div>
  </div>
</section>

<!-- Market Analysis: Today / This Week / Next Week -->
<div class="section-heading">
  <h2>Market Analysis</h2>
  <span class="section-sub">Sector &amp; stock intelligence at a glance</span>
  <a href="{{ '/stocks/' | relative_url }}" class="view-all">Full stock table &rarr;</a>
</div>

<div class="analysis-grid">

  <div class="analysis-card">
    <div class="analysis-card-header">
      <span class="period">Today</span>
      <span class="tag semi">May 3, 2026</span>
    </div>
    <div class="analysis-card-body">
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text"><strong>NVIDIA (NVDA)</strong> up 1.4% on continued data centre demand signals ahead of next earnings.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot down"></div>
        <div class="analysis-item-text"><strong>ON Semiconductor (ON)</strong> down 2.8% after EV demand softness commentary from a major OEM.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text"><strong>IonQ (IONQ)</strong> up 6.9% following a new government contract announcement.</div>
      </div>
    </div>
  </div>

  <div class="analysis-card">
    <div class="analysis-card-header">
      <span class="period">This Week</span>
      <span class="tag">Apr 28 &ndash; May 3</span>
    </div>
    <div class="analysis-card-body">
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text"><strong>Semiconductors</strong> outperformed the broader market +2.1% driven by CoWoS capacity upgrades at TSMC.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot down"></div>
        <div class="analysis-item-text"><strong>Solar/Energy</strong> sector underperformed &minus;3.5% on rising interest rate expectations reducing project economics.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text"><strong>AI Cloud (MSFT, GOOGL)</strong> both reported strong Azure/GCP AI revenue growth beats.</div>
      </div>
    </div>
  </div>

  <div class="analysis-card">
    <div class="analysis-card-header">
      <span class="period">Next Week</span>
      <span class="tag">May 4 &ndash; 10</span>
    </div>
    <div class="analysis-card-body">
      <div class="analysis-item">
        <div class="analysis-dot"></div>
        <div class="analysis-item-text"><strong>Earnings watch:</strong> AMD, ARM, and SMCI report. AMD guidance on MI300X demand will set the AI chip narrative.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot"></div>
        <div class="analysis-item-text"><strong>TSMC April sales data</strong> due May 8. Expect strong YoY growth confirming AI server demand.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot"></div>
        <div class="analysis-item-text"><strong>Federal Reserve speaker</strong> scheduled Tuesday. Watch for signals on rate path impacting growth tech valuations.</div>
      </div>
    </div>
  </div>

</div>

<!-- Sector Themes -->
<div class="section-heading">
  <h2>Sector Themes</h2>
  <span class="section-sub">Pick a sector to explore stocks, analysis, and roadmaps</span>
</div>

<div class="sector-grid">
  <a href="{{ '/sectors/ai/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#129302;</div>
    <div class="sector-card-name">Artificial Intelligence</div>
    <div class="sector-card-desc">LLMs, AI chips, inference infrastructure, enterprise AI deployment and the race to AGI.</div>
  </a>
  <a href="{{ '/sectors/semiconductors/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#128421;</div>
    <div class="sector-card-name">Semiconductors</div>
    <div class="sector-card-desc">Foundries, fabless design, EUV lithography, packaging, and the global chip supply chain.</div>
  </a>
  <a href="{{ '/sectors/quantum/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#128307;</div>
    <div class="sector-card-name">Quantum Computing</div>
    <div class="sector-card-desc">Hardware platforms, error correction progress, and which stocks are positioned for the quantum era.</div>
  </a>
  <a href="{{ '/sectors/energy/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#9889;</div>
    <div class="sector-card-name">Energy Tech</div>
    <div class="sector-card-desc">Clean energy, grid infrastructure, nuclear fusion timelines, and power demand from AI data centres.</div>
  </a>
  <a href="{{ '/sectors/hardware/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#128421;</div>
    <div class="sector-card-name">Hardware</div>
    <div class="sector-card-desc">Servers, networking, storage, and the physical infrastructure powering the AI supercycle.</div>
  </a>
  <a href="{{ '/sectors/software/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#128187;</div>
    <div class="sector-card-name">Software</div>
    <div class="sector-card-desc">Cloud platforms, cybersecurity, AI-native SaaS, and the software layer monetising the AI build-out.</div>
  </a>
</div>

<!-- Latest Articles -->
<div class="section-heading">
  <h2>Latest Analysis</h2>
  <a href="{{ '/blog/' | relative_url }}" class="view-all">All articles &rarr;</a>
</div>

<div class="post-list">
  {% for post in site.posts limit:4 %}
  <a href="{{ post.url | relative_url }}" class="post-list-item" style="text-decoration:none; color:inherit; display:grid;">
    <div>
      <div class="post-list-meta">
        <span class="post-list-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        {% if post.category %}<span class="tag">{{ post.category }}</span>{% endif %}
      </div>
      <div class="post-list-title">{{ post.title }}</div>
      <div class="post-list-excerpt">{{ post.excerpt | strip_html | truncate: 140 }}</div>
    </div>
    {% if post.tickers %}
    <div class="post-list-tickers">
      {% for t in post.tickers %}<span class="ticker-badge">{{ t }}</span>{% endfor %}
    </div>
    {% endif %}
  </a>
  {% endfor %}
</div>
