---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 3
rubric: v3
---

# Variations — topic-story (Round 3)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: R2's excellence signals produced two new aspirational criteria. C-12
(Pre-Synthesis Extraction Visible) was sourced from R2 V-05's EVALUATOR/AUTHOR phase
separation — but V-05's flat list was an internal processing step, not present in the output
artifact. C-12's pass condition requires a discrete extraction section visible in the output.
C-13 (Framework Subordination) was sourced from V-04 vs V-02 divergence on C-07 — V-04
establishes the editorial arc first via inertia framing, then subordinates gap closure
vocabulary to it; V-02 lets the protocol vocabulary drive and the arc never emerges. C-13's
pass condition: removing all structural labels must leave a coherent editorial narrative.

Round 3 primary axes: V-01 targets C-12 directly (extraction visible in output). V-02
targets C-13 directly (arc-first, markers as post-hoc annotation, with a removal test).
V-03 is a role-sequence variant (strict EXTRACTOR/AUTHOR role boundary with forbidden
lists) — a structurally different mechanism for C-12 that also tests role-discipline as an
independent path to extraction-before-synthesis. V-04 and V-05 are combinations.

---

## V-01

**Variation axis**: Output format — extraction section visible in artifact
**Hypothesis**: C-12 requires a discrete extraction section in the output, not an internal
phase. R2 V-05's EVALUATOR phase produced a flat list as a processing step that was never
written to the artifact — the model extracted internally and synthesized from memory,
reintroducing reading-order bias. Making the Signal Extract a named output section directly
satisfies C-12's pass condition ("a discrete extraction section is present — a flat list,
one sentence per signal, in artifact order"). The synthesis then draws exclusively from the
visible list, making the bias-resistance architecture auditable rather than asserted.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill produces an artifact with two named sections in order: **Signal Extract**, then
**Story**. Both appear in the output. Complete them in sequence — do not begin the Story
until the Signal Extract is finished.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present. Note the original question or
hypothesis that motivated signal gathering.

---

### Step 2 — Signal Extract

Write the Signal Extract as the first section of the output artifact.

```markdown
## Signal Extract
- `{artifact-name}`: {one sentence — the single most important finding from this artifact}
- `{artifact-name}`: {one sentence — the single most important finding from this artifact}
...
```

Rules:
- One line per artifact, in the order you read them (artifact order, not thematic order)
- No grouping by namespace or apparent theme
- No ranking by apparent significance
- One sentence per artifact, no elaboration

The purpose of this list: every finding surfaces at equal weight, in gather order, before
synthesis begins. Patterns identified from this flat list are less vulnerable to
reading-order bias and thematic pre-clustering than patterns identified by re-reading
artifacts in sequence. This list is not a scratchpad — it is part of the artifact.

Do not begin the Story until the Signal Extract is complete.

---

### Step 3 — Story

Write the Story immediately following the Signal Extract. Synthesize from the Signal
Extract — not from re-reading artifacts. When you reference a finding, it must appear in
the Signal Extract.

Five beats, all present and distinguishable:

**Beat 1 — What we set out to understand**
One to three sentences. The original question from strategy.md, or inferred from the topic
if strategy is absent. What specific uncertainty motivated signal gathering?

**Beat 2 — What each signal revealed**
Draw from the Signal Extract. One key finding per signal — the finding most relevant to the
original question. Two sentences maximum per signal. Exercise editorial discipline: omit
secondary findings.

**Beat 3 — What the signals say together**
The interpretive core. Name the pattern — a convergence, divergence, tension, or gap —
visible only across the Signal Extract, not in any single entry. Reference at least two
entries by artifact name. Draw a conclusion about their relationship.

Falsifiability test: *Can any single Signal Extract entry produce this conclusion alone?*
If yes, the pattern is not yet cross-signal. Look at what two or more entries reveal
together that no single entry shows.

**Beat 4 — What remains uncertain**
Specific open questions not closed by any Signal Extract entry. Scope each: what exactly
is unknown, and why does it matter for the recommendation? No generic disclaimers.

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph connecting the recommendation to the Beat 3 pattern. The recommendation must
be inferable from Beat 3 before a reader reaches Beat 5. If the recommendation surprises,
rewrite Beat 3 first.

---

### Voice

Write as an author, not as a system. Active voice. Take positions. The Story section
should read as a briefing a decision-maker would quote from.

---

### Output

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## Signal Extract
[flat list — artifact order, one line per signal]

## Story
[five beats]
```

---

## V-02

**Variation axis**: Inertia framing — arc-first, markers as post-hoc annotation
**Hypothesis**: C-13's failure mode is vocabulary-driven narrative: inertia markers appear
as section organizers and the arc never emerges independent of them. Removing markers leaves
a protocol log. The fix: require the model to write editorial prose first within each
section, then add the inertia marker as confirmation of what the prose already says. The
marker annotates; it does not organize. The removal test — "if removing all markers creates
a gap in the reasoning, the markers were doing structural work they should not have been
doing" — is a verifiable post-hoc check that the arc was established through words, not
labels. This is architecturally distinct from R2 V-01 (which used inertia markers as
section openers) and V-04 (which combined markers with gap closure). Those variants
established the marker first, then wrote to satisfy it; V-02 here reverses the order.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Declare the trajectory (private, before writing)

Based on strategy.md (or inferred from the topic if absent), state:

> **Trajectory**: The default expectation entering signal gathering was: [one sentence —
> what the team expected to find or hoped to confirm].

This is your arc anchor. You will annotate the Story relative to it. But the annotation
confirms what your prose already establishes — it does not prescribe what to write.

---

### Write the story

Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Writing discipline for every section**: Write the editorial prose first. Once the prose
is complete, add the inertia marker as a final annotation. The marker should confirm what
the prose already says. If choosing the marker tells you what to write, you are using it
backwards — the prose should determine the marker, not the reverse.

Inertia markers:
- `[CONFIRMED]` — section's evidence supports the trajectory
- `[COMPLICATED]` — complicates but does not reverse
- `[REVERSES]` — substantially undermines the trajectory
- `[UNCERTAIN]` — genuine open question the trajectory cannot resolve

**Removal test**: When the story is complete, re-read it without the inertia markers. The
story must be fully readable — a reader with no knowledge of the marker vocabulary should
be able to follow the reasoning. If removing a marker creates a logical gap, the marker was
doing structural work it should not have been doing. Rewrite the prose so the arc is
carried by the words.

---

**S1 — What we set out to understand** `[marker — added after writing prose]`
Prose first. One to three sentences. The original question and the specific uncertainty that
motivated signal gathering.

**S2 — What each signal revealed** `[marker — added after writing prose]`
Prose first. One key finding per signal, two sentences maximum. Single most relevant finding
per signal.
If the marker is `[COMPLICATED]`: the prose — not the marker — must name which signals
pushed against the default expectation and why.

**S3 — What the signals say together** `[marker — added after writing prose]`
Prose first. The cross-signal pattern. Reference at least two signals. Draw the cross-signal
conclusion. Where signals diverge, name the tension and adjudicate: state which
interpretation the evidence more strongly supports and why. Do not paper over genuine
conflict.
If the marker is `[COMPLICATED]` or `[REVERSES]`: the prose must already carry the
explanation of what caused the shift before the marker is placed.

**S4 — What remains uncertain** `[marker — added after writing prose]`
Prose first. Specific, scoped open questions. Name what is unknown and why it matters for
the recommendation. Debates already adjudicated in S3 are not gaps — a gap requires a
gathering action, not a judgment.

**S5 — Recommendation** `[marker — added after writing prose]`
Prose first. One of: **proceed**, **pause**, **pivot**, **abandon**. One paragraph
connecting the recommendation to the S3 pattern.
"Proceed with caution" without naming the caution fails. "It depends" without a stated
default fails. The marker must match the arc — proceeding despite `[REVERSES]` requires
the prose to carry the explicit reasoning against the trajectory.

---

**Voice**: Active. Opinionated. The story should be fully intelligible to a reader who
ignores every bracket label. Write as the author of a briefing.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

---

## V-03

**Variation axis**: Role sequence — strict EXTRACTOR / AUTHOR boundary with forbidden lists
**Hypothesis**: The failure mode C-12 targets — reading-order bias and thematic
pre-clustering — is caused by the model blending extraction and synthesis in real time as
it reads each artifact. Naming two distinct roles with explicit forbidden lists creates a
hard cognitive boundary that V-01's output-visibility instruction does not create: the
EXTRACTOR is forbidden from interpreting; the AUTHOR is forbidden from re-reading signals.
The EXTRACTOR's flat list appears in the output (satisfying C-12's pass condition
independently of V-01's output-format instruction). The Author-cannot-re-read rule closes
the escape route V-01 leaves open: a model could produce a Signal Extract section but then
re-read artifacts anyway and synthesize from memory. Role-with-forbidden-list closes that.
This tests whether role-discipline is a distinct and sufficient mechanism for C-12.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs two roles in strict sequence: **EXTRACTOR**, then **AUTHOR**. The roles
may not overlap. Each role has a forbidden list. Complete EXTRACTOR fully before beginning
AUTHOR.

---

## EXTRACTOR

**Your job**: Read everything. Extract the single most important finding from each artifact.
Produce a flat list. Write the list to the output artifact.

**Forbidden**: Forming patterns. Noting similarities. Drawing cross-signal conclusions.
Identifying tensions. Grouping by theme. These belong to AUTHOR.

**Step 1**: Glob `simulations/**/{topic}-*`. Read every artifact. Also read
`simulations/{topic}/strategy.md` if present — note the original question.

**Step 2**: For each artifact, in the order you encountered it, write exactly one line:
`{artifact-name}: {one sentence — the single most important finding, stated as a fact, no
interpretation}`

Every artifact gets one line. If you find yourself writing "this might suggest..." or
"combined with X, this indicates..." — stop. That is synthesis. Save it for AUTHOR. State
the finding as a standalone fact.

Produce the complete Signal Extract before advancing. Do not begin AUTHOR until the list
is finished.

---

**EXTRACTOR OUTPUT — written to artifact**:

```markdown
## Signal Extract
*{N} artifacts read, in gather order.*
- `{artifact-name}`: {finding as fact}
- `{artifact-name}`: {finding as fact}
...
```

---

## AUTHOR

**Your job**: Synthesize. Find the pattern. Tell the story. Recommend.

**Forbidden**: Re-reading signal artifacts. You may only draw on findings that appear in
the Signal Extract above. If you feel the need to re-read a signal to confirm something,
the finding is already in the list — use it. If it is not in the list, it is not available
to this synthesis.

**Input**: The Signal Extract above and the original question from strategy.md (or inferred
from topic if absent).

---

### Write the story

Write immediately following the Signal Extract in the artifact.

Five beats, all present and distinguishable:

**Beat 1 — What we set out to understand**
The original question. One to three sentences. What specific uncertainty motivated signal
gathering?

**Beat 2 — What each signal revealed**
Draw directly from the Signal Extract. One finding per signal, two sentences maximum. The
most relevant finding per signal for the original question — not a secondary finding.

**Beat 3 — What the signals say together**
The pattern visible only across the flat list, not in any single entry. Reference at least
two entries by artifact name. Draw the cross-signal conclusion.

Self-check: scan the Signal Extract. Does any single entry contain your conclusion? If yes,
the pattern is a single-signal observation repackaged, not a synthesis. Find what two or
more entries reveal in combination that no single entry shows.

Where entries point in different directions, name the tension and adjudicate — state which
interpretation the weight of the list supports and why.

**Beat 4 — What remains uncertain**
Specific open questions not closed by any Signal Extract entry. Scope each: what is unknown
and why it matters for the recommendation. Generic disclaimers fail.

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**. One paragraph connecting to the
Beat 3 pattern. "Proceed with caution" without naming the caution fails. "It depends"
without a stated default fails.

---

**Voice**: Active, editorial, opinionated. Take positions. Write as an author, not as a
reporter recapping a list.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

[Signal Extract — produced by EXTRACTOR]

## Story
[five beats — produced by AUTHOR]
```

---

## V-04

**Variation axis**: Combination — V-01 (extraction visible in output) + V-02 (arc-first,
markers as post-hoc annotation)
**Hypothesis**: V-01 targets C-12 via output format: extraction section must appear in the
artifact. V-02 targets C-13 via writing order: prose establishes arc first, marker confirms
post-hoc. The two axes are orthogonal — V-01 operates before synthesis begins (the
extraction architecture); V-02 operates during synthesis (the relationship between
vocabulary and arc within each section). No structural conflict: the Signal Extract
(V-01 mechanism) is produced before the Story begins, and the arc-first discipline (V-02
mechanism) operates within each Story section. Together they should crack C-12 and C-13
simultaneously. Baseline coverage for C-01 through C-11 is maintained: anti-summary
pressure from the extraction-first architecture, per-signal discipline enforced by the
flat-list format, and recommendation grounding enforced by the pattern-traceability rule.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill produces an artifact with two named sections in order: **Signal Extract**, then
**Story**. Complete them in sequence.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present. Note the original question and the
default expectation entering signal gathering.

---

### Step 2 — Trajectory declaration (private)

Before writing, state:

> **Trajectory**: The default expectation entering signal gathering was: [one sentence —
> what the team expected to find].

This is your arc anchor. Sections will be annotated relative to it — but the arc is
established through prose first. The trajectory declaration is a reference, not a frame.

---

### Step 3 — Signal Extract

Write the Signal Extract as the first named section of the output artifact. Do not begin
the Story until this section is complete.

```markdown
## Signal Extract
- `{artifact-name}`: {one sentence — the single most important finding, in artifact order}
...
```

Rules: one line per artifact, in the order read, no thematic grouping, no ranking by
apparent significance. This list is the synthesis input, not an internal step.

---

### Step 4 — Story

Write the Story drawing from the Signal Extract and trajectory declaration. Five beats,
all present and distinguishable.

**Writing discipline for every section**: Write the editorial prose first. Once the prose
is complete, add the inertia marker as a final annotation confirming what the prose already
says. If choosing the marker tells you what to write, reverse the order — prose determines
marker, not the reverse.

Inertia markers: `[CONFIRMED]` · `[COMPLICATED]` · `[REVERSES]` · `[UNCERTAIN]`

**Removal test**: When the Story is complete, re-read it without markers. It must be fully
readable. If removing a marker creates a logical gap, rewrite the prose to carry the arc.

---

**Beat 1 — What we set out to understand** `[marker — after prose]`
*Prose first.* One to three sentences. The original question. What specific uncertainty
motivated signal gathering?

**Beat 2 — What each signal revealed** `[marker — after prose]`
*Prose first.* Draw from the Signal Extract. One finding per signal, two sentences maximum.
If the marker becomes `[COMPLICATED]`: the prose must name which Signal Extract entries
pushed against the default and why — by artifact name.

**Beat 3 — What the signals say together** `[marker — after prose]`
*Prose first.* The cross-signal pattern. Reference at least two Signal Extract entries.
Draw the cross-signal conclusion. Where entries diverge, adjudicate — name which
interpretation the evidence more strongly supports and why.

Falsifiability test: *Does any single Signal Extract entry contain this conclusion?* If
yes, the pattern is not yet cross-signal.

If the marker becomes `[COMPLICATED]` or `[REVERSES]`: the prose — not the marker —
must name what caused the shift.

**Beat 4 — What remains uncertain** `[marker — after prose]`
*Prose first.* Specific, scoped open questions. Debates adjudicated in Beat 3 are not
gaps — a gap requires a gathering action.

**Beat 5 — Recommendation** `[marker — after prose]`
*Prose first.* One of: **proceed**, **pause**, **pivot**, **abandon**. One paragraph
connecting to the Beat 3 pattern. Marker must match the arc — proceeding despite
`[REVERSES]` requires the prose to carry explicit reasoning against the trajectory.
"It depends" without a stated default fails. "Proceed with caution" without naming the
caution fails.

---

**Voice**: Active. Opinionated. Write as the author of a briefing.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## Signal Extract
[flat list — artifact order, one line per signal]

## Story
[five beats, prose-first then marker annotation, removal test applied]
```

---

## V-05

**Variation axis**: Full combination — R2 V-05 base (EVALUATOR/AUTHOR phase separation +
inertia markers + gap closure protocol) upgraded with R3 additions (extraction visible in
output artifact + arc-first annotation discipline in AUTHOR phase)
**Hypothesis**: R2 V-05 was the strongest performer across C-01, C-04, C-05 but did not
crack C-12: the EVALUATOR's flat list was an internal processing step, not written to the
artifact. C-12's pass condition explicitly requires visibility in the output. Adding two
targeted instructions to the R2 V-05 base: (1) the EVALUATOR's flat list is explicitly
produced as a named Signal Extract section in the artifact; (2) the AUTHOR phase receives
an arc-first instruction — each section writes prose before placing the inertia marker —
with the removal test. These additions are surgical: the existing EVALUATOR/AUTHOR phase
boundary (C-12 architecture), inertia markers (C-09/C-10), and gap closure format (C-11)
are preserved. Expected to crack all six aspirational criteria simultaneously: C-08 via
the narrative arc established in AUTHOR's arc-first discipline; C-09 via the trajectory
declaration calibrating recommendation strength to signal convergence; C-10 via the
adjudication requirement in S3; C-11 via the "inferable from S3" rule in S5; C-12 via the
Signal Extract section in the output; C-13 via the arc-first/removal-test instruction.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two phases: **EVALUATOR** then **AUTHOR**. Do not begin the AUTHOR
phase until the EVALUATOR phase is complete.

---

## EVALUATOR Phase

**Gather all signals.**
Glob `simulations/**/{topic}-*`. Read every artifact.
Also read `simulations/{topic}/strategy.md` if present.

**Produce the Signal Extract.**
For each artifact, in the order you read it, write exactly one line:
`{artifact-name}: {one sentence — the single most important finding from this artifact}`

Do not filter. Do not rank. Do not group by namespace or theme. Every artifact gets one
line. Artifact order is neutral relative to the pattern not yet identified.

This list is written to the output artifact as a named section. It is not a scratchpad.

**Declare the trajectory.**
Based on strategy.md (or inferred from the topic if absent):

> **Trajectory**: [one sentence — the default expectation the team held entering signal
> gathering]

Do not begin the AUTHOR phase until both the Signal Extract and trajectory declaration
are complete and written.

---

**EVALUATOR produces this section in the artifact:**

```markdown
## Signal Extract
*{N} artifacts, in gather order.*
- `{artifact-name}`: {finding}
- `{artifact-name}`: {finding}
...
```

---

## AUTHOR Phase

**Input**: The Signal Extract and trajectory declaration from the EVALUATOR phase.
**Rule**: Do not re-read signal artifacts. Every finding you reference must appear in the
Signal Extract. If you need to consult a signal, the finding is already in the list.

Write to `simulations/{topic}/{topic}-story-{date}.md`, with the Story section following
the Signal Extract.

**Writing discipline for every section**: Write the editorial prose first. Once the prose
is complete, add the inertia marker as a final annotation confirming what the prose already
says. Prose determines marker. If choosing the marker tells you what to write, you are
using it backwards.

Inertia markers: `[CONFIRMED]` · `[COMPLICATED]` · `[REVERSES]` · `[UNCERTAIN]`

**Removal test**: When the Story is complete, re-read it without any inertia markers. It
must be fully readable as a briefing. If removing a marker creates a logical gap — if the
reasoning depends on the bracket label — rewrite the prose to carry the arc independently.

A reader scanning only the five markers must be able to follow the arc without reading the
prose. Both constraints must be satisfied: the prose carries the arc AND the markers
faithfully annotate it.

---

**S1 — What we set out to understand** `[marker — after prose]`
*Prose first.* Restate the trajectory and original question. One to three sentences. What
specific uncertainty motivated signal gathering?

**S2 — What each signal revealed** `[marker — after prose]`
*Prose first.* Draw from the Signal Extract. One finding per signal, two to three sentences
maximum. These entries are raw material for S3 — their combination, not their enumeration,
is what this document is for.
If the marker becomes `[COMPLICATED]`: the prose must name which Signal Extract entries
pushed against the default and why — by artifact name.

**S3 — What the signals say together** `[marker — after prose]`
*Prose first.* The cross-signal pattern. Only visible across the Signal Extract, not in
any single entry. Reference at least two entries. Draw the cross-signal conclusion.
Where entries diverge, name the tension and adjudicate — commit to which interpretation
the evidence more strongly supports, and say why. A synthesis that papers over real
disagreement is editorial suppression, not synthesis.
Falsifiability test: *Does any single Signal Extract entry contain this conclusion?* If
yes, the pattern is not yet cross-signal.
If the marker becomes `[COMPLICATED]` or `[REVERSES]`: the prose must carry the
explanation of what caused the shift before the marker is placed.

**S4 — What remains uncertain** `[UNCERTAIN]`
*Prose first.* Specific, scoped gaps. Debates adjudicated in S3 are not gaps — a gap
requires a gathering action. Do not re-open adjudicated tensions here.

Format each entry:
```
Gap: [what is unknown]
Most exposed finding: [which Signal Extract entry cannot be confirmed without this signal]
Next signal: {namespace}/{skill} — [one sentence: what the signal would reveal]
```

**S5 — Recommendation** `[marker — after prose]`
*Prose first.* One of: **proceed**, **pause**, **pivot**, **abandon**. One paragraph
grounding the recommendation in the S3 pattern. The recommendation direction must be
inferable from S3 and S4 before a reader reaches S5 — the final beat should land as "of
course," not as a pivot. The marker must match the arc — proceeding despite `[REVERSES]`
requires the prose to carry explicit reasoning against the trajectory.
"It depends" without a stated default fails. "Proceed with caution" without naming the
caution fails.

---

**Voice**: Active. Opinionated. Write as the author of a briefing a decision-maker would
quote from.

---

### Output structure

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## Signal Extract
*{N} artifacts, in gather order.*
- `{artifact-name}`: {finding}
...

## Story

### S1 — What we set out to understand
[MARKER] Prose...

### S2 — What each signal revealed
[MARKER] Per-signal findings from Signal Extract...

### S3 — What the signals say together
[MARKER] Cross-signal pattern with adjudication...

### S4 — What remains uncertain
[UNCERTAIN] Gap entries (Gap / Most exposed finding / Next signal)...

### S5 — Recommendation
[MARKER] **PROCEED / PAUSE / PIVOT / ABANDON** — grounding paragraph...
```

Artifact: `simulations/{topic}/{topic}-story-{date}.md`
