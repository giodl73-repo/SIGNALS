---
skill: quest-variate
skill_target: prove-topic
round: R6
date: 2026-03-16
rubric: prove-topic-rubric-v6-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [role_a_binding_confirmation, per_artifact_displacement_read, binding_note_subsection_precision]
  combined: [V-04 (c24+c26), V-05 (c24+c25+c26 all-axis)]
r5_context: >
  R5 explored inertia framing, all-table format, conversational register, role-sequence+lifecycle,
  and inertia+exit-signal+two-write combinations. The installed SKILL.md incorporates CAMPAIGN OPEN,
  INCUMBENT ANCHOR sub-section (C-21), SESSION INVARIANTS TABLE (C-12), ROLE OWNERSHIP TABLE (C-06),
  null tally chain (C-05), pre-committed handoff schema (C-07), and all six EXIT SIGNALs (C-01).
  R6 targets three new v6 criteria: C-24 (ROLE A reads INCUMBENT ANCHOR before Stage 0), C-25
  (Stage 5 cites all three artifact Displacement reads), C-26 (Invariant D binding note names
  CAMPAIGN OPEN INCUMBENT ANCHOR sub-section). C-22 (binding note floor) and C-16/C-20
  (Displacement read infrastructure) are added as necessary floors for C-24/C-26 and C-25.
---

## V-01 -- Axis: ROLE A Binding Confirmation (C-24)

**Variation axis**: ROLE A initialization only. ROLE A's execution block is extended with an
explicit incumbent binding confirmation step: ROLE A reads CAMPAIGN OPEN INCUMBENT ANCHOR
sub-section and records the resolved incumbent_name value before Stage 0 fires. Also adds
C-22 floor: Invariant D binding note with literal-string failure label. All other structure
unchanged from the installed golden prompt.

**Hypothesis**: Adding a ROLE A binding confirmation step -- analogous to schema_compliance_confirmed
(C-18) for Invariant E -- closes the activation gap between INCUMBENT ANCHOR declaration (C-21)
and Invariant D enforcement (C-22). The binding confirmation must appear before Stage 0 gate_open,
making the pre-stage binding activation explicit and auditable.

---

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

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

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of {status_quo_comparator} by {topic} on [dimension]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator} to
       |                           |   {topic} for [use case]? [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending]"
       |                           | Binding: [incumbent from CAMPAIGN OPEN] resolves to
       |                           |   incumbent_name. Naming as literal string = FORMAT ERROR.
       |                           | Enforcement: Template deviation = FORMAT ERROR.
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | Cannot be modified or bypassed at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | Cannot be softened or overridden at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | Cannot be modified or bypassed at synthesis.

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, incumbent_strength,
                             incumbent_vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Step 1 -- INCUMBENT ANCHOR binding read:
    Read CAMPAIGN OPEN INCUMBENT ANCHOR sub-section (above).
    Record resolved binding:
      incumbent_anchor_read: [incumbent_name value from CAMPAIGN OPEN INCUMBENT ANCHOR]
    Confirm Invariant D binding is active against this resolved value.
    This record must appear before Stage 0 gate_open EXIT SIGNAL.
    Stating the incumbent as a literal string without tracing to CAMPAIGN OPEN
    INCUMBENT ANCHOR sub-section = FAIL.
  Step 2 -- Invariant registry confirmation:
    Confirms all four SESSION INVARIANT TABLE rows filled and active.
    Confirms Invariant D binding note present and matches incumbent_anchor_read.
  invariant_registry_confirmed: [true when Step 1 and Step 2 both confirmed]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis                           | n/a
  hypothesis                 | Stage 1 artifact                          | n/a
  counter_hypothesis         | Stage 1 artifact                          | n/a
  s2_ce_verdict              | Stage 2 artifact                          | n/a
  s3_ce_verdict              | Stage 3 artifact                          | n/a
  s4_ce_verdict              | Stage 4 artifact                          | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by B

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete -- all four rows filled, SESSION INVARIANT D
      displacement-question templates registered
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- incumbent_anchor_read confirmed, invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. ROLE A incumbent_anchor_read
   active. SESSION INVARIANT D active. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered (confirmed by ROLE A at GATE S Step 3)

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense -- grounded in ROLE C analysis]
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
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from table row D):
      "Does [evidence item] support the displacement of {status_quo_comparator} by
       {topic} on [dimension]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D, Stage 2 template applied verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1).

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|------------------------------
  1    | [source]                 | [summary]            | "Does [item 1] support
  2    | [source]                 | [summary]            |  displacement of [comparator]
  3    | [source]                 | [summary]            |  by [topic] on [dim]? [verdict]"
  add  |                          |                      | (fill each row verbatim)

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim from table row D):
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D, Stage 3 template applied verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1).

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT
  -----------------|------------------------------|------------------------------
  [type 1]         | [quote or paraphrase]        | "Does [account 1] reveal a viable
  [type 2]         | [quote or paraphrase]        |  transition path from [comparator]
  [type 3]         | [quote or paraphrase]        |  to [topic] for [use case]? [verdict]"
  add rows          |                              | (fill each row verbatim)

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim from table row D):
      "Does [prototype result] make a credible case for displacing {status_quo_comparator}
       with {topic}? [Yes / No / Pending]"
      Displacement verdict required. Omission = FORMAT ERROR.

STAGE 4 BODY:
Design and assess minimal prototype.

  prototype_design:   [brief description]
  prototype_result:   [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D, Stage 4 template applied verbatim):

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------------------------
  prototype  | [prototype_result]            | "Does [prototype result] make a
             |                               |  credible case for displacing
             |                               |  [comparator] with [topic]?
             |                               |  [Yes / No / Pending]"

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
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
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]
  [add rows as needed]   |                                          |

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch -- record if mismatch before continuing]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4 -- with explicit
                           incumbent displacement verdict from Stage 4 check]
  confidence_composite:  [final value]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]| does not pass through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | does not pass through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | does not pass through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.

---

## V-02 -- Axis: Per-Artifact Displacement Read Fields (C-25)

**Variation axis**: Per-artifact Displacement read fields only. Each of Stages 2, 3, and 4
adds a labeled "Displacement read:" synthesis field to the stage body, explicitly noted as
part of the written artifact's content. Stage 5 evidence_summary is required to cite all
three artifact Displacement read values by name and value. All other structure unchanged.

**Hypothesis**: Adding a "Displacement read:" synthesis field to each evidence artifact
(websearch, interview, prototype) makes displacement evidence portable outside stage output.
When Stage 5 synthesis must cite all three artifact values explicitly, it closes the chain
from raw stage output through artifact storage to final synthesis verdict -- making the
displacement argument auditable end-to-end across all three evidence sources.

---

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

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

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of {status_quo_comparator} by {topic} on [dimension]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator} to
       |                           |   {topic} for [use case]? [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending]"
       |                           | Enforcement: Template deviation = FORMAT ERROR.
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | Cannot be modified or bypassed at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | Cannot be softened or overridden at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | Cannot be modified or bypassed at synthesis.

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, incumbent_strength,
                             incumbent_vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all four SESSION INVARIANT TABLE rows filled and active.
  invariant_registry_confirmed: [true when all four invariants in table are registered]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis                           | n/a
  hypothesis                 | Stage 1 artifact                          | n/a
  counter_hypothesis         | Stage 1 artifact                          | n/a
  s2_ce_verdict              | Stage 2 artifact                          | n/a
  s3_ce_verdict              | Stage 3 artifact                          | n/a
  s4_ce_verdict              | Stage 4 artifact                          | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by B

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete -- all four rows filled, SESSION INVARIANT D
      displacement-question templates registered
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered (confirmed by ROLE A at GATE S Step 3)

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense -- grounded in ROLE C analysis]
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
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from table row D):
      "Does [evidence item] support the displacement of {status_quo_comparator} by
       {topic} on [dimension]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D, Stage 2 template applied verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1).

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|------------------------------
  1    | [source]                 | [summary]            | "Does [item 1] support
  2    | [source]                 | [summary]            |  displacement of [comparator]
  3    | [source]                 | [summary]            |  by [topic] on [dim]? [verdict]"
  add  |                          |                      | (fill each row verbatim)

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]

Displacement read: [one sentence: does Stage 2 web evidence support, challenge, or leave
  inconclusive the case for displacing the incumbent? State verdict explicitly.]
Note: Include labeled "Displacement read:" field in the {topic}-websearch-{date}.md artifact
  body. Field present only in stage output but absent from artifact content = FAIL.

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-websearch-{date}.md (include Displacement read field). Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim from table row D):
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D, Stage 3 template applied verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1).

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT
  -----------------|------------------------------|------------------------------
  [type 1]         | [quote or paraphrase]        | "Does [account 1] reveal a viable
  [type 2]         | [quote or paraphrase]        |  transition path from [comparator]
  [type 3]         | [quote or paraphrase]        |  to [topic] for [use case]? [verdict]"
  add rows          |                              | (fill each row verbatim)

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]

Displacement read: [one sentence: does Stage 3 practitioner evidence support, challenge,
  or leave inconclusive the case for displacing the incumbent? State verdict explicitly.]
Note: Include labeled "Displacement read:" field in {topic}-interview-{date}.md artifact body.
  Field absent from artifact content = FAIL.

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-interview-{date}.md (include Displacement read field). Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim from table row D):
      "Does [prototype result] make a credible case for displacing {status_quo_comparator}
       with {topic}? [Yes / No / Pending]"
      Displacement verdict required. Omission = FORMAT ERROR.

STAGE 4 BODY:
Design and assess minimal prototype.

  prototype_design:   [brief description]
  prototype_result:   [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D, Stage 4 template applied verbatim):

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------------------------
  prototype  | [prototype_result]            | "Does [prototype result] make a
             |                               |  credible case for displacing
             |                               |  [comparator] with [topic]?
             |                               |  [Yes / No / Pending]"

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]

Displacement read: [same verdict as s4_displacement_verdict, stated as one sentence.
  Value must match s4_displacement_verdict exactly.]
Note: Include labeled "Displacement read:" field in {topic}-prototype-{date}.md artifact body.
  All three stage artifacts (websearch, interview, prototype) must carry this field.
  Field absent from any artifact = FAIL.

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-prototype-{date}.md (include Displacement read field). Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict = [value]. null_tally_final = [N].
   Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch -- record if mismatch before continuing]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4. Must cite all three
                           artifact Displacement read values by source artifact and value:
                             websearch Displacement read: [value from {topic}-websearch-{date}.md]
                             interview Displacement read: [value from {topic}-interview-{date}.md]
                             prototype Displacement read: [value from {topic}-prototype-{date}.md]
                           Plus explicit Stage 4 displacement verdict from s4_displacement_verdict.
                           Citing only stage-output verdict without artifact Displacement read
                           values = FAIL. Citing fewer than all three artifacts = FAIL.]
  confidence_composite:  [final value]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]| does not pass through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | does not pass through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | does not pass through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.

---

## V-03 -- Axis: Binding Note Sub-Section Precision (C-26)

**Variation axis**: Invariant D binding note only. SESSION INVARIANTS TABLE Invariant D is
extended with: (1) templates that reference `[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]`
as a bound variable rather than literal `{status_quo_comparator}`, (2) a binding resolution
note that names the INCUMBENT ANCHOR sub-section specifically (not the CAMPAIGN OPEN parent
block), and (3) a failure label for literal-string use. This cross-wires the SESSION INVARIANTS
chain to the CAMPAIGN OPEN chain at sub-section precision. All other structure unchanged.

**Hypothesis**: When Invariant D templates use a sub-section-scoped binding reference, the
structural connection between SESSION INVARIANTS and CAMPAIGN OPEN becomes explicit. The binding
note names CAMPAIGN OPEN INCUMBENT ANCHOR specifically, so any divergence between what the
template references and what CAMPAIGN OPEN declares is immediately self-incriminating as a
FORMAT ERROR through the two-layer enforcement architecture.

---

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

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

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]
       |                           |   by {topic} on [dimension]? [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from [incumbent from CAMPAIGN OPEN
       |                           |   INCUMBENT ANCHOR] to {topic} for [use case]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing [incumbent from CAMPAIGN OPEN
       |                           |   INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"
       |                           | Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]
       |                           |   resolves to incumbent_name declared in CAMPAIGN OPEN
       |                           |   INCUMBENT ANCHOR sub-section (sub-section, not parent
       |                           |   block). Naming incumbent as literal string in templates
       |                           |   = FORMAT ERROR. Re-establishing per stage = FORMAT ERROR.
       |                           | Enforcement: Template deviation = FORMAT ERROR.
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | Cannot be modified or bypassed at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | Cannot be softened or overridden at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | Cannot be modified or bypassed at synthesis.

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, incumbent_strength,
                             incumbent_vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all four SESSION INVARIANT TABLE rows filled and active.
  Confirms Invariant D templates reference [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]
  (not a literal string).
  invariant_registry_confirmed: [true when all four invariants in table are registered]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis                           | n/a
  hypothesis                 | Stage 1 artifact                          | n/a
  counter_hypothesis         | Stage 1 artifact                          | n/a
  s2_ce_verdict              | Stage 2 artifact                          | n/a
  s3_ce_verdict              | Stage 3 artifact                          | n/a
  s4_ce_verdict              | Stage 4 artifact                          | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by B

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete -- all four rows filled. Invariant D binding note
      names CAMPAIGN OPEN INCUMBENT ANCHOR sub-section as resolution source.
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- invariant_registry_confirmed = true (binding reference confirmed)

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active
   with CAMPAIGN OPEN INCUMBENT ANCHOR sub-section binding. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered with CAMPAIGN OPEN INCUMBENT ANCHOR binding

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense -- grounded in ROLE C analysis]
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
  [ ] SESSION INVARIANT D Stage 2 template active with CAMPAIGN OPEN INCUMBENT ANCHOR binding:
      "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN
       INCUMBENT ANCHOR] by {topic} on [dimension]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR. Literal string = FORMAT ERROR.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D, Stage 2 template applied verbatim):
Apply template using CAMPAIGN OPEN INCUMBENT ANCHOR binding. Structural origin: ROLE C.

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|------------------------------
  1    | [source]                 | [summary]            | "Does [item 1] support
  2    | [source]                 | [summary]            |  displacement of [incumbent
  3    | [source]                 | [summary]            |  from CAMPAIGN OPEN INCUMBENT
  add  |                          |                      |  ANCHOR] by [topic]? [verdict]"

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active with CAMPAIGN OPEN INCUMBENT ANCHOR binding:
      "Does [practitioner account] reveal a viable transition path from [incumbent from
       CAMPAIGN OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D, Stage 3 template applied verbatim):
Apply template using CAMPAIGN OPEN INCUMBENT ANCHOR binding. Structural origin: ROLE C.

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT
  -----------------|------------------------------|------------------------------
  [type 1]         | [quote or paraphrase]        | "Does [account 1] reveal a viable
  [type 2]         | [quote or paraphrase]        |  transition path from [incumbent
  [type 3]         | [quote or paraphrase]        |  from CAMPAIGN OPEN INCUMBENT
  add rows          |                              |  ANCHOR] to [topic]? [verdict]"

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active with CAMPAIGN OPEN INCUMBENT ANCHOR binding:
      "Does [prototype result] make a credible case for displacing [incumbent from CAMPAIGN
       OPEN INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"
      Displacement verdict required. Omission = FORMAT ERROR. Literal string = FORMAT ERROR.

STAGE 4 BODY:
Design and assess minimal prototype.

  prototype_design:   [brief description]
  prototype_result:   [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D, Stage 4 template applied verbatim):
Apply template using CAMPAIGN OPEN INCUMBENT ANCHOR binding. Structural origin: ROLE C.

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------------------------
  prototype  | [prototype_result]            | "Does [prototype result] make a
             |                               |  credible case for displacing
             |                               |  [incumbent from CAMPAIGN OPEN
             |                               |  INCUMBENT ANCHOR] with [topic]?
             |                               |  [Yes / No / Pending]"

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
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
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch -- record if mismatch before continuing]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4 -- with explicit
                           incumbent displacement verdict from Stage 4 check]
  confidence_composite:  [final value]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]| does not pass through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | does not pass through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | does not pass through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.

---

## V-04 -- Combined: C-24 + C-26 (ROLE A Binding Confirmation + Sub-Section Precision)

**Variation axes**: ROLE A binding confirmation (C-24) combined with Invariant D sub-section
precision (C-26). ROLE A explicitly reads CAMPAIGN OPEN INCUMBENT ANCHOR sub-section by name
and records the resolved binding before Stage 0 fires -- tracing to the sub-section, not the
parent block. Invariant D templates use `[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]` binding
references, and the binding note names the INCUMBENT ANCHOR sub-section as the canonical
resolution source. This creates the cross-chain connection: SESSION INVARIANTS chain wired to
CAMPAIGN OPEN chain at sub-section precision, confirmed mechanically by ROLE A before Stage 0.

**Hypothesis**: When ROLE A reads CAMPAIGN OPEN INCUMBENT ANCHOR sub-section by name and
Invariant D's binding note cross-references the same sub-section, the binding is simultaneously
declared (C-21), registered with failure label at sub-section precision (C-26), and mechanically
activated (C-24). ROLE A's pre-stage record traces to the sub-section specifically, making it
impossible to satisfy C-24 with a parent-block reference alone.

---

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.
Do not re-establish the incumbent per stage. Carry forward from this sub-section only.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]
       |                           |   by {topic} on [dimension]? [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from [incumbent from CAMPAIGN OPEN
       |                           |   INCUMBENT ANCHOR] to {topic} for [use case]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing [incumbent from CAMPAIGN OPEN
       |                           |   INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"
       |                           | Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]
       |                           |   resolves to incumbent_name in CAMPAIGN OPEN INCUMBENT
       |                           |   ANCHOR sub-section (the named sub-section, not the
       |                           |   CAMPAIGN OPEN parent block). Naming as literal string
       |                           |   = FORMAT ERROR. Re-establishing per stage = FORMAT ERROR.
       |                           | Enforcement: Template deviation = FORMAT ERROR.
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | Cannot be modified or bypassed at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | Cannot be softened or overridden at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | Cannot be modified or bypassed at synthesis.

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, incumbent_strength,
                             incumbent_vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Step 1 -- INCUMBENT ANCHOR binding read:
    Read CAMPAIGN OPEN INCUMBENT ANCHOR sub-section (the named sub-section above --
    not the CAMPAIGN OPEN parent block).
    Record resolved binding:
      incumbent_anchor_read: [incumbent_name from CAMPAIGN OPEN INCUMBENT ANCHOR sub-section]
    Tracing to CAMPAIGN OPEN parent block without naming INCUMBENT ANCHOR sub-section = FAIL.
    Stating incumbent as literal string without sub-section trace = FAIL.
    This record must appear before Stage 0 gate_open EXIT SIGNAL.
  Step 2 -- Invariant registry confirmation:
    Confirms all four SESSION INVARIANT TABLE rows filled and active.
    Confirms Invariant D binding note names CAMPAIGN OPEN INCUMBENT ANCHOR sub-section
    (not CAMPAIGN OPEN parent block).
    Confirms incumbent_anchor_read matches Invariant D binding note resolution value.
  invariant_registry_confirmed: [true when Step 1 and Step 2 both confirmed]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis                           | n/a
  hypothesis                 | Stage 1 artifact                          | n/a
  counter_hypothesis         | Stage 1 artifact                          | n/a
  s2_ce_verdict              | Stage 2 artifact                          | n/a
  s3_ce_verdict              | Stage 3 artifact                          | n/a
  s4_ce_verdict              | Stage 4 artifact                          | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by B

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR sub-section filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete -- Invariant D binding note names CAMPAIGN OPEN
      INCUMBENT ANCHOR sub-section as resolution source
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- incumbent_anchor_read confirmed (traced to INCUMBENT ANCHOR
      sub-section), invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. ROLE A incumbent_anchor_read
   active (CAMPAIGN OPEN INCUMBENT ANCHOR sub-section). SESSION INVARIANT D active with
   sub-section-scoped binding. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered with CAMPAIGN OPEN INCUMBENT ANCHOR binding
  [ ] ROLE A incumbent_anchor_read confirmed

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense -- grounded in ROLE C analysis]
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
  [ ] SESSION INVARIANT D Stage 2 template active with CAMPAIGN OPEN INCUMBENT ANCHOR binding:
      "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN
       INCUMBENT ANCHOR] by {topic} on [dimension]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR. Literal string = FORMAT ERROR.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D, Stage 2 template applied verbatim):

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|------------------------------
  1    | [source]                 | [summary]            | [apply verbatim -- use
  2    | [source]                 | [summary]            |  CAMPAIGN OPEN INCUMBENT
  3    | [source]                 | [summary]            |  ANCHOR binding reference]
  add  |                          |                      |

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active with CAMPAIGN OPEN INCUMBENT ANCHOR binding:
      "Does [practitioner account] reveal a viable transition path from [incumbent from
       CAMPAIGN OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D, Stage 3 template applied verbatim):

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT
  -----------------|------------------------------|------------------------------
  [type 1]         | [quote or paraphrase]        | [apply verbatim -- use
  [type 2]         | [quote or paraphrase]        |  CAMPAIGN OPEN INCUMBENT
  [type 3]         | [quote or paraphrase]        |  ANCHOR binding reference]
  add rows          |                              |

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active with CAMPAIGN OPEN INCUMBENT ANCHOR binding:
      "Does [prototype result] make a credible case for displacing [incumbent from CAMPAIGN
       OPEN INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"
      Displacement verdict required. Omission = FORMAT ERROR. Literal string = FORMAT ERROR.

STAGE 4 BODY:
Design and assess minimal prototype.

  prototype_design:   [brief description]
  prototype_result:   [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D, Stage 4 template applied verbatim):

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------------------------
  prototype  | [prototype_result]            | [apply verbatim -- use
             |                               |  CAMPAIGN OPEN INCUMBENT
             |                               |  ANCHOR binding reference]

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
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
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch -- record if mismatch before continuing]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4 -- with explicit
                           incumbent displacement verdict from Stage 4 check]
  confidence_composite:  [final value]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]| does not pass through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | does not pass through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | does not pass through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.

---

## V-05 -- All-Axis: C-24 + C-25 + C-26 (Full Integration)

**Variation axes**: All three new v6 criteria combined. (1) C-26: Invariant D binding note
names CAMPAIGN OPEN INCUMBENT ANCHOR sub-section as canonical resolution source, with failure
label. (2) C-24: ROLE A reads CAMPAIGN OPEN INCUMBENT ANCHOR sub-section by name and records
the resolved binding before Stage 0 fires. (3) C-25: Each of Stages 2, 3, 4 writes a labeled
"Displacement read:" field into its artifact body; Stage 5 evidence_summary cites all three.

**Hypothesis**: When all three chains are active simultaneously -- Invariant D binding
cross-wired to INCUMBENT ANCHOR sub-section (C-26), ROLE A pre-stage activation confirmation
(C-24), and per-artifact Displacement read fields consumed by Stage 5 synthesis (C-25) -- every
v6 criterion is satisfied architecturally. The SESSION INVARIANTS chain and CAMPAIGN OPEN chain
connect at sub-section precision; binding is mechanically activated before Stage 0; displacement
evidence is traceable through artifact storage to synthesis across all three evidence artifacts.

---

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.
Do not re-establish the incumbent per stage. Carry forward from this sub-section only.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]
       |                           |   by {topic} on [dimension]? [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from [incumbent from CAMPAIGN OPEN
       |                           |   INCUMBENT ANCHOR] to {topic} for [use case]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing [incumbent from CAMPAIGN OPEN
       |                           |   INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"
       |                           | Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]
       |                           |   resolves to incumbent_name declared in CAMPAIGN OPEN
       |                           |   INCUMBENT ANCHOR sub-section (sub-section, not parent
       |                           |   block). Naming as literal string = FORMAT ERROR.
       |                           |   Re-establishing per stage = FORMAT ERROR.
       |                           | Enforcement: Template deviation = FORMAT ERROR.
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | Cannot be modified or bypassed at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | Cannot be softened or overridden at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | Cannot be modified or bypassed at synthesis.

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, incumbent_strength,
                             incumbent_vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Step 1 -- INCUMBENT ANCHOR binding read:
    Read CAMPAIGN OPEN INCUMBENT ANCHOR sub-section (the named sub-section above).
    Record resolved binding:
      incumbent_anchor_read: [incumbent_name from CAMPAIGN OPEN INCUMBENT ANCHOR sub-section]
    Tracing to CAMPAIGN OPEN parent block without naming INCUMBENT ANCHOR sub-section = FAIL.
    Stating incumbent as literal string = FAIL.
    This record must appear before Stage 0 gate_open EXIT SIGNAL.
  Step 2 -- Invariant registry and displacement read confirmation:
    Confirms all four SESSION INVARIANT TABLE rows filled and active.
    Confirms Invariant D binding note names CAMPAIGN OPEN INCUMBENT ANCHOR sub-section
    (not CAMPAIGN OPEN parent block).
    Confirms incumbent_anchor_read matches Invariant D binding note resolution value.
    Confirms Stages 2, 3, 4 are each committed to write "Displacement read:" field
    to their respective artifact bodies.
  invariant_registry_confirmed: [true when Step 1 and Step 2 both confirmed]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis                           | n/a
  hypothesis                 | Stage 1 artifact                          | n/a
  counter_hypothesis         | Stage 1 artifact                          | n/a
  s2_ce_verdict              | Stage 2 artifact                          | n/a
  s3_ce_verdict              | Stage 3 artifact                          | n/a
  s4_ce_verdict              | Stage 4 artifact                          | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by B

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR sub-section filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete -- Invariant D binding note names CAMPAIGN OPEN
      INCUMBENT ANCHOR sub-section as resolution source
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- incumbent_anchor_read confirmed (traces to INCUMBENT ANCHOR
      sub-section), displacement read commitment confirmed, invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. ROLE A incumbent_anchor_read
   active (traced to CAMPAIGN OPEN INCUMBENT ANCHOR sub-section). SESSION INVARIANT D
   active with sub-section-scoped binding. Displacement read commitment active for
   Stages 2, 3, 4. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered with CAMPAIGN OPEN INCUMBENT ANCHOR binding
  [ ] ROLE A incumbent_anchor_read confirmed

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense -- grounded in ROLE C analysis]
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
  [ ] SESSION INVARIANT D Stage 2 template active with CAMPAIGN OPEN INCUMBENT ANCHOR binding:
      "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN
       INCUMBENT ANCHOR] by {topic} on [dimension]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR. Literal string = FORMAT ERROR.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D, Stage 2 template applied verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1).

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|------------------------------
  1    | [source]                 | [summary]            | [apply verbatim template with
  2    | [source]                 | [summary]            |  CAMPAIGN OPEN INCUMBENT
  3    | [source]                 | [summary]            |  ANCHOR binding reference]
  add  |                          |                      |

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]

Displacement read: [one sentence: does Stage 2 web evidence support, challenge, or leave
  inconclusive the case for displacing the incumbent? State verdict explicitly.]
Note: Write labeled "Displacement read:" field into {topic}-websearch-{date}.md artifact body.
  Field present only in stage output but absent from artifact = FAIL for C-25.

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-websearch-{date}.md (include Displacement read field). Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active with CAMPAIGN OPEN INCUMBENT ANCHOR binding:
      "Does [practitioner account] reveal a viable transition path from [incumbent from
       CAMPAIGN OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D, Stage 3 template applied verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1).

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT
  -----------------|------------------------------|------------------------------
  [type 1]         | [quote or paraphrase]        | [apply verbatim template with
  [type 2]         | [quote or paraphrase]        |  CAMPAIGN OPEN INCUMBENT
  [type 3]         | [quote or paraphrase]        |  ANCHOR binding reference]
  add rows          |                              |

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]

Displacement read: [one sentence: does Stage 3 practitioner evidence support, challenge,
  or leave inconclusive the case for displacing the incumbent? State verdict explicitly.]
Note: Write labeled "Displacement read:" field into {topic}-interview-{date}.md artifact body.
  Field absent from artifact = FAIL for C-25.

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-interview-{date}.md (include Displacement read field). Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active with CAMPAIGN OPEN INCUMBENT ANCHOR binding:
      "Does [prototype result] make a credible case for displacing [incumbent from CAMPAIGN
       OPEN INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"
      Displacement verdict required. Omission = FORMAT ERROR. Literal string = FORMAT ERROR.

STAGE 4 BODY:
Design and assess minimal prototype.

  prototype_design:   [brief description]
  prototype_result:   [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D, Stage 4 template applied verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1).

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------------------------
  prototype  | [prototype_result]            | [apply verbatim template with
             |                               |  CAMPAIGN OPEN INCUMBENT
             |                               |  ANCHOR binding reference]

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]

Displacement read: [same verdict as s4_displacement_verdict, stated as one sentence.
  Value must match s4_displacement_verdict exactly.]
Note: Write labeled "Displacement read:" field into {topic}-prototype-{date}.md artifact body.
  All three stage artifacts (websearch, interview, prototype) must carry this field.
  Any absent = FAIL for C-25.

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 handoff fields populated -- 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-prototype-{date}.md (include Displacement read field). Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict = [value]. null_tally_final = [N].
   Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active
  [ ] All three artifact Displacement read fields confirmed written
      (websearch, interview, prototype) -- Stage 5 will consume all three

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch -- record if mismatch before continuing]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4. Must cite all three
                           artifact Displacement read values by source artifact and value:
                             websearch Displacement read: [value from {topic}-websearch-{date}.md]
                             interview Displacement read: [value from {topic}-interview-{date}.md]
                             prototype Displacement read: [value from {topic}-prototype-{date}.md]
                           Plus explicit Stage 4 displacement verdict from s4_displacement_verdict.
                           Citing only stage-output verdict without artifact Displacement reads
                           = FAIL. Citing fewer than all three artifact reads = FAIL.]
  confidence_composite:  [final value]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]| does not pass through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | does not pass through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | does not pass through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   All three artifact Displacement reads cited in evidence_summary."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
