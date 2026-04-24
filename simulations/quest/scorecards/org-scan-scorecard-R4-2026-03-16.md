# org-scan Round 4 — Quest Score

## Rubric: v4 | Variations: V-01 through V-05

---

## V-01 — Single-axis: C-17 (GATE-PASS-TOKEN Protocol Block)

**Axis**: Extract pass-token format into named `GATE-PASS-TOKEN:` constant; C-18 deliberately omitted.

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Areas named and traceable | Essential | PASS | A.1 with anti-fab: "Only name areas you can trace to a Phase 1 finding. Every area must have a cited source." |
| C-02 Multi-source scan (3+ of 7) | Essential | PASS | All 7 source types enumerated in Phase 1 |
| C-03 Headcount as range with rationale | Essential | PASS | A.3 requires explicit derivation chain; round numbers without evidence chain explicitly fail |
| C-04 Cross-cutting concerns with boundary note | Essential | PASS | A.2 requires "why ownership cannot be localized" per concern |
| C-05 Raw analysis only — no org chart | Essential | PASS | Critical constraint stated in preamble with "(stated here and repeated in the output format below)" |
| C-06 Team boundary candidates with seam rationale | Recommended | PASS | B.1 requires coupling risk (Low/Med/High) with note per seam |
| C-07 Org shape named and justified | Recommended | PASS | B.2 names shape options and requires Group A citation |
| C-08 Evidence gaps flagged explicitly | Recommended | PASS | Dedicated Evidence Gaps section at end |
| C-09 5+ file paths cited | Aspirational | PASS | Path floor gate: "At least 5 distinct file paths cited across all sources" |
| C-10 Current vs recommended separated | Aspirational | PASS | GROUP A / GROUP B named structural headers |
| C-11 Anti-fabrication language per evidence-dependent section | Aspirational | PASS | Embedded in A.1, A.2, A.3, B.1, B.2 — every section carries its own note |
| C-12 Hard sequencing gate | Aspirational | PASS | "Do not write a single word of Group A until the GATE-PASS-TOKEN is written" |
| C-13 Critical constraint stated twice | Aspirational | PASS | Preamble + "(stated here and repeated in the output format below)" |
| C-14 Verification checklist at gate | Aspirational | PASS | 5 numbered items + mandatory GATE-PASS-TOKEN write before Group A |
| C-15 Structural group labels | Aspirational | PASS | GROUP A / GROUP B as discrete named groups, not section headings within a flow |
| C-16 File path floor as gate condition | Aspirational | PASS | Item 4 is a proceed-or-stop condition: shortfall must be recorded before proceeding |
| C-17 Gate confirmation token (named-token format) | Aspirational | **PASS** | `GATE-PASS-TOKEN:` defined as named constant in preamble — structural, not incidental |
| C-18 Gate failure output (named fail string) | Aspirational | **FAIL** | Item 4 says "record the shortfall before proceeding" — no named fail string; deliberately omitted to isolate axis |

**Aspirational passing**: C-09 through C-17 = 9 criteria × 2 = 18 pts → capped at **10**

```
composite = (5/5 × 60) + (3/3 × 30) + 10 = 60 + 30 + 10 = 100
```

**Score: 100** | Essential: 5/5 | Recommended: 3/3 | Aspirational: 9/10 (capped at 10)

---

## V-02 — Single-axis: C-18 (Gate Failure Output)

**Axis**: V-05/R3 base + item 4 adds `If fewer than 5 paths: write \`Path floor not met\` and stop`; C-17 inherited.

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01 through C-05 | Essential | PASS × 5 | Inherited from V-05/R3 base — areas traceable, 7 sources, headcount derivation, concerns with ownership note, no org chart |
| C-06 through C-08 | Recommended | PASS × 3 | Inherited — seam rationale, org shape justification, evidence gaps section |
| C-09 through C-16 | Aspirational | PASS × 8 | Inherited — paths, GROUP separation, anti-fab per section, hard gate, constraint×2, checklist, group labels, floor-as-gate |
| C-17 Gate confirmation token | Aspirational | PASS | V-05/R3 had "Gate clear — ..." as confirmation sentence; named-token format inherited |
| C-18 Gate failure output | Aspirational | **PASS** | Item 4: `If fewer than 5 paths: write \`Path floor not met\` and stop` — exact named string, machine-parseable without prose inspection |

**Aspirational passing**: C-09 through C-18 = 10 × 2 = 20 pts → capped at **10**

```
composite = 60 + 30 + 10 = 100
```

**Score: 100** | Essential: 5/5 | Recommended: 3/3 | Aspirational: 10/10 (capped at 10)

---

## V-03 — Output Format: Table-Driven + Inertia Column

**Axis**: Replace prose scan log with evidence table; Inertia Match column per row; tables throughout.

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01 through C-05 | Essential | PASS × 5 | Table rows carry per-area evidence citations; source-type table covers all 7; headcount row requires derivation; concerns table includes ownership span; no-org-chart constraint stated |
| C-06 through C-08 | Recommended | PASS × 3 | Seam table with coupling-risk column; org shape row with Group A citation reference; evidence gaps as table rows |
| C-09 File paths 5+ | Aspirational | PASS | Path column in scan table; floor gate enforced |
| C-10 Current vs recommended separated | Aspirational | PASS | GROUP A / GROUP B table sections |
| C-11 Anti-fabrication per section | Aspirational | PASS | Column header or row note anchors each table to Phase 1 |
| C-12 Hard sequencing gate | Aspirational | PASS | Gate table with mandatory token row before Group A |
| C-13 Critical constraint ×2 | Aspirational | PASS | Preamble + column header in output table |
| C-14 Verification checklist at gate | Aspirational | PASS | Gate checklist as numbered table rows + confirmation token row |
| C-15 Structural group labels | Aspirational | PASS | GROUP A / GROUP B as named table-group headers |
| C-16 File path floor as gate condition | Aspirational | PASS | Gate table item 4: proceed-or-stop condition |
| C-17 Gate confirmation token | Aspirational | PASS | Named-token format written as gate table confirmation row |
| C-18 Gate failure output | Aspirational | PASS | Fail string `Path floor not met` in item 4 of gate table |

**Aspirational passing**: 10/10 × 2 = 20 → capped at **10**

```
composite = 60 + 30 + 10 = 100
```

**Score: 100** | Essential: 5/5 | Recommended: 3/3 | Aspirational: 10/10 (capped at 10)

**Structural note**: Inertia Match column is a new per-row evidence discipline not captured in any current criterion. Flagged for v5.

---

## V-04 — Bidirectional Gate Tokens (GATE TOKEN PROTOCOL block)

**Axis**: Named `GATE TOKEN PROTOCOL` preamble block defines both pass token and fail token as named constants before Phase 1.

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01 through C-05 | Essential | PASS × 5 | All five essential properties inherited; critical constraint appears in preamble and output format |
| C-06 through C-08 | Recommended | PASS × 3 | All three recommended properties inherited |
| C-09 through C-16 | Aspirational | PASS × 8 | All eight inherited aspirational criteria pass |
| C-17 Gate confirmation token | Aspirational | **PASS** | Pass token defined as named constant in GATE TOKEN PROTOCOL block — more structural than V-01 (which embedded the format in preamble prose); constant is referenced by name at the gate |
| C-18 Gate failure output | Aspirational | **PASS** | Fail token defined as named constant in same GATE TOKEN PROTOCOL block — both directions machine-parseable by name lookup, not prose inspection |

**Aspirational passing**: 10/10 × 2 = 20 → capped at **10**

```
composite = 60 + 30 + 10 = 100
```

**Score: 100** | Essential: 5/5 | Recommended: 3/3 | Aspirational: 10/10 (capped at 10)

**Structural note**: Defining both gate directions as named constants in a single protocol block — rather than embedding them in gate instructions — is a pattern not yet captured as a criterion. The block makes gate token completeness structurally verifiable (both constants present or absent) rather than requiring per-instruction inspection. Flagged for v5.

---

## V-05 — Full Integration (All 10 Aspirational + B.2 Anti-Fab)

**Axis**: V-05/R3 base + GATE TOKEN PROTOCOL block + explicit fail token + B.2 anti-fabrication note.

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01 through C-05 | Essential | PASS × 5 | All essential criteria from V-05/R3 base; C-05 critical constraint stated in preamble and output format |
| C-06 through C-08 | Recommended | PASS × 3 | All recommended criteria; B.2 now carries explicit anti-fab note matching depth of B.1 |
| C-09 through C-16 | Aspirational | PASS × 8 | All inherited; C-16 path floor gate in item 4 |
| C-17 Gate confirmation token | Aspirational | PASS | Pass token defined as structural constant in GATE TOKEN PROTOCOL block |
| C-18 Gate failure output | Aspirational | PASS | Fail token defined as structural constant in same block + item 4 write instruction |

**Aspirational passing**: 10/10 × 2 = 20 → capped at **10**

```
composite = 60 + 30 + 10 = 100
```

**Score: 100** | Essential: 5/5 | Recommended: 3/3 | Aspirational: 10/10 (capped at 10)

**R3 Signal 1 gap closed**: B.2 now reads "The org shape recommendation is as evidence-dependent as the seam candidates" — anti-fabrication note in B.2 matches depth of B.1. This closes the gap the R3 scorecard identified. Not yet a criterion.

---

## Composite Summary

| Variation | Essential | Recommended | Aspirational (raw) | Aspirational (capped) | Composite | Golden? |
|-----------|-----------|-------------|--------------------|-----------------------|-----------|---------|
| V-01 | 5/5 (60) | 3/3 (30) | 18 | 10 | **100** | YES |
| V-02 | 5/5 (60) | 3/3 (30) | 20 | 10 | **100** | YES |
| V-03 | 5/5 (60) | 3/3 (30) | 20 | 10 | **100** | YES |
| V-04 | 5/5 (60) | 3/3 (30) | 20 | 10 | **100** | YES |
| V-05 | 5/5 (60) | 3/3 (30) | 20 | 10 | **100** | YES |

All five are golden at 100. Ranking by structural quality (not score):

1. **V-04 / V-05** — GATE TOKEN PROTOCOL block defines both tokens as named constants; both gate directions are structurally verifiable by block presence, not instruction-text inspection. V-05 additionally closes the R3 B.2 gap.
2. **V-02 / V-03** — Both achieve 10/10 aspirational; V-03 adds inertia-column discipline as a new structural layer.
3. **V-01** — 9/10 aspirational (C-18 deliberately absent); still caps at 100 but structurally incomplete on gate failure.

---

## Excellence Signals

**From top-scoring variations (V-04 / V-05)**:

**Named protocol block as structural anchor** (V-04): Both gate tokens defined once in a `GATE TOKEN PROTOCOL` preamble block, then referenced by name at the gate. The block's presence or absence is structurally detectable — no prose inspection required to verify completeness. This is stronger than V-01's embedded preamble definition (also structural but single-directional).

**B.2 anti-fabrication at B.1 depth** (V-05): Every evidence-dependent section carries an anti-fabrication note. B.2 previously lacked one, making the org shape recommendation structurally weaker than B.1's seam candidates. V-05 closes this asymmetry. When a skill has anti-fab in some sections but not others, the sections without it are the failure points.

**C-17 vs. incidental token**: V-05/R3 had "Gate clear — ..." embedded in gate text — C-17 passed incidentally. V-01 and V-04 make it a named constant defined before Phase 1. The distinction: incidental satisfies the criterion but doesn't prevent drift; a named constant makes deviation structurally detectable.

**Per-row evidence discipline** (V-03): Table format with an Inertia Match column enforces per-claim traceability at the cell level. Every row either carries evidence or it visibly doesn't — no prose can hide a gap. This is a stronger structural guarantee than anti-fabrication prose notes, which require reading and judgment.

---

## New Patterns for v5

Two patterns appear in R4 that are not yet captured as rubric criteria:

1. **GATE TOKEN PROTOCOL as named preamble block**: Defining both pass and fail tokens as named constants in a single block before Phase 1 — not embedding them in gate instructions. The block makes gate token completeness verifiable by block inspection (both constants present or absent) rather than per-instruction text search. V-04 and V-05 demonstrate this.

2. **Symmetric anti-fabrication coverage**: Every evidence-dependent section in the output carries an anti-fabrication note at equal depth. V-05 demonstrates this by closing the B.2 gap — when some sections have anti-fab and others don't, the uncovered sections are the structural weak points. A criterion requiring symmetric coverage across all output sections (not just the ones that happen to have it) would make this gap detectable.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["GATE TOKEN PROTOCOL as named preamble block defining both pass and fail tokens as named constants — gate completeness verifiable by block presence, not instruction-text inspection", "Symmetric anti-fabrication coverage — every evidence-dependent output section carries an anti-fabrication note at equal depth; asymmetric coverage (B.1 has it, B.2 does not) creates structurally detectable weak points"]}
```
