---
name: trace
description: "Trace namespace -- 7 skills for platform-level simulation.

/trace-request     -> request hand-compilation through service boundaries
/trace-state       -> state transition with preconditions, postconditions, invariants
/trace-contract    -> expected vs actual output comparison with mismatch severity
/trace-component   -> user action through UI component tree and re-render chain
/trace-deployment  -> deployment sequence with pre-checks and rollback path
/trace-migration   -> schema change with before/after data state and loss detection
/trace-permissions -> RBAC walk-through with privilege escalation detection

Run any sub-skill directly, or describe your system and the most relevant trace skill will run.
"
allowed-tools: [Read, Write, Glob, Grep]
param_set: analysis
---
Hand-compile a request through service boundaries, APIs, and middleware. Step by step: entry point, authentication, routing, each service boundary crossed, storage access, response assembly, error paths. No boundary skipped. Identify: failure points at each boundary, latency sources, authorization gaps, batch operation edge cases. Stock roles: Dataverse / Commerce / Automate platform expert auto-selected from context.

Write artifact to: simulations/trace/request/{topic}-request-{date}.md
