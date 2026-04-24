---
skill: quest-variate
skill_target: campaign-evidence
date: 2026-03-16
round: 7
rubric_version: 7
---

# Variates: campaign-evidence (Round 7)

Five complete, runnable skill body prompts. Single-axis variations first (V-01 through V-03),
combined axes second (V-04 through V-05).

**Baseline requirements for all R7 variates** (C-22, C-23, C-24 are now rubric-required):
- Every rule invocation carries `[ Yes / No ]` binary form (C-22)
- Every rule invocation carries `[Stage N of 5]` index suffix (C-23)
- Every stage carries explicit entry and exit conditions (C-24)

Variations explore what happens *given* these three requirements are in place.

---

## V-01 -- Axis: Lifecycle Emphasis (Gate as First-Class Artifact)

**Variation axis**: Entry and exit conditions are not prose annotations -- they are formal gate
declarations that the executor must fill in as pass/fail before advancing to the next stage.
A failed or blank gate record is structurally visible. The gate record is part of the output,
not just a pre-execution check.

**Hypothesis**: When the gate is an artifact rather than an instruction, the executor must
produce evidence of gate passage. A blank gate record becomes as visible as a missing section.
Compliance is not claimed in prose -- it is present or absent as a filled cell.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable -- cannot be modified after any stage executes.
This is a commitment, not a record.

**SEQUENCING RULE** [invoked at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
A hypothesis anchored before evidence gathering is a bias, not a hypothesis. Evidence stages
(web search, intelligence) run before hypothesis declaration. Hypotheses are derived from
evidence, not confirmed against pre-anchored assumptions.
Rationale: pre-evidence hypotheses function as anchors that distort evidence weighting.

**ATTRIBUTION RULE** [invoked at: Stage 1, Stage 2, Stage 4]
Every material claim names its source stage. Labels: `[web search]` (S1), `[intelligence]`
(S2), `[analysis]` (S4). A claim without a stage label is unattributed.

**CALIBRATION RULE** [invoked at: Stage 4, Stage 5]
Confidence ratings must vary across findings. Uniform confidence across all findings is a
calibration failure. Anti-uniformity check required at every invocation site.

**FALSIFICATION RULE** [invoked at: Stage 3, Stage 5]
Each hypothesis carries one of: Supported / Refuted / Indeterminate. Assigned from evidence
weight, not fit to expectation. Refuted and Indeterminate are first-class outcomes.

Coverage map (immutable from this point):

| Rule | S1: Web | S2: Intel | S3: Hypo | S4: Analysis | S5: Synth |
|------|---------|-----------|----------|--------------|-----------|
| SEQUENCING | checked | checked | checked | checked | checked |
| ATTRIBUTION | checked | checked | -- | checked | -- |
| CALIBRATION | -- | -- | -- | checked | checked |
| FALSIFICATION | -- | -- | checked | -- | checked |

---

### Stage 1 -- prove-websearch

**ENTRY GATE (fill before executing)**:

| Condition | Status |
|-----------|--------|
| No hypothesis has been stated prior to this stage | [ Pass / Fail ] |
| This is the first stage to execute | [ Pass / Fail ] |

> If any entry condition is Fail: stop. Record gate failure. Do not proceed.

---

SEQUENCING RULE [Stage 1 of 5]: Is this stage running before any hypothesis has been stated? [ Yes / No ]
ATTRIBUTION RULE [Stage 1 of 5]: Will every finding carry a `[web search]` label? [ Yes / No ]

Search for evidence on **{{topic}}**: primary sources, recent publications, technical
references, industry reports, quantitative data. Collect broadly -- do not filter for any
anticipated conclusion.

Label every finding: `[web search]`

---

**EXIT GATE (fill before advancing to Stage 2)**:

| Condition | Status |
|-----------|--------|
| Raw evidence corpus assembled (minimum 8 labeled findings) | [ Pass / Fail ] |
| No hypothesis stated anywhere in Stage 1 output | [ Pass / Fail ] |
| Every finding carries `[web search]` label | [ Pass / Fail ] |

> If any exit condition is Fail: complete the condition, then re-verify. Do not advance until all Pass.

SEQUENCING RULE [Stage 1 of 5]: No hypothesis stated in this stage? [ Yes / No ]
ATTRIBUTION RULE [Stage 1 of 5]: Every finding labeled `[web search]`? [ Yes / No ]

---

### Stage 2 -- prove-intelligence

**ENTRY GATE (fill before executing)**:

| Condition | Status |
|-----------|--------|
| Stage 1 exit gate is all-Pass | [ Pass / Fail ] |
| No hypothesis has been stated at any point | [ Pass / Fail ] |

> If any entry condition is Fail: stop. Record gate failure. Do not proceed.

---

SEQUENCING RULE [Stage 2 of 5]: Has hypothesis declaration not yet occurred? [ Yes / No ]
ATTRIBUTION RULE [Stage 2 of 5]: Will every new claim carry an `[intelligence]` label? [ Yes / No ]

Apply expert judgment to the Stage 1 corpus:
- Patterns and contradictions across findings
- Evidence strength characterization (well-evidenced vs. thin)
- Domain-specific considerations the surface search missed
- Knowledge gaps -- what is absent from the evidence record

Label every new claim: `[intelligence]`

---

**EXIT GATE (fill before advancing to Stage 3)**:

| Condition | Status |
|-----------|--------|
| Evidence landscape characterized (patterns, conflicts, gaps named) | [ Pass / Fail ] |
| No hypothesis stated anywhere in Stage 2 output | [ Pass / Fail ] |
| Every new claim carries `[intelligence]` label | [ Pass / Fail ] |

> If any exit condition is Fail: complete the condition, then re-verify. Do not advance until all Pass.

SEQUENCING RULE [Stage 2 of 5]: No hypothesis stated in this stage? [ Yes / No ]
ATTRIBUTION RULE [Stage 2 of 5]: Every new claim labeled `[intelligence]`? [ Yes / No ]

---

### Stage 3 -- prove-hypothesis

**ENTRY GATE (fill before executing)**:

| Condition | Status |
|-----------|--------|
| Stage 1 exit gate is all-Pass | [ Pass / Fail ] |
| Stage 2 exit gate is all-Pass | [ Pass / Fail ] |

> If any entry condition is Fail: stop. Complete the blocking stage first. Do not declare hypotheses.

---

SEQUENCING RULE [Stage 3 of 5]: Were Stages 1 and 2 complete before this stage began? [ Yes / No ]
FALSIFICATION RULE [Stage 3 of 5]: Is each hypothesis stated in a form that evidence could refute? [ Yes / No ]

A hypothesis anchored before evidence gathering is a bias, not a hypothesis. The following
hypotheses are derived from the evidence gathered in Stages 1 and 2.

Declare 3-5 hypotheses. For each:
- State the falsifiable claim
- Cite the specific Stage 1 or Stage 2 evidence that grounds it
- Name what evidence would refute it (the falsification condition)

FALSIFICATION RULE [Stage 3 of 5]: Could counter-evidence exist that would mark any of these Refuted? [ Yes / No ]

---

**EXIT GATE (fill before advancing to Stage 4)**:

| Condition | Status |
|-----------|--------|
| 3-5 hypotheses declared | [ Pass / Fail ] |
| Each hypothesis has a named falsification condition | [ Pass / Fail ] |
| Each hypothesis cites specific Stage 1 or Stage 2 evidence | [ Pass / Fail ] |

> If any exit condition is Fail: complete the condition. Do not advance until all Pass.

---

### Stage 4 -- prove-analysis

**ENTRY GATE (fill before executing)**:

| Condition | Status |
|-----------|--------|
| Stage 3 exit gate is all-Pass | [ Pass / Fail ] |
| Hypothesis register from Stage 3 is available | [ Pass / Fail ] |

> If any entry condition is Fail: stop. Complete Stage 3 first.

---

SEQUENCING RULE [Stage 4 of 5]: Were Stages 1-3 complete before this stage began? [ Yes / No ]
ATTRIBUTION RULE [Stage 4 of 5]: Does every analyzed claim carry a source-stage label? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5]: Do confidence ratings vary across findings -- at least two distinct levels? [ Yes / No ]

For each hypothesis:
- Assess supporting evidence weight (label by source stage)
- Assess challenging evidence weight (label by source stage)
- Assign confidence: High / Medium / Low
- State the specific evidence driving the confidence assignment

Calibration checkpoint: If confidence ratings are uniform across all findings -- recalibrate
explicitly. Uniform confidence is a calibration failure.

CALIBRATION RULE [Stage 4 of 5]: At least one finding at a different confidence level from the others? [ Yes / No ]

---

**EXIT GATE (fill before advancing to Stage 5)**:

| Condition | Status |
|-----------|--------|
| Every hypothesis analyzed (supporting + challenging evidence) | [ Pass / Fail ] |
| Every claim carries a source-stage label | [ Pass / Fail ] |
| At least two distinct confidence levels present | [ Pass / Fail ] |

> If any exit condition is Fail: complete the condition. Do not advance until all Pass.

---

### Stage 5 -- prove-synthesize

**ENTRY GATE (fill before executing)**:

| Condition | Status |
|-----------|--------|
| Stage 4 exit gate is all-Pass | [ Pass / Fail ] |
| Hypothesis register with confidence ratings is available | [ Pass / Fail ] |

> If any entry condition is Fail: stop. Complete Stage 4 first.

---

SEQUENCING RULE [Stage 5 of 5]: Were all four prior stages complete before synthesis began? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5]: Two distinct confidence levels present in the full brief? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5]: Does every declared hypothesis carry a final status? [ Yes / No ]

**Consensus** (Stages 1 and 2 agree):
[findings where web search and intelligence concur]

**Conflict** (Stages 1 and 2 diverge):
[findings where web search and intelligence differ -- name the divergence explicitly]

**Hypothesis Register**:

| H# | Hypothesis | Status | Confidence | Evidence Basis |
|----|------------|--------|------------|----------------|
| H-01 | ... | Supported/Refuted/Indeterminate | High/Med/Low | ... |

**Gaps and Open Questions**:
What remains under-evidenced after this full campaign?

**Decision Readiness** (one sentence):
[Ready to proceed.] or [Needs more investigation on {specific gap} before committing.]

CALIBRATION RULE [Stage 5 of 5]: Non-uniform confidence ratings confirmed? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5]: Every hypothesis carries a status? [ Yes / No ]

---

**EXIT GATE (brief complete)**:

| Condition | Status |
|-----------|--------|
| All five stages produced output | [ Pass / Fail ] |
| All hypothesis Status cells populated | [ Pass / Fail ] |
| Confidence ratings non-uniform | [ Pass / Fail ] |
| Decision readiness expressed in one sentence | [ Pass / Fail ] |

> If any exit condition is Fail: the brief is incomplete. Do not deliver until all Pass.

---

### Output: Evidence Brief

Compile all stage outputs into a single self-contained document. Include: title, topic context,
gate record summary (each gate that was checked), executive summary, hypothesis register with
falsification status, evidence record with attribution, synthesis (consensus and conflict
explicitly separated), gaps list, and the decision readiness sentence.

---

## V-02 -- Axis: Output Format (Invocation Audit Table as Primary Governance Artifact)

**Variation axis**: All rule invocations across all five stages are captured in a running audit
table in addition to appearing inline. The audit table has columns: Rule | Stage | Stage-Index |
Condition | Verdict. A reader verifies C-16 (zero-gap coverage) and C-23 (stage-indexed trail)
by inspecting one table -- row count against the coverage map is arithmetic, not interpretive.

**Hypothesis**: The inline invocations prove real-time compliance; the audit table proves
retrospective completeness. A missing invocation is visible as a missing row -- no parsing of
prose required. The table is the proof; the inline invocations are the work.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1 begins. Immutable -- cannot be modified after any stage executes.

**SEQUENCING RULE** [invoked at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
A hypothesis anchored before evidence gathering is a bias, not a hypothesis. Evidence stages
run first; hypothesis declaration follows. Any reordering of Stages 1-3 violates this rule.
Rationale: pre-evidence hypotheses function as anchors that distort evidence weighting.

**ATTRIBUTION RULE** [invoked at: Stage 1, Stage 2, Stage 4]
Every material claim names its source stage: `[web search]`, `[intelligence]`, `[analysis]`.

**CALIBRATION RULE** [invoked at: Stage 4, Stage 5]
Confidence ratings must vary. Uniform confidence is a calibration failure. Anti-uniformity
check required at every invocation.

**FALSIFICATION RULE** [invoked at: Stage 3, Stage 5]
Each hypothesis carries: Supported / Refuted / Indeterminate. Assigned from evidence weight.

Coverage map (immutable):

| Rule | S1 | S2 | S3 | S4 | S5 | Expected Invocations |
|------|----|----|----|----|----|---------------------|
| SEQUENCING | checked | checked | checked | checked | checked | 5 |
| ATTRIBUTION | checked | checked | -- | checked | -- | 3 |
| CALIBRATION | -- | -- | -- | checked | checked | 2 |
| FALSIFICATION | -- | -- | checked | -- | checked | 2 |
| **Total** | | | | | | **12** |

> The audit table at the close of the brief must contain exactly 12 rows. Any count other
> than 12 indicates a missing or extra invocation.

---

### Running Invocation Audit Table

> Append a row to this table at every rule invocation. Do not batch entries post-hoc.

| # | Rule | Stage | Stage-Index | Condition Checked | Verdict |
|---|------|-------|-------------|------------------|---------|
| (rows added inline as campaign executes) | | | | | |

---

### Stage 1 -- prove-websearch

**Entry condition**: No hypothesis stated. This is the first stage.
**Exit condition**: Evidence corpus assembled; no hypothesis stated; all findings labeled `[web search]`.

SEQUENCING RULE [Stage 1 of 5]: Running before any hypothesis stated? [ Yes / No ]
> Append row: SEQUENCING | S1 | 1 of 5 | Running before hypothesis? | [Yes/No]

ATTRIBUTION RULE [Stage 1 of 5]: Every finding will carry `[web search]`? [ Yes / No ]
> Append row: ATTRIBUTION | S1 | 1 of 5 | Findings labeled [web search]? | [Yes/No]

Search **{{topic}}**: primary sources, recent publications, technical references, industry
reports. Label every finding `[web search]`. Collect indiscriminately.

---

### Stage 2 -- prove-intelligence

**Entry condition**: Stage 1 exit condition met. No hypothesis stated.
**Exit condition**: Evidence interpreted; patterns/conflicts/gaps named; no hypothesis stated; all new claims labeled `[intelligence]`.

SEQUENCING RULE [Stage 2 of 5]: Hypothesis declaration not yet occurred? [ Yes / No ]
> Append row: SEQUENCING | S2 | 2 of 5 | No hypothesis yet? | [Yes/No]

ATTRIBUTION RULE [Stage 2 of 5]: Every new claim will carry `[intelligence]`? [ Yes / No ]
> Append row: ATTRIBUTION | S2 | 2 of 5 | New claims labeled [intelligence]? | [Yes/No]

Apply expert judgment to Stage 1 corpus: patterns, contradictions, evidence strength,
domain-specific considerations, knowledge gaps. Label every new claim `[intelligence]`.

---

### Stage 3 -- prove-hypothesis

**Entry condition**: Stages 1 and 2 exit conditions met.
**Exit condition**: 3-5 falsifiable hypotheses declared, each grounded in Stage 1/2 evidence with explicit falsification condition.

SEQUENCING RULE [Stage 3 of 5]: Were Stages 1 and 2 complete before this began? [ Yes / No ]
> Append row: SEQUENCING | S3 | 3 of 5 | S1 and S2 complete? | [Yes/No]

FALSIFICATION RULE [Stage 3 of 5]: Each hypothesis stated in falsifiable form? [ Yes / No ]
> Append row: FALSIFICATION | S3 | 3 of 5 | Hypotheses falsifiable? | [Yes/No]

A hypothesis anchored before evidence is a bias, not a hypothesis. These are derived from
Stages 1 and 2. Declare 3-5 with: claim, grounding evidence, falsification condition.

FALSIFICATION RULE [Stage 3 of 5]: Counter-evidence exists that could refute these? [ Yes / No ]
> Append row: FALSIFICATION | S3 | 3 of 5 | Refutation possible? | [Yes/No]

---

### Stage 4 -- prove-analysis

**Entry condition**: Stage 3 exit condition met. Hypothesis register available.
**Exit condition**: All hypotheses analyzed; all claims source-labeled; at least two distinct confidence levels present.

SEQUENCING RULE [Stage 4 of 5]: Stages 1-3 complete before this began? [ Yes / No ]
> Append row: SEQUENCING | S4 | 4 of 5 | S1-S3 complete? | [Yes/No]

ATTRIBUTION RULE [Stage 4 of 5]: Every analyzed claim carries source-stage label? [ Yes / No ]
> Append row: ATTRIBUTION | S4 | 4 of 5 | Claims source-labeled? | [Yes/No]

CALIBRATION RULE [Stage 4 of 5]: Confidence ratings vary -- at least two distinct levels? [ Yes / No ]
> Append row: CALIBRATION | S4 | 4 of 5 | Two distinct confidence levels present? | [Yes/No]

For each hypothesis: supporting evidence weight, challenging evidence weight (both labeled by
source stage), confidence (High/Med/Low), explicit basis.

CALIBRATION RULE [Stage 4 of 5]: At least one finding at different confidence from others? [ Yes / No ]
> Append row: CALIBRATION | S4 | 4 of 5 | Non-uniform at mid-stage? | [Yes/No]

---

### Stage 5 -- prove-synthesize

**Entry condition**: Stage 4 exit condition met. Full evidence corpus with confidence ratings available.
**Exit condition**: Synthesis complete; all hypothesis statuses assigned; decision readiness in one sentence.

SEQUENCING RULE [Stage 5 of 5]: All four prior stages complete before synthesis? [ Yes / No ]
> Append row: SEQUENCING | S5 | 5 of 5 | S1-S4 complete? | [Yes/No]

CALIBRATION RULE [Stage 5 of 5]: Two distinct confidence levels in full brief? [ Yes / No ]
> Append row: CALIBRATION | S5 | 5 of 5 | Non-uniform confidence in full brief? | [Yes/No]

FALSIFICATION RULE [Stage 5 of 5]: Every hypothesis has a final status? [ Yes / No ]
> Append row: FALSIFICATION | S5 | 5 of 5 | All hypotheses have status? | [Yes/No]

**Consensus** (Stages 1 and 2 agree): [where web search and intelligence concur]
**Conflict** (Stages 1 and 2 diverge): [where they differ -- name the divergence]

**Hypothesis Register**:

| H# | Hypothesis | Status | Confidence | Evidence Basis |
|----|------------|--------|------------|----------------|
| H-01 | ... | Supported/Refuted/Indeterminate | High/Med/Low | ... |

**Gaps and Open Questions**: What remains under-evidenced?

**Decision Readiness** (one sentence):
[Ready to proceed.] or [Needs more investigation on {specific gap} before committing.]

CALIBRATION RULE [Stage 5 of 5]: Non-uniform confidence confirmed for full brief? [ Yes / No ]
> Append row: CALIBRATION | S5 | 5 of 5 | Final non-uniform check | [Yes/No]

FALSIFICATION RULE [Stage 5 of 5]: All hypothesis Status cells populated? [ Yes / No ]
> Append row: FALSIFICATION | S5 | 5 of 5 | All statuses assigned? | [Yes/No]

---

### Final Audit Table Verification

> Count rows in the audit table. Expected: 12.
> If count != 12: identify which coverage-map cell is missing and add the invocation.

| Expected Row Count | Actual Row Count | Delta | Action |
|--------------------|-----------------|-------|--------|
| 12 | [count] | [delta] | [Pass / Reconcile] |

---

### Output: Evidence Brief

Compile all stage outputs into a single self-contained document with: title, topic context,
executive summary, hypothesis register with falsification status, evidence record with
attribution, synthesis section (consensus and conflict explicitly separated), gaps list,
decision readiness sentence, and the completed 12-row invocation audit table.

---

## V-03 -- Axis: Phrasing Register (Minimal-Token Binary -- Maximum Governance, Minimum Overhead)

**Variation axis**: Rule invocations are stripped to their minimal verifiable form. Each
invocation is one line: `RULE [Stage N of 5]: [condition]? [ Yes / No ]`. No surrounding
prose, no explanation, no restatement. The executor fills the binary and advances. All
governance is present; cognitive overhead is near zero.

**Hypothesis**: Maximum invocation compressibility makes compliance frictionless. If the full
governance act can be expressed in one line, the cost of compliance approaches zero. High
invocation overhead causes executors to batch invocations or skip them; low overhead removes
the incentive to cut corners.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Immutable. Declared before Stage 1. Cannot be modified after any stage executes.

**SEQUENCING RULE** [S1, S2, S3, S4, S5]: Evidence before hypotheses. Pre-evidence hypotheses are anchors. Rationale: anchoring distorts evidence weighting; evidence-first eliminates it.
**ATTRIBUTION RULE** [S1, S2, S4]: Every claim labeled by source stage.
**CALIBRATION RULE** [S4, S5]: Confidence varies. Uniform confidence = calibration failure.
**FALSIFICATION RULE** [S3, S5]: Each hypothesis: Supported / Refuted / Indeterminate.

Coverage (immutable):

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| SEQUENCING | x | x | x | x | x |
| ATTRIBUTION | x | x | -- | x | -- |
| CALIBRATION | -- | -- | -- | x | x |
| FALSIFICATION | -- | -- | x | -- | x |

---

### Stage 1 -- prove-websearch

Entry: No hypothesis stated. First stage.
Exit: Evidence corpus assembled. No hypothesis stated. All findings labeled `[web search]`.

SEQUENCING RULE [Stage 1 of 5]: Running before any hypothesis stated? [ Yes / No ]
ATTRIBUTION RULE [Stage 1 of 5]: Every finding labeled `[web search]`? [ Yes / No ]

Gather evidence on **{{topic}}**: primary sources, publications, technical data, reports.
Label every finding `[web search]`. Do not filter.

SEQUENCING RULE [Stage 1 of 5]: No hypothesis appeared in this stage? [ Yes / No ]
ATTRIBUTION RULE [Stage 1 of 5]: All findings carry source label? [ Yes / No ]

---

### Stage 2 -- prove-intelligence

Entry: Stage 1 exit met. No hypothesis stated.
Exit: Evidence interpreted. Patterns, conflicts, gaps named. No hypothesis stated. All claims labeled `[intelligence]`.

SEQUENCING RULE [Stage 2 of 5]: No hypothesis yet? [ Yes / No ]
ATTRIBUTION RULE [Stage 2 of 5]: New claims labeled `[intelligence]`? [ Yes / No ]

Expert interpretation of Stage 1 corpus: patterns, contradictions, strength characterization,
domain considerations, knowledge gaps. Label every new claim `[intelligence]`.

SEQUENCING RULE [Stage 2 of 5]: No hypothesis in Stage 2 output? [ Yes / No ]
ATTRIBUTION RULE [Stage 2 of 5]: All new claims carry `[intelligence]`? [ Yes / No ]

---

### Stage 3 -- prove-hypothesis

Entry: Stages 1-2 exit met.
Exit: 3-5 falsifiable hypotheses. Each grounded in S1/S2. Each has falsification condition.

SEQUENCING RULE [Stage 3 of 5]: S1 and S2 complete before this stage? [ Yes / No ]
FALSIFICATION RULE [Stage 3 of 5]: Each hypothesis falsifiable? [ Yes / No ]

Derive 3-5 hypotheses from Stages 1-2 evidence. For each: claim | grounding | falsification condition.
A hypothesis anchored before evidence is a bias, not a hypothesis.

FALSIFICATION RULE [Stage 3 of 5]: Refuting evidence could exist for each? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5]: All hypotheses grounded in Stages 1-2 evidence? [ Yes / No ]

---

### Stage 4 -- prove-analysis

Entry: Stage 3 exit met. Hypothesis register available.
Exit: All hypotheses analyzed. All claims source-labeled. At least two confidence levels present.

SEQUENCING RULE [Stage 4 of 5]: S1-S3 complete? [ Yes / No ]
ATTRIBUTION RULE [Stage 4 of 5]: Analyzed claims will carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5]: At least two distinct confidence levels? [ Yes / No ]

For each hypothesis: supporting evidence | challenging evidence | confidence (H/M/L) | basis.
Label all evidence by source stage.

CALIBRATION RULE [Stage 4 of 5]: At least one finding at different confidence? [ Yes / No ]
ATTRIBUTION RULE [Stage 4 of 5]: All claims carry source-stage labels? [ Yes / No ]
SEQUENCING RULE [Stage 4 of 5]: No new hypotheses introduced at this stage? [ Yes / No ]

---

### Stage 5 -- prove-synthesize

Entry: Stage 4 exit met. Full evidence with confidence ratings available.
Exit: Synthesis complete. All hypothesis statuses assigned. Decision readiness one sentence.

SEQUENCING RULE [Stage 5 of 5]: S1-S4 complete? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5]: Two distinct confidence levels in full brief? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5]: Every hypothesis has a final status? [ Yes / No ]

**Consensus**: [where S1 and S2 agree]
**Conflict**: [where S1 and S2 diverge -- name the divergence]

**Hypothesis Register**:

| H# | Hypothesis | Status | Confidence | Evidence |
|----|------------|--------|------------|----------|
| H-01 | ... | S/R/I | H/M/L | ... |

**Gaps**: [what remains under-evidenced]

**Decision Readiness** (one sentence): [Ready.] or [Needs {gap}.]

CALIBRATION RULE [Stage 5 of 5]: Confidence non-uniform across full brief? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5]: All hypothesis Status cells filled? [ Yes / No ]
SEQUENCING RULE [Stage 5 of 5]: S1-S4 all contributed to this synthesis? [ Yes / No ]

---

### Output: Evidence Brief

Single self-contained document. Rule invocation markers remain visible. A reader verifies
compliance by scanning for `[ Yes / No ]` tokens -- any `[ No ]` is a flagged failure.

---

## V-04 -- Combined: Lifecycle Emphasis + Inertia Framing

**Variation axes**:
- **Lifecycle emphasis**: Stage gates are verifiable conditions that advance or block; a failed
  gate record is structurally visible and propagates to downstream stages
- **Inertia framing**: The campaign initializes at posture "do not proceed." Only evidence that
  clears an explicit threshold shifts the posture. The status-quo option is named and as
  well-specified as the action option

**Hypothesis**: Gate propagation forces upstream completion before downstream execution;
inertia framing prevents premature commitment by requiring evidence to win, not merely to exist.
Together, they eliminate two failure modes: silent stage skipping and optimism bias.

---

You are running the full evidence campaign for: **{{topic}}**

**Initial posture: Do not proceed.**

Evidence must affirmatively shift this posture to "proceed." Evidence that fails to clear the
threshold confirms the status quo -- which is also a valid, actionable outcome. A brief that
returns "status quo holds" is not a failure; it is honest signal.

### GOVERNANCE PREAMBLE

Finalized before Stage 1. Immutable -- cannot be modified after any stage executes.

**SEQUENCING RULE** [invoked at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
Evidence stages run before hypothesis declaration. A hypothesis anchored before evidence is an
anchor, not a hypothesis. Rationale: pre-committed hypotheses distort evidence weighting.

**ATTRIBUTION RULE** [invoked at: Stage 1, Stage 2, Stage 4]
Every material claim names its source stage: `[web search]`, `[intelligence]`, `[analysis]`.

**CALIBRATION RULE** [invoked at: Stage 4, Stage 5]
Confidence ratings must vary. Uniform confidence is a calibration failure. Anti-uniformity
check mandatory at every invocation.

**FALSIFICATION RULE** [invoked at: Stage 3, Stage 5]
Each hypothesis: Supported / Refuted / Indeterminate. "Refuted" is a first-class outcome --
a campaign where every hypothesis is Supported has likely failed to falsify.

**INERTIA RULE** [invoked at: Stage 5]
Default posture is "do not proceed." Evidence must clear a stated threshold to shift it.
If evidence does not clear the threshold, the brief returns "status quo holds." The status quo
is a competitor, not a fallback.

Coverage map (immutable):

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| SEQUENCING | x | x | x | x | x |
| ATTRIBUTION | x | x | -- | x | -- |
| CALIBRATION | -- | -- | -- | x | x |
| FALSIFICATION | -- | -- | x | -- | x |
| INERTIA | -- | -- | -- | -- | x |

---

### Stage 1 -- prove-websearch

**Entry condition**: No hypothesis stated. This is Stage 1. | Verify: [ Pass / Fail ]
> Fail = stop. Do not execute Stage 1 until entry condition is met.

SEQUENCING RULE [Stage 1 of 5]: Running before any hypothesis stated? [ Yes / No ]
ATTRIBUTION RULE [Stage 1 of 5]: Every finding will carry `[web search]`? [ Yes / No ]

Search **{{topic}}** for primary sources, recent publications, technical references, industry
reports, quantitative data. Collect indiscriminately. Label every finding `[web search]`.

SEQUENCING RULE [Stage 1 of 5]: No hypothesis appeared in Stage 1 output? [ Yes / No ]
ATTRIBUTION RULE [Stage 1 of 5]: All findings carry `[web search]`? [ Yes / No ]

**Exit condition**: Evidence corpus assembled (8+ findings, all labeled). No hypothesis stated.
Verify: [ Pass / Fail ]
> Fail = do not advance to Stage 2. Complete condition. Verify again.

---

### Stage 2 -- prove-intelligence

**Entry condition**: Stage 1 exit is Pass. No hypothesis stated. | Verify: [ Pass / Fail ]
> Fail = Stage 1 exit condition not met. Return to Stage 1.

SEQUENCING RULE [Stage 2 of 5]: No hypothesis declared at any point? [ Yes / No ]
ATTRIBUTION RULE [Stage 2 of 5]: New claims will carry `[intelligence]`? [ Yes / No ]

Interpret Stage 1 corpus through expert judgment: patterns, contradictions, evidence strength,
domain considerations, knowledge gaps. Note which gaps are material to the action threshold --
these will matter at Stage 5 posture assessment.

Label every new claim `[intelligence]`.

SEQUENCING RULE [Stage 2 of 5]: Stage 2 output contains no hypothesis? [ Yes / No ]
ATTRIBUTION RULE [Stage 2 of 5]: All new claims carry `[intelligence]`? [ Yes / No ]

**Exit condition**: Evidence interpreted. Patterns/conflicts/gaps named. No hypothesis. All labeled.
Verify: [ Pass / Fail ]
> Fail = complete condition. Do not advance until Pass.

---

### Stage 3 -- prove-hypothesis

**Entry condition**: Stages 1 and 2 exit are both Pass. | Verify: [ Pass / Fail ]
> Fail = identify which prior exit failed. Return to that stage.

SEQUENCING RULE [Stage 3 of 5]: S1 and S2 both complete before this stage? [ Yes / No ]
FALSIFICATION RULE [Stage 3 of 5]: Each hypothesis stated in falsifiable form? [ Yes / No ]

A hypothesis anchored before evidence is a bias, not a hypothesis. These are derived from
Stages 1 and 2. Declare 3-5 hypotheses, each with:
- Falsifiable claim
- Grounding evidence from Stage 1 or Stage 2 (cite specifically)
- Falsification condition (what would refute this)

Note: the action threshold (Stage 5) requires hypotheses to survive falsification. Hypotheses
that are indeterminate or refuted will weigh against shifting from the initial posture.

FALSIFICATION RULE [Stage 3 of 5]: Counter-evidence could refute each hypothesis? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5]: All hypotheses grounded in S1-S2 evidence only? [ Yes / No ]

**Exit condition**: 3-5 hypotheses declared, each falsifiable with grounding and falsification condition.
Verify: [ Pass / Fail ]

---

### Stage 4 -- prove-analysis

**Entry condition**: Stage 3 exit is Pass. Hypothesis register available. | Verify: [ Pass / Fail ]
> Fail = Stage 3 exit not met. Return to Stage 3.

SEQUENCING RULE [Stage 4 of 5]: S1-S3 complete? [ Yes / No ]
ATTRIBUTION RULE [Stage 4 of 5]: Analyzed claims carry source-stage labels? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5]: Confidence ratings will vary across findings? [ Yes / No ]

For each hypothesis: weigh supporting and challenging evidence (source-labeled). Assign
confidence (High / Medium / Low) with explicit basis. Where evidence is thin (per Stage 2
gaps), confidence will be Low -- this is honest signal, not weakness.

Note: Low-confidence findings do not auto-refute the action case, but they strengthen the
"needs more investigation" posture at Stage 5.

CALIBRATION RULE [Stage 4 of 5]: At least two distinct confidence levels present? [ Yes / No ]
ATTRIBUTION RULE [Stage 4 of 5]: All claims carry source-stage labels? [ Yes / No ]
SEQUENCING RULE [Stage 4 of 5]: No new hypotheses introduced at Stage 4? [ Yes / No ]

**Exit condition**: All hypotheses analyzed. All claims labeled. At least two confidence levels.
Verify: [ Pass / Fail ]

---

### Stage 5 -- prove-synthesize

**Entry condition**: Stage 4 exit is Pass. Full evidence with confidence ratings available. | Verify: [ Pass / Fail ]
> Fail = Stage 4 exit not met. Return to Stage 4.

SEQUENCING RULE [Stage 5 of 5]: S1-S4 all complete? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5]: Two distinct confidence levels in full brief? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5]: Every hypothesis has a final status? [ Yes / No ]
INERTIA RULE [Stage 5 of 5]: Is evidence evaluated against an explicit action threshold? [ Yes / No ]

**Consensus** (Stages 1 and 2 agree): [where web search and intelligence concur]
**Conflict** (Stages 1 and 2 diverge): [where they differ -- name the divergence explicitly]

**Hypothesis Register**:

| H# | Hypothesis | Status | Confidence | Evidence Basis |
|----|------------|--------|------------|----------------|
| H-01 | ... | Supported/Refuted/Indeterminate | High/Med/Low | ... |

**Gaps and Open Questions**: What remains under-evidenced?

**Posture Assessment**:
- Status quo option: [describe what "do not proceed" means for {{topic}}]
- Action threshold: [state what evidence level would justify proceeding]
- Evidence against threshold: [does the evidence clear the threshold?]

INERTIA RULE [Stage 5 of 5]: Does evidence clear the action threshold? [ Yes / No ]

**Decision Readiness** (one sentence):
[Ready to proceed.] or [Status quo holds -- needs {specific gap} before threshold is met.]

CALIBRATION RULE [Stage 5 of 5]: Non-uniform confidence ratings confirmed? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5]: Every hypothesis has a status? [ Yes / No ]
SEQUENCING RULE [Stage 5 of 5]: All five stages contributed to this synthesis? [ Yes / No ]

**Exit condition**: Synthesis complete. All statuses assigned. Decision readiness one sentence. Posture stated.
Verify: [ Pass / Fail ]

---

### Output: Evidence Brief

Single self-contained document. The "status quo holds" outcome is as valid and well-documented
as "ready to proceed." Include: title, topic context, initial posture declaration, gate record
(each stage's entry/exit verification), executive summary, hypothesis register, evidence record,
synthesis (consensus and conflict), posture assessment, gaps, and decision readiness sentence.

---

## V-05 -- Combined: Output Format + Role Sequence (Evidence Matrix + Sequence as Structural Proof)

**Variation axes**:
- **Output format**: The brief's core artifact is a tabular evidence matrix where rows are
  claims and columns include Stage, Confidence, H# association, and Verdict. Governance
  compliance is verifiable by inspecting column values -- a blank cell is an anomaly, not a
  prose gap
- **Role sequence**: The evidence-first sequence is encoded structurally in the matrix itself:
  Stage column values S1 and S2 appear before any S3-derived hypothesis rows. Sequence
  violation is visible as an out-of-order Stage column value -- detectable by sort, not by
  reading

**Hypothesis**: Structural proof of sequencing is stronger than narrative proof. If the
evidence matrix is built in stage order and the hypothesis table references only S1/S2 rows,
sequence compliance is verifiable by inspection rather than by reading every line.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1. Immutable after any stage executes.

**SEQUENCING RULE** [invoked at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
Evidence stages before hypothesis declaration. A hypothesis before evidence is a bias, not a
hypothesis. Structural proof: the matrix must show S1 and S2 rows before any hypothesis-linked
S4 rows. Rationale: pre-evidence hypotheses distort evidence weighting.

**ATTRIBUTION RULE** [invoked at: Stage 1, Stage 2, Stage 4]
Every evidence row carries a Stage column value: `S1:Web`, `S2:Intel`, or `S4:Analysis`.
A row with a blank Stage column is unattributed and fails the rule.

**CALIBRATION RULE** [invoked at: Stage 4, Stage 5]
The Confidence column must contain varied values. If every row shows the same confidence
rating, the column fails calibration. Anti-uniformity check: scan the Confidence column --
if all values are identical, recalibrate before proceeding.

**FALSIFICATION RULE** [invoked at: Stage 3, Stage 5]
Each hypothesis row in the hypothesis table carries a Status column value:
Supported / Refuted / Indeterminate. A blank Status cell fails the rule.

Coverage map (immutable):

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| SEQUENCING | x | x | x | x | x |
| ATTRIBUTION | x | x | -- | x | -- |
| CALIBRATION | -- | -- | -- | x | x |
| FALSIFICATION | -- | -- | x | -- | x |

---

### Evidence Matrix (build incrementally across all stages)

> Add rows at each stage. Never retroactively insert rows out of sequence.
> The Stage column order in this table is the structural proof of SEQUENCING compliance.

| Row# | Claim | Source Ref | Stage | Confidence | H# | Notes |
|------|-------|-----------|-------|------------|----|-------|
| (rows added per stage below) | | | | | | |

---

### Hypothesis Table (populated at Stage 3; status assigned at Stage 5)

| H# | Hypothesis | Grounded In (Row#s) | Falsification Condition | Status | Final Confidence |
|----|------------|---------------------|------------------------|--------|-----------------|
| (populated at Stage 3) | | | | | |

---

### Stage 1 -- prove-websearch

**Entry condition**: Evidence matrix is empty. No hypothesis table rows exist.
**Exit condition**: At least 8 evidence rows with Stage = `S1:Web`. No hypothesis table rows.

SEQUENCING RULE [Stage 1 of 5]: Matrix is empty; this is the first stage? [ Yes / No ]
ATTRIBUTION RULE [Stage 1 of 5]: All rows being added will have Stage = `S1:Web`? [ Yes / No ]

Gather evidence on **{{topic}}**: primary sources, recent publications, technical references,
industry reports. Add each finding as a row to the Evidence Matrix with Stage = `S1:Web`.
Leave Confidence and H# blank (not applicable at this stage).

SEQUENCING RULE [Stage 1 of 5]: No hypothesis table rows were created in Stage 1? [ Yes / No ]
ATTRIBUTION RULE [Stage 1 of 5]: All Stage 1 rows have Stage column = `S1:Web`? [ Yes / No ]

---

### Stage 2 -- prove-intelligence

**Entry condition**: Stage 1 exit met. Matrix contains S1:Web rows only. No hypothesis rows.
**Exit condition**: New S2:Intel rows added for all expert interpretations. No hypothesis rows.

SEQUENCING RULE [Stage 2 of 5]: Matrix contains only S1:Web rows at start of this stage? [ Yes / No ]
ATTRIBUTION RULE [Stage 2 of 5]: All new rows being added will have Stage = `S2:Intel`? [ Yes / No ]

Apply expert interpretation to Stage 1 rows: patterns, contradictions, strength assessment,
domain considerations, knowledge gaps. Add each interpretation as a new Evidence Matrix row
with Stage = `S2:Intel`. Reference the Row# of the Stage 1 finding being interpreted in Notes.

SEQUENCING RULE [Stage 2 of 5]: No hypothesis table rows created in Stage 2? [ Yes / No ]
ATTRIBUTION RULE [Stage 2 of 5]: All Stage 2 rows have Stage column = `S2:Intel`? [ Yes / No ]

---

### Stage 3 -- prove-hypothesis

**Entry condition**: Stage 2 exit met. Matrix contains S1 and S2 rows only. Hypothesis table is empty.
**Exit condition**: 3-5 hypothesis table rows with Grounded In referencing only S1/S2 matrix Row#s.

SEQUENCING RULE [Stage 3 of 5]: Hypothesis table was empty before this stage began? [ Yes / No ]
FALSIFICATION RULE [Stage 3 of 5]: Each hypothesis is stated in falsifiable form? [ Yes / No ]

A hypothesis anchored before evidence is a bias, not a hypothesis. Populate the Hypothesis
Table. For each hypothesis:
- State a falsifiable claim
- Cite specific Evidence Matrix Row#s from S1:Web or S2:Intel as grounding
- Name the falsification condition

Note: Grounded In must reference only S1 or S2 rows -- any S4 row reference would indicate
hypothesis formation after analysis, which violates the evidence-first sequence.

FALSIFICATION RULE [Stage 3 of 5]: Counter-evidence could mark each hypothesis Refuted? [ Yes / No ]
SEQUENCING RULE [Stage 3 of 5]: All Grounded In references point to S1 or S2 rows only? [ Yes / No ]

---

### Stage 4 -- prove-analysis

**Entry condition**: Stage 3 exit met. Hypothesis table has 3-5 rows. Matrix has S1 and S2 rows.
**Exit condition**: New S4:Analysis rows added. All hypothesis H# values referenced. Confidence column non-uniform.

SEQUENCING RULE [Stage 4 of 5]: S1-S3 complete before this stage? [ Yes / No ]
ATTRIBUTION RULE [Stage 4 of 5]: New rows being added will have Stage = `S4:Analysis`? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5]: Confidence column will show at least two distinct values? [ Yes / No ]

Add analysis rows to the Evidence Matrix with Stage = `S4:Analysis`. For each hypothesis:
- Add supporting evidence rows (with H# = hypothesis being analyzed, Confidence assigned)
- Add challenging evidence rows (with same H# notation)
- State the confidence basis in Notes

Calibration check: scan the Confidence column -- if all values are identical, recalibrate now.

CALIBRATION RULE [Stage 4 of 5]: Confidence column contains at least two distinct values? [ Yes / No ]
ATTRIBUTION RULE [Stage 4 of 5]: All Stage 4 rows have Stage column = `S4:Analysis`? [ Yes / No ]
SEQUENCING RULE [Stage 4 of 5]: No new hypothesis rows created at Stage 4? [ Yes / No ]

---

### Stage 5 -- prove-synthesize

**Entry condition**: Stage 4 exit met. Evidence Matrix has S1, S2, and S4 rows. Hypothesis table has 3-5 rows with empty Status.
**Exit condition**: All hypothesis Status and Final Confidence cells populated. Decision readiness one sentence.

SEQUENCING RULE [Stage 5 of 5]: Evidence Matrix contains S1, S2, and S4 rows in that order? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5]: Confidence column non-uniform across full matrix? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5]: Every Hypothesis Table Status cell will be populated? [ Yes / No ]

Assign final status and confidence to each hypothesis row in the Hypothesis Table.

**Consensus** (rows where S1:Web and S2:Intel agree):
[cite matching Evidence Matrix Row#s]

**Conflict** (rows where S1:Web and S2:Intel diverge):
[cite conflicting Row#s and name the divergence explicitly]

**Gaps**: What Evidence Matrix cells would need to exist for a complete picture?

**Sequence verification**: Sort the Evidence Matrix by Stage column. The sort order should be:
S1:Web rows first, S2:Intel rows second, S4:Analysis rows last. Any deviation indicates a
sequence violation.

**Decision Readiness** (one sentence):
[Ready to proceed.] or [Needs more investigation on {gap} -- {N} claims remain Low confidence.]

CALIBRATION RULE [Stage 5 of 5]: Confidence column non-uniform in final matrix? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5]: All Hypothesis Table Status cells populated? [ Yes / No ]
SEQUENCING RULE [Stage 5 of 5]: Matrix Stage column sort order is S1 -> S2 -> S4? [ Yes / No ]

---

### Output: Evidence Brief

The complete brief is: the assembled Evidence Matrix + Hypothesis Table + synthesis section.
Governance compliance is verifiable by column inspection:
- Stage column populated in every row (ATTRIBUTION)
- Confidence column non-uniform (CALIBRATION)
- Status column populated in all hypothesis rows (FALSIFICATION)
- Stage column sort order S1 -> S2 -> S4, hypothesis Grounded In references S1/S2 only (SEQUENCING)

A reader need not read the full prose to audit governance -- they inspect four columns.
