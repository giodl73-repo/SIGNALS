## Scout-Size — Quest Score R13

**Rubric**: v13 (5 Essential, 3 Recommended, 27 Aspirational — denominator 27)
**Variations**: V-01 through V-05

---

## Per-Variation Criterion Evaluation

### Essential (C-01–C-05)

All five variations inherit the R12 structural baseline. Every variation produces named integration points with a numeric count (C-01), uses exact LOW/MEDIUM/HIGH/XL vocabulary (C-02), names a workaround and cost direction (C-03), states confidence with a named basis (C-04), and omits task breakdowns/owner names/sprint assignments (C-05).

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| C-01 Surface area enumerated | PASS | PASS | PASS | PASS | PASS |
| C-02 Complexity tier on-scale | PASS | PASS | PASS | PASS | PASS |
| C-03 Inertia check present | PASS | PASS | PASS | PASS | PASS |
| C-04 Confidence level + basis | PASS | PASS | PASS | PASS | PASS |
| C-05 Signal boundary respected | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60 pts (all five variations)**

---

### Recommended (C-06–C-08)

All five variations carry specialist-discipline team-size fields (C-06), sprint-range timeline fields (C-07), and named primary complexity driver fields (C-08).

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| C-06 Specialist types named | PASS | PASS | PASS | PASS | PASS |
| C-07 Sprint range format | PASS | PASS | PASS | PASS | PASS |
| C-08 Primary driver named | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 30 pts (all five variations)**

---

### Aspirational (C-09–C-35)

#### C-09 — Sensitivity: tier-up and tier-down conditions
All: PASS. Every variation has a sensitivity table with both directions.

#### C-10 — Confidence calibration: what would change it
All: PASS. Confidence calibration table present in all.

#### C-11 — Confidence gap named
All: PASS. Standalone CONFIDENCE GAP CHECKPOINT section names the primary residual uncertainty in all.

#### C-12 — Sensitivity framed as single named conditions
All: PASS. WRONG examples show "scope grows" failing; CORRECT shows single named falsifiable scenarios. Table structure enforces single-condition format.

#### C-13 — Sensitivity names explicit tier destination
All: PASS. Column header reads "Destination Tier [must differ from current — fill LOW / MEDIUM / HIGH / XL]"; output slot is "Tier rises to [ ]" / "Tier drops to [ ]" in all.

#### C-14 — Sensitivity conditions are falsifiable
All: PASS. WRONG/CORRECT examples teach the distinction; column label names investigation action. "Scope grows" fails; "offline-sync required — confirm by reviewing PRD" passes.

#### C-15 — Confidence basis and gap non-overlapping
All: PASS. WRONG block shows basis-negation; self-test query is concrete and executable; gap field label encodes the relational constraint. Defense cluster present in all (C-30 scope). Non-overlap enforced structurally.

#### C-16 — Sensitivity destination tier differs from current
All: PASS. Column header encodes the relational rule at the field label level: "[must differ from current — fill LOW / MEDIUM / HIGH / XL]".

#### C-17 — High-risk constraints carry inline failure examples
All: PASS. Minimum scope (C-11, C-15, C-16) all have WRONG/CORRECT blocks adjacent to the constrained fields. Confidence gap, sensitivity destination, and confidence basis each carry inline examples.

#### C-18 — Constraints encoded as structural features
All: PASS. Tier vocabulary constraint is in column header; sensitivity destination constraint is in column header; gap field label encodes non-overlap rule. C-13 and C-16 both encoded as structural labels (minimum scope for C-18).

#### C-19 — Inline failure examples precede the output field they govern
All: PASS. Every WRONG/CORRECT block appears before the field it governs. Gap checkpoint examples precede "Gap: _____". Sensitivity examples precede the sensitivity table. Phase 0 examples (V-03/V-04/V-05) precede the gate status field. No examples appear in a post-output checklist position.

*Note: R12 V-05 had C-19 PARTIAL; R13 V-05 resolves this — all step tables now have pre-slot examples.*

#### C-20 — Complementary constraint pairs use role-separated production
- V-01: FAIL. Single-phase; basis and gap produced in same phase.
- V-02: FAIL. Single-phase; same.
- V-03: FAIL. Phase 0 is an entry gate, not a role producing the confidence pair. Analysis is single-phase thereafter.
- V-04: PASS. Phase 1 Sizing Analyst produces confidence basis; Phase 2 Risk Assessor produces confidence gap. Non-overlap charter explicit in Phase 2.
- V-05: PASS. Same role-separation architecture as V-04.

#### C-21 — Inline failure examples provide both WRONG and CORRECT instances
All: PASS. Every inline block in the gap checkpoint and sensitivity section carries both a named WRONG instance and a named CORRECT instance in the same section. No examples are WRONG-only or CORRECT-only.

#### C-22 — Relational constraints co-encoded in dependent field's definition
All: PASS. Gap field label: "[must address a dimension not covered by the Step N basis — not a negation of it]". Sensitivity destination column: "[must differ from current — fill LOW / MEDIUM / HIGH / XL]". Both relational constraints are encoded at the production site.

#### C-23 — Role charters assign explicit ownership of all output fields
- V-01/V-02/V-03: FAIL. No role-separated production; criterion inapplicable and earns no credit.
- V-04: PASS. Phase 1 charter names owned fields + explicit exclusion list for Phase 2 fields. Phase 2 charter names owned fields + exclusion list for Phase 0/Phase 1 fields. All output fields accounted for.
- V-05: PASS. Same charter coverage as V-04.

#### C-24 — Phase 2 non-access clause names prohibited content category
- V-01/V-02/V-03: FAIL. No Phase 2 charter.
- V-04: PASS. "Prohibited content category: any item the Sizing Analyst enumerated in P1-5 as confirmed — e.g., 'API contract is stable,' 'integration points are enumerated.'" Named category, not just structural rule.
- V-05: PASS. Same structure. "Prohibited content category: any item in the P1-5 confirmed set..."

#### C-25 — Phase 2 charter embeds a self-test falsifiability query
- V-01/V-02/V-03: FAIL. No Phase 2 charter.
- V-04: PASS. Phase 2 charter contains: "Ask: if I reversed a statement from P1-5 ('X is confirmed' → 'X is not confirmed'), would I produce my gap? **If yes: you have written a basis-negation — a Phase 2 charter violation.**" Concrete executable procedure, not a rule restatement.
- V-05: PASS. Same self-test in Phase 2 charter.

#### C-26 — Role ownership co-encoded in output structure field labels
- V-01/V-02/V-03: FAIL. No roles; compilation table has no role tags.
- V-04: PASS. Working step tables carry role tags in column headers: "[Phase 1 Sizing Analyst — name each individually]", "[Phase 2 Risk Assessor — ...]". Compilation table carries "Produced By" column with role attributions at every row.
- V-05: PASS. Same — working step tables have role-tagged column headers; compilation table has "Phase" column.

#### C-27 — Cross-phase relational constraints co-encoded in dependent field's label within compilation table
- V-01/V-02: FAIL. Single-phase; compilation table has no cross-phase field relationships.
- V-03: FAIL. Phase 0 + single-phase combination; compilation table has no role-tagged cross-phase label encoding.
- V-04: PARTIAL. Multi-phase compilation table present ("Field | Produced By | Value"). Sensitivity destination column does carry the constraint label in working step tables. However, the confidence gap (C-15 minimum scope) is excluded from the compilation table via C-32 standalone section, so the C-27 requirement for gap-column constraint encoding in the compilation table cannot be satisfied at the table level. Evidence note: the footnote "_Confidence Gap [Phase 2 Risk Assessor]: See CONFIDENCE GAP CHECKPOINT above_" does not encode the relational constraint in the table row. Partial credit for non-gap cross-phase field constraint labels.
- V-05: PARTIAL. Same analysis as V-04. Gap excluded from compilation table via C-32; compilation table carries "Phase" attribution column with constraint-labeled tier sensitivity fields but not the gap relational constraint.

#### C-28 — Single-phase self-test query embedded in gap field body
All: PASS. Every variation embeds a concrete executable self-test in the gap section body: "Ask: if I reversed something from my Step N basis... would I produce my gap?" This is distinct from any rule statement and any WRONG/CORRECT example. V-04/V-05 also satisfy C-25 (Phase 2 charter self-test); their gap section additionally carries the embedded query, satisfying the feature that C-28 specifies.

#### C-29 — Phase 1 charter carries explicit field exclusion list mirroring Phase 2 non-access
- V-01/V-02/V-03: FAIL. No Phase 1 charter.
- V-04: PASS. "**Fields reserved for Phase 2 [do not produce here]**: Confidence Gap · Confidence Calibration · Tier Sensitivity" — matches Phase 2's owned-field list exactly.
- V-05: PASS. Same exclusion list.

#### C-30 — Defense cluster for highest-risk relational constraint
All: PASS. The CONFIDENCE GAP CHECKPOINT section in every variation satisfies all three cluster requirements simultaneously:
1. Gap field label encodes the relational constraint (C-22 scope) ✓
2. Self-test query is embedded in the gap body section (C-28/C-25 scope) ✓
3. Both WRONG and CORRECT instances appear within the same section (C-21 scope) ✓

No mechanism is scattered to a separate section.

#### C-31 — Named pre-commit gate block for in-table field constraints
All: PASS. The confidence gap is promoted to a standalone section (C-32), eliminating the need for C-31's gate-block compensation mechanism. For all other constrained table fields (confidence basis, sensitivity), C-19 is satisfied (examples precede field production). C-31's trigger condition — "C-19 not achieved for a table-based C-17 field" — does not apply.

#### C-32 — Gap field promoted to named standalone section
All: PASS. "── CONFIDENCE GAP CHECKPOINT ──" delimiter-header section appears after the confidence basis section and before calibration in all five variations. Gap is not a table cell.

#### C-33 — Self-test consequence branch names the detected failure class
All: PASS.
- V-01: "**If yes: you have written a basis-negation.**"
- V-02: "**If yes: you have written a basis-negation.**"
- V-03: "**If yes: you have produced a basis-negation.**" (second-person register)
- V-04: "**If yes: you have written a basis-negation — a Phase 2 charter violation.**"
- V-05: "**If yes: you have written a basis-negation. You are in a basis-negation pattern.**"

#### C-34 — Failure-class label co-encoded in WRONG instance examples *(new in v13)*
- V-01: PASS. WRONG block carries "> **DIAGNOSIS: basis-negation.**" as a labeled second line immediately after the WRONG example text. Failure class labeled at example-exposure time.
- V-02: PASS. WRONG block carries a full three-field sub-block: **FAILURE CLASS**: basis-negation / **DETECTION PATTERN**: gap is derivable from basis by direct negation / **WHY IT FAILS**: a reader learns nothing... All three fields are labeled within the WRONG block.
- V-03: PASS. WRONG block carries "> **You have produced a basis-negation.**" in second-person. Names the failure class at example-exposure time; second-person addresses the model as observer.
- V-04: PASS. WRONG block carries "> **DIAGNOSIS: basis-negation.**" with additional explanation: "The Risk Assessor has reversed the Sizing Analyst's confirmed item. This is the charter violation..."
- V-05: PASS. WRONG block carries the full three-field sub-block (identical to V-02 approach): **FAILURE CLASS**: basis-negation / **DETECTION PATTERN** / **WHY IT FAILS**.

#### C-35 — Pre-analysis gate phase with binary entry signal *(new in v13)*
- V-01: FAIL. Single-phase, no Phase 0. No binary gate.
- V-02: FAIL. Single-phase, no Phase 0.
- V-03: PASS. "Phase 0: Inertia Gate" produces "Gate status [produce exactly one]: **OPEN** / **CLOSED — [name unmet condition]**". Gate conditions explicit (workaround + cost direction). Phase 1 conditioned: "_Proceed to Step 1 only if gate status = OPEN._"
- V-04: PASS. "Phase 0: Inertia Gate" with identical binary signal and gate-close conditions. "Phase 1 may not begin until Phase 0 is CLOSED" (actually "OPEN" — phase 0 opens to phase 1). Binary signal present; CLOSED output names unmet condition.
- V-05: PASS. "Phase 0: Entry Gate" extended to two named preconditions (Precondition A: Inertia, Precondition B: Signal boundary). Binary output: "**OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**". Either failure closes the gate. Phase 0 enforces C-05 signal boundary structurally as a gate dependency rather than prose instruction.

---

## Aspirational Score Totals

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | P | P | P | P | P |
| C-10 | P | P | P | P | P |
| C-11 | P | P | P | P | P |
| C-12 | P | P | P | P | P |
| C-13 | P | P | P | P | P |
| C-14 | P | P | P | P | P |
| C-15 | P | P | P | P | P |
| C-16 | P | P | P | P | P |
| C-17 | P | P | P | P | P |
| C-18 | P | P | P | P | P |
| C-19 | P | P | P | P | P |
| C-20 | **F** | **F** | **F** | P | P |
| C-21 | P | P | P | P | P |
| C-22 | P | P | P | P | P |
| C-23 | **F** | **F** | **F** | P | P |
| C-24 | **F** | **F** | **F** | P | P |
| C-25 | **F** | **F** | **F** | P | P |
| C-26 | **F** | **F** | **F** | P | P |
| C-27 | **F** | **F** | **F** | PARTIAL | PARTIAL |
| C-28 | P | P | P | P | P |
| C-29 | **F** | **F** | **F** | P | P |
| C-30 | P | P | P | P | P |
| C-31 | P | P | P | P | P |
| C-32 | P | P | P | P | P |
| C-33 | P | P | P | P | P |
| C-34 | P | P | P | P | P |
| C-35 | **F** | **F** | P | P | P |

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| Aspirational score | 19.0 | 19.0 | 20.0 | 26.5 | 26.5 |
| Aspirational pts | 7.04 | 7.04 | 7.41 | 9.81 | 9.81 |
| **Composite** | **97.0** | **97.0** | **97.4** | **99.8** | **99.8** |

---

## Ranking

| Rank | Variation | Composite | Discriminating factors |
|------|-----------|-----------|------------------------|
| **1 (tied)** | **V-05** | **99.8** | Three-field DIAGNOSIS block (C-34 max depth); Phase 0 extended to C-05 signal boundary + inertia (2-precondition gate); full C-20 cluster; C-33/C-34/C-35 all satisfied |
| **1 (tied)** | **V-04** | **99.8** | Phase 0 inertia gate (C-35); full C-20 cluster; C-34 single-annotation; single-precondition gate |
| **3** | **V-03** | **97.4** | Gains C-35 over V-01/V-02 via Phase 0 binary gate; loses entire C-20 cluster (single-phase after gate) |
| **4 (tied)** | **V-01** | **97.0** | C-34 PASS (inline DIAGNOSIS annotation); no Phase 0 gate; no role separation |
| **4 (tied)** | **V-02** | **97.0** | C-34 PASS (three-field sub-block, strongest single-phase C-34 form); no Phase 0; no role separation; ties V-01 |

**Tiebreaker V-04 vs V-05**: Scores are identical under the current rubric. V-05 is architecturally superior — Phase 0 Precondition B converts C-05 from a post-output prose check to a structural production dependency, eliminating the last major enforcement gap that role separation and label encoding cannot address. A future criterion capturing "C-05 structurally enforced as gate precondition" would separate them. Declare V-05 champion on architectural depth.

**Tiebreaker V-01 vs V-02**: Both score 97.0. V-02's three-field DIAGNOSIS block (FAILURE CLASS / DETECTION PATTERN / WHY IT FAILS) is richer at example-exposure time than V-01's single annotation line, but the rubric does not distinguish PASS depth within C-34. No score differentiator. V-02 has the more elaborated C-34 form.

---

## Excellence Signals from V-05

**Signal 1 — Two-precondition Phase 0 gate as total entry enforcement**
V-05 extends Phase 0 beyond inertia to also check the C-05 signal boundary. A CLOSED gate results from either missing inertia OR detected plan-level artifacts. This converts signal boundary enforcement from a post-hoc prose instruction ("Signal boundary check: remove any task breakdowns...") into a structural production dependency: if the input contains plan artifacts, gate = CLOSED, no sizing output is produced. The two-precondition gate design is the first instance where C-05 becomes a gate dependency rather than a closing reminder — eliminating the last major compliance failure that can pass through all role-separation and structural-label mechanisms.

**Signal 2 — Three-field DIAGNOSIS sub-block in WRONG instance for richest C-34 form**
V-05 inherits V-02's three-field WRONG block annotation (FAILURE CLASS / DETECTION PATTERN / WHY IT FAILS) while combining it with the full three-phase architecture. At example-exposure time, the model encounters not just the failure class name but also its detection mechanism ("the Risk Assessor reversed a P1-5 confirmed item") and its failure explanation ("the gap is derivable from P1-5 by negation with no new information; the Phase 2 charter exists precisely to prevent this substitution"). The three-field form creates a richer diagnostic priming event than a single labeled line — the model absorbs the pattern, the detection signal, and the architectural reason simultaneously before producing the gap.

**Signal 3 — C-27 remains the only incomplete criterion (PARTIAL) via C-32 tension**
Both top-scoring variations get PARTIAL on C-27 because C-32 removes the gap from the compilation table, making the C-15 relational constraint unavailable for in-table column-header encoding (C-27's minimum scope). This is a structural tension: C-32 (standalone gap section) is architecturally correct for the gap but vacates the compilation table slot where C-27 would apply. A future design could satisfy C-27 by encoding the C-15 constraint in the compilation table's gap reference footnote or by adding a relational constraint tag to the cross-phase reference note.

---

```json
{"top_score": 99.8, "all_essential_pass": true, "new_patterns": ["Two-precondition Phase 0 gate enforces both inertia and C-05 signal boundary as structural entry dependencies — a CLOSED gate on either precondition halts all analysis output, converting signal boundary from a post-hoc prose check into a production gate that role separation and label encoding cannot substitute for", "Three-field WRONG block annotation (FAILURE CLASS / DETECTION PATTERN / WHY IT FAILS) provides richer C-34 diagnostic priming than a single labeled line — model encounters the failure class name, its detection mechanism, and its architectural failure reason as distinct labeled fields at example-exposure time before the gap field is produced"]}
```
