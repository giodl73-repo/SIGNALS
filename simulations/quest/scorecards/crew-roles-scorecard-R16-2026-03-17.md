# crew-roles — Quest Score R16

## Evaluation Method

Static analysis against v10 rubric (27 aspirational + 5 essential + 3 recommended). No trace artifact; scoring from structural presence of mechanisms. Baseline: R15 V-05 scored 27/27 aspirational; R16 tests whether stylistic axes preserve or degrade that count.

---

## Criteria Differential Analysis

Three criteria distinguish variations in this round:

**C-10 — Inertia domain-grounded**
V-01 and V-02 ask "What is the status quo?" inside CONVERGENCE SUMMARY — one question, no structural separation of strengths from gaps, no verbatim anchor for verification. V-03/V-04/V-05 produce a named INERTIA BASELINE artifact with enumerated strengths and gaps plus INERTIA ANCHOR CHECK that verifies verbatim terms in Phase 7. V-01/V-02: PARTIAL. V-03/V-04/V-05: PASS.

**C-34 — Per-slot Phase 1 source + CHECK 5A/5B**
V-01/V-03/V-04 use exact specification notation `Phase 1 source: {row-id} = "{verbatim phrase}"`. V-02 and V-05 use conversational notation `source: row-{N} = "{exact words}"` — functionally equivalent but deviates from the convention the rubric names. V-02/V-05: PARTIAL. V-01/V-03/V-04: PASS.

**C-35 — ROLE-REPLACE sub-procedure (4 fields + CONFIRMED gate)**
V-01/V-03/V-04 use exact `ROLE-REPLACE CONFIRMED: YES/NO`. V-02 emits `Replacement logged: complete/incomplete`; V-05 emits `Replacement complete: yes/no`. Four fields present in all; gate terminology differs. V-02/V-05: PARTIAL. V-01/V-03/V-04: PASS.

All other 24 aspirational criteria (C-09, C-11 through C-33) are structurally present and PASS in all five variations.

---

## Per-Variation Scorecard

### V-01 — VERBOSE

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Essential** | | |
| C-01 All 5 fields | PASS | Phase 4 FRAME FILL lists all 5 field groups explicitly |
| C-02 Inertia-advocate | PASS | Phase 3: "exactly one role whose orientation is 'status-quo advocate'" |
| C-03 Output path | PASS | `.roles/{domain}/` in Phase 6 + CHECK 7 |
| C-04 Domain specificity | PASS | Source citation required per field; FRAME FILL blocks enforce it |
| C-05 Min 3 roles | PASS | Phase 3: "Minimum 5" |
| **Recommended** | | |
| C-06 Lens actionability | PASS | LENS AUDIT fires inline; verify[1]/[2] + simplify[1] checked per role |
| C-07 Collaborates_with resolves | PASS | Phase 4: "2-3 role names from CANDIDATE ROSTER, not generic titles" |
| C-08 Perspective diversity | PASS | PERSPECTIVE AUDIT in Phase 5 + CHECK 8 from written files |
| **Aspirational** | | |
| C-09 Scope gradient | PASS | SCOPE AUDIT requires ≥2 distinct values; CHECK 3A re-validates |
| C-10 Inertia domain-grounded | **PARTIAL** | Status quo question inside CONVERGENCE SUMMARY only; no INERTIA BASELINE artifact separating strengths from gaps; no verbatim anchor check |
| C-11 Vocabulary-forced-field | PASS | Planned-Vocab-Term column + CHECK 4B verbatim verification |
| C-12 through C-29 (18 criteria) | PASS | INPUT INVENTORY, FRAME FILL gate, planning table, Phase 7 checks all structurally present |
| C-30 Inertia-first gate | PASS | STEP 6.1: "WRITE INERTIA-ADVOCATE FIRST" |
| C-31 Vocab binding column | PASS | Planned-Vocab-Term in Phase 5 planning table |
| C-32 Inline LENS AUDIT | PASS | STEP 6.2 fires LENS AUDIT block after each role |
| C-33 PERSPECTIVE AUDIT + CHECK 8 | PASS | Phase 5 gate + Phase 7 CHECK 8 from written files |
| C-34 Per-slot source + 5A/5B | PASS | Exact `Phase 1 source: {row-id} = "{verbatim phrase}"` notation; CHECK 5A and 5B distinct |
| C-35 ROLE-REPLACE sub-procedure | PASS | 4 fields + `ROLE-REPLACE CONFIRMED: YES/NO` gate |

**Score: 26.5/27 × 10 = 9.81**

---

### V-02 — CONVERSATIONAL

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-08 | PASS | All essential/recommended structurally present |
| C-09 Scope gradient | PASS | "Scope check: passed (N distinct scopes)" in Step 5 |
| C-10 Inertia domain-grounded | **PARTIAL** | Step 2 domain summary asks about "the current solution" but no structured strengths/gaps separation; no INERTIA ANCHOR CHECK |
| C-11 through C-29 | PASS | All phases and checks present in plain-English form |
| C-30 Inertia-first gate | PASS | Step 6: "Start with the inertia advocate. Write that file first" |
| C-31 Vocab binding column | PASS | Vocab-Term column in Step 5 table |
| C-32 Inline LENS AUDIT | PASS | Step 6 inline check after each role |
| C-33 PERSPECTIVE AUDIT + CHECK 8 | PASS | Step 5 "Perspective check" gate + Step 7 check 8 |
| C-34 Per-slot source + 5A/5B | **PARTIAL** | `source: row-{N} = "{exact words}"` — functional match but deviates from `Phase 1 source: {row-id}` convention; 5a/5b split present |
| C-35 ROLE-REPLACE sub-procedure | **PARTIAL** | 4 fields present; gate is `Replacement logged: complete/incomplete` not `ROLE-REPLACE CONFIRMED: YES/NO` |

**Score: 25.0/27 × 10 = 9.26**

---

### V-03 — INERTIA-AS-BENCHMARK

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-08 | PASS | All present; LENS AUDIT adds collaborates_with-includes-inertia check |
| C-09 Scope gradient | PASS | SCOPE AUDIT gate in Phase 5 |
| C-10 Inertia domain-grounded | **PASS** | Phase 2 INERTIA BASELINE: named tool + "strengths it has" + "gaps it does not solve"; INERTIA ANCHOR CHECK in Phase 7 verifies verbatim strength terms in lens.verify |
| C-11 through C-29 | PASS | INPUT INVENTORY, FRAME FILL with source citations, planning table with Gap-Addressed column, Phase 7 full check suite |
| C-30 Inertia-first gate | PASS | Phase 6: "Write the inertia-advocate file first" |
| C-31 Vocab binding column | PASS | Planned-Vocab-Term column in Phase 5 |
| C-32 Inline LENS AUDIT | PASS | LENS AUDIT after each role including collaborates_with check |
| C-33 PERSPECTIVE AUDIT + CHECK 8 | PASS | Phase 5 gate + Phase 7 CHECK 8 |
| C-34 Per-slot source + 5A/5B | PASS | `Phase 1 source: {row-id} = "{phrase}"` inline in FRAME FILL; CHECK 5A + 5B in Phase 7 |
| C-35 ROLE-REPLACE sub-procedure | PASS | 4 fields + `ROLE-REPLACE CONFIRMED: YES/NO`; CHECK 3B/4B stay FAIL while NO |

**Score: 27/27 × 10 = 10.0**

---

### V-04 — VERBOSE + INERTIA-AS-BENCHMARK

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-08 | PASS | All present; LENS AUDIT includes collaborates_with-inertia-advocate check |
| C-09 Scope gradient | PASS | SCOPE AUDIT in Phase 5 + CHECK 3A from written files |
| C-10 Inertia domain-grounded | **PASS** | Phase 2: INERTIA BASELINE with "2-3 strengths" + "2-3 gaps" as first-class artifact; INERTIA ANCHOR CHECK in Phase 7 (standalone + inside ROLE-REPLACE re-evaluation) |
| C-11 through C-29 | PASS | Full phase structure with EXIT GATE labels; INPUT INVENTORY, FRAME FILL, planning table with Gap/Strength column |
| C-30 Inertia-first gate | PASS | STEP 6.1 labeled explicitly |
| C-31 Vocab binding column | PASS | Planned-Vocab-Term in Phase 5 table |
| C-32 Inline LENS AUDIT | PASS | STEP 6.2 LENS AUDIT with 5 items including collaborates_with check |
| C-33 PERSPECTIVE AUDIT + CHECK 8 | PASS | Phase 5 dual gate (EXIT GATE: SCOPE AUDIT PASS + PERSPECTIVE AUDIT PASS) + Phase 7 CHECK 8 |
| C-34 Per-slot source + 5A/5B | PASS | Exact `Phase 1 source: {row-id} = "{verbatim phrase}"` per field; CHECK 5A (frame match) + 5B (source verifiable) distinct in Phase 7 |
| C-35 ROLE-REPLACE sub-procedure | PASS | 4 fields + `ROLE-REPLACE CONFIRMED: YES/NO`; **uniquely includes INERTIA ANCHOR CHECK in re-evaluation**: `re-evaluation: {re-run CHECK 1, 3A, 4A, 5A, 5B, 6, 8 and INERTIA ANCHOR CHECK for this role}` |

**Score: 27/27 × 10 = 10.0**

---

### V-05 — VERBOSE + CONVERSATIONAL + INERTIA-AS-BENCHMARK

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-08 | PASS | All present; Lens check includes collaborates_with-inertia-advocate item |
| C-09 Scope gradient | PASS | "Scope check: N distinct scopes" in Step 5 |
| C-10 Inertia domain-grounded | **PASS** | Step 2 "inertia baseline" with "does well" list and "leaves open" list; "Inertia anchor" check in Step 7 verifies verbatim terms |
| C-11 through C-29 | PASS | All phases structurally present; input list, full field fill, planning table with Gap-addressed column |
| C-30 Inertia-first gate | PASS | Step 6: "Start with the inertia advocate. Write its file" |
| C-31 Vocab binding column | PASS | Vocab-Term column in Step 5 table |
| C-32 Inline LENS AUDIT | PASS | "Lens check [{role-name}]" after each role; 5 items |
| C-33 PERSPECTIVE AUDIT + CHECK 8 | PASS | Step 5 perspective check + Step 7 check 8 "Perspective spread" |
| C-34 Per-slot source + 5A/5B | **PARTIAL** | Uses `source: row-{N} = "{exact words}"` notation (conversational); 5a/5b split present; deviates from `Phase 1 source: {row-id}` convention |
| C-35 ROLE-REPLACE sub-procedure | **PARTIAL** | 4 fields present; uses `Replacement complete: yes/no` not `ROLE-REPLACE CONFIRMED: YES/NO`; re-check includes inertia anchor but naming diverges |

**Score: 26.5/27 × 10 = 9.81**

---

## Rankings

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|--------------------|
| 1 | **V-04** (Verbose + Benchmark) | **10.0** | Only variation with INERTIA ANCHOR CHECK inside ROLE-REPLACE re-evaluation |
| 1 | V-03 (Benchmark) | 10.0 | INERTIA BASELINE + INERTIA ANCHOR CHECK; no verbose scaffolding |
| 3 | V-01 (Verbose) | 9.81 | Full structure; C-10 PARTIAL — no INERTIA BASELINE |
| 3 | V-05 (All three) | 9.81 | C-10 PASS; C-34/C-35 PARTIAL due to conversational notation |
| 5 | V-02 (Conversational) | 9.26 | Three PARTIAL: C-10 + C-34 + C-35 |

**V-04 designated top variation** (tie-breaker: INERTIA ANCHOR CHECK embedded in ROLE-REPLACE re-evaluation is unique to V-04).

---

## Excellence Signals from V-04

**Signal 1 — INERTIA ANCHOR CHECK inside ROLE-REPLACE re-evaluation**
When a role is replaced (CHECK 3B or 4B mismatch), V-04's ROLE-REPLACE re-evaluation includes `INERTIA ANCHOR CHECK` as one of the re-run checks. This closes a drift path not addressed by any prior criterion: a replacement role could be written without verifying it preserves the inertia-advocate's verbatim grounding to INERTIA BASELINE strengths. Phase 7's standalone INERTIA ANCHOR CHECK only fires once at the end; V-04 fires it again whenever a role changes. Candidate for C-36.

**Signal 2 — INERTIA BASELINE as Phase 2 first-class artifact with enumerated strengths and gaps**
V-01/V-02 embed the status quo question inside CONVERGENCE SUMMARY (one question among several). V-03/V-04/V-05 produce a separate labeled artifact with a numbered list of 2-3 strengths and 2-3 gaps. This structural separation makes the INERTIA ANCHOR CHECK verifiable (verbatim term matching is only possible when terms are explicitly listed) and makes the Gap/Strength column in the planning table non-redundant (each role's justification traces to a named gap). Candidate for C-36 co-criterion or standalone C-37.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["INERTIA ANCHOR CHECK inside ROLE-REPLACE re-evaluation: replacement events re-run inertia grounding verification, closing the drift path where a replaced role weakens verbatim anchoring to INERTIA BASELINE strengths without Phase 7 catching it", "INERTIA BASELINE as labeled Phase 2 artifact with enumerated strengths and gaps list: structural separation from CONVERGENCE SUMMARY enables verbatim term matching in INERTIA ANCHOR CHECK and non-redundant Gap/Strength column forward-references in planning table"]}
```
