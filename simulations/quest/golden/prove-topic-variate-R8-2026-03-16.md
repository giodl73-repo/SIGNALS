---
skill: quest-variate
skill_target: prove-topic
round: R8
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [inertia_framing, confidence_gate, evidence_gap_inventory]
  combined: [V-04 (inertia_framing+exit_signal_chaining), V-05 (confidence_gate+staged_hypothesis_sharpening+two_write_synthesis)]
r7_context: >
  R7 explored three single axes: evidence_strength_tiering, staged_hypothesis_sharpening,
  and competing_explanation_protocol. V-04 combined evidence_strength_tiering with
  exit_signal_chaining (proven 100/100 from R2). V-05 combined staged_hypothesis_sharpening
  + backward_read_chain + two_write_synthesis.
  R8 explores three axes drawn from the rubric listed axes not yet exercised as singles:
  (1) inertia_framing -- the status-quo comparator is a named, defended incumbent throughout
  every stage; each stage carries an explicit incumbent-check; synthesis is framed as
  displacement-against-a-defended-position, not a verdict label;
  (2) confidence_gate -- after Stages 2 and 3 the investigator emits a per-stage confidence
  level (High/Medium/Low) with rationale; Stage 4 opens with a confidence trajectory chart;
  synthesis reports what moved confidence and why;
  (3) evidence_gap_inventory -- parallel to THIN: flags, each evidence stage ends with an
  EVIDENCE-GAP: inventory of what was sought but not found; synthesis opens with a
  completeness table before stating the verdict.
  V-04 combines inertia_framing with exit_signal_chaining: each exit signal carries the
  incumbent_holds observation so synthesis receives a wire-level picture of the competition.
  V-05 combines confidence_gate + staged_hypothesis_sharpening + two_write_synthesis:
  confidence gates feed the sharpening decision (delta annotation records what confidence
  change forced the revision); two-write synthesis delivers a confidence-trajectory evidence
  map (Write A) and a readiness signal (Write B).
  All R8 variations carry: (1) explicit scout-blocking before Stage 1, (2) per-stage
  artifact writes with full paths, (3) scout_source in hypothesis frontmatter,
  (4) THIN: flagging at point of discovery, (5) exact readiness statement closing synthesis.
---

## V-01 -- Axis: Inertia Framing

**Variation axis**: Inertia framing only -- the status-quo comparator ({status_quo_comparator})
is treated as a named, defended incumbent throughout every stage. Each evidence stage
includes an explicit "incumbent check": sources and findings are evaluated not only for
whether they support the hypothesis, but for whether they show the incumbent defending
its position. Stage 4 opens with a displacement tension table. Synthesis is framed as
a verdict against a named, active competitor with a dedicated incumbent defense summary.

**Hypothesis**: Framing evidence collection as a competition rather than a confirmation
exercise changes what investigators look for. Without an explicit incumbent check at each
stage, investigators unconsciously ignore evidence of the incumbent holding. Naming
{status_quo_comparator} as an active defender in every stage instruction forces the
investigator to assess both sides of the displacement question and delivers a synthesis
that honestly characterizes what the incumbent still does better -- not as a closing
caveat, but as a through-line.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic} displacing {status_quo_comparator}.
{status_quo_comparator} is the named incumbent. Evaluate every stage for both
displacement evidence AND incumbent defense.

## SETUP

Locate the scout artifact: glob simulations/scout/{topic}-scout-*.md

SCOUT READY cannot fire without a found file.
If absent: emit "SCOUT READY: BLOCKED." Stop.
If found: emit "SCOUT READY: [path]"

  scout_source: [path]

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 -- HYPOTHESIS

Entry: SCOUT READY fired.

Read the scout artifact. Frame a falsifiable hypothesis about {topic} displacing
{status_quo_comparator}. Name the specific dimension of displacement (cost, speed,
accuracy, adoption, etc.).

Include:
- hypothesis: [falsifiable claim -- {topic} displaces {status_quo_comparator} on [dimension]]
- incumbent_position: [one sentence -- what {status_quo_comparator} currently holds and why teams keep it]
- counter_hypothesis: [incumbent's best defense against displacement]

Frontmatter must include:
  scout_source: [SCOUT READY path]

Write: simulations/prove/{topic}-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path]"

STAGE 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEB SEARCH

Entry: STAGE 1 COMPLETE fired.

Gather minimum 3 external sources. Per source:
- Cite (URL or reference).
- Summarize in one sentence.
- Displacement evidence: does this source support {topic} displacing {status_quo_comparator}? Yes / No / Inconclusive
- Incumbent check: does this source show {status_quo_comparator} actively holding advantages? Yes / No

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

After all sources, answer the incumbent check summary:
  s2_incumbent_holds: [list dimensions where {status_quo_comparator} is shown to hold in this stage]

Write: simulations/prove/{topic}-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path]"

STAGE 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE

Entry: STAGE 2 COMPLETE fired.

Search internal sources (simulations/, specs, artifacts). Per finding:
- Exact file path.
- Relevant passage or summary.
- Displacement evidence: supports hypothesis? Yes / No / Inconclusive
- Incumbent check: does this finding show {status_quo_comparator} holding advantages? Yes / No

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

After all findings, answer the incumbent check summary:
  s3_incumbent_holds: [list dimensions where {status_quo_comparator} is shown to hold in this stage]

Write: simulations/prove/{topic}-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path]"

STAGE 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS

Entry: STAGE 3 COMPLETE fired.

Open with the displacement tension table:

| Dimension | {topic} evidence | {status_quo_comparator} still holds |
|-----------|-----------------|--------------------------------------|
| [dim 1]   | [supporting sources] | [incumbent hold from S2+S3] |
| [dim 2]   | [supporting sources] | [incumbent hold from S2+S3] |
| ...       | ...             | ...                                  |

Analyze patterns across Stage 2 and Stage 3 evidence.
Distinguish causation from correlation.
Displacement verdict: Yes / No / Pending. Explain in 1-2 sentences.

Write: simulations/prove/{topic}-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path]"

STAGE 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS

Entry: STAGE 4 COMPLETE fired.

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Displacement verdict (1-2 sentences): on which dimension(s) does {topic} displace
{status_quo_comparator}, and on which does the incumbent still hold?

Summarize the supporting displacement evidence in 2-3 sentences.

Incumbent defense summary: name 1-3 specific dimensions where {status_quo_comparator}
continues to hold, drawn from s2_incumbent_holds and s3_incumbent_holds.

For each THIN-flagged claim from Stages 2-3: name the source stage, the weakened
claim, and your adjusted confidence for that dimension.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/{topic}-synthesis-{date}.md
Confirm write.

---

## V-02 -- Axis: Confidence Gate

**Variation axis**: Confidence gate only -- after completing evidence collection in Stage 2
and Stage 3, the investigator emits a per-stage confidence assessment on the hypothesis:
High / Medium / Low, with a one-sentence rationale explaining what drove the rating.
Stage 4 analysis opens with a confidence trajectory chart. Stage 5 synthesis reports the
full trajectory and names what drove each movement.

**Hypothesis**: Without an explicit confidence assessment after each evidence batch,
synthesis treats all stages as equally informative -- a single strong source in Stage 2
and five weak findings in Stage 3 arrive at synthesis with equal implicit weight. Requiring
the investigator to rate confidence after each stage externalizes the belief-update process:
Stage 4 can reason about why confidence moved, and synthesis delivers a verdict whose
confidence level is traceable to specific evidence stages rather than emerging opaquely
from the full batch.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic} against {status_quo_comparator}.
After each evidence stage, gate on a confidence assessment before the next stage begins.
Stage 4 and Stage 5 reason over the confidence trajectory.

## SETUP

Locate the scout artifact: glob simulations/scout/{topic}-scout-*.md

SCOUT READY cannot fire without a found file.
If absent: emit "SCOUT READY: BLOCKED." Stop.
If found: emit "SCOUT READY: [path]"

  scout_source: [path]

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 -- HYPOTHESIS

Entry: SCOUT READY fired.

Read the scout artifact. Frame a falsifiable hypothesis about {topic} displacing
{status_quo_comparator}. Include counter_hypothesis (incumbent's best defense).

Frontmatter must include:
  scout_source: [SCOUT READY path]
  confidence_prior: [High / Medium / Low -- prior probability before evidence collection]
  confidence_prior_rationale: [one sentence -- what from the scout artifact sets this prior]

Write: simulations/prove/{topic}-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path] | Prior confidence: [level]"

STAGE 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEB SEARCH

Entry: STAGE 1 COMPLETE fired.

Gather minimum 3 external sources. Per source:
- Cite (URL or reference).
- Summarize in one sentence.
- Supports or opposes displacement of {status_quo_comparator} by {topic}? Yes / No / Inconclusive

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

After all sources, emit the Stage 2 confidence gate:
  s2_confidence: [High / Medium / Low]
  s2_confidence_rationale: [one sentence -- what drove the rating up, down, or held it vs. prior]

Write: simulations/prove/{topic}-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path] | S2 confidence: [s2_confidence]"

STAGE 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE

Entry: STAGE 2 COMPLETE fired. S2 confidence: [s2_confidence].

Search internal sources (simulations/, specs, artifacts). Per finding:
- Exact file path.
- Relevant passage or summary.
- Supports or opposes the hypothesis?

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

After all findings, emit the Stage 3 confidence gate:
  s3_confidence: [High / Medium / Low]
  s3_confidence_rationale: [one sentence -- what drove the rating vs. S2]

Write: simulations/prove/{topic}-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path] | S3 confidence: [s3_confidence]"

STAGE 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS

Entry: STAGE 3 COMPLETE fired. Confidence trajectory available.

Open with the confidence trajectory chart:

| Stage | Confidence | Driver |
|-------|-----------|--------|
| S1 Hypothesis | [prior] | [rationale] |
| S2 Web Search | [s2_confidence] | [s2_rationale] |
| S3 Intelligence | [s3_confidence] | [s3_rationale] |

Analyze patterns across Stage 2 and Stage 3 evidence.
Distinguish causation from correlation.
Displacement verdict: Yes / No / Pending. Explain in 1-2 sentences.

Write: simulations/prove/{topic}-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path]"

STAGE 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS

Entry: STAGE 4 COMPLETE fired.

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Report the confidence trajectory:
  confidence_trajectory: [prior] -> [s2_confidence] -> [s3_confidence] -> [final verdict]
  trajectory_summary: [one sentence -- did evidence strengthen, weaken, or hold confidence?]

Summarize the supporting evidence in 2-3 sentences.

For each THIN-flagged claim from Stages 2-3: name the source stage, the weakened
claim, and your adjusted confidence for that dimension.

Name the primary adoption risk: what does {status_quo_comparator} still do better?

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/{topic}-synthesis-{date}.md
Confirm write.

---

## V-03 -- Axis: Evidence Gap Inventory

**Variation axis**: Evidence gap inventory only -- parallel to THIN: flags (which mark
weak or thin claims found), each evidence stage (2 and 3) ends with an explicit
EVIDENCE-GAP: inventory listing evidence that was sought but not found. Gaps are named
with a category and a one-sentence note on why the gap matters to the hypothesis.
Stage 5 synthesis opens with a completeness table (gaps filled vs. remaining) before
stating the verdict.

**Hypothesis**: THIN: flags address evidence that was found but is weak. Evidence-gap
inventory addresses a different failure mode: the absence of evidence that should exist.
A synthesis that does not account for what it could not find may reach a confident verdict
on incomplete coverage. An explicit gap inventory at each stage forces the investigator to
name the shape of the unknown before synthesizing, and the completeness table gives the
reader a calibrated view of how much of the planned evidence was actually available.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic} against {status_quo_comparator}.
Inventory evidence gaps at each collection stage. Synthesis opens with a completeness
assessment before stating the verdict.

## SETUP

Locate the scout artifact: glob simulations/scout/{topic}-scout-*.md

SCOUT READY cannot fire without a found file.
If absent: emit "SCOUT READY: BLOCKED." Stop.
If found: emit "SCOUT READY: [path]"

  scout_source: [path]

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 -- HYPOTHESIS

Entry: SCOUT READY fired.

Read the scout artifact. Frame a falsifiable hypothesis about {topic} displacing
{status_quo_comparator}. Include counter_hypothesis.

List the evidence types you expect to find in Stages 2-3 that would confirm or deny
the hypothesis (e.g., adoption studies, pricing comparisons, user research, internal
specs). This is the evidence plan against which gaps will be measured.

  evidence_plan: [list 3-5 expected evidence types]

Frontmatter must include:
  scout_source: [SCOUT READY path]

Write: simulations/prove/{topic}-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path]"

STAGE 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEB SEARCH

Entry: STAGE 1 COMPLETE fired.

Gather minimum 3 external sources. Per source:
- Cite (URL or reference).
- Summarize in one sentence.
- Supports or opposes displacement of {status_quo_comparator} by {topic}? Yes / No / Inconclusive

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

After all sources, inventory evidence gaps:
For each evidence type from the evidence_plan that you sought but could not find,
emit: EVIDENCE-GAP: [category] -- [what was sought] -- [why it matters to the hypothesis]

Write: simulations/prove/{topic}-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path]"

STAGE 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE

Entry: STAGE 2 COMPLETE fired.

Search internal sources (simulations/, specs, artifacts). Per finding:
- Exact file path.
- Relevant passage or summary.
- Supports or opposes the hypothesis?

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

After all findings, inventory evidence gaps:
For each evidence type from the evidence_plan (or new gaps discovered) that was
sought but not found internally, emit:
EVIDENCE-GAP: [category] -- [what was sought] -- [why it matters to the hypothesis]

For any S2 gap partially or fully filled by internal sources, emit:
EVIDENCE-GAP-FILLED: [category] -- [internal source that filled it]

Write: simulations/prove/{topic}-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path]"

STAGE 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS

Entry: STAGE 3 COMPLETE fired.

Analyze patterns across Stage 2 and Stage 3 evidence.
Distinguish causation from correlation.
Displacement verdict: Yes / No / Pending. Explain in 1-2 sentences.

Write: simulations/prove/{topic}-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path]"

STAGE 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS

Entry: STAGE 4 COMPLETE fired.

Open with the evidence completeness table:

| Evidence Type | Planned | Found | Gap Remaining |
|--------------|---------|-------|---------------|
| [type 1] | Yes | Yes / Partial / No | [gap note or "none"] |
| [type 2] | Yes | Yes / Partial / No | [gap note or "none"] |
| ...      | ...     | ...   | ...           |

  completeness_rating: [Complete / Mostly Complete / Partial / Incomplete]
  completeness_note: [one sentence -- how gaps affect verdict confidence]

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Summarize the supporting evidence in 2-3 sentences.

For each THIN-flagged claim from Stages 2-3: name the source stage, the weakened
claim, and your adjusted confidence for that dimension.

For each EVIDENCE-GAP that remains unfilled: name the category and note how it
would change the verdict if filled with positive vs. negative evidence.

Name the primary adoption risk: what does {status_quo_comparator} still do better?

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/{topic}-synthesis-{date}.md
Confirm write.

---

## V-04 -- Combined: Inertia Framing + Exit-Signal Chaining

**Variation axes**: Inertia framing (V-01 single axis this round) combined with exit-signal
chaining (R2-V02 proven 100/100 excellence pattern). The exit signal carries the
incumbent_holds observation as part of its payload, so synthesis receives a wire-level
picture of where {status_quo_comparator} is defending at every stage boundary rather
than constructing the picture from memory at the end.

**Hypothesis**: Exit-signal chaining provides the structural gate enforcement that scored
100/100 in R2. Carrying the incumbent_holds observation on the signal wire addresses a
weakness in all prior variations: the incumbent's defense is assembled retroactively in
synthesis rather than being tracked as evidence accumulates. Wiring the incumbent
assessment into the signal chain makes the competition visible at each stage boundary
and prevents synthesis from cherry-picking the incumbent's weaknesses while ignoring
the strengths gathered stage by stage.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic} displacing {status_quo_comparator}.
Exit signals chain each stage to the next and carry the current incumbent-holds
observation so synthesis receives a running wire-level picture of the competition.

## SETUP

Locate the scout artifact: glob simulations/scout/{topic}-scout-*.md

SCOUT READY cannot fire without a found file.
If absent: emit "SCOUT READY: BLOCKED." Stop.
If found: emit "SCOUT READY: [path]"

  scout_source: [path]

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 -- HYPOTHESIS

Entry: SCOUT READY fired.

Read the scout artifact at [SCOUT READY path]. Frame a falsifiable hypothesis about
{topic} displacing {status_quo_comparator} on a named dimension.

Include:
- hypothesis: [falsifiable claim]
- incumbent_position: [what {status_quo_comparator} currently holds -- one sentence]
- counter_hypothesis: [incumbent's best defense]

Frontmatter must include:
  scout_source: [SCOUT READY path]

Write: simulations/prove/{topic}-hypothesis-{date}.md
Confirm write.
Emit: "STAGE 1 COMPLETE: [path] | Incumbent: [incumbent_position abbreviated to <15 words]"

STAGE 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEB SEARCH

Entry: STAGE 1 COMPLETE fired. Incumbent position received.

Gather minimum 3 external sources. Per source:
- Cite (URL or reference).
- Summarize in one sentence.
- Displacement evidence: supports {topic} displacing {status_quo_comparator}? Yes / No / Inconclusive
- Incumbent check: does this source show {status_quo_comparator} actively holding? Yes / No

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

After all sources, tally:
  s2_displacement_support: [N sources supporting displacement]
  s2_incumbent_holds: [key dimension(s) where incumbent is shown to hold]

Write: simulations/prove/{topic}-websearch-{date}.md
Confirm write.
Emit: "STAGE 2 COMPLETE: [path] | Displacement support: [s2_displacement_support] | Incumbent holds: [s2_incumbent_holds]"

STAGE 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE

Entry: STAGE 2 COMPLETE fired. S2 payload received.

Search internal sources (simulations/, specs, artifacts). Per finding:
- Exact file path.
- Relevant passage or summary.
- Displacement evidence: supports hypothesis? Yes / No / Inconclusive
- Incumbent check: does this finding show {status_quo_comparator} holding? Yes / No

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

After all findings, tally:
  s3_displacement_support: [N findings supporting displacement]
  s3_incumbent_holds: [key dimension(s) where incumbent is shown to hold internally]

Write: simulations/prove/{topic}-intelligence-{date}.md
Confirm write.
Emit: "STAGE 3 COMPLETE: [path] | Displacement support: [s3_displacement_support] | Incumbent holds: [s3_incumbent_holds]"

STAGE 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS

Entry: STAGE 3 COMPLETE fired. Full signal chain received.

Open with the displacement tension table from the signal chain:

| Dimension | Displacement evidence | {status_quo_comparator} holds |
|-----------|-----------------------|-------------------------------|
| [from combined incumbent_holds] | [count] | [yes/partial/no] |

Analyze patterns. Distinguish causation from correlation.
Displacement verdict: Yes / No / Pending. Explain in 1-2 sentences.

  combined_displacement_support: [S2 + S3 total]
  combined_incumbent_holds: [merged list from signal chain]

Write: simulations/prove/{topic}-analysis-{date}.md
Confirm write.
Emit: "STAGE 4 COMPLETE: [path] | Support: [combined_displacement_support] | Incumbent still holds: [combined_incumbent_holds abbreviated]"

STAGE 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS

Entry: STAGE 4 COMPLETE fired. Full wire history available.

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Displacement verdict (2-3 sentences): cite the combined_displacement_support count
and name the primary dimension of displacement.

Incumbent defense summary: name 1-3 specific dimensions from the combined_incumbent_holds
wire where {status_quo_comparator} continues to hold. These are the adoption barriers.

For each THIN-flagged claim from Stages 2-3: name the source stage, the weakened
claim, and your adjusted confidence for that dimension.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/{topic}-synthesis-{date}.md
Confirm write.

---

## V-05 -- Combined: Confidence Gate + Staged Hypothesis Sharpening + Two-Write Synthesis

**Variation axes**: Confidence gate (V-02 single axis this round), staged hypothesis
sharpening (R7-V02 pattern), and two-write synthesis (R2-V04 proven excellence pattern).
The three axes operate at independent levels -- belief-state tracking (confidence gate),
belief revision (sharpening), and output structure (two-write) -- so no axis competes
with another. The confidence gate feeds the sharpening decision: the Stage 3 delta
annotation records which confidence change forced the revision. Two-write synthesis
delivers a confidence-trajectory evidence map (Write A) and a readiness signal (Write B).

**Hypothesis**: Staged hypothesis sharpening (R7) forced explicit belief revision but did
not track what drove the revision. Confidence gates (R8) track belief movement but have
not yet been connected to the sharpening step. Combining them creates a causal chain: if
S3 confidence drops from S2, the sharpening MUST reflect what internal evidence forced
the narrowing. Two-write synthesis closes the loop: Write A maps claims to
confidence-traced evidence; Write B is the clean readiness signal. Together the three
axes address three independent failure modes from prior rounds: invisible belief revision,
untraceable confidence movement, and verdict-readiness conflation.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic} against {status_quo_comparator}.
Confidence gates track belief movement. The hypothesis sharpens mid-campaign, informed
by the confidence trajectory. Synthesis writes a confidence-trajectory evidence map and
a separate readiness signal.

## SETUP

Locate the scout artifact: glob simulations/scout/{topic}-scout-*.md

SCOUT READY cannot fire without a found file.
If absent: emit "SCOUT READY: BLOCKED." Stop.
If found: record scout_source: [exact path].
Emit: "SETUP COMPLETE. Chain head: [scout_source]"

STAGE 1 cannot begin until SETUP COMPLETE fires.

---

## STAGE 1 -- HYPOTHESIS

Entry: SETUP COMPLETE. Chain head: [scout_source].

Read the scout artifact at [scout_source]. Frame a falsifiable hypothesis about {topic}
displacing {status_quo_comparator}.

Include:
- hypothesis_v1: [falsifiable claim]
- counter_hypothesis: [incumbent's best defense]
- confidence_prior: [High / Medium / Low -- prior probability before evidence collection]
- confidence_prior_rationale: [one sentence -- what from the scout artifact sets this prior]

Frontmatter must include:
  scout_source: [exact path from SETUP]
  hypothesis_version: v1
  confidence_prior: [level]

Write: simulations/prove/{topic}-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path] | Prior: [confidence_prior]"

STAGE 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEB SEARCH

Entry: STAGE 1 COMPLETE fired.

Gather minimum 3 external sources. Per source:
- Cite (URL or reference).
- Summarize in one sentence.
- Supports or opposes displacement of {status_quo_comparator} by {topic}? Yes / No / Inconclusive

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

After all sources, emit the Stage 2 confidence gate:
  s2_confidence: [High / Medium / Low]
  s2_confidence_rationale: [one sentence -- what drove the rating up, down, or held it vs. prior]

Write: simulations/prove/{topic}-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path] | S2 confidence: [s2_confidence]"

STAGE 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE + HYPOTHESIS SHARPENING

Entry: STAGE 2 COMPLETE fired. S2 confidence: [s2_confidence].

Search internal sources (simulations/, specs, artifacts). Per finding:
- Exact file path.
- Relevant passage or summary.
- Supports or opposes the hypothesis?

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

After recording all internal findings, emit the Stage 3 confidence gate:
  s3_confidence: [High / Medium / Low]
  s3_confidence_rationale: [one sentence -- what drove the rating vs. S2]

Then sharpen the hypothesis. The sharpening MUST be informed by the confidence
trajectory -- if confidence moved, the delta annotation must name why:

  hypothesis_v1: [original from Stage 1]
  hypothesis_v2: [sharpened -- narrow or qualify the claim based on Stages 2-3 evidence]
  delta: [one sentence -- what changed and what in the confidence trajectory forced the change]
  confidence_trigger: [the specific evidence or gap that caused confidence to move]

If no sharpening is warranted: state "hypothesis_v2: unchanged" and explain why in one
sentence (include that confidence was stable if applicable).

Frontmatter must include:
  hypothesis_version: v2
  s3_confidence: [level]

Write: simulations/prove/{topic}-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path] | S3 confidence: [s3_confidence] | Hypothesis v2 set"

STAGE 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS

Entry: STAGE 3 COMPLETE fired. Hypothesis v2 and full confidence trajectory available.

Open with the confidence trajectory chart:

| Stage | Confidence | Driver |
|-------|-----------|--------|
| S1 Hypothesis | [confidence_prior] | [prior rationale] |
| S2 Web Search | [s2_confidence] | [s2 rationale] |
| S3 Intelligence | [s3_confidence] | [s3 rationale + confidence_trigger if applicable] |

State hypothesis_v2 explicitly before analyzing.

Analyze patterns across Stage 2 and Stage 3 evidence against hypothesis_v2.
Distinguish causation from correlation.
Displacement verdict: Yes / No / Pending. Explain in 1-2 sentences.

Write: simulations/prove/{topic}-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path]"

STAGE 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS

Entry: STAGE 4 COMPLETE fired.

### Write A -- Confidence-Trajectory Evidence Map

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Report the full confidence trajectory:
  confidence_trajectory: [prior] -> [s2_confidence] -> [s3_confidence] -> [final verdict label]
  trajectory_summary: [one sentence -- did evidence strengthen, weaken, or hold confidence, and why?]

Trace the hypothesis evolution:
  hypothesis_v1: [Stage 1 original]
  hypothesis_v2: [Stage 3 sharpened]
  delta_summary: [what the confidence trajectory forced us to change and why]

For each major displacement claim in hypothesis_v2:
- State the claim.
- Cite supporting evidence (stage + source).
- If THIN-flagged: name the source stage, the weakened claim, and adjusted confidence.

Name the primary adoption risk: what does {status_quo_comparator} still do better?

Write A: simulations/prove/{topic}-synthesis-{date}.md
Confirm Write A.

### Write B -- Readiness Signal

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

Write B: simulations/prove/{topic}-handoff-{date}.md
Confirm Write B.
