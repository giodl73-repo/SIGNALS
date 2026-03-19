Written to `simulations/quest/variations/validate-inertia-variations-R8-2026-03-17.md`.

---

## R8 Variations Summary

| # | Label | Axis | Primary target |
|---|-------|------|----------------|
| **V-36** | C-28 at Phase 2 boundary | Output format / lifecycle | Phase 2 -> Phase 5(2) link |
| **V-37** | C-29 double-specification at production site | Phrasing register / lifecycle | Phase 5(3) forward-declaration |
| **V-38** | C-28 at Phase 6 Part B boundary | Output format | Phase 6B -> Phase 7 link |
| **V-39** | Full C-28 propagation — all four boundaries | Combination | All links + all consumers |
| **V-40** | Full integration — Citation Architecture preamble | All axes | Meta-artifact + all 21 |

---

### Entering R8 diagnosis

V-35 scored 270/270 on R7. Against the R8 rubric (290 pts), the question is whether C-28 and C-29 are **already satisfied** or whether two unnamed citation boundaries expose gaps:

- **Phase 2 → Phase 5(2):** V-35 requires Phase 5(2) to reference "the relevant Phase 2 durability property by name" — but Phase 2 produces no named boundary artifact. V-36 and V-39 add "PERSONA INVENTORY DECLARED" to close this.
- **Phase 6 Part B → Phase 7:** V-35 requires Phase 7 to mention "trajectory direction from Phase 6 Part B" — but Phase 6 Part B produces no named artifact. V-38 and V-39 add "TRAJECTORY VERDICT: [direction]" to close this.
- **C-29 production-site gap:** V-35's exact-copy instruction appears only in AMEND (consumption). V-37 adds a forward-declaration at Phase 5(3) (production), forcing the model to choose a verbatim-copyable label before proceeding.

### Key design decisions

**V-36 vs V-38 as diagnostic single-axis probes** — if either PARTIAL, the scoring gap is localized. If both pass, C-28's pass condition is narrower than the broad definition suggests.

**V-37 is the only variation that targets production-side C-29** — the hypothesis is that a label chosen with no awareness of the verbatim requirement may be written as a sentence fragment or long phrase that the model naturalistically paraphrases 2000 tokens later.

**V-40's Citation Architecture preamble** introduces a meta-artifact ("CITATION ARCHITECTURE DECLARED") that no prior variation has tested. The table format concentrates all four artifact rows in one place the model reads before writing anything, which may be more reliable than distributed per-phase instructions across a 1500-token output.
l persistence property drawn from Phase 2's
competitive strength inventory. Citation Chain Verification gains a 5th field for the Phase 2
artifact. Tests whether the C-24/C-28 named artifact pattern needs to extend to the Phase 2
-> Phase 5(2) citation link.

**V-37 (single-axis: C-29 production-site forward-declaration):** Adds a forward-declaration
of the exact-copy requirement immediately after the Phase 5(3) LEVER POINT label is produced,
before the falsifiability test: "This label is required verbatim in AMEND(d)'s 'Lever anchor:'
field. Paraphrase or description does not satisfy the requirement. Only the exact string above,
character-for-character." Tests whether specifying the exact-copy constraint at the production
site forces the model to choose a label that can be cited verbatim in AMEND -- improving chain
integrity through production-side awareness, not only consumption-side instruction.

**V-38 (single-axis: C-28 at Phase 6 Part B boundary):** Adds "TRAJECTORY VERDICT:
[Resolving/Stable/Worsening]" as a required named artifact line at the Phase 6 Part B boundary,
immediately after the trajectory direction is stated. Phase 7 is required to copy this exact
label when citing the kill-barrier trajectory direction. Citation Chain Verification gains a
5th field for the Phase 6 Part B artifact. Tests whether C-28 applies to the Phase 6 Part B
-> Phase 7 citation link.

**V-39 (combination: V-36 + V-38 -- full C-28 propagation):** Adds named artifacts at Phase 2
(V-36) and Phase 6 Part B (V-38), completing the set of four named boundary artifacts: Phase 1
("SCORING INFRASTRUCTURE DECLARED"), Phase 2 ("PERSONA INVENTORY DECLARED"), Phase 5(3)
("LEVER POINT: [label]"), Phase 6 Part B ("TRAJECTORY VERDICT: [direction]"). Citation Chain
Verification expands to 6 fields covering all four source boundaries and their downstream
consumers. Exact-copy citation required at all four consumers. Tests whether the full C-28
propagation produces a coherent, self-auditing output.

**V-40 (all 21 -- Citation Architecture preamble):** V-39 base plus a "Citation Architecture"
section before Phase 1 that front-loads the entire citation design: all four named artifacts,
all four downstream consumers, and the exact-copy requirement for each link, in a single table.
The preamble closes with "CITATION ARCHITECTURE DECLARED." -- a meta-artifact that all
subsequent boundary declarations reference as the structural authority. Tests whether
front-loading the full citation architecture reduces per-phase instructional drift, and whether
a meta-artifact declaration is more robust than distributed per-phase instruction.

---

### V-36: C-28 at Phase 2 Boundary

**Axis:** Output format / lifecycle emphasis -- adds a named boundary artifact at Phase 2
completion ("PERSONA INVENTORY DECLARED") and requires Phase 5(2) to cite it by that artifact
name. Single axis: only the Phase 2 -> Phase 5(2) link is modified from V-35.
**Hypothesis:** C-28 requires the named artifact pattern to propagate to every section that
serves as an upstream citation source. V-35 names Phase 1 and Phase 5(3) but not Phase 2,
which is the upstream source for Phase 5(2)'s structural persistence reasoning. If Phase 5(2)
draws from Phase 2 without naming the source artifact, C-28 is not satisfied at that link --
the persistence analysis becomes a paraphrase chain from Phase 2 prose rather than a reference
chain from a named artifact. V-36 closes this gap with a minimal addition. Expected: 290/290.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?
Complete each phase in sequence. Each phase gates the next.

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

**Completeness gate:** Before writing the boundary artifact, verify the following for each
persona:

1. All three inventory fields (Dimension, Advantage, Durability) are present and populated.
2. No Durability entry uses "familiarity," "habit," "people are used to it," or any equivalent.
   If it does, replace it with a structural constraint before proceeding.
3. Each Dimension names a specific competitive axis -- not a category like "usability."

Do not proceed to Phase 3 until every persona's inventory passes all three checks. An
inventory entry that fails any check must be corrected in this phase, not deferred to Phase 5.

**Required inventory label:** After all persona inventories pass the completeness gate above,
write the following statement on its own line before Phase 3 begins:

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite this
> Phase 2 output by reference -- naming the specific Durability property from the relevant
> persona's competitive strength inventory to show why the kill barrier structurally persists.
> A Phase 5(2) analysis that references a persona's competitive advantage without naming the
> PERSONA INVENTORY DECLARED entry fails the structural persistence requirement."

Do not proceed to Phase 3 until this statement is written. The statement is the boundary
marker that closes Phase 2.

---

## Phase 3 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2 competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|----------------|

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
Do not repeat (1). Name the structural mechanism and cite the PERSONA INVENTORY DECLARED
source: reference the specific Durability property by its Phase 2 label. A structural
persistence claim that references Phase 2 content without naming the PERSONA INVENTORY
DECLARED artifact is a paraphrase chain, not a reference chain.]

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

Before writing AMEND, confirm the citation chain is intact by completing all five fields below.
If any field cannot be completed with the named text (must paraphrase or reference by phase
number), return to the phase that produced the unnamed output and correct it before proceeding.

**Chain verification:**

1. **Phase 1 artifact name:** [write the exact text of the boundary artifact produced in
   Phase 1 -- the literal statement written on its own line before Phase 2 began]
2. **Phase 2 artifact name:** [write the exact text of the boundary artifact produced in
   Phase 2 -- the literal statement written on its own line before Phase 3 began]
3. **Phase 4 citation:** [write the artifact name from (1) as it appears in your Phase 4
   methodology traces -- confirm your traces named the artifact, not just cited the phase]
4. **Phase 5(2) citation:** [write the artifact name from (2) as it appears in your Phase 5(2)
   structural persistence analysis -- confirm the analysis named the PERSONA INVENTORY DECLARED
   artifact, not just referenced Phase 2 generically]
5. **Phase 5(3) lever label:** [write the exact LEVER POINT label produced in Phase 5(3)]

**Gate rule:** Do not proceed to AMEND until all five fields are completed with named text.
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
> Chain Verification step (5)]."
>
> Then state: [At T=6mo, the absence of this lever would be observable as: [specific
> condition from the Phase 5(3) falsifiability test, adapted to this persona]. Must be
> falsifiable -- possible to observe it as absent.]

The lever anchor must cite the exact LEVER POINT label. A confirmation signal that paraphrases
the mechanism without citing the label fails C-26 link 4. The AMEND section is not complete
without the lever anchor and observable condition.

---

### V-37: C-29 Double-Specification at Production Site

**Axis:** Phrasing register / lifecycle emphasis -- adds a forward-declaration of the exact-copy
requirement at the Phase 5(3) LEVER POINT production site, before the falsifiability test, in
addition to V-35's existing AMEND(d) instruction. Single axis: only the Phase 5(3) post-label
block is modified from V-35.
**Hypothesis:** V-35's C-29 instruction appears exclusively in AMEND(d) (the consumption site).
A model generating Phase 5(3) may choose a lever label that doesn't survive exact-copy citation
-- e.g., a long phrase with embedded punctuation that the model paraphrases at AMEND time.
Specifying the exact-copy constraint at the production site forces the model to choose a label
it can reproduce verbatim: a 3--7 word phrase that is unambiguous and self-contained. The
production-site constraint acts as a quality gate on the artifact; the AMEND-site constraint
acts as a reproduction gate. Both gates together produce a label that is both well-formed and
faithfully copied. Expected: 290/290.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?
Complete each phase in sequence. Each phase gates the next.

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
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|----------------|

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

**Forward-declaration of exact-copy requirement:** Immediately after writing the LEVER POINT
label above, write the following statement on its own line:

> "This LEVER POINT label will be required verbatim in AMEND(d)'s 'Lever anchor:' field and
> in Citation Chain Verification step (3). Only the exact string above, character-for-character,
> satisfies the exact-copy citation requirement. A paraphrase or description of the mechanism
> does not satisfy the requirement -- the label string itself must appear unchanged."

Before continuing: confirm the label you just produced can survive exact-copy citation. It
must be a standalone phrase of 3--7 words with no embedded punctuation that would change its
identity when copied. If the label does not meet this standard, revise it now before proceeding.
Do not proceed to the falsifiability test with a label you would not reproduce exactly in AMEND.

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
3. **Phase 5(3) lever label:** [write the exact LEVER POINT label produced in Phase 5(3) --
   confirm it is the exact string that will appear in AMEND(d)'s 'Lever anchor:' field]
4. **AMEND(d) anchor:** [write the exact LEVER POINT label from (3) as it will appear in
   the "Lever anchor:" line in AMEND(d) -- confirm it is the same string as (3), not a
   paraphrase]

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
> "Lever anchor: [copy the exact LEVER POINT label from Phase 5(3) -- the same string
> declared in Citation Chain Verification step (3). Character-for-character. A paraphrase of
> the mechanism does not satisfy the exact-copy citation requirement.]"
>
> Then state: [At T=6mo, the absence of this lever would be observable as: [specific
> condition from the Phase 5(3) falsifiability test, adapted to this persona]. Must be
> falsifiable -- possible to observe it as absent.]

The lever anchor must cite the exact LEVER POINT label. A confirmation signal that paraphrases
the mechanism without citing the label fails C-26 link 4. The AMEND section is not complete
without the lever anchor and observable condition.

---

### V-38: C-28 at Phase 6 Part B Boundary

**Axis:** Output format -- adds a named boundary artifact at Phase 6 Part B ("TRAJECTORY
VERDICT: [direction]") and requires Phase 7 to cite it by exact label. Single axis: only Phase
6 Part B and Phase 7 are modified from V-35.
**Hypothesis:** C-28 requires named artifacts at every citation source boundary. Phase 6 Part B
produces the kill-barrier trajectory verdict that Phase 7 cites when stating "Kill-barrier
trajectory direction from Phase 6 Part B." V-35 does not require Phase 6 Part B to produce a
named artifact, so Phase 7 draws from Phase 6 Part B prose -- a paraphrase chain at that link.
V-38 adds the required artifact and exact-copy citation at Phase 7. If C-28 applies to this
link, V-38 closes it. If C-28 is satisfied by Phase 5(3) alone, V-38 is over-specified.
Expected: 290/290.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?
Complete each phase in sequence. Each phase gates the next.

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
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|----------------|

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

**Required trajectory label:** After stating the trajectory direction and completing Part B
above, write the following on its own line:

> **TRAJECTORY VERDICT: [copy the exact direction word from above -- Resolving, Stable, or
> Worsening]**

This label is the named artifact for Phase 6 Part B. Phase 7 must cite this exact label when
stating the kill-barrier trajectory direction. Do not proceed to Phase 7 until this label is
written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas (e.g., "2 High, 1 Critical, 1 Medium")
- Kill-barrier trajectory direction: copy the exact TRAJECTORY VERDICT label from Phase 6
  Part B (e.g., "TRAJECTORY VERDICT: Worsening"). A Phase 7 that references "Phase 6 Part B"
  without copying the exact label is a paraphrase chain, not a reference chain.
- Competitive summary: kill barrier dimension and its Phase 2 structural durability basis
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## Citation Chain Verification

Before writing AMEND, confirm the citation chain is intact by completing all five fields below.
If any field cannot be completed with the named text (must paraphrase or reference by phase
number), return to the phase that produced the unnamed output and correct it before proceeding.

**Chain verification:**

1. **Phase 1 artifact name:** [write the exact text of the boundary artifact produced in
   Phase 1 -- the literal statement written on its own line before Phase 2 began]
2. **Phase 4 citation:** [write the artifact name from (1) as it appears in your Phase 4
   methodology traces -- confirm your traces named the artifact, not just cited the phase]
3. **Phase 5(3) lever label:** [write the exact LEVER POINT label produced in Phase 5(3)]
4. **Phase 6 Part B trajectory label:** [write the exact TRAJECTORY VERDICT label produced
   in Phase 6 Part B]
5. **AMEND(d) anchor:** [write the exact LEVER POINT label from (3) as it will appear in
   the "Lever anchor:" line in AMEND(d)]

**Gate rule:** Do not proceed to AMEND until all five fields are completed with named text.
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

---

### V-39: Full C-28 Propagation -- All Four Boundaries

**Axis:** Output format combination -- V-36 (Phase 2 named artifact) + V-38 (Phase 6 Part B
named artifact) layered onto V-35, which already has Phase 1 and Phase 5(3). All four citation
source boundaries now produce named artifacts. Citation Chain Verification expands to 6 fields.
Exact-copy citation required at all four downstream consumers (Phase 4, Phase 5(2), AMEND,
Phase 7).
**Hypothesis:** If C-28 requires named artifacts at every upstream source boundary in the full
citation chain, V-39 is the exhaustive implementation: four named artifacts, four downstream
cite instructions requiring exact-copy, and a single 6-field verification gate that audits all
four links before AMEND. A model that produces all four artifacts and copies all four labels
correctly cannot silently introduce a paraphrase at any link. Comparison with V-36 and V-38
individually will show whether the full-propagation overhead is necessary or whether the R8
rubric's C-28 pass condition is satisfied by Phase 5(3) alone. Expected: 290/290.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?
Complete each phase in sequence. Each phase gates the next.

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

**Completeness gate:** Before writing the boundary artifact, verify the following for each
persona:

1. All three inventory fields (Dimension, Advantage, Durability) are present and populated.
2. No Durability entry uses "familiarity," "habit," "people are used to it," or any equivalent.
   If it does, replace it with a structural constraint before proceeding.
3. Each Dimension names a specific competitive axis -- not a category like "usability."

Do not proceed to Phase 3 until every persona's inventory passes all three checks. An
inventory entry that fails any check must be corrected in this phase, not deferred to Phase 5.

**Required inventory label:** After all persona inventories pass the completeness gate above,
write the following statement on its own line before Phase 3 begins:

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite this
> Phase 2 output by reference -- naming the specific Durability property from the relevant
> persona's competitive strength inventory to show why the kill barrier structurally persists.
> A Phase 5(2) analysis that references a persona's competitive advantage without naming the
> PERSONA INVENTORY DECLARED entry fails the structural persistence requirement."

Do not proceed to Phase 3 until this statement is written. The statement is the boundary
marker that closes Phase 2.

---

## Phase 3 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2 competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|----------------|

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
Do not repeat (1). Name the structural mechanism and cite the PERSONA INVENTORY DECLARED
source: reference the specific Durability property by its Phase 2 label. A structural
persistence claim that does not name the PERSONA INVENTORY DECLARED artifact is a paraphrase
chain, not a reference chain.]

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

**Required trajectory label:** After stating the trajectory direction and completing Part B
above, write the following on its own line:

> **TRAJECTORY VERDICT: [copy the exact direction word from above -- Resolving, Stable, or
> Worsening]**

This label is the named artifact for Phase 6 Part B. Phase 7 must copy this exact label when
stating the kill-barrier trajectory direction. Do not proceed to Phase 7 until this label is
written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas (e.g., "2 High, 1 Critical, 1 Medium")
- Kill-barrier trajectory direction: copy the exact TRAJECTORY VERDICT label from Phase 6
  Part B (e.g., "TRAJECTORY VERDICT: Worsening"). A Phase 7 that references "Phase 6 Part B"
  without copying the exact label is a paraphrase chain, not a reference chain.
- Competitive summary: kill barrier dimension and its Phase 2 structural durability basis
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## Citation Chain Verification

Before writing AMEND, confirm the citation chain is intact by completing all six fields below.
If any field cannot be completed with the named text (must paraphrase or reference by phase
number), return to the phase that produced the unnamed output and correct it before proceeding.

**Chain verification:**

1. **Phase 1 artifact name:** [write the exact text of the boundary artifact produced in
   Phase 1 -- the literal statement written on its own line before Phase 2 began]
2. **Phase 2 artifact name:** [write the exact text of the boundary artifact produced in
   Phase 2 -- the literal statement written on its own line before Phase 3 began]
3. **Phase 4 citation:** [write the artifact name from (1) as it appears in your Phase 4
   methodology traces -- confirm your traces named the artifact, not just cited the phase]
4. **Phase 5(2) citation:** [write the artifact name from (2) as it appears in your Phase 5(2)
   structural persistence analysis -- confirm the analysis named the PERSONA INVENTORY DECLARED
   artifact, not just referenced Phase 2 generically]
5. **Phase 5(3) lever label:** [write the exact LEVER POINT label produced in Phase 5(3)]
6. **Phase 6 Part B trajectory label:** [write the exact TRAJECTORY VERDICT label produced
   in Phase 6 Part B]

**Gate rule:** Do not proceed to AMEND until all six fields are completed with named text.
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
> Chain Verification step (5)]."
>
> Then state: [At T=6mo, the absence of this lever would be observable as: [specific
> condition from the Phase 5(3) falsifiability test, adapted to this persona]. Must be
> falsifiable -- possible to observe it as absent.]

The lever anchor must cite the exact LEVER POINT label. A confirmation signal that paraphrases
the mechanism without citing the label fails C-26 link 4. The AMEND section is not complete
without the lever anchor and observable condition.

---

### V-40: Full Integration -- Citation Architecture Preamble

**Axis:** All axes -- V-39's full four-boundary propagation plus a "Citation Architecture"
section before Phase 1 that front-loads the entire citation design in a single reference table:
all four named artifacts, all four downstream consumers, and the exact-copy requirement for
each link. The section closes with "CITATION ARCHITECTURE DECLARED." -- a meta-artifact that
subsequent boundary declarations reference as the structural authority.
**Hypothesis:** V-39 embeds C-28/C-29 compliance at six distributed instruction points across
seven phases. A model completing a long output may drift: the Phase 2 instruction for exact-
copy citation at Phase 5(2) was encountered 1000+ tokens before Phase 5(2) is written. V-40
concentrates the full citation architecture into one section read once before any analysis
begins. Per-phase instructions then reference the architecture ("as declared in CITATION
ARCHITECTURE DECLARED") rather than re-specifying the requirement. If front-loading reduces
drift, V-40 produces fewer paraphrase chains at later-phase links. If distributed instruction
is more reliable (each phase self-contained), V-39 and V-40 score equally. The meta-artifact
adds a fifth named boundary artifact, which the model must produce and all phases may reference.
Expected ceiling: 290/290.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?
Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. Every phase that produces a named
artifact or cites an upstream artifact operates under the authority of this architecture.

**Named artifacts this output will produce:**

| Phase | Artifact label | Downstream consumer | Exact-copy requirement |
|-------|---------------|---------------------|------------------------|
| Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Copy the artifact name, not "Phase 1" |
| Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Copy the artifact name, not "Phase 2" |
| Phase 5(3) | "LEVER POINT: [label]" | Citation Chain Verification (5); AMEND(d) | Copy the exact label string verbatim |
| Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7 trajectory cite; Citation Chain Verification (6) | Copy the exact direction word |

**Exact-copy rule:** A downstream cite that describes or paraphrases the upstream artifact's
content is a paraphrase chain. A downstream cite that reproduces the upstream artifact's label
character-for-character is a reference chain. Only reference chains satisfy the citation
requirements for this output.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. If a phase would produce unnamed prose where this
architecture requires a named artifact, that phase has not completed its output. Return to the
phase and emit the required artifact before proceeding.

**Required architecture label:** After reading this section and before Phase 1 begins, write
the following on its own line:

> "CITATION ARCHITECTURE DECLARED. All named artifact boundaries and exact-copy citation
> requirements are specified in the table above. Each phase that produces a named artifact
> must emit its label exactly as declared. Each phase that cites an upstream artifact must
> copy the upstream label verbatim."

Do not proceed to Phase 1 until this label is written. The label is the boundary marker that
closes the Citation Architecture section.

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

**Required infrastructure label** (Citation Architecture, Phase 1 row): After completing the
dimension weights and score thresholds above, write the following statement on its own line
before Phase 2 begins:

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

**Completeness gate:** Before writing the boundary artifact, verify the following for each
persona:

1. All three inventory fields (Dimension, Advantage, Durability) are present and populated.
2. No Durability entry uses "familiarity," "habit," "people are used to it," or any equivalent.
   If it does, replace it with a structural constraint before proceeding.
3. Each Dimension names a specific competitive axis -- not a category like "usability."

Do not proceed to Phase 3 until every persona's inventory passes all three checks. An
inventory entry that fails any check must be corrected in this phase, not deferred to Phase 5.

**Required inventory label** (Citation Architecture, Phase 2 row): After all persona
inventories pass the completeness gate above, write the following statement on its own line
before Phase 3 begins:

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite this
> Phase 2 output by reference -- naming the specific Durability property from the relevant
> persona's competitive strength inventory to show why the kill barrier structurally persists.
> A Phase 5(2) analysis that references a persona's competitive advantage without naming the
> PERSONA INVENTORY DECLARED entry fails the structural persistence requirement."

Do not proceed to Phase 3 until this statement is written. The statement is the boundary
marker that closes Phase 2.

---

## Phase 3 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2 competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|----------------|

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
showing how those inputs produce the assigned score. Cite Phase 1 by copying the artifact name
"SCORING INFRASTRUCTURE DECLARED" (as declared in the Citation Architecture Phase 1 row).
Do not write "Phase 1." Write the artifact name.

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
Do not repeat (1). Name the structural mechanism and cite the PERSONA INVENTORY DECLARED source
(as declared in the Citation Architecture Phase 2 row): copy the artifact name and reference
the specific Durability property from it. Do not write "Phase 2." Write "PERSONA INVENTORY
DECLARED."]

**(3) Intervention target**
[What a mitigation must target -- the specific lever point that, if addressed, would disrupt
the structural persistence mechanism in (2). Name the target, not the intervention. "Better
onboarding" is an intervention; "the moment a user first completes a cross-team workflow
without reverting to their previous tool" is a lever point.]

**Required lever label** (Citation Architecture, Phase 5(3) row): After writing the lever point
description above, write the following on its own line:

> **LEVER POINT: [exact label -- 3--7 words naming this specific mechanism]**

This label is the named artifact for this lever point. The Citation Chain Verification step
(field 5) and AMEND(d) must copy this exact label string verbatim, as declared in the Citation
Architecture Phase 5(3) row. Do not proceed to the falsifiability test until the label is
written.

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

**Required trajectory label** (Citation Architecture, Phase 6 Part B row): After stating the
trajectory direction and completing Part B above, write the following on its own line:

> **TRAJECTORY VERDICT: [copy the exact direction word from above -- Resolving, Stable, or
> Worsening]**

This label is the named artifact for Phase 6 Part B. Phase 7 must copy this exact label, as
declared in the Citation Architecture Phase 6 Part B row. Do not write "Phase 6 Part B." Write
"TRAJECTORY VERDICT: [direction]." Do not proceed to Phase 7 until this label is written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas (e.g., "2 High, 1 Critical, 1 Medium")
- Kill-barrier trajectory direction: copy the exact TRAJECTORY VERDICT label from Phase 6
  Part B (as declared in the Citation Architecture Phase 6 Part B row). Do not write "Phase 6
  Part B." Write the exact label.
- Competitive summary: kill barrier dimension and its Phase 2 structural durability basis
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## Citation Chain Verification

Before writing AMEND, confirm the citation chain is intact by completing all six fields below.
Each field must contain the named text that was actually produced -- not a phase reference and
not a paraphrase. If any field cannot be completed, return to the phase that produced the
unnamed output and correct it before proceeding.

**Chain verification:**

1. **Phase 1 artifact name:** [write the exact text of the boundary artifact produced in
   Phase 1 -- the literal statement written on its own line before Phase 2 began]
2. **Phase 2 artifact name:** [write the exact text of the boundary artifact produced in
   Phase 2 -- the literal statement written on its own line before Phase 3 began]
3. **Phase 4 citation:** [write the artifact name from (1) as it appears in your Phase 4
   methodology traces -- confirm your traces named the artifact, not just cited the phase]
4. **Phase 5(2) citation:** [write the artifact name from (2) as it appears in your Phase 5(2)
   structural persistence analysis -- confirm the analysis named the PERSONA INVENTORY DECLARED
   artifact, not just referenced Phase 2 generically]
5. **Phase 5(3) lever label:** [write the exact LEVER POINT label produced in Phase 5(3) --
   this is the string that will be copied verbatim into AMEND(d)]
6. **Phase 6 Part B trajectory label:** [write the exact TRAJECTORY VERDICT label produced
   in Phase 6 Part B -- this is the string that was copied into Phase 7]

**Gate rule:** Do not proceed to AMEND until all six fields are completed with named text.
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
> "Lever anchor: [copy the exact LEVER POINT label from Citation Chain Verification field (5)
> -- the same string declared in the Citation Architecture Phase 5(3) row. Character-for-
> character. A paraphrase of the mechanism does not satisfy the exact-copy citation requirement
> declared in CITATION ARCHITECTURE DECLARED.]"
>
> Then state: [At T=6mo, the absence of this lever would be observable as: [specific
> condition from the Phase 5(3) falsifiability test, adapted to this persona]. Must be
> falsifiable -- possible to observe it as absent.]

The lever anchor must cite the exact LEVER POINT label. A confirmation signal that paraphrases
the mechanism without citing the label fails C-26 link 4. The AMEND section is not complete
without the lever anchor and observable condition.
