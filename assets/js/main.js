/* Future Trends — main.js */

document.addEventListener('DOMContentLoaded', () => {
  feather.replace({ 'stroke-width': 2 });
  initSidebar();
  initStocksTable();
  initTopMovers();
});

/* ── Sidebar: hamburger + collapsible nav ── */
function initSidebar() {
  const btn     = document.getElementById('hamburgerBtn');
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('sidebarOverlay');

  if (btn && sidebar && overlay) {
    btn.addEventListener('click', () => {
      const open = sidebar.classList.toggle('open');
      overlay.classList.toggle('open', open);
      btn.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open);
    });
    overlay.addEventListener('click', () => {
      sidebar.classList.remove('open');
      overlay.classList.remove('open');
      btn.classList.remove('open');
    });
  }

  // Collapsible sub-menus
  document.querySelectorAll('.nav-toggle').forEach(toggle => {
    toggle.addEventListener('click', () => {
      const item = toggle.closest('.nav-item');
      const open = item.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
  });

  // Auto-open active parent
  document.querySelectorAll('.nav-sub-link.active').forEach(link => {
    link.closest('.nav-item')?.classList.add('open');
  });
}

/* ── Top Movers widget (homepage) ── */
function initTopMovers() {
  const container = document.getElementById('top-movers-list');
  if (!container) return;

  const base = window.siteBaseUrl || '';
  fetch(base + '/assets/data/stocks.json')
    .then(r => r.json())
    .then(data => {
      const stocks = data.stocks || [];
      const sorted = [...stocks]
        .filter(s => s.change_pct !== null)
        .sort((a, b) => Math.abs(b.change_pct) - Math.abs(a.change_pct))
        .slice(0, 8);

      container.innerHTML = sorted.map(s => {
        const up  = s.change_pct >= 0;
        const pct = (up ? '+' : '') + s.change_pct.toFixed(2) + '%';
        return `
          <div class="mover-row">
            <span class="mover-ticker">${s.ticker}</span>
            <span class="mover-name">${s.name}</span>
            <span class="mover-price">$${s.price.toFixed(2)}</span>
            <span class="mover-change ${up ? 'up' : 'down'}">${pct}</span>
          </div>`;
      }).join('');

      // Stamp last-updated time
      const ts = document.getElementById('movers-updated');
      if (ts && data.updated) {
        const d = new Date(data.updated);
        ts.textContent = 'Updated ' + d.toLocaleDateString('en-SG', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
      }
    })
    .catch(() => {
      container.innerHTML = '<div id="movers-loading">Unable to load stock data.</div>';
    });
}

/* ── Stocks page: full sortable, filterable table ── */
function initStocksTable() {
  const tableBody = document.getElementById('stocks-tbody');
  if (!tableBody) return;

  const base = window.siteBaseUrl || '';
  let allStocks = [];
  let activeFilter = 'All';
  let sortKey = 'market_cap';
  let sortDir = -1; // -1 = desc, 1 = asc

  fetch(base + '/assets/data/stocks.json')
    .then(r => r.json())
    .then(data => {
      allStocks = data.stocks || [];
      renderSectorFilters(allStocks);
      renderTable();

      // Update timestamp
      const ts = document.getElementById('stocks-updated');
      if (ts && data.updated) {
        ts.textContent = 'Data updated: ' + new Date(data.updated).toLocaleString('en-SG');
      }
    })
    .catch(() => {
      tableBody.innerHTML = '<tr><td colspan="7" style="text-align:center;color:var(--text-3);padding:2rem;">Unable to load stock data.</td></tr>';
    });

  // Search
  const searchEl = document.getElementById('stock-search');
  if (searchEl) searchEl.addEventListener('input', renderTable);

  // Sort by button clicks (market cap, alpha, sector)
  document.querySelectorAll('.sort-btn[data-sort]').forEach(btn => {
    btn.addEventListener('click', () => {
      const key = btn.dataset.sort;
      if (sortKey === key) { sortDir *= -1; }
      else { sortKey = key; sortDir = -1; }
      document.querySelectorAll('.sort-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderTable();
    });
  });

  // Column header sort
  document.querySelectorAll('.stocks-table th[data-sort]').forEach(th => {
    th.addEventListener('click', () => {
      const key = th.dataset.sort;
      document.querySelectorAll('.stocks-table th').forEach(h => {
        h.classList.remove('sorted-asc', 'sorted-desc');
      });
      if (sortKey === key) { sortDir *= -1; }
      else { sortKey = key; sortDir = -1; }
      th.classList.add(sortDir === -1 ? 'sorted-desc' : 'sorted-asc');
      sortKey = key;
      renderTable();
    });
  });

  function renderSectorFilters(stocks) {
    const wrap = document.getElementById('sector-filters');
    if (!wrap) return;
    const sectors = ['All', ...new Set(stocks.map(s => s.sector).filter(Boolean).sort())];
    wrap.innerHTML = sectors.map(s =>
      `<button class="filter-btn${s === activeFilter ? ' active' : ''}" data-sector="${s}">${s}</button>`
    ).join('');
    wrap.querySelectorAll('.filter-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        activeFilter = btn.dataset.sector;
        wrap.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        renderTable();
      });
    });
  }

  function renderTable() {
    const query = (document.getElementById('stock-search')?.value || '').toLowerCase();
    let stocks = allStocks.filter(s => {
      const matchSector  = activeFilter === 'All' || s.sector === activeFilter;
      const matchSearch  = !query ||
        s.ticker.toLowerCase().includes(query) ||
        s.name.toLowerCase().includes(query);
      return matchSector && matchSearch;
    });

    stocks = stocks.sort((a, b) => {
      let av = a[sortKey], bv = b[sortKey];
      if (sortKey === 'ticker' || sortKey === 'name' || sortKey === 'sector') {
        av = (av || '').toLowerCase();
        bv = (bv || '').toLowerCase();
        return av < bv ? -sortDir : av > bv ? sortDir : 0;
      }
      return (bv - av) * sortDir * -1;
    });

    tableBody.innerHTML = stocks.map(s => {
      const up  = s.change_pct >= 0;
      const pct = s.change_pct !== null ? (up ? '+' : '') + s.change_pct.toFixed(2) + '%' : '—';
      const chg = s.change !== null ? (up ? '+' : '') + '$' + Math.abs(s.change).toFixed(2) : '—';
      const mkt = s.market_cap ? formatMarketCap(s.market_cap) : '—';
      const url = `${base}/stocks/${s.ticker.toLowerCase()}/`;
      
      return `
        <tr>
          <td class="td-ticker"><a href="${url}" class="ticker-link">${s.ticker}</a></td>
          <td class="td-name">${s.name}</td>
          <td class="td-sector"><span class="tag">${s.sector || '—'}</span></td>
          <td class="td-price">$${s.price ? s.price.toFixed(2) : '—'}</td>
          <td class="td-change ${up ? 'up' : 'down'}">${chg}</td>
          <td class="td-change ${up ? 'up' : 'down'}">${pct}</td>
          <td class="td-mktcap">${mkt}</td>
        </tr>`;
    }).join('');

    const count = document.getElementById('stocks-count');
    if (count) count.textContent = stocks.length + ' stocks';
  }
}

function formatMarketCap(val) {
  if (val >= 1e12) return '$' + (val / 1e12).toFixed(2) + 'T';
  if (val >= 1e9)  return '$' + (val / 1e9).toFixed(1) + 'B';
  if (val >= 1e6)  return '$' + (val / 1e6).toFixed(0) + 'M';
  return '$' + val;
}
