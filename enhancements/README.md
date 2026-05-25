# Enhancements — Martech Platform Roadmap

> **Scope: Full platform, not just this site.**
> The Future Trends site (`mengliang10.github.io/future`) is the hook — a live proof of concept demonstrating programmatic content at scale. Every enhancement here must be architected for a multi-property, multi-tenant Martech platform that will eventually serve many sites, clients, and verticals.

---

## Why This Matters

The content we publish is the bait. The platform we build is the product.

The Future Trends site proves the pipeline: research → DB → automated page generation → publish → monetize. That same pipeline, hardened and scaled, is the foundation of a Martech SaaS platform. Every architectural decision made here — CMS choice, SEO tooling, ad infrastructure — should be evaluated through two lenses simultaneously:

| Lens | Question |
|------|----------|
| **Site lens** | Does this work for Future Trends today? |
| **Platform lens** | Can this serve 50 properties, 10 clients, or be resold as a service? |

If an enhancement only passes the site lens, it is a local fix, not an investment. Prioritize enhancements that pass both.

---

## Enhancement Index

| # | File | Theme | Status |
|---|------|-------|--------|
| 1 | [01-cms-overhaul.md](01-cms-overhaul.md) | Replace Jenkins/manual with headless CMS | Draft |
| 2 | [02-seo-stack.md](02-seo-stack.md) | SEO without SemRush — open-source + API stack | Draft |
| 3 | [03-geo-strategy.md](03-geo-strategy.md) | Generative Engine Optimization for AI search | Draft |
| 4 | [04-aio-optimization.md](04-aio-optimization.md) | AI Overview (Google AIO) optimization | Draft |
| 5 | [05-martech-consolidation.md](05-martech-consolidation.md) | Merge Martech project into unified platform | Draft |
| 6 | [06-domain-migration.md](06-domain-migration.md) | Migrate from GitHub Pages to owned domain | Draft |
| 7 | [07-monetize-adsense.md](07-monetize-adsense.md) | Google AdSense integration | Draft |
| 8 | [08-monetize-adserver.md](08-monetize-adserver.md) | Build and operate a first-party ad server | Draft |

---

## Platform Vision

```mermaid
graph TD
    subgraph Content["Content Layer (Hook)"]
        FT[Future Trends Site]
        MT[Martech Directory]
        SX[Site N...]
    end

    subgraph Platform["Martech Platform (Product)"]
        CMS[Headless CMS]
        PIPE[Research Pipeline]
        SEO[SEO Engine]
        GEO[GEO / AIO Engine]
        ADS[Ad Server]
        ANA[Analytics Layer]
    end

    subgraph Revenue["Revenue Layer"]
        ADSENSE[Google AdSense]
        DIRECT[Direct Campaigns]
        SAAS[Platform SaaS Fees]
        DATA[Data Licensing]
    end

    FT --> CMS
    MT --> CMS
    SX --> CMS
    CMS --> PIPE
    CMS --> SEO
    CMS --> GEO
    CMS --> ADS
    ADS --> ADSENSE
    ADS --> DIRECT
    CMS --> SAAS
    ANA --> DATA
```

---

## Design Principles for Every Enhancement

1. **API-first** — every component exposes an interface; nothing is wired together by hand.
2. **Multi-tenancy from day one** — even if only one tenant exists today, the data model must support N.
3. **Open-source preferred** — proprietary SaaS tools create lock-in and margin leakage; replace them where credible OSS alternatives exist.
4. **Measurable** — every enhancement has a metric that proves it is working.
5. **Incremental** — each enhancement ships in phases; no big-bang rewrites.

---

## How to Add a New Enhancement

1. Copy the template below into a new file: `NN-short-name.md`
2. Fill in: problem statement, full-scale vision, phased implementation, mermaid diagrams, success metrics.
3. Add a row to the index table above.
4. Link from `DEVELOPMENT.md` in the Martech project if implementation has started.

```markdown
# Enhancement NN — Title

## Problem
## Full-Scale Vision
## Current State
## Phased Implementation
## Architecture Diagram (mermaid)
## Success Metrics
## Open Questions
```
