# Future Trends

> The future of technology & AI: today.

Precise, actionable intelligence on semiconductors, AI, quantum computing, and the technologies shaping tomorrow. Linked to stocks, roadmaps, and real money.

## Live Site

**https://mengliang10.github.io/future/**

GitHub Pages builds the site automatically every time you push to `main`. Allow 1–2 minutes after a push for changes to appear.

---

## Site Structure

```
future/
├── _config.yml              # Site title, URL, baseurl, plugins
├── _layouts/                # Page templates (default, page, post)
├── _includes/               # Reusable components
│   ├── sidebar.html         # Fixed left navigation
│   ├── head.html            # Meta tags, fonts, Open Graph
│   ├── footer.html          # Site footer
│   └── marketing-tags.html  # All ad/analytics tag placeholders
├── assets/
│   ├── css/main.css         # Full dark navy theme
│   ├── js/main.js           # Sidebar toggle, stock table, top movers
│   └── data/stocks.json     # Stock price data (auto-updated daily)
├── scripts/
│   └── fetch_stocks.py      # Python script fetching 100 stocks via yfinance
├── .github/workflows/
│   └── fetch-stocks.yml     # GitHub Actions cron job (daily 01:00 UTC)
├── index.md                 # Homepage
├── about.md                 # About page
├── contact.md               # Contact form
├── stocks/index.md          # Full sortable stock table
├── sectors/                 # AI, Semiconductors, Quantum, Energy, Hardware, Software
├── roadmap/                 # Now-2028, 2028-2030, 2030-2040, 2040-2050, 2050+, Far Future
├── blog/index.md            # Blog index (Substack placeholder)
└── _posts/                  # Articles (YYYY-MM-DD-title.md format)
```

---

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Site generator | Jekyll (GitHub Pages native) |
| Hosting | GitHub Pages (free) |
| Stock data | yfinance via GitHub Actions |
| Contact form | Formspree (free tier) |
| Fonts | Google Fonts (Space Grotesk, Inter, JetBrains Mono) |
| Icons | Feather Icons |
| Analytics | Google Analytics 4 (add your ID) |

---

*Content on this site is for informational purposes only and does not constitute financial advice.*
