Written to `simulations/quest/variations/validate-inertia-variations-R11-2026-03-17.md`.

---

## R11 Variations Summary

| # | Label | Axis | Primary target | Predicted score |
|---|-------|------|----------------|-----------------|
| **V-51** | Atomic inline Row 5 | C-35 single-axis | Full column spec embedded in Row 5 cell; no pointer subsection | 350/370 |
| **V-52** | Audit-first AMEND derivation | C-36 single-axis | AMEND(d) derives from L3 Evidence column, not CCV | 350/370 |
| **V-53** | AUDIT ARCHITECTURE named block | C-37 single-axis (+C-35 byproduct) | Co-resident block holds duality + inline column spec | 360/370 |
| **V-54** | Atomic + audit-first | C-35 + C-36 combined | Row 5 inline AND audit-first AMEND(d); no named block | 360/370 |
| **V-55** | Full ceiling | C-35 + C-36 + C-37 | AUDIT ARCHITECTURE DECLARED block + audit-first AMEND(d) | 370/370 |

---

### Structural questions under test

**Q1 (C-35, V-51):** V-45's Row 5 says "5-column audit table (see below)" — a pointer to a subsection. C-35 requires the Evidence semantics inline at the declaration site. V-51 eliminates the subsection and embeds the full spec in the Row 5 cell. Single-axis test: does atomic inline Row 5 earn C-35?

**Q2 (C-36, V-52):** V-45's AMEND(d) derives from CCV step (5) and retroactively confirms against the L3 Evidence cell. C-36 requires the derivation direction to be inverted: L3 Evidence → AMEND, with Phase 5(3) reconstruction explicitly prohibited. V-52 restructures AMEND(d) and signals the direction in preamble Row 3. Single-axis test: does audit-first derivation earn C-36?

**Q3 (C-37, V-53):** V-45 satisfies C-33 in the preamble intro and C-34 in the Row 5 subsection — separate structural positions that can be separately dropped. V-53 inserts an AUDIT ARCHITECTURE DECLARED named, gated block after the preamble table holding both C-33 and C-34 co-resident. C-35 is also captured because the block carries the full inline spec without pointer indirection.

**Q4 (C-35 + C-36, V-54):** Tests whether the two independent structural changes (atomic Row 5, audit-first AMEND) compose cleanly without interaction effects. C-37 still fails because the two criteria remain at separate structural positions.

**Q5 (full ceiling, V-55):** AUDIT ARCHITECTURE DECLARED block (C-33 + C-34 + C-35 + C-37) + audit-first AMEND(d) (C-36) = 370/370.
ns. C-37 requires both C-33 and C-34 in one named, gated block. No such block. |

Estimated V-50 against R11: ~350/370 (C-35 PARTIAL=5, C-36 PARTIAL=5, C-37 FAIL=0).

**Three structural questions tested:**

**Q1 (C-35):** V-51 eliminates the subsection entirely and embeds the full column spec +
Evidence semantics in the Row 5 cell. V-47 demonstrated this atomic inline form scores
340/340 on R10. Tests single-axis: does atomic inline Row 5 earn C-35 against R11?

**Q2 (C-36):** V-52 restructures AMEND(d) to derive FROM the L3 Evidence column as the
explicit authority, prohibiting reconstruction from Phase 5(3). Preamble Row 3 signals the
directional requirement. V-48 demonstrated audit-first scores 340/340 on R10. Tests
single-axis: does audit-first AMEND(d) earn C-36 against R11?

**Q3 (C-37):** V-53 introduces the AUDIT ARCHITECTURE DECLARED named block after the preamble
table and before Phase 1, containing both C-33 duality framing and C-34 column structure
(inline, not pointed -- which also satisfies C-35 as a byproduct). V-49 demonstrated the
co-resident block scores 340/340 on R10. Tests single-axis: does the named block earn C-37
(and capture C-35)?

**Q4 (C-35 + C-36):** V-54 composes atomic inline Row 5 and audit-first AMEND(d) without an
AUDIT ARCHITECTURE block. Tests whether the two independent changes compose cleanly.

**Q5 (full ceiling):** V-55 applies all three: AUDIT ARCHITECTURE DECLARED block (satisfies
C-33, C-34, C-35, C-37) + audit-first AMEND(d) (satisfies C-36). Tests the 370/370 ceiling.

---

### V-51: Atomic Inline Row 5

**Axis:** C-35 single-axis. Row 5 cell carries the full 5-column spec and Evidence-column
semantics inline. The "Row 5 audit format" subsection is removed. All other V-45 structure is
preserved: duality framing in preamble introduction; AMEND(d) cites CCV step (5) with the
Evidence verbatim-match requirement.
**Hypothesis:** C-35 requires column names and Evidence semantics at the declaration site
without indirection. V-45's Row 5 cell says "5-column audit table (see below)" and delegates
semantics to a subsection -- a model reading the preamble row may treat the subsection pointer
as deferred content and never follow it. V-51 eliminates the pointer: the full spec fits in
the Row 5 Requirement cell. V-47 demonstrated this inline form scores 340/340 on R10; now
testing whether it earns C-35 (10 pts) while retaining C-34 (column structure declared in
preamble before Phase 1, now the Row 5 cell itself). Expected: 350/370 (adds C-35; C-36 and
C-37 remain unaddressed).

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
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | 5-column table: Source artifact | Consumer site | Evidence [write actual downstream cite text verbatim -- for L3, write the exact "Lever anchor: [LEVER POINT label]" text that will appear in AMEND(d); for L1/L2/L4, write the phrase from the consuming section that names the source artifact character-for-character; write the actual text, not a description] | Link type (Reference-chain if Evidence reproduces source label verbatim; Description-chain if Evidence describes or paraphrases) | Verdict (PASS for Reference-chain; CHAIN INTEGRITY FAILURE for Description-chain -- not "weaker" or "incomplete"); close with CHAIN COMPLETE or CHAIN BREAK gate before CCV |

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

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
- Reference-chain: Evidence reproduces Source artifact label verbatim. Verdict: PASS.
- Description-chain: Evidence describes or paraphrases. Verdict: CHAIN INTEGRITY FAILURE --
  not "weaker," not "incomplete."
- L3 evidence: write the exact "Lever anchor: [LEVER POINT label]" text that will appear in
  AMEND(d). Forward commitment. If you would paraphrase, correct it now.

**Required aggregate declaration on its own line:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs with CHAIN INTEGRITY FAILURE] -- return to Phase [X] and
> produce the required named artifact before re-auditing."

**Gate rule:** Do not proceed to CCV until CHAIN COMPLETE is written. If CHAIN BREAK, correct
and re-audit.

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
Correct the upstream phase before proceeding.

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

---

### V-52: Audit-First AMEND Derivation

**Axis:** C-36 single-axis. AMEND(d) is restructured to derive the lever anchor FROM the L3
Evidence column as the explicit authority, prohibiting reconstruction from Phase 5(3). Preamble
Row 3 updated to signal this directional requirement at architecture-read time. The "Row 5
audit format" subsection is retained (no C-35 change). Duality framing remains in preamble
introduction. No AUDIT ARCHITECTURE DECLARED block (no C-37 change).
**Hypothesis:** V-45's AMEND(d) instruction reads "copy from CCV step (5) -- this must match
the L3 Evidence verbatim." This forward-then-verify direction has a three-site drift surface:
Phase 5(3) -> CCV -> AMEND. C-36 requires collapsing to one step: L3 Evidence -> AMEND.
V-48 demonstrated this restructuring scores 340/340 on R10; now testing whether it earns C-36
(10 pts) under R11. The preamble Row 3 addition ("AMEND(d) must derive lever anchor from L3
Evidence column; do not construct from Phase 5(3)") applies the same drift-reduction logic
that justifies the preamble for artifact declarations. Expected: 350/370 (adds C-36; C-35 and
C-37 remain unaddressed).

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
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: copy the exact label string verbatim. AMEND(d) must derive its lever anchor FROM the L3 Evidence column of the Citation Chain Completeness Audit -- do not construct the anchor from Phase 5(3) independently and verify retroactively; the audit L3 Evidence cell is the derivation source. |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | 5-column audit table (see format below); CHAIN COMPLETE gate before CCV |

**Row 5 audit format:** The CITATION CHAIN COMPLETENESS AUDIT must use the following table
structure for all four links:

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|

- Evidence column: write the actual text from the downstream site that cites the source.
  For L3 (AMEND not yet written), write the exact text that WILL appear in AMEND(d)'s
  "Lever anchor:" field.
- Link type: Reference-chain if Evidence reproduces source label verbatim; Description-chain
  if Evidence describes or paraphrases.
- Verdict: PASS for Reference-chain; CHAIN INTEGRITY FAILURE for Description-chain.
- After the table, write "CHAIN COMPLETE: all four links are reference chains" or
  "CHAIN BREAK: [list link IDs] -- return to Phase [X] before proceeding."

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

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
- Reference-chain: Evidence reproduces Source artifact label verbatim. Verdict: PASS.
- Description-chain: Evidence describes or paraphrases. Verdict: CHAIN INTEGRITY FAILURE --
  not "weaker," not "incomplete."
- L3 evidence: write the exact "Lever anchor: [LEVER POINT label]" text that will appear in
  AMEND(d). Forward commitment. If you would paraphrase, correct it now.

**Required aggregate declaration on its own line:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs with CHAIN INTEGRITY FAILURE] -- return to Phase [X] and
> produce the required named artifact before re-auditing."

**Gate rule:** Do not proceed to CCV until CHAIN COMPLETE is written. If CHAIN BREAK, correct
and re-audit.

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
Correct the upstream phase before proceeding.

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
> Locate the L3 row of the Citation Chain Completeness Audit above. The Evidence column of
> that row contains the lever anchor text you pre-committed to when you wrote the audit. Copy
> it exactly, character-for-character, into the "Lever anchor:" field below. Do not reconstruct
> the label from Phase 5(3) or from CCV step (5). The audit is the derivation authority -- the
> L3 Evidence cell is the source you are copying from.
>
> "Lever anchor: [copy the exact text from the L3 Evidence cell -- do not reconstruct from
> Phase 5(3)]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must reproduce the L3 Evidence cell text exactly. The AMEND section is not
complete without the lever anchor and the observable condition.

---

### V-53: AUDIT ARCHITECTURE Named Block

**Axis:** C-37 single-axis (with C-35 captured as structural byproduct). The AUDIT
ARCHITECTURE DECLARED named block is introduced after the preamble table and before Phase 1.
The block contains: (1) duality framing (C-33 content) and (2) full inline column spec with
Evidence-column semantics (C-34 + C-35 content). The duality sentence is removed from the
preamble introduction. The "Row 5 audit format" subsection is removed. Row 5's Requirement
cell references the AUDIT ARCHITECTURE DECLARED block. A gate condition prevents Phase 1
until the model writes the block. AMEND(d) retains V-45 style (no C-36 change).
**Hypothesis:** C-37 requires C-33 and C-34 to co-reside in a single named, gated artifact,
making simultaneous omission the only non-compliance shape. V-45 satisfies C-33 at the
preamble intro and C-34 at the Row 5 subsection -- separate structural positions that can be
separately dropped. The AUDIT ARCHITECTURE DECLARED block forces co-presence: neither
criterion's content can be emitted without the other because they are in the same required
output unit. V-49 demonstrated this pattern scores 340/340 on R10. Note: the block also
carries the full column spec inline (no pointer), so C-35 passes as a structural byproduct.
Expected: 360/370 (adds C-37 and C-35; C-36 remains unaddressed).

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?
Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. This architecture declares every
named artifact and exact-copy requirement before any production phase begins, and declares
the Citation Chain Completeness Audit that will verify the chain after all production phases
are complete. The structural roles of this preamble and the audit are declared in the AUDIT
ARCHITECTURE DECLARED block below.

**Named artifacts, required outputs, and verification:**

| # | Phase / Position | Artifact or output | Downstream consumer | Requirement |
|---|------------------|--------------------|---------------------|-------------|
| 1 | Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Exact-copy: copy artifact name, not "Phase 1" |
| 2 | Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Exact-copy: copy artifact name, not "Phase 2" |
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: copy the exact label string verbatim |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | See AUDIT ARCHITECTURE DECLARED block below for column structure and Evidence semantics; CHAIN COMPLETE gate before CCV |

---

**AUDIT ARCHITECTURE DECLARED**

This output has two structural artifacts serving distinct roles. The Citation Architecture
preamble (rows 1--5 above) is declarative: it specifies what will be produced and how it
will be cited before any production phase begins. The Citation Chain Completeness Audit is
confirmatory: it verifies what was produced after all production phases are complete. These
roles are structurally distinct. Neither artifact can substitute for or subsume the other.
The preamble cannot confirm chain integrity because it precedes production. The audit cannot
declare artifact names and exact-copy requirements because those must be known before Phase 1.

The Citation Chain Completeness Audit (row 5) must use the following 5-column structure for
all four links: Source artifact | Consumer site | Evidence [write actual downstream cite text
verbatim -- for L3, write the exact "Lever anchor: [LEVER POINT label]" text that will appear
in AMEND(d); for L1/L2/L4, write the phrase from the consuming section that names the source
artifact character-for-character; write the actual text produced, not a description of it] |
Link type [Reference-chain if Evidence reproduces source artifact label verbatim;
Description-chain if Evidence describes or paraphrases] | Verdict [PASS for Reference-chain;
CHAIN INTEGRITY FAILURE for Description-chain -- not "weaker" or "incomplete"]. Close the
audit table with "CHAIN COMPLETE: all four links are reference chains" or "CHAIN BREAK:
[list link IDs] -- return to Phase [X] before proceeding."

Do not proceed to Phase 1 until "AUDIT ARCHITECTURE DECLARED" is written on its own line
above. The block above is the required output. Its presence confirms that both the duality
framing (preamble's declarative role vs. audit's confirmatory role) and the audit column
structure (including Evidence-column semantics) have been declared before Phase 1 begins.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block specifying the audit's structural role and column
> format. All named artifacts must be produced exactly as declared. All downstream cites must
> copy upstream labels verbatim. The audit must be produced after Phase 7 and must declare
> CHAIN COMPLETE before the CCV gate may proceed."

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

Produce the 5-column audit table using the column structure declared in AUDIT ARCHITECTURE
DECLARED above. For each link, write the actual downstream cite text in the Evidence column.
Assign Link type and Verdict from that evidence.

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [write the exact phrase from your Phase 4 trace that names the Phase 1 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [write the exact phrase from your Phase 5(2) that names the Phase 2 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the exact text that WILL appear in AMEND(d)'s "Lever anchor:" field] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Required aggregate declaration on its own line:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs with CHAIN INTEGRITY FAILURE] -- return to Phase [X] and
> produce the required named artifact before re-auditing."

**Gate rule:** Do not proceed to CCV until CHAIN COMPLETE is written. If CHAIN BREAK, correct
and re-audit.

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
Correct the upstream phase before proceeding.

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

---

### V-54: Atomic Inline + Audit-First (C-35 + C-36)

**Axis:** C-35 + C-36 combined. Row 5 cell carries the full column spec and Evidence semantics
inline (no pointer subsection). AMEND(d) is restructured to derive from the L3 Evidence column
as the authority. Duality framing remains in the preamble introduction (no C-37). No AUDIT
ARCHITECTURE DECLARED block. Preamble Row 3 updated to signal audit-first direction.
**Hypothesis:** V-51 demonstrates atomic inline Row 5 satisfies C-35. V-52 demonstrates
audit-first AMEND(d) satisfies C-36. These two changes operate on different structural
positions (preamble Row 5 vs. AMEND(d)) and should not interfere. V-54 tests whether they
compose cleanly. Expected: 360/370 (adds C-35 and C-36; C-37 still fails because duality and
column structure remain at separate structural positions -- preamble introduction vs. Row 5
cell -- not co-resident in a named block).

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
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: copy the exact label string verbatim. AMEND(d) must derive its lever anchor FROM the L3 Evidence column of the Citation Chain Completeness Audit -- the audit is the derivation authority; do not construct from Phase 5(3) and verify retroactively. |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | 5-column table: Source artifact | Consumer site | Evidence [write actual downstream cite text verbatim -- for L3, write the exact "Lever anchor: [LEVER POINT label]" text that will appear in AMEND(d); for L1/L2/L4, write the phrase from the consuming section that names the source artifact character-for-character; write the actual text, not a description] | Link type (Reference-chain if Evidence reproduces source label verbatim; Description-chain if Evidence describes or paraphrases) | Verdict (PASS for Reference-chain; CHAIN INTEGRITY FAILURE for Description-chain -- not "weaker" or "incomplete"); close with CHAIN COMPLETE or CHAIN BREAK gate before CCV |

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

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
- Reference-chain: Evidence reproduces Source artifact label verbatim. Verdict: PASS.
- Description-chain: Evidence describes or paraphrases. Verdict: CHAIN INTEGRITY FAILURE --
  not "weaker," not "incomplete."
- L3 evidence: write the exact "Lever anchor: [LEVER POINT label]" text that will appear in
  AMEND(d). Forward commitment. If you would paraphrase, correct it now before writing AMEND.

**Required aggregate declaration on its own line:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs with CHAIN INTEGRITY FAILURE] -- return to Phase [X] and
> produce the required named artifact before re-auditing."

**Gate rule:** Do not proceed to CCV until CHAIN COMPLETE is written. If CHAIN BREAK, correct
and re-audit.

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
Correct the upstream phase before proceeding.

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
> Locate the L3 row of the Citation Chain Completeness Audit above. The Evidence column of
> that row contains the lever anchor text you pre-committed to when you wrote the audit. Copy
> it exactly, character-for-character, into the "Lever anchor:" field below. Do not reconstruct
> the label from Phase 5(3) or from CCV step (5). The audit L3 Evidence cell is the derivation
> source; the audit is the authority.
>
> "Lever anchor: [copy the exact text from the L3 Evidence cell -- do not reconstruct from
> Phase 5(3)]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must reproduce the L3 Evidence cell text exactly. The AMEND section is not
complete without the lever anchor and the observable condition.

---

### V-55: Full Ceiling (C-35 + C-36 + C-37)

**Axis:** All three combined. The AUDIT ARCHITECTURE DECLARED named block contains both
duality framing and full inline column spec (satisfying C-33, C-34, C-35, C-37 together).
AMEND(d) derives from L3 Evidence column as the authority (satisfying C-36). Preamble Row 3
registers audit-first direction at architecture-read time. Row 5 references the AUDIT
ARCHITECTURE DECLARED block. No separate Row 5 subsection. No duality in preamble intro
(moved to block).
**Hypothesis:** This is the structural combination that satisfies all 37 criteria. C-37 forces
co-residence of C-33 and C-34; the inline column spec inside the block also satisfies C-35
(no pointer indirection); audit-first AMEND(d) satisfies C-36. The structural claim: one named
gated block (V-53 pattern) + one inverted derivation direction (V-52 pattern) compose to the
370/370 ceiling. V-53 demonstrated co-residence works at 360/370; V-54 demonstrated
atomic + audit-first compose at 360/370. V-55 applies both simultaneously. Expected: 370/370.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?
Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. This architecture declares every
named artifact and exact-copy requirement before any production phase begins, and declares
the Citation Chain Completeness Audit that will verify the chain after all production phases
are complete. The structural roles of this preamble and the audit, and the audit's column
format, are declared in the AUDIT ARCHITECTURE DECLARED block below.

**Named artifacts, required outputs, and verification:**

| # | Phase / Position | Artifact or output | Downstream consumer | Requirement |
|---|------------------|--------------------|---------------------|-------------|
| 1 | Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Exact-copy: copy artifact name, not "Phase 1" |
| 2 | Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Exact-copy: copy artifact name, not "Phase 2" |
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: copy the exact label string verbatim. AMEND(d) must derive its lever anchor FROM the L3 Evidence column of the Citation Chain Completeness Audit -- the audit is the derivation authority; do not construct from Phase 5(3) and retroactively confirm. |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | See AUDIT ARCHITECTURE DECLARED block below for column structure, Evidence-column semantics, and audit structural role; CHAIN COMPLETE gate before CCV |

---

**AUDIT ARCHITECTURE DECLARED**

This output has two structural artifacts serving distinct and non-substitutable roles. The
Citation Architecture preamble (rows 1--5 above) is declarative: it specifies what will be
produced and how it will be cited before any production phase begins. The Citation Chain
Completeness Audit is confirmatory: it verifies what was produced after all production phases
are complete. These roles are structurally distinct. The preamble cannot confirm chain
integrity because it precedes production. The audit cannot declare artifact names and
exact-copy requirements because those must be known before Phase 1. Neither artifact
substitutes for or subsumes the other's function.

The Citation Chain Completeness Audit (row 5) must use the following 5-column structure for
all four links: Source artifact | Consumer site | Evidence [write actual downstream cite text
verbatim -- for L3, write the exact "Lever anchor: [LEVER POINT label]" text that will appear
in AMEND(d); for L1/L2/L4, write the phrase from the consuming section that names the source
artifact character-for-character; write the actual text produced, not a description or
summary of it; the Evidence cell must be populated with the real text, not a placeholder] |
Link type [Reference-chain if Evidence reproduces source artifact label verbatim;
Description-chain if Evidence describes or paraphrases rather than copying] | Verdict [PASS
for Reference-chain; CHAIN INTEGRITY FAILURE for Description-chain -- not "weaker" or
"incomplete"; a description-chain link is a structural chain failure]. Close the audit table
with "CHAIN COMPLETE: all four links are reference chains" or "CHAIN BREAK: [list link IDs]
-- return to Phase [X] before proceeding."

Do not proceed to Phase 1 until "AUDIT ARCHITECTURE DECLARED" is written on its own line
above. The block above is the required output. Its presence confirms that both the duality
framing (preamble's declarative role vs. audit's confirmatory role) and the full audit column
structure (including Evidence-column semantics) have been declared before Phase 1 begins.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block specifying the audit's structural role and column
> format. All named artifacts must be produced exactly as declared. All downstream cites must
> copy upstream labels verbatim. AMEND(d) must derive its lever anchor from the L3 Evidence
> column of the audit -- not from Phase 5(3). The audit must be produced after Phase 7 and
> must declare CHAIN COMPLETE before the CCV gate may proceed."

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

Produce the 5-column audit table using the column structure declared in AUDIT ARCHITECTURE
DECLARED above. For each link, write the actual downstream cite text in the Evidence column.
Assign Link type and Verdict from that evidence.

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [write the exact phrase from your Phase 4 trace that names the Phase 1 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [write the exact phrase from your Phase 5(2) that names the Phase 2 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the exact text that WILL appear in AMEND(d)'s "Lever anchor:" field -- this is a forward commitment; AMEND(d) will copy from this cell, not from Phase 5(3)] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Verdict rules:**
- Reference-chain: Evidence reproduces Source artifact label verbatim. Verdict: PASS.
- Description-chain: Evidence describes or paraphrases. Verdict: CHAIN INTEGRITY FAILURE --
  not "weaker," not "incomplete."
- L3 forward commitment: the text you write in the L3 Evidence cell is the source AMEND(d)
  will copy from. Write the exact "Lever anchor: [LEVER POINT label]" text as it will appear.
  AMEND(d) does not reconstruct from Phase 5(3); it copies from this cell exactly.

**Required aggregate declaration on its own line:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs with CHAIN INTEGRITY FAILURE] -- return to Phase [X] and
> produce the required named artifact before re-auditing."

**Gate rule:** Do not proceed to CCV until CHAIN COMPLETE is written. If CHAIN BREAK, correct
and re-audit.

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
Correct the upstream phase before proceeding.

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
> Locate the L3 row of the Citation Chain Completeness Audit above. The Evidence column of
> that row contains the lever anchor text you pre-committed to when you wrote the audit. That
> cell is the derivation authority. Copy its contents exactly, character-for-character, into
> the "Lever anchor:" field below. Do not reconstruct the anchor from Phase 5(3). Do not use
> CCV step (5) as the source. The L3 Evidence cell is the one source; copy it verbatim.
>
> "Lever anchor: [copy the exact text from the L3 Evidence cell of the Citation Chain
> Completeness Audit -- do not reconstruct from Phase 5(3)]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must reproduce the L3 Evidence cell text exactly. The AMEND section is not
complete without the lever anchor and the observable condition.

---

## R11 Structural Summary

| Variation | C-35 | C-36 | C-37 | Predicted total |
|-----------|------|------|------|-----------------|
| V-51 | PASS | FAIL | FAIL | 350/370 |
| V-52 | FAIL | PASS | FAIL | 350/370 |
| V-53 | PASS (byproduct) | FAIL | PASS | 360/370 |
| V-54 | PASS | PASS | FAIL | 360/370 |
| V-55 | PASS | PASS | PASS | 370/370 |

**Structural decisions per variation:**

- **V-51 vs V-45:** Row 5 cell carries full inline spec; "Row 5 audit format" subsection
  removed. Tests whether atomic inline Row 5 alone earns C-35.

- **V-52 vs V-45:** Row 3 adds audit-first direction signal; AMEND(d) replaces "copy from CCV
  step (5) -- match audit verbatim" with "locate L3 Evidence cell; it is the derivation source;
  copy it; do not reconstruct from Phase 5(3)." Tests C-36 single-axis.

- **V-53 vs V-45:** AUDIT ARCHITECTURE DECLARED block inserted after preamble table with
  duality framing + full inline column spec + Phase 1 gate. Duality removed from preamble
  intro. Row 5 subsection removed. Row 5 cell references the block. Tests C-37 single-axis;
  C-35 captured because inline block spec eliminates pointer indirection.

- **V-54 vs V-45:** Row 5 atomic inline (C-35) + Row 3 direction signal + audit-first AMEND(d)
  (C-36). No AUDIT ARCHITECTURE block. Duality in preamble intro. Tests C-35 + C-36
  composition without C-37.

- **V-55 vs V-45:** AUDIT ARCHITECTURE block (C-33 + C-34 + C-35 + C-37) + Row 3 direction
  signal + audit-first AMEND(d) (C-36). Full 370/370 ceiling design.
