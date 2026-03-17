---
name: trace-migration
description: Schema change tracing with before/after data state and data loss detection.
allowed-tools: [Read, Write, Glob]
param_set: analysis
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


Trace before/after a schema change or version upgrade. For each changed entity: what data exists before, what the migration does to it, what the state is after. Identify: data loss paths, nullable violations, missing default values, performance cliffs from schema changes. Stock roles: Commerce / Finance / Operations migration expert.

Write artifact to: simulations/trace/migration/{topic}-migration-{date}.md
