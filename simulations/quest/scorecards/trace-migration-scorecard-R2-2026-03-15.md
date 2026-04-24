## trace-migration — Round 2 Scoring

**Rubric:** v2 (12 criteria, 110 pts max)
**Variations:** V-01 through V-05

---

## Per-Variation Evaluation

### V-01 — Phrasing Register

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Entity enumeration | **PASS** | ENTITY REGISTRY table precedes all content; gap rule states "omission is higher risk than false inclusion — mark uncertain entries POSSIBLE"; gap → HALT BLOCK before continuation |
| C-02 | Before/after state | **PASS** | Dedicated BEFORE STATE and AFTER STATE sections; after state explicitly "independently readable without reading BEFORE STATE" |
| C-03 | Named migration operations | **PASS** | DIRECTIVE 0 defines 20 approved verbs in enumerated table; one minimum per entity rule; disallowed phrase → enforcement flag required before entry counts |
| C-04 | Data loss paths | **PASS** | DATA LOSS PATHS section checks all five mechanisms; "If none: state 'No data loss paths identified.' Silence does not pass." |
| C-05 | Constraint violations | **PASS** | CONSTRAINT VIOLATIONS section; all four constraint types analyzed; "If no new constraints: state explicitly. Missing constraint analysis does not pass." |
| C-06 | Default value gap analysis | **PASS** | DEFAULT VALUE ANALYSIS section per entity; domain-correct semantics check included |
| C-07 | Performance cliff | **PASS** | PERFORMANCE CLIFF section; four high-risk operations named; LOW/MEDIUM/HIGH + mitigation required |
| C-08 | Reversibility | **PASS** | REVERSIBILITY verdict (REVERSIBLE / CONDITIONAL / IRREVERSIBLE) + rationale per entity |
| C-09 | Cross-entity cascade (≥2 traces) | **PASS** | DIRECTIVE D-1 states "section with one trace does not pass C-09"; DIRECTIVE D-2 cross-layer requirement explicitly separate |
| C-10 | Quantified risk scoring | **PASS** | RISK REGISTER with severity, likelihood, remediation — all three fields required per issue |
| C-11 | Vocabulary enforcement | **PASS** | DIRECTIVE 0: 20 approved verbs (table), 5 disallowed phrases with rejection form, enforcement format "[NON-COMPLIANT: 'X' is not an approved verb — use Y]" |
| C-12 | Halt-on-gap escalation | **PASS** | DIRECTIVE 1 HALT BLOCK FORM names gap condition, responsible role, acknowledgment gate; no-gap declaration required even when no gaps fire |

**Score: 110/110 — Golden**
All essential PASS + composite 110 ≥ 85.

---

### V-02 — Output Format

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Entity enumeration | **PASS** | TABLE 1 with Registry Status column (REGISTERED / GAP-DETECTED); TABLE 1-HALT fires on GAP-DETECTED; must be complete before TABLE 2 |
| C-02 | Before/after state | **PASS** | TABLE 2 one row per column/constraint; Before State: "name actual type and nullability — 'Existing state' does not pass"; After State: "independently readable" |
| C-03 | Named migration operations | **PASS** | TABLE 0 VOCABULARY CONTRACT precedes all; Migration Operation column in TABLE 2 must use TABLE 0 verbs; COMPLIANCE STATUS cell fires on violation |
| C-04 | Data loss paths | **PASS** | TABLE 3 with loss mechanism column (TYPE NARROWING / COLUMN DROP / LOSSY CAST / CASCADE DELETE / OVERWRITE BACKFILL); NONE row with reasoning required |
| C-05 | Constraint violations | **PASS** | TABLE 4 one row per new/tightened constraint; "If no new constraints: write NONE row per entity with reasoning" |
| C-06 | Default value gap analysis | **PASS** | TABLE 5 with "Semantically Correct?" and "Domain Concern" columns per row |
| C-07 | Performance cliff | **PASS** | TABLE 6 with Risk Level column; Scheduling Constraint column added beyond baseline requirement |
| C-08 | Reversibility | **PASS** | TABLE 7 one row per entity; Rollback Path + Residual Consequence columns beyond baseline |
| C-09 | Cross-entity cascade (≥2 traces) | **PASS** | TABLE 8 "Minimum two complete traces required. Single-trace sections do not pass C-09."; Impact Layer column separates schema vs. cross-layer |
| C-10 | Quantified risk scoring | **PASS** | TABLE 9 with Source Table column (TABLE 3/4/5/6/7/8) enabling bidirectional coverage verification |
| C-11 | Vocabulary enforcement | **PASS** | TABLE 0: 20 approved verbs, 5 disallowed phrases with rejection messages; COMPLIANCE STATUS column in TABLE 2 makes violations visible as malformed cells without prose re-reading |
| C-12 | Halt-on-gap escalation | **PASS** | TABLE 1-HALT mandatory form; all five required fields; no-gap declaration "NO GAPS DETECTED — signed by Operations" explicitly required |

**Score: 110/110 — Golden**
All essential PASS + composite 110 ≥ 85.

**Distinctive strength:** Compliance enforcement is embedded in the data structure itself. A TABLE 2 violation is a malformed cell, not missing prose — visible by column scan. TABLE 1-HALT adjacent to GAP-DETECTED makes gap-without-halt a visibly empty form cell.

---

### V-03 — Lifecycle Emphasis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Entity enumeration | **PASS** | Phase 1 ENTITY INVENTORY TABLE; Phase 1 GAP HALT GATE blocks Phase 2 if any entry has UNKNOWN change class |
| C-02 | Before/after state | **PASS** | Phase 2 per-entity BEFORE STATE documentation; Phase 2 GAP HALT GATE blocks Phase 3 if UNKNOWN fields remain |
| C-03 | Named migration operations | **PASS** | Phase 0-A VOCABULARY PROTOCOL with 20 approved verbs; Phase 3 VOCABULARY GATE scans every operation cell before phase closes |
| C-04 | Data loss paths | **PASS** | Phase 4 DATA LOSS ANALYSIS per entity; explicit "None" with reasoning required |
| C-05 | Constraint violations | **PASS** | Phase 4 CONSTRAINT VIOLATION ANALYSIS; "State explicitly if no new constraints" |
| C-06 | Default value gap analysis | **PASS** | Phase 4 DEFAULT VALUE ANALYSIS per entity with domain-correctness check |
| C-07 | Performance cliff | **PASS** | Phase 4 PERFORMANCE CLIFF; risk level + mitigation required for each high-risk operation |
| C-08 | Reversibility | **PASS** | Phase 4 REVERSIBILITY verdict + rationale per entity |
| C-09 | Cross-entity cascade (≥2 traces) | **PASS** | Phase 5: "minimum two complete cascade traces required — a Phase 5 section with one trace does not pass"; Phase 5 GAP HALT GATE verifies each trace has named mitigation |
| C-10 | Quantified risk scoring | **PASS** | Risk Register in Phase 5 with all three fields |
| C-11 | Vocabulary enforcement | **PASS** | Phase 0-A: 20 approved verbs listed, 5 disallowed phrases, enforcement example shown; Phase 3 VOCABULARY GATE as closing condition before phase advances |
| C-12 | Halt-on-gap escalation | **PASS** | Phase 0-B: HALT BLOCK FORM with all required fields; no-gap declaration required at Phase 0 initialization; phase gates at every boundary |

**Score: 110/110 — Golden**
All essential PASS + composite 110 ≥ 85.

**Distinctive strength:** Every phase boundary has both a VOCABULARY GATE and a GAP HALT GATE — skipping a gate is visible as a missing close condition, not missing prose. Phases cannot advance structurally without clearing both.

---

### V-04 — Role Sequence + Phrasing Register

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Entity enumeration | **PASS** | DIRECTIVE A: Operations runs first; entity registry is the contract; gap → DIRECTIVE 1 HALT BLOCK before proceeding |
| C-02 | Before/after state | **PASS** | DIRECTIVE B per entity: BEFORE STATE + AFTER STATE; "AFTER STATE: Full post-migration schema. Independently readable." |
| C-03 | Named migration operations | **PASS** | DIRECTIVE 0: 20 approved verbs (pipe-separated); disallowed phrases named with DIRECTIVE 0 VIOLATION enforcement tag per phrase |
| C-04 | Data loss paths | **PASS** | DIRECTIVE B: DATA LOSS PATHS; "Explicit 'none' with reasoning if not applicable" |
| C-05 | Constraint violations | **PASS** | DIRECTIVE B: CONSTRAINT VIOLATIONS; "Explicit 'none' if no new constraints" |
| C-06 | Default value gap analysis | **PASS** | DIRECTIVE B: DEFAULT VALUE ANALYSIS per entity |
| C-07 | Performance cliff | **PASS** | DIRECTIVE B: PERFORMANCE CLIFF; four high-risk operation types named; risk level + mitigation required |
| C-08 | Reversibility | **PASS** | DIRECTIVE B: REVERSIBILITY verdict + rationale |
| C-09 | Cross-entity cascade (≥2 traces) | **PASS** | DIRECTIVE D-1: "A section with one trace does not satisfy C-09"; DIRECTIVE D-2: cross-layer requirement as separate named directive |
| C-10 | Quantified risk scoring | **PASS** | DIRECTIVE E: RISK REGISTER; "An issue present in role analysis but absent from the register is a coverage gap — issue DIRECTIVE 1 HALT BLOCK" |
| C-11 | Vocabulary enforcement | **PASS** | DIRECTIVE 0: 20 approved verbs, 3 disallowed phrases (exactly at minimum), each with named DIRECTIVE 0 VIOLATION enforcement form |
| C-12 | Halt-on-gap escalation | **PASS** | DIRECTIVE 1: HALT BLOCK form with all required fields; no-gap declaration explicitly required form; four named gap conditions enumerated |

**Score: 110/110 — Golden**
All essential PASS + composite 110 ≥ 85.

**Note on C-11:** Disallowed phrases count is exactly 3 (minimum). Passes but narrower margin than V-01/V-02/V-03. Enforcement tags are per-phrase rather than per-table, which is strong for spot-checking individual violations.

---

### V-05 — Role Sequence + Output Format + Lifecycle Emphasis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Entity enumeration | **PASS** | Phase 1 ENTITY REGISTRY with Registry Completeness column; Operations-first; GAP-DETECTED → HALT PROTOCOL; Phase 1 gate verifies all COMPLETE before Phase 2 |
| C-02 | Before/after state | **PASS** | Phase 2 table format one row per column/constraint; Before State: "enumerate actual type and nullability — 'As-is' does not pass"; After State: "full definition, not just the delta" |
| C-03 | Named migration operations | **PASS** | VOCABULARY CONTRACT declared before analysis; Migration Operation column with Compliance column; NOT-APPROVED fires in cell |
| C-04 | Data loss paths | **PASS** | Phase 3 DATA LOSS per entity; five loss mechanism types listed; "If none: explicit 'None — [reasoning]'" |
| C-05 | Constraint violations | **PASS** | Phase 3 CONSTRAINT VIOLATION per entity; four constraint types; explicit "No new or tightened constraints" required |
| C-06 | Default value gap analysis | **PASS** | Phase 3 DEFAULT VALUE GAP with domain concern column; empty strings, zero on financial totals, sentinel values flagged |
| C-07 | Performance cliff | **PASS** | Phase 3 PERFORMANCE CLIFF; "Mitigation required for MEDIUM and HIGH" — strengthens baseline |
| C-08 | Reversibility | **PASS** | Phase 3 REVERSIBILITY with Rollback Path + Residual Consequence columns |
| C-09 | Cross-entity cascade (≥2 traces) | **PASS** | Phase 4 CASCADE TRACE TABLE "minimum two rows"; Phase 4 gate: "Verify cascade trace count >= 2 and at least one cross-layer trace present" as boolean gate condition |
| C-10 | Quantified risk scoring | **PASS** | Risk Register in Phase 4 with Source Phase column; "All Phase 3 severity >= MEDIUM and all Phase 4 cascade consequences must have risk register entries" |
| C-11 | Vocabulary enforcement | **PASS** | VOCABULARY CONTRACT: 20 approved verbs, 3 disallowed phrases with NOT-APPROVED enforcement; Compliance column in Phase 2 table; enforcement example shown |
| C-12 | Halt-on-gap escalation | **PASS** | HALT PROTOCOL table form declared before analysis; no-gap declaration table required before Phase 1; phase gates at every boundary; "Analysis does not advance past an unresolved halt block" |

**Score: 110/110 — Golden**
All essential PASS + composite 110 ≥ 85.

**Distinctive strength:** Three independent layers each eliminate different failure modes. Role-sequence catches entity omission. Compliance column catches vocabulary at row level. Phase gates catch advancement past gaps. Single-layer failure degrades gracefully — the other two layers remain active.

---

## Composite Scores

| Rank | Variation | Essential | Recommended | Aspirational | Total | Golden |
|------|-----------|-----------|-------------|--------------|-------|--------|
| T-1 | V-01 | 60/60 | 30/30 | 20/20 | **110/110** | Yes |
| T-1 | V-02 | 60/60 | 30/30 | 20/20 | **110/110** | Yes |
| T-1 | V-03 | 60/60 | 30/30 | 20/20 | **110/110** | Yes |
| T-1 | V-04 | 60/60 | 30/30 | 20/20 | **110/110** | Yes |
| T-1 | V-05 | 60/60 | 30/30 | 20/20 | **110/110** | Yes |

All five variations score 110/110. The v2 rubric was designed to codify patterns already demonstrated by R1's best variation (V-04) — R2 variations were written expressly to satisfy the new criteria, so the perfect-score result is structurally correct. Differentiation below is on robustness and fault-tolerance, not on pass/fail.

**Tie-break ranking by structural fault tolerance:**

1. **V-05** — Three independent enforcement layers. Each layer catches a different failure mode; any single-layer failure is compensated by the other two.
2. **V-02** — Compliance as malformed cell rather than missing prose. Violations are structurally visible by column scan; gap-without-halt is a visible empty form cell.
3. **V-03** — Phase gates as closing conditions at every boundary. Advancement past a gap requires explicitly skipping a named gate.
4. **V-04** — DIRECTIVE-capitalized imperatives with per-phrase enforcement tags. Strongest vocabulary enforcement with DIRECTIVE 0 VIOLATION tag format.
5. **V-01** — Comprehensive DIRECTIVE contract. Strong but relies on single-layer enforcement.

---

## Excellence Signals — V-05 (Top Robustness)

**Signal 1 — Multi-layer enforcement redundancy.** Three independently sufficient layers (role sequence, compliance column, phase gates) each catch a different failure mode. If a model skips the vocabulary contract, the Compliance column in Phase 2 still flags violations. If the Compliance column is ignored, the Phase 2 gate catches it. Defense-in-depth at the prompt level.

**Signal 2 — Count assertion at phase gate.** Phase 4 gate states "Verify cascade trace count >= 2 and at least one cross-layer trace present." This converts the C-09 tightened pass condition from a prose guideline into a boolean gate — a model advancing with one trace must explicitly write "PASS" on a gate that names the count requirement. The count violation is structurally unavoidable to miss.

**Signal 3 — Table-format halt block.** The HALT BLOCK FORM in V-05 is a two-column table, not a prose block. A skipped halt block is a missing table, not a missing paragraph — more structurally visible as an omission. The no-gap declaration forces the same table form even when no gaps fire, establishing the halt pattern before any gaps can occur.

**Signal 4 (from V-02) — Source-table tracing in risk register.** TABLE 9's Source Table column (TABLE 3/4/5/6/7/8) enables bidirectional coverage verification: forward (did finding X get a risk entry?) and backward (does risk entry Y trace to a source finding?). Coverage gaps in the risk register are detectable by mechanical cross-reference rather than by full re-read.

---

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["Compliance-status column co-location: embedding the enforcement check as an adjacent cell in the same table row makes violations visible as malformed cells by column scan — a reader does not need to re-read surrounding prose to spot a disallowed phrase", "Boolean count gate at phase boundary: stating the two-trace minimum as a named gate condition (cascade trace count >= 2) converts a content guideline into a structural assertion — a model advancing past the gate with one trace must explicitly affirm a false condition", "Multi-layer enforcement redundancy: three independent enforcement layers each targeting a different failure mode (role sequence catches entity omission, compliance column catches vocabulary, phase gates catch gap advancement) — single-layer failure degrades gracefully without collapsing the other two"]}
```
