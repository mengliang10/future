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
      <span class="period">This Week</span>
      <span class="tag semi">May 19 &ndash; 23, 2026</span>
    </div>
    <div class="analysis-card-body">
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text"><strong>UK gilts</strong> staged their biggest weekly yield drop since 2023 as fiscal fears eased — causal model: yield spread normalisation precedes growth re-rating 90–270 days out.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text"><strong>Bitcoin (BTC)</strong> holding near $77,000. Quantum-exposure supply narrative gaining traction in on-chain research; implied volatility at 7-month low.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text"><strong>Nuclear stocks (GEV, CEG, NNE)</strong> — EDF joins AI gigafactory alliance; US federal funds awarded for SMR deployment. Research confidence: 0.212, pilot by 2029.</div>
      </div>
    </div>
  </div>

  <div class="analysis-card">
    <div class="analysis-card-header">
      <span class="period">Key Signals</span>
      <span class="tag">Causal Research Pipeline</span>
    </div>
    <div class="analysis-card-body">
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text"><strong>10Y-2Y Spread</strong> → GDP Growth: highest-confidence rule in the DB (conf 1.000, 952 sources, Sharpe 8.56). Spread direction is the single most reliable macro leading indicator.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot down"></div>
        <div class="analysis-item-text"><strong>DXY → Gold:</strong> Dollar strength suppresses gold (conf 0.677, Sharpe 1.99). Real yields (TIPS) are the deeper driver (conf 0.591, 136 sources).</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text"><strong>HY Credit Spread → Value Factor:</strong> conf 0.774, 31 sources, Sharpe 1.97. Spread compression historically amplifies value rotation within 1–3 months.</div>
      </div>
    </div>
  </div>

  <div class="analysis-card">
    <div class="analysis-card-header">
      <span class="period">Next Week</span>
      <span class="tag">May 26 &ndash; 30</span>
    </div>
    <div class="analysis-card-body">
      <div class="analysis-item">
        <div class="analysis-dot"></div>
        <div class="analysis-item-text"><strong>NVIDIA earnings:</strong> CoWoS allocation, GB200 NVL72 rack demand, and Blackwell ramp commentary will set the AI infrastructure narrative for Q3.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot"></div>
        <div class="analysis-item-text"><strong>FERC decision on Crane nuclear restart</strong> expected June/July. Positive ruling is a catalyst for CEG and the broader nuclear PPA trade.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot"></div>
        <div class="analysis-item-text"><strong>Humanoid robot deployments:</strong> Watch for Tesla Optimus factory trial updates. Research pipeline confidence 0.171 from 17 independent sources — pilot stage confirmed.</div>
      </div>
    </div>
  </div>

</div>

<!-- Market Intelligence -->
<div class="section-heading">
  <h2>Market Intelligence</h2>
  <span class="section-sub">High-conviction research across core sectors and deep-dive technical themes.</span>
</div>

<div class="sector-grid">
  <a href="{{ '/sectors/ai/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#129302;</div>
    <div class="sector-card-name">AI & Machine Learning</div>
    <div class="sector-card-desc">LLM unit economics, inference infrastructure, and the competitive landscape of model frameworks.</div>
  </a>
  <a href="{{ '/sectors/semiconductors/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#128421;</div>
    <div class="sector-card-name">Advanced Semiconductors</div>
    <div class="sector-card-desc">Foundry yields, High-NA EUV, Advanced Packaging (CoWoS), and the global WFE supply chain.</div>
  </a>
  <a href="{{ '/sectors/robotics/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#129307;</div>
    <div class="sector-card-name">Robotics & Automation</div>
    <div class="sector-card-desc">Humanoid robots, industrial automation, and the physical AI revolution reshaping manufacturing.</div>
  </a>
  <a href="{{ '/sectors/space/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#128640;</div>
    <div class="sector-card-name">Space Economy</div>
    <div class="sector-card-desc">Launch economics, satellite constellations, lunar commerce, and the $1T space market by 2040.</div>
  </a>
  <a href="{{ '/sectors/biotech/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#129516;</div>
    <div class="sector-card-name">Biotech & Longevity</div>
    <div class="sector-card-desc">CRISPR gene editing, mRNA platforms, AI drug discovery, and the science of extending human lifespan.</div>
  </a>
  <a href="{{ '/sectors/energy/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#9889;</div>
    <div class="sector-card-name">Future Energy & Nuclear</div>
    <div class="sector-card-desc">SMRs, nuclear renaissance, uranium supply, and the power infrastructure the AI era demands.</div>
  </a>
  <a href="{{ '/sectors/blockchain/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#128279;</div>
    <div class="sector-card-name">Blockchain & Digital Assets</div>
    <div class="sector-card-desc">Bitcoin treasury plays, crypto exchanges, mining operators, and the tokenised financial future.</div>
  </a>
  <a href="{{ '/sectors/cyber/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#128274;</div>
    <div class="sector-card-name">Cybersecurity</div>
    <div class="sector-card-desc">The permanent arms race between attackers and defenders — platforms winning at scale.</div>
  </a>
  <a href="{{ '/sectors/autonomous/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#128664;</div>
    <div class="sector-card-name">Autonomous Vehicles</div>
    <div class="sector-card-desc">Self-driving technology, lidar sensors, autonomous trucking, and the end of human-piloted transport.</div>
  </a>
  <a href="{{ '/sectors/xr/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#128257;</div>
    <div class="sector-card-name">XR & Spatial Computing</div>
    <div class="sector-card-desc">VR, AR glasses, the metaverse, and the next generation of human-computer interaction.</div>
  </a>
  <a href="{{ '/sectors/marketing/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#127919;</div>
    <div class="sector-card-name">Marketing Technology</div>
    <div class="sector-card-desc">Programmatic advertising, customer data platforms, and AI-driven growth in a $750B market.</div>
  </a>
  <a href="{{ '/sectors/bci/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#129504;</div>
    <div class="sector-card-name">Brain-Computer Interface</div>
    <div class="sector-card-desc">Neural implants, Neuralink milestones, and the merger of human cognition with machine intelligence.</div>
  </a>
  <a href="{{ '/sectors/quantum/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#9883;</div>
    <div class="sector-card-name">Quantum Computing</div>
    <div class="sector-card-desc">Hardware platforms, error correction milestones, and which stocks are positioned for the quantum era.</div>
  </a>
  <a href="{{ '/scifi/' | relative_url }}" class="sector-card">
    <div class="sector-card-icon">&#127909;</div>
    <div class="sector-card-name">Sci-Fi Cinema & Drama</div>
    <div class="sector-card-desc">From Her to Interstellar — mapping the futures imagined on screen to the technologies being built today.</div>
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
