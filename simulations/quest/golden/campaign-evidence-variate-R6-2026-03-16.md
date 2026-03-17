---
skill: quest-variate
skill_target: campaign-evidence
date: 2026-03-16
round: 6
rubric_version: 6
---

# Variates: campaign-evidence (Round 6)

Five complete, runnable skill body prompts. Single-axis variations first (V-01 through V-03), combined axes second (V-04 through V-05).

---

## V-01 -- Axis: Phrasing Register (Interrogative/Verification-First)

**Variation axis**: Every governance rule invocation uses an interrogative form -- a verification question rather than a passive tag. The executor cannot close any stage without answering a binary question.

**Hypothesis**: Interrogative invocation eliminates the gap between "rule was remembered" and "rule was applied." A passive tag can be added without engaging with the rule's requirement; a question cannot be closed without an answer.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

This map is finalized before Stage 1 begins and cannot be modified after any stage executes. Modification after execution begins is prohibited. This is a commitment, not a record.

**SEQUENCING RULE** [invoked at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
A hypothesis anchored before evidence gathering is a bias, not a hypothesis. Evidence stages (web search, intelligence) run before hypothesis declaration. Hypotheses are derived from evidence; they are not confirmed against pre-anchored assumptions.

**ATTRIBUTION RULE** [invoked at: Stage 1, Stage 2, Stage 4]
Every material claim names its source stage. Label: `[web search]`, `[intelligence]`, or `[analysis]`.

**CALIBRATION RULE** [invoked at: Stage 4, Stage 5]
Confidence ratings must vary across findings. If every finding carries the same confidence level, calibration has failed regardless of the level chosen.

**FALSIFICATION RULE** [invoked at: Stage 3, Stage 5]
Each hypothesis carries one status: Supported / Refuted / Indeterminate. Status is assigned from evidence weight, not from fit to expectation.

Coverage map (immutable from this point forward):

| Rule | S1: Web | S2: Intel | S3: Hypo | S4: Analysis | S5: Synth |
|------|---------|-----------|----------|--------------|-----------|
| SEQUENCING | checked | checked | checked | checked | checked |
| ATTRIBUTION | checked | checked | -- | checked | -- |
| CALIBRATION | -- | -- | -- | checked | checked |
| FALSIFICATION | -- | -- | checked | -- | checked |

---

### Stage 1 -- prove-websearch

SEQUENCING RULE invoked: Is this stage running before any hypothesis has been stated? [ Yes / No ]

Search for primary evidence on **{{topic}}**. Pull recent publications, industry reports, technical references, quantitative data. Do not filter for any anticipated conclusion -- collect indiscriminately.

Label every finding: `[web search]`

ATTRIBUTION RULE invoked: Does every finding carry a `[web search]` label? [ Yes / No ]

---

### Stage 2 -- prove-intelligence

SEQUENCING RULE invoked: Has hypothesis declaration not yet occurred? [ Yes / No ]

Apply expert judgment to the web search corpus:
- Identify patterns and contradictions
- Characterize evidence strength (well-evidenced vs. thin)
- Surface domain-specific considerations
- Note knowledge gaps

Label every finding: `[intelligence]`

ATTRIBUTION RULE invoked: Does every new claim carry an `[intelligence]` label? [ Yes / No ]

---

### Stage 3 -- prove-hypothesis

SEQUENCING RULE invoked: Were Stages 1 and 2 complete before this stage began? [ Yes / No ]
FALSIFICATION RULE invoked: Is each hypothesis stated in a form that evidence could refute? [ Yes / No ]

A hypothesis anchored before evidence gathering is a bias, not a hypothesis. The following hypotheses are derived from the evidence gathered in Stages 1 and 2.

Declare 3-5 falsifiable hypotheses. For each:
- State the claim
- Cite the Stage 1 or Stage 2 evidence that grounds it
- Identify what evidence would refute it

FALSIFICATION RULE invoked: Could counter-evidence exist that would mark any of these as Refuted? [ Yes / No ]

---

### Stage 4 -- prove-analysis

ATTRIBUTION RULE invoked: Does every analyzed claim carry a source-stage label? [ Yes / No ]
CALIBRATION RULE invoked: Do confidence ratings vary across findings -- are at least two distinct levels present? [ Yes / No ]

For each hypothesis:
- Assess supporting evidence weight `[web search]` / `[intelligence]`
- Assess challenging evidence weight
- Assign confidence: High / Medium / Low
- State the specific evidence driving this confidence assignment

If confidence ratings are emerging as uniform: explicitly reassess. Uniform confidence is a calibration failure.

CALIBRATION RULE invoked: Is there at least one finding at a different confidence level from the others? [ Yes / No ]

---

### Stage 5 -- prove-synthesize

SEQUENCING RULE invoked: Were all four prior stages complete before synthesis began? [ Yes / No ]
CALIBRATION RULE invoked: Two distinct confidence levels present across the full brief? [ Yes / No ]
FALSIFICATION RULE invoked: Does every declared hypothesis carry a final status? [ Yes / No ]

**Consensus** (where Stage 1 and Stage 2 agree):
[findings where web search and intelligence concur]

**Conflict** (where Stage 1 and Stage 2 diverge):
[findings where web search and intelligence differ -- name the divergence explicitly]

**Hypothesis Register**:

| Hypothesis | Status | Confidence | Evidence Basis |
|------------|--------|------------|----------------|
| H-01: ... | Supported/Refuted/Indeterminate | High/Med/Low | ... |

**Gaps and Open Questions**:
What remains under-evidenced after this full campaign?

**Decision Readiness** (one sentence):
[Ready to proceed.] or [Needs more investigation on {specific gap} before committing.]

CALIBRATION RULE invoked: Are confidence ratings above non-uniform? [ Yes / No ]
FALSIFICATION RULE invoked: Every hypothesis carries a status above? [ Yes / No ]

---

### Output: Evidence Brief

Compile all stage outputs into a single self-contained document. Include: title, topic context, executive summary, hypothesis register with falsification status, evidence record with attribution, synthesis section (consensus and conflict explicitly separated), gaps list, and the decision readiness sentence.

---

## V-02 -- Axis: Role Sequence (Evidence-First Sequence as Central Narrative)

**Variation axis**: The non-standard sequence -- web search and intelligence before hypothesis declaration -- is foregrounded as the defining structural principle of the campaign. The brief opens with an explicit sequence chain. The rationale for the reordering is named in a dedicated declaration block before the preamble.

**Hypothesis**: Naming the reordering as the campaign's primary design decision -- rather than embedding it as an unnamed structural convention -- ensures that any reader or executor understands why the sequence is unusual and cannot accidentally revert to the conventional order.

---

You are running the full evidence campaign for: **{{topic}}**

This campaign runs in evidence-first sequence. The conventional investigation order is: state hypothesis -> gather evidence -> evaluate. This campaign inverts that order by design.

### EVIDENCE-FIRST SEQUENCE DECLARATION

**Why this matters**: A hypothesis stated before evidence is gathered functions as an anchor. Investigators unconsciously weight confirming evidence higher and discount disconfirming evidence. By gathering evidence first and deriving hypotheses from it, the campaign eliminates the anchoring mechanism entirely. Hypotheses here are conclusions grounded in evidence, not predictions confirmed against it.

**Sequence chain**:
1. prove-websearch (gather)
2. prove-intelligence (interpret)
3. prove-hypothesis (derive -- from evidence, not before it)
4. prove-analysis (evaluate)
5. prove-synthesize (conclude)

This sequence is governed by the SEQUENCING RULE below. Any reordering of Stages 1-3 violates it.

### GOVERNANCE PREAMBLE

This preamble is finalized before Stage 1 begins and cannot be modified after any stage executes. This is a commitment, not a record.

**SEQUENCING RULE** [invoked at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
Evidence stages run before hypothesis declaration. Hypotheses are derived from evidence, not confirmed against pre-anchored assumptions. The sequence chain above is enforced -- not recommended.

**ATTRIBUTION RULE** [invoked at: Stage 1, Stage 2, Stage 4]
Every material claim names its source stage: `[web search]`, `[intelligence]`, or `[analysis]`.

**CALIBRATION RULE** [invoked at: Stage 4, Stage 5]
Confidence ratings must vary across findings. Uniform confidence -- every finding rated identically -- is a calibration failure. If all ratings are the same, recalibrate before proceeding.

**FALSIFICATION RULE** [invoked at: Stage 3, Stage 5]
Each hypothesis has one status: Supported / Refuted / Indeterminate. Assigned at synthesis from evidence weight.

Coverage map (immutable):

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| SEQUENCING | checked | checked | checked | checked | checked |
| ATTRIBUTION | checked | checked | -- | checked | -- |
| CALIBRATION | -- | -- | -- | checked | checked |
| FALSIFICATION | -- | -- | checked | -- | checked |

---

### Stage 1 -- Gather: prove-websearch

SEQUENCING RULE invoked.

No hypothesis has been stated. No hypothesis should be stated here. The only task is evidence collection.

Gather evidence on **{{topic}}**: primary sources, recent publications, technical data, market reports, case studies. Collect broadly -- do not filter for any anticipated conclusion.

Label every finding `[web search]`.

ATTRIBUTION RULE invoked.

---

### Stage 2 -- Interpret: prove-intelligence

SEQUENCING RULE invoked.

No hypothesis has been stated. Apply expert interpretation to the web search corpus:
- What patterns emerge?
- Where does evidence conflict?
- Where are the significant gaps?
- What domain-specific considerations does a surface search miss?

Label every new claim `[intelligence]`.

ATTRIBUTION RULE invoked.

---

### Stage 3 -- Derive: prove-hypothesis

SEQUENCING RULE invoked: Stages 1 and 2 are complete. Hypothesis declaration is now permitted.

A hypothesis anchored before evidence gathering is a bias, not a hypothesis. The following hypotheses are derived from the evidence in Stages 1 and 2.

Declare 3-5 hypotheses:
- Each is a falsifiable claim
- Each cites specific Stage 1 or Stage 2 evidence as its basis
- Each names what counter-evidence would look like (falsification condition)

Note: the evidence-first sequence means these hypotheses may differ from what an investigator would have predicted before gathering evidence. That divergence is the point.

FALSIFICATION RULE invoked.

---

### Stage 4 -- Evaluate: prove-analysis

SEQUENCING RULE invoked.
ATTRIBUTION RULE invoked.
CALIBRATION RULE invoked.

For each hypothesis:
- Weigh supporting evidence vs. challenging evidence (label by source stage)
- Assign confidence: High / Medium / Low
- State what drives the confidence assignment

Calibration check: Are at least two distinct confidence levels present? If all findings are rated identically, recalibrate now -- uniform confidence is a calibration failure.

---

### Stage 5 -- Conclude: prove-synthesize

SEQUENCING RULE invoked.
CALIBRATION RULE invoked: Two distinct confidence levels present above?
FALSIFICATION RULE invoked: Every hypothesis has a final status?

**Consensus** (web search and intelligence agree): ...
**Conflict** (web search and intelligence diverge): ...

**Hypothesis Register**:

| # | Hypothesis | Status | Confidence | Evidence |
|---|------------|--------|------------|----------|
| H-01 | ... | ... | ... | ... |

**Gaps and Open Questions**: What remains under-evidenced?

**Decision Readiness** (one sentence, one posture, one specific gap if not ready):
[Ready to proceed.] or [Needs more investigation on {specific gap} before committing.]

---

### Output: Evidence Brief

Assemble into a single document. A reader unfamiliar with this campaign must be able to understand: what was investigated, why this sequence was used, what was found, and what the decision posture is.

---

## V-03 -- Axis: Output Format (Inline Scope Annotations as Primary Structure)

**Variation axis**: Rules are declared with their stage applicability as inline `[invoked at: ...]` annotations within each rule body. There is no separate coverage table -- scope is inseparable from rule identity. A reader cannot encounter a rule without reading where it applies.

**Hypothesis**: Separating rule declarations from coverage maps creates drift risk -- the map can become stale while rules evolve. Inline annotations make rule identity and applicability scope a single inseparable unit; drift requires editing the rule itself.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

The following rules govern this campaign. Declared before Stage 1 begins. Immutable -- cannot be modified after any stage executes. This is a commitment, not a record.

**SEQUENCING RULE** [invoked at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
A hypothesis anchored before evidence gathering is a bias, not a hypothesis. Evidence stages run first; hypothesis declaration follows. Any reordering of Stages 1-3 violates this rule. Rationale: pre-evidence hypotheses function as anchors that distort evidence weighting.

**ATTRIBUTION RULE** [invoked at: Stage 1, Stage 2, Stage 4]
Every material claim names its source stage. Labels: `[web search]` (Stage 1), `[intelligence]` (Stage 2), `[analysis]` (Stage 4). A claim without a stage label is not attributed.

**CALIBRATION RULE** [invoked at: Stage 4, Stage 5]
Confidence ratings must vary. If all findings carry the same confidence level, calibration has failed -- recalibrate before proceeding. The anti-uniformity check is mandatory at every invocation.

**FALSIFICATION RULE** [invoked at: Stage 3, Stage 5]
Each hypothesis carries one of: Supported / Refuted / Indeterminate. Assigned at synthesis from evidence, not fit to expectation.

---

### Stage 1 -- prove-websearch

SEQUENCING RULE invoked [Stage 1 of 5].

Search for evidence on **{{topic}}**. Gather broadly: recent publications, primary data, technical references, case studies. No hypothesis is in play -- collect indiscriminately.

Label every finding: `[web search]`

ATTRIBUTION RULE invoked [Stage 1 of 5]: Every finding carries `[web search]`?

---

### Stage 2 -- prove-intelligence

SEQUENCING RULE invoked [Stage 2 of 5].

Expert interpretation of Stage 1 corpus:
- Patterns and contradictions
- Evidence strength characterization (well-evidenced vs. thin)
- Domain-specific considerations
- Knowledge gaps

Label every new claim: `[intelligence]`

ATTRIBUTION RULE invoked [Stage 2 of 5]: Every new claim carries `[intelligence]`?

---

### Stage 3 -- prove-hypothesis

SEQUENCING RULE invoked [Stage 3 of 5]: Were Stages 1 and 2 complete before this stage began?
FALSIFICATION RULE invoked [Stage 3 of 5]: Is each hypothesis stated in a form that evidence could refute?

A hypothesis anchored before evidence is a bias, not a hypothesis. These hypotheses are derived from the evidence in Stages 1 and 2.

Declare 3-5 hypotheses:

```
H-01: [claim] -- Grounded in: [Stage 1/2 evidence] -- Falsified if: [condition]
H-02: [claim] -- Grounded in: [Stage 1/2 evidence] -- Falsified if: [condition]
H-03: [claim] -- Grounded in: [Stage 1/2 evidence] -- Falsified if: [condition]
```

FALSIFICATION RULE invoked [Stage 3 of 5]: Could counter-evidence exist that would refute any of these?

---

### Stage 4 -- prove-analysis

SEQUENCING RULE invoked [Stage 4 of 5].
ATTRIBUTION RULE invoked [Stage 4 of 5].
CALIBRATION RULE invoked [Stage 4 of 5]: Do confidence ratings vary?

For each hypothesis:

```
H-01:
  Supporting evidence: ... [web search] / [intelligence]
  Challenging evidence: ... [web search] / [intelligence]
  Confidence: High / Medium / Low
  Basis: ...
```

CALIBRATION RULE invoked [Stage 4 of 5]: At least two distinct confidence levels present above?

---

### Stage 5 -- prove-synthesize

SEQUENCING RULE invoked [Stage 5 of 5].
CALIBRATION RULE invoked [Stage 5 of 5]: Two distinct confidence levels present in full brief?
FALSIFICATION RULE invoked [Stage 5 of 5]: Every hypothesis has a final status?

**Consensus** (Stages 1 and 2 agree):
...

**Conflict** (Stages 1 and 2 diverge):
...

**Hypothesis Register**:

```
H-01 | Status: [Supported/Refuted/Indeterminate] | Confidence: [H/M/L] | Basis: ...
H-02 | Status: ... | Confidence: ... | Basis: ...
H-03 | Status: ... | Confidence: ... | Basis: ...
```

**Gaps**:
What remains under-evidenced after this campaign?

**Decision Readiness** (one sentence):
[Ready to proceed.] or [Needs more investigation on {gap} before committing.]

CALIBRATION RULE invoked [Stage 5 of 5]: Non-uniform confidence ratings confirmed?
FALSIFICATION RULE invoked [Stage 5 of 5]: All hypotheses have status?

---

### Output: Evidence Brief

Single self-contained document. Include rule invocation markers for transparency -- a reader should be able to verify that every rule was applied at every stage where its `[invoked at: ...]` annotation commits to applying it.

---

## V-04 -- Combined: Lifecycle Emphasis + Inertia Framing

**Variation axes**:
- **Lifecycle emphasis**: Each stage carries explicit entry conditions, exit conditions, and a word-budget note. Phase boundaries are not implied -- they are stated.
- **Inertia framing**: The default posture is "do not proceed" unless evidence compels it. The decision readiness stage names the specific threshold that flips the posture. The status-quo option is treated as a legitimate competitor to the action option.

**Hypothesis**: Explicit entry/exit conditions prevent stage bleed (beginning synthesis before analysis is complete). Inertia framing prevents premature commitment by ensuring the "don't proceed" case is as well-defined as the "proceed" case.

---

You are running the full evidence campaign for: **{{topic}}**

Default posture: **Do not proceed.** Evidence must affirmatively shift this posture. A brief that fails to build a compelling case confirms the status quo -- which is also a valid outcome.

### GOVERNANCE PREAMBLE

Declared before Stage 1 begins. Immutable after any stage begins execution.

**SEQUENCING RULE** [invoked at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
Evidence stages run before hypothesis declaration. A hypothesis anchored before evidence is an anchor, not a hypothesis. Rationale: pre-committed hypotheses cause investigators to unconsciously weight confirming evidence higher and dismiss disconfirming evidence.

**ATTRIBUTION RULE** [invoked at: Stage 1, Stage 2, Stage 4]
Every material claim names its source stage. Labels: `[web search]`, `[intelligence]`, `[analysis]`.

**CALIBRATION RULE** [invoked at: Stage 4, Stage 5]
Confidence ratings must vary. Uniform confidence is a calibration failure. Anti-uniformity check required at every invocation site.

**FALSIFICATION RULE** [invoked at: Stage 3, Stage 5]
Each hypothesis: Supported / Refuted / Indeterminate. The "Refuted" and "Indeterminate" outcomes are first-class -- a campaign where every hypothesis is Supported has likely failed to falsify.

**INERTIA RULE** [invoked at: Stage 5]
The status quo is a competitor. The default posture is "do not proceed." Evidence must meet a threshold to shift it. If evidence does not meet the threshold, the brief returns "status quo holds" -- this is not a failure.

Coverage map (immutable from this point):

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| SEQUENCING | checked | checked | checked | checked | checked |
| ATTRIBUTION | checked | checked | -- | checked | -- |
| CALIBRATION | -- | -- | -- | checked | checked |
| FALSIFICATION | -- | -- | checked | -- | checked |
| INERTIA | -- | -- | -- | -- | checked |

---

### Stage 1 -- prove-websearch

**Entry condition**: No hypothesis has been stated. This is the first stage.
**Word budget**: Comprehensive but focused -- 10-20 findings, labeled, no editorializing.
**Exit condition**: Raw evidence corpus assembled; no hypothesis stated.

SEQUENCING RULE invoked. ATTRIBUTION RULE invoked.

Search **{{topic}}** for: primary sources, recent data, technical documentation, industry reports. Label everything `[web search]`. Do not filter.

---

### Stage 2 -- prove-intelligence

**Entry condition**: Stage 1 complete. No hypothesis stated.
**Word budget**: Expert interpretation -- characterize the evidence landscape in 5-10 observations.
**Exit condition**: Evidence interpreted; patterns, conflicts, gaps named; no hypothesis stated.

SEQUENCING RULE invoked. ATTRIBUTION RULE invoked.

Interpret the Stage 1 corpus through expert judgment. Label all new claims `[intelligence]`. Explicitly name: where is evidence strong? Where is it thin? Where are the gaps? These gaps will matter at the decision readiness stage.

---

### Stage 3 -- prove-hypothesis

**Entry condition**: Stages 1 and 2 complete.
**Word budget**: 3-5 hypotheses; each with grounding evidence and falsification condition.
**Exit condition**: Hypotheses declared, falsifiable, grounded in Stages 1 and 2.

SEQUENCING RULE invoked. FALSIFICATION RULE invoked.

A hypothesis anchored before evidence is a bias. These are derived from the corpus, not stated before it. Declare each with:
- Claim (falsifiable)
- Grounding evidence (cite Stage 1/2 specific findings)
- Falsification condition (what would refute this)

Note: "Indeterminate" is a legitimate outcome -- not every hypothesis resolves cleanly.

---

### Stage 4 -- prove-analysis

**Entry condition**: Stages 1-3 complete.
**Word budget**: Per-hypothesis analysis; confidence assigned with explicit basis.
**Exit condition**: All hypotheses analyzed; confidence levels varied (at least two distinct levels).

SEQUENCING RULE invoked. ATTRIBUTION RULE invoked. CALIBRATION RULE invoked.

Weigh evidence per hypothesis. Confidence: High / Medium / Low. State basis explicitly.

Calibration checkpoint: If all confidence ratings are identical -- recalibrate. Is the evidence truly equally strong for every claim? If yes, explain why. If no, differentiate.

Note for decision readiness: where evidence is thin (identified in Stage 2), confidence will be Low. Low-confidence findings strengthen the "don't proceed without more investigation" posture -- this is honest signal, not a weakness.

CALIBRATION RULE invoked: At least two distinct confidence levels present? [ ]

---

### Stage 5 -- prove-synthesize

**Entry condition**: Stages 1-4 complete.
**Word budget**: Synthesis (~200-300 words) + hypothesis register + gaps + single verdict sentence.
**Exit condition**: Complete evidence brief with decision readiness verdict.

SEQUENCING RULE invoked. CALIBRATION RULE invoked. FALSIFICATION RULE invoked. INERTIA RULE invoked.

**Consensus** (Stages 1 and 2 agree): ...
**Conflict** (Stages 1 and 2 diverge): ...

**Hypothesis Register**:

| H# | Claim | Status | Confidence | Basis |
|----|-------|--------|------------|-------|

**Gaps and Open Questions**: What would need to be true for a fuller picture?

**Posture Assessment**:
The status quo is: [describe what "don't proceed" looks like for this topic].
The action threshold requires: [what evidence level would justify moving forward].

INERTIA RULE invoked: Does the evidence clear the threshold, or does the status quo hold?

**Decision Readiness** (one sentence):
[Ready to proceed.] or [Status quo holds -- needs more investigation on {specific gap}.] or [Indeterminate -- insufficient evidence to shift posture in either direction.]

CALIBRATION RULE invoked: Non-uniform confidence ratings confirmed? [ ]
FALSIFICATION RULE invoked: Every hypothesis has a status? [ ]

---

### Output: Evidence Brief

Single self-contained document. The "don't proceed" outcome is as valid and well-documented as the "proceed" outcome. A reader should understand both what the evidence says and what threshold was used to evaluate it.

---

## V-05 -- Combined: Role Sequence + Output Format (Evidence-First + Tabular Brief Matrix)

**Variation axes**:
- **Role sequence**: Evidence-first sequence is structurally enforced; hypothesis declaration is explicitly the third stage, positioned after evidence gathering and interpretation.
- **Output format**: The brief's core artifact is a tabular evidence matrix where rows are claims, columns are Stage, Confidence, and Falsification status. The table format makes governance properties machine-checkable.

**Hypothesis**: A tabular evidence matrix compresses the brief's governance properties into a format where compliance is visually verifiable -- a missing confidence rating or stage label is visible as a blank cell, not a prose gap.

---

You are running the full evidence campaign for: **{{topic}}**

### GOVERNANCE PREAMBLE

Finalized before Stage 1. Immutable -- cannot be modified after any stage begins.

**SEQUENCING RULE** [invoked at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
Web search and intelligence run before hypothesis declaration. A hypothesis anchored before evidence gathering is a bias, not a hypothesis. Rationale: pre-evidence hypotheses function as anchors that distort evidence weighting. Hypothesis declaration is Stage 3, not Stage 1.

**ATTRIBUTION RULE** [invoked at: Stage 1, Stage 2, Stage 4]
Every claim in the evidence matrix names its source stage. Column: `Stage`. Values: `S1:Web`, `S2:Intel`, `S4:Analysis`. A row with a blank Stage column is not attributed.

**CALIBRATION RULE** [invoked at: Stage 4, Stage 5]
The `Confidence` column must contain varied values across the matrix. If every row shows the same confidence rating, the column fails calibration -- recalibrate before synthesis.

**FALSIFICATION RULE** [invoked at: Stage 3, Stage 5]
Each hypothesis in the hypothesis table carries a `Status` column value: Supported / Refuted / Indeterminate.

Coverage map (immutable):

| Rule | S1 | S2 | S3 | S4 | S5 |
|------|----|----|----|----|----|
| SEQUENCING | checked | checked | checked | checked | checked |
| ATTRIBUTION | checked | checked | -- | checked | -- |
| CALIBRATION | -- | -- | -- | checked | checked |
| FALSIFICATION | -- | -- | checked | -- | checked |

---

### Stage 1 -- prove-websearch

SEQUENCING RULE invoked.

Gather evidence on **{{topic}}**. Output as evidence rows:

| Claim | Source | Stage | Notes |
|-------|--------|-------|-------|
| [finding] | [URL/ref] | S1:Web | |
| ... | ... | S1:Web | |

No confidence assigned at this stage. No hypothesis stated. Stage column: `S1:Web` for every row.

ATTRIBUTION RULE invoked: Stage column populated for all rows?

---

### Stage 2 -- prove-intelligence

SEQUENCING RULE invoked.

Interpret Stage 1 corpus. Add intelligence claims as new evidence rows:

| Claim | Source | Stage | Notes |
|-------|--------|-------|-------|
| [interpretation] | [Stage 1 finding it derives from] | S2:Intel | |

Characterize: patterns, conflicts, gaps, evidence strength. Do not declare hypotheses.

ATTRIBUTION RULE invoked: Stage column shows `S2:Intel` for all new rows?

---

### Stage 3 -- prove-hypothesis

SEQUENCING RULE invoked: Stages 1 and 2 are complete. Hypothesis declaration now permitted.
FALSIFICATION RULE invoked.

Derive hypotheses from the evidence corpus. Output as hypothesis table:

| H# | Hypothesis | Grounded In | Falsification Condition |
|----|------------|-------------|------------------------|
| H-01 | [claim] | [S1/S2 finding] | [what would refute] |
| H-02 | ... | ... | ... |

A hypothesis anchored before evidence is a bias, not a hypothesis. These are derived from Stages 1 and 2.

---

### Stage 4 -- prove-analysis

SEQUENCING RULE invoked. ATTRIBUTION RULE invoked. CALIBRATION RULE invoked.

Evaluate each hypothesis. Add analysis rows to evidence matrix:

| Claim | Source | Stage | Confidence | Notes |
|-------|--------|-------|------------|-------|
| Supporting: [evidence for H-01] | ... | S4:Analysis | High/Med/Low | re: H-01 |
| Challenging: [evidence against H-01] | ... | S4:Analysis | High/Med/Low | re: H-01 |

CALIBRATION RULE invoked: Does the Confidence column contain at least two distinct values?

---

### Stage 5 -- prove-synthesize

SEQUENCING RULE invoked.
CALIBRATION RULE invoked: Two distinct confidence levels in full evidence matrix?
FALSIFICATION RULE invoked: Every hypothesis has a final status?

Complete the hypothesis table with final status:

| H# | Hypothesis | Status | Final Confidence | Evidence Summary |
|----|------------|--------|-----------------|-----------------|
| H-01 | ... | Supported/Refuted/Indeterminate | High/Med/Low | ... |

**Consensus** (S1:Web and S2:Intel agree):
[findings where web search and intelligence concur]

**Conflict** (S1:Web and S2:Intel diverge):
[findings where web search and intelligence differ -- name the divergence explicitly]

**Full Evidence Matrix**:

| Claim | Source | Stage | Confidence | H# | Notes |
|-------|--------|-------|------------|-----|-------|
| [all evidence rows from Stages 1, 2, 4] | | | | | |

**Gaps**: What cells would need to be filled for a complete picture?

**Decision Readiness** (one sentence):
[Ready to proceed.] or [Needs more investigation on {gap} -- {N} claims remain Low confidence.]

CALIBRATION RULE invoked: Confidence column non-uniform across matrix? [ ]
FALSIFICATION RULE invoked: All hypothesis Status cells populated? [ ]

---

### Output: Evidence Brief

The complete brief is the assembled evidence matrix + hypothesis table + synthesis section. A reader can verify governance compliance by checking:
- All `Stage` cells populated (ATTRIBUTION)
- `Confidence` column shows varied values (CALIBRATION)
- All `Status` cells populated in hypothesis table (FALSIFICATION)
- Hypothesis table rows were added after Stage 1 and Stage 2 rows (SEQUENCING)
