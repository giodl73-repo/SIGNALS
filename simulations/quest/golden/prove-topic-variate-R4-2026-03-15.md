---
skill: quest-variate
skill_target: prove-topic
round: R4
date: 2026-03-15
rubric: prove-topic-rubric-v4-2026-03-15.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [adversarial_escalation, mechanical_ce_cap, stage_exit_integrity]
  combined: [V-04, V-05]
r3_high_scores: V-04/V-05 (C-14 mandatory counter-evidence, C-15 gate_s_cleared in artifact)
r4_targets: C-16 (null counter-evidence triggers adversarial escalation), C-17 (confidence mechanically capped by counter-evidence state)
severity_stack: "C-14 (recording) -> C-16 (escalation) -> C-17 (consequence) — all three required to close the null counter-evidence path"
---

# prove-topic — Variation Round R4

Five complete, runnable skill body prompts. Each is self-contained — no diff, no cross-references.

Round 4 targets C-16 and C-17, the two new criteria in rubric v4. These criteria close the
null counter-evidence path: C-14 requires recording, C-16 requires escalation, C-17 requires
a mechanical consequence on the confidence composite. A variation that passes C-14 but not
C-16/C-17 records the null result and then ignores it — the gap these two criteria close.

Single-axis variations (V-01, V-02, V-03) isolate one design decision each.
Combined variations (V-04, V-05) compound the highest-signal combinations.

---

## V-01 — Axis: Adversarial Escalation Protocol (C-16)

**Variation axis**: Adversarial escalation — when null counter-evidence is found at any
evidence stage, the campaign enters an escalated state. An adversarial reviewer type is
registered at campaign open. Null results at any stage activate the escalation path: a
named review task is created, the synthesis handoff status is set to ESCALATED (not Ready),
and promotion to topic-story is blocked until the adversarial review is either completed
or explicitly deferred with justification.

**Hypothesis**: Naming an adversarial reviewer type at campaign open and requiring the null
counter-evidence path to activate a concrete escalation task (not just a warning) prevents
the campaign from quietly completing with HIGH confidence on uniformly supportive evidence.
The escalation state in the handoff artifact forces the downstream topic-story author to
act, not just observe.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Five stages run in fixed sequence. Null counter-evidence escalates — it does not pass through.

---

## CAMPAIGN OPEN

Register before any stage begins:

  status_quo_comparator: [name the incumbent approach this topic must beat]
  adversarial_reviewer_type: [name the role or perspective most likely to challenge the
                               claim — e.g., "engineer who has shipped the status-quo",
                               "PM skeptical of new tooling", "domain expert favoring
                               existing approach"]
  escalation_triggered: false   (updated to true if null counter-evidence found)

Both fields mandatory. Do not proceed without filling both.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record all found artifacts:
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
Gather external sources for the claim.
For each: Title, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Counter-Evidence Search (MANDATORY)
Actively search for evidence favoring [status_quo_comparator] over the claim.
For each result: Source, Finding, Type (Contradicts / Complicates / Weakens).

If no counter-evidence found after active search:
  "Active counter-evidence search at Stage 2 yielded no results.
  Possible reasons: [at least one specific reason].
  Null result recorded.
  ESCALATION NOTE: If Stage 3 and Stage 4 also yield null counter-evidence,
  the campaign will enter escalated state and promotion will be blocked."

Counter-evidence found at this stage: [yes / no]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md" — advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Look for internal signals favoring [status_quo_comparator].
For each: Source, Signal, Type.

If none found:
  "Active internal counter-evidence scan yielded no results.
  Possible reasons: [at least one specific reason].
  Null result recorded."

Counter-evidence found at this stage: [yes / no]

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

Counter-evidence found at this stage: [yes / no]

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: {topic}-prototype-{date}.md" — advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

Required sections — all mandatory:

### Findings
  Summary of what the evidence shows. Reference each artifact by slug.

### Counter-Evidence Register
  MANDATORY. All counter-evidence from S2, S3, and S4.
  | Stage | Source | Finding | Type |
  |-------|--------|---------|------|

  Aggregate null check:
    Stages with counter-evidence: S2=[yes/no]  S3=[yes/no]  S4=[yes/no]

  If ALL THREE stages returned null counter-evidence:
    "No counter-evidence gathered across all three evidence stages. Active searches
    were conducted per campaign protocol at each stage. Null result recorded.

    ADVERSARIAL ESCALATION ACTIVATED:
    Reviewer: [adversarial_reviewer_type from campaign open]
    Attack task: Challenge the claim from the perspective of someone who has shipped
                 [status_quo_comparator]. Specifically: what evidence would you expect
                 to find that this campaign missed? What failure mode does this claim
                 ignore?
    Escalation requirement: This campaign is blocked from promoting to topic-story
                            until the adversarial review task is completed or explicitly
                            deferred with documented justification.

    Update campaign state: escalation_triggered: true"

### Confidence
  Level: [HIGH / MEDIUM / LOW]
  Rationale: Derived from evidence across all three stages.
  Escalation adjustment: If escalation_triggered is true, confidence cannot be rated HIGH.
                         Level is set to MEDIUM at maximum pending adversarial review.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  escalation_triggered: [true / false]
  status: [Ready / Escalated — adversarial review required before topic-story promotion]
  escalation_reviewer: [adversarial_reviewer_type or "N/A"]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Artifact written: {topic}-synthesize-{date}.md.
         Status: [Ready / Escalated]."
```

---

## V-02 — Axis: Mechanical Counter-Evidence Cap (C-17)

**Variation axis**: Mechanical counter-evidence cap — the confidence composite is computed
using a formula that includes an explicit counter-evidence score (CE-score). The CE-score
is derived mechanically from counter-evidence state, not verbal judgment:
- Counter-evidence found (any stage): CE-score = 0 (no penalty — search was conducted)
- Null counter-evidence across ALL stages: CE-score = -2 (penalty subtracted from composite)

The composite formula is fixed: `(S2 × 0.30 + S3 × 0.30 + S4 × 0.40) + CE-score`.
The cap is mechanical — the number produced by the formula determines the level, not the
narrator's post-hoc assessment of how confident they feel.

**Hypothesis**: Expressing the null counter-evidence penalty as a fixed numeric subtraction
in the composite formula prevents the synthesis from treating "no counter-evidence found"
as a neutral outcome. The CE-score makes the consequence of the null path observable,
auditable, and reproducible — a reviewer can recompute the composite from the stage scores
and verify the level assignment without reading the prose.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. Confidence is computed from a fixed formula.
Counter-evidence state is a first-class input to the formula.

---

## CONFIDENCE FORMULA

Initialize at campaign open. Fill in as stages complete.

  Evidence stage scores (0-10 per stage):
    Stage 2 score: ___ / 10
    Stage 3 score: ___ / 10
    Stage 4 score: ___ / 10

  Evidence composite: (S2 × 0.30) + (S3 × 0.30) + (S4 × 0.40) = ___

  Counter-evidence score (CE-score):
    Rule: If counter-evidence was found in AT LEAST ONE of S2, S3, S4:
          CE-score = 0
    Rule: If null counter-evidence across ALL of S2, S3, S4:
          CE-score = -2

  Final composite: evidence_composite + CE-score = ___

  Level mapping:
    7.0 and above: HIGH
    4.0 to 6.9:    MEDIUM
    below 4.0:     LOW

  The level is assigned by the formula result. Verbal override is not permitted.

Evidence stage scoring guide:
  9-10 = Multiple independent strong sources, no gaps
  7-8  = Clear support, minor gaps
  5-6  = Mixed or limited evidence
  3-4  = Thin or inconsistent evidence
  0-2  = No useful evidence or strong contradictions

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record:
  | Slug | Key finding |
  |------|-------------|
  | [slug] | [finding] |

GATE S: Scout confirmed. gate_s_cleared: true
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
  status_quo_comparator: [name the incumbent approach]
  initial_score_estimate: ___ / 10

Body:
  Claim: One testable sentence derived from the scout record.
  Falsification: What evidence would disprove this?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Artifact written: {topic}-hypothesis-{date}.md" — advance to STAGE 2.

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

Gather external evidence for and against the claim.
For each source: Finding, Verdict (Supports / Contradicts / Neutral).

Counter-evidence: List any contradicting sources.
If none found after active search:
  "No external counter-evidence found. Null result recorded."

Stage 2 score: ___ / 10
Score rationale: One sentence.
Counter-evidence found: [yes / no]
Update formula: Stage 2 score → [value]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md" — advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

Scan internal sources. Record: Path, Signal type, Finding.

Counter-evidence: Internal signals favoring the status-quo comparator.
If none: "No internal counter-signals found. Null result recorded."

Stage 3 score: ___ / 10
Score rationale: One sentence.
Counter-evidence found: [yes / no]
Update formula: Stage 3 score → [value]

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md" — advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

Design and describe a minimal experiment. Record: Setup, Result, Verdict.

Counter-evidence: Any results contradicting the claim.
If none: "Prototype results uniformly supportive. Null counter-evidence recorded."

Stage 4 score: ___ / 10
Score rationale: One sentence.
Counter-evidence found: [yes / no]
Update formula: Stage 4 score → [value]

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: {topic}-prototype-{date}.md" — advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

Required sections — all mandatory:

### Formula Computation
  Stage scores:
    S2: ___ / 10  (weight 30%)  contribution: ___
    S3: ___ / 10  (weight 30%)  contribution: ___
    S4: ___ / 10  (weight 40%)  contribution: ___
  Evidence composite: ___

  Counter-evidence state:
    S2 counter-evidence: [found / null]
    S3 counter-evidence: [found / null]
    S4 counter-evidence: [found / null]
    Any stage with counter-evidence: [yes / no]

  CE-score:
    If yes: CE-score = 0
    If no (all null): CE-score = -2
    CE-score applied: ___

  Final composite: evidence_composite + CE-score = ___
  Level (from formula): [HIGH / MEDIUM / LOW]

  The level assigned above is the confidence level. No adjustment by prose judgment.

### Findings
  What the evidence shows. Reference each artifact by slug.

### Counter-Evidence
  MANDATORY. All counter-evidence from S2, S3, S4. If all null:
    "No counter-evidence gathered in any stage. CE-score of -2 applied.
    Final composite reflects this deduction. Null result not suppressed."

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level from formula]
  composite_score: [final composite] / 10
  ce_score_applied: [0 / -2]
  status: [Ready / Needs more evidence — specify]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Artifact: {topic}-synthesize-{date}.md. Ready for topic-story."
```

---

## V-03 — Axis: Stage-Exit Integrity Gate (process compliance checkpoint at every stage)

**Variation axis**: Stage-exit integrity gate — every evidence stage (S2, S3, S4) ends with
a mandatory 3-item compliance gate before the write instruction executes. The gate checks:
(1) counter-evidence search conducted, (2) artifact path follows topic-prefix convention,
(3) finding linked to prior artifact or scout record. All three must be confirmed — an
unchecked gate blocks the write. The synthesis compiles a 12-item campaign integrity summary
(4 gates × 3 items) so downstream reviewers can audit process compliance without replaying
the session.

**Hypothesis**: Placing a 3-item compliance gate at the exit of each evidence stage converts
the skill from a sequence of content instructions into a verifiable process — each gate
creates an explicit moment where the model must confirm it did the thing, not just produce
content adjacent to it. The synthesis integrity summary makes the audit artifact-portable.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. Each evidence stage exits through a compliance gate.
All gate items must confirm before the write instruction runs.

---

## STAGE-EXIT GATE FORMAT

Every evidence stage ends with:

  EXIT GATE — Stage N:
    [ ] Counter-evidence search conducted (yes / no)
    [ ] Artifact path follows {topic}-[signal]-{date}.md convention (yes / no)
    [ ] Finding linked to scout record or prior artifact (yes / no)

  All three must be checked [yes] before the Write instruction executes.
  If any item is [no]: resolve before proceeding. Do not skip or defer.

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
  status_quo_comparator: [name the incumbent approach]

Body:
  Claim: One testable sentence derived from the scout record.
  Falsification: What evidence would disprove this?

Note: Stage 1 produces a hypothesis, not an evidence artifact. No exit gate required.

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Artifact written: {topic}-hypothesis-{date}.md" — advance to STAGE 2.

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

Gather external evidence for and against the claim.
For each source: Finding, Verdict (Supports / Contradicts / Neutral).

Counter-evidence: Actively search for sources favoring the status_quo_comparator.
If none after active search: "No external counter-evidence found. Null result recorded."

  EXIT GATE — Stage 2:
    [ ] Counter-evidence search conducted and result recorded (yes / no)
    [ ] Artifact path is simulations/prove/{topic}/{topic}-websearch-{date}.md (yes / no)
    [ ] Findings are grounded in the claim stated in {topic}-hypothesis-{date}.md (yes / no)

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Gate S2 cleared. Artifact written: {topic}-websearch-{date}.md" — advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

Scan internal sources. Record: Path, Signal type (supports / gap / risk), Finding.

Counter-evidence: Internal signals favoring the status-quo comparator.
If none: "No internal counter-signals. Null result recorded."

  EXIT GATE — Stage 3:
    [ ] Counter-evidence scan conducted and result recorded (yes / no)
    [ ] Artifact path is simulations/prove/{topic}/{topic}-intelligence-{date}.md (yes / no)
    [ ] Findings link back to {topic}-websearch-{date}.md or {topic}-hypothesis-{date}.md (yes / no)

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Gate S3 cleared. Artifact written: {topic}-intelligence-{date}.md" — advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

Design a minimal experiment. Record: Setup, Result, Verdict.

Counter-evidence: Results contradicting the claim.
If none: "Prototype results uniformly supportive. Null counter-evidence recorded."

  EXIT GATE — Stage 4:
    [ ] Counter-evidence search or counter-experiment conducted and result recorded (yes / no)
    [ ] Artifact path is simulations/prove/{topic}/{topic}-prototype-{date}.md (yes / no)
    [ ] Experiment result linked to claim in {topic}-hypothesis-{date}.md (yes / no)

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Gate S4 cleared. Artifact written: {topic}-prototype-{date}.md" — advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

Required sections — all mandatory:

### Campaign Integrity Summary
  Compile all gate results from S2, S3, S4:
  | Stage | Counter-evidence conducted | Path correct | Finding linked |
  |-------|---------------------------|--------------|----------------|
  | S2    | [yes / no]                | [yes / no]   | [yes / no]     |
  | S3    | [yes / no]                | [yes / no]   | [yes / no]     |
  | S4    | [yes / no]                | [yes / no]   | [yes / no]     |
  Total gate items passed: ___ / 9
  Any failures: [list stage and item, or "none"]

### Findings
  What the evidence shows. Reference each artifact by path.

### Counter-Evidence
  MANDATORY. All counter-evidence from S2, S3, S4.
  If no counter-evidence found across all stages:
    "No counter-evidence gathered in any stage. Active searches were conducted per gate
    protocol (all counter-evidence gate items confirmed [yes]). Null result recorded.
    Recommend adversarial review before topic-story promotion."

### Confidence
  Level: [HIGH / MEDIUM / LOW]
  Integrity score: [N] / 9 gates passed
  Rationale: Derived from evidence and integrity summary.
  If any gate item failed: note the impact on confidence reliability.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  integrity_score: [N] / 9
  status: [Ready / Conditional — specify]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Artifact: {topic}-synthesize-{date}.md. Ready for topic-story."
```

---

## V-04 — Combined: C-16 + C-17 Severity Stack (adversarial escalation + mechanical cap)

**Variation axis**: This variation closes the full null counter-evidence severity stack by
combining V-01 (adversarial escalation protocol) with V-02 (mechanical CE-score penalty):
- C-14: Null counter-evidence is recorded at each stage (base requirement)
- C-16: Null across all stages triggers adversarial escalation with named reviewer and
  blocked handoff status
- C-17: Null across all stages applies CE-score = -2, reducing the composite and
  mechanically preventing HIGH confidence

The two consequences are mechanically linked: you cannot have CE-score penalty without
escalation_triggered, and you cannot clear escalation without either adversarial review
completed or explicit deferral. The synthesis cannot produce HIGH confidence AND Ready
status on a null counter-evidence campaign.

**Hypothesis**: The combination of a numeric penalty AND a status block creates a two-lock
mechanism on the null counter-evidence path. Breaking through requires either finding
counter-evidence (which lifts both locks) or explicitly addressing the adversarial escalation
AND accepting the reduced composite — you cannot accidentally pass through unnoticed.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. Null counter-evidence across all stages triggers two
consequences: (1) CE-score penalty in the composite formula, (2) adversarial escalation
that blocks promotion. Both locks are required to close the null path.

---

## CAMPAIGN OPEN

Register before any stage begins:

  status_quo_comparator: [name the incumbent approach this topic must beat]
  adversarial_reviewer_type: [name the role most likely to challenge the claim]

  confidence_formula:
    evidence_composite: (S2 × 0.30) + (S3 × 0.30) + (S4 × 0.40)
    CE-score: 0 if any stage found counter-evidence; -2 if all stages null
    final_composite: evidence_composite + CE-score
    level: HIGH (≥7.0) / MEDIUM (4.0-6.9) / LOW (<4.0)

  escalation_state: not_triggered   (updated to triggered if all stages null)

All three registrations mandatory. Do not proceed without filling all three.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

GATE S — all items required:
  [ ] scout_path: [confirmed]
  [ ] key_finding: [recorded]
  [ ] status_quo_comparator: [registered]
  [ ] adversarial_reviewer_type: [registered]
  gate_s_cleared: true

Do not open Stage 1 without all items confirmed.

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
For each source: Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Counter-Evidence Search (MANDATORY)
Actively search for evidence favoring [status_quo_comparator].
For each result: Source, Finding, Type.

If none found after active search:
  "Active counter-evidence search at Stage 2 yielded no results.
  Possible reasons: [at least one]. Null result recorded."

Stage 2 score: ___ / 10
Counter-evidence found at Stage 2: [yes / no]
Update formula: Stage 2 score → [value]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md" — advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type, Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Look for internal signals favoring [status_quo_comparator].
If none: "No internal counter-signals. Null result recorded."

Stage 3 score: ___ / 10
Counter-evidence found at Stage 3: [yes / no]
Update formula: Stage 3 score → [value]

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md" — advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

### Part A — Claim Test
Design a minimal experiment. Record: Setup, Result, Verdict.

### Part B — Counter-Experiment (MANDATORY)
Test a scenario where [status_quo_comparator] would outperform the claim.
If not testable: "Reason: [specific]. Limitation propagates to synthesis."

Stage 4 score: ___ / 10
Counter-evidence found at Stage 4: [yes / no]
Update formula: Stage 4 score → [value]

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: {topic}-prototype-{date}.md" — advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage. Two-lock null counter-evidence check runs at synthesis open.

### Null Counter-Evidence Check (runs before all other sections)

  Counter-evidence state:
    S2: [found / null]    S3: [found / null]    S4: [found / null]
    Any stage with counter-evidence: [yes / no]

  LOCK 1 — CE-score (C-17 mechanical cap):
    If any stage found counter-evidence: CE-score = 0
    If all stages null: CE-score = -2

  LOCK 2 — Escalation state (C-16 adversarial escalation):
    If all stages null:
      "ADVERSARIAL ESCALATION TRIGGERED.
      Reviewer: [adversarial_reviewer_type from campaign open]
      Attack task: Challenge the claim from the perspective of [adversarial_reviewer_type].
                   What evidence would they expect to find? What failure mode is unaddressed?
      Escalation requirement: Promotion to topic-story is blocked until this review is
                              completed OR explicitly deferred with written justification.
      Update escalation_state: triggered"

### Formula Computation
  S2: ___ × 0.30 = ___
  S3: ___ × 0.30 = ___
  S4: ___ × 0.40 = ___
  Evidence composite: ___
  CE-score applied: [0 / -2]
  Final composite: ___
  Level (from formula — no override): [HIGH / MEDIUM / LOW]

### Findings
  What the evidence shows. Reference each artifact by slug.

### Counter-Evidence Register
  MANDATORY. All counter-evidence from S2, S3, S4.
  | Stage | Source | Finding | Type |
  |-------|--------|---------|------|

  If all null: see adversarial escalation block above.

### Status-Quo Comparison
  Claim evidence vs. [status_quo_comparator].
  Verdict: Replace / Augment / Coexist / Insufficient to determine.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level from formula]
  composite_score: [final_composite] / 10
  ce_score_applied: [0 / -2]
  escalation_state: [not_triggered / triggered]
  status: [Ready / Escalated — adversarial review required before topic-story promotion]
  escalation_reviewer: [adversarial_reviewer_type or "N/A"]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Artifact: {topic}-synthesize-{date}.md. Status: [Ready / Escalated]."
```

---

## V-05 — Combined: Full Excellence Signal Compound (R3 V-05 + C-16 + C-17 integrated)

**Variation axis**: This variation extends R3's V-05 (the accumulated excellence compound
through Round 3) by fully integrating C-16 and C-17 into its structure. The base from R3 V-05:
- GATE S with 4-checkbox clearance (C-11)
- Per-artifact full path in every write instruction (C-13)
- Status-quo comparator registered at session open (C-12)
- gate_s_cleared in hypothesis frontmatter (C-15)
- Mandatory counter-evidence with null fallback (C-14)
- Evidence weighting ledger with confidence cap (R3 V-01)

R4 additions:
- Adversarial reviewer type registered at campaign open, escalation_state tracked (C-16)
- CE-score as a formal input to the confidence formula (C-17)
- Adversarial escalation activated when all counter-evidence stages return null

**Hypothesis**: The R3 V-05 compound was the highest-scoring configuration for criteria
C-01 through C-15. Adding C-16 and C-17 without removing any existing mechanism produces
a configuration that satisfies all 17 criteria simultaneously. The additional mechanisms
are additive, not conflicting — CE-score supplements the evidence ledger cap, escalation
supplements the null counter-evidence recording.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. All five stages in fixed sequence.
No stage opens without the preceding artifact confirmed.
Null counter-evidence triggers two mechanical consequences: CE-score penalty and
adversarial escalation. Both must be resolved before promotion.

---

## CAMPAIGN OPEN

Register before any stage begins:

  status_quo_comparator: [name the incumbent approach this topic must beat]
  adversarial_reviewer_type: [name the role most likely to challenge the claim]

  evidence_ledger:
    web_search:   weight: 30%   quality: [to be filled]
    intelligence: weight: 30%   quality: [to be filled]
    prototype:    weight: 40%   quality: [to be filled]

  confidence_formula:
    evidence_composite: (S2 × 0.30) + (S3 × 0.30) + (S4 × 0.40)
    CE-score: 0 if any stage found counter-evidence; -2 if all null
    prototype_cap: if prototype quality = Thin, final composite cannot exceed 6.9 (MEDIUM)
    final_composite: evidence_composite + CE-score  [capped if prototype Thin]
    level: HIGH (≥7.0) / MEDIUM (4.0-6.9) / LOW (<4.0)

  escalation_state: not_triggered

All registrations mandatory. Do not proceed without filling all fields.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

GATE S — all four items required before Stage 1 opens:
  [ ] scout_path: [confirmed path]
  [ ] key_finding: [recorded]
  [ ] status_quo_comparator: [registered at campaign open]
  [ ] evidence_ledger: [initialized with weights and adversarial_reviewer_type registered]
  gate_s_cleared: true

Do not open Stage 1 until all four are confirmed.

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
  status_quo_comparator: [from campaign open]
  adversarial_reviewer_type: [from campaign open]
  evidence_weights_registered: true

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
  Possible reasons: [at least one specific reason].
  Null result recorded explicitly."

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
Look for internal signals favoring [status_quo_comparator].
For each: Source, Signal, Type.

If none: "No internal counter-signals found. Null result recorded."

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

### Null Counter-Evidence Check (runs first, before all other sections)

  Counter-evidence state:
    S2: [found / null]    S3: [found / null]    S4: [found / null]
    Any stage with counter-evidence: [yes / no]

  CE-score:
    Any found → CE-score = 0
    All null  → CE-score = -2 AND escalation_state → triggered

  If escalation triggered:
    "ADVERSARIAL ESCALATION TRIGGERED.
    Reviewer: [adversarial_reviewer_type from campaign open]
    Attack task: Challenge the claim from the perspective of [adversarial_reviewer_type].
                 What evidence would they expect to find? What failure mode is unaddressed?
    Block: Promotion to topic-story requires adversarial review completion or explicit
           written deferral with justification."

### Evidence Ledger Final
  | Stage | Evidence Type | Weight | Quality   | Score / 10 | Contribution |
  |-------|--------------|--------|-----------|------------|--------------|
  | S2    | Web Search   | 30%    | [verdict] | [score]    | [×0.30]      |
  | S3    | Intelligence | 30%    | [verdict] | [score]    | [×0.30]      |
  | S4    | Prototype    | 40%    | [verdict] | [score]    | [×0.40]      |
  Evidence composite: ___
  CE-score: [0 / -2]
  Prototype cap applied: [yes / no]
  Final composite (after CE-score and cap): ___
  Level (from formula — no override): [HIGH / MEDIUM / LOW]

### Findings
  Summary of what the evidence shows. Reference each artifact by full path.

### Counter-Evidence Register
  MANDATORY. All counter-evidence from S2, S3, and S4.
  | Stage | Source | Finding | Type |
  |-------|--------|---------|------|

  If all null: see adversarial escalation block above. CE-score of -2 applied to formula.
  Null result is not suppressed. Uniformly supportive evidence is a campaign integrity flag.

### Status-Quo Comparison
  Claim evidence vs. [status_quo_comparator from campaign open].
  Verdict: Replace / Augment / Coexist / Insufficient to determine.
  Counter-experiment result (Stage 4 Part B): [verdict or limitation note].

### Composite Confidence
  Computed from formula. Not assigned by judgment.
  Final composite: [N] / 10
  Level: [HIGH / MEDIUM / LOW]
  Prototype cap: [yes / no]
  CE-score applied: [0 / -2]
  Counter-evidence impact: [None found — CE-score applied / Present-weak / Present-material]

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level from formula]
  composite_score: [final_composite] / 10
  ce_score_applied: [0 / -2]
  escalation_state: [not_triggered / triggered]
  status: [Ready / Escalated — adversarial review required before topic-story promotion]
  escalation_reviewer: [adversarial_reviewer_type or "N/A"]
  ready: [true / false — if false, specify blocker]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Campaign complete. simulations/prove/{topic}/{topic}-synthesize-{date}.md written.
         Status: [Ready / Escalated]. Confidence: [level] ([composite] / 10)."
```
