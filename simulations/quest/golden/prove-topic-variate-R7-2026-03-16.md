---
skill: quest-variate
skill_target: prove-topic
round: R7
date: 2026-03-16
rubric: prove-topic-rubric-v7-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [role_a_displacement_chain_contract, stage5_entry_chain_gate, stage5_exit_chain_audit]
  combined: [V-04 (C-27+C-28), V-05 (C-27+C-28+C-29+full_stack)]
r6_high_scores: V-05 (C-27 PASS, C-28 PASS, C-29 PASS -- all three satisfied as full-stack combination)
r7_targets: C-27 (ROLE A commits binding chain AND displacement evidence chain in single pre-stage block), C-28 (Stage 5 ENTRY CONDITIONS gate on all three artifact Displacement reads confirmed), C-29 (Stage 5 EXIT SIGNAL names displacement read chain closure as chain-closure audit record)
severity_stack_gap: "R6 V-05 satisfies all three simultaneously but only as a full-stack all-axis combination. No R6 single-axis variation isolates C-27/C-28/C-29 individually. V-01 isolates C-27 (ROLE A contract standalone). V-02 isolates C-28 (Stage 5 entry gate standalone). V-03 isolates C-29 (EXIT SIGNAL chain audit standalone). V-04 combines C-27+C-28. V-05 assembles all three on the full structural stack."
---

# prove-topic -- Variation Round R7

Five complete, runnable skill body prompts. Each is self-contained -- no diff, no cross-references.

Round 7 targets C-27, C-28, and C-29, the three new criteria in rubric v7. These criteria
extend prior-round gains from displacement evidence artifact portability into pre-stage
commitment and post-stage audit:

- **C-27** addresses *when* the displacement evidence chain is contracted: ROLE A
  initialization before Stage 0 fires commits Stages 2/3/4 to writing Displacement read
  fields to artifact bodies. R6 variations write per-stage Displacement read fields but no
  single-axis variation uses ROLE A initialization to contract the chain.

- **C-28** addresses *how* Stage 5 guards against chain gaps: an explicit structural gate
  in ENTRY CONDITIONS requiring all three artifact Displacement reads confirmed before
  synthesis begins. R6 variations cite reads in evidence_summary but place no pre-synthesis
  structural gate enforcing their presence.

- **C-29** addresses *what EXIT SIGNALs record*: Stage 5 EXIT SIGNAL names displacement
  read chain closure explicitly, converting a stage-completion stamp into a chain-closure
  audit record. Forms C-17 (declaration) + C-25 (output) + C-29 (audit) three-layer
  synthesis governance architecture.

---

## V-01 -- Axis: ROLE A Displacement Chain Contract (C-27)

**Variation hypothesis**: Adding an explicit `displacement_read_contract` field to ROLE A
initialization -- committing Stages 2/3/4 to writing "Displacement read:" to artifact bodies
before Stage 5 entry -- satisfies C-27 as a standalone structural insertion without requiring
other stage-level changes.

```
depth: standard
confidence: standard
for: {value}
iterations: 1

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
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all five before roles execute.

Canonical failure labels registered here; echoed verbatim at inline enforcement checkpoints.

  ID   | NAME                      | DECLARATION                                | FAILURE LABEL
  -----|---------------------------|--------------------------------------------|---------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support     | FORMAT ERROR
       | REGISTER                  |   the displacement of [incumbent from       |
       |                           |   CAMPAIGN OPEN INCUMBENT ANCHOR] by        |
       |                           |   {topic} on [dimension]?                   |
       |                           |   [Yes / No / Inconclusive]"                |
       |                           | Binding: [incumbent from CAMPAIGN OPEN      |
       |                           |   INCUMBENT ANCHOR] resolves to             |
       |                           |   incumbent_name. Naming as literal string  |
       |                           |   = FORMAT ERROR.                           |
       |                           | Stage 3: "Does [practitioner account]       |
       |                           |   reveal a viable transition path from      |
       |                           |   [incumbent from CAMPAIGN OPEN INCUMBENT   |
       |                           |   ANCHOR] to {topic} for [use case]?        |
       |                           |   [Yes / No / Inconclusive]"                |
       |                           | Stage 4: "Does [prototype result] make a    |
       |                           |   credible case for displacing [incumbent   |
       |                           |   from CAMPAIGN OPEN INCUMBENT ANCHOR]      |
       |                           |   with {topic}? [Yes / No / Pending]"       |
       |                           | Template deviation = FORMAT ERROR.          |
       |                           | Cannot be modified or bypassed at any stage.|
  -----|---------------------------|--------------------------------------------|---------------------
  A    | ADVERSARIAL REVIEWER TYPE | adversarial_reviewer_type: [role most       | DUAL-LOCK ERROR
       |                           |   likely to challenge displacement claim].  |
       |                           | Activation: null_tally_final >= 3.          |
  -----|---------------------------|--------------------------------------------|---------------------
  B    | CONFIDENCE CAP            | confidence_composite -= 2 if               | INTEGRITY FAILURE
       |                           |   null_tally_final >= 3. Hard cap.          |
  -----|---------------------------|--------------------------------------------|---------------------
  C    | DERIVATION ANNOTATION     | Every handoff field carries [derived from:  | ORDER ERROR
       |                           |   X]. Unlabeled = FORMAT ERROR.             |
  -----|---------------------------|--------------------------------------------|---------------------
  E    | HANDOFF SCHEMA INTEGRITY  | All 11 handoff fields required.            | Invariant E
       |                           | Missing or unlabeled = Invariant E          | checkpoint -- FAIL
       |                           |   checkpoint -- FAIL.                       |

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE
  -------|--------------------------|------------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared               | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3      | THIRD

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Step 1: Confirm all five SESSION INVARIANT TABLE rows filled and active.
  invariant_registry_confirmed: [true when all five invariants registered]

  Step 2: Read CAMPAIGN OPEN INCUMBENT ANCHOR sub-section. Record resolved binding.
  incumbent_anchor_read: [incumbent_name value from CAMPAIGN OPEN INCUMBENT ANCHOR --
                          copied, not inferred. Must trace to sub-section by name.
                          Invariant D binding active.]

  Step 3: Commit displacement evidence chain for Stages 2, 3, and 4.
  displacement_read_contract: Stages 2, 3, 4 will write "Displacement read:" field to
    artifact bodies before Stage 5 entry. Stage 5 entry will confirm all three.
    Contract active. Cannot be bypassed.

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. Mismatch = INTEGRITY FAILURE.

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
  confidence_composite       | Stage 5 minus reductions                  | capped by INV B

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete -- all five rows with canonical failure labels
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified, scout_loaded confirmed
  [ ] ROLE A executed -- invariant_registry_confirmed = true,
      incumbent_anchor_read confirmed (tracing to CAMPAIGN OPEN INCUMBENT ANCHOR sub-section),
      displacement_read_contract active (Stages 2/3/4 committed)

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED  | RESULT
  -----|------------------------------|---------|-----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true      | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true      | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true      | [confirm or BLOCKED]
  3a   | incumbent_anchor_read        | ROLE A  | confirmed | [confirm or BLOCKED]
  3b   | displacement_read_contract   | ROLE A  | active    | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3, 3a, 3b all confirmed. SESSION INVARIANT D active.
   Displacement read contract active for Stages 2, 3, 4. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered (ROLE A Step 3)

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
      "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN
       INCUMBENT ANCHOR] by {topic} on [dimension]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D, Stage 2 template verbatim):

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|------------------------------
  1    | [source]                 | [summary]            | "Does [item 1] support
  2    | [source]                 | [summary]            |  displacement of [incumbent from
  3    | [source]                 | [summary]            |  CAMPAIGN OPEN INCUMBENT ANCHOR]
  add  |                          |                      |  by {topic} on [dim]? [verdict]"

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  Displacement read:          [stage-level displacement conclusion synthesized from check table]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-websearch-{date}.md.
  Artifact body includes "Displacement read: [value]" field.
  (Per displacement_read_contract from ROLE A Step 3.)
  Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N].
   Displacement read written to artifact. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim from table row D):
      "Does [practitioner account] reveal a viable transition path from [incumbent from
       CAMPAIGN OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D, Stage 3 template verbatim):

  PRACTITIONER     | KEY ACCOUNT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------------|--------------------------|------------------------------
  [type 1]         | [quote or paraphrase]    | "Does [account 1] reveal a viable
  [type 2]         | [quote or paraphrase]    |  transition path from [incumbent from
  [type 3]         | [quote or paraphrase]    |  CAMPAIGN OPEN INCUMBENT ANCHOR]
  add rows          |                          |  to {topic} for [use case]? [verdict]"

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  Displacement read:          [stage-level displacement conclusion synthesized from check table]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-interview-{date}.md.
  Artifact body includes "Displacement read: [value]" field.
  (Per displacement_read_contract from ROLE A Step 3.)
  Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N].
   Displacement read written to artifact. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim from table row D):
      "Does [prototype result] make a credible case for displacing [incumbent from
       CAMPAIGN OPEN INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"
      Verdict required. Omission = FORMAT ERROR.

STAGE 4 BODY:
Design and assess minimal prototype.

  prototype_design:   [brief description]
  prototype_result:   [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D, Stage 4 template verbatim):

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------------------------
  prototype  | [prototype_result]            | "Does [result] make a credible case
             |                               |  for displacing [incumbent from CAMPAIGN
             |                               |  OPEN INCUMBENT ANCHOR] with {topic}?
             |                               |  [Yes / No / Pending]"

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]
  Displacement read:       [stage-level displacement conclusion synthesized from check table]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-prototype-{date}.md.
  Artifact body includes "Displacement read: [value]" field.
  (Per displacement_read_contract from ROLE A Step 3.)
  Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict = [value]. null_tally_final = [N].
   Displacement read written to artifact. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All five SESSION INVARIANT TABLE rows active

STAGE 5 BODY:

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### ATOMIC DUAL-LOCK

  S2 -> [s2_ce_verdict] | S3 -> [s3_ce_verdict] | S4 -> [s4_ce_verdict]
  null_tally_final = [N]
  Cross-check vs Stage 4: [Match / Mismatch -- record if mismatch]

  >= 3: Lock 1 (INV A) adversarial review + Lock 2 (INV B) -= 2. DUAL-LOCK ERROR if bypassed.
        co_activation_confirmed: dual_lock_fired
  < 3:  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4 -- cite Stage 4
                           displacement verdict explicitly]
  confidence_composite:  [final value]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. Unlabeled = FORMAT ERROR.

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]| not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields verified]            | Invariant E checkpoint -- FAIL if not

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-02 -- Axis: Stage 5 Entry Condition Chain Gate (C-28)

**Variation hypothesis**: Adding `[ ] All three artifact Displacement read fields confirmed
written` as an explicit Stage 5 ENTRY CONDITION -- without modifying ROLE A or any earlier
stage -- satisfies C-28 as a standalone insertion at Stage 5 entry alone.

```
depth: standard
confidence: standard
for: {value}
iterations: 1

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
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

Canonical failure labels registered here; echoed verbatim at inline checkpoints.

  ID   | NAME                      | DECLARATION                                | FAILURE LABEL
  -----|---------------------------|--------------------------------------------|---------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the | FORMAT ERROR
       | REGISTER                  |   displacement of [incumbent from CAMPAIGN  |
       |                           |   OPEN INCUMBENT ANCHOR] by {topic} on     |
       |                           |   [dimension]? [Yes / No / Inconclusive]"  |
       |                           | Binding: resolves to incumbent_name.       |
       |                           |   Literal string = FORMAT ERROR.           |
       |                           | Stage 3: "Does [practitioner account]      |
       |                           |   reveal a viable transition path from     |
       |                           |   [incumbent from CAMPAIGN OPEN INCUMBENT  |
       |                           |   ANCHOR] to {topic} for [use case]?       |
       |                           |   [Yes / No / Inconclusive]"               |
       |                           | Stage 4: "Does [prototype result] make a   |
       |                           |   credible case for displacing [incumbent  |
       |                           |   from CAMPAIGN OPEN INCUMBENT ANCHOR]     |
       |                           |   with {topic}? [Yes / No / Pending]"      |
       |                           | Template deviation = FORMAT ERROR.         |
  -----|---------------------------|--------------------------------------------|---------------------
  A    | ADVERSARIAL REVIEWER TYPE | Activation: null_tally_final >= 3.         | DUAL-LOCK ERROR
  -----|---------------------------|--------------------------------------------|---------------------
  B    | CONFIDENCE CAP            | -= 2 if null_tally_final >= 3. Hard cap.   | INTEGRITY FAILURE
  -----|---------------------------|--------------------------------------------|---------------------
  C    | DERIVATION ANNOTATION     | [derived from: X] on every handoff field.  | ORDER ERROR
  -----|---------------------------|--------------------------------------------|---------------------
  E    | HANDOFF SCHEMA INTEGRITY  | 11 fields required. Missing/unlabeled =    | Invariant E
       |                           |   Invariant E checkpoint -- FAIL.          | checkpoint -- FAIL

### ROLE OWNERSHIP TABLE

  ROLE   | TITLE                    | OWNED FIELD                  | EXECUTE
  -------|--------------------------|------------------------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared               | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | THIRD

ROLE C: incumbent_threat_locked: [true when INCUMBENT ANCHOR filled]
ROLE B: scout_artifact: [path], scout_loaded: [t/f], gate_s_cleared: [true or BLOCKED]
ROLE A: invariant_registry_confirmed: [true when all invariants registered]

### CE VERDICT OWNERSHIP TABLE

  s2_ce_verdict | Stage 2 | null or citation
  s3_ce_verdict | Stage 3 | null or citation
  s4_ce_verdict | Stage 4 | null or description
  null_tally_final | Stage 4 close | count(null) s2+s3+s4 -- Mismatch = INTEGRITY FAILURE

### PRE-COMMITTED HANDOFF SCHEMA (11 fields)

  scout_anchor | incumbent_threat_locked | hypothesis | counter_hypothesis |
  s2_ce_verdict | s3_ce_verdict | s4_ce_verdict | null_tally_final |
  co_activation_confirmed | incumbent_defense_closed | confidence_composite

---

## STAGE 0 -- GATE S

ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN filled | [ ] INCUMBENT ANCHOR filled | [ ] SESSION INVARIANTS complete
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: gate_s_cleared = true
  [ ] ROLE A: invariant_registry_confirmed = true

CLEARANCE TABLE:
  1 | incumbent_threat_locked    | ROLE C | [confirm or BLOCKED]
  2 | gate_s_cleared             | ROLE B | [confirm or BLOCKED]
  3 | invariant_registry_confirmed| ROLE A | [confirm or BLOCKED]

EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1-3 confirmed. SESSION INVARIANT D active. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

ENTRY CONDITIONS:
  [ ] gate_open received | [ ] scout_artifact available | [ ] INV D registered

  source_scout_artifact: [from ROLE B]
  hypothesis:            [falsifiable claim]
  counter_hypothesis:    [incumbent's best defense]

Write: {topic}-hypothesis-{date}.md. Confirm write.
EXIT SIGNAL: hypothesis_locked -- "{topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

ENTRY CONDITIONS:
  [ ] hypothesis_locked | [ ] hypothesis artifact confirmed
  [ ] INV D Stage 2 template: "Does [evidence item] support the displacement of [incumbent
      from CAMPAIGN OPEN INCUMBENT ANCHOR] by {topic} on [dim]? [Yes/No/Inconclusive]"
      Template deviation = FORMAT ERROR.

INCUMBENT CHECK TABLE -- Stage 2:
  ITEM | SOURCE | SUMMARY | TEMPLATE APPLIED & VERDICT
  1    |        |         | [verbatim INV D Stage 2 template + verdict]
  2    |        |         |
  3+   |        |         |

  s2_ce_verdict: [null or citation]
  Displacement read: [stage displacement conclusion]

Running tally: "[N] null. 2 stages remain."
Write: {topic}-websearch-{date}.md (include Displacement read field). Confirm write.
EXIT SIGNAL: websearch_complete -- "s2_ce_verdict=[value]. Tally=[N]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

ENTRY CONDITIONS:
  [ ] websearch_complete | [ ] s2_ce_verdict recorded
  [ ] INV D Stage 3 template: "Does [practitioner account] reveal a viable transition path
      from [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR] to {topic} for [use case]?
      [Yes/No/Inconclusive]" -- Template deviation = FORMAT ERROR.

INCUMBENT CHECK TABLE -- Stage 3:
  PRACTITIONER | KEY ACCOUNT | TEMPLATE APPLIED & VERDICT
  [type 1]     |             | [verbatim INV D Stage 3 template + verdict]
  [type 2]     |             |
  [type 3]     |             |

  s3_ce_verdict: [null or citation]
  Displacement read: [stage displacement conclusion]

Running tally: "[N] null. 1 stage remains."
Write: {topic}-interview-{date}.md (include Displacement read field). Confirm write.
EXIT SIGNAL: interview_complete -- "s3_ce_verdict=[value]. Tally=[N]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

ENTRY CONDITIONS:
  [ ] interview_complete | [ ] s3_ce_verdict recorded
  [ ] INV D Stage 4 template: "Does [prototype result] make a credible case for displacing
      [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR] with {topic}? [Yes/No/Pending]"
      Omission = FORMAT ERROR.

  prototype_design: [description]
  prototype_result: [1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4:
  prototype | [result] | "Does [result] make a credible case for displacing [incumbent from
                          CAMPAIGN OPEN INCUMBENT ANCHOR] with {topic}? [Yes/No/Pending]"

  s4_displacement_verdict: [Yes/No/Pending]
  s4_ce_verdict: [null or description]
  Displacement read: [stage displacement conclusion]

null_tally_final = [N]
Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [t/f]."

Write: {topic}-prototype-{date}.md (include Displacement read field). Confirm write.
EXIT SIGNAL: prototype_complete -- "s4_ce_verdict=[value]. null_tally_final=[N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active
  [ ] All three artifact Displacement read fields confirmed written:
      - {topic}-websearch-{date}.md: Displacement read confirmed
      - {topic}-interview-{date}.md: Displacement read confirmed
      - {topic}-prototype-{date}.md: Displacement read confirmed
      Stage 5 will consume all three. If any unconfirmed: halt and record which
      artifact is missing before proceeding.

STAGE 5 BODY:

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  [counter_hypothesis from Stage 1] | REFUTED / PARTIALLY REFUTED / OPEN RISK | [cite artifact]
  OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### ATOMIC DUAL-LOCK

  S2 -> [s2_ce_verdict] | S3 -> [s3_ce_verdict] | S4 -> [s4_ce_verdict]
  null_tally_final = [N] | Cross-check vs Stage 4: [Match / Mismatch]

  >= 3: Lock 1 (INV A) adversarial review + Lock 2 (INV B) -= 2.
        co_activation_confirmed: dual_lock_fired
  < 3:  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences. Cite Stage 4 displacement verdict. Cite
                           artifact Displacement reads if present in artifacts.]
  confidence_composite:  [final value]
  key_risk:              [residual incumbent strength]

### HANDOFF TABLE

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  scout_anchor               | [value] | [derived from: ROLE B]              | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C]              | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4]            | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields verified]            | Invariant E checkpoint -- FAIL if not

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-03 -- Axis: Stage 5 EXIT SIGNAL Chain Closure Audit (C-29)

**Variation hypothesis**: Extending Stage 5 EXIT SIGNAL text to name displacement read chain
closure explicitly -- "All three artifact Displacement reads cited in evidence_summary.
Displacement read chain closed." -- satisfies C-29 as a standalone modification to EXIT
SIGNAL wording alone, without modifying ROLE A or Stage 5 ENTRY CONDITIONS.

```
depth: standard
confidence: standard
for: {value}
iterations: 1

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
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

Canonical failure labels registered here; echoed verbatim at inline checkpoints.

  ID   | NAME                      | DECLARATION                                | FAILURE LABEL
  -----|---------------------------|--------------------------------------------|---------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the | FORMAT ERROR
       | REGISTER                  |   displacement of [incumbent from CAMPAIGN  |
       |                           |   OPEN INCUMBENT ANCHOR] by {topic} on     |
       |                           |   [dimension]? [Yes / No / Inconclusive]"  |
       |                           | Binding: resolves to incumbent_name.       |
       |                           |   Literal string = FORMAT ERROR.           |
       |                           | Stage 3: "Does [practitioner account]      |
       |                           |   reveal a viable transition path from     |
       |                           |   [incumbent from CAMPAIGN OPEN INCUMBENT  |
       |                           |   ANCHOR] to {topic} for [use case]?       |
       |                           |   [Yes / No / Inconclusive]"               |
       |                           | Stage 4: "Does [prototype result] make a   |
       |                           |   credible case for displacing [incumbent  |
       |                           |   from CAMPAIGN OPEN INCUMBENT ANCHOR]     |
       |                           |   with {topic}? [Yes / No / Pending]"      |
       |                           | Template deviation = FORMAT ERROR.         |
  -----|---------------------------|--------------------------------------------|---------------------
  A    | ADVERSARIAL REVIEWER TYPE | Activation: null_tally_final >= 3.         | DUAL-LOCK ERROR
  -----|---------------------------|--------------------------------------------|---------------------
  B    | CONFIDENCE CAP            | -= 2 if null_tally_final >= 3. Hard cap.   | INTEGRITY FAILURE
  -----|---------------------------|--------------------------------------------|---------------------
  C    | DERIVATION ANNOTATION     | [derived from: X] on every handoff field.  | ORDER ERROR
  -----|---------------------------|--------------------------------------------|---------------------
  E    | HANDOFF SCHEMA INTEGRITY  | 11 fields required. Missing/unlabeled =    | Invariant E
       |                           |   Invariant E checkpoint -- FAIL.          | checkpoint -- FAIL

### ROLE OWNERSHIP TABLE

  ROLE   | TITLE                    | OWNED FIELD                  | EXECUTE
  -------|--------------------------|------------------------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared               | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | THIRD

ROLE C: incumbent_threat_locked: [true when INCUMBENT ANCHOR filled]
ROLE B: scout_artifact: [path], scout_loaded: [t/f], gate_s_cleared: [true or BLOCKED]
ROLE A: invariant_registry_confirmed: [true when all invariants registered]

### CE VERDICT OWNERSHIP / NULL TALLY CHAIN

  s2_ce_verdict | s3_ce_verdict | s4_ce_verdict | null_tally_final (Stage 4 close)
  Mismatch = INTEGRITY FAILURE.

### PRE-COMMITTED HANDOFF SCHEMA (11 fields)

  scout_anchor | incumbent_threat_locked | hypothesis | counter_hypothesis |
  s2_ce_verdict | s3_ce_verdict | s4_ce_verdict | null_tally_final |
  co_activation_confirmed | incumbent_defense_closed | confidence_composite

---

## STAGE 0 -- GATE S

ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS complete
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: gate_s_cleared = true
  [ ] ROLE A: invariant_registry_confirmed = true

CLEARANCE TABLE:
  1 | incumbent_threat_locked    | ROLE C | [confirm or BLOCKED]
  2 | gate_s_cleared             | ROLE B | [confirm or BLOCKED]
  3 | invariant_registry_confirmed| ROLE A | [confirm or BLOCKED]

EXIT SIGNAL: gate_open -- "Steps 1-3 confirmed. INV D active. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

ENTRY CONDITIONS: [ ] gate_open | [ ] scout_artifact | [ ] INV D registered

  source_scout_artifact: [from ROLE B]
  hypothesis:            [falsifiable claim]
  counter_hypothesis:    [incumbent's best defense]

Write: {topic}-hypothesis-{date}.md. Confirm write.
EXIT SIGNAL: hypothesis_locked -- "{topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

ENTRY CONDITIONS:
  [ ] hypothesis_locked | [ ] hypothesis artifact confirmed
  [ ] INV D Stage 2 template active:
      "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN
       INCUMBENT ANCHOR] by {topic} on [dim]? [Yes/No/Inconclusive]"
      Template deviation = FORMAT ERROR.

INCUMBENT CHECK TABLE -- Stage 2:
  ITEM | SOURCE | SUMMARY | TEMPLATE APPLIED & VERDICT
  1    |        |         | [verbatim INV D template + verdict]
  2    |        |         |
  3+   |        |         |

  s2_ce_verdict: [null or citation]
  Displacement read: [stage displacement conclusion]

Running tally: "[N] null. 2 stages remain."
Write: {topic}-websearch-{date}.md (include Displacement read field). Confirm write.
EXIT SIGNAL: websearch_complete -- "s2_ce_verdict=[value]. Tally=[N]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

ENTRY CONDITIONS:
  [ ] websearch_complete | [ ] s2_ce_verdict recorded
  [ ] INV D Stage 3 template active:
      "Does [practitioner account] reveal a viable transition path from [incumbent from
       CAMPAIGN OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes/No/Inconclusive]"
      Template deviation = FORMAT ERROR.

INCUMBENT CHECK TABLE -- Stage 3:
  PRACTITIONER | KEY ACCOUNT | TEMPLATE APPLIED & VERDICT
  [type 1]     |             | [verbatim INV D template + verdict]
  [type 2]     |             |
  [type 3]     |             |

  s3_ce_verdict: [null or citation]
  Displacement read: [stage displacement conclusion]

Running tally: "[N] null. 1 stage remains."
Write: {topic}-interview-{date}.md (include Displacement read field). Confirm write.
EXIT SIGNAL: interview_complete -- "s3_ce_verdict=[value]. Tally=[N]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

ENTRY CONDITIONS:
  [ ] interview_complete | [ ] s3_ce_verdict recorded
  [ ] INV D Stage 4 template active:
      "Does [prototype result] make a credible case for displacing [incumbent from
       CAMPAIGN OPEN INCUMBENT ANCHOR] with {topic}? [Yes/No/Pending]"
      Omission = FORMAT ERROR.

  prototype_design: [description] | prototype_result: [1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4:
  prototype | [result] | "Does [result] make a credible case for displacing [incumbent from
                          CAMPAIGN OPEN INCUMBENT ANCHOR] with {topic}? [Yes/No/Pending]"

  s4_displacement_verdict: [Yes/No/Pending] | s4_ce_verdict: [null or description]
  Displacement read: [stage displacement conclusion]

null_tally_final = [N]
Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [t/f]."

Write: {topic}-prototype-{date}.md (include Displacement read field). Confirm write.
EXIT SIGNAL: prototype_complete -- "s4_ce_verdict=[value]. null_tally_final=[N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received
  [ ] null_tally_final recorded
  [ ] counter_hypothesis present
  [ ] All four SESSION INVARIANTS active

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  [counter_hypothesis from Stage 1] | REFUTED / PARTIALLY REFUTED / OPEN RISK | [cite artifact]
  OPEN RISK: reduce confidence_composite one tier.

### ATOMIC DUAL-LOCK

  S2 -> [s2_ce_verdict] | S3 -> [s3_ce_verdict] | S4 -> [s4_ce_verdict]
  null_tally_final = [N] | Cross-check: [Match / Mismatch]

  >= 3: co_activation_confirmed: dual_lock_fired (Lock 1 INV A + Lock 2 INV B -= 2)
  < 3:  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences. Cite Stage 4 displacement verdict.
                           Cite all three artifact Displacement reads:
                           websearch Displacement read: [value from {topic}-websearch-{date}.md],
                           interview Displacement read: [value from {topic}-interview-{date}.md],
                           prototype Displacement read: [value from {topic}-prototype-{date}.md]]
  confidence_composite:  [final value]
  key_risk:              [residual incumbent strength]

### HANDOFF TABLE

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  scout_anchor               | [value] | [derived from: ROLE B]              | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C]              | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4]            | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields verified]            | Invariant E checkpoint -- FAIL if not

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   All three artifact Displacement reads cited in evidence_summary
   (websearch, interview, prototype). Displacement read chain closed."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-04 -- Combined: C-27 + C-28 (ROLE A Chain Contract + Stage 5 Entry Gate)

**Variation hypothesis**: ROLE A displacement chain contract (C-27) and Stage 5 entry
condition chain gate (C-28) reinforce each other: ROLE A commits pre-Stage 0, and Stage 5
entry conditions verify the commitment was honored before synthesis begins. Together they
eliminate the gap between contract declaration and synthesis consumption.

```
depth: standard
confidence: standard
for: {value}
iterations: 1

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
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

Canonical failure labels registered here; echoed verbatim at inline checkpoints.

  ID   | NAME                      | DECLARATION                                | FAILURE LABEL
  -----|---------------------------|--------------------------------------------|---------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the | FORMAT ERROR
       | REGISTER                  |   displacement of [incumbent from CAMPAIGN  |
       |                           |   OPEN INCUMBENT ANCHOR] by {topic} on     |
       |                           |   [dimension]? [Yes / No / Inconclusive]"  |
       |                           | Binding: [incumbent from CAMPAIGN OPEN     |
       |                           |   INCUMBENT ANCHOR] resolves to            |
       |                           |   incumbent_name. Naming as literal string |
       |                           |   = FORMAT ERROR.                          |
       |                           | Stage 3: "Does [practitioner account]      |
       |                           |   reveal a viable transition path from     |
       |                           |   [incumbent from CAMPAIGN OPEN INCUMBENT  |
       |                           |   ANCHOR] to {topic} for [use case]?       |
       |                           |   [Yes / No / Inconclusive]"               |
       |                           | Stage 4: "Does [prototype result] make a   |
       |                           |   credible case for displacing [incumbent  |
       |                           |   from CAMPAIGN OPEN INCUMBENT ANCHOR]     |
       |                           |   with {topic}? [Yes / No / Pending]"      |
       |                           | Template deviation = FORMAT ERROR.         |
  -----|---------------------------|--------------------------------------------|---------------------
  A    | ADVERSARIAL REVIEWER TYPE | Activation: null_tally_final >= 3.         | DUAL-LOCK ERROR
  -----|---------------------------|--------------------------------------------|---------------------
  B    | CONFIDENCE CAP            | -= 2 if null_tally_final >= 3. Hard cap.   | INTEGRITY FAILURE
  -----|---------------------------|--------------------------------------------|---------------------
  C    | DERIVATION ANNOTATION     | [derived from: X] on every handoff field.  | ORDER ERROR
  -----|---------------------------|--------------------------------------------|---------------------
  E    | HANDOFF SCHEMA INTEGRITY  | 11 fields required. Missing/unlabeled =    | Invariant E
       |                           |   Invariant E checkpoint -- FAIL.          | checkpoint -- FAIL

### ROLE OWNERSHIP TABLE

  ROLE   | TITLE                    | OWNED FIELD                  | EXECUTE
  -------|--------------------------|------------------------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared               | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | THIRD

ROLE C execution (fill now):
  incumbent_threat_locked: [true when INCUMBENT ANCHOR filled]

ROLE B execution (fill now):
  scout_artifact:  [path]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true or CAMPAIGN BLOCKED]

ROLE A execution (fill now):
  Step 1: Confirm SESSION INVARIANTS registered.
  invariant_registry_confirmed: [true]

  Step 2: Read CAMPAIGN OPEN INCUMBENT ANCHOR sub-section. Record resolved binding.
  incumbent_anchor_read: [incumbent_name from CAMPAIGN OPEN INCUMBENT ANCHOR -- copied,
                          must trace to sub-section by name. Invariant D binding active.]

  Step 3: Commit displacement evidence chain for Stages 2, 3, and 4.
  displacement_read_contract: Stages 2, 3, 4 will write "Displacement read:" field to
    artifact bodies. Stage 5 entry conditions will verify all three confirmed before
    synthesis begins. Contract active. Cannot be bypassed.

### CE VERDICT OWNERSHIP / NULL TALLY CHAIN

  s2/s3/s4_ce_verdict | null_tally_final (Stage 4 close)
  Mismatch = INTEGRITY FAILURE.

### PRE-COMMITTED HANDOFF SCHEMA (11 fields)

  scout_anchor | incumbent_threat_locked | hypothesis | counter_hypothesis |
  s2_ce_verdict | s3_ce_verdict | s4_ce_verdict | null_tally_final |
  co_activation_confirmed | incumbent_defense_closed | confidence_composite

---

## STAGE 0 -- GATE S

ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS complete
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: gate_s_cleared = true
  [ ] ROLE A: invariant_registry_confirmed = true,
      incumbent_anchor_read confirmed (tracing to CAMPAIGN OPEN INCUMBENT ANCHOR sub-section),
      displacement_read_contract active

CLEARANCE TABLE:
  1  | incumbent_threat_locked    | ROLE C | [confirm or BLOCKED]
  2  | gate_s_cleared             | ROLE B | [confirm or BLOCKED]
  3  | invariant_registry_confirmed| ROLE A | [confirm or BLOCKED]
  3a | incumbent_anchor_read      | ROLE A | [confirm or BLOCKED]
  3b | displacement_read_contract | ROLE A | active / [BLOCKED]

EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1-3b confirmed. Displacement read contract active.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

ENTRY CONDITIONS: [ ] gate_open | [ ] scout_artifact | [ ] INV D registered

  source_scout_artifact: [from ROLE B]
  hypothesis:            [falsifiable claim]
  counter_hypothesis:    [incumbent's best defense]

Write: {topic}-hypothesis-{date}.md. Confirm write.
EXIT SIGNAL: hypothesis_locked -- "{topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

ENTRY CONDITIONS:
  [ ] hypothesis_locked | [ ] hypothesis artifact confirmed
  [ ] INV D Stage 2 template: "Does [evidence item] support the displacement of [incumbent
      from CAMPAIGN OPEN INCUMBENT ANCHOR] by {topic} on [dim]? [Yes/No/Inconclusive]"
      Template deviation = FORMAT ERROR.

INCUMBENT CHECK TABLE -- Stage 2:
  ITEM | SOURCE | SUMMARY | TEMPLATE APPLIED & VERDICT
  1    |        |         | [verbatim INV D template + verdict]
  2    |        |         |
  3+   |        |         |

  s2_ce_verdict: [null or citation]
  Displacement read: [stage displacement conclusion]

Running tally: "[N] null. 2 stages remain."
Write: {topic}-websearch-{date}.md.
  Artifact includes "Displacement read: [value]" field (per displacement_read_contract).
  Confirm write.
EXIT SIGNAL: websearch_complete -- "s2_ce_verdict=[value]. Tally=[N]. Displacement read in artifact. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

ENTRY CONDITIONS:
  [ ] websearch_complete | [ ] s2_ce_verdict recorded
  [ ] INV D Stage 3 template: "Does [practitioner account] reveal a viable transition path
      from [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR] to {topic} for [use case]?
      [Yes/No/Inconclusive]" -- Template deviation = FORMAT ERROR.

INCUMBENT CHECK TABLE -- Stage 3:
  PRACTITIONER | KEY ACCOUNT | TEMPLATE APPLIED & VERDICT
  [type 1]     |             | [verbatim INV D template + verdict]
  [type 2]     |             |
  [type 3]     |             |

  s3_ce_verdict: [null or citation]
  Displacement read: [stage displacement conclusion]

Running tally: "[N] null. 1 stage remains."
Write: {topic}-interview-{date}.md.
  Artifact includes "Displacement read: [value]" field (per displacement_read_contract).
  Confirm write.
EXIT SIGNAL: interview_complete -- "s3_ce_verdict=[value]. Tally=[N]. Displacement read in artifact. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

ENTRY CONDITIONS:
  [ ] interview_complete | [ ] s3_ce_verdict recorded
  [ ] INV D Stage 4 template: "Does [prototype result] make a credible case for displacing
      [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR] with {topic}? [Yes/No/Pending]"
      Omission = FORMAT ERROR.

  prototype_design: [description] | prototype_result: [1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4:
  prototype | [result] | "Does [result] make a credible case for displacing [incumbent from
                          CAMPAIGN OPEN INCUMBENT ANCHOR] with {topic}? [Yes/No/Pending]"

  s4_displacement_verdict: [Yes/No/Pending] | s4_ce_verdict: [null or description]
  Displacement read: [stage displacement conclusion]

null_tally_final = [N]
Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [t/f]."

Write: {topic}-prototype-{date}.md.
  Artifact includes "Displacement read: [value]" field (per displacement_read_contract).
  Confirm write.
EXIT SIGNAL: prototype_complete -- "s4_ce_verdict=[value]. null_tally_final=[N]. Displacement read in artifact. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received
  [ ] null_tally_final recorded
  [ ] counter_hypothesis present
  [ ] All four SESSION INVARIANTS active
  [ ] All three artifact Displacement read fields confirmed written
      (per displacement_read_contract committed by ROLE A Step 3):
      - {topic}-websearch-{date}.md: Displacement read confirmed
      - {topic}-interview-{date}.md: Displacement read confirmed
      - {topic}-prototype-{date}.md: Displacement read confirmed
      Stage 5 will consume all three. If any unconfirmed: halt and record missing artifact.

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  [counter_hypothesis from Stage 1] | REFUTED / PARTIALLY REFUTED / OPEN RISK | [cite artifact]
  OPEN RISK: reduce confidence_composite one tier.

### ATOMIC DUAL-LOCK

  S2/S3/S4 -> [respective ce_verdicts]
  null_tally_final = [N] | Cross-check vs Stage 4: [Match / Mismatch]

  >= 3: co_activation_confirmed: dual_lock_fired (Lock 1 INV A + Lock 2 INV B -= 2)
  < 3:  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences. Cite Stage 4 displacement verdict. Cite artifact reads:
                           websearch Displacement read: [value],
                           interview Displacement read: [value],
                           prototype Displacement read: [value]]
  confidence_composite:  [final value]
  key_risk:              [residual incumbent strength]

### HANDOFF TABLE

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  scout_anchor               | [value] | [derived from: ROLE B]              | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C]              | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4]            | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields verified]            | Invariant E checkpoint -- FAIL if not

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-05 -- Full Integration: C-27 + C-28 + C-29 + Full Structural Stack

**Variation hypothesis**: All three v7 criteria assembled on the complete prior-round
structural stack -- C-14 two-layer enforcement, C-16/C-20 per-stage Displacement read fields
in artifacts, C-17 SYNTHESIS DECLARATIONS prohibition, C-18 Invariant E checkpoint,
C-21 INCUMBENT ANCHOR prohibition, C-22 binding failure label, C-24/C-26 sub-section
precision, C-25 all-three reads in evidence_summary -- will satisfy all 29 criteria.

```
depth: standard
confidence: standard
for: {value}
iterations: 1

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
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

All invariants carry: "cannot be modified or bypassed at any subsequent stage."
Canonical failure labels registered here. Echoed verbatim at every inline enforcement
checkpoint. Divergence from registered label = registered label fires automatically.

  ID   | NAME                      | DECLARATION                                | FAILURE LABEL
  -----|---------------------------|--------------------------------------------|---------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the | FORMAT ERROR
       | REGISTER                  |   displacement of [incumbent from CAMPAIGN  |
       |                           |   OPEN INCUMBENT ANCHOR] by {topic} on     |
       |                           |   [dimension]? [Yes / No / Inconclusive]"  |
       |                           | Stage 3: "Does [practitioner account]      |
       |                           |   reveal a viable transition path from     |
       |                           |   [incumbent from CAMPAIGN OPEN INCUMBENT  |
       |                           |   ANCHOR] to {topic} for [use case]?       |
       |                           |   [Yes / No / Inconclusive]"               |
       |                           | Stage 4: "Does [prototype result] make a   |
       |                           |   credible case for displacing [incumbent  |
       |                           |   from CAMPAIGN OPEN INCUMBENT ANCHOR]     |
       |                           |   with {topic}? [Yes / No / Pending]"      |
       |                           | Binding: [incumbent from CAMPAIGN OPEN     |
       |                           |   INCUMBENT ANCHOR] resolves to            |
       |                           |   incumbent_name. Naming as literal string |
       |                           |   = FORMAT ERROR.                          |
       |                           | Template deviation = FORMAT ERROR.         |
       |                           | Cannot be modified or bypassed at any stage|
  -----|---------------------------|--------------------------------------------|---------------------
  A    | ADVERSARIAL REVIEWER TYPE | adversarial_reviewer_type: [role most      | DUAL-LOCK ERROR
       |                           |   likely to challenge displacement claim]. |
       |                           | Activation: null_tally_final >= 3.         |
       |                           | Cannot be modified or bypassed at synthesis|
  -----|---------------------------|--------------------------------------------|---------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: -= 2 if                 | INTEGRITY FAILURE
       |                           |   null_tally_final >= 3. Hard cap.         |
       |                           | Cannot be softened or overridden.          |
  -----|---------------------------|--------------------------------------------|---------------------
  C    | DERIVATION ANNOTATION     | Every handoff field carries [derived from: | ORDER ERROR
       |                           |   X]. Unlabeled = FORMAT ERROR.            |
       |                           | Cannot be modified or bypassed at synthesis|
  -----|---------------------------|--------------------------------------------|---------------------
  E    | HANDOFF SCHEMA INTEGRITY  | All 11 handoff fields required.            | Invariant E
       |                           | Missing or unlabeled = Invariant E         | checkpoint -- FAIL
       |                           |   checkpoint -- FAIL.                      |

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE
  -------|--------------------------|------------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared               | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3      | THIRD

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Step 1: Confirm all five SESSION INVARIANT TABLE rows filled and active.
  invariant_registry_confirmed: [true when all five invariants registered]

  Step 2: Read CAMPAIGN OPEN INCUMBENT ANCHOR sub-section. Record resolved binding value.
  incumbent_anchor_read: [incumbent_name value from CAMPAIGN OPEN INCUMBENT ANCHOR
                          sub-section -- copied, not inferred. Must trace to
                          INCUMBENT ANCHOR sub-section by name, not to parent CAMPAIGN OPEN
                          block. Invariant D binding active per SESSION INVARIANTS table row D.]

  Step 3: Commit displacement evidence chain for Stages 2, 3, and 4.
  displacement_read_contract: Stages 2, 3, 4 will write "Displacement read:" field to
    artifact bodies before Stage 5 entry. Stage 5 entry conditions will confirm all three
    artifact Displacement reads written before synthesis begins. Contract active.
    Cannot be bypassed at any stage.

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = INTEGRITY FAILURE.

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
  confidence_composite       | Stage 5 minus reductions                  | capped by INV B

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled
  [ ] INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete -- all five rows with canonical failure labels
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout_artifact identified, scout_loaded confirmed
  [ ] ROLE A: invariant_registry_confirmed = true,
      incumbent_anchor_read confirmed (tracing to CAMPAIGN OPEN INCUMBENT ANCHOR sub-section),
      displacement_read_contract active (Stages 2/3/4 committed)

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED  | RESULT
  -----|------------------------------|---------|-----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true      | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true      | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true      | [confirm or BLOCKED]
  3a   | incumbent_anchor_read        | ROLE A  | confirmed | [confirm or BLOCKED]
       |   (INCUMBENT ANCHOR          |         |           |
       |    sub-section by name)      |         |           |
  3b   | displacement_read_contract   | ROLE A  | active    | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3, 3a, 3b all confirmed.
   SESSION INVARIANT D active. Displacement read contract active for Stages 2, 3, 4.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered (ROLE A Step 3)

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense -- grounded in ROLE C analysis]
  gate_s_cleared:               [true]
  invariant_registry_confirmed: [true]
  incumbent_threat_locked:      [true]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from SESSION INVARIANTS table row D):
      "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN
       INCUMBENT ANCHOR] by {topic} on [dimension]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR. (Canonical label from SESSION INVARIANTS INV D.)

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D, Stage 2 template verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|------------------------------
  1    | [source]                 | [summary]            | "Does [item 1] support the
  2    | [source]                 | [summary]            |  displacement of [incumbent
  3    | [source]                 | [summary]            |  from CAMPAIGN OPEN INCUMBENT
  add  |                          |                      |  ANCHOR] by {topic} on [dim]?
       |                          |                      |  [Yes/No/Inconclusive]"

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  Displacement read:          [stage-level displacement conclusion synthesized from table]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-websearch-{date}.md.
  Artifact body includes "Displacement read: [value]" field.
  (Required by displacement_read_contract from ROLE A Step 3.)
  Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict = [value]. Tally: [N].
   Displacement read written to {topic}-websearch-{date}.md. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim from SESSION INVARIANTS table row D):
      "Does [practitioner account] reveal a viable transition path from [incumbent from
       CAMPAIGN OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"
      Template deviation = FORMAT ERROR. (Canonical label from SESSION INVARIANTS INV D.)

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D, Stage 3 template verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).

  PRACTITIONER     | KEY ACCOUNT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------------|--------------------------|------------------------------
  [type 1]         | [quote or paraphrase]    | "Does [account 1] reveal a viable
  [type 2]         | [quote or paraphrase]    |  transition path from [incumbent from
  [type 3]         | [quote or paraphrase]    |  CAMPAIGN OPEN INCUMBENT ANCHOR]
  add rows          |                          |  to {topic} for [use case]? [verdict]"

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  Displacement read:          [stage-level displacement conclusion synthesized from table]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-interview-{date}.md.
  Artifact body includes "Displacement read: [value]" field.
  (Required by displacement_read_contract from ROLE A Step 3.)
  Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict = [value]. Tally: [N].
   Displacement read written to {topic}-interview-{date}.md. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim from SESSION INVARIANTS table row D):
      "Does [prototype result] make a credible case for displacing [incumbent from
       CAMPAIGN OPEN INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"
      Verdict required. Omission = FORMAT ERROR.
      Template deviation = FORMAT ERROR. (Canonical label from SESSION INVARIANTS INV D.)

STAGE 4 BODY:
Design and assess minimal prototype.

  prototype_design:   [brief description]
  prototype_result:   [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D, Stage 4 template verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------------------------
  prototype  | [prototype_result]            | "Does [result] make a credible
             |                               |  case for displacing [incumbent
             |                               |  from CAMPAIGN OPEN INCUMBENT
             |                               |  ANCHOR] with {topic}?
             |                               |  [Yes / No / Pending]"

  s4_displacement_verdict: [Yes / No / Pending]  <- required; omission = FORMAT ERROR
  s4_ce_verdict:           [null if no CE; description if found]
  Displacement read:       [stage-level displacement conclusion synthesized from table]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 handoff fields populated.

Write artifact: {topic}-prototype-{date}.md.
  Artifact body includes "Displacement read: [value]" field.
  (Required by displacement_read_contract from ROLE A Step 3.)
  Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict = [value]. null_tally_final = [N].
   Displacement read written to {topic}-prototype-{date}.md. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All five SESSION INVARIANT TABLE rows active
  [ ] All three artifact Displacement read fields confirmed written
      (per displacement_read_contract committed by ROLE A Step 3):
      - {topic}-websearch-{date}.md: Displacement read confirmed
      - {topic}-interview-{date}.md: Displacement read confirmed
      - {topic}-prototype-{date}.md: Displacement read confirmed
      Structural gate: if any Displacement read unconfirmed, halt synthesis.
      Record which artifact is missing. Do not begin SYNTHESIS DECLARATIONS
      until all three confirmed.

STAGE 5 BODY:

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]
  [add rows as needed]   |                                          |

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch -- record if mismatch]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2. DUAL-LOCK ERROR if bypassed.
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4.
                           Required citations:
                           (1) Stage 4 displacement verdict: [Yes/No/Pending from s4_displacement_verdict]
                           (2) websearch Displacement read: [value from {topic}-websearch-{date}.md]
                           (3) interview Displacement read: [value from {topic}-interview-{date}.md]
                           (4) prototype Displacement read: [value from {topic}-prototype-{date}.md]
                           All four citations required. Missing any = incomplete chain.]
  confidence_composite:  [final value]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = FORMAT ERROR.
(Canonical label from SESSION INVARIANTS INV C. Echoed here per two-layer enforcement.)

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]| not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields present and labeled] | Invariant E checkpoint -- FAIL
                             |         |                                     | if any field missing or unlabeled

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   All three artifact Displacement reads cited in evidence_summary
   (websearch: confirmed, interview: confirmed, prototype: confirmed).
   Displacement read chain closed. Null tally chain closed. Handoff schema complete."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```
