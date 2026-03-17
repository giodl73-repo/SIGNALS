---

```yaml
---
skill: quest-variate
skill_target: prove-topic
round: R5
date: 2026-03-16
rubric: prove-topic-rubric-v5-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single:
    - C-21: CAMPAIGN OPEN INCUMBENT ANCHOR sub-section with Do-not-re-establish prohibition
    - C-22: Invariant D binding resolution note with literal-string canonical failure label
    - C-23: Stage 5 evidence_summary cites artifact Displacement read by value
  combined:
    - V-04: C-21 + C-22 (registration layer complete)
    - V-05: C-21 + C-22 + C-23 (all three new criteria on full R4 gold base)
r4_best: V-05 (86 on v3 rubric; V-04 scored 81)
round_targets: >
  v5 adds C-21/C-22/C-23 from R4 excellence signals.
  C-21: INCUMBENT ANCHOR sub-section + explicit "Do not re-establish" prohibition.
        V-02 in R4 showed: naming the sub-section and adding prohibition text prevents
        per-stage drift. Extends C-15 (block exists) -- C-21 checks it is locked.
  C-22: Invariant D carries binding resolution note + canonical failure label for
        literal-string use. Templates bind to [incumbent from CAMPAIGN OPEN], not literal.
        Naming as literal string = FORMAT ERROR registered and echoed.
  C-23: Stage 5 evidence_summary cites at least one artifact Displacement read field
        by value. Closes the chain: C-16 (stage declares read) -> C-20 (artifact carries
        read) -> C-23 (Stage 5 consumes artifact read value, not just stage verdict).
  All R5 variations carry R4 gold: C-14 (two-layer enforcement), C-15 (CAMPAIGN OPEN),
  C-16 (per-stage Displacement read), C-17 (SYNTHESIS DECLARATIONS prohibition),
  C-18 (Invariant E checkpoint), C-19 (template binding to CAMPAIGN OPEN where axis
  applies), C-20 (artifact Displacement read field where axis applies).
---
```

---

## V-01 -- Axis: CAMPAIGN OPEN INCUMBENT ANCHOR With Prohibition (C-21)

**Variation axis**: C-21 only -- the INCUMBENT ANCHOR sub-section gains an explicit
named header and carries the "Do not re-establish the incumbent per stage. Carry forward
from CAMPAIGN OPEN." prohibition. No other changes from R4 V-01 gold base.

**Hypothesis**: The named sub-section header promotes the incumbent registration from a
fill-in block to a structural anchor. The explicit prohibition sentence makes downstream
re-establishment self-violating -- any stage that re-names the incumbent is detectable
as a C-21 violation from two directions (absent from sub-section authority + re-establishment
present inline), mirroring the C-17 mechanism for SYNTHESIS DECLARATIONS.

---

```
You are running the prove-topic Signal skill.

Topic: {topic}
Date:  {date}

The campaign builds the case for displacing the status quo with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has
numbered ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until all
entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS -- FAILURE LABEL REGISTRY

Standalone block. Appears before Stage 0. All invariants active for full campaign.
Cannot be modified or bypassed at any subsequent stage.

  ID | NAME                        | DECLARATION                              | FAILURE LABEL
  ---|-----------------------------|------------------------------------------|---------------------
  D  | INCUMBENT CHECK PHRASING    | Stage 2: "Does [evidence item] support   | FORMAT ERROR
     | REGISTER                    |   the displacement of                    |
     |                             |   {status_quo_comparator} by {topic}     |
     |                             |   on [dimension]? [Yes/No/Inconclusive]" |
     |                             | Stage 3: "Does [practitioner account]    |
     |                             |   reveal a viable transition path from   |
     |                             |   {status_quo_comparator} to {topic}     |
     |                             |   for [use case]? [Yes/No/Inconclusive]" |
     |                             | Stage 4: "Does [prototype result] make   |
     |                             |   a credible case for displacing         |
     |                             |   {status_quo_comparator} with {topic}?  |
     |                             |   [Yes/No/Pending]"                      |
     |                             | Template deviation = FORMAT ERROR.       |
  ---|-----------------------------|------------------------------------------|---------------------
  A  | ADVERSARIAL REVIEWER TYPE   | adversarial_reviewer_type: [role most    | DUAL-LOCK ERROR
     |                             |   likely to challenge displacement].     |
     |                             | Activation: null_tally_final >= 3.       |
  ---|-----------------------------|------------------------------------------|---------------------
  B  | CONFIDENCE CAP              | confidence_composite -= 2 if             | DUAL-LOCK ERROR
     |                             |   null_tally_final >= 3 (hard cap).      |
     |                             | Cannot be softened.                      |
  ---|-----------------------------|------------------------------------------|---------------------
  C  | DERIVATION ANNOTATION       | Every handoff field: [derived from: X].  | FORMAT ERROR
     |                             | Unlabeled field = FORMAT ERROR.          |
  ---|-----------------------------|------------------------------------------|---------------------
  E  | HANDOFF SCHEMA COMPLIANCE   | All 11 handoff fields present, each with | Invariant E
     |                             |   [derived from: X] annotation.          | checkpoint -- FAIL
     |                             | schema_compliance_confirmed row echoes   |
     |                             |   this label verbatim at Stage 5.        |
     |                             | Missing or unlabeled field =             |
     |                             |   Invariant E checkpoint -- FAIL.        |
  ---|-----------------------------|------------------------------------------|---------------------
  F  | SYNTHESIS FIELD ISOLATION   | hypothesis_verdict, confidence_composite,| SYNTHESIS
     |                             |   key_risk: each on its own line.        | FORMAT ERROR
     |                             | Do not embed in prose. Each extractable  |
     |                             |   by label match.                        |

Inline enforcement: Every stage checkpoint echoes the exact FAILURE LABEL from this registry.
Drift between registered label and inline echo = self-incriminating failure.

### ROLE OWNERSHIP TABLE

Roles execute in sequence C -> B -> A before Stage 0.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP
  -------|--------------------------|------------------------------|-------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked      | Step 1
  ROLE B | SCOUT LOADER             | gate_s_cleared               | Step 2
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [glob simulations/scout/{topic}-scout-*.md -- exact path or ABSENT]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded = true; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all six SESSION INVARIANT rows (D, A, B, C, E, F) filled and active.
  Confirms Invariant E canonical label "Invariant E checkpoint -- FAIL" registered.
  adversarial_reviewer_type: [role name -- registered now, carried to ATOMIC DUAL-LOCK]
  invariant_registry_confirmed: [true when all six rows registered]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Stage 5 reconstructs S2->S3->S4 chain independently
and declares Stage 5 chain confirmation. Mismatch = INTEGRITY FAILURE.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE
  ---------------------------|-------------------------------------------
  scout_anchor               | ROLE B scout load
  incumbent_threat_locked    | ROLE C analysis
  hypothesis                 | Stage 1 artifact
  counter_hypothesis         | Stage 1 artifact
  s2_ce_verdict              | Stage 2 artifact
  s3_ce_verdict              | Stage 3 artifact
  s4_ce_verdict              | Stage 4 artifact
  null_tally_final           | s2+s3+s4 CE verdicts (not through co_activation)
  co_activation_confirmed    | ATOMIC DUAL-LOCK (not through incumbent_defense)
  incumbent_defense_closed   | s2+s3+s4 direct chain (not through co_activation)
  confidence_composite       | Stage 5 synthesis (capped by Invariant B if triggered)

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS block complete -- all six rows (D, A, B, C, E, F) registered
  [ ] Invariant E canonical label confirmed: "Invariant E checkpoint -- FAIL"
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- adversarial_reviewer_type registered; invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|-------------------------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role. Label: ORDER ERROR.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANTS D/A/B/C/E/F
   active. Invariant E checkpoint -- FAIL registered. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered (confirmed by ROLE A at Step 3)

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic} displacing incumbent]
  counter_hypothesis:           [incumbent best defense -- grounded in INCUMBENT ANCHOR]
  gate_s_cleared:               [true -- from GATE S Step 2]
  invariant_registry_confirmed: [true -- from GATE S Step 3]
  incumbent_threat_locked:      [true -- from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from registry row D):
      "Does [evidence item] support the displacement of {status_quo_comparator} by
       {topic} on [dimension]? [Yes / No / Inconclusive]"
      Invariant D checkpoint -- FORMAT ERROR if template deviated.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D template verbatim):
Structural origin: ROLE C incumbent_threat_locked (confirmed GATE S Step 1).

  ITEM | SOURCE       | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------|----------------------|----------------------------
  1    | [source]     | [summary]            | "Does [item 1] support the
  2    | [source]     | [summary]            |  displacement of [comparator]
  3    | [source]     | [summary]            |  by [topic] on [dim]?
  ...  |              |                      |  [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if any row omits template or uses non-verbatim wording.

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  Displacement read: [one sentence: does Stage 2 evidence support, challenge, or leave
                      inconclusive the case for displacing {status_quo_comparator}?]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim from registry row D):
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
      Invariant D checkpoint -- FORMAT ERROR if template deviated.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D template verbatim):

  PRACTITIONER | KEY ACCOUNT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -------------|--------------------------|----------------------------
  [type 1]     | [quote or paraphrase]    | "Does [account 1] reveal a
  [type 2]     | [quote or paraphrase]    |  viable transition path from
  [type 3]     | [quote or paraphrase]    |  [comparator] to [topic]
                                          |  for [use case]?
                                          |  [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if any row omits template or uses non-verbatim wording.

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  Displacement read: [one sentence: does Stage 3 evidence support, challenge, or leave
                      inconclusive the transition from {status_quo_comparator}?]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim from registry row D):
      "Does [prototype result] make a credible case for displacing {status_quo_comparator}
       with {topic}? [Yes / No / Pending]"
      Invariant D checkpoint -- FORMAT ERROR if template deviated or verdict omitted.

STAGE 4 BODY:

  prototype_design: [brief description]
  prototype_result: [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D template verbatim):

  ITEM      | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  ----------|-------------------------------|----------------------------
  prototype | [prototype_result]            | "Does [prototype result] make
                                            |  a credible case for displacing
                                            |  [comparator] with [topic]?
                                            |  [Yes/No/Pending]"

  Invariant D checkpoint -- FORMAT ERROR if template omitted or verdict missing.

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]
  Displacement read: [one sentence: does the prototype make a credible case for displacing
                      {status_quo_comparator}? Cite s4_displacement_verdict.]

Final null tally:
  null_tally_final = [N]
  Stage 4 cross-check: "Running count from Stage 3 was [M]. Final is [N].
  Match: [true / false]." Mismatch = INTEGRITY FAILURE.

SCHEMA INTEGRITY: [N]/11 handoff fields populated.
Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict = [value]. null_tally_final = [N].
   Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All six SESSION INVARIANT rows (D, A, B, C, E, F) active

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS | VERDICT                                 | EVIDENCE
  -------------------|-----------------------------------------|-------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK applies.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction (INTEGRITY FAILURE if chain total does not match Stage 4):
  S2 -> s2_ce_verdict: [null | value -- from Stage 2 artifact]
  S3 -> s3_ce_verdict: [null | value -- from Stage 3 artifact]
  S4 -> s4_ce_verdict: [null | value -- from Stage 4 artifact]
  Reconstructed null count: [N]
  Stage 4 declared null_tally_final: [M]
  Stage 5 chain confirmation: "S2=[s2_val] + S3=[s3_val] + S4=[s4_val] = [N] null.
    Stage 4 declared [M]. Match: [true / false]."
  Mismatch = INTEGRITY FAILURE. Record before continuing.

DUAL-LOCK EVALUATION:
  null_tally_final = [N]
  If null_tally_final >= 3:
    Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
    Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
    co_activation_confirmed: dual_lock_fired
  Else:
    co_activation_confirmed: not_triggered

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.
Invariant F checkpoint -- SYNTHESIS FORMAT ERROR if any field appears only within prose.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  confidence_composite:  [final numeric value after all reductions]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### SYNTHESIS BODY

  evidence_summary: [2-3 sentences integrating Stages 2, 3, 4. Must cite Stage 4
                     displacement verdict explicitly: "Stage 4 displacement verdict: [Y/N/P]."]

### HANDOFF TABLE

SESSION INVARIANT C enforced: all fields carry [derived from: X]. Unlabeled = FORMAT ERROR.
SESSION INVARIANT E enforced: all 11 fields present.
Invariant E checkpoint -- FAIL if any field unlabeled or missing.

  FIELD                      | VALUE   | DERIVATION
  ---------------------------|---------|----------------------------------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]
  hypothesis                 | [value] | [derived from: Stage 1 artifact]
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]
  schema_compliance_confirmed| [true]  | [Invariant E checkpoint -- FAIL if unlabeled/missing]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-02 -- Axis: Invariant D Binding Resolution Note With Literal-String Failure Label (C-22)

**Variation axis**: C-22 only -- Invariant D in SESSION INVARIANTS is upgraded in two ways:
(1) templates use `[incumbent from CAMPAIGN OPEN]` instead of the literal comparator name,
and (2) a binding resolution note is added: "Binding: [incumbent from CAMPAIGN OPEN] resolves
to incumbent_name from CAMPAIGN OPEN INCUMBENT ANCHOR. Naming as literal string = FORMAT ERROR."
No other changes from R4 V-01 base. INCUMBENT ANCHOR section has no "Do not re-establish"
prohibition (that is C-21's single axis).

**Hypothesis**: The binding resolution note closes the loop that C-19 opens. C-19 checks
that the template uses the bound reference; C-22 checks that the binding mechanism itself
has a registered canonical failure label. When the literal-string failure label is in the
SESSION INVARIANTS registry, any stage that hard-codes the incumbent name diverges from the
registry AND from the inline echo simultaneously -- both structural directions detect the
violation without requiring a human reviewer to notice the drift.

---

```
You are running the prove-topic Signal skill.

Topic: {topic}
Date:  {date}

The campaign builds the case for displacing the status quo with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has
numbered ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until all
entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS -- FAILURE LABEL REGISTRY

Standalone block. Appears before Stage 0. All invariants active for full campaign.
Cannot be modified or bypassed at any subsequent stage.

  ID | NAME                        | DECLARATION                              | FAILURE LABEL
  ---|-----------------------------|------------------------------------------|---------------------
  D  | INCUMBENT CHECK PHRASING    | Stage 2: "Does [evidence item] support   | FORMAT ERROR
     | REGISTER                    |   the displacement of                    |
     |                             |   [incumbent from CAMPAIGN OPEN]         |
     |                             |   by {topic} on [dimension]?             |
     |                             |   [Yes/No/Inconclusive]"                 |
     |                             | Stage 3: "Does [practitioner account]    |
     |                             |   reveal a viable transition path from   |
     |                             |   [incumbent from CAMPAIGN OPEN]         |
     |                             |   to {topic} for [use case]?             |
     |                             |   [Yes/No/Inconclusive]"                 |
     |                             | Stage 4: "Does [prototype result] make   |
     |                             |   a credible case for displacing         |
     |                             |   [incumbent from CAMPAIGN OPEN]         |
     |                             |   with {topic}? [Yes/No/Pending]"        |
     |                             | Binding: [incumbent from CAMPAIGN OPEN]  |
     |                             |   resolves to incumbent_name from        |
     |                             |   CAMPAIGN OPEN INCUMBENT ANCHOR.        |
     |                             | Naming as literal string = FORMAT ERROR. |
     |                             | Template deviation = FORMAT ERROR.       |
  ---|-----------------------------|------------------------------------------|---------------------
  A  | ADVERSARIAL REVIEWER TYPE   | adversarial_reviewer_type: [role most    | DUAL-LOCK ERROR
     |                             |   likely to challenge displacement].     |
     |                             | Activation: null_tally_final >= 3.       |
  ---|-----------------------------|------------------------------------------|---------------------
  B  | CONFIDENCE CAP              | confidence_composite -= 2 if             | DUAL-LOCK ERROR
     |                             |   null_tally_final >= 3 (hard cap).      |
     |                             | Cannot be softened.                      |
  ---|-----------------------------|------------------------------------------|---------------------
  C  | DERIVATION ANNOTATION       | Every handoff field: [derived from: X].  | FORMAT ERROR
     |                             | Unlabeled field = FORMAT ERROR.          |
  ---|-----------------------------|------------------------------------------|---------------------
  E  | HANDOFF SCHEMA COMPLIANCE   | All 11 handoff fields present, each with | Invariant E
     |                             |   [derived from: X] annotation.          | checkpoint -- FAIL
     |                             | schema_compliance_confirmed row echoes   |
     |                             |   this label verbatim at Stage 5.        |
     |                             | Missing or unlabeled field =             |
     |                             |   Invariant E checkpoint -- FAIL.        |
  ---|-----------------------------|------------------------------------------|---------------------
  F  | SYNTHESIS FIELD ISOLATION   | hypothesis_verdict, confidence_composite,| SYNTHESIS
     |                             |   key_risk: each on its own line.        | FORMAT ERROR
     |                             | Do not embed in prose. Each extractable  |
     |                             |   by label match.                        |

Inline enforcement: Every stage checkpoint echoes the exact FAILURE LABEL from this registry.
Drift between registered label and inline echo = self-incriminating failure.

### ROLE OWNERSHIP TABLE

Roles execute in sequence C -> B -> A before Stage 0.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP
  -------|--------------------------|------------------------------|-------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked      | Step 1
  ROLE B | SCOUT LOADER             | gate_s_cleared               | Step 2
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [glob simulations/scout/{topic}-scout-*.md -- exact path or ABSENT]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded = true; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all six SESSION INVARIANT rows (D, A, B, C, E, F) filled and active.
  Confirms Invariant D binding: "[incumbent from CAMPAIGN OPEN] resolves to incumbent_name."
  Confirms Invariant D canonical failure label for literal-string use registered.
  Confirms Invariant E "Invariant E checkpoint -- FAIL" canonical label registered.
  adversarial_reviewer_type: [role name -- registered now, carried to ATOMIC DUAL-LOCK]
  invariant_registry_confirmed: [true when all six rows registered with canonical labels]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Stage 5 reconstructs S2->S3->S4 chain independently
and declares Stage 5 chain confirmation. Mismatch = INTEGRITY FAILURE.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE
  ---------------------------|-------------------------------------------
  scout_anchor               | ROLE B scout load
  incumbent_threat_locked    | ROLE C analysis
  hypothesis                 | Stage 1 artifact
  counter_hypothesis         | Stage 1 artifact
  s2_ce_verdict              | Stage 2 artifact
  s3_ce_verdict              | Stage 3 artifact
  s4_ce_verdict              | Stage 4 artifact
  null_tally_final           | s2+s3+s4 CE verdicts (not through co_activation)
  co_activation_confirmed    | ATOMIC DUAL-LOCK (not through incumbent_defense)
  incumbent_defense_closed   | s2+s3+s4 direct chain (not through co_activation)
  confidence_composite       | Stage 5 synthesis (capped by Invariant B if triggered)

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS block complete -- all six rows (D, A, B, C, E, F) registered
  [ ] Invariant D binding resolution note confirmed: "Naming as literal string = FORMAT ERROR"
  [ ] Invariant E canonical label confirmed: "Invariant E checkpoint -- FAIL"
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- binding + labels confirmed; invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|-------------------------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role. Label: ORDER ERROR.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 confirmed. Invariant D binding registered.
   Naming as literal string = FORMAT ERROR active. Invariant E checkpoint -- FAIL active.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates with [incumbent from CAMPAIGN OPEN] binding active

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic} displacing incumbent]
  counter_hypothesis:           [incumbent best defense -- grounded in INCUMBENT ANCHOR]
  gate_s_cleared:               [true -- from GATE S Step 2]
  invariant_registry_confirmed: [true -- from GATE S Step 3]
  incumbent_threat_locked:      [true -- from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from registry -- uses binding):
      "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN]
       by {topic} on [dimension]? [Yes / No / Inconclusive]"
      Binding resolves to: incumbent_name from CAMPAIGN OPEN INCUMBENT ANCHOR.
      Naming as literal string = FORMAT ERROR. Template deviation = FORMAT ERROR.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D template verbatim):
Binding: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name. Do not substitute literal.

  ITEM | SOURCE       | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------|----------------------|----------------------------
  1    | [source]     | [summary]            | "Does [item 1] support the
  2    | [source]     | [summary]            |  displacement of [incumbent
  3    | [source]     | [summary]            |  from CAMPAIGN OPEN] by
  ...  |              |                      |  [topic] on [dim]?
                                             |  [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if any row uses literal name or non-verbatim wording.
  Naming as literal string = FORMAT ERROR. Echoes registry label verbatim.

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  Displacement read: [one sentence: does Stage 2 evidence support, challenge, or leave
                      inconclusive the case for displacing [incumbent from CAMPAIGN OPEN]?]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim -- uses binding):
      "Does [practitioner account] reveal a viable transition path from
       [incumbent from CAMPAIGN OPEN] to {topic} for [use case]? [Yes / No / Inconclusive]"
      Binding resolves to: incumbent_name from CAMPAIGN OPEN INCUMBENT ANCHOR.
      Naming as literal string = FORMAT ERROR. Template deviation = FORMAT ERROR.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D template verbatim):
Binding: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name. Do not substitute literal.

  PRACTITIONER | KEY ACCOUNT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -------------|--------------------------|----------------------------
  [type 1]     | [quote or paraphrase]    | "Does [account 1] reveal a viable
  [type 2]     | [quote or paraphrase]    |  transition path from [incumbent
  [type 3]     | [quote or paraphrase]    |  from CAMPAIGN OPEN] to [topic]
                                          |  for [use case]? [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if any row uses literal name or non-verbatim wording.
  Naming as literal string = FORMAT ERROR.

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  Displacement read: [one sentence: does Stage 3 evidence support or challenge displacement
                      of [incumbent from CAMPAIGN OPEN]?]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim -- uses binding):
      "Does [prototype result] make a credible case for displacing
       [incumbent from CAMPAIGN OPEN] with {topic}? [Yes / No / Pending]"
      Binding resolves to: incumbent_name from CAMPAIGN OPEN INCUMBENT ANCHOR.
      Naming as literal string = FORMAT ERROR. Template deviation = FORMAT ERROR.

STAGE 4 BODY:

  prototype_design: [brief description]
  prototype_result: [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D template verbatim):
Binding: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name. Do not substitute literal.

  ITEM      | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  ----------|-------------------------------|----------------------------
  prototype | [prototype_result]            | "Does [prototype result] make
                                            |  a credible case for displacing
                                            |  [incumbent from CAMPAIGN OPEN]
                                            |  with [topic]? [Yes/No/Pending]"

  Invariant D checkpoint -- FORMAT ERROR if template omitted, literal used, or verdict missing.
  Naming as literal string = FORMAT ERROR.

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]
  Displacement read: [one sentence: does the prototype make a credible case for displacing
                      [incumbent from CAMPAIGN OPEN]? Cite s4_displacement_verdict.]

Final null tally:
  null_tally_final = [N]
  Stage 4 cross-check: "Running count from Stage 3 was [M]. Final is [N].
  Match: [true / false]." Mismatch = INTEGRITY FAILURE.

SCHEMA INTEGRITY: [N]/11 handoff fields populated.
Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict = [value]. null_tally_final = [N].
   Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All six SESSION INVARIANT rows (D, A, B, C, E, F) active

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS | VERDICT                                 | EVIDENCE
  -------------------|-----------------------------------------|-------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK applies.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction (INTEGRITY FAILURE if chain total does not match Stage 4):
  S2 -> s2_ce_verdict: [null | value -- from Stage 2 artifact]
  S3 -> s3_ce_verdict: [null | value -- from Stage 3 artifact]
  S4 -> s4_ce_verdict: [null | value -- from Stage 4 artifact]
  Reconstructed null count: [N]
  Stage 4 declared null_tally_final: [M]
  Stage 5 chain confirmation: "S2=[s2_val] + S3=[s3_val] + S4=[s4_val] = [N] null.
    Stage 4 declared [M]. Match: [true / false]."
  Mismatch = INTEGRITY FAILURE. Record before continuing.

DUAL-LOCK EVALUATION:
  null_tally_final = [N]
  If null_tally_final >= 3:
    Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
    Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
    co_activation_confirmed: dual_lock_fired
  Else:
    co_activation_confirmed: not_triggered

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.
Invariant F checkpoint -- SYNTHESIS FORMAT ERROR if any field appears only within prose.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  confidence_composite:  [final numeric value after all reductions]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### SYNTHESIS BODY

  evidence_summary: [2-3 sentences integrating Stages 2, 3, 4. Must cite Stage 4
                     displacement verdict explicitly: "Stage 4 displacement verdict: [Y/N/P]."]

### HANDOFF TABLE

SESSION INVARIANT C enforced: all fields carry [derived from: X]. Unlabeled = FORMAT ERROR.
SESSION INVARIANT E enforced: all 11 fields present.
Invariant E checkpoint -- FAIL if any field unlabeled or missing.

  FIELD                      | VALUE   | DERIVATION
  ---------------------------|---------|----------------------------------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]
  hypothesis                 | [value] | [derived from: Stage 1 artifact]
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]
  schema_compliance_confirmed| [true]  | [Invariant E checkpoint -- FAIL if unlabeled/missing]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-03 -- Axis: Stage 5 Cites Artifact Displacement Read by Value (C-23)

**Variation axis**: C-23 only -- Stage 2, 3, and 4 write confirmations explicitly describe
"Displacement read: [value]" as a required field in the artifact file body (not just stage
output). Stage 5 SYNTHESIS BODY requires citing at least one artifact Displacement read field
by value in evidence_summary. No other changes from R4 V-01 base. INCUMBENT ANCHOR has no
prohibition; Invariant D uses literal comparator name.

**Hypothesis**: Mandating that artifact files carry the Displacement read field and that Stage 5
consumes it by value closes the portability chain. If Stage 5 only reads stage output, the
Displacement read exists in session memory but not in the written artifact -- it is not portable
to downstream skills. By requiring the Stage 5 evidence_summary to cite the artifact field value
directly ("websearch Displacement read: [value]"), the chain becomes: stage output declares it
(C-16) -> artifact carries it (C-20) -> Stage 5 cites the artifact value (C-23). All three links
must fire for the chain to be intact.

---

```
You are running the prove-topic Signal skill.

Topic: {topic}
Date:  {date}

The campaign builds the case for displacing the status quo with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has
numbered ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until all
entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS -- FAILURE LABEL REGISTRY

Standalone block. Appears before Stage 0. All invariants active for full campaign.
Cannot be modified or bypassed at any subsequent stage.

  ID | NAME                        | DECLARATION                              | FAILURE LABEL
  ---|-----------------------------|------------------------------------------|---------------------
  D  | INCUMBENT CHECK PHRASING    | Stage 2: "Does [evidence item] support   | FORMAT ERROR
     | REGISTER                    |   the displacement of                    |
     |                             |   {status_quo_comparator} by {topic}     |
     |                             |   on [dimension]? [Yes/No/Inconclusive]" |
     |                             | Stage 3: "Does [practitioner account]    |
     |                             |   reveal a viable transition path from   |
     |                             |   {status_quo_comparator} to {topic}     |
     |                             |   for [use case]? [Yes/No/Inconclusive]" |
     |                             | Stage 4: "Does [prototype result] make   |
     |                             |   a credible case for displacing         |
     |                             |   {status_quo_comparator} with {topic}?  |
     |                             |   [Yes/No/Pending]"                      |
     |                             | Template deviation = FORMAT ERROR.       |
  ---|-----------------------------|------------------------------------------|---------------------
  A  | ADVERSARIAL REVIEWER TYPE   | adversarial_reviewer_type: [role most    | DUAL-LOCK ERROR
     |                             |   likely to challenge displacement].     |
     |                             | Activation: null_tally_final >= 3.       |
  ---|-----------------------------|------------------------------------------|---------------------
  B  | CONFIDENCE CAP              | confidence_composite -= 2 if             | DUAL-LOCK ERROR
     |                             |   null_tally_final >= 3 (hard cap).      |
     |                             | Cannot be softened.                      |
  ---|-----------------------------|------------------------------------------|---------------------
  C  | DERIVATION ANNOTATION       | Every handoff field: [derived from: X].  | FORMAT ERROR
     |                             | Unlabeled field = FORMAT ERROR.          |
  ---|-----------------------------|------------------------------------------|---------------------
  E  | HANDOFF SCHEMA COMPLIANCE   | All 11 handoff fields present, each with | Invariant E
     |                             |   [derived from: X] annotation.          | checkpoint -- FAIL
     |                             | schema_compliance_confirmed row echoes   |
     |                             |   this label verbatim at Stage 5.        |
     |                             | Missing or unlabeled field =             |
     |                             |   Invariant E checkpoint -- FAIL.        |
  ---|-----------------------------|------------------------------------------|---------------------
  F  | SYNTHESIS FIELD ISOLATION   | hypothesis_verdict, confidence_composite,| SYNTHESIS
     |                             |   key_risk: each on its own line.        | FORMAT ERROR
     |                             | Do not embed in prose. Each extractable  |
     |                             |   by label match.                        |
  ---|-----------------------------|------------------------------------------|---------------------
  G  | ARTIFACT DISPLACEMENT READ  | Stages 2, 3, 4 artifact files must carry | PORTABILITY ERROR
     |                             |   "Displacement read: [value]" as a      |
     |                             |   labeled field in artifact body.        |
     |                             | Stage 5 evidence_summary must cite at    |
     |                             |   least one artifact Displacement read   |
     |                             |   by value: e.g.,                        |
     |                             |   "websearch Displacement read: [value]" |
     |                             | Absent from artifact body = PORTABILITY  |
     |                             |   ERROR. Stage 5 citing stage output     |
     |                             |   only without artifact citation = FAIL. |

Inline enforcement: Every stage checkpoint echoes the exact FAILURE LABEL from this registry.
Drift between registered label and inline echo = self-incriminating failure.

### ROLE OWNERSHIP TABLE

Roles execute in sequence C -> B -> A before Stage 0.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP
  -------|--------------------------|------------------------------|-------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked      | Step 1
  ROLE B | SCOUT LOADER             | gate_s_cleared               | Step 2
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [glob simulations/scout/{topic}-scout-*.md -- exact path or ABSENT]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded = true; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all seven SESSION INVARIANT rows (D, A, B, C, E, F, G) filled and active.
  Confirms Invariant E "Invariant E checkpoint -- FAIL" canonical label registered.
  Confirms Invariant G "PORTABILITY ERROR" canonical label registered.
  adversarial_reviewer_type: [role name -- registered now, carried to ATOMIC DUAL-LOCK]
  invariant_registry_confirmed: [true when all seven rows registered]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Stage 5 reconstructs S2->S3->S4 chain independently
and declares Stage 5 chain confirmation. Mismatch = INTEGRITY FAILURE.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE
  ---------------------------|-------------------------------------------
  scout_anchor               | ROLE B scout load
  incumbent_threat_locked    | ROLE C analysis
  hypothesis                 | Stage 1 artifact
  counter_hypothesis         | Stage 1 artifact
  s2_ce_verdict              | Stage 2 artifact
  s3_ce_verdict              | Stage 3 artifact
  s4_ce_verdict              | Stage 4 artifact
  null_tally_final           | s2+s3+s4 CE verdicts (not through co_activation)
  co_activation_confirmed    | ATOMIC DUAL-LOCK (not through incumbent_defense)
  incumbent_defense_closed   | s2+s3+s4 direct chain (not through co_activation)
  confidence_composite       | Stage 5 synthesis (capped by Invariant B if triggered)

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS block complete -- all seven rows (D, A, B, C, E, F, G) registered
  [ ] Invariant E canonical label confirmed: "Invariant E checkpoint -- FAIL"
  [ ] Invariant G canonical label confirmed: "PORTABILITY ERROR"
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- adversarial_reviewer_type registered; invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|-------------------------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role. Label: ORDER ERROR.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANTS D/A/B/C/E/F/G
   active. Invariant E checkpoint -- FAIL registered. PORTABILITY ERROR registered.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered (confirmed by ROLE A at Step 3)

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic} displacing incumbent]
  counter_hypothesis:           [incumbent best defense -- grounded in INCUMBENT ANCHOR]
  gate_s_cleared:               [true -- from GATE S Step 2]
  invariant_registry_confirmed: [true -- from GATE S Step 3]
  incumbent_threat_locked:      [true -- from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from registry row D):
      "Does [evidence item] support the displacement of {status_quo_comparator} by
       {topic} on [dimension]? [Yes / No / Inconclusive]"
      Invariant D checkpoint -- FORMAT ERROR if template deviated.
  [ ] SESSION INVARIANT G active: artifact must carry "Displacement read: [value]" in body.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D template verbatim):

  ITEM | SOURCE       | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------|----------------------|----------------------------
  1    | [source]     | [summary]            | "Does [item 1] support the
  2    | [source]     | [summary]            |  displacement of [comparator]
  3    | [source]     | [summary]            |  by [topic] on [dim]?
  ...  |              |                      |  [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if any row omits template or uses non-verbatim wording.

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  Displacement read: [one sentence: does Stage 2 evidence support, challenge, or leave
                      inconclusive the case for displacing {status_quo_comparator}?]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-websearch-{date}.md
Artifact body must include as a labeled field:
  Displacement read: [value from Stage 2 Displacement read above]
Invariant G checkpoint -- PORTABILITY ERROR if "Displacement read:" absent from artifact body.
Confirm write with: "{topic}-websearch-{date}.md written. Displacement read: [value] included."

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N].
   Artifact Displacement read: [value] confirmed in file. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] Stage 2 artifact Displacement read confirmed in file
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim from registry row D):
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
      Invariant D checkpoint -- FORMAT ERROR if template deviated.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D template verbatim):

  PRACTITIONER | KEY ACCOUNT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -------------|--------------------------|----------------------------
  [type 1]     | [quote or paraphrase]    | "Does [account 1] reveal a viable
  [type 2]     | [quote or paraphrase]    |  transition path from [comparator]
  [type 3]     | [quote or paraphrase]    |  to [topic] for [use case]?
                                          |  [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if any row omits template or uses non-verbatim wording.

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  Displacement read: [one sentence: does Stage 3 evidence support or challenge displacement?]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-interview-{date}.md
Artifact body must include as a labeled field:
  Displacement read: [value from Stage 3 Displacement read above]
Invariant G checkpoint -- PORTABILITY ERROR if "Displacement read:" absent from artifact body.
Confirm write with: "{topic}-interview-{date}.md written. Displacement read: [value] included."

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N].
   Artifact Displacement read: [value] confirmed in file. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] Stage 3 artifact Displacement read confirmed in file
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim from registry row D):
      "Does [prototype result] make a credible case for displacing {status_quo_comparator}
       with {topic}? [Yes / No / Pending]"
      Invariant D checkpoint -- FORMAT ERROR if template deviated or verdict omitted.

STAGE 4 BODY:

  prototype_design: [brief description]
  prototype_result: [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D template verbatim):

  ITEM      | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  ----------|-------------------------------|----------------------------
  prototype | [prototype_result]            | "Does [prototype result] make
                                            |  a credible case for displacing
                                            |  [comparator] with [topic]?
                                            |  [Yes/No/Pending]"

  Invariant D checkpoint -- FORMAT ERROR if template omitted or verdict missing.

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]
  Displacement read: [one sentence: does prototype make a credible case for displacing
                      {status_quo_comparator}? Cite s4_displacement_verdict.]

Final null tally:
  null_tally_final = [N]
  Stage 4 cross-check: "Running count from Stage 3 was [M]. Final is [N].
  Match: [true / false]." Mismatch = INTEGRITY FAILURE.

SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-prototype-{date}.md
Artifact body must include as a labeled field:
  Displacement read: [value from Stage 4 Displacement read above]
Invariant G checkpoint -- PORTABILITY ERROR if "Displacement read:" absent from artifact body.
Confirm write with: "{topic}-prototype-{date}.md written. Displacement read: [value] included."

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict = [value]. null_tally_final = [N].
   Artifact Displacement read: [value] confirmed in file. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] All three artifact Displacement read values confirmed in file bodies
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All seven SESSION INVARIANT rows active

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS | VERDICT                                 | EVIDENCE
  -------------------|-----------------------------------------|-------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK applies.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction (INTEGRITY FAILURE if chain total does not match Stage 4):
  S2 -> s2_ce_verdict: [null | value -- from Stage 2 artifact]
  S3 -> s3_ce_verdict: [null | value -- from Stage 3 artifact]
  S4 -> s4_ce_verdict: [null | value -- from Stage 4 artifact]
  Reconstructed null count: [N]
  Stage 4 declared null_tally_final: [M]
  Stage 5 chain confirmation: "S2=[s2_val] + S3=[s3_val] + S4=[s4_val] = [N] null.
    Stage 4 declared [M]. Match: [true / false]."
  Mismatch = INTEGRITY FAILURE. Record before continuing.

DUAL-LOCK EVALUATION:
  null_tally_final = [N]
  If null_tally_final >= 3:
    Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
    Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
    co_activation_confirmed: dual_lock_fired
  Else:
    co_activation_confirmed: not_triggered

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.
Invariant F checkpoint -- SYNTHESIS FORMAT ERROR if any field appears only within prose.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  confidence_composite:  [final numeric value after all reductions]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### SYNTHESIS BODY

  evidence_summary: [2-3 sentences integrating Stages 2, 3, 4. Must include:
    (1) Citation of Stage 4 displacement verdict: "Stage 4 displacement verdict: [Y/N/P]."
    (2) At least one artifact Displacement read citation by value, e.g.:
        "websearch Displacement read: [value from {topic}-websearch-{date}.md artifact]"
        "interview Displacement read: [value from {topic}-interview-{date}.md artifact]"
        "prototype Displacement read: [value from {topic}-prototype-{date}.md artifact]"
    Citing stage output Displacement read only, without citing artifact file value = FAIL.
    Invariant G checkpoint -- PORTABILITY ERROR if no artifact Displacement read cited.]

### HANDOFF TABLE

SESSION INVARIANT C enforced: all fields carry [derived from: X]. Unlabeled = FORMAT ERROR.
SESSION INVARIANT E enforced: all 11 fields present.
Invariant E checkpoint -- FAIL if any field unlabeled or missing.

  FIELD                      | VALUE   | DERIVATION
  ---------------------------|---------|----------------------------------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]
  hypothesis                 | [value] | [derived from: Stage 1 artifact]
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]
  schema_compliance_confirmed| [true]  | [Invariant E checkpoint -- FAIL if unlabeled/missing]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-04 -- Combined: C-21 + C-22 (Registration Layer Complete)

**Variation axes**: INCUMBENT ANCHOR prohibition (C-21) combined with Invariant D binding
resolution note and literal-string failure label (C-22). Together these two criteria complete
the "registration layer": the CAMPAIGN OPEN anchor is prohibited from per-stage re-establishment,
and the Invariant D template explicitly names the failure mode for violating that prohibition.
C-21 seals the anchor; C-22 makes the seal auditable through the two-layer enforcement
architecture. No C-23 (artifact Displacement read portability is a single axis for V-03).

**Hypothesis**: The anchor prohibition (C-21) and the binding failure label (C-22) are
structurally interdependent: the prohibition has no mechanical teeth unless there is a
registered failure label that activates when the rule is broken. V-04 tests whether combining
both halves of the enforcement pair produces a qualitatively stronger gate than either half
alone -- analogous to how C-17 (prohibition text) + C-13 (field isolation) together are
stronger than either criterion satisfies independently.

---

```
You are running the prove-topic Signal skill.

Topic: {topic}
Date:  {date}

The campaign builds the case for displacing the status quo with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has
numbered ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until all
entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS -- FAILURE LABEL REGISTRY

Standalone block. Appears before Stage 0. All invariants active for full campaign.
Cannot be modified or bypassed at any subsequent stage.

  ID | NAME                        | DECLARATION                              | FAILURE LABEL
  ---|-----------------------------|------------------------------------------|---------------------
  D  | INCUMBENT CHECK PHRASING    | Stage 2: "Does [evidence item] support   | FORMAT ERROR
     | REGISTER                    |   the displacement of                    |
     |                             |   [incumbent from CAMPAIGN OPEN]         |
     |                             |   by {topic} on [dimension]?             |
     |                             |   [Yes/No/Inconclusive]"                 |
     |                             | Stage 3: "Does [practitioner account]    |
     |                             |   reveal a viable transition path from   |
     |                             |   [incumbent from CAMPAIGN OPEN]         |
     |                             |   to {topic} for [use case]?             |
     |                             |   [Yes/No/Inconclusive]"                 |
     |                             | Stage 4: "Does [prototype result] make   |
     |                             |   a credible case for displacing         |
     |                             |   [incumbent from CAMPAIGN OPEN]         |
     |                             |   with {topic}? [Yes/No/Pending]"        |
     |                             | Binding: [incumbent from CAMPAIGN OPEN]  |
     |                             |   resolves to incumbent_name from        |
     |                             |   CAMPAIGN OPEN INCUMBENT ANCHOR.        |
     |                             | Naming as literal string = FORMAT ERROR. |
     |                             | Template deviation = FORMAT ERROR.       |
  ---|-----------------------------|------------------------------------------|---------------------
  A  | ADVERSARIAL REVIEWER TYPE   | adversarial_reviewer_type: [role most    | DUAL-LOCK ERROR
     |                             |   likely to challenge displacement].     |
     |                             | Activation: null_tally_final >= 3.       |
  ---|-----------------------------|------------------------------------------|---------------------
  B  | CONFIDENCE CAP              | confidence_composite -= 2 if             | DUAL-LOCK ERROR
     |                             |   null_tally_final >= 3 (hard cap).      |
     |                             | Cannot be softened.                      |
  ---|-----------------------------|------------------------------------------|---------------------
  C  | DERIVATION ANNOTATION       | Every handoff field: [derived from: X].  | FORMAT ERROR
     |                             | Unlabeled field = FORMAT ERROR.          |
  ---|-----------------------------|------------------------------------------|---------------------
  E  | HANDOFF SCHEMA COMPLIANCE   | All 11 handoff fields present, each with | Invariant E
     |                             |   [derived from: X] annotation.          | checkpoint -- FAIL
     |                             | schema_compliance_confirmed row echoes   |
     |                             |   this label verbatim at Stage 5.        |
     |                             | Missing or unlabeled field =             |
     |                             |   Invariant E checkpoint -- FAIL.        |
  ---|-----------------------------|------------------------------------------|---------------------
  F  | SYNTHESIS FIELD ISOLATION   | hypothesis_verdict, confidence_composite,| SYNTHESIS
     |                             |   key_risk: each on its own line.        | FORMAT ERROR
     |                             | Do not embed in prose. Each extractable  |
     |                             |   by label match.                        |

Inline enforcement: Every stage checkpoint echoes the exact FAILURE LABEL from this registry.
Drift between registered label and inline echo = self-incriminating failure.

### ROLE OWNERSHIP TABLE

Roles execute in sequence C -> B -> A before Stage 0.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP
  -------|--------------------------|------------------------------|-------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked      | Step 1
  ROLE B | SCOUT LOADER             | gate_s_cleared               | Step 2
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [glob simulations/scout/{topic}-scout-*.md -- exact path or ABSENT]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded = true; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all six SESSION INVARIANT rows (D, A, B, C, E, F) filled and active.
  Confirms Invariant D: "[incumbent from CAMPAIGN OPEN] resolves to incumbent_name."
  Confirms Invariant D canonical failure label for literal-string use registered.
  Confirms Invariant E "Invariant E checkpoint -- FAIL" canonical label registered.
  adversarial_reviewer_type: [role name -- registered now, carried to ATOMIC DUAL-LOCK]
  invariant_registry_confirmed: [true when all rows registered with canonical labels]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Stage 5 reconstructs S2->S3->S4 chain independently
and declares Stage 5 chain confirmation. Mismatch = INTEGRITY FAILURE.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE
  ---------------------------|-------------------------------------------
  scout_anchor               | ROLE B scout load
  incumbent_threat_locked    | ROLE C analysis
  hypothesis                 | Stage 1 artifact
  counter_hypothesis         | Stage 1 artifact
  s2_ce_verdict              | Stage 2 artifact
  s3_ce_verdict              | Stage 3 artifact
  s4_ce_verdict              | Stage 4 artifact
  null_tally_final           | s2+s3+s4 CE verdicts (not through co_activation)
  co_activation_confirmed    | ATOMIC DUAL-LOCK (not through incumbent_defense)
  incumbent_defense_closed   | s2+s3+s4 direct chain (not through co_activation)
  confidence_composite       | Stage 5 synthesis (capped by Invariant B if triggered)

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] "Do not re-establish" prohibition confirmed in INCUMBENT ANCHOR section
  [ ] SESSION INVARIANTS block complete -- all six rows (D, A, B, C, E, F) registered
  [ ] Invariant D binding resolution note confirmed: "[incumbent from CAMPAIGN OPEN]
      resolves to incumbent_name. Naming as literal string = FORMAT ERROR."
  [ ] Invariant E canonical label confirmed: "Invariant E checkpoint -- FAIL"
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- binding + labels confirmed; invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|-------------------------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role. Label: ORDER ERROR.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 confirmed. INCUMBENT ANCHOR locked with
   'Do not re-establish' prohibition. Invariant D binding active: [incumbent from CAMPAIGN OPEN]
   resolves to incumbent_name. Naming as literal string = FORMAT ERROR active.
   Invariant E checkpoint -- FAIL registered. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates with [incumbent from CAMPAIGN OPEN] binding active

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.
The incumbent reference for all displacement checks is INCUMBENT ANCHOR incumbent_name.
Do not re-establish the incumbent inline. All Invariant D templates carry binding reference.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic} displacing incumbent]
  counter_hypothesis:           [incumbent best defense -- grounded in INCUMBENT ANCHOR]
  gate_s_cleared:               [true -- from GATE S Step 2]
  invariant_registry_confirmed: [true -- from GATE S Step 3]
  incumbent_threat_locked:      [true -- from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim -- binding to CAMPAIGN OPEN):
      "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN]
       by {topic} on [dimension]? [Yes / No / Inconclusive]"
      Binding resolves to: incumbent_name from INCUMBENT ANCHOR.
      Naming as literal string = FORMAT ERROR. Template deviation = FORMAT ERROR.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D template verbatim):
Binding active: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name.
Naming as literal string = FORMAT ERROR. Do not re-establish incumbent inline.

  ITEM | SOURCE       | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------|----------------------|----------------------------
  1    | [source]     | [summary]            | "Does [item 1] support the
  2    | [source]     | [summary]            |  displacement of [incumbent
  3    | [source]     | [summary]            |  from CAMPAIGN OPEN] by
  ...  |              |                      |  [topic] on [dim]?
                                             |  [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if any row uses literal name or non-verbatim wording.
  Naming as literal string = FORMAT ERROR. Echoes registry label verbatim.

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  Displacement read: [one sentence: does Stage 2 evidence support, challenge, or leave
                      inconclusive the case for displacing [incumbent from CAMPAIGN OPEN]?]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim -- binding to CAMPAIGN OPEN):
      "Does [practitioner account] reveal a viable transition path from
       [incumbent from CAMPAIGN OPEN] to {topic} for [use case]? [Yes / No / Inconclusive]"
      Binding resolves to: incumbent_name from INCUMBENT ANCHOR.
      Naming as literal string = FORMAT ERROR. Template deviation = FORMAT ERROR.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.
Do not re-establish incumbent name inline. All checks use [incumbent from CAMPAIGN OPEN] binding.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D template verbatim):
Binding active. Naming as literal string = FORMAT ERROR.

  PRACTITIONER | KEY ACCOUNT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -------------|--------------------------|----------------------------
  [type 1]     | [quote or paraphrase]    | "Does [account 1] reveal a viable
  [type 2]     | [quote or paraphrase]    |  transition path from [incumbent
  [type 3]     | [quote or paraphrase]    |  from CAMPAIGN OPEN] to [topic]
                                          |  for [use case]? [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if any row uses literal name or non-verbatim wording.
  Naming as literal string = FORMAT ERROR.

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  Displacement read: [one sentence: does Stage 3 evidence support or challenge displacement
                      of [incumbent from CAMPAIGN OPEN]?]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim -- binding to CAMPAIGN OPEN):
      "Does [prototype result] make a credible case for displacing
       [incumbent from CAMPAIGN OPEN] with {topic}? [Yes / No / Pending]"
      Binding resolves to: incumbent_name from INCUMBENT ANCHOR.
      Naming as literal string = FORMAT ERROR. Template deviation = FORMAT ERROR.

STAGE 4 BODY:

  prototype_design: [brief description]
  prototype_result: [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D template verbatim):
Binding active. Do not re-establish incumbent inline. Naming as literal string = FORMAT ERROR.

  ITEM      | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  ----------|-------------------------------|----------------------------
  prototype | [prototype_result]            | "Does [prototype result] make
                                            |  a credible case for displacing
                                            |  [incumbent from CAMPAIGN OPEN]
                                            |  with [topic]? [Yes/No/Pending]"

  Invariant D checkpoint -- FORMAT ERROR if template omitted, literal used, or verdict missing.
  Naming as literal string = FORMAT ERROR.

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]
  Displacement read: [one sentence: does prototype make credible case for displacing
                      [incumbent from CAMPAIGN OPEN]? Cite s4_displacement_verdict.]

Final null tally:
  null_tally_final = [N]
  Stage 4 cross-check: "Running count from Stage 3 was [M]. Final is [N].
  Match: [true / false]." Mismatch = INTEGRITY FAILURE.

SCHEMA INTEGRITY: [N]/11 handoff fields populated.
Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict = [value]. null_tally_final = [N].
   Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All six SESSION INVARIANT rows (D, A, B, C, E, F) active

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS | VERDICT                                 | EVIDENCE
  -------------------|-----------------------------------------|-------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK applies.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction (INTEGRITY FAILURE if chain total does not match Stage 4):
  S2 -> s2_ce_verdict: [null | value -- from Stage 2 artifact]
  S3 -> s3_ce_verdict: [null | value -- from Stage 3 artifact]
  S4 -> s4_ce_verdict: [null | value -- from Stage 4 artifact]
  Reconstructed null count: [N]
  Stage 4 declared null_tally_final: [M]
  Stage 5 chain confirmation: "S2=[s2_val] + S3=[s3_val] + S4=[s4_val] = [N] null.
    Stage 4 declared [M]. Match: [true / false]."
  Mismatch = INTEGRITY FAILURE. Record before continuing.

DUAL-LOCK EVALUATION:
  null_tally_final = [N]
  If null_tally_final >= 3:
    Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
    Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
    co_activation_confirmed: dual_lock_fired
  Else:
    co_activation_confirmed: not_triggered

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.
Invariant F checkpoint -- SYNTHESIS FORMAT ERROR if any field appears only within prose.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  confidence_composite:  [final numeric value after all reductions]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### SYNTHESIS BODY

  evidence_summary: [2-3 sentences integrating Stages 2, 3, 4. Must cite Stage 4
                     displacement verdict explicitly: "Stage 4 displacement verdict: [Y/N/P]."
                     Do not re-establish the incumbent by name in this prose; all
                     displacement references carry forward from CAMPAIGN OPEN binding.]

### HANDOFF TABLE

SESSION INVARIANT C enforced: all fields carry [derived from: X]. Unlabeled = FORMAT ERROR.
SESSION INVARIANT E enforced: all 11 fields present.
Invariant E checkpoint -- FAIL if any field unlabeled or missing.

  FIELD                      | VALUE   | DERIVATION
  ---------------------------|---------|----------------------------------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]
  hypothesis                 | [value] | [derived from: Stage 1 artifact]
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]
  schema_compliance_confirmed| [true]  | [Invariant E checkpoint -- FAIL if unlabeled/missing]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-05 -- Combined: C-21 + C-22 + C-23 (All Three New Criteria on Full R4 Gold Base)

**Variation axes**: All three new v5 criteria combined. INCUMBENT ANCHOR carries "Do not
re-establish" prohibition (C-21). Invariant D carries binding resolution note and canonical
literal-string failure label (C-22). Stages 2/3/4 artifact writes carry "Displacement read:"
in file body; Stage 5 evidence_summary cites at least one artifact value by name (C-23).
All R4 gold patterns retained: C-14 through C-20.

**Hypothesis**: The three new criteria form a closed structural loop: C-21 seals the incumbent
name at CAMPAIGN OPEN; C-22 makes the binding mechanism self-auditing via two-layer enforcement;
C-23 closes the portability chain by requiring Stage 5 to consume the artifact field value, not
just the stage output verdict. When all three fire together, incumbent identity is traceable from
CAMPAIGN OPEN registration through artifact storage to final synthesis citation -- any break in
the chain is detectable from a registered failure label. This is the maximum aspirational ceiling
for v5.

---

```
You are running the prove-topic Signal skill.

Topic: {topic}
Date:  {date}

The campaign builds the case for displacing the status quo with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has
numbered ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until all
entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS -- FAILURE LABEL REGISTRY

Standalone block. Appears before Stage 0. All invariants active for full campaign.
Cannot be modified or bypassed at any subsequent stage.

  ID | NAME                        | DECLARATION                              | FAILURE LABEL
  ---|-----------------------------|------------------------------------------|---------------------
  D  | INCUMBENT CHECK PHRASING    | Stage 2: "Does [evidence item] support   | FORMAT ERROR
     | REGISTER                    |   the displacement of                    |
     |                             |   [incumbent from CAMPAIGN OPEN]         |
     |                             |   by {topic} on [dimension]?             |
     |                             |   [Yes/No/Inconclusive]"                 |
     |                             | Stage 3: "Does [practitioner account]    |
     |                             |   reveal a viable transition path from   |
     |                             |   [incumbent from CAMPAIGN OPEN]         |
     |                             |   to {topic} for [use case]?             |
     |                             |   [Yes/No/Inconclusive]"                 |
     |                             | Stage 4: "Does [prototype result] make   |
     |                             |   a credible case for displacing         |
     |                             |   [incumbent from CAMPAIGN OPEN]         |
     |                             |   with {topic}? [Yes/No/Pending]"        |
     |                             | Binding: [incumbent from CAMPAIGN OPEN]  |
     |                             |   resolves to incumbent_name from        |
     |                             |   CAMPAIGN OPEN INCUMBENT ANCHOR.        |
     |                             | Naming as literal string = FORMAT ERROR. |
     |                             | Template deviation = FORMAT ERROR.       |
  ---|-----------------------------|------------------------------------------|---------------------
  A  | ADVERSARIAL REVIEWER TYPE   | adversarial_reviewer_type: [role most    | DUAL-LOCK ERROR
     |                             |   likely to challenge displacement].     |
     |                             | Activation: null_tally_final >= 3.       |
  ---|-----------------------------|------------------------------------------|---------------------
  B  | CONFIDENCE CAP              | confidence_composite -= 2 if             | DUAL-LOCK ERROR
     |                             |   null_tally_final >= 3 (hard cap).      |
     |                             | Cannot be softened.                      |
  ---|-----------------------------|------------------------------------------|---------------------
  C  | DERIVATION ANNOTATION       | Every handoff field: [derived from: X].  | FORMAT ERROR
     |                             | Unlabeled field = FORMAT ERROR.          |
  ---|-----------------------------|------------------------------------------|---------------------
  E  | HANDOFF SCHEMA COMPLIANCE   | All 11 handoff fields present, each with | Invariant E
     |                             |   [derived from: X] annotation.          | checkpoint -- FAIL
     |                             | schema_compliance_confirmed row echoes   |
     |                             |   this label verbatim at Stage 5.        |
     |                             | Missing or unlabeled field =             |
     |                             |   Invariant E checkpoint -- FAIL.        |
  ---|-----------------------------|------------------------------------------|---------------------
  F  | SYNTHESIS FIELD ISOLATION   | hypothesis_verdict, confidence_composite,| SYNTHESIS
     |                             |   key_risk: each on its own line.        | FORMAT ERROR
     |                             | Do not embed in prose. Each extractable  |
     |                             |   by label match.                        |
  ---|-----------------------------|------------------------------------------|---------------------
  G  | ARTIFACT DISPLACEMENT READ  | Stages 2, 3, 4 artifact files must carry | PORTABILITY ERROR
     |                             |   "Displacement read: [value]" as        |
     |                             |   labeled field in artifact body.        |
     |                             | Stage 5 evidence_summary must cite at    |
     |                             |   least one artifact Displacement read   |
     |                             |   by value (e.g.,                        |
     |                             |   "websearch Displacement read: [val]"). |
     |                             | Absent from artifact = PORTABILITY ERROR.|
     |                             | Stage 5 cites stage output only,         |
     |                             |   without artifact citation = FAIL.      |

Inline enforcement: Every stage checkpoint echoes the exact FAILURE LABEL from this registry.
Drift between registered label and inline echo = self-incriminating failure.

### ROLE OWNERSHIP TABLE

Roles execute in sequence C -> B -> A before Stage 0.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP
  -------|--------------------------|------------------------------|-------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked      | Step 1
  ROLE B | SCOUT LOADER             | gate_s_cleared               | Step 2
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled;
                            "Do not re-establish" prohibition confirmed present]

ROLE B execution (fill now):
  scout_artifact:  [glob simulations/scout/{topic}-scout-*.md -- exact path or ABSENT]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded = true; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all seven SESSION INVARIANT rows (D, A, B, C, E, F, G) filled and active.
  Confirms Invariant D: "[incumbent from CAMPAIGN OPEN] resolves to incumbent_name."
  Confirms Invariant D canonical failure label: "Naming as literal string = FORMAT ERROR."
  Confirms Invariant E "Invariant E checkpoint -- FAIL" canonical label registered.
  Confirms Invariant G "PORTABILITY ERROR" canonical label registered.
  adversarial_reviewer_type: [role name -- registered now, carried to ATOMIC DUAL-LOCK]
  invariant_registry_confirmed: [true when all seven rows registered]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Stage 5 reconstructs S2->S3->S4 chain independently
and declares Stage 5 chain confirmation. Mismatch = INTEGRITY FAILURE.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE
  ---------------------------|-------------------------------------------
  scout_anchor               | ROLE B scout load
  incumbent_threat_locked    | ROLE C analysis
  hypothesis                 | Stage 1 artifact
  counter_hypothesis         | Stage 1 artifact
  s2_ce_verdict              | Stage 2 artifact
  s3_ce_verdict              | Stage 3 artifact
  s4_ce_verdict              | Stage 4 artifact
  null_tally_final           | s2+s3+s4 CE verdicts (not through co_activation)
  co_activation_confirmed    | ATOMIC DUAL-LOCK (not through incumbent_defense)
  incumbent_defense_closed   | s2+s3+s4 direct chain (not through co_activation)
  confidence_composite       | Stage 5 synthesis (capped by Invariant B if triggered)

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] "Do not re-establish" prohibition confirmed present in INCUMBENT ANCHOR
  [ ] SESSION INVARIANTS block complete -- all seven rows (D, A, B, C, E, F, G) registered
  [ ] Invariant D binding resolution note confirmed:
      "[incumbent from CAMPAIGN OPEN] resolves to incumbent_name. Naming as literal string = FORMAT ERROR."
  [ ] Invariant E canonical label confirmed: "Invariant E checkpoint -- FAIL"
  [ ] Invariant G canonical label confirmed: "PORTABILITY ERROR"
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- all labels confirmed; invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|-------------------------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role. Label: ORDER ERROR.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 confirmed.
   INCUMBENT ANCHOR locked: 'Do not re-establish' prohibition active.
   Invariant D binding active: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name.
   Naming as literal string = FORMAT ERROR active.
   Invariant E checkpoint -- FAIL registered.
   PORTABILITY ERROR registered.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates with [incumbent from CAMPAIGN OPEN] binding active
  [ ] INCUMBENT ANCHOR prohibition active: no inline re-establishment of incumbent

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.
Incumbent identity carries from CAMPAIGN OPEN. Do not re-state incumbent_name in this block.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic} displacing incumbent]
  counter_hypothesis:           [incumbent best defense -- grounded in INCUMBENT ANCHOR]
  gate_s_cleared:               [true -- from GATE S Step 2]
  invariant_registry_confirmed: [true -- from GATE S Step 3]
  incumbent_threat_locked:      [true -- from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim -- binding to CAMPAIGN OPEN):
      "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN]
       by {topic} on [dimension]? [Yes / No / Inconclusive]"
      Binding: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name from INCUMBENT ANCHOR.
      Naming as literal string = FORMAT ERROR. Template deviation = FORMAT ERROR.
  [ ] SESSION INVARIANT G active: artifact body must carry "Displacement read: [value]"

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D template verbatim):
Binding active. Naming as literal string = FORMAT ERROR. Do not re-establish incumbent inline.

  ITEM | SOURCE       | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------|----------------------|----------------------------
  1    | [source]     | [summary]            | "Does [item 1] support the
  2    | [source]     | [summary]            |  displacement of [incumbent
  3    | [source]     | [summary]            |  from CAMPAIGN OPEN] by
  ...  |              |                      |  [topic] on [dim]?
                                             |  [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if any row uses literal name or non-verbatim wording.
  Naming as literal string = FORMAT ERROR. Echoes registry label verbatim.

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  Displacement read: [one sentence: does Stage 2 evidence support, challenge, or leave
                      inconclusive the case for displacing [incumbent from CAMPAIGN OPEN]?]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-websearch-{date}.md
Artifact body must include as a labeled field:
  Displacement read: [value from Stage 2 Displacement read above]
Invariant G checkpoint -- PORTABILITY ERROR if "Displacement read:" absent from artifact body.
Confirm write with: "{topic}-websearch-{date}.md written. Displacement read: [value] in artifact."

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N].
   Artifact Displacement read: [value] confirmed. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] Stage 2 artifact Displacement read confirmed in file body
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim -- binding to CAMPAIGN OPEN):
      "Does [practitioner account] reveal a viable transition path from
       [incumbent from CAMPAIGN OPEN] to {topic} for [use case]? [Yes / No / Inconclusive]"
      Binding: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name from INCUMBENT ANCHOR.
      Naming as literal string = FORMAT ERROR. Template deviation = FORMAT ERROR.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.
Do not re-establish incumbent name inline. Binding carries from CAMPAIGN OPEN.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D template verbatim):
Binding active. Naming as literal string = FORMAT ERROR.

  PRACTITIONER | KEY ACCOUNT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -------------|--------------------------|----------------------------
  [type 1]     | [quote or paraphrase]    | "Does [account 1] reveal a viable
  [type 2]     | [quote or paraphrase]    |  transition path from [incumbent
  [type 3]     | [quote or paraphrase]    |  from CAMPAIGN OPEN] to [topic]
                                          |  for [use case]? [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if any row uses literal name or non-verbatim wording.
  Naming as literal string = FORMAT ERROR.

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  Displacement read: [one sentence: does Stage 3 evidence support or challenge displacement
                      of [incumbent from CAMPAIGN OPEN]?]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-interview-{date}.md
Artifact body must include as a labeled field:
  Displacement read: [value from Stage 3 Displacement read above]
Invariant G checkpoint -- PORTABILITY ERROR if "Displacement read:" absent from artifact body.
Confirm write with: "{topic}-interview-{date}.md written. Displacement read: [value] in artifact."

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N].
   Artifact Displacement read: [value] confirmed. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] Stage 3 artifact Displacement read confirmed in file body
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim -- binding to CAMPAIGN OPEN):
      "Does [prototype result] make a credible case for displacing
       [incumbent from CAMPAIGN OPEN] with {topic}? [Yes / No / Pending]"
      Binding: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name from INCUMBENT ANCHOR.
      Naming as literal string = FORMAT ERROR. Template deviation = FORMAT ERROR.

STAGE 4 BODY:
Do not re-establish incumbent name inline. All displacement references use CAMPAIGN OPEN binding.

  prototype_design: [brief description]
  prototype_result: [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D template verbatim):
Binding active. Naming as literal string = FORMAT ERROR.

  ITEM      | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  ----------|-------------------------------|----------------------------
  prototype | [prototype_result]            | "Does [prototype result] make
                                            |  a credible case for displacing
                                            |  [incumbent from CAMPAIGN OPEN]
                                            |  with [topic]? [Yes/No/Pending]"

  Invariant D checkpoint -- FORMAT ERROR if template omitted, literal used, or verdict missing.
  Naming as literal string = FORMAT ERROR.

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]
  Displacement read: [one sentence: does prototype make credible case for displacing
                      [incumbent from CAMPAIGN OPEN]? Cite s4_displacement_verdict.]

Final null tally:
  null_tally_final = [N]
  Stage 4 cross-check: "Running count from Stage 3 was [M]. Final is [N].
  Match: [true / false]." Mismatch = INTEGRITY FAILURE.

SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-prototype-{date}.md
Artifact body must include as a labeled field:
  Displacement read: [value from Stage 4 Displacement read above]
Invariant G checkpoint -- PORTABILITY ERROR if "Displacement read:" absent from artifact body.
Confirm write with: "{topic}-prototype-{date}.md written. Displacement read: [value] in artifact."

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict = [value]. null_tally_final = [N].
   Artifact Displacement read: [value] confirmed. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] All three artifact Displacement read values confirmed in artifact file bodies
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All seven SESSION INVARIANT rows (D, A, B, C, E, F, G) active

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS | VERDICT                                 | EVIDENCE
  -------------------|-----------------------------------------|-------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK applies.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction (INTEGRITY FAILURE if chain total does not match Stage 4):
  S2 -> s2_ce_verdict: [null | value -- from Stage 2 artifact]
  S3 -> s3_ce_verdict: [null | value -- from Stage 3 artifact]
  S4 -> s4_ce_verdict: [null | value -- from Stage 4 artifact]
  Reconstructed null count: [N]
  Stage 4 declared null_tally_final: [M]
  Stage 5 chain confirmation: "S2=[s2_val] + S3=[s3_val] + S4=[s4_val] = [N] null.
    Stage 4 declared [M]. Match: [true / false]."
  Mismatch = INTEGRITY FAILURE. Record before continuing.

DUAL-LOCK EVALUATION:
  null_tally_final = [N]
  If null_tally_final >= 3:
    Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
    Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
    co_activation_confirmed: dual_lock_fired
  Else:
    co_activation_confirmed: not_triggered

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.
Invariant F checkpoint -- SYNTHESIS FORMAT ERROR if any field appears only within prose.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  confidence_composite:  [final numeric value after all reductions]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### SYNTHESIS BODY

  evidence_summary: [2-3 sentences integrating Stages 2, 3, 4. Must include ALL of:
    (1) Stage 4 displacement verdict: "Stage 4 displacement verdict: [Y/N/P]."
    (2) At least one artifact Displacement read citation by value -- cite the artifact
        field, not just the stage output. Required forms:
          "websearch Displacement read: [value from {topic}-websearch-{date}.md]"
          "interview Displacement read: [value from {topic}-interview-{date}.md]"
          "prototype Displacement read: [value from {topic}-prototype-{date}.md]"
        Minimum: one artifact cited by Displacement read value.
        All three is ideal. Zero = PORTABILITY ERROR (Invariant G checkpoint).
    (3) Do not re-establish incumbent by literal name. Carry from CAMPAIGN OPEN binding.]

### HANDOFF TABLE

SESSION INVARIANT C enforced: all fields carry [derived from: X]. Unlabeled = FORMAT ERROR.
SESSION INVARIANT E enforced: all 11 fields present.
Invariant E checkpoint -- FAIL if any field unlabeled or missing.

  FIELD                      | VALUE   | DERIVATION
  ---------------------------|---------|----------------------------------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]
  hypothesis                 | [value] | [derived from: Stage 1 artifact]
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]
  schema_compliance_confirmed| [true]  | [Invariant E checkpoint -- FAIL if unlabeled/missing]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   Artifact Displacement reads consumed by synthesis confirmed."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## Variation Summary

| Var | Axis | C-21 | C-22 | C-23 | Notes |
|-----|------|------|------|------|-------|
| V-01 | INCUMBENT ANCHOR prohibition | + | -- | -- | Prohibition text added; Invariant D unchanged |
| V-02 | Invariant D binding resolution note | -- | + | -- | `[incumbent from CAMPAIGN OPEN]` + binding note + literal-string label; no prohibition |
| V-03 | Artifact Displacement read portability | -- | -- | + | Invariant G added; artifact writes carry field; Stage 5 must cite value |
| V-04 | C-21 + C-22 combined | + | + | -- | Registration layer complete: anchor sealed + binding failure label active |
| V-05 | All three combined | + | + | + | Maximum v5 ceiling; displacement chain traceable CAMPAIGN OPEN -> artifact -> synthesis |

**Expected scoring delta vs R4 V-05 base (86 on v4 rubric):**
- V-01: +2 (C-21) = ~88 expected
- V-02: +2 (C-22) + +1 (C-19 already in base, now reinforced) = ~88 expected
- V-03: +2 (C-23) = ~88 expected
- V-04: +4 (C-21 + C-22) = ~90 expected
- V-05: +6 (C-21 + C-22 + C-23) = ~92 expected; golden threshold requires composite >= 80 + all 5 essential PASS
