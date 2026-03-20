---
name: tools-coverage
description: "Show Signal coverage statistics for a topic or workspace. Which namespaces covered, which empty, gap analysis, commitment readiness. DISPLAY ONLY."
allowed-tools: [Read, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /tools-coverage for: {{topic}} (or workspace if no topic given).

Show Signal coverage statistics -- which namespaces have been covered and which are missing.

DISPLAY ONLY -- no file written.

---

## STEP 1: SCAN

Glob: signals/**/{topic}-*-*.md (if topic given)
Glob: signals/**/*-*-*.md (if no topic -- workspace view)

Group artifacts by namespace:
  discover, specify, validate, simulate, prove, listen, rhythm, roles, topic

Count: artifacts per namespace, unique skills run, date range.

---

## STEP 2: COVERAGE TABLE

```
SIGNAL COVERAGE: {topic or "workspace"}
=========================================
Namespace     | Skills run | Artifacts | Last run   | Status
--------------|------------|-----------|------------|--------
discover      | N          | N         | YYYY-MM-DD | COVERED / EMPTY
specify       | N          | N         | YYYY-MM-DD | COVERED / EMPTY
validate      | N          | N         | YYYY-MM-DD | COVERED / EMPTY
simulate      | N          | N         | YYYY-MM-DD | COVERED / EMPTY
prove         | N          | N         | YYYY-MM-DD | COVERED / EMPTY
listen        | N          | N         | YYYY-MM-DD | COVERED / EMPTY
rhythm        | N          | N         | YYYY-MM-DD | COVERED / EMPTY
roles         | N          | N         | YYYY-MM-DD | COVERED / EMPTY
topic         | N          | N         | YYYY-MM-DD | COVERED / EMPTY

Total: N/9 namespaces covered | N skills run | N artifacts
```

---

## STEP 3: GAP ANALYSIS

For each EMPTY namespace, show the highest-value skill to run next:
```
COVERAGE GAPS:
  -> /discover-competitors {{topic}}    (inertia + competitive signal)
  -> /validate-design {{topic}}         (design review signal)
  ...
```

If all 9 covered: "Full coverage achieved for {{topic}}."

---

## STEP 4: COMMITMENT READINESS

```
Essential for commit (must have):
  [x] discover (competition + feasibility scoped)
  [ ] specify (spec written)
  [ ] validate (design reviewed)

Readiness: X/3 essential namespaces covered
```
