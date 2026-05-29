---
layout: page
title: Blog
subtitle: In-depth analysis, sector deep dives, and research summaries.
permalink: /blog/
---

<div class="placeholder-block">
  <h3>Substack Integration: Coming Soon</h3>
  <p>Recent articles from the Future Trends Substack publication will populate here automatically once the publication is live. Subscribe below to be notified at launch.</p>
</div>

## Recent Articles

<div class="post-list">
  {% for post in site.posts %}
  <a href="{{ post.url | relative_url }}" class="post-list-item" style="text-decoration:none; color:inherit; display:grid;">
    <div>
      <div class="post-list-meta">
        <span class="post-list-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        {% if post.category %}<span class="tag">{{ post.category }}</span>{% endif %}
        {% if post.read_time %}<span style="font-size:0.72rem; color:var(--text-3); font-family:var(--font-mono);">{{ post.read_time }} min read</span>{% endif %}
      </div>
      <div class="post-list-title">{{ post.title }}</div>
      <div class="post-list-excerpt">{{ post.excerpt | strip_html | truncate: 180 }}</div>
    </div>
    {% if post.tickers %}
    <div class="post-list-tickers">
      {% for t in post.tickers %}<span class="ticker-badge">{{ t }}</span>{% endfor %}
    </div>
    {% endif %}
  </a>
  {% endfor %}
</div>
