Written to `simulations/quest/rubrics/quest-variate-rubric-v5-2026-03-14.md`.

---

### Changes from v4 -> v5

Two new criteria extracted from R4 excellence signals:

**C-19 — Cross-variation causal prediction** (R4/V-03)

The flagged V-03 pattern: the hypothesis names V-04 and V-05 by ID as predicted degradation sites. This is strictly stronger than C-18. C-18 says "predict a secondary effect." C-19 says "predict *which specific sibling variations* will exhibit that effect." A hypothesis can satisfy C-18 by predicting "increases X while reducing Y" without knowing or stating where Y's reduction will show up. C-19 requires the cross-variation localization.

**C-20 — Structural hypothesis template enforcement** (R4/V-05)

V-05's three-part template is the structural analog to C-18, exactly as C-10 is the structural analog to C-03. C-16 (inertia labels) improves hypothesis quality through behavioral framing; it does not make multi-part hypothesis structure mandatory. Only a template with named columns (primary effect / secondary effect / predicted manifestation site) forces C-18 compliance mechanically. Distinct from C-16 by level: phase vs. hypothesis-field.

**Scoring:** `aspirational_pass / 13 * 10`

**R4 -> R5 candidate flagged:** V-05's hypothesis predicts its template will produce "more formulaic and verbose" outputs with reduced analytical precision. If R5 provides evidence of that precision/compliance tradeoff, a C-21 distinguishing structural completeness from analytical quality of hypotheses may be warranted.
tructured template.
- C-19 and C-20 can co-occur: a template (C-20) that includes a "predicted manifestation variation" column produces C-19 naturally, but C-19 can also arise from a practitioner voluntarily cross-referencing variation IDs without any template.

**Note on R4 -> R5 candidate:** V-05's three-part template creates a potential further pattern -- whether template-enforced hypotheses trade analytical precision for structural compliance (the "formulaic and verbose" prediction in V-05's hypothesis). If R5 variations show measurable precision loss from template rigidity, a criterion distinguishing "structural completeness" from "analytical quality" of hypotheses may be warranted.

---

## Design Decisions

- **C-08 through C-20** are all aspirational -- their absence does not prevent a functional variation set, but their presence marks a higher-order design capability.
- **C-16/C-17/C-18** are distinct from C-10/C-11/C-12/C-13/C-14/C-15: a skill body can satisfy C-10 without C-16, C-05 without C-18, etc.
- **C-19** is distinct from C-18: C-18 requires that at least one variation's hypothesis model a countervailing secondary effect. C-19 requires that hypothesis to identify *which other specific variations* will exhibit that effect. Cross-variation falsifiability is a strictly stronger claim than within-variation secondary prediction.
- **C-20** is distinct from C-16: C-16 operates at phase level (inertia labels before each phase's instructions). C-20 operates at hypothesis-field level (a template with named columns that force multi-part structure). A skill with strong C-16 framing will improve hypothesis quality on average; only C-20 makes multi-part hypothesis structure mandatory through format.
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
| C-08 | **Combination pass labeled and deferred** | behavior | v1 | If N > 6, combination passes appear after all single-axis variations and name both axes. |
| C-09 | **Baseline variation included** | behavior | v1 | One variation (typically V-01) serves as the canonical baseline so subsequent variations are anchored to a known point. |
| C-10 | **Stop conditions encode constraint structurally** | behavior | R1/V-04 | The skill body uses explicit stop conditions or phase gates to enforce single-axis isolation mechanically -- not as advisory instructions. A halt-and-rewrite trigger is present: the structure itself prevents axis drift rather than warning against it. |
| C-11 | **Hypothesis committed before generation begins** | behavior | R1/V-04 | The skill body requires axis and hypothesis to be declared in a phase prior to generating the variation body. Generation does not begin until the hypothesis is locked. Prevents lazy axis selection driven by what is easy to generate. |
| C-12 | **Explicit rewrite trigger** | behavior | R1/V-04 | The skill body specifies a named rewrite trigger condition (e.g., "if multi-axis drift detected, discard variation and regenerate") rather than a warning or advisory note. The trigger is checkable before the next phase begins. |
| C-13 | **Body-first generation ordering** | behavior | R2/V-01 | The skill body sequences full variation generation before any critique, scoring, or review step. The complete body is committed before evaluation can interrupt the generation path. Prevents diff-leak failures caused by premature critique interleaving with body construction. |
| C-14 | **Per-variation completeness checkpoint** | behavior | R2/V-02 | The skill body includes an explicit quality gate after each individual variation body is generated, before proceeding to the next variation. End-of-run review alone does not satisfy this criterion. Prevents late-variation degradation where early bodies are complete but later ones truncate under token pressure. |
| C-15 | **Named domain persona for role framing** | behavior | R2/V-03 | The skill uses a named domain expert persona (e.g., VariationScientist) rather than a generic instruction-following framing. Named roles carry behavioral priors toward systematic, hypothesis-driven work -- resulting in more precise axis selection and more falsifiable hypotheses than role-neutral framing. |
| C-16 | **Inertia labels per phase boundary** | behavior | R3/V-05 | The skill body names the failure mode that each phase is designed to prevent, placed before that phase's instructions execute. This is causal framing: "this phase prevents X" rather than "do not do X." Distinct from C-10 (which gates after violation); C-16 sets behavioral prior before execution so the model enters each phase already oriented against the named failure. |
| C-17 | **Intentional degradation as experimental control** | behavior | R3/V-03 | At least one variation intentionally removes a structural feature (e.g., STOP CONDITION gates, inertia labels) to serve as a measurement instrument for that feature's contribution to output quality. The variation's hypothesis explicitly predicts where and how degradation will manifest relative to the baseline. The variation is not an accident -- it is a controlled experiment within the variation set. |
| C-18 | **Cross-axis secondary-effect prediction in hypothesis** | behavior | R3/V-04 | The hypothesis for at least one variation predicts secondary structural effects caused by the primary axis change -- not only the intended outcome but downstream consequences on other observable dimensions. At minimum, the hypothesis models one opposing or countervailing effect (e.g., "increases compliance with spirit while reducing compliance with letter"). Higher-order falsifiability beyond C-05's single-outcome prediction. |
| C-19 | **Cross-variation causal prediction** | behavior | R4/V-03 | The hypothesis for at least one variation identifies specific other variations in the set by ID as the predicted sites where its secondary effects will manifest (e.g., "produces detectable completeness degradation in V-04 and V-05"). Cross-variation falsifiability: the prediction spans the variation set rather than staying within a single variation's scope. Distinct from C-18: C-18 requires a countervailing secondary effect; C-19 requires that effect be localized to named sibling variations. A variation can satisfy C-18 without C-19 if it predicts opposing effects without naming where in the set those effects will appear. |
| C-20 | **Structural hypothesis template enforcement** | behavior | R4/V-05 | The skill body provides a multi-part hypothesis template (e.g., a planning table with named columns for primary-effect prediction, secondary-effect prediction, and predicted manifestation site) that mechanically produces C-18-compliant hypotheses through format constraints rather than instruction or inertia framing. This is to C-18 what C-10 is to C-03: structural prevention rather than advisory instruction. Distinct from C-16: C-16 operates at phase level; C-20 operates at hypothesis-field level. A skill with C-16 inertia labels will improve hypothesis quality on average; only C-20 makes multi-part hypothesis structure mandatory through format. |

---

## Scoring

```
Composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 13 * 10)
```

---

## Failure Modes (by criterion)

| Criterion | Most likely failure |
|-----------|-------------------|
| C-01 | Model emits "same structure as V-01 with X changed" instead of a full body |
| C-03 | Register change silently removes STOP CONDITION labels (co-varying structure + register) |
| C-05 | Hypothesis states intent ("to test whether...") rather than prediction ("will produce...") |
| C-11 | Axis declared inline with body in the same step; hypothesis written after generation |
| C-14 | Single review table at end covers all variations; no per-variation gate present |
| C-18 | Hypothesis lists two positive outcomes rather than a primary effect and a countervailing/opposing consequence |
| C-19 | Secondary effects predicted in general terms without naming which specific variation IDs will exhibit them |
| C-20 | Inertia label instructs "include a secondary-effect prediction" (C-16 approach) but no template column enforces the field structurally |
