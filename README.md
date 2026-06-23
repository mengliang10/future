# Future Trends

> The future of technology & AI: today.

Precise, actionable intelligence on semiconductors, AI, quantum computing, and the technologies shaping tomorrow. Linked to stocks, roadmaps, and real money.

## Live Site

**https://mengliang10.github.io/future/**

GitHub Pages builds the site automatically every time you push to `main`. Allow 1–2 minutes after a push for changes to appear.

---

## Generative Engine Optimization (GEO)

This site is structured specifically to optimize visibility and citation within AI-driven search and synthesis engines (such as Perplexity, ChatGPT Search, Gemini AI Overviews, and Claude):
1. **Crawl Guidance (`llms.txt`)**: A structured file is hosted at the root (`/llms.txt`) based on the emerging standard to guide LLM crawlers directly to critical technology indices, sector briefs, and methodology resources.
2. **Factual Claim Structuring**: Core technology profiles are compiled into self-contained, dated assertion blocks (e.g., *"[Technology] is in [production_stage] as of [year] with [evidence_count] sources confirming..."*). This self-contained structure removes pronoun/context ambiguity, making it highly extractable for RAG systems.
3. **Rich Schema.org Metadata**: Pages embed rich JSON-LD markup containing Schema.org `TechArticle`, `Claim`, and `Dataset` schemas to explicitly signal machine-readable technology properties, temporal coverage, and confidence levels.

---

## Local Vector Database & Embeddings

The local research and trading backend leverages a private vector search architecture to compute semantic correlation and deduplicate inputs:
1. **`sqlite-vec` Database Integration**: The local relational data stores utilize the SQLite extension `sqlite-vec` (version `0.1.9+`) to initialize `vec0` virtual tables. This enables efficient, low-memory Approximate Nearest Neighbor (ANN) searches directly inside database queries.
2. **Cosine-Similarity & Deduplication**: Textual claims, news feeds, and trading rules are embedded into `float32` vectors. The local pipeline calculates cosine-similarity scores to automatically identify, reconcile, and merge duplicate or highly similar rules.
3. **Offline Vector Consensus**: Private vectors are stored and queried entirely locally in the offline database system, protecting proprietary strategy intelligence while maintaining high performance for semantic matching.

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
