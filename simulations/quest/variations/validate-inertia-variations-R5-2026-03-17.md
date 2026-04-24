Written to `simulations/quest/variations/validate-inertia-variations-R5-2026-03-17.md`.

---

## validate-inertia Variations R5 -- Summary

| # | Label | Axis | Primary targets |
|---|-------|------|-----------------|
| V-21 | Literal disqualifier in per-persona grid | Output format | C-19 |
| V-22 | Binary reselection gate as required table | Lifecycle emphasis | C-20 |
| V-23 | "Checkpoint verdict" phrasing | Phrasing register | C-20 (alt mechanism) |
| V-24 | Disqualifier + gate combination | Output format + lifecycle | C-19, C-20 |
| V-25 | Full integration -- all twelve aspirationals | All axes | C-09--C-20 |

---

### Design notes

**C-19 failure mode in V-20:** V-20's Phase 6 uses "Part A / Part B" labels and names Part B "distinct from Part A grid" -- but Part A contains no literal sentence stating it does not satisfy the kill-barrier trajectory verdict requirement. C-19's pass condition requires a literal "does not satisfy" statement. Implicit separation earns PARTIAL; absence fails.

**C-20 status in V-20:** V-20 already has `[YES / NO]` placeholders and "If either is NO: reselect" -- likely passes C-20 already. V-22 and V-23 isolate this mechanism to confirm it and test two implementation registers (table vs. checkpoint-verdict phrasing).

**Single-axis logic:**
- V-21 (C-19): adds one required sentence containing "does not satisfy" to the per-persona timeline section header -- nothing else changes
- V-22 (C-20): formats the temporal persistence test as a mandatory two-row table with gate rule
- V-23 (C-20 alt): replaces the table with a PROCEED/RESELECT verdict word -- tests whether behavioral framing closes C-20 as reliably as structural formatting

**V-24** (C-19 + C-20): minimal combination -- confirms both mechanisms activate cleanly without the full aspirational stack of V-25.

**V-25** (all 12): V-20 + one addition: the required "does not satisfy" disqualifier sentence in Phase 6 Part A. The only gap between V-20 and a perfect v5 rubric score.
 adding the one mechanism V-20 lacked: the literal "does not satisfy"
disqualifier sentence in Phase 6 Part A. C-20 is already structurally present in V-20's Phase
5 temporal gate; V-25 keeps it and tightens the label to match the C-20 pass condition exactly.
Expected ceiling: 200/200 if all phases execute without degradation.

---

### V-21: Literal Disqualifier in Per-Persona Grid

**Axis:** Output format -- the per-persona adoption timeline section must contain a required
literal sentence stating it does not satisfy the kill-barrier trajectory verdict criterion
**Hypothesis:** Adding a required "does not satisfy" sentence inside the per-persona timeline
section will close C-19 by making the disqualifier an explicit format requirement rather than
an implied separation. V-17 and V-19 separated the two outputs structurally but left the
disqualifier implicit ("context only"). C-19 requires a literal statement -- this variation
enforces it as a sentence the model must produce containing "does not satisfy."

---

You are running **validate-inertia** for: {{topic}}

Stress-test adoption inertia. Why would users NOT adopt this feature even if it works perfectly?

---

## Phase 1 -- Persona Identification

Name 2--4 user personas. Each must have:

- **Name and role** -- specific title or function, not a category
- **Current workaround** -- the actual tool or method they use today (name it -- "ad hoc" fails)
- **Outcome they optimize for** -- what the current workaround successfully delivers

---

## Phase 2 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof req. (named threshold) | Learning curve |
|---------|---------------------------------|--------------------|----------------------------|-------------------------------|-------------------------------------|---------------|

Column rules:

- **Switching cost:** Time, steps, effort rating (1--10), or relative measure. Required.
  Qualitative descriptions alone fail.
- **Social proof req.:** Name a specific threshold or condition. Binary Y/N fails. Examples:
  "needs 2+ teammates already using it," "will adopt solo if manager mandates it."
- **Habit lock-in:** Name the specific repeated behavior. "General familiarity" fails.

---

## Phase 3 -- Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

One sentence per score naming the primary inertia driver.

Every Phase 1 persona must be scored individually. No shared scores.

---

## Phase 4 -- Kill Barrier

Identify the single adoption killer -- the one barrier that would block adoption even if all
other inertia were resolved.

- **Kill barrier:** [name it precisely]
- **Structural persistence:** [the underlying property that prevents self-resolution through
  product maturity or organic adoption -- not familiarity, but the structural constraint]
- **Most exposed persona:** [name]

---

## Phase 5 -- Per-Persona Adoption Timeline

**Section label: PER-PERSONA ADOPTION TIMELINE**

**Required disqualifier:** Before presenting the grid, write this sentence (fill in the
bracketed part with your Phase 6 section label):

> "This section does not satisfy the kill-barrier trajectory verdict requirement. That output
> belongs exclusively to [Phase 6 section label]."

After writing the disqualifier sentence, present the timeline grid for the confirmed kill
barrier and at least two personas:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat
- T=6mo and T=18mo cannot copy T=0 without an explicit stated reason

The disqualifier sentence is not satisfied by headings, labels, or implicit separation. It
must appear as a sentence containing the words "does not satisfy."

---

## Phase 6 -- Kill-Barrier Trajectory Verdict

**KILL-BARRIER TRAJECTORY VERDICT**

This section produces a dedicated, labeled verdict for the kill barrier's own time-sensitivity.
It is not a summary of Phase 5.

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence explaining the direction in terms of the structural
persistence property from Phase 4. Must reference that persistence property by name.]

**Relationship to Phase 5 grid:** [One sentence: does this verdict align with or differ from
the per-persona trajectories? If it differs, state why. If it aligns, confirm which structural
property drives both.]

This section is not satisfied by pointing to Phase 5. The verdict must exist as a labeled
output here.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas
- Kill-barrier trajectory direction from Phase 6
- 1--2 sentence rationale connecting score distribution, trajectory, and the confirmed kill
  barrier structural persistence property

---

## AMEND

Select the persona most exposed to the confirmed kill barrier.

- **Focus persona:** [name]
- **Switching cost (sharpened):** [most precise quantified value for this persona]
- **Kill barrier for this persona:** [one sentence restating the barrier and why it persists
  specifically for them]
- **Mitigation:** [one concrete intervention -- explain why this lever addresses the structural
  persistence property from Phase 4, not just what the intervention does]

---

### V-22: Binary Reselection Gate as Required Table

**Axis:** Lifecycle emphasis -- the kill barrier temporal persistence test is structured as a
required two-row table with explicit YES/NO answers and a conditional reselection instruction
**Hypothesis:** Formatting the temporal persistence test as a mandatory table with a YES/NO
column -- followed by a literal "If either is NO: reselect" line -- will close C-20 by making
the binary confirmation gate a required structural element rather than an implied temporal
assertion. A kill barrier that passes the gate proceeds to Phase 5. One that does not must be
replaced before any further analysis occurs. C-20 PARTIAL is the floor (gate present at only
one horizon); full pass requires both horizons answered and the reselect instruction present.

---

You are running **validate-inertia** for: {{topic}}

Stress-test adoption inertia. Why would users NOT adopt this feature even if it works perfectly?

---

## Phase 1 -- Persona Identification

Name 2--4 user personas. Each must have:

- **Name and role** -- specific title or function, not a category
- **Current workaround** -- the actual tool or method they use today (name it)
- **Outcome they optimize for** -- what the current workaround successfully delivers

---

## Phase 2 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof req. (named threshold) | Learning curve |
|---------|---------------------------------|--------------------|----------------------------|-------------------------------|-------------------------------------|---------------|

- **Switching cost:** Measurable value required -- time, steps, effort rating (1--10), or
  relative measure. "It's hard" does not pass.
- **Social proof req.:** Name a specific count, role, or condition. Binary Y/N fails.
- **Habit lock-in:** Name the specific repeated behavior. "General familiarity" fails.

---

## Phase 3 -- Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

One sentence per score naming the primary inertia driver. Every Phase 1 persona must be
scored individually. No shared scores.

---

## Phase 4 -- Kill Barrier

Identify the single adoption killer -- the one barrier that would block adoption even if all
other inertia were resolved.

- **Kill barrier:** [name it precisely]
- **Structural persistence:** [the property that prevents self-resolution -- the structural
  constraint, not familiarity]
- **Most exposed persona:** [name]

**Temporal persistence confirmation table:**

| Question | Your answer (write YES or NO) |
|----------|-------------------------------|
| Does this barrier exist today (T=0)? | |
| Does this barrier persist at T=18mo, absent any deliberate structural intervention targeting the persistence property? | |

**Gate rule:** If either answer is NO -- this barrier does not qualify as the kill barrier.
Return to this phase, select a different barrier, and complete the confirmation table again.
Do not proceed to Phase 5 until both answers are YES.

Label the confirmed barrier **CONFIRMED KILL BARRIER** before proceeding.

---

## Phase 5 -- Per-Persona Adoption Timeline

For the confirmed kill barrier and at least two personas, project inertia across three
horizons:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat
- T=6mo and T=18mo cannot copy T=0 without an explicit stated reason

---

## Phase 6 -- Kill-Barrier Trajectory Verdict

**KILL-BARRIER TRAJECTORY VERDICT**

This section is distinct from the Phase 5 per-persona grid. The trajectory verdict must be
derived from the structural persistence property, not inferred from the grid.

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence referencing the persistence property from Phase 4 by
name. Must explain why the barrier moves (or does not move) in this direction structurally.]

**Relationship to Phase 5 grid:** [One sentence: alignment or divergence with per-persona
trajectories, and why.]

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas
- Kill-barrier trajectory direction from Phase 6
- 1--2 sentence rationale connecting distribution, trajectory, and confirmed kill barrier

---

## AMEND

Select the persona most exposed to the confirmed kill barrier.

- **Focus persona:** [name]
- **Switching cost (sharpened):** [most precise quantified value for this persona]
- **Kill barrier for this persona:** [one sentence naming the barrier and why it is most acute
  for them]
- **Mitigation:** [one concrete intervention -- explain why this lever addresses the structural
  persistence property from Phase 4, not just what the intervention does]

---

### V-23: "Checkpoint Verdict" Phrasing

**Axis:** Phrasing register -- the kill barrier temporal persistence test is framed as a
pass/fail checkpoint the model must resolve with a verdict word (PROCEED or RESELECT)
**Hypothesis:** Framing the binary gate as a named checkpoint with an explicit verdict word
(PROCEED / RESELECT) rather than a YES/NO table will close C-20 through a different register.
The checkpoint framing makes the binary gate a model behavior requirement rather than a
formatting requirement -- the model must choose PROCEED or RESELECT before any subsequent
phase appears. Expected: same ceiling as V-22 for C-20; the register difference may affect
how models handle ambiguous barriers that partially satisfy either horizon.

---

You are running **validate-inertia** for: {{topic}}

Stress-test adoption inertia. Why would users NOT adopt this feature even if it works perfectly?

---

## Phase 1 -- Persona Identification

Name 2--4 user personas. Each must have:

- **Name and role** -- specific title or function, not a category
- **Current workaround** -- the actual tool or method they use today (name it)
- **Outcome they optimize for** -- what the current workaround delivers

---

## Phase 2 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof req. (named threshold) | Learning curve |
|---------|---------------------------------|--------------------|----------------------------|-------------------------------|-------------------------------------|---------------|

- **Switching cost:** Measurable value required. Qualitative descriptions alone fail.
- **Social proof req.:** Name a specific threshold or condition. Binary Y/N fails.
- **Habit lock-in:** Name the specific repeated behavior.

---

## Phase 3 -- Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

One sentence per score naming the primary inertia driver. Every Phase 1 persona scored
individually. No shared scores.

---

## Phase 4 -- Kill Barrier

Name exactly one adoption killer -- the barrier that would block adoption even if all other
inertia were resolved.

- **Kill barrier:** [name it]
- **Structural persistence:** [the structural property that prevents self-resolution -- not
  familiarity]
- **Most exposed persona:** [name]

**Kill-barrier qualification checkpoint:**

Before proceeding, answer these two questions:

1. Does this barrier exist today (T=0)? ___
2. Does this barrier persist at T=18mo without deliberate structural intervention? ___

**Checkpoint verdict:** Write one of the following words on its own line:

- **PROCEED** -- if and only if both answers are YES
- **RESELECT** -- if either answer is NO

If your verdict is **RESELECT**: name a replacement barrier and re-run this phase from the
barrier identification step. Do not write Phase 5 until your checkpoint verdict is PROCEED.

---

## Phase 5 -- Per-Persona Adoption Timeline

For the confirmed kill barrier and at least two personas, project inertia across three
horizons:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat
- T=6mo and T=18mo cannot copy T=0 without an explicit stated reason

---

## Phase 6 -- Kill-Barrier Trajectory Verdict

**KILL-BARRIER TRAJECTORY VERDICT**

This section is distinct from the Phase 5 grid. The verdict is about the kill barrier itself,
not a summary of the per-persona trajectories.

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence referencing the persistence property from Phase 4 by
name and explaining why the barrier moves (or does not) in this direction over the time
horizon.]

**Relationship to Phase 5:** [One sentence confirming alignment or stating divergence.]

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas
- Kill-barrier trajectory direction from Phase 6
- 1--2 sentence rationale connecting score distribution, trajectory, and the confirmed kill
  barrier

---

## AMEND

Select the persona most exposed to the confirmed kill barrier.

- **Focus persona:** [name]
- **Switching cost (sharpened):** [most precise quantified value for this persona]
- **Kill barrier for this persona:** [one sentence naming the barrier and why it persists for
  them specifically]
- **Mitigation:** [one concrete intervention -- explain why this lever addresses the structural
  persistence property from Phase 4, not just what the intervention does]

---

### V-24: Disqualifier + Gate Combination

**Axis:** Combination -- output format (C-19 literal disqualifier) + lifecycle emphasis
(C-20 binary reselection gate)
**Hypothesis:** Combining V-21's literal "does not satisfy" sentence requirement (Phase 5)
with V-22's binary YES/NO confirmation table and reselect gate (Phase 4) closes both C-19 and
C-20 in one variation while keeping other aspirationals at incidental coverage levels. The two
mechanisms occupy different phases and do not compete. Expected: C-19 and C-20 both reach full
pass; C-18 receives incidental coverage through the kill-barrier trajectory verdict section;
other aspirationals depend on whether standard phase structure happens to satisfy them.

---

You are running **validate-inertia** for: {{topic}}

Stress-test adoption inertia. Why would users NOT adopt this feature even if it works perfectly?

---

## Phase 1 -- Persona Identification

Name 2--4 user personas. Each must have:

- **Name and role** -- specific title or function, not a category
- **Current workaround** -- the actual tool or method they use today (name it)
- **Outcome they optimize for** -- what the current workaround successfully delivers

---

## Phase 2 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof req. (named threshold) | Learning curve |
|---------|---------------------------------|--------------------|----------------------------|-------------------------------|-------------------------------------|---------------|

- **Switching cost:** Measurable value required -- time, steps, effort rating (1--10), or
  relative measure. Qualitative descriptions alone fail.
- **Social proof req.:** Name a specific threshold or condition. Binary Y/N fails.
- **Habit lock-in:** Name the specific repeated behavior. "General familiarity" fails.

---

## Phase 3 -- Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

One sentence per score naming the primary inertia driver. Every Phase 1 persona scored
individually. No shared scores.

---

## Phase 4 -- Kill Barrier with Binary Confirmation Gate

Identify the single adoption killer.

- **Kill barrier:** [name it precisely]
- **Structural persistence:** [the structural property that prevents self-resolution -- not
  familiarity, but the structural constraint that keeps this barrier alive as the product
  matures]
- **Most exposed persona:** [name]

**Temporal persistence confirmation table:**

| Question | Your answer (write YES or NO) |
|----------|-------------------------------|
| Does this barrier exist today (T=0)? | |
| Does this barrier persist at T=18mo, absent deliberate structural intervention targeting the persistence property above? | |

**Gate rule:** If either answer is NO -- this barrier does not qualify as the kill barrier.
Return to the top of this phase, select a different barrier, and complete the confirmation
table again. Do not proceed to Phase 5 until both answers are YES.

Label the confirmed barrier **CONFIRMED KILL BARRIER** before proceeding.

---

## Phase 5 -- Per-Persona Adoption Timeline

**Section header: PER-PERSONA ADOPTION TIMELINE**

Required disqualifier -- write this sentence before presenting the grid:

> "This section does not satisfy the kill-barrier trajectory verdict requirement. That output
> belongs exclusively to Phase 6."

Then present the timeline grid for the confirmed kill barrier and at least two personas:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat
- T=6mo and T=18mo cannot copy T=0 without an explicit stated reason

---

## Phase 6 -- Kill-Barrier Trajectory Verdict

**KILL-BARRIER TRAJECTORY VERDICT**

This section produces the dedicated verdict for the kill barrier's own time-sensitivity. It
is not a summary of Phase 5 and is not satisfied by pointing to Phase 5.

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence referencing the persistence property from Phase 4 by
name. Must explain the trajectory direction in terms of the structural mechanism, not from
the per-persona grid.]

**Relationship to Phase 5 grid:** [One sentence confirming alignment or stating divergence
with per-persona trajectories, and why.]

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas
- Kill-barrier trajectory direction from Phase 6
- 1--2 sentence rationale connecting distribution, trajectory, and confirmed kill barrier

---

## AMEND

Select the persona most exposed to the confirmed kill barrier.

- **Focus persona:** [name]
- **Switching cost (sharpened):** [most precise quantified value for this persona]
- **Kill barrier for this persona:** [one sentence restating the barrier and why it persists
  specifically for them]
- **Mitigation:** [one concrete intervention -- explain why this lever addresses the structural
  persistence property from Phase 4, not just what the intervention does]

---

### V-25: Full Integration -- All Twelve Aspirationals

**Axis:** Combination -- all twelve aspirational axes (C-09 through C-20)
**Hypothesis:** Extending V-20 (which covered C-09 through C-18 with structural enforcement
across seven phases) with one addition -- the literal "does not satisfy" disqualifier sentence
in Phase 6 Part A (C-19) -- produces maximum structural coverage for the v5 rubric. C-20 is
already present in V-20's Phase 5 temporal persistence gate; V-25 keeps it and tightens the
gate label to match the C-20 pass condition exactly (explicit binary table, explicit gate rule).
Expected ceiling: 200/200 if all phases execute cleanly without degradation.

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

**Competitive strength inventory** -- for each strength the current solution has:

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
