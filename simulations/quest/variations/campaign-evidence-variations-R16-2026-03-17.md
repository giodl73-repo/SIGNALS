---
skill: quest-variate
skill_target: campaign-evidence
date: 2026-03-17
round: 16
rubric_version: 16
---

# Variates: campaign-evidence (Round 16)

Five complete, runnable skill body prompts. Single-axis variations first (V-01 through V-03),
combined axes second (V-04 through V-05).

**Structural signals from R15 scorecard driving R16 variation axes:**

- **Signal 1 (now C-39):** V-03's interrogative column headers were a PASS+ excellence signal —
  the question lives at the structural column level, not the cell level. Any blank POST cell is
  simultaneously an unanswered column-level standing question, making the gap doubly visible.
  Promoted to criterion C-39 in v16.

- **Signal 2 (now C-40):** V-04's Intel→Web role reversal implicitly demonstrated that
  SEQUENCING RULE governs evidence-stage relative ordering — not only hypothesis placement.
  The scope extension was unnamed and unauditable. C-40 requires explicit scope declaration:
  the SEQUENCING RULE must name evidence-stage ordering as a governed dimension alongside
  hypothesis placement.

**Baseline inherited from R15 (all R16 variates must satisfy):**

Coverage map (5 rules × 5 stages = 25 cells):

| Rule | S1: Web | S2: Intel | S3: Hypo | S4: Analysis | S5: Synth | Positive | Negative |
|------|---------|-----------|----------|--------------|-----------|----------|----------|
| ATTRIBUTION  | + | + | + | + | + | 5 | 0 |
| CALIBRATION  | - | - | - | + | + | 2 | 3 |
| FALSIFICATION| - | - | + | - | + | 2 | 3 |
| SEQUENCING   | + | + | + | - | - | 3 | 2 |
| PROVENANCE   | - | - | + | + | + | 3 | 2 |
| **Total**    |   |   |   |   |   | **15** | **10** |

**Invocation checksum:** 40 artifacts = (15 positive × 2 phases) + (10 negative × 1)

**R15 baseline requirements inherited:**
- Universal binary `[ Yes / No ]` on all applicable invocations (C-22)
- Stage-index suffix `[Stage N of 5]` on every invocation (C-23)
- Entry and exit conditions per stage (C-24)
- Gate record pre-templated in preamble with blank cells (C-27)
- Named role + "Role passes to:" transfer at each boundary (C-30)
- Negative invocation at every non-applicable stage (C-31)
- Role access scope declared per stage (C-32)
- Invocation matrix checksum (C-33)
- Artifact provenance tags `[source: Stage N -- Artifact Name]` in scope-restricted stages (C-34)
- Dual-phase PRE/POST checkpoints at all applicable stages (C-35)
- Handoff declarations enumerate transferred artifacts + PROVENANCE activation status (C-36)
- PRE and POST as separately-named table artifacts with execution content physically between (C-37)
- Full invocation apparatus pre-declared in preamble as blank templates + stage-body timing directives (C-38)
- Explicit C-14 rationale sentence for evidence-first sequencing

**New in R16 (both required in all variates):**
- C-39: Governing question IS the column header in PRE/POST tables
- C-40: SEQUENCING RULE declaration explicitly names evidence-stage relative ordering as governed

---

## V-01 — Axis: Output format (interrogative column headers, consolidated table)

**Variation axis:** The governing question is promoted to the column header of every PRE and
POST checkpoint table. PRE tables carry "Will [this rule] hold? [SN of 5]" as the answer-column
header; POST tables carry "Does [this rule] hold? [SN of 5]". The question is not a cell
prompt — it is the structural column name. Any unfilled answer cell is simultaneously a blank
answer AND an unanswered standing column-level question, making gaps doubly visible (C-39).
SEQUENCING RULE explicitly declares evidence-stage relative ordering as a governed dimension
alongside hypothesis placement (C-40). Standard three-zone layout (PRE zone / EXECUTION zone /
POST zone) from R14 V-01.

**Hypothesis:** Interrogative at column-header level is the minimum-change C-39 implementation.
The consolidated table format is preserved from R15; only the column header wording changes.
This isolates C-39's structural contribution: the question shifts from a cell-embedded prompt
(which an executor can skip while filling adjacent cells) to a column-level commitment that
frames every cell in that column as an answer to a standing question.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable — cannot be modified after any stage executes.

---

#### Rule Registry (all five rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+); PRE and POST at each]`
Every material claim names its source stage via label: `[web]` S1, `[intel]` S2,
`[hypothesis]` S3, `[analysis]` S4, `[synthesis]` S5. An unlabeled claim is unattributed.

**CALIBRATION RULE** `[invoked at: S4(+), S5(+); PRE and POST; S1(-), S2(-), S3(-)]`
Confidence ratings must vary across findings. Uniform ratings are a calibration failure.
Anti-uniformity guard: if all confidence ratings at any applicable stage are identical,
CALIBRATION fails. Distribution must be stated explicitly at S4 and S5.

**FALSIFICATION RULE** `[invoked at: S3(+), S5(+); PRE and POST; S1(-), S2(-), S4(-)]`
Each hypothesis carries an explicit falsification condition. Final status: Supported /
Refuted / Indeterminate. A hypothesis without a falsification condition is a belief, not a
hypothesis.

**SEQUENCING RULE** `[invoked at: S1(+), S2(+), S3(+); PRE and POST; S4(-), S5(-)]`
Governs two ordered constraints:
(1) **Hypothesis placement** — evidence stages S1 and S2 complete before hypothesis
    declaration at S3. Rationale: "A hypothesis anchored before evidence gathering is a bias,
    not a hypothesis."
(2) **Evidence-stage relative ordering** — S1 (Web) executes before S2 (Intelligence).
    This ordering is a named governance decision, not a structural convention. Any reversal
    requires explicit SEQUENCING RULE justification at the S1 boundary.
Both constraints are governed by this rule and invocable by identifier.

**PROVENANCE RULE** `[invoked at: S3(+), S4(+), S5(+); PRE and POST; S1(-), S2(-)]`
Activated at the handoff boundary preceding each scope-restricted stage. Every claim in
S3, S4, S5 carries `[source: Stage N -- Artifact Name]`. Claim without provenance tag is
a structural gap.

Peer declaration: all five rules are equal-tier. Adding a sixth peer rule propagates
automatically through the coverage map and checksum; no static integers require manual update.

---

#### Role Roster

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Web Evidence Collector | External sources only. No prior artifacts. |
| S2 | Intelligence Analyst | ARTIFACT-S1 only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only. |
| S5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 only. |

---

#### Coverage Map (immutable — sealed before Stage 1)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION  | + | + | + | + | + |
| CALIBRATION  | - | - | - | + | + |
| FALSIFICATION| - | - | + | - | + |
| SEQUENCING   | + | + | + | - | - |
| PROVENANCE   | - | - | + | + | + |

Invocation checksum: **40 artifacts** = (15 positive × 2 phases) + (10 negative × 1).
Derived from map dimensions; updates automatically if rules or stages are added.
This map is finalized before Stage 1 begins and cannot be modified after execution starts.

---

#### Gate Record Template (pre-instantiated — blank cells filled during execution)

| Stage | Role | Entry Condition | Entry | Exit Condition | Exit |
|-------|------|----------------|:-----:|----------------|:----:|
| S1 | Web Evidence Collector | First stage — no prerequisites | Pass | 6+ `[web]` findings; no hypothesis stated | [ ] |
| S2 | Intelligence Analyst | S1 exit Pass; handoff S1→S2 complete | [ ] | Evidence landscape characterized; no hypothesis; all `[intel]` | [ ] |
| S3 | Hypothesis Architect | S2 exit Pass; handoff S2→S3 complete + PROVENANCE activated | [ ] | 3–5 hypotheses with falsification conditions; all carry provenance tags | [ ] |
| S4 | Evidence Analyst | S3 exit Pass; handoff S3→S4 complete + PROVENANCE activated | [ ] | All hypotheses analyzed; 2+ confidence levels; all carry provenance tags | [ ] |
| S5 | Synthesis Director | S4 exit Pass; handoff S4→S5 complete + PROVENANCE activated | [ ] | Consensus/conflict separated; all hypotheses have final status; one-sentence decision readiness | [ ] |

---

#### Pre-Declared Invocation Apparatus (C-38 — blank templates for all 5 stages)

> Fill each PRE table BEFORE writing stage output. Fill each POST table AFTER stage output closes.
> Templates appear here as blank. Identical forms appear in each stage body as timing directives.

**FORM PRE-S1** | **FORM POST-S1**
PRE: "Will [this rule] hold? [S1 of 5]" | POST: "Does [this rule] hold? [S1 of 5]"

**FORM PRE-S2** | **FORM POST-S2**
PRE: "Will [this rule] hold? [S2 of 5]" | POST: "Does [this rule] hold? [S2 of 5]"

**FORM PRE-S3** | **FORM POST-S3**
PRE: "Will [this rule] hold? [S3 of 5]" | POST: "Does [this rule] hold? [S3 of 5]"

**FORM PRE-S4** | **FORM POST-S4**
PRE: "Will [this rule] hold? [S4 of 5]" | POST: "Does [this rule] hold? [S4 of 5]"

**FORM PRE-S5** | **FORM POST-S5**
PRE: "Will [this rule] hold? [S5 of 5]" | POST: "Does [this rule] hold? [S5 of 5]"

---

### STAGE EXECUTION

Do not advance to Stage N+1 until Stage N's exit gate is all-Pass and its handoff block
is complete.

---

### Stage 1 — Web Evidence Collector

**Entry gate:**

| Condition | Status |
|-----------|--------|
| First stage — no prior stages required | Pass |
| No hypothesis has been stated anywhere in this document | Pass |

---
**Fill FORM PRE-S1 now — before writing any Stage 1 content.**

#### PRE-EXECUTION COMMITMENT TABLE — Stage 1

| Rule | Applicable [S1 of 5]? | Will this rule hold? [S1 of 5] |
|------|:---------------------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — evidence collection | N/A |
| FALSIFICATION | No — no hypothesis yet | N/A |
| SEQUENCING | Yes — S1 executes before S2 (evidence-stage ordering) and no hypothesis stated | [ Yes / No ] |
| PROVENANCE | No — S1 is not scope-restricted | N/A |

---
**Stage 1 execution begins here.**

Conduct structured web research on $ARGUMENTS. Search for: primary sources, recent
publications, technical data, industry reports, expert commentary, quantitative evidence.
Label every finding `[web]`. Do not state hypotheses. Collect broadly; at least 6 findings.

**Stage 1 execution closes here.**

---
**Fill FORM POST-S1 now — after Stage 1 output above is complete.**

#### POST-EXECUTION VERIFICATION TABLE — Stage 1

| Rule | Applicable [S1 of 5]? | Does this rule hold? [S1 of 5] |
|------|:---------------------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — evidence collection | N/A confirmed |
| FALSIFICATION | No — no hypothesis declared | N/A confirmed |
| SEQUENCING | Yes | [ Yes / No ] |
| PROVENANCE | No — S1 not scope-restricted | N/A confirmed |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 6+ findings, each labeled `[web]` | [ Pass / Fail ] |
| No hypothesis stated anywhere in Stage 1 output | [ Pass / Fail ] |
| SEQUENCING evidence-stage ordering confirmed: S1 ran before S2 | [ Pass / Fail ] |

**HANDOFF DECLARATION — S1 to S2:**

> **Role passes to: Stage 2 — Intelligence Analyst.**
> Transferring: ARTIFACT-S1 (Web Findings Corpus).
> Intelligence Analyst authorized to read: ARTIFACT-S1 only.
> **PROVENANCE RULE status:** NOT activated at this boundary. Stage 2 is not scope-restricted.
> PROVENANCE RULE activates at the S2→S3 handoff.

---

### Stage 2 — Intelligence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S1 exit gate all-Pass | [ Pass / Fail ] |
| Handoff S1→S2 complete | [ Pass / Fail ] |
| No hypothesis stated anywhere yet | [ Pass / Fail ] |

---
**Fill FORM PRE-S2 now — before writing any Stage 2 content.**

#### PRE-EXECUTION COMMITMENT TABLE — Stage 2

| Rule | Applicable [S2 of 5]? | Will this rule hold? [S2 of 5] |
|------|:---------------------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — evidence characterization | N/A |
| FALSIFICATION | No — no hypothesis yet | N/A |
| SEQUENCING | Yes — S2 executes after S1 (evidence-stage ordering confirmed) and no hypothesis stated | [ Yes / No ] |
| PROVENANCE | No — S2 is not scope-restricted | N/A |

---
**Stage 2 execution begins here.**

Apply expert judgment to ARTIFACT-S1. Characterize evidence patterns, contradictions,
strength ratings (well-evidenced / thin / contested), and knowledge gaps. Label every new
claim `[intel]`. Do not state hypotheses.

**Stage 2 execution closes here.**

---
**Fill FORM POST-S2 now — after Stage 2 output above is complete.**

#### POST-EXECUTION VERIFICATION TABLE — Stage 2

| Rule | Applicable [S2 of 5]? | Does this rule hold? [S2 of 5] |
|------|:---------------------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — evidence characterization | N/A confirmed |
| FALSIFICATION | No — no hypothesis declared | N/A confirmed |
| SEQUENCING | Yes | [ Yes / No ] |
| PROVENANCE | No — S2 not scope-restricted | N/A confirmed |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Evidence landscape characterized; patterns, conflicts, gaps named | [ Pass / Fail ] |
| No hypothesis in Stage 2 output | [ Pass / Fail ] |
| All new claims carry `[intel]` | [ Pass / Fail ] |

**HANDOFF DECLARATION — S2 to S3:**

> **Role passes to: Stage 3 — Hypothesis Architect.**
> Transferring: ARTIFACT-S1 (Web Findings Corpus), ARTIFACT-S2 (Intelligence Assessment).
> Hypothesis Architect authorized to read: ARTIFACT-S1 + ARTIFACT-S2 only.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Obligations active for ARTIFACT-S1 and ARTIFACT-S2.
> Every Stage 3 claim must carry `[source: Stage N -- Artifact Name]` where N ∈ {1, 2}.

---

### Stage 3 — Hypothesis Architect

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S2 exit gate all-Pass | [ Pass / Fail ] |
| Handoff S2→S3 complete with PROVENANCE activation | [ Pass / Fail ] |
| PROVENANCE active for ARTIFACT-S1 and ARTIFACT-S2 | [ Pass / Fail ] |

---
**Fill FORM PRE-S3 now — before writing any Stage 3 content.**

#### PRE-EXECUTION COMMITMENT TABLE — Stage 3

| Rule | Applicable [S3 of 5]? | Will this rule hold? [S3 of 5] |
|------|:---------------------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — hypothesis stage | N/A |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | Yes — opening only after S1 + S2 exits confirmed | [ Yes / No ] |
| PROVENANCE | Yes | [ Yes / No ] |

---
**Stage 3 execution begins here.**

Declare 3–5 hypotheses about $ARGUMENTS. Each must: (1) state a testable claim; (2) cite
the prompting evidence `[source: Stage 1 -- Web Findings Corpus]` or
`[source: Stage 2 -- Intelligence Assessment]`; (3) state an explicit falsification
condition; (4) assign preliminary confidence (High / Medium / Low).
Label every claim `[hypothesis]`.

**Stage 3 execution closes here.**

---
**Fill FORM POST-S3 now — after Stage 3 output above is complete.**

#### POST-EXECUTION VERIFICATION TABLE — Stage 3

| Rule | Applicable [S3 of 5]? | Does this rule hold? [S3 of 5] |
|------|:---------------------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — hypothesis stage | N/A confirmed |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | Yes | [ Yes / No ] |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 3–5 hypotheses with explicit falsification conditions | [ Pass / Fail ] |
| All claims carry `[hypothesis]` and provenance tags | [ Pass / Fail ] |

**HANDOFF DECLARATION — S3 to S4:**

> **Role passes to: Stage 4 — Evidence Analyst.**
> Transferring: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 (Hypothesis Register).
> Evidence Analyst authorized to read: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Obligations active for ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3.
> Every Stage 4 claim must carry `[source: Stage N -- Artifact Name]` where N ∈ {1, 2, 3}.

---

### Stage 4 — Evidence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S3 exit gate all-Pass | [ Pass / Fail ] |
| Handoff S3→S4 complete + PROVENANCE activated | [ Pass / Fail ] |

---
**Fill FORM PRE-S4 now — before writing any Stage 4 content.**

#### PRE-EXECUTION COMMITMENT TABLE — Stage 4

| Rule | Applicable [S4 of 5]? | Will this rule hold? [S4 of 5] |
|------|:---------------------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | No — analysis stage | N/A |
| SEQUENCING | No — ordering constraint complete | N/A |
| PROVENANCE | Yes | [ Yes / No ] |

---
**Stage 4 execution begins here.**

Analyze each hypothesis from ARTIFACT-S3 against ARTIFACT-S1 and ARTIFACT-S2.
For each: summarize supporting evidence, counter-evidence, assign confidence
(High / Medium / Low — calibrate; uniform ratings fail), note gaps.
Label all claims `[analysis]`. Attach `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3}.

**Stage 4 execution closes here.**

---
**Fill FORM POST-S4 now — after Stage 4 output above is complete.**

#### POST-EXECUTION VERIFICATION TABLE — Stage 4

| Rule | Applicable [S4 of 5]? | Does this rule hold? [S4 of 5] |
|------|:---------------------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | No — analysis stage | N/A confirmed |
| SEQUENCING | No — ordering constraint complete | N/A confirmed |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| All hypotheses analyzed | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| All claims carry `[analysis]` and provenance tags | [ Pass / Fail ] |

**HANDOFF DECLARATION — S4 to S5:**

> **Role passes to: Stage 5 — Synthesis Director.**
> Transferring: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4 (Evidence Analysis).
> Synthesis Director authorized to read: ARTIFACT-S1 through ARTIFACT-S4 only.
> **PROVENANCE RULE ACTIVATED AT THIS BOUNDARY.**
> Obligations active for all four artifacts.
> Every Stage 5 claim must carry `[source: Stage N -- Artifact Name]` where N ∈ {1, 2, 3, 4}.

---

### Stage 5 — Synthesis Director

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S4 exit gate all-Pass | [ Pass / Fail ] |
| Handoff S4→S5 complete + PROVENANCE activated | [ Pass / Fail ] |

---
**Fill FORM PRE-S5 now — before writing any Stage 5 content.**

#### PRE-EXECUTION COMMITMENT TABLE — Stage 5

| Rule | Applicable [S5 of 5]? | Will this rule hold? [S5 of 5] |
|------|:---------------------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | No — synthesis stage | N/A |
| PROVENANCE | Yes | [ Yes / No ] |

---
**Stage 5 execution begins here.**

Synthesize findings into a coherent evidence brief on $ARGUMENTS:
1. **Consensus** — where S1 and S2 agree, with `[source: Stage N -- Artifact Name]`
2. **Conflicts** — where S1 and S2 diverge; name each conflict explicitly
3. **Hypothesis verdicts** — Supported / Refuted / Indeterminate with final confidence (non-uniform)
4. **Falsification status** — each hypothesis's falsification condition confirmed or rejected
5. **Gaps and open questions** — what remains under-evidenced after the full campaign
6. **Decision readiness** — one sentence naming posture and, if not ready, the specific gap

Label all claims `[synthesis]`. Every claim carries `[source: Stage N -- Artifact Name]`.

**Stage 5 execution closes here.**

---
**Fill FORM POST-S5 now — after Stage 5 output above is complete.**

#### POST-EXECUTION VERIFICATION TABLE — Stage 5

| Rule | Applicable [S5 of 5]? | Does this rule hold? [S5 of 5] |
|------|:---------------------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | No — synthesis stage | N/A confirmed |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Consensus and conflict explicitly separated | [ Pass / Fail ] |
| All hypotheses carry final Supported/Refuted/Indeterminate status | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| Gaps and open questions surfaced | [ Pass / Fail ] |
| Decision readiness stated in one sentence | [ Pass / Fail ] |
| All claims carry `[synthesis]` and provenance tags | [ Pass / Fail ] |

---

## Consolidated Invocation Audit Table

| Rule | S1 PRE | S1 POST | S2 PRE | S2 POST | S3 PRE | S3 POST | S4 PRE | S4 POST | S5 PRE | S5 POST | Total |
|------|--------|---------|--------|---------|--------|---------|--------|---------|--------|---------|-------|
| ATTRIBUTION | + | + | + | + | + | + | + | + | + | + | 10 |
| CALIBRATION | N/A | N/A | N/A | N/A | N/A | N/A | + | + | + | + | 4+3=7 |
| FALSIFICATION | N/A | N/A | N/A | N/A | + | + | N/A | N/A | + | + | 4+3=7 |
| SEQUENCING | + | + | + | + | + | + | N/A | N/A | N/A | N/A | 6+2=8 |
| PROVENANCE | N/A | N/A | N/A | N/A | + | + | + | + | + | + | 6+2=8 |
| **Total** | | | | | | | | | | | **40** |

Row count = (15 positive × 2) + (10 negative × 1) = 40. Derived from coverage map dimensions.

---

## V-02 — Axis: Lifecycle emphasis (SEQUENCING RULE dual-track with separate invocation lines)

**Variation axis:** SEQUENCING RULE is split into two explicitly-named tracks in the rule
declaration: **SEQUENCING-HYPO** (hypothesis placement constraint) and **SEQUENCING-ORDER**
(evidence-stage relative ordering constraint). Each track is invoked separately at applicable
stages, giving the coverage map 6 effective rule-rows for SEQUENCING intersections. This makes
each governance dimension independently auditable: a brief that satisfies hypothesis placement
but silently reorders evidence stages produces a SEQUENCING-ORDER FAIL that is structurally
visible — not concealed by the passing SEQUENCING-HYPO invocation. C-39 is implemented via
interrogative column headers. C-40 is satisfied by the dual-track declaration.

**Hypothesis:** Splitting SEQUENCING into two named tracks extends the evidence-stage ordering
constraint from an implicit structural property to an independently-invocable governance
dimension. A reader auditing the brief can verify hypothesis placement compliance and
evidence-stage ordering compliance as separate questions, each with its own invocation trail.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable after execution starts.

---

#### Rule Registry (all rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+)]`
Every claim names its source stage: `[web]` S1, `[intel]` S2, `[hypothesis]` S3,
`[analysis]` S4, `[synthesis]` S5. Unlabeled claim = unattributed.

**CALIBRATION RULE** `[invoked at: S4(+), S5(+); S1(-), S2(-), S3(-)]`
Confidence ratings vary across findings. Uniform ratings = calibration failure.
Anti-uniformity guard: state distribution explicitly. Both phases required at applicable stages.

**FALSIFICATION RULE** `[invoked at: S3(+), S5(+); S1(-), S2(-), S4(-)]`
Each hypothesis carries an explicit falsification condition.
Final status: Supported / Refuted / Indeterminate.

**SEQUENCING-HYPO RULE** `[invoked at: S1(+), S2(+), S3(+); S4(-), S5(-)]`
Evidence stages S1 and S2 complete before hypothesis declaration at S3.
Rationale: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis."
This is a named governance rule referenceable by identifier at each stage it governs.

**SEQUENCING-ORDER RULE** `[invoked at: S1(+), S2(+); S3(-), S4(-), S5(-)]`
Web Evidence Collector (S1) executes before Intelligence Analyst (S2). This ordering
is a governed constraint, not a structural convention. Reversing S1↔S2 requires explicit
SEQUENCING-ORDER RULE justification stated at the S1 boundary before S1 executes.
Both C-40-governed dimensions are now separately invocable: SEQUENCING-HYPO governs
the evidence-to-hypothesis boundary; SEQUENCING-ORDER governs the S1→S2 evidence boundary.

**PROVENANCE RULE** `[invoked at: S3(+), S4(+), S5(+); S1(-), S2(-)]`
Activated at the handoff boundary preceding each scope-restricted stage.
Every claim in S3, S4, S5 carries `[source: Stage N -- Artifact Name]`.

Peer declaration: all six rule-rows are equal-tier. Coverage map has 6 rule rows × 5 stages.
Adding a new peer rule propagates automatically through the map and checksum.

---

#### Revised Coverage Map (6 rules × 5 stages = 30 cells)

| Rule | S1 | S2 | S3 | S4 | S5 | Positive | Negative |
|------|----|----|----|----|----|----------|----------|
| ATTRIBUTION     | + | + | + | + | + | 5 | 0 |
| CALIBRATION     | - | - | - | + | + | 2 | 3 |
| FALSIFICATION   | - | - | + | - | + | 2 | 3 |
| SEQUENCING-HYPO | + | + | + | - | - | 3 | 2 |
| SEQUENCING-ORDER| + | + | - | - | - | 2 | 3 |
| PROVENANCE      | - | - | + | + | + | 3 | 2 |
| **Total**       |   |   |   |   |   | **17** | **13** |

Invocation checksum: **47 artifacts** = (17 positive × 2 phases) + (13 negative × 1).
Derived from map dimensions (6 rules × 5 stages = 30 cells; 17 positive, 13 negative).
Finalized before Stage 1; cannot be modified after execution begins.

---

#### Role Roster

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Web Evidence Collector | External sources only. |
| S2 | Intelligence Analyst | ARTIFACT-S1 only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only. |
| S5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 only. |

---

#### Gate Record Template

| Stage | Role | Entry | Exit |
|-------|------|:-----:|:----:|
| S1 | Web Evidence Collector | Pass | [ ] |
| S2 | Intelligence Analyst | [ ] | [ ] |
| S3 | Hypothesis Architect | [ ] | [ ] |
| S4 | Evidence Analyst | [ ] | [ ] |
| S5 | Synthesis Director | [ ] | [ ] |

---

#### Pre-Declared Invocation Forms (C-38 — blank templates, all stages)

All PRE and POST forms for all 5 stages pre-instantiated below. Stage bodies carry
timing directives referencing form IDs. Fill PRE before execution, POST after.

FORM-PRE-S1 / FORM-POST-S1 / FORM-PRE-S2 / FORM-POST-S2 / FORM-PRE-S3 / FORM-POST-S3 /
FORM-PRE-S4 / FORM-POST-S4 / FORM-PRE-S5 / FORM-POST-S5 — templates embedded in each stage.

---

### Stage 1 — Web Evidence Collector

**Entry gate:** First stage — no prerequisites. Pass.

---
> **Timing directive:** Fill FORM-PRE-S1 before writing Stage 1 content.

#### FORM-PRE-S1: PRE-EXECUTION TABLE — Stage 1

| Rule | Applicable? | Will this rule hold? [S1 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — evidence collection | N/A |
| FALSIFICATION | No — no hypothesis | N/A |
| SEQUENCING-HYPO | Yes — no hypothesis will appear | [ Yes / No ] |
| SEQUENCING-ORDER | Yes — S1 executes before S2 | [ Yes / No ] |
| PROVENANCE | No — not scope-restricted | N/A |

---
*Stage 1 execution — Web Evidence Collector:*

Conduct structured web research on $ARGUMENTS. Label every finding `[web]`.
Do not state hypotheses. Collect at least 6 findings from diverse primary and secondary sources.

---
> **Timing directive:** Fill FORM-POST-S1 after Stage 1 content is complete.

#### FORM-POST-S1: POST-EXECUTION TABLE — Stage 1

| Rule | Applicable? | Does this rule hold? [S1 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No | N/A confirmed |
| FALSIFICATION | No | N/A confirmed |
| SEQUENCING-HYPO | Yes | [ Yes / No ] |
| SEQUENCING-ORDER | Yes | [ Yes / No ] |
| PROVENANCE | No | N/A confirmed |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 6+ `[web]` labeled findings | [ Pass / Fail ] |
| No hypothesis stated | [ Pass / Fail ] |
| SEQUENCING-ORDER confirmed: S1 ran before S2 | [ Pass / Fail ] |

**HANDOFF S1→S2:** Role passes to Stage 2 — Intelligence Analyst.
Transferring: ARTIFACT-S1 (Web Findings Corpus). Authorized reads: ARTIFACT-S1 only.
PROVENANCE RULE: NOT activated — Stage 2 is not scope-restricted.

---

### Stage 2 — Intelligence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S1 exit gate all-Pass | [ Pass / Fail ] |
| Handoff S1→S2 complete | [ Pass / Fail ] |

---
> **Timing directive:** Fill FORM-PRE-S2 before writing Stage 2 content.

#### FORM-PRE-S2: PRE-EXECUTION TABLE — Stage 2

| Rule | Applicable? | Will this rule hold? [S2 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — evidence characterization | N/A |
| FALSIFICATION | No — no hypothesis | N/A |
| SEQUENCING-HYPO | Yes — no hypothesis will appear | [ Yes / No ] |
| SEQUENCING-ORDER | Yes — confirming S1 completed before this stage opened | [ Yes / No ] |
| PROVENANCE | No — not scope-restricted | N/A |

---
*Stage 2 execution — Intelligence Analyst:*

Apply expert judgment to ARTIFACT-S1. Characterize evidence patterns, contradictions,
strength ratings (well-evidenced / thin / contested), and knowledge gaps.
Label every new claim `[intel]`. Do not state hypotheses.

---
> **Timing directive:** Fill FORM-POST-S2 after Stage 2 content is complete.

#### FORM-POST-S2: POST-EXECUTION TABLE — Stage 2

| Rule | Applicable? | Does this rule hold? [S2 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No | N/A confirmed |
| FALSIFICATION | No | N/A confirmed |
| SEQUENCING-HYPO | Yes | [ Yes / No ] |
| SEQUENCING-ORDER | Yes | [ Yes / No ] |
| PROVENANCE | No | N/A confirmed |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Evidence landscape characterized; patterns, conflicts, gaps named | [ Pass / Fail ] |
| No hypothesis in Stage 2 | [ Pass / Fail ] |
| All new claims carry `[intel]` | [ Pass / Fail ] |

**HANDOFF S2→S3:** Role passes to Stage 3 — Hypothesis Architect.
Transferring: ARTIFACT-S1, ARTIFACT-S2 (Intelligence Assessment).
Authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
**PROVENANCE RULE ACTIVATED.** Obligations for ARTIFACT-S1 and ARTIFACT-S2.
Every Stage 3 claim: `[source: Stage N -- Artifact Name]` where N ∈ {1, 2}.

---

### Stage 3 — Hypothesis Architect

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S2 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S2→S3 boundary | [ Pass / Fail ] |

---
> **Timing directive:** Fill FORM-PRE-S3 before writing Stage 3 content.

#### FORM-PRE-S3: PRE-EXECUTION TABLE — Stage 3

| Rule | Applicable? | Will this rule hold? [S3 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — hypothesis stage | N/A |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING-HYPO | Yes — opening only after S1 + S2 exits confirmed | [ Yes / No ] |
| SEQUENCING-ORDER | No — ordering constraint complete | N/A |
| PROVENANCE | Yes | [ Yes / No ] |

---
*Stage 3 execution — Hypothesis Architect:*

Declare 3–5 hypotheses. Each: (1) testable claim; (2) prompting evidence with
`[source: Stage N -- Artifact Name]`; (3) explicit falsification condition;
(4) preliminary confidence (High / Medium / Low). Label every claim `[hypothesis]`.

---
> **Timing directive:** Fill FORM-POST-S3 after Stage 3 content is complete.

#### FORM-POST-S3: POST-EXECUTION TABLE — Stage 3

| Rule | Applicable? | Does this rule hold? [S3 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No | N/A confirmed |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING-HYPO | Yes | [ Yes / No ] |
| SEQUENCING-ORDER | No — ordering constraint complete | N/A confirmed |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 3–5 hypotheses with explicit falsification conditions | [ Pass / Fail ] |
| All claims carry `[hypothesis]` and provenance tags | [ Pass / Fail ] |

**HANDOFF S3→S4:** Role passes to Stage 4 — Evidence Analyst.
Transferring: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 (Hypothesis Register).
Authorized reads: ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only.
**PROVENANCE RULE ACTIVATED.** Every Stage 4 claim: `[source: Stage N -- Artifact Name]` N ∈ {1,2,3}.

---

### Stage 4 — Evidence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S3 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S3→S4 boundary | [ Pass / Fail ] |

---
> **Timing directive:** Fill FORM-PRE-S4 before writing Stage 4 content.

#### FORM-PRE-S4: PRE-EXECUTION TABLE — Stage 4

| Rule | Applicable? | Will this rule hold? [S4 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | No — analysis stage | N/A |
| SEQUENCING-HYPO | No — constraint complete | N/A |
| SEQUENCING-ORDER | No — constraint complete | N/A |
| PROVENANCE | Yes | [ Yes / No ] |

---
*Stage 4 execution — Evidence Analyst:*

Analyze each hypothesis from ARTIFACT-S3 against ARTIFACT-S1 and ARTIFACT-S2.
Assign varied confidence (High / Medium / Low — uniform ratings fail CALIBRATION).
Label `[analysis]`. Attach `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3}.

---
> **Timing directive:** Fill FORM-POST-S4 after Stage 4 content is complete.

#### FORM-POST-S4: POST-EXECUTION TABLE — Stage 4

| Rule | Applicable? | Does this rule hold? [S4 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | No | N/A confirmed |
| SEQUENCING-HYPO | No | N/A confirmed |
| SEQUENCING-ORDER | No | N/A confirmed |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| All hypotheses analyzed | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| All claims carry `[analysis]` and provenance tags | [ Pass / Fail ] |

**HANDOFF S4→S5:** Role passes to Stage 5 — Synthesis Director.
Transferring: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3, ARTIFACT-S4.
Authorized reads: ARTIFACT-S1 through ARTIFACT-S4 only.
**PROVENANCE RULE ACTIVATED.** Every Stage 5 claim: `[source: Stage N -- Artifact Name]` N ∈ {1,2,3,4}.

---

### Stage 5 — Synthesis Director

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S4 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S4→S5 boundary | [ Pass / Fail ] |

---
> **Timing directive:** Fill FORM-PRE-S5 before writing Stage 5 content.

#### FORM-PRE-S5: PRE-EXECUTION TABLE — Stage 5

| Rule | Applicable? | Will this rule hold? [S5 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING-HYPO | No — synthesis stage | N/A |
| SEQUENCING-ORDER | No — synthesis stage | N/A |
| PROVENANCE | Yes | [ Yes / No ] |

---
*Stage 5 execution — Synthesis Director:*

Synthesize findings into a coherent brief on $ARGUMENTS:
1. Consensus findings — where S1 and S2 agree
2. Conflicts — where S1 and S2 diverge; name each explicitly
3. Hypothesis verdicts — Supported / Refuted / Indeterminate with final confidence (non-uniform)
4. Falsification status per hypothesis
5. Gaps and open questions
6. Decision readiness — one sentence naming posture and, if not ready, the specific gap

Label `[synthesis]`. Attach `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3,4}.

---
> **Timing directive:** Fill FORM-POST-S5 after Stage 5 content is complete.

#### FORM-POST-S5: POST-EXECUTION TABLE — Stage 5

| Rule | Applicable? | Does this rule hold? [S5 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING-HYPO | No | N/A confirmed |
| SEQUENCING-ORDER | No | N/A confirmed |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Consensus and conflict explicitly separated | [ Pass / Fail ] |
| All hypotheses carry final status | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| Gaps surfaced | [ Pass / Fail ] |
| Decision readiness in one sentence | [ Pass / Fail ] |

---

## V-03 — Axis: Phrasing register (per-rule mini-tables; rule-specific interrogative headers)

**Variation axis:** Each stage's dual-phase checkpoints are implemented as per-rule mini-tables —
one two-row table per rule per stage (PRE row + POST row, separated by execution text). Each
mini-table's column header names the rule explicitly: "Will ATTRIBUTION hold? [SN of 5]" /
"Does ATTRIBUTION hold? [SN of 5]". This is the strongest C-39 implementation: the question
is rule-specific at the header level, so any blank cell under "Will ATTRIBUTION hold?" is an
unanswered question whose subject (ATTRIBUTION) is declared in the column name, not inferred.
Phrasing is formal but direct; role names use domain-evocative titles. SEQUENCING RULE
explicitly declares evidence-stage ordering (C-40).

**Hypothesis:** Per-rule mini-tables with rule-specific interrogative headers are the most
granular C-39 implementation. The distinction from consolidated tables: in a consolidated table,
"Will this rule hold?" is a generic column header that all rules share; in a per-rule mini-table,
"Will CALIBRATION hold?" identifies both the question and its subject at the structural level.
An executor who skips the CALIBRATION mini-table produces an absence of an artifact named
"CALIBRATION checkpoint" — not a blank cell in a shared table, but a missing named object.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable after execution starts.

---

#### Rule Registry (all five rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+)]`
Source label required on every material claim: `[web]` S1, `[intel]` S2,
`[hypothesis]` S3, `[analysis]` S4, `[synthesis]` S5.

**CALIBRATION RULE** `[invoked at: S4(+), S5(+); S1(-), S2(-), S3(-)]`
Confidence ratings must span at least two distinct levels per applicable stage.
If all confidence ratings are identical, CALIBRATION fails. Uniform distribution = failure.

**FALSIFICATION RULE** `[invoked at: S3(+), S5(+); S1(-), S2(-), S4(-)]`
Every hypothesis carries an explicit falsification condition.
Final status: Supported / Refuted / Indeterminate. No falsification condition = belief, not hypothesis.

**SEQUENCING RULE** `[invoked at: S1(+), S2(+), S3(+); S4(-), S5(-)]`
Governs two constraints:
(1) **Hypothesis placement** — S1 and S2 complete before S3. Rationale: a hypothesis
    declared before evidence gathering is an anchor, not a prediction.
(2) **Evidence-stage relative ordering** — S1 (Web) executes before S2 (Intelligence).
    This is a governed ordering. Declaring the rationale for any reversal is required.
Both constraints are invocable by rule name and are not structural conventions.

**PROVENANCE RULE** `[invoked at: S3(+), S4(+), S5(+); S1(-), S2(-)]`
Activated at each scope-restricted stage handoff. Every claim in S3–S5 carries
`[source: Stage N -- Artifact Name]`. No tag = structural gap.

Peer declaration: all five rules are equal-tier. Map extends automatically with new rules.

---

#### Role Roster

| Stage | Role | Authorized Reads |
|-------|------|-----------------|
| S1 | Web Scout | External sources only |
| S2 | Intelligence Reader | ARTIFACT-S1 |
| S3 | Hypothesis Architect | ARTIFACT-S1, ARTIFACT-S2 |
| S4 | Evidence Analyst | ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 |
| S5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 |

---

#### Coverage Map (immutable)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION  | + | + | + | + | + |
| CALIBRATION  | - | - | - | + | + |
| FALSIFICATION| - | - | + | - | + |
| SEQUENCING   | + | + | + | - | - |
| PROVENANCE   | - | - | + | + | + |

Invocation checksum: **40 artifacts** = (15 × 2) + (10 × 1). Derived from map dimensions.
Finalized before Stage 1; immutable.

---

#### Gate Record Template

| Stage | Entry | Exit |
|-------|:-----:|:----:|
| S1 — Web Scout | Pass | [ ] |
| S2 — Intelligence Reader | [ ] | [ ] |
| S3 — Hypothesis Architect | [ ] | [ ] |
| S4 — Evidence Analyst | [ ] | [ ] |
| S5 — Synthesis Director | [ ] | [ ] |

---

#### Pre-Declared Mini-Table Library (C-38 — blank templates for all stages)

Per-rule mini-tables for all 5 stages are pre-declared below as blank templates.
Each stage body carries a timing directive naming which forms to fill and when.
Every mini-table is named: e.g., MINI-ATTRIBUTION-S1, MINI-CALIBRATION-S4.

> Notation: each mini-table has two rows: PRE (fill before execution) and POST (fill after).
> The stage's execution content occupies the space between filling the PRE row and POST row.

---

### Stage 1 — Web Scout

**Entry gate:** First stage. No prerequisites. Pass.

> **Timing directive:** For each rule below, fill the PRE cell before writing Stage 1 content.
> Fill the POST cell after Stage 1 content closes.

#### MINI-ATTRIBUTION-S1

| Phase | Will ATTRIBUTION hold? [S1 of 5] |
|-------|:---------------------------------:|
| PRE | [ Yes / No ] |

*— Stage 1 ATTRIBUTION checkpoint: execution content between PRE and POST rows —*

| Phase | Does ATTRIBUTION hold? [S1 of 5] |
|-------|:---------------------------------:|
| POST | [ Yes / No ] |

#### MINI-CALIBRATION-S1

| Phase | Does CALIBRATION apply? [S1 of 5] |
|-------|:---------------------------------:|
| PRE | N/A — evidence collection stage |
| POST | N/A confirmed |

#### MINI-FALSIFICATION-S1

| Phase | Does FALSIFICATION apply? [S1 of 5] |
|-------|:------------------------------------:|
| PRE | N/A — no hypothesis declared yet |
| POST | N/A confirmed |

#### MINI-SEQUENCING-S1

| Phase | Will SEQUENCING hold? [S1 of 5] |
|-------|:--------------------------------:|
| PRE | [ Yes / No ] |

*— Stage 1 SEQUENCING checkpoint: execution content between PRE and POST rows —*

| Phase | Does SEQUENCING hold? [S1 of 5] |
|-------|:--------------------------------:|
| POST | [ Yes / No ] |

#### MINI-PROVENANCE-S1

| Phase | Does PROVENANCE apply? [S1 of 5] |
|-------|:---------------------------------:|
| PRE | N/A — S1 is not scope-restricted |
| POST | N/A confirmed |

---

*Stage 1 execution — Web Scout:*

Conduct structured web research on $ARGUMENTS. Label every finding `[web]`.
Do not state hypotheses. Collect at least 6 diverse findings.

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 6+ `[web]` labeled findings | [ Pass / Fail ] |
| No hypothesis stated | [ Pass / Fail ] |

**HANDOFF S1→S2:** Role passes to Stage 2 — Intelligence Reader.
Transferring: ARTIFACT-S1 (Web Findings Corpus).
Intelligence Reader authorized reads: ARTIFACT-S1 only.
PROVENANCE RULE: NOT activated — Stage 2 not scope-restricted.

---

### Stage 2 — Intelligence Reader

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S1 exit gate all-Pass | [ Pass / Fail ] |
| Handoff S1→S2 complete | [ Pass / Fail ] |

> **Timing directive:** Fill PRE rows below before writing Stage 2 content.
> Fill POST rows after Stage 2 content closes.

#### MINI-ATTRIBUTION-S2

| Phase | Will ATTRIBUTION hold? [S2 of 5] |
|-------|:---------------------------------:|
| PRE | [ Yes / No ] |

*— Stage 2 ATTRIBUTION checkpoint: execution content between PRE and POST rows —*

| Phase | Does ATTRIBUTION hold? [S2 of 5] |
|-------|:---------------------------------:|
| POST | [ Yes / No ] |

#### MINI-CALIBRATION-S2

| Phase | Does CALIBRATION apply? [S2 of 5] |
|-------|:---------------------------------:|
| PRE | N/A — evidence characterization |
| POST | N/A confirmed |

#### MINI-FALSIFICATION-S2

| Phase | Does FALSIFICATION apply? [S2 of 5] |
|-------|:------------------------------------:|
| PRE | N/A — no hypothesis yet |
| POST | N/A confirmed |

#### MINI-SEQUENCING-S2

| Phase | Will SEQUENCING hold? [S2 of 5] |
|-------|:--------------------------------:|
| PRE | [ Yes / No ] |

*— Stage 2 SEQUENCING checkpoint: execution content between PRE and POST rows —*

| Phase | Does SEQUENCING hold? [S2 of 5] |
|-------|:--------------------------------:|
| POST | [ Yes / No ] |

#### MINI-PROVENANCE-S2

| Phase | Does PROVENANCE apply? [S2 of 5] |
|-------|:---------------------------------:|
| PRE | N/A — S2 not scope-restricted |
| POST | N/A confirmed |

---

*Stage 2 execution — Intelligence Reader:*

Apply expert judgment to ARTIFACT-S1. Characterize patterns, contradictions, strength ratings,
gaps. Label every new claim `[intel]`. Do not state hypotheses.

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Evidence landscape characterized; patterns, conflicts, gaps named | [ Pass / Fail ] |
| No hypothesis in Stage 2 | [ Pass / Fail ] |
| All new claims carry `[intel]` | [ Pass / Fail ] |

**HANDOFF S2→S3:** Role passes to Stage 3 — Hypothesis Architect.
Transferring: ARTIFACT-S1, ARTIFACT-S2 (Intelligence Assessment).
Hypothesis Architect authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
**PROVENANCE RULE ACTIVATED.** Obligations for ARTIFACT-S1, ARTIFACT-S2.
Every Stage 3 claim: `[source: Stage N -- Artifact Name]` N ∈ {1, 2}.

---

### Stage 3 — Hypothesis Architect

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S2 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S2→S3 | [ Pass / Fail ] |

> **Timing directive:** Fill PRE rows below before writing Stage 3 content.
> Fill POST rows after Stage 3 content closes.

#### MINI-ATTRIBUTION-S3

| Phase | Will ATTRIBUTION hold? [S3 of 5] |
|-------|:---------------------------------:|
| PRE | [ Yes / No ] |

*— execution between PRE and POST —*

| Phase | Does ATTRIBUTION hold? [S3 of 5] |
|-------|:---------------------------------:|
| POST | [ Yes / No ] |

#### MINI-CALIBRATION-S3

| Phase | Does CALIBRATION apply? [S3 of 5] |
|-------|:---------------------------------:|
| PRE | N/A — hypothesis stage |
| POST | N/A confirmed |

#### MINI-FALSIFICATION-S3

| Phase | Will FALSIFICATION hold? [S3 of 5] |
|-------|:-----------------------------------:|
| PRE | [ Yes / No ] |

*— execution between PRE and POST —*

| Phase | Does FALSIFICATION hold? [S3 of 5] |
|-------|:-----------------------------------:|
| POST | [ Yes / No ] |

#### MINI-SEQUENCING-S3

| Phase | Will SEQUENCING hold? [S3 of 5] |
|-------|:--------------------------------:|
| PRE | [ Yes / No ] |

*— execution between PRE and POST —*

| Phase | Does SEQUENCING hold? [S3 of 5] |
|-------|:--------------------------------:|
| POST | [ Yes / No ] |

#### MINI-PROVENANCE-S3

| Phase | Will PROVENANCE hold? [S3 of 5] |
|-------|:--------------------------------:|
| PRE | [ Yes / No ] |

*— execution between PRE and POST —*

| Phase | Does PROVENANCE hold? [S3 of 5] |
|-------|:--------------------------------:|
| POST | [ Yes / No ] |

---

*Stage 3 execution — Hypothesis Architect:*

Declare 3–5 hypotheses. Each: (1) testable claim; (2) prompting evidence cited as
`[source: Stage N -- Artifact Name]`; (3) explicit falsification condition;
(4) preliminary confidence (High / Medium / Low). Label every claim `[hypothesis]`.

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 3–5 hypotheses with falsification conditions | [ Pass / Fail ] |
| All claims carry `[hypothesis]` and provenance tags | [ Pass / Fail ] |

**HANDOFF S3→S4:** Role passes to Stage 4 — Evidence Analyst.
Transferring: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3.
Authorized reads: S1 + S2 + S3 only.
**PROVENANCE RULE ACTIVATED.** Every Stage 4 claim: `[source: Stage N -- Artifact Name]` N ∈ {1,2,3}.

---

### Stage 4 — Evidence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S3 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S3→S4 | [ Pass / Fail ] |

> **Timing directive:** Fill PRE rows below before writing Stage 4 content.
> Fill POST rows after Stage 4 content closes.

#### MINI-ATTRIBUTION-S4

| Phase | Will ATTRIBUTION hold? [S4 of 5] |
|-------|:---------------------------------:|
| PRE | [ Yes / No ] |

*— execution between PRE and POST —*

| Phase | Does ATTRIBUTION hold? [S4 of 5] |
|-------|:---------------------------------:|
| POST | [ Yes / No ] |

#### MINI-CALIBRATION-S4

| Phase | Will CALIBRATION hold? [S4 of 5] |
|-------|:---------------------------------:|
| PRE | [ Yes / No ] |

*— execution between PRE and POST —*

| Phase | Does CALIBRATION hold? [S4 of 5] |
|-------|:---------------------------------:|
| POST | [ Yes / No ] |

#### MINI-FALSIFICATION-S4

| Phase | Does FALSIFICATION apply? [S4 of 5] |
|-------|:------------------------------------:|
| PRE | N/A — analysis stage |
| POST | N/A confirmed |

#### MINI-SEQUENCING-S4

| Phase | Does SEQUENCING apply? [S4 of 5] |
|-------|:---------------------------------:|
| PRE | N/A — ordering constraint complete |
| POST | N/A confirmed |

#### MINI-PROVENANCE-S4

| Phase | Will PROVENANCE hold? [S4 of 5] |
|-------|:--------------------------------:|
| PRE | [ Yes / No ] |

*— execution between PRE and POST —*

| Phase | Does PROVENANCE hold? [S4 of 5] |
|-------|:--------------------------------:|
| POST | [ Yes / No ] |

---

*Stage 4 execution — Evidence Analyst:*

Analyze each hypothesis from ARTIFACT-S3 against ARTIFACT-S1 and ARTIFACT-S2.
Assign varied confidence (High / Medium / Low — uniform fails CALIBRATION).
Label `[analysis]`. Attach `[source: Stage N -- Artifact Name]` N ∈ {1,2,3}.

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| All hypotheses analyzed with supporting and counter-evidence | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| All claims carry `[analysis]` and provenance tags | [ Pass / Fail ] |

**HANDOFF S4→S5:** Role passes to Stage 5 — Synthesis Director.
Transferring: ARTIFACT-S1 through ARTIFACT-S4.
Synthesis Director authorized reads: S1–S4 only.
**PROVENANCE RULE ACTIVATED.** Every Stage 5 claim: `[source: Stage N -- Artifact Name]` N ∈ {1,2,3,4}.

---

### Stage 5 — Synthesis Director

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S4 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S4→S5 | [ Pass / Fail ] |

> **Timing directive:** Fill PRE rows below before writing Stage 5 content.
> Fill POST rows after Stage 5 content closes.

#### MINI-ATTRIBUTION-S5

| Phase | Will ATTRIBUTION hold? [S5 of 5] |
|-------|:---------------------------------:|
| PRE | [ Yes / No ] |

*— execution between PRE and POST —*

| Phase | Does ATTRIBUTION hold? [S5 of 5] |
|-------|:---------------------------------:|
| POST | [ Yes / No ] |

#### MINI-CALIBRATION-S5

| Phase | Will CALIBRATION hold? [S5 of 5] |
|-------|:---------------------------------:|
| PRE | [ Yes / No ] |

*— execution between PRE and POST —*

| Phase | Does CALIBRATION hold? [S5 of 5] |
|-------|:---------------------------------:|
| POST | [ Yes / No ] |

#### MINI-FALSIFICATION-S5

| Phase | Will FALSIFICATION hold? [S5 of 5] |
|-------|:-----------------------------------:|
| PRE | [ Yes / No ] |

*— execution between PRE and POST —*

| Phase | Does FALSIFICATION hold? [S5 of 5] |
|-------|:-----------------------------------:|
| POST | [ Yes / No ] |

#### MINI-SEQUENCING-S5

| Phase | Does SEQUENCING apply? [S5 of 5] |
|-------|:---------------------------------:|
| PRE | N/A — synthesis stage |
| POST | N/A confirmed |

#### MINI-PROVENANCE-S5

| Phase | Will PROVENANCE hold? [S5 of 5] |
|-------|:--------------------------------:|
| PRE | [ Yes / No ] |

*— execution between PRE and POST —*

| Phase | Does PROVENANCE hold? [S5 of 5] |
|-------|:--------------------------------:|
| POST | [ Yes / No ] |

---

*Stage 5 execution — Synthesis Director:*

Synthesize all evidence into a coherent brief on $ARGUMENTS:
1. Consensus — where S1 and S2 agree, cited
2. Conflicts — where S1 and S2 diverge, named explicitly
3. Hypothesis verdicts — Supported / Refuted / Indeterminate with final varied confidence
4. Falsification status — each hypothesis's condition confirmed or rejected
5. Gaps and open questions
6. Decision readiness — one sentence naming posture and specific gap if not ready

Label `[synthesis]`. Every claim carries `[source: Stage N -- Artifact Name]`.

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Consensus and conflict explicitly separated | [ Pass / Fail ] |
| All hypotheses carry final status | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| Gaps surfaced | [ Pass / Fail ] |
| Decision readiness in one sentence | [ Pass / Fail ] |

---

## V-04 — Combined: Role sequence (Intel→Web) + Interrogative headers + Explicit C-40 scope

**Variation axes:** (1) Role sequence — Intelligence Analyst runs as Stage 1, Web Evidence
Collector as Stage 2. (2) Interrogative column headers (C-39). (3) SEQUENCING RULE explicitly
declares evidence-stage relative ordering as a governed dimension with named rationale (C-40).

The combination is the key structural advance: in R15 V-04, the role reversal implicitly
demonstrated that SEQUENCING governs evidence-stage ordering, but the demonstration was unnamed.
Here, the SEQUENCING RULE declaration explicitly states: "The sequence Intelligence (S1) → Web
(S2) is a named governance decision subject to SEQUENCING RULE invocation and justification.
Any alternate ordering requires explicit SEQUENCING RULE rationale at the S1 boundary."
This makes the implicit R15 V-04 demonstration into an auditable commitment: the evidence-stage
ordering is now a rule-governed choice, not a structural convention.

**Hypothesis:** Role reversal + explicit C-40 scope declaration forces SEQUENCING RULE invocation
at the S1→S2 boundary with a specific question: "Does this evidence stage execute in its declared
position in the Intelligence→Web sequence?" This invocation has no analog in standard Web→Intel
ordering campaigns because the default order is treated as a convention, not a rule. Making
the sequence explicit and governed forces every campaign to answer the question, whether running
the default or a reversal.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable after execution starts.

---

#### Rule Registry (all five rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+)]`
Every material claim names its source stage: `[intel]` S1, `[web]` S2,
`[hypothesis]` S3, `[analysis]` S4, `[synthesis]` S5.

**CALIBRATION RULE** `[invoked at: S4(+), S5(+); S1(-), S2(-), S3(-)]`
Confidence ratings must vary across findings. Uniform ratings = failure.
Anti-uniformity guard: state distribution at S4 and S5. At least two distinct levels required.

**FALSIFICATION RULE** `[invoked at: S3(+), S5(+); S1(-), S2(-), S4(-)]`
Each hypothesis carries an explicit falsification condition.
Final status: Supported / Refuted / Indeterminate.

**SEQUENCING RULE** `[invoked at: S1(+), S2(+), S3(+); S4(-), S5(-)]`
Governs two explicitly-named constraints:
(1) **Evidence-stage relative ordering** — Intelligence Analyst (S1) executes before
    Web Evidence Collector (S2). This ordering is a named SEQUENCING RULE decision.
    Rationale: internal intelligence characterization frames the evidence before external
    web collection broadens it — reversing this sequence changes the framing relationship.
    Any executor who runs Web before Intelligence must invoke SEQUENCING RULE at S1 and
    provide a justification for the departure before S1 output begins.
(2) **Hypothesis placement** — both evidence stages S1 and S2 complete before hypothesis
    declaration at S3. Rationale: "A hypothesis declared before evidence gathering is an
    anchor masquerading as a prediction."
Both constraints are first-class governance dimensions — invocable by identifier, auditable
independently.

**PROVENANCE RULE** `[invoked at: S3(+), S4(+), S5(+); S1(-), S2(-)]`
Activated at handoff boundaries preceding scope-restricted stages.
Every claim in S3–S5 carries `[source: Stage N -- Artifact Name]`.

Peer declaration: all five rules equal-tier. Map auto-extends with additional rules.

---

#### Role Roster (Intel→Web sequence)

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Intelligence Analyst | Internal sources, prior knowledge only. No web evidence. |
| S2 | Web Evidence Collector | ARTIFACT-S1 (Intelligence Assessment) + external sources. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 (Web Findings Corpus) only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 (Hypothesis Register) only. |
| S5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 only. |

---

#### Coverage Map (immutable)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION  | + | + | + | + | + |
| CALIBRATION  | - | - | - | + | + |
| FALSIFICATION| - | - | + | - | + |
| SEQUENCING   | + | + | + | - | - |
| PROVENANCE   | - | - | + | + | + |

Invocation checksum: **40 artifacts** = (15 × 2) + (10 × 1). Derived from map; immutable.

---

#### Gate Record Template

| Stage | Role | Entry | Exit |
|-------|------|:-----:|:----:|
| S1 | Intelligence Analyst | Pass | [ ] |
| S2 | Web Evidence Collector | [ ] | [ ] |
| S3 | Hypothesis Architect | [ ] | [ ] |
| S4 | Evidence Analyst | [ ] | [ ] |
| S5 | Synthesis Director | [ ] | [ ] |

---

#### Pre-Declared Invocation Apparatus (C-38)

All PRE and POST checkpoint tables for all 5 stages are pre-declared below as blank templates.
Stage bodies carry timing directives: "Fill PRE-SN before execution / Fill POST-SN after."

---

### Stage 1 — Intelligence Analyst

**Entry gate:** First stage. No prerequisites. Pass.
SEQUENCING RULE note: This campaign runs Intelligence before Web (S1=Intel, S2=Web).
This ordering is a named SEQUENCING RULE decision declared in the Rule Registry.

---
**Fill PRE-S1 before writing Stage 1 content.**

#### PRE-EXECUTION TABLE — Stage 1 (Intelligence Analyst)

| Rule | Applicable? | Will this rule hold? [S1 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — evidence stage | N/A |
| FALSIFICATION | No — no hypothesis | N/A |
| SEQUENCING | Yes — confirming Intel-first ordering and no hypothesis will appear | [ Yes / No ] |
| PROVENANCE | No — S1 not scope-restricted | N/A |

---
*Stage 1 execution — Intelligence Analyst:*

Draw on internal knowledge and prior research to characterize the evidence landscape for
$ARGUMENTS. Identify known findings, contested areas, established patterns, and knowledge
gaps — without consulting external web sources. Label every claim `[intel]`.
Do not state hypotheses. This is the intelligence pre-characterization stage.

---
**Fill POST-S1 after Stage 1 content is complete.**

#### POST-EXECUTION TABLE — Stage 1 (Intelligence Analyst)

| Rule | Applicable? | Does this rule hold? [S1 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No | N/A confirmed |
| FALSIFICATION | No | N/A confirmed |
| SEQUENCING | Yes — Intel-first confirmed; no hypothesis in output | [ Yes / No ] |
| PROVENANCE | No | N/A confirmed |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Intelligence characterization complete; all claims `[intel]` | [ Pass / Fail ] |
| No web sources consulted | [ Pass / Fail ] |
| No hypothesis stated | [ Pass / Fail ] |

**HANDOFF S1→S2:** Role passes to Stage 2 — Web Evidence Collector.
Transferring: ARTIFACT-S1 (Intelligence Assessment).
Web Evidence Collector authorized reads: ARTIFACT-S1 + external sources.
PROVENANCE RULE: NOT activated — Stage 2 not scope-restricted.

---

### Stage 2 — Web Evidence Collector

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S1 exit gate all-Pass | [ Pass / Fail ] |
| Handoff S1→S2 complete | [ Pass / Fail ] |

---
**Fill PRE-S2 before writing Stage 2 content.**

#### PRE-EXECUTION TABLE — Stage 2 (Web Evidence Collector)

| Rule | Applicable? | Will this rule hold? [S2 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — evidence collection | N/A |
| FALSIFICATION | No — no hypothesis | N/A |
| SEQUENCING | Yes — S2 executes after S1; no hypothesis will appear | [ Yes / No ] |
| PROVENANCE | No — S2 not scope-restricted | N/A |

---
*Stage 2 execution — Web Evidence Collector:*

Conduct structured web research on $ARGUMENTS. Search for: primary sources, recent
publications, technical data, expert commentary, quantitative evidence. Consider ARTIFACT-S1
as the framing context — identify where web evidence confirms, expands, or contradicts the
intelligence characterization. Label every finding `[web]`. Do not state hypotheses.

---
**Fill POST-S2 after Stage 2 content is complete.**

#### POST-EXECUTION TABLE — Stage 2 (Web Evidence Collector)

| Rule | Applicable? | Does this rule hold? [S2 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No | N/A confirmed |
| FALSIFICATION | No | N/A confirmed |
| SEQUENCING | Yes — S2 ran after S1; no hypothesis in output | [ Yes / No ] |
| PROVENANCE | No | N/A confirmed |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 6+ `[web]` labeled findings | [ Pass / Fail ] |
| No hypothesis stated | [ Pass / Fail ] |

**HANDOFF S2→S3:** Role passes to Stage 3 — Hypothesis Architect.
Transferring: ARTIFACT-S1 (Intelligence Assessment), ARTIFACT-S2 (Web Findings Corpus).
Hypothesis Architect authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
**PROVENANCE RULE ACTIVATED.** Obligations for ARTIFACT-S1 and ARTIFACT-S2.
Every Stage 3 claim: `[source: Stage N -- Artifact Name]` N ∈ {1, 2}.

---

### Stage 3 — Hypothesis Architect

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S2 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S2→S3 | [ Pass / Fail ] |

---
**Fill PRE-S3 before writing Stage 3 content.**

#### PRE-EXECUTION TABLE — Stage 3 (Hypothesis Architect)

| Rule | Applicable? | Will this rule hold? [S3 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — hypothesis stage | N/A |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | Yes — S1 and S2 exits confirmed before this stage | [ Yes / No ] |
| PROVENANCE | Yes | [ Yes / No ] |

---
*Stage 3 execution — Hypothesis Architect:*

Declare 3–5 hypotheses grounded in ARTIFACT-S1 and ARTIFACT-S2.
Each: (1) testable claim; (2) prompting evidence cited as
`[source: Stage 1 -- Intelligence Assessment]` or `[source: Stage 2 -- Web Findings Corpus]`;
(3) explicit falsification condition; (4) preliminary confidence (High / Medium / Low).
Label every claim `[hypothesis]`.

---
**Fill POST-S3 after Stage 3 content is complete.**

#### POST-EXECUTION TABLE — Stage 3 (Hypothesis Architect)

| Rule | Applicable? | Does this rule hold? [S3 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No | N/A confirmed |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | Yes | [ Yes / No ] |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 3–5 hypotheses with explicit falsification conditions | [ Pass / Fail ] |
| All claims carry `[hypothesis]` and `[source: Stage N -- Artifact Name]` | [ Pass / Fail ] |

**HANDOFF S3→S4:** Role passes to Stage 4 — Evidence Analyst.
Transferring: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 (Hypothesis Register).
Authorized reads: S1 + S2 + S3 only.
**PROVENANCE RULE ACTIVATED.** Every Stage 4 claim: `[source: Stage N -- Artifact Name]` N ∈ {1,2,3}.

---

### Stage 4 — Evidence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S3 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S3→S4 | [ Pass / Fail ] |

---
**Fill PRE-S4 before writing Stage 4 content.**

#### PRE-EXECUTION TABLE — Stage 4 (Evidence Analyst)

| Rule | Applicable? | Will this rule hold? [S4 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | No — analysis stage | N/A |
| SEQUENCING | No — ordering complete | N/A |
| PROVENANCE | Yes | [ Yes / No ] |

---
*Stage 4 execution — Evidence Analyst:*

Analyze each hypothesis from ARTIFACT-S3 against ARTIFACT-S1 and ARTIFACT-S2.
Assign varied confidence (High / Medium / Low — uniform fails CALIBRATION). Label `[analysis]`.
Attach `[source: Stage N -- Artifact Name]` where N ∈ {1,2,3}.

---
**Fill POST-S4 after Stage 4 content is complete.**

#### POST-EXECUTION TABLE — Stage 4 (Evidence Analyst)

| Rule | Applicable? | Does this rule hold? [S4 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | No | N/A confirmed |
| SEQUENCING | No | N/A confirmed |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| All hypotheses analyzed | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| All claims carry `[analysis]` and provenance tags | [ Pass / Fail ] |

**HANDOFF S4→S5:** Role passes to Stage 5 — Synthesis Director.
Transferring: ARTIFACT-S1 through ARTIFACT-S4.
Authorized reads: S1–S4 only.
**PROVENANCE RULE ACTIVATED.** Every Stage 5 claim: `[source: Stage N -- Artifact Name]` N ∈ {1,2,3,4}.

---

### Stage 5 — Synthesis Director

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S4 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S4→S5 | [ Pass / Fail ] |

---
**Fill PRE-S5 before writing Stage 5 content.**

#### PRE-EXECUTION TABLE — Stage 5 (Synthesis Director)

| Rule | Applicable? | Will this rule hold? [S5 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | No — synthesis stage | N/A |
| PROVENANCE | Yes | [ Yes / No ] |

---
*Stage 5 execution — Synthesis Director:*

Synthesize all evidence into a coherent brief on $ARGUMENTS:
1. Consensus — where Intelligence (S1) and Web (S2) agree; where they add to each other
2. Conflicts — where S1 and S2 diverge; name each conflict explicitly
3. Hypothesis verdicts — Supported / Refuted / Indeterminate with final varied confidence
4. Falsification status — each hypothesis's condition confirmed or rejected
5. Gaps and open questions remaining after the full campaign
6. Decision readiness — one sentence naming posture and specific gap if not ready

Label `[synthesis]`. Attach `[source: Stage N -- Artifact Name]` N ∈ {1,2,3,4}.

---
**Fill POST-S5 after Stage 5 content is complete.**

#### POST-EXECUTION TABLE — Stage 5 (Synthesis Director)

| Rule | Applicable? | Does this rule hold? [S5 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | No | N/A confirmed |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Consensus and conflict explicitly separated | [ Pass / Fail ] |
| All hypotheses carry final status | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| Gaps surfaced | [ Pass / Fail ] |
| Decision readiness in one sentence | [ Pass / Fail ] |

---

## V-05 — Combined: Fixed dual-table format + Inertia framing + C-39 + C-40

**Variation axes:** (1) Fixed output format — the R15 V-05 C-37 failure is corrected: PRE and
POST are physically-separated named table artifacts, not columns in one table.
(2) Inertia framing — the status-quo comparator ("continue with $ARGUMENTS as-is / do nothing")
is named explicitly in the decision readiness verdict AND in the SEQUENCING RULE declaration as
the antipattern the rule excludes. (3) Interrogative column headers (C-39). (4) SEQUENCING RULE
explicitly names evidence-stage ordering as governed (C-40), with inertia framing identifying
"hypothesis-first mode" as the inertia antipattern excluded by the rule.

**Hypothesis:** Naming the inertia antipattern within rule declarations converts governance from
abstract constraints into explicit rejections of named failure modes. An executor reading
"SEQUENCING RULE excludes: (1) hypothesis-first mode, (2) unordered evidence collection" has
a concrete reference for what non-compliance looks like — the rule is not just a prescription
but an exclusion of a named comparator. The decision readiness verdict names the option being
foregone: "Ready to proceed over [inertia: maintain current approach]" is a richer signal than
"Ready to proceed" because it records what was considered and rejected.

---

You are running the full evidence campaign for: **$ARGUMENTS**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable after execution starts.

---

#### Rule Registry (all five rules are peers; no rule is primary)

**ATTRIBUTION RULE** `[invoked at: S1(+), S2(+), S3(+), S4(+), S5(+)]`
Every material claim names its source stage: `[web]` S1, `[intel]` S2,
`[hypothesis]` S3, `[analysis]` S4, `[synthesis]` S5.
Inertia antipattern excluded: undifferentiated prose with no source labels (legacy research mode).

**CALIBRATION RULE** `[invoked at: S4(+), S5(+); S1(-), S2(-), S3(-)]`
Confidence ratings must vary. Uniform ratings = calibration failure.
Anti-uniformity guard: state distribution explicitly. At least two distinct levels required.
Inertia antipattern excluded: confidence uniformity ("all findings are Medium confidence").

**FALSIFICATION RULE** `[invoked at: S3(+), S5(+); S1(-), S2(-), S4(-)]`
Each hypothesis carries an explicit falsification condition.
Final status: Supported / Refuted / Indeterminate.
Inertia antipattern excluded: unfalsifiable claims ("the evidence supports the hypothesis" with
no criterion that would cause rejection).

**SEQUENCING RULE** `[invoked at: S1(+), S2(+), S3(+); S4(-), S5(-)]`
Governs two explicitly-named constraints:
(1) **Hypothesis placement** — evidence stages S1 and S2 complete before hypothesis
    declaration at S3. Rationale: "A hypothesis declared before evidence gathering is an
    anchor masquerading as a prediction."
(2) **Evidence-stage relative ordering** — Web (S1) executes before Intelligence (S2).
    This ordering is a governed SEQUENCING decision. Any reversal requires explicit
    justification at the S1 boundary before S1 output begins.
Inertia antipattern excluded:
(a) **hypothesis-first mode** — state hypotheses, then gather evidence to confirm them
(b) **unordered evidence collection** — gather evidence in whatever order is convenient,
    without declaring the ordering as a governed sequencing choice

**PROVENANCE RULE** `[invoked at: S3(+), S4(+), S5(+); S1(-), S2(-)]`
Activated at handoff boundaries preceding scope-restricted stages.
Every claim in S3–S5 carries `[source: Stage N -- Artifact Name]`.
Inertia antipattern excluded: anonymous synthesis ("the evidence suggests...") with no
artifact-level citation.

Peer declaration: all five rules are equal-tier. Map auto-extends with new rules.

---

#### Role Roster

| Stage | Role Name | Authorized Reads |
|-------|-----------|-----------------|
| S1 | Web Evidence Collector | External sources only. No prior artifacts. |
| S2 | Intelligence Analyst | ARTIFACT-S1 only. |
| S3 | Hypothesis Architect | ARTIFACT-S1 + ARTIFACT-S2 only. |
| S4 | Evidence Analyst | ARTIFACT-S1 + ARTIFACT-S2 + ARTIFACT-S3 only. |
| S5 | Synthesis Director | ARTIFACT-S1 through ARTIFACT-S4 only. |

---

#### Coverage Map (immutable)

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| ATTRIBUTION  | + | + | + | + | + |
| CALIBRATION  | - | - | - | + | + |
| FALSIFICATION| - | - | + | - | + |
| SEQUENCING   | + | + | + | - | - |
| PROVENANCE   | - | - | + | + | + |

Invocation checksum: **40 artifacts** = (15 × 2) + (10 × 1). Derived from map; immutable.

---

#### Gate Record Template

| Stage | Role | Entry | Exit |
|-------|------|:-----:|:----:|
| S1 | Web Evidence Collector | Pass | [ ] |
| S2 | Intelligence Analyst | [ ] | [ ] |
| S3 | Hypothesis Architect | [ ] | [ ] |
| S4 | Evidence Analyst | [ ] | [ ] |
| S5 | Synthesis Director | [ ] | [ ] |

---

#### Pre-Declared Invocation Apparatus (C-38)

All PRE-EXECUTION and POST-EXECUTION checkpoint tables for all 5 stages are pre-declared
below as blank templates. Stage bodies carry timing directives: "Fill NAMED-PRE-SN before
execution; fill NAMED-POST-SN after." Both tables are named and physically separated
by execution content in each stage body — satisfying C-37.

[NAMED-PRE-S1 through NAMED-POST-S5 templates embedded inline in stage bodies below]

---

### Stage 1 — Web Evidence Collector

**Entry gate:** First stage. Pass.

---
**Timing directive: Fill NAMED-PRE-S1 before writing any Stage 1 content.**

#### NAMED-PRE-S1: PRE-EXECUTION COMMITMENT TABLE — Stage 1

| Rule | Applicable? | Will this rule hold? [S1 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — evidence collection | N/A |
| FALSIFICATION | No — no hypothesis | N/A |
| SEQUENCING | Yes — S1 before S2 (evidence ordering); no hypothesis | [ Yes / No ] |
| PROVENANCE | No — not scope-restricted | N/A |

---
*Stage 1 execution — Web Evidence Collector:*

Conduct structured web research on $ARGUMENTS. Label every finding `[web]`.
Do not state hypotheses. Collect at least 6 findings.
The status quo — proceeding with $ARGUMENTS without this investigation — is the inertia
option this campaign exists to evaluate. Gather evidence broadly.

---
**Timing directive: Fill NAMED-POST-S1 after Stage 1 content is complete.**

#### NAMED-POST-S1: POST-EXECUTION VERIFICATION TABLE — Stage 1

| Rule | Applicable? | Does this rule hold? [S1 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No | N/A confirmed |
| FALSIFICATION | No | N/A confirmed |
| SEQUENCING | Yes | [ Yes / No ] |
| PROVENANCE | No | N/A confirmed |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 6+ `[web]` labeled findings | [ Pass / Fail ] |
| No hypothesis stated | [ Pass / Fail ] |

**HANDOFF S1→S2:** Role passes to Stage 2 — Intelligence Analyst.
Transferring: ARTIFACT-S1 (Web Findings Corpus).
Intelligence Analyst authorized reads: ARTIFACT-S1 only.
PROVENANCE RULE: NOT activated — Stage 2 not scope-restricted.

---

### Stage 2 — Intelligence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S1 exit gate all-Pass | [ Pass / Fail ] |
| Handoff S1→S2 complete | [ Pass / Fail ] |

---
**Timing directive: Fill NAMED-PRE-S2 before writing any Stage 2 content.**

#### NAMED-PRE-S2: PRE-EXECUTION COMMITMENT TABLE — Stage 2

| Rule | Applicable? | Will this rule hold? [S2 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — evidence characterization | N/A |
| FALSIFICATION | No — no hypothesis | N/A |
| SEQUENCING | Yes — S2 executes after S1; no hypothesis | [ Yes / No ] |
| PROVENANCE | No — not scope-restricted | N/A |

---
*Stage 2 execution — Intelligence Analyst:*

Apply expert judgment to ARTIFACT-S1. Characterize patterns, contradictions, strength
ratings (well-evidenced / thin / contested), and knowledge gaps.
Label every new claim `[intel]`. Do not state hypotheses.

---
**Timing directive: Fill NAMED-POST-S2 after Stage 2 content is complete.**

#### NAMED-POST-S2: POST-EXECUTION VERIFICATION TABLE — Stage 2

| Rule | Applicable? | Does this rule hold? [S2 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No | N/A confirmed |
| FALSIFICATION | No | N/A confirmed |
| SEQUENCING | Yes | [ Yes / No ] |
| PROVENANCE | No | N/A confirmed |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Evidence landscape characterized | [ Pass / Fail ] |
| No hypothesis in Stage 2 | [ Pass / Fail ] |
| All new claims carry `[intel]` | [ Pass / Fail ] |

**HANDOFF S2→S3:** Role passes to Stage 3 — Hypothesis Architect.
Transferring: ARTIFACT-S1, ARTIFACT-S2 (Intelligence Assessment).
Hypothesis Architect authorized reads: ARTIFACT-S1 + ARTIFACT-S2 only.
**PROVENANCE RULE ACTIVATED.** Obligations for ARTIFACT-S1, ARTIFACT-S2.
Every Stage 3 claim: `[source: Stage N -- Artifact Name]` N ∈ {1, 2}.

---

### Stage 3 — Hypothesis Architect

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S2 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S2→S3 | [ Pass / Fail ] |

---
**Timing directive: Fill NAMED-PRE-S3 before writing any Stage 3 content.**

#### NAMED-PRE-S3: PRE-EXECUTION COMMITMENT TABLE — Stage 3

| Rule | Applicable? | Will this rule hold? [S3 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No — hypothesis stage | N/A |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | Yes — S1 + S2 exits confirmed | [ Yes / No ] |
| PROVENANCE | Yes | [ Yes / No ] |

---
*Stage 3 execution — Hypothesis Architect:*

Declare 3–5 hypotheses grounded in ARTIFACT-S1 and ARTIFACT-S2.
Each: (1) testable claim; (2) `[source: Stage N -- Artifact Name]`; (3) explicit falsification
condition; (4) preliminary confidence (High / Medium / Low).
Label every claim `[hypothesis]`.
Note: hypotheses here replace hypothesis-first mode (the inertia antipattern) — they emerge
from evidence gathered, not from pre-committed assumptions confirmed by collection.

---
**Timing directive: Fill NAMED-POST-S3 after Stage 3 content is complete.**

#### NAMED-POST-S3: POST-EXECUTION VERIFICATION TABLE — Stage 3

| Rule | Applicable? | Does this rule hold? [S3 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | No | N/A confirmed |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | Yes | [ Yes / No ] |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| 3–5 hypotheses with explicit falsification conditions | [ Pass / Fail ] |
| All claims carry `[hypothesis]` and provenance tags | [ Pass / Fail ] |

**HANDOFF S3→S4:** Role passes to Stage 4 — Evidence Analyst.
Transferring: ARTIFACT-S1, ARTIFACT-S2, ARTIFACT-S3 (Hypothesis Register).
Authorized reads: S1 + S2 + S3 only.
**PROVENANCE RULE ACTIVATED.** Every Stage 4 claim: `[source: Stage N -- Artifact Name]` N ∈ {1,2,3}.

---

### Stage 4 — Evidence Analyst

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S3 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S3→S4 | [ Pass / Fail ] |

---
**Timing directive: Fill NAMED-PRE-S4 before writing any Stage 4 content.**

#### NAMED-PRE-S4: PRE-EXECUTION COMMITMENT TABLE — Stage 4

| Rule | Applicable? | Will this rule hold? [S4 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | No — analysis stage | N/A |
| SEQUENCING | No — ordering complete | N/A |
| PROVENANCE | Yes | [ Yes / No ] |

---
*Stage 4 execution — Evidence Analyst:*

Analyze each hypothesis from ARTIFACT-S3 against ARTIFACT-S1 and ARTIFACT-S2.
Assign varied confidence (High / Medium / Low — uniform fails CALIBRATION). Label `[analysis]`.
Attach `[source: Stage N -- Artifact Name]` N ∈ {1,2,3}.

---
**Timing directive: Fill NAMED-POST-S4 after Stage 4 content is complete.**

#### NAMED-POST-S4: POST-EXECUTION VERIFICATION TABLE — Stage 4

| Rule | Applicable? | Does this rule hold? [S4 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | No | N/A confirmed |
| SEQUENCING | No | N/A confirmed |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| All hypotheses analyzed | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| All claims carry `[analysis]` and provenance tags | [ Pass / Fail ] |

**HANDOFF S4→S5:** Role passes to Stage 5 — Synthesis Director.
Transferring: ARTIFACT-S1 through ARTIFACT-S4.
Authorized reads: S1–S4 only.
**PROVENANCE RULE ACTIVATED.** Every Stage 5 claim: `[source: Stage N -- Artifact Name]` N ∈ {1,2,3,4}.

---

### Stage 5 — Synthesis Director

**Entry gate:**

| Condition | Status |
|-----------|--------|
| S4 exit gate all-Pass | [ Pass / Fail ] |
| PROVENANCE activated at S4→S5 | [ Pass / Fail ] |

---
**Timing directive: Fill NAMED-PRE-S5 before writing any Stage 5 content.**

#### NAMED-PRE-S5: PRE-EXECUTION COMMITMENT TABLE — Stage 5

| Rule | Applicable? | Will this rule hold? [S5 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | No — synthesis stage | N/A |
| PROVENANCE | Yes | [ Yes / No ] |

---
*Stage 5 execution — Synthesis Director:*

Synthesize all evidence into a coherent brief on $ARGUMENTS:
1. Consensus — where S1 and S2 agree
2. Conflicts — where S1 and S2 diverge; name each explicitly
3. Hypothesis verdicts — Supported / Refuted / Indeterminate with final varied confidence
4. Falsification status per hypothesis
5. Gaps and open questions remaining after the full campaign
6. Decision readiness — one sentence naming posture and specific gap if not ready.
   Format: "Ready to proceed over [inertia: maintain current approach to $ARGUMENTS]" OR
   "Needs more investigation on [specific gap] before discarding [inertia: maintain current
   approach to $ARGUMENTS]."

Label `[synthesis]`. Attach `[source: Stage N -- Artifact Name]` N ∈ {1,2,3,4}.

---
**Timing directive: Fill NAMED-POST-S5 after Stage 5 content is complete.**

#### NAMED-POST-S5: POST-EXECUTION VERIFICATION TABLE — Stage 5

| Rule | Applicable? | Does this rule hold? [S5 of 5] |
|------|:-----------:|:------------------------------:|
| ATTRIBUTION | Yes | [ Yes / No ] |
| CALIBRATION | Yes | [ Yes / No ] |
| FALSIFICATION | Yes | [ Yes / No ] |
| SEQUENCING | No | N/A confirmed |
| PROVENANCE | Yes | [ Yes / No ] |

---

**Exit gate:**

| Condition | Status |
|-----------|--------|
| Consensus and conflict explicitly separated | [ Pass / Fail ] |
| All hypotheses carry final status | [ Pass / Fail ] |
| Confidence ratings span 2+ distinct levels | [ Pass / Fail ] |
| Gaps surfaced | [ Pass / Fail ] |
| Decision readiness names posture AND names the inertia comparator | [ Pass / Fail ] |

---

## Variation Axis Summary

| Variate | Primary Axis | Secondary Axes | C-39 Mechanism | C-40 Mechanism |
|---------|-------------|----------------|----------------|----------------|
| V-01 | Output format | — | Consolidated PRE/POST tables; "Will/Does this rule hold?" as column header | SEQUENCING RULE declaration adds evidence-stage ordering as explicit governed constraint |
| V-02 | Lifecycle emphasis | — | Consolidated PRE/POST tables with interrogative headers | SEQUENCING split into dual-track (SEQUENCING-HYPO + SEQUENCING-ORDER); independently invocable |
| V-03 | Phrasing register | — | Per-rule mini-tables with rule-specific headers: "Will ATTRIBUTION hold?" / "Does ATTRIBUTION hold?" | SEQUENCING RULE declaration names both governed dimensions; conversational phrasing |
| V-04 | Role sequence (Intel→Web) | Interrogative headers, explicit C-40 scope | Consolidated PRE/POST tables; interrogative headers | SEQUENCING RULE explicitly names Intel→Web as a governed decision; invoked at S1→S2 boundary with evidence-ordering compliance question |
| V-05 | Output format (fixed dual-table) | Inertia framing, C-39, C-40 | Separate NAMED-PRE and NAMED-POST tables with execution content physically between | SEQUENCING RULE names inertia antipatterns: hypothesis-first mode and unordered evidence collection as the excluded patterns |

**C-37 structural property across all 5 variates:** Every variate places execution content
physically between the PRE table artifact and the POST table artifact. V-01/V-04/V-05 use
standard NAMED-PRE / NAMED-POST tables. V-02 uses FORM-PRE / FORM-POST tables with timing
directives. V-03 uses per-rule mini-tables where each mini-table has a PRE row and a POST
row separated by a "*execution between*" marker — the two-row within-mini-table format is the
per-rule analog of the cross-table separation in other variates.

**C-38 structural property across all 5 variates:** All variates pre-declare the invocation
apparatus in the preamble section before Stage 1 executes (blank templates or form references),
AND embed timing directives in each stage body naming the specific form to fill and when.
Both structural components are present in all five variates.

**C-39 implementation spectrum:**
- V-01, V-04, V-05: Consolidated table; generic "Will/Does this rule hold?" header
- V-02: Consolidated table; same header pattern; SEQUENCING split into two named rule-rows
- V-03: Per-rule mini-tables; rule-specific header: "Will ATTRIBUTION hold?" / "Does ATTRIBUTION hold?"
  V-03 is the strongest C-39 implementation — the subject of the question is in the column name.

**C-40 implementation spectrum:**
- V-01, V-03, V-04, V-05: Single SEQUENCING RULE with both governed constraints declared
- V-02: SEQUENCING split into SEQUENCING-HYPO and SEQUENCING-ORDER as peer rule-rows;
  independent coverage-map entries; independently auditable
  V-02 is the strongest C-40 implementation — evidence-stage ordering has its own invocation trail.
