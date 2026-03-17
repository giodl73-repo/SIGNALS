---
skill: quest-variate
skill_target: campaign-evidence
date: 2026-03-17
round: 14
rubric_version: 14
---

# Variates: campaign-evidence (Round 14)

Five complete, runnable skill body prompts. Single-axis variations first (V-01 through V-03),
combined axes second (V-04 through V-05).

**Structural signals from R13 PASS+ analysis driving R14 variation axes:**

- **Signal 1 (C-35 candidate):** A single binary invocation — even in interrogative form — can
  be answered "Yes" prospectively and never revisited once the stage produces output. Splitting
  every applicable invocation into a pre-execution commitment checkpoint (answered before the
  stage writes anything) and a post-execution verification checkpoint (answered after the stage
  closes) creates a two-record artifact. If the pre-answer is "Yes" and the stage produces
  non-compliant output, the post-check must answer "No" — the discrepancy is visible across
  two records that cannot be collapsed into a single act.

- **Signal 2 (C-36 candidate):** In R13 V-01, PROVENANCE RULE is activated at the handoff
  boundary immediately preceding each scope-restricted stage. But the handoff only names the
  receiving role and its artifacts; it does not enumerate which specific artifacts carry
  provenance obligations. Moving artifact enumeration into the handoff body itself — naming
  each transferred artifact and marking "PROVENANCE RULE: activated for [Artifact A],
  [Artifact B] at this boundary" — converts provenance from a role-charter lookup into a
  live transfer event. A receiving role cannot claim ignorance; the obligation was named at
  the moment of receipt, attached to specific artifacts.

**Baseline inherited from R13 (all R14 variates must satisfy):**

Coverage map (5 rules × 5 stages = 25 cells):

| Rule | S1: Web | S2: Intel | S3: Hypo | S4: Analysis | S5: Synth | Positive | Negative |
|------|---------|-----------|----------|--------------|-----------|----------|----------|
| ATTRIBUTION  | + | + | + | + | + | 5 | 0 |
| CALIBRATION  | - | - | - | + | + | 2 | 3 |
| FALSIFICATION| - | - | + | - | + | 2 | 3 |
| SEQUENCING   | + | + | + | - | - | 3 | 2 |
| PROVENANCE   | - | - | + | + | + | 3 | 2 |
| **Total**    |   |   |   |   |   | **15** | **10** |

**R14 checkpoint checksum (C-35 adds dual-phase to all positive cells):**
- Positive cells: 15 × 2 phases = 30 checkpoint pairs
- Negative cells: 10 × 1 = 10 negative invocations
- Total invocation artifacts: **40**

**C-36 requirement (new in R14):** Every handoff declaration enumerates all artifacts
being transferred AND explicitly states PROVENANCE RULE activation status at that boundary —
even for non-scope-restricted stages (where the declaration reads "PROVENANCE RULE: not yet
activated at this boundary — Stage N+1 is not scope-restricted").

**Role names (consistent across all variates):**
- Stage 1: Web Evidence Collector
- Stage 2: Intelligence Analyst
- Stage 3: Hypothesis Architect
- Stage 4: Evidence Analyst
- Stage 5: Synthesis Director

**R13 baseline requirements inherited:**
- Universal binary `[ Yes / No ]` on all applicable invocations (C-22)
- Stage-index suffix `[Stage N of 5]` on every invocation (C-23)
- Entry and exit conditions per stage (C-24)
- Gate record pre-templated in preamble with blank cells (C-27)
- Named role + "Role passes to:" transfer at each boundary (C-30)
- Negative invocation at every non-applicable stage (C-31)
- Role access scope declared per stage (C-32)
- Invocation matrix total pre-declared as derivable checksum (C-33)
- Provenance tags `[source: Stage N -- Artifact Name]` in scope-restricted stages (C-34)

---

## V-01 -- Axis: Role Sequence (Temporal Boundary Markers Separate Pre from Post)

**Variation axis:** Each stage body is split into three named zones by explicit boundary
markers: `-- GOVERNANCE PRE-EXECUTION COMMITMENT --`, `-- STAGE EXECUTION OPEN --`, and
`-- STAGE EXECUTION CLOSE / POST-EXECUTION VERIFICATION --`. The pre-execution commitment
block must be answered before any content is written in the execution zone. The post-execution
verification block opens only after the execution zone closes. This makes the temporal
separation between C-35's two phases a structural property of the document layout — not a
prose instruction to "answer before writing."

**Hypothesis:** Explicit zone boundaries (PRE / EXECUTION / POST) enforce temporal separation
mechanically: a reader scanning the document can verify that the pre-block precedes any
stage output and the post-block follows it, without interpretive judgment. If the execution
zone contains hypothesis text and the pre-block's FALSIFICATION pre-check is answered "Yes
(will include falsification conditions)" — but the post-check answers "No (did not)" — the
discrepancy is visible across two geographically separated sections of the document, not
collapsible into a single row edit.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable — cannot be modified after any stage executes.
This document is a commitment, not a record.

---

#### Rule Registry (all five rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); both PRE and POST phases]`
Every material claim names its source stage via label: `[web]` S1, `[intel]` S2,
`[hypothesis]` S3, `[analysis]` S4, `[synthesis]` S5. An unlabeled claim is unattributed.

**CALIBRATION RULE** `[invoked at: S1(-), S2(-), S3(-), S4(+), S5(+); both PRE and POST phases at applicable stages]`
Confidence ratings must vary across findings. Uniform ratings (all High, all Medium, all Low)
are a calibration failure. Anti-uniformity guard: if all confidence ratings at any positive
invocation stage are identical, CALIBRATION fails. State distribution explicitly at S4 and S5.

**FALSIFICATION RULE** `[invoked at: S1(-), S2(-), S3(+), S4(-), S5(+); both PRE and POST phases at applicable stages]`
Each hypothesis carries an explicit falsification condition. Final status options:
Supported / Refuted / Indeterminate. A hypothesis without a falsification condition is a belief.

**SEQUENCING RULE** `[invoked at: S1(+), S2(+), S3(+), S4(-), S5(-); both PRE and POST phases at applicable stages]`
Evidence stages (S1, S2) complete before hypothesis declaration (S3). Named principle:
"A hypothesis anchored before evidence gathering is a bias, not a hypothesis." This sequencing
decision is a named governance rule so any reader can cite it by identifier.

**PROVENANCE RULE** `[invoked at: S1(-), S2(-), S3(+), S4(+), S5(+); both PRE and POST phases at applicable stages]`
This rule is activated exclusively at the handoff boundary preceding each scope-restricted
stage — not by the role roster. Every claim in a scope-restricted stage (S3, S4, S5) carries
`[source: Stage N -- Artifact Name]`. A claim without a provenance tag is a structural gap.

Peer declaration: all five rules are equal-tier. Adding a sixth peer rule propagates
automatically through the coverage map and checksum; no static integers require manual update.

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

#### Coverage Map (immutable — sealed before Stage 1; cannot be modified after execution begins)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION  | + | + | + | + | + |
| CALIBRATION  | - | - | - | + | + |
| FALSIFICATION| - | - | + | - | + |
| SEQUENCING   | + | + | + | - | - |
| PROVENANCE   | - | - | + | + | + |

Invocation checksum: **40 artifacts** = (15 positive cells × 2 phases) + (10 negative cells × 1)
= 30 PRE/POST checkpoint pairs + 10 negative invocations. Derived from map dimensions;
updates automatically if rules or stages are added.

---

#### Gate Record Template (pre-instantiated — blank cells filled during execution)

| Stage | Role | Entry Condition | Entry Status | Exit Condition | Exit Status |
|-------|------|----------------|:---:|----------------|:---:|
| S1 | Web Evidence Collector | First stage — no prerequisites | Pass | 6+ labeled findings; no hypothesis stated | [ ] |
| S2 | Intelligence Analyst | S1 exit Pass; handoff S1→S2 complete | [ ] | Evidence landscape characterized; no hypothesis; all `[intel]` | [ ] |
| S3 | Hypothesis Architect | S2 exit Pass; handoff S2→S3 complete + PROVENANCE activated | [ ] | 3-5 hypotheses with falsification conditions; all carry provenance tags | [ ] |
| S4 | Evidence Analyst | S3 exit Pass; handoff S3→S4 complete + PROVENANCE activated | [ ] | All hypotheses analyzed; 2+ confidence levels; all carry provenance tags | [ ] |
| S5 | Synthesis Director | S4 exit Pass; handoff S4→S5 complete + PROVENANCE activated | [ ] | Synthesis complete; consensus/conflict separated; decision verdict one sentence | [ ] |

---

### STAGE EXECUTION

Do not advance to Stage N+1 until Stage N's exit gate is all-Pass and its handoff block
is complete. The handoff block authorizes the next stage to open.

---

### Stage 1 -- Web Evidence Collector

**Entry gate:**

| Condition | Status |
|-----------|--------|
| First stage — no prior stages required | Pass |
| No hypothesis has been stated anywhere in this document | Pass |

---
-- GOVERNANCE PRE-EXECUTION COMMITMENT -- Stage 1 of 5 --
Answer before writing any Stage 1 content:

ATTRIBUTION [S1 of 5] PRE: Will all findings be labeled `[web]`? [ Yes / No ]
CALIBRATION [S1 of 5] PRE: Applicable at evidence collection? [ No — does not apply ]
FALSIFICATION [S1 of 5] PRE: Applicable before hypothesis declaration? [ No — does not apply ]
SEQUENCING [S1 of 5] PRE: Will this stage produce only evidence (no hypotheses)? [ Yes / No ]
PROVENANCE [S1 of 5] PRE: Applicable at a non-scope-restricted stage? [ No — not yet activated ]

---
-- STAGE EXECUTION OPEN -- Stage 1 --

Conduct structured web research on $ARGUMENTS. Search for: primary sources, recent
publications, technical data, industry reports, expert commentary, quantitative evidence.
Label every finding `[web]`. Do not state hypotheses. Collect broadly.

---
-- STAGE EXECUTION CLOSE / POST-EXECUTION VERIFICATION -- Stage 1 of 5 --
Answer after Stage 1 content above is complete:

ATTRIBUTION [S1 of 5] POST: Are all findings labeled `[web]`? [ Yes / No ]
CALIBRATION [S1 of 5] POST: N/A confirmed — no confidence ratings at evidence collection? [ Yes ]
FALSIFICATION [S1 of 5] POST: N/A confirmed — no hypothesis declared? [ Yes ]
SEQUENCING [S1 of 5] POST: No hypothesis appears in Stage 1 output? [ Yes / No ]
PROVENANCE [S1 of 5] POST: N/A confirmed — Stage 1 is not scope-restricted? [ Yes ]

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 6+ findings documented, each labeled `[web]` | [ Pass / Fail ] |
| No hypothesis stated anywhere in Stage 1 output | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S1 to S2 (C-36):**

> **Role passes to: Stage 2 -- Intelligence Analyst.**
> Artifacts enumerated for transfer:
> - ARTIFACT-S1: Web Findings Corpus
>
> Intelligence Analyst authorized reads: ARTIFACT-S1 only.
>
> **PROVENANCE RULE status at this boundary:** NOT activated.
> Stage 2 (Intelligence Analyst) is not scope-restricted. Provenance tagging per claim
> is not required at Stage 2. PROVENANCE RULE will be activated at the S2→S3 handoff.

---

### Stage 2 -- Intelligence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S1 exit gate is all-Pass | [ Pass / Fail ] |
| Handoff block S1→S2 is complete | [ Pass / Fail ] |
| No hypothesis has been stated anywhere | [ Pass / Fail ] |

---
-- GOVERNANCE PRE-EXECUTION COMMITMENT -- Stage 2 of 5 --
Answer before writing any Stage 2 content:

ATTRIBUTION [S2 of 5] PRE: Will all new claims be labeled `[intel]`? [ Yes / No ]
CALIBRATION [S2 of 5] PRE: Applicable at intelligence characterization? [ No — does not apply ]
FALSIFICATION [S2 of 5] PRE: Applicable before hypothesis declaration? [ No — does not apply ]
SEQUENCING [S2 of 5] PRE: Will this stage produce only evidence (no hypotheses)? [ Yes / No ]
PROVENANCE [S2 of 5] PRE: Applicable at a non-scope-restricted stage? [ No — not yet activated ]

---
-- STAGE EXECUTION OPEN -- Stage 2 --

Apply expert judgment to ARTIFACT-S1. Characterize: evidence patterns, contradictions,
strength ratings (well-evidenced / thin / contested), and knowledge gaps. Label every
new claim `[intel]`. Do not state hypotheses.

---
-- STAGE EXECUTION CLOSE / POST-EXECUTION VERIFICATION -- Stage 2 of 5 --

ATTRIBUTION [S2 of 5] POST: Are all new claims labeled `[intel]`? [ Yes / No ]
CALIBRATION [S2 of 5] POST: N/A confirmed? [ Yes ]
FALSIFICATION [S2 of 5] POST: N/A confirmed — no hypothesis declared? [ Yes ]
SEQUENCING [S2 of 5] POST: No hypothesis appears in Stage 2 output? [ Yes / No ]
PROVENANCE [S2 of 5] POST: N/A confirmed — Stage 2 is not scope-restricted? [ Yes ]

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Evidence landscape characterized: patterns, conflicts, gaps named | [ Pass / Fail ] |
| No hypothesis stated in Stage 2 output | [ Pass / Fail ] |
| All new claims carry `[intel]` label | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S2 to S3 (C-36):**

> **Role passes to: Stage 3 -- Hypothesis Architect.**
> Artifacts enumerated for transfer:
> - ARTIFACT-S1: Web Findings Corpus
> - ARTIFACT-S2: Intelligence Assessment
>
> Hypothesis Architect authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
>
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 3 (Hypothesis Architect) is scope-restricted.
> Provenance obligations activated for: ARTIFACT-S1, ARTIFACT-S2.
> Every claim produced by the Hypothesis Architect must carry
> `[source: Stage N -- Artifact Name]` where N ∈ {1, 2}.
> A claim with no provenance tag is a structural gap. A tag citing any other artifact
> is a charter violation detectable at the artifact-tag level.

---

### Stage 3 -- Hypothesis Architect

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S2 exit gate is all-Pass | [ Pass / Fail ] |
| Handoff block S2→S3 is complete and includes PROVENANCE RULE activation | [ Pass / Fail ] |
| PROVENANCE RULE activated for ARTIFACT-S1 and ARTIFACT-S2 at this boundary | [ Pass / Fail ] |

---
-- GOVERNANCE PRE-EXECUTION COMMITMENT -- Stage 3 of 5 --
Answer before writing any Stage 3 content:

ATTRIBUTION [S3 of 5] PRE: Will all claims be labeled `[hypothesis]`? [ Yes / No ]
CALIBRATION [S3 of 5] PRE: Applicable before analysis? [ No — does not apply ]
FALSIFICATION [S3 of 5] PRE: Will each hypothesis carry an explicit falsification condition? [ Yes / No ]
SEQUENCING [S3 of 5] PRE: Are S1 and S2 exits confirmed before this stage opens? [ Yes / No ]
PROVENANCE [S3 of 5] PRE: Will every claim carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2}? [ Yes / No ]

---
-- STAGE EXECUTION OPEN -- Stage 3 --

Declare 3-5 hypotheses about $ARGUMENTS. Each hypothesis must:
1. State a specific testable claim
2. Cite the evidence that prompted it: `[source: Stage 1 -- Web Findings Corpus]` or
   `[source: Stage 2 -- Intelligence Assessment]`
3. State a falsification condition: "This hypothesis is refuted if [criterion]"
4. Carry a preliminary confidence level (High / Medium / Low)

Label every claim `[hypothesis]`.

---
-- STAGE EXECUTION CLOSE / POST-EXECUTION VERIFICATION -- Stage 3 of 5 --

ATTRIBUTION [S3 of 5] POST: Are all claims labeled `[hypothesis]`? [ Yes / No ]
CALIBRATION [S3 of 5] POST: N/A confirmed? [ Yes ]
FALSIFICATION [S3 of 5] POST: Does every hypothesis carry an explicit falsification condition? [ Yes / No ]
SEQUENCING [S3 of 5] POST: All hypotheses grounded in S1+S2 evidence — no pre-evidence assumptions? [ Yes / No ]
PROVENANCE [S3 of 5] POST: Every claim carries `[source: Stage N -- Artifact Name]` where N ∈ {1,2}? [ Yes / No ]

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 3-5 hypotheses with explicit falsification conditions | [ Pass / Fail ] |
| All claims carry `[hypothesis]` label | [ Pass / Fail ] |
| All claims carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2} | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S3 to S4 (C-36):**

> **Role passes to: Stage 4 -- Evidence Analyst.**
> Artifacts enumerated for transfer:
> - ARTIFACT-S1: Web Findings Corpus
> - ARTIFACT-S2: Intelligence Assessment
> - ARTIFACT-S3: Hypothesis Register
>
> Evidence Analyst authorized reads: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.
>
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 4 (Evidence Analyst) is scope-restricted.
> Provenance obligations activated for: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3.
> Every claim produced by the Evidence Analyst must carry
> `[source: Stage N -- Artifact Name]` where N ∈ {1, 2, 3}.

---

### Stage 4 -- Evidence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S3 exit gate is all-Pass | [ Pass / Fail ] |
| Handoff block S3→S4 is complete and includes PROVENANCE RULE activation | [ Pass / Fail ] |
| PROVENANCE RULE activated for ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 | [ Pass / Fail ] |

---
-- GOVERNANCE PRE-EXECUTION COMMITMENT -- Stage 4 of 5 --
Answer before writing any Stage 4 content:

ATTRIBUTION [S4 of 5] PRE: Will all claims be labeled `[analysis]`? [ Yes / No ]
CALIBRATION [S4 of 5] PRE: Will at least two distinct confidence levels appear across findings? [ Yes / No ]
FALSIFICATION [S4 of 5] PRE: Applicable at analysis stage? [ No — falsification governs hypothesis declaration and synthesis ]
SEQUENCING [S4 of 5] PRE: Applicable here? [ No — evidence-before-hypothesis ordering is complete ]
PROVENANCE [S4 of 5] PRE: Will every claim carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3}? [ Yes / No ]

---
-- STAGE EXECUTION OPEN -- Stage 4 --

Analyze each hypothesis from ARTIFACT-S3 against evidence in ARTIFACT-S1 and ARTIFACT-S2.
For each hypothesis:
1. Summarize supporting evidence `[source: Stage N -- Artifact Name]`
2. Summarize counter-evidence or absences `[source: Stage N -- Artifact Name]`
3. Assign confidence (High / Medium / Low) — calibrate across hypotheses; uniform ratings fail
4. Note gaps or conflicts discovered

Label every claim `[analysis]`.

---
-- STAGE EXECUTION CLOSE / POST-EXECUTION VERIFICATION -- Stage 4 of 5 --

ATTRIBUTION [S4 of 5] POST: Are all claims labeled `[analysis]`? [ Yes / No ]
CALIBRATION [S4 of 5] POST: At least two distinct confidence levels present? [ Yes / No ]
FALSIFICATION [S4 of 5] POST: N/A confirmed? [ Yes ]
SEQUENCING [S4 of 5] POST: N/A confirmed — ordering constraint complete? [ Yes ]
PROVENANCE [S4 of 5] POST: Every claim carries `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3}? [ Yes / No ]

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| All hypotheses from S3 addressed | [ Pass / Fail ] |
| At least two distinct confidence levels used | [ Pass / Fail ] |
| All claims carry `[analysis]` and `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3} | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S4 to S5 (C-36):**

> **Role passes to: Stage 5 -- Synthesis Director.**
> Artifacts enumerated for transfer:
> - ARTIFACT-S1: Web Findings Corpus
> - ARTIFACT-S2: Intelligence Assessment
> - ARTIFACT-S3: Hypothesis Register
> - ARTIFACT-S4: Evidence Analysis
>
> Synthesis Director authorized reads: ARTIFACT-S1 through ARTIFACT-S4 only.
>
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 5 (Synthesis Director) is scope-restricted.
> Provenance obligations activated for: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4.
> Every claim produced by the Synthesis Director must carry
> `[source: Stage N -- Artifact Name]` where N ∈ {1, 2, 3, 4}.

---

### Stage 5 -- Synthesis Director

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S4 exit gate is all-Pass | [ Pass / Fail ] |
| Handoff block S4→S5 is complete and includes PROVENANCE RULE activation | [ Pass / Fail ] |
| PROVENANCE RULE activated for ARTIFACT-S1 through ARTIFACT-S4 | [ Pass / Fail ] |

---
-- GOVERNANCE PRE-EXECUTION COMMITMENT -- Stage 5 of 5 --
Answer before writing any Stage 5 content:

ATTRIBUTION [S5 of 5] PRE: Will all claims be labeled `[synthesis]`? [ Yes / No ]
CALIBRATION [S5 of 5] PRE: Will the confidence distribution be non-uniform and explicitly stated? [ Yes / No ]
FALSIFICATION [S5 of 5] PRE: Will each hypothesis receive a final status (Supported/Refuted/Indeterminate)? [ Yes / No ]
SEQUENCING [S5 of 5] PRE: Applicable at synthesis? [ No — ordering constraint complete ]
PROVENANCE [S5 of 5] PRE: Will every claim carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3,4}? [ Yes / No ]

---
-- STAGE EXECUTION OPEN -- Stage 5 --

Synthesize findings into a coherent evidence brief on $ARGUMENTS:

1. **Consensus findings**: where S1 and S2 agree — cite `[source: Stage N -- Artifact Name]`
2. **Conflicts**: where S1 and S2 diverge — name the conflict explicitly
3. **Hypothesis verdicts**: Supported / Refuted / Indeterminate for each hypothesis, with
   final falsification status declared
4. **Confidence distribution**: "X findings at High, Y at Medium, Z at Low" — non-uniform
5. **Gaps and open questions**: what remains under-evidenced after the full campaign
6. **Decision readiness**: one sentence naming posture and, if not ready, the specific gap

Label every claim `[synthesis]`. Every claim carries `[source: Stage N -- Artifact Name]`.

---
-- STAGE EXECUTION CLOSE / POST-EXECUTION VERIFICATION -- Stage 5 of 5 --

ATTRIBUTION [S5 of 5] POST: Are all claims labeled `[synthesis]`? [ Yes / No ]
CALIBRATION [S5 of 5] POST: Is the confidence distribution non-uniform and explicitly stated? [ Yes / No ]
FALSIFICATION [S5 of 5] POST: Does every hypothesis carry a final status? [ Yes / No ]
SEQUENCING [S5 of 5] POST: N/A confirmed — ordering constraint complete? [ Yes ]
PROVENANCE [S5 of 5] POST: Every claim carries `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3,4}? [ Yes / No ]

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Consensus and conflict explicitly separated | [ Pass / Fail ] |
| All hypotheses carry final status | [ Pass / Fail ] |
| Gaps section present | [ Pass / Fail ] |
| Decision readiness stated in one sentence | [ Pass / Fail ] |
| All claims carry `[synthesis]` and `[source: Stage N -- Artifact Name]` | [ Pass / Fail ] |

---

### OUTPUT ASSEMBLY

Assemble the final evidence brief:

1. **Brief header**: title, topic, date, stages run
2. **Filled gate record**: copy the gate record template above and fill all cells
3. **Stage outputs**: S1 through S5 in sequence
4. **Consolidated invocation audit table**: 40 rows (15 positive cells × 2 phases + 10 negative cells × 1)
   Columns: Rule | Stage | Phase (PRE/POST/N/A) | Answer | Pass/Fail
5. **Synthesis narrative**: consensus findings, conflicts, hypothesis verdicts, confidence distribution
6. **Gaps and open questions**
7. **Decision readiness** (one sentence)

**Delivery gate:** Confirm audit table row count = 40 before closing. Count ≠ 40 is a
delivery blocker.

---

---

## V-02 -- Axis: Output Format (Separate PRE and POST Invocation Tables at Each Stage)

**Variation axis:** Every governance invocation is a row in one of two named tables at each
stage: a **PRE-EXECUTION COMMITMENT TABLE** (filled before writing any stage content) and a
**POST-EXECUTION VERIFICATION TABLE** (filled after stage content closes). The two tables are
the only invocation artifacts — there are no inline invocation tags in the stage narrative.
Evidence claims are rows in a stage-indexed master table with columns for Stage, Attribution
Label, Provenance Tag (if scope-restricted), and Confidence. Sequencing compliance is
machine-verifiable by sorting the Stage column: a hypothesis row with Stage = S1 or S2 is a
data error, not a prose-interpretation dispute.

**Hypothesis:** Separating pre and post invocations into two distinct tables — each requiring
a column to be filled at a specific time — makes the temporal gap a structural property of
the form, not an instruction. The pre-table cannot be post-filled without visible anachronism
(it precedes the execution block in the document); the post-table cannot be pre-filled because
the execution block has not yet closed. An executor who fills both tables simultaneously
produces a document that is structurally inconsistent — the execution block falls between two
filled tables, making simultaneous filling visually legible as a violation.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable.

---

#### Rule Registry

| Rule | Declaration | Scope (Applicable Stages) | Anti-Pattern |
|------|-------------|--------------------------|--------------|
| ATTRIBUTION | Every material claim names its source stage | S1(+), S2(+), S3(+), S4(+), S5(+) | Unlabeled material claim |
| CALIBRATION | Confidence ratings vary across findings | S4(+), S5(+) | All findings same confidence level |
| FALSIFICATION | Each hypothesis has explicit falsification condition | S3(+), S5(+) | Hypothesis without falsification condition |
| SEQUENCING | S1+S2 evidence complete before S3 hypothesis declaration | S1(+), S2(+), S3(+) | Hypothesis stated before S1/S2 exit |
| PROVENANCE | Scope-restricted stages carry per-claim source artifact tags | S3(+), S4(+), S5(+) | Claim missing `[source: Stage N -- Artifact Name]` in S3/S4/S5 |

Peer declaration: five equal-tier rules. New rule = automatic propagation through coverage
map and checksum. No static integers.

---

#### Role Roster

| Stage | Role | Authorized Reads | Scope-Restricted? |
|-------|------|-----------------|:-----------------:|
| S1 | Web Evidence Collector | External sources only | No |
| S2 | Intelligence Analyst | ARTIFACT-S1 only | No |
| S3 | Hypothesis Architect | ARTIFACT-S1, ARTIFACT-S2 only | **Yes** |
| S4 | Evidence Analyst | ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 only | **Yes** |
| S5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 only | **Yes** |

---

#### Coverage Map (immutable — sealed before Stage 1)

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|----|:---:|:---:|
| ATTRIBUTION  | + | + | + | + | + | 5 | 0 |
| CALIBRATION  | - | - | - | + | + | 2 | 3 |
| FALSIFICATION| - | - | + | - | + | 2 | 3 |
| SEQUENCING   | + | + | + | - | - | 3 | 2 |
| PROVENANCE   | - | - | + | + | + | 3 | 2 |

Checksum: **(15 positive × 2 phases) + (10 negative × 1) = 40 invocation artifacts.**
Derived from map dimensions. No static integer stores this independently.

---

#### Gate Record Template

| Stage | Role | Entry Status | Exit Status |
|-------|------|:---:|:---:|
| S1 | Web Evidence Collector | Pass | [ ] |
| S2 | Intelligence Analyst | [ ] | [ ] |
| S3 | Hypothesis Architect | [ ] | [ ] |
| S4 | Evidence Analyst | [ ] | [ ] |
| S5 | Synthesis Director | [ ] | [ ] |

---

#### Master Evidence Table (rows added as stages execute)

| Row ID | Stage | Role | Label | Content (summary) | Source Artifact | Confidence |
|--------|-------|------|-------|-------------------|----------------|:---:|
| — | — | — | — | *(filled during execution)* | — | — |

Stage column values: S1, S2, S3, S4, S5. SEQUENCING compliance: hypothesis rows (Stage=S3)
may reference only source rows where Stage ∈ {S1, S2}. Provenance = foreign-key reference
into this table. Sort Stage column to verify sequencing; any H-row citing S3 is a violation.

---

### STAGE EXECUTION

---

### Stage 1 -- Web Evidence Collector

**Entry gate:**

| Condition | Status |
|-----------|--------|
| First stage — no prior stages | Pass |
| No hypothesis stated anywhere | Pass |

---

#### PRE-EXECUTION COMMITMENT TABLE — Stage 1

*Fill before writing any Stage 1 content. Pre-answer is on record before execution opens.*

| Rule | [S1 of 5] Pre-check: Will this hold? | Committed Answer |
|------|--------------------------------------|:---:|
| ATTRIBUTION | Will all findings be labeled `[web]`? | [ Yes / No ] |
| CALIBRATION | Applicable at evidence collection? | [ No — N/A ] |
| FALSIFICATION | Applicable before hypothesis declaration? | [ No — N/A ] |
| SEQUENCING | Will this stage produce only evidence (no hypotheses)? | [ Yes / No ] |
| PROVENANCE | Applicable at non-scope-restricted stage? | [ No — N/A ] |

---

*[Execute Stage 1 — Web Evidence Collector]*

Conduct structured web research on $ARGUMENTS. Search for primary sources, technical data,
industry reports, quantitative evidence, expert commentary. Label every finding `[web]`.
Add each finding as a row in the Master Evidence Table (Stage=S1). Do not state hypotheses.

---

#### POST-EXECUTION VERIFICATION TABLE — Stage 1

*Fill after Stage 1 content above is complete. Post-answer reflects actual output.*

| Rule | [S1 of 5] Post-check: Did this hold? | Verified Answer |
|------|--------------------------------------|:---:|
| ATTRIBUTION | Are all findings labeled `[web]`? | [ Yes / No ] |
| CALIBRATION | N/A confirmed — no confidence ratings at S1? | [ Yes ] |
| FALSIFICATION | N/A confirmed — no hypothesis declared? | [ Yes ] |
| SEQUENCING | No hypothesis appears in Stage 1 output? | [ Yes / No ] |
| PROVENANCE | N/A confirmed — Stage 1 not scope-restricted? | [ Yes ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 6+ rows in Master Evidence Table with Stage=S1, all labeled `[web]` | [ Pass / Fail ] |
| No hypothesis row (Stage=S3) in Master Evidence Table | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S1 to S2 (C-36):**

> **Role passes to: Stage 2 -- Intelligence Analyst.**
> Artifacts enumerated for transfer:
> - ARTIFACT-S1: Web Findings Corpus (all Stage=S1 rows in Master Evidence Table)
>
> Intelligence Analyst authorized reads: ARTIFACT-S1 only.
>
> **PROVENANCE RULE status:** NOT activated at this boundary.
> Stage 2 is not scope-restricted. Per-claim source tagging not required.
> PROVENANCE RULE will be evaluated and activated or declined at each subsequent handoff.

---

### Stage 2 -- Intelligence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S1 exit all-Pass | [ Pass / Fail ] |
| Handoff S1→S2 complete with provenance status declared | [ Pass / Fail ] |

---

#### PRE-EXECUTION COMMITMENT TABLE — Stage 2

| Rule | [S2 of 5] Pre-check | Committed Answer |
|------|---------------------|:---:|
| ATTRIBUTION | Will all new claims be labeled `[intel]`? | [ Yes / No ] |
| CALIBRATION | Applicable at intelligence characterization? | [ No — N/A ] |
| FALSIFICATION | Applicable before hypothesis declaration? | [ No — N/A ] |
| SEQUENCING | Will this stage produce only evidence (no hypotheses)? | [ Yes / No ] |
| PROVENANCE | Applicable at non-scope-restricted stage? | [ No — N/A ] |

---

*[Execute Stage 2 — Intelligence Analyst]*

Apply expert judgment to ARTIFACT-S1 rows. For each pattern, gap, or contradiction observed:
add a row to the Master Evidence Table (Stage=S2, Label=`[intel]`). Characterize evidence
strength (well-evidenced / thin / contested). Do not state hypotheses.

---

#### POST-EXECUTION VERIFICATION TABLE — Stage 2

| Rule | [S2 of 5] Post-check | Verified Answer |
|------|---------------------|:---:|
| ATTRIBUTION | All new claims labeled `[intel]`? | [ Yes / No ] |
| CALIBRATION | N/A confirmed? | [ Yes ] |
| FALSIFICATION | N/A confirmed — no hypothesis declared? | [ Yes ] |
| SEQUENCING | No hypothesis row appears in Stage 2 output? | [ Yes / No ] |
| PROVENANCE | N/A confirmed — Stage 2 not scope-restricted? | [ Yes ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Evidence landscape characterized; patterns, conflicts, gaps named | [ Pass / Fail ] |
| No Stage=S3 row in Master Evidence Table | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S2 to S3 (C-36):**

> **Role passes to: Stage 3 -- Hypothesis Architect.**
> Artifacts enumerated for transfer:
> - ARTIFACT-S1: Web Findings Corpus (Stage=S1 rows)
> - ARTIFACT-S2: Intelligence Assessment (Stage=S2 rows)
>
> Hypothesis Architect authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
>
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 3 is scope-restricted. Provenance obligations activated for: ARTIFACT-S1, ARTIFACT-S2.
> Every Stage=S3 row in the Master Evidence Table must carry a Source Artifact value
> referencing only Stage=S1 or Stage=S2 rows. A missing Source Artifact is a structural gap.
> A Source Artifact referencing Stage=S3, S4, or S5 is a charter violation.

---

### Stage 3 -- Hypothesis Architect

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S2 exit all-Pass | [ Pass / Fail ] |
| Handoff S2→S3 complete with PROVENANCE RULE activated for ARTIFACT-S1, ARTIFACT-S2 | [ Pass / Fail ] |

---

#### PRE-EXECUTION COMMITMENT TABLE — Stage 3

| Rule | [S3 of 5] Pre-check | Committed Answer |
|------|---------------------|:---:|
| ATTRIBUTION | Will all hypothesis rows carry `[hypothesis]` label? | [ Yes / No ] |
| CALIBRATION | Applicable before analysis? | [ No — N/A ] |
| FALSIFICATION | Will each hypothesis carry explicit falsification condition? | [ Yes / No ] |
| SEQUENCING | Are S1 and S2 exits confirmed — no hypotheses exist in Master Table yet? | [ Yes / No ] |
| PROVENANCE | Will every Stage=S3 row carry Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2}? | [ Yes / No ] |

---

*[Execute Stage 3 — Hypothesis Architect]*

Declare 3-5 hypotheses about $ARGUMENTS. Add each as a row in the Master Evidence Table
(Stage=S3, Label=`[hypothesis]`). Each row must include:
- Content: hypothesis claim
- Source Artifact: ARTIFACT-S1 or ARTIFACT-S2 (the evidence that prompted the hypothesis)
- Falsification Condition: "Refuted if [criterion]" (include in Content field)
- Confidence: High / Medium / Low

---

#### POST-EXECUTION VERIFICATION TABLE — Stage 3

| Rule | [S3 of 5] Post-check | Verified Answer |
|------|---------------------|:---:|
| ATTRIBUTION | All hypothesis rows carry `[hypothesis]` label? | [ Yes / No ] |
| CALIBRATION | N/A confirmed? | [ Yes ] |
| FALSIFICATION | Every hypothesis row carries explicit falsification condition? | [ Yes / No ] |
| SEQUENCING | All Stage=S3 rows cite Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2}? | [ Yes / No ] |
| PROVENANCE | Every Stage=S3 row has non-empty Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2}? | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 3-5 Stage=S3 rows with falsification conditions in Master Evidence Table | [ Pass / Fail ] |
| All Stage=S3 rows carry Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2} | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S3 to S4 (C-36):**

> **Role passes to: Stage 4 -- Evidence Analyst.**
> Artifacts enumerated for transfer:
> - ARTIFACT-S1: Web Findings Corpus
> - ARTIFACT-S2: Intelligence Assessment
> - ARTIFACT-S3: Hypothesis Register (Stage=S3 rows)
>
> Evidence Analyst authorized reads: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.
>
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 4 is scope-restricted. Provenance obligations activated for:
> ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3.
> Every Stage=S4 row must carry Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3}.

---

### Stage 4 -- Evidence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S3 exit all-Pass | [ Pass / Fail ] |
| Handoff S3→S4 complete with PROVENANCE RULE activated | [ Pass / Fail ] |

---

#### PRE-EXECUTION COMMITMENT TABLE — Stage 4

| Rule | [S4 of 5] Pre-check | Committed Answer |
|------|---------------------|:---:|
| ATTRIBUTION | Will all analysis rows carry `[analysis]` label? | [ Yes / No ] |
| CALIBRATION | Will at least two distinct Confidence values appear across Stage=S4 rows? | [ Yes / No ] |
| FALSIFICATION | Applicable at analysis stage? | [ No — N/A; governs S3 and S5 ] |
| SEQUENCING | Applicable here? | [ No — N/A; ordering constraint complete ] |
| PROVENANCE | Will every Stage=S4 row carry Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3}? | [ Yes / No ] |

---

*[Execute Stage 4 — Evidence Analyst]*

For each hypothesis row (Stage=S3) in ARTIFACT-S3:
- Add supporting-evidence rows to Master Evidence Table (Stage=S4, Label=`[analysis]`,
  Source Artifact=ARTIFACT-S1 or ARTIFACT-S2)
- Add counter-evidence rows (Stage=S4, Source Artifact named)
- Add a summary row (Stage=S4) with Confidence: High / Medium / Low — calibrate across
  hypotheses; uniform ratings fail CALIBRATION

---

#### POST-EXECUTION VERIFICATION TABLE — Stage 4

| Rule | [S4 of 5] Post-check | Verified Answer |
|------|---------------------|:---:|
| ATTRIBUTION | All Stage=S4 rows carry `[analysis]` label? | [ Yes / No ] |
| CALIBRATION | At least two distinct Confidence values among Stage=S4 rows? | [ Yes / No ] |
| FALSIFICATION | N/A confirmed? | [ Yes ] |
| SEQUENCING | N/A confirmed? | [ Yes ] |
| PROVENANCE | All Stage=S4 rows carry Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3}? | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| All S3 hypotheses addressed in Stage=S4 rows | [ Pass / Fail ] |
| At least two distinct confidence levels in Stage=S4 rows | [ Pass / Fail ] |

**HANDOFF DECLARATION -- S4 to S5 (C-36):**

> **Role passes to: Stage 5 -- Synthesis Director.**
> Artifacts enumerated for transfer:
> - ARTIFACT-S1: Web Findings Corpus
> - ARTIFACT-S2: Intelligence Assessment
> - ARTIFACT-S3: Hypothesis Register
> - ARTIFACT-S4: Evidence Analysis (Stage=S4 rows)
>
> Synthesis Director authorized reads: ARTIFACT-S1 through ARTIFACT-S4 only.
>
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 5 is scope-restricted. Provenance obligations activated for:
> ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4.
> Every Stage=S5 row must carry Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4}.

---

### Stage 5 -- Synthesis Director

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S4 exit all-Pass | [ Pass / Fail ] |
| Handoff S4→S5 complete with PROVENANCE RULE activated | [ Pass / Fail ] |

---

#### PRE-EXECUTION COMMITMENT TABLE — Stage 5

| Rule | [S5 of 5] Pre-check | Committed Answer |
|------|---------------------|:---:|
| ATTRIBUTION | Will all synthesis rows carry `[synthesis]` label? | [ Yes / No ] |
| CALIBRATION | Will confidence distribution be non-uniform and explicitly stated? | [ Yes / No ] |
| FALSIFICATION | Will each hypothesis receive a final status row (Supported/Refuted/Indeterminate)? | [ Yes / No ] |
| SEQUENCING | Applicable at synthesis? | [ No — N/A ] |
| PROVENANCE | Will every Stage=S5 row carry Source Artifact ∈ {ARTIFACT-S1..ARTIFACT-S4}? | [ Yes / No ] |

---

*[Execute Stage 5 — Synthesis Director]*

Add synthesis rows to Master Evidence Table (Stage=S5, Label=`[synthesis]`):
- Consensus rows: findings where S1 and S2 agree, Source Artifact named
- Conflict rows: findings where S1 and S2 diverge, both artifacts cited
- Verdict rows: final status per hypothesis (Supported/Refuted/Indeterminate), with
  falsification status declared, Source Artifact=ARTIFACT-S3+ARTIFACT-S4
- Gap rows: what remains under-evidenced
- One decision-readiness row: posture sentence

---

#### POST-EXECUTION VERIFICATION TABLE — Stage 5

| Rule | [S5 of 5] Post-check | Verified Answer |
|------|---------------------|:---:|
| ATTRIBUTION | All Stage=S5 rows carry `[synthesis]` label? | [ Yes / No ] |
| CALIBRATION | Confidence distribution non-uniform and explicitly stated in Master Table? | [ Yes / No ] |
| FALSIFICATION | Every hypothesis has a Verdict row with final status? | [ Yes / No ] |
| SEQUENCING | N/A confirmed? | [ Yes ] |
| PROVENANCE | All Stage=S5 rows carry Source Artifact ∈ {ARTIFACT-S1..ARTIFACT-S4}? | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Consensus and conflict rows both present | [ Pass / Fail ] |
| All hypothesis verdict rows present with final status | [ Pass / Fail ] |
| Gap rows present | [ Pass / Fail ] |
| Decision-readiness row present (one sentence) | [ Pass / Fail ] |

---

### OUTPUT ASSEMBLY

Assemble in order:
1. **Brief header**
2. **Filled gate record** (copy template above, fill all cells)
3. **Master Evidence Table** (complete, all stages, sorted by Stage then Row ID)
4. **Consolidated invocation audit table** (40 rows: 30 PRE/POST pairs + 10 N/A; columns: Rule | Stage | Phase | Answer | Pass/Fail)
5. **Synthesis narrative** assembled from Stage=S5 rows
6. **Decision readiness sentence** (from the single decision-readiness row)

**Delivery gate:** Confirm Master Evidence Table has Stage=S1 rows (≥6) and Stage=S5 rows
(≥1 decision-readiness). Confirm audit table = 40 rows. Count ≠ 40 is a delivery blocker.

---

---

## V-03 -- Axis: Lifecycle Emphasis (All Stage Templates Pre-Declared in Preamble as Blank Forms)

**Variation axis:** Every invocation table for every stage — both PRE and POST — is
pre-declared in the preamble as a blank form with empty answer cells. Stage bodies contain
only the execution instruction; they reference back to the preamble's pre-declared tables
rather than redeclaring governance inline. This converts compliance from creative recall
(remembering to add governance at each stage) into mechanical form-filling (cells exist
in the preamble before execution begins; unfilled cells are visible at any point during
execution). The preamble dominates the document length; stage bodies are minimal.

**Hypothesis:** Pre-declaring all 10 invocation tables (2 phases × 5 stages) in the preamble
makes missing invocations structurally visible before any stage executes. An executor who
skips a pre-check produces a blank cell in a table that already exists in the preamble — the
gap is visible before the affected stage's output appears. The pre-commitment form is a
standing record that the post-execution check cannot retroactively erase; answering both
phases simultaneously would require filling a preamble cell before the stage exists and a
stage-close cell before the stage opens.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

All governance artifacts are pre-declared below as blank forms. Fill each cell at the
prescribed moment. Blank cells in final output indicate compliance gaps. This preamble
is immutable — it cannot be modified after Stage 1 begins.

---

#### Rule Registry

**ATTRIBUTION RULE** `[S1(+), S2(+), S3(+), S4(+), S5(+) — both PRE and POST phases]`
Every material claim names its source stage. Labels: `[web]`, `[intel]`, `[hypothesis]`,
`[analysis]`, `[synthesis]`. Unlabeled material claim = attribution failure.

**CALIBRATION RULE** `[S4(+), S5(+) both phases; S1(-), S2(-), S3(-) negative]`
Confidence ratings vary. Uniform ratings fail. Anti-uniformity guard active at S4 and S5.
State distribution: "X High, Y Medium, Z Low."

**FALSIFICATION RULE** `[S3(+), S5(+) both phases; S1(-), S2(-), S4(-) negative]`
Each hypothesis has explicit falsification condition. Final status: Supported / Refuted /
Indeterminate.

**SEQUENCING RULE** `[S1(+), S2(+), S3(+) both phases; S4(-), S5(-) negative]`
Evidence (S1, S2) before hypothesis (S3). "A hypothesis anchored before evidence is a bias,
not a hypothesis."

**PROVENANCE RULE** `[S3(+), S4(+), S5(+) both phases; S1(-), S2(-) negative]`
Activated at handoff boundary preceding each scope-restricted stage. Per-claim source tags
`[source: Stage N -- Artifact Name]` in S3, S4, S5.

Peer declaration: five equal-tier rules. New rule propagates automatically.

---

#### Role Roster

| Stage | Role | Authorized Reads | Scope-Restricted |
|-------|------|-----------------|:---:|
| S1 | Web Evidence Collector | External sources only | No |
| S2 | Intelligence Analyst | ARTIFACT-S1 only | No |
| S3 | Hypothesis Architect | ARTIFACT-S1, ARTIFACT-S2 | **Yes** |
| S4 | Evidence Analyst | ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 | **Yes** |
| S5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 | **Yes** |

---

#### Coverage Map (sealed — cannot be modified after Stage 1 begins)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION  | + | + | + | + | + |
| CALIBRATION  | - | - | - | + | + |
| FALSIFICATION| - | - | + | - | + |
| SEQUENCING   | + | + | + | - | - |
| PROVENANCE   | - | - | + | + | + |

Checksum: (15 × 2) + (10 × 1) = **40 invocation artifacts**. Derived; not stored independently.

---

#### Gate Record (pre-declared — fill cells as stages complete)

| Stage | Role | Entry | Exit |
|-------|------|:---:|:---:|
| S1 | Web Evidence Collector | Pass | [ ] |
| S2 | Intelligence Analyst | [ ] | [ ] |
| S3 | Hypothesis Architect | [ ] | [ ] |
| S4 | Evidence Analyst | [ ] | [ ] |
| S5 | Synthesis Director | [ ] | [ ] |

---

#### PRE-EXECUTION COMMITMENT FORMS (pre-declared — fill each before its stage opens)

**Form PRE-S1** *(fill before writing any Stage 1 content)*

| Rule | [S1 of 5] Pre-commitment | Answer |
|------|--------------------------|:---:|
| ATTRIBUTION | Will all findings carry `[web]` label? | [ ] |
| CALIBRATION | Applicable? | [ No — N/A ] |
| FALSIFICATION | Applicable? | [ No — N/A ] |
| SEQUENCING | Will Stage 1 produce only evidence (no hypotheses)? | [ ] |
| PROVENANCE | Applicable? | [ No — N/A ] |

**Form PRE-S2** *(fill before writing any Stage 2 content)*

| Rule | [S2 of 5] Pre-commitment | Answer |
|------|--------------------------|:---:|
| ATTRIBUTION | Will all new claims carry `[intel]` label? | [ ] |
| CALIBRATION | Applicable? | [ No — N/A ] |
| FALSIFICATION | Applicable? | [ No — N/A ] |
| SEQUENCING | Will Stage 2 produce only evidence (no hypotheses)? | [ ] |
| PROVENANCE | Applicable? | [ No — N/A ] |

**Form PRE-S3** *(fill before writing any Stage 3 content)*

| Rule | [S3 of 5] Pre-commitment | Answer |
|------|--------------------------|:---:|
| ATTRIBUTION | Will all claims carry `[hypothesis]` label? | [ ] |
| CALIBRATION | Applicable? | [ No — N/A ] |
| FALSIFICATION | Will each hypothesis carry explicit falsification condition? | [ ] |
| SEQUENCING | Are S1 and S2 exits confirmed before this form is filled? | [ ] |
| PROVENANCE | Will all claims carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2}? | [ ] |

**Form PRE-S4** *(fill before writing any Stage 4 content)*

| Rule | [S4 of 5] Pre-commitment | Answer |
|------|--------------------------|:---:|
| ATTRIBUTION | Will all claims carry `[analysis]` label? | [ ] |
| CALIBRATION | Will ≥2 distinct confidence levels appear? | [ ] |
| FALSIFICATION | Applicable? | [ No — N/A; governs S3 and S5 ] |
| SEQUENCING | Applicable? | [ No — N/A; ordering constraint complete ] |
| PROVENANCE | Will all claims carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3}? | [ ] |

**Form PRE-S5** *(fill before writing any Stage 5 content)*

| Rule | [S5 of 5] Pre-commitment | Answer |
|------|--------------------------|:---:|
| ATTRIBUTION | Will all claims carry `[synthesis]` label? | [ ] |
| CALIBRATION | Will confidence distribution be non-uniform and explicitly stated? | [ ] |
| FALSIFICATION | Will each hypothesis receive a final status declaration? | [ ] |
| SEQUENCING | Applicable? | [ No — N/A ] |
| PROVENANCE | Will all claims carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3,4}? | [ ] |

---

#### POST-EXECUTION VERIFICATION FORMS (pre-declared — fill each after its stage closes)

**Form POST-S1** *(fill after Stage 1 content is complete)*

| Rule | [S1 of 5] Post-verification | Answer |
|------|----------------------------|:---:|
| ATTRIBUTION | All findings carry `[web]` label? | [ ] |
| CALIBRATION | N/A confirmed — no confidence ratings at S1? | [ Yes ] |
| FALSIFICATION | N/A confirmed — no hypothesis declared? | [ Yes ] |
| SEQUENCING | No hypothesis appears in Stage 1 output? | [ ] |
| PROVENANCE | N/A confirmed — Stage 1 not scope-restricted? | [ Yes ] |

**Form POST-S2** *(fill after Stage 2 content is complete)*

| Rule | [S2 of 5] Post-verification | Answer |
|------|----------------------------|:---:|
| ATTRIBUTION | All new claims carry `[intel]` label? | [ ] |
| CALIBRATION | N/A confirmed? | [ Yes ] |
| FALSIFICATION | N/A confirmed — no hypothesis declared? | [ Yes ] |
| SEQUENCING | No hypothesis appears in Stage 2 output? | [ ] |
| PROVENANCE | N/A confirmed — Stage 2 not scope-restricted? | [ Yes ] |

**Form POST-S3** *(fill after Stage 3 content is complete)*

| Rule | [S3 of 5] Post-verification | Answer |
|------|----------------------------|:---:|
| ATTRIBUTION | All claims carry `[hypothesis]` label? | [ ] |
| CALIBRATION | N/A confirmed? | [ Yes ] |
| FALSIFICATION | Every hypothesis carries explicit falsification condition? | [ ] |
| SEQUENCING | All hypotheses grounded in S1+S2 evidence — no pre-evidence assumptions? | [ ] |
| PROVENANCE | All claims carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2}? | [ ] |

**Form POST-S4** *(fill after Stage 4 content is complete)*

| Rule | [S4 of 5] Post-verification | Answer |
|------|----------------------------|:---:|
| ATTRIBUTION | All claims carry `[analysis]` label? | [ ] |
| CALIBRATION | ≥2 distinct confidence levels present? | [ ] |
| FALSIFICATION | N/A confirmed? | [ Yes ] |
| SEQUENCING | N/A confirmed? | [ Yes ] |
| PROVENANCE | All claims carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3}? | [ ] |

**Form POST-S5** *(fill after Stage 5 content is complete)*

| Rule | [S5 of 5] Post-verification | Answer |
|------|----------------------------|:---:|
| ATTRIBUTION | All claims carry `[synthesis]` label? | [ ] |
| CALIBRATION | Confidence distribution non-uniform and explicitly stated? | [ ] |
| FALSIFICATION | Every hypothesis carries final status (Supported/Refuted/Indeterminate)? | [ ] |
| SEQUENCING | N/A confirmed? | [ Yes ] |
| PROVENANCE | All claims carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3,4}? | [ ] |

---

*End of preamble. All forms above are pre-declared and awaiting execution. Stage bodies follow.*

---

### STAGE EXECUTION

---

### Stage 1 -- Web Evidence Collector

→ Fill **Form PRE-S1** in preamble above before writing below this line.

Conduct structured web research on $ARGUMENTS. Search for primary sources, technical data,
industry reports, quantitative evidence, expert commentary. Label every finding `[web]`.
Minimum 6 findings. Do not state hypotheses.

*[Web Evidence Collector output here]*

**Exit gate:** 6+ `[web]` findings present. No hypothesis stated. → Update Gate Record S1 Exit.

→ Fill **Form POST-S1** in preamble above after completing output above.

**HANDOFF DECLARATION -- S1 to S2 (C-36):**
> **Role passes to: Stage 2 -- Intelligence Analyst.**
> Artifacts transferred: ARTIFACT-S1 (Web Findings Corpus).
> Authorized reads for Intelligence Analyst: ARTIFACT-S1 only.
> **PROVENANCE RULE status:** NOT activated. Stage 2 not scope-restricted.

→ Update Gate Record S2 Entry in preamble above.

---

### Stage 2 -- Intelligence Analyst

→ Fill **Form PRE-S2** in preamble above before writing below this line.

Apply expert judgment to ARTIFACT-S1. Characterize patterns, contradictions, evidence
strength (well-evidenced / thin / contested), and knowledge gaps. Label every new claim
`[intel]`. Do not state hypotheses.

*[Intelligence Analyst output here]*

**Exit gate:** Evidence landscape characterized. No hypothesis stated. All claims `[intel]`.
→ Update Gate Record S2 Exit.

→ Fill **Form POST-S2** in preamble above after completing output above.

**HANDOFF DECLARATION -- S2 to S3 (C-36):**
> **Role passes to: Stage 3 -- Hypothesis Architect.**
> Artifacts transferred: ARTIFACT-S1 (Web Findings Corpus), ARTIFACT-S2 (Intelligence Assessment).
> Authorized reads for Hypothesis Architect: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 3 is scope-restricted. Provenance obligations activated for: ARTIFACT-S1, ARTIFACT-S2.
> Every claim in Stage 3 must carry `[source: Stage N -- Artifact Name]` where N ∈ {1, 2}.

→ Update Gate Record S3 Entry in preamble above.

---

### Stage 3 -- Hypothesis Architect

→ Fill **Form PRE-S3** in preamble above before writing below this line.

Declare 3-5 hypotheses about $ARGUMENTS grounded in ARTIFACT-S1 and ARTIFACT-S2. Each
hypothesis: (1) testable claim, (2) `[source: Stage N -- Artifact Name]` where N ∈ {1,2},
(3) falsification condition ("Refuted if [criterion]"), (4) confidence (High/Medium/Low).
Label every claim `[hypothesis]`.

*[Hypothesis Architect output here]*

**Exit gate:** 3-5 hypotheses with falsification conditions. All claims `[hypothesis]` and
`[source: Stage N -- Artifact Name]`. → Update Gate Record S3 Exit.

→ Fill **Form POST-S3** in preamble above after completing output above.

**HANDOFF DECLARATION -- S3 to S4 (C-36):**
> **Role passes to: Stage 4 -- Evidence Analyst.**
> Artifacts transferred: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 (Hypothesis Register).
> Authorized reads: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 4 is scope-restricted. Provenance obligations activated for: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3.
> Every claim in Stage 4 must carry `[source: Stage N -- Artifact Name]` where N ∈ {1, 2, 3}.

→ Update Gate Record S4 Entry in preamble above.

---

### Stage 4 -- Evidence Analyst

→ Fill **Form PRE-S4** in preamble above before writing below this line.

Analyze each hypothesis from ARTIFACT-S3 against ARTIFACT-S1 and ARTIFACT-S2. For each:
supporting evidence (cite source artifact), counter-evidence (cite source artifact),
confidence (High/Medium/Low — calibrate; uniform ratings fail CALIBRATION), new gaps.
Label every claim `[analysis]`.

*[Evidence Analyst output here]*

**Exit gate:** All hypotheses addressed. ≥2 distinct confidence levels. All claims `[analysis]`
and `[source: Stage N -- Artifact Name]`. → Update Gate Record S4 Exit.

→ Fill **Form POST-S4** in preamble above after completing output above.

**HANDOFF DECLARATION -- S4 to S5 (C-36):**
> **Role passes to: Stage 5 -- Synthesis Director.**
> Artifacts transferred: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4 (Evidence Analysis).
> Authorized reads: ARTIFACT-S1 through ARTIFACT-S4 only.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 5 is scope-restricted. Provenance obligations activated for: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4.
> Every claim in Stage 5 must carry `[source: Stage N -- Artifact Name]` where N ∈ {1, 2, 3, 4}.

→ Update Gate Record S5 Entry in preamble above.

---

### Stage 5 -- Synthesis Director

→ Fill **Form PRE-S5** in preamble above before writing below this line.

Synthesize findings on $ARGUMENTS into a coherent evidence brief:
1. Consensus findings (where S1 and S2 agree) — cite source artifact
2. Conflicts (where S1 and S2 diverge) — name the conflict explicitly
3. Hypothesis verdicts: final status (Supported/Refuted/Indeterminate) per hypothesis
4. Confidence distribution statement (non-uniform required)
5. Gaps and open questions
6. Decision readiness (one sentence: posture + specific gap if not ready)

Label every claim `[synthesis]`. Every claim carries `[source: Stage N -- Artifact Name]`.

*[Synthesis Director output here]*

**Exit gate:** All sections present. Confidence distribution non-uniform and stated.
Decision readiness is one sentence. → Update Gate Record S5 Exit.

→ Fill **Form POST-S5** in preamble above after completing output above.

---

### OUTPUT ASSEMBLY

Final brief = preamble (all forms filled) + stage outputs (S1–S5) + consolidated audit table.

**Consolidated invocation audit table** (assembled from preamble forms):

| Rule | Stage | Phase | Answer | Pass/Fail |
|------|-------|-------|--------|:---------:|
| *[40 rows: copy each row from PRE and POST forms above, column by column]* | | | | |

**Delivery gate:** Count rows in audit table = 40. Count ≠ 40 is a delivery blocker.
**Decision readiness** (one sentence from Stage 5): *[copy here]*

---

---

## V-04 -- Axes: Role Sequence + Phrasing Register (Imperative Second-Person, Obligation-First)

**Variation axes:**
1. **Role Sequence:** Hypothesis declaration (Stage 3) is explicitly commanded to occur after
   Stages 1 and 2, and the SEQUENCING RULE is phrased as a direct obligation on the executor.
2. **Phrasing Register:** The entire prompt uses imperative second-person address — "You are
   the Web Evidence Collector. You must..." — rather than declarative descriptions. Pre-execution
   commitments are framed as personal obligations the executor assumes before acting; post-execution
   verifications are framed as questions the executor must answer truthfully about their own output.

**Hypothesis:** Imperative framing with role-persona assignment ("You are X") activates a
different compliance posture than declarative governance tables: an executor addressed
directly as a named role with personal obligations is less likely to treat governance as
an administrative form to fill in retrospectively. The pre-execution commitment framed as
"You commit, before writing, to the following:" creates a personal record — answering "Yes"
is a public declaration, not a checkbox.

---

You are running the full evidence campaign for: **$ARGUMENTS**

---

### GOVERNANCE FRAMEWORK

Before you execute any stage, read and accept the following five obligations. They govern
your conduct at every stage of this campaign. All five are your obligations equally — none
outranks another.

**You must attribute.** Every material claim you write names the stage that produced it.
Use `[web]` for Stage 1 findings, `[intel]` for Stage 2, `[hypothesis]` for Stage 3,
`[analysis]` for Stage 4, `[synthesis]` for Stage 5. You apply this at every stage.
`[ATTRIBUTION: S1(+), S2(+), S3(+), S4(+), S5(+)]`

**You must calibrate.** When you assign confidence ratings, you must vary them. If you
finish Stage 4 or Stage 5 and every finding carries the same confidence level, you have
failed calibration — go back and recalibrate before proceeding. You must explicitly state
the distribution: "X High, Y Medium, Z Low."
`[CALIBRATION: S4(+), S5(+)]`

**You must falsify.** Every hypothesis you declare carries a falsification condition —
a stated criterion that, if observed, causes you to refute the hypothesis. You finalize
each hypothesis's status (Supported / Refuted / Indeterminate) at synthesis.
`[FALSIFICATION: S3(+), S5(+)]`

**You must sequence.** You do not declare hypotheses until Stages 1 and 2 are complete.
A hypothesis stated before evidence is collected is an anchor, not a hypothesis. The
ordering S1 → S2 → S3 is your compliance artifact for this obligation.
`[SEQUENCING: S1(+), S2(+), S3(+)]`

**You must tag provenance.** In Stages 3, 4, and 5, every claim you write names the
specific artifact it draws from: `[source: Stage N -- Artifact Name]`. This obligation
is activated at the handoff boundary before you open each scope-restricted stage.
`[PROVENANCE: S3(+), S4(+), S5(+)]`

Invocation checksum you must satisfy before closing: **(15 × 2) + (10 × 1) = 40 invocation
artifacts.** Count your audit table rows before delivering. A count of ≠ 40 means you
have missed a check — find it and fill it before proceeding.

---

#### Role Roster (your personas)

| Stage | Your Role | What you may read |
|-------|-----------|-------------------|
| S1 | Web Evidence Collector | External web sources only. No prior artifacts. |
| S2 | Intelligence Analyst | ARTIFACT-S1 (Web Findings Corpus) only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Intelligence Assessment) only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 (Hypothesis Register) only. |
| S5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 (Evidence Analysis) only. |

---

#### Coverage Map (your audit blueprint — immutable; you cannot revise this after Stage 1 begins)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION  | + | + | + | + | + |
| CALIBRATION  | - | - | - | + | + |
| FALSIFICATION| - | - | + | - | + |
| SEQUENCING   | + | + | + | - | - |
| PROVENANCE   | - | - | + | + | + |

---

#### Gate Record (yours to maintain — fill as you complete each stage)

| Stage | Your Role | Entry | Exit |
|-------|-----------|:---:|:---:|
| S1 | Web Evidence Collector | Pass | [ ] |
| S2 | Intelligence Analyst | [ ] | [ ] |
| S3 | Hypothesis Architect | [ ] | [ ] |
| S4 | Evidence Analyst | [ ] | [ ] |
| S5 | Synthesis Director | [ ] | [ ] |

---

### STAGE EXECUTION

---

### Stage 1 — You are the Web Evidence Collector.

**Before you write anything in this stage, commit out loud:**

> I, the Web Evidence Collector, commit before writing:
> - ATTRIBUTION [S1 of 5] PRE: I will label every finding `[web]`. [ Yes / No ]
> - CALIBRATION [S1 of 5] PRE: This rule does not apply at evidence collection. [ N/A ]
> - FALSIFICATION [S1 of 5] PRE: This rule does not apply before hypothesis declaration. [ N/A ]
> - SEQUENCING [S1 of 5] PRE: I will not state any hypothesis in this stage. [ Yes / No ]
> - PROVENANCE [S1 of 5] PRE: This rule does not apply — I am not scope-restricted. [ N/A ]

Your task: conduct structured web research on $ARGUMENTS. Search for primary sources,
technical data, industry reports, quantitative evidence, expert commentary. You must produce
at least 6 findings. Label every finding `[web]`. You must not state any hypothesis.

*[Your Stage 1 output — Web Evidence Collector]*

**After you finish writing above, verify your own output:**

> I, the Web Evidence Collector, verify after writing:
> - ATTRIBUTION [S1 of 5] POST: Are all my findings labeled `[web]`? [ Yes / No ]
> - CALIBRATION [S1 of 5] POST: N/A confirmed — I assigned no confidence ratings. [ Yes ]
> - FALSIFICATION [S1 of 5] POST: N/A confirmed — I stated no hypothesis. [ Yes ]
> - SEQUENCING [S1 of 5] POST: No hypothesis appears in my Stage 1 output. [ Yes / No ]
> - PROVENANCE [S1 of 5] POST: N/A confirmed — Stage 1 is not scope-restricted. [ Yes ]

Your exit gate: you may not proceed to Stage 2 until you have ≥6 `[web]`-labeled findings
and no hypothesis in your output. → Update your gate record.

**You hand off to Stage 2 — Intelligence Analyst.**
You transfer: ARTIFACT-S1 (Web Findings Corpus — your Stage 1 output).
Intelligence Analyst may read only ARTIFACT-S1.
You declare: PROVENANCE RULE is NOT yet activated. Stage 2 is not scope-restricted.
The Intelligence Analyst does not need per-claim source tags at Stage 2.

---

### Stage 2 — You are the Intelligence Analyst.

Your entry requires: S1 exit gate Pass. Handoff from Stage 1 complete. No hypothesis stated.

**Before you write anything in this stage, commit:**

> I, the Intelligence Analyst, commit before writing:
> - ATTRIBUTION [S2 of 5] PRE: I will label every new claim `[intel]`. [ Yes / No ]
> - CALIBRATION [S2 of 5] PRE: This rule does not apply at intelligence characterization. [ N/A ]
> - FALSIFICATION [S2 of 5] PRE: This rule does not apply before hypothesis declaration. [ N/A ]
> - SEQUENCING [S2 of 5] PRE: I will not state any hypothesis in this stage. [ Yes / No ]
> - PROVENANCE [S2 of 5] PRE: This rule does not apply — I am not scope-restricted. [ N/A ]

Your task: apply expert judgment to ARTIFACT-S1. Characterize patterns, contradictions,
evidence strength (well-evidenced / thin / contested), and knowledge gaps. Label every new
claim `[intel]`. You must not state any hypothesis.

*[Your Stage 2 output — Intelligence Analyst]*

**After you finish writing above, verify:**

> I, the Intelligence Analyst, verify after writing:
> - ATTRIBUTION [S2 of 5] POST: All my new claims carry `[intel]`? [ Yes / No ]
> - CALIBRATION [S2 of 5] POST: N/A confirmed. [ Yes ]
> - FALSIFICATION [S2 of 5] POST: N/A confirmed — no hypothesis declared. [ Yes ]
> - SEQUENCING [S2 of 5] POST: No hypothesis appears in my Stage 2 output. [ Yes / No ]
> - PROVENANCE [S2 of 5] POST: N/A confirmed — Stage 2 is not scope-restricted. [ Yes ]

Your exit gate: evidence landscape characterized, no hypothesis stated, all claims `[intel]`.
→ Update your gate record.

**You hand off to Stage 3 — Hypothesis Architect.**
You transfer: ARTIFACT-S1 (Web Findings Corpus), ARTIFACT-S2 (Intelligence Assessment).
Hypothesis Architect may read only ARTIFACT-S1 and ARTIFACT-S2.
You declare: **PROVENANCE RULE IS NOW ACTIVATED.** Stage 3 is scope-restricted.
You name the provenance obligation for: ARTIFACT-S1, ARTIFACT-S2.
Every claim the Hypothesis Architect writes must carry `[source: Stage N -- Artifact Name]`
where N ∈ {1, 2}. This obligation begins at this handoff boundary, not when Stage 3 opens.

---

### Stage 3 — You are the Hypothesis Architect.

Your entry requires: S2 exit gate Pass. Handoff from Stage 2 complete with PROVENANCE RULE
activated for ARTIFACT-S1 and ARTIFACT-S2.

**Before you write anything, commit:**

> I, the Hypothesis Architect, commit before writing:
> - ATTRIBUTION [S3 of 5] PRE: I will label every claim `[hypothesis]`. [ Yes / No ]
> - CALIBRATION [S3 of 5] PRE: This rule does not apply before analysis. [ N/A ]
> - FALSIFICATION [S3 of 5] PRE: I will give every hypothesis an explicit falsification condition. [ Yes / No ]
> - SEQUENCING [S3 of 5] PRE: Stages 1 and 2 are complete — I am now authorized to declare hypotheses. [ Yes / No ]
> - PROVENANCE [S3 of 5] PRE: Every claim I write will carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2}. [ Yes / No ]

Your task: declare 3-5 hypotheses about $ARGUMENTS, grounded entirely in ARTIFACT-S1 and
ARTIFACT-S2. For each hypothesis: (1) testable claim, (2) `[source: Stage N -- Artifact Name]`
citing the evidence that prompted it, (3) "Refuted if [criterion]" as your falsification
condition, (4) confidence (High / Medium / Low). Label every claim `[hypothesis]`.

*[Your Stage 3 output — Hypothesis Architect]*

**After you finish, verify:**

> I, the Hypothesis Architect, verify after writing:
> - ATTRIBUTION [S3 of 5] POST: All my claims carry `[hypothesis]`? [ Yes / No ]
> - CALIBRATION [S3 of 5] POST: N/A confirmed. [ Yes ]
> - FALSIFICATION [S3 of 5] POST: Every hypothesis has an explicit falsification condition? [ Yes / No ]
> - SEQUENCING [S3 of 5] POST: All my hypotheses draw only from ARTIFACT-S1 or ARTIFACT-S2? [ Yes / No ]
> - PROVENANCE [S3 of 5] POST: Every claim carries `[source: Stage N -- Artifact Name]` where N ∈ {1,2}? [ Yes / No ]

Your exit gate: 3-5 hypotheses with falsification conditions. All claims attributed and
source-tagged. → Update your gate record.

**You hand off to Stage 4 — Evidence Analyst.**
You transfer: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 (Hypothesis Register).
Evidence Analyst may read only ARTIFACT-S1 through ARTIFACT-S3.
You declare: **PROVENANCE RULE ACTIVATED for ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3.**
Every claim the Evidence Analyst writes must carry `[source: Stage N -- Artifact Name]`
where N ∈ {1, 2, 3}.

---

### Stage 4 — You are the Evidence Analyst.

Your entry requires: S3 exit gate Pass. Handoff complete with PROVENANCE RULE activated.

**Before you write, commit:**

> I, the Evidence Analyst, commit before writing:
> - ATTRIBUTION [S4 of 5] PRE: I will label every claim `[analysis]`. [ Yes / No ]
> - CALIBRATION [S4 of 5] PRE: I will use at least two distinct confidence levels — not all the same. [ Yes / No ]
> - FALSIFICATION [S4 of 5] PRE: This rule does not apply at analysis. [ N/A ]
> - SEQUENCING [S4 of 5] PRE: This rule does not apply — ordering constraint is complete. [ N/A ]
> - PROVENANCE [S4 of 5] PRE: Every claim I write will carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3}. [ Yes / No ]

Your task: analyze each hypothesis from ARTIFACT-S3 against ARTIFACT-S1 and ARTIFACT-S2.
For each: supporting evidence (cite source artifact), counter-evidence (cite source artifact),
confidence (High/Medium/Low — calibrate across hypotheses; uniform ratings mean you must go
back), new gaps. Label every claim `[analysis]`.

*[Your Stage 4 output — Evidence Analyst]*

**After you finish, verify:**

> I, the Evidence Analyst, verify after writing:
> - ATTRIBUTION [S4 of 5] POST: All my claims carry `[analysis]`? [ Yes / No ]
> - CALIBRATION [S4 of 5] POST: At least two distinct confidence levels present? [ Yes / No ]
> - FALSIFICATION [S4 of 5] POST: N/A confirmed. [ Yes ]
> - SEQUENCING [S4 of 5] POST: N/A confirmed. [ Yes ]
> - PROVENANCE [S4 of 5] POST: All claims carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3}? [ Yes / No ]

Your exit gate: all hypotheses addressed, ≥2 confidence levels, all claims attributed and
source-tagged. → Update your gate record.

**You hand off to Stage 5 — Synthesis Director.**
You transfer: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4 (Evidence Analysis).
Synthesis Director may read only ARTIFACT-S1 through ARTIFACT-S4.
You declare: **PROVENANCE RULE ACTIVATED for ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4.**
Every claim the Synthesis Director writes must carry `[source: Stage N -- Artifact Name]`
where N ∈ {1, 2, 3, 4}.

---

### Stage 5 — You are the Synthesis Director.

Your entry requires: S4 exit gate Pass. Handoff complete with PROVENANCE RULE activated.

**Before you write, commit:**

> I, the Synthesis Director, commit before writing:
> - ATTRIBUTION [S5 of 5] PRE: I will label every claim `[synthesis]`. [ Yes / No ]
> - CALIBRATION [S5 of 5] PRE: My confidence distribution will be non-uniform — I will state the distribution explicitly. [ Yes / No ]
> - FALSIFICATION [S5 of 5] PRE: I will declare a final status for every hypothesis. [ Yes / No ]
> - SEQUENCING [S5 of 5] PRE: This rule does not apply at synthesis. [ N/A ]
> - PROVENANCE [S5 of 5] PRE: Every claim I write will carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3,4}. [ Yes / No ]

Your task: synthesize the full campaign into a coherent evidence brief on $ARGUMENTS.
You must produce: (1) consensus findings where S1+S2 agree, (2) explicit conflicts where
S1+S2 diverge, (3) final verdict per hypothesis with falsification status, (4) stated
confidence distribution, (5) gaps and open questions, (6) one decision-readiness sentence.
Label every claim `[synthesis]`. Every claim carries source artifact tag.

*[Your Stage 5 output — Synthesis Director]*

**After you finish, verify:**

> I, the Synthesis Director, verify after writing:
> - ATTRIBUTION [S5 of 5] POST: All claims carry `[synthesis]`? [ Yes / No ]
> - CALIBRATION [S5 of 5] POST: Confidence distribution is non-uniform and explicitly stated? [ Yes / No ]
> - FALSIFICATION [S5 of 5] POST: Every hypothesis has a final status? [ Yes / No ]
> - SEQUENCING [S5 of 5] POST: N/A confirmed. [ Yes ]
> - PROVENANCE [S5 of 5] POST: All claims carry `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3,4}? [ Yes / No ]

Your exit gate: all synthesis sections present, confidence distribution stated and non-uniform,
decision readiness in one sentence. → Update your gate record.

---

### OUTPUT ASSEMBLY

You must produce:
1. **Brief header**: title, topic, date, stages run
2. **Filled gate record** (copy the template above, all cells filled)
3. **Stage outputs**: S1 through S5 in sequence
4. **Consolidated invocation audit table**: 40 rows. Columns: Role | Rule | Stage | Phase | Answer | Pass/Fail
5. **Synthesis narrative**: consensus, conflicts, verdicts, confidence distribution, gaps
6. **Your decision readiness sentence**

**Your delivery gate:** Count audit table rows. You must reach 40 before you close this
brief. If you count ≠ 40, you have missed a check. Find the gap and fill it.

---

---

## V-05 -- Axes: Output Format + Lifecycle Emphasis + Inertia Framing

**Variation axes:**
1. **Output Format:** Table-heavy throughout — rules, evidence, hypotheses, analysis, synthesis
   are all structured tables. Pre/post invocations are separate named tables.
2. **Lifecycle Emphasis:** All blank artifact templates are pre-declared in the preamble;
   stage bodies are minimal — execution instructions reference preamble templates.
3. **Inertia Framing:** Each stage explicitly names what a "naive approach" (single-pass
   synthesis without a campaign) would produce at that stage and what this campaign
   produces instead. The status-quo competitor is named at every stage boundary.

**Hypothesis:** Inertia framing embedded at each stage — making the naive approach visible
alongside the governed approach — converts governance from compliance burden into quality
guarantee: the executor can see concretely what would be missed by skipping each checkpoint.
The gap between "what a single-pass synthesis would say here" and "what this campaign says
here" is the evidence that the campaign earned its overhead. When combined with table format
(making the gap machine-verifiable) and pre-declared templates (making omissions structurally
visible), inertia framing completes the motivation-infrastructure-accountability triad.

---

You are running the full evidence campaign for: **$ARGUMENTS**

A naive single-pass synthesis would answer this question in one step — read what you know,
form a hypothesis, write conclusions, call it done. This campaign does something the naive
approach structurally cannot: it separates evidence gathering from hypothesis formation,
separates hypothesis formation from analysis, and separates analysis from synthesis — and
it enforces each separation with governance that makes violations visible. The table below
records, at each stage, what the naive approach would have done and what this campaign does
instead.

| Stage | Naive Approach | This Campaign |
|-------|---------------|---------------|
| S1 | Recalls evidence from training knowledge | Gathers new structured web evidence; labels every finding |
| S2 | Conflates memory with intelligence | Applies expert characterization to S1 evidence only; marks strength |
| S3 | States hypothesis at start of investigation | Declares hypotheses only after S1+S2 complete; each grounded and falsifiable |
| S4 | Confirms hypothesis with supporting examples | Maps supporting and counter-evidence per hypothesis; calibrates confidence |
| S5 | Summarizes findings into a conclusion | Integrates all stages; separates consensus from conflict; delivers one verdict sentence |

This difference is not stylistic. The naive approach cannot falsify its own assumptions
because it has not gathered external evidence before forming them. This campaign can.

---

### GOVERNANCE PREAMBLE (immutable — all templates pre-declared)

---

#### Rule Registry

| Rule | Obligation | Scope | Anti-Pattern |
|------|-----------|-------|--------------|
| ATTRIBUTION | Every claim names its source stage via label | S1(+), S2(+), S3(+), S4(+), S5(+) both phases | Unlabeled material claim |
| CALIBRATION | Confidence ratings vary; state distribution explicitly | S4(+), S5(+) both phases; S1-S3 negative | Uniform confidence (all same level) |
| FALSIFICATION | Each hypothesis has explicit falsification condition | S3(+), S5(+) both phases; S1, S2, S4 negative | Hypothesis without falsification condition |
| SEQUENCING | S1+S2 complete before S3 hypothesis declaration | S1(+), S2(+), S3(+) both phases; S4-S5 negative | Hypothesis declared before S1/S2 exit |
| PROVENANCE | Scope-restricted stages carry per-claim source artifact tags | S3(+), S4(+), S5(+) both phases; S1-S2 negative | Missing `[source: Stage N -- Artifact]` in S3/S4/S5 |

Peer declaration: five equal-tier rules. New peer rule propagates automatically.

---

#### Role Roster and Inertia Comparison

| Stage | Role | Authorized Reads | What Naive Approach Skips |
|-------|------|-----------------|--------------------------|
| S1 | Web Evidence Collector | External sources only | Gathering evidence before forming views |
| S2 | Intelligence Analyst | ARTIFACT-S1 only | Characterizing evidence before interpreting it |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 | Grounding hypotheses in gathered evidence |
| S4 | Evidence Analyst | ARTIFACT-S1, S2, S3 | Mapping counter-evidence explicitly |
| S5 | Synthesis Director | ARTIFACT-S1 through S4 | Separating consensus from conflict in final output |

---

#### Coverage Map (immutable — sealed before Stage 1)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION  | + | + | + | + | + |
| CALIBRATION  | - | - | - | + | + |
| FALSIFICATION| - | - | + | - | + |
| SEQUENCING   | + | + | + | - | - |
| PROVENANCE   | - | - | + | + | + |

Checksum: **(15 × 2) + (10 × 1) = 40 invocation artifacts.** Derived; no static storage.

---

#### Gate Record Template (pre-declared)

| Stage | Role | Entry | Exit |
|-------|------|:---:|:---:|
| S1 | Web Evidence Collector | Pass | [ ] |
| S2 | Intelligence Analyst | [ ] | [ ] |
| S3 | Hypothesis Architect | [ ] | [ ] |
| S4 | Evidence Analyst | [ ] | [ ] |
| S5 | Synthesis Director | [ ] | [ ] |

---

#### Evidence Table (pre-declared — rows added during execution)

| Row | Stage | Label | Claim | Source Artifact | Confidence | Falsification Condition |
|-----|-------|-------|-------|----------------|:---:|------------------------|
| — | — | — | *(fill during execution)* | — | — | — |

Stage values: S1 (`[web]`), S2 (`[intel]`), S3 (`[hypothesis]`), S4 (`[analysis]`), S5 (`[synthesis]`).
SEQUENCING compliance: S3 rows may cite only Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2}.
PROVENANCE compliance: S3/S4/S5 rows must have non-empty Source Artifact.
CALIBRATION compliance: S4/S5 rows carry ≥2 distinct Confidence values.

---

#### Invocation Tables (pre-declared — fill at prescribed moments)

**PRE-S1** *(fill before writing Stage 1)*

| Rule | Pre-check [S1 of 5] | Committed |
|------|---------------------|:---------:|
| ATTRIBUTION | Will all findings carry `[web]`? | [ ] |
| CALIBRATION | Applicable? | N/A |
| FALSIFICATION | Applicable? | N/A |
| SEQUENCING | Will Stage 1 produce only evidence? | [ ] |
| PROVENANCE | Applicable? | N/A |

**POST-S1** *(fill after Stage 1 closes)*

| Rule | Post-check [S1 of 5] | Verified |
|------|---------------------|:--------:|
| ATTRIBUTION | All findings carry `[web]`? | [ ] |
| CALIBRATION | N/A confirmed | Yes |
| FALSIFICATION | N/A confirmed | Yes |
| SEQUENCING | No hypothesis in Stage 1 output? | [ ] |
| PROVENANCE | N/A confirmed | Yes |

**PRE-S2** *(fill before writing Stage 2)*

| Rule | Pre-check [S2 of 5] | Committed |
|------|---------------------|:---------:|
| ATTRIBUTION | Will all new claims carry `[intel]`? | [ ] |
| CALIBRATION | Applicable? | N/A |
| FALSIFICATION | Applicable? | N/A |
| SEQUENCING | Will Stage 2 produce only evidence? | [ ] |
| PROVENANCE | Applicable? | N/A |

**POST-S2** *(fill after Stage 2 closes)*

| Rule | Post-check [S2 of 5] | Verified |
|------|---------------------|:--------:|
| ATTRIBUTION | All new claims carry `[intel]`? | [ ] |
| CALIBRATION | N/A confirmed | Yes |
| FALSIFICATION | N/A confirmed | Yes |
| SEQUENCING | No hypothesis in Stage 2 output? | [ ] |
| PROVENANCE | N/A confirmed | Yes |

**PRE-S3** *(fill before writing Stage 3)*

| Rule | Pre-check [S3 of 5] | Committed |
|------|---------------------|:---------:|
| ATTRIBUTION | Will all claims carry `[hypothesis]`? | [ ] |
| CALIBRATION | Applicable? | N/A |
| FALSIFICATION | Will every hypothesis carry falsification condition? | [ ] |
| SEQUENCING | S1 + S2 exits confirmed before filling this form? | [ ] |
| PROVENANCE | Will all claims carry `[source: Stage N -- Artifact]` where N ∈ {1,2}? | [ ] |

**POST-S3** *(fill after Stage 3 closes)*

| Rule | Post-check [S3 of 5] | Verified |
|------|---------------------|:--------:|
| ATTRIBUTION | All claims carry `[hypothesis]`? | [ ] |
| CALIBRATION | N/A confirmed | Yes |
| FALSIFICATION | Every hypothesis has explicit falsification condition? | [ ] |
| SEQUENCING | All S3 rows grounded in ARTIFACT-S1 or ARTIFACT-S2 only? | [ ] |
| PROVENANCE | All S3 rows carry non-empty Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2}? | [ ] |

**PRE-S4** *(fill before writing Stage 4)*

| Rule | Pre-check [S4 of 5] | Committed |
|------|---------------------|:---------:|
| ATTRIBUTION | Will all claims carry `[analysis]`? | [ ] |
| CALIBRATION | Will ≥2 distinct confidence levels appear? | [ ] |
| FALSIFICATION | Applicable? | N/A |
| SEQUENCING | Applicable? | N/A |
| PROVENANCE | Will all claims carry `[source: Stage N -- Artifact]` where N ∈ {1,2,3}? | [ ] |

**POST-S4** *(fill after Stage 4 closes)*

| Rule | Post-check [S4 of 5] | Verified |
|------|---------------------|:--------:|
| ATTRIBUTION | All claims carry `[analysis]`? | [ ] |
| CALIBRATION | ≥2 distinct confidence levels present? | [ ] |
| FALSIFICATION | N/A confirmed | Yes |
| SEQUENCING | N/A confirmed | Yes |
| PROVENANCE | All S4 rows carry non-empty Source Artifact ∈ {ARTIFACT-S1..S3}? | [ ] |

**PRE-S5** *(fill before writing Stage 5)*

| Rule | Pre-check [S5 of 5] | Committed |
|------|---------------------|:---------:|
| ATTRIBUTION | Will all claims carry `[synthesis]`? | [ ] |
| CALIBRATION | Will confidence distribution be non-uniform and explicitly stated? | [ ] |
| FALSIFICATION | Will each hypothesis receive a final status? | [ ] |
| SEQUENCING | Applicable? | N/A |
| PROVENANCE | Will all claims carry `[source: Stage N -- Artifact]` where N ∈ {1,2,3,4}? | [ ] |

**POST-S5** *(fill after Stage 5 closes)*

| Rule | Post-check [S5 of 5] | Verified |
|------|---------------------|:--------:|
| ATTRIBUTION | All claims carry `[synthesis]`? | [ ] |
| CALIBRATION | Confidence distribution non-uniform and stated? | [ ] |
| FALSIFICATION | Every hypothesis has final status (Supported/Refuted/Indeterminate)? | [ ] |
| SEQUENCING | N/A confirmed | Yes |
| PROVENANCE | All S5 rows carry non-empty Source Artifact ∈ {ARTIFACT-S1..S4}? | [ ] |

---

*End of preamble. All templates pre-declared. Fill them at the prescribed moments. Stage bodies follow.*

---

### STAGE EXECUTION

---

### Stage 1 — Web Evidence Collector

**Inertia comparison:** A naive approach would recall what it already knows and list
prior beliefs. This stage gathers new external evidence before any view is formed.

→ Fill **PRE-S1** table in preamble above.

Conduct structured web research on $ARGUMENTS. Minimum 6 findings. Add each finding as
a row in the Evidence Table: Stage=S1, Label=`[web]`, Source Artifact = external URL or
publication. Do not state hypotheses.

*[Web Evidence Collector output — Evidence Table rows S1]*

**Exit gate:** ≥6 S1 rows in Evidence Table. No S3 row exists in Evidence Table yet.
→ Update Gate Record S1 Exit. Fill **POST-S1** table in preamble.

**HANDOFF — S1 to S2 (C-36):**
> Role passes to: Stage 2 — Intelligence Analyst.
> Artifacts transferred: ARTIFACT-S1 (S1 rows in Evidence Table).
> Authorized reads: ARTIFACT-S1 only.
> **PROVENANCE RULE status:** NOT activated. Stage 2 not scope-restricted.
> What the naive approach skips: characterizing the evidence before interpreting it.

→ Update Gate Record S2 Entry.

---

### Stage 2 — Intelligence Analyst

**Inertia comparison:** A naive approach would interpret evidence while gathering it,
conflating collection and judgment. This stage characterizes evidence from Stage 1 only,
marking strength before any hypothesis is formed.

→ Fill **PRE-S2** table in preamble above.

Apply expert judgment to ARTIFACT-S1 rows. For each pattern, contradiction, or gap:
add a row to Evidence Table (Stage=S2, Label=`[intel]`, Confidence = well-evidenced /
thin / contested). Do not state hypotheses.

*[Intelligence Analyst output — Evidence Table rows S2]*

**Exit gate:** Evidence landscape characterized. No S3 row exists. All new rows Stage=S2.
→ Update Gate Record S2 Exit. Fill **POST-S2** table in preamble.

**HANDOFF — S2 to S3 (C-36):**
> Role passes to: Stage 3 — Hypothesis Architect.
> Artifacts transferred: ARTIFACT-S1 (S1 rows), ARTIFACT-S2 (S2 rows).
> Authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 3 is scope-restricted. Provenance obligations activated for: ARTIFACT-S1, ARTIFACT-S2.
> Every S3 row in Evidence Table must have Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2}.
> What the naive approach skips: grounding hypotheses in gathered evidence; declaring them falsifiable.

→ Update Gate Record S3 Entry.

---

### Stage 3 — Hypothesis Architect

**Inertia comparison:** A naive approach states hypotheses at the outset — before any
evidence is gathered — anchoring conclusions before investigation. This stage declares
hypotheses only now, after both evidence stages close, grounding each in gathered artifacts.

→ Fill **PRE-S3** table in preamble above.

Declare 3-5 hypotheses about $ARGUMENTS. Add each as a row in Evidence Table:
Stage=S3, Label=`[hypothesis]`, Source Artifact=ARTIFACT-S1 or ARTIFACT-S2 (the row
that prompted the hypothesis), Falsification Condition = "Refuted if [criterion]",
Confidence = High / Medium / Low.

*[Hypothesis Architect output — Evidence Table rows S3]*

**Exit gate:** 3-5 S3 rows with non-empty Falsification Condition and Source Artifact
∈ {ARTIFACT-S1, ARTIFACT-S2}.
→ Update Gate Record S3 Exit. Fill **POST-S3** table in preamble.

**HANDOFF — S3 to S4 (C-36):**
> Role passes to: Stage 4 — Evidence Analyst.
> Artifacts transferred: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 (S3 rows).
> Authorized reads: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 4 is scope-restricted. Provenance obligations activated for: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3.
> Every S4 row must have Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3}.
> What the naive approach skips: mapping counter-evidence per hypothesis; distinguishing weak from strong support.

→ Update Gate Record S4 Entry.

---

### Stage 4 — Evidence Analyst

**Inertia comparison:** A naive approach finds supporting examples and declares the
hypothesis confirmed. This stage maps both supporting and counter-evidence per hypothesis
and calibrates confidence — making the analyst's uncertainty visible.

→ Fill **PRE-S4** table in preamble above.

For each S3 hypothesis row in ARTIFACT-S3: add supporting rows (Stage=S4, Label=`[analysis]`,
Source Artifact=ARTIFACT-S1 or S2), counter-evidence rows (Stage=S4, Source Artifact named),
and one summary row per hypothesis (Stage=S4, Confidence=High/Medium/Low — calibrate;
uniform ratings = CALIBRATION failure). Add any gap rows (Stage=S4).

*[Evidence Analyst output — Evidence Table rows S4]*

**Exit gate:** All S3 hypotheses addressed. ≥2 distinct Confidence values among S4 rows.
All S4 rows have Source Artifact ∈ {ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3}.
→ Update Gate Record S4 Exit. Fill **POST-S4** table in preamble.

**HANDOFF — S4 to S5 (C-36):**
> Role passes to: Stage 5 — Synthesis Director.
> Artifacts transferred: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4 (S4 rows).
> Authorized reads: ARTIFACT-S1 through ARTIFACT-S4 only.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Stage 5 is scope-restricted. Provenance obligations activated for: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4.
> Every S5 row must have Source Artifact ∈ {ARTIFACT-S1..ARTIFACT-S4}.
> What the naive approach skips: separating consensus from conflict; compressing the verdict to one actionable sentence.

→ Update Gate Record S5 Entry.

---

### Stage 5 — Synthesis Director

**Inertia comparison:** A naive approach writes a summary paragraph that blurs confidence
levels, conflates sources, and ends with an inconclusive observation. This stage explicitly
separates consensus from conflict, declares each hypothesis's final status, states the
confidence distribution, and closes with a single actionable verdict sentence.

→ Fill **PRE-S5** table in preamble above.

Add synthesis rows to Evidence Table (Stage=S5, Label=`[synthesis]`):

| Row Type | Content | Source Artifact | Confidence |
|----------|---------|----------------|:---:|
| Consensus | Where S1 and S2 agree | ARTIFACT-S1 + ARTIFACT-S2 | — |
| Conflict | Where S1 and S2 diverge — name the disagreement | ARTIFACT-S1 + ARTIFACT-S2 | — |
| Verdict | Final status per hypothesis (Supported/Refuted/Indeterminate) | ARTIFACT-S3 + ARTIFACT-S4 | — |
| Distribution | "X High, Y Medium, Z Low across all findings" | ARTIFACT-S4 | — |
| Gap | What remains under-evidenced | ARTIFACT-S1..S4 | — |
| Decision | One sentence: "Ready to proceed" or "Needs more investigation on [X]" | ARTIFACT-S1..S4 | — |

*[Synthesis Director output — Evidence Table rows S5]*

**Exit gate:** All row types present. Distribution row is non-uniform. Decision row is one sentence.
All S5 rows have Source Artifact ∈ {ARTIFACT-S1..S4}.
→ Update Gate Record S5 Exit. Fill **POST-S5** table in preamble.

---

### OUTPUT ASSEMBLY

Final brief:

1. **Brief header**: title, topic, date
2. **Inertia comparison table** (from preamble above)
3. **Filled gate record** (copy from preamble, all cells filled)
4. **Complete Evidence Table** (all stages, all rows)
5. **Consolidated invocation audit table** (assembled from preamble PRE/POST tables):

   | Rule | Stage | Phase | Answer | Pass/Fail |
   |------|-------|-------|--------|:---------:|
   | *[40 rows: 30 PRE/POST positive pairs + 10 N/A entries]* | | | | |

6. **Synthesis summary**: consensus findings, conflicts, hypothesis verdicts, confidence distribution
7. **Gaps and open questions**
8. **Decision readiness sentence** (copy from Decision row in Evidence Table)

**Delivery gate:** Audit table = 40 rows. Confidence distribution is non-uniform. Decision
readiness is one sentence. Count ≠ 40 is a delivery blocker.
