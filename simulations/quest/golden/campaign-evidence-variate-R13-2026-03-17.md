---
skill: quest-variate
skill_target: campaign-evidence
date: 2026-03-17
round: 13
rubric_version: 13
---

# Variates: campaign-evidence (Round 13)

Five complete, runnable skill body prompts. Single-axis variations first (V-01 through V-03),
combined axes second (V-04 through V-05).

**Structural signals from R12 PASS+ analysis driving R13 variation axes:**

- **Signal 1 (from C-21, V-03 PASS+):** Dual-phase interrogative invocation -- a pre-execution
  commitment check ("Will X hold? [Yes/No]") followed by a post-execution verification check
  ("Does X hold? [Yes/No]") at every governance-checkable stage. Intent-execution gaps become
  visible even when the executor answers "Yes" to the prospective check and then produces
  non-compliant output, because the post-execution check must also be answered.

- **Signal 2 (from C-30, V-05 PASS+):** Provenance activation moves from the role charter
  (a static declaration) to the live handoff boundary (an active transfer event). The handoff
  block enumerates every artifact being transferred AND activates the PROVENANCE RULE at that
  boundary -- making the rule active at the moment a scope-restricted role receives authorized
  artifacts, rather than expecting the role to consult its preamble declaration on entry.

These two signals are candidates for C-36 and C-37 in rubric v14. R13 variates embed them
structurally so they can be evaluated and scored before promotion.

**Inherited baseline (all R13 variates must satisfy):**

Coverage map (5 rules x 5 stages = 25 cells):

| Rule | S1: Web | S2: Intel | S3: Hypo | S4: Analysis | S5: Synth | Positive | Negative |
|------|---------|-----------|----------|--------------|-----------|----------|----------|
| ATTRIBUTION  | + | + | + | + | + | 5 | 0 |
| CALIBRATION  | - | - | - | + | + | 2 | 3 |
| FALSIFICATION| - | - | + | - | + | 2 | 3 |
| SEQUENCING   | + | + | + | - | - | 3 | 2 |
| PROVENANCE   | - | - | + | + | + | 3 | 2 |
| **Total**    |   |   |   |   |   | **15** | **10** |

**Preamble checksum declaration (required):** "25 invocation artifacts = 15 positive + 10 negative,
derived from 5 rules x 5 stages."

**Scope-restricted stages** (PROVENANCE RULE applies): Stage 3 (Hypothesis Architect),
Stage 4 (Evidence Analyst), Stage 5 (Synthesis Director). Every claim in these stages must
carry `[source: Stage N -- Artifact Name]`.

**Delivery gate (C-33 enforcement):** The brief SHALL NOT be closed or delivered until the
invocation artifact count at the consolidated audit table equals 25. A count != 25 is a
delivery blocker, not a finding.

**Role names (consistent across all variates):**
- Stage 1: Web Evidence Collector
- Stage 2: Intelligence Analyst
- Stage 3: Hypothesis Architect
- Stage 4: Evidence Analyst
- Stage 5: Synthesis Director

**R12 baseline requirements inherited:**
- Universal binary `[ Yes / No ]` on every invocation (C-22)
- Stage-index suffix `[Stage N of 5]` on every invocation (C-23)
- Entry and exit conditions per stage (C-24)
- Gate record pre-templated in preamble with blank cells (C-27)
- Named role + "Role passes to:" transfer at each boundary (C-30)
- Negative invocation at every non-applicable stage (C-31)
- Role access scope declared per stage (C-32)
- Invocation matrix total pre-declared as derivable checksum (C-33)
- Provenance tags `[source: Stage N -- Artifact Name]` in scope-restricted stages (C-34)

---

## V-01 -- Axis: Role Sequence (Provenance Activation at Handoff Boundary, Not in Role Charter)

**Variation axis**: Provenance activation is removed from the static role charter and placed
exclusively at the live handoff boundary. In R12 V-01 and V-02, the PROVENANCE RULE was
declared in the preamble's role roster with inline scope annotations -- the receiving role
was expected to consult its charter on entry. V-01 here removes provenance from the charter
and activates it dynamically: when Role A hands off to Role B, the handoff declaration
enumerates the authorized artifacts AND states "PROVENANCE RULE activated for this role at
this boundary." A receiving role that runs without a completed handoff block has no activated
provenance rule -- the gap is structural, not retrospective.

**Hypothesis**: Moving provenance activation from the role charter (consulted once, easy to
skip) to the handoff boundary (must be completed before the next role opens) converts
provenance compliance from a static declaration into a live enforcement event. A role that
begins execution without a completed handoff block is structurally unauthorized -- the
provenance gap is visible before the first claim is made, not discovered at audit.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable -- cannot be modified after any stage executes.
This document is a commitment, not a record. The coverage map, gate template, role roster,
and invocation checksum are sealed at preamble finalization.

---

#### Rule Registry (all five rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+)]`
Every material claim names its source stage. Labels: `[web]` S1, `[intel]` S2,
`[hypothesis]` S3, `[analysis]` S4, `[synthesis]` S5. Unlabeled claims are unattributed.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+)]`
Confidence ratings must vary across findings. Uniform ratings are a calibration failure.
Anti-uniformity guard: at every positive invocation, verify at least two distinct confidence
levels appear above. If all ratings are identical, CALIBRATION fails.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+)]`
Each hypothesis carries an explicit falsification condition: a stated criterion that, if
observed, causes the hypothesis to be rejected. A hypothesis without a falsification
condition is a belief. Final status options: Supported / Refuted / Indeterminate.

**SEQUENCING RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-)]`
Evidence stages (S1, S2) must complete before hypothesis declaration (S3). A hypothesis
stated before any evidence stage executes is an anchor, not a hypothesis. Named principle:
"A hypothesis anchored before evidence gathering is a bias, not a hypothesis." This
sequencing decision is formalized as a named rule so any reader can cite it by identifier.

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+)]`
NOTE: This rule is NOT activated by the role roster. It is activated exclusively at the
handoff boundary immediately preceding each scope-restricted stage. Every claim in a
scope-restricted stage carries `[source: Stage N -- Artifact Name]`. A claim with no
provenance tag is a structural gap. A tag naming an out-of-scope artifact is a charter
violation. Scope-restricted stages: S3, S4, S5.

Peer declaration: ATTRIBUTION, CALIBRATION, FALSIFICATION, SEQUENCING, PROVENANCE are
equal-tier governance rules. No rule is primary. Adding a new peer rule propagates
automatically through the coverage map and checksum; no static integers require manual
update.

---

#### Role Roster (access scope only -- provenance activation occurs at handoff, not here)

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Web Evidence Collector | External sources only. No prior artifacts. |
| S2 | Intelligence Analyst | ARTIFACT-S1 (Web Findings Corpus) only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Intelligence Assessment) only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 (Hypothesis Register) only. |
| S5 | Synthesis Director | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 + ARTIFACT-S4 (Evidence Analysis) only. |

---

#### Coverage Map (immutable -- sealed at preamble; cannot be modified after execution begins)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION  | + | + | + | + | + |
| CALIBRATION  | - | - | - | + | + |
| FALSIFICATION| - | - | + | - | + |
| SEQUENCING   | + | + | + | - | - |
| PROVENANCE   | - | - | + | + | + |

This map is finalized before Stage 1 begins and cannot be modified after any stage executes.
Invocation checksum: **25 artifacts = 15 positive + 10 negative** (5 rules x 5 stages).
This count is derivable from the map dimensions; it updates automatically if rules or stages
are added. No static integer stores this value independently.

---

#### Gate Record Template (pre-instantiated -- blank cells filled during execution)

| Stage | Role | Entry: Condition | Entry: Status | Exit: Condition | Exit: Status |
|-------|------|-----------------|---------------|-----------------|--------------|
| S1 | Web Evidence Collector | First stage -- no prerequisites | [ Pass ] | 6+ labeled findings; no hypothesis stated | [ ] |
| S2 | Intelligence Analyst | S1 exit all-Pass; handoff block complete | [ ] | Evidence landscape characterized; no hypothesis; all claims `[intel]` | [ ] |
| S3 | Hypothesis Architect | S2 exit all-Pass; handoff block complete; PROVENANCE RULE activated | [ ] | 3-5 hypotheses with falsification conditions; all claims carry provenance tags | [ ] |
| S4 | Evidence Analyst | S3 exit all-Pass; handoff block complete; PROVENANCE RULE activated | [ ] | All hypotheses analyzed; 2+ confidence levels; all claims carry provenance tags | [ ] |
| S5 | Synthesis Director | S4 exit all-Pass; handoff block complete; PROVENANCE RULE activated | [ ] | Synthesis complete; consensus/conflict separated; decision verdict one sentence; all claims carry provenance tags | [ ] |

---

### STAGE EXECUTION

Do not advance to Stage N+1 until Stage N's exit gate is all-Pass and its handoff block is
complete. Completing the handoff block is what authorizes the next stage to open.

---

### Stage 1 -- Web Evidence Collector

**ENTRY GATE:**

| Condition | Status |
|-----------|--------|
| First stage -- no prior stages required | [ Pass ] |
| No hypothesis has been stated anywhere | [ Pass ] |

**Rule invocations [Stage 1 of 5]:**

ATTRIBUTION [S1 of 5]: Are all findings labeled `[web]`? [ Yes / No ]
CALIBRATION [S1 of 5]: Applicable at evidence collection? [ No -- confidence governs analysis ]
FALSIFICATION [S1 of 5]: Applicable before hypothesis declaration? [ No ]
SEQUENCING [S1 of 5]: Is this an evidence stage executing before hypothesis declaration? [ Yes / No ]
PROVENANCE [S1 of 5]: Applicable at a non-scope-restricted stage? [ No -- activated at handoff ]

Conduct structured web research on $ARGUMENTS. Search for: primary sources, recent
publications, technical data, industry reports, quantitative evidence. Label every finding
`[web]`. Do not state hypotheses. Collect broadly -- gaps are for Stage 2 to characterize.

**EXIT GATE:**

| Condition | Status |
|-----------|--------|
| 6+ findings documented, each labeled `[web]` | [ Pass / Fail ] |
| No hypothesis stated anywhere in Stage 1 output | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S1 to S2:**

> **Role passes to: Stage 2 -- Intelligence Analyst.**
> Artifacts authorized for transfer: ARTIFACT-S1 (Web Findings Corpus).
> Intelligence Analyst access scope: ARTIFACT-S1 only. External sources and pre-Stage-1
> information are outside scope.
> PROVENANCE RULE status at this boundary: Not yet activated. Stage 2 is not scope-restricted.

---

### Stage 2 -- Intelligence Analyst

**ENTRY GATE:**

| Condition | Status |
|-----------|--------|
| S1 exit gate is all-Pass | [ Pass / Fail ] |
| Handoff block S1-to-S2 is complete | [ Pass / Fail ] |
| No hypothesis has been stated anywhere | [ Pass / Fail ] |

**Rule invocations [Stage 2 of 5]:**

ATTRIBUTION [S2 of 5]: Are all new claims labeled `[intel]`? [ Yes / No ]
CALIBRATION [S2 of 5]: Applicable at intelligence characterization? [ No ]
FALSIFICATION [S2 of 5]: Applicable before hypothesis declaration? [ No ]
SEQUENCING [S2 of 5]: Is evidence gathering still complete before hypothesis? [ Yes / No ]
PROVENANCE [S2 of 5]: Applicable at a non-scope-restricted stage? [ No -- not yet activated ]

Apply expert judgment to ARTIFACT-S1. Characterize: patterns, contradictions, evidence
strength (well-evidenced / thin / contested), knowledge gaps. Label every new claim `[intel]`.

**EXIT GATE:**

| Condition | Status |
|-----------|--------|
| Evidence landscape characterized: patterns, conflicts, gaps named | [ Pass / Fail ] |
| No hypothesis stated in Stage 2 output | [ Pass / Fail ] |
| All new claims carry `[intel]` label | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S2 to S3:**

> **Role passes to: Stage 3 -- Hypothesis Architect.**
> Artifacts authorized for transfer: ARTIFACT-S1 (Web Findings Corpus), ARTIFACT-S2
> (Intelligence Assessment).
> Hypothesis Architect access scope: ARTIFACT-S1 + ARTIFACT-S2 only. Any claim citing
> information outside these two artifacts is a charter violation.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.** Stage 3 is scope-restricted. Every claim
> produced by the Hypothesis Architect must carry `[source: Stage N -- Artifact Name]`
> where N is 1 or 2. A claim with no provenance tag is a structural gap detectable at this
> boundary.

---

### Stage 3 -- Hypothesis Architect

**ENTRY GATE:**

| Condition | Status |
|-----------|--------|
| S2 exit gate is all-Pass | [ Pass / Fail ] |
| Handoff block S2-to-S3 is complete and includes PROVENANCE RULE activation | [ Pass / Fail ] |
| PROVENANCE RULE activated at this boundary | [ Pass / Fail ] |

**Rule invocations [Stage 3 of 5]:**

ATTRIBUTION [S3 of 5]: All claims labeled `[hypothesis]`? [ Yes / No ]
CALIBRATION [S3 of 5]: Applicable before analysis? [ No ]
FALSIFICATION [S3 of 5]: Does every hypothesis carry an explicit falsification condition? [ Yes / No ]
SEQUENCING [S3 of 5]: All hypotheses grounded in S1+S2 evidence, not pre-evidence assumptions? [ Yes / No ]
PROVENANCE [S3 of 5]: Does every claim carry `[source: Stage N -- Artifact Name]` where N in {1,2}? [ Yes / No ]

Declare 3-5 hypotheses about $ARGUMENTS. Each hypothesis must:
1. State a specific claim about the topic
2. Cite the evidence that prompted it: `[source: Stage 1 -- Web Findings Corpus]` or
   `[source: Stage 2 -- Intelligence Assessment]`
3. State a falsification condition
4. Carry a preliminary confidence level (High / Medium / Low)

Label every claim `[hypothesis]`.

**EXIT GATE:**

| Condition | Status |
|-----------|--------|
| 3-5 hypotheses with falsification conditions | [ Pass / Fail ] |
| Every claim carries `[hypothesis]` label | [ Pass / Fail ] |
| Every claim carries `[source: Stage N -- Artifact Name]` where N in {1,2} | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S3 to S4:**

> **Role passes to: Stage 4 -- Evidence Analyst.**
> Artifacts authorized for transfer: ARTIFACT-S1 (Web Findings Corpus), ARTIFACT-S2
> (Intelligence Assessment), ARTIFACT-S3 (Hypothesis Register).
> Evidence Analyst access scope: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.** Stage 4 is scope-restricted. Every claim
> produced by the Evidence Analyst must carry `[source: Stage N -- Artifact Name]`
> where N in {1,2,3}. A tag naming any other artifact is a charter violation.

---

### Stage 4 -- Evidence Analyst

**ENTRY GATE:**

| Condition | Status |
|-----------|--------|
| S3 exit gate is all-Pass | [ Pass / Fail ] |
| Handoff block S3-to-S4 is complete and includes PROVENANCE RULE activation | [ Pass / Fail ] |
| PROVENANCE RULE activated at this boundary | [ Pass / Fail ] |

**Rule invocations [Stage 4 of 5]:**

ATTRIBUTION [S4 of 5]: All claims labeled `[analysis]`? [ Yes / No ]
CALIBRATION [S4 of 5]: Are at least two distinct confidence levels present across findings? [ Yes / No ]
FALSIFICATION [S4 of 5]: Applicable at analysis stage? [ No -- falsification governs hypothesis declaration and synthesis ]
SEQUENCING [S4 of 5]: Applicable here? [ No -- evidence-before-hypothesis ordering is complete ]
PROVENANCE [S4 of 5]: Does every claim carry `[source: Stage N -- Artifact Name]` where N in {1,2,3}? [ Yes / No ]

Analyze each hypothesis from ARTIFACT-S3 against the evidence in ARTIFACT-S1 and
ARTIFACT-S2. For each hypothesis:
1. Summarize supporting evidence (cite: `[source: Stage N -- Artifact Name]`)
2. Summarize counter-evidence or absences
3. Assign confidence: High / Medium / Low -- calibrate across hypotheses; uniform ratings fail
4. Note any new gaps or conflicts discovered

Label every claim `[analysis]`.

**EXIT GATE:**

| Condition | Status |
|-----------|--------|
| All hypotheses from S3 are addressed | [ Pass / Fail ] |
| At least two distinct confidence levels used | [ Pass / Fail ] |
| All claims carry `[analysis]` label | [ Pass / Fail ] |
| All claims carry `[source: Stage N -- Artifact Name]` where N in {1,2,3} | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S4 to S5:**

> **Role passes to: Stage 5 -- Synthesis Director.**
> Artifacts authorized for transfer: ARTIFACT-S1 (Web Findings Corpus), ARTIFACT-S2
> (Intelligence Assessment), ARTIFACT-S3 (Hypothesis Register), ARTIFACT-S4 (Evidence Analysis).
> Synthesis Director access scope: ARTIFACT-S1 through ARTIFACT-S4 only.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.** Stage 5 is scope-restricted. Every claim
> produced by the Synthesis Director must carry `[source: Stage N -- Artifact Name]`
> where N in {1,2,3,4}. A tag naming any other artifact is a charter violation.

---

### Stage 5 -- Synthesis Director

**ENTRY GATE:**

| Condition | Status |
|-----------|--------|
| S4 exit gate is all-Pass | [ Pass / Fail ] |
| Handoff block S4-to-S5 is complete and includes PROVENANCE RULE activation | [ Pass / Fail ] |
| PROVENANCE RULE activated at this boundary | [ Pass / Fail ] |

**Rule invocations [Stage 5 of 5]:**

ATTRIBUTION [S5 of 5]: All claims labeled `[synthesis]`? [ Yes / No ]
CALIBRATION [S5 of 5]: Confidence distribution varied (not uniform) across final findings? [ Yes / No ]
FALSIFICATION [S5 of 5]: Does every hypothesis carry a final status (Supported/Refuted/Indeterminate)? [ Yes / No ]
SEQUENCING [S5 of 5]: Applicable at synthesis? [ No -- ordering constraint complete ]
PROVENANCE [S5 of 5]: Does every claim carry `[source: Stage N -- Artifact Name]` where N in {1,2,3,4}? [ Yes / No ]

Synthesize findings into a coherent evidence brief on $ARGUMENTS:

1. **Consensus findings**: where S1 and S2 agree
2. **Conflicts**: where S1 and S2 diverge -- name the conflict explicitly
3. **Hypothesis verdicts**: final status (Supported/Refuted/Indeterminate) for each hypothesis
4. **Gaps and open questions**: what remains under-evidenced after the full campaign
5. **Decision readiness**: one sentence naming posture and, if not ready, the specific gap

Label every claim `[synthesis]`. Every claim carries `[source: Stage N -- Artifact Name]`.

**EXIT GATE:**

| Condition | Status |
|-----------|--------|
| Consensus and conflict explicitly separated | [ Pass / Fail ] |
| All hypotheses carry final status | [ Pass / Fail ] |
| Gaps section present | [ Pass / Fail ] |
| Decision readiness stated in one sentence | [ Pass / Fail ] |
| All claims carry `[synthesis]` and `[source: Stage N -- Artifact Name]` | [ Pass / Fail ] |

---

### OUTPUT ASSEMBLY

Assemble the final evidence brief with these sections in order:

1. **Brief header**: title, topic, date, stages run
2. **Filled gate record**: copy the gate record template above and fill all Pass/Fail cells
3. **Stage outputs**: S1 through S5 in sequence
4. **Consolidated invocation audit table**: one row per rule/stage cell; columns: Rule, Stage,
   Applicable (+/-), Invocation form (binary/negative), Pass/Fail
5. **Synthesis narrative**: consensus findings, conflicts, hypothesis verdicts
6. **Gaps and open questions**
7. **Decision readiness** (one sentence)

**Delivery gate check before closing:** Confirm invocation artifact count at the audit table
equals 25 (5 rules x 5 stages). A count != 25 is a delivery blocker. Do not close this brief
until the audit table count equals 25.

---

---

## V-02 -- Axis: Output Format (Stage-Indexed Evidence Table with Grounded-In Constraints)

**Variation axis**: Every evidence claim, hypothesis, analysis finding, and synthesis
conclusion is a row in a stage-indexed master table -- not embedded in stage narrative. Each
row carries a Stage column (S1-S5) enabling SEQUENCING RULE verification by sort: hypothesis
rows citing S1/S2 stage values is compliant; a hypothesis row with Stage = S0 or pre-declared
value is a visible violation. Grounded-in constraints are enforced at the column level:
hypothesis rows (Stage=S3) may reference only source rows where Stage in {S1,S2}. Provenance
tags become foreign-key references into the same table. Every governance artifact -- coverage
map, gate record, audit table, evidence table -- is a table, not prose.

**Hypothesis**: When every claim is a table row with a Stage column, SEQUENCING compliance
becomes machine-verifiable by sort. A hypothesis row that references a Stage S3 source is a
visible data error, not a prose-interpretation dispute. Provenance checking reduces to a
foreign-key join. Audit completeness is a row count, not a scan. Table-first format converts
compliance from an interpretive judgment into a mechanical check.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable after execution starts.

---

#### Rule Registry (all five rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+)]`
Every claim row in the Evidence Table carries a Stage column value and a Source-Stage label.
A row with a blank Stage value is unattributed. 70%+ of claim rows must carry stage labels.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+)]`
Confidence column values in the Evidence Table must vary across findings. A table where
every row in the Confidence column carries the same value fails calibration. At least two
distinct Confidence values must appear in rows where Stage in {S4, S5}.
Anti-uniformity guard: if min(Confidence) = max(Confidence) across S4/S5 rows, CALIBRATION fails.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+)]`
The Hypotheses Table carries a Falsification-Condition column and a Final-Status column.
A hypothesis row with a blank Falsification-Condition value fails this rule. Final-Status
values: Supported / Refuted / Indeterminate.

**SEQUENCING RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-)]`
The Evidence Table Stage column is the sequencing enforcement mechanism. Hypothesis rows
(Stage = S3) may reference only source rows where Stage in {S1, S2}. If any hypothesis
row's Source-Stage value is S3, S4, or S5, SEQUENCING fails.
Named principle (SEQUENCING RULE, formalized): "A hypothesis anchored before evidence
gathering is a bias, not a hypothesis." This principle is the reason the Stage column exists.

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+)]`
The Evidence Table Source-Stage column is the provenance enforcement mechanism.
In scope-restricted stages (S3, S4, S5), the Source-Stage column value must fall within
the role's declared access scope. Any row where Source-Stage is outside the role's authorized
scope is a charter violation detectable by column value, not prose interpretation.

Peer declaration: Five equal-tier rules. Adding a new peer rule adds a row to the coverage
map and a column to the invocation audit table. No static integer requires manual update.

---

#### Coverage Map (immutable -- row count = rule count; column count = stage count)

| Rule | S1 | S2 | S3 | S4 | S5 | + | - |
|------|----|----|----|----|----|---|---|
| ATTRIBUTION  | + | + | + | + | + | 5 | 0 |
| CALIBRATION  | - | - | - | + | + | 2 | 3 |
| FALSIFICATION| - | - | + | - | + | 2 | 3 |
| SEQUENCING   | + | + | + | - | - | 3 | 2 |
| PROVENANCE   | - | - | + | + | + | 3 | 2 |
| **Totals**   | 3 | 3 | 4 | 3 | 4 | **15** | **10** |

Invocation checksum: 25 artifacts = 15 positive + 10 negative. Derivable from table dimensions.
This map is sealed. Columns cannot be added or removed after any stage executes.

---

#### Gate Record Template (pre-instantiated blank table)

| Stage | Role | Entry Conditions | Entry Pass/Fail | Exit Conditions | Exit Pass/Fail |
|-------|------|-----------------|-----------------|-----------------|----------------|
| S1 | Web Evidence Collector | First stage | [ Pass ] | 6+ rows in Evidence Table with Stage=S1 and Source=external | [ ] |
| S2 | Intelligence Analyst | S1 exit Pass; Evidence Table has S1 rows | [ ] | S2 rows in Evidence Table; Landscape Summary row present | [ ] |
| S3 | Hypothesis Architect | S2 exit Pass; S1+S2 rows present | [ ] | Hypotheses Table has 3-5 rows; all have Falsification-Condition values; all Source-Stage in {S1,S2} | [ ] |
| S4 | Evidence Analyst | S3 exit Pass; Hypotheses Table present | [ ] | All S3 hypotheses have corresponding S4 analysis rows; 2+ Confidence values present | [ ] |
| S5 | Synthesis Director | S4 exit Pass; all prior tables present | [ ] | Synthesis Table complete; Consensus/Conflict rows distinguished; Decision-Readiness row present (one sentence) | [ ] |

---

#### Role Roster

| Stage | Role | Authorized Source-Stage Values |
|-------|------|-------------------------------|
| S1 | Web Evidence Collector | External (no prior-stage values) |
| S2 | Intelligence Analyst | S1 |
| S3 | Hypothesis Architect | S1, S2 |
| S4 | Evidence Analyst | S1, S2, S3 |
| S5 | Synthesis Director | S1, S2, S3, S4 |

---

#### Master Evidence Table Schema (pre-declared; rows added by each stage)

| Row-ID | Stage | Role | Claim | Source-Stage | Source-Artifact | Confidence | Type |
|--------|-------|------|-------|-------------|-----------------|------------|------|
| (blank -- rows added during execution) | | | | | | | |

Row types: Finding (S1/S2), Pattern (S2), Hypothesis (S3), Analysis (S4), Synthesis (S5).
Source-Stage must equal the stage that produced the artifact being cited.
Confidence values: High / Medium / Low / N/A (for S1 and S2 rows).

---

#### Hypotheses Table Schema (pre-declared; rows added by Stage 3)

| Hyp-ID | Claim | Source-Stage | Source-Artifact | Falsification-Condition | Confidence | Final-Status |
|--------|-------|-------------|-----------------|------------------------|------------|--------------|
| (blank -- rows added at Stage 3) | | | | | | |

Final-Status values: Supported / Refuted / Indeterminate. Source-Stage must be in {S1, S2}.

---

### STAGE EXECUTION

For each stage: fill the entry gate, run the invocations, produce output as table rows, fill
the exit gate, complete the handoff. Do not produce narrative-only output -- all findings are
table rows.

---

**Stage 1 -- Web Evidence Collector**

Entry gate conditions:
- [ Pass ] First stage -- automatic

Rule invocations [Stage 1 of 5]:

| Rule | Applicable | Invocation | Pass/Fail |
|------|-----------|------------|-----------|
| ATTRIBUTION [S1] | + | Are all S1 rows in Evidence Table labeled with Source=external? | [ Yes / No ] |
| CALIBRATION [S1] | - | Not applicable at evidence collection. | [ No ] |
| FALSIFICATION [S1] | - | Not applicable before hypothesis declaration. | [ No ] |
| SEQUENCING [S1] | + | Does Evidence Table contain zero S3/S4/S5 rows at this point? | [ Yes / No ] |
| PROVENANCE [S1] | - | Not applicable -- S1 is not scope-restricted. | [ No ] |

Execute: Add 6+ rows to Evidence Table with Stage=S1, Type=Finding, Source=external.
No hypothesis rows. No Stage column values other than S1.

Exit gate conditions:

| Condition | Pass/Fail |
|-----------|-----------|
| Evidence Table has 6+ rows with Stage=S1 | [ Pass / Fail ] |
| No rows with Stage=S3 present anywhere in tables | [ Pass / Fail ] |

> Role passes to: Stage 2 -- Intelligence Analyst.
> Authorized table access: Evidence Table rows where Stage=S1.

---

**Stage 2 -- Intelligence Analyst**

Entry gate:

| Condition | Pass/Fail |
|-----------|-----------|
| S1 exit all-Pass | [ Pass / Fail ] |
| Evidence Table has 6+ S1 rows | [ Pass / Fail ] |

Rule invocations [Stage 2 of 5]:

| Rule | Applicable | Invocation | Pass/Fail |
|------|-----------|------------|-----------|
| ATTRIBUTION [S2] | + | All new rows carry Stage=S2? | [ Yes / No ] |
| CALIBRATION [S2] | - | Not applicable at intelligence characterization. | [ No ] |
| FALSIFICATION [S2] | - | Not applicable before hypothesis declaration. | [ No ] |
| SEQUENCING [S2] | + | No hypothesis rows exist yet (no Stage=S3 rows)? | [ Yes / No ] |
| PROVENANCE [S2] | - | Not applicable -- S2 is not scope-restricted. | [ No ] |

Execute: Add rows to Evidence Table with Stage=S2, Type=Pattern. Add a Landscape Summary row
characterizing evidence strength, conflicts, and gaps across S1 findings. Source-Stage=S1 for
all pattern rows. No hypothesis rows.

Exit gate:

| Condition | Pass/Fail |
|-----------|-----------|
| Evidence Table has S2 rows with Source-Stage=S1 | [ Pass / Fail ] |
| Landscape Summary row present | [ Pass / Fail ] |
| No Stage=S3 rows in any table | [ Pass / Fail ] |

> Role passes to: Stage 3 -- Hypothesis Architect.
> Authorized table access: Evidence Table rows where Stage in {S1, S2}.

---

**Stage 3 -- Hypothesis Architect**

Entry gate:

| Condition | Pass/Fail |
|-----------|-----------|
| S2 exit all-Pass | [ Pass / Fail ] |
| Evidence Table has both S1 and S2 rows | [ Pass / Fail ] |

Rule invocations [Stage 3 of 5]:

| Rule | Applicable | Invocation | Pass/Fail |
|------|-----------|------------|-----------|
| ATTRIBUTION [S3] | + | All Hypotheses Table rows carry Stage=S3? | [ Yes / No ] |
| CALIBRATION [S3] | - | Not applicable before analysis. | [ No ] |
| FALSIFICATION [S3] | + | All Hypotheses Table rows have non-blank Falsification-Condition? | [ Yes / No ] |
| SEQUENCING [S3] | + | All Hypotheses Table Source-Stage values in {S1, S2}? | [ Yes / No ] |
| PROVENANCE [S3] | + | All Hypotheses Table Source-Stage values in {S1, S2} (role access scope)? | [ Yes / No ] |

Execute: Add 3-5 rows to Hypotheses Table. For each row, Source-Stage must be S1 or S2.
Every row must have a non-blank Falsification-Condition value and a Confidence value.

Exit gate:

| Condition | Pass/Fail |
|-----------|-----------|
| Hypotheses Table has 3-5 rows | [ Pass / Fail ] |
| All rows have non-blank Falsification-Condition | [ Pass / Fail ] |
| All Source-Stage values in {S1, S2} | [ Pass / Fail ] |

> Role passes to: Stage 4 -- Evidence Analyst.
> Authorized table access: Evidence Table rows where Stage in {S1, S2, S3}; full Hypotheses Table.

---

**Stage 4 -- Evidence Analyst**

Entry gate:

| Condition | Pass/Fail |
|-----------|-----------|
| S3 exit all-Pass | [ Pass / Fail ] |
| Hypotheses Table has 3-5 rows with Falsification-Conditions | [ Pass / Fail ] |

Rule invocations [Stage 4 of 5]:

| Rule | Applicable | Invocation | Pass/Fail |
|------|-----------|------------|-----------|
| ATTRIBUTION [S4] | + | All new S4 rows carry Stage=S4? | [ Yes / No ] |
| CALIBRATION [S4] | + | Do S4 rows carry at least 2 distinct Confidence values? | [ Yes / No ] |
| FALSIFICATION [S4] | - | Not applicable at analysis stage (governs S3 and S5). | [ No ] |
| SEQUENCING [S4] | - | Not applicable -- evidence-before-hypothesis ordering complete. | [ No ] |
| PROVENANCE [S4] | + | All S4 Source-Stage values in {S1, S2, S3}? | [ Yes / No ] |

Execute: For each hypothesis in Hypotheses Table, add analysis rows to Evidence Table with
Stage=S4. Include supporting evidence rows and counter-evidence rows. Vary Confidence values
across hypotheses (uniform Confidence across all S4 rows fails CALIBRATION). Source-Stage
must be in {S1, S2, S3}.

Exit gate:

| Condition | Pass/Fail |
|-----------|-----------|
| Each Hypotheses Table row has corresponding S4 Evidence Table rows | [ Pass / Fail ] |
| At least 2 distinct Confidence values across S4 rows | [ Pass / Fail ] |
| All S4 Source-Stage values in {S1, S2, S3} | [ Pass / Fail ] |

> Role passes to: Stage 5 -- Synthesis Director.
> Authorized table access: Evidence Table all rows; full Hypotheses Table.

---

**Stage 5 -- Synthesis Director**

Entry gate:

| Condition | Pass/Fail |
|-----------|-----------|
| S4 exit all-Pass | [ Pass / Fail ] |
| Evidence Table has S1, S2, S3, S4 rows | [ Pass / Fail ] |

Rule invocations [Stage 5 of 5]:

| Rule | Applicable | Invocation | Pass/Fail |
|------|-----------|------------|-----------|
| ATTRIBUTION [S5] | + | All S5 rows carry Stage=S5? | [ Yes / No ] |
| CALIBRATION [S5] | + | Confidence distribution varied (not uniform) across all S5 rows? | [ Yes / No ] |
| FALSIFICATION [S5] | + | All Hypotheses Table rows have non-blank Final-Status values? | [ Yes / No ] |
| SEQUENCING [S5] | - | Not applicable at synthesis. | [ No ] |
| PROVENANCE [S5] | + | All S5 Source-Stage values in {S1, S2, S3, S4}? | [ Yes / No ] |

Execute: Produce Synthesis Table rows with Stage=S5. Distinguish row types:
- Consensus (where S1 and S2 agree)
- Conflict (where S1 and S2 diverge -- name the specific conflict)
- Hypothesis-Verdict (final status for each hypothesis)
- Gap (what remains under-evidenced)
- Decision-Readiness (one-sentence posture statement -- this is a single row)

Update Hypotheses Table Final-Status column for all rows.

Exit gate:

| Condition | Pass/Fail |
|-----------|-----------|
| Synthesis Table has Consensus and Conflict rows | [ Pass / Fail ] |
| All Hypotheses Table Final-Status cells filled | [ Pass / Fail ] |
| Gap rows present in Synthesis Table | [ Pass / Fail ] |
| Exactly one Decision-Readiness row (one sentence) | [ Pass / Fail ] |
| All S5 Source-Stage values in {S1, S2, S3, S4} | [ Pass / Fail ] |

---

### OUTPUT ASSEMBLY

Assemble the final evidence brief in this order:

1. **Brief header**: title, topic, date
2. **Governance preamble** (this section, as finalized above)
3. **Filled gate record** (copy the gate table above with all cells filled)
4. **Master Evidence Table** (all rows, Stage=S1 through S5)
5. **Hypotheses Table** (all rows including Final-Status)
6. **Synthesis Table** (S5 rows)
7. **Consolidated invocation audit table**: 25 rows (one per coverage map cell); columns:
   Rule, Stage, Stage-Index, Applicable (+/-), Invocation question, Pass/Fail

**Delivery gate:** Count rows in the consolidated invocation audit table. Must equal 25.
A count != 25 is a delivery blocker. Do not publish this brief until the count equals 25.

---

---

## V-03 -- Axis: Lifecycle Emphasis (Dual-Phase Interrogatives at Every Governance-Checkable Stage)

**Variation axis**: Every applicable governance rule invocation is split into two temporally
separated checkpoints: (1) a pre-execution commitment check asking "Will X hold at this
stage? [Yes/No]" and (2) a post-execution verification check asking "Does X hold at this
stage? [Yes/No]". The pre-execution check is a commitment: the executor states intent before
the stage runs. The post-execution check is a verification: the executor confirms or
disconfirms the commitment against actual output. A "Yes" pre-execution followed by a "No"
post-execution is an intent-execution gap -- structurally visible as a two-row disagreement
in the invocation trail. Non-applicable invocations remain single-phase (no execution
commitment to split).

**Hypothesis**: Dual-phase interrogatives make intent-execution gaps visible even when the
executor answers "Yes" to the prospective check and then produces non-compliant output. The
post-execution verification must also be answered -- it cannot be skipped because the
pre-execution answer was "Yes." Two-phase invocations at every applicable stage convert the
governance trail from a static record of intent into a live comparison of intent vs. actuality.
A discrepancy between pre- and post-execution answers is a governance failure marker that
requires no interpretation.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable after execution starts.
This preamble contains the commitment architecture: all governance rules, the coverage map,
the dual-phase invocation structure, the gate record template, and the invocation checksum.
No element of this preamble may be modified after Stage 1 begins.

---

#### Rule Registry (all five rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+)]`
`[dual-phase: pre-execution commitment + post-execution verification at all 5 stages]`
At least 70% of material claims name their source stage. Stage labels: `[web]` S1,
`[intel]` S2, `[hypothesis]` S3, `[analysis]` S4, `[synthesis]` S5. An unlabeled claim
is an attribution gap.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+)]`
`[dual-phase: pre-execution commitment + post-execution verification at S4 and S5]`
Confidence ratings must vary across findings. Uniform ratings fail calibration.
Anti-uniformity guard: if all findings carry the same confidence level, calibration is
insufficient, regardless of whether the level is High, Medium, or Low.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+)]`
`[dual-phase: pre-execution commitment + post-execution verification at S3 and S5]`
Each hypothesis carries an explicit falsification condition. Final status at synthesis:
Supported / Refuted / Indeterminate. A hypothesis without a falsification condition is
a belief, not a hypothesis.

**SEQUENCING RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-)]`
`[dual-phase: pre-execution commitment + post-execution verification at S1, S2, S3]`
Evidence stages (S1, S2) complete before hypothesis declaration (S3). Named principle
(SEQUENCING RULE, formalized): "A hypothesis anchored before evidence gathering is a bias,
not a hypothesis." This principle is the reason this rule exists, encoded so any reader
can cite it by name.

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+)]`
`[dual-phase: pre-execution commitment + post-execution verification at S3, S4, S5]`
Every claim in a scope-restricted stage carries `[source: Stage N -- Artifact Name]`.
Scope-restricted stages: S3, S4, S5. A claim with no provenance tag is a structural gap.
A tag naming an out-of-scope artifact is a charter violation.

Peer declaration: Five equal-tier rules. No rule is primary. Coverage map auto-extends when
a new peer rule is added. Invocation checksum updates accordingly without static edits.

---

#### Dual-Phase Invocation Structure (all positive invocations are dual-phase)

Each positive invocation at an applicable stage has this structure:

```
[RULE NAME, Stage N of 5, PRE-EXECUTION]:
Will [rule condition] hold at this stage? [ Yes / No ]

... stage executes ...

[RULE NAME, Stage N of 5, POST-EXECUTION]:
Does [rule condition] hold in the output above? [ Yes / No ]
```

Negative invocations remain single-phase (no execution to split):

```
[RULE NAME, Stage N of 5]: Applicable at this stage? [ No -- reason ]
```

A pre-execution "Yes" followed by a post-execution "No" is an intent-execution gap.
The invocation trail records both answers. Gap is visible without interpretation.

---

#### Dual-Phase Coverage Map (positive = 2-phase; negative = 1-phase)

| Rule | S1 | S2 | S3 | S4 | S5 | + (2-phase) | - (1-phase) |
|------|----|----|----|----|----|-------------|-------------|
| ATTRIBUTION  | + | + | + | + | + | 5 | 0 |
| CALIBRATION  | - | - | - | + | + | 2 | 3 |
| FALSIFICATION| - | - | + | - | + | 2 | 3 |
| SEQUENCING   | + | + | + | - | - | 3 | 2 |
| PROVENANCE   | - | - | + | + | + | 3 | 2 |
| **Totals**   |   |   |   |   |   | **15** | **10** |

Positive invocations produce 2 artifacts each (pre + post). Negative invocations produce
1 artifact each. Total invocation artifacts: (15 x 2) + (10 x 1) = **40**.

Invocation checksum: **40 invocation artifacts = 30 dual-phase answers + 10 negative checks,
derived from: (15 positive x 2) + (10 negative x 1), where positive/negative counts derive
from 5 rules x 5 stages.** This count is derivable from map dimensions; adding a rule or
stage updates the checksum without static edits.

---

#### Gate Record Template (pre-instantiated blank)

| Stage | Role | Entry Gate | Entry Status | Exit Gate | Exit Status |
|-------|------|-----------|--------------|-----------|-------------|
| S1 | Web Evidence Collector | First stage | [ Pass ] | 6+ labeled findings; no hypothesis | [ ] |
| S2 | Intelligence Analyst | S1 exit all-Pass | [ ] | Landscape characterized; no hypothesis | [ ] |
| S3 | Hypothesis Architect | S2 exit all-Pass | [ ] | 3-5 hypotheses with falsification conditions; all claims carry provenance tags | [ ] |
| S4 | Evidence Analyst | S3 exit all-Pass | [ ] | All hypotheses analyzed; 2+ confidence levels; all claims carry provenance tags | [ ] |
| S5 | Synthesis Director | S4 exit all-Pass | [ ] | Synthesis complete; consensus/conflict separated; one-sentence decision verdict; all claims carry provenance tags | [ ] |

---

#### Role Roster and Access Scopes

| Stage | Role | Authorized Reads |
|-------|------|-----------------|
| S1 | Web Evidence Collector | External sources only |
| S2 | Intelligence Analyst | ARTIFACT-S1 (Web Findings Corpus) only |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Intelligence Assessment) only |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 (Hypothesis Register) only |
| S5 | Synthesis Director | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 + ARTIFACT-S4 (Evidence Analysis) only |

---

### STAGE EXECUTION

At each stage:
1. Fill entry gate (Pass/Fail each condition)
2. For every applicable rule: state the PRE-EXECUTION commitment check and answer
3. Execute the stage
4. For every applicable rule: state the POST-EXECUTION verification check and answer
5. For every non-applicable rule: state the single-phase negative invocation
6. Fill exit gate
7. Complete handoff declaration

If any post-execution answer is "No" when the pre-execution answer was "Yes": flag as an
INTENT-EXECUTION GAP. Document the discrepancy in the invocation trail. Do not suppress it.

---

**Stage 1 -- Web Evidence Collector**

Entry gate:
- [ Pass ] First stage -- automatic
- [ Pass ] No hypothesis stated anywhere

**PRE-EXECUTION COMMITMENT CHECKS [Stage 1 of 5]:**

ATTRIBUTION [S1 of 5, PRE-EXECUTION]:
Will all findings in Stage 1 be labeled `[web]`? [ Yes / No ]

SEQUENCING [S1 of 5, PRE-EXECUTION]:
Will Stage 1 complete without any hypothesis being stated? [ Yes / No ]

Non-applicable (single-phase, stated before execution):
CALIBRATION [S1 of 5]: Not applicable at evidence collection -- confidence governs analysis. [ No ]
FALSIFICATION [S1 of 5]: Not applicable before hypothesis declaration. [ No ]
PROVENANCE [S1 of 5]: Not applicable -- Stage 1 is not scope-restricted. [ No ]

Conduct structured web research on $ARGUMENTS. Collect 6+ findings from primary sources,
recent publications, technical references, and quantitative studies. Label every finding
`[web]`. Do not state hypotheses.

**POST-EXECUTION VERIFICATION CHECKS [Stage 1 of 5]:**

ATTRIBUTION [S1 of 5, POST-EXECUTION]:
Does the output above have all findings labeled `[web]`? [ Yes / No ]

SEQUENCING [S1 of 5, POST-EXECUTION]:
Does the output above contain zero hypothesis statements? [ Yes / No ]

Exit gate:
- [ ] 6+ findings, each labeled `[web]`
- [ ] No hypothesis stated in Stage 1 output

> Role passes to: Stage 2 -- Intelligence Analyst.
> ARTIFACT-S1 (Web Findings Corpus) transferred. Intelligence Analyst access scope: ARTIFACT-S1 only.

---

**Stage 2 -- Intelligence Analyst**

Entry gate:
- [ ] S1 exit all-Pass
- [ ] ARTIFACT-S1 received

**PRE-EXECUTION COMMITMENT CHECKS [Stage 2 of 5]:**

ATTRIBUTION [S2 of 5, PRE-EXECUTION]:
Will all new claims be labeled `[intel]`? [ Yes / No ]

SEQUENCING [S2 of 5, PRE-EXECUTION]:
Will Stage 2 complete without any hypothesis being stated? [ Yes / No ]

Non-applicable:
CALIBRATION [S2 of 5]: Not applicable at intelligence characterization. [ No ]
FALSIFICATION [S2 of 5]: Not applicable before hypothesis declaration. [ No ]
PROVENANCE [S2 of 5]: Not applicable -- Stage 2 is not scope-restricted. [ No ]

Apply expert judgment to ARTIFACT-S1: identify patterns, contradictions, evidence strength
(well-evidenced / thin / contested), and knowledge gaps. Label every new claim `[intel]`.
Do not state hypotheses.

**POST-EXECUTION VERIFICATION CHECKS [Stage 2 of 5]:**

ATTRIBUTION [S2 of 5, POST-EXECUTION]:
Does the output above have all new claims labeled `[intel]`? [ Yes / No ]

SEQUENCING [S2 of 5, POST-EXECUTION]:
Does the output above contain zero hypothesis statements? [ Yes / No ]

Exit gate:
- [ ] Evidence landscape characterized: patterns, conflicts, gaps named
- [ ] No hypothesis stated in Stage 2 output
- [ ] All new claims carry `[intel]` label

> Role passes to: Stage 3 -- Hypothesis Architect.
> ARTIFACT-S2 (Intelligence Assessment) transferred. Access scope: ARTIFACT-S1 + ARTIFACT-S2 only.

---

**Stage 3 -- Hypothesis Architect**

Entry gate:
- [ ] S2 exit all-Pass
- [ ] ARTIFACT-S1 + ARTIFACT-S2 available

**PRE-EXECUTION COMMITMENT CHECKS [Stage 3 of 5]:**

ATTRIBUTION [S3 of 5, PRE-EXECUTION]:
Will all hypotheses be labeled `[hypothesis]`? [ Yes / No ]

FALSIFICATION [S3 of 5, PRE-EXECUTION]:
Will every hypothesis carry an explicit falsification condition? [ Yes / No ]

SEQUENCING [S3 of 5, PRE-EXECUTION]:
Will all hypotheses be grounded exclusively in ARTIFACT-S1 and ARTIFACT-S2 evidence,
with no pre-evidence assumptions imported? [ Yes / No ]

PROVENANCE [S3 of 5, PRE-EXECUTION]:
Will every claim carry `[source: Stage N -- Artifact Name]` where N in {1,2}? [ Yes / No ]

Non-applicable:
CALIBRATION [S3 of 5]: Not applicable before analysis. [ No ]

Declare 3-5 hypotheses about $ARGUMENTS. Each hypothesis must:
1. State a specific claim
2. Carry `[source: Stage 1 -- Web Findings Corpus]` or `[source: Stage 2 -- Intelligence Assessment]`
3. Carry an explicit falsification condition
4. Carry a preliminary confidence level: High / Medium / Low
Label every claim `[hypothesis]`.

**POST-EXECUTION VERIFICATION CHECKS [Stage 3 of 5]:**

ATTRIBUTION [S3 of 5, POST-EXECUTION]:
Does every hypothesis above carry the `[hypothesis]` label? [ Yes / No ]

FALSIFICATION [S3 of 5, POST-EXECUTION]:
Does every hypothesis above carry an explicit falsification condition? [ Yes / No ]

SEQUENCING [S3 of 5, POST-EXECUTION]:
Do all hypotheses above cite only Stage 1 or Stage 2 artifacts -- no pre-evidence
sources, no Stage 3+ sources? [ Yes / No ]

PROVENANCE [S3 of 5, POST-EXECUTION]:
Does every claim above carry `[source: Stage N -- Artifact Name]` where N in {1,2}? [ Yes / No ]

Exit gate:
- [ ] 3-5 hypotheses with falsification conditions
- [ ] All claims labeled `[hypothesis]`
- [ ] All claims carry `[source: Stage N -- Artifact Name]` where N in {1,2}

> Role passes to: Stage 4 -- Evidence Analyst.
> ARTIFACT-S3 (Hypothesis Register) transferred. Access scope: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.

---

**Stage 4 -- Evidence Analyst**

Entry gate:
- [ ] S3 exit all-Pass
- [ ] ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 available

**PRE-EXECUTION COMMITMENT CHECKS [Stage 4 of 5]:**

ATTRIBUTION [S4 of 5, PRE-EXECUTION]:
Will all analysis findings be labeled `[analysis]`? [ Yes / No ]

CALIBRATION [S4 of 5, PRE-EXECUTION]:
Will at least two distinct confidence levels appear across the findings -- not all High,
not all Medium, not all Low? [ Yes / No ]

PROVENANCE [S4 of 5, PRE-EXECUTION]:
Will every claim carry `[source: Stage N -- Artifact Name]` where N in {1,2,3}? [ Yes / No ]

Non-applicable:
FALSIFICATION [S4 of 5]: Not applicable at analysis stage (governs S3 and S5). [ No ]
SEQUENCING [S4 of 5]: Not applicable -- evidence-before-hypothesis constraint is complete. [ No ]

Analyze each hypothesis from ARTIFACT-S3 against ARTIFACT-S1 and ARTIFACT-S2 evidence.
For each: summarize supporting evidence (cite artifact), summarize counter-evidence (cite
artifact), assign calibrated confidence. Confidence must vary -- uniform confidence across
all hypotheses fails CALIBRATION. Label every claim `[analysis]`.

**POST-EXECUTION VERIFICATION CHECKS [Stage 4 of 5]:**

ATTRIBUTION [S4 of 5, POST-EXECUTION]:
Does every finding above carry the `[analysis]` label? [ Yes / No ]

CALIBRATION [S4 of 5, POST-EXECUTION]:
Do the confidence ratings above contain at least two distinct values? [ Yes / No ]

PROVENANCE [S4 of 5, POST-EXECUTION]:
Does every claim above carry `[source: Stage N -- Artifact Name]` where N in {1,2,3}? [ Yes / No ]

Exit gate:
- [ ] All hypotheses from S3 addressed
- [ ] At least two distinct confidence levels used
- [ ] All claims labeled `[analysis]`
- [ ] All claims carry `[source: Stage N -- Artifact Name]` where N in {1,2,3}

> Role passes to: Stage 5 -- Synthesis Director.
> ARTIFACT-S4 (Evidence Analysis) transferred. Access scope: ARTIFACT-S1 through ARTIFACT-S4 only.

---

**Stage 5 -- Synthesis Director**

Entry gate:
- [ ] S4 exit all-Pass
- [ ] ARTIFACT-S1 through ARTIFACT-S4 available

**PRE-EXECUTION COMMITMENT CHECKS [Stage 5 of 5]:**

ATTRIBUTION [S5 of 5, PRE-EXECUTION]:
Will all synthesis claims be labeled `[synthesis]`? [ Yes / No ]

CALIBRATION [S5 of 5, PRE-EXECUTION]:
Will confidence ratings across synthesis findings be varied -- not uniformly identical? [ Yes / No ]

FALSIFICATION [S5 of 5, PRE-EXECUTION]:
Will every hypothesis from S3 receive a final status verdict (Supported/Refuted/Indeterminate)? [ Yes / No ]

PROVENANCE [S5 of 5, PRE-EXECUTION]:
Will every claim carry `[source: Stage N -- Artifact Name]` where N in {1,2,3,4}? [ Yes / No ]

Non-applicable:
SEQUENCING [S5 of 5]: Not applicable at synthesis. [ No ]

Produce a synthesis covering:
1. Consensus findings (where S1 and S2 agree -- cite artifacts)
2. Conflicts (where S1 and S2 diverge -- name the conflict explicitly, cite artifacts)
3. Hypothesis verdicts (final status for each, with rationale, cite artifacts)
4. Gaps and open questions (what remains under-evidenced after full campaign)
5. Decision readiness: one sentence naming posture, and if not ready, the specific gap

Label all claims `[synthesis]`. All claims carry `[source: Stage N -- Artifact Name]`.

**POST-EXECUTION VERIFICATION CHECKS [Stage 5 of 5]:**

ATTRIBUTION [S5 of 5, POST-EXECUTION]:
Does every claim above carry the `[synthesis]` label? [ Yes / No ]

CALIBRATION [S5 of 5, POST-EXECUTION]:
Does the confidence distribution above contain at least two distinct values? [ Yes / No ]

FALSIFICATION [S5 of 5, POST-EXECUTION]:
Does every hypothesis from Stage 3 have a final status verdict above? [ Yes / No ]

PROVENANCE [S5 of 5, POST-EXECUTION]:
Does every claim above carry `[source: Stage N -- Artifact Name]` where N in {1,2,3,4}? [ Yes / No ]

Exit gate:
- [ ] Consensus and conflict explicitly separated
- [ ] All hypotheses carry final status
- [ ] Gaps section present
- [ ] Decision readiness stated in one sentence
- [ ] All claims labeled `[synthesis]` with provenance tags

---

### OUTPUT ASSEMBLY

Assemble the final evidence brief:

1. **Brief header**: title, topic, date
2. **Governance preamble** (as above, sealed)
3. **Filled gate record** (all Pass/Fail cells completed)
4. **Stage 1 output** (S1 findings)
5. **Stage 2 output** (S2 patterns and landscape)
6. **Stage 3 output** (hypotheses with falsification conditions)
7. **Stage 4 output** (evidence analysis with calibrated confidence)
8. **Stage 5 output** (synthesis: consensus, conflict, verdicts, gaps, decision readiness)
9. **Consolidated invocation audit table**: rows for all 40 invocation artifacts; columns:
   Rule, Stage, Phase (PRE/POST/N-A), Applicable, Answer, Discrepancy flag

**Delivery gate:** Count rows in the consolidated invocation audit table. Must equal 40.
A count != 40 is a delivery blocker. If any row shows Pre=Yes / Post=No, flag as
INTENT-EXECUTION GAP and document before closing.

---

---

## V-04 -- Axis: Phrasing Register (RFC SHALL/MUST Formal Imperative)

**Variation axis**: Every governance obligation is stated as a numbered SHALL/MUST
requirement in RFC-style formal imperative language. Governance rules become requirement
statements (REQ-ATTR-01, REQ-CAL-01, etc.) with machine-verifiable compliance conditions.
Stage instructions are commands, not suggestions. The executor's compliance posture is
formal: every SHALL is a binding commitment. Passive compliance ("the executor may note..."),
hedged language ("it is recommended that..."), and aspirational framing ("the brief should
include...") are absent. What is required is stated as required; what is prohibited is stated
as prohibited.

**Hypothesis**: RFC-style imperative language converts aspirational criteria into binding
obligations. A brief constructed under SHALL/MUST phrasing cannot claim partial compliance
("mostly attributed") -- either a claim carries a stage label or it does not. Either an
invocation artifact exists or a SHALL has been violated. The register shift forces binary
compliance surfaces to remain binary rather than softening into prose judgments.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

The following requirements are binding. They are finalized before Stage 1 begins. They SHALL
NOT be modified after any stage executes. The executor SHALL treat each numbered requirement
as a verifiable obligation, not a guideline.

---

#### Requirement Set: Governance Rules

**REQ-ATTR-01 (ATTRIBUTION RULE)** `[applies at: S1, S2, S3, S4, S5]`
The executor SHALL label every material claim with its source stage. Stage labels are:
`[web]` for Stage 1, `[intel]` for Stage 2, `[hypothesis]` for Stage 3, `[analysis]` for
Stage 4, `[synthesis]` for Stage 5. An unlabeled material claim SHALL be treated as an
attribution violation. At least 70% of material claims MUST carry stage labels.

**REQ-CAL-01 (CALIBRATION RULE)** `[applies at: S4, S5]`
The executor SHALL assign varied confidence ratings across findings. Confidence ratings MUST
include at least two distinct values (e.g., High and Medium; Medium and Low). The executor
SHALL NOT assign uniform confidence ratings to all findings. If uniform ratings are produced,
the executor MUST regenerate with calibration applied before advancing.

**REQ-FAL-01 (FALSIFICATION RULE)** `[applies at: S3, S5]`
The executor SHALL include an explicit falsification condition with each hypothesis. A
falsification condition MUST be a stated criterion that would cause the hypothesis to be
rejected. The executor SHALL NOT declare a hypothesis without a falsification condition. At
synthesis, the executor SHALL assign each hypothesis a final status: Supported, Refuted,
or Indeterminate.

**REQ-SEQ-01 (SEQUENCING RULE)** `[applies at: S1, S2, S3]`
The executor SHALL complete evidence stages (S1, S2) before declaring any hypothesis (S3).
The executor SHALL NOT state any hypothesis in Stage 1 or Stage 2 output. The executor SHALL
NOT open Stage 3 until Stage 1 and Stage 2 exit gates are all-Pass. Named principle:
"A hypothesis anchored before evidence gathering is a bias, not a hypothesis." This principle
SHALL be encoded as a named rule (REQ-SEQ-01) referenceable by identifier.

**REQ-PROV-01 (PROVENANCE RULE)** `[applies at: S3, S4, S5]`
The executor SHALL include a provenance tag `[source: Stage N -- Artifact Name]` with every
claim produced in a scope-restricted stage (S3, S4, S5). A claim without a provenance tag in
a scope-restricted stage SHALL be treated as a structural gap. A provenance tag naming an
artifact outside the role's declared access scope SHALL be treated as a charter violation.

Peer declaration: REQ-ATTR-01, REQ-CAL-01, REQ-FAL-01, REQ-SEQ-01, REQ-PROV-01 are
equal-tier requirements. No requirement is primary. Adding a new peer requirement SHALL
propagate automatically through the coverage map. The executor SHALL NOT require manual
updates to static integers when a new rule is added.

---

#### Coverage Map (immutable -- sealed before Stage 1)

| Requirement | S1 | S2 | S3 | S4 | S5 |
|------------|----|----|----|----|----|
| REQ-ATTR-01 | SHALL | SHALL | SHALL | SHALL | SHALL |
| REQ-CAL-01  | N/A  | N/A  | N/A  | SHALL | SHALL |
| REQ-FAL-01  | N/A  | N/A  | SHALL | N/A  | SHALL |
| REQ-SEQ-01  | SHALL | SHALL | SHALL | N/A  | N/A  |
| REQ-PROV-01 | N/A  | N/A  | SHALL | SHALL | SHALL |

SHALL count: 15. N/A count: 10. Total invocation artifacts: 25 (derived from 5 req x 5
stages). This map is finalized before Stage 1 begins. The executor SHALL NOT modify it.

---

#### Gate Record Template

| Stage | Role | Entry: SHALL conditions | Entry | Exit: SHALL conditions | Exit |
|-------|------|------------------------|-------|------------------------|------|
| S1 | Web Evidence Collector | First stage -- auto-Pass | [ Pass ] | SHALL produce 6+ labeled findings; SHALL NOT state hypothesis | [ ] |
| S2 | Intelligence Analyst | S1 exit SHALL be all-Pass | [ ] | SHALL characterize evidence landscape; SHALL NOT state hypothesis | [ ] |
| S3 | Hypothesis Architect | S2 exit SHALL be all-Pass | [ ] | SHALL produce 3-5 hypotheses with falsification conditions; SHALL include provenance tags | [ ] |
| S4 | Evidence Analyst | S3 exit SHALL be all-Pass | [ ] | SHALL analyze all hypotheses; SHALL use 2+ confidence values; SHALL include provenance tags | [ ] |
| S5 | Synthesis Director | S4 exit SHALL be all-Pass | [ ] | SHALL separate consensus from conflict; SHALL assign hypothesis verdicts; SHALL include one-sentence decision readiness; SHALL include provenance tags | [ ] |

---

#### Role Roster

| Stage | Role | Access Scope |
|-------|------|-------------|
| S1 | Web Evidence Collector | External sources ONLY. The executor SHALL NOT access prior-stage artifacts (none exist). |
| S2 | Intelligence Analyst | ARTIFACT-S1 ONLY. The executor SHALL NOT access external sources beyond Stage 1 corpus. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 ONLY. The executor SHALL NOT import pre-evidence assumptions. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 ONLY. The executor SHALL NOT access new external sources. |
| S5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 ONLY. The executor SHALL NOT introduce new external sources at synthesis. |

---

### STAGE EXECUTION REQUIREMENTS

The executor SHALL follow this protocol at every stage:
1. SHALL verify entry gate conditions before beginning
2. SHALL record a binary invocation artifact for every rule (SHALL or N/A)
3. SHALL execute stage in accordance with the stage specification
4. SHALL verify exit gate conditions before handoff
5. SHALL complete handoff declaration before the next stage opens

The executor SHALL NOT skip gate verification. The executor SHALL NOT advance to Stage N+1
before Stage N exit gate is all-Pass. The executor SHALL NOT modify the preamble after
Stage 1 begins.

---

**Stage 1 -- Web Evidence Collector**

Entry gate:
- [ Pass ] REQ-ENTRY-S1: First stage -- no prior stages required.

Invocations [Stage 1 of 5]:
- REQ-ATTR-01 [S1 of 5]: All S1 findings SHALL carry `[web]` label. All labeled? [ Yes / No ]
- REQ-CAL-01 [S1 of 5]: N/A -- REQ-CAL-01 SHALL NOT be invoked at evidence collection. [ N/A ]
- REQ-FAL-01 [S1 of 5]: N/A -- REQ-FAL-01 SHALL NOT be invoked before hypothesis declaration. [ N/A ]
- REQ-SEQ-01 [S1 of 5]: No hypothesis SHALL exist at this point. Stage 1 running pre-hypothesis? [ Yes / No ]
- REQ-PROV-01 [S1 of 5]: N/A -- REQ-PROV-01 SHALL NOT be invoked at non-scope-restricted stages. [ N/A ]

The executor SHALL conduct structured web research on $ARGUMENTS. The executor SHALL collect
a minimum of 6 findings from primary sources, recent publications, technical references, and
quantitative studies. The executor SHALL label every finding `[web]`. The executor SHALL NOT
state any hypothesis in Stage 1 output.

Exit gate:
- [ ] REQ-EXIT-S1a: 6+ findings, all labeled `[web]`
- [ ] REQ-EXIT-S1b: Zero hypothesis statements in Stage 1 output

> **HANDOFF: Role passes to Stage 2 -- Intelligence Analyst.**
> ARTIFACT-S1 (Web Findings Corpus) is transferred.
> Intelligence Analyst access scope: ARTIFACT-S1 ONLY.

---

**Stage 2 -- Intelligence Analyst**

Entry gate:
- [ ] REQ-ENTRY-S2a: S1 exit gate SHALL be all-Pass before Stage 2 opens.
- [ ] REQ-ENTRY-S2b: No hypothesis SHALL have been stated at any prior point.

Invocations [Stage 2 of 5]:
- REQ-ATTR-01 [S2 of 5]: All S2 claims SHALL carry `[intel]` label. All labeled? [ Yes / No ]
- REQ-CAL-01 [S2 of 5]: N/A -- REQ-CAL-01 SHALL NOT be invoked at intelligence characterization. [ N/A ]
- REQ-FAL-01 [S2 of 5]: N/A -- REQ-FAL-01 SHALL NOT be invoked before hypothesis declaration. [ N/A ]
- REQ-SEQ-01 [S2 of 5]: No hypothesis SHALL exist at this point. Still pre-hypothesis? [ Yes / No ]
- REQ-PROV-01 [S2 of 5]: N/A -- REQ-PROV-01 SHALL NOT be invoked at Stage 2. [ N/A ]

The executor SHALL apply expert judgment to ARTIFACT-S1: characterize patterns,
contradictions, evidence strength (well-evidenced / thin / contested), and knowledge gaps.
The executor SHALL label every new claim `[intel]`. The executor SHALL NOT state any
hypothesis in Stage 2 output. The executor SHALL draw only on ARTIFACT-S1.

Exit gate:
- [ ] REQ-EXIT-S2a: Evidence landscape characterized with patterns, conflicts, gaps named
- [ ] REQ-EXIT-S2b: Zero hypothesis statements in Stage 2 output
- [ ] REQ-EXIT-S2c: All new claims carry `[intel]` label

> **HANDOFF: Role passes to Stage 3 -- Hypothesis Architect.**
> ARTIFACT-S2 (Intelligence Assessment) is transferred.
> Hypothesis Architect access scope: ARTIFACT-S1 + ARTIFACT-S2 ONLY.

---

**Stage 3 -- Hypothesis Architect**

Entry gate:
- [ ] REQ-ENTRY-S3a: S2 exit gate SHALL be all-Pass before Stage 3 opens.
- [ ] REQ-ENTRY-S3b: ARTIFACT-S1 + ARTIFACT-S2 SHALL be available.

Invocations [Stage 3 of 5]:
- REQ-ATTR-01 [S3 of 5]: All hypotheses SHALL carry `[hypothesis]` label. All labeled? [ Yes / No ]
- REQ-CAL-01 [S3 of 5]: N/A -- REQ-CAL-01 SHALL NOT be invoked before analysis stages. [ N/A ]
- REQ-FAL-01 [S3 of 5]: Every hypothesis SHALL carry an explicit falsification condition. All present? [ Yes / No ]
- REQ-SEQ-01 [S3 of 5]: All hypotheses SHALL be grounded in S1/S2 evidence exclusively. No pre-evidence anchors? [ Yes / No ]
- REQ-PROV-01 [S3 of 5]: Every claim SHALL carry `[source: Stage N -- Artifact Name]` where N in {1,2}. All tagged? [ Yes / No ]

The executor SHALL declare 3-5 hypotheses about $ARGUMENTS. Each hypothesis SHALL:
1. State a specific falsifiable claim
2. Carry `[source: Stage 1 -- Web Findings Corpus]` or `[source: Stage 2 -- Intelligence Assessment]`
3. Carry an explicit falsification condition
4. Carry a preliminary confidence level (High / Medium / Low)
5. Carry the `[hypothesis]` label

The executor SHALL NOT import any assumption that predates Stage 1 evidence.

Exit gate:
- [ ] REQ-EXIT-S3a: 3-5 hypotheses produced
- [ ] REQ-EXIT-S3b: All hypotheses carry explicit falsification conditions
- [ ] REQ-EXIT-S3c: All claims carry `[hypothesis]` label
- [ ] REQ-EXIT-S3d: All claims carry `[source: Stage N -- Artifact Name]` where N in {1,2}

> **HANDOFF: Role passes to Stage 4 -- Evidence Analyst.**
> ARTIFACT-S3 (Hypothesis Register) is transferred.
> Evidence Analyst access scope: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 ONLY.

---

**Stage 4 -- Evidence Analyst**

Entry gate:
- [ ] REQ-ENTRY-S4a: S3 exit gate SHALL be all-Pass.
- [ ] REQ-ENTRY-S4b: Hypotheses Table SHALL have 3-5 rows with falsification conditions.

Invocations [Stage 4 of 5]:
- REQ-ATTR-01 [S4 of 5]: All analysis claims SHALL carry `[analysis]` label. All labeled? [ Yes / No ]
- REQ-CAL-01 [S4 of 5]: At least 2 distinct confidence levels SHALL appear across findings. Present? [ Yes / No ]
- REQ-FAL-01 [S4 of 5]: N/A -- REQ-FAL-01 SHALL NOT be invoked at analysis stage. [ N/A ]
- REQ-SEQ-01 [S4 of 5]: N/A -- evidence-before-hypothesis constraint SHALL be considered complete. [ N/A ]
- REQ-PROV-01 [S4 of 5]: Every claim SHALL carry `[source: Stage N -- Artifact Name]` where N in {1,2,3}. All tagged? [ Yes / No ]

The executor SHALL analyze each hypothesis from ARTIFACT-S3 against evidence in ARTIFACT-S1
and ARTIFACT-S2. The executor SHALL summarize supporting evidence (cite artifact), counter-
evidence (cite artifact), and SHALL assign a calibrated confidence level. Confidence SHALL
vary across hypotheses -- the executor SHALL NOT assign identical confidence to all findings.
The executor SHALL label every claim `[analysis]`.

Exit gate:
- [ ] REQ-EXIT-S4a: All S3 hypotheses addressed
- [ ] REQ-EXIT-S4b: At least 2 distinct confidence levels used
- [ ] REQ-EXIT-S4c: All claims carry `[analysis]` label
- [ ] REQ-EXIT-S4d: All claims carry `[source: Stage N -- Artifact Name]` where N in {1,2,3}

> **HANDOFF: Role passes to Stage 5 -- Synthesis Director.**
> ARTIFACT-S4 (Evidence Analysis) is transferred.
> Synthesis Director access scope: ARTIFACT-S1 through ARTIFACT-S4 ONLY.

---

**Stage 5 -- Synthesis Director**

Entry gate:
- [ ] REQ-ENTRY-S5a: S4 exit gate SHALL be all-Pass.
- [ ] REQ-ENTRY-S5b: ARTIFACT-S1 through ARTIFACT-S4 SHALL be available.

Invocations [Stage 5 of 5]:
- REQ-ATTR-01 [S5 of 5]: All synthesis claims SHALL carry `[synthesis]` label. All labeled? [ Yes / No ]
- REQ-CAL-01 [S5 of 5]: Confidence distribution SHALL be varied -- not uniform -- across final findings. Varied? [ Yes / No ]
- REQ-FAL-01 [S5 of 5]: Every hypothesis SHALL receive a final status verdict. All assigned? [ Yes / No ]
- REQ-SEQ-01 [S5 of 5]: N/A -- sequencing constraint SHALL be considered complete at synthesis. [ N/A ]
- REQ-PROV-01 [S5 of 5]: Every claim SHALL carry `[source: Stage N -- Artifact Name]` where N in {1,2,3,4}. All tagged? [ Yes / No ]

The executor SHALL produce a synthesis covering:
1. Consensus findings -- where S1 and S2 agree (cite ARTIFACT-S1/S2)
2. Conflicts -- where S1 and S2 diverge; the executor SHALL name each conflict explicitly
3. Hypothesis verdicts -- final status for each hypothesis (Supported/Refuted/Indeterminate)
4. Gaps and open questions -- what remains under-evidenced after the full campaign
5. Decision readiness -- exactly one sentence naming posture; if not ready, name the gap

The executor SHALL label all claims `[synthesis]`. The executor SHALL include provenance tags
on all claims. The executor SHALL NOT produce a multi-paragraph decision readiness section;
the compression to one sentence is itself a required output property.

Exit gate:
- [ ] REQ-EXIT-S5a: Consensus and conflict explicitly separated
- [ ] REQ-EXIT-S5b: All hypotheses carry final status verdicts
- [ ] REQ-EXIT-S5c: Gaps section present
- [ ] REQ-EXIT-S5d: Decision readiness stated in exactly one sentence
- [ ] REQ-EXIT-S5e: All claims carry `[synthesis]` and `[source: Stage N -- Artifact Name]`

---

### OUTPUT ASSEMBLY REQUIREMENTS

The executor SHALL assemble the final evidence brief with these required sections:

1. **Brief header** (required): title, topic, date, stages run
2. **Governance preamble** (required): this section, as sealed
3. **Filled gate record** (required): all Pass/Fail cells completed
4. **Stage outputs** (required): S1 through S5 in order
5. **Consolidated invocation audit table** (required): 25 rows (one per coverage map cell);
   columns: Requirement, Stage, Stage-Index, Applicable (SHALL/N/A), Pass/Fail
6. **Synthesis narrative** (required): consensus, conflicts, hypothesis verdicts
7. **Gaps and open questions** (required)
8. **Decision readiness** (required): one sentence

**Delivery gate:** The executor SHALL count rows in the consolidated invocation audit table.
The count MUST equal 25. A count != 25 SHALL be treated as a delivery blocker. The executor
SHALL NOT close or deliver this brief until the audit table contains exactly 25 rows.

---

---

## V-05 -- Combination: Output Format + Dual-Phase Interrogatives + Provenance Activation at Handoff Boundary

**Variation axes combined:**
1. **Output Format** (V-02): Table-first, stage-indexed, machine-verifiable column encoding
2. **Lifecycle Emphasis** (V-03): Dual-phase interrogatives (pre-execution commitment + post-execution verification at every applicable stage)
3. **Provenance Activation at Handoff Boundary** (Signal 2 from R12 V-05 PASS+): The PROVENANCE RULE is not activated in the role charter. It is activated exclusively at the handoff boundary immediately preceding each scope-restricted stage. The handoff block enumerates authorized artifacts AND activates provenance checking at the transfer event.

**Hypothesis**: Combining table-first encoding (makes SEQUENCING violations sort-detectable),
dual-phase interrogatives (makes intent-execution gaps visible in the invocation trail), and
handoff-boundary provenance activation (makes the provenance rule live at the moment of
transfer, not in a static charter) produces a brief where every structural gap surfaces as a
visible artifact deficiency -- a missing table row, a pre/post answer discrepancy, or an
absent handoff activation block -- rather than an interpretation dispute. The three axes
are complementary: format makes compliance mechanical, lifecycle makes failures temporally
pinned, handoff activation makes authority-granting an explicit event.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable -- cannot be modified after execution starts.
This preamble contains: rule declarations (with inline scope and dual-phase applicability),
coverage map, dual-phase invocation architecture, gate record template (blank), role roster
(access scope only -- provenance NOT activated here), and invocation checksum.

Provenance activation occurs at handoff boundaries, not here.

---

#### Rule Registry (all five rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+)]`
`[dual-phase at all 5 stages: pre-execution commitment + post-execution verification]`
Every row in the Evidence Table carries a Stage column value. Unlabeled rows are
attribution violations. 70%+ of claim rows must carry stage labels.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+)]`
`[dual-phase at S4, S5: pre-execution commitment + post-execution verification]`
Confidence column values in the Evidence Table must vary. At S4 and S5: min(Confidence)
MUST NOT equal max(Confidence) across rows. Uniform Confidence values fail this rule.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+)]`
`[dual-phase at S3, S5: pre-execution commitment + post-execution verification]`
Hypotheses Table Falsification-Condition column must be non-blank for all rows.
Final-Status column must be non-blank at Stage 5. Values: Supported/Refuted/Indeterminate.

**SEQUENCING RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-)]`
`[dual-phase at S1, S2, S3: pre-execution commitment + post-execution verification]`
Stage column in Evidence Table is the sequencing enforcement mechanism. Hypothesis rows
(Stage=S3) may only reference Source-Stage values in {S1, S2}. Any Source-Stage=S3 on a
row that is itself Stage=S3 is a sequencing violation.
Named principle (SEQUENCING RULE): "A hypothesis anchored before evidence gathering is
a bias, not a hypothesis."

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+)]`
`[dual-phase at S3, S4, S5: pre-execution commitment + post-execution verification]`
**THIS RULE IS NOT ACTIVATED HERE.** It is activated exclusively at the handoff boundary
immediately preceding each scope-restricted stage. The handoff block enumerates authorized
artifacts and activates provenance checking at the transfer moment. Scope-restricted stages:
S3, S4, S5. Every row produced by these stages must carry Source-Stage and Source-Artifact
column values within the role's authorized scope.

Peer declaration: Five equal-tier rules. No rule is primary. Adding a peer rule extends
the coverage map automatically. No static integer requires manual update.

---

#### Dual-Phase Coverage Map (+ = dual-phase; - = single-phase negative)

| Rule | S1 | S2 | S3 | S4 | S5 | + (dual) | - (single) |
|------|----|----|----|----|----|----------|------------|
| ATTRIBUTION  | + | + | + | + | + | 5 | 0 |
| CALIBRATION  | - | - | - | + | + | 2 | 3 |
| FALSIFICATION| - | - | + | - | + | 2 | 3 |
| SEQUENCING   | + | + | + | - | - | 3 | 2 |
| PROVENANCE   | - | - | + | + | + | 3 | 2 |
| **Totals**   | 3 | 3 | 4 | 3 | 4 | **15** | **10** |

Dual-phase invocations produce 2 artifacts each (pre + post).
Single-phase negatives produce 1 artifact each.
Total invocation artifacts: (15 x 2) + (10 x 1) = **40**.
Checksum: **40 invocation artifacts = 30 dual-phase answers + 10 negative checks**,
derived from (positive count x 2) + (negative count x 1). Derivable from map; no static
integer stored independently.

---

#### Gate Record Template (pre-instantiated blank)

| Stage | Role | Entry | Entry-Status | Exit | Exit-Status |
|-------|------|-------|--------------|------|-------------|
| S1 | Web Evidence Collector | First stage | [ Pass ] | 6+ Evidence Table rows with Stage=S1; no Stage=S3 rows anywhere | [ ] |
| S2 | Intelligence Analyst | S1 exit all-Pass; handoff S1-S2 complete | [ ] | S2 rows in Evidence Table; Landscape Summary row; no Stage=S3 rows | [ ] |
| S3 | Hypothesis Architect | S2 exit all-Pass; handoff S2-S3 complete; PROVENANCE activated at boundary | [ ] | Hypotheses Table: 3-5 rows; Falsification-Condition non-blank; all Source-Stage in {S1,S2} | [ ] |
| S4 | Evidence Analyst | S3 exit all-Pass; handoff S3-S4 complete; PROVENANCE activated at boundary | [ ] | S4 analysis rows; 2+ distinct Confidence values; all Source-Stage in {S1,S2,S3} | [ ] |
| S5 | Synthesis Director | S4 exit all-Pass; handoff S4-S5 complete; PROVENANCE activated at boundary | [ ] | Synthesis rows; Consensus+Conflict rows; all Final-Status filled; Decision-Readiness row (1 sentence); all Source-Stage in {S1,S2,S3,S4} | [ ] |

---

#### Role Roster (access scope only; provenance activation at handoff, not here)

| Stage | Role | Authorized Source-Stage Values |
|-------|------|-------------------------------|
| S1 | Web Evidence Collector | External (no prior-stage rows) |
| S2 | Intelligence Analyst | S1 |
| S3 | Hypothesis Architect | S1, S2 |
| S4 | Evidence Analyst | S1, S2, S3 |
| S5 | Synthesis Director | S1, S2, S3, S4 |

Note: Provenance checking for S3/S4/S5 is activated at the handoff boundary preceding each
stage. The role roster declares access scope for reference; the enforcement event is the
handoff block.

---

#### Master Evidence Table Schema (pre-declared; rows added by all stages)

| Row-ID | Stage | Role | Claim | Source-Stage | Source-Artifact | Confidence | Row-Type |
|--------|-------|------|-------|-------------|-----------------|------------|----------|
| (blank -- populated during execution) | | | | | | | |

Row-Types: Finding (S1), Pattern (S2), Hypothesis (S3 -- in Hypotheses Table), Analysis (S4), Synthesis (S5).
Sequencing check: sort by Stage column; no S3 row should have Source-Stage outside {S1, S2}.
Provenance check: for S3/S4/S5 rows, Source-Stage must be within role's authorized scope.

---

#### Hypotheses Table Schema (pre-declared; rows added by Stage 3)

| Hyp-ID | Stage | Claim | Source-Stage | Source-Artifact | Falsification-Condition | Confidence | Final-Status |
|--------|-------|-------|-------------|-----------------|------------------------|------------|--------------|
| (blank -- populated at Stage 3) | | | | | | | |

Final-Status values: Supported / Refuted / Indeterminate.

---

### STAGE EXECUTION

Protocol per stage:
1. Verify entry gate (fill Pass/Fail for each condition)
2. State PRE-EXECUTION commitment for each applicable rule (before adding any rows)
3. Add table rows / produce stage output
4. State POST-EXECUTION verification for each applicable rule
5. State single-phase negative for each non-applicable rule
6. Fill exit gate
7. Complete handoff declaration (includes PROVENANCE RULE activation if next stage is S3/S4/S5)

---

**Stage 1 -- Web Evidence Collector**

Entry gate:
- [ Pass ] First stage -- no prerequisites

**PRE-EXECUTION [Stage 1 of 5]:**
ATTRIBUTION [S1, PRE]: Will all S1 rows carry Stage=S1? [ Yes / No ]
SEQUENCING [S1, PRE]: Will zero Hypothesis rows (Stage=S3) be created at this stage? [ Yes / No ]

Add 6+ rows to Evidence Table with Stage=S1, Row-Type=Finding, Source-Stage=External.

**POST-EXECUTION [Stage 1 of 5]:**
ATTRIBUTION [S1, POST]: Do all rows above carry Stage=S1? [ Yes / No ]
SEQUENCING [S1, POST]: Are there zero Stage=S3 rows in any table? [ Yes / No ]

Non-applicable:
CALIBRATION [S1]: Not applicable at evidence collection. [ No ]
FALSIFICATION [S1]: Not applicable before hypothesis declaration. [ No ]
PROVENANCE [S1]: Not activated -- Stage 1 is not scope-restricted. [ No ]

Exit gate:
- [ ] Evidence Table has 6+ rows with Stage=S1
- [ ] Zero rows with Stage=S3 anywhere

**HANDOFF DECLARATION -- S1 to S2:**

> **Role passes to: Stage 2 -- Intelligence Analyst.**
> Artifacts transferred: Evidence Table rows where Stage=S1 (ARTIFACT-S1).
> Intelligence Analyst authorized Source-Stage values: {S1}.
> External sources and pre-Stage-1 information are outside authorized scope.
> PROVENANCE RULE status: Not activated. Stage 2 is not scope-restricted.

---

**Stage 2 -- Intelligence Analyst**

Entry gate:
- [ ] S1 exit all-Pass
- [ ] Handoff S1-to-S2 complete
- [ ] Evidence Table has S1 rows

**PRE-EXECUTION [Stage 2 of 5]:**
ATTRIBUTION [S2, PRE]: Will all new S2 rows carry Stage=S2? [ Yes / No ]
SEQUENCING [S2, PRE]: Will zero Hypothesis rows (Stage=S3) be created at this stage? [ Yes / No ]

Apply expert judgment to S1 rows in Evidence Table. Add S2 rows: Pattern rows and a
Landscape Summary row characterizing evidence strength, conflicts, and gaps. Source-Stage=S1
for all S2 rows. Do not create Stage=S3 rows.

**POST-EXECUTION [Stage 2 of 5]:**
ATTRIBUTION [S2, POST]: Do all new rows carry Stage=S2? [ Yes / No ]
SEQUENCING [S2, POST]: Are there zero Stage=S3 rows in any table? [ Yes / No ]

Non-applicable:
CALIBRATION [S2]: Not applicable. [ No ]
FALSIFICATION [S2]: Not applicable. [ No ]
PROVENANCE [S2]: Not activated -- Stage 2 is not scope-restricted. [ No ]

Exit gate:
- [ ] Evidence Table has S2 rows with Source-Stage=S1
- [ ] Landscape Summary row present
- [ ] Zero Stage=S3 rows in any table

**HANDOFF DECLARATION -- S2 to S3:**

> **Role passes to: Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: Evidence Table rows where Stage in {S1, S2} (ARTIFACT-S1 + ARTIFACT-S2).
> Hypothesis Architect authorized Source-Stage values: {S1, S2}.
> Any hypothesis row citing Source-Stage outside {S1, S2} is a charter violation.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 3 is scope-restricted. Every row produced by the Hypothesis Architect must carry
> non-blank Source-Stage and Source-Artifact column values within {S1, S2}. A row with blank
> Source-Stage in the Hypotheses Table is a structural gap that must be resolved before the
> S3 exit gate can pass. A row with Source-Stage outside {S1, S2} is a visible charter
> violation. Provenance enforcement is live from this boundary forward for Stage 3 output.

---

**Stage 3 -- Hypothesis Architect**

Entry gate:
- [ ] S2 exit all-Pass
- [ ] Handoff S2-to-S3 complete
- [ ] PROVENANCE RULE activation block present in handoff S2-to-S3

**PRE-EXECUTION [Stage 3 of 5]:**
ATTRIBUTION [S3, PRE]: Will all Hypotheses Table rows carry Stage=S3? [ Yes / No ]
FALSIFICATION [S3, PRE]: Will all Hypotheses Table rows carry non-blank Falsification-Condition? [ Yes / No ]
SEQUENCING [S3, PRE]: Will all Hypotheses Table Source-Stage values be in {S1, S2}? [ Yes / No ]
PROVENANCE [S3, PRE]: Will all Hypotheses Table rows carry non-blank Source-Stage and Source-Artifact in {S1, S2}? [ Yes / No ]

Add 3-5 rows to Hypotheses Table. Each row must have:
- Stage=S3
- Claim (specific falsifiable statement)
- Source-Stage in {S1, S2}
- Source-Artifact name (e.g., "Web Findings Corpus" or "Intelligence Assessment")
- Non-blank Falsification-Condition
- Confidence value (High/Medium/Low)
- Final-Status = blank (to be filled at Stage 5)

**POST-EXECUTION [Stage 3 of 5]:**
ATTRIBUTION [S3, POST]: Do all Hypotheses Table rows carry Stage=S3? [ Yes / No ]
FALSIFICATION [S3, POST]: Do all rows carry non-blank Falsification-Condition? [ Yes / No ]
SEQUENCING [S3, POST]: Do all Source-Stage values fall within {S1, S2}? [ Yes / No ]
PROVENANCE [S3, POST]: Do all rows carry non-blank Source-Stage and Source-Artifact in {S1, S2}? [ Yes / No ]

Non-applicable:
CALIBRATION [S3]: Not applicable before analysis. [ No ]

Exit gate:
- [ ] Hypotheses Table has 3-5 rows
- [ ] All rows have non-blank Falsification-Condition
- [ ] All Source-Stage values in {S1, S2}
- [ ] PROVENANCE RULE compliance verified via POST-EXECUTION check above

**HANDOFF DECLARATION -- S3 to S4:**

> **Role passes to: Stage 4 -- Evidence Analyst.**
> Artifacts transferred: Evidence Table rows Stage in {S1,S2}, Hypotheses Table (ARTIFACT-S3).
> Evidence Analyst authorized Source-Stage values: {S1, S2, S3}.
> Any S4 row citing Source-Stage outside {S1, S2, S3} is a charter violation.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 4 is scope-restricted. Every row produced by the Evidence Analyst must carry
> non-blank Source-Stage in {S1, S2, S3} and a named Source-Artifact. A row with blank
> Source-Stage is a structural gap. Provenance enforcement is live for Stage 4 output.

---

**Stage 4 -- Evidence Analyst**

Entry gate:
- [ ] S3 exit all-Pass
- [ ] Handoff S3-to-S4 complete
- [ ] PROVENANCE RULE activation block present in handoff S3-to-S4

**PRE-EXECUTION [Stage 4 of 5]:**
ATTRIBUTION [S4, PRE]: Will all S4 rows carry Stage=S4? [ Yes / No ]
CALIBRATION [S4, PRE]: Will at least 2 distinct Confidence values appear in S4 rows? [ Yes / No ]
PROVENANCE [S4, PRE]: Will all S4 rows carry non-blank Source-Stage in {S1, S2, S3}? [ Yes / No ]

Add analysis rows to Evidence Table for each hypothesis in Hypotheses Table.
For each hypothesis: add supporting-evidence row(s) with Source-Stage in {S1,S2,S3}, counter-
evidence row(s) with Source-Stage in {S1,S2,S3}, and assign a calibrated Confidence value.
Confidence must vary -- if all S4 rows carry the same Confidence value, CALIBRATION fails.

**POST-EXECUTION [Stage 4 of 5]:**
ATTRIBUTION [S4, POST]: Do all new rows carry Stage=S4? [ Yes / No ]
CALIBRATION [S4, POST]: Do S4 rows contain at least 2 distinct Confidence values? [ Yes / No ]
PROVENANCE [S4, POST]: Do all S4 rows carry non-blank Source-Stage in {S1, S2, S3}? [ Yes / No ]

Non-applicable:
FALSIFICATION [S4]: Not applicable at analysis stage. [ No ]
SEQUENCING [S4]: Not applicable -- ordering constraint complete. [ No ]

Exit gate:
- [ ] Each hypothesis from S3 has corresponding S4 rows
- [ ] At least 2 distinct Confidence values across S4 rows
- [ ] All S4 Source-Stage values in {S1, S2, S3}

**HANDOFF DECLARATION -- S4 to S5:**

> **Role passes to: Stage 5 -- Synthesis Director.**
> Artifacts transferred: Full Evidence Table (S1-S4) + Hypotheses Table (ARTIFACT-S4).
> Synthesis Director authorized Source-Stage values: {S1, S2, S3, S4}.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 5 is scope-restricted. Every synthesis row must carry non-blank Source-Stage in
> {S1, S2, S3, S4} and a named Source-Artifact. Provenance enforcement is live for Stage 5.

---

**Stage 5 -- Synthesis Director**

Entry gate:
- [ ] S4 exit all-Pass
- [ ] Handoff S4-to-S5 complete
- [ ] PROVENANCE RULE activation block present in handoff S4-to-S5

**PRE-EXECUTION [Stage 5 of 5]:**
ATTRIBUTION [S5, PRE]: Will all S5 rows carry Stage=S5? [ Yes / No ]
CALIBRATION [S5, PRE]: Will Confidence values across S5 rows be varied, not uniform? [ Yes / No ]
FALSIFICATION [S5, PRE]: Will all Hypotheses Table Final-Status cells be filled at this stage? [ Yes / No ]
PROVENANCE [S5, PRE]: Will all S5 rows carry non-blank Source-Stage in {S1, S2, S3, S4}? [ Yes / No ]

Add rows to Evidence Table with Stage=S5. Row types:
- Consensus (where S1 and S2 agree -- cite both artifacts)
- Conflict (where S1 and S2 diverge -- name the conflict; cite conflicting artifacts)
- Hypothesis-Verdict (final status for each hypothesis from Hypotheses Table)
- Gap (what remains under-evidenced after full campaign)
- Decision-Readiness (exactly one row; value is one sentence naming posture and specific gap
  if not ready -- e.g., "Ready to proceed" or "Needs more investigation on X before committing")

Update Hypotheses Table: fill Final-Status column for all rows.

**POST-EXECUTION [Stage 5 of 5]:**
ATTRIBUTION [S5, POST]: Do all S5 rows carry Stage=S5? [ Yes / No ]
CALIBRATION [S5, POST]: Do S5 rows carry at least 2 distinct Confidence values? [ Yes / No ]
FALSIFICATION [S5, POST]: Are all Hypotheses Table Final-Status cells non-blank? [ Yes / No ]
PROVENANCE [S5, POST]: Do all S5 rows carry non-blank Source-Stage in {S1, S2, S3, S4}? [ Yes / No ]

Non-applicable:
SEQUENCING [S5]: Not applicable at synthesis. [ No ]

Exit gate:
- [ ] Evidence Table has Consensus and Conflict rows (Stage=S5)
- [ ] All Hypotheses Table Final-Status cells filled
- [ ] Gap rows present
- [ ] Exactly one Decision-Readiness row (one sentence value)
- [ ] All S5 Source-Stage values in {S1, S2, S3, S4}
- [ ] PROVENANCE compliance verified via POST-EXECUTION check above

---

### OUTPUT ASSEMBLY

Assemble the final evidence brief:

1. **Brief header**: title, topic, date
2. **Governance preamble** (this section, as sealed)
3. **Filled gate record** (all Pass/Fail cells completed)
4. **Master Evidence Table** (all rows, Stage=S1 through S5, including Synthesis rows)
5. **Hypotheses Table** (all rows including Final-Status)
6. **Consolidated invocation audit table**: 40 rows (one per dual-phase answer + negative);
   columns: Rule, Stage, Phase (PRE/POST/N-A), Applicable (+/-), Answer, Discrepancy

**Delivery gate:** Count rows in the consolidated invocation audit table. Must equal 40.
A count != 40 is a delivery blocker. If any row pair shows PRE=Yes / POST=No, flag as
INTENT-EXECUTION GAP and document. Do not close this brief until count equals 40 and no
undocumented gaps remain.

---

## Variate Summary

| Variate | Primary Axis | Key Structural Innovation | Signal Probed |
|---------|-------------|--------------------------|---------------|
| V-01 | Role Sequence | Provenance activation moves from role charter to live handoff boundary; role charter declares scope only | Signal 2 (C-30 PASS+) |
| V-02 | Output Format | Table-first with Stage column; SEQUENCING compliance verifiable by sort; provenance as foreign-key reference | C-28 structural depth |
| V-03 | Lifecycle Emphasis | Dual-phase interrogatives at every applicable stage; intent-execution gap visible as PRE/POST discrepancy | Signal 1 (C-21 PASS+) |
| V-04 | Phrasing Register | RFC SHALL/MUST throughout; every obligation is a numbered, verifiable requirement | Formalism depth |
| V-05 | Combination | Table-first + dual-phase interrogatives + provenance activation at handoff boundary (all three axes combined) | Signal 1 + Signal 2 |

**Predicted winner**: V-05, because it combines the two PASS+ structural innovations with the
table-first format that makes compliance mechanically verifiable. V-03 alone surfaces intent-
execution gaps but not provenance activation gaps. V-01 alone activates provenance at handoffs
but does not make SEQUENCING sort-verifiable. V-05 closes all three vectors simultaneously.
