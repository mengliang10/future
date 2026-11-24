// Analytical questions, not verified news or forecasts. Inspired by supplied research previews; see https://www.damnang.com/archive?sort=new for provenance.
export const sectorLenses: Record<string,string> = {
  "semiconductors": "Evaluate optical integration, packaging and lithography as a linked system. Usable substrate capacity, package dimensions, assembly and optical testing, and cost per good wafer can constrain accelerator shipments.",
  "memory": "Evaluate next-generation DRAM and HBM by good-die output, yield, throughput, thermal constraints and customer qualification.",
  "ai-infrastructure": "Compare GPUs and custom accelerators by workload-specific total cost, software migration, utilization, interconnects and power. Track switch-side and accelerator-side optical integration separately.",
  "robotics": "Assess physical AI using sensor reliability, closed-loop control, safety, uptime and cost per completed task in paid deployments.",
  "applied-ai": "Distinguish predictive model capability from commercial adoption and causal incremental outcomes; monitor experimentation, advertiser economics and privacy."
};
export const recordLenses: Record<string,string> = {
  "silicon-photonics-interconnect": "Compare pluggable, near-packaged and co-packaged optics by reach, power, laser integration, assembly yield and testing. Track qualified switch and accelerator deployments separately.",
  "ai-hardware-asic-tpunputrainium": "Assess cost per useful inference at matched accuracy, latency and utilization, including design amortization and software portability.",
  "ai-accelerators": "Compare benchmarks at equivalent workload, precision, power, scale and software maturity; include kernel porting costs.",
  "dram-and-hbm-demand": "Track good-die output, stacking yield, thermal performance, packaging capacity and qualification.",
  "euv-lithography-135nm": "Compare cost per good wafer, exposure throughput, yield and avoided patterning steps.",
  "high-na-euv": "Monitor process control, overlay, utilization and avoided multi-patterning steps.",
  "robotics-automation": "Measure task completion, uptime, interventions, safety and unit economics in real deployments.",
  "programmatic-display-advertising": "Use controlled experiments to distinguish attributed conversions from causal lift; monitor incremental advertiser value and privacy.",
  "nvda": "Monitor workload migration to custom silicon, optical qualification and system-level cost.",
  "amd": "Evaluate reproducible benchmarks, kernel portability and deployment economics rather than extrapolating individual model tests.",
  "mrvl": "Monitor optical and custom silicon design wins, qualifications and shipments; verify transaction and customer claims independently.",
  "avgo": "Monitor custom accelerator design wins, optical switching qualification and customer concentration.",
  "mu": "Track disclosed HBM output, yield and qualification; distinguish anecdotal testimony from company-wide evidence.",
  "asml": "Evaluate lithography throughput, utilization and customer cost per good wafer.",
  "cere.pvt": "Evaluate wafer-scale redundancy through qualified output, routing and shared-circuit constraints, test coverage and repair limits.",
  "tsm": "Monitor usable advanced packaging output, substrate availability, assembly yield and qualification.",
  "googl": "Compare custom accelerator economics including design amortization, compiler support and utilization.",
  "meta": "Monitor AI advertising adoption and incremental advertiser value using controlled experiments."
};
