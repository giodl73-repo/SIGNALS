Now I have all five variations. Let me evaluate each against the v5 rubric.

---

## discover-competitors-alt-scorecard-R5-2026-03-17.md

**Skill:** discover-competitors-alt
**Round:** R5
**Rubric version:** v5
**Date:** 2026-03-17

---

### Scoring Reference

| Tier | Criteria | Points each | Total |
|------|----------|-------------|-------|
| Essential | C-01 – C-05 | 12 | 60 |
| Recommended | C-06 – C-08 | 10 | 30 |
| Aspirational | C-09 – C-20 | 5 (2.5 partial) | 60 |
| **Max composite** | | | **150** |

---

### V-01 — Symmetric Verification Loop (C-20 isolation)

**Base:** R4 V-04. **Change:** Pre-submission verification block replaced with symmetric 3-sub-question loop (format artifact? format-failure declared? FAILS/PASS pair?) per constraint.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Inertia-first | PASS | "Competitor 0: None / status quo. Threat level: HIGH. State explicitly." Phase 2 opens with inertia. |
| C-02 | Focus woven | PASS | Pre-map table in Phase 1 feeds Map Position column; findings reference Phase 1 row labels verbatim. Focus visible in every downstream section. |
| C-03 | Threat levels | PASS | Competitor table schema has explicit Threat column; inertia row carries HIGH. |
| C-04 | Whitespace | PASS | DUAL-AXIS WHITESPACE section requires Competitive gap: and Focus gap: labeled findings with combined paragraph. |
| C-05 | Auto-detect | PASS | "SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt." |
| C-06 | Inertia stickiness | PASS | Three labeled slots (WORKAROUND SATISFACTION, SWITCHING COST, HABIT LOCK-IN) with per-slot FAILS/PASS pairs requiring mechanism specificity, not just presence. |
| C-07 | Web-verified | PASS | "Use WebSearch if needed. Cite inline." + "Verify at least one major competitor claim via WebSearch." |
| C-08 | AMEND 3 items | PASS | "AMEND: Exactly 3 items. Input change + output change. Specific." |
| C-09 | Cross-dimensional | PASS | Map Position column threads Phase 1 dimensions through Phase 3; dual-axis finding requires both dimensions. |
| C-10 | Table stakes | PASS | "Reference at least one Phase 1 data point per item." |
| C-11 | Pre-map table | PASS | Phase 1 table with FAILS/PASS in SR block and at phase instruction level; verbatim row labels. |
| C-12 | Whitespace dual-line | PASS | Dual-line template with both labels; FAILS/PASS pair at Phase 4 instruction level. |
| C-13 | Inertia labeled slots | PASS | Three labeled slots with per-slot FAILS/PASS pairs at Phase 2 instruction level. |
| C-14 | Hard-stacked | PASS | SR meta-declaration: "All constraints enforce via the same apparatus: named format artifact + format-failure declaration + FAILS/PASS rejection example pair." |
| C-15 | Map Position column | PASS | Explicit column, verbatim-only rule, empty-cell failure declared. |
| C-16 | Domain-exclusive | PASS | Portability test applied per slot; standalone test block with exact fail condition. |
| C-17 | Symmetric enforcement | PASS | SR5 enforcement symmetry explicitly checks all three carry identical three-component fingerprint. |
| C-18 | Phase-level fingerprint | **PASS** | All three constraints (C-11/SR1, C-13/SR2, C-12/SR4) carry named format artifact + format-failure declaration + FAILS/PASS pair at phase instruction level. Labeled-slot apparatus, not table — but fingerprint is present. |
| C-19 | Apparatus uniformity | **FAIL** | Mixed apparatus: Phase 1 table, Phase 2 labeled text slots, Phase 4 dual-line template. Not all-table. |
| C-20 | Symmetric loop | **PASS** | PRE-SUBMISSION VERIFICATION asks identical three sub-questions per constraint for SR1, SR2, SR4: format artifact present? format-failure declared? FAILS/PASS pair present? Symmetric by construction. |

**Score:** Essential 60/60 + Recommended 30/30 + C-09–C-17: 45/45 + C-18: 5 + C-19: 0 + C-20: 5 = **145/150**

---

### V-02 — All-Table Apparatus (C-19, C-18 carry test)

**Base:** R4 V-05. **Change:** Phase 2 labeled slots → 3-row mechanism table; Phase 4 dual-line → 2-row whitespace table. SR-block FAILS/PASS updated to reference table rows. Phase-instruction-level FAILS/PASS pairs removed from Phase 2 and Phase 4.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Inertia-first | PASS | Identical inertia-first setup. |
| C-02 | Focus woven | PASS | Pre-map → mechanism table rows → Map Position → whitespace table rows → combined paragraph. Distributed throughout. |
| C-03 | Threat levels | PASS | Threat column in competitor table. |
| C-04 | Whitespace | PASS | Whitespace table (2 rows) + combined paragraph required. |
| C-05 | Auto-detect | PASS | SETUP block unchanged. |
| C-06 | Inertia stickiness | PASS | Mechanism table rows require domain-exclusive content; portability test per row. |
| C-07 | Web-verified | PASS | WebSearch + cite inline. |
| C-08 | AMEND 3 items | PASS | Explicit. |
| C-09 | Cross-dimensional | PASS | Map Position column + whitespace table grounded in Phase 1. |
| C-10 | Table stakes | PASS | "Reference at least one Phase 1 data point per item." |
| C-11 | Pre-map table | PASS | FAILS/PASS in SR block item 1. |
| C-12 | Whitespace (table) | PASS | Whitespace table with FAILS/PASS in SR block item 4. |
| C-13 | Inertia (table) | PASS | Mechanism table with FAILS/PASS in SR block item 2. |
| C-14 | Hard-stacked | PASS | SR preamble: "All three primary structural requirements (SR1, SR2, SR4) enforce via table schema." |
| C-15 | Map Position column | PASS | Explicit, verbatim-only. |
| C-16 | Domain-exclusive | PASS | Portability test per row. |
| C-17 | Symmetric enforcement | PASS | All-table apparatus creates identical empty-cell failure surface across all three constraints. |
| C-18 | Phase-level fingerprint | **PARTIAL** | SR block carries labeled FAILS/PASS pairs for SR1 (C-11), SR2 (C-13), SR4 (C-12). SR-block pairs satisfy C-11/SR1 (consistent with R4 precedent). However, Phase 2 instruction only has "An empty row fails" (declarative, not labeled pair); Phase 4 has no FAILS/PASS at phase instruction level. C-18 requires the fingerprint "at its phase instruction." SR-block placement satisfies C-11 but C-12 and C-13 lack phase-instruction-level pairs. PARTIAL: one of three at phase instruction level (C-11 via SR1 position), two only at SR-block level. |
| C-19 | Apparatus uniformity | **PASS** | All three constraints use table schema: Phase 1 pre-map table, Phase 2 mechanism table, Phase 4 whitespace table. Empty-cell failure surface identical across all three. |
| C-20 | Symmetric loop | **PASS** | PRE-SUBMISSION VERIFICATION asks same three sub-questions per constraint (format artifact? format-failure declared? enforcement apparatus present?) for SR1, SR2, SR4 in their table forms. Symmetric. |

**Score:** Essential 60/60 + Recommended 30/30 + C-09–C-17: 45/45 + C-18: 2.5 + C-19: 5 + C-20: 5 = **147.5/150**

---

### V-03 — All-Table + Phase-Level FAILS/PASS Pairs (C-18 + C-19)

**Base:** R4 V-03 (all-table, C-19 PASS). **Change:** Added explicit FAILS/PASS pairs at each table's phase instruction. No verification loop.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Inertia-first | PASS | Standard inertia-first setup. |
| C-02 | Focus woven | PASS | Pre-map → mechanism table → Map Position → whitespace table. |
| C-03 | Threat levels | PASS | Threat column. |
| C-04 | Whitespace | PASS | Whitespace table required; both rows; combined paragraph. |
| C-05 | Auto-detect | PASS | SETUP block. |
| C-06 | Inertia stickiness | PASS | Mechanism table rows with portability test; FAILS/PASS at phase level. |
| C-07 | Web-verified | PASS | WebSearch + cite. |
| C-08 | AMEND 3 items | PASS | Explicit. |
| C-09 | Cross-dimensional | PASS | Map Position + whitespace table grounded in Phase 1. |
| C-10 | Table stakes | PASS | "Reference at least one Phase 1 data point per item." |
| C-11 | Pre-map table | PASS | FAILS/PASS at phase instruction level for both market and positioning variants. |
| C-12 | Whitespace (table) | PASS | "FAILS: Whitespace table absent; single-row table... PASS: Both rows present and grounded..." at Phase 4 instruction level. |
| C-13 | Inertia (table) | PASS | "FAILS: Mechanism table absent; any row empty... PASS: All three rows present..." at Phase 2 instruction level. |
| C-14 | Hard-stacked | PASS | SR block: "All three primary structural requirements (SR1, SR2, SR4) enforce via table schema." |
| C-15 | Map Position column | PASS | Explicit, verbatim. |
| C-16 | Domain-exclusive | PASS | Portability test per row. |
| C-17 | Symmetric enforcement | PASS | All-table apparatus + phase-level FAILS/PASS pairs. |
| C-18 | Phase-level fingerprint | **PASS** | All three constraints carry named format artifact + format-failure declaration + FAILS/PASS pair at phase instruction level. Phase 1 table (market/positioning variants both), Phase 2 mechanism table, Phase 4 whitespace table. Three-component fingerprint present at phase instruction level for C-11, C-13, C-12. |
| C-19 | Apparatus uniformity | **PASS** | All-table: pre-map table, mechanism table, whitespace table. |
| C-20 | Symmetric loop | **FAIL** | Pre-submission verification is prose: "Before submitting: verify all four Structural Requirements are met. Each of SR1, SR2, and SR4 must be a populated table..." No symmetric sub-question structure; no per-constraint question repetition. Fails C-20's "identical sub-questions per constraint" requirement. |

**Score:** Essential 60/60 + Recommended 30/30 + C-09–C-17: 45/45 + C-18: 5 + C-19: 5 + C-20: 0 = **145/150**

---

### V-04 — All-Table + Symmetric Verification Loop (C-19 + C-20)

**Base:** R4 V-03 (all-table). **Change:** Added symmetric verification loop without adding FAILS/PASS pairs at phase instructions.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Inertia-first | PASS | Standard. |
| C-02 | Focus woven | PASS | Pre-map → mechanism table → Map Position → whitespace table. |
| C-03 | Threat levels | PASS | Threat column. |
| C-04 | Whitespace | PASS | Whitespace table; both rows; combined paragraph. |
| C-05 | Auto-detect | PASS | SETUP block. |
| C-06 | Inertia stickiness | PASS | Mechanism table rows with portability test. |
| C-07 | Web-verified | PASS | WebSearch + cite. |
| C-08 | AMEND 3 items | PASS | Explicit. |
| C-09 | Cross-dimensional | PASS | Map Position + grounded whitespace. |
| C-10 | Table stakes | PASS | Phase 1 data per item. |
| C-11 | Pre-map table | PASS | SR block item: "Absent table or empty cells fail." Named format artifact present. |
| C-12 | Whitespace (table) | PASS | SR block item: "Absent table or single-row table fails." Named format artifact present. |
| C-13 | Inertia (table) | PASS | SR block item: "Empty row or content that passes the portability test fails." Named format artifact present. |
| C-14 | Hard-stacked | PASS | SR block: "All three primary structural requirements enforce via table schema." |
| C-15 | Map Position column | PASS | Explicit, verbatim. |
| C-16 | Domain-exclusive | PASS | Portability test per row. |
| C-17 | Symmetric enforcement | PASS | All-table apparatus. |
| C-18 | Phase-level fingerprint | **FAIL** | SR block items use declarative failure language only ("Absent table or empty cells fail") — no labeled FAILS/PASS pairs anywhere for C-12 or C-13. Phase 2 instruction: "An empty row fails." Phase 4: no FAILS/PASS at instruction level. C-18 requires the named FAILS/PASS pair apparatus specifically. Declarative failure statements without labeled pair format do not satisfy C-18. |
| C-19 | Apparatus uniformity | **PASS** | All-table. |
| C-20 | Symmetric loop | **PASS** | PRE-SUBMISSION VERIFICATION asks identical three sub-questions per SR: format artifact present? format-failure declared? enforcement apparatus present (table schema with...)? Same question structure for SR1, SR2, SR4. Rubric defines C-20 as "format artifact present? format-failure declared? enforcement apparatus present?" — V-04 matches exactly. |

**Score:** Essential 60/60 + Recommended 30/30 + C-09–C-17: 45/45 + C-18: 0 + C-19: 5 + C-20: 5 = **145/150**

---

### V-05 — Full R5 Stack (C-18 + C-19 + C-20)

**Axes:** All-table apparatus + phase-instruction FAILS/PASS pairs + symmetric verification loop.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Inertia-first | PASS | "Competitor 0: None / status quo. Threat level: HIGH. State explicitly." |
| C-02 | Focus woven | PASS | Pre-map table → mechanism table → Map Position column → whitespace table → combined paragraph. Focus dimension traceable through all phases. |
| C-03 | Threat levels | PASS | Threat column; inertia row HIGH. |
| C-04 | Whitespace | PASS | Whitespace table (2 rows) + combined paragraph; both required. |
| C-05 | Auto-detect | PASS | SETUP block. |
| C-06 | Inertia stickiness | PASS | Mechanism table rows; portability test per row; FAILS/PASS at phase level. |
| C-07 | Web-verified | PASS | WebSearch + cite inline for both Phase 2 and Phase 3. |
| C-08 | AMEND 3 items | PASS | Explicit. |
| C-09 | Cross-dimensional | PASS | Map Position column grounds Phase 3 in Phase 1; whitespace table grounded in Map Position values. |
| C-10 | Table stakes | PASS | "Reference at least one Phase 1 data point per item." |
| C-11 | Pre-map table | PASS | Phase instruction FAILS/PASS for both market/positioning variants + SR block item. |
| C-12 | Whitespace (table) | PASS | Phase instruction: "FAILS: Whitespace table absent; single-row table... PASS: Both rows present and grounded..." + SR block item. |
| C-13 | Inertia (table) | PASS | Phase instruction: "FAILS: Mechanism table absent; any row empty; any row content passing the portability test. PASS: All three rows present..." + SR block item. |
| C-14 | Hard-stacked | PASS | SR block: "All three primary structural requirements (SR1, SR2, SR4) enforce via table schema." |
| C-15 | Map Position column | PASS | Explicit, verbatim-only, empty-cell failure declared. |
| C-16 | Domain-exclusive | PASS | Portability test per row; standalone block. |
| C-17 | Symmetric enforcement | PASS | All-table + phase-instruction FAILS/PASS + SR block FAILS/PASS. Maximum enforcement surface. |
| C-18 | Phase-level fingerprint | **PASS** | All three constraints carry three-component fingerprint at phase instruction level: named format artifact (pre-map table / mechanism table / whitespace table) + format-failure declaration + labeled FAILS/PASS pair. SR block doubles coverage. No constraint relies on SR block alone. |
| C-19 | Apparatus uniformity | **PASS** | All-table: pre-map table (C-11), mechanism table (C-13), whitespace table (C-12). Empty-cell failure surface structurally identical across all three. |
| C-20 | Symmetric loop | **PASS** | PRE-SUBMISSION VERIFICATION: identical three sub-questions per constraint (format artifact present? format-failure declared? FAILS/PASS pair present?) for SR1, SR2, SR4. "FAILS/PASS pair present?" is the strongest formulation — asks for the actual artifact, not just the apparatus type. |

**Score:** Essential 60/60 + Recommended 30/30 + C-09–C-17: 45/45 + C-18: 5 + C-19: 5 + C-20: 5 = **150/150**

---

### Composite Scores

| Rank | Variation | Essential | Rec | Asp C-09-17 | C-18 | C-19 | C-20 | Total |
|------|-----------|-----------|-----|-------------|------|------|------|-------|
| 1 | V-05 | 60 | 30 | 45 | 5 | 5 | 5 | **150** |
| 2 | V-02 | 60 | 30 | 45 | 2.5 | 5 | 5 | **147.5** |
| 3 (tie) | V-01 | 60 | 30 | 45 | 5 | 0 | 5 | **145** |
| 3 (tie) | V-03 | 60 | 30 | 45 | 5 | 5 | 0 | **145** |
| 3 (tie) | V-04 | 60 | 30 | 45 | 0 | 5 | 5 | **145** |

All essential criteria pass across all five variations.

---

### Key Open Question Resolved

**V-02 resolves the SR-block vs. phase-instruction question for C-18:** SR-block FAILS/PASS pairs that reference table rows satisfy C-18 for C-11 (consistent with R4 precedent where SR1's position precedes Phase 1) but PARTIALLY for C-12 and C-13 — the actual phase instructions for Phase 2 and Phase 4 in V-02 use declarative failure language only ("An empty row fails"), not labeled pairs. C-18 PARTIAL score of 2.5 confirms SR-block placement is insufficient for constraints whose phase instructions are narratively soft.

**V-04 answers the sub-question wording question for C-20:** The loop's third sub-question can use "enforcement apparatus present (table schema with...)" rather than "FAILS/PASS pair present?" and still satisfy C-20. Symmetry of structure dominates over exact wording of the third sub-question.

---

### Excellence Signals (V-05)

1. **Double-enforcement per constraint:** Phase-instruction FAILS/PASS pair + SR-block FAILS/PASS pair for the same constraint is not redundant — it creates two observable failure surfaces. The phase instruction pair fires during execution; the SR block pair fires during the pre-execution checklist. Both together eliminated any ambiguity about where C-18 credit lies.

2. **"FAILS/PASS pair present?" as the highest-signal C-20 sub-question 3:** Asking whether the pair itself exists rather than whether an "enforcement apparatus" exists makes sub-question 3 a direct integrity check, not a structural description check. V-05's loop explicitly asks for the artifact; V-04's loop asks for the type. Both pass C-20, but V-05's formulation is more diagnostic.

3. **Table schema as named format artifact:** When apparatus is all-table, the table itself becomes the named format artifact for C-18. The column headers (or row labels) are the format specification. The empty-cell failure is the failure declaration. The labeled FAILS/PASS pair at the phase instruction level confirms what "empty" means in this domain. All three components are present and their table-form equivalents are unambiguous.

---

### Rubric Writing Artifact

`simulations/quest/rubrics/discover-competitors-alt-rubric-v5-2026-03-17.md` — v5 rubric as provided.
`simulations/quest/scorecards/discover-competitors-alt-scorecard-R5-2026-03-17.md` — this document.

---

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["SR-block-only FAILS/PASS pairs are PARTIAL for C-18 when phase instructions are declaratively soft -- phase-instruction-level placement is load-bearing for C-12 and C-13, not just SR-block placement", "C-20 symmetric loop satisfies with 'enforcement apparatus present?' as sub-question 3, not only 'FAILS/PASS pair present?' -- loop symmetry of structure dominates over exact sub-question wording", "Phase-instruction FAILS/PASS + SR-block FAILS/PASS double-coverage per constraint is not redundant -- it eliminates C-18 ambiguity by creating two observable failure surfaces at different execution points"]}
```
