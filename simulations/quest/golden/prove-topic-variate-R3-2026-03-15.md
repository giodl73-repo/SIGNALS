---
skill: quest-variate
skill_target: prove-topic
round: R3
date: 2026-03-15
rubric: prove-topic-rubric-v3-2026-03-15.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [evidence_weighting, confidence_calibration, artifact_chaining]
  combined: [V-04, V-05]
r2_high_scores: V-04/V-05 (C-14 counter-evidence mandatory, C-15 gate_s_cleared in frontmatter)
r3_targets: C-14 (unconditional counter-evidence section), C-15 (gate clearance in artifact)
---

# prove-topic — Variation Round R3

Five complete, runnable skill body prompts. Each is self-contained — no diff, no cross-references.

Round 3 builds on the R2 excellence signals now formalized as C-14 and C-15 in rubric v3.
Single-axis variations (V-01, V-02, V-03) isolate one design decision each.
Combined variations (V-04, V-05) compound the highest-signal combinations.

---

## V-01 — Axis: Evidence Weighting (weighted ledger per evidence type)

**Variation axis**: Evidence weighting — each evidence stage contributes a named weight to a
campaign-level evidence ledger. Weights are registered at session open and referenced by the
synthesis when computing composite confidence. Thin evidence at a high-weight stage has a
larger confidence impact than thin evidence at a low-weight stage.

**Hypothesis**: Making evidence weights explicit at session open causes the synthesis to
produce confidence levels calibrated to the actual distribution of evidence gathered, rather
than a flat average that treats a weak prototype result the same as a weak web search.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Five stages execute in fixed order. Each stage writes its artifact before the next begins.

---

## CAMPAIGN OPEN — Evidence Ledger Initialization

Before loading scout signals, initialize the evidence ledger for this campaign.

  evidence_ledger:
    web_search:   weight: 30%   quality: [to be filled]
    intelligence: weight: 30%   quality: [to be filled]
    prototype:    weight: 40%   quality: [to be filled]

Quality scale:  Strong / Moderate / Thin
Weight rationale: Prototype results are the most direct empirical test of the claim.
                  Web and intelligence stages provide confirmatory external and internal
                  context, weighted equally.

Rule: If the prototype stage (40%) returns Thin, the synthesis confidence is capped at
MEDIUM regardless of web and intelligence quality.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

For each artifact found, record:
  | Slug | Namespace | Key finding (one sentence) |
  |------|-----------|---------------------------|
  | [slug] | [ns] | [finding] |

If no artifacts found:
  "No prior scout signals. Hypothesis proceeds from stated assumptions."

GATE S: Scout record is on file before proceeding. Do not write the hypothesis
until this gate is confirmed. Record: gate_s_cleared: true

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [slug from GATE S, or "assumption" if no scout found]
  gate_s_cleared: true
  evidence_weights_registered: true

Body:
  Claim: One testable sentence derived from the scout record (or stated assumption).
  Falsification: What observable outcome would disprove this?
  Status-quo comparator: Name the incumbent approach this claim must beat.

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Artifact written: {topic}-hypothesis-{date}.md" — then advance to STAGE 2.

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

Evidence weight: 30%

Gather external evidence related to the claim.
For each source: Title, Finding, Verdict (Supports / Contradicts / Neutral).

Counter-evidence: List any sources that contradict the claim or favor the status-quo.
If none found after active search:
  "No external counter-evidence found. Null result recorded. Active search conducted."

Evidence quality for ledger: [Strong / Moderate / Thin]
Update evidence ledger: web_search quality: [verdict]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md" — then advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

Evidence weight: 30%

Scan internal sources (project files, prior artifacts, existing designs).
For each source: Path, Signal type (supports / gap / risk), Finding.

Counter-evidence: List any internal signals favoring the status-quo comparator.
If none: "No internal counter-signals found. Null result recorded."

If internal sources are sparse, note: thin_evidence: true

Evidence quality for ledger: [Strong / Moderate / Thin]
Update evidence ledger: intelligence quality: [verdict]

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md" — then advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

Evidence weight: 40%

Design and describe a minimal experiment that tests the claim directly.
Setup: what was built or simulated.
Result: what happened.
Verdict: Confirms / Partially confirms / Disconfirms.

Counter-evidence: Any prototype results that contradict the claim.
If none: "Prototype results uniformly supportive. Null counter-evidence recorded."

Evidence quality for ledger: [Strong / Moderate / Thin]
Update evidence ledger: prototype quality: [verdict]

Weight-adjusted propagation:
  If prototype quality is Thin (40% weight):
    Set thin_evidence_cap: true — synthesis confidence cannot exceed MEDIUM.
  If web or intelligence is Thin (30% each):
    Note in synthesis, no automatic cap.

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: {topic}-prototype-{date}.md" — then advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage. No further stages follow this one.

Required sections — all mandatory:

### Evidence Ledger Final
  | Stage | Evidence Type | Weight | Quality |
  |-------|--------------|--------|---------|
  | S2 | Web Search   | 30%    | [from ledger] |
  | S3 | Intelligence | 30%    | [from ledger] |
  | S4 | Prototype    | 40%    | [from ledger] |
  Thin evidence stages: [list or "none"]
  Cap applied: [yes — prototype thin / no]

### Findings
  Summarize what the evidence shows. Reference each stage artifact by slug.

### Counter-Evidence
  MANDATORY. List all counter-evidence gathered in S2, S3, and S4.
  If no counter-evidence was found in any stage:
    "No counter-evidence gathered across the campaign. All evidence was uniformly
    supportive of the claim. This uniformity is recorded as a null result, not
    suppressed. Recommend adversarial review before promotion to topic-story.
    Confidence is subject to confirmation bias risk."

### Composite Confidence
  Level: [HIGH / MEDIUM / LOW]
  Weight-adjusted rationale: derive from ledger weights and quality verdicts.
  If thin_evidence_cap is true: Level cannot exceed MEDIUM.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  status: [Ready / Needs more evidence — specify]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Artifact written: {topic}-synthesize-{date}.md. Ready for topic-story."
```

---

## V-02 — Axis: Confidence Calibration (numeric per-stage scoring that aggregates)

**Variation axis**: Confidence calibration — each evidence stage produces a numeric confidence
score (0–10) before advancing. The synthesis aggregates stage scores using the campaign's
evidence weights into a composite. Any stage scoring below 4 triggers an automatic cap.
The numeric trail is visible in each artifact's frontmatter.

**Hypothesis**: Requiring an explicit numeric confidence score at each evidence stage prevents
the synthesis from ignoring weak mid-campaign signals. A stage that produces no useful
evidence cannot be rounded up by strong results elsewhere.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Stages run in fixed sequence. Each stage scores its evidence contribution before the
next stage opens.

---

## CONFIDENCE LEDGER

Initialize at session open. Fill in as stages complete.

  Stage 2 score: ___ / 10
  Stage 3 score: ___ / 10
  Stage 4 score: ___ / 10
  Composite:     ___ / 10  (weighted: S2 × 0.30 + S3 × 0.30 + S4 × 0.40)

Scoring guide:
  9–10 = Multiple independent strong sources, no counter-evidence
  7–8  = Clear support, minor gaps or weak counter-evidence
  5–6  = Mixed evidence, some counter-evidence present
  3–4  = Thin or contradictory evidence
  0–2  = No useful evidence or strong contradictions

Cap rule: If any single stage scores < 4, synthesis confidence is capped at LOW
regardless of other stage scores.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record found artifacts:
  | Slug | Key finding |
  |------|-------------|
  | [slug] | [finding] |

GATE S: Scout record confirmed. Record: gate_s_cleared: true
Do not advance to Stage 1 until this gate is confirmed.

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
  initial_confidence: [N] / 10
  initial_confidence_rationale: [one sentence]

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
If none found: "No external counter-evidence found."

Stage 2 confidence score: ___ / 10
Score rationale: One sentence explaining the score.
Update confidence ledger: Stage 2 → [score]

If score < 4: "WARNING: Stage 2 thin evidence. Synthesis confidence capped at LOW."

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md" — advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

Scan internal sources (project files, prior artifacts, existing designs).
For each source: Path, Signal type, Finding.

Counter-evidence: List internal signals favoring the status-quo comparator.
If none: "No internal counter-signals found."

Stage 3 confidence score: ___ / 10
Score rationale: One sentence.
Update confidence ledger: Stage 3 → [score]

If score < 4: "WARNING: Stage 3 thin evidence. Synthesis confidence capped at LOW."

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md" — advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

Design and describe a minimal experiment. Record: Setup, Result, Verdict.

Counter-evidence: Any results contradicting the claim.
If none: "Prototype results uniformly supportive."

Stage 4 confidence score: ___ / 10
Score rationale: One sentence.
Update confidence ledger: Stage 4 → [score]

If score < 4: "WARNING: Stage 4 thin evidence (40% weight). Synthesis confidence
capped at LOW. This is the highest-weight stage — low score has proportional impact."

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: {topic}-prototype-{date}.md" — advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage. No further stages follow.

Required sections — all mandatory:

### Confidence Ledger Final
  | Stage | Type | Weight | Score / 10 | Weighted contribution |
  |-------|------|--------|------------|----------------------|
  | S2 | Web Search   | 30% | [score] | [score × 0.30] |
  | S3 | Intelligence | 30% | [score] | [score × 0.30] |
  | S4 | Prototype    | 40% | [score] | [score × 0.40] |
  Composite: [sum] / 10
  Cap triggered: [yes — Stage N scored < 4] or [no cap]

### Findings
  What the evidence shows. Reference each stage artifact by slug.

### Counter-Evidence
  MANDATORY. All counter-evidence gathered in S2, S3, S4.
  If no counter-evidence was found in any stage:
    "No counter-evidence gathered in any stage. Null result recorded.
    Confidence composite adjusted: maximum score reduced by 1 point to account
    for absence of adversarial signal. Recommend adversarial review before
    topic-story promotion."

### Composite Confidence
  Score: [composite] / 10
  Level: [HIGH (7–10) / MEDIUM (5–6) / LOW (0–4)]
  Cap applied: [yes / no]
  Counter-evidence impact: [none / present-weak / present-material]

### Status-Quo Comparison
  Does the evidence support replacing [status_quo_comparator], augmenting it,
  or is evidence insufficient to determine? State clearly.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [HIGH / MEDIUM / LOW]
  composite_score: [N] / 10

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Artifact written: {topic}-synthesize-{date}.md. Ready for topic-story."
```

---

## V-03 — Axis: Artifact Chaining (prior_artifact field in every frontmatter)

**Variation axis**: Artifact chaining — each artifact's frontmatter includes a `prior_artifact`
field naming the immediately preceding artifact. This creates an explicit, traversable chain
from the scout artifact through synthesis. Reviewers and downstream tools can audit the full
evidence lineage from any artifact in the chain without replaying the session.

**Hypothesis**: Requiring each artifact to name its predecessor in frontmatter prevents
orphaned artifacts and makes it immediately visible if a stage was skipped or out of order —
because the chain will have a broken link.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Each artifact names its predecessor in frontmatter. This creates an auditable chain.
Five stages run in fixed sequence.

---

## ARTIFACT CHAIN

The chain for this campaign:

  [scout artifact]                         (input — loaded, not written)
  → {topic}-hypothesis-{date}.md           (Stage 1)
  → {topic}-websearch-{date}.md            (Stage 2)
  → {topic}-intelligence-{date}.md         (Stage 3)
  → {topic}-prototype-{date}.md            (Stage 4)
  → {topic}-synthesize-{date}.md           (Stage 5 — terminal)

Rule: Every artifact frontmatter must include:
  prior_artifact: [full path of immediately preceding artifact]
A missing prior_artifact field means the chain is broken.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record:
  | Path | Key finding |
  |------|-------------|
  | [path] | [finding] |

GATE S: Confirm scout artifact path before proceeding.
Record: gate_s_cleared: true  scout_path: [confirmed path]
Do not open Stage 1 without this confirmation.

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  prior_artifact: [scout path from GATE S]
  scout_anchor: [scout slug]
  gate_s_cleared: true
  status_quo_comparator: [name the incumbent approach]

Body:
  Claim: One testable sentence derived from the scout record.
  Falsification: What would disprove this?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Chain link 1 written: {topic}-hypothesis-{date}.md"
Advance to STAGE 2.

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-websearch
  prior_artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Gather external evidence. For each source: Finding, Verdict (Supports/Contradicts/Neutral).

Counter-evidence: List any contradicting sources.
If none found after search: "No external counter-evidence found. Null result recorded."

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Chain link 2 written: {topic}-websearch-{date}.md"
Advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-intelligence
  prior_artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md
  thin_evidence_inherited: [true if Stage 2 evidence was Thin, else false]

Scan internal sources. Record: Path, Signal type, Finding.

Counter-evidence: Internal signals favoring the status-quo comparator.
If none: "No internal counter-signals. Null result recorded."

Thin evidence flag: If sparse, set thin_evidence: true — this propagates to Stage 4.

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Chain link 3 written: {topic}-intelligence-{date}.md"
Advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-prototype
  prior_artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md
  thin_evidence_inherited: [true if Stage 2 or 3 set thin_evidence, else false]

Design and describe a minimal experiment. Record: Setup, Result, Verdict.

Counter-evidence: Results contradicting the claim.
If none: "Prototype results uniformly supportive. Null counter-evidence recorded."

Thin evidence propagation:
  If any of Stages 2, 3, or 4 has thin evidence, set:
    thin_evidence_propagated: true
  This field is read by Stage 5 to set the confidence cap.

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Chain link 4 written: {topic}-prototype-{date}.md"
Advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage. This is the last link in the chain.

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-synthesize
  prior_artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md
  chain_complete: true
  next_artifact: topic-story

Required sections — all mandatory:

### Chain Summary
  | Link | Artifact | Key output |
  |------|----------|------------|
  | S0 | [scout slug] | [key finding] |
  | S1 | {topic}-hypothesis-{date}.md | [claim] |
  | S2 | {topic}-websearch-{date}.md  | [verdict] |
  | S3 | {topic}-intelligence-{date}.md | [verdict] |
  | S4 | {topic}-prototype-{date}.md  | [verdict] |

### Findings
  What the evidence chain shows. Reference each artifact by path.

### Counter-Evidence
  MANDATORY. All counter-evidence from S2, S3, and S4.
  If none found across any stage:
    "No counter-evidence gathered in the chain. Null result recorded.
    Recommend adversarial review before promoting to topic-story.
    Confidence is subject to confirmation bias — cannot be rated HIGH without
    adversarial input."

### Confidence
  Level: [HIGH / MEDIUM / LOW]
  Thin evidence stages: [list from thin_evidence_propagated, or "none"]
  Rationale: Derived from chain evidence and propagation flags.

### Handoff
  This artifact is the direct input to topic-story.
  next: topic-story
  status: [Ready / Conditional — specify requirement]
  confidence: [level]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Chain complete. Final artifact: {topic}-synthesize-{date}.md. Ready for topic-story."
```

---

## V-04 — Combined: Active Counter-Evidence Posture + Gate Trace Density (C-14 + C-15 amplified)

**Variation axis**: This variation makes counter-evidence gathering a first-class active task
at every evidence stage — not a retrospective audit at synthesis. Each evidence stage has
a mandatory counter-evidence search sub-section with a required null-result fallback. Gate
clearance propagates not just into hypothesis frontmatter but into a campaign preamble block
that all stages reference.

**Hypothesis**: When counter-evidence search is structurally required at each evidence stage
(with an explicit null fallback), the synthesis counter-evidence section reflects active
search rather than passive aggregation — raising the evidentiary bar for HIGH confidence
claims and surfacing the absence of opposing evidence as a signal requiring explanation.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. Counter-evidence is an active target at every stage,
not a synthesis afterthought. Gate clearance propagates through the artifact chain.

---

## CAMPAIGN PREAMBLE

Register before any stage begins:

  status_quo_comparator: [name the incumbent — the approach this topic must beat]
  counter_evidence_target: [name the most likely form of opposing evidence]

These registrations anchor the counter-evidence search at every stage.
Both fields are mandatory. Do not proceed without filling both.

---

## STAGE 0 — SCOUT LOAD + GATE

Search: simulations/scout/**/{topic}-*.md

Record all found artifacts:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

GATE S CLEARANCE — all four items required before Stage 1 opens:
  [ ] scout_path: [confirmed path]
  [ ] key_finding: [recorded]
  [ ] status_quo_comparator: [registered in preamble]
  [ ] counter_evidence_target: [registered in preamble]
  gate_s_cleared: true

Do not open Stage 1 until all four checkboxes are marked.

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [slug from GATE S]
  gate_s_cleared: true
  gate_s_path: [scout path confirmed at GATE S]
  status_quo_comparator: [from preamble]
  counter_evidence_target: [from preamble]

Body:
  Claim: One testable sentence derived from the scout record.
  Falsification: What would disprove this?
  Why claim beats status-quo: One sentence addressing the comparator directly.

Note: gate_s_cleared and gate_s_path appear in this artifact so gate compliance
can be audited from the artifact chain without replaying the session.

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Artifact written: {topic}-hypothesis-{date}.md" — advance to STAGE 2.

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

Carry forward from preamble:
  status_quo_comparator: [from preamble]
  counter_evidence_target: [from preamble]

### Part A — Supporting Evidence
For each source: Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Counter-Evidence Search (MANDATORY)
Actively search for:
  (a) Evidence supporting the status_quo_comparator over the claim
  (b) Evidence matching the counter_evidence_target

For each result: Source, Finding, Type (Contradicts / Complicates / Weakens).

If no counter-evidence found after active search:
  "Active counter-evidence search at Stage 2 yielded no results.
  Possible reasons: [list at least one genuine reason].
  This null result is recorded explicitly, not elided."

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md" — advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

Carry forward: status_quo_comparator, counter_evidence_target.

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Look specifically for internal signals favoring the status_quo_comparator.
For each: Source, Signal, Type.

If none found:
  "Active internal counter-evidence scan yielded no results.
  Possible reasons: [list at least one].
  Null result recorded."

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md" — advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

Carry forward: status_quo_comparator, counter_evidence_target.

### Part A — Claim Test
Design a minimal experiment. Record: Setup, Result, Verdict.

### Part B — Counter-Experiment (MANDATORY)
Test or describe a scenario where the status_quo_comparator would outperform the claim.
Record: Scenario, Status-quo result, Claim result, Comparison verdict.

If no counter-scenario is testable:
  "Status-quo comparison not testable at prototype stage.
  Reason: [specific reason].
  This limitation propagates to synthesis confidence."

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: {topic}-prototype-{date}.md" — advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

Required sections — all mandatory:

### Findings
  What the evidence shows. Reference each stage artifact by path.

### Counter-Evidence Register
  MANDATORY. Aggregate all counter-evidence from Stages 2, 3, and 4.
  | Stage | Source | Finding | Type |
  |-------|--------|---------|------|
  | S2 | ... | ... | ... |
  | S3 | ... | ... | ... |
  | S4 | ... | ... | ... |

  If no counter-evidence was gathered in any stage:
    "No counter-evidence gathered across all three active search stages.
    Active searches were conducted per campaign protocol. This may indicate:
    (a) genuine absence of opposing evidence for this claim, or
    (b) a gap in search coverage or comparator framing.
    Confidence is not rated HIGH on this basis alone. Adversarial review is
    required before promoting to topic-story. Confidence adjusted to MEDIUM max."

### Status-Quo Comparison
  Claim evidence vs. [status_quo_comparator].
  Verdict: Replace / Augment / Coexist / Insufficient to determine.
  Counter-experiment result (from Stage 4): [verdict or limitation note].

### Confidence
  Level: [HIGH / MEDIUM / LOW]
  Counter-evidence impact: [None found (adjusted) / Present-weak / Present-material]
  Rationale: Derive from evidence chain and counter-evidence quality.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  counter_evidence_status: [None found / Present — see register]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Synthesis complete. Artifact written: {topic}-synthesize-{date}.md. Ready for topic-story."
```

---

## V-05 — Combined: Full Excellence Signal Compound (R1 + R2 + evidence weighting)

**Variation axis**: This variation compounds all proven excellence signals across R1 and R2
with the evidence weighting axis introduced in V-01 of this round:
- GATE S with 4-checkbox clearance (R1 C-11)
- Per-artifact full path in every write instruction (R1 C-13)
- Status-quo comparator registered at session open (R1 C-12)
- gate_s_cleared in hypothesis frontmatter (R2 C-15)
- Mandatory counter-evidence with null fallback (R2 C-14)
- Evidence weighting ledger with confidence cap (R3 V-01)

**Hypothesis**: Compounding all accumulated excellence signals into a single variation
produces the highest-scoring rubric result by eliminating every known failure mode in
one skill body. The combination cost — cognitive load — is worth paying because a
practitioner running prove-topic only runs it once per topic.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. All five stages run in fixed sequence.
No stage opens without the preceding artifact confirmed.

---

## CAMPAIGN OPEN

Register before any stage begins:

  status_quo_comparator: [name the incumbent approach this topic must beat]

  evidence_ledger:
    web_search:   weight: 30%   quality: [to be filled]
    intelligence: weight: 30%   quality: [to be filled]
    prototype:    weight: 40%   quality: [to be filled]

  Cap rule: Prototype quality Thin → confidence cannot exceed MEDIUM.

Both registrations are mandatory. Do not proceed without filling both.

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
  [ ] evidence_ledger: [initialized]
  gate_s_cleared: true

Do not open Stage 1 without all four confirmed.

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [slug from GATE S]
  scout_path: [path from GATE S]
  gate_s_cleared: true
  status_quo_comparator: [from campaign open]
  evidence_weights_registered: true

Body:
  Claim: One testable sentence derived from the scout record.
         Link explicitly to the scout finding that grounds it.
         Do not derive from general knowledge.
  Falsification: What evidence would disprove this?
  Why claim beats status-quo: One sentence addressing the comparator directly.

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Artifact written: {topic}-hypothesis-{date}.md" — advance to STAGE 2.

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

Evidence weight: 30%

### Part A — Supporting Evidence
Gather external evidence for the claim.
For each source: Title, Finding, Strength (Strong / Moderate / Weak).

### Part B — Counter-Evidence Search (MANDATORY)
Actively search for evidence favoring the status_quo_comparator.
For each result: Source, Finding, Type (Contradicts / Complicates / Weakens).

If none found after active search:
  "Active counter-evidence search at Stage 2 yielded no results.
  Possible reasons: [at least one]. Null result recorded."

Evidence quality: [Strong / Moderate / Thin]
Update evidence ledger: web_search quality: [verdict]

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md" — advance to STAGE 3.

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

Evidence weight: 30%

### Part A — Internal Signals
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Counter-Evidence Scan (MANDATORY)
Look for internal signals favoring the status_quo_comparator.
For each: Source, Signal, Type.

If none: "No internal counter-signals found. Null result recorded."

Evidence quality: [Strong / Moderate / Thin]
Update evidence ledger: intelligence quality: [verdict]

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md" — advance to STAGE 4.

---

## STAGE 4 — PROTOTYPE

Artifact: simulations/prove/{topic}/{topic}-prototype-{date}.md

Evidence weight: 40%

### Part A — Claim Test
Design a minimal experiment. Record: Setup, Result, Verdict.

### Part B — Counter-Experiment (MANDATORY)
Test or describe a scenario favoring the status_quo_comparator.
Record: Scenario, Status-quo result, Claim result, Verdict.
If not testable: "Reason: [specific]. Limitation propagates to synthesis."

Evidence quality: [Strong / Moderate / Thin]
Update evidence ledger: prototype quality: [verdict]

Weight-adjusted cap:
  If prototype quality is Thin:
    Set thin_evidence_cap: true
    "WARNING: Prototype stage (40% weight) is Thin. Synthesis confidence capped at MEDIUM."

Write: simulations/prove/{topic}/{topic}-prototype-{date}.md
Confirm: "Artifact written: {topic}-prototype-{date}.md" — advance to STAGE 5.

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage. No stages follow this one.

Required sections — all mandatory, no conditional elision:

### Evidence Ledger Final
  | Stage | Evidence Type | Weight | Quality |
  |-------|--------------|--------|---------|
  | S2 | Web Search   | 30% | [verdict] |
  | S3 | Intelligence | 30% | [verdict] |
  | S4 | Prototype    | 40% | [verdict] |
  Thin evidence stages: [list or "none"]
  Cap applied: [yes — prototype thin / no]

### Findings
  Summary of what the evidence shows. Reference each artifact by full path.

### Counter-Evidence Register
  MANDATORY. All counter-evidence from S2, S3, and S4.
  | Stage | Source | Finding | Type |
  |-------|--------|---------|------|

  If no counter-evidence was found across any stage:
    "No counter-evidence gathered across all three evidence stages.
    Active searches were conducted per campaign protocol at each stage.
    Null result recorded — not suppressed. This cannot be treated as confirmation.
    Confidence is capped at HIGH-with-caveat pending adversarial review.
    Recommend naming an adversarial reviewer before topic-story promotion."

### Status-Quo Comparison
  Claim evidence vs. [status_quo_comparator from campaign open].
  Verdict: Replace / Augment / Coexist / Insufficient to determine.
  Counter-experiment result: [from Stage 4 Part B, or limitation note].

### Composite Confidence
  Weighted by evidence ledger.
  Level: [HIGH / MEDIUM / LOW]
  Cap applied: [yes / no]
  Counter-evidence impact: [None found (see register) / Present-weak / Present-material]
  Rationale: Derive from ledger weights, quality verdicts, and counter-evidence register.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  counter_evidence_status: [None found / Present]
  ready: [true / false — if false, specify blocker]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Campaign complete. {topic}-synthesize-{date}.md ready for topic-story."
```
