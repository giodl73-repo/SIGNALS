---
skill: quest-variate
skill_target: campaign-evidence
round: 2
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-evidence-rubric-v2-2026-03-16.md
---

# Variations — campaign-evidence / Round 2

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

---

## V-01 — Axis: Role Sequence (Evidence-First)

**Hypothesis**: Reversing the default sequence — running prove-websearch and
prove-intelligence *before* prove-hypothesis forces C-10 (hypotheses declared
post-evidence) to pass structurally. The hypothesis card is written after the
evidence gathering stages complete, so falsification decisions are grounded in
what was actually found rather than pre-anchored assumptions. C-03 (falsification
status) also benefits because the status reflects real evidence, not prior belief.

```
Run the full evidence campaign for: {{topic}}

Evidence comes first. Hypotheses are declared after you have seen what the sources
say — not before.

Execute in this order:

## Stage 1 — prove-websearch

Search the public web for evidence relevant to {{topic}}. For each source:
- Query used
- Direct quote (verbatim, with URL)
- Strength: Strong / Moderate / Weak
- Bearing: Supports / Refutes / Neutral

Do not use training data as evidence. Every claim must have a URL.

Write findings to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

## Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals) for
evidence relevant to {{topic}}. For each source:
- File path (exact)
- Relevant excerpt
- Strength: Strong / Moderate / Weak
- Bearing: Supports / Refutes / Neutral

Write findings to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

## Stage 3 — prove-hypothesis

Now that you have seen what the web and internal sources say, declare the hypothesis.
This ordering is intentional: the hypothesis must reflect the evidence you found,
not a belief you held before searching.

State:
- Claim: [one sentence — what you now believe based on Stages 1-2]
- Falsification condition: [what evidence would disprove this claim]
- Confidence prior: [High / Medium / Low] — [cite the specific findings from
  Stages 1-2 that drive this rating]
- Experiments: [2-3 tests that would further test the claim]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

## Stage 4 — prove-analysis

Analyze patterns in the evidence gathered across Stages 1-3. For each pattern:
- What was analyzed (data source, file, or finding set)
- Pattern observed
- Causal or correlational? State explicitly.
- Confidence: [High / Medium / Low] — [reason]

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

## Stage 5 — prove-synthesize

Merge all signals from Stages 1-4 into an answer-first evidence brief.

Required structure:

**Evidence Brief: {{topic}}**

**Hypothesis**: [from Stage 3]
**Falsification outcome**: [Supported / Refuted / Indeterminate] — [cite the
finding that determined this]

**Key findings** (label each with stage of origin and confidence):
1. [finding] — Stage [N] — [High / Medium / Low confidence]
2. [finding] — Stage [N] — [High / Medium / Low confidence]
3. [finding] — Stage [N] — [High / Medium / Low confidence]
[continue as needed]

Note: Confidence levels must vary. If all findings carry the same level, you have
not calibrated — revisit.

**Consensus**: Where did websearch (Stage 1) and intelligence (Stage 2) agree?
**Divergence**: Where did they disagree, and why?

**Counter-evidence**: [at least one finding that argues against the hypothesis]

**Open gaps**: [what the campaign did not resolve]

**Decision readiness**: [one sentence — ready to proceed or needs more investigation
on [specific gap]]

Write brief to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-10 (structural enforcement — hypothesis after evidence),
C-03 (falsification outcome grounded in actual findings), C-02 (confidence per
finding), C-06 (consensus/divergence explicit), C-07 (calibration warning), C-09,
C-12 (one-sentence decision readiness), C-08 (open gaps).
**Risk**: The evidence-first ordering means Stage 3 hypothesis may feel redundant
to a model that already threaded beliefs through the websearch stage. C-01 still
requires all five stages to be named and present — a model may abbreviate Stage 3
since the hypothesis feels "already done."

---

## V-02 — Axis: Output Format (Per-Finding Confidence Table)

**Hypothesis**: Providing a pre-defined table schema with an explicit confidence
column per row forces C-02 (per-finding confidence) and C-07 (calibration) to pass
by construction. An anti-uniformity note embedded in the schema itself targets
C-11 (calibration anti-pattern guard) structurally rather than as a prose
instruction.

```
Run the full evidence campaign for: {{topic}}

Execute all five prove stages in sequence. For each stage, produce the structured
output shown. Capture everything in a single evidence brief.

---

## Stage 1 — prove-hypothesis

Claim: [one sentence]
Falsification condition: [what would disprove this]
Confidence prior: [High / Medium / Low] — [reason in one clause]

Experiments:
| # | Experiment | Predicted result |
|---|-----------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |

---

## Stage 2 — prove-websearch

| # | Source / URL | Quote (verbatim) | Strength | Bearing |
|---|-------------|-----------------|----------|---------|
| 1 | | | Weak / Moderate / Strong | Supports / Refutes / Neutral |
| 2 | | | | |
| 3 | | | | |

(Minimum 3 sources. Every row requires a URL — no training-data claims.)

---

## Stage 3 — prove-intelligence

| # | File path | Excerpt | Strength | Bearing |
|---|-----------|---------|----------|---------|
| 1 | | | Weak / Moderate / Strong | Supports / Refutes / Neutral |
| 2 | | | | |
| 3 | | | | |

---

## Stage 4 — prove-analysis

| # | Source analyzed | Pattern found | Causal or correlational | Confidence |
|---|----------------|--------------|------------------------|------------|
| 1 | | | | High / Medium / Low |
| 2 | | | | |
| 3 | | | | |

Causal vs correlational: state "Causal" only if mechanism is identified.

---

## Stage 5 — prove-synthesize

### Findings table

| # | Finding | Source stage | Confidence | Notes |
|---|---------|-------------|------------|-------|
| 1 | | Stage [N] | High / Medium / Low | |
| 2 | | Stage [N] | High / Medium / Low | |
| 3 | | Stage [N] | High / Medium / Low | |

CALIBRATION CHECK: Review the Confidence column before proceeding. If every row
carries the same rating, you have not calibrated — redistribute based on evidence
strength. A uniform column is a rubric failure.

### Falsification status

| Hypothesis | Status | Evidence basis |
|-----------|--------|----------------|
| [from Stage 1] | Supported / Refuted / Indeterminate | [cite Stage and row #] |

### Consensus and divergence

Websearch (Stage 2) and intelligence (Stage 3) agreed on:
- [point of agreement]

Websearch (Stage 2) and intelligence (Stage 3) diverged on:
- [point of divergence] — reason: [why they differ]

### Counter-evidence

[At least one finding that argues against the main hypothesis, with stage citation]

### Open gaps

[What the campaign did not resolve]

### Decision readiness

[One sentence: ready to proceed or needs more investigation on [specific gap]]

---

Write artifact to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five named stages each with schema), C-02 (confidence
column per row in findings table), C-03 (falsification status table), C-04
(structured brief readable by an outsider), C-06 (consensus/divergence section),
C-07 (calibration check embedded in schema), C-08 (open gaps), C-09, C-11
(CALIBRATION CHECK as explicit anti-pattern guard), C-12 (one-sentence decision
readiness).
**Risk**: Table-heavy output may produce shallow cell content — a model filling
the schema mechanically satisfies structure without substance. The calibration check
relies on self-review; a model may write it and then ignore it.

---

## V-03 — Axis: Phrasing Register (Conversational)

**Hypothesis**: Question-driven framing produces more natural per-claim reasoning.
When the model is asked to "explain what the sources actually say" rather than
"produce evidence tables," it tends to thread stage attribution organically through
the prose, satisfying C-05 (source attribution) and C-06 (consensus/conflict) more
naturally than schema-filling. The risk is weaker C-01 coverage discipline.

```
You are running a full evidence campaign for: {{topic}}

The goal is a complete evidence brief — a document that tells the reader what was
investigated, what was found at each stage, and what the evidence collectively says.
The brief is a deliverable for someone who did not run the investigation.

Work through these questions in order:

**1. What do we believe going in, and what would change our mind?**

State the hypothesis — one sentence, falsifiable. What evidence would disprove it?
What is your confidence level (High / Medium / Low), and why?
What experiments would test it?

**2. What does the public web say?**

Search for evidence. For each source: quote it verbatim (include the URL), note
whether it supports or refutes the hypothesis, and rate its strength (Weak /
Moderate / Strong). Do not paraphrase without attribution. Training data is not
evidence.

**3. What do internal sources say?**

Search the repo, design docs, scenarios, and prior signals. For each source: give
the exact file path, quote the relevant section, and explain its bearing on the
hypothesis. Internal sources can be stronger than public sources for product-specific
claims — treat them seriously.

**4. What patterns emerge across the evidence?**

Analyze the findings from stages 2 and 3. What patterns appear? For each: is the
relationship causal (mechanism identified) or correlational? How confident are you
in each pattern (High / Medium / Low), and why?

**5. What does the evidence add up to?**

Write the evidence brief. Answer these questions directly:

- Which hypothesis does this investigation address?
- What is the falsification status: supported, refuted, or indeterminate?
  Name the specific finding that determined the outcome.
- What are the key findings? For each one, say where it came from (which stage),
  what it says, and how confident you are. Do not assign the same confidence level
  to every finding — if everything looks the same, your calibration is off.
- Where did the web search (stage 2) and internal search (stage 3) agree?
  Where did they disagree, and why does that matter?
- What was the strongest counter-evidence — the finding that most challenges
  the hypothesis?
- What does this campaign still not know? Name the open gaps.
- Are we ready to proceed, or do we need more investigation on something specific?
  Answer in one sentence.

Write the complete brief to:
simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-04 (explicit framing — "a deliverable for someone who did
not run the investigation"), C-05 (question 5 asks "where it came from (which
stage)"), C-06 (explicit agreement/disagreement question), C-07 (anti-uniformity
instruction in question 5), C-08 (open gaps question), C-09, C-12 (one-sentence
decision readiness).
**Risk**: No formal stage headers — C-01 (all five stages executed) may not pass
unless the model naturally labels its sections after each question. The conversational
tone may also reduce precision on C-02 (per-finding confidence labeling) and
C-03 (explicit falsification status declaration).

---

## V-04 — Combined Axes: Lifecycle Emphasis + Output Format

**Hypothesis**: Explicit gate checks per stage, combined with a structured output
schema, prevent shallow passes and ensure every stage exists as a named artifact
block before synthesis starts. The CALIBRATION GATE at Stage 5 turns C-07 and C-11
into mandatory checkpoints rather than aspirational goals. Gates prevent a model
from running all five stages as a single prose paragraph (the most common C-01 failure).

```
Run the full evidence campaign for: {{topic}}

This skill executes five prove stages in sequence. Each stage has a defined output
and a gate check. Do not advance until the gate check passes.

---

### STAGE 1 — prove-hypothesis [FRAMING GATE]

State the investigation frame:

Claim: [one sentence — what you believe]
Falsification condition: [what would disprove this]
Confidence prior: [High / Medium / Low] — [one-clause reason]
Experiments: [list 2-3 tests]

Gate check: falsification condition defined and non-trivial? --> proceed to Stage 2.

---

### STAGE 2 — prove-websearch [EVIDENCE GATE]

Search the public web. Minimum 3 sources.

For each source:
- URL (required — no training-data claims)
- Direct quote (verbatim)
- Strength: Weak / Moderate / Strong
- Bearing: Supports / Refutes / Neutral

Gate check: 3+ sources with URLs, at least one Refutes or Neutral? --> proceed to Stage 3.

---

### STAGE 3 — prove-intelligence [INTERNAL GATE]

Search internal sources (repo files, docs, scenarios, prior signals).

For each source:
- File path (exact)
- Excerpt (relevant section)
- Strength: Weak / Moderate / Strong
- Bearing: Supports / Refutes / Neutral

Gate check: 3+ internal sources cited with exact file paths? --> proceed to Stage 4.

---

### STAGE 4 — prove-analysis [PATTERN GATE]

Analyze patterns in Stages 1-3 evidence.

For each pattern:
- Source (Stage 2 row / Stage 3 file / Stage 1 experiment)
- Pattern
- Causal or correlational? State explicitly — "Causal" requires identified mechanism.
- Confidence: High / Medium / Low — [reason]

Gate check: at least 2 patterns analyzed, causal/correlational labeled per pattern?
--> proceed to Stage 5.

---

### STAGE 5 — prove-synthesize [CALIBRATION GATE + DECISION GATE]

Before writing synthesis: check that your confidence ratings across Stages 1-4
include at least two distinct levels (High, Medium, Low). If every rating is the
same level, redistribute — uniform confidence is a calibration failure.

Write the evidence brief with this required structure:

**Evidence Brief: {{topic}}**

**Hypothesis** (from Stage 1): [claim]
**Falsification status**: [Supported / Refuted / Indeterminate]
**Falsification basis**: [cite the Stage and finding that determined this]

**Key findings**:
| # | Finding | Source stage | Confidence |
|---|---------|-------------|------------|
| 1 | | Stage [N] | High / Medium / Low |
| 2 | | Stage [N] | High / Medium / Low |
| 3 | | Stage [N] | High / Medium / Low |
| 4 | | Stage [N] | High / Medium / Low |
| 5 | | Stage [N] | High / Medium / Low |

**Stage 2 vs Stage 3 — Consensus**: [where web and internal sources agreed]
**Stage 2 vs Stage 3 — Divergence**: [where they disagreed, and why]

**Counter-evidence**: [the finding most challenging to the hypothesis]

**Open gaps**: [what this campaign did not resolve]

**Decision readiness**: [one sentence — ready to proceed or needs more investigation
on [specific gap]]

---

Write artifact to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five named stages, each with schema and gate), C-02
(confidence per row in findings table), C-03 (falsification status + basis), C-04
(titled structured brief), C-06 (consensus/divergence section), C-07 (CALIBRATION
GATE requires two distinct levels), C-08 (open gaps), C-09, C-11 (CALIBRATION GATE
as explicit anti-uniformity guard), C-12 (one-sentence decision readiness).
**Risk**: Gate language may become prose commentary — a model may write "Gate check:
pass" without having completed the actual stage output. Five gate checks add
verbosity; a model following them too literally may produce five shallow outputs
rather than three thorough ones.

---

## V-05 — Combined Axes: Role Sequence (Evidence-First) + Named Rules

**Hypothesis**: Pairing evidence-first sequencing (websearch + intelligence before
hypothesis finalization) with explicit named rules — CALIBRATION RULE, FALSIFICATION
RULE, ATTRIBUTION RULE — targets the hardest aspirational criteria (C-10, C-11,
C-12) alongside the essential ones (C-02, C-03). Named rules make violation visible
as a named failure rather than an omission. The combination is additive: evidence-
first handles C-10 structurally; named rules handle C-02, C-07, C-11, C-12 via
explicit prohibition.

```
Run the full evidence campaign for: {{topic}}

Produce a complete evidence brief. The brief is a single document that a reader
unfamiliar with the run can understand — it must stand alone.

---

CALIBRATION RULE: Confidence ratings must vary. If every finding carries the same
confidence level, you have not calibrated — the evidence does not actually support
uniform certainty. Before finalizing synthesis, review your ratings and confirm at
least two distinct levels appear. A brief with uniform confidence fails this rule.

FALSIFICATION RULE: Every hypothesis in this brief must carry an explicit status
(Supported / Refuted / Indeterminate) with a named evidence basis. A hypothesis
without a falsification outcome is not an outcome — it is a draft.

ATTRIBUTION RULE: Every material claim in the synthesis must name its source stage.
"[claim] — Stage [N]" is the minimum. Floating claims not traceable to a stage are
not acceptable.

---

Execute in this sequence:

### Stage 1 — prove-websearch

Search the public web for evidence. For each source: URL, verbatim quote, strength
(Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral). No training-data
claims — every claim needs a URL.

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

### Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals). For
each source: exact file path, excerpt, strength, bearing.

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

### Stage 3 — prove-hypothesis [POST-EVIDENCE]

You have now seen what the web and internal sources say. Declare the hypothesis.

Claim: [one sentence — what the evidence supports you believing]
Falsification condition: [what would disprove this]
Confidence: [High / Medium / Low] — [cite specific findings from Stages 1-2 that
  drive this rating]
Experiments: [2-3 tests that would further test the claim]

This stage is ordered after evidence gathering by design. A hypothesis anchored
before evidence gathering is a bias, not a hypothesis.

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

### Stage 4 — prove-analysis

Analyze patterns in the combined evidence from Stages 1-3. For each pattern: data
source, pattern observed, causal or correlational (state explicitly), confidence
(High / Medium / Low with reason).

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

### Stage 5 — prove-synthesize

CALIBRATION CHECK (apply CALIBRATION RULE now): Review all confidence ratings from
Stages 1-4 before writing. If all ratings are the same level, revise before
proceeding.

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}

**Hypothesis** (finalized post-evidence, Stage 3): [claim]

**Falsification status** (FALSIFICATION RULE): [Supported / Refuted / Indeterminate]
**Basis**: [name the specific finding — Stage N, row or excerpt — that determined this]

**Key findings** (ATTRIBUTION RULE — every finding names its source stage):
1. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
2. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
3. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
[continue — minimum 5 findings]

**Consensus** (Stage 1 vs Stage 2): [where web and internal sources agreed]
**Divergence** (Stage 1 vs Stage 2): [where they disagreed — and why it matters]

**Counter-evidence**: [the finding most challenging to the hypothesis, with stage cite]

**Open gaps**: [what the campaign did not resolve — enables a follow-up to pick up cleanly]

**Decision readiness**: [EXACTLY ONE SENTENCE — e.g., "Ready to proceed" or "Needs
more investigation on [specific named gap] before committing."]

Write brief to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five named stages), C-02 (per-finding confidence with
rationale), C-03 (FALSIFICATION RULE + status + basis required), C-04 (titled,
dated, self-contained brief), C-05 (ATTRIBUTION RULE + per-finding stage cites),
C-06 (consensus/divergence named), C-07 (CALIBRATION RULE requires two distinct
levels), C-08 (open gaps), C-09, C-10 (Stage 3 explicitly labeled "POST-EVIDENCE"
with design rationale), C-11 (CALIBRATION CHECK as explicit anti-uniformity guard),
C-12 (EXACTLY ONE SENTENCE directive on decision readiness).
**Risk**: Named rules add prose overhead — a model may include the rule text in its
output without applying the rules. The [POST-EVIDENCE] label on Stage 3 must
actually change the model's behavior, not just appear as a section header. If C-10
is assessed purely by position (hypothesis appears after websearch), this variation
wins; if assessed by the quality of grounding, shallow models may still pre-anchor.

---

## Variation Summary

| ID | Axes | Primary Rubric Targets | Key Risk |
|----|------|----------------------|----------|
| V-01 | Role sequence (evidence-first) | C-10, C-03, C-02, C-06, C-07, C-08, C-09, C-12 | Stage 3 may feel redundant; C-01 abbreviated |
| V-02 | Output format (per-finding table) | C-01, C-02, C-03, C-04, C-06, C-07, C-08, C-09, C-11, C-12 | Schema filling without substance; self-check ignored |
| V-03 | Phrasing register (conversational) | C-04, C-05, C-06, C-07, C-08, C-09, C-12 | C-01 stage coverage at risk; C-02/C-03 may be imprecise |
| V-04 | Lifecycle emphasis + output format | C-01, C-02, C-03, C-04, C-06, C-07, C-08, C-09, C-11, C-12 | Gate checks become prose; stages may be shallow |
| V-05 | Role sequence (evidence-first) + named rules | C-01..C-12 (broadest) | Named rules treated as style; Stage 3 POST-EVIDENCE not behavioral |

**Predicted leaderboard going into quest-score**: V-05 > V-04 > V-02 > V-01 > V-03.
V-05 is the only variation that directly names and structurally enforces all four
essential criteria AND the three hardest aspirationals (C-10, C-11, C-12). V-03 is
most likely to fail C-01 (stage coverage) and C-02 (per-finding confidence precision)
due to its unstructured register. V-04's gate pattern is strong for essential coverage
but the calibration gate depends on self-review, which is the same weakness as V-02.
The evidence-first ordering in V-01 and V-05 is the only structural defense for C-10;
the other three variations require behavioral compliance with an instruction.
