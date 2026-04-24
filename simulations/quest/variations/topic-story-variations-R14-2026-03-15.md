# topic-story Variations — Round 14

---

## V-01 — Single Axis: Pre-Composition Blocks as Hard Output Sections

**Axis:** Pre-composition structure — BLOCK D / BLOCK P / BLOCK B / LEDGER appear as locked output sections before narrative begins, with explicit closure rules.

**Hypothesis:** Treating Part 1 as a completed, standalone document section (not setup steps) forces analytical work to finish before prose begins. The boundary prevents discovery-during-composition, which produces summaries rather than syntheses.

---

```
You are writing a `topic-story` artifact for: **{topic}**.

The artifact has two parts. Part 1 must be complete before Part 2 begins.
Part 2 draws only from Part 1. Any finding not in the LEDGER may not appear in the narrative.

---

# PART 1 — PRE-COMPOSITION

Complete all four sections below. These are not notes — they are named output sections
of the final artifact.

---

## LEDGER

Every finding from the signal artifacts that belongs in the narrative. One sentence per entry.
Exhaustive within scope: if a finding is worth including, it goes here.
If a finding is not here, it cannot appear in the narrative.

- L-01:
- L-02:
- L-03:
...

---

## BLOCK D — Deltas

For each signal namespace represented, state the contrast between what was expected and
what was found. Omit signals that confirmed expectations without surprise.

Format for each entry:
[Namespace / Signal]: Expected [X]. Found [Y].

---

## BLOCK P — Pattern

One sentence. Self-contained. The cross-signal claim that references what two or more
signals show together — a claim that cannot be derived from any single signal alone.

This sentence must be readable without the surrounding narrative and must convey the
full synthetic claim.

**The pattern:**

---

## BLOCK B — Bridge

One sentence. This sentence appears verbatim in Beat 5 of the narrative.
It names the pattern (or its direct consequence) as the stated reason for
the recommendation verb that follows.

**The bridge:**

---

# PART 2 — NARRATIVE

Five beats. Draw only from the LEDGER. Do not introduce any finding not listed there.

---

## Beat 1 — What we set out to understand

Open with the recommendation verdict in the first sentence.
State the question the team was trying to answer and why it mattered.

---

## Beat 2 — What the signals revealed

For each signal type that contributes to the cross-signal pattern: one key finding,
one to two sentences. Not exhaustive — only findings that feed the synthesis.
Reference at least three distinct namespaces or artifact types.

---

## Beat 3 — What the signals say together

State BLOCK P verbatim as the opening sentence of this beat.
Then explain what the pattern means: the relationship, tension, or gap revealed.
A reader who reads only this beat must be able to identify the synthetic claim.

---

## Beat 4 — What remains uncertain

Name at least one specific open question. For each, state the decision-cost direction:
"If [X] resolves to [Y], the recommendation shifts from [verb] to [verb]."
Generic hedges without a stated direction fail this beat.

---

## Beat 5 — The recommendation

Name who is deciding and under what constraint.
State the recommendation verb: proceed / pause / pivot / abandon.
Include BLOCK B verbatim — do not paraphrase.
Close with one concrete next step.

---

# SIGNAL ARTIFACTS

{signal_artifacts}
```

---

## V-02 — Single Axis: Role Sequence (Analyst then Author)

**Axis:** Role sequence — an explicit analyst persona completes all analytical work before the author persona writes a single word of narrative.

**Hypothesis:** Naming distinct cognitive roles and enforcing a handoff between them prevents prose momentum from substituting for analysis. The analyst produces the ledger and pattern; the author's only job is voice and arc.

---

```
You are writing a `topic-story` artifact for: **{topic}**.

You will play two roles in sequence. Complete Role 1 fully before beginning Role 2.

---

# ROLE 1 — ANALYST

Your job: extract, compare, and synthesize. No narrative prose. No transitions.
Output structured analytical blocks only.

**Step A — Build the LEDGER**

Read every signal artifact. List every finding that is relevant to the feature decision.
One sentence per finding. Label each L-01, L-02, etc.
This list is exhaustive and closed: findings that don't appear here cannot appear in
the narrative.

**Step B — Build BLOCK D (Deltas)**

For each signal namespace, complete the frame:
"We expected [X]. We found [Y]."
Omit namespaces where signals confirmed expectations without meaningful contrast.
These are the surprises the narrative must surface.

**Step C — Build BLOCK P (Pattern)**

Write one sentence that states what the signals say together — a claim that requires
at least two signals and cannot be derived from any one of them.
This sentence must be self-contained: a reader who sees only this sentence grasps the
full synthetic claim.

**The pattern:**

**Step D — Build BLOCK B (Bridge)**

Write one sentence that connects the pattern to a specific recommendation verb.
This sentence names the pattern (or its consequence) as the reason for the verb.
This exact sentence will appear verbatim in Beat 5.

**The bridge:**

---

# ROLE 2 — AUTHOR

Your job: shape the analyst's output into a five-beat narrative with voice and arc.
You may not introduce any finding not present in the LEDGER.
You may not change the wording of BLOCK P or BLOCK B where they appear.

**Beat 1 — What we set out to understand**

State the recommendation verdict in your first sentence.
Then set the context: what question drove the signal gathering, and why the team needed
an answer.

**Beat 2 — What the signals revealed**

Draw from the LEDGER. For each signal type contributing to the pattern, state the
key finding in one to two sentences. Cover at least three distinct namespaces.
Do not recite the LEDGER — select what the story needs.

**Beat 3 — What the signals say together**

Open with BLOCK P verbatim.
Unpack the pattern in two to four sentences: the relationship or tension or gap.
Use at least one finding from BLOCK D to show where signals surprised expectations.

**Beat 4 — What remains uncertain**

State the open questions that remain after the signals. For each:
name the question specifically, then state the direction it would shift the
recommendation if resolved. "If [X], this moves from [verb] to [verb]."

**Beat 5 — The recommendation**

Name the role making the decision and their constraint.
State the verb.
Include BLOCK B verbatim.
Close with one concrete next step for that decision-maker.

---

# SIGNAL ARTIFACTS

{signal_artifacts}
```

---

## V-03 — Single Axis: Phrasing Register (Imperative Numbered with Inline Failure Conditions)

**Axis:** Phrasing register — every requirement is numbered, imperative, and followed by an explicit FAIL condition stating exactly what would cause that requirement to not pass.

**Hypothesis:** Inline failure conditions shift the model from attempting to satisfy the spirit of a requirement to testing its own output against a concrete binary. This reduces interpretive drift on criteria like "self-contained" and "verbatim."

---

```
Write a `topic-story` artifact for: **{topic}**.

Follow every numbered instruction. After drafting, verify each FAIL condition against
your output. Revise until no FAIL condition applies.

---

## PART 1 — PRE-COMPOSITION BLOCKS

Output these four blocks as named sections in the document.

**1. Build the LEDGER.**
List every finding from the signal artifacts you will use in the narrative.
Label each entry L-01, L-02, etc. One sentence per entry.
FAIL: any finding appears in Part 2 that has no corresponding LEDGER entry.

**2. Build BLOCK D.**
For each signal that contradicted or surprised expectations, write:
"[Namespace]: Expected [X]. Found [Y]."
Omit signals that confirmed expectations without contrast.
FAIL: Beat 3 contains no contrastive statement traceable to a BLOCK D entry.

**3. Build BLOCK P.**
Write one sentence. It must state what two or more signals show together that no
single signal shows alone. It must be readable in isolation without the surrounding text.
FAIL: the sentence requires the narrative to be read before its claim is understood.
FAIL: the sentence can be derived from a single artifact.

**4. Build BLOCK B.**
Write one sentence that names the pattern (or its consequence) as the reason for
the recommendation verb. This exact sentence appears in Beat 5 — not a paraphrase.
FAIL: Beat 5 contains a restatement rather than verbatim text.
FAIL: the sentence does not name the pattern as the cause of the recommendation.

---

## PART 2 — THE FIVE BEATS

**5. Write Beat 1 — What we set out to understand.**
The first sentence must state the recommendation verdict.
FAIL: the verdict appears anywhere other than the first substantive sentence.
FAIL: the first sentence is context, hedging, or framing rather than a verdict.

**6. Write Beat 2 — What the signals revealed.**
State the key finding for each signal type that feeds the pattern.
Reference at least three distinct namespaces or artifact types.
FAIL: fewer than three signal sources are identifiable.
FAIL: any finding in this beat has no LEDGER entry.

**7. Write Beat 3 — What the signals say together.**
Open with BLOCK P verbatim.
State the pattern's meaning: the relationship, tension, or gap.
Include at least one contrastive statement from BLOCK D.
FAIL: the opening sentence is not BLOCK P verbatim.
FAIL: no contrastive or delta statement appears.

**8. Write Beat 4 — What remains uncertain.**
Name at least one specific unresolved question.
For each question, state: "If [X] resolves to [Y], the recommendation shifts from
[verb] to [verb]."
FAIL: any uncertainty item lacks a stated direction-of-change.
FAIL: the uncertainty is stated as "more research may be needed" without naming
what research or what it would change.

**9. Write Beat 5 — The recommendation.**
Name the decision-maker role and constraint.
State the recommendation verb: proceed / pause / pivot / abandon.
Include BLOCK B verbatim.
Close with one concrete next step.
FAIL: no decision-maker role is named or implied.
FAIL: BLOCK B is paraphrased rather than quoted verbatim.
FAIL: recommendation weight contradicts the evidence described in the beats above.

---

## SIGNAL ARTIFACTS

{signal_artifacts}
```

---

## V-04 — Combined Axis: Pre-Composition Structure + Delta as Primary Anchor

**Axes:** Pre-composition structure (blocks as output sections) + delta surfacing emphasis (BLOCK D anchors the narrative arc, not just a required element).

**Hypothesis:** When delta discovery — "we expected X but found Y" — is elevated to the primary structural anchor of both the pre-composition and the narrative arc (rather than a check-the-box element), the synthesis gains the editorial voice that distinguishes a story from a report.

---

```
You are writing a `topic-story` for: **{topic}**.

This is a synthesis artifact, not a report. The difference: a report says what
each signal found. A synthesis says what the signals found that changed what we thought.

The anchor of this artifact is the delta — where signals diverged from expectation.
Build toward the delta. Write from the delta.

---

# PART 1 — PRE-COMPOSITION

Output all four blocks as named sections. The narrative in Part 2 draws only from these.

---

## LEDGER

Exhaustive list of findings that belong in the narrative. One sentence each.
Label L-01 through L-N. Findings not here may not appear in the story.

---

## BLOCK D — Deltas (PRIMARY ANCHOR)

For every signal namespace where the evidence contradicted, qualified, or extended
your expectation going in:

[Namespace]: **Expected:** [X]. **Found:** [Y]. **Decision relevance:** [one clause].

This block is the editorial core. If no delta exists for a namespace, omit it.
Aim for two to four entries. A block with only confirmations misses the point.

---

## BLOCK P — Pattern

One sentence derived from the deltas and other signals together.
What do the signals say together that the deltas alone cannot say?
State the synthetic claim. Self-contained — readable without the surrounding text.

**The pattern:**

---

## BLOCK B — Bridge

One sentence. The logical move from BLOCK P to the recommendation verb.
Names the pattern (or its consequence) as the explicit cause.
This sentence appears verbatim in Beat 5.

**The bridge:**

---

# PART 2 — NARRATIVE

The arc follows the delta: intent → discovery → pattern → decision.
Use only findings from the LEDGER.

---

## Beat 1 — What we set out to understand

State the recommendation verdict in the opening sentence.
Then: what was the team trying to learn, and what did they expect to find?
(Setting up the delta makes the arc land.)

---

## Beat 2 — What the signals revealed

Cover each signal namespace that contributes to the pattern. One to two sentences
per signal type. At least three distinct namespaces.
Lean into findings that will pay off in Beat 3's delta statement.

---

## Beat 3 — What the signals say together

Open with BLOCK P verbatim.
Then land at least one explicit delta from BLOCK D: name the expectation, name
the finding, state what the gap means for the decision.
This beat should feel like the story arriving somewhere unexpected.

---

## Beat 4 — What remains uncertain

Name the open questions. For each:
state the question specifically, then state the direction:
"If [X] resolves to [Y], this shifts from [verb] to [verb]."
Frame uncertainties as residual deltas — things the signals began to answer but
didn't fully resolve.

---

## Beat 5 — The recommendation

Name the decision-maker role and their constraint.
State the recommendation verb.
Include BLOCK B verbatim.
One concrete next step.

---

# SIGNAL ARTIFACTS

{signal_artifacts}
```

---

## V-05 — Combined Axis: Tabular LEDGER + Role Sequence

**Axes:** Output format (tabular LEDGER with structured columns) + role sequence (table-builder before narrative author).

**Hypothesis:** A tabular LEDGER with explicit columns (Namespace | Key Finding | Delta | Decision Weight) forces the extraction pass to be structured and auditable, and makes gaps in signal coverage visible before composition begins. Writing "from the rows" prevents both omission and fabrication.

---

```
Write a `topic-story` artifact for: **{topic}**.

The artifact is produced in two passes. Complete Pass 1 before writing a word of Pass 2.

---

# PASS 1 — TABLE-BUILD (Analyst mode)

Your only job in Pass 1: extract and structure. No prose. No transitions. No synthesis yet.

---

## LEDGER TABLE

Scan every signal artifact. For each finding worth including in the narrative,
add one row to this table. Be exhaustive within scope.

| ID | Namespace | Key Finding (one sentence) | Delta (expected vs. found, or "confirmed") | Decision Weight (high / medium / low) |
|----|-----------|---------------------------|---------------------------------------------|---------------------------------------|
| L-01 | | | | |
| L-02 | | | | |
...

Rules:
- One row per discrete finding. Do not combine findings.
- Delta column: if the signal surprised expectations, state "Expected [X]. Found [Y]."
  If it confirmed expectations, write "confirmed."
- Decision Weight: high = finding would alone shift the recommendation; medium = contributes;
  low = supporting color.

---

## BLOCK P — Pattern

After completing the table, write one sentence that states what the high- and
medium-weight rows say together that no single row says alone.
The sentence must be self-contained and must reference findings from at least
two different namespaces.

**The pattern:**

---

## BLOCK B — Bridge

One sentence. Names the pattern (or its consequence) as the reason for the
recommendation verb. This exact sentence appears verbatim in Beat 5.

**The bridge:**

---

# PASS 2 — NARRATIVE (Author mode)

Write the five-beat narrative. Source every claim from a LEDGER TABLE row.
Do not introduce any finding without a row number.
Do not paraphrase BLOCK P or BLOCK B where they appear.

---

## Beat 1 — What we set out to understand

State the recommendation verdict in the first sentence.
Then: the question being answered and why it mattered.

---

## Beat 2 — What the signals revealed

For each namespace with at least one high- or medium-weight row:
state the key finding in one to two sentences. Reference the row ID in brackets
(e.g., [L-03]) to keep traceability visible.
Cover at least three distinct namespaces.

---

## Beat 3 — What the signals say together

Open with BLOCK P verbatim.
Then: unpack the pattern using findings from at least two different namespaces.
Include at least one delta from a row where the Delta column is not "confirmed."

---

## Beat 4 — What remains uncertain

Name at least one open question with no corresponding high-weight row in the table —
a gap the signal gathering did not close.
For each: state the decision-cost direction.
"If [X] resolves to [Y], the recommendation shifts from [verb] to [verb]."

---

## Beat 5 — The recommendation

Name the decision-maker role and constraint.
State the recommendation verb: proceed / pause / pivot / abandon.
Include BLOCK B verbatim.
One concrete next step.

---

# SIGNAL ARTIFACTS

{signal_artifacts}
```

---

## Summary Table

| Variation | Primary Axis | Secondary Axis | Key Hypothesis |
|-----------|-------------|----------------|----------------|
| V-01 | Pre-comp blocks as locked output sections | — | Hard Part 1 / Part 2 boundary prevents discovery-during-composition |
| V-02 | Role sequence: analyst → author | — | Named persona handoff prevents prose from substituting for analysis |
| V-03 | Phrasing register: imperative + inline FAIL conditions | — | Inline binary tests reduce interpretive drift on "self-contained" and "verbatim" |
| V-04 | Pre-comp structure + delta as primary anchor | Combined | Elevating delta to the arc's structural center produces editorial voice |
| V-05 | Tabular LEDGER + role sequence | Combined | Structured columns make coverage gaps visible before composition; rows prevent fabrication |
