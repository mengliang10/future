---
layout: page
title: Research
description: "The data pipeline, causal graph, and methodology behind Future Trends analysis."
permalink: /research/
---

# Research

Future Trends is built on a structured research pipeline that connects raw technology signals to investment theses.

## Pipeline Architecture

The research pipeline runs four automated stages, updated continuously:

| Stage | What it does | Current Scale |
|-------|-------------|---------------|
| **Ingest** | Pulls structured data from primary sources: research papers, earnings transcripts, patent filings, analyst reports, RSS feeds (1,100+ feeds via Miniflux), Telegram, Discord | 1,700+ signals/day |
| **Extract** | Parses causal claims ("X enables Y", "X precedes Y by N months") using NLP + Bayesian scoring | 100+ claims/day |
| **Graph** | Builds a directed graph of technology dependencies; computes bottleneck scores, critical path analysis, downstream impact | 212 nodes, 14 sectors |
| **Publish** | Generates sector pages, stock linkages, roadmap content, and this website from graph output | Auto-deployed via GitHub Pages |

## Graph Schema

Every sector page, stock analysis, and roadmap entry on this site is backed by a causal dependency graph of **212+ technology nodes** across 14 sectors. Each node is scored by its downstream connectivity (bottleneck score) and linked to listed equities.

Nodes represent technologies, components, or market structures. Edges represent causal relationships with typed directions:

| Edge Type | Meaning | Example |
|-----------|---------|---------|
| `CAUSES` | X directly causes Y | AI buildout → HBM memory demand |
| `PRECEDES` | X typically occurs before Y | CPO testing → data center optical adoption |
| `ENABLES` | X is a prerequisite for Y | High-NA EUV → 2nm process node |
| `AMPLIFIES` | X increases the magnitude of Y | Agentic AI → data center power demand |
| `SUPPRESSES` | X decreases Y | Insider lockup → SPCX selling pressure |
| `CORRELATES` | X and Y move together | Memory prices → semi equipment orders |
| `BLOCKS` | X prevents Y | China export controls → advanced chip access |

Each edge carries a probability score (0-1) derived from Bayesian updates over observed market outcomes, updated continuously as new data is ingested.

## Current Bottleneck Technologies (June 2026)

Technologies that unlock the most downstream nodes — the critical path for frontier tech:

| Technology | Category | Bottleneck Score | Downstream Nodes |
|-----------|----------|-----------------|-----------------|
| Silicon Photonics Interconnect | Semiconductors | 0.408 | 35 |
| 6G X-MIMO 7 GHz Network | Connectivity | 0.186 | 14 |
| AI Formal Mathematical Reasoning | AI & Cloud | 0.114 | 6 |
| Topological Qubit (Majorana Fermion) | Quantum | 0.102 | 9 |
| Quantum Error Correction (Surface Code) | Quantum | 0.092 | 8 |
| AI Materials Discovery | AI & Cloud | 0.081 | 7 |

## Data Sources

- Company earnings transcripts (NVDA, TSM, ASML, AVGO, MSFT, GOOGL, AMZN, ORCL, MU)
- Semiconductor industry reports (SEMI, Gartner, IDC, semiengineering.com)
- Academic papers (arXiv CS, Nature, IEEE, Science)
- Patent databases (USPTO, WIPO)
- RSS feeds (1,100+ via Miniflux self-hosted reader)
- Social signals (Telegram, Discord — 25+ channels)
- Prediction markets (Polymarket, Kalshi) for probabilistic inputs
- Analyst research (Seeking Alpha, The Fly, MarketFlux, Goldman Sachs, BofA)

---

*The underlying graph database and ingest pipeline are maintained privately and are not open source. This page describes the methodology publicly.*
