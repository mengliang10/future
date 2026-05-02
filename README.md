# Future Trends

> The future of technology & AI — today.

Precise, actionable intelligence on semiconductors, AI, quantum computing, and the technologies shaping tomorrow. Linked to stocks, roadmaps, and real money.

---

## Live Site

**https://mengliang10.github.io/future/**

GitHub Pages builds the site automatically every time you push to `main`. Allow 1–2 minutes after a push for changes to appear.

---

## First-Time Setup Checklist

### 1. Enable GitHub Actions write permissions
The daily stock price fetch needs permission to commit back to the repo.

1. Go to **github.com/mengliang10/future**
2. Click **Settings → Actions → General**
3. Scroll to **Workflow permissions**
4. Select **Read and write permissions**
5. Click **Save**

To trigger the first stock fetch manually:
1. Go to **Actions → Fetch Stock Data**
2. Click **Run workflow → Run workflow**

Stock data will then refresh daily at 09:00 Singapore time (01:00 UTC).

---

### 2. Set up the Contact form (Formspree)
The contact form uses [Formspree](https://formspree.io) — free for basic use, no server needed.

1. Sign up at **formspree.io**
2. Create a new form
3. Copy your form endpoint (looks like `https://formspree.io/f/xabcdefg`)
4. Open `contact.md` and replace:
   ```
   https://formspree.io/f/REPLACE_WITH_YOUR_FORM_ID
   ```
   with your actual endpoint
5. Push to `main` — done

---

### 3. Add marketing tags (after finalising design)
All tag snippets are pre-written and waiting in `_includes/marketing-tags.html`.
Uncomment the relevant block and fill in your ID for each:

| Tag | Where to get the ID |
|-----|-------------------|
| Google Tag Manager | tagmanager.google.com |
| Google Analytics 4 | analytics.google.com |
| Meta Pixel | business.facebook.com/events_manager |
| LinkedIn Insight Tag | linkedin.com/campaignmanager |
| Microsoft Clarity | clarity.microsoft.com |
| Google AdSense | adsense.google.com |

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

## Adding a New Blog Post

Create a file in `_posts/` named `YYYY-MM-DD-your-title.md` with this front matter:

```markdown
---
layout: post
title: "Your Article Title"
subtitle: "One line summary"
date: 2026-05-10
category: Semiconductors
read_time: 5
tickers: [NVDA, TSM, ASML]
tags: [nvidia, semiconductors, AI chips]
---

Your article content in Markdown here.
```

Push to `main` and it appears on the site and blog index automatically.

---

## Adding a New Stock

Open `scripts/fetch_stocks.py` and add an entry to the `STOCKS` list:

```python
{"ticker": "TICKER", "name": "Company Name", "sector": "Sector Name"},
```

Also add the same entry to `assets/data/stocks.json` as a placeholder.
The next GitHub Actions run will fetch live data for it.

---

## Local Development (Optional)

To preview the site on your machine before pushing:

```bash
# Install Ruby and Bundler first (ruby-lang.org)
cd future
bundle install
bundle exec jekyll serve
# Open http://localhost:4000/future/
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
