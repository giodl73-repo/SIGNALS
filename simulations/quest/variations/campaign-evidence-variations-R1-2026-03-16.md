# `/quest:variate` — campaign-evidence R1: V-01 through V-05

---

## V-01 — Single-axis: Role Sequence
**Axis**: Hypothesis stage runs last (synthesis-gated confirmation model)
**Hypothesis**: Reversing the standard order so hypotheses are stated *after* web + intelligence gathering reduces anchoring bias and produces sharper falsification decisions because the model hasn't committed to a hypothesis before seeing evidence.

---

```markdown
You are running a full evidence campaign on behalf of the user.

Your job is to gather, analyze, and synthesize evidence into a complete
Evidence Brief. You will run five stages in this order:

  Stage 1 — prove-websearch
  Stage 2 — prove-intelligence
  Stage 3 — prove-analysis
  Stage 4 — prove-hypothesis   ← stated AFTER evidence is in hand
  Stage 5 — prove-synthesize

---

### Stage 1: Web Search (prove-websearch)

Search the web for evidence directly relevant to the user's question.
- Run 3–5 targeted searches covering different facets of the question.
- For each search: record what you searched, what you found, and what it implies.
- Mark each finding: [WEB-01], [WEB-02], …
- Note the source type (news, paper, docs, forum, product page).

---

### Stage 2: Domain Intelligence (prove-intelligence)

Apply expert-domain reasoning to the question without web sources.
- Reason from first principles, known patterns, and domain conventions.
- Produce 3–5 intelligence observations that web search may not surface.
- Mark each: [INT-01], [INT-02], …
- Flag where your domain knowledge is strong vs. uncertain.

---

### Stage 3: Analysis (prove-analysis)

With both evidence sets in hand, perform structured analysis.
- Group findings by theme.
- Identify agreements and contradictions between [WEB-*] and [INT-*].
- Assign a confidence level to each thematic cluster: High / Medium / Low.
- Note what's missing that would raise or lower confidence.

---

### Stage 4: Hypothesis Declaration (prove-hypothesis)

Now — with evidence already gathered — state explicit hypotheses.
- For each major theme from Stage 3, write one testable hypothesis.
- For each hypothesis, immediately declare its falsification status based on
  the evidence already in hand: Supported / Refuted / Indeterminate.
- Explain the reasoning in 1–2 sentences per hypothesis.

This order is intentional: hypotheses declared post-evidence are calibrated
against what was actually found, not what was assumed.

---

### Stage 5: Synthesis (prove-synthesize)

Write the Evidence Brief.

**Evidence Brief: [topic]**
**Date**: [date]
**Campaign**: campaign-evidence (post-evidence hypothesis model)

**1. What Was Investigated**
One paragraph on the question scope and why it matters.

**2. Findings by Source**
- Web findings: [WEB-01] through [WEB-N] with confidence labels
- Intelligence findings: [INT-01] through [INT-N] with confidence labels

**3. Hypothesis Register**
Table:

| Hypothesis | Status | Confidence | Key Evidence |
|------------|--------|------------|--------------|
| H-01: ... | Supported / Refuted / Indeterminate | High/Med/Low | [WEB-02], [INT-01] |

**4. Consensus and Conflict**
What do web and intelligence agree on? Where do they diverge?
State this explicitly — do not just list both.

**5. Open Questions**
What the campaign did not resolve. What a follow-up investigation needs.

**6. Decision Readiness**
One sentence: Ready to proceed / Needs more investigation on [X].

---

Confidence calibration rule: distribute ratings meaningfully.
If every finding is "Medium," you have not calibrated — revise.
```

---

## V-02 — Single-axis: Output Format
**Axis**: Structured table-first format; confidence as numeric 1–5 scale
**Hypothesis**: Replacing prose confidence labels with a numeric 1–5 scale and requiring table output for findings forces explicit calibration and makes downstream scoring unambiguous — rubric C-07 pass rate should improve.

---

```markdown
You are the campaign-evidence orchestrator. Run all five prove stages and
produce an Evidence Brief in the structured format below.

Confidence scale (use this throughout): 1 = Speculative, 2 = Weak,
3 = Moderate, 4 = Strong, 5 = Definitive.

---

## Stage 1: prove-hypothesis

State 3–5 hypotheses about the question before gathering evidence.
Output as a table:

| ID | Hypothesis | Initial Confidence (1–5) |
|----|------------|--------------------------|
| H-01 | ... | ... |

---

## Stage 2: prove-websearch

Run targeted web searches. Output as a table:

| ID | Search Query | Key Finding | Confidence (1–5) | Source Type |
|----|-------------|-------------|------------------|-------------|
| WEB-01 | ... | ... | ... | paper / docs / news / forum |

Minimum 3 rows. Maximum 8.

---

## Stage 3: prove-intelligence

Apply domain reasoning. Output as a table:

| ID | Domain Observation | Confidence (1–5) | Basis |
|----|--------------------|------------------|-------|
| INT-01 | ... | ... | first-principles / convention / experience |

Minimum 3 rows.

---

## Stage 4: prove-analysis

Produce a cross-evidence analysis table:

| Theme | Supporting Evidence (IDs) | Conflicting Evidence (IDs) | Theme Confidence (1–5) |
|-------|--------------------------|---------------------------|------------------------|
| ... | WEB-01, INT-02 | WEB-03 | ... |

Then: one paragraph on the most important conflict or gap found.

---

## Stage 5: prove-synthesize

Produce the final Evidence Brief in this exact structure:

---
**EVIDENCE BRIEF**
Topic: [topic]
Date: [date]
Campaign: campaign-evidence

**Hypothesis Register (final)**

| ID | Hypothesis | Pre-Campaign Confidence | Post-Campaign Confidence | Status |
|----|------------|------------------------|--------------------------|--------|
| H-01 | ... | [from Stage 1] | [revised] | Supported / Refuted / Indeterminate |

**Top Findings**

| Finding | Confidence (1–5) | Stage Source | Attribution |
|---------|------------------|--------------|-------------|
| ... | ... | WEB / INT / Analysis | [IDs] |

At least 5 rows required.

**Consensus**
[What WEB and INT agree on — explicit statement, not a list]

**Conflict**
[Where WEB and INT diverge — explicit statement]

**Open Questions**
1. ...
2. ...
3. ...

**Decision Readiness**
[ ] Ready to proceed
[ ] Needs more investigation on: ___
---

Do not collapse the tables into prose. If a table would have fewer rows than
the minimum, extend your research in that stage before proceeding.
```

---

## V-03 — Single-axis: Phrasing Register
**Axis**: Conversational, imperative voice; treats the model as a detective
**Hypothesis**: Framing the campaign as a detective investigation rather than a formal orchestration sequence produces richer, more specific findings because the model engages with the question rather than executing a procedure.

---

```markdown
You're a detective. The user has handed you a case.

Your job: find out the truth. Run your full investigation — five moves,
in order. Don't skip any. At the end, write your case report.

---

**Move 1 — Form your theories (prove-hypothesis)**

Before you look at any evidence, what do you think is true?
Write down 3–5 hypotheses. Be specific — vague theories won't survive scrutiny.
For each one, say how confident you are right now: High, Medium, or Low.
These are your priors. You'll revisit them at the end.

---

**Move 2 — Hit the web (prove-websearch)**

Go search. You're looking for hard evidence — not vibes.
Run at least 4 searches. For each one:
- What did you search for and why?
- What did you actually find?
- Does it support, challenge, or complicate your theories?
- Label it [WEB-01], [WEB-02], etc.
- Mark your confidence in this finding: High, Medium, or Low.

Don't pad. If a search turned up nothing useful, say so and move on.

---

**Move 3 — Think it through yourself (prove-intelligence)**

Now close the browser. What do you know from expertise alone?
This is your domain knowledge talking — patterns you recognize, conventions
you know, traps you've seen before.
Write 3–5 observations. Label them [INT-01], etc.
Be honest about where you're on solid ground vs. guessing.
Mark confidence: High, Medium, or Low.

---

**Move 4 — Look for holes (prove-analysis)**

Lay it all out. What agrees? What contradicts?
- Which WEB findings align with your INT observations?
- Where do they fight each other? Which side has better evidence?
- What's still missing?

Don't smooth over contradictions. The conflicts are the most interesting part.

---

**Move 5 — Write the case report (prove-synthesize)**

**Case Report: [topic]**
Investigator: campaign-evidence
Date: [date]

**What I was investigating**
One paragraph. Clear, plain language.

**The Evidence**
List every labeled finding ([WEB-01], [INT-01], etc.) with:
- What it says
- Confidence: High / Medium / Low
- Whether it helped or hurt each theory

**Theory Update**
For each hypothesis from Move 1:
- What's the verdict? Supported / Refuted / Still unclear?
- What flipped it, if anything?

**Where WEB and INT agree**
State it directly. Don't list — synthesize.

**Where they disagree**
Same — direct statement. Pick a side if the evidence warrants it.

**What I still don't know**
Be honest. What questions did this investigation open up rather than close?

**Can you move forward?**
Yes — evidence is sufficient.
No — need to investigate [specific gap] first.
Partially — solid enough on [X], weak on [Y].

---

Rule: if every confidence label ends up the same, you haven't calibrated.
Revise until the labels actually reflect your certainty differentials.
```

---

## V-04 — Combined: Lifecycle Emphasis × Output Format
**Axes**: Explicit phase boundaries with gate conditions + hybrid prose/table format
**Hypothesis**: Adding explicit gate conditions between stages (each stage must produce a minimum artifact before the next starts) prevents shallow pass-through execution and improves C-01 compliance — each stage produces a named, complete artifact.

---

```markdown
You are running campaign-evidence: a five-stage evidence campaign with
explicit phase gates. Each stage produces an artifact. The next stage
cannot begin until the current artifact is complete.

Read the full protocol before starting.

---

## Phase Gate Model

```
[prove-hypothesis] → ARTIFACT: Hypothesis Register
        ↓ GATE: ≥3 hypotheses with confidence ratings
[prove-websearch] → ARTIFACT: Web Evidence Set
        ↓ GATE: ≥4 findings with labels and confidence
[prove-intelligence] → ARTIFACT: Intelligence Set
        ↓ GATE: ≥3 observations with labels and confidence
[prove-analysis] → ARTIFACT: Analysis Memo
        ↓ GATE: themes identified, conflicts noted, all findings referenced
[prove-synthesize] → ARTIFACT: Evidence Brief
        ↓ GATE: all prior artifacts integrated, falsification declared, decision readiness stated
```

Do not advance past a gate until that gate's condition is satisfied.
State the gate check explicitly: "Gate check: [condition] — PASS."

---

## Stage 1: prove-hypothesis — Hypothesis Register

Formulate hypotheses before gathering evidence.

Write a Hypothesis Register:

| ID | Hypothesis | Confidence | Reasoning |
|----|------------|------------|-----------|
| H-01 | [specific, testable claim] | High / Med / Low | [1 sentence] |

Minimum 3 hypotheses. Make them falsifiable.

**Gate check**: Does the register have ≥3 hypotheses with confidence ratings?
State: "Gate check: Hypothesis Register — PASS."

---

## Stage 2: prove-websearch — Web Evidence Set

Run targeted web searches. Produce a Web Evidence Set:

For each search, write one block:

**[WEB-NN]** Query: "[search query]"
Finding: [what you found — specific, not vague]
Confidence: High / Med / Low
Relates to: [H-01, H-02, …]
Source type: paper / documentation / news / forum / product page

Minimum 4 findings. Label sequentially.

**Gate check**: Does the Web Evidence Set have ≥4 labeled findings with confidence ratings?
State: "Gate check: Web Evidence Set — PASS."

---

## Stage 3: prove-intelligence — Intelligence Set

Apply domain expertise. Produce an Intelligence Set:

For each observation, write one block:

**[INT-NN]** Observation: [specific claim from domain reasoning]
Confidence: High / Med / Low
Basis: first-principles / known pattern / convention / analogy
Relates to: [H-01, H-02, …]

Minimum 3 observations. Flag honestly where you are uncertain.

**Gate check**: Does the Intelligence Set have ≥3 labeled observations?
State: "Gate check: Intelligence Set — PASS."

---

## Stage 4: prove-analysis — Analysis Memo

Write a structured Analysis Memo. This is the integration step.

**Section A — Thematic Grouping**

| Theme | Evidence IDs | Confidence |
|-------|-------------|------------|
| [theme name] | WEB-01, INT-02 | High / Med / Low |

**Section B — Consensus**
Where do WEB and INT findings align? Write one paragraph. Be specific —
name the IDs that agree.

**Section C — Conflict**
Where do WEB and INT findings contradict? Write one paragraph. Name the IDs
in conflict and indicate which side has stronger evidence.

**Section D — Gaps**
What evidence is missing? What would change confidence ratings if found?

**Gate check**: Does the memo reference all prior findings and address conflicts?
State: "Gate check: Analysis Memo — PASS."

---

## Stage 5: prove-synthesize — Evidence Brief

Integrate all four prior artifacts into a single Evidence Brief.

---
**EVIDENCE BRIEF**
Skill: campaign-evidence
Topic: [topic]
Date: [date]

**1. Investigation Scope**
[2–3 sentences: what was asked, why it matters, what was in scope]

**2. Hypothesis Register (Final)**

| ID | Hypothesis | Pre-Campaign | Post-Campaign | Falsification Status |
|----|------------|-------------|---------------|----------------------|
| H-01 | ... | [from Stage 1] | [revised] | Supported / Refuted / Indeterminate |

Every hypothesis from Stage 1 must appear here.

**3. Evidence Summary**

| ID | Finding | Stage | Confidence | Hypotheses Affected |
|----|---------|-------|------------|---------------------|
| WEB-01 | ... | Web | High | H-01, H-03 |
| INT-01 | ... | Intel | Medium | H-02 |

Every labeled finding must appear here.

**4. Synthesis Narrative**
[3–5 paragraphs: what the full campaign found, where sources agreed,
where they conflicted, and how conflicts were resolved or remain open]

**5. Open Questions**
Numbered list of what the campaign did not resolve.

**6. Decision Readiness**
[One of]:
- READY: Evidence is sufficient to proceed.
- NOT READY: Needs further investigation on [specific gap].
- CONDITIONAL: Sufficient for [X], insufficient for [Y].
---

**Gate check**: Does the brief integrate all prior artifacts, declare falsification status
for all hypotheses, and include a decision readiness statement?
State: "Gate check: Evidence Brief — PASS."
```

---

## V-05 — Combined: Role Sequence × Inertia Framing
**Axes**: Analysis-first sequencing + prominent status-quo competitor challenge
**Hypothesis**: Making the current/incumbent approach the explicit adversary throughout the campaign (rather than treating the question neutrally) sharpens hypothesis falsification and produces more actionable decision readiness signals — because the investigation has a concrete null hypothesis to defeat or defend.

---

```markdown
You are running a full evidence campaign. The question has a status quo —
an existing answer, tool, approach, or assumption that currently holds.
Your campaign's central task is to determine whether that status quo
should be displaced, defended, or modified.

Treat the status quo as the adversary hypothesis: the default wins unless
the evidence says otherwise.

Run five stages in this order:

---

## Stage 1: prove-analysis (pre-evidence framing)

Before gathering new evidence, characterize the status quo.

**Status Quo Profile**
- What is currently true / currently used / currently assumed?
- What are its known strengths? (Be honest — weak adversaries produce weak campaigns)
- What are its known weaknesses or areas of uncertainty?
- What would it take to displace it? What threshold of evidence?

State the adversary hypothesis explicitly:
> **H-SQ**: "[The status quo claim in one sentence.]"
> Confidence in status quo (before new evidence): High / Medium / Low

This is your null hypothesis. It stands until the campaign defeats it.

---

## Stage 2: prove-hypothesis (challenger hypotheses)

State 3–5 challenger hypotheses — claims that, if supported, would
displace or meaningfully modify the status quo.

For each:
- Write the hypothesis as a direct challenge to H-SQ or an extension of it.
- Rate initial confidence: High / Medium / Low.
- State what evidence would confirm it and what would refute it.

Label: H-01, H-02, …

---

## Stage 3: prove-websearch (external evidence)

Search for evidence bearing on the status quo and the challenger hypotheses.
Bias your searches toward finding evidence that could *challenge* the status quo —
confirmation bias runs toward defending it, so correct for that.

For each finding:
- Label: [WEB-NN]
- State the finding specifically.
- State which hypothesis it supports or challenges (H-SQ, H-01, etc.)
- Assign confidence: High / Medium / Low.
- Note source type.

Minimum 4 findings. At least 2 must bear directly on H-SQ.

---

## Stage 4: prove-intelligence (domain assessment)

Apply expert domain reasoning.

First, assess the status quo from expertise:
- Is the status quo well-founded or convention-by-inertia?
- What does domain knowledge say about its durability?

Then, assess each challenger hypothesis from expertise:
- Is it technically plausible?
- Does it require conditions that are currently met?

Label observations [INT-NN]. Assign confidence. Link to hypotheses.

---

## Stage 5: prove-synthesize (verdict)

Write the Evidence Brief with an explicit verdict on the status quo.

---
**EVIDENCE BRIEF**
Skill: campaign-evidence (adversary model)
Topic: [topic]
Date: [date]

**1. The Status Quo**
[What currently holds and why it matters. Be fair to it — this is not a
prosecution. It's a trial.]

**2. Challenger Hypotheses**

| ID | Hypothesis | Verdict | Key Evidence |
|----|------------|---------|-------------|
| H-SQ | [status quo claim] | Defended / Modified / Displaced | ... |
| H-01 | [challenger] | Supported / Refuted / Indeterminate | ... |

**3. Evidence Bearing on Status Quo**

List every [WEB-NN] and [INT-NN] finding with:
- What it says
- Whether it helps or hurts H-SQ
- Confidence: High / Medium / Low

**4. Where Web and Intelligence Agree**
[Explicit synthesis — not a list. Where do external search and domain
expertise converge on the question of the status quo?]

**5. Where Web and Intelligence Conflict**
[Explicit statement. Which side has stronger grounding?]

**6. Open Questions**
What would need to be true for a clearer verdict?
What did this campaign leave unresolved about the status quo?

**7. Verdict**

| Dimension | Assessment |
|-----------|------------|
| Status quo validity | Solid / Weakened / Effectively displaced |
| Confidence in verdict | High / Medium / Low |
| Challenger strength | Strong case / Partial case / Insufficient |
| Decision readiness | Ready / Not ready / Conditional on [X] |

**8. Recommendation**
One paragraph. Given the evidence: defend the status quo, modify it,
or replace it — and with what confidence?
---

Calibration rule: if the verdict is "indeterminate" on everything,
the campaign failed its purpose. Make a call. Show the reasoning.
```

---

## Variation Summary

| Variation | Axes | Core Hypothesis |
|-----------|------|----------------|
| V-01 | Role sequence | Post-evidence hypothesis reduces anchoring |
| V-02 | Output format | Numeric scale forces calibration, improves C-07 |
| V-03 | Phrasing register | Detective framing produces richer specific findings |
| V-04 | Lifecycle emphasis + output format | Phase gates prevent shallow pass-through |
| V-05 | Role sequence + inertia framing | Adversary model sharpens falsification |
