---
layout: page
title: Stocks
subtitle: 100 tracked tech and future-tech stocks — sortable, filterable, live-updated daily.
permalink: /stocks/
---

<div class="section-heading">
  <h2>All Tracked Symbols</h2>
  <span class="section-sub">100 tracked tech and future-tech stocks — sortable and filterable.</span>
</div>

<div class="stocks-controls">
  <input type="text" id="stock-search" class="search-input" placeholder="Search ticker or company name...">
  <button class="sort-btn active" data-sort="market_cap">By Market Cap</button>
  <button class="sort-btn" data-sort="ticker">A &ndash; Z</button>
  <button class="sort-btn" data-sort="change_pct">By % Change</button>
</div>

<div id="sector-filters" class="sector-filter"></div>

<div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.75rem;">
  <span id="stocks-count" style="font-size:0.78rem; color:var(--text-3);"></span>
  <span id="stocks-updated" style="font-size:0.72rem; color:var(--text-3); font-family:var(--font-mono);"></span>
</div>

<div class="stocks-table-wrap">
  <table class="stocks-table">
    <thead>
      <tr>
        <th data-sort="ticker">Ticker</th>
        <th data-sort="name">Company</th>
        <th data-sort="sector">Sector</th>
        <th data-sort="price" style="text-align:right;">Price</th>
        <th data-sort="change" style="text-align:right;">Chg</th>
        <th data-sort="change_pct" style="text-align:right;">%</th>
        <th data-sort="rsi" style="text-align:right;">RSI</th>
        <th data-sort="market_cap" style="text-align:right;">Mkt Cap</th>
      </tr>
    </thead>
    <tbody id="stocks-tbody">
      <tr><td colspan="8" style="text-align:center; color:var(--text-3); padding:2rem;">Loading stock data&hellip;</td></tr>
    </tbody>
  </table>
</div>

<div class="callout callout-info" style="margin-top:1.5rem;">
  <span class="callout-icon">&#9432;</span>
  <span>Prices updated daily via <strong>yfinance</strong> by automated GitHub Actions. Data reflects prior trading day close. Not real-time.</span>
</div>
