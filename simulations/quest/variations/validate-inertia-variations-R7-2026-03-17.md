Written to `simulations/quest/variations/validate-inertia-variations-R7-2026-03-17.md`.

---

## validate-inertia Variations R7 -- Summary

| # | Label | Axis | Primary target |
|---|-------|------|----------------|
| V-31 | Named lever artifact at Phase 5(3) | Output format | C-26 link 3 |
| V-32 | AMEND lever citation by mechanism name | Output format | C-26 link 4 |
| V-33 | Citation chain verification step | Lifecycle emphasis | C-26 (all links) |
| V-34 | Named lever + AMEND lever citation | Output format combination | C-26 links 3+4 |
| V-35 | Full integration -- all nineteen aspirationals | All axes | C-09--C-27 |

---

### Diagnosis entering R7

**C-24, C-25, C-27 already pass in V-30.** The only new gap is **C-26's Phase 5 → AMEND link**.

C-26 requires a four-link citation chain with named anchors at every link:
- Link 1: Phase 1 → Phase 4 (V-30 covers this: instruction names "SCORING INFRASTRUCTURE DECLARED")
- Link 2: Phase 4 → Phase 5 (implicit, no gap)
- Link 3: Phase 5(3) produces a **named lever point artifact** — V-30 produces prose, no label
- Link 4: AMEND(d) names that lever point as its observable anchor — V-30 says "the Phase 5(3) falsifiability test" (phase reference, not named anchor)

---

### Variation logic

**V-31 (single-axis: link 3):** Adds `LEVER POINT: [label]` required format after Phase 5(3) prose. AMEND(d) gets a required `Lever anchor: [copy exact label]` field. Tests whether the formal artifact label is necessary on the production side.

**V-32 (single-axis: link 4):** No Phase 5 label requirement. AMEND(d) must quote the mechanism by name ("The absence of [mechanism name, not 'Phase 5(3)']..."). Tests whether the citation requirement on the AMEND side alone closes link 4 without requiring a Phase 5 label.

**V-33 (single-axis: structural verification):** Adds a post-Phase-7 "Citation Chain Verification" step with four required named fields (Phase 1 artifact, Phase 4 citation, Phase 5(3) lever, AMEND(d) anchor). A gate blocks AMEND until all four fields are completed with named text. Tests whether structural self-verification closes C-26 more reliably than per-phase inline requirements.

**V-34 (combination: links 3+4):** V-31's named lever label + V-31's AMEND lever anchor citation. Closes both sides of the Phase 5 → AMEND link. Excludes V-33's verification step to confirm the two production requirements alone are sufficient.

**V-35 (all 19):** V-30 base + V-34 (named lever + AMEND anchor) + V-33 (citation chain verification). All gaps closed. Expected ceiling: 270/270.
the AMEND-side citation
requirement alone closes C-26 link 4 -- whether the lever mechanism name, quoted inline,
satisfies the "named anchor" criterion without a formal Phase 5 artifact label.

**V-33 (C-26 structural verification):** A different architecture for closing C-26 entirely.
Rather than embedding citation requirements in Phase 4 and AMEND individually, V-33 adds
a post-Phase-7 "Citation Chain Verification" step that requires the model to explicitly
confirm the chain before writing AMEND: write the Phase 1 artifact name, write how it appears
in Phase 4, write the Phase 5(3) lever mechanism name, write how it appears in AMEND(d). A
model that cannot complete any link must go back and correct it. This tests whether structural
self-verification closes C-26 more reliably than per-phase inline requirements.

**V-34 (C-26 full chain -- V-31 + V-32 combined):** The minimal combination that closes both
C-26 links 3 and 4. Phase 5(3) produces "LEVER POINT: [name]" and AMEND(d) is required to
cite that name. The two requirements are in different phases and do not compete. The
verification step from V-33 is excluded so that C-26 closure depends only on the two
production requirements.

**V-35 (all 19):** V-30 + V-31 + V-32 + V-33. All four new criteria (C-24, C-25, C-26,
C-27) are covered: C-24 via the Phase 1 boundary artifact from V-30; C-25 via V-30's
prohibition gates; C-26 via V-34's named lever chain; C-27 via V-30's falsifiability test
with rejection clause. V-33's citation chain verification adds a structural confirmation step
that makes chain breaks detectable before AMEND is written. Expected ceiling: 270/270.

---

### V-31: Named Lever Artifact at Phase 5(3)

**Axis:** Output format -- Phase 5(3) must produce a named, citable lever artifact label
before the falsifiability test, analogous to "SCORING INFRASTRUCTURE DECLARED" at Phase 1
**Hypothesis:** V-30's Phase 5(3) produces prose whose lever description cannot be cited by
name in AMEND without paraphrasing. Adding a required "LEVER POINT: [name]" label after the
prose forces Phase 5(3) to produce a named artifact. The corresponding AMEND(d) requirement
to write "Lever anchor: [copy LEVER POINT label]" creates the named citation link. C-26 link
3 (Phase 5(3) produces named lever point) and link 4 (AMEND names it as observable anchor)
both close. C-26 PASS expected; C-27 coverage preserved from V-30.

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

Do not proceed to Phase 2 until this statement is written. The statement is the boundary
marker that closes Phase 1.

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

Do not proceed to Phase 3 until every persona's inventory passes all three checks. An
inventory entry that fails any check must be corrected in this phase, not deferred to Phase 5.

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

Passing trace: "Jordan's switching cost of 7/10 (High, Phase 1 weight: High per SCORING
INFRASTRUCTURE DECLARED) and Critical workaround satisfaction satisfy the Phase 1 SCORING
INFRASTRUCTURE DECLARED rule that two High-weighted dimensions at H produce a High score."

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

**Required lever label:** After writing the lever point description above, write the following
on its own line:

> **LEVER POINT: [exact label -- 3--7 words naming this specific mechanism]**

This label is the named artifact for this lever point. It will be cited by name in AMEND(d).
Use the same label text consistently. Do not proceed to the falsifiability test until the
label is written.

**Falsifiability test (required before writing Part (4)):** Write the following sentence,
completing the bracketed portion:

> "At T=6mo, the absence of this lever being addressed would be observable as: [specific
> behavioral or measurable condition]."

If you cannot complete this sentence with a specific observable condition -- your Part (3)
intervention target is too general. Replace Part (3) with a more specific mechanism, rewrite
the lever label, and repeat the falsifiability test. Do not write Part (4) until the test
produces a specific observable condition. The AMEND confirmation signal in step (d) must cite
the LEVER POINT label directly.

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
> **(d) Confirmation signal at T=6mo:** Write the following before stating the observable
> condition:
>
> "Lever anchor: [copy the exact LEVER POINT label from Phase 5(3)]."
>
> Then state: [At T=6mo, the absence of this lever would be observable as: [specific
> condition from the Phase 5(3) falsifiability test, adapted to this persona]. Must be
> falsifiable -- possible to observe it as absent.]

The lever anchor must appear as written above, citing the exact LEVER POINT label text from
Phase 5(3). A confirmation signal that restates the mechanism without citing the label earns
PARTIAL on C-26. The AMEND section is not complete without the lever anchor and observable
condition.

---

### V-32: AMEND Lever Citation by Mechanism Name

**Axis:** Output format -- AMEND(d) is required to cite the Phase 5(3) lever mechanism by
its own descriptive name, not by phase reference, creating the named anchor citation from the
AMEND direction without requiring Phase 5(3) to produce a formal labeled artifact
**Hypothesis:** V-30's AMEND(d) says "the observable condition named in the Phase 5(3)
falsifiability test" -- this is a phase reference. If a model writes correct content derived
from Phase 5(3) but without naming the specific lever mechanism, it produces a paraphrase
chain and fails C-26 link 4. Requiring AMEND(d) to write "The absence of [lever mechanism
name -- not 'Phase 5(3)'] at T=6mo would be observable as: [condition]" forces mechanism
naming. This variation tests whether the AMEND-side citation requirement alone closes C-26
link 4 without requiring a formal Phase 5 artifact label. If C-26 PASS is achievable without
the V-31 formal label, V-31's added structure is unnecessary overhead; if PARTIAL, the label
is needed.

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

Do not proceed to Phase 2 until this statement is written. The statement is the boundary
marker that closes Phase 1.

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

Do not proceed to Phase 3 until every persona's inventory passes all three checks. An
inventory entry that fails any check must be corrected in this phase, not deferred to Phase 5.

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
without reverting to their previous tool" is a lever point. Be specific enough that the
absence of this lever being addressed would be observable at T=6mo.]

**Falsifiability test (required before writing Part (4)):** Write the following sentence,
completing the bracketed portion:

> "At T=6mo, the absence of this lever being addressed would be observable as: [specific
> behavioral or measurable condition]."

If you cannot complete this sentence with a specific observable condition -- your Part (3)
intervention target is too general. Replace Part (3) with a more specific mechanism and repeat
the falsifiability test. Do not write Part (4) until the test produces a specific observable
condition. The AMEND confirmation signal in step (d) must name this specific lever mechanism
directly -- not cite "Phase 5(3)."

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
> **(d) Confirmation signal at T=6mo:** Write the observable condition using this form:
>
> "The absence of [describe the specific Phase 5(3) lever mechanism by its own name -- do
> not write 'Phase 5(3)' or 'the falsifiability test'; name the mechanism itself] at T=6mo
> would be observable as: [specific behavioral or measurable condition]."
>
> The lever mechanism must be named here by description, not by phase reference. A
> confirmation signal that writes "the Phase 5(3) lever" instead of naming the mechanism
> earns PARTIAL on C-26.

The confirmation signal must be an observable, not a hope. The AMEND section is not complete
without it.

---

### V-33: Citation Chain Verification Step

**Axis:** Lifecycle emphasis -- a post-Phase-7 structural verification step requires the model
to explicitly name each artifact in the citation chain before AMEND can be written, making
chain breaks detectable and correctable before the final output is produced
**Hypothesis:** V-30 embeds citation requirements in individual phases (Phase 4 instruction
names "SCORING INFRASTRUCTURE DECLARED"; AMEND(d) references "Phase 5(3)"). The chain can
still break silently if any link paraphrases rather than names. A verification step that
requires naming all four chain links explicitly -- Phase 1 artifact, Phase 4 citation, Phase
5(3) lever mechanism, AMEND(d) anchor -- converts C-26 from a distributed requirement into a
single gate. If any link cannot name its upstream source, the model must correct it before
AMEND is written. This approach tests whether structural self-verification is a more reliable
closure mechanism than per-phase inline citation requirements. Expected: C-26 PASS if models
complete the verification step faithfully; if models skip or abbreviate the step, PARTIAL.

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

Do not proceed to Phase 2 until this statement is written. The statement is the boundary
marker that closes Phase 1.

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

Do not proceed to Phase 3 until every persona's inventory passes all three checks. An
inventory entry that fails any check must be corrected in this phase, not deferred to Phase 5.

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

## Citation Chain Verification

Before writing AMEND, confirm the citation chain is intact by completing all four fields below.
If any field cannot be completed with the named text (must paraphrase or reference by phase
number), return to the phase that produced the unnamed output and correct it before proceeding.

**Chain verification:**

1. **Phase 1 artifact name:** [write the exact text of the boundary artifact produced in
   Phase 1 -- the literal statement written on its own line before Phase 2 began]
2. **Phase 4 citation:** [write the artifact name from (1) as it appears in your Phase 4
   methodology traces -- show that your traces named the artifact, not just cited the phase]
3. **Phase 5(3) lever mechanism:** [write the specific lever point mechanism as named or
   described in Phase 5(3) -- the text that AMEND(d) will use as its observable anchor]
4. **AMEND(d) anchor:** [write the exact mechanism text from (3) as it will appear in
   AMEND(d) -- confirm it names the mechanism, not "Phase 5(3)"]

**Gate rule:** Do not proceed to AMEND until all four fields are completed with named text.
A field that contains "Phase X" or "see above" without the actual artifact name or mechanism
description fails the verification. Correct the upstream phase before proceeding.

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
> **(d) Confirmation signal at T=6mo:** [The observable condition from the Phase 5(3)
> falsifiability test, adapted to this persona. Name the specific lever mechanism here --
> use the text confirmed in Citation Chain Verification step (3), not a phase reference.
> Must be falsifiable -- possible to observe it as absent.]

The confirmation signal must name the lever mechanism from the chain verification, not reference
Phase 5(3). The AMEND section is not complete without it.

---

### V-34: Named Lever + AMEND Lever Citation (C-26 Full Chain)

**Axis:** Output format combination -- Phase 5(3) produces a named lever artifact (V-31) and
AMEND(d) is required to cite that lever by its exact label (V-31 AMEND), closing both C-26
links 3 and 4 without a verification step
**Hypothesis:** C-26 links 3 and 4 are independent -- producing a named lever in Phase 5(3)
and requiring AMEND(d) to cite it occupy different output locations and do not compete. V-33's
verification step confirms the chain but does not produce it. V-34 confirms that the two
production requirements alone (named lever label + AMEND lever citation) are sufficient to
close C-26. If V-34 passes C-26 where V-31 and V-32 individually earn PARTIAL, the mechanism
is confirmed: both links must be closed simultaneously. If V-34 passes C-26 where V-33 earns
PARTIAL, the verification step is supplementary, not required.

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

Do not proceed to Phase 2 until this statement is written. The statement is the boundary
marker that closes Phase 1.

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

Do not proceed to Phase 3 until every persona's inventory passes all three checks. An
inventory entry that fails any check must be corrected in this phase, not deferred to Phase 5.

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

Passing trace: "Jordan's switching cost of 7/10 (High, Phase 1 weight: High per SCORING
INFRASTRUCTURE DECLARED) and Critical workaround satisfaction satisfy the Phase 1 SCORING
INFRASTRUCTURE DECLARED rule that two High-weighted dimensions at H produce a High score."

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

**Required lever label:** After writing the lever point description above, write the following
on its own line:

> **LEVER POINT: [exact label -- 3--7 words naming this specific mechanism]**

This label is the named artifact for this lever point. AMEND(d) must cite this exact label
text. Do not proceed to the falsifiability test until the label is written.

**Falsifiability test (required before writing Part (4)):** Write the following sentence,
completing the bracketed portion:

> "At T=6mo, the absence of this lever being addressed would be observable as: [specific
> behavioral or measurable condition]."

If you cannot complete this sentence with a specific observable condition -- your Part (3)
intervention target is too general. Replace Part (3) with a more specific mechanism, rewrite
the lever label, and repeat the falsifiability test. Do not write Part (4) until the test
produces a specific observable condition.

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
> **(d) Confirmation signal at T=6mo:** Write the following before stating the observable
> condition:
>
> "Lever anchor: [copy the exact LEVER POINT label from Phase 5(3)]."
>
> Then state: [At T=6mo, the absence of this lever would be observable as: [specific
> condition from the Phase 5(3) falsifiability test, adapted to this persona]. Must be
> falsifiable -- possible to observe it as absent.]

The lever anchor must appear as written above, citing the exact LEVER POINT label text from
Phase 5(3). A confirmation signal that restates the mechanism in new words without citing the
label earns PARTIAL on C-26. The AMEND section is not complete without the lever anchor and
observable condition.

---

### V-35: Full Integration -- All Nineteen Aspirationals

**Axis:** Combination -- all four new single-axis mechanisms (V-31 named lever artifact +
V-32 mechanism-named AMEND citation + V-33 citation chain verification) layered onto V-30,
which already closed C-09 through C-25 and C-27
**Hypothesis:** V-30 scored at most 230/230 on the v6 rubric and passes C-24, C-25, and C-27
against the v7 rubric. The v7 rubric adds C-26 as the only unclosed gap. V-34 closes C-26
links 3 and 4 (named lever in Phase 5(3) + AMEND lever citation by exact label). V-33 adds a
citation chain verification step between Phase 7 and AMEND that makes any remaining chain
break detectable before AMEND is written. The three additions occupy Phase 5 (lever label),
Phase 7/AMEND boundary (verification step), and AMEND(d) (lever anchor citation). No phase
overlap. V-30's coverage of C-09 through C-25 and C-27 is preserved. Expected ceiling:
270/270.

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

Do not proceed to Phase 2 until this statement is written. The statement is the boundary
marker that closes Phase 1.

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

Do not proceed to Phase 3 until every persona's inventory passes all three checks. An
inventory entry that fails any check must be corrected in this phase, not deferred to Phase 5.

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

Passing trace: "Jordan's switching cost of 7/10 (High, Phase 1 weight: High per SCORING
INFRASTRUCTURE DECLARED) and Critical workaround satisfaction satisfy the Phase 1 SCORING
INFRASTRUCTURE DECLARED rule that two High-weighted dimensions at H produce a High score."

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

**Required lever label:** After writing the lever point description above, write the following
on its own line:

> **LEVER POINT: [exact label -- 3--7 words naming this specific mechanism]**

This label is the named artifact for this lever point. The Citation Chain Verification step
and AMEND(d) must cite this exact label text. Do not proceed to the falsifiability test until
the label is written.

**Falsifiability test (required before writing Part (4)):** Write the following sentence,
completing the bracketed portion:

> "At T=6mo, the absence of this lever being addressed would be observable as: [specific
> behavioral or measurable condition]."

If you cannot complete this sentence with a specific observable condition -- your Part (3)
intervention target is too general. Replace Part (3) with a more specific mechanism, rewrite
the lever label, and repeat the falsifiability test. Do not write Part (4) until the test
produces a specific observable condition.

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

## Citation Chain Verification

Before writing AMEND, confirm the citation chain is intact by completing all four fields below.
If any field cannot be completed with the named text (must paraphrase or reference by phase
number), return to the phase that produced the unnamed output and correct it before proceeding.

**Chain verification:**

1. **Phase 1 artifact name:** [write the exact text of the boundary artifact produced in
   Phase 1 -- the literal statement written on its own line before Phase 2 began]
2. **Phase 4 citation:** [write the artifact name from (1) as it appears in your Phase 4
   methodology traces -- confirm your traces named the artifact, not just cited the phase]
3. **Phase 5(3) lever label:** [write the exact LEVER POINT label produced in Phase 5(3)]
4. **AMEND(d) anchor:** [write the exact LEVER POINT label from (3) as it will appear in
   the "Lever anchor:" line in AMEND(d)]

**Gate rule:** Do not proceed to AMEND until all four fields are completed with named text.
A field that contains "Phase X" or "see above" without the actual artifact name or label fails
the verification. Correct the upstream phase before proceeding.

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
> **(d) Confirmation signal at T=6mo:** Write the following before stating the observable
> condition:
>
> "Lever anchor: [copy the exact LEVER POINT label from Phase 5(3) -- confirmed in Citation
> Chain Verification step (3)]."
>
> Then state: [At T=6mo, the absence of this lever would be observable as: [specific
> condition from the Phase 5(3) falsifiability test, adapted to this persona]. Must be
> falsifiable -- possible to observe it as absent.]

The lever anchor must cite the exact LEVER POINT label. A confirmation signal that paraphrases
the mechanism without citing the label fails C-26 link 4. The AMEND section is not complete
without the lever anchor and observable condition.
