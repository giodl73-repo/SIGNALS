---
skill: quest-variate
skill_target: campaign-evidence
date: 2026-03-17
round: 17
rubric_version: 17
---

# Variates: campaign-evidence (Round 17)

**Skill**: campaign-evidence
**Rubric**: v17 (C-01--C-07 essential+recommended; C-08--C-42 aspirational; denominator 35)
**Date**: 2026-03-17
**Round**: 17

---

## Context: what informed this round

R16 delivered two PASS+ signals that form the R17 targets:

| R16 signal | Where it appeared | What it demonstrated |
|-----------|-------------------|----------------------|
| V-03 PASS+ on C-39 | `"Will ATTRIBUTION hold?"` as column header | Rule-named interrogative header makes each checkpoint table self-describing when removed from context |
| V-02 PASS+ on C-40 | SEQUENCING split into SEQUENCING-HYPO and SEQUENCING-ORDER | Two peer rules with independent coverage-map rows and invocation trails; checksum shift to 47 demonstrates C-29 extensibility in live action |

R16's V-05 was the sole variation to pass C-37/C-38 (named dual tables physically separated by
execution content) but failed C-39 because its table names were artifact labels ("NAMED-PRE",
"NAMED-POST"), not interrogatives. V-01 through V-04 passed C-39 but failed C-37/C-38 because
zone markers (`-- PRE --` / `-- POST --`) do not produce two physically-separated table artifacts.

**R17 challenge**: Combine V-05's named-table physical separation with V-03's rule-named column
headers AND V-02's SEQUENCING decomposition.

**New criteria in v17 rubric:**
- **C-41**: Column headers name the specific governance rule under interrogation — "Will ATTRIBUTION
  hold?" not "Will this rule hold?" A generic interrogative shared across all rules does not pass.
- **C-42**: SEQUENCING decomposed into independently-trackable peer rules SEQUENCING-HYPO and
  SEQUENCING-ORDER, each with its own coverage-map row, invocation trail, and checksum contribution.
  Checksum shift from 40 to 47 demonstrates C-29 extensibility.

**Three variation axes for R17:**
- **Axis A**: Rule-named interrogative column headers on physically-separated named tables (C-41)
- **Axis B**: SEQUENCING decomposed into peer rules with independent tracking (C-42)
- **Axis C**: Inertia framing — named excluded antipatterns within rule declarations

**Checksum implications:**
- 5 rules (SEQUENCING single): 15 positive × 2 phases + 10 negative = **40 invocation artifacts**
- 6 rules (SEQUENCING-HYPO + SEQUENCING-ORDER): 17 positive × 2 phases + 13 negative = **47 invocation artifacts**

**R16 baseline carried forward by all R17 variates (C-01 through C-38):**
Multi-stage campaign, evidence-first, falsifiable hypotheses, self-contained output,
stage attribution, consensus/conflict synthesis, calibrated confidence, gaps + decision verdict,
named rules at preamble + point-of-use, prospective immutable coverage map, inline scope
annotations, universal binary invocation, stage-index suffixes, entry/exit gates, gate record
pre-templated, column-encoded sequencing, extensible governance, named role handoffs, negative
invocations, access-scope declarations, derivable checksum, artifact provenance tags,
dual-phase PRE/POST checkpoints, handoff artifact enumeration + provenance activation,
**named PRE/POST table artifacts physically separated by execution content**,
complete apparatus pre-instantiated in preamble with timing directives.

---

## V-01 -- Axis A: Rule-named interrogative column headers (C-41 only; SEQUENCING = single rule)

**Variation axis:** Output format — each stage uses a named PRE table and a named POST table,
physically separated by execution content, where each applicable rule occupies its own column
with a rule-named interrogative header (e.g., "Will ATTRIBUTION hold? [Stage 1 of 5]").
Non-applicable rules appear in an N/A block immediately below the PRE table. SEQUENCING
remains a single rule to isolate the C-41 axis.

**Hypothesis:** Multi-column rule-named headers on physically-separated named table artifacts
satisfy C-41 without per-rule table proliferation. "Will ATTRIBUTION hold?" as a column header
makes the checkpoint self-describing: any blank POST cell is an unanswered commitment about
ATTRIBUTION specifically. Combining with V-05's named-table structure satisfies C-37/C-38 + C-41
simultaneously. SEQUENCING kept single (5 rules, checksum 40) to confirm C-41 independently.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable — cannot be modified after any stage executes.**

---

#### Rule Registry (all five rules are peers; no rule is primary)

Adding a sixth peer rule propagates automatically through the coverage map, checksum, and form
templates; no static integers require manual update.

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every material claim names its source stage: `[web]` for S1, `[intel]` for S2,
`[hypothesis]` for S3, `[analysis]` for S4, `[synthesis]` for S5. An unlabeled claim fails.
Anti-pattern: claim without a stage source tag.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary. Distribution must show at least two distinct levels. Anti-uniformity
guard: if all findings at any positive stage carry the same confidence level, CALIBRATION fails.
State distribution explicitly at S4 and S5.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition — a criterion whose occurrence would
cause the hypothesis to be rejected. Final status options: Supported / Refuted / Indeterminate.
Principle: "A hypothesis without a falsification condition is a belief."

**SEQUENCING RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Governs two dimensions: (1) hypothesis placement — evidence stages (S1, S2) complete before
hypothesis declaration (S3); (2) evidence-stage relative ordering — the ordering among evidence
stages is a named, governed decision invokable by identifier. Principle: "A hypothesis anchored
before evidence gathering is a bias, not a hypothesis." Excluded antipattern: hypothesis-first mode.

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at the handoff boundary preceding each scope-restricted stage. Every claim in S3, S4,
S5 carries `[source: Stage N -- Artifact Name]`. A claim without a provenance tag is a gap.
Activation is a live transfer event at the handoff boundary, not a static role-charter property.

---

#### Role Roster (access scope declared; provenance activation occurs at handoff boundary)

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Web Evidence Collector | External sources only. No prior artifacts. |
| S2 | Intelligence Analyst | ARTIFACT-S1 (Web Findings Corpus) only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Intelligence Assessment) only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 (Hypothesis Register) only. |
| S5 | Synthesis Director | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 + ARTIFACT-S4 (Evidence Analysis) only. |

---

#### Coverage Map (immutable -- sealed before Stage 1; cannot be modified after execution begins)

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|-----|----------|----------|
| ATTRIBUTION   | + | + | + | + | + | 5 | 0 |
| CALIBRATION   | - | - | - | + | + | 2 | 3 |
| FALSIFICATION | - | - | + | - | + | 2 | 3 |
| SEQUENCING    | + | + | + | - | - | 3 | 2 |
| PROVENANCE    | - | - | + | + | + | 3 | 2 |
| **Total**     |   |   |   |   |   | **15** | **10** |

**Checksum (derivable expression):** 15 positive cells × 2 phases = 30 PRE/POST pairs;
10 negative cells × 1 = 10 N/A declarations. **Total: 40 invocation artifacts.**
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

#### Form Templates (blank -- pre-instantiated per C-38; fill at stages following timing directives)

**FORM-PRE-S1** (fill before writing any Stage 1 output):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING hold? [Stage 1 of 5] |
|---------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage; no confidence ratings); FALSIFICATION -- N/A (no hypotheses declared); PROVENANCE -- N/A (Stage 1 not scope-restricted; rule activates at S2->S3 handoff).

**FORM-POST-S1** (fill after Stage 1 output is complete):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING hold? [Stage 1 of 5] |
|---------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] |

---

**FORM-PRE-S2** (fill before writing any Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING hold? [Stage 2 of 5] |
|---------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] |

N/A [Stage 2 of 5]: CALIBRATION -- N/A (evidence stage); FALSIFICATION -- N/A (no hypotheses); PROVENANCE -- N/A (not scope-restricted).

**FORM-POST-S2** (fill after Stage 2 output is complete):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING hold? [Stage 2 of 5] |
|---------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] |

---

**FORM-PRE-S3** (fill before writing any Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|--------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (no confidence ratings at hypothesis stage).

**FORM-POST-S3** (fill after Stage 3 output is complete):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|--------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

---

**FORM-PRE-S4** (fill before writing any Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A (falsification verdicts at S3/S5, not analysis); SEQUENCING -- N/A (analysis stage; sequencing rule governs only S1-S3).

**FORM-POST-S4** (fill after Stage 4 output is complete):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

---

**FORM-PRE-S5** (fill before writing any Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

N/A [Stage 5 of 5]: SEQUENCING -- N/A (synthesis stage; evidence collection complete; sequencing rule does not govern S4 or S5).

**FORM-POST-S5** (fill after Stage 5 output is complete):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

---

### Stage 1 -- Web Evidence Collector

**Entry condition:** First stage. No prior artifacts. No hypothesis stated anywhere in this document.

**Timing directive:** Fill FORM-PRE-S1 (from preamble) before writing any Stage 1 output.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search the web for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S1: Web Findings Corpus** with at minimum 6 findings, each labeled `[web]`. Include: direct quotes or data with source attribution; source strength (Strong / Moderate / Weak); coverage across market, technical, competitive, and risk dimensions. Do not state any hypothesis. Stage-index column value: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 complete with 6+ labeled `[web]` findings; no hypothesis stated.

> **Handoff S1 -> S2: Role passes to Stage 2 -- Intelligence Analyst.**
> Artifacts transferred: ARTIFACT-S1 (Web Findings Corpus).
> Intelligence Analyst authorized reads: ARTIFACT-S1 only.
> **PROVENANCE RULE status at this boundary:** Not yet activated. Stage 2 is not scope-restricted.
> PROVENANCE RULE will activate at the S2->S3 handoff.

---

### Stage 2 -- Intelligence Analyst

**Entry condition:** S1 exit gate Pass. Handoff S1->S2 complete. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 (from preamble) before writing any Stage 2 output.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search internal sources (codebase, specs, prior analyses, documentation) for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S2: Intelligence Assessment** with at minimum 3 findings, each labeled `[intel]`. Include: file-path citations for codebase evidence; relevance assessment (High / Medium / Low); contrasts with ARTIFACT-S1 findings where notable. Do not state any hypothesis. Stage-index column value: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 complete with 3+ labeled `[intel]` findings; no hypothesis stated.

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: ARTIFACT-S2 (Intelligence Assessment). Prior artifact: ARTIFACT-S1.
> Hypothesis Architect authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE status at this boundary: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2.
> Every claim in Stage 3 must carry `[source: Stage N -- Artifact Name]`.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. Handoff S2->S3 complete. PROVENANCE RULE active.

**Access scope:** ARTIFACT-S1 and ARTIFACT-S2 only. No pre-campaign assumptions.

**Timing directive:** Fill FORM-PRE-S3 (from preamble) before writing any Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare hypotheses grounded exclusively in ARTIFACT-S1 and ARTIFACT-S2. Produce **ARTIFACT-S3: Hypothesis Register** with 3--5 hypotheses, each labeled `[hypothesis]`. For each hypothesis: (1) claim statement; (2) explicit falsification condition; (3) initial confidence (High / Medium / Low); (4) supporting evidence citations with `[source: Stage N -- Artifact Name]` tags. Rationale for post-evidence declaration: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis." Stage-index column value: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** ARTIFACT-S3 with 3--5 falsifiable hypotheses; all claims carrying provenance tags.

> **Handoff S3 -> S4: Role passes to Stage 4 -- Evidence Analyst.**
> Artifacts transferred: ARTIFACT-S3 (Hypothesis Register). Prior artifacts: ARTIFACT-S1, ARTIFACT-S2.
> Evidence Analyst authorized reads: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.
> **PROVENANCE RULE status at this boundary: REMAINS ACTIVE** for all three artifacts.
> Every claim in Stage 4 must carry `[source: Stage N -- Artifact Name]`.

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit gate Pass. Handoff S3->S4 complete. PROVENANCE RULE active.

**Access scope:** ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 only.

**Timing directive:** Fill FORM-PRE-S4 (from preamble) before writing any Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Analyze evidence and hypotheses from prior artifacts. Produce **ARTIFACT-S4: Evidence Analysis** with findings labeled `[analysis]`. Include: pattern identification from S1+S2 together; correlation vs causation distinctions; confidence ratings with explicit distribution (must show at least two distinct levels: High / Medium / Low); support/refutation signals per hypothesis from ARTIFACT-S3. All claims carry `[source: Stage N -- Artifact Name]`. Stage-index column value: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** ARTIFACT-S4 with calibrated (non-uniform) confidence distribution; all provenance-tagged.

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.**
> Artifacts transferred: ARTIFACT-S4 (Evidence Analysis). Prior artifacts: ARTIFACT-S1, S2, S3.
> Synthesis Director authorized reads: all four prior artifacts.
> **PROVENANCE RULE status at this boundary: REMAINS ACTIVE** for all four artifacts.
> Every claim in Stage 5 must carry `[source: Stage N -- Artifact Name]`.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. Handoff S4->S5 complete. All four artifacts exist.

**Access scope:** ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4.

**Timing directive:** Fill FORM-PRE-S5 (from preamble) before writing any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Synthesize all evidence into a coherent brief. Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]` with:
1. **Campaign summary** -- what was investigated, which 5 stages ran.
2. **Consensus findings** -- where ARTIFACT-S1 and ARTIFACT-S2 agree; cite both.
3. **Conflict findings** -- where S1 and S2 diverge; name the divergence and its significance.
4. **Hypothesis verdicts** -- for each hypothesis in ARTIFACT-S3: Supported / Refuted / Indeterminate + confidence + falsification status.
5. **Confidence distribution** -- state explicitly: N High, N Medium, N Low. Anti-uniformity check: if all same level, CALIBRATION fails -- recalibrate before proceeding.
6. **Gaps and open questions** -- explicit list of what remains unknown after the full campaign.
7. **Decision readiness** -- one sentence: "Ready to proceed" OR "Needs more investigation on [specific gap] before committing."

All synthesis claims carry `[source: Stage N -- Artifact Name]`. Stage-index column value: **S5**.

[Fill FORM-POST-S5 here]

**Exit condition:** ARTIFACT-S5 complete with consensus/conflict synthesis, calibrated confidence, one-sentence decision verdict.

---

### Final Output

Produce the complete output containing three sections:

**Section 1 -- Evidence Brief** (ARTIFACT-S5 in full; self-contained for a reader unfamiliar with the run)

**Section 2 -- Gate Record** (filled from the preamble gate template; all 5 stages, entry and exit)

**Section 3 -- Consolidated Invocation Audit Table**

| Rule | Stage | Phase | Form ID | Result |
|------|-------|-------|---------|--------|
| ATTRIBUTION | S1 | PRE | FORM-PRE-S1 | |
| ATTRIBUTION | S1 | POST | FORM-POST-S1 | |
| SEQUENCING | S1 | PRE | FORM-PRE-S1 | |
| SEQUENCING | S1 | POST | FORM-POST-S1 | |
| CALIBRATION | S1 | N/A | FORM-PRE-S1 | N/A |
| FALSIFICATION | S1 | N/A | FORM-PRE-S1 | N/A |
| PROVENANCE | S1 | N/A | FORM-PRE-S1 | N/A |
| *(continue for S2 through S5 -- 40 rows total)* | | | | |

Row count must equal **40** (derived from coverage map: 15 positive × 2 + 10 negative × 1).
Any mismatch indicates a missing invocation artifact.

---
---

## V-02 -- Axis B: SEQUENCING decomposed into independently-trackable peer rules (C-42 only; generic headers)

**Variation axis:** Lifecycle emphasis -- SEQUENCING is declared as two distinct peer rules
(SEQUENCING-HYPO governing hypothesis placement; SEQUENCING-ORDER governing evidence-stage
relative ordering), each with its own coverage-map row, its own invocation trail, and its own
checksum contribution. Named PRE/POST tables remain (satisfying C-37/C-38). Column headers
use a generic interrogative ("Will this rule hold?") to isolate the C-42 axis.

**Hypothesis:** Decomposing SEQUENCING into two peer rules makes hypothesis placement and
evidence-ordering independently auditable. A brief can record a SEQUENCING invocation at the
hypothesis boundary while leaving the evidence-ordering boundary uninvoked -- the gap is
visible as a missing SEQUENCING-ORDER row in the audit table, not hidden behind a shared
rule identifier. The checksum shift from 40 to 47 when the second rule is added demonstrates
the extensibility property (C-29) in live action: the architecture absorbed the new peer rule
without requiring static integer updates.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

---

#### Rule Registry (all six rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every material claim names its source stage: `[web]` S1, `[intel]` S2, `[hypothesis]` S3,
`[analysis]` S4, `[synthesis]` S5. Unlabeled claim = unattributed.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary. At least two distinct levels required. Anti-uniformity guard:
uniform ratings at any applicable stage = CALIBRATION failure.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition. Final status: Supported / Refuted /
Indeterminate. "A hypothesis without a falsification condition is a belief."

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Governs hypothesis placement: evidence stages (S1, S2) must complete before hypothesis
declaration (S3). Excluded antipattern: hypothesis-first mode (stating hypotheses before or
during evidence collection). "A hypothesis anchored before evidence gathering is a bias."

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage relative ordering: the sequence in which S1 and S2 execute is a named,
governed decision. Default order: Web (S1) before Intelligence (S2). Any deviation must be
declared as a SEQUENCING-ORDER-governed decision and invoked at the stage boundary where the
ordering choice takes effect. Excluded antipattern: unordered collection (evidence stages run
in arbitrary sequence without a declared ordering rationale).

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at handoff boundary preceding each scope-restricted stage. Every claim in S3, S4,
S5 carries `[source: Stage N -- Artifact Name]`. Claim without provenance tag = structural gap.

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

**Checksum (derivable expression):** 17 positive cells × 2 phases = 34 PRE/POST pairs;
13 negative cells × 1 = 13 N/A declarations. **Total: 47 invocation artifacts.**
Prior denominator (single SEQUENCING rule) was 40. The shift to 47 is automatic: SEQUENCING-ORDER
added 2 positive cells (S1+, S2+) and 3 negative cells (S3-, S4-, S5-), contributing 7 new
artifacts without any static integer update.

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

#### Form Templates (blank -- pre-instantiated per C-38)

**FORM-PRE-S1** (fill before Stage 1 output):

| Rule | Will this rule hold? [Stage 1 of 5] |
|------|-------------------------------------|
| ATTRIBUTION | [ Yes / No ] |
| SEQUENCING-HYPO | [ Yes / No ] |
| SEQUENCING-ORDER | [ Yes / No ] -- default Web-first ordering declared |
| CALIBRATION | N/A -- evidence stage; no confidence ratings |
| FALSIFICATION | N/A -- no hypothesis declaration at this stage |
| PROVENANCE | N/A -- Stage 1 not scope-restricted |

**FORM-POST-S1** (fill after Stage 1 output):

| Rule | Does this rule hold? [Stage 1 of 5] |
|------|--------------------------------------|
| ATTRIBUTION | [ Yes / No ] |
| SEQUENCING-HYPO | [ Yes / No ] |
| SEQUENCING-ORDER | [ Yes / No ] -- Web-first ordering complied? |
| CALIBRATION | N/A confirmed |
| FALSIFICATION | N/A confirmed |
| PROVENANCE | N/A confirmed |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Rule | Will this rule hold? [Stage 2 of 5] |
|------|-------------------------------------|
| ATTRIBUTION | [ Yes / No ] |
| SEQUENCING-HYPO | [ Yes / No ] |
| SEQUENCING-ORDER | [ Yes / No ] -- S2 follows S1; ordering declared at S1 boundary |
| CALIBRATION | N/A -- evidence stage |
| FALSIFICATION | N/A -- no hypotheses |
| PROVENANCE | N/A -- not scope-restricted |

**FORM-POST-S2** (fill after Stage 2 output):

| Rule | Does this rule hold? [Stage 2 of 5] |
|------|--------------------------------------|
| ATTRIBUTION | [ Yes / No ] |
| SEQUENCING-HYPO | [ Yes / No ] |
| SEQUENCING-ORDER | [ Yes / No ] |
| CALIBRATION | N/A confirmed |
| FALSIFICATION | N/A confirmed |
| PROVENANCE | N/A confirmed |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Rule | Will this rule hold? [Stage 3 of 5] |
|------|-------------------------------------|
| ATTRIBUTION | [ Yes / No ] |
| FALSIFICATION | [ Yes / No ] |
| SEQUENCING-HYPO | [ Yes / No ] -- hypotheses declared after S1+S2 complete? |
| PROVENANCE | [ Yes / No ] -- all claims will carry provenance tags? |
| CALIBRATION | N/A -- hypothesis stage |
| SEQUENCING-ORDER | N/A -- evidence ordering governed only at S1, S2 |

**FORM-POST-S3** (fill after Stage 3 output):

| Rule | Does this rule hold? [Stage 3 of 5] |
|------|--------------------------------------|
| ATTRIBUTION | [ Yes / No ] |
| FALSIFICATION | [ Yes / No ] |
| SEQUENCING-HYPO | [ Yes / No ] |
| PROVENANCE | [ Yes / No ] |
| CALIBRATION | N/A confirmed |
| SEQUENCING-ORDER | N/A confirmed |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Rule | Will this rule hold? [Stage 4 of 5] |
|------|-------------------------------------|
| ATTRIBUTION | [ Yes / No ] |
| CALIBRATION | [ Yes / No ] -- at least two distinct confidence levels? |
| PROVENANCE | [ Yes / No ] |
| FALSIFICATION | N/A -- verdicts at S3/S5 |
| SEQUENCING-HYPO | N/A -- analysis stage |
| SEQUENCING-ORDER | N/A -- analysis stage |

**FORM-POST-S4** (fill after Stage 4 output):

| Rule | Does this rule hold? [Stage 4 of 5] |
|------|--------------------------------------|
| ATTRIBUTION | [ Yes / No ] |
| CALIBRATION | [ Yes / No ] -- distribution: __ High, __ Medium, __ Low |
| PROVENANCE | [ Yes / No ] |
| FALSIFICATION | N/A confirmed |
| SEQUENCING-HYPO | N/A confirmed |
| SEQUENCING-ORDER | N/A confirmed |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Rule | Will this rule hold? [Stage 5 of 5] |
|------|-------------------------------------|
| ATTRIBUTION | [ Yes / No ] |
| CALIBRATION | [ Yes / No ] |
| FALSIFICATION | [ Yes / No ] -- all hypothesis verdicts stated? |
| PROVENANCE | [ Yes / No ] |
| SEQUENCING-HYPO | N/A -- synthesis stage |
| SEQUENCING-ORDER | N/A -- synthesis stage |

**FORM-POST-S5** (fill after Stage 5 output):

| Rule | Does this rule hold? [Stage 5 of 5] |
|------|--------------------------------------|
| ATTRIBUTION | [ Yes / No ] |
| CALIBRATION | [ Yes / No ] -- distribution: __ High, __ Medium, __ Low |
| FALSIFICATION | [ Yes / No ] |
| PROVENANCE | [ Yes / No ] |
| SEQUENCING-HYPO | N/A confirmed |
| SEQUENCING-ORDER | N/A confirmed |

---

### Stage 1 -- Web Evidence Collector

**Entry condition:** First stage. No prior artifacts. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S1 before writing any Stage 1 output.

[Fill FORM-PRE-S1 here -- SEQUENCING-ORDER: declare Web-first ordering as governed decision]

**Stage 1 execution:** Conduct structured web research on **$ARGUMENTS**. Produce **ARTIFACT-S1: Web Findings Corpus** with 6+ findings, each labeled `[web]`. Source strength (Strong / Moderate / Weak) per finding. No hypotheses. Stage-index column: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 with 6+ `[web]` findings; no hypothesis stated.

> **Handoff S1 -> S2: Role passes to Stage 2 -- Intelligence Analyst.**
> Artifacts transferred: ARTIFACT-S1 (Web Findings Corpus).
> Authorized reads for S2: ARTIFACT-S1 only.
> **PROVENANCE RULE:** Not yet activated. Stage 2 not scope-restricted.

---

### Stage 2 -- Intelligence Analyst

**Entry condition:** S1 exit Pass. Handoff S1->S2 complete. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 before writing any Stage 2 output.

[Fill FORM-PRE-S2 here -- SEQUENCING-ORDER: S2 follows declared S1-first order]

**Stage 2 execution:** Search internal sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S2: Intelligence Assessment** with 3+ findings, each labeled `[intel]`. File-path citations; relevance (High / Medium / Low); contrasts with ARTIFACT-S1. No hypotheses. Stage-index column: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 with 3+ `[intel]` findings; no hypothesis stated.

> **Handoff S2 -> S3: Role passes to Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: ARTIFACT-S2. Prior: ARTIFACT-S1.
> Authorized reads: ARTIFACT-S1 + ARTIFACT-S2.
> **PROVENANCE RULE: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2 at this boundary.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + ARTIFACT-S2 only.

**Timing directive:** Fill FORM-PRE-S3 before writing any Stage 3 output.

[Fill FORM-PRE-S3 here -- SEQUENCING-HYPO: confirm evidence stages complete before declaration]

**Stage 3 execution:** Declare 3--5 hypotheses grounded in ARTIFACT-S1 + ARTIFACT-S2. Produce **ARTIFACT-S3: Hypothesis Register** labeled `[hypothesis]`. Each hypothesis: claim + falsification condition + initial confidence + `[source: Stage N -- Artifact Name]` tags. Rationale: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis." Stage-index: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** ARTIFACT-S3 with 3--5 falsifiable hypotheses; all provenance-tagged.

> **Handoff S3 -> S4: Role passes to Stage 4 -- Evidence Analyst.**
> Artifacts transferred: ARTIFACT-S3. Prior: ARTIFACT-S1, ARTIFACT-S2.
> **PROVENANCE RULE: REMAINS ACTIVE** for all three artifacts.

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + S2 + S3 only.

**Timing directive:** Fill FORM-PRE-S4 before writing any Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Analyze evidence and hypotheses. Produce **ARTIFACT-S4: Evidence Analysis** labeled `[analysis]`. Include: patterns from S1+S2; confidence distribution (2+ distinct levels); support/refutation signals per hypothesis; all claims carry `[source: Stage N -- Artifact Name]`. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** ARTIFACT-S4 with non-uniform confidence distribution; all provenance-tagged.

> **Handoff S4 -> S5: Role passes to Stage 5 -- Synthesis Director.**
> Artifacts transferred: ARTIFACT-S4. Prior: ARTIFACT-S1, S2, S3.
> **PROVENANCE RULE: REMAINS ACTIVE** for all four artifacts.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit Pass. All four artifacts. PROVENANCE RULE active.

**Timing directive:** Fill FORM-PRE-S5 before writing any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Synthesize all evidence. Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]`:
1. Campaign summary; 2. Consensus findings (S1+S2 agree); 3. Conflict findings (S1+S2 diverge -- name and explain);
4. Hypothesis verdicts (Supported / Refuted / Indeterminate + confidence + falsification status);
5. Confidence distribution (N High, N Medium, N Low -- anti-uniformity check required);
6. Gaps and open questions; 7. Decision readiness -- one sentence.
All claims carry `[source: Stage N -- Artifact Name]`. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

**Exit condition:** ARTIFACT-S5 with consensus/conflict synthesis, calibrated confidence, one-sentence decision verdict.

---

### Final Output

Three sections: **Evidence Brief** (ARTIFACT-S5) + **Gate Record** (filled preamble template) +
**Consolidated Invocation Audit Table** (47 rows: 34 PRE/POST pairs + 13 N/A declarations,
derived from 6 rules × 5 stages as mapped above; row count must equal checksum).

---
---

## V-03 -- Axis A (phrasing variant): Conversational rule-named interrogative column headers

**Variation axis:** Phrasing register -- rule-named interrogative column headers use expanded,
descriptive phrasing ("Will every ATTRIBUTION claim be labeled with its source stage?") rather
than terse formal phrasing ("Will ATTRIBUTION hold?"). SEQUENCING remains a single rule to
keep the axis single. Tests whether C-41 requires the rule name in terse form or whether
natural-language phrasing that names the rule still passes.

**Hypothesis:** C-41 requires that the column header "names the specific governance rule under
interrogation." Expanded phrasing that names the rule explicitly ("Will every ATTRIBUTION claim
carry a source stage label?") satisfies the naming requirement while being more self-explanatory
to a first-time reader. The column header communicates what compliance looks like, not just which
rule applies. If C-41 is strict about form (must be "Will X hold?"), this variation will fail
C-41 while still passing C-39; if C-41 requires only rule identity in the header, this passes.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

---

#### Rule Registry (all five rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every claim names its source stage via tag. `[web]` S1, `[intel]` S2, `[hypothesis]` S3,
`[analysis]` S4, `[synthesis]` S5. Unlabeled claim = ATTRIBUTION failure.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must distribute across at least two distinct levels. Uniform ratings =
CALIBRATION failure. Anti-uniformity guard active at S4 and S5.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Every hypothesis carries a stated condition whose occurrence would cause rejection. Options:
Supported / Refuted / Indeterminate. Unfalsifiable hypothesis = belief, not hypothesis.

**SEQUENCING RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Governs two dimensions: (1) evidence completion before hypothesis declaration; (2) declared
ordering among evidence stages. Principle: "A hypothesis anchored before evidence is a bias."
Excluded antipatterns: hypothesis-first mode; unordered evidence collection.

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at handoff preceding scope-restricted stage. Claims in S3, S4, S5 carry
`[source: Stage N -- Artifact Name]`. Activation is a handoff event, not a role-charter property.

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
| ATTRIBUTION   | + | + | + | + | + | 5 | 0 |
| CALIBRATION   | - | - | - | + | + | 2 | 3 |
| FALSIFICATION | - | - | + | - | + | 2 | 3 |
| SEQUENCING    | + | + | + | - | - | 3 | 2 |
| PROVENANCE    | - | - | + | + | + | 3 | 2 |
| **Total**     |   |   |   |   |   | **15** | **10** |

**Checksum:** 40 invocation artifacts (= 15 × 2 + 10 × 1). Derivable from map dimensions.

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

#### Form Templates (blank -- pre-instantiated; fill at stages following timing directives)

**FORM-PRE-S1** (fill before Stage 1 output):

| Will every ATTRIBUTION claim be labeled with its source stage? [Stage 1 of 5] | Will SEQUENCING be honored -- no hypotheses before evidence? [Stage 1 of 5] |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [ Yes / No ] | [ Yes / No ] |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage); FALSIFICATION -- N/A (no hypotheses); PROVENANCE -- N/A (not scope-restricted).

**FORM-POST-S1** (fill after Stage 1 output):

| Was every ATTRIBUTION claim labeled with its source stage? [Stage 1 of 5] | Was SEQUENCING honored -- no hypothesis appeared in Stage 1? [Stage 1 of 5] |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [ Yes / No ] | [ Yes / No ] |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will every ATTRIBUTION claim be labeled with its source stage? [Stage 2 of 5] | Will SEQUENCING be honored -- no hypotheses before evidence? [Stage 2 of 5] |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [ Yes / No ] | [ Yes / No ] |

N/A [Stage 2 of 5]: CALIBRATION -- N/A; FALSIFICATION -- N/A; PROVENANCE -- N/A.

**FORM-POST-S2** (fill after Stage 2 output):

| Was every ATTRIBUTION claim labeled with its source stage? [Stage 2 of 5] | Was SEQUENCING honored -- no hypothesis appeared? [Stage 2 of 5] |
|---------------------------------------------------------------------------|------------------------------------------------------------------|
| [ Yes / No ] | [ Yes / No ] |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will every ATTRIBUTION claim be labeled? [Stage 3 of 5] | Will FALSIFICATION conditions be stated for every hypothesis? [Stage 3 of 5] | Will SEQUENCING be honored -- hypotheses declared only after S1+S2? [Stage 3 of 5] | Will every PROVENANCE claim cite its source artifact? [Stage 3 of 5] |
|----------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

N/A [Stage 3 of 5]: CALIBRATION -- N/A (hypothesis stage).

**FORM-POST-S3** (fill after Stage 3 output):

| Was every ATTRIBUTION claim labeled? [Stage 3 of 5] | Did every hypothesis carry a FALSIFICATION condition? [Stage 3 of 5] | Was SEQUENCING honored -- hypotheses declared post-evidence? [Stage 3 of 5] | Did every PROVENANCE claim cite its source artifact? [Stage 3 of 5] |
|------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will every ATTRIBUTION claim be labeled? [Stage 4 of 5] | Will CALIBRATION ratings show 2+ distinct levels? [Stage 4 of 5] | Will every PROVENANCE claim cite its source artifact? [Stage 4 of 5] |
|----------------------------------------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A; SEQUENCING -- N/A.

**FORM-POST-S4** (fill after Stage 4 output):

| Was every ATTRIBUTION claim labeled? [Stage 4 of 5] | Did CALIBRATION ratings show 2+ distinct levels? [Stage 4 of 5] | Did every PROVENANCE claim cite its source artifact? [Stage 4 of 5] |
|------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- distribution: __ High, __ Medium, __ Low | [ Yes / No ] |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will every ATTRIBUTION claim be labeled? [Stage 5 of 5] | Will CALIBRATION ratings show 2+ distinct levels? [Stage 5 of 5] | Will every FALSIFICATION verdict be stated? [Stage 5 of 5] | Will every PROVENANCE claim cite its source artifact? [Stage 5 of 5] |
|----------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

N/A [Stage 5 of 5]: SEQUENCING -- N/A (synthesis stage).

**FORM-POST-S5** (fill after Stage 5 output):

| Was every ATTRIBUTION claim labeled? [Stage 5 of 5] | Did CALIBRATION ratings show 2+ distinct levels? [Stage 5 of 5] | Was every FALSIFICATION verdict stated? [Stage 5 of 5] | Did every PROVENANCE claim cite its source artifact? [Stage 5 of 5] |
|------------------------------------------------------|------------------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- distribution: __ High, __ Medium, __ Low | [ Yes / No ] | [ Yes / No ] |

---

### Stage 1 -- Web Evidence Collector

**Entry condition:** First stage. No prior artifacts. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S1 before any Stage 1 output.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Web research on **$ARGUMENTS**. Produce **ARTIFACT-S1: Web Findings Corpus** with 6+ findings, each labeled `[web]`. Source strength per finding. No hypotheses. Stage-index: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 with 6+ labeled findings; no hypothesis.

> **Handoff S1 -> S2:** Role passes to Stage 2 -- Intelligence Analyst.
> Artifacts: ARTIFACT-S1. Authorized reads for S2: ARTIFACT-S1 only.
> **PROVENANCE RULE:** Not yet activated.

---

### Stage 2 -- Intelligence Analyst

**Entry condition:** S1 exit Pass. Handoff complete. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 before any Stage 2 output.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Internal source search on **$ARGUMENTS**. Produce **ARTIFACT-S2: Intelligence Assessment** with 3+ findings labeled `[intel]`, file-path citations, relevance ratings. No hypotheses. Stage-index: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 with 3+ labeled findings; no hypothesis.

> **Handoff S2 -> S3:** Role passes to Stage 3 -- Hypothesis Architect.
> Artifacts: ARTIFACT-S2 (+ prior ARTIFACT-S1). Authorized reads: ARTIFACT-S1 + ARTIFACT-S2.
> **PROVENANCE RULE: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2 at this boundary.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit Pass. PROVENANCE active. Access: ARTIFACT-S1 + S2 only.

**Timing directive:** Fill FORM-PRE-S3 before any Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare 3--5 hypotheses from ARTIFACT-S1+S2. Produce **ARTIFACT-S3: Hypothesis Register** labeled `[hypothesis]`. Each: claim + falsification condition + confidence + provenance tags. Rationale: "A hypothesis anchored before evidence is a bias." Stage-index: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** ARTIFACT-S3 with 3--5 falsifiable hypotheses; all provenance-tagged.

> **Handoff S3 -> S4:** Role passes to Stage 4 -- Evidence Analyst.
> Artifacts: ARTIFACT-S3 (+ prior S1, S2). **PROVENANCE RULE: REMAINS ACTIVE.**

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit Pass. PROVENANCE active. Access: ARTIFACT-S1 + S2 + S3.

**Timing directive:** Fill FORM-PRE-S4 before any Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Analyze evidence and hypotheses. Produce **ARTIFACT-S4: Evidence Analysis** labeled `[analysis]`. Patterns from S1+S2; calibrated confidence (2+ levels); hypothesis support signals; all provenance-tagged. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** ARTIFACT-S4 with non-uniform confidence; all provenance-tagged.

> **Handoff S4 -> S5:** Role passes to Stage 5 -- Synthesis Director.
> Artifacts: ARTIFACT-S4 (+ prior S1, S2, S3). **PROVENANCE RULE: REMAINS ACTIVE.**

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit Pass. All four artifacts. PROVENANCE active.

**Timing directive:** Fill FORM-PRE-S5 before any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]`:
1. Campaign summary; 2. Consensus (S1+S2 agree); 3. Conflict (S1+S2 diverge -- name + explain);
4. Hypothesis verdicts; 5. Confidence distribution (anti-uniformity check required);
6. Gaps; 7. Decision readiness sentence. All claims carry `[source: Stage N -- Artifact Name]`. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

**Exit condition:** ARTIFACT-S5 complete; one-sentence decision verdict; calibrated confidence.

---

### Final Output

**Evidence Brief** + **Gate Record** + **Consolidated Invocation Audit Table** (40 rows,
derived from 5 rules × 5 stages as mapped; row count must equal checksum of 40).

---
---

## V-04 -- Combined: Role sequence reversal + C-41 + C-42

**Variation axis:** Role sequence + C-41 + C-42 combined. Evidence stages run in reversed order:
Stage 1 = Intelligence Analyst (internal sources first), Stage 2 = Web Evidence Collector
(external sources second). SEQUENCING-ORDER is invoked at the S1 boundary to declare the
Intel-first ordering as a named, governed decision. SEQUENCING-HYPO governs hypothesis
placement. Column headers are rule-named interrogatives (C-41). Six rules, checksum 47.

**Hypothesis:** Combining role-sequence reversal with SEQUENCING-ORDER decomposition demonstrates
C-42 in live action: the rule is invoked at a real ordering boundary (Intel before Web) rather
than stated only in the preamble. SEQUENCING-ORDER's PRE invocation at Stage 1 must answer
"Yes -- Intel-first ordering declared as governed decision." Any SEQUENCING-ORDER invocation
at Stage 2 must confirm compliance with the Stage 1 declaration. The reversal makes the
evidence-ordering constraint actively tested rather than trivially satisfied by convention.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

**Note on stage ordering:** This campaign runs Intelligence (S1) before Web (S2). This ordering
is governed by SEQUENCING-ORDER RULE and is declared as a named decision at Stage 1. Both
stages complete before hypothesis declaration (S3) as governed by SEQUENCING-HYPO RULE.

---

#### Rule Registry (all six rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every claim names its source stage: `[intel]` S1, `[web]` S2, `[hypothesis]` S3,
`[analysis]` S4, `[synthesis]` S5. Unlabeled claim = ATTRIBUTION failure.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary across at least two distinct levels. Anti-uniformity guard at S4, S5.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition. Options: Supported / Refuted /
Indeterminate. Unfalsifiable claim = belief.

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence stages (S1 Intelligence, S2 Web) complete before hypothesis declaration (S3).
Excluded antipattern: hypothesis-first mode. "A hypothesis anchored before evidence is a bias."

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs the relative ordering of evidence stages. This campaign declares: **Intel-first ordering**
(S1 = Intelligence, S2 = Web). This reversal from the default Web-first convention is a named,
governed decision invoked at the S1 boundary. SEQUENCING-ORDER must be invoked at S1 to declare
the ordering and at S2 to confirm compliance. Excluded antipattern: unordered evidence collection.

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at handoff to S3. Every claim in S3, S4, S5 carries `[source: Stage N -- Artifact Name]`.

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

**Checksum:** 47 invocation artifacts (= 17 × 2 + 13 × 1). Derived from map; no static integers.

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

#### Form Templates (blank -- pre-instantiated per C-38)

**FORM-PRE-S1** (fill before Stage 1 output -- declare Intel-first ordering):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] -- Intel-first declared as governed decision |

N/A [Stage 1 of 5]: CALIBRATION -- N/A; FALSIFICATION -- N/A; PROVENANCE -- N/A.

**FORM-POST-S1** (fill after Stage 1 output):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] -- Intel-first ordering complied? |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] -- S2 Web follows declared S1 Intel order |

N/A [Stage 2 of 5]: CALIBRATION -- N/A; FALSIFICATION -- N/A; PROVENANCE -- N/A.

**FORM-POST-S2** (fill after Stage 2 output):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

N/A [Stage 3 of 5]: CALIBRATION -- N/A; SEQUENCING-ORDER -- N/A (governs only S1/S2 ordering).

**FORM-POST-S3** (fill after Stage 3 output):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A; SEQUENCING-HYPO -- N/A; SEQUENCING-ORDER -- N/A.

**FORM-POST-S4** (fill after Stage 4 output):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- distribution: __ High, __ Medium, __ Low | [ Yes / No ] |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A; SEQUENCING-ORDER -- N/A.

**FORM-POST-S5** (fill after Stage 5 output):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- distribution: __ High, __ Medium, __ Low | [ Yes / No ] | [ Yes / No ] |

---

### Stage 1 -- Intelligence Analyst (Intel-first; SEQUENCING-ORDER declared here)

**Entry condition:** First stage. No prior artifacts. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S1 before any Stage 1 output. Declare Intel-first ordering in SEQUENCING-ORDER cell.

[Fill FORM-PRE-S1 here -- SEQUENCING-ORDER PRE: "Intel-first ordering declared as SEQUENCING-ORDER-governed decision at Stage 1 boundary. [ Yes ]"]

**Stage 1 execution:** Search internal sources (codebase, specs, prior analyses) on **$ARGUMENTS**. Produce **ARTIFACT-S1: Intelligence Assessment** with 3+ findings, each labeled `[intel]`. File-path citations; relevance (High / Medium / Low). No hypotheses. Stage-index: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 with 3+ `[intel]` findings; no hypothesis.

> **Handoff S1 -> S2:** Role passes to Stage 2 -- Web Evidence Collector.
> Artifacts: ARTIFACT-S1 (Intelligence Assessment).
> Authorized reads for S2: ARTIFACT-S1 only.
> **SEQUENCING-ORDER:** S2 Web follows declared Intel-first order.
> **PROVENANCE RULE:** Not yet activated.

---

### Stage 2 -- Web Evidence Collector

**Entry condition:** S1 exit Pass. Handoff complete. Intel-first ordering in effect.

**Timing directive:** Fill FORM-PRE-S2 before any Stage 2 output.

[Fill FORM-PRE-S2 here -- SEQUENCING-ORDER PRE: "S2 Web follows S1 Intel per declared ordering. [ Yes ]"]

**Stage 2 execution:** Conduct web research on **$ARGUMENTS**. Produce **ARTIFACT-S2: Web Findings Corpus** with 6+ findings, each labeled `[web]`. Source strength per finding. No hypotheses. Stage-index: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 with 6+ `[web]` findings; no hypothesis.

> **Handoff S2 -> S3:** Role passes to Stage 3 -- Hypothesis Architect.
> Artifacts: ARTIFACT-S2 (Web Findings Corpus). Prior: ARTIFACT-S1.
> Authorized reads: ARTIFACT-S1 + ARTIFACT-S2.
> **PROVENANCE RULE: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit Pass. PROVENANCE active. Access: ARTIFACT-S1 + S2 only.

**Timing directive:** Fill FORM-PRE-S3 before any Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare 3--5 hypotheses grounded in ARTIFACT-S1 (intel) + ARTIFACT-S2 (web). Produce **ARTIFACT-S3: Hypothesis Register** labeled `[hypothesis]`. Each: claim + falsification condition + confidence + `[source: Stage N -- Artifact Name]`. Rationale for post-evidence declaration stated. Stage-index: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** ARTIFACT-S3 with 3--5 falsifiable hypotheses; all provenance-tagged.

> **Handoff S3 -> S4:** Role passes to Stage 4 -- Evidence Analyst.
> Artifacts: ARTIFACT-S3. Prior: ARTIFACT-S1, S2. **PROVENANCE RULE: REMAINS ACTIVE.**

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit Pass. PROVENANCE active. Access: ARTIFACT-S1 + S2 + S3.

**Timing directive:** Fill FORM-PRE-S4 before any Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Analyze evidence and hypotheses. Produce **ARTIFACT-S4: Evidence Analysis** labeled `[analysis]`. Patterns; calibrated confidence (2+ levels); hypothesis signals. All provenance-tagged. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** ARTIFACT-S4 with non-uniform confidence; all provenance-tagged.

> **Handoff S4 -> S5:** Role passes to Stage 5 -- Synthesis Director.
> All four artifacts. **PROVENANCE RULE: REMAINS ACTIVE.**

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit Pass. All four artifacts. PROVENANCE active.

**Timing directive:** Fill FORM-PRE-S5 before any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]`:
1. Campaign summary (note Intel-first ordering); 2. Consensus (S1+S2 agree); 3. Conflict (S1+S2 diverge);
4. Hypothesis verdicts; 5. Confidence distribution (anti-uniformity check);
6. Gaps; 7. Decision readiness -- one sentence. All provenance-tagged. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

**Exit condition:** ARTIFACT-S5 complete.

---

### Final Output

**Evidence Brief** + **Gate Record** + **Consolidated Invocation Audit Table** (47 rows, derived
from 6-rule × 5-stage coverage map above; row count must equal checksum of 47).

---
---

## V-05 -- Combined: Inertia framing + C-41 + C-42

**Variation axis:** Inertia framing + C-41 + C-42 combined. The preamble opens with an explicit
"Inertia Baseline" section naming what an unstructured investigation looks like and why it fails.
Each rule declaration names its specific excluded antipatterns. SEQUENCING-HYPO excludes
"hypothesis-first mode"; SEQUENCING-ORDER excludes "unordered collection." Column headers
are rule-named interrogatives (C-41). Six rules, checksum 47.

**Hypothesis:** Naming excluded antipatterns within each rule declaration converts C-42 compliance
from a positive assertion ("evidence ordering is governed") to a two-sided declaration with
named failure modes ("evidence ordering is governed; violations are classified as unordered-
collection"). Decision-readiness verdicts can reference antipattern names directly: "No
hypothesis-first mode detected; no unordered collection present." The inertia baseline section
makes the improvement from unstructured to governed campaign explicit and provides a reference
for a first-time reader to understand what is being prevented.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. **Immutable -- cannot be modified after any stage executes.**

---

#### Inertia Baseline: What This Campaign Replaces

An unstructured investigation has three characteristic failure modes:

| Failure Mode | What It Looks Like | Rule That Prevents It |
|-------------|--------------------|-----------------------|
| **Hypothesis-first mode** | Researcher states beliefs before collecting evidence; evidence search is confirmatory, not exploratory | SEQUENCING-HYPO RULE |
| **Unordered collection** | Evidence stages run in arbitrary sequence; ordering decisions are implicit and unauditable | SEQUENCING-ORDER RULE |
| **Uniform confidence** | All findings rated "Medium" or all rated "High"; no calibration against actual evidence strength | CALIBRATION RULE |
| **Attribution collapse** | Claims cite "the evidence" without naming which stage or source produced them | ATTRIBUTION RULE |
| **Unconstrained synthesis** | Synthesis draws on pre-campaign assumptions not present in any evidence artifact | PROVENANCE RULE |
| **Unfalsifiable hypothesis** | Hypothesis has no stated rejection criterion; no finding could ever disprove it | FALSIFICATION RULE |

This campaign governs all six failure modes via the six rules below.

---

#### Rule Registry (all six rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every claim names its source stage: `[web]` S1, `[intel]` S2, `[hypothesis]` S3, `[analysis]` S4,
`[synthesis]` S5. Unlabeled claim = ATTRIBUTION failure. Excluded antipattern: **attribution collapse**.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary across at least two distinct levels. Anti-uniformity guard: uniform
ratings at any applicable stage = failure. Excluded antipattern: **uniform confidence**.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries a stated rejection criterion. Options: Supported / Refuted / Indeterminate.
Excluded antipattern: **unfalsifiable hypothesis** ("a hypothesis without a falsification condition
is a belief").

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence stages (S1, S2) complete before hypothesis declaration (S3). The ordering decision that
hypotheses follow evidence is a named, governed constraint invokable by identifier.
Excluded antipattern: **hypothesis-first mode** (stating hypotheses before or during evidence
collection; the antipattern is visible in SEQUENCING-HYPO invocation records as an S3 PRE
check answered before S1/S2 exits are confirmed).

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs the relative ordering of evidence stages. The sequence in which S1 and S2 execute must
be declared as a named, governed decision at Stage 1. Default: Web (S1) before Intelligence (S2).
Any reversal is permitted but must be declared at Stage 1's SEQUENCING-ORDER PRE invocation.
Excluded antipattern: **unordered collection** (evidence stages run without a declared ordering
rationale; their sequence is structural convention, not a named governance decision).

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at the handoff boundary preceding each scope-restricted stage. Every claim in S3, S4,
S5 carries `[source: Stage N -- Artifact Name]`. Excluded antipattern: **unconstrained synthesis**
(synthesis draws on assumptions not present in any named evidence artifact).

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

**Checksum (derivable):** 17 × 2 + 13 × 1 = **47 invocation artifacts**.
Prior single-SEQUENCING-rule campaigns had checksum 40. The shift to 47 reflects SEQUENCING-ORDER
adding 2 positive cells (S1+, S2+) and 3 negative cells (S3-, S4-, S5-) -- 7 new artifacts --
absorbed automatically without any static integer update, demonstrating C-29 extensibility.

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

#### Form Templates (blank -- pre-instantiated per C-38)

**FORM-PRE-S1** (fill before Stage 1 output -- declare evidence-stage ordering):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- no hypothesis-first mode | [ Yes / No ] -- ordering declared: _______ |

N/A [Stage 1 of 5]: CALIBRATION -- N/A (evidence stage); FALSIFICATION -- N/A (no hypotheses); PROVENANCE -- N/A (not scope-restricted).

**FORM-POST-S1** (fill after Stage 1 output):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- no hypothesis-first mode detected | [ Yes / No ] -- ordering complied with declaration? |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- no hypothesis-first mode | [ Yes / No ] -- S2 follows declared ordering? |

N/A [Stage 2 of 5]: CALIBRATION -- N/A; FALSIFICATION -- N/A; PROVENANCE -- N/A.

**FORM-POST-S2** (fill after Stage 2 output):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] | [ Yes / No ] | [ Yes / No ] |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- no unfalsifiable hypotheses | [ Yes / No ] -- hypotheses declared only after S1+S2 complete? | [ Yes / No ] -- no unconstrained synthesis |

N/A [Stage 3 of 5]: CALIBRATION -- N/A; SEQUENCING-ORDER -- N/A.

**FORM-POST-S3** (fill after Stage 3 output):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- all hypotheses falsifiable? | [ Yes / No ] -- hypothesis-first mode absent? | [ Yes / No ] -- unconstrained synthesis absent? |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- no uniform confidence | [ Yes / No ] -- no unconstrained synthesis |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A; SEQUENCING-HYPO -- N/A; SEQUENCING-ORDER -- N/A.

**FORM-POST-S4** (fill after Stage 4 output):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- distribution: __ High, __ Medium, __ Low; uniform-confidence antipattern absent? | [ Yes / No ] |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- no uniform-confidence antipattern | [ Yes / No ] -- all verdicts stated; no unfalsifiable claims | [ Yes / No ] -- no unconstrained synthesis |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A; SEQUENCING-ORDER -- N/A.

**FORM-POST-S5** (fill after Stage 5 output):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] | [ Yes / No ] -- distribution: __ High, __ Medium, __ Low; uniform-confidence antipattern absent? | [ Yes / No ] -- unfalsifiable-hypothesis antipattern absent? | [ Yes / No ] -- unconstrained-synthesis antipattern absent? |

---

### Stage 1 -- Web Evidence Collector

**Entry condition:** First stage. No prior artifacts. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S1 before any Stage 1 output. Declare evidence-stage ordering in SEQUENCING-ORDER cell (default: Web-first; declare any reversal here).

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Conduct structured web research on **$ARGUMENTS**. Produce **ARTIFACT-S1: Web Findings Corpus** with 6+ findings, each labeled `[web]`. Source strength (Strong / Moderate / Weak) per finding. No hypotheses. Inertia guard: if any hypothesis appears in Stage 1 output, SEQUENCING-HYPO fails -- hypothesis-first mode detected. Stage-index: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1 with 6+ `[web]` findings; no hypothesis-first mode detected.

> **Handoff S1 -> S2:** Role passes to Stage 2 -- Intelligence Analyst.
> Artifacts transferred: ARTIFACT-S1 (Web Findings Corpus).
> Authorized reads for S2: ARTIFACT-S1 only.
> SEQUENCING-ORDER: S2 follows declared ordering from S1 FORM-PRE.
> **PROVENANCE RULE:** Not yet activated.

---

### Stage 2 -- Intelligence Analyst

**Entry condition:** S1 exit Pass. Handoff complete. Declared ordering in effect.

**Timing directive:** Fill FORM-PRE-S2 before any Stage 2 output.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search internal sources on **$ARGUMENTS**. Produce **ARTIFACT-S2: Intelligence Assessment** with 3+ findings, each labeled `[intel]`. File-path citations; relevance ratings. No hypotheses. Inertia guard: unordered-collection antipattern is absent if this stage follows declared ordering. Stage-index: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 with 3+ `[intel]` findings; no hypothesis; ordering complied.

> **Handoff S2 -> S3:** Role passes to Stage 3 -- Hypothesis Architect.
> Artifacts: ARTIFACT-S2 (+ ARTIFACT-S1).
> Authorized reads: ARTIFACT-S1 + ARTIFACT-S2.
> **PROVENANCE RULE: ACTIVATED** for ARTIFACT-S1 and ARTIFACT-S2.
> Provenance activation prevents unconstrained-synthesis antipattern at S3.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit Pass. PROVENANCE active. Access: ARTIFACT-S1 + S2 only.

**Timing directive:** Fill FORM-PRE-S3 before any Stage 3 output.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare 3--5 hypotheses grounded in ARTIFACT-S1 + ARTIFACT-S2. Produce **ARTIFACT-S3: Hypothesis Register** labeled `[hypothesis]`. Each: claim + falsification condition + confidence + `[source: Stage N -- Artifact Name]`. Principle: "A hypothesis anchored before evidence is a bias, not a hypothesis." Inertia guard: hypothesis-first-mode antipattern is absent when all hypotheses are declared here (S3), after S1 and S2 exits are confirmed. Stage-index: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** ARTIFACT-S3 with 3--5 falsifiable hypotheses; hypothesis-first mode absent; all provenance-tagged.

> **Handoff S3 -> S4:** Role passes to Stage 4 -- Evidence Analyst.
> Artifacts: ARTIFACT-S3 (+ S1, S2). **PROVENANCE RULE: REMAINS ACTIVE.**

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit Pass. PROVENANCE active. Access: ARTIFACT-S1 + S2 + S3.

**Timing directive:** Fill FORM-PRE-S4 before any Stage 4 output.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Analyze evidence and hypotheses. Produce **ARTIFACT-S4: Evidence Analysis** labeled `[analysis]`. Patterns from S1+S2; confidence distribution (2+ levels -- uniform-confidence antipattern check required); hypothesis support signals; all provenance-tagged. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** ARTIFACT-S4 with non-uniform confidence (uniform-confidence antipattern absent); all provenance-tagged.

> **Handoff S4 -> S5:** Role passes to Stage 5 -- Synthesis Director.
> All four artifacts. **PROVENANCE RULE: REMAINS ACTIVE.**
> Unconstrained-synthesis antipattern is prevented at S5 by PROVENANCE activation.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit Pass. All four artifacts. PROVENANCE active.

**Timing directive:** Fill FORM-PRE-S5 before any Stage 5 output.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]`:
1. **Campaign summary** -- topic, 5 stages, evidence-stage ordering declared at S1.
2. **Consensus findings** -- where S1+S2 agree; cite both artifacts.
3. **Conflict findings** -- where S1+S2 diverge; name the divergence and significance.
4. **Hypothesis verdicts** -- Supported / Refuted / Indeterminate + confidence + falsification status.
5. **Confidence distribution** -- N High, N Medium, N Low. Anti-uniformity check: if all same level, uniform-confidence antipattern detected -- recalibrate before proceeding.
6. **Gaps and open questions** -- what remains unknown after the full campaign.
7. **Antipattern absence confirmation** -- one line per antipattern: "Hypothesis-first mode: absent. Unordered collection: absent. Uniform confidence: absent. Attribution collapse: absent. Unconstrained synthesis: absent. Unfalsifiable hypothesis: absent."
8. **Decision readiness** -- one sentence: "Ready to proceed" OR "Needs more investigation on [specific gap] before committing."

All claims carry `[source: Stage N -- Artifact Name]`. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

**Exit condition:** ARTIFACT-S5 complete; antipattern-absence section included; one-sentence decision verdict.

---

### Final Output

Three sections:

**Section 1 -- Evidence Brief** (ARTIFACT-S5 in full; self-contained)

**Section 2 -- Gate Record** (filled from preamble template)

**Section 3 -- Consolidated Invocation Audit Table** (47 rows, derived from 6-rule × 5-stage
coverage map; includes antipattern-reference column):

| Rule | Stage | Phase | Form ID | Result | Antipattern Guarded |
|------|-------|-------|---------|--------|---------------------|
| ATTRIBUTION | S1 | PRE | FORM-PRE-S1 | | attribution collapse |
| ATTRIBUTION | S1 | POST | FORM-POST-S1 | | attribution collapse |
| SEQUENCING-HYPO | S1 | PRE | FORM-PRE-S1 | | hypothesis-first mode |
| SEQUENCING-HYPO | S1 | POST | FORM-POST-S1 | | hypothesis-first mode |
| SEQUENCING-ORDER | S1 | PRE | FORM-PRE-S1 | | unordered collection |
| SEQUENCING-ORDER | S1 | POST | FORM-POST-S1 | | unordered collection |
| CALIBRATION | S1 | N/A | FORM-PRE-S1 | N/A | uniform confidence |
| FALSIFICATION | S1 | N/A | FORM-PRE-S1 | N/A | unfalsifiable hypothesis |
| PROVENANCE | S1 | N/A | FORM-PRE-S1 | N/A | unconstrained synthesis |
| *(continue for S2 through S5 -- 47 rows total)* | | | | | |

Row count must equal **47**. Any mismatch indicates a missing invocation artifact.
