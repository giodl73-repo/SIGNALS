---
skill: quest-variate
skill_target: prove-topic
round: R14
date: 2026-03-16
rubric: prove-topic-rubric-v13-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [role_sequence, output_format, lifecycle_emphasis]
  combined: [V-04 (phrasing_register + inertia_framing), V-05 (all_four)]
r13_anchor: >
  R13 V-05 satisfies C-01 through C-36 on the full v12 stack. C-37 (role declaration
  order encodes C->B->A dependency), C-38 (SESSION INVARIANT D template printed verbatim
  at each INCUMBENT CHECK execution point), and C-39 (dual-site enforcement: template in
  ENTRY CONDITIONS gate obligation AND INCUMBENT CHECK execution obligation) are the three
  new aspirational criteria added in v13. All R14 variations build on the complete
  v12+C-37+C-38+C-39 foundation — no criterion from C-01 through C-39 is relaxed.
r14_targets: >
  R13 established three structural innovations:
  C-37: roles declared C->B->A so the dependency chain is readable before the gate block.
  C-38: SESSION INVARIANT D template printed verbatim at each INCUMBENT CHECK execution
  point — deviation visible before it happens, not only by backward registry lookup.
  C-39: template at both ENTRY CONDITIONS (gate obligation) AND INCUMBENT CHECK headers
  (execution obligation) — two independent structural sites per stage.

  R14 variation axes:
  (1) Role sequence — numbered dependency chain: each role declaration in CAMPAIGN OPEN
  opens with a numbered "STEP N OF 3" header that states the dependency rationale inline.
  The execution dependency reads as a self-annotated chain: ROLE C establishes what must
  be displaced before ROLE B can evaluate the scout artifact, and ROLE B confirms the
  scout before ROLE A can frame invariants. Tests whether inline dependency rationale
  makes C-37 more readable than a plain ordering alone.

  (2) Output format — checklist-dominant: all structured metadata uses [ ] checkbox lists
  instead of tables. SESSION INVARIANTS as a numbered [ ] list with enforcement language
  per item. ROLE definitions as confirmed [ ] items. GATE S as a numbered [ ] checklist.
  INCUMBENT CHECK blocks as a [ ] checklist with template verbatim per item. Tests whether
  compact checkbox structure preserves C-37/C-38/C-39 fidelity without table syntax.

  (3) Lifecycle emphasis — stage validation block: after the stage body and before the
  EXIT SIGNAL, each evidence stage includes a STAGE VALIDATION block that explicitly
  post-confirms: SESSION INVARIANT D template was applied verbatim (not paraphrased),
  CE verdict recorded (not blank), artifact written. This adds a post-execution validation
  layer that mirrors the pre-execution ENTRY CONDITIONS, sandwiching each stage between
  two enforcement sites in addition to the INCUMBENT CHECK mid-stage execution site.

  (4) Combined — phrasing register + inertia framing: CAMPAIGN OPEN opens with a THREAT
  REGISTER (structured four-field table: incumbent_name, incumbent_strength,
  incumbent_vulnerability, incumbent_moat). SESSION INVARIANT D is the first invariant
  registered after the THREAT REGISTER and explicitly references THREAT REGISTER field
  names in variable slot annotations. Each INCUMBENT CHECK prints the template verbatim
  and cites which THREAT REGISTER field the question probes. Tests whether grounding
  displacement-question vocabulary in a named threat model field strengthens C-38/C-39
  without lengthening the campaign.

  (5) Combined — all four axes: numbered dependency chain (V-01), checklist format for
  role confirmation (V-02 style inline with V-01 structure), stage validation blocks
  (V-03), threat-register inertia framing with SESSION INVARIANT D as primary (V-04).
  Tests whether the maximum structural density design satisfies C-37/C-38/C-39 together
  while remaining auditable as a single prompt.

---

## V-01 — Axis: Role Sequence (Numbered Dependency Chain)

**Variation axis**: Each role declaration in CAMPAIGN OPEN opens with a numbered "STEP N
OF 3 IN DEPENDENCY CHAIN" header and includes an inline dependency rationale — one
sentence explaining why this role must resolve before the next can begin. The execution
chain reads: ROLE C (Step 1) establishes who must be displaced; ROLE B (Step 2) can only
evaluate whether the scout artifact is relevant once ROLE C has named the incumbent; ROLE A
(Step 3) can only register invariants that govern displacement questions once ROLE B has
confirmed the scout is loaded. The GATE S block cites this chain explicitly:
"Clearance sequence: C (Step 1 complete) -> B (Step 2 complete) -> A (Step 3 complete)."

**Hypothesis**: C-37 requires the C->B->A ordering to be readable from the declaration
order before the gate block. R13 V-01 achieved this by position alone — ROLE C is listed
first, the order implies priority. The numbered dependency chain makes the order
semantically self-documenting: each role carries its own rationale, so a practitioner
cannot reorder the roles without also reordering the rationale sentences — making order
violations visible rather than just irregular. The gate citation of "Step 1 complete ->
Step 2 complete -> Step 3 complete" turns the clearance sequence into a dependency audit
rather than a three-checkbox confirmation.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Campaign opens with three blocking roles in dependency order. Five evidence stages follow.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

---

### STEP 1 OF 3 IN DEPENDENCY CHAIN — ROLE C: INCUMBENT THREAT ANALYST

Dependency rationale: ROLE C must resolve first because ROLE B cannot evaluate whether
a scout artifact is relevant until the incumbent has been named and analyzed. What the
scout must demonstrate displaceability against is set here — before any artifact is loaded.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]
  incumbent_threat_locked: [set to true when all three fields above are complete]

GATE S field: incumbent_threat_locked — required at GATE S Step 1.
INCUMBENT CHECK blocks at Stages 2, 3, and 4 cite ROLE C fields as their structural origin.

---

### STEP 2 OF 3 IN DEPENDENCY CHAIN — ROLE B: SCOUT LOADER

Dependency rationale: ROLE B can only confirm the scout artifact is useful once ROLE C
has established what displacement means for this campaign. The scout must speak to
{status_quo_comparator} — confirming this requires the incumbent to be named first.

  scout_artifact: [full path to {topic}-scout-record-{date}.md or equivalent]
  scout_loaded:   [true / false — confirm artifact found and readable]
  gate_s_cleared: [set to true if scout_loaded = true; else CAMPAIGN BLOCKED]

GATE S field: gate_s_cleared — required at GATE S Step 2.
CAMPAIGN BLOCKED if scout_loaded = false. Do not proceed to Step 3 or any stage.

---

### STEP 3 OF 3 IN DEPENDENCY CHAIN — ROLE A: HYPOTHESIS ARCHITECT

Dependency rationale: ROLE A can only register invariants that govern displacement-question
phrasing once ROLE B has confirmed the scout artifact is loaded. The phrasing templates in
SESSION INVARIANT D reference {status_quo_comparator} — the incumbent ROLE C named in
Step 1 — so invariant registration depends on the full Step 1 -> Step 2 chain completing.

SESSION INVARIANTS — all four locked now, cannot be modified or bypassed at any stage:

  SESSION INVARIANT A — ADVERSARIAL REVIEWER TYPE:
    adversarial_reviewer_type: [role most likely to challenge the displacement claim]
    Activation: null_tally_final >= 3
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

  SESSION INVARIANT B — CONFIDENCE CAP:
    null_ce_cap_rule: confidence_composite -= 2 if null_tally_final >= 3 (hard cap)
    Invariant language: locked formula — cannot be softened or overridden at synthesis.

  SESSION INVARIANT C — DERIVATION ANNOTATION:
    annotation_rule: Every handoff field must carry [derived from: X].
                     Unlabeled handoff field = format error.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

  SESSION INVARIANT D — INCUMBENT CHECK PHRASING REGISTER:
    These templates govern all INCUMBENT CHECK displacement questions.
    They are printed verbatim at each INCUMBENT CHECK execution point.
    Template deviation = SESSION INVARIANT D violation = format error.
    Invariant language: pre-registered — cannot be modified or bypassed at any stage.

    Stage 2 template:
      "Does [evidence item] support the displacement of {status_quo_comparator} by
       {topic} on [dimension]? [Yes / No / Inconclusive]"

    Stage 3 template:
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"

    Stage 4 template:
      "Does [prototype result] make a credible case for displacing
       {status_quo_comparator} with {topic}? [Yes / No / Pending]"

  TEMPLATE ECHO RULE (SESSION INVARIANT D): The exact template text above must be printed
  verbatim at each INCUMBENT CHECK block header before applying it to evidence items.
  Referencing SESSION INVARIANT D by name without printing the template = PARTIAL compliance.

  invariant_registry_confirmed: [set to true after all four invariants registered]

CE VERDICT OWNERSHIP TABLE — locked now:

  FIELD            | OWNED BY       | FORMULA
  -----------------|----------------|--------------------------------------------------
  s2_ce_verdict    | Stage 2        | null if no counter-evidence; citation if found
  s3_ce_verdict    | Stage 3        | null if no counter-evidence; citation if found
  s4_ce_verdict    | Stage 4        | null if no counter-evidence; description if found
  null_tally_final | Stage 4 close  | count(s2_ce_verdict=null) + count(s3_ce_verdict=null)
                   |                |   + count(s4_ce_verdict=null)

NULL TALLY CHAIN RULE — locked now:
  Per-stage verdicts accumulate as running tally from Stage 2 onward.
  Stage 4 close reconstructs full sequence: S2->[verdict], S3->[verdict], S4->[verdict].
  null_tally_final = sum of null slots.
  ATOMIC DUAL-LOCK at synthesis cross-checks Stage 4 running count against final chain.
  Mismatch = NULL TALLY CHAIN integrity failure — record before synthesis continues.

PRE-COMMITTED HANDOFF SCHEMA — locked now (11 fields, no additions, no omissions):

  FIELD                     | REQUIRED DERIVATION SOURCE
  --------------------------|-----------------------------------------------------------
  scout_anchor              | ROLE B scout load
  incumbent_threat_locked   | ROLE C analysis
  hypothesis                | Stage 1 artifact
  counter_hypothesis        | Stage 1 artifact
  s2_ce_verdict             | Stage 2 artifact
  s3_ce_verdict             | Stage 3 artifact
  s4_ce_verdict             | Stage 4 artifact
  null_tally_final          | Stage 4 close — derived from s2_ce_verdict + s3_ce_verdict
                            |   + s4_ce_verdict — independent of co_activation_confirmed
  co_activation_confirmed   | ATOMIC DUAL-LOCK — must equal dual_lock_fired or not_triggered
  incumbent_defense_closed  | Independent chain: s2->s3->s4 direct — not through
                            |   co_activation_confirmed
  confidence_composite      | Stage 5 synthesis — capped by SESSION INVARIANT B if
                            |   null_tally_final >= 3

GATE S field: invariant_registry_confirmed — required at GATE S Step 3.

---

## GATE S — PRE-HYPOTHESIS GATE

Clearance sequence mirrors the dependency chain: Step 1 (ROLE C complete) -> Step 2
(ROLE B complete) -> Step 3 (ROLE A complete). Each step depends on the prior.

  Step 1 — ROLE C (Step 1 of dependency chain): incumbent_threat_locked = [true / BLOCKED]
  Step 2 — ROLE B (Step 2 of dependency chain): gate_s_cleared = [true / BLOCKED]
  Step 3 — ROLE A (Step 3 of dependency chain): invariant_registry_confirmed = [true / BLOCKED]

  First step that fails: CAMPAIGN BLOCKED. Record which step and which role own the
  blocking field. Do not proceed to Stage 1.

---

## STAGE 1 — HYPOTHESIS

Entry condition: GATE S clearance sequence complete (all three steps confirmed).

Load the scout artifact named by ROLE B. Read its signals. Frame hypothesis.

  source_scout_artifact:        [repeat path from ROLE B — copied, not inferred]
  hypothesis:                   [clear falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C
                                  incumbent_strength and incumbent_vulnerability]
  gate_s_cleared:               [copy from GATE S Step 2 — must be true]
  invariant_registry_confirmed: [copy from ROLE A Step 3 — must be true]
  incumbent_threat_locked:      [copy from ROLE C Step 1 — must be true]

Write artifact: {topic}-hypothesis-{date}.md
Confirm write before advancing to Stage 2.

---

## STAGE 2 — WEB SEARCH

ENTRY CONDITIONS — all must confirm before body begins:
  [ ] Stage 1 EXIT confirmed: hypothesis artifact written
  [ ] gate_s_cleared = true (from GATE S)
  [ ] SESSION INVARIANT D Stage 2 template active and printed verbatim below:
      "Does [evidence item] support the displacement of {status_quo_comparator} by
       {topic} on [dimension]? [Yes / No / Inconclusive]"
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 2 BODY:
Gather minimum 3 external sources. For each item:
  - Record source URL or citation
  - Summarize finding in one sentence
  - Apply INCUMBENT CHECK

### INCUMBENT CHECK — Stage 2

Structural origin: ROLE C `incumbent_threat_locked` (confirmed at GATE S Step 1).

Template (SESSION INVARIANT D, Stage 2 — verbatim, fill bracketed slots only):
  "Does [evidence item] support the displacement of {status_quo_comparator} by
   {topic} on [dimension]? [Yes / No / Inconclusive]"

Apply verbatim to each evidence item:
  Item 1: "Does [item 1 description] support the displacement of {status_quo_comparator}
           by {topic} on [dimension]? [verdict]"
  Item 2: "Does [item 2 description] support the displacement of {status_quo_comparator}
           by {topic} on [dimension]? [verdict]"
  Item 3: "Does [item 3 description] support the displacement of {status_quo_comparator}
           by {topic} on [dimension]? [verdict]"

Any paraphrase of the template = SESSION INVARIANT D violation = format error.

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no counter-evidence; cite item if found]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-websearch-{date}.md
Confirm write before advancing to Stage 3.

---

## STAGE 3 — INTERVIEW

ENTRY CONDITIONS — all must confirm before body begins:
  [ ] Stage 2 EXIT confirmed: s2_ce_verdict recorded (not blank), artifact written
  [ ] Running null tally updated after Stage 2
  [ ] SESSION INVARIANT D Stage 3 template active and printed verbatim below:
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 3 BODY:
Simulate interviews with 2-3 practitioner types relevant to {topic}. For each:
  - Name practitioner type
  - Record key quote or paraphrase
  - Apply INCUMBENT CHECK

### INCUMBENT CHECK — Stage 3

Structural origin: ROLE C `incumbent_threat_locked` (confirmed at GATE S Step 1).

Template (SESSION INVARIANT D, Stage 3 — verbatim, fill bracketed slots only):
  "Does [practitioner account] reveal a viable transition path from
   {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"

Apply verbatim to each practitioner account:
  Account 1: "Does [account 1 summary] reveal a viable transition path from
              {status_quo_comparator} to {topic} for [use case]? [verdict]"
  Account 2: "Does [account 2 summary] reveal a viable transition path from
              {status_quo_comparator} to {topic} for [use case]? [verdict]"
  Account 3: "Does [account 3 summary] reveal a viable transition path from
              {status_quo_comparator} to {topic} for [use case]? [verdict]"

Any paraphrase of the template = SESSION INVARIANT D violation = format error.

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no counter-evidence; cite account if found]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-interview-{date}.md
Confirm write before advancing to Stage 4.

---

## STAGE 4 — PROTOTYPE

ENTRY CONDITIONS — all must confirm before body begins:
  [ ] Stage 3 EXIT confirmed: s3_ce_verdict recorded (not blank), artifact written
  [ ] Running null tally updated after Stage 3
  [ ] SESSION INVARIANT D Stage 4 template active and printed verbatim below:
      "Does [prototype result] make a credible case for displacing
       {status_quo_comparator} with {topic}? [Yes / No / Pending]"
      Displacement verdict (Yes / No / Pending) required. Omission = format error.
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 4 BODY:
Design and assess a minimal prototype or proof-of-concept for {topic}.

  prototype_design: [brief description of prototype or experiment]
  prototype_result: [what was learned — one to three sentences]

### INCUMBENT CHECK — Stage 4

Structural origin: ROLE C `incumbent_threat_locked` (confirmed at GATE S Step 1).

Template (SESSION INVARIANT D, Stage 4 — verbatim, fill bracketed slots only):
  "Does [prototype result] make a credible case for displacing
   {status_quo_comparator} with {topic}? [Yes / No / Pending]"

Apply verbatim:
  "Does [prototype_result summary] make a credible case for displacing
   {status_quo_comparator} with {topic}? [Yes / No / Pending]"

Displacement verdict is required. Omitting Yes / No / Pending = format error.
Any paraphrase of the template = SESSION INVARIANT D violation = format error.

  s4_displacement_verdict: [Yes / No / Pending]
  s4_ce_verdict:           [null if no counter-evidence; description if found]

Final null tally:
  null_tally_final = count(s2_ce_verdict=null) + count(s3_ce_verdict=null)
                       + count(s4_ce_verdict=null) = [N]
  Running count cross-check: "Running count from Stage 3 was [M]. Final after Stage 4
  is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-prototype-{date}.md
Confirm write before advancing to Stage 5.

---

## STAGE 5 — SYNTHESIS

Entry condition: Stage 4 EXIT confirmed (null_tally_final recorded, artifact written).

### COUNTER-HYPOTHESIS RESOLUTION

Resolve every counter_hypothesis declared at Stage 1:

  counter_hypothesis_1: [restate from Stage 1]
    verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
    evidence: [cite Stage 2, 3, or 4 artifact]
    confidence_effect: [OPEN RISK reduces confidence_composite one tier — record here]

Add row for each additional counter_hypothesis.
OPEN RISK verdicts must reduce confidence_composite before ATOMIC DUAL-LOCK fires.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [sum]
  Cross-check against Stage 4 running count: [Match / Mismatch — record if mismatch]

If null_tally_final >= 3:
  DUAL-LOCK fires. Both constraints activate simultaneously:
  Lock 1 — SESSION INVARIANT A: adversarial review by [adversarial_reviewer_type] required.
            Promotion to topic-story BLOCKED pending adversarial review.
  Lock 2 — SESSION INVARIANT B: confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired

If null_tally_final < 3:
  DUAL-LOCK does not fire.
  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:   [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:     [2-3 sentences integrating Stages 2, 3, 4]
  confidence_composite: [score after counter-hypothesis reductions and null-CE cap]
  key_risk:             [primary risk to adoption of {topic} over {status_quo_comparator}]

### HANDOFF BLOCK

All fields carry [derived from: X] per SESSION INVARIANT C.
Derivation annotations required on every field. Unlabeled field = format error.

  scout_anchor:              [value] [derived from: ROLE B scout load — Step 2 of chain]
  incumbent_threat_locked:   [true]  [derived from: ROLE C analysis — Step 1 of chain]
  hypothesis:                [value] [derived from: Stage 1 artifact]
  counter_hypothesis:        [value] [derived from: Stage 1 artifact]
  s2_ce_verdict:             [value] [derived from: Stage 2 artifact]
  s3_ce_verdict:             [value] [derived from: Stage 3 artifact]
  s4_ce_verdict:             [value] [derived from: Stage 4 artifact]
  null_tally_final:          [value] [derived from: s2_ce_verdict + s3_ce_verdict +
                                      s4_ce_verdict — independent of co_activation_confirmed]
                                      independence_chain: s2->s3->s4->null_tally_final
                                      (does not pass through ATOMIC DUAL-LOCK)
  co_activation_confirmed:   [value] [derived from: ATOMIC DUAL-LOCK — must equal
                                      dual_lock_fired or not_triggered]
                                      independence_chain: ATOMIC DUAL-LOCK path only —
                                      independent of incumbent_defense_closed
  incumbent_defense_closed:  [t/f]   [derived from: s2+s3+s4 CE verdicts direct chain]
                                      independence_chain: s2->s3->s4->incumbent_defense
                                      (does not pass through co_activation_confirmed)
  confidence_composite:      [value] [derived from: Stage 5 synthesis — reduced by OPEN
                                      RISK verdicts and capped by SESSION INVARIANT B]
  schema_compliance_confirmed:[true] [all 11 fields present, derivation sources match
                                      pre-committed schema from CAMPAIGN OPEN]

SYNTHESIS READINESS SIGNAL:
Evidence brief ready for topic-story.

Write artifact: {topic}-synthesis-{date}.md
Write artifact: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-02 — Axis: Output Format (Checklist-Dominant)

**Variation axis**: All structured metadata is expressed using [ ] checkbox lists rather
than tables or dense prose blocks. SESSION INVARIANTS are a numbered [ ] list with
enforcement consequence stated per item. ROLE definitions are expressed as confirmed [ ]
checklist items: filling a role's fields checks its box, and the box must be checked before
GATE S reads it. GATE S is a numbered [ ] clearance list. INCUMBENT CHECK at each stage is
a [ ] checklist where each item shows the verbatim template filled for that evidence item.

**Hypothesis**: Table-dominant formats (R13 V-02/V-05) compress structural metadata but
require wide lines and column alignment — difficult to read in terminals or narrow contexts.
Prose-heavy formats (R13 V-01/V-04) are readable but require pattern-matching to audit
completeness. Checklist-dominant format occupies a middle position: each [ ] item is
self-contained and visually countable, invariant enforcement language appears inline with
each item, and the template-per-evidence-item structure at INCUMBENT CHECK makes C-38
(verbatim template at execution) and C-39 (verbatim template at entry) auditable by
counting checked items rather than scanning tables or paragraphs.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Three roles run in sequence at CAMPAIGN OPEN. Five stages follow.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### SESSION INVARIANTS

Register all four. Check each box when complete.
All carry: pre-registered — cannot be modified or bypassed at any subsequent stage.

  [ ] SESSION INVARIANT A — ADVERSARIAL REVIEWER TYPE
        adversarial_reviewer_type: [role most likely to challenge the displacement claim]
        Activation: null_tally_final >= 3
        Consequence: adversarial review required — promotion BLOCKED until complete.

  [ ] SESSION INVARIANT B — CONFIDENCE CAP
        null_ce_cap_rule: confidence_composite -= 2 if null_tally_final >= 3 (hard cap)
        Consequence: cap applies at synthesis — cannot be softened or bypassed.

  [ ] SESSION INVARIANT C — DERIVATION ANNOTATION
        annotation_rule: Every handoff field must carry [derived from: X].
        Consequence: unlabeled handoff field = format error.

  [ ] SESSION INVARIANT D — INCUMBENT CHECK PHRASING REGISTER
        Stage 2 template (VERBATIM — no paraphrase permitted):
          "Does [evidence item] support the displacement of {status_quo_comparator}
           by {topic} on [dimension]? [Yes / No / Inconclusive]"
        Stage 3 template (VERBATIM — no paraphrase permitted):
          "Does [practitioner account] reveal a viable transition path from
           {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
        Stage 4 template (VERBATIM — no paraphrase permitted):
          "Does [prototype result] make a credible case for displacing
           {status_quo_comparator} with {topic}? [Yes / No / Pending]"
        TEMPLATE ECHO RULE: Print the stage template verbatim at each INCUMBENT CHECK
        execution point and at each stage's ENTRY CONDITIONS. Reference by name is
        insufficient — the text must appear at the point of use.
        Consequence: template deviation = SESSION INVARIANT D violation = format error.

All four boxes must be checked before ROLE C begins.

### ROLES

Roles execute in dependency order: C first, then B, then A.

  [ ] ROLE C — INCUMBENT THREAT ANALYST (execute first)
        Why first: the incumbent must be named before the scout artifact can be evaluated
        as relevant to the displacement case.
          incumbent_name:          [full name of status_quo_comparator]
          incumbent_strength:      [why the incumbent is currently winning — one sentence]
          incumbent_vulnerability: [where it is most exposed to {topic} — one sentence]
          incumbent_threat_locked: true  ← check this box when complete

  [ ] ROLE B — SCOUT LOADER (execute second)
        Why second: scout relevance can only be confirmed after the incumbent is named.
          scout_artifact:  [{topic}-scout-record-{date}.md or equivalent path]
          scout_loaded:    [true / false]
          gate_s_cleared:  [true if scout_loaded = true; CAMPAIGN BLOCKED otherwise]
        ← check this box when complete; if scout_loaded = false, do not proceed

  [ ] ROLE A — HYPOTHESIS ARCHITECT (execute third)
        Why third: invariant templates reference {status_quo_comparator} — the incumbent
        named in ROLE C — so registration depends on ROLE C completing first.
          invariant_registry_confirmed: true  ← check this box after all four SESSION
                                                INVARIANT boxes above are checked

All three role boxes must be checked before GATE S runs.

### CE VERDICT OWNERSHIP

  [ ] s2_ce_verdict    owned by Stage 2   — null if no CE; citation if found
  [ ] s3_ce_verdict    owned by Stage 3   — null if no CE; citation if found
  [ ] s4_ce_verdict    owned by Stage 4   — null if no CE; description if found
  [ ] null_tally_final owned by Stage 4 close — count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): running tally from Stage 2; reconstructed at synthesis;
ATOMIC DUAL-LOCK cross-checks; mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA

  [ ] scout_anchor              — derived from ROLE B scout load
  [ ] incumbent_threat_locked   — derived from ROLE C analysis
  [ ] hypothesis                — derived from Stage 1 artifact
  [ ] counter_hypothesis        — derived from Stage 1 artifact
  [ ] s2_ce_verdict             — derived from Stage 2 artifact
  [ ] s3_ce_verdict             — derived from Stage 3 artifact
  [ ] s4_ce_verdict             — derived from Stage 4 artifact
  [ ] null_tally_final          — derived from s2+s3+s4 CE verdicts (not through co_activation)
  [ ] co_activation_confirmed   — derived from ATOMIC DUAL-LOCK (not through incumbent_defense)
  [ ] incumbent_defense_closed  — derived from s2+s3+s4 direct chain (not through co_activation)
  [ ] confidence_composite      — derived from Stage 5 synthesis (capped by SESSION INVARIANT B)

11 fields. No additions. No omissions. Derivation-source mismatch = format error.

---

## GATE S — PRE-HYPOTHESIS GATE

Check each step in sequence:

  [ ] Step 1: ROLE C box checked — incumbent_threat_locked = true
  [ ] Step 2: ROLE B box checked — gate_s_cleared = true
  [ ] Step 3: ROLE A box checked — invariant_registry_confirmed = true

All three boxes must be checked. First unchecked box: CAMPAIGN BLOCKED.
Record which step failed and which role owns the blocking field.

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] GATE S: all three steps checked
  [ ] scout_artifact path available from ROLE B

STAGE 1 BODY:
Load the scout artifact. Read its signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — from ROLE C framing]
  gate_s_cleared:               true  [from GATE S Step 2]
  invariant_registry_confirmed: true  [from GATE S Step 3]
  incumbent_threat_locked:      true  [from GATE S Step 1]

  [ ] Write artifact: {topic}-hypothesis-{date}.md — check box when written
Advance to Stage 2 only after artifact write confirmed.

---

## STAGE 2 — WEB SEARCH

ENTRY CONDITIONS:
  [ ] Stage 1 artifact write confirmed
  [ ] SESSION INVARIANT D Stage 2 template active and printed verbatim:
      "Does [evidence item] support the displacement of {status_quo_comparator} by
       {topic} on [dimension]? [Yes / No / Inconclusive]"
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK — Stage 2:
Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).
Template (SESSION INVARIANT D, Stage 2 — VERBATIM, fill bracketed slots only):
  "Does [evidence item] support the displacement of {status_quo_comparator} by
   {topic} on [dimension]? [Yes / No / Inconclusive]"

  [ ] Item 1: Source [URL/citation] — [1-sentence summary]
              "Does [item 1] support the displacement of {status_quo_comparator}
               by {topic} on [dimension]? [verdict]"
  [ ] Item 2: Source [URL/citation] — [1-sentence summary]
              "Does [item 2] support the displacement of {status_quo_comparator}
               by {topic} on [dimension]? [verdict]"
  [ ] Item 3: Source [URL/citation] — [1-sentence summary]
              "Does [item 3] support the displacement of {status_quo_comparator}
               by {topic} on [dimension]? [verdict]"

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

  [ ] Write artifact: {topic}-websearch-{date}.md — check box when written
Advance to Stage 3 only after artifact write confirmed.

---

## STAGE 3 — INTERVIEW

ENTRY CONDITIONS:
  [ ] Stage 2 artifact write confirmed
  [ ] s2_ce_verdict recorded (not blank)
  [ ] SESSION INVARIANT D Stage 3 template active and printed verbatim:
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews. For each:
  - Name practitioner type
  - Record key quote or paraphrase

INCUMBENT CHECK — Stage 3:
Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).
Template (SESSION INVARIANT D, Stage 3 — VERBATIM, fill bracketed slots only):
  "Does [practitioner account] reveal a viable transition path from
   {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"

  [ ] Account 1: [practitioner type] — [key quote or paraphrase]
                 "Does [account 1 summary] reveal a viable transition path from
                  {status_quo_comparator} to {topic} for [use case]? [verdict]"
  [ ] Account 2: [practitioner type] — [key quote or paraphrase]
                 "Does [account 2 summary] reveal a viable transition path from
                  {status_quo_comparator} to {topic} for [use case]? [verdict]"
  [ ] Account 3: [practitioner type] — [key quote or paraphrase]
                 "Does [account 3 summary] reveal a viable transition path from
                  {status_quo_comparator} to {topic} for [use case]? [verdict]"

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

  [ ] Write artifact: {topic}-interview-{date}.md — check box when written
Advance to Stage 4 only after artifact write confirmed.

---

## STAGE 4 — PROTOTYPE

ENTRY CONDITIONS:
  [ ] Stage 3 artifact write confirmed
  [ ] s3_ce_verdict recorded (not blank)
  [ ] SESSION INVARIANT D Stage 4 template active and printed verbatim:
      "Does [prototype result] make a credible case for displacing
       {status_quo_comparator} with {topic}? [Yes / No / Pending]"
      Displacement verdict (Yes / No / Pending) required. Omission = format error.
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 4 BODY:
Design and assess a minimal prototype.

  prototype_design: [brief description]
  prototype_result: [what was learned — 1-3 sentences]

INCUMBENT CHECK — Stage 4:
Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).
Template (SESSION INVARIANT D, Stage 4 — VERBATIM, fill bracketed slots only):
  "Does [prototype result] make a credible case for displacing
   {status_quo_comparator} with {topic}? [Yes / No / Pending]"

  [ ] Prototype: [prototype_result summary]
                 "Does [prototype result] make a credible case for displacing
                  {status_quo_comparator} with {topic}? [Yes / No / Pending]"

  s4_displacement_verdict: [Yes / No / Pending]  ← required; omission = format error
  s4_ce_verdict:           [null if no CE; description if found]

Final null tally:
  null_tally_final = [N]  (s2 + s3 + s4 null count)
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

  [ ] Write artifact: {topic}-prototype-{date}.md — check box when written
Advance to Stage 5 only after artifact write confirmed.

---

## STAGE 5 — SYNTHESIS

ENTRY CONDITIONS:
  [ ] Stage 4 artifact write confirmed
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT boxes above confirmed checked

### COUNTER-HYPOTHESIS RESOLUTION

For each counter_hypothesis from Stage 1:

  [ ] counter_hypothesis_1: [restate]
        verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
        evidence: [cite Stage 2, 3, or 4 artifact]
        OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN:
  S2 -> [s2_ce_verdict]
  S3 -> [s3_ce_verdict]
  S4 -> [s4_ce_verdict]
  null_tally_final = [N]
  Cross-check vs Stage 4 count: [Match / Mismatch — explain if mismatch]

  [ ] If null_tally_final >= 3:
        Lock 1 (SESSION INVARIANT A): adversarial review required. BLOCKED.
        Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap).
        co_activation_confirmed: dual_lock_fired
  [ ] If null_tally_final < 3:
        co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:   [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:     [2-3 sentences integrating Stages 2, 3, 4]
  confidence_composite: [final value after all reductions]
  key_risk:             [primary adoption risk]

### HANDOFF BLOCK

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  [ ] scout_anchor:              [value] [derived from: ROLE B scout load]
  [ ] incumbent_threat_locked:   [true]  [derived from: ROLE C analysis]
  [ ] hypothesis:                [value] [derived from: Stage 1 artifact]
  [ ] counter_hypothesis:        [value] [derived from: Stage 1 artifact]
  [ ] s2_ce_verdict:             [value] [derived from: Stage 2 artifact]
  [ ] s3_ce_verdict:             [value] [derived from: Stage 3 artifact]
  [ ] s4_ce_verdict:             [value] [derived from: Stage 4 artifact]
  [ ] null_tally_final:          [value] [derived from: s2+s3+s4 CE verdicts]
                                          independence_chain: s2->s3->s4->null_tally_final
                                          (does not pass through co_activation_confirmed)
  [ ] co_activation_confirmed:   [value] [derived from: ATOMIC DUAL-LOCK]
                                          independence_chain: ATOMIC DUAL-LOCK only
  [ ] incumbent_defense_closed:  [t/f]   [derived from: s2+s3+s4 direct chain]
                                          independence_chain: s2->s3->s4->incumbent_defense
                                          (does not pass through co_activation_confirmed)
  [ ] confidence_composite:      [value] [derived from: Stage 5 synthesis]
  [ ] schema_compliance_confirmed:[true] [all 11 boxes checked, derivation sources match]

SYNTHESIS READINESS SIGNAL:
Evidence brief ready for topic-story.

  [ ] Write artifact: {topic}-synthesis-{date}.md
  [ ] Write artifact: {topic}-handoff-{date}.md
Check both boxes when written. Campaign complete.
```

---

## V-03 — Axis: Lifecycle Emphasis (Stage Validation Block)

**Variation axis**: After the stage body and before the EXIT SIGNAL, each evidence stage
(Stages 2, 3, and 4) includes a STAGE VALIDATION block — a post-execution checklist that
explicitly confirms the stage's structural obligations were met: (1) SESSION INVARIANT D
template was applied verbatim at INCUMBENT CHECK, not paraphrased; (2) CE verdict recorded
and not left blank; (3) artifact written. This sandwiches each evidence stage between
three enforcement sites: ENTRY CONDITIONS (pre-execution gate), INCUMBENT CHECK (mid-stage
execution), and STAGE VALIDATION (post-execution confirmation). The STAGE VALIDATION block
is distinct from the EXIT SIGNAL — EXIT SIGNAL names the stage outcome; VALIDATION
confirms structural compliance before the exit is issued.

**Hypothesis**: C-38 and C-39 together establish two structural enforcement sites per
stage: ENTRY CONDITIONS (template confirmed before entering) and INCUMBENT CHECK
(template printed at execution). Both are forward-looking obligations. Neither includes a
post-execution confirmation that the template was actually applied verbatim during execution
— the enforcement is declared before and at the moment of use, but no structural checkpoint
verifies compliance after. Adding a STAGE VALIDATION block creates a third site — a
post-execution audit before the EXIT SIGNAL allows the next stage to begin. A stage that
fails STAGE VALIDATION cannot issue its EXIT SIGNAL, blocking forward progress until
SESSION INVARIANT D compliance is confirmed. Three-site enforcement (entry gate, execution
echo, post-execution validation) closes the gap where entry and execution obligations are
present but execution compliance is never explicitly verified.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Each stage has ENTRY CONDITIONS, a BODY, a STAGE VALIDATION block, and an EXIT SIGNAL.
No stage issues its EXIT SIGNAL until STAGE VALIDATION confirms structural compliance.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### ROLES — execute in dependency order: C first, B second, A third

ROLE C — INCUMBENT THREAT ANALYST (execute first)
  Dependency: must resolve before ROLE B to establish what displacement means for this topic.
  Produces: incumbent_threat_locked (required by GATE S Step 1).
  INCUMBENT CHECK blocks at Stages 2, 3, 4 cite this field as structural origin.

    incumbent_name:          [full name of status_quo_comparator]
    incumbent_strength:      [one sentence: why the incumbent is currently winning]
    incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]
    incumbent_threat_locked: [true when all three fields above complete]

ROLE B — SCOUT LOADER (execute second)
  Dependency: must resolve after ROLE C — scout relevance requires the incumbent to be named.
  Produces: gate_s_cleared (required by GATE S Step 2).

    scout_artifact:  [{topic}-scout-record-{date}.md or equivalent path]
    scout_loaded:    [true / false]
    gate_s_cleared:  [true if scout_loaded = true; CAMPAIGN BLOCKED otherwise]

ROLE A — HYPOTHESIS ARCHITECT (execute third)
  Dependency: must resolve after ROLE B — invariant templates reference {status_quo_comparator}
  named in ROLE C; registration depends on the full C->B chain completing.
  Produces: invariant_registry_confirmed (required by GATE S Step 3).

SESSION INVARIANTS — locked now, cannot be modified or bypassed at any subsequent stage:

  SESSION INVARIANT A — ADVERSARIAL REVIEWER TYPE:
    adversarial_reviewer_type: [role most likely to challenge the displacement claim]
    Activation: null_tally_final >= 3
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

  SESSION INVARIANT B — CONFIDENCE CAP:
    null_ce_cap_rule: confidence_composite -= 2 if null_tally_final >= 3 (hard cap)
    Invariant language: locked formula — cannot be softened or overridden at synthesis.

  SESSION INVARIANT C — DERIVATION ANNOTATION:
    annotation_rule: Every handoff field must carry [derived from: X].
                     Unlabeled handoff field = format error.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

  SESSION INVARIANT D — INCUMBENT CHECK PHRASING REGISTER:
    Stage 2 template:
      "Does [evidence item] support the displacement of {status_quo_comparator} by
       {topic} on [dimension]? [Yes / No / Inconclusive]"
    Stage 3 template:
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
    Stage 4 template:
      "Does [prototype result] make a credible case for displacing
       {status_quo_comparator} with {topic}? [Yes / No / Pending]"
    TEMPLATE ECHO RULE: Template must be printed verbatim at each INCUMBENT CHECK execution
    point AND confirmed verbatim in ENTRY CONDITIONS before the stage begins.
    Post-execution: template application must be confirmed in STAGE VALIDATION before EXIT.
    Template deviation at any site = SESSION INVARIANT D violation = format error.
    Invariant language: pre-registered — cannot be modified or bypassed at any stage.

  invariant_registry_confirmed: [true after all four invariants registered]

CE VERDICT OWNERSHIP TABLE — locked now:

  FIELD            | OWNED BY       | FORMULA
  -----------------|----------------|--------------------------------------------------
  s2_ce_verdict    | Stage 2        | null if no CE; citation if found
  s3_ce_verdict    | Stage 3        | null if no CE; citation if found
  s4_ce_verdict    | Stage 4        | null if no CE; description if found
  null_tally_final | Stage 4 close  | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. ATOMIC DUAL-LOCK reconstructs
at synthesis. Mismatch = integrity failure.

PRE-COMMITTED HANDOFF SCHEMA — locked now (11 fields):

  FIELD                     | REQUIRED DERIVATION SOURCE
  --------------------------|-----------------------------------------------------------
  scout_anchor              | ROLE B scout load
  incumbent_threat_locked   | ROLE C analysis
  hypothesis                | Stage 1 artifact
  counter_hypothesis        | Stage 1 artifact
  s2_ce_verdict             | Stage 2 artifact
  s3_ce_verdict             | Stage 3 artifact
  s4_ce_verdict             | Stage 4 artifact
  null_tally_final          | s2+s3+s4 CE verdicts — independent of co_activation_confirmed
  co_activation_confirmed   | ATOMIC DUAL-LOCK — independent of incumbent_defense_closed
  incumbent_defense_closed  | s2+s3+s4 direct chain — not through co_activation_confirmed
  confidence_composite      | Stage 5 synthesis — capped by SESSION INVARIANT B

---

## GATE S — PRE-HYPOTHESIS GATE

Check in dependency order:

  Step 1 — ROLE C: incumbent_threat_locked = [true / BLOCKED — record ROLE C failure]
  Step 2 — ROLE B: gate_s_cleared = [true / BLOCKED — record ROLE B failure]
  Step 3 — ROLE A: invariant_registry_confirmed = [true / BLOCKED — record ROLE A failure]

If any step fails: CAMPAIGN BLOCKED. Do not proceed to Stage 1.

GATE EXIT: "GATE S clear — dependency chain C->B->A confirmed. Stage 1 ready."

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] GATE S exit confirmed: all three dependency chain steps checked
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D registered by ROLE A

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — from ROLE C framing]
  gate_s_cleared:               [true — carried from GATE S Step 2]
  invariant_registry_confirmed: [true — carried from GATE S Step 3]
  incumbent_threat_locked:      [true — carried from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked — artifact written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

ENTRY CONDITIONS:
  [ ] Stage 1 EXIT SIGNAL received: hypothesis_locked
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim — required at INCUMBENT CHECK):
      "Does [evidence item] support the displacement of {status_quo_comparator} by
       {topic} on [dimension]? [Yes / No / Inconclusive]"
      Template deviation = format error. Do not paraphrase.

STAGE 2 BODY:
Gather minimum 3 external sources. For each:
  - Record source URL or citation
  - Summarize finding in one sentence
  - Apply INCUMBENT CHECK

### INCUMBENT CHECK — Stage 2

Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).

Template (SESSION INVARIANT D, Stage 2 — VERBATIM, fill bracketed slots only):
  "Does [evidence item] support the displacement of {status_quo_comparator} by
   {topic} on [dimension]? [Yes / No / Inconclusive]"

Apply verbatim to each evidence item:
  Item 1: [source] — [summary]
    "Does [item 1] support the displacement of {status_quo_comparator}
     by {topic} on [dimension]? [verdict]"
  Item 2: [source] — [summary]
    "Does [item 2] support the displacement of {status_quo_comparator}
     by {topic} on [dimension]? [verdict]"
  Item 3: [source] — [summary]
    "Does [item 3] support the displacement of {status_quo_comparator}
     by {topic} on [dimension]? [verdict]"

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 VALIDATION:
  [ ] SESSION INVARIANT D template applied verbatim to all items — not paraphrased
      Confirm: "SESSION INVARIANT D Stage 2 template was printed verbatim above each
                item. Template text matches CAMPAIGN OPEN registration. No paraphrase."
  [ ] s2_ce_verdict recorded (null or citation — not blank)
  [ ] Artifact {topic}-websearch-{date}.md confirmed written
  VALIDATION RESULT: [PASS — proceed] / [FAIL — identify violation before exiting]

STAGE 2 EXIT SIGNAL: websearch_complete — issues only after STAGE 2 VALIDATION PASS
  "STAGE 2 EXIT: websearch_complete — validation passed. Tally: [N]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

ENTRY CONDITIONS:
  [ ] Stage 2 EXIT SIGNAL received: websearch_complete (validation passed)
  [ ] s2_ce_verdict recorded (not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim — required at INCUMBENT CHECK):
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
      Template deviation = format error. Do not paraphrase.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews. For each:
  - Name practitioner type
  - Record key quote or paraphrase

### INCUMBENT CHECK — Stage 3

Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).

Template (SESSION INVARIANT D, Stage 3 — VERBATIM, fill bracketed slots only):
  "Does [practitioner account] reveal a viable transition path from
   {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"

Apply verbatim to each practitioner account:
  Account 1: [practitioner type] — [key quote or paraphrase]
    "Does [account 1 summary] reveal a viable transition path from
     {status_quo_comparator} to {topic} for [use case]? [verdict]"
  Account 2: [practitioner type] — [key quote or paraphrase]
    "Does [account 2 summary] reveal a viable transition path from
     {status_quo_comparator} to {topic} for [use case]? [verdict]"
  Account 3: [practitioner type] — [key quote or paraphrase]
    "Does [account 3 summary] reveal a viable transition path from
     {status_quo_comparator} to {topic} for [use case]? [verdict]"

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 VALIDATION:
  [ ] SESSION INVARIANT D template applied verbatim to all accounts — not paraphrased
      Confirm: "SESSION INVARIANT D Stage 3 template was printed verbatim above each
                account. Template text matches CAMPAIGN OPEN registration. No paraphrase."
  [ ] s3_ce_verdict recorded (null or citation — not blank)
  [ ] Artifact {topic}-interview-{date}.md confirmed written
  VALIDATION RESULT: [PASS — proceed] / [FAIL — identify violation before exiting]

STAGE 3 EXIT SIGNAL: interview_complete — issues only after STAGE 3 VALIDATION PASS
  "STAGE 3 EXIT: interview_complete — validation passed. Tally: [N]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

ENTRY CONDITIONS:
  [ ] Stage 3 EXIT SIGNAL received: interview_complete (validation passed)
  [ ] s3_ce_verdict recorded (not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim — required at INCUMBENT CHECK):
      "Does [prototype result] make a credible case for displacing
       {status_quo_comparator} with {topic}? [Yes / No / Pending]"
      Displacement verdict (Yes / No / Pending) required. Omission = format error.
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 4 BODY:
Design and assess a minimal prototype.

  prototype_design: [brief description]
  prototype_result: [what was learned — 1-3 sentences]

### INCUMBENT CHECK — Stage 4

Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).

Template (SESSION INVARIANT D, Stage 4 — VERBATIM, fill bracketed slots only):
  "Does [prototype result] make a credible case for displacing
   {status_quo_comparator} with {topic}? [Yes / No / Pending]"

Apply verbatim:
  "Does [prototype_result summary] make a credible case for displacing
   {status_quo_comparator} with {topic}? [Yes / No / Pending]"

Displacement verdict (Yes / No / Pending) is required. Omission = format error.

  s4_displacement_verdict: [Yes / No / Pending]
  s4_ce_verdict:           [null if no CE; description if found]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 VALIDATION:
  [ ] SESSION INVARIANT D template applied verbatim — not paraphrased
      Confirm: "SESSION INVARIANT D Stage 4 template was printed verbatim above the
                prototype item. Template text matches CAMPAIGN OPEN registration.
                No paraphrase. Displacement verdict (Yes/No/Pending) is present."
  [ ] s4_displacement_verdict recorded (not blank)
  [ ] s4_ce_verdict recorded (null or description — not blank)
  [ ] null_tally_final computed and cross-checked against Stage 3 running count
  [ ] Artifact {topic}-prototype-{date}.md confirmed written
  VALIDATION RESULT: [PASS — proceed] / [FAIL — identify violation before exiting]

STAGE 4 EXIT SIGNAL: prototype_complete — issues only after STAGE 4 VALIDATION PASS
  "STAGE 4 EXIT: prototype_complete — validation passed. null_tally_final = [N].
   Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

ENTRY CONDITIONS:
  [ ] Stage 4 EXIT SIGNAL received: prototype_complete (validation passed)
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANTS active

### COUNTER-HYPOTHESIS RESOLUTION

For each counter_hypothesis from Stage 1:
  [restate] — verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  Evidence: [cite stage artifact]
  OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 validation count: [Match / Mismatch — record if mismatch]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review required. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:   [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:     [2-3 sentences integrating Stages 2, 3, 4]
  confidence_composite: [final value after all reductions]
  key_risk:             [primary adoption risk]

### HANDOFF BLOCK

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  scout_anchor:              [value] [derived from: ROLE B scout load]
  incumbent_threat_locked:   [true]  [derived from: ROLE C analysis]
  hypothesis:                [value] [derived from: Stage 1 artifact]
  counter_hypothesis:        [value] [derived from: Stage 1 artifact]
  s2_ce_verdict:             [value] [derived from: Stage 2 artifact]
  s3_ce_verdict:             [value] [derived from: Stage 3 artifact]
  s4_ce_verdict:             [value] [derived from: Stage 4 artifact]
  null_tally_final:          [value] [derived from: s2+s3+s4 CE verdicts]
                                      independence_chain: s2->s3->s4->null_tally_final
                                      (does not pass through co_activation_confirmed)
  co_activation_confirmed:   [value] [derived from: ATOMIC DUAL-LOCK]
                                      independence_chain: ATOMIC DUAL-LOCK only
  incumbent_defense_closed:  [t/f]   [derived from: s2+s3+s4 direct chain]
                                      independence_chain: s2->s3->s4->incumbent_defense
                                      (does not pass through co_activation_confirmed)
  confidence_composite:      [value] [derived from: Stage 5 synthesis]
  schema_compliance_confirmed:[true] [all 11 fields present, derivation sources match]

SYNTHESIS READINESS SIGNAL:
Evidence brief ready for topic-story.

Write artifact: {topic}-synthesis-{date}.md
Write artifact: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-04 — Combined: Phrasing Register + Inertia Framing (Threat Register as Vocabulary Anchor)

**Variation axis**: CAMPAIGN OPEN opens with a THREAT REGISTER — a four-field structured
block (incumbent_name, incumbent_strength, incumbent_vulnerability, incumbent_moat) that
establishes the competitive landscape before any invariant is registered. SESSION INVARIANT
D is the first invariant registered after the THREAT REGISTER and explicitly references
THREAT REGISTER field names in its variable slot annotations: `[dimension]` in the Stage 2
template maps to incumbent_vulnerability fields; `[use case]` in Stage 3 maps to known
incumbent strongholds. Each INCUMBENT CHECK block prints the template verbatim AND cites
which THREAT REGISTER field the displacement question is probing. Inertia framing is
reinforced by opening CAMPAIGN OPEN with incumbent strength/moat before any claim about
{topic} is framed. Roles still execute C->B->A but ROLE C reads the THREAT REGISTER
rather than producing its own fields — the THREAT REGISTER becomes the shared source
for both ROLE C's locked field and SESSION INVARIANT D's vocabulary anchor.

**Hypothesis**: SESSION INVARIANT D in prior variations declares abstract template slots
(`[dimension]`, `[use case]`) without grounding them in specific incumbent knowledge.
A practitioner filling the Stage 2 template must independently decide what "dimension" is
relevant for comparing {topic} to {status_quo_comparator}. The THREAT REGISTER pre-loads
this decision: `[dimension]` is drawn from `incumbent_vulnerability` and
`incumbent_strength` fields registered before any stage begins. SESSION INVARIANT D
declares templates whose slots already have known candidates — the phrasing register is
grounded, not abstract. This should strengthen C-38/C-39 fidelity because each verbatim
echo of the template is also an echo of the THREAT REGISTER's vocabulary, not just
invariant syntax.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Inertia is the default. Evidence must overcome it.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### THREAT REGISTER

Fill before registering any invariant or executing any role.
This block grounds the displacement-question vocabulary for the entire campaign.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning —
                             this is the key dimension {topic} must overcome]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed —
                             this is the primary dimension to probe in evidence stages]
  incumbent_moat:          [one sentence: the switching cost or lock-in that protects
                             the incumbent — what makes displacement hard]

The THREAT REGISTER is read by ROLE C to produce `incumbent_threat_locked` and by
SESSION INVARIANT D to ground its template variable slots. Clearing the THREAT REGISTER
before ROLE C executes ensures both ROLE C and SESSION INVARIANT D share the same
vocabulary foundation.

---

### SESSION INVARIANT D — INCUMBENT CHECK PHRASING REGISTER

Register first. Grounds all INCUMBENT CHECK blocks across the campaign.
Invariant language: pre-registered — cannot be modified or bypassed at any stage.

The templates below use THREAT REGISTER fields as vocabulary anchors for variable slots.
`[dimension]` in Stage 2 draws from incumbent_vulnerability or incumbent_strength.
`[use case]` in Stage 3 draws from incumbent_moat or known incumbent strongholds.
Variable slots must be filled — the THREAT REGISTER fields above are the source.

TEMPLATE ECHO RULE: Print the stage-specific template verbatim at ENTRY CONDITIONS for
each evidence stage AND immediately before applying it at each INCUMBENT CHECK block.
Reference by name without printing the full text = PARTIAL compliance only.
Consequence: template deviation = SESSION INVARIANT D violation = format error.

  STAGE 2 TEMPLATE (web search — verbatim):
    "Does [evidence item] support the displacement of {status_quo_comparator} by {topic}
     on [dimension — from THREAT REGISTER]? [Yes / No / Inconclusive]"
    Variable slot guide: [evidence item] = source name or finding; [dimension] = which
    THREAT REGISTER field (incumbent_vulnerability or incumbent_strength) this source
    speaks to.

  STAGE 3 TEMPLATE (interview — verbatim):
    "Does [practitioner account] reveal a viable transition path from
     {status_quo_comparator} to {topic} for [use case — from THREAT REGISTER]?
     [Yes / No / Inconclusive]"
    Variable slot guide: [practitioner account] = one-sentence account summary;
    [use case] = which THREAT REGISTER stronghold or moat context applies.

  STAGE 4 TEMPLATE (prototype — verbatim):
    "Does [prototype result] make a credible case for displacing {status_quo_comparator}
     with {topic}? [Yes / No / Pending]"
    Note: Stage 4 template requires an explicit verdict token. Omission = format error
    independent of SESSION INVARIANT D compliance.

### SESSION INVARIANT A — ADVERSARIAL REVIEWER TYPE

  adversarial_reviewer_type: [role most likely to challenge the displacement claim —
                               should be someone who knows incumbent_moat well]
  Activation: null_tally_final >= 3
  Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

### SESSION INVARIANT B — CONFIDENCE CAP

  null_ce_cap_rule: confidence_composite -= 2 if null_tally_final >= 3 (hard cap)
  Invariant language: locked formula — cannot be softened or overridden at synthesis.

### SESSION INVARIANT C — DERIVATION ANNOTATION

  annotation_rule: Every handoff field must carry [derived from: X].
                   Unlabeled handoff field = format error.
  Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

---

### ROLES — execute in dependency order C -> B -> A

ROLE C — INCUMBENT THREAT ANALYST (execute first)
  Reads THREAT REGISTER above. Confirms analysis complete.
  Why first: ROLE C establishes the displacement target before ROLE B evaluates the scout.
  Without ROLE C completing, ROLE B cannot assess whether the scout addresses the
  right incumbent.

    incumbent_threat_locked: [true when THREAT REGISTER complete and ROLE C satisfied]

  GATE S Step 1: incumbent_threat_locked must be true.
  INCUMBENT CHECK blocks at Stages 2, 3, 4 cite ROLE C `incumbent_threat_locked` as
  structural origin — and cite the THREAT REGISTER field that grounds the template slot.

ROLE B — SCOUT LOADER (execute second)
  Why second: scout relevance is evaluated against the incumbent ROLE C named.
    scout_artifact:  [{topic}-scout-record-{date}.md or equivalent path]
    scout_loaded:    [true / false]
    gate_s_cleared:  [true if scout_loaded = true; CAMPAIGN BLOCKED otherwise]

  GATE S Step 2: gate_s_cleared must be true.

ROLE A — HYPOTHESIS ARCHITECT (execute third)
  Why third: invariant templates reference THREAT REGISTER vocabulary — registration
  depends on the THREAT REGISTER being filled and ROLE C confirming it.

    invariant_registry_confirmed: [true when all four SESSION INVARIANTS registered]

  GATE S Step 3: invariant_registry_confirmed must be true.

CE VERDICT OWNERSHIP TABLE — locked now:

  FIELD            | OWNED BY       | FORMULA
  -----------------|----------------|--------------------------------------------------
  s2_ce_verdict    | Stage 2        | null if no CE; citation if found
  s3_ce_verdict    | Stage 3        | null if no CE; citation if found
  s4_ce_verdict    | Stage 4        | null if no CE; description if found
  null_tally_final | Stage 4 close  | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): running tally from Stage 2; ATOMIC DUAL-LOCK reconstructs
at synthesis; mismatch = integrity failure.

PRE-COMMITTED HANDOFF SCHEMA — locked now (11 fields):

  FIELD                     | REQUIRED DERIVATION SOURCE
  --------------------------|-----------------------------------------------------------
  scout_anchor              | ROLE B scout load
  incumbent_threat_locked   | ROLE C analysis (reads THREAT REGISTER)
  hypothesis                | Stage 1 artifact
  counter_hypothesis        | Stage 1 artifact
  s2_ce_verdict             | Stage 2 artifact
  s3_ce_verdict             | Stage 3 artifact
  s4_ce_verdict             | Stage 4 artifact
  null_tally_final          | s2+s3+s4 CE verdicts — independent of co_activation_confirmed
  co_activation_confirmed   | ATOMIC DUAL-LOCK — independent of incumbent_defense_closed
  incumbent_defense_closed  | s2+s3+s4 direct chain — not through co_activation_confirmed
  confidence_composite      | Stage 5 synthesis — capped by SESSION INVARIANT B

---

## GATE S — PRE-HYPOTHESIS GATE

Clearance sequence C -> B -> A (dependency order):

  Step 1 — ROLE C: incumbent_threat_locked = [true / BLOCKED]
  Step 2 — ROLE B: gate_s_cleared = [true / BLOCKED]
  Step 3 — ROLE A: invariant_registry_confirmed = [true / BLOCKED]

First failure: CAMPAIGN BLOCKED. Record step and owning role. Do not proceed.

---

## STAGE 1 — HYPOTHESIS

Entry condition: GATE S all three steps confirmed.

Load scout artifact named by ROLE B. Read signals. Frame hypothesis against the
THREAT REGISTER incumbent — the counter_hypothesis should reflect incumbent_moat
as the strongest defense.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in THREAT REGISTER:
                                  why incumbent_moat makes displacement difficult]
  gate_s_cleared:               [true — from GATE S Step 2]
  invariant_registry_confirmed: [true — from GATE S Step 3]
  incumbent_threat_locked:      [true — from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md
Confirm write before Stage 2.

---

## STAGE 2 — WEB SEARCH

ENTRY CONDITIONS:
  [ ] Stage 1 artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim — from CAMPAIGN OPEN):
      "Does [evidence item] support the displacement of {status_quo_comparator} by {topic}
       on [dimension — from THREAT REGISTER]? [Yes / No / Inconclusive]"
      For this campaign, [dimension] candidates: {incumbent_vulnerability}, {incumbent_strength}.
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 2 BODY:
Gather minimum 3 external sources. Focus on THREAT REGISTER dimensions.

For each item:
  - Record source URL or citation
  - Summarize finding in one sentence

### INCUMBENT CHECK — Stage 2

Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).
THREAT REGISTER field probed: [which of incumbent_vulnerability / incumbent_strength
this item speaks to — name the THREAT REGISTER field]

Template (SESSION INVARIANT D, Stage 2 — VERBATIM, fill bracketed slots only):
  "Does [evidence item] support the displacement of {status_quo_comparator} by {topic}
   on [dimension — from THREAT REGISTER]? [Yes / No / Inconclusive]"

Apply verbatim to each evidence item:
  Item 1: [source] — [summary] — THREAT REGISTER field: [field name]
    "Does [item 1] support the displacement of {status_quo_comparator} by {topic}
     on [dimension from THREAT REGISTER]? [verdict]"
  Item 2: [source] — [summary] — THREAT REGISTER field: [field name]
    "Does [item 2] support the displacement of {status_quo_comparator} by {topic}
     on [dimension from THREAT REGISTER]? [verdict]"
  Item 3: [source] — [summary] — THREAT REGISTER field: [field name]
    "Does [item 3] support the displacement of {status_quo_comparator} by {topic}
     on [dimension from THREAT REGISTER]? [verdict]"

Any paraphrase of the template = SESSION INVARIANT D violation = format error.

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-websearch-{date}.md. Confirm before Stage 3.

---

## STAGE 3 — INTERVIEW

ENTRY CONDITIONS:
  [ ] Stage 2 artifact confirmed written
  [ ] s2_ce_verdict recorded (not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim — from CAMPAIGN OPEN):
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case — from THREAT REGISTER]?
       [Yes / No / Inconclusive]"
      For this campaign, [use case] candidates: contexts where incumbent_moat is strongest.
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews. Focus on contexts where incumbent_moat applies.

### INCUMBENT CHECK — Stage 3

Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).
THREAT REGISTER field probed: [which of incumbent_moat / incumbent_strength this
account speaks to — name the THREAT REGISTER field]

Template (SESSION INVARIANT D, Stage 3 — VERBATIM, fill bracketed slots only):
  "Does [practitioner account] reveal a viable transition path from
   {status_quo_comparator} to {topic} for [use case — from THREAT REGISTER]?
   [Yes / No / Inconclusive]"

Apply verbatim to each account:
  Account 1: [practitioner type] — [key quote] — THREAT REGISTER field: [field name]
    "Does [account 1 summary] reveal a viable transition path from
     {status_quo_comparator} to {topic} for [use case from THREAT REGISTER]? [verdict]"
  Account 2: [practitioner type] — [key quote] — THREAT REGISTER field: [field name]
    "Does [account 2 summary] reveal a viable transition path from
     {status_quo_comparator} to {topic} for [use case from THREAT REGISTER]? [verdict]"
  Account 3: [practitioner type] — [key quote] — THREAT REGISTER field: [field name]
    "Does [account 3 summary] reveal a viable transition path from
     {status_quo_comparator} to {topic} for [use case from THREAT REGISTER]? [verdict]"

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-interview-{date}.md. Confirm before Stage 4.

---

## STAGE 4 — PROTOTYPE

ENTRY CONDITIONS:
  [ ] Stage 3 artifact confirmed written
  [ ] s3_ce_verdict recorded (not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim — from CAMPAIGN OPEN):
      "Does [prototype result] make a credible case for displacing {status_quo_comparator}
       with {topic}? [Yes / No / Pending]"
      Displacement verdict (Yes / No / Pending) required. Omission = format error.
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 4 BODY:
Design and assess a minimal prototype. The prototype should probe incumbent_vulnerability
or attempt to demonstrate displacement in a context where incumbent_moat is present.

  prototype_design: [brief description — which THREAT REGISTER dimension does it test?]
  prototype_result: [what was learned — 1-3 sentences]

### INCUMBENT CHECK — Stage 4

Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).
THREAT REGISTER field probed: incumbent_vulnerability (displacement case) and
incumbent_moat (displacement difficulty).

Template (SESSION INVARIANT D, Stage 4 — VERBATIM, fill bracketed slots only):
  "Does [prototype result] make a credible case for displacing {status_quo_comparator}
   with {topic}? [Yes / No / Pending]"

Apply verbatim:
  "Does [prototype_result summary] make a credible case for displacing
   {status_quo_comparator} with {topic}? [Yes / No / Pending]"

Displacement verdict (Yes / No / Pending) required. Omission = format error.
Any paraphrase = SESSION INVARIANT D violation = format error.

  s4_displacement_verdict: [Yes / No / Pending]
  s4_ce_verdict:           [null if no CE; description if found]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-prototype-{date}.md. Confirm before Stage 5.

---

## STAGE 5 — SYNTHESIS

Entry condition: Stage 4 artifact confirmed written, null_tally_final recorded.

### COUNTER-HYPOTHESIS RESOLUTION

Resolve every counter_hypothesis from Stage 1 (which should reflect incumbent_moat):

  counter_hypothesis_1: [restate — which THREAT REGISTER moat does this reflect?]
    verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
    evidence: [cite Stage 2, 3, or 4 artifact and THREAT REGISTER field it addresses]
    confidence_effect: [OPEN RISK reduces confidence_composite one tier — record here]

OPEN RISK verdicts reduce confidence_composite before ATOMIC DUAL-LOCK fires.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 count: [Match / Mismatch — record if mismatch]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type] required.
            Reviewer should know {status_quo_comparator} incumbent_moat deeply.
            Promotion BLOCKED pending adversarial review.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:   [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:     [2-3 sentences — reference THREAT REGISTER framing: does evidence
                          address incumbent_vulnerability and overcome incumbent_moat?]
  confidence_composite: [final value after all reductions]
  key_risk:             [primary adoption risk — should name incumbent_moat as the
                          residual challenge even if hypothesis is SUPPORTED]

### HANDOFF BLOCK

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  scout_anchor:              [value] [derived from: ROLE B scout load]
  incumbent_threat_locked:   [true]  [derived from: ROLE C reading THREAT REGISTER]
  hypothesis:                [value] [derived from: Stage 1 artifact]
  counter_hypothesis:        [value] [derived from: Stage 1 artifact — reflects
                                      THREAT REGISTER incumbent_moat framing]
  s2_ce_verdict:             [value] [derived from: Stage 2 artifact]
  s3_ce_verdict:             [value] [derived from: Stage 3 artifact]
  s4_ce_verdict:             [value] [derived from: Stage 4 artifact]
  null_tally_final:          [value] [derived from: s2+s3+s4 CE verdicts]
                                      independence_chain: s2->s3->s4->null_tally_final
                                      (does not pass through co_activation_confirmed)
  co_activation_confirmed:   [value] [derived from: ATOMIC DUAL-LOCK]
                                      independence_chain: ATOMIC DUAL-LOCK only
  incumbent_defense_closed:  [t/f]   [derived from: s2+s3+s4 direct chain]
                                      independence_chain: s2->s3->s4->incumbent_defense
                                      (does not pass through co_activation_confirmed)
  confidence_composite:      [value] [derived from: Stage 5 synthesis]
  schema_compliance_confirmed:[true] [all 11 fields present, derivation sources match]

SYNTHESIS READINESS SIGNAL:
Evidence brief ready for topic-story.

Write artifact: {topic}-synthesis-{date}.md
Write artifact: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-05 — Combined: Role Sequence + Checklist Format + Stage Validation + Threat Register

**Variation axis**: All four axes combined. CAMPAIGN OPEN opens with a THREAT REGISTER
(V-04 inertia framing). SESSION INVARIANT D leads the invariant block with THREAT REGISTER
field annotations on variable slots (V-04 phrasing register). Roles are declared in C->B->A
dependency order with numbered "STEP N OF 3" headers citing the dependency rationale (V-01
role sequence). Role confirmation uses [ ] checkbox lists; GATE S, ENTRY CONDITIONS, and
STAGE VALIDATION use [ ] checklists (V-02 checklist format). Each evidence stage has
ENTRY CONDITIONS (with verbatim SESSION INVARIANT D template), an INCUMBENT CHECK body
(with verbatim template re-echo), a STAGE VALIDATION block (post-execution compliance
confirmation), and an EXIT SIGNAL (V-03 lifecycle emphasis). The combination tests whether
maximum structural density satisfies C-37/C-38/C-39 across all three enforcement sites —
entry gate, execution echo, post-execution validation — while remaining readable.

**Hypothesis**: Each prior variation made one structural trade-off: V-01 adds rationale text;
V-02 is compact but may lose narrative; V-03 adds validation overhead; V-04 grounds
vocabulary but adds THREAT REGISTER fields. Combined, these axes should produce a prompt
where C-37 (dependency order readable from role declaration), C-38 (template at execution
point), and C-39 (template at both gate and execution) are each enforced at multiple
structural sites simultaneously: ROLE TABLE encodes C-37; ENTRY CONDITIONS + INCUMBENT
CHECK + STAGE VALIDATION each enforce C-38/C-39 at different moments. A reviewer can
audit any criterion by inspecting a single named structural component.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Inertia is the default. Evidence must overcome it.
Six stages: Stage 0 (gate), Stages 1-5 (evidence + synthesis).
Each stage has ENTRY CONDITIONS, BODY, VALIDATION, and EXIT SIGNAL in sequence.
No stage exits until VALIDATION confirms structural compliance.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### THREAT REGISTER

Fill before any invariant registration or role execution.
Grounds displacement-question vocabulary for the full campaign.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]
  incumbent_moat:          [one sentence: switching cost or lock-in protecting the incumbent]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. Register all four before roles execute.
All carry: pre-registered — cannot be modified or bypassed at any subsequent stage.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|-------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2 (VERBATIM):
       | REGISTER                  |   "Does [evidence item] support the displacement of
       |                           |   {status_quo_comparator} by {topic} on
       |                           |   [dimension — from THREAT REGISTER]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 3 (VERBATIM):
       |                           |   "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator}
       |                           |   to {topic} for [use case — from THREAT REGISTER]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 4 (VERBATIM):
       |                           |   "Does [prototype result] make a credible case for
       |                           |   displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending]"
       |                           | TEMPLATE ECHO RULE: Print verbatim at ENTRY
       |                           | CONDITIONS AND at INCUMBENT CHECK block AND confirm
       |                           | verbatim in STAGE VALIDATION. Three enforcement sites.
       |                           | Deviation at any site = format error.
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|-------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the claim — should know incumbent_moat].
       |                           | Activation: null_tally_final >= 3.
       |                           | Cannot be modified or bypassed at synthesis.
  -----|---------------------------|-------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap, not softened).
       |                           | Cannot be softened or overridden at synthesis.
  -----|---------------------------|-------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | Cannot be modified or bypassed at synthesis.

### ROLE OWNERSHIP TABLE

Roles execute in dependency order: C first, B second, A third.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C execution (STEP 1 OF 3):
  Why first: ROLE C names what must be displaced before ROLE B can evaluate the scout.
  Reads THREAT REGISTER. Confirms analysis complete.
  [ ] incumbent_threat_locked: true  (set when THREAT REGISTER complete and ROLE C satisfied)

ROLE B execution (STEP 2 OF 3):
  Why second: scout relevance requires the incumbent to be named first (ROLE C Step 1).
  [ ] scout_artifact:  [{topic}-scout-record-{date}.md or equivalent path]
  [ ] scout_loaded:    [true / false]
  [ ] gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED if false]

ROLE A execution (STEP 3 OF 3):
  Why third: invariant templates reference THREAT REGISTER vocabulary (named by ROLE C).
  Confirms all four SESSION INVARIANT TABLE rows filled and active.
  [ ] invariant_registry_confirmed: true  (set when all four invariant rows checked)

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY       | FORMULA
  -----------------|----------------|--------------------------------------------------
  s2_ce_verdict    | Stage 2        | null if no CE; citation if found
  s3_ce_verdict    | Stage 3        | null if no CE; citation if found
  s4_ce_verdict    | Stage 4        | null if no CE; description if found
  null_tally_final | Stage 4 close  | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): running tally from Stage 2; reconstructed in ATOMIC
DUAL-LOCK; Stage 4 running count cross-checked; mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis (reads THREAT REGISTER)   | n/a
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
  confidence_composite       | Stage 5 minus reductions                  | capped by INV B

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] THREAT REGISTER complete (all four fields filled)
  [ ] SESSION INVARIANTS TABLE complete (all four rows filled, INV D templates registered)
  [ ] ROLE C executed — incumbent_threat_locked box checked
  [ ] ROLE B executed — gate_s_cleared box checked (scout_loaded = true required)
  [ ] ROLE A executed — invariant_registry_confirmed box checked

STAGE 0 BODY — CLEARANCE TABLE:

  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 VALIDATION:
  [ ] All three CLEARANCE TABLE results = confirm
  VALIDATION RESULT: [PASS] / [BLOCKED — record which step]

STAGE 0 EXIT SIGNAL: gate_open (issues only after VALIDATION PASS)
  "STAGE 0 EXIT: gate_open — dependency chain C->B->A confirmed. SESSION INVARIANT D
   active. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B (STEP 2 of dependency chain)
  [ ] SESSION INVARIANT D templates registered (confirmed by ROLE A at GATE S Step 3)

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis against THREAT REGISTER incumbent.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — reflects THREAT REGISTER
                                  incumbent_moat as primary challenge to displacement]
  gate_s_cleared:               true  [from GATE S Step 2]
  invariant_registry_confirmed: true  [from GATE S Step 3]
  incumbent_threat_locked:      true  [from GATE S Step 1]

STAGE 1 VALIDATION:
  [ ] hypothesis declared (falsifiable claim present)
  [ ] counter_hypothesis declared (references THREAT REGISTER incumbent_moat)
  [ ] gate fields (gate_s_cleared, invariant_registry_confirmed, incumbent_threat_locked)
      all carry true from GATE S
  VALIDATION RESULT: [PASS] / [FAIL — identify gap before exiting]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked (issues only after VALIDATION PASS)
  "STAGE 1 EXIT: hypothesis_locked — artifact written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim — from TABLE ROW D):
      "Does [evidence item] support the displacement of {status_quo_comparator} by {topic}
       on [dimension — from THREAT REGISTER]? [Yes / No / Inconclusive]"
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 2 BODY:
Gather minimum 3 external sources. Focus evidence on THREAT REGISTER dimensions.

INCUMBENT CHECK TABLE — Stage 2:
Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).
SESSION INVARIANT D Stage 2 template (VERBATIM — fill bracketed slots only):
  "Does [evidence item] support the displacement of {status_quo_comparator} by {topic}
   on [dimension — from THREAT REGISTER]? [Yes / No / Inconclusive]"

  ITEM | SOURCE           | SUMMARY (1 sentence) | THREAT REGISTER FIELD | TEMPLATE APPLIED
  -----|------------------|----------------------|-----------------------|------------------
  1    | [URL/citation]   | [summary]            | [TR field name]       | "Does [item 1]
  2    | [URL/citation]   | [summary]            | [TR field name]       |  support the
  3    | [URL/citation]   | [summary]            | [TR field name]       |  displacement of
  add  |                  |                      |                       |  {sq} by {topic}
       |                  |                      |                       |  on [dim]?
       |                  |                      |                       |  [verdict]"

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 VALIDATION:
  [ ] SESSION INVARIANT D Stage 2 template printed verbatim in INCUMBENT CHECK table
      header above — text matches TABLE ROW D declaration. No paraphrase.
      Confirm: "Template text in INCUMBENT CHECK matches CAMPAIGN OPEN registration."
  [ ] SESSION INVARIANT D Stage 2 template was also present in ENTRY CONDITIONS above
      (gate obligation confirmed).
  [ ] s2_ce_verdict recorded (not blank)
  [ ] Artifact {topic}-websearch-{date}.md confirmed written
  VALIDATION RESULT: [PASS — template at entry and execution confirmed] /
                     [FAIL — identify site where template was absent or paraphrased]

STAGE 2 EXIT SIGNAL: websearch_complete (issues only after VALIDATION PASS)
  "STAGE 2 EXIT: websearch_complete — template compliance confirmed at entry and
   execution. s2_ce_verdict = [value]. Tally: [N]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete (validation passed)
  [ ] s2_ce_verdict recorded (not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (verbatim — from TABLE ROW D):
      "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case — from THREAT REGISTER]?
       [Yes / No / Inconclusive]"
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 3 BODY:
Simulate 2-3 practitioner interviews. Focus on contexts where incumbent_moat applies.

INCUMBENT CHECK TABLE — Stage 3:
Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).
SESSION INVARIANT D Stage 3 template (VERBATIM — fill bracketed slots only):
  "Does [practitioner account] reveal a viable transition path from
   {status_quo_comparator} to {topic} for [use case — from THREAT REGISTER]?
   [Yes / No / Inconclusive]"

  PRACTITIONER     | KEY ACCOUNT (1 sentence)    | TR FIELD    | TEMPLATE APPLIED
  -----------------|-----------------------------|-------------|------------------
  [type 1]         | [quote or paraphrase]       | [TR field]  | "Does [account 1]
  [type 2]         | [quote or paraphrase]       | [TR field]  |  reveal a viable
  [type 3]         | [quote or paraphrase]       | [TR field]  |  transition path
  add rows         |                             |             |  from {sq} to
                   |                             |             |  {topic} for
                   |                             |             |  [use case]?
                   |                             |             |  [verdict]"

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 VALIDATION:
  [ ] SESSION INVARIANT D Stage 3 template printed verbatim in INCUMBENT CHECK table
      header above — text matches TABLE ROW D declaration. No paraphrase.
      Confirm: "Template text in INCUMBENT CHECK matches CAMPAIGN OPEN registration."
  [ ] SESSION INVARIANT D Stage 3 template was also present in ENTRY CONDITIONS above
      (gate obligation confirmed).
  [ ] s3_ce_verdict recorded (not blank)
  [ ] Artifact {topic}-interview-{date}.md confirmed written
  VALIDATION RESULT: [PASS — template at entry and execution confirmed] /
                     [FAIL — identify site where template was absent or paraphrased]

STAGE 3 EXIT SIGNAL: interview_complete (issues only after VALIDATION PASS)
  "STAGE 3 EXIT: interview_complete — template compliance confirmed at entry and
   execution. s3_ce_verdict = [value]. Tally: [N]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete (validation passed)
  [ ] s3_ce_verdict recorded (not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (verbatim — from TABLE ROW D):
      "Does [prototype result] make a credible case for displacing {status_quo_comparator}
       with {topic}? [Yes / No / Pending]"
      Displacement verdict (Yes / No / Pending) required. Omission = format error.
      Template deviation = SESSION INVARIANT D violation = format error.

STAGE 4 BODY:
Design and assess a minimal prototype. Probe THREAT REGISTER dimensions directly.

  prototype_design: [brief description — which TR field does it test?]
  prototype_result: [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4:
Structural origin: ROLE C `incumbent_threat_locked` (GATE S Step 1).
SESSION INVARIANT D Stage 4 template (VERBATIM — fill bracketed slots only):
  "Does [prototype result] make a credible case for displacing {status_quo_comparator}
   with {topic}? [Yes / No / Pending]"

  ITEM       | PROTOTYPE RESULT (1 sentence) | TR FIELD    | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------|------------------------------
  prototype  | [prototype_result]            | [TR field]  | "Does [prototype result]
             |                               |             |  make a credible case for
             |                               |             |  displacing {sq} with
             |                               |             |  {topic}? [verdict]"

  s4_displacement_verdict: [Yes / No / Pending]  ← required; omission = format error
  s4_ce_verdict:           [null if no CE; description if found]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 declared fields populated — 0 additions, 0 omissions,
0 source mismatches so far.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 VALIDATION:
  [ ] SESSION INVARIANT D Stage 4 template printed verbatim in INCUMBENT CHECK table
      header above — text matches TABLE ROW D declaration. No paraphrase.
      Confirm: "Template text in INCUMBENT CHECK matches CAMPAIGN OPEN registration."
  [ ] SESSION INVARIANT D Stage 4 template was also present in ENTRY CONDITIONS above
      (gate obligation confirmed).
  [ ] s4_displacement_verdict recorded (Yes / No / Pending — not blank)
  [ ] s4_ce_verdict recorded (null or description — not blank)
  [ ] null_tally_final computed and cross-checked against Stage 3 running count
  [ ] Artifact {topic}-prototype-{date}.md confirmed written
  VALIDATION RESULT: [PASS — template at entry and execution confirmed] /
                     [FAIL — identify site where template was absent or paraphrased]

STAGE 4 EXIT SIGNAL: prototype_complete (issues only after VALIDATION PASS)
  "STAGE 4 EXIT: prototype_complete — template compliance confirmed at entry and
   execution. null_tally_final = [N]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete (validation passed)
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active (confirmed by ROLE A)

STAGE 5 BODY:

### COUNTER-HYPOTHESIS RESOLUTION TABLE

  COUNTER_HYPOTHESIS               | VERDICT                                  | EVIDENCE
  ---------------------------------|------------------------------------------|-------------------
  [from Stage 1 — TR moat framing] | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]
  [add rows as needed]             |                                          |

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### ATOMIC DUAL-LOCK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch — record if mismatch]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type].
            Reviewer knows {status_quo_comparator} incumbent_moat. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

### SYNTHESIS BODY

  hypothesis_verdict:   [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:     [2-3 sentences — reference THREAT REGISTER: does evidence address
                          incumbent_vulnerability and overcome incumbent_moat?]
  confidence_composite: [final value after all reductions]
  key_risk:             [primary adoption risk — name incumbent_moat as residual challenge]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                             | IND. CHAIN
  ---------------------------|---------|----------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]      | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C / THREAT REGISTER]| n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]       | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]       | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]       | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]       | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]       | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]   | not through
                             |         |                                         |   co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]       | not through
                             |         |                                         |   incumbent_def
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]  | not through
                             |         |                                         |   co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]      | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match schema]  | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write artifact: {topic}-synthesis-{date}.md
Write artifact: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```
