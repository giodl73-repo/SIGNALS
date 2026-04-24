---
skill: quest-variate
skill_target: campaign-evidence
date: 2026-03-17
round: 20
rubric_version: 20
---

# Variates: campaign-evidence (Round 20)

**Skill**: campaign-evidence
**Rubric**: v20 (C-01--C-07 essential+recommended; C-08--C-50 aspirational; denominator 50)
**Date**: 2026-03-17
**Round**: 20

---

## Context: what informed this round

R19 delivered 100/100 on V-05, satisfying C-45, C-46, C-47 in combination. Three excellence signals
from that scorecard are now formalized as criteria:

| R19 signal | Where it appeared | Formalized as |
|-----------|-------------------|---------------|
| Binary cells cite IB rows by typed identifier | V-01 form templates: `[IB-ATTR] absent?` notation | C-48 |
| Audit table antipattern column populated with IB-IDs | V-01/V-05 audit table: `IB-ATTR`, `IB-CAL` as cell values | C-49 |
| PRE binary, POST binary, and N/A all carry IB-IDs uniformly | V-05 three-tier integration | C-50 |

**Discrimination design for R20:**

C-48 and C-50 both concern the form-template binary tier, but differently:
- **C-48 PASS** requires typed ID as the **sole** annotation in binary cells: `[ Yes / No ] — [IB-ATTR]` with no English name alongside.
- **C-50 PASS** requires all three tiers to carry IB-IDs (English+ID format is sufficient for the binary tier); N/A cells must also cite IB-IDs; an explicit HOMOGENEITY INVARIANT declaration is required.

This means a binary cell reading `[ Yes / No ] — no attribution collapse [IB-ATTR]` satisfies C-50 (IB-ID present) but fails C-48 (name present alongside ID — not ID-only). A binary cell reading `[ Yes / No ] — [IB-ATTR]` satisfies both.

**Three single-axis variations, then two combined:**
- **Axis A (C-48)**: Binary cells shift to typed-ID-only annotation. N/A cells retain English-name-only format (no IB-IDs in N/A tier -- C-50 FAIL). Audit table retains English names (C-49 FAIL). Web-first ordering.
- **Axis B (C-49)**: Audit table column becomes FK-typed (`Antipattern (IB-ID FK)` header; IB-ID values only). Binary cells retain English+ID suffix (C-48 FAIL -- not ID-only). N/A cells retain English names. Web-first ordering.
- **Axis C (C-50)**: Binary cells use English+ID suffix (C-48 FAIL). N/A cells gain IB-IDs. Explicit HOMOGENEITY INVARIANT declaration. Audit table retains English names (C-49 FAIL). Web-first ordering.

**Isolation matrix:**

| | C-48 (binary ID-only) | C-49 (audit FK-typed) | C-50 (three-tier + declaration) |
|---|---|---|---|
| V-01 | **NEW** | -- | -- |
| V-02 | -- | **NEW** | -- |
| V-03 | -- | -- | **NEW** |
| V-04 | **NEW** | **NEW** | -- |
| V-05 | **NEW** | **NEW** | **NEW** |

**R19 baseline carried forward (C-01 through C-47):**
Multi-stage campaign, evidence-first, falsifiable hypotheses, self-contained output, stage attribution,
consensus/conflict synthesis, calibrated confidence, gaps + decision verdict, named rules at preamble +
point of use, prospective immutable coverage map, inline scope annotations, universal binary invocation,
stage-index suffixes, entry/exit gates, gate record pre-templated, column-encoded sequencing, extensible
governance, named role handoffs, negative invocations, access-scope declarations, derivable checksum,
artifact provenance tags, dual-phase PRE/POST checkpoints, handoff artifact enumeration + provenance
activation, named PRE/POST table artifacts physically separated by execution content, complete apparatus
pre-instantiated in preamble with timing directives, interrogative column headers, SEQUENCING decomposed
into SEQUENCING-HYPO + SEQUENCING-ORDER, SEQUENCING-ORDER names live ordering decisions (C-43),
antipattern-absence annotations in binary cells (C-44), IB vocabulary fixture with ID column (C-45),
checksum extensibility narrative (C-46), antipattern names in N/A declarations (C-47).

---

## V-01 -- Axis A: Typed-ID-only binary cells (C-48 only)

**Variation axis:** Binary cells use IB-ID as the sole annotation — no English antipattern name in the
cell body. Format: `[ Yes / No ] — [IB-ATTR]`. A cell annotation that cannot be parsed as `[IB-XXX]`
is a structural violation, not a vocabulary drift. Web-first ordering (default) to isolate from C-43.
N/A cells carry English antipattern names only (C-47 satisfied; no IB-IDs in N/A tier -- C-50 not
tested). Audit table antipattern column uses English names (C-49 not tested). Checksum narrative
present (C-46). IB vocabulary fixture with ID column present (C-45).

**Hypothesis:** C-48 requires that the typed identifier be the sole annotation, making the link
mechanically verifiable by identifier syntax rather than name-match. A binary cell reading `[IB-ATTR]`
is auditable against the IB fixture by ID lookup; any non-`[IB-XXX]` annotation is a structural
violation regardless of whether the English name was spelled correctly. C-48 can be satisfied with
Web-first ordering and without N/A IB-IDs or FK-typed audit table -- the binary-cell ID-only
commitment is the sole signal.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

---

#### Inertia Baseline: Canonical Antipattern Vocabulary Fixture

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
Every material claim names its source stage. An unlabeled claim fails ATTRIBUTION.
Excluded antipattern: **attribution collapse** [IB-ATTR].

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary. Distribution must show at least two distinct levels.
Excluded antipattern: **uniform confidence** [IB-CAL].

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition. Status: Supported / Refuted / Indeterminate.
Principle: "A hypothesis without a falsification condition is a belief."
Excluded antipattern: **unfalsifiable hypothesis** [IB-FALS].

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence stages (S1, S2) complete before hypothesis declaration (S3).
Principle: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis."
Excluded antipattern: **hypothesis-first mode** [IB-SEQ-H].

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage relative ordering. **This campaign declares: Web-first ordering (S1 = Web,
S2 = Intelligence).** The ordering decision must be named at S1 PRE.
Excluded antipattern: **unordered collection** [IB-SEQ-O].

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at the handoff boundary preceding each scope-restricted stage. Claims in S3, S4, S5 carry
`[source: Stage N -- Artifact Name]`.
Excluded antipattern: **unconstrained synthesis** [IB-PROV].

---

#### Role Roster

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
**47 invocation artifacts.** Architectural history: prior monolithic SEQUENCING rule (5 rules, 40 total
artifacts). Decomposition: SEQUENCING split into SEQUENCING-HYPO (3 positive + 2 negative) and
SEQUENCING-ORDER (2 positive + 3 negative), replacing the original 8 artifacts with 15. Delta: +7
propagated automatically. Total: 40 - 8 + 15 = **47. No static integer updated manually.**
Derived from map dimensions; updates automatically when rules or stages are added.

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

#### Form Templates (blank -- pre-instantiated; binary cells use typed-ID-only annotation per C-48)

**Cell format contract (C-48):** Every binary `[ Yes / No ]` cell annotation uses the IB-ID typed
identifier as the sole reference -- `[IB-XXX]`. No English antipattern name appears in the cell body.
An annotation that cannot be parsed as an `[IB-XXX]` token is a C-48 violation regardless of whether
the English name was spelled correctly. The IB fixture (above) supplies names for human lookup;
cells cite IDs for mechanical verification.

**FORM-PRE-S1** (fill before Stage 1 output -- declare Web-first ordering decision):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; Web-first declared as governed decision |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable). FALSIFICATION -- N/A (no hypotheses declared). PROVENANCE -- N/A (not scope-restricted; activates at S2->S3 handoff).

**FORM-POST-S1** (fill after Stage 1 output is complete):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; Web-first ordering executed |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; S2 Intel follows Web-first governed order |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable). FALSIFICATION -- N/A (no hypotheses declared). PROVENANCE -- N/A (not scope-restricted).

**FORM-POST-S2** (fill after Stage 2 output is complete):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; Web-first ordering confirmed at S2 |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-FALS] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-PROV] |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage; uniform-confidence antipattern not applicable). SEQUENCING-ORDER -- N/A (governs S1, S2 only).

**FORM-POST-S3** (fill after Stage 3 output is complete):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-FALS] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-PROV] |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL]; 2+ distinct confidence levels required | [ Yes / No ] — [IB-PROV] |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A (verdicts at S3/S5; unfalsifiable-hypothesis antipattern not applicable at analysis stage). SEQUENCING-HYPO -- N/A (analysis stage). SEQUENCING-ORDER -- N/A (analysis stage).

**FORM-POST-S4** (fill after Stage 4 output is complete):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] — [IB-PROV] |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL] | [ Yes / No ] — [IB-FALS]; all verdicts stated? | [ Yes / No ] — [IB-PROV] |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A (synthesis stage; hypothesis-first-mode antipattern not applicable). SEQUENCING-ORDER -- N/A (synthesis stage; unordered-collection antipattern not applicable).

**FORM-POST-S5** (fill after Stage 5 output is complete):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] — [IB-FALS] | [ Yes / No ] — [IB-PROV] |

---

### Stage 1 -- Web Evidence Collector (Web-first; SEQUENCING-ORDER decision declared here)

**Entry condition:** First stage. No prior artifacts. No hypothesis stated anywhere in this document.

**Timing directive:** Fill FORM-PRE-S1 (from preamble) before writing any Stage 1 output. Record
`[IB-SEQ-O]` resolved: Web-first declared as governed decision.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search external sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S1:
Web Findings Corpus** with at minimum 6 findings, each labeled `[web]`. Include: direct quotes or
data with source attribution; source strength (Strong / Moderate / Weak); coverage across market,
technical, competitive, and risk dimensions. No hypothesis stated. Stage-index column value: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 complete with 6+ labeled `[web]` findings; no hypothesis stated;
`[IB-SEQ-O]` governed decision named in PRE and POST cells via typed-ID notation.

> **Handoff S1 -> S2: Role passes to Stage 2 -- Intelligence Analyst.**
> Artifacts transferred: ARTIFACT-S1 (Web Findings Corpus).
> Intelligence Analyst authorized reads: ARTIFACT-S1 only.
> **SEQUENCING-ORDER:** S2 Intelligence follows Web-first governed ordering declared at S1.
> **PROVENANCE RULE status:** Not yet activated. Activates at S2->S3 handoff.

---

### Stage 2 -- Intelligence Analyst

**Entry condition:** S1 exit gate Pass. Web-first ordering in effect. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 (from preamble) before writing any Stage 2 output.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search internal sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S2:
Intelligence Assessment** with at minimum 3 findings, each labeled `[intel]`. Include: file-path
citations; relevance assessment (High / Medium / Low); notable patterns. No hypothesis stated.
Stage-index column value: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 with 3+ labeled `[intel]` findings; no hypothesis stated.

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: ARTIFACT-S2 (Intelligence Assessment). Prior: ARTIFACT-S1.
> Hypothesis Architect authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE status at this boundary: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2.
> Every claim in Stage 3 must carry `[source: Stage N -- Artifact Name]`.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + ARTIFACT-S2 only.

**Timing directive:** Fill FORM-PRE-S3 (from preamble) before writing any Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare hypotheses grounded in ARTIFACT-S1 and ARTIFACT-S2. Produce
**ARTIFACT-S3: Hypothesis Register** with 3-5 hypotheses, each labeled `[hypothesis]`. For each:
(1) claim; (2) explicit falsification condition (`[IB-FALS]` guard); (3) initial confidence
(High / Medium / Low); (4) evidence citations with `[source: Stage N -- Artifact Name]`. Rationale:
"A hypothesis anchored before evidence gathering is a bias, not a hypothesis." Stage-index: **S3**.

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
labeled `[analysis]`. Include: patterns from S1+S2 with correlation vs causation distinctions;
confidence distribution showing at least two distinct levels (`[IB-CAL]` guard); support/refutation
signals per hypothesis. All claims carry `[source: Stage N -- Artifact Name]`. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** ARTIFACT-S4 with non-uniform confidence distribution; all provenance-tagged.

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.**
> Artifacts transferred: ARTIFACT-S4 (Evidence Analysis). Prior: ARTIFACT-S1, S2, S3.
> Synthesis Director authorized reads: all four prior artifacts. PROVENANCE RULE: REMAINS ACTIVE.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. All four artifacts present. PROVENANCE RULE active.

**Timing directive:** Fill FORM-PRE-S5 (from preamble) before writing any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]` with:
1. **Campaign summary** -- topic; 5 stages in Web-first order (SEQUENCING-ORDER governed).
2. **Consensus findings** -- where ARTIFACT-S1 and ARTIFACT-S2 agree; cite both with stage attribution.
3. **Conflict findings** -- where S1 and S2 diverge; name divergence and assess significance.
4. **Hypothesis verdicts** -- Supported / Refuted / Indeterminate per hypothesis.
5. **Confidence distribution** -- N High, N Medium, N Low. `[IB-CAL]` guard: if all same level, recalibrate.
6. **Gaps and open questions.**
7. **Decision readiness** -- one sentence: "Ready to proceed" OR "Needs more investigation on [specific gap]."

All claims carry `[source: Stage N -- Artifact Name]`. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

**Exit condition:** ARTIFACT-S5 with consensus/conflict synthesis, calibrated confidence, one-sentence verdict.

---

### Final Output

**Section 1 -- Evidence Brief** (ARTIFACT-S5 in full)

**Section 2 -- Gate Record** (from preamble template; all 5 stages)

**Section 3 -- Consolidated Invocation Audit Table**

| Rule | Stage | Phase | Form ID | Antipattern | Result |
|------|-------|-------|---------|-------------|--------|
| ATTRIBUTION | S1 | PRE | FORM-PRE-S1 | attribution collapse | |
| ATTRIBUTION | S1 | POST | FORM-POST-S1 | attribution collapse | |
| SEQUENCING-HYPO | S1 | PRE | FORM-PRE-S1 | hypothesis-first mode | |
| SEQUENCING-HYPO | S1 | POST | FORM-POST-S1 | hypothesis-first mode | |
| SEQUENCING-ORDER | S1 | PRE | FORM-PRE-S1 | unordered collection | |
| SEQUENCING-ORDER | S1 | POST | FORM-POST-S1 | unordered collection | |
| CALIBRATION | S1 | N/A | -- | uniform confidence | N/A |
| FALSIFICATION | S1 | N/A | -- | unfalsifiable hypothesis | N/A |
| PROVENANCE | S1 | N/A | -- | unconstrained synthesis | N/A |
| *(continue for S2 through S5 -- 47 rows total; Antipattern column uses English names from rule declarations)* | | | | | |

Row count must equal **47** (derived from coverage map). Antipattern column uses English names --
not IB-ID values (C-49 not targeted in this variation).

---
---

## V-02 -- Axis B: FK-typed audit table (C-49 only)

**Variation axis:** Audit table antipattern column becomes a foreign-key reference table: column
header renamed to `Antipattern (IB-ID FK)`, cell values are IB-IDs only (`IB-ATTR`, `IB-CAL`, etc.),
no English names in the column. Binary cells carry English+IB-ID suffix format (C-44/C-45 baseline;
C-48 NOT tested -- cells are not ID-only). N/A cells carry English antipattern names (C-47 baseline;
no IB-IDs in N/A tier -- C-50 not tested). Web-first ordering. Checksum narrative present (C-46).

**Hypothesis:** C-49 is about the audit table's antipattern column specifically. Typing that column to
IB-ID values turns the audit table into a reference table joinable against the IB fixture -- any cell
value not present as an IB-ID row is a structural violation, not a name-match dispute. C-49 can be
satisfied without making binary cells ID-only (C-48 absent) and without N/A IB-IDs (C-50 absent).
The FK-typed audit table is independently testable as a structural property of the final output section.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

---

#### Inertia Baseline: Canonical Antipattern Vocabulary Fixture

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

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every material claim names its source stage. An unlabeled claim fails ATTRIBUTION.
Excluded antipattern: **attribution collapse** [IB-ATTR].

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary. At least two distinct levels required.
Excluded antipattern: **uniform confidence** [IB-CAL].

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition. Status: Supported / Refuted / Indeterminate.
Principle: "A hypothesis without a falsification condition is a belief."
Excluded antipattern: **unfalsifiable hypothesis** [IB-FALS].

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence stages (S1, S2) complete before hypothesis declaration (S3).
Principle: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis."
Excluded antipattern: **hypothesis-first mode** [IB-SEQ-H].

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage relative ordering. **This campaign declares: Web-first ordering (S1 = Web,
S2 = Intelligence).** Ordering decision must be named at S1 PRE.
Excluded antipattern: **unordered collection** [IB-SEQ-O].

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at handoff boundary preceding scope-restricted stage. Claims in S3, S4, S5 carry provenance.
Excluded antipattern: **unconstrained synthesis** [IB-PROV].

---

#### Role Roster

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Web Evidence Collector | External sources only. No prior artifacts. |
| S2 | Intelligence Analyst | ARTIFACT-S1 (Web Findings Corpus) only. |
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

**Checksum (derivable expression):** 17 x 2 + 13 x 1 = **47 invocation artifacts.** Architectural
history: prior monolithic SEQUENCING rule (5 rules, 40 artifacts). Decomposition event: SEQUENCING
split into SEQUENCING-HYPO + SEQUENCING-ORDER, replacing 8 original artifacts with 15. Delta: +7
propagated automatically. 40 - 8 + 15 = **47. No static integer updated manually.**

---

#### Gate Record Template (pre-instantiated blank)

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|:----------:|:---------:|
| S1 | Web Evidence Collector | Pass (first stage) | [ Pass / Fail ] |
| S2 | Intelligence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S3 | Hypothesis Architect | [ Pass / Fail ] | [ Pass / Fail ] |
| S4 | Evidence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S5 | Synthesis Director | [ Pass / Fail ] | [ Pass / Fail ] |

---

#### Form Templates (blank -- pre-instantiated; binary cells use English+IB-ID suffix format)

**FORM-PRE-S1** (fill before Stage 1 output):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — no attribution collapse [IB-ATTR] | [ Yes / No ] — no hypothesis-first mode [IB-SEQ-H] | [ Yes / No ] — no unordered collection [IB-SEQ-O]; Web-first declared as governed decision |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable). FALSIFICATION -- N/A (no hypotheses declared). PROVENANCE -- N/A (not scope-restricted).

**FORM-POST-S1** (fill after Stage 1 output is complete):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — attribution-collapse absent [IB-ATTR] | [ Yes / No ] — hypothesis-first mode absent [IB-SEQ-H] | [ Yes / No ] — unordered-collection absent [IB-SEQ-O]; Web-first executed |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — no attribution collapse [IB-ATTR] | [ Yes / No ] — no hypothesis-first mode [IB-SEQ-H] | [ Yes / No ] — no unordered collection [IB-SEQ-O]; S2 Intel follows Web-first order |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable). FALSIFICATION -- N/A (no hypotheses declared). PROVENANCE -- N/A (not scope-restricted).

**FORM-POST-S2** (fill after Stage 2 output is complete):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — attribution-collapse absent [IB-ATTR] | [ Yes / No ] — hypothesis-first mode absent [IB-SEQ-H] | [ Yes / No ] — unordered-collection absent [IB-SEQ-O]; ordering confirmed |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] — no attribution collapse [IB-ATTR] | [ Yes / No ] — no unfalsifiable hypothesis [IB-FALS] | [ Yes / No ] — no hypothesis-first mode [IB-SEQ-H] | [ Yes / No ] — no unconstrained synthesis [IB-PROV] |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage; uniform-confidence antipattern not applicable). SEQUENCING-ORDER -- N/A (governs S1, S2 only).

**FORM-POST-S3** (fill after Stage 3 output is complete):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] — attribution-collapse absent [IB-ATTR] | [ Yes / No ] — unfalsifiable-hypothesis absent [IB-FALS] | [ Yes / No ] — hypothesis-first mode absent [IB-SEQ-H] | [ Yes / No ] — unconstrained-synthesis absent [IB-PROV] |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] — no attribution collapse [IB-ATTR] | [ Yes / No ] — no uniform confidence [IB-CAL]; 2+ distinct levels required | [ Yes / No ] — no unconstrained synthesis [IB-PROV] |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A (verdicts at S3/S5; unfalsifiable-hypothesis antipattern not applicable). SEQUENCING-HYPO -- N/A (analysis stage). SEQUENCING-ORDER -- N/A (analysis stage).

**FORM-POST-S4** (fill after Stage 4 output is complete):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] — attribution-collapse absent [IB-ATTR] | [ Yes / No ] — uniform-confidence absent [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] — unconstrained-synthesis absent [IB-PROV] |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] — no attribution collapse [IB-ATTR] | [ Yes / No ] — no uniform confidence [IB-CAL] | [ Yes / No ] — no unfalsifiable hypothesis [IB-FALS]; all verdicts stated | [ Yes / No ] — no unconstrained synthesis [IB-PROV] |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A (synthesis stage; hypothesis-first mode not applicable). SEQUENCING-ORDER -- N/A (synthesis stage; unordered-collection antipattern not applicable).

**FORM-POST-S5** (fill after Stage 5 output is complete):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] — attribution-collapse absent [IB-ATTR] | [ Yes / No ] — uniform-confidence absent [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] — unfalsifiable-hypothesis absent [IB-FALS] | [ Yes / No ] — unconstrained-synthesis absent [IB-PROV] |

---

### Stage 1 -- Web Evidence Collector (Web-first ordering declared here)

**Entry condition:** First stage. No prior artifacts. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S1 (from preamble) before writing any Stage 1 output.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search external sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S1:
Web Findings Corpus** with 6+ findings labeled `[web]`. Include: quotes/data with source attribution;
source strength (Strong / Moderate / Weak); market, technical, competitive, and risk coverage. No
hypothesis stated. Stage-index: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 complete; no hypothesis stated; ordering decision named.

> **Handoff S1 -> S2: Role passes to Stage 2 -- Intelligence Analyst.**
> Artifacts transferred: ARTIFACT-S1 (Web Findings Corpus). Intelligence Analyst authorized reads: ARTIFACT-S1 only.
> **PROVENANCE RULE status:** Not yet activated. Activates at S2->S3 handoff.

---

### Stage 2 -- Intelligence Analyst

**Entry condition:** S1 exit gate Pass. Web-first ordering in effect. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 (from preamble) before writing any Stage 2 output.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search internal sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S2:
Intelligence Assessment** with 3+ findings labeled `[intel]`. Stage-index: **S2**.

[Fill FORM-POST-S2 here]

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: ARTIFACT-S2. Prior: ARTIFACT-S1.
> Authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + ARTIFACT-S2 only.

**Timing directive:** Fill FORM-PRE-S3 (from preamble) before writing any Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare hypotheses. Produce **ARTIFACT-S3: Hypothesis Register** with 3-5
hypotheses labeled `[hypothesis]`. Each: claim; falsification condition; confidence; provenance tags.
Stage-index: **S3**.

[Fill FORM-POST-S3 here]

> **Handoff S3 -> S4: Role passes to Stage 4 -- Evidence Analyst.**
> Authorized reads: ARTIFACT-S1 + S2 + S3. PROVENANCE RULE: REMAINS ACTIVE.

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + S2 + S3 only.

**Timing directive:** Fill FORM-PRE-S4 (from preamble) before writing any Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Produce **ARTIFACT-S4: Evidence Analysis** labeled `[analysis]`. Correlation vs
causation; confidence distribution (2+ distinct levels); support/refutation per hypothesis. All
claims provenance-tagged. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.**
> Authorized reads: all four artifacts. PROVENANCE RULE: REMAINS ACTIVE.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. All four artifacts present.

**Timing directive:** Fill FORM-PRE-S5 (from preamble) before writing any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]` with: campaign
summary; consensus findings; conflict findings; hypothesis verdicts; confidence distribution; gaps;
one-sentence decision readiness verdict. All claims provenance-tagged. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

---

### Final Output

**Section 1 -- Evidence Brief** (ARTIFACT-S5 in full)

**Section 2 -- Gate Record** (from preamble template)

**Section 3 -- Consolidated Invocation Audit Table (FK-typed antipattern column)**

| Rule | Stage | Phase | Form ID | Antipattern (IB-ID FK) | Result |
|------|-------|-------|---------|------------------------|--------|
| ATTRIBUTION | S1 | PRE | FORM-PRE-S1 | IB-ATTR | |
| ATTRIBUTION | S1 | POST | FORM-POST-S1 | IB-ATTR | |
| SEQUENCING-HYPO | S1 | PRE | FORM-PRE-S1 | IB-SEQ-H | |
| SEQUENCING-HYPO | S1 | POST | FORM-POST-S1 | IB-SEQ-H | |
| SEQUENCING-ORDER | S1 | PRE | FORM-PRE-S1 | IB-SEQ-O | |
| SEQUENCING-ORDER | S1 | POST | FORM-POST-S1 | IB-SEQ-O | |
| CALIBRATION | S1 | N/A | -- | IB-CAL | N/A |
| FALSIFICATION | S1 | N/A | -- | IB-FALS | N/A |
| PROVENANCE | S1 | N/A | -- | IB-PROV | N/A |
| *(continue for S2 through S5 -- 47 rows total)* | | | | | |

**Column contract (C-49):** The `Antipattern (IB-ID FK)` column contains only IB-ID values drawn
from the Inertia Baseline fixture. No English antipattern names appear in this column. Any cell
value not matching an IB-ID row is a structural violation detectable by identifier lookup against
the fixture -- no name-matching interpretation required. Row count: **47** (derived from coverage map).

---
---

## V-03 -- Axis C: Three-tier homogeneity declaration (C-50 only)

**Variation axis:** Explicit HOMOGENEITY INVARIANT declared in the governance preamble: PRE binary
cells, POST binary cells, and N/A cells all cite IB-IDs uniformly. Binary cells use English+IB-ID
suffix format (same as V-02 -- C-48 NOT satisfied: name present alongside ID, not ID-only). N/A cells
gain IB-IDs alongside English names (all three tiers now carry IB-IDs). Audit table uses English names
(C-49 NOT tested). Web-first ordering. Checksum narrative present (C-46).

**Hypothesis:** C-50 requires that the three-tier uniformity be both structurally present (all tiers
carry IB-IDs) AND explicitly declared as an architectural invariant. The HOMOGENEITY INVARIANT
declaration converts the uniformity from a coincidental structural property into a named commitment:
a reader can cite it by name, and any tier that lacks IB-IDs violates a stated rule rather than a
structural convention. C-50 is satisfiable without making binary cells ID-only (C-48 absent) and
without FK-typing the audit table (C-49 absent). The declaration and the N/A tier IB-IDs are the
sole signals.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

---

#### Inertia Baseline: Canonical Antipattern Vocabulary Fixture

| IB ID | Antipattern Name | Governing Rule | Detection Point | Consequence |
|-------|-----------------|----------------|-----------------|-------------|
| IB-ATTR | Attribution collapse | ATTRIBUTION | Every stage POST | Non-compliant finding; stage ATTRIBUTION fails |
| IB-CAL | Uniform confidence | CALIBRATION | S4 POST, S5 POST | CALIBRATION fails; recalibrate before exit |
| IB-FALS | Unfalsifiable hypothesis | FALSIFICATION | S3 POST, S5 POST | Hypothesis removed from register |
| IB-SEQ-H | Hypothesis-first mode | SEQUENCING-HYPO | S3 PRE | Stage 3 blocked until S1+S2 exits confirmed |
| IB-SEQ-O | Unordered collection | SEQUENCING-ORDER | S1 PRE | SEQUENCING-ORDER fails; ordering must be named |
| IB-PROV | Unconstrained synthesis | PROVENANCE | S3/S4/S5 PRE | Provenance gate fails; source artifact required |

**HOMOGENEITY INVARIANT (C-50):** PRE binary cells, POST binary cells, and N/A cells all cite IB-IDs
uniformly. Every cell in the invocation apparatus -- whether a binary Yes/No check or a negative N/A
declaration -- must reference an IB-ID from this fixture. A cell tier that carries English antipattern
names without an IB-ID reference violates this invariant. The invariant applies to form templates,
stage-embedded invocations, and the consolidated audit table's N/A rows.

---

#### Rule Registry (all six rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every material claim names its source stage. Excluded antipattern: **attribution collapse** [IB-ATTR].

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary. At least two distinct levels required.
Excluded antipattern: **uniform confidence** [IB-CAL].

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition.
Principle: "A hypothesis without a falsification condition is a belief."
Excluded antipattern: **unfalsifiable hypothesis** [IB-FALS].

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence stages complete before hypothesis declaration.
Principle: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis."
Excluded antipattern: **hypothesis-first mode** [IB-SEQ-H].

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage relative ordering. **This campaign: Web-first (S1 = Web, S2 = Intelligence).**
Excluded antipattern: **unordered collection** [IB-SEQ-O].

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Claims in S3, S4, S5 carry `[source: Stage N -- Artifact Name]`.
Excluded antipattern: **unconstrained synthesis** [IB-PROV].

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

**Checksum:** 17 x 2 + 13 x 1 = **47.** Architectural history: prior monolithic SEQUENCING (5 rules,
40 artifacts). Decomposition: SEQUENCING -> SEQUENCING-HYPO + SEQUENCING-ORDER, +7 artifacts
automatically. 40 - 8 + 15 = **47. No static integer updated manually.**

---

#### Gate Record Template (pre-instantiated blank)

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|:----------:|:---------:|
| S1 | Web Evidence Collector | Pass (first stage) | [ Pass / Fail ] |
| S2 | Intelligence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S3 | Hypothesis Architect | [ Pass / Fail ] | [ Pass / Fail ] |
| S4 | Evidence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S5 | Synthesis Director | [ Pass / Fail ] | [ Pass / Fail ] |

---

#### Form Templates (blank -- pre-instantiated; HOMOGENEITY INVARIANT applies: all tiers carry IB-IDs)

**FORM-PRE-S1** (fill before Stage 1 output):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — no attribution collapse [IB-ATTR] | [ Yes / No ] — no hypothesis-first mode [IB-SEQ-H] | [ Yes / No ] — no unordered collection [IB-SEQ-O]; Web-first declared as governed decision |

N/A [Stage 1 of 5]: CALIBRATION -- N/A [IB-CAL] (evidence stage; uniform-confidence antipattern not applicable). FALSIFICATION -- N/A [IB-FALS] (no hypotheses declared; unfalsifiable-hypothesis antipattern not applicable). PROVENANCE -- N/A [IB-PROV] (not scope-restricted; unconstrained-synthesis antipattern not applicable here).

**FORM-POST-S1** (fill after Stage 1 output is complete):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — attribution-collapse absent [IB-ATTR] | [ Yes / No ] — hypothesis-first mode absent [IB-SEQ-H] | [ Yes / No ] — unordered-collection absent [IB-SEQ-O]; Web-first executed |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — no attribution collapse [IB-ATTR] | [ Yes / No ] — no hypothesis-first mode [IB-SEQ-H] | [ Yes / No ] — no unordered collection [IB-SEQ-O]; S2 Intel follows Web-first order |

N/A [Stage 2 of 5]: CALIBRATION -- N/A [IB-CAL] (evidence stage; uniform-confidence antipattern not applicable). FALSIFICATION -- N/A [IB-FALS] (no hypotheses; unfalsifiable-hypothesis antipattern not applicable). PROVENANCE -- N/A [IB-PROV] (not scope-restricted; unconstrained-synthesis antipattern not applicable).

**FORM-POST-S2** (fill after Stage 2 output is complete):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — attribution-collapse absent [IB-ATTR] | [ Yes / No ] — hypothesis-first mode absent [IB-SEQ-H] | [ Yes / No ] — unordered-collection absent [IB-SEQ-O]; ordering confirmed |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] — no attribution collapse [IB-ATTR] | [ Yes / No ] — no unfalsifiable hypothesis [IB-FALS] | [ Yes / No ] — no hypothesis-first mode [IB-SEQ-H] | [ Yes / No ] — no unconstrained synthesis [IB-PROV] |

N/A [Stage 3 of 5]: CALIBRATION -- N/A [IB-CAL] (hypothesis stage; uniform-confidence antipattern not applicable). SEQUENCING-ORDER -- N/A [IB-SEQ-O] (governs S1, S2 only; unordered-collection antipattern not applicable here).

**FORM-POST-S3** (fill after Stage 3 output is complete):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] — attribution-collapse absent [IB-ATTR] | [ Yes / No ] — unfalsifiable-hypothesis absent [IB-FALS] | [ Yes / No ] — hypothesis-first mode absent [IB-SEQ-H] | [ Yes / No ] — unconstrained-synthesis absent [IB-PROV] |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] — no attribution collapse [IB-ATTR] | [ Yes / No ] — no uniform confidence [IB-CAL]; 2+ distinct levels required | [ Yes / No ] — no unconstrained synthesis [IB-PROV] |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A [IB-FALS] (verdicts at S3/S5; unfalsifiable-hypothesis antipattern not applicable at analysis stage). SEQUENCING-HYPO -- N/A [IB-SEQ-H] (analysis stage; hypothesis-first mode not applicable). SEQUENCING-ORDER -- N/A [IB-SEQ-O] (analysis stage; unordered-collection antipattern not applicable).

**FORM-POST-S4** (fill after Stage 4 output is complete):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] — attribution-collapse absent [IB-ATTR] | [ Yes / No ] — uniform-confidence absent [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] — unconstrained-synthesis absent [IB-PROV] |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] — no attribution collapse [IB-ATTR] | [ Yes / No ] — no uniform confidence [IB-CAL] | [ Yes / No ] — no unfalsifiable hypothesis [IB-FALS]; all verdicts stated | [ Yes / No ] — no unconstrained synthesis [IB-PROV] |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A [IB-SEQ-H] (synthesis stage; hypothesis-first mode not applicable). SEQUENCING-ORDER -- N/A [IB-SEQ-O] (synthesis stage; unordered-collection antipattern not applicable).

**FORM-POST-S5** (fill after Stage 5 output is complete):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] — attribution-collapse absent [IB-ATTR] | [ Yes / No ] — uniform-confidence absent [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] — unfalsifiable-hypothesis absent [IB-FALS] | [ Yes / No ] — unconstrained-synthesis absent [IB-PROV] |

---

### Stage 1 -- Web Evidence Collector (Web-first declared here)

**Entry condition:** First stage. No prior artifacts. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S1 (from preamble) before writing any Stage 1 output.
HOMOGENEITY INVARIANT: confirm N/A cells carry IB-IDs.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search external sources. Produce **ARTIFACT-S1: Web Findings Corpus** with
6+ findings labeled `[web]`. No hypothesis stated. Stage-index: **S1**.

[Fill FORM-POST-S1 here]

> **Handoff S1 -> S2: Role passes to Stage 2 -- Intelligence Analyst.**
> Artifacts transferred: ARTIFACT-S1. PROVENANCE not yet activated.

---

### Stage 2 -- Intelligence Analyst

**Entry condition:** S1 exit gate Pass. Web-first in effect. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 (from preamble) before Stage 2 output.
HOMOGENEITY INVARIANT: confirm N/A cells carry IB-IDs.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search internal sources. Produce **ARTIFACT-S2: Intelligence Assessment**
with 3+ findings labeled `[intel]`. Stage-index: **S2**.

[Fill FORM-POST-S2 here]

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> PROVENANCE RULE: ACTIVATED for ARTIFACT-S1 and ARTIFACT-S2.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + S2 only.

**Timing directive:** Fill FORM-PRE-S3 before Stage 3 output.
HOMOGENEITY INVARIANT: confirm N/A cells carry IB-IDs.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare 3-5 hypotheses. Produce **ARTIFACT-S3: Hypothesis Register** labeled
`[hypothesis]`. Each: claim; falsification condition; confidence; provenance tags. Stage-index: **S3**.

[Fill FORM-POST-S3 here]

> **Handoff S3 -> S4: Role passes to Stage 4 -- Evidence Analyst.**

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + S2 + S3 only.

**Timing directive:** Fill FORM-PRE-S4 before Stage 4 output.
HOMOGENEITY INVARIANT: confirm N/A cells carry IB-IDs.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Produce **ARTIFACT-S4: Evidence Analysis** labeled `[analysis]`. Correlation vs
causation; 2+ confidence levels; support/refutation signals. All claims provenance-tagged. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.**

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. All four artifacts present.

**Timing directive:** Fill FORM-PRE-S5 before Stage 5 output.
HOMOGENEITY INVARIANT: confirm N/A cells carry IB-IDs.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]` with: campaign
summary; consensus/conflict findings; hypothesis verdicts; confidence distribution; gaps; one-sentence
decision readiness verdict. All claims provenance-tagged. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

---

### Final Output

**Section 1 -- Evidence Brief** (ARTIFACT-S5 in full)

**Section 2 -- Gate Record** (from preamble template)

**Section 3 -- Consolidated Invocation Audit Table**

| Rule | Stage | Phase | Form ID | Antipattern | Result |
|------|-------|-------|---------|-------------|--------|
| ATTRIBUTION | S1 | PRE | FORM-PRE-S1 | attribution collapse [IB-ATTR] | |
| ATTRIBUTION | S1 | POST | FORM-POST-S1 | attribution collapse [IB-ATTR] | |
| CALIBRATION | S1 | N/A | -- | uniform confidence [IB-CAL] | N/A |
| FALSIFICATION | S1 | N/A | -- | unfalsifiable hypothesis [IB-FALS] | N/A |
| PROVENANCE | S1 | N/A | -- | unconstrained synthesis [IB-PROV] | N/A |
| *(continue for S2-S5; 47 rows; Antipattern column carries English name + [IB-ID] per HOMOGENEITY INVARIANT)* | | | | | |

Note: Antipattern column uses English+IB-ID format; not FK-typed to IB-IDs only (C-49 not targeted).
Row count: **47** (derived from coverage map).

---
---

## V-04 -- Combined A+B: Typed-ID-only binary cells + FK-typed audit table (C-48 + C-49)

**Variation axis:** Intel-first ordering (carries C-43 -- SEQUENCING-ORDER names live ordering
decision explicitly). Binary cells use typed-ID-only annotation (C-48: `[ Yes / No ] — [IB-ATTR]`).
Audit table column FK-typed to IB-IDs (C-49: `Antipattern (IB-ID FK)` header, IB-ID values only).
N/A cells carry English antipattern names only -- no IB-IDs (C-50 not satisfied: N/A tier lacks
IB-IDs; HOMOGENEITY INVARIANT not declared). Checksum narrative (C-46). IB fixture (C-45).

**Hypothesis:** C-48 and C-49 are independently satisfiable and reinforce each other when combined:
the binary cells cite fixtures by ID (C-48) and the audit table's antipattern column uses the same
IDs as FK references (C-49), making the two artifacts jointly auditable against the same IB fixture.
C-50 fails because N/A cells carry only English names -- the third tier breaks homogeneity. The
combination C-48+C-49 is achievable without the N/A tier upgrade.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

**Stage ordering note:** This campaign runs Intelligence (S1) before Web (S2) -- a non-default
SEQUENCING-ORDER-governed decision declared at Stage 1.

---

#### Inertia Baseline: Canonical Antipattern Vocabulary Fixture

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

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Excluded antipattern: **attribution collapse** [IB-ATTR].

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary. At least two distinct levels required.
Excluded antipattern: **uniform confidence** [IB-CAL].

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition.
Principle: "A hypothesis without a falsification condition is a belief."
Excluded antipattern: **unfalsifiable hypothesis** [IB-FALS].

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence stages complete before hypothesis declaration.
Principle: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis."
Excluded antipattern: **hypothesis-first mode** [IB-SEQ-H].

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage relative ordering. **This campaign: Intel-first (S1 = Intelligence, S2 = Web)
-- a non-default ordering; named and governed at S1 PRE.**
Excluded antipattern: **unordered collection** [IB-SEQ-O].

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Excluded antipattern: **unconstrained synthesis** [IB-PROV].

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

**Checksum:** 17 x 2 + 13 x 1 = **47.** Architectural history: prior monolithic SEQUENCING (5 rules,
40 artifacts). Decomposition: SEQUENCING -> SEQUENCING-HYPO + SEQUENCING-ORDER; +7 artifacts
propagated automatically. 40 - 8 + 15 = **47. No static integer updated manually.**

---

#### Gate Record Template (pre-instantiated blank)

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|:----------:|:---------:|
| S1 | Intelligence Analyst | Pass (first stage) | [ Pass / Fail ] |
| S2 | Web Evidence Collector | [ Pass / Fail ] | [ Pass / Fail ] |
| S3 | Hypothesis Architect | [ Pass / Fail ] | [ Pass / Fail ] |
| S4 | Evidence Analyst | [ Pass / Fail ] | [ Pass / Fail ] |
| S5 | Synthesis Director | [ Pass / Fail ] | [ Pass / Fail ] |

---

#### Form Templates (blank -- pre-instantiated; C-48: binary cells use typed-ID-only annotation)

**Cell format contract (C-48):** Binary cell annotations use only `[IB-XXX]` typed identifiers. No
English antipattern name appears in any binary cell body. Mechanical verification: parse each
annotation -- any token that is not `[IB-XXX]` format is a C-48 violation.

**FORM-PRE-S1** (fill before Stage 1 output -- declare Intel-first as governed SEQUENCING-ORDER decision):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; Intel-first ordered as governed decision |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable). FALSIFICATION -- N/A (no hypotheses declared). PROVENANCE -- N/A (not scope-restricted).

**FORM-POST-S1** (fill after Stage 1 output is complete):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; Intel-first executed as governed decision |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; S2 Web follows Intel-first governed order |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable). FALSIFICATION -- N/A (no hypotheses declared). PROVENANCE -- N/A (not scope-restricted).

**FORM-POST-S2** (fill after Stage 2 output is complete):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; Intel-first ordering confirmed at S2 |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-FALS] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-PROV] |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage; uniform-confidence antipattern not applicable). SEQUENCING-ORDER -- N/A (governs S1, S2 only).

**FORM-POST-S3** (fill after Stage 3 output is complete):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-FALS] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-PROV] |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL]; 2+ distinct confidence levels required | [ Yes / No ] — [IB-PROV] |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A (verdicts at S3/S5; unfalsifiable-hypothesis antipattern not applicable at analysis stage). SEQUENCING-HYPO -- N/A (analysis stage). SEQUENCING-ORDER -- N/A (analysis stage).

**FORM-POST-S4** (fill after Stage 4 output is complete):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] — [IB-PROV] |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL] | [ Yes / No ] — [IB-FALS]; all verdicts stated? | [ Yes / No ] — [IB-PROV] |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A (synthesis stage; hypothesis-first mode not applicable). SEQUENCING-ORDER -- N/A (synthesis stage; unordered-collection antipattern not applicable).

**FORM-POST-S5** (fill after Stage 5 output is complete):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] — [IB-FALS] | [ Yes / No ] — [IB-PROV] |

---

### Stage 1 -- Intelligence Analyst (Intel-first; SEQUENCING-ORDER decision declared here)

**Entry condition:** First stage. No prior artifacts. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S1 (from preamble) before any Stage 1 output. Record
`[IB-SEQ-O]` resolved: Intel-first ordered as governed decision.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search internal sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S1:
Intelligence Assessment** with 3+ findings labeled `[intel]`. Include file-path citations; relevance
assessment. No hypothesis stated. Stage-index: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 complete; no hypothesis stated; Intel-first decision named by
`[IB-SEQ-O]` identifier in PRE and POST cells.

> **Handoff S1 -> S2: Role passes to Stage 2 -- Web Evidence Collector.**
> Artifacts transferred: ARTIFACT-S1 (Intelligence Assessment). Web Evidence Collector authorized reads: ARTIFACT-S1 only.
> **SEQUENCING-ORDER:** S2 Web follows Intel-first governed ordering declared at S1.
> **PROVENANCE RULE status:** Not yet activated. Activates at S2->S3 handoff.

---

### Stage 2 -- Web Evidence Collector

**Entry condition:** S1 exit gate Pass. Intel-first ordering in effect. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 (from preamble) before any Stage 2 output.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search external sources. Produce **ARTIFACT-S2: Web Findings Corpus** with
6+ findings labeled `[web]`. Stage-index: **S2**.

[Fill FORM-POST-S2 here]

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> Authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + S2 only.

**Timing directive:** Fill FORM-PRE-S3 (from preamble) before Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare 3-5 hypotheses. Produce **ARTIFACT-S3: Hypothesis Register** labeled
`[hypothesis]`. Each: claim; falsification condition; confidence; provenance tags. Stage-index: **S3**.

[Fill FORM-POST-S3 here]

> **Handoff S3 -> S4: Role passes to Stage 4 -- Evidence Analyst.** PROVENANCE: REMAINS ACTIVE.

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + S2 + S3 only.

**Timing directive:** Fill FORM-PRE-S4 (from preamble) before Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Produce **ARTIFACT-S4: Evidence Analysis** labeled `[analysis]`. 2+ confidence
levels (`[IB-CAL]` guard); support/refutation signals; all claims provenance-tagged. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.** PROVENANCE: REMAINS ACTIVE.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. All four artifacts present.

**Timing directive:** Fill FORM-PRE-S5 (from preamble) before Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]` with: campaign
summary (Intel-first order, SEQUENCING-ORDER governed); consensus/conflict findings; hypothesis verdicts;
confidence distribution; gaps; one-sentence decision readiness verdict. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

---

### Final Output

**Section 1 -- Evidence Brief** (ARTIFACT-S5 in full)

**Section 2 -- Gate Record** (from preamble template)

**Section 3 -- Consolidated Invocation Audit Table (FK-typed antipattern column)**

| Rule | Stage | Phase | Form ID | Antipattern (IB-ID FK) | Result |
|------|-------|-------|---------|------------------------|--------|
| ATTRIBUTION | S1 | PRE | FORM-PRE-S1 | IB-ATTR | |
| ATTRIBUTION | S1 | POST | FORM-POST-S1 | IB-ATTR | |
| SEQUENCING-HYPO | S1 | PRE | FORM-PRE-S1 | IB-SEQ-H | |
| SEQUENCING-HYPO | S1 | POST | FORM-POST-S1 | IB-SEQ-H | |
| SEQUENCING-ORDER | S1 | PRE | FORM-PRE-S1 | IB-SEQ-O | |
| SEQUENCING-ORDER | S1 | POST | FORM-POST-S1 | IB-SEQ-O | |
| CALIBRATION | S1 | N/A | -- | IB-CAL | N/A |
| FALSIFICATION | S1 | N/A | -- | IB-FALS | N/A |
| PROVENANCE | S1 | N/A | -- | IB-PROV | N/A |
| *(continue for S2 through S5 -- 47 rows total)* | | | | | |

**Column contract (C-49):** `Antipattern (IB-ID FK)` column contains only IB-ID values. No English
names. Row count: **47** (derived from coverage map). Binary cells use `[IB-XXX]` typed-ID-only
format (C-48). N/A cells carry English names only -- third tier not IB-ID cited (C-50 absent).

---
---

## V-05 -- Combined A+B+C: Full integration (C-48 + C-49 + C-50)

**Variation axis:** Intel-first ordering (C-43). Binary cells: typed-ID-only `[IB-ATTR]` annotation
(C-48). Audit table: FK-typed `Antipattern (IB-ID FK)` column (C-49). N/A cells: carry IB-IDs
alongside English names (all three tiers carry IB-IDs). Explicit HOMOGENEITY INVARIANT declaration
(C-50). Checksum narrative (C-46). IB fixture (C-45). All R19 baseline criteria carried forward.

**Hypothesis:** With all three criteria satisfied simultaneously, the invocation apparatus achieves
complete structural homogeneity across every cell type and every output artifact. Binary cells are
mechanically verifiable by ID-syntax (C-48). The audit table is a reference table joinable against the
IB fixture by identifier (C-49). Every cell in every tier -- PRE binary, POST binary, N/A -- carries
an IB-ID, and this uniformity is declared as an invariant (C-50). The three criteria reinforce each
other: C-48 makes individual binary cells machine-checkable; C-49 makes the audit table machine-
checkable; C-50 makes the tier-uniformity property explicit and referenceable by name. Together they
convert the invocation apparatus from a documentation artifact into a self-auditing reference system.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

**Stage ordering note:** This campaign runs Intelligence (S1) before Web (S2) -- a non-default
SEQUENCING-ORDER-governed decision declared at Stage 1 via `[IB-SEQ-O]`.

---

#### Inertia Baseline: Canonical Antipattern Vocabulary Fixture

| IB ID | Antipattern Name | Governing Rule | Detection Point | Consequence |
|-------|-----------------|----------------|-----------------|-------------|
| IB-ATTR | Attribution collapse | ATTRIBUTION | Every stage POST | Non-compliant finding; stage ATTRIBUTION fails |
| IB-CAL | Uniform confidence | CALIBRATION | S4 POST, S5 POST | CALIBRATION fails; recalibrate before exit |
| IB-FALS | Unfalsifiable hypothesis | FALSIFICATION | S3 POST, S5 POST | Hypothesis removed from register |
| IB-SEQ-H | Hypothesis-first mode | SEQUENCING-HYPO | S3 PRE | Stage 3 blocked until S1+S2 exits confirmed |
| IB-SEQ-O | Unordered collection | SEQUENCING-ORDER | S1 PRE | SEQUENCING-ORDER fails; ordering must be named |
| IB-PROV | Unconstrained synthesis | PROVENANCE | S3/S4/S5 PRE | Provenance gate fails; source artifact required |

**HOMOGENEITY INVARIANT (C-50):** PRE binary cells, POST binary cells, and N/A cells all cite
IB-IDs uniformly. No cell tier is exempt. Binary cells: `[ Yes / No ] — [IB-XXX]` (typed-ID-only,
no English name in annotation body). N/A cells: `-- N/A [IB-XXX] (structural reason; antipattern
name not applicable)`. Any cell that lacks an `[IB-XXX]` reference is a homogeneity violation
detectable by identifier-syntax scan, independent of English name correctness.

---

#### Rule Registry (all six rules are peers; no rule is primary)

Adding a seventh peer rule propagates automatically through coverage map, checksum, and form templates;
no static integers require manual update.

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every material claim names its source stage: `[intel]` S1, `[web]` S2, `[hypothesis]` S3,
`[analysis]` S4, `[synthesis]` S5. An unlabeled claim fails ATTRIBUTION.
Excluded antipattern: **attribution collapse** [IB-ATTR].

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary. Distribution must show at least two distinct levels. Anti-uniformity
guard active at S4 and S5: state distribution explicitly.
Excluded antipattern: **uniform confidence** [IB-CAL].

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition. Final status: Supported / Refuted /
Indeterminate.
Principle: "A hypothesis without a falsification condition is a belief."
Excluded antipattern: **unfalsifiable hypothesis** [IB-FALS].

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence stages (S1, S2) complete before hypothesis declaration (S3).
Principle: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis."
Excluded antipattern: **hypothesis-first mode** [IB-SEQ-H].

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage relative ordering. **This campaign: Intel-first (S1 = Intelligence, S2 = Web)
-- a non-default ordering; named and governed at S1 PRE via `[IB-SEQ-O]`.**
Excluded antipattern: **unordered collection** [IB-SEQ-O].

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at handoff boundary preceding scope-restricted stage. Claims in S3, S4, S5 carry
`[source: Stage N -- Artifact Name]`.
Excluded antipattern: **unconstrained synthesis** [IB-PROV].

---

#### Role Roster (access scope declared; provenance activation at handoff boundary)

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Intelligence Analyst | Internal sources only. No prior artifacts. |
| S2 | Web Evidence Collector | ARTIFACT-S1 (Intelligence Assessment) only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Web Findings Corpus) only. |
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
**47 invocation artifacts.** Architectural history: prior monolithic SEQUENCING rule (5 rules, 40
total artifacts). Decomposition event: SEQUENCING split into SEQUENCING-HYPO (IB-SEQ-H: 3 positive
+ 2 negative = 8 artifacts) and SEQUENCING-ORDER (IB-SEQ-O: 2 positive + 3 negative = 10 artifacts),
replacing the original 8 artifacts with 18. Wait -- correction applying map: SEQUENCING-HYPO has
3 positive x 2 + 2 negative x 1 = 8 artifacts; SEQUENCING-ORDER has 2 positive x 2 + 3 negative x
1 = 7 artifacts; combined 15 artifacts replacing the original 8. Delta: +7 propagated automatically.
40 - 8 + 15 = **47. No static integer updated manually.** Derived from map dimensions; updates
automatically when rules or stages are added.

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

#### Form Templates (blank -- pre-instantiated; HOMOGENEITY INVARIANT enforced across all tiers)

**Cell format contracts:**
- **(C-48) Binary cells:** annotation is `[IB-XXX]` typed identifier only. No English name in cell body.
- **(C-50) N/A cells:** format is `-- N/A [IB-XXX] (structural reason)`. IB-ID must appear in every N/A declaration.
- Both contracts enforced by identifier-syntax scan; name-string matching not required.

**FORM-PRE-S1** (fill before Stage 1 output -- declare Intel-first as governed SEQUENCING-ORDER decision):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; Intel-first ordered as governed decision |

N/A [Stage 1 of 5]: CALIBRATION -- N/A [IB-CAL] (evidence stage; uniform-confidence antipattern not applicable). FALSIFICATION -- N/A [IB-FALS] (no hypotheses declared; unfalsifiable-hypothesis antipattern not applicable). PROVENANCE -- N/A [IB-PROV] (not scope-restricted; unconstrained-synthesis antipattern not applicable here).

**FORM-POST-S1** (fill after Stage 1 output is complete):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; Intel-first executed as governed decision |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; S2 Web follows Intel-first governed order |

N/A [Stage 2 of 5]: CALIBRATION -- N/A [IB-CAL] (evidence stage; uniform-confidence antipattern not applicable). FALSIFICATION -- N/A [IB-FALS] (no hypotheses declared; unfalsifiable-hypothesis antipattern not applicable). PROVENANCE -- N/A [IB-PROV] (not scope-restricted; unconstrained-synthesis antipattern not applicable).

**FORM-POST-S2** (fill after Stage 2 output is complete):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-SEQ-O]; Intel-first ordering confirmed at S2 |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-FALS] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-PROV] |

N/A [Stage 3 of 5]: CALIBRATION -- N/A [IB-CAL] (hypothesis stage; uniform-confidence antipattern not applicable). SEQUENCING-ORDER -- N/A [IB-SEQ-O] (governs S1, S2 only; unordered-collection antipattern not applicable here).

**FORM-POST-S3** (fill after Stage 3 output is complete):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-FALS] | [ Yes / No ] — [IB-SEQ-H] | [ Yes / No ] — [IB-PROV] |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL]; 2+ distinct confidence levels required | [ Yes / No ] — [IB-PROV] |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A [IB-FALS] (verdicts at S3/S5; unfalsifiable-hypothesis antipattern not applicable at analysis stage). SEQUENCING-HYPO -- N/A [IB-SEQ-H] (analysis stage; hypothesis-first mode not applicable). SEQUENCING-ORDER -- N/A [IB-SEQ-O] (analysis stage; unordered-collection antipattern not applicable).

**FORM-POST-S4** (fill after Stage 4 output is complete):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] — [IB-PROV] |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL] | [ Yes / No ] — [IB-FALS]; all verdicts stated? | [ Yes / No ] — [IB-PROV] |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A [IB-SEQ-H] (synthesis stage; hypothesis-first mode not applicable). SEQUENCING-ORDER -- N/A [IB-SEQ-O] (synthesis stage; unordered-collection antipattern not applicable).

**FORM-POST-S5** (fill after Stage 5 output is complete):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] — [IB-ATTR] | [ Yes / No ] — [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] — [IB-FALS] | [ Yes / No ] — [IB-PROV] |

---

### Stage 1 -- Intelligence Analyst (Intel-first; SEQUENCING-ORDER governed decision declared here)

**Entry condition:** First stage. No prior artifacts. No hypothesis stated anywhere in this document.

**Timing directive:** Fill FORM-PRE-S1 (from preamble) before any Stage 1 output.
C-48 check: binary annotations are `[IB-XXX]` only -- no English names. C-50 check: N/A cells
carry `[IB-XXX]` identifiers per HOMOGENEITY INVARIANT.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search internal sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S1:
Intelligence Assessment** with 3+ findings labeled `[intel]`. Include: file-path citations; relevance
assessment (High / Medium / Low); notable patterns. No hypothesis stated. Stage-index column: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 complete with 3+ labeled `[intel]` findings; no hypothesis stated;
`[IB-SEQ-O]` Intel-first decision named in PRE and POST cells; all form annotations typed-ID-only.

> **Handoff S1 -> S2: Role passes to Stage 2 -- Web Evidence Collector.**
> Artifacts transferred: ARTIFACT-S1 (Intelligence Assessment).
> Web Evidence Collector authorized reads: ARTIFACT-S1 only.
> **SEQUENCING-ORDER [IB-SEQ-O]:** S2 Web follows Intel-first governed ordering declared at S1.
> **PROVENANCE RULE [IB-PROV] status:** Not yet activated. Activates at S2->S3 handoff.

---

### Stage 2 -- Web Evidence Collector

**Entry condition:** S1 exit gate Pass. Intel-first ordering in effect. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 (from preamble) before any Stage 2 output.
C-48 check: binary annotations typed-ID-only. C-50 check: N/A cells carry IB-IDs.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search external sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S2:
Web Findings Corpus** with 6+ findings labeled `[web]`. Include: direct quotes with source attribution;
source strength (Strong / Moderate / Weak); market, technical, competitive, risk dimensions. No
hypothesis stated. Stage-index: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 with 6+ labeled `[web]` findings; no hypothesis stated.

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: ARTIFACT-S2 (Web Findings Corpus). Prior: ARTIFACT-S1.
> Hypothesis Architect authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE [IB-PROV] status at this boundary: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2.
> Every claim in Stage 3 must carry `[source: Stage N -- Artifact Name]`.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. PROVENANCE RULE [IB-PROV] active. Access: ARTIFACT-S1 + S2 only.

**Timing directive:** Fill FORM-PRE-S3 (from preamble) before any Stage 3 output.
C-48 check: binary annotations typed-ID-only. C-50 check: N/A cells carry IB-IDs.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare hypotheses grounded in ARTIFACT-S1 and ARTIFACT-S2. Produce
**ARTIFACT-S3: Hypothesis Register** with 3-5 hypotheses labeled `[hypothesis]`. For each:
(1) claim; (2) explicit falsification condition (`[IB-FALS]` guard); (3) initial confidence
(High / Medium / Low); (4) evidence citations with `[source: Stage N -- Artifact Name]`. Rationale:
"A hypothesis anchored before evidence gathering is a bias, not a hypothesis." Stage-index: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** ARTIFACT-S3 with 3-5 falsifiable hypotheses; all claims carrying provenance tags.

> **Handoff S3 -> S4: Role passes to Stage 4 -- Evidence Analyst.**
> Artifacts transferred: ARTIFACT-S3 (Hypothesis Register). Prior: ARTIFACT-S1, ARTIFACT-S2.
> Evidence Analyst authorized reads: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.
> **PROVENANCE RULE [IB-PROV] status: REMAINS ACTIVE** for all three artifacts.

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + S2 + S3 only.

**Timing directive:** Fill FORM-PRE-S4 (from preamble) before any Stage 4 output.
C-48 check: binary annotations typed-ID-only. C-50 check: N/A cells carry IB-IDs.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Analyze evidence against hypotheses. Produce **ARTIFACT-S4: Evidence Analysis**
labeled `[analysis]`. Include: patterns from S1+S2 with correlation vs causation distinctions;
confidence distribution with at least two distinct levels (`[IB-CAL]` guard: if all same, recalibrate);
support/refutation signals per hypothesis. All claims carry `[source: Stage N -- Artifact Name]`.
Stage-index: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** ARTIFACT-S4 with non-uniform confidence distribution; all provenance-tagged.

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.**
> Artifacts transferred: ARTIFACT-S4 (Evidence Analysis). Prior: ARTIFACT-S1, S2, S3.
> Synthesis Director authorized reads: all four prior artifacts.
> **PROVENANCE RULE [IB-PROV] status: REMAINS ACTIVE** for all four artifacts.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. All four artifacts present. PROVENANCE RULE active.

**Timing directive:** Fill FORM-PRE-S5 (from preamble) before any Stage 5 output.
C-48 check: binary annotations typed-ID-only. C-50 check: N/A cells carry IB-IDs.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]` with:
1. **Campaign summary** -- topic; 5 stages in Intel-first order (SEQUENCING-ORDER [IB-SEQ-O] governed).
2. **Consensus findings** -- where ARTIFACT-S1 and ARTIFACT-S2 agree; cite both with stage attribution.
3. **Conflict findings** -- where S1 and S2 diverge; name divergence and assess significance.
4. **Hypothesis verdicts** -- Supported / Refuted / Indeterminate per hypothesis; falsification status.
5. **Confidence distribution** -- N High, N Medium, N Low. `[IB-CAL]` guard: if all same, recalibrate.
6. **Gaps and open questions** -- what remains unknown after the full campaign.
7. **Decision readiness** -- one sentence: "Ready to proceed" OR "Needs more investigation on [X]."

All claims carry `[source: Stage N -- Artifact Name]`. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

**Exit condition:** ARTIFACT-S5 complete with consensus/conflict synthesis, calibrated confidence,
one-sentence decision readiness verdict.

---

### Final Output

**Section 1 -- Evidence Brief** (ARTIFACT-S5 in full; self-contained)

**Section 2 -- Gate Record** (filled from preamble template; all 5 stages, entry and exit)

**Section 3 -- Consolidated Invocation Audit Table (FK-typed; HOMOGENEITY INVARIANT verified)**

| Rule | Stage | Phase | Form ID | Antipattern (IB-ID FK) | Result |
|------|-------|-------|---------|------------------------|--------|
| ATTRIBUTION | S1 | PRE | FORM-PRE-S1 | IB-ATTR | |
| ATTRIBUTION | S1 | POST | FORM-POST-S1 | IB-ATTR | |
| SEQUENCING-HYPO | S1 | PRE | FORM-PRE-S1 | IB-SEQ-H | |
| SEQUENCING-HYPO | S1 | POST | FORM-POST-S1 | IB-SEQ-H | |
| SEQUENCING-ORDER | S1 | PRE | FORM-PRE-S1 | IB-SEQ-O | |
| SEQUENCING-ORDER | S1 | POST | FORM-POST-S1 | IB-SEQ-O | |
| CALIBRATION | S1 | N/A | -- | IB-CAL | N/A |
| FALSIFICATION | S1 | N/A | -- | IB-FALS | N/A |
| PROVENANCE | S1 | N/A | -- | IB-PROV | N/A |
| *(continue for S2 through S5 -- 47 rows total; all IB Row values from IB fixture)* | | | | | |

**Column contracts:**
- `Antipattern (IB-ID FK)`: IB-ID values only. No English names. Join-auditable against IB fixture. (C-49)
- Binary cells in forms: `[IB-XXX]` typed-ID-only annotation. No English names. (C-48)
- N/A rows in this table: IB-ID values in FK column. N/A cells in forms: `[IB-XXX]` present. (C-50)
- Row count: **47** (derived from coverage map dimensions; updates automatically when rules added).
- HOMOGENEITY INVARIANT verification: scan all cell annotations for `[IB-XXX]` token -- any cell
  (binary or N/A, forms or table) lacking this token is a C-50 violation detectable by identifier-
  syntax parsing without interpretation.
