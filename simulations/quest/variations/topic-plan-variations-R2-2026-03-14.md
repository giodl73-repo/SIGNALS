# topic-plan Variations — Round 2

## Variation Axes Selected

- **Axis A** — Role sequence (strategy-first vs. signals-first vs. interleaved)
- **Axis B** — Output format (table-driven vs. prose vs. hybrid)
- **Axis C** — Inertia framing (prominence of no-change as default outcome)

Single-axis: V-01 (A), V-02 (B), V-03 (C). Combinations: V-04 (A+B), V-05 (B+C+register).

---

## V-01 — Axis A: Role Sequence (Strategy-First)

**Variation axis**: Role sequence — read strategy before signals.
**Hypothesis**: Reading strategy.md first primes the analysis for what was *expected*. When signals arrive second, surprises are more salient. This ordering makes the delta feel like a contrast, not just a reading exercise, and reduces inventory drift.

---

```
You are executing /topic:plan — revising the signal strategy for topic {{topic}}.

**Phase 1 — Read strategy.md first**

Read `simulations/{{topic}}/strategy.md` before reading any signal artifacts.

Extract and record:
- Namespaces covered and their planned skills
- Stated rationale for each coverage decision
- Gaps the strategy already acknowledges
- Implicit assumptions (things the strategy treats as settled)

Do not read signals yet. Build a clear model of what the strategy expected before looking at what actually arrived.

**Phase 2 — Read all signal artifacts**

Glob `simulations/{{topic}}/` and read every signal artifact file present. For each, record:
- Namespace and skill
- Date
- Key finding in 1–2 sentences

**Phase 3 — Identify the delta**

The delta is what signals revealed that the strategy did not anticipate.

Warning: A plain inventory of signal contents is the failure mode this step guards against. The delta names surprises — things the strategy assumed, implied, or missed that signals contradicted or revealed.

For each delta item, write: "Strategy assumed [X]. Signal [artifact name] revealed [Y]."

If no item passes that test, write: "No delta — all signals confirmed strategy expectations." You may stop here; no changes are needed.

**Phase 4 — Propose typed changes**

Using only the delta, propose changes in three categories. Every category must appear — use an explicit no-change row when a category is empty.

**ADD** — skills or namespaces the strategy lacks that signal evidence demands:
- Format: `[namespace/skill] — [reason] [artifact]`
- If none: "ADD: No changes warranted by current signals."

**REMOVE** — skills in the strategy that signals show are redundant or misdirected:
- Format: `[namespace/skill] — [reason] [artifact]`
- If none: "REMOVE: No changes warranted by current signals."

**REPRIORITIZE** — skills already planned that signals show are sequenced incorrectly:
- Format: `[namespace/skill]: [from priority X] → [to priority Y] — [reason] [artifact]`
- If none: "REPRIORITIZE: No changes warranted by current signals."

**Phase 5 — Before/after strategy summary**

Show a diff-style view of how the strategy would change. For each changed item:

```
BEFORE: [current namespace/skill state or text]
AFTER:  [proposed state or text]
WHY:    [artifact name] revealed [delta finding]
```

Items not changing are omitted.

**Phase 6 — Namespace gap audit**

Audit all 9 namespaces for coverage relative to the topic's current stage. Thin coverage is not automatically a gap — only flag it if the stage requires it.

scout | draft | review | flow | trace | prove | listen | program | topic

For each: state current coverage, stage-appropriate coverage, and gap if any.

**Phase 7 — Conflicting signals**

If any two artifacts contain findings that point in opposite directions on the same question, name them here and recommend how the revised strategy should handle the conflict. If none: state that explicitly.

**Phase 8 — Confirmation gate**

Present the full proposal. Do not modify `simulations/{{topic}}/strategy.md`.

Gate: "Reply **apply** to write these changes to strategy.md, or **cancel** to discard."

Do not touch strategy.md until the user replies "apply."
```

---

## V-02 — Axis B: Output Format (Table-Driven)

**Variation axis**: Output format — every phase expressed as a table.
**Hypothesis**: Table format makes omissions structurally visible. A missing row in a typed-proposal table is obvious; a missing paragraph is invisible. Forcing ADD / REMOVE / REPRIORITIZE into rows with a mandatory "No changes" row closes the silent-omission failure mode at the format level rather than relying on instruction compliance.

---

```
You are executing /topic:plan — revising the signal strategy for topic {{topic}}.

**Step 1 — Read inputs**

Read `simulations/{{topic}}/strategy.md` and every signal artifact in `simulations/{{topic}}/`.

**Step 2 — Strategy baseline table**

| Namespace | Planned Skills | Stated Rationale | Acknowledged Gaps |
|-----------|---------------|-----------------|-------------------|
| ...       | ...           | ...             | ...               |

**Step 3 — Signal inventory table** (intermediate work only — not the delta)

| Artifact | Namespace | Skill | Date | Key Finding |
|----------|-----------|-------|------|-------------|
| ...      | ...       | ...   | ...  | ...         |

**Step 4 — Delta table**

Warning: This table records what signals revealed that the strategy did not anticipate — NOT what signals exist. Each row names a surprise. If a signal only confirmed what the strategy expected, it does not appear here.

| Delta ID | What strategy assumed | What signal revealed | Artifact | Implication |
|----------|-----------------------|----------------------|----------|-------------|
| D-01     | ...                   | ...                  | ...      | ...         |

If no surprises exist: write one row — "No delta. All signals confirmed strategy expectations."

**Step 5 — Proposals table**

Proposals flow from delta rows. Every type must appear — use explicit no-change rows.

| Proposal ID | Type         | Namespace/Skill | Change Description | Delta Row | Evidence Artifact |
|-------------|--------------|-----------------|-------------------|-----------|-------------------|
| P-01        | ADD          | ...             | ...               | D-01      | ...               |
| —           | REMOVE       | No changes.     | —                 | —         | —                 |
| P-02        | REPRIORITIZE | ...             | ...               | D-02      | ...               |

**Step 6 — Before/after diff table**

Each changed item carries an inline evidence bracket.

| Item             | Before              | After                     | [Evidence]               |
|------------------|---------------------|---------------------------|--------------------------|
| scout/market     | Priority 3, Wave 2  | Priority 1, Wave 1        | [market-signal-YYYY.md]  |
| ...              | ...                 | ...                       | ...                      |

Items not changing are omitted.

**Step 7 — Namespace gap audit table**

All 9 namespaces must appear. Coverage is assessed relative to topic stage, not raw signal count.

| Namespace | Signals Present | Stage-Required | Gap |
|-----------|----------------|----------------|-----|
| scout     | ...            | ...            | ... |
| draft     | ...            | ...            | ... |
| review    | ...            | ...            | ... |
| flow      | ...            | ...            | ... |
| trace     | ...            | ...            | ... |
| prove     | ...            | ...            | ... |
| listen    | ...            | ...            | ... |
| program   | ...            | ...            | ... |
| topic     | ...            | ...            | ... |

**Step 8 — Conflict table**

| Conflict ID | Artifact A | Artifact B | Opposing Findings | Recommended Resolution |
|-------------|------------|------------|-------------------|----------------------|
| ...         | ...        | ...        | ...               | ...                  |

If no conflicts: one row — "No conflicting signals found."

**Step 9 — Confirmation gate**

Present proposals table. Do not write to `simulations/{{topic}}/strategy.md`.

Gate: "Reply **apply** to write all changes to strategy.md, or **cancel** to discard."
```

---

## V-03 — Axis C: Inertia Framing (Status Quo as Default)

**Variation axis**: Inertia framing — no-change is the baseline; proposals must overcome evidence inertia.
**Hypothesis**: Naming "no change" as the correct default outcome upfront shifts the burden of proof. Proposals must clear an explicit evidence bar. This suppresses hallucinated or thin-delta changes and forces the skill to report "strategy is current" when that is actually true — which is often.

---

```
You are executing /topic:plan — revising the signal strategy for topic {{topic}}.

The default outcome of this skill is: **no change to strategy.md**. A strategy revision is only warranted when signal artifacts reveal something the strategy did not anticipate. Your job is to determine whether that threshold is met — and if so, what exactly to change.

**Phase 1 — Read the strategy**

Read `simulations/{{topic}}/strategy.md`. Record what the strategy currently commits to: namespaces covered, planned skills, stated rationale, acknowledged gaps.

**Phase 2 — Read all signals**

Glob `simulations/{{topic}}/` and read every signal artifact. For each, record the key finding.

**Phase 3 — Test the inertia threshold**

For each signal, ask: "Did this find something the strategy did not anticipate?"

If yes: record as a delta. Format: "Strategy assumed [X]. [Artifact] revealed [Y]. This changes the strategy because [Z]."

If no: record as confirmation. Format: "[Artifact] confirmed strategy assumption [X]."

Warning: A plain inventory of signals ("these signals exist") is not the delta. Do not proceed to proposals unless at least one genuine delta exists. If no delta clears the threshold, report: "Strategy is current — all signals confirm the plan. No changes proposed." Then stop.

**Phase 4 — Typed proposals** (only if delta exists)

Organize proposals by type. Every type gets an explicit entry.

**ADD** — skills or namespaces not in the current strategy that signal evidence demands:
- Each entry: `[namespace/skill] — [reason] — [artifact]`
- If none: "No additions warranted by current signals."

**REMOVE** — skills in the strategy that signals show are redundant or wrong:
- Each entry: `[namespace/skill] — [reason] — [artifact]`
- If none: "No removals warranted by current signals."

**REPRIORITIZE** — skills already planned that signals show are sequenced incorrectly:
- Each entry: `[namespace/skill]: [from] → [to] — [reason] — [artifact]`
- If none: "No reprioritization warranted by current signals."

**Phase 5 — Before/after view**

For each proposed change, show exactly what moves:

```
BEFORE: [current strategy text or state]
AFTER:  [proposed text or state]
WHY:    [artifact] revealed [delta finding]
```

**Phase 6 — Namespace gap audit**

Assess current signal coverage against the topic's stage across all 9 namespaces:

scout | draft | review | flow | trace | prove | listen | program | topic

Thin coverage is not automatically a gap. Only flag a namespace if the topic's current stage requires that coverage to be present. State your stage reasoning.

**Phase 7 — Conflicting signals**

Name any two artifacts that point in opposite directions on the same question. Recommend how the revised strategy should handle the conflict. If none exist, state that explicitly.

**Phase 8 — Confirmation gate**

If changes are proposed:
- Present the full proposal
- Gate: "Reply **apply** to update strategy.md with the above changes, or **cancel** to leave it unchanged."

If no changes are proposed:
- Report: "Strategy is current — no changes proposed."

Do not modify `simulations/{{topic}}/strategy.md` until "apply" is received.
```

---

## V-04 — Axes A + B: Strategy-First Sequence + Table Format

**Variation axes**: Role sequence (A) combined with table-driven output (B).
**Hypothesis**: Reading strategy before signals sets expectations baseline, then all outputs flow into tables with mandatory rows. The combination closes two independent failure modes simultaneously: inventory bias (from A) and silent omission (from B). The delta table structurally enforces the "surprise" test because each row must name a strategy assumption alongside the signal finding.

---

```
You are executing /topic:plan — revising the signal strategy for topic {{topic}}.

**Phase 1 — Read strategy.md first**

Before reading any signal artifacts, read `simulations/{{topic}}/strategy.md`.

Fill this table from the strategy:

| Namespace | Planned Skills | Stated Rationale | Acknowledged Gaps | Implicit Assumptions |
|-----------|---------------|-----------------|-------------------|----------------------|
| ...       | ...           | ...             | ...               | ...                  |

This is your expectations baseline. Every signal will be evaluated against it.

**Phase 2 — Read signal artifacts**

Glob `simulations/{{topic}}/` and read every signal artifact.

Fill this table:

| Artifact | Namespace | Skill | Date | Key Finding |
|----------|-----------|-------|------|-------------|
| ...      | ...       | ...   | ...  | ...         |

**Phase 3 — Delta table**

Compare signal findings against strategy expectations from Phase 1.

Warning: This table names surprises — findings that the strategy did not anticipate. A plain inventory of signal contents is not the delta and fails this step. Each row must pair a strategy expectation with the signal that contradicted or exceeded it.

| Delta ID | Strategy Expected | Signal Found | Artifact | Change Implication |
|----------|--------------------|--------------|----------|--------------------|
| D-01     | ...                | ...          | ...      | ...                |

If no surprises: one row — "No delta. All signals confirmed strategy expectations."

**Phase 4 — Proposals table**

Proposals flow from delta rows only. Every type must appear — mandatory no-change rows where empty.

| Proposal ID | Type         | Namespace/Skill | Change Description | Delta Row | Evidence Artifact |
|-------------|--------------|-----------------|-------------------|-----------|-------------------|
| P-01        | ADD          | ...             | ...               | D-01      | ...               |
| —           | REMOVE       | No changes.     | —                 | —         | —                 |
| P-02        | REPRIORITIZE | ...             | ...               | D-02      | ...               |

**Phase 5 — Before/after diff table**

Each changed item carries an inline evidence bracket. Items not changing are omitted.

| Item         | Before                  | After                    | [Evidence]                  |
|--------------|-------------------------|--------------------------|------------------------------|
| ...          | ...                     | ...                      | [artifact-name.md]           |

**Phase 6 — Namespace gap audit table**

All 9 namespaces must appear. Coverage is assessed relative to topic stage, not signal count.

| Namespace | Signals Present | Stage-Required | Gap |
|-----------|----------------|----------------|-----|
| scout     | ...            | ...            | ... |
| draft     | ...            | ...            | ... |
| review    | ...            | ...            | ... |
| flow      | ...            | ...            | ... |
| trace     | ...            | ...            | ... |
| prove     | ...            | ...            | ... |
| listen    | ...            | ...            | ... |
| program   | ...            | ...            | ... |
| topic     | ...            | ...            | ... |

**Phase 7 — Conflict table**

| Conflict ID | Artifact A | Artifact B | Opposing Findings | Recommended Resolution |
|-------------|------------|------------|-------------------|----------------------|
| ...         | ...        | ...        | ...               | ...                  |

If no conflicts: single row — "No conflicting signals found."

**Phase 8 — Confirmation gate**

Present the proposals table. Do not write to `simulations/{{topic}}/strategy.md`.

Gate: "Reply **apply** to write all changes to `simulations/{{topic}}/strategy.md`, or **cancel** to discard."
```

---

## V-05 — Axes B + C + Register: Table Format, Inertia Framing, Conversational Register

**Variation axes**: Table format (B) combined with inertia framing (C), written in direct second-person imperative.
**Hypothesis**: Tables enforce completeness without reading overhead. Inertia framing prevents thin-delta proposals. Conversational register — short sentences, second-person "you," minimal preamble — lowers cognitive load and makes each step feel like an action verb rather than a specification. Together, the three axes produce a prompt that is both structurally rigorous and easy to execute linearly.

---

```
You are running /topic:plan for {{topic}}.

Your job is to find what changed — not to list what exists.

Start here: **assume nothing needs to change.** Evidence overrides that assumption. Without evidence, the strategy stands.

---

**1. Read the strategy**

Open `simulations/{{topic}}/strategy.md`. Note what it commits to — namespaces, skills, rationale, gaps already known.

---

**2. Read the signals**

Glob `simulations/{{topic}}/`. Read every artifact there. Note what each one found.

---

**3. Find the delta**

For every signal, ask: "Did this find something the strategy didn't see coming?"

Don't list signals. Find surprises.

| Delta # | The strategy said...  | The signal showed... | Signal file |
|---------|-----------------------|----------------------|-------------|
| 1       | ...                   | ...                  | ...         |

If nothing surprised the strategy: write "No delta — all signals confirmed the plan." Stop here. No changes needed; report that to the user.

---

**4. Propose changes**

Only for what the delta justifies. Three types — all three must appear, even when empty.

| Type         | What                           | Why           | Signal file |
|--------------|--------------------------------|---------------|-------------|
| ADD          | ...                            | ...           | ...         |
| REMOVE       | No changes.                    | —             | —           |
| REPRIORITIZE | ...                            | ...           | ...         |

---

**5. Show before/after**

For each proposed change, show exactly what moves. Include the evidence bracket inline.

| Item              | Before                 | After                  | [Signal]                    |
|-------------------|------------------------|------------------------|-----------------------------|
| scout/market      | Priority 3, Wave 2     | Priority 1, Wave 1     | [market-signal-YYYY.md]     |
| ...               | ...                    | ...                    | ...                         |

---

**6. Check all 9 namespaces**

Does the topic's current stage need coverage in each one? Go through all nine explicitly.

| Namespace | Covered now? | Needed at this stage? | Gap? |
|-----------|--------------|-----------------------|------|
| scout     | ...          | ...                   | ...  |
| draft     | ...          | ...                   | ...  |
| review    | ...          | ...                   | ...  |
| flow      | ...          | ...                   | ...  |
| trace     | ...          | ...                   | ...  |
| prove     | ...          | ...                   | ...  |
| listen    | ...          | ...                   | ...  |
| program   | ...          | ...                   | ...  |
| topic     | ...          | ...                   | ...  |

---

**7. Flag conflicts**

Any two signals saying opposite things about the same question?

| Signal A | Signal B | What they disagree on | How to handle |
|----------|----------|-----------------------|---------------|
| ...      | ...      | ...                   | ...           |

None found: write one row saying so.

---

**8. Wait for confirmation**

Show the proposals. Don't touch `simulations/{{topic}}/strategy.md` yet.

If changes exist: "Ready to update strategy.md with the above changes. Reply **apply** to confirm, or **cancel** to discard."

If no changes: "Strategy is current. No changes proposed."
```

---

## Summary

| ID | Axes | Core Bet |
|----|------|----------|
| V-01 | A only — strategy-first sequence | Expectation contrast sharpens delta detection |
| V-02 | B only — table-driven output | Mandatory rows close silent omission at format level |
| V-03 | C only — inertia framing | Burden-of-proof default suppresses thin-delta proposals |
| V-04 | A + B — sequence + tables | Two independent failure modes closed simultaneously |
| V-05 | B + C + register — tables + inertia + conversational | Rigorous structure, low cognitive load, evidence-gated proposals |
