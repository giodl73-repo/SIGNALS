Written to `simulations/quest/variations/validate-inertia-variations-R4-2026-03-17.md`.

---

## validate-inertia Variations R4 — Summary

| # | Label | Axis | Primary targets |
|---|-------|------|-----------------|
| V-16 | Score table with trace column | Output format | C-17 |
| V-17 | Kill-barrier trajectory as a gated phase | Lifecycle emphasis | C-18 |
| V-18 | "Show your work" derivation register | Phrasing register | C-17 (alt mechanism) |
| V-19 | Trace column + trajectory verdict block | Output format + lifecycle | C-17, C-18 |
| V-20 | Full integration — all ten aspirationals | All axes | C-09–C-18 |

---

### Design notes

**V-16 vs V-18 (both target C-17, different mechanisms):**
- V-16 enforces C-17 as a table format requirement — the trace column cannot be omitted because it is a column. Strong structural guarantee, may produce minimal one-liner traces.
- V-18 enforces C-17 as an epistemic obligation — "your reader must re-derive your score from your inputs alone." May produce richer derivations but is more susceptible to partial traces that name values without citing the declared threshold.

**V-17 targets C-18's specific failure mode:** the rubric says "a verdict present in the grid only, without a dedicated kill-barrier trajectory statement, fails." Phase 6 enforces the separation by explicitly stating the per-persona grid (Phase 5) does not satisfy the requirement, and requiring a labeled `KILL-BARRIER TRAJECTORY VERDICT` block with trajectory direction + structural reasoning + relationship note.

**V-20 extends V-15** with the two new mechanisms: trace column in Phase 4 (C-17) and Part B of Phase 6 (C-18). All 10 aspirationals now have structural enforcement — none left to suggestion.
verdict is distinct from the timeline grid. C-18 says "a
verdict present in the grid only, without a dedicated kill-barrier trajectory statement, fails"
— this phase enforces the separation structurally.

**V-18** — Alternate C-17 axis (phrasing register). Instead of a table column, the prompt uses
a conversational "show your work" framing: after each persona score is assigned, the model must
write a derivation sentence the way a math proof works — cite the dimension values first, then
reference the threshold they satisfy. The instruction is framed as "your reader must be able to
re-derive your score from your inputs alone." This is a different structural mechanism from
V-16: V-16 enforces the trace as a table format requirement; V-18 enforces it as an epistemic
obligation in prose. Expected: V-18 may produce richer derivation sentences than V-16 but is
more susceptible to partial traces that name values without referencing the declared threshold.

**V-19** — C-17 + C-18 combination. Takes V-16's score table with trace column (Phase 3) and
V-17's dedicated kill-barrier trajectory verdict phase (Phase 6), combining them into one
variation. The two mechanisms occupy different sections and do not compete. Phase 1 methodology
declaration is required as a prerequisite for C-17. Expected coverage: C-17 (trace column in
score table), C-18 (dedicated trajectory verdict phase), C-09 (methodology declaration
prerequisite). Other aspirationals are incidentally covered to the degree they survive in
standard sections.

**V-20** — Maximum combination. Extends V-15 (which targeted C-09 through C-16) with two new
mechanisms: a methodology trace column in Phase 4 (C-17) and a dedicated kill-barrier
trajectory verdict section within Phase 6 labeled separately from the per-persona timeline grid
(C-18). All ten aspirationals are now structurally enforced. Phase 1 = methodology declaration
(C-09). Phase 2 = competitive inventory with durability (C-11). Phase 3 = inertia table with
named social proof threshold (C-12). Phase 4 = scores with trace column (C-09, C-17). Phase 5
= four-part kill barrier with temporal persistence gate (C-14, C-15). Phase 6 = timeline grid
(C-10) + dedicated kill-barrier trajectory verdict (C-18). AMEND = full causal chain with
confirmation signal (C-13, C-16). Expected ceiling: 180/180 if all phases execute cleanly.

---

### V-16: Score Table with Trace Column

**Axis:** Output format — mandatory Methodology trace column in the per-persona score table
**Hypothesis:** A required table column for the per-persona derivation sentence will close C-17
by making it structurally impossible to assign scores without tracing them to the declared
methodology. The trace must name the persona's dimension values from Phase 2 and reference the
declared threshold from Phase 1. C-09 is a required prerequisite; C-17 is the target.

---

You are running **validate-inertia** for: {{topic}}

Stress-test adoption inertia. Why would users NOT adopt this feature even if it works perfectly?

---

## Phase 1 — Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Reason (one sentence — why this dimension matters more or less for this feature) |
|-----------|------------------------------|---------------------------------------------------------------------------------|

Dimensions to weight: Workaround satisfaction / Switching cost / Habit lock-in / Social proof
requirement / Learning curve.

**Score thresholds** — state the dimension-combination rule that produces each tier:

- **Critical:** [which combination of dimension values at what levels produces this tier]
- **High:** [minimum qualifying combination]
- **Medium:** [minimum qualifying combination]
- **Low:** [all dimensions must satisfy what condition]

Phase 2 cannot begin until the methodology is declared. Per-persona traces in Phase 3 must
reference these thresholds by name.

---

## Phase 2 — Persona Inertia Analysis

Identify 2--4 named personas. For each:

- **Name and role** — specific title or function, not a category
- **Current workaround** — name the actual tool or method (not "ad hoc" — name what they do)
- **Outcome it delivers** — what job the current workaround successfully does for them

For each persona, assess inertia dimensions:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof req. (named threshold) | Learning curve |
|---------|---------------------------------|--------------------|----------------------------|-------------------------------|-------------------------------------|---------------|

Column rules:

- **Switching cost:** Required as a measurable value — time, steps, effort rating (1--10), or
  relative measure. Qualitative-only ("it's hard") fails.
- **Habit lock-in:** Name the specific repeated behavior (keyboard shortcut, naming convention,
  mental model). "General familiarity" is not a named behavior.
- **Social proof req.:** Name a specific threshold or condition — not binary Y/N. Examples:
  "needs 2+ teammates on the same tool before committing," "will adopt solo if manager
  mandates it." Binary answers fail.

---

## Phase 3 — Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

The score table **requires a Methodology trace column**:

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

**Methodology trace** — required format: one sentence that (a) names the specific dimension
values from Phase 2 for this persona, and (b) states the Phase 1 threshold those values satisfy,
showing how those inputs produce the assigned score.

Example of a passing trace: "Sarah's switching cost of 7/10 (High) and Critical workaround
satisfaction match the Phase 1 rule that two or more High-weighted dimensions at H produce a
High score."

Example of a failing trace: "Sarah has high switching costs and values her current workflow,
yielding a High score." — Values implied but not named; Phase 1 threshold not cited.

Every Phase 2 persona must appear. A shared score for multiple personas does not pass.

---

## Phase 4 — Kill Barrier

Identify the single adoption killer — the one factor that would block adoption even if all
other inertia were resolved.

- **Kill barrier:** [name it precisely]
- **Why it survives:** [the structural reason this barrier persists even as the product matures
  and organic adoption accumulates — not that people are used to it, but what structural
  property keeps it alive]
- **Most exposed persona:** [name]

---

## Phase 5 — Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas (e.g., "2 High, 1 Medium, 1 Critical")
- 1--2 sentence rationale connecting the score distribution to the confirmed kill barrier

---

## AMEND

Select the persona most exposed to the kill barrier.

- **Focus persona:** [name]
- **Switching cost (sharpened):** [most precise quantified value for this persona]
- **Kill barrier for this persona:** [one sentence naming the barrier and why it matters
  specifically for them]
- **Mitigation:** [one concrete intervention — explain why this lever addresses the structural
  reason the barrier exists, not just what it does]

---

### V-17: Kill-Barrier Trajectory as a Gated Phase

**Axis:** Lifecycle emphasis — dedicated gated phase for the kill-barrier trajectory verdict,
structurally separated from any per-persona timeline grid
**Hypothesis:** Making the kill-barrier trajectory verdict its own labeled phase — with an
explicit prohibition on substituting the per-persona grid — will close C-18. The phase requires
a trajectory direction label (Resolving / Stable / Worsening) and structural reasoning tied to
the persistence property, not derivable from the grid.

---

You are running **validate-inertia** for: {{topic}}

Stress-test adoption inertia. Why would users NOT adopt this feature even if it works perfectly?

---

## Phase 1 — Persona Identification

Name 2--4 user personas. Each must have:

- **Name and role** — specific title or function, not a category
- **Current workaround** — the actual tool or method they use today (name it — "ad hoc" fails)
- **Outcome they optimize for** — what the current workaround successfully delivers

---

## Phase 2 — Inertia Dimension Analysis

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

## Phase 3 — Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

One sentence per score naming the primary inertia driver.

Every Phase 1 persona must be scored individually. No shared scores.

---

## Phase 4 — Kill Barrier

Identify the single adoption killer — the one barrier that would block adoption even if all
other inertia were resolved.

- **Kill barrier:** [name it precisely]
- **Structural persistence:** [the underlying property that prevents this barrier from
  self-resolving through product maturity or organic adoption — not familiarity, but the
  structural constraint that keeps it alive]
- **Most exposed persona:** [name]

---

## Phase 5 — Per-Persona Adoption Timeline (context only)

For the confirmed kill barrier and the 2 most affected personas, project inertia across three
horizons:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat
- T=6mo and T=18mo cannot copy T=0 without an explicit reason why nothing changes

**This grid captures per-persona trajectory only. It does not satisfy Phase 6. The
kill-barrier trajectory verdict must appear as a distinct labeled output in Phase 6.**

---

## Phase 6 — Kill-Barrier Trajectory Verdict

This phase produces a **dedicated, labeled verdict for the kill barrier's own
time-sensitivity** — separate from the per-persona timeline in Phase 5.

**KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence explaining why the kill barrier moves in this direction
(or does not move) over the time horizon, tied explicitly to the persistence property named in
Phase 4. Must reference that structural property by name. "The barrier will not resolve on its
own" without referencing the structural constraint fails.]

**Relationship to Phase 5 grid:** [One sentence: does this verdict align with or differ from
the per-persona trajectories in Phase 5? If it differs, state why. If it aligns, confirm
which structural property drives both.]

This phase is not satisfied by pointing to Phase 5. The kill-barrier trajectory verdict must
exist as a distinct labeled output here.

---

## Phase 7 — Overall Adoption Inertia Risk

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
- **Mitigation:** [one concrete intervention — explain why this lever addresses the structural
  persistence property from Phase 4, not just what the intervention does]

---

### V-18: "Show Your Work" Derivation Register

**Axis:** Phrasing register — conversational proof-style derivation obligation for per-persona
scores (targets C-17 through epistemic framing rather than table format)
**Hypothesis:** Framing the per-persona derivation as a math-proof obligation ("your reader
must be able to re-derive your score from your inputs alone") will close C-17 through a
different mechanism from V-16's table column. A conversational instruction may produce richer
derivation sentences but is more susceptible to partial traces that name values without
referencing the declared threshold — expect C-17 PARTIAL as the floor, full pass as ceiling.

---

You are running **validate-inertia** for: {{topic}}

Stress-test adoption inertia. Why would users NOT adopt this feature even if it works perfectly?

---

## Phase 1 — Declare Your Scoring Framework

Before you assess any persona, commit to how you will score inertia.

For each of the five dimensions, state: its weight for this feature class (High / Medium / Low)
and one sentence explaining why. Then define the combination of dimension levels that produces
each score tier (Critical, High, Medium, Low).

**Why first:** If you score personas before declaring a methodology, scores become unfalsifiable
— you can always reverse-engineer a justification. Declaring the framework first means every
score can be checked against it.

**Dimension weights and threshold definitions must appear here before any persona is named.**

---

## Phase 2 — Persona Inertia Map

Identify 2--4 named personas. For each:

- Name and role (specific, not categorical)
- Named current workaround (the actual tool or method — "ad hoc" is not a workaround; name
  what they do)
- Outcome the current workaround delivers

Then for each persona, complete the inertia dimension table:

| Persona | Workaround satisfaction (H/M/L) | Basis | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof req. (named threshold) | Learning curve |
|---------|---------------------------------|-------|----------------------------|-------------------------------|-------------------------------------|---------------|

- **Switching cost** must be a measurable value. "It's hard" does not pass.
- **Social proof req.** must name a specific count, role, or condition. Binary Y/N fails.
- **Habit lock-in** must name a specific repeated behavior, not generic familiarity.

---

## Phase 3 — Per-Persona Inertia Scores

Assign each persona a score: Low / Medium / High / Critical.

**Requirement: show your work for every score.**

For each persona, write a derivation sentence following this structure:

> "[Persona]'s [Dimension A] value of [value] and [Dimension B] value of [value] — combined
> with the Phase 1 rule that [quote or paraphrase the relevant threshold] — produce a [score]."

Your derivation sentence must:

1. Name at least two dimension values from Phase 2 that are most diagnostic for this persona
2. Reference the specific Phase 1 threshold those values satisfy
3. Be independently verifiable: a reader who knows only Phase 1 and Phase 2 should reach the
   same score without additional context

A derivation that names dimension values without citing the Phase 1 threshold fails. A
derivation that asserts a threshold without naming the dimension values fails. Both are required.

Every Phase 2 persona requires its own derivation. No shared scores.

---

## Phase 4 — Kill Barrier

Name exactly one adoption killer — the single factor that would block adoption even if all
other inertia were resolved.

- **Kill barrier:** [name it]
- **Structural persistence:** [why this barrier does not self-resolve through product maturity,
  adoption accumulation, or improved UX — name the underlying property, not the symptom]
- **Most exposed persona:** [name]

---

## Phase 5 — Overall Risk Verdict

Verdict: Low / Medium / High / Critical.

- Score distribution across personas
- 1--2 sentence rationale connecting the distribution and the confirmed kill barrier

---

## AMEND

Select the persona most exposed to the kill barrier.

- **Focus persona:** [name]
- **Switching cost (sharpened):** [most precise quantified value for this persona]
- **Kill barrier for this persona:** [one sentence naming the barrier and why it is most acute
  for them]
- **Mitigation:** [one concrete intervention — explain why this lever reaches the structural
  persistence property from Phase 4, not just what the intervention does]

---

### V-19: Trace Column + Trajectory Verdict Block

**Axis:** Combination — output format (score trace column, C-17) + lifecycle emphasis
(dedicated kill-barrier trajectory verdict, C-18)
**Hypothesis:** Combining V-16's score table trace column (Phase 3) with V-17's dedicated
kill-barrier trajectory verdict phase (Phase 6) closes both C-17 and C-18 in one variation.
C-09 is a prerequisite for C-17. The two mechanisms occupy different sections and do not
compete. Other aspirationals receive incidental coverage from standard section structure.

---

You are running **validate-inertia** for: {{topic}}

Stress-test adoption inertia. Why would users NOT adopt this feature even if it works perfectly?

---

## Phase 1 — Scoring Methodology Declaration

Before assessing any persona, declare the inertia scoring framework.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Reason (one sentence) |
|-----------|------------------------------|-----------------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof requirement
/ Learning curve.

**Score thresholds:**

- **Critical:** [state the dimension-combination rule]
- **High:** [state the minimum qualifying combination]
- **Medium:** [state the minimum qualifying combination]
- **Low:** [state the condition all dimensions must satisfy]

Phase 2 cannot begin until methodology is declared. Per-persona traces in Phase 3 must
reference these thresholds.

---

## Phase 2 — Persona Inertia Analysis

Identify 2--4 named personas. For each:

- Name and role (specific, not categorical)
- Named current workaround (the actual tool or method — "ad hoc" fails)
- Outcome the current workaround delivers

For each persona, complete the inertia dimension table:

| Persona | Workaround satisfaction (H/M/L) | Basis | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof req. (named threshold) | Learning curve |
|---------|---------------------------------|-------|----------------------------|-------------------------------|-------------------------------------|---------------|

- **Switching cost:** Required as a measurable value — time, steps, effort rating (1--10), or
  relative measure. Qualitative descriptions alone fail.
- **Social proof req.:** Name a specific threshold or condition. Binary Y/N fails. Examples:
  "needs 2+ teammates on the same tool," "will adopt solo if manager mandates it."
- **Habit lock-in:** Name the specific repeated behavior. "General familiarity" fails.

---

## Phase 3 — Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

The score table **requires a Methodology trace column**:

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

**Methodology trace** — required format: one sentence that (a) names the specific dimension
values from Phase 2 for this persona, and (b) states the Phase 1 threshold those values satisfy.

Failing trace: "Alex has high switching costs and relies heavily on the current tool, yielding
High." — Dimension values implied, Phase 1 threshold not cited.

Passing trace: "Alex's switching cost of 8/10 (High) and Critical workaround satisfaction
match the Phase 1 rule that two or more High-weighted dimensions at H produce a High score." —
Dimension values named and Phase 1 threshold explicitly cited.

Every Phase 2 persona must appear. No shared scores.

---

## Phase 4 — Kill Barrier

Identify the single adoption killer — the one factor that would block adoption even if all
other inertia were resolved.

- **Kill barrier:** [name it precisely]
- **Structural persistence:** [the underlying property that prevents self-resolution through
  product maturity or organic adoption — not familiarity, but the structural constraint]
- **Most exposed persona:** [name]

---

## Phase 5 — Per-Persona Adoption Timeline (context only)

For the confirmed kill barrier and the 2 most affected personas, project inertia across three
horizons:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat
- T=6mo and T=18mo cannot copy T=0 without an explicit reason

**This grid captures per-persona trajectory only. It does not satisfy Phase 6.**

---

## Phase 6 — Kill-Barrier Trajectory Verdict

**KILL-BARRIER TRAJECTORY VERDICT**

This section produces a dedicated labeled verdict for the kill barrier's own time-sensitivity.
It is not a summary of Phase 5 — it is a verdict about the kill barrier itself.

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence explaining the direction in terms of the structural
persistence property from Phase 4. Must reference that property by name.]

**Relationship to Phase 5 grid:** [One sentence: does this verdict align with or differ from
the per-persona trajectories? If it differs, state why. If it aligns, confirm which structural
property drives both.]

This phase is not satisfied by pointing to Phase 5. The verdict must exist as a labeled output
here.

---

## Phase 7 — Overall Adoption Inertia Risk

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
- **Mitigation:** [one concrete intervention — explain why this lever addresses the structural
  persistence property from Phase 4, not just what the intervention does]

---

### V-20: Full Integration — All Ten Aspirationals

**Axis:** Combination — all ten aspirational axes (C-09 through C-18)
**Hypothesis:** Extending V-15 (which targeted C-09 through C-16) with C-17's score trace
column and C-18's dedicated kill-barrier trajectory verdict produces maximum structural coverage
for the v4 rubric. All ten aspirationals are enforced by format, not suggestion. Expected
ceiling: 180/180 if all phases execute cleanly without degradation.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly? Complete
each phase in sequence. Each phase gates the next.

---

## Phase 1 — Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework that will govern per-persona
scores in Phase 4.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight (one sentence — reference a property of this feature or user population) |
|-----------|------------------------------|------------------------------------------------------------------------------------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof requirement
/ Learning curve.

**Score thresholds** — define the dimension-combination rules that produce each tier:

- **Critical:** [state which dimension combinations produce this tier]
- **High:** [state which combinations produce this tier]
- **Medium:** [state which combinations]
- **Low:** [state what condition all dimensions must satisfy]

Phase 2 cannot begin until methodology is declared. Per-persona traces in Phase 4 must
reference these thresholds and dimension weights.

---

## Phase 2 — Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named competitor.

**Persona entry:**

- Name and role (specific, not categorical)
- Current solution (named tool or method — "ad hoc" is not a solution; name what they do)
- Outcome the current solution delivers

**Competitive strength inventory** — for each strength the current solution has:

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

- **Dimension:** The specific axis on which the current solution wins (zero-setup cost, output
  format compatibility, existing keyboard shortcuts, audit trail depth, etc.)
- **Advantage:** What the current solution does better on that dimension for this persona
- **Durability:** Why this advantage is structurally hard to replicate or displace. Must
  reference a structural constraint — technical, organizational, integration-based, or
  switching-cost-based. **Familiarity is not durability.** "People are used to it" does not
  qualify. Name the structural constraint that makes the advantage persist after the feature
  ships and is known.

A competitive strength without a named structural durability basis must be removed or replaced.

---

## Phase 3 — Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2 competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|---------------|

- **Switching cost:** Time, steps, effort rating (1--10), or relative measure. Required.
  Qualitative descriptions do not pass.
- **Satisfaction basis:** Reference a named competitive strength from Phase 2 — not a vague
  sentiment.
- **Social proof threshold:** Name a specific count, role, or condition — not binary Y/N.
  Examples: "needs 2 colleagues using it for more than one sprint," "will adopt solo if manager
  endorses at team standup." Binary answers fail.

---

## Phase 4 — Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

The score table **requires a Methodology trace column**:

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

**Methodology trace** — required: one sentence that (a) names the specific dimension values
from Phase 3 for this persona, and (b) states the Phase 1 threshold those values satisfy,
showing how those inputs produce the assigned score.

Failing trace: "Jordan has high switching costs and depends on the current tool, yielding
High." — Values not named precisely; Phase 1 threshold not cited.

Passing trace: "Jordan's switching cost of 7/10 (High, Phase 1 weight: High) and Critical
workaround satisfaction satisfy the Phase 1 rule that two High-weighted dimensions at H produce
a High score." — Dimension values named and Phase 1 threshold explicitly cited.

Every Phase 2 persona must be scored individually. A shared blanket score does not pass.

---

## Phase 5 — Kill Barrier: Four-Part Causal Analysis

Identify the single adoption killer — expressed as the competitive dimension on which the
current solution wins. Use exactly **four labeled sub-parts**. Each must be distinct. Do not
merge any two into a single statement.

**KILL BARRIER**

**(1) Barrier definition**
[What the barrier is — the observable adoption friction as the most exposed persona experiences
it. State the competitive dimension. Describe the phenomenon; do not include its cause here.]

**(2) Structural persistence**
[Why this barrier structurally persists — the underlying property from the Phase 2 competitive
inventory that prevents it from self-resolving through product maturity or organic adoption.
Do not repeat (1). Name the structural mechanism and reference the relevant Phase 2 durability
property by name.]

**(3) Intervention target**
[What a mitigation must target — the specific lever point that, if addressed, would disrupt
the structural persistence mechanism in (2). Name the target, not the intervention. "Better
onboarding" is an intervention; "the information gap that makes migration feel irreversible"
is a target.]

**(4) Lever efficacy**
[Why addressing (3) resolves the structural root cause in (2). Explain the causal connection.
Reference (2) by name. "It reduces friction" states a result; explain why this lever reaches
the structural condition named in (2).]

**Temporal persistence test:**

> **T=0 qualification:** Does this barrier exist today? [YES / NO]
>
> **T=18mo qualification:** Does this barrier persist at 18 months — absent a deliberate
> structural intervention targeting the durability property? [YES / NO]
>
> If either is NO: reselect. Only a barrier that passes both horizons qualifies.

Label the confirmed result **CONFIRMED KILL BARRIER**. Name the most exposed persona.

Do not proceed to Phase 6 until the kill barrier passes both temporal qualifications.

---

## Phase 6 — Adoption Timeline and Kill-Barrier Trajectory Verdict

**Part A: Per-persona adoption timeline**

For the confirmed kill barrier and at least two personas, project inertia across three horizons:

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

## Phase 7 — Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas (e.g., "2 High, 1 Critical, 1 Medium")
- Kill-barrier trajectory direction from Phase 6 Part B
- Competitive summary: kill barrier dimension and its Phase 2 structural durability basis
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## AMEND — Focus, Quantify, Confirm

Select the persona most exposed to the confirmed kill barrier.

**Focus persona:** [name]

**Switching cost (sharpened):** [most precise quantified value — time, steps, effort rating, or
relative measure]

**Kill barrier for this persona:** [one sentence restating the barrier in terms of this
persona's specific situation — name the competitive dimension and why it is most acute for them]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete, specific action]
>
> **(b) Root cause addressed:** [which structural condition from Phase 5(2) this targets —
> quote or directly reference the persistence property by name]
>
> **(c) Causal mechanism:** [why this lever resolves the structural root cause — the causal
> connection. Reference the intervention target from Phase 5(3). Do not describe what happens;
> explain why this lever reaches the structural condition.]
>
> **(d) Confirmation signal at T=6mo:** [A specific leading indicator or observable condition
> that would confirm the intervention is working at six months. Name what you would measure or
> observe. Vague forward hopes ("users will feel more comfortable") do not qualify. The signal
> must be falsifiable — it must be possible to observe it as absent.]

The confirmation signal must be an observable, not a hope. The AMEND section is not complete
without it.
