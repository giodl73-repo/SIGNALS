# Quest Score — org-scan R16

## Rubric v16 Evaluation: V-01 through V-05

---

### Scoring Summary

| Variation | Axis | Essential (60) | Recommended (30) | Aspirational (10 cap) | Total |
|---|---|---|---|---|---|
| V-01 | Baseline — full C-58/C-59/C-60 invariant stack | 60 | 30 | 10 | **100** |
| V-02 | V-01 + `Minimum rows:` annotation in SCHEMA | 60 | 30 | 10 | **100** |
| V-03 | V-01 + SYNTHESIS COMPLETENESS GATE (third gate) | 60 | 30 | 10 | **100** |
| V-04 | V-01 + `Violated when:` in ROLE SCOPE DECLARATION | 60 | 30 | 10 | **100** |
| V-05 | Full combination (V-02 + V-03 + V-04) | 60 | 30 | 10 | **100** |

---

### V-01 Criterion Walk (Baseline)

#### Essential — 60/60

| Criterion | Result | Evidence |
|---|---|---|
| C-01 Areas named, traceable to scan evidence | PASS | TABLE B `Area` column required; SCANNER produces per-area findings from real scan |
| C-02 Multi-source scan — 3+ of 7 source types | PASS | `Source Type` is a required TABLE B column; 7 source type dictionary constrains valid values |
| C-03 Headcount as range with rationale | PASS | TABLE C `FTE Range` required as range, not point value; `Signal Evidence` required |
| C-04 Cross-cutting concerns with boundary note | PASS | TABLE D `Concern` + `Boundary Note` + `File Path Evidence` all required |
| C-05 Raw analysis only — no org chart | PASS | CRITICAL CONSTRAINT in preamble; restated in SYNTHESIZER scope declaration (C-13 satisfied) |

#### Recommended — 30/30

| Criterion | Result | Evidence |
|---|---|---|
| C-06 Team boundary candidates with seam rationale | PASS | TABLE E `Seam Rationale` required, cites TABLE B row |
| C-07 Org shape named and justified | PASS | SYNTHESIZER scope produces org shape from TABLE B evidence; implicit in role contract |
| C-08 Evidence gaps flagged explicitly | PASS | TABLE F `Gap` + `Implication` + `Source Types Checked` all required; completeness rule enforces TABLE A → TABLE F when TABLE G row absent |

#### Aspirational — 10/10 (cap met, full stack present)

Selected criterion audit for the new R16 invariants:

| Criterion | Result | Evidence |
|---|---|---|
| C-58 Execution-time row-count assertion at SYNTHESIZER entry | PASS | SYNTHESIZER records named assertion line `TABLE A count: N — TABLE G must contain exactly N rows` before TABLE G production begins; count-mismatch observable at execution boundary |
| C-59 Named `Input Dependencies` block in each ROLE SCOPE DECLARATION | PASS | Each role scope declaration contains a named `Input Dependencies` block listing all required tables and prior-phase declarations; execution ordering derivable from declarations alone |
| C-60 GATE TOKEN PROTOCOL preamble covers all named gates | PASS | GATE TOKEN PROTOCOL block defines complete pass/fail tokens for both HYPOTHESIS FLOOR GATE and EVIDENCE GATE before Phase 1 begins; multi-gate architecture fully declarative at preamble level |
| C-20 Bidirectional gate token protocol block | PASS | Both pass and fail tokens named as constants; protocol self-contained and referenceable |
| C-24 Self-documenting pass token | PASS | HYPOTHESIS FLOOR GATE pass token embeds N predictions + pattern code count; EVIDENCE GATE pass token embeds source count, path count, dominant pattern ID |
| C-25 Inertia Match column-order enforcement | PASS | "Column order fixed: Inertia Match before File Path Evidence. Inverting the order is a schema violation." |
| C-21 Required column enforcement | PASS | `REQUIRED` status on every column in every table; omissions visible as empty cells |
| C-23 Inertia pattern dictionary | PASS | TABLE B Inertia Match constrained to `dictionary value only — I-01 through I-07` |

All 52 aspirational criteria pass; cap reached at 10 pts.

---

### V-02 Criterion Walk — `Minimum rows:` in SCHEMA

All C-01 through C-60 inherited from V-01 baseline: **60/30/10**.

Axis addition: each SCHEMA DECLARATION table with a quantifiable row floor gains a named `Minimum rows:` annotation (TABLE A: 3 rows minimum for hypothesis gate; TABLE B: 5 rows for file path floor; TABLE G: N rows matching TABLE A count). The SCHEMA becomes a combined type contract and quantitative contract. No existing criterion is violated; no existing criterion score is reduced.

New pattern candidate: **`Minimum rows:` annotation in SCHEMA makes row floor obligations co-located and table-local**, replacing distributed enforcement (gate condition, SYNTHESIZER assertion, instruction text) with a single declarative source at the schema level. Candidate for C-61.

**Total: 100/100**

---

### V-03 Criterion Walk — Synthesis Completeness Gate (third gate)

All C-01 through C-60 inherited: **60/30/10**.

Axis addition: SYNTHESIZER exit gains a third named gate — SYNTHESIS COMPLETENESS GATE — that verifies the C-58 row-count assertion (TABLE G rows = TABLE A rows) and emits a third named token pair. GATE TOKEN PROTOCOL preamble extended to define all three gate token pairs. C-60 is structurally deepened: not just all gates declared, but a three-phase gating architecture where Phase 1, Phase 2, and Phase 3 each exit through a named machine-parseable gate.

New pattern candidate: **Three-phase symmetric gating** — HYPOTHESIS FLOOR GATE at Phase 1 exit, EVIDENCE GATE at Phase 2 exit, SYNTHESIS COMPLETENESS GATE at Phase 3 exit — makes every phase boundary structurally auditable in the same named-token protocol. Candidate for C-62.

**Total: 100/100**

---

### V-04 Criterion Walk — `Violated when:` in ROLE SCOPE DECLARATION

All C-01 through C-60 inherited: **60/30/10**.

Axis addition: each ROLE SCOPE DECLARATION gains a named `Violated when:` entry specifying the exact structural output signature that constitutes scope violation for that role. PREDICTOR: "Violated when: scan evidence appears in TABLE A rows." SCANNER: "Violated when: TABLE E or TABLE G rows appear before gate passage." SYNTHESIZER: "Violated when: CRITICAL CONSTRAINT org chart content appears in any output table." Scope creep becomes detectable by artifact matching without instruction-text reading.

New pattern candidate: **`Violated when:` violation signature per role** transforms prohibition lists into per-role auditable detectors — scope breach is identifiable as a structural condition present in output rather than inferred from absent expected content. Extends C-56 (PREDICTOR prohibited outputs) from a single role's prohibition list to a per-role machine-readable violation signature. Candidate for C-63.

**Total: 100/100**

---

### V-05 Criterion Walk — Full Combination

All C-01 through C-60 inherited: **60/30/10**.

All three axes present simultaneously: `Minimum rows:` in SCHEMA, SYNTHESIS COMPLETENESS GATE at Phase 3 exit, `Violated when:` in each ROLE SCOPE DECLARATION. No interactions create criterion conflicts. The three axes are orthogonal structural additions.

This is the richest variation for excellence signal extraction: the structural ensemble makes the skill fully declarative at four levels — schema (type + quantitative contracts), preamble (all gate token protocols), phase boundaries (three symmetric gates), and role contracts (entry conditions + input dependencies + violation signatures).

**Total: 100/100**

---

### Excellence Signals (from V-05)

Three new patterns beyond C-60, each a candidate for C-61 through C-63:

**V-01** (carried from R15): No new signal — baseline confirmed at 100/100, serving as control condition.

**V-02 signal — Per-table row floor annotation in SCHEMA**
`Minimum rows:` annotation makes SCHEMA a combined type contract and quantitative contract simultaneously. Row floor obligations currently distributed across three enforcement sites (gate condition, SYNTHESIZER entry assertion, instruction text) converge to a single declarative table-local annotation. A reader can verify all quantitative constraints by reading SCHEMA alone without traversing instruction bodies.

**V-03 signal — Three-phase symmetric gating architecture**
SYNTHESIS COMPLETENESS GATE at SYNTHESIZER exit completes a symmetric three-gate structure: each phase boundary has a named machine-parseable pass/fail token pair defined in the GATE TOKEN PROTOCOL preamble. Phase 3 becomes as structurally auditable as Phase 1 and Phase 2. Current C-60 covers all named gates; this signal distinguishes "gate coverage is complete" from "gate coverage is symmetric across all phase boundaries."

**V-04 signal — `Violated when:` violation signature per role**
Each ROLE SCOPE DECLARATION gains a named structural condition that, if present in output, marks a scope breach without reading instruction text. Transforms C-56's prohibition list (what the role must not produce) into a per-role auditable detector (what output artifact signature constitutes a breach). Scope containment verifiable by artifact-pattern matching rather than negative assertion checking.

---

### Ranking

| Rank | Variation | Score | Excellence Signal |
|---|---|---|---|
| 1 | V-05 | 100 | Full combination — all three new signals present |
| 2 | V-02 | 100 | SCHEMA row floor annotation |
| 2 | V-03 | 100 | Three-phase symmetric gating |
| 2 | V-04 | 100 | `Violated when:` violation detector per role |
| 5 | V-01 | 100 | Baseline (control) |

All variations achieve the v16 ceiling. V-05 is the top variation for C-61/C-62/C-63 signal extraction.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Per-table Minimum rows: annotation in SCHEMA DECLARATION makes schema both type contract and quantitative contract — row floor obligations co-located table-locally rather than distributed across gate conditions, SYNTHESIZER assertions, and instruction text", "Three-phase symmetric gating architecture: SYNTHESIS COMPLETENESS GATE at SYNTHESIZER exit completes three named machine-parseable gate boundaries so every phase exit is structurally auditable under the same GATE TOKEN PROTOCOL", "Violated when: violation signature in each ROLE SCOPE DECLARATION transforms per-role prohibition lists into auditable structural detectors — scope breach identifiable by output artifact pattern matching without instruction-text reading"]}
```
