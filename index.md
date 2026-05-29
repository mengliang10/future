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

<div class="analysis-grid">

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
          Research confidence reached <strong>{{ node.confidence | times: 100 | round: 0 }}%</strong> as of {{ node.updated_at | date: "%b %d" }}.
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
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {% for bn in site.data.intelligence_meta.bottlenecks limit:4 %}
          <tr>
            <td><strong>{{ bn.node_name }}</strong></td>
            <td><span style="font-size:0.75rem;">Unlocks {{ bn.downstream_node_count }} nodes</span></td>
            <td><span class="signal-dir up">{{ bn.bottleneck_score | round: 2 }}</span></td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

  <!-- Recent Evidence Ingestion -->
  <div class="analysis-card">
    <div class="analysis-card-header">
      <span class="period">Recent Ingestion</span>
      <span class="tag">LATEST EVIDENCE</span>
    </div>
    <div class="analysis-card-body">
      {% for item in site.data.intelligence_meta.recent_ingestion limit:3 %}
      <div class="analysis-item">
        <div class="analysis-dot"></div>
        <div class="analysis-item-text" style="font-size:0.85rem;">
          <strong>{{ item.technology_name | capitalize }}</strong><br>
          {{ item.source_title | truncate: 80 }}<br>
          <span style="font-size:0.75rem; color:var(--text-3);">Ingested: {{ item.ingested_at | date: "%b %d, %Y" }}</span>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>

</div>

<!-- Alphabetical Company Index -->
<div class="section-heading" style="margin-top: 4rem;">
  <h2>Company Intelligence Index</h2>
  <span class="section-sub">A &ndash; Z list of all tracked entities including private and international leaders.</span>
</div>

<div class="company-index-grid">
  {% for company in site.data.intelligence_meta.company_index %}
  <a href="{{ '/stocks/' | append: company.ticker | downcase | relative_url }}" class="index-item">
    <span class="index-ticker">{{ company.ticker }}</span>
    <span class="index-name">{{ company.name }}</span>
  </a>
  {% endfor %}
</div>

<style>
.company-index-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 2rem;
}

.index-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  transition: all var(--transition);
}

.index-item:hover {
  background: var(--bg-3);
  border-color: var(--accent);
  transform: translateY(-2px);
  box-shadow: var(--accent-glow);
}

.index-ticker {
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--accent);
  font-size: 0.8rem;
  min-width: 70px;
}

.index-name {
  font-size: 0.9rem;
  color: var(--text-2);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

@media (max-width: 1024px) {
  .company-index-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 640px) {
  .company-index-grid { grid-template-columns: 1fr; }
}
</style>

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
