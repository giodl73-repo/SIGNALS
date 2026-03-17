---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 11
rubric: v10
---

# Variations — topic-story (Round 11)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v10 rubric adds C-28 (recommendation preview before analytic blocks)
and C-29 (namespace enumeration as EXTRACTOR instruction). Two universal failures from
Round 10:

**Pattern 1 — C-01 universal failure (source of C-28):**
Every R10 variation places the first explicit recommendation verb in Beat 5 — the last
beat. The five-beat epistemic sequence structurally defers the verdict. No R10 variation
used a pre-analysis verdict declaration. C-28 is the structural fix: a named VERDICT
block placed before any analytic work — not a forward reference, but an independently
stated recommendation verb. The VERDICT block and Beat 5 are independent placements;
VERDICT satisfies BLUF (C-01); Beat 5 delivers the accountability-addressed,
bridge-connected recommendation. Three single-axis approaches for C-28: V-01 adds VERDICT
as a pre-gather declaration to the R10 V-01 base; V-02 positions VERDICT before all three
tri-roles; V-03 frames VERDICT as the inertia recommendation being tested by signals.
The three framings differ in how the upfront verdict relates to the final one: V-01 treats
it as a prior commitment that Beat 5 independently confirms; V-02 treats it as a structural
gate that the role sequence enforces; V-03 treats it as the baseline whose evolution the
story measures.

**Pattern 2 — C-05 universal failure (source of C-29):**
Every R10 variation leaves namespace coverage to authorial discretion — no template
enforces namespace enumeration as a named step. C-05 requires three distinct signal sources;
C-29 requires the template to mandate enumeration as a named EXTRACTOR deliverable.
C-29 depends on C-26 (tri-role structure): EXTRACTOR must be a named role distinct from
ANALYST for namespace enumeration to be a role-bound requirement rather than an editorial
option. V-02 and V-05 implement the full tri-role (EXTRACTOR/ANALYST/AUTHOR) to satisfy
C-26 and thereby enable C-29. V-04 adds namespace enumeration as a named Step 1 sub-task
without full tri-role — a targeted addition to the R10 V-04 base that tests whether the
C-29 mandate can be partially achieved without the full dependency chain.

Round 11 primary axes:
- V-01: Output format — VERDICT block added to R10 V-01 base (C-28 only, no tri-role)
- V-02: Role sequence — full tri-role EXTRACTOR/ANALYST/AUTHOR (C-24, C-26, C-28, C-29)
- V-03: Inertia framing — VERDICT as the entering recommendation tested by signals
- V-04: Combination — VERDICT + namespace enumeration on R10 V-04 base (C-28 + C-29 targeted)
- V-05: Full combination — tri-role + VERDICT + reconciliation + 5-element derivation + terminal checklist

---

## V-01

**Variation axis**: Output format — pre-analysis VERDICT block added to R10 V-01 base
**Hypothesis**: C-01 fails because the five-beat sequence structurally positions the
verdict last. The fix does not require architectural change — it requires a single named
block placed before gather that states the recommendation verb independently. R10 V-01's
four-element derivation chain (Beat 4.5 with adjacent-verb contrast) remains intact;
so does the hypothesis mutation ledger. The only addition is a VERDICT block before Step 1.
This tests whether the minimal insertion satisfies C-28 (and thereby C-01) without
touching namespace enumeration, role structure, or the derivation chain mechanics. C-29
is not addressed here — namespace coverage remains discretionary. The VERDICT block uses
two required lines: the verb and a one-sentence basis. Conditionality is prohibited —
a conditional VERDICT ("if signals are positive, proceed") is a forward reference, not an
independent declaration. Beat 5 must state the pattern-to-recommendation bridge
independently — the VERDICT does not discharge that requirement.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### VERDICT *(complete before proceeding to Step 1)*

Before reading any signal artifact, state your recommendation.

```
VERDICT: [PROCEED | PAUSE | PIVOT | ABANDON]
Basis: [one sentence — the specific claim or prior posture that licenses this verdict]
```

The VERDICT is an independently-stated decision, not a placeholder. Prohibited forms:
"TBD pending signals." "Will depend on what signals show." "Unclear without evidence."
These fail — the VERDICT names the verb the team holds as a prior, before signal reading.

The VERDICT and Beat 5 are independent placements. Both are required. The VERDICT satisfies
BLUF here; Beat 5 delivers the full accountability-addressed recommendation argument.
If Beat 5 verb differs from VERDICT, name the reason explicitly in Beat 5.

Do not begin Step 1 until the VERDICT is declared.

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

**Reconciliation check**: CONFIRMED with visible unresolved CONTRADICTS entries, or
REVERSED with no CONTRADICTS entries, must be revised before proceeding.

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
revisit — verify anchor citations span multiple entries.

**Beat 4 — What remains uncertain**
Specific, scoped gaps. RESOLVED verdicts are not gaps. UNRESOLVED verdicts become gaps.

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 4.5 — Derivation chain** *(written before Beat 5)*

Four elements, each on its own line:

```
Anchored claim: "[exact S3 claim from Beat 3 that drives the decision, copied verbatim
  with inline anchor citation]" (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence from
  ledger, copied verbatim]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what in the
  vector and gap profile licenses this specific verb]
Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what specific element
  of the signal evidence, verdict distribution, or net vector value would have to differ for
  this adjacent verb to apply instead — name the exact claim a reader who prefers the
  adjacent verb must contest]
```

Adjacent pairs: PROCEED ↔ PAUSE (confidence), PAUSE ↔ PIVOT (commitment),
PIVOT ↔ ABANDON (recovery).

The "Adjacent verb" line names the other case: what specific gap, stance count, or vector
condition would have to hold for the adjacent verb to be the right call.

Do not write Beat 5 until all four derivation chain elements are internally consistent.

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** (must match Beat 4.5 verb).

Opens with the pattern-to-recommendation bridge — independently placed, not carried
from Beat 4.5:
"Because [named cross-signal pattern from Beat 3], [verb]."

One paragraph total. Names what to do, under what conditions, with what scope.
If Beat 5 verb differs from VERDICT declared before Step 1: name the revision reason
explicitly. "Proceed with caution" without naming the specific caution fails.

---

**Voice**: Active, opinionated. The VERDICT reads as an entering commitment. The ledger
reads as a formal record. The derivation chain reads as a decision frame. Beat 5 reads
as a directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## VERDICT
**[PROCEED | PAUSE | PIVOT | ABANDON]**
Basis: [one sentence]

## Hypothesis Mutation Ledger
**Working hypothesis (S0)**: [claim]

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
**PROCEED | PAUSE | PIVOT | ABANDON**
Because [named cross-signal pattern from Beat 3], [verb]. [Directive continuation — what
  to do, under what conditions, with what scope.]
```

---

## V-02

**Variation axis**: Role sequence — full tri-role EXTRACTOR/ANALYST/AUTHOR with mandatory
namespace enumeration as EXTRACTOR's first deliverable
**Hypothesis**: C-05 and C-29 fail when namespace coverage is left to authorial discretion.
The structural fix is the tri-role sequence: EXTRACTOR reads artifacts and produces two
deliverables — (1) namespace enumeration as a named, minimum-threshold output and (2)
signal digests with stances. ANALYST reads EXTRACTOR output only and produces the
pre-composition analytic blocks (hypothesis mutation, pattern, delta, posture, derivation
pre-work) — separating artifact reading from synthesis. AUTHOR reads ANALYST output and
writes narrative beats. This one-way flow satisfies C-24 (role execution order gate) and
C-26 (tri-role artifact extraction gate). The namespace enumeration instruction in
EXTRACTOR satisfies C-29 by converting C-05's coverage requirement from an authorial
option into a role-bound deliverable. C-28 is satisfied by placing VERDICT before
EXTRACTOR begins — the VERDICT is the one output that precedes all roles. Explicit
"ROLE COMPLETE" markers enforce one-way gate discipline: ANALYST cannot re-read artifacts;
AUTHOR cannot re-read digests or artifacts.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### VERDICT *(complete before any role begins)*

Before any artifact is read, state the recommendation.

```
VERDICT: [PROCEED | PAUSE | PIVOT | ABANDON]
Basis: [one sentence — the specific claim or prior posture that licenses this verdict]
```

Independently stated. Not conditional. Not a forward reference.
VERDICT and Beat 5 are independent placements — both required.
Do not begin EXTRACTOR work until the VERDICT is declared.

---

## ROLE: EXTRACTOR

*Reads signal artifacts. Produces digests. Does not synthesize or draw cross-signal
conclusions. ANALYST may not begin until both EXTRACTOR outputs are marked COMPLETE.*

### EXTRACTOR Output 1 — Namespace Enumeration

Glob `simulations/**/{topic}-*`. Before reading any artifact, list the namespaces
expected for this topic. After reading, verify and update.

```
Namespaces represented:
1. {namespace} — {N} artifacts: [{artifact names}]
2. {namespace} — {N} artifacts: [{artifact names}]
...
Total distinct namespaces: {N}
Coverage gap (if any): [which namespaces are absent that would strengthen the synthesis]
```

Minimum: 3 distinct namespaces or artifact types. If fewer than 3, flag as coverage gap.

This enumeration is a required EXTRACTOR deliverable, not an authorial editorial option.
C-05's signal coverage requirement is satisfied structurally here — not at the author's
discretion. The namespace list must appear in the artifact before ANALYST begins.

### EXTRACTOR Output 2 — Signal Digests

Read every artifact found. Also read `simulations/{topic}/strategy.md` if present.
For each artifact, in the order read:

```
- `{artifact-name}` [{namespace}]: {key finding — one to two sentences, stated as fact}
  Hypothesis relevance: {one sentence — how this finding bears on the working hypothesis}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Candidate hypothesis update: [previous claim] → [proposed update]
```

Rules:
- One entry per artifact, in gather order. No thematic grouping.
- Every entry gets a stance. "Unclear" is not a stance — assign best-fit and note ambiguity.
- EXTRACTOR does not resolve conflicts between artifacts.
- EXTRACTOR does not state the cross-signal pattern.
- Digests are extraction outputs, not synthesis claims.

**EXTRACTOR COMPLETE** — ANALYST may now begin. EXTRACTOR produces no further output.

---

## ROLE: ANALYST

*Reads EXTRACTOR outputs only. Does not re-read original signal artifacts. Produces four
outputs. AUTHOR may not begin until all four ANALYST outputs are marked COMPLETE.*

### ANALYST Output 1 — Hypothesis Mutation Chain

**Working hypothesis (S0)**: [one sentence — the specific falsifiable claim the team
entered with, derived from the digest set and strategy.md context. Not a goal or question.
A specific claim that could be proven wrong.]

Apply EXTRACTOR stance entries in artifact order:

```
- `{artifact-name}`: {stance from EXTRACTOR digest}
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [evolved hypothesis after all modifications applied]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
Mechanism: [one sentence — which stances and on which dimension drove this classification,
  citing at least one artifact by name]
```

**Anti-stagnation check**: S3 identical to S0 → state explicitly why no modification
was warranted. Silently identical S0 and S3 fails.

**Reconciliation check**: CONFIRMED with unresolved CONTRADICTS in EXTRACTOR digests →
revise to QUALIFIED or flag for AUTHOR to adjudicate in Beat 3.

### ANALYST Output 2 — Cross-Signal Pattern Block

A discrete, self-contained, labeled claim that stands independently of narrative prose.

```
PATTERN: [one to three sentences — the relationship, tension, or gap across signals that
no single signal shows alone. Must reference at least two EXTRACTOR digest entries by
artifact name. Must be a synthetic claim — not a side-by-side summary of findings.]
(anchored: {artifact-name-1}, {stance}) and ({artifact-name-2}, {stance})
```

Falsifiability test: can any single EXTRACTOR digest entry contain this pattern claim
without the others? If yes, the claim is not cross-signal — revise.

ANALYST Output 2 is the pre-composition pattern artifact. AUTHOR cites it in Beat 3
but does not re-derive it from scratch. Non-substitution: the PATTERN block here does
not discharge the independent bridge sentence required in Beat 5.

### ANALYST Output 3 — Delta Block

```
DELTA:
S0 (entering): [S0 hypothesis verbatim]
Key signal shift: {artifact-name} — {stance} — [what this entry changed in the hypothesis]
S3 (evolved): [S3 hypothesis verbatim]
Mutation: [one sentence — what specifically changed and why it matters for the decision]
```

Anti-stagnation: "The signals confirmed what we already believed" without a named
confidence gain or scope change fails — the mutation sentence must name what the signals
added that the entering hypothesis did not contain.

### ANALYST Output 4 — Evidence Posture and Derivation Pre-Work

```
Evidence posture: STRONG POSITIVE | MIXED | CONFLICTING | WEAK
[one sentence: share or weight of signals supporting the core hypothesis claim]

Anchored claim: "[exact S3 claim from Pattern block, verbatim, with anchor citation]"
  (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence,
  verbatim from Output 1]

Recommendation verb (pre-committed): {PROCEED | PAUSE | PIVOT | ABANDON}
[one sentence: what in the vector and gap profile licenses this specific verb]

Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON}
[one sentence: what specific element — stance count, gap profile, or vector property —
would have to differ for the adjacent verb to apply. Name the exact claim to contest.]

Conditions: [evidence-state parameter — one of: CONTRADICTS count / gap-closure cost /
  risk tolerance threshold / readiness signal distribution — stated as a specific value,
  not a contextual placeholder or restatement of the vector]
```

Adjacent pairs: PROCEED ↔ PAUSE (confidence), PAUSE ↔ PIVOT (commitment),
PIVOT ↔ ABANDON (recovery).

Pre-committed verb is not a prior discharge of the Beat 5 bridge sentence requirement.

**ANALYST COMPLETE** — AUTHOR may now begin. ANALYST produces no further output.

---

## ROLE: AUTHOR

*Reads ANALYST outputs only. Does not re-read EXTRACTOR digests or original artifacts.
Writes the five narrative beats and the independent recommendation paragraph.*

If any ANALYST output is missing or incomplete, return to ANALYST before beginning.

### Beat 1 — What we set out to understand
One to three sentences. The S0 hypothesis as a falsifiable claim. The entering default
and why it was the reasonable prior.

### Beat 2 — What each signal revealed *(draws from ANALYST Output 1 mutation chain)*
For each ledger entry, one editorial sentence on what the finding means for the hypothesis.
Two sentences maximum per signal.

### Beat 3 — What the signals say together
Open with the net mutation vector: "Across [N] signals, the hypothesis was [vector]."
Cite the PATTERN block from ANALYST Output 2. Every non-trivial claim carries an anchor:
`(anchored: {artifact-name}, {stance})`.

For every CONTRADICTS tension in ANALYST Output 1:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause.

### Beat 4 — What remains uncertain
UNRESOLVED verdicts from Beat 3 become gaps. RESOLVED verdicts are not gaps.

```
Gap: [what is unknown]
Most exposed finding: [which artifact's claim is unverifiable without this]
Next signal: {namespace}/{skill} — [expected finding type]
```

### Beat 5 — Recommendation

**Non-substitution rule — Beat 5 specific**: The pattern-to-recommendation bridge
sentence required in Beat 5 is an independently-placed requirement. ANALYST Output 4
pre-commits the recommendation verb — that pre-commitment does not discharge the bridge
sentence that Beat 5 must contain. Even if equivalent in content, the bridge must appear
here as an original statement, not a reference to ANALYST Output 4.

Beat 5 bridge format — first or second sentence:
"Because [named cross-signal pattern from Beat 3], [verb]."

One of: **proceed**, **pause**, **pivot**, **abandon** (must match ANALYST Output 4 verb).
One paragraph: what to do, under what conditions, with what scope.
If Beat 5 verb differs from VERDICT declared before EXTRACTOR: name the revision reason.

---

**Voice**: EXTRACTOR records without judgment. ANALYST reasons without narrating.
AUTHOR advocates without re-deriving. Three distinct voices, one-way flow.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## VERDICT
**[PROCEED | PAUSE | PIVOT | ABANDON]**
Basis: [one sentence]

---

## EXTRACTOR

### Namespace Enumeration
1. {namespace} — {N} artifacts: [names]
...
Total distinct namespaces: {N}
Coverage gap: [or "none"]

### Signal Digests
- `{artifact-name}` [{namespace}]: {finding}
  Hypothesis relevance: {relevance}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [Candidate hypothesis update if MODIFIES]
...

**EXTRACTOR COMPLETE**

---

## ANALYST

### Hypothesis Mutation Chain
**S0**: [claim]
- `{artifact-name}`: {stance}
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} — [mechanism sentence]

### Pattern Block
PATTERN: [synthetic cross-signal claim]
(anchored: {artifact-name-1}, {stance}) and ({artifact-name-2}, {stance})

### Delta Block
DELTA:
S0 (entering): [verbatim]
Key signal shift: {artifact-name} — {stance} — [change]
S3 (evolved): [verbatim]
Mutation: [what changed and why it matters]

### Evidence Posture and Derivation Pre-Work
Evidence posture: {posture} — [basis sentence]
Anchored claim: "[verbatim S3 claim]" (anchored: {artifact-name}, {stance})
Net vector: {vector} — [mechanism verbatim]
Recommendation verb (pre-committed): {VERB} — [licensing sentence]
Adjacent verb: {ADJACENT-VERB} — [contestation claim]
Conditions: [named evidence-state parameter — specific value]

**ANALYST COMPLETE**

---

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector].
PATTERN: [cited from ANALYST — cross-signal claim with anchor citations]
[Conflict / Verdict entries for each tension]

### Beat 4 — What remains uncertain
[Gap / Most exposed finding / Next signal entries]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON**
Because [named cross-signal pattern from Beat 3], [verb].
[Directive continuation — what to do, under what conditions, with what scope.]
```

---

## V-03

**Variation axis**: Inertia framing — VERDICT as the entering recommendation, tested
by signals, with verdict evolution as the primary delta measure
**Hypothesis**: C-28 requires a VERDICT before analysis; C-21 requires a falsifiable
hypothesis as the inertia baseline; C-22 requires the delta to show substantive mutation.
These three criteria share a common structure: a stated prior that the signals test. V-01
satisfies C-28 with a VERDICT block. V-03 goes further: the VERDICT is explicitly the
inertia recommendation — the verb the team would commit to based on the entering hypothesis
before any signal is read. This converts the VERDICT from a structural BLUF device into
the measurement baseline. The S0→S3 delta is now measured in two dimensions: how the
hypothesis evolved and whether the recommended verb held. If the verb changed, the story
must name which signals caused the change. If the verb held, the story must name what the
signals added beyond confirming the prior — otherwise the anti-stagnation check fires.
The inertia basis is independently falsifiable: it names the condition that, if wrong,
would warrant a different verb — creating a precise target for the signals to confirm or
challenge. This framing makes C-09 (delta surfacing) and C-22 (anti-stagnation) directly
measurable: the inertia verb either matches or doesn't match the Beat 5 verb, and the
story must account for both outcomes.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### INERTIA VERDICT *(complete before gathering signals)*

Before reading any signal artifact, state the recommendation that follows from the team's
entering hypothesis — the verb the team would commit to today, based on prior knowledge,
without additional signal evidence.

```
INERTIA VERDICT: [PROCEED | PAUSE | PIVOT | ABANDON]
Entering hypothesis: [one sentence — the specific claim the team believes to be true,
  stated as a falsifiable assertion]
Inertia basis: [one sentence — why this hypothesis, as currently understood, warrants
  this verb. Name the specific condition: what would have to change for the verb to shift.]
```

The INERTIA VERDICT is not conditional on signals. It is the committed prior that signals
will test. Prohibited: "Unclear until signals are read." "Will determine after gathering."
The INERTIA VERDICT names the recommendation the team holds as a prior — signals either
confirm it or challenge it.

Do not begin signal gathering until the INERTIA VERDICT is declared.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Inertia ledger

For each signal artifact, record how it bears on the INERTIA VERDICT — does it support,
modify, or challenge the entering recommendation?

```
- `{artifact-name}`: {key finding, one to two sentences}
  Stance on inertia verdict: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Verdict update: [what changed in the hypothesis or in the verb warrant]
  [if CONTRADICTS]: Challenge: [what specific claim the signal disputes in the inertia basis]
```

After all entries:

```
Evolved hypothesis (S3): [one sentence — hypothesis after all modifications]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
Verdict evolution: [one sentence — did the recommended verb hold, weaken, strengthen, or
  change? Name which stances and on which dimension drove the evolution.]
```

**Anti-stagnation check**: If the verb did not change and the hypothesis barely changed,
state explicitly what the signals added beyond confirming the prior. "Signals confirmed
what we expected" without naming what the confirmation adds to confidence or scope fails.

**Inertia-to-final delta:**
```
Inertia: {original verb} — [inertia basis, verbatim]
Final: {final verb} — [what changed, or what the signals added that the prior lacked]
```

---

### Step 3 — Write the story beats

**Beat 1 — What we set out to understand**
State the inertia position explicitly: the team's entering recommendation (from the
INERTIA VERDICT block) and the hypothesis behind it. This is not an abstract question —
it names the specific claim and verb the team committed to before gathering signals.

**Beat 2 — What each signal revealed** *(draws from the inertia ledger)*
For each ledger entry, one editorial sentence on what the finding added to or challenged
in the inertia verdict. Reference the stance explicitly. Two sentences maximum per signal.
CONFIRMS strengthens the inertia; MODIFIES adjusts the hypothesis the inertia rested on;
CONTRADICTS directly contests the inertia basis.

**Beat 3 — What the signals say together**
Open with the net mutation vector: "Across [N] signals, the inertia verdict was [vector]."
Then name the cross-signal pattern — the relationship, tension, or gap only visible across
the full ledger. Every non-trivial claim cites the anchor:
`(anchored: {artifact-name}, {stance})`.

For every tension between stances:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause.

The cross-signal pattern must be a relationship, tension, or gap — not a list of findings.
A Beat 3 claim derivable from any single ledger entry fails.

**Beat 4 — What remains uncertain**
UNRESOLVED verdict entries from Beat 3 become gaps here.

```
Gap: [what is unknown]
Most exposed claim: [which ledger entry's finding cannot be confirmed without resolving this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Beat 5 — Recommendation**

Before writing the recommendation paragraph, complete the inertia-to-final comparison:

```
Inertia verb: [from INERTIA VERDICT block]
Final verb: [PROCEED | PAUSE | PIVOT | ABANDON]
Verb held? YES | NO
[if YES]: What signals added beyond the prior: [what the signals contributed that the
  inertia basis alone did not contain — cite specific ledger entries]
[if NO]: What changed: [which signal(s) with which stance(s) shifted the verb and why]
```

Then write the recommendation paragraph:
- Names the final verb explicitly
- Opens with the pattern-to-recommendation bridge, independently stated:
  "Because [cross-signal pattern from Beat 3], [verb]."
  This bridge is required here — the inertia-to-final comparison above does not discharge it.
- If the verb matches INERTIA VERDICT: names what signal evidence added to the
  pre-existing basis (anti-stagnation satisfied by evidence addition, not verbal confirmation)
- If the verb changed: names the specific transition and what it implies for action
- Names what to do, under what conditions, with what scope

---

**Voice**: The INERTIA VERDICT reads as a committed prior. Beat 2 reads as a reckoning.
Beat 3 reads as the verdict on the verdict. Beat 5 reads as the evidence-tested conclusion.
The arc is measurable: entering commitment → signal challenge → evolved recommendation.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## INERTIA VERDICT
**[PROCEED | PAUSE | PIVOT | ABANDON]**
Entering hypothesis: [claim]
Inertia basis: [why this verb, now, before signals]

## Inertia Ledger
- `{artifact-name}`: {finding}
  Stance on inertia verdict: CONFIRMS | MODIFIES | CONTRADICTS
  [Verdict update or Challenge if applicable]
...
**Evolved hypothesis (S3)**: [claim]
**Net mutation vector**: {vector} — [mechanism sentence]
**Verdict evolution**: [held / weakened / strengthened / changed — mechanism]

**Inertia-to-final delta:**
Inertia: {original verb} — [inertia basis verbatim]
Final: {final verb} — [what changed or what signals added]

## Story

### Beat 1 — What we set out to understand
[Inertia position and entering hypothesis stated explicitly]

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the inertia verdict was [vector].
[cross-signal pattern — each claim with anchor citations]
[Conflict / Verdict / because-clause entries for each tension]

### Beat 4 — What remains uncertain
[Gap / Most exposed claim / Next signal entries]

### Beat 5 — Recommendation
Inertia verb: {verb} | Final verb: {verb} | Verb held? YES | NO
[What signals added (if held) or what changed (if shifted)]

**PROCEED | PAUSE | PIVOT | ABANDON**
Because [cross-signal pattern from Beat 3], [verb].
[Directive continuation — what to do, conditions, scope.]
```

---

## V-04

**Variation axis**: Combination — VERDICT block (C-28) + namespace enumeration as named
Step 1 sub-task (C-29 targeted) on R10 V-04 base (reconciliation table + 5-element
derivation chain)
**Hypothesis**: R10 V-04 was the strongest Round 10 performer, achieving C-17 through C-23
via the reconciliation table (C-20) and five-element derivation chain (adjacent verb +
conditions). C-28 and C-29 are both additive insertions that do not require structural
change to R10 V-04: C-28 is satisfied by placing VERDICT as a pre-gather block; C-29 is
partially addressed by adding namespace enumeration as a named Step 1 sub-task before
artifact reading. V-04 tests whether these minimal insertions on the R10 V-04 base are
sufficient — without full tri-role implementation — for C-28 and C-29. The key diagnostic:
if C-29 depends on C-26 (tri-role structure), V-04 will show a PARTIAL — the namespace
enumeration instruction will be present but the structural gate (EXTRACTOR as a named
role) will be missing. If the named sub-step is sufficient for C-29's pass condition,
V-04 demonstrates the additive approach. The R10 V-04 mechanisms for C-22, C-23, and
C-20 remain intact — this is the minimum-change upgrade to the proven base.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### VERDICT *(complete before proceeding)*

Before reading any signal artifact, state your recommendation.

```
VERDICT: [PROCEED | PAUSE | PIVOT | ABANDON]
Basis: [one sentence — the specific claim or prior posture that licenses this verdict]
```

The VERDICT is an independently-stated decision. Not conditional. Not a placeholder.
The VERDICT and Beat 5 are independent placements — both required. "TBD pending signals"
fails. Do not begin Step 1 until the VERDICT is declared.

---

### Step 1 — Gather and Namespace Enumeration

**Step 1a — Namespace enumeration** *(complete before artifact reading)*

Before reading any artifact, list the signal namespaces expected for this topic based on
available context. After reading, verify and update.

```
Namespaces found:
1. {namespace} — {N} artifacts
2. {namespace} — {N} artifacts
...
Total distinct namespaces: {N}
Missing namespaces (if any): [which namespaces have no artifacts — note as coverage gaps]
```

Minimum: 3 distinct namespaces. If fewer than 3, flag the gap explicitly.
This enumeration is a required deliverable — not an authorial option. It appears in the
artifact before ledger work begins.

**Step 1b — Gather**

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

Before writing the story, complete the ledger.

**Working hypothesis (S0)**: [one sentence — falsifiable assertion, not a goal or question]

For each signal artifact:

```
- `{artifact-name}`: {key finding most relevant to the hypothesis, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [evolved working hypothesis]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[mechanism sentence — cite at least one artifact by name]
```

**Anti-stagnation check**: If S3 is identical to S0, state why explicitly.

---

### Step 2b — Vector-verdict reconciliation table

Complete immediately after declaring the net mutation vector. One row per ledger entry.

```
| Signal | Verdict type | Consistent with declared vector? |
|--------|-------------|----------------------------------|
| {artifact-name} | CONFIRMS — {dimension} | YES |
| {artifact-name} | MODIFIES toward {dimension} | YES |
| {artifact-name} | CONTRADICTS on {dimension} — RESOLVED | YES (resolved) |
| {artifact-name} | CONTRADICTS on {dimension} — UNRESOLVED | CONFLICT |
```

**Consistency rules:**
- **CONFIRMED**: all CONTRADICTS must be RESOLVED. UNRESOLVED CONTRADICTS → CONFLICT row
  → revise vector to QUALIFIED or resolve the contradiction in Beat 3.
- **QUALIFIED**: CONFIRMS/MODIFIES expected; CONTRADICTS only if RESOLVED.
- **REVERSED**: majority evidential weight in CONTRADICTS or reversing MODIFIES.
- **REDIRECTED**: entries answer a different frame than S0 posed.

After the table:

```
Reconciliation: Vector is consistent — [reason]
```

OR:

```
Reconciliation: Vector revised from [X] to [Y] — [CONFLICT entry and revision reason]
```

Do not begin story beats until ledger, vector, reconciliation table, and conclusion
are all complete.

---

### Step 3 — Write the story beats

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. The
entering default: what the team expected to confirm and why.

**Beat 2 — What each signal revealed** *(draws from the ledger)*
For each ledger entry, one editorial sentence on what the finding means for the hypothesis.
Two sentences maximum per signal.

**Beat 3 — What the signals say together**
Open with the reconciled net mutation vector:
"Across [N] signals, the hypothesis was [CONFIRMED / QUALIFIED / REVERSED / REDIRECTED]."

**Anchor citation rule**: Every non-trivial claim in Beat 3 must cite:
`(anchored: {artifact-name}, {stance})`. MODIFIES entries anchor synthesis claims.
CONFIRMS entries anchor validation claims. CONTRADICTS entries anchor adjudication verdicts.

For every tension between stances (any CONFLICT row in the reconciliation table must
appear as an explicit Conflict/Verdict entry):

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason — name the
         element from that signal's ledger entry that outweighs the alternative]
     OR: UNRESOLVED because [what {namespace}/{skill} would provide the missing evidence]
```

Every verdict carries a because-clause.

Falsifiability test: does any single ledger entry contain the Beat 3 conclusion? If yes,
revisit — verify anchor citations span multiple entries.

**Beat 4 — What remains uncertain**
UNRESOLVED verdicts become gaps. RESOLVED verdicts are not gaps.

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [expected finding type]
```

**Beat 4.5 — Derivation chain** *(written before Beat 5)*

Five elements, each on its own line:

```
Anchored claim: "[exact S3 claim from Beat 3, verbatim with anchor citation]"
  (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence,
  verbatim from ledger — must match reconciliation table declaration exactly]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what in the
  vector and gap profile licenses this specific verb]
Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what specific element
  of the signal evidence, verdict distribution, or net vector value would have to differ for
  this adjacent verb to apply — name the exact claim a reader who prefers it must contest]
Conditions: [evidence-state parameter — one of: CONTRADICTS count / gap-closure cost /
  risk tolerance threshold / readiness signal distribution — stated as a specific value,
  not a contextual placeholder]
```

Adjacent pairs: PROCEED ↔ PAUSE (confidence), PAUSE ↔ PIVOT (commitment),
PIVOT ↔ ABANDON (recovery).

A conditions line filled with "under current conditions" or "in this context" fails.

Do not write Beat 5 until all five elements are internally consistent.

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** (must match Beat 4.5 verb).

Opens with the pattern-to-recommendation bridge — independently placed, not carried
from Beat 4.5:
"Because [named cross-signal pattern from Beat 3], [verb]."

One paragraph total: what to do, under what conditions, with what scope.
If Beat 5 verb differs from VERDICT declared before Step 1: name the revision reason.
"Proceed with caution" without naming the specific caution fails.

---

**Voice**: Active, opinionated. The VERDICT reads as a prior commitment. The namespace
enumeration establishes the evidence base. The reconciliation table verifies the vector.
The derivation chain provides three contestation points. Beat 5 delivers the directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## VERDICT
**[PROCEED | PAUSE | PIVOT | ABANDON]**
Basis: [one sentence]

## Namespace Enumeration
1. {namespace} — {N} artifacts
...
Total distinct namespaces: {N}
Missing: [or "none"]

## Hypothesis Mutation Ledger
**Working hypothesis (S0)**: [claim]

- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} — [mechanism sentence]

## Vector-Verdict Reconciliation
| Signal | Verdict type | Consistent? |
|--------|-------------|-------------|
...
**Reconciliation**: [consistent or revised statement]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector].
[cross-signal pattern with anchor citations]
[Conflict / Verdict / because-clause entries]

### Beat 4 — What remains uncertain
[Gap / Most exposed finding / Next signal entries]

### Beat 4.5 — Derivation chain
Anchored claim: "[verbatim S3 claim]" (anchored: {artifact-name}, {stance})
Net vector: {vector} — [mechanism sentence]
Recommendation verb: {VERB} — [licensing sentence]
Adjacent verb: {ADJACENT-VERB} — [contestation claim]
Conditions: [named evidence-state parameter — specific value]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON**
Because [named pattern from Beat 3], [verb]. [Directive continuation.]
```

---

## V-05

**Variation axis**: Full combination — tri-role EXTRACTOR/ANALYST/AUTHOR (C-24, C-26)
+ VERDICT preview (C-28) + namespace enumeration in EXTRACTOR (C-29) + reconciliation
table and 5-element derivation chain in ANALYST (C-20, C-22, C-23) + terminal
verification checklist (C-25)
**Hypothesis**: V-02 introduces the tri-role structure and satisfies C-24, C-26, C-28,
C-29. R10 V-04 adds the reconciliation table (C-20) and five-element derivation chain
(C-22, C-23). V-05 combines both: EXTRACTOR produces namespace enumeration and signal
digests; ANALYST produces the hypothesis mutation chain, reconciliation table, pattern
block, delta, posture, and full five-element derivation pre-work (with adjacent verb and
conditions); AUTHOR writes the five beats with an independent bridge sentence in Beat 5.
A terminal verification checklist (C-25) gates submission. Non-substitution is explicitly
stated for Beat 5's bridge sentence (C-27). The reconciliation table in ANALYST provides
the verified vector against which ANALYST's adjacent-verb contrast and conditions clause
operate — AUTHOR cannot revise the vector after ANALYST's reconciliation is complete,
so the contestation claims (C-22) and conditions mapping (C-23) address a fixed,
auditable record. This is the maximum-structure variation — it tests whether the full
architecture achieves consistent compliance across C-20, C-22, C-23, C-24, C-25, C-26,
C-27, C-28, C-29 simultaneously.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### VERDICT *(complete before any role begins)*

```
VERDICT: [PROCEED | PAUSE | PIVOT | ABANDON]
Basis: [one sentence — the entering claim or posture that warrants this recommendation]
```

Independently stated. Not conditional. Not a forward reference.
VERDICT and Beat 5 are independent placements — both required.
Do not begin EXTRACTOR work until the VERDICT is declared.

---

## ROLE: EXTRACTOR

*Reads signal artifacts. Produces two outputs. Does not synthesize or draw cross-signal
conclusions. ANALYST may not begin until both outputs are marked COMPLETE.*

### EXTRACTOR Output 1 — Namespace Enumeration

Glob `simulations/**/{topic}-*`. Also check `simulations/{topic}/strategy.md`.

Before reading any artifact, list the signal namespaces expected for this topic.
After reading, verify and update.

```
Namespaces represented:
1. {namespace} — {N} artifacts: [{artifact names}]
2. {namespace} — {N} artifacts: [{artifact names}]
...
Total distinct namespaces: {N}
Coverage gap (if any): [namespaces expected but absent — one sentence on impact]
```

Minimum: 3 distinct namespaces. If fewer than 3: flag as coverage gap.

This is a required EXTRACTOR deliverable. C-05's three-namespace minimum is structurally
enforced here — ANALYST does not have discretion to skip or defer this check.

### EXTRACTOR Output 2 — Signal Digests

Read every artifact found. For each, in gather order:

```
- `{artifact-name}` [{namespace}]: {key finding — one to two sentences, stated as fact}
  Hypothesis relevance: {one sentence — how this finding bears on the working hypothesis}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Candidate hypothesis update: [previous claim] → [proposed update]
```

Rules:
- One entry per artifact, in gather order. No thematic grouping.
- Every entry gets a stance. EXTRACTOR does not resolve conflicts.
- EXTRACTOR does not state patterns or draw synthesis conclusions.

**EXTRACTOR COMPLETE** — ANALYST may now begin.

---

## ROLE: ANALYST

*Reads EXTRACTOR outputs only. Does not re-read original signal artifacts. Produces four
outputs. AUTHOR may not begin until all four outputs are marked COMPLETE.*

### ANALYST Output 1 — Hypothesis Mutation Chain

**Working hypothesis (S0)**: [one sentence — falsifiable assertion derived from digest set
and strategy.md. Not a goal or question. A specific claim that could be proven wrong.]

Apply EXTRACTOR stance entries in artifact order:

```
- `{artifact-name}`: {stance from EXTRACTOR digest}
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [evolved hypothesis after all modifications]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
Mechanism: [one sentence — which stances and on which dimension, citing at least one
  artifact by name]
```

**Anti-stagnation check**: S3 identical to S0 → state explicitly why. Silently fails.

### ANALYST Output 2 — Vector-Verdict Reconciliation Table

One row per EXTRACTOR digest entry. Complete immediately after declaring the net vector.

```
| Signal | Verdict type | Consistent with declared vector? |
|--------|-------------|----------------------------------|
| {artifact-name} | CONFIRMS — {dimension from digest} | YES |
| {artifact-name} | MODIFIES toward {dimension} | YES |
| {artifact-name} | CONTRADICTS on {dimension} — RESOLVED | YES (resolved) |
| {artifact-name} | CONTRADICTS on {dimension} — UNRESOLVED | CONFLICT |
```

Consistency rules:
- **CONFIRMED**: all CONTRADICTS must be RESOLVED. UNRESOLVED → CONFLICT → revise vector.
- **QUALIFIED**: CONFIRMS/MODIFIES; CONTRADICTS only if RESOLVED.
- **REVERSED**: majority evidential weight in CONTRADICTS or reversing MODIFIES.
- **REDIRECTED**: entries answer a different frame than S0 posed.

```
Reconciliation: Vector is consistent — [reason]
```
OR:
```
Reconciliation: Vector revised from [X] to [Y] — [CONFLICT entry and revision reason]
```

### ANALYST Output 3 — Pattern Block and Delta

**Pattern block** *(discrete, self-contained, labeled)*:

```
PATTERN: [one to three sentences — the relationship, tension, or gap across signals that
no single signal shows alone. Must reference at least two EXTRACTOR digest entries by
artifact name. Must be a synthetic claim — not a side-by-side summary.]
(anchored: {artifact-name-1}, {stance}) and ({artifact-name-2}, {stance})
```

Falsifiability test: does any single EXTRACTOR digest entry contain this entire pattern?
If yes, the claim is not cross-signal — revise.

**Delta block**:

```
DELTA:
S0 (entering): [S0 hypothesis verbatim]
Key signal shift: {artifact-name} — {stance} — [what this entry changed]
S3 (evolved): [S3 hypothesis verbatim]
Mutation: [one sentence — what specifically changed and why it matters for the decision]
```

Anti-stagnation: "Signals confirmed the prior" without a named confidence gain fails.

### ANALYST Output 4 — Evidence Posture and Full Derivation Pre-Work

```
Evidence posture: STRONG POSITIVE | MIXED | CONFLICTING | WEAK
[one sentence: share or weight of signals supporting the core hypothesis claim]

Anchored claim: "[exact S3 claim from Pattern block, verbatim]"
  (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence,
  verbatim from Output 1 — must match reconciliation table declaration exactly]

Recommendation verb (pre-committed): {PROCEED | PAUSE | PIVOT | ABANDON}
[one sentence: what in the vector and gap profile licenses this specific verb]

Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON}
[one sentence: what specific element — stance count, gap profile, or vector property —
would have to differ for the adjacent verb to apply. Name the exact contestable claim.]

Conditions: [evidence-state parameter — one of: CONTRADICTS count / gap-closure cost /
  risk tolerance threshold / readiness signal distribution — stated as a specific value,
  not a contextual placeholder or vector restatement]
```

Adjacent pairs: PROCEED ↔ PAUSE (confidence), PAUSE ↔ PIVOT (commitment),
PIVOT ↔ ABANDON (recovery).

Permitted conditions categories:
1. Count of unresolved CONTRADICTS and threshold implication
2. Gap-closure cost and timing implication
3. Risk tolerance threshold and which side the current evidence sits
4. Share of signals confirming the core hypothesis and what that distribution implies

Conditions line examples that fail: "under current conditions" / "given this context" /
"QUALIFIED means pause in this situation" — opaque, no specific claim to contest.

**ANALYST COMPLETE** — AUTHOR may now begin.

---

## ROLE: AUTHOR

*Reads ANALYST outputs only. Does not re-read EXTRACTOR digests or original artifacts.
Writes the five narrative beats and the independent recommendation paragraph.*

If any ANALYST output is missing or incomplete, return to ANALYST — do not proceed.

### Beat 1 — What we set out to understand
One to three sentences. The S0 hypothesis as a falsifiable claim. The entering default
and why it was the reasonable prior.

### Beat 2 — What each signal revealed *(draws from ANALYST Output 1 mutation chain)*
For each ledger entry, one editorial sentence on what the finding means for the hypothesis.
Two sentences maximum per signal.

### Beat 3 — What the signals say together
Open with the reconciled net mutation vector: "Across [N] signals, the hypothesis was [vector]."
Cite the PATTERN block from ANALYST Output 3. Every non-trivial claim carries an anchor:
`(anchored: {artifact-name}, {stance})`.

For every CONFLICT row in ANALYST Output 2, write a Conflict/Verdict entry:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause.

### Beat 4 — What remains uncertain
UNRESOLVED verdicts from Beat 3 become gaps. RESOLVED verdicts are not gaps.

```
Gap: [what is unknown]
Most exposed finding: [which artifact's claim is unverifiable without this]
Next signal: {namespace}/{skill} — [expected finding type]
```

### Beat 5 — Recommendation

**Non-substitution rule — Beat 5 specific**: The pattern-to-recommendation bridge
sentence required in Beat 5 is an independently-placed requirement. ANALYST Output 4
pre-commits the recommendation verb — that pre-commitment does not discharge the bridge
sentence required here. Even if content-equivalent to a sentence in ANALYST Output 4,
the bridge must appear in Beat 5 as an original statement, not a reference or copy.

Beat 5 bridge sentence — first or second sentence of the paragraph:
"Because [named cross-signal pattern from Beat 3], [verb]."

One of: **proceed**, **pause**, **pivot**, **abandon** (must match ANALYST Output 4 verb).
One paragraph: what to do, under what conditions, with what scope.
If Beat 5 verb differs from VERDICT declared before EXTRACTOR: name the revision reason.
"Proceed with caution" without naming the specific caution fails.

---

## TERMINAL VERIFICATION CHECKLIST

*Complete this checklist before submitting. Each item is a binary pass/fail. Mark each.
An unmarked checklist item is not a completed verification — it is an empty declaration.
Do not submit until every item is marked.*

```
[ ] VERDICT block present before EXTRACTOR section
[ ] VERDICT is declarative — no conditionals or forward references
[ ] EXTRACTOR Output 1 (Namespace Enumeration) present and appears before ANALYST begins
[ ] Distinct namespace count >= 3 (or coverage gap explicitly flagged)
[ ] EXTRACTOR COMPLETE marker present before ANALYST section begins
[ ] ANALYST COMPLETE marker present before AUTHOR (Story) section begins
[ ] S0 is a falsifiable assertion — not a goal or question
[ ] S3 differs from S0 in a named way, or anti-stagnation explicitly explained
[ ] Reconciliation table present with one row per EXTRACTOR digest entry
[ ] Every CONFLICT row resolved or explicitly flagged — none silently passed to AUTHOR
[ ] PATTERN block is discrete, labeled, and self-contained
[ ] PATTERN block references at least two artifacts by name
[ ] DELTA block present with S0, key signal shift, S3, and mutation sentence
[ ] Evidence posture named in ANALYST Output 4 with specific basis sentence
[ ] Adjacent verb named with specific contestation claim — not a rationale for chosen verb
[ ] Conditions slot filled with named evidence-state parameter — specific value, not placeholder
[ ] Beat 1 states S0 as a falsifiable claim
[ ] Beat 3 opens with net mutation vector declaration
[ ] Every non-trivial Beat 3 claim has an anchor citation
[ ] Beat 3 cross-signal pattern is synthetic — not derivable from any single artifact
[ ] Beat 4 gaps are UNRESOLVED verdicts — RESOLVED verdicts are not listed as gaps
[ ] Beat 5 opens with independent bridge sentence in required format
[ ] Beat 5 verb matches ANALYST Output 4 pre-committed verb and VERDICT (or revision named)
[ ] Beat 5 recommendation names what to do, under what conditions, with what scope
```

---

**Voice**: EXTRACTOR records without judgment. ANALYST reasons without narrating.
AUTHOR advocates without re-deriving. Three distinct voices, one-way flow,
terminal verification before release.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## VERDICT
**[PROCEED | PAUSE | PIVOT | ABANDON]**
Basis: [one sentence]

---

## EXTRACTOR

### Namespace Enumeration
1. {namespace} — {N} artifacts: [names]
...
Total distinct namespaces: {N}
Coverage gap: [or "none"]

### Signal Digests
- `{artifact-name}` [{namespace}]: {finding}
  Hypothesis relevance: {relevance}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [Candidate hypothesis update if MODIFIES]
...

**EXTRACTOR COMPLETE**

---

## ANALYST

### Hypothesis Mutation Chain
**S0**: [claim]
- `{artifact-name}`: {stance}
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} — [mechanism sentence]

### Vector-Verdict Reconciliation
| Signal | Verdict type | Consistent? |
|--------|-------------|-------------|
...
**Reconciliation**: [consistent or revised]

### Pattern Block
PATTERN: [synthetic cross-signal claim]
(anchored: {artifact-name-1}, {stance}) and ({artifact-name-2}, {stance})

### Delta Block
DELTA:
S0 (entering): [verbatim]
Key signal shift: {artifact-name} — {stance} — [change]
S3 (evolved): [verbatim]
Mutation: [what changed and why it matters]

### Evidence Posture and Derivation Pre-Work
Evidence posture: {posture} — [basis]
Anchored claim: "[verbatim S3 claim]" (anchored: {artifact-name}, {stance})
Net vector: {vector} — [mechanism verbatim]
Recommendation verb (pre-committed): {VERB} — [licensing sentence]
Adjacent verb: {ADJACENT-VERB} — [contestation claim]
Conditions: [named evidence-state parameter — specific value]

**ANALYST COMPLETE**

---

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector].
PATTERN: [cited from ANALYST — cross-signal claim with anchor citations]
[Conflict / Verdict / because-clause entries for each CONFLICT row]

### Beat 4 — What remains uncertain
[Gap / Most exposed finding / Next signal entries]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON**
Because [named cross-signal pattern from Beat 3], [verb].
[Directive continuation — what to do, under what conditions, with what scope.]

---

## Terminal Verification Checklist
[ ] VERDICT block present before EXTRACTOR...
[all 24 items, each marked YES or reason if NO]
```
