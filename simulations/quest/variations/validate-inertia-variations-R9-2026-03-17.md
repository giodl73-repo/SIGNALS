Written to `simulations/quest/variations/validate-inertia-variations-R9-2026-03-17.md`.

---

## R9 Variations Summary

| # | Label | Axis | Primary target |
|---|-------|------|----------------|
| **V-41** | C-31 appended to CCV | Lifecycle emphasis | C-31 minimal-overhead: audit as CCV subsection |
| **V-42** | C-31 as standalone pre-CCV | Output format | C-31 structural separation from gate |
| **V-43** | C-31 with self-rejection gate | Phrasing register | C-31 behavioral enforcement (CHAIN COMPLETE/BREAK) |
| **V-44** | C-31 declared in preamble | Inertia framing | Preamble row 5 + standalone audit |
| **V-45** | Full integration | All axes | Preamble + Evidence column + CHAIN COMPLETE gate |

---

### Entering R9 diagnosis

V-40 scored 290/290 on R8. Against R9 (310 pts), it inherits C-28/C-29/C-30 clean. The sole gap is **C-31 — Citation chain completeness self-audit**. V-40's Citation Chain Verification is a 6-field production gate; it is not an enumerated audit with binary verdicts per link. V-40 scores 300/310 against R9.

### Four citation chain links the audit must cover

| Link | Source | Consumer | Status at audit time |
|------|--------|----------|---------------------|
| L1 | SCORING INFRASTRUCTURE DECLARED | Phase 4 traces | Retrospective |
| L2 | PERSONA INVENTORY DECLARED | Phase 5(2) | Retrospective |
| L3 | LEVER POINT: [label] | AMEND(d) anchor | Forward commitment |
| L4 | TRAJECTORY VERDICT: [direction] | Phase 7 | Retrospective |

### Design axis per variation

- **V-41** tests whether appending the audit to the existing CCV suffices, or whether models collapse it into the gate they just completed.
- **V-42** separates audit (C-31) and gate (C-24 CCV) into distinct sections with distinct structural functions.
- **V-43** adds a CHAIN COMPLETE/CHAIN BREAK aggregate declaration with a correction loop — converting the audit from observational record into structural enforcement.
- **V-44** front-loads the audit requirement into the Citation Architecture preamble (row 5), applying the same drift-reduction logic that justified the preamble for artifact declarations.
- **V-45** adds a 5-column Evidence column that forces the model to write the actual downstream cite text per link, converting assertion into demonstration.
 a forward commitment (AMEND has not yet been written when the audit runs). The audit confirms that the upstream artifact was correctly produced and commits to exact-copy at the downstream site.

### Key design decisions

**V-41 (single-axis: CCV subsection):** The CCV already requires the model to write exact artifact names in 6 fields. Adding a binary-verdict audit table immediately after the 6-field gate appends C-31 compliance without restructuring the section. The model has just confirmed each artifact name — the audit runs on already-resolved facts. Risk: the audit may be treated as a formality rather than a structural gate, since the CCV gate has already fired.

**V-42 (single-axis: standalone pre-CCV):** Separating the audit from the gate creates distinct structural functions — the audit (C-31) confirms chain integrity; the CCV (C-24 infrastructure) is a production gate that holds the model before AMEND. Placing the audit before the CCV creates a discovery-before-confirmation ordering: the model audits first, then confirms fields. Risk: two sequential sections with overlapping intent may cause the model to merge or abbreviate one.

**V-43 (single-axis: self-rejection gate):** V-42 base plus a required aggregate declaration at the audit close: either "CHAIN COMPLETE: all four links are reference chains" or "CHAIN BREAK: [list failures] — return to Phase [X] and correct before proceeding." The gate converts C-31 from an observational record into a structural correction trigger. Without a correction gate, a model can record a description link as "CHAIN INTEGRITY FAILURE" and proceed; with the gate, CHAIN BREAK fires a return instruction. Tests whether C-31 compliance is more reliable when the audit has enforcement power. Expected: 310/310.

**V-44 (combination: V-43 + preamble declaration):** The Citation Architecture preamble gains a 5th row: "Post-Phase-7 | CITATION CHAIN COMPLETENESS AUDIT | All 4 citation chain links | Binary reference-chain/description-chain verdict; any description link labeled CHAIN INTEGRITY FAILURE." The preamble's drift-reduction argument (front-loaded architecture awareness before any production phase) extends to the audit requirement. If the model reads "produce a CITATION CHAIN COMPLETENESS AUDIT" before Phase 1, the requirement is registered early. Tests whether preamble-declared audit requirements are more reliably executed than production-site-only requirements.

**V-45 (all axes: full integration):** V-44 base with two additions: (1) the audit section uses a precise 4-column table (Source artifact, Consumer site, Link type, Verdict) with explicit CHAIN INTEGRITY FAILURE fill-in for description links; (2) the audit closes with a required aggregate line before the CCV gate: "CITATION CHAIN AUDIT COMPLETE: [CHAIN COMPLETE / CHAIN BREAK: list failures]." The CCV is reinforced with "Do not proceed to AMEND until the CITATION CHAIN COMPLETENESS AUDIT declares CHAIN COMPLETE." C-30 and C-31 together form a complete structural integrity system: the preamble declares what will be produced; the audit verifies what was produced. Expected ceiling: 310/310.

---

### V-41: C-31 Appended to Citation Chain Verification

**Axis:** Lifecycle emphasis — adds a "Citation Chain Completeness Audit" subsection within the existing Citation Chain Verification, immediately after the 6-field gate table. The audit enumerates all four (source → consumer) pairs with binary reference-chain/description-chain verdicts. Description links are labeled CHAIN INTEGRITY FAILURE, not "weaker" or "incomplete." Single axis: only the Citation Chain Verification section is modified from V-40.
**Hypothesis:** The CCV gate already forces the model to name each artifact and confirm each consumption site. The audit runs on resolved facts — the model has just written the artifact names in the 6 fields. Adding binary verdicts as a subsection is minimum overhead: the model already has all the information needed. C-31 requires a named audit with enumerated pairs and binary verdicts; this variation tests whether appending to the CCV produces a compliant audit or whether models treat the subsection as a rephrase of the gate they just completed. Expected: 310/310.

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
INFRASTRUCTURE DECLARED) and Critical workaround satisfaction satisfy the SCORING
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

**Required lever label** (Citation Architecture, Phase 5(3) row): After writing the lever
point description above, write the following on its own line:

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

**Required trajectory label** (Citation Architecture, Phase 6 Part B row): After stating the
trajectory direction and completing Part B above, write the following on its own line:

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
  Part B (e.g., "TRAJECTORY VERDICT: Worsening"). Do not write "Phase 6 Part B." Write the
  exact label.
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

**Gate rule:** Do not proceed to the Citation Chain Completeness Audit until all six fields
are completed with named text. A field that contains "Phase X" or "see above" without the
actual artifact name or label fails the verification. Correct the upstream phase before
proceeding.

---

## Citation Chain Completeness Audit

After completing all six fields above, produce the following audit. This audit enumerates
every (source artifact → consumer site) pair in the citation chain, declares a binary verdict
for each link, and labels any description-based link as a chain integrity failure.

**Audit table:**

| Link | Source artifact | Consumer site | Link type | Verdict |
|------|----------------|---------------|-----------|---------|
| L1 | [write exact Phase 1 artifact name from field (1) above] | Phase 4 methodology traces | [write: Reference-chain OR Description-chain] | [write: PASS or CHAIN INTEGRITY FAILURE] |
| L2 | [write exact Phase 2 artifact name from field (2) above] | Phase 5(2) structural persistence | [write: Reference-chain OR Description-chain] | [write: PASS or CHAIN INTEGRITY FAILURE] |
| L3 | [write exact LEVER POINT label from field (5) above] | AMEND(d) lever anchor | [write: Reference-chain OR Description-chain] | [write: PASS or CHAIN INTEGRITY FAILURE] |
| L4 | [write exact TRAJECTORY VERDICT label from field (6) above] | Phase 7 trajectory cite | [write: Reference-chain OR Description-chain] | [write: PASS or CHAIN INTEGRITY FAILURE] |

**Audit rules:**
- A link is Reference-chain if and only if the downstream consumer copies the upstream artifact
  label verbatim (character-for-character). A link is Description-chain if the downstream
  consumer describes or paraphrases the upstream content rather than copying the label.
- A Description-chain link must be labeled CHAIN INTEGRITY FAILURE, not "weaker" or
  "incomplete."
- L3 is a forward commitment: the LEVER POINT label has been produced; confirm it will be
  copied verbatim in AMEND(d)'s "Lever anchor:" field.
- All four links must appear in the table. An audit that omits any link is incomplete.

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

### V-42: C-31 as Standalone Pre-CCV Section

**Axis:** Output format -- adds a "Citation Chain Completeness Audit" as a dedicated named
section between Phase 7 and the Citation Chain Verification. The CCV is unchanged. The audit
section is independent: it enumerates all four links, provides binary verdicts, labels
description chains as CHAIN INTEGRITY FAILURE, and ends. The audit runs before the CCV gate,
so any description chain discovered is visible before the model writes AMEND field confirmations.
Single axis: only the section order changes from V-41 (audit before CCV rather than appended
to CCV).
**Hypothesis:** Separating audit (C-31) and production gate (C-24 CCV) creates distinct
structural functions. V-41 appends the audit to the CCV, risking collapse into the gate --
the model may treat the audit table as a rephrase of fields it just completed rather than a
fresh enumeration with binary verdicts. V-42 forces the model to produce the audit as a
standalone section before the CCV, separating the discovery act from the confirmation act.
Expected: 310/310.

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

Do not proceed to Phase 1 until this label is written.

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

Do not proceed to Phase 2 until this statement is written.

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

- **Dimension:** The specific axis on which the current solution wins
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

Do not proceed to Phase 3 until every persona's inventory passes all three checks.

**Required inventory label** (Citation Architecture, Phase 2 row): After all persona
inventories pass the completeness gate above, write the following statement on its own line
before Phase 3 begins:

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite this
> Phase 2 output by reference -- naming the specific Durability property from the relevant
> persona's competitive strength inventory to show why the kill barrier structurally persists.
> A Phase 5(2) analysis that references a persona's competitive advantage without naming the
> PERSONA INVENTORY DECLARED entry fails the structural persistence requirement."

Do not proceed to Phase 3 until this statement is written.

---

## Phase 3 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2 competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------------------------|----------------|

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
from Phase 3 for this persona, and (b) states the Phase 1 threshold those values satisfy.
Cite Phase 1 by copying the artifact name "SCORING INFRASTRUCTURE DECLARED." Do not write
"Phase 1." Write the artifact name.

Every Phase 2 persona must be scored individually. A shared blanket score does not pass.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

Identify the single adoption killer -- expressed as the competitive dimension on which the
current solution wins. Use exactly **four labeled sub-parts**. Each must be distinct.

**KILL BARRIER**

**(1) Barrier definition**
[Observable adoption friction as the most exposed persona experiences it. State the competitive
dimension. Do not include cause here.]

**(2) Structural persistence**
[Why this barrier structurally persists. Name the structural mechanism and cite the PERSONA
INVENTORY DECLARED source: reference the specific Durability property by its Phase 2 label.
A structural persistence claim that does not name the PERSONA INVENTORY DECLARED artifact is
a paraphrase chain, not a reference chain.]

**(3) Intervention target**
[The specific lever point that, if addressed, would disrupt the structural persistence
mechanism in (2). Name the target, not the intervention.]

**Required lever label** (Citation Architecture, Phase 5(3) row): After writing the lever
point description above, write the following on its own line:

> **LEVER POINT: [exact label -- 3--7 words naming this specific mechanism]**

Do not proceed to the falsifiability test until the label is written.

**Falsifiability test:** Write the following sentence, completing the bracketed portion:

> "At T=6mo, the absence of this lever being addressed would be observable as: [specific
> behavioral or measurable condition]."

If you cannot complete this sentence with a specific observable condition, replace Part (3),
rewrite the lever label, and repeat the test. Do not write Part (4) until the test passes.

**(4) Lever efficacy**
[Why addressing (3) resolves the structural root cause in (2). Reference (2) by name.]

**Temporal persistence confirmation table:**

| Question | Your answer (write YES or NO) |
|----------|-------------------------------|
| Does this barrier exist today (T=0)? | |
| Does this barrier persist at T=18mo, absent deliberate structural intervention targeting the persistence property in (2)? | |

**Gate rule:** If either answer is NO, return to the top of this phase and select a different
barrier. Do not proceed to Phase 6 until both answers are YES.

Label the confirmed result **CONFIRMED KILL BARRIER**. Name the most exposed persona.

---

## Phase 6 -- Adoption Timeline and Kill-Barrier Trajectory Verdict

**Part A: Per-Persona Adoption Timeline**

**Required disqualifier -- write this sentence before presenting the grid:**

> "This Part A grid captures per-persona trajectory only. It does not satisfy the
> kill-barrier trajectory verdict requirement. That output belongs exclusively to Part B."

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory per persona: Resolving / Stable / Worsening
- At least one trajectory must be non-flat

**Part B: Kill-Barrier Trajectory Verdict (distinct from Part A grid)**

**KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence in terms of the structural persistence property from
Phase 5(2). Must reference that property by name.]

**Relationship to Part A grid:** [One sentence: alignment or divergence from per-persona
trajectories, and why.]

**Required trajectory label** (Citation Architecture, Phase 6 Part B row): After completing
Part B above, write the following on its own line:

> **TRAJECTORY VERDICT: [copy the exact direction word -- Resolving, Stable, or Worsening]**

Do not proceed to Phase 7 until this label is written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

Include:

- Score distribution across personas
- Kill-barrier trajectory direction: copy the exact TRAJECTORY VERDICT label from Phase 6
  Part B. Do not write "Phase 6 Part B." Write the exact label.
- Competitive summary: kill barrier dimension and Phase 2 structural durability basis
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## Citation Chain Completeness Audit

Before the production gate below, enumerate every (source artifact → consumer site) pair in
this output. Assign a binary verdict to each link. Label description-based links explicitly
as CHAIN INTEGRITY FAILURE.

**Audit table:**

| Link | Source artifact | Consumer site | Link type | Verdict |
|------|----------------|---------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Audit rules:**
- Reference-chain: downstream consumer copies the upstream label character-for-character.
- Description-chain: downstream consumer describes or paraphrases. Label verdict CHAIN
  INTEGRITY FAILURE -- not "weaker" or "incomplete."
- L3 is a forward commitment: confirm the LEVER POINT label was produced correctly and will
  be copied verbatim in AMEND(d)'s "Lever anchor:" field.
- All four links must appear. An audit missing any link is incomplete.

---

## Citation Chain Verification

Before writing AMEND, confirm the citation chain is intact by completing all six fields below.

**Chain verification:**

1. **Phase 1 artifact name:** [exact text of boundary artifact from Phase 1]
2. **Phase 2 artifact name:** [exact text of boundary artifact from Phase 2]
3. **Phase 4 citation:** [artifact name from (1) as it appears in Phase 4 traces]
4. **Phase 5(2) citation:** [artifact name from (2) as it appears in Phase 5(2)]
5. **Phase 5(3) lever label:** [exact LEVER POINT label from Phase 5(3)]
6. **Phase 6 Part B trajectory label:** [exact TRAJECTORY VERDICT label]

**Gate rule:** Do not proceed to AMEND until all six fields are completed with named text.
A field that contains "Phase X" or "see above" fails. Correct the upstream phase before
proceeding.

---

## AMEND -- Focus, Quantify, Confirm

Select the persona most exposed to the confirmed kill barrier.

**Focus persona:** [name]

**Switching cost (sharpened):** [most precise quantified value]

**Kill barrier for this persona:** [one sentence -- name the competitive dimension and why
it is most acute for this persona]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete, specific action]
>
> **(b) Root cause addressed:** [structural condition from Phase 5(2) -- name the persistence
> property]
>
> **(c) Causal mechanism:** [why this lever reaches the structural condition in (2). Reference
> the intervention target from Phase 5(3).]
>
> **(d) Confirmation signal at T=6mo:**
>
> "Lever anchor: [copy the exact LEVER POINT label from Phase 5(3) -- confirmed in Citation
> Chain Verification step (5)]."
>
> Then state: [At T=6mo, the absence of this lever would be observable as: [specific
> falsifiable condition]. Must be falsifiable.]

The lever anchor must cite the exact LEVER POINT label. The AMEND section is not complete
without the lever anchor and observable condition.

---

### V-43: C-31 with Self-Rejection Gate

**Axis:** Phrasing register -- V-42 base plus a required aggregate declaration at the close
of the Citation Chain Completeness Audit. After the 4-row audit table, the model must write
either "CHAIN COMPLETE: all four links are reference chains" or "CHAIN BREAK: [list links
labeled CHAIN INTEGRITY FAILURE] -- return to Phase [X] and correct before proceeding." The
aggregate declaration is a structural gate: the model cannot proceed to the CCV unless it has
written CHAIN COMPLETE. Single axis from V-42: only the audit close and its gate instruction
are added.
**Hypothesis:** V-42's audit is observational -- the model records CHAIN INTEGRITY FAILURE
for any description link and continues. A model can comply with C-31 syntactically while
retaining a broken chain. V-43's CHAIN BREAK gate converts the audit from documentation into
enforcement: a description link at audit time triggers a correction loop before the CCV gate
fires. If chain integrity is achievable (V-39/V-40 established it is), the gate should fire
CHAIN COMPLETE for every well-formed execution. If the gate fires CHAIN BREAK, it exposes a
broken link that V-42 would only record. Expected: 310/310.

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

Do not proceed to Phase 1 until this label is written.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework that will govern per-persona
scores in Phase 4.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight (one sentence -- reference a property of this feature or user population) |
|-----------|------------------------------|------------------------------------------------------------------------------------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof requirement
/ Learning curve.

**Score thresholds:**

- **Critical:** [state which dimension combinations produce this tier]
- **High:** [state which combinations]
- **Medium:** [state which combinations]
- **Low:** [state what condition all dimensions must satisfy]

**Required infrastructure label** (Citation Architecture, Phase 1 row): After completing the
dimension weights and score thresholds above, write the following on its own line:

> "SCORING INFRASTRUCTURE DECLARED. All per-persona methodology traces in Phase 4 must cite
> this Phase 1 output by reference -- naming the specific dimension weights and tier thresholds
> declared above to show how each persona's score was produced."

Do not proceed to Phase 2 until this statement is written.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named competitor.

**Persona entry:**

- Name and role (specific, not categorical)
- Current solution (named tool or method)
- Outcome the current solution delivers

**Competitive strength inventory** -- for each persona:

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

- **Durability:** Must reference a structural constraint. **Familiarity is not durability.**
  Name the structural constraint that makes the advantage persist after the feature ships.

**Completeness gate:**

1. All three inventory fields present and populated.
2. No Durability entry uses "familiarity," "habit," "people are used to it," or equivalent.
3. Each Dimension names a specific competitive axis.

Do not proceed to Phase 3 until every persona passes all three checks.

**Required inventory label** (Citation Architecture, Phase 2 row):

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite this
> Phase 2 output by reference -- naming the specific Durability property from the relevant
> persona's competitive strength inventory. A Phase 5(2) analysis that references a persona's
> competitive advantage without naming the PERSONA INVENTORY DECLARED entry fails."

Do not proceed to Phase 3 until this statement is written.

---

## Phase 3 -- Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-----------------------------------|----------------------------|-------------------------------|------------------------------------------|----------------|

- **Switching cost:** Time, steps, or effort rating (1--10). Qualitative-only fails.
- **Social proof threshold:** Named count, role, or condition -- not binary Y/N.

---

## Phase 4 -- Per-Persona Inertia Scores

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

**Methodology trace:** One sentence naming (a) dimension values from Phase 3 and (b) the
Phase 1 threshold those values satisfy. Cite Phase 1 by copying "SCORING INFRASTRUCTURE
DECLARED." Do not write "Phase 1." Every persona scored individually.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

**KILL BARRIER**

**(1) Barrier definition** -- observable adoption friction; state the competitive dimension.

**(2) Structural persistence** -- why the barrier structurally persists. Cite PERSONA
INVENTORY DECLARED: name the specific Durability property by its Phase 2 label.

**(3) Intervention target** -- the specific lever point. Name the target, not the intervention.

**Required lever label:**

> **LEVER POINT: [exact label -- 3--7 words]**

**Falsifiability test:**

> "At T=6mo, the absence of this lever being addressed would be observable as: [specific
> observable condition]."

If you cannot complete with a specific condition, replace Part (3) and repeat. Do not write
Part (4) until the test passes.

**(4) Lever efficacy** -- why (3) resolves the root cause in (2). Reference (2) by name.

**Temporal persistence confirmation:**

| Question | YES or NO |
|----------|-----------|
| Barrier exists at T=0? | |
| Barrier persists at T=18mo without structural intervention? | |

If either answer is NO, return to the top of this phase. Do not proceed to Phase 6 until both
are YES.

**CONFIRMED KILL BARRIER.** Name the most exposed persona.

---

## Phase 6 -- Adoption Timeline and Kill-Barrier Trajectory Verdict

**Part A:**

> "This Part A grid captures per-persona trajectory only. It does not satisfy the
> kill-barrier trajectory verdict requirement. That output belongs exclusively to Part B."

| Persona | T=0 | T=6mo | T=18mo | Trajectory | Driver |
|---------|-----|-------|--------|------------|--------|

At least one trajectory must be non-flat.

**Part B: KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [One sentence -- reference the structural persistence property from
Phase 5(2) by name.]

**Relationship to Part A:** [Alignment or divergence from per-persona trajectories.]

**Required trajectory label:**

> **TRAJECTORY VERDICT: [exact direction word]**

Do not proceed to Phase 7 until this label is written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

- Score distribution across personas
- Kill-barrier trajectory: copy the exact TRAJECTORY VERDICT label. Do not write "Phase 6
  Part B." Write the exact label.
- Competitive summary: kill barrier dimension and Phase 2 structural durability basis
- 1--2 sentence rationale

---

## Citation Chain Completeness Audit

Enumerate every (source artifact → consumer site) pair. Assign binary verdict per link.
Label any description-based link explicitly as CHAIN INTEGRITY FAILURE.

**Audit table:**

| Link | Source artifact | Consumer site | Link type | Verdict |
|------|----------------|---------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Audit rules:**
- Reference-chain: downstream copies label character-for-character.
- Description-chain: downstream describes or paraphrases. Verdict must be CHAIN INTEGRITY
  FAILURE, not "weaker."
- L3 is a forward commitment: confirm the LEVER POINT label is correctly produced and will
  be copied verbatim in AMEND(d).
- All four links must appear.

**Required aggregate declaration:** After completing the table above, write one of the
following on its own line:

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list the link IDs labeled CHAIN INTEGRITY FAILURE, e.g., L2, L4] --
> return to Phase [X] and correct the named artifact before proceeding."

**Gate rule:** Do not proceed to the Citation Chain Verification until this aggregate
declaration is written. If the declaration is CHAIN BREAK, return to the phase named in the
correction instruction, produce the required named artifact, and repeat the audit. Do not
proceed until the aggregate declaration is CHAIN COMPLETE.

---

## Citation Chain Verification

Before writing AMEND, complete all six fields below.

1. **Phase 1 artifact name:** [exact text]
2. **Phase 2 artifact name:** [exact text]
3. **Phase 4 citation:** [artifact name from (1) as it appears in Phase 4 traces]
4. **Phase 5(2) citation:** [artifact name from (2) as it appears in Phase 5(2)]
5. **Phase 5(3) lever label:** [exact LEVER POINT label]
6. **Phase 6 Part B trajectory label:** [exact TRAJECTORY VERDICT label]

Do not proceed to AMEND until all six fields are completed with named text.

---

## AMEND -- Focus, Quantify, Confirm

**Focus persona:** [name -- most exposed to confirmed kill barrier]

**Switching cost (sharpened):** [most precise quantified value]

**Kill barrier for this persona:** [one sentence -- competitive dimension, most acute because]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete action]
>
> **(b) Root cause addressed:** [structural condition from Phase 5(2) by name]
>
> **(c) Causal mechanism:** [why this lever reaches the structural condition. Reference
> Phase 5(3) intervention target.]
>
> **(d) Confirmation signal at T=6mo:**
>
> "Lever anchor: [copy the exact LEVER POINT label from Citation Chain Verification step (5)]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable condition].]

---

### V-44: C-31 Declared in Preamble + Standalone Audit

**Axis:** Inertia framing -- the Citation Architecture preamble gains a 5th row declaring
the Citation Chain Completeness Audit as a required output. The audit section (standalone,
positioned before the CCV, identical to V-42 in format) is now declared before Phase 1 as
part of the architecture design. The CHAIN COMPLETE/CHAIN BREAK gate from V-43 is included.
Single axis from V-43: the preamble table gains one row; the audit section is unchanged.
**Hypothesis:** C-30's drift-reduction argument applies to C-31's audit requirement. In V-43,
the model encounters the audit instruction between Phase 7 and the CCV -- approximately 1500
tokens after the last production phase. A model that has not been primed to expect an audit
at that position may abbreviate or skip it. Declaring the audit in the preamble registers the
requirement before Phase 1, when the model is reading the architecture. The 5th row makes the
audit a declared output of the same authority as the named artifact boundaries. Expected:
310/310.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?
Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. Every phase that produces a named
artifact or cites an upstream artifact operates under the authority of this architecture.
The Citation Chain Completeness Audit is a required output of this architecture -- see row 5.

**Named artifacts and required outputs:**

| # | Phase / Position | Artifact or output | Downstream consumer | Exact-copy or audit requirement |
|---|------------------|--------------------|---------------------|--------------------------------|
| 1 | Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Copy the artifact name, not "Phase 1" |
| 2 | Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Copy the artifact name, not "Phase 2" |
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Copy the exact label string verbatim |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Copy the exact direction word |
| 5 | After Phase 7, before AMEND | "CITATION CHAIN COMPLETENESS AUDIT" | This output itself | Enumerate all 4 (source -> consumer) pairs; binary Reference-chain / Description-chain verdict; any description link labeled CHAIN INTEGRITY FAILURE; close with CHAIN COMPLETE or CHAIN BREAK |

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:** Before Phase 1 begins, write the following on its own line:

> "CITATION ARCHITECTURE DECLARED. All named artifact boundaries, exact-copy requirements,
> and the Citation Chain Completeness Audit requirement are specified in the table above.
> Each phase that produces a named artifact must emit its label exactly as declared. Each
> phase that cites an upstream artifact must copy the upstream label verbatim. The Citation
> Chain Completeness Audit must be produced after Phase 7 and before AMEND."

Do not proceed to Phase 1 until this label is written.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework that will govern per-persona
scores in Phase 4.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight |
|-----------|------------------------------|-----------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof requirement
/ Learning curve.

**Score thresholds:**

- **Critical:** [dimension combinations]
- **High:** [combinations]
- **Medium:** [combinations]
- **Low:** [condition all dimensions must satisfy]

**Required infrastructure label** (Citation Architecture row 1):

> "SCORING INFRASTRUCTURE DECLARED. All per-persona methodology traces in Phase 4 must cite
> this Phase 1 output by reference -- naming the specific dimension weights and tier thresholds
> declared above. Phase 4 traces that reference dimension values without citing thresholds, or
> thresholds without dimension values, will not satisfy the per-score trace requirement."

Do not proceed to Phase 2 until this statement is written.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named competitor.

- Name and role (specific)
- Current solution (named tool or method)
- Outcome the current solution delivers

**Competitive strength inventory:**

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

**Durability must name a structural constraint.** Familiarity is not durability.

**Completeness gate:** For each persona: (1) all three fields present; (2) no Durability uses
familiarity/habit equivalents -- replace with structural constraint; (3) Dimension names a
specific axis. Do not proceed to Phase 3 until all personas pass.

**Required inventory label** (Citation Architecture row 2):

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite this
> Phase 2 output by reference -- naming the specific Durability property by its Phase 2 label.
> A structural persistence claim that does not name the PERSONA INVENTORY DECLARED artifact
> is a paraphrase chain, not a reference chain."

Do not proceed to Phase 3 until this statement is written.

---

## Phase 3 -- Inertia Dimension Analysis

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2) | Switching cost (quantified) | Habit lock-in | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-----------------------------------|----------------------------|---------------|------------------------------------------|----------------|

Switching cost: quantified (time, steps, rating 1--10). Qualitative-only fails.
Social proof threshold: named count, role, or condition. Binary Y/N fails.

---

## Phase 4 -- Per-Persona Inertia Scores

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

Methodology trace: (a) dimension values from Phase 3 + (b) Phase 1 threshold satisfied.
Cite Phase 1 by copying "SCORING INFRASTRUCTURE DECLARED" (Citation Architecture row 1).
Do not write "Phase 1." Write the artifact name. Every persona scored individually.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

**KILL BARRIER** -- four labeled sub-parts; each distinct; do not merge.

**(1) Barrier definition** -- observable phenomenon at the competitive dimension. No cause.

**(2) Structural persistence** -- why the barrier persists. Cite PERSONA INVENTORY DECLARED
(Citation Architecture row 2): name the specific Durability property. A persistence claim
without naming the PERSONA INVENTORY DECLARED artifact is a paraphrase chain.

**(3) Intervention target** -- specific lever point. Name the target, not the intervention.

**Required lever label** (Citation Architecture row 3):

> **LEVER POINT: [exact label -- 3--7 words]**

**Falsifiability test:**

> "At T=6mo, the absence of this lever would be observable as: [specific observable condition]."

Replace Part (3) and repeat if you cannot complete with a specific condition. Do not write
Part (4) until the test passes.

**(4) Lever efficacy** -- why (3) resolves (2). Reference (2) by name. Explain causally.

**Temporal persistence confirmation:**

| T=0 exists? | T=18mo persists without intervention? |
|-------------|--------------------------------------|
| YES / NO | YES / NO |

Both must be YES. If either is NO, return to the top of this phase.

**CONFIRMED KILL BARRIER.** Name the most exposed persona.

---

## Phase 6 -- Adoption Timeline and Kill-Barrier Trajectory Verdict

**Part A disqualifier (required before grid):**

> "This Part A grid captures per-persona trajectory only. It does not satisfy the
> kill-barrier trajectory verdict requirement. That output belongs exclusively to Part B."

| Persona | T=0 | T=6mo | T=18mo | Trajectory | Driver |
|---------|-----|-------|--------|------------|--------|

At least one trajectory non-flat.

**Part B: KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [In terms of Phase 5(2) structural persistence property -- name it.]

**Relationship to Part A:** [Alignment or divergence -- why.]

**Required trajectory label** (Citation Architecture row 4):

> **TRAJECTORY VERDICT: [exact direction word]**

Do not proceed to Phase 7 until written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

- Score distribution
- Kill-barrier trajectory: copy the exact TRAJECTORY VERDICT label (Citation Architecture
  row 4). Do not write "Phase 6 Part B." Write the exact label.
- Competitive summary
- 1--2 sentence rationale

---

## Citation Chain Completeness Audit

**(Citation Architecture row 5 -- required output before AMEND)**

Enumerate every (source artifact → consumer site) pair. Binary verdict per link. Description
links labeled CHAIN INTEGRITY FAILURE.

| Link | Source artifact | Consumer site | Link type | Verdict |
|------|----------------|---------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Rules:** Reference-chain = verbatim label copy. Description-chain = paraphrase or description
= CHAIN INTEGRITY FAILURE (not "weaker"). L3 is a forward commitment. All four links required.

**Required aggregate declaration:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs] -- return to Phase [X] and produce the named artifact before
> proceeding."

Do not proceed to CCV until CHAIN COMPLETE is written. If CHAIN BREAK, correct and re-audit.

---

## Citation Chain Verification

1. **Phase 1 artifact name:** [exact text]
2. **Phase 2 artifact name:** [exact text]
3. **Phase 4 citation:** [how Phase 4 named Phase 1 artifact]
4. **Phase 5(2) citation:** [how Phase 5(2) named Phase 2 artifact]
5. **Phase 5(3) lever label:** [exact LEVER POINT label]
6. **Phase 6 Part B trajectory label:** [exact TRAJECTORY VERDICT label]

Do not proceed to AMEND until all six fields completed with named text.

---

## AMEND -- Focus, Quantify, Confirm

**Focus persona:** [name]

**Switching cost (sharpened):** [quantified value]

**Kill barrier for this persona:** [one sentence -- competitive dimension, most acute because]

**Mitigation:**

> **(a) Intervention:** [one concrete action]
>
> **(b) Root cause addressed:** [structural condition from Phase 5(2) by name]
>
> **(c) Causal mechanism:** [why lever reaches structural condition. Reference Phase 5(3).]
>
> **(d) Confirmation signal:**
>
> "Lever anchor: [copy exact LEVER POINT label from CCV step (5)]."
>
> [At T=6mo, absence of this lever observable as: [specific falsifiable condition].]

---

### V-45: Full Integration -- Preamble + Structured Audit + CHAIN COMPLETE Gate

**Axis:** All axes -- V-44 base (preamble declares audit as row 5) with three additions:
(1) the Citation Architecture preamble explicitly names the audit section as a verification
counterpart to the producing architecture -- "architecture declares what is produced; audit
confirms what was produced"; (2) the audit section uses a structured 5-column table adding
an explicit "Evidence" column requiring the model to write the actual downstream text that
makes each link a reference chain or description chain, not just a verdict; (3) the CHAIN
COMPLETE gate is reinforced with "Do not proceed to CCV until the Citation Chain Completeness
Audit section ends with CHAIN COMPLETE written on its own line."
**Hypothesis:** V-44 provides the preamble declaration and V-43 provides the gate; V-45 adds
an Evidence column that forces the model to write the actual downstream cite text that it is
evaluating. A model writing "Reference-chain" in the verdict column without writing the
evidence may be asserting rather than verifying. The evidence column converts the audit from
a declaration into a demonstration: the model must reproduce the exact downstream label text
to complete the row, making description-chain errors immediately visible. The combination of
front-loaded architecture declaration (C-30) + structured evidence-based audit (C-31) + CHAIN
COMPLETE gate is the ceiling design. Expected: 310/310.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?
Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. This architecture has two structural
functions: (1) it declares every named artifact and exact-copy requirement before any
production phase begins; (2) it declares the Citation Chain Completeness Audit that will
verify the chain after all production phases are complete. Architecture declares what is
produced; the audit confirms what was produced.

**Named artifacts, required outputs, and verification:**

| # | Phase / Position | Artifact or output | Downstream consumer | Requirement |
|---|------------------|--------------------|---------------------|-------------|
| 1 | Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Exact-copy: copy artifact name, not "Phase 1" |
| 2 | Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Exact-copy: copy artifact name, not "Phase 2" |
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: copy the exact label string verbatim |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | 5-column audit table (see below); CHAIN COMPLETE gate before CCV |

**Row 5 audit format:** The CITATION CHAIN COMPLETENESS AUDIT must use the following table
structure for all four links:

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|

- Evidence column: write the actual text from the downstream site that cites the source.
  For L3 (AMEND not yet written), write the exact text that WILL appear in AMEND(d)'s
  "Lever anchor:" field.
- Link type: Reference-chain if the evidence reproduces the source artifact label verbatim;
  Description-chain if the evidence describes or paraphrases.
- Verdict: PASS for Reference-chain; CHAIN INTEGRITY FAILURE for Description-chain.
- After the table, write "CHAIN COMPLETE: all four links are reference chains" or
  "CHAIN BREAK: [list link IDs] -- return to Phase [X] before proceeding."

**Exact-copy rule:** Only reference chains -- verbatim label reproduction -- satisfy the
citation requirements. Description chains are structural failures.

**Structural prohibition:** Do not produce output that would require a downstream phase to
paraphrase. If a phase would produce unnamed prose where this architecture requires a named
artifact, the phase is incomplete. Return and emit the artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4) and the Citation Chain Completeness Audit requirement (row 5).
> All named artifacts must be produced exactly as declared. All downstream cites must copy
> upstream labels verbatim. The audit must be produced after Phase 7 and must declare CHAIN
> COMPLETE before the CCV gate may proceed."

Do not proceed to Phase 1 until this label is written.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight |
|-----------|------------------------------|-----------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof requirement
/ Learning curve.

**Score thresholds:**

- **Critical:** [dimension combinations]
- **High:** [combinations]
- **Medium:** [combinations]
- **Low:** [condition all dimensions must satisfy]

**Required infrastructure label** (Citation Architecture row 1):

> "SCORING INFRASTRUCTURE DECLARED. All per-persona methodology traces in Phase 4 must cite
> this Phase 1 output by reference -- naming the specific dimension weights and tier thresholds
> declared above. Traces that reference dimension values without citing thresholds, or
> thresholds without dimension values, fail the per-score trace requirement."

Do not proceed to Phase 2 until written.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named competitor.

- Name and role (specific)
- Current solution (named tool or method)
- Outcome the current solution delivers

**Competitive strength inventory per persona:**

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

Durability must name a structural constraint. **Familiarity is not durability.** Structural
constraints: technical, organizational, integration-based, or switching-cost-based.

**Completeness gate:** For each persona: (1) all three fields present; (2) no Durability uses
familiarity/habit -- replace with structural constraint; (3) Dimension names a specific axis.
Do not proceed to Phase 3 until all personas pass all three checks.

**Required inventory label** (Citation Architecture row 2):

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite this
> Phase 2 output by reference -- naming the specific Durability property by its Phase 2 label.
> A structural persistence claim that does not name the PERSONA INVENTORY DECLARED artifact
> is a paraphrase chain, not a reference chain."

Do not proceed to Phase 3 until written.

---

## Phase 3 -- Inertia Dimension Analysis

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2) | Switching cost (quantified) | Habit lock-in | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-----------------------------------|----------------------------|---------------|------------------------------------------|----------------|

Switching cost: time, steps, rating 1--10. Qualitative-only fails.
Social proof threshold: named count, role, or condition. Binary Y/N fails.

---

## Phase 4 -- Per-Persona Inertia Scores

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

Methodology trace: (a) name dimension values from Phase 3 + (b) state Phase 1 threshold
satisfied. Cite Phase 1 by copying "SCORING INFRASTRUCTURE DECLARED" (Citation Architecture
row 1). Do not write "Phase 1." Write the artifact name. Every persona scored individually.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

**KILL BARRIER** -- four labeled, distinct sub-parts. Do not merge any two.

**(1) Barrier definition** -- observable adoption friction; state the competitive dimension.
Do not include cause.

**(2) Structural persistence** -- why the barrier persists structurally. Cite PERSONA
INVENTORY DECLARED (Citation Architecture row 2): name the specific Durability property by
its Phase 2 label. A claim without naming the PERSONA INVENTORY DECLARED artifact is a
paraphrase chain.

**(3) Intervention target** -- specific lever point. Name the target, not the intervention.

**Required lever label** (Citation Architecture row 3):

> **LEVER POINT: [exact label -- 3--7 words]**

**Falsifiability test:**

> "At T=6mo, the absence of this lever would be observable as: [specific observable
> behavioral or measurable condition]."

Replace Part (3) and repeat if you cannot produce a specific observable condition. Do not
write Part (4) until the test passes.

**(4) Lever efficacy** -- why addressing (3) resolves (2). Explain causally. Reference (2)
by name.

**Temporal persistence confirmation:**

| T=0 exists? | T=18mo persists without structural intervention? |
|-------------|--------------------------------------------------|
| YES / NO | YES / NO |

Both must be YES to qualify. If either is NO, return to the top of this phase.

**CONFIRMED KILL BARRIER.** Name the most exposed persona.

---

## Phase 6 -- Adoption Timeline and Kill-Barrier Trajectory Verdict

**Part A disqualifier (required before grid):**

> "This Part A grid captures per-persona trajectory only. It does not satisfy the
> kill-barrier trajectory verdict requirement. That output belongs exclusively to Part B."

| Persona | T=0 | T=6mo | T=18mo | Trajectory | Driver of change |
|---------|-----|-------|--------|------------|-----------------|

At least one trajectory non-flat. T=6mo and T=18mo cannot copy T=0 without a stated reason.

**Part B: KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [Reference the structural persistence property from Phase 5(2)
by name. Argue from mechanism, not from the per-persona grid.]

**Relationship to Part A:** [Alignment or divergence -- which structural property drives both,
or why they differ.]

**Required trajectory label** (Citation Architecture row 4):

> **TRAJECTORY VERDICT: [exact direction word -- Resolving, Stable, or Worsening]**

Do not proceed to Phase 7 until written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

- Score distribution (e.g., "2 High, 1 Critical")
- Kill-barrier trajectory: copy the exact TRAJECTORY VERDICT label (Citation Architecture
  row 4). Do not write "Phase 6 Part B." Write the exact label.
- Competitive summary: kill barrier dimension + Phase 2 structural durability basis
- 1--2 sentence rationale tying score distribution, trajectory, and confirmed kill barrier

---

## Citation Chain Completeness Audit

**(Citation Architecture row 5 -- required before CCV)**

Produce the 5-column audit table below. For each link, write the actual downstream cite text
in the Evidence column. Assign Link type and Verdict from that evidence.

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [write the exact phrase from your Phase 4 trace that names the Phase 1 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [write the exact phrase from your Phase 5(2) that names the Phase 2 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the exact text that WILL appear in AMEND(d)'s "Lever anchor:" field] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Verdict rules:**
- Reference-chain: the Evidence text reproduces the Source artifact label verbatim
  (character-for-character). Verdict: PASS.
- Description-chain: the Evidence text describes or paraphrases rather than copying. Verdict:
  CHAIN INTEGRITY FAILURE -- not "weaker," not "incomplete."
- L3 evidence: write the exact "Lever anchor: [LEVER POINT label]" text that will appear in
  AMEND(d). This is a forward commitment. If you would paraphrase the label in AMEND(d),
  correct it now before proceeding.

**Required aggregate declaration on its own line:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs with CHAIN INTEGRITY FAILURE, e.g., L2] -- return to Phase
> [X] and produce the required named artifact before re-auditing."

**Gate rule:** Do not proceed to the Citation Chain Verification until CHAIN COMPLETE is
written on its own line. If CHAIN BREAK is written, return to the named phase, correct the
artifact, and re-run this audit from the top. Do not proceed until the audit closes with
CHAIN COMPLETE.

---

## Citation Chain Verification

Before writing AMEND, complete all six fields with named text.

1. **Phase 1 artifact name:** [exact text produced in Phase 1]
2. **Phase 2 artifact name:** [exact text produced in Phase 2]
3. **Phase 4 citation:** [exact artifact name from (1) as it appears in Phase 4 traces]
4. **Phase 5(2) citation:** [exact artifact name from (2) as it appears in Phase 5(2)]
5. **Phase 5(3) lever label:** [exact LEVER POINT label]
6. **Phase 6 Part B trajectory label:** [exact TRAJECTORY VERDICT label]

A field containing "Phase X" or "see above" without the actual artifact name fails.
Correct the upstream phase before proceeding. Do not write AMEND until all six fields pass.

---

## AMEND -- Focus, Quantify, Confirm

**Focus persona:** [name -- most exposed to confirmed kill barrier]

**Switching cost (sharpened):** [most precise quantified value]

**Kill barrier for this persona:** [one sentence -- competitive dimension, most acute because]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete action]
>
> **(b) Root cause addressed:** [name the structural condition from Phase 5(2)]
>
> **(c) Causal mechanism:** [why this lever reaches the structural condition in (2). Reference
> the Phase 5(3) lever point by name.]
>
> **(d) Confirmation signal at T=6mo:**
>
> "Lever anchor: [copy the exact LEVER POINT label from Citation Chain Verification step (5) --
> this must match the Evidence you wrote in the L3 row of the Citation Chain Completeness
> Audit verbatim]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must cite the exact LEVER POINT label. The AMEND section is not complete
without the lever anchor and the observable condition.
