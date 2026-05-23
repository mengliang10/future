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
  <h2>Market Intelligence</h2>
  <span class="section-sub">Macro signals, catalysts, and causal research — week of May 19–23, 2026</span>
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
        <div class="analysis-item-text"><strong>UK gilts</strong> staged their biggest weekly yield drop since 2023 as fiscal fears eased. Yield spread normalisation historically precedes GDP re-rating by 90–270 days — a green light for risk-on positioning in the UK and European tech names.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text"><strong>Bitcoin (BTC)</strong> holding near $77,000 with implied volatility at a 7-month low. On-chain researchers are attaching a quantum-exposure supply narrative — early days, but the conversation is moving from fringe to institutional desks.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text"><strong>Nuclear power (GEV, CEG, NNE)</strong> — EDF has joined the AI gigafactory alliance and US federal funds were awarded for SMR site development. Small modular reactors remain in the pilot phase with first commercial operations expected 2029. The trade is structural, not near-term earnings.</div>
      </div>
    </div>
  </div>

  <div class="analysis-card">
    <div class="analysis-card-header">
      <span class="period">Key Macro Signals</span>
      <span class="tag">Causal Research</span>
    </div>
    <div class="analysis-card-body">
      <table class="signal-table">
        <thead>
          <tr>
            <th>Signal</th>
            <th>Direction</th>
            <th>Implication</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>10Y–2Y Yield Spread</strong></td>
            <td><span class="signal-dir up">Steepening</span></td>
            <td>GDP acceleration in 3–9 months. Strongest macro leading indicator. Drives industrial capex, energy infra, and AI hardware cycles.</td>
          </tr>
          <tr>
            <td><strong>DXY (Dollar Index)</strong></td>
            <td><span class="signal-dir neutral">Softening</span></td>
            <td>Dollar weakness is a tailwind for gold, commodities, and EM tech. Real yields (TIPS) are the deeper driver — watch the 10Y real yield for the true signal.</td>
          </tr>
          <tr>
            <td><strong>HY Credit Spreads</strong></td>
            <td><span class="signal-dir up">Compressing</span></td>
            <td>Spread compression within 1–3 months historically amplifies value factor rotation. Risk appetite is opening — small/mid-cap tech names benefit first.</td>
          </tr>
          <tr>
            <td><strong>Uranium Spot Price</strong></td>
            <td><span class="signal-dir up">Elevated</span></td>
            <td>Above $90/lb incentivises mine restarts. Supply response takes 5–7 years — structural tailwind for CCJ and uranium royalty names.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="analysis-card">
    <div class="analysis-card-header">
      <span class="period">Watch Next Week</span>
      <span class="tag">May 26 &ndash; 30</span>
    </div>
    <div class="analysis-card-body">
      <div class="analysis-item">
        <div class="analysis-dot"></div>
        <div class="analysis-item-text"><strong>NVIDIA earnings (May 28):</strong> The key variables are CoWoS packaging allocation, GB200 NVL72 rack demand commentary, and Blackwell yield ramp. Whatever NVDA says about data centre capex commitment sets the AI infrastructure narrative for the rest of 2026.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot"></div>
        <div class="analysis-item-text"><strong>Crane Clean Energy Center (FERC):</strong> Federal ruling on the Three Mile Island Unit 1 restart is expected June–July. A positive decision is a direct catalyst for <a href="{{ '/stocks/ceg/' | relative_url }}" style="color:var(--accent);">CEG</a> and validates the entire nuclear PPA trade with hyperscalers.</div>
      </div>
      <div class="analysis-item">
        <div class="analysis-dot"></div>
        <div class="analysis-item-text"><strong>Tesla Optimus factory trial data:</strong> First-generation humanoid robots are in live pilot at Tesla's Giga facilities. Any operational update — task success rate, cycle time, unit economics — moves the humanoid thesis from pilot-stage confidence to early-commercial. Watch <a href="{{ '/stocks/tsla/' | relative_url }}" style="color:var(--accent);">TSLA</a> and <a href="{{ '/stocks/nvda/' | relative_url }}" style="color:var(--accent);">NVDA</a>.</div>
      </div>
    </div>
  </div>

</div>

<!-- Market Intelligence -->
<div class="section-heading">
  <h2>Sectors &amp; Research</h2>
  <span class="section-sub">High-conviction research across 13 sectors — with technology nodes, causal signals, and investable stocks.</span>
  <a href="{{ '/tech/' | relative_url }}" class="view-all">Technology Intelligence (212 nodes) &rarr;</a>
</div>

<div class="sector-grid">
  <a href="{{ '/tech/' | relative_url }}" class="sector-card" style="border-color:var(--accent-2); background:linear-gradient(135deg,var(--bg-3),var(--bg-2));">
    <div class="sector-card-icon">&#127775;</div>
    <div class="sector-card-name" style="color:var(--accent);">Technology Intelligence</div>
    <div class="sector-card-desc">212 tracked future technologies — vetted, confidence-rated, linked to stocks. Confirmed → Confident → Researching → Speculative.</div>
  </a>
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
