---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 9
rubric: v8
new_criteria: C-24, C-25
---

# Variations — topic-story (Round 9, rubric v8 / C-24+C-25 track)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v8 rubric adds C-24 (Role execution order as pre-composition gate) and
C-25 (Terminal verification checklist). N_aspirational rises from 16 → 18. Two extractable
patterns from the prior track's V-01 architecture that produced C-24 and C-25:

**Prior-track finding on C-24 (Role execution order — C-18 gap):**
Every prior variation established structural pre-composition order via separators, phase
labels, and named markers (OPEN/CLOSED, Part 1/Part 2, phase stamps). These satisfy C-18
(structural placement makes pre-composition verifiable). The gap that produced C-24: structural
separators can be respected after the fact. An author who writes Beat 3, then goes back and
fills in the pattern block, has violated the pre-composition principle — but no structural
separator is violated, because the separator only requires the block to appear *before* the
beat in the document. C-24 closes this gap by requiring named roles with an explicit one-way
transition: a designated analytic role (ANALYST) must complete all blocks before a designated
authoring role (AUTHOR) may begin any beat. The one-way marker is a named moment in the
document — `[ANALYST COMPLETE — AUTHOR MAY BEGIN]` or equivalent — that is structurally
impossible to produce retroactively without the violation being visible. If ANALYST work
appears after a beat, it's a named role boundary crossing, not just a placement issue.

**Prior-track finding on C-25 (Terminal verification checklist — compliance assumption gap):**
Every prior variation contained structural requirements that the author was instructed to
follow: pre-story gate, prohibition guards, non-substitution rules, role boundaries. The
gap: compliance was assumed from the presence of compliant sections. No variation required
the author to explicitly confirm each requirement at the end of the output. An author who
believes they've written the pattern block, named the roles, and completed the register can
submit without deliberately checking. C-25 closes this gap by requiring a terminal section
containing a binary declarative checklist — one item per structural requirement — that must
be filled in (not just present) before the artifact is submitted. The checklist converts
implicit compliance confidence into explicit affirmation: for each criterion, the author must
mark it pass or fail and attach the certifying evidence. The checklist is a gate — the
artifact is not complete until every item is checked.

**Round 9 primary axes**: V-01 targets C-24 via named ANALYST/AUTHOR roles with an explicit
one-way completion marker — the first variation to introduce named roles as the enforcement
mechanism (prior variations used phases and structural separators). V-02 targets C-25 via a
terminal "Submission Audit" section with per-criterion binary items — the first variation to
require explicit end-of-output affirmation. V-03 targets C-24 via named execution phases
(EVIDENCE / CONFLICT / PATTERN / STORY) with completion stamps and forward-only entry gates,
testing whether named phases satisfy C-24's structural verifiability requirement without
requiring role vocabulary. V-04 combines V-01 (role gate) and V-02 (terminal checklist) on
the prior-track V-01 base (OPEN/CLOSED lifecycle). V-05 is the full combination on the
strongest prior-track base (domain falsifier + reopen protocol + mutation ledger) upgraded
with V-01 role gate and V-02 terminal checklist.

---

## V-01

**Variation axis**: Role sequence — named ANALYST/AUTHOR roles with explicit one-way
completion marker (C-24 primary)
**Hypothesis**: C-18 is satisfied when a structural separator (Part 1/Part 2, phase stamp)
confirms pre-composition order. C-24 requires more: the analytic role must be *named*, the
transition must be one-directional, and violations must be structurally self-revealing. A
separator only confirms document order; it cannot confirm execution order. An author who
writes a beat first, then fills in the analytic block above it, satisfies a separator while
violating C-24's intent. Named roles close this gap: the ANALYST role produces all analytic
blocks (hypothesis ledger, conflict register, pattern block) and terminates with a named
completion marker. The AUTHOR role is not permitted to write any beat until the ANALYST
COMPLETE marker is present. This makes retroactive block-writing a visible role boundary
crossing — the AUTHOR has begun while the ANALYST marker is absent — rather than a silently
permitted document reordering. This tests whether named-role vocabulary plus a one-way
marker satisfies C-24 as a single-axis change over the structural-separator baseline.

---

You are running `/topic:story` for a topic. The topic name is provided.

**Role architecture**: This prompt defines two sequential roles — ANALYST and AUTHOR — that
must execute in order. The ANALYST completes all analytic work. The AUTHOR writes all
narrative. The roles do not overlap and cannot execute in reverse: no beat may begin before
the ANALYST COMPLETE marker is present. Producing analytic output after a beat is a role
boundary violation.

---

### ANALYST ROLE — begins now

The ANALYST performs three tasks in order. The ANALYST does not write story beats. Beat
vocabulary (Beat 1 through Beat 5) is prohibited during the ANALYST phase.

---

#### ANALYST Task 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found. Also read
`simulations/{topic}/strategy.md` if present.

---

#### ANALYST Task 2 — Hypothesis Mutation Ledger

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion — a claim that can be wrong, not a goal or question]

For each signal artifact, in order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two
  sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances applied]
```

**Anti-stagnation check**: If S3 is identical to S0, name the specific reason. Silently
identical S0 and S3 fails.

---

#### ANALYST Task 3 — Conflict Register

Write the following as the first line of the register:

```
[REGISTER: OPEN — accepting entries]
```

List every tension between stances (CONFIRMS vs CONTRADICTS, or competing MODIFIES
entries pulling in opposite directions).

For RESOLVED rows:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension of disagreement] | RESOLVED · `{signal}` because [specific evidential reason — name the element from that signal that outweighs the alternative] |
```

For UNRESOLVED rows:

```
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | — see UNRESOLVED scaffold — |

Row {N} — UNRESOLVED:
  Gap: [what is unknown — the specific question this conflict raises]
  Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
  Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Prohibition** (carries into all beats): Every conflict adjudication must appear as a
named row in this register. Conflict resolutions must not be recorded in prose narrative.

If no tensions exist, write: `Conflict Register: empty.`

When all entries are written, close with:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

Verify counts before writing. N = total rows; R + U = N.

---

#### ANALYST COMPLETE — AUTHOR MAY BEGIN

Write the following line as the final act of the ANALYST phase:

```
[ANALYST COMPLETE — AUTHOR MAY BEGIN]
```

This marker certifies that the hypothesis ledger and conflict register are finished. The
AUTHOR role begins only after this line is present. If this line is absent, no beat may be
written.

---

### AUTHOR ROLE — begins after [ANALYST COMPLETE] marker

The AUTHOR writes story beats only. The AUTHOR does not produce analytic blocks. If a new
conflict is discovered during beat writing, the AUTHOR must HALT, return the task to the
ANALYST role, add the conflict to the register, re-close it, append
`[ANALYST RE-COMPLETE — AUTHOR MAY RESUME]`, then resume the halted beat.

Write to `simulations/{topic}/{topic}-story-{date}.md`.

---

**Beat 1 — What we set out to understand**
One to three sentences. State the original question and the S0 working hypothesis. S0 must
appear as a falsifiable assertion, not a goal.

**Beat 2 — What each signal revealed**
Draw from ledger entries. For each: the key finding plus one editorial sentence on what it
means for the hypothesis. Two sentences maximum per signal.

**Beat 3 — What the signals say together**

Complete the pattern block before writing any prose in Beat 3:

```
[PATTERN BLOCK]
Pattern claim: [one declarative sentence — names the phenomenon across signals]
Cross-signal basis: [names the two or more artifacts whose stances, taken together,
  produce this claim — a claim derivable from any single artifact fails]
S0→S3 delta direction: [one sentence — how the hypothesis moved; not "confirmed", but
  the specific direction of movement]
Falsifiability test: does any single ledger entry contain this conclusion? If yes: revise.
[/PATTERN BLOCK]
```

After the pattern block, write the Beat 3 argument. Ground the pattern in the S0→S3 delta
and at least two RESOLVED register rows (cite by row number, include the because-clause).
UNRESOLVED rows are in Beat 4 — reference by row number only: "Row {N} remains open."

**Beat 4 — What remains uncertain**
*Conflicts carried forward:*
Reproduce every UNRESOLVED scaffold verbatim — three-line block exactly as written in the
register. Do not rewrite, condense, or reselect.

*Additional gaps (not sourced from conflict):*

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim depends on this]
Next signal: {namespace}/{skill} — [expected finding type]
```

If no additional gaps: `Additional gaps: none.`

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on S3, not S0. Ground in the Beat 3 pattern and at least one RESOLVED
row (cite by row number). Name the UNRESOLVED count from the closure stamp as the risk
floor. "It depends" without a stated default fails.

---

**Voice**: Active, opinionated. The role boundary is structural — not stylistic. The
[ANALYST COMPLETE] marker is the verification that the author earned the right to write.
The story beats carry the editorial argument against a closed analytic record.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## ANALYST PHASE

**Working hypothesis (S0)**: [claim]

### Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]
**Anti-stagnation check**: [note if S3 ≠ S0, or reason if S3 = S0]

### Conflict Register
[REGISTER: OPEN — accepting entries]

| Row | Signal-A | Signal-B | Dimension | Verdict |
| 1 | `...` | `...` | [...] | RESOLVED · `{signal}` because [...] |
| 2 | `...` | `...` | [...] | — see UNRESOLVED scaffold — |

Row 2 — UNRESOLVED:
  Gap: [what is unknown]
  Most exposed finding: [which entry]
  Next signal: {namespace}/{skill} — [expected finding]

[REGISTER CLOSED — 2 rows, 1 RESOLVED, 1 UNRESOLVED]

---
[ANALYST COMPLETE — AUTHOR MAY BEGIN]
---

## AUTHOR PHASE

### Beat 1 — What we set out to understand
[S0 as falsifiable assertion; original question]

### Beat 2 — What each signal revealed
[One finding + one editorial sentence per signal]

### Beat 3 — What the signals say together

[PATTERN BLOCK]
Pattern claim: [one declarative sentence]
Cross-signal basis: [`artifact-A`, `artifact-B` — what they show together]
S0→S3 delta direction: [direction of hypothesis movement]
Falsifiability test: [conclusion not derivable from any single entry — confirmed / revisit]
[/PATTERN BLOCK]

[Beat 3 argument grounding pattern in delta and RESOLVED rows]

### Beat 4 — What remains uncertain
*Conflicts carried forward:*
Row 2 — UNRESOLVED:
  Gap: [verbatim]
  Most exposed finding: [verbatim]
  Next signal: [verbatim]

*Additional gaps:*
[entries or "none"]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [paragraph; UNRESOLVED count as risk floor;
at least one RESOLVED row cited by number]
```

---

## V-02

**Variation axis**: Output format — terminal declarative checklist as submission gate
(C-25 primary)
**Hypothesis**: Every prior variation relied on the author's confidence that structural
requirements were met. No variation required the author to explicitly confirm each
requirement at the end. C-25 requires a terminal section with binary pass/fail items —
one per structural requirement — that must be filled in before submission. The key
distinction is *declarative* vs *instructional*: an instructional checklist says "verify
that you wrote the pattern block"; a declarative checklist says "[ ] Pattern block present:
[quote the block's first sentence here]". The declarative form requires the author to
produce evidence of compliance, not just assert it. This variation adds the terminal
Submission Audit as a single-axis change over the prior-track V-01 base (OPEN/CLOSED
lifecycle, pre-story gate, mutation ledger), keeping the analytic structure intact and
isolating the checklist mechanism as the sole difference.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found. Also read
`simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis Mutation Ledger

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
Hypothesis at S3: [one sentence — working hypothesis after all stances applied]
```

**Anti-stagnation check**: If S3 is identical to S0, state why. Silently identical S0
and S3 fails.

---

### Step 3 — Conflict Register

Write the following as the first line of the register section:

```
[REGISTER: OPEN]
```

List every tension between stances. For each:

For RESOLVED rows:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | RESOLVED · `{signal}` because [specific evidential reason] |
```

For UNRESOLVED rows:

```
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | — see UNRESOLVED scaffold — |

Row {N} — UNRESOLVED:
  Gap: [what is unknown]
  Most exposed finding: [which ledger entry depends on this]
  Next signal: {namespace}/{skill} — [expected finding type]
```

**Prohibition**: Every verdict must appear as a named row. Do not record conflict
resolutions in prose narrative.

If no tensions: `Conflict Register: empty.`

Close the register:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

---

### Step 4 — Write the story

**Pre-story gate**: Confirm `[REGISTER CLOSED — ...]` is present. If absent, return to
Step 3.

Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Beat 1 — What we set out to understand**
One to three sentences. State S0 as a falsifiable assertion.

**Beat 2 — What each signal revealed**
One key finding plus one editorial sentence per signal. Two sentences maximum.

**Beat 3 — What the signals say together**

Complete this block before writing prose in Beat 3:

```
Pattern claim: [one declarative sentence naming the cross-signal phenomenon]
Cross-signal basis: [`artifact-A`], [`artifact-B`] — what they show together that
  neither shows alone
Falsifiability test: does any single ledger entry contain this conclusion? [answer]
```

After the block, write the Beat 3 argument. Ground in S0→S3 delta and at least two
RESOLVED rows (cite by row number). UNRESOLVED rows cited by number only.

**Beat 4 — What remains uncertain**
*Conflicts carried forward:* Reproduce every UNRESOLVED scaffold verbatim.
*Additional gaps:* Standard gap format. If none: `Additional gaps: none.`

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on S3. Ground in Beat 3 pattern and at least one RESOLVED row.
Name the UNRESOLVED count as the risk floor.

---

### Step 5 — Submission Audit

**This section is a gate. The artifact is not complete until every item is marked [x].**

Fill each item by marking `[ ]` → `[x]` and providing the specified evidence. Do not
submit with any item left as `[ ]`.

```
SUBMISSION AUDIT — {topic}-story-{date}.md

[ ] S0 FALSIFIABLE — Quote the S0 sentence:
    "{...}"
    Confirm it is a falsifiable assertion (could be wrong): YES / NO

[ ] LEDGER COMPLETE — State artifact count:
    {N} artifacts processed. Confirm each has a Stance entry: YES / NO

[ ] S3 PRESENT — Quote the S3 sentence:
    "{...}"

[ ] ANTI-STAGNATION — Is S3 different from S0 in a way that affects recommendation
    direction or confidence?  YES / NO
    If NO, state reason: {...}

[ ] REGISTER LIFECYCLE — Does [REGISTER: OPEN] appear before the first register row?
    YES / NO
    Does [REGISTER CLOSED — ...] appear after the last row? YES / NO
    Quote the closure stamp: "[REGISTER CLOSED — {...}]"

[ ] PRE-STORY GATE — Was the closure stamp confirmed before Beat 1 was written?
    YES / NO

[ ] PATTERN BLOCK PRESENT — Quote the Pattern claim sentence:
    "{...}"
    Is this claim derivable from any single artifact alone? YES / NO
    (If YES: revise before proceeding)

[ ] UNRESOLVED VERBATIM — Count of UNRESOLVED scaffolds in Beat 4: {U}
    Confirm this matches the U count in the closure stamp: YES / NO

[ ] RECOMMENDATION VERB — Circle one: PROCEED / PAUSE / PIVOT / ABANDON
    Is the verb consistent with the evidence posture described in Beat 3? YES / NO
    Name the posture: {...}

[ ] RISK FLOOR NAMED — Does Beat 5 name the UNRESOLVED count as the risk floor?
    YES / NO
    Quote the sentence: "{...}"
```

All items must be [x] before the artifact is submitted. An unchecked item is a submission
error, not a style choice.

---

**Voice**: Active, opinionated. The Submission Audit is the last structural act — it converts
confidence into evidence. An author who cannot fill each audit item has not yet finished the
artifact.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [falsifiable assertion]

## Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]
**Anti-stagnation check**: [...]

## Conflict Register
[REGISTER: OPEN]

| Row | Signal-A | Signal-B | Dimension | Verdict |
[rows]
[UNRESOLVED scaffolds]
[REGISTER CLOSED — N rows, R RESOLVED, U UNRESOLVED]

## Story

### Beat 1 — What we set out to understand
[S0 as falsifiable assertion; original question]

### Beat 2 — What each signal revealed
[One finding + one editorial sentence per signal]

### Beat 3 — What the signals say together
Pattern claim: [one declarative sentence]
Cross-signal basis: [`artifact-A`], [`artifact-B`] — [what they show together]
Falsifiability test: [answer]

[Beat 3 argument]

### Beat 4 — What remains uncertain
*Conflicts carried forward:*
[UNRESOLVED scaffolds verbatim]
*Additional gaps:*
[entries or "none"]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [grounding paragraph]

---

## Submission Audit
[AUDIT — all items marked [x] before submission]
[ ] S0 FALSIFIABLE — "{...}" — YES / NO
[ ] LEDGER COMPLETE — {N} artifacts — YES / NO
[ ] S3 PRESENT — "{...}"
[ ] ANTI-STAGNATION — YES / NO — reason if NO
[ ] REGISTER LIFECYCLE — OPEN YES/NO · CLOSED YES/NO — "[REGISTER CLOSED — {...}]"
[ ] PRE-STORY GATE — YES / NO
[ ] PATTERN BLOCK PRESENT — "{...}" — derivable from single artifact? YES / NO
[ ] UNRESOLVED VERBATIM — count: {U} matches closure stamp? YES / NO
[ ] RECOMMENDATION VERB — PROCEED/PAUSE/PIVOT/ABANDON — posture consistent? YES / NO
[ ] RISK FLOOR NAMED — YES / NO — "{...}"
```

---

## V-03

**Variation axis**: Role sequence — named execution phases (EVIDENCE / CONFLICT /
PATTERN / STORY) with forward-only entry gates (C-24 via phase vocabulary, not role
vocabulary)
**Hypothesis**: C-24 requires named role sequencing with an explicit one-way transition.
V-01 satisfies this via actor-role vocabulary (ANALYST, AUTHOR). An open question is
whether *phase* vocabulary achieves the same structural verifiability. If the four analytic
phases (EVIDENCE, CONFLICT, PATTERN) each terminate with a named completion stamp, and each
subsequent phase requires confirming the prior stamp before entry, the one-directional
constraint is as structurally visible as a role boundary — the difference is naming
convention, not structural strength. This tests the hypothesis that C-24 can be satisfied
via phase-gating without requiring actor-role vocabulary. The mechanism: each phase is a
named section with an explicit entry gate and a mandatory completion stamp. The STORY phase
cannot be entered until the PATTERN phase stamp is present. Phase re-entry after a later
phase has begun is a named phase sequence violation — visible from the document structure.
Non-substitution is also enforced: each phase's output must appear in its designated
position in the STORY phase; prior-phase presence does not satisfy later-phase requirements.

---

You are running `/topic:story` for a topic. The topic name is provided.

**Phase architecture**: This prompt defines four sequential phases. Each phase has a named
entry gate and a completion stamp. Phases execute in order. No phase may begin until the
prior phase stamp is present. No phase's output satisfies the output requirement of a later
phase — each placement must be independently satisfied.

---

### PHASE I — EVIDENCE
*Entry gate: no prior phase required. Begin immediately.*

#### I.1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found. Also read
`simulations/{topic}/strategy.md` if present.

#### I.2 — Hypothesis Mutation Ledger

**Working hypothesis (S0)**: [one sentence — specific, falsifiable claim — could be
demonstrably wrong, not a goal or general question]

For each signal artifact, in order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — hypothesis after all stances applied]
```

**Anti-stagnation check**: If S3 = S0 in substance, name the specific reason. Silently
identical S0 and S3 fails.

**Phase I complete when**: S3 is written. Write the stamp:

```
[PHASE I COMPLETE — {N} artifacts processed; S3: {one-sentence hypothesis}]
```

---

### PHASE II — CONFLICT
*Entry gate: confirm `[PHASE I COMPLETE]` is present. Do not begin if absent.*

Write the following as the first line of the register:

```
[REGISTER: OPEN — Phase II conflict processing]
```

List every tension between stances. For each, write one row.

For RESOLVED rows:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | RESOLVED · `{signal}` because [specific evidential reason — name the element that outweighs the alternative] |
```

For UNRESOLVED rows:

```
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | — see scaffold — |

Row {N} — UNRESOLVED:
  Gap: [what is unknown — the specific question this conflict raises]
  Most exposed finding: [which ledger entry cannot be confirmed without resolving this]
  Next signal: {namespace}/{skill} — [expected finding type]
```

**Prohibition — carries into all STORY beats**: Conflict adjudications must appear as
named rows in this register. Do not record verdicts in prose.

If no tensions: `Conflict Register: empty.`

Close with:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

Verify: R + U = N.

**Phase II complete when**: Register is closed. Write the stamp:

```
[PHASE II COMPLETE — register closed: {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

---

### PHASE III — PATTERN
*Entry gate: confirm `[PHASE II COMPLETE]` is present. Do not begin if absent.*

Produce the pattern block. This block must stand alone — a reader who reads only this
block must understand the full cross-signal claim without requiring the STORY beats.

```
[PATTERN BLOCK — Phase III]
Pattern claim: [one declarative sentence — names the phenomenon]
Cross-signal basis: `{artifact-A}` × `{artifact-B}` [+ others] — [one sentence: what
  they show together that neither shows alone; name the specific stances involved]
S0→S3 delta: [one sentence — how and in what direction the hypothesis moved]
Evidence posture: STRONG POSITIVE | MIXED | CONFLICTING | WEAK — [one sentence: why]
Falsifiability test: does any single ledger entry contain this conclusion? [YES — revise /
  NO — proceed]
[/PATTERN BLOCK — Phase III]
```

**Phase III complete when**: Pattern block is written, falsifiability test passes. Write:

```
[PHASE III COMPLETE — pattern: {one-sentence pattern claim}; posture: {word}]
```

---

### PHASE IV — STORY
*Entry gate: confirm `[PHASE III COMPLETE]` is present. Do not begin if absent.*

Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Non-substitution rule**: Each beat must independently satisfy its placement requirements.
The PATTERN BLOCK from Phase III does not satisfy Beat 3's pattern requirement — the pattern
must appear in Beat 3 in its own prose-integrated form. Prior-phase presence is not credit
for later-phase placement. Each requirement must be met at its stated position.

**Beat 1 — What we set out to understand**
One to three sentences. State S0 as a falsifiable assertion. Name the entering question.

**Beat 2 — What each signal revealed**
One key finding plus one editorial sentence per signal. Two sentences maximum. Draw from
the Phase I ledger entries.

**Beat 3 — What the signals say together**
State the pattern claim in prose. Reference at least two artifacts by name. Ground the
argument in the S0→S3 delta (from Phase III). RESOLVED rows are pattern evidence — include
their because-clauses. UNRESOLVED rows are in Beat 4 — cite by row number only.

The pattern claim stated here must be derived from the Phase III pattern block, but must
be stated independently — not quoted or directly copied from Phase III. It must be earned
again through the Beat 3 argument.

**Beat 4 — What remains uncertain**
*Conflicts carried forward:* Reproduce every UNRESOLVED scaffold verbatim from Phase II.
*Additional gaps:* Standard gap format. If none: `Additional gaps: none.`

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on S3. Ground in the Beat 3 pattern. Name the evidence posture from
Phase III as the direct basis for the verb. Name the UNRESOLVED count as the risk floor.
Cite at least one RESOLVED row by number.

---

**Voice**: Active, opinionated. Phase stamps are structural acts — they certify that one
phase's output is complete before the next phase begins. The STORY beats are arguments
grounded in a fully closed analytic record, not summaries of it.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## Phase I — Evidence

**Working hypothesis (S0)**: [falsifiable claim]

### Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: ...
  [update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]
**Anti-stagnation check**: [...]

[PHASE I COMPLETE — {N} artifacts processed; S3: {...}]

## Phase II — Conflict

[REGISTER: OPEN — Phase II conflict processing]

| Row | Signal-A | Signal-B | Dimension | Verdict |
[rows + scaffolds]
[REGISTER CLOSED — N rows, R RESOLVED, U UNRESOLVED]

[PHASE II COMPLETE — register closed: N rows, R RESOLVED, U UNRESOLVED]

## Phase III — Pattern

[PATTERN BLOCK — Phase III]
Pattern claim: [one declarative sentence]
Cross-signal basis: `artifact-A` × `artifact-B` — [what they show together]
S0→S3 delta: [direction of movement]
Evidence posture: [STRONG POSITIVE | MIXED | CONFLICTING | WEAK] — [why]
Falsifiability test: [answer]
[/PATTERN BLOCK — Phase III]

[PHASE III COMPLETE — pattern: {...}; posture: {...}]

## Phase IV — Story

### Beat 1 — What we set out to understand
[S0 as falsifiable assertion; entering question]

### Beat 2 — What each signal revealed
[One finding + editorial sentence per signal]

### Beat 3 — What the signals say together
[Pattern in prose; references artifacts by name; grounds in delta and RESOLVED rows]

### Beat 4 — What remains uncertain
*Conflicts carried forward:* [UNRESOLVED scaffolds verbatim]
*Additional gaps:* [entries or "none"]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [posture named; UNRESOLVED count as risk floor;
one RESOLVED row cited by number]
```

---

## V-04

**Variation axis**: Combination — named ANALYST/AUTHOR role gate (C-24, V-01 mechanism)
+ terminal declarative checklist (C-25, V-02 mechanism), on the prior-track V-01 base
(OPEN/CLOSED lifecycle + domain falsifier field)
**Hypothesis**: V-01 and V-02 address C-24 and C-25 independently. The combination tests
whether the two mechanisms compose cleanly and whether the terminal checklist can enforce
the role boundary itself — i.e., whether the Submission Audit's [x] items for role
compliance add a layer of explicit confirmation on top of the structural marker. If the
ANALYST COMPLETE marker provides structural evidence and the audit item requires the author
to quote it, the combination closes the gap where an author might produce the marker
without noticing it was absent at beat-writing time. The base incorporates the prior-track
V-01's OPEN/CLOSED lifecycle and domain falsifier to keep those mechanisms in place while
adding the C-24/C-25 mechanisms on top.

---

You are running `/topic:story` for a topic. The topic name is provided.

**Role architecture**: Two sequential roles — ANALYST and AUTHOR — execute in order. The
ANALYST produces all analytic blocks. The AUTHOR writes all narrative beats. No beat may
begin before `[ANALYST COMPLETE — AUTHOR MAY BEGIN]` is present. Analytic output appearing
after a beat is a role boundary violation. This rule is audited in the Submission Audit.

---

### ANALYST ROLE

The ANALYST executes four tasks before yielding to the AUTHOR. No beat vocabulary is
permitted during the ANALYST phase.

#### ANALYST Task 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found. Also read
`simulations/{topic}/strategy.md` if present.

#### ANALYST Task 2 — Hypothesis Mutation Ledger

**Working hypothesis (S0)**: [one sentence — falsifiable claim — could be demonstrably
wrong, not a goal or question]

For each artifact, in order:

```
- `{artifact-name}`: {key finding, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous] → [updated]
```

After all entries:

```
Hypothesis at S3: [one sentence]
```

**Anti-stagnation check**: If S3 = S0 in substance, name the specific reason.

#### ANALYST Task 3 — Conflict Register

Write:

```
[REGISTER: OPEN — accepting entries]
```

List every tension. For RESOLVED rows:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{A}` | `{B}` | [dimension] | RESOLVED · `{signal}` because [specific evidential reason — name the element that outweighs the alternative] |
```

For UNRESOLVED rows:

```
| {N} | `{A}` | `{B}` | [dimension] | — see scaffold — |

Row {N} — UNRESOLVED:
  Gap: [what is unknown]
  Most exposed finding: [which ledger entry depends on this]
  Next signal: {namespace}/{skill} — [expected finding type]
```

**Prohibition**: Verdicts must appear as named rows. Do not record adjudications in prose.

If no tensions: `Conflict Register: empty.`

Close:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

#### ANALYST Task 4 — Pattern Block

Complete this block before the ANALYST phase concludes:

```
[PATTERN BLOCK]
Pattern claim: [one declarative sentence — names the cross-signal phenomenon]
Cross-signal basis: [`artifact-A`], [`artifact-B`] — what they show together that
  neither shows alone
S0→S3 delta: [one sentence — specific direction of hypothesis movement]
Evidence posture: STRONG POSITIVE | MIXED | CONFLICTING | WEAK — [one sentence: basis]
Domain Falsifier: [one sentence — names a specific observable condition in the subject
  domain that, if observed in the world, would demonstrate the pattern claim is incorrect.
  CONSTRAINT: Must name something external to this signal set and observable in the world,
  market, or system under analysis. Prohibited: conditions about signal provenance,
  source diversity, extraction method, or author overlap. "If all signals came from the
  same author" is a quality check — not a domain falsifier.]
Falsifiability test: does any single ledger entry contain this conclusion? [YES — revise /
  NO — proceed]
[/PATTERN BLOCK]
```

---

#### ANALYST COMPLETE — AUTHOR MAY BEGIN

```
[ANALYST COMPLETE — AUTHOR MAY BEGIN]
```

This marker is required before any beat is written. Its absence when a beat appears is a
role boundary violation audited in the Submission Audit.

---

### AUTHOR ROLE

Write to `simulations/{topic}/{topic}-story-{date}.md`.

If a new conflict is discovered during beat writing: HALT at the point of conflict. Return
to the ANALYST role. Add the conflict to the register. Update the closure stamp. Append
`[ANALYST RE-COMPLETE — AUTHOR MAY RESUME]`. Resume from the halt point.

**Non-substitution rule**: The PATTERN BLOCK produced in the ANALYST phase does not satisfy
Beat 3's pattern placement requirement. Beat 3 must state the pattern independently in prose.
Prior-phase presence is not credit for a later-phase placement requirement.

**Beat 1 — What we set out to understand**
One to three sentences. S0 as a falsifiable assertion. Name the entering question.

**Beat 2 — What each signal revealed**
One key finding plus one editorial sentence per signal. Two sentences maximum.

**Beat 3 — What the signals say together**
State the cross-signal pattern in prose. Reference at least two artifacts by name. Ground
in the S0→S3 delta and at least two RESOLVED rows (include because-clauses; cite by row
number). UNRESOLVED rows in Beat 4 — cite by row number only.

The pattern stated here must be derived from but independently stated from the ANALYST
PATTERN BLOCK. It must be earned through Beat 3's prose argument.

**Beat 4 — What remains uncertain**
*Conflicts carried forward:* Reproduce every UNRESOLVED scaffold verbatim.
*Additional gaps:* Standard gap format. If none: `Additional gaps: none.`

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on S3. Names the evidence posture from the PATTERN BLOCK as the
stated basis for the verb. Grounds in the Beat 3 pattern. Names the UNRESOLVED count as
the risk floor. Cites at least one RESOLVED row by number.

---

### Submission Audit

**Gate**: The artifact is not complete until every item is marked [x]. Do not submit with
any item left as [ ].

```
SUBMISSION AUDIT — {topic}-story-{date}.md

[ ] ANALYST COMPLETE MARKER — Is [ANALYST COMPLETE — AUTHOR MAY BEGIN] present?
    YES / NO
    Does it appear before Beat 1? YES / NO
    Is any analytic block (ledger, register, pattern block) written after a beat?
    YES (role violation — fix before proceeding) / NO

[ ] S0 FALSIFIABLE — Quote the S0 sentence:
    "{...}"
    Is it a falsifiable assertion (could be demonstrably wrong)? YES / NO

[ ] LEDGER COMPLETE — {N} artifacts processed. Each has a Stance: YES / NO

[ ] S3 PRESENT AND DISTINCT — Quote S3: "{...}"
    Is S3 different from S0 in a way that affects recommendation direction or confidence?
    YES / NO. If NO: state reason: {...}

[ ] REGISTER LIFECYCLE — [REGISTER: OPEN] present before first row? YES / NO
    [REGISTER CLOSED — ...] present after last row? YES / NO
    Quote closure stamp: "[REGISTER CLOSED — {...}]"

[ ] PATTERN BLOCK PRESENT — Is [PATTERN BLOCK] ... [/PATTERN BLOCK] present in ANALYST
    phase? YES / NO
    Quote pattern claim: "{...}"
    Is claim derivable from a single artifact? YES (revise) / NO

[ ] DOMAIN FALSIFIER — Does Domain Falsifier name an externally observable domain
    condition? YES / NO
    Does it name a provenance condition (prohibited)? YES (revise) / NO

[ ] NON-SUBSTITUTION — Does Beat 3 state the pattern independently (not quote from
    PATTERN BLOCK)? YES / NO

[ ] UNRESOLVED VERBATIM — Count of UNRESOLVED scaffolds in Beat 4: {U}
    Matches U in closure stamp? YES / NO

[ ] EVIDENCE POSTURE IN BEAT 5 — Does Beat 5 name the evidence posture and cite it as
    the basis for the verb? YES / NO
    Posture: {...} · Verb: {...}

[ ] RISK FLOOR NAMED — Does Beat 5 name the UNRESOLVED count as risk floor? YES / NO
    Quote: "{...}"
```

---

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## ANALYST PHASE

**Working hypothesis (S0)**: [falsifiable claim]

### Hypothesis Mutation Ledger
[entries; S3; anti-stagnation]

### Conflict Register
[REGISTER: OPEN — accepting entries]
[rows + scaffolds]
[REGISTER CLOSED — N rows, R RESOLVED, U UNRESOLVED]

### Pattern Block
[PATTERN BLOCK]
Pattern claim: [...]
Cross-signal basis: [...] — [...]
S0→S3 delta: [...]
Evidence posture: [STRONG POSITIVE | MIXED | CONFLICTING | WEAK] — [...]
Domain Falsifier: [externally observable condition — not provenance]
Falsifiability test: [answer]
[/PATTERN BLOCK]

---
[ANALYST COMPLETE — AUTHOR MAY BEGIN]
---

## AUTHOR PHASE

### Beat 1 — What we set out to understand
[S0 as falsifiable assertion; entering question]

### Beat 2 — What each signal revealed
[One finding + editorial sentence per signal]

### Beat 3 — What the signals say together
[Pattern in prose; independently stated; references artifacts; grounds in delta + RESOLVED rows]

### Beat 4 — What remains uncertain
*Conflicts carried forward:* [UNRESOLVED scaffolds verbatim]
*Additional gaps:* [entries or "none"]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [posture named as basis for verb; risk floor;
RESOLVED row cited]

---

## Submission Audit
[ ] ANALYST COMPLETE MARKER — present? YES/NO · before Beat 1? YES/NO · analytic after beat? YES/NO
[ ] S0 FALSIFIABLE — "{...}" — YES/NO
[ ] LEDGER COMPLETE — {N} artifacts — YES/NO
[ ] S3 PRESENT AND DISTINCT — "{...}" — YES/NO — reason if NO
[ ] REGISTER LIFECYCLE — OPEN YES/NO · CLOSED YES/NO — "[REGISTER CLOSED — {...}]"
[ ] PATTERN BLOCK PRESENT — "{...}" — single-artifact derivable? YES/NO
[ ] DOMAIN FALSIFIER — domain observable? YES/NO · provenance condition? YES/NO
[ ] NON-SUBSTITUTION — Beat 3 independent? YES/NO
[ ] UNRESOLVED VERBATIM — count {U} matches stamp? YES/NO
[ ] EVIDENCE POSTURE IN BEAT 5 — YES/NO · posture: {...} · verb: {...}
[ ] RISK FLOOR NAMED — YES/NO · "{...}"
```

---

## V-05

**Variation axis**: Full combination — all strongest mechanisms from prior track (domain
falsifier, reopen protocol, mutation ledger spine) upgraded with V-01 role gate (C-24)
and V-02 terminal checklist (C-25), plus multi-stage consistency and non-substitution
enforcement
**Hypothesis**: The strongest prior-track variation (V-05 of that track: EVALUATOR/AUTHOR
phases + domain falsifier + full lifecycle) satisfies the structural criteria up through
C-23. What it lacks: named roles with an explicit one-way marker (C-24) and a terminal
binary audit (C-25). This variation takes that full base, upgrades the EVALUATOR section
to also function as the named ANALYST role (satisfying C-24's role vocabulary requirement),
adds the terminal Submission Audit (C-25), enforces non-substitution at each beat (C-19),
and adds multi-stage consistency by requiring the evidence posture and recommendation verb
to appear at two named positions — once in the ANALYST PATTERN BLOCK and once in Beat 5
(C-20). This tests whether the fully integrated architecture — every mechanism stacked —
produces reliable composite scoring across all criteria.

---

You are running `/topic:story` for a topic. The topic name is provided.

**Architecture**: Three named roles execute in strict sequence — EXTRACTOR, ANALYST,
AUTHOR. The EXTRACTOR reads artifacts and produces signal summaries. The ANALYST processes
summaries into analytic blocks. The AUTHOR writes narrative beats. Each role terminates with
a named completion marker. No role may begin until the prior role's marker is present.
Producing any role's output after a later role has begun is a named role boundary violation.

---

### EXTRACTOR ROLE

#### EXTRACTOR Task — Gather and Extract

Glob `simulations/**/{topic}-*`. Read every artifact found. Also read
`simulations/{topic}/strategy.md` if present.

For each artifact, produce one extract entry:

```
SIGNAL EXTRACT: `{artifact-name}`
  Type: {namespace}/{skill}
  Core finding: [one sentence — the single most important fact from this artifact]
  Hypothesis bearing: [one sentence — how this relates to the team's entering claim]
```

Produce one entry per artifact. Entries appear as a named Signal Extract section, not
inline with analysis.

Write the completion marker:

```
[EXTRACTOR COMPLETE — {N} artifacts extracted — ANALYST MAY BEGIN]
```

---

### ANALYST ROLE
*Entry gate: confirm `[EXTRACTOR COMPLETE]` is present.*

The ANALYST performs four tasks. No beat vocabulary is permitted during the ANALYST phase.

#### ANALYST Task 1 — Hypothesis Mutation Ledger

**Working hypothesis (S0)**: [one sentence — falsifiable claim — could be demonstrably
wrong, not a goal or question. Must be a specific proposition, not a research intent]

For each artifact, using its Signal Extract entry, in order:

```
- `{artifact-name}`: {key finding — one to two sentences, drawn from Signal Extract}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous] → [updated]
```

After all entries:

```
Hypothesis at S3: [one sentence — final evolved hypothesis]
```

**Anti-stagnation check**: If S3 = S0 in substance, name the specific reason and why the
signals produced no directional movement. Silently identical S0 and S3 fails.

#### ANALYST Task 2 — Conflict Register

Write:

```
[REGISTER: OPEN — accepting entries]
```

List every tension between stances. For RESOLVED rows:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{A}` | `{B}` | [dimension of disagreement] | RESOLVED · `{signal}` because [specific evidential reason — name the element from that signal that outweighs the alternative, not a general preference] |
```

For UNRESOLVED rows:

```
| {N} | `{A}` | `{B}` | [dimension] | — see scaffold — |

Row {N} — UNRESOLVED:
  Gap: [what is unknown — the specific question this conflict raises]
  Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
  Next signal: {namespace}/{skill} — [expected finding type]
```

**Prohibition — carries into all AUTHOR beats**: Every conflict adjudication must appear as
a named row in this register. Do not record verdicts in narrative prose. This prohibition
applies at beat-writing time even though it is stated here.

If no tensions: `Conflict Register: empty.`

**Reopen protocol**: If a new conflict is discovered during the AUTHOR phase, the AUTHOR
halts at the discovery point. The ANALYST reopens:
(1) Append the new row to the register.
(2) Update the closure stamp: replace `[REGISTER CLOSED — ...]` with
    `[REGISTER RE-CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED — reopened during Story]`
(3) Write: `[ANALYST RE-COMPLETE — AUTHOR MAY RESUME]`
(4) The AUTHOR resumes from the halt point.

Close:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

Verify: R + U = N.

#### ANALYST Task 3 — Pattern Block

```
[PATTERN BLOCK]
Pattern claim: [one declarative sentence — self-contained; names the cross-signal
  phenomenon; a reader who reads only this sentence must understand the full claim]
Cross-signal basis: `{artifact-A}` × `{artifact-B}` [+ others] — [one sentence: what
  they show together that neither shows alone; name the specific stances involved]
S0→S3 delta: [one sentence — specific direction and degree of hypothesis movement; not
  "confirmed" but a named directional shift with the cause named]
Evidence posture: STRONG POSITIVE | MIXED | CONFLICTING | WEAK — [one sentence: basis]
Domain Falsifier: [one sentence — names a specific observable condition in the subject
  domain — a measurable threshold, behavioral indicator, market signal, or system output
  — that, if observed in the world, would demonstrate the pattern claim is incorrect.
  CONSTRAINT: Must be external to this signal set. Must be observable in the world,
  market, or system under analysis. Prohibited: conditions about signal provenance, source
  diversity, extraction method, or author overlap. "If all signals came from the same
  author" is a quality check on the evidence, not a domain falsifier.]
Recommendation direction: PROCEED | PAUSE | PIVOT | ABANDON — [one sentence: why this
  posture produces this verb; this is the first of two required posture-to-verb statements]
Falsifiability test: does any single ledger entry contain this conclusion? [YES — revise /
  NO — proceed]
[/PATTERN BLOCK]
```

#### ANALYST COMPLETE — AUTHOR MAY BEGIN

```
[ANALYST COMPLETE — AUTHOR MAY BEGIN]
```

This marker certifies that the Signal Extract, hypothesis ledger, conflict register, and
pattern block are all complete. The AUTHOR role begins only after this line is present.
Its absence when a beat appears is a role boundary violation, audited in the Submission Audit.

---

### AUTHOR ROLE
*Entry gate: confirm `[ANALYST COMPLETE — AUTHOR MAY BEGIN]` is present.*

Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Non-substitution rule**: The ANALYST PATTERN BLOCK does not satisfy Beat 3's pattern
placement requirement. Beat 3 must state the pattern independently in prose — derived from,
but not quoting, the ANALYST block. This rule applies at each beat:
- Beat 3 pattern: must be independently stated, not referenced from PATTERN BLOCK
- Beat 5 posture-to-verb statement: must be independently stated, not referenced from
  PATTERN BLOCK's Recommendation direction field. Both must appear at their named position.

**Multi-stage consistency rule**: Evidence posture and recommendation verb appear at two
named positions:
(1) ANALYST PATTERN BLOCK (Recommendation direction field)
(2) Beat 5 (evidence-verb statement)
Both must be consistent. Inconsistency between positions is a correctness error.

**Beat 1 — What we set out to understand**
One to three sentences. State S0 as a falsifiable assertion — a specific claim that could
be demonstrably wrong. Name the entering question. Do not summarize the artifact list.

**Beat 2 — What each signal revealed**
Draw from the Signal Extract and ledger entries. For each artifact: the key finding plus
one editorial sentence on what it means for the hypothesis. Two sentences maximum per signal.
Do not produce new analysis here — use the Signal Extract entries as the source.

**Beat 3 — What the signals say together**
State the cross-signal pattern in prose. Reference at least two artifacts by name. Ground
the argument in the S0→S3 delta from the ledger. RESOLVED rows are pattern evidence —
present their because-clauses as part of the argument (cite by row number). UNRESOLVED rows
are in Beat 4 — reference by row number only: "Row {N} remains open."

The pattern stated here must be independently derived through Beat 3's prose argument. It
must be consistent with the ANALYST PATTERN BLOCK but stated in prose, not lifted from it.

**Beat 4 — What remains uncertain**
*Conflicts carried forward:* Reproduce every UNRESOLVED scaffold verbatim — three-line
block exactly as written in the register. Do not rewrite, condense, or reselect.
*Additional gaps (not sourced from conflict):*

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim depends on this]
Next signal: {namespace}/{skill} — [expected finding type]
```

If no additional gaps: `Additional gaps: none.`

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on S3, not S0. Contains:
- Evidence-posture statement: name the overall signal posture and cite it as the direct
  basis for the verb chosen. This is the second of two required posture-to-verb statements;
  it must be consistent with the Recommendation direction in the ANALYST PATTERN BLOCK.
- Pattern citation: the Beat 3 pattern, named by reference, is the stated reason for the verb.
- Risk floor: the UNRESOLVED count from the closure stamp, named as the risk floor.
- Warrant: at least one RESOLVED row cited by number.
"It depends" without a stated default fails.

---

### Submission Audit

**Gate**: Artifact is not complete until every item is marked [x]. Do not submit with any
item as [ ]. Each item requires quoted evidence, not assertion.

```
SUBMISSION AUDIT — {topic}-story-{date}.md

ROLE BOUNDARY COMPLIANCE
[ ] EXTRACTOR COMPLETE marker present: YES / NO
[ ] ANALYST COMPLETE marker present: YES / NO
    Does ANALYST COMPLETE appear before Beat 1? YES / NO
    Does any analytic block appear after a beat? YES (role violation) / NO

ANALYTIC COMPLETENESS
[ ] Signal Extract section present: YES / NO · {N} entries: YES / NO
[ ] S0 is falsifiable assertion: YES / NO
    Quote S0: "{...}"
[ ] Ledger complete: {N} artifacts, each with Stance: YES / NO
[ ] S3 present: Quote S3: "{...}"
[ ] Anti-stagnation: S3 ≠ S0 in direction or confidence? YES / NO
    If NO: reason: {...}
[ ] REGISTER: OPEN declaration present: YES / NO
[ ] Closure stamp present: Quote: "[REGISTER CLOSED — {...}]" YES / NO
[ ] Pattern block present with all fields: YES / NO
    Quote pattern claim: "{...}"
    Is claim derivable from a single artifact alone? YES (revise) / NO
[ ] Domain Falsifier names externally observable condition: YES / NO
    Names provenance condition (prohibited)? YES (revise) / NO
[ ] Recommendation direction in PATTERN BLOCK: verb: {...} · posture: {...}

NON-SUBSTITUTION COMPLIANCE
[ ] Beat 3 pattern stated independently (not quoted from PATTERN BLOCK): YES / NO
[ ] Beat 5 posture-to-verb stated independently (not quoted from PATTERN BLOCK): YES / NO

MULTI-STAGE CONSISTENCY
[ ] Posture in PATTERN BLOCK: {...}
[ ] Posture in Beat 5: {...}
    Consistent? YES / NO
[ ] Verb in PATTERN BLOCK: {...}
[ ] Verb in Beat 5: {...}
    Consistent? YES / NO

STORY BEAT COMPLIANCE
[ ] Beat 4 UNRESOLVED scaffolds: count {U} matches closure stamp U count: YES / NO
[ ] UNRESOLVED scaffolds reproduced verbatim (not rewritten): YES / NO
[ ] Beat 5 risk floor names UNRESOLVED count: YES / NO
    Quote: "{...}"
[ ] At least one RESOLVED row cited in Beat 5 by row number: YES / NO
    Which row: Row {N}
```

---

**Voice**: Active, opinionated. The three-role architecture is structural enforcement —
EXTRACTOR sees the evidence, ANALYST adjudicates it, AUTHOR argues from the closed record.
The Submission Audit is the final act: it converts structural confidence into structural
evidence.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## EXTRACTOR PHASE

### Signal Extract
SIGNAL EXTRACT: `{artifact-name}`
  Type: {namespace}/{skill}
  Core finding: [one sentence]
  Hypothesis bearing: [one sentence]
[... one entry per artifact]

[EXTRACTOR COMPLETE — {N} artifacts extracted — ANALYST MAY BEGIN]

## ANALYST PHASE

**Working hypothesis (S0)**: [falsifiable claim]

### Hypothesis Mutation Ledger
- `{artifact-name}`: {finding from Signal Extract}
  Stance: ...
  [update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]
**Anti-stagnation check**: [...]

### Conflict Register
[REGISTER: OPEN — accepting entries]
[rows + scaffolds]
[REGISTER CLOSED — N rows, R RESOLVED, U UNRESOLVED]

### Pattern Block
[PATTERN BLOCK]
Pattern claim: [self-contained declarative sentence]
Cross-signal basis: `artifact-A` × `artifact-B` — [what together]
S0→S3 delta: [direction and cause]
Evidence posture: [STRONG POSITIVE | MIXED | CONFLICTING | WEAK] — [basis]
Domain Falsifier: [externally observable domain condition — not provenance]
Recommendation direction: [PROCEED | PAUSE | PIVOT | ABANDON] — [posture-to-verb reason]
Falsifiability test: [answer]
[/PATTERN BLOCK]

---
[ANALYST COMPLETE — AUTHOR MAY BEGIN]
---

## AUTHOR PHASE

### Beat 1 — What we set out to understand
[S0 as falsifiable assertion; entering question]

### Beat 2 — What each signal revealed
[One finding + editorial sentence per signal; drawn from Signal Extract]

### Beat 3 — What the signals say together
[Pattern in prose — independently stated, derived from but not quoting PATTERN BLOCK;
references artifacts by name; grounds in delta and RESOLVED rows with because-clauses]

### Beat 4 — What remains uncertain
*Conflicts carried forward:* [UNRESOLVED scaffolds verbatim from register]
*Additional gaps:* [entries or "none"]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [evidence posture named as basis for verb —
second of two posture-to-verb statements; Beat 3 pattern cited by reference; UNRESOLVED
count named as risk floor; at least one RESOLVED row cited by number]

---

## Submission Audit
ROLE BOUNDARY COMPLIANCE
[ ] EXTRACTOR COMPLETE: YES/NO
[ ] ANALYST COMPLETE: YES/NO · before Beat 1? YES/NO · analytic after beat? YES/NO

ANALYTIC COMPLETENESS
[ ] Signal Extract: YES/NO · {N} entries
[ ] S0 falsifiable: YES/NO · "{...}"
[ ] Ledger complete: {N} artifacts · YES/NO
[ ] S3: "{...}" · ≠ S0? YES/NO
[ ] REGISTER OPEN: YES/NO · REGISTER CLOSED: YES/NO · "[REGISTER CLOSED — {...}]"
[ ] Pattern block all fields: YES/NO · claim: "{...}" · single-artifact? YES/NO
[ ] Domain Falsifier domain-observable: YES/NO · provenance? YES/NO
[ ] PATTERN BLOCK recommendation: verb: {...} posture: {...}

NON-SUBSTITUTION
[ ] Beat 3 independent: YES/NO
[ ] Beat 5 posture-to-verb independent: YES/NO

MULTI-STAGE CONSISTENCY
[ ] PATTERN BLOCK posture: {...} · Beat 5 posture: {...} · consistent? YES/NO
[ ] PATTERN BLOCK verb: {...} · Beat 5 verb: {...} · consistent? YES/NO

STORY BEAT COMPLIANCE
[ ] Beat 4 UNRESOLVED count {U} matches stamp: YES/NO
[ ] Scaffolds verbatim: YES/NO
[ ] Risk floor named: YES/NO · "{...}"
[ ] RESOLVED row cited in Beat 5: YES/NO · Row {N}
```
