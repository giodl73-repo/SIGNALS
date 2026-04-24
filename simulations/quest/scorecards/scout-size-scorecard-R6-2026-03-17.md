## Scorecard — scout-size Round 6

### Scoring model reminder
```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/15 × 10)
```

---

## V-01 — Synthesis Named Chain

**Axis**: C-22 mechanism only. Gate-embedded hypothesis + verdict close templates that require `"PRE-FLIGHT GATE"` by label. Intentionally leaves INERTIA CHECK unguarded and uses bare exclusion guards (C-20 fail, C-23 expected fail).

| ID | Weight | Criterion | Verdict | Evidence |
|----|--------|-----------|---------|----------|
| C-01 | essential | Complexity tier vocabulary | **PASS** | `LOW / MEDIUM / HIGH / XL` present |
| C-02 | essential | Sprint range | **PASS** | `N–M sprints` format enforced |
| C-03 | essential | Surface area total row | **PASS** | Table with `**Total**` row required |
| C-04 | essential | Inertia check | **PASS** | INERTIA CHECK section with Workaround + cost direction |
| C-05 | essential | Confidence with basis | **PASS** | Confidence + Basis fields present |
| C-06 | recommended | Specializations named | **PASS** | `specialist disciplines + FTE fractions + implementation ownership per role` |
| C-07 | recommended | Complexity driver | **PASS** | `Primary driver` field required |
| C-08 | recommended | AMEND modifies output | **PASS** | No AMEND present — default pass |
| C-09 | aspirational | Scope exclusions stated | **PASS** | PRE-FLIGHT GATE out-of-scope boundary field |
| C-10 | aspirational | Break-even signal | **PASS** | PRE-FLIGHT GATE break-even field |
| C-11 | aspirational | Specialization ownership | **PASS** | Team signal requires ownership per role |
| C-12 | aspirational | Named unknowns | **PASS** | OPEN UNKNOWNS with typed fields |
| C-13 | aspirational | Cross-signal synthesis | **PASS** | Synthesis requires combining ≥2 dimensions |
| C-14 | aspirational | Unknowns dedicated section | **PASS** | OPEN UNKNOWNS section; CONFIDENCE says "Do not list unknowns here. Unknowns go in OPEN UNKNOWNS below." |
| C-15 | aspirational | Hypothesis-revision lifecycle | **PASS** | Hypothesis in PRE-FLIGHT GATE; synthesis confirms/revises citing gate |
| C-16 | aspirational | AMEND cascades to synthesis | **PASS** | No AMEND — default pass |
| C-17 | aspirational | Sections name failure modes | **PASS** | SYNTHESIS anti-pattern blockquote present |
| C-18 | aspirational | Pre-analysis gate | **PASS** | PRE-FLIGHT GATE before all sections; 3 fields; STOP instruction |
| C-19 | aspirational | Prohibition guards (min 1) | **PASS** | SURFACE AREA and CONFIDENCE carry prohibitions |
| C-20 | aspirational | Complete closure mesh | **FAIL** | INERTIA CHECK carries no prohibition against scope exclusions — unguarded adjacent section |
| C-21 | aspirational | Gate elicits hypothesis | **PASS** | Hypothesis is field 3 inside PRE-FLIGHT GATE; synthesis names gate by label |
| C-22 | aspirational | Synthesis names gate at both ends | **PASS** | Anchor: "look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there"; verdict close templates: "The preliminary hypothesis committed in PRE-FLIGHT GATE..." |
| C-23 | aspirational | Guards name canonical home | **FAIL** | SURFACE AREA: "Do not include scope exclusions here." — bare exclusion, no home reference. No guard redirects to PRE-FLIGHT GATE by name. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 13/15

```
composite = (5/5 × 60) + (3/3 × 30) + (13/15 × 10) = 60 + 30 + 8.67 = 98.67
```

**Band**: Gold | **Score: 98.67**

---

## V-02 — Navigational Guards

**Axis**: C-23 mechanism only. Full bilateral closure with navigational guards naming canonical home. Intentionally places hypothesis in standalone MANDATORY OPENING (C-21 fail, C-22 automatically fails as C-21 prerequisite unmet).

| ID | Weight | Criterion | Verdict | Evidence |
|----|--------|-----------|---------|----------|
| C-01 | essential | Complexity tier vocabulary | **PASS** | `LOW / MEDIUM / HIGH / XL` present |
| C-02 | essential | Sprint range | **PASS** | `N–M sprints` required |
| C-03 | essential | Surface area total row | **PASS** | Total row required |
| C-04 | essential | Inertia check | **PASS** | INERTIA CHECK with workaround + cost direction |
| C-05 | essential | Confidence with basis | **PASS** | Confidence + Basis present |
| C-06 | recommended | Specializations named | **PASS** | Disciplines + ownership per role |
| C-07 | recommended | Complexity driver | **PASS** | Primary driver required |
| C-08 | recommended | AMEND modifies output | **PASS** | No AMEND — default pass |
| C-09 | aspirational | Scope exclusions stated | **PASS** | PRE-FLIGHT GATE out-of-scope boundary |
| C-10 | aspirational | Break-even signal | **PASS** | PRE-FLIGHT GATE break-even field |
| C-11 | aspirational | Specialization ownership | **PASS** | Ownership area per role required |
| C-12 | aspirational | Named unknowns | **PASS** | OPEN UNKNOWNS with typed fields |
| C-13 | aspirational | Cross-signal synthesis | **PASS** | Synthesis requires ≥2 dimensions |
| C-14 | aspirational | Unknowns dedicated section | **PASS** | OPEN UNKNOWNS section; CONFIDENCE explicitly closed with navigational redirect |
| C-15 | aspirational | Hypothesis-revision lifecycle | **PASS** | MANDATORY OPENING has hypothesis before analysis; synthesis confirms/revises |
| C-16 | aspirational | AMEND cascades to synthesis | **PASS** | AMEND cascade instruction present in SYNTHESIS; no active AMEND = default pass |
| C-17 | aspirational | Sections name failure modes | **PASS** | SYNTHESIS anti-pattern and OPEN UNKNOWNS failure mode blockquotes both present |
| C-18 | aspirational | Pre-analysis gate | **PASS** | PRE-FLIGHT GATE present before analysis; STOP instruction; scope + break-even fields |
| C-19 | aspirational | Prohibition guards (min 1) | **PASS** | CONFIDENCE and SURFACE AREA carry prohibition guards |
| C-20 | aspirational | Complete closure mesh | **PASS** | INERTIA CHECK: "scope was resolved in PRE-FLIGHT GATE, not in analysis steps"; SURFACE AREA: same; COMPLEXITY: scope exclusions + unknowns both guarded; CONFIDENCE: unknowns guarded; SYNTHESIS: both unknowns and scope guarded; OPEN UNKNOWNS: closed bilaterally |
| C-21 | aspirational | Gate elicits hypothesis | **FAIL** | Hypothesis is in standalone MANDATORY OPENING (separate section after gate), not inside PRE-FLIGHT GATE block |
| C-22 | aspirational | Synthesis names gate at both ends | **FAIL** | C-21 prerequisite unmet — synthesis references "MANDATORY OPENING: PRELIMINARY HYPOTHESIS," not PRE-FLIGHT GATE |
| C-23 | aspirational | Guards name canonical home | **PASS** | INERTIA CHECK: "scope was resolved in PRE-FLIGHT GATE, not in analysis steps"; SURFACE AREA, COMPLEXITY, SYNTHESIS all use navigational redirect naming PRE-FLIGHT GATE or OPEN UNKNOWNS by label |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 13/15

```
composite = (5/5 × 60) + (3/3 × 30) + (13/15 × 10) = 60 + 30 + 8.67 = 98.67
```

**Band**: Gold | **Score: 98.67**

---

## V-03 — Minimal Combination

**Axes**: C-22 + C-23 combined. Gate-embedded hypothesis + verdict close templates require gate label + all guards are navigational redirects. No self-check machinery.

| ID | Weight | Criterion | Verdict | Evidence |
|----|--------|-----------|---------|----------|
| C-01 | essential | Complexity tier vocabulary | **PASS** | `LOW / MEDIUM / HIGH / XL` |
| C-02 | essential | Sprint range | **PASS** | `N–M sprints` |
| C-03 | essential | Surface area total row | **PASS** | Total row required |
| C-04 | essential | Inertia check | **PASS** | INERTIA CHECK section |
| C-05 | essential | Confidence with basis | **PASS** | Confidence + Basis |
| C-06 | recommended | Specializations named | **PASS** | Disciplines + ownership per role |
| C-07 | recommended | Complexity driver | **PASS** | Primary driver |
| C-08 | recommended | AMEND modifies output | **PASS** | No AMEND — default pass |
| C-09 | aspirational | Scope exclusions stated | **PASS** | PRE-FLIGHT GATE out-of-scope boundary |
| C-10 | aspirational | Break-even signal | **PASS** | PRE-FLIGHT GATE break-even field |
| C-11 | aspirational | Specialization ownership | **PASS** | Ownership per role required |
| C-12 | aspirational | Named unknowns | **PASS** | OPEN UNKNOWNS typed fields |
| C-13 | aspirational | Cross-signal synthesis | **PASS** | ≥2 dimensions required in synthesis |
| C-14 | aspirational | Unknowns dedicated section | **PASS** | OPEN UNKNOWNS section; CONFIDENCE: "Do not list unknowns here — unknowns belong in OPEN UNKNOWNS, not in the confidence basis." |
| C-15 | aspirational | Hypothesis-revision lifecycle | **PASS** | Hypothesis inside PRE-FLIGHT GATE; synthesis: "State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE" |
| C-16 | aspirational | AMEND cascades to synthesis | **PASS** | No AMEND — default pass |
| C-17 | aspirational | Sections name failure modes | **PASS** | SYNTHESIS anti-pattern blockquote: "Restating sections in sequence...is juxtaposition — it fails this section" |
| C-18 | aspirational | Pre-analysis gate | **PASS** | PRE-FLIGHT GATE with 3 fields; STOP instruction before INERTIA CHECK |
| C-19 | aspirational | Prohibition guards (min 1) | **PASS** | SURFACE AREA, CONFIDENCE carry prohibitions |
| C-20 | aspirational | Complete closure mesh | **PASS** | INERTIA CHECK: "scope was resolved in PRE-FLIGHT GATE, not in analysis steps"; SURFACE AREA and COMPLEXITY: scope guarded with navigational form; COMPLEXITY: unknowns guarded; CONFIDENCE: unknowns guarded; SYNTHESIS: both guarded; OPEN UNKNOWNS: "Do not list unknowns in CONFIDENCE above or in SYNTHESIS below" |
| C-21 | aspirational | Gate elicits hypothesis | **PASS** | Preliminary hypothesis as field 3 inside PRE-FLIGHT GATE; synthesis references gate by name |
| C-22 | aspirational | Synthesis names gate at both ends | **PASS** | Anchor: "look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis..."; verdict close templates: "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed/revised/partially revised..." |
| C-23 | aspirational | Guards name canonical home | **PASS** | INERTIA CHECK, SURFACE AREA, COMPLEXITY: "scope was resolved in PRE-FLIGHT GATE, not in analysis steps"; CONFIDENCE, COMPLEXITY: "unknowns belong in OPEN UNKNOWNS, not in analysis sections" |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 15/15

```
composite = (5/5 × 60) + (3/3 × 30) + (15/15 × 10) = 60 + 30 + 10 = 100
```

**Band**: Gold | **Score: 100**

---

## V-04 — Full Integration + 23-Criterion Self-Check

**Axes**: All R6 mechanisms + failure mode blockquotes in STEP 6/7 + AMEND cascade + self-check updated to 23 criteria with C-22/C-23 items.

| ID | Weight | Criterion | Verdict | Evidence |
|----|--------|-----------|---------|----------|
| C-01 | essential | Complexity tier vocabulary | **PASS** | `LOW / MEDIUM / HIGH / XL` |
| C-02 | essential | Sprint range | **PASS** | `N–M sprints` |
| C-03 | essential | Surface area total row | **PASS** | Total row required |
| C-04 | essential | Inertia check | **PASS** | STEP 1 INERTIA CHECK with wrong/correct examples |
| C-05 | essential | Confidence with basis | **PASS** | Confidence + Basis |
| C-06 | recommended | Specializations named | **PASS** | Disciplines + FTE fractions + ownership |
| C-07 | recommended | Complexity driver | **PASS** | Primary driver with sensitivity template |
| C-08 | recommended | AMEND modifies output | **PASS** | AMEND INSTRUCTION in STEP 7 explicitly calls cascade; no active AMEND = default pass |
| C-09 | aspirational | Scope exclusions stated | **PASS** | PRE-FLIGHT GATE out-of-scope boundary field |
| C-10 | aspirational | Break-even signal | **PASS** | PRE-FLIGHT GATE break-even; self-check C-10 item confirms |
| C-11 | aspirational | Specialization ownership | **PASS** | STEP 4 failing/passing examples explicitly require ownership area |
| C-12 | aspirational | Named unknowns | **PASS** | STEP 6 typed fields with generic-placeholder failure mode |
| C-13 | aspirational | Cross-signal synthesis | **PASS** | STEP 7 requires ≥2 dimensions; self-check C-13 item |
| C-14 | aspirational | Unknowns dedicated section | **PASS** | STEP 6 canonical; STEP 5 explicitly closed; self-check C-14 item |
| C-15 | aspirational | Hypothesis-revision lifecycle | **PASS** | Hypothesis inside PRE-FLIGHT GATE; STEP 7 confirms/revises it; self-check C-15 item |
| C-16 | aspirational | AMEND cascades to synthesis | **PASS** | AMEND INSTRUCTION in STEP 7; self-check C-16 item; no active AMEND |
| C-17 | aspirational | Sections name failure modes | **PASS** | STEP 6 failure mode: "Dependencies may exist is a placeholder"; STEP 7 failure mode: juxtaposition anti-pattern |
| C-18 | aspirational | Pre-analysis gate | **PASS** | PRE-FLIGHT GATE before all STEPs; 3 fields; STOP instruction |
| C-19 | aspirational | Prohibition guards (min 1) | **PASS** | Multiple sections carry prohibitions |
| C-20 | aspirational | Complete closure mesh | **PASS** | STEP 1: scope guarded; STEP 2: scope guarded; STEP 3: scope + unknowns both guarded; STEP 5: unknowns guarded; STEP 7: both guarded; self-check C-20 item enumerates every required section |
| C-21 | aspirational | Gate elicits hypothesis | **PASS** | Hypothesis field 3 inside PRE-FLIGHT GATE; STEP 7 anchor names gate; self-check C-21 item |
| C-22 | aspirational | Synthesis names gate at both ends | **PASS** | STEP 7 anchor: "look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there"; verdict close templates require "PRE-FLIGHT GATE"; self-check C-22 item: "'My earlier estimate was confirmed' fails C-22 — it names no structural site" |
| C-23 | aspirational | Guards name canonical home | **PASS** | All guards use navigational form; self-check C-23 item distinguishes redirect from dead-end |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 15/15

```
composite = (5/5 × 60) + (3/3 × 30) + (15/15 × 10) = 60 + 30 + 10 = 100
```

**Band**: Gold | **Score: 100**

---

## V-05 — Dual Enforcement + Structural Definitions

**Axes**: All V-04 mechanisms + C-22 and C-23 self-check items extended with exact disqualifying form strings. Highest-reliability form of the v6 rubric.

| ID | Weight | Criterion | Verdict | Evidence |
|----|--------|-----------|---------|----------|
| C-01–C-08 | essential / recommended | All fields | **PASS** | Same as V-04 — identical structure |
| C-09 | aspirational | Scope exclusions | **PASS** | PRE-FLIGHT GATE; self-check C-09 |
| C-10 | aspirational | Break-even | **PASS** | PRE-FLIGHT GATE; self-check C-10 |
| C-11 | aspirational | Specialization ownership | **PASS** | STEP 4 examples |
| C-12 | aspirational | Named unknowns | **PASS** | STEP 6 typed fields + failure mode |
| C-13 | aspirational | Cross-signal synthesis | **PASS** | STEP 7 ≥2 dimension requirement |
| C-14 | aspirational | Unknowns dedicated section | **PASS** | STEP 6 canonical; STEP 5 closed; self-check C-14 |
| C-15 | aspirational | Hypothesis-revision | **PASS** | Hypothesis in gate; STEP 7 confirms/revises; self-check C-15 with disqualifying condition |
| C-16 | aspirational | AMEND cascade | **PASS** | AMEND INSTRUCTION present; default pass |
| C-17 | aspirational | Failure modes named | **PASS** | STEP 6 + STEP 7 anti-pattern blockquotes |
| C-18 | aspirational | Pre-analysis gate | **PASS** | PRE-FLIGHT GATE before all STEPs; STOP |
| C-19 | aspirational | Prohibition guards min 1 | **PASS** | Multiple sections |
| C-20 | aspirational | Complete closure mesh | **PASS** | Self-check C-20 enumerates every required section: STEP 1, 2, 3, 5, 7 for scope; STEP 3, 5, 7 for unknowns |
| C-21 | aspirational | Gate elicits hypothesis | **PASS** | Self-check C-21: "Passing C-18 and C-15 independently still fails C-21 if hypothesis is outside the gate block" |
| C-22 | aspirational | Synthesis names gate at both ends | **PASS** | Self-check C-22: exact disqualifying string "'My earlier estimate was confirmed' fails C-22 even if C-21 passes"; verdict close template in STEP 7 requires label in written output; STEP 7 body line: "Writing 'my earlier estimate was confirmed' fails C-22 because it does not identify the structural site" |
| C-23 | aspirational | Guards name canonical home | **PASS** | Self-check C-23: "Failing: 'do not include scope exclusions here' — this is a dead end that excludes without redirecting"; all guards use navigational form |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 15/15

```
composite = (5/5 × 60) + (3/3 × 30) + (15/15 × 10) = 60 + 30 + 10 = 100
```

**Band**: Gold | **Score: 100**

---

## Rankings

| Rank | Variation | Essential | Recommended | Aspirational | Score | Criteria Failed |
|------|-----------|-----------|-------------|--------------|-------|-----------------|
| 1 | **V-03** | 5/5 | 3/3 | 15/15 | **100** | — |
| 1 | **V-04** | 5/5 | 3/3 | 15/15 | **100** | — |
| 1 | **V-05** | 5/5 | 3/3 | 15/15 | **100** | — |
| 4 | V-01 | 5/5 | 3/3 | 13/15 | **98.67** | C-20, C-23 |
| 4 | V-02 | 5/5 | 3/3 | 13/15 | **98.67** | C-21, C-22 |

All 5 variations achieve Gold band. All essential criteria pass in all variations. R6 confirms the expected score distribution from the variate file exactly.

---

## Excellence Signals from V-03/V-04/V-05

**E-01 — Gate-as-atomic-commitment-block (C-21 → C-22 chain)**
The preliminary hypothesis is field 3 inside the PRE-FLIGHT GATE block — not a standalone MANDATORY OPENING that follows the gate. This makes the gate an atomic unit: scope boundary, break-even, and hypothesis are all committed before analysis, from the same structural site. Synthesis then traces back to that site by name at both the anchor instruction and the verdict close, producing a structurally verifiable chain. The critical mechanism: the verdict close template begins `"The preliminary hypothesis committed in PRE-FLIGHT GATE..."` so the gate label is part of what the model writes, not just an instruction it can ignore.

**E-02 — Navigational redirect guard (dead-end → C-23 pass)**
The structural distinction between `"Do not include scope exclusions here"` (dead-end) and `"Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps"` (navigational redirect). The redirect form closes the door AND names the room — a reader following the prohibition knows exactly where the excluded content belongs. This pattern applied to both canonical field types (scope exclusions → PRE-FLIGHT GATE; unknowns → OPEN UNKNOWNS) and in all adjacent sections simultaneously achieves C-20 and C-23 together.

**E-03 — Verdict close template as mechanical enforcement**
Prior rounds enforced the gate reference only through the synthesis *instruction* (`"look back at PRE-FLIGHT GATE"`). R6 moves the enforcement into the verdict close *template form*: the three permitted verdict strings each begin with `"The preliminary hypothesis committed in PRE-FLIGHT GATE..."`. The model cannot write a compliant verdict without writing the gate label — it is not a reminder but a structural requirement baked into the template.

**E-04 — V-05 self-check structural definitions as self-audit**
V-05's self-check items for C-22 and C-23 name the exact disqualifying string: C-22 item states `"'My earlier estimate was confirmed' fails C-22 even if C-21 passes"` and C-23 item contrasts `"Passing: 'scope was resolved in PRE-FLIGHT GATE, not in analysis steps'" vs "Failing: 'do not include scope exclusions here'"`. This pattern — naming the exact failing form, not just the passing form — makes compliance self-auditable before writing. This is the highest-reliability enforcement mechanism and the pattern that distinguishes V-05 from V-03/V-04 at execution time.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Verdict close template mechanically embeds gate label — three permitted verdict strings each begin 'The preliminary hypothesis committed in PRE-FLIGHT GATE...', making the gate label structurally required in what the model writes, not only in the instruction preamble", "Navigational redirect guard distinguishes dead-end from redirect — 'do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps' closes door AND names destination, achieving C-23; bare exclusion form closes door without pointing to room and fails C-23 regardless of C-20 pass"]}
```
