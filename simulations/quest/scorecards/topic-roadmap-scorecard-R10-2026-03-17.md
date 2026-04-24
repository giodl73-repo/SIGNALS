## Round 10 Scorecard — topic-roadmap v10

---

### Scoring Basis

**Formula**: aspirational raw score / 34 * 10 (17 criteria × 2 max each)
**Essential gate**: C-01–C-05 (all must pass)
**Recommended gate**: C-06–C-08 (at least 2/3 must pass)
**Aspirational criteria**: C-09–C-25 (0 / 1 / 2 per criterion)

---

### Essential Criteria — All Variations

All five variations share identical structure for essential criteria.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| **C-01** Signal inventory table with delta categories | PASS | PASS | PASS | PASS | PASS | Phase 2 table schema committed; all 4 delta categories in Phase 4; proposals appear only after Phase 4 |
| **C-02** Inventory precedes proposals | PASS | PASS | PASS | PASS | PASS | Phase 2 → Phase 3 → Phase 4 → Phase 5 ordering enforced by entry conditions |
| **C-03** Proposals action-typed | PASS | PASS | PASS | PASS | PASS | Phase 6 schema includes Action (ADD/REMOVE/REPRIORITIZE), Before/After state, evidence column |
| **C-04** Confirmation gate present and blocking | PASS | PASS | PASS | PASS | PASS | Phase 7: "STOP HERE. Write nothing further until the user replies." + "PENDING CONFIRMATION — strategy.md has NOT been modified." |
| **C-05** All-namespace coverage with null rows | PASS | PASS | PASS | PASS | PASS | Phase 2: "Zero-artifact namespaces emit an explicit null row." Phase 6: "Silence is not a null declaration." All 9 namespaces required both places |

**All essential: PASS across all five variations.**

---

### Recommended Criteria — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| **C-06** Null path stop | PASS | PASS | PASS | PASS | PASS | Phase 5: `If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS." Stop. Phase 6 does NOT open.` |
| **C-07** Confidence tiers defined | PASS | PASS | PASS | PASS | PASS | Verdict Vocabulary block: HIGH / MEDIUM / LOW each with countable artifact-independence criteria |
| **C-08** Consequence-if-unchanged in proposals | PASS | PASS | PASS | PASS | PASS | Phase 5 table: "Consequence if HOLDS"; Phase 6a/6b tables: "Consequence if unchanged" — present in both locations |

**All recommended: PASS across all five variations (3/3).**

---

### Aspirational Criteria — Per Variation

#### C-09 — Pre-signal defense register (max 2)

All variations include PHASE-1-READ-BARRIER with explicit hard constraint before any file is read, defense register table schema, and entry/exit conditions.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

V-03 note: "DO NOT read strategy.md or any signal file before Phase 1 is complete" is present in the ENTRY CONDITION; full pass without the restart clause (restart is C-22 scope).

---

#### C-10 — SIGNAL READ-LOCK (max 2)

All variations have named SIGNAL READ-LOCK immediately after inventory table, with explicit prohibition on re-reading and bias labels (confirmation bias; vocabulary contamination).

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-11 — INERTIA-GATE phase sequencing (max 2)

All variations have an explicit INERTIA-GATE label at Phase 5 entry with stated HOLDS exclusion ("HOLDS dimensions have no path to Phase 6"). This criterion tests gate existence and labeling — dual-site is C-21.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

V-03 note: Phase 5 Mechanism states "Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have no path to Phase 6." — explicit label satisfies C-11.

---

#### C-12 — Consequence column in defeat assessment (max 2)

All variations include "Consequence if HOLDS" in the Phase 5 defeat assessment table and "Consequence if unchanged" in Phase 6 proposal tables. However, no variation's Phase 5 EXIT CRITERION explicitly requires the consequence field to be populated before a row may advance — the gate is structural (column present) but not enforced at the exit condition level.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **1** | **1** | **1** | **1** | **1** |

Partial across all: consequence in defeat assessment present, not enforced as an advancement gate in the exit criterion text.

---

#### C-13 — DEFEATED/HOLDS verdict semantics (max 2)

All variations define DEFEATED and HOLDS in the Verdict Vocabulary block with forward-path statements. HOLDS → "no path to Phase 6"; DEFEATED → "advances to Phase 6."

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-14 — NEW/PRIOR split with explicit date anchor (max 2)

All variations: Phase 2 includes "Record STRATEGY DATE as a named field before classification begins. Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE." Explicit inequality stated; strategy date recorded before classification.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-15 — Confidence levels with evidential criteria (max 2)

All variations: Verdict Vocabulary block defines HIGH (≥2 independent NEW artifacts), MEDIUM (1 NEW artifact), LOW (inference only). Countable artifact-independence criteria present for all three tiers.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-16 — Type-labeled nulls for all categories (max 2)

All variations: Phase 4 has all 4 delta-type nulls (CONFIRMED / EXPANDED / UNEXPECTED / CHALLENGED) with category labels. Phase 6 has Null (ADDITIONS), Null-REMOVALS, Null-REPRIORITIZATIONS. All 7 null types present with labels. "Silence is not a null declaration" enforces prohibition on silent omission.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-17 — Bias labels per proposal row and per phase (max 2)

All variations have per-phase "Bias blocked:" annotations (e.g., Phase 2: recency bias; Phase 3: framing bias; Phase 4: confirmation bias). However, no variation includes a "Bias blocked by guard" column in Phase 6 proposal tables (6a and 6b schemas do not have this column). The phase-level annotations satisfy one level; proposal table column is absent across all.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **1** | **1** | **1** | **1** | **1** |

Partial across all: phase-level bias annotations present; proposal table "Bias blocked by guard" column missing.

---

#### C-18 — WITHDRAW operator with row-level semantics (max 2)

All variations: Phase 7 defines WITHDRAW [#] syntax, states it removes only named proposals (remainder applied), explicitly distinguishes from NO (rejects all) and REVISED (requires resubmission).

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-19 — Phase entry/exit conditions (max 2)

All variations define ENTRY CONDITION and EXIT CRITERION for every gated phase (1–8). Each entry condition references the preceding phase's exit criterion by phase number. INERTIA-GATE phases and confirmation gate both carry entry and exit conditions.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-20 — Bias labels at every structural guard (max 2)

All variations label every named guard: INERTIA PRIOR, SCHEMA COMMITMENT, PHASE-1-READ-BARRIER, SIGNAL READ-LOCK, VERDICT SEMANTICS BLOCK, INERTIA-GATE (Sites 1 and 2), CONFIRMATION GATE, WRITE GUARD, WRITE GUARD (confirmed). Every guard site carries an inline bias label.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-21 — Dual-site INERTIA-GATE enforcement (max 2)

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **2** | "Site 1 of 2 -- Phase 5 entry" and "Site 2 of 2 -- Phase 6 entry"; Phase 6 label states "HOLDS exclusion is enforced here without relying on the Phase 5 site to carry the constraint. A reviewer can confirm HOLDS exclusion from this block alone, without reading Phase 5." Independent restatement explicit. |
| **V-02** | **2** | Same dual-site structure and independent restatement as V-01. |
| **V-03** | **0** | Phase 5 has `INERTIA-GATE` and Phase 6 has `INERTIA-GATE (Phase 6 entry)`, but no "Site 1 of 2 / Site 2 of 2" structure; Phase 6 Mechanism references "from Phase 5" without independent self-containment ("Only DEFEATED dimensions from Phase 5 appear here" relies on Phase 5 scope). No independent restatement of the HOLDS exclusion at Phase 6 entry. |
| **V-04** | **2** | "Site 1 of 2 -- Phase 5 entry" and "Site 2 of 2 -- Phase 6 entry"; Phase 6 label has full independent HOLDS exclusion restatement. |
| **V-05** | **2** | Same dual-site structure and independent restatement as V-04. |

---

#### C-22 — Restart isolation clause in Phase 1 read-barrier (max 2)

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **2** | "RESTART ISOLATION: If execution resumes after an interruption without prior context, do NOT re-read strategy.md or any signal file to reconstruct the state of this run. Write the defense register from prior knowledge only. Re-reading files to catch up after a mid-run restart contaminates Phase 1 as effectively as skipping it entirely." Co-located with first-run constraint. |
| **V-02** | **2** | Identical restart clause to V-01. |
| **V-03** | **0** | Phase 1 has FIRST-RUN isolation ("DO NOT read strategy.md or any signal file before Phase 1 is complete") but no RESTART ISOLATION clause. Mid-run restart path is unguarded. |
| **V-04** | **2** | Full restart clause co-located with first-run constraint. |
| **V-05** | **2** | Full restart clause co-located with first-run constraint. |

---

#### C-23 — Dedicated verdict vocabulary block before Phase 5 (max 2)

All variations have a standalone "## Verdict Vocabulary" section positioned after Phase 4 and before Phase 5. Both DEFEATED and HOLDS defined with forward-path statements ("dimension advances to Phase 6" / "no path to Phase 6"). Block structurally separate from phase instructions.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

---

#### C-24 — Structural mechanism spatial separation (max 2)

This is the primary new criterion for R10. Each of the three mechanisms (Phase 1 barrier + restart clause, Verdict Vocabulary block, INERTIA-GATE labels) must occupy independent sections with no cross-contamination.

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **2** | SECTION SCOPE declaration on Phase 1 ("does not contain verdict vocabulary definitions; does not contain INERTIA-GATE exclusion text"), on Verdict Vocabulary ("does not contain Phase 1 read-barrier language; does not contain restart isolation clause text; does not contain INERTIA-GATE exclusion text"), on Phase 5 ("does not redefine verdict semantics; does not contain restart isolation language"). Phase 5 INERTIA-GATE Mechanism stripped of verdict semantic descriptions — contains only "Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have no path to Phase 6." All three mechanisms spatially clean. |
| **V-02** | **0** | Phase 5 INERTIA-GATE block deliberately retains inline verdict semantic descriptions: "HOLDS is the default verdict and requires no evidence; DEFEATED requires specific named signal evidence." Gate-exclusion text and verdict semantics co-located. No SECTION SCOPE declarations present to separate mechanisms. |
| **V-03** | **2** | SECTION SCOPE on Phase 1 ("read-barrier ONLY; does not contain verdict vocabulary definitions; does not contain INERTIA-GATE exclusion text"), on Verdict Vocabulary ("verdict definitions ONLY; does not contain Phase 1 read-barrier language; does not contain INERTIA-GATE exclusion text"), on Phase 5 ("gate-exclusion text and verdict application ONLY; does not redefine verdict semantics; does not contain restart isolation language"), on Phase 6 ("gate-exclusion text and proposal generation ONLY; does not redefine verdict semantics"). Phase 5 INERTIA-GATE Mechanism is clean (gate-exclusion only). Three mechanisms spatially separated. |
| **V-04** | **2** | SECTION SCOPE with MUST NOT CONTAIN prohibitions: Phase 1 "MUST NOT CONTAIN: verdict vocabulary definitions; INERTIA-GATE exclusion text"; Verdict Vocabulary "MUST NOT CONTAIN: Phase 1 read-barrier language; restart isolation clause text; INERTIA-GATE exclusion text"; Phase 5 "MUST NOT CONTAIN: verdict semantic redefinitions; restart isolation language." Prohibitive formulation makes violations structurally detectable. Phase 5 INERTIA-GATE Mechanism is clean. |
| **V-05** | **2** | Heading-level SCOPE annotations: `## Phase 1 [SCOPE: read-barrier and restart clause only -- no verdict vocabulary, no INERTIA-GATE text]`; `## Verdict Vocabulary [SCOPE: verdict definitions only -- no gate labels, no restart text, no phase instructions]`; `## Phase 5 [SCOPE: gate-exclusion and verdict application only -- no verdict redefinitions, no restart language]`; `## Phase 6 [SCOPE: proposal generation only -- DEFEATED dimensions; no verdict redefinitions]`. Spatial separation is verifiable from the document outline without reading section body. Phase 5 INERTIA-GATE Mechanism is clean. |

---

#### C-25 — Phase 5 verdict deferral with anti-duplication clause (max 2)

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **1** | Phase 5: "Apply the Verdict Vocabulary defined above." — forward-reference present. No anti-duplication clause ("Do not redefine here" or equivalent) co-located. Partial per rubric: "Phase 5 forward-references the block but omits the anti-duplication clause." |
| **V-02** | **2** | Phase 5: "Apply the Verdict Vocabulary block defined above. Do not redefine verdict semantics here. Any inline DEFEATED or HOLDS definition appearing in this phase is a structural violation of the single-source guarantee established by the Verdict Vocabulary block." Forward-reference + categorical prohibition. No inline verdict definitions in Phase 5 body. Full pass. |
| **V-03** | **2** | Phase 5: "Apply the Verdict Vocabulary defined above. Do not redefine verdict semantics here. Any inline DEFEATED or HOLDS definition in this phase is a structural violation." Forward-reference + anti-duplication clause. Full pass. |
| **V-04** | **2** | Phase 5: same categorical anti-duplication as V-02, plus SECTION SCOPE "MUST NOT CONTAIN: verdict semantic redefinitions" reinforces single-source at the section boundary. Full pass. |
| **V-05** | **2** | Phase 5: same categorical anti-duplication as V-02, plus heading-level SCOPE annotation explicitly prohibits verdict redefinitions. Full pass. |

---

### Composite Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | 2 | 2 | 2 | 2 | 2 |
| C-10 | 2 | 2 | 2 | 2 | 2 |
| C-11 | 2 | 2 | 2 | 2 | 2 |
| C-12 | 1 | 1 | 1 | 1 | 1 |
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
| **Raw (of 34)** | **31** | **30** | **28** | **32** | **32** |
| **Score (×10/34)** | **9.12** | **8.82** | **8.24** | **9.41** | **9.41** |

**Rank**: V-04 = V-05 (9.41) > V-01 (9.12) > V-02 (8.82) > V-03 (8.24)

---

### Excellence Signals — V-04 / V-05 (Tied Top)

**What makes V-04 better than V-01 (which isolated C-24):**
The full stack (C-21 + C-22 + C-23 + C-24 + C-25) adds 2 points (C-21 full vs V-01's base, C-22 full vs V-01's base) but V-01 already had C-21 and C-22. The marginal gain over V-01 is: C-25 partial (1) → C-25 full (2) = +1 point. V-04's categorical anti-duplication clause lifts C-25 to full pass.

**What makes V-04 better than V-02 (which isolated C-25):**
V-02's deliberate C-24 failure costs 2 points. The spatial cleanup (removing verdict semantics from Phase 5 INERTIA-GATE) is the decisive move.

**V-04 vs V-05 tie analysis:**
Both achieve 32/34. Heading-level SCOPE annotation (V-05) makes spatial separation verifiable from the document outline without reading section body — a stronger auditor signal — but C-24 full pass is binary (2/2) for both. No scoring mechanism gives V-05 a marginal advantage over V-04 under this rubric. Both are equally production-ready; V-05 is preferred if outline-verifiability is operationally important.

**Chronic partial criteria (shared gap across all variations):**
- **C-12 (1/2)**: Consequence column present in defeat assessment; Phase 5 EXIT CRITERION does not explicitly block row advancement if the field is unpopulated.
- **C-17 (1/2)**: Per-phase bias annotations present; "Bias blocked by guard" column absent from Phase 6 proposal tables.

These two criteria represent the next promotion frontier — both are structural additions to existing phases, orthogonal to C-24/C-25.

---

```json
{"top_score": 9.41, "all_essential_pass": true, "new_patterns": ["Heading-level SCOPE annotation in section headings makes spatial separation verifiable from document outline without reading body text — a reviewer scanning headers can confirm each section's declared scope before encountering body content", "MUST NOT CONTAIN prohibition format in SECTION SCOPE blocks names what is explicitly forbidden rather than only what is contained, making violations structurally detectable by citing the prohibition directly"]}
```
