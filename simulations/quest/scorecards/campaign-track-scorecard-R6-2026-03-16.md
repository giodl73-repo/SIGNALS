# Scorecard: campaign-track / Round 6

**Skill**: campaign-track
**Rubric version**: 6
**Variations scored**: V-01 through V-05
**Scoring**: Essential 10 pts, Recommended 5 pts, Aspirational 3 pts | Max: 98 pts

---

## Criterion Matrix

| Criterion | Tier | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|
| C-01 Orchestration sequence | E | PASS | PASS | PASS | PASS | PASS |
| C-02 Topic registration artifact | E | PASS | PASS | PASS | PASS | PASS |
| C-03 Coverage delta display | E | PASS | PASS | PASS | PASS | PASS |
| C-04 Narrative synthesis present | E | PASS | PASS | PASS | PASS | PASS |
| C-05 Session-bookend utility | E | PASS | PASS | PASS | PASS | PASS |
| C-06 Actionable recommendations | R | PASS | PASS | PASS | PASS | PASS |
| C-07 Coverage ratio + readiness | R | PASS | PASS | PASS | PASS | PASS |
| C-08 Cross-namespace balance | R | PASS | PASS | PASS | PASS | PASS |
| C-09 Echo integration | A | PASS | PASS | PASS | PASS | PASS |
| C-10 Dual-session delta | A | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-11 Role-gated phases | A | PASS | PASS | PASS | PASS | PASS |
| C-12 Explicit progression gates | A | PASS | PASS | PASS | PASS | PASS |
| C-13 Empty-state as named section | A | PASS | PASS | PASS | PASS | PASS |
| C-14 Per-role prohibition lists | A | PASS | FAIL | FAIL | PASS | PASS |
| C-15 Typed output contracts | A | FAIL | PASS | FAIL | PASS | PASS |
| C-16 Terminal completion checklist | A | FAIL | FAIL | PASS | FAIL | PASS |
| C-22 Prohibition-count parity | A | PASS | FAIL | FAIL | PASS | PASS |
| C-23 Full-phase type coverage | A | FAIL | PASS | FAIL | PASS | PASS |
| C-24 Terminal checklist quality | A | FAIL | FAIL | PASS | FAIL | PASS |

---

## Evidence Notes

### V-01 — Prohibition-count parity axis

**C-22 PASS**: Parity rule section opens with "Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no fewer." Structural invalidity stated: "a role with 4 or 6 items has violated the parity contract and is structurally invalid." All four role blocks confirm `(exactly 5)`. Count is auditable without reading content.

**C-14 PASS**: 5 named forbidden actions per role, enumerated 1-5. Passes the "at least two roles with one or more named prohibited actions" bar comfortably.

**C-15 FAIL**: Phases describe fields narratively ("Topic name and namespace assignment", "Priority level (High / Medium / Low)") — no type constraints, no enumerated token sets, no integer declarations.

**C-16 FAIL**: No terminal checklist. Output section emits a dashboard summary only.

**C-23 FAIL**: No typed contract section; full-phase coverage inapplicable.

**C-24 FAIL**: No checklist of any kind.

---

### V-02 — Full-phase type coverage axis

**C-23 PASS**: Opens with "Full-Phase Type Coverage Rule — All four phases have typed output contracts. Partial coverage... is not acceptable. A phase without a typed contract is an incomplete phase." All four phase contracts follow with enumerated token sets, integer declarations, and format strings.

**C-15 PASS**: Contracts present for all 4 phases. Phase 3 explicitly calls out "Fewer than 9 rows fails Phase 3. Prose counts in integer fields fail Phase 3." Phase 4 has "Absent echoes field fails Phase 4. Paraphrased verdict_verb fails Phase 4." Per-contract fail conditions strengthen the typed structure.

**C-14 FAIL**: Roles section lists four personas (Registrar / Planner / Analyst / Narrator) with phase assignments only. No forbidden action lists.

**C-22 FAIL**: No prohibition count declared; parity not applicable without prohibitions.

**C-16 FAIL**: No terminal checklist.

**C-24 FAIL**: No checklist.

---

### V-03 — Field-level terminal checklist axis

**C-24 PASS**: TERMINAL section has 22 field-level items. Each item names a specific artifact field (`topic_name`, `namespace`, `priority`, `planned_signals`, `planned_signals[*].target_skill`, `namespace_coverage`, `collection_purpose`, `row count`, `planned`, `collected`, `missing`, `zero_flag`, `coverage_ratio`, `readiness_verdict`, `verdict_verb`, `hypothesis_mutation.s0`, `hypothesis_mutation.current`, `echoes`, `next_signal_recommendations`, and two `[*]` field checks). Every item has a targeted FAIL action ("FAIL action: re-run Phase X"). Count is complete.

**C-16 PASS**: TERMINAL section with per-phase PASS conditions. Distinguishes targeted re-run ("re-run the affected phase only") from full restart. Condition: "When all TERMINAL items show PASS, emit consolidated dashboard."

**C-14 FAIL**: Roles section lists names and phase assignments. No prohibition lists.

**C-15 FAIL**: Phases defined narratively. No type constraints declared for any phase.

**C-22 FAIL**: No prohibition count.

**C-23 FAIL**: No full-phase type coverage rule.

---

### V-04 — Combined C-22 + C-23

**C-22 PASS**: Parity rule declared ("exactly 5 forbidden actions -- no more, no fewer... A role with fewer than 5 items or more than 5 items is structurally invalid."). Active-role annotations at each phase header reinforce the count at point of execution: `*Analyst active. Exactly 5 forbidden actions apply.*`

**C-23 PASS**: "Full-Phase Type Coverage Rule: All four phases have typed output contracts. Partial coverage -- typing fewer than four phases -- is not acceptable and produces an incomplete campaign artifact." All four contracts present.

**C-14 PASS**: 5 named forbidden actions per role, consistent numbering.

**C-15 PASS**: All 4 phases have full typed contracts with enumerated token sets and integer declarations.

**C-16 FAIL**: No terminal checklist.

**C-24 FAIL**: No field-level checklist.

---

### V-05 — Full stack

**C-22 PASS**: Parity rule states "numbered list format is required: each item labeled 1 through 5." Structural invalidity: "A role with 4 or 6 items is structurally invalid and fails audit." Active-role annotations ("*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*") fire at each of the four phase headers — parity enforcement appears at the declaration site AND at execution.

**C-23 PASS**: "No phase is exempt. Partial coverage fails." Full-Phase Type Coverage Rule declared before the contracts. All four contracts follow with explicit fail conditions.

**C-24 PASS**: 22 field-level items, each naming a specific field, its constraint, and a targeted FAIL action. Terminal section ends: "All 22 items PASS: campaign is complete. Dashboard ready to emit." Count stated explicitly — audit by enumeration.

**C-16 PASS**: TERMINAL section gated dashboard emission — "When all 22 TERMINAL items show PASS, emit consolidated dashboard."

**C-14 PASS**: 4 roles × 5 numbered prohibitions. Narrator prohibition 5 is the sharpest ("only exact Phase 4 Contract tokens are valid; 'likely confirmed' or 'essentially confirmed' both fail") — specific failure examples, not just abstract rule.

**C-15 PASS**: All 4 phases fully typed. Phase-level postconditions within phase bodies reference the contract directly ("Produce strategy.md conforming to Phase 1 Contract").

**C-10 FAIL** (all variations): None address session-to-session delta comparison. C-10 remains unaddressed in R6.

---

## Score Computation

| | E (×10) | R (×5) | A (×3) | Raw | /98 | % |
|--|---------|--------|--------|-----|-----|---|
| **V-01** | 50 | 15 | 18 (C-09,C-11,C-12,C-13,C-14,C-22) | 83 | 83/98 | **85** |
| **V-02** | 50 | 15 | 18 (C-09,C-11,C-12,C-13,C-15,C-23) | 83 | 83/98 | **85** |
| **V-03** | 50 | 15 | 18 (C-09,C-11,C-12,C-13,C-16,C-24) | 83 | 83/98 | **85** |
| **V-04** | 50 | 15 | 24 (C-09,C-11,C-12,C-13,C-14,C-15,C-22,C-23) | 89 | 89/98 | **91** |
| **V-05** | 50 | 15 | 30 (C-09,C-11,C-12,C-13,C-14,C-15,C-16,C-22,C-23,C-24) | 95 | 95/98 | **97** |

**Leaderboard**: V-05 (97) > V-04 (91) > V-01 = V-02 = V-03 (85)

*Note: V-01/V-02/V-03 tie at 85 because each single-axis variation picks up exactly 2 R6-relevant aspirationals (one pre-R6 + one new) alongside the shared baseline. Predicted leaderboard "V-03 > V-01 >= V-02" does not hold under equal-weight aspirational scoring.*

---

## Excellence Signals — V-05

Three patterns account for V-05's separation from V-04 (which shares all other structure):

**1. Active-role annotation integrates all live constraints at point of execution**

Each phase opens with:
> `*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*`

This pulls three rules (role identity, parity count, typed contract) into a single line at the moment the model transitions phases. Rules declared in separate sections (parity rule, typed contracts section, prohibitions section) don't have to be remembered — they're restated at the execution site. This is the structural reason V-05 avoids the "rules applied independently" risk V-04 carries.

**2. Phase postcondition as named GATE target**

V-05 adds an explicit postcondition before each gate:
> `Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields present and typed correctly. GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.`

The gate no longer references a vague artifact presence — it references a named postcondition with specific field requirements. A model checking the gate must verify the postcondition, not just confirm the file was written. This tightens the progression constraint beyond V-04's artifact-present gates.

**3. Terminal item count as completion invariant**

V-05's checklist closes with:
> `All 22 items PASS: campaign is complete. Dashboard ready to emit.`

Stating the count (22) makes the completion condition mechanically verifiable: a model either produces 22 PASS/FAIL verdicts or produces fewer. Any output with fewer than 22 items is visibly incomplete. V-03 has the same 22 items but does not state the count as a completion invariant — it relies on the reader to notice an incomplete checklist. V-05 makes the count an exit criterion.

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["active-role annotation at phase header integrates role identity, parity count, and contract reference into a single execution-point reminder", "named phase postcondition as explicit GATE target — gate references the postcondition, not just artifact presence, requiring field-level verification before advancing", "terminal checklist item count declared as completion invariant — stating count (22) makes incomplete outputs visibly defective without requiring content review"]}
```
