---
skill: quest-variate
skill_target: campaign-evidence
date: 2026-03-16
round: 11
rubric_version: 11
---

# Variates: campaign-evidence (Round 11)

Five complete, runnable skill body prompts. Single-axis variations first (V-01 through V-03),
combined axes second (V-04 through V-05).

**New requirements for all R11 variates** (C-32 and C-33 are the addition from v11):
- **C-32**: Each named role (C-30) carries an explicit access scope — a list of which
  prior-stage outputs it is authorized to read, and no others.
- **C-33**: The total invocation artifact count is declared in the preamble as a derivable
  expression before Stage 1 executes. Count must equal (rules x stages). Any execution
  producing a different count has a coverage gap detectable by arithmetic, not interpretation.

**Checksum arithmetic for all R11 variates:**
Coverage map (4 rules x 5 stages = 20 cells):

| Rule | S1: Web | S2: Intel | S3: Hypo | S4: Analysis | S5: Synth | Positive | Negative |
|------|---------|-----------|----------|--------------|-----------|----------|----------|
| ATTRIBUTION | + | + | + | + | + | 5 | 0 |
| CALIBRATION | - | - | - | + | + | 2 | 3 |
| FALSIFICATION | - | - | + | - | + | 2 | 3 |
| SEQUENCING | + | + | + | - | - | 3 | 2 |
| **Total** | | | | | | **12** | **8** |

**Preamble checksum declaration (required):** "20 invocation artifacts = 12 positive + 8 negative,
derived from 4 rules x 5 stages."

**Baseline requirements inherited from prior rounds** (C-22, C-23, C-24, C-25, C-27, C-30, C-31):
- Universal binary `[ Yes / No ]` on every invocation (C-22)
- Stage-index suffix `[Stage N of 5]` on every invocation (C-23)
- Entry and exit conditions per stage (C-24)
- Gate record pre-templated in preamble with blank cells (C-27)
- Named role + explicit "Role passes to:" transfer at each boundary (C-30)
- Negative invocation at every non-applicable stage (C-31)

Variations explore how C-32 (access scope) and C-33 (checksum) are structurally embedded.

---

## V-01 -- Axis: Role Sequence (Access Scope as Information Boundary)

**Variation axis**: Each stage is a named role whose access scope is an explicit information
boundary, not merely an ordering constraint. The access scope names which prior-stage artifacts
the role is authorized to consume. A hypothesis constructed from pre-Stage-1 information is not
a "late step" -- it is a role charter violation, detectable at the scope level without parsing
sequencing order.

**Hypothesis**: When access scope is declared as an authorized-artifact list, sequencing
violations become impersonation: the Hypothesis Architect consumed information it had no
authorization to read. This makes C-32 the enforcement mechanism for C-02, C-10, and C-30
simultaneously -- the actor-transfer declaration (C-30) tells you who is running; the access
scope (C-32) tells you whether they used the right information; together they make sequencing
non-compliance structurally legible at the boundary.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable -- cannot be modified after any stage executes.
This is a commitment, not a record.

---

#### Rule Registry (all rules are peers; no rule is primary)

**SEQUENCING RULE** `[invoked at: Stage 1(+), Stage 2(+), Stage 3(+), Stage 4(-), Stage 5(-)]`
A hypothesis anchored before evidence gathering is a bias, not a hypothesis. Evidence stages
(S1, S2) complete before hypothesis declaration (S3). Sequencing compliance is verified at
every stage boundary where sequencing governs.
Rationale: pre-evidence hypotheses distort evidence weighting by anchoring to pre-committed
conclusions.

**ATTRIBUTION RULE** `[invoked at: Stage 1(+), Stage 2(+), Stage 3(+), Stage 4(+), Stage 5(+)]`
Every material claim names its source stage. Labels: `[web]` (S1), `[intel]` (S2),
`[hypothesis]` (S3), `[analysis]` (S4), `[synthesis]` (S5). A claim without a stage label is
unattributed.

**CALIBRATION RULE** `[invoked at: Stage 1(-), Stage 2(-), Stage 3(-), Stage 4(+), Stage 5(+)]`
Confidence ratings must vary across findings. Uniform confidence is a calibration failure.
Anti-uniformity guard: if all findings carry the same confidence level, the stage must revise.
Interrogative form: "Are at least two distinct confidence levels present?"

**FALSIFICATION RULE** `[invoked at: Stage 1(-), Stage 2(-), Stage 3(+), Stage 4(-), Stage 5(+)]`
Each hypothesis carries an explicit falsification condition -- a stated criterion that would
cause it to be rejected. Final status: Supported / Refuted / Indeterminate, assigned from
evidence weight, not fit to expectation.

Rule peer declaration: SEQUENCING, ATTRIBUTION, CALIBRATION, FALSIFICATION are equal-tier
governance rules. This declaration updates automatically as rules are added; no rule has
primary status.

---

#### Role Roster and Access Scopes

| Stage | Role Name | Access Scope -- Authorized Reads |
|-------|-----------|----------------------------------|
| Stage 1 | Web Evidence Collector | External sources only. No prior-stage artifacts exist. |
| Stage 2 | Intelligence Analyst | Stage 1 artifact (ARTIFACT-S1) only. No external sources beyond Stage 1 corpus. |
| Stage 3 | Hypothesis Architect | Stage 1 artifact (ARTIFACT-S1) + Stage 2 artifact (ARTIFACT-S2) only. Any hypothesis constructed using information that predates Stage 1 violates this role's access scope. |
| Stage 4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + Stage 3 artifact (ARTIFACT-S3) only. No new external sources. |
| Stage 5 | Synthesis Director | All prior artifacts: ARTIFACT-S1 through ARTIFACT-S4. |

Access scope is an information boundary, not just a sequencing constraint. A role that
references information outside its declared scope has violated its charter, regardless of
whether stage ordering appears correct.

---

#### Coverage Map (immutable from this point)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION | + | + | + | + | + |
| CALIBRATION | - | - | - | + | + |
| FALSIFICATION | - | - | + | - | + |
| SEQUENCING | + | + | + | - | - |

**Invocation matrix checksum (C-33):** 20 invocation artifacts = 12 positive + 8 negative,
derived from 4 rules x 5 stages. This count is pre-declared and immutable. Any execution
producing != 20 invocation artifacts has a coverage gap.

---

#### Gate Record Template (pre-instantiated blank -- fill during execution)

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|-----------|-----------|
| Stage 1 | Web Evidence Collector | First stage -- automatic Pass: [ Pass ] | Min 6 labeled findings; no hypothesis stated: [ ] |
| Stage 2 | Intelligence Analyst | Stage 1 exit gate passed: [ ] | Evidence landscape characterized; no hypothesis stated: [ ] |
| Stage 3 | Hypothesis Architect | Stage 1 + Stage 2 exit gates passed: [ ] | 3-5 hypotheses, each with falsification condition: [ ] |
| Stage 4 | Evidence Analyst | Stages 1-3 exit gates passed: [ ] | All hypotheses analyzed; confidence levels vary: [ ] |
| Stage 5 | Synthesis Director | Stages 1-4 exit gates passed: [ ] | Consensus/conflict separated; decision verdict present: [ ] |

---

### Stage 1 -- Web Evidence Collector

**ROLE: Web Evidence Collector**
**ACCESS SCOPE: External sources only. ARTIFACT-S1 does not yet exist.**

**ENTRY GATE (fill before executing)**:

| Condition | Status |
|-----------|--------|
| First stage -- no prior stages required | [ Pass ] |
| No hypothesis has been stated | [ Pass ] |

ATTRIBUTION RULE [Stage 1 of 5] -- ATTRIBUTION applied (all findings labeled `[web]`)? [ Yes / No ]
CALIBRATION RULE [Stage 1 of 5] -- CALIBRATION applicable here? [ No -- confidence rating governs Stage 4 analysis, not evidence collection ]
FALSIFICATION RULE [Stage 1 of 5] -- FALSIFICATION applicable here? [ No -- no hypotheses are declared at this stage ]
SEQUENCING RULE [Stage 1 of 5] -- Running before any hypothesis has been stated? [ Yes / No ]

Search for evidence on **{{topic}}**: primary sources, recent publications, technical references,
industry data, quantitative studies. Collect broadly -- do not filter for any anticipated
conclusion. Label every finding `[web]`.

**EXIT GATE (fill before advancing)**:

| Condition | Status |
|-----------|--------|
| Minimum 6 findings documented, each labeled `[web]` | [ Pass / Fail ] |
| No hypothesis stated anywhere in Stage 1 output | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 1 of 5] -- Every finding carries `[web]` label? [ Yes / No ]
SEQUENCING RULE [Stage 1 of 5] -- No hypothesis stated in this stage? [ Yes / No ]

> **Role passes to: Stage 2 -- Intelligence Analyst.**
> Handoff authorized only after Stage 1 exit gate is all-Pass.
> ARTIFACT-S1 (Web Findings Corpus) is now readable by Intelligence Analyst per its access scope.

---

### Stage 2 -- Intelligence Analyst

**ROLE: Intelligence Analyst**
**ACCESS SCOPE: ARTIFACT-S1 only. This role may not consult external sources or any information
predating Stage 1.**

**ENTRY GATE (fill before executing)**:

| Condition | Status |
|-----------|--------|
| Stage 1 exit gate is all-Pass | [ Pass / Fail ] |
| No hypothesis has been stated at any point | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 2 of 5] -- All new claims will carry `[intel]` label? [ Yes / No ]
CALIBRATION RULE [Stage 2 of 5] -- CALIBRATION applicable here? [ No -- confidence rating governs Stage 4, not Stage 2 intelligence characterization ]
FALSIFICATION RULE [Stage 2 of 5] -- FALSIFICATION applicable here? [ No -- no hypotheses are declared at this stage ]
SEQUENCING RULE [Stage 2 of 5] -- Hypothesis declaration has not yet occurred? [ Yes / No ]

Apply expert judgment to ARTIFACT-S1:
- Patterns and contradictions across findings
- Evidence strength (well-evidenced vs. thin)
- Domain-specific considerations the surface search missed
- Knowledge gaps -- what is absent from the evidence record

Label every new claim `[intel]`.

**EXIT GATE (fill before advancing)**:

| Condition | Status |
|-----------|--------|
| Evidence landscape characterized: patterns, conflicts, gaps named | [ Pass / Fail ] |
| No hypothesis stated anywhere in Stage 2 output | [ Pass / Fail ] |
| All new claims carry `[intel]` label | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 2 of 5] -- Every new claim labeled `[intel]`? [ Yes / No ]
SEQUENCING RULE [Stage 2 of 5] -- No hypothesis stated in this stage? [ Yes / No ]

> **Role passes to: Stage 3 -- Hypothesis Architect.**
> Handoff authorized only after Stage 2 exit gate is all-Pass.
> ARTIFACT-S2 (Intelligence Assessment) is now readable by Hypothesis Architect per its access scope.

---

### Stage 3 -- Hypothesis Architect

**ROLE: Hypothesis Architect**
**ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2 only. This role's charter is violated if any
hypothesis references information available before Stage 1 began. Such a hypothesis is not a
post-evidence derivation -- it is a pre-committed belief wearing the role's label.**

**ENTRY GATE (fill before executing)**:

| Condition | Status |
|-----------|--------|
| Stage 1 exit gate is all-Pass | [ Pass / Fail ] |
| Stage 2 exit gate is all-Pass | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 3 of 5] -- All hypotheses cite specific ARTIFACT-S1 or ARTIFACT-S2 evidence? [ Yes / No ]
CALIBRATION RULE [Stage 3 of 5] -- CALIBRATION applicable here? [ No -- this stage declares hypotheses, not confidence ratings ]
FALSIFICATION RULE [Stage 3 of 5] -- Each hypothesis carries an explicit falsification condition? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5] -- Stages 1 and 2 complete before this stage began? [ Yes / No ]

SEQUENCING RULE rationale (stated as named rule, not structural convention): A hypothesis
declared before evidence is a bias, not a hypothesis. This sequencing rule governs Stage 3's
opening condition. It is referenceable by identifier: "SEQUENCING RULE requires Stage 3 opens
only after Stage 1 and Stage 2 exit gates pass."

Declare 3-5 hypotheses. For each:
- State the falsifiable claim
- Cite the specific ARTIFACT-S1 or ARTIFACT-S2 evidence grounding it
- Name the falsification condition: what evidence would cause rejection

**EXIT GATE (fill before advancing)**:

| Condition | Status |
|-----------|--------|
| 3-5 hypotheses declared | [ Pass / Fail ] |
| Each hypothesis cites ARTIFACT-S1 or ARTIFACT-S2 evidence | [ Pass / Fail ] |
| Each hypothesis carries a named falsification condition | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 3 of 5] -- Each hypothesis cites source artifact? [ Yes / No ]
FALSIFICATION RULE [Stage 3 of 5] -- Each hypothesis has a stated falsification condition? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5] -- Stage 3 opened only after Stage 1 + Stage 2 exit gates passed? [ Yes / No ]

> **Role passes to: Stage 4 -- Evidence Analyst.**
> Handoff authorized only after Stage 3 exit gate is all-Pass.
> ARTIFACT-S3 (Hypothesis Register) is now readable by Evidence Analyst per its access scope.

---

### Stage 4 -- Evidence Analyst

**ROLE: Evidence Analyst**
**ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only. No new external sources at this
stage. This role analyzes -- it does not gather new evidence.**

**ENTRY GATE (fill before executing)**:

| Condition | Status |
|-----------|--------|
| Stages 1, 2, and 3 exit gates are all-Pass | [ Pass / Fail ] |
| Hypothesis register (ARTIFACT-S3) is available | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 4 of 5] -- Every analyzed claim carries a source-stage label? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5] -- At least two distinct confidence levels present across findings? [ Yes / No ]
FALSIFICATION RULE [Stage 4 of 5] -- FALSIFICATION applicable here? [ No -- hypotheses were declared in Stage 3; this stage applies evidence to them, not re-declares them ]
SEQUENCING RULE [Stage 4 of 5] -- SEQUENCING applicable here? [ No -- this is a post-hypothesis analysis stage; sequencing governs stages before and including Stage 3 ]

For each hypothesis in ARTIFACT-S3:
- Assess supporting evidence weight (cite source artifact)
- Assess challenging evidence weight (cite source artifact)
- Assign confidence: High / Medium / Low
- State the evidence driving the confidence assignment

Calibration guard: If confidence ratings are uniform across all findings -- recalibrate. Uniform
confidence across all findings is a calibration failure (CALIBRATION RULE anti-uniformity check).

**EXIT GATE (fill before advancing)**:

| Condition | Status |
|-----------|--------|
| All hypotheses in ARTIFACT-S3 analyzed | [ Pass / Fail ] |
| Every claim carries source-stage label | [ Pass / Fail ] |
| At least two distinct confidence levels present | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 4 of 5] -- All claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5] -- Confidence ratings non-uniform (at least 2 distinct levels)? [ Yes / No ]

> **Role passes to: Stage 5 -- Synthesis Director.**
> Handoff authorized only after Stage 4 exit gate is all-Pass.
> ARTIFACT-S4 (Evidence Analysis) is now readable by Synthesis Director per its access scope.

---

### Stage 5 -- Synthesis Director

**ROLE: Synthesis Director**
**ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 + ARTIFACT-S4. Full read access to all
prior stages. This is the final stage; there is no handoff.**

**ENTRY GATE (fill before executing)**:

| Condition | Status |
|-----------|--------|
| Stages 1-4 exit gates are all-Pass | [ Pass / Fail ] |
| All four prior artifacts available | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 5 of 5] -- All synthesis claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5] -- Non-uniform confidence ratings confirmed in synthesis? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5] -- Every hypothesis carries a final status (Supported / Refuted / Indeterminate)? [ Yes / No ]
SEQUENCING RULE [Stage 5 of 5] -- SEQUENCING applicable here? [ No -- synthesis is the terminal stage; all sequencing decisions were resolved at Stages 1-3 ]

**Consensus** (ARTIFACT-S1 and ARTIFACT-S2 agree):

**Conflict** (ARTIFACT-S1 and ARTIFACT-S2 diverge -- name the divergence explicitly):

**Hypothesis Register**:

| H# | Hypothesis | Falsification Condition | Status | Confidence | Grounding |
|----|------------|------------------------|--------|------------|-----------|
| H-01 | ... | ... | Supported/Refuted/Indeterminate | High/Med/Low | [source artifact] |

**Gaps and Open Questions** (what remains under-evidenced after this campaign):

**Decision Readiness** (one sentence -- name posture and, if not ready, name the specific gap):

ATTRIBUTION RULE [Stage 5 of 5] -- Synthesis claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5] -- Confidence distribution non-uniform? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5] -- All hypotheses resolved with final status? [ Yes / No ]

**EXIT GATE (brief complete)**:

| Condition | Status |
|-----------|--------|
| All five stage artifacts produced | [ Pass / Fail ] |
| All hypothesis Status cells populated | [ Pass / Fail ] |
| Confidence ratings non-uniform | [ Pass / Fail ] |
| Decision readiness expressed in one sentence | [ Pass / Fail ] |

---

### Output: Evidence Brief

Compile all stage artifacts into a single self-contained document with:
title, topic context, **Gate Record** (filled from preamble template), **Consolidated Invocation
Audit Table** (see below), stage-by-stage findings, hypothesis register, synthesis
(consensus/conflict explicitly separated), gaps list, decision readiness sentence.

**Consolidated Invocation Audit Table** (row count must equal checksum: 20):

| # | Rule | Stage | Stage-Index | Form | Pass/Fail |
|---|------|-------|-------------|------|-----------|
| 1 | ATTRIBUTION | S1 | [Stage 1 of 5] | Binary | |
| 2 | CALIBRATION | S1 | [Stage 1 of 5] | Binary (negative) | |
| 3 | FALSIFICATION | S1 | [Stage 1 of 5] | Binary (negative) | |
| 4 | SEQUENCING | S1 | [Stage 1 of 5] | Binary | |
| 5 | ATTRIBUTION | S2 | [Stage 2 of 5] | Binary | |
| 6 | CALIBRATION | S2 | [Stage 2 of 5] | Binary (negative) | |
| 7 | FALSIFICATION | S2 | [Stage 2 of 5] | Binary (negative) | |
| 8 | SEQUENCING | S2 | [Stage 2 of 5] | Binary | |
| 9 | ATTRIBUTION | S3 | [Stage 3 of 5] | Binary | |
| 10 | CALIBRATION | S3 | [Stage 3 of 5] | Binary (negative) | |
| 11 | FALSIFICATION | S3 | [Stage 3 of 5] | Binary | |
| 12 | SEQUENCING | S3 | [Stage 3 of 5] | Binary | |
| 13 | ATTRIBUTION | S4 | [Stage 4 of 5] | Binary | |
| 14 | CALIBRATION | S4 | [Stage 4 of 5] | Binary | |
| 15 | FALSIFICATION | S4 | [Stage 4 of 5] | Binary (negative) | |
| 16 | SEQUENCING | S4 | [Stage 4 of 5] | Binary (negative) | |
| 17 | ATTRIBUTION | S5 | [Stage 5 of 5] | Binary | |
| 18 | CALIBRATION | S5 | [Stage 5 of 5] | Binary | |
| 19 | FALSIFICATION | S5 | [Stage 5 of 5] | Binary | |
| 20 | SEQUENCING | S5 | [Stage 5 of 5] | Binary (negative) | |

**Checksum verification:** Row count = 20. Coverage map: 4 rules x 5 stages = 20. Match: [ Yes / No ]

---

---

## V-02 -- Axis: Output Format (Checksum as Structural Anchor)

**Variation axis**: The invocation matrix checksum (C-33) is the primary structural anchor of
the output format. The brief's final section contains an arithmetic verification cell: expected
total (derived from coverage map dimensions), actual row count, and match status. All other
output structures -- gate record, audit table, hypothesis register -- are pre-templated in the
preamble with blank cells. A missing invocation is visible as a missing row, not a prose
omission. Compliance is arithmetic, not interpretive.

**Hypothesis**: When the expected artifact count is pre-declared as a derivable expression
(rules x stages) and the actual count is a cell in the output, any missing invocation produces
a mismatch that is detectable without reading the brief's content. The checksum converts
completeness from a scan into a subtraction problem.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable -- cannot be modified after any stage executes.

---

#### Rule Registry

**ATTRIBUTION RULE** [scope: S1(+), S2(+), S3(+), S4(+), S5(+)]
Every material claim names its source stage. Labels: `[web]`, `[intel]`, `[hypothesis]`,
`[analysis]`, `[synthesis]`. A claim without a stage label is unattributed.

**CALIBRATION RULE** [scope: S1(-), S2(-), S3(-), S4(+), S5(+)]
Confidence ratings vary across findings. Uniform ratings are a calibration failure.
Anti-uniformity guard required at every positive invocation: "Are at least two distinct
confidence levels present?"

**FALSIFICATION RULE** [scope: S1(-), S2(-), S3(+), S4(-), S5(+)]
Each hypothesis carries a falsification condition and a final status.
Final status options: Supported / Refuted / Indeterminate.

**SEQUENCING RULE** [scope: S1(+), S2(+), S3(+), S4(-), S5(-)]
Evidence stages complete before hypothesis declaration. A hypothesis declared before Stage 2
exits is a sequencing violation. Rationale: pre-evidence hypotheses are anchors, not hypotheses.

Peer declaration: ATTRIBUTION, CALIBRATION, FALSIFICATION, SEQUENCING are equal-tier rules.
No rule is primary. Newly added rules inherit peer status automatically.

---

#### Role Roster and Access Scopes

| Stage | Role | Access Scope |
|-------|------|-------------|
| Stage 1 | Web Evidence Collector | External sources only |
| Stage 2 | Intelligence Analyst | Stage 1 output only |
| Stage 3 | Hypothesis Architect | Stage 1 + Stage 2 outputs only |
| Stage 4 | Evidence Analyst | Stage 1 + Stage 2 + Stage 3 outputs only |
| Stage 5 | Synthesis Director | All prior stage outputs (Stage 1-4) |

---

#### Coverage Map and Invocation Matrix Checksum (C-33)

Pre-declared before Stage 1 executes. Immutable.

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|----|----------|----------|
| ATTRIBUTION | + | + | + | + | + | 5 | 0 |
| CALIBRATION | - | - | - | + | + | 2 | 3 |
| FALSIFICATION | - | - | + | - | + | 2 | 3 |
| SEQUENCING | + | + | + | - | - | 3 | 2 |
| **Total** | | | | | | **12** | **8** |

**Checksum (C-33):** 20 invocation artifacts = 12 positive + 8 negative,
derived from 4 rules x 5 stages.

> This value is pre-declared. The audit table at the close of the brief must contain
> exactly 20 rows. Any count other than 20 indicates a missing or duplicate invocation.
> A discrepancy is detectable by subtraction: expected 20, actual [count at close].

---

#### Gate Record Template (blank -- fill during execution)

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|-----------|-----------|
| Stage 1 | Web Evidence Collector | Automatic -- first stage: [ Pass ] | 6+ labeled findings; no hypothesis: [ ] |
| Stage 2 | Intelligence Analyst | Stage 1 exit all-Pass: [ ] | Evidence landscape characterized; no hypothesis: [ ] |
| Stage 3 | Hypothesis Architect | Stage 1+2 exit all-Pass: [ ] | 3-5 hypotheses with falsification conditions: [ ] |
| Stage 4 | Evidence Analyst | Stage 1-3 exit all-Pass: [ ] | All hypotheses analyzed; 2+ confidence levels: [ ] |
| Stage 5 | Synthesis Director | Stage 1-4 exit all-Pass: [ ] | Synthesis complete; decision verdict in one sentence: [ ] |

---

#### Invocation Audit Table (running -- append each row inline as it occurs)

> Append a row immediately at each rule invocation. Do not batch post-hoc.
> Row count at brief close must equal 20 (checksum declared above).

| # | Rule | Stage | Stage-Index | Invocation Form | Pass/Fail |
|---|------|-------|-------------|----------------|-----------|
| (rows appended as stages execute) | | | | | |

---

### Stage 1 -- Web Evidence Collector

Role: Web Evidence Collector | Access scope: external sources only

**Entry condition**: No hypothesis stated; first stage.

ATTRIBUTION RULE [Stage 1 of 5] -- All findings labeled `[web]`? [ Yes / No ]
> Append audit row: ATTRIBUTION | S1 | [Stage 1 of 5] | Binary | [result]

CALIBRATION RULE [Stage 1 of 5] -- Applicable at this stage? [ No -- confidence rating not yet applicable ]
> Append audit row: CALIBRATION | S1 | [Stage 1 of 5] | Binary (negative) | Not applicable

FALSIFICATION RULE [Stage 1 of 5] -- Applicable at this stage? [ No -- no hypotheses declared yet ]
> Append audit row: FALSIFICATION | S1 | [Stage 1 of 5] | Binary (negative) | Not applicable

SEQUENCING RULE [Stage 1 of 5] -- Running before any hypothesis stated? [ Yes / No ]
> Append audit row: SEQUENCING | S1 | [Stage 1 of 5] | Binary | [result]

Search **{{topic}}**: primary sources, publications, technical references, industry data.
Label every finding `[web]`. Collect broadly -- do not filter for expected conclusions.

**Exit condition**: 6+ labeled findings; no hypothesis; all findings carry `[web]`.

> **Role passes to: Stage 2 -- Intelligence Analyst.**

---

### Stage 2 -- Intelligence Analyst

Role: Intelligence Analyst | Access scope: Stage 1 output only

**Entry condition**: Stage 1 exit gate all-Pass.

ATTRIBUTION RULE [Stage 2 of 5] -- All new claims labeled `[intel]`? [ Yes / No ]
> Append audit row: ATTRIBUTION | S2 | [Stage 2 of 5] | Binary | [result]

CALIBRATION RULE [Stage 2 of 5] -- Applicable at this stage? [ No -- confidence rating not yet applicable ]
> Append audit row: CALIBRATION | S2 | [Stage 2 of 5] | Binary (negative) | Not applicable

FALSIFICATION RULE [Stage 2 of 5] -- Applicable at this stage? [ No -- no hypotheses declared yet ]
> Append audit row: FALSIFICATION | S2 | [Stage 2 of 5] | Binary (negative) | Not applicable

SEQUENCING RULE [Stage 2 of 5] -- Hypothesis declaration not yet occurred? [ Yes / No ]
> Append audit row: SEQUENCING | S2 | [Stage 2 of 5] | Binary | [result]

Apply expert judgment to Stage 1 corpus: patterns, contradictions, evidence strength, gaps,
domain-specific considerations. Label every new claim `[intel]`.

**Exit condition**: Evidence landscape characterized; no hypothesis stated; all new claims `[intel]`.

> **Role passes to: Stage 3 -- Hypothesis Architect.**

---

### Stage 3 -- Hypothesis Architect

Role: Hypothesis Architect | Access scope: Stage 1 + Stage 2 outputs only

**Entry condition**: Stage 1 and Stage 2 exit gates all-Pass.

ATTRIBUTION RULE [Stage 3 of 5] -- Each hypothesis cites specific Stage 1 or Stage 2 evidence? [ Yes / No ]
> Append audit row: ATTRIBUTION | S3 | [Stage 3 of 5] | Binary | [result]

CALIBRATION RULE [Stage 3 of 5] -- Applicable at this stage? [ No -- hypothesis declaration, not confidence rating ]
> Append audit row: CALIBRATION | S3 | [Stage 3 of 5] | Binary (negative) | Not applicable

FALSIFICATION RULE [Stage 3 of 5] -- Each hypothesis carries an explicit falsification condition? [ Yes / No ]
> Append audit row: FALSIFICATION | S3 | [Stage 3 of 5] | Binary | [result]

SEQUENCING RULE [Stage 3 of 5] -- Stages 1 and 2 complete before this stage began? [ Yes / No ]
> Append audit row: SEQUENCING | S3 | [Stage 3 of 5] | Binary | [result]

Declare 3-5 hypotheses derived from Stage 1 + Stage 2 evidence. For each: falsifiable claim,
grounding evidence citation, falsification condition.

**Exit condition**: 3-5 hypotheses; each cites Stage 1/2 evidence; each has falsification condition.

> **Role passes to: Stage 4 -- Evidence Analyst.**

---

### Stage 4 -- Evidence Analyst

Role: Evidence Analyst | Access scope: Stage 1 + Stage 2 + Stage 3 outputs only

**Entry condition**: Stages 1, 2, 3 exit gates all-Pass.

ATTRIBUTION RULE [Stage 4 of 5] -- All claims carry source-stage labels? [ Yes / No ]
> Append audit row: ATTRIBUTION | S4 | [Stage 4 of 5] | Binary | [result]

CALIBRATION RULE [Stage 4 of 5] -- At least two distinct confidence levels present? [ Yes / No ]
> Append audit row: CALIBRATION | S4 | [Stage 4 of 5] | Binary | [result]

FALSIFICATION RULE [Stage 4 of 5] -- Applicable at this stage? [ No -- hypotheses declared in Stage 3; Stage 4 applies evidence, not re-declares ]
> Append audit row: FALSIFICATION | S4 | [Stage 4 of 5] | Binary (negative) | Not applicable

SEQUENCING RULE [Stage 4 of 5] -- Applicable at this stage? [ No -- post-hypothesis analysis; sequencing governs stages before and including Stage 3 ]
> Append audit row: SEQUENCING | S4 | [Stage 4 of 5] | Binary (negative) | Not applicable

For each hypothesis: supporting evidence, challenging evidence (both labeled by source stage),
confidence rating (High / Medium / Low), evidence basis for rating.

Calibration guard: uniform confidence across all findings is a failure -- recalibrate.

**Exit condition**: All hypotheses analyzed; all claims labeled; 2+ distinct confidence levels.

> **Role passes to: Stage 5 -- Synthesis Director.**

---

### Stage 5 -- Synthesis Director

Role: Synthesis Director | Access scope: Stage 1-4 outputs (full read)

**Entry condition**: Stages 1-4 exit gates all-Pass.

ATTRIBUTION RULE [Stage 5 of 5] -- All synthesis claims carry source-stage labels? [ Yes / No ]
> Append audit row: ATTRIBUTION | S5 | [Stage 5 of 5] | Binary | [result]

CALIBRATION RULE [Stage 5 of 5] -- Confidence ratings non-uniform across full brief? [ Yes / No ]
> Append audit row: CALIBRATION | S5 | [Stage 5 of 5] | Binary | [result]

FALSIFICATION RULE [Stage 5 of 5] -- All hypotheses carry final status? [ Yes / No ]
> Append audit row: FALSIFICATION | S5 | [Stage 5 of 5] | Binary | [result]

SEQUENCING RULE [Stage 5 of 5] -- Applicable at this stage? [ No -- terminal stage; sequencing resolved at Stages 1-3 ]
> Append audit row: SEQUENCING | S5 | [Stage 5 of 5] | Binary (negative) | Not applicable

**Consensus** (Stage 1 + Stage 2 agree): ...

**Conflict** (Stage 1 + Stage 2 diverge -- name the divergence explicitly): ...

**Hypothesis Register**:

| H# | Hypothesis | Falsification Condition | Status | Confidence | Evidence Basis |
|----|------------|------------------------|--------|------------|----------------|

**Gaps and Open Questions**: ...

**Decision Readiness** (one sentence): ...

**Exit condition**: All hypothesis Status cells populated; confidence non-uniform;
decision verdict present as one sentence.

---

### Output: Arithmetic Verification

At close of brief, verify checksum:

| Metric | Expected | Actual | Match |
|--------|----------|--------|-------|
| Total invocation artifacts | 20 | [count audit table rows] | [ Yes / No ] |
| Positive invocations | 12 | [count positive rows] | [ Yes / No ] |
| Negative invocations | 8 | [count negative rows] | [ Yes / No ] |
| Coverage map derivation | 4 rules x 5 stages = 20 | [confirm] | [ Yes / No ] |

> If any cell shows No: a coverage gap exists. Identify missing rows and add before delivering.

---

---

## V-03 -- Axis: Lifecycle Emphasis (Preamble as Commitment Ledger)

**Variation axis**: The brief's lifecycle is organized as Phase 0 (pre-execution commitment),
Phases 1-5 (stage execution), and Phase 6 (output compilation). Phase 0 is the commitment
ledger -- every structural decision is declared and locked before Phase 1 begins. Phase 0
produces three artifacts: the coverage map (C-17/C-19), the blank gate record template (C-27),
and the checksum declaration (C-33). The access scopes per role (C-32) are also Phase 0
declarations. No stage may begin until Phase 0 is fully populated.

**Hypothesis**: When the preamble is a ledger that must be filled before execution begins,
every structural omission is a blank cell visible from the start of the document. A missing
access scope, an absent checksum, or a blank gate template row are all visible without reading
the stage narrative. Phase 0 compliance is scannable; Phase 1-5 compliance is auditable.

---

You are running the full evidence campaign for: **{{topic}}**

---

## PHASE 0: PRE-EXECUTION COMMITMENT LEDGER

> Phase 0 must be fully populated before Phase 1 (Stage 1) begins. Every blank cell in
> Phase 0 is a visible structural gap. Fill all cells now.

### P0-A: Rule Registry

**SEQUENCING RULE** [scope: S1(+), S2(+), S3(+), S4(-), S5(-)]
Evidence stages (Stage 1, Stage 2) complete before hypothesis declaration (Stage 3).
Rationale: a hypothesis declared before evidence is a bias, not a hypothesis.
This rule is referenceable by identifier at each stage it governs.

**ATTRIBUTION RULE** [scope: S1(+), S2(+), S3(+), S4(+), S5(+)]
Every material claim names its source stage with a labeled tag. Unlabeled claims are
unattributed.

**CALIBRATION RULE** [scope: S1(-), S2(-), S3(-), S4(+), S5(+)]
Confidence ratings vary across findings. Uniform confidence is a calibration failure.
Anti-uniformity guard: "Are at least two distinct confidence levels present?"

**FALSIFICATION RULE** [scope: S1(-), S2(-), S3(+), S4(-), S5(+)]
Each hypothesis carries an explicit falsification condition and a final status
(Supported / Refuted / Indeterminate).

> Peer declaration: all four rules are equal-tier. This declaration is extensible: adding
> a rule does not require updating any static integer or priority ranking.

### P0-B: Role Roster and Access Scopes (C-32)

> Access scopes are declared here before any stage executes. A role that reads outside its
> declared scope has violated its charter, regardless of stage ordering.

| Stage | Role | Access Scope |
|-------|------|-------------|
| Stage 1 | Web Evidence Collector | External sources only. No prior-stage artifacts. |
| Stage 2 | Intelligence Analyst | Stage 1 output only. No external sources. |
| Stage 3 | Hypothesis Architect | Stage 1 + Stage 2 outputs only. Pre-Stage-1 information is out of scope. |
| Stage 4 | Evidence Analyst | Stage 1 + Stage 2 + Stage 3 outputs only. No new external sources. |
| Stage 5 | Synthesis Director | All prior stage outputs (Stage 1-4). |

### P0-C: Coverage Map (immutable from this point; cannot be modified after Phase 1 begins)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION | + | + | + | + | + |
| CALIBRATION | - | - | - | + | + |
| FALSIFICATION | - | - | + | - | + |
| SEQUENCING | + | + | + | - | - |

### P0-D: Invocation Matrix Checksum (C-33)

**Pre-declared derivation:** 20 invocation artifacts = 12 positive + 8 negative,
derived from 4 rules x 5 stages.

This value is locked at Phase 0 and cannot change. If the execution-close row count
differs from 20, a coverage gap exists.

### P0-E: Gate Record Template (blank -- fill during Phases 1-5)

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|-----------|-----------|
| Stage 1 | Web Evidence Collector | Automatic -- first stage: [ Pass ] | 6+ labeled findings; no hypothesis: [ ] |
| Stage 2 | Intelligence Analyst | Stage 1 exit all-Pass: [ ] | Evidence landscape characterized; no hypothesis: [ ] |
| Stage 3 | Hypothesis Architect | Stage 1+2 exit all-Pass: [ ] | 3-5 hypotheses with falsification conditions: [ ] |
| Stage 4 | Evidence Analyst | Stage 1-3 exit all-Pass: [ ] | All hypotheses analyzed; 2+ confidence levels: [ ] |
| Stage 5 | Synthesis Director | Stage 1-4 exit all-Pass: [ ] | Synthesis complete; one-sentence decision verdict: [ ] |

> Phase 0 complete when: all rule scopes declared, all roles have access scopes, coverage map
> filled, checksum stated, gate record template has all rows. Verify all cells non-blank before
> advancing to Phase 1.

---

## PHASES 1-5: STAGE EXECUTION

Execute each stage in order. Fill gate record cells. Append invocation audit rows.
Access scopes from P0-B are binding.

---

### Phase 1: Stage 1 -- Web Evidence Collector

Access scope: External sources only (P0-B).

**Entry gate**: Automatic -- first stage. [ Pass ]

**Rule invocations (fill each cell):**

| Rule | Stage-Index | Applicable? | Invocation | Pass/Fail |
|------|-------------|------------|------------|-----------|
| ATTRIBUTION | [Stage 1 of 5] | Yes | All findings labeled `[web]`? [ Yes / No ] | |
| CALIBRATION | [Stage 1 of 5] | No | Not applicable -- confidence rating governs Stage 4. [ N/A ] | N/A |
| FALSIFICATION | [Stage 1 of 5] | No | Not applicable -- no hypotheses at this stage. [ N/A ] | N/A |
| SEQUENCING | [Stage 1 of 5] | Yes | Running before any hypothesis stated? [ Yes / No ] | |

Search **{{topic}}**: primary sources, publications, technical references, industry data.
Label every finding `[web]`. Collect without filtering for expected conclusions.

**Exit gate**: Fill P0-E row for Stage 1.

> **Role passes to: Stage 2 -- Intelligence Analyst.**

---

### Phase 2: Stage 2 -- Intelligence Analyst

Access scope: Stage 1 output only (P0-B).

**Entry gate**: Stage 1 exit all-Pass. Fill P0-E entry cell.

**Rule invocations:**

| Rule | Stage-Index | Applicable? | Invocation | Pass/Fail |
|------|-------------|------------|------------|-----------|
| ATTRIBUTION | [Stage 2 of 5] | Yes | All new claims labeled `[intel]`? [ Yes / No ] | |
| CALIBRATION | [Stage 2 of 5] | No | Not applicable -- confidence rating governs Stage 4. [ N/A ] | N/A |
| FALSIFICATION | [Stage 2 of 5] | No | Not applicable -- no hypotheses declared yet. [ N/A ] | N/A |
| SEQUENCING | [Stage 2 of 5] | Yes | No hypothesis stated yet? [ Yes / No ] | |

Apply expert judgment to Stage 1 corpus: patterns, contradictions, evidence strength, gaps.
Label every new claim `[intel]`.

**Exit gate**: Fill P0-E exit cell for Stage 2.

> **Role passes to: Stage 3 -- Hypothesis Architect.**

---

### Phase 3: Stage 3 -- Hypothesis Architect

Access scope: Stage 1 + Stage 2 outputs only (P0-B).

**Entry gate**: Stage 1 + Stage 2 exit all-Pass. Fill P0-E entry cell.

**Rule invocations:**

| Rule | Stage-Index | Applicable? | Invocation | Pass/Fail |
|------|-------------|------------|------------|-----------|
| ATTRIBUTION | [Stage 3 of 5] | Yes | Each hypothesis cites Stage 1 or Stage 2 evidence? [ Yes / No ] | |
| CALIBRATION | [Stage 3 of 5] | No | Not applicable -- hypothesis declaration, not confidence rating. [ N/A ] | N/A |
| FALSIFICATION | [Stage 3 of 5] | Yes | Each hypothesis has explicit falsification condition? [ Yes / No ] | |
| SEQUENCING | [Stage 3 of 5] | Yes | Stage 1 + Stage 2 complete before this stage opened? [ Yes / No ] | |

Declare 3-5 hypotheses from Stage 1 + Stage 2 evidence. Each: falsifiable claim, grounding
evidence, falsification condition.

**Exit gate**: Fill P0-E exit cell for Stage 3.

> **Role passes to: Stage 4 -- Evidence Analyst.**

---

### Phase 4: Stage 4 -- Evidence Analyst

Access scope: Stage 1 + Stage 2 + Stage 3 outputs only (P0-B).

**Entry gate**: Stages 1-3 exit all-Pass. Fill P0-E entry cell.

**Rule invocations:**

| Rule | Stage-Index | Applicable? | Invocation | Pass/Fail |
|------|-------------|------------|------------|-----------|
| ATTRIBUTION | [Stage 4 of 5] | Yes | All claims carry source-stage labels? [ Yes / No ] | |
| CALIBRATION | [Stage 4 of 5] | Yes | At least two distinct confidence levels present? [ Yes / No ] | |
| FALSIFICATION | [Stage 4 of 5] | No | Not applicable -- hypotheses declared in Stage 3; Stage 4 applies evidence. [ N/A ] | N/A |
| SEQUENCING | [Stage 4 of 5] | No | Not applicable -- post-hypothesis stage; sequencing governed Stages 1-3. [ N/A ] | N/A |

For each hypothesis: supporting evidence, challenging evidence, confidence (High/Med/Low),
evidence basis. Calibration guard: uniform confidence requires revision.

**Exit gate**: Fill P0-E exit cell for Stage 4.

> **Role passes to: Stage 5 -- Synthesis Director.**

---

### Phase 5: Stage 5 -- Synthesis Director

Access scope: All prior stage outputs -- Stage 1-4 (P0-B).

**Entry gate**: Stages 1-4 exit all-Pass. Fill P0-E entry cell.

**Rule invocations:**

| Rule | Stage-Index | Applicable? | Invocation | Pass/Fail |
|------|-------------|------------|------------|-----------|
| ATTRIBUTION | [Stage 5 of 5] | Yes | All synthesis claims carry source-stage labels? [ Yes / No ] | |
| CALIBRATION | [Stage 5 of 5] | Yes | Confidence ratings non-uniform across full brief? [ Yes / No ] | |
| FALSIFICATION | [Stage 5 of 5] | Yes | All hypotheses carry final status? [ Yes / No ] | |
| SEQUENCING | [Stage 5 of 5] | No | Not applicable -- terminal stage; sequencing resolved at Stages 1-3. [ N/A ] | N/A |

**Consensus** (Stage 1 + Stage 2 agree): ...
**Conflict** (Stage 1 + Stage 2 diverge): ...
**Hypothesis Register**: [H# | Hypothesis | Status | Confidence | Evidence Basis]
**Gaps and Open Questions**: ...
**Decision Readiness** (one sentence): ...

**Exit gate**: Fill P0-E exit cell for Stage 5.

---

## PHASE 6: OUTPUT COMPILATION

Compile into a single self-contained document. Required sections:
1. Title and topic context
2. Phase 0 declarations (P0-A through P0-E) -- as governance record
3. Stage findings (Stage 1-4 with labeled claims)
4. Hypothesis Register with falsification status
5. Synthesis (consensus / conflict explicitly separated)
6. Gaps and Open Questions
7. Decision Readiness (one sentence)
8. Consolidated Invocation Audit Table
9. Checksum Verification

**Checksum Verification (Phase 6 gate):**

| Metric | Expected | Actual | Match |
|--------|----------|--------|-------|
| Total invocation artifact rows | 20 | [count] | [ Yes / No ] |
| Positive rows | 12 | [count] | [ Yes / No ] |
| Negative rows | 8 | [count] | [ Yes / No ] |

> If match = No: brief is not complete. Identify gap and add missing invocation before delivering.

---

---

## V-04 -- Axes: Role Sequence + Output Format (Artifact-Signed Handoffs)

**Variation axes (combined)**:
- **Role Sequence**: Each stage is a named role that produces a signed artifact. Handoffs
  transfer artifact custody, not just execution control. An artifact's provenance is its signer.
- **Output Format**: The final brief is organized around artifact receipts. Each artifact appears
  as a named section with its signer declared. The audit table links rule invocations to artifact
  names, not only stage numbers.

**Hypothesis**: When roles sign artifacts and handoffs transfer custody, access scope violations
become artifact-provenance violations: a hypothesis that cites information outside Stage 1-2
has sourced from an artifact its role was not authorized to receive. The checksum covers
invocations and artifact signatures simultaneously -- both are countable.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable.

---

#### Rule Registry (all peers)

**ATTRIBUTION RULE** [scope: S1(+), S2(+), S3(+), S4(+), S5(+)]
Every material claim carries a source-artifact tag: `[ARTIFACT-S1]`, `[ARTIFACT-S2]`,
`[ARTIFACT-S3]`, `[ARTIFACT-S4]`. A claim without an artifact tag is unattributed.

**CALIBRATION RULE** [scope: S1(-), S2(-), S3(-), S4(+), S5(+)]
Confidence ratings vary. Uniform ratings are a failure. Anti-uniformity interrogative at
every positive invocation: "Are at least two distinct confidence levels present?"

**FALSIFICATION RULE** [scope: S1(-), S2(-), S3(+), S4(-), S5(+)]
Each hypothesis carries an explicit falsification condition and final status.

**SEQUENCING RULE** [scope: S1(+), S2(+), S3(+), S4(-), S5(-)]
Evidence artifacts (ARTIFACT-S1, ARTIFACT-S2) must exist and be signed before ARTIFACT-S3
is opened. An ARTIFACT-S3 entry citing sources outside ARTIFACT-S1 and ARTIFACT-S2 is a
sequencing violation at the artifact-provenance level.

---

#### Role Roster, Access Scopes, and Artifact Signatures

| Stage | Role | Access Scope | Produces | Signs |
|-------|------|-------------|----------|-------|
| Stage 1 | Web Evidence Collector | External sources only | ARTIFACT-S1: Web Findings Corpus | Signed by: Web Evidence Collector |
| Stage 2 | Intelligence Analyst | ARTIFACT-S1 only | ARTIFACT-S2: Intelligence Assessment | Signed by: Intelligence Analyst |
| Stage 3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 only | ARTIFACT-S3: Hypothesis Register | Signed by: Hypothesis Architect |
| Stage 4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only | ARTIFACT-S4: Evidence Analysis | Signed by: Evidence Analyst |
| Stage 5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 | ARTIFACT-S5: Evidence Brief | Signed by: Synthesis Director |

**Invocation matrix checksum:** 20 artifacts = 12 positive + 8 negative, derived from
4 rules x 5 stages.

---

#### Coverage Map (immutable)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION | + | + | + | + | + |
| CALIBRATION | - | - | - | + | + |
| FALSIFICATION | - | - | + | - | + |
| SEQUENCING | + | + | + | - | - |

---

#### Gate Record Template (blank)

| Stage | Role | Artifact Produced | Entry Gate | Exit Gate |
|-------|------|-------------------|-----------|-----------|
| Stage 1 | Web Evidence Collector | ARTIFACT-S1 | Automatic: [ Pass ] | ARTIFACT-S1 signed and contains 6+ labeled findings: [ ] |
| Stage 2 | Intelligence Analyst | ARTIFACT-S2 | ARTIFACT-S1 signed: [ ] | ARTIFACT-S2 signed and evidence landscape characterized: [ ] |
| Stage 3 | Hypothesis Architect | ARTIFACT-S3 | ARTIFACT-S1 + ARTIFACT-S2 signed: [ ] | ARTIFACT-S3 signed with 3-5 hypotheses + falsification conditions: [ ] |
| Stage 4 | Evidence Analyst | ARTIFACT-S4 | ARTIFACT-S1 through ARTIFACT-S3 signed: [ ] | ARTIFACT-S4 signed with all hypotheses analyzed + 2+ confidence levels: [ ] |
| Stage 5 | Synthesis Director | ARTIFACT-S5 | ARTIFACT-S1 through ARTIFACT-S4 signed: [ ] | ARTIFACT-S5 signed with synthesis, gaps, decision verdict: [ ] |

---

### Stage 1 -- Web Evidence Collector

**ARTIFACT-S1: Web Findings Corpus** | *Produced by: Web Evidence Collector*
Access scope: External sources only. ARTIFACT-S1 does not yet exist.

ATTRIBUTION [Stage 1 of 5] -- Findings will carry `[ARTIFACT-S1]` tag? [ Yes / No ]
CALIBRATION [Stage 1 of 5] -- Applicable? [ No -- not yet applicable ]
FALSIFICATION [Stage 1 of 5] -- Applicable? [ No -- no hypotheses declared ]
SEQUENCING [Stage 1 of 5] -- Running before ARTIFACT-S3 exists? [ Yes / No ]

Search **{{topic}}**: primary sources, publications, technical references, industry data.
Tag every finding `[ARTIFACT-S1]`.

ATTRIBUTION [Stage 1 of 5] -- All findings tagged? [ Yes / No ]
SEQUENCING [Stage 1 of 5] -- ARTIFACT-S3 not yet instantiated? [ Yes / No ]

**ARTIFACT-S1 signed.** Date/context: [fill]

> **Custody transferred to: Stage 2 -- Intelligence Analyst.**
> ARTIFACT-S1 is now available in Intelligence Analyst's access scope.

---

### Stage 2 -- Intelligence Analyst

**ARTIFACT-S2: Intelligence Assessment** | *Produced by: Intelligence Analyst*
Access scope: ARTIFACT-S1 only.

ATTRIBUTION [Stage 2 of 5] -- New claims will carry `[ARTIFACT-S2]` tag? [ Yes / No ]
CALIBRATION [Stage 2 of 5] -- Applicable? [ No -- not yet applicable ]
FALSIFICATION [Stage 2 of 5] -- Applicable? [ No -- no hypotheses declared ]
SEQUENCING [Stage 2 of 5] -- ARTIFACT-S3 not yet instantiated? [ Yes / No ]

Apply expert judgment to ARTIFACT-S1: patterns, contradictions, evidence strength, gaps.
Tag every new claim `[ARTIFACT-S2]`.

ATTRIBUTION [Stage 2 of 5] -- All new claims tagged `[ARTIFACT-S2]`? [ Yes / No ]
SEQUENCING [Stage 2 of 5] -- No hypothesis stated? [ Yes / No ]

**ARTIFACT-S2 signed.** Date/context: [fill]

> **Custody transferred to: Stage 3 -- Hypothesis Architect.**
> ARTIFACT-S1 + ARTIFACT-S2 are now available in Hypothesis Architect's access scope.

---

### Stage 3 -- Hypothesis Architect

**ARTIFACT-S3: Hypothesis Register** | *Produced by: Hypothesis Architect*
Access scope: ARTIFACT-S1 + ARTIFACT-S2 only. Any hypothesis entry citing information outside
these two artifacts violates this role's access charter.

ATTRIBUTION [Stage 3 of 5] -- Each hypothesis cites ARTIFACT-S1 or ARTIFACT-S2 provenance? [ Yes / No ]
CALIBRATION [Stage 3 of 5] -- Applicable? [ No -- hypothesis declaration, not confidence rating ]
FALSIFICATION [Stage 3 of 5] -- Each hypothesis carries an explicit falsification condition? [ Yes / No ]
SEQUENCING [Stage 3 of 5] -- ARTIFACT-S1 + ARTIFACT-S2 both signed before this stage began? [ Yes / No ]

Declare 3-5 hypotheses. Each entry in ARTIFACT-S3:
- Falsifiable claim
- Provenance: cite specific ARTIFACT-S1 or ARTIFACT-S2 entry
- Falsification condition

ATTRIBUTION [Stage 3 of 5] -- All ARTIFACT-S3 entries cite source artifact? [ Yes / No ]
FALSIFICATION [Stage 3 of 5] -- All entries have falsification conditions? [ Yes / No ]
SEQUENCING [Stage 3 of 5] -- Only ARTIFACT-S1 + ARTIFACT-S2 sourced? [ Yes / No ]

**ARTIFACT-S3 signed.** Date/context: [fill]

> **Custody transferred to: Stage 4 -- Evidence Analyst.**
> ARTIFACT-S1 through ARTIFACT-S3 are now available in Evidence Analyst's access scope.

---

### Stage 4 -- Evidence Analyst

**ARTIFACT-S4: Evidence Analysis** | *Produced by: Evidence Analyst*
Access scope: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only. No new external sources.

ATTRIBUTION [Stage 4 of 5] -- All entries in ARTIFACT-S4 cite source artifact? [ Yes / No ]
CALIBRATION [Stage 4 of 5] -- At least two distinct confidence levels in ARTIFACT-S4? [ Yes / No ]
FALSIFICATION [Stage 4 of 5] -- Applicable? [ No -- Stage 3 declared hypotheses; Stage 4 applies evidence ]
SEQUENCING [Stage 4 of 5] -- Applicable? [ No -- post-hypothesis stage ]

For each ARTIFACT-S3 hypothesis: supporting evidence (cite source artifact), challenging
evidence (cite source artifact), confidence (High/Med/Low), evidence basis.

Calibration guard: if all confidence ratings are identical -- ARTIFACT-S4 requires revision.

ATTRIBUTION [Stage 4 of 5] -- All ARTIFACT-S4 entries cite source artifacts? [ Yes / No ]
CALIBRATION [Stage 4 of 5] -- Confidence non-uniform? [ Yes / No ]

**ARTIFACT-S4 signed.** Date/context: [fill]

> **Custody transferred to: Stage 5 -- Synthesis Director.**
> ARTIFACT-S1 through ARTIFACT-S4 are now available in Synthesis Director's access scope.

---

### Stage 5 -- Synthesis Director

**ARTIFACT-S5: Evidence Brief** | *Produced by: Synthesis Director*
Access scope: ARTIFACT-S1 through ARTIFACT-S4. Full read. Terminal stage.

ATTRIBUTION [Stage 5 of 5] -- All synthesis claims cite source artifacts? [ Yes / No ]
CALIBRATION [Stage 5 of 5] -- Confidence non-uniform across ARTIFACT-S5? [ Yes / No ]
FALSIFICATION [Stage 5 of 5] -- All ARTIFACT-S3 hypotheses have final status in ARTIFACT-S5? [ Yes / No ]
SEQUENCING [Stage 5 of 5] -- Applicable? [ No -- terminal stage ]

**Consensus** (ARTIFACT-S1 + ARTIFACT-S2 agree): ...
**Conflict** (ARTIFACT-S1 + ARTIFACT-S2 diverge): ...
**Hypothesis Register** (from ARTIFACT-S3, resolved via ARTIFACT-S4):

| H# | Hypothesis | Falsification Condition | Status | Confidence | Source Artifacts |
|----|------------|------------------------|--------|------------|-----------------|

**Gaps and Open Questions**: ...
**Decision Readiness** (one sentence): ...

ATTRIBUTION [Stage 5 of 5] -- Full brief has source-artifact tags? [ Yes / No ]
CALIBRATION [Stage 5 of 5] -- Non-uniform confidence confirmed? [ Yes / No ]
FALSIFICATION [Stage 5 of 5] -- All hypotheses resolved? [ Yes / No ]

**ARTIFACT-S5 signed.** Date/context: [fill]

---

### Consolidated Invocation Audit Table and Checksum

| # | Rule | Artifact | Stage-Index | Form | Pass/Fail |
|---|------|---------|-------------|------|-----------|
| 1 | ATTRIBUTION | ARTIFACT-S1 | [Stage 1 of 5] | Binary | |
| 2 | CALIBRATION | ARTIFACT-S1 | [Stage 1 of 5] | Binary (negative) | N/A |
| 3 | FALSIFICATION | ARTIFACT-S1 | [Stage 1 of 5] | Binary (negative) | N/A |
| 4 | SEQUENCING | ARTIFACT-S1 | [Stage 1 of 5] | Binary | |
| 5 | ATTRIBUTION | ARTIFACT-S2 | [Stage 2 of 5] | Binary | |
| 6 | CALIBRATION | ARTIFACT-S2 | [Stage 2 of 5] | Binary (negative) | N/A |
| 7 | FALSIFICATION | ARTIFACT-S2 | [Stage 2 of 5] | Binary (negative) | N/A |
| 8 | SEQUENCING | ARTIFACT-S2 | [Stage 2 of 5] | Binary | |
| 9 | ATTRIBUTION | ARTIFACT-S3 | [Stage 3 of 5] | Binary | |
| 10 | CALIBRATION | ARTIFACT-S3 | [Stage 3 of 5] | Binary (negative) | N/A |
| 11 | FALSIFICATION | ARTIFACT-S3 | [Stage 3 of 5] | Binary | |
| 12 | SEQUENCING | ARTIFACT-S3 | [Stage 3 of 5] | Binary | |
| 13 | ATTRIBUTION | ARTIFACT-S4 | [Stage 4 of 5] | Binary | |
| 14 | CALIBRATION | ARTIFACT-S4 | [Stage 4 of 5] | Binary | |
| 15 | FALSIFICATION | ARTIFACT-S4 | [Stage 4 of 5] | Binary (negative) | N/A |
| 16 | SEQUENCING | ARTIFACT-S4 | [Stage 4 of 5] | Binary (negative) | N/A |
| 17 | ATTRIBUTION | ARTIFACT-S5 | [Stage 5 of 5] | Binary | |
| 18 | CALIBRATION | ARTIFACT-S5 | [Stage 5 of 5] | Binary | |
| 19 | FALSIFICATION | ARTIFACT-S5 | [Stage 5 of 5] | Binary | |
| 20 | SEQUENCING | ARTIFACT-S5 | [Stage 5 of 5] | Binary (negative) | N/A |

**Checksum:** Expected 20 rows, derived from 4 rules x 5 stages.
Actual row count: [fill]. Match: [ Yes / No ]

---

---

## V-05 -- Axes: Lifecycle Emphasis + Phrasing Register (Formal Imperative)

**Variation axes (combined)**:
- **Lifecycle Emphasis**: The brief's structure is governed by a formal lifecycle protocol.
  Each phase is a compliance gate. An executor may not advance without satisfying the prior gate.
- **Phrasing Register**: The prompt is written in formal imperative. Every requirement is a
  SHALL or MUST. No advisory language. No hedging. Compliance conditions are stated as hard
  constraints, not as suggestions.

**Hypothesis**: Formal imperative register signals that the governance framework is
non-negotiable. An executor reading "the executor SHALL NOT advance" interprets the gate as
a constraint, not a recommendation. Combined with lifecycle gating, the register reinforces
the lifecycle: "This brief is compliant if and only if..." makes non-compliance definitionally
visible, not merely unfortunate.

---

You are running the campaign-evidence skill for: **{{topic}}**

This skill SHALL produce a complete evidence brief by executing five named stages in declared
order. The executor SHALL NOT advance to any stage until all prior stages' exit conditions are
met. The executor SHALL NOT state a hypothesis before Stage 3. The executor SHALL NOT deliver
the brief until the final checksum verifies at 20 invocation artifacts.

---

### ARTICLE I: GOVERNANCE FRAMEWORK

The following four rules SHALL govern this brief. All rules are equal-tier peers. No rule is
primary. Adding a rule SHALL NOT require updating any static integer elsewhere in this brief.

**SEQUENCING RULE** [scope: S1(+), S2(+), S3(+), S4(-), S5(-)]
The executor SHALL complete evidence stages (Stage 1, Stage 2) before opening hypothesis stage
(Stage 3). A hypothesis stated before Stage 2 exit gate passes is a SEQUENCING RULE violation.
Rationale: a hypothesis anchored before evidence gathering is a bias, not a hypothesis.
The executor SHALL invoke this rule at every applicable stage and SHALL declare inapplicability
at every non-applicable stage.

**ATTRIBUTION RULE** [scope: S1(+), S2(+), S3(+), S4(+), S5(+)]
The executor SHALL tag every material claim with its source-stage label. Unlabeled claims are
unattributed and SHALL be treated as missing evidence. At least 70% of material claims SHALL
carry stage labels.

**CALIBRATION RULE** [scope: S1(-), S2(-), S3(-), S4(+), S5(+)]
The executor SHALL assign confidence ratings that vary across findings. Uniform confidence
across all findings is a CALIBRATION RULE violation. The executor SHALL invoke the anti-
uniformity interrogative at Stage 4 and Stage 5: "Are at least two distinct confidence levels
present?" A brief that cannot answer Yes SHALL NOT proceed past Stage 4's exit gate.

**FALSIFICATION RULE** [scope: S1(-), S2(-), S3(+), S4(-), S5(+)]
Each hypothesis the executor declares SHALL carry an explicit falsification condition. The
executor SHALL assign a final status (Supported / Refuted / Indeterminate) to each hypothesis
at Stage 5. The executor SHALL assign status from evidence weight, not fit to expectation.
A Refuted or Indeterminate outcome is a first-class result and SHALL NOT be revised upward
without new evidence.

---

### ARTICLE II: ROLE CHARTER AND ACCESS SCOPES

Each stage SHALL be executed as a named role. The executor SHALL NOT read information outside
a role's declared access scope. A role that constructs output from out-of-scope information
has violated its charter. This violation SHALL be treated as equivalent to a gate failure.

| Stage | Role | Access Scope -- Authorized Reads |
|-------|------|----------------------------------|
| Stage 1 | Web Evidence Collector | External sources only. No prior-stage outputs exist. |
| Stage 2 | Intelligence Analyst | Stage 1 output only. External sources SHALL NOT be consulted. |
| Stage 3 | Hypothesis Architect | Stage 1 + Stage 2 outputs only. Pre-Stage-1 information is out of scope. The executor SHALL NOT declare a hypothesis grounded in information that predates Stage 1. |
| Stage 4 | Evidence Analyst | Stage 1 + Stage 2 + Stage 3 outputs only. No new external sources SHALL be introduced. |
| Stage 5 | Synthesis Director | All prior stage outputs (Stage 1-4). No restrictions. |

---

### ARTICLE III: COVERAGE COMMITMENT

The following coverage map is finalized at this point and SHALL NOT be modified after Stage 1
begins. The executor acknowledges that any post-execution modification is detectable as a
governance violation.

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION | + | + | + | + | + |
| CALIBRATION | - | - | - | + | + |
| FALSIFICATION | - | - | + | - | + |
| SEQUENCING | + | + | + | - | - |

**INVOCATION MATRIX CHECKSUM (C-33, immutable):**
The brief SHALL contain exactly 20 invocation artifacts = 12 positive + 8 negative,
derived from 4 rules x 5 stages. The executor SHALL verify this count before delivering.
A brief with a count other than 20 SHALL NOT be delivered.

---

### ARTICLE IV: PRE-EXECUTION GATE RECORD

The following gate record template SHALL be present in the brief before Stage 1 executes.
The executor SHALL fill each cell during execution. A brief delivered with any blank cell
in this table is non-compliant.

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|-----------|-----------|
| Stage 1 | Web Evidence Collector | First stage -- automatic: [ Pass ] | 6+ labeled findings; no hypothesis: [ ] |
| Stage 2 | Intelligence Analyst | Stage 1 exit all-Pass: [ ] | Evidence landscape characterized; no hypothesis: [ ] |
| Stage 3 | Hypothesis Architect | Stage 1+2 exit all-Pass: [ ] | 3-5 hypotheses with falsification conditions: [ ] |
| Stage 4 | Evidence Analyst | Stage 1-3 exit all-Pass: [ ] | All hypotheses analyzed; 2+ confidence levels: [ ] |
| Stage 5 | Synthesis Director | Stage 1-4 exit all-Pass: [ ] | Synthesis complete; one-sentence decision verdict: [ ] |

---

### ARTICLE V: EXECUTION PROTOCOL

The executor SHALL execute Stages 1-5 in declared order. At each stage, the executor SHALL
fill entry gate, execute stage body, invoke all applicable rules with binary form and stage
index, declare inapplicability at non-applicable stages, and fill exit gate before advancing.

---

#### Stage 1 -- Web Evidence Collector

Access scope: External sources only (Article II).
The executor SHALL NOT state a hypothesis in this stage.

**Entry gate fill:** [ Pass ] (first stage)

The executor SHALL invoke all four rules now, in binary form:

ATTRIBUTION RULE [Stage 1 of 5] -- All findings SHALL carry `[web]` label? [ Yes / No ]
CALIBRATION RULE [Stage 1 of 5] -- CALIBRATION applies here? [ No -- confidence rating governs Stage 4 ]
FALSIFICATION RULE [Stage 1 of 5] -- FALSIFICATION applies here? [ No -- no hypotheses at this stage ]
SEQUENCING RULE [Stage 1 of 5] -- Executing before any hypothesis is stated? [ Yes / No ]

The executor SHALL search **{{topic}}**: primary sources, publications, technical references,
industry data. The executor SHALL label every finding `[web]`. The executor SHALL NOT filter
for expected conclusions.

**Exit gate fill:**

| Condition | SHALL be met before advancing | Status |
|-----------|------------------------------|--------|
| 6+ findings documented, each labeled `[web]` | MUST | [ Pass / Fail ] |
| No hypothesis stated in Stage 1 | MUST | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 1 of 5] -- All findings labeled `[web]`? [ Yes / No ]
SEQUENCING RULE [Stage 1 of 5] -- No hypothesis stated? [ Yes / No ]

> **The executor SHALL transfer control to: Stage 2 -- Intelligence Analyst.**
> Transfer SHALL NOT occur until Stage 1 exit gate is all-Pass.

---

#### Stage 2 -- Intelligence Analyst

Access scope: Stage 1 output only (Article II). The executor SHALL NOT consult external sources.
The executor SHALL NOT state a hypothesis in this stage.

**Entry gate fill:** Stage 1 exit all-Pass: [ Pass / Fail ]

ATTRIBUTION RULE [Stage 2 of 5] -- New claims SHALL carry `[intel]` label? [ Yes / No ]
CALIBRATION RULE [Stage 2 of 5] -- CALIBRATION applies here? [ No -- not yet applicable ]
FALSIFICATION RULE [Stage 2 of 5] -- FALSIFICATION applies here? [ No -- no hypotheses declared ]
SEQUENCING RULE [Stage 2 of 5] -- No hypothesis stated yet? [ Yes / No ]

The executor SHALL apply expert judgment to Stage 1 corpus: patterns, contradictions,
evidence strength, domain-specific considerations, knowledge gaps. The executor SHALL label
every new claim `[intel]`.

**Exit gate fill:**

| Condition | SHALL be met | Status |
|-----------|-------------|--------|
| Evidence landscape characterized (patterns, conflicts, gaps named) | MUST | [ Pass / Fail ] |
| No hypothesis stated in Stage 2 | MUST | [ Pass / Fail ] |
| All new claims carry `[intel]` label | MUST | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 2 of 5] -- All new claims labeled `[intel]`? [ Yes / No ]
SEQUENCING RULE [Stage 2 of 5] -- No hypothesis stated? [ Yes / No ]

> **Transfer to: Stage 3 -- Hypothesis Architect.**
> SHALL NOT transfer until Stage 2 exit gate is all-Pass.

---

#### Stage 3 -- Hypothesis Architect

Access scope: Stage 1 + Stage 2 outputs only (Article II). The executor SHALL NOT construct
any hypothesis from information that predates Stage 1.

**Entry gate fill:**

| Condition | SHALL be met | Status |
|-----------|-------------|--------|
| Stage 1 exit gate all-Pass | MUST | [ Pass / Fail ] |
| Stage 2 exit gate all-Pass | MUST | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 3 of 5] -- Each hypothesis SHALL cite specific Stage 1 or Stage 2 evidence? [ Yes / No ]
CALIBRATION RULE [Stage 3 of 5] -- CALIBRATION applies here? [ No -- hypothesis declaration, not confidence rating ]
FALSIFICATION RULE [Stage 3 of 5] -- Each hypothesis SHALL carry an explicit falsification condition? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5] -- Stage 1 + Stage 2 complete before this stage opened? [ Yes / No ]

The executor SHALL declare 3-5 hypotheses. Each hypothesis SHALL include:
- A falsifiable claim
- A citation of the specific Stage 1 or Stage 2 evidence grounding it
- An explicit falsification condition

**Exit gate fill:**

| Condition | SHALL be met | Status |
|-----------|-------------|--------|
| 3-5 hypotheses declared | MUST | [ Pass / Fail ] |
| Each hypothesis cites Stage 1 or Stage 2 evidence | MUST | [ Pass / Fail ] |
| Each hypothesis carries a named falsification condition | MUST | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 3 of 5] -- Hypotheses cite source evidence? [ Yes / No ]
FALSIFICATION RULE [Stage 3 of 5] -- Hypotheses have falsification conditions? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5] -- Stage 3 opened only after Stage 1+2 exit gates passed? [ Yes / No ]

> **Transfer to: Stage 4 -- Evidence Analyst.**
> SHALL NOT transfer until Stage 3 exit gate is all-Pass.

---

#### Stage 4 -- Evidence Analyst

Access scope: Stage 1 + Stage 2 + Stage 3 outputs only (Article II). The executor SHALL NOT
introduce new external sources at this stage.

**Entry gate fill:**

| Condition | SHALL be met | Status |
|-----------|-------------|--------|
| Stages 1, 2, 3 exit gates all-Pass | MUST | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 4 of 5] -- All analyzed claims SHALL carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5] -- At least two distinct confidence levels SHALL be present? [ Yes / No ]
FALSIFICATION RULE [Stage 4 of 5] -- FALSIFICATION applies here? [ No -- hypotheses declared in Stage 3; Stage 4 applies evidence to them ]
SEQUENCING RULE [Stage 4 of 5] -- SEQUENCING applies here? [ No -- post-hypothesis stage ]

For each hypothesis, the executor SHALL document: supporting evidence (cite source stage),
challenging evidence (cite source stage), confidence rating (High / Medium / Low), evidence
basis for the rating.

The executor SHALL invoke the calibration anti-uniformity check: if all confidence ratings
are identical, the executor SHALL revise before filling the exit gate.

**Exit gate fill:**

| Condition | SHALL be met | Status |
|-----------|-------------|--------|
| All hypotheses analyzed | MUST | [ Pass / Fail ] |
| All claims carry source-stage labels | MUST | [ Pass / Fail ] |
| At least two distinct confidence levels present | MUST | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 4 of 5] -- All claims labeled? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5] -- Confidence non-uniform? [ Yes / No ]

> **Transfer to: Stage 5 -- Synthesis Director.**
> SHALL NOT transfer until Stage 4 exit gate is all-Pass.

---

#### Stage 5 -- Synthesis Director

Access scope: Stage 1-4 outputs (Article II). Terminal stage.

**Entry gate fill:**

| Condition | SHALL be met | Status |
|-----------|-------------|--------|
| Stages 1, 2, 3, 4 exit gates all-Pass | MUST | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 5 of 5] -- All synthesis claims SHALL carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5] -- Non-uniform confidence SHALL be confirmed? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5] -- All hypotheses SHALL carry final status? [ Yes / No ]
SEQUENCING RULE [Stage 5 of 5] -- SEQUENCING applies here? [ No -- terminal stage ]

**Consensus** (Stage 1 + Stage 2 agree): ...
**Conflict** (Stage 1 + Stage 2 diverge -- name divergence explicitly): ...

**Hypothesis Register**:

| H# | Hypothesis | Falsification Condition | Status | Confidence | Evidence Basis |
|----|------------|------------------------|--------|------------|----------------|

**Gaps and Open Questions**: ...
**Decision Readiness** (one sentence; SHALL name posture and, if not ready, the specific gap): ...

ATTRIBUTION RULE [Stage 5 of 5] -- Synthesis claims labeled? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5] -- Confidence non-uniform? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5] -- All hypotheses resolved? [ Yes / No ]

**Exit gate fill:**

| Condition | SHALL be met | Status |
|-----------|-------------|--------|
| All five stages produced output | MUST | [ Pass / Fail ] |
| All hypothesis Status cells populated | MUST | [ Pass / Fail ] |
| Confidence ratings non-uniform | MUST | [ Pass / Fail ] |
| Decision readiness expressed as one sentence | MUST | [ Pass / Fail ] |

---

### ARTICLE VI: DELIVERY COMPLIANCE

The executor SHALL NOT deliver the brief until all conditions in this article are met.

**Consolidated Invocation Audit Table** (the executor SHALL populate all 20 rows):

| # | Rule | Stage | Stage-Index | Form | Pass/Fail |
|---|------|-------|-------------|------|-----------|
| 1-20 | [fill per execution] | | | | |

**FINAL CHECKSUM VERIFICATION (delivery gate):**

| Metric | Required | Actual | Compliant |
|--------|----------|--------|-----------|
| Total invocation artifact rows | 20 | [count] | [ Yes / No ] |
| Positive invocations | 12 | [count] | [ Yes / No ] |
| Negative invocations | 8 | [count] | [ Yes / No ] |
| Derivation verified (4 x 5 = 20) | Yes | [confirm] | [ Yes / No ] |

The brief is compliant if and only if: all gate record cells are Pass, all invocation audit
rows are filled, and the checksum row shows Compliant = Yes for all four metrics.
