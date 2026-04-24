---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 20
rubric: v19
---

# Variations -- topic-story (Round 20, rubric v19)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v19 rubric adds C-48 (Beat 4 named resolution path taxonomy) and
updates C-46's pass condition. C-48 was sourced from V-05 R19's excellence signal — Beat 4
items tagged with `SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH`. The v19 pass condition
adds a new discriminator: *uniform tags across all items fail* — the taxonomy earns its
place only when it produces differentiated classifications.

V-05 R19 introduced the format field but not a differentiation enforcement rule. Against v19:
- V-04 R19: fails C-48 (no taxonomy instruction)
- V-05 R19: C-48 status uncertain — taxonomy format field present, no differentiation gate

C-46 updated pass condition note: V-04 R19's labels (`Pattern necessity test (apply before
finalizing this beat):`, `Completeness gate (apply before finalizing this beat):`) already
encode action + positional marker. The v19 discriminator targets `Sub-step (before
finalizing):` — category label, not action name. V-04 R19 labels are action-named, so C-46
is NOT at risk. R20 does not need to re-certify C-46.

**State entering R20 (against v19, ceiling 197.5):**

- V-04 R19: 195.0 (v18 ceiling). Against v19: C-48 FAIL. Score: 195.0.
- V-05 R19: 195.0 (v18 ceiling). Against v19: C-48 UNCERTAIN (no differentiation gate).
- R20 delta available: C-48 PASS = +2.5. R20 ceiling: 197.5.

**C-48 mechanism analysis:**

The taxonomy is `SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH`. Definitions:
- `SIGNAL_PATH`: closable by gathering more signal artifacts from an existing namespace
- `EXPERIMENT_PATH`: closable by running a targeted experiment that generates new evidence
  not derivable from existing signals
- `DECIDE_PATH`: requires a human/org decision; no amount of signal or experiment closes it

Failure condition: all items carry the same path type.
Pass condition: differentiated classifications — at least two distinct types across items.

The prompt must:
1. Define the three classes (or make them self-defining)
2. Require a `Resolution path:` field per item
3. Enforce differentiation explicitly — a model left free will often uniform-tag to SIGNAL_PATH

**R20 isolation design:**

| Variation | Axis | C-48 approach | C-48 | C-46 | C-47 | Register |
|-----------|------|---------------|------|------|------|----------|
| V-01 | Output format: minimal one-line differentiation rule | format field + "at least two distinct types" | TARGET PASS | PASS | PASS | formal |
| V-02 | Lifecycle: C-46-form differentiation audit sub-step | named audit label with action + position | TARGET PASS | PASS | PASS | formal |
| V-03 | Phrasing register: example-anchored definitions (conversational) | full definitions with examples, informal differentiation guidance | TARGET PASS | PASS | PASS | conversational |
| V-04 | Role sequence: EVALUATOR pre-classifies in E-5 | classification done in EVALUATOR, AUTHOR auto-transfers | TARGET PASS | PASS | PASS | formal |
| V-05 | Combination: all C-48 mechanisms + axiom grammar base | EVALUATOR pre-classifies + AUTHOR audit sub-step + definitions | TARGET PASS (strongest) | PASS | PASS | formal |

**Expected scores (v19, ceiling 197.5):**

| Variation | Expected | Key risk |
|-----------|----------|----------|
| V-01 | 197.5 | "at least two distinct types" may not prevent uniform tagging in practice |
| V-02 | 197.5 | audit sub-step may be skipped; action-name label may be insufficient alone |
| V-03 | 195.0 or 197.5 | conversational framing may produce the taxonomy but blur classification discipline |
| V-04 | 197.5 | EVALUATOR pre-classification eliminates AUTHOR discretion; cleanest separation |
| V-05 | 197.5 | fullest defense; combination may produce ceiling if all C-48 sub-mechanisms fire |

If V-03 scores 195.0: conversational register produces taxonomy but uniform tags; formal
definitions are load-bearing. If V-01 underscores V-02: the one-line differentiation rule
is insufficient; a named audit sub-step is required.

---

## V-01

**Variation axis**: Output format -- minimal differentiation rule appended to Beat 4
taxonomy instruction. Single axis.

**Hypothesis**: C-48 is achievable by adding a `Resolution path:` format field per item
plus a single explicit differentiation constraint: "At least two distinct path types must
appear across all items." The constraint is stated as a prose sentence, not as a named
sub-step label (C-46 form not used for this check). V-04 R19 base inherits C-46 and C-47.
Expected: C-48 PASS if the one-sentence constraint prevents uniform tagging. Score: 197.5.

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

`Resolution path:` REQUIRED FORMAT FIELD per item. At least two distinct path types must
appear across all items. Uniform tags (all items carrying the same type) indicate
undifferentiated classification and fail the taxonomy check.

Completeness gate (apply before finalizing this beat):
Count UNRESOLVED items in E-5. Verify Beat 4 item count matches. Every item has
`Resolution path:` filled. Beat 4 is not complete until count match and taxonomy fill
are both confirmed.

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
Record) | Conflict Register | Story beats 1-5 (Beat 4 with Resolution path tags)

---

## V-02

**Variation axis**: Lifecycle emphasis -- C-46-form named audit sub-step for taxonomy
differentiation. Single axis.

**Hypothesis**: C-48 differentiation is more reliably enforced by a named sub-step label
than by a prose constraint sentence. The label `Differentiation audit (apply before
finalizing this beat):` encodes both the action (audit) and the position (before
finalizing) in a single typographic unit -- the same C-46 structural pattern that
enforces necessity tests and proportionality audits. The definitions of the three path
types are embedded in the audit instruction body. Expected: C-48 PASS via named sub-step.
Score: 197.5.

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

Completeness gate (apply before finalizing this beat):
Count UNRESOLVED items in E-5. Verify Beat 4 item count matches. Every item has
`Resolution path:` filled. Beat 4 is not complete until count match and field fill
are both confirmed.

Differentiation audit (apply before finalizing this beat):
Verify the Resolution path tags are not uniform across all items. If every item carries
the same tag, revisit: SIGNAL_PATH means an existing namespace skill run would surface
the missing data; EXPERIMENT_PATH means a targeted test must generate new evidence not
already in the signal set; DECIDE_PATH means no investigation can substitute for a
human or team commitment. Genuinely distinct uncertainty items will rarely share a
single mechanism class. If all items remain SIGNAL_PATH after review, state explicitly
why EXPERIMENT_PATH and DECIDE_PATH do not apply.

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
Record) | Conflict Register | Story beats 1-5 (Beat 4 with Resolution path tags)

---

## V-03

**Variation axis**: Phrasing register -- example-anchored, conversational taxonomy
definitions. Single axis.

**Hypothesis**: The C-48 differentiation failure comes not from missing enforcement but
from abstract type definitions that are easy to conflate. If the three path types are
defined with concrete examples that are hard to confuse, the model will naturally produce
differentiated output without needing a formal differentiation gate. This tests whether
register (conversational + example-anchored) can do what enforcement instructions do.
C-46 and C-47 inherited from V-04 R19 base. Expected: 197.5 if examples drive
differentiation; 195.0 if conversational framing loses discipline.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### EVALUATOR Phase

[Identical to V-01 EVALUATOR Phase above -- E-1 through E-8, same rules and format fields]

---

### Mid-Draft Conflict Re-Sealing Protocol

[Identical to V-01 Mid-Draft Conflict Re-Sealing Protocol above]

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

**Beat 4**: For each UNRESOLVED conflict, write one sentence describing what remains open,
then tag it with the resolution path that fits.

Ask yourself: what would it actually take to close this? Three things are possible:

- **SIGNAL_PATH** -- you could close this by running more signal-gathering work in an
  existing namespace. Example: a scout:competitors run would surface whether a rival has
  already solved this. The answer exists somewhere and an existing skill can find it.
- **EXPERIMENT_PATH** -- this can only be closed by generating evidence that doesn't yet
  exist and can't be inferred from anything already gathered. Example: building a quick
  prototype to see if users actually respond the way the interviews predicted. No amount
  of reading or searching closes it; you have to make something and observe.
- **DECIDE_PATH** -- no research or experiment can close this. It takes a person or a team
  to make a call -- on priorities, resources, strategy, or values. Example: whether to
  target enterprise or consumer first is a strategic choice, not an empirical question.

Not all items will resolve to the same type. If you look at your uncertainty list and every
item maps to SIGNAL_PATH, pause: most real decision contexts have at least one thing that
requires a commitment rather than more evidence.

```
- {conflict-ID}: {finding, one sentence}
  Resolution path: SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH
```

Completeness gate (apply before finalizing this beat):
Verify UNRESOLVED count from E-5 matches Beat 4 item count. Every item tagged. Not all
items carry the same Resolution path type.

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
Record) | Conflict Register | Story beats 1-5 (Beat 4 with Resolution path tags)

---

## V-04

**Variation axis**: Role sequence -- EVALUATOR pre-classifies resolution paths in E-5,
AUTHOR auto-transfers. Combination: role sequence + output format.

**Hypothesis**: The differentiation failure in C-48 can be prevented at the EVALUATOR
phase rather than enforced at the AUTHOR phase. By adding a Resolution path column to
the E-5 Conflict Register, the EVALUATOR classifies each UNRESOLVED item before any
narrative writing begins. The AUTHOR's Beat 4 instruction becomes a pure transfer: copy
UNRESOLVED rows from E-5 including the pre-classified tags. Because the EVALUATOR works
analytically on the conflict register rather than in narrative flow, classification quality
is higher and uniform-tagging is more visible and correctable. Expected: 197.5.
Discriminator vs V-01/V-02: if V-04 scores higher, EVALUATOR-phase classification
produces better differentiation than AUTHOR-phase enforcement.

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
| ID | Artifact | Stance | Weight | Status | Adjudication | Because | Resolution path |
```

Status: RESOLVED | UNRESOLVED. Because: one sentence.

`Resolution path:` REQUIRED for UNRESOLVED rows only. Leave blank for RESOLVED rows.
Choose from: SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH.

- SIGNAL_PATH: an existing namespace skill run would surface the missing evidence.
- EXPERIMENT_PATH: new evidence must be generated; existing signals cannot close this.
- DECIDE_PATH: no signal or experiment closes this; a human or team decision is required.

**Path diversity check**: After classifying all UNRESOLVED rows, verify the tags are not
uniform. If all UNRESOLVED items carry the same tag, re-examine each: is the distinction
between investigation-closable and decision-required genuinely absent, or has the
classification collapsed due to insufficient attention to mechanism type?

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

**Beat 4**: UNRESOLVED conflicts. Auto-transfer only from E-5 UNRESOLVED rows.
Copy each UNRESOLVED row's finding and its pre-classified Resolution path tag.
No new items, no omissions, no tag changes.

```
- {conflict-ID}: {finding, one sentence}
  Resolution path: {SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH} [verbatim from E-5]
```

Completeness gate (apply before finalizing this beat):
Count UNRESOLVED rows in E-5. Verify Beat 4 item count matches. Every item has
`Resolution path:` transcribed verbatim from E-5. Beat 4 is not complete until both
transfer completeness and verbatim tag fidelity are confirmed.

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
Record) | Conflict Register | Story beats 1-5 (Beat 4 with Resolution path tags
auto-transferred from E-5)

---

## V-05

**Variation axis**: Combination -- EVALUATOR pre-classifies in E-5 (V-04 mechanism) +
AUTHOR named audit sub-step (V-02 mechanism) + axiom grammar base (V-05 R19 C-38 frame).
Full ceiling attempt.

**Hypothesis**: The strongest defense against C-48 uniform-tag failure combines three
mechanisms: (1) EVALUATOR-phase classification in E-5 with a path diversity check before
sealing, (2) AUTHOR-phase differentiation audit sub-step that verifies tags transferred
from E-5 are genuinely differentiated, and (3) the axiom grammar base for C-38 compliance
(constitutive framing). The three mechanisms address different failure modes: E-5
pre-classification catches uniform tags before narrative writing; the AUTHOR audit catches
any reclassification drift during narrative; the axiom grammar ensures C-38/C-39 remain
unaffected by the taxonomy addition. Expected: 197.5 with the strongest C-48 defense.

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
| ID | Artifact | Stance | Weight | Status | Adjudication | Because | Resolution path |
```

Status: RESOLVED | UNRESOLVED. Because: one sentence.

`Resolution path:` REQUIRED for UNRESOLVED rows only. Leave blank for RESOLVED rows.
Choose from: SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH.

- SIGNAL_PATH: an existing namespace skill run (scout, prove, listen, etc.) would surface
  the missing evidence; the data exists and can be gathered.
- EXPERIMENT_PATH: new evidence must be generated by a targeted experiment or prototype;
  existing signals cannot close this by further reading or searching.
- DECIDE_PATH: no signal or experiment closes this; requires a human or team commitment
  on priorities, resources, strategy, or values.

**Path diversity check (complete before sealing E-5)**: Verify UNRESOLVED rows carry at
least two distinct Resolution path types. If all items are SIGNAL_PATH: distinguish which
items could be closed by further gathering vs which require a new test vs which require
a commitment. Re-examine before proceeding. If genuine homogeneity exists, state why in
the Because column.

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

**Beat 4**: UNRESOLVED conflicts. Auto-transfer only from E-5 UNRESOLVED rows.
Copy each UNRESOLVED row's finding and its pre-classified Resolution path tag verbatim.
No new items, no omissions, no tag changes.

```
- {conflict-ID}: {finding, one sentence}
  Resolution path: {SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH} [verbatim from E-5]
```

Completeness gate (apply before finalizing this beat):
Count UNRESOLVED rows in E-5. Verify Beat 4 item count matches. Every item has
`Resolution path:` transcribed verbatim from E-5. Beat 4 is not complete until transfer
completeness and verbatim fidelity are both confirmed.

Differentiation audit (apply before finalizing this beat):
Verify the Resolution path tags across Beat 4 items are not uniform. If every item carries
the same tag, the E-5 path diversity check did not prevent homogeneous classification.
Return to E-5 and revise before proceeding. A Beat 4 where all items carry the same
Resolution path type fails C-48 regardless of tag fill completeness.

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
Record with AXIOM-constitutive causal chains) | Conflict Register | Story beats 1-5
(Beat 4 with Resolution path tags auto-transferred from E-5, differentiation verified)

---

## Summary

| | Axis | Base | C-48 mechanism | C-46 | C-47 | Key question |
|---|---|---|---|---|---|---|
| V-01 | Output format: minimal one-line constraint | V-04 R19 | format field + "at least two distinct types" sentence | PASS | PASS | Is a single prose differentiation sentence sufficient? |
| V-02 | Lifecycle: C-46-form differentiation audit sub-step | V-04 R19 | named sub-step label + definitions in body | PASS | PASS | Does a C-46-form label for C-48 out-perform a prose constraint? |
| V-03 | Phrasing register: example-anchored conversational definitions | V-04 R19 | inline example definitions + "not all items same" note | PASS | PASS | Can example-anchored register drive differentiation without a formal gate? |
| V-04 | Role sequence: EVALUATOR pre-classifies in E-5 | V-04 R19 | E-5 column + path diversity check in EVALUATOR | PASS | PASS | Does EVALUATOR-phase classification prevent AUTHOR-phase uniform tagging? |
| V-05 | Combination: E-5 pre-classify + AUTHOR audit sub-step + axiom grammar | V-05 R19 | E-5 diversity check + AUTHOR differentiation audit + axiom C-38 | PASS | PASS | Does stacking all C-48 mechanisms on the axiom base reach ceiling? |

**Discriminator predictions:**

If V-01 < V-04: EVALUATOR-phase classification is load-bearing; AUTHOR-phase prose constraint is insufficient.
If V-02 > V-01: C-46-form named sub-step label produces better differentiation than prose.
If V-03 < V-01: Register (conversational + examples) is not sufficient; formal gate is required.
If V-05 = V-04: The combination adds no value over EVALUATOR-only pre-classification.
If V-05 > V-04: Both EVALUATOR diversity check and AUTHOR audit sub-step contribute independently to C-48 pass.
