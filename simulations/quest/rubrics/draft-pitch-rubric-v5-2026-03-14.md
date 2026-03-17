**R4 excellence signals identified:**

- **V-01**: C-17 passes via an embedded **definitional negative example** — the skill names the prohibited form ("A restatement of Core Belief in negative form does not pass") and shows a concrete prohibited instance. C-17's pass condition requires failure modes to not be restatements; V-01 structurally enforces this by embedding the exclusion criterion directly in the step instruction.

- **V-02**: C-18 passes with a CTA template whose placeholder **names its static source within the placeholder syntax**: `[active X inertia from SIGNAL DEFAULTS]`. The source is traceable from the template text alone, without reading the rest of the skill.

- **V-03**: C-18 passes with a CTA template whose placeholder **names a dynamic gate output** as source: `[inertia argument from AUDIENCE BELIEF MAP]`. Unlike V-02's DEFAULTS reference (always available), this creates a visible execution dependency — the CTA step cannot be completed without the upstream gate having run.

---

# Rubric: draft-pitch — v5

**Change from v4**: Added C-19, C-20, C-21 from R4 excellence signals. Aspirational denominator updated from 11 to 14.

---

## Essential Criteria (60% weight)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | All three versions present | coverage | Three labeled sections: exec, dev, maker. All non-empty. |
| C-02 | Each version has all four elements | coverage | Hook, What, Why, CTA present in all three versions (12 elements total). |
| C-03 | Exec version is outcome-first with ROI framing | correctness | Business outcome (cost, risk, productivity) before any feature or technology mention. |
| C-04 | Anti-positioning section present | coverage | Explicit "what we are NOT" section ruling out at least one adjacent category. Absence = hard fail. |

---

## Recommended Criteria (30% weight)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | Dev version shows the tool, not the business case | depth | Concrete interaction — command, artifact, or workflow step. Reader can answer "what would I actually type?" |
| C-06 | Maker version is jargon-free | depth | No unexplained acronyms, namespace names, or internal terminology. |
| C-07 | Prior signals consulted | behavior | Pitch reflects framing from available scout/positioning signals. Waived if none exist. |

---

## Aspirational Criteria (10% weight)

**From R1 excellence signals (C-08 – C-12):**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | Proof points are specific and traceable | depth | At least two proof points cite a named source or artifact path. Vague claims fail. |
| C-09 | Competitive framing names inertia as primary competitor | depth | "Doing nothing" / "the meeting that never happened" is named as the real competition. |
| C-10 | Exec self-check is embedded at generation time | process | Skill instructs the model to write the exec opening, test it against C-03, and rewrite *before* continuing. A post-draft checklist does not pass. |
| C-11 | Positioning answers are locked in writing before prose begins | process | Strategy questions (primary competitor, ruling-out statement, signal framing) produce explicit written outputs before any version is drafted. An ambient preamble does not pass. |
| C-12 | Default fallback values provided for missing signals | resilience | Skill supplies explicit defaults per signal-dependent field so C-09 passes unconditionally even with no prior scout artifacts. |

**From R2 excellence signals (C-13 – C-15):**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-13 | DEFAULTS TABLE loaded unconditionally before any intake step | resilience | A defaults table (or equivalent block) appears at the top of the skill, before any signal intake or branching logic, with an explicit statement that defaults apply to all runs and are overridden by signal values when available. Conditional loading inside an intake branch does not pass. |
| C-14 | Gate output is named and cited by downstream instruction | process | The output of a critical gate step (exec self-check, positioning lock, or equivalent) is assigned a named identifier that a later instruction references by that exact name. Skipping the gate step produces a broken downstream reference, not just an ignored suggestion. A narrative write-test-rewrite instruction without a named output does not pass. |
| C-15 | Audience belief mapping precedes argument construction | depth | Before drafting any pitch version, the skill elicits — in writing — what each audience must believe first (e.g., "what must the exec believe before the argument lands?"). Pitch content follows from these written belief anchors, not from structural slot-filling. An implicit or ambient audience framing does not pass. |

**From R3 excellence signals (C-16 – C-18):**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-16 | Multi-node named dependency chain across gate outputs | process | Three or more named gate outputs form a forward-reference chain: each output is assigned a name at creation and cited by that exact name in at least one later step. A single named gate output with one downstream citation does not pass. The chain must be readable from skill structure alone — not traceable only through execution. |
| C-17 | Belief mapping includes per-audience failure modes | depth | The audience belief mapping step includes, for each audience, an explicit failure mode: what the pitch fails to achieve if that belief anchor is not established. A beliefs-only mapping does not pass. A failure mode that restates the belief (e.g., "if exec doesn't believe X, they won't believe X") does not pass. |
| C-18 | Per-audience inertia fields in DEFAULTS with structural CTA template | resilience | SIGNAL DEFAULTS contains a distinct inertia argument for each pitch audience (exec, dev, maker). The CTA construction instruction requires addressing the audience-specific inertia argument via an explicit structural template (e.g., "Instead of [inertia argument], [action]"). A single shared inertia field does not pass. A narrative suggestion to "address inertia" without a per-audience field and structural template does not pass. |

**New — from R4 excellence signals:**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-19 | Definitional instruction includes embedded named negative example | process | When a step defines a required output form that has a common prohibited variant, the skill includes both a definition of the required form AND a named, concrete example of the prohibited form with an explicit statement that the prohibited form does not pass. A column header or pass-condition statement without an embedded prohibited example does not pass. The negative example must be specific enough to exclude the most common wrong answer (e.g., showing a belief-restatement failure mode and naming it as such). |
| C-20 | Structural template placeholder names its source artifact within placeholder syntax | depth | At least one structural template (e.g., CTA construction template) contains a placeholder that names its source artifact or field within the placeholder text itself — e.g., `[inertia argument from AUDIENCE BELIEF MAP]` rather than `[inertia argument]`. The named source must be a named output or named section that appears elsewhere in the skill. A placeholder with no source citation does not pass. A placeholder that cites a generic category (e.g., `[your value prop]`) without naming a specific prior artifact does not pass. |
| C-21 | Structural template placeholder cites a dynamic gate output, creating visible execution dependency | process | At least one structural template's placeholder names a dynamic gate output — a named artifact produced by a prior gate step, not a static defaults block — as its source, using the exact name assigned in that step. This creates a visible execution dependency: the output construction step cannot be completed without the prior gate step's output. A template that sources exclusively from DEFAULTS (a static block) does not pass. A template placeholder that references a gate output by a different name than the step assigns does not pass. |

---

## Composite Score Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 10)
```

**Golden threshold**: All 4 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Platinum | 100 | All essential + recommended + aspirational pass |
