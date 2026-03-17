Done. The v9 rubric is at `simulations/quest/rubrics/draft-pitch-rubric-v9-2026-03-14.md`.

---

## What was added: C-38 – C-40

Three new aspirational criteria extracted from the R8 V-05 excellence signals. Aspirational denominator moves from **30 → 33**.

| ID | Pattern | What it captures beyond C-28–C-37 |
|----|---------|-----------------------------------|
| **C-38** | Phase-level envelopment | C-28–C-37 test whether individual elements are present. C-38 tests whether all three (INERTIA PROFILE + Maker-first + DIFFERENTIATION GATE) are present *and* their sequential pre/fill/close relationship is made explicit, forming a coherent envelope. Having any two of three fails. |
| **C-39** | Pre-committed anchor preserves order integrity | C-36 tests that Maker-first is declared with rationale. C-39 tests that an output from an *earlier phase* is explicitly pre-committed (locked) before the draft phase, so the constrained order cannot be accused of weakening the exec version. Without a named anchor, the order claim is structurally undefended. |
| **C-40** | Gate converts advisory → structural stops | C-34/C-35 test the mechanism (YES/NO + rewrite loop). C-40 tests the origin of the gate's constraints — they must be pre-existing advisory instructions elsewhere in the skill that the gate promotes to pass/fail exits, not new constraints introduced only at the gate. A gate that invents constraints fails; a gate that enforces pre-stated ones passes. |

The scoring formula updates to `(aspirational_pass/33)*10`.
ndition |
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
| C-23 | Formal BINDING DECLARATION at top of consuming phase | process | A formal binding declaration (table or equivalent structured block) appears at the top of the phase that consumes SIGNAL DEFAULTS values into a gate output, before any column definitions or fill instructions. The declaration explicitly maps each DEFAULTS field to its destination gate-output column. Data flow from DEFAULTS into the gate output must be auditable from the declaration alone without reading column definitions in sequence. An absorption note embedded inside a column definition paragraph does not pass. |
| C-24 | Inline provenance declaration at each gate-output citation | depth | At least one placeholder that cites a dynamic gate output embeds provenance within the placeholder syntax itself — naming the origin phase, confirming the output type as a gate output, and confirming lock-before-execution at the cite site (e.g., `[Field from GATE OUTPUT NAME [Phase N gate output, locked before Phase M begins], audience row]`). A placeholder that cites a gate output by name only, without embedded provenance, does not pass. Provenance declared only at the *Produces* statement and not repeated at cite sites does not pass. |

**From R6 excellence signals (C-25 – C-27):**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-25 | Binding declaration includes exhaustiveness scope closure | process | The BINDING DECLARATION contains an explicit statement that no DEFAULTS fields outside the declared binding set are bound to the gate output — e.g., "No other DEFAULTS fields are directly bound to BELIEF MAP columns." This closes the binding scope and prevents implicit hidden bindings. A binding table that lists the declared mappings without an explicit statement that the list is exhaustive does not pass. |
| C-26 | Binding declaration includes explicit downstream access prohibition | process | The BINDING DECLARATION includes an explicit prohibition statement naming the downstream consuming step and the forbidden access pattern — e.g., "Phase 5 CTA construction reads from AUDIENCE BELIEF MAP, not from SIGNAL DEFAULTS directly" or "Phase 5 does not read SIGNAL DEFAULTS inertia fields directly." Stating only the correct access path (what the downstream step should read) without explicitly naming and prohibiting the bypass path does not pass. |
| C-27 | Binding declaration includes meta-purpose statement naming auditability | process | The BINDING DECLARATION contains an explicit statement that the declaration's purpose is to make the DEFAULTS→gate-output data flow auditable from skill structure alone — e.g., "This declaration makes the full DEFAULTS→BELIEF MAP data flow auditable from skill structure alone." A binding table that achieves auditability without stating it as intent does not pass. |

**From R7/R8 excellence signals (C-28 – C-37):**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-28 | INERTIA PROFILE pre-step present at top of draft phase | process | A named INERTIA PROFILE block appears as the first step of the draft phase, before any version-drafting instruction. Absence = fail. An inline note inside a drafting instruction does not pass. |
| C-29 | INERTIA PROFILE cites prior gate output as provenance | process | The INERTIA PROFILE instruction explicitly names the gate output (e.g., AUDIENCE BELIEF MAP) as its source. A free-form inertia step with no named source does not pass. |
| C-30 | INERTIA PROFILE includes gate stop | process | The INERTIA PROFILE block contains an explicit gate-stop instruction preventing advancement to version drafting until the profile is complete. An advisory note to "complete before continuing" does not pass. |
| C-31 | Why-It-Matters instructed to reflect INERTIA PROFILE arc | process | The Why-It-Matters fill instruction for each version explicitly references the INERTIA PROFILE as the source for the arc (not SIGNAL DEFAULTS directly). An instruction that cites SIGNAL DEFAULTS fields or omits provenance does not pass. |
| C-32 | VERSION DIFFERENTIATION GATE present as named post-step | process | A named DIFFERENTIATION GATE (or equivalent named post-step) appears at the end of the draft phase, after all versions are drafted. Absence = fail. An unmarked checklist does not pass. |
| C-33 | Gate uses structured per-version table | process | The gate contains a structured table with one row per draft version and named columns covering content differentiation. A prose checklist without a table does not pass. |
| C-34 | Gate questions use YES/NO format with declared passing state | process | Each gate question is formulated as a YES/NO question and the passing answer for each question is declared explicitly (e.g., "Passing state: Q1=YES, Q2=NO"). A question without a declared passing answer does not pass. |
| C-35 | Gate includes rewrite-until-pass loop instruction | process | The gate contains an explicit instruction to rewrite the failing version, re-fill the table, and re-answer all questions until passing state is reached. An advisory note to "revise if needed" does not pass. |
| C-36 | Constraint-ascending draft order declared (Maker-first) | process | The draft order is explicitly declared as Maker→Dev→Exec (or equivalent constraint-ascending order), with a stated rationale that plain-language coherence is established before specialized framing is added. An undeclared default order or a declaration without rationale does not pass. |
| C-37 | Position labels present on version headers | process | Each version header carries an explicit position label (e.g., "draft first", "draft second", "draft last") that makes the constraint-ascending order auditable from skill text without execution inspection. Version headers without position labels do not pass. |

**From R8 excellence signals (C-38 – C-40):**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-38 | Phase-level envelopment: named pre-step + constrained fill order + named post-step form a coherent pre-commit/fill/close structure | process | The draft phase contains all three envelope elements — a named pre-step (e.g., INERTIA PROFILE), a declared constraint-ascending fill order (e.g., Maker-first), and a named post-step gate (e.g., DIFFERENTIATION GATE) — AND their sequential relationship is explicit in skill structure, making the phase auditable as a unit from structure alone. Presence of any one or two elements without the third does not pass. Presence of all three without an explicit statement of their sequential relationship does not pass. The envelope pattern must mirror the pre-commit/fill/close structure established for earlier phases — not be a novel arrangement. |
| C-39 | Pre-committed anchor preserves constrained-order integrity | process | When a constraint-ascending draft order is declared, at least one output from an earlier phase is explicitly pre-committed (locked before the draft phase begins) so that the constrained order cannot weaken that pre-committed output. The pre-committed output must be identified by name, and the skill must explicitly state that the earlier lock prevents the draft order from affecting that output. A constraint-ascending order declaration without a named pre-committed anchor does not pass. A pre-committed anchor that is not named or whose relationship to draft-order integrity is not stated does not pass. |
| C-40 | Gate converts pre-existing advisory constraints into structural stops | process | The gate's YES/NO questions correspond to quality constraints that already appear as advisory instructions elsewhere in the skill (e.g., "zero unexplained acronyms", "show the tool not the business case"). The gate does not introduce new constraints; it converts pre-existing advisory instructions into pass/fail phase exits. A gate whose questions introduce constraints with no prior advisory counterpart in the skill does not pass. A gate that restates advisory instructions without converting them to binary pass/fail form does not pass. |

---

### Scoring Formula

```
Score = (essential_pass/4)*60 + (recommended_pass/3)*30 + (aspirational_pass/33)*10
```

Aspirational denominator: **33** (C-08 – C-40)
