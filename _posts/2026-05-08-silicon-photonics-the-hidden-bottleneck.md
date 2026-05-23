---
layout: post
title: "Silicon Photonics: The Hidden Bottleneck Blocking 34 Technologies"
subtitle: "Copper interconnects are hitting a physical wall. The AI cluster scaling story depends on solving a packaging problem most investors have never heard of."
date: 2026-05-08
category: Semiconductors
read_time: 7
tickers: [LITE, COHR, NVDA, TSM, INTC, AMAT]
tags: [silicon photonics, co-packaged optics, data centre, interconnects, semiconductors, AI infrastructure]
---

If you want to understand what actually constrains AI cluster scaling beyond GPU count, ignore the chip architecture debates for a moment and look at copper wire. Specifically, look at what happens to copper electrical signalling at the data rates that next-generation AI clusters demand. The answer is where the most important bottleneck in our entire technology research graph lives.

## The #1 Bottleneck in Our Tech Graph

Our research pipeline — which maps causal dependencies between 212 tracked technology nodes — scores Silicon Photonics Interconnect as the single highest-impact bottleneck in the graph. The numbers: **34 downstream technology nodes** are directly or transitively blocked by this one technology, with a confidence score of 0.720 and an estimated commercial deployment window around 2028. No other technology node in our database has a comparable downstream dependency count.

To understand why, you need to understand what is happening inside an AI data centre right now.

## The Copper Wall

Modern AI training clusters link hundreds or thousands of GPUs. The interconnects — the links carrying data between chips — are the circulatory system. Today, those links use SerDes (Serialiser/Deserialiser) electrical signalling over copper. Current state-of-the-art SerDes operates at approximately 56 Gbps per lane. With PAM4 signalling and advanced DSP, this can be pushed to 112 Gbps per lane at short distances.

The problem is physics. At these data rates, copper traces attenuate signal rapidly with distance. Retimers and repeaters add latency and power consumption. At the scales required for 100,000-GPU clusters — the architecture Microsoft, Google, and Meta are building toward — electrical interconnects face three compounding constraints simultaneously: bandwidth per watt, bandwidth per millimetre of physical routing space, and signal integrity at rack-to-rack distances beyond two metres.

Optical interconnects — specifically silicon photonics using light instead of electrons — solve all three problems: 400 Gbps+ per lane, near-zero distance attenuation, and bandwidth per watt roughly 10x better than copper at these data rates.

## Co-Packaged Optics: The Architecture Shift

The traditional approach integrates optics into discrete pluggable modules at the edge of a switch or NIC — a design that still has copper electrical connections from the chip die to the optical module. These copper hops are increasingly the bottleneck.

**Co-Packaged Optics (CPO)** eliminates the copper hop entirely: optical engines are packaged directly alongside the compute die on the same substrate, reducing the electrical path to millimetres. The bandwidth density improvement is roughly 4-8x over pluggable optics, and power consumption drops by 30-50%.

The roadmap is advancing on two fronts:

**Intel** has the longest commercial silicon photonics history. Its 400G silicon photonics modules are in production. The CPO program — previously known as co-packaged optics for the Tofino series — targets integration with next-generation Xeon and custom ASICs. Intel's integrated photonics group is one of its few divisions consistently executing ahead of schedule.

**Broadcom** is pursuing CPO for its Tomahawk and Jericho switch ASICs. The BCM81000 optical DSP chipset is the first step. Hyperscalers that run custom network ASICs based on Broadcom silicon have the clearest near-term CPO upgrade path.

**NVIDIA** is working on optical integration for its NVLink and InfiniBand networking stacks — both critical for inter-GPU cluster communication. The Quantum-X800 InfiniBand switch at 3.2 Tbps aggregate bandwidth is already pushing the limits of copper-based front-panel ports.

## Why 34 Nodes Depend on This

The downstream dependency count of 34 reflects the cascading nature of the interconnect constraint. Technologies that cannot advance until silicon photonics reaches commercial maturity include: next-generation AI cluster architectures, disaggregated memory fabrics, optical computing hybrids, photonic neural networks, quantum networking (entanglement distribution requires optical channels), next-generation HPC systems, and in-memory computing interconnects. The constraint is not silicon photonics alone — it is that these architectures were designed assuming optical interconnects would be available. They are waiting.

## The Investment Timeline

The 2028 commercial deployment estimate reflects an S-curve that is already bending. Several inflection points to track:

**2025-2026:** CPO qualification by at least one Tier-1 hyperscaler for a production switch program. This is the key catalyst — once a hyperscaler's procurement team validates CPO for production, the entire supply chain shifts.

**2026-2027:** Volume production of 800G silicon photonics integrated modules. Lumentum (LITE) and Coherent (COHR) are the primary component suppliers here — wafer-scale indium phosphide laser arrays integrated with silicon waveguides.

**2027-2028:** Rack-scale CPO deployment in new AI data centre builds. At this point, pluggable optics become the legacy architecture for high-end applications, and NVIDIA, Broadcom, and Marvell start shipping switch ASICs with integrated optical engines as standard.

## Stock-by-Stock Analysis

**Lumentum (LITE)** — Pure-play optical components. Vertically integrated from chip design to module assembly. The laser chips and photonic integrated circuits at the heart of CPO come disproportionately from Lumentum's San Jose and Ottawa fabs. Revenue is cyclical with data centre capex, but the CPO transition represents a structural share gain from pluggable to co-packaged — addressable market roughly doubles. Trading at a discount to historical multiples on cyclical concerns; the 2026-2028 CPO ramp is the re-rating catalyst.

**Coherent (COHR)** — Broader optical networking exposure, including telecom. The II-VI acquisition gave Coherent vertical integration into compound semiconductors (InP, GaAs, SiC) that are essential for high-speed optical engines. More diversified than LITE but also more exposed to slower telecom cycles. The 800ZR coherent optics market and data centre DCI (Data Centre Interconnect) are near-term revenue drivers while CPO develops.

**NVIDIA (NVDA)** — Network infrastructure beneficiary. Every additional bandwidth available in AI clusters translates directly into more GPU utilisation, which drives accelerator demand. NVDA's Mellanox acquisition was specifically to own the full network stack. The transition to optical extends the viability of ever-larger GPU clusters.

**TSMC (TSM)** — Silicon photonics wafers require advanced CMOS process integration. TSMC's photonics PDK (Process Design Kit) and silicon photonics shuttle runs position it as the foundry for integrated photonic chips. CPO volume adoption is a new workload for TSMC's advanced packaging and wafer business.

**Intel (INTC)** — The most direct CPO equity play, but also the highest execution risk. Intel Foundry Services needs to win external CPO customers to justify the investment. The upside is enormous if Intel's integrated photonics becomes a platform; the risk is that customers route around Intel to TSMC or GlobalFoundries for the photonics wafers.

**Applied Materials (AMAT)** — CVD, PVD, and etch equipment for silicon photonics wafer fabrication. Every silicon photonics wafer goes through AMAT deposition and etch tools. Not a pure-play, but a no-drama way to benefit from volume ramp.

## The Thesis in One Sentence

Silicon photonics is the single technology whose commercial deployment most directly determines the pace of AI infrastructure scaling, and the listed companies that supply its components are priced as cyclical hardware vendors rather than structural bottleneck incumbents.

*Disclaimer: This is analysis and commentary, not investment advice.*
