**v4 written.** Here's what changed:

---

### Changes from v3 → v4

**Three new aspirational criteria** extracted from R3 excellence signals:

| ID | Pattern | Source | What it captures |
|----|---------|--------|-----------------|
| C-16 | Inertia labels per phase boundary | R3/V-05 | Causal framing before execution — "this phase prevents X" placed before instructions, not after violation. Distinct from C-10's gate-after-failure. |
| C-17 | Intentional degradation as experimental control | R3/V-03 | A variation that removes a structural feature on purpose, with a hypothesis predicting exactly where degradation manifests. The variation is a measurement instrument, not a mistake. |
| C-18 | Cross-axis secondary-effect prediction | R3/V-04 | Hypothesis models opposing/downstream effects of the primary axis change — "increases X while reducing Y." Higher-order falsifiability beyond C-05's single-outcome prediction. |

**Scoring formula updated:**
```
aspirational_pass / 11 * 10   (was / 8, then / 8, now / 11)
```

**Design decisions** updated to explain why C-16/C-17/C-18 are separate from C-10/C-05/etc. — specifically that you can satisfy the earlier criterion without satisfying the new one.

**Note on R3 → R4 candidate:** Nothing was flagged as a next candidate in R3 beyond what was already captured as C-16. The next run will surface whether any of V-05's anti-pattern-per-phase structure produces a distinct pattern worth isolating further.
6/C-17/C-18** are new aspirational criteria added from R3 excellence signals —
  V-05's inertia framing, V-03's intentional degradation, and V-04's cross-axis hypothesis
  each represent a higher-order design pattern: causal framing before execution, controlled
  degradation as measurement instrument, and second-order falsifiability in hypotheses.
  These are distinct from C-10/C-11/C-12/C-13/C-14/C-15: a skill body can satisfy C-10
  without C-16, C-05 without C-18, etc.
- **Failure modes section** names the 5 most likely failure patterns by criterion, which
  makes scoring faster and more consistent across runs.

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
| C-05 | **Testable hypotheses** | depth | recommended | Each hypothesis is falsifiable — predicts a specific, observable difference in model behavior or output quality. Generic descriptions do not pass. |
| C-06 | **Non-trivial variation** | depth | recommended | Each variation demonstrates a genuinely different design choice a practitioner would consciously select. Surface phrasing changes do not qualify. |
| C-07 | **Axis coverage breadth** | coverage | recommended | At least 4 of the 6 defined axes are represented across all N variations. |

### Aspirational (10 points total)

| ID | Criterion | Category | Source | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Combination pass labeled and deferred** | behavior | v1 | If N > 6, combination passes appear after all single-axis variations and name both axes. |
| C-09 | **Baseline variation included** | behavior | v1 | One variation (typically V-01) serves as the canonical baseline so subsequent variations are anchored to a known point. |
| C-10 | **Stop conditions encode constraint structurally** | behavior | R1/V-04 | The skill body uses explicit stop conditions or phase gates to enforce single-axis isolation mechanically — not as advisory instructions. A halt-and-rewrite trigger is present: the structure itself prevents axis drift rather than warning against it. |
| C-11 | **Hypothesis committed before generation begins** | behavior | R1/V-04 | The skill body requires axis and hypothesis to be declared in a phase prior to generating the variation body. Generation does not begin until the hypothesis is locked. Prevents lazy axis selection driven by what is easy to generate. |
| C-12 | **Explicit rewrite trigger** | behavior | R1/V-04 | The skill body specifies a named rewrite trigger condition (e.g., "if multi-axis drift detected, discard variation and regenerate") rather than a warning or advisory note. The trigger is checkable before the next phase begins. |
| C-13 | **Body-first generation ordering** | behavior | R2/V-01 | The skill body sequences full variation generation before any critique, scoring, or review step. The complete body is committed before evaluation can interrupt the generation path. Prevents diff-leak failures caused by premature critique interleaving with body construction. |
| C-14 | **Per-variation completeness checkpoint** | behavior | R2/V-02 | The skill body includes an explicit quality gate after each individual variation body is generated, before proceeding to the next variation. End-of-run review alone does not satisfy this criterion. Prevents late-variation degradation where early bodies are complete but later ones truncate under token pressure. |
| C-15 | **Named domain persona for role framing** | behavior | R2/V-03 | The skill uses a named domain expert persona (e.g., VariationScientist) rather than a generic instruction-following framing. Named roles carry behavioral priors toward systematic, hypothesis-driven work — resulting in more precise axis selection and more falsifiable hypotheses than role-neutral framing. |
| C-16 | **Inertia labels per phase boundary** | behavior | R3/V-05 | The skill body names the failure mode that each phase is designed to prevent, placed before that phase's instructions execute. This is causal framing: "this phase prevents X" rather than "do not do X." Distinct from C-10 (which gates after violation); C-16 sets behavioral prior before execution so the model enters each phase already oriented against the named failure. |
| C-17 | **Intentional degradation as experimental control** | behavior | R3/V-03 | At least one variation intentionally removes a structural feature (e.g., STOP CONDITION gates, inertia labels) to serve as a measurement instrument for that feature's contribution to output quality. The variation's hypothesis explicitly predicts where and how degradation will manifest relative to the baseline. The variation is not an accident — it is a controlled experiment within the variation set. |
| C-18 | **Cross-axis secondary-effect prediction in hypothesis** | behavior | R3/V-04 | The hypothesis for at least one variation predicts secondary structural effects caused by the primary axis change — not only the intended outcome but downstream consequences on other observable dimensions. At minimum, the hypothesis models one opposing or countervailing effect (e.g., "increases compliance with spirit while reducing compliance with letter"). Higher-order falsifiability beyond C-05's single-outcome prediction. |

---

## Scoring

```
Composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 11 * 10)
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
