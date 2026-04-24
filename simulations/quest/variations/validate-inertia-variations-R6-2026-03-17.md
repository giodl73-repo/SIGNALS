Written to `simulations/quest/variations/validate-inertia-variations-R6-2026-03-17.md`.

---

## validate-inertia Variations R6 -- Summary

| # | Label | Axis | Primary targets |
|---|-------|------|-----------------|
| V-26 | Phase-zero self-identification label | Lifecycle emphasis | C-21 |
| V-27 | Competitive inventory completeness gate | Lifecycle emphasis | C-22 |
| V-28 | Falsifiable anchor in intervention target | Output format | C-23 |
| V-29 | Phase-zero gate + falsifiable anchor | Lifecycle + output format | C-21, C-23 |
| V-30 | Full integration -- all fifteen aspirationals | All axes | C-09--C-23 |

---

### Design rationale

**C-21 diagnosis (V-26 target):** V-25 Phase 1 says "Per-persona traces in Phase 4 must reference these thresholds and dimension weights" -- that's a downstream instruction, not a self-identification statement. C-21 requires the phase to *identify itself as the source* C-17 traces will cite. V-26 adds a required labeled output: `SCORING INFRASTRUCTURE DECLARED.` written on its own line before Phase 2. Without this label, models produce Phase 4 traces that paraphrase dimension weights without explicitly citing Phase 1 -- the pass condition says "cite this phase by reference."

**C-22 diagnosis (V-27 target):** V-25 Phase 2 already has Dimension/Advantage/Durability columns and "Familiarity is not durability." C-22 likely already passes in V-25. V-27 isolates this with a formal completeness gate (three checks, must not advance to Phase 3 until each persona passes all three) to confirm the mechanism and catch the most common failure mode: Durability entries that use habit/familiarity under analytical pressure.

**C-23 diagnosis (V-28 target):** V-25 Phase 5 Part (3) gives good examples of mechanism vs. approach granularity but doesn't require the model to *test* falsifiability before proceeding. A target can read as a mechanism while being too general to anchor C-16. V-28 inserts a required falsifiability test sentence between Part (3) and Part (4): "At T=6mo, the absence of this lever being addressed would be observable as: [specific condition]." If the model can't complete it, Part (3) is rejected.

**V-29 (C-21 + C-23):** These are the two uncertain closures. C-22 is likely incidentally handled by V-25's Phase 2. V-29 combines only the uncertain two, confirming their independence before V-30 adds all three.

**V-30 (all 15):** V-25 base + V-26 + V-27 + V-28. Three additions, three phases (1, 2, 5), no overlap. Expected ceiling: 230/230.
erely reference a prior section), C-23 because falsifiability testing requires the model to
reject a too-general target. V-27 (C-22) is likely already satisfied by V-25's structure;
V-29 isolates the two uncertain closures.

**V-30 (all 15):** V-25 base + all three new mechanisms. Expected ceiling: 230/230 if all
phases execute without degradation. The three new mechanisms occupy distinct phases (Phase 1,
Phase 2, Phase 5) and do not compete.

---

### V-26: Phase-Zero Self-Identification Label

**Axis:** Lifecycle emphasis -- Phase 1 must produce a required labeled statement that
explicitly designates itself as the scoring infrastructure C-17 traces will cite by name
**Hypothesis:** V-25 Phase 1 instructs models to reference thresholds downstream but does
not require the phase to self-identify as the named infrastructure source. Adding a required
labeled output statement -- "SCORING INFRASTRUCTURE DECLARED" -- that models must write
before Phase 2 begins will close C-21 by making the self-identification a structural
production requirement. The label forces the model to name the phase as the C-17 source at
declaration time, not merely imply it.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly? Complete
each phase in sequence. Each phase gates the next.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework that will govern per-persona
scores in Phase 4.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight (one sentence -- reference a property of this feature or user population) |
|-----------|------------------------------|------------------------------------------------------------------------------------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof requirement
/ Learning curve.

**Score thresholds** -- define the dimension-combination rules that produce each tier:

- **Critical:** [state which dimension combinations produce this tier]
- **High:** [state which combinations produce this tier]
- **Medium:** [state which combinations]
- **Low:** [state what condition all dimensions must satisfy]

**Required infrastructure label:** After completing the dimension weights and score thresholds
above, write the following statement on its own line before Phase 2 begins:

> "SCORING INFRASTRUCTURE DECLARED. All per-persona methodology traces in Phase 4 must cite
> this Phase 1 output by reference -- naming the specific dimension weights and tier thresholds
> declared above to show how each persona's score was produced. Phase 4 traces that reference
> dimension values without citing these thresholds, or that cite thresholds without naming
> dimension values, will not satisfy the per-score trace requirement."

Phase 2 cannot begin until this statement is written. The statement is the boundary marker that
closes Phase 1.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named competitor.

**Persona entry:**

- Name and role (specific, not categorical)
- Current solution (named tool or method -- "ad hoc" is not a solution; name what they do)
- Outcome the current solution delivers

**Competitive strength inventory** -- for each persona, complete the inventory before
proceeding to Phase 3:

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

- **Dimension:** The specific axis on which the current solution wins (zero-setup cost, output
  format compatibility, existing keyboard shortcuts, audit trail depth, etc.)
- **Advantage:** What the current solution does better on that dimension for this persona
- **Durability:** Why this advantage is structurally hard to replicate or displace. Must
  reference a structural constraint -- technical, organizational, integration-based, or
  switching-cost-based. **Familiarity is not durability.** "People are used to it" does not
  qualify. Name the structural constraint that makes the advantage persist after the feature
  ships and is known.

A competitive strength without a named structural durability basis must be removed or replaced.

---

## Phase 3 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2 competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|---------------|

- **Switching cost:** Time, steps, effort rating (1--10), or relative measure. Required.
  Qualitative descriptions do not pass.
- **Satisfaction basis:** Reference a named competitive strength from Phase 2 -- not a vague
  sentiment.
- **Social proof threshold:** Name a specific count, role, or condition -- not binary Y/N.
  Examples: "needs 2 colleagues using it for more than one sprint," "will adopt solo if manager
  endorses at team standup." Binary answers fail.

---

## Phase 4 -- Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

The score table **requires a Methodology trace column**:

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

**Methodology trace** -- required: one sentence that (a) names the specific dimension values
from Phase 3 for this persona, and (b) states the Phase 1 threshold those values satisfy,
showing how those inputs produce the assigned score. The trace must cite Phase 1 by reference
-- the infrastructure declared and labeled there.

Failing trace: "Jordan has high switching costs and depends on the current tool, yielding
High." -- Values not named precisely; Phase 1 threshold not cited.

Passing trace: "Jordan's switching cost of 7/10 (High, Phase 1 weight: High) and Critical
workaround satisfaction satisfy the Phase 1 rule that two High-weighted dimensions at H produce
a High score." -- Dimension values named and Phase 1 threshold explicitly cited.

Every Phase 2 persona must be scored individually. A shared blanket score does not pass.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

Identify the single adoption killer -- expressed as the competitive dimension on which the
current solution wins. Use exactly **four labeled sub-parts**. Each must be distinct. Do not
merge any two into a single statement.

**KILL BARRIER**

**(1) Barrier definition**
[What the barrier is -- the observable adoption friction as the most exposed persona experiences
it. State the competitive dimension. Describe the phenomenon; do not include its cause here.]

**(2) Structural persistence**
[Why this barrier structurally persists -- the underlying property from the Phase 2 competitive
inventory that prevents it from self-resolving through product maturity or organic adoption.
Do not repeat (1). Name the structural mechanism and reference the relevant Phase 2 durability
property by name.]

**(3) Intervention target**
[What a mitigation must target -- the specific lever point that, if addressed, would disrupt
the structural persistence mechanism in (2). Name the target, not the intervention. "Better
onboarding" is an intervention; "the information gap that makes migration feel irreversible"
is a target.]

**(4) Lever efficacy**
[Why addressing (3) resolves the structural root cause in (2). Explain the causal connection.
Reference (2) by name. "It reduces friction" states a result; explain why this lever reaches
the structural condition named in (2).]

**Temporal persistence confirmation table:**

| Question | Your answer (write YES or NO) |
|----------|-------------------------------|
| Does this barrier exist today (T=0)? | |
| Does this barrier persist at T=18mo, absent deliberate structural intervention targeting the persistence property in (2)? | |

**Gate rule:** If either answer is NO -- this barrier does not qualify as the kill barrier.
Return to the top of this phase, select a different barrier, and complete all four sub-parts
and the confirmation table again. Do not proceed to Phase 6 until both answers are YES.

Label the confirmed result **CONFIRMED KILL BARRIER**. Name the most exposed persona.

---

## Phase 6 -- Adoption Timeline and Kill-Barrier Trajectory Verdict

**Part A: Per-Persona Adoption Timeline**

**Required disqualifier -- write this sentence before presenting the grid:**

> "This Part A grid captures per-persona trajectory only. It does not satisfy the
> kill-barrier trajectory verdict requirement. That output belongs exclusively to Part B."

Then present the timeline grid for the confirmed kill barrier and at least two personas:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat
- T=6mo and T=18mo cannot copy T=0 without an explicit stated reason

**Part B: Kill-Barrier Trajectory Verdict (distinct from Part A grid)**

**KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence explaining the direction in terms of the structural
persistence property from Phase 5(2). Must reference that property by name. The direction must
be argued from the structural mechanism, not inferred from the per-persona grid.]

**Relationship to Part A grid:** [One sentence: does this verdict align with or differ from
the per-persona trajectories? If it differs, state why. If it aligns, confirm which structural
property drives both.]

This verdict must exist as a labeled output in Part B. A trajectory direction present only in
the Part A grid without a dedicated labeled verdict here fails C-18.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas (e.g., "2 High, 1 Critical, 1 Medium")
- Kill-barrier trajectory direction from Phase 6 Part B
- Competitive summary: kill barrier dimension and its Phase 2 structural durability basis
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## AMEND -- Focus, Quantify, Confirm

Select the persona most exposed to the confirmed kill barrier.

**Focus persona:** [name]

**Switching cost (sharpened):** [most precise quantified value -- time, steps, effort rating, or
relative measure]

**Kill barrier for this persona:** [one sentence restating the barrier in terms of this
persona's specific situation -- name the competitive dimension and why it is most acute for them]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete, specific action]
>
> **(b) Root cause addressed:** [which structural condition from Phase 5(2) this targets --
> quote or directly reference the persistence property by name]
>
> **(c) Causal mechanism:** [why this lever resolves the structural root cause -- the causal
> connection. Reference the intervention target from Phase 5(3). Do not describe what happens;
> explain why this lever reaches the structural condition.]
>
> **(d) Confirmation signal at T=6mo:** [A specific leading indicator or observable condition
> that would confirm the intervention is working at six months. Name what you would measure or
> observe. Vague forward hopes ("users will feel more comfortable") do not qualify. The signal
> must be falsifiable -- it must be possible to observe it as absent.]

The confirmation signal must be an observable, not a hope. The AMEND section is not complete
without it.

---

### V-27: Competitive Inventory Completeness Gate

**Axis:** Lifecycle emphasis -- Phase 2 competitive strength inventory has an explicit
completeness gate before Phase 3 can begin, enforcing that all three named fields are present
and that Durability entries name a structural constraint rather than familiarity
**Hypothesis:** V-25 Phase 2 already has Dimension/Advantage/Durability columns and a
"Familiarity is not durability" disqualifier. C-22's pass condition adds that the inventory
must be "completed in the persona identification phase, before kill-barrier analysis begins"
and that "an inventory present but missing any of the three fields earns PARTIAL." Adding an
explicit completeness gate with a Durability validation rule -- and a prohibition on advancing
to Phase 3 until the gate is passed -- closes C-22 by making the three-field structure and
the structural-constraint-only Durability rule mechanically enforced rather than
format-suggested.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly? Complete
each phase in sequence. Each phase gates the next.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework that will govern per-persona
scores in Phase 4.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight (one sentence -- reference a property of this feature or user population) |
|-----------|------------------------------|------------------------------------------------------------------------------------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof requirement
/ Learning curve.

**Score thresholds** -- define the dimension-combination rules that produce each tier:

- **Critical:** [state which dimension combinations produce this tier]
- **High:** [state which combinations produce this tier]
- **Medium:** [state which combinations]
- **Low:** [state what condition all dimensions must satisfy]

Phase 2 cannot begin until methodology is declared. Per-persona traces in Phase 4 must
reference these thresholds and dimension weights.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named competitor.

**Persona entry:**

- Name and role (specific, not categorical)
- Current solution (named tool or method -- "ad hoc" is not a solution; name what they do)
- Outcome the current solution delivers

**Competitive strength inventory** -- for each persona, complete the following inventory before
proceeding. This inventory must be finished here, in the persona identification phase. Kill-
barrier analysis in Phase 5 will cite Phase 2 Durability properties by name -- if they are not
named here, Phase 5 cannot satisfy its structural persistence requirement.

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

- **Dimension:** The specific axis on which the current solution wins (zero-setup cost, output
  format compatibility, existing keyboard shortcuts, audit trail depth, etc.)
- **Advantage:** What the current solution does better on that dimension for this persona
- **Durability:** Why this advantage is structurally hard to replicate or displace. Must
  reference a structural constraint -- technical, organizational, integration-based, or
  switching-cost-based. **Familiarity is not durability.** "People are used to it" does not
  qualify. Name the structural constraint that makes the advantage persist after the feature
  ships and is known.

**Completeness gate:** Before writing Phase 3, verify the following for each persona:

1. All three inventory fields (Dimension, Advantage, Durability) are present and populated.
2. No Durability entry uses "familiarity," "habit," "people are used to it," or any equivalent.
   If it does, replace it with a structural constraint before proceeding.
3. Each Dimension names a specific competitive axis -- not a category like "usability."

Do not write Phase 3 until every persona's inventory passes all three checks. An inventory
entry that fails any check must be corrected in this phase, not deferred to Phase 5.

---

## Phase 3 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2 competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|---------------|

- **Switching cost:** Time, steps, effort rating (1--10), or relative measure. Required.
  Qualitative descriptions do not pass.
- **Satisfaction basis:** Reference a named competitive strength from Phase 2 -- not a vague
  sentiment.
- **Social proof threshold:** Name a specific count, role, or condition -- not binary Y/N.
  Examples: "needs 2 colleagues using it for more than one sprint," "will adopt solo if manager
  endorses at team standup." Binary answers fail.

---

## Phase 4 -- Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

The score table **requires a Methodology trace column**:

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

**Methodology trace** -- required: one sentence that (a) names the specific dimension values
from Phase 3 for this persona, and (b) states the Phase 1 threshold those values satisfy,
showing how those inputs produce the assigned score.

Failing trace: "Jordan has high switching costs and depends on the current tool, yielding
High." -- Values not named precisely; Phase 1 threshold not cited.

Passing trace: "Jordan's switching cost of 7/10 (High, Phase 1 weight: High) and Critical
workaround satisfaction satisfy the Phase 1 rule that two High-weighted dimensions at H produce
a High score." -- Dimension values named and Phase 1 threshold explicitly cited.

Every Phase 2 persona must be scored individually. A shared blanket score does not pass.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

Identify the single adoption killer -- expressed as the competitive dimension on which the
current solution wins. Use exactly **four labeled sub-parts**. Each must be distinct. Do not
merge any two into a single statement.

**KILL BARRIER**

**(1) Barrier definition**
[What the barrier is -- the observable adoption friction as the most exposed persona experiences
it. State the competitive dimension. Describe the phenomenon; do not include its cause here.]

**(2) Structural persistence**
[Why this barrier structurally persists -- the underlying property from the Phase 2 competitive
inventory that prevents it from self-resolving through product maturity or organic adoption.
Do not repeat (1). Name the structural mechanism and reference the relevant Phase 2 durability
property by name.]

**(3) Intervention target**
[What a mitigation must target -- the specific lever point that, if addressed, would disrupt
the structural persistence mechanism in (2). Name the target, not the intervention. "Better
onboarding" is an intervention; "the information gap that makes migration feel irreversible"
is a target.]

**(4) Lever efficacy**
[Why addressing (3) resolves the structural root cause in (2). Explain the causal connection.
Reference (2) by name. "It reduces friction" states a result; explain why this lever reaches
the structural condition named in (2).]

**Temporal persistence confirmation table:**

| Question | Your answer (write YES or NO) |
|----------|-------------------------------|
| Does this barrier exist today (T=0)? | |
| Does this barrier persist at T=18mo, absent deliberate structural intervention targeting the persistence property in (2)? | |

**Gate rule:** If either answer is NO -- this barrier does not qualify as the kill barrier.
Return to the top of this phase, select a different barrier, and complete all four sub-parts
and the confirmation table again. Do not proceed to Phase 6 until both answers are YES.

Label the confirmed result **CONFIRMED KILL BARRIER**. Name the most exposed persona.

---

## Phase 6 -- Adoption Timeline and Kill-Barrier Trajectory Verdict

**Part A: Per-Persona Adoption Timeline**

**Required disqualifier -- write this sentence before presenting the grid:**

> "This Part A grid captures per-persona trajectory only. It does not satisfy the
> kill-barrier trajectory verdict requirement. That output belongs exclusively to Part B."

Then present the timeline grid for the confirmed kill barrier and at least two personas:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat
- T=6mo and T=18mo cannot copy T=0 without an explicit stated reason

**Part B: Kill-Barrier Trajectory Verdict (distinct from Part A grid)**

**KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence explaining the direction in terms of the structural
persistence property from Phase 5(2). Must reference that property by name.]

**Relationship to Part A grid:** [One sentence: alignment or divergence, and why.]

This verdict must exist as a labeled output in Part B. A trajectory direction present only in
the Part A grid without a dedicated labeled verdict here fails.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas (e.g., "2 High, 1 Critical, 1 Medium")
- Kill-barrier trajectory direction from Phase 6 Part B
- Competitive summary: kill barrier dimension and its Phase 2 structural durability basis
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## AMEND -- Focus, Quantify, Confirm

Select the persona most exposed to the confirmed kill barrier.

**Focus persona:** [name]

**Switching cost (sharpened):** [most precise quantified value -- time, steps, effort rating, or
relative measure]

**Kill barrier for this persona:** [one sentence restating the barrier in terms of this
persona's specific situation -- name the competitive dimension and why it is most acute for them]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete, specific action]
>
> **(b) Root cause addressed:** [which structural condition from Phase 5(2) this targets --
> quote or directly reference the persistence property by name]
>
> **(c) Causal mechanism:** [why this lever resolves the structural root cause -- the causal
> connection. Reference the intervention target from Phase 5(3). Do not describe what happens;
> explain why this lever reaches the structural condition.]
>
> **(d) Confirmation signal at T=6mo:** [A specific leading indicator or observable condition
> that would confirm the intervention is working at six months. Name what you would measure or
> observe. Vague forward hopes ("users will feel more comfortable") do not qualify. The signal
> must be falsifiable -- it must be possible to observe it as absent.]

---

### V-28: Falsifiable Anchor in Intervention Target

**Axis:** Output format -- Phase 5 Part (3) must produce a falsifiability test as a required
output before Part (4) appears, ensuring the named intervention target is specific enough to
anchor the AMEND confirmation signal as an observable condition
**Hypothesis:** V-25 Phase 5 Part (3) prompts "Name the target, not the intervention" with a
good example, but does not require the model to demonstrate falsifiability before proceeding.
A model can name a target at "approach granularity" that reads as a mechanism while remaining
too general to anchor C-16. Adding a required falsifiability test -- "Write one sentence: at
T=6mo, the absence of this lever being addressed would be observable as [specific condition].
If you cannot complete this, your Part (3) is too general; replace it." -- closes C-23 by
making the falsifiability requirement a structural production gate, not an implicit expectation.
The test is executed in Part (3), before AMEND exists, so the anchor is established upstream.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly? Complete
each phase in sequence. Each phase gates the next.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework that will govern per-persona
scores in Phase 4.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight (one sentence -- reference a property of this feature or user population) |
|-----------|------------------------------|------------------------------------------------------------------------------------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof requirement
/ Learning curve.

**Score thresholds** -- define the dimension-combination rules that produce each tier:

- **Critical:** [state which dimension combinations produce this tier]
- **High:** [state which combinations produce this tier]
- **Medium:** [state which combinations]
- **Low:** [state what condition all dimensions must satisfy]

Phase 2 cannot begin until methodology is declared. Per-persona traces in Phase 4 must
reference these thresholds and dimension weights.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named competitor.

**Persona entry:**

- Name and role (specific, not categorical)
- Current solution (named tool or method -- "ad hoc" is not a solution; name what they do)
- Outcome the current solution delivers

**Competitive strength inventory** -- for each persona:

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

- **Dimension:** The specific axis on which the current solution wins
- **Advantage:** What the current solution does better on that dimension for this persona
- **Durability:** Why this advantage is structurally hard to replicate or displace. Must
  reference a structural constraint. **Familiarity is not durability.** Name the structural
  constraint that makes the advantage persist after the feature ships and is known.

A competitive strength without a named structural durability basis must be removed or replaced.

---

## Phase 3 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2 competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|---------------|

- **Switching cost:** Time, steps, effort rating (1--10), or relative measure. Required.
- **Satisfaction basis:** Reference a named competitive strength from Phase 2.
- **Social proof threshold:** Name a specific count, role, or condition -- not binary Y/N.

---

## Phase 4 -- Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

The score table **requires a Methodology trace column**:

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

**Methodology trace** -- required: one sentence that (a) names the specific dimension values
from Phase 3 for this persona, and (b) states the Phase 1 threshold those values satisfy,
showing how those inputs produce the assigned score.

Every Phase 2 persona must be scored individually. A shared blanket score does not pass.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

Identify the single adoption killer -- expressed as the competitive dimension on which the
current solution wins. Use exactly **four labeled sub-parts**. Each must be distinct. Do not
merge any two into a single statement.

**KILL BARRIER**

**(1) Barrier definition**
[What the barrier is -- the observable adoption friction as the most exposed persona experiences
it. State the competitive dimension. Describe the phenomenon; do not include its cause here.]

**(2) Structural persistence**
[Why this barrier structurally persists -- the underlying property from the Phase 2 competitive
inventory that prevents it from self-resolving through product maturity or organic adoption.
Do not repeat (1). Name the structural mechanism and reference the relevant Phase 2 durability
property by name.]

**(3) Intervention target**
[What a mitigation must target -- the specific lever point that, if addressed, would disrupt
the structural persistence mechanism in (2). Name the target, not the intervention. "Better
onboarding" is an intervention; "the moment a user first completes a cross-team workflow
without reverting to their previous tool" is a lever point.]

**Falsifiability test (required before writing Part (4)):** Write the following sentence,
completing the bracketed portion:

> "At T=6mo, the absence of this lever being addressed would be observable as: [specific
> behavioral or measurable condition]."

If you cannot complete this sentence with a specific observable condition -- your Part (3)
intervention target is too general. Replace Part (3) with a more specific mechanism and repeat
the falsifiability test. Do not write Part (4) until the falsifiability test produces a
specific observable condition. The AMEND confirmation signal in step (d) must cite this lever
point directly.

**(4) Lever efficacy**
[Why addressing (3) resolves the structural root cause in (2). Explain the causal connection.
Reference (2) by name. "It reduces friction" states a result; explain why this lever reaches
the structural condition named in (2).]

**Temporal persistence confirmation table:**

| Question | Your answer (write YES or NO) |
|----------|-------------------------------|
| Does this barrier exist today (T=0)? | |
| Does this barrier persist at T=18mo, absent deliberate structural intervention targeting the persistence property in (2)? | |

**Gate rule:** If either answer is NO -- this barrier does not qualify as the kill barrier.
Return to the top of this phase, select a different barrier, and complete all four sub-parts
and the confirmation table again. Do not proceed to Phase 6 until both answers are YES.

Label the confirmed result **CONFIRMED KILL BARRIER**. Name the most exposed persona.

---

## Phase 6 -- Adoption Timeline and Kill-Barrier Trajectory Verdict

**Part A: Per-Persona Adoption Timeline**

**Required disqualifier -- write this sentence before presenting the grid:**

> "This Part A grid captures per-persona trajectory only. It does not satisfy the
> kill-barrier trajectory verdict requirement. That output belongs exclusively to Part B."

Then present the timeline grid for the confirmed kill barrier and at least two personas:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat
- T=6mo and T=18mo cannot copy T=0 without an explicit stated reason

**Part B: Kill-Barrier Trajectory Verdict (distinct from Part A grid)**

**KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence explaining the direction in terms of the structural
persistence property from Phase 5(2). Must reference that property by name.]

**Relationship to Part A grid:** [One sentence: alignment or divergence, and why.]

This verdict must exist as a labeled output in Part B. A trajectory direction present only in
the Part A grid without a dedicated labeled verdict here fails.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas
- Kill-barrier trajectory direction from Phase 6 Part B
- Competitive summary: kill barrier dimension and its Phase 2 structural durability basis
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## AMEND -- Focus, Quantify, Confirm

Select the persona most exposed to the confirmed kill barrier.

**Focus persona:** [name]

**Switching cost (sharpened):** [most precise quantified value]

**Kill barrier for this persona:** [one sentence restating the barrier -- name the competitive
dimension and why it is most acute for them]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete, specific action]
>
> **(b) Root cause addressed:** [which structural condition from Phase 5(2) this targets --
> reference the persistence property by name]
>
> **(c) Causal mechanism:** [why this lever resolves the structural root cause. Reference the
> intervention target from Phase 5(3) -- the specific mechanism named and falsifiability-tested
> there. Explain why this lever reaches the structural condition, not what the result will be.]
>
> **(d) Confirmation signal at T=6mo:** [The observable condition named in the Phase 5(3)
> falsifiability test, adapted to this persona. Must be an observable, not a hope. Must be
> possible to observe it as absent.]

---

### V-29: Phase-Zero Gate + Falsifiable Anchor

**Axis:** Combination -- lifecycle emphasis (C-21 self-identification label) + output format
(C-23 falsifiability test in Phase 5 Part (3))
**Hypothesis:** C-21 and C-23 are the two uncertain closures in V-25 -- C-22 is likely already
passing in V-25 given the Dimension/Advantage/Durability table in Phase 2. V-29 combines V-26's
required infrastructure label at Phase 1 close with V-28's falsifiability test in Phase 5
Part (3). These mechanisms occupy Phase 1 and Phase 5 respectively, do not interact, and
should activate independently. Expected: C-21 and C-23 both reach full pass; all criteria
from R5 that passed in V-25 remain intact; C-22 receives incidental coverage through the
unchanged Phase 2 structure.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly? Complete
each phase in sequence. Each phase gates the next.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework that will govern per-persona
scores in Phase 4.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight (one sentence -- reference a property of this feature or user population) |
|-----------|------------------------------|------------------------------------------------------------------------------------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof requirement
/ Learning curve.

**Score thresholds** -- define the dimension-combination rules that produce each tier:

- **Critical:** [state which dimension combinations produce this tier]
- **High:** [state which combinations produce this tier]
- **Medium:** [state which combinations]
- **Low:** [state what condition all dimensions must satisfy]

**Required infrastructure label:** After completing the dimension weights and score thresholds
above, write the following statement on its own line before Phase 2 begins:

> "SCORING INFRASTRUCTURE DECLARED. All per-persona methodology traces in Phase 4 must cite
> this Phase 1 output by reference -- naming the specific dimension weights and tier thresholds
> declared above to show how each persona's score was produced. Phase 4 traces that reference
> dimension values without citing these thresholds, or that cite thresholds without naming
> dimension values, will not satisfy the per-score trace requirement."

Phase 2 cannot begin until this statement is written.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named competitor.

**Persona entry:**

- Name and role (specific, not categorical)
- Current solution (named tool or method -- "ad hoc" is not a solution; name what they do)
- Outcome the current solution delivers

**Competitive strength inventory** -- for each persona:

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

- **Dimension:** The specific axis on which the current solution wins
- **Advantage:** What the current solution does better on that dimension for this persona
- **Durability:** Why this advantage is structurally hard to replicate or displace. Must
  reference a structural constraint -- technical, organizational, integration-based, or
  switching-cost-based. **Familiarity is not durability.** "People are used to it" does not
  qualify. Name the structural constraint that makes the advantage persist after the feature
  ships and is known.

A competitive strength without a named structural durability basis must be removed or replaced.

---

## Phase 3 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2 competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|---------------|

- **Switching cost:** Time, steps, effort rating (1--10), or relative measure. Required.
  Qualitative descriptions do not pass.
- **Satisfaction basis:** Reference a named competitive strength from Phase 2.
- **Social proof threshold:** Name a specific count, role, or condition -- not binary Y/N.

---

## Phase 4 -- Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

The score table **requires a Methodology trace column**:

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

**Methodology trace** -- required: one sentence that (a) names the specific dimension values
from Phase 3 for this persona, and (b) states the Phase 1 threshold those values satisfy,
showing how those inputs produce the assigned score. Cite Phase 1 by reference -- the
SCORING INFRASTRUCTURE DECLARED there.

Every Phase 2 persona must be scored individually. A shared blanket score does not pass.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

Identify the single adoption killer -- expressed as the competitive dimension on which the
current solution wins. Use exactly **four labeled sub-parts**. Each must be distinct. Do not
merge any two into a single statement.

**KILL BARRIER**

**(1) Barrier definition**
[What the barrier is -- the observable adoption friction as the most exposed persona experiences
it. State the competitive dimension. Describe the phenomenon; do not include its cause here.]

**(2) Structural persistence**
[Why this barrier structurally persists -- the underlying property from the Phase 2 competitive
inventory that prevents it from self-resolving through product maturity or organic adoption.
Do not repeat (1). Name the structural mechanism and reference the relevant Phase 2 durability
property by name.]

**(3) Intervention target**
[What a mitigation must target -- the specific lever point that, if addressed, would disrupt
the structural persistence mechanism in (2). Name the target, not the intervention. "Better
onboarding" is an intervention; "the moment a user first completes a cross-team workflow
without reverting to their previous tool" is a lever point.]

**Falsifiability test (required before writing Part (4)):** Write the following sentence,
completing the bracketed portion:

> "At T=6mo, the absence of this lever being addressed would be observable as: [specific
> behavioral or measurable condition]."

If you cannot complete this sentence with a specific observable condition -- your Part (3)
intervention target is too general. Replace Part (3) with a more specific mechanism and repeat
the test. Do not write Part (4) until the test produces a specific observable condition.

**(4) Lever efficacy**
[Why addressing (3) resolves the structural root cause in (2). Explain the causal connection.
Reference (2) by name.]

**Temporal persistence confirmation table:**

| Question | Your answer (write YES or NO) |
|----------|-------------------------------|
| Does this barrier exist today (T=0)? | |
| Does this barrier persist at T=18mo, absent deliberate structural intervention targeting the persistence property in (2)? | |

**Gate rule:** If either answer is NO -- this barrier does not qualify as the kill barrier.
Return to the top of this phase, select a different barrier, and complete all four sub-parts
and the confirmation table again. Do not proceed to Phase 6 until both answers are YES.

Label the confirmed result **CONFIRMED KILL BARRIER**. Name the most exposed persona.

---

## Phase 6 -- Adoption Timeline and Kill-Barrier Trajectory Verdict

**Part A: Per-Persona Adoption Timeline**

**Required disqualifier -- write this sentence before presenting the grid:**

> "This Part A grid captures per-persona trajectory only. It does not satisfy the
> kill-barrier trajectory verdict requirement. That output belongs exclusively to Part B."

Then present the timeline grid for the confirmed kill barrier and at least two personas:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat
- T=6mo and T=18mo cannot copy T=0 without an explicit stated reason

**Part B: Kill-Barrier Trajectory Verdict (distinct from Part A grid)**

**KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence explaining the direction in terms of the structural
persistence property from Phase 5(2). Must reference that property by name.]

**Relationship to Part A grid:** [One sentence: alignment or divergence, and why.]

This verdict must exist as a labeled output in Part B. A trajectory direction present only in
the Part A grid without a dedicated labeled verdict here fails.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas
- Kill-barrier trajectory direction from Phase 6 Part B
- Competitive summary: kill barrier dimension and its Phase 2 structural durability basis
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## AMEND -- Focus, Quantify, Confirm

Select the persona most exposed to the confirmed kill barrier.

**Focus persona:** [name]

**Switching cost (sharpened):** [most precise quantified value]

**Kill barrier for this persona:** [one sentence restating the barrier -- name the competitive
dimension and why it is most acute for them]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete, specific action]
>
> **(b) Root cause addressed:** [which structural condition from Phase 5(2) this targets --
> reference the persistence property by name]
>
> **(c) Causal mechanism:** [why this lever resolves the structural root cause. Reference the
> intervention target from Phase 5(3). Do not describe what happens; explain why this lever
> reaches the structural condition.]
>
> **(d) Confirmation signal at T=6mo:** [The observable condition named in the Phase 5(3)
> falsifiability test, adapted to this persona. Must be falsifiable -- possible to observe it
> as absent.]

---

### V-30: Full Integration -- All Fifteen Aspirationals

**Axis:** Combination -- all three new single-axis mechanisms (V-26 + V-27 + V-28) layered
onto V-25, which already closed C-09 through C-20
**Hypothesis:** V-25 scored 200/200 on the v5 rubric. The v6 rubric adds C-21, C-22, C-23.
V-26 closes C-21 via the SCORING INFRASTRUCTURE DECLARED label; V-27 confirms and gates C-22
via the completeness gate in Phase 2; V-28 closes C-23 via the Phase 5(3) falsifiability test.
The three additions occupy Phase 1 (V-26), Phase 2 (V-27), and Phase 5 (V-28) respectively --
no phase overlap, no competition. V-25's coverage of C-09 through C-20 is preserved intact.
Expected ceiling: 230/230.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly? Complete
each phase in sequence. Each phase gates the next.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework that will govern per-persona
scores in Phase 4.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight (one sentence -- reference a property of this feature or user population) |
|-----------|------------------------------|------------------------------------------------------------------------------------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof requirement
/ Learning curve.

**Score thresholds** -- define the dimension-combination rules that produce each tier:

- **Critical:** [state which dimension combinations produce this tier]
- **High:** [state which combinations produce this tier]
- **Medium:** [state which combinations]
- **Low:** [state what condition all dimensions must satisfy]

**Required infrastructure label:** After completing the dimension weights and score thresholds
above, write the following statement on its own line before Phase 2 begins:

> "SCORING INFRASTRUCTURE DECLARED. All per-persona methodology traces in Phase 4 must cite
> this Phase 1 output by reference -- naming the specific dimension weights and tier thresholds
> declared above to show how each persona's score was produced. Phase 4 traces that reference
> dimension values without citing these thresholds, or that cite thresholds without naming
> dimension values, will not satisfy the per-score trace requirement."

Phase 2 cannot begin until this statement is written. The statement is the boundary marker
that closes Phase 1.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named competitor.

**Persona entry:**

- Name and role (specific, not categorical)
- Current solution (named tool or method -- "ad hoc" is not a solution; name what they do)
- Outcome the current solution delivers

**Competitive strength inventory** -- for each persona, complete the following inventory before
proceeding. This inventory must be finished here, in the persona identification phase. Kill-
barrier analysis in Phase 5 will cite Phase 2 Durability properties by name -- if they are not
named here, Phase 5 cannot satisfy its structural persistence requirement.

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

- **Dimension:** The specific axis on which the current solution wins (zero-setup cost, output
  format compatibility, existing keyboard shortcuts, audit trail depth, etc.)
- **Advantage:** What the current solution does better on that dimension for this persona
- **Durability:** Why this advantage is structurally hard to replicate or displace. Must
  reference a structural constraint -- technical, organizational, integration-based, or
  switching-cost-based. **Familiarity is not durability.** "People are used to it" does not
  qualify. Name the structural constraint that makes the advantage persist after the feature
  ships and is known.

**Completeness gate:** Before writing Phase 3, verify the following for each persona:

1. All three inventory fields (Dimension, Advantage, Durability) are present and populated.
2. No Durability entry uses "familiarity," "habit," "people are used to it," or any equivalent.
   If it does, replace it with a structural constraint before proceeding.
3. Each Dimension names a specific competitive axis -- not a category like "usability."

Do not write Phase 3 until every persona's inventory passes all three checks. An inventory
entry that fails any check must be corrected in this phase, not deferred to Phase 5.

---

## Phase 3 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2 competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|---------------|

- **Switching cost:** Time, steps, effort rating (1--10), or relative measure. Required.
  Qualitative descriptions do not pass.
- **Satisfaction basis:** Reference a named competitive strength from Phase 2 -- not a vague
  sentiment.
- **Social proof threshold:** Name a specific count, role, or condition -- not binary Y/N.
  Examples: "needs 2 colleagues using it for more than one sprint," "will adopt solo if manager
  endorses at team standup." Binary answers fail.

---

## Phase 4 -- Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

The score table **requires a Methodology trace column**:

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

**Methodology trace** -- required: one sentence that (a) names the specific dimension values
from Phase 3 for this persona, and (b) states the Phase 1 threshold those values satisfy,
showing how those inputs produce the assigned score. Cite Phase 1 by reference -- the
SCORING INFRASTRUCTURE DECLARED there is the named source.

Failing trace: "Jordan has high switching costs and depends on the current tool, yielding
High." -- Values not named precisely; Phase 1 threshold not cited.

Passing trace: "Jordan's switching cost of 7/10 (High, Phase 1 weight: High) and Critical
workaround satisfaction satisfy the Phase 1 rule that two High-weighted dimensions at H produce
a High score." -- Dimension values named and Phase 1 threshold explicitly cited.

Every Phase 2 persona must be scored individually. A shared blanket score does not pass.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

Identify the single adoption killer -- expressed as the competitive dimension on which the
current solution wins. Use exactly **four labeled sub-parts**. Each must be distinct. Do not
merge any two into a single statement.

**KILL BARRIER**

**(1) Barrier definition**
[What the barrier is -- the observable adoption friction as the most exposed persona experiences
it. State the competitive dimension. Describe the phenomenon; do not include its cause here.]

**(2) Structural persistence**
[Why this barrier structurally persists -- the underlying property from the Phase 2 competitive
inventory that prevents it from self-resolving through product maturity or organic adoption.
Do not repeat (1). Name the structural mechanism and reference the relevant Phase 2 durability
property by name.]

**(3) Intervention target**
[What a mitigation must target -- the specific lever point that, if addressed, would disrupt
the structural persistence mechanism in (2). Name the target, not the intervention. "Better
onboarding" is an intervention; "the moment a user first completes a cross-team workflow
without reverting to their previous tool" is a lever point.]

**Falsifiability test (required before writing Part (4)):** Write the following sentence,
completing the bracketed portion:

> "At T=6mo, the absence of this lever being addressed would be observable as: [specific
> behavioral or measurable condition]."

If you cannot complete this sentence with a specific observable condition -- your Part (3)
intervention target is too general. Replace Part (3) with a more specific mechanism and repeat
the falsifiability test. Do not write Part (4) until the test produces a specific observable
condition. The AMEND confirmation signal in step (d) must cite this lever point directly.

**(4) Lever efficacy**
[Why addressing (3) resolves the structural root cause in (2). Explain the causal connection.
Reference (2) by name. "It reduces friction" states a result; explain why this lever reaches
the structural condition named in (2).]

**Temporal persistence confirmation table:**

| Question | Your answer (write YES or NO) |
|----------|-------------------------------|
| Does this barrier exist today (T=0)? | |
| Does this barrier persist at T=18mo, absent deliberate structural intervention targeting the persistence property in (2)? | |

**Gate rule:** If either answer is NO -- this barrier does not qualify as the kill barrier.
Return to the top of this phase, select a different barrier, and complete all four sub-parts
and the confirmation table again. Do not proceed to Phase 6 until both answers are YES.

Label the confirmed result **CONFIRMED KILL BARRIER**. Name the most exposed persona.

---

## Phase 6 -- Adoption Timeline and Kill-Barrier Trajectory Verdict

**Part A: Per-Persona Adoption Timeline**

**Required disqualifier -- write this sentence before presenting the grid:**

> "This Part A grid captures per-persona trajectory only. It does not satisfy the
> kill-barrier trajectory verdict requirement. That output belongs exclusively to Part B."

Then present the timeline grid for the confirmed kill barrier and at least two personas:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat
- T=6mo and T=18mo cannot copy T=0 without an explicit stated reason

**Part B: Kill-Barrier Trajectory Verdict (distinct from Part A grid)**

**KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence explaining the direction in terms of the structural
persistence property from Phase 5(2). Must reference that property by name. The direction must
be argued from the structural mechanism, not inferred from the per-persona grid.]

**Relationship to Part A grid:** [One sentence: does this verdict align with or differ from
the per-persona trajectories? If it differs, state why. If it aligns, confirm which structural
property drives both.]

This verdict must exist as a labeled output in Part B. A trajectory direction present only in
the Part A grid without a dedicated labeled verdict here fails C-18.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas (e.g., "2 High, 1 Critical, 1 Medium")
- Kill-barrier trajectory direction from Phase 6 Part B
- Competitive summary: kill barrier dimension and its Phase 2 structural durability basis
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## AMEND -- Focus, Quantify, Confirm

Select the persona most exposed to the confirmed kill barrier.

**Focus persona:** [name]

**Switching cost (sharpened):** [most precise quantified value -- time, steps, effort rating, or
relative measure]

**Kill barrier for this persona:** [one sentence restating the barrier in terms of this
persona's specific situation -- name the competitive dimension and why it is most acute for them]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete, specific action]
>
> **(b) Root cause addressed:** [which structural condition from Phase 5(2) this targets --
> quote or directly reference the persistence property by name]
>
> **(c) Causal mechanism:** [why this lever resolves the structural root cause -- the causal
> connection. Reference the intervention target from Phase 5(3) -- the specific mechanism named
> and falsifiability-tested there. Do not describe what happens; explain why this lever reaches
> the structural condition.]
>
> **(d) Confirmation signal at T=6mo:** [The observable condition named in the Phase 5(3)
> falsifiability test, adapted to this persona. Must be an observable, not a hope. Must be
> possible to observe it as absent.]

The confirmation signal must be an observable, not a hope. The AMEND section is not complete
without it.
