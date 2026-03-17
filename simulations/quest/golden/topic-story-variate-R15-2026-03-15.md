---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 15
rubric: v14
---

# Variations -- topic-story (Round 15)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v14 rubric adds C-35 (Dual Weight-Trigger Format Coverage) and C-36
(EVALUATOR-Phase Rule Citation Independence). From Round 14:

- V-01 R14: C-33 PASS, C-34 N/A (single-phase), C-35 N/A, C-36 N/A
- V-02 R14: C-33 PASS (sealed in Packet), C-34 NO (re-sealing step b instructional),
  C-35 PARTIAL (C-33 yes, C-34 no), C-36 PARTIAL (`Contestation rule:` is in Beat 4.5
  AUTHOR phase -- AUTHOR controls its value)
- V-03 R14: C-33 NO, C-34 PASS (`Re-sealing Reconciliation Decision` FORMAT BLOCK),
  C-35 PARTIAL (C-34 yes, C-33 no), C-36 N/A (no C-33 format fields in E-5)
- V-04 R14: C-33 PASS + C-31 PASS (single-phase), C-34 N/A, C-35 N/A, C-36 N/A
- V-05 R14: C-33 PASS + C-34 PASS (EVALUATOR/AUTHOR), C-35 PASS, C-36 PARTIAL --
  `Rule applied:` is sealed in Packet but `Contestation rule:` in Beat 4.5 is AUTHOR-phase.
  AUTHOR is told "use same label scheme as Packet Rule applied:" but selects the value.
  C-36 closes the gap where format-constrained fields are still populated by the authoring
  agent rather than being sealed EVALUATOR-phase outputs.

**C-36 gap analysis**: In all R14 two-phase specs, `Contestation rule:` lives in Beat 4.5
(AUTHOR phase). AUTHOR derives it by scanning the reconciliation table and identifying the
weight-level change that would flip the vector -- the same analytical work EVALUATOR already
performed to produce `Rule applied:`. C-36 requires the rule citation in Beat 4.5 to be
produced and sealed by EVALUATOR before authoring begins, making it architecturally
independent from AUTHOR's prose choices. The fix: EVALUATOR derives `Contestation rule:`
analytically (either within E-4 as a post-table output or as a dedicated E-8.5 step), seals
it in the Derivation Packet, and AUTHOR reads it verbatim without derivation.

**Round 15 primary axes**:

V-01 targets C-36 on the V-05 R14 base by adding `Contestation rule:` as a format-constrained
E-4 output (after all reconciliation rows) sealed in the Packet. AUTHOR Beat 4.5 reads verbatim.
V-02 targets C-36 with a dedicated E-8.5 Contestation Analysis step (EVALUATOR-phase), which
explicitly walks the Adjacent-verb derivation chain and seals the output. V-03 tests a phrasing
register axis: reader-verification framing -- the spec tells the model what a compliance reviewer
checks rather than prescribing what to write. V-04 combines V-01 and V-02 (E-4 field + E-8.5
chain, so derivation is traceable end-to-end). V-05 adds C-35 Dual Coverage Verification before
the Packet seal and re-sealing `Contestation rule:` update, covering the full v14 criterion set.

---

## V-01

**Variation axis**: Output format -- `Contestation rule:` as EVALUATOR-phase E-4 sealed field

**Hypothesis**: C-36 PARTIAL in R14 V-05 because `Contestation rule:` is populated by AUTHOR
using "same label scheme as Packet Rule applied:" -- instructional, not sealed. Moving
`Contestation rule:` to E-4 (after all reconciliation rows, alongside `Rule applied:`) and
sealing it in the Derivation Packet makes both rule citations EVALUATOR-phase outputs.
AUTHOR Beat 4.5 reads `Contestation rule:` verbatim from Packet -- no derivation, no choice.
C-34 retained from V-05 R14. C-35 prediction: PASS (both E-4 format fields and Re-sealing
FORMAT BLOCK present). C-36 prediction: PASS.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### EVALUATOR Phase

Complete all E-steps in sequence. Do not begin AUTHOR phase until the Derivation Packet is sealed.

#### E-1: Working hypothesis (S0)

State the specific claim the team entered with as a falsifiable assertion (not a goal, not a question).

#### E-2: Signal Extract

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to S0, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Inertia: HIGH | MEDIUM | LOW
  Rationale: {one sentence -- why this weight, tied to signal quality and specificity}
  [if MODIFIES]: Hypothesis update: [previous wording] -> [updated wording]
```

#### E-3: Hypothesis trajectory

```
Hypothesis at S3: [working hypothesis after all stances applied]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED

Evidence trajectory: CONVERGING | DIVERGING | FLAT | MIXED
```

#### E-4: Vector-verdict reconciliation table

One row per E-2 entry. Columns: Artifact | Stance | Weight | Rule applied | Reconciliation.

**Weight-level consistency rules** (apply by verdict + weight; each rule has a label):

- CONFIRMED/HIGH: HIGH-weight affirmative evidence. Vector locks CONFIRMED unless 2+ HIGH-weight
  CONTRADICTS present. Consequence: net vector is CONFIRMED.
- CONFIRMED/MEDIUM: Moderate affirmative. CONFIRMED holds unless HIGH-weight CONTRADICTS or 2+
  MEDIUM-weight CONTRADICTS overrule. Consequence: supports CONFIRMED, does not lock it.
- CONFIRMED/LOW: Weak affirmative. A single MEDIUM- or HIGH-weight CONTRADICTS reduces vector to
  QUALIFIED. Consequence: CONFIRMED is fragile -- treat as QUALIFIED if contrary signal exists.
- CONFIRMED/CLEAR: No prior state; purely additive. Consequence: adds CONFIRMED weight without
  triggering fragility rules.
- QUALIFIED/HIGH: HIGH-weight partial affirmative. Holds QUALIFIED floor regardless of LOW-weight
  CONTRADICTS. Consequence: vector cannot drop below QUALIFIED.
- QUALIFIED/MEDIUM: Moderate partial. Compatible with CONFIRMED if HIGH-weight CONFIRMS present.
  Consequence: does not independently force QUALIFIED.
- QUALIFIED/LOW: Weak partial. Does not independently prevent CONFIRMED. Consequence: negligible
  downward pressure.
- REVERSED/HIGH-dominant: Single HIGH-weight CONTRADICTS flips CONFIRMED to REVERSED unless 2+
  HIGH-weight CONFIRMS present. Consequence: net vector becomes REVERSED or QUALIFIED.
- REVERSED/MEDIUM-dominant: Two or more MEDIUM-weight CONTRADICTS with no HIGH-weight CONFIRMS
  flip net vector. Consequence: net vector becomes REVERSED.
- REVERSED/LOW-dominant: All CONFIRMS are LOW-weight and one or more CONTRADICTS exist at any
  weight. Consequence: net vector becomes QUALIFIED or REVERSED by count.
- REDIRECTED/ANY: New dominant goal or target emerged. Consequence: prior vector irrelevant;
  vector becomes REDIRECTED.

For each row:

```
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {brief consequence statement from rule definition}
Reconciliation: Vector is consistent | Vector revised from {OLD} to {NEW}: {brief reason}
```

`Rule applied:` is a REQUIRED FORMAT FIELD. A row that names weight levels without labeling the
triggered rule is incomplete.

After completing all rows, write the Contestation output:

```
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- row `{artifact-name}`,
  if weight were {HIGHER_OR_LOWER_WEIGHT_LEVEL} instead of {CURRENT_WEIGHT_LEVEL},
  the {VECTOR}/{ALTERNATIVE_WEIGHT} rule would fire, producing net vector {ALTERNATIVE_VECTOR}
  and Adjacent verb {ADJACENT_VERB}
```

`Contestation rule:` is a REQUIRED FORMAT FIELD. It names the single reconciliation row whose
weight-level change most narrowly produces the Adjacent verb. Sealed in Derivation Packet.

#### E-5: Conflict Register

All CONTRADICTS entries not overruled by weight-level rules.

```
| ID | Artifact | Stance | Weight | Status | Adjudication | Because |
|----|----------|--------|--------|--------|--------------|---------|
```

Status: RESOLVED (weight-level rule closed it) | UNRESOLVED (remains open)
Because: one sentence -- the specific factual reason the resolution is justified.

#### E-6: Pattern synthesis

Raw analytical output (not narrative prose). What do the HIGH-weight signals reveal together?
What do UNRESOLVED conflicts define as the boundary of knowledge? What does the evidence
trajectory imply about confidence stability?

#### E-7: Confidence Band

```
Band: HIGH | MEDIUM | LOW

Derivation:
  Signal count: {N}
  Weight distribution: HIGH={h}, MEDIUM={m}, LOW={l}
  Unresolved conflicts: {u}
  Trajectory: {from E-3}

Default: HIGH requires 3+ HIGH-weight CONFIRMS + 0 UNRESOLVED. LOW requires 2+ UNRESOLVED
  or DIVERGING trajectory with no HIGH-weight CONFIRMS. Otherwise MEDIUM.

[If non-default]: OVERRIDE: [reason default does not apply]
```

#### E-8: Seal Derivation Packet

```
[DERIVATION PACKET SEALED]
  S0: {from E-1}
  S3: {from E-3}
  Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED}
  Evidence trajectory: {CONVERGING | DIVERGING | FLAT | MIXED}
  Signal extracts: {from E-2 -- artifact-name, stance, weight, key finding}
  Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence from E-4}
  Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- row {artifact-name}, if weight
    {HIGHER_OR_LOWER}, Adjacent verb: {ADJACENT_VERB} [verbatim from E-4 Contestation output]
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose narrative, and
    recommendation preference are each prohibited as inputs to retroactive revision of any
    Packet field. `Contestation rule:` is an EVALUATOR-phase output; AUTHOR reads it verbatim.
  VALIDITY NOTICE: A Packet missing the IMMUTABLE clause is structurally incomplete. A Packet
    in which `Rule applied:` or `Contestation rule:` appear in AUTHOR-phase sections rather
    than this sealed record violates C-36.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

If AUTHOR discovers a new conflict while writing:

1. STOP authoring immediately.
2. Return to EVALUATOR. Execute ALL of the following:

   a. E-2 update: Add or revise the conflict entry.

   b. E-4 update: Update reconciliation table. Apply weight-level consistency rules.

      ```
      Re-sealing Reconciliation Decision:
        Rule re-executed: {VECTOR}/{WEIGHT_LEVEL} rule -- [the specific rule applied to the
          new or revised entry]
        Vector status: UNCHANGED | REVISED from {OLD} to {NEW}
        [If REVISED]: Trigger: {artifact-name} ({weight level}, {verdict type}) triggered
          the {VECTOR}/{WEIGHT_LEVEL} rule -- consequence: [specific consequence from rule]
      ```

      The `Re-sealing Reconciliation Decision` FORMAT BLOCK is required even if vector is
      unchanged. `Trigger:` required only when vector is revised.

   c. Update `Contestation rule:` (E-4 post-table field) if the re-sealing changes the
      Adjacent verb or the pivot row.

   d. E-5 update: Add conflict to Register.
   e. E-6 update: Revise pattern synthesis.
   f. E-7 update: Recalculate Confidence Band.
   g. E-8 re-seal: New Packet supersedes old. Updated `Rule applied:` and `Contestation rule:`
      must appear in the new Packet.

3. Resume AUTHOR from the point of discovery.

Silent conflict absorption is prohibited.

---

### AUTHOR Phase

Derive all content from the sealed Derivation Packet. Do not re-adjudicate signals or re-derive
the vector, Rule applied:, or Contestation rule:.

#### A-1: Write story beats

**Beat 1**: Original question (one sentence). S0 from Packet (one sentence). Entering default
-- what the team would have done without this signal-gathering (one sentence).

**Beat 2**: One editorial sentence per signal. Interpret, do not summarize. Highest-weight
signals first.

**Beat 3**: Pattern synthesis. Dominant claim anchored to two or more signals. How CONFIRMS
and CONTRADICTS define the boundary. What the evidence trajectory implies about confidence
stability.

**Beat 3 Output Inventory** (complete before writing Beat 4):

```
Pattern claims (verbatim, with artifact anchors):
  1. {claim text} [{artifact-name}, {artifact-name}]
  2. ...

Evidence anchors:
  1. {artifact-name}: {finding verbatim from E-2}
  2. ...

Adjudication commitments (RESOLVED conflicts only):
  1. {conflict-ID}: {adjudication verbatim from E-5}
  2. ...

[INVENTORY CLOSED -- {P} pattern claims, {A} evidence anchors, {C} adjudication commitments
 IMMUTABLE -- after sealing, contents are fixed. Beat 5 framing, prose narrative, and
 recommendation preference are prohibited as inputs to retroactive revision.
 A stamp missing the IMMUTABLE field is structurally incomplete and does not constitute
 a valid seal.]
```

**Beat 4**: One sentence per UNRESOLVED conflict from E-5. Auto-transfer only -- no
re-adjudication.

**Beat 4.5**: Six elements, all derived from sealed Packet:

```
Anchored claim: {verbatim from Beat 3 Output Inventory pattern claim #1}

Net vector: {verbatim from Packet}

Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Licensing: Packet Rule applied: [{VECTOR}/{WEIGHT_LEVEL} rule] and Band [{HIGH|MEDIUM|LOW}]
    authorize this verb. {One sentence: what weight-level pattern justifies the verb.}

Adjacent verb: {the verb one step away on the recommendation ladder}
  Pivot: row `{artifact-name}`, if weight were {HIGHER_OR_LOWER} instead of {CURRENT}

Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
  [Copy verbatim from Packet `Contestation rule:` field. Do not re-derive. Do not rephrase.]

Conditions: {weight-sensitive parameter -- the specific finding or threshold whose change would
  let the Adjacent verb displace the Recommendation verb}
```

`Contestation rule:` MUST match the Packet field verbatim. AUTHOR does not select this value.
Any deviation is a C-36 violation.

**Beat 5**: Stance (PROCEED | PAUSE | PIVOT | ABANDON) matching Packet Selected stance and Band
gate. One sentence: the specific condition under which this stance reverses.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet | Conflict Register | Story beats 1-5

---

## V-02

**Variation axis**: Role sequence -- dedicated E-8.5 Contestation Analysis step in EVALUATOR phase

**Hypothesis**: V-01 derives `Contestation rule:` as a post-table output of E-4, which means
the derivation is embedded in the reconciliation table step. C-36 still holds because E-4 is
EVALUATOR-phase, but the analytical chain (which row, which weight change, which rule would
fire) is not explicitly visible. V-02 moves `Contestation rule:` to a dedicated E-8.5 step
between E-7 (Confidence Band) and E-8 (Packet seal). E-8.5 makes the full derivation visible
as a named analytical step: identify the Adjacent verb, scan the table for the minimum-change
row, name the rule that would fire. This is architecturally equivalent to V-01 for C-36 but
tests whether an explicit named step produces more reliable derivation. C-34 retained. C-35
prediction: PASS. C-36 prediction: PASS. E-4 no longer carries a post-table `Contestation
rule:` field; E-8.5 owns it.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### EVALUATOR Phase

Complete all E-steps in sequence. Seal the Derivation Packet before any authoring begins.

#### E-1: Working hypothesis (S0)

One sentence: the specific claim the team entered with, stated as a falsifiable assertion.

#### E-2: Signal Extract

For each signal artifact, in order read:

```
- `{artifact-name}`: {key finding most relevant to S0, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Inertia: HIGH | MEDIUM | LOW
  Rationale: {one sentence -- why this weight}
  [if MODIFIES]: Hypothesis update: [previous] -> [updated]
```

#### E-3: Hypothesis trajectory

```
Hypothesis at S3: [working hypothesis after all stances applied]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
Evidence trajectory: CONVERGING | DIVERGING | FLAT | MIXED
```

#### E-4: Vector-verdict reconciliation table

One row per E-2 entry. Columns: Artifact | Stance | Weight | Rule applied | Reconciliation.

**Weight-level consistency rules**:

- CONFIRMED/HIGH: HIGH-weight affirmative. Vector locks CONFIRMED unless 2+ HIGH-weight
  CONTRADICTS. Consequence: net vector is CONFIRMED.
- CONFIRMED/MEDIUM: Moderate affirmative. CONFIRMED holds unless HIGH-weight CONTRADICTS or 2+
  MEDIUM-weight CONTRADICTS overrule. Consequence: supports CONFIRMED, does not lock it.
- CONFIRMED/LOW: Weak affirmative. Single MEDIUM- or HIGH-weight CONTRADICTS reduces to
  QUALIFIED. Consequence: CONFIRMED is fragile.
- CONFIRMED/CLEAR: No prior state; additive. Consequence: adds CONFIRMED weight without
  triggering fragility rules.
- QUALIFIED/HIGH: HIGH-weight partial. Holds QUALIFIED floor. Consequence: vector cannot drop
  below QUALIFIED.
- QUALIFIED/MEDIUM: Moderate partial. Compatible with CONFIRMED if HIGH-weight CONFIRMS present.
  Consequence: does not independently force QUALIFIED.
- QUALIFIED/LOW: Weak partial. Does not independently prevent CONFIRMED. Consequence: negligible
  downward pressure.
- REVERSED/HIGH-dominant: Single HIGH-weight CONTRADICTS flips CONFIRMED to REVERSED unless 2+
  HIGH-weight CONFIRMS present. Consequence: vector becomes REVERSED or QUALIFIED.
- REVERSED/MEDIUM-dominant: Two or more MEDIUM-weight CONTRADICTS with no HIGH-weight CONFIRMS.
  Consequence: vector becomes REVERSED.
- REVERSED/LOW-dominant: All CONFIRMS LOW-weight and one or more CONTRADICTS at any weight.
  Consequence: vector becomes QUALIFIED or REVERSED by count.
- REDIRECTED/ANY: New dominant goal emerged. Consequence: vector becomes REDIRECTED.

For each row:

```
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {brief consequence statement}
Reconciliation: Vector is consistent | Vector revised from {OLD} to {NEW}: {brief reason}
```

`Rule applied:` is a REQUIRED FORMAT FIELD.

#### E-5: Conflict Register

```
| ID | Artifact | Stance | Weight | Status | Adjudication | Because |
|----|----------|--------|--------|--------|--------------|---------|
```

Status: RESOLVED | UNRESOLVED. Because: one sentence.

#### E-6: Pattern synthesis

Raw analytical output. What do HIGH-weight signals reveal together? What do UNRESOLVED conflicts
define as the boundary of knowledge? What does the evidence trajectory imply?

#### E-7: Confidence Band

```
Band: HIGH | MEDIUM | LOW
Derivation:
  Signal count: {N}
  Weight distribution: HIGH={h}, MEDIUM={m}, LOW={l}
  Unresolved conflicts: {u}
  Trajectory: {from E-3}
Default: HIGH = 3+ HIGH-weight CONFIRMS + 0 UNRESOLVED. LOW = 2+ UNRESOLVED or DIVERGING
  with no HIGH-weight CONFIRMS. Otherwise MEDIUM.
[If non-default]: OVERRIDE: {reason}
```

#### E-8.5: Contestation Analysis

This step derives the `Contestation rule:` that will be sealed in the Derivation Packet.

```
Current state:
  Net vector: {from E-3}
  Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} [per Band gate]
  Adjacent verb: {the verb one step away on the recommendation ladder}

Scan E-4 reconciliation table. Identify the single row where a weight-level change would most
narrowly produce the Adjacent verb.

  Pivot row: `{artifact-name}`
  Current weight: {HIGH | MEDIUM | LOW}
  Current rule applied: {rule label from E-4}

  If weight were {HIGHER | LOWER} ({new weight level}):
    Rule that would fire: {VECTOR}/{WEIGHT_LEVEL} rule
    Resulting net vector: {ALTERNATIVE_VECTOR}
    This would license: {ADJACENT_VERB}

Contestation output:
  Adjacent verb: {verb}
  Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
```

The Contestation output is sealed in the Derivation Packet. AUTHOR reads `Contestation rule:`
verbatim from the Packet. AUTHOR does not re-derive or re-select this value.

#### E-8: Seal Derivation Packet

```
[DERIVATION PACKET SEALED]
  S0: {from E-1}
  S3: {from E-3}
  Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED}
  Evidence trajectory: {CONVERGING | DIVERGING | FLAT | MIXED}
  Signal extracts: {from E-2}
  Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence from E-4}
  Contestation analysis (from E-8.5):
    Adjacent verb: {verb}
    Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- pivot row `{artifact-name}`,
      if weight {HIGHER_OR_LOWER}
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision. `Rule applied:`
    and `Contestation rule:` are EVALUATOR-phase outputs; AUTHOR reads verbatim.
  VALIDITY NOTICE: Packet missing IMMUTABLE clause is structurally incomplete. `Contestation
    rule:` in AUTHOR-phase sections rather than this sealed record is a C-36 violation.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

If AUTHOR discovers a new conflict while writing:

1. STOP authoring.
2. Return to EVALUATOR:

   a. E-2 update: Add or revise the conflict entry.

   b. E-4 update:

      ```
      Re-sealing Reconciliation Decision:
        Rule re-executed: {VECTOR}/{WEIGHT_LEVEL} rule -- [rule applied to new/revised entry]
        Vector status: UNCHANGED | REVISED from {OLD} to {NEW}
        [If REVISED]: Trigger: {artifact-name} ({weight level}, {verdict type}) triggered
          the {VECTOR}/{WEIGHT_LEVEL} rule -- consequence: [specific consequence]
      ```

      `Re-sealing Reconciliation Decision` FORMAT BLOCK required even if vector unchanged.

   c. Re-run E-8.5 Contestation Analysis if vector changed. Update Contestation output.

   d. E-5, E-6, E-7 updates.

   e. E-8 re-seal: New Packet supersedes old. Updated `Rule applied:` and Contestation
      analysis must appear.

3. Resume AUTHOR.

---

### AUTHOR Phase

Derive all content from sealed Derivation Packet.

**Beat 1**: Question, S0, entering default.

**Beat 2**: One editorial sentence per signal. Highest-weight first.

**Beat 3**: Pattern synthesis. Dominant claim, boundary definition, trajectory implication.

**Beat 3 Output Inventory**:

```
Pattern claims (verbatim, with anchors):
  1. {claim} [{artifact-name}, ...]
Evidence anchors:
  1. {artifact-name}: {finding verbatim from E-2}
Adjudication commitments (RESOLVED conflicts only):
  1. {conflict-ID}: {adjudication verbatim from E-5}

[INVENTORY CLOSED -- {P} pattern claims, {A} evidence anchors, {C} adjudication commitments
 IMMUTABLE -- after sealing, contents are fixed. Beat 5 framing, prose narrative, and
 recommendation preference are prohibited as inputs to retroactive revision.
 A stamp missing the IMMUTABLE field is structurally incomplete and does not constitute
 a valid seal.]
```

**Beat 4**: One sentence per UNRESOLVED conflict. Auto-transfer only.

**Beat 4.5**:

```
Anchored claim: {verbatim from Beat 3 Inventory pattern claim #1}

Net vector: {verbatim from Packet}

Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Licensing: Packet Rule applied: [{VECTOR}/{WEIGHT_LEVEL} rule] and Band [{HIGH|MEDIUM|LOW}]
    authorize this verb. {One sentence: what weight-level pattern justifies it.}

Adjacent verb: {from Packet Contestation analysis}
  Pivot: {verbatim from Packet -- row and weight}

Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
  [Verbatim from Packet Contestation analysis. Do not re-derive. Do not rephrase.]

Conditions: {finding or threshold whose change would let Adjacent verb displace Recommendation
  verb}
```

`Contestation rule:` value is read from the sealed Packet. AUTHOR does not select or modify it.

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet | Conflict Register | Story beats 1-5

---

## V-03

**Variation axis**: Phrasing register -- reader-verification framing for C-36 compliance

**Hypothesis**: V-01 and V-02 enforce C-36 through prescriptive format-field instructions
("REQUIRED FORMAT FIELD", "Do not re-derive", "AUTHOR does not select this value"). An
alternative framing is reader-verification: the spec tells the model what a compliance
reviewer checks, defining correctness in terms of what an auditor would find rather than
what to write. This may produce more reliable C-36 adherence because it activates the model
as a self-verifier. Base: V-01 architecture (E-4 `Contestation rule:` field + C-34 re-sealing
block). The prescriptive language in Beat 4.5 and Packet is replaced with reader-audit
language. C-35 prediction: PASS. C-36 prediction: depends on whether audit framing outperforms
format-field prescription.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### EVALUATOR Phase

Complete all E-steps. A compliance reviewer will verify that all sealed fields in the
Derivation Packet are present and that no sealed field appears for the first time in AUTHOR-
phase sections. Do not begin AUTHOR phase until the Packet is sealed.

#### E-1: Working hypothesis (S0)

One sentence: the specific falsifiable assertion the team entered with.

#### E-2: Signal Extract

```
- `{artifact-name}`: {key finding, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Inertia: HIGH | MEDIUM | LOW
  Rationale: {why this weight}
  [if MODIFIES]: Hypothesis update: [previous] -> [updated]
```

#### E-3: Hypothesis trajectory

```
Hypothesis at S3: [after all stances applied]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
Evidence trajectory: CONVERGING | DIVERGING | FLAT | MIXED
```

#### E-4: Vector-verdict reconciliation table

One row per E-2 entry. Columns: Artifact | Stance | Weight | Rule applied | Reconciliation.

**Weight-level consistency rules**:

- CONFIRMED/HIGH: HIGH-weight affirmative. Vector locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Moderate affirmative. CONFIRMED holds unless HIGH-weight or 2+ MEDIUM-weight CONTRADICTS.
- CONFIRMED/LOW: Weak affirmative. Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: HIGH-weight partial. Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Moderate partial. Does not independently force QUALIFIED.
- QUALIFIED/LOW: Weak partial. Negligible downward pressure.
- REVERSED/HIGH-dominant: Single HIGH-weight CONTRADICTS flips CONFIRMED unless 2+ HIGH-weight CONFIRMS.
- REVERSED/MEDIUM-dominant: Two or more MEDIUM-weight CONTRADICTS with no HIGH-weight CONFIRMS.
- REVERSED/LOW-dominant: All CONFIRMS LOW-weight and one or more CONTRADICTS at any weight.
- REDIRECTED/ANY: New dominant goal emerged.

For each row:

```
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence}
Reconciliation: Vector is consistent | Vector revised from {OLD} to {NEW}: {reason}
```

A reviewer auditing this table checks: does every row name the specific rule label triggered
(e.g., CONFIRMED/HIGH, QUALIFIED/MEDIUM)? A row that says "the CONFIRMED signal outweighs"
without the rule label is incomplete -- the `Rule applied:` field is missing or empty.

After all rows, write the Contestation output:

```
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- row `{artifact-name}`,
  if weight were {ALTERNATIVE_WEIGHT_LEVEL}, the {VECTOR}/{ALTERNATIVE_WEIGHT} rule would
  fire, producing net vector {ALTERNATIVE_VECTOR} and Adjacent verb {ADJACENT_VERB}
```

A reviewer auditing this output checks: is this the specific rule that produces the Adjacent
verb? Is the pivot row identified by artifact name? A contestation statement that says "a
stronger contradicting signal might qualify the vector" without naming the rule label and the
specific row fails this audit.

#### E-5: Conflict Register

```
| ID | Artifact | Stance | Weight | Status | Adjudication | Because |
```

Status: RESOLVED | UNRESOLVED. Because: one sentence.

#### E-6: Pattern synthesis

Raw analysis: what do HIGH-weight signals reveal together, what do UNRESOLVED conflicts bound,
what does trajectory imply about confidence stability.

#### E-7: Confidence Band

```
Band: HIGH | MEDIUM | LOW
Derivation: Signal count: {N}, Weight: HIGH={h} MEDIUM={m} LOW={l}, UNRESOLVED: {u},
  Trajectory: {from E-3}
[OVERRIDE: {reason} if non-default]
```

Default: HIGH = 3+ HIGH-weight CONFIRMS, 0 UNRESOLVED. LOW = 2+ UNRESOLVED or DIVERGING,
no HIGH-weight CONFIRMS. Otherwise MEDIUM.

#### E-8: Seal Derivation Packet

```
[DERIVATION PACKET SEALED]
  S0: {from E-1}
  S3: {from E-3}
  Net vector: {from E-3}
  Evidence trajectory: {from E-3}
  Signal extracts: {from E-2}
  Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence from E-4}
  Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- row {artifact-name},
    if weight {HIGHER_OR_LOWER}, Adjacent verb: {ADJACENT_VERB}
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. A reviewer checking C-36 compliance reads
    this Packet first, then reads Beat 4.5. The `Rule applied:` and `Contestation rule:`
    values in Beat 4.5 must match these sealed entries exactly. If they differ, the AUTHOR
    modified an EVALUATOR-phase output -- that is the C-36 violation. Beat 5 framing, prose
    narrative, and recommendation preference are prohibited inputs to revision of any field.
  VALIDITY NOTICE: A Packet missing IMMUTABLE is structurally incomplete.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

A reviewer auditing a mid-draft conflict event checks: did authoring stop? Did the EVALUATOR
re-execute all steps? Is the new Packet the superseding one? Silent continuation is a
structural violation.

If AUTHOR discovers a conflict while writing:

1. STOP. Log: `CONFLICT DETECTED: {artifact-name} -- {description}. Authoring halted.`

2. Return to EVALUATOR:

   a. E-2 update: Add or revise the conflict entry.

   b. E-4 update. Produce the Re-sealing Reconciliation Decision:

      ```
      Re-sealing Reconciliation Decision:
        Rule re-executed: {VECTOR}/{WEIGHT_LEVEL} rule -- [rule applied to new/revised entry]
        Vector status: UNCHANGED | REVISED from {OLD} to {NEW}
        [If REVISED]: Trigger: {artifact-name} ({weight level}, {verdict type}) triggered
          the {VECTOR}/{WEIGHT_LEVEL} rule -- consequence: [consequence]
      ```

      A reviewer checks: is the rule label named (not just described in prose)? Is the
      decision in this FORMAT BLOCK rather than embedded in narrative?

   c. If vector changed, update `Contestation rule:` (E-4 post-table field). The new Packet
      must carry the updated value.

   d. E-5, E-6, E-7 updates.

   e. E-8 re-seal: new Packet supersedes old.

3. Resume AUTHOR. Log: `RESEALING COMPLETE. Resuming from: {point of discovery}.`

---

### AUTHOR Phase

A compliance reviewer reading the finished story checks two things for C-36:
1. Copy the Packet's `Rule applied:` value. Does Beat 4.5 Recommendation verb licensing cite
   this exact label? If not: C-36 violation.
2. Copy the Packet's `Contestation rule:` value. Does Beat 4.5 `Contestation rule:` field
   match exactly? If not: C-36 violation.

Keep both Packet values in mind as you write. You are reading from the Packet -- not choosing
or deriving.

**Beat 1**: Question, S0 from Packet, entering default.

**Beat 2**: Editorial sentence per signal. Highest-weight first.

**Beat 3**: Pattern synthesis from E-6. Dominant claim anchored to two or more signals.

**Beat 3 Output Inventory**:

A reviewer auditing Beat 3 checks: does every pattern claim have artifact anchors? Does every
RESOLVED adjudication commitment match E-5 verbatim?

```
Pattern claims (verbatim, with anchors):
  1. {claim} [{artifact-name}, ...]
Evidence anchors:
  1. {artifact-name}: {finding from E-2}
Adjudication commitments (RESOLVED only):
  1. {conflict-ID}: {adjudication from E-5}

[INVENTORY CLOSED -- {P} pattern claims, {A} evidence anchors, {C} adjudication commitments
 IMMUTABLE -- after sealing, contents are fixed. Beat 5 framing, prose narrative, and
 recommendation preference are prohibited as inputs to retroactive revision.
 A stamp missing the IMMUTABLE field is structurally incomplete and does not constitute
 a valid seal.]
```

**Beat 4**: UNRESOLVED conflicts from E-5. One sentence each. Auto-transfer only.

**Beat 4.5**:

```
Anchored claim: {verbatim from Beat 3 Inventory claim #1}

Net vector: {verbatim from Packet}

Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Licensing: Packet Rule applied: [{VECTOR}/{WEIGHT_LEVEL} rule -- paste this label exactly]
    and Band [{HIGH|MEDIUM|LOW}] authorize this verb. {One sentence.}

Adjacent verb: {one step away}
  Pivot: {row and weight from Packet Contestation rule}

Contestation rule: {paste from Packet `Contestation rule:` field -- exact match required}

Conditions: {finding or threshold whose change would let Adjacent verb win}
```

Reviewer test: highlight `Rule applied:` in Beat 4.5 and in the Packet -- they must match.
Highlight `Contestation rule:` in Beat 4.5 and in the Packet -- they must match. A mismatch
is a structural error, not a style choice.

**Beat 5**: Stance matching Packet Selected stance and Band gate. Reversal condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet | Conflict Register | Story beats 1-5

---

## V-04

**Variation axis**: Combination -- role sequence + output format: E-8.5 Contestation Analysis
chain + E-4 `Contestation rule:` field sealed together

**Hypothesis**: V-01 seals `Contestation rule:` as an E-4 post-table field (derivation
implicit). V-02 derives it through a dedicated E-8.5 step (derivation explicit but E-4 carries
no field). V-04 combines both: E-8.5 produces the full visible derivation chain (adjacent verb,
pivot row, weight-level analysis, rule that would fire), and E-4 carries a `Contestation rule:`
field that reads from E-8.5 output. This creates a two-level architecture: E-8.5 for auditable
derivation, E-4 for the format-constrained record that enters the Packet. Prediction: C-35 PASS
(both E-4 format fields and Re-sealing FORMAT BLOCK present). C-36 PASS (E-8.5 is EVALUATOR-
phase; E-4 field reads from it; Packet seals it; AUTHOR reads verbatim). C-30 PASS (weight-
level rules named by label in E-4). C-31 PASS (IMMUTABLE clause in Beat 3 stamp and Packet).
C-33 PASS (`Rule applied:` FORMAT FIELD). C-34 PASS (Re-sealing Reconciliation Decision
FORMAT BLOCK).

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### EVALUATOR Phase

Complete all E-steps in sequence. E-8.5 must run before E-8 (it feeds the Packet). Seal the
Derivation Packet before any authoring begins.

#### E-1: Working hypothesis (S0)

One sentence: specific falsifiable assertion the team entered with.

#### E-2: Signal Extract

```
- `{artifact-name}`: {key finding, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Inertia: HIGH | MEDIUM | LOW
  Rationale: {why this weight}
  [if MODIFIES]: Hypothesis update: [previous] -> [updated]
```

#### E-3: Hypothesis trajectory

```
Hypothesis at S3: [after all stances applied]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
Evidence trajectory: CONVERGING | DIVERGING | FLAT | MIXED
```

#### E-4: Vector-verdict reconciliation table

One row per E-2 entry.

**Weight-level consistency rules**:

- CONFIRMED/HIGH: HIGH-weight affirmative. Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Moderate affirmative. Holds unless HIGH-weight or 2+ MEDIUM-weight CONTRADICTS.
- CONFIRMED/LOW: Weak affirmative. Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: HIGH-weight partial. Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Moderate partial. Does not independently force QUALIFIED.
- QUALIFIED/LOW: Weak partial. Negligible downward pressure.
- REVERSED/HIGH-dominant: Single HIGH-weight CONTRADICTS flips CONFIRMED unless 2+ HIGH CONFIRMS.
- REVERSED/MEDIUM-dominant: 2+ MEDIUM CONTRADICTS, no HIGH CONFIRMS.
- REVERSED/LOW-dominant: All CONFIRMS LOW-weight, one or more CONTRADICTS at any weight.
- REDIRECTED/ANY: New dominant goal emerged.

For each row:

```
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence}
Reconciliation: Vector is consistent | Vector revised from {OLD} to {NEW}: {reason}
```

`Rule applied:` REQUIRED FORMAT FIELD.

After all rows, read from E-8.5 Contestation Analysis (which runs after E-7):

```
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- row `{artifact-name}`,
  if weight were {ALTERNATIVE_WEIGHT}, the {VECTOR}/{ALTERNATIVE_WEIGHT} rule would fire,
  Adjacent verb: {ADJACENT_VERB}
  [Copy from E-8.5 Contestation output -- do not re-derive here]
```

`Contestation rule:` REQUIRED FORMAT FIELD. Populated from E-8.5 output, sealed in Packet.

Note: Complete E-4 rows now. Return to fill in `Contestation rule:` after E-8.5 runs.

#### E-5: Conflict Register

```
| ID | Artifact | Stance | Weight | Status | Adjudication | Because |
```

Status: RESOLVED | UNRESOLVED. Because: one sentence.

#### E-6: Pattern synthesis

Raw analysis: HIGH-weight pattern, UNRESOLVED boundary, trajectory implication.

#### E-7: Confidence Band

```
Band: HIGH | MEDIUM | LOW
Derivation: Signal count: {N}, Weight: HIGH={h} MEDIUM={m} LOW={l}, UNRESOLVED: {u},
  Trajectory: {from E-3}
Default: HIGH = 3+ HIGH-weight CONFIRMS, 0 UNRESOLVED. LOW = 2+ UNRESOLVED or DIVERGING
  with no HIGH CONFIRMS. Otherwise MEDIUM.
[OVERRIDE: {reason} if non-default]
```

#### E-8.5: Contestation Analysis

```
Current state:
  Net vector: {from E-3}
  Band: {from E-7}
  Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} [per Band gate]
  Adjacent verb: {one step away on the ladder}

Scan E-4 reconciliation table. Find the single row whose weight-level change most narrowly
produces the Adjacent verb.

  Pivot row: `{artifact-name}`
  Current weight: {HIGH | MEDIUM | LOW}
  Current rule applied: {rule label from E-4}

  Weight-level analysis:
    If weight were {HIGHER | LOWER} ({new level}):
      Rule that would fire: {VECTOR}/{WEIGHT_LEVEL} rule
      Consequence: {from rule definition}
      Resulting net vector: {ALTERNATIVE_VECTOR}
      This licenses: {ADJACENT_VERB}

Contestation output:
  Adjacent verb: {verb}
  Pivot row: `{artifact-name}`, current weight {CURRENT} -> hypothetical {ALTERNATIVE}
  Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
```

Return to E-4 and fill in the `Contestation rule:` post-table field using this output.

#### E-8: Seal Derivation Packet

```
[DERIVATION PACKET SEALED]
  S0: {from E-1}
  S3: {from E-3}
  Net vector: {from E-3}
  Evidence trajectory: {from E-3}
  Signal extracts: {from E-2}
  Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence from E-4}
  Contestation analysis:
    Derivation (from E-8.5): Adjacent verb {ADJACENT_VERB} via pivot row `{artifact-name}`,
      if weight {CURRENT} -> {ALTERNATIVE}, {VECTOR}/{ALTERNATIVE_WEIGHT} rule fires
    Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule [verbatim from E-8.5 Contestation output]
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision. `Rule applied:`
    and `Contestation rule:` are EVALUATOR-phase outputs sealed here; AUTHOR reads verbatim.
  VALIDITY NOTICE: Packet missing IMMUTABLE is structurally incomplete. `Contestation rule:`
    appearing in AUTHOR-phase sections rather than this Packet is a C-36 violation.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

If AUTHOR discovers a conflict while writing:

1. STOP.
2. Return to EVALUATOR:

   a. E-2 update.

   b. E-4 update:

      ```
      Re-sealing Reconciliation Decision:
        Rule re-executed: {VECTOR}/{WEIGHT_LEVEL} rule -- [rule applied to new/revised entry]
        Vector status: UNCHANGED | REVISED from {OLD} to {NEW}
        [If REVISED]: Trigger: {artifact-name} ({weight}, {verdict type}) triggered
          {VECTOR}/{WEIGHT_LEVEL} rule -- consequence: [consequence]
      ```

      FORMAT BLOCK required even if vector unchanged. `Trigger:` only when REVISED.

   c. If vector changed: re-run E-8.5 Contestation Analysis with updated table. Update
      Contestation output. Return to E-4 `Contestation rule:` post-table field with new value.

   d. E-5, E-6, E-7 updates.

   e. E-8 re-seal: new Packet, with updated `Rule applied:`, `Contestation analysis`, and
      `Contestation rule:`.

3. Resume AUTHOR.

---

### AUTHOR Phase

Derive all content from sealed Derivation Packet.

**Beat 1**: Question, S0, entering default.

**Beat 2**: Editorial sentence per signal. Highest-weight first.

**Beat 3**: Pattern synthesis. Dominant claim, boundary, trajectory.

**Beat 3 Output Inventory**:

```
Pattern claims (verbatim, with anchors):
  1. {claim} [{artifact-name}, ...]
Evidence anchors:
  1. {artifact-name}: {finding from E-2}
Adjudication commitments (RESOLVED only):
  1. {conflict-ID}: {adjudication from E-5}

[INVENTORY CLOSED -- {P} pattern claims, {A} evidence anchors, {C} adjudication commitments
 IMMUTABLE -- after sealing, contents are fixed. Beat 5 framing, prose narrative, and
 recommendation preference are prohibited as inputs to retroactive revision.
 A stamp missing the IMMUTABLE field is structurally incomplete and does not constitute
 a valid seal.]
```

**Beat 4**: UNRESOLVED conflicts. One sentence each. Auto-transfer.

**Beat 4.5**:

```
Anchored claim: {verbatim from Beat 3 Inventory claim #1}

Net vector: {verbatim from Packet}

Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Licensing: Packet Rule applied: [{VECTOR}/{WEIGHT_LEVEL} rule] and Band [{HIGH|MEDIUM|LOW}]
    authorize this verb. {One sentence.}

Adjacent verb: {from Packet Contestation analysis}
  Pivot: {row and weight from Packet, verbatim}

Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
  [Copy verbatim from Packet Contestation analysis `Contestation rule:` field.
   Do not re-derive from E-4. Do not modify.]

Conditions: {finding or threshold whose change lets Adjacent verb displace Recommendation verb}
```

**Beat 5**: Stance, reversal condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet | Conflict Register | Story beats 1-5

---

## V-05

**Variation axis**: Full combination -- C-35 Dual Coverage Verification + C-36 full sealing
independence + re-sealing `Contestation rule:` update

**Hypothesis**: V-04 achieves C-35 and C-36 for the initial draft path. Two residual gaps:
(1) C-35 is not explicitly verified before the Packet is sealed -- both format-constrained
fields exist but neither an explicit audit step nor a dual-coverage checkpoint confirms
their co-presence; (2) after a re-sealing event, `Contestation rule:` may need to update
(if vector changes) but the re-sealing protocol in V-04 addresses this only as a conditional
("if vector changed"). V-05 adds: (a) an E-8.75 Dual Coverage Verification step that
explicitly checks both C-35 conditions before E-8 Packet seal; (b) makes `Contestation rule:`
update mandatory in re-sealing protocol step c whenever the Re-sealing Reconciliation Decision
reports REVISED vector (not just "if vector changed" -- the trigger is the FORMAT BLOCK
declaring REVISED); (c) adds a C-36 independence note to the Packet seal that names what
a compliance auditor checks. Combines all v14 criteria: C-30, C-31, C-33, C-34, C-35, C-36.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### EVALUATOR Phase

Complete all E-steps in order through E-8.75 before sealing the Derivation Packet at E-8.

#### E-1: Working hypothesis (S0)

One sentence: specific falsifiable assertion.

#### E-2: Signal Extract

```
- `{artifact-name}`: {key finding, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Inertia: HIGH | MEDIUM | LOW
  Rationale: {why this weight}
  [if MODIFIES]: Hypothesis update: [previous] -> [updated]
```

#### E-3: Hypothesis trajectory

```
Hypothesis at S3: [after all stances applied]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
Evidence trajectory: CONVERGING | DIVERGING | FLAT | MIXED
```

#### E-4: Vector-verdict reconciliation table

One row per E-2 entry.

**Weight-level consistency rules**:

- CONFIRMED/HIGH: HIGH-weight affirmative. Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Moderate affirmative. Holds unless HIGH-weight or 2+ MEDIUM CONTRADICTS.
- CONFIRMED/LOW: Weak affirmative. Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: HIGH-weight partial. Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Moderate partial. Does not independently force QUALIFIED.
- QUALIFIED/LOW: Weak partial. Negligible downward pressure.
- REVERSED/HIGH-dominant: Single HIGH-weight CONTRADICTS flips CONFIRMED unless 2+ HIGH CONFIRMS.
- REVERSED/MEDIUM-dominant: 2+ MEDIUM CONTRADICTS, no HIGH CONFIRMS.
- REVERSED/LOW-dominant: All CONFIRMS LOW-weight, one or more CONTRADICTS at any weight.
- REDIRECTED/ANY: New dominant goal emerged.

For each row:

```
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence}
Reconciliation: Vector is consistent | Vector revised from {OLD} to {NEW}: {reason}
```

`Rule applied:` REQUIRED FORMAT FIELD.

After all rows -- fill in `Contestation rule:` from E-8.5 output (see below):

```
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- row `{artifact-name}`,
  if weight {CURRENT} -> {ALTERNATIVE}, Adjacent verb: {ADJACENT_VERB}
  [Filled from E-8.5 Contestation output after E-7 runs]
```

`Contestation rule:` REQUIRED FORMAT FIELD. Populated from E-8.5.

#### E-5: Conflict Register

```
| ID | Artifact | Stance | Weight | Status | Adjudication | Because |
```

Status: RESOLVED | UNRESOLVED. Because: one sentence.

#### E-6: Pattern synthesis

Raw analysis: HIGH-weight pattern, UNRESOLVED boundary, trajectory implication.

#### E-7: Confidence Band

```
Band: HIGH | MEDIUM | LOW
Derivation: Signal count: {N}, Weight: HIGH={h} MEDIUM={m} LOW={l}, UNRESOLVED: {u},
  Trajectory: {from E-3}
Default: HIGH = 3+ HIGH CONFIRMS, 0 UNRESOLVED. LOW = 2+ UNRESOLVED or DIVERGING no HIGH
  CONFIRMS. Otherwise MEDIUM.
[OVERRIDE: {reason} if non-default]
```

#### E-8.5: Contestation Analysis

```
Current state:
  Net vector: {from E-3}
  Band: {from E-7}
  Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Adjacent verb: {one step away}

Scan E-4 table. Find the single row whose weight-level change most narrowly produces
Adjacent verb.

  Pivot row: `{artifact-name}`
  Current weight: {HIGH | MEDIUM | LOW}
  Current rule applied: {from E-4}

  If weight were {HIGHER | LOWER} ({new level}):
    Rule that would fire: {VECTOR}/{WEIGHT_LEVEL} rule
    Consequence: {from rule definition}
    Resulting vector: {ALTERNATIVE_VECTOR}
    This licenses: {ADJACENT_VERB}

Contestation output:
  Adjacent verb: {verb}
  Pivot row: `{artifact-name}`, {CURRENT} -> {ALTERNATIVE}
  Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
```

Return to E-4. Fill in `Contestation rule:` post-table field from this output.

#### E-8.75: Dual Coverage Verification

Before sealing the Packet, verify that both C-35 conditions are present:

```
C-35 Dual Coverage Verification:

  Condition 1 -- E-4 weight-trigger format fields:
    Rule applied: [field present and labeled with {VECTOR}/{WEIGHT_LEVEL} pattern?]
      Status: PRESENT | MISSING
    Contestation rule: [field present and labeled?]
      Status: PRESENT | MISSING

  Condition 2 -- Re-sealing Reconciliation Decision FORMAT BLOCK:
    [Is the Re-sealing Reconciliation Decision FORMAT BLOCK defined in this spec
     with Rule re-executed:, Vector status:, and conditional Trigger: sub-fields?]
      Status: PRESENT | MISSING

  C-35 result: PASS (both PRESENT) | FAIL (one or both MISSING)

  If C-35 FAIL: STOP. Return to E-4 and/or re-sealing protocol to add missing format
    structure before proceeding to E-8.
```

Proceed to E-8 only if C-35 result is PASS.

#### E-8: Seal Derivation Packet

```
[DERIVATION PACKET SEALED]
  S0: {from E-1}
  S3: {from E-3}
  Net vector: {from E-3}
  Evidence trajectory: {from E-3}
  Signal extracts: {from E-2}
  Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence from E-4}
  Contestation analysis:
    Derivation (from E-8.5): Adjacent verb {ADJACENT_VERB} via pivot row `{artifact-name}`,
      {CURRENT} -> {ALTERNATIVE} weight, {VECTOR}/{ALTERNATIVE_WEIGHT} rule fires
    Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule [verbatim from E-8.5]
  C-35 verification: PASS (from E-8.75)
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    produced in E-4 and E-8.5 respectively, before AUTHOR access begins. Compliance
    audit: copy `Rule applied:` from this Packet; verify Beat 4.5 Licensing cites this
    exact label. Copy `Contestation rule:` from this Packet; verify Beat 4.5 `Contestation
    rule:` field matches exactly. Any mismatch is a C-36 violation -- AUTHOR deviated from
    sealed EVALUATOR output.
  VALIDITY NOTICE: Packet missing IMMUTABLE is structurally incomplete. Packet without C-35
    verification record was sealed without completing E-8.75.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

If AUTHOR discovers a conflict while writing:

1. STOP.
2. Return to EVALUATOR:

   a. E-2 update.

   b. E-4 update. Produce Re-sealing Reconciliation Decision:

      ```
      Re-sealing Reconciliation Decision:
        Rule re-executed: {VECTOR}/{WEIGHT_LEVEL} rule -- [rule applied to new/revised entry]
        Vector status: UNCHANGED | REVISED from {OLD} to {NEW}
        [If REVISED]: Trigger: {artifact-name} ({weight}, {verdict type}) triggered
          {VECTOR}/{WEIGHT_LEVEL} rule -- consequence: [consequence]
      ```

      FORMAT BLOCK required even if vector unchanged. `Trigger:` required only when REVISED.

   c. If `Vector status: REVISED` (declared in FORMAT BLOCK):
      - Re-run E-8.5 Contestation Analysis with updated table.
      - Update E-4 `Contestation rule:` post-table field with new Contestation output.
      - The trigger for this update is `Vector status: REVISED` in the FORMAT BLOCK -- not
        informal assessment of whether the vector "seems to have changed."

   d. E-5, E-6, E-7 updates.

   e. Re-run E-8.75 Dual Coverage Verification. C-35 must remain PASS after re-sealing.

   f. E-8 re-seal: new Packet supersedes old. New Packet must include updated `Rule applied:`,
      updated Contestation analysis (if step c ran), updated C-35 verification record.

3. Resume AUTHOR.

---

### AUTHOR Phase

Derive all content from sealed Derivation Packet. `Rule applied:` and `Contestation rule:` are
read verbatim from Packet. AUTHOR does not derive, select, or modify either value.

**Beat 1**: Question, S0, entering default.

**Beat 2**: Editorial sentence per signal. Highest-weight first.

**Beat 3**: Pattern synthesis. Dominant claim, boundary, trajectory.

**Beat 3 Output Inventory**:

```
Pattern claims (verbatim, with anchors):
  1. {claim} [{artifact-name}, ...]
Evidence anchors:
  1. {artifact-name}: {finding from E-2}
Adjudication commitments (RESOLVED only):
  1. {conflict-ID}: {adjudication from E-5}

[INVENTORY CLOSED -- {P} pattern claims, {A} evidence anchors, {C} adjudication commitments
 IMMUTABLE -- after sealing, contents are fixed. Beat 5 framing, prose narrative, and
 recommendation preference are prohibited as inputs to retroactive revision.
 A stamp missing the IMMUTABLE field is structurally incomplete and does not constitute
 a valid seal.]
```

**Beat 4**: UNRESOLVED conflicts. One sentence each. Auto-transfer.

**Beat 4.5**:

```
Anchored claim: {verbatim from Beat 3 Inventory claim #1}

Net vector: {verbatim from Packet}

Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Licensing: Packet Rule applied: [{VECTOR}/{WEIGHT_LEVEL} rule -- exact label from Packet}]
    and Band [{HIGH|MEDIUM|LOW}] authorize this verb. {One sentence.}

Adjacent verb: {from Packet Contestation analysis}
  Pivot: {row and weight verbatim from Packet Contestation analysis}

Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
  [Verbatim from Packet Contestation analysis `Contestation rule:`. Do not re-derive.
   Do not rephrase. C-36 compliance: this value was sealed in EVALUATOR phase.]

Conditions: {finding or threshold whose change lets Adjacent verb displace Recommendation verb}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. Reversal condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35 verification) | Conflict Register | Story beats 1-5

---

## Summary

| | Axis | Base | C-33 | C-34 | C-35 | C-36 | Key addition |
|---|---|---|---|---|---|---|---|
| V-01 | Output format | V-05 R14 | PASS | PASS | PASS | Target PASS | `Contestation rule:` as E-4 post-table EVALUATOR field sealed in Packet |
| V-02 | Role sequence | V-05 R14 | PASS | PASS | PASS | Target PASS | Dedicated E-8.5 Contestation Analysis step; Packet carries full derivation chain |
| V-03 | Phrasing register | V-01 | PASS | PASS | PASS | Prediction TBD | Reader-audit framing: "reviewer checks X matches Y" instead of "REQUIRED FORMAT FIELD" |
| V-04 | Combination | V-01+V-02 | PASS | PASS | PASS | Target PASS | E-8.5 chain + E-4 field: two-level architecture (derivation + format record) |
| V-05 | Full combination | V-04 | PASS | PASS | PASS | Target PASS | E-8.75 Dual Coverage Verification + mandatory re-sealing `Contestation rule:` update on REVISED trigger |

**C-36 architecture** (all two-phase variations): EVALUATOR produces `Contestation rule:` in
E-4 (V-01, V-03) or E-8.5 (V-02) or both (V-04, V-05). Derivation Packet seals it. AUTHOR
reads verbatim. No AUTHOR-phase derivation of rule citations.

**Single-phase variations**: Not included in Round 15. C-36 is N/A for single-phase (no
phase separation). The R15 round focuses on closing the two-phase C-36 gap identified in
R14 V-05.
