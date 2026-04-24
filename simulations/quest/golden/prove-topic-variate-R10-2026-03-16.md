---
skill: quest-variate
skill_target: prove-topic
round: R10
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [conviction_ladder, counter_claim_chain, evidence_provenance_tracking]
  combined: [V-04 (conviction_ladder+counter_claim_chain), V-05 (counter_claim_chain+evidence_provenance_tracking+conviction_ladder)]
r9_context: >
  R9 explored three single axes: claim_decomposition, scout_extraction_protocol,
  phased_read_back_blocking. V-04 combined claim_decomposition with evidence_strength_tiering.
  V-05 combined scout_extraction_protocol + phased_read_back_blocking + backward_citation_chain.
  R10 explores three axes not yet tried as singles under v14:
  (1) conviction_ladder -- the hypothesis opens at a declared conviction level (Speculative).
  Each stage has explicit move rules: evidence that supports the hypothesis raises conviction
  one tier; a THIN flag or active counter-evidence lowers it one tier; a net-zero stage holds.
  Stage 4 produces the conviction trajectory. Synthesis derives the verdict label directly from
  the final conviction level. Distinct from confidence_gate (R8): conviction_gate emits a
  per-stage rating with rationale; conviction_ladder commits to move rules upfront and produces
  a continuous trajectory with explicit trigger events at each stage.
  (2) counter_claim_chain -- Stage 1 defines 2-3 explicit counter-claims (the incumbent's best
  defenses against displacement). Evidence stages must address each counter-claim directly.
  Stage 4 resolves each counter-claim (Refuted / Partially Refuted / Open Risk). Synthesis
  must list every unresolved counter-claim as a named risk before the verdict. Distinct from
  claim_decomposition (R9): claim_decomposition decomposes the positive hypothesis; counter_claim_chain
  defines the strongest arguments against it and requires each to be resolved.
  (3) evidence_provenance_tracking -- Every evidence item carries a three-field provenance record:
  (source, claim_it_addresses, forward_path: stage_where_used). Stage 4 can only build
  conclusions from evidence with a complete forward_path. Evidence with an incomplete chain is
  flagged THIN-PROVENANCE. Synthesis reports provenance completeness (N/M items with complete
  chains) as a confidence signal. Distinct from backward_citation_chain (R6): backward citation
  traces synthesis claims back to artifacts; provenance tracking requires each evidence item to
  declare its forward path at collection time, preventing orphaned evidence.
  V-04 combines conviction_ladder (V-01) with counter_claim_chain (V-02): the conviction moves
  when counter-claims are resolved; a Refuted counter-claim raises conviction one tier; an Open
  Risk lowers it one tier. Synthesis reports the conviction trajectory with the counter-claim
  resolution events that triggered each move.
  V-05 combines all three axes: counter_claim_chain + evidence_provenance_tracking + conviction_ladder.
  Stage 1 declares counter-claims and opens at Speculative with provenance headers. Evidence
  stages advance provenance chains and trigger conviction moves via counter-claim resolution events.
  Stage 4 produces a joint verdict matrix (counter-claim resolution x conviction trajectory).
  Synthesis cites evidence by provenance chain, names the final conviction level, and lists
  unresolved counter-claims as named residual risks.
  All R10 variations carry: (1) explicit scout-blocking before Stage 1, (2) per-stage artifact
  writes with full paths, (3) scout_source in hypothesis frontmatter, (4) THIN: flagging at point
  of discovery, (5) exact readiness statement closing synthesis.
---

# prove-topic -- Variate Round 10 (Rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-10 aspirational)
**Date**: 2026-03-16
**Round**: 10

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

## V-01 -- Axis: Conviction Ladder

**Variation axis**: Conviction ladder only -- the hypothesis opens at a declared conviction
level of Speculative. Before Stage 1 begins, move rules are registered: finding supporting
evidence raises conviction one tier; a THIN flag or active counter-evidence lowers it one
tier; a stage that yields neither holds. The four tiers are Speculative, Plausible, Likely,
Confident. Stage 4 produces the full conviction trajectory (starting level, each stage move,
and trigger event). Synthesis derives the verdict label directly from the final conviction
level: Confident = SUPPORTED, Likely = PARTIALLY SUPPORTED, Plausible or Speculative =
UNSUPPORTED.

**Hypothesis**: A single confidence rating at synthesis gives no account of how the
investigation moved from prior to posterior. Conviction ladder makes the journey auditable:
a SUPPORTED verdict that passed through Speculative -> Plausible -> Likely -> Confident is
qualitatively different from one that jumped from Plausible -> Confident on a single strong
source. The move rules registered upfront prevent post-hoc rationalization: the investigator
cannot adjust the rules once evidence starts arriving. The trajectory also reveals which
stage carried the most evidential weight, which has implications for where to invest in
additional evidence.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic}. The hypothesis opens at Speculative.
Move rules are pre-committed. Conviction trajectory is tracked stage by stage.
Final verdict derives from the ending conviction level.

## SETUP

Locate the scout artifact: glob `simulations/scout/{topic}-scout-*.md`

SCOUT GATE cannot clear without a found file.
If absent: emit "SCOUT GATE: BLOCKED. No scout artifact for {topic}. Run /scout first."
Halt immediately. Stage 1 cannot begin under any condition.
If found:
  scout_source: [path]
  Emit: "SCOUT GATE: CLEARED. scout_source: [path]"

Stage 1 is structurally blocked until SCOUT GATE: CLEARED fires.

### CONVICTION MOVE RULES (pre-committed, locked before Stage 1)

Register now. Cannot be modified after Stage 1 begins.

  MOVE UP (+1 tier):   At least one item from this stage supports the hypothesis with
                       no THIN flag attached.
  MOVE DOWN (-1 tier): This stage yields a THIN flag OR active counter-evidence on the
                       hypothesis claim.
  HOLD (no move):      Stage yields only inconclusive or mixed evidence with no net
                       direction.

  Tier scale (locked): Speculative -> Plausible -> Likely -> Confident
  Opening level:       Speculative

  conviction_move_rules_locked: true

---

## STAGE 1 -- HYPOTHESIS

Entry: SCOUT GATE: CLEARED fired.

Read the scout artifact. Frame a falsifiable hypothesis grounded in scout content.
Record a falsification condition (what evidence would prove the hypothesis false).

Frontmatter must include:
  scout_source: [path from SCOUT GATE]
  conviction_level_at_entry: Speculative

  hypothesis: [falsifiable claim about {topic}]
  falsification_condition: [what evidence would disprove this]

Conviction move for Stage 1:
  stage_1_evidence_direction: [Supports / Opposes / Inconclusive]
  stage_1_thin_flags: [count]
  stage_1_move: [+1 / -1 / HOLD] -- [trigger event in one phrase]
  conviction_level_after_stage_1: [tier]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path] | conviction: [tier]"

Stage 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH

Entry: STAGE 1 COMPLETE fired.

Gather external evidence. Minimum 3 sources.

For each source:
  | Source | One-line summary | Supports / Opposes / Inconclusive |
  |--------|-----------------|-----------------------------------|

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

Conviction move for Stage 2:
  stage_2_evidence_direction: [net direction across all sources]
  stage_2_thin_flags: [count]
  stage_2_move: [+1 / -1 / HOLD] -- [trigger event in one phrase]
  conviction_level_after_stage_2: [tier]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path] | conviction: [tier]"

Stage 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE

Entry: STAGE 2 COMPLETE fired.

Search internal sources (simulations/, specs, artifacts). Minimum 2 internal sources.

For each finding:
  | File Path | One-line summary | Supports / Opposes / Inconclusive |
  |-----------|-----------------|-----------------------------------|

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

Conviction move for Stage 3:
  stage_3_evidence_direction: [net direction]
  stage_3_thin_flags: [count]
  stage_3_move: [+1 / -1 / HOLD] -- [trigger event in one phrase]
  conviction_level_after_stage_3: [tier]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path] | conviction: [tier]"

Stage 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS

Entry: STAGE 3 COMPLETE fired.

Produce the conviction trajectory table:

  | Stage   | Entry Level  | Evidence Direction | THIN flags | Move  | Exit Level  | Trigger Event |
  |---------|--------------|--------------------|------------|-------|-------------|---------------|
  | Stage 1 | Speculative  | [direction]        | [N]        | [+1/-1/HOLD] | [tier] | [phrase] |
  | Stage 2 | [from S1]    | [direction]        | [N]        | ...   | [tier]      | [phrase] |
  | Stage 3 | [from S2]    | [direction]        | [N]        | ...   | [tier]      | [phrase] |

  conviction_final: [tier]
  conviction_delta: [signed integer from Speculative baseline]

Aggregate THIN flags. Map each to the claim it weakens.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path] | conviction_final: [tier]"

Stage 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS

Entry: STAGE 4 COMPLETE fired.

Derive the verdict from conviction_final:
  Confident          -> SUPPORTED
  Likely             -> PARTIALLY SUPPORTED
  Plausible or lower -> UNSUPPORTED

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Report the conviction trajectory in one sentence:
  The verdict is [label] because the investigation moved [opening_level] -> [final_level]
  driven by [primary_trigger_event] in Stage [N].

For each THIN flag: name the source stage, weakened claim, and conviction-adjusted
confidence for that claim.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

---

## V-02 -- Axis: Counter-Claim Chain

**Variation axis**: Counter-claim chain only -- Stage 1 defines 2-3 explicit counter-claims
alongside the hypothesis. Counter-claims represent the incumbent's strongest defenses against
displacement. Evidence stages must address each counter-claim directly. Stage 4 resolves
each counter-claim: Refuted (strong evidence negates it), Partially Refuted (mixed evidence
weakens but does not eliminate it), or Open Risk (insufficient evidence to resolve it). The
synthesis verdict must name every Open Risk counter-claim before stating the overall label.

**Hypothesis**: A hypothesis alone frames what the investigator wants to be true. Counter-claims
force the investigator to explicitly articulate what the incumbent's defenders would say, and
then require evidence addressing those specific defenses rather than only accumulating
confirmatory evidence. The resolution table in Stage 4 makes the weakness of the evidence
base explicit: an UNSUPPORTED hypothesis may result from strong counter-claims rather than
weak supporting evidence, and the counter-claim chain makes that distinction clear. Open Risk
counter-claims are the natural output for topic-story: they represent residual uncertainty
that downstream work must address.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic}. Stage 1 defines explicit counter-claims.
Evidence stages address each counter-claim. Stage 4 resolves them. Synthesis names all
Open Risk counter-claims before issuing the verdict.

## SETUP

Locate the scout artifact: glob `simulations/scout/{topic}-scout-*.md`

SCOUT GATE cannot clear without a found file.
If absent: emit "SCOUT GATE: BLOCKED. No scout artifact for {topic}. Run /scout first."
Halt immediately. Stage 1 cannot begin under any condition.
If found:
  scout_source: [path]
  Emit: "SCOUT GATE: CLEARED. scout_source: [path]"

Stage 1 is structurally blocked until SCOUT GATE: CLEARED fires.

---

## STAGE 1 -- HYPOTHESIS + COUNTER-CLAIMS

Entry: SCOUT GATE: CLEARED fired.

Read the scout artifact. Frame the hypothesis, then define 2-3 counter-claims that
represent the incumbent's strongest arguments against the hypothesis.

Each counter-claim must be:
- Specific (names a concrete mechanism or failure mode)
- Independently addressable (evidence for CC-A does not automatically address CC-B)
- Grounded in scout content (cite which scout finding motivates this counter-claim)

  hypothesis: [falsifiable claim about {topic}]
  counter_claim_A: [incumbent defense #1] -- grounded in: [scout passage]
  counter_claim_B: [incumbent defense #2] -- grounded in: [scout passage]
  counter_claim_C: [incumbent defense #3, if applicable -- otherwise omit]

Frontmatter must include:
  scout_source: [path from SCOUT GATE]
  counter_claims: [A, B, C]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path]"

Stage 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH (addressing counter-claims)

Entry: STAGE 1 COMPLETE fired.

Gather external evidence. For each source, record which counter-claim it addresses
(or note "hypothesis support" if it supports the main claim without addressing a CC):

  | Source | One-line summary | Addresses | Direction |
  |--------|-----------------|-----------|-----------|
  | [url]  | [summary]       | CC-A / CC-B / hypothesis | Supports / Refutes / Inconclusive |

Note THIN: [counter_claim or hypothesis] -- [area] -- [gap] at point of discovery. Do not defer.

Stage 2 counter-claim tally (running):
  CC-A: [N sources addressing, direction]
  CC-B: [N sources addressing, direction]
  CC-C (if any): [N sources addressing, direction]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path]"

Stage 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE (addressing counter-claims)

Entry: STAGE 2 COMPLETE fired.

Search internal sources (simulations/, specs, artifacts). Record which counter-claim
each finding addresses:

  | File Path | One-line summary | Addresses | Direction |
  |-----------|-----------------|-----------|-----------|
  | [path]    | [summary]       | CC-A / CC-B / hypothesis | Supports / Refutes / Inconclusive |

Note THIN: [counter_claim or hypothesis] -- [area] -- [gap] at point of discovery. Do not defer.

Stage 3 counter-claim tally (running):
  CC-A: [cumulative across Stages 2+3, direction]
  CC-B: [cumulative across Stages 2+3, direction]
  CC-C (if any): [cumulative across Stages 2+3, direction]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path]"

Stage 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS (counter-claim resolution table)

Entry: STAGE 3 COMPLETE fired.

Resolve each counter-claim using combined Stage 2 + Stage 3 evidence:

  | Counter-Claim | Evidence for refutation | Evidence supporting CC | THIN flags | Resolution |
  |---------------|------------------------|----------------------|------------|------------|
  | CC-A          | [N items, summary]     | [N items, summary]   | [N]        | Refuted / Partially Refuted / Open Risk |
  | CC-B          | ...                    | ...                  | ...        | ...        |
  | CC-C (if any) | ...                    | ...                  | ...        | ...        |

  open_risk_count: [N counter-claims unresolved]

Aggregate THIN flags. Map each to the hypothesis claim or counter-claim it weakens.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path] | open_risks: [N]"

Stage 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS (verdict with counter-claim resolution)

Entry: STAGE 4 COMPLETE fired.

Before stating the verdict, list every Open Risk counter-claim:

  OPEN RISKS (unresolved counter-claims -- must name each before verdict):
  [CC-X]: [one sentence describing the residual risk]
  [... one entry per Open Risk CC]

  If no Open Risks: "All counter-claims resolved."

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Derive the verdict using this rule:
  - All CCs Refuted: verdict leans SUPPORTED
  - One CC Partially Refuted, rest Refuted: PARTIALLY SUPPORTED
  - Any CC Open Risk: verdict is capped at PARTIALLY SUPPORTED
  - Majority of CCs Open Risk: UNSUPPORTED

State the verdict rationale in one sentence citing the binding counter-claim resolution status.

For each THIN flag: name the source stage, weakened claim, and adjusted confidence.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

---

## V-03 -- Axis: Evidence Provenance Tracking

**Variation axis**: Evidence provenance tracking only -- every evidence item collected in
Stages 2 and 3 carries a three-field provenance record at the time of collection:
(source, claim_it_addresses, forward_path: which stage will use it). Stage 4 can only
derive conclusions from evidence with a complete forward_path. An item collected but
never assigned a forward_path is flagged THIN-PROVENANCE (unused evidence = hidden gap).
Synthesis reports provenance completeness as a confidence signal: N/M items with complete
chains. A low completeness ratio flags a fragmented evidence base.

**Hypothesis**: Standard evidence gathering collects sources and checks if they are
relevant. Provenance tracking requires each item to declare its intended use at the
time of collection, not at the time of use. This prevents two common failures:
(1) orphaned evidence -- items collected but never connected to a specific claim in
analysis, inflating the apparent evidence base; (2) claim-without-support -- analysis
assertions that cannot be traced to a specific collected item. Reporting completeness
as a confidence signal gives the downstream consumer (topic-story) a data-quality
indicator alongside the verdict.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic}. Every evidence item carries a
provenance record at collection. Stage 4 derives conclusions only from items with
complete provenance. Synthesis reports provenance completeness as a confidence signal.

## SETUP

Locate the scout artifact: glob `simulations/scout/{topic}-scout-*.md`

SCOUT GATE cannot clear without a found file.
If absent: emit "SCOUT GATE: BLOCKED. No scout artifact for {topic}. Run /scout first."
Halt immediately. Stage 1 cannot begin under any condition.
If found:
  scout_source: [path]
  Emit: "SCOUT GATE: CLEARED. scout_source: [path]"

Stage 1 is structurally blocked until SCOUT GATE: CLEARED fires.

### PROVENANCE RECORD FORMAT (pre-committed, locked before Stage 1)

Every evidence item must carry exactly these three fields at collection time:
  source:           [URL or file path]
  claim_addressed:  [which hypothesis claim or sub-question this item speaks to]
  forward_path:     [Stage 4 conclusion this item will feed -- e.g., "Stage 4: displacement verdict"]

An item without all three fields is flagged THIN-PROVENANCE at time of collection.

---

## STAGE 1 -- HYPOTHESIS

Entry: SCOUT GATE: CLEARED fired.

Read the scout artifact. Frame a falsifiable hypothesis and name the key claims that
evidence must address (these become valid claim_addressed values for Stages 2 and 3).

  hypothesis: [falsifiable claim]
  addressable_claims:
    - [claim-1: e.g., "displacement feasibility"]
    - [claim-2: e.g., "adoption readiness"]
    - [claim-3: e.g., "incumbent vulnerability", if applicable]

Frontmatter must include:
  scout_source: [path from SCOUT GATE]
  addressable_claims: [list]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path]"

Stage 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH (with provenance)

Entry: STAGE 1 COMPLETE fired.

Gather external evidence. For each item, complete the full provenance record:

  | # | source | claim_addressed | forward_path | Summary | THIN-PROVENANCE? |
  |---|--------|-----------------|--------------|---------|-----------------|
  | 1 | [url]  | [from addressable_claims] | [Stage 4 conclusion it feeds] | [1 sentence] | yes/no |
  | 2 | ...    | ...             | ...          | ...     | ...             |

Items with an incomplete provenance record (missing any field): flag as THIN-PROVENANCE: [item #] -- [which field missing].

Note standard THIN: [area] -- [gap] for content gaps. Do not defer either type of flag.

Stage 2 provenance summary:
  total_items: [N]
  complete_provenance: [N]
  thin_provenance: [N]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path] | provenance: [complete]/[total]"

Stage 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE (with provenance)

Entry: STAGE 2 COMPLETE fired.

Search internal sources (simulations/, specs, artifacts). Apply same provenance format:

  | # | source | claim_addressed | forward_path | Summary | THIN-PROVENANCE? |
  |---|--------|-----------------|--------------|---------|-----------------|
  | 1 | [path] | [from addressable_claims] | [Stage 4 conclusion it feeds] | [1 sentence] | yes/no |
  | 2 | ...    | ...             | ...          | ...     | ...             |

Flag THIN-PROVENANCE for any item with an incomplete record. Do not defer.
Note standard THIN: [area] -- [gap] for content gaps.

Stage 3 provenance summary:
  total_items: [N]
  complete_provenance: [N]
  thin_provenance: [N]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path] | provenance: [complete]/[total]"

Stage 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS (provenance-gated conclusions)

Entry: STAGE 3 COMPLETE fired.

Derive conclusions only from evidence items with forward_path complete.

Provenance completeness table (combined Stages 2 + 3):
  total_items: [N]
  complete_provenance: [N] (M%)
  thin_provenance: [N]

For each addressable_claim, list only items with forward_path pointing to that claim:

  | Claim | Items with complete provenance | Net direction | Confidence |
  |-------|-------------------------------|---------------|------------|
  | claim-1 | [N items] | Supported / Opposed / Inconclusive | High / Medium / Low |
  | claim-2 | ...       | ...                                | ...                |

Aggregate standard THIN flags. Displacement verdict: Yes / No / Pending. Explain in 1-2 sentences.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path] | provenance_completeness: [N]%"

Stage 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS (with provenance confidence signal)

Entry: STAGE 4 COMPLETE fired.

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Provenance confidence signal (report before evidence summary):
  provenance_completeness: [N]% ([complete]/[total] items)
  provenance_quality: [Strong (>80%) / Moderate (50-80%) / Fragmented (<50%)]
  provenance_note: [one sentence on what incomplete provenance means for confidence]

Evidence summary: 2-3 sentences integrating the verdict across addressable_claims,
citing only items with complete provenance.

For each THIN-PROVENANCE flag: name the item, missing field, and what claim that item
was intended to address.
For each standard THIN flag: name source stage, weakened claim, adjusted confidence.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

---

## V-04 -- Combined: Conviction Ladder + Counter-Claim Chain

**Variation axes**: Conviction ladder (V-01 single axis this round) combined with counter-claim
chain (V-02 single axis this round). The conviction level moves when counter-claims are resolved:
Refuting a counter-claim raises conviction one tier; an Open Risk counter-claim lowers it one tier;
a Partially Refuted counter-claim holds. Synthesis reports the conviction trajectory with the
counter-claim resolution events that triggered each move, making the displacement verdict
mechanically derived from the chain of counter-claim outcomes.

**Hypothesis**: Conviction ladder (V-01) produces a trajectory but its move triggers (supporting
evidence, THIN flag) are symmetric -- any good source moves the needle up regardless of what the
source says about. Counter-claim chain (V-02) directs evidence gathering toward the specific
arguments the investigator most needs to address. Combined, the move triggers become interpretively
richer: conviction rises when a specific incumbent defense is refuted, not when any positive
evidence appears. This makes the trajectory interpretable: "rose from Plausible to Likely at Stage
3 when counter-claim B (adoption barrier) was refuted by two internal case studies" is a more
informative summary than "conviction rose because Stage 3 had net positive evidence."

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic}. Stage 1 registers counter-claims and opens
the conviction ladder at Speculative. Conviction moves when counter-claims are resolved.
Synthesis derives the verdict from the final conviction level and names all Open Risks.

## SETUP

Locate the scout artifact: glob `simulations/scout/{topic}-scout-*.md`

SCOUT GATE cannot clear without a found file.
If absent: emit "SCOUT GATE: BLOCKED. No scout artifact for {topic}. Run /scout first."
Halt immediately. Stage 1 cannot begin under any condition.
If found:
  scout_source: [path]
  Emit: "SCOUT GATE: CLEARED. scout_source: [path]"

Stage 1 is structurally blocked until SCOUT GATE: CLEARED fires.

### CONVICTION-COUNTER-CLAIM MOVE RULES (pre-committed, locked before Stage 1)

  Counter-claim Refuted:          +1 tier
  Counter-claim Partially Refuted: HOLD
  Counter-claim Open Risk:        -1 tier
  Tier scale (locked): Speculative -> Plausible -> Likely -> Confident
  Opening level: Speculative
  Additional trigger: THIN flag on a counter-claim (missing evidence to refute it): HOLD
  Additional trigger: THIN flag on main hypothesis support: -1 tier

  conviction_move_rules_locked: true

---

## STAGE 1 -- HYPOTHESIS + COUNTER-CLAIMS

Entry: SCOUT GATE: CLEARED fired.

Read the scout artifact. Frame the hypothesis and define 2-3 counter-claims (incumbent defenses).

  hypothesis: [falsifiable claim about {topic}]
  counter_claim_A: [incumbent defense #1]
  counter_claim_B: [incumbent defense #2]
  counter_claim_C: [incumbent defense #3, if applicable]
  conviction_level_at_entry: Speculative

Frontmatter must include:
  scout_source: [path from SCOUT GATE]
  counter_claims: [A, B, C]
  conviction_opening: Speculative

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path] | conviction: Speculative"

Stage 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH (per counter-claim, conviction tracked)

Entry: STAGE 1 COMPLETE fired.

Gather external evidence addressing counter-claims and hypothesis support:

  | Source | Summary | Addresses | Direction |
  |--------|---------|-----------|-----------|
  | [url]  | [1 sentence] | CC-A/CC-B/CC-C/hypothesis | Refutes CC / Supports CC / Supports hypothesis |

Note THIN: [CC or hypothesis] -- [area] -- [gap] at point of discovery. Do not defer.

Stage 2 conviction assessment:
  cc_A_direction_this_stage: [strongly toward Refuted / toward Open Risk / inconclusive]
  cc_B_direction_this_stage: [...]
  net_move_trigger: [which CC direction is dominant this stage]
  stage_2_move: [+1 / -1 / HOLD] -- [one-phrase trigger]
  conviction_after_stage_2: [tier]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path] | conviction: [tier]"

Stage 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE (per counter-claim, conviction tracked)

Entry: STAGE 2 COMPLETE fired.

Search internal sources. Record per-counter-claim direction:

  | File Path | Summary | Addresses | Direction |
  |-----------|---------|-----------|-----------|
  | [path]    | [1 sentence] | CC-A/CC-B/CC-C/hypothesis | Refutes CC / Supports CC / Supports hypothesis |

Note THIN: [CC or hypothesis] -- [area] -- [gap] at point of discovery. Do not defer.

Stage 3 conviction assessment:
  cc_A_direction_this_stage: [...]
  cc_B_direction_this_stage: [...]
  net_move_trigger: [which CC direction is dominant this stage]
  stage_3_move: [+1 / -1 / HOLD] -- [one-phrase trigger]
  conviction_after_stage_3: [tier]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path] | conviction: [tier]"

Stage 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS (counter-claim resolution + conviction trajectory)

Entry: STAGE 3 COMPLETE fired.

Counter-claim resolution table (combined Stages 2 + 3):

  | Counter-Claim | Refuting evidence | Supporting evidence | THIN flags | Resolution |
  |---------------|-------------------|---------------------|------------|------------|
  | CC-A          | [N items]         | [N items]           | [N]        | Refuted / Partially Refuted / Open Risk |
  | CC-B          | ...               | ...                 | ...        | ...        |
  | CC-C (if any) | ...               | ...                 | ...        | ...        |

Conviction trajectory table:

  | Stage   | Entry Level | Trigger Event (CC resolution) | Move     | Exit Level |
  |---------|-------------|-------------------------------|----------|------------|
  | Stage 1 | Speculative | [opening -- no move]          | HOLD     | Speculative |
  | Stage 2 | Speculative | [CC resolution trend]         | [+1/-1/HOLD] | [tier] |
  | Stage 3 | [from S2]   | [CC resolution trend]         | [+1/-1/HOLD] | [tier] |
  | Stage 4 | [from S3]   | [final CC resolution]         | [+1/-1/HOLD] | [tier] |

  conviction_final: [tier]
  open_risk_count: [N CCs unresolved]

Aggregate THIN flags. Map each to the CC or claim it weakens.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path] | conviction_final: [tier] | open_risks: [N]"

Stage 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS (verdict from conviction + counter-claim resolution)

Entry: STAGE 4 COMPLETE fired.

Before verdict, list every Open Risk counter-claim:

  OPEN RISKS:
  [CC-X]: [one sentence: residual risk for topic-story]
  (If none: "All counter-claims resolved.")

Derive verdict from conviction_final:
  Confident  -> SUPPORTED
  Likely     -> PARTIALLY SUPPORTED
  Plausible or lower -> UNSUPPORTED

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Report the trajectory in two sentences:
  Sentence 1: conviction moved [opening] -> [final] driven by [primary CC resolution event].
  Sentence 2: [binding counter-claim] [resolution] was the [decisive / limiting] factor.

For each THIN flag: name source stage, weakened CC or claim, adjusted confidence.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

---

## V-05 -- Combined: Counter-Claim Chain + Evidence Provenance Tracking + Conviction Ladder

**Variation axes**: All three R10 axes combined. Stage 1 declares counter-claims, opens the
conviction ladder at Speculative, and registers provenance headers. Evidence stages collect
items with provenance records and assess counter-claim resolution direction to trigger conviction
moves. Stage 4 produces a joint matrix (counter-claim resolution x conviction trajectory) and
a provenance completeness table. Synthesis cites the evidence chain by provenance, names the
final conviction level, and lists unresolved counter-claims as named residual risks.

**Hypothesis**: Each of the three R10 axes addresses a distinct failure mode:
(1) counter_claim_chain ensures evidence addresses the actual opposing arguments, not just
confirmatory sources; (2) evidence_provenance_tracking ensures each item is connected to a
specific conclusion at collection time, preventing orphaned evidence; (3) conviction_ladder
makes the verdict mechanically derivable from the evidence chain, preventing post-hoc verdict
assignment. None competes with another: they operate at different points in the campaign.
Together they close three independent failure modes: wrong-target evidence, orphaned evidence,
and verdict drift. A campaign that passes all three is strong at evidence direction, evidence
quality, and verdict derivability.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic}. Stage 1 declares counter-claims, opens
conviction at Speculative, and registers provenance headers. Evidence stages collect items
with provenance records and assess counter-claim resolution. Stage 4 produces a joint matrix.
Synthesis derives the verdict from conviction_final and names all Open Risks.

## SETUP

Locate the scout artifact: glob `simulations/scout/{topic}-scout-*.md`

SCOUT GATE cannot clear without a found file.
If absent: emit "SCOUT GATE: BLOCKED. No scout artifact for {topic}. Run /scout first."
Halt immediately. Stage 1 cannot begin under any condition.
If found:
  scout_source: [path]
  Emit: "SCOUT GATE: CLEARED. scout_source: [path]"

Stage 1 is structurally blocked until SCOUT GATE: CLEARED fires.

### CAMPAIGN INVARIANTS (pre-committed before Stage 1, cannot be modified)

CONVICTION MOVE RULES:
  Counter-claim Refuted:           +1 tier
  Counter-claim Partially Refuted: HOLD
  Counter-claim Open Risk:         -1 tier
  Hypothesis THIN flag:            -1 tier
  Tier scale: Speculative -> Plausible -> Likely -> Confident
  Opening level: Speculative

PROVENANCE RECORD FORMAT (three required fields per evidence item):
  source:          [URL or file path]
  claim_addressed: [hypothesis claim or counter-claim this item speaks to]
  forward_path:    [Stage 4 conclusion this item will feed]
  Items missing any field: THIN-PROVENANCE flag at collection time.

  campaign_invariants_locked: true

---

## STAGE 1 -- HYPOTHESIS + COUNTER-CLAIMS + CONVICTION OPEN

Entry: SCOUT GATE: CLEARED fired.

Read the scout artifact. Frame the hypothesis, define 2-3 counter-claims, and open
the conviction ladder.

  hypothesis: [falsifiable claim about {topic}]
  counter_claim_A: [incumbent defense #1] -- grounded in: [scout passage]
  counter_claim_B: [incumbent defense #2] -- grounded in: [scout passage]
  counter_claim_C: [incumbent defense #3, if applicable]
  conviction_opening: Speculative

  addressable_claims_for_provenance:
    - [e.g., "hypothesis-main"]
    - [e.g., "CC-A: [label]"]
    - [e.g., "CC-B: [label]"]

Frontmatter must include:
  scout_source: [path from SCOUT GATE]
  counter_claims: [A, B, C]
  conviction_opening: Speculative
  addressable_claims: [list]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path] | conviction: Speculative"

Stage 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH (with provenance, per counter-claim, conviction tracked)

Entry: STAGE 1 COMPLETE fired.

Gather external evidence. For each item, complete the full provenance record AND label
which CC or hypothesis claim it addresses:

  | # | source | claim_addressed | forward_path | Summary | THIN-PROVENANCE? |
  |---|--------|-----------------|--------------|---------|-----------------|
  | 1 | [url]  | [CC-A / CC-B / hypothesis-main] | [Stage 4 conclusion] | [1 sentence] | yes/no |

Flag THIN-PROVENANCE for any item missing a provenance field. Do not defer.
Note standard THIN: [CC or claim] -- [area] -- [gap] for content gaps. Do not defer.

Stage 2 provenance summary:
  total_items: [N] | complete_provenance: [N] | thin_provenance: [N]

Stage 2 conviction assessment:
  cc_A_direction_this_stage: [toward Refuted / toward Open Risk / inconclusive]
  cc_B_direction_this_stage: [...]
  stage_2_move: [+1 / -1 / HOLD] -- [CC trigger phrase]
  conviction_after_stage_2: [tier]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path] | conviction: [tier] | provenance: [complete]/[total]"

Stage 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE (with provenance, per counter-claim, conviction tracked)

Entry: STAGE 2 COMPLETE fired.

Search internal sources. Same provenance format:

  | # | source | claim_addressed | forward_path | Summary | THIN-PROVENANCE? |
  |---|--------|-----------------|--------------|---------|-----------------|
  | 1 | [path] | [CC-A / CC-B / hypothesis-main] | [Stage 4 conclusion] | [1 sentence] | yes/no |

Flag THIN-PROVENANCE and standard THIN: flags at point of discovery. Do not defer.

Stage 3 provenance summary:
  total_items: [N] | complete_provenance: [N] | thin_provenance: [N]

Stage 3 conviction assessment:
  cc_A_direction_this_stage: [...]
  cc_B_direction_this_stage: [...]
  stage_3_move: [+1 / -1 / HOLD] -- [CC trigger phrase]
  conviction_after_stage_3: [tier]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path] | conviction: [tier] | provenance: [complete]/[total]"

Stage 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS (joint matrix: CC resolution x conviction trajectory)

Entry: STAGE 3 COMPLETE fired.

Counter-claim resolution table (combined Stages 2 + 3, provenance-gated):

  | Counter-Claim | Complete-prov items refuting | Complete-prov items supporting | THIN flags | Resolution |
  |---------------|------------------------------|-------------------------------|------------|------------|
  | CC-A          | [N]                          | [N]                           | [N]        | Refuted / Partially Refuted / Open Risk |
  | CC-B          | ...                          | ...                           | ...        | ...        |
  | CC-C (if any) | ...                          | ...                           | ...        | ...        |

Conviction trajectory table:

  | Stage   | Entry Level | CC Resolution Trigger         | Move     | Exit Level |
  |---------|-------------|-------------------------------|----------|------------|
  | Stage 1 | Speculative | [opening]                     | HOLD     | Speculative |
  | Stage 2 | Speculative | [CC resolution trend]         | [+1/-1/HOLD] | [tier] |
  | Stage 3 | [from S2]   | [CC resolution trend]         | [+1/-1/HOLD] | [tier] |
  | Stage 4 | [from S3]   | [final CC resolution]         | [+1/-1/HOLD] | [tier] |

  conviction_final: [tier]

Provenance completeness (combined):
  total_items: [N] | complete_provenance: [N] ([M]%) | thin_provenance: [N]

open_risk_count: [N CCs unresolved]

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path] | conviction_final: [tier] | provenance: [M]% | open_risks: [N]"

Stage 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS (verdict from conviction + CC resolution + provenance)

Entry: STAGE 4 COMPLETE fired.

OPEN RISKS (list before verdict):
  [CC-X]: [one sentence: residual risk for topic-story]
  (If none: "All counter-claims resolved.")

Provenance confidence signal:
  provenance_completeness: [M]% ([complete]/[total] items)
  provenance_quality: [Strong (>80%) / Moderate (50-80%) / Fragmented (<50%)]

Derive verdict from conviction_final:
  Confident  -> SUPPORTED
  Likely     -> PARTIALLY SUPPORTED
  Plausible or lower -> UNSUPPORTED

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Report the verdict chain in three sentences:
  Sentence 1: The evidence campaign moved conviction [opening] -> [final] driven by
              [primary CC resolution event].
  Sentence 2: [binding factor: named CC resolution or provenance gap] was the
              [decisive / limiting] element.
  Sentence 3: [N] open risk(s) and [M]% provenance completeness are the primary
              uncertainties for downstream work.

For each THIN-PROVENANCE flag: name the item, missing field, and intended claim.
For each standard THIN flag: name source stage, weakened claim, adjusted confidence.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.
