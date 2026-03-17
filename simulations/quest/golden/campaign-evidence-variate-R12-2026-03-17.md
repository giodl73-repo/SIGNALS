---
skill: quest-variate
skill_target: campaign-evidence
date: 2026-03-17
round: 12
rubric_version: 12
---

# Variates: campaign-evidence (Round 12)

Five complete, runnable skill body prompts. Single-axis variations first (V-01 through V-03),
combined axes second (V-04 through V-05).

**New requirements for all R12 variates** (C-34 and C-35 are the additions from v12):
- **C-34**: Each claim produced in a scope-restricted stage (Stage 3: Hypothesis Architect,
  Stage 4: Evidence Analyst, Stage 5: Synthesis Director) carries an artifact provenance tag
  naming the specific prior-stage output artifact it draws from.
  Format: `[source: Stage N -- Artifact Name]`.
  A claim with no provenance tag in a scope-restricted stage is a structural gap equivalent to
  an unattributed assertion. A claim whose tag names an artifact outside the role's declared
  access scope is a visible scope violation.
- **C-35**: The pre-declared invocation matrix checksum (C-33) is formalized as a delivery gate
  condition -- an explicit constraint that the brief is structurally incomplete and may not be
  closed or delivered until the actual invocation artifact count equals 20 (the preamble value).
  This is enforcement, not observation: a count mismatch is a delivery blocker, not a finding.

**Checksum arithmetic for all R12 variates:**
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

**Scope-restricted stages** (C-34 applies): Stage 3, Stage 4, Stage 5. Every claim in these
stages must carry `[source: Stage N -- Artifact Name]`.

**Delivery gate (C-35):** "This brief SHALL NOT be closed or delivered until invocation artifact
count = 20. A count != 20 is a delivery blocker."

**Baseline requirements inherited from prior rounds** (C-22, C-23, C-24, C-25, C-27, C-30,
C-31, C-32, C-33):
- Universal binary `[ Yes / No ]` on every invocation (C-22)
- Stage-index suffix `[Stage N of 5]` on every invocation (C-23)
- Entry and exit conditions per stage (C-24)
- Gate record pre-templated in preamble with blank cells (C-27)
- Named role + explicit "Role passes to:" transfer at each boundary (C-30)
- Negative invocation at every non-applicable stage (C-31)
- Role access scope declared per stage (C-32)
- Invocation matrix total pre-declared as derivable checksum (C-33)

Variations explore how C-34 (provenance tags) and C-35 (delivery gate) are structurally embedded.

---

## V-01 -- Axis: Output Format (Provenance Tags as Scannable Annotation Blocks)

**Variation axis**: Artifact provenance tags are structured as standalone annotation blocks
appended after each claim -- not inline labels buried in prose. Each block is a named field:
`[source: Stage N -- Artifact Name]`. In scope-restricted stages, claims and their provenance
blocks are co-located and independently scannable. A reviewer auditing C-34 compliance does
not need to parse narrative; they scan for provenance blocks and verify each matches the role's
declared access scope.

**Hypothesis**: When provenance tags are structured annotation blocks rather than inline labels,
C-34 compliance becomes a visual scan rather than a prose interpretation. A missing block is
a visible gap. A block citing an out-of-scope artifact is a visible violation. The format
converts provenance from a quality of the claim into a required artifact co-located with it.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable -- cannot be modified after any stage executes.
This is a commitment, not a record.

---

#### Rule Registry (all rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: Stage 1(+), Stage 2(+), Stage 3(+), Stage 4(+), Stage 5(+)]`
Every material claim names its source stage. Labels: `[web]` (S1), `[intel]` (S2),
`[hypothesis]` (S3), `[analysis]` (S4), `[synthesis]` (S5). A claim without a stage label
is unattributed.

**CALIBRATION RULE** `[invoked at: Stage 1(-), Stage 2(-), Stage 3(-), Stage 4(+), Stage 5(+)]`
Confidence ratings must vary across findings. Uniform ratings are a calibration failure.
Anti-uniformity guard at every positive invocation: "Are at least two distinct confidence
levels present?" [ Yes / No ]

**FALSIFICATION RULE** `[invoked at: Stage 1(-), Stage 2(-), Stage 3(+), Stage 4(-), Stage 5(+)]`
Each hypothesis carries a falsification condition and a final status.
Final status options: Supported / Refuted / Indeterminate.

**SEQUENCING RULE** `[invoked at: Stage 1(+), Stage 2(+), Stage 3(+), Stage 4(-), Stage 5(-)]`
Evidence stages (S1, S2) complete before hypothesis declaration (S3). Pre-evidence hypotheses
are anchors, not hypotheses. Rationale encoded as named rule: "A hypothesis anchored before
evidence gathering is a bias, not a hypothesis."

**PROVENANCE RULE** `[invoked at: Stage 1(-), Stage 2(-), Stage 3(+), Stage 4(+), Stage 5(+)]`
Every claim in a scope-restricted stage carries a provenance block immediately following:
`[source: Stage N -- Artifact Name]`. The named artifact must be within the role's declared
access scope. A claim with no provenance block is a structural gap. A claim whose provenance
block names an out-of-scope artifact is a charter violation.

Scope-restricted stages: Stage 3 (Hypothesis Architect), Stage 4 (Evidence Analyst),
Stage 5 (Synthesis Director).

Peer declaration: ATTRIBUTION, CALIBRATION, FALSIFICATION, SEQUENCING, PROVENANCE are
equal-tier governance rules. No rule is primary. Newly added rules inherit peer status
automatically. Rule count = 5; coverage map dimensions update accordingly.

---

**COVERAGE MAP UPDATE FOR PROVENANCE RULE:**

With 5 rules x 5 stages = 25 cells:

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|----|----------|----------|
| ATTRIBUTION | + | + | + | + | + | 5 | 0 |
| CALIBRATION | - | - | - | + | + | 2 | 3 |
| FALSIFICATION | - | - | + | - | + | 2 | 3 |
| SEQUENCING | + | + | + | - | - | 3 | 2 |
| PROVENANCE | - | - | + | + | + | 3 | 2 |
| **Total** | | | | | | **15** | **10** |

**Invocation matrix checksum (C-33):** 25 invocation artifacts = 15 positive + 10 negative,
derived from 5 rules x 5 stages.

**DELIVERY GATE (C-35):** This brief SHALL NOT be closed or delivered until the invocation
artifact count at the consolidated audit table equals 25. A count != 25 is a delivery blocker.
Closing a brief with count != 25 is a structural violation equivalent to an unverified gate.

---

#### Role Roster and Access Scopes (C-32)

| Stage | Role Name | Access Scope -- Authorized Reads |
|-------|-----------|----------------------------------|
| Stage 1 | Web Evidence Collector | External sources only. No prior-stage artifacts exist. |
| Stage 2 | Intelligence Analyst | ARTIFACT-S1 (Web Findings Corpus) only. No external sources beyond Stage 1 corpus. |
| Stage 3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Intelligence Assessment) only. A hypothesis citing information predating Stage 1 is a charter violation. |
| Stage 4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 (Hypothesis Register) only. No new external sources. |
| Stage 5 | Synthesis Director | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 + ARTIFACT-S4 (Evidence Analysis) only. |

Provenance tag format for scope-restricted stages:
- Stage 3 claims: `[source: Stage 1 -- Web Findings Corpus]` or `[source: Stage 2 -- Intelligence Assessment]`
- Stage 4 claims: `[source: Stage 1 -- Web Findings Corpus]`, `[source: Stage 2 -- Intelligence Assessment]`, or `[source: Stage 3 -- Hypothesis Register]`
- Stage 5 claims: any of ARTIFACT-S1 through ARTIFACT-S4 by name

---

#### Gate Record Template (pre-instantiated blank -- fill during execution)

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|-----------|-----------|
| Stage 1 | Web Evidence Collector | First stage -- automatic: [ Pass ] | 6+ labeled findings; no hypothesis: [ ] |
| Stage 2 | Intelligence Analyst | Stage 1 exit all-Pass: [ ] | Landscape characterized; no hypothesis; all claims `[intel]`: [ ] |
| Stage 3 | Hypothesis Architect | Stage 1+2 exit all-Pass: [ ] | 3-5 hypotheses with falsification conditions; all claims carry provenance blocks: [ ] |
| Stage 4 | Evidence Analyst | Stage 1-3 exit all-Pass: [ ] | All hypotheses analyzed; 2+ confidence levels; all claims carry provenance blocks: [ ] |
| Stage 5 | Synthesis Director | Stage 1-4 exit all-Pass: [ ] | Synthesis complete; consensus/conflict separated; decision verdict in one sentence; all claims carry provenance blocks: [ ] |

---

### Stage 1 -- Web Evidence Collector

**ROLE: Web Evidence Collector**
**ACCESS SCOPE: External sources only. ARTIFACT-S1 does not yet exist.**

**ENTRY GATE:**

| Condition | Status |
|-----------|--------|
| First stage -- no prior stages required | [ Pass ] |
| No hypothesis has been stated | [ Pass ] |

ATTRIBUTION RULE [Stage 1 of 5] -- All findings labeled `[web]`? [ Yes / No ]
CALIBRATION RULE [Stage 1 of 5] -- Applicable? [ No -- confidence rating governs analysis stages, not evidence collection ]
FALSIFICATION RULE [Stage 1 of 5] -- Applicable? [ No -- no hypotheses declared at this stage ]
SEQUENCING RULE [Stage 1 of 5] -- Running before any hypothesis stated? [ Yes / No ]
PROVENANCE RULE [Stage 1 of 5] -- Applicable? [ No -- Stage 1 is not scope-restricted; no prior artifacts exist ]

Search for evidence on **{{topic}}**: primary sources, recent publications, technical references,
industry data, quantitative studies. Label every finding `[web]`. Collect broadly.

**EXIT GATE:**

| Condition | Status |
|-----------|--------|
| Minimum 6 findings documented, each labeled `[web]` | [ Pass / Fail ] |
| No hypothesis stated in Stage 1 output | [ Pass / Fail ] |

> **Role passes to: Stage 2 -- Intelligence Analyst.**
> ARTIFACT-S1 (Web Findings Corpus) is now readable by Intelligence Analyst per its access scope.

---

### Stage 2 -- Intelligence Analyst

**ROLE: Intelligence Analyst**
**ACCESS SCOPE: ARTIFACT-S1 only. No external sources; no information predating Stage 1.**

**ENTRY GATE:**

| Condition | Status |
|-----------|--------|
| Stage 1 exit gate is all-Pass | [ Pass / Fail ] |
| No hypothesis stated at any prior point | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 2 of 5] -- All new claims labeled `[intel]`? [ Yes / No ]
CALIBRATION RULE [Stage 2 of 5] -- Applicable? [ No -- confidence rating governs analysis, not intelligence characterization ]
FALSIFICATION RULE [Stage 2 of 5] -- Applicable? [ No -- no hypotheses declared at this stage ]
SEQUENCING RULE [Stage 2 of 5] -- Hypothesis declaration has not yet occurred? [ Yes / No ]
PROVENANCE RULE [Stage 2 of 5] -- Applicable? [ No -- Stage 2 is not scope-restricted; its only source is Stage 1 and all Stage 2 claims are labeled `[intel]` ]

Apply expert judgment to ARTIFACT-S1: patterns, contradictions, evidence strength (well-evidenced
vs. thin), domain-specific considerations, knowledge gaps. Label every new claim `[intel]`.

**EXIT GATE:**

| Condition | Status |
|-----------|--------|
| Evidence landscape characterized: patterns, conflicts, gaps named | [ Pass / Fail ] |
| No hypothesis stated anywhere in Stage 2 output | [ Pass / Fail ] |
| All new claims carry `[intel]` label | [ Pass / Fail ] |

> **Role passes to: Stage 3 -- Hypothesis Architect.**
> ARTIFACT-S2 (Intelligence Assessment) is now readable by Hypothesis Architect per its access scope.

---

### Stage 3 -- Hypothesis Architect

**ROLE: Hypothesis Architect**
**ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2 only. Any hypothesis referencing information
predating Stage 1 is a charter violation -- it is a pre-committed belief wearing this role's label.**

**ENTRY GATE:**

| Condition | Status |
|-----------|--------|
| Stage 1 exit gate is all-Pass | [ Pass / Fail ] |
| Stage 2 exit gate is all-Pass | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 3 of 5] -- Each hypothesis cites specific ARTIFACT-S1 or ARTIFACT-S2 evidence? [ Yes / No ]
CALIBRATION RULE [Stage 3 of 5] -- Applicable? [ No -- hypothesis declaration, not confidence rating ]
FALSIFICATION RULE [Stage 3 of 5] -- Each hypothesis carries an explicit falsification condition? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5] -- Stage 1 and Stage 2 complete before this stage began? [ Yes / No ]
PROVENANCE RULE [Stage 3 of 5] -- All claims carry provenance annotation blocks naming ARTIFACT-S1 or ARTIFACT-S2? [ Yes / No ]

Declare 3-5 hypotheses. For each hypothesis, use the following format:

**H-NN**: [Falsifiable claim text]
> Falsification condition: [The criterion that would cause rejection of this hypothesis]
> [source: Stage N -- Artifact Name] -- [The specific evidence in ARTIFACT-SN grounding this hypothesis]

A hypothesis block with no `[source: ...]` annotation block is a structural gap (C-34 violation).
A hypothesis whose `[source: ...]` names an artifact not in {ARTIFACT-S1, ARTIFACT-S2} is a
scope violation (C-32 violation).

**EXIT GATE:**

| Condition | Status |
|-----------|--------|
| 3-5 hypotheses declared | [ Pass / Fail ] |
| Each hypothesis cites ARTIFACT-S1 or ARTIFACT-S2 (scope check) | [ Pass / Fail ] |
| Each hypothesis carries a named falsification condition | [ Pass / Fail ] |
| Every hypothesis claim carries a `[source: Stage N -- Artifact Name]` provenance block | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 3 of 5] -- Hypotheses cite source artifacts? [ Yes / No ]
FALSIFICATION RULE [Stage 3 of 5] -- Each hypothesis has a falsification condition? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5] -- Stage 3 opened only after Stage 1+2 exit gates passed? [ Yes / No ]
PROVENANCE RULE [Stage 3 of 5] -- All claims carry `[source: Stage N -- Artifact Name]` blocks? [ Yes / No ]

> **Role passes to: Stage 4 -- Evidence Analyst.**
> ARTIFACT-S3 (Hypothesis Register) is now readable by Evidence Analyst per its access scope.

---

### Stage 4 -- Evidence Analyst

**ROLE: Evidence Analyst**
**ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only. No new external sources.
This role analyzes -- it does not gather new evidence.**

**ENTRY GATE:**

| Condition | Status |
|-----------|--------|
| Stages 1, 2, 3 exit gates are all-Pass | [ Pass / Fail ] |
| ARTIFACT-S3 (Hypothesis Register) is available | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 4 of 5] -- All analyzed claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5] -- At least two distinct confidence levels present? [ Yes / No ]
FALSIFICATION RULE [Stage 4 of 5] -- Applicable? [ No -- hypotheses declared in Stage 3; Stage 4 applies evidence, not re-declares ]
SEQUENCING RULE [Stage 4 of 5] -- Applicable? [ No -- post-hypothesis analysis; sequencing constraint resolved at Stage 3 ]
PROVENANCE RULE [Stage 4 of 5] -- All claims carry `[source: Stage N -- Artifact Name]` blocks naming authorized artifacts? [ Yes / No ]

For each hypothesis in ARTIFACT-S3:
- Assess supporting evidence weight

  > [source: Stage N -- Artifact Name] -- cite the specific artifact and finding

- Assess challenging evidence weight

  > [source: Stage N -- Artifact Name] -- cite the specific artifact and finding

- Assign confidence: High / Medium / Low
- State the evidence driving the confidence assignment

Calibration guard: if all confidence ratings are uniform -- recalibrate before advancing.
Uniform confidence is a CALIBRATION RULE failure.

**EXIT GATE:**

| Condition | Status |
|-----------|--------|
| All hypotheses in ARTIFACT-S3 analyzed | [ Pass / Fail ] |
| Every analyzed claim carries source-stage label | [ Pass / Fail ] |
| Every analyzed claim carries `[source: Stage N -- Artifact Name]` provenance block | [ Pass / Fail ] |
| At least two distinct confidence levels present | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 4 of 5] -- All claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5] -- Confidence ratings non-uniform (2+ distinct levels)? [ Yes / No ]
PROVENANCE RULE [Stage 4 of 5] -- All claims carry provenance blocks naming authorized artifacts? [ Yes / No ]

> **Role passes to: Stage 5 -- Synthesis Director.**
> ARTIFACT-S4 (Evidence Analysis) is now readable by Synthesis Director per its access scope.

---

### Stage 5 -- Synthesis Director

**ROLE: Synthesis Director**
**ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 + ARTIFACT-S4. Full read access
to all prior stages. This is the final stage; there is no handoff.**

**ENTRY GATE:**

| Condition | Status |
|-----------|--------|
| Stages 1-4 exit gates are all-Pass | [ Pass / Fail ] |
| All four prior artifacts available | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 5 of 5] -- All synthesis claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5] -- Non-uniform confidence ratings confirmed? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5] -- Every hypothesis carries a final status (Supported / Refuted / Indeterminate)? [ Yes / No ]
SEQUENCING RULE [Stage 5 of 5] -- Applicable? [ No -- synthesis is terminal; all sequencing resolved at Stages 1-3 ]
PROVENANCE RULE [Stage 5 of 5] -- All synthesis claims carry `[source: Stage N -- Artifact Name]` blocks? [ Yes / No ]

**Consensus** (ARTIFACT-S1 and ARTIFACT-S2 agree -- name the agreement explicitly):

> [source: Stage N -- Artifact Name] for each consensus claim

**Conflict** (ARTIFACT-S1 and ARTIFACT-S2 diverge -- name the divergence explicitly):

> [source: Stage N -- Artifact Name] for each conflict claim

**Hypothesis Register:**

| H# | Hypothesis | Falsification Condition | Status | Confidence | Provenance |
|----|------------|------------------------|--------|------------|-----------|
| H-01 | ... | ... | Supported/Refuted/Indeterminate | High/Med/Low | [source: Stage N -- Artifact Name] |

**Gaps and Open Questions** (what remains under-evidenced after this campaign):

> [source: Stage N -- Artifact Name] for each gap assessment

**Decision Readiness** (one sentence -- name posture and, if not ready, name the specific gap):

**EXIT GATE:**

| Condition | Status |
|-----------|--------|
| All five stage artifacts produced | [ Pass / Fail ] |
| All hypothesis Status cells populated | [ Pass / Fail ] |
| Confidence ratings non-uniform | [ Pass / Fail ] |
| Decision readiness in one sentence | [ Pass / Fail ] |
| Every claim in Stage 5 carries a `[source: Stage N -- Artifact Name]` provenance block | [ Pass / Fail ] |

ATTRIBUTION RULE [Stage 5 of 5] -- Synthesis claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5] -- Confidence distribution non-uniform? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5] -- All hypotheses resolved with final status? [ Yes / No ]
PROVENANCE RULE [Stage 5 of 5] -- All claims carry provenance blocks? [ Yes / No ]

---

### Output: Evidence Brief

Compile all stage artifacts into a single self-contained document with: title, topic context,
**Gate Record** (filled from preamble template), **Consolidated Invocation Audit Table**,
**Provenance Compliance Summary**, stage-by-stage findings, hypothesis register,
synthesis (consensus/conflict explicitly separated), gaps list, decision readiness sentence.

**Consolidated Invocation Audit Table** (row count must equal checksum: 25):

| # | Rule | Stage | Stage-Index | Form | Pass/Fail |
|---|------|-------|-------------|------|-----------|
| 1 | ATTRIBUTION | S1 | [Stage 1 of 5] | Binary | |
| 2 | CALIBRATION | S1 | [Stage 1 of 5] | Binary (negative) | |
| 3 | FALSIFICATION | S1 | [Stage 1 of 5] | Binary (negative) | |
| 4 | SEQUENCING | S1 | [Stage 1 of 5] | Binary | |
| 5 | PROVENANCE | S1 | [Stage 1 of 5] | Binary (negative) | |
| 6 | ATTRIBUTION | S2 | [Stage 2 of 5] | Binary | |
| 7 | CALIBRATION | S2 | [Stage 2 of 5] | Binary (negative) | |
| 8 | FALSIFICATION | S2 | [Stage 2 of 5] | Binary (negative) | |
| 9 | SEQUENCING | S2 | [Stage 2 of 5] | Binary | |
| 10 | PROVENANCE | S2 | [Stage 2 of 5] | Binary (negative) | |
| 11 | ATTRIBUTION | S3 | [Stage 3 of 5] | Binary | |
| 12 | CALIBRATION | S3 | [Stage 3 of 5] | Binary (negative) | |
| 13 | FALSIFICATION | S3 | [Stage 3 of 5] | Binary | |
| 14 | SEQUENCING | S3 | [Stage 3 of 5] | Binary | |
| 15 | PROVENANCE | S3 | [Stage 3 of 5] | Binary | |
| 16 | ATTRIBUTION | S4 | [Stage 4 of 5] | Binary | |
| 17 | CALIBRATION | S4 | [Stage 4 of 5] | Binary | |
| 18 | FALSIFICATION | S4 | [Stage 4 of 5] | Binary (negative) | |
| 19 | SEQUENCING | S4 | [Stage 4 of 5] | Binary (negative) | |
| 20 | PROVENANCE | S4 | [Stage 4 of 5] | Binary | |
| 21 | ATTRIBUTION | S5 | [Stage 5 of 5] | Binary | |
| 22 | CALIBRATION | S5 | [Stage 5 of 5] | Binary | |
| 23 | FALSIFICATION | S5 | [Stage 5 of 5] | Binary | |
| 24 | SEQUENCING | S5 | [Stage 5 of 5] | Binary (negative) | |
| 25 | PROVENANCE | S5 | [Stage 5 of 5] | Binary | |

**DELIVERY GATE (C-35):** Row count = [ ]. Checksum = 25.
This brief SHALL NOT be closed until row count = 25. Count mismatch is a delivery blocker.
Match: [ Yes / No ]

---

---

## V-02 -- Axis: Lifecycle Emphasis (Delivery Gate as First-Class Constraint)

**Variation axis**: The delivery gate (C-35) is the first structural element of the preamble --
positioned before the rule registry, role roster, and coverage map. The executor encounters
the enforcement condition before reading any rule it enforces. This inverts the conventional
preamble order (rules then enforcement) to gate-then-rules: the executor understands what
"closing the brief" means before they see the rules that fill the gate.

**Hypothesis**: When the delivery gate is positioned at the opening of the preamble rather
than the close of the output, it reframes the entire campaign. The executor is not working
toward a brief that will later be checked -- they are filling a delivery precondition at
every stage. The gate stops being a postscript and becomes the framing condition for all work.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable.

---

#### DELIVERY GATE (C-35) -- Read This First

**This brief SHALL NOT be closed or delivered until:**
1. The consolidated invocation audit table contains exactly 25 rows (5 rules x 5 stages).
2. Every row in the audit table has a Pass/Fail value.
3. Every claim in scope-restricted stages (Stage 3, Stage 4, Stage 5) carries a
   `[source: Stage N -- Artifact Name]` provenance block naming an artifact within the
   role's declared access scope.
4. All gate record cells are filled Pass.

**A brief submitted with:**
- Audit table row count != 25: DELIVERY BLOCKED
- Any scope-restricted claim lacking a provenance block: DELIVERY BLOCKED
- Any gate record cell unfilled or Fail: DELIVERY BLOCKED
- Invocation count mismatch vs. checksum: DELIVERY BLOCKED

This is not a checklist to verify at the end. It is the closing condition for every stage.
Each stage that completes fills cells in the gate record, adds rows to the audit table, and
attaches provenance blocks to its claims. A brief that reaches Stage 5 with unfilled cells
cannot be closed.

---

#### Rule Registry (5 peers; no rule is primary)

**PROVENANCE RULE** `[invoked at: Stage 1(-), Stage 2(-), Stage 3(+), Stage 4(+), Stage 5(+)]`
Every claim in a scope-restricted stage carries a provenance block: `[source: Stage N -- Artifact Name]`.
The named artifact must be within the role's declared access scope (C-32). A missing block is
a structural gap. A block citing an out-of-scope artifact is a charter violation.
Scope-restricted stages: Stage 3, Stage 4, Stage 5.

**ATTRIBUTION RULE** `[invoked at: Stage 1(+), Stage 2(+), Stage 3(+), Stage 4(+), Stage 5(+)]`
Every material claim names its source stage. Labels: `[web]`, `[intel]`, `[hypothesis]`,
`[analysis]`, `[synthesis]`. Unattributed claims fail this rule.

**CALIBRATION RULE** `[invoked at: Stage 1(-), Stage 2(-), Stage 3(-), Stage 4(+), Stage 5(+)]`
Confidence ratings must vary. Uniform ratings are a calibration failure.
Anti-uniformity check: "Are at least two distinct confidence levels present?" [ Yes / No ]

**FALSIFICATION RULE** `[invoked at: Stage 1(-), Stage 2(-), Stage 3(+), Stage 4(-), Stage 5(+)]`
Each hypothesis carries a falsification condition and a final status:
Supported / Refuted / Indeterminate.

**SEQUENCING RULE** `[invoked at: Stage 1(+), Stage 2(+), Stage 3(+), Stage 4(-), Stage 5(-)]`
Evidence stages (S1, S2) complete before hypothesis declaration (S3).
"A hypothesis anchored before evidence gathering is a bias, not a hypothesis."

Peer declaration: PROVENANCE, ATTRIBUTION, CALIBRATION, FALSIFICATION, SEQUENCING are
equal-tier peers. No rule is primary. Rule count = 5.

---

#### Coverage Map (immutable)

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|----|----------|----------|
| ATTRIBUTION | + | + | + | + | + | 5 | 0 |
| CALIBRATION | - | - | - | + | + | 2 | 3 |
| FALSIFICATION | - | - | + | - | + | 2 | 3 |
| SEQUENCING | + | + | + | - | - | 3 | 2 |
| PROVENANCE | - | - | + | + | + | 3 | 2 |
| **Total** | | | | | | **15** | **10** |

**Invocation checksum (C-33):** 25 artifacts = 15 positive + 10 negative, from 5 rules x 5 stages.
Derivable expression: rules(5) x stages(5) = 25. Adding a rule shifts count to 30 automatically.

**DELIVERY GATE ENFORCEMENT (C-35):** Audit table at brief close must have row count = 25.
This brief SHALL NOT be closed until count = 25. A count != 25 blocks delivery.

---

#### Role Roster and Access Scopes (C-32)

| Stage | Role | Access Scope |
|-------|------|-------------|
| Stage 1 | Web Evidence Collector | External sources. No prior artifacts. |
| Stage 2 | Intelligence Analyst | ARTIFACT-S1 (Web Findings Corpus) only. |
| Stage 3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Intelligence Assessment). |
| Stage 4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 (Hypothesis Register). |
| Stage 5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 (Evidence Analysis). |

Provenance block format for scope-restricted stages:
- Valid S3 blocks: `[source: Stage 1 -- Web Findings Corpus]`, `[source: Stage 2 -- Intelligence Assessment]`
- Valid S4 blocks: add `[source: Stage 3 -- Hypothesis Register]`
- Valid S5 blocks: add `[source: Stage 4 -- Evidence Analysis]`

---

#### Gate Record Template (blank -- fill during execution)

| Stage | Role | Entry | Exit |
|-------|------|-------|------|
| Stage 1 | Web Evidence Collector | First stage: [ Pass ] | 6+ labeled findings; no hypothesis: [ ] |
| Stage 2 | Intelligence Analyst | Stage 1 exit Pass: [ ] | Landscape characterized; no hypothesis; all `[intel]`: [ ] |
| Stage 3 | Hypothesis Architect | Stage 1+2 exit Pass: [ ] | 3-5 hypotheses; all with falsification conditions; all with provenance blocks: [ ] |
| Stage 4 | Evidence Analyst | Stage 1-3 exit Pass: [ ] | All hypotheses analyzed; 2+ confidence levels; all claims with provenance blocks: [ ] |
| Stage 5 | Synthesis Director | Stage 1-4 exit Pass: [ ] | Synthesis done; consensus/conflict separated; decision verdict; all claims with provenance blocks: [ ] |

---

### Stage 1 -- Web Evidence Collector

**ROLE: Web Evidence Collector | ACCESS SCOPE: External sources only**

ATTRIBUTION RULE [Stage 1 of 5] -- All findings labeled `[web]`? [ Yes / No ]
CALIBRATION RULE [Stage 1 of 5] -- Applicable? [ No -- not an analysis stage ]
FALSIFICATION RULE [Stage 1 of 5] -- Applicable? [ No -- no hypotheses yet ]
SEQUENCING RULE [Stage 1 of 5] -- Running before any hypothesis? [ Yes / No ]
PROVENANCE RULE [Stage 1 of 5] -- Applicable? [ No -- evidence collection, not scope-restricted stage ]

Search **{{topic}}**: primary sources, publications, technical references, industry data,
quantitative studies. Label every finding `[web]`. Collect without filtering for expected
conclusions. Minimum 6 labeled findings. Do not state any hypothesis.

Gate record Stage 1 entry: [ Pass ] (automatic -- first stage)
Gate record Stage 1 exit: [ Pass / Fail ] (check: 6+ `[web]` findings, no hypothesis stated)

> **Role passes to: Stage 2 -- Intelligence Analyst.**
> ARTIFACT-S1 (Web Findings Corpus) produced.

---

### Stage 2 -- Intelligence Analyst

**ROLE: Intelligence Analyst | ACCESS SCOPE: ARTIFACT-S1 only**

ATTRIBUTION RULE [Stage 2 of 5] -- All new claims labeled `[intel]`? [ Yes / No ]
CALIBRATION RULE [Stage 2 of 5] -- Applicable? [ No -- not an analysis stage ]
FALSIFICATION RULE [Stage 2 of 5] -- Applicable? [ No -- no hypotheses yet ]
SEQUENCING RULE [Stage 2 of 5] -- Hypothesis not yet declared? [ Yes / No ]
PROVENANCE RULE [Stage 2 of 5] -- Applicable? [ No -- Stage 2 is not scope-restricted ]

Apply judgment to ARTIFACT-S1: patterns, contradictions, evidence strength, gaps,
domain considerations. Label every new claim `[intel]`. Do not state any hypothesis.

Gate record Stage 2 entry: [ Pass / Fail ] (check: Stage 1 exit gate passed)
Gate record Stage 2 exit: [ Pass / Fail ] (check: landscape characterized, no hypothesis,
all claims `[intel]`)

> **Role passes to: Stage 3 -- Hypothesis Architect.**
> ARTIFACT-S2 (Intelligence Assessment) produced.

---

### Stage 3 -- Hypothesis Architect

**ROLE: Hypothesis Architect | ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2 only**

ATTRIBUTION RULE [Stage 3 of 5] -- Each hypothesis cites ARTIFACT-S1 or ARTIFACT-S2 evidence? [ Yes / No ]
CALIBRATION RULE [Stage 3 of 5] -- Applicable? [ No -- hypothesis declaration, not confidence rating ]
FALSIFICATION RULE [Stage 3 of 5] -- Each hypothesis has an explicit falsification condition? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5] -- Stages 1 and 2 complete before this stage began? [ Yes / No ]
PROVENANCE RULE [Stage 3 of 5] -- All hypothesis claims carry `[source: Stage N -- Artifact Name]` blocks? [ Yes / No ]

Declare 3-5 hypotheses in this format:

**H-NN**: [Claim]
> Falsification condition: [What would cause rejection]
> `[source: Stage 1 -- Web Findings Corpus]` or `[source: Stage 2 -- Intelligence Assessment]`
> Grounding: [Specific finding in the named artifact]

Gate record Stage 3 entry: [ Pass / Fail ]
Gate record Stage 3 exit: [ Pass / Fail ] (check: 3-5 hypotheses, all with falsification
conditions, all with provenance blocks citing authorized artifacts only)

> **Role passes to: Stage 4 -- Evidence Analyst.**
> ARTIFACT-S3 (Hypothesis Register) produced.

---

### Stage 4 -- Evidence Analyst

**ROLE: Evidence Analyst | ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only**

ATTRIBUTION RULE [Stage 4 of 5] -- All analyzed claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5] -- At least two distinct confidence levels present? [ Yes / No ]
FALSIFICATION RULE [Stage 4 of 5] -- Applicable? [ No -- Stage 3 declared hypotheses; Stage 4 applies evidence ]
SEQUENCING RULE [Stage 4 of 5] -- Applicable? [ No -- post-hypothesis analysis stage ]
PROVENANCE RULE [Stage 4 of 5] -- All claims carry provenance blocks citing authorized artifacts? [ Yes / No ]

For each hypothesis in ARTIFACT-S3:
- Supporting evidence:
  `[source: Stage N -- Artifact Name]` -- [specific finding]
- Challenging evidence:
  `[source: Stage N -- Artifact Name]` -- [specific finding]
- Confidence: High / Medium / Low
- Rationale: [evidence driving confidence]

Calibration guard: if all ratings uniform -- recalibrate before advancing.

Gate record Stage 4 entry: [ Pass / Fail ]
Gate record Stage 4 exit: [ Pass / Fail ] (check: all hypotheses analyzed, 2+ confidence
levels, all claims with provenance blocks)

> **Role passes to: Stage 5 -- Synthesis Director.**
> ARTIFACT-S4 (Evidence Analysis) produced.

---

### Stage 5 -- Synthesis Director

**ROLE: Synthesis Director | ACCESS SCOPE: ARTIFACT-S1 through ARTIFACT-S4**

ATTRIBUTION RULE [Stage 5 of 5] -- All synthesis claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5] -- Non-uniform confidence confirmed? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5] -- Every hypothesis has final status? [ Yes / No ]
SEQUENCING RULE [Stage 5 of 5] -- Applicable? [ No -- terminal synthesis stage ]
PROVENANCE RULE [Stage 5 of 5] -- All synthesis claims carry provenance blocks? [ Yes / No ]

**Consensus:** (ARTIFACT-S1 and ARTIFACT-S2 agree)
> `[source: Stage N -- Artifact Name]` per consensus claim

**Conflict:** (ARTIFACT-S1 and ARTIFACT-S2 diverge -- name the divergence explicitly)
> `[source: Stage N -- Artifact Name]` per conflict claim

**Hypothesis Register:**

| H# | Hypothesis | Falsification Condition | Status | Confidence | Source |
|----|------------|------------------------|--------|------------|--------|
| H-01 | ... | ... | Supported/Refuted/Indeterminate | High/Med/Low | [source: Stage N -- Artifact Name] |

**Gaps and Open Questions:**
> `[source: Stage N -- Artifact Name]` per gap assessment

**Decision Readiness** (one sentence):

Gate record Stage 5 entry: [ Pass / Fail ]
Gate record Stage 5 exit: [ Pass / Fail ]

---

### Output: Evidence Brief

Compile all artifacts into one self-contained document: title, topic context, Gate Record
(filled), Consolidated Invocation Audit Table (25 rows), Provenance Compliance Summary,
stage findings, hypothesis register, synthesis, gaps, decision readiness sentence.

**Consolidated Invocation Audit Table:**

| # | Rule | Stage | Stage-Index | Form | Pass/Fail |
|---|------|-------|-------------|------|-----------|
| 1-25 | (append inline at each invocation) | | | | |

**DELIVERY GATE FINAL CHECK (C-35):**
- Row count: [ ] / 25
- Gate record cells all-Pass: [ Yes / No ]
- All scope-restricted claims have provenance blocks: [ Yes / No ]

**This brief SHALL NOT be closed until all three delivery gate conditions above read Yes/Pass.**
Count != 25 blocks delivery. Gate fail blocks delivery. Missing provenance blocks delivery.

---

---

## V-03 -- Axis: Phrasing Register (Full Interrogative-Imperative)

**Variation axis**: Every governance element -- rule invocations, gate conditions, provenance
checks, delivery gate -- uses interrogative phrasing with a required binary response. The
executor cannot passively note compliance; they must answer each question. A non-answer is
visible as a structural gap. Passive tags ("ATTRIBUTION RULE applied") are replaced with
interrogative commands ("Has ATTRIBUTION RULE been applied? [ Yes / No ]"). The phrasing
register converts rule invocation from a stamp into a test.

**Hypothesis**: Interrogative phrasing eliminates the passive-compliance failure mode: an
executor who writes "ATTRIBUTION RULE invoked" has stamped a label. An executor who must
answer "Has every finding in this stage been labeled with its source stage? [ Yes / No ]"
cannot close the field without making a binary decision. The phrasing itself compels honest
invocation rather than performative tagging.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Cannot be modified after Stage 1 executes.

---

#### Governing Rules (5 equal-tier peers)

**PROVENANCE RULE** `[scope: S3(+), S4(+), S5(+), S1(-), S2(-)]`
_Question form_: Has every claim in this scope-restricted stage been tagged with `[source: Stage N -- Artifact Name]` naming a specific artifact within this role's declared access scope? [ Yes / No ]
Scope-restricted stages: Stage 3, Stage 4, Stage 5. A missing tag is a structural gap. A tag
naming an out-of-scope artifact is a charter violation.

**ATTRIBUTION RULE** `[scope: S1(+), S2(+), S3(+), S4(+), S5(+)]`
_Question form_: Has every material claim in this stage been labeled with its source-stage
identifier (`[web]`, `[intel]`, `[hypothesis]`, `[analysis]`, `[synthesis]`)? [ Yes / No ]

**CALIBRATION RULE** `[scope: S4(+), S5(+), S1(-), S2(-), S3(-)]`
_Question form_: Are at least two distinct confidence levels present in this stage's output?
[ Yes / No ] If uniform -- recalibrate before advancing.

**FALSIFICATION RULE** `[scope: S3(+), S5(+), S1(-), S2(-), S4(-)]`
_Question form_ (S3): Does every declared hypothesis carry an explicit falsification condition? [ Yes / No ]
_Question form_ (S5): Does every hypothesis in the register carry a final status (Supported / Refuted / Indeterminate)? [ Yes / No ]

**SEQUENCING RULE** `[scope: S1(+), S2(+), S3(+), S4(-), S5(-)]`
_Question form_: Has this stage begun before any hypothesis has been declared (for S1-S2)?
Or: Did Stage 1 and Stage 2 complete before this stage began (for S3)? [ Yes / No ]
Rule principle: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis."

Peer declaration: all 5 rules are equal-tier. Count = 5. This declaration auto-updates.

---

#### Coverage Map

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|----|----------|----------|
| ATTRIBUTION | + | + | + | + | + | 5 | 0 |
| CALIBRATION | - | - | - | + | + | 2 | 3 |
| FALSIFICATION | - | - | + | - | + | 2 | 3 |
| SEQUENCING | + | + | + | - | - | 3 | 2 |
| PROVENANCE | - | - | + | + | + | 3 | 2 |
| **Total** | | | | | | **15** | **10** |

**Checksum (C-33):** Is the expected total 25 invocation artifacts (5 rules x 5 stages =
15 positive + 10 negative)? [ Yes -- this value is pre-declared and immutable ]

**DELIVERY GATE (C-35):** Will this brief remain open until the consolidated audit table
contains exactly 25 rows? [ Yes -- this is a structural constraint, not a preference. A count
!= 25 blocks delivery. This brief SHALL NOT be closed with count != 25. ]

---

#### Role Roster (access scopes declared per C-32)

| Stage | Role | Authorized to read |
|-------|------|--------------------|
| Stage 1 | Web Evidence Collector | External sources only |
| Stage 2 | Intelligence Analyst | ARTIFACT-S1 only |
| Stage 3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 |
| Stage 4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 |
| Stage 5 | Synthesis Director | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 + ARTIFACT-S4 |

---

#### Gate Record Template

| Stage | Role | Entry: Pass? | Exit: Pass? |
|-------|------|-------------|------------|
| Stage 1 | Web Evidence Collector | [ Pass ] (first stage) | [ ] |
| Stage 2 | Intelligence Analyst | [ ] | [ ] |
| Stage 3 | Hypothesis Architect | [ ] | [ ] |
| Stage 4 | Evidence Analyst | [ ] | [ ] |
| Stage 5 | Synthesis Director | [ ] | [ ] |

---

### Stage 1 -- Web Evidence Collector

**ROLE: Web Evidence Collector | ACCESS SCOPE: External sources only**

_Before executing -- answer each question:_

**ATTRIBUTION RULE [Stage 1 of 5]**: Will every finding in Stage 1 be labeled `[web]`? [ Yes / No ]
**CALIBRATION RULE [Stage 1 of 5]**: Does CALIBRATION apply at this evidence-collection stage? [ No -- confidence rating not yet applicable ]
**FALSIFICATION RULE [Stage 1 of 5]**: Does FALSIFICATION apply at this stage? [ No -- no hypotheses declared yet ]
**SEQUENCING RULE [Stage 1 of 5]**: Is this stage running before any hypothesis has been declared? [ Yes / No ]
**PROVENANCE RULE [Stage 1 of 5]**: Does PROVENANCE apply at this stage? [ No -- Stage 1 is not scope-restricted ]

Search **{{topic}}**: primary sources, recent publications, technical references, industry data,
quantitative studies. Label every finding `[web]`. Collect broadly without filtering for
expected conclusions.

_After executing -- answer each question:_

**ATTRIBUTION RULE [Stage 1 of 5]**: Has every finding been labeled `[web]`? [ Yes / No ]
**SEQUENCING RULE [Stage 1 of 5]**: Has any hypothesis been stated in this stage's output? [ No -- hypothesis not yet declared ]

Gate record Stage 1 exit: [ Pass / Fail ] (minimum 6 labeled findings; no hypothesis stated)

> **Role passes to: Stage 2 -- Intelligence Analyst.** Is Stage 1 exit gate all-Pass? [ Yes / No ]
> If No -- Stage 2 may not begin.

---

### Stage 2 -- Intelligence Analyst

**ROLE: Intelligence Analyst | ACCESS SCOPE: ARTIFACT-S1 only**

_Before executing:_

**ATTRIBUTION RULE [Stage 2 of 5]**: Will every new claim be labeled `[intel]`? [ Yes / No ]
**CALIBRATION RULE [Stage 2 of 5]**: Does CALIBRATION apply here? [ No -- intelligence review, not confidence rating ]
**FALSIFICATION RULE [Stage 2 of 5]**: Does FALSIFICATION apply here? [ No -- no hypotheses yet ]
**SEQUENCING RULE [Stage 2 of 5]**: Has Stage 1 completed with no hypothesis stated? [ Yes / No ]
**PROVENANCE RULE [Stage 2 of 5]**: Does PROVENANCE apply here? [ No -- Stage 2 is not scope-restricted ]

Gate record Stage 2 entry: [ Pass / Fail ] (is Stage 1 exit all-Pass?)

Apply judgment to ARTIFACT-S1: patterns, contradictions, evidence strength, gaps,
domain-specific considerations. Label every new claim `[intel]`. Do not state any hypothesis.

_After executing:_

**ATTRIBUTION RULE [Stage 2 of 5]**: Has every new claim been labeled `[intel]`? [ Yes / No ]
**SEQUENCING RULE [Stage 2 of 5]**: Has any hypothesis appeared in Stage 2 output? [ No ]

Gate record Stage 2 exit: [ Pass / Fail ] (landscape characterized; no hypothesis; all `[intel]`)

> **Role passes to: Stage 3 -- Hypothesis Architect.** Is Stage 2 exit gate all-Pass? [ Yes / No ]

---

### Stage 3 -- Hypothesis Architect

**ROLE: Hypothesis Architect | ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2**

_Before executing:_

**ATTRIBUTION RULE [Stage 3 of 5]**: Will every hypothesis cite specific ARTIFACT-S1 or ARTIFACT-S2 evidence? [ Yes / No ]
**CALIBRATION RULE [Stage 3 of 5]**: Does CALIBRATION apply here? [ No -- hypothesis declaration, not confidence rating ]
**FALSIFICATION RULE [Stage 3 of 5]**: Will every hypothesis carry an explicit falsification condition? [ Yes / No ]
**SEQUENCING RULE [Stage 3 of 5]**: Did Stage 1 and Stage 2 complete before this stage began? [ Yes / No ]
**PROVENANCE RULE [Stage 3 of 5]**: Will every claim in this stage carry a `[source: Stage N -- Artifact Name]` block naming ARTIFACT-S1 or ARTIFACT-S2? [ Yes / No ]

Gate record Stage 3 entry: [ Pass / Fail ] (Stage 1 + Stage 2 exit gates all-Pass?)

Declare 3-5 hypotheses. For each:

**H-NN**: [Falsifiable claim]
> Falsification condition: [Criterion for rejection]
> `[source: Stage N -- Artifact Name]` -- [Specific grounding evidence]

_After executing:_

**ATTRIBUTION RULE [Stage 3 of 5]**: Does every hypothesis cite ARTIFACT-S1 or ARTIFACT-S2? [ Yes / No ]
**FALSIFICATION RULE [Stage 3 of 5]**: Does every hypothesis carry a falsification condition? [ Yes / No ]
**SEQUENCING RULE [Stage 3 of 5]**: Did Stage 3 open only after Stage 1+2 exit gates passed? [ Yes / No ]
**PROVENANCE RULE [Stage 3 of 5]**: Does every claim in Stage 3 carry a provenance block naming only ARTIFACT-S1 or ARTIFACT-S2? [ Yes / No ]

Gate record Stage 3 exit: [ Pass / Fail ] (3-5 hypotheses; all with falsification conditions;
all claims with valid provenance blocks)

> **Role passes to: Stage 4 -- Evidence Analyst.** Is Stage 3 exit gate all-Pass? [ Yes / No ]

---

### Stage 4 -- Evidence Analyst

**ROLE: Evidence Analyst | ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3**

_Before executing:_

**ATTRIBUTION RULE [Stage 4 of 5]**: Will every analyzed claim carry a source-stage label? [ Yes / No ]
**CALIBRATION RULE [Stage 4 of 5]**: Will confidence ratings be non-uniform (2+ distinct levels)? [ Yes / No ]
**FALSIFICATION RULE [Stage 4 of 5]**: Does FALSIFICATION apply here? [ No -- hypotheses were declared in Stage 3 ]
**SEQUENCING RULE [Stage 4 of 5]**: Does SEQUENCING apply here? [ No -- post-hypothesis analysis stage ]
**PROVENANCE RULE [Stage 4 of 5]**: Will every claim carry a `[source: Stage N -- Artifact Name]` block naming an artifact from {ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3}? [ Yes / No ]

Gate record Stage 4 entry: [ Pass / Fail ] (Stages 1-3 exit gates all-Pass?)

For each hypothesis in ARTIFACT-S3:
- Supporting evidence: `[source: Stage N -- Artifact Name]` -- [finding]
- Challenging evidence: `[source: Stage N -- Artifact Name]` -- [finding]
- Confidence: High / Medium / Low
- Rationale: [evidence basis for confidence level]

_After executing:_

**ATTRIBUTION RULE [Stage 4 of 5]**: Does every claim carry a source-stage label? [ Yes / No ]
**CALIBRATION RULE [Stage 4 of 5]**: Are at least two distinct confidence levels present? [ Yes / No ] If uniform -- recalibrate now.
**PROVENANCE RULE [Stage 4 of 5]**: Does every claim carry a provenance block naming only {ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3}? [ Yes / No ]

Gate record Stage 4 exit: [ Pass / Fail ] (all hypotheses analyzed; 2+ confidence levels;
all claims with valid provenance blocks)

> **Role passes to: Stage 5 -- Synthesis Director.** Is Stage 4 exit gate all-Pass? [ Yes / No ]

---

### Stage 5 -- Synthesis Director

**ROLE: Synthesis Director | ACCESS SCOPE: ARTIFACT-S1 through ARTIFACT-S4**

_Before executing:_

**ATTRIBUTION RULE [Stage 5 of 5]**: Will every synthesis claim carry a source-stage label? [ Yes / No ]
**CALIBRATION RULE [Stage 5 of 5]**: Will confidence distribution remain non-uniform in synthesis? [ Yes / No ]
**FALSIFICATION RULE [Stage 5 of 5]**: Will every hypothesis receive a final status? [ Yes / No ]
**SEQUENCING RULE [Stage 5 of 5]**: Does SEQUENCING apply here? [ No -- terminal synthesis stage ]
**PROVENANCE RULE [Stage 5 of 5]**: Will every synthesis claim carry a `[source: Stage N -- Artifact Name]` block? [ Yes / No ]

Gate record Stage 5 entry: [ Pass / Fail ] (Stages 1-4 exit gates all-Pass?)

**Consensus** (ARTIFACT-S1 and ARTIFACT-S2 agree):
`[source: Stage N -- Artifact Name]` per claim

**Conflict** (ARTIFACT-S1 and ARTIFACT-S2 diverge -- name explicitly):
`[source: Stage N -- Artifact Name]` per claim

**Hypothesis Register:**

| H# | Hypothesis | Falsification Condition | Status | Confidence | Provenance |
|----|------------|------------------------|--------|------------|-----------|
| H-01 | ... | ... | Supported/Refuted/Indeterminate | High/Med/Low | [source: Stage N -- Artifact Name] |

**Gaps and Open Questions:**
> `[source: Stage N -- Artifact Name]` per gap

**Decision Readiness** (one sentence -- posture + gap if not ready):

_After executing:_

**ATTRIBUTION RULE [Stage 5 of 5]**: Do all synthesis claims carry source-stage labels? [ Yes / No ]
**CALIBRATION RULE [Stage 5 of 5]**: Is confidence distribution non-uniform? [ Yes / No ]
**FALSIFICATION RULE [Stage 5 of 5]**: Does every hypothesis carry final status? [ Yes / No ]
**PROVENANCE RULE [Stage 5 of 5]**: Do all synthesis claims carry provenance blocks? [ Yes / No ]

Gate record Stage 5 exit: [ Pass / Fail ] (all conditions met)

---

### Output: Evidence Brief

Compile into one document: title, topic context, Gate Record (filled), Consolidated Invocation
Audit Table, stage findings, hypothesis register, synthesis, gaps, decision readiness.

**Consolidated Invocation Audit Table** (25 rows required):

| # | Rule | Stage | Stage-Index | Form | Pass/Fail |
|---|------|-------|-------------|------|-----------|
| 1 | ATTRIBUTION | S1 | [Stage 1 of 5] | Binary | |
| 2 | CALIBRATION | S1 | [Stage 1 of 5] | Binary (negative) | |
| 3 | FALSIFICATION | S1 | [Stage 1 of 5] | Binary (negative) | |
| 4 | SEQUENCING | S1 | [Stage 1 of 5] | Binary | |
| 5 | PROVENANCE | S1 | [Stage 1 of 5] | Binary (negative) | |
| 6 | ATTRIBUTION | S2 | [Stage 2 of 5] | Binary | |
| 7 | CALIBRATION | S2 | [Stage 2 of 5] | Binary (negative) | |
| 8 | FALSIFICATION | S2 | [Stage 2 of 5] | Binary (negative) | |
| 9 | SEQUENCING | S2 | [Stage 2 of 5] | Binary | |
| 10 | PROVENANCE | S2 | [Stage 2 of 5] | Binary (negative) | |
| 11 | ATTRIBUTION | S3 | [Stage 3 of 5] | Binary | |
| 12 | CALIBRATION | S3 | [Stage 3 of 5] | Binary (negative) | |
| 13 | FALSIFICATION | S3 | [Stage 3 of 5] | Binary | |
| 14 | SEQUENCING | S3 | [Stage 3 of 5] | Binary | |
| 15 | PROVENANCE | S3 | [Stage 3 of 5] | Binary | |
| 16 | ATTRIBUTION | S4 | [Stage 4 of 5] | Binary | |
| 17 | CALIBRATION | S4 | [Stage 4 of 5] | Binary | |
| 18 | FALSIFICATION | S4 | [Stage 4 of 5] | Binary (negative) | |
| 19 | SEQUENCING | S4 | [Stage 4 of 5] | Binary (negative) | |
| 20 | PROVENANCE | S4 | [Stage 4 of 5] | Binary | |
| 21 | ATTRIBUTION | S5 | [Stage 5 of 5] | Binary | |
| 22 | CALIBRATION | S5 | [Stage 5 of 5] | Binary | |
| 23 | FALSIFICATION | S5 | [Stage 5 of 5] | Binary | |
| 24 | SEQUENCING | S5 | [Stage 5 of 5] | Binary (negative) | |
| 25 | PROVENANCE | S5 | [Stage 5 of 5] | Binary | |

**DELIVERY GATE INTERROGATIVE (C-35):**
- Does the audit table contain exactly 25 rows? [ Yes / No ]
- Are all gate record cells Pass? [ Yes / No ]
- Do all scope-restricted stage claims carry provenance blocks? [ Yes / No ]

Is this brief ready to close? [ Yes / No ] -- If No on any line above: brief remains open.
"This brief SHALL NOT be delivered while any delivery gate answer is No."

---

---

## V-04 -- Combined Axes: Provenance Tags + Delivery Gate as Interlocked Constraints

**Variation axes combined**: Output format (provenance tags as structured blocks) + Lifecycle
emphasis (delivery gate as opening constraint). The two R12 criteria are declared as mutually
reinforcing: the delivery gate cannot pass until provenance compliance is verified, and
provenance compliance is only verifiable because the blocks are structured, not inline.
C-34 and C-35 are interlocked: you cannot satisfy the gate without the structured blocks;
the structured blocks only matter because the gate checks them.

**Hypothesis**: C-34 and C-35 form a closed enforcement loop. C-35 (delivery gate) names
the condition: "all scope-restricted claims have provenance blocks." C-34 (structured blocks)
makes the condition checkable: scan for blocks, verify names, compare to access scope. An
executor who satisfies C-34 structurally cannot fail C-35's provenance check, and vice versa.
Declaring them as interlocked in the preamble makes the loop explicit before Stage 1 begins.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable.

---

#### INTERLOCKED DELIVERY CONSTRAINTS (C-34 + C-35)

These two constraints enforce each other. Both must pass before the brief may close.

**DELIVERY GATE (C-35):** This brief SHALL NOT be closed until:
1. Consolidated audit table row count = 25 (5 rules x 5 stages)
2. Every scope-restricted claim carries a `[source: Stage N -- Artifact Name]` provenance block

**PROVENANCE BLOCK REQUIREMENT (C-34):** Every claim in Stage 3, Stage 4, and Stage 5
carries a provenance annotation block in the format:
```
[source: Stage N -- Artifact Name]
```
The named artifact must be within the declaring role's access scope. The provenance block
is a required structural element -- not a comment or annotation. A claim with no block
is incomplete. A block naming an out-of-scope artifact is a charter violation (C-32 breach).

Interlock: The delivery gate (C-35) cannot pass while any scope-restricted claim lacks a
provenance block. Structured provenance blocks (C-34) are what make the delivery gate
checkable in O(n) time: scan all claims in Stage 3-5, check for `[source: ...]` presence,
verify artifact name against role access scope, close gate if all-Pass.

---

#### Rule Registry (5 peers)

**PROVENANCE RULE** `[scope: S3(+), S4(+), S5(+), S1(-), S2(-)]`
At every scope-restricted stage: has every claim been tagged `[source: Stage N -- Artifact Name]`
naming an artifact within this role's access scope? [ Yes / No ]

**ATTRIBUTION RULE** `[scope: S1(+), S2(+), S3(+), S4(+), S5(+)]`
At every stage: has every material claim been labeled with its source-stage identifier? [ Yes / No ]

**CALIBRATION RULE** `[scope: S4(+), S5(+), S1(-), S2(-), S3(-)]`
At analysis and synthesis: are at least two distinct confidence levels present? [ Yes / No ]

**FALSIFICATION RULE** `[scope: S3(+), S5(+), S1(-), S2(-), S4(-)]`
At hypothesis declaration: does every hypothesis carry a falsification condition? [ Yes / No ]
At synthesis: does every hypothesis carry a final status? [ Yes / No ]

**SEQUENCING RULE** `[scope: S1(+), S2(+), S3(+), S4(-), S5(-)]`
Evidence before hypothesis. "A hypothesis anchored before evidence gathering is a bias."
At S1-S2: Has any hypothesis been stated? [ No -- required ]
At S3: Did S1 and S2 complete before this stage? [ Yes / No ]

Peer declaration: 5 equal-tier rules. Count = 5. Auto-updates on addition.

---

#### Coverage Map and Checksums

| Rule | S1 | S2 | S3 | S4 | S5 | + | - |
|------|----|----|----|----|----|---|---|
| ATTRIBUTION | + | + | + | + | + | 5 | 0 |
| CALIBRATION | - | - | - | + | + | 2 | 3 |
| FALSIFICATION | - | - | + | - | + | 2 | 3 |
| SEQUENCING | + | + | + | - | - | 3 | 2 |
| PROVENANCE | - | - | + | + | + | 3 | 2 |
| **Total** | | | | | | **15** | **10** |

**Checksum (C-33):** 25 invocation artifacts = 15(+) + 10(-), derived from 5 x 5.
**DELIVERY GATE (C-35):** Audit table SHALL have row count = 25 before brief closes.

---

#### Role Roster and Access Scopes (C-32)

| Stage | Role | Authorized Artifacts | Valid Provenance Block Values |
|-------|------|---------------------|-------------------------------|
| Stage 1 | Web Evidence Collector | External only | (not scope-restricted) |
| Stage 2 | Intelligence Analyst | ARTIFACT-S1 | (not scope-restricted) |
| Stage 3 | Hypothesis Architect | ARTIFACT-S1, ARTIFACT-S2 | `[source: Stage 1 -- Web Findings Corpus]`, `[source: Stage 2 -- Intelligence Assessment]` |
| Stage 4 | Evidence Analyst | ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 | above + `[source: Stage 3 -- Hypothesis Register]` |
| Stage 5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 | above + `[source: Stage 4 -- Evidence Analysis]` |

---

#### Gate Record Template

| Stage | Role | Entry | Exit |
|-------|------|-------|------|
| Stage 1 | Web Evidence Collector | [ Pass ] | [ ] |
| Stage 2 | Intelligence Analyst | [ ] | [ ] |
| Stage 3 | Hypothesis Architect | [ ] | [ ] -- includes: all claims carry valid provenance blocks |
| Stage 4 | Evidence Analyst | [ ] | [ ] -- includes: all claims carry valid provenance blocks |
| Stage 5 | Synthesis Director | [ ] | [ ] -- includes: all claims carry valid provenance blocks |

---

### Stage 1 -- Web Evidence Collector

**ROLE: Web Evidence Collector | ACCESS SCOPE: External sources only**
(Not scope-restricted -- PROVENANCE RULE does not apply)

ATTRIBUTION RULE [Stage 1 of 5] -- All findings labeled `[web]`? [ Yes / No ]
CALIBRATION RULE [Stage 1 of 5] -- Applicable? [ No ]
FALSIFICATION RULE [Stage 1 of 5] -- Applicable? [ No ]
SEQUENCING RULE [Stage 1 of 5] -- Running before hypothesis? [ Yes / No ]
PROVENANCE RULE [Stage 1 of 5] -- Applicable? [ No -- S1 not scope-restricted ]

Search **{{topic}}**: primary sources, publications, technical references, industry data,
quantitative studies. Label every finding `[web]`. Minimum 6 findings. No hypothesis.

Gate record S1 exit: [ Pass / Fail ]

> **Role passes to: Stage 2 -- Intelligence Analyst.**
> ARTIFACT-S1 (Web Findings Corpus) produced and sealed.

---

### Stage 2 -- Intelligence Analyst

**ROLE: Intelligence Analyst | ACCESS SCOPE: ARTIFACT-S1 only**
(Not scope-restricted -- PROVENANCE RULE does not apply)

ATTRIBUTION RULE [Stage 2 of 5] -- All new claims labeled `[intel]`? [ Yes / No ]
CALIBRATION RULE [Stage 2 of 5] -- Applicable? [ No ]
FALSIFICATION RULE [Stage 2 of 5] -- Applicable? [ No ]
SEQUENCING RULE [Stage 2 of 5] -- No hypothesis yet? [ Yes / No ]
PROVENANCE RULE [Stage 2 of 5] -- Applicable? [ No -- S2 not scope-restricted ]

Apply expert judgment to ARTIFACT-S1: patterns, contradictions, strength, gaps.
Label every new claim `[intel]`. No hypothesis.

Gate record S2 exit: [ Pass / Fail ]

> **Role passes to: Stage 3 -- Hypothesis Architect.**
> ARTIFACT-S2 (Intelligence Assessment) produced and sealed.

---

### Stage 3 -- Hypothesis Architect

**ROLE: Hypothesis Architect | ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2**
**SCOPE-RESTRICTED: PROVENANCE RULE active. Every claim must carry a provenance block.**

Provenance block format for this stage:
- `[source: Stage 1 -- Web Findings Corpus]` -- grounding evidence from ARTIFACT-S1
- `[source: Stage 2 -- Intelligence Assessment]` -- grounding evidence from ARTIFACT-S2

Any other artifact name in a `[source: ...]` block is a charter violation (C-32 breach).

ATTRIBUTION RULE [Stage 3 of 5] -- Every hypothesis cites ARTIFACT-S1 or ARTIFACT-S2? [ Yes / No ]
CALIBRATION RULE [Stage 3 of 5] -- Applicable? [ No ]
FALSIFICATION RULE [Stage 3 of 5] -- Every hypothesis has a falsification condition? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5] -- Stages 1+2 complete before this stage? [ Yes / No ]
PROVENANCE RULE [Stage 3 of 5] -- Every claim carries a valid `[source: Stage N -- Artifact Name]` block? [ Yes / No ]

Declare 3-5 hypotheses in this format:

**H-NN**: [Claim]
> Falsification condition: [Rejection criterion]
> `[source: Stage 1 -- Web Findings Corpus]` or `[source: Stage 2 -- Intelligence Assessment]`
> Grounding: [specific finding from named artifact]

Gate record S3 exit: [ Pass / Fail ] -- includes: provenance blocks present and in-scope

> **Role passes to: Stage 4 -- Evidence Analyst.**
> ARTIFACT-S3 (Hypothesis Register) produced and sealed.

---

### Stage 4 -- Evidence Analyst

**ROLE: Evidence Analyst | ACCESS SCOPE: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3**
**SCOPE-RESTRICTED: PROVENANCE RULE active. Every claim must carry a provenance block.**

Valid provenance blocks at this stage:
- `[source: Stage 1 -- Web Findings Corpus]`
- `[source: Stage 2 -- Intelligence Assessment]`
- `[source: Stage 3 -- Hypothesis Register]`

ATTRIBUTION RULE [Stage 4 of 5] -- All analyzed claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5] -- 2+ distinct confidence levels present? [ Yes / No ]
FALSIFICATION RULE [Stage 4 of 5] -- Applicable? [ No ]
SEQUENCING RULE [Stage 4 of 5] -- Applicable? [ No ]
PROVENANCE RULE [Stage 4 of 5] -- Every claim carries a valid provenance block? [ Yes / No ]

For each hypothesis in ARTIFACT-S3:
- Supporting evidence:
  `[source: Stage N -- Artifact Name]` -- [specific finding]
- Challenging evidence:
  `[source: Stage N -- Artifact Name]` -- [specific finding]
- Confidence: High / Medium / Low
- Rationale: [basis for assignment]

Gate record S4 exit: [ Pass / Fail ] -- includes: 2+ confidence levels, all provenance blocks valid

> **Role passes to: Stage 5 -- Synthesis Director.**
> ARTIFACT-S4 (Evidence Analysis) produced and sealed.

---

### Stage 5 -- Synthesis Director

**ROLE: Synthesis Director | ACCESS SCOPE: ARTIFACT-S1 through ARTIFACT-S4**
**SCOPE-RESTRICTED: PROVENANCE RULE active. Every claim must carry a provenance block.**

ATTRIBUTION RULE [Stage 5 of 5] -- All synthesis claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5] -- Non-uniform confidence confirmed? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5] -- Every hypothesis has a final status? [ Yes / No ]
SEQUENCING RULE [Stage 5 of 5] -- Applicable? [ No ]
PROVENANCE RULE [Stage 5 of 5] -- Every synthesis claim carries a provenance block? [ Yes / No ]

**Consensus** (ARTIFACT-S1 and ARTIFACT-S2 agree):
> `[source: Stage N -- Artifact Name]` per consensus claim

**Conflict** (ARTIFACT-S1 and ARTIFACT-S2 diverge):
> `[source: Stage N -- Artifact Name]` per conflict claim

**Hypothesis Register:**

| H# | Hypothesis | Falsification Condition | Status | Confidence | Provenance |
|----|------------|------------------------|--------|------------|-----------|
| H-01 | ... | ... | Supported/Refuted/Indeterminate | High/Med/Low | [source: Stage N -- Artifact Name] |

**Gaps and Open Questions:**
> `[source: Stage N -- Artifact Name]` per gap

**Decision Readiness** (one sentence):

Gate record S5 exit: [ Pass / Fail ]

---

### Output: Evidence Brief

**INTERLOCKED DELIVERY CHECK:**

| Check | Status |
|-------|--------|
| Audit table row count = 25 | [ ] |
| All gate record cells Pass | [ ] |
| All Stage 3 claims carry valid provenance blocks | [ ] |
| All Stage 4 claims carry valid provenance blocks | [ ] |
| All Stage 5 claims carry valid provenance blocks | [ ] |

**DELIVERY GATE (C-35):** All rows above must be [ Pass ] before brief closes.
This brief SHALL NOT be delivered while any interlocked delivery check is unfilled or Fail.

**Consolidated Invocation Audit Table** (25 rows):

| # | Rule | Stage | Stage-Index | Form | Pass/Fail |
|---|------|-------|-------------|------|-----------|
| 1 | ATTRIBUTION | S1 | [Stage 1 of 5] | Binary | |
| 2 | CALIBRATION | S1 | [Stage 1 of 5] | Binary (negative) | |
| 3 | FALSIFICATION | S1 | [Stage 1 of 5] | Binary (negative) | |
| 4 | SEQUENCING | S1 | [Stage 1 of 5] | Binary | |
| 5 | PROVENANCE | S1 | [Stage 1 of 5] | Binary (negative) | |
| 6 | ATTRIBUTION | S2 | [Stage 2 of 5] | Binary | |
| 7 | CALIBRATION | S2 | [Stage 2 of 5] | Binary (negative) | |
| 8 | FALSIFICATION | S2 | [Stage 2 of 5] | Binary (negative) | |
| 9 | SEQUENCING | S2 | [Stage 2 of 5] | Binary | |
| 10 | PROVENANCE | S2 | [Stage 2 of 5] | Binary (negative) | |
| 11 | ATTRIBUTION | S3 | [Stage 3 of 5] | Binary | |
| 12 | CALIBRATION | S3 | [Stage 3 of 5] | Binary (negative) | |
| 13 | FALSIFICATION | S3 | [Stage 3 of 5] | Binary | |
| 14 | SEQUENCING | S3 | [Stage 3 of 5] | Binary | |
| 15 | PROVENANCE | S3 | [Stage 3 of 5] | Binary | |
| 16 | ATTRIBUTION | S4 | [Stage 4 of 5] | Binary | |
| 17 | CALIBRATION | S4 | [Stage 4 of 5] | Binary | |
| 18 | FALSIFICATION | S4 | [Stage 4 of 5] | Binary (negative) | |
| 19 | SEQUENCING | S4 | [Stage 4 of 5] | Binary (negative) | |
| 20 | PROVENANCE | S4 | [Stage 4 of 5] | Binary | |
| 21 | ATTRIBUTION | S5 | [Stage 5 of 5] | Binary | |
| 22 | CALIBRATION | S5 | [Stage 5 of 5] | Binary | |
| 23 | FALSIFICATION | S5 | [Stage 5 of 5] | Binary | |
| 24 | SEQUENCING | S5 | [Stage 5 of 5] | Binary (negative) | |
| 25 | PROVENANCE | S5 | [Stage 5 of 5] | Binary | |

Row count: [ ] / 25. Match checksum: [ Yes / No ]

---

---

## V-05 -- Combined Axes: Role Sequence + Provenance Embedded in Handoff Declarations

**Variation axes combined**: Role sequence (C-30 handoff declarations) + Provenance tags
(C-34) embedded in the transfer itself. The role handoff declaration is the natural enforcement
point for provenance: when a role passes authority to the next stage, it simultaneously
declares which of its output artifacts the next role may cite as provenance sources. The
handoff is not just "Role A passes to Role B" -- it is "Role A passes ARTIFACT-SN to Role B;
all claims by Role B citing ARTIFACT-SN MUST carry `[source: Stage N -- Artifact Name]`."

**Hypothesis**: Provenance requirements are most enforceable when embedded at the point of
artifact handoff rather than declared separately in a rule. A Hypothesis Architect who receives
ARTIFACT-S1 and ARTIFACT-S2 via explicit handoff declarations that say "all claims citing these
artifacts MUST carry provenance blocks" cannot claim ignorance of the requirement -- the
obligation is attached to the artifact at the moment of transfer. This makes provenance a
property of receipt, not a separate governance rule, while C-35 ensures the blocks accumulated
across all stages constitute a verifiable pre-delivery count.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable.

---

#### Rule Registry (5 peers; no rule is primary)

**ATTRIBUTION RULE** `[scope: S1(+), S2(+), S3(+), S4(+), S5(+)]`
Every material claim names its source stage. Labels: `[web]`, `[intel]`, `[hypothesis]`,
`[analysis]`, `[synthesis]`. Unattributed claims fail this rule.

**CALIBRATION RULE** `[scope: S4(+), S5(+), S1(-), S2(-), S3(-)]`
Confidence ratings vary. Uniform ratings are a calibration failure.
Guard: "Are at least two distinct confidence levels present?" [ Yes / No ]

**FALSIFICATION RULE** `[scope: S3(+), S5(+), S1(-), S2(-), S4(-)]`
Every hypothesis carries a falsification condition and a final status.

**SEQUENCING RULE** `[scope: S1(+), S2(+), S3(+), S4(-), S5(-)]`
Evidence before hypothesis. "A hypothesis anchored before evidence gathering is a bias."

**PROVENANCE RULE** `[scope: S3(+), S4(+), S5(+), S1(-), S2(-)]`
At each scope-restricted stage: every claim carries `[source: Stage N -- Artifact Name]`
naming an artifact received via handoff to this role. The provenance obligation is declared
at the handoff point -- not separately. A claim with no provenance block, or one naming
an artifact not received via handoff, fails this rule.

Peer declaration: ATTRIBUTION, CALIBRATION, FALSIFICATION, SEQUENCING, PROVENANCE are
equal-tier peers. Count = 5. Coverage map: 5 x 5 = 25 cells.

---

#### Coverage Map

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|----|----------|----------|
| ATTRIBUTION | + | + | + | + | + | 5 | 0 |
| CALIBRATION | - | - | - | + | + | 2 | 3 |
| FALSIFICATION | - | - | + | - | + | 2 | 3 |
| SEQUENCING | + | + | + | - | - | 3 | 2 |
| PROVENANCE | - | - | + | + | + | 3 | 2 |
| **Total** | | | | | | **15** | **10** |

**Checksum (C-33):** 25 invocation artifacts = 15(+) + 10(-), from 5 rules x 5 stages.

**DELIVERY GATE (C-35):** This brief SHALL NOT be closed until audit table row count = 25.
A count != 25 is a delivery blocker. The delivery gate is satisfied by provenance blocks
accumulated via handoff declarations -- not by a post-hoc audit.

---

#### Role Roster (access scopes via handoff protocol)

| Stage | Role | Receives From | Provenance Obligation |
|-------|------|--------------|-----------------------|
| Stage 1 | Web Evidence Collector | External sources | No provenance blocks required (not scope-restricted) |
| Stage 2 | Intelligence Analyst | ARTIFACT-S1 via S1 handoff | No provenance blocks required (ARTIFACT-S1 is the only source; `[intel]` attribution sufficient) |
| Stage 3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 via S2 handoff | MUST cite ARTIFACT-S1 or ARTIFACT-S2 with `[source: Stage N -- Artifact Name]` per claim |
| Stage 4 | Evidence Analyst | ARTIFACT-S1+S2+S3 via S3 handoff | MUST cite authorized artifacts with `[source: Stage N -- Artifact Name]` per claim |
| Stage 5 | Synthesis Director | ARTIFACT-S1+S2+S3+S4 via S4 handoff | MUST cite any prior artifact with `[source: Stage N -- Artifact Name]` per claim |

---

#### Gate Record Template

| Stage | Role | Entry | Exit |
|-------|------|-------|------|
| Stage 1 | Web Evidence Collector | [ Pass ] (first) | [ ] |
| Stage 2 | Intelligence Analyst | [ ] | [ ] |
| Stage 3 | Hypothesis Architect | [ ] | [ ] |
| Stage 4 | Evidence Analyst | [ ] | [ ] |
| Stage 5 | Synthesis Director | [ ] | [ ] |

---

### Stage 1 -- Web Evidence Collector

**ROLE: Web Evidence Collector**
Receives from: External sources. No prior handoffs.
This role is not scope-restricted. PROVENANCE RULE does not apply.

ATTRIBUTION RULE [Stage 1 of 5] -- All findings labeled `[web]`? [ Yes / No ]
CALIBRATION RULE [Stage 1 of 5] -- Applicable? [ No ]
FALSIFICATION RULE [Stage 1 of 5] -- Applicable? [ No ]
SEQUENCING RULE [Stage 1 of 5] -- Running before any hypothesis? [ Yes / No ]
PROVENANCE RULE [Stage 1 of 5] -- Applicable? [ No -- not scope-restricted ]

Search **{{topic}}**: primary sources, publications, technical references, industry data,
quantitative studies. Label every finding `[web]`. Minimum 6 findings. No hypothesis.

Gate record S1 exit: [ Pass / Fail ]

> **Role passes to: Stage 2 -- Intelligence Analyst.**
>
> HANDOFF DECLARATION:
> ARTIFACT-S1 (Web Findings Corpus) is hereby transferred to Intelligence Analyst.
> Intelligence Analyst is authorized to read ARTIFACT-S1 only.
> Intelligence Analyst is not scope-restricted; `[intel]` attribution satisfies ATTRIBUTION RULE.
> No provenance block requirement at Stage 2 (PROVENANCE RULE not yet active).

---

### Stage 2 -- Intelligence Analyst

**ROLE: Intelligence Analyst**
Receives from: Stage 1 handoff -- ARTIFACT-S1 only.
This role is not scope-restricted. PROVENANCE RULE does not apply.

ATTRIBUTION RULE [Stage 2 of 5] -- All new claims labeled `[intel]`? [ Yes / No ]
CALIBRATION RULE [Stage 2 of 5] -- Applicable? [ No ]
FALSIFICATION RULE [Stage 2 of 5] -- Applicable? [ No ]
SEQUENCING RULE [Stage 2 of 5] -- No hypothesis yet? [ Yes / No ]
PROVENANCE RULE [Stage 2 of 5] -- Applicable? [ No -- not scope-restricted ]

Apply expert judgment to ARTIFACT-S1: patterns, contradictions, strength, gaps,
domain considerations. Label every new claim `[intel]`. No hypothesis.

Gate record S2 exit: [ Pass / Fail ]

> **Role passes to: Stage 3 -- Hypothesis Architect.**
>
> HANDOFF DECLARATION:
> ARTIFACT-S2 (Intelligence Assessment) is hereby transferred to Hypothesis Architect.
> Hypothesis Architect receives: ARTIFACT-S1 + ARTIFACT-S2.
> **PROVENANCE OBLIGATION ACTIVATES:** Hypothesis Architect is scope-restricted.
> Every claim produced in Stage 3 MUST carry one of:
> - `[source: Stage 1 -- Web Findings Corpus]`
> - `[source: Stage 2 -- Intelligence Assessment]`
> Any other provenance block value is a charter violation. Any claim with no provenance
> block is a structural gap (C-34). PROVENANCE RULE is active for Stage 3.

---

### Stage 3 -- Hypothesis Architect

**ROLE: Hypothesis Architect**
Receives from: Stage 2 handoff -- ARTIFACT-S1 + ARTIFACT-S2.
**SCOPE-RESTRICTED: PROVENANCE RULE active per Stage 2 handoff declaration.**
Authorized provenance values: `[source: Stage 1 -- Web Findings Corpus]`,
`[source: Stage 2 -- Intelligence Assessment]`

ATTRIBUTION RULE [Stage 3 of 5] -- Every hypothesis cites authorized artifact? [ Yes / No ]
CALIBRATION RULE [Stage 3 of 5] -- Applicable? [ No ]
FALSIFICATION RULE [Stage 3 of 5] -- Every hypothesis has a falsification condition? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5] -- Stages 1+2 complete before this stage? [ Yes / No ]
PROVENANCE RULE [Stage 3 of 5] -- Every claim carries an authorized provenance block? [ Yes / No ]

Declare 3-5 hypotheses:

**H-NN**: [Claim]
> Falsification condition: [Rejection criterion]
> `[source: Stage 1 -- Web Findings Corpus]` or `[source: Stage 2 -- Intelligence Assessment]`
> Grounding: [specific evidence from named artifact]

Gate record S3 exit: [ Pass / Fail ] -- includes: all claims carry authorized provenance blocks

> **Role passes to: Stage 4 -- Evidence Analyst.**
>
> HANDOFF DECLARATION:
> ARTIFACT-S3 (Hypothesis Register) is hereby transferred to Evidence Analyst.
> Evidence Analyst receives: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3.
> **PROVENANCE OBLIGATION CONTINUES:** Evidence Analyst is scope-restricted.
> Every claim produced in Stage 4 MUST carry one of:
> - `[source: Stage 1 -- Web Findings Corpus]`
> - `[source: Stage 2 -- Intelligence Assessment]`
> - `[source: Stage 3 -- Hypothesis Register]`
> Any other value is a charter violation. Any claim with no block is a structural gap.

---

### Stage 4 -- Evidence Analyst

**ROLE: Evidence Analyst**
Receives from: Stage 3 handoff -- ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3.
**SCOPE-RESTRICTED: PROVENANCE RULE active per Stage 3 handoff declaration.**

ATTRIBUTION RULE [Stage 4 of 5] -- All claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5] -- 2+ distinct confidence levels present? [ Yes / No ]
FALSIFICATION RULE [Stage 4 of 5] -- Applicable? [ No ]
SEQUENCING RULE [Stage 4 of 5] -- Applicable? [ No ]
PROVENANCE RULE [Stage 4 of 5] -- Every claim carries an authorized provenance block? [ Yes / No ]

For each hypothesis in ARTIFACT-S3:
- Supporting evidence:
  `[source: Stage N -- Artifact Name]` -- [specific finding]
- Challenging evidence:
  `[source: Stage N -- Artifact Name]` -- [specific finding]
- Confidence: High / Medium / Low -- [rationale]

Calibration guard: if all ratings uniform, recalibrate.

Gate record S4 exit: [ Pass / Fail ] -- includes: 2+ confidence levels, all provenance blocks valid

> **Role passes to: Stage 5 -- Synthesis Director.**
>
> HANDOFF DECLARATION:
> ARTIFACT-S4 (Evidence Analysis) is hereby transferred to Synthesis Director.
> Synthesis Director receives: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 + ARTIFACT-S4.
> **PROVENANCE OBLIGATION CONTINUES:** Synthesis Director is scope-restricted.
> Every synthesis claim MUST carry one of the four authorized artifact names as a provenance block.
> No claim may appear in Stage 5 without a `[source: Stage N -- Artifact Name]` block.
> DELIVERY GATE: after Stage 5 completes, the audit table must contain exactly 25 rows.

---

### Stage 5 -- Synthesis Director

**ROLE: Synthesis Director**
Receives from: Stage 4 handoff -- ARTIFACT-S1 through ARTIFACT-S4.
**SCOPE-RESTRICTED: PROVENANCE RULE active per Stage 4 handoff declaration.**
This is the terminal stage. No further handoffs.

ATTRIBUTION RULE [Stage 5 of 5] -- All synthesis claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5] -- Non-uniform confidence confirmed? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5] -- Every hypothesis has final status? [ Yes / No ]
SEQUENCING RULE [Stage 5 of 5] -- Applicable? [ No ]
PROVENANCE RULE [Stage 5 of 5] -- Every claim carries a provenance block for an authorized artifact? [ Yes / No ]

**Consensus** (ARTIFACT-S1 and ARTIFACT-S2 agree):
> `[source: Stage N -- Artifact Name]` per consensus claim

**Conflict** (ARTIFACT-S1 and ARTIFACT-S2 diverge -- name explicitly):
> `[source: Stage N -- Artifact Name]` per conflict claim

**Hypothesis Register:**

| H# | Hypothesis | Falsification Condition | Status | Confidence | Provenance |
|----|------------|------------------------|--------|------------|-----------|
| H-01 | ... | ... | Supported/Refuted/Indeterminate | High/Med/Low | [source: Stage N -- Artifact Name] |

**Gaps and Open Questions:**
> `[source: Stage N -- Artifact Name]` per gap

**Decision Readiness** (one sentence -- posture; if not ready, name the gap):

Gate record S5 exit: [ Pass / Fail ]

---

### Output: Evidence Brief

**DELIVERY GATE FINAL CHECK (C-35):**

| Condition | Status |
|-----------|--------|
| Audit table row count = 25 | [ ] |
| All gate record cells Pass | [ ] |
| Stage 3: all claims carry provenance blocks from handoff-authorized artifacts | [ ] |
| Stage 4: all claims carry provenance blocks from handoff-authorized artifacts | [ ] |
| Stage 5: all claims carry provenance blocks from handoff-authorized artifacts | [ ] |

**This brief SHALL NOT be closed until all five delivery gate conditions are Pass.**
A count != 25 blocks delivery. An unfilled gate cell blocks delivery.
A scope-restricted claim without a provenance block blocks delivery.

Compile all artifacts into one document: title, topic context, Gate Record (filled),
Consolidated Invocation Audit Table (25 rows), stage findings, hypothesis register,
synthesis (consensus/conflict separated), gaps, decision readiness sentence.

**Consolidated Invocation Audit Table** (25 rows = checksum):

| # | Rule | Stage | Stage-Index | Form | Pass/Fail |
|---|------|-------|-------------|------|-----------|
| 1 | ATTRIBUTION | S1 | [Stage 1 of 5] | Binary | |
| 2 | CALIBRATION | S1 | [Stage 1 of 5] | Binary (negative) | |
| 3 | FALSIFICATION | S1 | [Stage 1 of 5] | Binary (negative) | |
| 4 | SEQUENCING | S1 | [Stage 1 of 5] | Binary | |
| 5 | PROVENANCE | S1 | [Stage 1 of 5] | Binary (negative) | |
| 6 | ATTRIBUTION | S2 | [Stage 2 of 5] | Binary | |
| 7 | CALIBRATION | S2 | [Stage 2 of 5] | Binary (negative) | |
| 8 | FALSIFICATION | S2 | [Stage 2 of 5] | Binary (negative) | |
| 9 | SEQUENCING | S2 | [Stage 2 of 5] | Binary | |
| 10 | PROVENANCE | S2 | [Stage 2 of 5] | Binary (negative) | |
| 11 | ATTRIBUTION | S3 | [Stage 3 of 5] | Binary | |
| 12 | CALIBRATION | S3 | [Stage 3 of 5] | Binary (negative) | |
| 13 | FALSIFICATION | S3 | [Stage 3 of 5] | Binary | |
| 14 | SEQUENCING | S3 | [Stage 3 of 5] | Binary | |
| 15 | PROVENANCE | S3 | [Stage 3 of 5] | Binary | |
| 16 | ATTRIBUTION | S4 | [Stage 4 of 5] | Binary | |
| 17 | CALIBRATION | S4 | [Stage 4 of 5] | Binary | |
| 18 | FALSIFICATION | S4 | [Stage 4 of 5] | Binary (negative) | |
| 19 | SEQUENCING | S4 | [Stage 4 of 5] | Binary (negative) | |
| 20 | PROVENANCE | S4 | [Stage 4 of 5] | Binary | |
| 21 | ATTRIBUTION | S5 | [Stage 5 of 5] | Binary | |
| 22 | CALIBRATION | S5 | [Stage 5 of 5] | Binary | |
| 23 | FALSIFICATION | S5 | [Stage 5 of 5] | Binary | |
| 24 | SEQUENCING | S5 | [Stage 5 of 5] | Binary (negative) | |
| 25 | PROVENANCE | S5 | [Stage 5 of 5] | Binary | |

Row count: [ ] / 25. Checksum match: [ Yes / No ]
