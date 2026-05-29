# Enhancement 02: SEO Stack (Without SemRush)

## Problem

SemRush costs $140–$450/month per user and is designed for single-site, human-operated workflows. At Martech platform scale: multiple sites, programmatic content, automated publishing: a per-seat SaaS tool is the wrong model. The goal is an owned, automated SEO stack that costs near-zero in licensing, integrates with the research pipeline, and generates actionable signals without manual intervention.

---

## Full-Scale Vision

A self-hosted SEO intelligence layer that monitors keyword rankings, crawl health, backlink growth, and Core Web Vitals across every property on the platform. It runs on a cron schedule, writes results to a central SQLite/Postgres DB, and surfaces alerts and dashboards without any proprietary SaaS dependency.

```mermaid
graph TD
    subgraph DataSources["Data Sources (Free/API)"]
        GSC[Google Search Console API]
        GA4[Google Analytics 4 API]
        PAGESPEED[PageSpeed Insights API]
        SERPAPI[SerpAPI / ValueSERP]
        COMMONC[CommonCrawl Backlinks]
        SITEMAP[Sitemap.xml self-parsed]
    end

    subgraph Pipeline["SEO Pipeline (Python, cron)"]
        CRAWL[Crawler: scrapy / httpx]
        KWTRACK[Keyword Rank Tracker]
        TECHAUDIT[Technical Audit Engine]
        BACKLINK[Backlink Aggregator]
        SCORE[SEO Score Engine]
    end

    subgraph Storage["Storage"]
        DB[(seo_intelligence.db)]
    end

    subgraph Output["Output"]
        DASH[Grafana / Metabase Dashboard]
        ALERT[Slack / Email Alerts]
        REPORT[Weekly MD Report → CMS]
        RECS[Auto-recommendations → Backlog]
    end

    GSC --> KWTRACK
    GA4 --> SCORE
    PAGESPEED --> TECHAUDIT
    SERPAPI --> KWTRACK
    COMMONC --> BACKLINK
    SITEMAP --> CRAWL
    CRAWL --> TECHAUDIT
    KWTRACK --> DB
    TECHAUDIT --> DB
    BACKLINK --> DB
    SCORE --> DB
    DB --> DASH
    DB --> ALERT
    DB --> REPORT
    DB --> RECS
```

---

## Tool Stack (Zero-License)

| Function | SemRush Equivalent | OSS / Free Alternative | Cost |
|----------|--------------------|------------------------|------|
| Keyword rankings | Position Tracking | Google Search Console API + SerpAPI | Free / $50/mo |
| Site crawl | Site Audit | Scrapy + custom audit script | Free |
| Backlinks | Backlink Analytics | Ahrefs Webmaster Tools (free tier) + OpenLinkProfiler | Free |
| Core Web Vitals | Site Audit | PageSpeed Insights API (Google) | Free |
| Keyword research | Keyword Magic Tool | Google Keyword Planner API + DataForSEO | Free / ~$10/mo |
| Competitor analysis | Traffic Analytics | SimilarWeb free + manual GSC comparison | Free |
| Rank tracking | Position Tracking | SerpAPI (100 free/day) or custom SERP scraper | Free–$50/mo |

**Total estimated cost: $0–$60/month vs $140–$450/month for SemRush.**

---

## SEO Architecture for Programmatic Content

The Future Trends site generates content programmatically from a DB. This requires a different SEO model than hand-written content: optimisation must be baked into the generation templates, not applied manually post-publish.

```mermaid
flowchart LR
    subgraph DB["tech_graph.db"]
        NODE[tg_nodes\nname, category, description]
        CONF[tg_node_confidence_log\nsources, evidence]
        EDGE[tg_edges\nrelationships]
    end

    subgraph Template["Page Template (Jekyll)"]
        TITLE[<title> = node.name + category + year]
        META[meta description = first 160 chars of description]
        H1[H1 = node.name]
        SCHEMA[JSON-LD TechArticle schema]
        INTERNAL[Internal links from edges]
        BREADCRUMB[Breadcrumb schema]
    end

    subgraph OnPage["On-Page SEO Signals"]
        KW[Target keyword in: title, H1, URL, first 100 words]
        FRESH[Last-updated date = source_date]
        DEPTH[Word count >= 400 per page]
        LINK[3+ internal links per page]
    end

    NODE --> TITLE
    NODE --> H1
    NODE --> META
    CONF --> FRESH
    EDGE --> INTERNAL
    CONF --> DEPTH
    Template --> OnPage
```

### JSON-LD Schema for Tech Node Pages

Each `_tech/*.md` page should emit structured data to help both Google and AI search engines understand the content type:

```json
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "{{ page.title }}",
  "description": "{{ page.subtitle }}",
  "dateModified": "{{ page.date }}",
  "author": { "@type": "Organization", "name": "Future Trends" },
  "about": {
    "@type": "Thing",
    "name": "{{ page.title }}",
    "description": "{{ page.subtitle }}"
  },
  "keywords": "{{ page.category }}, {{ page.stage }}, {{ page.horizon }}"
}
```

---

## Keyword Strategy for Programmatic Pages

```mermaid
mindmap
  root((Keyword Clusters))
    Technology Name
      exact match slug
      technology + year
      technology + stock ticker
    Category
      AI + semiconductors
      future energy 2030
    Intent
      invest in X
      X commercial deployment
      X timeline prediction
    Longtail
      when will X be deployed
      X vs Y comparison
      X stock exposure
```

**Targeting principle:** Each page targets one primary keyword (the technology name) plus 3–5 longtail variants derived from `est_year_mode`, `category`, and linked tickers. These are injected automatically by the template: no manual keyword assignment needed.

---

## Technical SEO Checklist (Automated)

```mermaid
flowchart TD
    CRAWL[Weekly crawl via Scrapy] --> CHECKS
    CHECKS --> C1{All pages return 200?}
    CHECKS --> C2{Canonical tags correct?}
    CHECKS --> C3{No duplicate H1s?}
    CHECKS --> C4{Sitemap includes all pages?}
    CHECKS --> C5{Core Web Vitals: LCP < 2.5s?}
    CHECKS --> C6{Internal link depth <= 3 clicks?}
    CHECKS --> C7{Meta descriptions 120-160 chars?}
    C1 -- Fail --> A1[Alert: broken pages list]
    C2 -- Fail --> A2[Alert: canonical mismatch]
    C3 -- Fail --> A3[Alert: duplicate H1 report]
    C4 -- Fail --> A4[Regenerate sitemap.xml]
    C5 -- Fail --> A5[Alert: CWV degradation]
    C6 -- Fail --> A6[Suggest internal link additions]
    C7 -- Fail --> A7[Flag pages needing meta update]
```

---

## Phased Implementation

| Phase | Deliverable | Effort |
|-------|-------------|--------|
| 1 | GSC API integration → weekly rank pull to DB | 1 week |
| 2 | JSON-LD schema injection into Jekyll templates | 2 days |
| 3 | Automated sitemap.xml + robots.txt generator | 2 days |
| 4 | PageSpeed Insights weekly crawl → DB | 1 week |
| 5 | Keyword clustering script from GSC query data | 2 weeks |
| 6 | Grafana SEO dashboard | 1 week |
| 7 | SerpAPI rank tracker for top 50 target keywords | 1 week |

---

## Success Metrics

| Metric | Baseline | 6-Month Target |
|--------|----------|----------------|
| GSC impressions / month | Unknown | +200% |
| Pages indexed | Unknown | >95% of tech pages |
| Average position for technology keywords | Unknown | Top 20 |
| Core Web Vitals: LCP | Unknown | <2.5s |
| SEO tooling cost/month | $0 (no tooling) | <$60 |
| Time to detect SEO regression | Never | <24 hours |

---

## Open Questions

- SerpAPI free tier is 100 searches/day: sufficient for monitoring 50 keywords; need upgrade at scale.
- Should keyword research use Google Ads API (requires active ad account) or DataForSEO as fallback?
- At platform scale (10+ sites), does it make sense to self-host an open-source rank tracker like NightWatch alternative or SerpYacht?
