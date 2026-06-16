---
layout: default
title: Home
---

<section class="hero">
  <div class="hero-left">
    <p class="hero-eyebrow">Future Trends: Powered by Data &middot; Updated {{ 'now' | date: "%b %d, %Y" }}</p>
    <h1 class="hero-title">The future of technology &amp; AI today.</h1>
    <p class="hero-sub">Precise, actionable intelligence on semiconductors, AI, quantum computing, space economy, and the technologies shaping tomorrow. 212+ technology nodes tracked across 14 sectors. Linked to stocks, roadmaps, and real money.</p>
    <div class="hero-actions">
      <a href="{{ '/stocks/' | relative_url }}" class="btn btn-primary">View All Stocks</a>
      <a href="{{ '/tech/' | relative_url }}" class="btn btn-outline">Explore 212+ Technologies</a>
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

<!-- Market Pulse -->
<div class="section-heading">
  <h2>Market Pulse</h2>
  <span class="section-sub">Key themes shaping frontier technology markets right now.</span>
</div>

<div class="pulse-grid">
  <div class="pulse-card">
    <div class="pulse-card-icon">🚀</div>
    <div class="pulse-card-content">
      <div class="pulse-card-title">SpaceX Goes Public</div>
      <div class="pulse-card-desc">SPCX IPO marks the largest tech listing in history. Zephirin Group initiates Buy at $310. Index inclusion forcing institutional accumulation.</div>
    </div>
  </div>
  <div class="pulse-card">
    <div class="pulse-card-icon">🏦</div>
    <div class="pulse-card-content">
      <div class="pulse-card-title">FOMC Hawkish Pivot</div>
      <div class="pulse-card-desc">40% of fund managers now expect a rate hike within 12 months. Warsh chairs first Fed meeting. Dot plot is the binary event.</div>
    </div>
  </div>
  <div class="pulse-card">
    <div class="pulse-card-icon">🧠</div>
    <div class="pulse-card-content">
      <div class="pulse-card-title">AI Capex Supercycle</div>
      <div class="pulse-card-desc">NVDA issues first $25B bond. MU +10% on memory surge. ORCL commits 103% capex/revenue. GS says TSM undervalued on AI demand.</div>
    </div>
  </div>
  <div class="pulse-card">
    <div class="pulse-card-icon">🛢️</div>
    <div class="pulse-card-content">
      <div class="pulse-card-title">Hormuz Deal &amp; Oil Below $80</div>
      <div class="pulse-card-desc">US-Iran interim deal reopens Strait of Hormuz. Brent drops below $80 for first time since March. Tanker CEOs say normalization is weeks away.</div>
    </div>
  </div>
</div>

<!-- Sector Explorer -->
<div class="section-heading">
  <h2>Explore by Sector</h2>
  <a href="{{ '/sectors/' | relative_url }}" class="view-all">All sectors &rarr;</a>
</div>

<div class="sector-grid">
  <a href="{{ '/sectors/ai/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">🤖</div>
    <div class="sector-card-name">Artificial Intelligence</div>
    <div class="sector-card-desc">Foundation models, agents, inference infrastructure</div>
  </a>
  <a href="{{ '/sectors/semiconductors/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">🔬</div>
    <div class="sector-card-name">Semiconductors</div>
    <div class="sector-card-desc">GPUs, ASICs, HBM memory, foundry supply chain</div>
  </a>
  <a href="{{ '/sectors/quantum/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">⚛️</div>
    <div class="sector-card-name">Quantum Computing</div>
    <div class="sector-card-desc">Qubit platforms, error correction, listed stocks</div>
  </a>
  <a href="{{ '/sectors/robotics/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">🦾</div>
    <div class="sector-card-name">Robotics &amp; Automation</div>
    <div class="sector-card-desc">Humanoid robots, factory automation, embodied AI</div>
  </a>
  <a href="{{ '/sectors/space/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">🚀</div>
    <div class="sector-card-name">Space Economy</div>
    <div class="sector-card-desc">Launch, satellite networks, in-orbit manufacturing</div>
  </a>
  <a href="{{ '/sectors/biotech/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">🧬</div>
    <div class="sector-card-name">Biotech &amp; Longevity</div>
    <div class="sector-card-desc">AI drug discovery, gene editing, longevity therapeutics</div>
  </a>
  <a href="{{ '/sectors/energy/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">⚡</div>
    <div class="sector-card-name">Future Energy</div>
    <div class="sector-card-desc">SMRs, fusion, grid storage, data centre power</div>
  </a>
  <a href="{{ '/sectors/cyber/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">🛡️</div>
    <div class="sector-card-name">Cybersecurity</div>
    <div class="sector-card-desc">Zero trust, AI threat detection, post-quantum crypto</div>
  </a>
  <a href="{{ '/sectors/autonomous/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">🚗</div>
    <div class="sector-card-name">Autonomous Vehicles</div>
    <div class="sector-card-desc">Full self-driving, lidar, robo-taxi networks</div>
  </a>
  <a href="{{ '/sectors/blockchain/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">🔗</div>
    <div class="sector-card-name">Blockchain</div>
    <div class="sector-card-desc">Layer 2, DeFi, tokenisation, regulatory landscape</div>
  </a>
  <a href="{{ '/sectors/xr/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">🥽</div>
    <div class="sector-card-name">XR &amp; Spatial Computing</div>
    <div class="sector-card-desc">Mixed reality, spatial OS, AR glasses, Apple Vision</div>
  </a>
  <a href="{{ '/sectors/bci/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">🧠</div>
    <div class="sector-card-name">Brain-Computer Interface</div>
    <div class="sector-card-desc">Neural implants, non-invasive BCI, Neuralink</div>
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
        {% if post.category %}
        {% assign sector_slug = post.category | downcase | replace: ' ', '-' %}
        <a href="{{ '/sectors/' | append: sector_slug | append: '/' | relative_url }}" class="tag" style="text-decoration:none;">{{ post.category }}</a>
        {% endif %}
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
