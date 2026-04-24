---
skill: quest-score
skill_target: program-plan
date: 2026-03-15
round: 12
rubric: program-plan-rubric-v28-2026-03-15.md
variations_scored: [V-01, V-02, V-03, V-04, V-05]
new_criteria: C-35, C-36
scoring_formula: "essential_pass/4*60 + recommended_pass/3*30 + aspirational_pass/29*10"
max_composite: 100
---

# program-plan Skill Score — Round 12 (2026-03-15)

Rubric: v28 (C-01–C-36, 4 essential / 3 recommended / 29 aspirational, max composite 100)
New criteria this round: C-35 (second-person register as C-12 intensifier), C-36 (domain-
metaphor total saturation at all four structural anchor points)

---

## Context

R12 variations in the file were constructed against the OLD 240-pt rubric (flat scoring,
C-01–C-36 as output-quality checks). Rubric v28 restructures scoring into tiers AND changes
the meaning of all criteria — they now evaluate SKILL PROMPT DESIGN quality, not output
quality. As a result, the R12 variations satisfy essential and recommended criteria fully
but fail many aspirational criteria that require structural scaffolding (tabular catalog,
layer-divider YAML comments, per-layer prose narration, BAD/GOOD gate table) that the old
rubric never required.

**Baseline pass set (all 5 variations):** C-01, C-02, C-03, C-04 (essential); C-05, C-06,
C-07 (recommended); C-08, C-09, C-10, C-11, C-12, C-13, C-17 (aspirational) = 7/29.

**Differentiator:** C-16 (contrast-grounded identity) — V-04/V-05 PASS via dual-failure-mode
opening anatomy; V-01/V-02/V-03 FAIL (not-executor stated before contrast). 8/29 vs 7/29.

---

## Per-Variation Scoring

### V-01 — C-36 Contrastive-Clause Leading

**Axis**: ARTIFACT 0 echo exception leads with explicit contrastive negation ("not an arbitrary
convention -- it is the structural encoding of echo's anchor role as terminal consumer").
ARTIFACT 2 YAML fragment column present. Consumer-pull rule carries both negation + equivalence
forms. Register: compact formal/reference.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 valid YAML structure | PASS | stages: array with name/skills/gate per stage; echo YAML valid |
| C-02 echo final stage contract | PASS | name: echo, auto: true, skills: [] at end |
| C-03 valid Signal skill names | PASS | catalog shows all 9 namespaces; template references catalog |
| C-04 non-trivial gates | PASS | gate template: `{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists` |
| C-05 namespace dependency order | PASS | evidence_arc breadth→depth→synthesis; PASS/FAIL stage name examples enforce ordering |
| C-06 descriptive stage names | PASS | PASS: `discovery`, `stress-test`; FAIL: `scout_and_draft_stage` examples given |
| C-07 plan-not-executor framing | PASS | "the program is a plan, not an executor" in opening paragraph |
| C-08 deliberate evidence arc | PASS | three zones (breadth/depth/synthesis) with explicit namespace assignments |
| C-09 quantified gate | PASS | `>= N` present in gate template; Step 5a PASS example shows `>= 3` |
| C-10 inertia contrast | PASS | Step 5a PASS/FAIL gate examples; "failure mode to prevent: catalog-first" in preamble |
| C-11 self-verification checklist | PASS | Step 10 pre-printed checklist with 36 binary items |
| C-12 not-executor as opening identity | PASS | "the program is a plan, not an executor" in opening paragraph preamble |
| C-13 template-locked verification | PASS | Step 10 checklist pre-printed in template; model fills checkboxes |
| C-14 arc structure in template | FAIL | YAML template has evidence_arc field but NO layer-divider comments separating stage groups |
| C-15 not-executor dual-site | FAIL | opening prose YES; YAML template has NO `# REQUIRED PRESERVE: plan not executor` comment |
| C-16 contrast-grounded identity | FAIL | not-executor stated in opening paragraph BEFORE any failure-mode contrast; identity not derived from contrast |
| C-17 explicit dependency narration | PASS | ARTIFACT 0: "this stage produces the artifacts that close the next stage's input gap" — explicit cross-stage dependency prose |
| C-18 YAML-embedded dependency map | FAIL | requires C-14 to pass; layer dividers absent from YAML template |
| C-19 pre-template reference tables | FAIL | only 1 pre-template table (three-knowable-classes); catalog is code block not table; gate examples are bullets |
| C-20 per-layer arc narration | FAIL | zones described in table/bullets; no dedicated paragraph per arc layer (Layer 1, Layer 2, Layer 3) |
| C-21 echo stage narrated in prose | FAIL | echo exception in ARTIFACT 0 code block; does NOT cover: why echo carries no skills; auto:true semantics; arc-closure function |
| C-22 BAD/GOOD gate contrast as table | FAIL | gate contrasts are PASS/FAIL bullet points in Step 5a; no table with BAD/GOOD columns |
| C-23 tabular skill catalog | FAIL | catalog is a code block (namespace:skills text), not a table |
| C-24 layer paragraph headers | FAIL | requires C-20 to pass; no layer paragraphs exist |
| C-25 echo paragraph enumerated | FAIL | requires C-21 to pass; echo not explained in enumerated paragraph |
| C-26 layer header cross-layer ref | FAIL | requires C-24 to pass |
| C-27 terminal layer context dep | FAIL | requires C-24 to pass |
| C-28 BAD example causal narrative | FAIL | failure mode described abstractly ("catalog-first construction"); no rendered human-decision scene |
| C-29 identity claim process scope | FAIL | not-executor claim present; does NOT name "this conversation and the plan it produces" as replacement target |
| C-30 composite gate placeholder | FAIL | gate template combines count+presence but does NOT label them as explicitly separated named sub-conditions |
| C-31 gate table diagnostic column | FAIL | requires C-22 to pass; no gate table |
| C-32 middle-layer bidirectional | FAIL | requires C-24 to pass |
| C-33 skill catalog domain-functional | FAIL | requires C-23 to pass; no table catalog |
| C-34 verification domain-metaphor | FAIL | checklist items use structural/technical vocabulary; no domain-metaphor framing (no metaphor axis in V-01) |
| C-35 second-person C-12 register | FAIL | not-executor claim is third-person ("the program is a plan"); no "You are planning, not executing" form |
| C-36 domain-metaphor total saturation | FAIL | requires C-15, C-24, C-33, C-34 to pass; all four fail |

**Essential**: 4/4 PASS → 4 × 15 = **60 pts**
**Recommended**: 3/3 PASS → 3 × 10 = **30 pts**
**Aspirational**: 7/29 PASS → 7/29 × 10 = **2.41 pts**

**Composite**: 60 + 30 + 2.41 = **92.41**
**Golden**: YES (all essential PASS, composite 92.41 >= 80)

---

### V-02 — C-36 Named ROW-0 RULE

**Axis**: ARTIFACT 0 echo exception includes a labeled "ROW-0 RULE:" block that names and
forecloses the arbitrary-convention misreading as a canonical design contract. Named rule
makes C-36 auditable by label. ARTIFACT 2 YAML fragment column present. Both C-34 forms.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 valid YAML structure | PASS | identical scaffold to V-01 |
| C-02 echo final stage contract | PASS | echo last, auto:true, skills:[] |
| C-03 valid Signal skill names | PASS | catalog provided, 9 namespaces |
| C-04 non-trivial gates | PASS | compound gate template present |
| C-05 namespace dependency order | PASS | evidence_arc breadth→depth→synthesis |
| C-06 descriptive stage names | PASS | PASS/FAIL phase name examples |
| C-07 plan-not-executor framing | PASS | "the program is a plan, not an executor" opening |
| C-08 deliberate evidence arc | PASS | three zones explicitly described |
| C-09 quantified gate | PASS | `>= N` in template |
| C-10 inertia contrast | PASS | "failure mode: catalog-first" in preamble; PASS/FAIL gate examples |
| C-11 self-verification checklist | PASS | Step 10 pre-printed checklist |
| C-12 not-executor as opening identity | PASS | not-executor in opening paragraph |
| C-13 template-locked verification | PASS | Step 10 pre-printed |
| C-14 arc structure in template | FAIL | no layer-divider YAML comments in template |
| C-15 not-executor dual-site | FAIL | no REQUIRED PRESERVE YAML comment |
| C-16 contrast-grounded identity | FAIL | failure mode description comes AFTER identity claim in opening; not contrast-grounded |
| C-17 explicit dependency narration | PASS | consumer-pull rule in ARTIFACT 0 narrates cross-stage dependency |
| C-18 YAML-embedded dependency map | FAIL | requires C-14 |
| C-19 pre-template reference tables | FAIL | 1 pre-template table; catalog is code block |
| C-20 per-layer arc narration | FAIL | no layer-specific paragraphs |
| C-21 echo stage narrated in prose | FAIL | ROW-0 RULE block covers row-0 position but not: skills-free rationale, auto:true semantics, arc-closure function |
| C-22 BAD/GOOD gate contrast as table | FAIL | gate contrasts are bullet points, not a table |
| C-23 tabular skill catalog | FAIL | code block, not table |
| C-24 layer paragraph headers | FAIL | requires C-20 |
| C-25 echo paragraph enumerated | FAIL | requires C-21 |
| C-26 layer header cross-layer ref | FAIL | requires C-24 |
| C-27 terminal layer context dep | FAIL | requires C-24 |
| C-28 BAD example causal narrative | FAIL | failure mode described; no rendered human-decision scene |
| C-29 identity claim process scope | FAIL | not-executor not scoped to process replacement |
| C-30 composite gate placeholder | FAIL | sub-conditions present but not explicitly labeled as separable named parts |
| C-31 gate table diagnostic column | FAIL | requires C-22 |
| C-32 middle-layer bidirectional | FAIL | requires C-24 |
| C-33 skill catalog domain-functional | FAIL | requires C-23 |
| C-34 verification domain-metaphor | FAIL | no domain-metaphor axis; checklist items use structural vocabulary |
| C-35 second-person C-12 register | FAIL | not-executor claim is third-person |
| C-36 domain-metaphor total saturation | FAIL | requires C-15, C-24, C-33, C-34 |

**Essential**: 4/4 PASS → **60 pts**
**Recommended**: 3/3 PASS → **30 pts**
**Aspirational**: 7/29 PASS → **2.41 pts**

**Composite**: **92.41** | **Golden**: YES

---

### V-03 — C-35 Column-as-Discovery (Tutorial Register)

**Axis**: Tutorial/second-person voice throughout. ARTIFACT 2 framed as discovery moment:
"When your matrix rows are complete, look at the YAML fragment column: you'll notice it already
contains every per-stage annotation your YAML needs." C-36 as "why can't I move echo?" framing:
"not an arbitrary convention you are free to vary." C-34 both forms in ARTIFACT 0.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-04 | PASS | same structure as V-01/V-02 |
| C-05 through C-07 | PASS | same |
| C-08 deliberate evidence arc | PASS | three zones, explicit zone descriptions in second-person |
| C-09 quantified gate | PASS | `>= N` in template |
| C-10 inertia contrast | PASS | "failure mode to prevent: catalog-first" in opening; PASS/FAIL gate examples |
| C-11 self-verification checklist | PASS | Step 10 pre-printed |
| C-12 not-executor as opening identity | PASS | "the program is a plan, not an executor" in opening paragraph |
| C-13 template-locked verification | PASS | Step 10 pre-printed |
| C-14 arc structure in template | FAIL | no layer-divider YAML comments; evidence_arc field present but no structural dividers between stage groups |
| C-15 not-executor dual-site | FAIL | no REQUIRED PRESERVE YAML comment in template |
| C-16 contrast-grounded identity | FAIL | "the program is a plan, not an executor" stated in opening paragraph (first 3 sentences) before failure mode description; identity is not derived from contrast |
| C-17 explicit dependency narration | PASS | consumer-pull rule in ARTIFACT 0; tutorial voice explains "the annotations were determined by the backward derivation, not authored from skill knowledge" |
| C-18 YAML-embedded dependency map | FAIL | requires C-14 |
| C-19 pre-template reference tables | FAIL | 1 pre-template table; catalog is code block |
| C-20 per-layer arc narration | FAIL | lifecycle zones described as bullets; no dedicated per-layer paragraphs |
| C-21 echo stage narrated in prose | FAIL | "why can't I move echo?" tutorial framing covers row-0 position but not skills-free contract, auto:true semantics |
| C-22 BAD/GOOD gate contrast as table | FAIL | PASS/FAIL bullet points, not a table |
| C-23 tabular skill catalog | FAIL | code block |
| C-24 layer paragraph headers | FAIL | requires C-20 |
| C-25 echo paragraph enumerated | FAIL | requires C-21 |
| C-26 through C-32 | FAIL | cascade from C-24 or C-22 or C-23 |
| C-33 skill catalog domain-functional | FAIL | requires C-23 |
| C-34 verification domain-metaphor | FAIL | no domain-metaphor axis; "discovery" is a framing tone not a metaphor vocabulary |
| C-35 second-person C-12 register | FAIL | tutorial voice is second-person throughout BUT the not-executor claim "the program is a plan, not an executor" is third-person; C-35 requires the not-executor CLAIM in second-person ("You are planning, not executing") |
| C-36 domain-metaphor total saturation | FAIL | requires C-15, C-24, C-33, C-34 |

**Note on C-35**: V-03 uses second-person register throughout ("you'll notice", "you need to
understand", "what you must keep knowable") but the not-executor identity claim retains
third-person phrasing. C-35 requires the not-executor claim itself to be "You are X, not Y."

**Essential**: 4/4 PASS → **60 pts**
**Recommended**: 3/3 PASS → **30 pts**
**Aspirational**: 7/29 PASS → **2.41 pts**

**Composite**: **92.41** | **Golden**: YES

---

### V-04 — Failure Anatomy Names the Misreading (Combined)

**Axes**: Inertia-First + Tutorial Register. Opening names TWO failure modes explicitly:
Failure 1 (catalog-first) and Failure 2 (arbitrary-convention misreading). Every rule labeled
as counter-move against a specific failure. ARTIFACT 0 closes with explicit contrastive clause.
ARTIFACT 2 YAML fragment column. Both C-34 forms. Not-executor identity emerges from failure
anatomy as counter-move conclusion.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-04 | PASS | same scaffold |
| C-05 through C-07 | PASS | same |
| C-08 deliberate evidence arc | PASS | three zones |
| C-09 quantified gate | PASS | `>= N` |
| C-10 inertia contrast | PASS | Failure 1 description as opening bad-practice anatomy; PASS/FAIL gate examples with Failure 1 labels |
| C-11 self-verification checklist | PASS | Step 10 pre-printed (includes counter-move labels on C-31/C-36 items) |
| C-12 not-executor as opening identity | PASS | "Every skill runs standalone; the program is a plan, not an executor." concludes the opening failure-anatomy block |
| C-13 template-locked verification | PASS | Step 10 pre-printed |
| C-14 arc structure in template | FAIL | no layer-divider YAML comments |
| C-15 not-executor dual-site | FAIL | no REQUIRED PRESERVE YAML comment |
| C-16 contrast-grounded identity | PASS | opening structure: Failure 1 anatomy → Failure 2 anatomy → "every rule is a counter-move" → not-executor; identity emerges as conclusion of contrast block |
| C-17 explicit dependency narration | PASS | consumer-pull rule in ARTIFACT 0; "ARTIFACT 2 is the sole authoritative source... copy it directly" narrates derivation dependency |
| C-18 YAML-embedded dependency map | FAIL | requires C-14 |
| C-19 pre-template reference tables | FAIL | 1 pre-template table |
| C-20 per-layer arc narration | FAIL | zones described as bullets ("Breadth -- do you understand... Depth -- does your design... Synthesis -- are users adopting..."); no dedicated per-layer paragraph-level treatment |
| C-21 echo stage narrated in prose | FAIL | echo exception in ARTIFACT 0 explains row-0 anchor role; does not cover skills-free contract or auto:true semantics in prose |
| C-22 BAD/GOOD gate contrast as table | FAIL | PASS/FAIL bullet points; "Failure 1 at gate level" labels on some FAIL examples but not table structure |
| C-23 tabular skill catalog | FAIL | code block |
| C-24 layer paragraph headers | FAIL | requires C-20 |
| C-25 echo paragraph enumerated | FAIL | requires C-21 |
| C-26 through C-32 | FAIL | cascade |
| C-33 skill catalog domain-functional | FAIL | requires C-23 |
| C-34 verification domain-metaphor | FAIL | "failure anatomy" framing is methodological, not a domain metaphor; "counter-move against Failure 2" in C-31 item is close but uses structural not metaphorical vocabulary |
| C-35 second-person C-12 register | FAIL | "the program is a plan, not an executor" is third-person; second-person voice present elsewhere ("you will maintain", "Before you write") but not-executor claim itself is not addressed to "you" |
| C-36 domain-metaphor total saturation | FAIL | requires C-15, C-24, C-33, C-34 |

**Note on C-16**: V-04's dual-failure opening is the definitive C-16 implementation in R12.
The sequence "Failure 1 description → Failure 2 description → 'every rule is a counter-move'
→ not-executor" makes the skill's identity structurally dependent on the failure contrast.

**Essential**: 4/4 PASS → **60 pts**
**Recommended**: 3/3 PASS → **30 pts**
**Aspirational**: 8/29 PASS (C-08 through C-13, C-16, C-17) → 8/29 × 10 = **2.76 pts**

**Composite**: **92.76** | **Golden**: YES

---

### V-05 — Full Reference Implementation (R12)

**Axes**: All — Inertia-First + Tutorial + Matrix-as-Rendering-Scaffold + Failure Anatomy.
C-34 gets a bridge sentence ("The negation closes the producer-push misreading; the equivalence
makes the rule self-verifying from both ends simultaneously."). C-35: YAML fragment column
plus discovery framing plus "structural proof visible before any declaration." C-36: names and
quotes the misreading it forecloses ("the misreading that echo could be placed at row N by
convention is the failure mode this position forecloses").

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-04 | PASS | same scaffold |
| C-05 through C-07 | PASS | same |
| C-08 deliberate evidence arc | PASS | three zones; breadth/depth/synthesis with explicit namespace scope |
| C-09 quantified gate | PASS | `>= N` in template |
| C-10 inertia contrast | PASS | dual-failure opening; PASS/FAIL gate examples with "Failure 1 at gate" labels |
| C-11 self-verification checklist | PASS | Step 10 pre-printed; C-34 item includes bridge sentence |
| C-12 not-executor as opening identity | PASS | "the program is a plan, not an executor" concludes failure-anatomy opening |
| C-13 template-locked verification | PASS | Step 10 pre-printed |
| C-14 arc structure in template | FAIL | YAML template has evidence_arc field but no `# ---- Layer N: Zone ----` divider comments between stage groups |
| C-15 not-executor dual-site | FAIL | opening prose YES; YAML template does not contain a `# REQUIRED PRESERVE: plan not executor` type comment |
| C-16 contrast-grounded identity | PASS | same dual-failure opening as V-04; identity emerges as counter-move conclusion |
| C-17 explicit dependency narration | PASS | ARTIFACT 0 consumer-pull rule + "YAML fragment column is the structural proof that YAML is a rendered projection of the matrix" — explicit derivation dependency |
| C-18 YAML-embedded dependency map | FAIL | requires C-14 |
| C-19 pre-template reference tables | FAIL | 1 pre-template table (three-knowable-classes); catalog is code block |
| C-20 per-layer arc narration | FAIL | zones in bullet-list format ("Breadth -- do you understand... Depth -- does your design... Synthesis -- are users adopting..."); each gets a single bullet, not a paragraph-level narration |
| C-21 echo stage narrated in prose | FAIL | ARTIFACT 0 echo exception covers row-0 structural encoding; "Omission of # Band: from echo is normative: it is the derivation anchor, not a band member" — does NOT address skills-free rationale or auto:true semantics |
| C-22 BAD/GOOD gate contrast as table | FAIL | PASS/FAIL bullet points with Failure labels; not a table with BAD/GOOD column structure |
| C-23 tabular skill catalog | FAIL | code block |
| C-24 layer paragraph headers | FAIL | requires C-20 |
| C-25 echo paragraph enumerated | FAIL | requires C-21 |
| C-26 through C-32 | FAIL | cascade |
| C-33 skill catalog domain-functional | FAIL | requires C-23 |
| C-34 verification domain-metaphor | FAIL | bridge sentence in ARTIFACT 0 (not checklist) and C-34 checklist item describes structural requirement ("negation... equivalence... bridge sentence present") — structural vocabulary not domain-metaphor vocabulary |
| C-35 second-person C-12 register | FAIL | not-executor claim is third-person: "the program is a plan, not an executor"; second-person voice present throughout instruction prose but not in the identity claim itself |
| C-36 domain-metaphor total saturation | FAIL | requires C-15, C-24, C-33, C-34; all four site prerequisites fail |

**Note on C-35**: V-05's ARTIFACT 2 narrative ("You begin where the chain begins: what does
echo need to receive?") is second-person but addresses the derivation process, not the
not-executor identity. The identity claim itself remains third-person.

**Essential**: 4/4 PASS → **60 pts**
**Recommended**: 3/3 PASS → **30 pts**
**Aspirational**: 8/29 PASS (C-08 through C-13, C-16, C-17) → 8/29 × 10 = **2.76 pts**

**Composite**: **92.76** | **Golden**: YES

---

## Ranking

| Rank | Variation | Composite | Essential | Recommended | Aspirational |
|------|-----------|-----------|-----------|-------------|--------------|
| 1 (tie) | V-04 | 92.76 | 4/4 | 3/3 | 8/29 |
| 1 (tie) | V-05 | 92.76 | 4/4 | 3/3 | 8/29 |
| 3 (tie) | V-01 | 92.41 | 4/4 | 3/3 | 7/29 |
| 3 (tie) | V-02 | 92.41 | 4/4 | 3/3 | 7/29 |
| 3 (tie) | V-03 | 92.41 | 4/4 | 3/3 | 7/29 |

Tiebreak within Rank 1: V-05 as full reference implementation.

---

## Systematic Gap Analysis

The following aspirational criteria fail across ALL five variations. These are structural
features the R12 variations never contained (they were designed for the old 240-pt rubric):

| Gap cluster | Criteria | Root missing feature |
|-------------|----------|---------------------|
| Layer scaffolding | C-14, C-18, C-24, C-25, C-26, C-27, C-32 | No `# ---- Layer N: Zone ----` divider comments inside YAML template |
| Not-executor anchor | C-15 | No `# REQUIRED PRESERVE: plan not executor` comment in YAML template |
| Tabular structures | C-19, C-22, C-23, C-31, C-33 | Skill catalog is code block; gate contrast is bullet points; need 2+ pre-template tables |
| Per-layer narration | C-20 | Lifecycle zones described in bullets; need dedicated prose paragraph per arc layer |
| Echo prose | C-21, C-25 | Echo exception in code block; no paragraph covering skills-free contract + auto:true semantics + arc closure |
| Process narrative | C-28, C-29 | Bad-practice framed as abstract description; no rendered human-decision scene |
| Second-person identity | C-35 | Not-executor claim is third-person; needs "You are planning, not executing" form |
| Domain metaphor | C-34, C-36 | No metaphor axis; checklist uses structural vocabulary |
| Composite gate labels | C-30 | Gate template sub-conditions present but not labeled as named separable parts |

**Net: 22 aspirational criteria blocked by 9 structural absences.** C-14 alone cascades to 7
criteria failing. Resolving C-14 (layer dividers in template), C-15 (REQUIRED PRESERVE comment),
C-20 (per-layer paragraphs), C-21 (echo prose), C-22 (gate table), C-23 (tabular catalog),
C-28 (causal narrative), C-35 (second-person identity), and C-34 (domain metaphor) would bring
all 5 variations to 29/29 aspirational = composite 100.

---

## Excellence Signals (V-04/V-05 over V-01/V-02/V-03)

**Signal 1 — Dual-failure-mode opening as identity mechanism (C-16).**
V-04/V-05 name TWO distinct failure modes at the opening (Failure 1: catalog-first; Failure 2:
arbitrary-convention misreading), then declare "every rule in this protocol is a counter-move
against one of these two failure modes." This makes the not-executor identity claim load-bearing
rather than incidental: it is the structural conclusion of a contrast that defines the skill's
purpose. V-01/V-02/V-03 state the not-executor claim before any contrast is established,
leaving C-16 unsatisfied.

**Signal 2 — Counter-move labeling makes failure closure auditable.**
V-04/V-05 label each protocol rule as a specific counter-move ("counter-move against Failure 2"
in ARTIFACT 0 echo exception; "counter-move against Failure 1" in Step 2 catalog-closed rule).
This creates a traceable two-way mapping between failure modes and design rules, strengthening
the protocol's internal logic beyond what a single-failure framing achieves. This pattern goes
beyond what R11 achieved with single-failure anatomy openings.

**Signal 3 — Bridge sentence makes C-34 dual-form explicit (V-05 only).**
V-05 ARTIFACT 0 consumer-pull rule adds: "The negation closes the producer-push misreading;
the equivalence makes the rule self-verifying from both ends simultaneously." This bridge
sentence names WHY both forms are present, converting the dual-form from a design pattern into
a stated rationale. Checklist C-34 item in V-05 includes both the negation form, equivalence
form, AND the bridge sentence as three verifiable components — the strongest C-34 formulation
in R12.

---

## Score Card Summary

```
             C-01 C-02 C-03 C-04 | C-05 C-06 C-07 | C-08..C-36
V-01          P    P    P    P   |  P    P    P   | 7/29 (C-08..C-13, C-17)
V-02          P    P    P    P   |  P    P    P   | 7/29 (same)
V-03          P    P    P    P   |  P    P    P   | 7/29 (same)
V-04          P    P    P    P   |  P    P    P   | 8/29 (same + C-16)
V-05          P    P    P    P   |  P    P    P   | 8/29 (same + C-16)

essential_pass = 4/4 → 4 × 15 = 60 pts (all variations)
recommended_pass = 3/3 → 3 × 10 = 30 pts (all variations)
aspirational_pass (V-01/02/03) = 7/29 → 7/29 × 10 = 2.41 pts
aspirational_pass (V-04/05)    = 8/29 → 8/29 × 10 = 2.76 pts

V-01 composite = 92.41 | golden = YES
V-02 composite = 92.41 | golden = YES
V-03 composite = 92.41 | golden = YES
V-04 composite = 92.76 | golden = YES
V-05 composite = 92.76 | golden = YES

top_score = 92.76 (V-04 and V-05 tied; V-05 as full reference tiebreak)
all_essential_pass = true
```
