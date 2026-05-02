---
layout: post
title: "NVIDIA Blackwell: The Supply Chain Behind the Most Important Chip in the World"
subtitle: "CoWoS capacity, HBM3E allocation, and what the GB200 NVL72 rack means for the semi ecosystem."
date: 2026-05-02
category: Semiconductors
read_time: 8
tickers: [NVDA, TSM, MU, AMAT, LRCX]
tags: [NVIDIA, Blackwell, semiconductors, supply chain, AI chips]
---

The NVIDIA GB200 NVL72 is not a chip. It is a compute rack containing 36 Grace CPUs and 72 Blackwell B200 GPUs, connected by NVLink Switch chips, drawing 120kW of power, and delivering 30 petaflops of FP8 inference performance. Understanding how this product is built — and where the supply chain bottlenecks lie — is essential for understanding the semiconductor investment thesis for 2026–2028.

## The CoWoS Bottleneck

CoWoS (Chip-on-Wafer-on-Substrate) is TSMC's advanced packaging technology that stacks the compute die and HBM memory on a silicon interposer. Every H100 and B200 requires it. TSMC's CoWoS capacity is the single most important constraint on AI accelerator supply.

In 2024, TSMC could produce roughly 50,000–60,000 CoWoS substrates per month. Demand for H100/H200 exceeded this by a significant margin through most of the year. TSMC has been aggressively expanding CoWoS capacity through:

1. Converting existing fab space at Hsinchu and Taichung
2. Building dedicated CoW (Chip-on-Wafer) capacity at Fab 6
3. Qualifying additional substrate suppliers (ASE, Amkor)

Estimated CoWoS capacity by end 2026: ~90,000–100,000 units/month. Still likely below peak demand if hyperscaler capex guidance holds.

**Investment implication:** TSMC's packaging revenue is growing faster than wafer revenue. AMAT and LRCX supply key deposition and etch equipment for advanced packaging. Both are CoWoS beneficiaries beyond just the node story.

## HBM3E: The Memory Equation

Each B200 GPU ships with 192GB of HBM3E (High Bandwidth Memory 3E) across 8 stacks. The NVL72 rack thus requires 72 × 8 = 576 HBM3E stacks. SK Hynix supplies the majority; Micron (MU) is qualifying to take meaningful share in 2025–2026.

HBM is a premium product with high ASPs and tight supply. MU's HBM margin profile is significantly better than its DRAM commodity business. A successful HBM3E qualification at NVIDIA is a multi-year revenue and margin catalyst for Micron.

## The Thermal Problem

120kW per rack requires liquid cooling. Air cooling is not viable at this power density. This creates a demand signal for:
- Direct liquid cooling infrastructure (CDW, Vertiv)
- Facility power upgrades (ETN, PWR)
- Specialised server designs (DELL, HPE, SMCI)

SMCI's advantage is speed-to-market with custom cooling configurations. The company's share price volatility has been extreme, but its positioning in the AI server ecosystem is structurally sound.

## Key Takeaways

- **TSMC CoWoS** is the supply chain pinch point through 2027; TSMC and AMAT are structurally advantaged
- **Micron HBM** success is a high-conviction catalyst; the stock trades at a discount to its AI revenue potential
- **Power infrastructure** stocks (ETN, PWR) are the most underloved Blackwell derivatives
- **SMCI** high risk / high reward on continued AI server demand; accounting/governance risk remains

*Disclaimer: This is analysis and commentary, not investment advice.*
