Written to `simulations/quest/variations/validate-inertia-variations-R19-2026-03-17.md`.

---

## R19 Variations -- V-91 through V-95

| # | Label | C-45 | C-46 | C-47 | C-48 | C-49 | Predicted |
|---|-------|------|------|------|------|------|-----------|
| **V-91** | Ceiling: both S1 and S2 as distinct named disqualifiers | PASS | PASS | PASS | PASS | PASS | **490** |
| **V-92** | C-49 PARTIAL: S1 only (merged "or" shape named, S2 absent) | PASS | PASS | PASS | PASS | PARTIAL | **485** |
| **V-93** | C-49 PARTIAL: S2 only (outcome-language shape named, S1 absent) | PASS | PASS | PASS | PASS | PARTIAL | **485** |
| **V-94** | C-49 PARTIAL: merged description, no distinct labels | PASS | PASS | PASS | PASS | PARTIAL | **485** |
| **V-95** | Gap: C-45 FAIL + C-46/C-47/C-48/C-49 PASS | FAIL | PASS | PASS | PASS | PASS | **480** |

**Score derivation:** Baseline C-01--C-44 = 440. V-91: +10+10+10+10+10 = 490. V-92/V-93/V-94: +10+10+10+10+5 = 485 (three distinct C-49 PARTIAL paths). V-95: +0+10+10+10+10 = 480.

**Single locus of change:** V-91 through V-94 vary only the C-49 paragraph appended after the V-86 closure. V-95 restructures the closure to remove the positive duality declaration (C-45 FAIL) while holding C-46/C-47/C-48/C-49 all PASS.

**Key discrimination:**
- V-92 vs V-93 -- 485 via orthogonal S1-only vs S2-only absence; tests rubric recognition of which shape is present
- V-91 vs V-92/V-93/V-94 -- 10 pts isolates C-49 PASS vs PARTIAL
- V-91 vs V-95 -- 10 pts isolates C-45 PASS vs FAIL with C-49 held constant at PASS
- V-95 vs V-90 (R18) -- same C-45 FAIL structure; V-95 adds C-49 PASS, moving 470 → 480, closing the R19 gap
inct case. S2 absent. One shape enumerated,
  the other omitted.
- **C-49 PARTIAL (V-93):** Only S2 named as a distinct case. S1 absent. Mirror of V-92.
- **C-49 PARTIAL (V-94):** Both shapes described together in a single merged sentence without
  distinct labels -- "either a merged 'or' condition or outcome-language sentences earns partial
  credit." Neither shape is named as a distinct case.
- **V-95 (gap variation):** C-45 FAIL because no positive duality declaration exists ("The gate
  architecture closure has two functions serving structurally distinct roles..." is absent).
  Both closure functions are referenced only in disqualifier-context sentences (C-47 FAIL
  disqualifier names both; C-48 PARTIAL path sentences name one each). C-46, C-47, C-48, C-49
  all satisfied independently through disqualifier framing and the C-49 taxonomy paragraph.
  Tests whether disqualifier-context function naming plus full C-47/C-48/C-49 coverage scores
  the same as V-87 and V-90 analogs but at the R19 rubric ceiling.

**Key discrimination tests:**

- V-92 vs V-93 -- both predict 485, orthogonal failure modes (S1-only vs S2-only). Tests whether
  rubric correctly identifies which shape is present.
- V-91 vs V-92/V-93/V-94 -- 10 pts isolated to C-49 PASS vs PARTIAL (490 vs 485).
- V-91 vs V-95 -- C-45 PASS vs FAIL isolates 10 pts (490 vs 480) with C-49 held constant.
- V-95 vs V-90(R18) -- same C-45 FAIL + C-46 PASS structure, but V-95 adds C-49 PASS (+10
  over V-90's 470 ceiling, now 480). Confirms C-49 is independently addable to the gap shape.
- V-92/V-93/V-94 form a 485-triple via three distinct C-49 PARTIAL paths -- same score, three
  structurally distinct failure modes.

**Score derivation:**

- Baseline (C-01--C-44 all PASS): 440 pts
- V-91: +10(C-45) +10(C-46) +10(C-47) +10(C-48) +10(C-49) = **490**
- V-92: +10(C-45) +10(C-46) +10(C-47) +10(C-48) +5(C-49) = **485**
- V-93: +10(C-45) +10(C-46) +10(C-47) +10(C-48) +5(C-49) = **485**
- V-94: +10(C-45) +10(C-46) +10(C-47) +10(C-48) +5(C-49) = **485**
- V-95: +0(C-45) +10(C-46) +10(C-47) +10(C-48) +10(C-49) = **480**

---

### V-91: Ceiling -- C-45 PASS + C-46 PASS + C-47 PASS + C-48 PASS + C-49 PASS (490/490)

**Axis:** Block body (1) names both closure functions as structurally distinct roles (C-45 PASS),
(2) declares both non-propagation directions (C-46 PASS), (3) adds explicit FAIL disqualifier for
naming neither function (C-47 PASS), (4) enumerates both PARTIAL paths as separate distinct
disqualifier sentences (C-48 PASS), and (5) enumerates both C-48 PARTIAL shapes (S1: merged "or"
condition; S2: separate sentences, outcome language, no "disqualifier" framing) as distinct named
disqualifier cases (C-49 PASS).
**Hypothesis:** C-41 PASS (10) + C-42 PASS (10) + C-43 PASS (10) + C-44 PASS (10) +
C-45 PASS (10) + C-46 PASS (10) + C-47 PASS (10) + C-48 PASS (10) + C-49 PASS (10) +
C-01--C-40 = 400 pts. Ceiling: 490/490.
**Change from V-86:** C-49 paragraph appended after the C-46 non-propagation paragraph. C-49
paragraph names S1 and S2 as distinct named cases, each labeled a disqualifier, in separate
sentences. All phases, CCV, and AMEND identical to V-86.

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

The gate architecture closure has two functions serving structurally distinct roles. The produced
architecture label (the "CITATION ARCHITECTURE DECLARED" label required below) serves a
self-documenting function: it certifies that the block instruction body named all three axes by
label and declared partial axis coverage a gate failure. The block instruction body serves a
self-enforcing function: it declares the gate prohibitions before any production phase begins,
so compliance constraints are present and visible before Phase 1 is executed. These are
structurally distinct roles -- the self-documenting label function certifies that the block body
declared the constraints; the self-enforcing block body function enforces compliance by making
the prohibitions present before execution. A block body that names neither the self-documenting
label function nor the self-enforcing block body function is a disqualifier and fails this
requirement entirely -- the absence of both functions means the closure architecture is
undeclared. A block body that names the self-documenting label function without naming the
self-enforcing block body function is a separate disqualifier earning partial credit -- naming
one function omits one structural role and does not satisfy the duality requirement. A block
body that names both functions without declaring them as structurally distinct roles is a further
separate disqualifier also earning partial credit -- both functions present without structural
differentiation fails the distinctness requirement while preserving partial function coverage.
Both roles must be named and declared structurally distinct to satisfy this requirement.

These two closure functions are genuinely independent. Satisfying the produced-label
certification requirement (C-43: the produced architecture label cites the block instruction body
as the explicit source of both gate components -- axis enumeration and impossibility statement)
does not discharge the split-gate prohibition requirement (C-44: the block instruction body names
both split-gate failure modes as explicit disqualifiers in the block body). Satisfying the
split-gate prohibition requirement (C-44: block instruction body names both split-gate
disqualifiers) does not discharge the produced-label certification requirement (C-43: produced
architecture label cites the block body as the source of both gate components). Both closure
criteria must be independently satisfied. A block body that names both closure functions
(satisfying the duality requirement above) without explicitly declaring this non-propagation
relationship earns partial credit: naming the duality does not substitute for declaring the
independence between the two closure criteria.

The C-48 PARTIAL taxonomy -- enumerating both C-45 PARTIAL paths as separate disqualifiers --
has two structurally distinct shapes. Shape S1 is a merged "or" condition: both PARTIAL paths
combined into a single sentence using "or" -- for example, "A block body that names one function
without the other or names both without structural distinctness earns partial credit." Shape S1
is a disqualifier: merging both PARTIAL paths into one sentence fails the enumeration requirement
and earns partial credit rather than full passage. Shape S2 is a separate-sentence form using
outcome language without explicit "disqualifier" framing: the two PARTIAL paths appear in
separate sentences, each using language such as "earns partial credit," without labeling either
sentence a disqualifier -- for example, "A block body that names one function without the other
earns partial credit. A block body that names both functions without structural distinctness also
earns partial credit." Shape S2 is a disqualifier: outcome language without disqualifier framing
fails the enumeration requirement even when paths appear in separate sentences. Both shapes are
distinct partial-credit disqualifiers. Both shapes must be named as distinct cases to satisfy
this enumeration requirement. A merged description of S1 and S2 that does not name each shape
as a distinct case is itself a partial-credit form and does not satisfy this requirement.

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


### V-92: C-49 PARTIAL -- S1 Only (485/490)

**Axis:** Block body names both closure functions as structurally distinct roles (C-45 PASS),
declares both non-propagation directions (C-46 PASS), adds explicit FAIL disqualifier for
naming neither function (C-47 PASS), enumerates both PARTIAL paths as separate distinct
disqualifier sentences (C-48 PASS). C-49 paragraph names Shape S1 (merged "or" condition) as
a distinct disqualifier case but does not name Shape S2 (separate-sentence outcome-language
form). S2 absent from the taxonomy enumeration (C-49 PARTIAL).
**Hypothesis:** C-45 PASS (10) + C-46 PASS (10) + C-47 PASS (10) + C-48 PASS (10) +
C-49 PARTIAL (5) + C-01--C-44 = 440 pts. Total predicted: 485/490.
**Change from V-91:** C-49 paragraph reduced to S1 description only. S2 paragraph removed.
All other closure text, all phases, CCV, and AMEND identical to V-91.

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

The gate architecture closure has two functions serving structurally distinct roles. The produced
architecture label (the "CITATION ARCHITECTURE DECLARED" label required below) serves a
self-documenting function: it certifies that the block instruction body named all three axes by
label and declared partial axis coverage a gate failure. The block instruction body serves a
self-enforcing function: it declares the gate prohibitions before any production phase begins,
so compliance constraints are present and visible before Phase 1 is executed. These are
structurally distinct roles -- the self-documenting label function certifies that the block body
declared the constraints; the self-enforcing block body function enforces compliance by making
the prohibitions present before execution. A block body that names neither the self-documenting
label function nor the self-enforcing block body function is a disqualifier and fails this
requirement entirely -- the absence of both functions means the closure architecture is
undeclared. A block body that names the self-documenting label function without naming the
self-enforcing block body function is a separate disqualifier earning partial credit -- naming
one function omits one structural role and does not satisfy the duality requirement. A block
body that names both functions without declaring them as structurally distinct roles is a further
separate disqualifier also earning partial credit -- both functions present without structural
differentiation fails the distinctness requirement while preserving partial function coverage.
Both roles must be named and declared structurally distinct to satisfy this requirement.

These two closure functions are genuinely independent. Satisfying the produced-label
certification requirement (C-43: the produced architecture label cites the block instruction body
as the explicit source of both gate components -- axis enumeration and impossibility statement)
does not discharge the split-gate prohibition requirement (C-44: the block instruction body names
both split-gate failure modes as explicit disqualifiers in the block body). Satisfying the
split-gate prohibition requirement (C-44: block instruction body names both split-gate
disqualifiers) does not discharge the produced-label certification requirement (C-43: produced
architecture label cites the block body as the source of both gate components). Both closure
criteria must be independently satisfied. A block body that names both closure functions
(satisfying the duality requirement above) without explicitly declaring this non-propagation
relationship earns partial credit: naming the duality does not substitute for declaring the
independence between the two closure criteria.

The C-48 PARTIAL taxonomy -- enumerating both C-45 PARTIAL paths as separate disqualifiers --
has a partial-credit form. Shape S1 is a merged "or" condition: both PARTIAL paths combined into
a single sentence using "or" -- for example, "A block body that names one function without the
other or names both without structural distinctness earns partial credit." Shape S1 is a
disqualifier: merging both PARTIAL paths into one sentence fails the enumeration requirement and
earns partial credit rather than full passage. A block body that enumerates only this shape
without also naming the S2 shape satisfies one case but not both and earns partial credit on
the taxonomy enumeration requirement.

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


### V-93: C-49 PARTIAL -- S2 Only (485/490)

**Axis:** Block body names both closure functions as structurally distinct roles (C-45 PASS),
declares both non-propagation directions (C-46 PASS), adds explicit FAIL disqualifier for
naming neither function (C-47 PASS), enumerates both PARTIAL paths as separate distinct
disqualifier sentences (C-48 PASS). C-49 paragraph names Shape S2 (separate-sentence
outcome-language form) as a distinct disqualifier case but does not name Shape S1 (merged "or"
condition). S1 absent from the taxonomy enumeration (C-49 PARTIAL).
**Hypothesis:** C-45 PASS (10) + C-46 PASS (10) + C-47 PASS (10) + C-48 PASS (10) +
C-49 PARTIAL (5) + C-01--C-44 = 440 pts. Total predicted: 485/490.
**Change from V-91:** C-49 paragraph reduced to S2 description only. S1 paragraph removed.
Mirror of V-92: same predicted score via orthogonal absence (S1-only vs S2-only). All other
closure text, all phases, CCV, and AMEND identical to V-91.

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

The gate architecture closure has two functions serving structurally distinct roles. The produced
architecture label (the "CITATION ARCHITECTURE DECLARED" label required below) serves a
self-documenting function: it certifies that the block instruction body named all three axes by
label and declared partial axis coverage a gate failure. The block instruction body serves a
self-enforcing function: it declares the gate prohibitions before any production phase begins,
so compliance constraints are present and visible before Phase 1 is executed. These are
structurally distinct roles -- the self-documenting label function certifies that the block body
declared the constraints; the self-enforcing block body function enforces compliance by making
the prohibitions present before execution. A block body that names neither the self-documenting
label function nor the self-enforcing block body function is a disqualifier and fails this
requirement entirely -- the absence of both functions means the closure architecture is
undeclared. A block body that names the self-documenting label function without naming the
self-enforcing block body function is a separate disqualifier earning partial credit -- naming
one function omits one structural role and does not satisfy the duality requirement. A block
body that names both functions without declaring them as structurally distinct roles is a further
separate disqualifier also earning partial credit -- both functions present without structural
differentiation fails the distinctness requirement while preserving partial function coverage.
Both roles must be named and declared structurally distinct to satisfy this requirement.

These two closure functions are genuinely independent. Satisfying the produced-label
certification requirement (C-43: the produced architecture label cites the block instruction body
as the explicit source of both gate components -- axis enumeration and impossibility statement)
does not discharge the split-gate prohibition requirement (C-44: the block instruction body names
both split-gate failure modes as explicit disqualifiers in the block body). Satisfying the
split-gate prohibition requirement (C-44: block instruction body names both split-gate
disqualifiers) does not discharge the produced-label certification requirement (C-43: produced
architecture label cites the block body as the source of both gate components). Both closure
criteria must be independently satisfied. A block body that names both closure functions
(satisfying the duality requirement above) without explicitly declaring this non-propagation
relationship earns partial credit: naming the duality does not substitute for declaring the
independence between the two closure criteria.

The C-48 PARTIAL taxonomy -- enumerating both C-45 PARTIAL paths as separate disqualifiers --
has a partial-credit form. Shape S2 is a separate-sentence form using outcome language without
explicit "disqualifier" framing: the two PARTIAL paths appear in separate sentences, each using
language such as "earns partial credit," without labeling either sentence a disqualifier -- for
example, "A block body that names one function without the other earns partial credit. A block
body that names both functions without structural distinctness also earns partial credit." Shape
S2 is a disqualifier: outcome language without disqualifier framing fails the enumeration
requirement even when paths appear in separate sentences, earning partial credit. A block body
that enumerates only this shape without also naming the S1 shape satisfies one case but not both
and earns partial credit on the taxonomy enumeration requirement.

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


### V-94: C-49 PARTIAL -- Merged Description of Both Shapes (485/490)

**Axis:** Block body names both closure functions as structurally distinct roles (C-45 PASS),
declares both non-propagation directions (C-46 PASS), adds explicit FAIL disqualifier for
naming neither function (C-47 PASS), enumerates both PARTIAL paths as separate distinct
disqualifier sentences (C-48 PASS). C-49 paragraph describes both shapes together in a single
merged sentence without naming each as a distinct case. Neither S1 nor S2 is labeled as a
separately named disqualifier; both shapes are described under a single merged clause (C-49
PARTIAL).
**Hypothesis:** C-45 PASS (10) + C-46 PASS (10) + C-47 PASS (10) + C-48 PASS (10) +
C-49 PARTIAL (5) + C-01--C-44 = 440 pts. Total predicted: 485/490.
**Change from V-91:** C-49 paragraph replaced with a single merged sentence describing both
shapes without distinct named labels. All other closure text, all phases, CCV, and AMEND
identical to V-91.

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

The gate architecture closure has two functions serving structurally distinct roles. The produced
architecture label (the "CITATION ARCHITECTURE DECLARED" label required below) serves a
self-documenting function: it certifies that the block instruction body named all three axes by
label and declared partial axis coverage a gate failure. The block instruction body serves a
self-enforcing function: it declares the gate prohibitions before any production phase begins,
so compliance constraints are present and visible before Phase 1 is executed. These are
structurally distinct roles -- the self-documenting label function certifies that the block body
declared the constraints; the self-enforcing block body function enforces compliance by making
the prohibitions present before execution. A block body that names neither the self-documenting
label function nor the self-enforcing block body function is a disqualifier and fails this
requirement entirely -- the absence of both functions means the closure architecture is
undeclared. A block body that names the self-documenting label function without naming the
self-enforcing block body function is a separate disqualifier earning partial credit -- naming
one function omits one structural role and does not satisfy the duality requirement. A block
body that names both functions without declaring them as structurally distinct roles is a further
separate disqualifier also earning partial credit -- both functions present without structural
differentiation fails the distinctness requirement while preserving partial function coverage.
Both roles must be named and declared structurally distinct to satisfy this requirement.

These two closure functions are genuinely independent. Satisfying the produced-label
certification requirement (C-43: the produced architecture label cites the block instruction body
as the explicit source of both gate components -- axis enumeration and impossibility statement)
does not discharge the split-gate prohibition requirement (C-44: the block instruction body names
both split-gate failure modes as explicit disqualifiers in the block body). Satisfying the
split-gate prohibition requirement (C-44: block instruction body names both split-gate
disqualifiers) does not discharge the produced-label certification requirement (C-43: produced
architecture label cites the block body as the source of both gate components). Both closure
criteria must be independently satisfied. A block body that names both closure functions
(satisfying the duality requirement above) without explicitly declaring this non-propagation
relationship earns partial credit: naming the duality does not substitute for declaring the
independence between the two closure criteria.

The C-48 PARTIAL taxonomy -- enumerating both C-45 PARTIAL paths as separate disqualifiers --
has partial-credit forms: a merged "or" condition combining both PARTIAL paths into one sentence,
or separate sentences using outcome language such as "earns partial credit" without explicit
"disqualifier" framing, each earns partial credit and does not satisfy the full enumeration
requirement.

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


### V-95: Gap -- C-45 FAIL + C-46/C-47/C-48/C-49 PASS (480/490)

**Axis:** Block body omits the positive duality declaration ("The gate architecture closure has
two functions serving structurally distinct roles...") -- the self-documenting label function
and self-enforcing block body function are referenced exclusively in disqualifier-context
sentences, never in a positive "this closure has two functions" statement (C-45 FAIL). C-47
PASS: explicit FAIL disqualifier for the zero-function case names both functions in negative
framing. C-48 PASS: both PARTIAL paths enumerated as separate distinct disqualifier sentences
(functions referenced in negative framing). C-46 PASS: non-propagation declared between C-43
and C-44 without naming the closure functions positively. C-49 PASS: both S1 and S2 shapes
enumerated as distinct named disqualifier cases.
**Hypothesis:** C-45 FAIL (0) + C-46 PASS (10) + C-47 PASS (10) + C-48 PASS (10) +
C-49 PASS (10) + C-01--C-44 = 440 pts. Total predicted: 480/490.
**Structural note:** Functions appear only in disqualifier-context sentences -- zero positive
duality declaration. This replicates the V-90 (R18) C-45 FAIL structure but extends it with
C-49 PASS, moving the predicted score from 470 (V-90) to 480 (+10 from C-49). Tests the gap
identified in R18 and R19: C-45 FAIL + full C-46/C-47/C-48 coverage + C-49 PASS.
**Change from V-91:** Positive duality paragraph removed. Closure restructured: C-47 FAIL
disqualifier leads, followed by C-48 PARTIAL path disqualifiers, followed by C-49 taxonomy
paragraph, followed by C-46 non-propagation paragraph (referencing criteria by number rather
than by function name to avoid accidentally satisfying C-45).

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

A block body that names neither the self-documenting label function nor the self-enforcing block
body function is a disqualifier and fails this requirement entirely -- the absence of both
functions means the closure architecture is undeclared. A block body that names the
self-documenting label function without naming the self-enforcing block body function is a
separate disqualifier earning partial credit -- naming one function omits one structural role
and does not satisfy the duality requirement. A block body that names both functions without
declaring them as structurally distinct roles is a further separate disqualifier also earning
partial credit -- both functions present without structural differentiation fails the
distinctness requirement while preserving partial function coverage.

The C-48 PARTIAL taxonomy -- enumerating both C-45 PARTIAL paths as separate disqualifiers --
has two structurally distinct shapes. Shape S1 is a merged "or" condition: both PARTIAL paths
combined into a single sentence using "or" -- for example, "A block body that names one function
without the other or names both without structural distinctness earns partial credit." Shape S1
is a disqualifier: merging both PARTIAL paths into one sentence fails the enumeration requirement
and earns partial credit rather than full passage. Shape S2 is a separate-sentence form using
outcome language without explicit "disqualifier" framing: the two PARTIAL paths appear in
separate sentences, each using language such as "earns partial credit," without labeling either
sentence a disqualifier -- for example, "A block body that names one function without the other
earns partial credit. A block body that names both functions without structural distinctness also
earns partial credit." Shape S2 is a disqualifier: outcome language without disqualifier framing
fails the enumeration requirement even when paths appear in separate sentences. Both shapes are
distinct partial-credit disqualifiers. Both shapes must be named as distinct cases to satisfy
this enumeration requirement. A merged description of S1 and S2 that does not name each shape
as a distinct case is itself a partial-credit form and does not satisfy this requirement.

These two closure requirements (C-43 and C-44) are genuinely independent. Satisfying C-43
does not discharge C-44, and satisfying C-44 does not discharge C-43. Both must be
independently satisfied. A block body that satisfies the duality requirement without explicitly
declaring this non-propagation relationship earns partial credit: duality satisfaction does not
substitute for declaring the independence between the two closure criteria.

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
