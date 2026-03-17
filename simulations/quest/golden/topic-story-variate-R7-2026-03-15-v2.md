---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 7
rubric: v7
---

# Variations — topic-story (Round 7, rubric v7)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v7 rubric adds C-20 (Inter-Beat Artifact Dependency) and C-21 (Escape
Hatch Explicit Prohibition). Two extractable patterns from Round 6:

**Pattern A — Inter-beat artifact dependency (C-20, sourced from R6 V-05 double-satisfy
mechanism):**
R6 V-05 earned both C-13 (RESOLVED/UNRESOLVED named taxonomy) and C-19 (UNRESOLVED path
connecting to gaps) via a single structural element: the UNRESOLVED verdict format was
written identically to the gap entry format, so carrying UNRESOLVED items to Beat 4 was
reproduction rather than authorial selection. C-20 elevates this from an incidental property
to a required architectural constraint: the UNRESOLVED verdict format must structurally
pre-populate the gap format — the output of Beat 3 is the input to Beat 4 for any UNRESOLVED
item. An author who writes an UNRESOLVED verdict simultaneously writes the gap. No prose
instruction ("carry these forward") is sufficient for C-20 — only a format identity between
the verdict and the gap entry closes the selection gap. The distinction from C-19: C-19 tests
whether an UNRESOLVED path exists at all; C-20 tests whether that path is enforced by
artifact identity or merely requested by instruction.

**Pattern B — Escape hatch prohibition (C-21, sourced from R6 C-18 PASS vs PARTIAL split):**
R6 introduced a Conflict Register as the scannable commitment artifact for C-18. Variations
with a register but without an explicit prohibition earned C-18 PARTIAL: their specifications
retained "draw from the pattern discussion" or equivalent language that left prose as a
valid carrier for adjudication commitments. Variations that explicitly stated "do not record
conflict resolutions in prose narrative — every verdict must appear as a named row in the
register" earned C-18 PASS. The structured artifact alone does not close the fallback path;
the prohibition closes it. C-21 formalizes this: whenever a structured commitment artifact
is present, the specification must include explicit language prohibiting prose-absorbed
fallback. The prohibition is not implied by the artifact's existence — it must be stated
as a negative instruction.

Round 7 primary axes: V-01 targets C-20 directly (UNRESOLVED verdict format = gap entry
format; auto-seeding via format identity). V-02 targets C-21 directly (explicit prohibition
paired with the Conflict Register). V-03 targets a role sequence axis: the Conflict Register
is written before synthesis prose (structural position enforces register priority before the
author can absorb decisions into narrative). V-04 combines C-20 + C-21 on the R6 V-05 base
(mutation ledger + EVALUATOR/AUTHOR phases + Conflict Register). V-05 is the full
combination: R6 V-05 base upgraded with C-20 auto-seeding in the EVALUATOR's conflict output
and C-21 explicit prohibition in the AUTHOR's register section.

---

## V-01

**Variation axis**: Output format — UNRESOLVED-to-gap format identity (C-20 target)
**Hypothesis**: C-20 fails when the UNRESOLVED verdict and the gap entry are two separate
format elements connected by a prose instruction. The author reads "UNRESOLVED verdicts
become gaps" and must then re-express the UNRESOLVED item in the gap format — a selection
and translation step. The fix: make the UNRESOLVED verdict *identical in format* to a gap
entry. An author writing `UNRESOLVED — Gap: [...] / Most exposed: [...] / Next signal: [...]`
has simultaneously written the verdict and the gap — there is nothing to carry forward because
the item is already in gap format. Beat 4 reproduces the UNRESOLVED rows verbatim. This tests
whether format identity between verdict and gap (without any other structural change) satisfies
C-20's pass condition independently.

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

**Anti-stagnation check**: If S3 is identical to S0, state why: "S3 = S0:
[reason no signal modified the hypothesis]." Silently identical S0 and S3 fails.

Do not begin the story beats until the ledger is complete.

---

### Step 3 — Conflict Register

Before writing story prose, build the Conflict Register. List every tension between stances
(CONFIRMS vs CONTRADICTS, or MODIFIES entries pulling in different directions).

For each tension, write one entry using this exact format:

```
| Signal-A | Signal-B | Dimension | Verdict | Because |
| `{artifact-A}` | `{artifact-B}` | [what dimension they disagree on] | RESOLVED · `{signal}` \| UNRESOLVED | [specific evidential reason for RESOLVED; or continue below for UNRESOLVED] |
```

For UNRESOLVED entries, the register row expands to the gap format in place:

```
UNRESOLVED — seeded to Beat 4:
  Gap: [what is unknown]
  Most exposed finding: [which ledger entry cannot be confirmed without this]
  Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Format identity rule**: An UNRESOLVED row is a gap entry. Beat 4 reproduces it verbatim
— do not rewrite or re-select. Every UNRESOLVED row in this register appears in Beat 4,
and only rows from this register appear in Beat 4 under the "Conflicts carried forward"
label.

If no tensions exist, write: `Conflict Register: empty — no cross-signal tensions in this
ledger.` Beat 4 may still contain gaps not sourced from conflicts.

---

### Step 4 — Write the story

Five beats, all present and distinguishable.
Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. Name the
specific uncertainty, not the background.

**Beat 2 — What each signal revealed**
Draw from the ledger entries. One editorial sentence per artifact beyond the finding —
what it means for the hypothesis. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries. Draw a conclusion
derivable only from the full entry set.

The S0→S3 delta is your spine — name the direction of hypothesis mutation. Then apply the
Conflict Register: present its RESOLVED verdicts and their because-clauses as part of the
pattern. UNRESOLVED rows are already in Beat 4 — do not re-adjudicate them here.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, revisit.

**Beat 4 — What remains uncertain**
Two categories, kept separate:

*Conflicts carried forward (from Conflict Register):*
Reproduce every UNRESOLVED row from the register verbatim.

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
pattern and at least one RESOLVED verdict from the Conflict Register.
"It depends" without a stated default fails.

---

**Voice**: Active, opinionated. The ledger and Conflict Register read as formal records;
the story beats read as an editorial argument built on those records.

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
| Signal-A | Signal-B | Dimension | Verdict | Because |
|...|...|...|...|...|
[UNRESOLVED rows expanded to gap format]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
[cross-signal pattern drawing from RESOLVED verdicts]

### Beat 4 — What remains uncertain
**Conflicts carried forward:**
[UNRESOLVED rows reproduced verbatim from register]

**Additional gaps:**
[Gap / Most exposed finding / Next signal entries, or "none"]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [grounding paragraph]
```

---

## V-02

**Variation axis**: Phrasing register — explicit prohibition on prose-absorbed commitments
(C-21 target)
**Hypothesis**: C-21 fails when the Conflict Register coexists with a prose path for
adjudication decisions. Even when authors fill the register, narrative prose naturally
absorbs verdict reasoning — "as we saw from the tension between X and Y, the data supports
Z" — creating a dual-carrier problem where the auditor must read both register and prose to
reconstruct commitments. The fix is a single explicit negative instruction, placed
immediately after the register definition: "Every adjudication verdict, resolved or
unresolved, must appear as a named row in the register. Do not record conflict resolutions
in prose narrative. If a verdict is not in the register, it is not an auditable commitment."
This closes the fallback path explicitly. This tests whether the prohibition alone (without
format identity or structural position changes) satisfies C-21 — and whether it also improves
C-18 (commitment auditability) by eliminating the prose carrier.

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

**Anti-stagnation check**: If S3 = S0, state why. An unchanged hypothesis stated with a
reason is defensible. Silently identical S0 and S3 fails.

Do not begin the story beats until the ledger is complete.

---

### Step 3 — Conflict Register

Identify every tension between stances in the ledger (CONFIRMS vs CONTRADICTS, or MODIFIES
entries pointing in different directions). Write each tension as a named row.

**Register:**

```
| Tension | Dimension | Verdict | Because-clause |
| `{artifact-A}` vs `{artifact-B}` | [what they disagree on] | RESOLVED · `{signal}` OR UNRESOLVED | [specific evidential reason, or what {namespace}/{skill} would resolve it] |
```

**Prohibition**: Every adjudication verdict — resolved or unresolved — must appear as a
named row in this register. Do not record conflict resolutions in prose narrative. A verdict
that appears only in the Story section (Beat 3) and not in this register is not an auditable
commitment and will not satisfy the auditability requirement. If a conflict arises during
prose writing that was not anticipated here, return to this register and add the row before
continuing.

If no tensions exist, write: `Conflict Register: empty.`

---

### Step 4 — Write the story

Five beats. Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis.

**Beat 2 — What each signal revealed**
One key editorial sentence per signal beyond the finding. Two sentences maximum.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries. Draw the conclusion
derivable only from the full set.

Reference the Conflict Register for tensions: cite RESOLVED verdicts by their register row
("as registered: [verdict]") and note that UNRESOLVED tensions are carried to Beat 4.
Do not re-adjudicate verdicts already in the register. Do not introduce new verdicts
in prose — if a new tension surfaces while writing this section, add it to the register first.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, revisit.

**Beat 4 — What remains uncertain**
RESOLVED register rows are not gaps. UNRESOLVED register rows become gaps automatically —
reproduce each one here in the standard gap format:

```
Gap: [what is unknown — drawn from the UNRESOLVED row's because-clause]
Most exposed finding: [which ledger entry depends on this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

New gaps not sourced from conflict:
```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis. Ground the recommendation in the Beat 3 pattern
and at least one register row. Where a RESOLVED verdict supports the recommendation, cite
the register row. Where an UNRESOLVED gap constrains it, name the constraint.
"Proceed with caution" without naming the caution fails.

---

**Voice**: Active, editorial. The register reads as a formal record — terse rows, no
commentary. The story beats read as an argument that builds from those rows.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

---

## V-03

**Variation axis**: Role sequence — Adjudication-first (register written before synthesis
prose; structural position enforces C-21 without verbal prohibition)
**Hypothesis**: C-21's prohibition can be satisfied two ways: an explicit verbal instruction
("do not use prose") or a structural sequence that makes prose-absorption architecturally
impossible. If the Conflict Register is completed before any narrative prose is written,
the author has no narrative section to absorb verdicts into at the moment of adjudication.
The prohibition is enforced by position, not rule. This tests whether structural sequencing
alone satisfies C-21 — and whether it also produces C-20 compliance as a side effect (since
filling the register before writing guarantees the UNRESOLVED rows are available before
Beat 4 is drafted, creating natural pre-population). The risk: without an explicit
prohibition, an author can still repeat register decisions in prose retrospectively.
Structural position reduces but may not eliminate the prose-absorption risk.

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

### Step 3 — Conflict Register (complete before writing any prose)

**This step must be completed before Beat 1 prose begins.** The register is the canonical
location of all adjudication decisions. Writing prose before the register is complete
produces an unverifiable artifact.

Scan the ledger for every tension (CONFIRMS vs CONTRADICTS, or competing MODIFIES updates).
For each, write one entry:

```
Row {N}:
  Tension: `{artifact-A}` vs `{artifact-B}` — [dimension of disagreement]
  Verdict: RESOLVED · `{artifact}` — [specific evidential reason, naming the signal element
            that outweighs the alternative]
      OR:  UNRESOLVED — [what specific {namespace}/{skill} would provide the missing evidence]
```

**UNRESOLVED rows**: Write the gap entry inline, as the next line of the same row:

```
  → Gap: [what is unknown]
    Most exposed finding: [which ledger entry depends on this]
    Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

When the register is complete, you have:
1. A full set of RESOLVED verdicts and their evidential reasons
2. A full set of UNRESOLVED rows that are simultaneously gap entries

Now write the story. Do not introduce new verdicts in prose. If a tension surfaces during
story writing that is not in the register, stop, add the row, then continue.

---

### Step 4 — Write the story

Five beats. Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis.

**Beat 2 — What each signal revealed**
One key editorial sentence per signal beyond the finding. Two sentences maximum.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries.

The register is already written — apply it. For each RESOLVED verdict, state what it
establishes about the pattern (cite by row number or artifact name). Do not repeat the
because-clause from the register verbatim — synthesize what the resolution means for the
pattern.

The S0→S3 delta is your spine: name the direction of hypothesis mutation and ground it in
the MODIFIES entries from the ledger.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, revisit.

**Beat 4 — What remains uncertain**
*From the register:* Reproduce every UNRESOLVED row (the gap entry portion) verbatim.
These have already been written — do not rewrite or re-select.

*Additional gaps (not from conflict):*
```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim depends on this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis. Reference the register's verdict distribution —
what proportion of tensions were RESOLVED vs UNRESOLVED, and what the RESOLVED verdicts'
weight of evidence establishes about the claim. The UNRESOLVED count sets the risk floor.
"It depends" without a stated default fails.

---

**Voice**: Active, opinionated. The register is terse and formal — row numbers, named signals,
one-sentence evidential reasons. The story prose is editorial.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

---

## V-04

**Variation axis**: Combination — V-01 (UNRESOLVED-to-gap format identity, C-20) + V-02
(explicit prohibition on prose-absorbed commitments, C-21), on the R6 V-05 base (mutation
ledger + EVALUATOR/AUTHOR phases)
**Hypothesis**: V-01 satisfies C-20 via format identity: the UNRESOLVED verdict row is
written in gap format, making Beat 4 reproduction automatic. V-02 satisfies C-21 via
explicit prohibition: "do not record conflict resolutions in prose narrative." These axes
are orthogonal — format identity operates on the UNRESOLVED row's structure; the prohibition
operates on where verdicts may appear. The combination should satisfy both without
interaction effects. The R6 V-05 base provides the EVALUATOR/AUTHOR phase separation (C-12
Signal Extract visible, C-15 stance rationale, C-16 S0→S3 delta) and the because-clause
adjudication (C-17). Adding a Conflict Register with explicit prohibition to that base
closes C-18 (scannable commitment artifact), C-19 (UNRESOLVED path to gaps), C-20 (auto-
seeding via format identity), and C-21 (explicit fallback prohibition). Expected full-criteria
profile: C-12, C-15, C-16, C-17, C-18, C-19, C-20, C-21, plus the baseline for C-01
through C-14.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two phases: **EVALUATOR** then **AUTHOR**. Do not begin AUTHOR until
EVALUATOR is complete and written to the artifact.

---

## EVALUATOR Phase

**Permitted**: Reading artifacts. Extracting findings. Assigning stances and rationales.
Tracking hypothesis mutation. Identifying tensions.
**Forbidden**: Forming cross-signal patterns. Drawing synthesis conclusions. Adjudicating
conflicts. Writing the Conflict Register verdicts. These belong to AUTHOR.

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
- No thematic grouping or ranking
- Every entry gets a stance and rationale — these are EVALUATOR responsibilities
- The rationale names specific evidence, not general direction
- Only MODIFIES entries get a hypothesis update line

---

### Step 4 — Declare S3 and flag tensions

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all MODIFIES stances applied]
```

**Anti-stagnation check**: If S3 = S0, explain: "S3 = S0: [reason]." Silently identical
S0 and S3 fails.

**Tension flags** (for AUTHOR — do not adjudicate here):

Scan for stance pairings where CONFIRMS and CONTRADICTS appear for the same or related
claims, or where MODIFIES entries pull in different directions. For each, write one flag:

```
Tension flag {N}: `{artifact-A}` [stance] vs `{artifact-B}` [stance] — [dimension in
one phrase]
```

These flags transfer to AUTHOR's Conflict Register step.

---

**EVALUATOR writes this section to the artifact:**

```markdown
## Signal Extract
*{N} artifacts, in gather order. Working hypothesis (S0): [claim]*

- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {reason}
  [Hypothesis update if MODIFIES]
...

**Hypothesis at S3**: [evolved claim — or S0 with explanation if unchanged]

**Tension flags**: [{N} flagged — list them]
```

Do not begin AUTHOR until this section is complete.

---

## AUTHOR Phase

**Permitted**: Pattern derivation. Cross-signal synthesis. Adjudication via Conflict
Register. Recommendation.
**Forbidden**: Re-reading signal artifacts. All findings, stances, and rationales are in
the Signal Extract. If a finding is not in the Signal Extract, it is not available to
this synthesis.

**Input**: Signal Extract, stances, rationale sentences, S3 hypothesis, tension flags.

---

### Step 5 — Build the Conflict Register

Using the tension flags from EVALUATOR, write one entry per flagged tension:

```
| Row | Signal-A | Signal-B | Dimension | Verdict | Because |
| {N} | `{artifact-A}` | `{artifact-B}` | [disagreement] | RESOLVED · `{signal}` OR UNRESOLVED | [evidential reason for RESOLVED; or what {namespace}/{skill} would resolve it] |
```

**UNRESOLVED rows expand to gap format inline:**

```
Row {N}: [tension description]
Verdict: UNRESOLVED — seeded to Beat 4:
  Gap: [what is unknown]
  Most exposed finding: [which Signal Extract entry depends on this]
  Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Prohibition**: Every adjudication verdict — resolved or unresolved — must appear as a
named row in this register. Do not record conflict resolutions in prose narrative. A verdict
that appears in the Story section but not in this register is not an auditable commitment.
If a new tension surfaces during prose writing, return to this register, add the row, then
continue.

---

### Step 6 — Write the story

Write to `simulations/{topic}/{topic}-story-{date}.md`, Story section following the Signal
Extract and Conflict Register.

**Writing discipline**: Prose establishes arc first; inertia markers annotate after.
Markers: `[CONFIRMED]` · `[COMPLICATED]` · `[REVERSES]` · `[UNCERTAIN]`
Removal test: strip all markers. The Story must be fully readable with no logical gaps.

---

**S1 — What we set out to understand** `[TRAJECTORY: assumed]`
*Prose first.* The original question and S0 working hypothesis. One to three sentences.

**S2 — What each signal revealed** `[marker — after prose]`
*Prose first.* Draw from the Signal Extract. One editorial sentence per entry beyond the
finding. Two sentences maximum per signal.

**S3 — What the signals say together** `[marker — after prose]`
*Prose first.* The cross-signal pattern. Reference at least two Signal Extract entries.

The S0→S3 delta is the spine. For each Conflict Register row, state what the RESOLVED
verdict establishes. Do not introduce verdict reasoning here that is not already in the
register row — cite the row and draw the synthesis implication.

Falsifiability test: *does any single Signal Extract entry contain the S3 conclusion?*
If yes, revisit.

**S4 — What remains uncertain** `[UNCERTAIN]`
*From the register:* Reproduce every UNRESOLVED row's gap entry verbatim.

*Additional gaps (not sourced from conflict):*
```
Gap: [what is unknown]
Most exposed finding: [which Signal Extract entry's rationale depends on this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**S5 — Recommendation** `[marker — after prose]`
*Prose first.* One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis. Reference at least one Conflict Register row
and its RESOLVED verdict as causal warrant.
"It depends" without a stated default fails. "Proceed with caution" without naming the
caution fails.

---

**Voice**: Active, opinionated. Signal Extract and Conflict Register read as formal records.
Story reads as an editorial argument auditable against those records.

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
**Tension flags**: [list]

## Conflict Register
| Row | Signal-A | Signal-B | Dimension | Verdict | Because |
|...|...|...|...|...|...|
[UNRESOLVED rows expanded with seeded gap entries]

**Prohibition**: Every verdict lives in this register. No prose-absorbed commitments.

## Story

### S1 — What we set out to understand
[TRAJECTORY: assumed] Prose...

### S2 — What each signal revealed
[MARKER] Per-signal prose...

### S3 — What the signals say together
[MARKER] Cross-signal pattern — cites register rows for verdict synthesis...

### S4 — What remains uncertain
[UNCERTAIN] UNRESOLVED rows reproduced verbatim / Additional gaps...

### S5 — Recommendation
[MARKER] **PROCEED | PAUSE | PIVOT | ABANDON** — [paragraph citing register verdict]
```

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

---

## V-05

**Variation axis**: Full combination — R6 V-05 base (EVALUATOR/AUTHOR phases + Signal
Extract + stance rationale + because-clause adjudication) upgraded with C-20 UNRESOLVED
auto-seeding and C-21 explicit prohibition, integrated as EVALUATOR-level tension output
and AUTHOR-level register constraint
**Hypothesis**: R6 V-05 was the strongest baseline available: EVALUATOR phase produced
Signal Extract with stance rationale (C-15) and S0→S3 mutation (C-16); AUTHOR drew
exclusively from that record for adjudication (C-17) with because-clause verdicts. The
missing elements were C-18 (scannable commitment artifact) and C-19 (UNRESOLVED path to
gaps). R6 V-05 addressed C-19 by requiring UNRESOLVED verdicts to be "carried to Beat 4"
— but the carry was instructional, not structural, which is why it earned C-19 PASS but
not C-20. For Round 7, the EVALUATOR phase gains a Tension Flag output that pre-identifies
conflict pairs for the AUTHOR (removing discovery overhead from adjudication). The AUTHOR
phase gains a Conflict Register with two structural features: (1) UNRESOLVED rows written
in gap format so Beat 4 reproduction is verbatim (C-20), and (2) an explicit prohibition
on prose-absorbed verdicts immediately following the register definition (C-21). Expected
full-criteria profile: C-12, C-15, C-16, C-17, C-18, C-19, C-20, C-21, plus the complete
R6 V-05 baseline for C-01 through C-14.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two phases: **EVALUATOR** then **AUTHOR**. Do not begin AUTHOR until
EVALUATOR is complete and written to the artifact.

---

## EVALUATOR Phase

**Permitted**: Reading artifacts. Extracting findings. Assigning stances and rationales.
Tracking hypothesis mutation. Flagging tensions.
**Forbidden**: Forming cross-signal patterns. Drawing synthesis conclusions. Adjudicating
conflicts. All of these belong to AUTHOR.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Declare working hypothesis (S0)

The specific claim the team entered with — the expected answer, not the question.
Stated as a falsifiable assertion.

```
Working hypothesis (S0): [one sentence]
```

---

### Step 3 — Signal Extract with stance rationale

For each artifact, in the order read:

```
- `{artifact-name}`: {one sentence — the single most important finding, stated as fact}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {one sentence — the specific element that drove the stance classification}
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

Rules:
- One entry per artifact, in gather order
- No thematic grouping, no ranking by significance
- Rationale names specific evidence: the finding, measurement, or observation
- "This signal generally supports the hypothesis" is not a rationale
- Only MODIFIES entries get a hypothesis update line

---

### Step 4 — Declare S3, tension flags

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all MODIFIES stances applied]
```

**Anti-stagnation check**: If S3 = S0, explain why. Silently identical S0 and S3 fails.

**Tension flags** — scan the entry list for every pair where:
- One entry has CONFIRMS and another has CONTRADICTS on a related claim, or
- Two MODIFIES entries update the hypothesis in different directions

For each, write one flag:

```
T{N}: `{artifact-A}` ({stance}) vs `{artifact-B}` ({stance}) — [one phrase: what dimension
they disagree on]
```

These are EVALUATOR outputs that AUTHOR will adjudicate. Do not state verdicts here.

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

**Tension flags**: T1: [...], T2: [...], ...  (or "none" if no cross-stance tensions)
```

Do not begin AUTHOR until the Signal Extract and tension flags are written.

---

## AUTHOR Phase

**Permitted**: Conflict Register construction. Pattern synthesis. Recommendation.
**Forbidden**: Re-reading signal artifacts. All inputs are in the Signal Extract. If
a finding or rationale is not there, it does not exist for this synthesis.

---

### Step 5 — Conflict Register

For each tension flag, write one entry:

```
Row T{N}: `{artifact-A}` vs `{artifact-B}` — [dimension]
Verdict: RESOLVED · `{artifact}` — [specific evidential reason — name the element from
         that entry's rationale that outweighs the alternative's rationale]
```

For UNRESOLVED verdicts, write in auto-seeded gap format:

```
Row T{N}: `{artifact-A}` vs `{artifact-B}` — [dimension]
Verdict: UNRESOLVED — seeded to S4:
  Gap: [what is unknown — the specific question the conflict raises]
  Most exposed finding: [which Signal Extract entry's rationale depends on resolving this]
  Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Prohibition**: Every adjudication verdict — RESOLVED or UNRESOLVED — must appear as a
named row in this register. Do not record conflict resolutions in prose narrative. A verdict
in the story section that does not correspond to a register row is not an auditable
commitment. If a tension surfaces during story writing that was not flagged by EVALUATOR,
stop, add the row to this register, then resume.

If no tension flags were declared, write: `Conflict Register: none (no tensions flagged by
EVALUATOR).`

---

### Step 6 — Write the story

Write to `simulations/{topic}/{topic}-story-{date}.md`, Story section following Signal
Extract and Conflict Register.

**Writing discipline**: Prose first; inertia markers after.
Markers: `[CONFIRMED]` · `[COMPLICATED]` · `[REVERSES]` · `[UNCERTAIN]`
Removal test: remove all markers. Story must be fully readable with no logical gaps.

---

**S1 — What we set out to understand** `[TRAJECTORY: assumed]`
*Prose first.* The original question and the S0 working hypothesis. One to three sentences.
The entering default: what the team expected to confirm, and why that expectation was the
reasonable prior.

**S2 — What each signal revealed** `[marker — after prose]`
*Prose first.* Draw from the Signal Extract. For each entry: the key finding plus one
editorial sentence on what it means given its stance and rationale. Two sentences maximum.

If the marker is `[COMPLICATED]` or `[REVERSES]`: prose must name which Signal Extract
entries have MODIFIES or CONTRADICTS stances and cite their rationale before the marker.

**S3 — What the signals say together** `[marker — after prose]`
*Prose first.* The cross-signal pattern. Reference at least two Signal Extract entries.

The S0→S3 delta is the spine — name the direction of hypothesis mutation.

For each Conflict Register row, apply its verdict to the synthesis argument:
- RESOLVED rows: state what the verdict establishes about the pattern; cite the row (T{N})
- UNRESOLVED rows: note the open question; do not re-adjudicate

Do not introduce new verdict reasoning in this section. All verdicts live in the register.

Falsifiability test: *does any single Signal Extract entry contain the S3 conclusion?*

**S4 — What remains uncertain** `[UNCERTAIN]`
*Prose first.* Two categories:

*From the Conflict Register:* Reproduce every UNRESOLVED row's gap entry verbatim.
These are pre-written — do not select, rewrite, or merge them.

*Additional gaps (not from conflict):*
```
Gap: [what is unknown]
Most exposed finding: [which Signal Extract entry's rationale depends on this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

If no additional gaps, write: `Additional gaps: none.`

**S5 — Recommendation** `[marker — after prose]`
*Prose first.* One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis. Reference at least one Conflict Register row
(by T{N}) and name the verdict's evidential weight as causal warrant for the recommendation.

The UNRESOLVED count from the register sets the risk floor: a recommendation that dismisses
UNRESOLVED tensions without naming them fails.
"It depends" without a stated default fails. "Proceed with caution" without naming the
caution fails.

---

**Voice**: Active. Opinionated. The Signal Extract and Conflict Register read as formal
records — terse, named, auditable. The Story reads as an editorial argument a decision-maker
would quote from.

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
...
Row T{N}: `{artifact-A}` vs `{artifact-B}` — [dimension]
Verdict: UNRESOLVED — seeded to S4:
  Gap: [...]
  Most exposed finding: [...]
  Next signal: [...]

**Prohibition**: Every verdict belongs here. No prose-absorbed commitments.

## Story

### S1 — What we set out to understand
[TRAJECTORY: assumed] Prose...

### S2 — What each signal revealed
[MARKER] Per-signal prose with stance and rationale context...

### S3 — What the signals say together
[MARKER] Cross-signal pattern — S0→S3 delta as spine, register rows applied...

### S4 — What remains uncertain
[UNCERTAIN]
*From register (UNRESOLVED rows reproduced verbatim):*
[...]
*Additional gaps:*
[Gap / Most exposed finding / Next signal — or "none"]

### S5 — Recommendation
[MARKER] **PROCEED | PAUSE | PIVOT | ABANDON** — [paragraph citing register row T{N}
as causal warrant, UNRESOLVED count as risk floor]
```

Artifact: `simulations/{topic}/{topic}-story-{date}.md`
