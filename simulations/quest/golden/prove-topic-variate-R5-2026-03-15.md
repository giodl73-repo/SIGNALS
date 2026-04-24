---
skill: quest-variate
skill_target: prove-topic
round: R5
date: 2026-03-15
rubric: prove-topic-rubric-v5-2026-03-15.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [lifecycle_emphasis, output_format, phrasing_register]
  combined: [V-04, V-05]
r4_high_scores: V-04/V-05 (C-16 adversarial escalation + C-17 mechanical CE cap co-present)
r5_targets: C-18 (null CE doubly locked — C-16 and C-17 co-fire from one trigger), C-19 (full null-CE protocol pre-committed at CAMPAIGN OPEN before Stage 0)
severity_stack_gap: "R4 V-04/V-05 satisfy C-16 and C-17 individually but use separate conditional blocks — a null path exists where one fires without the other (fails C-18). Both also register the adversarial reviewer and formula but do not explicitly commit them as session-level invariants before Stage 0 (fails C-19)."
---

# prove-topic — Variation Round R5

Five complete, runnable skill body prompts. Each is self-contained — no diff, no cross-references.

Round 5 targets C-18 and C-19, the two new criteria in rubric v5. These criteria close the
final gaps in the null counter-evidence severity stack:

- C-19 addresses *when* the protocol is committed: at CAMPAIGN OPEN before Stage 0, not
  reactively at synthesis time. R4 variations register the adversarial reviewer type and cap
  formula as fields to fill — but do not explicitly name them as session-level invariants that
  cannot be modified after this point. C-19 requires the language of pre-commitment.

- C-18 addresses *how* the protocol fires: both C-16 (escalation) and C-17 (cap) must activate
  from one trigger event in the same synthesis output. R4 V-04 uses two separate conditional
  blocks: a LOCK 1/LOCK 2 structure where each could theoretically fire independently. C-18
  requires a single atomic activation block where both fire together or neither fires.

A variation can satisfy C-14 through C-17 and still fail both C-18 and C-19. Each addresses
a different compliance layer: C-19 is about session-level invariance (pre-commitment), C-18 is
about co-activation integrity (atomic trigger). Together they close the severity stack.

---

## V-01 — Axis: Lifecycle Emphasis (C-19: pre-commitment at campaign open)

**Variation axis**: Lifecycle emphasis — CAMPAIGN OPEN is rewritten as a PROTOCOL DECLARATION
block. Both null-CE consequences (adversarial reviewer type and confidence cap formula) are
named as session-level invariants before Stage 0. The language distinguishes pre-commitment
("committed here — applies regardless of what evidence is found") from reactive compliance
("will activate if null is detected at synthesis"). The invariant language propagates into each
stage's null-result note so the model carries the commitment forward actively.

**Hypothesis**: Framing the null-CE response as a session-level invariant declared before
evidence collection — rather than a conditional mechanism resolved at synthesis — prevents the
model from treating the adversarial reviewer appointment and confidence cap as decisions to be
made at synthesis time. Pre-commitment language names the mechanism and its activation
condition once, irreversibly. Subsequent stages reference the pre-committed protocol rather
than constructing a response from scratch.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Five stages execute in fixed sequence. The null counter-evidence response is a
pre-committed protocol — declared at campaign open, applies regardless of what is found.

---

## PROTOCOL DECLARATION

Declare before any stage begins. These are session-level invariants.
They apply regardless of what evidence is found during the campaign.
Do not modify after this point.

  status_quo_comparator: [name the incumbent approach this topic must beat]

  NULL-CE INVARIANT A — Adversarial Reviewer (pre-commitment):
    adversarial_reviewer_type: [name the role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    This is a pre-registered appointment — not a synthesis decision. The reviewer
    type is on record now. At synthesis, execution is the only option.

  NULL-CE INVARIANT B — Confidence Cap (pre-commitment):
    Formula: CE-score = -2 if all three evidence stages null; CE-score = 0 otherwise.
    This formula is locked at campaign open. It cannot be overridden by narrative
    confidence judgment at synthesis. It applies regardless of how evidence quality
    reads across other dimensions.

  protocol_declared: true

Both NULL-CE invariants are committed. Do not proceed without both declared.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record all found artifacts:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

GATE S: Scout path confirmed.
  gate_s_cleared: true
  status_quo_comparator: [confirmed from protocol declaration]
  adversarial_reviewer_type: [confirmed from protocol declaration — Invariant A on file]
  null_ce_formula: [confirmed from protocol declaration — Invariant B on file]

Do not open Stage 1 without this gate confirmed and both invariants verified on file.

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [slug from GATE S]
  gate_s_cleared: true
  status_quo_comparator: [from protocol declaration]
  adversarial_reviewer_type: [from protocol declaration — pre-committed Invariant A]
  protocol_declared: true

Body:
  Claim: One testable sentence derived from the scout record.
         Ground in the scout finding — do not derive from general knowledge.
  Falsification: What evidence would disprove this?
  Comparator challenge: Why does this claim beat [status_quo_comparator]?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Artifact written: {topic}-hypothesis-{date}.md" — advance to STAGE 2.

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

### Part A — Supporting Evidence
Gather external sources for the claim.
For each: Title, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Counter-Evidence Search (MANDATORY)
Actively search for evidence favoring [status_quo_comparator] over the claim.
For each result: Source, Finding, Type (Contradicts / Complicates / Weakens).

If no counter-evidence found after active search:
  "Active counter-evidence search at Stage 2 yielded no results.
  Possible reasons: [at least one specific reason].
  Null result recorded. Per pre-committed Invariant B: if S3 and S4 also return null,
  CE-score = -2 applies. Per pre-committed Invariant A: adversarial reviewer
  [adversarial_reviewer_type] activates. Both are session invariants — not new decisions."

Counter-evidence found at Stage 2: [yes / no]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md" — advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Internal signals favoring [status_quo_comparator].
For each: Source, Signal, Type.

If none found:
  "No internal counter-signals found. Null result recorded.
  Running tally: if Stage 4 also returns null, both pre-committed invariants activate.
  Invariant A ([adversarial_reviewer_type]) and Invariant B (CE-score = -2) apply —
  committed at protocol declaration, not assignable or modifiable at synthesis."

Counter-evidence found at Stage 3: [yes / no]

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md" — advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

### Part A — Claim Test
Design a minimal experiment. Record: Setup, Result, Verdict.

### Part B — Counter-Experiment (MANDATORY)
Test a scenario where [status_quo_comparator] would outperform the claim.
Record: Scenario, Status-quo result, Claim result, Comparison verdict.
If not testable: "Reason: [specific]. Limitation propagates to synthesis."

If no counter-evidence found at this stage:
  "Stage 4 counter-experiment yielded no finding favoring [status_quo_comparator].
  Null result recorded.
  [If S2 and S3 were also null]: All three stages returned null. Pre-committed
  protocol invariants activate at synthesis — execution of the committed protocol,
  not a new decision."

Counter-evidence found at Stage 4: [yes / no]

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: {topic}-prototype-{date}.md" — advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

Required sections — all mandatory:

### Protocol Compliance Verification
  Retrieve from protocol declaration:
    adversarial_reviewer_type: [confirmed — Invariant A]
    ce_score_formula: CE-score = -2 if all null; 0 otherwise [confirmed — Invariant B]
    protocol_declared: true
  Both invariants on file: [yes / no]
  If either missing: "Protocol invariant missing — session integrity compromised."

### Counter-Evidence State
  S2: [found / null]    S3: [found / null]    S4: [found / null]
  All three null: [yes / no]

  If ALL stages null:
    "Pre-committed protocol executes — committed at protocol declaration, before Stage 0.
    Invariant A (Adversarial Reviewer):
      Reviewer: [adversarial_reviewer_type] (pre-registered — not appointed now)
      Task: Challenge this claim from the perspective of [adversarial_reviewer_type].
            What evidence would they expect to find? What failure mode is unaddressed?
      Block: Promotion to topic-story blocked until adversarial review completed
             or explicitly deferred with written justification.
    Invariant B (Confidence Cap):
      CE-score = -2 (pre-committed formula — not a synthesis judgment)
      Applied to composite."

### Findings
  Summary of what the evidence shows. Reference each artifact by slug.

### Counter-Evidence Register
  MANDATORY. All counter-evidence from S2, S3, S4.
  | Stage | Source | Finding | Type |
  |-------|--------|---------|------|
  If all null: see protocol execution block above.

### Confidence
  Level: [HIGH / MEDIUM / LOW]
  CE-score applied: [0 / -2] (pre-committed Invariant B — not a synthesis decision)
  Rationale: Derived from evidence across all three stages.
  If escalation triggered: confidence cannot be HIGH pending adversarial review.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  ce_score_applied: [0 / -2]
  escalation_triggered: [true / false]
  status: [Ready / Escalated — adversarial review required before topic-story promotion]
  escalation_reviewer: [adversarial_reviewer_type or "N/A"]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Protocol invariants applied: [yes / not triggered].
         Artifact: {topic}-synthesize-{date}.md. Status: [Ready / Escalated]."
```

---

## V-02 — Axis: Output Format (C-18: atomic dual-lock activation block)

**Variation axis**: Output format — the synthesis uses a single ATOMIC DUAL-LOCK ACTIVATION
block. Both null-CE consequences (confidence cap and adversarial escalation) are evaluated
inside one block from one trigger condition. The format structurally prevents partial
activation: both locks are outputs of the same block. A reviewer can verify co-activation by
confirming the DUAL-LOCK block was entered — there is no conditional branch inside it that
could activate one lock while skipping the other.

**Hypothesis**: Restructuring the null-CE response from two sequential conditional checks into
one atomic block eliminates the architecture that allows C-16 and C-17 to fire independently.
When the trigger ("all three stages returned null") is evaluated once, both outputs (CE-score
penalty and adversarial escalation) are derived simultaneously. The format carries a co-
activation confirmation field that must match the trigger — making partial activation visible
as a format error, not just a semantic miss.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. Five stages in fixed sequence.
Null counter-evidence triggers an ATOMIC DUAL-LOCK — both the confidence cap and adversarial
escalation activate together from one trigger event. Partial activation is a format error.

---

## CAMPAIGN OPEN

Register before any stage begins:

  status_quo_comparator: [name the incumbent approach this topic must beat]
  adversarial_reviewer_type: [name the role most likely to challenge the claim]
  ce_penalty_rule: CE-score = -2 if all stages null; CE-score = 0 if any stage finds CE

Both fields mandatory. Do not proceed without filling both.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

GATE S: Scout path confirmed. gate_s_cleared: true
Do not open Stage 1 without this gate confirmed.

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [slug from GATE S]
  gate_s_cleared: true
  status_quo_comparator: [from campaign open]
  adversarial_reviewer_type: [from campaign open]

Body:
  Claim: One testable sentence derived from the scout record.
  Falsification: What evidence would disprove this?
  Comparator challenge: Why does this claim beat [status_quo_comparator]?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Artifact written: {topic}-hypothesis-{date}.md" — advance to STAGE 2.

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

### Part A — Supporting Evidence
External sources for the claim.
For each: Source, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Counter-Evidence Search (MANDATORY)
Active search for evidence favoring [status_quo_comparator].
For each found: Source, Finding, Type (Contradicts / Complicates / Weakens).

If none after active search:
  "Active search at Stage 2 yielded no results. Possible reasons: [one]. Null recorded."

Counter-evidence found at Stage 2: [yes / no]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md" — advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Internal signals favoring [status_quo_comparator].
If none: "No internal counter-signals. Null recorded."

Counter-evidence found at Stage 3: [yes / no]

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md" — advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

### Part A — Claim Test
Design a minimal experiment. Record: Setup, Result, Verdict.

### Part B — Counter-Experiment (MANDATORY)
Test a scenario where [status_quo_comparator] outperforms the claim.
Record: Scenario, Status-quo result, Claim result, Verdict.
If not testable: "Reason: [specific]. Limitation propagates to synthesis."

Counter-evidence found at Stage 4: [yes / no]

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: {topic}-prototype-{date}.md" — advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

Required sections — all mandatory:

### CE State Collection
  S2: [found / null]    S3: [found / null]    S4: [found / null]
  Trigger condition (all three null): [yes / no]

### ATOMIC DUAL-LOCK ACTIVATION

  ══════════════════════════════════════════════════════════════════
  Enter this block ONLY when trigger condition is YES (all three null).
  Both locks activate from this single entry. Partial activation is a
  format error — if you enter this block, both locks must appear.
  ══════════════════════════════════════════════════════════════════

  LOCK A — Confidence Cap:
    CE-score = -2
    Evidence composite (S2×0.30 + S3×0.30 + S4×0.40): ___
    Final composite after CE penalty: ___
    Confidence ceiling: MEDIUM maximum. HIGH is not available when CE-score = -2.
    cap_applied: true

  LOCK B — Adversarial Escalation:
    Reviewer: [adversarial_reviewer_type from campaign open]
    Task: Challenge this claim from the perspective of [adversarial_reviewer_type].
          What evidence should this campaign have found? What failure mode is unaddressed?
    Block: Promotion to topic-story blocked until adversarial review is completed
           or explicitly deferred with written justification.
    escalation_triggered: true

  co_activation_confirmed: true
  [Both LOCK A and LOCK B appear above. This field confirms co-activation.
  A synthesis output that sets this field true but omits one lock is invalid.]

  ══════════════════════════════════════════════════════════════════
  END DUAL-LOCK BLOCK
  ══════════════════════════════════════════════════════════════════

  If trigger condition is NO (at least one stage found counter-evidence):
    CE-score = 0. escalation_triggered = false. Continue to Findings.

### Findings
  Summary of what the evidence shows. Reference each artifact by slug.

### Counter-Evidence Register
  MANDATORY. All counter-evidence from S2, S3, S4.
  | Stage | Source | Finding | Type |
  |-------|--------|---------|------|
  If all null: see ATOMIC DUAL-LOCK ACTIVATION block above.

### Confidence
  Level: [HIGH / MEDIUM / LOW] (HIGH unavailable if dual-lock fired)
  CE-score applied: [0 / -2]
  Rationale: Derived from composite and CE-score.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  ce_score_applied: [0 / -2]
  escalation_triggered: [true / false]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [true / false — must equal dual_lock_fired]
  status: [Ready / Escalated — adversarial review required before topic-story promotion]
  escalation_reviewer: [adversarial_reviewer_type or "N/A"]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Dual-lock: [fired / not fired]. Co-activation: [confirmed / N/A].
         Status: [Ready / Escalated]."
```

---

## V-03 — Axis: Phrasing Register (invariant language propagated forward through all stages)

**Variation axis**: Phrasing register — the entire skill is written in a formal invariant
register. Every section that touches the null-CE protocol uses pre-commitment framing
consistently: "pre-registered invariant", "committed before collection", "applies regardless",
"session-level commitment", "not a synthesis decision". The protocol language propagates into
Stage 2, 3, and 4 null-result notes so the model carries the commitment forward actively at
each stage rather than rediscovering it at synthesis.

**Hypothesis**: The failure mode C-19 targets — reactive compliance vs. session-level
invariance — is a language problem as much as a structure problem. A variation can have all
the right fields in CAMPAIGN OPEN but still produce a synthesis that treats the reviewer
appointment and cap formula as new decisions, because the intermediate stages never carried
the invariant framing forward. Propagating the pre-commitment register through every stage
that records a null result creates a continuous chain from CAMPAIGN OPEN to synthesis,
leaving no stage at which the model can "forget" the protocol is already committed.

---

```
Topic: {topic}
Date:  {date}

Prove evidence campaign. Two session-level invariants govern null counter-evidence outcomes.
Both are pre-registered at campaign open — committed before evidence collection begins —
and cannot be modified or bypassed at synthesis time.

---

## SESSION INVARIANT REGISTRY
(Declared before Stage 0 — binding for the full session)

  status_quo_comparator: [name the incumbent approach]
  — Primary test throughout: does the claim demonstrably improve on this incumbent?

  SESSION INVARIANT A — Adversarial Reviewer (pre-registration):
    adversarial_reviewer_type: [name the role most likely to challenge the claim]
    Activation condition: all three evidence stages (S2, S3, S4) return null CE.
    Status: pre-registered. This reviewer is on record now. If the activation
    condition fires, this is execution — not appointment.

  SESSION INVARIANT B — Confidence Cap (pre-registration):
    Rule: CE-score = -2 if activation condition fires; CE-score = 0 otherwise.
    Status: pre-registered formula. Cannot be overridden, softened, or bypassed
    by narrative judgment at synthesis. It is a session-level commitment.

  invariant_registry_locked: true

Do not proceed without both invariants declared and registry locked.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

GATE S: Scout confirmed.
  gate_s_cleared: true
  invariant_registry_confirmed: true  (both session invariants on file before Stage 1)

Do not open Stage 1 without both items confirmed.

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [slug from GATE S]
  gate_s_cleared: true
  status_quo_comparator: [from invariant registry]
  adversarial_reviewer_type: [from invariant registry — pre-registered Session Invariant A]
  null_ce_formula: CE-score = -2 if all null [Session Invariant B — pre-registered]
  invariant_registry_locked: true

Body:
  Claim: One testable sentence derived from the scout record.
         Grounded in the scout finding — not general knowledge.
  Falsification: What evidence would disprove this?
  Comparator challenge: Why does this claim beat [status_quo_comparator]?
  Note: If this campaign yields null counter-evidence at all three evidence stages,
        Session Invariant A ([adversarial_reviewer_type]) activates. That is a
        pre-registered commitment, not a decision taken at synthesis.

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Artifact written: {topic}-hypothesis-{date}.md" — advance to STAGE 2.

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

Session invariants active throughout this stage.

### Part A — Supporting Evidence
External sources for the claim.
For each: Source, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Counter-Evidence Search (MANDATORY)
Active search for evidence favoring [status_quo_comparator].
For each found: Source, Finding, Type (Contradicts / Complicates / Weakens).

If no counter-evidence found after active search:
  "Active counter-evidence search at Stage 2 yielded no results.
  Possible reasons: [at least one specific reason]. Null result recorded.
  Running tally: S2 null. Two stages remain.
  Pre-registration note: If S3 and S4 also return null, the activation condition fires.
  Session Invariant A ([adversarial_reviewer_type]) and Session Invariant B
  (CE-score = -2) will execute at synthesis — pre-committed session obligations,
  not conditional judgments made at that time."

Counter-evidence found at Stage 2: [yes / no]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md" — advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

Session invariants active throughout this stage.

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Internal signals favoring [status_quo_comparator].
For each: Source, Signal, Type.

If no counter-evidence found:
  "No internal counter-signals found. Null result recorded.
  Running tally: [S2 status], S3 null.
  Pre-registration note: One stage remains. If Stage 4 returns null, both pre-registered
  invariants execute. Invariant A ([adversarial_reviewer_type]) is a pre-committed
  appointment — not a synthesis-time decision. Invariant B (CE-score = -2) is a
  pre-committed formula — not a narrative judgment made after the evidence is read."

Counter-evidence found at Stage 3: [yes / no]

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md" — advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

Session invariants active throughout this stage. Final evidence stage.

### Part A — Claim Test
Design a minimal experiment. Record: Setup, Result, Verdict.

### Part B — Counter-Experiment (MANDATORY)
Test or describe a scenario where [status_quo_comparator] outperforms the claim.
Record: Scenario, Status-quo result, Claim result, Verdict.
If not testable: "Reason: [specific]. Limitation propagates to synthesis."

If no counter-evidence found at this stage:
  "Stage 4 counter-experiment yielded no finding favoring [status_quo_comparator].
  Null result recorded.
  [If S2 and S3 were also null:] Activation condition confirmed — all three stages
  returned null. Pre-registered session invariants execute at synthesis as committed.
  This is the pre-committed protocol running, not a decision being made."

Counter-evidence found at Stage 4: [yes / no]

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: {topic}-prototype-{date}.md" — advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

### Invariant Retrieval
  Retrieve from session invariant registry (pre-registered before Stage 0):
    Session Invariant A: adversarial_reviewer_type = [confirmed]
    Session Invariant B: CE-score formula = -2 if all null; 0 otherwise [confirmed]
    invariant_registry_locked: true

### CE State and Protocol Execution
  S2: [found / null]    S3: [found / null]    S4: [found / null]
  Activation condition (all three null): [yes / no]

  If activation condition fires:
    "Pre-registered session invariants execute — committed at session open,
    not assigned at this moment.

    Session Invariant A executing (pre-registered adversarial reviewer):
      Reviewer: [adversarial_reviewer_type]
      Task: Challenge this claim from the perspective of [adversarial_reviewer_type].
            What evidence should this campaign have found? What failure mode is
            unaddressed by the supportive evidence gathered?
      Effect: Promotion to topic-story blocked until adversarial review is completed
              or explicitly deferred with written justification.
      escalation_triggered: true

    Session Invariant B executing (pre-registered confidence cap formula):
      CE-score = -2 (pre-committed formula — not a narrative judgment applied now)
      Applied to composite. High confidence unavailable while escalation_triggered."

### Findings
  Summary of what the evidence shows. Reference each artifact by slug.

### Counter-Evidence Register
  MANDATORY. All counter-evidence from S2, S3, S4.
  | Stage | Source | Finding | Type |
  |-------|--------|---------|------|
  If all null: see protocol execution block above.

### Confidence
  Level: [HIGH / MEDIUM / LOW]
  CE-score applied: [0 / -2]
  Source: Session Invariant B (pre-registered formula — not a synthesis assignment)
  Rationale: Derived from evidence and pre-committed formula.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  ce_score_applied: [0 / -2]
  escalation_triggered: [true / false]
  invariants_executed: [A_reviewer / B_cap / both / neither]
  status: [Ready / Escalated — adversarial review required before topic-story promotion]
  escalation_reviewer: [adversarial_reviewer_type or "N/A"]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Invariants: [executed / not triggered].
         Status: [Ready / Escalated]."
```

---

## V-04 — Combined: C-19 Protocol Manifest + C-18 Atomic Dual-Lock

**Variation axis**: This variation directly combines V-01 (CAMPAIGN OPEN as a PROTOCOL
DECLARATION with session-level invariants) and V-02 (synthesis ATOMIC DUAL-LOCK ACTIVATION
block) to close both C-19 and C-18 in one design:

- C-19: CAMPAIGN OPEN names both the adversarial reviewer type and the confidence cap formula
  as session-level invariants, with explicit pre-commitment language, before Stage 0.
- C-18: The synthesis uses one ATOMIC DUAL-LOCK block — a single trigger event fires both
  consequences simultaneously. The block has one entry condition; both locks are outputs of
  that entry. Partial activation is named as a format violation inside the block.

**Hypothesis**: C-18 and C-19 fail independently in R4: C-19 fails because the CAMPAIGN OPEN
fields are presented as registration slots, not invariant declarations; C-18 fails because the
synthesis uses a LOCK 1 / LOCK 2 structure with sequential conditional checks that could
theoretically diverge. Combining the protocol manifest (C-19) with the atomic block (C-18)
closes both without conflict — pre-commitment governs when the protocol is established; atomic
co-activation governs how it fires. They address different failure modes in the same null-CE
path.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. Five stages in fixed sequence.
The null counter-evidence response is a pre-committed protocol that fires atomically.
Both consequences — confidence cap and adversarial escalation — are committed at campaign
open as session invariants and activate together from one trigger event at synthesis.

---

## CAMPAIGN OPEN — PROTOCOL MANIFEST

Declare all session invariants before Stage 0 begins.
The full null-CE protocol is committed here. Cannot be modified after this point.

  status_quo_comparator: [name the incumbent approach this topic must beat]

  NULL-CE PROTOCOL — pre-committed, applies regardless of what evidence is found:

    INVARIANT A — Adversarial Reviewer:
      adversarial_reviewer_type: [name the role most likely to challenge the claim]
      Activation: fires if ALL of S2, S3, S4 return null counter-evidence.
      Pre-commitment: this reviewer is named here. At synthesis, this is not an
      appointment — it is execution of a pre-committed protocol.

    INVARIANT B — Confidence Cap:
      Formula: CE-score = -2 if all three stages null; CE-score = 0 if any stage finds CE.
      Pre-commitment: this formula is locked in. At synthesis, it is not a judgment —
      it is the formula executing. Verbal override is not permitted.

    INVARIANT C — Co-Activation Rule:
      When the activation condition fires, A and B fire together — from one trigger.
      A synthesis output where only one activates is a protocol violation.

  protocol_manifest_locked: true

All three invariants declared. Do not proceed without all three.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

GATE S — all items required before Stage 1 opens:
  [ ] scout_path: [confirmed]
  [ ] key_finding: [recorded]
  [ ] status_quo_comparator: [registered — manifest field 1]
  [ ] adversarial_reviewer_type: [registered — Invariant A]
  [ ] ce_score_formula: [declared — Invariant B]
  [ ] co_activation_rule: [declared — Invariant C]
  gate_s_cleared: true

Do not open Stage 1 without all six items confirmed.

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [slug from GATE S]
  gate_s_cleared: true
  status_quo_comparator: [from protocol manifest]
  adversarial_reviewer_type: [from protocol manifest — Invariant A pre-committed]
  protocol_manifest_locked: true

Body:
  Claim: One testable sentence derived from the scout record.
         Do not derive from general knowledge.
  Falsification: What evidence would disprove this?
  Comparator challenge: Why does this claim beat [status_quo_comparator]?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Artifact written: {topic}-hypothesis-{date}.md" — advance to STAGE 2.

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

### Part A — Supporting Evidence
For each source: Title, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Counter-Evidence Search (MANDATORY)
Active search for evidence favoring [status_quo_comparator].
For each: Source, Finding, Type (Contradicts / Complicates / Weakens).

If none after active search:
  "Active search at Stage 2 yielded no results. Possible reasons: [one].
  Null recorded. Per pre-committed Invariant B and Invariant A: if S3 and S4 also
  null, the atomic dual-lock fires at synthesis — both as pre-committed invariants,
  not new decisions."

Counter-evidence found at Stage 2: [yes / no]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md" — advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type, Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Internal signals favoring [status_quo_comparator].
If none: "No internal counter-signals. Null recorded. Pre-committed invariants
  track toward activation if Stage 4 also null."

Counter-evidence found at Stage 3: [yes / no]

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md" — advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

### Part A — Claim Test
Minimal experiment. Record: Setup, Result, Verdict.

### Part B — Counter-Experiment (MANDATORY)
Test a scenario where [status_quo_comparator] outperforms the claim.
Record: Scenario, Status-quo result, Claim result, Verdict.
If not testable: "Reason: [specific]. Limitation propagates to synthesis."

Counter-evidence found at Stage 4: [yes / no]

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: {topic}-prototype-{date}.md" — advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

Required sections — all mandatory:

### Null CE State
  S2: [found / null]    S3: [found / null]    S4: [found / null]
  All three null — activation condition met: [yes / no]

### ATOMIC DUAL-LOCK ACTIVATION
  ════════════════════════════════════════════════════════════════════════
  ENTER ONLY WHEN: all three of S2, S3, S4 returned null counter-evidence.
  PRE-COMMITTED PROTOCOL EXECUTING — committed at Campaign Open, not now.
  INVARIANT C requires: both locks activate. Exit without both = protocol violation.
  ════════════════════════════════════════════════════════════════════════

  LOCK A — Invariant A executing (confidence cap):
    CE-score = -2 (pre-committed Invariant B formula — not a synthesis judgment)
    Evidence composite (S2×0.30 + S3×0.30 + S4×0.40): ___
    Final composite after CE penalty: ___
    Ceiling: MEDIUM maximum. HIGH not available while escalation_triggered.
    cap_applied: true

  LOCK B — Invariant A executing (adversarial escalation):
    Reviewer: [adversarial_reviewer_type] (pre-registered in protocol manifest)
    Task: Challenge this claim from the perspective of [adversarial_reviewer_type].
          What evidence would they expect to find? What failure mode is unaddressed?
    Block: Promotion to topic-story blocked until adversarial review is completed
           or explicitly deferred with written justification.
    escalation_triggered: true

  co_activation_confirmed: true
  [LOCK A and LOCK B both appear above. Invariant C fulfilled.
  A synthesis that sets co_activation_confirmed: true but omits one lock is invalid.]

  ════════════════════════════════════════════════════════════════════════
  END DUAL-LOCK BLOCK
  ════════════════════════════════════════════════════════════════════════

  If activation condition NOT met (any stage found counter-evidence):
    CE-score = 0. escalation_triggered = false. Continue to Findings.

### Findings
  Summary of what the evidence shows. Reference each artifact by slug.

### Counter-Evidence Register
  MANDATORY.
  | Stage | Source | Finding | Type |
  |-------|--------|---------|------|
  If all null: recorded in ATOMIC DUAL-LOCK ACTIVATION block above.

### Confidence
  Level: [HIGH / MEDIUM / LOW]
  CE-score applied: [0 / -2]
  Source: Invariant B (pre-committed formula — not assigned at synthesis)
  Rationale: Composite from evidence stages and CE-score.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  ce_score_applied: [0 / -2]
  escalation_triggered: [true / false]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [true / false — must equal dual_lock_fired]
  status: [Ready / Escalated — adversarial review required before topic-story promotion]
  escalation_reviewer: [adversarial_reviewer_type or "N/A"]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Dual-lock: [fired / not fired]. Co-activation: [confirmed / N/A].
         Status: [Ready / Escalated]."
```

---

## V-05 — Combined: Full Excellence Compound (R4 V-05 + C-18 + C-19)

**Variation axis**: This variation extends R4's V-05 (the accumulated excellence compound
through Round 4) with full C-18 and C-19 integration. The R4 V-05 base satisfies C-01
through C-17:
- GATE S 4-checkbox clearance (C-11)
- Per-artifact full path in every write instruction (C-13)
- Status-quo comparator registered at campaign open (C-12)
- gate_s_cleared in hypothesis frontmatter (C-15)
- Mandatory counter-evidence with null fallback (C-14)
- Evidence weighting ledger with prototype cap (C-09, C-10)
- Adversarial reviewer registered, escalation_state tracked (C-16)
- CE-score as a formal input to the confidence formula (C-17)

R5 additions:
1. CAMPAIGN OPEN rewritten as a PROTOCOL MANIFEST with explicit invariant language —
   adversarial reviewer type and CE-score formula declared as session-level commitments
   before Stage 0 (C-19).
2. Stage 5 null-CE check replaced with ATOMIC DUAL-LOCK ACTIVATION block — single trigger
   fires both CE-score penalty and adversarial escalation from one entry (C-18).

**Hypothesis**: R4 V-05 satisfies C-16 and C-17 individually in separate conditional branches
(LOCK 1 / LOCK 2 structure). A null-CE path exists where CE-score = -2 applies but escalation
does not fire (LOCK 1 skipped), or escalation fires but the CE-score remains zero (LOCK 2
skipped). The atomic dual-lock closes this. Simultaneously, R4 V-05's CAMPAIGN OPEN uses
registration language ("register before any stage begins") rather than invariant language —
the model can treat the adversarial reviewer type as an initial fill-in, not a committed
protocol. The protocol manifest closes this. Neither change conflicts with existing mechanisms.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. All five stages in fixed sequence.
No stage opens without the preceding artifact confirmed.
The null counter-evidence response is a pre-committed protocol — declared as session
invariants before Stage 0, fires atomically at synthesis with both locks co-active.

---

## CAMPAIGN OPEN — PROTOCOL MANIFEST

Declare all session invariants before Stage 0 begins.
Both null-CE protocols are committed here. Cannot be modified after this point.

  status_quo_comparator: [name the incumbent approach this topic must beat]

  NULL-CE PROTOCOL — pre-committed, applies regardless of what evidence is found:

    INVARIANT A — Adversarial Reviewer (pre-commitment):
      adversarial_reviewer_type: [name the role most likely to challenge the claim]
      Activation: all three evidence stages return null counter-evidence.
      This reviewer is pre-registered now — not appointed at synthesis.

    INVARIANT B — Confidence Cap (pre-commitment):
      CE-score = -2 if all three stages null; CE-score = 0 if any stage finds CE.
      This formula is a session-level commitment. Verbal override not permitted.

    INVARIANT C — Co-Activation Rule:
      When activation fires, A and B fire together from one trigger.
      Partial activation is a protocol violation.

  evidence_ledger:
    web_search:   weight: 30%   quality: [to be filled at Stage 2]
    intelligence: weight: 30%   quality: [to be filled at Stage 3]
    prototype:    weight: 40%   quality: [to be filled at Stage 4]

  confidence_formula:
    evidence_composite: (S2 × 0.30) + (S3 × 0.30) + (S4 × 0.40)
    CE-score: pre-committed Invariant B formula
    prototype_cap: if prototype quality = Thin, final composite cannot exceed 6.9 (MEDIUM)
    final_composite: evidence_composite + CE-score [capped if prototype Thin]
    level: HIGH (>=7.0) / MEDIUM (4.0-6.9) / LOW (<4.0)

  escalation_state: not_triggered

  protocol_manifest_locked: true

All fields mandatory. Do not proceed without all declared.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

GATE S — all six items required before Stage 1 opens:
  [ ] scout_path: [confirmed path]
  [ ] key_finding: [recorded]
  [ ] status_quo_comparator: [registered — manifest field 1]
  [ ] adversarial_reviewer_type: [registered — Invariant A pre-committed]
  [ ] ce_score_formula: [declared — Invariant B pre-committed]
  [ ] evidence_ledger: [initialized with weights]
  gate_s_cleared: true

Do not open Stage 1 until all six items confirmed.

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [slug from GATE S]
  scout_path: [full path from GATE S]
  gate_s_cleared: true
  status_quo_comparator: [from protocol manifest]
  adversarial_reviewer_type: [from protocol manifest — Invariant A pre-committed]
  evidence_weights_registered: true
  protocol_manifest_locked: true

Body:
  Claim: One testable sentence derived from the scout record.
         Link explicitly to the scout finding that grounds it.
         Do not derive from general knowledge.
  Falsification: What evidence would disprove this?
  Comparator challenge: Why does this claim beat [status_quo_comparator]?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Artifact written: simulations/prove/{topic}/{topic}-hypothesis-{date}.md"
Advance to STAGE 2.

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

Evidence weight: 30%

### Part A — Supporting Evidence
Gather external evidence for the claim.
For each source: Title, Finding, Strength (Strong / Moderate / Weak).

### Part B — Counter-Evidence Search (MANDATORY)
Actively search for evidence favoring [status_quo_comparator].
For each result: Source, Finding, Type (Contradicts / Complicates / Weakens).

If none found after active search:
  "Active counter-evidence search at Stage 2 yielded no results.
  Possible reasons: [at least one specific reason]. Null result recorded.
  Per pre-committed Invariant B and Invariant A: if S3 and S4 also null, the
  atomic dual-lock fires at synthesis — pre-committed protocol execution,
  not a new decision."

Stage 2 score: ___ / 10
Counter-evidence found: [yes / no]
Evidence quality: [Strong / Moderate / Thin]
Update evidence ledger: web_search quality: [verdict]
Update formula: Stage 2 score → [value]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: simulations/prove/{topic}/{topic}-websearch-{date}.md"
Advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

Evidence weight: 30%

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Internal signals favoring [status_quo_comparator].
For each: Source, Signal, Type.

If none found:
  "No internal counter-signals found. Null result recorded.
  Pre-commitment tracking: if Stage 4 also null, both pre-registered invariants
  execute atomically at synthesis."

Stage 3 score: ___ / 10
Counter-evidence found: [yes / no]
Evidence quality: [Strong / Moderate / Thin]
Update evidence ledger: intelligence quality: [verdict]
Update formula: Stage 3 score → [value]

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: simulations/prove/{topic}/{topic}-intelligence-{date}.md"
Advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

Evidence weight: 40%

### Part A — Claim Test
Design a minimal experiment. Record: Setup, Result, Verdict.

### Part B — Counter-Experiment (MANDATORY)
Test or describe a scenario where [status_quo_comparator] would outperform the claim.
Record: Scenario, Status-quo result, Claim result, Comparison verdict.
If not testable: "Reason: [specific]. Limitation propagates to synthesis confidence."

Stage 4 score: ___ / 10
Counter-evidence found: [yes / no]
Evidence quality: [Strong / Moderate / Thin]
Update evidence ledger: prototype quality: [verdict]
Update formula: Stage 4 score → [value]

Prototype thin check:
  If prototype quality is Thin:
    Set prototype_cap: true
    "WARNING: Prototype (40% weight) is Thin. Final composite capped at 6.9 (MEDIUM max)."

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: simulations/prove/{topic}/{topic}-prototype-{date}.md"
Advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage. No stages follow this one.

Required sections — all mandatory:

### Protocol Manifest Verification
  Retrieve pre-committed invariants from protocol manifest:
    Invariant A: adversarial_reviewer_type = [confirmed]
    Invariant B: CE-score formula = -2 if all null; 0 otherwise [confirmed]
    Invariant C: co-activation rule [confirmed]
    protocol_manifest_locked: true
  If any invariant missing: "Protocol manifest incomplete — session integrity compromised."

### CE State Collection
  S2: [found / null]    S3: [found / null]    S4: [found / null]
  Activation condition (all three null): [yes / no]

### ATOMIC DUAL-LOCK ACTIVATION
  ════════════════════════════════════════════════════════════════════════
  ENTER ONLY WHEN: activation condition is YES.
  PRE-COMMITTED PROTOCOL EXECUTING per Invariant C — both locks must fire.
  A synthesis output that exits this block with only one lock active is a
  protocol violation (Invariant C).
  ════════════════════════════════════════════════════════════════════════

  LOCK A — Invariant B executing (confidence cap):
    CE-score = -2 (pre-committed formula — not a synthesis judgment)
    Prototype cap applies: [yes / no] (from Stage 4 thin check)
    cap_applied: true

  LOCK B — Invariant A executing (adversarial escalation):
    Reviewer: [adversarial_reviewer_type] (pre-registered in protocol manifest)
    Task: Challenge this claim from the perspective of [adversarial_reviewer_type].
          What evidence would they expect to find? What failure mode is unaddressed?
    Block: Promotion to topic-story blocked until adversarial review is completed
           or explicitly deferred with written justification.
    escalation_triggered: true
    Update escalation_state: triggered

  co_activation_confirmed: true
  [LOCK A and LOCK B both appear above. Invariant C fulfilled.
  Setting co_activation_confirmed: true without both locks present is invalid.]

  ════════════════════════════════════════════════════════════════════════
  END DUAL-LOCK BLOCK
  ════════════════════════════════════════════════════════════════════════

  If activation condition NOT met:
    CE-score = 0. escalation_state = not_triggered. Continue to Evidence Ledger Final.

### Evidence Ledger Final
  | Stage | Evidence Type | Weight | Quality   | Score / 10 | Contribution |
  |-------|--------------|--------|-----------|------------|--------------|
  | S2    | Web Search   | 30%    | [verdict] | [score]    | [×0.30]      |
  | S3    | Intelligence | 30%    | [verdict] | [score]    | [×0.30]      |
  | S4    | Prototype    | 40%    | [verdict] | [score]    | [×0.40]      |
  Evidence composite: ___
  CE-score (from pre-committed Invariant B): [0 / -2]
  Prototype cap applied: [yes / no]
  Final composite (after CE-score and cap): ___
  Level (from formula — no override): [HIGH / MEDIUM / LOW]

### Findings
  Summary of what the evidence shows. Reference each artifact by full path.

### Counter-Evidence Register
  MANDATORY. All counter-evidence from S2, S3, and S4.
  | Stage | Source | Finding | Type |
  |-------|--------|---------|------|
  If all null: see ATOMIC DUAL-LOCK ACTIVATION above.
  Null result is not suppressed. Uniformly supportive evidence is a campaign integrity flag.

### Status-Quo Comparison
  Claim evidence vs. [status_quo_comparator from protocol manifest].
  Verdict: Replace / Augment / Coexist / Insufficient to determine.
  Counter-experiment result (Stage 4 Part B): [verdict or limitation note].

### Composite Confidence
  Computed from formula. Not assigned by judgment.
  Final composite: [N] / 10
  Level: [HIGH / MEDIUM / LOW]
  Prototype cap: [yes / no]
  CE-score applied: [0 / -2] (pre-committed Invariant B)
  Counter-evidence impact: [None found — dual-lock fired / Present-weak / Present-material]

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level from formula]
  composite_score: [final_composite] / 10
  ce_score_applied: [0 / -2]
  escalation_state: [not_triggered / triggered]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [true / false — must equal dual_lock_fired]
  status: [Ready / Escalated — adversarial review required before topic-story promotion]
  escalation_reviewer: [adversarial_reviewer_type or "N/A"]
  ready: [true / false — if false, specify blocker]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Campaign complete. simulations/prove/{topic}/{topic}-synthesize-{date}.md written.
         Status: [Ready / Escalated]. Dual-lock: [fired / not fired].
         Confidence: [level] ([composite] / 10)."
```
