# prove-synthesize — Variation Set R9

**Skill**: prove-synthesize
**Round**: 9
**Rubric**: v9 (C-32, C-33, C-34 targeted)
**Single-axis**: V-01, V-02, V-03
**Combined-axis**: V-04, V-05

---

## V-01 — Single Axis: Role Sequence (Verdict-First: SYNTHESIST → ADVERSARY → ANALYST)

**Axis**: Role sequence
**Hypothesis**: Front-loading the SYNTHESIST role forces a verdict commitment before adversarial exposure — the synthesist cannot pre-hedge in anticipation of challenges it hasn't seen yet.

---

```
# prove-synthesize

This synthesis is self-contained and supersedes all underlying investigation signals. A reader
with no access to the investigation artifacts must be able to understand the answer, the
confidence, and the reasoning. The synthesis supersedes every individual signal — it does not
summarize them. Issue a judgment; the signal inventory is now subordinate to this document.

---

## Cognitive Roles — Run in Order

### SYNTHESIST (runs first)

Your task: commit to a verdict before examining adversarial angles. State yes / no / maybe.
Assign a confidence from 0–100. Name the three signals that most influenced the verdict.
Name the strongest single counter-evidence entry.

Failure mode to foreclose: **hedging** (e.g., "on balance the evidence leans toward yes, though
meaningful uncertainty remains" — any sentence that refuses to land on yes, no, or maybe is not
a verdict; it is a summary dressed as a conclusion).

Gate: If your opening sentence does not contain yes / no / maybe and a numeric confidence, the
SYNTHESIST role is incomplete. Return and issue the verdict before continuing.

### ADVERSARY (runs second)

Your task: identify the exact structural vulnerability in the SYNTHESIST's verdict. What is the
weakest point in the evidence selection? What alternative explanation does the current synthesis
foreclose without justification?

Failure mode to foreclose: **generic challenge** (e.g., "more data would improve confidence" or
"the sample is limited" — name the exact vulnerability, e.g., "all three key signals come from
user interview artifacts; no instrumentation signal appears in the key evidence, so the verdict
rests entirely on self-report data").

Gate: If the challenge would apply verbatim to a different synthesis with different signals, the
challenge is generic. Sharpen it until it names a weakness specific to this evidence set.

### ANALYST (runs third)

Your task: adjudicate the ADVERSARY's challenge. Does it require a confidence revision? A
counter-evidence addition? A new open question? Apply the minimum change that addresses the
challenge. Do not re-run the SYNTHESIST verdict.

Failure mode to foreclose: **selective collection** (e.g., confirming the ADVERSARY's challenge
only when it supports the initial verdict and dismissing it when it complicates the verdict —
treat the challenge as evidence, not as a threat to defend against).

Gate: The ANALYST output must either (a) name a specific change to the synthesis with the reason,
or (b) explicitly rebut the ADVERSARY challenge by naming why the structural weakness does not
alter the verdict. An implicit dismissal fails this gate.

---

## Output Structure

Produce the synthesis in the following fixed order.

**Answer**: yes / no / maybe — one sentence stating the verdict and its direction.

**Confidence**: 0–100 — one sentence calibrating the score. Name what evidence would raise it;
name what evidence would lower it.

**Key Evidence**: The three signals that most influenced the answer. NOT: table format for this
section. The "Why this signal outranks the alternatives:" sub-item is required at each of the
three positions — naming what property of the signal made it rank above others that were
considered. Prose only; argument construction required.

**Counter-Evidence**: What argues against the verdict. One to two entries. Each entry names the
signal and states the specific reason it did not overturn the verdict.

**Principles Extracted**: What this investigation tells us beyond the specific hypothesis.
Minimum two principles. Each principle is stated as a transferable claim — applicable to a
different hypothesis on a different topic.

**Open Questions**: What the investigation did not resolve. Minimum one entry. Each entry names
the evidence that would resolve it.

---

## Self-Containment Check

Before finalizing, confirm a reader without the investigation artifacts can answer:
- What was the hypothesis?
- What is the verdict and confidence?
- What are the three strongest supporting signals?
- What is the strongest objection and why it did not prevail?

If any cannot be answered from this document alone, the synthesis is incomplete.
```

---

## V-02 — Single Axis: Output Format (Ranked-Argument Paragraphs, No Section Headers)

**Axis**: Output format
**Hypothesis**: Removing section headers and requiring flowing ranked-argument paragraphs forces the synthesist to argue the answer through prose construction rather than populate labeled containers — producing a more integrated synthesis.

---

```
# prove-synthesize

This synthesis supersedes all underlying investigation signals and is self-contained. It does not
summarize the signal inventory — it replaces the signal inventory as the authoritative record on
this hypothesis. A reader with no access to the investigation artifacts must be able to understand
the verdict, the confidence, the reasoning, and the limits of the reasoning from this document
alone.

---

## Cognitive Roles

Run all three roles before producing any output. Roles run concurrently in your reasoning;
the output produced afterward is a single document, not three labeled sections.

**ANALYST**: Your task is evidence selection and confidence calibration. Identify the three
signals that most influenced the verdict and the strongest counter-evidence. Failure mode to
foreclose: **selective collection** (e.g., building the signal set only from one investigation
track — e.g., three signals all sourced from user interviews with no instrumentation signal —
while signals from other tracks exist in the inventory but were not evaluated).

**ADVERSARY**: Your task is structural challenge. Name the exact vulnerability in the evidence
selection. Generic challenges are not permitted (e.g., "confidence could be higher with more
data" applies to every synthesis). A valid challenge names a specific weakness in this evidence
set (e.g., "the three key signals all measure stated preference, not observed behavior — the
synthesis has no revealed-preference signal in key evidence").

**SYNTHESIST**: Your task is verdict and supersession. Issue a yes / no / maybe verdict. Commit
to a confidence from 0–100. Issue the judgment. Failure mode to foreclose: **hedging** (e.g.,
"the evidence suggests yes but further investigation is warranted" — a sentence that defers
commitment is a refusal to synthesize; it is not a synthesis). The synthesis supersedes every
individual signal — it does not summarize them.

---

## Output Format

Produce a single continuous prose document. No section headers. No bullet lists. No tables.

**Paragraph 1 — Verdict**: Open with the verdict (yes / no / maybe) and confidence score in the
first sentence. The remainder of the paragraph calibrates confidence: what would raise it, what
would lower it, and why the current score reflects the evidence weight.

**Paragraph 2 — Key Evidence**: Present the three most influential signals as a ranked argument.
NOT: table format for this section. The "why this signal ranks above the one below it" bridge
sentence is required between each pair of ranked signals — the bridge makes the ranking a
reasoned argument, not a list. Each signal is named and its contribution to the verdict is
stated. Prose argument construction required; enumerated lists are not permitted.

**Paragraph 3 — Counter-Evidence**: Present the strongest evidence against the verdict. Name the
signal. State the specific reason it did not overturn the verdict. If the ADVERSARY identified
a structural vulnerability during role processing, address it here.

**Paragraph 4 — Principles**: Extract minimum two transferable principles — claims that would
apply to a different hypothesis on a different topic. State each as a declarative sentence.
Explain briefly why this investigation surfaces the principle.

**Paragraph 5 — Open Questions**: State minimum one open question. Name the evidence that would
resolve it. If the question was raised by the ADVERSARY challenge, acknowledge that.

---

## Self-Containment Check

The document is complete when a reader who has never seen the investigation artifacts can answer:
what was the hypothesis, what is the verdict, what are the three strongest signals, what argues
against, and what remains unresolved. If any of these cannot be answered from the prose alone,
the synthesis is incomplete.
```

---

## V-03 — Single Axis: Lifecycle Emphasis (Explicit Phase Markers with Word-Count Envelopes)

**Axis**: Lifecycle emphasis
**Hypothesis**: Marking phase boundaries explicitly (GATHER → CHALLENGE → COMMIT) with word-count envelopes forces a disciplined progression from evidence to verdict — preventing the synthesist from collapsing all phases into a single undifferentiated judgment pass.

---

```
# prove-synthesize

This synthesis is self-contained and supersedes all underlying investigation signals. It does not
integrate or aggregate the signal inventory — it displaces the signal inventory as the
authoritative record on this hypothesis. A reader without access to the investigation artifacts
must be able to understand the verdict and reasoning from this document alone.

---

## Phase Structure

The synthesis runs in three phases. Complete each phase before entering the next. The phases are
not output sections — they are reasoning stages. Only Phase 3 produces output.

---

### PHASE 1 — GATHER (internal, no output)

Role: **ANALYST**
Task: Identify and rank all signals relevant to the hypothesis. Select the three that most
influenced the verdict. Identify the strongest counter-evidence. Assign a preliminary confidence
from 0–100.

Failure mode to foreclose: **selective collection** (e.g., evaluating only signals from the most
recent investigation round while ignoring earlier rounds that produced conflicting findings —
a collection is complete only when signals that contradict the current confidence estimate have
been evaluated and either included in counter-evidence or explicitly set aside with a reason).

Gate: PHASE 1 is complete when you can name: (a) three key signals by name and their verdict
direction, (b) one counter-evidence entry by name, (c) a preliminary confidence score. If any
of these is missing, PHASE 1 is incomplete.

---

### PHASE 2 — CHALLENGE (internal, no output)

Role: **ADVERSARY**
Task: Challenge the ANALYST's evidence selection. Name the exact structural vulnerability.

Failure mode to foreclose: **generic challenge** (e.g., "the evidence base is limited" or "sample
size may affect confidence" — name the exact vulnerability, e.g., "all three key signals measure
adoption intent, not adoption behavior; the synthesis has no signal that observed users actually
completing the workflow end-to-end").

Gate: The challenge names a specific weakness in this evidence set — a weakness that would not
apply verbatim to a synthesis built from a different hypothesis. If the challenge is generic,
sharpen it before advancing to PHASE 3.

---

### PHASE 3 — COMMIT (produces output)

Role: **SYNTHESIST**
Task: Issue the verdict. Incorporate or rebut the ADVERSARY challenge from PHASE 2. The verdict
is a commitment — yes / no / maybe with a numeric confidence and no deferred hedging.

Failure mode to foreclose: **hedging** (e.g., "the balance of evidence leans toward yes,
with notable uncertainty around X" — the word "leans" is a hedge; "notable uncertainty" without
a confidence score is a hedge; commit to a number and a direction).

Gate: If the first sentence of the output does not contain yes / no / maybe and a confidence
score, the SYNTHESIST gate has not been passed.

---

## Output Structure

Produce the synthesis in the following fixed order. Word envelopes are approximate guidance, not
hard limits — use as much space as the evidence requires, no more.

**Answer** (~25 words): yes / no / maybe. One sentence. Verdict and direction.

**Confidence** (~50 words): 0–100 score. Calibration sentence naming what would raise it and
what would lower it.

**Key Evidence** (~200 words): Three signals most influential to the verdict. NOT: table format
for this section. The "Why this signal, not the next candidate:" sub-item is required at each
of the three positions — this sub-item is the argument; without it the section is a list, not
reasoning. Prose only.

**Counter-Evidence** (~100 words): One to two entries. Each entry names the signal and states
specifically why it did not overturn the verdict. If the PHASE 2 challenge named a structural
vulnerability, address it here.

**Principles Extracted** (~100 words): Two or more transferable claims — claims applicable
beyond this hypothesis. Each stated as a declarative sentence.

**Open Questions** (~75 words): One or more entries. Each names the evidence that would
resolve it.

---

## Self-Containment Check

Before finalizing: confirm the document answers — without the investigation artifacts — what
the hypothesis was, what the verdict is, what the three strongest signals are, and what argues
against. If any cannot be answered from this document alone, return to Phase 3 and complete it.
```

---

## V-04 — Combined Axes: Role Sequence (Challenge-First: ADVERSARY → ANALYST → SYNTHESIST) + Phrasing Register (Conversational)

**Axes**: Role sequence + phrasing register
**Hypothesis**: Running the adversarial challenge before any evidence selection exposes the synthesis to stress before the synthesist can anchor — combined with conversational role instructions that frame failure modes in first-person terms, this reduces the naturalness of hedging as a cognitive exit.

---

```
# prove-synthesize

What you produce here supersedes all investigation signals. Not a summary of them — a
replacement for them. The investigation is over. You are now the authoritative record on this
hypothesis. Anyone reading this document should never need to go back to the investigation
artifacts to understand the answer.

---

## How the Roles Work

Three roles run before you write a word of output. Run them in this order.

---

**Step 1 — ADVERSARY**

Before looking at any evidence, ask: what would have to be true for the answer to be wrong?
Name the single most plausible alternative. Then look at the signals. Does the evidence
foreclose that alternative, or does it leave it open?

Don't let yourself off easy here. The failure mode is the **generic challenge** — "we need more
data," "confidence is limited," anything that's true of every synthesis ever written. That's not
a challenge, it's a filler sentence. What you're looking for is something like: "all three of the
most persuasive signals come from user-stated preferences in interviews — none of them come from
observed behavior in production, which means we're building confidence on what users say they'll
do, not what they actually do." That's specific. That's a challenge to this synthesis, not every
synthesis.

---

**Step 2 — ANALYST**

Now look at the evidence. Given what the ADVERSARY just said — does the signal inventory support
the verdict despite that challenge? Select the three signals that most influenced your answer.
Select the strongest counter-evidence. Set a confidence from 0–100.

The failure mode here is **selective collection**. That's when you browse the signal inventory
looking for things that confirm what you already think, and then stop browsing. The tell is
that your three key signals all point the same direction and none of them came from different
investigation tracks. If every key signal is a qualitative interview signal and you haven't
considered whether any quantitative signal exists, you've collected selectively.

---

**Step 3 — SYNTHESIST**

Now commit. Yes, no, or maybe. Pick one. Assign a number between 0 and 100. Issue the verdict.

The failure mode is **hedging**, and it sounds like this: "the evidence suggests yes, though
important uncertainties remain." That sentence refuses to commit. A number like 67 and the word
"yes" is a commitment. "Suggests yes" is not. The synthesis supersedes every individual signal —
it does not summarize them. Write like the investigation is closed, because it is.

---

## Output

Write the synthesis as follows. This order is fixed.

**Answer** — yes / no / maybe, first sentence, verdict stated plainly.

**Confidence** — the number, then one sentence on what would push it higher and what would push
it lower.

**Key Evidence** — the three signals. NOT: table format for this section. Each signal entry must
include a "Why not the next candidate:" sentence — that sentence is what turns a list into a
ranked argument; without it you have three entries, not evidence reasoning. Prose only.

**Counter-Evidence** — what argues against the verdict, one or two entries. For each: name the
signal, explain why it didn't change the answer.

**Principles** — at least two claims this investigation surfaces that apply beyond this
hypothesis — transferable, stated as declarative sentences.

**Open Questions** — at least one. What evidence would close it.

---

## Before You Submit

Can a reader who never saw the investigation artifacts understand: what the hypothesis was, what
the verdict is, the three strongest signals, the strongest objection, and why the answer survived
it? If not, it's not done.
```

---

## V-05 — Combined Axes: Output Format (Prose) + Inertia Framing (Prominent Status-Quo Competitor)

**Axes**: Output format + inertia framing
**Hypothesis**: Requiring the synthesist to explicitly name and argue against the status-quo competitor — what the hypothesis outcome would displace — forces a more honest confidence calibration and surfaces counter-evidence that is structurally invisible when counter-evidence is framed only as "signals against."

---

```
# prove-synthesize

This synthesis supersedes all underlying investigation signals. It is the authoritative record
on this hypothesis. It does not aggregate, summarize, or integrate the signal inventory — it
displaces the signal inventory. A reader with no access to the investigation artifacts must be
able to understand the verdict, the reasoning, the limits, and the status-quo alternative from
this document alone.

---

## Cognitive Roles

Run all three roles before producing output. Do not produce output during role execution.

**ANALYST**
Identify the three signals most influential to the verdict. Identify the strongest counter-evidence.
Identify the status-quo competitor — what outcome, behavior, or decision already exists that
the hypothesis outcome would have to displace. Assign preliminary confidence from 0–100.

Failure mode to foreclose: **selective collection** (e.g., evaluating only signals aligned with
the verdict direction while not evaluating signals sourced from the investigation track most
likely to produce disconfirming evidence — e.g., skipping instrumentation signals when the
verdict is about user behavior, because interview signals already produced the desired answer).

Gate: Name the status-quo competitor before advancing. If the status-quo competitor is unnamed,
the ANALYST role is incomplete.

**ADVERSARY**
Challenge the verdict. Name the exact structural vulnerability in the evidence selection. Does
the status-quo competitor have evidence in the signal inventory that the ANALYST passed over?
Is there a signal that argues the status quo is not displaced by this outcome?

Failure mode to foreclose: **generic challenge** (e.g., "confidence would improve with more
investigation" is not a challenge to this synthesis — it is a challenge to every synthesis ever
written; name the exact vulnerability, e.g., "the key evidence contains no signal showing the
status-quo behavior was actually attempted and failed — we have evidence of preference for the
new behavior but no evidence of rejection of the old one").

Gate: The challenge names a specific structural weakness in this evidence set. Generic
challenges fail this gate.

**SYNTHESIST**
Issue the verdict. Yes / no / maybe. Commit to a confidence from 0–100. Incorporate or rebut
the ADVERSARY challenge. The synthesis supersedes every individual signal — it does not
summarize them.

Failure mode to foreclose: **hedging** (e.g., "the investigation provides moderate support for
yes" — "moderate support" is a hedge dressed as a conclusion; the verdict is yes, no, or maybe,
with a number, stated in the first sentence, not in the conclusion of a qualifying paragraph).

---

## Output Structure

Produce the synthesis in this fixed order. All sections are prose. No tables anywhere in the
synthesis.

**Answer**: yes / no / maybe — stated in the first sentence. Confidence score in the same
sentence or the sentence immediately following.

**Confidence Calibration**: One paragraph. Name what evidence would raise the confidence score
and what evidence would lower it. Name the current score's meaning — what it asserts about
the balance of evidence.

**Status-Quo Competitor**: One paragraph naming the status-quo outcome, behavior, or decision
that the hypothesis would displace. What already exists? What would have to stop being true?
Why is this the correct framing of the alternative hypothesis? This section exists because
counter-evidence is incomplete without naming what the verdict competes against.

**Key Evidence**: The three signals most influential to the verdict. NOT: table format for this
section. The "Why this signal ranks above the next candidate:" bridge is required between each
pair of ranked signals — the bridge is the argument; without it the section is enumeration, not
reasoning. Prose only; the ranked argument must be constructable from the prose alone, without
a reader needing to infer the ranking.

**Counter-Evidence**: One to two entries. For each: name the signal, state why it did not
overturn the verdict. If the status-quo competitor has supporting signals in the inventory,
those signals are mandatory counter-evidence candidates — address them here or explain why
they were not selected.

**Principles Extracted**: Two or more transferable claims this investigation surfaces. Stated
as declarative sentences applicable beyond this hypothesis and this topic.

**Open Questions**: One or more entries. Each names the evidence that would resolve it. If the
ADVERSARY named a structural vulnerability that the synthesis cannot fully address, it belongs
here.

---

## Self-Containment Check

Before finalizing: a reader without investigation artifacts must be able to answer — what was
the hypothesis, what is the verdict and confidence, what were the three strongest signals, what
was the status-quo competitor and why it did not prevail, and what remains unresolved. If any
cannot be answered from this document, the synthesis is incomplete. Return and complete it.
```

---

## Variation Summary

| Variation | Primary Axis | Secondary Axis | Key Structural Bet | C-32 Site | C-33 Site | C-34 Site |
|-----------|-------------|---------------|-------------------|-----------|-----------|-----------|
| V-01 | Role sequence (SYNTH→ADV→ANAL) | — | Verdict commitment before adversarial exposure prevents pre-hedging | ADVERSARY gate parenthetical | Key Evidence NOT: + sub-item slot | Opening mandate + SYNTHESIST gate |
| V-02 | Output format (flowing paragraphs) | — | No headers forces argument construction, not container-filling | ANALYST failure mode inline | Key Evidence NOT: + bridge sentence slot | Opening mandate |
| V-03 | Lifecycle emphasis (PHASE labels + word envelopes) | — | Phase discipline prevents single-pass collapse from evidence to verdict | PHASE 2 gate parenthetical | Key Evidence NOT: + sub-item slot | Opening mandate |
| V-04 | Role sequence (ADV→ANAL→SYNTH) | Phrasing register (conversational) | Challenge before anchoring + first-person failure modes reduce hedging as natural exit | ADVERSARY section worked example | Key Evidence NOT: + "Why not" sentence slot | Opening mandate + SYNTHESIST instruction |
| V-05 | Output format (prose) | Inertia framing (status-quo competitor) | Naming the displaced incumbent forces honest counter-evidence selection | ADVERSARY gate parenthetical | Key Evidence NOT: + bridge slot | Opening mandate + SYNTHESIST gate |
