---
agent: 'agent'
tools: ['codebase']
description: 'ETL pipeline and sync process tracing with data loss and schema mismatch detection.'
---

depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Trace data through ETL pipelines, sync processes, CDX flows, or dual-write patterns. For each data item: source, transformations at each stage, destination, latency, error handling at each boundary. Identify: data loss points, schema mismatches, stale data windows, missing error recovery. Stock roles: Finance / Operations / Commerce data domain expert.

Write artifact to: simulations/flow/dataflow/{topic}-dataflow-{date}.md
