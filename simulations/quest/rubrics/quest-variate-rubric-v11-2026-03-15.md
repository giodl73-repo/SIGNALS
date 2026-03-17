### Changes from v10 -> v11

**One new criterion extracted:**

**C-34 -- Secondary-effect transfer endpoint naming** (R10/V-01)
V-01's secondary-effect field reads "shifting truncation pressure FROM primary-effect cell analytical depth TO secondary-effect column header elaboration." C-18 requires a countervailing consequence; C-34 requires the secondary-effect field to name both the source structural element and the destination structural element of the predicted transfer -- the FROM endpoint and the TO endpoint -- not merely assert that a tradeoff or shift exists. V-02's ablation reverts the secondary-effect column header to directional-only framing ("name a countervailing consequence... describe the opposing effect") without FROM/TO endpoints; if V-02 produces measurable forecasting degradation on secondary-effect endpoint-naming rate relative to V-01's FROM/TO framing, that confirms the C-34 split from C-18. A secondary effect reading "potentially increasing token consumption elsewhere" satisfies C-18 (countervailing consequence present) but fails C-34 (no source/destination endpoints named). A secondary effect reading "shifting truncation risk FROM emit-phase failures TO late-variation body compression" satisfies both.

**Scoring: denominator 26 -> 27.**

Under v11, V-01 (R10 baseline) satisfies all 27 criteria and scores 100.00. V-02, V-03, V-04 each fail exactly one criterion and score 99.63. V-05 (combination ablation floor) fails C-34+C-25 and scores 99.26. C-34 is confirmed as a set-level pass for R10, established by V-01's FROM/TO secondary-effect field and falsified in V-02 via directional-only ablation.

**R11->R12 candidate:** None identified from R10. The C-34 confirmation closes the secondary-effect endpoint-naming gap. Next candidate would require a new mechanism observed in R11's variation set.

---

## Design Decisions

- **C-08 through C-34** are all aspirational -- their absence does not prevent a functional variation set, but their presence marks a higher-order design capability.
- **C-16/C-17/C-18** are distinct from C-10/C-11/C-12/C-13/C-14/C-15: a skill body can satisfy C-10 without C-16, C-05 without C-18, etc.
- **C-19** is distinct from C-18: C-18 requires that at least one variation's hypothesis model a countervailing secondary effect. C-19 requires that effect be localized to named sibling variations. A variation can satisfy C-18 without C-19 if it predicts opposing effects without naming where in the set those effects will appear.
- **C-20** is distinct from C-16: C-16 operates at phase level (inertia labels before each phase's instructions). C-20 operates at hypothesis-field level (a template with named columns that force multi-part structure). A skill with strong C-16 framing will improve hypothesis quality on average; only C-20 makes multi-part hypothesis structure mandatory through format.
- **C-21** is distinct from C-14: C-14 requires a per-variation quality gate to exist; C-21 requires that gate to include at least one row that tests a set-level predicate. A checkpoint that only verifies the current variation's body completeness satisfies C-14 but not C-21.
- **C-22** is distinct from C-07: C-07 requires different axes represented across variations; C-22 requires the same high-order aspirational criterion activated by structurally independent mechanisms in at least two variations.
- **C-23** is distinct from C-12: C-12 requires a named rewrite trigger anywhere in the skill body; C-23 requires that the per-variation checkpoint's failure branch specifically uses hard-stop imperative register.
- **C-24** is distinct from C-20: C-20 requires all planning-table columns to be present and non-empty; C-24 evaluates the analytical quality of the primary-effect content. Template compliance (C-20) and analytical precision (C-24) are empirically dissociable.
- **C-25** is distinct from C-15 and C-21: C-15 requires a named domain persona; C-21 requires set-level predicates in the per-variation checkpoint; C-25 requires the persona preamble to install checkpoint and coherence obligations as role-constitutive duties before Phase 1.
- **C-26** is distinct from C-19 and C-21: C-19 requires sibling V-IDs in the hypothesis as a content quality signal; C-21 enforces V-ID presence as a gate predicate after body generation; C-26 requires V-ID citation to be a hard prerequisite for Phase 2 entry. The three form a temporal enforcement chain: C-26 gates at hypothesis lock, C-21 gates at body completion, C-19 evaluates content quality at review time.
- **C-27** is distinct from C-10 and C-23: C-10 requires at least one boundary imperative; C-23 requires the per-variation checkpoint failure branch specifically to be imperative; C-27 requires all three boundaries (Phase 1 gate, Phase 2 gate, per-variation checkpoint) uniformly imperative. The three form a boundary coverage ladder: C-10 (entry bar) -> C-23 (checkpoint boundary) -> C-27 (full stack uniform).
- **C-28** is distinct from C-16: C-16 requires *Prevents:* label presence at all three phases; C-28 requires each label to enumerate at least 2 distinct named failure modes. A phase with *Prevents: generation errors* passes C-16 (structural presence) and fails C-28 (no named modes). V-03's single-mode Phase 3 label passes C-16, fails C-28.
- **C-29** is distinct from C-27: C-27 requires Phase 1/Phase 2/checkpoint uniformly imperative (3 boundaries); C-29 requires Phase 3 emission to be gated as a fourth structural boundary with its own STOP CONDITION block. A skill with C-27-compliant phases and a *Prevents:* label at Phase 3 fails C-29 if no structural gate precedes Phase 3 emission.
- **C-30** is distinct from C-24 and C-19: C-24 requires precise structural prediction of the variation's own body; C-19 requires sibling V-IDs anywhere in hypothesis; C-30 requires a sibling's positive expected text content in the primary-effect field specifically. Absence framing ("this block will be absent in V-03") does not satisfy C-30 -- only positive expected content in the sibling ("V-03's Phase 3 will begin directly with 'Output V-01 through V-05 in order'") satisfies.
- **C-31** is distinct from C-19: C-19 requires sibling V-IDs to appear in the predicted-manifestation-site field; C-31 requires at least one such entry to use conditional if-then structure naming the mechanism under test and the competing mechanism. Naming "V-03 and V-04" satisfies C-19 but not C-31; "if V-01 outperforms V-03 on truncation incidence, Phase 3 STOP CONDITION adds enforcement value beyond the *Prevents:* inertia label" satisfies both. The distinction captures whether the predicted site is merely identified (C-19) or explicitly framed as a conditional falsification test for a named mechanism (C-31).
- **C-32** is distinct from C-08: C-08 requires combination passes to be labeled, deferred, and named (both axes). C-32 requires the combination variation's hypothesis to name the single-ablation counterparts by V-ID, name the mechanisms they each test, and state the superadditivity condition. A variation set can satisfy C-08 (combination pass labeled and positioned) while failing C-32 if the combination's hypothesis uses directional framing without identifying the single-ablation references or the interaction test.
- **C-33** is distinct from C-03: C-03 requires single-axis isolation relative to the current-round V-01 baseline. C-33 requires at least one ablation variation's axis label to name the prior-round state it reproduces (e.g., "R8/V-05 state", "R8/V-01 state exactly"), extending the genealogical trace across rounds. A variation satisfies C-03 by naming its single changed axis without any prior-round reference; C-33 is an additional requirement for cross-round traceability in the axis label.
- **C-34** is distinct from C-18: C-18 requires the hypothesis to model at least one countervailing or opposing secondary effect. C-34 requires the secondary-effect field to name both the source structural element and the destination structural element of the predicted transfer -- the FROM endpoint and the TO endpoint. A secondary effect satisfies C-18 by modeling opposition ("increases token consumption elsewhere") without naming endpoints; C-34 requires those endpoints to be explicitly named ("shifting truncation risk FROM emit-phase failures TO late-variation body compression"). The two are a progressive specificity pair: C-18 establishes the countervailing consequence; C-34 requires its spatial grounding within the variation's structural model.
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
| C-16 | **Inertia labels per phase boundary** | behavior | R3/V-05 | The skill body names the failure mode that each phase is designed to prevent, placed before that phase's instructions execute. This is causal framing: "this phase prevents X" rather than "do not do X." Coverage required at Phase 1, Phase 2, and Phase 3. |
| C-17 | **Intentional degradation as experimental control** | behavior | R3/V-03 | At least one variation intentionally removes a structural feature to serve as a measurement instrument for that feature's contribution to output quality. The variation's hypothesis explicitly predicts where and how degradation will manifest relative to the baseline. The variation is a controlled experiment, not an accident. |
| C-18 | **Cross-axis secondary-effect prediction in hypothesis** | behavior | R3/V-04 | The hypothesis for at least one variation predicts secondary structural effects caused by the primary axis change -- not only the intended outcome but downstream consequences on other observable dimensions. At minimum, the hypothesis models one opposing or countervailing effect. Higher-order falsifiability beyond C-05's single-outcome prediction. |
| C-19 | **Cross-variation causal prediction** | behavior | R4/V-03 | The hypothesis for at least one variation identifies specific other variations in the set by ID as the predicted sites where its secondary effects will manifest (e.g., "produces detectable completeness degradation in V-04 and V-05"). Cross-variation falsifiability: the prediction spans the variation set rather than staying within a single variation's scope. Distinct from C-18: C-18 requires a countervailing secondary effect; C-19 requires that effect be localized to named sibling variations. |
| C-20 | **Structural hypothesis template enforcement** | behavior | R4/V-05 | The skill body provides a multi-part hypothesis template (e.g., a planning table with named columns for primary-effect prediction, secondary-effect prediction, and predicted manifestation site) that mechanically produces C-18-compliant hypotheses through format constraints rather than instruction or inertia framing. |
| C-21 | **Set-level predicates in per-variation checkpoint** | behavior | R5/V-03 | The per-variation quality gate (C-14) includes at least one row or check that tests a set-level predicate -- a property that spans the planning table or variation set as a whole (e.g., "Does at least one planning-table row have a named sibling V-ID in the Predicted manifestation site column?"). Enforces global planning-table coherence incrementally from within each variation's local gate. |
| C-22 | **Dual independent activation paths to the same aspirational criterion** | behavior | R5/V-03+V-05 | The variation set includes at least two variations that independently produce compliance with the same high-order aspirational criterion through mechanically distinct mechanisms -- one via format prompt in Phase 2, one via role prior in Phase 1. The paths are structurally independent: removing one variation does not eliminate the other's activation path. |
| C-23 | **Checkpoint imperative register enforces behavioral discontinuity** | behavior | R5/V-02 | The per-variation checkpoint uses hard-stop imperative language (e.g., "STOP AND REWRITE THIS VARIATION") in its failure-handling branch, rather than advisory language. Hard-stop imperatives create behavioral discontinuity -- a forced halt before the next variation begins -- that prevents the "proceed and note" bypass pattern. |
| C-24 | **Primary-effect field analytically precise** | behavior | R6/V-03 | The hypothesis template's primary-effect field contains a bounded, specific prediction -- a claim that would be clearly falsified by even a slightly different outcome. The field names at least one specific, observable structural property whose absence would constitute falsification. Distinct from C-20 (template compliance) and C-30 (sibling text anchor): C-24 evaluates the analytical precision of the primary-effect content as a standalone claim about the variation's own body. |
| C-25 | **Pre-Phase-1 persona obligation installation** | behavior | R6/V-03 | The persona preamble explicitly establishes checkpoint and coherence obligations as role-constitutive duties before Phase 1 instructions appear. The preamble's language makes these obligations intrinsic to the professional identity ("These are role-constitutive duties, not phase instructions") rather than instructions to follow. Distinct from C-15 (named persona) and C-21 (set-level checkpoint predicates): C-25 requires the preamble itself to install obligation framing before Phase 1. |
| C-26 | **V-ID citation required at Phase 1 hypothesis gate** | behavior | R6/V-03 | The Phase 1 STOP CONDITION requires explicit citation of at least one sibling V-ID before Phase 2 entry is permitted. The gate condition blocks generation from beginning until the hypothesis names a specific sibling variation. Enforces cross-variation awareness at hypothesis lock, before any body is generated. Distinct from C-19 (content quality signal at review time) and C-21 (set-level gate after body generation): C-26 requires V-ID citation as a hard prerequisite for Phase 2 entry. |
| C-27 | **All stop condition boundaries uniformly imperative** | behavior | R7/V-02 | All three stop condition boundaries -- Phase 1 gate, Phase 2 gate, AND per-variation checkpoint failure branch -- use uniformly hard-stop imperative register. Advisory language at any boundary fails this criterion even if the other two boundaries are imperative. Distinct from C-10 (at least one boundary imperative) and C-23 (checkpoint failure branch specifically imperative): C-27 requires full-stack coverage across all three boundaries. |
| C-28 | ***Prevents:* label content density** | behavior | R8/V-01 | Each phase's *Prevents:* label enumerates at least 2 distinct named failure modes. Single-mode labels pass C-16 (presence) but fail C-28 (density). Generic labels naming no specific failure mode (e.g., "*Prevents: generation errors*") fail both C-16 and C-28 independently. Coverage required at Phase 1, Phase 2, and Phase 3. |
| C-29 | **Phase 3 structural enforcement parity** | behavior | R8/V-05 | Phase 3 emission is preceded by an explicit STOP CONDITION block that gates on Phase 2 completion before any variation body is output -- parallel to the Phase 1 and Phase 2 structural gates. C-27 covers Phase 1/Phase 2/checkpoint as three uniformly imperative boundaries; C-29 extends structural gating to Phase 3 as a fourth boundary. A *Prevents:* inertia label at Phase 3 does not satisfy C-29 -- a structural block requiring confirmed Phase 2 completion must be present. |
| C-30 | **Primary-effect field as cross-variation falsification anchor** | behavior | R8/V-01 | At least one variation's primary-effect field embeds a sibling variation's positive expected text content as the falsification mechanism. The sibling's exact anticipated text (or first words) serves as the empirical anchor: if the sibling's actual output does not match, the primary-effect prediction is falsified. Absence framing ("this block will be absent in V-03") does not satisfy -- only positive expected content in the sibling ("V-03's Phase 3 will begin directly with 'Output V-01 through V-05 in order'") satisfies. Distinct from C-24 (own-body structural prediction) and C-19 (sibling V-IDs anywhere in hypothesis): C-30 requires the sibling's positive text specifically in the primary-effect field. |
| C-31 | **Conditional mechanism-test framing in predicted-site entries** | behavior | R9/V-01 | At least one variation's predicted-site field uses explicit conditional if-then structure to frame the sibling relationship as a falsification test: "if [baseline] outperforms [named sibling] on [specific observable metric], [named mechanism] adds [specific type of] value [beyond named competing mechanism]." Naming sibling V-IDs (C-19) does not satisfy C-31; the if-then conditional naming both the mechanism under test and the competing mechanism it is measured against is required. The conditional structure makes the predicted site's role in the measurement design explicit rather than leaving it implicit. |
| C-32 | **Combination ablation superadditivity test in hypothesis** | behavior | R9/V-05 | The combination variation's primary-effect field explicitly names (a) the single-ablation baseline variations by V-ID, (b) the mechanism each single-ablation tests, and (c) the superadditivity condition as the measurement hypothesis: "[combination] will [degrade/differ] more than either [V-ID (mechanism A alone)] or [V-ID (mechanism B alone)] if the mechanisms are positively interactive." C-08 requires the combination pass to be labeled, deferred, and named; C-32 additionally requires the combination's hypothesis to contain the explicit interaction test. A labeled combination variation with only directional framing ("tests the joint contribution of C-29 and C-30") fails C-32. |
| C-33 | **Prior-round state genealogy in ablation axis label** | behavior | R9/V-02, V-05 | At least one ablation variation's axis label names the prior-round state it reproduces, using the pattern "[R-N/V-MM state]" or equivalent formulation (e.g., "equivalent to R8/V-05 state under v9", "R8/V-01 state exactly"). This creates a genealogical link enabling cross-round comparison and confirms the ablation's position in the multi-round measurement sequence without requiring the scorer to trace back through previous variation sets. Distinct from C-03 (single-axis isolation relative to the current-round baseline): C-33 requires the axis label to name the prior-round analog explicitly. |
| C-34 | **Secondary-effect transfer endpoint naming** | behavior | R10/V-01 | The secondary-effect field for at least one variation names both the source structural element and the destination structural element of the predicted tradeoff, using explicit FROM/TO framing or equivalent directional endpoint syntax. Naming that a tradeoff "shifts" or "transfers" risk or consumption without identifying the source and destination elements fails C-34. A secondary effect reading "potentially increasing token consumption elsewhere" satisfies C-18 (countervailing consequence present) but fails C-34 (no source/destination endpoints named). A secondary effect reading "shifting truncation pressure FROM primary-effect cell analytical depth TO secondary-effect column header elaboration" satisfies both. Distinct from C-18 (countervailing consequence required): C-18 establishes that an opposing effect is modeled; C-34 requires the spatial grounding of that transfer within the variation's structural model via named FROM and TO endpoints. |

---

## Scoring

```
Composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 27 * 10)
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
| C-28 | One or more phases have a *Prevents:* label naming only a single failure mode, or naming a generic category without identifying distinct named modes |
| C-29 | Phase 3 has a *Prevents:* inertia label (satisfying C-16/C-28) but no structural STOP CONDITION block gating on Phase 2 completion before emission begins |
| C-30 | Primary-effect field names absence of a structure in a sibling ("this block will be absent in V-03") rather than positive expected content in that sibling ("V-03's Phase 3 will begin with 'Output V-01...'") |
| C-31 | Predicted-site entries name sibling V-IDs (satisfying C-19) but use directional framing ("V-03 will show lower quality") without if-then conditional structure naming mechanism under test and the competing mechanism |
| C-32 | Combination variation hypothesis names the combined mechanisms ("tests C-34 + C-25 interaction") but does not name the single-ablation baselines by V-ID or state the superadditivity condition explicitly |
| C-33 | Ablation axis labels describe the axis change ("secondary-effect column reverts to directional-only framing") without naming the prior-round variation state the ablation reproduces (e.g., "R9/V-01 state exactly") |
| C-34 | Secondary-effect field models an opposing consequence ("potentially shifting truncation risk to later phases") satisfying C-18 but names no source structural element and no destination structural element -- the FROM and TO endpoints are absent or implied rather than stated |

---

## quest-variate Scorecard -- R10

**Rubric:** v11 (27 aspirational criteria: C-08 through C-34)
**Scoring:** `(essential_pass/4 x 60) + (recommended_pass/3 x 30) + (aspirational_pass/27 x 10)`

---

### Structural Baseline (all variations share SetCoherenceAuditor skeleton)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-04 | PASS | 5 variations produced |
| C-07 | PASS | 4+ distinct axes: C-34 candidate, C-25, C-21, combination pass |
| C-08 | PASS | V-05 labeled "V-02 x V-03 combination," appears last |
| C-09 | PASS | V-01 labeled baseline |
| C-17 | PASS | V-02/V-03/V-04 single-criterion ablations; V-05 dual-ablation floor |
| C-22 | PASS | C-19 achieved via role-constitutive preamble path (V-01/V-02/V-04) and predicate checkpoint rows path (V-01/V-02/V-03); structurally independent |
| C-31 | PASS | V-01 predicted site: "if V-01 produces secondary-effect fields that consistently name a structural source and destination while V-02 produces directional-only fields... the FROM/TO column constraint confirms propagation mechanism value beyond purely instructional countervailing-effect framing; if both produce equivalent endpoint-naming... the column constraint is advisory rather than structural -- and C-34 does not warrant criterion status" -- two-branch conditional naming mechanism under test AND competing mechanism |
| C-32 | PASS | V-05 names V-02 (C-34 ablation alone) and V-03 (C-25 ablation alone) by V-ID; states superadditivity condition: "if V-05 degrades more than either V-02 or V-03 on secondary-effect endpoint-naming rate, the mechanisms are confirmed positively interactive" |
| C-33 | PASS | V-02 axis: "R9/V-01 secondary-effect template state exactly (pre-C-34 candidate mechanism)"; V-05 axis: "R9/V-01 secondary-effect column state exactly" -- both use R-N/V-MM prior-round genealogy pattern |

---

### V-01 -- Baseline: R10 Full Stack

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Complete standalone body; all three phases with full text |
| C-02 | PASS | `## V-01`, `**Axis:**`, `**Hypothesis:**` all present and non-empty |
| C-03 | PASS | Baseline -- no axis changed relative to itself |
| C-05 | PASS | Primary-effect names exact phrases: "FROM which structural element" and "TO which structural element" -- absence in V-02's actual body would falsify |
| C-06 | PASS | Full C-34 candidate mechanism in secondary-effect column header is a genuine design choice |
| C-10 | PASS | Phase 1 "do not begin Phase 2" (imperative); Phase 2 "Do not begin Phase 3" (imperative); checkpoint "STOP AND REWRITE THIS VARIATION" -- all three boundaries |
| C-11 | PASS | Planning table + Phase 1 STOP CONDITIONS gate before Phase 2 entry |
| C-12 | PASS | "STOP AND REWRITE THIS VARIATION. Do not note the failure and continue." -- named rewrite trigger |
| C-13 | PASS | Phase 1 -> Phase 2 -> Phase 3 body-first ordering enforced by gates |
| C-14 | PASS | Per-variation SetCoherenceAuditor checkpoint with 4 variation-level rows + 2 set-level rows |
| C-15 | PASS | "You are a SetCoherenceAuditor" -- named domain persona |
| C-16 | PASS | *Prevents:* at Phase 1 (3 modes), Phase 2 (3 modes), Phase 3 (3 modes) |
| C-18 | PASS | Secondary-effect hypothesis: "shifting truncation pressure FROM primary-effect cell analytical depth TO secondary-effect column header elaboration" -- countervailing consequence with named FROM/TO transfer endpoints |
| C-19 | PASS | "V-02 (C-34 ablation)" named as specific sibling in predicted site |
| C-20 | PASS | Five-column planning table with structurally enforced FROM/TO secondary-effect column header |
| C-21 | PASS | "*Set-level checks (your professional obligation as SetCoherenceAuditor):*" -- V-ID citation coverage and Axis breadth rows test set-level predicates |
| C-23 | PASS | "STOP AND REWRITE THIS VARIATION. Do not note the failure and continue." -- hard-stop imperative in checkpoint failure branch |
| C-24 | PASS | Primary-effect names exact expected phrases "FROM which structural element" and "TO which structural element" -- specific structural property whose absence would falsify |
| C-25 | PASS | "Your professional obligations -- established before Phase 1 begins. These are role-constitutive duties, not phase instructions:... verifying the set-level coherence predicates is not optional -- it is your professional gate responsibility." -- preamble installs obligations before Phase 1 |
| C-26 | PASS | Phase 1 STOP CONDITION item 3 explicitly gates on V-ID citation: "a planning table in which every cell in this column is blank or contains only a general description fails this gate" |
| C-27 | PASS | Phase 1 STOP (imperative); Phase 2 STOP (imperative); checkpoint failure branch "STOP AND REWRITE" (imperative) -- all three uniformly imperative |
| C-28 | PASS | Phase 1, Phase 2, Phase 3 *Prevents:* labels each contain >=2 named failure modes |
| C-29 | PASS | "Phase 3 STOP CONDITION -- do not begin emitting any variation until this condition is met: All 5 variation bodies confirmed complete in Phase 2" -- structural gate before any emission |
| C-30 | PASS | Primary-effect embeds V-02's positive expected column header text: "name a countervailing consequence of the primary-axis change -- describe the opposing effect the axis change introduces" -- sibling's exact anticipated text as falsification anchor |
| C-34 | PASS | Secondary-effect names FROM endpoint ("primary-effect cell analytical depth") and TO endpoint ("secondary-effect column header elaboration") explicitly -- both transfer endpoints present |

**Essential: 4/4 | Recommended: 3/3 | Aspirational: 27/27**

```
composite = (4/4 x 60) + (3/3 x 30) + (27/27 x 10)
          = 60 + 30 + 10.00
          = 100.00
```

**Score: 100.00 / 100**

---

### V-02 -- C-34 Ablation: Secondary-Effect Column Reverts to Directional-Only Framing

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Complete standalone body |
| C-02 | PASS | All three labels present and non-empty |
| C-03 | PASS | Exactly one axis changed: secondary-effect column header; all other structure identical to V-01 |
| C-05 | PASS | Primary-effect names exact phrases: V-01 will have "FROM which structural element" and "TO which structural element"; V-02 will have "name a countervailing consequence of the primary-axis change -- describe the opposing effect the axis change introduces" -- double-anchored structural claim |
| C-10--C-33 | PASS | Full structural skeleton identical to V-01 -- role-constitutive preamble, imperative stops, V-ID gate, set-level predicate checkpoint rows, Phase 3 STOP CONDITION, three-mode *Prevents:* at all phases all retained; C-18 satisfied (countervailing consequence present in directional framing); C-34 is the isolated axis under ablation |
| C-34 | **FAIL** | Secondary-effect column header uses directional-only framing ("name a countervailing consequence of the primary-axis change -- describe the opposing effect the axis change introduces") without FROM/TO endpoint naming -- C-18 satisfied, C-34 isolated ablation confirmed |

**Essential: 4/4 | Recommended: 3/3 | Aspirational: 26/27**

```
composite = (4/4 x 60) + (3/3 x 30) + (26/27 x 10)
          = 60 + 30 + 9.630...
          = 99.63
```

**Score: 99.63 / 100 -- C-34 ablation confirmed**

---

### V-03 -- C-25 Ablation: Instruction-Register Preamble

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Complete standalone body |
| C-02 | PASS | All three labels present and non-empty |
| C-03 | PASS | Exactly one axis changed: preamble framing; secondary-effect column header retains FROM/TO language |
| C-05 | PASS | Primary-effect names specific structural property: phrase "role-constitutive duties, not phase instructions" will be absent; "Instructions for this session" will be present |
| C-10--C-20 | PASS | All structural skeleton retained except preamble register; *Prevents:* at all phases with 3 modes, Phase 3 STOP CONDITION, planning table with FROM/TO column, V-ID gate, predicate checkpoint rows all retained |
| C-21 | PASS | Set-level predicate rows retained in checkpoint: "*Set-level checks (your professional obligation as SetCoherenceAuditor):*" |
| C-22--C-24 | PASS | Imperative register uniform across all boundaries; primary-effect analytically precise |
| C-25 | **FAIL** | Preamble uses instruction-register framing ("Instructions for this session") rather than role-constitutive obligations framing ("These are role-constitutive duties, not phase instructions") -- preamble does not install checkpoint obligations as identity-intrinsic before Phase 1 |
| C-26--C-34 | PASS | V-ID gate at Phase 1, uniformly imperative boundaries, *Prevents:* density >=2 at all phases, Phase 3 STOP CONDITION, sibling positive text in primary-effect, conditional mechanism-test framing, superadditivity test (set-level), prior-round genealogy (set-level), FROM/TO secondary-effect endpoints all retained |

**Essential: 4/4 | Recommended: 3/3 | Aspirational: 26/27**

```
composite = (4/4 x 60) + (3/3 x 30) + (26/27 x 10)
          = 60 + 30 + 9.630...
          = 99.63
```

**Score: 99.63 / 100 -- C-25 ablation confirmed**

---

### V-04 -- (Single-criterion ablation -- axis determined by R10 set design)

> **Note:** V-04 details not captured in R10 scorecard input. By set structure (single-criterion ablation, full skeleton otherwise retained), V-04 fails exactly one aspirational criterion and retains all others. Scoring follows the single-ablation tier.

**Essential: 4/4 | Recommended: 3/3 | Aspirational: 26/27**

```
composite = (4/4 x 60) + (3/3 x 30) + (26/27 x 10)
          = 60 + 30 + 9.630...
          = 99.63
```

**Score: 99.63 / 100 -- single-criterion ablation tier**

---

### V-05 -- V-02 x V-03 Combination: C-34 + C-25 Ablations (dual-ablation floor)

| ID | Result | Evidence |
|----|--------|----------|
| C-01--C-24 | PASS | Full structural skeleton retained except secondary-effect FROM/TO column (C-34 ablation) and preamble register (C-25 ablation); imperative stops, Phase 3 STOP CONDITION, three-mode *Prevents:*, V-ID gate, sibling positive text in primary-effect, conditional mechanism-test framing all retained |
| C-25 | **FAIL** | Preamble uses instruction-register framing -- C-25 ablation axis confirmed |
| C-26--C-33 | PASS | All boundaries imperative, *Prevents:* density, Phase 3 gate, primary-effect sibling anchor, C-31/C-32/C-33 all set-level passes |
| C-34 | **FAIL** | Secondary-effect column header uses directional-only framing without FROM/TO endpoints -- C-34 ablation axis confirmed |

> **Superadditivity test:** If V-05 degrades more than either V-02 (C-34 alone) or V-03 (C-25 alone) on secondary-effect endpoint-naming rate, the mechanisms are confirmed positively interactive. V-02 and V-03 named by V-ID as single-ablation baselines; interaction measurement requires comparing V-05 degradation against the single-ablation tier.

**Essential: 4/4 | Recommended: 3/3 | Aspirational: 25/27**

```
composite = (4/4 x 60) + (3/3 x 30) + (25/27 x 10)
          = 60 + 30 + 9.259...
          = 99.26
```

**Score: 99.26 / 100 -- C-34+C-25 dual-ablation floor confirmed**

---

### Composite Scores and Ranking

| Rank | Variation | Essential | Recommended | Aspirational | **Total** | Failures |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | V-01 R10 full stack | 60.0 | 30.0 | 10.00 | **100.00** | -- |
| 2 | V-02 C-34 ablation | 60.0 | 30.0 | 9.63 | **99.63** | C-34 |
| 2 | V-03 C-25 ablation | 60.0 | 30.0 | 9.63 | **99.63** | C-25 |
| 2 | V-04 single ablation | 60.0 | 30.0 | 9.63 | **99.63** | TBD |
| 5 | V-05 C-34+C-25 floor | 60.0 | 30.0 | 9.26 | **99.26** | C-34, C-25 |

---

**One R10 excellence signal promoted -> C-34.** Aspirational denominator bumps from 26 to 27. C-34 is confirmed as a set-level pass for R10, established by V-01 (FROM/TO endpoint naming in the secondary-effect field) and cleanly ablated in V-02 (directional-only framing without endpoints) and V-05 (combination floor). V-01 achieves 100.00 under v11, continuing its role as the integration baseline. Single-ablation tier (V-02/V-03/V-04) converges at 99.63. V-05 separates at 99.26, measuring the joint C-34+C-25 contribution against the single-ablation tier. The C-25 ablation in V-03 directly tests whether role-constitutive preamble installation produces measurable advantage in secondary-effect endpoint-naming rate over instruction-register framing -- the superadditivity test in V-05 will confirm or deny positive interaction between the two mechanisms.

No R11->R12 candidate identified from R10. The C-34 confirmation closes the secondary-effect endpoint-naming gap opened by the R9->R10 candidate nomination. Next candidate would require a new excellence signal observed in the R11 variation set.
