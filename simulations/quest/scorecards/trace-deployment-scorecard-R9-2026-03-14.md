# trace-deployment — Round 9 Scorecard

**Rubric**: v8 | **Total**: 175 pts | **Variations**: V-01 through V-05

---

## Criterion-by-Criterion

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | FAIL | FAIL | PASS | PASS | FAIL |
| C-15 | PASS | PASS | FAIL | FAIL | PASS |
| C-16 | FAIL | FAIL | PASS | PASS | FAIL |
| C-17 | PASS | PASS | FAIL | FAIL | PASS |
| C-18 | FAIL | FAIL | PASS | PASS | FAIL |
| C-19 | PASS | PASS | FAIL | FAIL | PASS |
| C-20 | PASS | PASS | FAIL | FAIL | PASS |
| C-21 | FAIL | FAIL | PASS | PASS | FAIL |
| C-22 | FAIL | FAIL | FAIL | **PASS** | FAIL |
| C-23 | FAIL | PASS | FAIL | FAIL | PASS |
| C-24 | FAIL | FAIL | FAIL | **PASS** | FAIL |
| C-25 | PASS | FAIL | FAIL | FAIL | FAIL |

---

## Composite Scores

| Variation | Essential | Rec | Asp | **Total** | Golden |
|-----------|-----------|-----|-----|-----------|--------|
| V-01 (prose + C-25) | 60 | 30 | 50 | **140/175** | YES |
| V-02 (prose + C-23) | 60 | 30 | 50 | **140/175** | YES |
| V-03 (template + C-21) | 60 | 30 | 45 | **135/175** | YES |
| V-04 (template + C-24) | 60 | 30 | 55 | **150/175** | YES |
| V-05 (prose + both voices) | 60 | 30 | 50 | **140/175** | YES |

**Ranking**: V-04 > V-01 = V-02 = V-05 > V-03

---

## Key Findings

**V-04 breaks to 150 — new ceiling.** First C-24 confirmation: colloquial section headers + bare field labels in a single variation adds 10 pts over single-axis template. Template path ceiling is now 150/175.

**V-05 confirms C-23 and C-25 are mutually exclusive.** Role block with both inertia narrative and operational framing: C-23 passes (inertia present), C-25 fails (inertia present violates "without first-person incident narrative"). No single variation can pass both. Prose ceiling is hard-capped at 140.

**Path map:**
- Prose (any persona voice): 140 ceiling
- Template + colloquial + inline prose: 135
- Template + colloquial + bare: **150**
- Template + both voices: unreachable (C-15 blocks prose-path criteria on template path)

---

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["c24-confirmed-colloquial-bare-labels-template-ceiling-150", "c23-c25-mutually-exclusive-inertia-presence-violates-c25-without-condition"]}
```
rative return instruction | **FAIL** | **FAIL** | PASS | PASS | **FAIL** |
| C-15 | Prose-instruction saturation closes structural criteria | PASS | PASS | **FAIL** | **FAIL** | PASS |
| C-16 | Gate-free coverage via template field scaffolding | **FAIL** | **FAIL** | PASS | PASS | **FAIL** |
| C-17 | C-15 at minimum prose density | PASS | PASS | **FAIL** | **FAIL** | PASS |
| C-18 | C-14 and C-16 simultaneously | **FAIL** | **FAIL** | PASS | PASS | **FAIL** |
| C-19 | C-15 disqualifier by contextual failure-mode framing | PASS | PASS | **FAIL** | **FAIL** | PASS |
| C-20 | C-19 without inertia narrative source | PASS | PASS | **FAIL** | **FAIL** | PASS |
| C-21 | Template path, colloquial register | **FAIL** | **FAIL** | PASS | PASS | **FAIL** |
| C-22 | Template path, bare field labels | **FAIL** | **FAIL** | **FAIL** | PASS | **FAIL** |
| C-23 | Role-block inertia orthogonal to C-20 disqualifier source | **FAIL** | PASS | **FAIL** | **FAIL** | PASS |
| C-24 | C-21 and C-22 jointly satisfied | **FAIL** | **FAIL** | **FAIL** | **PASS** | **FAIL** |
| C-25 | Present-tense operational persona passes C-20 as distinct role-block voice | PASS | **FAIL** | **FAIL** | **FAIL** | **FAIL** |

---

### Detailed Criterion Notes

#### C-09 (all PASS)
All five: Gap table with Rank, Phase, Gap summary, Severity, Why columns. Comparative return instruction ("compare each gap against the other three" or equivalent) closes this on all paths.

#### C-12 (all PASS)
V-01: "Current practice: X / Known failure mode: Y" in role block; prose body reinforces "this is your baseline." V-02: No operational fields in role block, but body instruction "State the current deployment practice... this is your baseline" establishes baseline before gap analysis — satisfies "or equivalent" language. V-03/V-04: "Current practice: [...]" and "Known failure mode: [...]" as template fields before phase sections. V-05: Both role-block inertia narrative (implicit baseline from incidents) AND body instruction "this is your baseline."

#### C-14 rationale (V-01, V-02, V-05 FAIL)
All prose paths place the gap table instruction at the end of the prompt. C-14 requires the table to appear as an empty skeleton *before* Phase 1. Prose path carries no template apparatus — no front-loaded skeleton is architecturally possible.

#### C-15 rationale (V-03, V-04 FAIL)
Template path achieves structural criteria through field scaffolding, not prose-instruction saturation. C-15 requires "without structural template apparatus." Template fields, section headers, and skeleton structure disqualify regardless of what prose appears alongside.

#### C-16 rationale (V-01, V-02, V-05 FAIL)
Prose path carries no template field count architecture. C-16 requires field-count floors (≥3 Check-NN, ≥4 Step-NN, ≥2 Validation-NN, Trigger + Rollback-NN + Verification, automation hook fields) — these are structural requirements, not achievable through prose instructions.

#### C-18 (V-03, V-04 PASS; others FAIL)
V-03 and V-04 both satisfy C-14 and C-16 simultaneously. Colloquial "leave this blank now" guard is skeleton commitment text, not GATE enforcement text — gate-free architecture is preserved. V-01/V-02/V-05 fail because C-14 and C-16 both fail on prose path.

#### C-20 rationale (prose path PASS, template path FAIL)
Template path fails C-15 → fails C-19 → fails C-20 (prerequisite chain). Prose path (V-01, V-02, V-05): disqualifiers are all domain-vocabulary-only ("'price feed healthy' does not name a probe or measurable threshold"; "'SKU manifest invalid' does not name a measurable threshold or probe result"). No incident reference or "we learned..." framing in any disqualifier position. C-20 PASS for all prose variations.

#### C-21 rationale (V-03, V-04 PASS; others FAIL)
C-21 requires C-14, C-16, C-18 all pass (template path). Prose path fails all three. V-03: colloquial headers ("Before you touch anything:", "Roll it out:", "Did it work:", "If you need to back out:") and colloquial field labels ("check-1:", "step-1:", "validation-1:") ✓. V-04: same colloquial structure per design description ✓.

#### C-22 rationale (V-04 PASS; V-03 FAIL; others FAIL)
C-22 requires template path (C-14/C-16/C-18 pass) AND bare field labels with no inline prose. V-04: bare identifiers only ("check-1:", "step-1:", "validation-1:", etc.); no embedded instruction content within any field. V-03: inline prose throughout every field ("What are you confirming? | Passes when: [name the observable artifact or state — not 'environment is ready'] | Fails when: [specific symptom]") — disqualifies under C-22's bare-label requirement.

#### C-23 rationale (V-02, V-05 PASS; others FAIL)
C-23 requires C-20 to pass AND inertia narrative in role block. Template path (V-03/V-04): C-20 fails, prerequisite unmet. V-01: Role block is "Current practice: X. Known failure mode: Y." — present-tense operational, no "we learned / after the outage we found" framing. FAIL. V-02: "After an inventory sync outage we learned... After a price feed lock incident we found..." — explicit first-person incident framing. Disqualifiers remain domain-vocabulary-only. PASS. V-05: Role block contains inertia narrative ("After X we learned...") PLUS operational framing ("Current practice: X. Known failure mode: Y."). Inertia is present → C-23 PASS.

#### C-24 rationale (V-04 PASS; all others FAIL) ← FIRST CONFIRMED PASS
V-04: C-21 PASS (colloquial register) AND C-22 PASS (bare field labels) in a single variation. This is the first confirmed simultaneous satisfaction. C-24 PASS. Template path ceiling reaches 150/175. All other variations fail C-24 because they fail at least one of C-21/C-22.

#### C-25 rationale (V-01 PASS; all others FAIL)
C-25 requires C-20 to pass AND role block uses present-tense operational baseline framing WITHOUT first-person incident narrative.

Template path (V-03/V-04): C-20 fails — prerequisite unmet. Role-block content is irrelevant.

V-01: C-20 passes. Role block: "Current practice: {topic} deployments run from a shared runbook with manual gate sign-offs... Known failure mode: gates clear under time pressure without observable verification..." — present-tense operational, no inertia. PASS.

V-02: C-20 passes. Role block contains inertia ("After an inventory sync outage we learned... After a price feed lock incident we found...") — first-person incident narrative IS present. C-25's "without first-person incident narrative" condition violated. FAIL.

V-05: C-20 passes. Role block contains BOTH inertia narrative AND operational framing. Inertia narrative IS present → C-25's "without" condition violated. FAIL. (C-23 PASS, C-25 FAIL — the two criteria are mutually exclusive.)

**Finding**: C-23 and C-25 cannot both pass in a single variation. C-23 requires inertia-narrative presence; C-25 requires inertia-narrative absence. These are anti-correlated properties — no role block can simultaneously satisfy both pass conditions. V-05 confirms mutual exclusion.

---

## Aspirational Subtotals

| Variation | Passing aspirational criteria | Pts |
|-----------|-------------------------------|-----|
| V-01 | C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, **C-25** | 50 |
| V-02 | C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, **C-23** | 50 |
| V-03 | C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-21 | 45 |
| V-04 | C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-21, **C-22**, **C-24** | 55 |
| V-05 | C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, **C-23** | 50 |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 60 | 30 | 50 | **140/175** | YES |
| V-02 | 60 | 30 | 50 | **140/175** | YES |
| V-03 | 60 | 30 | 45 | **135/175** | YES |
| V-04 | 60 | 30 | 55 | **150/175** | YES |
| V-05 | 60 | 30 | 50 | **140/175** | YES |

**Ranking**: V-04 > V-01 = V-02 = V-05 > V-03

All variations pass the golden threshold (all essential pass + composite ≥ 80).

---

## Excellence Signals

**Top variation: V-04 at 150/175 — new ceiling**

V-04 is the first variation to satisfy C-24 (colloquial register AND bare field labels jointly). The distinguishing properties:
- Colloquial section headers ("Before you touch anything:", "Roll it out:", etc.) satisfy C-21
- Bare field identifiers with zero inline instruction prose satisfy C-22
- Both axes satisfied simultaneously in a single variation → C-24 PASS
- 10 aspirational pts added over the single-axis template variations (V-03 at 135)

The template path ceiling is now confirmed at 150/175. It cannot advance until a prose-path criterion (C-23, C-25, or a future C-26+) becomes achievable on the template path, which is architecturally blocked by C-15's "without structural template apparatus" condition.

**C-23 and C-25 are mutually exclusive per V-05**

V-05's role block (both inertia + operational framing) confirms: C-23 passes (inertia present), C-25 fails (inertia also present, violating "without first-person incident narrative"). The two criteria cannot co-exist in a single variation. The prose path has two parallel routes to 140 — C-23 route (V-02 pattern) and C-25 route (V-01 pattern) — but not a combined route to 145. This is a hard ceiling for single-variation prose path.

**Prose ceiling confirmed at 140**

Three prose variations (V-01, V-02, V-05) all score 140. The prose path cannot advance without a new aspirational criterion that can be satisfied in combination with C-23 or C-25 independently. Future rubric additions (C-26+) may create a 145 or 150 prose ceiling.

**C-25 vs C-23 as probe axes:**
- V-01 (C-25 route): present-tense operational baseline in role block
- V-02 (C-23 route): first-person inertia narrative in role block
- V-05 (both): confirms mutual exclusion, score equals single-axis prose ceiling

---

## Path Map (R9 state)

| Path | Ceiling | Limiting axis |
|------|---------|---------------|
| Prose + operational persona (C-25) | 140/175 | C-14/C-16/C-18 unreachable; C-23/C-25 mutually exclusive |
| Prose + inertia persona (C-23) | 140/175 | Same |
| Template + colloquial + inline prose (C-21 only) | 135/175 | C-22 blocked by inline prose |
| Template + colloquial + bare labels (C-24) | **150/175** | C-15/C-19/C-20/C-23/C-25 unreachable on template path |
| Prose + both voices (C-23 + C-25 test) | 140/175 | C-25 fails; no additive gain over single-voice |

---

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["c24-confirmed-colloquial-bare-labels-template-ceiling-150", "c23-c25-mutually-exclusive-inertia-presence-violates-c25-without-condition"]}
```
