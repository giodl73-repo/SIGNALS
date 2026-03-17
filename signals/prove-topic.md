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
       |                           | Enforcement: Template deviation = format error.
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
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through
                             |                                           |   co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through
                             |                                           |   incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through
                             |                                           |   co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by B

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete — all four rows filled, SESSION INVARIANT D
      displacement-question templates registered
  [ ] ROLE C executed — incumbent_threat_locked = true
  [ ] ROLE B executed — scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed — invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered (confirmed by ROLE A at GATE S Step 3)

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  gate_s_cleared:               [true — from GATE S Step 2]
  invariant_registry_confirmed: [true — from GATE S Step 3]
  incumbent_threat_locked:      [true — from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from table row D):
      "Does [evidence item] support the displacement of {status_quo_comparator} by
       {topic} on [dimension]? [Yes / No / Inconclusive]"
      Template deviation = format error.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE — Stage 2 (SESSION INVARIANT D, Stage 2 template applied verbatim):
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
SCHEMA INTEGRITY: [N]/11 handoff fields populated — 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete — s2_ce_verdict = [value]. Tally: [N]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value — not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim from table row D):
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
      Template deviation = format error.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3 (SESSION INVARIANT D, Stage 3 template applied verbatim):
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
SCHEMA INTEGRITY: [N]/11 handoff fields populated — 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete — s3_ce_verdict = [value]. Tally: [N]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value — not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim from table row D):
      "Does [prototype result] make a credible case for displacing {status_quo_comparator}
       with {topic}? [Yes / No / Pending]"
      Displacement verdict (Yes / No / Pending) required. Omission = format error.
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 4 BODY:
Design and assess minimal prototype.

  prototype_design:   [brief description]
  prototype_result:   [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4 (SESSION INVARIANT D, Stage 4 template applied verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1).

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------------------------
  prototype  | [prototype_result]            | "Does [prototype result] make a
             |                               |  credible case for displacing
             |                               |  [comparator] with [topic]?
             |                               |  [Yes / No / Pending]"

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = format error
  s4_ce_verdict:           [null if no CE; description if found]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 handoff fields populated — 0 additions, 0 omissions, 0 mismatches.
Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete — s4_ce_verdict = [value]. null_tally_final = [N].
   Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

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
  Cross-check vs Stage 4 exit count: [Match / Mismatch — record if mismatch before continuing]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4 — with explicit
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
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]| does not pass
                             |         |                                     | through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | does not pass
                             |         |                                     | through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | does not pass
                             |         |                                     | through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.