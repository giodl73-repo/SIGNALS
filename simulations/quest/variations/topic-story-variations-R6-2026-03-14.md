# topic-story Rubric v6 — Skill Variations V-01 through V-05

---

## V-01 — Axis: Role Sequence (Binary-Verifiable Checklist Gates the Write)

**Hypothesis**: When the pre-artifact checklist uses binary-verifiable items (locate a named element vs. evaluate quality), authors complete C-19 and C-22 requirements structurally and produce complete artifacts more reliably than when checklist items require editorial judgment at gate-time.

---

You are synthesizing signals for the topic: `{{topic}}`.

Read every signal artifact for this topic before proceeding. They are in `simulations/` under the appropriate namespace directories. Do not begin writing the artifact until the pre-artifact checklist below is complete.

---

### PRE-ARTIFACT CHECKLIST

Answer each item YES or NO. Each item is answered by locating a specific named element — not by making a quality judgment. Record your answers. Do not write the artifact until you have completed this checklist.

**Structure verification (locate-and-find)**

- [ ] Will the artifact include a section with the label `## Signal Findings`?
- [ ] Will the artifact include a section with the label `## What the Signals Say Together`?
- [ ] Will the artifact include a section with the label `## What Remains Uncertain`?
- [ ] Will the artifact include a section with the label `## Recommendation`?
- [ ] Will `## What the Signals Say Together` contain a line starting with `**Pattern claim**:`?
- [ ] Will `## What the Signals Say Together` contain a line starting with `**Disproof condition**:`?
- [ ] Will `## Recommendation` contain a line starting with `**Verdict**:` followed by one of: `proceed` / `pause` / `pivot` / `abandon`?

**Per-finding enforcement (locate-and-find)**

- [ ] Will each finding block in `## Signal Findings` end with a line starting with `**Inertia verdict**:`?
- [ ] Will the `**Pattern claim**:` be a single sentence containing the word "because" or "since" (causal account)?
- [ ] Will `**Disproof condition**:` name a specific observable condition (not a rhetorical hedge)?

**Anti-neutral enforcement (locate-and-find)**

- [ ] Will `## What Remains Uncertain` contain at least one line starting with `**Consequence**:`?
- [ ] Will `## Recommendation` NOT contain the string `"the team should consider"`?
- [ ] Will `## Recommendation` NOT contain the string `"based on available evidence"`?
- [ ] Will `## Recommendation` NOT contain the string `"it would be reasonable to"`?

Record checklist answers. If any structural item is NO, revise your plan before writing. If any anti-neutral item would be YES (the forbidden phrase is present), revise the section before finalizing.

---

### ARTIFACT TEMPLATE

Write the artifact using this template. Every labeled field is required. Every label is a binary-verifiable element — reviewers will locate it by name.

```
---
topic: {{topic}}
signal: story
date: {{date}}
---

## What We Set Out to Understand

[One to three sentences. State the question the feature investigation was trying to answer.
Name the decision at stake. Write in active voice.]

## Signal Findings

[For each signal gathered for this topic, write one finding block.
Order by decision relevance — highest decision impact first.
Apply the inertia filter: if this finding would not change what the team does, omit it.]

**[Signal namespace] — [Signal type]**
[Key finding. One to two sentences. Name what the signal revealed, not what it contained.
No enumeration of sub-findings.]
**Inertia verdict**: [YES the team would proceed without this / NO this finding changes the decision / PARTIAL — one clause stating which aspect changes and which does not.]

[Repeat block for each decision-relevant signal]

## What the Signals Say Together

[Interpretive prose. Name the pattern the signals form together — not a list of signals,
not a tour of findings. Two to four sentences. Explain why the signals converge, not just
that they do. The causal mechanism must be named.]

**Pattern claim**: [One sentence. A falsifiable assertion about what the signals collectively
establish. Specific enough that a contradictory finding would disprove it.]

**Disproof condition**: [The pattern claim above fails if: [name the specific observable
condition that would falsify it — a finding type, a measurement result, a user behavior].]

## What Remains Uncertain

[Name what you genuinely do not know and why it matters to the decision.
Do not list gaps for completeness. Every uncertainty named here must have a consequence.
If an uncertainty would not change the recommendation, omit it.]

**[Uncertainty label]**: [What is unknown and why the current evidence cannot resolve it.]
**Consequence**: [This matters because if [specific condition X holds], then the recommendation changes from [current verdict] to [alternative verdict].]

[Repeat block for each decision-relevant uncertainty]

## Recommendation

**Verdict**: [proceed / pause / pivot / abandon]

[Two to four sentences. Take a position. State what the team should do next and name the
first concrete action. Name the condition that would cause you to revise this recommendation.
Write in second person ("proceed to build X") or first person ("I recommend proceeding") —
not third person passive.]
```

---

### POST-WRITE VERIFICATION

After writing, perform a final structural scan:

1. Locate `**Pattern claim**:` — confirm it is a single sentence containing "because" or "since."
2. Locate `**Disproof condition**:` — confirm it names a specific observable condition, not a phrase like "if the evidence changes."
3. Locate every `**Inertia verdict**:` — confirm one exists per finding block.
4. Locate every `**Consequence**:` — confirm one exists per uncertainty block and names both the condition and the alternative verdict.
5. Locate `**Verdict**:` — confirm it is one of the four permitted values.
6. Scan `## Recommendation` for: "the team should consider" / "based on available evidence" / "it would be reasonable to." If found, revise before saving.

Write the artifact to: `simulations/topic/story/{{topic}}-story-{{date}}.md`

---

## V-02 — Axis: Inertia Framing (Status-Quo Competitor Runs Through All Four Sections)

**Hypothesis**: When the inertia question ("would we proceed/hold without this signal?") is the explicit organizing principle for all four sections — not just a per-finding filter — the synthesis becomes more decision-oriented throughout, and the recommendation acquires explicit accountability by naming what the team would do in the absence of evidence.

---

You are synthesizing signals for the topic: `{{topic}}`.

Read every signal artifact for this topic before writing. Do not summarize what each signal contains. Your job is editorial synthesis: what do the signals say *together*, and what should the team do *because of what the signals say together*.

The organizing principle for every section is the inertia question: **what would the team do if this signal (or set of signals) did not exist?** The value of every finding and the force of the recommendation both derive from their distance from the default.

---

### INERTIA BASELINE

Before writing any section, state the default position:

> Without any gathered signals, the team's prior for this feature is: [state the pre-investigation assumption — e.g., "proceed to spec" / "hold pending discovery" / "the feature is technically feasible" / "unknown"].

This baseline becomes the benchmark for the recommendation. The recommendation is only as strong as the distance between it and the baseline.

---

### SECTION 1 — Signal Findings

For each gathered signal, write one finding. The structure is:

**[Namespace] — [Signal type]**
[What the signal revealed. One to two sentences. Write what the signal *means*, not what it *contains*.]
**Without this signal**: [One clause. What would the team assume or do if this signal had never been gathered?]
**With this signal**: [One clause. What does the team now know or do differently?]
**Delta**: [move / hold / reinforce — one word, then one clause explaining whether this signal moves the team away from the baseline, holds the baseline, or reinforces a move already established by a prior signal.]

Apply a decision filter before including a finding: if "Without this signal" and "With this signal" would be the same statement, omit the finding. It has no decision value.

---

### SECTION 2 — What the Signals Say Together

Do not tour the findings. Name the pattern.

Begin by stating what the signals say together that *no individual signal could say alone*. The synthesis is the emergent claim — the thing that becomes visible only when the signals are read as a set.

Then provide the causal account: explain why the signals converge. Name the mechanism. "The signals agree because [X]" — where X is not "there are many signals" but the structural reason the evidence points the same direction.

Then state:

**Pattern claim**: [One sentence. Specific, falsifiable. A claim that could be disproved by a specific finding type.]

**What a skeptic would have to show is false**: [The pattern claim fails if: [specific observable condition]. Name it concretely — a measurement result, a user behavior, a technical property, a market condition.]

**Distance from baseline**: [One sentence. The pattern claim represents a [large / moderate / small] departure from the pre-investigation prior, because [reason].]

---

### SECTION 3 — What Remains Uncertain

Do not list gaps. Name uncertainties that have decision consequences.

For each uncertainty:

**[Uncertainty label]**: [What is unknown. One sentence.]
**Why it cannot be resolved with current signals**: [One clause naming the missing signal type or evidence gap.]
**Verdict consequence**: [If this uncertainty resolves in direction A, the recommendation becomes [X]. If it resolves in direction B, the recommendation becomes [Y].]

If an uncertainty would not change the recommendation regardless of how it resolves, omit it. The uncertainty section is not an honest accounting of ignorance — it is a decision-calibrated accounting of what matters.

Do not write sentences of the form "It is unclear whether X." Every sentence in this section names the uncertainty and its verdict consequence in the same breath.

---

### SECTION 4 — Recommendation

State:

**Without signals**: [One sentence. What the team would do if the signals had never been gathered — the baseline position.]
**With signals**: [One sentence. What the signals establish that changes the baseline.]
**Verdict**: [proceed / pause / pivot / abandon]

[Two to four sentences of reasoning. Take a position. Name the first action. Name the condition under which you would revise this recommendation — one specific observable event that would change the verdict.]

Do not write: "The team should consider..." or "Based on the available evidence, it would be reasonable to..."

Write: "Proceed to [specific action]." or "Pause until [specific condition]." The verdict is not a suggestion.

---

Save the completed artifact to: `simulations/topic/story/{{topic}}-story-{{date}}.md`

---

## V-03 — Axis: Output Format (Strict Labeled Fields as Required Template Elements)

**Hypothesis**: When every required output element is a named labeled field in a required template — rather than an embedded instruction to "include" something — authors produce C-20-compliant artifacts (disproof condition as labeled field, not buried in prose) more reliably, and reviewers can verify compliance by locating fields rather than reading body text.

---

You are synthesizing signals for the topic: `{{topic}}`.

Read every signal artifact for this topic. Your output is a single artifact written into the template below. Every labeled field is required. A missing labeled field is a structural fail regardless of whether the content appears in the prose. Reviewers locate compliance by field, not by reading.

---

### REQUIRED OUTPUT TEMPLATE

Every field label below is required. Write content after the `:` delimiter. Do not rename fields. Do not omit fields. Do not merge fields.

```
---
topic: {{topic}}
signal: story
date: {{date}}
---

**Investigation question**: [The question the feature investigation was designed to answer.
One sentence. Names the decision at stake.]

---

## Signal Findings

[One block per decision-relevant signal. Omit signals whose finding would not change
the team's course of action.]

### [Namespace]: [Signal type]

**Finding**: [What the signal revealed. One to two sentences. Interpretive — what it means,
not what it contained.]

**Decision relevance**: [One sentence. Why this finding bears on the decision at stake.]

**Inertia verdict**: [proceed-without / hold-without / unknown-without — followed by one clause
stating what the team would assume if this signal had not been gathered.]

---

## What the Signals Say Together

**Synthesis**: [Interpretive prose. The pattern the signals form together. Two to four sentences.
Not a tour of findings. Name what becomes visible when the signals are read as a set.]

**Causal account**: [One to two sentences. Explain why the signals converge — name the
mechanism, not just the observation.]

**Pattern claim**: [One sentence. A falsifiable assertion about what the signals collectively
establish. Must be specific enough that a contradictory finding could disprove it.]

**Disproof condition**: [The pattern claim fails if: [specific observable condition —
a finding type, measurement result, user behavior, or market condition]. Do not write
"if the evidence changes" or "if further research shows otherwise."]

---

## What Remains Uncertain

[One block per decision-relevant uncertainty. Omit uncertainties that would not change
the recommendation regardless of resolution.]

### [Uncertainty label]

**Unknown**: [What is not known. One sentence.]

**Evidence gap**: [Why current signals cannot resolve this. Name the missing signal type.]

**Consequence**: [Verdict consequence. "If [condition A], recommendation becomes [X].
If [condition B], recommendation becomes [Y]."]

---

## Recommendation

**Verdict**: [proceed / pause / pivot / abandon — one of these four values exactly]

**Rationale**: [Two sentences. State what the signals establish that justifies this verdict.
Write in active, committed voice. Not "it would be reasonable to..." — state the position.]

**First action**: [One sentence. The specific first step the team should take given this verdict.]

**Revision trigger**: [One sentence. The specific observable event that would cause this
recommendation to change. Name the event — not "if conditions change" but the event itself.]

**Confidence qualifier**: [One sentence. State any single uncertainty from the section above
that most threatens this recommendation, and how much it threatens it.]
```

---

### FIELD COMPLETENESS CHECK

After writing, scan for every field label. Confirm each is present and populated. A field present but left as a bracket placeholder is a structural fail equivalent to a missing field.

Required fields (in order):
1. `**Investigation question**:`
2. `**Finding**:` (one per signal block)
3. `**Decision relevance**:` (one per signal block)
4. `**Inertia verdict**:` (one per signal block)
5. `**Synthesis**:`
6. `**Causal account**:`
7. `**Pattern claim**:`
8. `**Disproof condition**:`
9. `**Unknown**:` (one per uncertainty block)
10. `**Evidence gap**:` (one per uncertainty block)
11. `**Consequence**:` (one per uncertainty block)
12. `**Verdict**:`
13. `**Rationale**:`
14. `**First action**:`
15. `**Revision trigger**:`
16. `**Confidence qualifier**:`

Save to: `simulations/topic/story/{{topic}}-story-{{date}}.md`

---

## V-04 — Axis: Phrasing Register (Anti-Neutral Enforcement at Sentence Grain)

**Hypothesis**: When the template names the sentence-level failure condition per section (e.g., "a sentence that names uncertainty without naming its verdict consequence is a failed sentence") and provides verbatim hedge strings the author can match against their draft, authors produce C-21- and C-23-compliant artifacts more reliably than when anti-neutral instructions say "write decisively" or "maintain interpretive voice."

---

You are synthesizing signals for the topic: `{{topic}}`.

Read every signal artifact for this topic. Write the artifact in four sections. The four sections are structurally distinct: each performs a different analytical operation, and each has its own failure mode. The failure modes are named below, at sentence grain. Scan every sentence you write against the failure mode for its section.

---

### SECTION DEFINITIONS AND FAILURE CONDITIONS

**Section 1 — Signal Findings**
*Operation*: Curate for decision salience. Select what changed your understanding.
*Sentence-level failure condition*: A sentence that reports what a signal *contains* rather than what it *reveals* is a failed sentence. "The scout-feasibility signal identified three technical risks" is a contents report. "The scout-feasibility signal established that the primary technical risk is integration latency under concurrent load, not throughput" is a finding. Revise or remove any contents-report sentence.

**Section 2 — What the Signals Say Together**
*Operation*: Name the pattern. Explain why it exists.
*Sentence-level failure condition*: A sentence that lists signals or references individual findings is a failed sentence. "The scout, draft, and flow signals all indicated X" is a signal list. "The signals converge on X because [mechanism]" is a synthesis. Revise or remove any sentence that references individual signals by name in lieu of naming the pattern.

**Section 3 — What Remains Uncertain**
*Operation*: Name what matters to the decision that the signals could not resolve.
*Sentence-level failure condition*: A sentence that names an uncertainty without naming its verdict consequence is a failed sentence. "It is unclear whether enterprise customers will accept the pricing model" names uncertainty. "If enterprise customers reject the pricing model, the recommendation shifts from proceed to pivot toward a consumption-based alternative" names uncertainty and its consequence. Revise or remove any sentence that does not complete the "if this uncertainty resolves against us, then [verdict change]" arc.

**Section 4 — Recommendation**
*Operation*: Advocate with accountability. Name the action and the revision trigger.
*Sentence-level failure condition*: A sentence that hedges the verdict is a failed sentence. Do not write:
- "The team should consider proceeding..."
- "Based on the available evidence, it would be reasonable to..."
- "It may be worth exploring..."
- "One option would be to..."
- "The signals suggest that X might..."

Each of these constructions assigns the decision to the reader. The recommendation section owns the decision. Write: "Proceed to [action]." or "Pause until [condition]." or "Pivot to [alternative]." or "Abandon [feature] because [reason]."

---

### ARTIFACT STRUCTURE

```
---
topic: {{topic}}
signal: story
date: {{date}}
---

## What We Set Out to Understand

[One to three sentences. The question and the decision at stake.]

## Signal Findings

[One finding per decision-relevant signal. Apply the contents-report failure condition
to every sentence before including it.]

**[Namespace] — [Signal type]**
[Finding. What the signal revealed. One to two sentences.]
**Inertia verdict**: [Would the team proceed without this finding? One clause.]

## What the Signals Say Together

[Interpretive prose. Apply the signal-list failure condition to every sentence.
Two to four sentences. Include a causal account.]

**Pattern claim**: [One falsifiable sentence.]

**Disproof condition**: [The claim fails if: [specific observable condition].]

## What Remains Uncertain

[One block per decision-relevant uncertainty. Apply the verdict-consequence failure
condition to every sentence.]

**[Uncertainty label]**: [What is unknown.] If this resolves against current assumptions,
the recommendation shifts from [current verdict] to [alternative verdict] because [reason].

## Recommendation

**Verdict**: [proceed / pause / pivot / abandon]

[Two to four sentences. Apply the hedge failure condition to every sentence.
Name the action. Name the revision trigger. Write in committed voice.]
```

---

### SENTENCE-LEVEL SCAN (REQUIRED)

After writing each section, run this scan:

**Signal Findings scan**: Read each sentence. Ask: "Does this sentence report what the signal contained, or what it revealed?" If contained: revise.

**Synthesis scan**: Read each sentence. Ask: "Does this sentence list signals by name in place of naming the pattern?" If yes: revise.

**Uncertainty scan**: Read each sentence. Ask: "Does this sentence name an uncertainty without completing the verdict-consequence arc?" If yes: revise or remove.

**Recommendation scan**: Read each sentence. Check for: "should consider" / "it would be reasonable" / "it may be worth" / "one option would be" / "the signals suggest that X might". If found: revise. The recommendation owns the decision.

Save to: `simulations/topic/story/{{topic}}-story-{{date}}.md`

---

## V-05 — Axis: Combination (Binary-Verifiable Checklist + Inertia Framing + Sentence-Level Anti-Neutral)

**Hypothesis**: The three axes from V-01, V-02, and V-04 address complementary failure modes — structural incompleteness (V-01: checklist items must be binary-verifiable), decision-irrelevant content (V-02: inertia filter per section), and voice collapse in uncertainty and recommendation (V-04: sentence-level failure conditions + verbatim hedges). Combined without redundancy, they address the most common failure patterns observed across Rounds 1–5.

---

You are synthesizing signals for the topic: `{{topic}}`.

Read every signal artifact for this topic. This prompt has three enforcement layers that operate at different levels. Complete them in order.

**Layer 1** (before writing): Binary-verifiable checklist — locate named elements, not quality judgments.
**Layer 2** (while writing): Inertia framing — every section anchored to the distance from the default position.
**Layer 3** (after writing): Sentence-level scan — named failure conditions per section, verbatim hedges named.

---

### LAYER 1 — PRE-ARTIFACT CHECKLIST

Answer YES or NO. Each item is answered by locating a named element. Do not evaluate quality.

- [ ] Will the artifact contain the label `## Signal Findings`?
- [ ] Will the artifact contain the label `## What the Signals Say Together`?
- [ ] Will the artifact contain the label `## What Remains Uncertain`?
- [ ] Will the artifact contain the label `## Recommendation`?
- [ ] Will each finding block end with a line beginning `**Inertia verdict**:`?
- [ ] Will `## What the Signals Say Together` contain a line beginning `**Pattern claim**:`?
- [ ] Will `## What the Signals Say Together` contain a line beginning `**Disproof condition**:`?
- [ ] Will `## What Remains Uncertain` contain at least one line beginning `**Verdict consequence**:`?
- [ ] Will `## Recommendation` contain a line beginning `**Verdict**:` followed by one of: `proceed` / `pause` / `pivot` / `abandon`?

If any item is NO, revise your writing plan before proceeding.

---

### LAYER 2 — INERTIA-ANCHORED SECTION INSTRUCTIONS

Before writing, establish the inertia baseline:

> **Baseline**: Without any gathered signals, the team's prior for `{{topic}}` was: [state it — e.g., "proceed to draft" / "hold pending discovery" / "technically feasible, user value unknown"].

This baseline anchors all four sections. Your synthesis is only as strong as the distance it establishes from this baseline.

**Signal Findings — inertia filter per finding**

Include a finding only if it changes the team's position relative to the baseline. For each finding:

**[Namespace] — [Signal type]**
[What the signal revealed. One to two sentences. What it means, not what it contained.]
**Inertia verdict**: [Would the team proceed from the baseline without this finding? YES / NO / PARTIAL — one clause naming what changes.]

If "Inertia verdict" would be YES for every signal, you have gathered evidence that confirms the prior without adding decision force. Name that honestly in the synthesis.

**What the Signals Say Together — distance from baseline**

Name the pattern and the causal account. Then state:

**Pattern claim**: [One falsifiable sentence.]
**Disproof condition**: [The claim fails if: [specific observable condition].]
**Baseline distance**: [The signals establish a [large / moderate / small] departure from the prior, because [reason].]

**What Remains Uncertain — decision-relevant uncertainties only**

For each uncertainty: name it, name why the signals cannot resolve it, and name the verdict consequence. If the uncertainty would not change the recommendation, omit it.

**[Uncertainty label]**: [What is unknown.]
**Verdict consequence**: [If [condition A], verdict becomes [X]. If [condition B], verdict becomes [Y].]

**Recommendation — named distance from baseline**

**Prior position**: [What the team would do without the signals.]
**Signals establish**: [What the signals add that changes the prior position.]
**Verdict**: [proceed / pause / pivot / abandon]
[Two to four sentences. Name the first action. Name the revision trigger.]

---

### LAYER 3 — POST-WRITE SENTENCE SCAN

After writing, scan each section for its named failure condition.

**Signal Findings**: Locate any sentence that reports what a signal *contained* rather than what it *revealed*. Signal-contents sentences begin: "The [signal] identified / found / noted / listed / showed that..." Revise each to state the interpretive finding.

**What the Signals Say Together**: Locate any sentence that lists signals by name in lieu of naming the pattern. Pattern sentences name the shape; they do not tour the evidence. Revise any sentence that begins "The scout, draft, and flow signals..." or equivalent.

**What Remains Uncertain**: Locate any sentence that names an uncertainty without completing the verdict-consequence arc. The arc is: "If [X], then [verdict changes to Y]." Every uncertainty sentence must complete this arc or be removed.

**Recommendation**: Scan for these verbatim strings — if any are present, revise the sentence:
- `"the team should consider"`
- `"it would be reasonable to"`
- `"it may be worth"`
- `"one option would be"`
- `"the signals suggest that"`
- `"based on available evidence"`
- `"might be"`
- `"could potentially"`

The recommendation owns the decision. It does not assign the decision to the reader.

---

### ARTIFACT OUTPUT

Write the artifact in the template structure defined by the labeled fields in Layer 2. Save to:

`simulations/topic/story/{{topic}}-story-{{date}}.md`
