---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 10
rubric: v9
---

# Variations — topic-story (Round 10)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v9 rubric adds C-22 (adjacent-verb contrast) and C-23 (vector-to-verb
conditions clause). Two extractable patterns from Round 9:

**Pattern A — Adjacent-verb contrast (C-22, sourced from R9 V-02 Beat 4.5 licensing
sentence):**
R9 V-02 introduced Beat 4.5 as a dedicated derivation beat with three lines. The third
line — "Recommendation verb: {VERB} — [one sentence: why this verb rather than the adjacent
alternatives]" — contains the *shape* of C-22 but not its specificity requirement. The line
asks for a licensing condition without requiring the adjacent verb to be named explicitly as
a contrast target. C-22's pass condition adds two requirements not present in R9 V-02: (1)
the adjacent verb must be named by label (PROCEED, PAUSE, PIVOT, or ABANDON), and (2) the
licensing sentence must state what specific element — in the signal evidence, the verdict
distribution, or the net vector value — would have to differ for the adjacent verb to apply
instead. A reader who believes the adjacent verb is warranted must find a specific claim in
that element to contest, not merely disagree with the recommendation. R9 V-01 and V-03 both
score C-21 at PARTIAL or PASS without ever naming the adjacent verb — confirming that the
derivation chain can be explicit without satisfying the adjacent-verb contrast requirement.

**Pattern B — Vector-to-verb conditions clause (C-23, sourced from R9 V-03 "because-
therefore" prose template):**
R9 V-03 introduced the prose construction: "Because [anchored S3 claim], the hypothesis
[arrived at / was moved to] [net vector]. [Net vector] [in this context / under these
conditions / given the gap profile] means [verb]." The `under [conditions]` slot is the
C-23 target — but R9 V-03's template leaves it open to be filled with vague markers like
"in this context" or "under these circumstances" that restate the vector without adding
constraining information. C-23 requires the conditions slot to name a current state of the
evidence landscape: the count of unresolved CONTRADICTS, the gap-closure cost, the risk
tolerance threshold, or the readiness signal distribution. A conditions clause filled with
a named evidence-state parameter is independently falsifiable: a reader who accepts the
QUALIFIED vector but disputes that the named condition holds can contest the verb choice
without contesting the evidence or the derivation chain. R9 V-01 and V-02 both have
vector-to-verb mappings that route through the derivation chain without conditions — V-02
gets C-21 PASS without C-23, confirming the independence of the two criteria.

Round 10 primary axes: V-01 targets C-22 directly (adjacent-verb as a mandatory fourth
line in Beat 4.5, named and with a specific contestation claim). V-02 targets C-23 directly
(conditions slot in the "because-therefore" prose construction made category-constrained —
must name an evidence-state parameter, not a contextual placeholder). V-03 targets both via
role sequence (a CHALLENGER sub-step before the recommendation paragraph argues the adjacent-
verb case, which the recommendation then rebuts — producing both C-22 and C-23 organically
rather than through format enforcement). V-04 combines V-01 and V-02 on the R9 V-04 base
(the round's strongest performer). V-05 is the full combination: R9 V-05 base
(EVALUATOR/AUTHOR phases) upgraded with C-22 adjacent-verb in AUTHOR's derivation chain
and C-23 conditions clause enforced in AUTHOR's recommendation paragraph.

---

## V-01

**Variation axis**: Output format — adjacent-verb contrast as mandatory fourth line in
derivation chain
**Hypothesis**: C-22 fails when the derivation chain's licensing sentence names a condition
for the chosen verb without committing to the adjacent verb by name. R9 V-02's "why this
verb rather than the adjacent alternatives" prompt is a condition opener — it asks for a
rationale but does not require the adjacent verb to be identified as the specific contrast
target. The fix is structural: add a mandatory fourth line to Beat 4.5 that (a) names the
adjacent verb explicitly by its PROCEED/PAUSE/PIVOT/ABANDON label and (b) states the specific
element — in the signal evidence, verdict distribution, or net vector value — that would have
to differ for that alternative to apply. This converts the licensing sentence from a rationale
("why I chose this verb") into a contrast claim ("why the other verb is ruled out by this
specific condition"). The distinction: a rationale can be contested in the abstract; a contrast
claim names the exact condition a dissenting reader must dispute. This tests whether adding
a single structural line to the existing R9 V-02 derivation chain satisfies C-22 without
requiring changes to any other beat.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

Before writing the story, complete the ledger. Write it to the artifact as the first section.

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances are applied]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: the specific mechanism — which stances, on which dimension, drove this
classification. Reference at least one ledger entry by artifact name.]
```

**Anti-stagnation check**: If S3 is identical to S0, state why explicitly. An unchanged
hypothesis stated with a reason is defensible. Silently identical S0 and S3 fails.

**Reconciliation check**: Compare the declared vector to the ledger stance distribution.
CONFIRMED with visible unresolved CONTRADICTS entries, or REVERSED with no CONTRADICTS
entries, must be revised before proceeding.

Do not begin the story beats until the ledger is complete.

---

### Step 3 — Write the story beats

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. State the
entering default: what the team expected to confirm, and why that expectation was the
reasonable prior.

**Beat 2 — What each signal revealed** *(draws from the ledger)*
For each ledger entry, one editorial sentence beyond the finding — what the finding means
for the hypothesis. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries.

Open Beat 3 with the net mutation vector:
"Across [N] signals, the hypothesis was [CONFIRMED / QUALIFIED / REVERSED / REDIRECTED]."
Then build the pattern from there.

**Anchor citation rule**: Every non-trivial claim in Beat 3 must cite the specific ledger
entry that licenses it, inline: `(anchored: {artifact-name}, {stance})`. A Beat 3 claim
without a ledger anchor is an assertion, not a derivation.

For every tension between stances:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause.

Falsifiability test: does any single ledger entry contain the Beat 3 conclusion? If yes,
revisit — and verify anchor citations span multiple entries.

**Beat 4 — What remains uncertain**
Specific, scoped gaps. RESOLVED verdicts are not gaps. UNRESOLVED verdicts become gaps.

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 4.5 — Derivation chain** *(written before the recommendation)*

Four elements, each on its own line:

```
Anchored claim: "[exact S3 claim from Beat 3 that drives the decision, copied verbatim
  with inline anchor citation]" (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence from ledger,
  copied verbatim]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what in the
  vector and gap profile licenses this specific verb]
Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what specific element
  of the signal evidence, verdict distribution, or net vector value would have to differ for
  this adjacent verb to apply instead — name the exact claim a reader who prefers the adjacent
  verb must contest]
```

**Adjacent verb guidance:**
The adjacent verb is the single most likely alternative a reasonable reader would choose.
Adjacent pairs by decision dimension:
- PROCEED ↔ PAUSE (confidence dimension — how much uncertainty is acceptable to move forward)
- PAUSE ↔ PIVOT (commitment dimension — whether the current direction is worth holding)
- PIVOT ↔ ABANDON (recovery dimension — whether a new direction is viable)

The "Adjacent verb" line is not a restatement of why the chosen verb is correct. It names
the *other* case: what specific gap, stance count, or vector condition would have to hold
for the adjacent verb to be the right call. A reader who believes PAUSE is warranted when
PROCEED is chosen must find a specific evidence-state claim in the "Adjacent verb: PAUSE"
line to contest — not merely a conviction to dispute.

Do not write Beat 5 until all four derivation chain elements are internally consistent.

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** (must match the verb in Beat 4.5).
One paragraph. The derivation chain is already recorded — Beat 5 does not repeat it. Beat 5
names what to do, under what conditions, and with what scope. "Proceed with caution" without
naming the caution fails.

---

**Voice**: Active, opinionated. The ledger reads as a formal record; the derivation chain
reads as a decision frame; the recommendation paragraph reads as a directive.

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
**Net mutation vector**: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism sentence]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector].
[cross-signal pattern — each claim with (anchored: {artifact-name}, {stance})]
[Conflict / Verdict / because-clause entries for each tension]

### Beat 4 — What remains uncertain
[Gap / Most exposed finding / Next signal entries]

### Beat 4.5 — Derivation chain
Anchored claim: "[verbatim S3 claim]" (anchored: {artifact-name}, {stance})
Net vector: {vector} — [mechanism sentence]
Recommendation verb: {VERB} — [licensing sentence]
Adjacent verb: {ADJACENT-VERB} — [specific contestation claim — what would have to differ]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive paragraph — what to do, under what
  conditions — does not re-argue the derivation chain]
```

---

## V-02

**Variation axis**: Phrasing register — conditions clause with mandatory evidence-state
category in vector-to-verb mapping
**Hypothesis**: C-23 fails when the `[under [conditions]]` slot in the R9 V-03 "because-
therefore" construction is filled with a contextual placeholder rather than a named evidence-
state parameter. "QUALIFIED in this context means pause" does not satisfy C-23 because "in
this context" is opaque — a reader who accepts the QUALIFIED vector but prefers PROCEED cannot
identify what specific condition to dispute. The fix is a category constraint on the conditions
slot: the model must fill it with a named parameter drawn from four permitted categories —
(1) count of unresolved CONTRADICTS, (2) gap-closure cost, (3) risk tolerance threshold,
(4) readiness signal distribution. Each category makes the mapping independently falsifiable:
a reader who disputes the stated condition can contest the verb choice without contesting the
evidence, the derivation chain, or the mutation vector. "QUALIFIED with 0 unresolved
CONTRADICTS means proceed" is falsifiable (a reader can dispute whether 0 is the right
threshold). "QUALIFIED in the current context means proceed" is not (nothing to contest).
This tests whether enforcing the conditions slot category alone — without the adjacent-verb
contrast mechanism of V-01 — satisfies C-23 in the prose register.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

Before writing the story, complete the ledger. Write it to the artifact as the first section.

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances are applied]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: the specific mechanism — which stances, on which dimension, drove this
classification. Reference at least one ledger entry by artifact name.]
```

**Anti-stagnation check**: If S3 is identical to S0, state why explicitly.

**Reconciliation check**: Compare the declared vector to the ledger stance distribution.
CONFIRMED with unresolved CONTRADICTS entries, or REVERSED with no CONTRADICTS entries,
must be revised before proceeding.

Do not begin the story beats until the ledger is complete.

---

### Step 3 — Write the story beats

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. State the
entering default: what the team expected to confirm, and why.

**Beat 2 — What each signal revealed** *(draws from the ledger)*
For each ledger entry, one editorial sentence beyond the finding — what the finding means
for the hypothesis. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries.

Open Beat 3 with the net mutation vector:
"Across [N] signals, the hypothesis was [CONFIRMED / QUALIFIED / REVERSED / REDIRECTED]."
Then build the pattern from there.

**Anchor citation rule**: Every non-trivial claim in Beat 3 must cite the specific ledger
entry that licenses it, inline: `(anchored: {artifact-name}, {stance})`. A Beat 3 claim
without a ledger anchor is an assertion.

For every tension between stances:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause.

Falsifiability test: does any single ledger entry contain the Beat 3 conclusion? If yes,
revisit.

**Beat 4 — What remains uncertain**
Specific, scoped gaps. RESOLVED verdicts are not gaps. UNRESOLVED verdicts become gaps.

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.

The recommendation paragraph must route through the derivation chain explicitly using
the following sentence construction, with the conditions slot filled from a named category:

> **Because** [exact anchored S3 claim from Beat 3, with inline anchor citation],
> the hypothesis arrived at [net vector as declared in the ledger].
> [Net vector] with [**conditions — one of the four permitted categories below**] means
> **[proceed / pause / pivot / abandon]**: [one to two sentences naming what to do].

**Permitted conditions categories** (choose exactly one; fill with specific values, not
generics):

1. **CONTRADICTS count**: State the count of unresolved CONTRADICTS entries and why that
   count maps to this verb. Example: "QUALIFIED with 0 unresolved CONTRADICTS means proceed —
   every tension in the ledger was resolved in favor of the core hypothesis."
2. **Gap-closure cost**: Characterize the effort required to close the Beat 4 gaps and why
   that cost profile maps to this verb. Example: "QUALIFIED given that all three gaps are
   closeable with a single prove/prototype signal means proceed — the qualification is bounded
   and addressable before commit."
3. **Risk tolerance threshold**: Name the risk tolerance level at which this vector maps to
   this verb versus the adjacent one. Example: "QUALIFIED at standard-risk tolerance means
   pause — the qualification introduces conditions that a conservative team must validate
   before committing resources."
4. **Readiness signal distribution**: State the share of signals confirming the core hypothesis
   and why that distribution maps to this verb. Example: "QUALIFIED with 7 of 9 signals
   confirming the core claim means proceed — the qualification narrows scope but does not
   reverse direction."

**Prohibited fills for the conditions slot:**
- Restatements of the vector: "QUALIFIED under these qualified conditions means proceed" — fails
- Contextual placeholders: "QUALIFIED in this context means pause" — fails
- Restatements of the recommendation: "QUALIFIED given these circumstances means proceed with
  full understanding of the qualification" — fails

The conditions sentence is independently falsifiable. A reader who accepts the net vector
and the evidence but disputes that the named condition holds can contest the verb choice
without disputing the derivation chain. This is the test: if a reader cannot find a specific
condition to dispute, the conditions clause has not satisfied C-23.

If Beat 4 gaps are blocking: name them in the conditions clause — "QUALIFIED with [N] gaps
closeable at [cost] means proceed unless [specific gap] resolves against the hypothesis, in
which case pause."

---

**Voice**: Active, editorial. The "because-therefore" construction is the author's voice at
its most committed — it names conditions, not hedges. The conditions clause reads as a
falsifiable claim, not a qualification.

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
**Net mutation vector**: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism sentence]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector].
[cross-signal pattern — each claim with (anchored: {artifact-name}, {stance})]
[Conflict / Verdict / because-clause entries for each tension]

### Beat 4 — What remains uncertain
[Gap / Most exposed finding / Next signal entries]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON**

Because [anchored S3 claim] (anchored: {artifact-name}, {stance}), the hypothesis arrived
at [net vector]. [Net vector] with [named evidence-state parameter from permitted categories]
means [verb]: [directive continuation — what to do].
```

---

## V-03

**Variation axis**: Role sequence — CHALLENGER sub-step before recommendation paragraph
**Hypothesis**: C-22 and C-23 are both reasoning requirements about what would make the
adjacent verb correct. Format constraints (V-01's fourth line, V-02's conditions slot) enforce
the output structure but do not guarantee that the reasoning behind the contrast claim is
substantive rather than formulaic. A CHALLENGER sub-step — where the model is instructed to
argue the adjacent-verb case before writing the recommendation — produces the adjacent-verb
argument organically: the model must identify what conditions would support the adjacent verb
and state them as claims, which the recommendation then answers. This is different from
V-01's fourth line (which states the contrast as a conclusion) and V-02's conditions slot
(which fills a template). The CHALLENGER produces the conditions for the adjacent verb;
the AUTHOR produces the conditions for the chosen verb and identifies why the current evidence
state satisfies the chosen verb's conditions rather than the adjacent verb's. Both C-22 and
C-23 emerge from the challenge-rebuttal structure rather than from format enforcement.
The rebuttal names the adjacent verb and the specific claim that rules it out (C-22); it also
names the conditions under which the chosen verb applies given the current evidence state
(C-23). This tests whether role-sequenced argument generation is more reliable than format
constraints for producing contestable, conditions-bounded verb selection.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

Before writing the story, complete the ledger. Write it to the artifact as the first section.

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances are applied]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: the specific mechanism — which stances, on which dimension, drove this
classification. Reference at least one ledger entry by artifact name.]
```

**Anti-stagnation check**: If S3 is identical to S0, state why explicitly.

**Reconciliation check**: CONFIRMED with unresolved CONTRADICTS, or REVERSED with no
CONTRADICTS, must be revised before proceeding.

Do not begin the story beats until the ledger is complete.

---

### Step 3 — Write the story beats

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. Name the
entering default: what the team expected to confirm, and why.

**Beat 2 — What each signal revealed** *(draws from the ledger)*
For each ledger entry, one editorial sentence beyond the finding — what the finding means
for the hypothesis. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries.

Open Beat 3 with the net mutation vector:
"Across [N] signals, the hypothesis was [CONFIRMED / QUALIFIED / REVERSED / REDIRECTED]."
Then build the pattern from there.

**Anchor citation rule**: Every non-trivial claim in Beat 3 must cite the specific ledger
entry that licenses it, inline: `(anchored: {artifact-name}, {stance})`.

For every tension between stances:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause.

Falsifiability test: does any single ledger entry contain the Beat 3 conclusion? If yes,
revisit.

**Beat 4 — What remains uncertain**
Specific, scoped gaps. RESOLVED verdicts are not gaps. UNRESOLVED verdicts become gaps.

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 5 — Recommendation**

Before writing the recommendation paragraph, run two sub-steps in sequence. Both sub-steps
are written to the artifact and visible to the reader.

**Sub-step A — CHALLENGER**

Identify the most likely adjacent verb — the single alternative a reasonable reader who
accepted the Beat 3 evidence but reached a different conclusion would choose. Adjacent pairs:
PROCEED ↔ PAUSE, PAUSE ↔ PIVOT, PIVOT ↔ ABANDON.

Write a CHALLENGER paragraph arguing for the adjacent verb. The paragraph must:
- Name the adjacent verb explicitly
- State the conditions under which that verb would be correct — what evidence state, gap
  profile, or vector property would make the adjacent verb the warranted call
- Reference at least one specific ledger entry or Beat 4 gap that the CHALLENGER would
  cite as grounds for the alternative verdict

The CHALLENGER speaks on behalf of a reader who holds the adjacent verb. The CHALLENGER
does not know the final recommendation — it argues from the evidence as read.

**Sub-step B — AUTHOR rebuttal**

Write the AUTHOR's rebuttal. The rebuttal must:
- Name the adjacent verb the CHALLENGER proposed
- State the specific claim that rules it out — what in the current evidence state, verdict
  distribution, or net vector value does not match the conditions the CHALLENGER named
- Name the conditions under which the chosen verb applies: the evidence-state parameter
  (CONTRADICTS count, gap-closure cost, risk tolerance, or readiness distribution) that
  the current signal set satisfies

The rebuttal is not a dismissal of the CHALLENGER. It engages the CHALLENGER's specific
conditions claim and names the current evidence state that resolves the contest in favor of
the chosen verb.

**Recommendation paragraph**

After the CHALLENGER and rebuttal, write one recommendation paragraph:
- One of: **proceed**, **pause**, **pivot**, **abandon** (must follow from the rebuttal)
- Names what to do, under what conditions, with what scope
- Does not repeat the CHALLENGER or rebuttal — assumes the reader has seen both
- "It depends" without a stated default fails

---

**Voice**: The CHALLENGER sub-step is argued in first person on behalf of a dissenting
reader. The AUTHOR rebuttal is editorial and committed. The recommendation paragraph is
directive. All three are visible in the artifact — the reader can audit the contest.

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
**Net mutation vector**: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism sentence]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector].
[cross-signal pattern — each claim with (anchored: {artifact-name}, {stance})]
[Conflict / Verdict / because-clause entries for each tension]

### Beat 4 — What remains uncertain
[Gap / Most exposed finding / Next signal entries]

### Beat 5 — Recommendation

**CHALLENGER — case for [adjacent verb]**
[Paragraph: adjacent verb named, conditions stated, at least one ledger/gap citation]

**AUTHOR — rebuttal**
[Paragraph: adjacent verb named, specific ruling-out claim, conditions for chosen verb
  as a named evidence-state parameter]

**PROCEED | PAUSE | PIVOT | ABANDON** — [directive paragraph — what to do, under what
  conditions, no re-argument of CHALLENGER/rebuttal]
```

---

## V-04

**Variation axis**: Combination — V-01 (adjacent-verb contrast as fourth derivation chain
line) + V-02 (conditions clause with mandatory evidence-state category) on R9 V-04 base
(reconciliation table + derivation chain beat + anchor citations)
**Hypothesis**: R9 V-04 was the strongest Round 9 performer, closing C-17 through C-21 via
the combination of reconciliation table (C-20) and derivation chain beat (C-21) on the R8
V-04 base. C-22 and C-23 are additive extensions to the existing Beat 4.5 structure: C-22
adds a fourth line naming the adjacent verb and its specific contestation claim; C-23 adds
a conditions clause to the Beat 5 recommendation paragraph's because-therefore construction,
requiring it to name an evidence-state parameter. Neither addition conflicts with the R9 V-04
structure — the fourth line slots after the existing "Recommendation verb" line in Beat 4.5;
the conditions category enforcement operates within Beat 5's opening sentence, which already
routes through the derivation chain. Together they produce three independent contestation
points on the recommendation: the derivation chain is traceable (C-21), the verb choice is
falsifiable via adjacent contrast (C-22), and the vector-to-verb mapping is falsifiable via
conditions (C-23). C-06 achieves its strictest satisfiable form when all three are active.
The reconciliation table (C-20) ensures the vector against which C-22 and C-23 operate is
verified — no adjacent-verb contrast can be assessed against an unverified vector declaration.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

Before writing the story, complete the ledger. Write it to the artifact as the first section.

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances are applied]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: the specific mechanism — which stances, on which dimension, drove this
classification. Reference at least one ledger entry by artifact name.]
```

**Anti-stagnation check**: If S3 is identical to S0, state why explicitly. An unchanged
hypothesis stated with a reason is defensible. Silently identical S0 and S3 fails.

---

### Step 2b — Vector-verdict reconciliation table

Complete the following table immediately after declaring the net mutation vector. One row
per ledger entry.

```
| Signal | Verdict type | Consistent with declared vector? |
|--------|-------------|----------------------------------|
| {artifact-name} | CONFIRMS — {brief dimension label} | YES |
| {artifact-name} | MODIFIES toward {dimension} | YES |
| {artifact-name} | CONTRADICTS on {dimension} — RESOLVED | YES (resolved) |
| {artifact-name} | CONTRADICTS on {dimension} — UNRESOLVED | CONFLICT |
```

**Consistency rules by declared vector:**

- **CONFIRMED**: All CONTRADICTS entries must be RESOLVED. Any UNRESOLVED CONTRADICTS entry
  produces a CONFLICT row — the vector cannot be CONFIRMED while an unresolved contradiction
  stands. Revise the vector to QUALIFIED or resolve the contradiction in Beat 3.
- **QUALIFIED**: CONFIRMS and MODIFIES entries expected; CONTRADICTS entries only if RESOLVED;
  MODIFIES entries pulling in a consistent direction.
- **REVERSED**: Majority evidential weight in CONTRADICTS or directionally-reversing MODIFIES.
  CONFIRMS entries permitted if narrower in scope than the reversal.
- **REDIRECTED**: Entries answer a different evaluative frame than S0 posed — neither CONFIRMS
  nor CONTRADICTS the original claim.

After the table:

```
Reconciliation: Vector is consistent — [one sentence explaining why the verdict distribution
  maps to the declared choice].
```

OR, if a CONFLICT row was found:

```
Reconciliation: Vector revised from [X] to [Y] — [one sentence naming the CONFLICT entry
  that forced the revision and what resolution was made].
```

Do not begin the story beats until the ledger, vector, reconciliation table, and
reconciliation conclusion are all complete.

---

### Step 3 — Write the story beats

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. Name the
entering default: what the team expected to confirm, and why.

**Beat 2 — What each signal revealed** *(draws from the ledger)*
For each ledger entry, one editorial sentence beyond the finding — what the finding means
for the hypothesis. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries.

Open Beat 3 with the reconciled net mutation vector:
"Across [N] signals, the hypothesis was [CONFIRMED / QUALIFIED / REVERSED / REDIRECTED]."
The reconciliation table validates this claim — no additional justification needed in the
prose itself.

**Anchor citation rule**: Every non-trivial claim in Beat 3 must cite the specific ledger
entry that licenses it, inline: `(anchored: {artifact-name}, {stance})`. MODIFIES entries
are the primary anchors for new synthesis claims. CONFIRMS entries anchor persistence or
validation claims. CONTRADICTS entries anchor adjudication verdicts.

For every tension between stances:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason — name the
         element from that signal's ledger entry that outweighs the alternative]
     OR: UNRESOLVED because [what {namespace}/{skill} would provide the missing evidence]
```

Every verdict carries a because-clause. Any CONFLICT row from the reconciliation table
must appear here as an explicit Conflict/Verdict entry.

Falsifiability test: does any single ledger entry contain the Beat 3 conclusion? If yes,
revisit — and verify anchor citations span multiple entries.

**Beat 4 — What remains uncertain**
Specific, scoped gaps. RESOLVED verdicts are not gaps. UNRESOLVED verdicts become gaps.

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 4.5 — Derivation chain** *(written before the recommendation)*

Five elements, each on its own line:

```
Anchored claim: "[exact S3 claim from Beat 3 that drives the decision, copied verbatim
  with inline anchor citation]" (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence from
  ledger, copied verbatim — must match reconciliation table declaration exactly]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what in the
  vector and gap profile licenses this specific verb]
Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what specific element
  of the signal evidence, verdict distribution, or net vector value would have to differ for
  this adjacent verb to apply instead — name the exact claim a reader who prefers the adjacent
  verb must contest]
Conditions: [evidence-state parameter — one of: CONTRADICTS count / gap-closure cost /
  risk tolerance threshold / readiness signal distribution — stated as a specific value, not
  a generic label]
```

**Adjacent verb and conditions guidance:**

The "Adjacent verb" line names the contrast target and the specific ruling-out claim (C-22).
The "Conditions" line names the evidence-state parameter that makes this vector imply this
verb rather than the adjacent one (C-23). The two lines operate at different levels: the
adjacent verb line tells a dissenting reader what specific claim to contest; the conditions
line tells anyone why the vector-to-verb mapping is not universal but conditioned on the
current evidence state.

Adjacent pairs: PROCEED ↔ PAUSE (confidence), PAUSE ↔ PIVOT (commitment), PIVOT ↔ ABANDON
(recovery).

Permitted conditions categories for the "Conditions" line — choose exactly one:
1. Count of unresolved CONTRADICTS and the threshold
2. Gap-closure cost and what that cost level implies for timing
3. Risk tolerance threshold and which side of it the current evidence sits
4. Readiness signal distribution — share of signals confirming the core hypothesis

A conditions line filled with a contextual placeholder ("under current conditions") fails.

Do not write Beat 5 until all five derivation chain elements are internally consistent.

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** (must match Beat 4.5).
One paragraph. The derivation chain is already recorded in Beat 4.5 — Beat 5 does not
repeat it. Beat 5 names what to do, under what conditions, with what scope.
"Proceed with caution" without naming the caution fails.

---

**Voice**: Active, opinionated. The ledger and reconciliation table read as a formal record;
the derivation chain reads as a decision frame with three contestation points; the
recommendation paragraph reads as a directive.

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
**Net mutation vector**: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism sentence]

## Vector-Verdict Reconciliation
| Signal | Verdict type | Consistent? |
|--------|-------------|-------------|
| {artifact-name} | {type — dimension} | YES / CONFLICT |
...
**Reconciliation**: Vector is consistent — [reason] | Vector revised from [X] to [Y] — [reason]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector].
[cross-signal pattern — each claim with (anchored: {artifact-name}, {stance})]
[Conflict / Verdict / because-clause entries for each tension]

### Beat 4 — What remains uncertain
[Gap / Most exposed finding / Next signal entries]

### Beat 4.5 — Derivation chain
Anchored claim: "[verbatim S3 claim]" (anchored: {artifact-name}, {stance})
Net vector: {vector} — [mechanism sentence]
Recommendation verb: {VERB} — [licensing sentence]
Adjacent verb: {ADJACENT-VERB} — [specific contestation claim — what would have to differ]
Conditions: [named evidence-state parameter — specific value, not generic label]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive paragraph — what to do, under what
  conditions — no re-argument of derivation chain]
```

---

## V-05

**Variation axis**: Full combination — R9 V-05 base (EVALUATOR/AUTHOR phases + Signal
Extract with stance rationale + reconciliation table in EVALUATOR) upgraded with C-22
adjacent-verb contrast in AUTHOR derivation chain and C-23 conditions clause enforced in
AUTHOR recommendation
**Hypothesis**: R9 V-05 achieved the cleanest architecture by phase-separating evidence
extraction (EVALUATOR) from synthesis (AUTHOR), with the reconciliation table completing
in EVALUATOR before AUTHOR ever touches synthesis. C-22 and C-23 are both AUTHOR-phase
concerns: the adjacent-verb contrast requires the S3 anchor and the net vector (both
declared in EVALUATOR output) but the contrast claim itself depends on the AUTHOR's Beat 3
synthesis — which EVALUATOR cannot produce. The conditions clause requires the gap profile
from AUTHOR's Beat 4 and the verdict distribution already verified by EVALUATOR's
reconciliation table. Adding C-22 to AUTHOR's derivation chain (as a fourth element between
"Recommendation verb" and the end of the chain) and enforcing C-23 in AUTHOR's recommendation
paragraph (conditions slot with mandatory evidence-state category) fits the phase model
cleanly: EVALUATOR produces the verified vector that C-22 and C-23 operate against; AUTHOR
produces the adjacent-verb contrast and conditions clause against that verified foundation.
The phase boundary strengthens both criteria independently: AUTHOR cannot introduce new
evidence after EVALUATOR's reconciliation table is complete, so the vector the adjacent-verb
contrast addresses cannot be revised after the fact — the contrast operates on a fixed,
auditable record.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two phases: **EVALUATOR** then **AUTHOR**. Do not begin AUTHOR until
EVALUATOR is complete and written to the artifact.

---

## EVALUATOR Phase

**Permitted**: Reading artifacts. Extracting findings. Assigning stances and rationales.
Tracking hypothesis mutation. Declaring the net vector. Completing the reconciliation table.
**Forbidden**: Forming cross-signal patterns. Drawing synthesis conclusions. Adjudicating
conflicts. These belong to AUTHOR.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Declare the working hypothesis (S0)

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
- No thematic grouping, no ranking by apparent significance
- Every entry gets a stance and a rationale — these are EVALUATOR responsibilities
- The rationale names the specific evidence: the finding, measurement, or observation that
  led to the classification. "This signal generally supports the hypothesis" fails.
  "The 94% pass rate confirms because it exceeds the threshold established in {other artifact}"
  passes.
- Only MODIFIES entries get a hypothesis update line
- CONFIRMS and CONTRADICTS entries carry only stance and rationale

---

### Step 4 — Declare S3 and net mutation vector

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all MODIFIES stances applied]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: the specific mechanism — which stances, on which dimension, drove this
classification. Reference at least one Signal Extract entry by artifact name.]
```

Definitions:
- **CONFIRMED** — S3 = S0. Signals validated the entering claim. Name the strongest validating entries.
- **QUALIFIED** — S3 adds conditions, scope limits, or caveats absent from S0. Name which MODIFIES entries introduced the qualification.
- **REVERSED** — S3 is directionally opposite to S0 on at least one primary dimension. Name the pivot entry.
- **REDIRECTED** — S3 addresses a materially different question than S0. Name the entry that surfaced the new question.

**Anti-stagnation check**: If S3 = S0, explain why: "S3 = S0: [reason no MODIFIES stance
was warranted]." Silently identical S0 and S3 fails.

---

### Step 5 — Vector-verdict reconciliation table

After declaring the vector, complete the following table before exiting EVALUATOR. One row
per Signal Extract entry.

```
| Signal | Verdict type | Consistent with declared vector? |
|--------|-------------|----------------------------------|
| {artifact-name} | CONFIRMS — {dimension from rationale} | YES |
| {artifact-name} | MODIFIES toward {dimension} | YES |
| {artifact-name} | CONTRADICTS on {dimension} — RESOLVED | YES (resolved) |
| {artifact-name} | CONTRADICTS on {dimension} — UNRESOLVED | CONFLICT |
```

**Consistency rules by declared vector:**
- **CONFIRMED**: All CONTRADICTS entries must be RESOLVED. Any UNRESOLVED CONTRADICTS entry
  is a CONFLICT row — the vector cannot be CONFIRMED while an unresolved contradiction stands.
  Revise the vector to QUALIFIED or flag the contradiction for AUTHOR to adjudicate in S3.
- **QUALIFIED**: CONFIRMS and MODIFIES entries expected; CONTRADICTS entries only if RESOLVED;
  MODIFIES entries pulling in a consistent direction.
- **REVERSED**: Majority evidential weight in CONTRADICTS or directionally-reversing MODIFIES.
  CONFIRMS entries permitted if narrower in scope than the reversal.
- **REDIRECTED**: Entries answer a different evaluative frame than S0 posed.

If a CONFLICT row exists: EVALUATOR must either revise the declared vector (updating the
Step 4 declaration) or flag the conflict row as "AUTHOR to adjudicate in S3." Unresolved
CONFLICT rows may not be silently passed to AUTHOR.

After the table:

```
Reconciliation: Vector is consistent — [reason].
  OR: Vector revised from [X] to [Y] — [reason].
  OR: CONFLICT on [{artifact-name}] — flagged for AUTHOR adjudication in S3.
```

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
**Net mutation vector**: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism sentence]

## Vector-Verdict Reconciliation
| Signal | Verdict type | Consistent? |
|--------|-------------|-------------|
...
**Reconciliation**: [conclusion sentence]
```

Do not begin AUTHOR until this section is complete.

---

## AUTHOR Phase

**Permitted**: Pattern derivation. Cross-signal synthesis. Conflict adjudication.
Recommendation. Adjacent-verb contrast. Conditions clause.
**Forbidden**: Re-reading signal artifacts. All findings, stances, and rationales are in
the Signal Extract. If a finding is not in the Signal Extract, it is not available to this
synthesis. If the Signal Extract is incomplete, return to EVALUATOR.

**Input**: The Signal Extract, stances, rationale sentences, S3 hypothesis, declared net
mutation vector, and reconciliation table above.

Write to `simulations/{topic}/{topic}-story-{date}.md`, Story section following the Signal
Extract and Reconciliation sections.

**Writing discipline**: Prose establishes arc first; trajectory markers annotate after.
Markers: `[CONFIRMED]` · `[COMPLICATED]` · `[REVERSES]` · `[UNCERTAIN]`
Removal test: strip all markers. The Story must be fully readable as a briefing with no
logical gaps. If removing a marker creates a gap, rewrite the prose before the marker.

---

**S1 — What we set out to understand** `[TRAJECTORY: assumed]`
*Prose first.* The original question and the S0 working hypothesis. The entering default:
what the team expected to confirm, and why that expectation was the reasonable prior.
One to three sentences.

**S2 — What each signal revealed** `[marker — after prose]`
*Prose first.* Draw from the Signal Extract. One editorial sentence per entry beyond the
finding — what the finding means given its stance and rationale. Two sentences maximum
per signal.

The marker here reflects the net stance pressure on the entering hypothesis after all S2
entries: `[CONFIRMED]` if predominantly CONFIRMS, `[COMPLICATED]` if CONFIRMS with notable
MODIFIES, `[REVERSES]` if CONTRADICTS or directionally reversing MODIFIES dominate.

If the marker is `[COMPLICATED]` or `[REVERSES]`: the prose must name the specific Signal
Extract entries with MODIFIES or CONTRADICTS stances and cite their rationale before the
marker is placed.

**S3 — What the signals say together** `[marker — after prose]`
*Prose first.* The cross-signal pattern. Only visible across the full Signal Extract.
Reference at least two entries by artifact name.

Open S3 by naming the declared net mutation vector:
"Across [N] signals, the hypothesis was [CONFIRMED / QUALIFIED / REVERSED / REDIRECTED]."
The reconciliation table validates this claim — no additional justification needed in prose.

**Anchor citation rule**: Every non-trivial S3 synthesis claim must cite the specific
Signal Extract entry that licenses it, inline: `(anchored: {artifact-name}, {stance})`.
A claim without a Signal Extract anchor is an assertion. MODIFIES entries are the primary
anchors for new synthesis claims. CONFIRMS entries anchor persistence or validation claims.
CONTRADICTS entries anchor adjudication verdicts.

For every tension between stances (CONFIRMS vs CONTRADICTS, or competing MODIFIES updates),
apply:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [the rationale from {signal}'s Signal
         Extract entry outweighs {other signal}'s rationale because {specific reason}]
     OR: UNRESOLVED because [what {namespace}/{skill} would provide the missing evidence]
```

Every tension named gets a verdict. Every verdict carries a because-clause that references
the rationale sentences from the Signal Extract. Any CONFLICT row flagged by EVALUATOR must
be adjudicated here.

Falsifiability test: does any single Signal Extract entry contain the S3 conclusion? If yes,
revisit — and verify anchor citations span multiple entries.

**S4 — What remains uncertain** `[UNCERTAIN]`
*Prose first.* Specific, scoped gaps. RESOLVED verdicts from S3 are not gaps. UNRESOLVED
verdicts from S3 become gaps automatically.

```
Gap: [what is unknown]
Most exposed finding: [which Signal Extract entry's rationale depends on this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**S4.5 — Derivation chain** *(written before S5)*

Five elements, each on its own line:

```
Anchored claim: "[exact S3 claim that drives the decision, copied verbatim with its
  inline anchor citation]" (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence from
  Signal Extract, copied verbatim — must match reconciliation table exactly]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what in the
  vector and gap profile licenses this specific verb]
Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what specific element
  of the Signal Extract record, reconciliation verdict distribution, or net vector value
  would have to differ for this adjacent verb to apply instead — name the exact claim a
  reader who prefers the adjacent verb must contest]
Conditions: [one of: CONTRADICTS count / gap-closure cost / risk tolerance threshold /
  readiness signal distribution — stated as a specific value drawn from the Signal Extract
  and reconciliation table, not a generic placeholder]
```

**Adjacent verb guidance for AUTHOR:**
The adjacent verb line must reference the reconciled evidence record — not a hypothetical
alternative reading. If EVALUATOR's reconciliation table shows 0 CONFLICT rows, and the
adjacent verb would require a CONFLICT row, name that: "PAUSE would apply if {artifact-name}
remained UNRESOLVED CONTRADICTS; the reconciliation table shows it was resolved, ruling out
PAUSE." The reconciliation table is the auditable foundation for the contrast claim.

**Conditions guidance for AUTHOR:**
The conditions category must draw from the Signal Extract's visible evidence state — the
actual count of CONTRADICTS in the reconciliation table, the actual gap count from S4, the
actual share of CONFIRMS in the record. A conditions clause that references evidence not in
the Signal Extract fails — AUTHOR cannot introduce new evidence.

Do not write S5 until all five derivation chain elements are internally consistent.

**S5 — Recommendation** `[marker — after prose]`
*Prose first.* One of: **proceed**, **pause**, **pivot**, **abandon** (must match S4.5).
One paragraph. The derivation chain in S4.5 is already recorded — S5 does not repeat it.
S5 names what to do, under what conditions, with what scope. "Proceed with caution" without
naming the caution fails.

---

**Voice**: Active. Opinionated. The Signal Extract and reconciliation table read as a formal
record; the Story reads as an editorial argument that a decision-maker would quote from; the
derivation chain in S4.5 reads as a decision frame with three independent contestation points.

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
**Net mutation vector**: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism sentence]

## Vector-Verdict Reconciliation
| Signal | Verdict type | Consistent? |
|--------|-------------|-------------|
...
**Reconciliation**: [conclusion sentence]

## Story

### S1 — What we set out to understand
[TRAJECTORY: assumed] Prose...

### S2 — What each signal revealed
[MARKER] Per-signal prose from Signal Extract stances and rationales...

### S3 — What the signals say together
[MARKER] Across [N] signals, the hypothesis was [vector].
[Cross-signal pattern — each claim with (anchored: {artifact-name}, {stance})]
[Conflict / Verdict / because-clause entries for each tension]

### S4 — What remains uncertain
[UNCERTAIN] Gap entries (Gap / Most exposed finding / Next signal)...

### S4.5 — Derivation chain
Anchored claim: "[verbatim S3 claim]" (anchored: {artifact-name}, {stance})
Net vector: {vector} — [mechanism sentence]
Recommendation verb: {VERB} — [licensing sentence]
Adjacent verb: {ADJACENT-VERB} — [specific contestation claim — what would have to differ,
  grounded in reconciliation table]
Conditions: [named evidence-state parameter — specific value from Signal Extract record]

### S5 — Recommendation
[MARKER] **PROCEED | PAUSE | PIVOT | ABANDON** — [directive paragraph — what to do,
  under what conditions — no re-argument of derivation chain or S4.5]
```

Artifact: `simulations/{topic}/{topic}-story-{date}.md`
