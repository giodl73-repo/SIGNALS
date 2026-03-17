Looking at the R3 scorecard, I'll extract three distinct excellence patterns not yet captured, then write the full v4 rubric.

**R3 excellence signals identified:**

- **V-01**: Three-node dependency chain (BELIEF MAP → POSITIONING LOCK → EXEC OPENING SENTENCE), each named and cited by exact name downstream. C-14 passes with one named gate; the chain is a structurally stronger form.
- **V-02**: BELIEF TABLE adds a "Failure Mode" column — what the pitch fails to achieve per audience if the belief anchor isn't established. C-15 requires belief anchors but not failure modes.
- **V-03**: Per-audience inertia fields in SIGNAL DEFAULTS (Exec/Dev/Maker) plus a structural CTA template (`Instead of [inertia argument], [action]`). C-09 names inertia as primary competitor; this extends it to audience-specific addressal via enforced structure.

---

# Rubric: draft-pitch — v4

**Change from v3**: Added C-16, C-17, C-18 from R3 excellence signals. Aspirational denominator updated from 8 to 11.

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

**New — from R3 excellence signals:**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-16 | Multi-node named dependency chain across gate outputs | process | Three or more named gate outputs form a forward-reference chain: each output is assigned a name at creation and cited by that exact name in at least one later step. A single named gate output with one downstream citation does not pass. The chain must be readable from skill structure alone — not traceable only through execution. |
| C-17 | Belief mapping includes per-audience failure modes | depth | The audience belief mapping step includes, for each audience, an explicit failure mode: what the pitch fails to achieve if that belief anchor is not established. A beliefs-only mapping does not pass. A failure mode that restates the belief (e.g., "if exec doesn't believe X, they won't believe X") does not pass. |
| C-18 | Per-audience inertia fields in DEFAULTS with structural CTA template | resilience | SIGNAL DEFAULTS contains a distinct inertia argument for each pitch audience (exec, dev, maker). The CTA construction instruction requires addressing the audience-specific inertia argument via an explicit structural template (e.g., "Instead of [inertia argument], [action]"). A single shared inertia field does not pass. A narrative suggestion to "address inertia" without a per-audience field and structural template does not pass. |

---

## Composite Score Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 10)
```

**Golden threshold**: All 4 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Platinum | 100 | All essential + recommended + aspirational pass |
| Golden | 80–99 | All essential pass, composite >= 80 |
| Silver | 60–79 | All essential pass, composite < 80 |
| Fail | < 60 or any essential fail | Not ready |

---

**Key design notes:**

- **C-10/C-11/C-12** are *process/resilience* criteria — they score skill design, not output content. A skill that produces correct output by luck (ambient context, strong model inference) does not pass. The distinction: enforcement vs. suggestion.
- **C-13** tightens C-12: a conditional defaults branch inside intake can still be bypassed by a misread intake step. Unconditional top-of-skill loading cannot. C-12 and C-13 can both pass (full-coverage unconditional table) or C-12 can pass while C-13 fails (conditional coverage).
- **C-14** tightens C-10/C-11: naming the gate output creates a mechanical dependency via forward reference. A narrative instruction is easier to elide than a broken reference. These three criteria represent a progression from suggestion → instruction → structural dependency.
- **C-15** is the first criterion targeting *persuasion quality* rather than structural compliance. All other aspirational criteria are enforceable by inspection of skill structure. C-15 requires the skill to root content in reader psychology before argument assembly — a qualitatively different design move.
- **C-16** extends C-14 from a single gate to a dependency graph. One named output with one citation establishes the pattern; three named outputs each with downstream citations make the chain non-bypassable — skipping any node breaks multiple later references simultaneously.
- **C-17** extends C-15 from belief anchors to belief consequences. Knowing what an audience must believe is the entry condition; knowing what breaks if they don't is the design constraint that shapes pitch construction. The two columns are causally related but not interchangeable.
- **C-18** closes the loop between C-09 (inertia named as competitor) and C-12/C-13 (defaults coverage). Naming inertia once as the primary competitor is a framing move. Supplying per-audience inertia arguments in DEFAULTS and enforcing structural addressal in every CTA is a construction move — it makes C-09 load-bearing across all three pitch versions, not just the positioning statement.
