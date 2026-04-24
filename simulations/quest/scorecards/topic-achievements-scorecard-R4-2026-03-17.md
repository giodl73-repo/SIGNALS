# Quest Scorecard — corps-achievements (Round 4, v4 Rubric)

**Date**: 2026-03-17
**Skill**: topic-achievements
**Rubric**: v4 (C-01–C-17, 9 aspirational)

---

## Scoring Assumptions

C-08 and C-10–C-13 are not shown in the rubric extract. Assumed from context:

| Criterion | Assumption |
|-----------|------------|
| C-08 | Falsified contract contains all three required components (consequence clause, evasion surface, floor declaration) |
| C-10 | CLASSIFY step/gate produces explicit intermediate output before state assignment |
| C-11 | Evasion surface is explicitly named in the contract |
| C-12 | Output table includes all required columns |
| C-13 | State count summary (earned/in-progress/locked) is visible in output |

---

## V-01 — Phrasing Register: Floor as Session-Level Preamble Invariant

| Tier | # | Criterion | Verdict | Evidence Note |
|------|---|-----------|---------|---------------|
| Essential | C-01 | One state per achievement | **PASS** | Step 3 Assign States assigns single state per row |
| Essential | C-02 | Falsified as honesty signal | **PASS** | Three-rule contract (Earn / Describe / Apply floor) frames investigation rigor |
| Essential | C-03 | Artifact-grounded classification | **PASS** | Step 1 Scan precedes Step 2 Classify |
| Essential | C-04 | IN-PROGRESS numeric progress | **PASS** | Table step structure supports n/m form |
| Essential | C-05 | Specific next action | **PASS** | Step 5 Next Action present |
| Recommended | C-06 | All 7 categories represented | **PARTIAL** | No explicit requirement to enumerate all 7 categories |
| Recommended | C-07 | EARNED achievements carry dates | **PARTIAL** | No date requirement stated in step structure |
| Recommended | C-08 | Falsified contract completeness | **PASS** | Three-rule block covers all required components |
| Aspirational | C-09 | CLASSIFY before STATE | **PASS** | Explicitly noted: "CLASSIFY step before STATE enforces C-09" |
| Aspirational | C-10 | Explicit classify output | **PARTIAL** | Step 2 Classify is named but not a gated intermediate output |
| Aspirational | C-11 | Evasion surface named | **PARTIAL** | "Apply floor" references invariant by number; evasion surface not named inline |
| Aspirational | C-12 | Table columns complete | **PASS** | Step 4 Achievement Table defined |
| Aspirational | C-13 | State count summary | **FAIL** | No frontmatter or count output specified |
| Aspirational | C-14 | Consequence clause present | **PASS** | Present in three-rule contract block |
| Aspirational | C-15 | Floor sentence unconditional | **PASS** | Session invariant 2 is unconditional at preamble level |
| Aspirational | C-16 | Structural compliance embedding | **FAIL** | Explicitly noted: "C-16 not targeted (requirements remain rule-stated)" |
| Aspirational | C-17 | Section-label unconditional | **PASS** | Preamble invariant position under neutral "Session invariants:" label |

**Essential**: 5/5 × 60 = **60**
**Recommended**: 2/3 × 30 = **20**
**Aspirational**: 6/9 × 10 = **6.7**
**Composite: 86.7 — Silver**

---

## V-02 — Output Format: Pre-Printed Verbatim Compliance Block in Instruction Body

| Tier | # | Criterion | Verdict | Evidence Note |
|------|---|-----------|---------|---------------|
| Essential | C-01 | One state per achievement | **PASS** | Step 4 Assign States and Build Table |
| Essential | C-02 | Falsified as honesty signal | **PASS** | Pre-printed compliance block frames contract rigor |
| Essential | C-03 | Artifact-grounded classification | **PASS** | Step 1 Scan → Step 3 Classify ordering |
| Essential | C-04 | IN-PROGRESS numeric progress | **PASS** | Table structure supports n/m form |
| Essential | C-05 | Specific next action | **PASS** | Step 5 Next Action present |
| Recommended | C-06 | All 7 categories represented | **PARTIAL** | Not guaranteed by prompt structure |
| Recommended | C-07 | EARNED achievements carry dates | **PARTIAL** | Not addressed in steps or pre-printed block |
| Recommended | C-08 | Falsified contract completeness | **PASS** | Pre-printed block includes consequence clause, evasion surface, floor as Rule 3 |
| Aspirational | C-09 | CLASSIFY before STATE | **PASS** | Step 3 Classify precedes Step 4 States |
| Aspirational | C-10 | Explicit classify output | **PARTIAL** | Step 3 is named but not a gated output requiring explicit list |
| Aspirational | C-11 | Evasion surface named | **PASS** | Pre-printed block explicitly includes evasion surface text verbatim |
| Aspirational | C-12 | Table columns complete | **PASS** | Step 4 table defined |
| Aspirational | C-13 | State count summary | **FAIL** | No frontmatter or count output specified |
| Aspirational | C-14 | Consequence clause present | **PASS** | Pre-printed in compliance block |
| Aspirational | C-15 | Floor sentence unconditional | **PASS** | Rule 3 in neutral-labeled "FALSIFIED ACHIEVEMENT CONTRACT — PRE-PRINTED" block |
| Aspirational | C-16 | Structural compliance embedding | **PASS** | Verbatim compliance block pre-printed in instruction body; model told not to rewrite |
| Aspirational | C-17 | Section-label unconditional | **PASS** | Neutral heading: "FALSIFIED ACHIEVEMENT CONTRACT — PRE-PRINTED" |

**Essential**: 5/5 × 60 = **60**
**Recommended**: 2/3 × 30 = **20**
**Aspirational**: 7/9 × 10 = **7.8**
**Composite: 87.8 — Silver**

---

## V-03 — Lifecycle Emphasis: SCAN GATE Carries Floor as Numbered Phase Invariant

| Tier | # | Criterion | Verdict | Evidence Note |
|------|---|-----------|---------|---------------|
| Essential | C-01 | One state per achievement | **PASS** | STATE GATE assigns single state per achievement |
| Essential | C-02 | Falsified as honesty signal | **PASS** | Three numbered items in STATE GATE, no conditional subheading |
| Essential | C-03 | Artifact-grounded classification | **PASS** | SCAN GATE → CLASSIFY GATE ordering |
| Essential | C-04 | IN-PROGRESS numeric progress | **PASS** | Gate output supports n/m form |
| Essential | C-05 | Specific next action | **PASS** | RECOMMEND step present |
| Recommended | C-06 | All 7 categories represented | **PARTIAL** | Not explicitly required in gate definitions |
| Recommended | C-07 | EARNED achievements carry dates | **PARTIAL** | Not specified in any gate |
| Recommended | C-08 | Falsified contract completeness | **PASS** | Three numbered items in STATE GATE cover all components |
| Aspirational | C-09 | CLASSIFY before STATE | **PASS** | CLASSIFY GATE architecturally precedes STATE GATE |
| Aspirational | C-10 | Explicit classify output | **PASS** | CLASSIFY GATE requires explicit intermediate classification before state assignment |
| Aspirational | C-11 | Evasion surface named | **PARTIAL** | Phase invariant 2 names the floor; evasion surface in STATE GATE Falsified items unclear |
| Aspirational | C-12 | Table columns complete | **PASS** | STATE GATE output structured with required fields |
| Aspirational | C-13 | State count summary | **FAIL** | No frontmatter or count output specified |
| Aspirational | C-14 | Consequence clause present | **PASS** | Present in STATE GATE Falsified numbered items |
| Aspirational | C-15 | Floor sentence unconditional | **PASS** | Phase invariant 2 in SCAN GATE is unconditional |
| Aspirational | C-16 | Structural compliance embedding | **FAIL** | Rule-stated: explicitly in coverage map as FAIL |
| Aspirational | C-17 | Section-label unconditional | **PASS** | SCAN GATE is neutral phase marker, no conditional trigger phrase |

**Essential**: 5/5 × 60 = **60**
**Recommended**: 2/3 × 30 = **20**
**Aspirational**: 6/9 × 10 = **6.7**
**Composite: 86.7 — Silver**

---

## V-04 — Role Sequence + Output Format: Pre-Printed Block in Classifier Role

| Tier | # | Criterion | Verdict | Evidence Note |
|------|---|-----------|---------|---------------|
| Essential | C-01 | One state per achievement | **PASS** | Role 2 Classifier assigns single state per achievement |
| Essential | C-02 | Falsified as honesty signal | **PASS** | Pre-printed "FALSIFIED CONTRACT — PRE-PRINTED" block in Role 2 |
| Essential | C-03 | Artifact-grounded classification | **PASS** | Role 1 Analyst produces evidence record; Role 2 classifies from it |
| Essential | C-04 | IN-PROGRESS numeric progress | **PASS** | Role 2 table output supports n/m form |
| Essential | C-05 | Specific next action | **PASS** | Role 2 includes recommendation output |
| Recommended | C-06 | All 7 categories represented | **PARTIAL** | Not explicitly required in role definition |
| Recommended | C-07 | EARNED achievements carry dates | **PARTIAL** | Not addressed in role description |
| Recommended | C-08 | Falsified contract completeness | **PASS** | Pre-printed block includes all three components |
| Aspirational | C-09 | CLASSIFY before STATE | **PASS** | Structural role separation: Role 2 cannot re-scan (Role 1 produces all evidence) |
| Aspirational | C-10 | Explicit classify output | **PASS** | Role 1 evidence record is explicit intermediate output before Role 2 begins |
| Aspirational | C-11 | Evasion surface named | **PASS** | Pre-printed block includes evasion surface (verbatim in block) |
| Aspirational | C-12 | Table columns complete | **PASS** | Role 2 produces structured table |
| Aspirational | C-13 | State count summary | **PASS** | Frontmatter carries `earned:` / `in_progress:` / `locked:` counts (explicitly stated) |
| Aspirational | C-14 | Consequence clause present | **PASS** | Pre-printed in Role 2 block |
| Aspirational | C-15 | Floor sentence unconditional | **PASS** | Rule 3 in neutral-labeled block, no conditional frame |
| Aspirational | C-16 | Structural compliance embedding | **PASS** | Pre-printed block in Role 2 (Classifier role); model fills around it |
| Aspirational | C-17 | Section-label unconditional | **PASS** | Neutral heading in Classifier role: no conditional trigger phrase |

**Essential**: 5/5 × 60 = **60**
**Recommended**: 2/3 × 30 = **20**
**Aspirational**: 8/9 × 10 = **8.9**
**Composite: 88.9 — Silver**

> Note: V-04 clears 8/9 aspirational but C-06 partial holds recommended at 2/3, placing composite at 88.9 — just below the Gold threshold of 90.

---

## V-05 — Golden Synthesis: Pre-Printed Skeleton + Preamble Invariant + SCAN GATE Invariant

| Tier | # | Criterion | Verdict | Evidence Note |
|------|---|-----------|---------|---------------|
| Essential | C-01 | One state per achievement | **PASS** | Pre-printed table skeleton with explicit STATE GATE |
| Essential | C-02 | Falsified as honesty signal | **PASS** | Falsified LOCKED cell pre-printed with full honesty framing |
| Essential | C-03 | Artifact-grounded classification | **PASS** | SCAN GATE → CLASSIFY GATE → FILL TEMPLATE ordering |
| Essential | C-04 | IN-PROGRESS numeric progress | **PASS** | Pre-printed skeleton includes progress `[PLACEHOLDER]` field in IN-PROGRESS rows |
| Essential | C-05 | Specific next action | **PASS** | Explicit recommendation step in pipeline |
| Recommended | C-06 | All 7 categories represented | **PASS** | Pre-printed skeleton defines all category rows — structural guarantee, not instruction |
| Recommended | C-07 | EARNED achievements carry dates | **PASS** | Pre-printed EARNED rows include date `[PLACEHOLDER]` — model fills, cannot omit |
| Recommended | C-08 | Falsified contract completeness | **PASS** | Consequence clause, evasion surface, floor declaration all pre-printed in Falsified cell |
| Aspirational | C-09 | CLASSIFY before STATE | **PASS** | CLASSIFY GATE is required architectural predecessor to FILL TEMPLATE |
| Aspirational | C-10 | Explicit classify output | **PASS** | CLASSIFY GATE requires explicit intermediate classification list before template fill |
| Aspirational | C-11 | Evasion surface named | **PASS** | "including as a closing reflection" pre-printed verbatim in Falsified cell |
| Aspirational | C-12 | Table columns complete | **PASS** | Pre-printed skeleton defines all columns — structural guarantee |
| Aspirational | C-13 | State count summary | **PASS** | STATE GATE writes `earned:` / `in_progress:` / `locked:` counts directly to frontmatter |
| Aspirational | C-14 | Consequence clause present | **PASS** | Pre-printed in Falsified cell — model cannot omit |
| Aspirational | C-15 | Floor sentence unconditional | **PASS** | Three independent occurrences, all under neutral labels |
| Aspirational | C-16 | Structural compliance embedding | **PASS** | Pre-printed table skeleton (strongest form: model fills `[PLACEHOLDER]` only) |
| Aspirational | C-17 | Section-label unconditional | **PASS** | Three-layer guarantee: preamble "Session invariant B:", SCAN GATE phase marker, pre-printed cell with no governing label |

**Essential**: 5/5 × 60 = **60**
**Recommended**: 3/3 × 30 = **30**
**Aspirational**: 9/9 × 10 = **10**
**Composite: 100 — Platinum**

---

## Rankings

| Rank | Variation | Composite | Grade | C-16 | C-17 | Key Differentiator |
|------|-----------|-----------|-------|------|------|--------------------|
| 1 | **V-05** | **100** | **Platinum** | PASS | PASS (3-layer) | Pre-printed skeleton + preamble + SCAN GATE — all recommended pass |
| 2 | V-04 | 88.9 | Silver | PASS | PASS | Role separation + frontmatter counts — C-06/C-07 partial limits recommended |
| 3 | V-02 | 87.8 | Silver | PASS | PASS | Instruction-body block — C-06/C-07 partial; no frontmatter counts |
| 4 | V-01 | 86.7 | Silver | FAIL | PASS | Preamble invariant only — rule-stated |
| 4 | V-03 | 86.7 | Silver | FAIL | PASS | SCAN GATE invariant only — rule-stated |

---

## Excellence Signals from V-05

V-05 is the only variation to reach Platinum. Three distinct patterns explain it:

### Signal 1: Defense-in-depth C-17 compliance

The floor declaration appears three times independently, each under a structurally neutral label:
1. **Preamble** — "Session invariant B:" (neutral category, no conditional trigger)
2. **SCAN GATE** — "Floor confirmed (Invariant B):" (phase marker, not conditional clause)
3. **Pre-printed Falsified table cell** — no governing section label at all

Each layer is independent. If the model elides the preamble or misreads the gate, the pre-printed cell maintains C-17 compliance. No single failure can collapse all three guarantees simultaneously. This is architecturally different from one unconditional statement repeated — each occurrence is in a structurally distinct position.

### Signal 2: Placeholder-fill skeleton as categorical risk elimination

Pre-printing the entire output skeleton with `[PLACEHOLDER]` fields changes the model's cognitive task from *generating compliance text* to *filling data into pre-written compliance text*. The consequence clause, evasion surface, and floor declaration are in the output before the model runs. There is no generative path through which the model can omit them. This is a qualitatively different compliance guarantee than C-16 alone captures — C-16 identifies the structural type; Signal 2 identifies *why* that type is categorically safer.

### Signal 3: STATE GATE → frontmatter bridge

Writing achievement counts from a named STATE GATE directly to frontmatter fields (`earned:`, `in_progress:`, `locked:`) creates a parallel structured metadata layer. The achievement state machine becomes queryable and auditable outside the document body — enabling downstream tooling to read state without parsing prose.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["defense-in-depth C-17 compliance via three structurally independent neutral-labeled occurrences of the floor declaration — any single failure leaves two redundant guarantees", "placeholder-fill skeleton changes the model task from generating compliance text to filling data around pre-printed compliance text, eliminating generative omission risk categorically rather than by instruction"]}
```
