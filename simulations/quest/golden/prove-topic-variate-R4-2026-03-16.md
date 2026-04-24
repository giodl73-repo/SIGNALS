---
skill: quest-variate
skill_target: prove-topic
round: R4
date: 2026-03-16
rubric: prove-topic-rubric-v4-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [invariant_e_registration, invariant_d_template_binding, artifact_displacement_read]
  combined: [V-04 (C-18+C-19), V-05 (all_three_new + C-06_fix + C-09_fix)]
round_targets: >
  v4 adds C-18/C-19/C-20 from R3 excellence signals.
  C-18: Register Invariant E in SESSION INVARIANTS block with canonical "Invariant E
        checkpoint -- FAIL" label, echoed at schema_compliance_confirmed row.
  C-19: Invariant D template text uses [incumbent from CAMPAIGN OPEN] binding throughout.
        Stage tables carry bound text -- incumbent never re-established per stage.
  C-20: Websearch/interview/prototype write confirmations explicitly describe "Displacement
        read:" as part of artifact file content, not just stage output.
  All R4 variations fix C-05 (persistent essential gap from R3): Stage 5 reconstructs
  S2->S3->S4->null_tally_final chain with explicit "Stage 5 chain confirmation" statement.
  All R4 variations carry forward R3 gold: C-14 (two-layer), C-15 (CAMPAIGN OPEN),
  C-16 (per-stage Displacement read), C-17 (SYNTHESIS DECLARATIONS prohibition).
r3_scores:
  V-01: 79
  V-02: 76
  V-03: 76
  V-04: 81
  V-05: 86
---

## V-01 -- Axis: Invariant E Registration (C-18)

**Variation axis**: C-18 only -- register Invariant E in SESSION INVARIANTS FAILURE LABEL REGISTRY
with canonical "Invariant E checkpoint -- FAIL" label; schema_compliance_confirmed row echoes it verbatim.

**Hypothesis**: Registering a named Invariant E in the SESSION INVARIANTS block with canonical label
extends the two-layer enforcement architecture to the handoff schema. The same bidirectional detection
that governs Invariant D now governs the HANDOFF TABLE: any missing or unlabeled handoff field is
self-incriminating from two structural directions (registry + inline echo) simultaneously.

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
     |                             |   likely to challenge displacement].      |
     |                             | Activation: null_tally_final >= 3.        |
  ---|-----------------------------|------------------------------------------|---------------------
  B  | CONFIDENCE CAP              | confidence_composite -= 2 if              | DUAL-LOCK ERROR
     |                             |   null_tally_final >= 3 (hard cap).       |
     |                             | Cannot be softened.                       |
  ---|-----------------------------|------------------------------------------|---------------------
  C  | DERIVATION ANNOTATION       | Every handoff field: [derived from: X].  | FORMAT ERROR
     |                             | Unlabeled field = FORMAT ERROR.           |
  ---|-----------------------------|------------------------------------------|---------------------
  E  | HANDOFF SCHEMA COMPLIANCE   | All 11 handoff fields present, each with | Invariant E
     |                             |   [derived from: X] annotation.          | checkpoint -- FAIL
     |                             | schema_compliance_confirmed row echoes    |
     |                             |   this label verbatim at Stage 5.        |
     |                             | Missing or unlabeled field =             |
     |                             |   Invariant E checkpoint -- FAIL.        |
  ---|-----------------------------|------------------------------------------|---------------------
  F  | SYNTHESIS FIELD ISOLATION   | hypothesis_verdict, confidence_composite,| SYNTHESIS
     |                             |   key_risk: each on its own line.        |   FORMAT ERROR
     |                             | Do not embed in prose. Each extractable  |
     |                             |   by label match.                        |

Inline enforcement: Every stage checkpoint echoes the exact FAILURE LABEL from this registry.
Drift between registered label and inline echo = self-incriminating failure.

### ROLE OWNERSHIP TABLE

Roles execute in sequence C -> B -> A before Stage 0.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP
  -------|--------------------------|---------------------------|-------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-{date}.md or equivalent path]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all six SESSION INVARIANT rows (D, A, B, C, E, F) filled and active.
  Confirms Invariant E "Invariant E checkpoint -- FAIL" canonical label registered.
  invariant_registry_confirmed: [true when all six invariants registered]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Stage 5 ATOMIC DUAL-LOCK reconstructs S2->S3->S4 chain
independently and declares Stage 5 chain confirmation statement. Mismatch = INTEGRITY FAILURE.

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
  confidence_composite       | Stage 5 synthesis (capped by Invariant B)

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS block complete -- all six rows (D, A, B, C, E, F) registered;
      Invariant E "Invariant E checkpoint -- FAIL" canonical label confirmed
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- invariant_registry_confirmed = true

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
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent best defense -- grounded in ROLE C analysis]
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

  ITEM | SOURCE                   | SUMMARY (1 sentence)  | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|----------------------------
  1    | [source]                 | [summary]            | "Does [item 1] support the
  2    | [source]                 | [summary]            |  displacement of [comparator]
  3    | [source]                 | [summary]            |  by [topic] on [dim]?
  ...  |                          |                      |  [Yes/No/Inconclusive]"

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

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT
  -----------------|------------------------------|----------------------------
  [type 1]         | [quote or paraphrase]        | "Does [account 1] reveal a
  [type 2]         | [quote or paraphrase]        |  viable transition path from
  [type 3]         | [quote or paraphrase]        |  [comparator] to [topic]
  ...              |                              |  for [use case]?
                   |                              |  [Yes/No/Inconclusive]"

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

  prototype_design:   [brief description]
  prototype_result:   [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D template verbatim):

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-----------------------------
  prototype  | [prototype_result]            | "Does [prototype result] make
             |                               |  a credible case for displacing
             |                               |  [comparator] with [topic]?
             |                               |  [Yes/No/Pending]"

  Invariant D checkpoint -- FORMAT ERROR if template omitted or verdict missing.

  s4_displacement_verdict: [Yes / No / Pending]   <- required; omission = FORMAT ERROR
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

  COUNTER_HYPOTHESIS     | VERDICT                                   | EVIDENCE
  -----------------------|-------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK   | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

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

  FIELD                      | VALUE   | DERIVATION                             | IND. CHAIN
  ---------------------------|---------|----------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]      | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]        | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]       | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]       | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]       | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]       | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]       | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]   | not through
                             |         |                                        |   co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]       | not through
                             |         |                                        |   incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]  | not through
                             |         |                                        |   co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]      | capped by INV B
  schema_compliance_confirmed| [true]  | [Invariant E checkpoint -- FAIL if any  | n/a
                             |         |  field unlabeled or missing]           |

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-02 -- Axis: Invariant D Template Binding to CAMPAIGN OPEN (C-19)

**Variation axis**: C-19 only -- Invariant D entry in SESSION INVARIANTS uses `[incumbent from
CAMPAIGN OPEN]` as the bound interpolation token. Stage check tables carry this bound text
verbatim. The incumbent is never re-established as a literal string per stage.

**Hypothesis**: Wiring the displacement-question templates to `[incumbent from CAMPAIGN OPEN]`
makes the binding architectural. The incumbent is named once (INCUMBENT ANCHOR in CAMPAIGN OPEN)
and referenced structurally everywhere else. Any stage that drifts to a literal string is
detectable because it diverges from the registered bound template -- the same bidirectional
principle as C-14, applied to template content rather than failure labels.

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

Fill before any role or invariant registration. All subsequent displacement checks
bind to the incumbent declared here. Do not re-establish the incumbent per stage.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS -- FAILURE LABEL REGISTRY

Standalone block. Appears before Stage 0. All invariants active for full campaign.
Cannot be modified or bypassed at any subsequent stage.

  ID | NAME                        | DECLARATION                                  | FAILURE LABEL
  ---|-----------------------------|----------------------------------------------|---------------------
  D  | INCUMBENT CHECK PHRASING    | Stage 2: "Does [evidence item] support the   | FORMAT ERROR
     | REGISTER                    |   displacement of [incumbent from CAMPAIGN   |
     |                             |   OPEN] by {topic} on [dimension]?           |
     |                             |   [Yes / No / Inconclusive]"                 |
     |                             | Stage 3: "Does [practitioner account] reveal |
     |                             |   a viable transition path from [incumbent   |
     |                             |   from CAMPAIGN OPEN] to {topic} for [use    |
     |                             |   case]? [Yes / No / Inconclusive]"          |
     |                             | Stage 4: "Does [prototype result] make a     |
     |                             |   credible case for displacing [incumbent    |
     |                             |   from CAMPAIGN OPEN] with {topic}?          |
     |                             |   [Yes / No / Pending]"                      |
     |                             | Binding: [incumbent from CAMPAIGN OPEN]      |
     |                             |   resolves to incumbent_name declared above. |
     |                             | Template deviation = FORMAT ERROR.           |
     |                             | Naming incumbent as literal string instead   |
     |                             |   of using CAMPAIGN OPEN binding = FORMAT    |
     |                             |   ERROR.                                     |
  ---|-----------------------------|----------------------------------------------|---------------------
  A  | ADVERSARIAL REVIEWER TYPE   | adversarial_reviewer_type: [role most likely | DUAL-LOCK ERROR
     |                             |   to challenge displacement].                 |
     |                             | Activation: null_tally_final >= 3.            |
  ---|-----------------------------|----------------------------------------------|---------------------
  B  | CONFIDENCE CAP              | confidence_composite -= 2 if                  | DUAL-LOCK ERROR
     |                             |   null_tally_final >= 3 (hard cap).           |
     |                             | Cannot be softened.                           |
  ---|-----------------------------|----------------------------------------------|---------------------
  C  | DERIVATION ANNOTATION       | Every handoff field: [derived from: X].      | FORMAT ERROR
     |                             | Unlabeled field = FORMAT ERROR.               |
  ---|-----------------------------|----------------------------------------------|---------------------
  E  | HANDOFF SCHEMA COMPLIANCE   | All 11 handoff fields present, labeled.      | FORMAT ERROR
  ---|-----------------------------|----------------------------------------------|---------------------
  F  | SYNTHESIS FIELD ISOLATION   | hypothesis_verdict, confidence_composite,    | SYNTHESIS
     |                             |   key_risk: each on its own line,            |   FORMAT ERROR
     |                             |   extractable by label match.                |

Inline enforcement: Every stage checkpoint echoes the exact FAILURE LABEL from this registry.

### ROLE OWNERSHIP TABLE

Roles execute in sequence C -> B -> A before Stage 0.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP
  -------|--------------------------|---------------------------|-------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-{date}.md or equivalent path]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all six SESSION INVARIANT rows filled and active.
  Confirms Invariant D templates use [incumbent from CAMPAIGN OPEN] binding.
  invariant_registry_confirmed: [true when all confirmed]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Stage 5 reconstructs chain and declares Stage 5 chain
confirmation. Mismatch = INTEGRITY FAILURE.

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
  confidence_composite       | Stage 5 synthesis (capped by Invariant B)

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator, incumbent_name)
  [ ] INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS block complete -- six rows; Invariant D templates confirmed to use
      [incumbent from CAMPAIGN OPEN] binding
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout loaded confirmed
  [ ] ROLE A executed -- invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|-------------------------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Label: ORDER ERROR.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 confirmed. Invariant D bound to [incumbent
   from CAMPAIGN OPEN]. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] Invariant D templates confirmed using [incumbent from CAMPAIGN OPEN] binding

STAGE 1 BODY:

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent best defense -- grounded in ROLE C analysis]
  gate_s_cleared:               [true]
  invariant_registry_confirmed: [true]
  incumbent_threat_locked:      [true]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] Invariant D Stage 2 template with [incumbent from CAMPAIGN OPEN] binding active:
      "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN]
       by {topic} on [dimension]? [Yes / No / Inconclusive]"
      Invariant D checkpoint -- FORMAT ERROR if deviated or incumbent named as literal.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 ([incumbent from CAMPAIGN OPEN] bound):

  ITEM | SOURCE   | SUMMARY           | TEMPLATE APPLIED & VERDICT
  -----|----------|-------------------|----------------------------
  1    | [source] | [summary]         | "Does [item 1] support the displacement of
  2    | [source] | [summary]         |  [incumbent from CAMPAIGN OPEN] by [topic]
  3    | [source] | [summary]         |  on [dim]? [Yes/No/Inconclusive]"
  ...

  Invariant D checkpoint -- FORMAT ERROR if any row names incumbent as literal string.

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  Displacement read: [one sentence synthesis of Stage 2 displacement evidence]

Running null tally: "Running tally: [N] null. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 populated.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded
  [ ] Invariant D Stage 3 template with [incumbent from CAMPAIGN OPEN] binding active:
      "Does [practitioner account] reveal a viable transition path from [incumbent from
       CAMPAIGN OPEN] to {topic} for [use case]? [Yes / No / Inconclusive]"
      Invariant D checkpoint -- FORMAT ERROR if deviated or incumbent named as literal.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 ([incumbent from CAMPAIGN OPEN] bound):

  PRACTITIONER | KEY ACCOUNT       | TEMPLATE APPLIED & VERDICT
  -------------|-------------------|---------------------------------
  [type 1]     | [paraphrase]      | "Does [account] reveal a viable transition path
  [type 2]     | [paraphrase]      |  from [incumbent from CAMPAIGN OPEN] to [topic]
  [type 3]     | [paraphrase]      |  for [use case]? [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if incumbent re-established as literal string.

  s3_incumbent_check_summary: [N/M/P]
  s3_ce_verdict:              [null | citation]
  Displacement read: [one sentence synthesis of Stage 3 transition evidence]

Running null tally: "Running tally: [N] null. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 populated.
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded
  [ ] Invariant D Stage 4 template with [incumbent from CAMPAIGN OPEN] binding active:
      "Does [prototype result] make a credible case for displacing [incumbent from
       CAMPAIGN OPEN] with {topic}? [Yes / No / Pending]"
      Invariant D checkpoint -- FORMAT ERROR if deviated or incumbent named as literal.

STAGE 4 BODY:

  prototype_design:   [brief description]
  prototype_result:   [what was learned]

INCUMBENT CHECK TABLE -- Stage 4 ([incumbent from CAMPAIGN OPEN] bound):

  ITEM      | RESULT     | TEMPLATE APPLIED & VERDICT
  ----------|------------|---------------------------------------------
  prototype | [result]   | "Does [result] make a credible case for
            |            |  displacing [incumbent from CAMPAIGN OPEN]
            |            |  with [topic]? [Yes/No/Pending]"

  Invariant D checkpoint -- FORMAT ERROR if template omitted, verdict missing, or
  incumbent named as literal string.

  s4_displacement_verdict: [Yes / No / Pending]
  s4_ce_verdict:           [null | description]
  Displacement read: [one sentence synthesis of Stage 4 prototype displacement verdict]

Final null tally:
  null_tally_final = [N]
  Stage 4 cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [T/F]."
  Mismatch = INTEGRITY FAILURE.

SCHEMA INTEGRITY: [N]/11 populated.
Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis present; Invariant D [incumbent from CAMPAIGN OPEN] binding active

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS | VERDICT                                 | EVIDENCE
  -------------------|-----------------------------------------|-------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK | [cite artifact]

OPEN RISK: reduce confidence_composite one tier.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction (INTEGRITY FAILURE if mismatch):
  S2 -> s2_ce_verdict: [null | value]
  S3 -> s3_ce_verdict: [null | value]
  S4 -> s4_ce_verdict: [null | value]
  Reconstructed null count: [N]
  Stage 4 declared null_tally_final: [M]
  Stage 5 chain confirmation: "S2=[v] + S3=[v] + S4=[v] = [N] null. Stage 4 declared [M].
    Match: [true / false]."
  Mismatch = INTEGRITY FAILURE. Record before continuing.

DUAL-LOCK EVALUATION:
  If null_tally_final >= 3:
    Lock 1 (INV A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
    Lock 2 (INV B): confidence_composite -= 2 (hard cap).
    co_activation_confirmed: dual_lock_fired
  Else:
    co_activation_confirmed: not_triggered

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.
Invariant F checkpoint -- SYNTHESIS FORMAT ERROR if any field in prose.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  confidence_composite:  [final value]
  key_risk:              [residual incumbent strength]

### SYNTHESIS BODY

  evidence_summary: [2-3 sentences. Cite Stage 4 displacement verdict. Reference
                     [incumbent from CAMPAIGN OPEN] by bound name -- no re-establishment.]

### HANDOFF TABLE

SESSION INVARIANT C: all fields [derived from: X]. FORMAT ERROR if unlabeled.
SESSION INVARIANT E: all 11 fields present. FORMAT ERROR if missing.

  FIELD                      | VALUE   | DERIVATION                             | IND. CHAIN
  ---------------------------|---------|----------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]      | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]        | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]       | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]       | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]       | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]       | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]       | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]   | not through co_act.
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]       | not through inc_def.
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]  | not through co_act.
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]      | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields labeled; FORMAT ERROR   | n/a
                             |         |  if any missing or unlabeled]          |

STAGE 5 EXIT SIGNAL: synthesis_complete
Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-03 -- Axis: Artifact Displacement Read Portability (C-20)

**Variation axis**: C-20 only -- each write confirmation for websearch, interview, and prototype
artifacts explicitly states that "Displacement read:" is part of the artifact file content, not
just stage output. The write confirmation carries the Displacement read value.

**Hypothesis**: Declaring "Displacement read:" as a required artifact field (not just stage output)
makes displacement evidence portable to downstream skills without re-reading stage output. The
per-stage reads (C-16) become structurally durable: they travel with the artifact file to
topic-story, handoff reader, and any future consumer. Missing from any one artifact = gap in
the displacement evidence chain.

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

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS -- FAILURE LABEL REGISTRY

Standalone block. Appears before Stage 0. All invariants active for full campaign.

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
  A  | ADVERSARIAL REVIEWER TYPE   | adversarial_reviewer_type: [role].       | DUAL-LOCK ERROR
     |                             | Activation: null_tally_final >= 3.        |
  ---|-----------------------------|------------------------------------------|---------------------
  B  | CONFIDENCE CAP              | -= 2 if null_tally_final >= 3.           | DUAL-LOCK ERROR
  ---|-----------------------------|------------------------------------------|---------------------
  C  | DERIVATION ANNOTATION       | Every handoff field: [derived from: X].  | FORMAT ERROR
  ---|-----------------------------|------------------------------------------|---------------------
  E  | HANDOFF SCHEMA COMPLIANCE   | All 11 fields present, labeled.          | FORMAT ERROR
  ---|-----------------------------|------------------------------------------|---------------------
  F  | SYNTHESIS FIELD ISOLATION   | hypothesis_verdict, confidence_composite,| SYNTHESIS
     |                             |   key_risk: each on its own line.        |   FORMAT ERROR

ARTIFACT DISPLACEMENT RULE (locked): The websearch, interview, and prototype artifacts must
each include a labeled "Displacement read:" field as part of their written file content.
Each write confirmation must explicitly state this field was written to the artifact.
A "Displacement read:" present only in stage output but not described in the artifact
write confirmation = FORMAT ERROR for that artifact. All three must carry the field.

Inline enforcement: Every stage checkpoint echoes the registered FAILURE LABEL above.

### ROLE OWNERSHIP TABLE

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP
  -------|--------------------------|---------------------------|-------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3

ROLE C (fill now): incumbent_threat_locked: [true when INCUMBENT ANCHOR complete]
ROLE B (fill now):
  scout_artifact:  [{topic}-scout-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if loaded; CAMPAIGN BLOCKED otherwise]
ROLE A (fill now):
  Confirms ARTIFACT DISPLACEMENT RULE registered alongside all invariants.
  invariant_registry_confirmed: [true when confirmed]

### CE VERDICT OWNERSHIP TABLE

  s2_ce_verdict / s3_ce_verdict / s4_ce_verdict: null or citation per stage.
  null_tally_final: count(null) across s2+s3+s4, owned by Stage 4 close.
  Stage 5 reconstructs independently. Mismatch = INTEGRITY FAILURE.

### PRE-COMMITTED HANDOFF SCHEMA

scout_anchor | incumbent_threat_locked | hypothesis | counter_hypothesis |
s2_ce_verdict | s3_ce_verdict | s4_ce_verdict | null_tally_final |
co_activation_confirmed | incumbent_defense_closed | confidence_composite

---

## STAGE 0 -- GATE S

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | RESULT
  -----|------------------------------|---------|-------------------------
  1    | incumbent_threat_locked      | ROLE C  | [confirm or BLOCKED: ORDER ERROR]
  2    | gate_s_cleared               | ROLE B  | [confirm or BLOCKED: ORDER ERROR]
  3    | invariant_registry_confirmed | ROLE A  | [confirm or BLOCKED: ORDER ERROR]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- ARTIFACT DISPLACEMENT RULE active. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

  source_scout_artifact:        [from ROLE B]
  hypothesis:                   [falsifiable claim]
  counter_hypothesis:           [incumbent best defense]
  gate_s_cleared / invariant_registry_confirmed / incumbent_threat_locked: [true]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked

---

## STAGE 2 -- WEB SEARCH

ENTRY: hypothesis_locked received. Invariant D Stage 2 template active.
ARTIFACT DISPLACEMENT RULE active: websearch artifact will include Displacement read.

INCUMBENT CHECK TABLE -- Stage 2 (Invariant D template verbatim):

  ITEM | SOURCE | SUMMARY | TEMPLATE & VERDICT
  -----|--------|---------|----------------------------
  1    | [src]  | [sum]   | "Does [item] support the displacement of [comparator] by [topic]
  2    | [src]  | [sum]   |  on [dim]? [Yes/No/Inconclusive]"
  3+   |        |         |

  Invariant D checkpoint -- FORMAT ERROR if template deviated.

  s2_incumbent_check_summary: [N/M/P]
  s2_ce_verdict:              [null | citation]
  Displacement read: [one sentence: Stage 2 evidence verdict on displacing {status_quo_comparator}]

Running null tally: [N] null across 1 stage. 2 remain.
SCHEMA INTEGRITY: [N]/11 populated.

Write artifact: {topic}-websearch-{date}.md
  Artifact includes:
    Displacement read: [exact value from Displacement read field above]
  Confirm write: "{topic}-websearch-{date}.md written. Artifact includes Displacement read: [value]."

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N]."

---

## STAGE 3 -- INTERVIEW

ENTRY: websearch_complete. s2_ce_verdict recorded. Invariant D Stage 3 template active.
ARTIFACT DISPLACEMENT RULE active: interview artifact will include Displacement read.

INCUMBENT CHECK TABLE -- Stage 3 (Invariant D template verbatim):

  PRACTITIONER | KEY ACCOUNT  | TEMPLATE & VERDICT
  -------------|--------------|-----------------------------
  [type 1]     | [paraphrase] | "Does [account] reveal a viable transition path from
  [type 2]     | [paraphrase] |  [comparator] to [topic] for [use case]? [verdict]"
  [type 3]     | [paraphrase] |

  Invariant D checkpoint -- FORMAT ERROR if template deviated.

  s3_incumbent_check_summary: [N/M/P]
  s3_ce_verdict:              [null | citation]
  Displacement read: [one sentence: Stage 3 transition evidence verdict]

Running null tally: [N] null across 2 stages. 1 remains.
SCHEMA INTEGRITY: [N]/11 populated.

Write artifact: {topic}-interview-{date}.md
  Artifact includes:
    Displacement read: [exact value from Displacement read field above]
  Confirm write: "{topic}-interview-{date}.md written. Artifact includes Displacement read: [value]."

STAGE 3 EXIT SIGNAL: interview_complete

---

## STAGE 4 -- PROTOTYPE

ENTRY: interview_complete. s3_ce_verdict recorded. Invariant D Stage 4 template active.
ARTIFACT DISPLACEMENT RULE active: prototype artifact will include Displacement read.

  prototype_design: [brief description]
  prototype_result: [what was learned]

INCUMBENT CHECK TABLE -- Stage 4 (Invariant D template verbatim):

  ITEM      | RESULT   | TEMPLATE & VERDICT
  ----------|----------|-----------------------------------------
  prototype | [result] | "Does [result] make a credible case for displacing [comparator]
            |          |  with [topic]? [Yes/No/Pending]"

  Invariant D checkpoint -- FORMAT ERROR if template omitted or verdict missing.

  s4_displacement_verdict: [Yes / No / Pending]
  s4_ce_verdict:           [null | description]
  Displacement read: [one sentence: Stage 4 prototype displacement verdict]

  null_tally_final = [N]
  Stage 4 cross-check: "Stage 3 count [M]. Final [N]. Match: [T/F]." Mismatch = INTEGRITY FAILURE.

SCHEMA INTEGRITY: [N]/11 populated.

Write artifact: {topic}-prototype-{date}.md
  Artifact includes:
    Displacement read: [exact value from Displacement read field above]
  Confirm write: "{topic}-prototype-{date}.md written. Artifact includes Displacement read: [value]."

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- null_tally_final = [N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

ENTRY: prototype_complete. null_tally_final recorded. All three artifact Displacement reads confirmed.

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS | VERDICT (REFUTED/PARTIALLY REFUTED/OPEN RISK) | EVIDENCE

OPEN RISK: reduce confidence_composite one tier.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction:
  S2 -> s2_ce_verdict: [null | value]
  S3 -> s3_ce_verdict: [null | value]
  S4 -> s4_ce_verdict: [null | value]
  Reconstructed: [N]
  Stage 4 declared: [M]
  Stage 5 chain confirmation: "S2=[v]+S3=[v]+S4=[v]=[N]. Stage 4=[M]. Match: [T/F]."
  Mismatch = INTEGRITY FAILURE.

  If null_tally_final >= 3:
    Lock 1 (INV A): adversarial review by [type]. BLOCKED.
    Lock 2 (INV B): confidence_composite -= 2. Hard cap.
    co_activation_confirmed: dual_lock_fired
  Else:
    co_activation_confirmed: not_triggered

### SYNTHESIS DECLARATIONS

Do not embed in prose. Each on its own line. Invariant F -- SYNTHESIS FORMAT ERROR if in prose.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  confidence_composite:  [final value]
  key_risk:              [residual incumbent strength]

### SYNTHESIS BODY

  evidence_summary: [2-3 sentences. Must cite Stage 4 artifact Displacement read explicitly.
                     Must state: "Stage 4 displacement verdict: [Yes/No/Pending]."]

### HANDOFF TABLE

All 11 fields. Each [derived from: X]. Invariant C: unlabeled = FORMAT ERROR.
Invariant E: missing field = FORMAT ERROR.

  scout_anchor               | [value] | [derived from: ROLE B]          | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C]          | n/a
  hypothesis                 | [value] | [derived from: Stage 1]         | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1]         | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2]         | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3]         | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4]         | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4]        | not through co_act.
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]| not through inc_def.
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct] | not through co_act.
  confidence_composite       | [value] | [derived from: Stage 5]         | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 labeled; FORMAT ERROR   | n/a
                             |         |  if any missing or unlabeled]   |

STAGE 5 EXIT SIGNAL: synthesis_complete
Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both. Campaign complete.
```

---

## V-04 -- Combo: Invariant E Registration + Invariant D Template Binding (C-18 + C-19)

**Variation axis**: C-18 + C-19 -- Invariant E registered with canonical "Invariant E checkpoint -- FAIL"
label (echoed at schema_compliance_confirmed), AND Invariant D templates use `[incumbent from CAMPAIGN
OPEN]` binding throughout.

**Hypothesis**: C-19 wires the upstream context (CAMPAIGN OPEN) to Invariant D, making incumbent
binding structural. C-18 extends bidirectional enforcement downstream to the HANDOFF TABLE via
Invariant E. Together they close the architectural enforcement loop: from the very first pre-stage
declaration (CAMPAIGN OPEN) through to the final handoff row, every displacement-relevant structure
is registered, bound, and bidirectionally detectable. Any drift -- either in template wording or
handoff completeness -- is caught from two directions simultaneously.

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

Fill before any role or invariant registration. All subsequent displacement checks
bind structurally to the incumbent declared here. Do not re-establish per stage.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS -- FAILURE LABEL REGISTRY

Standalone block. Appears before Stage 0. All invariants active for full campaign.
Cannot be modified or bypassed at any subsequent stage.

  ID | NAME                        | DECLARATION                                  | FAILURE LABEL
  ---|-----------------------------|----------------------------------------------|---------------------
  D  | INCUMBENT CHECK PHRASING    | Stage 2: "Does [evidence item] support the   | FORMAT ERROR
     | REGISTER                    |   displacement of [incumbent from CAMPAIGN   |
     |                             |   OPEN] by {topic} on [dimension]?           |
     |                             |   [Yes / No / Inconclusive]"                 |
     |                             | Stage 3: "Does [practitioner account] reveal |
     |                             |   a viable transition path from [incumbent   |
     |                             |   from CAMPAIGN OPEN] to {topic} for [use    |
     |                             |   case]? [Yes / No / Inconclusive]"          |
     |                             | Stage 4: "Does [prototype result] make a     |
     |                             |   credible case for displacing [incumbent    |
     |                             |   from CAMPAIGN OPEN] with {topic}?          |
     |                             |   [Yes / No / Pending]"                      |
     |                             | Binding: [incumbent from CAMPAIGN OPEN] =    |
     |                             |   incumbent_name declared above.             |
     |                             | Deviation or literal re-establishment =      |
     |                             |   FORMAT ERROR.                              |
  ---|-----------------------------|----------------------------------------------|---------------------
  A  | ADVERSARIAL REVIEWER TYPE   | adversarial_reviewer_type: [role].           | DUAL-LOCK ERROR
     |                             | Activation: null_tally_final >= 3.            |
  ---|-----------------------------|----------------------------------------------|---------------------
  B  | CONFIDENCE CAP              | confidence_composite -= 2 if >= 3 (hard cap).| DUAL-LOCK ERROR
  ---|-----------------------------|----------------------------------------------|---------------------
  C  | DERIVATION ANNOTATION       | Every handoff field: [derived from: X].      | FORMAT ERROR
  ---|-----------------------------|----------------------------------------------|---------------------
  E  | HANDOFF SCHEMA COMPLIANCE   | All 11 handoff fields present, each with     | Invariant E
     |                             |   [derived from: X] annotation.              | checkpoint -- FAIL
     |                             | schema_compliance_confirmed row echoes        |
     |                             |   "Invariant E checkpoint -- FAIL" verbatim. |
     |                             | Missing or unlabeled field =                  |
     |                             |   Invariant E checkpoint -- FAIL.             |
  ---|-----------------------------|----------------------------------------------|---------------------
  F  | SYNTHESIS FIELD ISOLATION   | hypothesis_verdict, confidence_composite,    | SYNTHESIS
     |                             |   key_risk: each on own line, extractable.   |   FORMAT ERROR

Inline enforcement: Every stage checkpoint echoes the exact FAILURE LABEL registered above.
Bidirectional: registered label + inline echo. Drift in either direction = self-incriminating.

### ROLE OWNERSHIP TABLE

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP
  -------|--------------------------|---------------------------|-------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3

ROLE C (fill now): incumbent_threat_locked: [true when INCUMBENT ANCHOR complete]
ROLE B (fill now):
  scout_artifact:  [{topic}-scout-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if loaded; CAMPAIGN BLOCKED otherwise]
ROLE A (fill now):
  Confirms six invariant rows. Confirms Invariant D uses [incumbent from CAMPAIGN OPEN]
  binding. Confirms Invariant E "Invariant E checkpoint -- FAIL" canonical label.
  invariant_registry_confirmed: [true when all confirmed]

### CE VERDICT OWNERSHIP TABLE

  s2/s3/s4_ce_verdict: null or citation. null_tally_final = count(null) at Stage 4 close.
  Stage 5 reconstructs chain independently. Mismatch = INTEGRITY FAILURE.

### PRE-COMMITTED HANDOFF SCHEMA

11 fields: scout_anchor | incumbent_threat_locked | hypothesis | counter_hypothesis |
s2_ce_verdict | s3_ce_verdict | s4_ce_verdict | null_tally_final |
co_activation_confirmed | incumbent_defense_closed | confidence_composite

---

## STAGE 0 -- GATE S

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | RESULT
  -----|------------------------------|---------|------------------------------------
  1    | incumbent_threat_locked      | ROLE C  | [confirm or BLOCKED: ORDER ERROR]
  2    | gate_s_cleared               | ROLE B  | [confirm or BLOCKED: ORDER ERROR]
  3    | invariant_registry_confirmed | ROLE A  | [confirm or BLOCKED: ORDER ERROR]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Invariant D bound to [incumbent from CAMPAIGN OPEN].
   Invariant E checkpoint -- FAIL registered. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

  source_scout_artifact: [from ROLE B]
  hypothesis:            [falsifiable claim about {topic}]
  counter_hypothesis:    [incumbent best defense]
  gate_s_cleared / invariant_registry_confirmed / incumbent_threat_locked: [true]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked

---

## STAGE 2 -- WEB SEARCH

ENTRY: hypothesis_locked. Invariant D Stage 2 template bound to [incumbent from CAMPAIGN OPEN].

INCUMBENT CHECK TABLE -- Stage 2:

  ITEM | SOURCE | SUMMARY | TEMPLATE ([incumbent from CAMPAIGN OPEN] bound) & VERDICT
  -----|--------|---------|-----------------------------------------------------------
  1    | [src]  | [sum]   | "Does [item] support the displacement of [incumbent from
  2    | [src]  | [sum]   |  CAMPAIGN OPEN] by [topic] on [dim]? [Yes/No/Inconclusive]"
  3+   |        |         |

  Invariant D checkpoint -- FORMAT ERROR if template deviated or incumbent named literally.

  s2_incumbent_check_summary: [N/M/P]
  s2_ce_verdict: [null | citation]
  Displacement read: [one sentence Stage 2 displacement verdict]

Running null tally: [N] null. 2 stages remain.
SCHEMA INTEGRITY: [N]/11 populated.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete

---

## STAGE 3 -- INTERVIEW

ENTRY: websearch_complete. Invariant D Stage 3 template bound to [incumbent from CAMPAIGN OPEN].

INCUMBENT CHECK TABLE -- Stage 3:

  PRACTITIONER | ACCOUNT      | TEMPLATE ([incumbent from CAMPAIGN OPEN] bound) & VERDICT
  -------------|--------------|-----------------------------------------------------------
  [type 1]     | [paraphrase] | "Does [account] reveal a viable transition path from
  [type 2]     | [paraphrase] |  [incumbent from CAMPAIGN OPEN] to [topic] for [use case]?
  [type 3]     | [paraphrase] |  [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if literal re-establishment of incumbent.

  s3_ce_verdict: [null | citation]
  Displacement read: [one sentence Stage 3 transition verdict]

Running null tally: [N] null. 1 remains.
SCHEMA INTEGRITY: [N]/11 populated.
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete

---

## STAGE 4 -- PROTOTYPE

ENTRY: interview_complete. Invariant D Stage 4 template bound to [incumbent from CAMPAIGN OPEN].

  prototype_design: [brief description]
  prototype_result: [what was learned]

INCUMBENT CHECK TABLE -- Stage 4:

  ITEM      | RESULT   | TEMPLATE ([incumbent from CAMPAIGN OPEN] bound) & VERDICT
  ----------|----------|---------------------------------------------------------
  prototype | [result] | "Does [result] make a credible case for displacing [incumbent
            |          |  from CAMPAIGN OPEN] with [topic]? [Yes/No/Pending]"

  Invariant D checkpoint -- FORMAT ERROR if template deviated, verdict missing, or literal.

  s4_displacement_verdict: [Yes / No / Pending]
  s4_ce_verdict: [null | description]
  Displacement read: [one sentence Stage 4 prototype displacement verdict]

  null_tally_final = [N]
  Stage 4 cross-check: "Stage 3 count [M]. Final [N]. Match: [T/F]." Mismatch = INTEGRITY FAILURE.

SCHEMA INTEGRITY: [N]/11 populated.
Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete

---

## STAGE 5 -- SYNTHESIS

ENTRY: prototype_complete. null_tally_final recorded. Invariants D, E active.

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  [from Stage 1] | REFUTED / PARTIALLY REFUTED / OPEN RISK | [cite artifact]
  OPEN RISK: reduce confidence_composite one tier.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction (INTEGRITY FAILURE if mismatch):
  S2=[s2_val] / S3=[s3_val] / S4=[s4_val]
  Reconstructed: [N]
  Stage 4 declared: [M]
  Stage 5 chain confirmation: "S2=[v]+S3=[v]+S4=[v]=[N]. Stage 4=[M]. Match: [T/F]."
  Mismatch = INTEGRITY FAILURE. Record before continuing.

DUAL-LOCK:
  If null_tally_final >= 3:
    Lock 1 (INV A): adversarial_reviewer_type fires. BLOCKED.
    Lock 2 (INV B): confidence_composite -= 2. Hard cap.
    co_activation_confirmed: dual_lock_fired
  Else:
    co_activation_confirmed: not_triggered

### SYNTHESIS DECLARATIONS

Do not embed in prose. Invariant F checkpoint -- SYNTHESIS FORMAT ERROR if in prose.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  confidence_composite:  [final value]
  key_risk:              [residual incumbent strength]

### SYNTHESIS BODY

  evidence_summary: [2-3 sentences. Cite Stage 4 displacement verdict. Reference
                     [incumbent from CAMPAIGN OPEN] by bound name.]

### HANDOFF TABLE

Invariant C: [derived from: X] on every field. FORMAT ERROR if unlabeled.
Invariant E: all 11 fields present. Invariant E checkpoint -- FAIL if any missing or unlabeled.

  FIELD                      | VALUE   | DERIVATION                              | IND. CHAIN
  ---------------------------|---------|-----------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]       | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]         | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]        | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]        | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]        | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]        | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]        | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]    | not through co_act.
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]        | not through inc_def.
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]   | not through co_act.
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]       | capped by INV B
  schema_compliance_confirmed| [true]  | [Invariant E checkpoint -- FAIL if any   | n/a
                             |         |  field unlabeled or missing]            |

STAGE 5 EXIT SIGNAL: synthesis_complete
Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both. Campaign complete.
```

---

## V-05 -- Full Integration: C-18 + C-19 + C-20 + C-05 fix + C-06 fix + C-09 fix

**Variation axis**: All three new v4 criteria combined with explicit fixes for the three persistent
gaps from R3: C-05 (Stage 5 chain reconstruction statement), C-06 (named ROLE B field output),
C-09 (conditional co_activation_confirmed branch with Lock 1/Lock 2 declarations).

**Hypothesis**: C-19 binds Invariant D to CAMPAIGN OPEN (upstream). C-18 extends bidirectional
enforcement to Invariant E (handoff schema downstream). C-20 makes displacement reads portable
in artifact files. The three gap fixes -- Stage 5 chain confirmation, ROLE B named fields, and
explicit dual-lock conditional -- close the remaining essential and recommended gaps from R3.
Together: all 5 essential PASS, all 3 recommended PASS, aspirational coverage above 80.

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

Fill before any role or invariant registration. All displacement checks across Stages 2, 3,
and 4 bind to the incumbent declared here. Do not re-establish the incumbent per stage.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS -- FAILURE LABEL REGISTRY

Standalone block. Appears before Stage 0. All invariants active for full campaign.
Cannot be modified or bypassed at any subsequent stage.

  ID | NAME                        | DECLARATION                                  | FAILURE LABEL
  ---|-----------------------------|----------------------------------------------|---------------------
  D  | INCUMBENT CHECK PHRASING    | Stage 2: "Does [evidence item] support the   | FORMAT ERROR
     | REGISTER                    |   displacement of [incumbent from CAMPAIGN   |
     |                             |   OPEN] by {topic} on [dimension]?           |
     |                             |   [Yes / No / Inconclusive]"                 |
     |                             | Stage 3: "Does [practitioner account] reveal |
     |                             |   a viable transition path from [incumbent   |
     |                             |   from CAMPAIGN OPEN] to {topic} for [use    |
     |                             |   case]? [Yes / No / Inconclusive]"          |
     |                             | Stage 4: "Does [prototype result] make a     |
     |                             |   credible case for displacing [incumbent    |
     |                             |   from CAMPAIGN OPEN] with {topic}?          |
     |                             |   [Yes / No / Pending]"                      |
     |                             | Binding: [incumbent from CAMPAIGN OPEN]      |
     |                             |   resolves to incumbent_name above.          |
     |                             | Template deviation = FORMAT ERROR.           |
     |                             | Naming incumbent as literal string instead   |
     |                             |   of using CAMPAIGN OPEN binding = FORMAT    |
     |                             |   ERROR.                                     |
  ---|-----------------------------|----------------------------------------------|---------------------
  A  | ADVERSARIAL REVIEWER TYPE   | adversarial_reviewer_type: [role most likely | DUAL-LOCK ERROR
     |                             |   to challenge displacement].                 |
     |                             | Activation: null_tally_final >= 3.            |
  ---|-----------------------------|----------------------------------------------|---------------------
  B  | CONFIDENCE CAP              | confidence_composite -= 2 if                  | DUAL-LOCK ERROR
     |                             |   null_tally_final >= 3 (hard cap).           |
     |                             | Cannot be softened or overridden.             |
  ---|-----------------------------|----------------------------------------------|---------------------
  C  | DERIVATION ANNOTATION       | Every handoff field: [derived from: X].      | FORMAT ERROR
     |                             | Unlabeled field = FORMAT ERROR.               |
  ---|-----------------------------|----------------------------------------------|---------------------
  E  | HANDOFF SCHEMA COMPLIANCE   | All 11 handoff fields present, each with     | Invariant E
     |                             |   [derived from: X] annotation.              | checkpoint -- FAIL
     |                             | schema_compliance_confirmed row echoes        |
     |                             |   "Invariant E checkpoint -- FAIL" verbatim. |
     |                             | Missing or unlabeled field =                  |
     |                             |   Invariant E checkpoint -- FAIL.             |
  ---|-----------------------------|----------------------------------------------|---------------------
  F  | SYNTHESIS FIELD ISOLATION   | hypothesis_verdict, confidence_composite,    | SYNTHESIS
     |                             |   key_risk: each on its own line,            |   FORMAT ERROR
     |                             |   extractable by label match.                |
     |                             | Do not embed in prose sentences.             |

ARTIFACT DISPLACEMENT RULE (locked): The websearch, interview, and prototype artifact files
must each contain a labeled "Displacement read:" field in their written content. The write
confirmation for each must explicitly state this field was written to the file with its value.
A Displacement read present only in stage output but not described in the write confirmation
= FORMAT ERROR for that artifact. All three artifacts must carry the field.

Inline enforcement: Every stage checkpoint echoes the exact FAILURE LABEL registered above.
All failure modes (D, A, B, C, E, F) are bidirectionally detectable (registry + inline echo).

### ROLE OWNERSHIP TABLE

Roles execute in sequence C -> B -> A before Stage 0.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP
  -------|--------------------------|---------------------------|-------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3

ROLE C execution (declare all fields by name):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (declare all fields by name -- required output):
  scout_artifact:  [exact path: {topic}-scout-{date}.md or state "[not found: {path searched}]"]
  scout_loaded:    [true if artifact found and readable; false if not found]
  gate_s_cleared:  [true if scout_loaded = true; false triggers CAMPAIGN BLOCKED at Step 2]

ROLE A execution (declare all fields by name):
  Confirms six SESSION INVARIANT rows (D, A, B, C, E, F) registered.
  Confirms Invariant D templates use [incumbent from CAMPAIGN OPEN] binding.
  Confirms Invariant E "Invariant E checkpoint -- FAIL" canonical label is registered.
  Confirms ARTIFACT DISPLACEMENT RULE is registered.
  invariant_registry_confirmed: [true when all confirmed]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Stage 5 ATOMIC DUAL-LOCK reconstructs S2->S3->S4->
null_tally_final chain independently and declares Stage 5 chain confirmation statement
with explicit match verdict. Mismatch = INTEGRITY FAILURE.

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
  confidence_composite       | Stage 5 synthesis (capped by Invariant B)

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator, incumbent_name)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS block complete -- six rows (D, A, B, C, E, F); Invariant D uses
      [incumbent from CAMPAIGN OPEN] binding; Invariant E "Invariant E checkpoint -- FAIL"
      registered; ARTIFACT DISPLACEMENT RULE registered
  [ ] ROLE C executed -- incumbent_threat_locked declared by name
  [ ] ROLE B executed -- scout_artifact, scout_loaded, gate_s_cleared declared by name
  [ ] ROLE A executed -- invariant_registry_confirmed declared by name

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|-----------------------------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED: ORDER ERROR]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED: ORDER ERROR]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED: ORDER ERROR]

  First BLOCKED step halts campaign. Record step, owning role, label ORDER ERROR.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 confirmed. Invariant D bound to [incumbent from
   CAMPAIGN OPEN]. Invariant E checkpoint -- FAIL registered. ARTIFACT DISPLACEMENT RULE active.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path from ROLE B (declared by name)
  [ ] Invariant D [incumbent from CAMPAIGN OPEN] binding confirmed

STAGE 1 BODY:
Load scout artifact. Frame hypothesis grounded in scout signals and INCUMBENT ANCHOR.

  source_scout_artifact:        [path from ROLE B -- copied verbatim, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent best defense -- grounded in ROLE C analysis]
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
  [ ] Invariant D Stage 2 template with [incumbent from CAMPAIGN OPEN] binding active:
      "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN]
       by {topic} on [dimension]? [Yes / No / Inconclusive]"
      Invariant D checkpoint -- FORMAT ERROR if template deviated or incumbent named literally.
  [ ] ARTIFACT DISPLACEMENT RULE active: websearch artifact will include Displacement read

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 ([incumbent from CAMPAIGN OPEN] bound):
Structural origin: ROLE C incumbent_threat_locked (GATE S Step 1).

  ITEM | SOURCE                   | SUMMARY (1 sentence)  | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|----------------------------
  1    | [source]                 | [summary]            | "Does [item 1] support the
  2    | [source]                 | [summary]            |  displacement of [incumbent
  3    | [source]                 | [summary]            |  from CAMPAIGN OPEN] by
  ...  |                          |                      |  [topic] on [dim]?
                                  |                      |  [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if template deviated or incumbent named as literal.

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  Displacement read: [one sentence: does Stage 2 evidence support, challenge, or leave
                      inconclusive the case for displacing [incumbent from CAMPAIGN OPEN]?]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-websearch-{date}.md
  Artifact content includes:
    Displacement read: [copy of Displacement read field above -- written to file]
  Confirm write: "{topic}-websearch-{date}.md written. Artifact includes
    Displacement read: [value]."

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] Invariant D Stage 3 template with [incumbent from CAMPAIGN OPEN] binding active:
      "Does [practitioner account] reveal a viable transition path from [incumbent from
       CAMPAIGN OPEN] to {topic} for [use case]? [Yes / No / Inconclusive]"
      Invariant D checkpoint -- FORMAT ERROR if deviated or incumbent named literally.
  [ ] ARTIFACT DISPLACEMENT RULE active: interview artifact will include Displacement read

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 ([incumbent from CAMPAIGN OPEN] bound):

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT
  -----------------|------------------------------|----------------------------
  [type 1]         | [quote or paraphrase]        | "Does [account] reveal a viable
  [type 2]         | [quote or paraphrase]        |  transition path from [incumbent
  [type 3]         | [quote or paraphrase]        |  from CAMPAIGN OPEN] to [topic]
  ...              |                              |  for [use case]?
                   |                              |  [Yes/No/Inconclusive]"

  Invariant D checkpoint -- FORMAT ERROR if incumbent re-established as literal string.

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  Displacement read: [one sentence: does Stage 3 evidence support, challenge, or leave
                      inconclusive the transition from [incumbent from CAMPAIGN OPEN]?]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-interview-{date}.md
  Artifact content includes:
    Displacement read: [copy of Displacement read field above -- written to file]
  Confirm write: "{topic}-interview-{date}.md written. Artifact includes
    Displacement read: [value]."

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] Invariant D Stage 4 template with [incumbent from CAMPAIGN OPEN] binding active:
      "Does [prototype result] make a credible case for displacing [incumbent from
       CAMPAIGN OPEN] with {topic}? [Yes / No / Pending]"
      Invariant D checkpoint -- FORMAT ERROR if deviated, verdict omitted, or literal name.
  [ ] ARTIFACT DISPLACEMENT RULE active: prototype artifact will include Displacement read

STAGE 4 BODY:

  prototype_design:   [brief description]
  prototype_result:   [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 ([incumbent from CAMPAIGN OPEN] bound):

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-----------------------------
  prototype  | [prototype_result]            | "Does [prototype result] make a
             |                               |  credible case for displacing
             |                               |  [incumbent from CAMPAIGN OPEN]
             |                               |  with [topic]? [Yes/No/Pending]"

  Invariant D checkpoint -- FORMAT ERROR if template deviated, verdict missing, or
  incumbent re-established as literal string.

  s4_displacement_verdict: [Yes / No / Pending]   <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]
  Displacement read: [one sentence: does the prototype make a credible case for displacing
                      [incumbent from CAMPAIGN OPEN]? Cite s4_displacement_verdict.]

Final null tally:
  null_tally_final = [N]
  Stage 4 cross-check: "Running count from Stage 3 was [M]. Final is [N].
  Match: [true / false]." Mismatch = INTEGRITY FAILURE.

SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-prototype-{date}.md
  Artifact content includes:
    Displacement read: [copy of Displacement read field above -- written to file]
  Confirm write: "{topic}-prototype-{date}.md written. Artifact includes
    Displacement read: [value]."

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict = [value]. null_tally_final = [N].
   Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All three evidence artifacts confirmed written with Displacement read fields
  [ ] All six SESSION INVARIANT rows (D, A, B, C, E, F) active
  [ ] Invariant E "Invariant E checkpoint -- FAIL" active for HANDOFF TABLE

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS     | VERDICT                                   | EVIDENCE
  -----------------------|-------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK   | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

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
  null_tally_final confirmed: [N]

DUAL-LOCK EVALUATION (DUAL-LOCK ERROR if conditions met but locks not declared):
  null_tally_final = [N]
  If null_tally_final >= 3:
    co_activation_confirmed: dual_lock_fired
    Lock 1 (SESSION INVARIANT A): adversarial_reviewer_type = [registered type]. Review fires.
    Lock 2 (SESSION INVARIANT B): confidence_composite before cap = [X].
      confidence_composite after cap = [X-2]. Hard cap applied. Cannot be softened.
    Note: "DUAL-LOCK FIRED. Both locks active per campaign registration."
  Else (null_tally_final < 3):
    co_activation_confirmed: not_triggered

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.
Invariant F checkpoint -- SYNTHESIS FORMAT ERROR if any field appears only within prose.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  confidence_composite:  [final numeric value after all reductions]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### SYNTHESIS BODY

  evidence_summary: [2-3 sentences integrating Stages 2, 3, 4. Must cite the cumulative
                     Displacement read from Stage 4 artifact. Must state explicitly:
                     "Stage 4 displacement verdict: [Yes/No/Pending]." Reference
                     [incumbent from CAMPAIGN OPEN] by bound name -- no re-establishment.]
  incumbent_defense_closed: [true if no open incumbent defense remains; false if CE unresolved]

### HANDOFF TABLE

SESSION INVARIANT C enforced: all fields carry [derived from: X]. Unlabeled = FORMAT ERROR.
SESSION INVARIANT E enforced: all 11 fields present.
Invariant E checkpoint -- FAIL if any field is unlabeled, missing, or has no derivation annotation.

  FIELD                      | VALUE   | DERIVATION                             | IND. CHAIN
  ---------------------------|---------|----------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]      | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]        | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]       | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]       | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]       | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]       | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]       | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]   | not through
                             |         |                                        |   co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]       | not through
                             |         |                                        |   incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]  | not through
                             |         |                                        |   co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]      | capped by INV B
  schema_compliance_confirmed| [true]  | [Invariant E checkpoint -- FAIL if any  | n/a
                             |         |  field unlabeled or missing]           |

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```
