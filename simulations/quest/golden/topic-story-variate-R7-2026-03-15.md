---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 7
rubric: v6
---

# Variations — topic-story (Round 7)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v6 rubric adds C-16 (hypothesis mutation proof) and C-17 (defensible
adjudication). The two extractable patterns from Round 6:

**C-16 sourced from R6 V-01 (C-14 PASS — hypothesis threading)**: The anti-stagnation
guard — "if S3's hypothesis is identical to S0, you have not stress-tested it" — is a
*negative proof requirement* not yet formalized. C-14 required the hypothesis to thread
through each signal; C-16 requires the delta between S0 and S3 to be *visible in the
artifact*, not merely implied by narrative progression.

**C-17 sourced from R6 V-02 (C-09 PASS via "apply the stance protocol to the adjudication
itself")**: Conflict adjudication verdicts must carry because-clauses. C-13 required
RESOLVED/UNRESOLVED classification; C-15 required rationale on per-signal stances; C-17
is the intersection — the adjudication verdict itself must be defensible, not just labeled.

Round 7 primary axes: V-01 targets C-16 directly (mutation ledger — S0 stated before reading,
S3 stated after, delta required). V-02 targets C-17 directly (because-clause enforcement on
each adjudication verdict). V-03 targets C-15 (stance rationale per signal — one sentence
explaining why the stance was assigned). V-04 combines C-16 + C-17 (mutation ledger +
because-clause adjudication). V-05 is the full combination: R3 V-05 base (EVALUATOR/AUTHOR
phases + Signal Extract visible in artifact) upgraded with all three v6 mechanisms.

---

## V-01

**Variation axis**: Lifecycle emphasis — hypothesis mutation ledger
**Hypothesis**: C-16 fails when the hypothesis evolves implicitly through narrative prose but
no visible S0→S3 delta exists in the artifact. The fix is structural: require the working
hypothesis to be stated before any signals are read (S0), require each signal in S2 to record
its effect on the hypothesis (CONFIRMS / MODIFIES [from X to Y] / CONTRADICTS), and require
a final hypothesis statement (S3) after all per-signal stances are recorded. The anti-stagnation
check — "if S3 is identical to S0, you have not stress-tested the hypothesis" — is a verifiable
artifact-level assertion, not a voice instruction. This tests whether a mutation ledger as an
output format directly satisfies C-16's pass condition without also requiring voice or register
changes.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Declare the working hypothesis (S0)

Before reading any signal findings, write:

```
Working hypothesis (S0): [one sentence — the specific claim the team entered with,
or inferred from strategy.md if not explicitly stated]
```

This is not the original question. It is the answer the team was implicitly expecting to
confirm. Write it as a falsifiable claim, not as a goal.

---

### Step 3 — Hypothesis mutation tracking (produces S2 section)

For each signal artifact, in the order read, write one entry:

```
- `{artifact-name}`: {one to two sentences — the key finding most relevant to the working
  hypothesis}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous claim] → [updated claim]
```

Every artifact gets one entry. Every entry gets a stance. Only MODIFIES entries get a
hypothesis update line — CONFIRMS and CONTRADICTS entries record only the stance.

When you finish all entries, write:

```
Hypothesis at S3: [one sentence — the working hypothesis after all stances are applied]
```

**Anti-stagnation check**: Compare S0 to the hypothesis at S3. If they are identical, you
have not stress-tested the hypothesis — the signals either were not read against it, or the
stances were labeled CONFIRMS when a closer reading would reveal modification. Review your
per-signal stances before proceeding to S3.

---

### Step 4 — Write the story

Five beats, all present and distinguishable. Write to
`simulations/{topic}/{topic}-story-{date}.md`.

The S2 content is already produced by Step 3 — do not re-write it. Pick it up from there.

**Beat 1 — What we set out to understand**
The original question from strategy.md, or inferred from the topic. One to three sentences.
State the specific uncertainty, not the general background.

**Beat 2 — What each signal revealed** *(from Step 3)*
The mutation-tracking entries above. These are already written — reproduce them in the
artifact.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two signal entries by artifact name. Draw a
conclusion derivable only from the full entry set, not from any single entry.

The S0→S3 delta is your pattern anchor: the direction of hypothesis mutation across the
signal set is itself a cross-signal finding. Name it: did signals converge on a modification?
Did they pull in different directions, producing a MODIFIES + CONTRADICTS tension? Did the
hypothesis survive intact when you expected it to be challenged?

Where signal stances conflict (CONFIRMS vs CONTRADICTS, or competing MODIFIES updates),
name the tension and adjudicate — state which interpretation the stances more strongly support.

Falsifiability test: *does any single entry contain this conclusion?* If yes, revisit.

**Beat 4 — What remains uncertain**
Specific, scoped gaps. CONTRADICTS stances that were not resolved in Beat 3 may become gaps
if the contradiction is genuine and unresolvable from current signals — but only if they
require a gathering action, not a judgment.

Format each entry:
```
Gap: [what is unknown]
Most exposed finding: [which S2 entry cannot be confirmed without this signal]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Ground the recommendation in the S0→S3 delta and the Beat 3 pattern.
The S3 hypothesis — not the S0 hypothesis — is what the recommendation acts on.
"It depends" without a stated default fails.

---

### Output

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [one sentence]

## What Each Signal Revealed
- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES] Hypothesis update: [before] → [after]
...

**Hypothesis at S3**: [one sentence — evolved from S0]

## What the Signals Say Together
[cross-signal pattern — S0→S3 delta as anchor]

## What Remains Uncertain
[Gap / Most exposed finding / Next signal entries]

## Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [grounding paragraph]
```

**Voice**: Active, opinionated. Take positions. Write as the author of a briefing.

---

## V-02

**Variation axis**: Output format — because-clause adjudication format
**Hypothesis**: C-17 fails when adjudication verdicts are labeled (RESOLVED / UNRESOLVED) but
not defended — the verdict is asserted, not earned. The fix is a format constraint on the
adjudication section: each conflict-pair entry must include a because-clause naming the specific
evidential reason the verdict was reached. "RESOLVED in favor of [signal] because [reason]"
forces the model to commit to an interpretation and expose the reasoning to audit. "UNRESOLVED
because [what gathering step would resolve it]" converts the unresolved state into an actionable
gap rather than a hedge. This tests whether format enforcement on the adjudication section alone
satisfies C-17 without requiring changes to the broader narrative structure.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Write the story

Write to `simulations/{topic}/{topic}-story-{date}.md`. Five beats, all present.

---

**Beat 1 — What we set out to understand**
One to three sentences. The original question from strategy.md, or inferred from the topic.
The specific uncertainty that motivated gathering signals.

**Beat 2 — What each signal revealed**
One key finding per signal, two sentences maximum. The finding most relevant to the original
question. No secondary findings.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two signals. Draw a conclusion derivable only
from the full signal set.

When signals conflict or pull in different directions, name each tension and adjudicate
using the following format:

```
Conflict: `{signal-A}` vs `{signal-B}` — [one sentence naming the dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason — which
         part of the signal, on what dimension, outweighs the alternative]
     OR: UNRESOLVED because [what specific gathering step would resolve it — named as
         {namespace}/{skill}]
```

Every named tension gets a verdict. A tension named and then dropped without a verdict is
editorial suppression, not adjudication. The because-clause is not optional — a verdict
without a because-clause fails this requirement.

Falsifiability test: *does any single signal contain the cross-signal conclusion?* If yes,
the pattern is not yet cross-signal.

**Beat 4 — What remains uncertain**
Specific, scoped gaps. Tensions adjudicated as RESOLVED in Beat 3 are not gaps.
UNRESOLVED verdicts from Beat 3 become gaps — reproduce them here in the gap format.

New gaps (not sourced from Beat 3):
```
Gap: [what is unknown]
Most exposed finding: [which Beat 2 finding cannot be confirmed without this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Ground the recommendation in the Beat 3 pattern and the resolution of any
RESOLVED verdicts. A recommendation that contradicts a RESOLVED verdict requires explicit
reasoning against it.
"Proceed with caution" without naming the caution fails.

---

**Voice**: Active, editorial, opinionated. Write as the author of a briefing. The adjudication
section reads as a formal record — every other section reads as an editorial argument.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

---

## V-03

**Variation axis**: Phrasing register — per-signal stance with rationale (C-15 target)
**Hypothesis**: C-15 fails when per-signal stances are labeled (CONFIRMS / CONTRADICTS) but
the rationale behind the label is absent or implied. A stance without rationale cannot be
audited: the reader cannot tell whether the label reflects a careful reading or a surface
classification. Requiring a rationale sentence — "this stance was assigned because [specific
element of the signal evidence]" — creates an auditable commitment: the model must say which
part of the signal drove the classification. This also serves C-14 (hypothesis threading) as a
side effect: the rationale sentence forces the model to read each signal against the hypothesis,
not just categorize it. This tests whether stance-rationale as a per-signal format requirement
satisfies C-15 independently of C-16 and C-17.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present. Note the working hypothesis the team
entered with — the specific claim being tested.

---

### Write the story

Write to `simulations/{topic}/{topic}-story-{date}.md`. Five beats.

---

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the working hypothesis entering signal
gathering. Name the hypothesis as a falsifiable claim: not "we wanted to understand X" but
"we expected X to be true."

**Beat 2 — What each signal revealed**
For each signal, write one entry:

```
`{artifact-name}` — {one to two sentences: the key finding most relevant to the hypothesis}
Stance: CONFIRMS | MODIFIES | CONTRADICTS
Rationale: [one sentence: the specific element of this signal that drove the stance assignment]
```

Every entry gets a stance and a rationale. The rationale names the part of the signal — the
specific finding, measurement, or observation — that led to the classification. "This signal
generally supports the hypothesis" is not a rationale. "The 94% pass rate in [artifact-name]
confirms the hypothesis because it exceeds the threshold established in [other signal]" is.

If the stance is MODIFIES, the rationale must name what specifically changed in the hypothesis
and why this signal drove the change.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two artifacts by name. Draw a conclusion
derivable only from the full set.

Review the rationale sentences from Beat 2: do they cluster around a dimension? Do competing
rationales name the same signal element from different angles? The rationale set is your
pre-synthesis, not the narrative — extract the pattern from what the rationales collectively
point at.

Where signals conflict, adjudicate: state which stance's rationale the evidence more
strongly supports, and why the winning rationale outweighs the losing one.

**Beat 4 — What remains uncertain**
Specific, scoped gaps. Each gap is a question the current rationale set cannot answer.

```
Gap: [what is unknown]
Most exposed finding: [which Beat 2 entry's rationale depends on this missing signal]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. The recommendation acts on the hypothesis as it stands after Beat 2 — the
evolved hypothesis, not the S0 hypothesis. Ground it in the Beat 3 pattern.
"It depends" without a stated default fails.

---

**Voice**: Active. Each rationale sentence is stated with confidence. A tentative rationale
("this might suggest") fails — commit to what the signal shows.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

---

## V-04

**Variation axis**: Combination — V-01 (hypothesis mutation ledger) + V-02 (because-clause
adjudication)
**Hypothesis**: V-01 targets C-16 via mutation ledger (S0→S3 delta visible). V-02 targets
C-17 via because-clause enforcement on adjudication verdicts. The two axes are orthogonal:
V-01 operates on the per-signal tracking structure (the delta arises from the ledger);
V-02 operates on the conflict resolution vocabulary within S3 (the verdict gets a because-clause).
No structural conflict: the mutation ledger is produced before S3 begins; the because-clause
format applies within S3 when conflicts surface. Together they should satisfy C-16 and C-17
simultaneously. Baseline coverage for C-01 through C-15 is maintained: anti-enumeration from
the ledger-first architecture (signals are processed into stances before synthesis), gap closure
from the namespace/skill format, inertia framing from the S0 declaration, and narrative arc
from the evolution of S0→S3.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

Before writing the story, complete the ledger. Write it to the artifact as the first section.

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with, stated
as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:
```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:
```
Hypothesis at S3: [one sentence — the working hypothesis after all stances are applied]
```

**Anti-stagnation check**: If the hypothesis at S3 is identical to S0, the hypothesis was
not stress-tested. Review per-signal stances — a finding that shifts emphasis, scope, or
condition counts as MODIFIES even if the core claim survives. If the hypothesis genuinely
survived unchanged across all signals, state that explicitly: "S3 = S0: [reason the
hypothesis was not modified by any signal]." An unchanged hypothesis stated with a reason
is defensible. An unchanged hypothesis with no stated reason fails.

Do not begin the story beats until the ledger is complete.

---

### Step 3 — Write the story beats

Write immediately following the ledger.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis.

**Beat 2 — What each signal revealed** *(draws from the ledger)*
The ledger entries above, reproduced in story register. For each entry, one key editorial
sentence beyond the finding — what the finding *means* for the hypothesis.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries. Draw the cross-signal
conclusion.

The S0→S3 delta is a pattern in itself: name the direction of hypothesis mutation across
the full ledger. Did signals systematically widen the scope? Narrow it? Reverse one of its
conditions?

For every tension surfaced (competing stances, or MODIFIES entries pointing in different
directions), apply the following format:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every tension named gets a verdict. Every verdict carries a because-clause.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, the
pattern is not yet cross-signal.

**Beat 4 — What remains uncertain**
Specific, scoped gaps. RESOLVED verdicts are not gaps. UNRESOLVED verdicts become gaps.

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry cannot be confirmed without this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. The recommendation acts on the S3 hypothesis, not S0. Ground it in the
Beat 3 pattern and any RESOLVED verdict directions. Where RESOLVED verdicts point toward
the recommendation, name them.
"Proceed with caution" without naming the caution fails.

---

**Voice**: Active. Opinionated. The ledger reads as a formal record; the story beats read
as an editorial argument built on that record.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
[cross-signal pattern]
[Conflict / Verdict / because-clause entries if tensions surfaced]

### Beat 4 — What remains uncertain
[Gap / Most exposed finding / Next signal entries]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [grounding paragraph referencing S3 hypothesis]
```

---

## V-05

**Variation axis**: Full combination — R3 V-05 base (EVALUATOR/AUTHOR phases + Signal Extract
visible in artifact) upgraded with v6 mechanisms: C-16 mutation ledger, C-17 because-clause
adjudication, C-15 stance rationale
**Hypothesis**: R3 V-05 was the strongest anti-enumeration mechanism available (EVALUATOR phase
eliminates reading-order bias before synthesis begins; Signal Extract in artifact satisfies C-12).
C-16 and C-17 require additions that are orthogonal to that base: the EVALUATOR phase now
produces both the Signal Extract *and* the S0→S3 mutation record (serving C-16), while the
AUTHOR phase's S3 adjudication section now mandates because-clauses on every verdict (serving
C-17). The per-signal stance rationale (C-15) is added to the EVALUATOR's extraction step —
each Signal Extract line gets a stance and a rationale sentence before synthesis begins, which
means the AUTHOR has a defensible record to draw on when adjudicating conflicts. Expected to
satisfy C-12 (Signal Extract visible), C-15 (stance rationale per signal), C-16 (S0→S3 delta
in artifact), and C-17 (because-clause on every adjudication verdict), while maintaining the
R3 baseline for C-01 through C-14.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two phases: **EVALUATOR** then **AUTHOR**. Do not begin AUTHOR until
EVALUATOR is complete and written to the artifact.

---

## EVALUATOR Phase

**Forbidden**: Forming patterns. Drawing cross-signal conclusions. These belong to AUTHOR.

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact.
Also read `simulations/{topic}/strategy.md` if present.

### Step 2 — Declare the working hypothesis (S0)

State the specific claim the team entered with — the expected answer, not the question.
Write it as a falsifiable assertion.

```
Working hypothesis (S0): [one sentence]
```

### Step 3 — Signal Extract with stance rationale

For each artifact, in the order read, write one entry:

```
- `{artifact-name}`: {one sentence — the single most important finding, stated as fact}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {one sentence — the specific element of this signal that drove the stance}
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

Rules:
- One entry per artifact, in gather order
- No thematic grouping, no ranking by apparent significance
- Every entry gets a stance and a rationale — these are EVALUATOR responsibilities
- The rationale names the specific evidence, not the general direction
- Only MODIFIES entries get a hypothesis update line

### Step 4 — Declare hypothesis at S3

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all MODIFIES stances applied]
```

**Anti-stagnation check**: If S3 = S0, state why: "S3 = S0: [reason no signal modified the
hypothesis]." Do not silently leave them identical — the equality must be explained.

**EVALUATOR produces this section in the artifact:**

```markdown
## Signal Extract
*{N} artifacts, in gather order. Working hypothesis (S0): [claim]*

- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {reason}
  [Hypothesis update if MODIFIES]
...

**Hypothesis at S3**: [evolved claim — or S0 with explanation if unchanged]
```

Do not begin AUTHOR until this section is complete.

---

## AUTHOR Phase

**Forbidden**: Re-reading signal artifacts. All findings and stances are in the Signal Extract.
If a finding is not in the Signal Extract, it is not available to this synthesis.

**Input**: The Signal Extract, stances, rationale sentences, and S0→S3 delta above.

Write to `simulations/{topic}/{topic}-story-{date}.md`, Story section following the Signal
Extract.

**Writing discipline**: Prose establishes arc first; inertia markers annotate after.
Inertia markers: `[CONFIRMED]` · `[COMPLICATED]` · `[REVERSES]` · `[UNCERTAIN]`
Removal test: when the Story is complete, re-read it without markers — it must be fully
readable as a briefing. If removing a marker creates a logical gap, rewrite the prose.

---

**S1 — What we set out to understand** `[marker — after prose]`
*Prose first.* The original question and the S0 working hypothesis. One to three sentences.
What specific uncertainty motivated signal gathering?

**S2 — What each signal revealed** `[marker — after prose]`
*Prose first.* Draw from the Signal Extract. One editorial sentence per entry beyond the
finding — what the finding means given its stance and rationale. Two sentences maximum per
signal.
If the marker is `[COMPLICATED]`: the prose must name which Signal Extract entries have
MODIFIES or CONTRADICTS stances and cite their rationale.

**S3 — What the signals say together** `[marker — after prose]`
*Prose first.* The cross-signal pattern. Only visible across the full Signal Extract.
Reference at least two entries by artifact name.

The S0→S3 delta is the spine: name the direction of hypothesis mutation across the stance
set. Did the mutation converge or diverge? Did one signal's MODIFIES reframe what others
were CONFIRMING?

For every tension between stances (CONFIRMS vs CONTRADICTS, or conflicting MODIFIES updates),
apply:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [the rationale from [signal]'s entry
         outweighs [other signal]'s rationale because {specific reason}]
     OR: UNRESOLVED because [what {namespace}/{skill} would provide the missing evidence]
```

Every tension named gets a verdict. Every verdict carries a because-clause. A named tension
without a verdict is editorial suppression.

Falsifiability test: *does any single Signal Extract entry contain this conclusion?* If yes,
revisit.

If the marker is `[COMPLICATED]` or `[REVERSES]`: the prose carries the explanation before
the marker is placed.

**S4 — What remains uncertain** `[UNCERTAIN]`
*Prose first.* Specific, scoped gaps. Debates with RESOLVED verdicts in S3 are not gaps.
UNRESOLVED verdicts from S3 become gaps automatically.

```
Gap: [what is unknown]
Most exposed finding: [which Signal Extract entry's rationale depends on this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**S5 — Recommendation** `[marker — after prose]`
*Prose first.* One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis. The S3 hypothesis — not S0 — is the claim being
recommended against. Ground the recommendation in the S3 pattern and the RESOLVED verdicts.
"It depends" without a stated default fails. "Proceed with caution" without naming the
caution fails.

---

**Voice**: Active. Opinionated. The Signal Extract reads as a formal record; the Story reads
as an editorial argument that a decision-maker would quote from.

---

### Output structure

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## Signal Extract
*{N} artifacts, in gather order. Working hypothesis (S0): [claim]*

- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {reason}
  [Hypothesis update if MODIFIES]
...

**Hypothesis at S3**: [evolved claim]

## Story

### S1 — What we set out to understand
[MARKER] Prose...

### S2 — What each signal revealed
[MARKER] Per-signal prose from Signal Extract stances...

### S3 — What the signals say together
[MARKER] Cross-signal pattern with S0→S3 delta as spine...
[Conflict / Verdict / because-clause entries for each tension]

### S4 — What remains uncertain
[UNCERTAIN] Gap entries (Gap / Most exposed finding / Next signal)...

### S5 — Recommendation
[MARKER] **PROCEED | PAUSE | PIVOT | ABANDON** — [grounding paragraph on S3 hypothesis]
```

Artifact: `simulations/{topic}/{topic}-story-{date}.md`
