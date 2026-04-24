Scorecard written. Summary:

## R5 Results

| Rank | Variation | Score | C-17 | C-18 |
|------|-----------|-------|------|------|
| 1 (tie) | V-02 | 100 | PASS | PASS |
| 1 (tie) | V-03 | 100 | PASS | PASS |
| 1 (tie) | V-05 | 100 | PASS | PASS |
| 4 | V-01 | 99 | PASS | **FAIL** |
| 5 | V-04 | 98 | **FAIL** | **FAIL** |

All variations golden. All five essential criteria pass across all five variations.

**Predictions confirmed perfectly**: V-01 at 17/18 (C-18 gap), V-02/V-03/V-05 at 18/18, V-04 with C-17 and C-18 both failing.

**Two new patterns:**

1. **Gate-level placement fails C-17** — V-04 confirms that post-generation checklist examples don't satisfy adjacency. The WRONG/CORRECT must be active when the model writes the field, not after.

2. **Role separation as structural C-15 guard** — V-03's two-phase design makes basis/gap conflation a role violation, not just a rule violation. The assessor's charter structurally prevents re-using what the analyst confirmed. This is a C-18-style architectural approach applied to C-15.
 |
| C-03 | Inertia check present | PASS | "Then say whether keeping that workaround running is cheaper, comparable, or more expensive... Do not mention the workaround in passing and move on — the comparison is the point." |
| C-04 | Confidence stated with basis | PASS | "*What do you know?* — name the specific thing that makes you as confident as you stated. Be concrete." — level + named concrete basis |
| C-05 | Signal boundary respected | PASS | Output format lists only sizing sections (Inertia Check · Surface Area · ... · Confidence Calibration). Question structure cannot elicit plan content; no task-assignment section exists. |
| C-06 | Team-size names disciplines | PASS | "'1 backend, 1 platform engineer, 0.5 PM' is right. '3 engineers' is not — what kind?" |
| C-07 | Timeline as sprint range | PASS | "Give a sprint range: '3–5 sprints.' Not a date. Not 'about a quarter.' Not a single number." |
| C-08 | Primary driver identified | PASS | "'It's a complex feature' is not a driver. Name the factor." |
| C-09 | Sensitivity tier up + down | PASS | "Name one thing that would push it UP and one thing that would push it DOWN." |
| C-10 | Confidence calibration | PASS | "Name what you would need to learn to move your confidence level materially up or down." |
| C-11 | Confidence gap named | PASS | Adjacent WRONG/CORRECT: "WRONG: 'Some integration aspects remain unclear.' CORRECT: 'The failover contract of the notification dispatch queue under concurrent write load is undocumented.'" — at the Gap field, generation time |
| C-12 | Sensitivity single named conditions | PASS | "Give a single, specific condition — not 'if the scope grows.'... 'If offline sync is required' is falsifiable. 'If requirements expand' is not." |
| C-13 | Sensitivity names explicit tier destination | PASS | "Say the destination tier out loud: 'Tier rises to XL' or 'Tier drops to MEDIUM.'" |
| C-14 | Sensitivity conditions falsifiable | PASS | "Name what investigation would confirm or rule out the condition." |
| C-15 | Basis and gap non-overlapping | PASS | Adjacent WRONG/CORRECT: "WRONG: 'Know: API contract is confirmed. Don't know: API contract is not yet verified.' — This negates the same thing. Same dimension, flipped polarity. This fails." CORRECT example with different dimensions shown. |
| C-16 | Sensitivity destination differs from current tier | PASS | Adjacent WRONG/CORRECT: "WRONG: Current tier is HIGH. Writing 'Tier rises to HIGH' — that is not movement. CORRECT: Current tier is HIGH → up says 'Tier rises to XL if...' / down says 'Tier drops to MEDIUM if...'" |
| C-17 | High-risk constraints carry inline failure examples | PASS | C-11 WRONG/CORRECT adjacent to Gap constraint. C-15 WRONG/CORRECT adjacent to basis/gap constraint. C-16 WRONG/CORRECT adjacent to tier-movement constraint. All appear at field definition, not in a separate section. All active at generation time. |
| C-18 | Constraints encoded as structural features | FAIL | Sensitivity is prose-only: "Name one thing that would push it UP... Say the destination tier out loud." No table. No column headers carrying the tier-constraint rule. C-13 and C-16 constraints live in prose paragraphs, not in named column labels. |

**Essential**: 5/5 PASS = 60 pts
**Recommended**: 3/3 PASS = 30 pts
**Aspirational**: 9/10 PASS (C-18 FAIL) = 9 pts

```
composite = (5/5 * 60) + (3/3 * 30) + (9/10 * 10) = 60 + 30 + 9 = 99
```

**Score: 99** | Golden: YES (all essential pass, composite >= 80)
**Confirmed prediction**: 17/18 (C-18 gap) — prediction correct.

---

## V-02 — Table Schema + Complete C-17 Coverage

**Variation axis**: Required table schema with named columns + WRONG/CORRECT adjacent at C-11,
C-15, C-16 + column header encoding for C-13/C-16.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Surface area enumerated | PASS | Section 2 table: named rows + required total row "N integration points" |
| C-02 | Complexity tier on-scale | PASS | Section 3 table field: "LOW / MEDIUM / HIGH / XL" + "Use only this vocabulary — no other phrasing" |
| C-03 | Inertia check present | PASS | Section 1 table: cost direction field with only three valid values; "must be filled with one of the three options above" |
| C-04 | Confidence stated with basis | PASS | Section 4 table: Confidence Level + Basis field "Concrete and named; identifies a specific known thing" |
| C-05 | Signal boundary respected | PASS | Opening: "Your output must not contain task lists, sprint assignments, owner names, or milestone dates." — explicit prohibition |
| C-06 | Team-size names disciplines | PASS | Section 3 table: "Disciplines required, not headcount alone" |
| C-07 | Timeline as sprint range | PASS | Section 3 table: "Sprint range only — no calendar dates, no point estimates" |
| C-08 | Primary driver identified | PASS | Section 3 table: "Not 'it's complex' — name the factor" |
| C-09 | Sensitivity tier up + down | PASS | Section 5 table has explicit Tier UP and Tier DOWN rows |
| C-10 | Confidence calibration | PASS | Section 6 dedicated with raise/lower fields |
| C-11 | Confidence gap named | PASS | Section 4 WRONG/CORRECT block adjacent to Gap field: "WRONG: 'Some integration aspects remain unclear.' CORRECT: 'Gap: the failover behavior of the notification dispatch queue under concurrent load has not been verified.'" |
| C-12 | Sensitivity single named conditions | PASS | Section 5: "Each condition is a single named scenario — not a list of factors or a vague hedge" |
| C-13 | Sensitivity names explicit tier destination | PASS | Section 5 column header: "Destination Tier [LOW/MEDIUM/HIGH/XL — must differ from Section 3 tier]" — structural enforcement |
| C-14 | Sensitivity conditions falsifiable | PASS | "How to settle it (falsifiable)" is a named column; "if requirements change" explicitly fails |
| C-15 | Basis and gap non-overlapping | PASS | Section 4 WRONG/CORRECT block adjacent to Basis/Gap table: "WRONG: 'Basis: API contract is confirmed. Gap: API contract is not yet verified.' — Same dimension, flipped polarity. CORRECT: Basis names structural clarity... Gap names a behavioral unknown in a different area." |
| C-16 | Sensitivity destination differs from current tier | PASS | Section 5 WRONG/CORRECT adjacent to Destination Tier column: "WRONG: Section 3 tier is HIGH. Writing 'Tier UP → Destination: HIGH.' — The destination equals the current tier. No movement. Null sensitivity. Fails. CORRECT: HIGH → UP must be XL; DOWN must be MEDIUM or LOW." Column header also encodes the rule. |
| C-17 | High-risk constraints carry inline failure examples | PASS | C-11 WRONG/CORRECT in Section 4 at Gap field. C-15 WRONG/CORRECT in Section 4 at Basis/Gap block. C-16 WRONG/CORRECT in Section 5 below Destination Tier column. All three adjacent at generation time. |
| C-18 | Constraints encoded as structural features | PASS | Section 5 column header "Destination Tier [LOW/MEDIUM/HIGH/XL — must differ from Section 3 tier]" encodes both C-13 (tier vocabulary) and C-16 (must-differ rule) in the column label itself. Violation is visible at the field level without cross-referencing prose rules. |

**Essential**: 5/5 PASS = 60 pts
**Recommended**: 3/3 PASS = 30 pts
**Aspirational**: 10/10 PASS = 10 pts

```
composite = (5/5 * 60) + (3/3 * 30) + (10/10 * 10) = 60 + 30 + 10 = 100
```

**Score: 100** | Golden: YES
**Confirmed prediction**: 18/18 — prediction correct.

---

## V-03 — Role Sequence + C-17/C-18

**Variation axis**: Two-phase (Sizing Analyst Phase 1 / Risk Assessor Phase 2) + C-17 adjacent in
Phase 2 table + C-18 column header in Phase 2 sensitivity table.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Surface area enumerated | PASS | Phase 1 §1.2: "List each integration point individually... Provide a total count. Format: '[Point A], [Point B] — N integration points.'" |
| C-02 | Complexity tier on-scale | PASS | Phase 1 §1.3: "Assign exactly one tier: LOW / MEDIUM / HIGH / XL. No other vocabulary." |
| C-03 | Inertia check present | PASS | Phase 1 §1.1: requires named workaround + cost direction; "An output that names the workaround without a cost direction has not completed this section." |
| C-04 | Confidence stated with basis | PASS | Phase 2 §2.1 table: Confidence Level + Basis field with "Concrete; names a specific established thing" |
| C-05 | Signal boundary respected | PASS | "No task lists, sprint assignments, owner names, or milestone dates appear anywhere." — explicit prohibition |
| C-06 | Team-size names disciplines | PASS | Phase 1 §1.5: "'1 backend, 1 platform, 0.5 PM.' Headcount alone ('3 engineers') fails." |
| C-07 | Timeline as sprint range | PASS | Phase 1 §1.6: "Give a sprint range: 'X–Y sprints.' No calendar dates. No point estimates." |
| C-08 | Primary driver identified | PASS | Phase 1 §1.4: "Name the one or two specific factors... Generic justification ('it's a large feature') fails." |
| C-09 | Sensitivity tier up + down | PASS | Phase 2 §2.2 table has explicit Tier UP and Tier DOWN rows |
| C-10 | Confidence calibration | PASS | Phase 2 §2.3: "State what information or result would materially raise or lower the stated confidence level." |
| C-11 | Confidence gap named | PASS | Phase 2 §2.1 Gap field with adjacent WRONG/CORRECT: "WRONG: 'Some areas of the integration are not yet verified.' CORRECT: 'Gap: the auth service's token-refresh behavior under network partition is undocumented and was not verified by the sizing analyst.'" |
| C-12 | Sensitivity single named conditions | PASS | Phase 2 §2.2 condition requirements item 1: "Single named scenario — not a list of factors" |
| C-13 | Sensitivity names explicit tier destination | PASS | Phase 2 §2.2 column: "Destination Tier [LOW/MEDIUM/HIGH/XL — must differ from Phase 1 tier]" |
| C-14 | Sensitivity conditions falsifiable | PASS | Phase 2 §2.2 "How to settle it" column + condition item 4: "'If requirements change' cannot be investigated. 'If offline sync across platforms is confirmed' can be settled by asking the PM." |
| C-15 | Basis and gap non-overlapping | PASS | Phase 2 §2.1 adjacent WRONG/CORRECT: "WRONG: Basis: API contract is confirmed. Gap: API contract is not yet confirmed. — Gap negates the basis on the same dimension." CORRECT shown. Also structurally reinforced: the assessor's role is to find what Phase 1 left open — conflation violates the role assignment itself. Double guard. |
| C-16 | Sensitivity destination differs from current tier | PASS | Phase 2 §2.2 WRONG/CORRECT adjacent to Destination Tier column: "WRONG: Phase 1 assigned HIGH. Assessor writes 'Tier UP → Destination: HIGH.' — No movement. Null sensitivity. Fails regardless of whether the condition is well-formed. CORRECT: HIGH → UP must be XL; DOWN must be MEDIUM or LOW." Column header also encodes the rule. |
| C-17 | High-risk constraints carry inline failure examples | PASS | C-11 WRONG/CORRECT in Phase 2 §2.1 at Gap field. C-15 WRONG/CORRECT in Phase 2 §2.1 at Basis/Gap block. C-16 WRONG/CORRECT in Phase 2 §2.2 below Destination Tier column. All adjacent at generation time (Phase 2 is where these fields are generated). |
| C-18 | Constraints encoded as structural features | PASS | Phase 2 §2.2 column header "Destination Tier [LOW/MEDIUM/HIGH/XL — must differ from Phase 1 tier]" encodes C-13 and C-16 constraints structurally. |

**Essential**: 5/5 PASS = 60 pts
**Recommended**: 3/3 PASS = 30 pts
**Aspirational**: 10/10 PASS = 10 pts

```
composite = (5/5 * 60) + (3/3 * 30) + (10/10 * 10) = 60 + 30 + 10 = 100
```

**Score: 100** | Golden: YES
**Confirmed prediction**: 18/18 — prediction correct.

**Note**: V-03 surfaces a structural property not present in V-02: role separation provides a second independent guard for C-15. The assessor is defined as finding what the analyst left open — conflating basis and gap is not just a formatting rule violation, it is a role violation. C-15 benefits from two enforcement mechanisms. This is architecturally distinct from V-02 and V-05 which rely on the inline example alone.

---

## V-04 — Lifecycle Gate + C-17 Inside the Checklist

**Variation axis**: Five lifecycle phases with anti-pattern gate at Phase 5. WRONG/CORRECT
examples for C-11, C-15, C-16 appear in the Phase 5 gate — after Phase 4 where those fields
are generated. Sensitivity is prose only. C-18 absent.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Surface area enumerated | PASS | Phase 2: "List every integration point individually... End with a total count. A general description without individually named points fails." |
| C-02 | Complexity tier on-scale | PASS | Phase 3: "Assign exactly one tier from the authorized vocabulary: LOW / MEDIUM / HIGH / XL. No other vocabulary. 'MODERATE', '3/5', 'fairly involved' all fail." |
| C-03 | Inertia check present | PASS | Phase 1: names workaround + cost direction required; "Naming the workaround without a cost direction does not complete this phase." |
| C-04 | Confidence stated with basis | PASS | Phase 4 Confidence Basis: "What IS established or verified. Name the specific source of current confidence. Must be concrete." |
| C-05 | Signal boundary respected | PASS | Opening: "This output is a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates." |
| C-06 | Team-size names disciplines | PASS | Phase 4 Team-Size Signal: "'1 backend, 1 platform, 0.5 PM' is correct. '3 engineers' fails — name the disciplines." |
| C-07 | Timeline as sprint range | PASS | Phase 4 Timeline Signal: "Sprint range. 'X–Y sprints.' Not a calendar date. Not a single number." |
| C-08 | Primary driver identified | PASS | Phase 3: "Name the primary driver: the one or two specific factors that most determine this tier. Generic justification fails." |
| C-09 | Sensitivity tier up + down | PASS | Phase 4 Sensitivity — Tier Up and Tier Down both required |
| C-10 | Confidence calibration | PASS | Phase 4: "Name what information or discovery would materially raise or lower the confidence level." |
| C-11 | Confidence gap named | PASS | Gate 5 explicitly guards: "Gap names a specific unknown — not a vague gesture at uncertainty." WRONG/CORRECT present. Criterion is guarded. |
| C-12 | Sensitivity single named conditions | PASS | Phase 4: "One specific condition that would raise the complexity tier." Gate 8 additionally guards falsifiability. |
| C-13 | Sensitivity names explicit tier destination | PASS | Phase 4: "State the destination tier explicitly: 'Tier rises to [LEVEL].' ... 'Tier drops to [LEVEL].'" |
| C-14 | Sensitivity conditions falsifiable | PASS | Gate 8: "'If requirements change' cannot be investigated. 'If offline sync is confirmed as in scope' can." |
| C-15 | Basis and gap non-overlapping | PASS | Gate 6 WRONG/CORRECT: "WRONG: 'Basis: API contract is confirmed. Gap: API contract is not yet verified.' — Same dimension, flipped sign. CORRECT: Basis names one confirmed area. Gap names a different, unresolved area." Criterion guarded by the gate. |
| C-16 | Sensitivity destination differs from current tier | PASS | Gate 7 WRONG/CORRECT: "WRONG: Current tier is MEDIUM. Tier-up condition says 'rises to MEDIUM.' No movement — null sensitivity. Fails. CORRECT: MEDIUM → up must name HIGH or XL; down must name LOW." Criterion guarded. |
| C-17 | High-risk constraints carry inline failure examples | FAIL | C-11, C-15, C-16 WRONG/CORRECT examples appear in Phase 5 gate. The fields they illustrate are generated in Phase 4. C-17 requires examples "at the point of the constraint so that the output field cannot be satisfied without the failure mode being active at generation time." Gate placement is post-generation: a model generating the Gap field in Phase 4 has not yet encountered the Gate 5 example. "From the constraint alone" (Phase 4's Gap field definition) the model cannot tell what a failing output looks like. |
| C-18 | Constraints encoded as structural features | FAIL | Phase 4 sensitivity is entirely prose: "Sensitivity — Tier Up: One specific condition... State the destination tier explicitly: 'Tier rises to [LEVEL].'" No table. No column headers. Tier-destination violations are not visible at the field level. |

**Essential**: 5/5 PASS = 60 pts
**Recommended**: 3/3 PASS = 30 pts
**Aspirational**: 8/10 PASS (C-17 FAIL, C-18 FAIL) = 8 pts

```
composite = (5/5 * 60) + (3/3 * 30) + (8/10 * 10) = 60 + 30 + 8 = 98
```

**Score: 98** | Golden: YES (all essential pass, composite >= 80)
**Confirmed prediction**: C-17 and C-18 both fail — prediction correct. Composite is 98, not 100.
Gate-level examples do not satisfy C-17's adjacency requirement. Post-generation checking is confirmed as insufficient.

---

## V-05 — Full Synthesis: Inertia-First + Table Schema + C-17 at All Three Targets

**Variation axis**: Inertia-first framing (Step 1 before estimates) + Step 8 sensitivity table
with column header encoding + WRONG/CORRECT adjacent to C-11, C-15, C-16.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Surface area enumerated | PASS | Step 2: "Name each one individually... End with a total count: 'N integration points.' A general description without named points and a count fails." |
| C-02 | Complexity tier on-scale | PASS | Step 3: "Assign exactly one tier from this set: LOW / MEDIUM / HIGH / XL. No other vocabulary is valid. 'MODERATE', '3/5', 'complex' all fail. This vocabulary is load-bearing — downstream skills parse it by exact string match." |
| C-03 | Inertia check present | PASS | Step 1: names workaround + cost direction; "Mentioning the workaround in passing without a cost direction fails." Explicitly first, before any estimates. |
| C-04 | Confidence stated with basis | PASS | Step 7: "Basis — what IS established or verified. The specific thing that grounds your confidence. Must be concrete and named." |
| C-05 | Signal boundary respected | PASS | Opening: "Do not include task lists, sprint assignments, owner names, or milestone dates anywhere in your output." |
| C-06 | Team-size names disciplines | PASS | Step 5: "Name the specialist disciplines required with allocation fractions. Example: '1 backend engineer, 1 platform engineer, 0.5 PM.' Headcount alone ('3 engineers') fails." |
| C-07 | Timeline as sprint range | PASS | Step 6: "Give a sprint range estimate: 'X–Y sprints.' Not a calendar date. Not a single fixed number." |
| C-08 | Primary driver identified | PASS | Step 4: "'It's complex' or 'the scope is large' are not drivers. Name the factor." |
| C-09 | Sensitivity tier up + down | PASS | Step 8: "State exactly one condition that would push the complexity tier UP and exactly one that would push it DOWN." |
| C-10 | Confidence calibration | PASS | Step 9: "Name what information or investigation result would materially raise or lower your stated confidence level." |
| C-11 | Confidence gap named | PASS | Step 7 adjacent WRONG/CORRECT: "WRONG: 'Some integration aspects remain unclear.' CORRECT: 'Gap: the failover contract of the notification dispatch queue under concurrent write load is undocumented.'" — at Gap field, generation time. |
| C-12 | Sensitivity single named conditions | PASS | Step 8 condition #1: "'Several factors could push the tier up' fails; 'tier rises to XL if offline sync is required' passes." |
| C-13 | Sensitivity names explicit tier destination | PASS | Step 8 column header "Destination Tier [LOW/MEDIUM/HIGH/XL — must differ from Step 3 tier]" + condition #2: "Explicit destination tier — fill the column with LOW, MEDIUM, HIGH, or XL." |
| C-14 | Sensitivity conditions falsifiable | PASS | Step 8 "How to settle it" column + condition #4: "'If requirements change' is not falsifiable. 'If offline sync is confirmed as in scope' is — someone can verify it." |
| C-15 | Basis and gap non-overlapping | PASS | Step 7 adjacent WRONG/CORRECT: "WRONG: 'Basis: API contract is confirmed. Gap: API contract is not yet verified.' — Same dimension, flipped polarity. Gap negates the basis rather than extending to a different unknown. Fails. CORRECT: Basis names what is structurally clear... Gap names a separate behavioral unknown... Different areas." |
| C-16 | Sensitivity destination differs from current tier | PASS | Step 8 condition #3 adjacent WRONG/CORRECT: "WRONG: Step 3 tier is HIGH. Writing 'Tier UP → Destination: HIGH.' The tier does not change. This is a null sensitivity — not a condition, a restatement. CORRECT: Step 3 tier is HIGH → UP destination must be XL; DOWN destination must be MEDIUM or LOW." Column header encodes the same rule structurally. |
| C-17 | High-risk constraints carry inline failure examples | PASS | C-11 WRONG/CORRECT in Step 7 at Gap field. C-15 WRONG/CORRECT in Step 7 at Basis/Gap block. C-16 WRONG/CORRECT in Step 8 at condition #3 adjacent to Destination Tier column. All three failure mode examples appear at their constraint, active at generation time. |
| C-18 | Constraints encoded as structural features | PASS | Step 8 table column header "Destination Tier [LOW/MEDIUM/HIGH/XL — must differ from Step 3 tier]" encodes C-13 (tier vocabulary) and C-16 (must-differ rule) structurally. Violation observable at the column level without prose cross-referencing. |

**Essential**: 5/5 PASS = 60 pts
**Recommended**: 3/3 PASS = 30 pts
**Aspirational**: 10/10 PASS = 10 pts

```
composite = (5/5 * 60) + (3/3 * 30) + (10/10 * 10) = 60 + 30 + 10 = 100
```

**Score: 100** | Golden: YES
**Confirmed prediction**: 18/18 — prediction correct.

---

## Ranking

| Rank | Variation | Score | Golden | C-17 | C-18 | Notes |
|------|-----------|-------|--------|------|------|-------|
| 1 (tie) | V-02 | 100 | YES | PASS | PASS | Table schema; complete C-17/C-18 at all three targets |
| 1 (tie) | V-03 | 100 | YES | PASS | PASS | Role separation adds structural C-15 guard; double enforcement |
| 1 (tie) | V-05 | 100 | YES | PASS | PASS | Inertia-first + table schema + full C-17; synthesis variation |
| 4 | V-01 | 99 | YES | PASS | FAIL | Prose sensitivity only; C-18 is the single separator from 100 |
| 5 | V-04 | 98 | YES | FAIL | FAIL | Gate placement is post-generation; examples arrive too late |

All five variations are golden. C-17 and C-18 are the discriminating criteria: they separate
98/99 from 100, not passing from golden.

---

## Excellence Signals

### Pattern 1 — Adjacency is load-bearing for C-17: gate-level placement confirmed insufficient (V-04)

V-04 is the structural test for C-17's "at generation time" clause. The WRONG/CORRECT examples
are well-formed and address exactly the right failure modes — but they live in Phase 5 (the
anti-pattern gate), while the fields they govern are generated in Phase 4.

The score confirms: gate-level examples do not satisfy C-17. A checklist that catches violations
after output generation is not equivalent to a constraint that shapes generation. "From the
constraint alone" (Phase 4's field definition), a reader cannot tell what a failing output looks
like — they would need to read ahead to Phase 5. C-17 fails.

The practical implication: if you want a failure example to prevent a specific failure mode, the
example must appear where the model writes the field. Gate verification is useful for catching
drift; it is not a substitute for adjacent constraint encoding.

### Pattern 2 — C-18 is the single binary separator between 99 and 100

V-01 satisfies C-17 completely — WRONG/CORRECT examples are adjacent, concrete, and cover all
three documented failure modes (C-11, C-15, C-16). It still scores 99.

The single criterion separating V-01 from V-02/V-03/V-05 is the presence of a column header
carrying the tier-movement constraint. The column header "Destination Tier [LOW/MEDIUM/HIGH/XL —
must differ from current tier]" does something that an adjacent WRONG/CORRECT example cannot: it
makes the constraint visible at the output skeleton level, before content is generated.

C-17 and C-18 are genuinely independent. C-17 answers: "Does the reader know what a wrong output
looks like?" C-18 answers: "Is the rule embedded in the structure itself?" You can fully satisfy
C-17 (adjacent, named, all three targets) and still fail C-18 if the format is prose.

### Pattern 3 — Role separation as a structural C-15 guard (V-03 exclusive)

V-03 is the only variation where C-15 is guarded by two independent mechanisms. The inline
WRONG/CORRECT example provides guard #1 — the same as V-02 and V-05. The role contract provides
guard #2: the assessor is explicitly defined as finding what the analyst left open. Conflating
basis and gap violates the role before it violates the rule.

This is architecturally distinct because the structural property would hold even if the
WRONG/CORRECT example were removed. The role design encodes the non-overlap constraint in the
job description itself — a kind of C-18 for C-15 at the prompt-architecture level rather than
the output-field level.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["gate-level placement fails C-17 adjacency requirement: WRONG/CORRECT examples in a post-generation verification checklist do not constrain generation — the example must appear at the field definition, active at the moment the model writes the field", "role separation as structural C-15 guard: two-phase analyst/assessor design makes basis/gap conflation a role violation by definition, providing enforcement independent of inline examples — the assessor cannot re-use what the analyst confirmed without failing the role contract itself"]}
```
