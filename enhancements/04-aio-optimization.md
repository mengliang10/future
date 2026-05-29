# Enhancement 04: AIO (AI Overview Optimization)

## Problem

Google's AI Overviews (formerly Search Generative Experience, SGE) now appear for roughly 30–40% of informational queries in the US. An AI Overview occupies the top of the SERP above all organic results, and the user often gets the answer without scrolling. Pages that feed AI Overviews receive a source chip citation: a different conversion mechanism than a ranked blue link. Pages not cited in AIO become invisible for that query class, regardless of their organic rank.

AIO differs from GEO (Enhancement 03) in a critical way: **GEO targets third-party AI assistants like ChatGPT/Perplexity; AIO targets Google's own SERP experience.** Both must be addressed, but with different signals and tactics.

---

## Full-Scale Vision

Every content page on the platform is structured and maintained so that Google's AI system can extract, summarise, and cite it in AI Overviews. This requires content architecture that favours directness and authority over engagement-bait writing, combined with structured data that signals the page's fitness for summarisation.

```mermaid
graph LR
    subgraph UserQuery["User Query on Google"]
        Q1["What is solid-state battery status 2025?"]
        Q2["When will autonomous vehicles deploy?"]
        Q3["Best stocks for AI infrastructure?"]
    end

    subgraph SERP["Google SERP"]
        AIO_BOX["AI Overview Box\n(above all organic results)"]
        ORG["Organic Results\n(position 1-10)"]
    end

    subgraph OurPages["Our Pages (Cited Source)"]
        TECH["_tech/solid-state-batteries.md"]
        SECTOR["sectors/autonomous.md"]
        STOCK["_stocks/nvda.md"]
    end

    Q1 --> AIO_BOX
    Q2 --> AIO_BOX
    Q3 --> AIO_BOX
    AIO_BOX -.->|source chip citation| TECH
    AIO_BOX -.->|source chip citation| SECTOR
    AIO_BOX -.->|source chip citation| STOCK
    TECH --> ORG
    SECTOR --> ORG
    STOCK --> ORG
```

---

## How Google AI Overviews Select Sources

Google has not published a specification, but analysis of AI Overview citations points to five consistent signals:

```mermaid
mindmap
  root((AIO Source Selection))
    Authority Signals
      Domain age and backlinks
      E-E-A-T author credentials
      HTTPS + Core Web Vitals
    Content Structure
      Direct answer in first paragraph
      Short declarative sentences
      FAQ sections with explicit Q+A format
      Tables with labeled rows and columns
    Schema Markup
      FAQPage schema
      HowTo or TechArticle schema
      speakable sections marked up
    Query Alignment
      Page explicitly answers the question asked
      Title matches common query phrasing
      Heading text mirrors question syntax
    Freshness
      dateModified within 90 days
      Evidence is dated, not evergreen-vague
```

---

## Content Architecture Changes

### 1. Direct-Answer Opening Paragraph

Google AIO prefers pages where the first 150 words directly answer the most likely query. Current tech node pages lead with the description. They should lead with a direct-answer summary block:

**Current:**
> Solid-State Batteries are an energy storage technology using solid electrolytes instead of liquid...

**AIO-Optimised:**
> **Solid-State Batteries: Current Status (2025)**: Commercial pilot deployments are underway at Toyota and CATL as of 2025. Volume production is estimated for 2027–2029. Our research database tracks 7 independent sources confirming pilot-stage readiness, with confidence score +0.62 (Researching).

```mermaid
flowchart TD
    subgraph PageTop["Page Opening: First 200 Words"]
        ANSWER[Direct answer to implied query\nStatus + Timeline + Confidence]
        EVIDENCE[Evidence count + confidence score]
        CLAIM[One key cited claim with date]
    end

    subgraph PageBody["Page Body"]
        STATUS[Status Table]
        PREREQS[Prerequisites]
        ENABLES[What This Enables]
        INVEST[Investment Exposure]
    end

    subgraph PageBottom["Page Bottom: AIO Boosters"]
        FAQ[FAQ Section: 3-5 common questions + direct answers]
        RELATED[Related Technologies]
    end

    PageTop --> PageBody --> PageBottom
```

### 2. FAQ Section (Auto-Generated from DB Fields)

Each tech node page should auto-generate a FAQ section from DB fields. This maps directly to Google's `FAQPage` schema and is a high-signal AIO source trigger.

| Question Template | DB Field Used |
|-------------------|---------------|
| What is [name]? | description |
| What stage is [name] at? | production_stage + STAGE_TEXT |
| When will [name] be commercially available? | est_year_mode + est_year_range |
| How confident is the [name] timeline? | confidence + conf_label |
| Which companies are investing in [name]? | tickers + stocks |
| What does [name] enable? | edges (ENABLES type) |
| What does [name] require? | edges (REQUIRES type) |

```liquid
{% comment %} Jekyll template fragment: FAQ section {% endcomment %}
<section class="faq-section" itemscope itemtype="https://schema.org/FAQPage">
  <h2>Frequently Asked Questions</h2>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 itemprop="name">What is {{ page.title }}?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">{{ page.subtitle }}</p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 itemprop="name">When will {{ page.title }} be commercially deployed?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">
        {% if page.est_year %}
          Estimated commercial deployment: {{ page.est_year }}
          {% if page.est_year_range %}(range: {{ page.est_year_range }}){% endif %}.
        {% else %}
          Timeline is not yet determined: technology is in early research phase.
        {% endif %}
      </p>
    </div>
  </div>
</section>
```

---

## AIO vs Organic Rank: Dual Optimisation

A page can rank #1 organically and still not be cited in the AI Overview, or vice versa. Optimise for both simultaneously with different levers:

```mermaid
quadrantChart
    title Page Optimisation Levers
    x-axis Organic SEO Impact --> AIO Impact
    y-axis Low Effort --> High Effort
    quadrant-1 Do First
    quadrant-2 Batch Later
    quadrant-3 Skip
    quadrant-4 Worth It Long-term
    Direct answer opening paragraph: [0.8, 0.2]
    FAQ section with schema: [0.75, 0.35]
    dateModified freshness: [0.7, 0.15]
    Internal linking structure: [0.4, 0.4]
    FAQPage JSON-LD schema: [0.65, 0.25]
    Backlink building: [0.3, 0.85]
    Page speed LCP optimization: [0.45, 0.55]
    Author bio / E-E-A-T page: [0.55, 0.6]
    Speakable schema: [0.6, 0.45]
```

---

## `speakable` Schema Markup

Google's `speakable` property flags specific sections of a page as AIO-ready summaries. This is a direct signal to the AI Overview system:

```json
{
  "@context": "https://schema.org/",
  "@type": "TechArticle",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".aio-summary", ".status-table", ".faq-section"]
  }
}
```

Requires adding a `.aio-summary` div to each tech node page containing the direct-answer opening paragraph.

---

## AIO Monitoring

Track whether our pages appear in AI Overviews using the Search Console API (Google now exposes AIO impressions/clicks) plus manual spot checks:

```mermaid
sequenceDiagram
    participant CRON as Weekly Cron
    participant GSC as Search Console API
    participant DB as seo_intelligence.db
    participant ALERT as Alert System

    CRON->>GSC: Pull impressions with search_type=DISCOVER
    CRON->>GSC: Pull AIO appearance data (searchAppearance=AI_OVERVIEW)
    GSC-->>CRON: Pages with AIO impressions + clicks
    CRON->>DB: Store page, query, impressions, clicks, date
    CRON->>DB: Compare vs prior week
    DB->>ALERT: Pages that lost AIO presence → investigate
    DB->>ALERT: New AIO appearances → record winning content pattern
```

---

## Phased Implementation

| Phase | Deliverable | Effort |
|-------|-------------|--------|
| 1 | Direct-answer summary block in Jekyll layout | 2 days |
| 2 | Auto-generated FAQ section from DB fields | 3 days |
| 3 | FAQPage + speakable JSON-LD in template | 2 days |
| 4 | `dateModified` header injection from `source_date` | 1 day |
| 5 | GSC AIO monitoring integration | 1 week |
| 6 | AIO appearance tracking dashboard | 1 week |

---

## Success Metrics

| Metric | Baseline | 6-Month Target |
|--------|----------|----------------|
| Pages with direct-answer opening | 0% | 100% |
| Pages with FAQ section | 0% | 100% |
| AIO impressions/month (GSC) | 0 | 500+ |
| AIO click-through rate | N/A | >5% |
| Pages cited in AI Overviews | 0 | 30+ |

---

## Open Questions

- Google has not made the AIO source selection algorithm public: all signals above are inferred from pattern analysis. Monitor `searchAppearance` field in GSC as the authoritative signal.
- Is there a conflict between AIO optimization (brevity, direct answers) and depth-of-content SEO (longer pages rank better)? Resolution: put the direct answer first, then depth below the fold.
- Should the direct-answer summary block be visually styled (highlighted box) or invisible to readers? Styled is better: it increases dwell time and signals deliberate information architecture.
