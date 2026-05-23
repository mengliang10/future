---
layout: post
title: "Silicon Photonics: The Hidden Bottleneck"
subtitle: "The AI infrastructure buildout has a chokepoint most investors have never heard of. It blocks more downstream technologies than any other single node in our research graph."
date: 2026-05-08
category: Semiconductors
read_time: 6
tickers: [LITE, COHR, NVDA, TSM, INTC, AMAT]
tags: [silicon photonics, co-packaged optics, data centre, interconnects, AI infrastructure]
---

Everyone is focused on GPUs. The real constraint holding back the next generation of AI clusters is copper wire.

This is not a metaphor. At the data rates required to link hundreds of thousands of GPUs - the scale that Microsoft, Google, and Meta are actively building toward - electrical copper interconnects are hitting a hard physics wall. Signal degrades with distance. Power consumption scales with bandwidth. Routing density runs out of room. These three constraints compound simultaneously as cluster sizes grow.

The solution is silicon photonics: using light instead of electrons to carry data between chips. It is not a new idea. It is, finally, commercially viable - and the companies that supply it are priced as cyclical hardware vendors rather than structural bottleneck incumbents.

## Why This Technology Unlocks Everything Else

Our research into technology dependencies identified silicon photonics interconnect as the single highest-impact bottleneck in the AI infrastructure stack. More downstream technologies are directly blocked by this one node than by any other. The list includes next-generation AI cluster architectures, disaggregated memory fabrics, photonic computing hybrids, quantum networking, and in-memory computing interconnects.

These architectures were designed assuming optical interconnects would be available. They are waiting.

The reason is straightforward: optical interconnects deliver roughly ten times better bandwidth per watt than copper at the data rates modern AI clusters demand, with near-zero signal degradation over distance. The transition is not about marginal improvement - it is about enabling a category of infrastructure that simply cannot be built with copper.

## The Architecture Shift: Co-Packaged Optics

Traditional data centres use pluggable optical modules at the edge of a switch. There is still a short copper electrical path from the chip to the optical module - and at current data rates, that copper hop is itself the bottleneck.

Co-packaged optics eliminates it entirely. The optical engine is packaged directly alongside the compute die on the same substrate, reducing the electrical path to millimetres. The result is a four-to-eight-fold improvement in bandwidth density and a 30–50 percent reduction in power consumption versus pluggable modules.

Broadcom is pursuing this for its switch ASICs. NVIDIA is working on optical integration for NVLink and InfiniBand. Intel has the longest production history in silicon photonics and is the most direct bet, though also the highest execution risk given Intel Foundry's challenges. The first major hyperscaler production qualification - expected in the 2026–2027 window - is the catalyst that shifts the entire supply chain.

## Who Wins

**[Lumentum](/stocks/LITE/)** is the clearest pure-play. Vertically integrated from chip design to module assembly, Lumentum supplies the laser chips and photonic integrated circuits that sit at the heart of co-packaged optics. Their addressable market roughly doubles with the transition from pluggable to co-packaged - and they are currently trading at a discount to historical multiples on cyclical concerns. The co-packaged optics ramp is the re-rating catalyst.

**[Coherent](/stocks/COHR/)** brings broader optical networking exposure including telecom, and critical vertical integration into compound semiconductors - the indium phosphide and gallium arsenide that high-speed optical engines require. More diversified than Lumentum, with near-term revenue supported by 800ZR coherent optics and data centre interconnect demand while co-packaged optics develops.

**[NVIDIA](/stocks/NVDA/)** benefits indirectly but substantially. Every additional bandwidth available in a cluster translates directly into higher GPU utilisation, which is the metric that drives accelerator demand. The Mellanox acquisition was specifically to own the full network stack. Optical interconnects extend the viability of ever-larger clusters - which extends the runway for GPU demand.

**[TSMC](/stocks/TSM/)** captures a new category of wafer work. Silicon photonics wafers require advanced CMOS process integration, and TSMC's photonics process design kit and shuttle run program position it as the foundry of record for integrated photonic chips.

**[Applied Materials](/stocks/AMAT/)** is the no-drama infrastructure play: every silicon photonics wafer goes through Applied's deposition and etch tools. Not a pure-play, but a clean way to benefit from volume ramp without picking a specific architecture winner.

## The Thesis in One Sentence

Silicon photonics is the single technology whose commercial deployment most directly determines the pace of AI infrastructure scaling - and the companies supplying it are priced as though that scaling is someone else's problem.

*Disclaimer: This is analysis and commentary, not investment advice.*
