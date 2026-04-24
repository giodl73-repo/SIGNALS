Written to `simulations/quest/variations/validate-inertia-variations-R12-2026-03-17.md`.

---

## R12 Variations — V-56 through V-60

| # | Label | Axis | Key change from V-55 | Predicted |
|---|-------|------|----------------------|-----------|
| **V-56** | Block positive-only | C-38 partial test | Third paragraph in block: names L3 Evidence as required source; no prohibition | 375/390 |
| **V-57** | Block positive + prohibition | C-38 + C-39 full | Third paragraph in block with explicit "not from Phase 5(3) and not from CCV" | 390/390 |
| **V-58** | Three-axis explicit block | Structural axis | Block reorganized into labeled Axis 1/2/3; Axis 3 carries prohibition; gate lists all three by name | 390/390 |
| **V-59** | Minimal footprint | Phrasing axis | Single appended sentence at end of block: "Derivation constraint: AMEND(d) must derive... not from Phase 5(3) and not from CCV" | 390/390 |
| **V-60** | Full ceiling | All combined | Three-axis block + gate explicitly checks each axis by name; AMEND references "Axis 3" prohibition | 390/390 |

**Structural questions under test:**
- **Q1 (V-56):** Does positive-only in block earn C-38 PARTIAL vs FAIL?
- **Q2 (V-57):** Does positive + prohibition in block earn C-38 + C-39 both PASS?
- **Q3 (V-58):** Does three-axis explicit labeling strengthen enforcement without scoring difference?
- **Q4 (V-59):** Does minimal footprint (single sentence, end of block) suffice, or does placement within the block matter?
- **Q5 (V-60):** Does an explicit per-axis gate check ("block containing Axes 1+2 but omitting Axis 3 fails") further harden C-38/C-39?

The key isolation: V-56 and V-57 are the clean single-axis tests for the two new criteria. V-58, V-59, V-60 probe whether structural form (labeling, footprint, gate granularity) changes the result.
C-39 full, V-57):** Does adding positive + explicit prohibition language
("not from Phase 5(3) or CCV") inside the block earn C-38 PASS (10) + C-39 PASS (10)?

**Q3 (structural axis, V-58):** Does restructuring the block into three explicitly labeled
axes (Axis 1 Duality / Axis 2 Format / Axis 3 Derivation) produce the same C-38+C-39 result
as V-57 while also making partial-axis omission structurally visible?

**Q4 (phrasing axis, V-59):** Does a single compact prohibition sentence appended at the
end of the existing block earn the same C-38+C-39 as V-57, or does placement earlier in the
block matter?

**Q5 (combination, V-60):** Does a gate that explicitly lists all three required axes by name
("Omitting any axis fails this gate") strengthen C-38/C-39 enforcement beyond V-57?

---

### V-56: Block Positive-Only (C-38 partial single-axis test)

**Axis:** Derivation direction added to AUDIT ARCHITECTURE DECLARED block -- positive
instruction only. Names L3 Evidence as required derivation source. Does NOT name Phase 5(3)
or CCV as prohibited sources within the block.
**Hypothesis:** Positive-only in block earns C-38 PARTIAL (5 pts). C-39 requires prohibition
form in block; positive-only earns C-39 FAIL (0). Total: 375/390.
**Change from V-55:** AUDIT ARCHITECTURE DECLARED block gains one additional paragraph
declaring L3 Evidence as derivation authority. No prohibition language in the block. All
other sections identical to V-55.

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

Additionally, a derivation constraint governs downstream use of the L3 artifact. AMEND(d)
must derive its lever anchor from the L3 Evidence column of the Citation Chain Completeness
Audit. The audit's L3 Evidence cell is the derivation authority -- the source AMEND(d) copies
from, not verifies against. This constraint is declared here so it is visible at the same
structural read-point as the artifact declarations and audit format above.

Do not proceed to Phase 1 until "AUDIT ARCHITECTURE DECLARED" is written on its own line
above. The block above is the required output. Its presence confirms that the duality
framing, the full audit column structure (including Evidence-column semantics), and the L3
derivation authority constraint have been declared before Phase 1 begins.

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

### V-57: Block Positive + Prohibition (C-38 + C-39 full single-axis test)

**Axis:** Derivation direction added to AUDIT ARCHITECTURE DECLARED block with explicit
prohibition language. Names L3 Evidence as required source AND names Phase 5(3) and CCV as
forbidden sources, inside the block.
**Hypothesis:** Positive + prohibition in block earns C-38 PASS (10) + C-39 PASS (10).
Total: 390/390.
**Change from V-55:** AUDIT ARCHITECTURE DECLARED block gains a third paragraph with
positive instruction and explicit prohibition ("not from Phase 5(3) and not from CCV").
All other sections identical to V-55 except the required label is updated to reference
the derivation constraint in the block.

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

A third structural constraint is declared here, co-resident with the duality framing and
audit format above. AMEND(d) must derive its lever anchor exclusively from the L3 Evidence
column of the Citation Chain Completeness Audit -- not from Phase 5(3) and not from CCV.
The L3 Evidence cell is the one permitted derivation source. Phase 5(3) and CCV are
prohibited derivation sources for the lever anchor in AMEND(d). This derivation direction
is declared at the architecture-read boundary so that the full constraint -- required source
AND forbidden sources -- is known before any production phase begins.

Do not proceed to Phase 1 until "AUDIT ARCHITECTURE DECLARED" is written on its own line
above. The block above is the required output. Its presence confirms that the duality
framing (preamble's declarative role vs. audit's confirmatory role), the full audit column
structure (including Evidence-column semantics), and the derivation direction constraint
(AMEND(d) derives from L3 Evidence; Phase 5(3) and CCV are prohibited) have all been
declared before Phase 1 begins.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block specifying the audit's structural role, column
> format, and derivation direction constraint. All named artifacts must be produced exactly
> as declared. All downstream cites must copy upstream labels verbatim. AMEND(d) must derive
> its lever anchor from the L3 Evidence column of the audit -- not from Phase 5(3) or CCV.
> The audit must be produced after Phase 7 and must declare CHAIN COMPLETE before the CCV
> gate may proceed."

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
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the exact text that WILL appear in AMEND(d)'s "Lever anchor:" field -- this is a forward commitment; AMEND(d) will copy from this cell, not from Phase 5(3) or CCV] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Verdict rules:**
- Reference-chain: Evidence reproduces Source artifact label verbatim. Verdict: PASS.
- Description-chain: Evidence describes or paraphrases. Verdict: CHAIN INTEGRITY FAILURE --
  not "weaker," not "incomplete."
- L3 forward commitment: the text you write in the L3 Evidence cell is the source AMEND(d)
  will copy from. Write the exact "Lever anchor: [LEVER POINT label]" text as it will appear.
  AMEND(d) does not reconstruct from Phase 5(3) or CCV; it copies from this cell exactly.

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
> CCV step (5) as the source. Both are prohibited derivation sources per the AUDIT
> ARCHITECTURE DECLARED block. The L3 Evidence cell is the one source; copy it verbatim.
>
> "Lever anchor: [copy the exact text from the L3 Evidence cell of the Citation Chain
> Completeness Audit -- do not reconstruct from Phase 5(3) or CCV]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must reproduce the L3 Evidence cell text exactly. The AMEND section is not
complete without the lever anchor and the observable condition.

---

### V-58: Three-Axis Explicit Block (Structural axis)

**Axis:** AUDIT ARCHITECTURE DECLARED block restructured into three explicitly named axes
(Axis 1: Duality / Axis 2: Audit Format / Axis 3: Derivation Direction). Each axis is a
labeled, required section. Prohibition language on Axis 3.
**Hypothesis:** Same C-38 PASS (10) + C-39 PASS (10) as V-57. Explicit axis labeling makes
partial omission structurally visible: a model cannot satisfy two axes while skipping the
third without visibly omitting a labeled required section. Total: 390/390.
**Change from V-55:** AUDIT ARCHITECTURE DECLARED block reorganized into three named axes;
gate condition updated to name all three; Axis 3 carries prohibition language. All phases
identical to V-55 except AMEND(d) references "Axis 3" prohibition and L3 Evidence note is
updated.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?
Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. This architecture declares every
named artifact, exact-copy requirement, and derivation direction constraint before any
production phase begins. The three structural axes governing citation chain integrity are
declared in the AUDIT ARCHITECTURE DECLARED block below. Read the block before Phase 1.

**Named artifacts, required outputs, and verification:**

| # | Phase / Position | Artifact or output | Downstream consumer | Requirement |
|---|------------------|--------------------|---------------------|-------------|
| 1 | Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Exact-copy: copy artifact name, not "Phase 1" |
| 2 | Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Exact-copy: copy artifact name, not "Phase 2" |
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: copy the exact label string verbatim. AMEND(d) must derive its lever anchor FROM the L3 Evidence column of the Citation Chain Completeness Audit -- the audit is the derivation authority; do not construct from Phase 5(3) and retroactively confirm. |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | See AUDIT ARCHITECTURE DECLARED block below (Axes 1--3); CHAIN COMPLETE gate before CCV |

---

**AUDIT ARCHITECTURE DECLARED**

This block declares three co-resident constraints. A model reading this block before Phase 1
knows the audit's structural role (Axis 1), the audit's column format (Axis 2), and the
derivation direction constraint (Axis 3) before executing any phase. All three axes are
required content of this block.

**Axis 1 -- Duality framing:** This output has two structural artifacts serving distinct and
non-substitutable roles. The Citation Architecture preamble (rows 1--5 above) is declarative:
it specifies what will be produced and how it will be cited before any production phase
begins. The Citation Chain Completeness Audit is confirmatory: it verifies what was produced
after all production phases are complete. These roles are structurally distinct. The preamble
cannot confirm chain integrity because it precedes production. The audit cannot declare
artifact names and exact-copy requirements because those must be known before Phase 1.
Neither artifact substitutes for or subsumes the other's function.

**Axis 2 -- Audit format:** The Citation Chain Completeness Audit (row 5) must use the
following 5-column structure for all four links: Source artifact | Consumer site | Evidence
[write actual downstream cite text verbatim -- for L3, write the exact "Lever anchor:
[LEVER POINT label]" text that will appear in AMEND(d); for L1/L2/L4, write the phrase from
the consuming section that names the source artifact character-for-character; write the actual
text produced, not a description or summary; the Evidence cell must be populated with real
text, not a placeholder] | Link type [Reference-chain if Evidence reproduces source artifact
label verbatim; Description-chain if Evidence describes or paraphrases] | Verdict [PASS for
Reference-chain; CHAIN INTEGRITY FAILURE for Description-chain -- not "weaker" or
"incomplete"]. Close with "CHAIN COMPLETE: all four links are reference chains" or "CHAIN
BREAK: [list link IDs] -- return to Phase [X] before proceeding."

**Axis 3 -- Derivation direction:** AMEND(d) must derive its lever anchor from the L3
Evidence column of the Citation Chain Completeness Audit. Phase 5(3) is a prohibited
derivation source for the lever anchor in AMEND(d). CCV is a prohibited derivation source
for the lever anchor in AMEND(d). The L3 Evidence cell is the one permitted source. AMEND(d)
does not construct the anchor independently; it copies from L3 Evidence directly. This
derivation direction and these prohibitions are declared at the architecture-read boundary
so that the full constraint -- required source AND forbidden sources -- is visible before any
reconstruction opportunity arises.

Do not proceed to Phase 1 until "AUDIT ARCHITECTURE DECLARED" is written on its own line
above AND all three axes are present: Axis 1 (duality framing), Axis 2 (5-column audit format
with Evidence semantics), Axis 3 (derivation direction with prohibited sources named). A block
containing only two of three axes fails this gate.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block with three co-resident axes: Axis 1 duality framing,
> Axis 2 audit column format with Evidence semantics, Axis 3 derivation direction with Phase
> 5(3) and CCV named as prohibited sources. All named artifacts must be produced exactly as
> declared. All downstream cites must copy upstream labels verbatim. AMEND(d) must derive its
> lever anchor from the L3 Evidence column -- not from Phase 5(3) or CCV (prohibited per Axis
> 3). The audit must be produced after Phase 7 and must declare CHAIN COMPLETE before the CCV
> gate may proceed."

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

Produce the 5-column audit table using the Axis 2 column structure from AUDIT ARCHITECTURE
DECLARED above. For each link, write the actual downstream cite text in the Evidence column.
Assign Link type and Verdict from that evidence.

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [write the exact phrase from your Phase 4 trace that names the Phase 1 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [write the exact phrase from your Phase 5(2) that names the Phase 2 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the exact text that WILL appear in AMEND(d)'s "Lever anchor:" field -- this is a forward commitment per Axis 3 of AUDIT ARCHITECTURE DECLARED; AMEND(d) copies from this cell, not from Phase 5(3) or CCV] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Verdict rules:**
- Reference-chain: Evidence reproduces Source artifact label verbatim. Verdict: PASS.
- Description-chain: Evidence describes or paraphrases. Verdict: CHAIN INTEGRITY FAILURE --
  not "weaker," not "incomplete."
- L3 forward commitment: the text you write in the L3 Evidence cell is the source AMEND(d)
  copies from per Axis 3. Write the exact "Lever anchor: [LEVER POINT label]" text as it
  will appear. Phase 5(3) and CCV are prohibited sources per Axis 3.

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
> cell is the derivation authority per Axis 3 of AUDIT ARCHITECTURE DECLARED. Copy its
> contents exactly, character-for-character, into the "Lever anchor:" field below. Do not
> reconstruct the anchor from Phase 5(3). Do not use CCV step (5) as the source. Both are
> prohibited derivation sources per Axis 3 of AUDIT ARCHITECTURE DECLARED. The L3 Evidence
> cell is the one permitted source.
>
> "Lever anchor: [copy the exact text from the L3 Evidence cell of the Citation Chain
> Completeness Audit -- Phase 5(3) and CCV are prohibited per Axis 3 of AUDIT ARCHITECTURE
> DECLARED; do not reconstruct]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must reproduce the L3 Evidence cell text exactly. The AMEND section is not
complete without the lever anchor and the observable condition.

---

### V-59: Minimal Footprint Prohibition (Phrasing axis)

**Axis:** Smallest possible addition to the V-55 block that earns C-38 + C-39. A single
compact sentence appended after the column-structure paragraph, before the gate instruction.
Tests whether minimal-footprint at the end of the block is sufficient for pass conditions,
or whether a dedicated paragraph (as in V-57) is required.
**Hypothesis:** Single appended prohibition sentence earns C-38 PASS (10) + C-39 PASS (10).
Placement at end of block should not matter for pass conditions vs. V-57's mid-block paragraph.
Total: 390/390.
**Change from V-55:** One sentence appended to AUDIT ARCHITECTURE DECLARED block before
the gate instruction: "Derivation constraint: AMEND(d) must derive its lever anchor from
the L3 Evidence column of the audit -- not from Phase 5(3) and not from CCV." Gate and
required label updated to reference this constraint. All phases otherwise identical.

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

Derivation constraint: AMEND(d) must derive its lever anchor from the L3 Evidence column
of the Citation Chain Completeness Audit -- not from Phase 5(3) and not from CCV.

Do not proceed to Phase 1 until "AUDIT ARCHITECTURE DECLARED" is written on its own line
above. The block above is the required output. Its presence confirms that the duality
framing, the full audit column structure (including Evidence-column semantics), and the
derivation direction constraint (AMEND(d) derives from L3 Evidence; Phase 5(3) and CCV are
prohibited derivation sources) have been declared before Phase 1 begins.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block specifying the audit's structural role, column
> format, and derivation direction constraint. All named artifacts must be produced exactly
> as declared. All downstream cites must copy upstream labels verbatim. AMEND(d) must derive
> its lever anchor from the L3 Evidence column of the audit -- not from Phase 5(3) or CCV.
> The audit must be produced after Phase 7 and must declare CHAIN COMPLETE before the CCV
> gate may proceed."

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
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the exact text that WILL appear in AMEND(d)'s "Lever anchor:" field -- this is a forward commitment; AMEND(d) will copy from this cell, not from Phase 5(3) or CCV] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Verdict rules:**
- Reference-chain: Evidence reproduces Source artifact label verbatim. Verdict: PASS.
- Description-chain: Evidence describes or paraphrases. Verdict: CHAIN INTEGRITY FAILURE --
  not "weaker," not "incomplete."
- L3 forward commitment: the text you write in the L3 Evidence cell is the source AMEND(d)
  will copy from. Write the exact "Lever anchor: [LEVER POINT label]" text as it will appear.
  AMEND(d) does not reconstruct from Phase 5(3) or CCV; it copies from this cell exactly.

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
> CCV step (5) as the source. Both are prohibited derivation sources per the AUDIT
> ARCHITECTURE DECLARED block. The L3 Evidence cell is the one source; copy it verbatim.
>
> "Lever anchor: [copy the exact text from the L3 Evidence cell of the Citation Chain
> Completeness Audit -- do not reconstruct from Phase 5(3) or CCV]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must reproduce the L3 Evidence cell text exactly. The AMEND section is not
complete without the lever anchor and the observable condition.

---

### V-60: Full Ceiling (All combined)

**Axis:** Three-axis block (V-58 structure) with explicit per-axis gate condition listing all
three axes by name + AMEND prohibition references the block by axis name. The gate explicitly
states that a block containing only two of three axes fails. Combines V-57 (prohibition in
block) and V-58 (three-axis explicit structure) into the cleanest enforcement model for both
C-38 and C-39.
**Hypothesis:** 390/390. Same C-38 PASS + C-39 PASS as V-57/V-58. The explicit three-axis
gate with named check eliminates the possibility of omitting Axis 3 without a visible gate
failure. This is the strongest enforcement shape for the two new criteria.
**Change from V-55:** Three-axis block (per V-58) with explicit gate listing all three axes +
AMEND references "Axis 3" prohibition explicitly. This is the recommended production variant.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?
Complete each phase in sequence. Each phase gates the next.

---

## Citation Architecture

Read this section once, in full, before Phase 1 begins. This architecture declares every
named artifact, exact-copy requirement, and derivation direction constraint before any
production phase begins. The three structural axes governing citation chain integrity are
declared in the AUDIT ARCHITECTURE DECLARED block below. Read the block before Phase 1.

**Named artifacts, required outputs, and verification:**

| # | Phase / Position | Artifact or output | Downstream consumer | Requirement |
|---|------------------|--------------------|---------------------|-------------|
| 1 | Phase 1 | "SCORING INFRASTRUCTURE DECLARED" | Phase 4 methodology traces | Exact-copy: copy artifact name, not "Phase 1" |
| 2 | Phase 2 | "PERSONA INVENTORY DECLARED" | Phase 5(2) structural persistence | Exact-copy: copy artifact name, not "Phase 2" |
| 3 | Phase 5(3) | "LEVER POINT: [label]" | CCV (5); AMEND(d) | Exact-copy: copy the exact label string verbatim. AMEND(d) must derive its lever anchor FROM the L3 Evidence column of the Citation Chain Completeness Audit -- the audit is the derivation authority; do not construct from Phase 5(3) and retroactively confirm. |
| 4 | Phase 6 Part B | "TRAJECTORY VERDICT: [direction]" | Phase 7; CCV (6) | Exact-copy: copy the exact direction word |
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | See AUDIT ARCHITECTURE DECLARED block below (Axes 1--3); CHAIN COMPLETE gate before CCV |

---

**AUDIT ARCHITECTURE DECLARED**

This block declares three co-resident constraints. A model reading this block before Phase 1
knows all three architecture constraints before executing any phase. All three axes are
required content of this block. A block missing any axis is an incomplete architecture
declaration.

**Axis 1 -- Duality framing:** This output has two structural artifacts serving distinct and
non-substitutable roles. The Citation Architecture preamble (rows 1--5 above) is declarative:
it specifies what will be produced and how it will be cited before any production phase
begins. The Citation Chain Completeness Audit is confirmatory: it verifies what was produced
after all production phases are complete. These roles are structurally distinct. The preamble
cannot confirm chain integrity because it precedes production. The audit cannot declare
artifact names and exact-copy requirements because those must be known before Phase 1.
Neither artifact substitutes for or subsumes the other's function.

**Axis 2 -- Audit format:** The Citation Chain Completeness Audit (row 5) must use the
following 5-column structure for all four links: Source artifact | Consumer site | Evidence
[write actual downstream cite text verbatim -- for L3, write the exact "Lever anchor:
[LEVER POINT label]" text that will appear in AMEND(d); for L1/L2/L4, write the phrase from
the consuming section that names the source artifact character-for-character; write the actual
text produced, not a description or summary; the Evidence cell must be populated with real
text, not a placeholder] | Link type [Reference-chain if Evidence reproduces source artifact
label verbatim; Description-chain if Evidence describes or paraphrases] | Verdict [PASS for
Reference-chain; CHAIN INTEGRITY FAILURE for Description-chain -- not "weaker" or
"incomplete"]. Close with "CHAIN COMPLETE: all four links are reference chains" or "CHAIN
BREAK: [list link IDs] -- return to Phase [X] before proceeding."

**Axis 3 -- Derivation direction:** AMEND(d) must derive its lever anchor from the L3
Evidence column of the Citation Chain Completeness Audit. Phase 5(3) is a prohibited
derivation source for the lever anchor in AMEND(d). CCV is a prohibited derivation source
for the lever anchor in AMEND(d). The L3 Evidence cell is the one permitted source. AMEND(d)
does not construct the anchor independently and retroactively confirm; it copies from L3
Evidence directly. This derivation direction and these prohibitions are declared at the
architecture-read boundary so that the full constraint -- required source AND forbidden
sources -- is known before any production phase begins.

Do not proceed to Phase 1 until all of the following are confirmed above:
- "AUDIT ARCHITECTURE DECLARED" is written on its own line.
- Axis 1 (duality framing: declarative vs. confirmatory structural roles) is present.
- Axis 2 (5-column audit format with Evidence-column semantics) is present.
- Axis 3 (derivation direction with Phase 5(3) and CCV named as prohibited sources) is present.
A block containing Axes 1 and 2 but omitting Axis 3 fails this gate.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block with three co-resident axes: Axis 1 duality framing,
> Axis 2 audit column format with Evidence semantics, Axis 3 derivation direction with Phase
> 5(3) and CCV named as prohibited sources. All named artifacts must be produced exactly as
> declared. All downstream cites must copy upstream labels verbatim. AMEND(d) must derive its
> lever anchor from the L3 Evidence column -- not from Phase 5(3) or CCV (Axis 3 prohibition).
> The audit must be produced after Phase 7 and must declare CHAIN COMPLETE before the CCV
> gate may proceed."

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

Produce the 5-column audit table using the Axis 2 column structure from AUDIT ARCHITECTURE
DECLARED above. For each link, write the actual downstream cite text in the Evidence column.
Assign Link type and Verdict from that evidence.

| Link | Source artifact | Consumer site | Evidence (write actual downstream cite text) | Link type | Verdict |
|------|----------------|---------------|---------------------------------------------|-----------|---------|
| L1 | [exact Phase 1 artifact name] | Phase 4 methodology traces | [write the exact phrase from your Phase 4 trace that names the Phase 1 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L2 | [exact Phase 2 artifact name] | Phase 5(2) structural persistence | [write the exact phrase from your Phase 5(2) that names the Phase 2 artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L3 | [exact LEVER POINT label] | AMEND(d) lever anchor | [write the exact text that WILL appear in AMEND(d)'s "Lever anchor:" field -- this is a forward commitment per Axis 3 of AUDIT ARCHITECTURE DECLARED; AMEND(d) copies from this cell only; Phase 5(3) and CCV are prohibited sources per Axis 3] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |
| L4 | [exact TRAJECTORY VERDICT label] | Phase 7 trajectory cite | [write the exact phrase from your Phase 7 that names the Phase 6 Part B artifact] | [Reference-chain / Description-chain] | [PASS / CHAIN INTEGRITY FAILURE] |

**Verdict rules:**
- Reference-chain: Evidence reproduces Source artifact label verbatim. Verdict: PASS.
- Description-chain: Evidence describes or paraphrases. Verdict: CHAIN INTEGRITY FAILURE --
  not "weaker," not "incomplete."
- L3 forward commitment: per Axis 3 of AUDIT ARCHITECTURE DECLARED, the text you write in
  the L3 Evidence cell is the source AMEND(d) copies from. Write the exact "Lever anchor:
  [LEVER POINT label]" text as it will appear. Phase 5(3) and CCV are prohibited.

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
> cell is the derivation authority per Axis 3 of AUDIT ARCHITECTURE DECLARED. Copy its
> contents exactly, character-for-character, into the "Lever anchor:" field below. Do not
> reconstruct the anchor from Phase 5(3). Do not use CCV step (5) as the source. Both are
> prohibited derivation sources per Axis 3 of AUDIT ARCHITECTURE DECLARED. The L3 Evidence
> cell is the one permitted source.
>
> "Lever anchor: [copy the exact text from the L3 Evidence cell of the Citation Chain
> Completeness Audit -- Phase 5(3) and CCV are prohibited per Axis 3 of AUDIT ARCHITECTURE
> DECLARED; do not reconstruct]."
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

The lever anchor must reproduce the L3 Evidence cell text exactly. The AMEND section is not
complete without the lever anchor and the observable condition.

---

## R12 Structural Summary

| Variation | Block derivation direction? | Block prohibition? | C-38 predicted | C-39 predicted | Total predicted |
|-----------|----------------------------|-------------------|----------------|----------------|-----------------|
| V-55 (baseline) | NO | NO | FAIL (0) | FAIL (0) | 370/390 |
| V-56 | YES (positive-only) | NO | PARTIAL (5) | FAIL (0) | 375/390 |
| V-57 | YES (paragraph, positive+prohibition) | YES | PASS (10) | PASS (10) | 390/390 |
| V-58 | YES (Axis 3, positive+prohibition) | YES | PASS (10) | PASS (10) | 390/390 |
| V-59 | YES (single sentence, positive+prohibition) | YES | PASS (10) | PASS (10) | 390/390 |
| V-60 | YES (Axis 3, positive+prohibition+explicit gate) | YES | PASS (10) | PASS (10) | 390/390 |
