---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 8
rubric: v7
---

# Variations — topic-story (Round 8, rubric v7)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v7 rubric adds C-20 (Inter-Beat Artifact Dependency) and C-21 (Escape
Hatch Explicit Prohibition). Round 7 established the baseline mechanisms for both:

**R7 findings on C-20 (UNRESOLVED-to-gap format identity):**
R7 V-01 achieved C-20 via format instruction — authors were told to write UNRESOLVED rows
in gap format. R7 V-05 achieved C-20 more reliably via EVALUATOR-phase pre-seeding. The
gap in both: format compliance is still volitional. The author must remember to apply gap
format at the moment of writing the UNRESOLVED verdict. A structurally stronger mechanism
would eliminate format choice: pre-scaffold the gap slot in the register template so that
filling the UNRESOLVED verdict *is* filling the gap entry — no format memory required.

**R7 findings on C-21 (explicit prohibition on prose-absorbed commitments):**
R7 V-02 achieved C-21 via a single-location prohibition immediately after the register
definition. R7 V-03 attempted structural enforcement via sequence (register before prose)
but was identified as vulnerable to retrospective prose-absorption. R7 V-04/V-05 combined
both. The gap in all: the prohibition appears once, at register definition time, before any
prose is written. By the time the author reaches Beat 3 and a verdict arises naturally in
narrative, the prohibition is pages behind. A structurally stronger mechanism brings the
prohibition to the author at the moment of risk — as a guard instruction at the entry to
each prose beat.

**Round 8 primary axes**: V-01 targets C-20 via pre-seeded gap scaffold — register template
contains blank UNRESOLVED slots in gap format; filling the verdict *is* filling the gap.
V-02 targets C-21 via distributed prohibition guards — a brief re-entry directive at the
top of each prose beat, keeping the prohibition live throughout writing. V-03 targets C-21
via lifecycle gate — the register must be explicitly closed (stamped complete) before the
Story section opens; closure is an act, not a passage. V-04 combines V-01 + V-02 on the
R7 V-04 base (mutation ledger + because-clause adjudication + UNRESOLVED path to Beat 4).
V-05 is the full combination: R7 V-05 base (EVALUATOR/AUTHOR phases + Signal Extract
visible in artifact) upgraded with V-01 pre-seeded scaffold in the EVALUATOR's register
output, V-02 distributed prohibition guards in the AUTHOR's beat openings, and V-03
lifecycle gate between EVALUATOR completion and AUTHOR start.

---

## V-01

**Variation axis**: Output format — pre-seeded gap scaffold in register template (C-20 target)
**Hypothesis**: C-20's pass condition requires that UNRESOLVED verdicts ARE gap entries by
format identity. R7 V-01 achieved this via format instruction: "write UNRESOLVED rows in
gap format." But instruction-following remains volitional — the author must choose to use
gap format at the moment of writing each verdict. A pre-seeded scaffold removes the choice
entirely: the Conflict Register template contains, for each row, a blank UNRESOLVED scaffold
pre-labeled with the gap fields. The author fills in the blanks rather than writing in a
format they must recall. The act of marking a verdict UNRESOLVED and filling the scaffold
is identical to writing the gap entry — Beat 4 copies verbatim with no re-expression step.
This tests whether scaffold pre-seeding (without any other structural change) satisfies
C-20's pass condition more reliably than format instruction.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

Before writing the story, complete the ledger.

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two
  sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — the working hypothesis after all stances are applied]
```

**Anti-stagnation check**: If S3 is identical to S0, state why: "S3 = S0: [reason]."
Silently identical S0 and S3 fails.

Do not begin the Conflict Register until the ledger is complete.

---

### Step 3 — Conflict Register

List every tension between stances (CONFIRMS vs CONTRADICTS, or MODIFIES entries pulling
in different directions).

For each tension, write one entry. Use the following scaffold exactly — fill in the blanks,
do not reformat:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension of disagreement] | RESOLVED · `{signal}` because [evidential reason] |
```

For RESOLVED rows: fill the Verdict cell with `RESOLVED · `{signal}` because [specific
evidential reason — name the element of that signal that outweighs the alternative]`.

For UNRESOLVED rows: the Verdict cell is left blank, and the scaffold below the row is
filled instead:

```
Row {N} — UNRESOLVED:
  Gap: [what is unknown — the specific question this conflict raises]
  Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
  Next signal: {namespace}/{skill} — [one sentence: what finding type is expected]
```

**Format identity rule**: The filled UNRESOLVED scaffold IS the gap entry. Beat 4 reproduces
every UNRESOLVED scaffold verbatim — do not rewrite, reselect, or reformulate. Every
UNRESOLVED scaffold in this register appears in Beat 4 under "Conflicts carried forward,"
and no other items appear under that label.

If no tensions exist, write: `Conflict Register: empty.` Beat 4 may still contain
non-conflict gaps.

---

### Step 4 — Write the story

Five beats, all present and distinguishable. Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. Name the
entering claim as a falsifiable assertion, not a goal.

**Beat 2 — What each signal revealed**
Draw from the ledger entries. For each entry: the key finding plus one editorial sentence
on what it means for the hypothesis. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries by artifact name. Draw a
conclusion derivable only from the full entry set, not from any single entry.

Apply the Conflict Register: present RESOLVED verdicts and their because-clauses as part
of the pattern argument. UNRESOLVED scaffold rows are already seated in Beat 4 — do not
re-adjudicate them here, do not restate the conflict in prose. Reference them only by row
number: "Row {N} remains open."

The S0→S3 delta is your spine — name the direction and ground it in the MODIFIES entries.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, the
conclusion is not yet cross-signal.

**Beat 4 — What remains uncertain**
Two categories, kept separate:

*Conflicts carried forward (from Conflict Register):*
Reproduce every UNRESOLVED scaffold verbatim — the three-line block already written.
Do not rewrite or condense.

*Additional gaps (not sourced from conflict):*
```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim depends on this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

If no additional gaps exist, write: `Additional gaps: none.`

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis, not S0. Ground the recommendation in the Beat 3
pattern and at least one RESOLVED verdict from the register.
"It depends" without a stated default fails.

---

**Voice**: Active, opinionated. The ledger and Conflict Register read as formal records —
filled scaffolds, not prose. The story beats read as an editorial argument built on those
records and auditable against them.

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

## Conflict Register
| Row | Signal-A | Signal-B | Dimension | Verdict |
| 1 | `...` | `...` | [...] | RESOLVED · `{signal}` because [...] |
| 2 | `...` | `...` | [...] | [blank — UNRESOLVED below] |
Row 2 — UNRESOLVED:
  Gap: [what is unknown]
  Most exposed finding: [which entry]
  Next signal: {namespace}/{skill} — [expected finding]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
[cross-signal pattern; RESOLVED verdicts applied; UNRESOLVED rows cited by row number only]

### Beat 4 — What remains uncertain
**Conflicts carried forward:**
Row 2 — UNRESOLVED:
  Gap: [verbatim reproduction]
  Most exposed finding: [verbatim]
  Next signal: [verbatim]

**Additional gaps:**
[Gap / Most exposed finding / Next signal, or "none"]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [grounding paragraph]
```

---

## V-02

**Variation axis**: Phrasing register — distributed prohibition guards at each prose beat
(C-21 target)
**Hypothesis**: C-21's pass condition requires an explicit prohibition on prose-absorbed
commitments. R7 V-02 satisfied this with a single prohibition immediately after the register
definition. The vulnerability: the prohibition is distant from the moment of risk. By the
time the author writes Beat 3 and a verdict surfaces naturally in the argument, the
prohibition is in a prior section — easy to overlook or rationalize past. A distributed
mechanism brings the prohibition to the author at the point of prose entry: a one-line
re-entry directive at the opening of each prose section that could absorb verdicts (Beat 3,
Beat 5). The directive is short — "Verdicts belong in the register. Do not introduce new
verdicts here." — and functions as a gate, not a reminder. If a new conflict surfaces
during prose writing, the directive specifies the interrupt protocol: stop, add the row,
then resume. This tests whether distributed placement (without pre-seeded scaffold or
lifecycle gate) is sufficient to satisfy C-21 independently.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two
  sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances are applied]
```

**Anti-stagnation check**: If S3 = S0, state why. Silently identical S0 and S3 fails.

Do not begin the Conflict Register until the ledger is complete.

---

### Step 3 — Conflict Register

Identify every tension between stances. Write each tension as one row:

```
| Row | Signal-A | Signal-B | Dimension | Verdict | Because |
| {N} | `{artifact-A}` | `{artifact-B}` | [what they disagree on] | RESOLVED · `{signal}` OR UNRESOLVED | [evidential reason for RESOLVED; or what signal would resolve UNRESOLVED] |
```

For UNRESOLVED rows, include the gap specification:
```
Row {N}: UNRESOLVED →
  Gap: [what is unknown]
  Most exposed finding: [which ledger entry depends on this]
  Next signal: {namespace}/{skill} — [expected finding type]
```

**Prohibition** (canonical statement): Every adjudication verdict — RESOLVED or UNRESOLVED
— must appear as a named row in this register. Do not record conflict resolutions in prose
narrative. A verdict that appears in the Story section but not in this register is not an
auditable commitment. This prohibition applies to all story beats.

If no tensions exist, write: `Conflict Register: empty.`

---

### Step 4 — Write the story

Five beats. Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis.

**Beat 2 — What each signal revealed**
One editorial sentence per signal beyond the finding. Two sentences maximum per signal.

**Beat 3 — What the signals say together**

> **Verdicts belong in the register. Do not introduce new verdicts here.** If a conflict
> surfaces while writing this section that is not yet in the register, stop — add the row
> to the register now — then return and continue.

The cross-signal pattern. Reference at least two ledger entries. Draw a conclusion
derivable only from the full entry set.

Apply the register: cite RESOLVED rows and their because-clauses as pattern evidence.
UNRESOLVED rows are in Beat 4 — do not re-adjudicate them; reference by row number only.

The S0→S3 delta is your spine. Name the direction and ground it in MODIFIES entries.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, revisit.

**Beat 4 — What remains uncertain**
UNRESOLVED register rows become gaps. Reproduce each UNRESOLVED block here:

```
Gap: [what is unknown — drawn from the UNRESOLVED row]
Most exposed finding: [which ledger entry depends on this]
Next signal: {namespace}/{skill} — [expected finding type]
```

Additional gaps not sourced from conflict:
```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [expected finding type]
```

**Beat 5 — Recommendation**

> **Verdicts belong in the register. Do not introduce new verdict reasoning here.** The
> recommendation may cite register rows by row number to ground its stance, but may not
> introduce new conflict adjudications. If new reasoning surfaces, return to the register.

One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis. Ground the recommendation in the Beat 3 pattern
and at least one RESOLVED register row (cite by row number).
"It depends" without a stated default fails. "Proceed with caution" without naming the
caution fails.

---

**Voice**: Active, editorial. Register rows are terse and formal. Story beats carry the
argument. The re-entry directives are gates, not suggestions — they are enforced by the
interrupt protocol.

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

## Conflict Register
| Row | Signal-A | Signal-B | Dimension | Verdict | Because |
|...|...|...|...|...|...|
[UNRESOLVED rows with gap blocks]

**Prohibition**: All verdicts live here. No prose-absorbed commitments.

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
> Verdicts belong in the register. Do not introduce new verdicts here.
[cross-signal pattern; RESOLVED rows cited by row number; UNRESOLVED cited by row number only]

### Beat 4 — What remains uncertain
[Gap / Most exposed finding / Next signal — UNRESOLVED rows reproduced, then additional gaps]

### Beat 5 — Recommendation
> Verdicts belong in the register. Do not introduce new verdict reasoning here.
**PROCEED | PAUSE | PIVOT | ABANDON** — [paragraph citing register rows as warrant]
```

---

## V-03

**Variation axis**: Lifecycle emphasis — register closure gate between record and prose
(C-21 structural enforcement)
**Hypothesis**: R7 V-03 enforced C-21 by structural sequence — register before prose — but
was identified as vulnerable to retrospective absorption: an author can still write verdict
reasoning in Beat 3 prose even when the register precedes it. A lifecycle closure gate is
architecturally stronger: the register section must be explicitly marked complete before the
Story section opens. The marker is a required artifact line: `[REGISTER CLOSED — {N} rows,
{R} RESOLVED, {U} UNRESOLVED]`. The Story section header instruction reads: "Do not open
Beat 1 until the closure line is present." Closure is an act — the author consciously
terminates the register as a record — not a passage through a sequence of steps. This
enforces two things simultaneously: (1) the author cannot begin prose before the register
is complete (sequence, as in R7 V-03), and (2) the author cannot return to prose-absorbed
adjudication after closure, because the register is now formally closed and any new tension
requires reopening the register before prose can resume. This tests whether lifecycle closure
(without scaffold pre-seeding or distributed prohibition) satisfies C-21 independently, and
whether closure also produces C-20 compliance as a side effect (since UNRESOLVED rows must
be present at closure for the count to be accurate).

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

```
Hypothesis at S3: [one sentence]
```

**Anti-stagnation check**: If S3 = S0, state why.

---

### Step 3 — Conflict Register (must be closed before Story opens)

Scan the ledger for every tension (CONFIRMS vs CONTRADICTS, or competing MODIFIES updates).
Write each as one row:

```
Row {N}: `{artifact-A}` vs `{artifact-B}` — [dimension]
  Verdict: RESOLVED · `{artifact}` — [specific evidential reason naming the element
           from that signal that outweighs the alternative]
```

For UNRESOLVED rows:

```
Row {N}: `{artifact-A}` vs `{artifact-B}` — [dimension]
  Verdict: UNRESOLVED
  Gap: [what is unknown]
  Most exposed finding: [which ledger entry cannot be confirmed without this]
  Next signal: {namespace}/{skill} — [expected finding type]
```

When all rows are written, write the following closure line as the final line of the
register section:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

**Do not open Beat 1 until this closure line is present.**

If a new conflict surfaces during story writing: stop. Reopen the register — write the new
row above the closure line — update the closure line counts — then resume the beat. Prose
written after a conflict that is not yet registered is not an auditable artifact.

If no tensions exist, write: `Conflict Register: empty.` Then write the closure line:
`[REGISTER CLOSED — 0 rows, 0 RESOLVED, 0 UNRESOLVED]`

---

### Step 4 — Write the story

Open only after the closure line is confirmed present. Write to
`simulations/{topic}/{topic}-story-{date}.md`.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis.

**Beat 2 — What each signal revealed**
One key editorial sentence per signal beyond the finding. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries.

The register is closed — apply it. RESOLVED rows are pattern evidence; cite their because-
clauses as part of the argument. Do not introduce verdict reasoning for any tension not
already in the closed register. UNRESOLVED rows are in Beat 4; reference by row number only.

The S0→S3 delta is the spine. Name the direction and ground it in MODIFIES entries.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, revisit.

**Beat 4 — What remains uncertain**
*From closed register (UNRESOLVED rows):*
Reproduce every UNRESOLVED row's gap block verbatim — Gap, Most exposed finding, Next signal.

*Additional gaps (not from conflict):*
```
Gap: [what is unknown]
Most exposed finding: [which ledger entry depends on this]
Next signal: {namespace}/{skill} — [expected finding type]
```

If no additional gaps, write: `Additional gaps: none.`

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis. Ground in the Beat 3 pattern and at least one
RESOLVED row from the closed register. The UNRESOLVED count (from the closure line) sets
the risk floor — name it.
"It depends" without a stated default fails.

---

**Voice**: Active, opinionated. The closure line is a formal artifact boundary — it is
authoritative and checkable. Story beats carry the editorial argument against the closed
record.

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

## Conflict Register
Row 1: `{artifact-A}` vs `{artifact-B}` — [dimension]
  Verdict: RESOLVED · `{signal}` — [evidential reason]
Row 2: `{artifact-C}` vs `{artifact-D}` — [dimension]
  Verdict: UNRESOLVED
  Gap: [what is unknown]
  Most exposed finding: [which entry]
  Next signal: [namespace/skill — expected finding]
[REGISTER CLOSED — 2 rows, 1 RESOLVED, 1 UNRESOLVED]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
[pattern — RESOLVED rows applied; UNRESOLVED cited by row number only]

### Beat 4 — What remains uncertain
*From closed register:*
Gap: [verbatim from Row 2]
Most exposed finding: [verbatim]
Next signal: [verbatim]

*Additional gaps:*
[entries or "none"]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [paragraph; UNRESOLVED count from closure line
as risk floor; at least one RESOLVED row as warrant]
```

---

## V-04

**Variation axis**: Combination — V-01 (pre-seeded gap scaffold, C-20) + V-02 (distributed
prohibition guards, C-21) on the R7 V-04 base (mutation ledger + because-clause adjudication
+ UNRESOLVED path to Beat 4)
**Hypothesis**: V-01 and V-02 are orthogonal: scaffold pre-seeding operates on the format
of UNRESOLVED rows in the register (C-20), while distributed prohibition guards operate on
where verdict reasoning may appear in prose (C-21). Neither changes the core ledger structure
or the because-clause format that made R7 V-04 the round's strongest performer on C-17.
Together, they should close both C-20 and C-21 without structural conflict, and without
requiring the EVALUATOR/AUTHOR split of V-05. The R7 V-04 base already satisfies C-12
(absence — no Signal Extract section), C-15 (stance rationale via hypothesis update
requirement), C-16 (S0→S3 delta visible in ledger), and C-17 (because-clause on every
verdict). V-01 adds C-20 by eliminating format choice from UNRESOLVED row writing. V-02
adds C-21 by distributing the prohibition to Beat 3 and Beat 5 entry points. Expected
profile: C-17 maintained, C-20 via scaffold, C-21 via distributed guards, plus the R7 V-04
baseline for C-01 through C-14.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

Before writing the story, complete the ledger. Write it as the first section of the artifact.

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two
  sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances are applied]
```

**Anti-stagnation check**: If S3 is identical to S0, state why. Silently identical S0 and
S3 fails.

Do not begin the Conflict Register until the ledger is complete.

---

### Step 3 — Conflict Register

List every tension between stances. For each tension, write one entry.

For RESOLVED rows:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | RESOLVED · `{signal}` because [specific evidential reason — name the element from that signal that outweighs the alternative] |
```

For UNRESOLVED rows, fill the pre-seeded scaffold below the table row instead of leaving
the Verdict cell incomplete:

```
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | — see UNRESOLVED scaffold below — |

Row {N} — UNRESOLVED scaffold:
  Gap: [what is unknown — the specific question this conflict raises]
  Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
  Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Format identity rule**: The filled UNRESOLVED scaffold IS the gap entry. Beat 4 reproduces
every UNRESOLVED scaffold verbatim — the three-line block exactly as written here.

**Prohibition** (canonical, applies to all story beats): Every adjudication verdict —
RESOLVED or UNRESOLVED — must appear as a named row in this register. Do not record conflict
resolutions in prose narrative. This prohibition applies to Beat 3 and Beat 5. If a new
conflict surfaces during prose writing, stop — add the row to this register now — then
resume.

If no tensions exist, write: `Conflict Register: empty.`

---

### Step 4 — Write the story beats

Write immediately following the register section.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. Name the
entering claim as a falsifiable assertion, not a goal.

**Beat 2 — What each signal revealed**
The ledger entries in story register. For each entry: one editorial sentence beyond the
finding — what the finding means for the hypothesis. Two sentences maximum per signal.

**Beat 3 — What the signals say together**

> **Register only. Do not introduce new verdicts here.** If a conflict surfaces during
> writing, stop — add the row to the register above — then return and continue.

The cross-signal pattern. Reference at least two ledger entries. Draw a conclusion
derivable only from the full entry set.

Apply the register: present RESOLVED rows and their because-clauses as pattern evidence.
UNRESOLVED rows are already seated in Beat 4 — reference them only by row number: "Row {N}
remains open."

The S0→S3 delta is the spine — name the direction and ground it in MODIFIES entries.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, revisit.

**Beat 4 — What remains uncertain**
Two categories, kept separate:

*Conflicts carried forward (from Conflict Register):*
Reproduce every UNRESOLVED scaffold verbatim — the three-line block exactly as written.
Do not rewrite or condense.

*Additional gaps (not sourced from conflict):*
```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [expected finding type]
```

If no additional gaps, write: `Additional gaps: none.`

**Beat 5 — Recommendation**

> **Register only. Do not introduce new verdict reasoning here.** Cite register rows by
> row number as causal warrant. If new reasoning is required, return to the register.

One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis, not S0. Ground the recommendation in the Beat 3
pattern and at least one RESOLVED register row (cite by row number).
"It depends" without a stated default fails. "Proceed with caution" without naming the
caution fails.

---

**Voice**: Active, opinionated. The ledger and Conflict Register read as formal records.
The story beats carry the editorial argument; the re-entry directives enforce the record
boundary without interrupting the argument's flow.

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

## Conflict Register
| Row | Signal-A | Signal-B | Dimension | Verdict |
| 1 | `...` | `...` | [...] | RESOLVED · `{signal}` because [...] |
| 2 | `...` | `...` | [...] | — see UNRESOLVED scaffold below — |

Row 2 — UNRESOLVED scaffold:
  Gap: [what is unknown]
  Most exposed finding: [which entry]
  Next signal: {namespace}/{skill} — [expected finding]

**Prohibition**: All verdicts live here. No prose-absorbed commitments.

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
> Register only. Do not introduce new verdicts here.
[cross-signal pattern; RESOLVED rows applied; UNRESOLVED cited by row number only]

### Beat 4 — What remains uncertain
**Conflicts carried forward:**
Row 2 — UNRESOLVED scaffold:
  Gap: [verbatim]
  Most exposed finding: [verbatim]
  Next signal: [verbatim]

**Additional gaps:**
[entries or "none"]

### Beat 5 — Recommendation
> Register only. Do not introduce new verdict reasoning here.
**PROCEED | PAUSE | PIVOT | ABANDON** — [paragraph; at least one register row cited as warrant]
```

---

## V-05

**Variation axis**: Full combination — R7 V-05 base (EVALUATOR/AUTHOR phases + Signal
Extract visible in artifact + stance rationale) upgraded with V-01 pre-seeded scaffold
(C-20), V-02 distributed prohibition guards (C-21), and V-03 lifecycle closure gate
**Hypothesis**: R7 V-05 achieved the strongest structural separation of evidence-extraction
from synthesis: the EVALUATOR phase produces a Signal Extract with stance and rationale
before any synthesis prose begins; the AUTHOR draws exclusively from that record. The
missing C-20 and C-21 mechanisms are addable to this base with minimal structural disruption.
C-20 (pre-seeded scaffold): the EVALUATOR's Conflict Register output uses blank UNRESOLVED
scaffolds, so filling the scaffold during EVALUATOR-phase adjudication simultaneously
produces the gap entry — no AUTHOR-phase format recall required. C-21 (distributed guards):
the AUTHOR phase begins each prose beat with a one-line re-entry directive; the prohibition
is live at the moment of writing, not only at register-definition time. V-03 lifecycle gate:
between EVALUATOR completion and AUTHOR start, a closure line marks the register as a
finalized record — the AUTHOR works from a closed artifact, not an open workspace.
Expected full-criteria profile: C-12 (Signal Extract visible in artifact), C-15 (stance
rationale per signal), C-16 (S0→S3 delta visible), C-17 (because-clause on every verdict),
C-20 (UNRESOLVED scaffold = gap entry; verbatim reproduction in S4), C-21 (distributed
prohibition guards at S3 and S5 entry), closure gate enforces register finality; plus the
R7 V-05 baseline for C-01 through C-14.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two phases: **EVALUATOR** then **AUTHOR**. Do not begin AUTHOR until
EVALUATOR is complete and the register closure line is written.

---

## EVALUATOR Phase

**Permitted**: Reading artifacts. Extracting findings. Assigning stances and rationales.
Tracking hypothesis mutation. Identifying tensions. Building the Conflict Register.
Writing the closure line.
**Forbidden**: Forming cross-signal patterns. Drawing synthesis conclusions. Writing story
beats. All of these belong to AUTHOR.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Declare working hypothesis (S0)

State the specific claim the team entered with — the expected answer, not the question.
Write it as a falsifiable assertion.

```
Working hypothesis (S0): [one sentence]
```

---

### Step 3 — Signal Extract with stance rationale

For each artifact, in the order read:

```
- `{artifact-name}`: {one sentence — the single most important finding, stated as fact}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {one sentence — the specific element of this signal that drove the stance}
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

Rules:
- One entry per artifact, in gather order
- No thematic grouping, no ranking by significance
- Every entry gets a stance and rationale — EVALUATOR responsibilities
- Rationale names specific evidence: a finding, measurement, or observation. "This signal
  generally supports the hypothesis" is not a rationale
- Only MODIFIES entries get a hypothesis update line

---

### Step 4 — Declare S3 and tension flags

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all MODIFIES stances applied]
```

**Anti-stagnation check**: If S3 = S0, explain: "S3 = S0: [reason no MODIFIES stance was
warranted]." Silently identical S0 and S3 fails.

**Tension flags** — scan for every pair where:
- One entry has CONFIRMS and another has CONTRADICTS on a related claim, or
- Two MODIFIES entries update the hypothesis in different directions

For each, write one flag:

```
T{N}: `{artifact-A}` ({stance}) vs `{artifact-B}` ({stance}) — [one phrase: dimension]
```

These are EVALUATOR outputs. Do not state verdicts here.

---

### Step 5 — Conflict Register (complete before closure)

For each tension flag, write one entry. Use the scaffold:

**RESOLVED verdict:**
```
Row T{N}: `{artifact-A}` vs `{artifact-B}` — [dimension]
  Verdict: RESOLVED · `{artifact}` — [specific evidential reason — name the element from
           that entry's rationale that outweighs the alternative's rationale]
```

**UNRESOLVED verdict — fill the pre-seeded scaffold:**
```
Row T{N}: `{artifact-A}` vs `{artifact-B}` — [dimension]
  Verdict: UNRESOLVED
  Gap: [what is unknown — the specific question the conflict raises]
  Most exposed finding: [which Signal Extract entry's rationale depends on resolving this]
  Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Format identity rule**: The filled UNRESOLVED scaffold IS the gap entry. S4 reproduces
every UNRESOLVED scaffold verbatim. Do not rewrite, reselect, or reformulate in S4.

When all tension flags are addressed, write the closure line:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

Do not begin AUTHOR until this closure line is written.

If no tensions were flagged, write: `Conflict Register: none (no tensions flagged).`
Then write the closure line: `[REGISTER CLOSED — 0 rows, 0 RESOLVED, 0 UNRESOLVED]`

---

**EVALUATOR writes this to the artifact:**

```markdown
## Signal Extract
*{N} artifacts, in gather order. Working hypothesis (S0): [claim]*

- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {reason}
  [Hypothesis update if MODIFIES]
...

**Hypothesis at S3**: [evolved claim — or S0 with explanation if unchanged]

**Tension flags**: T1: [...], T2: [...], ...  (or "none")

## Conflict Register
Row T1: `{artifact-A}` vs `{artifact-B}` — [dimension]
  Verdict: RESOLVED · `{artifact}` — [evidential reason]
Row T2: `{artifact-C}` vs `{artifact-D}` — [dimension]
  Verdict: UNRESOLVED
  Gap: [what is unknown]
  Most exposed finding: [which entry]
  Next signal: {namespace}/{skill} — [expected finding]
[REGISTER CLOSED — 2 rows, 1 RESOLVED, 1 UNRESOLVED]
```

Do not begin AUTHOR until the closure line is written.

---

## AUTHOR Phase

**Permitted**: Pattern synthesis. Recommendation. Writing story beats.
**Forbidden**: Re-reading signal artifacts. Re-opening the register. All findings, stances,
rationales, verdicts, and gap scaffolds are in the Signal Extract and Conflict Register.
If a finding is not in the Signal Extract, it is not available. If a verdict is not in
the closed register, it does not exist for this synthesis.

**Input**: Signal Extract (stances, rationale sentences, S3 hypothesis), and the closed
Conflict Register (RESOLVED rows, UNRESOLVED scaffolds, row count from closure line).

Write to `simulations/{topic}/{topic}-story-{date}.md`, Story section following Signal
Extract and Conflict Register.

**Writing discipline**: Prose establishes the arc; trajectory markers annotate after.
Markers: `[CONFIRMED]` · `[COMPLICATED]` · `[REVERSES]` · `[UNCERTAIN]`
Removal test: strip all markers. Story must be fully readable as a briefing with no
logical gaps.

---

**S1 — What we set out to understand** `[TRAJECTORY: assumed]`
*Prose first.* The original question and the S0 working hypothesis. The entering default:
what the team expected to confirm, and why that expectation was the reasonable prior.
One to three sentences.

**S2 — What each signal revealed** `[marker — after prose]`
*Prose first.* Draw from the Signal Extract. One editorial sentence per entry beyond the
finding — what the finding means given its stance and rationale. Two sentences maximum.

The marker reflects net stance pressure after all S2 entries: `[CONFIRMED]` if
predominantly CONFIRMS, `[COMPLICATED]` if CONFIRMS with notable MODIFIES, `[REVERSES]`
if CONTRADICTS or directionally reversing MODIFIES dominate.

**S3 — What the signals say together** `[marker — after prose]`

> **Register is closed. Do not introduce new verdicts here.** If a conflict surfaces that
> is not in the closed register, return to EVALUATOR — add the row, update the closure
> line — then resume. Prose that adjudicates an unregistered tension is not auditable.

*Prose first.* The cross-signal pattern. Reference at least two Signal Extract entries.

For each RESOLVED register row, state what the verdict establishes about the pattern —
cite by row label (T{N}). Do not repeat the because-clause verbatim; synthesize the
verdict's implication for the pattern. UNRESOLVED rows are in S4 — cite by row label only.

The S0→S3 delta is the spine. Name the direction and ground it in MODIFIES entries from
the Signal Extract.

Falsifiability test: *does any single Signal Extract entry contain the S3 conclusion?*
If yes, revisit.

**S4 — What remains uncertain** `[UNCERTAIN]`
*Prose first.* Two categories:

*From the closed register (UNRESOLVED scaffolds):*
Reproduce every UNRESOLVED scaffold verbatim — the four-line block exactly as written by
EVALUATOR. Do not rewrite or condense.

*Additional gaps (not from conflict):*
```
Gap: [what is unknown]
Most exposed finding: [which Signal Extract entry's rationale depends on this]
Next signal: {namespace}/{skill} — [expected finding type]
```

If no additional gaps, write: `Additional gaps: none.`

**S5 — Recommendation** `[marker — after prose]`

> **Register is closed. Do not introduce new verdict reasoning here.** Cite register rows
> by label (T{N}) as causal warrant. The UNRESOLVED count from the closure line is the
> risk floor — name it. If new reasoning is required, return to EVALUATOR.

*Prose first.* One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis. Name the vector: what did the signals do to the
entering claim? Ground the recommendation in at least one RESOLVED register row (cite T{N}).
Name the UNRESOLVED count as the risk floor.
"It depends" without a stated default fails. "Proceed with caution" without naming the
caution fails.

---

**Voice**: Active. Opinionated. Signal Extract and Conflict Register are formal, closed
records — terse, auditable, finalized before prose begins. Story beats carry the editorial
argument a decision-maker would quote from. Re-entry directives are gates, not style.

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
**Tension flags**: T1: [...], T2: [...]

## Conflict Register
Row T1: `{artifact-A}` vs `{artifact-B}` — [dimension]
  Verdict: RESOLVED · `{artifact}` — [evidential reason]
Row T2: `{artifact-C}` vs `{artifact-D}` — [dimension]
  Verdict: UNRESOLVED
  Gap: [what is unknown]
  Most exposed finding: [which entry]
  Next signal: {namespace}/{skill} — [expected finding]
[REGISTER CLOSED — 2 rows, 1 RESOLVED, 1 UNRESOLVED]

## Story

### S1 — What we set out to understand
[TRAJECTORY: assumed] Prose...

### S2 — What each signal revealed
[MARKER] Per-signal prose from Signal Extract stances and rationales...

### S3 — What the signals say together
> Register is closed. Do not introduce new verdicts here.
[MARKER] Cross-signal pattern — T1 applied, T2 cited by label only...

### S4 — What remains uncertain
[UNCERTAIN]
*From closed register:*
Row T2 — UNRESOLVED:
  Gap: [verbatim]
  Most exposed finding: [verbatim]
  Next signal: [verbatim]

*Additional gaps:*
[Gap / Most exposed finding / Next signal — or "none"]

### S5 — Recommendation
> Register is closed. Do not introduce new verdict reasoning here.
[MARKER] **PROCEED | PAUSE | PIVOT | ABANDON** — [paragraph; T{N} as warrant;
UNRESOLVED count from closure line as risk floor]
```

Artifact: `simulations/{topic}/{topic}-story-{date}.md`
