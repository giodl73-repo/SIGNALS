## Flow-Ratelimit R6 Scoring — Rubric v6

---

### V-01 Detailed Scoring

**Essential (5/5):**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Binding Constraint | PASS | Role 1 VERDICT requires binding constraint with number+unit and one causal sentence explaining why this limit binds before others |
| C-02 Causal Chain | PASS | Role 4 — directed hop chain `[Component]--[mechanism]-->[Component]--[mechanism]-->[effect]`, two hops minimum, named mechanisms |
| C-03 UX Differentiation | PASS | Role 8 — four-field template per throttle tier, minimum two tiers |
| C-04 Unprotected Burst Path | PASS | Role 5 — three-control checklist, STRUCTURAL vs INCIDENTAL classification with justification |
| C-05 Retry-After Gap Check | PASS | Role 6 — per-connector/HTTP-action evaluation, named failure modes from permitted set |

**Recommended (3/3):**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-06 Cascading Throttle | PASS | Role 7 — Tier 1 causes Tier 2, explicit causal link, numeric compounding effect required |
| C-07 Numeric Rate Limits | PASS | Role 3 registry requires number+unit for every component |
| C-08 Volume-to-Behavior Map | PASS | Role 9 — Volume map 1x/2x/5x with FORMAT CONTRACT five-column schema |

**Aspirational (14/15 pass, C-22 PARTIAL):**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09 Per-bottleneck Mitigations | PASS | Role 10 — exact action/setting/parameter named per row; generic advice fails |
| C-10 Quantified Impact | PASS | Role 9 5x cell — five-step arithmetic with Role 3 operands required |
| C-11 Burst Gap Classification | PASS | Role 5 — STRUCTURAL vs INCIDENTAL with justification per path |
| C-12 Dual-state Volume Mapping | PASS | Role 9 — BASELINE/PROTECTED dual columns per volume band |
| C-13 Verdict-before-Evidence | PASS | Role 1 VERDICT block before any inventory, burst audit, or volume table |
| C-14 Baseline-delta Mitigation | PASS | Role 10 — BASELINE names current behavior at component; PROTECTED names exact control changed |
| C-15 Document-head Global Verdict | PASS | Role 1 writes self-contained VERDICT with all three fields before Role 2 Format Contract |
| C-16 Format Contract Preamble | PASS | Role 2 FORMAT CONTRACT with three rejection clauses, scenario-specific BASELINE/PROTECTED definitions, two compliant tables (Roles 9 and 10) |
| C-17 Cascading Section Gates | PASS | All nine analysis-body transitions (Roles 3–11) gated with named deliverables from prior role |
| C-18 Bidirectional Verdict Revision | PASS | Roles 3, 5, 6 gates instruct REVISED marker insertion before proceeding; Role 11 reconciler scans for missing markers |
| C-19 Four-Field UX Template | PASS | Role 8 — labeled fields (a)–(d) per tier, prose without template fails |
| C-20 Arithmetic Trace Explicitness | PASS | Role 9 — five-step chain with Role 3 operands in cell; conclusion-only fails Rejection Clause B |
| C-21 Full Gate Chain Closure | PASS | All 9 analysis-body transitions gated; zero ungated boundaries |
| C-22 Gate-checkpoint Verdict Currency | PARTIAL | Currency checks at Roles 3, 5, 6 gates only (3 of 9 transitions); Roles 4, 7, 8, 9, 10 gates do not include explicit currency instructions; terminal Role 11 reconciler present. C-22 requires "each gated transition" — only 3/9 covered. Not sole-terminal (qualifies C-18), but fails the "each" requirement. |
| C-23 Schema-column Arithmetic Enforcement | PASS | Rejection Clause C declares DERIVATION CHAIN column as mandatory structural column (scan-visible schema violation if absent); two tables (Role 9, Role 10) must include column with populated cells |

**V-01 Composite: 60 + 30 + (14/15 × 30) = 60 + 30 + 28 = 118**

---

### V-02 Detailed Scoring

**Essential (5/5):** All pass — VERDICT preamble, causal chain, UX tiers, burst path, retry-after all present.

**Recommended (3/3):** All pass — cascade, numeric limits, volume map.

**Aspirational (12/15):**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09–C-16 | PASS | Format Contract preamble (C-16): STRUCTURAL REJECTION CLAUSE + CONTENT REJECTION CLAUSE, four-column schema declared as document-wide standard, scenario-specific BASELINE/PROTECTED |
| C-17 Cascading Section Gates | FAIL | Only PREAMBLE 1 and PREAMBLE 2 have explicit "do not write X until" gates; Sections 1–8 lack gate language — Section 1 instructs revision if needed but issues no blocking gate condition |
| C-18 Bidirectional Verdict Revision | PASS | Sections 1, 3, 6 instruct `[REVISED — see Section N]` marker insertion; final "After Section 8: verify each VERDICT claim" provides backup check |
| C-19 Four-Field Template | PASS | Section 4 — four-field template per tier |
| C-20 Arithmetic Explicitness | PASS | Section 5 — five-step template for 5x cell, each step references Section 1 value |
| C-21 Full Gate Chain Closure | FAIL | Requires C-17 PASS; C-17 fails → C-21 fails |
| C-22 Gate-checkpoint Currency | FAIL | Requires C-17 and C-18; C-17 fails → C-22 fails |
| C-23 Schema-column Enforcement | PASS | DERIVATION CHAIN declared as named 4th column in schema line with dedicated STRUCTURAL REJECTION CLAUSE; two tables (Sections 5, 7) must comply |

**V-02 Composite: 60 + 30 + (12/15 × 30) = 60 + 30 + 24 = 114**

---

### V-03 Detailed Scoring

**Essential (5/5):** All pass.

**Recommended (3/3):** All pass.

**Aspirational (10/15):**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09–C-15 | PASS | VERDICT-first, per-bottleneck mitigations, dual-state map in Section 5, four-field UX template, arithmetic trace |
| C-16 Format Contract Preamble | FAIL | No document-head Format Contract preamble; BASELINE/PROTECTED definitions appear at Section 5 only, not as a global declaration before Section 1. Imperative per-section commands replace the preamble. C-16 requires "placed before the first analysis section" |
| C-17 Cascading Section Gates | FAIL | No gate chain; per-section imperative commands govern local compliance only |
| C-18 Bidirectional Verdict Revision | PASS | Sections 1, 3, 6 instruct `[REVISED — see Section N]` marker; terminal scan "After Section 8" included |
| C-19 Four-Field Template | PASS | Section 4 — template structure mandatory |
| C-20 Arithmetic Explicitness | PASS | Section 5 — five-step chain template, "stating only the result is incomplete" |
| C-21 Full Gate Chain Closure | FAIL | Requires C-17; fails |
| C-22 Gate-checkpoint Currency | FAIL | Requires C-17; fails |
| C-23 Schema-column Enforcement | FAIL | Requires C-16; fails |

**V-03 Composite: 60 + 30 + (10/15 × 30) = 60 + 30 + 20 = 110**

---

### V-04 Detailed Scoring

**Essential (5/5):** All pass.

**Recommended (3/3):** All pass.

**Aspirational (14/15, C-22 PARTIAL):**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09–C-21 | PASS | Full gate chain on all 8 analysis-body transitions (Roles 3–10); FORMAT CONTRACT with schema-column schema + two rejection clauses; all structural requirements met |
| C-22 Gate-checkpoint Currency | PARTIAL | Currency checks at Roles 3, 5, 6, 9 gates (4 of 8 analysis transitions); Roles 4, 7, 8, 10 gates lack currency instructions. Stronger than V-01 (4/8 vs 3/9), but "each gated transition" requirement not fully satisfied. |
| C-23 Schema-column Enforcement | PASS | FORMAT CONTRACT declares DERIVATION CHAIN as mandatory column in four-column schema; two rejection clauses (structural + content); Roles 9 and 10 must include compliant tables |

**V-04 Composite: 60 + 30 + (14/15 × 30) = 60 + 30 + 28 = 118**

---

### V-05 Detailed Scoring

**Essential (5/5):** All pass.

**Recommended (3/3):** All pass.

**Aspirational (15/15):**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09–C-21 | PASS | Full ten-role gate chain with INERTIA-framed BASELINE, FORMAT CONTRACT four-column schema with INERTIA/PROTECTED/DERIVATION CHAIN, per-section COLUMN COMPLIANCE annotations, all structural gates present |
| C-22 Gate-checkpoint Currency | PASS | **Every single role gate (Roles 1–10) includes an explicit Verdict-currency instruction** — "Verdict-currency check: does Role N revise...? If yes: insert `[REVISED — see Role N]` now, before proceeding to Role N+1." Zero deferred revisions. Terminal reconciliation verifies only that gate-boundary markers were inserted — not the sole mechanism. Fully satisfies "each gated transition" |
| C-23 Schema-column Enforcement | PASS | FORMAT CONTRACT declares DERIVATION CHAIN as mandatory 4th column; SCHEMA REJECTION CLAUSE names it specifically; INERTIA-delta rule adds an additional analytical requirement to DERIVATION CHAIN cells in mitigation table; Roles 9 and 10 tables must comply |

**V-05 Composite: 60 + 30 + (15/15 × 30) = 60 + 30 + 30 = 120**

---

### Ranking

| Rank | Variation | Composite | All Essential | Notes |
|------|-----------|-----------|---------------|-------|
| **1** | **V-05** | **120** | Yes | Only variation with full C-22 pass; INERTIA framing + per-role column-compliance annotations |
| 2 | V-01 | 118 | Yes | C-22 PARTIAL — currency checks at 3 of 9 analysis transitions |
| 2 | V-04 | 118 | Yes | C-22 PARTIAL — currency checks at 4 of 8 analysis transitions |
| 4 | V-02 | 114 | Yes | No gate chain beyond preambles; C-17/C-21/C-22 fail |
| 5 | V-03 | 110 | Yes | No Format Contract preamble; C-16/C-23 fail; gate chain absent |

---

### Excellence Signals from V-05 Not Yet Encoded

**Signal 1 — INERTIA-delta rule as a DERIVATION CHAIN analytical requirement**

V-05 introduces the INERTIA-delta rule: every DERIVATION CHAIN cell in the mitigation table must show the delta *from* the INERTIA arithmetic — not merely the protected-state arithmetic in isolation. The derivation chain becomes a competitive proof: show the INERTIA failure rate, then show the PROTECTED failure rate, then show the delta proves the mitigation beats the status-quo competitor. C-23 requires DERIVATION CHAIN cells to contain step-by-step computation steps. The INERTIA-delta rule adds a second-order analytical requirement: the derivation must *prove improvement* over the inertia baseline, not merely demonstrate the protected state's arithmetic. This makes the mitigation table a competitive analysis, not an arithmetic display.

**Signal 2 — Per-role column-compliance annotations (explicit exemption declarations)**

V-05 introduces `COLUMN COMPLIANCE:` annotations at each role header that explicitly declare whether the DERIVATION CHAIN column is required or exempt for that role's output type (e.g., "COLUMN COMPLIANCE: Directed hop chain — no table. DERIVATION CHAIN not required in this role." vs "COLUMN REQUIRED: DERIVATION CHAIN"). This prevents the Format Contract's structural rejection clause from generating false violations against roles that produce hop chains, prose scenarios, or ordered lists rather than comparative tables. No existing criterion requires this; C-23 says "every comparative table containing quantified estimates" must have the column, but leaves ambiguous which sections produce such tables. The per-role annotation resolves that ambiguity locally, making schema compliance assessable without re-reading the Format Contract's scope definition.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["INERTIA-delta rule: DERIVATION CHAIN cells in the mitigation table must show arithmetic delta from the INERTIA state (prove the mitigation beats the status-quo competitor), not merely the protected-state arithmetic in isolation — making the derivation column a competitive proof, not just an arithmetic display", "Per-role column-compliance annotations: each role header explicitly declares whether the DERIVATION CHAIN column is required or exempt for that role's output type, preventing false schema violations against roles producing hop chains, prose scenarios, or ordered lists rather than comparative tables"]}
```
