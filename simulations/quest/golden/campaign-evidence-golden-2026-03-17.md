---
skill: quest-golden
skill_target: campaign-evidence
date: 2026-03-17
rounds: 20
rubric_final: campaign-evidence-rubric-v21-2026-03-17.md
score: 100.75
status: GOLDEN
---

# Golden Prompt -- campaign-evidence

**Source:** Round 20, V-05 (QU5-simplified)
**Score:** 100.75 / 100.75 (Essential 60 + Recommended 30 + Aspirational 10.75)
**Word count:** 2452 (simplified from 3070; 20.1% reduction)

---

## Prompt Body

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

**HOMOGENEITY INVARIANT (C-50):** All cell tiers (PRE binary, POST binary, N/A) cite IB-IDs uniformly. Binary cells: `[ Yes / No ] -- [IB-XXX]` (typed-ID-only, no English name). N/A cells: `-- N/A [IB-XXX] (reason)`. Any cell lacking `[IB-XXX]` is a homogeneity violation detectable by identifier-syntax scan.

---

#### Rule Registry

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each stage]`
Every material claim names its source stage: `[intel]` S1, `[web]` S2, `[hypothesis]` S3, `[analysis]` S4, `[synthesis]` S5. An unlabeled claim fails ATTRIBUTION.
Excluded antipattern: **attribution collapse** [IB-ATTR].

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); PRE and POST at S4, S5]`
Confidence ratings must vary (2+ distinct levels). State distribution explicitly at S4 and S5.
Excluded antipattern: **uniform confidence** [IB-CAL].

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); PRE and POST at S3, S5]`
Each hypothesis carries an explicit falsification condition. Final status: Supported / Refuted / Indeterminate.
Excluded antipattern: **unfalsifiable hypothesis** [IB-FALS].

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); PRE and POST at S1, S2, S3]`
Evidence stages (S1, S2) complete before hypothesis declaration (S3).
Excluded antipattern: **hypothesis-first mode** [IB-SEQ-H].

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+), S3(-), S4(-), S5(-); PRE and POST at S1, S2]`
Governs evidence-stage ordering. **This campaign: Intel-first (S1 = Intelligence, S2 = Web); named and governed at S1 PRE via `[IB-SEQ-O]`.**
Excluded antipattern: **unordered collection** [IB-SEQ-O].

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); PRE and POST at S3, S4, S5]`
Activated at handoff boundary preceding scope-restricted stage. Claims in S3, S4, S5 carry `[source: Stage N -- Artifact Name]`.
Excluded antipattern: **unconstrained synthesis** [IB-PROV].

---

#### Role Roster

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Intelligence Analyst | Internal sources only. No prior artifacts. |
| S2 | Web Evidence Collector | ARTIFACT-S1 (Intelligence Assessment) only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Web Findings Corpus) only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 (Hypothesis Register) only. |
| S5 | Synthesis Director | All four prior artifacts. |

---

#### Coverage Map (immutable)

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|-----|----------|----------|
| ATTRIBUTION      | + | + | + | + | + | 5 | 0 |
| CALIBRATION      | - | - | - | + | + | 2 | 3 |
| FALSIFICATION    | - | - | + | - | + | 2 | 3 |
| SEQUENCING-HYPO  | + | + | + | - | - | 3 | 2 |
| SEQUENCING-ORDER | + | + | - | - | - | 2 | 3 |
| PROVENANCE       | - | - | + | + | + | 3 | 2 |
| **Total**        |   |   |   |   |   | **17** | **13** |

**Checksum:** 17 positive x 2 PRE/POST + 13 negative x 1 N/A = **47 invocation artifacts.** Derived from map dimensions; updates automatically when rules or stages are added.

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

#### Form Templates (HOMOGENEITY INVARIANT enforced across all tiers)

**Cell format contracts:**
- **(C-48) Binary cells:** `[IB-XXX]` typed-ID-only annotation. No English name in cell body.
- **(C-50) N/A cells:** `-- N/A [IB-XXX] (reason)`. IB-ID required in every N/A declaration.

**FORM-PRE-S1** (fill before Stage 1 output -- declare Intel-first as governed SEQUENCING-ORDER decision):

| Will ATTRIBUTION hold? [Stage 1 of 5] | Will SEQUENCING-HYPO hold? [Stage 1 of 5] | Will SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] | [ Yes / No ] -- [IB-SEQ-H] | [ Yes / No ] -- [IB-SEQ-O]; Intel-first ordered as governed decision |

N/A [Stage 1 of 5]: CALIBRATION -- N/A [IB-CAL] (evidence stage). FALSIFICATION -- N/A [IB-FALS] (no hypotheses). PROVENANCE -- N/A [IB-PROV] (not scope-restricted).

**FORM-POST-S1** (fill after Stage 1 output):

| Does ATTRIBUTION hold? [Stage 1 of 5] | Does SEQUENCING-HYPO hold? [Stage 1 of 5] | Does SEQUENCING-ORDER hold? [Stage 1 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] | [ Yes / No ] -- [IB-SEQ-H] | [ Yes / No ] -- [IB-SEQ-O]; Intel-first executed as governed decision |

---

**FORM-PRE-S2** (fill before Stage 2 output):

| Will ATTRIBUTION hold? [Stage 2 of 5] | Will SEQUENCING-HYPO hold? [Stage 2 of 5] | Will SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] | [ Yes / No ] -- [IB-SEQ-H] | [ Yes / No ] -- [IB-SEQ-O]; S2 Web follows Intel-first governed order |

N/A [Stage 2 of 5]: CALIBRATION -- N/A [IB-CAL] (evidence stage). FALSIFICATION -- N/A [IB-FALS] (no hypotheses). PROVENANCE -- N/A [IB-PROV] (not scope-restricted).

**FORM-POST-S2** (fill after Stage 2 output):

| Does ATTRIBUTION hold? [Stage 2 of 5] | Does SEQUENCING-HYPO hold? [Stage 2 of 5] | Does SEQUENCING-ORDER hold? [Stage 2 of 5] |
|---------------------------------------|------------------------------------------|-------------------------------------------|
| [ Yes / No ] -- [IB-ATTR] | [ Yes / No ] -- [IB-SEQ-H] | [ Yes / No ] -- [IB-SEQ-O]; Intel-first ordering confirmed at S2 |

---

**FORM-PRE-S3** (fill before Stage 3 output):

| Will ATTRIBUTION hold? [Stage 3 of 5] | Will FALSIFICATION hold? [Stage 3 of 5] | Will SEQUENCING-HYPO hold? [Stage 3 of 5] | Will PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] | [ Yes / No ] -- [IB-FALS] | [ Yes / No ] -- [IB-SEQ-H] | [ Yes / No ] -- [IB-PROV] |

N/A [Stage 3 of 5]: CALIBRATION -- N/A [IB-CAL] (hypothesis stage). SEQUENCING-ORDER -- N/A [IB-SEQ-O] (governs S1, S2 only).

**FORM-POST-S3** (fill after Stage 3 output):

| Does ATTRIBUTION hold? [Stage 3 of 5] | Does FALSIFICATION hold? [Stage 3 of 5] | Does SEQUENCING-HYPO hold? [Stage 3 of 5] | Does PROVENANCE hold? [Stage 3 of 5] |
|---------------------------------------|----------------------------------------|------------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] | [ Yes / No ] -- [IB-FALS] | [ Yes / No ] -- [IB-SEQ-H] | [ Yes / No ] -- [IB-PROV] |

---

**FORM-PRE-S4** (fill before Stage 4 output):

| Will ATTRIBUTION hold? [Stage 4 of 5] | Will CALIBRATION hold? [Stage 4 of 5] | Will PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] | [ Yes / No ] -- [IB-CAL]; 2+ distinct confidence levels required | [ Yes / No ] -- [IB-PROV] |

N/A [Stage 4 of 5]: FALSIFICATION -- N/A [IB-FALS] (verdicts at S3/S5). SEQUENCING-HYPO -- N/A [IB-SEQ-H] (analysis stage). SEQUENCING-ORDER -- N/A [IB-SEQ-O] (analysis stage).

**FORM-POST-S4** (fill after Stage 4 output):

| Does ATTRIBUTION hold? [Stage 4 of 5] | Does CALIBRATION hold? [Stage 4 of 5] | Does PROVENANCE hold? [Stage 4 of 5] |
|---------------------------------------|---------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] | [ Yes / No ] -- [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- [IB-PROV] |

---

**FORM-PRE-S5** (fill before Stage 5 output):

| Will ATTRIBUTION hold? [Stage 5 of 5] | Will CALIBRATION hold? [Stage 5 of 5] | Will FALSIFICATION hold? [Stage 5 of 5] | Will PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] | [ Yes / No ] -- [IB-CAL] | [ Yes / No ] -- [IB-FALS]; all verdicts stated? | [ Yes / No ] -- [IB-PROV] |

N/A [Stage 5 of 5]: SEQUENCING-HYPO -- N/A [IB-SEQ-H] (synthesis stage). SEQUENCING-ORDER -- N/A [IB-SEQ-O] (synthesis stage).

**FORM-POST-S5** (fill after Stage 5 output):

| Does ATTRIBUTION hold? [Stage 5 of 5] | Does CALIBRATION hold? [Stage 5 of 5] | Does FALSIFICATION hold? [Stage 5 of 5] | Does PROVENANCE hold? [Stage 5 of 5] |
|---------------------------------------|---------------------------------------|----------------------------------------|--------------------------------------|
| [ Yes / No ] -- [IB-ATTR] | [ Yes / No ] -- [IB-CAL]; distribution: __ High, __ Medium, __ Low | [ Yes / No ] -- [IB-FALS] | [ Yes / No ] -- [IB-PROV] |

---

### Stage 1 -- Intelligence Analyst (Intel-first; SEQUENCING-ORDER governed decision declared here)

**Entry condition:** First stage. No prior artifacts. No hypothesis stated anywhere in this document.

**Timing directive:** Fill FORM-PRE-S1 before any Stage 1 output. C-48/C-50: binary annotations `[IB-XXX]` only; N/A cells carry `[IB-XXX]`.

[Fill FORM-PRE-S1 here]

**Stage 1 execution:** Search internal sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S1: Intelligence Assessment** with 3+ findings labeled `[intel]`. No hypothesis stated. Stage-index column: **S1**.

[Fill FORM-POST-S1 here]

**Exit condition:** ARTIFACT-S1: 3+ `[intel]` findings; no hypothesis; `[IB-SEQ-O]` Intel-first decision named in PRE and POST cells; all form annotations typed-ID-only.

> **Handoff S1 -> S2: Web Evidence Collector.** `[IB-SEQ-O]`: Intel-first in effect. `[IB-PROV]`: not yet activated; activates at S2->S3.

---

### Stage 2 -- Web Evidence Collector

**Entry condition:** S1 exit gate Pass. Intel-first ordering in effect. No hypothesis stated.

**Timing directive:** Fill FORM-PRE-S2 before any Stage 2 output. C-48/C-50: binary annotations `[IB-XXX]` only; N/A cells carry `[IB-XXX]`.

[Fill FORM-PRE-S2 here]

**Stage 2 execution:** Search external sources for evidence on **$ARGUMENTS**. Produce **ARTIFACT-S2: Web Findings Corpus** with 6+ findings labeled `[web]`. No hypothesis stated. Stage-index: **S2**.

[Fill FORM-POST-S2 here]

**Exit condition:** ARTIFACT-S2 with 6+ labeled `[web]` findings; no hypothesis stated.

> **Handoff S2 -> S3: Hypothesis Architect.** `[IB-PROV]`: ACTIVATED for ARTIFACT-S1 and ARTIFACT-S2. Every Stage 3 claim must carry `[source: Stage N -- Artifact Name]`.

---

### Stage 3 -- Hypothesis Architect

**Entry condition:** S2 exit gate Pass. PROVENANCE RULE `[IB-PROV]` active. Access: ARTIFACT-S1 + S2 only.

**Timing directive:** Fill FORM-PRE-S3 before any Stage 3 output. C-48/C-50: binary annotations `[IB-XXX]` only; N/A cells carry `[IB-XXX]`.

[Fill FORM-PRE-S3 here]

**Stage 3 execution:** Declare hypotheses grounded in ARTIFACT-S1 and ARTIFACT-S2. Produce **ARTIFACT-S3: Hypothesis Register** with 3-5 hypotheses labeled `[hypothesis]`. For each: (1) claim; (2) explicit falsification condition (`[IB-FALS]` guard); (3) initial confidence (High / Medium / Low); (4) evidence citations with `[source: Stage N -- Artifact Name]`. Stage-index: **S3**.

[Fill FORM-POST-S3 here]

**Exit condition:** ARTIFACT-S3 with 3-5 falsifiable hypotheses; all claims carrying provenance tags.

> **Handoff S3 -> S4: Evidence Analyst.** `[IB-PROV]`: REMAINS ACTIVE for all three artifacts.

---

### Stage 4 -- Evidence Analyst

**Entry condition:** S3 exit gate Pass. PROVENANCE RULE active. Access: ARTIFACT-S1 + S2 + S3 only.

**Timing directive:** Fill FORM-PRE-S4 before any Stage 4 output. C-48/C-50: binary annotations `[IB-XXX]` only; N/A cells carry `[IB-XXX]`.

[Fill FORM-PRE-S4 here]

**Stage 4 execution:** Analyze evidence against hypotheses. Produce **ARTIFACT-S4: Evidence Analysis** labeled `[analysis]`. Include: confidence distribution with 2+ distinct levels (`[IB-CAL]` guard: if all same, recalibrate); support/refutation signals per hypothesis. All claims carry `[source: Stage N -- Artifact Name]`. Stage-index: **S4**.

[Fill FORM-POST-S4 here]

**Exit condition:** ARTIFACT-S4 with non-uniform confidence distribution; all provenance-tagged.

> **Handoff S4 -> S5: Synthesis Director.** `[IB-PROV]`: REMAINS ACTIVE for all four artifacts.

---

### Stage 5 -- Synthesis Director

**Entry condition:** S4 exit gate Pass. All four artifacts present. PROVENANCE RULE active.

**Timing directive:** Fill FORM-PRE-S5 before any Stage 5 output. C-48/C-50: binary annotations `[IB-XXX]` only; N/A cells carry `[IB-XXX]`.

[Fill FORM-PRE-S5 here]

**Stage 5 execution:** Produce **ARTIFACT-S5: Evidence Brief** labeled `[synthesis]` with:
1. **Campaign summary** -- topic; 5 stages in Intel-first order (`[IB-SEQ-O]` governed).
2. **Consensus findings** -- where ARTIFACT-S1 and ARTIFACT-S2 agree; cite both with stage attribution.
3. **Conflict findings** -- where S1 and S2 diverge; name divergence and assess significance.
4. **Hypothesis verdicts** -- Supported / Refuted / Indeterminate per hypothesis; falsification status.
5. **Confidence distribution** -- N High, N Medium, N Low. `[IB-CAL]` guard: if all same, recalibrate.
6. **Gaps and open questions** -- what remains unknown after the full campaign.
7. **Decision readiness** -- one sentence: "Ready to proceed" OR "Needs more investigation on [X]."

All claims carry `[source: Stage N -- Artifact Name]`. Stage-index: **S5**.

[Fill FORM-POST-S5 here]

**Exit condition:** ARTIFACT-S5 complete with consensus/conflict synthesis, calibrated confidence, one-sentence decision readiness verdict.

---

### Final Output

**Section 1 -- Evidence Brief** (ARTIFACT-S5 in full; self-contained)

**Section 2 -- Gate Record** (all 5 stages, entry and exit)

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
| *(continue for S2 through S5 -- 47 rows total; all IB values from IB fixture)* | | | | | |

**Column contracts:** `Antipattern (IB-ID FK)` = IB-ID values only (C-49). Binary and N/A cells carry `[IB-XXX]` (C-48, C-50). Row count: **47** (derived from coverage map).

---

## What Made It Golden

Three patterns distinguish V-05 from baseline V-01, each targeting a different structural gap in the invocation apparatus:

**1. Complete IB-ID homogeneity across all three cell tiers (C-50)**
V-01 used IB-IDs in binary cells but left N/A cells with English-only names. V-05 extended IB-ID citation into the N/A tier and declared this uniformity as a named invariant -- the HOMOGENEITY INVARIANT. This converts compliance from a cell-by-cell convention into a single parse rule: scan every cell for `[IB-XXX]`; any cell lacking it is a violation, regardless of tier. No English-name lookup required at any point in the apparatus.

**2. FK-typed audit table antipattern column (C-49)**
V-01's audit table carried English antipattern names -- readable but not join-auditable. V-05 renamed the column `Antipattern (IB-ID FK)` and populated it exclusively with IB-ID values drawn from the fixture. This makes the audit table a reference table: any value not matching an IB fixture row is a structurally visible violation detectable by identifier lookup, without name-string interpretation. The column contract declares the FK constraint explicitly.

**3. Typed-ID-only binary cell annotations (C-48)**
V-02/V-03 annotated binary cells with English names alongside IB-IDs (e.g., `no attribution collapse [IB-ATTR]`). V-05 strips the English name entirely: the cell carries only `[IB-ATTR]`. Combined with C-49 and C-50, this makes every cell in the apparatus -- binary form cells, N/A cells, audit table cells -- machine-verifiable by the same `[IB-XXX]` identifier-syntax scan. Zero name-matching required anywhere in the brief.

**4. All three closing properties together**
The V-05 discrimination result -- C-48 PASS, C-49 PASS, C-50 PASS -- is not additive in value; it is multiplicative in verifiability. With all three active, a single automated scan over the document (find all cells, check for `[IB-XXX]` token, flag any miss) is sufficient to fully audit the governance apparatus. No prior variation achieved this. V-04 had C-48+C-49 but left N/A cells name-only; V-03 had C-50 but left binary cells name+ID and the audit table name-only. Only V-05 closes all three tiers uniformly.

---

## Final Rubric Summary (v21)

**50 criteria, 3 tiers:**

| Tier | Criteria | Points | Description |
|------|----------|--------|-------------|
| Essential | C-01 -- C-04 | 60 pts (4 x 15) | Multi-stage campaign; evidence before hypothesis; falsifiable hypotheses; self-contained output |
| Recommended | C-05 -- C-07 | 30 pts (3 x 10) | Source attribution; consensus/conflict synthesis; calibrated confidence |
| Aspirational | C-08 -- C-50 | 10.75 pts (43 x 0.25) | Governance depth ladder from C-08 (gaps surfaced) through C-50 (three-tier IB-ID homogeneity) |

**Key aspirational milestones:**

| Criteria | Theme |
|----------|-------|
| C-08 -- C-12 | Output quality: gaps, decision readiness, calibration guard, compressed verdict |
| C-13 -- C-20 | Rule governance: named rules, sequencing rationale, coverage map immutability, inline scope |
| C-21 -- C-28 | Invocation mechanics: interrogative form, binary universality, stage indexing, entry/exit gates |
| C-29 -- C-36 | Structural extensibility: peer rules, named handoff actors, negative invocations, role access scope |
| C-37 -- C-43 | Apparatus pre-instantiation: named PRE/POST tables, preamble templates, column-header interrogatives, SEQUENCING decomposition |
| C-44 -- C-47 | IB vocabulary fixture: antipattern-absence guards, canonical IB table, checksum narrative, N/A antipattern names |
| C-48 -- C-50 | IB-ID homogeneity: typed-ID-only binary cells; FK-typed audit column; three-tier uniformity with HOMOGENEITY INVARIANT |
