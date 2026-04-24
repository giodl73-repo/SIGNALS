---
mode: agent
description: "ETL pipeline and sync process tracing with data loss and schema mismatch detection."
---
Trace data through ETL pipelines, sync processes, CDX flows, or dual-write patterns. For each data item: source, transformations at each stage, destination, latency, error handling at each boundary. Identify: data loss points, schema mismatches, stale data windows, missing error recovery. Stock roles: Finance / Operations / Commerce data domain expert.

Write artifact to: signals/flow/dataflow/{topic}-dataflow-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
