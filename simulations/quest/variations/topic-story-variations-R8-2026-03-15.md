# Quest Variate — `topic-story` Round 8

---

## V-01 — Role Sequence axis

**Variation**: ANALYST role runs first and produces pre-composition artifacts; AUTHOR role runs second and writes narrative beats. Roles are explicitly separated by a named boundary.

**Hypothesis**: Separating ANALYST and AUTHOR into sequential execution roles — with an explicit non-substitution rule at the boundary — will enforce pre-composition discipline (C-10, C-15, C-18) more reliably than structural labels alone, because the role boundary makes it structurally impossible to produce narrative before analytic outputs are complete.

---

```
You are producing a `topic-story` signal artifact for Signal — the editorial
synthesis of all available signals for a named topic.

## Inputs
- Topic: {{topic}}
- Available signal artifacts: {{signal_list}}
- Prior recommendation or resolved verdict (if any): {{prior_verdict}}

---

## ROLE 1 — ANALYST

You are operating as ANALYST. Complete all three blocks below before writing
any narrative prose. Do not begin ROLE 2 until all blocks are finished.

### BLOCK A — Falsifiable Hypothesis (S0)
State the hypothesis as it stood before the signals were read.
Required form: "We believed: [specific falsifiable claim]."
A vague intent ("we set out to understand X") fails — the claim must be
specific enough that signals can confirm, refute, or modify it.

BLOCK A:
We believed: ___

### BLOCK B — Pre-Composition Pattern
State the cross-signal pattern as a discrete, labeled, self-contained claim.
Required form: "The pattern: [claim]."
The claim must name what two or more signals show together that no single
signal shows alone — a relationship, tension, or gap, not a list of findings.
Do not use forward references ("as shown below") or backward references
("the above signals"). A reader must understand the full pattern from this
block alone, without reading any surrounding text.

BLOCK B:
The pattern: ___

### BLOCK C — Delta (S0→S3)
State the contrastive finding as a discrete claim.
Required form: "We expected [X] but found [Y] — this [strengthens /
undermines / modifies] the hypothesis by [specific direction or degree]."
The delta must show substantive mutation. If the evolved hypothesis is
essentially the same as S0 — if S0 = S3 — the output fails.
Do not write a delta that could have been written before reading the signals.

BLOCK C:
We expected ___ but found ___ — this ___ the hypothesis by ___

---

NON-SUBSTITUTION RULE: The sentences produced in Blocks A, B, and C do not
satisfy the requirements for ROLE 2 placements. Each required placement in
ROLE 2 must be independently satisfied. Prior-role production is not credit —
the bridge sentence required in Beat 5 is not satisfied by the Block B sentence,
and the delta required in Beat 2 or Beat 3 is not satisfied by the Block C sentence.

---

## ROLE 2 — AUTHOR

You are now operating as AUTHOR. Write the five labeled beats below.
Use the ANALYST blocks as anchors — your narrative must be consistent with them
but must re-state critical claims independently in the positions required.

The first paragraph of the output (or the first named section) must state the
recommendation verdict. Do not build to a conclusion. A story that reaches the
recommendation only at the end fails.

---

**BOTTOM LINE**: [proceed / pause / pivot / abandon] — [one sentence stating why,
naming the pattern by reference]

---

### Beat 1 — What We Set Out to Understand
State the hypothesis in narrative voice. It must appear as a falsifiable claim —
the specific proposition the signals were gathered to test. Re-state it
independently of Block A; do not simply copy Block A verbatim.

### Beat 2 — What the Signals Revealed
For each signal namespace or artifact type consulted, name one key finding.
Minimum three distinct namespaces or artifact types. This beat shows the
evidence base — enough to make the synthesis credible. Do not enumerate
exhaustively. Include at least one explicit delta statement: "We expected [X]
but found [Y]." Re-state this independently of Block C.

### Beat 3 — What the Signals Say Together
State the cross-signal pattern in narrative voice. The pattern must appear as
a discrete labeled claim within this beat — a sentence or block that begins
"The pattern:" or equivalent, standing independently of the surrounding prose.
Reference at least two signals showing something together that neither shows
alone. Name a relationship, tension, or gap — not a collection of findings.
Re-state the pattern independently of Block B.

### Beat 4 — What Remains Uncertain
Name at least one specific open question. For each uncertainty item, state:
"If [X] resolves to [Y], this recommendation moves from [verb] to [verb]."
A named direction is required — generic hedges ("more research may be needed")
without a stated direction fail.

### Beat 5 — The Recommendation
This beat must contain, independently and in this order:
1. **Evidence posture statement**: Name the overall signal posture
   (strong positive / mixed / conflicting / weak / negative).
2. **Recommendation verb**: State proceed / pause / pivot / abandon.
3. **Bridge sentence**: Name the cross-signal pattern by reference and identify
   it as the stated reason for the verb. Required form: "Because [the named
   pattern], the recommendation is [verb]." The bridge must appear in this beat —
   not be imported from Beat 3 or Block B.
4. **Decision context**: Name or clearly address who is making this decision
   and under what constraint. A recommendation stated as a finding
   ("the signals suggest X") rather than a decision ("a team deciding Y
   should Z") fails.

PRIOR-VERDICT OVERRIDE: If {{prior_verdict}} is non-empty and this recommendation
contradicts it, name the prior verdict explicitly and state the reason for
the departure. Silent contradiction is a correctness error.

EVIDENCE-VERB CONSISTENCY CHECK: The posture named in (1) must be consistent
with the verb in (2) and with the signals described in Beats 2–3.
Strong positive → proceed; mixed → pause; conflicting → pivot;
weak or negative → abandon.

---

## Pre-Output Verification

Before finalizing, confirm:
- [ ] Block A contains a falsifiable claim (not a vague intent statement)
- [ ] Block B is self-contained; no forward or backward references
- [ ] Block C shows substantive S0→S3 mutation; S0 ≠ S3
- [ ] BOTTOM LINE appears before Beat 1
- [ ] Beat 2 references at least three distinct signal sources
- [ ] Beat 3 contains a discrete labeled pattern claim
- [ ] Beat 4 states a named directional consequence for each uncertainty
- [ ] Beat 5 contains posture, verb, bridge, and decision context — each
      stated independently of their Block/Beat 3 counterparts
- [ ] If prior verdict exists and is contradicted, override is named
```

---

## V-02 — Output Format axis

**Variation**: A signal posture table is produced as the mandatory opening structure. All critical claims (posture, pattern, verb) are entered into the table before narrative beats begin. The table must remain consistent with the narrative — divergence is structurally visible.

**Hypothesis**: A mandatory signal posture table preceding all narrative production will make multi-stage consistency (C-20) self-revealing — any claim shift between the table and the recommendation beat becomes a visible contradiction rather than an inference failure, because both entries are readable side-by-side without manual cross-referencing.

---

```
You are producing a `topic-story` signal artifact for Signal — the editorial
synthesis of all available signals for a named topic.

## Inputs
- Topic: {{topic}}
- Available signal artifacts: {{signal_list}}
- Prior recommendation or resolved verdict (if any): {{prior_verdict}}

---

## Step 1 — Signal Posture Table (complete before writing any beats)

Before writing any narrative, fill out the following table. Every cell is
required. This table is a pre-composition commitment — the narrative beats
must be consistent with it. If a cell value changes during writing, correct
the table first, then revise the narrative.

| Field | Value |
|-------|-------|
| **Topic** | {{topic}} |
| **S0 Hypothesis** | We believed: ___ |
| **Signal posture** | [strong positive / mixed / conflicting / weak / negative] |
| **Namespaces consulted** | [list, minimum 3] |
| **Cross-signal pattern** | The pattern: ___ |
| **S0→S3 delta** | We expected ___ but found ___ |
| **Recommendation verb** | [proceed / pause / pivot / abandon] |
| **Primary uncertainty** | [specific open question] |
| **If uncertainty resolves to [Y]** | recommendation moves to [verb] |
| **Decision context** | [who is deciding, under what constraint] |
| **Prior verdict (if any)** | {{prior_verdict}} |
| **Override reason (if contradicting)** | [named reason, or N/A] |

CONSISTENCY RULE: Each value in this table is a commitment. The narrative beats
below must independently re-state each critical claim (pattern, posture, verb,
delta) in the required positions — the table values are anchors, not substitutes
for placement in narrative.

---

## Step 2 — Narrative Beats

The first output after the table must be the bottom line. Do not build to a
conclusion — the recommendation appears first.

---

**BOTTOM LINE**: [verb from table] — [one sentence, naming the pattern]

---

### Beat 1 — What We Set Out to Understand
State the S0 hypothesis from the table in narrative voice, as a falsifiable
claim. Name what specific proposition the signals were gathered to test —
not a vague intent.

### Beat 2 — What the Signals Revealed
For each namespace listed in the table, name one key finding. Do not summarize
exhaustively — one signal finding per source. Include at least one contrastive
statement ("we expected X but found Y") drawn from the delta in the table.

### Beat 3 — What the Signals Say Together
State the cross-signal pattern as a discrete, labeled claim. It must appear
as a named sentence or block: "The pattern: ___." The claim names what two
or more signals show together that no single signal shows alone — a
relationship, tension, or gap. Do not restate findings side by side.

### Beat 4 — What Remains Uncertain
State the primary uncertainty from the table. For each uncertainty item:
"If [X] resolves to [Y], this recommendation moves from [verb from table]
to [alternate verb]." At least one named directional consequence is required.

### Beat 5 — The Recommendation
This beat must independently re-state, in order:
1. The signal posture from the table (e.g., "The overall signal posture
   is mixed")
2. The recommendation verb from the table
3. An explicit bridge sentence: "Because [the named pattern], the
   recommendation is [verb]" — this sentence must appear here and must
   not be satisfied by the Beat 3 pattern block
4. The decision context from the table — who is making this decision
   and under what constraint

TABLE-BEAT CONSISTENCY CHECK: If the posture in (1), the verb in (2), or
the bridge in (3) differs from the table values in Step 1, the output fails.
Both locations are readable — divergence is visible.

PRIOR-VERDICT OVERRIDE: If {{prior_verdict}} is non-empty and this recommendation
contradicts it, the override reason from the table must appear here explicitly.
Absence of an override reason when a contradiction exists is a correctness error.

---

## Step 3 — Self-Certification

After completing the beats, append:

**Signal Posture Self-Certification**: The overall signal posture for {{topic}}
is [posture]. This posture directly produces the recommendation verb [verb].
The cross-signal pattern that drives this determination is: "[pattern]".
These values are consistent with the table in Step 1 and the narrative in
Beat 5.
```

---

## V-03 — Lifecycle Emphasis axis

**Variation**: The output is divided into two explicitly labeled parts with a named completion gate between them. Part 1 is Pre-Composition Analysis; Part 2 is Narrative Production. The gate is structural — a visual separator with a named checklist that must pass before Part 2 begins.

**Hypothesis**: A hard structural separator with a named completion gate between pre-composition and narrative phases will satisfy C-18 (structural pre-composition gate) by making pre-composition verifiable from structure alone — the gate cannot be passed without producing the required artifacts, independent of any instructional language.

---

```
You are producing a `topic-story` signal artifact for Signal — the editorial
synthesis of all available signals for a named topic.

## Inputs
- Topic: {{topic}}
- Available signal artifacts: {{signal_list}}
- Prior recommendation or resolved verdict (if any): {{prior_verdict}}

---

# PART 1 — PRE-COMPOSITION ANALYSIS

Do not write any narrative prose in Part 1. This part produces three analytic
artifacts. Part 2 cannot begin until all three are complete and the gate check
below passes.

---

## 1.1 — Falsifiable Hypothesis (S0)

State the hypothesis as it stood before signals were gathered.
Form: "We believed: [specific falsifiable claim]."
The claim must be falsifiable — specific enough that the signals collected
could confirm, refute, or modify it. Vague intent statements fail:
"We set out to understand X" is not a hypothesis; "We believed X holds" is.

**S0**: We believed: ___

---

## 1.2 — Cross-Signal Pattern Block

Identify the pattern that emerges from reading the signals together.
Form: "The pattern: [discrete, self-contained claim]."

Requirements:
- Self-contained: the full claim is intelligible without any surrounding text
- Cross-signal: names what two or more signals show together that no single
  signal shows alone
- Synthetic: names a relationship, tension, or gap — not a list of findings
- No forward or backward references to other sections

**Pattern Block**:
The pattern: ___

---

## 1.3 — Delta Statement (S0→S3)

State the substantive change between S0 and the evolved hypothesis after
reading the signals.
Form: "We expected [X] but found [Y] — this [strengthens / undermines /
modifies] the hypothesis by [specific direction]."

Requirements:
- Shows mutation: the evolved view must differ from S0 in a way that affects
  direction or confidence
- S0 = S3 is a pattern failure — a delta that amounts to "confirmed what
  we believed" without naming a confidence shift fails
- Cannot be written before reading the signals — if the statement could have
  been produced from S0 alone, it fails

**Delta**: We expected ___ but found ___ — this ___ the hypothesis by ___

---

## PART 1 → PART 2 GATE

Before continuing, verify all four conditions. Do not proceed to Part 2
until all pass.

- [ ] 1.1: S0 is a falsifiable claim, not a vague intent
- [ ] 1.2: Pattern Block is self-contained and names a cross-signal relationship
- [ ] 1.3: Delta shows substantive mutation; S0 ≠ S3
- [ ] 1.3: Delta could not have been written before reading the signals

If any condition fails, revise the artifact before proceeding.

---

═══════════════════════════════════════════════════════════════
PART 1 COMPLETE — BEGINNING PART 2
═══════════════════════════════════════════════════════════════

---

# PART 2 — NARRATIVE PRODUCTION

NON-SUBSTITUTION RULE: The artifacts in Part 1 are analytic anchors. Each
critical claim (pattern, delta, posture, verb) must be independently stated
in the required narrative positions below. Presence in Part 1 is not credit
for placement in Part 2. The bridge sentence required in Beat 5 is not
satisfied by the Pattern Block. The delta required in Beat 2 is not satisfied
by the Delta Statement.

---

**BOTTOM LINE** [required first]: [proceed / pause / pivot / abandon] — [one
sentence, naming the pattern by reference, stating why this verdict follows]

The above line must appear before Beat 1. A story that builds to its
recommendation fails.

---

### Beat 1 — What We Set Out to Understand

State the falsifiable hypothesis in narrative voice. It must be a specific
claim that the signals could test — not a framing statement or question.
Re-state it independently of Section 1.1; do not copy verbatim.

### Beat 2 — What the Signals Revealed

For each of the signal sources consulted (minimum three distinct namespaces
or artifact types), name one key finding. Name the source and the finding;
do not summarize exhaustively. Include a contrastive statement here — at
least one explicit "we expected X but found Y" — re-stated independently
of Section 1.3.

### Beat 3 — What the Signals Say Together

State the cross-signal pattern. It must appear as a discrete labeled claim:
a sentence beginning "The pattern:" or an equivalent named block. Reference
at least two signals showing something together that neither shows alone.
Name a relationship, tension, or gap. Re-state independently of Section 1.2.

### Beat 4 — What Remains Uncertain

Name at least one specific open question that remains after the signals are
synthesized. For each uncertainty item, provide a decision-cost annotation:
"If [X] resolves to [Y], this recommendation moves from [current verb] to
[alternate verb]." The direction of change is required — "more research may
be needed" without a named consequence fails.

### Beat 5 — The Recommendation

This beat must contain each of the following, in order, stated independently
of their Part 1 counterparts:

**(a) Signal posture**: "The overall signal posture is [strong positive /
mixed / conflicting / weak / negative]."

**(b) Recommendation verb**: "The recommendation is [proceed / pause / pivot /
abandon]."

**(c) Bridge sentence**: "Because [the named cross-signal pattern], the
recommendation is [verb]." This sentence must appear here — it is not
satisfied by the Beat 3 pattern block or the Part 1 Pattern Block.

**(d) Decision context**: Name who is making this decision and under what
constraint. A finding statement ("the signals suggest X") rather than a
decision statement ("a team deciding whether to Y should Z") fails.

**(e) Evidence-verb consistency**: The posture in (a) must be consistent
with the verb in (b). Strong positive → proceed; mixed → pause;
conflicting → pivot; weak or negative → abandon.

PRIOR-VERDICT OVERRIDE: If {{prior_verdict}} is non-empty and (b) contradicts
it, include an explicit override sentence: "The prior verdict [prior_verdict]
is superseded because [reason]." Silent contradiction fails.
```

---

## V-04 — Inertia Framing axis

**Variation**: The falsifiable hypothesis (S0) is the dominant organizational anchor of the entire story. Every beat is framed relative to S0. The delta is computed as a named arithmetic step — explicitly measuring the distance between S0 and S3 — rather than described as a narrative observation.

**Hypothesis**: Anchoring the story structure to a falsifiable S0 hypothesis and computing the S0→S3 delta as a named measurement step will most directly address C-21/C-22 by making the delta a computed output with a visible reference point, rather than a composed narrative that could have been written before signals were read.

---

```
You are producing a `topic-story` signal artifact for Signal — the editorial
synthesis of all available signals for a named topic.

## Inputs
- Topic: {{topic}}
- Available signal artifacts: {{signal_list}}
- Prior recommendation or resolved verdict (if any): {{prior_verdict}}

---

## Orientation: Hypothesis-Anchored Synthesis

This story is organized around a falsifiable hypothesis (S0) — a specific
claim that was held before signals were gathered. Every beat is measured
against S0. The purpose of the synthesis is not to report what the signals
said but to show how the signals changed, confirmed, or undermined the
hypothesis, and what that movement means for the decision.

The recommendation is the destination. State it first.

---

## BOTTOM LINE (required first)

**Recommendation**: [proceed / pause / pivot / abandon]
**Why**: [one sentence, naming the S0→S3 movement and what it implies]

This must appear before any beats. A story that arrives at the recommendation
only at the end fails.

---

## Beat 1 — The Hypothesis We Held (S0)

State the inertia baseline: what was believed before signals were gathered.
This is not a research question or a curiosity — it is a specific falsifiable
claim that could be proven wrong.

Required form: "Before gathering signals, we held: [claim]. This prediction
implied [what decision or direction it would have supported]."

The S0 statement creates the reference point for the entire story. Without a
specific falsifiable claim here, the S0→S3 delta has no measurement basis
and collapses into description.

---

## Beat 2 — What the Signals Revealed

For each signal source consulted (minimum three distinct namespaces or artifact
types), state:
- Source (namespace or artifact type)
- Key finding (one sentence)
- Bearing on S0: "This [supports / challenges / modifies / is orthogonal to]
  the S0 hypothesis by [specific detail]"

Do not summarize exhaustively. Cover enough sources to establish the evidence
base. The S0 bearing is required for each source — signals that have no stated
relationship to the hypothesis do not count toward the minimum.

---

## Beat 3 — The S0→S3 Delta (Measured, Not Described)

This beat has two required sub-parts.

### 3a — Cross-Signal Pattern

State the pattern as a discrete, self-contained, labeled claim:
"The pattern: [claim]."

The claim must name what two or more signals show together that no single
signal shows alone — a relationship, tension, or gap. It must be self-contained:
a reader understands the full pattern from this block alone. No forward or
backward references.

### 3b — Hypothesis Evolution (S3)

Compute the delta explicitly.

"S0: We believed [claim from Beat 1].
S3: After signals, the hypothesis has [strengthened / weakened / mutated] to:
[revised or confirmed claim].
Delta: We expected [X] but found [Y]. The signals [increased / decreased /
reversed] confidence in S0 by [characterization] because [specific reason]."

The delta must show substantive mutation. S0 = S3 is a pattern failure —
if confidence changed at all, name how and why. A delta that could have been
written before reading the signals fails. The contrastive statement ("we
expected X but found Y") must be present and must name the specific direction
of change.

ANTI-STAGNATION CHECK: The evolved hypothesis (S3) must differ from S0 in
a way that affects the recommendation's direction or confidence level. A
delta that amounts to "the signals generally confirmed our hypothesis" without
naming a specific confidence shift fails.

---

## Beat 4 — What Remains Uncertain

State what the signals did not resolve. For each uncertainty:

"Open question: [specific question].
Decision cost: If this resolves to [Y], the recommendation moves from
[current verb] to [alternate verb]."

At least one uncertainty with a named directional consequence is required.
Generic hedges ("further investigation may be warranted") without a named
consequence fail. Each uncertainty must be framed as a gap relative to the
S0→S3 trajectory — what would move the delta further, reverse it, or
redirect the hypothesis.

---

## Beat 5 — The Recommendation

Four required components, each independent of their prior-beat counterparts:

**(a) Signal posture statement** (required in this beat):
"The overall signal posture for {{topic}} is [strong positive / mixed /
conflicting / weak / negative]."

**(b) Recommendation verb** (required in this beat):
"The recommendation is [proceed / pause / pivot / abandon]."

**(c) Bridge sentence** (required in this beat):
"Because [the cross-signal pattern from Beat 3a], the recommendation is [verb]."
This sentence must appear here. It is not satisfied by the Beat 3a pattern
block — non-substitution applies.

**(d) Decision framing**:
Name who is making this decision and under what constraint. A finding statement
is not a recommendation. "A [role] deciding whether to [action] should [verb]
because [reason]" is the required form.

EVIDENCE-VERB CONSISTENCY: The posture in (a) must be consistent with the
verb in (b). Strong positive → proceed; mixed → pause; conflicting → pivot;
weak or negative → abandon.

S0-VERB CONSISTENCY: The recommendation verb must be traceable to the
S0→S3 delta. If S0 was strongly confirmed → proceed; if S0 was undermined →
pivot or abandon; if S0 was partially confirmed with gaps → pause.

PRIOR-VERDICT OVERRIDE: If {{prior_verdict}} is non-empty and (b) contradicts
it, state: "The prior verdict of [prior_verdict] is superseded. The reason
for this departure is [specific reason]." Silent contradiction fails.
```

---

## V-05 — Combination (Role Sequence + Structural Gate + Inertia Framing)

**Variation**: Combines three axes — ANALYST/AUTHOR role separation (V-01), a Part 1/Part 2 structural gate (V-03), and S0-anchored inertia framing (V-04). The gate between parts is the role transition. The S0 hypothesis anchors both the analytic phase and the narrative phase.

**Hypothesis**: Combining analyst/author role separation, a structural Part 1/Part 2 gate, and S0-anchored inertia framing will achieve the highest composite score by addressing R7 excellence patterns C-21, C-22, and C-23 simultaneously — the role boundary enforces pre-composition, the gate makes it structurally verifiable, and the S0 anchor gives the delta a reference point with measurement force.

---

```
You are producing a `topic-story` signal artifact for Signal — the editorial
synthesis of all available signals for a named topic.

## Inputs
- Topic: {{topic}}
- Available signal artifacts: {{signal_list}}
- Prior recommendation or resolved verdict (if any): {{prior_verdict}}

---

# PART 1 — ANALYST ROLE (Pre-Composition)

You are ANALYST. Produce three named artifacts. Do not write narrative prose.
Part 2 does not begin until the Part 1 Gate passes.

---

## Artifact 1 — Falsifiable S0 Hypothesis

State what was believed before signals were gathered, as a specific falsifiable
claim. This is the inertia baseline: the prediction the signals are measured
against. Without a falsifiable S0, the S0→S3 delta has no reference point and
collapses into description.

Required form: "We believed: [specific falsifiable claim]."
Failure mode: "We set out to understand X" is not a hypothesis.

**S0**: We believed: ___

---

## Artifact 2 — Cross-Signal Pattern Block

Identify the pattern that the signals together reveal. State it as a discrete,
self-contained, labeled claim.

Required form: "The pattern: [claim]."
Requirements:
- Self-contained: complete without reading any surrounding text
- Cross-signal: names what two or more signals show together that neither
  shows alone
- Synthetic: a relationship, tension, or gap — not a collection of findings
- No forward references ("as shown below") or backward references
  ("the above signals")

**Pattern Block**: The pattern: ___

---

## Artifact 3 — S0→S3 Delta

Compute the movement between the S0 hypothesis and the evolved stance after
signals. This is a measurement, not a description.

Required form:
"S0: [claim from Artifact 1]
S3: [evolved claim — what the signals moved the hypothesis to]
Delta: We expected [X] but found [Y] — this [strengthens / undermines /
modifies] the hypothesis. Confidence [increased / decreased / reversed]
because [specific reason]."

Anti-stagnation check: S0 = S3 is a pattern failure. If confidence changed,
name the direction. The delta must not be writable before reading the signals.

**Delta**:
S0: ___
S3: ___
Delta: We expected ___ but found ___ — this ___ confidence because ___

---

## PART 1 → PART 2 GATE

Verify all conditions before proceeding. Do not cross the gate until all pass.

- [ ] Artifact 1: Contains a falsifiable claim (not a vague intent)
- [ ] Artifact 2: Is self-contained; references no surrounding text
- [ ] Artifact 2: Names a cross-signal relationship (not a summary list)
- [ ] Artifact 3: S3 differs from S0 in direction or confidence
- [ ] Artifact 3: Delta could not have been written before reading signals

**Gate status**: [PASS / FAIL — revise before continuing]

---

════════════════════════════════════════════════════════════════
ANALYST COMPLETE — TRANSITIONING TO AUTHOR
════════════════════════════════════════════════════════════════

NON-SUBSTITUTION RULE: Artifacts 1, 2, and 3 are analytic anchors. Each
critical claim must be independently re-stated in the required narrative
positions in Part 2. Artifact presence is not credit for narrative placement.
Specifically:
- The bridge sentence required in Beat 5 is not satisfied by Artifact 2
- The delta statement required in Beat 2 is not satisfied by Artifact 3
- The hypothesis statement required in Beat 1 is not satisfied by Artifact 1
Each placement must be independently satisfied.

---

# PART 2 — AUTHOR ROLE (Narrative Production)

You are AUTHOR. Write the five labeled beats. Anchor the narrative to the
Part 1 artifacts but re-state each critical claim independently.

The first thing the reader sees after the gate must be the recommendation.
A story that builds to its conclusion fails.

---

**BOTTOM LINE**: [proceed / pause / pivot / abandon] — [one sentence naming
the cross-signal pattern and the S0→S3 movement that produced this verdict]

---

### Beat 1 — What We Set Out to Understand

State the S0 hypothesis in narrative voice. It must be a falsifiable claim —
a specific proposition that the signals could test. Name what decision or
direction it implied if true. Re-state independently of Artifact 1.

### Beat 2 — What the Signals Revealed

For each signal source consulted (minimum three distinct namespaces or artifact
types), state the source and one key finding. For at least one source, state
how the finding bore on the S0 hypothesis. Include a contrastive statement
("we expected X but found Y") re-stated independently of Artifact 3.

### Beat 3 — What the Signals Say Together

State the cross-signal pattern as a discrete labeled claim in this beat:
"The pattern: [claim]." Self-contained, cross-signal, synthetic — same
requirements as Artifact 2, but this is an independent statement, not a copy.
A relationship, tension, or gap. Not a list of findings side by side.

### Beat 4 — What Remains Uncertain

Name at least one specific open question. For each:
"If [X] resolves to [Y], this recommendation moves from [current verb] to
[alternate verb]." Named directional consequence required. Frame each
uncertainty relative to the S0→S3 trajectory — what would it take to
shift the delta further, reverse it, or redirect the hypothesis?

### Beat 5 — The Recommendation

Five required components, each independently stated:

**(a) Signal posture** (in this beat): "The overall signal posture for
{{topic}} is [strong positive / mixed / conflicting / weak / negative]."

**(b) Recommendation verb** (in this beat): "The recommendation is
[proceed / pause / pivot / abandon]."

**(c) Explicit bridge** (in this beat): "Because [the named cross-signal
pattern], the recommendation is [verb]." This sentence must appear here
and must not be satisfied by the Beat 3 pattern block or Artifact 2.

**(d) S0→S3 traceability**: State how the delta produced this verb.
"The S0 hypothesis was [strengthened / undermined / modified]. This
[confirms / reverses / narrows] the direction, producing [verb]."

**(e) Decision framing**: Name who is making this decision and under what
constraint. "A [role] deciding whether to [action] should [verb] because
[reason drawn from the pattern]."

EVIDENCE-VERB CONSISTENCY: Posture in (a) must match verb in (b).
Strong positive → proceed; mixed → pause; conflicting → pivot;
weak or negative → abandon.

PRIOR-VERDICT OVERRIDE: If {{prior_verdict}} is non-empty and (b)
contradicts it, state the override explicitly: "The prior verdict of
[prior_verdict] is superseded. This departure is warranted because
[specific reason]." Silent contradiction is a correctness error.

---

## Part 2 Completion Check

Before finalizing output:
- [ ] BOTTOM LINE appears before Beat 1
- [ ] Beat 1 contains an independently stated falsifiable hypothesis
- [ ] Beat 2 references ≥3 signal sources with a re-stated delta
- [ ] Beat 3 contains a discrete independent labeled pattern claim
- [ ] Beat 4 states a named directional consequence per uncertainty
- [ ] Beat 5(a)–(e) each independently satisfied
- [ ] If prior verdict contradicted, override is named
- [ ] No Part 1 artifact is relied upon as a substitute for its Part 2 placement
```
