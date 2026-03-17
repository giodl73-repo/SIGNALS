Written to `simulations/quest/rubrics/quest-variate-rubric-v8-2026-03-14.md`.

---

### Changes from v7 -> v8

**One new criterion extracted: C-27 — All stop condition boundaries uniformly imperative** (R7/V-02)

V-02 was designed as the C-27 ablation candidate flagged at the end of v7. It confirmed the prediction cleanly: making Phase 2 STOP advisory while leaving Phase 1 and checkpoint imperative isolates exactly the Phase 2-to-Phase 3 transition as an independently testable failure site.

**C-10 is revised** (lowered bar: "at least one boundary imperative") and **C-27 is extracted** (full bar: "all three boundaries uniformly imperative"). The split is isomorphic to v7's PARTIAL scoring on V-02 — same information, cleaner pass conditions. C-10, C-23, and C-27 now form an explicit three-boundary coverage ladder.

**Scoring: denominator 19 -> 20.**

**Score changes vs. v7:**
- V-01: 100.0 (unchanged)
- V-02: 99.74 -> 99.5 (C-10 PARTIAL replaced by C-10 PASS + C-27 FAIL)
- V-03/V-04/V-05: 99.47 -> 99.5 (denominator math: 18/19×10=9.47 vs 19/20×10=9.5)

All four ablation variations converge to 99.5 — a flat tier reflecting R7's equal-depth single-criterion design.

**R7->R8 candidate:** Phase 3 *Prevents:* label content density. V-01's Phase 3 label names one failure mode (critique interleaving) while Phases 1 and 2 each name three. If removing Phase 3's label produces measurable emit-phase degradation, that evidence supports C-28 splitting C-16 into presence (current) vs. content density (new).
ing anyway may reduce output quality") is structurally distinct from V-01's Phase 2 imperative STOP ("Do not begin Phase 3... Do not proceed if any variation has a noted but unresolved failure"). The advisory register at Phase 2 allows the "proceed and note" bypass pattern at the Phase 2-to-Phase 3 boundary specifically -- the model can acknowledge the failure condition while continuing to emit. C-27 requires all three stop condition boundaries -- Phase 1 gate, Phase 2 gate, AND per-variation checkpoint failure branch -- to use uniformly hard-stop imperative register. A skill can satisfy C-10 (at least one imperative boundary) and C-23 (per-variation checkpoint failure branch specifically imperative) while failing C-27 if Phase 2 STOP uses advisory language. The C-10, C-23, C-27 trio now forms a coverage ladder: C-10 is the entry bar (at least one boundary imperative) -> C-23 tests the per-variation checkpoint failure branch specifically -> C-27 requires all three boundaries uniformly imperative.

**C-10, C-23, and C-27 form a three-boundary coverage chain**: C-10 (entry: at least one imperative) -> C-23 (per-variation checkpoint failure branch specifically imperative) -> C-27 (all three boundaries uniformly imperative).

**Scoring:** `aspirational_pass / 20 * 10` (denominator bumps from 19 to 20)

**R7->R8 candidate:** V-01's C-16 evidence shows Phase 1 *Prevents:* label enumerates three named failure modes (V-ID citations, axis breadth, falsifiable primary-effect), Phase 2 names three (truncation, diff-leak, coherence failures), and Phase 3 names one (critique interleaving). C-16 currently requires only presence at all three phases. The asymmetry in failure-mode density between Phase 3 (one) and Phases 1-2 (three each) is the first within-criterion density difference recorded across all R7 variations. If an intentional R8 ablation removes the Phase 3 *Prevents:* label entirely (or reduces it to a generic note) while retaining Phase 1 and Phase 2 labels, and that change produces measurable emit-phase quality degradation (critique fragments interleaved with emitted bodies, or partial bodies in Phase 3 output), that evidence could support C-28 splitting C-16 into presence (current C-16) vs. content density (C-28: "Each phase *Prevents:* label enumerates at least two distinct named failure modes"). The Phase 3 boundary is structurally notable: unlike Phase 1 and Phase 2 (each with explicit STOP conditions counted in C-10/C-27), Phase 3 has a *Prevents:* label but no stop condition in V-01's evidence record.

- C-10 and C-27 are related but non-overlapping: C-10 requires at least one stop condition boundary to use imperative register; C-27 requires all three boundaries (Phase 1 gate, Phase 2 gate, per-variation checkpoint) to use uniformly imperative register. A skill with Phase 1 and checkpoint imperative but advisory Phase 2 STOP satisfies C-10 while failing C-27.
- C-10, C-23, and C-27 are layered: C-23 requires the per-variation checkpoint failure branch specifically to use hard-stop imperative register; C-10 requires at least one boundary (which could be Phase 1 or Phase 2) to be imperative; C-27 requires all three simultaneously. A skill can satisfy C-23 (checkpoint imperative) without C-10 if Phase 1 and Phase 2 gates are advisory -- though in practice satisfying C-23 will usually also satisfy C-10.

---

## Design Decisions

- **C-08 through C-27** are all aspirational -- their absence does not prevent a functional variation set, but their presence marks a higher-order design capability.
- **C-16/C-17/C-18** are distinct from C-10/C-11/C-12/C-13/C-14/C-15: a skill body can satisfy C-10 without C-16, C-05 without C-18, etc.
- **C-19** is distinct from C-18: C-18 requires that at least one variation's hypothesis model a countervailing secondary effect. C-19 requires that hypothesis to identify *which other specific variations* will exhibit that effect. Cross-variation falsifiability is a strictly stronger claim than within-variation secondary prediction.
- **C-20** is distinct from C-16: C-16 operates at phase level (inertia labels before each phase's instructions). C-20 operates at hypothesis-field level (a template with named columns that force multi-part structure). A skill with strong C-16 framing will improve hypothesis quality on average; only C-20 makes multi-part hypothesis structure mandatory through format.
- **C-21** is distinct from C-14: C-14 requires a per-variation quality gate to exist; C-21 requires that gate to include at least one row that tests a set-level predicate (a property of the planning table or variation set as a whole, not the current variation's body). A strong C-14 checkpoint that only verifies the current body does not satisfy C-21.
- **C-22** is distinct from C-07: C-07 requires different axes represented across variations; C-22 requires the same high-order aspirational criterion activated by structurally independent mechanisms in at least two variations. The distinction is axis diversity (C-07) vs mechanism diversity toward a shared criterion (C-22).
- **C-23** is distinct from C-12: C-12 requires a named rewrite trigger in the skill body; C-23 requires that the *per-variation checkpoint's failure branch* uses hard-stop imperative register. A skill can satisfy C-12 via a phase-gate trigger (e.g., in Phase 1 or Phase 2 stop conditions) without placing imperative language in the checkpoint step, thus satisfying C-12 without C-23.
- **C-24** is distinct from C-20: C-20 requires all planning-table columns to be present and non-empty; C-24 requires the primary-effect field specifically to contain an analytically sharp, bounded prediction rather than a directional or scope-level description. Template compliance (C-20) and analytical precision (C-24) are empirically dissociable: role priors that increase secondary-effect elaboration can reduce primary-effect precision through crowding, satisfying C-20 while failing C-24.
- **C-25** is distinct from C-15 and C-21: C-15 requires a named domain persona; C-21 requires set-level predicates in the per-variation checkpoint; C-25 requires the persona preamble to install checkpoint and coherence obligations as role-constitutive duties before any phase instruction appears. A skill satisfying C-15 and C-21 fails C-25 if professional obligations are introduced only within phase instructions rather than pre-established as part of the role identity.
- **C-26** is distinct from C-19 and C-21: C-19 requires sibling V-IDs to appear in the hypothesis (a content quality predicate); C-21 requires set-level predicates in the per-variation checkpoint (a post-generation gate); C-26 requires V-ID citation to be enforced as a Phase 1 gate condition that blocks Phase 2 entry (a pre-generation prerequisite). The three criteria form a temporal enforcement chain: C-26 gates at hypothesis lock, C-21 gates at body completion, C-19 evaluates content quality at review time.
- **C-27** is distinct from C-10 and C-23: C-10 requires at least one stop condition boundary to use imperative register; C-23 requires the per-variation checkpoint failure branch specifically to be imperative; C-27 requires all three boundaries (Phase 1 gate, Phase 2 gate, per-variation checkpoint) to use uniformly imperative register. A skill satisfying C-10 and C-23 fails C-27 if Phase 2 STOP uses advisory language. The three criteria form a boundary coverage ladder: C-10 (entry bar) -> C-23 (checkpoint boundary) -> C-27 (full stack uniform).
- **Failure modes section** names the most likely failure patterns by criterion for faster, more consistent scoring across runs.

---

## Criteria

### Essential (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Complete runnable bodies** | completeness | essential | Each variation is a complete, standalone skill body. No diffs, no "same as above", no references to other variations. The body can be dropped into a skill file and run without modification. |
| C-02 | **Inline axis and hypothesis labels** | labeling | essential | Each variation includes an inline `**Axis:**` field, `**Hypothesis:**` field, and variation ID (`## V-01`). All three fields are present and non-empty. |
| C-03 | **Single-axis isolation** | correctness | essential | Each variation changes exactly one axis relative to a baseline. Variations that co-vary two or more axes without being labeled as combination passes fail. |
| C-04 | **N variations produced** | coverage | essential | Output contains exactly N complete variations. Default N=5 when not specified. |

### Recommended (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Testable hypotheses** | depth | recommended | Each hypothesis is falsifiable -- predicts a specific, observable difference in model behavior or output quality. Generic descriptions do not pass. |
| C-06 | **Non-trivial variation** | depth | recommended | Each variation demonstrates a genuinely different design choice a practitioner would consciously select. Surface phrasing changes do not qualify. |
| C-07 | **Axis coverage breadth** | coverage | recommended | At least 4 of the 6 defined axes are represented across all N variations. |

### Aspirational (10 points total)

| ID | Criterion | Category | Source | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Combination pass labeled and deferred** | behavior | v1 | If N > 6, combination passes appear after all single-axis variations and name both axes. For N=5 with only single-axis variations, passes by vacuous truth. |
| C-09 | **Baseline variation included** | behavior | v1 | One variation (typically V-01) serves as the canonical baseline so subsequent variations are anchored to a known point. The variation heading and Axis field identify it as the reference stack. |
| C-10 | **Stop conditions structurally present (at least one imperative)** | behavior | R1/V-04 | The skill body uses explicit stop conditions or phase gates at phase boundaries to enforce generation constraints structurally -- not as purely advisory instructions. At least one boundary (Phase 1 gate, Phase 2 gate, or per-variation checkpoint) uses hard-stop imperative register ("Do not proceed", "STOP AND REWRITE") rather than advisory language. The structure itself prevents axis drift or generation overflow, not merely warns against it. |
| C-11 | **Hypothesis committed before generation begins** | behavior | R1/V-04 | The skill body requires axis and hypothesis to be declared in a phase prior to generating the variation body. Generation does not begin until the hypothesis is locked. Prevents lazy axis selection driven by what is easy to generate. |
| C-12 | **Explicit rewrite trigger** | behavior | R1/V-04 | The skill body specifies a named rewrite trigger condition (e.g., "if multi-axis drift detected, discard variation and regenerate") rather than a warning or advisory note. The trigger is checkable before the next phase begins. |
| C-13 | **Body-first generation ordering** | behavior | R2/V-01 | The skill body sequences full variation generation before any critique, scoring, or review step. The complete body is committed before evaluation can interrupt the generation path. Prevents diff-leak failures caused by premature critique interleaving with body construction. |
| C-14 | **Per-variation completeness checkpoint** | behavior | R2/V-02 | The skill body includes an explicit quality gate after each individual variation body is generated, before proceeding to the next variation. End-of-run review alone does not satisfy this criterion. Prevents late-variation degradation where early bodies are complete but later ones truncate under token pressure. |
| C-15 | **Named domain persona for role framing** | behavior | R2/V-03 | The skill uses a named domain expert persona (e.g., VariationScientist) rather than a generic instruction-following framing. Named roles carry behavioral priors toward systematic, hypothesis-driven work -- resulting in more precise axis selection and more falsifiable hypotheses than role-neutral framing. |
| C-16 | **Inertia labels per phase boundary** | behavior | R3/V-05 | The skill body names the failure mode that each phase is designed to prevent, placed before that phase's instructions execute. This is causal framing: "this phase prevents X" rather than "do not do X." Distinct from C-10 (which gates after violation); C-16 sets behavioral prior before execution so the model enters each phase already oriented against the named failure. Coverage required at Phase 1, Phase 2, and Phase 3. |
| C-17 | **Intentional degradation as experimental control** | behavior | R3/V-03 | At least one variation intentionally removes a structural feature (e.g., STOP CONDITION gates, inertia labels) to serve as a measurement instrument for that feature's contribution to output quality. The variation's hypothesis explicitly predicts where and how degradation will manifest relative to the baseline. The variation is not an accident -- it is a controlled experiment within the variation set. |
| C-18 | **Cross-axis secondary-effect prediction in hypothesis** | behavior | R3/V-04 | The hypothesis for at least one variation predicts secondary structural effects caused by the primary axis change -- not only the intended outcome but downstream consequences on other observable dimensions. At minimum, the hypothesis models one opposing or countervailing effect (e.g., "increases compliance with spirit while reducing compliance with letter"). Higher-order falsifiability beyond C-05's single-outcome prediction. |
| C-19 | **Cross-variation causal prediction** | behavior | R4/V-03 | The hypothesis for at least one variation identifies specific other variations in the set by ID as the predicted sites where its secondary effects will manifest (e.g., "produces detectable completeness degradation in V-04 and V-05"). Cross-variation falsifiability: the prediction spans the variation set rather than staying within a single variation's scope. Distinct from C-18: C-18 requires a countervailing secondary effect; C-19 requires that effect be localized to named sibling variations. A variation can satisfy C-18 without C-19 if it predicts opposing effects without naming where in the set those effects will appear. |
| C-20 | **Structural hypothesis template enforcement** | behavior | R4/V-05 | The skill body provides a multi-part hypothesis template (e.g., a planning table with named columns for primary-effect prediction, secondary-effect prediction, and predicted manifestation site) that mechanically produces C-18-compliant hypotheses through format constraints rather than instruction or inertia framing. This is to C-18 what C-10 is to C-03: structural prevention rather than advisory instruction. Distinct from C-16: C-16 operates at phase level; C-20 operates at hypothesis-field level. A skill with C-16 inertia labels will improve hypothesis quality on average; only C-20 makes multi-part hypothesis structure mandatory through format. |
| C-21 | **Set-level predicates in per-variation checkpoint** | behavior | R5/V-03 | The per-variation quality gate (C-14) includes at least one row or check that tests a set-level predicate -- a property that spans the planning table or variation set as a whole (e.g., "Does at least one planning-table row have a named sibling V-ID in the Secondary effect column?"). This enforces global planning-table coherence incrementally from within each variation's local gate, rather than deferring cross-variation verification to a final end-of-run review. Distinct from C-14: C-14 requires the gate to exist; C-21 requires the gate to include set-level predicates alongside local body checks. A checkpoint that only verifies the current variation's body completeness satisfies C-14 but not C-21. |
| C-22 | **Dual independent activation paths to the same aspirational criterion** | behavior | R5/V-03+V-05 | The variation set includes at least two variations that independently produce compliance with the same high-order aspirational criterion (e.g., C-19) through mechanically distinct mechanisms -- one via a format prompt in Phase 2 (e.g., rubric row), one via a role prior established in Phase 1 (e.g., persona obligation). The paths are structurally independent: removing one variation does not eliminate the other's activation path. Distinct from C-07 (which requires different axes): C-22 requires the same high-order criterion reached by different structural mechanisms. |
| C-23 | **Checkpoint imperative register enforces behavioral discontinuity** | behavior | R5/V-02 | The per-variation checkpoint uses hard-stop imperative language (e.g., "STOP AND REWRITE THIS VARIATION") in its failure-handling branch, rather than advisory language (e.g., "please verify", "consider rewriting"). Hard-stop imperatives create behavioral discontinuity -- a forced halt before the next variation begins -- that prevents the "proceed and note" bypass pattern where a model fills all fields while silently continuing past a marginal checkpoint failure. Distinct from C-10 (which applies to phase-gate language at phase boundaries) and C-12 (which requires a named rewrite trigger to exist anywhere in the skill body): C-23 applies specifically to the failure branch of the per-variation checkpoint step (C-14). |
| C-24 | **Primary-effect field analytically precise** | behavior | R6/V-03 | The hypothesis template's primary-effect field contains a bounded, specific prediction -- a claim that would be clearly falsified by even a slightly different outcome -- rather than a directional or scope-level description. The field names at least one specific, observable structural property whose absence would constitute falsification (e.g., "V-03 bodies will contain a planning-table row with a sibling V-ID in the Secondary effect column" rather than "V-03 will produce more coherent hypotheses"). Distinct from C-20 (which requires template columns to be present and non-empty): C-24 evaluates the analytical quality of the primary-effect content. Template compliance (C-20) and analytical precision (C-24) are empirically dissociable: role priors that increase secondary-effect elaboration can crowd out primary-effect sharpness, satisfying C-20 while failing C-24. |
| C-25 | **Pre-Phase-1 persona obligation installation** | behavior | R6/V-03 | The persona preamble explicitly establishes checkpoint and coherence obligations as role-constitutive duties before Phase 1 instructions appear. The preamble's language makes these obligations intrinsic to the professional identity ("Your checkpoint obligation... These are not optional checks -- they are part of your professional gate") rather than instructions to follow. This creates behavioral priming that precedes all phase gates: the model enters Phase 1 already holding cross-variation coherence as a professional obligation, not as a triggered constraint. Distinct from C-15 (which requires a named domain persona but does not specify preamble content) and C-21 (which requires set-level predicates in the per-variation checkpoint step): C-25 requires the preamble itself -- prior to Phase 1 -- to install professional obligation framing for checkpoint and coherence duties. A skill can satisfy C-15 (named persona) and C-21 (set-level checkpoint predicates) while failing C-25 if professional obligations are introduced only within phase instructions rather than established in the preamble as role-constitutive. |
| C-26 | **V-ID citation required at Phase 1 hypothesis gate** | behavior | R6/V-03 | The Phase 1 STOP CONDITION (or equivalent hypothesis commitment gate) requires explicit citation of at least one sibling V-ID before Phase 2 entry is permitted -- not merely template column completion (C-20) or a general secondary-effect prediction (C-19). The gate condition blocks generation from beginning until the hypothesis names a specific sibling variation. This enforces cross-variation awareness at the point of hypothesis lock, before any body is generated, creating an earlier enforcement checkpoint than C-21 (which tests V-ID citation at the per-variation checkpoint, after body generation). Distinct from C-19 (which requires V-IDs to appear in the hypothesis as a content quality signal, assessed at review time) and C-21 (which enforces V-ID presence as a set-level gate predicate after body generation): C-26 requires V-ID citation to be a hard prerequisite for Phase 2 entry, mechanically enforced by the Phase 1 stop condition. A skill can satisfy C-19 and C-21 while failing C-26 if V-ID citation in the hypothesis is never checked as a condition for leaving Phase 1. |
| C-27 | **All stop condition boundaries uniformly imperative** | behavior | R7/V-02 | All three stop condition boundaries -- Phase 1 gate, Phase 2 gate, AND per-variation checkpoint failure branch -- use uniformly hard-stop imperative register. Advisory language at any boundary fails this criterion even if the other two boundaries are imperative. "Please verify all 5 variations have passed... Noting a failure and continuing anyway may reduce output quality" fails; "Do not begin Phase 3... Do not proceed if any variation has a noted but unresolved failure" passes. Distinct from C-10 (which requires only that at least one boundary uses imperative register) and C-23 (which requires only the per-variation checkpoint failure branch specifically to be imperative): C-27 requires full-stack coverage, confirmed by V-02's R7 controlled ablation demonstrating that advisory Phase 2 STOP creates a measurable bypass vulnerability at the Phase 2-to-Phase 3 transition. |

---

## Scoring

```
Composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 20 * 10)
```

---

## Failure Modes (by criterion)

| Criterion | Most likely failure |
|-----------|-------------------|
| C-01 | Model emits "same structure as V-01 with X changed" instead of a full body |
| C-03 | Register change silently removes STOP CONDITION labels (co-varying structure + register) |
| C-05 | Hypothesis states intent ("to test whether...") rather than prediction ("will produce...") |
| C-10 | All stop conditions use advisory language; no boundary uses hard-stop imperative |
| C-11 | Axis declared inline with body in the same step; hypothesis written after generation |
| C-14 | Single review table at end covers all variations; no per-variation gate present |
| C-18 | Hypothesis lists two positive outcomes rather than a primary effect and a countervailing/opposing consequence |
| C-19 | Secondary effects predicted in general terms without naming which specific variation IDs will exhibit them |
| C-20 | Inertia label instructs "include a secondary-effect prediction" (C-16 approach) but no template column enforces the field structurally |
| C-21 | Checkpoint has multiple rows but all rows test only the current variation's body (completeness, axis isolation, hypothesis present) -- no row tests a set-level predicate across the planning table |
| C-22 | Only one variation targets a given high-order criterion (e.g., C-19 achieved via rubric row only); no second independent activation path present in the set |
| C-23 | Checkpoint includes a rewrite instruction but phrases it as advisory ("if any row fails, consider rewriting before proceeding") rather than imperative ("STOP AND REWRITE THIS VARIATION") |
| C-24 | Primary-effect field filled with a directional claim ("will produce more structured outputs") rather than a specific falsifiable prediction naming an observable structural property |
| C-25 | Persona preamble names the role and lists capabilities but does not establish checkpoint or coherence obligations as role-constitutive duties; obligation language appears only within phase instructions |
| C-26 | Phase 1 STOP CONDITION requires hypothesis template completion (C-20) but does not explicitly gate on V-ID citation; sibling V-IDs appear in some hypotheses but are not enforced as a Phase 1 prerequisite |
| C-27 | Phase 1 and checkpoint use imperative register but Phase 2 STOP uses advisory language ("please verify", "may reduce quality"); only two of three boundaries are uniformly imperative |

---

## quest-variate Scorecard -- R7

**Rubric:** v8 (20 aspirational criteria: C-08 through C-27)
**Scoring:** Essential 60 + Recommended 30 + Aspirational (passes/20) x 10 = 100 max

---

### V-01 -- Baseline: R7 full stack

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Complete standalone body. All three phases present, droppable as-is. |
| C-02 | PASS | V-01 heading; Axis "Baseline -- R7 full stack..."; Hypothesis three-row table. |
| C-03 | PASS | Baseline -- establishes R7 reference stack. |
| C-04 | PASS (set) | 5 variations produced. |
| C-05 | PASS | "Planning-table primary-effect fields will contain a specific observable structural artifact (a named checkpoint row type, an explicit gate condition keyword, or a required template column name)" -- specific structural property, absence clearly falsifies. |
| C-06 | PASS | Full-stack integration of C-24+C-25+C-26 is a genuine practitioner-selectable design choice. |
| C-07 | PASS (set) | 4 distinct axes across V-02-V-05: Phase 2 register, preamble obligation style, Phase 1 V-ID gate, primary-effect column-header precision. |
| C-08 | PASS (N/A) | N=5; combination passes deferred per design notes. |
| C-09 | PASS (set) | V-01 is the labeled baseline. |
| C-10 | PASS | Phase 1 STOP imperative; Phase 2 STOP imperative; checkpoint "STOP AND REWRITE THIS VARIATION." All three boundaries imperative -- trivially satisfies the revised "at least one" bar. |
| C-11 | PASS | Phase 1 STOP gates on planning-table completion + precision + V-ID citation before any body is written. |
| C-12 | PASS | "STOP AND REWRITE THIS VARIATION" -- named rewrite trigger in checkpoint failure branch. |
| C-13 | PASS | Phases 1->2->3 ordered: plan -> generate+checkpoint -> emit. Phase 3 emits after all bodies complete. |
| C-14 | PASS | Per-variation checkpoint with 4 variation-level rows + 2 set-level rows. |
| C-15 | PASS | **SetCoherenceAuditor** -- named domain expert persona. |
| C-16 | PASS | *Prevents:* labels at Phase 1 (V-ID citations + axis breadth + falsifiable primary-effect), Phase 2 (truncation + diff-leak + coherence failures), Phase 3 (critique interleaving). All three phases covered. |
| C-17 | PASS (set) | V-02 (C-27 ablation), V-03 (C-25 ablation), V-04 (C-26 ablation), V-05 (C-24 ablation) -- four intentional single-criterion ablations. |
| C-18 | PASS | "Preamble obligation framing elaborates cross-variation interaction detail, potentially crowding primary-effect sharpness in later slots... precision column-header provides a structural floor." Named countervailing effect with mitigation. |
| C-19 | PASS | V-04 and V-05 named as predicted secondary-effect sites. |
| C-20 | PASS | Column header: "name one specific structural property whose absence in the actual body would clearly falsify this claim -- not a directional description." Five named columns enforcing multi-part structure. |
| C-21 | PASS | "*Set-level checks (your professional obligation as SetCoherenceAuditor):*" -- two predicate rows: V-ID citation coverage (planning-table property) and Axis breadth (set-level aggregate). |
| C-22 | PASS (set) | V-01 achieves C-21 via role-prior+format; V-03 via format only -- two structurally independent mechanisms. |
| C-23 | PASS | "STOP AND REWRITE THIS VARIATION. Do not note the failure and continue." Hard-stop imperative, no advisory fallback. |
| C-24 | PASS | Column header instructs falsifiability with negative example. Phase 1 STOP condition 2 checks for this. Precision floor structurally enforced. |
| C-25 | PASS | "Your professional obligations -- established before Phase 1 begins. These are role-constitutive duties, not phase instructions:... verifying the set-level coherence predicates is not optional -- it is your professional gate responsibility." Obligation framing in preamble before Phase 1 heading. |
| C-26 | PASS | Phase 1 STOP condition 3: "A planning table in which every cell in this column is blank or contains only a general description fails this gate regardless of whether other columns are complete." V-ID citation is a mandatory gate condition. |
| C-27 | PASS | Phase 1 STOP imperative ("Do not begin Phase 2 until..."); Phase 2 STOP imperative ("Do not begin Phase 3... Do not proceed if any variation has a noted but unresolved failure"); checkpoint "STOP AND REWRITE THIS VARIATION." All three boundaries uniformly imperative. |

**Aspirational: 20/20 -> 10.0** | **Total: 100.0**

---

### V-02 -- Phase 2 advisory (C-27 ablation)

| ID | Result | Evidence |
|----|--------|----------|
| C-01-C-09 | PASS | Complete body, labels, single axis, set-level pass. |
| C-10 | PASS | Phase 1 STOP imperative; checkpoint "STOP AND REWRITE THIS VARIATION" imperative. At least one boundary imperative -- revised C-10 bar satisfied even though Phase 2 STOP is advisory. |
| C-11-C-16 | PASS | All retained from V-01. |
| C-17 | PASS (set) | V-02 is itself the C-27 ablation instrument. |
| C-18 | PASS | "Degradation isolates specifically to the Phase 2-to-Phase-3 boundary, not to within-phase generation quality" -- named countervailing. |
| C-19 | PASS | V-01 named as sibling site. |
| C-20-C-26 | PASS | Precision column, obligation preamble, V-ID gate all retained. |
| C-27 | **FAIL** | Phase 2 STOP advisory: "Please verify all 5 variations have passed... Noting a failure and continuing anyway may reduce output quality." Advisory register at Phase 2 boundary while Phase 1 and checkpoint are imperative. Not all three boundaries uniformly imperative. C-27 ablated by design. |

**Aspirational: 19/20 -> 9.5** | **Total: 99.5**

---

### V-03 -- C-25 ablation: VariationScientist without preamble obligations

| ID | Result | Evidence |
|----|--------|----------|
| C-01-C-24 | PASS | All structural phases identical to V-01; precision column, V-ID gate, imperative stops, set-level checkpoint rows all retained. "*Set-level checks:*" label present (no obligation framing -- that is the ablation, which is C-25's domain, not C-21's pass condition). |
| C-25 | **FAIL** | Opening: "You are a VariationScientist -- a systematic specialist... You produce complete variation bodies, commit hypotheses before generation, and verify axis isolation." Descriptive framing. No "established before Phase 1 begins," no "role-constitutive duties, not phase instructions," no "professional gate responsibility." Obligation installation absent by design. |
| C-26 | PASS | Phase 1 condition 3 retained unchanged. |
| C-27 | PASS | All three stop boundaries retain imperative register from V-01 (Phase 2 advisory ablation was V-02's axis, not V-03's). |

**Aspirational: 19/20 -> 9.5** | **Total: 99.5**

---

### V-04 -- C-26 ablation: Phase 1 V-ID gate removed

| ID | Result | Evidence |
|----|--------|----------|
| C-01-C-25 | PASS | Full C-25 preamble obligations retained. Imperative stop conditions retained. Set-level checkpoint rows retained (C-21). Phase 1 *Prevents:* label correctly omits V-ID citation concern (accurate, not missing). |
| C-26 | **FAIL** | Phase 1 STOP has two conditions only: all rows complete; >=4 distinct axes. No V-ID citation gate. The planning table has the column but the Phase 1 STOP does not check it. C-26 ablated by design. |
| C-27 | PASS | Phase 1, Phase 2, and checkpoint stop conditions all retain imperative register. |

**Aspirational: 19/20 -> 9.5** | **Total: 99.5**

---

### V-05 -- C-24 ablation: primary-effect column header directional

| ID | Result | Evidence |
|----|--------|----------|
| C-01-C-23 | PASS | All structures identical to V-01 except column header wording. |
| C-24 | **FAIL** | Column header: "describe the expected behavioral change this axis produces." No falsifiability framing; no negative example. Phase 1 STOP condition 2 checks for "substantive prediction... not a trivial placeholder" -- quality threshold, not precision requirement. C-24 ablated by design. |
| C-25 | PASS | Full preamble obligations retained. |
| C-26 | PASS | Phase 1 condition 3 (V-ID citation gate) retained and unchanged. |
| C-20 | PASS | Template structure present; column non-empty. Hypothesis correctly articulates C-20 satisfied while C-24 fails. |
| C-27 | PASS | All three stop boundaries retain imperative register. |

**Aspirational: 19/20 -> 9.5** | **Total: 99.5**

---

### Composite Scores and Ranking

| Rank | Variation | Essential | Recommended | Aspirational | **Total** | Failures |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | V-01 Baseline R7 full stack | 60.0 | 30.0 | 10.0 | **100.0** | -- |
| 2 | V-02 Phase 2 advisory | 60.0 | 30.0 | 9.5 | **99.5** | C-27 |
| 2 | V-03 C-25 ablation | 60.0 | 30.0 | 9.5 | **99.5** | C-25 |
| 2 | V-04 C-26 ablation | 60.0 | 30.0 | 9.5 | **99.5** | C-26 |
| 2 | V-05 C-24 ablation | 60.0 | 30.0 | 9.5 | **99.5** | C-24 |

---

**One R7 excellence signal promoted -> C-27.** Aspirational denominator bumps from 19 to 20. C-27 is a clean split of v7's C-10: V-02's intentional Phase 2 STOP advisory ablation is the first controlled single-boundary-register experiment, confirming that the Phase 2-to-Phase 3 transition is an independently testable failure site. C-10 retains the structural enforcement intent (at least one boundary imperative) and C-27 captures the uniformity requirement (all three boundaries imperative). V-02, V-03, V-04, and V-05 all score 99.5 -- a flat tier that reflects R7's design intent of testing four independent criteria at equal depth. The R7->R8 candidate targets the Phase 3 *Prevents:* label content density gap (one failure mode vs. three in Phases 1-2) as the next boundary to test.
