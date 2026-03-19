---
name: request
description: "Hand-compile a request through service boundaries, APIs, and middleware. Step by step: entry point, authentication, rout"
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


---

### STEP 8a -- SCOPE-STRING TABLE

| BC-N | Boundary Name | Scope String | Source Step | Gap? |

---

### STEP 8b -- COHERENCE CHECK (three-phase lifecycle)

For each Gap?=Y boundary, execute three explicit sub-steps:

**8b-i -- ARM COLLECTION:** Collect the three coherence arms for this boundary:
- ARM-1 (Step3-Auth): [auth token / scope claim from Step 3]
- ARM-2 (Step8a-Invoked): [scope string from Step 8a table]
- ARM-3 (Step11-Params): [param-set from Step 11]

**8b-ii -- COHERENCE ASSERTION:** State whether the three arms are coherent. Prose assertion required.

**8b-iii -- CONTRADICTION DETECTION:** If assertion is coherent AND Step 8c will produce Match? = N, fire: