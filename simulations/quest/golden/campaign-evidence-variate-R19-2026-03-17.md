---
skill: quest-variate
skill_target: campaign-evidence
date: 2026-03-17
round: 19
rubric_version: 19
---

# Variates: campaign-evidence (Round 19)

**Skill**: campaign-evidence
**Rubric**: v19 (C-01--C-07 essential+recommended; C-08--C-47 aspirational; denominator 47)
**Date**: 2026-03-17
**Round**: 19

---

## Context: what informed this round

R18 delivered three PASS+ signals on C-43, C-44, and the IB table (pre-C-45):

| R18 signal | Where it appeared | What it demonstrated |
|-----------|-------------------|----------------------|
| V-01 PASS+ on C-43 | Intel-first ordering + SEQUENCING-ORDER invocations | Each SEQUENCING-ORDER cell named the live ordering decision ("Intel-first ordered as governed decision"), not just asserted compliance. |
| V-02 PASS+ on C-44 | Binary invocation cells | `[ Yes / No ] -- no hypothesis-first mode` grounds the check as a concrete antipattern-absence assertion. |
| V-03/V-05 partial on C-45 | Inertia Baseline table in preamble | The table existed and mapped antipatterns to rules -- but binary cell annotations and the audit table drew antipattern names ad hoc, not explicitly from the fixture. Vocabulary derivation was implicit, not structural. |

R18 gap analysis: C-45 requires the IB table to be the **canonical vocabulary source** -- cells must visibly draw from it, not merely coincide with it. C-46 requires the checksum section to **reconstruct the architectural history** (prior monolithic SEQUENCING state, decomposition event, delta propagated automatically). C-47 requires N/A declarations to **name the excluded antipattern**, not only cite the structural reason.

**R19 challenge**: Satisfy C-45, C-46, C-47 -- each independently, then in combination.

**Three single-axis variations, then two combined:**
- **Axis A (C-45)**: IB table with ID column; vocabulary contract; cells use `[IB-ID]` notation; audit table IB Row column. Web-first ordering to isolate from C-43.
- **Axis B (C-46)**: Checksum section contains architectural history prose reconstructing the decomposition event. Intel-first ordering to carry C-43. Cell annotations from R18 baseline (ad hoc names, no IB-ID notation).
- **Axis C (C-47)**: N/A declarations include excluded antipattern name alongside structural reason. Web-first ordering to isolate. No IB table as canonical source.

**R18 baseline carried forward (C-01 through C-44):**
Multi-stage campaign, evidence-first, falsifiable hypotheses, self-contained output, stage attribution,
consensus/conflict synthesis, calibrated confidence, gaps + decision verdict, named rules at preamble +
point of use, prospective immutable coverage map, inline scope annotations, universal binary invocation,
stage-index suffixes, entry/exit gates, gate record pre-templated, column-encoded sequencing, extensible
governance, named role handoffs, negative invocations, access-scope declarations, derivable checksum,
artifact provenance tags, dual-phase PRE/POST checkpoints, handoff artifact enumeration + provenance
activation, named PRE/POST table artifacts physically separated by execution content, complete apparatus
pre-instantiated in preamble with timing directives, interrogative at column-header level, SEQUENCING
scope covers evidence-stage ordering, rule-named interrogative column headers (C-41), SEQUENCING
decomposed into SEQUENCING-HYPO + SEQUENCING-ORDER peer rules (C-42), SEQUENCING-ORDER invocations
name live ordering decisions explicitly (C-43), binary invocation cells annotated with antipattern-absence
guards (C-44).

---

## V-01 -- Axis A: Vocabulary anchoring (C-45 only)

**Variation axis:** IB table as canonical vocabulary fixture. Web-first ordering (default) to isolate
from C-43. Binary cells use `[IB-ID]` notation drawn explicitly from the Inertia Baseline fixture.
Vocabulary contract declared in Form Templates header. Audit table includes `Antipattern (IB Row)`
column. No checksum extensibility narrative. N/A declarations use structural reason only (no antipattern
name in N/A cells -- that is C-47, not tested here).

**Hypothesis:** C-45 requires not just that the IB table exists but that the vocabulary derivation is
structurally visible. A cell reading `[ Yes / No ] -- [IB-ATTR] absent?` is auditably different from
`[ Yes / No ] -- no attribution collapse` even when the names coincide: the former makes the fixture
the authority; the latter embeds the name ad hoc. Adding an ID column to the IB table and a vocabulary
contract to the form templates section creates a machine-checkable link between every cell annotation
and its canonical source row. C-45 can be satisfied with Web-first ordering and without a checksum
narrative -- the vocabulary anchoring mechanism is the sole signal.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

---

#### Inertia Baseline: Canonical Antipattern Vocabulary Fixture

This table is the **single source of truth** for all antipattern names used in binary invocation
cells, rule declarations, and the audit table. No ad hoc antipattern naming is permitted anywhere
in this brief. Every binary cell annotation must reference an ID from this fixture.

| IB ID | Antipattern Name | Governing Rule | Detection Point | Consequence |
|-------|-----------------|----------------|-----------------|-------------|
| IB-ATTR | Attribution collapse | ATTRIBUTION | Every stage POST | Non-compliant finding; stage ATTRIBUTION fails |
| IB-CAL | Uniform confidence | CALIBRATION | S4 POST, S5 POST | CALIBRATION fails; recalibrate before exit |
| IB-FALS | Unfalsifiable hypothesis | FALSIFICATION | S3 POST, S5 POST | Hypothesis removed from register |
| IB-SEQ-H | Hypothesis-first mode | SEQUENCING-HYPO | S3 PRE | Stage 3 blocked until S1+S2 exits confirmed |
| IB-SEQ-O | Unordered collection | SEQUENCING-ORDER | S1 PRE | SEQUENCING-ORDER fails; ordering must be named |
| IB-PROV | Unconstrained synthesis | PROVENANCE | S3/S4/S5 PRE | Provenance gate fails; source artifact required |

---

#### Rule Registry (all six rules are peers; no rule is primary)

Adding a seventh peer rule propagates automatically through coverage map, checksum, and form templates;
no static integers require manual update.

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every material claim names its source stage: `[web]` S1, `[intel]` S2, `[hypothesis]` S3, `[analysis]` S4,
`[synthesis]` S5. An unlabeled claim fails ATTRIBUTION.
Excluded antipattern: **[IB-ATTR]** (see Inertia Baseline fixture).

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary. Distribution must show at least two distinct levels. Anti-uniformity guard
active at S4 and S5. State distribution explicitly.
Excluded antipattern: **[IB-CAL]** (see Inertia Baseline fixture).

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition. Final status: Supported / Refuted / Indeterminate.
Principle: "A hypothesis without a falsification condition is a belief."
Excluded antipattern: **[IB-FALS]** (see Inertia Baseline fixture).

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Governs hypothesis placement: evidence stages (S1, S2) must complete before hypothesis declaration (S3).
Principle: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis."
Excluded antipattern: **[IB-SEQ-H]** (see Inertia Baseline fixture).

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage relative ordering. **This campaign declares: Web-first ordering (S1 = Web,
S2 = Intelligence) -- the default governed ordering.** The ordering decision must be named at S1 PRE.
Excluded antipattern: **[IB-SEQ-O]** (see Inertia Baseline fixture).

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at the handoff boundary preceding each scope-restricted stage. Every claim in S3, S4, S5
carries `[source: Stage N -- Artifact Name]`.
Excluded antipattern: **[IB-PROV]** (see Inertia Baseline fixture).

---

#### Role Roster (access scope declared; provenance activation occurs at handoff boundary)

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Web Evidence Collector | External sources only. No prior artifacts. |
| S2 | Intelligence Analyst | ARTIFACT-S1 (Web Findings Corpus) only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Intelligence Assessment) only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 (Hypothesis Register) only. |
| S5 | Synthesis Director | All four prior artifacts. |

---

#### Coverage Map (immutable -- sealed before Stage 1; cannot be modified after execution begins)

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|-----|----------|----------|
| ATTRIBUTION      | + | + | + | + | + | 5 | 0 |
| CALIBRATION      | - | - | - | + | + | 2 | 3 |
| FALSIFICATION    | - | - | + | - | + | 2 | 3 |
| SEQUENCING-HYPO  | + | + | + | - | - | 3 | 2 |
| SEQUENCING-ORDER | + | + | - | - | - | 2 | 3 |
| PROVENANCE       | - | - | + | + | + | 3 | 2 |
| **Total**        |   |   |   |   |   | **17** | **13** |

**Checksum (derivable expression):** 17 positive cells x 2 PRE/POST + 13 negative cells x 1 N/A =
**47 invocation artifacts.** Derived from map dimensions; updates automatically when rules or stages
are added.

---

#### Gate Record Template (pre-instantiated blank -- fill as stages complete)

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|:----------:|:---------:|
| S1 | Web Evidence Collector | Pass (first stage) | [ Pass / Fail ] |
| S2 | Intelligence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S3 | Hypothesis Architect | [ Pass / Fail ] | [ Pass / Fail ] |
| S4 | Evidence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S5 | Synthesis Director | [ Pass / Fail ] | [ Pass / Fail ] |

---

#### Form Templates (blank -- pre-instantiated per C-38)

**Vocabulary contract:** All antipattern names in binary cell annotations are drawn from the Inertia
Baseline fixture above using the IB ID prefix (IB-ATTR, IB-CAL, IB-FALS, IB-SEQ-H, IB-SEQ-O,
IB-PROV). No ad hoc antipattern naming is permitted in any cell. The audit table antipattern column
uses the same IB IDs. Vocabulary drift between cells and the fixture is a C-45 violation.

**FORM-PRE-S1** (fill before Stage 1 output -- declare Web-first ordering as governed decision):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; Web-first declared as governed decision |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage); FALSIFICATION -- N/A (no hypotheses declared); PROVENANCE -- N/A (not scope-restricted; activates at S2->S3 handoff).

**FORM-POST-S1** (fill after Stage 1 output is complete):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; Web-first governed ordering executed |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; S2 Intel follows Web-first governed order |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage); FALSIFICATION -- N/A (no hypotheses); PROVENANCE -- N/A (not scope-restricted).

**FORM-POST-S2** (fill after Stage 2 output is complete):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; Web-first ordering confirmed at S2 |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-FALS] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage); SEQUENCING-ORDER -- N/A (governs S1, S2 only).

**FORM-POST-S3** (fill after Stage 3 output is complete):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-FALS] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-PROV] absent? |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent; 2+ distinct confidence levels required | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A (verdicts at S3/S5); SEQUENCING-HYPO -- N/A (analysis stage); SEQUENCING-ORDER -- N/A (analysis stage).

**FORM-POST-S4** (fill after Stage 4 output is complete):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent; distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- [IB-PROV] absent? |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent? | [ Yes / No ] -- [IB-FALS] absent; all verdicts stated? | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A (synthesis stage); SEQUENCING-ORDER -- N/A (synthesis stage).

**FORM-POST-S5** (fill after Stage 5 output is complete):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent; distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- [IB-FALS] absent? | [ Yes / No ] -- [IB-PROV] absent? |

---

### Stage 1 -- Web Evidence Collector (Web-first; SEQUENCING-ORDER decision declared here)

**Entry condition:** First stage. No prior artifacts. No hypothesis stated anywhere in this document.

**Timing directive:** Fill FORM-PRE-S1 (from preamble) before writing any Stage 1 output. Record
"Web-first declared as governed decision; [IB-SEQ-O] absent" in the SEQUENCING-ORDER cell.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search external sources (web, publications, public documentation) for evidence
on **$ARGUMENTS**. Produce **ARTIFACT-S1: Web Findings Corpus** with at minimum 6 findings, each
labeled `[web]`. Include: direct quotes or data with source attribution; source strength (Strong /
Moderate / Weak); coverage across market, technical, competitive, and risk dimensions. Do not state
any hypothesis. Stage-index column value: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 complete with 6+ labeled `[web]` findings; no hypothesis stated;
SEQUENCING-ORDER governed decision named in PRE and POST cells using IB-ID notation.

> **Handoff S1 -> S2: Role passes to Stage 2 -- Intelligence Analyst.**
> Artifacts transferred: ARTIFACT-S1 (Web Findings Corpus).
> Intelligence Analyst authorized reads: ARTIFACT-S1 only.
> **SEQUENCING-ORDER:** S2 Intelligence follows Web-first governed ordering declared at S1.
> **PROVENANCE RULE status:** Not yet activated. Stage 2 not scope-restricted. Activates at S2->S3 handoff.

---

### Stage 2 -- Intelligence Analyst

**Entry condition:** S1 exit gate Pass. Handoff S1->S2 complete. Web-first ordering in effect. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 (from preamble) before writing any Stage 2 output.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search internal sources (codebase, specs, documentation, prior analyses) for
evidence on **$ARGUMENTS**. Produce **ARTIFACT-S2: Intelligence Assessment** with at minimum 3
findings, each labeled `[intel]`. Include: file-path citations for codebase evidence; relevance
assessment (High / Medium / Low); notable patterns across sources. Do not state any hypothesis.
Stage-index column value: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 complete with 3+ labeled `[intel]` findings; no hypothesis stated.

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: ARTIFACT-S2 (Intelligence Assessment). Prior: ARTIFACT-S1.
> Hypothesis Architect authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE status at this boundary: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2.
> Every claim in Stage 3 must carry `[source: Stage N -- Artifact Name]`.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. Handoff S2->S3 complete. PROVENANCE RULE active. Access: ARTIFACT-S1 + ARTIFACT-S2 only.

**Timing directive:** Fill FORM-PRE-S3 (from preamble) before writing any Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare hypotheses grounded exclusively in ARTIFACT-S1 and ARTIFACT-S2.
Produce **ARTIFACT-S3: Hypothesis Register** with 3-5 hypotheses, each labeled `[hypothesis]`. For
each: (1) claim statement; (2) explicit falsification condition ([IB-FALS] guard); (3) initial
confidence (High / Medium / Low); (4) supporting evidence citations with `[source: Stage N -- Artifact Name]`
tags. Rationale for post-evidence declaration: "A hypothesis anchored before evidence gathering is a
bias, not a hypothesis." Stage-index column value: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** ARTIFACT-S3 with 3-5 falsifiable hypotheses; all claims carrying provenance tags.

> **Handoff S3 -> S4: Role passes to Stage 4 -- Evidence Analyst.**
> Artifacts transferred: ARTIFACT-S3 (Hypothesis Register). Prior: ARTIFACT-S1, ARTIFACT-S2.
> Evidence Analyst authorized reads: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.
> **PROVENANCE RULE status: REMAINS ACTIVE** for all three artifacts.

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + S2 + S3 only.

**Timing directive:** Fill FORM-PRE-S4 (from preamble) before writing any Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Analyze evidence against hypotheses. Produce **ARTIFACT-S4: Evidence Analysis**
labeled `[analysis]`. Include: patterns from S1+S2 with correlation vs. causation distinctions;
confidence distribution showing at least two distinct levels ([IB-CAL] guard); support/refutation
signals per hypothesis in ARTIFACT-S3. All claims carry `[source: Stage N -- Artifact Name]`.
Stage-index column value: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** ARTIFACT-S4 with non-uniform confidence distribution; all provenance-tagged.

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.**
> Artifacts transferred: ARTIFACT-S4 (Evidence Analysis). Prior: ARTIFACT-S1, S2, S3.
> Synthesis Director authorized reads: all four prior artifacts.
> **PROVENANCE RULE status: REMAINS ACTIVE** for all four artifacts.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. All four artifacts present. PROVENANCE RULE active.

**Timing directive:** Fill FORM-PRE-S5 (from preamble) before writing any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Synthesize all evidence. Produce **ARTIFACT-S5: Evidence Brief** labeled
`[synthesis]` with:
1. **Campaign summary** -- topic investigated; 5 stages ran in Web-first order (SEQUENCING-ORDER governed).
2. **Consensus findings** -- where ARTIFACT-S1 and ARTIFACT-S2 agree; cite both with stage attribution.
3. **Conflict findings** -- where S1 and S2 diverge; name the divergence and its significance.
4. **Hypothesis verdicts** -- Supported / Refuted / Indeterminate + confidence + falsification status per hypothesis.
5. **Confidence distribution** -- N High, N Medium, N Low. Anti-uniformity check ([IB-CAL]): if all same level, recalibrate.
6. **Gaps and open questions** -- what remains unknown after the full campaign.
7. **Decision readiness** -- one sentence: "Ready to proceed" OR "Needs more investigation on [specific gap] before committing."

All claims carry `[source: Stage N -- Artifact Name]`. Stage-index column value: **S5**.

[Fill FORM-POST-S5 here]

**Exit condition:** ARTIFACT-S5 complete with consensus/conflict synthesis, calibrated confidence, one-sentence decision verdict.

---

### Final Output

Three sections:

**Section 1 -- Evidence Brief** (ARTIFACT-S5 in full; self-contained for a reader unfamiliar with the run)

**Section 2 -- Gate Record** (filled from preamble gate template; all 5 stages, entry and exit)

**Section 3 -- Consolidated Invocation Audit Table**

| Rule | Stage | Phase | Form ID | Antipattern (IB Row) | Result |
|------|-------|-------|---------|----------------------|--------|
| ATTRIBUTION | S1 | PRE | FORM-PRE-S1 | IB-ATTR | |
| ATTRIBUTION | S1 | POST | FORM-POST-S1 | IB-ATTR | |
| SEQUENCING-HYPO | S1 | PRE | FORM-PRE-S1 | IB-SEQ-H | |
| SEQUENCING-HYPO | S1 | POST | FORM-POST-S1 | IB-SEQ-H | |
| SEQUENCING-ORDER | S1 | PRE | FORM-PRE-S1 | IB-SEQ-O | |
| SEQUENCING-ORDER | S1 | POST | FORM-POST-S1 | IB-SEQ-O | |
| CALIBRATION | S1 | N/A | -- | IB-CAL | N/A |
| FALSIFICATION | S1 | N/A | -- | IB-FALS | N/A |
| PROVENANCE | S1 | N/A | -- | IB-PROV | N/A |
| *(continue for S2 through S5 -- 47 rows total; IB Row column populated from Inertia Baseline fixture)* | | | | | |

Row count must equal **47** (derived: 17 positive x 2 + 13 negative x 1). IB Row values drawn from
Inertia Baseline fixture IDs; no ad hoc names. Any mismatch in row count = missing invocation artifact.

---
---

## V-02 -- Axis B: Checksum extensibility narrative (C-46 only)

**Variation axis:** Checksum section contains architectural history prose reconstructing the
decomposition event: prior monolithic SEQUENCING rule state, decomposition decision, delta propagated
automatically, no static integers updated. Intel-first ordering (C-43 in effect). Binary cells carry
antipattern-absence annotations (C-44, R18 baseline) but use ad hoc names -- not IB-ID notation (C-45
not tested here). No Inertia Baseline table as canonical vocabulary source. N/A declarations use
structural reason only.

**Hypothesis:** C-46 is independent of C-45. The checksum narrative reconstructs the design
rationale -- "prior monolithic SEQUENCING rule generated 40 total artifacts; decomposition into
SEQUENCING-HYPO + SEQUENCING-ORDER added 7 artifacts automatically, reaching 47 without manual
updates" -- and this reconstruction is sufficient to pass C-46 without requiring an IB table or
IB-ID vocabulary anchoring. The narrative demonstrates extensibility as a lived design event, not
as an assertion. A first-time reader can follow the arithmetic and reconstruct the decision from
the checksum section alone.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

**Stage ordering note:** This campaign runs Intelligence (S1) before Web (S2). This is a
SEQUENCING-ORDER-governed decision declared at Stage 1. Both evidence stages complete before
hypothesis declaration (S3) as governed by SEQUENCING-HYPO.

---

#### Rule Registry (all six rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every material claim names its source stage: `[intel]` S1, `[web]` S2, `[hypothesis]` S3, `[analysis]` S4,
`[synthesis]` S5. An unlabeled claim fails ATTRIBUTION.
Excluded antipattern: **attribution collapse** (claim cites "the evidence" without naming stage).

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary. At least two distinct levels required. Anti-uniformity guard at S4, S5.
Excluded antipattern: **uniform confidence** (all findings rated identically; no calibration).

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition. Status: Supported / Refuted / Indeterminate.
Excluded antipattern: **unfalsifiable hypothesis** ("a hypothesis without a falsification condition is a belief").

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence stages (S1, S2) complete before hypothesis declaration (S3).
Excluded antipattern: **hypothesis-first mode** (hypotheses stated before or during evidence collection).

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage relative ordering. **This campaign declares: Intel-first ordering (S1 =
Intelligence, S2 = Web) -- a non-default ordering that is a named, governed decision.** The ordering
decision must be named explicitly at S1 PRE and confirmed at S2 PRE.
Excluded antipattern: **unordered collection** (evidence stages run without declared ordering rationale).

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at handoff boundary preceding scope-restricted stage. Claims in S3, S4, S5 carry
`[source: Stage N -- Artifact Name]`.
Excluded antipattern: **unconstrained synthesis** (synthesis draws on information not in any named artifact).

---

#### Role Roster

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Intelligence Analyst | Internal sources only. No prior artifacts. |
| S2 | Web Evidence Collector | ARTIFACT-S1 (Intelligence Assessment) only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Web Findings Corpus) only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only. |
| S5 | Synthesis Director | All four prior artifacts. |

---

#### Coverage Map (immutable -- sealed before Stage 1)

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|-----|----------|----------|
| ATTRIBUTION      | + | + | + | + | + | 5 | 0 |
| CALIBRATION      | - | - | - | + | + | 2 | 3 |
| FALSIFICATION    | - | - | + | - | + | 2 | 3 |
| SEQUENCING-HYPO  | + | + | + | - | - | 3 | 2 |
| SEQUENCING-ORDER | + | + | - | - | - | 2 | 3 |
| PROVENANCE       | - | - | + | + | + | 3 | 2 |
| **Total**        |   |   |   |   |   | **17** | **13** |

**Checksum (derivable expression + architectural history):**

Current total: 17 positive cells x 2 PRE/POST + 13 negative cells x 1 N/A = **47 invocation artifacts.**

*Architectural history:* Prior to rule decomposition, SEQUENCING was a single monolithic rule
governing both hypothesis placement and evidence-stage relative ordering. Its coverage map row:
S1(+), S2(+), S3(+), S4(-), S5(-) -- three positive cells and two negative cells. With five peer
rules at that time (ATTRIBUTION, CALIBRATION, FALSIFICATION, SEQUENCING, PROVENANCE), the per-rule
artifact counts were: ATTRIBUTION 10, CALIBRATION 7, FALSIFICATION 7, SEQUENCING 8, PROVENANCE 8 --
**total 40 invocation artifacts.**

The decomposition event: SEQUENCING was split into two independent peer rules,
SEQUENCING-HYPO (hypothesis placement) and SEQUENCING-ORDER (evidence-stage relative ordering).
SEQUENCING-HYPO inherits the original coverage: S1(+), S2(+), S3(+), S4(-), S5(-) -- 6 PRE/POST
pairs + 2 N/A = **8 artifacts.** SEQUENCING-ORDER covers the evidence boundary only: S1(+), S2(+),
S3(-), S4(-), S5(-) -- 4 PRE/POST pairs + 3 N/A = **7 artifacts.** Combined: 15 artifacts replacing
the original 8 -- **delta of +7 artifacts propagated automatically.**

Total after decomposition: 40 - 8 + 15 = **47.** No static integer required manual update. The
coverage map gained a new row; the checksum recomputed from map dimensions; the form templates
gained a new PRE/POST pair at S1 and S2 and a new N/A declaration at S3, S4, S5. This is C-29
demonstrated by example, not by assertion: a first-time reader can reconstruct the design decision
from this section and verify that extensibility was structural, not incidental.

---

#### Gate Record Template (pre-instantiated blank -- fill as stages complete)

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|:----------:|:---------:|
| S1 | Intelligence Analyst | Pass (first stage) | [ Pass / Fail ] |
| S2 | Web Evidence Collector | [ Pass / Fail ] | [ Pass / Fail ] |
| S3 | Hypothesis Architect | [ Pass / Fail ] | [ Pass / Fail ] |
| S4 | Evidence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S5 | Synthesis Director | [ Pass / Fail ] | [ Pass / Fail ] |

---

#### Form Templates (blank -- pre-instantiated; antipattern annotations in every binary cell)

**FORM-PRE-S1** (fill before Stage 1 output -- name Intel-first ordering decision):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- no attribution collapse | [ Yes / No ] -- no hypothesis-first mode | [ Yes / No ] -- Intel-first ordered as governed decision; no unordered collection |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage); FALSIFICATION -- N/A (no hypotheses); PROVENANCE -- N/A (not scope-restricted).

**FORM-POST-S1** (fill after Stage 1 output is complete):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- attribution-collapse absent? | [ Yes / No ] -- hypothesis-first mode absent? | [ Yes / No ] -- Intel-first governed decision executed; unordered-collection absent? |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- no attribution collapse | [ Yes / No ] -- no hypothesis-first mode | [ Yes / No ] -- S2 Web follows Intel-first governed order; no unordered collection |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage); FALSIFICATION -- N/A; PROVENANCE -- N/A.

**FORM-POST-S2** (fill after Stage 2 output is complete):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- attribution-collapse absent? | [ Yes / No ] -- hypothesis-first mode absent? | [ Yes / No ] -- Intel-first ordering confirmed; unordered-collection absent? |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- no attribution collapse | [ Yes / No ] -- no unfalsifiable hypotheses | [ Yes / No ] -- no hypothesis-first mode; hypotheses only after S1+S2? | [ Yes / No ] -- no unconstrained synthesis |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage); SEQUENCING-ORDER -- N/A (S1/S2 only).

**FORM-POST-S3** (fill after Stage 3 output is complete):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- attribution-collapse absent? | [ Yes / No ] -- unfalsifiable-hypothesis absent? | [ Yes / No ] -- hypothesis-first mode absent? | [ Yes / No ] -- unconstrained-synthesis absent? |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- no attribution collapse | [ Yes / No ] -- no uniform confidence; 2+ distinct levels required | [ Yes / No ] -- no unconstrained synthesis |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A; SEQUENCING-HYPO -- N/A; SEQUENCING-ORDER -- N/A.

**FORM-POST-S4** (fill after Stage 4 output is complete):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- attribution-collapse absent? | [ Yes / No ] -- uniform-confidence absent? distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- unconstrained-synthesis absent? |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- no attribution collapse | [ Yes / No ] -- no uniform confidence | [ Yes / No ] -- no unfalsifiable hypotheses; all verdicts stated | [ Yes / No ] -- no unconstrained synthesis |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A (synthesis stage); SEQUENCING-ORDER -- N/A (synthesis stage).

**FORM-POST-S5** (fill after Stage 5 output is complete):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- attribution-collapse absent? | [ Yes / No ] -- uniform-confidence absent? distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- unfalsifiable-hypothesis absent? | [ Yes / No ] -- unconstrained-synthesis absent? |

---

### Stage 1 -- Intelligence Analyst (Intel-first; SEQUENCING-ORDER decision declared here)

**Entry condition:** First stage. No prior artifacts. No hypothesis stated anywhere in this document.

**Timing directive:** Fill FORM-PRE-S1 (from preamble) before writing any Stage 1 output. Record
"Intel-first ordered as governed decision; no unordered collection" in the SEQUENCING-ORDER cell.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search internal sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S1:
Intelligence Assessment** with at minimum 3 findings, each labeled `[intel]`. Include: file-path
citations; relevance assessment (High / Medium / Low); notable patterns. No hypothesis stated.
Stage-index column value: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 complete with 3+ labeled `[intel]` findings; no hypothesis stated;
SEQUENCING-ORDER decision named in PRE and POST cells.

> **Handoff S1 -> S2: Role passes to Stage 2 -- Web Evidence Collector.**
> Artifacts transferred: ARTIFACT-S1 (Intelligence Assessment).
> Web Evidence Collector authorized reads: ARTIFACT-S1 only.
> **SEQUENCING-ORDER:** S2 Web follows Intel-first governed ordering declared at S1.
> **PROVENANCE RULE status:** Not yet activated. Activates at S2->S3 handoff.

---

### Stage 2 -- Web Evidence Collector

**Entry condition:** S1 exit gate Pass. Intel-first ordering in effect. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 (from preamble) before writing any Stage 2 output.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search external sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S2:
Web Findings Corpus** with at minimum 6 findings, each labeled `[web]`. Include: direct quotes with
source attribution; source strength (Strong / Moderate / Weak); coverage across market, technical,
competitive, and risk dimensions. No hypothesis stated. Stage-index column value: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 with 6+ labeled `[web]` findings; no hypothesis stated.

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: ARTIFACT-S2 (Web Findings Corpus). Prior: ARTIFACT-S1.
> Hypothesis Architect authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE status at this boundary: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2.
> Every claim in Stage 3 must carry `[source: Stage N -- Artifact Name]`.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + ARTIFACT-S2 only.

**Timing directive:** Fill FORM-PRE-S3 (from preamble) before writing any Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare hypotheses grounded in ARTIFACT-S1 and ARTIFACT-S2. Produce
**ARTIFACT-S3: Hypothesis Register** with 3-5 hypotheses labeled `[hypothesis]`. For each:
(1) claim; (2) explicit falsification condition; (3) initial confidence (High / Medium / Low);
(4) evidence citations with `[source: Stage N -- Artifact Name]`. Rationale: "A hypothesis anchored
before evidence gathering is a bias, not a hypothesis." Stage-index: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** ARTIFACT-S3 with 3-5 falsifiable hypotheses; all claims provenance-tagged.

> **Handoff S3 -> S4: Role passes to Stage 4 -- Evidence Analyst.**
> Artifacts transferred: ARTIFACT-S3. Prior: ARTIFACT-S1, ARTIFACT-S2.
> Evidence Analyst authorized reads: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.
> **PROVENANCE RULE status: REMAINS ACTIVE** for all three artifacts.

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + S2 + S3 only.

**Timing directive:** Fill FORM-PRE-S4 (from preamble) before writing any Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Analyze evidence. Produce **ARTIFACT-S4: Evidence Analysis** labeled
`[analysis]`. Include: patterns from S1+S2; correlation vs causation distinctions; confidence
distribution (2+ distinct levels required; uniform-confidence antipattern guard active); support/
refutation signals per hypothesis. All claims carry `[source: Stage N -- Artifact Name]`.
Stage-index: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** ARTIFACT-S4 with non-uniform confidence distribution; all provenance-tagged.

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.**
> Synthesis Director authorized reads: all four prior artifacts. PROVENANCE RULE: REMAINS ACTIVE.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. All four artifacts present.

**Timing directive:** Fill FORM-PRE-S5 (from preamble) before writing any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]` with:
1. **Campaign summary** -- topic; 5 stages in Intel-first order (SEQUENCING-ORDER governed).
2. **Consensus findings** -- where S1 and S2 agree; cite both.
3. **Conflict findings** -- where S1 and S2 diverge; name and assess significance.
4. **Hypothesis verdicts** -- Supported / Refuted / Indeterminate per hypothesis.
5. **Confidence distribution** -- N High, N Medium, N Low. Uniform-confidence antipattern check.
6. **Gaps and open questions.**
7. **Decision readiness** -- one sentence verdict.

All claims carry `[source: Stage N -- Artifact Name]`. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

---

### Final Output

**Section 1 -- Evidence Brief** (ARTIFACT-S5 in full)

**Section 2 -- Gate Record** (from preamble template; all 5 stages)

**Section 3 -- Consolidated Invocation Audit Table** (47 rows; antipattern column uses ad hoc names
matching rule declaration text; row count derived from coverage map dimensions)

---
---

## V-03 -- Axis C: N/A antipattern grounding (C-47 only)

**Variation axis:** Every N/A declaration names the specific excluded antipattern alongside the
structural reason for inapplicability. Web-first ordering (default) to isolate from C-43. No Inertia
Baseline table as canonical fixture (C-45 not tested). Binary cells carry antipattern annotations
(C-44 baseline). N/A declarations use the antipattern name drawn from the rule declaration text.

**Hypothesis:** C-47 is independent of the IB fixture: a N/A declaration reading "CALIBRATION -- N/A
(evidence stage; uniform-confidence antipattern not applicable here)" satisfies C-47 by naming the
excluded antipattern inline, without requiring a preamble vocabulary fixture. The rule declaration
text already supplies the antipattern name; the N/A cell just needs to cite it. This makes the full
invocation apparatus homogeneous -- positive cells name the antipattern being guarded, N/A cells name
the antipattern being excluded -- without requiring IB-ID anchoring.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

---

#### Rule Registry (all six rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every material claim names its source stage. An unlabeled claim fails ATTRIBUTION.
Excluded antipattern: **attribution collapse**.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary. At least two distinct levels required.
Excluded antipattern: **uniform confidence**.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition.
Excluded antipattern: **unfalsifiable hypothesis**.

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence stages complete before hypothesis declaration.
Excluded antipattern: **hypothesis-first mode**.

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage ordering. This campaign: Web-first (default governed ordering).
Excluded antipattern: **unordered collection**.

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at handoff preceding scope-restricted stage. Claims in S3, S4, S5 carry source tags.
Excluded antipattern: **unconstrained synthesis**.

---

#### Role Roster

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Web Evidence Collector | External sources only. |
| S2 | Intelligence Analyst | ARTIFACT-S1 only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only. |
| S5 | Synthesis Director | All four prior artifacts. |

---

#### Coverage Map (immutable -- sealed before Stage 1)

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|-----|----------|----------|
| ATTRIBUTION      | + | + | + | + | + | 5 | 0 |
| CALIBRATION      | - | - | - | + | + | 2 | 3 |
| FALSIFICATION    | - | - | + | - | + | 2 | 3 |
| SEQUENCING-HYPO  | + | + | + | - | - | 3 | 2 |
| SEQUENCING-ORDER | + | + | - | - | - | 2 | 3 |
| PROVENANCE       | - | - | + | + | + | 3 | 2 |
| **Total**        |   |   |   |   |   | **17** | **13** |

**Checksum (derivable expression):** 17 x 2 + 13 x 1 = **47 invocation artifacts.** Derived from
map dimensions; updates automatically when rules or stages are added.

---

#### Gate Record Template

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|:----------:|:---------:|
| S1 | Web Evidence Collector | Pass (first stage) | [ Pass / Fail ] |
| S2 | Intelligence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S3 | Hypothesis Architect | [ Pass / Fail ] | [ Pass / Fail ] |
| S4 | Evidence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S5 | Synthesis Director | [ Pass / Fail ] | [ Pass / Fail ] |

---

#### Form Templates (blank -- pre-instantiated; C-47: N/A cells name excluded antipattern)

**N/A declaration format (applied throughout):** Every N/A cell names both the structural reason and
the excluded antipattern: `[Rule] -- N/A ([structural reason]; [antipattern name] antipattern not
applicable here)`.

**FORM-PRE-S1** (fill before Stage 1 output):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- no attribution collapse | [ Yes / No ] -- no hypothesis-first mode | [ Yes / No ] -- no unordered collection; Web-first declared |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable here); FALSIFICATION -- N/A (no hypotheses declared; unfalsifiable-hypothesis antipattern not applicable here); PROVENANCE -- N/A (not scope-restricted; unconstrained-synthesis antipattern not applicable here).

**FORM-POST-S1** (fill after Stage 1 output):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- attribution-collapse absent? | [ Yes / No ] -- hypothesis-first mode absent? | [ Yes / No ] -- unordered-collection absent; Web-first confirmed |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable here); FALSIFICATION -- N/A (no hypotheses; unfalsifiable-hypothesis antipattern not applicable here); PROVENANCE -- N/A (not scope-restricted; unconstrained-synthesis antipattern not applicable here).

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- no attribution collapse | [ Yes / No ] -- no hypothesis-first mode | [ Yes / No ] -- no unordered collection; S2 follows Web-first order |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable here); FALSIFICATION -- N/A (no hypotheses; unfalsifiable-hypothesis antipattern not applicable here); PROVENANCE -- N/A (not scope-restricted; unconstrained-synthesis antipattern not applicable here).

**FORM-POST-S2** (fill after Stage 2 output):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- attribution-collapse absent? | [ Yes / No ] -- hypothesis-first mode absent? | [ Yes / No ] -- unordered-collection absent; S2 follows Web-first |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable here); FALSIFICATION -- N/A (no hypotheses; unfalsifiable-hypothesis antipattern not applicable here); PROVENANCE -- N/A (not scope-restricted; unconstrained-synthesis antipattern not applicable here).

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- no attribution collapse | [ Yes / No ] -- no unfalsifiable hypotheses | [ Yes / No ] -- no hypothesis-first mode | [ Yes / No ] -- no unconstrained synthesis |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage; uniform-confidence antipattern not applicable here); SEQUENCING-ORDER -- N/A (governs S1/S2 only; unordered-collection antipattern not applicable here).

**FORM-POST-S3** (fill after Stage 3 output):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- attribution-collapse absent? | [ Yes / No ] -- unfalsifiable-hypothesis absent? | [ Yes / No ] -- hypothesis-first mode absent? | [ Yes / No ] -- unconstrained-synthesis absent? |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage; uniform-confidence antipattern not applicable here); SEQUENCING-ORDER -- N/A (governs S1/S2 only; unordered-collection antipattern not applicable here).

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- no attribution collapse | [ Yes / No ] -- no uniform confidence; 2+ distinct levels | [ Yes / No ] -- no unconstrained synthesis |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A (verdicts at S3/S5; unfalsifiable-hypothesis antipattern not applicable here); SEQUENCING-HYPO -- N/A (analysis stage; hypothesis-first mode antipattern not applicable here); SEQUENCING-ORDER -- N/A (analysis stage; unordered-collection antipattern not applicable here).

**FORM-POST-S4** (fill after Stage 4 output):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- attribution-collapse absent? | [ Yes / No ] -- uniform-confidence absent? distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- unconstrained-synthesis absent? |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A (verdicts at S3/S5; unfalsifiable-hypothesis antipattern not applicable here); SEQUENCING-HYPO -- N/A (analysis stage; hypothesis-first mode antipattern not applicable here); SEQUENCING-ORDER -- N/A (analysis stage; unordered-collection antipattern not applicable here).

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- no attribution collapse | [ Yes / No ] -- no uniform confidence | [ Yes / No ] -- no unfalsifiable hypotheses; all verdicts stated | [ Yes / No ] -- no unconstrained synthesis |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A (synthesis stage; hypothesis-first mode antipattern not applicable here); SEQUENCING-ORDER -- N/A (synthesis stage; unordered-collection antipattern not applicable here).

**FORM-POST-S5** (fill after Stage 5 output):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- attribution-collapse absent? | [ Yes / No ] -- uniform-confidence absent? distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- unfalsifiable-hypothesis absent? | [ Yes / No ] -- unconstrained-synthesis absent? |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A (synthesis stage; hypothesis-first mode antipattern not applicable here); SEQUENCING-ORDER -- N/A (synthesis stage; unordered-collection antipattern not applicable here).

---

### Stage 1 -- Web Evidence Collector

**Entry condition:** First stage. No prior artifacts. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S1 (from preamble) before any Stage 1 output. N/A cells include excluded antipattern name.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search external sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S1:
Web Findings Corpus** with 6+ findings labeled `[web]`. Source attribution and strength ratings
required. No hypothesis stated. Stage-index: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 with 6+ labeled findings; no hypothesis; N/A cells name excluded antipatterns.

> **Handoff S1 -> S2: Role passes to Stage 2 -- Intelligence Analyst.**
> Artifacts transferred: ARTIFACT-S1. Intelligence Analyst authorized reads: ARTIFACT-S1 only.
> PROVENANCE RULE: Not yet activated. Activates at S2->S3 handoff.

---

### Stage 2 -- Intelligence Analyst

**Entry condition:** S1 exit gate Pass. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 (from preamble) before any Stage 2 output.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search internal sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S2:
Intelligence Assessment** with 3+ findings labeled `[intel]`. File-path citations required. No hypothesis stated. Stage-index: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 with 3+ labeled findings; no hypothesis.

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: ARTIFACT-S2. Prior: ARTIFACT-S1.
> Hypothesis Architect authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2. Claims in S3 require source tags.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + ARTIFACT-S2.

**Timing directive:** Fill FORM-PRE-S3 (from preamble) before any Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Produce **ARTIFACT-S3: Hypothesis Register** with 3-5 hypotheses labeled
`[hypothesis]`. Each carries: claim; falsification condition; initial confidence; source citation with
`[source: Stage N -- Artifact Name]`. Rationale: "A hypothesis anchored before evidence gathering is
a bias, not a hypothesis." Stage-index: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** 3-5 falsifiable hypotheses; all claims provenance-tagged.

> **Handoff S3 -> S4: Role passes to Stage 4 -- Evidence Analyst.**
> Prior artifacts: S1, S2, S3. Evidence Analyst reads: S1+S2+S3 only. PROVENANCE RULE: REMAINS ACTIVE.

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit gate Pass. PROVENANCE RULE active.

**Timing directive:** Fill FORM-PRE-S4 (from preamble) before any Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Produce **ARTIFACT-S4: Evidence Analysis** labeled `[analysis]`. Include
patterns, correlation/causation distinctions, confidence distribution (2+ distinct levels required),
hypothesis support/refutation signals. All claims carry source tags. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** Non-uniform confidence distribution; all claims provenance-tagged.

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.**
> All four artifacts. PROVENANCE RULE: REMAINS ACTIVE.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. All four artifacts present.

**Timing directive:** Fill FORM-PRE-S5 (from preamble) before any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]` with:
campaign summary; consensus findings; conflict findings; hypothesis verdicts; confidence distribution
with anti-uniformity check; gaps and open questions; one-sentence decision readiness verdict. All
claims carry source tags. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

---

### Final Output

**Section 1 -- Evidence Brief** | **Section 2 -- Gate Record** | **Section 3 -- Consolidated Invocation Audit Table** (47 rows; N/A rows carry excluded antipattern names)

---
---

## V-04 -- Combined A+B: Vocabulary anchoring + checksum narrative (C-45 + C-46)

**Variation axis:** Intel-first ordering (C-43). Binary cells use IB-ID notation anchored to
Inertia Baseline fixture (C-45). Vocabulary contract declared. Checksum section includes
architectural history prose reconstructing the decomposition event (C-46). N/A declarations use
structural reason only (C-47 not tested; isolated for V-05).

**Hypothesis:** C-45 and C-46 reinforce each other structurally. The IB fixture establishes the
vocabulary; the checksum narrative explains why the fixture has 6 rows rather than 5 -- the
decomposition event that split SEQUENCING into SEQUENCING-HYPO and SEQUENCING-ORDER is the same
event that created IB-SEQ-H and IB-SEQ-O as distinct entries. A brief where the IB table names both
IB-SEQ-H and IB-SEQ-O, and the checksum narrative explains how those two rows appeared automatically
when SEQUENCING was decomposed, demonstrates C-29 (extensibility), C-45 (vocabulary fixture), and
C-46 (architectural history) as a coherent unit: the fixture is not arbitrary -- it reflects the
governed decomposition documented in the checksum narrative.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

**Stage ordering note:** Intel-first (S1 = Intelligence, S2 = Web). SEQUENCING-ORDER-governed
non-default decision declared at Stage 1. Both evidence stages complete before hypothesis (S3).

---

#### Inertia Baseline: Canonical Antipattern Vocabulary Fixture

This table is the **single source of truth** for all antipattern names. Binary cell annotations and
the audit table antipattern column draw vocabulary exclusively from this fixture using the IB ID.
No ad hoc naming permitted. The fixture has six rows -- two SEQUENCING rows (IB-SEQ-H, IB-SEQ-O) --
because SEQUENCING was decomposed into two peer rules, each targeting a distinct failure mode; see
Checksum section for the decomposition history.

| IB ID | Antipattern Name | Governing Rule | Detection Point | Consequence |
|-------|-----------------|----------------|-----------------|-------------|
| IB-ATTR | Attribution collapse | ATTRIBUTION | Every stage POST | Non-compliant finding |
| IB-CAL | Uniform confidence | CALIBRATION | S4 POST, S5 POST | CALIBRATION fails; recalibrate |
| IB-FALS | Unfalsifiable hypothesis | FALSIFICATION | S3 POST, S5 POST | Hypothesis removed |
| IB-SEQ-H | Hypothesis-first mode | SEQUENCING-HYPO | S3 PRE | Stage 3 blocked |
| IB-SEQ-O | Unordered collection | SEQUENCING-ORDER | S1 PRE | SEQUENCING-ORDER fails |
| IB-PROV | Unconstrained synthesis | PROVENANCE | S3/S4/S5 PRE | Provenance gate fails |

---

#### Rule Registry (all six rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every material claim names its source stage. Excluded antipattern: **[IB-ATTR]**.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence must vary. 2+ distinct levels required. Excluded antipattern: **[IB-CAL]**.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries explicit falsification condition. Excluded antipattern: **[IB-FALS]**.

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence (S1, S2) completes before hypothesis (S3). "A hypothesis anchored before evidence gathering
is a bias, not a hypothesis." Excluded antipattern: **[IB-SEQ-H]**.

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage relative ordering. **Intel-first (S1=Intelligence, S2=Web) declared as
non-default governed decision.** Excluded antipattern: **[IB-SEQ-O]**.

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at handoff preceding scope-restricted stage. Source tags required in S3, S4, S5.
Excluded antipattern: **[IB-PROV]**.

---

#### Role Roster

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Intelligence Analyst | Internal sources only. No prior artifacts. |
| S2 | Web Evidence Collector | ARTIFACT-S1 (Intelligence Assessment) only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Web Findings Corpus) only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only. |
| S5 | Synthesis Director | All four prior artifacts. |

---

#### Coverage Map (immutable -- sealed before Stage 1)

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|-----|----------|----------|
| ATTRIBUTION      | + | + | + | + | + | 5 | 0 |
| CALIBRATION      | - | - | - | + | + | 2 | 3 |
| FALSIFICATION    | - | - | + | - | + | 2 | 3 |
| SEQUENCING-HYPO  | + | + | + | - | - | 3 | 2 |
| SEQUENCING-ORDER | + | + | - | - | - | 2 | 3 |
| PROVENANCE       | - | - | + | + | + | 3 | 2 |
| **Total**        |   |   |   |   |   | **17** | **13** |

**Checksum (derivable expression + architectural history):**

Current total: 17 positive x 2 PRE/POST + 13 negative x 1 N/A = **47 invocation artifacts.**

*Architectural history:* Prior to rule decomposition, SEQUENCING was a single monolithic rule. Its
coverage: S1(+), S2(+), S3(+), S4(-), S5(-) -- 3 positive, 2 negative. With five peer rules at
that time, per-rule artifact counts were: ATTRIBUTION 10, CALIBRATION 7, FALSIFICATION 7,
SEQUENCING 8, PROVENANCE 8 -- **total 40 artifacts.**

The decomposition decision: SEQUENCING was split into SEQUENCING-HYPO (governs hypothesis placement,
preserving the original S1/S2/S3 positive coverage) and SEQUENCING-ORDER (governs evidence-stage
relative ordering, covering only the S1/S2 boundary). This created two new IB rows -- IB-SEQ-H and
IB-SEQ-O -- in the Inertia Baseline fixture above: the fixture reflects the decomposition, not a
design decision made independently of it. SEQUENCING-HYPO: 8 artifacts (6 PRE/POST + 2 N/A).
SEQUENCING-ORDER: 7 artifacts (4 PRE/POST + 3 N/A). Combined: 15 replacing 8 -- **delta +7.**

Total: 40 - 8 + 15 = **47. No static integer required manual update.** The coverage map, checksum
expression, IB fixture, and form templates all absorbed the new rule automatically. C-29 demonstrated
as a concrete historical event: add a seventh peer rule and all four structures update by derivation.

---

#### Gate Record Template

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|:----------:|:---------:|
| S1 | Intelligence Analyst | Pass (first stage) | [ Pass / Fail ] |
| S2 | Web Evidence Collector | [ Pass / Fail ] | [ Pass / Fail ] |
| S3 | Hypothesis Architect | [ Pass / Fail ] | [ Pass / Fail ] |
| S4 | Evidence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S5 | Synthesis Director | [ Pass / Fail ] | [ Pass / Fail ] |

---

#### Form Templates (blank -- pre-instantiated; IB-ID notation throughout)

**Vocabulary contract:** All binary cell antipattern annotations use IB ID references (IB-ATTR,
IB-CAL, etc.) drawn from the Inertia Baseline fixture. No ad hoc naming. Audit table antipattern
column cites the same IB IDs.

**FORM-PRE-S1** (fill before Stage 1 -- declare Intel-first as governed decision):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; Intel-first ordered as governed decision |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage); FALSIFICATION -- N/A (no hypotheses); PROVENANCE -- N/A (not scope-restricted).

**FORM-POST-S1** (fill after Stage 1 output):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; Intel-first governed decision executed |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage); FALSIFICATION -- N/A (no hypotheses); PROVENANCE -- N/A (not scope-restricted).

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; S2 Web follows Intel-first governed order |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage); FALSIFICATION -- N/A; PROVENANCE -- N/A.

**FORM-POST-S2** (fill after Stage 2 output):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; Intel-first ordering confirmed at S2 |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage); FALSIFICATION -- N/A; PROVENANCE -- N/A.

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-FALS] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage); SEQUENCING-ORDER -- N/A (S1/S2 only).

**FORM-POST-S3** (fill after Stage 3 output):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-FALS] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage); SEQUENCING-ORDER -- N/A (S1/S2 only).

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent; 2+ distinct levels required | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A; SEQUENCING-HYPO -- N/A; SEQUENCING-ORDER -- N/A.

**FORM-POST-S4** (fill after Stage 4 output):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent; distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A; SEQUENCING-HYPO -- N/A; SEQUENCING-ORDER -- N/A.

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent? | [ Yes / No ] -- [IB-FALS] absent; all verdicts stated? | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A; SEQUENCING-ORDER -- N/A.

**FORM-POST-S5** (fill after Stage 5 output):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent; distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- [IB-FALS] absent? | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A; SEQUENCING-ORDER -- N/A.

---

### Stage 1 -- Intelligence Analyst (Intel-first; SEQUENCING-ORDER decision declared here)

**Entry condition:** First stage. No prior artifacts. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S1 before any Stage 1 output. SEQUENCING-ORDER cell: record
"Intel-first ordered as governed decision; [IB-SEQ-O] absent."

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search internal sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S1:
Intelligence Assessment** with 3+ findings labeled `[intel]`. File-path citations; relevance
assessment; notable patterns. No hypothesis stated. Stage-index: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 with 3+ findings; no hypothesis; SEQUENCING-ORDER governed decision
named using IB-SEQ-O notation.

> **Handoff S1 -> S2: Role passes to Stage 2 -- Web Evidence Collector.**
> Artifacts transferred: ARTIFACT-S1. Web Evidence Collector authorized reads: ARTIFACT-S1 only.
> SEQUENCING-ORDER: S2 Web follows Intel-first governed ordering declared at S1.
> PROVENANCE RULE: Not yet activated. Activates at S2->S3 handoff.

---

### Stage 2 -- Web Evidence Collector

**Entry condition:** S1 exit gate Pass. Intel-first ordering in effect. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 before any Stage 2 output.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search external sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S2:
Web Findings Corpus** with 6+ findings labeled `[web]`. Direct quotes; source strength; coverage
across market, technical, competitive, risk dimensions. No hypothesis stated. Stage-index: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 with 6+ labeled findings; no hypothesis.

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: ARTIFACT-S2. Prior: ARTIFACT-S1.
> Hypothesis Architect reads: ARTIFACT-S1 + ARTIFACT-S2 only.
> PROVENANCE RULE: ACTIVATED for ARTIFACT-S1 and ARTIFACT-S2. Claims in S3 require source tags.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + ARTIFACT-S2.

**Timing directive:** Fill FORM-PRE-S3 before any Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Produce **ARTIFACT-S3: Hypothesis Register** with 3-5 hypotheses labeled
`[hypothesis]`. Each carries: claim; falsification condition ([IB-FALS] guard); initial confidence;
source citations `[source: Stage N -- Artifact Name]`. Rationale: "A hypothesis anchored before
evidence gathering is a bias, not a hypothesis." Stage-index: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** 3-5 falsifiable hypotheses; all claims provenance-tagged.

> **Handoff S3 -> S4: Role passes to Stage 4 -- Evidence Analyst.**
> Prior artifacts: S1, S2, S3. Evidence Analyst reads: S1+S2+S3 only. PROVENANCE: REMAINS ACTIVE.

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit gate Pass. PROVENANCE RULE active.

**Timing directive:** Fill FORM-PRE-S4 before any Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Produce **ARTIFACT-S4: Evidence Analysis** labeled `[analysis]`. Patterns
from S1+S2; correlation/causation distinctions; confidence distribution (2+ distinct levels,
[IB-CAL] guard); hypothesis support/refutation signals. Source tags on all claims. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** Non-uniform confidence; all claims provenance-tagged.

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.** All four artifacts. PROVENANCE: REMAINS ACTIVE.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. All four artifacts present.

**Timing directive:** Fill FORM-PRE-S5 before any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]` with:
campaign summary (Intel-first, SEQUENCING-ORDER governed); consensus findings; conflict findings;
hypothesis verdicts; confidence distribution ([IB-CAL] guard); gaps; one-sentence decision readiness
verdict. Source tags on all claims. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

---

### Final Output

**Section 1 -- Evidence Brief** (ARTIFACT-S5; self-contained)

**Section 2 -- Gate Record** (from preamble template)

**Section 3 -- Consolidated Invocation Audit Table**

| Rule | Stage | Phase | Form ID | Antipattern (IB Row) | Result |
|------|-------|-------|---------|----------------------|--------|
| ATTRIBUTION | S1 | PRE | FORM-PRE-S1 | IB-ATTR | |
| *(47 rows total; IB Row column draws from Inertia Baseline fixture)* | | | | | |

Row count derived: 17 x 2 + 13 x 1 = 47. IB Row values from fixture; no ad hoc names in audit table.

---
---

## V-05 -- Combined A+B+C: Full integration (C-45 + C-46 + C-47)

**Variation axis:** All three new R19 axes combined. Intel-first ordering (C-43). IB table as
canonical vocabulary fixture with IB-ID notation in cells (C-45). Checksum section reconstructs
architectural history of the decomposition event (C-46). N/A declarations name the excluded
antipattern using IB-ID alongside the structural reason (C-47). The full apparatus is homogeneous:
positive cells carry IB-ID annotations, N/A cells carry IB-ID exclusion names, the audit table has
an IB Row column, and the checksum section explains why the IB fixture has the rows it has.

**Hypothesis:** The three axes form a mutually reinforcing structure. C-45 (IB as vocabulary source)
establishes IB-IDs as the lingua franca of the entire apparatus. C-46 (architectural history) explains
the origin of IB-SEQ-H and IB-SEQ-O as entries -- they did not appear by fiat but by the same
decomposition event that shifted the artifact total from 40 to 47. C-47 (antipattern names in N/A)
makes N/A cells as informationally dense as positive cells: both name the IB antipattern they are
about, and both draw from the same fixture. Together they achieve structural homogeneity: every cell
in the apparatus -- PRE, POST, and N/A -- is traceable to an IB row by ID, and the checksum narrative
grounds the architecture in a concrete, reconstructible design decision.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

**Stage ordering note:** Intel-first (S1 = Intelligence, S2 = Web). SEQUENCING-ORDER-governed
non-default decision. Both evidence stages complete before hypothesis (S3).

---

#### Inertia Baseline: Canonical Antipattern Vocabulary Fixture

**Single source of truth** for all antipattern names throughout this brief: binary cell annotations,
N/A exclusion declarations, rule declarations, and the audit table antipattern column all draw
vocabulary from this fixture using the IB ID. No ad hoc naming anywhere. Vocabulary drift between
a cell annotation and its IB row is a C-45 violation. The two SEQUENCING rows (IB-SEQ-H, IB-SEQ-O)
reflect the decomposition event documented in the Checksum section.

| IB ID | Antipattern Name | Governing Rule | Detection Point | Consequence |
|-------|-----------------|----------------|-----------------|-------------|
| IB-ATTR | Attribution collapse | ATTRIBUTION | Every stage POST | Non-compliant finding |
| IB-CAL | Uniform confidence | CALIBRATION | S4 POST, S5 POST | CALIBRATION fails; recalibrate |
| IB-FALS | Unfalsifiable hypothesis | FALSIFICATION | S3 POST, S5 POST | Hypothesis removed |
| IB-SEQ-H | Hypothesis-first mode | SEQUENCING-HYPO | S3 PRE | Stage 3 blocked |
| IB-SEQ-O | Unordered collection | SEQUENCING-ORDER | S1 PRE | SEQUENCING-ORDER fails |
| IB-PROV | Unconstrained synthesis | PROVENANCE | S3/S4/S5 PRE | Provenance gate fails |

---

#### Rule Registry (all six rules are peers; no rule is primary)

Adding a seventh peer rule propagates automatically through coverage map, checksum, IB fixture, and
form templates; no static integers require manual update.

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every material claim names its source stage: `[intel]` S1, `[web]` S2, `[hypothesis]` S3,
`[analysis]` S4, `[synthesis]` S5. Excluded antipattern: **[IB-ATTR]**.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary. 2+ distinct levels required. Excluded antipattern: **[IB-CAL]**.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries explicit falsification condition. "A hypothesis without a falsification
condition is a belief." Excluded antipattern: **[IB-FALS]**.

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence (S1, S2) completes before hypothesis (S3). Excluded antipattern: **[IB-SEQ-H]**.

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage relative ordering. **Intel-first (S1=Intelligence, S2=Web) declared as
non-default governed decision at S1 PRE.** Excluded antipattern: **[IB-SEQ-O]**.

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at handoff preceding scope-restricted stage. Source tags required in S3/S4/S5.
Excluded antipattern: **[IB-PROV]**.

---

#### Role Roster

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Intelligence Analyst | Internal sources only. No prior artifacts. |
| S2 | Web Evidence Collector | ARTIFACT-S1 (Intelligence Assessment) only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Web Findings Corpus) only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only. |
| S5 | Synthesis Director | All four prior artifacts. |

---

#### Coverage Map (immutable -- sealed before Stage 1)

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|-----|----------|----------|
| ATTRIBUTION      | + | + | + | + | + | 5 | 0 |
| CALIBRATION      | - | - | - | + | + | 2 | 3 |
| FALSIFICATION    | - | - | + | - | + | 2 | 3 |
| SEQUENCING-HYPO  | + | + | + | - | - | 3 | 2 |
| SEQUENCING-ORDER | + | + | - | - | - | 2 | 3 |
| PROVENANCE       | - | - | + | + | + | 3 | 2 |
| **Total**        |   |   |   |   |   | **17** | **13** |

**Checksum (derivable expression + architectural history):**

Current total: 17 positive x 2 PRE/POST + 13 negative x 1 N/A = **47 invocation artifacts.**

*Architectural history:* Prior to rule decomposition, SEQUENCING was a single monolithic rule. Its
coverage row: S1(+), S2(+), S3(+), S4(-), S5(-). With five peer rules at that time, the total was:
ATTRIBUTION 10 + CALIBRATION 7 + FALSIFICATION 7 + SEQUENCING 8 + PROVENANCE 8 = **40 artifacts.**
The Inertia Baseline fixture had five rows at that time -- no IB-SEQ-H, no IB-SEQ-O; only a single
unnamed SEQUENCING antipattern whose two failure modes were conflated.

The decomposition event: SEQUENCING was split into SEQUENCING-HYPO (hypothesis placement, IB-SEQ-H)
and SEQUENCING-ORDER (evidence-stage ordering, IB-SEQ-O). These are the two rows appearing under
the SEQUENCING rules in the Inertia Baseline above -- they did not appear by editorial choice but
by structural necessity: two independent failure modes that the monolithic rule addressed with a
single invocation trail could now each be tracked with an independent trail, making either failure
visually distinct in the audit table.

Artifact delta: SEQUENCING-HYPO carries 8 artifacts (6 PRE/POST + 2 N/A); SEQUENCING-ORDER carries
7 artifacts (4 PRE/POST + 3 N/A). Combined 15 replacing 8 -- **delta +7 artifacts.** Total: 40 - 8
+ 15 = **47. No static integer required manual update.** Coverage map gained a row; checksum
recomputed from dimensions; IB fixture gained IB-SEQ-H and IB-SEQ-O; form templates gained new
PRE/POST pairs and N/A declarations at S1, S2, S3, S4, S5. A reader adding an eighth peer rule can
verify that all four structures update automatically, as this history demonstrates.

---

#### Gate Record Template

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|:----------:|:---------:|
| S1 | Intelligence Analyst | Pass (first stage) | [ Pass / Fail ] |
| S2 | Web Evidence Collector | [ Pass / Fail ] | [ Pass / Fail ] |
| S3 | Hypothesis Architect | [ Pass / Fail ] | [ Pass / Fail ] |
| S4 | Evidence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S5 | Synthesis Director | [ Pass / Fail ] | [ Pass / Fail ] |

---

#### Form Templates (blank -- pre-instantiated; IB-ID notation; N/A cells name excluded antipattern)

**Vocabulary contract:** All binary cell annotations and all N/A exclusion declarations use IB IDs
from the Inertia Baseline fixture. Format for binary cells: `[ Yes / No ] -- [IB-ID] absent?`.
Format for N/A cells: `[Rule] -- N/A ([structural reason]; [IB-ID] antipattern not applicable here)`.
No ad hoc naming. Audit table antipattern column cites IB IDs.

**FORM-PRE-S1** (fill before Stage 1 -- declare Intel-first as governed decision):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; Intel-first ordered as governed decision |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage; [IB-CAL] uniform-confidence antipattern not applicable here); FALSIFICATION -- N/A (no hypotheses declared; [IB-FALS] unfalsifiable-hypothesis antipattern not applicable here); PROVENANCE -- N/A (not scope-restricted; [IB-PROV] unconstrained-synthesis antipattern not applicable here).

**FORM-POST-S1** (fill after Stage 1 output):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; Intel-first governed decision executed |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage; [IB-CAL] not applicable here); FALSIFICATION -- N/A (no hypotheses; [IB-FALS] not applicable here); PROVENANCE -- N/A (not scope-restricted; [IB-PROV] not applicable here).

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; S2 Web follows Intel-first governed order |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage; [IB-CAL] not applicable here); FALSIFICATION -- N/A (no hypotheses; [IB-FALS] not applicable here); PROVENANCE -- N/A (not scope-restricted; [IB-PROV] not applicable here).

**FORM-POST-S2** (fill after Stage 2 output):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-SEQ-O] absent; Intel-first ordering confirmed at S2 |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage; [IB-CAL] not applicable here); FALSIFICATION -- N/A (no hypotheses; [IB-FALS] not applicable here); PROVENANCE -- N/A (not scope-restricted; [IB-PROV] not applicable here).

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-FALS] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage; [IB-CAL] uniform-confidence antipattern not applicable here); SEQUENCING-ORDER -- N/A (governs S1/S2 only; [IB-SEQ-O] unordered-collection antipattern not applicable here).

**FORM-POST-S3** (fill after Stage 3 output):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-FALS] absent? | [ Yes / No ] -- [IB-SEQ-H] absent? | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage; [IB-CAL] not applicable here); SEQUENCING-ORDER -- N/A (governs S1/S2 only; [IB-SEQ-O] not applicable here).

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent; 2+ distinct levels required | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A (verdicts at S3/S5; [IB-FALS] not applicable here); SEQUENCING-HYPO -- N/A (analysis stage; [IB-SEQ-H] not applicable here); SEQUENCING-ORDER -- N/A (analysis stage; [IB-SEQ-O] not applicable here).

**FORM-POST-S4** (fill after Stage 4 output):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent; distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A (verdicts at S3/S5; [IB-FALS] not applicable here); SEQUENCING-HYPO -- N/A (analysis stage; [IB-SEQ-H] not applicable here); SEQUENCING-ORDER -- N/A (analysis stage; [IB-SEQ-O] not applicable here).

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent? | [ Yes / No ] -- [IB-FALS] absent; all verdicts stated? | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A (synthesis stage; [IB-SEQ-H] hypothesis-first-mode antipattern not applicable here); SEQUENCING-ORDER -- N/A (synthesis stage; [IB-SEQ-O] unordered-collection antipattern not applicable here).

**FORM-POST-S5** (fill after Stage 5 output):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] absent? | [ Yes / No ] -- [IB-CAL] absent; distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- [IB-FALS] absent? | [ Yes / No ] -- [IB-PROV] absent? |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A (synthesis stage; [IB-SEQ-H] not applicable here); SEQUENCING-ORDER -- N/A (synthesis stage; [IB-SEQ-O] not applicable here).

---

### Stage 1 -- Intelligence Analyst (Intel-first; SEQUENCING-ORDER governed decision declared here)

**Entry condition:** First stage. No prior artifacts. No hypothesis stated anywhere in this document.

**Timing directive:** Fill FORM-PRE-S1 (from preamble) before any Stage 1 output. SEQUENCING-ORDER
cell: record "Intel-first ordered as governed decision; [IB-SEQ-O] absent." N/A cells: carry IB-IDs.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search internal sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S1:
Intelligence Assessment** with 3+ findings labeled `[intel]`. File-path citations; relevance
(High/Medium/Low); notable patterns. No hypothesis stated. Stage-index: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 with 3+ findings; no hypothesis; SEQUENCING-ORDER decision named
with [IB-SEQ-O] notation; N/A cells carry IB-IDs.

> **Handoff S1 -> S2: Role passes to Stage 2 -- Web Evidence Collector.**
> Artifacts transferred: ARTIFACT-S1 (Intelligence Assessment).
> Web Evidence Collector authorized reads: ARTIFACT-S1 only.
> SEQUENCING-ORDER: S2 Web follows Intel-first governed ordering declared at S1. [IB-SEQ-O] active.
> PROVENANCE RULE: Not yet activated. Activates at S2->S3 handoff.

---

### Stage 2 -- Web Evidence Collector

**Entry condition:** S1 exit gate Pass. Intel-first ordering in effect. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 (from preamble) before any Stage 2 output.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search external sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S2:
Web Findings Corpus** with 6+ findings labeled `[web]`. Direct quotes; source strength; coverage
across market, technical, competitive, risk dimensions. No hypothesis. Stage-index: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 with 6+ findings; no hypothesis; N/A cells carry IB-IDs.

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: ARTIFACT-S2 (Web Findings Corpus). Prior: ARTIFACT-S1.
> Hypothesis Architect reads: ARTIFACT-S1 + ARTIFACT-S2 only.
> PROVENANCE RULE: ACTIVATED for ARTIFACT-S1 and ARTIFACT-S2. Claims in S3 require source tags.
> Vocabulary contract active: all S3 annotations use IB-IDs.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + ARTIFACT-S2.

**Timing directive:** Fill FORM-PRE-S3 (from preamble) before any Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare hypotheses grounded in ARTIFACT-S1 and ARTIFACT-S2. Produce
**ARTIFACT-S3: Hypothesis Register** with 3-5 hypotheses labeled `[hypothesis]`. Each carries:
(1) claim; (2) explicit falsification condition ([IB-FALS] guard: "a hypothesis without a
falsification condition is a belief"); (3) initial confidence (High/Medium/Low); (4) source
citations `[source: Stage N -- Artifact Name]`. Stage-index: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** 3-5 falsifiable hypotheses; all claims provenance-tagged; N/A cells carry IB-IDs.

> **Handoff S3 -> S4: Role passes to Stage 4 -- Evidence Analyst.**
> Artifacts: S1, S2, S3. Evidence Analyst reads: S1+S2+S3 only. PROVENANCE: REMAINS ACTIVE.

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit gate Pass. PROVENANCE RULE active.

**Timing directive:** Fill FORM-PRE-S4 (from preamble) before any Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Produce **ARTIFACT-S4: Evidence Analysis** labeled `[analysis]`. Patterns
from S1+S2; correlation/causation distinctions; confidence distribution (2+ distinct levels,
[IB-CAL] guard: recalibrate if uniform); hypothesis support/refutation signals per ARTIFACT-S3.
Source tags on all claims. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** Non-uniform confidence distribution; all claims provenance-tagged.

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.**
> All four artifacts. PROVENANCE: REMAINS ACTIVE. Vocabulary contract ([IB-IDs]) active.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. All four artifacts present.

**Timing directive:** Fill FORM-PRE-S5 (from preamble) before any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]` with:
1. **Campaign summary** -- topic; 5 stages in Intel-first order ([IB-SEQ-O] governed decision at S1).
2. **Consensus findings** -- where ARTIFACT-S1 and ARTIFACT-S2 agree; cite both with stage attribution.
3. **Conflict findings** -- where S1 and S2 diverge; name the divergence and assess significance.
4. **Hypothesis verdicts** -- Supported / Refuted / Indeterminate + confidence + falsification status.
5. **Confidence distribution** -- N High, N Medium, N Low. [IB-CAL] guard: recalibrate if all same level.
6. **Gaps and open questions** -- what remains unknown after the full campaign.
7. **Decision readiness** -- one sentence: "Ready to proceed" OR "Needs more investigation on [gap] before committing."

Source tags on all claims. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

**Exit condition:** Evidence Brief complete; calibrated confidence; one-sentence verdict; all IB-IDs used throughout.

---

### Final Output

Three sections:

**Section 1 -- Evidence Brief** (ARTIFACT-S5 in full; self-contained for a reader unfamiliar with the run)

**Section 2 -- Gate Record** (filled from preamble gate template; all 5 stages, entry and exit)

**Section 3 -- Consolidated Invocation Audit Table**

| Rule | Stage | Phase | Form ID | Antipattern (IB Row) | Result |
|------|-------|-------|---------|----------------------|--------|
| ATTRIBUTION | S1 | PRE | FORM-PRE-S1 | IB-ATTR | |
| ATTRIBUTION | S1 | POST | FORM-POST-S1 | IB-ATTR | |
| SEQUENCING-HYPO | S1 | PRE | FORM-PRE-S1 | IB-SEQ-H | |
| SEQUENCING-HYPO | S1 | POST | FORM-POST-S1 | IB-SEQ-H | |
| SEQUENCING-ORDER | S1 | PRE | FORM-PRE-S1 | IB-SEQ-O | |
| SEQUENCING-ORDER | S1 | POST | FORM-POST-S1 | IB-SEQ-O | |
| CALIBRATION | S1 | N/A | -- | IB-CAL | N/A ([IB-CAL] not applicable: evidence stage) |
| FALSIFICATION | S1 | N/A | -- | IB-FALS | N/A ([IB-FALS] not applicable: no hypotheses) |
| PROVENANCE | S1 | N/A | -- | IB-PROV | N/A ([IB-PROV] not applicable: not scope-restricted) |
| *(continue for S2 through S5 -- 47 rows total; all IB Row values from Inertia Baseline fixture)* | | | | | |

Row count derived: 17 positive x 2 + 13 negative x 1 = **47.** IB Row column draws vocabulary
exclusively from Inertia Baseline fixture IDs. N/A Result cells include the IB-ID and exclusion
reason, making the audit table fully homogeneous: every row names an IB antipattern, whether the
invocation was positive (antipattern guarded) or negative (antipattern excluded).
