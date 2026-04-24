Looking at the R5 scorecard, three structural patterns emerge across the variations that are above what C-19–C-21 already capture:

1. **V-02 / V-04**: Both CTA placeholders cite AUDIENCE BELIEF MAP — no parallel DEFAULTS sourcing in the template. DEFAULTS values are absorbed into the gate output before CTA construction, making the gate output the single authoritative downstream source.

2. **V-04**: Explicit binding declaration at the top of Phase 2 — lists which DEFAULTS fields map to which BELIEF MAP columns. Data flow is auditable from skill structure alone without tracing execution.

3. **V-05**: Inline provenance declaration at each gate-output citation — names origin phase, output type, and confirms lock-before-execution at the cite site, not just at the *Produces* declaration.

These become C-22, C-23, C-24. Denominator moves from 14 to 17.

---

# Rubric: draft-pitch — v6

**Change from v5**: Added C-22, C-23, C-24 from R5 excellence signals. Aspirational denominator updated from 14 to 17.

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

**From R4 excellence signals (C-19 – C-21):**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-19 | Definitional instruction includes embedded named negative example | process | When a step defines a required output form that has a common prohibited variant, the skill includes both a definition of the required form AND a named, concrete example of the prohibited form with an explicit statement that the prohibited form does not pass. A column header or pass-condition statement without an embedded prohibited example does not pass. The negative example must be specific enough to exclude the most common wrong answer (e.g., showing a belief-restatement failure mode and naming it as such). |
| C-20 | Structural template placeholder names its source artifact within placeholder syntax | depth | At least one structural template (e.g., CTA construction template) contains a placeholder that names its source artifact or field within the placeholder text itself — e.g., `[inertia argument from AUDIENCE BELIEF MAP]` rather than `[inertia argument]`. The named source must be a named output or named section that appears elsewhere in the skill. A placeholder with no source citation does not pass. A placeholder that cites a generic category (e.g., `[your value prop]`) without naming a specific prior artifact does not pass. |
| C-21 | Structural template placeholder cites a dynamic gate output, creating visible execution dependency | process | At least one structural template's placeholder names a dynamic gate output — a named artifact produced by a prior gate step, not a static defaults block — as its source, using the exact name assigned in that step. This creates a visible execution dependency: the output construction step cannot be completed without the prior gate step's output. A template that sources exclusively from DEFAULTS (a static block) does not pass. A template placeholder that references a gate output by a different name than the step assigns does not pass. |

**From R5 excellence signals (C-22 – C-24):**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-22 | All structural template placeholders cite the same dynamic gate output | process | Every placeholder in a structural template (e.g., CTA) cites the same dynamic gate output — no placeholder in that template cites a static defaults block directly. DEFAULTS values must be absorbed into the gate output before the template's step runs, making the gate output the single authoritative source for all slots. A template where some placeholders cite SIGNAL DEFAULTS and others cite a gate output does not pass. A template where all placeholders cite SIGNAL DEFAULTS does not pass. |
| C-23 | Explicit DEFAULTS-to-gate-output binding declaration at gate step | process | The gate step that absorbs SIGNAL DEFAULTS values into its output (e.g., AUDIENCE BELIEF MAP) includes an explicit binding declaration — a statement identifying which DEFAULTS fields are copied or bound into which output columns. The binding must be readable from skill structure alone without inferring it from column names or downstream usage. An implicit binding (inferable only because a BELIEF MAP column name resembles a DEFAULTS field name) does not pass. A binding declared in a downstream step rather than at the gate step does not pass. |
| C-24 | Inline provenance declaration at each dynamic gate output citation | process | Each instruction that cites a dynamic gate output by name includes an inline parenthetical or annotation identifying the output's origin phase and confirming it is locked before the citing step runs — e.g., `(gate output from Phase 2, locked before Phase 5 begins)`. A bare name citation without an inline provenance declaration does not pass. A provenance declaration that appears only at the *Produces* location and not at the cite site does not pass. |

---

## Composite Score Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 17 * 10)
```

| Tier | Threshold |
|------|-----------|
| Platinum | ≥ 95 |
| Gold | ≥ 85 |
| Silver | ≥ 70 |
| Bronze | ≥ 55 |
| Fail | < 55 or any Essential fail |

---

## Retrograde Scores (v6 baseline)

| Round | Best variation | v5 score | v6 score | Delta | Gap criterion |
|-------|---------------|----------|----------|-------|---------------|
| R4 | V-05 | 100 | 98.24 | −1.76 | C-22 (CTA sources from DEFAULTS + BELIEF MAP in parallel), C-23 (no explicit binding declaration), C-24 (no inline provenance at cite site) |
| R5 | V-04, V-05 | 100 | — | — | V-04: passes C-22, C-23; fails C-24. V-05: fails C-22 (first CTA placeholder cites DEFAULTS directly); passes C-24 via traceability declaration. No single R5 variation passes all three. |
