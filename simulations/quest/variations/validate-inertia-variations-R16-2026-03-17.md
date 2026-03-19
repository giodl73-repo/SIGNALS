Written to `simulations/quest/variations/validate-inertia-variations-R16-2026-03-17.md`.

---

## R16 Variations -- V-76 through V-80

| # | Label | C-43 | C-44 | Predicted |
|---|-------|------|------|-----------|
| **V-76** | Ceiling: both disqualifiers + placement receipt | PASS | PASS | **440** |
| **V-77** | Mirror split-gate disqualifier omitted | PASS | PARTIAL | **435** |
| **V-78** | Label cites impossibility source only | PARTIAL | PASS | **435** |
| **V-79** | Label names artifact, no block body provenance | FAIL | PASS | **430** |
| **V-80** | V-71 shape re-run under v16 | PASS | FAIL | **430** |

---

**What varies and why:**

The sole structural manipulation is across two independent dimensions of the AUDIT ARCHITECTURE DECLARED block:

**Dimension 1 (C-44):** Whether the block instruction body names both split-gate failure modes as explicit disqualifiers. V-76/V-78/V-79 add both (PASS); V-77 adds only the axis-body/impossibility-label shape and omits the mirror (PARTIAL); V-80 adds neither (FAIL — V-71 shape).

**Dimension 2 (C-43):** Whether the produced architecture label cites the block body as the explicit source of both gate components. V-76/V-77/V-80 use the V-71 label unchanged — "in the block body names all three axes by label and declares partial axis coverage a gate failure" — which already satisfies C-43 (PASS). V-78 modifies the label to cite the block body only for the impossibility statement (PARTIAL). V-79 replaces the placement receipt sentence entirely with a description that names the artifact without block-body provenance (FAIL).

**Key discriminators:**
- V-77 and V-78 both score 435 but fail on different axes — C-44 vs C-43 PARTIAL respectively
- V-79 and V-80 both score 430 as complementary inversions: C-43 FAIL + C-44 PASS vs C-43 PASS + C-44 FAIL. These are the primary discrimination tests for the two new criteria.
block body
   as the source of BOTH axis enumeration AND the impossibility statement? Both cited = PASS;
   one cited = PARTIAL; neither cited = FAIL.
2. **C-44** (split-gate self-rejection): Does the block instruction body name BOTH split-gate
   failure modes (axis-body/impossibility-label AND impossibility-body/axis-label) as explicit
   disqualifiers? Both named = PASS; one named = PARTIAL; neither named = FAIL.

**Key structural questions R16 tests:**
- V-76 confirms the 440 ceiling is reachable by satisfying both C-43 and C-44 simultaneously.
- V-77 and V-78 both predict 435 but through different partial shapes: V-77 fails C-44 (block
  body misses the mirror disqualifier); V-78 fails C-43 (label misses axis enumeration
  provenance). The rubric must assign PARTIAL via two distinct structural diagnoses.
- V-79 and V-80 both predict 430 through complementary shapes: V-79 earns C-44 PASS + C-43
  FAIL; V-80 earns C-43 PASS + C-44 FAIL. These are the primary C-43 vs. C-44 discrimination
  tests -- same total score, different failure axis.

---

### V-76: Ceiling -- C-43 PASS + C-44 PASS (440/440)

**Axis:** AUDIT ARCHITECTURE DECLARED block body (1) places both gate components in the block
body (C-41/C-42 PASS shape from V-71), (2) names both split-gate failure modes as explicit
disqualifiers within the block body (C-44 PASS), and the produced architecture label (3) cites
the block instruction body as the explicit source of both gate components (C-43 PASS).
**Hypothesis:** C-41 PASS (10 pts) + C-42 PASS (10 pts) + C-43 PASS (10 pts) + C-44 PASS
(10 pts) + C-01--C-40 = 400 pts. Ceiling: 440/440.
**Change from V-71:** Block body gate check section extended with two explicit split-gate
disqualifiers naming both failure modes by configuration shape. Produced architecture label
unchanged from V-71 (already satisfies C-43 -- "in the block body names all three axes by
label and declares partial axis coverage a gate failure" cites the block body as source of
both components). All phases, CCV, and AMEND identical to V-71.

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

This block declares three co-resident axes. A model reading this block before Phase 1 knows
all three architecture constraints before executing any phase. All three axes are required
content of this block. A block missing any axis is an incomplete architecture declaration.

**Axis 1 -- Duality framing:** This output has two structural artifacts serving distinct and
non-substitutable roles. The Citation Architecture preamble (rows 1--5 above) is declarative:
it specifies what will be produced and how it will be cited before any production phase begins.
The Citation Chain Completeness Audit is confirmatory: it verifies what was produced after all
production phases are complete. These roles are structurally distinct. The preamble cannot
confirm chain integrity because it precedes production. The audit cannot declare artifact names
and exact-copy requirements because those must be known before Phase 1. Neither artifact
substitutes for or subsumes the other's function.

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
- Axis 2 (audit format: 5-column structure with Evidence-column semantics) is present.
- Axis 3 (derivation direction: L3 Evidence required; Phase 5(3) and CCV prohibited) is present.
A block containing Axes 1 and 2 but omitting Axis 3 fails this gate. A block containing any
two of the three axes while omitting the third fails this gate. Partial axis coverage is not
partial compliance -- it is a gate failure. All three axes must be declared before Phase 1 begins.
A block gate instruction body that names all three axes in this block body but displaces the
impossibility statement exclusively to the produced architecture label is a split-gate failure
and fails this gate. A block gate instruction body that declares the impossibility statement in
this block body but displaces axis enumeration exclusively to the produced architecture label is
the mirror split-gate failure and also fails this gate. Both split-gate configurations are named
disqualifiers. Both gate components -- axis enumeration and impossibility statement -- must
reside in this block body to satisfy this gate. Displacing either component exclusively to the
produced architecture label fails this gate regardless of which component is displaced.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block with three co-resident axes (Axis 1: duality framing,
> Axis 2: audit format, Axis 3: derivation direction). The block gate instruction in the block
> body names all three axes by label and declares partial axis coverage a gate failure. All
> named artifacts must be produced exactly as declared. All downstream cites must copy upstream
> labels verbatim. AMEND(d) must derive its lever anchor from the L3 Evidence column -- not
> from Phase 5(3) or CCV (Axis 3 prohibition). The audit must be produced after Phase 7 and
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


### V-77: C-44 PARTIAL -- One Split-Gate Shape Named, Mirror Omitted

**Axis:** Block body names the axis-body/impossibility-label split-gate failure mode as an
explicit disqualifier, but omits the mirror shape (impossibility-body/axis-label). One of the
two required C-44 disqualifiers is present; its mirror is absent. The produced architecture
label is identical to V-76 (C-43 PASS).
**Hypothesis:** C-41 PASS (10 pts) + C-42 PASS (10 pts) + C-43 PASS (10 pts) + C-44 PARTIAL
(5 pts) + C-01--C-40 = 400 pts. Total predicted: 435/440.
**Change from V-76:** Block body split-gate disqualifier section retains the first disqualifier
(axis-body/impossibility-label shape named as a gate failure) but removes the mirror
disqualifier (impossibility-body/axis-label shape). C-44 rubric: naming one shape but not its
mirror earns PARTIAL. All phases, CCV, and AMEND identical to V-76.

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

This block declares three co-resident axes. A model reading this block before Phase 1 knows
all three architecture constraints before executing any phase. All three axes are required
content of this block. A block missing any axis is an incomplete architecture declaration.

**Axis 1 -- Duality framing:** This output has two structural artifacts serving distinct and
non-substitutable roles. The Citation Architecture preamble (rows 1--5 above) is declarative:
it specifies what will be produced and how it will be cited before any production phase begins.
The Citation Chain Completeness Audit is confirmatory: it verifies what was produced after all
production phases are complete. These roles are structurally distinct. The preamble cannot
confirm chain integrity because it precedes production. The audit cannot declare artifact names
and exact-copy requirements because those must be known before Phase 1. Neither artifact
substitutes for or subsumes the other's function.

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
- Axis 2 (audit format: 5-column structure with Evidence-column semantics) is present.
- Axis 3 (derivation direction: L3 Evidence required; Phase 5(3) and CCV prohibited) is present.
A block containing Axes 1 and 2 but omitting Axis 3 fails this gate. A block containing any
two of the three axes while omitting the third fails this gate. Partial axis coverage is not
partial compliance -- it is a gate failure. All three axes must be declared before Phase 1 begins.
A block gate instruction body that names all three axes in this block body but displaces the
impossibility statement exclusively to the produced architecture label is a split-gate failure
and fails this gate.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block with three co-resident axes (Axis 1: duality framing,
> Axis 2: audit format, Axis 3: derivation direction). The block gate instruction in the block
> body names all three axes by label and declares partial axis coverage a gate failure. All
> named artifacts must be produced exactly as declared. All downstream cites must copy upstream
> labels verbatim. AMEND(d) must derive its lever anchor from the L3 Evidence column -- not
> from Phase 5(3) or CCV (Axis 3 prohibition). The audit must be produced after Phase 7 and
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


### V-78: C-43 PARTIAL -- Label Cites Source of One Gate Component Only

**Axis:** Block body places both gate components in the block body AND names both split-gate
failure modes as explicit disqualifiers (C-44 PASS, C-41 PASS, C-42 PASS). The produced
architecture label attributes the impossibility statement to "in the block body" but describes
axis enumeration without citing the block body as its named source -- producing a C-43 PARTIAL
shape (impossibility-statement provenance cited; axis-enumeration provenance uncited).
**Hypothesis:** C-41 PASS (10 pts) + C-42 PASS (10 pts) + C-43 PARTIAL (5 pts) + C-44 PASS
(10 pts) + C-01--C-40 = 400 pts. Total predicted: 435/440.
**Change from V-76:** Block gate section identical to V-76 (both split-gate disqualifiers
present). Produced architecture label modified: the sentence "The block gate instruction in
the block body names all three axes by label and declares partial axis coverage a gate
failure" is replaced with a two-sentence form that attributes the impossibility statement to
"in the block body" but states axis enumeration without a block-body source marker. All
phases, CCV, and AMEND identical to V-76.

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

This block declares three co-resident axes. A model reading this block before Phase 1 knows
all three architecture constraints before executing any phase. All three axes are required
content of this block. A block missing any axis is an incomplete architecture declaration.

**Axis 1 -- Duality framing:** This output has two structural artifacts serving distinct and
non-substitutable roles. The Citation Architecture preamble (rows 1--5 above) is declarative:
it specifies what will be produced and how it will be cited before any production phase begins.
The Citation Chain Completeness Audit is confirmatory: it verifies what was produced after all
production phases are complete. These roles are structurally distinct. The preamble cannot
confirm chain integrity because it precedes production. The audit cannot declare artifact names
and exact-copy requirements because those must be known before Phase 1. Neither artifact
substitutes for or subsumes the other's function.

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
- Axis 2 (audit format: 5-column structure with Evidence-column semantics) is present.
- Axis 3 (derivation direction: L3 Evidence required; Phase 5(3) and CCV prohibited) is present.
A block containing Axes 1 and 2 but omitting Axis 3 fails this gate. A block containing any
two of the three axes while omitting the third fails this gate. Partial axis coverage is not
partial compliance -- it is a gate failure. All three axes must be declared before Phase 1 begins.
A block gate instruction body that names all three axes in this block body but displaces the
impossibility statement exclusively to the produced architecture label is a split-gate failure
and fails this gate. A block gate instruction body that declares the impossibility statement in
this block body but displaces axis enumeration exclusively to the produced architecture label is
the mirror split-gate failure and also fails this gate. Both split-gate configurations are named
disqualifiers. Both gate components -- axis enumeration and impossibility statement -- must
reside in this block body to satisfy this gate. Displacing either component exclusively to the
produced architecture label fails this gate regardless of which component is displaced.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block with three co-resident axes (Axis 1: duality framing,
> Axis 2: audit format, Axis 3: derivation direction). The block gate instruction in the block
> body declares partial axis coverage a gate failure. The three required axes -- Axis 1
> (duality framing), Axis 2 (audit format), and Axis 3 (derivation direction) -- must all be
> declared before Phase 1 may begin. All named artifacts must be produced exactly as declared.
> All downstream cites must copy upstream labels verbatim. AMEND(d) must derive its lever
> anchor from the L3 Evidence column -- not from Phase 5(3) or CCV (Axis 3 prohibition). The
> audit must be produced after Phase 7 and must declare CHAIN COMPLETE before the CCV gate
> may proceed."

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


### V-79: C-43 FAIL -- Label Names Artifact Without Block Body Provenance

**Axis:** Block body places both gate components in the block body AND names both split-gate
failure modes as explicit disqualifiers (C-44 PASS, C-41 PASS, C-42 PASS). The produced
architecture label names the AUDIT ARCHITECTURE DECLARED artifact and describes its content
("three co-resident axes," "partial axis coverage fails the gate") but does not cite the
block instruction body as the explicit source of either gate component -- producing a C-43
FAIL shape. The label confirms the artifact and its gate requirement exist, but provides no
placement receipt auditable to the block body.
**Hypothesis:** C-41 PASS (10 pts) + C-42 PASS (10 pts) + C-43 FAIL (0 pts) + C-44 PASS
(10 pts) + C-01--C-40 = 400 pts. Total predicted: 430/440.
**Change from V-76:** Block gate section identical to V-76 (both split-gate disqualifiers
present, both gate components in block body). Produced architecture label modified: the
placement receipt sentence ("The block gate instruction in the block body names all three
axes by label and declares partial axis coverage a gate failure") is replaced with a
gate-description sentence that restates the requirement without attributing either component's
location to the block body. C-43 rubric: "a produced label that satisfies the C-37 named
artifact requirement without citing the block body as the explicit source of both components
fails C-43." All phases, CCV, and AMEND identical to V-76.

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

This block declares three co-resident axes. A model reading this block before Phase 1 knows
all three architecture constraints before executing any phase. All three axes are required
content of this block. A block missing any axis is an incomplete architecture declaration.

**Axis 1 -- Duality framing:** This output has two structural artifacts serving distinct and
non-substitutable roles. The Citation Architecture preamble (rows 1--5 above) is declarative:
it specifies what will be produced and how it will be cited before any production phase begins.
The Citation Chain Completeness Audit is confirmatory: it verifies what was produced after all
production phases are complete. These roles are structurally distinct. The preamble cannot
confirm chain integrity because it precedes production. The audit cannot declare artifact names
and exact-copy requirements because those must be known before Phase 1. Neither artifact
substitutes for or subsumes the other's function.

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
- Axis 2 (audit format: 5-column structure with Evidence-column semantics) is present.
- Axis 3 (derivation direction: L3 Evidence required; Phase 5(3) and CCV prohibited) is present.
A block containing Axes 1 and 2 but omitting Axis 3 fails this gate. A block containing any
two of the three axes while omitting the third fails this gate. Partial axis coverage is not
partial compliance -- it is a gate failure. All three axes must be declared before Phase 1 begins.
A block gate instruction body that names all three axes in this block body but displaces the
impossibility statement exclusively to the produced architecture label is a split-gate failure
and fails this gate. A block gate instruction body that declares the impossibility statement in
this block body but displaces axis enumeration exclusively to the produced architecture label is
the mirror split-gate failure and also fails this gate. Both split-gate configurations are named
disqualifiers. Both gate components -- axis enumeration and impossibility statement -- must
reside in this block body to satisfy this gate. Displacing either component exclusively to the
produced architecture label fails this gate regardless of which component is displaced.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block with three co-resident axes (Axis 1: duality framing,
> Axis 2: audit format, Axis 3: derivation direction). All three axes are required before
> Phase 1; partial axis coverage fails the gate. All named artifacts must be produced exactly
> as declared. All downstream cites must copy upstream labels verbatim. AMEND(d) must derive
> its lever anchor from the L3 Evidence column -- not from Phase 5(3) or CCV (Axis 3
> prohibition). The audit must be produced after Phase 7 and must declare CHAIN COMPLETE
> before the CCV gate may proceed."

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


### V-80: C-43 PASS, C-44 FAIL -- V-71 Shape Re-Confirmed Under v16

**Axis:** Structurally identical to V-71 (R15 ceiling): both gate components in the block
body (C-41/C-42 PASS), produced label cites block body as source of both components (C-43
PASS -- "in the block body names all three axes by label and declares partial axis coverage
a gate failure"). No split-gate disqualifiers in the block body (C-44 FAIL -- block body
contains both gate components but names neither split-gate configuration as a disqualifier).
**Hypothesis:** C-41 PASS (10 pts) + C-42 PASS (10 pts) + C-43 PASS (10 pts) + C-44 FAIL
(0 pts) + C-01--C-40 = 400 pts. Total predicted: 430/440.
**Change from V-71:** None. This is V-71 reproduced exactly and scored against the v16 rubric
to confirm two predictions: (a) the C-43 PASS that V-71 already achieves holds under v16
(the placement receipt sentence already in V-71's label is sufficient); (b) C-44 FAIL is the
correct score for a block body that has both gate components without naming either split-gate
configuration as a disqualifier. Complement to V-79: both predict 430, but V-79 earns that
score via C-43 FAIL + C-44 PASS; V-80 earns it via C-43 PASS + C-44 FAIL.

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

This block declares three co-resident axes. A model reading this block before Phase 1 knows
all three architecture constraints before executing any phase. All three axes are required
content of this block. A block missing any axis is an incomplete architecture declaration.

**Axis 1 -- Duality framing:** This output has two structural artifacts serving distinct and
non-substitutable roles. The Citation Architecture preamble (rows 1--5 above) is declarative:
it specifies what will be produced and how it will be cited before any production phase begins.
The Citation Chain Completeness Audit is confirmatory: it verifies what was produced after all
production phases are complete. These roles are structurally distinct. The preamble cannot
confirm chain integrity because it precedes production. The audit cannot declare artifact names
and exact-copy requirements because those must be known before Phase 1. Neither artifact
substitutes for or subsumes the other's function.

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
- Axis 2 (audit format: 5-column structure with Evidence-column semantics) is present.
- Axis 3 (derivation direction: L3 Evidence required; Phase 5(3) and CCV prohibited) is present.
A block containing Axes 1 and 2 but omitting Axis 3 fails this gate. A block containing any
two of the three axes while omitting the third fails this gate. Partial axis coverage is not
partial compliance -- it is a gate failure. All three axes must be declared before Phase 1 begins.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block with three co-resident axes (Axis 1: duality framing,
> Axis 2: audit format, Axis 3: derivation direction). The block gate instruction in the block
> body names all three axes by label and declares partial axis coverage a gate failure. All
> named artifacts must be produced exactly as declared. All downstream cites must copy upstream
> labels verbatim. AMEND(d) must derive its lever anchor from the L3 Evidence column -- not
> from Phase 5(3) or CCV (Axis 3 prohibition). The audit must be produced after Phase 7 and
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
