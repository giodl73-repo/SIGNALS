## `topic-story` — V-01 through V-05 (Round 16)

---

## V-01 — Role Sequence: Analyst Extract → Author Synthesize

**Variation axis:** Role sequence
**Hypothesis:** Forcing an explicit per-signal extraction table before synthesis prevents the author from skipping per-signal work and producing hollow cross-signal claims. The analyst role creates a forcing function: you cannot synthesize what you haven't extracted.

---

```
You are running the `topic-story` skill for the topic: {{topic}}.

---

### ROLE 1: ANALYST — Signal Extraction

Read all signal artifacts available for this topic. Your job is extraction, not interpretation.

For each signal namespace you find evidence for, fill one row:

| Namespace | Artifact type | Key finding (one sentence: what this revealed) | Direction |
|-----------|--------------|------------------------------------------------|-----------|
| scout     | ...           | ...                                            | supports / complicates / neutral |
| draft     | ...           | ...                                            | supports / complicates / neutral |
| flow      | ...           | ...                                            | supports / complicates / neutral |
| trace     | ...           | ...                                            | supports / complicates / neutral |
| prove     | ...           | ...                                            | supports / complicates / neutral |
| listen    | ...           | ...                                            | supports / complicates / neutral |
| program   | ...           | ...                                            | supports / complicates / neutral |
| topic     | ...           | ...                                            | supports / complicates / neutral |

Only include rows where you have actual evidence. Omit empty rows. Three or more rows required
for the synthesis to be credible.

Do not interpret, synthesize, or recommend yet. Stop here.

---

### ROLE 2: AUTHOR — Story Synthesis

You have the signal extraction table from ROLE 1. Now write the topic story.

ABSOLUTE RULE: Your first output line — before any heading, section label, or preamble —
must be the verdict. Format:
  [PROCEED / PAUSE / PIVOT / ABANDON]: [one sentence reason].

Then write the five-beat narrative:

**What we set out to understand**
One to three sentences. What was the decision question or hypothesis this topic was
investigating?

**What the signals revealed**
One sentence per namespace row from the extraction table. Not a re-summary of the artifact —
the finding that bears on the decision.

**What the signals say together**
State the pattern, tension, or gap that emerges from holding two or more signals together.
Apply the necessity test: remove either signal you reference and the claim must become false
or unprovable. A claim supportable by a single signal fails. A list of findings
("Signal A showed X and Signal B showed Y") fails — name the synthetic claim that requires
both.

**What remains uncertain**
Name at least one specific open question where: (a) the answer is not knowable from current
signals, and (b) if resolved differently, the recommendation would change.
Do not write generic hedges. "More research may be needed" fails.
Name what research, what it would resolve, what the decision implication is.

**The recommendation**
Restate the verdict from your first line. Add: the conditions under which you would reverse
it. The recommendation weight must be proportional — strong positive signals → proceed;
mixed → pause; conflicting → pivot; weak or negative → abandon.
```

---

## V-02 — Output Format: Decision Card + Narrative

**Variation axis:** Output format
**Hypothesis:** Opening with a compact structured decision card before prose forces precision in the verdict and creates an anchor the narrative must remain internally consistent with. Separating "what do we conclude" from "how do we argue it" prevents the story from building toward a conclusion rather than defending one.

---

```
You are running the `topic-story` skill for the topic: {{topic}}.

Your output has two parts: a DECISION CARD and a STORY. Write the DECISION CARD first.

---

### PART 1: DECISION CARD

Fill every field. This is the first thing the reader sees.

  VERDICT:       [PROCEED / PAUSE / PIVOT / ABANDON]
  CONFIDENCE:    [HIGH / MEDIUM / LOW]
  KEY SIGNAL:    [The single signal most driving the verdict — namespace + one-sentence finding]
  PATTERN:       [One sentence: what the signals say together that no single signal says alone]
  TOP RISK:      [The one thing most likely to make this verdict wrong]
  SIGNALS USED:  [Namespaces drawn from, e.g.: scout, flow, trace]

---

### PART 2: STORY

Write the five-beat narrative. The DECISION CARD is locked — the story must be consistent
with it. Do not re-open the verdict question inside the narrative.

**What we set out to understand**
What decision question or hypothesis was this topic investigating? One to three sentences.

**What the signals revealed**
For each namespace in SIGNALS USED: one sentence, the key finding. Not a re-summary — the
finding that matters for the verdict. Cover at least three namespaces.

**What the signals say together**
Expand the PATTERN from the Decision Card into a paragraph. Apply the necessity test: the
claim must require at least two of your cited signals to be true. Remove either and the claim
must fail or become unsupported. Name which signals you are conjoining and why the
combination matters. A list of individual findings fails.

**What remains uncertain**
Name at least one specific open question: what it is, why current signals cannot answer it,
and how a different answer would change the verdict. Specific, not generic.

**The recommendation**
PROCEED / PAUSE / PIVOT / ABANDON — same as the Decision Card. State conditions that would
cause you to revise.
```

---

## V-03 — Phrasing Register: Editorial Voice

**Variation axis:** Phrasing register
**Hypothesis:** Framing the skill as an editorial assignment for a senior PM reduces formal hedging, produces more direct verdicts, and yields a stronger author's voice. The editorial frame makes the "build to a conclusion" anti-pattern harder to fall into because editorials do not end with their thesis.

---

```
You are a senior product writer for the {{topic}} feature. Your signals team has gathered
evidence across multiple namespaces. Your job: write the editorial brief that a principal PM
would send to leadership at the end of a discovery sprint.

Before you write a single word of the brief: write your verdict sentence on the very first
line. Then write the brief below it. The brief is the argument for the verdict, not a
journey toward it.

Verdict format:  [PROCEED / PAUSE / PIVOT / ABANDON]: [one sentence reason].

---

The brief has five sections. Write in the PM's editorial voice — direct, specific, no
hedging for hedging's sake.

**What we set out to understand**
What was the question driving this discovery sprint? What would a clean answer have unlocked?
One to three sentences.

**What the signals revealed**
Go namespace by namespace. For each area where you have evidence: what is the one finding
that changes how you think about the decision? Keep it tight — one sentence per area. Cover
at least three distinct evidence areas.

**What the signals say together**
This is the core of the brief. Name the pattern. Not "Signal A showed X and Signal B
showed Y" — name the synthetic claim that you can only make because you held both signals
at once. A reader who only had one signal could not have seen this. The pattern is the thing
this sprint discovered that would not have been visible without the full evidence base.
Apply the necessity test: if you remove either signal you are citing, the claim must fail.

**What remains uncertain**
Name the honest gap. At least one question that the signals do not answer, where the answer
genuinely matters: if it resolves one way, you stay with the verdict; if it resolves the
other, you change it. Do not give leadership generic caveats — give them the specific thing
to watch.

**The recommendation**
Write the closing recommendation as you would say it in a review meeting: proceed, pause,
pivot, or abandon, and the reason. Match the weight of the evidence — if the signals are
mixed, say so; if they are strongly positive, say that too. State what would cause you to
revise.
```

---

## V-04 — Lifecycle Emphasis: Phase Gates with Per-Section Constraints

**Variation axis:** Lifecycle emphasis
**Hypothesis:** Explicit per-section word/sentence budgets force attention discipline. The "signals revealed" section cannot become a dump that crowds out synthesis; the synthesis section cannot be a single sentence after a long summary. Hard caps per beat make each phase do its specific job.

---

```
You are running the `topic-story` skill for the topic: {{topic}}.

---

RULE ZERO: Write your verdict as the absolute first line of output.
No heading, no preamble, no role label above it.
Format:  [PROCEED / PAUSE / PIVOT / ABANDON]: [one sentence].

---

Write the five-beat story. Constraints are enforced per section.

---

BEAT 1 — What we set out to understand
Budget: 1–3 sentences. Hard cap.

State the decision question or hypothesis this topic was investigating. What would a
yes-or-no answer have allowed the team to do?

---

BEAT 2 — What the signals revealed
Budget: 1 sentence per namespace. Hard cap per namespace.

List the namespaces you have evidence for. For each: one sentence — the finding, not the
artifact summary. If you cannot state the finding in one sentence, you have not extracted
it yet; go back and extract it before writing. Cover at least three namespaces. Do not
explain methodology.

---

BEAT 3 — What the signals say together
Budget: 2–4 sentences. Must cite at least two namespaces by name.

State the pattern, tension, or gap that emerges from holding the signals together. Apply
the necessity test: the claim must require at least two of your cited signals to be true.
If you can make the same claim from any one signal alone, the claim is not a synthesis —
revise until it is. State the synthetic claim in the first sentence; support it in the
remaining sentences.

---

BEAT 4 — What remains uncertain
Budget: 1–3 sentences. Must name a specific open question.

Identify at least one open question that (a) current signals cannot answer, and (b) if
resolved differently, would change the recommendation. State the question. State the
decision implication. "More research may be needed" without specifying what and why fails.

---

BEAT 5 — The recommendation
Budget: 2–4 sentences.

Restate the verdict from Rule Zero. State the primary evidence that supports it. State the
conditions under which you would revise — what would have to change or be learned. Match
the recommendation weight to the evidence: strong positive → proceed; mixed → pause;
conflicting → pivot; weak or negative → abandon.
```

---

## V-05 — Combined: Inertia Framing + Necessity Test + Verdict-First

**Variation axes:** Inertia framing + necessity test + verdict-first discipline
**Hypothesis:** Making the status-quo competitor explicit — what is lost or risked if the team does not act on these signals — forces the recommendation to be comparative rather than merely affirmative. Combined with an explicit necessity test instruction, this produces better C-07 proportionality (the recommendation must be evidently preferable to a named alternative) and C-41 compliance (the synthesis must earn its cross-signal claim).

---

```
You are running the `topic-story` skill for the topic: {{topic}}.

The question this skill answers: given all the evidence gathered, what is the best
decision — and what are we risking by choosing it over the alternatives?

---

RULE: Write your verdict as the literal first line of your output.
Nothing above it — no role label, no heading, no preamble.
Format:  [PROCEED / PAUSE / PIVOT / ABANDON]: [one sentence why].

---

Now write the five-beat story:

**What we set out to understand**
What was the decision question? State it precisely. One to three sentences. Include: what
would "proceed" unlock, and what would continuing without a decision cost?

**What the signals revealed**
For each signal namespace in your evidence base, state the key finding in one sentence.
Do not summarize the artifact — extract the finding that bears on the decision. Cover at
least three distinct namespaces.

**What the signals say together**
State the pattern. The synthesis claim must satisfy two conditions:

  1. Cross-signal condition: it references what two or more signals show together that
     no single signal shows alone.
  2. Necessity test: remove either signal you cite and the claim must become false or
     unprovable. If the claim still holds on one signal alone, it is not a synthesis —
     revise.

Then name the inertia cost: what is lost or risked if the team continues without acting
on these signals? This makes the recommendation comparative: proceed over what?

**What remains uncertain**
Name at least one specific open question where: the current signals do not resolve it, and
a different answer would change the recommendation. State the question. State the
implication. Be specific.

**The recommendation**
Restate the verdict. Then state the status-quo alternative: what happens if the team
proceeds without this decision, or delays it. The recommendation should be evidently
preferable to the alternative — if it is not, revisit whether the verdict is correct.
State conditions for revision.
```

---

**Design notes across variations:**

| Variation | Primary lever | Key technique for C-40/C-41 |
|-----------|--------------|------------------------------|
| V-01 | Role sequence | Analyst table forces extraction before synthesis; verdict rule in Role 2 header |
| V-02 | Output format | Decision card locks verdict before prose; PATTERN field enforces necessity framing |
| V-03 | Phrasing register | Editorial frame makes "build to conclusion" unnatural; one-line verdict before brief |
| V-04 | Lifecycle emphasis | Hard budgets per beat prevent summary bloat; necessity test in Beat 3 constraints |
| V-05 | Inertia framing | Comparative framing (proceed over what?) anchors proportionality; explicit necessity test |
