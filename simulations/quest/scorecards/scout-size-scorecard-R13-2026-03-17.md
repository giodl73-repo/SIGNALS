## R13 Scorecard — scout-size

**v13 champion achieved.** V-05 is the first variation to score **100.00**.

### Summary

| Rank | Variation | Score | New criteria |
|------|-----------|-------|--------------|
| **1** | **V-05** | **100.00** | C-36 + C-37 + C-38 |
| 2 | V-04 | 99.67 | C-37 + C-38 |
| 3 (tie) | V-01/V-02/V-03 | 99.33 | One each |

### How V-05 won

V-04 was at 99.67 (29/30 — C-36 PARTIAL, C-37 PASS, C-38 PASS). The single gap: **Tier-Destination column** used `[must differ: LOW / MEDIUM / HIGH / XL]` instead of `[FAIL: same tier as current, MODERATE, non-vocabulary...]`. V-05 fixes this, completing full `[FAIL:]` tag coverage on all six vocabulary-constrained column families.

### Three new patterns extracted

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Role-attributed PHASE SEALED confirmation blocks -- each phase seal names the role ('The Inertia Analyst confirms', 'The Sizing Analyst confirms', 'The Risk Assessor confirms'), reinforcing charter governance at every phase transition rather than only at charter declaration", "Tier-Destination column carries [FAIL: same tier as current, MODERATE, non-vocabulary] tag -- the specific gap between C-36 PARTIAL and PASS is the Tier-Destination field; 'must differ' phrasing without [FAIL:] prefix is insufficient", "Non-access rule in Phase 2 enumerates all prohibited gap candidates explicitly -- augments the self-test with a positive disqualification list, preventing basis-negation gaps structurally rather than behaviorally"]}
```
terion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Team-size names specializations | PASS | PASS | PASS | PASS | PASS |
| C-07 | Complexity justified with >=1 driver | PASS | PASS | PASS | PASS | PASS |
| C-08 | AMEND changes output (default PASS if absent) | PASS | PASS | PASS | PASS | PASS |

Evidence: All variations include Team-Size Signal with Specialist Discipline + Implementation
Ownership columns (C-06, C-11). Primary Driver column in Complexity section (C-07). No AMEND
invoked -- C-08 default PASS.

---

## Aspirational Criteria -- Baseline Block (C-09 through C-35)

All variations: **27/27 PASS** on baseline criteria.

| Range | Criteria | Status |
|-------|----------|--------|
| C-09/C-10 | PRE-FLIGHT GATE has Out-of-scope boundary and Break-even signal fields | PASS all |
| C-11 | Team-Size has Implementation Ownership column | PASS all |
| C-12 | Confidence Gap (Phase 2) names specific unknown | PASS all |
| C-13/C-15 | Synthesis has structured commitment chain; hypothesis committed in PRE-FLIGHT GATE | PASS all |
| C-14 | Open Unknowns section: Unknown / Impact / Movement fields | PASS all |
| C-17/C-27 | FAILURE MODE labeled blocks in Synthesis and Open Unknowns | PASS all |
| C-18/C-21 | PRE-FLIGHT GATE precedes all analysis sections; requires Tier + Timeline commitment | PASS all |
| C-19/C-20 | Surface Area, Complexity, Synthesis each carry scope exclusion prohibition; Synthesis closes Open Unknowns | PASS all |
| C-22/C-23/C-24/C-25 | Synthesis names PRE-FLIGHT GATE at anchor and verdict; prohibitions name canonical home; structured commitment chain trace; enforcement contract forward-references downstream sections | PASS all |
| C-26 | Synthesis carries STRUCTURAL AMEND RE-EVALUATION DIRECTIVE written rule | PASS all |
| C-28 through C-32 | Full self-check table with all criteria by ID; disqualifying forms for structural + depth + behavior + essential + recommended criteria | PASS all |
| C-33 | Phase 0 (Inertia Analyst) precedes Phase 1 in document order | PASS all |
| C-34 | Inertia entry: Workaround / Ongoing Cost / Cost Direction / Key Driver (4-field minimum) | PASS all |
| C-35 | [FAIL:] tags on Complexity Tier and Timeline column headers | PASS all |

---

## New Criteria (C-36, C-37, C-38) -- Per Variation

### C-37 -- 5-field inertia with Cost Trajectory (shape vocabulary: accelerating / stable / plateauing / reversing)

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PASS** | Phase 0 table has Cost Trajectory column: `[FAIL: "+~20%/quarter" without shape label, "worsening" alone, direction statement without shape, any non-vocabulary term -- exactly one: accelerating / stable / plateauing / reversing]`. Phase 0 SEALED confirms shape vocabulary with embedded disqualifying form. Direction and Trajectory are structurally separate columns. |
| V-02 | **FAIL** | Intentional single-axis design: 4-field inertia (Workaround, Cost, Cost Direction, Key Driver). No Cost Trajectory column. Self-check confirms: "4-field inertia -- C-37 intentionally absent." |
| V-03 | **FAIL** | Intentional single-axis design: 4-field inertia. No Cost Trajectory column. Self-check: "FAIL -- single-axis." |
| V-04 | **PASS** | Phase 0 table has Cost Trajectory column with [FAIL:] tag. Phase 0 SEALED embeds: "FAIL: '+~20%/quarter' without shape label; 'worsening' (directional, not shape); 'getting worse' (directional, not shape); Direction and Trajectory in single combined field." |
| V-05 | **PASS** | Phase 0 table Cost Trajectory: `[FAIL: "+~20%/quarter" alone without shape label; "worsening" alone; "getting worse"; Direction+Trajectory in single field; any term not in shape vocabulary -- exactly one: accelerating / stable / plateauing / reversing]`. Phase 0 SEALED adds "growing" as additional disqualifying form. Output Compilation labels trajectory explicitly: `[trajectory: accelerating/stable/plateauing/reversing]`. Three-layer enforcement. |

### C-36 -- Constraint tags cover ALL vocabulary-constrained column headers

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PARTIAL** | Cost Direction, Cost Trajectory, Complexity Tier, Timeline tagged. Confidence Level tagged. Tier-Destination: `[must differ from current: LOW / MEDIUM / HIGH / XL]` -- has vocabulary specification but lacks `[FAIL:]` prefix format. Self-check acknowledges "Tier-Destination untagged" -- PARTIAL. |
| V-02 | **PASS** | Explicitly designed for C-36. Tags on: Complexity Tier, Timeline, Confidence Level, Cost Direction, Tier-Destination `[FAIL: same as current, MODERATE, non-vocabulary...]`, FTE. Every appearing vocab-constrained column carries [FAIL:] tag. Note: 4-field inertia means no Cost Trajectory column appears, so C-36 is satisfied for all appearing fields. |
| V-03 | **PARTIAL** | Complexity Tier and Timeline tagged; Cost Direction tagged; Confidence Level `[FAIL: MEDIUM-HIGH, 3/5, "acceptable"...]` tagged. Tier-Destination: `[must differ: LOW / MEDIUM / HIGH / XL]` -- lacks [FAIL:] format. Self-check: "PARTIAL." |
| V-04 | **PARTIAL** | Complexity Tier, Timeline, Confidence Level, Cost Direction, Cost Trajectory, FTE all carry [FAIL:] tags. Tier-Destination: `[must differ: LOW / MEDIUM / HIGH / XL]` -- uses "must differ" phrasing without `[FAIL:]` prefix. C-36 requires every vocab-constrained field in [FAIL:] format; Tier-Destination gap -> PARTIAL. |
| V-05 | **PASS** | Exhaustive coverage. Tier-Destination: `[Sizing Analyst -- FAIL: same tier as current, MODERATE, non-vocabulary -- must differ from current: LOW / MEDIUM / HIGH / XL]`. Output Compilation also tags Tier-Up/Down: `[FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL]`. All six vocabulary-constrained column families carry [FAIL:] tags with exact disqualifying forms. |

### C-38 -- PHASE SEALED blocks at end of each phase (min 3 specific items per block)

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | Phase 0 SEALED present (5 items, specific fields, disqualifying forms). Phase 1 and Phase 2: verbal handoffs only -- no SEALED blocks. Self-check: "FAIL -- single-axis; V-01 tests C-37 only." C-38 requires SEALED at Phase 0, 1, AND 2. |
| V-02 | **FAIL** | No PHASE SEALED blocks. Intentional: Steps 1-9 flow without phase seals. Self-check: "No PHASE SEALED -- C-38 intentionally absent. FAIL -- single-axis." |
| V-03 | **PASS** | Phase 0 SEALED: 4 items, each embedding exact disqualifying forms (e.g., `FAIL: "neutral", "similar", "a wash", "worsening", "improving", "increasing cost", "moderate impact", any non-vocabulary paraphrase`). Phase 1 SEALED: 9 items with disqualifying forms. Phase 2 SEALED: 3 items with disqualifying forms. All items name specific fields, not generic completion language. |
| V-04 | **PASS** | Phase 0 SEALED: 5 items (all inertia fields including Cost Trajectory) with disqualifying forms. Specifically embeds: "FAIL: '+~20%/quarter' without shape label; 'worsening' (directional, not shape); 'getting worse' (directional, not shape); Direction and Trajectory in single combined field." Phase 1 SEALED: 9 items. Phase 2 SEALED: 4 items (adds "self-test applied" confirmation). Three SEALED blocks with specific fields and embedded disqualifying forms. |
| V-05 | **PASS** | Phase 0 SEALED attributed to role: "The Inertia Analyst confirms ALL before Phase 1 opens." 5 items with disqualifying forms; adds "growing" as form beyond V-04. Phase 1 SEALED: "The Sizing Analyst confirms ALL" -- 9 items. Phase 2 SEALED: "The Risk Assessor confirms ALL" -- 4 items. Role-attributed SEALED blocks reinforce charter governance at every phase transition. |

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (/30) | Composite | Band |
|-----------|---------------|------------------|--------------------|-----------|------|
| V-01 | 60 (5/5) | 30 (3/3) | 9.33 (28/30) | **99.33** | Gold |
| V-02 | 60 (5/5) | 30 (3/3) | 9.33 (28/30) | **99.33** | Gold |
| V-03 | 60 (5/5) | 30 (3/3) | 9.33 (28/30) | **99.33** | Gold |
| V-04 | 60 (5/5) | 30 (3/3) | 9.67 (29/30) | **99.67** | Gold |
| **V-05** | 60 (5/5) | 30 (3/3) | **10.00 (30/30)** | **100.00** | **Gold -- v13 Champion** |

Aspirational breakdown:
- V-01: baseline 27 + C-37 PASS = 28 (C-36 PARTIAL = 0; C-38 FAIL = 0)
- V-02: baseline 27 + C-36 PASS = 28 (C-37 FAIL = 0; C-38 FAIL = 0)
- V-03: baseline 27 + C-38 PASS = 28 (C-36 PARTIAL = 0; C-37 FAIL = 0)
- V-04: baseline 27 + C-37 + C-38 = 29 (C-36 PARTIAL = 0)
- V-05: baseline 27 + C-36 + C-37 + C-38 = 30

---

## Ranking

| Rank | Variation | Score | New criteria achieved |
|------|-----------|-------|-----------------------|
| 1 | **V-05** | 100.00 | C-36 + C-37 + C-38 |
| 2 | V-04 | 99.67 | C-37 + C-38 |
| 3 (tie) | V-01 | 99.33 | C-37 |
| 3 (tie) | V-02 | 99.33 | C-36 |
| 3 (tie) | V-03 | 99.33 | C-38 |

**V-05 is the v13 champion. First variation to achieve 30/30 aspirational = 100.00 composite.**

---

## Excellence Signals -- V-05 (patterns new to R13)

### Signal 1: Role-attributed PHASE SEALED confirmation blocks

V-05 attributes each SEALED block to the role that owns the phase:
- "The Inertia Analyst confirms ALL before Phase 1 opens."
- "The Sizing Analyst confirms ALL before Phase 2 opens."
- "The Risk Assessor confirms ALL before Output Compilation."

V-03 and V-04 had SEALED blocks using generic "confirm ALL" framing. The role attribution makes
phase-boundary enforcement structurally consistent with the charter model throughout the document
-- not just at the charter declaration site. Each role seals its own phase; no other role's
confirmation language appears at that boundary.

### Signal 2: Tier-Destination [FAIL:] tag with exact disqualifying forms closes the C-36 last gap

The specific innovation separating V-05 (C-36 PASS) from V-04 (C-36 PARTIAL):

- V-04: `[must differ: LOW / MEDIUM / HIGH / XL]` -- correct vocabulary, wrong format
- V-05: `[Sizing Analyst -- FAIL: same tier as current, MODERATE, non-vocabulary -- must differ from current: LOW / MEDIUM / HIGH / XL]` -- [FAIL:] format with exact disqualifying forms

V-02 R12 achieved C-36 without this because Cost Trajectory column didn't appear (4-field inertia).
V-05 R13 is the first variation to tag both Cost Trajectory AND Tier-Destination simultaneously in
[FAIL:] format, completing full vocabulary-constraint coverage.

### Signal 3: Non-access rule with explicit prohibited items enumeration for Phase 2

V-05 adds a "Non-access rule" block in Phase 2:
"Prohibited from citing as the gap: integration points Phase 1 enumerated, contracts Phase 1
confirmed, complexity drivers Phase 1 named, team/timeline signals Phase 1 produced, inertia
dimensions Phase 0 established."

The self-test remains, but the enumeration creates a positive disqualification list. This prevents
basis-negation gaps structurally (by naming all prohibited sources) rather than behaviorally
(by relying solely on the self-test question). Phase 2 in prior variations depended entirely on
the self-test to catch charter violations.

---

## JSON Summary

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Role-attributed PHASE SEALED confirmation blocks -- each phase seal names the role ('The Inertia Analyst confirms', 'The Sizing Analyst confirms', 'The Risk Assessor confirms'), reinforcing charter governance at every phase transition rather than only at charter declaration", "Tier-Destination column carries [FAIL: same tier as current, MODERATE, non-vocabulary] tag -- the specific gap between C-36 PARTIAL and PASS is the Tier-Destination field; 'must differ' phrasing without [FAIL:] prefix is insufficient", "Non-access rule in Phase 2 enumerates all prohibited gap candidates explicitly -- augments the self-test with a positive disqualification list, preventing basis-negation gaps structurally rather than behaviorally"]}
```
