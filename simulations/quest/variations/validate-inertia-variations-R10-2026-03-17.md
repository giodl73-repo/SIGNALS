Written to `simulations/quest/variations/validate-inertia-variations-R10-2026-03-17.md`.

---

## R10 Variations Summary

| # | Label | Axis | Primary target |
|---|-------|------|----------------|
| **V-46** | Duality in audit header only | C-33 placement | Preamble carries no duality framing; audit header carries it |
| **V-47** | Audit format inlined in Row 5 | C-34 delivery | Column spec embedded in preamble table cell, no subsection |
| **V-48** | Audit-first citation flow | C-32 enforcement | AMEND(d) derives lever anchor from L3 Evidence column directly |
| **V-49** | AUDIT ARCHITECTURE merged block | C-33 + C-34 consolidation | Single named block declares both duality and format |
| **V-50** | Double-reinforcement | All three (C-32/C-33/C-34) | Each criterion reinforced at two structural positions |

---

### Diagnosis

V-45 scores 340/340 on R10 — C-32/C-33/C-34 were extracted from its excellence signals, so it is already the ceiling. R10 variations don't chase a gap; they run **structural experiments** on V-45's implementation choices.

**Three structural questions tested:**

**Q1 (C-33 placement):** V-45 puts duality framing in the preamble intro. V-46 relocates it to the audit header only. If C-33 requires the declarative-context placement, V-46 earns PARTIAL — confirming that framing at execution-site isn't sufficient and preamble placement is the structural requirement.

**Q2 (C-34 delivery):** V-45 uses a "see below" pointer from Row 5 to a subsection. V-47 inlines the full column spec in the Row 5 cell. Tests whether atomic inline (no pointer indirection) reduces execution-time format drift, at the cost of losing the Evidence-column semantic prose from the subsection.

**Q3 (C-32 bidirectional lock direction):** V-45 runs forward-then-verify (copy from CCV → check against L3 audit). V-48 reverses: AMEND(d) derives from the L3 Evidence column first, making the audit the authoritative source rather than a retroactive validator.

**V-49** consolidates C-33 + C-34 into a single named `AUDIT ARCHITECTURE DECLARED` block — testing whether co-resident declaration prevents partial-criteria orphaning better than V-45's distributed placement.

**V-50** double-reinforces all three: C-33 at preamble + audit header, C-34 inline + subsection, C-32 with a three-way mismatch gate (LEVER POINT / CCV step 5 / L3 Evidence cell must all agree). Expected ceiling variant with maximum execution-time compliance at the cost of prompt length.
dit must cover

| Link | Source | Consumer | Status at audit time |
|------|--------|----------|---------------------|
| L1 | SCORING INFRASTRUCTURE DECLARED | Phase 4 traces | Retrospective |
| L2 | PERSONA INVENTORY DECLARED | Phase 5(2) | Retrospective |
| L3 | LEVER POINT: [label] | AMEND(d) anchor | Forward commitment |
| L4 | TRAJECTORY VERDICT: [direction] | Phase 7 | Retrospective |

### Design axis per variation

- **V-46** relocates C-33 duality framing from the preamble intro to the audit
  section header. Preamble carries no "architecture declares / audit confirms"
  sentence. Expected: PARTIAL on C-33 if the rubric reads preamble placement as
  required, or 340/340 if audit-header placement satisfies "labeled distinctly."
  This bounds C-33's placement sensitivity.
- **V-47** inlines the 5-column audit format in the Row 5 "Requirement" cell,
  removing the "Row 5 audit format" subsection. Expected: eliminates pointer-skip
  risk at the cost of reduced Evidence-column semantic depth; tests whether inline
  atomicity beats subsection verbosity for execution-time format compliance.
- **V-48** restructures AMEND(d) to derive the lever anchor from the L3 Evidence
  column directly ("locate L3 Evidence column, copy it here") rather than from
  CCV step (5) with a retroactive Evidence match check. Expected: makes the audit
  the authoritative source for the downstream cite; tests whether reversing the
  bidirectional lock direction strengthens C-32 runtime enforcement.
- **V-49** merges C-33 duality framing and C-34 format specification into a single
  named block "AUDIT ARCHITECTURE DECLARED" placed after the preamble table. Expected:
  consolidation prevents partial-criteria orphaning; tests whether unified declaration
  or V-45's distributed approach produces tighter co-compliance.
- **V-50** double-reinforces all three criteria: C-33 in both preamble intro and
  audit header; C-34 both inline in Row 5 and in the subsection; C-32 referencing
  both CCV step (5) and L3 Evidence column. Expected ceiling: 340/340 with maximally
  robust execution-time compliance -- no criterion can be partially satisfied if it
  appears at two structural positions.

---

### V-46: Duality Framing in Audit Header Only

**Axis:** C-33 placement -- single axis. V-45 base with one structural change:
the preamble intro loses the "Architecture declares what is produced; the audit
confirms what was produced" sentence. That framing appears instead as the opening
statement of the Citation Chain Completeness Audit section, at the point where the
model is about to write the audit.

**Hypothesis:** C-33 requires the output to "explicitly name" the two structural
roles as a duality. V-45 places this in the preamble intro (~50 tokens before
Phase 1). V-46 tests whether proximate placement at the audit execution site
satisfies the rubric condition "either in the preamble's introduction, the audit's
header, or a dedicated framing statement." If the rubric reads audit-header as a
valid placement, V-46 scores 340/340. If a PARTIAL is issued because the duality
is absent from the preamble's declarative context, this confirms preamble placement
is structurally critical -- a model must encounter the framing before the production
phases, not only at the moment the audit is written. Expected tiebreak: 330/340
(PARTIAL on C-33) or 340/340 depending on placement sensitivity.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works
perfectly? Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. This architecture has two
structural functions: (1) it declares every named artifact and exact-copy requirement
before any production phase begins; (2) it declares the Citation Chain Completeness
Audit that will verify the chain after all production phases are complete.

**Named artifacts, required outputs, and verification:**

| # | Phase / Position | Artifact or output | Downstream consumer | Requirement |
|---|------------------|--------------------|---------------------|-------------|
| 1 | Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Exact-copy: copy artifact name, not "Phase 1" |
| 2 | Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Exact-copy: copy artifact name, not "Phase 2" |
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: copy the exact label string verbatim |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | 5-column audit table (see below); CHAIN COMPLETE gate before CCV |

**Row 5 audit format:** The CITATION CHAIN COMPLETENESS AUDIT must use the following
table structure for all four links:

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|

- Evidence column: write the actual text from the downstream site that cites the
  source. For L3 (AMEND not yet written), write the exact text that WILL appear in
  AMEND(d)'s "Lever anchor:" field.
- Link type: Reference-chain if the evidence reproduces the source artifact label
  verbatim; Description-chain if the evidence describes or paraphrases.
- Verdict: PASS for Reference-chain; CHAIN INTEGRITY FAILURE for Description-chain.
- After the table, write "CHAIN COMPLETE: all four links are reference chains" or
  "CHAIN BREAK: [list link IDs] -- return to Phase [X] before proceeding."

**Exact-copy rule:** Only reference chains -- verbatim label reproduction -- satisfy
the citation requirements. Description chains are structural failures.

**Structural prohibition:** Do not produce output that would require a downstream
phase to paraphrase. If a phase would produce unnamed prose where this architecture
requires a named artifact, the phase is incomplete. Return and emit the artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4) and the Citation Chain Completeness Audit requirement
> (row 5). All named artifacts must be produced exactly as declared. All downstream
> cites must copy upstream labels verbatim. The audit must be produced after Phase 7
> and must declare CHAIN COMPLETE before the CCV gate may proceed."

Do not proceed to Phase 1 until this label is written.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight |
|-----------|------------------------------|-----------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof
requirement / Learning curve.

**Score thresholds:**

- **Critical:** [dimension combinations]
- **High:** [combinations]
- **Medium:** [combinations]
- **Low:** [condition all dimensions must satisfy]

**Required infrastructure label** (Citation Architecture row 1):

> "SCORING INFRASTRUCTURE DECLARED. All per-persona methodology traces in Phase 4
> must cite this Phase 1 output by reference -- naming the specific dimension weights
> and tier thresholds declared above. Traces that reference dimension values without
> citing thresholds, or thresholds without dimension values, fail the per-score trace
> requirement."

Do not proceed to Phase 2 until written.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named
competitor.

- Name and role (specific)
- Current solution (named tool or method)
- Outcome the current solution delivers

**Competitive strength inventory per persona:**

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

Durability must name a structural constraint. **Familiarity is not durability.**
Structural constraints: technical, organizational, integration-based, or
switching-cost-based.

**Completeness gate:** For each persona: (1) all three fields present; (2) no
Durability uses familiarity/habit -- replace with structural constraint; (3) Dimension
names a specific axis. Do not proceed to Phase 3 until all personas pass all three
checks.

**Required inventory label** (Citation Architecture row 2):

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite
> this Phase 2 output by reference -- naming the specific Durability property by its
> Phase 2 label. A structural persistence claim that does not name the PERSONA
> INVENTORY DECLARED artifact is a paraphrase chain, not a reference chain."

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

Methodology trace: (a) name dimension values from Phase 3 + (b) state Phase 1
threshold satisfied. Cite Phase 1 by copying "SCORING INFRASTRUCTURE DECLARED"
(Citation Architecture row 1). Do not write "Phase 1." Write the artifact name.
Every persona scored individually.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

**KILL BARRIER** -- four labeled, distinct sub-parts. Do not merge any two.

**(1) Barrier definition** -- observable adoption friction; state the competitive
dimension. Do not include cause.

**(2) Structural persistence** -- why the barrier persists structurally. Cite PERSONA
INVENTORY DECLARED (Citation Architecture row 2): name the specific Durability
property by its Phase 2 label. A claim without naming the PERSONA INVENTORY DECLARED
artifact is a paraphrase chain.

**(3) Intervention target** -- specific lever point. Name the target, not the
intervention.

**Required lever label** (Citation Architecture row 3):

> **LEVER POINT: [exact label -- 3--7 words]**

**Falsifiability test:**

> "At T=6mo, the absence of this lever would be observable as: [specific observable
> behavioral or measurable condition]."

Replace Part (3) and repeat if you cannot produce a specific observable condition.
Do not write Part (4) until the test passes.

**(4) Lever efficacy** -- why addressing (3) resolves (2). Explain causally.
Reference (2) by name.

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
> kill-barrier trajectory verdict requirement. That output belongs exclusively to
> Part B."

| Persona | T=0 | T=6mo | T=18mo | Trajectory | Driver of change |
|---------|-----|-------|--------|------------|-----------------|

At least one trajectory non-flat. T=6mo and T=18mo cannot copy T=0 without a stated
reason.

**Part B: KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [Reference the structural persistence property from Phase
5(2) by name. Argue from mechanism, not from the per-persona grid.]

**Relationship to Part A:** [Alignment or divergence -- which structural property
drives both, or why they differ.]

**Required trajectory label** (Citation Architecture row 4):

> **TRAJECTORY VERDICT: [exact direction word -- Resolving, Stable, or Worsening]**

Do not proceed to Phase 7 until written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

- Score distribution (e.g., "2 High, 1 Critical")
- Kill-barrier trajectory: copy the exact TRAJECTORY VERDICT label (Citation
  Architecture row 4). Do not write "Phase 6 Part B." Write the exact label.
- Competitive summary: kill barrier dimension + Phase 2 structural durability basis
- 1--2 sentence rationale tying score distribution, trajectory, and confirmed kill
  barrier

---

## Citation Chain Completeness Audit

**(Citation Architecture row 5 -- required before CCV)**

**Structural function of this audit:** The Citation Architecture preamble (rows 1--4)
declared what would be produced -- it is declarative. This audit confirms what was
produced -- it is confirmatory. These are structurally distinct roles: the preamble
declares; the audit verifies. Neither artifact substitutes for the other's function.
Do not omit this audit on the grounds that the preamble already established chain
structure; the preamble's declarative function does not subsume this audit's
confirmatory function.

Produce the 5-column audit table below. For each link, write the actual downstream
cite text in the Evidence column. Assign Link type and Verdict from that evidence.

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [write the exact phrase from your Phase 4 trace that names the Phase 1 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [write the exact phrase from your Phase 5(2) that names the Phase 2 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the exact text that WILL appear in AMEND(d)'s "Lever anchor:" field] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Verdict rules:**
- Reference-chain: the Evidence text reproduces the Source artifact label verbatim
  (character-for-character). Verdict: PASS.
- Description-chain: the Evidence text describes or paraphrases rather than copying.
  Verdict: CHAIN INTEGRITY FAILURE -- not "weaker," not "incomplete."
- L3 evidence: write the exact "Lever anchor: [LEVER POINT label]" text that will
  appear in AMEND(d). This is a forward commitment. If you would paraphrase the label
  in AMEND(d), correct it now before proceeding.

**Required aggregate declaration on its own line:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs with CHAIN INTEGRITY FAILURE, e.g., L2] -- return to
> Phase [X] and produce the required named artifact before re-auditing."

**Gate rule:** Do not proceed to the Citation Chain Verification until CHAIN COMPLETE
is written on its own line. If CHAIN BREAK is written, return to the named phase,
correct the artifact, and re-run this audit from the top. Do not proceed until the
audit closes with CHAIN COMPLETE.

---

## Citation Chain Verification

Before writing AMEND, complete all six fields with named text.

1. **Phase 1 artifact name:** [exact text produced in Phase 1]
2. **Phase 2 artifact name:** [exact text produced in Phase 2]
3. **Phase 4 citation:** [exact artifact name from (1) as it appears in Phase 4
   traces]
4. **Phase 5(2) citation:** [exact artifact name from (2) as it appears in Phase
   5(2)]
5. **Phase 5(3) lever label:** [exact LEVER POINT label]
6. **Phase 6 Part B trajectory label:** [exact TRAJECTORY VERDICT label]

A field containing "Phase X" or "see above" without the actual artifact name fails.
Correct the upstream phase before proceeding. Do not write AMEND until all six
fields pass.

---

## AMEND -- Focus, Quantify, Confirm

**Focus persona:** [name -- most exposed to confirmed kill barrier]

**Switching cost (sharpened):** [most precise quantified value]

**Kill barrier for this persona:** [one sentence -- competitive dimension, most acute
because]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete action]
>
> **(b) Root cause addressed:** [name the structural condition from Phase 5(2)]
>
> **(c) Causal mechanism:** [why this lever reaches the structural condition in (2).
> Reference the Phase 5(3) lever point by name.]
>
> **(d) Confirmation signal at T=6mo:**
>
> "Lever anchor: [copy the exact LEVER POINT label from Citation Chain Verification
> step (5) -- this must match the Evidence you wrote in the L3 row of the Citation
> Chain Completeness Audit verbatim]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must cite the exact LEVER POINT label. The AMEND section is not
complete without the lever anchor and the observable condition.

---

### V-47: Audit Format Inlined in Row 5

**Axis:** C-34 delivery -- single axis. V-45 base with one structural change:
the 5-column audit format specification is embedded directly in the Row 5
"Requirement" cell of the preamble table. The separate "Row 5 audit format"
subsection is removed. The preamble table is self-contained for both the audit's
existence requirement and its exact column structure.

**Hypothesis:** V-45 uses a "see below" pointer from Row 5 to a subsection that
specifies the 5-column format and Evidence-column semantics in prose. The pointer
creates a two-step read: encounter Row 5 -> follow to subsection. A model that reads
the preamble table but skips the subsection encounters the format for the first time
at audit execution (1500+ tokens later) -- the same drift-risk that justified the
preamble. V-47 collapses the pointer: the full column spec appears in the Row 5 cell.
C-34's pass condition requires "the preamble must declare the exact column structure
of the C-31 audit table -- specifically including the Evidence column -- before
Phase 1." Inline in Row 5 satisfies this atomically. Risk: the Evidence-column
semantics in V-45's subsection ("write the actual text... For L3 (AMEND not yet
written)...") cannot fit in a cell; if that semantic depth is needed for C-32
execution-time compliance, V-47 may produce weaker Evidence fill-in despite
satisfying C-34 structurally. Expected: 340/340 if column-name-level specification
satisfies C-34; potentially weaker C-32 runtime compliance.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works
perfectly? Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. This architecture has two
structural functions: (1) it declares every named artifact and exact-copy requirement
before any production phase begins; (2) it declares the Citation Chain Completeness
Audit that will verify the chain after all production phases are complete.
Architecture declares what is produced; the audit confirms what was produced.

**Named artifacts, required outputs, and verification:**

| # | Phase / Position | Artifact or output | Downstream consumer | Requirement |
|---|------------------|--------------------|---------------------|-------------|
| 1 | Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Exact-copy: copy artifact name, not "Phase 1" |
| 2 | Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Exact-copy: copy artifact name, not "Phase 2" |
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: copy the exact label string verbatim |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | 5-column table: Source artifact \| Consumer site \| Evidence (write actual downstream cite text verbatim, not a summary) \| Link type (Reference-chain or Description-chain) \| Verdict (PASS or CHAIN INTEGRITY FAILURE); CHAIN COMPLETE gate required before CCV |

**Exact-copy rule:** Only reference chains -- verbatim label reproduction -- satisfy
the citation requirements. Description chains are structural failures.

**Structural prohibition:** Do not produce output that would require a downstream
phase to paraphrase. If a phase would produce unnamed prose where this architecture
requires a named artifact, the phase is incomplete. Return and emit the artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4) and the Citation Chain Completeness Audit requirement
> (row 5). All named artifacts must be produced exactly as declared. All downstream
> cites must copy upstream labels verbatim. The audit must be produced after Phase 7
> and must declare CHAIN COMPLETE before the CCV gate may proceed."

Do not proceed to Phase 1 until this label is written.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight |
|-----------|------------------------------|-----------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof
requirement / Learning curve.

**Score thresholds:**

- **Critical:** [dimension combinations]
- **High:** [combinations]
- **Medium:** [combinations]
- **Low:** [condition all dimensions must satisfy]

**Required infrastructure label** (Citation Architecture row 1):

> "SCORING INFRASTRUCTURE DECLARED. All per-persona methodology traces in Phase 4
> must cite this Phase 1 output by reference -- naming the specific dimension weights
> and tier thresholds declared above. Traces that reference dimension values without
> citing thresholds, or thresholds without dimension values, fail the per-score trace
> requirement."

Do not proceed to Phase 2 until written.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named
competitor.

- Name and role (specific)
- Current solution (named tool or method)
- Outcome the current solution delivers

**Competitive strength inventory per persona:**

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

Durability must name a structural constraint. **Familiarity is not durability.**
Structural constraints: technical, organizational, integration-based, or
switching-cost-based.

**Completeness gate:** For each persona: (1) all three fields present; (2) no
Durability uses familiarity/habit -- replace with structural constraint; (3) Dimension
names a specific axis. Do not proceed to Phase 3 until all personas pass all three
checks.

**Required inventory label** (Citation Architecture row 2):

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite
> this Phase 2 output by reference -- naming the specific Durability property by its
> Phase 2 label. A structural persistence claim that does not name the PERSONA
> INVENTORY DECLARED artifact is a paraphrase chain, not a reference chain."

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

Methodology trace: (a) name dimension values from Phase 3 + (b) state Phase 1
threshold satisfied. Cite Phase 1 by copying "SCORING INFRASTRUCTURE DECLARED"
(Citation Architecture row 1). Do not write "Phase 1." Write the artifact name.
Every persona scored individually.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

**KILL BARRIER** -- four labeled, distinct sub-parts. Do not merge any two.

**(1) Barrier definition** -- observable adoption friction; state the competitive
dimension. Do not include cause.

**(2) Structural persistence** -- why the barrier persists structurally. Cite PERSONA
INVENTORY DECLARED (Citation Architecture row 2): name the specific Durability
property by its Phase 2 label. A claim without naming the PERSONA INVENTORY DECLARED
artifact is a paraphrase chain.

**(3) Intervention target** -- specific lever point. Name the target, not the
intervention.

**Required lever label** (Citation Architecture row 3):

> **LEVER POINT: [exact label -- 3--7 words]**

**Falsifiability test:**

> "At T=6mo, the absence of this lever would be observable as: [specific observable
> behavioral or measurable condition]."

Replace Part (3) and repeat if you cannot produce a specific observable condition.
Do not write Part (4) until the test passes.

**(4) Lever efficacy** -- why addressing (3) resolves (2). Explain causally.
Reference (2) by name.

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
> kill-barrier trajectory verdict requirement. That output belongs exclusively to
> Part B."

| Persona | T=0 | T=6mo | T=18mo | Trajectory | Driver of change |
|---------|-----|-------|--------|------------|-----------------|

At least one trajectory non-flat. T=6mo and T=18mo cannot copy T=0 without a stated
reason.

**Part B: KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [Reference the structural persistence property from Phase
5(2) by name. Argue from mechanism, not from the per-persona grid.]

**Relationship to Part A:** [Alignment or divergence -- which structural property
drives both, or why they differ.]

**Required trajectory label** (Citation Architecture row 4):

> **TRAJECTORY VERDICT: [exact direction word -- Resolving, Stable, or Worsening]**

Do not proceed to Phase 7 until written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

- Score distribution (e.g., "2 High, 1 Critical")
- Kill-barrier trajectory: copy the exact TRAJECTORY VERDICT label (Citation
  Architecture row 4). Do not write "Phase 6 Part B." Write the exact label.
- Competitive summary: kill barrier dimension + Phase 2 structural durability basis
- 1--2 sentence rationale tying score distribution, trajectory, and confirmed kill
  barrier

---

## Citation Chain Completeness Audit

**(Citation Architecture row 5 -- required before CCV)**

Produce the 5-column audit table declared in the Citation Architecture (row 5).
For each link, write the actual downstream cite text in the Evidence column.
Assign Link type and Verdict from that evidence.

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [write the exact phrase from your Phase 4 trace that names the Phase 1 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [write the exact phrase from your Phase 5(2) that names the Phase 2 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the exact text that WILL appear in AMEND(d)'s "Lever anchor:" field] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Verdict rules:**
- Reference-chain: the Evidence text reproduces the Source artifact label verbatim
  (character-for-character). Verdict: PASS.
- Description-chain: the Evidence text describes or paraphrases rather than copying.
  Verdict: CHAIN INTEGRITY FAILURE -- not "weaker," not "incomplete."
- L3 evidence: write the exact "Lever anchor: [LEVER POINT label]" text that will
  appear in AMEND(d). This is a forward commitment.

**Required aggregate declaration on its own line:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs with CHAIN INTEGRITY FAILURE, e.g., L2] -- return to
> Phase [X] and produce the required named artifact before re-auditing."

**Gate rule:** Do not proceed to the Citation Chain Verification until CHAIN COMPLETE
is written on its own line.

---

## Citation Chain Verification

Before writing AMEND, complete all six fields with named text.

1. **Phase 1 artifact name:** [exact text produced in Phase 1]
2. **Phase 2 artifact name:** [exact text produced in Phase 2]
3. **Phase 4 citation:** [exact artifact name from (1) as it appears in Phase 4
   traces]
4. **Phase 5(2) citation:** [exact artifact name from (2) as it appears in Phase
   5(2)]
5. **Phase 5(3) lever label:** [exact LEVER POINT label]
6. **Phase 6 Part B trajectory label:** [exact TRAJECTORY VERDICT label]

A field containing "Phase X" or "see above" without the actual artifact name fails.
Correct the upstream phase before proceeding. Do not write AMEND until all six
fields pass.

---

## AMEND -- Focus, Quantify, Confirm

**Focus persona:** [name -- most exposed to confirmed kill barrier]

**Switching cost (sharpened):** [most precise quantified value]

**Kill barrier for this persona:** [one sentence -- competitive dimension, most acute
because]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete action]
>
> **(b) Root cause addressed:** [name the structural condition from Phase 5(2)]
>
> **(c) Causal mechanism:** [why this lever reaches the structural condition in (2).
> Reference the Phase 5(3) lever point by name.]
>
> **(d) Confirmation signal at T=6mo:**
>
> "Lever anchor: [copy the exact LEVER POINT label from Citation Chain Verification
> step (5) -- this must match the Evidence you wrote in the L3 row of the Citation
> Chain Completeness Audit verbatim]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must cite the exact LEVER POINT label. The AMEND section is not
complete without the lever anchor and the observable condition.

---

### V-48: Audit-First Citation Flow

**Axis:** C-32 enforcement direction -- single axis. V-45 base with one structural
change in AMEND(d): the lever anchor instruction is restructured so the model
derives the lever anchor from the L3 Evidence column first, then writes it below,
rather than choosing the label from CCV step (5) and retroactively verifying it
matches the audit.

**Hypothesis:** V-45's AMEND(d) instruction runs forward-then-verify: "copy the
exact LEVER POINT label from CCV step (5) -- this must match the Evidence you wrote
in the L3 row verbatim." The model chooses the label from the lever production phase,
writes it, then checks against the audit. A model that slightly rephrases the lever
label between Phase 5(3) and AMEND may not self-detect the mismatch because it is
checking its own recent output. V-48 reverses the direction: AMEND(d) instructs the
model to locate the L3 Evidence column first, copy from there, and write that text
as the lever anchor. The audit becomes the authoritative source, not a retroactive
validator. This prevents two-step drift (Phase 5(3) -> CCV -> AMEND) by collapsing
to one-step copy (L3 Evidence -> AMEND). C-32's pass condition: "AMEND(d)'s
exact-copy instruction must reinforce the Evidence column by name, creating a
bidirectional lock." Referencing L3 Evidence column directly and making it the
source satisfies the bidirectional lock in the strongest possible form -- the audit
dictates the downstream cite rather than merely confirming it. Expected: 340/340
with tighter runtime C-32 enforcement than V-45.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works
perfectly? Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. This architecture has two
structural functions: (1) it declares every named artifact and exact-copy requirement
before any production phase begins; (2) it declares the Citation Chain Completeness
Audit that will verify the chain after all production phases are complete.
Architecture declares what is produced; the audit confirms what was produced.

**Named artifacts, required outputs, and verification:**

| # | Phase / Position | Artifact or output | Downstream consumer | Requirement |
|---|------------------|--------------------|---------------------|-------------|
| 1 | Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Exact-copy: copy artifact name, not "Phase 1" |
| 2 | Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Exact-copy: copy artifact name, not "Phase 2" |
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: AMEND(d) must derive lever anchor from L3 Evidence column of the audit, not construct independently |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | 5-column audit table (see below); L3 Evidence is the authoritative lever anchor source for AMEND(d); CHAIN COMPLETE gate before CCV |

**Row 5 audit format:** The CITATION CHAIN COMPLETENESS AUDIT must use the following
table structure for all four links:

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|

- Evidence column: write the actual text from the downstream site that cites the
  source. For L3 (AMEND not yet written), write the exact text that WILL appear in
  AMEND(d)'s "Lever anchor:" field. AMEND(d) will then copy this cell -- not CCV
  step (5) -- as its lever anchor. Write the complete "Lever anchor: [LEVER POINT
  label]" string here first.
- Link type: Reference-chain if the evidence reproduces the source artifact label
  verbatim; Description-chain if the evidence describes or paraphrases.
- Verdict: PASS for Reference-chain; CHAIN INTEGRITY FAILURE for Description-chain.
- After the table, write "CHAIN COMPLETE: all four links are reference chains" or
  "CHAIN BREAK: [list link IDs] -- return to Phase [X] before proceeding."

**Exact-copy rule:** Only reference chains -- verbatim label reproduction -- satisfy
the citation requirements. Description chains are structural failures.

**Structural prohibition:** Do not produce output that would require a downstream
phase to paraphrase. If a phase would produce unnamed prose where this architecture
requires a named artifact, the phase is incomplete. Return and emit the artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4) and the Citation Chain Completeness Audit requirement
> (row 5). All named artifacts must be produced exactly as declared. All downstream
> cites must copy upstream labels verbatim. The audit must be produced after Phase 7
> and must declare CHAIN COMPLETE before the CCV gate may proceed."

Do not proceed to Phase 1 until this label is written.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight |
|-----------|------------------------------|-----------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof
requirement / Learning curve.

**Score thresholds:**

- **Critical:** [dimension combinations]
- **High:** [combinations]
- **Medium:** [combinations]
- **Low:** [condition all dimensions must satisfy]

**Required infrastructure label** (Citation Architecture row 1):

> "SCORING INFRASTRUCTURE DECLARED. All per-persona methodology traces in Phase 4
> must cite this Phase 1 output by reference -- naming the specific dimension weights
> and tier thresholds declared above. Traces that reference dimension values without
> citing thresholds, or thresholds without dimension values, fail the per-score trace
> requirement."

Do not proceed to Phase 2 until written.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named
competitor.

- Name and role (specific)
- Current solution (named tool or method)
- Outcome the current solution delivers

**Competitive strength inventory per persona:**

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

Durability must name a structural constraint. **Familiarity is not durability.**
Structural constraints: technical, organizational, integration-based, or
switching-cost-based.

**Completeness gate:** For each persona: (1) all three fields present; (2) no
Durability uses familiarity/habit -- replace with structural constraint; (3) Dimension
names a specific axis. Do not proceed to Phase 3 until all personas pass all three
checks.

**Required inventory label** (Citation Architecture row 2):

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite
> this Phase 2 output by reference -- naming the specific Durability property by its
> Phase 2 label. A structural persistence claim that does not name the PERSONA
> INVENTORY DECLARED artifact is a paraphrase chain, not a reference chain."

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

Methodology trace: (a) name dimension values from Phase 3 + (b) state Phase 1
threshold satisfied. Cite Phase 1 by copying "SCORING INFRASTRUCTURE DECLARED"
(Citation Architecture row 1). Do not write "Phase 1." Write the artifact name.
Every persona scored individually.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

**KILL BARRIER** -- four labeled, distinct sub-parts. Do not merge any two.

**(1) Barrier definition** -- observable adoption friction; state the competitive
dimension. Do not include cause.

**(2) Structural persistence** -- why the barrier persists structurally. Cite PERSONA
INVENTORY DECLARED (Citation Architecture row 2): name the specific Durability
property by its Phase 2 label. A claim without naming the PERSONA INVENTORY DECLARED
artifact is a paraphrase chain.

**(3) Intervention target** -- specific lever point. Name the target, not the
intervention.

**Required lever label** (Citation Architecture row 3):

> **LEVER POINT: [exact label -- 3--7 words]**

**Falsifiability test:**

> "At T=6mo, the absence of this lever would be observable as: [specific observable
> behavioral or measurable condition]."

Replace Part (3) and repeat if you cannot produce a specific observable condition.
Do not write Part (4) until the test passes.

**(4) Lever efficacy** -- why addressing (3) resolves (2). Explain causally.
Reference (2) by name.

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
> kill-barrier trajectory verdict requirement. That output belongs exclusively to
> Part B."

| Persona | T=0 | T=6mo | T=18mo | Trajectory | Driver of change |
|---------|-----|-------|--------|------------|-----------------|

At least one trajectory non-flat. T=6mo and T=18mo cannot copy T=0 without a stated
reason.

**Part B: KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [Reference the structural persistence property from Phase
5(2) by name. Argue from mechanism, not from the per-persona grid.]

**Relationship to Part A:** [Alignment or divergence -- which structural property
drives both, or why they differ.]

**Required trajectory label** (Citation Architecture row 4):

> **TRAJECTORY VERDICT: [exact direction word -- Resolving, Stable, or Worsening]**

Do not proceed to Phase 7 until written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

- Score distribution (e.g., "2 High, 1 Critical")
- Kill-barrier trajectory: copy the exact TRAJECTORY VERDICT label (Citation
  Architecture row 4). Do not write "Phase 6 Part B." Write the exact label.
- Competitive summary: kill barrier dimension + Phase 2 structural durability basis
- 1--2 sentence rationale tying score distribution, trajectory, and confirmed kill
  barrier

---

## Citation Chain Completeness Audit

**(Citation Architecture row 5 -- required before CCV)**

Produce the 5-column audit table below. For each link, write the actual downstream
cite text in the Evidence column. Assign Link type and Verdict from that evidence.

**Important for L3:** The text you write in the Evidence column of the L3 row is the
exact text that AMEND(d) will derive its lever anchor from. Write the complete
"Lever anchor: [LEVER POINT label]" string here now. AMEND(d) will copy from this
cell directly.

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [write the exact phrase from your Phase 4 trace that names the Phase 1 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [write the exact phrase from your Phase 5(2) that names the Phase 2 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the complete "Lever anchor: [LEVER POINT label]" string -- AMEND(d) will copy this cell verbatim] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Verdict rules:**
- Reference-chain: the Evidence text reproduces the Source artifact label verbatim
  (character-for-character). Verdict: PASS.
- Description-chain: the Evidence text describes or paraphrases rather than copying.
  Verdict: CHAIN INTEGRITY FAILURE -- not "weaker," not "incomplete."

**Required aggregate declaration on its own line:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs with CHAIN INTEGRITY FAILURE, e.g., L2] -- return to
> Phase [X] and produce the required named artifact before re-auditing."

**Gate rule:** Do not proceed to the Citation Chain Verification until CHAIN COMPLETE
is written on its own line. If CHAIN BREAK is written, return to the named phase,
correct the artifact, and re-run this audit from the top.

---

## Citation Chain Verification

Before writing AMEND, complete all six fields with named text.

1. **Phase 1 artifact name:** [exact text produced in Phase 1]
2. **Phase 2 artifact name:** [exact text produced in Phase 2]
3. **Phase 4 citation:** [exact artifact name from (1) as it appears in Phase 4
   traces]
4. **Phase 5(2) citation:** [exact artifact name from (2) as it appears in Phase
   5(2)]
5. **Phase 5(3) lever label:** [exact LEVER POINT label]
6. **Phase 6 Part B trajectory label:** [exact TRAJECTORY VERDICT label]

A field containing "Phase X" or "see above" without the actual artifact name fails.
Correct the upstream phase before proceeding. Do not write AMEND until all six
fields pass.

---

## AMEND -- Focus, Quantify, Confirm

**Focus persona:** [name -- most exposed to confirmed kill barrier]

**Switching cost (sharpened):** [most precise quantified value]

**Kill barrier for this persona:** [one sentence -- competitive dimension, most acute
because]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete action]
>
> **(b) Root cause addressed:** [name the structural condition from Phase 5(2)]
>
> **(c) Causal mechanism:** [why this lever reaches the structural condition in (2).
> Reference the Phase 5(3) lever point by name.]
>
> **(d) Confirmation signal at T=6mo:**
>
> Step 1: Locate the L3 row of the Citation Chain Completeness Audit above. The
> Evidence column of that row contains the lever anchor text you pre-committed to
> when you wrote the audit. Copy it exactly, character-for-character, into the
> lever anchor field below -- do not reconstruct from Phase 5(3) or CCV step (5).
>
> "Lever anchor: [paste exactly from the L3 Evidence column of the Citation Chain
> Completeness Audit -- reproduce that cell's text verbatim here]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must reproduce the exact L3 Evidence cell text. Any difference
between the L3 Evidence cell and the lever anchor below is a chain integrity failure.
The AMEND section is not complete without the lever anchor and the observable
condition.

---

### V-49: AUDIT ARCHITECTURE Merged Block

**Axis:** C-33 + C-34 consolidation -- combined axis. V-45 base with three changes:
(1) the preamble intro loses the duality framing sentence; (2) the "Row 5 audit
format" subsection is removed; (3) a dedicated "AUDIT ARCHITECTURE DECLARED" block
is inserted after the preamble table and before the exact-copy rule, containing both
the architecture-audit duality framing (C-33) and the full 5-column format
specification (C-34) in one named structural unit.

**Hypothesis:** V-45 satisfies C-33 via the preamble intro and C-34 via the "Row 5
audit format" subsection -- two sections 150-200 tokens apart in the preamble. A
model reading for artifact declarations may encounter the duality framing in the intro
and the format spec in the subsection without treating them as co-resident structural
requirements. V-49 consolidates both into one named block that the model must emit
as a required output ("Do not proceed to Phase 1 until AUDIT ARCHITECTURE DECLARED
is written"). The block makes C-33 and C-34 co-resident: duality framing and format
spec cannot be separated or partially satisfied without omitting the entire block.
The "AUDIT ARCHITECTURE DECLARED" artifact label extends the named-artifact pattern
(C-24, C-28) to the audit architecture itself, making it a citable boundary artifact.
Risk: the block is placed after the preamble table (not in the intro); if C-33
strictly requires duality framing in the preamble introduction, V-49 earns PARTIAL
despite satisfying C-33 in a dedicated framing statement. Expected: 340/340 if
"dedicated framing statement" satisfies C-33's placement condition; potentially
PARTIAL if only preamble-intro or audit-header placement qualifies.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works
perfectly? Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. This architecture declares
every named artifact and exact-copy requirement before any production phase begins.
It also registers the Citation Chain Completeness Audit that will verify the chain
after all production phases are complete.

**Named artifacts, required outputs, and verification:**

| # | Phase / Position | Artifact or output | Downstream consumer | Requirement |
|---|------------------|--------------------|---------------------|-------------|
| 1 | Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Exact-copy: copy artifact name, not "Phase 1" |
| 2 | Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Exact-copy: copy artifact name, not "Phase 2" |
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: copy the exact label string verbatim |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | See AUDIT ARCHITECTURE DECLARED block below |

**AUDIT ARCHITECTURE DECLARED.**

This citation system has two distinct structural functions. The Citation Architecture
table (rows 1--4 above) is declarative: it establishes what artifacts will be
produced and what cite requirements bind each consumer, before any production phase
begins. The Citation Chain Completeness Audit (row 5, executed after Phase 7) is
confirmatory: it verifies what was actually produced against what was declared. The
preamble declares; the audit confirms. These roles are structurally distinct and
neither artifact can substitute for or subsume the other. Omitting the audit on the
grounds that the preamble already established chain structure is a structural
failure.

**Required audit format (5 columns, all four links):**

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|

- Evidence column: write the actual text from the downstream site that cites the
  source. For L3 (AMEND not yet written), write the exact text that WILL appear in
  AMEND(d)'s "Lever anchor:" field.
- Link type: Reference-chain if the evidence reproduces the source artifact label
  verbatim; Description-chain if the evidence describes or paraphrases.
- Verdict: PASS for Reference-chain; CHAIN INTEGRITY FAILURE for Description-chain.
- After the table, write "CHAIN COMPLETE: all four links are reference chains" or
  "CHAIN BREAK: [list link IDs] -- return to Phase [X] before proceeding."
- CHAIN COMPLETE must be written on its own line before the CCV gate may proceed.

Do not proceed to Phase 1 until "AUDIT ARCHITECTURE DECLARED" is written above.

**Exact-copy rule:** Only reference chains -- verbatim label reproduction -- satisfy
the citation requirements. Description chains are structural failures.

**Structural prohibition:** Do not produce output that would require a downstream
phase to paraphrase. If a phase would produce unnamed prose where this architecture
requires a named artifact, the phase is incomplete. Return and emit the artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4) and the Citation Chain Completeness Audit requirement
> (row 5). All named artifacts must be produced exactly as declared. All downstream
> cites must copy upstream labels verbatim. The audit must be produced after Phase 7
> and must declare CHAIN COMPLETE before the CCV gate may proceed."

Do not proceed to Phase 1 until this label is written.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight |
|-----------|------------------------------|-----------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof
requirement / Learning curve.

**Score thresholds:**

- **Critical:** [dimension combinations]
- **High:** [combinations]
- **Medium:** [combinations]
- **Low:** [condition all dimensions must satisfy]

**Required infrastructure label** (Citation Architecture row 1):

> "SCORING INFRASTRUCTURE DECLARED. All per-persona methodology traces in Phase 4
> must cite this Phase 1 output by reference -- naming the specific dimension weights
> and tier thresholds declared above. Traces that reference dimension values without
> citing thresholds, or thresholds without dimension values, fail the per-score trace
> requirement."

Do not proceed to Phase 2 until written.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named
competitor.

- Name and role (specific)
- Current solution (named tool or method)
- Outcome the current solution delivers

**Competitive strength inventory per persona:**

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

Durability must name a structural constraint. **Familiarity is not durability.**
Structural constraints: technical, organizational, integration-based, or
switching-cost-based.

**Completeness gate:** For each persona: (1) all three fields present; (2) no
Durability uses familiarity/habit -- replace with structural constraint; (3) Dimension
names a specific axis. Do not proceed to Phase 3 until all personas pass all three
checks.

**Required inventory label** (Citation Architecture row 2):

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite
> this Phase 2 output by reference -- naming the specific Durability property by its
> Phase 2 label. A structural persistence claim that does not name the PERSONA
> INVENTORY DECLARED artifact is a paraphrase chain, not a reference chain."

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

Methodology trace: (a) name dimension values from Phase 3 + (b) state Phase 1
threshold satisfied. Cite Phase 1 by copying "SCORING INFRASTRUCTURE DECLARED"
(Citation Architecture row 1). Do not write "Phase 1." Write the artifact name.
Every persona scored individually.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

**KILL BARRIER** -- four labeled, distinct sub-parts. Do not merge any two.

**(1) Barrier definition** -- observable adoption friction; state the competitive
dimension. Do not include cause.

**(2) Structural persistence** -- why the barrier persists structurally. Cite PERSONA
INVENTORY DECLARED (Citation Architecture row 2): name the specific Durability
property by its Phase 2 label. A claim without naming the PERSONA INVENTORY DECLARED
artifact is a paraphrase chain.

**(3) Intervention target** -- specific lever point. Name the target, not the
intervention.

**Required lever label** (Citation Architecture row 3):

> **LEVER POINT: [exact label -- 3--7 words]**

**Falsifiability test:**

> "At T=6mo, the absence of this lever would be observable as: [specific observable
> behavioral or measurable condition]."

Replace Part (3) and repeat if you cannot produce a specific observable condition.
Do not write Part (4) until the test passes.

**(4) Lever efficacy** -- why addressing (3) resolves (2). Explain causally.
Reference (2) by name.

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
> kill-barrier trajectory verdict requirement. That output belongs exclusively to
> Part B."

| Persona | T=0 | T=6mo | T=18mo | Trajectory | Driver of change |
|---------|-----|-------|--------|------------|-----------------|

At least one trajectory non-flat. T=6mo and T=18mo cannot copy T=0 without a stated
reason.

**Part B: KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [Reference the structural persistence property from Phase
5(2) by name. Argue from mechanism, not from the per-persona grid.]

**Relationship to Part A:** [Alignment or divergence -- which structural property
drives both, or why they differ.]

**Required trajectory label** (Citation Architecture row 4):

> **TRAJECTORY VERDICT: [exact direction word -- Resolving, Stable, or Worsening]**

Do not proceed to Phase 7 until written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

- Score distribution (e.g., "2 High, 1 Critical")
- Kill-barrier trajectory: copy the exact TRAJECTORY VERDICT label (Citation
  Architecture row 4). Do not write "Phase 6 Part B." Write the exact label.
- Competitive summary: kill barrier dimension + Phase 2 structural durability basis
- 1--2 sentence rationale tying score distribution, trajectory, and confirmed kill
  barrier

---

## Citation Chain Completeness Audit

**(Citation Architecture row 5 -- required before CCV)**

Produce the 5-column audit table declared in the AUDIT ARCHITECTURE DECLARED block.
For each link, write the actual downstream cite text in the Evidence column. Assign
Link type and Verdict from that evidence.

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [write the exact phrase from your Phase 4 trace that names the Phase 1 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [write the exact phrase from your Phase 5(2) that names the Phase 2 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the exact text that WILL appear in AMEND(d)'s "Lever anchor:" field] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Verdict rules:**
- Reference-chain: Evidence text reproduces Source artifact label verbatim. Verdict:
  PASS.
- Description-chain: Evidence describes or paraphrases. Verdict: CHAIN INTEGRITY
  FAILURE -- not "weaker," not "incomplete."
- L3 evidence: write the exact "Lever anchor: [LEVER POINT label]" text that will
  appear in AMEND(d). This is a forward commitment.

**Required aggregate declaration on its own line:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs] -- return to Phase [X] before re-auditing."

**Gate rule:** Do not proceed to the Citation Chain Verification until CHAIN COMPLETE
is written on its own line.

---

## Citation Chain Verification

Before writing AMEND, complete all six fields with named text.

1. **Phase 1 artifact name:** [exact text produced in Phase 1]
2. **Phase 2 artifact name:** [exact text produced in Phase 2]
3. **Phase 4 citation:** [exact artifact name from (1) as it appears in Phase 4
   traces]
4. **Phase 5(2) citation:** [exact artifact name from (2) as it appears in Phase
   5(2)]
5. **Phase 5(3) lever label:** [exact LEVER POINT label]
6. **Phase 6 Part B trajectory label:** [exact TRAJECTORY VERDICT label]

A field containing "Phase X" or "see above" without the actual artifact name fails.
Correct the upstream phase before proceeding. Do not write AMEND until all six
fields pass.

---

## AMEND -- Focus, Quantify, Confirm

**Focus persona:** [name -- most exposed to confirmed kill barrier]

**Switching cost (sharpened):** [most precise quantified value]

**Kill barrier for this persona:** [one sentence -- competitive dimension, most acute
because]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete action]
>
> **(b) Root cause addressed:** [name the structural condition from Phase 5(2)]
>
> **(c) Causal mechanism:** [why this lever reaches the structural condition in (2).
> Reference the Phase 5(3) lever point by name.]
>
> **(d) Confirmation signal at T=6mo:**
>
> "Lever anchor: [copy the exact LEVER POINT label from Citation Chain Verification
> step (5) -- this must match the Evidence you wrote in the L3 row of the Citation
> Chain Completeness Audit verbatim]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must cite the exact LEVER POINT label. The AMEND section is not
complete without the lever anchor and the observable condition.

---

### V-50: Double-Reinforcement -- All Three Criteria at Two Positions

**Axis:** All three (C-32/C-33/C-34) -- full integration with double-reinforcement.
V-45 base with each new criterion reinforced at two structural positions:
- **C-33 (duality framing):** in the preamble intro AND in the audit section header
- **C-34 (audit format):** abbreviated inline in Row 5 cell AND full spec in the
  "Row 5 audit format" subsection
- **C-32 (bidirectional lock):** AMEND(d) references both CCV step (5) and the L3
  Evidence column, with an explicit mismatch-correction instruction

**Hypothesis:** V-45 places each new criterion at one structural position. Attention
degradation across a 2000+ token output may cause a model to encounter a criterion
at read-time but not faithfully reproduce its enforcement at execution-time if that
criterion appears only once. V-50 tests whether double-positioning -- one declaration
plus one execution-site reinforcement -- eliminates all PARTIAL paths. C-33 at both
preamble intro and audit header satisfies "either in the preamble's introduction, the
audit's header, or a dedicated framing statement" at both allowed positions, with the
header reinforcement making the duality framing visible at the exact moment the model
is writing the audit. C-34 inline in Row 5 (atomic with the declaration) and in the
subsection (with Evidence-column semantic depth) gives the model the format at two
read points without redundancy -- the inline is a header, the subsection is prose
specification. C-32 referencing both CCV step (5) and L3 Evidence column, plus a
mismatch-correction instruction, creates a three-way lock: the lever label, the CCV,
and the audit must all agree. Expected ceiling: 340/340 with the highest execution-
time compliance of any R10 variation.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works
perfectly? Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. This architecture has two
structural functions: (1) it declares every named artifact and exact-copy requirement
before any production phase begins; (2) it declares the Citation Chain Completeness
Audit that will verify the chain after all production phases are complete.
Architecture declares what is produced; the audit confirms what was produced. These
are the two structurally distinct roles of this system: the preamble is declarative;
the audit is confirmatory. Neither artifact substitutes for the other's function.

**Named artifacts, required outputs, and verification:**

| # | Phase / Position | Artifact or output | Downstream consumer | Requirement |
|---|------------------|--------------------|---------------------|-------------|
| 1 | Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Exact-copy: copy artifact name, not "Phase 1" |
| 2 | Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Exact-copy: copy artifact name, not "Phase 2" |
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: copy the exact label string verbatim |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | 5-column table: Source artifact \| Consumer site \| Evidence (actual downstream cite text) \| Link type \| Verdict; full format in Row 5 audit format block below; CHAIN COMPLETE gate before CCV |

**Row 5 audit format:** The CITATION CHAIN COMPLETENESS AUDIT must use the following
table structure for all four links:

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|

- Evidence column: write the actual text from the downstream site that cites the
  source. For L3 (AMEND not yet written), write the exact text that WILL appear in
  AMEND(d)'s "Lever anchor:" field.
- Link type: Reference-chain if the evidence reproduces the source artifact label
  verbatim; Description-chain if the evidence describes or paraphrases.
- Verdict: PASS for Reference-chain; CHAIN INTEGRITY FAILURE for Description-chain.
- After the table, write "CHAIN COMPLETE: all four links are reference chains" or
  "CHAIN BREAK: [list link IDs] -- return to Phase [X] before proceeding."

**Exact-copy rule:** Only reference chains -- verbatim label reproduction -- satisfy
the citation requirements. Description chains are structural failures.

**Structural prohibition:** Do not produce output that would require a downstream
phase to paraphrase. If a phase would produce unnamed prose where this architecture
requires a named artifact, the phase is incomplete. Return and emit the artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4) and the Citation Chain Completeness Audit requirement
> (row 5). All named artifacts must be produced exactly as declared. All downstream
> cites must copy upstream labels verbatim. The audit must be produced after Phase 7
> and must declare CHAIN COMPLETE before the CCV gate may proceed."

Do not proceed to Phase 1 until this label is written.

---

## Phase 1 -- Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight |
|-----------|------------------------------|-----------------|

Dimensions: Workaround satisfaction / Switching cost / Habit lock-in / Social proof
requirement / Learning curve.

**Score thresholds:**

- **Critical:** [dimension combinations]
- **High:** [combinations]
- **Medium:** [combinations]
- **Low:** [condition all dimensions must satisfy]

**Required infrastructure label** (Citation Architecture row 1):

> "SCORING INFRASTRUCTURE DECLARED. All per-persona methodology traces in Phase 4
> must cite this Phase 1 output by reference -- naming the specific dimension weights
> and tier thresholds declared above. Traces that reference dimension values without
> citing thresholds, or thresholds without dimension values, fail the per-score trace
> requirement."

Do not proceed to Phase 2 until written.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named
competitor.

- Name and role (specific)
- Current solution (named tool or method)
- Outcome the current solution delivers

**Competitive strength inventory per persona:**

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

Durability must name a structural constraint. **Familiarity is not durability.**
Structural constraints: technical, organizational, integration-based, or
switching-cost-based.

**Completeness gate:** For each persona: (1) all three fields present; (2) no
Durability uses familiarity/habit -- replace with structural constraint; (3) Dimension
names a specific axis. Do not proceed to Phase 3 until all personas pass all three
checks.

**Required inventory label** (Citation Architecture row 2):

> "PERSONA INVENTORY DECLARED. Phase 5(2) structural persistence analysis must cite
> this Phase 2 output by reference -- naming the specific Durability property by its
> Phase 2 label. A structural persistence claim that does not name the PERSONA
> INVENTORY DECLARED artifact is a paraphrase chain, not a reference chain."

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

Methodology trace: (a) name dimension values from Phase 3 + (b) state Phase 1
threshold satisfied. Cite Phase 1 by copying "SCORING INFRASTRUCTURE DECLARED"
(Citation Architecture row 1). Do not write "Phase 1." Write the artifact name.
Every persona scored individually.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

**KILL BARRIER** -- four labeled, distinct sub-parts. Do not merge any two.

**(1) Barrier definition** -- observable adoption friction; state the competitive
dimension. Do not include cause.

**(2) Structural persistence** -- why the barrier persists structurally. Cite PERSONA
INVENTORY DECLARED (Citation Architecture row 2): name the specific Durability
property by its Phase 2 label. A claim without naming the PERSONA INVENTORY DECLARED
artifact is a paraphrase chain.

**(3) Intervention target** -- specific lever point. Name the target, not the
intervention.

**Required lever label** (Citation Architecture row 3):

> **LEVER POINT: [exact label -- 3--7 words]**

**Falsifiability test:**

> "At T=6mo, the absence of this lever would be observable as: [specific observable
> behavioral or measurable condition]."

Replace Part (3) and repeat if you cannot produce a specific observable condition.
Do not write Part (4) until the test passes.

**(4) Lever efficacy** -- why addressing (3) resolves (2). Explain causally.
Reference (2) by name.

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
> kill-barrier trajectory verdict requirement. That output belongs exclusively to
> Part B."

| Persona | T=0 | T=6mo | T=18mo | Trajectory | Driver of change |
|---------|-----|-------|--------|------------|-----------------|

At least one trajectory non-flat. T=6mo and T=18mo cannot copy T=0 without a stated
reason.

**Part B: KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [Reference the structural persistence property from Phase
5(2) by name. Argue from mechanism, not from the per-persona grid.]

**Relationship to Part A:** [Alignment or divergence -- which structural property
drives both, or why they differ.]

**Required trajectory label** (Citation Architecture row 4):

> **TRAJECTORY VERDICT: [exact direction word -- Resolving, Stable, or Worsening]**

Do not proceed to Phase 7 until written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

- Score distribution (e.g., "2 High, 1 Critical")
- Kill-barrier trajectory: copy the exact TRAJECTORY VERDICT label (Citation
  Architecture row 4). Do not write "Phase 6 Part B." Write the exact label.
- Competitive summary: kill barrier dimension + Phase 2 structural durability basis
- 1--2 sentence rationale tying score distribution, trajectory, and confirmed kill
  barrier

---

## Citation Chain Completeness Audit

**(Citation Architecture row 5 -- required before CCV)**

**Structural duality (required):** The Citation Architecture preamble declared what
would be produced -- it is declarative. This audit confirms what was produced -- it
is confirmatory. These are structurally distinct roles and neither artifact
substitutes for the other. Do not omit this audit on the grounds that the preamble
already established chain structure.

Produce the 5-column audit table below. For each link, write the actual downstream
cite text in the Evidence column. Assign Link type and Verdict from that evidence.

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [write the exact phrase from your Phase 4 trace that names the Phase 1 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [write the exact phrase from your Phase 5(2) that names the Phase 2 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the exact text that WILL appear in AMEND(d)'s "Lever anchor:" field] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Verdict rules:**
- Reference-chain: the Evidence text reproduces the Source artifact label verbatim
  (character-for-character). Verdict: PASS.
- Description-chain: the Evidence text describes or paraphrases rather than copying.
  Verdict: CHAIN INTEGRITY FAILURE -- not "weaker," not "incomplete."
- L3 evidence: write the exact "Lever anchor: [LEVER POINT label]" text that will
  appear in AMEND(d). This is a forward commitment. If you would paraphrase the label
  in AMEND(d), correct it now before proceeding.

**Required aggregate declaration on its own line:**

> "CHAIN COMPLETE: all four links are reference chains."

-- OR --

> "CHAIN BREAK: [list link IDs with CHAIN INTEGRITY FAILURE, e.g., L2] -- return to
> Phase [X] and produce the required named artifact before re-auditing."

**Gate rule:** Do not proceed to the Citation Chain Verification until CHAIN COMPLETE
is written on its own line. If CHAIN BREAK is written, return to the named phase,
correct the artifact, and re-run this audit from the top. Do not proceed until the
audit closes with CHAIN COMPLETE.

---

## Citation Chain Verification

Before writing AMEND, complete all six fields with named text.

1. **Phase 1 artifact name:** [exact text produced in Phase 1]
2. **Phase 2 artifact name:** [exact text produced in Phase 2]
3. **Phase 4 citation:** [exact artifact name from (1) as it appears in Phase 4
   traces]
4. **Phase 5(2) citation:** [exact artifact name from (2) as it appears in Phase
   5(2)]
5. **Phase 5(3) lever label:** [exact LEVER POINT label]
6. **Phase 6 Part B trajectory label:** [exact TRAJECTORY VERDICT label]

A field containing "Phase X" or "see above" without the actual artifact name fails.
Correct the upstream phase before proceeding. Do not write AMEND until all six
fields pass.

---

## AMEND -- Focus, Quantify, Confirm

**Focus persona:** [name -- most exposed to confirmed kill barrier]

**Switching cost (sharpened):** [most precise quantified value]

**Kill barrier for this persona:** [one sentence -- competitive dimension, most acute
because]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete action]
>
> **(b) Root cause addressed:** [name the structural condition from Phase 5(2)]
>
> **(c) Causal mechanism:** [why this lever reaches the structural condition in (2).
> Reference the Phase 5(3) lever point by name.]
>
> **(d) Confirmation signal at T=6mo:**
>
> "Lever anchor: [copy the exact LEVER POINT label from Citation Chain Verification
> step (5) -- this must also match verbatim the Evidence text you wrote in the L3
> row of the Citation Chain Completeness Audit; if the CCV step (5) text and the L3
> Evidence cell text differ by even one character, return to the audit, correct the
> L3 Evidence row to match the exact LEVER POINT label, then re-copy here]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must cite the exact LEVER POINT label and must match the L3 Evidence
cell. Any three-way mismatch between LEVER POINT, CCV step (5), and L3 Evidence is
a chain integrity failure requiring correction before AMEND is complete.
