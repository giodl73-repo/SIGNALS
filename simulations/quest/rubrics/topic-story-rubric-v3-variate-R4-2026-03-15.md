# R4 Variations — `topic-story` (v3 Rubric, 11 Criteria)

**Round**: 4
**Skill**: `topic-story`
**Base rubric**: `topic-story-rubric-v3-2026-03-15.md`
**Criteria**: C-01 through C-11 · Max 110 pts

---

## R3 State Summary

R3 produced the first concrete single-prompt 110 (V-01: inertia chain + gap closure with
`{namespace}/{skill} — {expected finding type}` format). V-04 (table + inertia + gap closure)
and V-05 (EVALUATOR + inertia + gap closure) both scored 110 but remained inferred — no
concrete prompt text was committed for either.

**R4 design requirement**: Three single-axis explorations followed by two combinations.
Combinations include concrete text for both V-04-class and V-05-class prompts — finally
producing runnable text for variations that have scored 110 by inference for three consecutive
rounds.

**New axes for R4:**
- **Verdict-first** (role sequence): model writes the recommendation first, then the synthesis
  that supports it. Tests whether pre-committing to a verdict strengthens or weakens evidence
  grounding.
- **Table S2 + C-11 complete** (output format): V-02 R3 dropped the `— {expected finding
  type}` qualifier, falling from 110 to 95. R4 V-02 restores it. Tests whether the table
  format can reach 110 without the full inertia chain.
- **Signal Debate Gate** (lifecycle emphasis): an explicit pre-recommendation audit step that
  requires listing every signal-vs-signal conflict and labeling each RESOLVED or UNRESOLVED.
  A pure C-09 mechanism that does not rely on inertia framing. Tests whether a structural gate
  is equivalent to COMPLICATED markers for tension surfacing.

---

## Variation Axes

| Variation | Axis | Hypothesis | Prior Precedent |
|-----------|------|------------|-----------------|
| V-01 | Role sequence (verdict-first) | Pre-committing to verdict makes arc structurally earned | None — new axis |
| V-02 | Output format (table S2 + C-11 full) | Table + full qualifier reaches 107.5; needs inertia for 110 | R3 V-02 scored 95 (qualifier dropped) |
| V-03 | Lifecycle emphasis (debate audit gate) | Explicit debate table satisfies C-09 without inertia markers | R3 V-03 SIGNAL AUDIT gate was incomplete |
| V-04 | Combination: table + inertia + gap closure | Concrete version of R3 V-04 (inferred 110) | R3 V-04 inferred; never in concrete text |
| V-05 | Combination: EVALUATOR + inertia + gap closure | Concrete version of R3 V-05 (inferred 110) | R3 V-05 inferred across three rounds |

---

## V-01 — Verdict-First Role Sequence

**Axis**: Role sequence — the model writes the recommendation first (one sentence), then writes
the five-section synthesis as the reasoning that arrived at that verdict.

**Hypothesis**: Pre-committing to a verdict before writing any section prevents the
"appended recommendation" failure mode that C-06 and C-08 guard against. The synthesis
becomes justification for a known destination rather than a search for an unknown one. This
should structurally guarantee C-06 (recommendation grounded in pattern) because the author
is forced to name the pattern that supports an already-stated verdict. Risk: the recommendation
becomes self-confirming rather than evidence-driven, potentially weakening C-04. Expected
score: ~100–107.5 (C-10 and C-11 absent from single-axis form).

---

```
Read all signal artifacts for **{topic}** from `simulations/{topic}/`.

You are writing the story of what these signals say together. Before writing anything else,
write your recommendation in one sentence. Then write the five-section synthesis that arrived
at that verdict. The five sections are the reasoning; the verdict is the destination they reach.

---

### VERDICT (write this first, before Section 1)

One sentence only: **[Proceed | Pause | Pivot | Abandon]** — [one clause naming the decisive
pattern that drives this verdict].

Constraint: Do not hedge. If you are uncertain, name the default and the single specific
condition that would change it. "It depends" is not a verdict.

---

### Section 1 — The Question

What the team set out to understand, and why the answer was not already known. One paragraph.

State the signal set: list each signal by namespace/skill identifier. These are the only
signals that can appear in this story.

---

### Section 2 — What Each Signal Revealed

One finding per signal. 2–3 sentences maximum per signal. The single most important thing
this signal contributed — not a summary of its contents.

These entries are raw material for Section 3. Their purpose here is precision, not
completeness. Cut everything that is not the key finding.

Do not enumerate. Do not walk through signals in sequence as if each one is a chapter.
The mode is triage: what did this signal add that no other signal could have added?

---

### Section 3 — What the Signals Say Together

This is the interpretive core. Name the specific pattern that emerges from reading the
signals as a set.

This pattern must require all the signals: remove any one signal and the pattern either
disappears or changes substantially.

Falsify it: state explicitly what different set of findings would have produced a different
pattern. If you cannot falsify it, you have not named a pattern — you have named an
expectation.

Where signals conflict or point in different directions, name the tension explicitly rather
than resolving it into a single thread. A pattern that papers over real disagreement is
editorial suppression, not synthesis.

This section names the evidence for the verdict you wrote first. If the pattern here would
not support that verdict, return to the VERDICT and correct it before continuing.

---

### Section 4 — What Remains Uncertain

Name at least one specific evidence gap — something not yet gathered. A gap is not a debate
within existing signals. Distinguish:
- A gap requires a gathering action. The signal has not been collected.
- A debate requires a decision. Both sides are present in Section 2.

For each gap, name:
- The specific open question
- Which Section 2 finding is most exposed by its absence
- **Signal that would close it**: `{namespace}/{skill} — {one sentence: the expected finding
  type, specific enough that a team member could run the skill tomorrow and know what they
  are looking for}`

Signal plugin namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

---

### Section 5 — Recommendation

Restate the verdict you wrote first. One sentence of editorial rationale grounded in the
pattern named in Section 3. A reader must be able to trace the reasoning from Section 2
through Section 3 to this verdict without consulting the source signals.

Open with exactly one of: **Proceed** | **Pause** | **Pivot** | **Abandon**

Explain what executing this recommendation means: what the team does next.

---

Write the artifact to `simulations/{topic}/{topic}-story-{date}.md`.
```

---

## V-02 — Table S2 + C-11 Complete

**Axis**: Output format — Section 2 as a markdown table (Signal | Key Finding | Inertia Stance),
with the full `{namespace}/{skill} — {expected finding type}` gap closure format in Section 4.

**Hypothesis**: R3 V-02 scored 95 because it dropped the `— {expected finding type}` qualifier
from C-11. Restoring it should move C-11 from PARTIAL to PASS. The table format's structural
enforcement of C-05 (exactly one sentence per cell, visually obvious) combined with complete
C-11 format should produce ~107.5 — same score as R2 V-01 inertia-only form. C-10 remains
unaddressed (no trajectory declaration or full five-marker chain). This variation tests whether
the table + C-11-complete combination reaches 107.5 without inertia framing.

---

```
Read all signal artifacts for **{topic}** from `simulations/{topic}/`.

You are writing an editorial synthesis — an interpretation of what these signals say together.
This is not a sequential summary of each signal's findings. The table in Section 2 is raw
material for Section 3. The combination is what this document is for, not the enumeration
of its rows.

---

### Section 1 — Topic Framing

What the team set out to understand and why. One paragraph.

Signal set: [list all gathered signals by namespace/skill identifier]

---

### Section 2 — Signal Findings

| Signal | Key Finding | Inertia Stance |
|--------|-------------|----------------|
| {namespace}/{skill} | {exactly one sentence} | REINFORCES \| CHALLENGES \| NEUTRAL |

Rules:
- Every Key Finding cell is exactly one sentence. A two-sentence cell is a constraint
  violation — visible at a glance and must be corrected before continuing.
- Inertia Stance: does this signal reinforce the default trajectory (build this feature) or
  challenge it?
- Do not reproduce detail that belongs in the source artifact.

---

### Section 3 — What the Signals Say Together

Name the specific pattern that emerges from the table as a set. This pattern must require
all rows — it cannot be derived from any single row alone.

Falsify it: what different table contents would have produced a different pattern?

A Section 3 synthesis that averages away a visible REINFORCES/CHALLENGES split in the
Section 2 table is not cross-signal analysis — it is a misread of the evidence the table
presents. Where the table shows tension, the synthesis must name it: which rows conflict,
on what dimension, and what the conflict means for the pattern.

---

### Section 4 — Evidence Gaps

Name at least one evidence gap — something not yet gathered. Distinguish:
- A gap requires a gathering action. The signal has not been collected.
- A debate requires a decision. The signals disagree and both table rows are present.

For each gap, name:
- The specific open question
- Which table row is most exposed by this absence
- **Signal that would close it**: `{namespace}/{skill} — {one sentence: the expected finding
  type, specific enough that a team member could run the skill tomorrow and know what they
  are looking for}`

The closure entry must include both the namespace/skill identifier AND the expected finding
type. Naming the namespace/skill without the finding type does not meet this bar.

Signal plugin namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

---

### Section 5 — Recommendation

Open with exactly one of: **Proceed** | **Pause** | **Pivot** | **Abandon**

One sentence of editorial rationale grounded in the Section 3 pattern. A reader must be able
to trace the reasoning from the table through Section 3 to this verdict without consulting
the source signals.

---

Write the artifact to `simulations/{topic}/{topic}-story-{date}.md`.
```

---

## V-03 — Signal Debate Gate

**Axis**: Lifecycle emphasis — an explicit DEBATE AUDIT step (after Section 3, before Sections
4–5) that requires listing every signal-vs-signal conflict and labeling each RESOLVED or
UNRESOLVED before the recommendation is written.

**Hypothesis**: A structural debate-listing gate is equivalent to the COMPLICATED inertia
marker for C-09 — it makes signal tension structurally visible and requires the author to
name it before proceeding. Unlike inertia framing, the gate is not a section-level mechanism
but a discrete audit checkpoint. An UNRESOLVED entry propagates into Sections 3 and 4
automatically. Expected score: ~95–105. C-09 PASS expected; C-10 FAIL expected (no
trajectory declaration); C-11 PASS if gap closure format is present.

---

```
Read all signal artifacts for **{topic}** from `simulations/{topic}/`.

You are writing an editorial synthesis that interprets what these signals say together. Do
not walk through each signal in sequence. Do not produce an annotated list. The mode is
interpretation: what do the signals mean in combination, and what should the team do?

---

### Section 1 — Topic Framing

What the team set out to understand and why. One paragraph.

Signal set: [list all gathered signals by namespace/skill identifier]

---

### Section 2 — What Each Signal Revealed

One key finding per signal. 2–3 sentences maximum. The single most important thing this
signal contributed — not a summary of its contents.

These are the raw materials. Their purpose here is precision. Cut everything that is not
the key finding.

---

### Section 3 — What the Signals Say Together

Name the specific pattern that emerges from the signals in combination. The pattern must:
- Require multiple signals: remove any one signal and the pattern changes substantially
- Be falsifiable: state what different findings would have produced a different pattern

---

### DEBATE AUDIT (complete before writing Sections 4–5)

Review every Section 2 finding. For each pair of signals that point in different directions —
on any dimension — complete one row:

| Signal A | Signal B | What they disagree on | Resolution |
|----------|----------|----------------------|------------|
| {namespace}/{skill} | {namespace}/{skill} | {one sentence: the dimension of conflict} | RESOLVED: {which view Section 3 adopts, and why} \| UNRESOLVED: {both views persist} |

If no conflicts are found, write: "No conflicts detected — signals converge on [one sentence
summarizing the convergence]." This is a substantive claim, not a formatting default.

Constraint: An UNRESOLVED entry must appear in Section 3 (named in the pattern) and in
Section 4 (as an evidence gap or a decision point). An UNRESOLVED conflict that is absent
from Sections 3 and 4 is editorial suppression, not synthesis.

---

### Section 4 — What Remains Uncertain

Name at least one evidence gap — something not yet gathered. Distinguish:
- A gap requires a gathering action. The signal has not been collected.
- A debate requires a decision. The signals disagree and both are present in the DEBATE
  AUDIT. List UNRESOLVED audit entries here as decision points — they are not gaps.

For each gap, name:
- The specific open question
- Which Section 2 finding is most exposed by its absence
- **Signal that would close it**: `{namespace}/{skill} — {one sentence: the expected finding
  type, specific enough that a team member could run the skill tomorrow and know what to
  look for}`

Signal plugin namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

---

### Section 5 — Recommendation

Open with exactly one of: **Proceed** | **Pause** | **Pivot** | **Abandon**

One sentence of editorial rationale grounded in the Section 3 pattern. If the DEBATE AUDIT
contains UNRESOLVED entries, the recommendation must acknowledge the strongest counterargument
rather than pretending convergence.

---

Write the artifact to `simulations/{topic}/{topic}-story-{date}.md`.
```

---

## V-04 — Table + Inertia + Gap Closure (R3 V-04 in Concrete Text)

**Axes combined**: Output format (table S2) + inertia framing (full five-section chain) +
gap closure (full `{namespace}/{skill} — {expected finding type}` format).

**Hypothesis**: V-04 has scored 110 by inference in R2 and R3. This is the first concrete
prompt text for this combination. The table's Inertia Stance column provides a per-row
classification layer that strengthens both C-05 (structural one-sentence enforcement) and
C-09 (REINFORCES/CHALLENGES split visible before S3 synthesis). The full five-marker inertia
chain (S1 default → S2 state → S3 reading → S4 exposure → S5 resolution) provides the C-10
mechanism. The complete gap closure format provides C-11. Expected: 110.

---

```
Read all signal artifacts for **{topic}** from `simulations/{topic}/`.

You are writing an editorial synthesis that interprets what these signals say together — not
a summary of what each signal found. This story has a default trajectory, a table of signals
that confirm or complicate it, and a recommendation that resolves it. The table in Section 2
is raw material for Section 3; the combination is what this document is for, not the
enumeration of its rows.

---

### Section 1 — Topic Framing

**Default trajectory**: State the current plan-of-record — build this feature / don't build
this feature — before any signal findings appear. One sentence. This is the inertia each
table row is classified against.

What the team set out to understand and why this question mattered now. One paragraph.

Signal set: [list all gathered signals by namespace/skill identifier]

**Inertia state**: UNCONTESTED — synthesis begins from here.

---

### Section 2 — What Each Signal Revealed

| Signal | Key Finding | Inertia Stance |
|--------|-------------|----------------|
| {namespace}/{skill} | {exactly one sentence — the single most important finding} | CONFIRMS \| COMPLICATES \| REVERSES |

Rules:
- Every Key Finding cell is exactly one sentence. A two-sentence cell is a visible constraint
  violation; correct it before continuing.
- Inertia Stance: does this signal confirm the default trajectory (CONFIRMS), complicate it
  (COMPLICATES), or reverse it (REVERSES)?
- If COMPLICATES or REVERSES: the prose below the table must name which dimension of the
  default is being challenged and which specific signals caused the shift.
- Do not reproduce detail that belongs in the source artifact.

A Section 3 synthesis that averages away a visible COMPLICATES/REVERSES split in this table
is not cross-signal analysis — it is a misread of the evidence the table presents.

**Inertia state after Section 2**: [CONFIRMED | COMPLICATED | REVERSED] — one sentence
stating what the table as a whole says about the default trajectory.

---

### Section 3 — What the Signals Say Together

Name the specific pattern that emerges from reading the table as a set. This pattern must
require all rows: remove any one and the pattern changes substantially.

Falsify it: what different table contents would have produced a different pattern?

Where the table shows a COMPLICATES or REVERSES stance: name what caused the shift —
which signals, on which dimension. This is not optional. A synthesis that absorbs a marked
tension without naming it is editorial suppression.

**Inertia reading**: [HOLDS | COMPLICATES | REVERSES] — one sentence: what does the
cross-signal pattern say about the default trajectory?

---

### Section 4 — What Remains Uncertain

Name at least one evidence gap — something not yet gathered. Distinguish:
- A gap requires a gathering action. The signal has not been collected.
- A debate requires a decision. The signals disagree and both table rows are present.

For each gap, name:
- The specific open question
- Which table row is most exposed by this absence
- **Signal that would close it**: `{namespace}/{skill} — {one sentence: the expected finding
  type, specific enough that a team member could run the skill tomorrow and know what they
  are looking for}`

Signal plugin namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

**Inertia exposure**: If this gap were closed against the current direction, how would the
trajectory change? One sentence.

---

### Section 5 — Recommendation

Open with exactly one of: **Proceed** | **Pause** | **Pivot** | **Abandon**

One sentence of editorial rationale grounded in the Section 3 pattern. A reader must trace
the reasoning from the table through Section 3 to this verdict without consulting the
source signals.

**Trajectory resolution**: [HOLDS | REVERSES | PIVOTS] — one sentence resolving the arc
that opened in Section 1. The recommendation resolves — not restates — the default trajectory.

---

Inertia chain audit: a reader scanning only the five markers (Section 1 state → Section 2
state → Section 3 reading → Section 4 exposure → Section 5 resolution) must be able to
follow the trajectory without reading the prose.

---

Write the artifact to `simulations/{topic}/{topic}-story-{date}.md`.
```

---

## V-05 — EVALUATOR + Inertia + Gap Closure (R3 V-05 in Concrete Text)

**Axes combined**: Role sequence (EVALUATOR pre-synthesis phase) + inertia framing (full
five-section chain) + gap closure (full `{namespace}/{skill} — {expected finding type}` format).

**Hypothesis**: V-05 has scored 110 by inference across R1, R2, and R3. This is the first
concrete prompt text for this architecture. The EVALUATOR phase provides the strongest
possible C-01 mechanism: the model reads all signals as a flat list before writing a single
prose sentence, eliminating reading-order bias at the architecture level. The inertia chain
in the AUTHOR phase provides C-09 and C-10. The complete gap closure format provides C-11.
Three anti-enumeration layers: EVALUATOR flat list + per-section inertia markers + "the
combination is what this document is for" framing. Expected: 110.

---

```
Read all signal artifacts for **{topic}** from `simulations/{topic}/`.

This task runs in two phases. Complete the EVALUATOR phase fully before writing any prose
in the AUTHOR phase.

---

## EVALUATOR PHASE

You are a signal evaluator, not a writer. Your job is to read every signal and produce a
flat inventory — one line per signal — before any synthesis begins. Do not write narrative
prose. Do not draw conclusions. Record.

For each gathered signal, produce exactly one line:

`{namespace}/{skill}: {one sentence — the single most important finding from this signal} | Inertia: [CONFIRMS | COMPLICATES | REVERSES] the default trajectory to build this feature`

Include every signal. Do not skip signals because they seem minor or redundant. If two
signals conflict, record both — do not resolve the conflict in the inventory.

After the full inventory is complete, scan it: are any lines in direct tension with each
other (one CONFIRMS, one REVERSES, on the same dimension)? Mark those pairs `[TENSION]`.

---

## AUTHOR PHASE

You are now the author. The EVALUATOR inventory is your source material. Use it; do not
re-read the original signals. The inventory is a flat list; your synthesis is an
interpretation of what it says in combination. Enumeration of inventory lines is not
synthesis.

---

### Section 1 — Topic Framing

**Default trajectory**: The plan-of-record before the EVALUATOR phase began. State it
explicitly in one sentence: build this feature / don't build this feature. This is the
inertia every EVALUATOR line was classified against.

What the team set out to understand and why. One paragraph.

Signal set: [list all signals from the EVALUATOR inventory]

**Inertia state**: UNCONTESTED — AUTHOR synthesis begins from here.

---

### Section 2 — What Each Signal Revealed

For each signal: its key finding from the EVALUATOR inventory, interpreted. 2–3 sentences
maximum — never expand beyond what the inventory recorded, but you may interpret the finding's
significance.

If the EVALUATOR inventory shows COMPLICATES or REVERSES for any line: name which signals
pushed against the default and on which dimension. Do not average them into a neutral reading.

**Inertia state after Section 2**: [CONFIRMED | COMPLICATED | REVERSED] — what does the
collection of EVALUATOR entries say about the default trajectory?

---

### Section 3 — What the Signals Say Together

This is the interpretive core. Draw on the EVALUATOR inventory as a set — not as a sequence.

Name the specific pattern that emerges. It must require multiple signals: remove any one
and the pattern changes. Falsify it: what different inventory contents would have produced
a different pattern?

Where the EVALUATOR inventory shows a `[TENSION]` pair: name it explicitly. Which signals
are in tension, on what dimension, and what the tension means for the synthesis. A pattern
that absorbs a marked `[TENSION]` without naming it is editorial suppression, not synthesis.

**Inertia reading**: [HOLDS | COMPLICATES | REVERSES] — what does the cross-signal pattern
say about the default trajectory?

---

### Section 4 — What Remains Uncertain

Name at least one evidence gap — something the EVALUATOR inventory does not contain.
Distinguish:
- A gap: a signal type not yet gathered. The EVALUATOR inventory has no line for it.
  Requires a gathering action.
- A debate: two EVALUATOR lines that are in `[TENSION]`. The evidence is present but
  disagrees. Requires a decision, not a gathering action.

For each gap, name:
- The specific open question
- Which EVALUATOR inventory line is most exposed by its absence
- **Signal that would close it**: `{namespace}/{skill} — {one sentence: the expected finding
  type, specific enough that a team member could run the skill tomorrow and know what to
  look for}`

Signal plugin namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

**Inertia exposure**: If this gap were closed against the current direction, how would the
trajectory change? One sentence.

---

### Section 5 — Recommendation

Open with exactly one of: **Proceed** | **Pause** | **Pivot** | **Abandon**

One sentence of editorial rationale grounded in the Section 3 pattern. Trace from the
EVALUATOR inventory through Section 3 to this verdict. Do not reference the original
source signals directly — the inventory is the authoritative source for this phase.

**Trajectory resolution**: [HOLDS | REVERSES | PIVOTS] — resolve the arc that opened in
Section 1. The recommendation resolves the trajectory; it does not introduce a new conclusion.

---

Inertia chain audit: a reader scanning only the five markers (Section 1 state → Section 2
state → Section 3 reading → Section 4 exposure → Section 5 resolution) must be able to
follow the trajectory without reading the prose.

---

Write the artifact to `simulations/{topic}/{topic}-story-{date}.md`.
```

---

## Predicted Scores Against v3 Rubric

| ID | Axis | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | Predicted |
|----|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| V-01 | Verdict-first | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | FAIL | PASS | ~97.5 |
| V-02 | Table + C-11 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | FAIL | PASS | ~107.5 |
| V-03 | Debate gate | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | FAIL | PASS | ~105 |
| V-04 | Table+Inertia+Gap | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **110** |
| V-05 | Eval+Inertia+Gap | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **110** |

**Prediction rationale:**

- **V-01 C-09 PARTIAL**: verdict-first framing does not name the tension-surfacing failure mode
  explicitly. The model may still average disagreements. The `{namespace}/{skill} — {expected
  finding type}` format in S4 provides full C-11.

- **V-01 C-10 FAIL**: no trajectory declaration in S1, no per-section inertia markers. The
  verdict-first architecture is a different arc mechanism (destination-first vs. trajectory-
  tracking) — it satisfies C-08 differently than C-10's specific marker chain requirement.

- **V-02 C-08 PARTIAL**: table format without full five-marker inertia chain does not guarantee
  arc across sections. The Inertia Stance column provides per-row classification within S2 but
  no cross-section trajectory that C-10 requires.

- **V-02 C-10 FAIL**: no trajectory declaration or five-marker chain. Same failure as R3 V-02.

- **V-03 C-08 PARTIAL**: the DEBATE AUDIT gate creates an arc checkpoint, but the sections
  before and after the gate are not formally linked by a trajectory state marker. Likely
  partial credit.

- **V-03 C-10 FAIL**: no trajectory declaration, no per-section inertia markers. The debate
  gate is a correctness mechanism (surfaces tension), not a trajectory-tracking mechanism.

- **V-04 and V-05**: both preserve all mechanisms that passed in R3. V-04 adds the table's
  structural one-sentence enforcement over V-01's prose form; V-05 adds the EVALUATOR phase's
  reading-order bias elimination. Both are expected to be the first concrete 110 scorers in
  their respective format classes.

---

## Design Notes

**Verdict-first (V-01) is a new mechanism for C-08.** The existing solutions for C-08
(inertia markers, EVALUATOR pre-synthesis momentum) are all forward-arc: the arc builds
from S1 to S5. Verdict-first creates a reverse-arc: the destination is declared, the synthesis
is the journey there. Both guarantee arc; they produce it differently. C-10 specifically
requires trajectory-tracking markers in the forward direction — verdict-first satisfies C-08
but cannot satisfy C-10's letter.

**The debate gate (V-03) and COMPLICATED inertia marker are not equivalent.** The COMPLICATED
marker classifies a section's relationship to the default trajectory; the debate gate audits
pairwise signal conflicts. They catch different failure modes:
- COMPLICATED catches trajectory-level disagreements (this section complicates the trajectory)
- Debate gate catches signal-level disagreements (these two signals conflict with each other)
A signal can COMPLICATE the trajectory without any two signals directly conflicting, and two
signals can conflict without either causing a trajectory COMPLICATION. Both mechanisms pass
C-09 independently.

**V-04 and V-05 are the same rubric score from different engineering postures.** V-04 assumes
the model's inertia markers are sufficient anti-enumeration pressure for the signal set size.
V-05 adds the EVALUATOR pre-read as an insurance layer for large or thematically dense signal
sets. Neither adds rubric value the other lacks; both reach 110.
