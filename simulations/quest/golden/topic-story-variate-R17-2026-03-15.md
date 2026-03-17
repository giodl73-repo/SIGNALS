---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 17
rubric: v16
---

# Variations -- topic-story (Round 17)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v16 rubric adds C-39 (Trigger Axiom Elevation with Constitutive
Mechanism), C-40 (Complete Vector-Status Branch Specification), and C-41 (Trigger
Compliance Sealed Record). All three are extracted from V-05 R16 mechanisms -- V-05 R16
was the only variation that achieved both C-37 PASS and C-38 PASS -- but at a precision
level V-05 R16 does not fully satisfy.

From Round 16:

- V-01 through V-04 R16: C-37 PASS, C-38 PASS (inherited formal trigger), C-39 PARTIAL,
  C-40 PASS (explicit REVISED + UNCHANGED branches), C-41 PARTIAL
- V-05 R16: C-37 PASS (two-level), C-38 PASS (named axiom above steps), C-39 PARTIAL
  (first requirement -- axiom above numbered steps -- SATISFIED; second requirement --
  FORMAT BLOCK declaration IS the trigger event, not a data source -- FAILS via step c's
  "read from" language), C-40 PASS (both branches explicitly named), C-41 PARTIAL
  (Packet records trigger definition, not evaluation outcome)

**C-39 gap analysis**: V-05 R16 C-38 AXIOM satisfies the first C-39 requirement: named
axiom promoted above numbered steps. Step c -- "C-38 trigger: read `Vector status:` from
FORMAT BLOCK" -- fails the second: "read from" frames FORMAT BLOCK as a data source that
step c queries. C-39 PASS requires the FORMAT BLOCK declaration to BE the trigger event --
writing "REVISED" fires E-8.5 immediately; no step reads the FORMAT BLOCK to decide
whether to fire. Two mechanism designs:

- **Axiom grammar change** (V-02, V-04): Rewrite the C-38 AXIOM as "Declaring
  `Vector status: REVISED` IS the re-derivation event." Restructure step c as two labeled
  terminal paths -- REVISED and UNCHANGED -- with no "read from" language. The AXIOM
  becomes constitutive; the paths are named outcomes, not trigger-check branches.

- **Step integration** (V-03, V-05): Replace the pre-step firing rule with a
  VECTOR-STATUS FIRING RULE that names the branch event. Embed E-8.5 inline within step b
  so that writing REVISED immediately runs E-8.5 as a sub-action of FORMAT BLOCK
  production. No separate step reads the FORMAT BLOCK post-declaration.

**C-40 gap analysis**: V-05 R16 step c names both REVISED (re-run E-8.5) and UNCHANGED
(do not re-run, carry forward). C-40 is PASS in V-05 R16 and all R16 variations with
explicit branch language. All R17 variations must preserve explicit REVISED and UNCHANGED
branch naming; none should lose C-40 by reducing to a single-branch protocol.

**C-41 gap analysis**: V-05 R16 Packet C-38 compliance states "trigger = `Vector status:
REVISED` in FORMAT BLOCK... declaration is authoritative." This records the trigger
definition only. After re-sealing, an auditor reading only the sealed Packet cannot
determine: (a) was C-38 evaluated in this re-sealing? (b) what was the outcome --
REVISED (E-8.5 re-ran, new Contestation output) or UNCHANGED (carried forward)? C-41
closes this by adding a named "Evaluation outcome:" field to the compliance record: either
"REVISED -- Contestation re-derived" or "UNCHANGED -- Contestation carried forward." The
field is additive; it does not modify the trigger definition or the AXIOM framing. It is
independent of C-39's mechanism choice.

**Round 17 isolation design:**

| Variation | C-37 | C-38 | C-39 | C-40 | C-41 | Axis |
|-----------|------|------|------|------|------|------|
| V-01 | PASS | PASS | PARTIAL | PASS | PASS | C-41 outcome record, V-05 R16 base unchanged |
| V-02 | PASS | PASS | PASS | PASS | PARTIAL | C-39 axiom grammar -- constitutive declaration |
| V-03 | PASS | PASS | PASS | PASS | PARTIAL | C-39 step-integration -- E-8.5 fires inside step b |
| V-04 | PASS | PASS | PASS | PASS | PASS | V-02 + V-01: axiom grammar + outcome record |
| V-05 | PASS | PASS | PASS | PASS | PASS | V-03 + V-01 + explicit C-40: step-integration + outcome record |

**Expected scores (v16, total max 185.0):**

V-05 R16 baseline against v16: ~182.5 (v15 ceiling ~177.5 + C-39 PARTIAL +1.25 +
C-40 PASS +2.5 + C-41 PARTIAL +1.25)

| Variation | Expected | Delta over V-05 R16 | Remaining PARTIAL |
|-----------|----------|---------------------|-------------------|
| V-01 | 183.75 | +1.25 | C-39 PARTIAL |
| V-02 | 183.75 | +1.25 | C-41 PARTIAL |
| V-03 | 183.75 | +1.25 | C-41 PARTIAL (different C-39 mechanism than V-02) |
| V-04 | 185.0 | +2.5 | none -- ceiling |
| V-05 | 185.0 | +2.5 | none -- ceiling, explicit C-40 confirmation |

V-04 and V-05 both target 185.0 via different C-39 mechanisms. If both score ceiling,
either mechanism satisfies C-39 PASS and R18 can use either as base. If they diverge,
the scoring establishes which constitutive form is canonical.

---

## V-01

**Variation axis**: C-41 outcome record -- minimal addition to V-05 R16. Single axis.

**Hypothesis**: V-05 R16 Packet C-38 compliance records the trigger definition but no
evaluation outcome. Adding a named "Evaluation outcome:" sub-field -- REVISED (E-8.5
re-ran) or UNCHANGED (carried forward) -- makes the trigger evaluation auditable from
the sealed Packet alone without re-reading the protocol execution trace. The change is
confined to two locations: (1) the Packet C-38 compliance field template in E-8, and
(2) a single requirement in step f that the outcome must be populated. All other
mechanisms inherit from V-05 R16 unchanged. C-39 remains PARTIAL (step c still uses
"read from"). C-40 remains PASS. C-41 prediction: PASS.

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
    Trigger: `Vector status: REVISED` in Re-sealing Reconciliation Decision FORMAT BLOCK
      is the sole re-derivation trigger. Informal assessment of vector change is not the
      trigger. The FORMAT BLOCK declaration is authoritative.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed; E-8.5 re-run
      complete, new Contestation output sealed in this Packet] | [UNCHANGED -- Contestation
      rule carried forward; no E-8.5 re-run; prior Contestation output retained]
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without both C-38 sub-fields (Trigger + Evaluation outcome) is
    incomplete -- both required for C-41 compliance.
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
      and updated C-38 compliance record with both sub-fields populated: Trigger
      (definition unchanged) and Evaluation outcome (REVISED -- Contestation re-derived,
      if step c ran E-8.5; or UNCHANGED -- Contestation rule carried forward, if step c
      did not run E-8.5).

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
   C-37: two-level verified. C-38: re-derivation trigger is FORMAT BLOCK REVISED declaration.
   C-41: Evaluation outcome sealed in Packet (REVISED or UNCHANGED).]
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

## V-02

**Variation axis**: C-39 constitutive axiom grammar -- the FORMAT BLOCK declaration IS
the trigger, not a data source step c reads. Base: V-05 R16. Single axis.

**Hypothesis**: V-05 R16 C-38 AXIOM satisfies C-39's first requirement (named axiom above
numbered steps) but fails the second via step c's "read from" gate. The fix is a grammar
change to the AXIOM: "declaring REVISED IS the firing event" removes all indirection --
the declaration and the trigger are the same act. Step c is then restructured as two
named terminal paths (REVISED path / UNCHANGED path) rather than a trigger-check that
reads the FORMAT BLOCK. Neither path uses "read from" language; each is a named outcome
with defined consequences. The constitutive grammar in the AXIOM eliminates bypass risk:
E-8.5 fires when REVISED is declared, not when a step decides to fire it. C-39 prediction:
PASS. C-41 inherits PARTIAL from V-05 R16 (Packet has no outcome field). C-40 inherits
PASS (both branches explicitly named in the terminal path structure).

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
  C-38 compliance: Declaring `Vector status: REVISED` in the Re-sealing Reconciliation
    Decision FORMAT BLOCK IS the Contestation rule re-derivation event -- the declaration
    and the trigger are the same act. Declaring `Vector status: UNCHANGED` IS the UNCHANGED
    terminal outcome. No step reads the FORMAT BLOCK post-declaration to decide whether to
    fire. The FORMAT BLOCK declaration is constitutive and authoritative.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 constitutive compliance record omits the re-derivation
    trigger declaration.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

**C-38 AXIOM**: Declaring `Vector status: REVISED` in step b IS the Contestation rule
re-derivation event. The FORMAT BLOCK is not a data source that a subsequent step reads
to decide whether to fire E-8.5. Writing `Vector status: REVISED` in the FORMAT BLOCK
constitutes the firing -- the declaration and the trigger are the same act. Writing
`Vector status: UNCHANGED` constitutes the UNCHANGED terminal outcome: `Contestation
rule:` is carried forward and E-8.5 does not run. No separate trigger-check step reads
the FORMAT BLOCK after it is written. Informal assessment of vector change is not
consulted. The FORMAT BLOCK declaration is constitutive and authoritative.

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

   c. REVISED terminal path (executed when step b declared `Vector status: REVISED`):
      Re-run E-8.5. Inline assertions must HOLD.
      Update E-4 `Contestation rule:` field with new Contestation output.

      UNCHANGED terminal path (executed when step b declared `Vector status: UNCHANGED`):
      Do not re-run E-8.5. `Contestation rule:` is carried forward from prior Packet.

   d. E-5, E-6, E-7 updates.

   e. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   f. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if REVISED path ran E-8.5), updated C-35/C-37 records,
      updated C-38 constitutive compliance record.

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
   C-37: two-level verified. C-38: declaring REVISED IS the firing event (constitutive).
   No step reads FORMAT BLOCK post-declaration to decide.]
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

## V-03

**Variation axis**: C-39 step-integration -- E-8.5 fires inside step b, no separate
trigger-check step. Base: V-05 R16. Single axis, different mechanism than V-02.

**Hypothesis**: V-02's constitutive grammar change reframes the AXIOM but leaves the
re-sealing steps structurally parallel to V-05 R16 (pre-step axiom + step c consuming
the FORMAT BLOCK value). An alternative approach: remove the pre-step firing rule and
integrate the REVISED branch E-8.5 execution directly inside step b -- the same step that
produces the FORMAT BLOCK. Writing `Vector status: REVISED` in the FORMAT BLOCK and
running E-8.5 are the same operation. No step c reads the FORMAT BLOCK; step b completes
both the declaration and its consequence before the next step begins. The VECTOR-STATUS
FIRING RULE (replacing the C-38 AXIOM) is still a named rule above numbered steps, still
identifies the branch event, but now names the FORMAT BLOCK production itself as where
the branch executes -- not as a source that a downstream step reads. C-39 prediction:
PASS (named rule above steps satisfies first requirement; FORMAT BLOCK production IS the
execution step satisfies second). C-41 inherits PARTIAL. C-40 inherits PASS.

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
  C-38 compliance: The VECTOR-STATUS FIRING RULE names step b as the execution point.
    Writing `Vector status: REVISED` in the FORMAT BLOCK IS the E-8.5 firing -- both occur
    in step b as a single integrated operation. Writing `Vector status: UNCHANGED` IS the
    UNCHANGED terminal outcome -- no E-8.5 re-run. No step reads the FORMAT BLOCK to
    decide; the written value determines execution immediately within step b.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 step-integration compliance record omits the
    re-derivation trigger.
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
that produces it. Informal assessment of vector change is not consulted.

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
        Step b is not complete until E-8.5 produces PASS.

      UNCHANGED path (if `Vector status: UNCHANGED` was written):
        `Contestation rule:` is carried forward unchanged. Proceed to step c.

   c. E-5, E-6, E-7 updates.

   d. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   e. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if REVISED path ran E-8.5), updated C-35/C-37 records,
      updated C-38 compliance record.

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
   C-37: two-level verified. C-38: REVISED declared in step b IS the E-8.5 firing
   (step-integration). No post-declaration read.]
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

## V-04

**Variation axis**: C-39 axiom grammar + C-41 outcome record. Combination of V-02 and V-01.

**Hypothesis**: C-39 and C-41 are orthogonal gaps. C-39 requires the trigger framing to
be constitutive (FORMAT BLOCK declaration IS the event). C-41 requires the sealed Packet
to record the evaluation outcome (REVISED or UNCHANGED). V-02 closes C-39 via axiom
grammar change; V-01 closes C-41 via the Evaluation outcome sub-field in the Packet.
Neither fix requires the other -- constitutive grammar does not produce an outcome record,
and an outcome record does not eliminate the "read from" framing. Combining them should
independently satisfy both criteria without interaction effects. Expected: C-39 PASS,
C-40 PASS, C-41 PASS. Score: 185.0 (ceiling).

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
    Trigger: Declaring `Vector status: REVISED` in the Re-sealing Reconciliation Decision
      FORMAT BLOCK IS the Contestation rule re-derivation event. The declaration and the
      trigger are the same act. Declaring `Vector status: UNCHANGED` IS the UNCHANGED
      terminal outcome. No step reads the FORMAT BLOCK post-declaration to decide. The
      FORMAT BLOCK declaration is constitutive and authoritative.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed; E-8.5 re-run
      complete, new Contestation output sealed in this Packet] | [UNCHANGED -- Contestation
      rule carried forward; no E-8.5 re-run; prior Contestation output retained]
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without both C-38 sub-fields (Trigger constitutive statement +
    Evaluation outcome) is incomplete -- both required.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

**C-38 AXIOM**: Declaring `Vector status: REVISED` in step b IS the Contestation rule
re-derivation event. The FORMAT BLOCK is not a data source that a subsequent step reads
to decide whether to fire E-8.5. Writing `Vector status: REVISED` in the FORMAT BLOCK
constitutes the firing -- the declaration and the trigger are the same act. Writing
`Vector status: UNCHANGED` constitutes the UNCHANGED terminal outcome: `Contestation
rule:` is carried forward and E-8.5 does not run. No separate trigger-check step reads
the FORMAT BLOCK after it is written. Informal assessment of vector change is not
consulted. The FORMAT BLOCK declaration is constitutive and authoritative.

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

   c. REVISED terminal path (executed when step b declared `Vector status: REVISED`):
      Re-run E-8.5. Inline assertions must HOLD.
      Update E-4 `Contestation rule:` field with new Contestation output.

      UNCHANGED terminal path (executed when step b declared `Vector status: UNCHANGED`):
      Do not re-run E-8.5. `Contestation rule:` is carried forward from prior Packet.

   d. E-5, E-6, E-7 updates.

   e. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   f. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if REVISED path ran E-8.5), updated C-35/C-37 records,
      and updated C-38 compliance record with both sub-fields: Trigger (constitutive
      statement) and Evaluation outcome (REVISED -- Contestation re-derived, if REVISED
      path executed; or UNCHANGED -- Contestation rule carried forward, if UNCHANGED
      path executed).

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
   C-37: two-level verified. C-38: declaring REVISED IS the firing (constitutive).
   C-41: Evaluation outcome sealed in Packet (REVISED or UNCHANGED).]
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

## V-05

**Variation axis**: C-39 step-integration + C-41 outcome record + explicit C-40
confirmation. Full combination targeting ceiling via V-03 C-39 mechanism.

**Hypothesis**: V-04 reaches ceiling via axiom grammar change (C-39) + outcome record
(C-41). V-05 reaches ceiling via step-integration (C-39) + outcome record (C-41) +
explicit C-40 branch record in the Packet. The explicit C-40 field tests whether naming
the complete branch specification in the sealed Packet (REVISED -> E-8.5 re-run;
UNCHANGED -> Contestation rule carried forward) adds any measurable score differential
over C-40 PASS from implicit naming. If V-04 and V-05 both score 185.0, the C-39
mechanism choice (axiom grammar vs step-integration) is equivalent for scoring purposes
and the explicit C-40 record is confirmed as non-scoring (already at PASS threshold).
If V-05 outscores V-04, the explicit C-40 record contributes beyond the PASS threshold.

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
      reads the FORMAT BLOCK to determine which path executes. The written value determines
      execution immediately within step b.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed within step b;
      E-8.5 re-run complete, new Contestation output sealed in this Packet] | [UNCHANGED
      -- Contestation rule carried forward; no E-8.5 re-run; prior Contestation output
      retained]
  C-40 branch specification:
    REVISED branch: `Vector status: REVISED` written in step b -> E-8.5 re-runs inline
      within step b -> new Contestation output -> E-4 `Contestation rule:` updated ->
      E-8.75 re-run -> re-seal. Terminal state: new Contestation derivation sealed.
    UNCHANGED branch: `Vector status: UNCHANGED` written in step b -> E-8.5 does NOT
      re-run -> `Contestation rule:` carried forward from prior Packet -> E-8.75 re-run
      -> re-seal. Terminal state: prior Contestation derivation retained.
    All terminal branches named. No inference required for either path.
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
    C-40 branch specification is structurally incomplete.
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
that produces it. Informal assessment of vector change is not consulted. Both terminal
branches (REVISED and UNCHANGED) are fully specified; neither path requires inference.

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
      updated Contestation analysis (if REVISED path ran E-8.5), updated C-35/C-37 records,
      updated C-38 compliance record with both sub-fields (Trigger + Evaluation outcome),
      and updated C-40 branch specification confirming which terminal branch executed.

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
   C-37: two-level verified. C-38: REVISED written in step b IS the firing (step-integration).
   C-40: both REVISED and UNCHANGED terminal branches fully specified in Packet.
   C-41: Evaluation outcome sealed in Packet (REVISED or UNCHANGED).]
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 records, C-40 branch specification)
| Conflict Register | Story beats 1-5

---

## Summary

| | Axis | Base | C-37 | C-38 | C-39 | C-40 | C-41 | Key addition |
|---|---|---|---|---|---|---|---|---|
| V-01 | C-41 outcome record | V-05 R16 | PASS | PASS | PARTIAL | PASS | Target PASS | Packet C-38 compliance gains Evaluation outcome sub-field; step f requires outcome population |
| V-02 | C-39 axiom grammar | V-05 R16 | PASS | PASS | Target PASS | PASS | PARTIAL | C-38 AXIOM rewritten as constitutive ("declaring REVISED IS the event"); step c restructured as REVISED/UNCHANGED terminal paths |
| V-03 | C-39 step-integration | V-05 R16 | PASS | PASS | Target PASS | PASS | PARTIAL | VECTOR-STATUS FIRING RULE replaces C-38 AXIOM; step b integrates E-8.5 inline when REVISED; no post-declaration read step |
| V-04 | C-39 axiom + C-41 | V-02 + V-01 | PASS | PASS | Target PASS | PASS | Target PASS | Constitutive axiom grammar (V-02) + Evaluation outcome sub-field in Packet (V-01) |
| V-05 | C-39 step-integration + C-41 + C-40 explicit | V-03 + V-01 | PASS | PASS | Target PASS | PASS | Target PASS | Step-integration (V-03) + outcome record (V-01) + explicit C-40 branch specification in Packet |

**C-39 architecture**: V-02 -- AXIOM grammar change, constitutive declaration, terminal
path restructuring in step c. V-03 -- VECTOR-STATUS FIRING RULE above steps, E-8.5
execution embedded within step b production, no downstream FORMAT BLOCK read. V-04 --
V-02 mechanism. V-05 -- V-03 mechanism. Critical distinction: V-02/V-04 grammar says
"declaring REVISED IS the event" but the step structure still shows a separate step c;
V-03/V-05 collapses the boundary entirely by making step b the execution step.

**C-41 architecture**: V-01, V-04, V-05 add "Evaluation outcome:" as a required sub-field
of the Packet's C-38 compliance record. The sub-field records whether C-38 was evaluated
and what the outcome was -- REVISED (E-8.5 re-ran) or UNCHANGED (carried forward). This
is the minimum addition that makes the sealed Packet self-auditing for C-38 compliance.
Without it (V-02, V-03), the Packet proves the trigger mechanism exists but not whether
the trigger fired in any specific re-sealing.

**C-40 architecture**: All five variations preserve explicit REVISED and UNCHANGED branch
naming in the re-sealing protocol, inheriting C-40 PASS from V-05 R16. V-05 additionally
seals a named C-40 branch specification in the Packet itself -- both terminal branches
declared with their full execution paths, confirming no inference is required for either.
