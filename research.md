---
layout: page
title: Research
description: "The data pipeline, causal graph, and methodology behind Future Trends analysis."
permalink: /research/
---

# Research

Future Trends is built on a structured research pipeline that connects raw technology signals to investment theses.

## What the pipeline produces

Every sector page, stock analysis, and roadmap entry on this site is backed by a causal dependency graph of **212+ technology nodes** across 14 sectors. Each node is scored by its downstream connectivity (bottleneck score) and linked to listed equities.

The research pipeline runs four stages:

| Stage | What it does |
|-------|-------------|
| **Ingest** | Pulls structured data from primary sources: research papers, earnings transcripts, patent filings, analyst reports |
| **Extract** | Parses causal claims ("X enables Y", "X precedes Y by N months") and scores confidence |
| **Graph** | Builds a directed graph of technology dependencies; computes bottleneck scores, critical path analysis |
| **Publish** | Generates sector pages, stock linkages, and roadmap content from graph output |

## Graph schema

Nodes represent technologies, components, or market structures. Edges represent causal relationships with typed directions: `CAUSES`, `PRECEDES`, `AMPLIFIES`, `SUPPRESSES`, `CORRELATES`, `BLOCKS`.

Each edge carries a probability score (0-1) derived from Bayesian updates over observed market outcomes, updated continuously as new data is ingested.

## Data sources

- Company earnings transcripts (NVDA, TSM, ASML, AVGO, MSFT, GOOGL, AMZN)
- Semiconductor industry reports (SEMI, Gartner, IDC)
- Academic papers (arXiv CS, Nature, IEEE)
- Patent databases
- Prediction markets (Polymarket, Kalshi) for probabilistic market inputs

---

*The underlying graph database and ingest pipeline are maintained privately and are not open source.*
