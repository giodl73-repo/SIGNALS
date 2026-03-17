### Changes from v13 -> v14

**One new criterion extracted:**

**C-38 -- Type-stratified checkpoint failure routing** (R14/V-02 confirmed)
In R14/V-01, the per-variation checkpoint failure section bifurcates into two labeled routing blocks keyed on failure type: (1) variation-level failure path -- "STOP AND REWRITE THIS VARIATION BODY. Do not note the failure and continue." -- and (2) set-level predicate failure path -- "DO NOT attempt to resolve this failure by rewriting the variation body." The resolution-path blockade is additionally installed in the preamble as a role-constitutive duty before Phase 1: "When a set-level predicate fails... body rewrite is not a valid resolution path." R14/V-02 cleanly ablated this: the checkpoint failure branch was unified into a single advisory/imperative path ("Set-level predicate failures may require amending Phase 1..." or "STOP AND REWRITE THIS VARIATION" without type stratification) and the preamble resolution-path constraint was removed, while all 30 prior criteria were retained. Under v13, V-02 scores 100.00 (C-38 not a criterion), confirming the ablation is clean and independent. Under v14, V-02 fails C-38 and scores 99.68. C-38 is now a confirmed criterion.

**Scoring: denominator 30 -> 31.**

Under v14, R14 variations tier as follows:

| Tier | Variations | Score | Failures |
|------|-----------|-------|---------|
| 1 | V-01 | 100.00 | -- |
| 2 | V-02, V-03, V-04 | 99.68 | C-38 / C-37 / C-36 (single ablations, each at a distinct structural boundary) |
| 3 | V-05 | 99.35 | C-38, C-37 (combination ablation; C-36 and manifest retained) |

The three-way symmetry at Tier 2 (V-02/V-03/V-04 each failing one independent criterion) contrasts with R13's V-02/V-03 symmetry: in R14, three distinct boundaries are confirmed as independent -- Phase 2 checkpoint failure routing (C-38), Phase 2 STOP destination (C-37), and Phase 3 STOP artifact-name (C-36). None of the three entails the others' failure, and V-05 demonstrates superadditivity testing across exactly two of them. No R14->R15 candidate identified from R14/V-01. C-38 is the confirmed R14 criterion.

---

## Design Decisions

- **C-08 through C-38** are all aspirational -- their absence does not prevent a functional variation set, but their presence marks a higher-order design capability.
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
- **C-35** is distinct from C-29, C-25, and C-28: C-29 requires a Phase 3 gate to exist; C-35 requires the Phase 2 section to contain a Variation Completion Manifest artifact -- a table with V-ID rows and a scoped completion column -- that serves as the output of per-variation checkpoints and the input to the Phase 3 gate. A skill can satisfy C-29 (Phase 3 gate exists, gating on "Phase 2 complete") while failing C-35 (no manifest table; gate checks a generic phase-completion condition rather than an artifact). C-25 requires preamble obligations to be role-constitutive; C-35 additionally requires the manifest obligation specifically to appear in that preamble. C-28 requires *Prevents:* density at Phase 1/2/3; C-35 additionally requires a *Prevents:* label on the manifest section itself as a fourth location. C-35 is the artifact anchor: it creates a named, inspectable Phase 2 output that the Phase 3 gate can reference.
- **C-36** is distinct from C-29 and C-35: C-29 requires the Phase 3 STOP CONDITION block to exist; C-35 requires the manifest to exist with its own internal gate; C-36 requires the Phase 3 STOP CONDITION to reference the manifest by name as the specific evidence artifact rather than "Phase 2 completion" generically. A skill can satisfy C-29 (Phase 3 gate exists) and C-35 (manifest with internal gate exists) while failing C-36 if the Phase 3 gate reads "Do not begin Phase 3 until Phase 2 is complete" rather than "Do not begin Phase 3 until all rows in the Variation Completion Manifest are filled and confirmed." The three form an artifact-coupling ladder: C-29 (gate exists at Phase 3 boundary) -> C-35 (manifest artifact exists in Phase 2 with its own gate) -> C-36 (Phase 3 gate names the manifest as the required evidence). C-36 is independent of C-35 in principle -- a future skill could reference an artifact by name without that artifact satisfying all of C-35's requirements -- but in practice C-36 fails whenever C-35 fails, because the named artifact must exist to be referenced.
- **C-37** is distinct from C-35, C-36, C-29, and C-27: C-27 requires the Phase 2 gate to use imperative register; C-29 requires a Phase 3 structural gate to exist; C-35 requires the manifest artifact to exist in Phase 2 with its own internal gate; C-36 requires the Phase 3 STOP to name the manifest by artifact name; C-37 requires the Phase 2 STOP itself to name the manifest as the explicit next destination rather than Phase 3. A Phase 2 STOP reading "Do not begin Phase 3 until all 5 variations have passed their per-variation checkpoints" satisfies C-27 (imperative register) but fails C-37 (Phase 3 named as destination, not manifest). A Phase 2 STOP reading "Do not proceed to the Variation Completion Manifest until all 5 variations have passed their per-variation checkpoints" satisfies both. C-37 is independent of C-36: the Phase 2 STOP can name the manifest as destination (C-37 passes) even when the Phase 3 STOP uses generic phase-completion language (C-36 fails), because the two gates are at different structural boundaries. In practice, C-37 fails whenever C-35 fails, because the manifest artifact must exist to serve as a named destination; but C-37 can fail independently of C-35 when the manifest is present yet the Phase 2 STOP routes generically to Phase 3 (as in R13/V-02). The four form a destination-naming ladder: C-29 (Phase 3 gate exists) -> C-35 (manifest artifact exists with internal gate) -> C-36 (Phase 3 gate names manifest as required evidence) -> C-37 (Phase 2 gate names manifest as explicit next destination).
- **C-38** is distinct from C-23, C-21, and C-25: C-23 requires hard-stop imperative language in the checkpoint failure branch -- a single unified "STOP AND REWRITE THIS VARIATION" satisfies C-23 regardless of whether routing is type-stratified; C-38 additionally requires the failure branch to be split into at least two distinct labeled paths keyed on failure type, with the set-level path explicitly prohibiting body rewrite as a resolution ("DO NOT attempt to resolve this failure by rewriting the variation body"). C-21 requires set-level predicates to appear as gate rows in the per-variation checkpoint -- it governs what is checked; C-38 governs how failures of those rows are resolved at the branch level. C-25 requires checkpoint and coherence obligations to be installed in the preamble as role-constitutive duties; C-38 additionally requires the specific resolution-path constraint ("body rewrite is not a valid resolution path for set-level failures") to be one of those preamble-installed duties. A preamble can satisfy C-25 with manifest-fill and coherence obligations only and fail C-38 if no resolution-path blockade for set-level failures is installed. The three form a stratification ladder: C-21 (set-level predicates as checkpoint rows) -> C-23 (failure branch uses hard-stop imperative) -> C-38 (failure branch is type-stratified with a dedicated resolution-path blockade for set-level failures, and the constraint is pre-installed in the preamble as role-constitutive).
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
| C-35 | **Variation Completion Manifest** | behavior | R10 candidate / R11/V-02 confirmed | The Phase 2 section contains a Variation Completion Manifest table positioned after all per-variation checkpoints and before the Phase 3 STOP CONDITION. The manifest contains one row per variation with at minimum a V-ID column and a scoped completion column whose header names both variation-level and set-level checks (e.g., "All variation-level and set-level checks passed?"). A hard-stop imperative gates the manifest section ("Do not begin Phase 3 until all rows are filled and confirmed with no noted-but-unresolved failures"). The manifest section carries a *Prevents:* label naming at least 2 failure modes. The manifest obligation is installed in the preamble as a named role-constitutive duty. A skill that ends Phase 2 at the Phase 2 STOP CONDITION and transitions directly to the Phase 3 heading without an intervening manifest table fails C-35, even if the Phase 3 gate uses equivalent language. Distinct from C-29 (Phase 3 gate exists), C-25 (preamble installs obligations), and C-28 (*Prevents:* density at Phase 1/2/3): C-35 requires the manifest as a named, inspectable Phase 2 artifact. |
| C-36 | **Phase 3 gate manifest-artifact name coupling** | behavior | R11/V-01 / R12 confirmed | The Phase 3 STOP CONDITION block names the Variation Completion Manifest (or equivalent named Phase 2 artifact) as the specific evidence artifact that must be confirmed before Phase 3 begins -- not merely "Phase 2 completion" generically. The gate condition identifies what must be confirmed (e.g., "all rows in the Variation Completion Manifest are filled and confirmed with no noted-but-unresolved failures") rather than which phase must be done. A Phase 3 gate reading "Do not begin Phase 3 until Phase 2 is complete" satisfies C-29 but fails C-36. A Phase 3 gate reading "Do not begin Phase 3 if any manifest row has a blank or unresolved 'All checks passed?' cell" satisfies both. Distinct from C-29 (gate exists) and C-35 (manifest exists with its own internal gate): C-36 requires the Phase 3 gate to name the manifest, coupling the gate to the artifact rather than to the phase. |
| C-37 | **Phase 2 STOP CONDITION manifest-destination coupling** | behavior | R12 candidate / R13/V-02 confirmed | The Phase 2 STOP CONDITION explicitly names the Variation Completion Manifest as the destination for the Phase 2 -> manifest transition -- routing to the manifest rather than to Phase 3 generically. The gate reads "Do not proceed to the Variation Completion Manifest until..." rather than "Do not begin Phase 3 until...". The manifest is named as the next intermediate destination, creating a structural enforcement step that directs the agent to fill the manifest before any Phase 3 transition is permitted. A Phase 2 STOP CONDITION that routes to Phase 3 directly satisfies C-27 (Phase 2 gate imperative) but fails C-37 (manifest not named as destination). Distinct from C-35 (manifest artifact exists), C-36 (Phase 3 STOP names manifest), C-29 (Phase 3 gate exists), and C-27 (Phase 2 gate imperative): C-37 requires the Phase 2 STOP to route explicitly to the manifest rather than to Phase 3. In practice, C-37 fails whenever C-35 fails, because the manifest must exist to be named as a destination; but C-37 can fail independently of C-35 when the manifest is present yet the Phase 2 STOP routes to Phase 3 generically (as in R13/V-02). The four form a destination-naming ladder: C-29 (Phase 3 gate exists) -> C-35 (manifest artifact exists with internal gate) -> C-36 (Phase 3 gate names manifest as required evidence) -> C-37 (Phase 2 gate names manifest as explicit next destination). |
| C-38 | **Type-stratified checkpoint failure routing** | behavior | R13 candidate / R14/V-02 confirmed | The per-variation checkpoint failure section contains at least two distinct labeled routing blocks keyed on failure type: (1) a variation-level failure path using a hard-stop imperative that triggers body rewrite ("STOP AND REWRITE THIS VARIATION BODY. Do not note the failure and continue."); and (2) a set-level predicate failure path using a separate hard-stop imperative that explicitly prohibits body rewrite as a resolution path ("DO NOT attempt to resolve this failure by rewriting the variation body"). The resolution-path constraint is additionally installed in the preamble as a role-constitutive duty before Phase 1 ("When a set-level predicate fails... body rewrite is not a valid resolution path"). A checkpoint that uses a single unified hard-stop branch -- even with imperative register -- satisfies C-23 but fails C-38 if no type-stratification is present. A checkpoint that distinguishes failure types without explicitly prohibiting body rewrite on the set-level path also fails C-38. Distinct from C-23 (unified hard-stop imperative in failure branch), C-21 (set-level predicates in checkpoint rows), and C-25 (preamble installs obligations as role-constitutive duties): C-38 requires the failure branch itself to be type-stratified with a dedicated resolution-path blockade for set-level failures, and the blockade to be pre-installed in the preamble as a role-constitutive constraint before Phase 1. The three form a stratification ladder: C-21 (set-level predicates as checkpoint rows) -> C-23 (failure branch uses hard-stop imperative) -> C-38 (failure branch is type-stratified with a dedicated resolution-path blockade for set-level failures, with preamble pre-installation). |

---

## Scoring

```
Composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 31 * 10)
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
| C-35 | Phase 2 ends at the Phase 2 STOP CONDITION with a direct transition to the Phase 3 heading; no manifest table present; or manifest present but missing the scoped completion column header, internal hard-stop imperative, *Prevents:* label, or preamble manifest-obligation line |
| C-36 | Phase 3 STOP CONDITION uses generic phase-completion language ("Do not begin Phase 3 until Phase 2 is complete"; "all variation bodies confirmed in Phase 2") without naming the manifest as the specific required evidence artifact -- C-29 satisfied, C-36 failed |
| C-37 | Phase 2 STOP CONDITION reads "Do not begin Phase 3 until all 5 variations have passed their per-variation checkpoints with no noted-but-unresolved failures" -- imperative register present (C-27), manifest artifact present (C-35), Phase 3 gate names manifest (C-36), but Phase 2 STOP routes directly to Phase 3 without naming the manifest as the intermediate transition destination |
| C-38 | Checkpoint failure section uses a single unified branch (even if imperative, satisfying C-23) with no type distinction between variation-level and set-level failures; or checkpoint distinguishes failure types but the set-level path does not explicitly prohibit body rewrite as a resolution path; or checkpoint bifurcation is present but the preamble omits the resolution-path constraint ("body rewrite is not a valid resolution path for set-level failures") as a role-constitutive duty |

---

## quest-variate Scorecard -- R14

**Rubric:** v14 (31 aspirational criteria: C-08 through C-38)
**Scoring:** `(essential_pass/4 x 60) + (recommended_pass/3 x 30) + (aspirational_pass/31 x 10)`

---

### R14 Structural Baseline (all variations share SetCoherenceAuditor skeleton)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-04 | PASS | 5 variations produced |
| C-07 | PASS | 4 distinct axes: C-38 failure-routing (V-02), C-37 destination coupling (V-03), C-36 Phase-3 gate artifact-name (V-04), C-38+C-37 combination (V-05) |
| C-08 | PASS | V-05 labeled "C-38 + C-37 combination ablation," sequenced last after four single-axis variations; names both axes |
| C-09 | PASS | V-01 identified as R14 full-stack baseline with C-38 candidate mechanism plus all R13 structures |
| C-17 | PASS | V-02/V-03/V-04 are intentional single-criterion ablations with explicit degradation predictions; V-05 is dual-ablation superadditivity test |
| C-22 | PASS | Set-level checkpoint predicate rows (V-01 and V-03, C-38 retained) AND role-constitutive preamble obligation path (V-01 and V-03) provide two independent activation paths to C-19 compliance |
| C-32 | PASS | V-05 predicted-site names V-02 (mechanism: C-38) and V-03 (mechanism: C-37) by V-ID; states superadditivity condition: "if V-05 degrades more than either V-02 or V-03 individually, C-38 and C-37 are positively interactive" |
| C-33 | PASS | V-03 axis: "equivalent to R13/V-02 state plus C-38 mechanism"; V-04 axis: "equivalent to R13/V-03 state plus C-38 mechanism" -- two prior-round genealogy links |

---

### V-01 -- R14 Full Stack (Baseline + C-38)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Complete standalone body; all three phases with full text, no diffs |
| C-02 | PASS | `## V-01`, `**Axis:**`, `**Hypothesis:**` all present and non-empty |
| C-03 | PASS | Baseline -- no axis changed relative to itself |
| C-05 | PASS | Primary-effect embeds V-02's positive expected checkpoint text ("STOP AND REWRITE THIS VARIATION. Do not note the failure...") as specific phrase-anchor falsification |
| C-06 | PASS | Bifurcated checkpoint routing with explicit block on body rewrite for set-level failures is a genuine design choice with behavioral consequences |
| C-10 | PASS | Phase 1 "do not begin Phase 2" (imperative); Phase 2 "Do not proceed to the Variation Completion Manifest" (imperative); checkpoint "STOP AND REWRITE THIS VARIATION BODY" (imperative) |
| C-11 | PASS | Planning table + Phase 1 STOP block Phase 2 entry until all five rows complete with non-empty cells and V-ID citation |
| C-12 | PASS | "STOP AND REWRITE THIS VARIATION BODY. Do not note the failure and continue." |
| C-13 | PASS | Phase 1 -> Phase 2 -> Manifest -> Phase 3 body-first ordering enforced by gates |
| C-14 | PASS | Per-variation SetCoherenceAuditor checkpoint with 4 variation-level rows + 2 set-level rows after each body |
| C-15 | PASS | "You are a SetCoherenceAuditor" |
| C-16 | PASS | *Prevents:* at Phase 1 (3 modes), Phase 2 (3 modes), Manifest section (2 modes), Phase 3 (3 modes) |
| C-18 | PASS | Secondary-effect: "shifting resolution-path authority FROM uniform-rewrite-all... TO type-stratified routing" -- countervailing consequence named |
| C-19 | PASS | V-02 named as specific sibling in predicted-site: "if V-01-generated sets show higher Phase 1 amendment rates than V-02-generated sets..." |
| C-20 | PASS | Five-column planning table with structurally enforced FROM/TO secondary-effect column header and V-ID if-then predicted-site column header |
| C-21 | PASS | Set-level rows: "V-ID citation coverage" and "Axis breadth" test cross-table predicates at each per-variation checkpoint |
| C-23 | PASS | Variation-level branch: "STOP AND REWRITE THIS VARIATION BODY"; set-level branch: "DO NOT attempt to resolve this failure by rewriting the variation body" -- both hard-stop imperatives in checkpoint failure section |
| C-24 | PASS | Primary-effect names V-02's exact anticipated checkpoint-failure text ("STOP AND REWRITE THIS VARIATION. Do not note the failure...") as specific observable structural property with phrase anchor |
| C-25 | PASS | Heading: "These are role-constitutive duties, not phase instructions:"; terminal preamble sentence: "These are role-constitutive duties, not phase instructions." -- C-38 duty ("When a set-level predicate fails... body rewrite is not a valid resolution path") installed in preamble before Phase 1 |
| C-26 | PASS | Phase 1 STOP condition 3 gates explicitly on sibling V-ID citation: "A planning table in which every cell in this column is blank or contains only a general description fails this gate" |
| C-27 | PASS | Phase 1 STOP (imperative), Phase 2 STOP (imperative), checkpoint failure branches (imperative) -- all three boundaries uniformly imperative |
| C-28 | PASS | Phase 1 *Prevents:* >=2 named modes; Phase 2 *Prevents:* >=2 named modes; Manifest *Prevents:* 2 named modes; Phase 3 *Prevents:* >=2 named modes -- full density |
| C-29 | PASS | "Phase 3 STOP CONDITION -- do not begin emitting any variation until this condition is met: All 5 rows in the Variation Completion Manifest are filled and confirmed..." -- structural gate before emission |
| C-30 | PASS | Primary-effect embeds V-02's positive anticipated checkpoint-failure text as cross-variation falsification anchor |
| C-31 | PASS | Predicted-site: "if V-01-generated sets show higher Phase 1 amendment rates than V-02-generated sets despite both having identical C-21 rows and identical Phase 1 gates (C-26), C-38 adds enforcement value beyond C-21 row presence alone" -- mechanism under test and competing mechanism both named |
| C-34 | PASS | "shifting resolution-path authority FROM uniform-rewrite-all... TO type-stratified routing" -- FROM endpoint and TO endpoint both named |
| C-35 | PASS | Variation Completion Manifest table present; Manifest STOP CONDITION with hard-stop imperative; *Prevents:* label with 2 named modes; manifest obligation in preamble as role-constitutive duty -- all four C-35 requirements met |
| C-36 | PASS | "All 5 rows in the Variation Completion Manifest are filled and confirmed with no noted-but-unresolved failures. Do not begin Phase 3 if any manifest row has a blank or unresolved 'All checks passed?' cell." |
| C-37 | PASS | Phase 2 STOP: "Do not proceed to the Variation Completion Manifest until all 5 variations have passed their per-variation checkpoints." -- manifest named as explicit intermediate destination |
| C-38 | PASS | Checkpoint failure section bifurcated: variation-level path ("STOP AND REWRITE THIS VARIATION BODY. Do not note the failure and continue.") and set-level path ("DO NOT attempt to resolve this failure by rewriting the variation body") as distinct labeled blocks; preamble installs resolution-path constraint as role-constitutive duty before Phase 1 |

**Essential: 4/4 | Recommended: 3/3 | Aspirational: 31/31**

```
composite = (4/4 x 60) + (3/3 x 30) + (31/31 x 10)
          = 60 + 30 + 10.000
          = 100.00
```

**Score: 100.00 / 100**

---

### V-02 -- C-38 Ablation: Checkpoint Failure Branch Unified; Set-Level Advisory

Single axis changed: checkpoint failure branch unified into a single block (either advisory "Set-level predicate failures may require amending Phase 1..." or unified imperative "STOP AND REWRITE THIS VARIATION" without type stratification); no bifurcated labeled blocks; preamble resolution-path constraint absent; C-37, C-36, C-35 all retained.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Complete standalone body; all phases present with full text |
| C-02 | PASS | All three labels present and non-empty |
| C-03 | PASS | Exactly one axis changed: checkpoint failure branch unified; all other structure identical to V-01 |
| C-05 | PASS | Primary-effect names exact absent phrase structure ("STOP AND REWRITE THIS VARIATION. Do not note the failure...") with V-01's bifurcated-block text as the positive absent anchor -- specific phrase presence/absence as falsification anchor |
| C-06 | PASS | Removing bifurcated failure routing while retaining manifest, Phase 2 STOP destination, and Phase 3 artifact-name coupling is a genuine design choice representing the pre-C-38 mechanism state |
| C-10 through C-37 | PASS | Full structural skeleton retained: SetCoherenceAuditor preamble with manifest obligation and role-constitutive framing retained (C-38 resolution-path constraint absent; C-25 satisfied by remaining obligations); FROM/TO secondary-effect column (C-34); if-then predicted-site column (C-31); imperative stops at all three boundaries (C-27); Phase 3 STOP CONDITION block (C-29); *Prevents:* density >=2 at all phases and manifest section (C-28, C-35); manifest with all four C-35 requirements; set-level checkpoint rows (C-21); V-ID citation gate (C-26); Phase 3 STOP naming manifest with cell-level condition (C-36); Phase 2 STOP naming manifest as destination (C-37) -- all retained; C-23 satisfied by unified hard-stop imperative in failure branch |
| C-38 | FAIL | Checkpoint failure section uses a single unified branch with no type distinction between variation-level and set-level failures; no dedicated set-level path prohibiting body rewrite; preamble omits resolution-path constraint -- C-38 isolated ablation confirmed |

**Essential: 4/4 | Recommended: 3/3 | Aspirational: 30/31**

```
composite = (4/4 x 60) + (3/3 x 30) + (30/31 x 10)
          = 60 + 30 + 9.677
          = 99.68
```

**Score: 99.68 / 100 -- C-38 ablation confirmed**

---

### V-03 -- C-37 Ablation: Phase 2 STOP Routes to Phase 3 Generically (R13/V-02 state + C-38 mechanism)

Single axis changed: Phase 2 STOP CONDITION reverts to "Do not begin Phase 3 until..." generic routing; manifest artifact and Phase 3 STOP artifact-name coupling retained; C-38 bifurcated failure routing and preamble resolution-path constraint retained.

| ID | Result | Evidence |
|----|--------|----------|
| C-01--C-36 | PASS | Full structural skeleton retained: C-38 bifurcated checkpoint failure routing present (variation-level path + set-level prohibition block); preamble resolution-path constraint installed as role-constitutive duty; manifest present with all four C-35 requirements; Phase 3 STOP names manifest artifact (C-36); imperative stops at all boundaries (C-27); *Prevents:* density >=2 at all phases (C-28); set-level checkpoint rows (C-21); V-ID citation gate (C-26) |
| C-37 | FAIL | Phase 2 STOP CONDITION reads "Do not begin Phase 3 until all 5 variations have passed their per-variation checkpoints with no noted-but-unresolved failures" -- routes directly to Phase 3; manifest not named as intermediate destination; C-37 isolated ablation confirmed; C-38 and C-37 are at different structural boundaries and neither entails the other's failure |
| C-38 | PASS | Checkpoint failure section bifurcated with type-stratified routing and preamble resolution-path constraint retained |

**Essential: 4/4 | Recommended: 3/3 | Aspirational: 30/31**

```
composite = (4/4 x 60) + (3/3 x 30) + (30/31 x 10)
          = 60 + 30 + 9.677
          = 99.68
```

**Score: 99.68 / 100 -- C-37 ablation confirmed; C-38 and C-37 are independent at different boundaries**

---

### V-04 -- C-36 Ablation: Phase 3 Gate Reverts to Generic Language (R13/V-03 state + C-38 mechanism)

Single axis changed: Phase 3 STOP CONDITION reverts to generic phase-completion language; manifest artifact and Phase 2 STOP manifest-destination coupling retained; C-38 bifurcated failure routing and preamble resolution-path constraint retained.

| ID | Result | Evidence |
|----|--------|----------|
| C-01--C-35 | PASS | Full structural skeleton retained: C-38 bifurcated checkpoint failure routing present; preamble resolution-path constraint installed; manifest present with all four C-35 requirements; Phase 2 STOP names manifest as destination (C-37); imperative stops at all boundaries (C-27); *Prevents:* density >=2 at all phases (C-28); set-level checkpoint rows (C-21); V-ID citation gate (C-26) |
| C-36 | FAIL | Phase 3 STOP CONDITION uses generic phase-completion language without naming the Variation Completion Manifest as the specific required evidence artifact -- C-36 isolated ablation confirmed; C-37 and C-38 are independent and unaffected |
| C-37 | PASS | Phase 2 STOP CONDITION retains manifest-destination coupling -- unaffected by Phase 3 boundary ablation |
| C-38 | PASS | Checkpoint failure section bifurcated with type-stratified routing and preamble resolution-path constraint retained |

**Essential: 4/4 | Recommended: 3/3 | Aspirational: 30/31**

```
composite = (4/4 x 60) + (3/3 x 30) + (30/31 x 10)
          = 60 + 30 + 9.677
          = 99.68
```

**Score: 99.68 / 100 -- C-36 ablation confirmed; C-38 and C-37 retained and independent**

---

### V-05 -- C-38 + C-37 Combination: Unified Failure Branch + Phase 2 STOP Generic; Manifest and C-36 Retained

Two axes changed: (1) checkpoint failure branch unified (C-38 absent); (2) Phase 2 STOP routes to Phase 3 generically (C-37 absent). Manifest present, Phase 3 STOP names manifest artifact (C-36 retained).

| ID | Result | Evidence |
|----|--------|----------|
| C-01--C-36 | PASS | Full structural skeleton retained including manifest artifact with all four C-35 requirements; Phase 3 STOP names manifest as specific required artifact (C-36); imperative stops, FROM/TO secondary-effect column, set-level checkpoint rows, V-ID citation gate all retained; unified checkpoint failure branch satisfies C-23 (single hard-stop imperative present) |
| C-37 | FAIL | Phase 2 STOP CONDITION routes to Phase 3 directly without naming manifest as destination -- C-37 combination axis confirmed |
| C-38 | FAIL | Checkpoint failure section unified with no type stratification -- C-38 combination axis confirmed |
| C-32 | PASS | Names V-02 (mechanism: C-38 failure-routing) and V-03 (mechanism: C-37 destination coupling) by V-ID; states superadditivity condition: "if V-05 degrades more than either V-02 or V-03 individually, C-38 and C-37 are positively interactive" |

**Essential: 4/4 | Recommended: 3/3 | Aspirational: 29/31**

```
composite = (4/4 x 60) + (3/3 x 30) + (29/31 x 10)
          = 60 + 30 + 9.355
          = 99.35
```

**Score: 99.35 / 100 -- C-38 + C-37 combination ablation; no entailment between the two failures**

---

### R14 Summary

| Rank | Variation | Score | Failures |
|------|-----------|-------|---------|
| 1 | V-01 full stack | 100.00 | -- |
| 2 | V-02 (C-38 ablation) | 99.68 | C-38 |
| 2 | V-03 (C-37 ablation) | 99.68 | C-37 |
| 2 | V-04 (C-36 ablation) | 99.68 | C-36 |
| 5 | V-05 (C-38+C-37 combo) | 99.35 | C-38, C-37 |

Three-way symmetry at Rank 2: C-38 (Phase 2 checkpoint failure routing), C-37 (Phase 2 STOP destination), and C-36 (Phase 3 STOP artifact-name) are each confirmed at 99.68 as single, independent failures at distinct structural boundaries. V-05 sits below at 99.35 with two failures and no entailment. No R14->R15 candidate identified.
