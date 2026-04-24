## `/quest:variate` — `topic-story` Round 10

**New criteria driving variation:** C-26 (tri-role EXTRACTOR/ANALYST/AUTHOR gate), C-27 (Beat 5 bridge independence).

**Three single-axis variations:** V-01 role sequence, V-02 output format, V-03 lifecycle emphasis.
**Two combination variations:** V-04 (role sequence + inertia framing), V-05 (output format + non-substitution explicitness).

---

## V-01 — Role Sequence Axis

**Hypothesis:** Making the three-role gate the primary structural spine — with explicit completion markers and one-directional transitions — will satisfy C-26 and C-27 while the role boundary architecture passively enforces C-18, C-24, and C-19 without separate instruction.

---

You are producing a `topic-story` artifact — an editorial synthesis that tells decision-makers what the signals say together. This is not a summary of each signal. It is a synthesis in the author's voice.

The output is produced in three sequential roles. Each role must complete its work before the next role begins. This is a one-way gate. No role may begin until the role before it is marked COMPLETE.

---

### ROLE 1: EXTRACTOR

**What you do:** Read each signal artifact available for this topic. Produce a signal digest — one entry per artifact. Do not analyze. Do not synthesize. Do not write narrative. Record only: what artifact, what it contains, what it asserts.

**Completion gate:** You may not begin ROLE 2 until the signal digest is complete and marked `[EXTRACTOR COMPLETE]`.

**Output format:**

```
[EXTRACTOR BLOCK]
- Artifact: {name/type}
  Contains: {one-sentence description of what it is}
  Asserts: {the single strongest claim this artifact makes}
...
[EXTRACTOR COMPLETE]
```

---

### ROLE 2: ANALYST

**What you do:** Read the EXTRACTOR BLOCK only — not the raw artifacts. Produce four analytic outputs in order. You may not begin ROLE 3 until all four are marked COMPLETE.

**Output 2A — Falsifiable Hypothesis (S0 Baseline)**

State the hypothesis that motivated this investigation as a falsifiable claim — a proposition the signals can confirm, refute, or modify. Format: *"Our hypothesis: [specific claim that could be wrong]."* A vague intent ("we set out to understand X") is not a hypothesis.

```
[ANALYST BLOCK A — S0 HYPOTHESIS]
Our hypothesis: ...
[BLOCK A COMPLETE]
```

**Output 2B — S0→S3 Delta**

State what the signals changed about the S0 hypothesis. This is a contrast: what you believed before vs. what the signals revealed. Format: *"We expected [S0 claim]. The signals [confirmed / refuted / modified] this: [what changed]."* Delta must name a direction — confidence shift, verb shift, or scope shift. S0 = S3 is a failure regardless of framing.

```
[ANALYST BLOCK B — DELTA]
We expected: ...
The signals revealed: ...
The delta: ... [name the shift]
[BLOCK B COMPLETE]
```

**Output 2C — Cross-Signal Pattern**

State the cross-signal pattern as a discrete, self-contained claim. This claim must: (1) reference what two or more signals show together that no single signal shows alone; (2) name a relationship, tension, or gap — not a list of findings; (3) be readable without the surrounding narrative.

```
[ANALYST BLOCK C — PATTERN]
The pattern: ...
[BLOCK C COMPLETE]
```

**Output 2D — Evidence Posture**

Name the overall signal posture from the set: strong positive / mixed / conflicting / weak / negative. Then state the recommendation verb that this posture produces: proceed / pause / pivot / abandon. This is a direct derivation — the posture causes the verb.

```
[ANALYST BLOCK D — POSTURE AND VERB]
Evidence posture: ...
Recommendation verb: ... [because: ...]
[BLOCK D COMPLETE]
[ANALYST COMPLETE]
```

---

### ROLE 3: AUTHOR

**What you do:** Read the ANALYST COMPLETE blocks only. Write the five narrative beats. You are translating analytic outputs into editorial prose — not re-deriving them.

**Structural rules before you begin:**

- Beat 1 opens with the S0 hypothesis from Block A, stated as a falsifiable claim.
- Beat 3 states the cross-signal pattern from Block C as a discrete, labeled sentence: *"The pattern: ..."* This sentence must be independently readable. It may not exist only embedded in surrounding prose.
- Beat 5 opens with the recommendation verb from Block D. Beat 5 must include: (a) an evidence-posture statement naming the posture that produced the verb; (b) a bridge sentence naming the cross-signal pattern as the stated reason for the verb. **This bridge sentence is independently required in Beat 5. The bridge sentence in Block C does not satisfy it. You must write it again here, in Beat 5, as a distinct placement.**

**Non-substitution rule:** Any claim required in a Beat — pattern statement, bridge sentence, posture statement — must be produced independently in that Beat. A claim produced in an analytic block does not discharge its Beat-level placement requirement, even if the content is identical.

---

**BEAT 1 — What we set out to understand**

State the falsifiable hypothesis that framed the investigation. State what a confirm, refute, or modification of that hypothesis would mean for the decision. One to two paragraphs.

**BEAT 2 — What the signals revealed**

For each signal type or namespace represented in the EXTRACTOR BLOCK, state one key finding — the single strongest claim that artifact contributed. This is not exhaustive enumeration. Limit to what the synthesis requires.

**BEAT 3 — What the signals say together**

Lead with the labeled pattern sentence: *"The pattern: ..."* Then develop the pattern claim in two to four sentences. Explain what relationship, tension, or gap the pattern names and why no single signal alone reveals it.

**BEAT 4 — What remains uncertain**

Name at least one open question that, if resolved, would change the recommendation verb or its confidence. For each uncertainty item, state the direction: *"If [X] resolves to [Y], this moves from [current verb] to [alternative verb]."* Generic hedges without a named direction fail.

**BEAT 5 — The recommendation**

Open with the recommendation verb. State the evidence posture that produced it. Include the bridge sentence: *"Because [name the cross-signal pattern], the recommendation is [verb]."* This sentence is independently placed here. Address the decision context — name or clearly imply who is making the decision and under what constraint.

If the recommendation verb contradicts any prior-stage verdict, name the override reason explicitly. Silent contradiction is a correctness failure.

---

### TERMINAL VERIFICATION CHECKLIST

Complete this checklist before submitting. Mark each item. This is a gate, not an appendix.

```
[ ] EXTRACTOR BLOCK is present and marked COMPLETE
[ ] ANALYST BLOCK A (S0 hypothesis) is present — stated as a falsifiable claim
[ ] ANALYST BLOCK B (Delta) names a direction — S0 ≠ S3
[ ] ANALYST BLOCK C (Pattern) is self-contained and readable without surrounding prose
[ ] ANALYST BLOCK D (Posture and Verb) names posture and derives verb from it
[ ] ANALYST COMPLETE marker is present
[ ] Beat 1 opens with the falsifiable hypothesis from Block A
[ ] Beat 3 contains the labeled "The pattern: ..." sentence, independently readable
[ ] Beat 5 opens with the recommendation verb
[ ] Beat 5 contains the evidence-posture statement
[ ] Beat 5 contains the bridge sentence naming the pattern as the reason for the verb
[ ] Beat 5 bridge sentence is independently produced — not copied from Block C
[ ] Beat 4 names at least one uncertainty with a direction (moves from X to Y)
[ ] No silent contradiction between recommendation verb and any prior verdict
[ ] All five beats are present with original labels
```

---

## V-02 — Output Format Axis

**Hypothesis:** Organizing the entire output around named, labeled blocks with explicit header conventions — rather than role sequencing as the primary principle — makes pre-composition artifacts structurally self-evident and reduces the cognitive load of maintaining role separation, while still satisfying C-26 by naming the three-role mapping inside each block header.

---

You are producing a `topic-story` artifact. This artifact has two parts:

- **Part 1 — Analytic Pre-Composition**: Three labeled blocks produced before any narrative is written. These blocks are the evidence that the story was synthesized, not written from memory.
- **Part 2 — Narrative Beats**: Five editorial beats written from Part 1 outputs only.

You must complete all of Part 1 before beginning Part 2.

---

### PART 1 — ANALYTIC PRE-COMPOSITION

**Block 1 of 3: Signal Digest** *(EXTRACTOR role)*

Read all available signal artifacts for this topic. For each artifact, record:

| Artifact | Type | Strongest claim |
|----------|------|-----------------|
| ... | ... | ... |

Do not analyze here. Do not write synthesis. Do not interpret. Record only what each artifact asserts.

Mark complete: `[SIGNAL DIGEST COMPLETE]`

---

**Block 2 of 3: Synthesis Analysis** *(ANALYST role — reads Block 1 only)*

Using the Signal Digest above — not the raw artifacts — produce three analytic outputs.

**2A. Falsifiable Hypothesis (S0)**

*"Our hypothesis entering this investigation: [specific claim that the signals could confirm, refute, or modify]."*

State as a proposition that could be wrong. A vague intent statement fails.

**2B. S0→S3 Delta**

*"We expected [S0 claim]. The signals [confirmed / refuted / modified] this because [specific evidence]."*

Name the shift explicitly: confidence level, direction of recommendation, or scope of the claim. S0 = S3 is a failure.

**2C. Cross-Signal Pattern**

> **The pattern:** [a single, complete sentence stating what two or more signals reveal together that no single signal reveals alone — a named relationship, tension, or gap]

This block must be self-contained. A reader must understand the full pattern claim without reading the surrounding document.

**2D. Evidence Posture and Verb**

| Dimension | Value |
|-----------|-------|
| Signal posture | strong positive / mixed / conflicting / weak / negative |
| Recommendation verb | proceed / pause / pivot / abandon |
| Derivation | [one sentence: posture → verb, citing the pattern] |

Mark complete: `[SYNTHESIS ANALYSIS COMPLETE]`

---

**Block 3 of 3: Uncertainty Register** *(ANALYST role)*

List open questions whose resolution would shift the recommendation. For each:

| Uncertainty | If resolves to | Verb moves from → to |
|-------------|---------------|----------------------|
| ... | ... | [current verb] → [alternative] |

Minimum one entry. Generic hedges without a named direction fail.

Mark complete: `[UNCERTAINTY REGISTER COMPLETE]`

---

### PART 2 — NARRATIVE BEATS

*Written by AUTHOR role, reading Part 1 blocks only.*

**Non-substitution rule:** Every claim required in a Beat must be independently produced in that Beat. A claim present in Part 1 does not satisfy its Beat-level placement. You must re-state it in the Beat.

---

**Beat 1 — What we set out to understand**

Open with the S0 hypothesis from Block 2A, stated as a falsifiable claim. Explain what a confirmation, refutation, or modification of that hypothesis would mean for the feature decision.

**Beat 2 — What the signals revealed**

For each artifact type in the Signal Digest, state one key finding — the claim that artifact contributed to the synthesis. This is selective, not exhaustive. Include only what the pattern requires to be credible.

**Beat 3 — What the signals say together**

Lead with the labeled pattern sentence from Block 2C, reproduced verbatim:

> **The pattern:** [from Block 2C]

Then develop the claim in two to four sentences. Explain the relationship, tension, or gap and why no single signal alone would surface it.

**Beat 4 — What remains uncertain**

Present the uncertainty register from Block 3, narrated. Each item must state what resolving it would change about the verb or confidence.

**Beat 5 — The recommendation**

Open with the recommendation verb. Include in this beat:

1. **Evidence posture statement:** Name the signal posture from Block 2D as the direct basis for the verb.
2. **Bridge sentence:** *"Because [name the cross-signal pattern from Block 2C], the recommendation is [verb]."* — This sentence is required here independently. It is not discharged by Block 2C or Beat 3.
3. **Decision context:** Name or clearly imply who is making the decision and under what constraint.

If the verb contradicts any prior-stage determination, name the override reason.

---

### TERMINAL VERIFICATION

```
[ ] Block 1 (Signal Digest) complete — artifact-by-artifact, no analysis
[ ] Block 2 (Synthesis Analysis) complete — hypothesis, delta, pattern, posture all present
[ ] Block 3 (Uncertainty Register) complete — each item has a verb-shift direction
[ ] Part 2 begins only after all Part 1 blocks are marked COMPLETE
[ ] Beat 3 leads with the labeled "The pattern:" sentence — self-contained
[ ] Beat 5 contains independently produced posture statement, bridge sentence, decision context
[ ] Beat 5 bridge sentence is not a copy-forward of Block 2C — independently written
[ ] Delta (Block 2B) names a direction — S0 ≠ S3
[ ] All five beats present with original labels
[ ] No silent contradiction between verb and any prior determination
```

---

## V-03 — Lifecycle Emphasis Axis

**Hypothesis:** Spending more instructional space on the pre-composition phase — particularly on making the falsifiable hypothesis and S0→S3 delta the spine of the investigation framing — and keeping narrative beat instructions minimal will strengthen C-21 and C-22 without over-constraining prose quality.

---

You are producing a `topic-story` artifact. The story synthesizes signals into editorial prose. Before writing a single word of narrative, you complete an analytic preparation sequence. The quality of the story depends entirely on the quality of the preparation.

---

### PREPARATION SEQUENCE

The preparation sequence has three stages and three roles. Each stage gates the next. Work through them in order.

---

**Stage P1 — Signal Extraction** *(EXTRACTOR)*

Purpose: Make explicit what evidence exists before any interpretation begins.

Read every signal artifact available for this topic. For each artifact, record:
- What kind of artifact it is (namespace, signal type)
- The single strongest claim it makes

Do not interpret. Do not relate artifacts to each other. Do not draw conclusions. Extract only.

When all artifacts are recorded, write: `[P1 COMPLETE — N artifacts extracted]`

---

**Stage P2 — Hypothesis and Delta** *(ANALYST — reads P1 output only)*

Purpose: Establish the measurable inertia baseline and compute what the signals shifted.

**P2a. State the S0 hypothesis as a falsifiable claim.**

This is the proposition you entered the investigation with — the belief that the signals were collected to test. A vague intent ("we set out to understand X") is not a hypothesis. A falsifiable hypothesis is a claim that could be wrong: *"We believed X"* or *"Our hypothesis: X holds."*

Write it now. It becomes your inertia baseline — the anchor against which the delta is measured.

**P2b. Compute the S0→S3 delta.**

What did the signals change about the S0 hypothesis? Work through the P1 extraction list. For each artifact, ask: does this confirm, refute, or modify the S0 claim? What is the cumulative effect?

Then state the delta explicitly:
- *We expected:* [S0 claim]
- *The signals showed:* [what the evidence actually says]
- *The shift:* [name the mutation — confidence direction, recommendation verb, or scope]

The delta must name a direction. If the signals simply confirmed the hypothesis, name how confidence changed even if direction did not. S0 = S3 with no mutation is a preparation failure.

**P2c. Assign anti-stagnation check.**

Confirm that the delta you named could not have been written before reading the signals. If the shift statement could have been written as a prior assumption, revise until it names something the signals specifically changed.

Write: `[P2 COMPLETE]`

---

**Stage P3 — Pattern, Posture, and Uncertainty** *(ANALYST — reads P1 and P2 outputs only)*

Purpose: Produce the three analytic claims the Author will use to write the narrative.

**P3a. Cross-signal pattern.**

State what two or more signals reveal together that no single signal reveals alone. This must be a named relationship, tension, or gap — not a list of findings. Write it as a standalone sentence that conveys the full claim without context.

> The pattern: [complete, self-contained claim]

**P3b. Evidence posture and recommendation verb.**

Name the overall signal posture across the extracted artifacts: strong positive / mixed / conflicting / weak / negative. Then derive the recommendation verb: proceed / pause / pivot / abandon. State the derivation in one sentence: the posture produces the verb because of [the pattern].

**P3c. Uncertainty register.**

List open questions whose resolution would shift the recommendation. For each, name: the question, what it would resolve to in order to shift the verb, and which direction the verb would move. Minimum one item.

Write: `[P3 COMPLETE]`

---

### NARRATIVE BEATS

*(AUTHOR — reads P3 outputs only)*

Write five beats. The beats are translation, not analysis — you are rendering the P3 analytic outputs into editorial prose. The preparation sequence already did the intellectual work.

**Required structural commitments:**

- Beat 1 must open with the falsifiable S0 hypothesis from P2a.
- Beat 3 must lead with the labeled pattern sentence from P3a, verbatim: *"The pattern: ..."*
- Beat 5 must open with the verb from P3b. Beat 5 must contain: an evidence posture statement citing P3b's posture, and a bridge sentence naming the pattern as the reason for the verb. **This bridge sentence is independently required in Beat 5. The pattern statement in Beat 3 or P3a does not satisfy it. Write it here, as a Beat 5 commitment.**
- If any beat-level claim contradicts a preparation-stage determination, name the override reason.

**Non-substitution:** Preparation-stage claims do not discharge their Beat-level placements. Each Beat placement is independently required.

---

**Beat 1 — What we set out to understand**
**Beat 2 — What the signals revealed**
**Beat 3 — What the signals say together**
**Beat 4 — What remains uncertain**
**Beat 5 — The recommendation**

---

### TERMINAL VERIFICATION

```
[ ] P1 complete — N artifacts extracted, extraction only (no interpretation)
[ ] P2a — S0 hypothesis is falsifiable, not a vague intent
[ ] P2b — Delta names a direction; S0 ≠ S3
[ ] P2c — Anti-stagnation check passed; delta could not have been pre-written
[ ] P3a — Pattern is a self-contained, standalone sentence
[ ] P3b — Posture named; verb derived from posture via pattern
[ ] P3c — Uncertainty register present with verb-shift directions
[ ] Beat 1 opens with falsifiable S0 hypothesis
[ ] Beat 3 leads with "The pattern: ..." verbatim from P3a
[ ] Beat 5 opens with verb
[ ] Beat 5 has posture statement
[ ] Beat 5 has bridge sentence — independently written, not a copy of P3a or Beat 3
[ ] No silent contradiction with any preparation-stage determination
[ ] All five beats present with original labels
```

---

## V-04 — Combination: Role Sequence + Inertia Framing

**Hypothesis:** Pairing the tri-role gate architecture (V-01) with S0 inertia framing as the explicit spine of the investigation — making the falsifiable hypothesis the first thing produced and the S0→S3 delta the last thing confirmed before narrative begins — will strengthen C-21 and C-22 while the role structure handles C-26 and C-27. The inertia framing also provides the natural vocabulary for the anti-stagnation check.

---

You are producing a `topic-story` artifact. The story tells decision-makers what the signals say together about a feature topic. It is not a summary of each signal — it is an editorial synthesis in your voice.

The output has a strict structure. Three roles run in sequence. Each role gates the next. The one-way rule: no role begins until the role before it is marked complete.

The spine of this investigation is the S0 hypothesis — the belief you entered with — and the S0→S3 delta — what the signals changed. Every structural requirement exists to make that delta honest.

---

### ROLE 1: EXTRACTOR

Your job: read the signals, record what they say.

Read each available artifact for this topic. For each, record exactly two things: what kind of signal it is, and the single strongest claim it makes. Do not interpret. Do not connect signals to each other. Do not write any synthetic claim. Your output is a reading record.

```
[EXTRACTOR BLOCK]
Signal: {artifact name or type}
Claim: {the strongest single assertion this artifact makes}

Signal: ...
Claim: ...
[EXTRACTOR COMPLETE]
```

Do not proceed to ROLE 2 until this block is marked COMPLETE.

---

### ROLE 2: ANALYST

Your job: read the EXTRACTOR BLOCK and produce four outputs, in order. You read EXTRACTOR output only — not the raw artifacts.

**A. State the S0 hypothesis.**

Before the signals, what was the team's working belief about this topic? State it as a falsifiable claim — a proposition that could be wrong. *"We believed..."* or *"Our hypothesis: X holds."* This is your inertia baseline. A vague intent statement fails. A description of what was investigated fails.

```
[ANALYST A — S0 HYPOTHESIS]
Our hypothesis: ...
[A COMPLETE]
```

**B. Compute the S0→S3 delta.**

Work through the EXTRACTOR BLOCK. What does the cumulative signal set do to the S0 hypothesis? Confirm it? Refute it? Modify it?

State the delta: *"We expected [S0]. The signals [confirmed / refuted / modified] this: [what changed]."* Name the shift — whether the recommendation direction moved, confidence changed, or scope narrowed or expanded. The delta must be something the signals produced, not something you could have written before reading them.

```
[ANALYST B — DELTA]
We expected: ...
Signals revealed: ...
Shift: ... [direction, confidence, or scope]
[B COMPLETE]
```

**C. Name the cross-signal pattern.**

State what two or more signals reveal together that no single signal reveals alone. This is a named relationship, tension, or gap — not a list of findings. Write it as a complete, self-contained sentence that conveys the full claim without surrounding context.

```
[ANALYST C — PATTERN]
The pattern: ...
[C COMPLETE]
```

**D. Derive evidence posture and recommendation verb.**

Name the overall signal posture: strong positive / mixed / conflicting / weak / negative. Then name the recommendation verb that this posture produces: proceed / pause / pivot / abandon. Write the derivation in one sentence: *"[Posture] because [the pattern], therefore [verb]."*

```
[ANALYST D — POSTURE AND VERB]
Posture: ...
Verb: ...
Derivation: ...
[D COMPLETE]
[ANALYST COMPLETE]
```

Do not proceed to ROLE 3 until ANALYST COMPLETE is present.

---

### ROLE 3: AUTHOR

Your job: translate the ANALYST blocks into narrative. You read ANALYST blocks only.

Before writing any beat, confirm the following rules:

1. **Beat 1** must open with the S0 hypothesis from Block A — stated as a falsifiable claim.
2. **Beat 3** must lead with the labeled pattern sentence: *"The pattern: [from Block C]."* The pattern sentence must be independently readable — not embedded in surrounding prose.
3. **Beat 5** must: (a) open with the recommendation verb from Block D; (b) name the evidence posture from Block D as the direct basis for the verb; (c) include a bridge sentence in this form: *"Because [the named cross-signal pattern], the recommendation is [verb]."* This bridge sentence is independently placed here. It is not satisfied by the pattern in Block C or in Beat 3. You must write it in Beat 5.
4. **Non-substitution:** No claim required in a Beat is discharged by its prior presence in an ANALYST block. Each placement is independently required.
5. **Anti-stagnation:** The delta in Beat 1 or Beat 3 must show mutation — it cannot be equivalent to restating the S0 hypothesis. S0 = S3 is a narrative failure.

---

**Beat 1 — What we set out to understand**

Open with the S0 hypothesis as a falsifiable claim. Explain what resolving it in either direction would mean for the feature decision. Close Beat 1 with a transition to what the signals actually produced.

**Beat 2 — What the signals revealed**

From the EXTRACTOR BLOCK, name the key finding from each signal type represented. This is not exhaustive — include what the pattern requires to be credible. Two to four sentences per signal type.

**Beat 3 — What the signals say together**

Lead with: *"The pattern: [verbatim from Block C]."* Develop the pattern in two to four sentences. Explain why this claim requires multiple signals — what relationship, tension, or gap it names that no single artifact surfaces.

**Beat 4 — What remains uncertain**

Name open questions whose resolution would shift the verb or confidence. For each, state: *"If [X] resolves to [Y], this moves from [verb] to [alternative verb]."* Minimum one item. Generic hedges without a directional statement fail.

**Beat 5 — The recommendation**

Open with the verb. Include: evidence posture statement, bridge sentence (independently written here, naming the pattern as the reason for the verb), and decision context — who is deciding and under what constraint. If the verb contradicts any prior ANALYST determination, name the override reason explicitly.

---

### TERMINAL VERIFICATION

```
[ ] EXTRACTOR BLOCK complete — claims only, no interpretation
[ ] ANALYST A — S0 hypothesis is a falsifiable proposition
[ ] ANALYST B — Delta names a direction; shift is signal-produced not pre-written
[ ] ANALYST C — Pattern is self-contained; full claim without context
[ ] ANALYST D — Posture named; verb derived in one sentence
[ ] ANALYST COMPLETE marker present
[ ] Beat 1 opens with S0 hypothesis from Block A
[ ] Beat 3 leads with "The pattern: ..." verbatim
[ ] Beat 5 opens with verb
[ ] Beat 5 contains posture statement (naming posture from Block D)
[ ] Beat 5 contains bridge sentence independently written — not a copy of Block C
[ ] Beat 4 contains at least one uncertainty with verb-shift direction
[ ] Delta shows genuine mutation — S0 ≠ S3
[ ] No silent contradiction between verb and prior ANALYST determination
[ ] All five beats present with original labels
```

---

## V-05 — Combination: Output Format + Non-Substitution Explicitness

**Hypothesis:** Embedding non-substitution rules directly adjacent to each required placement — rather than stating the rule once globally — reduces the probability of a model discharging a Beat-level requirement by reference to an earlier block. The block-and-beat format from V-02 provides the structural scaffold; explicit per-placement non-substitution warnings provide the correctness guardrails for C-19 and C-27.

---

You are producing a `topic-story` artifact — an editorial synthesis of signals gathered for a feature topic. The artifact has two parts. Complete Part 1 entirely before writing any line of Part 2.

---

## PART 1 — PRE-COMPOSITION BLOCKS

Three roles produce Part 1 in sequence. The roles and their outputs are labeled. Each block must be marked complete before the next begins.

---

### Block E — Signal Digest *(EXTRACTOR role)*

Read each available signal artifact. Record, for each:

| # | Artifact | Type | Strongest Claim |
|---|----------|------|-----------------|
| 1 | ... | ... | ... |
| 2 | ... | ... | ... |

*Do not interpret. Do not synthesize. Record only what each artifact asserts.*

`[BLOCK E COMPLETE — N signals recorded]`

---

### Block A1 — Falsifiable Hypothesis *(ANALYST role — reads Block E only)*

State the working hypothesis that framed this investigation as a proposition that could be disproven.

> **S0 hypothesis:** *[A specific claim that the signals can confirm, refute, or modify — not a description of what was investigated.]*

A sentence beginning "We set out to understand..." is not a hypothesis. A hypothesis begins "We believed..." or "Our hypothesis: X holds."

`[BLOCK A1 COMPLETE]`

---

### Block A2 — S0→S3 Delta *(ANALYST role — reads Block E and Block A1 only)*

Work through Block E. What is the cumulative effect of the signals on the S0 hypothesis?

> **We expected:** [restate S0]
>
> **The signals showed:** [what the evidence actually says]
>
> **The shift:** [name the mutation — direction, confidence level, or scope]

*The shift must be something the signals produced. If it could have been written before reading Block E, revise.*

`[BLOCK A2 COMPLETE]`

---

### Block A3 — Cross-Signal Pattern *(ANALYST role — reads Blocks E, A1, A2 only)*

State what two or more signals reveal together that no single signal reveals alone.

> **The pattern:** *[A complete, self-contained sentence naming a relationship, tension, or gap. This block must be readable without any surrounding context. A reader who reads only this block must understand the full synthetic claim.]*

Do not write a list of findings. Do not write "Signal A said X and Signal B said Y." Name the synthetic claim.

`[BLOCK A3 COMPLETE]`

---

### Block A4 — Evidence Posture and Verb *(ANALYST role — reads Blocks E, A1, A2, A3 only)*

| Dimension | Value |
|-----------|-------|
| Signal posture | strong positive / mixed / conflicting / weak / negative |
| Recommendation verb | proceed / pause / pivot / abandon |
| Derivation | [one sentence: this posture, given this pattern, produces this verb] |

`[BLOCK A4 COMPLETE]`

---

### Block A5 — Uncertainty Register *(ANALYST role)*

| Uncertainty | If resolves to... | Verb shifts from → to |
|-------------|------------------|-----------------------|
| ... | ... | [current verb] → [alternative] |

*Minimum one entry. "More research is needed" without a named direction fails.*

`[BLOCK A5 COMPLETE]`

`[PART 1 COMPLETE]`

---

## PART 2 — NARRATIVE BEATS

*(AUTHOR role — reads Part 1 blocks only)*

**Global non-substitution rule:** Every claim required in a Beat is independently required at that location. A claim present in a Part 1 block does not satisfy its Beat-level placement. You must produce it again, in the Beat.

---

### Beat 1 — What we set out to understand

Open with the S0 hypothesis from Block A1, stated as a falsifiable claim.

> ⚠️ **Placement rule:** The S0 hypothesis must appear in Beat 1. Its presence in Block A1 does not satisfy this requirement. Write it here as an independent narrative statement.

Explain what a confirmation, refutation, or modification of that hypothesis would mean for the feature decision. Transition to what the investigation actually found.

---

### Beat 2 — What the signals revealed

For each signal type in Block E, state one key finding — the claim it contributed to the synthesis. This is selective, not exhaustive. Include what the pattern in Block A3 requires to be credible.

---

### Beat 3 — What the signals say together

Lead with the labeled pattern sentence:

> **The pattern:** *[verbatim from Block A3]*

> ⚠️ **Placement rule:** This sentence is required here. Its presence in Block A3 does not satisfy this Beat 3 placement. Reproduce it verbatim and independently.

Develop the claim in two to four sentences: why this relationship, tension, or gap required multiple signals to surface.

---

### Beat 4 — What remains uncertain

Narrate the uncertainty register from Block A5. Each item must state: *"If [X] resolves to [Y], this moves from [current verb] to [alternative verb]."*

---

### Beat 5 — The recommendation

Open with the recommendation verb from Block A4.

**This beat must contain three independently-placed elements:**

**5a. Evidence posture statement.**

Name the signal posture from Block A4 as the direct basis for the verb.

> ⚠️ **Placement rule:** The posture statement is required here in Beat 5. Its presence in Block A4 does not satisfy this placement.

**5b. Bridge sentence.**

*"Because [name the cross-signal pattern], the recommendation is [verb]."*

> ⚠️ **Non-substitution (C-27 scope):** This bridge sentence is independently required in Beat 5. It is not satisfied by the pattern statement in Block A3 or in Beat 3, even if the content is identical. Write it here as a Beat 5 commitment, not a reference to earlier content.

**5c. Decision context.**

Name or clearly imply who is making the decision and under what constraint. A recommendation stated as a finding ("the signals suggest X") rather than a decision fails.

**5d. Override check.**

If the verb differs from any determination made in Part 1 blocks, name the override reason explicitly. Silent contradiction is a correctness failure.

---

## TERMINAL VERIFICATION CHECKLIST

Complete before submitting. This checklist is a gate.

```
[ ] Block E complete — extraction only, no interpretation
[ ] Block A1 — S0 hypothesis is falsifiable; begins "We believed..." or "Our hypothesis: ..."
[ ] Block A2 — Delta names a shift; could not have been written before Block E
[ ] Block A3 — Pattern is self-contained; no forward/backward references
[ ] Block A4 — Posture named; verb derived with one-sentence logic
[ ] Block A5 — At least one uncertainty with verb-shift direction
[ ] PART 1 COMPLETE marker present before Beat 1 begins
[ ] Beat 1 — S0 hypothesis present independently (not by reference to Block A1)
[ ] Beat 3 — "The pattern: ..." sentence present, verbatim, independently placed
[ ] Beat 5 — Opens with verb
[ ] Beat 5 — Posture statement present independently (not by reference to Block A4)
[ ] Beat 5 — Bridge sentence present independently; not a copy of Block A3 or Beat 3
[ ] Beat 5 — Decision context present
[ ] Beat 4 — Each uncertainty has "moves from X to Y" direction
[ ] Delta shows genuine mutation — S0 ≠ S3
[ ] No silent contradiction between Beat 5 verb and Part 1 determinations
[ ] All five beats present with original labels
```
