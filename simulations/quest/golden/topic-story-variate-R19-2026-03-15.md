---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 19
rubric: v18
---

# Variations -- topic-story (Round 19)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v18 rubric adds C-46 (Named sub-step labels as beat-internal positioning
anchors) and C-47 (Flip-conditional sentence template). Both extracted from V-03 R18
excellence signals — the highest-scoring variation in round history at 36/38 aspirational
(95%) against v17. V-03 R18 scored ceiling (190.0) against v17; the two criteria it failed
(C-46, C-47) did not exist yet. R19 target: C-46 PASS + C-47 PASS = new ceiling.

From Round 18 scoring against v17 (ceiling 190.0):

- V-03, V-04, V-05 R18: all 190.0 (ceiling). Against v18 (40 aspirational): C-46 FAIL,
  C-47 FAIL for all. Score unchanged: 190.0.
- R19 delta available: C-46 PASS = +2.5, C-47 PASS = +2.5. Total: +5.0.
- R19 ceiling: 195.0.

**C-46 mechanism** (Named sub-step labels as beat-internal positioning anchors):
Beat-internal sub-steps must carry the positional requirement in the LABEL NAME itself,
not in a separate instruction. The scorecard note: *"named sub-step labels align precisely
with criteria that require checks to be positioned within beats."* The label encodes both
action and position: `Necessity test (apply before finalizing this beat):` means the model
reads the position and the action in a single token sequence. A label that says only
`Sub-step:` or `Check:` without the positional qualifier fails C-46 even if the positional
requirement appears in surrounding prose.

**C-47 mechanism** (Flip-conditional sentence template):
The Beat 4.5 `Conditions:` field must supply a literal fill-in sentence template for both
resolution branches of the flip conditional. Scorecard note: *"sentence template for flip
conditional reduces variance on criteria requiring both resolution branches to be named."*
The template: `If [{open question}] resolves as [{favorable}], the verdict holds. If
[{open question}] resolves as [{unfavorable}], the verdict changes to [{adjacent verb}].`
Describing the requirement abstractly (`Conditions: {finding or threshold...}`) fails C-47
because the model must infer the template shape; supplying the template eliminates that
inference.

**R19 isolation design:**

| Variation | Base | C-46 | C-47 | Axis |
|-----------|------|------|------|------|
| V-01 | V-03 R18 | Target PASS | FAIL | Lifecycle: named sub-step labels in beats |
| V-02 | V-03 R18 | FAIL | Target PASS | Output format: flip-conditional sentence template |
| V-03 | V-03 R18 | PARTIAL? | FAIL | Phrasing: positional qualifier prose, no label-name encoding |
| V-04 | V-03 R18 | Target PASS | Target PASS | Combination: C-46 + C-47 (V-03 R18 base) |
| V-05 | V-04 R18 (axiom) | Target PASS | Target PASS | Combination: C-46 + C-47 + candidate C-48 |

**Expected scores (v18, total max 195.0):**

| Variation | Expected | Remaining gap |
|-----------|----------|---------------|
| V-01 | 192.5 | C-47 FAIL |
| V-02 | 192.5 | C-46 FAIL |
| V-03 | 190.0 or 192.5 | C-47 FAIL; C-46 PARTIAL (label present, no name-encoded position) |
| V-04 | 195.0 | none (ceiling) |
| V-05 | 195.0 | none (ceiling via axiom grammar + C-48 candidate) |

If V-03 scores 192.5: label presence alone satisfies C-46; name-encoding is not required.
If V-03 scores 190.0: C-46 requires the positional requirement encoded in the label name.

V-04 vs V-05 tests whether the axiom grammar base (V-04 R18) also reaches ceiling when
C-46 and C-47 are added. V-05's candidate C-48 (Beat 4 Named Resolution Path per item) is
the R20 aspiration mechanism.

---

## V-01

**Variation axis**: Lifecycle emphasis -- named sub-step labels as beat-internal positioning
anchors. Single axis.

**Hypothesis**: C-46 is satisfied by adding named sub-step labels to Beat 3, Beat 4, and
Beat 5 in the AUTHOR phase, where each label encodes the positional requirement in its
name. The label `Pattern necessity test (apply before finalizing this beat):` carries both
the action (necessity test) and the position (before finalizing), eliminating the need to
read surrounding prose for the positional requirement. C-47 is not targeted: Beat 4.5
Conditions retains the abstract `{finding or threshold}` prose form. Expected: C-46 PASS,
C-47 FAIL. Score: 192.5.

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

- CONFIRMED/HIGH: Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Holds unless HIGH-weight or 2+ MEDIUM CONTRADICTS.
- CONFIRMED/LOW: Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Does not independently force QUALIFIED.
- QUALIFIED/LOW: Negligible downward pressure.
- REVERSED/HIGH-dominant: Single HIGH CONTRADICTS flips CONFIRMED unless 2+ HIGH CONFIRMS.
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
  C-38 compliance:
    Trigger: Writing `Vector status: REVISED` in the FORMAT BLOCK IS the E-8.5 firing --
      both occur in step b as a single integrated operation (step-integration). Writing
      `Vector status: UNCHANGED` IS the UNCHANGED terminal outcome. No step after step b
      reads the FORMAT BLOCK. The written value determines execution immediately within
      step b.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed within step b;
      E-8.5 re-run complete before step b finished; new Contestation output sealed] |
      [UNCHANGED -- Contestation rule carried forward; no E-8.5 re-run; prior output
      retained]
  Branch Architecture Record:
    REVISED branch: `Vector status: REVISED` written in step b -> VECTOR-STATUS FIRING
      RULE executes; the written value IS the branch determination (constitutive) ->
      E-8.5 runs immediately as an integrated sub-operation within step b -> new
      Contestation output produced -> E-4 `Contestation rule:` updated -> step b
      completes (E-8.5 PASS is the completion condition) -> E-8.75 re-runs (mandatory)
      -> re-seal with new Contestation data. Terminal state: new Contestation derivation
      sealed; prior output superseded. Causal chain: declaration -> E-8.5 within step b
      -> E-4 update -> step b done -> E-8.75 -> re-seal.
    UNCHANGED branch: `Vector status: UNCHANGED` written in step b -> VECTOR-STATUS
      FIRING RULE constitutes UNCHANGED terminal outcome -> E-8.5 does NOT run -> no
      Contestation re-derivation -> `Contestation rule:` carried forward verbatim from
      prior sealed Packet -> step b completes immediately -> E-8.75 re-runs (mandatory)
      -> re-seal with prior Contestation data retained. Terminal state: prior Contestation
      derivation retained. Causal chain: declaration -> no E-8.5 -> prior output retained
      -> step b done -> E-8.75 -> re-seal.
    Auditor can derive either terminal state from this record without protocol access.
    Both branches fully specified; neither requires inference.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 compliance record (Trigger + Evaluation outcome) and
    Branch Architecture Record (C-42) is structurally incomplete.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

**VECTOR-STATUS FIRING RULE** (named above numbered steps): The `Vector status:` value
written in the Re-sealing Reconciliation Decision FORMAT BLOCK in step b is the execution
branch point. Writing `Vector status: REVISED` in step b IS the firing of E-8.5 -- E-8.5
runs immediately as part of step b, before step b is complete. Writing `Vector status:
UNCHANGED` in step b IS the UNCHANGED terminal outcome -- `Contestation rule:` is carried
forward and E-8.5 does not run. No step after step b reads the FORMAT BLOCK to determine
which path executes. The written value determines execution immediately, within the step
that produces it. Both terminal branches (REVISED and UNCHANGED) are fully specified;
neither path requires inference.

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

      REVISED path (execute now, within this step, if `Vector status: REVISED` was written):
        Re-run E-8.5. Inline assertions must HOLD.
        Update E-4 `Contestation rule:` from new Contestation output.
        Step b is not complete until E-8.5 produces PASS and E-4 is updated.

      UNCHANGED path (if `Vector status: UNCHANGED` was written):
        `Contestation rule:` is carried forward unchanged. Proceed to step c.

   c. E-5, E-6, E-7 updates.

   d. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   e. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if REVISED path ran E-8.5), updated C-35/C-37
      records, updated C-38 compliance record with both sub-fields (Trigger + Evaluation
      outcome), and updated Branch Architecture Record confirming which terminal branch
      executed with its full causal chain.

3. Resume AUTHOR.

---

### AUTHOR Phase

Derive all content from sealed Derivation Packet. `Rule applied:` and `Contestation rule:`
read verbatim from Packet. AUTHOR does not derive, select, or modify either value.

**Beat 1**: Question, S0 from Packet, entering default.

**Beat 2**: Editorial sentence per signal. Highest-weight first.

**Beat 3**: Pattern synthesis. Dominant claim, boundary, trajectory.

Cross-signal scan (complete before drafting this beat):
Confirm every claim references two or more artifacts. A claim derivable from a single
artifact does not qualify. Do not draft until scan is complete.

Pattern necessity test (apply before finalizing this beat):
Does the dominant claim name a relationship, tension, or gap -- not a collection of
findings? A claim of form "A said X and B said Y" fails. The claim must synthesize.
If fails: redraft before closing this beat.

Proportionality audit (required final act before closing this beat):
Is the claim weight consistent with HIGH-weight evidence and trajectory from E-3?
If the trajectory is DIVERGING or MIXED, the claim must acknowledge the split.
Seal the inventory only after this audit passes.

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

Auto-transfer check (apply before finalizing this beat):
Verify every UNRESOLVED row from E-5 appears here. No additions, no omissions.
Do not close this beat until count matches E-5 UNRESOLVED count.

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
   C-37: two-level verified. C-38: REVISED written in step b IS the firing (step-
   integration, C-43 PASS). C-41: Evaluation outcome sealed. C-42: Branch Architecture
   Record in Packet with full causal chains for both terminal paths.]
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

Verdict alignment check (required before writing this beat):
Confirm Selected stance in Packet matches Recommendation verb in Beat 4.5 exactly.
Confirm one-sentence reversal condition names a specific finding, not a generic hedge.
Do not write Beat 5 prose until both checks pass.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 compliance, Branch Architecture
Record) | Conflict Register | Story beats 1-5

---

## V-02

**Variation axis**: Output format -- flip-conditional sentence template in Beat 4.5
Conditions field. Single axis.

**Hypothesis**: C-47 is satisfied by replacing the abstract `Conditions: {finding or
threshold...}` prose with a literal fill-in sentence template that names both resolution
branches. The template `If [{open question}] resolves as [{favorable}], the verdict holds.
If [{open question}] resolves as [{unfavorable}], the verdict changes to [{adjacent verb}].`
forces the model to name both branches explicitly, eliminating the variance that comes from
inferring the template shape. C-46 is not targeted: no named sub-step labels are added to
beats. Expected: C-47 PASS, C-46 FAIL. Score: 192.5.

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

- CONFIRMED/HIGH: Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Holds unless HIGH-weight or 2+ MEDIUM CONTRADICTS.
- CONFIRMED/LOW: Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Does not independently force QUALIFIED.
- QUALIFIED/LOW: Negligible downward pressure.
- REVERSED/HIGH-dominant: Single HIGH CONTRADICTS flips CONFIRMED unless 2+ HIGH CONFIRMS.
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
  C-38 compliance:
    Trigger: Writing `Vector status: REVISED` in the FORMAT BLOCK IS the E-8.5 firing --
      both occur in step b as a single integrated operation (step-integration). Writing
      `Vector status: UNCHANGED` IS the UNCHANGED terminal outcome. No step after step b
      reads the FORMAT BLOCK. The written value determines execution immediately within
      step b.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed within step b;
      E-8.5 re-run complete before step b finished; new Contestation output sealed] |
      [UNCHANGED -- Contestation rule carried forward; no E-8.5 re-run; prior output
      retained]
  Branch Architecture Record:
    REVISED branch: `Vector status: REVISED` written in step b -> VECTOR-STATUS FIRING
      RULE executes; the written value IS the branch determination (constitutive) ->
      E-8.5 runs immediately as an integrated sub-operation within step b -> new
      Contestation output produced -> E-4 `Contestation rule:` updated -> step b
      completes (E-8.5 PASS is the completion condition) -> E-8.75 re-runs (mandatory)
      -> re-seal with new Contestation data. Terminal state: new Contestation derivation
      sealed; prior output superseded. Causal chain: declaration -> E-8.5 within step b
      -> E-4 update -> step b done -> E-8.75 -> re-seal.
    UNCHANGED branch: `Vector status: UNCHANGED` written in step b -> VECTOR-STATUS
      FIRING RULE constitutes UNCHANGED terminal outcome -> E-8.5 does NOT run -> no
      Contestation re-derivation -> `Contestation rule:` carried forward verbatim from
      prior sealed Packet -> step b completes immediately -> E-8.75 re-runs (mandatory)
      -> re-seal with prior Contestation data retained. Terminal state: prior Contestation
      derivation retained. Causal chain: declaration -> no E-8.5 -> prior output retained
      -> step b done -> E-8.75 -> re-seal.
    Auditor can derive either terminal state from this record without protocol access.
    Both branches fully specified; neither requires inference.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 compliance record (Trigger + Evaluation outcome) and
    Branch Architecture Record (C-42) is structurally incomplete.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

**VECTOR-STATUS FIRING RULE** (named above numbered steps): The `Vector status:` value
written in the Re-sealing Reconciliation Decision FORMAT BLOCK in step b is the execution
branch point. Writing `Vector status: REVISED` in step b IS the firing of E-8.5 -- E-8.5
runs immediately as part of step b, before step b is complete. Writing `Vector status:
UNCHANGED` in step b IS the UNCHANGED terminal outcome -- `Contestation rule:` is carried
forward and E-8.5 does not run. No step after step b reads the FORMAT BLOCK to determine
which path executes. The written value determines execution immediately, within the step
that produces it. Both terminal branches (REVISED and UNCHANGED) are fully specified;
neither path requires inference.

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

      REVISED path (execute now, within this step, if `Vector status: REVISED` was written):
        Re-run E-8.5. Inline assertions must HOLD.
        Update E-4 `Contestation rule:` from new Contestation output.
        Step b is not complete until E-8.5 produces PASS and E-4 is updated.

      UNCHANGED path (if `Vector status: UNCHANGED` was written):
        `Contestation rule:` is carried forward unchanged. Proceed to step c.

   c. E-5, E-6, E-7 updates.

   d. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   e. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if REVISED path ran E-8.5), updated C-35/C-37
      records, updated C-38 compliance record with both sub-fields (Trigger + Evaluation
      outcome), and updated Branch Architecture Record confirming which terminal branch
      executed with its full causal chain.

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
   C-37: two-level verified. C-38: REVISED written in step b IS the firing (step-
   integration, C-43 PASS). C-41: Evaluation outcome sealed. C-42: Branch Architecture
   Record in Packet with full causal chains for both terminal paths.]
Flip conditional:
  If [{open question from Beat 4}] resolves as [{favorable outcome}], the verdict holds.
  If [{open question from Beat 4}] resolves as [{unfavorable outcome}], the verdict
    changes to [{Adjacent verb}].
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 compliance, Branch Architecture
Record) | Conflict Register | Story beats 1-5

---

## V-03

**Variation axis**: Phrasing register -- positional qualifier in prose without label-name
encoding. Single axis.

**Hypothesis**: C-46 requires the positional requirement to be encoded IN the label name
itself. If a sub-step is labeled `Sub-step (before finalizing):` rather than `Necessity
test (apply before finalizing this beat):`, the positional qualifier appears in parentheses
but the label name itself (`Sub-step`) carries no positional meaning. Tests whether C-46
requires action + position fused into the label token, or whether any positional language
adjacent to a label name satisfies the criterion. C-47 is not targeted. Expected: C-46
PARTIAL (label present without name-fused position), C-47 FAIL. Score: 190.0 or 192.5.

Discriminator: if V-03 scores 192.5 (same as V-01/V-02), the label name does not need to
carry the positional requirement -- proximity is sufficient. If V-03 scores 190.0, C-46
requires the positional requirement fused into the label name, not just nearby.

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

- CONFIRMED/HIGH: Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Holds unless HIGH-weight or 2+ MEDIUM CONTRADICTS.
- CONFIRMED/LOW: Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Does not independently force QUALIFIED.
- QUALIFIED/LOW: Negligible downward pressure.
- REVERSED/HIGH-dominant: Single HIGH CONTRADICTS flips CONFIRMED unless 2+ HIGH CONFIRMS.
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
  C-38 compliance:
    Trigger: Writing `Vector status: REVISED` in the FORMAT BLOCK IS the E-8.5 firing --
      both occur in step b as a single integrated operation (step-integration). Writing
      `Vector status: UNCHANGED` IS the UNCHANGED terminal outcome. No step after step b
      reads the FORMAT BLOCK. The written value determines execution immediately within
      step b.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed within step b;
      E-8.5 re-run complete before step b finished; new Contestation output sealed] |
      [UNCHANGED -- Contestation rule carried forward; no E-8.5 re-run; prior output
      retained]
  Branch Architecture Record:
    REVISED branch: `Vector status: REVISED` written in step b -> VECTOR-STATUS FIRING
      RULE executes; the written value IS the branch determination (constitutive) ->
      E-8.5 runs immediately as an integrated sub-operation within step b -> new
      Contestation output produced -> E-4 `Contestation rule:` updated -> step b
      completes (E-8.5 PASS is the completion condition) -> E-8.75 re-runs (mandatory)
      -> re-seal with new Contestation data. Terminal state: new Contestation derivation
      sealed; prior output superseded. Causal chain: declaration -> E-8.5 within step b
      -> E-4 update -> step b done -> E-8.75 -> re-seal.
    UNCHANGED branch: `Vector status: UNCHANGED` written in step b -> VECTOR-STATUS
      FIRING RULE constitutes UNCHANGED terminal outcome -> E-8.5 does NOT run -> no
      Contestation re-derivation -> `Contestation rule:` carried forward verbatim from
      prior sealed Packet -> step b completes immediately -> E-8.75 re-runs (mandatory)
      -> re-seal with prior Contestation data retained. Terminal state: prior Contestation
      derivation retained. Causal chain: declaration -> no E-8.5 -> prior output retained
      -> step b done -> E-8.75 -> re-seal.
    Auditor can derive either terminal state from this record without protocol access.
    Both branches fully specified; neither requires inference.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 compliance record (Trigger + Evaluation outcome) and
    Branch Architecture Record (C-42) is structurally incomplete.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

**VECTOR-STATUS FIRING RULE** (named above numbered steps): The `Vector status:` value
written in the Re-sealing Reconciliation Decision FORMAT BLOCK in step b is the execution
branch point. Writing `Vector status: REVISED` in step b IS the firing of E-8.5 -- E-8.5
runs immediately as part of step b, before step b is complete. Writing `Vector status:
UNCHANGED` in step b IS the UNCHANGED terminal outcome -- `Contestation rule:` is carried
forward and E-8.5 does not run. No step after step b reads the FORMAT BLOCK to determine
which path executes. The written value determines execution immediately, within the step
that produces it. Both terminal branches (REVISED and UNCHANGED) are fully specified;
neither path requires inference.

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

      REVISED path (execute now, within this step, if `Vector status: REVISED` was written):
        Re-run E-8.5. Inline assertions must HOLD.
        Update E-4 `Contestation rule:` from new Contestation output.
        Step b is not complete until E-8.5 produces PASS and E-4 is updated.

      UNCHANGED path (if `Vector status: UNCHANGED` was written):
        `Contestation rule:` is carried forward unchanged. Proceed to step c.

   c. E-5, E-6, E-7 updates.

   d. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   e. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if REVISED path ran E-8.5), updated C-35/C-37
      records, updated C-38 compliance record with both sub-fields (Trigger + Evaluation
      outcome), and updated Branch Architecture Record confirming which terminal branch
      executed with its full causal chain.

3. Resume AUTHOR.

---

### AUTHOR Phase

Derive all content from sealed Derivation Packet. `Rule applied:` and `Contestation rule:`
read verbatim from Packet. AUTHOR does not derive, select, or modify either value.

**Beat 1**: Question, S0 from Packet, entering default.

**Beat 2**: Editorial sentence per signal. Highest-weight first.

**Beat 3**: Pattern synthesis. Dominant claim, boundary, trajectory.

Sub-step (before drafting this beat): confirm every claim references two or more artifacts.

Sub-step (before finalizing this beat): confirm the dominant claim names a relationship or
tension, not a collection of findings. A claim derivable from a single artifact fails.

Sub-step (required before closing this beat): confirm claim weight is consistent with
HIGH-weight evidence and trajectory.

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

Sub-step (before finalizing this beat): verify UNRESOLVED count matches E-5.

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
   C-37: two-level verified. C-38: REVISED written in step b IS the firing (step-
   integration, C-43 PASS). C-41: Evaluation outcome sealed. C-42: Branch Architecture
   Record in Packet with full causal chains for both terminal paths.]
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

Sub-step (before writing this beat): confirm Selected stance in Packet matches
Recommendation verb in Beat 4.5.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 compliance, Branch Architecture
Record) | Conflict Register | Story beats 1-5

---

## V-04

**Variation axis**: Combination -- C-46 named sub-step labels + C-47 flip-conditional
sentence template. V-03 R18 base.

**Hypothesis**: Adding both C-46 (named sub-step labels with fused positional requirements)
and C-47 (flip-conditional sentence template) to the V-03 R18 base reaches the v18 ceiling.
C-46 adds beat-internal sub-step labels to Beat 3, Beat 4, and Beat 5 where the label NAME
encodes both the action and the position. C-47 replaces the abstract Conditions field with
a literal fill-in two-branch template. All prior criteria (C-39 through C-45) are inherited
from V-03 R18. Expected: C-46 PASS, C-47 PASS. Score: 195.0 (ceiling).

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

- CONFIRMED/HIGH: Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Holds unless HIGH-weight or 2+ MEDIUM CONTRADICTS.
- CONFIRMED/LOW: Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Does not independently force QUALIFIED.
- QUALIFIED/LOW: Negligible downward pressure.
- REVERSED/HIGH-dominant: Single HIGH CONTRADICTS flips CONFIRMED unless 2+ HIGH CONFIRMS.
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
  C-38 compliance:
    Trigger: Writing `Vector status: REVISED` in the FORMAT BLOCK IS the E-8.5 firing --
      both occur in step b as a single integrated operation (step-integration). Writing
      `Vector status: UNCHANGED` IS the UNCHANGED terminal outcome. No step after step b
      reads the FORMAT BLOCK. The written value determines execution immediately within
      step b.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed within step b;
      E-8.5 re-run complete before step b finished; new Contestation output sealed] |
      [UNCHANGED -- Contestation rule carried forward; no E-8.5 re-run; prior output
      retained]
  Branch Architecture Record:
    REVISED branch: `Vector status: REVISED` written in step b -> VECTOR-STATUS FIRING
      RULE executes; the written value IS the branch determination (constitutive) ->
      E-8.5 runs immediately as an integrated sub-operation within step b -> new
      Contestation output produced -> E-4 `Contestation rule:` updated -> step b
      completes (E-8.5 PASS is the completion condition) -> E-8.75 re-runs (mandatory)
      -> re-seal with new Contestation data. Terminal state: new Contestation derivation
      sealed; prior output superseded. Causal chain: declaration -> E-8.5 within step b
      -> E-4 update -> step b done -> E-8.75 -> re-seal.
    UNCHANGED branch: `Vector status: UNCHANGED` written in step b -> VECTOR-STATUS
      FIRING RULE constitutes UNCHANGED terminal outcome -> E-8.5 does NOT run -> no
      Contestation re-derivation -> `Contestation rule:` carried forward verbatim from
      prior sealed Packet -> step b completes immediately -> E-8.75 re-runs (mandatory)
      -> re-seal with prior Contestation data retained. Terminal state: prior Contestation
      derivation retained. Causal chain: declaration -> no E-8.5 -> prior output retained
      -> step b done -> E-8.75 -> re-seal.
    Auditor can derive either terminal state from this record without protocol access.
    Both branches fully specified; neither requires inference.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 compliance record (Trigger + Evaluation outcome) and
    Branch Architecture Record (C-42) is structurally incomplete.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

**VECTOR-STATUS FIRING RULE** (named above numbered steps): The `Vector status:` value
written in the Re-sealing Reconciliation Decision FORMAT BLOCK in step b is the execution
branch point. Writing `Vector status: REVISED` in step b IS the firing of E-8.5 -- E-8.5
runs immediately as part of step b, before step b is complete. Writing `Vector status:
UNCHANGED` in step b IS the UNCHANGED terminal outcome -- `Contestation rule:` is carried
forward and E-8.5 does not run. No step after step b reads the FORMAT BLOCK to determine
which path executes. The written value determines execution immediately, within the step
that produces it. Both terminal branches (REVISED and UNCHANGED) are fully specified;
neither path requires inference.

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

      REVISED path (execute now, within this step, if `Vector status: REVISED` was written):
        Re-run E-8.5. Inline assertions must HOLD.
        Update E-4 `Contestation rule:` from new Contestation output.
        Step b is not complete until E-8.5 produces PASS and E-4 is updated.

      UNCHANGED path (if `Vector status: UNCHANGED` was written):
        `Contestation rule:` is carried forward unchanged. Proceed to step c.

   c. E-5, E-6, E-7 updates.

   d. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   e. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if REVISED path ran E-8.5), updated C-35/C-37
      records, updated C-38 compliance record with both sub-fields (Trigger + Evaluation
      outcome), and updated Branch Architecture Record confirming which terminal branch
      executed with its full causal chain.

3. Resume AUTHOR.

---

### AUTHOR Phase

Derive all content from sealed Derivation Packet. `Rule applied:` and `Contestation rule:`
read verbatim from Packet. AUTHOR does not derive, select, or modify either value.

**Beat 1**: Question, S0 from Packet, entering default.

**Beat 2**: Editorial sentence per signal. Highest-weight first.

**Beat 3**: Pattern synthesis. Dominant claim, boundary, trajectory.

Cross-signal scan (complete before drafting this beat):
Confirm every pattern claim references two or more artifacts. A claim derivable from a
single artifact does not qualify. Do not draft Beat 3 until scan is complete.

Pattern necessity test (apply before finalizing this beat):
Does the dominant claim name a relationship, tension, or gap -- not a collection of
findings? A claim of form "A said X and B said Y" fails the necessity test; the claim must
synthesize what those signals say together. If fails: redraft claim before sealing inventory.

Proportionality audit (required final act before closing this beat):
Is the claim weight consistent with HIGH-weight evidence, UNRESOLVED count, and trajectory
from E-3? If trajectory is DIVERGING or MIXED, claim must acknowledge the split explicitly.
Seal the Beat 3 Inventory only after this audit passes.

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

Completeness gate (apply before finalizing this beat):
Count UNRESOLVED items in E-5. Verify Beat 4 item count matches. No additions, no omissions.
Beat 4 is not complete until count match is confirmed.

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
   C-37: two-level verified. C-38: REVISED written in step b IS the firing (step-
   integration, C-43 PASS). C-41: Evaluation outcome sealed. C-42: Branch Architecture
   Record in Packet with full causal chains for both terminal paths.]
Flip conditional:
  If [{open question from Beat 4}] resolves as [{favorable outcome}], the verdict holds.
  If [{open question from Beat 4}] resolves as [{unfavorable outcome}], the verdict
    changes to [{Adjacent verb}].
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

Verdict alignment check (required before writing this beat):
Confirm Packet Selected stance matches Recommendation verb in Beat 4.5 exactly.
Confirm reversal condition names a specific finding from Beat 4, not a generic hedge.
Do not write Beat 5 prose until both conditions are confirmed.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 compliance, Branch Architecture
Record) | Conflict Register | Story beats 1-5

---

## V-05

**Variation axis**: Combination -- C-46 + C-47 on axiom grammar base (V-04 R18), with
candidate C-48 mechanism (Beat 4 Named Resolution Path per item).

**Hypothesis**: The axiom grammar base (V-04 R18) provides an independent path to C-38/C-39
that is architecturally distinct from V-03 R18's step-integration path. Adding C-46 (named
sub-step labels) and C-47 (flip-conditional template) to V-04 R18's AUTHOR phase should
reach ceiling by the same mechanism as V-04. Additionally, each Beat 4 UNRESOLVED item is
tagged with a named resolution path (`SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH`),
making Beat 4 a structured triage rather than a bare list. This resolution path tagging is
the candidate C-48 mechanism for v19: it adds FORMAT constraint to Beat 4 items analogous
to how C-44 added FORMAT constraint to gathering actions. Expected: C-46 PASS, C-47 PASS,
candidate C-48 present. Score: 195.0 (ceiling via axiom grammar path).

If V-05 scores the same as V-04, the axiom grammar architecture is confirmed ceiling-
equivalent to step-integration for C-46/C-47. If V-05 underscores V-04, the axiom grammar
path has a structural incompatibility with the named sub-step label mechanism.

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

- CONFIRMED/HIGH: Locks CONFIRMED unless 2+ HIGH-weight CONTRADICTS.
- CONFIRMED/MEDIUM: Holds unless HIGH-weight or 2+ MEDIUM CONTRADICTS.
- CONFIRMED/LOW: Single MEDIUM- or HIGH-weight CONTRADICTS reduces to QUALIFIED.
- CONFIRMED/CLEAR: No prior state; additive.
- QUALIFIED/HIGH: Holds QUALIFIED floor.
- QUALIFIED/MEDIUM: Does not independently force QUALIFIED.
- QUALIFIED/LOW: Negligible downward pressure.
- REVERSED/HIGH-dominant: Single HIGH CONTRADICTS flips CONFIRMED unless 2+ HIGH CONFIRMS.
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
  C-38 compliance:
    AXIOM: REVISED IS the E-8.5 re-derivation event (constitutive, C-39 PASS). Declaring
      `Vector status: REVISED` does not trigger E-8.5 -- it IS E-8.5. The act of writing
      REVISED in step b is constitutively identical to performing E-8.5. Declaring
      `Vector status: UNCHANGED` IS the UNCHANGED terminal outcome: no E-8.5 runs because
      UNCHANGED declares the absence of the re-derivation event, not its deferral.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed within step b;
      E-8.5 re-run complete before step b finished; new Contestation output sealed] |
      [UNCHANGED -- Contestation rule carried forward; no E-8.5 re-run; prior output
      retained]
  Branch Architecture Record:
    REVISED branch: Declaring `Vector status: REVISED` IS the E-8.5 re-derivation (AXIOM);
      E-8.5 runs as a constitutive sub-operation of step b; the written value is not a
      trigger but the event itself; new Contestation output produced within step b ->
      E-4 `Contestation rule:` updated -> step b completes (E-8.5 is step b's completion
      condition per AXIOM) -> E-8.75 re-runs -> re-seal. Terminal state: new derivation
      sealed; prior superseded. Causal chain: AXIOM constitutive -> E-8.5 within step b
      -> E-4 update -> step b done -> E-8.75 -> re-seal.
    UNCHANGED branch: Declaring `Vector status: UNCHANGED` IS the UNCHANGED outcome
      (AXIOM); E-8.5 absence is constitutive, not a consequence; `Contestation rule:`
      carried forward verbatim -> step b completes immediately -> E-8.75 re-runs ->
      re-seal. Terminal state: prior derivation retained. Causal chain: AXIOM constitutive
      -> no E-8.5 -> prior output retained -> step b done -> E-8.75 -> re-seal.
    Auditor can derive either terminal state from this record without protocol access.
    Both branches fully specified; neither requires inference.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 compliance record (AXIOM + Evaluation outcome) and
    Branch Architecture Record (C-42) is structurally incomplete.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

**VECTOR-STATUS AXIOM** (named above numbered steps): Declaring `Vector status: REVISED`
in the Re-sealing Reconciliation Decision FORMAT BLOCK in step b IS the E-8.5
re-derivation event -- constitutively, not causally. Declaring `Vector status: UNCHANGED`
IS the UNCHANGED terminal outcome -- constitutively; E-8.5 absence is declared, not
inferred. Both terminal branches (REVISED and UNCHANGED) are fully specified; neither
path requires inference. The AXIOM is not a trigger; it is the definition of what these
declarations mean.

If AUTHOR discovers a conflict while writing:

1. STOP.
2. Return to EVALUATOR:

   a. E-2 update.

   b. E-4 update. Produce Re-sealing Reconciliation Decision:

      ```
      Re-sealing Reconciliation Decision:
        Rule re-executed: {VECTOR}/{WEIGHT_LEVEL} rule -- [rule applied to new/revised entry]
        Vector status: UNCHANGED | REVISED from {OLD} to {NEW}
        [If REVISED]: AXIOM: this declaration IS E-8.5 re-derivation. Run E-8.5 now,
          within step b. Step b is not complete until E-8.5 produces PASS.
          Trigger: {artifact-name} ({weight}, {verdict type}) triggered
          {VECTOR}/{WEIGHT_LEVEL} rule -- consequence: [consequence]
      ```

      FORMAT BLOCK required even if vector unchanged.

      REVISED path (execute now, within this step, if `Vector status: REVISED` was written):
        AXIOM: This declaration IS E-8.5. Re-run E-8.5 immediately. Inline assertions
          must HOLD. Update E-4 `Contestation rule:` from new output. Step b is not
          complete until E-8.5 PASS and E-4 are both updated.

      UNCHANGED path (if `Vector status: UNCHANGED` was written):
        AXIOM: This declaration IS the UNCHANGED outcome. `Contestation rule:` carried
          forward unchanged. Proceed to step c.

   c. E-5, E-6, E-7 updates.

   d. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   e. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if REVISED path ran E-8.5), updated C-35/C-37
      records, updated C-38 compliance record with AXIOM framing and Evaluation outcome,
      and updated Branch Architecture Record with AXIOM-constitutive causal chains.

3. Resume AUTHOR.

---

### AUTHOR Phase

Derive all content from sealed Derivation Packet. `Rule applied:` and `Contestation rule:`
read verbatim from Packet. AUTHOR does not derive, select, or modify either value.

**Beat 1**: Question, S0 from Packet, entering default.

**Beat 2**: Editorial sentence per signal. Highest-weight first.

**Beat 3**: Pattern synthesis. Dominant claim, boundary, trajectory.

Cross-signal scan (complete before drafting this beat):
Confirm every pattern claim references two or more artifacts. A claim derivable from a
single artifact does not qualify. Do not draft Beat 3 until scan is complete.

Pattern necessity test (apply before finalizing this beat):
Does the dominant claim name a relationship, tension, or gap -- not a collection of
findings? A claim of form "A said X and B said Y" fails; the claim must synthesize what
those signals show together. If fails: redraft claim before sealing inventory.

Proportionality audit (required final act before closing this beat):
Is the claim weight consistent with HIGH-weight evidence, UNRESOLVED count, and trajectory
from E-3? If trajectory is DIVERGING or MIXED, the claim must acknowledge the split.
Seal the Beat 3 Inventory only after this audit passes.

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

**Beat 4**: UNRESOLVED conflicts. One sentence each. Per item:

```
- {conflict-ID}: {finding, one sentence}
  Resolution path: SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH
```

`Resolution path:` REQUIRED FORMAT FIELD per item. SIGNAL_PATH: resolvable by gathering
more signal artifacts. EXPERIMENT_PATH: resolvable by running a targeted experiment or
prototype. DECIDE_PATH: resolvable only by a human or team decision; no signal or
experiment can close it.

Completeness gate (apply before finalizing this beat):
Count UNRESOLVED items in E-5. Verify Beat 4 item count matches. Every item has
`Resolution path:` filled. Beat 4 is not complete until both checks pass.

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
   C-37: two-level verified. C-38: AXIOM -- REVISED IS E-8.5 (constitutive, C-39 PASS).
   C-41: Evaluation outcome sealed. C-42: Branch Architecture Record with AXIOM causal
   chains for both terminal paths.]
Flip conditional:
  If [{open question from Beat 4}] resolves as [{favorable outcome}], the verdict holds.
  If [{open question from Beat 4}] resolves as [{unfavorable outcome}], the verdict
    changes to [{Adjacent verb}].
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

Verdict alignment check (required before writing this beat):
Confirm Packet Selected stance matches Recommendation verb in Beat 4.5 exactly.
Confirm reversal condition names a specific finding from Beat 4, not a generic hedge.
Do not write Beat 5 prose until both conditions are confirmed.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 AXIOM compliance, Branch Architecture
Record with AXIOM causal chains) | Conflict Register | Story beats 1-5 (Beat 4 with
Resolution path tags)

---

## Summary

| | Axis | Base | C-46 | C-47 | Candidate C-48 | Key addition |
|---|---|---|---|---|---|---|
| V-01 | Lifecycle: named sub-step labels | V-03 R18 | Target PASS | FAIL | absent | Beat 3/4/5 sub-step labels with fused positional names |
| V-02 | Output format: flip-conditional template | V-03 R18 | FAIL | Target PASS | absent | Beat 4.5 two-branch fill-in template |
| V-03 | Phrasing: positional qualifier prose | V-03 R18 | PARTIAL? | FAIL | absent | Sub-step labels with position in parens, not in name |
| V-04 | Combination C-46 + C-47 | V-03 R18 | Target PASS | Target PASS | absent | Both mechanisms on step-integration base |
| V-05 | Combination C-46 + C-47 + C-48 | V-04 R18 (axiom) | Target PASS | Target PASS | present | Both mechanisms on axiom base + Beat 4 Resolution path |

**C-46 architecture**: V-01, V-04, V-05 all use named sub-step labels where the label
name itself carries the positional requirement: `Cross-signal scan (complete before
drafting this beat):` encodes both the action (scan) and the position (before drafting).
V-03 uses labels where position appears in parentheses but the label name (`Sub-step`) is
generic. V-03 vs V-01/V-04 discriminates whether label-name encoding is necessary for C-46
PASS or whether any positional language adjacent to a label name suffices.

**C-47 architecture**: V-02, V-04, V-05 replace the abstract `Conditions: {finding or
threshold...}` with a literal two-branch fill-in template in the Beat 4.5 block. The
template forces both resolution branches to be named explicitly and provides the structural
shape the model must fill. No reasoning about what shape the template should take;
the template is given. V-01 and V-03 retain the abstract form.

**Candidate C-48 architecture** (V-05 only): Each Beat 4 UNRESOLVED item is tagged with
`Resolution path: SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH`. This transforms Beat 4
from a bare UNRESOLVED list into a structured triage. SIGNAL_PATH items can be closed
by gathering more artifacts. EXPERIMENT_PATH items require a targeted prototype or
test. DECIDE_PATH items require human judgment and cannot be closed by signal work alone.
The Completeness gate in V-05 requires every item to have a Resolution path filled,
making this a FORMAT constraint on Beat 4 items. Candidate for v19 criterion C-48: Beat 4
Named Resolution Path -- each UNRESOLVED item must carry a `Resolution path:` field.

**V-04 vs V-05** tests whether the axiom grammar base (V-04 R18) reaches the v18 ceiling
via the same C-46/C-47 additions as V-04's step-integration base, and whether the
candidate C-48 mechanism produces any scoring differential above ceiling (which would
confirm it is not already covered by existing criteria).
