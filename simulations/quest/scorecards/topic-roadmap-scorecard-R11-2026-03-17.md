---

## Round 11 Scorecard — topic-roadmap

**Written to**: `simulations/quest/scorecards/topic-roadmap-scorecard-R11-2026-03-17.md`

---

### Composite Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-12 | 1 | 2 | 2 | 2 | 2 |
| C-17 | 1 | 1 | 1 | 1 | 1 |
| C-21 | 2 | 2 | **0** | 2 | 2 |
| C-22 | 2 | 2 | **0** | 2 | 2 |
| C-24 | 2 | **0** | 2 | 2 | 2 |
| C-25 | 1 | 2 | 2 | 2 | 2 |
| C-26 | **0** | 2 | 2 | 2 | 2 |
| **Raw (of 36)** | **31** | **33** | **31** | **35** | **35** |
| **Score** | **8.61** | **9.17** | **8.61** | **9.72** | **9.72** |

**Rank**: V-04 = V-05 (9.72) > V-02 (9.17) > V-01 = V-03 (8.61)

All essential (C-01–C-05) and all recommended (C-06–C-08) pass across all five variations.

---

### Key Finding — V-01 Axis Incomplete

V-01's column rename was applied (`Consequence if HOLDS` → `Consequence if unchanged` in Phase 5 schema), but the exit criterion sentence was **not** added. The Phase 5 EXIT CRITERION text is unchanged from R10 — it names no field condition. Result: C-26=0, C-12=1, same as the universal R10 state. The "one sentence closes the gap" hypothesis is correct in principle; the sentence just wasn't in the generated text.

---

### Status vs R10

| Criterion | R10 | R11 best |
|-----------|-----|----------|
| C-12 | 1 universal | **2** (V-02, V-03, V-04, V-05) |
| C-26 | n/a | **2** (V-02, V-03, V-04, V-05) |
| C-17 | 1 universal | **1 universal** (unresolved) |

C-12 and C-26 resolved in V-04/V-05. **C-17 is the sole remaining chronic partial** — `Bias blocked by guard` column missing from Phase 6 proposal tables.

---

```json
{"top_score": 9.72, "all_essential_pass": true, "new_patterns": ["Column rename in Phase 5 table schema is necessary but insufficient for C-26 full pass -- exit criterion text must independently name the field by its column header; two separate structural changes, both required", "Dual enforcement (table preamble + exit criterion) achieves C-12 full and C-26 full simultaneously -- preamble states blocking rule before the table, exit criterion names field at phase boundary; orthogonal placements"]}
```
5: `If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS." Stop. Phase 6 does NOT open.` |
| **C-07** Confidence tiers defined | PASS | PASS | PASS | PASS | PASS | Verdict Vocabulary block: HIGH / MEDIUM / LOW each with countable artifact-independence criteria |
| **C-08** Consequence-if-unchanged in proposals | PASS | PASS | PASS | PASS | PASS | V-01 text: Phase 5 table uses "Consequence if unchanged" (column renamed); Phase 6a/6b tables also use "Consequence if unchanged" — present in both locations. V-02–V-05 by axis: same or better. |

**All recommended: PASS across all five variations (3/3).**

---

### Aspirational Criteria — Per Variation

#### C-09 — Pre-signal defense register (max 2)

All variations: PHASE-1-READ-BARRIER with explicit hard constraint, defense register table schema, and ENTRY CONDITION before any file is read.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

V-01 text: "ENTRY CONDITION: No files have been read since Phase 1 began (first run or restart)." Hard constraint present.

---

#### C-10 — SIGNAL READ-LOCK (max 2)

All variations: named SIGNAL READ-LOCK immediately after inventory table, with explicit prohibition on re-reading and bias labels (confirmation bias; vocabulary contamination).

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

V-01 text: `[>> GUARD: SIGNAL READ-LOCK <<]` immediately after Phase 2 inventory; names both confirmation bias and vocabulary contamination.

---

#### C-11 — INERTIA-GATE phase sequencing (max 2)

All variations: explicit INERTIA-GATE label at Phase 5 entry with stated HOLDS exclusion ("HOLDS dimensions have no path to Phase 6").

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

V-01 text: `[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]` with Mechanism "Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have no path to Phase 6."

---

#### C-12 — Consequence column in defeat assessment (max 2)

**Key criterion for R11.** Full pass requires the consequence column to be present in the defeat assessment AND an explicit blocking mechanism stated.

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **1** | [TEXT] Column renamed to "Consequence if unchanged" in Phase 5 schema. EXIT CRITERION reads: "Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted if all HOLDS; at least one DEFEATED verdict present to proceed to Phase 6." — consequence field NOT mentioned in exit criterion. Column present, blocking mechanism absent from exit criterion. Partial. |
| **V-02** | **2** | [ANALYTICAL] Axis adds consequence enforcement in BOTH table preamble (before the table, blocking stated pre-gate) AND exit criterion (naming field at phase boundary). Blocking stated in preamble satisfies "positioned before the proposal gate." Full pass. |
| **V-03** | **2** | [ANALYTICAL] Numbered checklist exit criterion includes explicit item: "All DEFEATED rows have Consequence if unchanged field populated." Blocking is stated in the exit criterion itself. Full pass. |
| **V-04** | **2** | [ANALYTICAL] c26 minimal axis adds exit criterion sentence naming field. Full pass (column present + exit criterion enforces). |
| **V-05** | **2** | [ANALYTICAL] c26 imperative adds "BLOCKED: A DEFEATED row CANNOT exit Phase 5 if its Consequence if unchanged field is empty" — imperative blocking in exit criterion. Full pass. |

---

#### C-13 — DEFEATED/HOLDS verdict semantics (max 2)

All variations: Verdict Vocabulary block defines both verdicts with forward-path statements. HOLDS → "no path to Phase 6"; DEFEATED → "advances to Phase 6."

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-14 — NEW/PRIOR split with explicit date anchor (max 2)

All variations: Phase 2 includes explicit inequality rule and STRATEGY DATE as a named field.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

V-01 text: "Record STRATEGY DATE as a named field before classification begins. Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE."

---

#### C-15 — Confidence levels with evidential criteria (max 2)

All variations: Verdict Vocabulary block defines HIGH / MEDIUM / LOW with countable artifact-independence criteria.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

V-01 text: "HIGH: two or more independent NEW artifacts support the defeat on this dimension; MEDIUM: one NEW artifact; LOW: inference only (no direct NEW artifact evidence)."

---

#### C-16 — Type-labeled nulls for all categories (max 2)

All variations: all 4 delta-type nulls (CONFIRMED / EXPANDED / UNEXPECTED / CHALLENGED) and all 3 proposal-type nulls (ADDITIONS / REMOVALS / REPRIORITIZATIONS) with category labels.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

V-01 text: Phase 4 has all 4 labeled nulls; Phase 6 has labeled Null, Null-REMOVALS, Null-REPRIORITIZATIONS. "Silence is not a null declaration" present.

---

#### C-17 — Bias labels per proposal row and per phase (max 2)

**Chronic partial — universally 1 in R10; unchanged in R11.** No R11 axis addresses Phase 6 proposal table columns. Per-phase annotations present; "Bias blocked by guard" column absent from Phase 6 tables.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **1** | **1** | **1** | **1** | **1** |

Phase-level bias annotations present (Phase 2: recency bias; Phase 3: framing bias; Phase 4: confirmation bias). Phase 6a/6b schemas contain no "Bias blocked by guard" column. Partial across all variations.

---

#### C-18 — WITHDRAW operator with row-level semantics (max 2)

All variations: Phase 7 defines WITHDRAW syntax, row-level removal, and explicit distinction from NO and REVISED.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

V-01 text: "Reply WITHDRAW [#] to remove specific proposals before confirming. WITHDRAW syntax: WITHDRAW [2] or WITHDRAW [1, 3]. Removes named proposals only; remainder is applied. WITHDRAW is not NO (rejects all) and not REVISED (requires a resubmitted table)."

---

#### C-19 — Phase entry/exit conditions (max 2)

All variations: ENTRY CONDITION and EXIT CRITERION defined for every gated phase.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-20 — Bias labels at every structural guard (max 2)

All variations: every named guard carries an inline bias label (INERTIA PRIOR, SCHEMA COMMITMENT, PHASE-1-READ-BARRIER, SIGNAL READ-LOCK, VERDICT SEMANTICS BLOCK, INERTIA-GATE Sites 1 and 2, CONFIRMATION GATE, WRITE GUARD).

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-21 — Dual-site INERTIA-GATE enforcement (max 2)

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **2** | [TEXT] "Site 1 of 2 -- Phase 5 entry" and "Site 2 of 2 -- Phase 6 entry" present. Phase 6 Mechanism: "HOLDS exclusion is enforced here without relying on the Phase 5 site to carry the constraint. A reviewer can confirm HOLDS exclusion from this block alone, without reading Phase 5." Independent restatement explicit. |
| **V-02** | **2** | [ANALYTICAL] R10 V-02 base had C-21=2 with identical dual-site structure. No axis change removes this. |
| **V-03** | **0** | [ANALYTICAL] R10 V-03 base had C-21=0 (no "Site 1 of 2 / Site 2 of 2" structure; Phase 6 references Phase 5 without independent self-containment). No R11 axis changes this. |
| **V-04** | **2** | [ANALYTICAL] R10 V-04 base had C-21=2 with full independent restatement. |
| **V-05** | **2** | [ANALYTICAL] R10 V-05 base had C-21=2. |

---

#### C-22 — Restart isolation clause in Phase 1 read-barrier (max 2)

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **2** | [TEXT] "RESTART ISOLATION: If execution resumes after an interruption without prior context, do NOT re-read strategy.md or any signal file to reconstruct the state of this run. Write the defense register from prior knowledge only. Re-reading files to catch up after a mid-run restart contaminates Phase 1 as effectively as skipping it entirely." Co-located with first-run constraint. |
| **V-02** | **2** | [ANALYTICAL] R10 V-02 base had C-22=2 with identical restart clause. |
| **V-03** | **0** | [ANALYTICAL] R10 V-03 base had C-22=0 (first-run isolation only; no restart clause). No R11 axis changes this. |
| **V-04** | **2** | [ANALYTICAL] R10 V-04 base had C-22=2. |
| **V-05** | **2** | [ANALYTICAL] R10 V-05 base had C-22=2. |

---

#### C-23 — Dedicated verdict vocabulary block before Phase 5 (max 2)

All variations: standalone "## Verdict Vocabulary" section between Phase 4 and Phase 5; both verdicts defined with forward-path statements; structurally separate from phase instructions.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

V-01 text: `## Verdict Vocabulary` with SECTION SCOPE declaration and both DEFEATED/HOLDS defined as standalone definitions.

---

#### C-24 — Structural mechanism spatial separation (max 2)

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **2** | [TEXT] SECTION SCOPE on Phase 1 ("does not contain verdict vocabulary definitions; does not contain INERTIA-GATE exclusion text"), on Verdict Vocabulary ("does not contain Phase 1 read-barrier language; does not contain restart isolation clause text; does not contain INERTIA-GATE exclusion text"), on Phase 5 ("does not redefine verdict semantics (those are defined in the Verdict Vocabulary block above); does not contain restart isolation language"), on Phase 6. Phase 5 INERTIA-GATE Mechanism contains only gate-exclusion text — no inline verdict semantic descriptions. All three mechanisms spatially clean. |
| **V-02** | **0** | [ANALYTICAL] R10 V-02 deliberately retained inline verdict semantics in Phase 5 INERTIA-GATE ("HOLDS is the default verdict and requires no evidence; DEFEATED requires specific named signal evidence"). No SECTION SCOPE declarations. Axis is C-26, not C-24. C-24 failure carried from R10. |
| **V-03** | **2** | [ANALYTICAL] R10 V-03 had C-24=2 with full SECTION SCOPE declarations and clean Phase 5 INERTIA-GATE. No R11 axis changes this. |
| **V-04** | **2** | [ANALYTICAL] R10 V-04 had C-24=2 with MUST NOT CONTAIN prohibitions. |
| **V-05** | **2** | [ANALYTICAL] R10 V-05 had C-24=2 with heading-level SCOPE annotations. |

---

#### C-25 — Phase 5 verdict deferral with anti-duplication clause (max 2)

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **1** | [TEXT] Phase 5: "Apply the Verdict Vocabulary defined above." — forward-reference present. No anti-duplication clause co-located. Matches R10 V-01 partial: forward-reference present, anti-duplication absent. |
| **V-02** | **2** | [ANALYTICAL] R10 V-02 had C-25=2 with "Apply the Verdict Vocabulary block defined above. Do not redefine verdict semantics here. Any inline DEFEATED or HOLDS definition appearing in this phase is a structural violation of the single-source guarantee." No axis change removes this. |
| **V-03** | **2** | [ANALYTICAL] R10 V-03 had C-25=2 with forward-reference + anti-duplication clause. |
| **V-04** | **2** | [ANALYTICAL] R10 V-04 had C-25=2 with categorical anti-duplication. |
| **V-05** | **2** | [ANALYTICAL] R10 V-05 had C-25=2 with anti-duplication + heading-level SCOPE reinforcement. |

---

#### C-26 — Consequence field enforcement stated in Phase 5 exit criterion (max 2)

**New criterion in v11. This is the primary target for Round 11.**

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **0** | [TEXT] EXIT CRITERION reads: "Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted if all HOLDS; at least one DEFEATED verdict present to proceed to Phase 6." Field name "Consequence if unchanged" does NOT appear in the exit criterion. Column rename was applied (Phase 5 schema uses "Consequence if unchanged") but the exit criterion sentence was not added. Axis declared this as the change; the change was not implemented in the generated text. FAIL — same as R10 universal state. |
| **V-02** | **2** | [ANALYTICAL] Dual-enforcement axis: preamble note states blocking rule; exit criterion is also updated to name the field. Exit criterion includes "Consequence if unchanged field populated for all DEFEATED rows; exit blocked if any row is missing this field." Field named by column header in exit criterion text. Full pass. |
| **V-03** | **2** | [ANALYTICAL] Numbered checklist exit criterion. Item 4: "All DEFEATED rows have Consequence if unchanged field populated." Field named by column header in exit criterion checklist. Verifiable at phase boundary without reading surrounding prose. Full pass. |
| **V-04** | **2** | [ANALYTICAL] c26 minimal: exit criterion sentence "Consequence if unchanged field populated for all DEFEATED rows; exit blocked if any DEFEATED row is missing this field" added to the standard exit criterion text. Field named by column header. Full pass. |
| **V-05** | **2** | [ANALYTICAL] c26 imperative: "BLOCKED: A DEFEATED row CANNOT exit Phase 5 if its Consequence if unchanged field is empty." Imperative form names the field by column header in the exit criterion. Full pass. |

---

### Composite Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | 2 | 2 | 2 | 2 | 2 |
| C-10 | 2 | 2 | 2 | 2 | 2 |
| C-11 | 2 | 2 | 2 | 2 | 2 |
| C-12 | 1 | 2 | 2 | 2 | 2 |
| C-13 | 2 | 2 | 2 | 2 | 2 |
| C-14 | 2 | 2 | 2 | 2 | 2 |
| C-15 | 2 | 2 | 2 | 2 | 2 |
| C-16 | 2 | 2 | 2 | 2 | 2 |
| C-17 | 1 | 1 | 1 | 1 | 1 |
| C-18 | 2 | 2 | 2 | 2 | 2 |
| C-19 | 2 | 2 | 2 | 2 | 2 |
| C-20 | 2 | 2 | 2 | 2 | 2 |
| C-21 | 2 | 2 | 0 | 2 | 2 |
| C-22 | 2 | 2 | 0 | 2 | 2 |
| C-23 | 2 | 2 | 2 | 2 | 2 |
| C-24 | 2 | 0 | 2 | 2 | 2 |
| C-25 | 1 | 2 | 2 | 2 | 2 |
| C-26 | 0 | 2 | 2 | 2 | 2 |
| **Raw (of 36)** | **31** | **33** | **31** | **35** | **35** |
| **Score (×10/36)** | **8.61** | **9.17** | **8.61** | **9.72** | **9.72** |

**Rank**: V-04 = V-05 (9.72) > V-02 (9.17) > V-01 = V-03 (8.61)

---

### Excellence Signals — V-04 / V-05 (Tied Top)

**What V-04 achieves that V-01 does not:**
V-04 fully applies c26 minimal (column rename + exit criterion sentence) AND carries forward the full C-21/C-22/C-24/C-25 stack from R10. V-01 applies only the column rename; the exit criterion sentence was not present in the generated V-01 text. The decisive gap: column rename is necessary but not sufficient for C-26 full pass. The exit criterion sentence must independently name the field.

**What V-04 achieves that V-02 does not:**
V-02 achieves C-26=2 and C-12=2 via dual enforcement, but deliberately carries C-24=0 from the R10 V-02 base (Phase 5 INERTIA-GATE retains inline verdict semantics). The spatial separation cost (–2) outweighs the C-12 gain (+1) and C-26 gain (+2) relative to V-04. Net: V-02 is 33 vs V-04's 35.

**V-04 vs V-05 tie analysis:**
Both achieve 35/36. V-05's heading-level SCOPE annotations make spatial separation verifiable from the document outline — a stronger auditor signal — but C-24 full pass is binary (2/2) for both. The imperative framing of C-26 in V-05 ("BLOCKED: A DEFEATED row CANNOT exit Phase 5...") is marginally stronger than V-04's declarative sentence, but both satisfy the exit criterion naming requirement. No scoring mechanism differentiates them under this rubric. V-05 preferred if outline-verifiability is operationally important.

---

### Key Finding — V-01 Axis Implementation Incomplete

V-01's declared axis was: (1) rename "Consequence if HOLDS" → "Consequence if unchanged" in Phase 5 schema, AND (2) add one exit criterion sentence naming the field. The generated V-01 text applied only change (1): column renamed in both the output schema and Phase 5 table. Change (2) was not applied: the Phase 5 EXIT CRITERION text is unchanged from R10 and does not mention "Consequence if unchanged."

**Effect**: V-01 scores C-26=0 (fail) and C-12=1 (partial) — identical to the universal R10 state. The "minimum intervention hypothesis" (one sentence closes one rubric gap) is correct in principle but was not implemented in the V-01 generation. This is a variate quality finding, not a rubric finding.

**Implication for R12**: The V-04/V-05 full-stack approach is the production path. The "minimum intervention" approach in V-01 needs the exit criterion sentence to actually be present in the generated text for the axis to be validated.

---

### Chronic Partials

| Criterion | Round 10 | Round 11 | Status |
|-----------|----------|----------|--------|
| C-12 | 1/2 universal | 1/2 (V-01), 2/2 (V-02–V-05) | **RESOLVED** in V-02, V-03, V-04, V-05 |
| C-17 | 1/2 universal | 1/2 universal | **PERSISTENT** — "Bias blocked by guard" column absent from Phase 6 proposal tables across all 5 variations |
| C-26 | n/a (new) | 0/2 (V-01), 2/2 (V-02–V-05) | **NEW CRITERION**: achieved in V-02–V-05; V-01 failed axis implementation |

C-17 is now the sole unresolved chronic partial. Next round should target adding a "Bias blocked by guard" column to Phase 6a and Phase 6b proposal tables.

---

### Next Frontier — C-17 Full Pass

C-17 full pass requires:
- "Bias blocked by guard" column in Phase 6a and Phase 6b proposal schemas
- Column names the bias each row-level guard prevents at the decision surface
- Combined with existing per-phase annotations (already at 2/2)

Example column entries for Phase 6 rows:
- ADD row: "Action-default bias — change requires named NEW evidence; presence of evidence does not force the action"
- REMOVE row: "Loss aversion — existing items defended by INERTIA; removal requires DEFEATED verdict, not just absence of recent signals"
- REPRIORITIZE row: "Recency bias — newly visible dimension does not automatically outrank established dimensions; ranking change requires defeat of the incumbent ordering"

This is the pattern needed for C-17 → 2. One column, 3 entry templates, integrated into Phase 6 output schema committed at skill start.

---

```json
{"top_score": 9.72, "all_essential_pass": true, "new_patterns": ["Column rename in Phase 5 table schema is necessary but insufficient for C-26 full pass -- the exit criterion text must independently name the field by its column header; these are two separate structural changes that must both be present; V-01 demonstrates that applying only the column rename leaves C-26 at fail despite the naming alignment", "Dual enforcement (table preamble + exit criterion) achieves C-12 full and C-26 full simultaneously -- preamble states blocking rule before the table (C-12 gate), exit criterion names field at phase boundary (C-26 gate); the two sites serve different auditor needs and are orthogonal placements"]}
```
