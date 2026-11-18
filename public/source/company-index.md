---
layout: default
title: Company Intelligence Index
permalink: /company-index/
---

<div class="section-heading">
  <h1>Company Intelligence Index</h1>
  <p class="section-sub">A &ndash; Z list of all tracked entities including private and international leaders.</p>
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
  text-decoration: none;
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
