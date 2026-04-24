---
skill: quest-variate
skill_target: prove-topic
round: R11
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [falsification_gate, evidence_gap_accounting, stage_handoff_verification]
  combined: [V-04 (falsification_gate + evidence_gap_accounting), V-05 (all_three + full_R10_stack)]
r10_anchor: >
  R10 V-05 established the full structural stack for v14: conviction_ladder (Speculative
  opening, tier move rules, trajectory), counter_claim_chain (Stage 1 declares 2-3
  counter-claims, evidence stages address each, Stage 4 resolves each, synthesis lists
  unresolved as named risks), and evidence_provenance_tracking (every evidence item carries
  source + claim_addressed + forward_path; Stage 4 only concludes from items with complete
  chains; synthesis reports provenance_completeness). All R11 variations carry the R10
  must-haves: explicit scout-blocking, per-stage artifact writes with full paths,
  scout_source in hypothesis frontmatter, THIN: flagging at point of discovery, exact
  readiness statement closing synthesis.
r11_context: >
  R10 brought three axes that strengthen evidential accounting inside stages. R11 probes
  three orthogonal axes that reinforce campaign-level structure: what the hypothesis
  commits to falsify (upfront accountability), what each stage was unable to find
  (gap honesty), and what each stage formally hands to the next (chain-of-custody).

  V-01 (single: falsification_gate): The hypothesis must declare 2-3 explicit falsification
  conditions before Stage 2 begins. Each evidence stage checks whether any condition has
  been triggered (Triggered / Not Triggered / Ambiguous). Stage 4 produces a falsification
  verdict per condition. Synthesis cannot assert SUPPORTED when any condition is Ambiguous
  without naming it as a residual uncertainty. This forces the hypothesis to be committal
  before evidence collection, preventing the hypothesis from drifting toward whatever the
  evidence happens to say.

  V-02 (single: evidence_gap_accounting): Each evidence stage declares 1-2 items it
  actively sought but did not find (SOUGHT_NOT_FOUND list). Stage 5 synthesis opens with
  an EVIDENCE GAP SUMMARY: total sought_not_found count across all stages, and a
  gap-derived confidence cap (0-1 gaps = unconstrained, 2-3 gaps = confidence cap PARTIAL,
  4+ gaps = confidence cap LOW). The cap is applied before the final verdict.

  V-03 (single: stage_handoff_verification): Every stage closes with a committed HANDOFF
  BLOCK naming exactly three fields: artifact_written (path), claims_forwarded (2-3
  sentences), verdicts_forwarded (named verdicts the next stage must reference). The
  following stage's ENTRY CONDITIONS require "HANDOFF from Stage N received" before any
  work begins. Stage 5 synthesis constructs its verdict exclusively from the accumulated
  HANDOFF BLOCKs -- stage bodies are not re-read during synthesis.

  V-04 (combined: falsification_gate + evidence_gap_accounting): V-01 + V-02. Falsification
  conditions declared at Stage 1. Evidence stages check trigger status AND record gaps.
  Stage 4 resolves falsification conditions. Stage 5 opens with EVIDENCE GAP SUMMARY, then
  integrates falsification verdicts into the confidence rating. Tests whether honesty-at-
  collection (gaps) and commitment-before-collection (falsification) reinforce each other.

  V-05 (full: all_three + complete R10 V-05 stack): falsification_gate + evidence_gap_
  accounting + stage_handoff_verification layered on the full R10 V-05 baseline
  (conviction_ladder + counter_claim_chain + evidence_provenance_tracking). Stage 1
  declares counter-claims, opens at Speculative, seeds provenance headers, and registers
  falsification conditions. Evidence stages advance provenance chains, check falsification
  trigger status, record gaps, apply conviction moves per counter-claim resolution, and
  close with HANDOFF BLOCKs. Stage 4 produces a joint verdict matrix. Stage 5 opens with
  EVIDENCE GAP SUMMARY, resolves falsification per condition, reads exclusively from
  HANDOFF BLOCKs, and closes with the exact readiness statement.
---

# prove-topic Variations -- Round 11 (Rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-10 aspirational)
**Date**: 2026-03-16
**Round**: R11

---

## Artifact Paths (all variations)

| Stage | Signal             | Path                                                                        |
|-------|--------------------|-----------------------------------------------------------------------------|
| 1     | prove-hypothesis   | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`     |
| 2     | prove-websearch    | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`       |
| 3     | prove-intelligence | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |
| 4     | prove-analysis     | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`         |
| 5     | prove-synthesize   | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`     |

---

## V-01 -- Axis: Falsification Gate

**Variation axis**: falsification_gate only. The hypothesis must declare 2-3 explicit
falsification conditions before Stage 2 begins. Each evidence stage checks whether any
condition has been triggered. Stage 4 produces a per-condition falsification verdict.
Synthesis cannot claim SUPPORTED when any condition is Ambiguous.

**Hypothesis**: Without upfront falsification conditions the hypothesis is a moving
target -- the investigator can rationalize evidence toward the hypothesis rather than
testing it. Declaring falsification conditions before evidence collection forecloses
this drift: a SUPPORTED verdict must pass through conditions that had a real chance of
being triggered. This also surfaces the clearest gap between confidence and the strongest
case against the hypothesis, making the synthesis directly useful to a skeptical reviewer.

---

```
Topic: {topic}
Date:  {date}

Run the full prove evidence campaign for {topic}.
Five stages in fixed order: hypothesis, websearch, intelligence, analysis, synthesize.
Each stage writes one artifact. No stage begins until the prior stage artifact is written.

## SETUP

Glob: simulations/scout/{topic}-scout-*.md

If no file found:
  Emit: "SCOUT GATE: BLOCKED -- no scout artifact for {topic}. Run /scout first."
  Halt. Stage 1 cannot begin under any condition.
If found:
  scout_source: [path]
  Emit: "SCOUT GATE: CLEARED. scout_source: [path]"

Stage 1 is structurally blocked until SCOUT GATE: CLEARED fires.

---

## STAGE 1 -- HYPOTHESIS

Entry: SCOUT GATE: CLEARED fired.

Read the scout artifact at scout_source. Do not use general knowledge as a substitute.

Frame a falsifiable hypothesis grounded in scout content.
Then declare 2-3 explicit falsification conditions.

  hypothesis: [falsifiable claim about {topic}]
  status_quo_comparator: [the incumbent approach or product this topic must displace]

  FALSIFICATION CONDITIONS (locked before Stage 2 begins):
  | ID  | Condition (what evidence would prove the hypothesis false) |
  |-----|----------------------------------------------------------|
  | F-1 | [condition 1]                                            |
  | F-2 | [condition 2]                                            |
  | F-3 | [condition 3 -- optional]                                |

  falsification_conditions_locked: true

Note: Falsification conditions cannot be modified after this stage is written.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE -- [path]"

Stage 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH

Entry: STAGE 1 COMPLETE fired.

Gather minimum 3 external sources. For each source, record evidence and check
whether it triggers any falsification condition.

| # | Source (URL or title) | One-line summary | F-1 status | F-2 status | F-3 status |
|---|----------------------|-----------------|-----------|-----------|-----------|
| 1 | [source]             | [summary]       | [T/NT/A]  | [T/NT/A]  | [T/NT/A]  |
| 2 | [source]             | [summary]       | [T/NT/A]  | [T/NT/A]  | [T/NT/A]  |
| 3 | [source]             | [summary]       | [T/NT/A]  | [T/NT/A]  | [T/NT/A]  |

T = Triggered  NT = Not Triggered  A = Ambiguous

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

  s2_falsification_running_tally:
    F-1: [Triggered / Not Triggered / Ambiguous -- most adverse status across items]
    F-2: [Triggered / Not Triggered / Ambiguous]
    F-3: [Triggered / Not Triggered / Ambiguous]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE -- [path] | falsification tally: [summary]"

Stage 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE

Entry: STAGE 2 COMPLETE fired.

Search internal sources. Minimum 2 internal files. Record file-path citation for each.

| # | File path | Key finding (1 sentence) | F-1 status | F-2 status | F-3 status |
|---|-----------|--------------------------|-----------|-----------|-----------|
| 1 | [path]    | [finding]               | [T/NT/A]  | [T/NT/A]  | [T/NT/A]  |
| 2 | [path]    | [finding]               | [T/NT/A]  | [T/NT/A]  | [T/NT/A]  |

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

  s3_falsification_running_tally:
    F-1: [worst status so far across Stage 2 + Stage 3]
    F-2: [worst status so far across Stage 2 + Stage 3]
    F-3: [worst status so far across Stage 2 + Stage 3]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE -- [path] | falsification tally: [summary]"

Stage 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS

Entry: STAGE 3 COMPLETE fired.

Identify patterns across Stage 2 and Stage 3 evidence. Distinguish correlation from
causation. Record source attribution for each pattern claim.

Then produce the final falsification verdict per condition.

  FALSIFICATION VERDICT TABLE:
  | ID  | Condition        | Final status | Evidence basis (1 sentence) |
  |-----|------------------|--------------|-----------------------------|
  | F-1 | [from Stage 1]   | [T/NT/A]     | [cite stage artifact]       |
  | F-2 | [from Stage 1]   | [T/NT/A]     | [cite stage artifact]       |
  | F-3 | [from Stage 1]   | [T/NT/A]     | [cite stage artifact]       |

  any_condition_triggered: [true / false]
  any_condition_ambiguous: [true / false]

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE -- [path] | any_triggered: [t/f] | any_ambiguous: [t/f]"

Stage 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIZE

Entry: STAGE 4 COMPLETE fired.

### FALSIFICATION RESOLUTION

For each condition from Stage 1:

| ID  | Condition | Final status | Effect on verdict |
|-----|-----------|-------------|------------------|
| F-1 | [cond]    | [T/NT/A]    | [Blocks SUPPORTED / No effect / Named uncertainty] |
| F-2 | [cond]    | [T/NT/A]    | [Blocks SUPPORTED / No effect / Named uncertainty] |
| F-3 | [cond]    | [T/NT/A]    | [Blocks SUPPORTED / No effect / Named uncertainty] |

FALSIFICATION CEILING RULE:
  - If any_condition_triggered = true: verdict cannot exceed PARTIALLY SUPPORTED.
  - If any_condition_ambiguous = true: name each ambiguous condition as a residual
    uncertainty before stating the verdict.

### SYNTHESIS

  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary: [2-3 sentences integrating Stages 2, 3, 4]
  confidence: [High / Medium / Low]
  residual_uncertainties: [list any ambiguous falsification conditions; empty if none]
  key_risk: [primary risk to the hypothesis holding under adoption conditions]

READINESS: "Evidence brief for {topic} is complete. Ready for /topic-story."

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write. Emit: "STAGE 5 COMPLETE -- [path] | verdict: [value] | campaign done."
```

---

## V-02 -- Axis: Evidence Gap Accounting

**Variation axis**: evidence_gap_accounting only. Each evidence stage declares 1-2 items
actively sought but not found. Stage 5 opens with an EVIDENCE GAP SUMMARY that counts
all sought_not_found items across the campaign and applies a gap-derived confidence cap
before the verdict is set.

**Hypothesis**: Evidence gaps are as informative as evidence found, but most investigation
formats only report what was discovered. A campaign that sought ten sources and found three
looks the same as one that found three without trying for more. Forcing each stage to
declare sought_not_found at point of collection makes the confidence claim honest: a
SUPPORTED verdict with four documented gaps is a different kind of support than one with
no gaps. It also surfaces the strongest arguments for follow-on work without requiring a
separate recommendations section.

---

```
Topic: {topic}
Date:  {date}

Run the full prove evidence campaign for {topic}.
Five stages in fixed order: hypothesis, websearch, intelligence, analysis, synthesize.
Each stage writes one artifact. No stage begins until the prior stage artifact is written.

## SETUP

Glob: simulations/scout/{topic}-scout-*.md

If no file found:
  Emit: "SCOUT GATE: BLOCKED -- no scout artifact for {topic}. Run /scout first."
  Halt. Stage 1 cannot begin under any condition.
If found:
  scout_source: [path]
  Emit: "SCOUT GATE: CLEARED. scout_source: [path]"

Stage 1 is structurally blocked until SCOUT GATE: CLEARED fires.

---

## STAGE 1 -- HYPOTHESIS

Entry: SCOUT GATE: CLEARED fired.

Read the scout artifact at scout_source. Do not use general knowledge as a substitute.

  scout_source:            [path from SCOUT GATE -- copied, not inferred]
  hypothesis:              [falsifiable claim about {topic}]
  status_quo_comparator:   [incumbent approach this topic must displace]

  scout_extraction_note: [one sentence: which section of the scout artifact most directly
                           grounds this hypothesis]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE -- [path]"

Stage 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH

Entry: STAGE 1 COMPLETE fired.

Gather minimum 3 external sources.

| # | Source (URL or title) | One-line summary | Supports / Opposes / Inconclusive |
|---|----------------------|-----------------|----------------------------------|
| 1 | [source]             | [summary]       | [direction]                      |
| 2 | [source]             | [summary]       | [direction]                      |
| 3 | [source]             | [summary]       | [direction]                      |

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

SOUGHT_NOT_FOUND (Stage 2):
  1. [source type or query that was attempted but yielded no usable result]
  2. [second item -- omit if none]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE -- [path] | gaps logged: [count]"

Stage 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE

Entry: STAGE 2 COMPLETE fired.

Search internal sources. Minimum 2 internal files. Record file-path citation for each.

| # | File path | Key finding (1 sentence) | Supports / Opposes / Inconclusive |
|---|-----------|--------------------------|----------------------------------|
| 1 | [path]    | [finding]               | [direction]                      |
| 2 | [path]    | [finding]               | [direction]                      |

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

SOUGHT_NOT_FOUND (Stage 3):
  1. [internal source type or path pattern sought but not found]
  2. [second item -- omit if none]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE -- [path] | gaps logged: [count]"

Stage 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS

Entry: STAGE 3 COMPLETE fired.

Identify patterns across Stage 2 and Stage 3 evidence. Distinguish correlation from
causation. Record source attribution for each pattern claim.

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

SOUGHT_NOT_FOUND (Stage 4):
  1. [analysis or data pattern sought but no evidence base was available to support it]
  2. [second item -- omit if none]

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE -- [path] | gaps logged: [count]"

Stage 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIZE

Entry: STAGE 4 COMPLETE fired.

### EVIDENCE GAP SUMMARY

Compile all SOUGHT_NOT_FOUND items across Stages 2, 3, and 4.

| Stage | Item | Category [Coverage / Depth / Confirmation] |
|-------|------|--------------------------------------------|
| 2     | [item] | [category]                               |
| 3     | [item] | [category]                               |
| 4     | [item] | [category]                               |

  sought_not_found_total: [N]

GAP-DERIVED CONFIDENCE CAP (applied before verdict):
  0-1 gaps  -> confidence unconstrained
  2-3 gaps  -> confidence cap: PARTIAL (Medium ceiling)
  4+ gaps   -> confidence cap: LOW

  gap_confidence_cap: [Unconstrained / PARTIAL / LOW]

### SYNTHESIS

  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary: [2-3 sentences integrating Stages 2, 3, 4]
  confidence: [High / Medium / Low -- must not exceed gap_confidence_cap ceiling]
  key_risk: [primary risk, informed by the most significant gap category]

READINESS: "Evidence brief for {topic} is complete. Ready for /topic-story."

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write. Emit: "STAGE 5 COMPLETE -- [path] | verdict: [value] | gaps: [N] | campaign done."
```

---

## V-03 -- Axis: Stage Handoff Verification

**Variation axis**: stage_handoff_verification only. Every stage closes with a committed
HANDOFF BLOCK naming: artifact_written (path), claims_forwarded (2-3 sentences), and
verdicts_forwarded (named verdicts the next stage must reference). The following stage's
entry conditions require "HANDOFF from Stage N received" before any work begins. Stage 5
constructs its verdict exclusively from the accumulated HANDOFF BLOCKs.

**Hypothesis**: In multi-stage investigations, stage bodies accrue implicit assumptions
that are never surfaced as explicit commitments. Stage 4 may rest a conclusion on a
claim that Stage 3 only mentioned in passing, not in its core finding. Committed HANDOFF
BLOCKs force each stage to declare what it is handing forward before the next stage
begins. Stage 5 reading exclusively from HANDOFF BLOCKs makes the derivation chain
auditable: every line of the synthesis can be traced to a named prior-stage commitment,
not inferred from a re-reading of stage bodies.

---

```
Topic: {topic}
Date:  {date}

Run the full prove evidence campaign for {topic}.
Five stages in fixed order: hypothesis, websearch, intelligence, analysis, synthesize.
Each stage writes one artifact and commits a HANDOFF BLOCK before the next stage begins.
Stage 5 reads exclusively from HANDOFF BLOCKs -- stage bodies are not re-read.

## SETUP

Glob: simulations/scout/{topic}-scout-*.md

If no file found:
  Emit: "SCOUT GATE: BLOCKED -- no scout artifact for {topic}. Run /scout first."
  Halt. Stage 1 cannot begin under any condition.
If found:
  scout_source: [path]
  Emit: "SCOUT GATE: CLEARED. scout_source: [path]"

Stage 1 is structurally blocked until SCOUT GATE: CLEARED fires.

---

## STAGE 1 -- HYPOTHESIS

Entry: SCOUT GATE: CLEARED fired.

Read the scout artifact at scout_source. Do not use general knowledge as a substitute.

  scout_source:          [path from SCOUT GATE -- copied, not inferred]
  hypothesis:            [falsifiable claim about {topic}]
  status_quo_comparator: [incumbent approach this topic must displace]

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write.

HANDOFF BLOCK -- Stage 1 to Stage 2:
  artifact_written:   simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  claims_forwarded:   [2-3 sentences stating the hypothesis and the displacement claim
                       exactly as Stage 2 should treat them]
  verdicts_forwarded: hypothesis_status = OPEN (no evidence yet)

Emit: "STAGE 1 COMPLETE -- HANDOFF committed."

Stage 2 entry conditions: HANDOFF from Stage 1 received. Stage 2 cannot begin until this fires.

---

## STAGE 2 -- WEBSEARCH

Entry: HANDOFF from Stage 1 received.
  Confirm: claims_forwarded from Stage 1 HANDOFF loaded.
  hypothesis treated as: [repeat claims_forwarded verbatim from Stage 1 HANDOFF]

Gather minimum 3 external sources.

| # | Source (URL or title) | One-line summary | Supports / Opposes / Inconclusive |
|---|----------------------|-----------------|----------------------------------|
| 1 | [source]             | [summary]       | [direction]                      |
| 2 | [source]             | [summary]       | [direction]                      |
| 3 | [source]             | [summary]       | [direction]                      |

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write.

HANDOFF BLOCK -- Stage 2 to Stage 3:
  artifact_written:   simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  claims_forwarded:   [2-3 sentences stating what the web evidence established or failed
                       to establish -- net direction and confidence contribution]
  verdicts_forwarded: s2_direction = [Supports / Opposes / Inconclusive / Mixed]
                      s2_thin_count = [N]

Emit: "STAGE 2 COMPLETE -- HANDOFF committed."

Stage 3 entry conditions: HANDOFF from Stage 2 received. Stage 3 cannot begin until this fires.

---

## STAGE 3 -- INTELLIGENCE

Entry: HANDOFF from Stage 2 received.
  Confirm: claims_forwarded and s2_direction from Stage 2 HANDOFF loaded.

Search internal sources. Minimum 2 internal files. Record file-path citation for each.

| # | File path | Key finding (1 sentence) | Supports / Opposes / Inconclusive |
|---|-----------|--------------------------|----------------------------------|
| 1 | [path]    | [finding]               | [direction]                      |
| 2 | [path]    | [finding]               | [direction]                      |

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write.

HANDOFF BLOCK -- Stage 3 to Stage 4:
  artifact_written:   simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  claims_forwarded:   [2-3 sentences stating what internal evidence added or challenged
                       relative to Stage 2 web findings]
  verdicts_forwarded: s3_direction = [Supports / Opposes / Inconclusive / Mixed]
                      s3_thin_count = [N]
                      cumulative_direction = [net direction across Stage 2 + Stage 3]

Emit: "STAGE 3 COMPLETE -- HANDOFF committed."

Stage 4 entry conditions: HANDOFF from Stage 3 received. Stage 4 cannot begin until this fires.

---

## STAGE 4 -- ANALYSIS

Entry: HANDOFF from Stage 3 received.
  Confirm: cumulative_direction from Stage 3 HANDOFF loaded.

Identify patterns. Distinguish correlation from causation. Attribute each pattern to a
source from Stage 2 or Stage 3 artifact.

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write.

HANDOFF BLOCK -- Stage 4 to Stage 5:
  artifact_written:   simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  claims_forwarded:   [2-3 sentences stating the analysis conclusions and their evidential
                       basis -- what the patterns establish about the hypothesis]
  verdicts_forwarded: s4_pattern_verdict = [Supports / Opposes / Inconclusive / Mixed]
                      total_thin_count = [sum across Stages 1-4]
                      campaign_direction = [net across all four stages]

Emit: "STAGE 4 COMPLETE -- HANDOFF committed."

Stage 5 entry conditions: HANDOFF from Stage 4 received. Stage 5 cannot begin until this fires.

---

## STAGE 5 -- SYNTHESIZE

Entry: HANDOFF from Stage 4 received.

HANDOFF CHAIN REVIEW (read from HANDOFF BLOCKs only -- do not re-read stage bodies):

| Stage | verdicts_forwarded (key fields)                         |
|-------|--------------------------------------------------------|
| 1     | hypothesis_status = OPEN                               |
| 2     | s2_direction = [from HANDOFF] | s2_thin = [N]         |
| 3     | s3_direction = [from HANDOFF] | cumulative = [from HANDOFF] |
| 4     | s4_pattern_verdict = [from HANDOFF] | total_thin = [N] | campaign_direction = [from HANDOFF] |

Synthesis verdict is derived from campaign_direction and total_thin_count from Stage 4 HANDOFF.
No claim in the synthesis may reference evidence not committed in a HANDOFF BLOCK.

  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  derivation: "verdict derived from Stage 4 HANDOFF: campaign_direction = [value],
               total_thin_count = [N]"
  evidence_summary: [2-3 sentences citing HANDOFF fields -- not stage body content]
  confidence: [High / Medium / Low]
  key_risk: [primary residual risk from analysis patterns]

READINESS: "Evidence brief for {topic} is complete. Ready for /topic-story."

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write. Emit: "STAGE 5 COMPLETE -- [path] | verdict: [value] | campaign done."
```

---

## V-04 -- Axes: Falsification Gate + Evidence Gap Accounting

**Variation axes**: falsification_gate + evidence_gap_accounting combined. The hypothesis
commits 2-3 falsification conditions before Stage 2. Evidence stages check trigger status
AND declare sought_not_found items. Stage 4 produces falsification verdicts per condition.
Stage 5 opens with EVIDENCE GAP SUMMARY, applies gap confidence cap, then resolves
falsification conditions before setting the verdict.

**Hypothesis**: Falsification conditions and gap accounting are complementary honesty
mechanisms operating at different time horizons. Falsification conditions commit to what
would change the verdict before evidence arrives; gap accounting accounts for what the
investigation was unable to reach. Together they create a campaign that cannot claim
SUPPORTED without demonstrating that the hypothesis survived conditions it pre-committed
to test AND that the investigator fully surfaced what the evidence base did not contain.

---

```
Topic: {topic}
Date:  {date}

Run the full prove evidence campaign for {topic}.
Five stages in fixed order: hypothesis, websearch, intelligence, analysis, synthesize.
Each stage writes one artifact. No stage begins until the prior stage artifact is written.

## SETUP

Glob: simulations/scout/{topic}-scout-*.md

If no file found:
  Emit: "SCOUT GATE: BLOCKED -- no scout artifact for {topic}. Run /scout first."
  Halt. Stage 1 cannot begin under any condition.
If found:
  scout_source: [path]
  Emit: "SCOUT GATE: CLEARED. scout_source: [path]"

Stage 1 is structurally blocked until SCOUT GATE: CLEARED fires.

---

## STAGE 1 -- HYPOTHESIS

Entry: SCOUT GATE: CLEARED fired.

Read the scout artifact at scout_source. Do not use general knowledge as a substitute.

  scout_source:          [path from SCOUT GATE -- copied, not inferred]
  hypothesis:            [falsifiable claim about {topic}]
  status_quo_comparator: [incumbent approach this topic must displace]

  FALSIFICATION CONDITIONS (locked before Stage 2 begins):
  | ID  | Condition (what evidence would prove the hypothesis false) |
  |-----|----------------------------------------------------------|
  | F-1 | [condition 1]                                            |
  | F-2 | [condition 2]                                            |
  | F-3 | [condition 3 -- optional]                                |

  falsification_conditions_locked: true
  (Cannot be modified after this stage is written.)

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE -- [path]"

Stage 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH

Entry: STAGE 1 COMPLETE fired.

Gather minimum 3 external sources.

| # | Source | Summary (1 sentence) | Supports/Opposes | F-1 | F-2 | F-3 |
|---|--------|---------------------|-----------------|-----|-----|-----|
| 1 | [src]  | [summary]           | [direction]     | [T/NT/A] | [T/NT/A] | [T/NT/A] |
| 2 | [src]  | [summary]           | [direction]     | [T/NT/A] | [T/NT/A] | [T/NT/A] |
| 3 | [src]  | [summary]           | [direction]     | [T/NT/A] | [T/NT/A] | [T/NT/A] |

T = Triggered  NT = Not Triggered  A = Ambiguous

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

SOUGHT_NOT_FOUND (Stage 2):
  1. [source type or query attempted but yielded no usable result]
  2. [second item -- omit if none]

  s2_falsification_tally:
    F-1: [worst status across items]  F-2: [worst status]  F-3: [worst status]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE -- [path] | falsification tally: [summary] | gaps: [N]"

Stage 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE

Entry: STAGE 2 COMPLETE fired.

Search internal sources. Minimum 2 internal files. Record file-path citation for each.

| # | File path | Key finding (1 sentence) | Supports/Opposes | F-1 | F-2 | F-3 |
|---|-----------|--------------------------|-----------------|-----|-----|-----|
| 1 | [path]    | [finding]               | [direction]     | [T/NT/A] | [T/NT/A] | [T/NT/A] |
| 2 | [path]    | [finding]               | [direction]     | [T/NT/A] | [T/NT/A] | [T/NT/A] |

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

SOUGHT_NOT_FOUND (Stage 3):
  1. [internal source type or path pattern sought but not found]
  2. [second item -- omit if none]

  s3_falsification_tally (cumulative worst status across Stage 2 + Stage 3):
    F-1: [worst status]  F-2: [worst status]  F-3: [worst status]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE -- [path] | falsification tally: [summary] | gaps: [N]"

Stage 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS

Entry: STAGE 3 COMPLETE fired.

Identify patterns across Stage 2 and Stage 3 evidence. Distinguish correlation from
causation. Attribute each pattern to a source artifact.

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

SOUGHT_NOT_FOUND (Stage 4):
  1. [analysis or data sought but no evidence base available]
  2. [second item -- omit if none]

FALSIFICATION VERDICT TABLE (final):
| ID  | Condition      | Final status | Evidence basis (1 sentence)           |
|-----|----------------|-------------|---------------------------------------|
| F-1 | [from Stage 1] | [T/NT/A]    | [cite stage artifact]                 |
| F-2 | [from Stage 1] | [T/NT/A]    | [cite stage artifact]                 |
| F-3 | [from Stage 1] | [T/NT/A]    | [cite stage artifact]                 |

  any_condition_triggered: [true / false]
  any_condition_ambiguous: [true / false]

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE -- [path] | triggered: [t/f] | ambiguous: [t/f] | gaps: [N]"

Stage 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIZE

Entry: STAGE 4 COMPLETE fired.

### EVIDENCE GAP SUMMARY

| Stage | Sought-not-found item | Category |
|-------|----------------------|----------|
| 2     | [item]               | [Coverage / Depth / Confirmation] |
| 3     | [item]               | [Coverage / Depth / Confirmation] |
| 4     | [item]               | [Coverage / Depth / Confirmation] |

  sought_not_found_total: [N]
  gap_confidence_cap: [Unconstrained (0-1) / PARTIAL (2-3) / LOW (4+)]

### FALSIFICATION RESOLUTION

| ID  | Final status | Effect on verdict |
|-----|-------------|------------------|
| F-1 | [T/NT/A]   | [Blocks / No effect / Named uncertainty] |
| F-2 | [T/NT/A]   | [Blocks / No effect / Named uncertainty] |
| F-3 | [T/NT/A]   | [Blocks / No effect / Named uncertainty] |

CEILING RULES (applied in order):
  1. If any_condition_triggered = true: verdict cannot exceed PARTIALLY SUPPORTED.
  2. Confidence cannot exceed gap_confidence_cap ceiling.
  3. If any_condition_ambiguous = true: name each as residual uncertainty before verdict.

### VERDICT

  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary: [2-3 sentences integrating Stages 2, 3, 4]
  confidence: [High / Medium / Low -- respecting both ceiling rules]
  residual_uncertainties: [ambiguous conditions; empty if none]
  key_risk: [primary risk to the hypothesis under adoption conditions]

READINESS: "Evidence brief for {topic} is complete. Ready for /topic-story."

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write. Emit: "STAGE 5 COMPLETE -- [path] | verdict: [value] | gaps: [N] | campaign done."
```

---

## V-05 -- Full Integration: All Three Axes + Complete R10 Stack

**Variation axes**: falsification_gate + evidence_gap_accounting + stage_handoff_verification
layered on the complete R10 V-05 baseline (conviction_ladder + counter_claim_chain +
evidence_provenance_tracking).

**Hypothesis**: R10 V-05 achieved high scores on the evidence-chain-integrity criteria
by tracking conviction trajectory, resolving counter-claims at Stage 4, and requiring
complete provenance chains before analysis conclusions. The three R11 axes address
orthogonal structural gaps: pre-committed falsifiability, gap honesty, and custody chain
between stages. Integrating all six axes on a single structural stack tests whether they
compose without contradiction -- specifically whether conviction moves can be driven by
falsification events, whether sought_not_found items can be provenanced, and whether
HANDOFF BLOCKs can carry counter-claim resolution status forward without losing the
chain.

---

```
Topic: {topic}
Date:  {date}

Run the full prove evidence campaign for {topic}.
The campaign displaces {status_quo_comparator} with {topic}.
Five stages in fixed order: hypothesis, websearch, intelligence, analysis, synthesize.
Each stage writes one artifact and commits a HANDOFF BLOCK. Stage 5 reads exclusively
from HANDOFF BLOCKs.

## SETUP

Glob: simulations/scout/{topic}-scout-*.md

If no file found:
  Emit: "SCOUT GATE: BLOCKED -- no scout artifact for {topic}. Run /scout first."
  Halt. Stage 1 cannot begin under any condition.
If found:
  scout_source: [path]
  Emit: "SCOUT GATE: CLEARED. scout_source: [path]"

Stage 1 is structurally blocked until SCOUT GATE: CLEARED fires.

### PRE-STAGE COMMITMENT BLOCK

Register all campaign-level rules before Stage 1 begins. Cannot be modified once Stage 1
starts.

  status_quo_comparator: [incumbent approach or product]

  CONVICTION LADDER (pre-committed):
    Tiers: Speculative -> Plausible -> Likely -> Confident
    Opening level: Speculative
    Move UP (+1 tier): stage yields at least one item supporting hypothesis with no THIN flag.
    Move DOWN (-1 tier): stage yields a THIN flag OR active counter-evidence.
    HOLD: stage yields only inconclusive or mixed evidence.
    Verdict mapping: Confident = SUPPORTED | Likely = PARTIALLY SUPPORTED |
                     Plausible or Speculative = UNSUPPORTED
    conviction_move_rules_locked: true

  FALSIFICATION CONDITIONS (locked before Stage 2):
  | ID  | Condition |
  |-----|-----------|
  | F-1 | [what evidence would disprove the hypothesis] |
  | F-2 | [second condition] |
  | F-3 | [third condition -- optional] |
  falsification_conditions_locked: true

---

## STAGE 1 -- HYPOTHESIS

Entry: SCOUT GATE: CLEARED fired.

Read scout_source. Do not use general knowledge as a substitute.

  scout_source:          [path from SCOUT GATE -- copied, not inferred]
  hypothesis:            [falsifiable claim about {topic}]
  counter_claims:
    CC-1: [incumbent's strongest argument against displacement]
    CC-2: [second counter-claim]
    CC-3: [third counter-claim -- optional]
  conviction_at_entry:   Speculative

Verify falsification_conditions_locked = true before writing artifact.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write.

HANDOFF BLOCK -- Stage 1:
  artifact_written:   [path]
  claims_forwarded:   "Hypothesis: [hypothesis text]. Counter-claims registered: CC-1 through
                       CC-[N]. Falsification conditions F-1 through F-[N] active."
  verdicts_forwarded: hypothesis_status = OPEN | conviction = Speculative |
                      CC-1 = OPEN | CC-2 = OPEN | CC-3 = OPEN

Emit: "STAGE 1 COMPLETE -- HANDOFF committed. conviction = Speculative."

Stage 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH

Entry: HANDOFF from Stage 1 received.
  Load claims_forwarded and verdicts_forwarded from Stage 1 HANDOFF.
  Treat hypothesis, counter-claims, and falsification conditions as inherited from HANDOFF.

Gather minimum 3 external sources. For each source:
  - Record provenance: source | claim_addressed | forward_path (stage where this item
    will be cited in analysis)
  - Check falsification trigger status per condition (T/NT/A)
  - Rate evidence direction (Supports / Opposes / Inconclusive)
  - Note any counter-claim addressed

| # | Source | Claim addressed | Fwd path | F-1 | F-2 | F-3 | Direction | CC addressed |
|---|--------|----------------|----------|-----|-----|-----|-----------|-------------|
| 1 | [src]  | [claim]        | S4       | [T/NT/A] | [T/NT/A] | [T/NT/A] | [dir] | [CC-N or none] |
| 2 | [src]  | [claim]        | S4       | [T/NT/A] | [T/NT/A] | [T/NT/A] | [dir] | [CC-N or none] |
| 3 | [src]  | [claim]        | S4       | [T/NT/A] | [T/NT/A] | [T/NT/A] | [dir] | [CC-N or none] |

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

SOUGHT_NOT_FOUND (Stage 2):
  1. [source type or query attempted but yielded no usable result]
  2. [second item -- omit if none]

CONVICTION MOVE (Stage 2):
  stage_2_direction: [net direction across items]
  stage_2_thin_count: [N]
  stage_2_move: [+1 / -1 / HOLD] -- [trigger event in one phrase]
  conviction_after_stage_2: [tier]

  s2_falsification_tally:
    F-1: [worst status]  F-2: [worst status]  F-3: [worst status]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write.

HANDOFF BLOCK -- Stage 2:
  artifact_written:   [path]
  claims_forwarded:   [2-3 sentences: net direction, conviction move, any CC addressed]
  verdicts_forwarded: s2_direction = [value] | conviction = [tier] |
                      s2_thin_count = [N] | s2_gaps = [N] |
                      F-1 = [status] | F-2 = [status] | F-3 = [status] |
                      CC-1 = [OPEN / ADDRESSED / PARTIAL] |
                      CC-2 = [OPEN / ADDRESSED / PARTIAL] |
                      CC-3 = [OPEN / ADDRESSED / PARTIAL]

Emit: "STAGE 2 COMPLETE -- HANDOFF committed. conviction = [tier]."

Stage 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE

Entry: HANDOFF from Stage 2 received.
  Load verdicts_forwarded from Stage 2 HANDOFF.
  Current conviction level: [from Stage 2 HANDOFF].

Search internal sources. Minimum 2 internal files. Record file-path citation for each.

| # | File path | Claim addressed | Fwd path | F-1 | F-2 | F-3 | Direction | CC addressed |
|---|-----------|----------------|----------|-----|-----|-----|-----------|-------------|
| 1 | [path]    | [claim]        | S4       | [T/NT/A] | [T/NT/A] | [T/NT/A] | [dir] | [CC-N or none] |
| 2 | [path]    | [claim]        | S4       | [T/NT/A] | [T/NT/A] | [T/NT/A] | [dir] | [CC-N or none] |

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

SOUGHT_NOT_FOUND (Stage 3):
  1. [internal source type or path pattern sought but not found]
  2. [second item -- omit if none]

CONVICTION MOVE (Stage 3):
  stage_3_direction: [net direction]
  stage_3_thin_count: [N]
  stage_3_move: [+1 / -1 / HOLD] -- [trigger event]
  conviction_after_stage_3: [tier]

  s3_falsification_tally (cumulative worst across Stage 2 + Stage 3):
    F-1: [worst status]  F-2: [worst status]  F-3: [worst status]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write.

HANDOFF BLOCK -- Stage 3:
  artifact_written:   [path]
  claims_forwarded:   [2-3 sentences: what internal evidence added or challenged]
  verdicts_forwarded: s3_direction = [value] | conviction = [tier] |
                      s3_thin_count = [N] | s3_gaps = [N] |
                      F-1 = [cumulative] | F-2 = [cumulative] | F-3 = [cumulative] |
                      CC-1 = [status] | CC-2 = [status] | CC-3 = [status]

Emit: "STAGE 3 COMPLETE -- HANDOFF committed. conviction = [tier]."

Stage 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS

Entry: HANDOFF from Stage 3 received.
  Load verdicts_forwarded from Stage 3 HANDOFF.
  Current conviction level: [from Stage 3 HANDOFF].

Identify patterns across Stage 2 and Stage 3 evidence. Distinguish correlation from
causation. A conclusion may only be drawn from evidence items with a complete forward_path
chain (forward_path = S4 for items from Stage 2 and Stage 3). Items with no forward_path
are flagged THIN-PROVENANCE and cannot anchor analysis conclusions.

Flag THIN: [area] -- [gap] at point of discovery. Do not defer.

SOUGHT_NOT_FOUND (Stage 4):
  1. [analysis or data pattern sought but no adequate evidence base]
  2. [second item -- omit if none]

COUNTER-CLAIM RESOLUTION TABLE:
| CC   | Counter-claim text     | Verdict                                | Evidence basis (cite artifact) |
|------|----------------------|----------------------------------------|-------------------------------|
| CC-1 | [from Stage 1]       | [REFUTED / PARTIALLY REFUTED / OPEN]   | [stage artifact]              |
| CC-2 | [from Stage 1]       | [REFUTED / PARTIALLY REFUTED / OPEN]   | [stage artifact]              |
| CC-3 | [from Stage 1]       | [REFUTED / PARTIALLY REFUTED / OPEN]   | [stage artifact]              |

FALSIFICATION VERDICT TABLE:
| ID  | Condition      | Final status | Evidence basis (cite artifact) |
|-----|----------------|-------------|-------------------------------|
| F-1 | [from Stage 1] | [T/NT/A]    | [stage artifact]              |
| F-2 | [from Stage 1] | [T/NT/A]    | [stage artifact]              |
| F-3 | [from Stage 1] | [T/NT/A]    | [stage artifact]              |

  any_CC_open: [true / false]
  any_condition_triggered: [true / false]
  any_condition_ambiguous: [true / false]

CONVICTION MOVE (Stage 4):
  stage_4_move: [+1 / -1 / HOLD] -- [trigger: CC resolution or falsification event]
  conviction_after_stage_4: [tier]

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write.

HANDOFF BLOCK -- Stage 4:
  artifact_written:   [path]
  claims_forwarded:   [2-3 sentences: analysis conclusions, CC resolution summary,
                       falsification status, conviction trajectory]
  verdicts_forwarded: final_conviction = [tier] |
                      any_CC_open = [t/f] | any_triggered = [t/f] | any_ambiguous = [t/f] |
                      total_thin_count = [sum across Stages 1-4] |
                      total_gaps = [sum of SOUGHT_NOT_FOUND across Stages 2-4] |
                      CC-1 = [final] | CC-2 = [final] | CC-3 = [final] |
                      F-1 = [final] | F-2 = [final] | F-3 = [final]

Emit: "STAGE 4 COMPLETE -- HANDOFF committed. conviction = [tier]."

Stage 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIZE

Entry: HANDOFF from Stage 4 received.
Stage 5 reads exclusively from HANDOFF BLOCKs. Stage bodies are not re-read.

### CONVICTION TRAJECTORY (from HANDOFF chain)

| Stage | Move      | Trigger event                      | Conviction after |
|-------|-----------|------------------------------------|-----------------|
| 1     | --        | Campaign open                      | Speculative      |
| 2     | [from H2] | [from H2 claims_forwarded]        | [from H2]        |
| 3     | [from H3] | [from H3 claims_forwarded]        | [from H3]        |
| 4     | [from H4] | [from H4 claims_forwarded]        | [from H4]        |

  final_conviction: [from Stage 4 HANDOFF]
  conviction_derived_verdict: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]

### EVIDENCE GAP SUMMARY (from HANDOFF chain)

  total_gaps: [from Stage 4 HANDOFF total_gaps]
  gap_confidence_cap: [Unconstrained (0-1) / PARTIAL (2-3) / LOW (4+)]

### COUNTER-CLAIM RESOLUTION (from Stage 4 HANDOFF)

| CC   | Final verdict | Open risk? |
|------|--------------|-----------|
| CC-1 | [from H4]   | [Y/N]     |
| CC-2 | [from H4]   | [Y/N]     |
| CC-3 | [from H4]   | [Y/N]     |

### FALSIFICATION RESOLUTION (from Stage 4 HANDOFF)

| ID  | Final status | Effect on verdict |
|-----|-------------|------------------|
| F-1 | [from H4]  | [Blocks / No effect / Named uncertainty] |
| F-2 | [from H4]  | [Blocks / No effect / Named uncertainty] |
| F-3 | [from H4]  | [Blocks / No effect / Named uncertainty] |

### CEILING RULES (applied in order)

  1. Falsification: if any_triggered = true, verdict cannot exceed PARTIALLY SUPPORTED.
  2. Confidence cap: must not exceed gap_confidence_cap.
  3. Open counter-claims: list each as a named residual risk before verdict.
  4. Conviction ceiling: verdict cannot exceed conviction_derived_verdict.

The binding verdict is the most conservative ceiling that fires.

### VERDICT

  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  derivation: "verdict from: conviction = [tier], gaps = [N], triggered = [t/f],
               open_CCs = [list or none]"
  evidence_summary: [2-3 sentences derived from Stage 4 HANDOFF claims_forwarded]
  confidence: [High / Medium / Low -- respecting all ceiling rules]
  residual_uncertainties: [ambiguous falsification conditions + open counter-claims]
  key_risk: [primary residual risk framed as strongest remaining incumbent argument]

READINESS: "Evidence brief for {topic} is complete. Ready for /topic-story."

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write. Emit: "STAGE 5 COMPLETE -- [path] | verdict: [value] | conviction: [tier] | campaign done."
```
