---
name: signal-trace-migration
description: Schema change tracing with before/after data state and data loss detection.
allowed-tools: [Read, Write, Glob]
param_set: analysis
---
Trace before/after a schema change or version upgrade. For each changed entity: what data exists before, what the migration does to it, what the state is after. Identify: data loss paths, nullable violations, missing default values, performance cliffs from schema changes. Stock roles: Commerce / Finance / Operations migration expert.

Write artifact to: simulations/trace/migration/{topic}-migration-{date}.md
