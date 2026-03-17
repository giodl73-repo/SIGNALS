---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 2
rubric: v2
---

# Variations: `topic:echo` — Round 2

**Rubric:** v2 | **Date:** 2026-03-15

---

## Design Context

R1 differentiating evidence:
- V-04's Archaeologist/Chronicler split was the highest-performing C-01 mechanism because
  it forced prior-assumption surfacing *before* the gate ran. This became C-10.
- V-03's explicit CONFIRMATION routing to `topic-story` made the gate *provable* — a reader
  could verify it ran. This became C-11.
- V-04 was the only variation that asked "what do the surprises tell the next team
  *collectively*?" producing a synthesis block distinct from per-entry framing. This became C-12.

**R2 strategy:**

- V-01 through V-03: single-axis variations, each targeting exactly one new v2 aspirational
  criterion (C-10, C-11, C-12) with a single mechanism change.
- V-04: single-axis inertia framing — addresses the summary-substitution failure mode at the
  register level.
- V-05: combination of all three new aspirational targets at structurally distinct moments.

**What makes R2 different from R1:**

R1 variations were effective at essentials (C-01 through C-04) but did not structurally
enforce the three new aspirational criteria. R2 targets each criterion with a mechanism, not
just a prose instruction. A mechanism is a structural constraint that produces the desired
behavior as a side effect — not a reminder to do it.

- C-10 mechanism: a belief ledger drafted *before* signals are read (V-01)
- C-11 mechanism: a Confirmation Ledger that appears in the output artifact, not as
  scaffolding (V-02)
- C-12 mechanism: the collective orientation brief drafted *first*, before individual entries
  — forcing it to be generative rather than a summary of prose already written (V-03)

---

## V-01 — Role Sequence axis

**Variation axis:** Role sequence — Archaeologist pre-role documents prior beliefs before
any signal is read; gate runs on belief-delta pairs, not on findings alone.

**Hypothesis:** The C-10 failure mode is writing a finding without naming the belief it
overturned. The mechanism fix: require a belief ledger *before* signals are read — one
sentence per namespace stating what was assumed before investigation. When the ledger exists,
every finding can be evaluated against a named prior belief. Without the ledger, the model
reconstructs "what was assumed" post-hoc, which produces invented or vacuous deltas.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`. Two roles execute in sequence.

---

**Role 1: Archaeologist**

Before reading any signal artifact, document the prior state of belief.

Read only the pre-investigation materials for `{topic}`: the original spec, design notes, or
topic-plan. Do not read signal artifacts yet.

For each namespace that has signals (scout, draft, review, flow, trace, prove, listen,
program), write one sentence:
> "Before we read signals for `{namespace}`, we assumed: ___."

This is the belief ledger. It documents what the team expected to find, not what they found.
If there is no explicit assumption for a namespace, state the implicit one — what would a
reasonable person have assumed given the design materials?

Write the belief ledger now. It is execution scaffolding — do not include it in the output
artifact, but you will need it in the next role.

---

**Role 2: Chronicler**

Read the signal artifacts from `simulations/{topic}/`. For each namespace, compare what the
signals actually revealed against the corresponding entry in the belief ledger.

Apply the surprise gate per finding:
> "Does this finding contradict, reverse, or significantly complicate the prior belief for
> this namespace?"
>
> YES → genuine surprise. Carry forward.
> NO → the finding confirms or extends the prior belief. Do not include in the echo.
>    Destination: `topic-story`.

Minimum 2 findings must survive the gate. If fewer survive, re-examine the signals — you
may be applying the gate too broadly, or the beliefs were too loosely stated.

For each surviving finding, write one entry:

**[Surprise Name]**
*2-5 words, capitalized, reusable as a citation.*

- **Source signal**: Specific artifact name or skill type (e.g., `prove-interview`,
  `flow-resilience`). Not "the research" or "the signals."
- **Prior belief**: The exact belief from the Archaeologist's ledger that this finding
  overturns. Cite it verbatim or in summary. One sentence.
- **Finding**: What the signal actually revealed. Must contradict or complicate the prior
  belief. One sentence.
- **Belief delta**: What changed. "We assumed X; the signal showed Y; therefore Z changes
  in the design." Complete the sentence structure. Do not omit the third clause.
- **Design impact**: The specific component, flow, or decision that must change as a
  result. One sentence. Must name something specific.

---

**Synthesis**

Do the surprises share a root cause or reveal a common blind spot in the pre-investigation
beliefs? Write 2-4 sentences. Name any pattern you see. If none: state that explicitly.

---

**Forward guidance**

1-3 sentences for the next team building `{topic}`. Register:
"If you are about to build X, the beliefs we held about Y did not survive contact with Z.
Before you commit to Y, verify ___."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.
Include: entries (with Prior Belief and Belief Delta fields), Synthesis, Forward guidance.
Do not include the belief ledger or Skeptic log.

---

## V-02 — Lifecycle Emphasis axis

**Variation axis:** Lifecycle emphasis — a dedicated Confirmation Ledger phase whose output
*appears in the artifact*, proving the gate ran.

**Hypothesis:** The C-11 failure mode is a gate that ran but left no evidence. A reviewer
cannot distinguish a rigorous gate from an absent gate if only passing items appear in the
output. The mechanism fix: the Confirmation Ledger is not scaffolding — it is a required
output section. Every artifact that was reviewed and classified as a confirmation is named,
described in one phrase, and routed. A reader can verify the gate's operation by reading
the ledger section.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** It answers one question: what did we learn that we did not expect?
It is institutional memory for the next team. It is not a summary of findings. Each entry
is a named surprise — sourced, contrasted with prior expectation, and assessed for design
impact.

---

**Phase 1 — Signal Inventory.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). For each artifact, note in one phrase
what it was investigating. This is internal working memory.

---

**Phase 2 — Gate Adjudication.**

Scan the signals for all findings worth noting — notable, non-trivial, or worth remembering.
For each, apply the surprise gate:

> "Would a reasonably informed person reading only the pre-investigation design materials
> for `{topic}` — before any signals were gathered — have predicted this finding?"
>
> YES → classification: CONFIRMATION
> NO → classification: SURPRISE

Record every finding and its classification. Every reviewed finding must receive a
classification. Do not skip findings to make the gate seem cleaner.

---

**Phase 3 — Confirmation Ledger (included in output).**

For every finding classified CONFIRMATION, write one line:

> `[Namespace/Artifact] — [One phrase describing the finding] → CONFIRMATION → topic-story`

This ledger section appears in the output artifact. Its purpose: a future reader can verify
that the gate ran and that specific items were reviewed and consciously excluded.

Minimum: 1 confirmation must appear. If you found no confirmations, state:
> "All reviewed findings were surprises. No confirmations identified — this is unusual;
> re-examine the signal set."

---

**Phase 4 — Surprise Entries.**

For each SURPRISE classification (minimum 2), write one entry:

**[Surprise Name]**
*2-5 words, capitalized, reusable as a citation.*

- **Source signal**: Specific artifact name or skill type. Traceable.
- **Prior assumption**: What was expected before this signal. One sentence.
- **Finding**: What the signal actually revealed — must oppose the prior assumption.
  One sentence.
- **Design impact**: Specific component, flow, or decision affected. Must name something
  specific. Generic statements do not pass.

---

**Phase 5 — Synthesis.**

Do the surprises cluster? Write 2-4 sentences. Do 2 or more share a root cause or reveal
the same blind spot? Name any pattern; state its absence if none is evident.

---

**Phase 6 — Forward guidance.**

1-3 sentences for the next team building `{topic}`. Specific to these surprises. Register:
"If you are about to build X, know that Y because we found Z."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact structure:
1. Surprise Entries (Phase 4)
2. Synthesis (Phase 5)
3. Forward guidance (Phase 6)
4. **Confirmation Ledger** (Phase 3) — titled "What We Confirmed (Not Here)"

The Confirmation Ledger section is last so it does not distract from the surprises,
but it must be present. Without it, gate verification is impossible.

---

## V-03 — Output Format axis

**Variation axis:** Output format — collective orientation brief drafted *first*, before
individual entries; brief leads the artifact.

**Hypothesis:** The C-12 failure mode is a synthesis section written after all entries have
been composed — it summarizes what was just written and therefore cannot be non-derivable.
The mechanism fix: write the collective brief *before* writing individual entries. When the
brief must be composed without the individual entry prose to draw from, it must do genuine
synthesis — it must compress what the surprises mean together from signal-level understanding,
not from entry-level paraphrase. The brief written first is generative; the brief written
last is a restatement.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** It answers one question: what did we learn that we did not expect?
It is institutional memory. It is not a summary of findings. It is a record of surprises —
each named, sourced, and assessed for design impact — plus a collective orientation brief
that tells the next team what the surprises *mean together*.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). For each artifact, note in one phrase
what it was investigating. Internal scaffolding only.

---

**Step 2 — Identify surprise candidates.**

Scan the signals for findings not predictable from the original design materials. Apply the
prediction test per finding:

> "Would a reader of only the pre-investigation design materials have predicted this?"
>
> YES → confirmation. Not an echo entry.
> NO → surprise candidate.

Collect at least 2 surprise candidates before proceeding.

---

**Step 3 — Write the collective orientation brief first.**

Before writing any individual entry, write 3-5 sentences that answer:

> "What do these surprises mean together? If the next team read nothing else, what would
> they need to know to start their investigation with accurate expectations?"

Constraints:
- Do not mention individual surprise names (you have not written them yet).
- Do not summarize the signal artifacts.
- Speak from your understanding of what the surprise *set* reveals — what pattern, blind
  spot, or design assumption did the investigation collectively overturn?
- A reader who reads only this brief should come away with an accurate orientation to
  the topic's most important unknowns.

Write the brief now. You will refine it after the individual entries are written, but do
not let the refinement become a restatement. The brief must contain something that is not
derivable from reading the entries in sequence.

---

**Step 4 — Write individual entries.**

For each surprise candidate, write one entry:

**[Surprise Name]**
*2-5 words, capitalized, reusable as a citation.*

- **Source signal**: Specific artifact name or skill type. Not "the research."
- **Prior assumption**: What was expected before this signal. One sentence.
- **Finding**: What the signal actually revealed — must oppose the prior assumption.
  One sentence.
- **Design impact**: Specific component, flow, or decision affected. Must name something
  specific.

---

**Step 5 — Refine the collective brief.**

Return to the brief from Step 3. Read the individual entries. Revise the brief if needed —
but the revision must preserve or deepen what is non-derivable. If after revision the brief
is just a list of entry themes, it has degraded into a summary. The test: could a reader
who has not read the entries understand the surprise landscape accurately from only the
brief? If yes, the brief passes. If no, revise.

---

**Step 6 — Forward guidance.**

1-3 sentences for the next team building `{topic}`. Must be specific to these surprises.
Register: "If you are about to build X, know that Y because we found Z."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact structure:
1. **Orientation Brief** (from Steps 3/5) — titled "What These Surprises Mean Together"
2. Individual Entries (from Step 4)
3. Forward Guidance (from Step 6)

The brief leads the artifact. This structure reinforces its purpose: a future reader who
has limited time reads the brief first and decides whether to read the entries.

---

## V-04 — Inertia Framing axis

**Variation axis:** Phrasing register — the status-quo competitor (`topic-story`) is described
in concrete detail before any instruction begins; the echo's value is expressed as the delta
from that competitor.

**Hypothesis:** "Don't write a summary" is negative instruction. Describing exactly what a
summary contains — naming its sections, its scope, its audience — makes the contrast concrete.
When the model knows precisely what it is not writing (and why that output exists and is
useful), the surprise-only constraint requires less enforcement because the model has already
sorted two distinct product types, not just been warned about one failure mode.

---

### Prompt Body

You are writing `topic-echo` for `{topic}`.

---

**The output that already exists.**

When a signal investigation finishes, the natural output is a synthesis document. It
organizes findings by weight, draws out themes, and gives the team a coherent account of
what was learned. It answers: what did we find, and what does it mean? It is `topic-story`.

`topic-story` exists or will be written separately. It is useful. It is not what you are
writing now.

Here is what `topic-story` contains that you are NOT producing:
- Coverage of all major namespaces
- Restatement of findings that confirmed the design direction
- Recommendations organized by priority
- A coherent narrative from investigation start to conclusion

If your output could serve as the `topic-story` — if a PM reading it would say "this is a
good summary of what the investigation found" — you have written the wrong document.

---

**The output that does not yet exist.**

`topic-echo` is the output that `topic-story` cannot produce because `topic-story` is not
trying to. It answers a different question: **what did we learn that we did not expect?**

Its audience is not the current team. It is the *next* team — the team that will walk this
path a year from now and will carry the same false assumptions the current team carried at
the start. The echo's purpose is to correct those assumptions before they cause damage.

Each entry is a corrective: a place where reality diverged from prediction, named so the
next team can cite it by name.

---

**Execution.**

**Step 1 — Read signals.** Read artifacts from `simulations/{topic}/` across all namespaces.
Note what each artifact was investigating.

**Step 2 — Apply the prediction test per finding.** For each noteworthy finding: "Would a
person reading only the original design materials — before any signals — have predicted
this?" YES → it belongs in `topic-story`, not here. Cut it. NO → surprise candidate.

**Step 3 — Name each surprise.** Each gets a distinct, human-memorable name (2-5 words,
capitalized). Names must work as citations in conversation: "The Cascade Inversion" passes.
"Unexpected Finding 1" fails.

**Step 4 — For each named surprise (minimum 2):**

- **Source signal** — specific artifact name or skill type. Traceable to one artifact.
- **Prior assumption** — what was expected going in. One sentence. If no explicit
  assumption existed, state the implicit one.
- **Finding** — what the signal revealed. Must oppose or complicate the prior assumption.
  One sentence. The contrast must be explicit in the entry.
- **Design impact** — specific consequence for the design: which component, flow, decision,
  or assumption must change. Not "this affects the design." Name the thing.

**Step 5 — Synthesize.** Do the surprises share a root cause or reveal a common blind spot?
Write 2-4 sentences. Name any pattern; state its absence if none is evident.

**Step 6 — Forward guidance.** 1-3 sentences for the next team. Must be derivable only
from these surprises. Register: "If you are about to build X, the assumption about Y did
not survive — verify Z before you commit."

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

---

## V-05 — Combination: Belief Ledger + Confirmation Ledger + Collective Brief

**Variation axis:** All three new v2 aspirational targets (C-10, C-11, C-12) at structurally
distinct moments:
- C-10 (Epistemic Delta): Archaeologist pre-role writes belief ledger before signal reading
- C-11 (Confirmation Accounting): Confirmation Ledger is an output section (not scaffolding)
- C-12 (Collective Next-Team Signal): Collective brief drafted before individual entries

**Hypothesis:** Each aspirational criterion addresses a distinct failure point in the echo
production sequence. C-10 fails when prior beliefs are invented post-hoc (fix: ledger before
reading). C-11 fails when the gate leaves no evidence (fix: confirmations in the output).
C-12 fails when the collective synthesis is written after entries and becomes a restatement
(fix: brief written first). Assigning each mechanism to a structurally distinct moment
means they do not compete: the belief ledger, the gate, the output section, and the
first-draft brief are each doing different work at different times.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`. Execute in the order given. Do not skip phases.

---

**Anti-Pattern Notice — Read before executing.**

The two ways echo outputs most commonly fail:

**finding-as-surprise substitution** — a predictable outcome stated in surprise language.
The design called for X; the signal confirmed X; the output calls this "surprising."
*Test:* Would a person reading only the original design materials have predicted this?
YES → confirmation, not a surprise.

**summary-in-disguise** — the full investigation scope reformatted as echo entries. The tell:
if your output could be described as "a summary of what the investigation found," you have
written `topic-story`, not `topic-echo`.

---

**Phase 1 — Archaeologist (belief ledger before signal reading).**

Read only the pre-investigation materials for `{topic}` (spec, design notes, topic-plan).
Do not read signal artifacts yet.

For each namespace with signals (scout, draft, review, flow, trace, prove, listen, program),
write one sentence:
> "Before signals, we assumed about `{namespace}`: ___."

This is the belief ledger. It documents expectations, not findings. If there is no explicit
assumption for a namespace, state the implicit one.

The belief ledger is execution scaffolding — do not include it in the output artifact.

---

**Phase 2 — Signal Reading + Gate Adjudication.**

Now read the signal artifacts from `simulations/{topic}/`. For each namespace, compare what
the signals revealed against the corresponding belief ledger entry.

For each finding, issue a verdict:

```
Finding: {one-sentence description}
Namespace: {scout | draft | review | flow | trace | prove | listen | program | topic}
Verdict: SURPRISE | CONFIRMATION
Rationale: {one sentence — why this contradicts or confirms the prior belief}
Destination: [SURPRISE → echo] [CONFIRMATION → topic-story, not topic-echo]
```

State your verdict for every finding worth noting. Minimum 2 SURPRISE verdicts.
The gate log is execution scaffolding — do not include it in the output artifact.

---

**Phase 3 — Collective Brief (write before individual entries).**

Before writing any individual entry, write 3-5 sentences:

> "What do these surprises mean together? What must the next team know — the orientation
> that cannot be derived from reading each surprise in sequence?"

Constraints:
- Do not name individual surprises yet (they are not written).
- Do not summarize signal artifacts.
- Speak to the pattern, blind spot, or overturned assumption the *set* reveals.

The test: a reader who reads only this brief must come away with a meaningfully accurate
orientation to the topic's most important unknowns.

Draft this brief now. You will refine it after writing entries, but the core insight must
emerge here, not from reading your own prose.

---

**Phase 4 — Surprise Entries.**

For each SURPRISE verdict (minimum 2), write one entry using the belief ledger's prior
assumption as the anchor:

**[Surprise Name]**
*2-5 words, capitalized, reusable as a citation.*

- **Source signal**: Specific artifact name or skill type. Traceable.
- **Prior belief** (from Phase 1 ledger): The stated belief this finding overturns.
  Cite it directly or in summary.
- **Finding**: What the signal revealed — must contradict or complicate the prior belief.
  One sentence.
- **Belief delta**: "We assumed X; signal showed Y; therefore Z changes." Complete the
  structure. Do not omit the third clause.
- **Design impact**: Specific component, flow, or decision that must change. One sentence.
  Must name something specific.

---

**Phase 5 — Refine the Collective Brief.**

Return to the Phase 3 brief. Read the individual entries. Revise if needed, but preserve
what is non-derivable. If after revision the brief is just a list of entry themes, revise
again. The brief must orient a reader who has not read the entries.

---

**Phase 6 — Forward Guidance.**

1-3 sentences for the next team building `{topic}`. Must be specific to these surprises.
Register: "If you are about to build X, the assumption about Y did not survive — before
you commit, verify Z because we found ___."

---

**Phase 7 — Confirmation Ledger.**

For every CONFIRMATION verdict from Phase 2, write one line:

> `[Namespace/Artifact] — [One phrase] → CONFIRMATION → topic-story`

Minimum 1 confirmation must appear. If none were identified, state:
> "No confirmations identified — all reviewed findings were surprises. Re-examine if this
> seems unlikely."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact structure (in order):
1. **What These Surprises Mean Together** (Phase 5 collective brief)
2. Surprise Entries (Phase 4)
3. Forward Guidance (Phase 6)
4. **What We Confirmed (Not Here)** — Confirmation Ledger (Phase 7)

Phases 1-3 (belief ledger, gate log, initial brief draft) are execution scaffolding — omit
from artifact. Phases 5-7 are output.
