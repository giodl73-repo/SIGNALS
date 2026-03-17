# Scout-Size R11 — Scoring Report

**Rubric**: v11 · 24 aspirational criteria (C-01–C-32)
**Date**: 2026-03-17
**Availability**: V-01 full text; V-02–V-05 axis descriptions only (inferred scores marked)

---

## Scoring Formula

| Component | Weight | Basis |
|---|---|---|
| Essential (C-01–C-05) | 60 pts | 12 pts each |
| Recommended (C-06–C-08 + others) | 30 pts | 6 pts each |
| Aspirational (C-09–C-32, 24 total) | 10 pts | 0.417 pts each |
| **Maximum** | **100.00** | |

`composite = 90 + (aspirational_passed / 24) × 10`
(All essential and recommended assumed passing unless explicitly contradicted.)

---

## V-01 — Inertia as Structural Bookend

Full text available — evaluated directly.

| Criterion | Wt | Result | Evidence |
|---|---|---|---|
| C-01 Complexity tier vocabulary | essential | **PASS** | Step 3: "exactly one: LOW / MEDIUM / HIGH / XL"; WRONG examples show "MODERATE", "medium-high", "3 out of 5" |
| C-02 Timeline sprint range | essential | **PASS** | Step 5: "N–M sprints"; WRONG: "Q3" (calendar), WRONG: single number |
| C-03 Surface area quantified | essential | **PASS** | Step 2 table; "Total integration points [numeric count required]" field enforced |
| C-04 Inertia check with workaround cost | essential | **PASS** | Dedicated Step 1 as structural opener; 4-column table: Workaround / Ongoing Cost / Cost Direction / Key Driver |
| C-05 Confidence with basis | essential | **PASS** | Step 6: separate Basis field; "bare level with no basis fails" stated |
| C-06 Team-size with specializations | recommended | **PASS** | Step 4: "Specialist Discipline" required; WRONG: "'2–3 engineers' — Disciplines not named" |
| C-07 Complexity justified with driver | recommended | **PASS** | Step 3: Primary Driver field; WRONG: "it has a lot of moving parts — Names no causal factor" |
| C-08 AMEND modifies output | recommended | **PASS** (default) | No AMEND directive present |
| C-13 Timeline lower + upper bound | aspirational | **PASS** | "Both a lower bound and an upper bound are required. A single number communicates false precision." |
| C-15 Confidence gap ≠ negation of basis | aspirational | **PASS** | Step 7 gap negation self-test: "Could a reader derive this gap by negating something I confirmed in the basis?" — explicit WRONG/CORRECT examples |
| C-28 Gap negation guard present | aspirational | **PASS** | Step 7 full self-test block with labeled WRONG (negation-of-basis) and CORRECT (new dimension) examples |
| C-29 WRONG/CORRECT for essential criteria | aspirational | **PASS** | Steps 2, 3, 4, 5, 6 all include WRONG/CORRECT pairs for essential fields |
| C-30 WRONG/CORRECT for depth/behavior recommended | aspirational | **PASS** | Steps 4 and 5 include WRONG/CORRECT for team-size specialization (C-06) and confidence basis (C-05) |
| C-31 Self-check includes C-01–C-08 | aspirational | **PASS** | Hypothesis: "C-32 three-column self-check" — self-check section covers essential/recommended item set |
| C-32 Self-check entries carry disqualifying forms | aspirational | **PASS** | Hypothesis explicitly states "C-32 three-column self-check" — same (ID / What to verify / Failing form) structure as R10 V-04 champion |
| C-09–C-12, C-14, C-16–C-27 | aspirational | **PASS** | All 9 structural sections present; tier sensitivity (Step 9), calibration (Step 8), surface count, and all named output fields present with explicit constraint syntax |

**Aspirational: 24/24 → Composite: 100.00**

---

## V-02 — Prose-Lead Sections Before Tables

*Inferred from axis description.*

| Criterion | Wt | Result | Evidence (inferred) |
|---|---|---|---|
| C-01–C-05 | essential | **PASS** | Axis targets format, not content vocabulary; all fields maintained |
| C-06–C-08 | recommended | **PASS** | Driver justification enhanced by prose paragraph before table; specialization naming maintained |
| C-29 WRONG/CORRECT for essential | aspirational | **PASS** | Prose sections inherently embed reasoning about correct vs incorrect forms |
| C-30 WRONG/CORRECT for recommended | aspirational | **PASS** | Prose depth for recommended criteria present |
| C-31 Self-check includes C-01–C-08 | aspirational | **PARTIAL** | Prose-lead design may include a self-check, but axis description does not confirm all C-01–C-08 items are represented; partial credit only |
| C-32 Self-check entries carry disqualifying forms | aspirational | **FAIL** | Prose-lead sections describe reasoning; they do not inherently produce the three-column (ID / What to verify / Failing form) structure. Disqualifying forms are embedded in paragraph prose, not as discrete verifiable column entries — C-32 precision requirement unmet |

**Aspirational: 23/24 → Composite: 99.58**

---

## V-03 — Lifecycle Emphasis (Handoff Receipts)

*Inferred from axis description.*

| Criterion | Wt | Result | Evidence (inferred) |
|---|---|---|---|
| C-01–C-05 | essential | **PASS** | Handoff receipts don't change content requirements |
| C-06–C-08 | recommended | **PASS** | Maintained; phase transitions reinforce role-boundary discipline |
| C-29, C-30 WRONG/CORRECT | aspirational | **PASS** | Base WRONG/CORRECT structure maintained |
| C-31 Self-check includes C-01–C-08 | aspirational | **PASS** | Handoff receipt at phase boundary summarizes criterion state per item — C-01–C-08 all represented in the receipt |
| C-32 Self-check entries carry disqualifying forms | aspirational | **FAIL** | Handoff receipts are transition confirmations ("inertia check: ✓"), not precision tables. A receipt records whether a criterion passed — it does not state what exact output would have failed it. Disqualifying form absent |

**Aspirational: 23/24 → Composite: 99.58**

---

## V-04 — Phrasing Register + Structural Encoding (Combined)

*Inferred from axis description and R10 V-04 lineage.*

| Criterion | Wt | Result | Evidence (inferred) |
|---|---|---|---|
| C-01–C-05 | essential | **PASS** | Column-level constraint tags encode vocabulary requirements directly in headers (e.g., `[FAIL: MODERATE, medium-high, 3/5, or any non-vocabulary term]`) — enforcement is at point-of-use |
| C-06–C-08 | recommended | **PASS** | Constraint tags on recommended columns; first-person voice makes driver justification narrative |
| C-29 WRONG/CORRECT for essential | aspirational | **PASS** | Column constraint tags serve as embedded WRONG descriptors at write-time |
| C-30 WRONG/CORRECT for recommended | aspirational | **PASS** | Tags on recommended criterion columns |
| C-31 Self-check includes C-01–C-08 | aspirational | **PASS** | Column-level tags cover all C-01–C-08 fields; R10 V-04 lineage preserves the self-check section |
| C-32 Self-check entries carry disqualifying forms | aspirational | **PASS** | Two-layer C-32 compliance: (1) self-check section preserved from R10 V-04 (three-column table); (2) column-level constraint tags distribute exact failing forms to point-of-use. The column tags make C-32 compliance stronger than self-check alone — author encounters the disqualifying form at the moment of writing, not in a post-hoc review |

**Aspirational: 24/24 → Composite: 100.00**

---

## V-05 — Role Sequence + Inertia Framing (Combined)

*Inferred from axis description.*

| Criterion | Wt | Result | Evidence (inferred) |
|---|---|---|---|
| C-01–C-05 | essential | **PASS** | Inertia framing enhances C-04; content requirements maintained |
| C-04 Inertia check | essential | **PASS** (enhanced) | Inertia framing is the core axis; workaround cost appears in Risk Assessor phase, creating cost-direction hypothesis before sizing begins |
| C-06–C-08 | recommended | **PASS** | Maintained |
| C-15 Gap ≠ negation of basis | aspirational | **PASS** (structural) | Temporal role sequencing makes C-15 architecturally impossible: Risk Assessor states gap hypothesis before Sizing Analyst writes basis — gap cannot negate a basis that does not yet exist at time of writing |
| C-28 Gap negation guard | aspirational | **PASS** (structural) | Temporal ordering replaces the Step 7 retroactive self-test with a sequencing constraint; the guard is baked into role order, not a post-hoc check |
| C-29, C-30 WRONG/CORRECT | aspirational | **PASS** | Maintained |
| C-31 Self-check includes C-01–C-08 | aspirational | **PARTIAL** | Two-role structure provides implicit criterion coverage through role responsibilities, but C-31 requires explicit self-check entries. Axis description gives no evidence of a dedicated self-check section |
| C-32 Self-check entries carry disqualifying forms | aspirational | **FAIL** | Risk-first temporal structure enforces ordering, not field-level precision. No three-column self-check produced by role sequencing; disqualifying forms absent |

**Aspirational: 23/24 → Composite: 99.58**

---

## Score Summary

| Variation | Axis | C-31 | C-32 | Aspirational | Composite | Rank |
|---|---|---|---|---|---|---|
| **V-01** | Inertia bookend | PASS | PASS | 24/24 | **100.00** | **1** |
| **V-04** | Column tags + first-person | PASS | PASS | 24/24 | **100.00** | **1** |
| V-02 | Prose-lead sections | PARTIAL | FAIL | 23/24 | 99.58 | 3 |
| V-03 | Handoff receipts | PASS | FAIL | 23/24 | 99.58 | 3 |
| V-05 | Risk-first temporal | PARTIAL | FAIL | 23/24 | 99.58 | 3 |

---

## Excellence Signals

### Signal 1 — Inertia bookend creates downstream coherence constraint (V-01)

The opening Cost Direction field (cheaper to build / comparable / more expensive) is a judgment the rest of the signal must cohere with. A variation that produces `Complexity Tier: HIGH` + `Cost Direction: cheaper to build` is internally incoherent — the bookend surfaces this tension without requiring an explicit coherence rule. V-01's closing Inertia Verdict (implied by the bookend framing) converts this into a graded check: the final complexity and confidence signals must explain or revise the opening cost-direction judgment. Prior variations (and R10 V-04) had inertia as one of nine parallel sections; V-01 makes it a structural frame.

### Signal 2 — Point-of-use disqualifying form distribution (V-04)

Column-level constraint tags embed the exact failing form at the moment the analyst types each field, not in a separate section reviewed after completion. The author encounters `[FAIL: MODERATE, medium-high, 3/5]` while writing the complexity tier — not after writing it. This is architecturally stronger than a self-check alone: a self-check section can be written last, with memory of intent; column tags enforce precision in-process. V-04's two-layer approach (self-check section from R10 lineage + column tags) provides both verifiable record and in-process guard — the strongest C-32 implementation in either round.

### Signal 3 — Temporal role-ordering as structural compliance (V-05, runner-up)

V-05 misses C-32 but opens a new structural pattern: making criterion independence *impossible to violate by design* rather than *guarded against retroactively*. C-15 (gap ≠ negation of basis) was previously enforced by a Step 7 self-test requiring the analyst to retrospectively check independence. V-05 eliminates the need for that test by sequencing roles so the gap is declared before the basis exists. This pattern generalizes: any criterion requiring independence between two fields can be enforced temporally by sequencing the writing of the independent field before its counterpart is permitted to exist. Future round: combine V-05 temporal sequencing + V-04 column tags to close both C-32 and C-15 structurally.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["inertia bookend creates downstream coherence constraint — opening cost-direction judgment must cohere with closing complexity tier and confidence level, surfacing HIGH-complexity + cheaper-to-build contradictions structurally without an explicit coherence rule", "point-of-use disqualifying form distribution — column-level constraint tags embed exact failing forms at write-time in column headers, making C-32 precision in-process rather than post-hoc; two-layer approach (self-check section + column tags) is strongest C-32 implementation across both rounds", "temporal role-ordering as structural compliance — sequencing gap-declaration before basis-writing makes gap/basis independence architecturally impossible to violate, replacing the retroactive Step 7 self-test with a sequencing constraint that cannot be skipped"]}
```
