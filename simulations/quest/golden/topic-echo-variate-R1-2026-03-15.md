---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 1
rubric: v1
---

# Variations: `topic:echo` — Round 1

**Rubric:** v1 | **Date:** 2026-03-15

---

## V-01 — Output Format axis

**Hypothesis:** A rigid per-surprise entry form with labeled fields forces the three
essential behaviors (naming, attribution, design impact) mechanically and prevents
content drift from surprises into summaries. The form structure is the enforcement
mechanism — not prose instruction.

---

### Prompt Body

You are writing a `topic-echo` signal for the topic `{topic}`.

A `topic-echo` is institutional memory. It answers one question: **"What did we learn
that we did not expect?"** It is not a summary of findings. It is not a recap of the
signals gathered. It is a record of surprises — each one named, sourced, and assessed
for its impact on the design direction.

**Setup.** Read the signal artifacts for `{topic}` from `simulations/{topic}/`. Identify
signals that were gathered across namespaces (scout, draft, review, flow, trace, prove,
listen, program). For each signal artifact, note one sentence: what the signal was
investigating. Do not write anything yet.

**Identify candidates.** Scan each signal for findings that were not predicted by the
original design intent — findings that would have surprised the team before the
investigation began. A finding is a surprise if a reasonable person, reading only the
pre-investigation design materials, would not have anticipated it. Apply this test
strictly. If a finding confirms what the spec already implied, it is not a surprise.
Collect at least 2 candidates.

**Write the echo.** For each surprise, produce one entry in the following form.
Every field is required. Do not omit any field. Do not merge fields.

---

**Surprise Name:** `{A distinct 2-5 word handle, capitalized, reusable as a citation}`

**Source Signal:** `{skill-type/artifact name — e.g., flow-resilience, prove-interview}`

**Prior Assumption:** `{What the team assumed or expected before this signal was read.
One sentence. If there was no explicit assumption, state the implicit one.}`

**Finding:** `{What the signal actually revealed. One sentence. Must oppose or
contradict the Prior Assumption.}`

**Design Impact:** `{How this surprise changes, constrains, or challenges the design
direction. Must name a specific component, flow, or decision. "This matters because..."
is not sufficient — state what specifically changes.}`

---

Repeat this form for each surprise. Minimum 2 entries. No upper limit, but every
entry must survive the surprise test.

**Close with a cross-signal synthesis.** After the entries, write 2-4 sentences:
do the surprises cluster? Do they share a root cause, reveal a systemic blind spot,
or together point toward a design direction not previously visible? If they do not
cluster, say so explicitly.

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

---

## V-02 — Phrasing Register axis

**Hypothesis:** A conversational, first-person imperative register ("Before you write
anything, ask yourself...") makes the anti-pattern vivid and personal. The key failure
mode — expected findings dressed as surprises — is most reliably prevented when the
instruction sounds like a colleague warning you, not a spec describing a process.

---

### Prompt Body

You're writing the echo for `{topic}`.

Here's the one thing you need to hold onto: this is not a summary. Every team that
runs this process produces a summary at the end — a tidy account of what they found
and what it means. That output already exists: it's the `topic-story`. What you're
writing now is different. The echo is for the *next* team that walks this path. It
answers the question they'll ask a year from now: "Did anyone come this way before?
What surprised them?"

**Before you write anything, ask yourself:** If I had read only the original spec and
design materials for `{topic}` — before any of these signals were gathered — would I
have predicted this finding? If the answer is yes, cut it. It belongs in the story,
not the echo.

**First: orient yourself.** Read the signal artifacts in `simulations/{topic}/`. You're
looking for moments where the signal said something the design didn't anticipate. Not
confirmations. Not validations. Moments where the signal said: "actually, no."

**Then: write each surprise.** For each one you find, give it a name — a real name,
not "Finding 1." Something a teammate could say in a hallway: "The Cascade Inversion"
or "The Silent Adopter Paradox." Names that stick are the whole point.

For each named surprise:
- Say where it came from. Which signal? Be specific enough that someone could go
  read the artifact themselves.
- Say what you assumed going in and what you actually found. The contrast is the
  surprise. Without the contrast, a reader who wasn't there can't gauge how surprising
  it actually was.
- Say what it does to the design. Not "this is important" — say which decision it
  forces, which component it affects, which assumption it invalidates.

You need at least two. One surprise is a footnote. Two is the beginning of a pattern.

**Finally: look across the surprises.** Is there something they share? A common root?
A blind spot in the original design thinking? If the surprises cluster around the same
theme, name the cluster. That's the real institutional memory — not the individual
surprises, but what they say together.

Write the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

---

## V-03 — Lifecycle Emphasis axis

**Hypothesis:** An explicit gate question per candidate surprise ("Would someone have
predicted this before reading the signal? If yes, cut it.") applied as a formal
lifecycle step reduces the key failure mode more reliably than embedded prose
instruction. Making the gate a named phase forces the model to evaluate each item
before committing it to output.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**Purpose.** The echo answers one question: what did we learn that we did not expect?
Its audience is the next team that works on this topic. It is not a summary of
findings. It is a record of surprises with enough traceability that a future reader
can verify each one.

---

**Phase 1 — Signal Inventory**

Read the signal artifacts from `simulations/{topic}/`. List the artifact names and
the namespace each belongs to (scout, draft, review, flow, trace, prove, listen,
program, topic). For each artifact, write one phrase: what was being investigated.
This inventory is working memory — do not include it in the output artifact.

---

**Phase 2 — Surprise Candidate Selection**

For each signal, identify findings that were not predictable from the original design
intent. A finding qualifies as a surprise candidate if it satisfies both:

1. It describes something the spec or design materials did not anticipate.
2. A reader of only the pre-investigation materials would not have predicted it.

For each candidate, apply the **surprise gate**:
> "If someone had read only the design materials before this investigation — no signals,
> no interviews, no experiments — would they have expected this finding?"
>
> If yes → discard. This is a confirmation, not a surprise.
> If no → retain as a named surprise.

Run every candidate through the gate. Candidates that fail are not wrong — they are
valuable confirmations that belong in `topic-story`, not `topic-echo`.

---

**Phase 3 — Surprise Documentation**

For each retained candidate (minimum 2), produce:

**[Surprise Name]** — A 2-5 word handle, capitalized, distinct from all other
names in this echo. Reusable as a citation.

- *Source signal*: The artifact name or skill type (e.g., `prove-interview`,
  `flow-resilience`). Specific enough to locate.
- *Expected*: What was assumed or predicted before this signal.
- *Actual*: What the signal revealed. Must be in opposition to Expected.
- *Design impact*: The specific component, flow, or decision this finding affects
  and how.

---

**Phase 4 — Pattern Synthesis**

Examine the set of named surprises. Write 1-3 sentences:
- Do two or more surprises share a root cause or reveal the same blind spot?
- If yes, name the pattern.
- If no, say so — absence of pattern is itself information.

---

**Phase 5 — Future-Team Guidance**

Write 1-3 sentences of forward-looking guidance addressed explicitly to the next team
that builds `{topic}`. This guidance must be specific to these surprises — not generic
advice. The register: "If you are about to build X, know that..." or "Before committing
to Y, verify Z because we found..."

---

**Phase 6 — Write Artifact**

Write the completed echo to `simulations/{topic}/{topic}-echo-{date}.md`.
Include only Phases 3-5 in the artifact. Phases 1-2 are execution scaffolding.

---

## V-04 — Combination: Role Sequence + Output Format

**Hypothesis:** Running a Skeptic role before the Author role eliminates false
surprises before they enter the output. The Skeptic's sole job is to challenge
each candidate with "would you have predicted this?" — a single-question filter
applied adversarially. Surviving candidates are then handed to the Author who
writes them in a structured per-field form that enforces naming, attribution, and
impact without additional instruction.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`. Two roles execute in sequence.

---

**Role 1: Skeptic**

Read the signal artifacts from `simulations/{topic}/`. Across all signals, assemble
a list of findings that *might* be surprises — anything the signal revealed that is
noteworthy or non-trivial.

For each candidate, answer one question:
> "Before this investigation began — before any of these signals were gathered —
> would a reasonably informed person working from the design materials have
> predicted this finding?"

- Answer YES: the finding is a confirmation. Label it CONFIRMED. Do not carry it
  forward. (It is valuable, but it belongs in `topic-story`.)
- Answer NO: the finding is a genuine surprise. Label it SURPRISE. Carry it forward.

Minimum 2 SURPRISE candidates must survive. If fewer than 2 survive the gate,
re-examine the signals — you may have applied the filter too aggressively, or the
signals may need closer reading. State which candidates you examined and how you
ruled on each (one line per candidate). This Skeptic log is execution scaffolding —
do not include it in the output artifact.

---

**Role 2: Author**

Receive the SURPRISE candidates from the Skeptic. For each, write one entry in the
following exact form:

---

**[Surprise Name]**
*A distinct 2-5 word handle, capitalized. Not a numbered item. Not "Finding N."
Memorable enough to cite by name in conversation.*

| Field | Content |
|---|---|
| Source Signal | `{artifact name or skill type}` |
| Prior Assumption | `{what the team assumed or expected before this signal}` |
| Finding | `{what the signal actually revealed — must oppose Prior Assumption}` |
| Design Impact | `{specific component, flow, or decision this changes — not generic}` |

---

After all entries, write a **Synthesis** paragraph (2-4 sentences): do the surprises
cluster? Do they share a root cause or reveal the same blind spot? If they cluster,
name the pattern. If they do not, say so.

Write the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
The artifact contains: surprise entries (table form) + Synthesis. Not the Skeptic log.

---

## V-05 — Combination: Inertia Framing + Phrasing Register

**Hypothesis:** Explicitly naming and describing the status-quo output — the summary
that every team naturally produces — makes the contrast vivid before instruction
begins. When the model understands precisely what it is *not* writing, combined with
a formal register that names anti-patterns by label, the surprise-only constraint is
maintained most reliably.

---

### Prompt Body

You are writing `topic-echo` for `{topic}`.

---

**What you are NOT writing.**

Every team that completes a signal investigation naturally produces a summary:
a coherent account of what was learned, organized by finding, synthesized into a
recommendation. That output is `topic-story`. It is useful. It already exists or
should be written separately.

The echo is not that. The echo does not summarize. It does not restate findings.
It does not recap the signals or their conclusions. If a reader could describe your
output as "a summary of what the investigation found," you have written a story, not
an echo.

The failure mode has a name: **finding-as-surprise substitution** — when an expected
or predictable outcome is dressed in the language of surprise. It is the most common
way echo outputs fail. An output can look like an echo, use the word "unexpectedly,"
and still be a story in disguise if none of its items are genuinely surprising.

---

**What you ARE writing.**

The echo answers one question: **what did we learn that we did not expect?**

Its audience is a future team that has not yet begun this investigation. Its purpose
is to prevent that team from carrying the same false assumptions the current team
carried. Each entry in the echo is a corrective — a place where reality diverged
from prediction.

---

**Execution.**

**Step 1 — Read signals.** Read signal artifacts from `simulations/{topic}/` across
all namespaces. Note what each signal was investigating.

**Step 2 — Apply the prediction test.** For each finding worth noting, ask: "Would
a person who read only the original design materials — before any signals were
gathered — have predicted this?" If yes, it is a confirmation. Do not include it.
Confirmations are not surprises. They are evidence the design was right, which is
valuable, but it belongs elsewhere.

**Step 3 — Name each surprise.** Assign each surviving finding a distinct,
human-memorable name (2-5 words, capitalized). Names must be reusable as citations
in future conversations. "The Throttle Blindspot" passes. "Surprise 1" fails.
"An unexpected finding" fails.

**Step 4 — For each named surprise, provide:**

- **Source signal** — the artifact name or skill type. Traceable to a specific signal,
  not to "the research" or "the interviews."
- **Expectation delta** — what was assumed going in (Prior Assumption) and what
  the signal actually revealed (Finding). The contrast must be explicit in the entry,
  not reconstructed from context.
- **Design impact** — the specific consequence for the design: which component,
  flow, decision, or assumption must now change. One sentence minimum. Generic
  statements ("this affects the design") do not pass.

Minimum 2 surprises. Each must independently pass the prediction test.

**Step 5 — Synthesize.** After all entries: do the surprises share a root cause?
Reveal a common blind spot? Name any pattern you see across them. If there is none,
state that explicitly.

**Step 6 — Forward guidance.** End with 1-3 sentences addressed to the next team,
written as specific advice derivable only from these surprises. The register:
"If you are building {feature}, know that {surprise-derived warning}."

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
