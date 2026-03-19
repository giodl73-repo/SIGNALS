Written to `simulations/quest/variations/validate-inertia-variations-R15-2026-03-17.md`.

---

## R15 Variations -- V-71 through V-75

| # | Label | Axis | Predicted |
|---|-------|------|-----------|
| **V-71** | Ceiling: both components in block body | C-41 PASS + C-42 PASS | **420** |
| **V-72** | Axes in body, impossibility in label | C-41 PARTIAL + C-42 PARTIAL | **410** |
| **V-73** | Impossibility in body, axes in label | C-41 PARTIAL + C-42 PARTIAL | **410** |
| **V-74** | Both in produced label only | C-41 PARTIAL (named) + C-42 FAIL | **405** |
| **V-75** | Redundant full gate in body AND label | C-41 PASS + C-42 PASS | **420** |

---

**What varies and why:**

The sole structural manipulation across all five is the AUDIT ARCHITECTURE DECLARED block — specifically, which gate components live in the block body vs. the produced architecture label. Phases 1–7, the audit table, CCV, and AMEND are identical across all variations.

**Two gate components:**
1. Axis enumeration — naming Axis 1, Axis 2, Axis 3 by label
2. Impossibility statement — "partial coverage is not partial compliance; it is a gate failure"

**Key question C-42 adds:** V-74 is the critical test. C-41 gives it PARTIAL (5 pts) via its named PARTIAL condition — "full per-axis gate in produced label only." C-42 gives it FAIL (0 pts) because both components are in the label only. This is the only shape where C-41 and C-42 diverge, making V-74 the primary differentiation test for the new criterion.

**V-75** (redundant dual-site) tests the inverse question: when the block body has everything already, does the label also having it create a split? It shouldn't — duplication is not division.
that the presence of gate components in the label does not create a disqualifying split when both components are also present in the body.

**C-42 scoring reference:**

| Shape | C-40 | C-41 | C-42 | Pts from these three |
|-------|------|------|------|----------------------|
| Both in block body (V-71, V-75) | PASS | PASS | PASS | 30 |
| Axes in body, impossibility in label (V-72) | PARTIAL | PARTIAL | PARTIAL | 15 |
| Impossibility in body, axes in label (V-73) | PARTIAL | PARTIAL | PARTIAL | 15 |
| Both in produced label only (V-74) | PARTIAL | PARTIAL | FAIL | 10 |

Baseline (C-01--C-39): 390 pts. Total predicted = 390 + above.

**Key isolation:** V-74 is the critical C-42 test. Under C-41, "both in produced label" earns
the named PARTIAL (5 pts). Under C-42, the same shape earns FAIL (0 pts). V-74 tests whether
the rubric's explicit FAIL verdict fires independently of C-41's explicit PARTIAL verdict --
i.e., that a response can earn C-41 PARTIAL while simultaneously earning C-42 FAIL. V-72 and
V-73 test the PARTIAL/PARTIAL symmetry for the two split shapes, confirming that partial body
coverage yields C-42 PARTIAL not FAIL. V-75 tests that duplication in the label does not
retroactively create a split.

---

### V-71: Ceiling -- Both Components in Block Body (C-41 PASS + C-42 PASS)

**Axis:** AUDIT ARCHITECTURE DECLARED block gate instruction places BOTH gate components --
axis enumeration (all three axes named by label) AND impossibility statement (partial coverage
is a gate failure) -- entirely in the block body. The produced architecture label acknowledges
the block gate without restating it. Both C-41 and C-42 should score PASS.
**Hypothesis:** C-40 PASS (10 pts) + C-41 PASS (10 pts) + C-42 PASS (10 pts). C-01--C-39 =
390 pts. Ceiling: 420/420.
**Change from V-66 (R14 ceiling):** Structurally identical to V-66. Re-run under the v15
rubric to confirm that the new C-42 criterion scores PASS for this shape and that the ceiling
is now 420 not 410. All phases, CCV, and AMEND identical to V-66.

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


### V-72: Axes in Block Body, Impossibility in Produced Label (C-42 PARTIAL test)

**Axis:** AUDIT ARCHITECTURE DECLARED block body names all three axes by label (Axis 1, Axis
2, Axis 3) but contains NO impossibility statement. The impossibility statement -- "A block
missing any axis fails this gate; partial axis coverage is not partial compliance" -- is
displaced exclusively to the produced architecture label. One gate component (axis
enumeration) is in the block body; the other gate component (impossibility declaration) is in
the label. This is the split shape mapped to C-42 PARTIAL in the rubric's verdict table.
**Hypothesis:** C-40 PARTIAL (5 pts) -- axes named in block body, impossibility absent from
block body. C-41 PARTIAL (5 pts) -- full gate not in block body (impossibility component
missing). C-42 PARTIAL (5 pts) -- split shape: one component in body, one exclusively in
label. C-01--C-39 = 390 pts. Total predicted: 410/420.
**Change from V-71:** Block gate body retains all three axis declarations but strips the
impossibility statement entirely. The produced label receives the impossibility clause in
addition to its standard content. All phases, CCV, and AMEND identical to V-71.

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

Do not proceed to Phase 1 until "AUDIT ARCHITECTURE DECLARED" is written on its own line
above and all three axes (Axis 1, Axis 2, Axis 3) are present in this block.

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
> Axis 2: audit format, Axis 3: derivation direction). A block missing any of these three axes
> fails its gate. A block containing Axes 1 and 2 but omitting Axis 3 fails its gate. A block
> containing any two axes while omitting the third fails its gate. Partial axis coverage is not
> partial compliance -- it is a gate failure. All named artifacts must be produced exactly as
> declared. All downstream cites must copy upstream labels verbatim. AMEND(d) must derive its
> lever anchor from the L3 Evidence column -- not from Phase 5(3) or CCV (Axis 3 prohibition).
> The audit must be produced after Phase 7 and must declare CHAIN COMPLETE before the CCV gate
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


### V-73: Impossibility in Block Body, Axes in Produced Label (C-42 PARTIAL mirror)

**Axis:** AUDIT ARCHITECTURE DECLARED block body contains the impossibility statement --
"Partial axis coverage is not partial compliance -- it is a gate failure. All three axes must
be declared before Phase 1 begins." -- but does NOT name any of the three axes by label. The
three axis labels (Axis 1: duality framing, Axis 2: audit format, Axis 3: derivation
direction) are displaced exclusively to the produced architecture label. One gate component
(impossibility declaration) is in the block body; the other gate component (axis enumeration)
is in the label. Mirror shape of V-72.
**Hypothesis:** C-40 PARTIAL (5 pts) -- block body lacks axis labels (no axis named by label
in block body). C-41 PARTIAL (5 pts) -- full gate not in block body (axis enumeration
component missing). C-42 PARTIAL (5 pts) -- split shape, mirror of V-72. C-01--C-39 = 390.
Total predicted: 410/420.
**Change from V-72:** Axis labels stripped from block body; impossibility statement moved to
block body in their place. Produced label now carries the axis enumeration that V-72's label
carried as its impossibility clause. All phases, CCV, and AMEND identical to V-71.

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

This block is the required architecture declaration for citation chain integrity. The three
axes governing audit structure and derivation direction are defined for this output. This
block declares the gate condition: partial axis coverage is not partial compliance -- it is a
gate failure. A block that omits any axis fails this gate regardless of which axes are present.
All three axes must be declared before Phase 1 begins.

Do not proceed to Phase 1 until "AUDIT ARCHITECTURE DECLARED" is written on its own line
above and the gate condition declared in this block is satisfied.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block. The block contains three co-resident axes that must
> all be present: Axis 1 (duality framing: declarative vs. confirmatory structural roles --
> the Citation Architecture preamble is declarative, specifying artifacts before production;
> the Citation Chain Completeness Audit is confirmatory, verifying artifacts after production;
> these roles are structurally distinct and neither substitutes for the other), Axis 2 (audit
> format: the Audit must use a 5-column structure -- Source artifact, Consumer site, Evidence
> [write actual downstream cite text verbatim; the Evidence cell must contain real text, not a
> placeholder], Link type [Reference-chain or Description-chain], Verdict [PASS or CHAIN
> INTEGRITY FAILURE]), Axis 3 (derivation direction: AMEND(d) must derive its lever anchor
> from the L3 Evidence column only; Phase 5(3) and CCV are prohibited derivation sources for
> AMEND(d)'s lever anchor). All named artifacts must be produced exactly as declared. All
> downstream cites must copy upstream labels verbatim. AMEND(d) must derive its lever anchor
> from the L3 Evidence column only. The audit must be produced after Phase 7 and must declare
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


### V-74: Both Components in Produced Label Only (C-42 FAIL test)

**Axis:** AUDIT ARCHITECTURE DECLARED block body is a minimal read-completion trigger: it
names the artifact and instructs the model to read it before Phase 1. The block body contains
NEITHER axis enumeration NOR an impossibility statement. Both gate components -- axis
enumeration (Axis 1, Axis 2, Axis 3 named by label) AND the impossibility statement ("partial
coverage is a gate failure") -- live exclusively in the produced architecture label. This is
the shape the rubric's C-42 verdict table explicitly names as FAIL for C-42 while C-41 earns
its named PARTIAL (5 pts). The divergence between C-41 and C-42 is maximized here.
**Hypothesis:** C-40 PARTIAL (5 pts) -- block body names no axes. C-41 PARTIAL (5 pts) --
named PARTIAL condition: full per-axis gate present only in produced architecture label.
C-42 FAIL (0 pts) -- both components in produced label only; explicit FAIL in C-42 table.
C-01--C-39 = 390 pts. Total predicted: 405/420.
**Change from V-71:** Block gate body stripped to read-completion trigger only. Produced label
receives the full per-axis gate: axis enumeration by label AND impossibility statement. This
is the divergence shape: C-41 earns its named PARTIAL while C-42 earns FAIL (0 pts). All
phases, CCV, and AMEND identical to V-71.

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
| 5 | After Phase 7, before CCV | CITATION CHAIN COMPLETENESS AUDIT | Self-verifying | See AUDIT ARCHITECTURE DECLARED block below; CHAIN COMPLETE gate before CCV |

---

**AUDIT ARCHITECTURE DECLARED**

This block is the required architecture declaration. Read it before Phase 1.

Do not proceed to Phase 1 until "AUDIT ARCHITECTURE DECLARED" is written on its own line above.

---

**Exact-copy rule:** A downstream cite that describes or paraphrases is a paraphrase chain.
A downstream cite that reproduces the artifact label character-for-character is a reference
chain. Only reference chains satisfy the citation requirements.

**Structural prohibition:** Do not produce output in any phase that would require a downstream
phase to paraphrase rather than copy. Return to the phase and emit the required artifact.

**Required architecture label:**

> "CITATION ARCHITECTURE DECLARED. This architecture declares all artifact production
> requirements (rows 1--4), the Citation Chain Completeness Audit requirement (row 5), and
> the AUDIT ARCHITECTURE DECLARED block with three co-resident axes. The block must contain:
> Axis 1 (duality framing: declarative vs. confirmatory structural roles -- the Citation
> Architecture preamble is declarative and precedes production; the Citation Chain Completeness
> Audit is confirmatory and follows production; these roles are structurally distinct and
> neither substitutes for the other), Axis 2 (audit format: the Audit must use a 5-column
> structure -- Source artifact, Consumer site, Evidence [write actual downstream cite text
> verbatim; the Evidence cell must be populated with real text, not a placeholder], Link type
> [Reference-chain or Description-chain], Verdict [PASS or CHAIN INTEGRITY FAILURE]), Axis 3
> (derivation direction: AMEND(d) must derive its lever anchor from the L3 Evidence column
> only; Phase 5(3) and CCV are prohibited derivation sources). A block containing Axes 1 and
> 2 but omitting Axis 3 fails its gate. A block containing any two of the three axes while
> omitting the third fails its gate. Partial axis coverage is not partial compliance -- it is
> a gate failure. All named artifacts must be produced exactly as declared. All downstream
> cites must copy upstream labels verbatim. AMEND(d) must derive its lever anchor from the L3
> Evidence column -- not from Phase 5(3) or CCV. The audit must be produced after Phase 7 and
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


### V-75: Redundant Full Gate in Both Block Body and Produced Label (C-42 PASS -- duplication is not a split)

**Axis:** AUDIT ARCHITECTURE DECLARED block body contains the full gate: axis enumeration
(all three axes named by label) AND impossibility statement. The produced architecture label
ALSO carries the full gate: it redundantly restates the axis enumeration by label AND the
impossibility statement. Both gate components are present in both locations. This tests
whether C-42 penalizes redundant restatement as a "split." The rubric's C-42 criterion
targets components that are divided -- present in one location and absent from the other.
When both components are in both locations, no split exists; the gate is duplicated, not
divided. V-75 is V-71's redundancy analog: if V-66/V-71 earn C-41 PASS and V-70 (redundant
dual-site gate) also earned C-41 PASS, then V-75 should earn C-42 PASS by the same logic.
**Hypothesis:** C-40 PASS (10 pts) -- full axis enumeration in block body. C-41 PASS (10 pts)
-- full per-axis gate in block body. C-42 PASS (10 pts) -- both components in block body;
label restatement is redundant, not a disqualifying split. C-01--C-39 = 390 pts.
Total predicted: 420/420.
**Change from V-71:** Produced architecture label expanded to redundantly restate the full
per-axis gate (axis labels by name AND impossibility statement) in addition to its standard
summary content. Block body is identical to V-71. All phases, CCV, and AMEND identical to
V-71.

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
> body names all three axes by label and declares partial axis coverage a gate failure: a block
> containing Axes 1 and 2 but omitting Axis 3 fails; a block containing any two axes while
> omitting the third fails; partial axis coverage is not partial compliance -- it is a gate
> failure. All three axes must be declared in the block body before Phase 1 begins. All named
> artifacts must be produced exactly as declared. All downstream cites must copy upstream
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
