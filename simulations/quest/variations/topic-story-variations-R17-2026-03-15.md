## Quest Variate — `topic-story` Round 17

**Rubric:** v16 | **New criteria to address:** C-42 (genre frame as BLUF enforcer), C-43 (decision-flip conditional per uncertainty item)

---

## V-01: Genre Frame
**Axis:** Prompt register — genre contract replaces structural scaffolding
**Hypothesis:** Framing the output as an "editorial brief" (genre) rather than a labeled multi-role architecture eliminates the C-42 tension between "verdict first" instruction and structural heading placement. The genre carries the rule; no explicit BLUF instruction is needed.

```markdown
You are writing an editorial brief for the signal team. An editorial
brief opens with its verdict — before any structural framing — and
earns its conclusion through the evidence that follows.

Topic: {{topic}}
Date: {{date}}

Signals available:
{{signals}}

Write the brief with exactly these five sections:

## What we set out to understand
One or two sentences. The question the investigation was designed
to answer.

## What the signals revealed
One key finding per signal namespace represented. Not a summary —
what did this signal actually tell us?

## What the signals say together
The pattern. A synthetic claim derivable only by reading two or
more signals together. Name the relationship, tension, or gap.
A sentence supportable by any single signal alone fails.

## What remains uncertain
Each open question as a binary conditional:
If [question] resolves [one way], the verdict holds.
If [question] resolves [the other way], the verdict changes to
[alternative].
One conditional per uncertainty item.

## The recommendation
Proceed / Pause / Pivot / Abandon with one sentence of
justification tied to the pattern named above.

The brief opens with its verdict. The first line of your output
is the recommendation sentence — before any section heading.
```

---

## V-02: Decision-Flip Conditional
**Axis:** Uncertainty format — explicit flip-test template per item
**Hypothesis:** Providing a structured template ("If A → holds; if B → flips to X") for each uncertainty item will reliably produce C-43-compliant output without requiring the model to derive the binary conditional structure on its own.

```markdown
You are the synthesist for the {{topic}} investigation. Produce the
Signal story artifact — an editorial synthesis in the author's voice,
not a summary of findings.

Topic: {{topic}}
Date: {{date}}

Signals available:
{{signals}}

Produce a story artifact with these five labeled beats:

**What we set out to understand**
The investigation question — one or two sentences.

**What the signals revealed**
For each signal namespace: one sentence naming the key finding.
Not exhaustive. What did this artifact actually show?

**What the signals say together**
The cross-signal pattern. State a claim referencing what two or
more signals show together that neither shows alone. Apply the
necessity test: if either referenced signal were removed, the
claim must fail. Name the relationship, tension, or gap.

**What remains uncertain**
List each open question in flip-test form:
- Uncertainty: [state the open question]
- If resolves as [A]: recommendation holds
- If resolves as [B]: recommendation changes to [alternative]

Do not write generic hedges. Every uncertainty item names the
question, both resolution branches, and what each branch means
for the verdict.

**The recommendation**
Proceed / Pause / Pivot / Abandon. One sentence of justification
referencing the pattern. Proportionality check: does this
recommendation match the evidence weight described above?

Open with the recommendation. The first substantive sentence of
your output states the verdict before any other content.
```

---

## V-03: Synthesis-First Role Sequence
**Axis:** Role sequence — pattern identification precedes section writing
**Hypothesis:** Forcing pattern identification as an explicit first step (before any section is written) will produce stronger C-03 and C-04 compliance by priming the model to read for connections rather than summarize sequentially. The pattern drives the sections; the sections do not generate the pattern.

```markdown
Topic: {{topic}}
Date: {{date}}

Signals available:
{{signals}}

You are writing a topic-story artifact. A topic-story is not a
summary. It is an editorial synthesis: what do the signals say
together that no single signal says alone?

--- STEP 1: Read for pattern ---

Before writing a word of the story, name the dominant cross-signal
pattern. Ask:
- Is there a tension between what users want and what the system
  can deliver?
- Is there a gap between expected and observed?
- Is there a convergence that resolves an earlier uncertainty?
- Is there a contradiction between two high-confidence signals?

State the pattern in one sentence. Then write the story from
that pattern outward.

--- STEP 2: Write the story ---

## What we set out to understand
The investigation question.

## What the signals revealed
One key finding per signal namespace. Not exhaustive.

## What the signals say together
The pattern from Step 1. Articulate the cross-signal claim.
Pass the necessity test: remove one referenced signal and the
claim must fail or become unprovable.

## What remains uncertain
Specific open questions only. For each, name:
- The question
- Which resolution holds the verdict
- Which resolution flips it

## The recommendation
Proceed / Pause / Pivot / Abandon, with one justification
sentence proportional to the evidence described above.

Output format: the first line is the recommendation verdict
sentence. The five sections follow.
```

---

## V-04: Structured Decision Card
**Axis:** Output format — tight card with constrained slots
**Hypothesis:** Hard slot constraints (sentence counts, bullet limits) will force proportionality (C-07) and eliminate padding, while the explicit VERDICT slot placed before any delimiter will satisfy C-40 without architectural-label conflict. The card format is a genre frame, not a role/part scaffold.

```markdown
Topic: {{topic}}
Date: {{date}}

Signals available:
{{signals}}

Produce a Signal Story in decision-card format. Each slot is
constrained — do not exceed the stated limits.

─────────────────────────────────────────
VERDICT  [1 sentence — absolute first line of output]
Proceed / Pause / Pivot / Abandon + the single most important
reason.
─────────────────────────────────────────
INVESTIGATION QUESTION  [1–2 sentences]
What were we trying to understand?
─────────────────────────────────────────
SIGNALS  [3–6 bullets, one per namespace]
• [Namespace]: [Key finding — 1 sentence]
─────────────────────────────────────────
THE PATTERN  [2–4 sentences]
The cross-signal synthesis. Name the relationship, tension, or gap
visible only when two or more signals are read together. Necessity
test: each referenced signal is a load-bearing premise — remove
it and the claim must fail.
─────────────────────────────────────────
OPEN QUESTIONS  [1–3 items, flip-test form]
[Question]:
  If [resolves as A] → verdict holds
  If [resolves as B] → verdict changes to [alternative]
─────────────────────────────────────────
RECOMMENDATION  [1 sentence]
Restate the verdict with proportionality check: does this match
the signal pattern above?
─────────────────────────────────────────
```

---

## V-05: Combined — Genre Frame + Flip-Conditional + Synthesis Primer
**Axis:** Multi-axis combination — genre contract (C-42) + flip-test template (C-43) + synthesis-first sequencing (C-03, C-04, C-41)
**Hypothesis:** Combining the genre frame (which carries the BLUF rule structurally), the explicit flip-test template (which produces binary conditionals per uncertainty), and the synthesis-identification primer (which ensures the pattern is necessity-tested before writing) will maximize scores across C-40, C-41, C-42, and C-43 simultaneously without mutual interference.

```markdown
Write an editorial brief for the {{topic}} investigation.

Topic: {{topic}}
Date: {{date}}

Signals available:
{{signals}}

An editorial brief in this genre:
- Opens with its verdict — the first line of output is the verdict
  sentence, before any heading or label
- Earns the verdict through synthesis, not summary
- Each uncertainty is a binary flip-test, not a generic hedge
- The pattern passes the necessity test: remove one signal and
  the claim fails

─── Before writing ───────────────────────────────────────────────

Identify the dominant cross-signal pattern. What do two or more
of these signals show together that neither shows alone? Name it.
Then write the brief from that pattern outward.

─── The brief ────────────────────────────────────────────────────

**What we set out to understand**
The investigation question in one or two sentences.

**What the signals revealed**
One key finding per signal type. Key finding, not summary.

**What the signals say together**
The pattern identified above. The cross-signal claim must be
false or unprovable if either of its referenced signals is
removed. Name the relationship, tension, or gap.

**What remains uncertain**
Each open question in flip-test form:
- If [X resolves as A]: the current verdict holds
- If [X resolves as B]: the verdict changes to [alternative]
No generic hedges. Every item maps both resolution branches to
verdict outcomes.

**The recommendation**
Proceed / Pause / Pivot / Abandon. One sentence of justification
tied directly to the pattern, proportional to the evidence weight
described above.

─── Genre rule ───────────────────────────────────────────────────

This artifact is an editorial brief. The genre carries its own
structure: a brief opens with its verdict. No architectural
labels, role headers, or part delimiters precede the verdict.
The first line of output is the verdict sentence.
```

---

**Variation summary:**

| Variation | Axis | Primary criteria targeted |
|-----------|------|--------------------------|
| V-01 | Genre frame replaces scaffold | C-42, C-40 |
| V-02 | Explicit flip-test template | C-43, C-06 |
| V-03 | Synthesis-identification before writing | C-03, C-04, C-41 |
| V-04 | Constrained card format | C-07, C-40 (slot placement) |
| V-05 | Combined: genre + flip + primer | C-40, C-41, C-42, C-43 |
