---
layout: post
title: "Macro Causal Signals: What the Research Pipeline Found"
subtitle: "We ingested 2,545 documents and extracted 1,409 active causal rules. Here is what the most robust ones say about the current environment."
date: 2026-05-23
category: Macro
read_time: 8
tickers: []
tags: [macro, yield curve, GDP, recession, gold, credit spreads, causal inference, research pipeline]
---

Most investment research uses correlations. Correlations are observed patterns between variables across historical periods. They break without warning because they are not grounded in mechanism — when the underlying cause-and-effect relationship changes, the correlation disappears. Our research pipeline takes a different approach: it extracts and validates **causal claims** from primary sources, scores them by the number of independent sources making the same claim, and then backtests the rules against historical data to assign a Sharpe ratio. The result is a database of 1,409 active causal rules, each with a source count, lag window, and empirical Sharpe.

Here is what the most robust rules in that database say, and what they imply right now.

## How the Pipeline Works

The pipeline ingests three categories of primary sources: Federal Reserve speeches and FOMC minutes, Bank for International Settlements (BIS) research papers, and curated academic economics journals via RSS. Each document is chunked and processed by a language model that extracts structured causal claims in the format: `[VARIABLE A] → [EDGE TYPE] → [VARIABLE B]`, where edge types include CAUSES, AMPLIFIES, SUPPRESSES, and PRECEDES.

Extracted claims are staged and validated before entering the rules database. Validation involves two steps: source count (a rule requires at least one independent source beyond the initial extraction; most strong rules have dozens); and backtest validation (the rule's implied trading signal is backtested against available historical data, and rules with negative Sharpe ratios are flagged for review). The Sharpe ratios reported below are empirical — measured against real data, not simulated.

The current database contains 1,409 active rules drawn from 2,545 ingested documents.

## The Most Robust Rules

### 1. Yield Spread (10Y-2Y) → GDP Growth

**Confidence: 1.000 | Sources: 952 | Lag: 90-270 days | Sharpe: 8.56**

This is the single strongest rule in the entire database, by every metric simultaneously: maximum confidence, highest source count by far (952 independent sources — nearly double the next-largest), and a Sharpe ratio of 8.56 that would be extraordinary for any systematic strategy. The mechanism is well established: a steeper yield curve indicates that banks can borrow short-term cheaply and lend long-term profitably, encouraging credit expansion and economic activity. An inverted curve does the reverse — it compresses bank margins, tightens credit supply, and precedes economic slowdown.

The lag window of 90-270 days means yield curve changes take 3-9 months to show up in GDP growth statistics. This is one of the most reliably exploitable signals in macro investing — and the 952-source consensus is why.

**Current implication:** Monitor the 10Y-2Y spread direction, not just level. A spread that is inverted but steepening is a different signal than one that is flat and beginning to invert.

### 2. Unemployment Rate → GDP Growth

**Confidence: 1.000 | Sources: 3 | Lag: 90-180 days | Sharpe: 10.17**

Maximum confidence with only 3 sources and the highest Sharpe in the database at 10.17. Three sources sounds low — but confidence 1.000 means all three sources are in complete agreement on direction and magnitude. The mechanism (Okun's Law and related) is taught in every undergraduate economics course: falling unemployment leads to rising incomes, consumer spending, and GDP; rising unemployment has the reverse effect with a 3-6 month lag. The Sharpe of 10.17 reflects that this relationship is exceptionally clean historically — few false signals.

**Current implication:** Any sustained rise in unemployment claims data has GDP implications with 3-6 month forward visibility. This is why weekly initial claims data moves markets despite being a lagging indicator of individual job losses — it is a leading indicator of aggregate demand.

### 3. HY Credit Spread → Value Factor

**Confidence: 0.774 | Sources: 31 | Lag: 30-90 days | Sharpe: 1.97**

Thirty-one sources at 0.774 confidence, 1-3 month lag. High-yield credit spreads widen when credit markets are pricing in elevated default risk — typically at the onset of or during economic stress. When spreads widen, the Value factor (long cheap stocks vs short expensive stocks) tends to outperform. The mechanism: in stress environments, the growth premium embedded in expensive stocks is discounted more harshly, while cheap stocks with real earnings and cash flows hold value better. This is a cross-asset rule with genuine trading utility — at 1.97 Sharpe over a 30-90 day signal window, it is the most actionable of the credit-to-equity relationships in our database.

**Current implication:** Watch HY spreads (ICE BofA High Yield Index, ticker HY on Bloomberg) as a leading indicator for Value vs Growth factor rotation. Spread widening of 50+ basis points over a 4-week period has historically been the threshold for a durable factor rotation signal.

### 4. Yield Curve Inversion → US Recession

**Confidence: 0.745 | Sources: 221 | Lag: 365-540 days | Sharpe: 3.46**

This is the yield curve's most widely discussed property, and the 221-source count reflects decades of academic and central bank research. At confidence 0.745 it is not certainty — there are false positives (2019's brief inversion that did not produce an organic recession before COVID distorted everything). The 12-18 month lag is the critical parameter: yield curve inversions are not a signal for immediate action; they are a signal to manage portfolio duration and cyclical exposure over the following year.

**Current implication:** The 10Y-2Y spread inverted significantly in 2022-2023 and has been normalising. The 12-18 month lag from peak inversion means the GDP impact window runs through 2024-2025. Forward-looking, a period of normalisation after inversion is historically a mixed signal — it can precede recovery, or it can represent the disinversion that occurs as short-term rates are cut in response to a recession that is already underway. Distinguish between "bear steepener" (long rates rising) and "bull steepener" (short rates falling) disinversion — the latter is the recession-risk scenario.

### 5. 10Y Real Yield (TIPS) → Gold Price

**Confidence: 0.591 | Sources: 136 | Sharpe: 1.65**

Gold's relationship with real yields is mechanistically clean: gold has no yield, so its opportunity cost rises as real yields rise and falls as real yields fall. One hundred thirty-six sources validate this in our database. The 0.591 confidence reflects that gold has other drivers (geopolitical risk, USD strength, central bank purchases) that create noise around the real yield signal.

### 6. DXY → Gold Price (Suppression)

**Confidence: 0.677 | Sources: 4 | Sharpe: 1.99**

The USD denominating relationship. Gold is priced in dollars; a stronger dollar makes gold more expensive in foreign currency, reducing foreign demand. The 0.677 confidence and 1.99 Sharpe are solid for a 4-source rule, reflecting how clean this cross-asset relationship is. Combined with the real yield rule, the gold positioning framework becomes: fade gold when (real yields rising AND DXY strengthening), accumulate on the reverse combination.

## What These Rules Imply Right Now

Reading these rules against current conditions:

**GDP trajectory:** The yield spread and unemployment rules are the two highest-confidence inputs. The current shape and direction of both matters more than any single data point.

**Factor positioning:** HY credit spreads at elevated levels (above 400bps) signal Value over Growth. At compressed levels (below 300bps), growth premium is easier to sustain.

**Gold:** The real yield / DXY combination creates the clearest systematic signal. If real yields are declining (Fed cutting) while DXY is also weakening (dollar bear market), gold has historically been one of the most reliable assets to own.

**Recession timing:** Any yield curve inversion that occurred in the 2022-2023 period should have materialised in GDP impact by now, consistent with the 12-18 month lag. New inversions from current levels would reset the recession clock forward.

The causal rules approach does not replace judgment — it organises evidence. The 952-source yield spread rule is not telling you to trade mechanically off the 10Y-2Y spread; it is telling you that 952 independent academic and central bank research documents agree that the mechanism is real, the direction is consistent, and the lag window is well-defined. That is the most reliable foundation available for macro reasoning.

*Disclaimer: This is analysis and commentary, not investment advice.*
