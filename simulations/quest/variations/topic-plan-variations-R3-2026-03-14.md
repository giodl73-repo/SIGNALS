Now I have enough context. The v3 rubric has 18 criteria (C-01 through C-18). The three new discriminating criteria for Round 3 are:
- **C-16**: Stage-drift detection (compare inferred vs declared stage)
- **C-17**: Conflict resolution coverage check (every conflict maps to a proposal or explicit waiver)
- **C-18**: Count-mechanical confidence (tier derived by counting files, not subjectively)

Generating 5 variations now.

---

# topic-plan — Round 3 Variations (V-01 through V-05)

**Rubric target**: v3 (C-01–C-18)
**New discriminating criteria**: C-16 (stage-drift detection), C-17 (conflict resolution coverage), C-18 (count-mechanical confidence)

---

## Variation Axes

| V | Single axis | Hypothesis |
|---|-------------|------------|
| V-01 | **Format** — column-annotation compression | All 18 criteria survive compression into table columns and inline annotation rules with minimum prose overhead |
| V-02 | **Lifecycle emphasis** — explicit phase boundaries with named entry conditions | Explicit STEP labels with phase-entry declarations make the protocol auditable at each transition; C-17 becomes a pre-proposal gate, not an afterthought |
| V-03 | **Role sequence** — stage inference runs first, governs all downstream | Making stage inference Phase A before signal reading means C-16 drift detection is architecturally load-bearing, not bolted on |
| V-04 | **Inertia framing** — vintage cost + deferral cost foregrounded throughout | Backward-looking accumulated gap cost (C-29 preview) combined with forward-looking deferral cost makes urgency structural rather than asserted |
| V-05 | **Phrasing register** — conversational guidance | First-person framing ("I'll read...", "I won't touch strategy.md until you say yes") makes structural machinery feel like assistance; C-16/C-17/C-18 embed naturally without checklist mode |

---

## V-01 — Minimal Footprint

**Axis**: Format (column-annotation compression)
**Hypothesis**: All 18 criteria can be encoded as table column annotations and inline rules with minimum prose overhead and the lowest reading cost.

```
You are running /topic:plan for topic: {topic}.

STEP 1 — READ STRATEGY
Read `simulations/{topic}/strategy.md`.
Record: declared stage, namespaces covered, planned skills, stated rationale, acknowledged gaps.
Do not proceed to Step 2 until this file has been read.

STEP 2 — READ SIGNALS
Glob `simulations/**/{topic}-*`. Read each file found.
If nothing is found, stop and report: "No signal artifacts found for {topic}."

Build the signal inventory table:

| File | Namespace | Date | Key finding (1 line) | Consistent with strategy? (yes / no / conflict) |

For every row where Consistent? = conflict, append immediately below that row:
  → Implication for strategy: [how the revised strategy must handle this contradiction]

Build the namespace coverage table (all 9 rows required — omitting any row is incomplete):

| Namespace | Signal count | Expected at [declared stage]? (yes / no / too early) | Gap? (yes / no) |

Namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

Stage inference: from signal density distribution above.
  scout/draft-dominant → exploration
  flow/trace-dominant → build
  prove/listen-dominant → validation

Write these four fields:
  Inferred stage: [value from density above]
  Declared stage: [from strategy.md Step 1]
  Stage drift detected: [Yes / No]
  Governing baseline: [inferred stage if drift Yes; declared stage if drift No]

If Stage drift = Yes, append:
  "Strategy declares [X]; signal portfolio suggests [Y].
   Inferred stage [Y] governs namespace gap evaluation.
   A stage-correction proposal will appear in Step 4."

STEP 3 — IDENTIFY THE DELTA
Frame this as a gap audit. The question is not "what changed?" but
"what is the strategy failing to account for, given what the signals now reveal?"

A plain inventory of signal files is not the delta. Name only what the strategy did not anticipate.

Write one bullet per finding in this form:
  → Strategy assumed [X] / Signal revealed [Y]

Categories (all required; write "No findings" per category if none apply):
  1. Missing coverage dimensions
  2. Obsolete or premature coverage
  3. Priority misalignments
  4. Signal conflicts — cite implication notes from Step 2
  5. Namespace gaps — cite Gap? column from Step 2, qualified by governing baseline

If signals fully confirm the strategy: write exactly one bullet:
  → Strategy assumed [current plan] / Signals confirmed — no gaps detected.

STEP 4 — PROPOSE CHANGES
Build the change proposals table.
One row per type minimum — write "None proposed" if a type has no changes.
A table missing any type row is an incomplete review.

| Type | Before | After | Evidence [file(s)] | Confidence | If skipped |

Column rules:
- Type: ADD / REMOVE / REPRIORITIZE
- Evidence: specific signal artifact filename(s) — not descriptions
- Confidence: count the cited files, then assign mechanically:
    High = 3+ consistent signal files / Medium = 2 files or mixed evidence / Low = 1 file
  Do not assign confidence by feel — the count determines the tier.
- If skipped: name what remains unaddressed or worsens if this proposal is deferred

If Stage drift = Yes, include as the first row:
  Type = REPRIORITIZE | Before = Stage: [declared] | After = Stage: [inferred]
  Evidence = [signal files used for inference] | Confidence = [computed] | If skipped = [what stays misaligned]

Conflict resolution check: For every row in the Step 2 inventory where Consistent? = conflict,
verify it maps to a proposal row above. For any implication that has no corresponding proposal, add:
  Type = NOTE | Before = [conflict description] | After = No action needed — [reason]
Every implication from Step 2 must appear in this table — either as a proposal or as an explicit waiver.

STEP 5 — CONFIRM BEFORE WRITING
strategy.md has NOT been modified.

Before/After summary:
| Namespace / Skill | Before | After | Confidence |

Confidence guide: High → strong support, apply; Medium → reasonable, review;
Low → sparse, consider deferring (use "Defer row N").

Options: YES / NO / Revise row N [instructions] / Defer row N

Waiting.

When confirmed: update `simulations/{topic}/strategy.md` with approved changes only.
```

---

## V-02 — Rich Protocol

**Axis**: Lifecycle emphasis (explicit phase boundaries with named entry conditions)
**Hypothesis**: Named STEP labels with explicit phase-entry declarations and dedicated first-class structures (conflict table, stage table, gate field) make the protocol auditable at each transition; C-17 becomes a hard pre-proposal gate rather than a post-hoc check.

```
You are running /topic:plan for topic: {topic}.
You will not modify strategy.md until the user explicitly confirms.

---

STEP 1 — Read the strategy

Read `simulations/{topic}/strategy.md`.

Extract:
| Field             | Value |
|-------------------|-------|
| Declared stage    |       |
| Namespaces covered|       |
| Planned skills    |       |
| Stated rationale  |       |
| Acknowledged gaps |       |

Phase entry for Step 2: AVAILABLE only after the table above is filled from the file.

---

STEP 2 — Read signals and surface conflicts

Glob `simulations/**/{topic}-*`. Read every file found.
If nothing found: stop. Report "No signal artifacts located for {topic}."

**Signal inventory:**

| File | Namespace | Date | Key finding | Consistent with strategy? (yes / no / conflict) |

**Conflict table** — one row per contradicting signal pair:

| Signal A | Signal B | Nature of contradiction | Implication for strategy |

If no conflicts found, write a single line: "No conflicts detected."
Do not omit this section — an absent conflict table is indistinguishable from a skipped audit.

**Stage inference:**

Tally namespace density from the inventory above:
  scout/draft-dominant → exploration
  flow/trace-dominant → build
  prove/listen-dominant → validation

| Field            | Value |
|------------------|-------|
| Inferred stage   | [from density above] |
| Declared stage   | [from Step 1] |
| Drift detected   | Yes / No |
| Governing baseline | [inferred if drift Yes; declared if drift No] |

If Drift = Yes:
  "Strategy declares [X]; signal portfolio suggests [Y].
   Inferred stage [Y] governs namespace evaluation from this point.
   A stage-correction proposal will appear in Step 4."

**Namespace coverage table** — evaluated against [governing baseline]:

| Namespace | Signal count | Expected at [governing baseline]? (yes / no / too early) | Coverage gap? |

All 9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.
A table with fewer than 9 rows is an incomplete audit.

Phase entry for Step 3: AVAILABLE only when signal inventory, conflict table (including
no-conflict declaration if none), stage table, and namespace table are all complete.

---

STEP 3 — Identify the delta

Frame this as a gap audit — not a change log.

The question: Given the signals and the governing stage baseline,
what is the strategy failing to account for?

A plain inventory of signal files is not the delta. Name only what the strategy did not anticipate.

Write one bullet per finding, using this form:
  → Strategy assumed [X] / Signal revealed [Y]

Required categories (write "No findings" if a category is empty):
  3a. Missing coverage dimensions
  3b. Obsolete or premature coverage
  3c. Priority misalignments
  3d. Signal conflicts — for each row in the Step 2 conflict table, cite the implication
      and state the recommended handling
  3e. Namespace gaps — for each gap row from Step 2, state whether it should be addressed
      at the governing stage

If signals fully confirm the strategy, write:
  → Strategy assumed [current plan] / Signals confirmed — no gaps detected.

Phase entry for Step 4: AVAILABLE only after all five delta categories are addressed.

---

STEP 4 — Pre-proposal conflict resolution gate

Before assembling the change table, verify:
Every row in the Step 2 conflict table with an Implication entry either:
  (a) maps to a proposal row you are about to write, or
  (b) is explicitly waived here with a reason.

List any unresolved implications:
  [ list or write "All implications resolved" ]

Gate status: OPEN ([N] unresolved — resolve above) / CLOSED (all implications resolved)

The change proposals table is available only when Gate status = CLOSED.

---

STEP 5 — Propose changes

One row per type minimum. Write "None proposed" for empty types.
A missing type row is an incomplete review.

| Type | Before | After | Evidence [file(s)] | Confidence | If skipped |

Column rules:
- Type: ADD / REMOVE / REPRIORITIZE
  If Drift = Yes: first row must be Type = REPRIORITIZE,
    Before = Stage: [declared], After = Stage: [inferred]
- Evidence: specific signal artifact filenames — not descriptions
- Confidence: count the cited files and assign by rule:
    High = 3+ consistent files / Medium = 2 files or mixed / Low = 1 file
  The count determines the tier. Do not assign subjectively.
- If skipped: name the specific gap or misalignment that persists

Conflict coverage verification:
After assembling the table, confirm every Step 2 conflict implication maps to a row above
or carries an explicit "No action needed — [reason]" annotation.

| Conflict (from Step 2) | Addressed by row | Or: No action needed — reason |

---

STEP 6 — Confirm before writing

strategy.md has NOT been modified.

Before / After summary:
| Namespace / Skill | Before | After | Confidence |

Confidence guide:
  High → strong signal support — apply
  Medium → adequate but mixed — review before applying
  Low → thin evidence — consider deferring (use "Defer row N")

Options: YES / NO / Revise row N [instructions] / Defer row N

Waiting for your response.

When confirmed: update `simulations/{topic}/strategy.md` with approved changes only.
```

---

## V-03 — Stage-First

**Axis**: Role sequence (stage inference runs as Phase A before signal reading, governs all downstream analysis)
**Hypothesis**: Running stage inference as a dedicated first computation — before reading signals for gap analysis — makes stage-drift detection architecturally central; all downstream namespace, gap, and proposal work inherits the corrected baseline rather than the potentially stale declared stage.

```
You are running /topic:plan for topic: {topic}.
You will compute the governing stage baseline first. All subsequent analysis depends on it.
strategy.md will not be modified until the user confirms.

---

PHASE A — ESTABLISH GOVERNING STAGE

Read `simulations/{topic}/strategy.md`.
Note the declared stage.
Note namespaces covered, planned skills, rationale, acknowledged gaps.

Glob `simulations/**/{topic}-*` and tally the namespace distribution of files found:

| Namespace group     | Files found | Stage signal |
|---------------------|-------------|--------------|
| scout + draft       |             | exploration  |
| flow + trace        |             | build        |
| prove + listen      |             | validation   |
| program + topic     |             | (lifecycle)  |

Dominant group by file count determines inferred stage.

| Field              | Value |
|--------------------|-------|
| Inferred stage     | [dominant group above] |
| Declared stage     | [from strategy.md] |
| Stage drift        | Yes / No |
| Governing baseline | [inferred if drift Yes; declared if drift No] |

If Drift = Yes:
  "strategy.md declares [X]; signal distribution suggests [Y].
   Governing baseline: [Y].
   This discrepancy will appear as a typed REPRIORITIZE row in Phase C.
   All namespace evaluation below uses [Y], not [X]."

Phase B available only after governing baseline is written.

---

PHASE B — READ SIGNALS AND SURFACE CONFLICTS

Read every signal file from the Phase A glob.
Do not fabricate signal content — cite only what is in the files.

**Signal inventory:**

| File | Namespace | Date | Key finding | Consistent with strategy? (yes / no / conflict) |

**Conflict table** — list every signal pair that contradicts each other or the strategy:

| Signal A | Signal B | Contradiction | Implication for strategy | Resolved by proposal? (fill in Phase C) |

If no conflicts found: write "No conflicts detected." Do not omit this section.

**Namespace coverage table** — evaluated against [governing baseline from Phase A]:

| Namespace | Signal count | Expected at [governing baseline]? (yes / no / too early) | Coverage gap? |

All 9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.
Evaluate each namespace against the governing baseline, not the declared stage.
A table with fewer than 9 rows is an incomplete audit.

Phase C available only after all three structures above are complete.

---

PHASE C — DELTA, CONFLICT RESOLUTION, AND PROPOSALS

**Delta framing:**
The question is not "what changed?" but "what does the strategy fail to account for?"

Write one bullet per finding:
  → Strategy assumed [X] / Signal revealed [Y]

Categories: missing dimensions, obsolete coverage, priority misalignments,
signal conflicts (cite Phase B conflict table), namespace gaps (cite Phase B gap column).

If signals confirm strategy: "Strategy assumed [current plan] / Signals confirmed — no gaps."

**Pre-proposal conflict resolution check:**
Before writing the change table, verify: every Phase B conflict row with an Implication entry
maps to a proposal below or is explicitly waived. Unresolved implications block the change table.

Gate: OPEN if any implication unresolved — resolve above. CLOSED when all resolved.
(Change table follows only when gate is CLOSED.)

**Change proposals:**

| Type | Before | After | Evidence [file(s)] | Confidence | If skipped |

Rules:
- One row per type (ADD / REMOVE / REPRIORITIZE). "None proposed" for empty types.
  Missing type row = incomplete review.
- If Drift = Yes: first row must be:
    Type = REPRIORITIZE | Before = Stage: [declared] | After = Stage: [governing baseline]
    Evidence = [files from Phase A used for inference] | Confidence = [computed] | If skipped = [what remains misaligned if stage row is deferred]
- Evidence: specific filenames only.
- Confidence: count the cited files — High = 3+ consistent / Medium = 2 or mixed / Low = 1.
  The count determines the tier. Do not assign by feel.
- If skipped: what coverage gap or misalignment persists if this change is not applied.

**Conflict coverage table:**
| Phase B conflict | Addressed by row # | Or: No action needed — reason |
Every row must be filled. An implication that disappears between Phase B and this table is a gap.

---

PHASE D — CONFIRM BEFORE WRITING

strategy.md has NOT been modified.

Post-apply preview — what the strategy would look like after all proposals are applied:

| Coverage area | Before | After | Confidence |

Confidence guide: High → apply; Medium → review; Low → consider "Defer row N."

Options: YES / NO / Revise row N [instructions] / Defer row N

Waiting.

When confirmed: update `simulations/{topic}/strategy.md` with approved changes only.
```

---

## V-04 — Inertia-Foregrounded

**Axis**: Inertia framing (vintage cost + deferral cost at every proposal row and at the confirmation gate)
**Hypothesis**: Placing backward-looking accumulated gap cost (vintage cost) alongside forward-looking deferral cost in every proposal row makes urgency structural rather than asserted; proposals carry their own inertia argument without requiring a separate analysis pass.

```
You are running /topic:plan for topic: {topic}.
For each proposed change you will name both the accumulated cost already incurred
(how long this gap has existed) and the deferral cost (what worsens if not applied now).
strategy.md will not be modified until the user confirms.

---

STEP 1 — READ STRATEGY AND SIGNALS

Read `simulations/{topic}/strategy.md`.
Extract: declared stage, namespaces covered, planned skills, rationale, acknowledged gaps.

Glob `simulations/**/{topic}-*`. Read every file found.
If nothing found: stop. "No signal artifacts found for {topic}."

**Signal inventory:**

| File | Namespace | Date | Key finding | Consistent with strategy? (yes / no / conflict) |

For every row where Consistent? = conflict, append:
  → Implication for strategy: [how the revised strategy must handle this]

**Stage inference:**
From the signal namespace distribution:
  scout/draft-dominant → exploration
  flow/trace-dominant → build
  prove/listen-dominant → validation

| Field              | Value |
|--------------------|-------|
| Inferred stage     | [from distribution] |
| Declared stage     | [from strategy.md] |
| Stage drift        | Yes / No |
| Governing baseline | [inferred if drift Yes; declared if drift No] |

If Drift = Yes:
  "Strategy declares [X]; signals suggest [Y]. Governing baseline: [Y].
   Stage correction will appear as a typed proposal in Step 3."

**Namespace coverage table** — evaluated against [governing baseline]:

| Namespace | Signal count | Expected at [governing baseline]? | Coverage gap? | Earliest gap signal date |

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.
Include the earliest signal date for gap rows — this anchors the vintage cost calculation.

---

STEP 2 — IDENTIFY THE DELTA

Frame this as a gap audit. Not: what changed. What is the strategy failing to account for?

Write one bullet per finding:
  → Strategy assumed [X] / Signal revealed [Y]

Categories: missing dimensions, obsolete coverage, priority misalignments,
signal conflicts (cite implication notes from Step 1), namespace gaps (cite gap rows from Step 1).

If signals confirm the strategy: "Strategy assumed [current plan] / Signals confirmed — no gaps."

---

STEP 3 — PRE-PROPOSAL CONFLICT RESOLUTION

Before writing proposals, list every conflict implication from Step 1 and verify it maps
to a proposal below or is explicitly waived.

| Conflict implication | Status: maps to row / waived — reason |

Gate: OPEN if any implication is unresolved — resolve here before proceeding.
Change table available only when all implications are resolved or waived.

---

STEP 4 — PROPOSE CHANGES

One row per type minimum (ADD / REMOVE / REPRIORITIZE).
Write "None proposed" for empty types. A missing type row is an incomplete review.

| Type | Before | After | Evidence [file(s)] | Confidence | Vintage cost | If skipped |

Column rules:
- Evidence: specific signal artifact filenames.
- Confidence: count the cited files and assign by rule:
    High = 3+ consistent files / Medium = 2 files or mixed / Low = 1 file
  Assign by counting — not by assessment. The cited file count determines the tier.
- **Vintage cost (backward-looking):** How long has this gap existed?
    Express as: elapsed time since earliest relevant signal (e.g., "Gap exists since [date] — [N] weeks").
    This is what has already been lost by not addressing it earlier.
- **If skipped (forward-looking):** What remains unaddressed or worsens next planning cycle
    if this proposal is deferred today?

If Drift = Yes: first row must be:
  Type = REPRIORITIZE | Before = Stage: [declared] | After = Stage: [governing baseline]
  Evidence = [inference files] | Confidence = [computed] | Vintage cost = [since earliest stage signal]
  If skipped = [what namespace alignment stays wrong if stage correction is deferred]

Conflict coverage: for each implication from Step 3, write the proposal row number
that addresses it or "No action needed — [reason]." Every implication must be accounted for.

---

STEP 5 — POST-APPLY PREVIEW AND CONFIRMATION

Before asking for confirmation, show what strategy.md would look like after
all proposals are applied — not just the diff.

**Post-apply coverage view:**

| Namespace / Skill | Current state | Post-apply state | Confidence |

strategy.md has NOT been modified.

Inertia reminder: Low-confidence proposals still carry vintage cost — what has already been lost.
Consider: "Defer row N" defers both the fix and the ongoing accumulation.

Confidence guide: High → apply; Medium → review; Low → weigh vintage cost before deferring.

Options: YES / NO / Revise row N [instructions] / Defer row N

Waiting.

When confirmed: update `simulations/{topic}/strategy.md` with approved changes only.
```

---

## V-05 — Conversational Register

**Axis**: Phrasing register (first-person guidance throughout)
**Hypothesis**: A conversational tone ("I'll read...", "I won't touch strategy.md until you say yes") makes structural machinery feel like assistance rather than form-filling, and naturally embeds C-16, C-17, and C-18 without breaking into checklist mode — while achieving the same criterion coverage as more formal variations.

```
You are running /topic:plan for topic: {topic}.

My job here is straightforward: look at what the signals have actually revealed since
the strategy was written, identify what the strategy is failing to account for, and
propose specific typed changes. I won't touch strategy.md until you say yes.

---

**Step 1: Read the strategy**

I'll start by reading `simulations/{topic}/strategy.md` so my proposals are grounded
in what the strategy actually says — the declared stage, which namespaces it covers,
what skills are planned, the rationale, and any gaps it already acknowledges.

---

**Step 2: Read every signal file, flag conflicts, and compute the governing stage**

Running: glob `simulations/**/{topic}-*`

I'll read each file and build a signal inventory:

| File | Namespace | Date | Key finding | Consistent with strategy? (yes / no / conflict) |

Where signals contradict each other or the strategy, I'll put them in a conflict table
and note what the strategy needs to do about it:

| Signal A | Signal B | What they disagree about | What the strategy needs to do about it |

If I find no conflicts, I'll write "No conflicts detected" rather than leaving the section
blank — an absent section is indistinguishable from a skipped check.

Then I'll work out where the topic actually is, from the signal distribution:
  - Scout/draft-heavy → exploration stage
  - Flow/trace-heavy → build stage
  - Prove/listen-heavy → validation stage

And I'll compare that to what strategy.md declares:

| Field | Value |
|-------|-------|
| Inferred stage (from signal distribution) | |
| Declared stage (from strategy.md) | |
| Stage drift? | Yes / No |
| Governing baseline (what I'll use downstream) | |

If drift: "The strategy says [X]; signal distribution suggests [Y]. I'll use [Y] as the
governing baseline for everything below — and I'll include a stage-correction proposal.
This matters because namespace gaps look different depending on which stage is correct."

Last, a namespace coverage table — all 9 namespaces, each evaluated against
the governing baseline (not the potentially stale declared stage):

| Namespace | Signals found | Expected at [governing baseline]? (yes / no / too early) | Gap? |

scout, draft, review, flow, trace, prove, listen, program, topic.
Fewer than 9 rows means I missed something.

---

**Step 3: Name what the strategy is missing**

Not: what has changed since the strategy was written.
What does the strategy fail to account for, given what we've now learned?

I'll write one bullet per gap:
  → Strategy assumed [X] / Signal revealed [Y]

Categories I'll cover (writing "No findings" rather than skipping):
  1. Missing coverage dimensions
  2. Obsolete or premature coverage
  3. Priority misalignments
  4. Signal conflicts — each row from Step 2's conflict table, with recommended handling
  5. Namespace gaps — each gap row from Step 2, qualified by the governing stage

If signals fully confirm the strategy, I'll write one row:
  → Strategy assumed [current plan] / Signals confirmed — no gaps detected.

---

**Step 4: Propose specific changes**

Before I write the change table, I'll verify: every conflict from Step 2 either maps
to a proposal below or is explicitly marked "no action needed." I won't let an implication
name a problem in one step and silently disappear before the proposals.

Conflict resolution check:
| Conflict (from Step 2) | Maps to row # | Or: No action needed — reason |
(Every row must be filled before I build the change table.)

Here's the change table:

| Type | Before | After | Evidence [file(s)] | Confidence | If skipped |

What I'll follow:
- One row for each of ADD, REMOVE, REPRIORITIZE. If a type has no proposals,
  the row says "None proposed" — leaving out a type means I didn't check it.
- If stage drift was detected: first row is Type = REPRIORITIZE, Before = Stage: [declared],
  After = Stage: [governing baseline]. The user confirms this like any other change.
- Evidence: the actual filenames — not descriptions.
- Confidence: I'll count the cited files and assign by rule —
    High = 3+ consistent files / Medium = 2 files or mixed evidence / Low = 1 file.
  The count sets the tier. I won't assign confidence by feel.
- If skipped: the specific gap or misalignment that persists if this change is deferred.

---

**Step 5: Here's what the strategy would look like after changes — then I'll wait**

Before asking for your confirmation, I'll reconstruct the post-apply strategy view
so you're saying yes to an outcome, not a list of edits:

| Coverage area | Before | After | Confidence |

I haven't touched strategy.md yet.

Confidence guide:
  High → solid evidence, apply
  Medium → reasonable support — your call
  Low → thin evidence — consider "Defer row N" to come back when more signals exist

What would you like to do?

YES to apply all / NO to cancel / Revise row N [your instructions] / Defer row N

Waiting.

---

Once you confirm, I'll update `simulations/{topic}/strategy.md` with the approved
changes and nothing else.
```

---

## Cross-Variation Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 reads strategy.md | Step 1 | Step 1 | Phase A | Step 1 | Step 1 |
| C-02 reads signal files | Step 2 glob | Step 2 glob | Phase A glob | Step 1 glob | Step 2 glob |
| C-03 delta not inventory | Step 3 anti-inventory note | Step 3 "gap audit, not change log" | Phase C "fail to account for" | Step 2 framing | Step 3 framing |
| C-04 typed changes | ADD/REMOVE/REPRIORITIZE table | Same + gate | Same + REPRIORITIZE Stage row first | Same + stage row | Same |
| C-05 confirm before writing | "Waiting." | "Waiting for your response." | "Waiting." | "Waiting." | "Waiting." |
| C-06 signal citations | Evidence column | Evidence column | Evidence column | Evidence column | Evidence column |
| C-07 before/after summary | Step 5 table | Step 6 table | Phase D post-apply preview | Step 5 post-apply | Step 5 |
| C-08 all three types | "None proposed" rule | "None proposed" rule | "None proposed" rule | "None proposed" rule | "None proposed" rule |
| C-09 namespace gap detection | 9-row table + Gap? column | 9-row table + Coverage gap? | 9-row against governing baseline | 9-row + earliest gap date | 9-row table |
| C-10 conflicting signals | Conflict annotation + implication | Dedicated conflict table | Dedicated conflict table | Conflict annotation + implication | Dedicated conflict table |
| C-11 gap-first delta | "failing to account for" + anti-inventory | "gap audit, not a change log" | "fail to account for" | "failing to account for" | "what the strategy fails to account for" |
| C-12 conflict detection in READ phase | Consistent? column in Step 2 | Conflict table in Step 2 | Conflict table in Phase B | Consistent? column in Step 1 | Conflict table in Step 2 |
| C-13 evidence-weighted gate | Confidence column + Defer row N | Confidence column + guide + Defer | Confidence column + guide + Defer | Confidence + vintage warning | Confidence column + guide + Defer |
| C-14 implication coupling in READ | Inline annotation rule | Dedicated conflict table with Implication column | Conflict table with Implication column | Inline annotation rule | Conflict table with "What the strategy needs to do" |
| C-15 stage-relative namespace rows | "Expected at [declared stage]?" column | "Expected at [governing baseline]?" per row | "Expected at [governing baseline]?" per row | "Expected at [governing baseline]?" per row | "Expected at [governing stage]?" per row |
| **C-16 stage-drift detection** | Inferred/Declared/Drift/Governing fields in Step 2 | Drift table in Step 2 with Governing baseline | Phase A dedicated stage computation with Governing baseline field | Stage inference table in Step 1 | Step 2 drift comparison table |
| **C-17 conflict coverage check** | Step 4 coverage check table | Step 4 gate + Step 5 coverage table | Phase C conflict coverage table | Step 3 gate + Step 4 coverage check | Step 4 conflict resolution check table |
| **C-18 count-mechanical confidence** | "Count the cited files — High = 3+..." | "Count the cited files and assign by rule" | "Count the cited files — High = 3+..." | "Count the cited files and assign by rule" | "I'll count the cited files and assign by rule" |

All five variations target all 18 criteria. Discriminating depth is at C-16 (V-03 strongest — Phase A makes it governing), C-17 (V-02 strongest — explicit gate field with OPEN/CLOSED state), C-18 (equal across all — all use the same count rule, varied only in register).
