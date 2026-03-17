# topic-story Variations — Round 7 (V-01 through V-05)

---

## V-01 — Variation Axis: Role Sequence

**Hypothesis:** An explicit three-role pipeline (Signal Analyst → Pattern Builder → Narrator) with handoff certification forces pre-composition artifacts to exist structurally before narrative begins. Each role's output becomes a visible anchor, making cross-stage inconsistency self-revealing (C-18, C-20). Non-substitution is enforced by a stated rule at the handoff boundary (C-19).

---

```
You are producing a topic-story for: {{topic}}

Available signals (read all before proceeding):
{{signals}}

---

# THREE-ROLE PIPELINE

Complete all three parts in order. Do not skip or merge parts.

---

## PART 1 — Signal Analyst

Role: Read signals. Produce structured evidence output. No prose narrative.

Complete each field:

**POSTURE:** [One of: strong positive / mixed / conflicting / weak] — [Name the signals
that determined this]

**COVERAGE:** [List each signal namespace or artifact type referenced. Minimum 3.]
-
-
-

**DELTA CANDIDATES:** [For each signal that contradicted an expected or baseline finding]
- Expected [X] but found [Y] — [source signal]
- (continue as needed)

**OPEN QUESTIONS:** [For each unresolved question that would change the recommendation]
- If [X] resolves to [Y], verb shifts from [A] to [B]
- (continue as needed)

---

## PART 2 — Pattern Builder

Role: Receive Part 1 output. Derive pattern, delta, verb. No prose narrative.

Read the Signal Analyst output. Produce three labeled blocks only:

**The pattern:** [A single complete sentence stating what two or more signals show together
that no single signal shows alone. Self-contained — reads without surrounding text.]

**The delta:** Expected [X] but found [Y]. [The primary surprise from Part 1 candidates.
Self-contained.]

**Verb:** [proceed / pause / pivot / abandon] — Because [the pattern, referenced directly].

---

NON-SUBSTITUTION RULE: The pattern block above does not satisfy the requirement for a
pattern statement in Beat 3. The verb block above does not satisfy the bridge sentence
required in the Recommendation beat. Each placement is independently required in the
narrative. Prior-stage presence is not credit.

---

## PART 3 — Narrator

Role: Receive Parts 1-2. Write the five-beat story. Each beat independently satisfies its
requirement — prior-stage blocks are not credit.

Open with the recommendation verdict — one sentence that states the verb and its basis —
before any other content.

Then write the five beats:

---

### What we set out to understand
[The question or decision that drove signal gathering. 1-2 sentences. No findings yet.]

### What the signals revealed
[For each signal referenced: one sentence on the key finding. Include >= 3 distinct
namespaces. Name specific artifacts where possible. Not exhaustive — only findings that
bear on the synthesis.]

### What the signals say together
[State the cross-signal pattern. This placement is independently required — the Part 2
pattern block is not credit here. Begin: "The pattern: [full claim]." Then expand: name
the relationship, tension, or gap. 2-4 sentences.]

### What remains uncertain
[For each open question from Part 1: state it specifically. Then state the decision cost:
"If [X] resolves to [Y], this moves from [verb] to [verb]." No generic hedges.]

### The recommendation
[State the evidence posture from Part 1. Name the cross-signal pattern. Write the bridge
sentence: "Because [pattern], the recommendation is [verb]." This bridge sentence is
independently required here — the Part 2 verb block is not credit. End with: who should
make this decision, under what constraint.]

---

Consistency verification (run after writing):

| Claim            | Part 1     | Part 2     | Beat 3      | Rec. beat   |
|------------------|------------|------------|-------------|-------------|
| Evidence posture | stated     | —          | —           | must match  |
| Pattern stmt     | —          | stated     | must match  | referenced  |
| Rec. verb        | —          | stated     | —           | must match  |

If any "must match" cell differs from its Part anchor, revise before output.
```

---

## V-02 — Variation Axis: Output Format (Table-First Analysis Block)

**Hypothesis:** A table-structured analysis block with one row per claim makes non-substitution visible by forcing each placement into a discrete, labeled cell (C-19). Multi-stage consistency is enforceable by column alignment: a "Stage where this appears" column names exactly where each claim must recur in the narrative, and the table makes any missing placement an auditable gap (C-20).

---

```
You are producing a topic-story for: {{topic}}

Available signals:
{{signals}}

---

# ANALYSIS TABLES — complete before writing any narrative

Fill every cell. Leave no cell blank. An entry in an earlier table does not satisfy a
later table or a narrative placement.

---

## Table 1 — Evidence Inventory

| Signal / Artifact | Namespace | Key Finding (one sentence) | Confirms or Surprises baseline? |
|-------------------|-----------|---------------------------|---------------------------------|
| [name]            | [ns]      | [finding]                 | Confirms / Surprises: [what]    |
| (add rows)        |           |                           |                                 |

Minimum 3 namespaces represented.

---

## Table 2 — Synthesis Declarations

| Claim              | Content                                                              | Required at (narrative position)       |
|--------------------|----------------------------------------------------------------------|----------------------------------------|
| Evidence posture   | [strong positive / mixed / conflicting / weak] — [basis]            | Beat 5 (Recommendation)               |
| Cross-signal pattern | [What 2+ signals show together that no single signal shows alone] | Beat 3 AND Beat 5 bridge sentence      |
| Primary delta      | Expected [X] but found [Y]                                           | Beat 2 or Beat 3                       |
| Recommendation verb | [proceed / pause / pivot / abandon]                                 | Beat 5 bridge sentence                 |

Non-substitution rule: The "Required at" column names where each claim must appear
independently in the narrative. Completing this table does not satisfy any narrative
placement.

---

## Table 3 — Uncertainty Register

| Open Question | Resolution Path | If YES: verb shifts to | If NO: verb shifts to |
|---------------|----------------|----------------------|-----------------------|
| [question]    | [what would resolve it] | [verb]       | [verb]                |
| (add rows)    |                |                      |                       |

Minimum 1 row. Generic "more research needed" entries fail this table.

---

# STORY — write using the five beats

Opening sentence: State the recommendation verb and its basis in one sentence. This is
the first content in the story — no hedging, no context-setting before it.

---

### What we set out to understand
[Question or decision driving signal gathering. 1-2 sentences.]

### What the signals revealed
[Draw from Table 1. One sentence per signal. At least 3 namespaces visible. State the
primary delta from Table 2 using "expected X but found Y" language. Name specific
artifacts where possible.]

### What the signals say together
[State the pattern from Table 2, row "Cross-signal pattern." Required independently here
— Table 2 is not credit. Write: "The pattern: [full sentence]." Expand to name the
relationship or tension. 2-4 sentences. A reader must understand the pattern without
consulting Table 2.]

### What remains uncertain
[Draw from Table 3. One item per row. Write: "If [question], this moves from [current
verb] to [shifted verb]." No row may appear as a generic hedge here.]

### The recommendation
[State evidence posture — required independently here, Table 2 is not credit. Write the
bridge sentence: "Because [pattern], the recommendation is [verb]." Bridge required
independently here. Address the decision-maker role: who is deciding, under what
constraint.]

---

Consistency audit (run after writing):
For each row in Table 2's "Required at" column: confirm the claim appears at that
narrative position. Missing any placement is a structural error — revise before output.
```

---

## V-03 — Variation Axis: Lifecycle Emphasis (Expanded Pre-Composition Gates)

**Hypothesis:** Allocating explicit sub-steps and named gates to the pre-composition phase — with checkboxes that must be satisfied before narrative begins — produces better C-15/C-18 compliance by making "analytic work before writing" a structural requirement rather than an instruction. Narrative phase is compressed to a tight template, reducing summary drift.

---

```
You are producing a topic-story for: {{topic}}

Available signals:
{{signals}}

---

# PRE-COMPOSITION PHASE

Complete all four gates in order. You may not begin narrative writing until Gate 4 is
complete and all checkboxes are marked.

---

## Gate 1 — Signal Inventory

List every available signal. For each: namespace, artifact name, one-word disposition.

Format:
- [Namespace] / [Artifact] — [confirms / surprises / neutral]

(Minimum 3 namespaces. Continue until all signals are listed.)

[ ] Gate 1 complete: all signals listed with disposition.

---

## Gate 2 — Delta Extraction

For each "surprises" item from Gate 1, write the full contrastive statement.

Format: "Expected [X] based on [assumption], but [artifact] showed [Y]."

List all deltas. Identify the primary delta (star it or mark it PRIMARY).

[ ] Gate 2 complete: all deltas extracted, primary delta identified.

---

## Gate 3 — Pattern Derivation

Read all signals together. Write the cross-signal pattern.

Rules:
- One complete, self-contained sentence
- Not derivable from any single artifact
- Names a relationship, tension, or gap — not a list of findings
- Label it: The pattern: [sentence]
- Must stand independently without surrounding narrative

**The pattern:** [sentence]

**Posture assessment:** [strong positive / mixed / conflicting / weak] — [which signals
determine this]

**Verb derived from pattern and posture:** [proceed / pause / pivot / abandon]

[ ] Gate 3 complete: pattern is self-contained and cross-signal; posture declared; verb
derived.

---

## Gate 4 — Uncertainty Register

For each unresolved question that would shift the recommendation verb, write the full
entry.

Format: "[Open question] — If resolved as [X], verb moves to [verb]; if resolved as [Y],
verb stays at [current] or moves to [other]."

(Minimum 1 entry. Generic hedges fail this gate.)

[ ] Gate 4 complete: all uncertainty items have explicit decision-cost annotations.

---

PRE-COMPOSITION CHECKPOINT

Before writing the narrative, confirm all four gates are checked. The outputs above do
not satisfy narrative placements — each beat independently requires its stated content.

---

# NARRATIVE PHASE

Write the story in the five beats. Gate outputs are not credit for any beat.

Opening: State the recommendation verb and its basis in the first sentence. No hedging,
no context before this.

---

### What we set out to understand
One to two sentences. The question or decision. No findings yet.

### What the signals revealed
Draw from Gate 1. One key finding per signal referenced. At least 3 namespaces visible.
State the primary delta from Gate 2 using contrastive language.

### What the signals say together
State the pattern — independently required here, Gate 3 is not credit. Write:
"The pattern: [Gate 3 sentence restated]." Expand: name the relationship or tension in
1-3 additional sentences. A reader must grasp the pattern without reading the Gates.

### What remains uncertain
Draw from Gate 4. For each item: state the question specifically, then write the decision
cost. No generic hedges. Mirrors Gate 4 entries but in narrative prose.

### The recommendation
State the evidence posture — independently required here, Gate 3 posture is not credit.
Write the bridge: "Because [the pattern], the recommendation is [verb]." Bridge is
independently required here, Gate 3 verb is not credit. Name the decision-maker role or
constraint.

---

Post-composition consistency check:
- Evidence posture: Gate 3 AND Recommendation beat? [ ]
- Pattern: Gate 3 AND Beat 3 AND referenced in Recommendation beat? [ ]
- Verb: Gate 3 AND Recommendation beat? [ ]

Any inconsistency between positions is a structural error — revise before output.
```

---

## V-04 — Variation Axes: Role Sequence + Inertia Framing

**Hypothesis:** Adding an explicit Devil's Advocate role that argues for the status quo before the pattern is set produces stronger recommendation proportionality (C-07) because the counter-argument must be acknowledged in the synthesis, not ignored. Delta surfacing (C-09) is sharpened because the contrast is defined relative to an explicit baseline position, not just "initial assumptions."

---

```
You are producing a topic-story for: {{topic}}

Available signals:
{{signals}}

---

# FOUR-ROLE PIPELINE

Complete all four parts in order.

---

## PART 1 — Signal Analyst

Role: Inventory and classify all signals. Produce structured output only. No narrative.

**POSTURE:** [strong positive / mixed / conflicting / weak] — [signals driving this]

**COVERAGE:**
- [Namespace]: [artifact(s)], [disposition: confirms / surprises / neutral]
- (list all; minimum 3 namespaces)

**DELTA CANDIDATES:**
- Expected [X] but [artifact] showed [Y]
- (all candidates)

**OPEN QUESTIONS:**
- [Question] — If [X], verb shifts to [A]; if [Y], verb shifts to [B]
- (all questions)

---

## PART 2 — Devil's Advocate

Role: Make the strongest available case for status quo / do nothing / no change. Argue
against departure from current state. Use only signals in evidence — do not fabricate.
Find the best version of the "don't proceed" argument.

**Status quo argument:** [3-5 sentences. Which signals support this reading? What does
the evidence look like if you weight the cautionary signals most heavily?]

**Signals that support inertia:** [List specifically — which signals, which findings,
which gaps favor holding current state]

**The risk inertia protects against:** [Name it. What failure mode does not acting avoid?]

**Inertia weight:** [Light / Moderate / Heavy — and why, based on Part 2 argument]

---

## PART 3 — Pattern Builder

Role: Receive Parts 1-2. Build the pattern that accounts for both the evidence and the
counter-argument. The pattern must be responsive to Part 2.

**The pattern:** [One complete, self-contained sentence. What do two or more signals show
together that no single signal shows alone? The pattern must address the inertia argument
— either explaining why it is outweighed, or naming the tension that makes this a
pause/pivot rather than a proceed.]

**The delta:** Expected [X] but found [Y]. [Primary surprise. Self-contained.]

**Verb:** [proceed / pause / pivot / abandon] — Because [pattern], despite [inertia weight
from Part 2].

---

NON-SUBSTITUTION RULE: The pattern block above does not satisfy Beat 3 placement. The
verb block above does not satisfy the bridge sentence required in the Recommendation beat.
Both are independently required. Prior-stage presence is not credit.

---

## PART 4 — Narrator

Role: Write the five-beat story. The counter-argument from Part 2 must be legible in the
story — not buried. The recommendation must be proportionate to both evidence and inertia
weight. Parts 1-3 are not credit for any beat.

Open with the recommendation verdict: one sentence naming the verb and its basis before
any other content.

---

### What we set out to understand
[Question or decision driving signal gathering. 1-2 sentences.]

### What the signals revealed
[Key finding per signal. >= 3 namespaces visible. State the primary delta using
contrastive language. Note where signals surprised the status-quo expectation.]

### What the signals say together
[State the pattern independently — Part 3 block is not credit. Write: "The pattern:
[full sentence]." Address the inertia argument from Part 2: is it outweighed? Does it
produce a tension? 2-4 sentences.]

### What remains uncertain
[Draw from Part 1 open questions. For each: state specifically, then state decision cost:
"If [X], this moves from [verb] to [verb]." Include at least one question where the
inertia position from Part 2 could be vindicated.]

### The recommendation
[State evidence posture from Part 1. Note inertia weight from Part 3. Write the bridge:
"Because [pattern], and despite [inertia weight], the recommendation is [verb]." Bridge
is independently required here — Part 3 verb block is not credit. Name the decision-maker
role or constraint.]

---

Consistency verification:

| Claim            | Part 1     | Part 3     | Beat 3      | Rec. beat         |
|------------------|------------|------------|-------------|-------------------|
| Evidence posture | stated     | —          | —           | must match Part 1 |
| Inertia weight   | —          | stated     | visible     | must match Part 3 |
| Pattern stmt     | —          | stated     | must match  | referenced        |
| Rec. verb        | —          | stated     | —           | must match Part 3 |

Inconsistency in any "must match" cell is a structural error — revise before output.
```

---

## V-05 — Variation Axes: Output Format + Lifecycle Emphasis + Structural Multi-Stage Consistency

**Hypothesis:** A fully templated output where critical claims are forced to appear at multiple named structural positions — with a final consistency table that makes any mismatch between positions an auditable ✗ — makes C-19 and C-20 verifiable from structure alone without instructional reminders. Combining table-format pre-composition (C-18), explicit lifecycle gates, and a Block C reconciliation table creates the strongest structural enforcement available across all aspirational criteria.

---

```
You are producing a topic-story for: {{topic}}

Available signals (read all before proceeding):
{{signals}}

---

# TOPIC-STORY — STRUCTURED PRODUCTION TEMPLATE

Critical claims must appear at multiple named positions. Inconsistency between positions
is a structural error detectable from this document alone — no external review required.
Complete all blocks in order.

---

# BLOCK A — PRE-COMPOSITION ARTIFACTS

These blocks must be completed before narrative writing begins. They do not satisfy
narrative placement requirements — each artifact must appear independently at its named
narrative position.

---

## A1 — Signal Inventory

| # | Signal / Artifact | Namespace | Key Finding (one sentence) | Disposition         |
|---|-------------------|-----------|---------------------------|---------------------|
| 1 |                   |           |                           | confirms/surprises  |
| 2 |                   |           |                           |                     |
| 3 |                   |           |                           |                     |
| (add rows as needed) | | | |                     |

Coverage check — distinct namespaces represented: _____, _____, _____, ... (minimum 3)

---

## A2 — Delta Table

| # | Expected          | Found     | Source Signal | Decision Relevance |
|---|-------------------|-----------|--------------|-------------------|
| 1 |                   |           |              | high/medium/low   |
| (add rows) | | | |                   |

Primary delta (mark one): Expected _____ but found _____

---

## A3 — Pattern Statement

**The pattern:** [One complete, self-contained sentence. What two or more signals show
together that no single signal shows alone. Names a relationship, tension, or gap. Not
derivable from any single artifact. Must read without surrounding text.]

A3 placement rule: This pattern must appear independently in Beat 3 AND in the bridge
sentence of the Recommendation beat. This block does not satisfy either placement.

---

## A4 — Evidence Posture Declaration

**Posture:** [strong positive / mixed / conflicting / weak]
**Basis:** [Name the signals that determine this posture]

A4 placement rule: This posture must appear independently in the Recommendation beat.
This block does not satisfy that placement.

---

## A5 — Recommendation Verb

**Verb:** [proceed / pause / pivot / abandon]
**Basis:** Because [pattern from A3], with posture [from A4].

A5 placement rule: This verb must appear independently in the bridge sentence of the
Recommendation beat. This block does not satisfy that placement.

---

## A6 — Uncertainty Register

| # | Open Question | Resolution Path | If YES: verb shifts to | If NO: verb shifts to |
|---|--------------|----------------|----------------------|-----------------------|
| 1 |              |                |                      |                       |
| (add rows) | | | |                       |

Minimum 1 row. Generic "more research needed" entries fail this block.

---

## PRE-COMPOSITION CHECKPOINT

Before writing Block B, verify:
[ ] A1: >= 3 namespaces represented
[ ] A2: Primary delta identified and starred
[ ] A3: Pattern is self-contained, cross-signal, and names a relationship/tension/gap
[ ] A4: Posture declared with named basis
[ ] A5: Verb derived from A3 + A4, explicitly stated
[ ] A6: Each uncertainty row has a decision-cost annotation in both directions

Only proceed to Block B when all checkboxes pass.

---

# BLOCK B — NARRATIVE

Write the five beats. Pre-composition blocks do not satisfy narrative placements. Each
beat independently requires its stated content — prior-stage presence is not credit.

Opening sentence (first content in the story): State the recommendation verb and its
basis. One sentence. No hedging, no context-setting before this.

---

### Beat 1 — What we set out to understand
[The question or decision driving signal gathering. 1-2 sentences. No findings yet.]

---

### Beat 2 — What the signals revealed
[Draw from A1. One key finding per signal referenced. Show >= 3 distinct namespaces. State
the primary delta from A2 using "expected X but found Y" language. Name specific artifacts
where possible.]

---

### Beat 3 — What the signals say together

Pattern (independently required here — A3 is not credit):
The pattern: [Restate the full A3 sentence. Must be independently stated here, not
referenced to A3. Complete sentence, self-contained.]

[Expand: 2-3 sentences naming the relationship, tension, or gap. A reader who has not
seen Block A must understand the pattern from this beat alone.]

---

### Beat 4 — What remains uncertain
[Draw from A6. For each row: state the open question specifically, then write:
"If [X], this moves from [current verb] to [other verb]." No generic hedges permitted.
Each item must carry its decision-cost annotation.]

---

### Beat 5 — The recommendation

Posture (independently required here — A4 is not credit):
Evidence posture: [Restate posture word] — [Restate the signals driving this, in terms
visible in the narrative, not just A4]

Bridge sentence (independently required here — A5 is not credit):
Because [the cross-signal pattern, named explicitly], the recommendation is [verb].

Decision context:
[Name or address the decision-maker role. Who is deciding, under what constraint.]

---

# BLOCK C — CONSISTENCY VERIFICATION TABLE

Complete after writing Block B. Fill every cell. This table makes cross-stage
inconsistency structurally visible — any mismatch is a structural error requiring revision.

| Claim              | A-block value                       | Beat 3 / Beat 5 value                | Match? |
|--------------------|-------------------------------------|--------------------------------------|--------|
| Evidence posture   | [posture word from A4]              | [posture word from Beat 5]           | [ ] / [X] |
| Pattern (first 10 words) | [first 10 words of A3]        | [first 10 words of Beat 3 pattern]   | [ ] / [X] |
| Recommendation verb | [verb from A5]                     | [verb from Beat 5 bridge sentence]   | [ ] / [X] |
| Primary delta      | [Expected/Found from A2 starred row] | [delta statement from Beat 2]       | [ ] / [X] |

If any row shows X (mismatch): revise the narrative beat to match the pre-composition
artifact. Do not revise the pre-composition artifact to match the narrative. Output only
when all rows show checkmark.
```

---

## Summary Table

| Variation | Primary Axis | Secondary Axis | Key Rubric Targets |
|-----------|-------------|----------------|-------------------|
| V-01 | Role sequence (3-role pipeline) | — | C-10, C-15, C-18, C-19, C-20 |
| V-02 | Output format (table-first) | — | C-18, C-19, C-20 |
| V-03 | Lifecycle emphasis (4 gates) | — | C-10, C-15, C-18 |
| V-04 | Role sequence + inertia framing | — | C-07, C-09, C-19, C-20 |
| V-05 | Output format + lifecycle + multi-stage consistency | — | C-18, C-19, C-20, C-10, C-15 |
