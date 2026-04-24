Here is the complete updated rubric as Markdown:

---

Written to `simulations/quest/rubrics/quest-variate-rubric-v6-2026-03-14.md`.

---

### Changes from v5 -> v6

Three new criteria extracted from R5 excellence signals:

**C-21 — Set-level predicates in per-variation checkpoint** (R5/V-03)

V-03's 8-criterion rubric includes rows that test *set-level* predicates — properties that apply to the planning table or variation set as a whole (e.g., "Does at least one planning-table row have a named V-ID in the Secondary effect column?"). This creates an incremental enforcement loop: global planning-table coherence is verified from *within* each variation's local gate, not deferred to a final end-of-run review. Distinct from C-14 (which assesses the current variation's body completeness): C-21 requires the checkpoint to also evaluate predicates that span the variation set. A checkpoint can satisfy C-14 without C-21 if every row in the gate tests only the current variation.

**C-22 — Dual independent activation paths to the same aspirational criterion** (R5/V-03+V-05)

The variation set includes at least two variations that independently produce compliance with the same high-order aspirational criterion (e.g., C-19) through mechanically distinct mechanisms — one via a format prompt embedded in Phase 2 (rubric row), one via a role prior established in Phase 1 (persona obligation). The paths are structurally independent: removing one variation does not eliminate the other's activation path. This creates a natural experiment for comparing path effectiveness across runs. Distinct from C-07 (which requires different axes across variations): C-22 requires the same high-order criterion reached by different structural mechanisms, not different axes. A set can satisfy C-07 without C-22 if each axis produces a unique criterion and no criterion is targeted by more than one variation.

**C-23 — Checkpoint imperative register enforces behavioral discontinuity** (R5/V-02)

The per-variation checkpoint uses hard-stop imperative language ("STOP AND REWRITE THIS VARIATION") rather than advisory language ("please verify" / "consider rewriting") in its failure-handling branch. Hard-stop imperatives create behavioral discontinuity — a forced halt before the next variation begins — that prevents the "proceed and note" bypass pattern where a model satisfies surface compliance (all fields non-empty) while silently continuing past a marginal checkpoint failure. Distinct from C-10 (which applies to phase-gate language at phase boundaries) and C-12 (which requires a named rewrite trigger to exist in the skill body): C-23 applies specifically to the failure branch of the *per-variation checkpoint step* (C-14). A skill can satisfy C-12 via a phase-gate trigger and C-14 via a present checkpoint while failing C-23 if the checkpoint's failure-handling language is advisory rather than imperative.

**Scoring:** `aspirational_pass / 16 * 10`

**R5 -> R6 candidate flagged:** V-05's secondary-effect hypothesis predicts that CausalAuditor's cross-variation audit obligation increases Phase 1 hypothesis verbosity, producing a precision tradeoff — "hypotheses name more interaction effects but the primary-effect prediction becomes less sharply constructed." This is the precision/compliance tradeoff first noted as an R4→R5 candidate (from V-05's "formulaic and verbose" prediction in R4). R5 provides the clearest signal yet: V-05's CausalAuditor body demonstrates the pattern in its own hypothesis construction. If R6 variations show measurable primary-effect precision loss in template-compliant hypotheses vs non-template hypotheses, a C-24 distinguishing "structural completeness of hypothesis" (C-20 compliance: all columns filled) from "analytical sharpness of the primary-effect prediction" may be warranted.

- C-21 and C-14 are related but distinct: C-14 requires a per-variation checkpoint to exist; C-21 requires that checkpoint to include at least one row testing a set-level predicate. C-21 is not satisfied by a C-14 checkpoint that only tests the current variation's body.
- C-22 can co-occur with C-19: a set that satisfies C-22 around C-19 necessarily satisfies C-19. But C-19 can be satisfied by a single variation (V-03) without C-22 if no second independent activation path exists.
- C-23 and C-12 are related but non-overlapping: C-12 requires a named rewrite trigger in the skill body; C-23 requires that the *per-variation checkpoint's failure branch* uses hard-stop imperative register. A skill can satisfy C-12 through a phase-gate trigger without placing imperative language in the checkpoint step, thus satisfying C-12 without C-23.

**Note on R5 -> R6 candidate:** V-05's CausalAuditor body demonstrates the precision/compliance tradeoff in its own hypothesis: the secondary-effect field is longer and more interaction-laden than V-01's, while the primary-effect prediction is correspondingly less sharply bounded. If R6 provides cross-variation evidence — template-compliant hypotheses averaging lower primary-effect specificity than non-template hypotheses — a criterion separating "all hypothesis fields structurally present" (C-20) from "primary-effect field analytically precise" (C-24) may be warranted.

---

## Design Decisions

- **C-08 through C-23** are all aspirational -- their absence does not prevent a functional variation set, but their presence marks a higher-order design capability.
- **C-16/C-17/C-18** are distinct from C-10/C-11/C-12/C-13/C-14/C-15: a skill body can satisfy C-10 without C-16, C-05 without C-18, etc.
- **C-19** is distinct from C-18: C-18 requires that at least one variation's hypothesis model a countervailing secondary effect. C-19 requires that hypothesis to identify *which other specific variations* will exhibit that effect. Cross-variation falsifiability is a strictly stronger claim than within-variation secondary prediction.
- **C-20** is distinct from C-16: C-16 operates at phase level (inertia labels before each phase's instructions). C-20 operates at hypothesis-field level (a template with named columns that force multi-part structure). A skill with strong C-16 framing will improve hypothesis quality on average; only C-20 makes multi-part hypothesis structure mandatory through format.
- **C-21** is distinct from C-14: C-14 requires a per-variation quality gate to exist; C-21 requires that gate to include at least one row that tests a set-level predicate (a property of the planning table or variation set as a whole, not the current variation's body). A strong C-14 checkpoint that only verifies the current body does not satisfy C-21.
- **C-22** is distinct from C-07: C-07 requires different axes represented across variations; C-22 requires the same high-order aspirational criterion activated by structurally independent mechanisms in at least two variations. The distinction is axis diversity (C-07) vs mechanism diversity toward a shared criterion (C-22).
- **C-23** is distinct from C-12: C-12 requires a named rewrite trigger in the skill body; C-23 requires that the *per-variation checkpoint's failure branch* uses hard-stop imperative register. A skill can satisfy C-12 via a phase-gate trigger (e.g., in Phase 1 or Phase 2 stop conditions) without placing imperative language in the checkpoint step, thus satisfying C-12 without C-23.
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
| C-21 | **Set-level predicates in per-variation checkpoint** | behavior | R5/V-03 | The per-variation quality gate (C-14) includes at least one row or check that tests a set-level predicate -- a property that spans the planning table or variation set as a whole (e.g., "Does at least one planning-table row have a named sibling V-ID in the Secondary effect column?"). This enforces global planning-table coherence incrementally from within each variation's local gate, rather than deferring cross-variation verification to a final end-of-run review. Distinct from C-14: C-14 requires the gate to exist; C-21 requires the gate to include set-level predicates alongside local body checks. A checkpoint that only verifies the current variation's body completeness satisfies C-14 but not C-21. |
| C-22 | **Dual independent activation paths to the same aspirational criterion** | behavior | R5/V-03+V-05 | The variation set includes at least two variations that independently produce compliance with the same high-order aspirational criterion (e.g., C-19) through mechanically distinct mechanisms -- one via a format prompt in Phase 2 (e.g., rubric row), one via a role prior established in Phase 1 (e.g., persona obligation). The paths are structurally independent: removing one variation does not eliminate the other's activation path. This creates a natural experiment for comparing path effectiveness across runs, and provides a redundancy guarantee that the criterion survives partial variation failure. Distinct from C-07 (which requires different axes): C-22 requires the same high-order criterion reached by different structural mechanisms. A set can satisfy C-07 without C-22 if no criterion is independently targeted by more than one activation path. |
| C-23 | **Checkpoint imperative register enforces behavioral discontinuity** | behavior | R5/V-02 | The per-variation checkpoint uses hard-stop imperative language (e.g., "STOP AND REWRITE THIS VARIATION") in its failure-handling branch, rather than advisory language (e.g., "please verify", "consider rewriting"). Hard-stop imperatives create behavioral discontinuity -- a forced halt before the next variation begins -- that prevents the "proceed and note" bypass pattern where a model fills all fields while silently continuing past a marginal checkpoint failure. Distinct from C-10 (which applies to phase-gate language at phase boundaries) and C-12 (which requires a named rewrite trigger to exist anywhere in the skill body): C-23 applies specifically to the failure branch of the per-variation checkpoint step (C-14). A skill can satisfy C-12 via a phase-gate trigger and C-14 via a present checkpoint while failing C-23 if the checkpoint's failure branch uses advisory rather than imperative register. |

---

## Scoring

```
Composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10)
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
| C-21 | Checkpoint has multiple rows but all rows test only the current variation's body (completeness, axis isolation, hypothesis present) -- no row tests a set-level predicate across the planning table |
| C-22 | Only one variation targets a given high-order criterion (e.g., C-19 achieved via rubric row only); no second independent activation path present in the set |
| C-23 | Checkpoint includes a rewrite instruction but phrases it as advisory ("if any row fails, consider rewriting before proceeding") rather than imperative ("STOP AND REWRITE THIS VARIATION") |

---

**Three R5 excellence signals promoted → C-21, C-22, C-23.** Aspirational denominator bumps from 13 to 16. The R5 perfect-but-for-V-01 result (85/100) would score 88.75/100 under v6 if the same run also activated all three new criteria — which V-03/V-05 collectively do. The V-05 precision/compliance tradeoff carries forward as R6→R7 candidate (C-24).
