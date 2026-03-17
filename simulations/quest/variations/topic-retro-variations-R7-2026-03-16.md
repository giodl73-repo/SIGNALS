# quest:variate — topic-retro — Round 7 (V-01 through V-05)

---

## V-01 — Axis: Lifecycle Emphasis
**Hypothesis:** Making phase boundaries structurally mandatory — with explicit seal declarations between every phase — forces correct Echo-before-accuracy ordering and makes the conflict audit unconditional, regardless of author discipline.

---

```
You are running /topic-retro for the topic provided.

A post-commitment retrospective reviews all signals gathered before the decision,
scores their predictions against what actually happened, identifies gaps, and
surfaces the one genuinely unexpected finding (the Echo). The Echo drives signal
design improvement.

AMEND: If an AMEND instruction is present, honor it throughout all phases —
inventory, accuracy, gaps, and Echo all stay within the amended scope.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 0 — PRIOR BELIEF CAPTURE (run before opening any signal files)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before reviewing any signal artifacts, record the team's prior belief:

**PRE-RETRO PRIOR BELIEF (captured at intake, before signals are opened)**

| Field | Entry |
|-------|-------|
| Default assumption about signal accuracy | [fill now, before reviewing artifacts] |
| Expected weakest namespace | [fill now] |
| Expected strongest namespace | [fill now] |
| Expected top gap | [fill now] |

This table must be filled before proceeding to Phase 1. It will be
compared against findings at Phase 5 close to demonstrate belief shift,
not assert it.

─────────────────────────────────────────
Phase boundary: Prior belief is now sealed. Proceed to Phase 1.
─────────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — ECHO IDENTIFICATION (run before accuracy scoring)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify the single most surprising finding from this retro — the thing that
genuinely was not expected. Name it now, before any accuracy analysis, to
prevent post-hoc absorption into the accuracy narrative.

Rules:
- Exactly one Echo. Not a list. Not a cluster.
- State it as a single sentence.
- Do not revise it in later phases. Conflicts are noted, not resolved.

**ECHO (LOCKED)**

| Field | Value |
|-------|-------|
| WHEN locked | Phase 1 — before accuracy scoring |
| LOCK STATUS | LOCKED |
| Echo statement | [single sentence] |
| Authorized conflict response | Log tension in Phase 3 conflict audit. Never revise this record. |

─────────────────────────────────────────
Phase boundary: Echo is now immutable. Proceed to Phase 2.
─────────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — SIGNAL INVENTORY AND ACCURACY SCORING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

List every signal artifact gathered for this topic. One row per artifact.
No artifact known to exist may be omitted.

For each artifact, record the prediction made at signal time and whether it
was correct in practice: C = Correct, P = Partial, W = Wrong.

**Signal Inventory**

| Namespace | Artifact | Date | Prediction at Signal Time | Result (C/P/W) |
|-----------|----------|------|--------------------------|----------------|
| | | | | |

**Per-Namespace Accuracy**

Formula: Score = (C×100 + P×50) / (C + P + W)
[e.g. C=3, P=1, W=2 → (300+50)/6 = 58.3]

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=3,P=1,W=2 → 58.3] |
|-----------|---|---|---|--------------------------------------------------------|
| scout | | | | |
| draft | | | | |
| review | | | | |
| flow | | | | |
| trace | | | | |
| prove | | | | |
| listen | | | | |
| program | | | | |
| topic | | | | |
| **TOTAL** | | | | |

**Overall Accuracy Judgment**

State an overall score, ratio, or qualitative rating grounded in the
per-namespace scores above.

─────────────────────────────────────────
Phase boundary: Accuracy scoring is now sealed. Proceed to Phase 3.
─────────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — CONFLICT AUDIT (unconditional — runs whether or not tension is perceived)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Review Phase 2 findings against the locked Echo from Phase 1.

This audit runs unconditionally. Silence is not a valid no-conflict signal.
You must produce an explicit result in every retro.

| Audit Question | Answer |
|----------------|--------|
| Does Phase 2 analysis suggest revising the Echo? | Yes / No |
| If yes: what is the tension? | [describe or N/A] |
| Resolution | Preserve original Echo. Log tension here. Do not revise. |
| Conflict audit result | CONFLICT DETECTED / NO CONFLICT |

─────────────────────────────────────────
Phase boundary: Conflict audit complete. Proceed to Phase 4.
─────────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — GAP ANALYSIS AND ECHO FEEDBACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Missing Signals**

Identify which signal types were absent. For each gap, name the namespace
and signal type. Generic statements ("we had few signals") do not qualify.

| Gap | Namespace | Signal Type | Would It Have Changed the Decision? | Actionable Fix |
|-----|-----------|-------------|-------------------------------------|----------------|
| | | | Yes / No / Maybe | [specific skill, question, or threshold] |

**Echo Feedback Loop**

Translate the locked Echo into a concrete change proposal. Not just
"we learned X" — but "therefore we should do Y differently."

| Echo (from Phase 1) | Change Proposal | Type |
|--------------------|-----------------|------|
| [paste Echo statement] | [new skill / rubric amendment / threshold adjustment] | skill / rubric / threshold |

**Calibration Trend** (if prior retro exists for this team or namespace)

Compare this retro's accuracy to a prior retro. Is prediction quality
improving, degrading, or stable? If no prior retro exists, state that.

─────────────────────────────────────────
Phase boundary: Gap analysis and feedback loop complete. Proceed to Phase 5.
─────────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — FOIL CLOSE (cost-of-inaction, belief-shift record)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Status-Quo Foil**

| | Without This Retro | With This Retro |
|--|-------------------|-----------------|
| PRE-RETRO prior belief (from Phase 0) | [paste Phase 0 default assumption] | — |
| POST-RETRO actual finding | — | [state what the retro revealed] |
| Signal accuracy assumption | [Phase 0 expected] | [Phase 2 actual score] |
| Weakest namespace assumption | [Phase 0 expected] | [Phase 2 actual] |
| Top gap assumption | [Phase 0 expected] | [Phase 4 actual] |
| Default action without retro | [what team would have done] | [what team will now do differently] |

This table closes the epistemic loop opened in Phase 0. Both columns are
now complete. The belief shift is demonstrated, not asserted.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
END OF RETRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## V-02 — Axis: Output Format (Table-Heavy with Formula Headers)
**Hypothesis:** Embedding the accuracy formula directly in column headers — with worked examples — produces mechanically consistent per-namespace scoring because the instruction is always co-located with the cell being filled, eliminating drift between stated formula and applied formula.

---

```
You are running /topic-retro for the topic provided.

Review all signals gathered before the commitment decision, score their
predictions against actual outcomes, identify gaps, and surface the one
unexpected finding that improves future signal design.

AMEND: If an AMEND instruction is present, apply it as a constraint to
every table — inventory, accuracy, gaps, and Echo stay within scope.

────────────────────────────────────────

TABLE 0 — PRE-RETRO INTAKE (fill before opening any signal file)

| Prior Belief Field | Your Entry (before reviewing artifacts) |
|-------------------|-----------------------------------------|
| Expected overall accuracy (high/med/low) | |
| Namespace you expect to score highest | |
| Namespace you expect to score lowest | |
| Signal type you expect to be missing | |
| Decision you think this retro will NOT change | |

Seal this table before proceeding.

────────────────────────────────────────

TABLE 1 — ECHO (identify before scoring accuracy)

Exactly one Echo: the single most surprising finding from this retro,
stated as one sentence. Identified before accuracy analysis to prevent
post-hoc absorption.

| ECHO (LOCKED) | |
|---------------|---|
| WHEN locked | Before accuracy scoring (Table 2) |
| LOCK STATUS | LOCKED |
| Echo statement (one sentence) | |
| Authorized conflict response | Log in Table 3 conflict column. Never revise this row. |

────────────────────────────────────────

TABLE 2 — SIGNAL INVENTORY

One row per artifact. No artifact known to exist may be omitted.
C = Correct, P = Partial, W = Wrong.

| Namespace | Artifact Name | Date | Prediction at Signal Time | Result (C/P/W) | Revision Flag? |
|-----------|---------------|------|--------------------------|----------------|----------------|
| | | | | | No / Yes → log in T3 |

────────────────────────────────────────

TABLE 3 — PER-NAMESPACE ACCURACY + CONFLICT LOG

Formula applied to each namespace row: Score = (C×100 + P×50) / (C + P + W)
Worked example: C=2, P=1, W=1 → (200+50)/4 = 62.5

Conflict column: Would Phase 2 findings suggest revising the Echo?
This column runs unconditionally — enter NO CONFLICT or describe tension.

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1→62.5] | Conflict with Echo? (NO CONFLICT or describe) |
|-----------|---|---|---|------------------------------------------------------|----------------------------------------------|
| scout | | | | | |
| draft | | | | | |
| review | | | | | |
| flow | | | | | |
| trace | | | | | |
| prove | | | | | |
| listen | | | | | |
| program | | | | | |
| topic | | | | | |
| **TOTAL** | | | | | Echo preserved. Conflicts logged above. |

**Overall Accuracy:** [score / ratio / qualitative rating derived from totals row]

────────────────────────────────────────

TABLE 4 — GAP ANALYSIS

| # | Missing Signal Type | Namespace | Would It Have Changed the Decision? | Actionable Fix (skill / question / threshold) |
|---|--------------------|-----------|------------------------------------|----------------------------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

────────────────────────────────────────

TABLE 5 — ECHO FEEDBACK LOOP

Translate the locked Echo into a change proposal.
Not "we learned X" — "therefore we will do Y."

| Echo (from Table 1) | Concrete Change Proposal | Change Type |
|--------------------|--------------------------|-------------|
| [paste Echo statement] | | new skill / rubric amendment / threshold |

────────────────────────────────────────

TABLE 6 — CALIBRATION TREND

Compare to the most recent prior retro for this team or namespace.
If no prior retro exists, state that explicitly.

| Dimension | Prior Retro | This Retro | Direction |
|-----------|-------------|------------|-----------|
| Overall accuracy | | | improving / degrading / stable / n/a |
| Weakest namespace | | | |
| Top gap type | | | |

────────────────────────────────────────

TABLE 7 — STATUS-QUO FOIL (closes the epistemic loop from Table 0)

PRE-RETRO column uses Table 0 entries (captured before signals were opened).
POST-RETRO column is filled now, after all tables complete.

| Dimension | Without This Retro (PRE — from Table 0) | With This Retro (POST — now) |
|-----------|----------------------------------------|------------------------------|
| Overall accuracy assumption | [Table 0 entry] | [Table 3 total score] |
| Weakest namespace assumption | [Table 0 entry] | [Table 3 actual] |
| Top gap assumption | [Table 0 entry] | [Table 4 actual] |
| Belief about decision quality | [Table 0 entry] | [post-retro revision] |
| What the team would have done | [default action without retro] | [what changes now] |

────────────────────────────────────────
```

---

## V-03 — Axis: Phrasing Register (Conversational/Imperative)
**Hypothesis:** Direct imperative phrasing — "Write the Echo now. One sentence. Lock it." — reduces hedging, prevents multi-Echo outputs, and produces tighter single-sentence Echoes because commands leave less room for interpretive drift than descriptive instructions.

---

```
You are running /topic-retro. Here's what you do: look back at every signal
gathered before the team committed to this feature, score the predictions
against reality, find the gaps, and name the one thing nobody saw coming.

AMEND instruction (if provided): stay within that scope for everything —
inventory, scoring, gaps, Echo. All of it.

════════════════════════════════════════

STEP 0 — Write down what you expect to find. Do this now, before looking
at any signal files.

Be direct: What do you think the overall accuracy will be? Which namespace
do you expect to have performed worst? What signal do you expect was
missing? What decision do you expect this retro will not change?

Write those answers down. They are your PRE-RETRO record. You will compare
them to your findings at the end to show whether the retro changed
anything — or just confirmed what you already knew.

Keep this record. You will need it for Step 5.

════════════════════════════════════════

STEP 1 — Name the Echo. Do this before scoring anything.

What is the single most surprising thing you discovered doing this retro?
The thing that genuinely was not expected. One sentence. Only one.

Write it here. Lock it.

**ECHO (LOCKED)**

| WHEN locked | LOCK STATUS | Echo Statement | If later analysis wants to change this |
|-------------|-------------|----------------|----------------------------------------|
| Step 1 — before scoring | LOCKED | [one sentence] | Log the tension. Keep this record. Never revise it. |

That's your Echo. It does not change. If you find something in Step 3 that
seems to contradict it, note the tension — but the Echo stays.

════════════════════════════════════════

STEP 2 — List every signal. Score each one.

One row per artifact. Do not leave any out. For each one, write down what
the prediction was at signal time, then score it: C (Correct), P (Partial),
or W (Wrong).

| Namespace | Artifact | Date | What Was Predicted | C / P / W |
|-----------|----------|------|-------------------|-----------|

Now group by namespace and score each group.

The formula: (C × 100 + P × 50) ÷ (C + P + W)
Quick check: C=2, P=1, W=1 → (200 + 50) ÷ 4 = 62.5

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1→62.5] |
|-----------|---|---|---|------------------------------------------------------|
| scout | | | | |
| draft | | | | |
| review | | | | |
| flow | | | | |
| trace | | | | |
| prove | | | | |
| listen | | | | |
| program | | | | |
| topic | | | | |
| TOTAL | | | | |

Give an overall verdict: score, ratio, or a plain "strong / moderate / weak"
grounded in the numbers above.

════════════════════════════════════════

STEP 3 — Run the conflict audit. This runs every time, not just when you
notice something.

Look at your Step 2 findings. Does anything there make you want to change
your Echo from Step 1?

Answer explicitly. Do not leave this blank.

| Does Step 2 suggest revising the Echo? | What is the tension (if any)? | What you do about it |
|----------------------------------------|-------------------------------|----------------------|
| YES or NO | describe or N/A | Keep the Echo. Log here. |

════════════════════════════════════════

STEP 4 — Find the gaps. Turn them into actions.

What signal types were missing? For each gap: name the namespace, name the
signal type, say whether it would have changed the decision, and give a
concrete fix — a specific skill to run, a question to ask, or a threshold
to set.

"We had few signals" is not a gap. Name the thing.

| Gap | Namespace | Signal Type | Changes the Decision? | Fix |
|-----|-----------|-------------|----------------------|-----|
| | | | Yes / No / Maybe | [specific action] |

Now turn the Echo into a concrete change:

What does the Echo tell you to do differently? Not just "we learned X."
Name the change: a new skill, a rubric edit, a threshold, a prompt.

| Echo | What Changes | Type |
|------|-------------|------|
| [Step 1 Echo] | | skill / rubric / threshold / other |

If you have a previous retro for this team or namespace, compare trends:
accuracy going up, down, or flat? If no prior retro, say so.

════════════════════════════════════════

STEP 5 — Close the loop. Show what changed.

Pull up your Step 0 record. Now compare it to what you found.

| What You Expected (Step 0) | What You Actually Found | Did It Change? |
|---------------------------|------------------------|----------------|
| Overall accuracy | | Yes / No |
| Worst namespace | | Yes / No |
| Missing signal type | | Yes / No |
| Decision that wouldn't change | | Yes / No |

Now fill the foil:

| | Without This Retro | With This Retro |
|--|-------------------|-----------------| 
| Default assumption | [your Step 0 expected accuracy] | [Step 2 actual score] |
| What the team would have done | [action without retro] | [action now] |
| Worst blind spot | [Step 0 expectation] | [Step 4 actual gap] |

The left column comes from your Step 0 record. Both sides now visible.
That is the value of the retro.

════════════════════════════════════════
```

---

## V-04 — Axes: Role Sequence + Lifecycle Emphasis (Combination)
**Hypothesis:** Assigning a dedicated "Echo Anchor" role that runs exclusively in Phase 0 — before any signal files are opened — makes C-22 structurally impossible to fake: the prior belief and the Echo are produced by a role whose only job is to write them before analysis begins, creating a temporally verifiable bracket.

---

```
You are running /topic-retro. Three roles execute in strict sequence.
No role may read the output of a later phase before completing its own.

AMEND: If an AMEND instruction is provided, each role applies it as a
scope constraint to its own output.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROLE A — THE ECHO ANCHOR
Runs: Before any signal files are opened.
Job: Capture the prior belief record and identify the Echo.
Constraint: Cannot reference any signal artifact content.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**ROLE A OUTPUT — PRIOR BELIEF RECORD (PRE-RETRO, before signals opened)**

You do not yet know what the signals say. Write from expectation only.

| Field | Entry (from expectation, no artifact data) |
|-------|--------------------------------------------|
| Expected overall accuracy level | high / medium / low |
| Namespace expected to score highest | |
| Namespace expected to score lowest | |
| Signal type most likely to be absent | |
| The one finding you expect NOT to be surprised by | |

Now identify the Echo: the single most surprising thing you anticipate
this retro will surface. You are naming it from intuition before analysis.
This is your pre-analysis Echo hypothesis.

After Phase B scoring completes, the actual Echo will replace or confirm
this hypothesis — but this record stands as the prior belief anchor.

**ECHO ANCHOR RECORD (LOCKED at Role A)**

| WHEN locked | LOCK STATUS | Pre-analysis Echo hypothesis | Authorized conflict response |
|-------------|-------------|------------------------------|------------------------------|
| Role A — before signals opened | LOCKED | [one sentence hypothesis] | If Role B/C findings conflict: log tension in Role C conflict audit. Never revise this record. |

─────────────────────────────────────────
Role A complete. Echo Anchor record is sealed. Signal files may now be opened.
Role B begins.
─────────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROLE B — THE SCORER
Runs: After Role A seals. Has access to all signal artifacts.
Job: Build the complete inventory, score every prediction, render accuracy.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**ROLE B OUTPUT — SIGNAL INVENTORY**

One row per artifact. No artifact may be omitted.
C = Correct, P = Partial, W = Wrong

| Namespace | Artifact | Date | Prediction at Signal Time | C/P/W |
|-----------|----------|------|--------------------------|-------|

**ROLE B OUTPUT — PER-NAMESPACE ACCURACY**

Formula: Score = (C×100 + P×50) / (C+P+W)
[e.g. C=3, P=2, W=1 → (300+100)/6 = 66.7]

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=3,P=2,W=1→66.7] |
|-----------|---|---|---|------------------------------------------------------|
| scout | | | | |
| draft | | | | |
| review | | | | |
| flow | | | | |
| trace | | | | |
| prove | | | | |
| listen | | | | |
| program | | | | |
| topic | | | | |
| **TOTAL** | | | | |

**ROLE B OUTPUT — OVERALL ACCURACY JUDGMENT**

State score, ratio, or rating grounded in the per-namespace totals above.

─────────────────────────────────────────
Role B complete. Accuracy scoring is sealed. Role C begins.
─────────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROLE C — THE ANALYST
Runs: After Role B seals. Has access to Role A and Role B outputs.
Job: Audit conflict, identify gaps, translate Echo, close the foil.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**ROLE C SECTION 1 — CONFLICT AUDIT (unconditional)**

Compare Role B findings to the Role A Echo Anchor record.
This audit runs in every retro. Silence is not a valid result.

| Does Role B suggest revising the Echo Anchor? | Tension (if any) | Resolution |
|-----------------------------------------------|-----------------|------------|
| YES / NO | [describe or N/A] | Echo Anchor preserved. Tension logged. |
| **Audit result** | | CONFLICT DETECTED / NO CONFLICT |

**ROLE C SECTION 2 — GAP ANALYSIS**

What signal types were absent? For each: namespace, signal type, decision
impact, and a concrete actionable fix.

| Gap | Namespace | Signal Type | Decision Impact | Actionable Fix |
|-----|-----------|-------------|----------------|----------------|
| | | | Yes/No/Maybe | [skill / question / threshold] |

**ROLE C SECTION 3 — ECHO FEEDBACK LOOP**

The Role A Echo hypothesis: does Role B data confirm, refine, or contradict it?
Name the actual Echo (confirmed from Role A or refined by Role B evidence).
Then translate it into a change proposal.

| Echo (final — from Role A or refined) | Change Proposal | Type |
|---------------------------------------|-----------------|------|
| | | skill / rubric / threshold |

**ROLE C SECTION 4 — CALIBRATION TREND**

Compare to the most recent prior retro for this team or namespace.
If no prior retro: state that explicitly.

| Dimension | Prior Retro | This Retro | Direction |
|-----------|-------------|------------|-----------|
| Overall accuracy | | | improving / degrading / stable / n/a |
| Weakest namespace | | | |

**ROLE C SECTION 5 — FOIL CLOSE**

Uses Role A prior belief record for the PRE column.
Fills POST column from Role B and Role C findings.

| Dimension | Without This Retro (PRE — Role A record) | With This Retro (POST — Role B/C findings) |
|-----------|------------------------------------------|-------------------------------------------|
| Overall accuracy | [Role A expected] | [Role B total score] |
| Weakest namespace | [Role A expected] | [Role B actual] |
| Top gap | [Role A expected] | [Role C actual] |
| Default team action | [what team would have done without retro] | [what changes based on Role C findings] |

PRE column: Role A record, written before signals were opened.
POST column: Role B/C findings, written after all analysis complete.
The bracket demonstrates belief shift rather than asserting it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RETRO COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## V-05 — Axes: Inertia Framing + Output Format (Combination)
**Hypothesis:** Framing the entire retro around the cost-of-inaction question — "what would the team have done without these signals?" — as the organizing entry point (rather than the inventory) produces stronger C-20 and C-22 pass rates because the default assumption is the first thing written, making it structurally impossible to fill in from hindsight.

---

```
You are running /topic-retro for the topic provided.

The framing question for this retro: What would have happened if you had
made the commitment without any signals at all? That is your status-quo
competitor. Everything this retro produces is measured against it.

AMEND: If an AMEND instruction is present, it applies to all sections.

────────────────────────────────────────────────────────────────

SECTION 0 — THE DEFAULT OUTCOME (write before opening signal files)

Name the status-quo. What would the team have done — and believed — if
no signals had been gathered and no retro had been run?

| Default Assumption (no signals) | Your Entry (before reviewing artifacts) |
|---------------------------------|----------------------------------------|
| Overall prediction confidence | high / medium / low — assumed by default |
| Implicit accuracy assumption | "we assume signals were X% accurate" |
| Weakest area assumed | which namespace, if any, was assumed risky |
| Gap assumed not to exist | which signal type was assumed sufficient |
| Commitment quality without retro | [characterize the decision without signal data] |

This is the baseline. Every finding in Sections 2–4 is compared against
this record. Fill it now. Once sealed, it is not revised.

SEAL: Default outcome record is complete. Signal files may now be opened.

────────────────────────────────────────────────────────────────

SECTION 1 — THE ECHO (before accuracy, before inventory)

What is the one thing this retro revealed that the status-quo would have
completely missed? One sentence. The genuine surprise. The finding that
most changes what you would have done without signals.

**ECHO (LOCKED)**

| Field | Value |
|-------|-------|
| WHEN locked | Section 1 — before inventory and accuracy |
| LOCK STATUS | LOCKED |
| Echo statement | [one sentence — the genuine surprise] |
| What the status-quo would have assumed instead | [what the default outcome (Section 0) implied about this] |
| Authorized conflict response | Log tension in Section 3 conflict audit. Do not revise this record. |

SEAL: Echo is locked. If Sections 2–3 produce tension with this record,
that tension is logged — not used to revise the Echo.

────────────────────────────────────────────────────────────────

SECTION 2 — SIGNAL INVENTORY AND ACCURACY

List every signal gathered for this topic. One row per artifact.
Score each against what actually happened.

| Namespace | Artifact | Date | Prediction at Signal Time | C/P/W | Cost Without This Signal |
|-----------|----------|------|--------------------------|-------|--------------------------|
| | | | | | [what team would have assumed without it] |

Per-namespace accuracy. Formula embedded in header:

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=2,W=1→80] | Default Assumption vs Actual |
|-----------|---|---|---|---------------------------------------------------|------------------------------|
| scout | | | | | [Section 0 assumption] vs [this score] |
| draft | | | | | |
| review | | | | | |
| flow | | | | | |
| trace | | | | | |
| prove | | | | | |
| listen | | | | | |
| program | | | | | |
| topic | | | | | |
| **TOTAL** | | | | | |

**Overall Accuracy vs Default:** State the gap between what was assumed in
Section 0 and what the per-namespace scores actually show.

────────────────────────────────────────────────────────────────

SECTION 3 — CONFLICT AUDIT (unconditional — always runs)

Does the Section 2 accuracy picture suggest revising the Section 1 Echo?

| Question | Answer |
|----------|--------|
| Does accuracy analysis conflict with the Echo? | YES / NO |
| If YES: describe the tension | |
| Resolution | Echo preserved. Tension logged here. Status-quo framing unchanged. |
| Audit verdict | CONFLICT DETECTED / NO CONFLICT |

────────────────────────────────────────────────────────────────

SECTION 4 — GAPS AND FEEDBACK

What was missing? For each gap: name it, say whether it would have
closed the gap between the default assumption and the actual outcome,
and give a concrete fix.

| Gap | Namespace | Signal Type | Would It Have Changed Section 0 Default? | Actionable Fix |
|-----|-----------|-------------|------------------------------------------|----------------|
| | | | Yes / No / Maybe | [specific skill / question / threshold] |

Echo feedback: translate the locked Echo into a change proposal.
Phrase it as cost-of-inaction: "Without this change, the status-quo
assumption will persist and the team will continue to [X]."

| Echo | Cost of Not Acting | Change Proposal | Type |
|------|--------------------|-----------------|------|
| [Section 1 Echo] | [what continues without action] | | skill / rubric / threshold |

Calibration trend (compare to prior retro if one exists):

| Dimension | Prior Retro | This Retro | Direction |
|-----------|-------------|------------|-----------|
| Overall accuracy vs default assumption | | | improving / degrading / stable / n/a |

────────────────────────────────────────────────────────────────

SECTION 5 — FOIL CLOSE

The PRE column is your Section 0 record, written before signals were opened.
The POST column is your Section 2–4 findings, written now.

| Dimension | Without This Retro (PRE — Section 0 record) | With This Retro (POST — Sections 2–4) |
|-----------|---------------------------------------------|---------------------------------------|
| Overall accuracy assumed | [Section 0 entry] | [Section 2 total score] |
| Weakest namespace assumed | [Section 0 entry] | [Section 2 actual worst] |
| Top gap assumed not to exist | [Section 0 entry] | [Section 4 actual gap] |
| Decision quality assumed | [Section 0 characterization] | [revised characterization] |
| What team does without retro | [Section 0 default action] | [Section 4 change proposal] |

PRE column: Section 0, written before signals were opened.
POST column: filled now, after all sections complete.

This is the demonstrated value of running the retro against the
status-quo competitor.

────────────────────────────────────────────────────────────────
```

---

## Variation Summary

| Variation | Primary Axis | Hypothesis |
|-----------|-------------|------------|
| V-01 | Lifecycle Emphasis | Explicit phase boundary declarations force correct ordering and make the conflict audit unconditional by structure |
| V-02 | Output Format | Formula-in-header with worked examples eliminates drift between stated formula and applied scoring |
| V-03 | Phrasing Register | Imperative commands reduce hedging and produce tighter single-sentence Echoes |
| V-04 | Role Sequence + Lifecycle | Dedicated Echo Anchor role running before signals are opened makes C-22 structurally unfakeable |
| V-05 | Inertia Framing + Output Format | Organizing the retro around the status-quo competitor makes prior-belief capture the mandatory first act |
