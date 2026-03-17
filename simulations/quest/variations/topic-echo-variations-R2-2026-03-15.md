---

# Variations: `topic:echo` — Round 2

**Rubric:** v2 | **Date:** 2026-03-15

---

## Design Context

R1 differentiating evidence identified three mechanisms that became the new v2 aspirational criteria:
- **V-04's Archaeologist/Chronicler split** → C-10 (Epistemic Delta Tracing): forced prior-assumption surfacing before the gate ran
- **V-03's CONFIRMATION routing** → C-11 (Confirmation Accounting): made gate operation *provable* by showing what was excluded
- **V-04's collective framing question** → C-12 (Collective Next-Team Signal): "what do surprises tell the next team together?" produced output not derivable from individual entries

R2 targets each new criterion with a **mechanism**, not a prose instruction. A mechanism is a structural constraint that produces the desired behavior as a side effect.

- C-10 mechanism: belief ledger drafted *before* signals are read (V-01)
- C-11 mechanism: Confirmation Ledger appears in the output artifact, not scaffolding (V-02)
- C-12 mechanism: collective brief drafted *before* individual entries — generative, not derivative (V-03)

---

## V-01 — Role Sequence axis

**Variation axis:** Role sequence — Archaeologist pre-role documents prior beliefs before any signal is read; gate runs on belief-delta pairs, not on findings alone.

**Hypothesis:** The C-10 failure mode is writing a finding without naming the belief it overturned. The mechanism fix: require a belief ledger *before* signals are read. When the ledger exists, every finding is evaluated against a named prior belief. Without it, the model reconstructs "what was assumed" post-hoc, which produces invented or vacuous deltas. The belief delta becomes structural rather than optional.

---

### Prompt Body

```
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

Minimum 2 findings must survive the gate. If fewer survive, re-examine — the beliefs may
have been too loosely stated.

For each surviving finding, write one entry:

**[Surprise Name]**
*2-5 words, capitalized, reusable as a citation.*

- **Source signal**: Specific artifact name or skill type. Not "the research."
- **Prior belief**: The exact belief from the Archaeologist's ledger this finding overturns.
  One sentence.
- **Finding**: What the signal revealed. Must contradict or complicate the prior belief.
  One sentence.
- **Belief delta**: "We assumed X; the signal showed Y; therefore Z changes in the design."
  Complete the sentence structure. Do not omit the third clause.
- **Design impact**: Specific component, flow, or decision that must change. One sentence.

---

**Synthesis**

Do the surprises share a root cause or reveal a common blind spot in the pre-investigation
beliefs? Write 2-4 sentences. Name any pattern; state its absence if none is evident.

---

**Forward guidance**

1-3 sentences for the next team building `{topic}`. Register:
"If you are about to build X, the beliefs we held about Y did not survive contact with Z.
Before you commit to Y, verify ___."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.
Include: entries (with Prior Belief and Belief Delta fields), Synthesis, Forward guidance.
Do not include the belief ledger.
```

---

## V-02 — Lifecycle Emphasis axis

**Variation axis:** Lifecycle emphasis — a dedicated Confirmation Ledger phase whose output *appears in the artifact*, proving the gate ran.

**Hypothesis:** The C-11 failure mode is a gate that ran but left no evidence. A reviewer cannot distinguish a rigorous gate from an absent gate if only passing items appear in the output. The mechanism fix: the Confirmation Ledger is a **required output section**, not scaffolding. Every artifact reviewed and classified as a confirmation is named, described, and routed. A future reader verifies gate operation by reading the ledger.

---

### Prompt Body

```
You are executing `topic-echo` for `{topic}`.

**What the echo is.** It answers one question: what did we learn that we did not expect?
Institutional memory for the next team. Not a summary. Each entry is a named surprise —
sourced, contrasted with prior expectation, assessed for design impact.

---

**Phase 1 — Signal Inventory.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Note what each was investigating.
Internal working memory only.

---

**Phase 2 — Gate Adjudication.**

For each noteworthy finding, apply the surprise gate:
> "Would a reasonably informed person reading only the pre-investigation design materials
> have predicted this finding?"
>
> YES → CONFIRMATION
> NO → SURPRISE

Every reviewed finding must receive a classification. Do not skip findings.

---

**Phase 3 — Confirmation Ledger (included in output).**

For every CONFIRMATION, write one line:

> `[Namespace/Artifact] — [One phrase describing the finding] → CONFIRMATION → topic-story`

This section appears in the output artifact. A future reader verifies that the gate ran
and that specific items were consciously excluded.

If you found no confirmations, state:
> "All reviewed findings were surprises. No confirmations identified — re-examine the
> signal set; this is unusual."

---

**Phase 4 — Surprise Entries (minimum 2).**

For each SURPRISE classification:

**[Surprise Name]**
*2-5 words, capitalized, reusable as a citation.*

- **Source signal**: Specific artifact name or skill type. Traceable.
- **Prior assumption**: What was expected before this signal. One sentence.
- **Finding**: What the signal revealed — must oppose the prior assumption. One sentence.
- **Design impact**: Specific component, flow, or decision affected. Must name something
  specific.

---

**Phase 5 — Synthesis.**

Do the surprises cluster? Write 2-4 sentences. Name any pattern; state its absence.

---

**Phase 6 — Forward guidance.**

1-3 sentences for the next team. Register: "If you are about to build X, know that Y."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact structure:
1. Surprise Entries (Phase 4)
2. Synthesis (Phase 5)
3. Forward Guidance (Phase 6)
4. **What We Confirmed (Not Here)** — Confirmation Ledger (Phase 3)

The ledger is last so it does not distract from the surprises, but it must be present.
```

---

## V-03 — Output Format axis

**Variation axis:** Output format — collective orientation brief drafted *first*, before individual entries; brief leads the artifact.

**Hypothesis:** The C-12 failure mode is a synthesis section written after all entries, which summarizes prose already committed — it cannot be non-derivable. The mechanism fix: write the collective brief *before* individual entries. Without entry prose to draw from, the brief must compress signal-level understanding, not paraphrase entry-level writing. The brief written first is generative; the brief written last is a restatement.

---

### Prompt Body

```
You are executing `topic-echo` for `{topic}`.

**What the echo is.** Institutional memory. Not a summary. A record of surprises — each
named, sourced, assessed for design impact — plus a collective orientation brief that tells
the next team what the surprises *mean together*.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces. Note what each
was investigating. Internal scaffolding only.

---

**Step 2 — Identify surprise candidates.**

For each noteworthy finding, apply the prediction test:
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
- Do not name individual surprises (you have not written them yet).
- Do not summarize the signal artifacts.
- Speak to the pattern, blind spot, or design assumption the surprise *set* reveals.

Test: A reader who reads only this brief must come away with an accurate orientation to
the topic's most important unknowns. If the brief reads like a list of topics, it fails.

Write the brief now.

---

**Step 4 — Write individual entries.**

For each surprise candidate:

**[Surprise Name]**
*2-5 words, capitalized, reusable as a citation.*

- **Source signal**: Specific artifact name or skill type. Not "the research."
- **Prior assumption**: What was expected. One sentence.
- **Finding**: What the signal revealed — must oppose the prior assumption. One sentence.
- **Design impact**: Specific component, flow, or decision affected. Must name something.

---

**Step 5 — Refine the collective brief.**

Return to the brief from Step 3. Read the individual entries. Revise if needed — but
preserve or deepen what is non-derivable. If after revision the brief is just a list of
entry themes, it has degraded into a summary. The test: could a reader who has not read
the entries understand the surprise landscape accurately from only the brief? If yes, pass.

---

**Step 6 — Forward guidance.**

1-3 sentences for the next team. Must be specific to these surprises. Register:
"If you are about to build X, know that Y because we found Z."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact structure:
1. **What These Surprises Mean Together** (Step 5 collective brief)
2. Individual Entries (Step 4)
3. Forward Guidance (Step 6)

The brief leads the artifact. A future reader with limited time reads the brief first.
```

---

## V-04 — Inertia Framing axis

**Variation axis:** Phrasing register — the status-quo competitor (`topic-story`) is described in concrete detail *before* any instruction begins; echo value is expressed as the delta from that competitor.

**Hypothesis:** "Don't write a summary" is negative instruction. Describing exactly what a summary contains — its sections, scope, audience — makes the contrast concrete before instruction begins. When the model has already sorted two distinct product types, the surprise-only constraint requires less enforcement than when it is stated as a warning about one failure mode.

---

### Prompt Body

```
You are writing `topic-echo` for `{topic}`.

---

**The output that already exists.**

When a signal investigation finishes, the natural output is a synthesis document. It
organizes findings by weight, draws out themes, gives the team a coherent account of what
was learned. It answers: what did we find, and what does it mean? It is `topic-story`.

Here is what `topic-story` contains that you are NOT producing:
- Coverage of all major namespaces
- Findings that confirmed the design direction
- Recommendations organized by priority
- A coherent narrative from investigation start to conclusion

If your output could serve as the `topic-story` — if a PM reading it would say "this is a
good summary of what the investigation found" — you have written the wrong document.

---

**The output that does not yet exist.**

`topic-echo` answers a different question: **what did we learn that we did not expect?**

Its audience is not the current team. It is the *next* team — the team that will walk this
path and carry the same false assumptions the current team carried at the start. The echo's
purpose is to correct those assumptions before they cause damage.

Each entry is a corrective: a place where reality diverged from prediction, named so the
next team can cite it in conversation.

---

**Execution.**

**Step 1 — Read signals.** Read artifacts from `simulations/{topic}/` across all namespaces.

**Step 2 — Apply the prediction test per finding.** "Would a person reading only the
original design materials — before any signals — have predicted this?" YES → `topic-story`,
not here. NO → surprise candidate.

**Step 3 — Name each surprise.** 2-5 words, capitalized, memorable. "The Cascade Inversion"
passes. "Unexpected Finding 1" fails.

**Step 4 — For each named surprise (minimum 2):**

- **Source signal** — specific artifact or skill type. Traceable.
- **Prior assumption** — what was expected. One sentence.
- **Finding** — what the signal revealed. Must oppose the prior assumption. One sentence.
- **Design impact** — specific component, flow, or decision that must change. Name it.

**Step 5 — Synthesize.** Do the surprises share a root cause or reveal a common blind spot?
2-4 sentences. Name any pattern; state its absence.

**Step 6 — Forward guidance.** 1-3 sentences for the next team. Register:
"If you are about to build X, the assumption about Y did not survive — verify Z."

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
```

---

## V-05 — Combination: Belief Ledger + Confirmation Ledger + Collective Brief

**Variation axis:** All three new v2 aspirational targets (C-10, C-11, C-12) at structurally distinct moments.

**Hypothesis:** Each criterion addresses a distinct failure point: C-10 fails when prior beliefs are invented post-hoc (fix: belief ledger before reading); C-11 fails when the gate leaves no evidence (fix: confirmations in the output); C-12 fails when the collective synthesis is written after entries (fix: brief drafted first, before entry prose exists). Assigning each mechanism to a structurally distinct moment means they do not compete — each runs at a different time on different material.

---

### Prompt Body

```
You are executing `topic-echo` for `{topic}`. Execute in the order given. Do not skip phases.

---

**Anti-Pattern Notice.**

**finding-as-surprise substitution** — predictable outcome stated in surprise language.
*Test:* Would a person reading only the original design materials have predicted this?
YES → confirmation, not a surprise.

**summary-in-disguise** — full investigation scope reformatted as echo entries.
*Test:* Could your output be described as "a summary of what the investigation found"?
YES → you have written `topic-story`, not `topic-echo`.

---

**Phase 1 — Archaeologist (belief ledger, before signal reading).**

Read only the pre-investigation materials for `{topic}` (spec, design notes, topic-plan).
Do not read signal artifacts yet.

For each namespace with signals, write one sentence:
> "Before signals, we assumed about `{namespace}`: ___."

If no explicit assumption exists for a namespace, state the implicit one.

Belief ledger is execution scaffolding — do not include in the output artifact.

---

**Phase 2 — Gate Adjudication (signals + per-finding verdict).**

Read signal artifacts from `simulations/{topic}/`. For each finding, compare against the
belief ledger entry for its namespace. Issue a verdict:

```
Finding: {one-sentence description}
Namespace: {namespace}
Verdict: SURPRISE | CONFIRMATION
Rationale: {one sentence — why it contradicts or confirms the prior belief}
Destination: [SURPRISE → echo] [CONFIRMATION → topic-story, not topic-echo]
```

Every finding worth noting must receive a verdict. Minimum 2 SURPRISE verdicts.
Gate log is execution scaffolding — do not include in the output artifact.

---

**Phase 3 — Collective Brief (write before individual entries).**

Before writing any individual entry, write 3-5 sentences:

> "What do these surprises mean together? What must the next team know — the orientation
> that cannot be derived from reading each surprise in sequence?"

Do not name individual surprises. Do not summarize artifacts. Speak to the pattern or
blind spot the *set* reveals.

Test: a reader who reads only this brief must come away with an accurate orientation
to the topic's most important unknowns.

---

**Phase 4 — Surprise Entries.**

For each SURPRISE verdict (minimum 2), anchored in the belief ledger:

**[Surprise Name]**
*2-5 words, capitalized, reusable as a citation.*

- **Source signal**: Specific artifact or skill type. Traceable.
- **Prior belief** (from Phase 1): The stated belief this finding overturns.
- **Finding**: What the signal revealed — must contradict the prior belief. One sentence.
- **Belief delta**: "We assumed X; signal showed Y; therefore Z changes." Do not omit
  the third clause.
- **Design impact**: Specific component, flow, or decision. Must name something specific.

---

**Phase 5 — Refine Collective Brief.**

Return to the Phase 3 brief. Read the entries. Revise if needed. Preserve what is
non-derivable. Test: could a reader who has not read the entries orient accurately from
the brief alone? If yes, pass. If not, revise until yes.

---

**Phase 6 — Forward Guidance.**

1-3 sentences for the next team. Specific to these surprises. Register:
"If you are about to build X, the assumption about Y did not survive — before you commit,
verify Z because we found ___."

---

**Phase 7 — Confirmation Ledger (output section).**

For every CONFIRMATION verdict from Phase 2, write one line:

> `[Namespace/Artifact] — [One phrase] → CONFIRMATION → topic-story`

If no confirmations: "No confirmations identified — all findings were surprises. Re-examine."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact structure:
1. **What These Surprises Mean Together** (Phase 5 collective brief)
2. Surprise Entries (Phase 4)
3. Forward Guidance (Phase 6)
4. **What We Confirmed (Not Here)** — Confirmation Ledger (Phase 7)

Phases 1-3 are execution scaffolding — omit. Phases 5-7 are output.
```

---

## Variation Summary

| Var | Axis | Primary Target | Mechanism |
|-----|------|----------------|-----------|
| V-01 | Role sequence | C-10 Epistemic Delta | Belief ledger drafted before signal reading |
| V-02 | Lifecycle emphasis | C-11 Confirmation Accounting | Confirmation Ledger as required output section |
| V-03 | Output format | C-12 Collective Next-Team Signal | Collective brief drafted before individual entries |
| V-04 | Phrasing register / inertia framing | C-01 Surprise filter | Competitor (`topic-story`) described in concrete detail before instruction |
| V-05 | Combination | C-10 + C-11 + C-12 | All three mechanisms at structurally distinct phases |

**Key design principle for R2:** Each new criterion is enforced by a structural constraint at a distinct moment in the execution sequence. No two mechanisms share a phase. This prevents attention competition and ensures each mechanism runs on its target material — the belief ledger on pre-signal assumptions, the gate log on candidate findings, the collective brief on signal-level understanding before prose exists.
