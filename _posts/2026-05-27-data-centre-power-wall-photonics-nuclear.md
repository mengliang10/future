---
layout: post
title: "The Data Centre Power Wall"
subtitle: "Silicon photonics unlocks 34 downstream technologies. Nuclear closes the energy gap. Our research graph now shows these two constraints dominating everything else in the AI stack."
date: 2026-05-27
category: Semiconductors
read_time: 8
tickers: [MRVL, AVGO, NVDA, TSM, CEG, SMR, CCJ, GEV, ETN, ANET, INTC, II]
tags: [silicon photonics, data centres, nuclear energy, AI infrastructure, semiconductors, power, bottleneck analysis]
---

The AI stock rally of May 2026 is being priced as a software story: valuations driven by inference demand, model capability, and the compounding returns of agent autonomy. But our research graph tells a different story at the physical layer. The biggest single constraint on the AI build-out is not compute or software. It is the movement of data inside data centres, and the electricity required to run them.

Our causal dependency graph now covers 212 technology nodes across 14 sectors. We score each node by how many downstream technologies it enables: its *bottleneck score*. The single highest-scoring node in the entire graph, by a wide margin, is **Silicon Photonics Interconnect**, with a bottleneck score of 0.585 and 34 downstream dependencies. The next closest node, 6G Extreme-MIMO, scores 0.280. Photonics is not just an important node. It is in a different tier of criticality than everything else we track.

## Why Photonics Unlocks Everything Else

The core problem is bandwidth-per-watt inside the data centre. Copper interconnects have served computing well for four decades, but at the scale required by modern AI training (clusters of 100,000 GPUs or more, moving petabytes of activations per second) copper hits two walls simultaneously: latency from signal integrity degradation over distance, and thermal density from resistive losses.

Optical interconnects move data on photons instead of electrons. The physics are fundamentally different: photons do not generate resistive heat and travel at the speed of light with essentially zero signal degradation over relevant distances. Co-packaged optics (CPO), integrating photonic engines directly on the switch package, eliminates the external optical module entirely, reducing the power budget for data movement by an estimated 75 percent at scale.

The 34 downstream nodes that Silicon Photonics unlocks in our graph include: AI hardware ASIC design at scale, neuromorphic computing chips, compute-in-memory architectures, wafer-on-wafer 3D integration, autonomous robotics sensor fusion, and several quantum networking nodes. This is not a coincidence. Photonics is the plumbing that allows every other high-bandwidth technology to function at commercially viable power densities.

Our confidence score for Silicon Photonics as a deployable technology is +0.72, with a mode year of 2028. The technology is not speculative: volume production is already underway at several fabs. What 2028 represents is the crossover point at which CPO becomes the default interconnect standard rather than the premium option.

**Stocks with direct exposure:** MRVL (optical DSP and CPO silicon), AVGO (InfiniBand and Ethernet ASICs), INTC (silicon photonics manufacturing via Intel Foundry), ANET (network switches requiring CPO integration), II (Coherent Corp, pure-play photonics).

## The Energy Problem That Precedes the Photonics Solution

Photonics reduces the power density of data movement. It does not solve the underlying power supply problem. A frontier AI training cluster today consumes roughly 100-200 megawatts. The next generation, driven by post-Blackwell architectures and the requirement to train models at 10 to 100 times current parameter counts, will require one gigawatt or more per facility. There is no grid in the world that was designed to deliver this.

Our research graph scores **Solid-State Battery** as the #1 energy technology bottleneck (score 0.083, 5 downstream nodes, est 2029), but for the immediate data centre constraint, the relevant node is something more basic: grid interconnection capacity. The permitting and construction backlog for large power connections to US substations now runs 5 to 12 years in most jurisdictions. The AI hyperscalers cannot wait.

This is why our evidence pipeline has been picking up an accelerating signal in two specific areas: small modular reactors (SMRs) and direct power purchase agreements with existing nuclear plants. The mechanism is straightforward: nuclear provides 24/7 baseload power at high density on a small land footprint, without the intermittency problems of solar and wind that make large-scale battery storage mandatory. For a data centre operator, a nuclear PPA eliminates the grid interconnection problem entirely.

The evidence today from our nuclear feed is consistent with this thesis: world nuclear capacity additions are running ahead of schedule for 2026, driven primarily by Asia, and US tech company interest in direct nuclear offtake has moved from exploratory to contractual in several cases.

**Stocks with direct exposure:** CEG (Constellation Energy, largest US nuclear operator with existing tech PPAs), SMR (NuScale, SMR design), CCJ (Cameco, uranium supply), GEV (GE Vernova, grid infrastructure and reactor services), ETN (Eaton, power distribution and data centre electrical systems).

## What the Graph Says About Timing

The chart below summarises the confidence scores and estimated deployment years for the top bottleneck nodes in our current graph snapshot.

| Node | Category | Conf | Est Year | Bottleneck Score | Downstream Nodes |
|------|----------|------|----------|-----------------|-----------------|
| Silicon Photonics Interconnect | Semiconductors | +0.72 | 2028 | **0.585** | 34 |
| 6G Extreme-MIMO | Connectivity | +1.00 | 2026 | 0.280 | 14 |
| Quantum Error Correction (Surface Code) | Quantum | +0.80 | 2026 | 0.144 | 8 |
| Topological Qubit (Majorana) | Quantum | +0.55 | 2030 | 0.140 | 9 |
| AI Materials Discovery | AI & Cloud | +0.75 | 2028 | 0.122 | 7 |
| AI Formal Mathematical Reasoning | AI & Cloud | +0.90 | 2026 | 0.114 | 6 |
| Fault-Tolerant QC (1,000 Logical Qubits) | Quantum | +0.85 | 2028 | 0.111 | 6 |
| Solid-State Battery | Energy Tech | +0.65 | 2029 | 0.083 | 5 |
| Compute-in-Memory (CIM) | Semiconductors | +0.60 | 2029 | 0.080 | 5 |
| Full Rocket Reusability (Starship) | Space Tech | +0.82 | 2025 | 0.091 | 5 |

The striking feature of this table is the gap between Silicon Photonics (0.585) and everything else. If you force-rank technology investments by the number of other technologies they enable, photonics is not a niche bet on optical networking. It is the highest-leverage node in the AI infrastructure stack.

The second observation is how many high-confidence nodes cluster around 2026: 6G, Quantum Error Correction, AI Formal Reasoning. These are not predictions: they are nodes our evidence pipeline has already marked as achieved or in production. The graph is updating in real-time as evidence comes in from academic papers, engineering journals, and technology news.

## The Capital Flow Implication

The current AI rally is priced primarily on software and inference. NVIDIA trades at a premium that reflects GPU demand. The hyperscalers are valued on compute capacity. What is not yet fully priced is the capital required to solve the physical layer: specifically, photonics manufacturing capacity and nuclear power infrastructure.

Both of these have long lead times. A photonics fab expansion takes three to five years from capex commitment to volume production. A nuclear power agreement from signing to first power is seven to fifteen years for new builds, or two to four years for existing plant reactivations. The investment community tends to underweight infrastructure with long lead times because the payoff is outside the standard forecasting horizon. Our graph suggests this is exactly backwards: the earlier in the dependency chain a constraint sits, the more important it is to price correctly.

The current evidence weight in our pipeline assigns:
- **Semiconductors** (photonics, CIM, neuromorphic, 3D integration): 12 active bottleneck nodes, avg confidence +0.72
- **Energy Tech** (solid-state battery, SMR, grid storage): 10 active bottleneck nodes, avg confidence +0.65
- **AI & Cloud** (materials discovery, formal reasoning, agent memory): 12 active bottleneck nodes, avg confidence +0.81

The AI & Cloud category has the highest confidence scores but the lowest bottleneck scores: meaning the AI software layer is well-understood and rapidly advancing, but it depends on physical infrastructure that is moving more slowly. This is the investment gap the graph is pointing at.

## What This Means for Portfolios

The practical read from this bottleneck analysis is not that you should underweight AI software. It is that the physical infrastructure stocks: specifically photonics and nuclear: are underpriced relative to the returns they will capture if the AI build-out continues at the pace currently signalled by hyperscaler capex guidance.

The asymmetry: if AI capex slows, software-heavy names correct first and hardest. Photonics and nuclear infrastructure retain value because they have use cases beyond AI. If AI capex accelerates, photonics and nuclear are the tightest supply constraints in the stack: price discovery there will happen late and fast.

Our research graph will continue to update as new evidence comes in. The bottleneck scores, confidence levels, and downstream dependency counts are recalculated weekly as papers, news, and engineering data flow through the pipeline. This snapshot represents the state of the graph as of May 27, 2026.
