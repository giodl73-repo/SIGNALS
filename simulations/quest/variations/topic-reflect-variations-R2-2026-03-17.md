# /quest:variate — topic-reflect (Round 2) — Five Variations

---

## V-01

**Axis:** Output format — Stage 4 prose template with inline example
**Hypothesis:** Embedding a labeled sample block with a real-looking example artifact name in the Stage 4 instruction makes C-11/C-12 compliance structural. The model cannot compress "Signal Source" into a fragment when a full-filename example is sitting directly above the blank.

---

```markdown
Run /topic:reflect for: {{topic}}.

One question drives this skill: **What did we learn that we did not expect?**

Do not summarize all findings. Surface surprises only — signals that contradicted,
inverted, or materially revised a belief you held before gathering evidence.
Confirmations are not surprises.

---

## Stage 1 — Opening Model

Before examining any signal artifact, record your prior beliefs.

- **Opening Model**: One sentence stating what you assumed was true about this topic.
- **Epistemic Profile**: Rate each of the 5 canonical dimensions
  (Feasibility · Usability · Scalability · Adoptability · Correctness)
  using: High / Medium / Low / Unknown.
- **Beliefs**: Write at least 3 falsifiable claims, labeled B-1, B-2, B-3
  (add more as needed). Each belief is a claim the signals will be tested against.

COMMIT-STAGE-1

---

## Stage 2 — Signal Inventory

List every signal artifact gathered for this topic. Per artifact:
- Artifact name and namespace
- Date
- Primary finding (one sentence)

Inventory only. Do not evaluate surprises yet.

COMMIT-STAGE-2

---

## Stage 3 — Adversarial Gate

Before writing any Stage 4 entries, run the five-check gate.

| # | Check | Finding | Verdict |
|---|-------|---------|---------|
| 1 | Contradiction: does at least one signal contradict a named B-#? | | |
| 2 | Source specificity: can every candidate surprise name a single artifact? | | |
| 3 | Design impact: does every candidate affect a specific component, API,
      flow, or decision (not "the system")? | | |
| 4 | Epistemic coverage: do 2+ of the 5 canonical dimensions appear? | | |
| 5 | Foreknowledge: did any surprise use knowledge unavailable at Stage 1? | | |

Assign VALID or INVALID to each row.

Then write exactly one of:
- **GATE-CONFIRMED — proceed to Stage 4** (all five VALID)
- **GATE-REJECTED — extend sweep and re-run** (any INVALID)

COMMIT-STAGE-3

---

## Stage 4 — Surprise Synthesis

Write one numbered prose entry per GATE-CONFIRMED surprise.
**Use the prose block template below. Do not use a table or columns.**

The template (copy and fill for each surprise):

---
**[N]. [Surprise Name — 3 to 6 words]**

**Surprise:** [Full sentence or two. Name the specific B-# belief this
contradicts. Explain what changed and why it was unexpected given that
prior belief.]

**Signal Source:** [Name the artifact. Include namespace and date.
Example: "flow-trigger-golden-2026-03-14.md (flow namespace, March 14)."
Do not write "multiple sources." If the signal appeared across several
artifacts, name the one most responsible. Filename + namespace + date —
never a fragment.]

**Design Impact:** [Name the exact component, API endpoint, flow, or
architectural decision the team must revisit. Write a complete sentence.
Example: "The retry backoff logic in FlowEngine.dispatch() must be
redesigned to handle nested trigger chains." Do not write "the system"
or any phrase shorter than a complete thought.]

COMMIT-ENTRY
---

Minimum 2 entries. If the gate yielded fewer than 2 confirmed surprises,
extend the signal sweep and re-run Stage 3.

COMMIT-STAGE-4

---

## Stage 5 — Cluster Map

Group Stage 4 entries into 2–4 clusters by theme.

| Cluster Name | Entries (N-#) | Shared Pattern | Next Team / Skill |

The "Next Team / Skill" column must name a specific skill path
(e.g., `/flow:resilience`) or a specific role (e.g., "API contract
owner"). "Investigate" alone does not pass.

COMMIT-STAGE-5

---

## Stage 6 — Verdict

Close the Symmetric Contract.

For each Stage 1 belief, assign a verdict:
- **COHERENT** — signals confirmed this belief
- **CONTRADICTORY** — signals overturned this belief
- **FOREKNOWLEDGE-FLAGGED** — if Stage 3 check 5 fired for this belief

| Belief | Verdict | Revision Direction | Key Signal |

Then state: **Foreknowledge Signal = CLEAR** or **FLAGGED**.
If FLAGGED, name the belief and the artifact that introduced the
foreknowledge. Do not publish this artifact.

COMMIT-STAGE-6
```

---

## V-02

**Axis:** Lifecycle emphasis — combined candidate identification + gate in Stage 3 (gate-early)
**Hypothesis:** Running the adversarial gate on named candidates before any prose is written forces VALID/INVALID verdicts before the model invests in narrative, preventing motivated reasoning that inflates gate passage rates.

---

```markdown
Run /topic:reflect for: {{topic}}.

**The question:** What did we learn that we did not expect?

A surprise is a signal that contradicted or substantially revised a belief
held before gathering evidence. Confirmations and expected outcomes are not
surprises, no matter how valuable.

---

## Stage 1 — Opening Model

Write your prior beliefs before reviewing any artifact.

- **Opening Model**: One sentence — what did you assume was true?
- **Epistemic Profile**: Rate each canonical dimension
  (Feasibility · Usability · Scalability · Adoptability · Correctness):
  High / Medium / Low / Unknown.
- **Beliefs B-1, B-2, B-3...**: Minimum 3. Each is a falsifiable claim.
  Number them sequentially.

COMMIT-STAGE-1

---

## Stage 2 — Signal Inventory

List every signal artifact. Per artifact: name, namespace, date,
one-sentence finding.

COMMIT-STAGE-2

---

## Stage 3 — Candidate Identification and Gate (Combined)

This stage has two steps. Complete both before proceeding.

**Step A — Identify candidates**

For each signal from Stage 2 that surprised you, write one line:

> Candidate: [name] | Source: [artifact name] | Contradicts: [B-#]

Do not write prose yet. List format only.

**Step B — Gate the full candidate list**

Run five adversarial checks against all candidates together:

| # | Check | Finding | Verdict |
|---|-------|---------|---------|
| 1 | Contradiction: does at least one candidate overturn a named B-#? | | |
| 2 | Source: can each candidate be traced to one named artifact
      (not "multiple sources")? | | |
| 3 | Design Impact: does each candidate affect a named component, API,
      flow, or decision (not "the system")? | | |
| 4 | Epistemic Coverage: do 2+ canonical dimensions appear across
      candidates? | | |
| 5 | Foreknowledge: did any candidate rely on knowledge unavailable
      at Stage 1? | | |

VALID = check passes. INVALID = check fails.

Close with:
- **GATE-CONFIRMED — proceed to Stage 4** (all VALID)
- **GATE-REJECTED — extend sweep, re-run Stage 3** (any INVALID)

COMMIT-STAGE-3

---

## Stage 4 — Surprise Entries

For each GATE-CONFIRMED candidate, write one numbered prose entry.
No tables. One block per surprise.

---
**[N]. [Surprise Name]**

**Surprise:** What was unexpected and why, given B-[number] from Stage 1.
One or two sentences. The B-# reference is required.

**Signal Source:** Artifact name, namespace, date. Full phrase — not a
fragment, not an abbreviation, not "multiple sources." Name one primary
artifact.

**Design Impact:** Specific component, API, flow, or decision.
A complete sentence. Not "the system."

COMMIT-ENTRY
---

Minimum 2 entries. If fewer than 2 candidates cleared the gate,
extend the sweep before continuing.

COMMIT-STAGE-4

---

## Stage 5 — Cluster Map

| Cluster | Entries | Pattern | Next Team / Skill |

At least one named skill or role in the last column — not "investigate"
alone.

COMMIT-STAGE-5

---

## Stage 6 — Verdict

| Belief | Verdict | Revision Direction | Evidence |

Verdicts: COHERENT · CONTRADICTORY · FOREKNOWLEDGE-FLAGGED.

Foreknowledge Signal: CLEAR or FLAGGED. If FLAGGED: name the belief
and artifact. Do not publish.

COMMIT-STAGE-6
```

---

## V-03

**Axis:** Phrasing register — direct imperative commands throughout
**Hypothesis:** Replacing descriptive framing ("every entry should include," "the field must contain") with direct imperatives ("Name the artifact. Do not write 'multiple sources.'") reduces the ambiguity surface. Rules feel like constraints, not suggestions.

---

```markdown
Run /topic:reflect for: {{topic}}.

**One question: What did we learn that we did not expect?**

Do not summarize. Do not list confirmations. Surface only what surprised
you — signals that changed a belief, not confirmed one.

---

## Stage 1

Write your opening model now, before reading any artifact.

1. State your **Opening Model** in one sentence. What did you assume?
2. Rate each epistemic dimension. Use High / Medium / Low / Unknown.
   Dimensions: Feasibility · Usability · Scalability · Adoptability · Correctness.
3. Write your beliefs. Label them B-1, B-2, B-3 (minimum 3). Make each
   falsifiable. Number them.

COMMIT-STAGE-1

---

## Stage 2

Inventory your signals. For each artifact: name it, name its namespace,
give its date, state its finding in one sentence. List every artifact
gathered for this topic.

COMMIT-STAGE-2

---

## Stage 3

Run the adversarial gate. Five checks. Fill this table:

| # | Check | Finding | Verdict |
|---|-------|---------|---------|
| 1 | Contradiction: does at least one signal contradict a B-#? | | |
| 2 | Source: can every surprise name one specific artifact? | | |
| 3 | Design impact: does every surprise name a specific component
      or decision — not "the system"? | | |
| 4 | Epistemic coverage: do 2+ canonical dimensions appear? | | |
| 5 | Foreknowledge: did any surprise use post-Stage-1 knowledge? | | |

Assign VALID or INVALID. Do not skip rows.

Write one of:
- **GATE-CONFIRMED — proceed to Stage 4** (all VALID)
- **GATE-REJECTED — extend sweep and re-run** (any INVALID)

COMMIT-STAGE-3

---

## Stage 4

Write one entry per surprise. No tables. Use this exact format:

---
**[N]. [Surprise name — 3 to 6 words]**

**Surprise:** State what happened. Name B-[number] from Stage 1.
Explain why it was unexpected.

**Signal Source:** Name the artifact. Name the namespace. Give the date.
Do not write "multiple sources." Do not abbreviate the filename.
Write a complete phrase — not a fragment.

**Design Impact:** Name a specific component, API, flow, or decision.
Write a full sentence. Do not write "the system." Do not write a fragment.

COMMIT-ENTRY
---

Write at least 2 entries. If you have only 1, sweep more signals first.

COMMIT-STAGE-4

---

## Stage 5

Group surprises into 2–4 clusters. Build this table:

| Cluster | Entries | What connects them | Next Team / Skill |

Name a skill or role in the last column. "Investigate" alone fails.

COMMIT-STAGE-5

---

## Stage 6

Close the Symmetric Contract. For each Stage 1 belief, write a verdict:

- **COHERENT** — signals confirmed it
- **CONTRADICTORY** — signals overturned it
- **FOREKNOWLEDGE-FLAGGED** — if check 5 fired for this belief

| Belief | Verdict | Revision Direction | Key Evidence |

State: Foreknowledge Signal = CLEAR or FLAGGED.
If FLAGGED: name the belief and the artifact. Do not publish.

COMMIT-STAGE-6
```

---

## V-04

**Axes:** Role sequence (Belief Archaeologist → Signal Detective) + Inertia framing (opening model as status-quo position to be defeated)
**Hypothesis:** Naming distinct roles for Stage 1 and Stage 4 creates an explicit handoff that anchors Stage 4 B-# references. Framing the opening model as "the status-quo position" — the thing signals must defeat to qualify as surprises — strengthens the contradiction requirement of C-01.

---

```markdown
Run /topic:reflect for: {{topic}}.

This skill is an inversion exercise. Before signals, there was a
**status-quo position** — what the team assumed before evidence arrived.
After signals, the question is: what did the evidence defeat?

A surprise is a signal that beat the status-quo position. Confirmations
do not qualify. Use only signals that challenged or overturned an
assumption you held before gathering evidence.

---

## Stage 1 — Belief Archaeologist

You are the **Belief Archaeologist**. Before reviewing any artifact,
excavate the prior position.

Record the team's assumptions as they existed before signals:

- **Opening Model**: One sentence. What was the status-quo position on
  this topic? What did the team assume without evidence?
- **Epistemic Profile**: Rate each of the 5 canonical dimensions
  (Feasibility · Usability · Scalability · Adoptability · Correctness)
  at their pre-signal confidence: High / Medium / Low / Unknown.
- **Beliefs B-1, B-2, B-3...**: Minimum 3 falsifiable claims.
  These are the line items of the status-quo position — the claims
  the signals will be tested against.

Goal: make the prior position specific enough that signals have
something real to defeat.

COMMIT-STAGE-1

---

## Stage 2 — Signal Inventory

List every signal artifact gathered for this topic.
Per artifact: name, namespace, date, one-sentence finding.

COMMIT-STAGE-2

---

## Stage 3 — Adversarial Gate

Before the Signal Detective runs, gate the candidates.
Five adversarial checks:

| # | Check | Finding | Verdict |
|---|-------|---------|---------|
| 1 | Contradiction: does at least one candidate overturn a specific
      B-# status-quo belief? | | |
| 2 | Source: can each candidate trace to one named artifact
      (not a vague collection)? | | |
| 3 | Design Impact: does each candidate affect a named component,
      API, flow, or decision? | | |
| 4 | Epistemic Coverage: do 2+ of the 5 canonical dimensions appear? | | |
| 5 | Foreknowledge: was any surprise introduced by knowledge
      unavailable at Stage 1? | | |

VALID or INVALID per check.

- **GATE-CONFIRMED — proceed to Stage 4** (all VALID)
- **GATE-REJECTED — extend sweep, re-run gate** (any INVALID)

COMMIT-STAGE-3

---

## Stage 4 — Signal Detective

You are now the **Signal Detective**. For each GATE-CONFIRMED surprise,
write a numbered entry showing:
(a) which status-quo belief the signal defeated,
(b) which artifact carried the signal,
(c) what must change in the design as a result.

One prose block per surprise. No tables.

---
**[N]. [Surprise Name]**

**Surprise:** Describe what was unexpected. Reference the specific
status-quo belief it defeats: "This overturns B-[number], which held
that..." One or two full sentences.

**Signal Source:** Name the artifact that carried this signal.
Include namespace and date. Example: "scout-competitors-golden-2026-03-14.md
(scout namespace, March 14)." If the signal spanned multiple artifacts,
name the one most responsible. Full filename — never a fragment, never
"multiple sources."

**Design Impact:** Name the exact component, API, flow, or decision
the team must revisit. Write a complete sentence. Example: "The
signal-dispatch throttle in FlowEngine must be redesigned to handle
back-pressure from nested subscriptions." Do not write "the system"
or any abbreviated phrase.

COMMIT-ENTRY
---

Minimum 2 entries. If fewer than 2 candidates cleared the gate,
extend the sweep.

COMMIT-STAGE-4

---

## Stage 5 — Cluster Map

Group entries by shared theme. The cluster map is the handoff artifact
the next team reads before starting.

| Cluster | Entries | Shared Pattern | Next Team / Skill |

Name a specific skill (e.g., `/flow:throttle`) or named role in the
last column.

COMMIT-STAGE-5

---

## Stage 6 — Has the Status-Quo Position Survived?

Return to the Belief Archaeologist role. For each B-# belief, render
a verdict:

- **COHERENT** — signals confirmed it; status quo survives here
- **CONTRADICTORY** — signals overturned it; status quo defeated here
- **FOREKNOWLEDGE-FLAGGED** — if Stage 3 check 5 fired for this belief

| Belief | Verdict | Revision Direction | Key Signal |

Foreknowledge Signal: CLEAR or FLAGGED.
If FLAGGED: name the belief and the artifact. Do not publish.

COMMIT-STAGE-6
```

---

## V-05

**Axes:** Compressed lifecycle (minimal stage prose) + front-loaded token protocol (all tokens listed upfront with placement rules)
**Hypothesis:** Placing the complete token inventory in a reference table at the top of the prompt — before Stage 1 — makes token placement a known constraint from the start rather than a per-stage discovery. Inline reminders then reference the table rather than re-explain, reducing prompt verbosity while improving C-09 compliance.

---

```markdown
Run /topic:reflect for: {{topic}}.

**The question:** What did we learn that we did not expect?

Surface surprises only — signals that contradicted a prior belief.
Confirmations are not surprises.

---

## Token Protocol

Place every token exactly as shown. Do not omit any.

| Token | Placement |
|-------|-----------|
| COMMIT-STAGE-1 | End of Stage 1 output |
| COMMIT-STAGE-2 | End of Stage 2 output |
| COMMIT-STAGE-3 | End of Stage 3, after GATE token |
| COMMIT-ENTRY | End of each Stage 4 surprise block |
| COMMIT-STAGE-4 | After all Stage 4 entries |
| COMMIT-STAGE-5 | End of Stage 5 output |
| COMMIT-STAGE-6 | End of Stage 6 output |

GATE token (choose one, place at end of Stage 3 before COMMIT-STAGE-3):
- `GATE-CONFIRMED — proceed to Stage 4` (all gate checks VALID)
- `GATE-REJECTED — extend sweep and re-run` (any check INVALID)

---

## Stage 1 — Opening Model

Before reviewing any signal, write:
- **Opening Model**: one sentence — what did you assume?
- **Epistemic Profile**: rate each of the 5 canonical dimensions
  (Feasibility · Usability · Scalability · Adoptability · Correctness):
  High / Medium / Low / Unknown
- **Beliefs B-1 through B-N**: minimum 3, each falsifiable

COMMIT-STAGE-1

---

## Stage 2 — Signal Inventory

List every artifact gathered. Per artifact: name, namespace, date,
one-sentence finding.

COMMIT-STAGE-2

---

## Stage 3 — Adversarial Gate

| # | Check | Finding | Verdict |
|---|-------|---------|---------|
| 1 | Contradiction: at least one signal contradicts a B-# | | |
| 2 | Source: each surprise traces to one named artifact | | |
| 3 | Design Impact: each surprise names a specific component,
      API, flow, or decision | | |
| 4 | Epistemic Coverage: 2+ canonical dimensions present | | |
| 5 | Foreknowledge: no surprise uses post-Stage-1 knowledge | | |

VALID / INVALID per row.

[GATE token here]

COMMIT-STAGE-3

---

## Stage 4 — Surprise Entries

One numbered prose block per GATE-CONFIRMED surprise. No tables.

---
**[N]. Surprise Name**

**Surprise:** Full sentence. Reference B-[number] from Stage 1.

**Signal Source:** Artifact name + namespace + date. Full phrase.
Never "multiple sources." Never a fragment.

**Design Impact:** Specific component, API, flow, or decision.
Full sentence. Never "the system." Never a fragment.

COMMIT-ENTRY
---

Minimum 2 entries. Extend sweep if fewer cleared the gate.

COMMIT-STAGE-4

---

## Stage 5 — Cluster Map

| Cluster | Entries | Pattern | Next Team / Skill |

At least one named skill or role in the last column.

COMMIT-STAGE-5

---

## Stage 6 — Verdict

| Belief | Verdict | Revision Direction | Evidence |

Verdicts: COHERENT · CONTRADICTORY · FOREKNOWLEDGE-FLAGGED.

Foreknowledge Signal: CLEAR or FLAGGED.
If FLAGGED: name the belief and artifact. Do not publish.

COMMIT-STAGE-6
```

---

## Variation Matrix

| Variation | Primary Axis | Secondary Axis | Key Differentiator | C-11/C-12 Strategy |
|-----------|-------------|---------------|--------------------|--------------------|
| V-01 | Output format | — | Inline example artifact name in template | Prose block with real-looking example makes abstraction concrete |
| V-02 | Lifecycle emphasis | — | Gate runs during candidate ID (Stage 3 = Step A + Step B) | Standard prose block; gate-early prevents motivated reasoning |
| V-03 | Phrasing register | — | Every instruction is an imperative; no descriptive framing | Direct commands: "Name the artifact. Do not write 'multiple sources.'" |
| V-04 | Role sequence | Inertia framing | Belief Archaeologist → Signal Detective handoff; status-quo framing | Prose block; B-# anchoring strengthened by defeat framing |
| V-05 | Lifecycle emphasis | Token protocol | Token table front-loaded; stage bodies compressed | Minimal stage prose; token constraint visible from line 1 |
