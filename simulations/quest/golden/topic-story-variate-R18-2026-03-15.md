---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 18
rubric: v17
---

# Variations -- topic-story (Round 18)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v17 rubric adds C-42 (Sealed Branch Architecture Record) and C-43
(Trigger-Action Step Co-Location). Both are extracted from R17 mechanisms.

From Round 17 scoring against v16 (ceiling 185.0):

- V-05 R17: 185.0 (ceiling) -- step-integration C-39 PASS, C-40 explicit branch spec in
  Packet, C-41 PASS. Against v17: C-42 PASS (C-40 branch spec field in Packet covers
  derivation chains) and C-43 PASS (step-integration, no interval). Projected: 190.0.
- V-04 R17: 185.0 (ceiling via axiom grammar) -- C-38 AXIOM constitutive, C-41 PASS,
  C-40 PASS (step-level naming in protocol). Against v17: C-42 FAIL (no branch spec in
  Packet), C-43 PARTIAL (axiom grammar, step c still carries re-derivation -- interval
  exists). Projected: 186.25.
- V-03 R17: step-integration, C-41 PARTIAL. Against v17: C-43 PASS, C-42 FAIL (no sealed
  branch record in Packet). Projected: 187.50.

**C-42 gap**: V-04 R17 and V-03 R17 name branch paths in protocol text but the sealed
Packet has no standalone record specifying both terminal paths with full derivation chains.
An auditor reading only the Packet cannot reconstruct what REVISED and UNCHANGED do
without returning to the protocol. C-42 closes this by sealing a named "Branch
Architecture Record" in the Packet that is causally self-documenting.

**C-43 gap**: V-04 R17 C-38 AXIOM declares "REVISED IS the re-derivation event" (C-39
PASS) but step c carries the actual E-8.5 re-run -- a logical interval exists: REVISED
is written in step b, and E-8.5 has not run until step c executes. Step-integration
(V-05 R17) eliminates this by making E-8.5 run within step b before step b completes.
Axiom grammar satisfies C-39 but not C-43 unless step b's completion condition is
extended to include E-8.5.

**Round 18 isolation design:**

| Variation | Base | C-42 | C-43 | Axis |
|-----------|------|------|------|------|
| V-01 | V-04 R17 | Target PASS | PARTIAL | C-42 only: Branch Architecture Record in Packet |
| V-02 | V-04 R17 | FAIL | Target PASS | C-43 only: axiom grammar + step-completion |
| V-03 | V-05 R17 | Target PASS | PASS | C-42 vocab: rename C-40 field, expand chains |
| V-04 | V-01 + V-02 | Target PASS | Target PASS | Axiom grammar + C-42 + C-43 combined |
| V-05 | V-03 base | Target PASS | Target PASS | Step-integration + explicit no-interval + C-42 |

**Expected scores (v17, total max 190.0):**

V-04 R17 against v17: 185.0 + C-43 PARTIAL +1.25 + C-42 FAIL +0 = 186.25

| Variation | Expected | Remaining gap |
|-----------|----------|---------------|
| V-01 | 188.75 | C-43 PARTIAL |
| V-02 | 187.50 | C-42 FAIL |
| V-03 | 190.0 | none |
| V-04 | 190.0 | none (if axiom grammar C-43 step-completion passes) |
| V-05 | 190.0 | none |

If V-04 scores 190.0, axiom grammar + step-completion is confirmed as a C-43 PASS
mechanism and R19 has two independent ceiling paths. If V-04 scores 188.75, C-43 via
axiom grammar is insufficient and step-integration remains the only confirmed C-43 PASS
mechanism.

---

## V-01

**Variation axis**: C-42 minimal addition to V-04 R17. Single axis.

**Hypothesis**: C-42 is independent of the C-43 mechanism. V-04 R17 has C-39 PASS
(axiom grammar), C-40 PASS, C-41 PASS, but no branch architecture record in the sealed
Packet. Adding a named "Branch Architecture Record:" field to E-8 that specifies both
terminal paths with their full derivation chains should achieve C-42 PASS. Step c remains
separate (C-43 PARTIAL). Expected: C-42 PASS, C-43 PARTIAL. Score: 188.75.

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
  Branch Architecture Record:
    REVISED branch: `Vector status: REVISED` written in step b -> C-38 AXIOM fires;
      declaring REVISED IS the re-derivation event (constitutive) -> E-8.5 re-runs in
      step c -> new Contestation output produced -> E-4 `Contestation rule:` updated ->
      E-8.75 re-runs (mandatory) -> re-seal with new Contestation data. Terminal state:
      new Contestation derivation sealed; Evaluation outcome: REVISED. Causal chain:
      declaration -> E-8.5 (step c) -> E-4 update -> E-8.75 -> re-seal.
    UNCHANGED branch: `Vector status: UNCHANGED` written in step b -> UNCHANGED terminal
      outcome constituted by the declaration; E-8.5 does NOT re-run -> `Contestation
      rule:` carried forward verbatim from prior sealed Packet -> E-8.75 re-runs
      (mandatory) -> re-seal with prior Contestation data retained. Terminal state:
      prior Contestation derivation retained; Evaluation outcome: UNCHANGED. Causal
      chain: declaration -> no E-8.5 -> prior output retained -> E-8.75 -> re-seal.
    Both terminal branches fully specified. Auditor can reconstruct either path from
    this Packet without returning to the protocol.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 compliance record (Trigger + Evaluation outcome) is
    incomplete. Packet without Branch Architecture Record (C-42) omits sealed derivation
    chains; auditor cannot reconstruct terminal paths.
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
the FORMAT BLOCK after it is written. The declaration is constitutive and authoritative.

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
      updated Contestation analysis (if REVISED path ran E-8.5), updated C-35/C-37
      records, updated C-38 compliance record with both sub-fields (Trigger + Evaluation
      outcome), and updated Branch Architecture Record confirming which terminal branch
      executed and its derivation chain.

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
   C-37: two-level verified. C-38: declaring REVISED IS the firing (constitutive, C-39).
   C-41: Evaluation outcome sealed. C-42: Branch Architecture Record in Packet with
   derivation chains for both terminal paths.]
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 compliance, Branch Architecture
Record) | Conflict Register | Story beats 1-5

---

## V-02

**Variation axis**: C-43 via axiom grammar -- step-completion reframing. Single axis.

**Hypothesis**: The C-43 gap in V-04 R17 is that step c carries E-8.5 re-derivation,
creating an interval where REVISED is written in step b but E-8.5 has not run. Extending
step b's completion condition to require E-8.5 to finish for the REVISED branch eliminates
this interval while keeping the constitutive axiom (C-39 PASS). No Branch Architecture
Record (C-42 FAIL), isolating the C-43 axis. Expected: C-42 FAIL, C-43 PASS. Score: 187.50.

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
      FORMAT BLOCK IS the Contestation rule re-derivation event and initiates the REVISED
      completion sequence for step b. Step b is not complete until, for the REVISED branch,
      E-8.5 has run within step b and produced PASS. Declaring REVISED and step b
      completing are inseparable -- there is no state where REVISED is declared and step b
      is complete but E-8.5 has not run. Declaring `Vector status: UNCHANGED` IS the
      UNCHANGED terminal outcome; step b completes immediately; E-8.5 does not run.
      No step reads the FORMAT BLOCK post-declaration. The declaration is constitutive.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed within step b;
      E-8.5 ran and completed before step b finished; new Contestation output sealed] |
      [UNCHANGED -- Contestation rule carried forward; no E-8.5 re-run; prior output
      retained]
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 compliance record (Trigger + Evaluation outcome) is
    incomplete. Packet C-38 Trigger missing step-completion language fails C-43. Packet
    lacks Branch Architecture Record -- auditor cannot reconstruct terminal paths without
    returning to protocol.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

**C-38 AXIOM**: Declaring `Vector status: REVISED` in step b IS the Contestation rule
re-derivation event and initiates the REVISED completion sequence: E-8.5 must run within
step b and produce PASS before step b is complete. There is no state where `Vector status:
REVISED` is declared in the FORMAT BLOCK and step b is complete but E-8.5 has not run.
Writing `Vector status: UNCHANGED` constitutes the UNCHANGED terminal outcome: step b
completes immediately upon FORMAT BLOCK production; `Contestation rule:` is carried
forward; E-8.5 does not run. No step after step b reads the FORMAT BLOCK to determine
which path executed. The declaration is constitutive and authoritative.

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

      REVISED completion sequence (step b not done until this finishes):
        Run E-8.5 now, within this step. Inline assertions must HOLD.
        Update E-4 `Contestation rule:` from new Contestation output.
        Step b is complete when E-8.5 produces PASS and E-4 is updated.

      UNCHANGED completion sequence (step b done when FORMAT BLOCK is written):
        Do not run E-8.5. `Contestation rule:` carried forward. Proceed to step c.

   c. E-5, E-6, E-7 updates.

   d. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   e. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if REVISED completion sequence ran E-8.5), updated
      C-35/C-37 records, and updated C-38 compliance record with both sub-fields
      (Trigger -- including step-completion language -- and Evaluation outcome).

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
   C-37: two-level verified. C-38: declaring REVISED IS the event (constitutive, C-39)
   AND requires E-8.5 within step b before step b completes (step-completion, C-43).
   C-41: Evaluation outcome sealed.]
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 compliance) | Conflict Register |
Story beats 1-5

---

## V-03

**Variation axis**: C-42 explicit vocabulary -- V-05 R17 base with renamed and expanded
Branch Architecture Record. Single axis.

**Hypothesis**: V-05 R17's "C-40 branch specification:" Packet field already contains
both terminal paths and their derivation chains, satisfying C-42 by substance. Renaming
it "Branch Architecture Record:" (matching C-42's causal self-documentation framing) and
expanding the derivation chain language to name each causal step explicitly confirms C-42
PASS. C-43 PASS is inherited from V-05 R17 step-integration. Tests whether vocabulary
alignment has independent scoring impact. Expected: C-42 PASS, C-43 PASS. Score: 190.0.

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
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 compliance, Branch Architecture
Record) | Conflict Register | Story beats 1-5

---

## V-04

**Variation axis**: C-42 + C-43 via axiom grammar. Combination of V-01 and V-02.

**Hypothesis**: V-01 adds C-42 (Branch Architecture Record) to V-04 R17; V-02 adds C-43
(step-completion) to V-04 R17. C-42 and C-43 are orthogonal: combining them on the axiom
grammar base should achieve both simultaneously. If V-04 scores 190.0, axiom grammar +
step-completion is confirmed as a C-43 PASS mechanism and R19 has two independent ceiling
paths. Expected: C-42 PASS, C-43 PASS. Score: 190.0.

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
      FORMAT BLOCK IS the Contestation rule re-derivation event and initiates the REVISED
      completion sequence for step b. Step b is not complete until, for the REVISED branch,
      E-8.5 has run within step b and produced PASS. There is no state where REVISED is
      declared and step b is complete but E-8.5 has not run. Declaring `Vector status:
      UNCHANGED` IS the UNCHANGED terminal outcome; step b completes immediately; E-8.5
      does not run. No step reads the FORMAT BLOCK post-declaration. The declaration is
      constitutive and authoritative.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed; E-8.5 ran
      within step b and completed before step b was done; new Contestation output sealed] |
      [UNCHANGED -- Contestation rule carried forward; no E-8.5 re-run; prior output
      retained]
  Branch Architecture Record:
    REVISED branch: `Vector status: REVISED` written in step b -> C-38 AXIOM fires
      (constitutive declaration IS the event) AND initiates REVISED completion sequence
      -> E-8.5 runs within step b before step b is complete -> new Contestation output
      produced -> E-4 `Contestation rule:` updated -> step b completes (E-8.5 PASS
      required) -> E-8.75 re-runs (mandatory) -> re-seal with new Contestation data.
      Terminal state: new Contestation derivation sealed. Causal chain: declaration ->
      E-8.5 within step b -> E-4 update -> step b done -> E-8.75 -> re-seal.
    UNCHANGED branch: `Vector status: UNCHANGED` written in step b -> C-38 AXIOM
      constitutes UNCHANGED terminal outcome -> E-8.5 does NOT run -> `Contestation
      rule:` carried forward verbatim from prior sealed Packet -> step b complete
      immediately -> E-8.75 re-runs (mandatory) -> re-seal with prior Contestation data
      retained. Terminal state: prior Contestation derivation retained. Causal chain:
      declaration -> no E-8.5 -> prior output retained -> step b done -> E-8.75 ->
      re-seal.
    Both terminal branches fully specified with derivation chains. Auditor can reconstruct
    either path from this Packet without returning to the protocol.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 compliance record (Trigger + Evaluation outcome) is
    incomplete. Packet C-38 Trigger missing step-completion language fails C-43. Packet
    without Branch Architecture Record (C-42) omits sealed derivation chains.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

**C-38 AXIOM**: Declaring `Vector status: REVISED` in step b IS the Contestation rule
re-derivation event and initiates the REVISED completion sequence: E-8.5 must run within
step b and produce PASS before step b is complete. There is no state where `Vector status:
REVISED` is declared and step b is complete but E-8.5 has not run -- the REVISED
completion sequence and step b's completion boundary are the same boundary. Writing
`Vector status: UNCHANGED` constitutes the UNCHANGED terminal outcome: step b completes
upon FORMAT BLOCK production; `Contestation rule:` is carried forward; E-8.5 does not
run. No step after step b reads the FORMAT BLOCK. The declaration is constitutive and
authoritative.

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

      REVISED completion sequence (step b not done until this finishes):
        Run E-8.5 now, within this step. Inline assertions must HOLD.
        Update E-4 `Contestation rule:` from new Contestation output.
        Step b is complete when E-8.5 produces PASS and E-4 is updated.

      UNCHANGED completion sequence (step b done when FORMAT BLOCK is written):
        Do not run E-8.5. `Contestation rule:` carried forward. Proceed to step c.

   c. E-5, E-6, E-7 updates.

   d. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   e. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if REVISED completion sequence ran E-8.5), updated
      C-35/C-37 records, updated C-38 compliance record with both sub-fields (Trigger
      including step-completion language + Evaluation outcome), and updated Branch
      Architecture Record confirming which terminal branch executed with derivation chain.

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
   C-37: two-level verified. C-38: declaring REVISED IS the firing (constitutive, C-39)
   and requires E-8.5 within step b before step b completes (step-completion, C-43).
   C-41: Evaluation outcome sealed. C-42: Branch Architecture Record in Packet.]
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 compliance, Branch Architecture
Record) | Conflict Register | Story beats 1-5

---

## V-05

**Variation axis**: Step-integration + explicit no-interval guarantee + expanded Branch
Architecture Record. Combination building on V-03.

**Hypothesis**: V-03 achieves C-42 and C-43 by carrying V-05 R17 mechanisms with
renamed/expanded vocabulary. V-05 adds an explicit "no interval" statement in two
locations: the FIRING RULE ("There is no state where `Vector status: REVISED` is written
and E-8.5 has not executed within step b") and the Branch Architecture Record's REVISED
branch derivation chain. If V-03 and V-05 both score 190.0, explicit no-interval language
provides no scoring differential and V-03's vocabulary is canonical. If V-05 outscores
V-03, the explicit no-interval formulation is required for full C-43 credit and becomes
the R19 base. Expected: C-42 PASS, C-43 PASS. Score: 190.0.

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
      both occur in step b as a single integrated operation (step-integration). There is
      no state where `Vector status: REVISED` is written and E-8.5 has not executed
      within step b. Writing `Vector status: UNCHANGED` IS the UNCHANGED terminal outcome.
      No step after step b reads the FORMAT BLOCK. The written value determines execution
      immediately within step b.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed within step b;
      E-8.5 re-run complete before step b finished; new Contestation output sealed] |
      [UNCHANGED -- Contestation rule carried forward; E-8.5 did not run; no partial
      execution state; prior Contestation output retained]
  Branch Architecture Record:
    REVISED branch: `Vector status: REVISED` written in step b -> VECTOR-STATUS FIRING
      RULE executes; the written value IS the branch determination (constitutive) ->
      E-8.5 runs immediately as an integrated sub-operation within step b; there is no
      state between REVISED written and E-8.5 completed within step b -> new Contestation
      output produced -> E-4 `Contestation rule:` updated -> step b completes (E-8.5
      PASS is the completion condition) -> E-8.75 re-runs (mandatory) -> re-seal with
      new Contestation data. Terminal state: new Contestation derivation sealed; prior
      output superseded. Causal chain: declaration constitutes E-8.5 trigger -> E-8.5
      within step b (no interval between REVISED written and E-8.5 complete) -> E-4
      update -> step b done -> E-8.75 -> re-seal.
    UNCHANGED branch: `Vector status: UNCHANGED` written in step b -> VECTOR-STATUS
      FIRING RULE constitutes UNCHANGED terminal outcome -> E-8.5 does NOT run; there
      is no partial execution state for the UNCHANGED branch; the absence of E-8.5 is
      a defined property of this path -> `Contestation rule:` carried forward verbatim
      from prior sealed Packet -> step b completes immediately on FORMAT BLOCK production
      -> E-8.75 re-runs (mandatory) -> re-seal with prior Contestation data retained.
      Terminal state: prior Contestation derivation retained. Causal chain: declaration
      constitutes UNCHANGED terminal outcome -> no E-8.5 (by design, not omission) ->
      prior output retained -> step b done -> E-8.75 -> re-seal.
    Both terminal branches fully specified with derivation chains and explicit no-interval
    guarantees. Neither path has an unspecified intermediate state. Auditor can reconstruct
    either path from this Packet without protocol access.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Beat 5 framing, AUTHOR prose, and
    recommendation preference are prohibited inputs to retroactive revision.
  C-36 INDEPENDENCE: `Rule applied:` and `Contestation rule:` are EVALUATOR-phase outputs
    sealed here. AUTHOR reads verbatim. Audit: copy `Rule applied:` from Packet; verify
    Beat 4.5 Licensing matches. Copy `Contestation rule:`; verify Beat 4.5 field matches.
  VALIDITY NOTICE: Packet without C-37 two-level verification was sealed with unverified
    consistency. Packet without C-38 compliance record (Trigger + Evaluation outcome) is
    incomplete. Packet C-38 Trigger missing "no interval" statement fails C-43. Packet
    without Branch Architecture Record (C-42) omits sealed derivation chains. Packet
    Branch Architecture Record missing no-interval statements for both branches is
    incomplete for C-42 causal self-documentation.
]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

**VECTOR-STATUS FIRING RULE** (named above numbered steps): The `Vector status:` value
written in the Re-sealing Reconciliation Decision FORMAT BLOCK in step b is the execution
branch point. Writing `Vector status: REVISED` in step b IS the firing of E-8.5 -- E-8.5
runs immediately as part of step b, before step b is complete. There is no state where
`Vector status: REVISED` is written and E-8.5 has not executed within step b. Writing
`Vector status: UNCHANGED` in step b IS the UNCHANGED terminal outcome -- `Contestation
rule:` is carried forward and E-8.5 does not run; there is no partial execution state for
the UNCHANGED path. No step after step b reads the FORMAT BLOCK. The written value
determines execution immediately, within the step that produces it. Both terminal branches
(REVISED and UNCHANGED) are fully specified with no-interval guarantees.

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

      REVISED path (execute now, within this step; there is no state between REVISED
      written and E-8.5 complete):
        Re-run E-8.5 immediately. Inline assertions must HOLD.
        Update E-4 `Contestation rule:` from new Contestation output.
        Step b is not complete until E-8.5 produces PASS and E-4 is updated.

      UNCHANGED path (step b complete when FORMAT BLOCK is written; E-8.5 does not run;
      no partial execution):
        `Contestation rule:` is carried forward unchanged. Proceed to step c.

   c. E-5, E-6, E-7 updates.

   d. Re-run E-8.75. MANDATORY for every re-sealing regardless of Vector status.
      Combined must be PASS before proceeding.

   e. E-8 re-seal: new Packet supersedes old. Must include updated `Rule applied:`,
      updated Contestation analysis (if REVISED path ran E-8.5), updated C-35/C-37
      records, updated C-38 compliance record with both sub-fields (Trigger must include
      "no interval" statement + Evaluation outcome), and updated Branch Architecture
      Record confirming which terminal branch executed with derivation chain and
      no-interval statement.

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
   C-37: two-level verified. C-38: REVISED written in step b IS the firing; no state
   between REVISED written and E-8.5 complete (step-integration, C-43 PASS, no-interval
   explicit). C-41: Evaluation outcome sealed. C-42: Branch Architecture Record in Packet
   with full derivation chains and no-interval guarantees for both branches.]
Conditions: {finding or threshold whose change would let Adjacent verb win}
```

**Beat 5**: Stance matching Packet Selected stance and Band gate. One sentence: reversal
condition.

---

### Output artifact

Write to: `simulations/{topic}/{topic}-story-{date}.md`

Structure: Derivation Packet (with C-35, C-37, C-38 compliance including no-interval,
Branch Architecture Record with no-interval guarantees) | Conflict Register | Story
beats 1-5

---

## Summary

| | Axis | Base | C-39 | C-40 | C-41 | C-42 | C-43 | Key addition |
|---|---|---|---|---|---|---|---|---|
| V-01 | C-42 minimal | V-04 R17 | PASS | PASS | PASS | Target PASS | PARTIAL | Branch Architecture Record in Packet; both paths with chains; step c remains separate |
| V-02 | C-43 step-completion | V-04 R17 | PASS | PASS | PASS | FAIL | Target PASS | AXIOM: declaring REVISED requires E-8.5 in step b; step b not done until E-8.5 passes |
| V-03 | C-42 vocab | V-05 R17 | PASS | PASS | PASS | Target PASS | PASS | Rename C-40 field to Branch Architecture Record; explicit causal chains per branch |
| V-04 | C-42 + C-43 axiom | V-01 + V-02 | PASS | PASS | PASS | Target PASS | Target PASS | Constitutive AXIOM + step-completion (C-43) + Branch Architecture Record (C-42) |
| V-05 | C-42 + C-43 no-interval | V-03 + stronger | PASS | PASS | PASS | Target PASS | Target PASS | FIRING RULE + step b + Packet all have explicit "no interval" language |

**C-42 architecture**: All four targeting variations (V-01/V-03/V-04/V-05) add a named
"Branch Architecture Record" to the sealed Packet. The record specifies both terminal
paths (REVISED and UNCHANGED) with full derivation chains. This is the minimum addition
that makes the Packet causally self-documenting per the C-42 criterion. The distinction
from C-40: C-40 PASS is achievable by step-level branch naming in protocol text; C-42
requires the same information sealed in the Packet as a named record.

**C-43 architecture**: V-02 and V-04 achieve C-43 via step-completion reframing on the
axiom grammar base: the AXIOM is amended so that declaring REVISED requires E-8.5 to
complete within step b before step b is done. V-03 and V-05 achieve C-43 via step-
integration (VECTOR-STATUS FIRING RULE, inherited from V-05 R17). Critical test: if
V-04 scores 190.0, axiom grammar + step-completion is a confirmed C-43 PASS path.

**Scoring leverage**: V-01 vs V-02 isolates C-42 vs C-43 on the same axiom base.
V-03 vs V-05 isolates whether explicit "no interval" language adds scoring value beyond
V-05 R17's implicit step-integration guarantee. V-04 vs V-03 tests whether axiom grammar
matches step-integration when both C-42 and C-43 are combined.
