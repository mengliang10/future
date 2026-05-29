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

<!-- Automated Intelligence: Research Frontier & Chokepoints -->
<div class="section-heading">
  <h2>Intelligence Frontier</h2>
  <span class="section-sub">Automated research feed — latest technology nodes and strategic chokepoints.</span>
  <a href="{{ '/tech/' | relative_url }}" class="view-all">Technology Intelligence (220 nodes) &rarr;</a>
</div>

<div class="analysis-grid" style="grid-template-columns: repeat(2, 1fr);">

  <!-- Research Frontier (Possibility A) -->
  <div class="analysis-card">
    <div class="analysis-card-header">
      <span class="period">Research Frontier</span>
      <span class="tag semi">LATEST UPDATES</span>
    </div>
    <div class="analysis-card-body">
      {% for node in site.data.intelligence_meta.frontier limit:3 %}
      <div class="analysis-item">
        <div class="analysis-dot up"></div>
        <div class="analysis-item-text">
          <a href="{{ '/tech/' | append: node.id | append: '/' | relative_url }}" style="font-weight:700; color:var(--accent);">{{ node.name }}</a><br>
          <span style="font-size:0.8rem; color:var(--text-3);">{{ node.category }} &middot; Stage: {{ node.status | replace: '_', ' ' | capitalize }}</span><br>
          Research Maturity: <strong>{{ node.confidence | times: 100 | round: 0 }}%</strong> (Discovery phase: gathering evidence and validating technical claims) as of {{ node.updated_at | date: "%b %d" }}.
        </div>
      </div>
      {% endfor %}
    </div>
  </div>

  <!-- Strategic Chokepoints -->
  <div class="analysis-card">
    <div class="analysis-card-header">
      <span class="period">Strategic Chokepoints</span>
      <span class="tag">BOTTLENECK MATRIX</span>
    </div>
    <div class="analysis-card-body">
      <table class="signal-table">
        <thead>
          <tr>
            <th>Chokepoint</th>
            <th>Impact</th>
            <th>Strategic Score</th>
          </tr>
        </thead>
        <tbody>
          {% for bn in site.data.intelligence_meta.bottlenecks limit:4 %}
          <tr>
            <td><strong>{{ bn.node_name }}</strong></td>
            <td><span style="font-size:0.75rem;">Foundation for {{ bn.downstream_node_count }} tech pathways</span></td>
            <td>
              <span class="signal-dir up">{{ bn.bottleneck_score | round: 2 }}</span><br>
              <span style="font-size:0.65rem; color:var(--text-3); font-weight:normal;">Critical Priority</span>
            </td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

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
