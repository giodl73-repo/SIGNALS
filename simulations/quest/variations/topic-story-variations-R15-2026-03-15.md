# Quest Variations — `topic-story` Round 15

**Rubric version:** v14 (39 criteria, C-39 new: Analyst/Author role sequence)
**Variation strategy:** V-01 and V-02 are single-axis (role sequence, output format). V-03 is single-axis (lifecycle emphasis). V-04 and V-05 are combinations.

---

## V-01 — Axis: Role sequence | Hypothesis: Explicit named Analyst→Author pipeline enforces C-39 most directly

The two-role model with a hard handoff prevents any narrative from beginning until all pre-composition blocks are complete. The analyst is explicitly prohibited from writing prose; the author is explicitly prohibited from revising the brief.

```
You are running a two-role synthesis pipeline. Complete the Analyst role in full
before the Author role begins a single sentence of narrative.

---

## ROLE 1: ANALYST

You are not writing a story. You are building the brief the author will work from.
Complete all four blocks now.

**BLOCK D — Signal inventory**
List every signal artifact you are drawing from.
Format: `[namespace] / artifact-name — one-sentence finding`
Minimum three rows from distinct namespaces.

**BLOCK P — Pattern claim**
State the cross-signal pattern in one to three sentences. It must name a
relationship, tension, or gap that two or more signals show together and that
no single signal shows alone. Label it:

  Pattern: [your claim here]

The pattern must be falsifiable by removing a signal: if you could derive it
from any single artifact, rewrite it.

**BLOCK B — Verdict**
State the recommendation verb and one-sentence rationale. Choose one verb:
proceed / pause / pivot / abandon.

  Verdict: [verb] — [one sentence derived from BLOCK P]

**LEDGER — Uncertainty inventory**
List each open question that, if resolved, would change the recommendation.
For each item, state:
  - The question precisely
  - If it resolves one way: recommendation shifts to [verb]
  - If it resolves the other way: recommendation holds at [verb] or shifts to [verb]

Minimum two items. "More research may be needed" is not an acceptable entry.
Each item must name a specific resolvable question with a directional consequence.

---

## ROLE 2: AUTHOR

The Analyst's output above is your complete brief. Do not revise it, extend it,
or derive new analytical claims during writing. Write the narrative now.

**Placement rule:** Before the first section heading, output the verdict as a
standalone callout:

  **Verdict:** [verb from BLOCK B] — [rationale from BLOCK B]

Then write the five-beat story with exactly these labeled sections:

**What we set out to understand**
One paragraph. The question or decision this topic was investigating.

**What the signals revealed**
One paragraph per major signal. Lead with the finding, not the artifact name.
What did this signal add that the others could not provide alone?
Include at least one contrastive statement — "we expected X but found Y" —
drawn from a genuine surprise in the signal record.

**What the signals say together**
Open with the Pattern from BLOCK P, stated verbatim or near-verbatim.
Explain why the pattern holds only across multiple signals: what disappears
if any single signal is removed. One to two paragraphs. Do not introduce a
new analytical claim here — use what the Analyst identified.

**What remains uncertain**
Convert the LEDGER to prose. Preserve the directional framing for each item:
state what would change about the recommendation if the uncertainty resolves
against you.

**The recommendation**
Restate the verdict from BLOCK B, expanded to name:
  - The decision-maker role (not a person — a role)
  - The constraint under which the recommendation holds
  - The primary uncertainty from the LEDGER that, if it resolves badly,
    invalidates the recommendation

This section is a directive to a decision-maker. It is not a finding or
a summary of evidence.
```

---

## V-02 — Axis: Output format | Hypothesis: Fill-in-the-blank block templates enforce pre-composition structurally without requiring named roles

Rather than assigning work to roles, this variation provides hard-edged templates that must be populated before narrative begins. The structural constraint does the enforcement work that named roles do in V-01.

```
Write a topic story. A topic story is an editorial synthesis in the author's voice
— not a summary of signals, not a list of findings. It interprets what the signals
say together.

Before writing any narrative, complete the four pre-composition tables below.
These are analytical working documents, not prose. They must be fully populated
before you write a single narrative sentence.

---

### PRE-COMPOSITION BLOCKS

**BLOCK D: Evidence base**

| Namespace | Artifact | Key finding (one sentence) |
|-----------|----------|---------------------------|
|           |          |                           |
|           |          |                           |
|           |          |                           |

Minimum three rows from distinct namespaces. Add rows as needed.
Mark load-bearing signals with * in the Namespace column.

**BLOCK P: Cross-signal pattern**

Complete this sentence and stop:

  The pattern across signals: ___

The blank must name a relationship, tension, or gap. It must require at least
two signals to be true. Test: if any single signal were removed, would the
claim still hold? If yes, rewrite it — it is not a cross-signal pattern.

**BLOCK B: Verdict**

  [proceed / pause / pivot / abandon] — [one sentence rationale from BLOCK P]

The rationale must cite the pattern, not restate a single signal finding.

**LEDGER: Open questions**

| Question | If resolves toward A | If resolves toward B |
|----------|---------------------|---------------------|
|          | recommendation: [verb] | recommendation: [verb] |
|          | recommendation: [verb] | recommendation: [verb] |

Minimum two rows. Each question must be specific and resolvable in principle.
Generic uncertainty ("we need more data") fails.

---

### NARRATIVE

The blocks are complete. Write the story.

**First line of output** (before any section heading):

  **Verdict:** [verb from BLOCK B] — [rationale from BLOCK B]

Then the five sections:

**What we set out to understand**
The question or decision this topic was investigating. One paragraph.

**What the signals revealed**
One paragraph per major signal. Key finding per signal, not an exhaustive
account. Include at least one explicit contrastive statement:
"We expected [X]. We found [Y]."

**What the signals say together**
Open with the pattern from BLOCK P verbatim. Then make the case for why it
is a synthesis: show what disappears if a signal is removed.

**What remains uncertain**
Render the LEDGER as prose. Preserve directional framing: for each item,
state which way the recommendation would move if the uncertainty resolves
against the current verdict.

**The recommendation**
State: who is deciding (role), under what constraint, and what the directive
is. Derive the directive explicitly from BLOCK P and BLOCK B.
Format: "A [role] deciding [decision] should [verb] because [pattern claim].
This holds unless [primary LEDGER item] resolves against it."
```

---

## V-03 — Axis: Lifecycle emphasis | Hypothesis: Foregrounding the uncertainty and delta beats closes the most common gaps in C-09 and C-12

Most story prompts treat uncertainty as a brief closing beat. This variation makes it the heaviest-weighted section with the most instruction space, and treats delta surfacing as a first-class pre-composition step rather than an optional flavor element.

```
Write a topic story: an editorial synthesis interpreting what the gathered signals
say together. This is not a summary. Every section has a specific job; the jobs
are not interchangeable.

---

## BEFORE YOU WRITE

Complete these analytical steps as labeled blocks. Do not begin narrative prose
until all four are done.

**Evidence inventory**
List every signal artifact you are drawing from, grouped by namespace. Mark with *
the signals that the cross-signal pattern depends on most heavily.

**Cross-signal pattern**
In one sentence, state what the signals reveal together that no single signal
reveals alone. Label it: `Pattern: ___`
This is your thesis. The entire narrative serves it.

**Delta log**
Go through each major signal. For each, answer: did it confirm, surprise, or
contradict what you expected going in? Collect the surprises. Format:
  Expected: [X]
  Found: [Y]
You need at least one genuine surprise. If none exist, examine your priors
more carefully — the absence of surprise often reflects a failure to form
an expectation, not a lack of delta.

**Uncertainty audit**
List every open question that, if resolved against the current verdict, would
change the recommendation. For each:
  - State the question precisely (not a category — a specific question)
  - State which direction the recommendation shifts if it resolves against you
  - State what it would take to resolve it

Apply this filter: if "more data" does not specify what data, what experiment,
or what threshold, it fails. Each uncertainty must be resolvable in principle.

---

## NARRATIVE

**Verdict line** — first line of output, before sections:

  **Verdict:** [proceed / pause / pivot / abandon] — [one sentence]

**What we set out to understand**
The question or decision driving this investigation. One paragraph.
Name the status quo this work was interrogating.

**What the signals revealed**
What each major signal contributed. Lead each paragraph with the finding,
not the artifact name. Use at least one entry from your delta log: report
the surprise, not the expectation.

**What the signals say together**
Open with the Pattern verbatim. Show why it holds only across signals.
One to two paragraphs. No new analytical claims — use what you identified above.

**What remains uncertain** [this section carries the most weight]
Convert your uncertainty audit to prose. For each item, you must include:
  1. The precise question
  2. What resolving it would change about the recommendation (direction and verb)
  3. What it would take to resolve it

Aim for two to four items. One well-specified uncertainty is worth more than
five vague ones. Do not end this section with a general hedge. End it by naming
the single uncertainty that most threatens the current recommendation.

**The recommendation**
Lead with the verdict verb. Then:
  - Name the decision-maker by role, not by name
  - State the constraint under which the recommendation holds
  - Name the primary uncertainty from the audit that, if resolved badly,
    invalidates it
  - State what "resolved badly" means concretely

This is a directive to a decision-maker. "The signals suggest X" is a finding,
not a recommendation.
```

---

## V-04 — Combination: Role sequence + phrasing register | Hypothesis: Detective/journalist framing creates the most intuitive mental model for the analyst→author handoff, lowering failure rate on C-39 through metaphor rather than instruction

The detective metaphor encodes role separation procedurally: detectives build case files; journalists write stories. The two roles never swap. The framing also carries the formal/precise register into the analytical phase without sounding bureaucratic.

```
This is a two-phase synthesis. Phase 1 is investigation. Phase 2 is writing.
The investigator does not write stories. The journalist does not gather evidence.
Complete Phase 1 before beginning Phase 2.

---

## PHASE 1: INVESTIGATION (Detective role)

You are building a case file. Your job is to determine what the evidence shows.
Narrative interpretation begins in Phase 2. Not here.

**EXHIBITS**
List every signal you are working from. Format:

  Exhibit A: [namespace] / [artifact name] — [finding in one sentence]
  Exhibit B: [namespace] / [artifact name] — [finding in one sentence]
  ...

Include at least three exhibits from distinct namespaces.
Mark pivotal exhibits — the ones the charge depends on — with ★.

**THE CHARGE**
In exactly one sentence, state what the exhibits collectively demonstrate that
no single exhibit demonstrates alone. Use precise, declarative language.
This is your synthesis claim.

  The charge: ___

Test: could you derive the charge from any single exhibit? If yes, rewrite it.

**THE VERDICT**
Based on the charge, state the recommendation.

  Verdict: [proceed / pause / pivot / abandon] — [one sentence rationale]

**REASONABLE DOUBT**
What would a skeptic challenge? List each objection that, if sustained, would
overturn or weaken the verdict. For each challenge:
  - State it precisely
  - State what it would take to resolve it
  - State whether resolving it would sustain or overturn the verdict

**DELTA LOG**
Where did the evidence surprise you? List cases where a signal showed something
other than what you expected going in.

  Expected: [X]
  Found: [Y]

At least one entry required. If you cannot identify a surprise, examine whether
you formed an expectation before reading each signal.

---

## PHASE 2: WRITING (Journalist role)

The case file is closed. You are not a detective now. Write the story.
Your only permitted source for analytical claims is the case file above.
Do not derive new conclusions during writing.

**PLACEMENT RULE**
Before any narrative text, output the verdict as a standalone callout:

  **Verdict:** [verb] — [rationale from the case file]

Then the five-beat story:

**What we set out to understand**
The question this investigation was answering. One paragraph, tight.

**What the signals revealed**
Report the pivotal exhibits (★) first. What did each contribute that the others
could not? Use at least one finding from the delta log — report the surprise,
not just the finding.

**What the signals say together**
Open with the charge from the case file, stated verbatim. Walk the reader through
why the charge requires more than one exhibit to be true. One to two paragraphs.

**What remains uncertain**
Convert the reasonable-doubt list to prose. Each item must state the direction
the verdict would move if the challenge were sustained.

**The recommendation**
Name the role making the decision. State the constraint it operates under.
Restate the verdict with the charge as its explicit stated basis. Name the
primary doubt that, if sustained, changes the verdict. This is a directive.
```

---

## V-05 — Combination: Role sequence + inertia framing | Hypothesis: Anchoring the analyst phase to a status quo baseline forces proportionality (C-07) and accountability (C-13) structurally, not through instruction

Every feature decision is ultimately "this vs. doing nothing." Making the status quo an explicit analytical object in the analyst phase means the pattern claim and verdict must engage with it — not just describe what signals showed.

```
Produce a topic story: an editorial synthesis of gathered signals that answers
one question all signal work is ultimately about — is this feature worth doing
instead of doing nothing?

Complete the Analyst phase before beginning the Author phase.

---

## ANALYST PHASE

You are not writing a story. You are building the brief. Complete all five blocks.

**BLOCK D — Signal register**
List every signal you are drawing from. Include namespace and key finding.
Mark the three signals with the highest bearing on the decision with ★.

**BLOCK S — Status quo baseline**
Describe the current state of the system, workflow, or capability this feature
would change, in two to three sentences. Be specific: what does the user do
today, and at what cost? This is the competitor. The decision is always
this feature versus continuing to do this.

**BLOCK P — Pattern claim**
State the cross-signal pattern in one sentence. The pattern must explain how
the signals relate to the status quo: does the evidence show the feature
meaningfully improves on it, fails to, or is ambiguous?

  Pattern: ___

The pattern must name a relationship across at least two signals. It must
take a position on the status quo delta: closing it, widening it, or
revealing there is no gap.

**BLOCK B — Verdict**
  [proceed / pause / pivot / abandon] — [one sentence linking BLOCK P to BLOCK S]

The rationale must name the status quo explicitly. "The signals suggest X"
is not a rationale. "Given [status quo], the pattern shows [X], so [verb]" is.

**LEDGER — Uncertainty register**
For each open question, state:
  - The question
  - How it relates to the status quo baseline
  - If it resolves one way: recommendation shifts to [verb]
  - If it resolves the other way: recommendation holds at [verb] / shifts to [verb]

Minimum two items. Generic uncertainty fails.

---

## AUTHOR PHASE

The analyst's blocks are complete and closed. Write the narrative using only
what the blocks contain. Do not derive new analytical claims during authoring.

**First line of output** (before any section heading):

  **Verdict:** [verb from BLOCK B] — [rationale from BLOCK B]

**What we set out to understand**
The question and the decision context. Name the status quo this feature competes
with. One paragraph.

**What the signals revealed**
Key finding from each major signal. What did it add to the case? Include at
least one finding that surprised you — where the evidence departed from
expectation. State the surprise explicitly: "We expected [X]. We found [Y]."

**What the signals say together**
Open with BLOCK P verbatim. Show why the pattern holds only across multiple
signals. Then tie the pattern to the status quo: does the evidence show a
meaningful gap between current state and what this feature would provide?
One to two paragraphs.

**What remains uncertain**
Convert the LEDGER to prose. For each item, preserve the status-quo connection
and the directional framing: state which way the recommendation would move
if the uncertainty resolves against the current verdict.

**The recommendation**
Format: "A [decision-maker role] deciding whether to invest in [feature area],
given [status quo from BLOCK S], should [verb from BLOCK B] because [BLOCK P].
This holds unless [primary LEDGER item] resolves against it, in which case
the right move is [alternative verb]."

This is a directive to a decision-maker. It is not a summary of evidence.
```

---

## Summary

| Variation | Axis | C-39 mechanism | Key hypothesis |
|-----------|------|----------------|----------------|
| V-01 | Role sequence | Named roles, hard handoff, prohibition on cross-role work | Explicit prohibition is the strongest enforcement |
| V-02 | Output format | Populated tables must precede narrative section | Template structure does the role-separation work without named roles |
| V-03 | Lifecycle emphasis | Uncertainty/delta weighted as primary sections | Gap in C-09/C-12 is instruction space, not concept |
| V-04 | Role sequence + register | Detective/journalist metaphor encodes handoff intuitively | Metaphor lowers failure rate by making role separation memorable |
| V-05 | Role sequence + inertia | Status quo as explicit analytical object in analyst phase | Anchoring to status quo baseline auto-enforces C-07 and C-13 |
