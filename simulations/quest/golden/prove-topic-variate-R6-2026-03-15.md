---
skill: quest-variate
skill_target: prove-topic
round: R6
date: 2026-03-15
rubric: prove-topic-rubric-v6-2026-03-15.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [role_sequence, output_format, lifecycle_emphasis]
  combined: [V-04, V-05]
r5_high_scores: V-02 (C-21 PASS — co-activation echo in handoff), V-03 (C-20 PASS — per-stage tally, C-22 PASS — invariant registry field)
r6_targets: C-20 (per-stage null tally with running count and protocol reference), C-21 (co-activation state echoed into handoff with integrity constraint), C-22 (invariant_registry_confirmed as distinct gate field in hypothesis frontmatter)
severity_stack_gap: "R5 V-02 satisfies C-21 but fails C-20 (no per-stage tally) and C-22 (no invariant-registry field — only gate_s_cleared). R5 V-03 satisfies C-20 and C-22 but fails C-21 (no co-activation echo in handoff). No R5 variation satisfies all three simultaneously. Each v6 criterion extends an existing one: C-20 extends C-09 into per-stage accumulation, C-21 extends C-18 into the handoff artifact, C-22 extends C-15 with a second attestation field."
---

# prove-topic — Variation Round R6

Five complete, runnable skill body prompts. Each is self-contained — no diff, no cross-references.

Round 6 targets C-20, C-21, and C-22, the three new criteria in rubric v6. These criteria
extend prior-round gains from synthesis-internal compliance into collection-phase visibility
and cross-artifact auditability:

- **C-20** addresses *when* null results are tracked: per evidence stage with a running count,
  not retroactively at synthesis. R5 variations record null results per stage (satisfying
  C-09) but do not use running-tally language that makes accumulation auditable during
  collection. C-20 requires "Running tally: SN null. X stages remain..." framing and an
  explicit reference to the pre-committed protocol, so each null result is visible as a
  pre-registered obligation becoming active — not a finding to be interpreted at synthesis.

- **C-21** addresses *where* co-activation is visible: in the handoff artifact that downstream
  skills consume. R5 V-02 fires the ATOMIC DUAL-LOCK inside the synthesis block (C-18 PASS)
  but the handoff section lacks a `co_activation_confirmed` field — meaning topic-story
  must replay the full session to verify null-CE closure. C-21 requires the co-activation
  outcome to propagate into the Handoff section as an explicit field with an integrity
  constraint (`co_activation_confirmed: [must equal dual_lock_fired]`).

- **C-22** addresses *what* the hypothesis frontmatter attests: two independently-auditable
  fields, not one. R5 variations use `gate_s_cleared: true` to attest scout load (C-15
  PASS) but do not separately attest that the invariant registry was active when the
  hypothesis was formed. C-22 requires `invariant_registry_confirmed: true` as a distinct
  field alongside `gate_s_cleared: true` — two separate attestations readable from the
  artifact alone without session replay.

A variation can satisfy the full v5 stack and still fail all three: null acknowledged at
synthesis but not accumulated per stage (C-20 FAIL), dual-lock fires but no echo in handoff
(C-21 FAIL), gate clears but no invariant-registry field in hypothesis (C-22 FAIL).

---

## V-01 — Axis: Role Sequence (two pre-evidence blocking roles)

**Variation axis**: Role sequence — the campaign opens with two distinct, sequentially
blocked roles before any evidence stage begins. ROLE A verifies and locks the invariant
registry. ROLE B loads the scout record. Stage 1 requires both roles complete. This
architecture produces `invariant_registry_confirmed` as a first-class output of an
independent blocking step, not an annotation on scout-load. It also produces C-20 naturally:
each evidence role ends with an explicit exit block whose null-result note carries the
running tally framed as an active obligation from the locked registry.

**Hypothesis**: When invariant registry verification and scout-load are separate blocking
roles with distinct outputs, the hypothesis frontmatter must carry two independent
attestation fields (one per role) to record completion of both. A single `gate_s_cleared`
field would only trace Role B — the separate `invariant_registry_confirmed` field traces
Role A. This structural separation closes C-22 without requiring a special instruction to
"add a second field," because the fields arise from two separate blocking actions.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign opens with two blocking roles followed by five evidence stages.
All roles and stages execute in fixed sequence. No step may be skipped or reordered.

---

## ROLE A — INVARIANT REGISTRY LOCK

Execute first. This role declares and locks the null counter-evidence protocol as a
session-level invariant. Both invariants are committed here, before any evidence is
collected. They cannot be modified or bypassed at synthesis time.

Fill all fields:

  status_quo_comparator: [name the incumbent approach this topic must beat]

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Status: pre-registered now. If activation fires at synthesis, that is execution
            of this pre-committed appointment — not a new decision.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Status: locked formula. Cannot be softened, overridden, or bypassed at synthesis
            by narrative confidence judgment. Session-level commitment.

  invariant_registry_confirmed: true
  registry_note: "Both invariants are on record. Cannot be modified after this point."

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

Execute after ROLE A. Do not begin hypothesis work until this role completes.

Search: simulations/scout/**/{topic}-*.md

Record found artifacts:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [one-line finding] |

GATE S (requires both ROLE A and ROLE B complete):
  gate_s_cleared: true
  scout_anchor: [slug of primary scout artifact]
  invariant_registry_confirmed: true  [echo from ROLE A — must match]

If no scout artifact found:
  gate_s_cleared: false
  STOP: "GATE S FAIL — no scout record for {topic}. Run scout skills first.
         Invariant registry is locked (ROLE A complete) but scout prerequisite unmet.
         Do not advance to Stage 1."

If GATE S clears:
  Confirm: "Scout loaded: {scout_anchor}. Gate S cleared. Invariant registry confirmed.
            Both prerequisites satisfied — opening Stage 1."

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter (all fields mandatory):
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [slug from ROLE B]
  gate_s_cleared: true                  ← attests ROLE B completed
  invariant_registry_confirmed: true    ← attests ROLE A completed (distinct field)
  status_quo_comparator: [from ROLE A]
  adversarial_reviewer_type: [from ROLE A — Invariant A, pre-committed]
  ce_score_formula: CE-score = -2 if all null [ROLE A — Invariant B, pre-committed]

Body:
  Claim: One testable sentence derived from the scout record.
         Ground in the scout finding — do not derive from general knowledge.
  Falsification: What evidence would disprove this?
  Comparator challenge: Why does this claim beat [status_quo_comparator]?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. Claim: [one-line summary].
          Advancing to Stage 2."

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

### Part A — Supporting Evidence
Gather external sources bearing on the claim.
For each: Source title, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Counter-Evidence Search (MANDATORY)
Actively search for evidence favoring [status_quo_comparator] over the claim.
For each found: Source, Finding, Type (Contradicts / Complicates / Weakens).

If no counter-evidence found after active search:
  "Active counter-evidence search at Stage 2 yielded no results.
   Reason: [one specific reason].
   Running tally: 1 null. 2 evidence stages remain (S3, S4).
   Pre-committed obligations now pending — not decisions to be made at synthesis:
   — Invariant A ([adversarial_reviewer_type]) activates if S3 and S4 also null.
   — Invariant B (CE-score = -2) activates if S3 and S4 also null.
   Both were registered in ROLE A before this stage opened."

Counter-evidence found at Stage 2: [yes / no]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md. CE at S2: [found/null].
          Advancing to Stage 3."

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Internal signals favoring [status_quo_comparator].
For each: Source path, Signal, Type.

If none found:
  "No internal counter-signals found at Stage 3.
   Running tally: [N] null (S2 result: [found/null], S3: null). 1 evidence stage remains (S4).
   Pre-committed obligations remain active:
   — Invariant A ([adversarial_reviewer_type]): activates at synthesis if S4 also null.
   — Invariant B (CE-score = -2): activates at synthesis if S4 also null.
   These were locked in ROLE A — not assignable or bypassable at synthesis."

Counter-evidence found at Stage 3: [yes / no]

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md. CE at S3: [found/null].
          Advancing to Stage 4."

---

## STAGE 4 — ANALYSIS

Artifact: simulations/prove/{topic}/{topic}-analysis-{date}.md

### Part A — Evidence Assessment
Assess evidence gathered in Stages 2–3 against the hypothesis.
For each signal: Stage source, Strength (HIGH / MEDIUM / LOW), Assessment.

Thin-evidence flag: if fewer than 2 HIGH-strength signals across Stages 2–3,
flag as THIN. Propagate to synthesis with specific description.

### Part B — Counter-Evidence Assessment (MANDATORY)
Assess all counter-evidence gathered. If none gathered across S2 and S3:
  "No counter-evidence found in any collection stage.
   Running tally: [N] null. All evidence stages complete.
   Pre-committed protocol executes at synthesis — this is not a new decision.
   ROLE A Invariant A: [adversarial_reviewer_type] executes.
   ROLE A Invariant B: CE-score = -2 applies."

Counter-evidence found at Stage 4: [yes / no]

Write: simulations/prove/{topic}/{topic}-analysis-{date}.md
Confirm: "Artifact written: {topic}-analysis-{date}.md. CE at S4: [found/null].
          Thin-evidence flag: [yes/no]. Advancing to Stage 5."

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage. All mandatory sections must be present.

### Invariant Compliance Check
Retrieve from ROLE A registry:
  adversarial_reviewer_type: [confirmed]
  ce_score_formula: CE-score = -2 if all null; 0 otherwise [confirmed]
  invariant_registry_confirmed: true
Both invariants on file: [yes / no]
If no: "ROLE A invariant missing — session integrity compromised. Do not proceed."

### Counter-Evidence State
  S2: [found / null]    S3: [found / null]    S4: [found / null]
  All three null: [yes / no]

### ATOMIC DUAL-LOCK ACTIVATION
If all three stages null — one trigger, both locks fire simultaneously:

  dual_lock_fired: true
  co_activation_confirmed: true    ← must equal dual_lock_fired

  LOCK 1 — Adversarial Escalation (ROLE A Invariant A):
    Reviewer: [adversarial_reviewer_type] (pre-committed in ROLE A — not appointed now)
    Task: Challenge this claim. What evidence should this campaign have found?
          What failure mode remains unaddressed?
    Block: Promotion to topic-story blocked until adversarial review complete
           or explicitly deferred with written justification.

  LOCK 2 — Confidence Cap (ROLE A Invariant B):
    CE-score = -2 (pre-committed formula — not a synthesis judgment)
    Confidence cannot be rated HIGH while null-CE escalation is active.

  Both locks active. Partial activation is a format error.

If not all null:
  dual_lock_fired: false
  co_activation_confirmed: false
  CE-score: 0

### Findings
Summary of evidence. Reference each artifact by slug ({topic}-hypothesis, {topic}-websearch,
{topic}-intelligence, {topic}-analysis).

### Counter-Evidence Register (MANDATORY)
| Stage | Source | Finding | Type |
|-------|--------|---------|------|
If all null: recorded in ATOMIC DUAL-LOCK block above.

### Thin-Evidence Note
If Stage 4 flagged THIN: "Stage 4 flagged thin evidence: [description].
This qualifies confidence: [specific qualification]."
If not flagged: "Evidence density sufficient across collection stages."

### Confidence
Level: [HIGH / MEDIUM / LOW]
CE-score applied: [0 / -2] (pre-committed ROLE A Invariant B — not a synthesis decision)
If dual-lock fired: level cannot be HIGH.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [must equal dual_lock_fired]
  escalation_triggered: [true / false]
  escalation_reviewer: [adversarial_reviewer_type or "N/A"]
  status: [Ready / Escalated — adversarial review required before topic-story promotion]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Dual-lock: [fired / not triggered]. Co-activation: [true/false].
          Status: [Ready / Escalated]. Artifact: {topic}-synthesize-{date}.md."
```

---

## V-02 — Axis: Output Format (cumulative null-tally table)

**Variation axis**: Output format — each evidence stage produces a row in a cumulative
null-tally table that builds across the campaign. The table (Stage | CE Found | Running Null
Count | Protocol Obligations Active) is the primary null-tracking structure. Because the
table persists across stages and accumulates visibly, each null result is recorded as a row
the moment it occurs, making accumulation auditable at any point during collection rather
than only at synthesis. The co-activation echo in the Handoff uses an integrity constraint
that references the dual-lock table row.

**Hypothesis**: Forcing null results into a shared table that grows across stages makes
C-20's "per-stage accumulation" the natural output format — the tally column is filled in
once per stage, incrementing with each null. The table format also surfaces C-22 naturally:
the hypothesis frontmatter mirrors the table structure (two rows: scout gate, invariant
registry) making the dual-attestation pattern visually obvious.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. Five stages in fixed sequence. Null counter-evidence is
tracked in a running tally table — one row per evidence stage, tally accumulates.
Both CE consequences are pre-committed at campaign open. Partial activation is a format error.

---

## CAMPAIGN OPEN

Declare before any stage. Both fields mandatory — do not proceed without both.

  status_quo_comparator: [name the incumbent approach this topic must beat]
  adversarial_reviewer_type: [role most likely to challenge the claim]
  ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise

Session-level invariants. Cannot be modified after this point.

---

## NULL-TALLY TABLE
(Complete one row per evidence stage as that stage runs. Table is the authoritative
running record of CE accumulation. Protocol obligations in the rightmost column are
pre-committed consequences — not decisions to be made at synthesis.)

| Stage | Stage Name       | CE Found | Running Null Count | Protocol Obligations Active |
|-------|------------------|----------|--------------------|-----------------------------|
| S2    | Web Search       | [yes/no] | [0 or 1]           | [None / Inv-A+B pending if S3+S4 also null] |
| S3    | Intelligence Scan| [yes/no] | [0–2]              | [None / Inv-A+B execute if S4 also null] |
| S4    | Analysis         | [yes/no] | [0–3]              | [None / DUAL-LOCK fires at synthesis] |

Fill each row as you complete that stage. Do not fill forward.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Found artifacts:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

GATE S:
  gate_s_cleared: true
  invariant_registry_confirmed: true    ← separate field: attests CAMPAIGN OPEN complete

Both fields required before Stage 1 opens.

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [slug from GATE S]
  gate_s_cleared: true
  invariant_registry_confirmed: true    ← distinct from gate_s_cleared; two separate attestations
  status_quo_comparator: [from campaign open]
  adversarial_reviewer_type: [from campaign open — pre-committed]
  ce_score_formula: CE-score = -2 if all null [pre-committed]

Body:
  Claim: One testable sentence derived from the scout record. Ground in scout finding.
  Falsification: What evidence would disprove this?
  Comparator challenge: Why does this claim beat [status_quo_comparator]?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md." — advance to Stage 2.

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
  "Stage 2 counter-evidence search: null. Reason: [one specific reason].
   [Update NULL-TALLY TABLE row S2: CE Found = no, Running Null Count = 1,
    Protocol Obligations = Inv-A ([adversarial_reviewer_type]) + Inv-B (CE-score = -2)
    pending execution if S3 and S4 also null — pre-committed at campaign open.]"

Update NULL-TALLY TABLE row S2 now.

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md. S2 tally row updated." — advance to Stage 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Internal signals favoring [status_quo_comparator].
If none: "Stage 3 counter-evidence scan: null.
  [Update NULL-TALLY TABLE row S3: CE Found = no, Running Null Count = [S2 count + 1],
   Protocol Obligations = Inv-A + Inv-B execute at synthesis if S4 also null — pre-committed
   at campaign open, not assignable at synthesis.]"

Update NULL-TALLY TABLE row S3 now.

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md. S3 tally row updated." — advance to Stage 4.

---

## STAGE 4 — ANALYSIS

Artifact: simulations/prove/{topic}/{topic}-analysis-{date}.md

### Part A — Evidence Assessment
Assess evidence from S2–S3 against the hypothesis.
For each signal: Source stage, Strength (HIGH / MEDIUM / LOW), Assessment.
Thin-evidence flag: if fewer than 2 HIGH signals, flag THIN and describe what is missing.

### Part B — Counter-Evidence Assessment (MANDATORY)
Assess all counter-evidence gathered. If none:
  "Stage 4 counter-analysis: null.
   [Update NULL-TALLY TABLE row S4: CE Found = no, Running Null Count = [S2+S3+1],
    Protocol Obligations = DUAL-LOCK fires at synthesis — Inv-A + Inv-B both activate.
    This is execution of pre-committed protocol, not a new synthesis decision.]"

Update NULL-TALLY TABLE row S4 now.

Write: simulations/prove/{topic}/{topic}-analysis-{date}.md
Confirm: "Artifact written: {topic}-analysis-{date}.md. S4 tally row updated.
          Null-tally table complete." — advance to Stage 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

### Null-Tally Table (completed)
Paste the filled NULL-TALLY TABLE here. All three rows must be present.
Running null count from S4 row: [0–3]

### CE State
  All three stages null: [yes / no — derived from table]

### ATOMIC DUAL-LOCK ACTIVATION
If all three stages null — both locks fire from this single entry:

  ═══════════════════════════════════════════════════════
  DUAL-LOCK ACTIVATION — triggered by table total = 3 null
  Both locks activate from this single entry.
  Partial activation is a format error.
  ═══════════════════════════════════════════════════════

  dual_lock_fired: true
  co_activation_confirmed: true    ← must equal dual_lock_fired

  LOCK 1 — Adversarial Escalation (pre-committed Invariant A):
    Reviewer: [adversarial_reviewer_type]
    Task: Challenge this claim. What evidence was missing? What failure mode is unaddressed?
    Block: Promotion to topic-story blocked until adversarial review complete
           or deferred with written justification.

  LOCK 2 — Confidence Cap (pre-committed Invariant B):
    CE-score = -2. Confidence ceiling: MEDIUM. HIGH not available.
    cap_applied: true

  ═══════════════════════════════════════════════════════
  END DUAL-LOCK
  ═══════════════════════════════════════════════════════

If not all null: dual_lock_fired = false. co_activation_confirmed = false. CE-score = 0.

### Findings
Summary. Reference each artifact slug ({topic}-hypothesis, {topic}-websearch,
{topic}-intelligence, {topic}-analysis).

### Counter-Evidence Register (MANDATORY)
| Stage | Source | Finding | Type |
|-------|--------|---------|------|
If all null: see DUAL-LOCK ACTIVATION block above.

### Thin-Evidence
If Stage 4 THIN flag active: state the finding and how it qualifies confidence.
If not: "Evidence density sufficient."

### Confidence
Level: [HIGH / MEDIUM / LOW]
CE-score applied: [0 / -2]
If dual-lock fired: level cannot be HIGH.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [must equal dual_lock_fired]
  null_tally_final: [0–3]
  escalation_triggered: [true / false]
  escalation_reviewer: [adversarial_reviewer_type or "N/A"]
  status: [Ready / Escalated — adversarial review required before topic-story promotion]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Null tally: [N]/3. Dual-lock: [fired / not triggered].
          Co-activation: [true/false]. Status: [Ready / Escalated]."
```

---

## V-03 — Axis: Lifecycle Emphasis (STAGE ENTER / STAGE EXIT blocks with tally gate)

**Variation axis**: Lifecycle emphasis — each evidence stage is wrapped in an explicit
STAGE ENTER block (entry conditions, carry-forward state) and a STAGE EXIT block (output
summary, null-tally update, advance condition). The null tally lives in STAGE EXIT and is
a required field before the stage can close. Because the tally is a gate condition on
stage exit, not a synthesis note, null results are committed as accumulating obligations
at the moment they occur — each STAGE EXIT block uses the "X stages remain as pre-committed
obligations" language that closes C-20.

**Hypothesis**: Embedding the running tally in the lifecycle boundary (STAGE EXIT, not
just a note in the evidence body) makes it a structural gate rather than an informational
annotation. A model that skips the STAGE EXIT block cannot complete the stage — so the
tally language is always present when a null result is recorded. This closes the gap where
C-09 and C-19 both pass but C-20 fails because null accumulation is assembled retroactively
at Stage 5 rather than tracked per-stage. C-21 and C-22 are addressed by including distinct
fields in the GATE S exit block and the Handoff exit block respectively.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. Five stages in fixed sequence.
Each stage has a STAGE ENTER block (entry conditions) and a STAGE EXIT block
(output confirmation + null-tally update). STAGE EXIT is mandatory — a stage
is not complete until its exit block is written.

---

## SESSION INVARIANT REGISTRY
(Declare before Stage 0 — binding for the full session. Cannot be modified or bypassed.)

  status_quo_comparator: [name the incumbent approach this topic must beat]

  INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: all three evidence stages (S2, S3, S4) return null CE.
    Pre-committed now. If activation fires, execution is the only valid response.

  INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Pre-committed formula. Cannot be overridden by narrative confidence at synthesis.

  invariant_registry_confirmed: true
  registry_status: "Locked. Do not modify after this point."

---

## STAGE 0 — SCOUT LOAD

STAGE ENTER:
  Entry: Always open after SESSION INVARIANT REGISTRY is complete.
  Carry-forward: invariant_registry_confirmed = true from above.

Search: simulations/scout/**/{topic}-*.md

Record:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

GATE S — Required fields before STAGE 0 EXIT:
  gate_s_cleared: true
  scout_anchor: [slug]
  invariant_registry_confirmed: true    ← distinct from gate_s_cleared; traces Session Invariant Registry

If scout not found:
  gate_s_cleared: false
  "GATE S FAIL — no scout record for {topic}. Do not advance. Run scout skills first."

STAGE 0 EXIT:
  gate_s_cleared: [true / false]
  scout_anchor: [slug or "none"]
  invariant_registry_confirmed: [true]
  exit_condition: gate_s_cleared = true AND invariant_registry_confirmed = true
  Confirm: "Stage 0 complete. Scout: {scout_anchor}. Gate S cleared.
            Invariant registry confirmed. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE ENTER:
  Entry condition: Stage 0 EXIT confirmed with gate_s_cleared = true AND
                   invariant_registry_confirmed = true.
  Carry-forward: scout_anchor, status_quo_comparator, adversarial_reviewer_type.

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [from Stage 0]
  gate_s_cleared: true
  invariant_registry_confirmed: true    ← separate attestation: invariant registry was active
  status_quo_comparator: [from session invariant registry]
  adversarial_reviewer_type: [from session invariant registry — Invariant A, pre-committed]
  ce_score_formula: CE-score = -2 if all null [Invariant B, pre-committed]

Body:
  Claim: One testable sentence derived from the scout record. Ground in scout finding.
  Falsification: What evidence would disprove this?
  Comparator challenge: Why does this claim beat [status_quo_comparator]?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

STAGE 1 EXIT:
  artifact_written: {topic}-hypothesis-{date}.md
  claim_summary: [one-line claim]
  null_tally: 0  (no evidence stages have run yet)
  Confirm: "Stage 1 complete. Hypothesis written. Advancing to Stage 2."

---

## STAGE 2 — WEB SEARCH

STAGE ENTER:
  Entry condition: Stage 1 EXIT confirmed.
  Carry-forward: scout_anchor, status_quo_comparator, adversarial_reviewer_type,
                 invariant_registry_confirmed = true.

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

### Part A — Supporting Evidence
External sources for the claim.
For each: Source, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Counter-Evidence Search (MANDATORY)
Active search for evidence favoring [status_quo_comparator].
For each found: Source, Finding, Type (Contradicts / Complicates / Weakens).

If none after active search:
  "Stage 2 counter-evidence search: null result. Reason: [one specific reason]."

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md

STAGE 2 EXIT:
  artifact_written: {topic}-websearch-{date}.md
  ce_found_s2: [yes / no]
  null_tally: [0 if CE found; 1 if null]
  If null_tally = 1:
    "Running tally: 1 null. 2 evidence stages remain (S3, S4) as pre-committed obligations.
     Invariant A ([adversarial_reviewer_type]) and Invariant B (CE-score = -2) activate at
     synthesis if S3 and S4 also return null. These are locked session invariants — not
     decisions pending synthesis."
  Confirm: "Stage 2 complete. CE: [found/null]. Tally: [0/1]. Advancing to Stage 3."

---

## STAGE 3 — INTELLIGENCE SCAN

STAGE ENTER:
  Entry condition: Stage 2 EXIT confirmed.
  Carry-forward: null_tally from Stage 2, all session invariants.

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Internal signals favoring [status_quo_comparator].
If none: "Stage 3 counter-evidence scan: null result."

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md

STAGE 3 EXIT:
  artifact_written: {topic}-intelligence-{date}.md
  ce_found_s3: [yes / no]
  null_tally: [S2 tally + increment if S3 null]
  If S3 null:
    "Running tally: [N] null. 1 evidence stage remains (S4) as pre-committed obligation.
     Invariant A ([adversarial_reviewer_type]) activates at synthesis if S4 also null.
     Invariant B (CE-score = -2) activates at synthesis if S4 also null.
     Both invariants were locked in SESSION INVARIANT REGISTRY — not assignable at synthesis."
  Confirm: "Stage 3 complete. CE: [found/null]. Tally: [N]. Advancing to Stage 4."

---

## STAGE 4 — ANALYSIS

STAGE ENTER:
  Entry condition: Stage 3 EXIT confirmed.
  Carry-forward: null_tally from Stage 3, all session invariants.

Artifact: simulations/prove/{topic}/{topic}-analysis-{date}.md

### Part A — Evidence Assessment
Assess evidence from S2–S3 against the hypothesis.
For each signal: Source stage, Strength (HIGH / MEDIUM / LOW), Assessment.
Thin-evidence flag: fewer than 2 HIGH signals → flag THIN, describe gap.

### Part B — Counter-Evidence Assessment (MANDATORY)
Assess all counter-evidence gathered. If none from S2 or S3:
  "Stage 4 counter-analysis: null result."

Write: simulations/prove/{topic}/{topic}-analysis-{date}.md

STAGE 4 EXIT:
  artifact_written: {topic}-analysis-{date}.md
  ce_found_s4: [yes / no]
  null_tally_final: [S3 tally + increment if S4 null]
  thin_evidence_flag: [yes / no]
  If S4 null:
    "Running tally: [N] null. All evidence stages complete. 0 stages remain.
     Pre-committed protocol executes at synthesis — this is not a new decision.
     Invariant A: [adversarial_reviewer_type] appointed and tasked at synthesis.
     Invariant B: CE-score = -2 applied at synthesis. Both locked in SESSION INVARIANT REGISTRY."
  Confirm: "Stage 4 complete. CE: [found/null]. Final tally: [N]. Advancing to Stage 5."

---

## STAGE 5 — SYNTHESIS

STAGE ENTER:
  Entry condition: Stage 4 EXIT confirmed.
  Carry-forward: null_tally_final, thin_evidence_flag, all session invariants.

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage. All mandatory sections required.

### Session Invariant Compliance
  adversarial_reviewer_type: [confirmed from SESSION INVARIANT REGISTRY]
  ce_score_formula: CE-score = -2 if all null [confirmed]
  invariant_registry_confirmed: true
Both invariants on file: [yes / no]. If no: halt — session integrity compromised.

### CE State
  S2: [found / null]    S3: [found / null]    S4: [found / null]
  null_tally_final: [0–3]
  All three null: [yes / no]

### ATOMIC DUAL-LOCK ACTIVATION
If all three null — one trigger, both locks fire simultaneously:

  dual_lock_fired: true
  co_activation_confirmed: true    ← must equal dual_lock_fired

  LOCK 1 — Adversarial Escalation (SESSION INVARIANT A):
    Reviewer: [adversarial_reviewer_type] (pre-committed — not appointed now)
    Task: Challenge the claim. What was missing? What failure mode is unaddressed?
    Block: Promotion to topic-story blocked until adversarial review complete
           or deferred with written justification.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B):
    CE-score = -2 (locked formula — not a synthesis judgment)
    Confidence ceiling: MEDIUM. HIGH not available.

  Both locks active. Partial activation is a format error.

If not all null: dual_lock_fired = false. co_activation_confirmed = false. CE-score = 0.

### Findings
Summary. Reference each slug ({topic}-hypothesis, {topic}-websearch, {topic}-intelligence,
{topic}-analysis).

### Counter-Evidence Register (MANDATORY)
| Stage | Source | Finding | Type |
|-------|--------|---------|------|
If all null: see DUAL-LOCK ACTIVATION block above.

### Thin-Evidence
If Stage 4 flagged THIN: name the finding and qualify confidence.
If not: "Evidence density sufficient."

### Confidence
Level: [HIGH / MEDIUM / LOW]
CE-score applied: [0 / -2] (SESSION INVARIANT B — not a synthesis decision)
If dual-lock fired: level cannot be HIGH.

STAGE 5 EXIT (= Handoff):
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [must equal dual_lock_fired]
  null_tally_final: [0–3]
  escalation_triggered: [true / false]
  escalation_reviewer: [adversarial_reviewer_type or "N/A"]
  status: [Ready / Escalated — adversarial review required before topic-story promotion]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Stage 5 complete. Tally: [N]/3. Dual-lock: [fired / not triggered].
          Co-activation: [true/false]. Handoff: topic-story. Status: [Ready / Escalated]."
```

---

## V-04 — Axes: Phrasing Register + Inertia Framing

**Variation axis**: Phrasing register (conversational throughout) combined with inertia
framing (the status-quo comparator is a named, active character called "the incumbent" that
is referenced at every stage). The incumbent is introduced at campaign open as a named
position and appears in every stage's counter-evidence instructions and in every null-result
note. The running tally is framed as "what we still owe the incumbent in review" — a debt
language that makes C-20's accumulation feel like an obligation growing toward the incumbent
rather than protocol compliance.

**Hypothesis**: Naming the incumbent at campaign open and referencing it throughout each
stage (rather than only in counter-evidence sections) produces a different path to C-20 and
C-12 co-compliance: the comparator is present at every stage, not just the counter-evidence
parts. The running tally framed as "what the incumbent is still owed" makes the accumulation
feel like an obligation being tracked, not a flag being set. This framing may also be more
natural for users who think about the decision in terms of "why build this when we have X."

---

```
Topic: {topic}
Date:  {date}

You are making the evidence case for this topic. Before you commit anything, you need to
beat the incumbent — the existing approach that would keep running if this feature never
ships. Name the incumbent now. It shows up at every stage.

---

## OPENING DECLARATIONS

  incumbent: [name the status-quo approach this topic must beat — be specific]
  challenger_claim: [one sentence: what this feature does that the incumbent can't]
  reviewer_type: [the role most likely to argue for the incumbent]

These are locked at campaign open. They carry through every stage.

Null-evidence commitments (locked here — not decisions for later):
  If all three evidence stages find nothing against the incumbent:
    — Reviewer [reviewer_type] challenges the claim before topic-story promotion.
    — Confidence is capped: CE-score = -2 (locks the ceiling below HIGH).
  Both consequences are pre-registered. If they fire, you execute — you don't decide.

  invariant_registry_confirmed: true

Do not proceed without all fields above filled.

---

## STAGE 0 — SCOUT LOAD

Go find the scout record for {topic}: simulations/scout/**/{topic}-*.md

Write down what you find:
  | What you found | Path | The key signal |
  |----------------|------|----------------|
  | [slug] | [path] | [finding] |

GATE S: Before Stage 1 opens, confirm:
  gate_s_cleared: true        (you found the scout record)
  scout_anchor: [slug]
  invariant_registry_confirmed: true    (opening declarations are on file)

If you can't find a scout record, stop here and say why. Don't guess forward.

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

You're going to write the claim you'll spend the next four stages testing. It comes from
the scout record — not from what you already know about the topic.

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [from Stage 0 — named, not paraphrased]
  gate_s_cleared: true
  invariant_registry_confirmed: true    ← separate: confirms opening declarations active
  incumbent: [from opening declarations]
  reviewer_type: [from opening declarations — pre-committed]
  ce_score_formula: CE-score = -2 if all null [opening declarations — pre-committed]

Body:
  Claim: The thing you're going to prove. One sentence. Grounded in the scout finding.
  Falsification: What would make this claim wrong?
  Why not just keep using [incumbent]? [One sentence that addresses the incumbent directly]

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md — now testing it against evidence."

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

You're looking for two things: evidence that the claim is right, and evidence that
the incumbent still has a leg to stand on.

### Looking for support
External sources that back the claim.
For each: What's the source? What does it say? Does it support, complicate, or cut against?

### Defending the incumbent (MANDATORY)
Actively look for evidence that [incumbent] is still the right call — that this feature
isn't needed, or that the incumbent handles the job well enough.
For each result: Source, What it says, How it helps the incumbent's case.

If you find nothing defending the incumbent after a real search:
  "Searched for incumbent defense at Stage 2. Nothing found. Reason: [one specific reason].
   Running tally: 1 null. The incumbent is still owed a defense at S3 and S4.
   If those also come up empty: [reviewer_type] reviews the claim before promotion,
   and confidence is capped (CE-score = -2). Both were locked at opening — not my call now."

CE found at Stage 2: [yes / no]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Web search written: {topic}-websearch-{date}.md — moving to internal signals."

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

Now look inside the project. Does anything in the existing work support the claim?
Does anything suggest the incumbent is already covering this ground?

### Internal signals for the claim
Project files, prior artifacts, designs. What's there?
Record: Path, Signal type (supports / gap / risk), What it says.

### Internal signals for the incumbent (MANDATORY)
Anything internal that suggests [incumbent] is working fine and this feature is redundant?
For each: Source path, What it says, How it helps the incumbent.

If nothing internal defends the incumbent:
  "Internal scan found no support for [incumbent] at Stage 3. Null result.
   Running tally: [N] null. The incumbent is still owed one more review (S4).
   If S4 also finds nothing: [reviewer_type] challenges the claim and confidence is capped.
   Both consequences are locked at opening — not a judgment I'm making at synthesis."

CE found at Stage 3: [yes / no]

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Intelligence scan written: {topic}-intelligence-{date}.md — moving to analysis."

---

## STAGE 4 — ANALYSIS

Artifact: simulations/prove/{topic}/{topic}-analysis-{date}.md

Now you assess what you've actually gathered — including what the incumbent is owed.

### Evidence assessment
What did Stages 2 and 3 actually find for the claim?
For each signal: Where did it come from? How strong is it? What does it mean?
Thin-evidence flag: if you can't point to at least 2 solid signals, mark this THIN
and say exactly what's missing.

### Incumbent defense assessment (MANDATORY)
What did Stages 2 and 3 find for the incumbent? If nothing:
  "All collection stages found no defense for [incumbent]. Null result across S2, S3, S4.
   Running tally: [N] null. All stages complete — 0 stages remain to defend the incumbent.
   At synthesis: [reviewer_type] reviews the claim (pre-committed at opening — execution,
   not appointment). CE-score = -2 applies (pre-committed formula — execution, not judgment).
   Both obligations are paid at synthesis, not negotiated."

CE found at Stage 4: [yes / no]

Write: simulations/prove/{topic}/{topic}-analysis-{date}.md
Confirm: "Analysis written: {topic}-analysis-{date}.md — ready for synthesis."

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

This is the final brief. You're summarizing what the evidence says, applying the
pre-committed protocol if it triggers, and handing off to topic-story.

### Check the locked commitments
Retrieve from opening declarations:
  incumbent: [confirmed]
  reviewer_type: [confirmed — pre-committed Invariant A]
  ce_score_formula: CE-score = -2 if all null [confirmed — pre-committed Invariant B]
  invariant_registry_confirmed: true
Both on file: [yes / no]. If no: "Session integrity issue — invariants missing."

### Incumbent defense tally
  S2: [found / null]    S3: [found / null]    S4: [found / null]
  All three null: [yes / no]

### ATOMIC DUAL-LOCK — fires when all three stages found nothing for the incumbent

If all three null — both locks activate from this single check:

  dual_lock_fired: true
  co_activation_confirmed: true    ← must equal dual_lock_fired

  LOCK 1 — Challenge Review (pre-committed):
    [reviewer_type] is tasked: challenge this claim. What should the campaign have found?
    What risk does the incumbent handle that this feature might not?
    Topic-story is blocked until this challenge is addressed or explicitly deferred.

  LOCK 2 — Confidence Cap (pre-committed):
    CE-score = -2. Ceiling: MEDIUM. HIGH is off the table while the challenge is open.

  Both active. One trigger. Partial activation would mean the incumbent got a half-defense.

If not all null: dual_lock_fired = false. co_activation_confirmed = false. CE-score = 0.

### What the evidence shows
Summary — what did you find? Reference each artifact by slug.

### Incumbent defense record (MANDATORY)
Everything found that defends the incumbent.
| Stage | Source | Finding | Type |
|-------|--------|---------|------|
If nothing found: see DUAL-LOCK above.

### Thin-evidence note
If Stage 4 flagged THIN: describe what's missing and qualify confidence accordingly.
If not: "Evidence was sufficient."

### Confidence
Level: [HIGH / MEDIUM / LOW]
CE-score applied: [0 / -2] (locked at opening — not a synthesis call)
If challenge review is open: level cannot be HIGH.

### Handoff to topic-story
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [must equal dual_lock_fired]
  challenge_reviewer: [reviewer_type or "N/A"]
  escalation_triggered: [true / false]
  status: [Ready / Challenged — [reviewer_type] review required before topic-story]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Evidence brief complete. Dual-lock: [fired / not triggered].
          Co-activation: [true/false]. Status: [Ready / Challenged]."
```

---

## V-05 — Axes: Role Sequence + Output Format + Inertia Framing (combined)

**Variation axis**: Three axes combined. Role sequence (V-01): the invariant registry is
verified in a distinct ROLE A before the scout load in ROLE B. Output format (V-02): each
evidence stage produces a row in a cumulative incumbent-defense table. Inertia framing
(V-04): the status-quo comparator is the "incumbent" throughout, and the running tally is
framed as outstanding incumbent-defense obligations. The table accumulates incumbent-defense
results per stage, making C-20 structural (tally in table row), C-22 structural (two
blocking roles produce two fields), and C-21 structural (co-activation mirrors the
dual-lock row from the table into the Handoff).

**Hypothesis**: When all three axes are active simultaneously, the three v6 criteria
arise from distinct structural sources rather than from three separate instructions on a
single-axis prompt. C-20 arises from the table row structure (V-02 axis), C-22 arises
from the two-role blocking structure (V-01 axis), and C-21 arises from the table's
dual-lock row being echoed into the Handoff (combined). No single axis can be dropped
without losing at least one criterion — making the variation a stress test of whether
multi-axis combination is more robust than single-axis approaches for the v6 severity stack.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. The incumbent is the status-quo approach you must beat.
Two pre-evidence roles lock the protocol and load the scout record.
Evidence stages track incumbent-defense results in a running table.
Both null-CE consequences fire atomically if all stages fail to find incumbent defense.

---

## ROLE A — INVARIANT REGISTRY LOCK

Execute first. Lock the null-CE protocol and name the incumbent.

  incumbent: [name the status-quo approach this topic must beat — be specific]
  reviewer_type: [role most likely to defend the incumbent]
  ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise

  SESSION INVARIANT A — Reviewer:
    Activation: all three evidence stages return null incumbent defense.
    Status: pre-registered now. If activation fires, execution only.

  SESSION INVARIANT B — Cap:
    ce_score_formula above. Locked. Cannot be overridden at synthesis.

  invariant_registry_confirmed: true
  registry_note: "Locked. Cannot be modified after ROLE A."

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

Execute after ROLE A.

Search: simulations/scout/**/{topic}-*.md

Found:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

GATE S:
  gate_s_cleared: true
  scout_anchor: [slug]
  invariant_registry_confirmed: true    ← echoed from ROLE A

If scout not found: gate_s_cleared = false. STOP.
"GATE S FAIL — no scout record. ROLE A invariants are locked but scout prerequisite unmet."

ROLE B COMPLETE. Both prerequisites confirmed — open Stage 1.

---

## INCUMBENT-DEFENSE TABLE
(Fill one row per evidence stage as that stage runs. Do not fill forward.)

| Stage | Stage Name        | Incumbent Defense Found | Running Null Count | Obligations Active |
|-------|-------------------|-------------------------|--------------------|--------------------|
| S2    | Web Search        | [yes/no]                | [0 or 1]           | [None / A+B pending if S3+S4 null] |
| S3    | Intelligence Scan | [yes/no]                | [0–2]              | [None / A+B execute if S4 null] |
| S4    | Analysis          | [yes/no]                | [0–3]              | [None / DUAL-LOCK at synthesis] |

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [from ROLE B]
  gate_s_cleared: true                  ← ROLE B output
  invariant_registry_confirmed: true    ← ROLE A output (distinct field)
  incumbent: [from ROLE A]
  reviewer_type: [from ROLE A — pre-committed]
  ce_score_formula: CE-score = -2 if all null [from ROLE A — pre-committed]

Body:
  Claim: One testable sentence from the scout record.
  Falsification: What would disprove this?
  Why not [incumbent]?: One sentence — what does this claim provide that the incumbent can't?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. Advancing to Stage 2."

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

### Part A — Claim Evidence
External sources supporting the claim.
For each: Source, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Incumbent Defense (MANDATORY)
Active search for evidence that [incumbent] is still adequate.
For each: Source, Finding, Type (Contradicts / Complicates / Weakens the claim).

If none after active search:
  "Stage 2 incumbent-defense search: null. Reason: [one specific reason].
   [Update INCUMBENT-DEFENSE TABLE row S2: Defense Found = no, Running Null = 1,
    Obligations = A ([reviewer_type]) + B (CE-score = -2) pending if S3+S4 also null.
    Pre-committed in ROLE A — not a synthesis decision.]"

Update INCUMBENT-DEFENSE TABLE row S2.

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md. S2 table row updated. Advancing to Stage 3."

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals for Claim
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Incumbent Defense (MANDATORY)
Internal signals suggesting [incumbent] is adequate.
If none: "Stage 3 incumbent-defense scan: null.
  [Update INCUMBENT-DEFENSE TABLE row S3: Defense Found = no, Running Null = [S2+1],
   Obligations = A + B execute at synthesis if S4 also null.
   Pre-committed in ROLE A — not assignable at synthesis.]"

Update INCUMBENT-DEFENSE TABLE row S3.

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md. S3 table row updated. Advancing to Stage 4."

---

## STAGE 4 — ANALYSIS

Artifact: simulations/prove/{topic}/{topic}-analysis-{date}.md

### Part A — Evidence Assessment
Assess signals from S2–S3 against the hypothesis.
For each: Source stage, Strength (HIGH / MEDIUM / LOW), Assessment.
Thin-evidence flag: fewer than 2 HIGH signals → flag THIN, describe the gap.

### Part B — Incumbent Defense Assessment (MANDATORY)
Assess all incumbent-defense evidence from S2 and S3. If none from either:
  "Stage 4 incumbent-defense assessment: null. No defense found across S2, S3, S4.
   [Update INCUMBENT-DEFENSE TABLE row S4: Defense Found = no, Running Null = [S2+S3+1],
    Obligations = DUAL-LOCK fires at synthesis. Invariant A: [reviewer_type] executes.
    Invariant B: CE-score = -2 applies. Both pre-committed in ROLE A — execution only.]"

Update INCUMBENT-DEFENSE TABLE row S4.

Write: simulations/prove/{topic}/{topic}-analysis-{date}.md
Confirm: "Artifact written: {topic}-analysis-{date}.md. S4 table row updated.
          Incumbent-defense table complete. Thin flag: [yes/no]. Advancing to Stage 5."

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

### ROLE A Invariant Compliance
  reviewer_type: [confirmed from ROLE A]
  ce_score_formula: CE-score = -2 if all null [confirmed from ROLE A]
  invariant_registry_confirmed: true
Both on file: [yes / no]. If no: halt.

### Incumbent-Defense Table (completed)
Paste filled INCUMBENT-DEFENSE TABLE here. All three rows required.
Running null count from S4 row: [0–3]

### CE State
  All three null: [yes / no — derived from table]

### ATOMIC DUAL-LOCK
If all three null — one trigger, both locks fire simultaneously:

  ═══════════════════════════════════════════════════════════════
  DUAL-LOCK ACTIVATION — table total = 3 null incumbent defense
  Both locks activate from this single entry.
  Partial activation is a format error.
  ═══════════════════════════════════════════════════════════════

  dual_lock_fired: true
  co_activation_confirmed: true    ← must equal dual_lock_fired

  LOCK 1 — Reviewer Challenge (ROLE A Invariant A):
    [reviewer_type] is tasked: challenge the claim from the incumbent's position.
    What evidence was absent? What risk does the incumbent handle that this claim doesn't?
    Promotion to topic-story blocked until challenge addressed or explicitly deferred.

  LOCK 2 — Confidence Cap (ROLE A Invariant B):
    CE-score = -2. Ceiling: MEDIUM. HIGH not available while challenge is open.
    cap_applied: true

  ═══════════════════════════════════════════════════════════════
  END DUAL-LOCK
  ═══════════════════════════════════════════════════════════════

If not all null: dual_lock_fired = false. co_activation_confirmed = false. CE-score = 0.

### Findings
Summary. Reference each artifact slug: {topic}-hypothesis, {topic}-websearch,
{topic}-intelligence, {topic}-analysis.

### Incumbent Defense Register (MANDATORY)
| Stage | Source | Finding | Type |
|-------|--------|---------|------|
If all null: see DUAL-LOCK block above.

### Thin-Evidence
If Stage 4 flagged THIN: name the finding, qualify confidence.
If not: "Evidence density sufficient."

### Confidence
Level: [HIGH / MEDIUM / LOW]
CE-score applied: [0 / -2] (ROLE A Invariant B — not a synthesis decision)
If dual-lock fired: level cannot be HIGH.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [must equal dual_lock_fired]
  null_tally_final: [0–3]
  incumbent_defense_closed: [true if all null, false if any found]
  escalation_triggered: [true / false]
  escalation_reviewer: [reviewer_type or "N/A"]
  status: [Ready / Challenged — [reviewer_type] review required before topic-story]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Evidence brief complete. Incumbent-defense table: [N]/3 null.
          Dual-lock: [fired / not triggered]. Co-activation: [true/false].
          Status: [Ready / Challenged]. Handoff: topic-story."
```
