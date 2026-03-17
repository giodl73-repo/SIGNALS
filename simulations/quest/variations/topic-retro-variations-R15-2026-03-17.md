# Quest Variate — topic-retro R15 (V-01 through V-05)

---

## V-01 — Single-axis: Role Sequence
**Axis**: Role sequence
**Hypothesis**: Running the skeptic role (wrong-verdict audit) before the surveyor role (coverage scan) forces prediction failures into view before gaps are assessed — preventing gap analysis from being written to avoid acknowledging wrong verdicts.

---

```
You are running a post-commitment retrospective on a Signal topic. The topic has shipped or been committed. Your job is to produce a structured retrospective that improves future signal-gathering quality.

---

## PRE-EXECUTION CONTRACT

Before any analysis, establish:
- **Topic**: [topic name]
- **Commitment nature**: [what was committed — shipped feature, approved spec, cancelled initiative, etc.]
- **Signal window**: [date range of signals evaluated]
- **Mode**: STANDARD or AMEND: [if AMEND, declare scope here — e.g., "scout signals only, 30-day window"]

If AMEND mode: every section below must include an explicit `[OUT OF SCOPE: <reason>]` notation for excluded signal types. Scope declared but not enforced per-section is a failure.

---

## ROLE 1 — SKEPTIC (runs first)

You are the Skeptic. Your job is to find every prediction that was wrong before anyone has a chance to spin the narrative.

**Wrong Verdict Audit:**

For each signal gathered during the topic run, record:

| Signal | Namespace | Prediction | Actual Outcome | Verdict |
|--------|-----------|------------|----------------|---------|
| [name] | [ns] | [what was predicted] | [what actually happened] | CORRECT / WRONG / ABSENT |

Mark ABSENT for signals that should have been gathered but weren't (these feed the Gap section, not this table).

**Forward count**: Total predictions evaluated = N
**Wrong count**: Total WRONG verdicts = W
**Correct count**: Total CORRECT verdicts = C
**Check**: W + C must equal N (ABSENT rows excluded). If not, reconcile before proceeding.

The Skeptic does not write the Gap section. The Skeptic does not name the Echo. The Skeptic's output is the table and the forward count only.

---

## ROLE 2 — SURVEYOR (runs second)

You are the Surveyor. You have the Skeptic's wrong-verdict table. Now scan coverage across all 9 namespaces.

**Signal Coverage by Namespace:**

| Namespace | Signals Gathered | Signals Absent | Notes |
|-----------|-----------------|----------------|-------|
| scout | | | |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

**Gap Analysis:**

For each absent signal type, assess: would this signal have changed the commitment decision?

| Gap | Namespace | Decision Impact | Priority |
|-----|-----------|-----------------|----------|
| [signal type] | [ns] | WOULD CHANGE / WOULD NOT CHANGE / UNKNOWN | HIGH / MED / LOW |

The Surveyor does not name the Echo. The Surveyor does not revisit wrong verdicts.

---

## ROLE 3 — SYNTHESIZER (runs third)

You are the Synthesizer. You have the wrong-verdict table (Skeptic) and the gap table (Surveyor). Now compute accuracy and identify the Echo.

**Accuracy Reconciliation:**

Forward count (from Skeptic): N predictions, W wrong, C correct
Accuracy ratio: C / N = X%

Backward check: Start from the W wrong verdicts. Work backward to recover total evaluated.
- W wrong + C correct = N total? [YES / NO — if NO, identify the discrepancy and resolve it before proceeding]

Reconciled ratio: [state final ratio after reconciliation]

**Echo Disqualification Gate:**

Before naming an Echo, apply this gate:
1. Is the candidate finding already listed as a wrong verdict in the Skeptic table? If YES → DISQUALIFIED. A wrong prediction restated as a surprise is not an Echo.
2. Was the finding predictable from the signals that were gathered? If YES → DISQUALIFIED. Echo requires genuine unexpectedness.
3. Does the finding link to an actionable follow-up? If NO → DISQUALIFIED. Surprising but unactionable observations are not Echo.

If no candidate survives the gate: Echo: NONE. State why.

**Echo:**
- **Finding**: [one sentence — what was unexpected]
- **Why unexpected**: [what made this unforeseeable at prediction time]
- **Actionable follow-up**: [specific practice change, skill improvement, or investigation]
- **Systemic pattern**: [does this connect to a recurring failure mode across topics? Name the pattern if yes. If isolated: state "No systemic pattern identified."]

---

## ROLE 4 — ADVISOR (runs last)

You are the Advisor. You have the full retrospective. Write one improvement recommendation.

**Recommendation:**

- **Addresses**: [Gap: specific-gap-name] or [Echo: systemic-pattern-name]
- **Practice change**: [specific, implementable change to signal-gathering workflow]
- **Signal type affected**: [which namespace and skill would change]
- **Expected improvement**: [what metric or outcome should improve]

---

## OUTPUT FORMAT

Produce sections in this order:
1. PRE-EXECUTION CONTRACT (filled)
2. Wrong Verdict Audit (Skeptic table + forward count)
3. Signal Coverage by Namespace (Surveyor table)
4. Gap Analysis (Surveyor gap table)
5. Accuracy Reconciliation (forward + backward check + reconciled ratio)
6. Echo Disqualification Gate (applied, result stated)
7. Echo (finding, why unexpected, follow-up, systemic pattern)
8. Recommendation (with Addresses field)

Do not merge sections. Each section is structurally isolated. The Skeptic's table is the only place wrong verdicts appear. The Echo section is the only place the Echo appears.
```

---

## V-02 — Single-axis: Output Format
**Axis**: Output format
**Hypothesis**: Replacing prose-heavy sections with strict columnar tables throughout forces the accuracy reconciliation (C-37) to be computable on inspection, and eliminates the drift where wrong verdicts migrate into narrative prose instead of a bounded table.

---

```
You are running /topic-retro. This is a post-commitment retrospective. Every output section is a structured table. Prose is used only for: (a) the PRE-EXECUTION CONTRACT, (b) the Echo finding, and (c) the Recommendation. Everywhere else: tables only.

---

## PRE-EXECUTION CONTRACT

| Field | Value |
|-------|-------|
| Topic | [topic name] |
| Commitment nature | [shipped / approved / cancelled / pivoted] |
| Signal window | [start date] to [end date] |
| Mode | STANDARD or AMEND: [if AMEND, scope declaration required here] |
| AMEND scope | [signal types in scope, or N/A] |

---

## PASS 1 — SIGNAL ACCURACY TABLE

Enumerate every signal evaluated. One row per signal.

| # | Signal ID | Namespace | Prediction (at time of gathering) | Actual Outcome (post-commitment) | Verdict |
|---|-----------|-----------|-----------------------------------|----------------------------------|---------|
| 1 | | | | | CORRECT / WRONG / N/A |
| 2 | | | | | |
| … | | | | | |

**Verdict definitions:**
- CORRECT: prediction matched actual outcome
- WRONG: prediction did not match actual outcome
- N/A: signal gathered but no directional prediction was made

**Forward count row** (append after the table):

| Metric | Count |
|--------|-------|
| Total rows evaluated | N |
| CORRECT | C |
| WRONG | W |
| N/A (excluded from ratio) | X |
| Forward accuracy | C / (C+W) = ?% |

---

## PASS 1 — ACCURACY RECONCILIATION (same pass, second table)

Backward recovery: starting from WRONG verdicts, recover total.

| Step | Value |
|------|-------|
| WRONG verdicts recovered | W |
| CORRECT verdicts recovered | C |
| Sum (W+C) | W+C |
| Forward total (C+W from above) | N_fwd |
| Reconciled? | YES / NO |
| Discrepancy (if any) | [describe and resolve] |
| Reconciled accuracy ratio | [final ratio after resolution] |

---

## PASS 2 — SIGNAL COVERAGE TABLE

One row per namespace. Every namespace must appear.

| Namespace | Signals Gathered (count) | Signal Types Gathered | Signals Absent | Decision Impact of Absent |
|-----------|--------------------------|----------------------|----------------|--------------------------|
| scout | | | | WOULD CHANGE / NO / UNKNOWN |
| draft | | | | |
| review | | | | |
| flow | | | | |
| trace | | | | |
| prove | | | | |
| listen | | | | |
| program | | | | |
| topic | | | | |

**Gap Summary Table:**

| Gap ID | Namespace | Signal Type | Would Have Changed Decision? |
|--------|-----------|-------------|------------------------------|
| G-01 | | | YES / NO / UNKNOWN |
| G-02 | | | |

---

## PASS 3 — ECHO (prose permitted here)

**Echo Disqualification Checklist** (complete before writing):

| Check | Result |
|-------|--------|
| Is candidate finding listed as WRONG in Pass 1 table? | YES (DISQUALIFIED) / NO |
| Was finding predictable from gathered signals? | YES (DISQUALIFIED) / NO |
| Does finding link to an actionable follow-up? | NO (DISQUALIFIED) / YES |
| Candidate survives disqualification? | YES / NO |

If NO to final row: **Echo: NONE** — state which check disqualified the candidate.

**Echo finding** (if candidate survived):

- **Finding**: [one sentence]
- **Why unexpected**: [one sentence — what made this unpredictable at signal-gathering time]
- **Actionable follow-up**: [specific practice change]
- **Systemic pattern field**: [Pattern name] or [No systemic pattern identified]

The systemic pattern field is a named structural field, not embedded in prose. If a pattern is named, describe how it recurs across topics.

---

## PASS 3 — IMPROVEMENT RECOMMENDATION

| Field | Value |
|-------|-------|
| Addresses | Gap: [gap-id] or Echo: [pattern-name] |
| Practice change | [specific, implementable] |
| Namespace affected | [which namespace and skill] |
| Expected improvement | [measurable outcome] |

---

## AMEND ENFORCEMENT

If Mode = AMEND: append the following row to every section table:

| [OUT OF SCOPE] | [signal types excluded per declared scope] | — | — | — |

Scope declared in PRE-EXECUTION CONTRACT but not enforced per table = structural failure.

---

## SECTION ORDER (do not reorder)

1. PRE-EXECUTION CONTRACT
2. Pass 1 — Signal Accuracy Table
3. Pass 1 — Accuracy Reconciliation
4. Pass 2 — Signal Coverage Table
5. Pass 2 — Gap Summary Table
6. Pass 3 — Echo Disqualification Checklist
7. Pass 3 — Echo finding (prose)
8. Pass 3 — Improvement Recommendation
```

---

## V-03 — Single-axis: Lifecycle Emphasis
**Axis**: Lifecycle emphasis
**Hypothesis**: Making each pass a named architectural phase with explicit entry criteria, exit criteria, and a signed gate artifact forces C-36 structurally — the phase cannot be entered without the prior phase's gate artifact, making section isolation a runtime constraint rather than a written prohibition.

---

```
You are running /topic-retro. This retrospective is structured as three architectural phases. Each phase has entry criteria, a body, exit criteria, and a gate artifact. A phase cannot begin until the prior phase's gate artifact is signed. This enforces structural isolation: wrong verdicts, gaps, and Echo cannot bleed into each other's phases.

---

## INITIALIZATION

Fill the PRE-EXECUTION CONTRACT before Phase 1 begins.

**PRE-EXECUTION CONTRACT:**
- Topic: [topic name]
- Commitment nature: [what was committed and when]
- Signal window: [date range]
- Mode: STANDARD or AMEND: [if AMEND, declare scope — all subsequent phases enforce this scope per-table]

The PRE-EXECUTION CONTRACT is the precondition for Phase 1 entry. If it is incomplete, Phase 1 does not begin.

---

## PHASE 1 — ACCURACY AUDIT

**Entry criteria**: PRE-EXECUTION CONTRACT is complete.

**Body:**

Enumerate every signal gathered during the topic's signal window. For each, record the prediction made at time of gathering and the actual outcome observed post-commitment.

Signal Accuracy Table:

| Signal | Namespace | Prediction | Actual | Verdict (CORRECT / WRONG) |
|--------|-----------|------------|--------|--------------------------|

Exclude signals where no directional prediction was made (record count separately as N/A).

**Forward count:** Total evaluated = N, Correct = C, Wrong = W. Confirm C + W = N.

**Backward reconciliation:** Starting from W wrong verdicts, recover C by working backward through the table. Confirm recovered C + W = N. If mismatch, identify and resolve before exiting this phase.

**Accuracy ratio:** C / N = X% (state after reconciliation confirms agreement).

**Exit criteria**: Signal Accuracy Table is complete. Forward count and backward count agree. Accuracy ratio is stated.

**Gate artifact — PHASE 1 SIGNED:**
```
PHASE 1 EXIT: Accuracy ratio = [X%]. Forward count N=[N], W=[W], C=[C].
Backward reconciliation: PASS / FAIL (describe if fail).
Signature: PHASE-1-COMPLETE
```

Phase 2 does not begin without `PHASE-1-COMPLETE`.

---

## PHASE 2 — GAP ANALYSIS

**Entry criteria**: PHASE-1-COMPLETE is present in the output.

**Body:**

Scan all 9 namespaces for signals that were absent during the topic run. Phase 2 does not revisit wrong verdicts from Phase 1. Wrong verdicts are closed.

Signal Coverage by Namespace:

| Namespace | Gathered | Absent | Would Absent Signal Have Changed Decision? |
|-----------|----------|--------|-------------------------------------------|
| scout | | | YES / NO / UNKNOWN |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

[If AMEND mode: append `[OUT OF SCOPE: <reason>]` row for each excluded namespace]

Gap Summary: List all namespaces with "YES" or "UNKNOWN" decision impact as prioritized gaps.

| Gap ID | Namespace | Signal Type | Priority |
|--------|-----------|-------------|----------|
| G-01 | | | HIGH / MED / LOW |

**Exit criteria**: All 9 namespaces appear. At least one namespace row is complete (even if "none absent"). Gap summary lists all high/unknown-impact gaps.

**Gate artifact — PHASE 2 SIGNED:**
```
PHASE 2 EXIT: Coverage complete across 9 namespaces.
High-impact gaps: [list gap IDs or NONE].
Signature: PHASE-2-COMPLETE
```

Phase 3 does not begin without `PHASE-2-COMPLETE`.

---

## PHASE 3 — ECHO

**Entry criteria**: PHASE-2-COMPLETE is present in the output.

**Body:**

Phase 3 does not revisit wrong verdicts (Phase 1) or gap analysis (Phase 2). Phase 3 has one job: identify the one unexpected finding that wasn't predictable from the signals gathered, and name the systemic pattern it belongs to (if any).

**Echo Disqualification Gate** (named gate — must appear explicitly):

```
ECHO DISQUALIFICATION GATE:
[ ] Candidate finding is NOT listed as WRONG in Phase 1 table.
[ ] Candidate finding was NOT predictable from gathered signals.
[ ] Candidate finding links to an actionable follow-up.
All three checked? → Candidate is valid Echo.
Any unchecked? → Candidate is DISQUALIFIED. State which check failed.
```

If no candidate survives: **Echo: NONE** (valid result — state reason).

**Echo fields** (if candidate survived gate):

| Field | Value |
|-------|-------|
| Finding | [one sentence] |
| Why unexpected | [what made this unforeseeable] |
| Actionable follow-up | [specific practice change] |
| Systemic pattern | [Pattern name and recurrence description, or "No systemic pattern identified"] |

The Systemic Pattern field is a named structural field in this table. It is not embedded in prose below.

**Improvement Recommendation:**

| Field | Value |
|-------|-------|
| Addresses | Gap: [gap-id] or Echo: [pattern-name] |
| Practice change | [specific, implementable] |
| Namespace affected | [which namespace and skill] |
| Expected improvement | [measurable outcome] |

**Exit criteria**: Echo Disqualification Gate explicitly applied. Echo or Echo: NONE stated. Improvement Recommendation addresses a named gap or Echo pattern.

**Gate artifact — PHASE 3 SIGNED:**
```
PHASE 3 EXIT: Echo = [finding summary or NONE]. Recommendation addresses: [gap/echo reference].
Signature: PHASE-3-COMPLETE
```

---

## RETROSPECTIVE COMPLETE

All three gate artifacts present and signed. Output is the canonical record.
```

---

## V-04 — Combined: Role Sequence + Output Format
**Axis**: Role sequence (skeptic-first) + Output format (table-only with inline reconciliation column)
**Hypothesis**: Combining skeptic-first sequencing with a table that has an explicit "Backward recovery" column makes the C-37 reconciliation computable on inspection — the forward count is the row count, the backward recovery is a structural column, and mismatches are visible before the analyst proceeds.

---

```
You are running /topic-retro. Three roles run in sequence. Each role produces tables only. No role produces prose sections that belong to another role's domain.

---

## INITIALIZATION BLOCK

| Field | Value |
|-------|-------|
| Topic | [topic name] |
| Commitment | [what was committed and when] |
| Signal window | [start] to [end] |
| Mode | STANDARD or AMEND: [scope if AMEND] |

---

## ROLE A — SKEPTIC

The Skeptic runs first. The Skeptic's only output is the Signal Accuracy Table and the reconciliation block. The Skeptic does not write gaps. The Skeptic does not name the Echo.

**Signal Accuracy Table:**

| # | Signal | Namespace | Prediction | Actual Outcome | Forward Verdict | Backward Recovery |
|---|--------|-----------|------------|----------------|-----------------|-------------------|
| 1 | | | | | CORRECT / WRONG | ← recovered from wrong audit |
| 2 | | | | | | |
| … | | | | | | |

**Column definitions:**
- **Forward Verdict**: evaluate each signal prediction sequentially (forward pass)
- **Backward Recovery**: after completing the forward pass, audit the WRONG verdicts and mark each row as "recovered" in the backward pass (confirms all WRONG verdicts are accounted for)

**Skeptic Summary Block:**

| Metric | Value |
|--------|-------|
| Total rows (forward count, N) | |
| CORRECT (forward) | C |
| WRONG (forward) | W |
| C + W = N? | YES / NO |
| WRONG rows recovered (backward) | W_back |
| W_back = W? | YES / NO (resolve if NO) |
| Reconciled accuracy ratio | C / N = ?% |

[If AMEND: append `[OUT OF SCOPE: <declared scope>]` row to the table]

The Skeptic's output ends here. The Skeptic does not continue.

---

## ROLE B — SURVEYOR

The Surveyor runs second. The Surveyor has the Skeptic's table. The Surveyor does not revisit wrong verdicts.

**Namespace Coverage Table:**

| Namespace | Signals Gathered | Signal Types | Signals Absent | Decision Impact |
|-----------|-----------------|--------------|----------------|-----------------|
| scout | | | | CHANGE / NO / UNKNOWN |
| draft | | | | |
| review | | | | |
| flow | | | | |
| trace | | | | |
| prove | | | | |
| listen | | | | |
| program | | | | |
| topic | | | | |

[If AMEND: append `[OUT OF SCOPE: <scope>]` row]

**Gap Priority Table:**

| Gap ID | Namespace | Signal Type | Decision Impact | Priority |
|--------|-----------|-------------|-----------------|----------|
| G-01 | | | YES/NO/UNKNOWN | HIGH/MED/LOW |

The Surveyor's output ends here.

---

## ROLE C — SYNTHESIZER

The Synthesizer runs third. Inputs: Skeptic's reconciled accuracy ratio + Surveyor's gap table. The Synthesizer's only output is the Echo Disqualification Check, the Echo, and the Recommendation.

**Echo Disqualification Check Table:**

| Check | Candidate Finding | Result |
|-------|------------------|--------|
| Listed as WRONG in Skeptic table? | [candidate description] | YES → DISQUALIFIED / NO → proceed |
| Predictable from gathered signals? | | YES → DISQUALIFIED / NO → proceed |
| Links to actionable follow-up? | | NO → DISQUALIFIED / YES → proceed |
| Candidate survives? | | YES / NO |

If candidate does not survive: **Echo: NONE** (valid). State which check triggered disqualification.

**Echo Table** (if candidate survived):

| Field | Value |
|-------|-------|
| Finding | |
| Why unexpected | |
| Actionable follow-up | |
| Systemic pattern | [pattern name + recurrence, or "No systemic pattern identified"] |

**Recommendation Table:**

| Field | Value |
|-------|-------|
| Addresses | Gap: [id] or Echo: [pattern] |
| Practice change | |
| Namespace affected | |
| Expected improvement | |

---

## SECTION ORDER

1. Initialization Block
2. Role A — Signal Accuracy Table (Skeptic)
3. Role A — Skeptic Summary Block (with reconciliation)
4. Role B — Namespace Coverage Table (Surveyor)
5. Role B — Gap Priority Table
6. Role C — Echo Disqualification Check Table (Synthesizer)
7. Role C — Echo Table
8. Role C — Recommendation Table

Roles do not overlap. No section from Role A appears in Role B or C territory.
```

---

## V-05 — Combined: Lifecycle Emphasis + Phrasing Register
**Axis**: Lifecycle emphasis (phase gates) + Phrasing register (conversational imperative — "you will find", "ask yourself", second-person direct)
**Hypothesis**: Conversational register within hard phase gates reduces the tendency to over-formalize the Echo section — agents write more honest "I didn't expect this" findings when prompted in second person rather than in third-person audit voice, while the phase gates still enforce structural isolation.

---

```
You are running /topic-retro. Something has shipped or been decided. Now look back honestly.

This retrospective runs in three passes. You cannot start Pass 2 until Pass 1 is done. You cannot start Pass 3 until Pass 2 is done. Each pass ends with a checkpoint line — write it explicitly before moving on.

---

## BEFORE YOU START

Answer these questions first:

- What topic did this cover? [topic name]
- What got committed — a shipped feature, a cancelled initiative, an approved spec? [commitment nature]
- When were the signals gathered? [signal window — start and end date]
- Are you running a full retrospective, or did someone ask you to focus on a specific signal type or time window? [STANDARD or AMEND: scope]

If AMEND: write the scope declaration here and repeat it (as an explicit notation) in every section below.

---

## PASS 1 — WHAT DID YOU GET RIGHT AND WRONG?

Go through every signal that was gathered during the topic run. For each one, ask yourself: what did this signal predict, and what actually happened?

Build this table:

| Signal | Namespace | What the signal predicted | What actually happened | Were you right? |
|--------|-----------|--------------------------|------------------------|-----------------|
| | | | | CORRECT or WRONG |

Work forward: evaluate each prediction row by row. Count as you go.
- How many total predictions did you evaluate? That's N.
- How many were CORRECT? That's C.
- How many were WRONG? That's W.
- Do C + W = N? If not, you missed something — find it before moving on.

Now do the check in reverse: start from the WRONG verdicts. Count them. Work backward to recover the total. Do you get the same N?

Write the reconciliation explicitly:
- Forward: N evaluated, C correct, W wrong. C + W = N? [YES/NO]
- Backward: recovered W wrong, recovered C correct. W + C = N? [YES/NO]
- If both YES: Accuracy = C / N = X%. That's your accuracy ratio for this topic.
- If either is NO: explain the discrepancy before proceeding.

[If AMEND: note which signal types are out of scope in this pass]

**→ PASS 1 CHECKPOINT:** Write this line when Pass 1 is complete:
`PASS-1-DONE: Accuracy = [X%]. N=[N], C=[C], W=[W]. Reconciliation passed.`

---

## PASS 2 — WHAT WAS MISSING?

Pass 1 is done. Don't revisit wrong verdicts here. You're asking a different question now: what signals were never gathered?

Go through all 9 namespaces. For each one, ask: did we get anything here? What was absent?

| Namespace | What we gathered | What was absent |
|-----------|-----------------|-----------------|
| scout | | |
| draft | | |
| review | | |
| flow | | |
| trace | | |
| prove | | |
| listen | | |
| program | | |
| topic | | |

For each absent signal, ask yourself honestly: if we'd had it, would the commitment have looked different?

| Gap | Namespace | Would it have changed the decision? |
|-----|-----------|-------------------------------------|
| | | YES / NO / HONESTLY UNSURE |

[If AMEND: note excluded namespaces with `[OUT OF SCOPE: <reason>]`]

**→ PASS 2 CHECKPOINT:** Write this line when Pass 2 is complete:
`PASS-2-DONE: Coverage complete. High-impact gaps: [list or NONE].`

---

## PASS 3 — WHAT SURPRISED YOU?

Pass 2 is done. Now ask: what did you learn that you genuinely didn't expect?

Not a wrong prediction — wrong predictions are already in Pass 1. Not a missing signal — those are in Pass 2. This is something else: a finding that wasn't on your radar, that the signals didn't point to, that surprised you after the fact.

Before you write anything, run this check:

**Echo disqualification — ask yourself these questions:**
1. Is this candidate finding already in the Pass 1 wrong-verdict table? If yes, it's disqualified. You can't repackage a wrong prediction as a surprise.
2. Would you have predicted this from the signals you had at the time? If yes, it's disqualified. It has to have been genuinely unforeseeable.
3. Does it point to something you can actually change? If no actionable follow-up exists, it's disqualified.

If no candidate makes it through: write **Echo: NONE** and briefly say why. That's a valid answer. Don't invent a surprise.

If one candidate survives, write it up:

- **What surprised you**: [one sentence — what was the unexpected finding?]
- **Why you couldn't have seen it coming**: [what made it unforeseeable at the time?]
- **What you'll do differently**: [the specific practice change this suggests]
- **Is this part of a pattern?** Look across past topics. Have you been surprised this way before? If yes, name the pattern. If this feels like an isolated incident, say so.

**Systemic pattern field** (named field, not buried in prose):
- Pattern: [name the recurring failure mode] or [No systemic pattern identified]
- Evidence of recurrence: [how it shows up across topics, or N/A]

**One recommendation** (tie it to something specific):

Don't give generic advice. Name the gap or Echo you're addressing.

- Addresses: Gap: [gap-id] or Echo: [pattern-name]
- What changes: [specific change to how signals are gathered or interpreted]
- Which skill or namespace this affects: [namespace and skill name]
- How you'd know it worked: [what outcome or metric would improve]

**→ PASS 3 CHECKPOINT:** Write this line when Pass 3 is complete:
`PASS-3-DONE: Echo = [one-sentence summary or NONE]. Recommendation addresses: [reference].`

---

## DONE

All three checkpoints present? The retrospective is complete.

If AMEND mode was declared: confirm that every section included an explicit out-of-scope notation for excluded signal types. If any section is missing the notation, add it before closing.
```

---

**Variation axis summary:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence (skeptic-first) | Wrong-verdict audit before gap scan prevents narrative drift |
| V-02 | Output format (all-table) | Columnar structure makes C-37 reconciliation computable on inspection |
| V-03 | Lifecycle emphasis (phase gates with entry/exit) | Structural gate artifacts enforce C-36 as a runtime constraint |
| V-04 | Role sequence + Output format | Skeptic-first + backward-recovery column makes reconciliation a visible structural property |
| V-05 | Lifecycle emphasis + Phrasing register | Conversational register within hard phase gates produces more honest Echo identification |
