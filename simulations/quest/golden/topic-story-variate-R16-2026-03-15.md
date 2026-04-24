---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 16
rubric: v15
---

# Variations -- topic-story (Round 16)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v15 rubric adds C-37 (Pre-Seal Dual Coverage Verification) and C-38
(Vector Revision Contestation Re-Derivation Trigger). From Round 15:

- V-01 R15: C-37 N/A (no E-8.75), C-38 PARTIAL (`if vector changed` informal trigger)
- V-02 R15: C-37 N/A, C-38 PARTIAL (informal trigger in step c)
- V-03 R15: C-37 N/A, C-38 PARTIAL
- V-04 R15: C-37 N/A, C-38 PARTIAL
- V-05 R15: C-37 PARTIAL (E-8.75 checks presence -- Status: PRESENT | MISSING -- not
  mutual consistency), C-38 PASS (formal `Vector status: REVISED` trigger in step c)

**C-37 gap analysis**: V-05 R15 E-8.75 confirms both `Rule applied:` and `Contestation
rule:` fields are PRESENT and labeled. The gap: two fields labeled with {VECTOR}/{WEIGHT_LEVEL}
patterns can be independently populated and still cite contradictory derivation chains.
`Rule applied:` determines net vector CONFIRMED via CONFIRMED/HIGH; `Contestation rule:`
could cite REVERSED/HIGH-dominant with a pivot row that does not connect to the Adjacent-verb
derivation E-8.5 produced -- both PRESENT, both labeled, C-37 PARTIAL. The mutual consistency
check closes this: after confirming presence, E-8.75 must verify (a) `Contestation rule:`
names a rule whose ALTERNATIVE_VECTOR differs from the current net vector produced by `Rule
applied:`, and (b) the Adjacent verb derivable from `Contestation rule:` matches the Adjacent
verb declared in E-8.5 Contestation output.

**C-38 gap analysis**: V-01-V-04 R15 use `if vector changed` or `if vector changed: re-run
E-8.5` as the re-sealing trigger. The gap: this is an informal assessment parallel to the
FORMAT BLOCK. A re-sealing can produce a FORMAT BLOCK declaring `Vector status: REVISED`
while the informal branch is not taken, or vice versa. C-38 requires the trigger to be the
`Vector status: REVISED` declaration in the FORMAT BLOCK itself -- not a parallel evaluation.

**Round 16 primary axes**:

V-01: C-37 on V-05 R15 base -- extend E-8.75 with mutual consistency assertion (vectors-differ
+ Adjacent-verb-match). C-38 inherited (PASS).

V-02: C-37 via role sequence -- consistency check moves into E-8.5 inline; E-8.75 becomes a
lightweight report reading E-8.5 result.

V-03: phrasing register -- reader-verification framing for C-37. Spec narrates what a
compliance reviewer checks rather than prescribing format-field assertions.

V-04: combination V-01+V-02 -- E-8.5 inline assertion + E-8.75 independent cross-check;
two-level architecture.

V-05: full combination -- C-37 two-level + C-38 promoted to named protocol axiom + E-8.75
mandatory every re-sealing + C-38 compliance record in Packet.

---

## V-01

**Variation axis**: Output format -- E-8.75 extended with mutual consistency assertion

**Hypothesis**: V-05 R15 E-8.75 checks presence (Status: PRESENT | MISSING) but not that
the two citations are mutually consistent. `Rule applied:` determines CONFIRMED via
CONFIRMED/HIGH; `Contestation rule:` could cite REVERSED/HIGH-dominant -- both PRESENT,
both labeled, but Contestation rule's ALTERNATIVE_VECTOR does not differ from the net vector
in the correct direction. Extending E-8.75 with a two-field consistency check closes this:
after presence, verify that `Contestation rule:` names a rule producing an ALTERNATIVE_VECTOR
that differs from the current net vector, and that the Adjacent verb implied matches E-8.5
output. C-37 prediction: PASS. C-38 inherited from V-05 R15: PASS.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### EVALUATOR Phase

Complete all E-steps in order through E-8.75 before sealing at E-8.

#### E-1: Working hypothesis (S0)

One sentence: specific falsifiable assertion the team entered with.

#### E-2: Signal Extract

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

**Weight-level consistency rules** (apply by verdict + weight; each rule has a label):

- CONFIRMED/HIGH: HIGH-weight affirmative. Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
  Consequence: net vector is CONFIRMED.
- CONFIRMED/MEDIUM: Moderate affirmative. Holds unless HIGH-weight or 2+ MEDIUM CONTRADICTS.
  Consequence: supports CONFIRMED, does not lock it.
- CONFIRMED/LOW: Weak affirmative. Single MEDIUM- or HIGH-weight CONTRADICTS reduces to
  QUALIFIED. Consequence: CONFIRMED is fragile.
- CONFIRMED/CLEAR: No prior state; additive. Consequence: adds CONFIRMED weight without
  triggering fragility rules.
- QUALIFIED/HIGH: HIGH-weight partial. Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Moderate partial. Does not independently force QUALIFIED.
- QUALIFIED/LOW: Weak partial. Negligible downward pressure.
- REVERSED/HIGH-dominant: Single HIGH-weight CONTRADICTS flips CONFIRMED unless 2+
  HIGH-weight CONFIRMS. Consequence: vector becomes REVERSED or QUALIFIED.
- REVERSED/MEDIUM-dominant: 2+ MEDIUM-weight CONTRADICTS, no HIGH-weight CONFIRMS.
  Consequence: vector becomes REVERSED.
- REVERSED/LOW-dominant: All CONFIRMS LOW-weight, one or more CONTRADICTS at any weight.
  Consequence: vector becomes QUALIFIED or REVERSED by count.
- REDIRECTED/ANY: New dominant goal emerged. Consequence: vector becomes REDIRECTED.

For each row:

```
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {brief consequence statement}
Reconciliation: Vector is consistent | Vector revised from {OLD} to {NEW}: {reason}
```

`Rule applied:` is a REQUIRED FORMAT FIELD.

After all rows -- fill in `Contestation rule:` from E-8.5 output:

```
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- row `{artifact-name}`,
  if weight {CURRENT} -> {ALTERNATIVE}, Adjacent verb: {ADJACENT_VERB}
  [Filled from E-8.5 Contestation output after E-7 runs]
```

`Contestation rule:` is a REQUIRED FORMAT FIELD. Populated from E-8.5, sealed in Packet.

#### E-5: Conflict Register

```
| ID | Artifact | Stance | Weight | Status | Adjudication | Because |
|----|----------|--------|--------|--------|--------------|---------|
```

Status: RESOLVED | UNRESOLVED. Because: one sentence.

#### E-6: Pattern synthesis

Raw analysis: HIGH-weight pattern, UNRESOLVED conflict boundary, trajectory implication.

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

  If weight were {HIGHER | LOWER} ({new level}):
    Rule that would fire: {VECTOR}/{WEIGHT_LEVEL} rule
    Consequence: {from rule definition}
    Resulting net vector: {ALTERNATIVE_VECTOR}
    This licenses: {ADJACENT_VERB}

Contestation output:
  Adjacent verb: {verb}
  Pivot row: `{artifact-name}`, {CURRENT} -> {ALTERNATIVE}
  Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
```

Return to E-4. Fill in `Contestation rule:` post-table field from this output.

#### E-8.75: Dual Coverage Verification

Before sealing the Packet, verify C-35 presence and C-37 mutual consistency.

```
C-35/C-37 Dual Coverage Verification:

  Presence check (C-35):
    Rule applied: [present in E-4 with {VECTOR}/{WEIGHT_LEVEL} label?]
      Status: PRESENT | MISSING
    Contestation rule: [present in E-4 post-table field with label?]
      Status: PRESENT | MISSING
    Re-sealing Reconciliation Decision FORMAT BLOCK: [defined in re-sealing protocol
      with Rule re-executed:, Vector status:, conditional Trigger:?]
      Status: PRESENT | MISSING
  C-35 result: PASS (all three PRESENT) | FAIL

  Mutual consistency check (C-37):
    [Only runs if C-35 PASS]
    Net vector from Rule applied: {VECTOR from E-4 dominant row}
    Alternative vector from Contestation rule: {ALTERNATIVE_VECTOR from E-8.5}
    Consistency test 1 -- vectors differ: {VECTOR} != {ALTERNATIVE_VECTOR}?
      Status: CONSISTENT | INCONSISTENT
    Adjacent verb from E-8.5 Contestation output: {ADJACENT_VERB}
    Adjacent verb implied by Contestation rule ALTERNATIVE_VECTOR: {verb}
    Consistency test 2 -- Adjacent verbs match?
      Status: CONSISTENT | INCONSISTENT
  C-37 result: PASS (both CONSISTENT) | PARTIAL (one or both INCONSISTENT) |
               N/A (C-35 FAIL -- fix presence first)

  If C-35 FAIL: STOP. Return to E-4 and/or re-sealing protocol.
  If C-37 PARTIAL: STOP. Return to E-8.5 -- Contestation rule does not produce a different
    outcome from Rule applied:. Rescan E-4 for the correct pivot row. Repopulate
    E-4 `Contestation rule:` and re-run this step.
```

Proceed to E-8 only if C-35 PASS and C-37 PASS.

#### E-8: Seal Derivation Packet

```
[DERIVATION PACKET SEALED]
  S0: {from E-1}
  S3: {from E-3}
  Net vector: {from E-3}
  Evidence trajectory: {from E-3}
  Signal extracts: {from E-2 -- artifact-name, stance, weight, key finding}
  Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence from E-4}
  Contestation analysis:
    Derivation (from E-8.5): Adjacent verb {ADJACENT_VERB} via pivot row `{artifact-name}`,
      {CURRENT} -> {ALTERNATIVE} weight, {VECTOR}/{ALTERNATIVE_WEIGHT} rule fires
    Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule [verbatim from E-8.5]
  C-35 verification: PASS (from E-8.75)
  C-37 verification: PASS -- vectors differ ({VECTOR} vs {ALTERNATIVE_VECTOR}),
    Adjacent verbs consistent ({ADJACENT_VERB} from E-8.5 and Contestation rule)
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here before AUTHOR access begins. AUTHOR reads verbatim from this Packet.
  VALIDITY NOTICE: Packet missing IMMUTABLE is structurally incomplete. Packet without
    C-35 and C-37 verification records was sealed without completing E-8.75.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

If AUTHOR discovers a conflict while writing:

1. STOP.
2. Return to EVALUATOR:

   a. E-2 update: Add or revise the conflict entry.

   b. E-4 update. Produce Re-sealing Reconciliation Decision:

      ```
      Re-sealing Reconciliation Decision:
        Rule re-executed: {VECTOR}/{WEIGHT_LEVEL} rule -- [rule applied to new/revised entry]
        Vector status: UNCHANGED | REVISED from {OLD} to {NEW}
        [If REVISED]: Trigger: {artifact-name} ({weight}, {verdict type}) triggered
          {VECTOR}/{WEIGHT_LEVEL} rule -- consequence: [consequence]
      ```

      FORMAT BLOCK required even if vector unchanged. `Trigger:` only when REVISED.

   c. If `Vector status: REVISED` (declared in FORMAT BLOCK):
      - Re-run E-8.5 Contestation Analysis with updated table.
      - Update E-4 `Contestation rule:` post-table field.
      - The trigger is `Vector status: REVISED` in the FORMAT BLOCK -- not informal
        assessment of whether the vector changed.

   d. E-5, E-6, E-7 updates.

   e. Re-run E-8.75. Both C-35 and C-37 must remain PASS.

   f. E-8 re-seal: new Packet supersedes old.

3. Resume AUTHOR.

---

### AUTHOR Phase

Derive all content from sealed Derivation Packet. `Rule applied:` and `Contestation rule:`
read verbatim from Packet. AUTHOR does not derive, select, or modify either value.

**Beat 1**: Question (one sentence), S0 from Packet (one sentence), entering default (one
sentence -- what the team would have done without signal-gathering).

**Beat 2**: One editorial sentence per signal. Interpret, do not summarize. Highest-weight
signals first.

**Beat 3**: Pattern synthesis. Dominant claim anchored to two or more signals. How CONFIRMS
and CONTRADICTS define the boundary. What evidence trajectory implies about confidence
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

**Beat 4**: One sentence per UNRESOLVED conflict from E-5. Auto-transfer only.

**Beat 4.5**:

```
Anchored claim: {verbatim from Beat 3 Inventory pattern claim #1}

Net vector: {verbatim from Packet}

Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Licensing: Packet Rule applied: [{VECTOR}/{WEIGHT_LEVEL} rule -- exact label from Packet}]
    and Band [{HIGH|MEDIUM|LOW}] authorize this verb. {One sentence.}

Adjacent verb: {from Packet Contestation analysis}
  Pivot: {row and weight verbatim from Packet Contestation analysis}

Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
  [Verbatim from Packet. Do not re-derive. Do not rephrase. C-36: sealed EVALUATOR-phase.
   C-37: Packet confirms this rule produces a different vector than Rule applied:.]

Conditions: {finding or threshold whose change would let Adjacent verb displace
  Recommendation verb}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35 and C-37 verification) | Conflict Register |
Story beats 1-5

---

## V-02

**Variation axis**: Role sequence -- consistency check embedded in E-8.5; E-8.75 becomes
a report step

**Hypothesis**: V-01 checks consistency at E-8.75 post-derivation. E-8.5 is the natural
locus: it already knows the net vector (from E-3), the governing rule (from E-4), the
Contestation rule it derived, and the Adjacent verb. Moving the consistency assertion into
E-8.5 makes derivation and its consistency guarantee atomic. E-8.75 becomes a lightweight
report reading E-8.5 outputs, not re-checking. May be more reliable: the check runs at
derivation rather than as a post-hoc audit. C-37 prediction: PASS. C-38 inherited: PASS.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### EVALUATOR Phase

Complete all E-steps in order. E-8.5 runs after E-7. E-8.75 reads E-8.5 result. E-8 seals.

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

One row per E-2 entry. Columns: Artifact | Stance | Weight | Rule applied | Reconciliation.

**Weight-level consistency rules**:

- CONFIRMED/HIGH: HIGH-weight affirmative. Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Holds unless HIGH-weight or 2+ MEDIUM CONTRADICTS.
- CONFIRMED/LOW: Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Does not independently force QUALIFIED.
- QUALIFIED/LOW: Negligible downward pressure.
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

After all rows -- filled from E-8.5:

```
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- row `{artifact-name}`,
  {CURRENT} -> {ALTERNATIVE}, Adjacent verb: {ADJACENT_VERB}
  [Filled from E-8.5 after E-7 runs]
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
Default: HIGH = 3+ HIGH CONFIRMS, 0 UNRESOLVED. LOW = 2+ UNRESOLVED or DIVERGING
  no HIGH CONFIRMS. Otherwise MEDIUM.
[OVERRIDE: {reason} if non-default]
```

#### E-8.5: Contestation Analysis with Inline Consistency Verification

This step derives the Contestation rule and verifies its consistency with `Rule applied:`
before the output leaves E-8.5.

```
Current state:
  Net vector: {from E-3}
  Governing Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule from dominant E-4 row
  Band: {from E-7}
  Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Adjacent verb: {one step away on the ladder}

Scan E-4 table. Find the single row whose weight-level change most narrowly produces
the Adjacent verb.

  Pivot row: `{artifact-name}`
  Current weight: {HIGH | MEDIUM | LOW}
  Current rule applied: {rule label from E-4}

  If weight were {HIGHER | LOWER} ({new level}):
    Rule that would fire: {VECTOR}/{WEIGHT_LEVEL} rule
    Consequence: {from rule definition}
    Resulting net vector: {ALTERNATIVE_VECTOR}
    This licenses: {ADJACENT_VERB}

Contestation output:
  Adjacent verb: {verb}
  Pivot row: `{artifact-name}`, {CURRENT} -> {ALTERNATIVE}
  Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule

Inline consistency verification (C-37):
  Governing Rule applied: vector = {VECTOR}
  Contestation rule: ALTERNATIVE_VECTOR = {ALTERNATIVE_VECTOR}
  Test 1 -- vectors differ: {VECTOR} != {ALTERNATIVE_VECTOR}?
    Result: CONSISTENT | INCONSISTENT
  Recommendation verb: {verb}; Adjacent verb: {ADJACENT_VERB}
  Test 2 -- verbs differ (Adjacent != Recommendation)?
    Result: CONSISTENT | INCONSISTENT
  C-37 inline result: PASS (both CONSISTENT) | FAIL
  [If FAIL]: STOP. Contestation rule does not produce a different outcome from
    Rule applied:. Rescan E-4 for the correct pivot row and re-derive.
```

Return to E-4. Fill in `Contestation rule:` post-table field from Contestation output.

#### E-8.75: Dual Coverage Report

Read from E-4 and E-8.5. Report C-35 and C-37 without re-deriving.

```
C-35/C-37 Report:
  C-35 presence:
    Rule applied: PRESENT in E-4 rows with {VECTOR}/{WEIGHT_LEVEL} label? {YES | NO}
    Contestation rule: PRESENT in E-4 post-table field from E-8.5? {YES | NO}
    Re-sealing FORMAT BLOCK defined in protocol? {YES | NO}
    C-35 result: PASS (all YES) | FAIL
  C-37: {PASS -- from E-8.5 inline result | FAIL}
  Combined: PASS (C-35 PASS and C-37 PASS) | FAIL
```

Proceed to E-8 only if Combined PASS.

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
    C-37 inline verification: PASS (vectors differ, Adjacent != Recommendation)
    Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule [verbatim from E-8.5]
  C-35 verification: PASS (from E-8.75 report)
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim.
  VALIDITY NOTICE: Packet without C-37 inline verification was sealed before E-8.5
    completed its consistency check.
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

   c. If `Vector status: REVISED` (declared in FORMAT BLOCK):
      - Re-run E-8.5 with updated table. Inline consistency check must produce C-37 PASS.
      - Update E-4 `Contestation rule:` post-table field.

   d. E-5, E-6, E-7 updates.

   e. Re-run E-8.75. Combined must be PASS.

   f. E-8 re-seal: new Packet supersedes old.

3. Resume AUTHOR.

---

### AUTHOR Phase

Derive all content from sealed Derivation Packet.

**Beat 1**: Question, S0 from Packet, entering default.

**Beat 2**: One editorial sentence per signal. Highest-weight first.

**Beat 3**: Pattern synthesis. Dominant claim, boundary, trajectory.

**Beat 3 Output Inventory**:

```
Pattern claims (verbatim, with anchors):
  1. {claim} [{artifact-name}, ...]
Evidence anchors:
  1. {artifact-name}: {finding verbatim from E-2}
Adjudication commitments (RESOLVED only):
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
Anchored claim: {verbatim from Beat 3 Inventory claim #1}
Net vector: {verbatim from Packet}
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Licensing: Packet Rule applied: [{VECTOR}/{WEIGHT_LEVEL} rule}] and Band [{band}]
    authorize this verb. {One sentence.}
Adjacent verb: {from Packet Contestation analysis}
  Pivot: {row and weight verbatim from Packet}
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
  [Verbatim from Packet. Do not re-derive. Do not rephrase.]
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. Reversal condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet | Conflict Register | Story beats 1-5

---

## V-03

**Variation axis**: Phrasing register -- reader-verification framing for C-37 mutual
consistency

**Hypothesis**: V-01 and V-02 enforce C-37 through prescriptive format blocks. An
alternative framing tells the model what a compliance reviewer checks rather than prescribing
the internal check format. For C-37, the spec describes what an auditor looks for: does
`Contestation rule:` name a rule whose ALTERNATIVE_VECTOR differs from the net vector `Rule
applied:` determined? If the spec frames E-8.75 this way, the model may produce more reliable
consistency because it activates self-review rather than format compliance alone. Base: V-01
architecture. C-37 prediction: depends on whether audit framing outperforms format-field
prescription. C-38 inherited: PASS.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### EVALUATOR Phase

Complete all E-steps. A compliance reviewer will verify Packet consistency before authoring.

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

One row per E-2 entry. Columns: Artifact | Stance | Weight | Rule applied | Reconciliation.

**Weight-level consistency rules**:

- CONFIRMED/HIGH: HIGH-weight affirmative. Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Holds unless HIGH-weight or 2+ MEDIUM CONTRADICTS.
- CONFIRMED/LOW: Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Does not independently force QUALIFIED.
- QUALIFIED/LOW: Negligible downward pressure.
- REVERSED/HIGH-dominant: Single HIGH-weight CONTRADICTS flips CONFIRMED unless 2+ HIGH CONFIRMS.
- REVERSED/MEDIUM-dominant: 2+ MEDIUM CONTRADICTS, no HIGH CONFIRMS.
- REVERSED/LOW-dominant: All CONFIRMS LOW-weight, one or more CONTRADICTS at any weight.
- REDIRECTED/ANY: New dominant goal emerged.

For each row:

```
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence}
Reconciliation: Vector is consistent | Vector revised from {OLD} to {NEW}: {reason}
```

A reviewer checks every row: does it name the specific rule label? A row that describes
the outcome without the label is missing `Rule applied:`.

After all rows, write the Contestation output from E-8.5:

```
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- row `{artifact-name}`,
  if weight {CURRENT} -> {ALTERNATIVE}, Adjacent verb: {ADJACENT_VERB}
```

A reviewer checks this field: does `Contestation rule:` name a rule whose ALTERNATIVE_VECTOR
differs from the net vector `Rule applied:` determined? If both cite rules producing the same
vector, the Contestation chain does not contest the current outcome.

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
[OVERRIDE: {reason} if non-default]
```

Default: HIGH = 3+ HIGH CONFIRMS, 0 UNRESOLVED. LOW = 2+ UNRESOLVED or DIVERGING
no HIGH CONFIRMS. Otherwise MEDIUM.

#### E-8.5: Contestation Analysis

```
Current state:
  Net vector: {from E-3}
  Band: {from E-7}
  Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Adjacent verb: {one step away}

Scan E-4 table. Find the single row whose weight-level change most narrowly produces
the Adjacent verb.

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

Return to E-4. Fill in `Contestation rule:` post-table field.

#### E-8.75: Dual Coverage Verification

A compliance reviewer auditing this Packet checks four things before accepting the seal:

1. Is `Rule applied:` present in E-4 rows and labeled with a {VECTOR}/{WEIGHT_LEVEL}
   pattern? A row that describes the outcome without the label fails this check.

2. Is `Contestation rule:` present as an E-4 post-table field and labeled?

3. Is the Re-sealing Reconciliation Decision FORMAT BLOCK defined in the re-sealing
   protocol with `Rule re-executed:`, `Vector status:`, and conditional `Trigger:` fields?

4. Does `Contestation rule:` produce a different net vector than `Rule applied:`?
   Read the net vector from the dominant `Rule applied:` entry. Read the ALTERNATIVE_VECTOR
   from `Contestation rule:`. They must differ. If they name the same vector, the Contestation
   rule is not contesting the current outcome.

```
Verification record:
  Check 1 -- Rule applied: labeled? {YES | NO}
  Check 2 -- Contestation rule: labeled? {YES | NO}
  Check 3 -- Re-sealing FORMAT BLOCK defined? {YES | NO}
  Check 4 -- Contestation ALTERNATIVE_VECTOR differs from Rule applied: vector?
    Rule applied: net vector = {VECTOR}
    Contestation rule: ALTERNATIVE_VECTOR = {ALTERNATIVE_VECTOR}
    Differ? {YES | NO}
  C-35 result: PASS (Checks 1-3 YES) | FAIL
  C-37 result: PASS (Check 4 YES) | PARTIAL (Check 4 NO) | N/A (C-35 FAIL)
```

A reviewer finding C-37 PARTIAL: the model selected a pivot row whose weight change does
not move the outcome. Return to E-8.5, rescan E-4, re-derive the correct pivot row.

Proceed to E-8 only if C-35 PASS and C-37 PASS.

#### E-8: Seal Derivation Packet

```
[DERIVATION PACKET SEALED]
  S0: {from E-1}
  S3: {from E-3}
  Net vector: {from E-3}
  Evidence trajectory: {from E-3}
  Signal extracts: {from E-2}
  Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence from E-4}
  Contestation analysis (from E-8.5):
    Adjacent verb: {ADJACENT_VERB}
    Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- pivot row `{artifact-name}`,
      {CURRENT} -> {ALTERNATIVE}
  C-35 verification: PASS (from E-8.75)
  C-37 verification: PASS -- reviewer check: Rule applied: vector = {VECTOR};
    Contestation rule: ALTERNATIVE_VECTOR = {ALTERNATIVE_VECTOR}; vectors differ.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. A reviewer checking C-36 reads this
    Packet first, then reads Beat 4.5. `Rule applied:` in Beat 4.5 Licensing must match
    exactly. `Contestation rule:` must match exactly. Any mismatch is a C-36 violation.
  VALIDITY NOTICE: Packet missing IMMUTABLE is structurally incomplete.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

A reviewer auditing a re-sealing event checks: did authoring stop? Did EVALUATOR re-execute
all steps? Is the FORMAT BLOCK present? Is the new Packet the superseding one?

If AUTHOR discovers a conflict while writing:

1. STOP. Log: `CONFLICT DETECTED: {artifact-name} -- {description}. Authoring halted.`

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

   c. If `Vector status: REVISED` (declared in FORMAT BLOCK):
      - Re-run E-8.5. Update E-4 `Contestation rule:` field.

   d. E-5, E-6, E-7 updates.

   e. Re-run E-8.75. A reviewer checks: do C-35 and C-37 both still pass?

   f. E-8 re-seal: new Packet supersedes old.

3. Resume AUTHOR. Log: `RESEALING COMPLETE. Resuming from: {point of discovery}.`

---

### AUTHOR Phase

A compliance reviewer checks three things:
1. Copy `Rule applied:` from Packet. Does Beat 4.5 Licensing cite this exact label?
2. Copy `Contestation rule:` from Packet. Does Beat 4.5 field match exactly?
3. Does the Packet's C-37 record confirm the two citations are consistent?

**Beat 1**: Question, S0 from Packet, entering default.

**Beat 2**: One editorial sentence per signal. Highest-weight first.

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
  Licensing: Packet Rule applied: [{VECTOR}/{WEIGHT_LEVEL} rule -- paste exactly}]
    and Band [{band}] authorize this verb. {One sentence.}
Adjacent verb: {from Packet Contestation analysis}
  Pivot: {row and weight from Packet, verbatim}
Contestation rule: {paste from Packet -- exact match required}
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

Reviewer test: `Rule applied:` in Beat 4.5 must match Packet. `Contestation rule:` must
match Packet. Packet C-37 record confirms they are consistent.

**Beat 5**: Stance matching Packet Selected stance and Band gate. Reversal condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet | Conflict Register | Story beats 1-5

---

## V-04

**Variation axis**: Combination -- E-8.5 inline consistency assertion (V-02) + E-8.75
independent verification (V-01): two-level consistency architecture

**Hypothesis**: V-01 checks consistency at E-8.75. V-02 checks in E-8.5 inline. V-04
combines both: E-8.5 produces the Contestation rule and asserts consistency immediately;
E-8.75 independently confirms presence and consistency without re-deriving. If E-8.5 inline
check fails, error is caught at derivation; if E-8.75 detects inconsistency that E-8.5
missed, the gate prevents sealing. C-37 prediction: PASS (two independent checks). C-38
inherited: PASS.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### EVALUATOR Phase

Complete all E-steps. E-8.5 runs after E-7. E-8.75 reads E-8.5 and independently
cross-checks. E-8 seals.

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

One row per E-2 entry. Columns: Artifact | Stance | Weight | Rule applied | Reconciliation.

**Weight-level consistency rules**:

- CONFIRMED/HIGH: HIGH-weight affirmative. Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Holds unless HIGH-weight or 2+ MEDIUM CONTRADICTS.
- CONFIRMED/LOW: Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Does not independently force QUALIFIED.
- QUALIFIED/LOW: Negligible downward pressure.
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

After all rows -- filled from E-8.5:

```
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- row `{artifact-name}`,
  {CURRENT} -> {ALTERNATIVE}, Adjacent verb: {ADJACENT_VERB}
  [Filled from E-8.5 -- do not fill before E-8.5 completes]
```

`Contestation rule:` REQUIRED FORMAT FIELD.

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
Default: HIGH = 3+ HIGH CONFIRMS, 0 UNRESOLVED. LOW = 2+ UNRESOLVED or DIVERGING
  no HIGH CONFIRMS. Otherwise MEDIUM.
[OVERRIDE: {reason} if non-default]
```

#### E-8.5: Contestation Analysis with Inline Consistency Assertion

```
Current state:
  Net vector: {from E-3}
  Governing Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule from dominant E-4 row
  Band: {from E-7}
  Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Adjacent verb: {one step away}

Scan E-4 table. Find the single row whose weight-level change most narrowly produces
the Adjacent verb.

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

Inline consistency assertion (C-37):
  Governing Rule applied: vector = {VECTOR}
  Contestation rule: ALTERNATIVE_VECTOR = {ALTERNATIVE_VECTOR}
  Assertion A: {VECTOR} != {ALTERNATIVE_VECTOR}. Result: HOLDS | FAILS
  Assertion B: {ADJACENT_VERB} != {Recommendation verb}. Result: HOLDS | FAILS
  C-37 inline: PASS (both HOLD) | FAIL
  [If FAIL]: STOP. Rescan E-4 for the correct pivot row.
```

Return to E-4. Fill `Contestation rule:` post-table field from Contestation output.

#### E-8.75: Dual Coverage Verification (independent of E-8.5)

```
C-35/C-37 Verification:

  C-35 presence:
    Rule applied: PRESENT in E-4 rows with {VECTOR}/{WEIGHT_LEVEL} label? {YES | NO}
    Contestation rule: PRESENT in E-4 post-table field? {YES | NO}
    Re-sealing FORMAT BLOCK defined in protocol? {YES | NO}
    C-35 result: PASS (all YES) | FAIL

  C-37 mutual consistency:
    E-8.5 inline C-37: {PASS | FAIL -- carry from E-8.5}
    Independent cross-check:
      Rule applied: net vector = {VECTOR}
      Contestation rule: ALTERNATIVE_VECTOR = {ALTERNATIVE_VECTOR}
      Vectors differ? {YES | NO}
    C-37 result: PASS (E-8.5 PASS and cross-check YES) | FAIL

  Combined: PASS (C-35 PASS and C-37 PASS) | FAIL
  [If any FAIL: STOP. Identify failing step, return to E-4 or E-8.5.]
```

Proceed to E-8 only if Combined is PASS.

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
      {CURRENT} -> {ALTERNATIVE}, {VECTOR}/{ALTERNATIVE_WEIGHT} rule fires
    C-37 inline: PASS
    Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule [verbatim from E-8.5]
  C-35 verification: PASS (from E-8.75)
  C-37 verification: PASS -- two-level (E-8.5 inline + E-8.75 cross-check);
    vectors differ ({VECTOR} vs {ALTERNATIVE_VECTOR})
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim.
  VALIDITY NOTICE: Packet with C-37 FAIL at either level was sealed with inconsistent
    rule citations.
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

   c. If `Vector status: REVISED` (declared in FORMAT BLOCK):
      - Re-run E-8.5 with updated table. Inline assertions must HOLD.
      - Update E-4 `Contestation rule:` field.

   d. E-5, E-6, E-7 updates.

   e. Re-run E-8.75. Combined must be PASS.

   f. E-8 re-seal: new Packet supersedes old.

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
  1. {artifact-name}: {finding verbatim from E-2}
Adjudication commitments (RESOLVED only):
  1. {conflict-ID}: {adjudication verbatim from E-5}

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
  Licensing: Packet Rule applied: [{VECTOR}/{WEIGHT_LEVEL} rule -- exact label}]
    and Band [{band}] authorize this verb. {One sentence.}
Adjacent verb: {from Packet Contestation analysis}
  Pivot: {row and weight verbatim from Packet}
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
  [Verbatim from Packet. Do not re-derive. C-37: two-level verified consistent.]
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

**Beat 5**: Stance, reversal condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet | Conflict Register | Story beats 1-5

---

## V-05

**Variation axis**: Full combination -- C-37 two-level consistency + C-38 as named protocol
axiom + complete v15 criterion coverage

**Hypothesis**: V-04 achieves C-37 PASS (two-level) and C-38 PASS (inherited `Vector status:
REVISED` trigger). Two residual design choices: (1) the C-38 trigger is embedded in step c
as a conditional -- a model could evaluate "if vector changed" informally despite the
instruction. Promoting C-38 to a named axiom at the head of the re-sealing protocol removes
the conditional: the FORMAT BLOCK `Vector status:` field IS the trigger. (2) E-8.75 re-run
should be mandatory every re-sealing -- not just when C-37 needs re-checking -- making full
consistency verification a required step regardless of Vector status. V-05 adds: (a) named
C-38 axiom before numbered steps; (b) E-8.75 mandatory every re-sealing; (c) explicit C-38
compliance record in Packet. Covers all v15 criteria.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### EVALUATOR Phase

Complete all E-steps in order through E-8.75 before sealing at E-8.

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

One row per E-2 entry. Columns: Artifact | Stance | Weight | Rule applied | Reconciliation.

**Weight-level consistency rules**:

- CONFIRMED/HIGH: HIGH-weight affirmative. Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Holds unless HIGH-weight or 2+ MEDIUM CONTRADICTS.
- CONFIRMED/LOW: Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Does not independently force QUALIFIED.
- QUALIFIED/LOW: Negligible downward pressure.
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

After all rows -- filled from E-8.5:

```
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- row `{artifact-name}`,
  {CURRENT} -> {ALTERNATIVE}, Adjacent verb: {ADJACENT_VERB}
  [Filled from E-8.5 -- do not fill before E-8.5 completes]
```

`Contestation rule:` REQUIRED FORMAT FIELD.

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
Default: HIGH = 3+ HIGH CONFIRMS, 0 UNRESOLVED. LOW = 2+ UNRESOLVED or DIVERGING
  no HIGH CONFIRMS. Otherwise MEDIUM.
[OVERRIDE: {reason} if non-default]
```

#### E-8.5: Contestation Analysis with Inline Consistency Assertion

```
Current state:
  Net vector: {from E-3}
  Governing Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule from dominant E-4 row
  Band: {from E-7}
  Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Adjacent verb: {one step away}

Scan E-4 table. Find the single row whose weight-level change most narrowly produces
the Adjacent verb.

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

Inline consistency assertion (C-37):
  Governing Rule applied: vector = {VECTOR}
  Contestation rule: ALTERNATIVE_VECTOR = {ALTERNATIVE_VECTOR}
  Assertion A: {VECTOR} != {ALTERNATIVE_VECTOR}. Result: HOLDS | FAILS
  Assertion B: {ADJACENT_VERB} != {Recommendation verb}. Result: HOLDS | FAILS
  C-37 inline: PASS (both HOLD) | FAIL
  [If FAIL]: STOP. Rescan E-4 for the correct pivot row.
```

Return to E-4. Fill `Contestation rule:` post-table field from Contestation output.

#### E-8.75: Dual Coverage Verification

```
C-35/C-37 Verification:

  C-35 presence:
    Rule applied: PRESENT in E-4 rows? {YES | NO}
    Contestation rule: PRESENT in E-4 post-table field? {YES | NO}
    Re-sealing FORMAT BLOCK defined in protocol? {YES | NO}
    C-35 result: PASS (all YES) | FAIL

  C-37 mutual consistency:
    E-8.5 inline C-37: {PASS | FAIL}
    Cross-check: Rule applied: vector = {VECTOR}; Contestation rule:
      ALTERNATIVE_VECTOR = {ALTERNATIVE_VECTOR}; differ? {YES | NO}
    C-37 result: PASS (E-8.5 PASS and cross-check YES) | FAIL

  Combined: PASS (C-35 PASS and C-37 PASS) | FAIL
  [If any FAIL: STOP. Return to E-4 or E-8.5.]
```

Proceed to E-8 only if Combined is PASS.

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
      {CURRENT} -> {ALTERNATIVE}, {VECTOR}/{ALTERNATIVE_WEIGHT} rule fires
    C-37 inline: PASS
    Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule [verbatim from E-8.5]
  C-35 verification: PASS (from E-8.75)
  C-37 verification: PASS -- two-level (E-8.5 inline + E-8.75 cross-check);
    Rule applied: vector {VECTOR} != Contestation rule ALTERNATIVE_VECTOR {ALTERNATIVE_VECTOR}
  C-38 compliance: Contestation re-derivation trigger = `Vector status: REVISED` in
    Re-sealing Reconciliation Decision FORMAT BLOCK. Informal assessment of vector change
    is not the trigger. The FORMAT BLOCK declaration is authoritative.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 compliance record omits the re-derivation trigger.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

**C-38 AXIOM**: The trigger for Contestation rule re-derivation (E-8.5 re-run) is the
`Vector status:` field value in the Re-sealing Reconciliation Decision FORMAT BLOCK.
When `Vector status: REVISED` is declared in the FORMAT BLOCK, E-8.5 MUST re-run and
produce a new Contestation output with inline consistency assertion before re-sealing.
When `Vector status: UNCHANGED` is declared, E-8.5 does NOT re-run. The analyst's informal
assessment of whether the vector changed is not consulted. The FORMAT BLOCK declaration
is authoritative.

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

      FORMAT BLOCK required even if vector unchanged.

   c. C-38 trigger: read `Vector status:` from FORMAT BLOCK.
      - If `Vector status: REVISED`: Re-run E-8.5. Inline assertions must HOLD.
        Update E-4 `Contestation rule:` field with new Contestation output.
      - If `Vector status: UNCHANGED`: Do not re-run E-8.5. `Contestation rule:`
        is unchanged.

   d. E-5, E-6, E-7 updates.

   e. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   f. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if step c ran E-8.5), updated C-35/C-37 records,
      updated C-38 compliance record reflecting the Vector status decision.

3. Resume AUTHOR.

---

### AUTHOR Phase

Derive all content from sealed Derivation Packet. `Rule applied:` and `Contestation rule:`
read verbatim from Packet. AUTHOR does not derive, select, or modify either value.

**Beat 1**: Question, S0 from Packet, entering default.

**Beat 2**: Editorial sentence per signal. Highest-weight first.

**Beat 3**: Pattern synthesis. Dominant claim, boundary, trajectory.

**Beat 3 Output Inventory**:

```
Pattern claims (verbatim, with anchors):
  1. {claim} [{artifact-name}, ...]
Evidence anchors:
  1. {artifact-name}: {finding verbatim from E-2}
Adjudication commitments (RESOLVED only):
  1. {conflict-ID}: {adjudication verbatim from E-5}

[INVENTORY CLOSED -- {P} pattern claims, {A} evidence anchors, {C} adjudication commitments
 IMMUTABLE -- after sealing, contents are fixed. Beat 5 framing, prose narrative, and
 recommendation preference are prohibited as inputs to retroactive revision.
 A stamp missing the IMMUTABLE field is structurally incomplete and does not constitute
 a valid seal.]
```

**Beat 4**: UNRESOLVED conflicts. One sentence each. Auto-transfer only.

**Beat 4.5**:

```
Anchored claim: {verbatim from Beat 3 Inventory claim #1}
Net vector: {verbatim from Packet}
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON}
  Licensing: Packet Rule applied: [{VECTOR}/{WEIGHT_LEVEL} rule -- exact label from Packet}]
    and Band [{band}] authorize this verb. {One sentence.}
Adjacent verb: {from Packet Contestation analysis}
  Pivot: {row and weight verbatim from Packet Contestation analysis}
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule
  [Verbatim from Packet. Do not re-derive. Do not rephrase. C-36: EVALUATOR-phase.
   C-37: two-level verified. C-38: re-derivation trigger is FORMAT BLOCK REVISED declaration.]
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 records) | Conflict Register |
Story beats 1-5

---

## Summary

| | Axis | Base | C-33 | C-34 | C-35 | C-36 | C-37 | C-38 | Key addition |
|---|---|---|---|---|---|---|---|---|---|
| V-01 | Output format | V-05 R15 | PASS | PASS | PASS | PASS | Target PASS | PASS | E-8.75 extended: vectors-differ + Adjacent-verb-match assertions after presence check |
| V-02 | Role sequence | V-05 R15 | PASS | PASS | PASS | PASS | Target PASS | PASS | Consistency check in E-8.5 inline; E-8.75 reports without re-deriving |
| V-03 | Phrasing register | V-01 | PASS | PASS | PASS | PASS | Prediction TBD | PASS | Reader-audit framing: spec narrates what reviewer checks rather than prescribing assertions |
| V-04 | Combination | V-01+V-02 | PASS | PASS | PASS | PASS | Target PASS | PASS | E-8.5 inline + E-8.75 cross-check: two-level consistency architecture |
| V-05 | Full combination | V-04 | PASS | PASS | PASS | PASS | Target PASS | Target PASS | C-38 promoted to named axiom; E-8.75 mandatory every re-sealing; C-38 record in Packet |

**C-37 architecture**: V-01 -- post-derivation audit in E-8.75. V-02 -- derivation-time
inline in E-8.5. V-03 -- audit-framing description. V-04 -- both levels. V-05 -- both
levels, mandatory re-check. Consistency test in all cases: `Contestation rule:`
ALTERNATIVE_VECTOR must differ from net vector `Rule applied:` produced; Adjacent verb
from `Contestation rule:` must differ from Recommendation verb.

**C-38 architecture**: V-01 through V-04 inherit the `Vector status: REVISED` trigger from
V-05 R15 (embedded in step c). V-05 promotes it to a named axiom preceding the numbered
steps -- the FORMAT BLOCK declaration is the sole trigger, informal vector assessment
explicitly excluded.
