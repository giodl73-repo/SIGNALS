## topic-plan Skill — Variate R1 (V-01 through V-05)

---

### V-01 — Single Axis: Output Format
**Axis**: Table-heavy, structured diff format
**Hypothesis**: A scannable before/after table reduces confirmation friction and forces typed proposals at the point of output rather than burying them in prose.

---

```markdown
# topic-plan — Revise Signal Strategy

You are updating the signal strategy for a topic in the Signal plugin.
The strategy was written at a point in time. Signals gathered since then
may have revealed new dimensions, invalidated assumptions, or shifted
priorities. Your job is to surface those gaps and propose a revised plan.

## Step 1 — Read the Current Strategy

Read `simulations/{topic}/strategy.md`.

Extract and hold:
- Which namespaces are covered
- Which skills are planned
- The stated rationale for coverage priorities
- Any explicit gaps the strategy acknowledged

## Step 2 — Read All Gathered Signals

Glob `simulations/{topic}/**/*-{date}.md` to find all signal artifacts.
Read each one. For each signal note:
- Namespace and skill it came from
- Key finding or output
- Whether the strategy anticipated this dimension

## Step 3 — Compute the Delta

Answer this question directly: **What did the signals reveal that the
strategy did not anticipate?**

A plain inventory of signals is not the delta. The delta is the gap between
what the strategy expected to learn and what the signals actually showed.

## Step 4 — Produce the Revision Table

Output a table with the following columns:

| Change Type | Target (skill or namespace) | Signal Evidence | Rationale | Priority |
|-------------|----------------------------|-----------------|-----------|----------|
| ADD         | ...                         | artifact name   | ...       | high/med/low |
| REMOVE      | ...                         | artifact name   | ...       | — |
| REPRIORITIZE| ...                         | artifact name   | ...       | new priority |

Valid change types: **ADD**, **REMOVE**, **REPRIORITIZE** only.
Untyped observations do not belong in this table.

If a category has no changes, include one row with "No changes" under
that type — do not omit the category.

## Step 5 — Before/After Summary

After the table, produce a compact diff-style view:

```
BEFORE  scout: feasibility, market, compliance
AFTER   scout: feasibility, market, compliance, stakeholders [+stakeholders: signal S3 showed missing exec alignment]

BEFORE  prove: hypothesis, prototype
AFTER   prove: hypothesis [−prototype: signal P2 showed scope exceeds current wave; defer]

BEFORE  listen: (not covered)
AFTER   listen: feedback [+feedback: signal R4 surfaced active user complaints that need tracking]
```

Show only namespaces with changes.

## Step 6 — Namespace Gap Check

Review all 9 namespaces: scout, draft, review, flow, trace, prove, listen,
program, topic. For each one not in the current strategy, state whether
the signals suggest it should be added or is appropriately deferred,
given the topic's current stage.

## Step 7 — Conflict Detection

If two signals point in opposite directions on the same dimension (e.g.,
one feasibility signal says viable, another says blocked), name the
conflict explicitly in a "Conflicts" section and state how the revised
strategy should handle it.

## Step 8 — Confirmation Gate

**Do not modify `strategy.md` yet.**

Present the revision table and before/after summary. Ask:

> "Ready to apply these changes to strategy.md? Reply 'apply' to confirm,
> or tell me what to adjust."

Only write to `strategy.md` after the user confirms.
```

---

### V-02 — Single Axis: Lifecycle Emphasis
**Axis**: Explicit phase labels, hard boundaries, stop-gate language at each transition
**Hypothesis**: Named phases with hard stop gates reduce the failure mode where the model reads inputs and immediately writes output, skipping delta reasoning.

---

```markdown
# topic-plan — Revise Signal Strategy

Revise the signal strategy for a topic based on what new signals have revealed.

---

## PHASE 1: INPUT ACQUISITION
*Complete this phase fully before proceeding to Phase 2.*

**1a. Read the strategy.**
Open `simulations/{topic}/strategy.md`. Hold its full contents in context.
Note the namespaces covered, skills planned, and the reasoning behind
coverage choices.

**1b. Read all signals.**
Find all artifacts under `simulations/{topic}/`. Read each one.
Build a mental inventory: namespace, skill, finding, date.

**STOP. Do not proceed to Phase 2 until both reads are complete.**

---

## PHASE 2: DELTA IDENTIFICATION
*The purpose of this phase is to answer ONE question.*

The question: **What did these signals reveal that the strategy did not
anticipate when it was written?**

This is not an inventory. Do not list the signals. Answer the gap question.

Work through it systematically:
- For each signal, ask: "Did the strategy expect to learn this?"
- If yes: the signal confirms the strategy. Note it but do not treat it
  as a revision driver.
- If no: the signal revealed a new dimension. This is a candidate revision.

Capture your delta findings as a working list before moving to Phase 3.

**STOP. Do not produce output yet.**

---

## PHASE 3: PROPOSAL FORMATION
*Convert delta findings into typed change proposals.*

Every proposal must be one of three types:

- **ADD** — a new skill or coverage area not currently in the strategy
- **REMOVE** — a planned skill or area that signals show is no longer needed
- **REPRIORITIZE** — a planned skill whose order or weight should shift

For each proposal:
1. State the type
2. Name the target (skill name or namespace)
3. Cite the signal artifact(s) that motivated it
4. Write one sentence of rationale

If your delta findings produced no ADDs, say so explicitly.
If your delta findings produced no REMOVEs, say so explicitly.
If your delta findings produced no REPRIORITIZEs, say so explicitly.

Addressing all three types — even with a "none" conclusion — is required.

---

## PHASE 4: GAP AUDIT
*Run after proposal formation, before output.*

Check all 9 namespaces: scout, draft, review, flow, trace, prove, listen,
program, topic.

For each namespace absent from the strategy, state:
- Is there signal evidence suggesting it should be added?
- Or is it appropriately deferred for this topic's stage?

This is a 9-row audit. Include every namespace.

---

## PHASE 5: OUTPUT
*Present to the user. Do not write files.*

Structure your output as:

1. **Delta Summary** — 2-4 sentences naming what the signals revealed
   that the strategy missed
2. **Proposals** — typed list (ADD / REMOVE / REPRIORITIZE) with evidence
   and rationale per item
3. **Before/After** — compact view of how strategy.md would change
4. **Namespace Gap Audit** — 9-row table
5. **Conflicts** — any signals pointing in opposite directions; if none, say so

End with:

> "Confirm 'apply' to update strategy.md, or tell me what to adjust."

**STOP. Do not write to strategy.md until the user responds.**

---

## PHASE 6: WRITE (conditional)
*Only execute if the user confirms.*

On confirmation, update `simulations/{topic}/strategy.md` to reflect the
approved proposals. Preserve the file's existing structure and voice.
After writing, confirm: "strategy.md updated."
```

---

### V-03 — Single Axis: Inertia Framing
**Axis**: Strategy-as-prior framing (Bayesian update metaphor); the existing strategy is a prior belief, not a target to preserve
**Hypothesis**: Framing the strategy as a prior that evidence updates — rather than a document to edit — increases the quality of delta identification by removing the model's tendency to rationalize the existing plan.

---

```markdown
# topic-plan — Update the Signal Strategy

The signal strategy is a prior belief about what evidence you need to gather.
Like any prior, it was written with incomplete information. Signals gathered
since then are evidence. Your job is to update the prior.

Do not preserve the strategy because it was already written. Do not revise
it because revision feels productive. Update it only where the evidence
demands it.

## Reading the Prior

Read `simulations/{topic}/strategy.md`.

Internalize it as a belief state, not a document:
- What the strategy believed about which namespaces mattered
- What it believed about the order of evidence-gathering
- What it believed were the open questions

## Reading the Evidence

Read all signal artifacts under `simulations/{topic}/`.

For each signal, ask: **Does this change the prior?**

Three outcomes per signal:
- **Confirms** — signal aligns with what the strategy expected. No update needed.
- **Extends** — signal reveals a dimension the strategy didn't cover. Candidate for addition.
- **Contradicts** — signal shows the strategy was wrong about something. Candidate for removal or re-prioritization.

Note each signal's outcome. Confirmations are not revision drivers.
Extensions and contradictions are.

## The Update Decision

For each extension or contradiction, decide on a typed update:

**ADD** — The strategy should cover something it currently doesn't.
Evidence: [signal artifact]. Rationale: [what the signal revealed].

**REMOVE** — The strategy is planning coverage that signals now show
is unnecessary or out of scope.
Evidence: [signal artifact]. Rationale: [what changed].

**REPRIORITIZE** — The strategy covers the right ground but in the wrong
order or with the wrong weight.
Evidence: [signal artifact]. Rationale: [what shifted].

The status quo is a valid choice. If the prior survives the evidence, say
so clearly: "No updates required — signals confirm the existing strategy."
A non-update is a legitimate output. But it must be argued, not defaulted to.

## Namespace Pressure Check

Nine namespaces exist: scout, draft, review, flow, trace, prove, listen,
program, topic. For each one not in the strategy, does any signal create
pressure to add it? State the answer for each absent namespace. "No pressure"
is an acceptable answer, but silence is not.

## Conflict Surface

If two signals contradict each other — one says a dimension is covered,
another says it's blocked; one says scope is viable, another says it's
too large — name the contradiction. The revised strategy cannot silently
hold two incompatible beliefs. Recommend how to resolve it.

## Output Format

Present:

1. **Evidence summary** — what the signals showed (extensions and
   contradictions only; confirmations may be noted briefly)
2. **Proposed updates** — typed list: ADD / REMOVE / REPRIORITIZE,
   each with evidence citation and rationale
3. **Strategy before/after** — show the change, not just describe it
4. **Namespace pressure check** — absent namespaces assessed
5. **Conflicts** — named or cleared

Then ask the user to confirm before writing.

> "These updates reflect what the evidence demands. Confirm 'apply' to
> write strategy.md, or tell me what to adjust."

Write to `simulations/{topic}/strategy.md` only on confirmation.
```

---

### V-04 — Combined: Role Sequence + Phrasing Register
**Axes**: Signals-first reading order (read evidence before strategy); conversational, imperative-light register
**Hypothesis**: Reading signals before strategy gives the model fresh eyes — it sees what the evidence actually shows before pattern-matching it against the existing plan. Conversational register reduces defensive hedging and produces more direct proposals.

---

```markdown
# topic-plan — Revise the Signal Strategy

Here's the situation: you wrote a strategy for gathering signals on a topic.
You've gathered some signals. Now check if the strategy still makes sense.

Start with what you've learned, then compare it to what you planned.

---

**First, read the signals.**

Find everything under `simulations/{topic}/` — all the artifacts gathered
so far. Read them before you open strategy.md. You want fresh eyes on the
evidence before you see the plan.

As you read each signal, just note what it showed. Don't try to match it
to the strategy yet. What did this signal actually tell you?

---

**Now read the strategy.**

Open `simulations/{topic}/strategy.md`. Now you can compare:

What did the signals show that the strategy didn't plan for?
What did the strategy plan for that the signals suggest isn't needed?
What's in the right place but should probably move up or down in priority?

These are the three questions that matter. Work through them.

---

**Write out your proposals.**

For each gap you found, make a concrete proposal. Use one of these labels:

- **ADD** — something new that should be in the strategy
- **REMOVE** — something in the strategy that's no longer needed
- **REPRIORITIZE** — right idea, wrong order or weight

Every proposal needs: the label, what it affects (which skill or namespace),
which signal led you here, and a short reason why.

If you didn't find any ADDs, say so. Same for REMOVEs and REPRIORITIZEs.
Cover all three, even if the answer is "nothing to change here."

---

**Check the namespace map.**

The Signal plugin has 9 namespaces: scout, draft, review, flow, trace,
prove, listen, program, topic. Look at which ones the strategy doesn't
cover. For each one that's absent, does the evidence suggest it should
be added, or is it reasonable to leave it out for now? Be direct.

---

**Look for contradictions.**

Did any two signals point in opposite directions? If so, say which ones
and what they conflict on. The revised strategy shouldn't paper over that —
it should make a call.

---

**Show the before and after.**

Before you ask for confirmation, show what the strategy looks like now
versus what you're proposing. Keep it compact — just the parts that change.

---

**Then ask before you write anything.**

Don't update strategy.md yet. Show the proposals and the before/after,
and ask:

> "Want me to apply these changes to strategy.md? Say 'apply' to confirm,
> or let me know what you'd change."

Only write the file once you get the go-ahead.
```

---

### V-05 — Combined: Output Format + Inertia Framing
**Axes**: Evidence-linked proposal table (minimal prose); explicit "hold / revise / drop" framing for existing strategy items
**Hypothesis**: Combining a tight output format with explicit keep/change/drop accounting forces the model to commit to each existing strategy item rather than only proposing additive changes — common failure mode is all additions, no removals.

---

```markdown
# topic-plan — Signal Strategy Revision

You are running a strategy revision pass for a Signal topic.

The strategy was written with a set of assumptions. Signals gathered since
then are evidence against those assumptions. Your output is a proposal set,
not a narrative. Show your work in tables.

---

## Inputs

Read both inputs completely before producing any output.

1. `simulations/{topic}/strategy.md` — the current strategy
2. All artifacts under `simulations/{topic}/` — gathered signals

---

## Part A: Signal Inventory

Build a table of signals read:

| Artifact | Namespace | Skill | Key Finding | Strategy Anticipated? |
|----------|-----------|-------|-------------|----------------------|
| ...      | ...       | ...   | 1 sentence  | Yes / No / Partial   |

"Strategy Anticipated?" = Yes if the strategy planned for this dimension,
No if the signal revealed something the strategy didn't cover,
Partial if the strategy touched it but underweighted it.

---

## Part B: Existing Strategy Audit

For each item currently in `strategy.md` (each planned skill or coverage area),
make a disposition:

| Strategy Item | Namespace | Disposition | Signal Evidence | Rationale |
|---------------|-----------|-------------|-----------------|-----------|
| ...           | ...       | HOLD / REVISE / DROP | artifact name | 1 sentence |

Valid dispositions:
- **HOLD** — signals confirm this item remains valuable as planned
- **REVISE** — item stays but needs adjustment (scope, priority, framing)
- **DROP** — signals show this item is no longer needed or out of scope

Every existing strategy item must appear in this table.
Omitting items is not allowed.

---

## Part C: New Coverage Proposals

For each "No" or "Partial" row in Part A, and for any namespace gap
identified below, propose additions:

| Proposed Addition | Namespace | Skill | Evidence | Priority | Rationale |
|-------------------|-----------|-------|----------|----------|-----------|
| ...               | ...       | ...   | artifact | H/M/L    | 1 sentence |

If no additions are warranted, include one row: "No additions — signals
confirm current coverage is sufficient."

---

## Part D: Namespace Gap Audit

| Namespace | In Strategy? | Signal Pressure to Add? | Recommendation |
|-----------|-------------|------------------------|----------------|
| scout     | Yes/No      | Yes/No/Partial          | Keep out / Add: [skill] |
| draft     | ...         | ...                     | ... |
| review    | ...         | ...                     | ... |
| flow      | ...         | ...                     | ... |
| trace     | ...         | ...                     | ... |
| prove     | ...         | ...                     | ... |
| listen    | ...         | ...                     | ... |
| program   | ...         | ...                     | ... |
| topic     | ...         | ...                     | ... |

Fill all 9 rows.

---

## Part E: Conflict Register

| Conflict | Signal A | Signal B | Direction A | Direction B | Recommended Resolution |
|----------|----------|----------|-------------|-------------|----------------------|
| ...      | artifact | artifact | e.g., "viable" | e.g., "blocked" | ... |

If no conflicts found: "No conflicting signals detected."

---

## Part F: Before/After Summary

Show only lines that change:

```
BEFORE  [namespace]: [skill list]
AFTER   [namespace]: [revised skill list]  (+addition / −removal / ~revision)
```

Omit namespaces with no changes.

---

## Confirmation Gate

Present all five parts above. Then ask:

> "Ready to apply? Reply 'apply' to update strategy.md with the REVISE
> dispositions from Part B and the additions from Part C. Or tell me
> what to adjust."

Do not write to `simulations/{topic}/strategy.md` until the user confirms.
```

---

## Variation Summary

| # | Axes | Core Bet | Key Rubric Risks Addressed |
|---|------|----------|---------------------------|
| V-01 | Output format | Table forces typed proposals at output time | C-04, C-07, C-08 |
| V-02 | Lifecycle emphasis | Hard stop gates prevent premature writing | C-05, C-03, C-02 |
| V-03 | Inertia framing | Prior/evidence metaphor improves delta quality | C-03, C-10 |
| V-04 | Role sequence + register | Signals-first reader finds gaps; conversational reduces hedging | C-02, C-03, C-06 |
| V-05 | Output format + inertia framing | Existing items audited explicitly; no omission escape hatch | C-04, C-08, C-09, C-10 |
