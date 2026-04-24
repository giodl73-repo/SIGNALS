Written to `simulations/quest/golden/flow-ratelimit-variate-R14-2026-03-17.md`.

---

# flow-ratelimit — Variate R14

**Rubric:** v14 (C-01 through C-35, 27 aspirational) | **Max composite:** 120/120

## State analysis

R12 V-05 under v14 misses two criteria:
- **C-34** (BORDERLINE FAIL) — zero-count declaration absent from check (a); three behavioral declarations are not all explicitly produced
- **C-35** (FAIL) — no named invariant before the reconciler opens; check (a) self-asserts rather than confirming a pre-declared rule

## Variation map

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Axis | Role sequence (baseline carry) | Lifecycle emphasis | Output format | Role sequence + output format | Full integration |
| NMI position | none | inside Role 10 body | standalone pre-terminal section | standalone pre-terminal section | standalone pre-terminal section |
| Explicit 3 declarations in check (a) | implicit | yes | implicit | yes | yes |
| Check (a) names NMI-01 | no | yes | no | yes | yes |
| Gate 9→NMI requires NMI-01 deliverable | no | no | no | no | yes |
| C-34 | borderline FAIL | PASS | borderline FAIL | PASS | PASS |
| C-35 | FAIL | FAIL (inside body) | FAIL (no name ref) | PASS | PASS |
| Predicted composite | 118.89 | 118.89 | 118.89 | 120/120 | 120/120 |

## Single-axis questions

- **Q1 (V-01 vs V-02):** Do explicit three declarations in check (a) satisfy C-34 without any NMI? Hypothesis: yes — C-34 is about declarations from within the reconciler body, not about pre-declared constraints.
- **Q2 (V-02 vs V-04):** Does NMI position (inside vs. before Role 10) determine C-35 compliance regardless of declaration quality? Hypothesis: yes — "inside the reconciler body" is an explicit exclusion.
- **Q3 (V-03 vs V-04):** Does the absence of "NMI-01" by name in check (a) alone cause C-35 failure when the NMI is correctly positioned? Hypothesis: yes — name reference in check (a) is an explicit pass condition.

## Structure by variation

- **V-01** — R12 V-05 carry, 11 roles, implicit declarations, no NMI
- **V-02** — NMI-01 block as first element inside Role 10 (after the header), explicit 3 declarations, name reference in check (a)
- **V-03** — Standalone `## PRE-TERMINAL INVARIANT — NMI-01` section between Role 9 and Role 10; check (a) uses generic "pure verification" language, no NMI-01 reference
- **V-04** — V-03 structure + explicit 3 declarations labeled (i)(ii)(iii) in check (a) + "referencing NMI-01" language
- **V-05** — V-04 + explicit `"deferred from Role N — [reason]"` annotation in Role 9 + Gate 9→NMI names NMI-01 as a deliverable by identifier
