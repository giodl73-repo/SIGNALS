Here is the complete v4 rubric:

---

# /quest:rubric — validate-inertia — v4

**Skill:** `validate-inertia` | **Version:** v4 | **Date:** 2026-03-17

---

## Essential Criteria (60 pts total)

*Each essential criterion is worth 12 pts.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Named personas, role-grounded resistance** | correctness | essential | Output names at least 2-3 personas, each with a role and a role-grounded reason why they would resist adoption. Generic statements not tied to a specific persona fail. |
| C-02 | **Switching cost quantified** | correctness | essential | At least one switching cost expressed in concrete units: time, money, effort, or risk. Vague language does not pass. |
| C-03 | **Kill barrier named** | correctness | essential | Output explicitly names the single barrier most likely to block adoption entirely, labeled as such. Must be specific to this feature, not a generic observation. |
| C-04 | **Workaround satisfaction assessed** | correctness | essential | Output evaluates how well the current workaround already solves the problem for at least one persona, including why it feels "good enough." |
| C-05 | **Per-persona inertia score present** | format | essential | Each persona receives a discrete inertia score on a consistent scale. All scores use the same scale and appear in the output. |

---

## Recommended Criteria (30 pts total)

*Each recommended criterion is worth 10 pts.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Habit lock-in addressed** | depth | recommended | Identifies a behavioral/habitual pattern that would cause the persona to revert even after initial adoption. Must be persona-specific. |
| C-07 | **Social proof requirement mapped** | depth | recommended | Identifies what social proof threshold a skeptical persona needs before adopting -- specific names, numbers, or evidence type. |
| C-08 | **Learning curve quantified** | depth | recommended | At least one persona's learning curve expressed in concrete terms: ramp time, concept count, or comparison anchor. |

---

## Aspirational Criteria (10 pts total)

*All 10 criteria are 1 pt each. Point weights flattened in v4 to accommodate C-16/C-17/C-18 while keeping total at 10 pts.*

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Overall risk rating with mitigation** | depth | Synthesizes per-persona scores into an overall risk level AND proposes one specific mitigation targeting C-03's kill barrier. Restating the barrier does not pass. | 1 pt |
| C-10 | **Inertia asymmetry identified** | correctness | Distinguishes structural inertia (product changes required) vs. behavioral (can be overcome with onboarding), and calls out permanent lost TAM vs. delayed adoption. | 1 pt |
| C-11 | **Kill barrier hypothesized before persona analysis** | structure | Kill barrier stated as an explicit hypothesis in the first section, before any persona analysis begins. Feature-specific; not derived from persona aggregation. | 1 pt |
| C-12 | **Status-quo treated as competitor** | depth | Reasons about why at least one persona *chose* the incumbent -- "they adopted X because...", "X won this persona because..." Describes the adoption decision, not merely current state. | 1 pt |
| C-13 | **Inertia landscape classified before persona analysis** | structure | A dedicated pre-persona phase classifies the overall landscape as Structural/Behavioral/Mixed, states the type and its implication, and gates the analysis on the result. | 1 pt |
| C-14 | **Type-conditioned mitigation** | depth | C-09 mitigation explicitly branches on type: "if structural: name the product change / if behavioral: name the launch sequence." Unconditional mitigations do not pass. | 1 pt |
| C-15 | **Lost TAM implication stated unconditionally** | correctness | A non-conditional statement -- labeled "Lost TAM implication" or equivalent -- names permanent lost TAM vs. delayed adoption. Sections gated on "if evidence supports it" do not pass. | 1 pt |
| C-16 | **Mitigation contract written before persona analysis** | structure | The classification phase writes an explicit "Required mitigation form:" contract specifying the exact form Phase 4 mitigation must take, conditioned on the classified type. Phase 4 fulfills the contract rather than re-deriving. The model reads its own prior output; generic drift requires contradicting it. Classification without the contract, or contract written after persona analysis, does not pass. | 1 pt |
| C-17 | **Required unconditional fields isolated in standalone phases** | structure | Any field that must appear regardless of evidence confidence gets its own dedicated phase, section header, required-presence instruction ("required regardless of evidence confidence"), and anchoring vocabulary. Fields sharing a phase with conditional if/then analysis do not pass -- proximity to conditional language causes drift that only phase-boundary isolation prevents. | 1 pt |
| C-18 | **Procedural gate with self-affirmation token** | structure | At least one critical pre-analysis classification is framed as a blocking prerequisite ("Do not proceed until you have classified X") and the output includes a self-affirmation token ("Gate passed. Proceeding.") that makes the classification a confirmed output artifact. Section headers that can be passively read without producing a traceable token do not pass. | 1 pt |

---

## Reviewer Notes (additions for v4)

- **C-16** is the strongest implementation of C-14: the contract in Phase 2 makes the required mitigation form readable in the model's own prior output, eliminating re-derivation. Passing C-16 without C-13 is structurally impossible.
- **C-17** is the strongest implementation of C-15: phase isolation removes conditional drift risk entirely. An output can pass C-15 (unconditional label present) but fail C-17 (label embedded in a conditional synthesis section).
- **C-18** is the strongest implementation of C-13: the self-affirmation token makes the classification a confirmed output artifact. An output can pass C-13 (dedicated phase present) but fail C-18 (no blocking instruction, no token in output).
- C-16/C-17/C-18 are structurally independent and can all pass simultaneously. Each closes a different failure mode: generic mitigation drift (C-16), conditional field drift (C-17), silent phase skip (C-18).

---

Written to `simulations/quest/rubrics/validate-inertia-rubric-v4-2026-03-17.md`.

**What changed:**

| ID | Source | Pattern |
|----|--------|---------|
| C-16 | V-02 R3 | Mitigation contract written in Phase 2 -- "Required mitigation form: [if Structural: ...] [if Behavioral: ...]". Phase 4 fulfills the contract; model reads its own prior output rather than re-deriving type at synthesis time. Generic drift requires contradicting a prior output, not just ignoring an instruction. |
| C-17 | V-03 R3 | Phase 5 "LOST TAM IMPLICATION" as a standalone section with its own header + required-presence instruction + anchoring vocabulary. Proximity to if/then language in shared synthesis sections causes conditional drift; phase boundaries are the structural prevention. |
| C-18 | V-04 R3 | "Do not proceed until you have classified inertia type." → "Gate passed. Proceeding." The self-affirmation token appears in output as a confirmed prerequisite, not a passively-read header. Structural gating becomes traceable. |

**Point redistribution:** All 10 aspirational criteria (C-09 through C-18) are 1 pt each. Prior v3 weighting {C-09=2, C-10=2, C-13=2} flattened to make room. Total aspirational tier unchanged at 10 pts.
"Use 'permanent lost TAM' and 'delayed adoption' as anchoring terms"). Fields that share a phase with conditional if/then analysis do not pass even if labeled "required" -- phase-boundary isolation is the structural requirement, because proximity to surrounding conditional language causes conditional drift. | 1 pt |
| C-18 | **Procedural gate with self-affirmation token** | structure | aspirational | At least one critical pre-analysis classification (e.g., the inertia landscape classification) is framed as a blocking prerequisite: "Do not proceed to [next phase] until you have [completed X]." The output includes a self-affirmation token -- e.g., "Gate passed. Proceeding." -- that appears as a confirmed prerequisite in model output, making the classification a traceable artifact rather than a passively-read section header. Outputs where the classification instruction is readable but produces no confirmation token in output do not pass. | 1 pt |

---

## Scoring Reference

| Score Range | Interpretation |
|-------------|----------------|
| 100 | All criteria pass -- exemplary output |
| 80-99 | Golden threshold met -- output is useful and publishable |
| 60-79 | Essential pass but recommended gaps -- usable, needs improvement |
| < 60 | One or more essential criteria fail -- output is not useful |

---

## Reviewer Notes

- C-01 and C-03 are the two criteria most commonly failed by shallow outputs. If both fail, the output is a generic risk list, not an inertia analysis.
- C-02 passes if at least one cost is quantified; not all costs need numbers.
- C-05 fails if personas receive narrative assessments with no discrete score -- the score is the primary artifact.
- C-09 mitigation must target the kill barrier named in C-03; restating the barrier as a recommendation does not pass.
- C-10 is strictly aspirational: structural vs. behavioral inertia is a sophisticated distinction that requires domain knowledge about the persona's org context.
- C-11 is achievable only when the output is structured as a two-phase analysis (barrier hypothesis -> persona analysis). Single-phase outputs that derive the kill barrier at the end fail this criterion even if C-03 passes.
- C-12 is strengthened by competitor framing at the prompt level (e.g., "treat the current workaround as a competitor"). Outputs that merely describe what a persona uses without reasoning about the adoption decision do not pass.
- C-13 is achievable only when the output has a dedicated pre-persona phase (e.g., "Inertia Landscape" or "Phase 2: Classification") that names the type and its structural implication. Outputs that classify inertia type inline with persona analysis or in a closing synthesis fail this criterion.
- C-14 requires the mitigation to branch explicitly on inertia type. "If structural... / If behavioral..." is the target form. Anti-patterns lists and unconditional interventions do not pass.
- C-15 fails if the Lost TAM statement is conditional. The statement must appear regardless of what the analysis found -- its content varies, but its presence must not.
- C-13 and C-14 are complementary: C-13 places the classification before the personas; C-14 propagates that classification into the mitigation. An output can pass C-13 without passing C-14 (classifies early but collapses to unconditional mitigation), but passing C-14 without C-13 is structurally unusual.
- C-16 is the strongest implementation of C-14: rather than instructing the model to branch on type at synthesis time, the contract in Phase 2 makes the required form readable in the model's own prior output. Passing C-16 without C-13 is structurally impossible -- the contract can only be written in the pre-persona classification phase.
- C-17 is the strongest implementation of C-15: phase isolation removes the conditional drift risk entirely. An output can pass C-15 (unconditional label present) but fail C-17 (label embedded in a conditional synthesis section, creating drift risk under adversarial outputs).
- C-18 is the strongest implementation of C-13: the self-affirmation token makes the classification a confirmed output artifact. An output can pass C-13 (dedicated classification phase present, correctly gated) but fail C-18 (no blocking prerequisite instruction, no token in output).
- C-16, C-17, and C-18 are structurally independent: a four-phase design can pass all three simultaneously. Each addresses a different failure mode -- generic mitigation drift (C-16), conditional field drift (C-17), and silent phase skip (C-18).

---

## Version Notes

**v4 changes (2026-03-17):**
- Added C-16: Mitigation contract written before persona analysis -- extracted from V-02 R3 excellence signal (Phase 2 writes "Required mitigation form: [if Structural: ...] [if Behavioral: ...]" as a binding contract; Phase 4 fulfills it; model reads its own prior output, preventing generic drift structurally rather than by instruction)
- Added C-17: Required unconditional fields isolated in standalone phases -- extracted from V-03 R3 excellence signal (Phase 5 "LOST TAM IMPLICATION" as a dedicated standalone section with its own header, required-presence instruction, and anchoring vocabulary; proximity to surrounding if/then language in shared synthesis sections causes conditional drift that phase-boundary isolation prevents)
- Added C-18: Procedural gate with self-affirmation token -- extracted from V-04 R3 excellence signal ("Do not proceed until you have classified inertia type" -> "Gate passed. Proceeding." makes the classification a confirmed output artifact rather than a passively-read header; self-affirmation token is traceable in model output)
- Redistributed aspirational point weights: all 10 aspirational criteria (C-09 through C-18) are 1 pt each (total aspirational tier unchanged at 10 pts); prior v3 weighting {C-09=2, C-10=2, C-13=2} flattened to accommodate three new criteria without total change

**v3 changes (2026-03-17):**
- Added C-13: Inertia landscape classified before persona analysis -- extracted from V-02 R2 excellence signal (pre-persona Structural/Behavioral/Mixed classification phase transforms C-10 from post-hoc synthesis to deliberate analytical choice; inertia type structurally gates mitigation specificity)
- Added C-14: Type-conditioned mitigation -- extracted from V-02 R2 excellence signal (if-structural/if-behavioral branching is a stronger C-09 guarantee than anti-patterns lists; constrains answer space before writing rather than naming failures after)
- Added C-15: Lost TAM implication stated unconditionally -- extracted from V-02 R2 excellence signal (conditional asymmetry sections reliably produce PARTIAL on C-10 regardless of structural/behavioral vocabulary; non-conditional required statement locks in the framing)
- Redistributed aspirational point weights: C-09=2, C-10=2, C-11=1, C-12=1, C-13=2, C-14=1, C-15=1 (total aspirational tier unchanged at 10 pts)

**v2 changes (2026-03-17):**
- Added C-11: Kill barrier sequenced first -- extracted from V-05 R1 excellence signal (Phase 1 hypothesis before persona analysis produced the strongest C-03 results across all variants)
- Added C-12: Status-quo as competitor -- extracted from V-03 R1 excellence signal (competitor framing produced the strongest C-04 results across all variants, including "why they chose it" reasoning)
- Redistributed aspirational point weights: C-09=3, C-10=3, C-11=2, C-12=2 (total aspirational tier unchanged at 10 pts)
- Completed C-01 pass condition (was truncated in v1)
