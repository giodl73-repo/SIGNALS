# mock-accept Round 4 — Scorecard

**Rubric version:** v4 | **Date:** 2026-03-16
**Denominator:** 11 aspirational | **Ceiling:** 103.75

---

## Scoring Basis

All R4 variations carry the R3 V-05 base intact: SKIP table, Slot-2-first ordering, ARCH-GUARD-BYPASS + STRATEGY-TO-PM-GUARD-BYPASS bypass-error-codes, two-list partition with explicit empty records, CANARY GATE two-branch structure, VERDICT-ECHO Error-code field, CANARY SUPPRESSED prose reframe, non-conflation prose sentence.

Differentiation is entirely in C-17, C-18, C-19.

---

## V-01 — Lifecycle Emphasis: `Semantics:` Labeled Field in BRANCH B

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 — FORBIDDEN OUTPUTS TRIAD + completeness check | PASS | All three labels present; "A two-of-three set does not satisfy this gate." explicit |
| C-02 — Triad labels all labeled | PASS | [EVIDENCE-HEAVY] [TIER-CRITICAL] [COMPLIANCE] present |
| C-03 — Status written back with CANARY ASSERTION | PASS | Step 8 Edit tool invocation; BRANCH A / BRANCH B mutually exclusive |
| C-04 — Review artifact with required structure | PASS | Step 7: Coverage Review table, P1/P2/P3 next-steps, cross-namespace risk + urgency |
| C-05 — MOCK-ACCEPTED two-slot positive argument | PASS | SLOT 2 (Contrast) written first; exact reason codes; Slot 1 anchored to SQ-1 |
| C-06 — Entity-naming grammar on sub-questions | PASS | "Yes/no answers do not satisfy entity-naming sub-question requirements." |
| C-07 — Step sequencing + guard compliance | PASS | Both blocked-list records required; bypass-error-codes named at guard sites |
| C-08 — Evaluation-driven REAL-REQUIRED template | PASS | trigger / Failing evaluation / Failing verdict / Claim + Error-code / Artifact state all present |
| C-09–C-16 (R3 base, 8 criteria) | PASS ×8 | Carried forward from R3 V-05 |
| **C-17 — CANARY SUPPRESSED as labeled Semantics field** | **PASS** | `Semantics: SUCCESS — this is the correct disclosure output, not an error or failure mode.` as parseable field in BRANCH B |
| **C-18 — Dedicated non-conflation structure** | **PARTIAL** | `Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression.` present as prose inside BRANCH B — non-conflation named but no dedicated table with separate Type column per term |
| **C-19 — Subject-check metacognitive step on Error-code** | **PARTIAL** | Error-code field with Note form carried from R3 base — conditional present but no explicit `Subject-check:` sub-step before emission; NONE branch is passive application, not deliberate result |

**Essential:** 60 / 60 | **Recommended:** 30 / 30
**Aspirational:** 8 × 1.25 + 1.25 (C-17) + 0.625 (C-18) + 0.625 (C-19) = **12.5**
**Composite: 102.5**

---

## V-02 — Output Format: CANARY TERMINOLOGY TABLE Before Branches

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Identical to V-01 base |
| C-09–C-16 | PASS ×8 | R3 base carried forward |
| **C-17 — CANARY SUPPRESSED labeled Semantics field** | **PARTIAL** | BRANCH B states "CANARY SUPPRESSED is not an error — it is the correct disclosure output when edits are incomplete" as prose; no `Semantics:` field; positive reframe present but not parseable as labeled declaration |
| **C-18 — Dedicated non-conflation structure** | **PASS** | CANARY TERMINOLOGY TABLE inserted before BRANCH A/B: 2 rows with Term / Type / Meaning columns; CANARY SUPPRESSED → "Correct output"; CANARY-FALSE-POSITIVE → "Named error"; Type column forces per-term categorical distinction, not summarizable in a single sentence |
| **C-19 — Subject-check metacognitive step** | **PARTIAL** | Error-code with Note form from R3 base; no Subject-check sub-step |

**Essential:** 60 / 60 | **Recommended:** 30 / 30
**Aspirational:** 8 × 1.25 + 0.625 (C-17) + 1.25 (C-18) + 0.625 (C-19) = **12.5**
**Composite: 102.5**

---

## V-03 — Phrasing Register: Metacognitive `Subject-check:` on Error-code

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Identical to base; C-08 strengthened by Subject-check but base still satisfies criterion |
| C-09–C-16 | PASS ×8 | R3 base carried forward |
| **C-17 — CANARY SUPPRESSED labeled Semantics field** | **PARTIAL** | BRANCH B prose: "CANARY SUPPRESSED is not an error — it is the correct disclosure output when edits are incomplete." No `Semantics:` field |
| **C-18 — Dedicated non-conflation structure** | **PARTIAL** | `Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression.` as inline prose in BRANCH B; no table |
| **C-19 — Subject-check metacognitive step** | **PASS** | `Subject-check:` sub-step inserted before Error-code field: explicit `If subject = role name → VERDICT-ECHO` / `If subject = artifact, section, or field → NONE` conditional; Error-code value references Subject-check result; NONE branch is deliberate, not default |

**Essential:** 60 / 60 | **Recommended:** 30 / 30
**Aspirational:** 8 × 1.25 + 0.625 (C-17) + 0.625 (C-18) + 1.25 (C-19) = **12.5**
**Composite: 102.5**

---

## V-04 — Combination: Semantics Field + Terminology Table (C-17 + C-18)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Identical to base |
| C-09–C-16 | PASS ×8 | R3 base carried forward |
| **C-17 — CANARY SUPPRESSED labeled Semantics field** | **PASS** | BRANCH B: `Semantics: SUCCESS — this is the correct disclosure output, not an error or failure mode.` as labeled field; positive reframe is checkable, not only searchable prose |
| **C-18 — Dedicated non-conflation structure** | **PASS** | CANARY TERMINOLOGY TABLE before branches: 2 rows / 3 columns; structural non-conflation; inline "Do NOT conflate them." follows table as enforcement note |
| **C-19 — Subject-check metacognitive step** | **PARTIAL** | Error-code with Note form from R3 base; no Subject-check sub-step; NONE branch is passive application |

**Essential:** 60 / 60 | **Recommended:** 30 / 30
**Aspirational:** 8 × 1.25 + 1.25 (C-17) + 1.25 (C-18) + 0.625 (C-19) = **13.125**
**Composite: 103.1**

---

## V-05 — Full R4 Integration: C-17 + C-18 + C-19

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Full base; all phase gates, triad, templates intact |
| C-09–C-16 | PASS ×8 | R3 base carried forward |
| **C-17 — CANARY SUPPRESSED labeled Semantics field** | **PASS** | BRANCH B: `Semantics: SUCCESS — this is the correct disclosure output, not an error or failure mode.` — labeled parseable field; positive reframe is a distinct checkable declaration |
| **C-18 — Dedicated non-conflation structure** | **PASS** | CANARY TERMINOLOGY TABLE before branches; 2 rows: CANARY SUPPRESSED → "Correct output" / CANARY-FALSE-POSITIVE → "Named error"; Type column forces categorical distinction independent of surrounding prose |
| **C-19 — Subject-check metacognitive step** | **PASS** | `Subject-check:` sub-step in STEP 6 REAL-REQUIRED template: explicit subject identification before Error-code emission; NONE branch fires only when Subject-check identifies artifact as subject — deliberate result, not fallback; VERDICT-ECHO examples and NONE examples anchor both branches |

**Essential:** 60 / 60 | **Recommended:** 30 / 30
**Aspirational:** 8 × 1.25 + 1.25 + 1.25 + 1.25 = **13.75** (ceiling)
**Composite: 103.75**

---

## Ranking

| Rank | Variation | Score | C-17 | C-18 | C-19 |
|------|-----------|-------|------|------|------|
| 1 | **V-05** | **103.75** | PASS | PASS | PASS |
| 2 | V-04 | 103.1 | PASS | PASS | PARTIAL |
| 3 (tie) | V-01 | 102.5 | PASS | PARTIAL | PARTIAL |
| 3 (tie) | V-02 | 102.5 | PARTIAL | PASS | PARTIAL |
| 3 (tie) | V-03 | 102.5 | PARTIAL | PASS | PARTIAL |

---

## Excellence Signals from V-05

**Pattern A — Prose-to-labeled-field promotion:** `Semantics: SUCCESS` converts the CANARY SUPPRESSED positive reframe from a searchable sentence into a parseable structural declaration. The field can be checked by position, not by text search through prose. This is the most direct mechanism for making a behavioral intention machine-verifiable.

**Pattern B — Pre-branch terminology table with Type column:** Inserting a 2-row structured table before BRANCH A/B definitions forces per-term categorical separation (Correct output vs. Named error). A prose non-conflation sentence can be paraphrased into a summary that merges both terms; a table with an explicit Type column cannot. The table functions as a machine-readable contract preceding the branching logic that depends on it.

**Pattern C — Metacognitive sub-step before conditional field emission:** `Subject-check:` before `Error-code:` converts a passive field application into an active deliberate test. The model must identify the grammatical subject of its Claim sentence, then emit the error-code as a function of that identification. NONE becomes an affirmative statement ("artifact is subject → NONE") rather than a default. This pattern generalizes: any conditional field that is typically filled by default benefits from a named sub-step that forces the condition to be evaluated explicitly before emission.

---

```json
{"top_score": 103.75, "all_essential_pass": true, "new_patterns": ["Semantics: SUCCESS as labeled parseable field in BRANCH B promotes positive reframe from prose to checkable structural declaration", "Pre-branch CANARY TERMINOLOGY TABLE with Type column forces per-term categorical distinction that cannot be collapsed into a single sentence", "Subject-check: metacognitive sub-step before Error-code emission converts NONE branch from passive default to explicit deliberate result of subject identification"]}
```
