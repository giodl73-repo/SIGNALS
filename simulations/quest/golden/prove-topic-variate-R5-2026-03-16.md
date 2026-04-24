---
skill: quest-variate
skill_target: prove-topic
round: R5
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [inertia_framing, output_format_table, phrasing_register_conversational]
  combined: [V-04 (role_sequence+lifecycle_emphasis), V-05 (inertia+exit_signal+two_write)]
r2_context: >
  Rubric v14 ceiling reached in R2. Four of five variations scored 100/100.
  V-01 (minimalism) scored 97.5 on C-10 (structural block prose-only).
  Excellence signals: exit-signal chaining, two-write synthesis, role-sequence architecture.
  R5 explores three untested single axes (inertia framing, all-table format, conversational
  register) plus two combinations that integrate R2 excellence patterns with new axes.
  All R5 variations carry: (1) SCOUT READY structural block, (2) per-stage artifact writes
  with full paths, (3) synthesis closing with exact readiness statement, (4) in-artifact
  scout_source in hypothesis frontmatter, (5) THIN: flagging at point of discovery.
---

## V-01 — Axis: Inertia Framing

**Variation axis**: Inertia framing only — the incumbent/status-quo is named at the top and
serves as the narrative spine throughout. Every stage carries an explicit displacement check
asking how that stage's evidence bears on displacing the incumbent. The campaign is framed as
a displacement case, not a neutral investigation.

**Hypothesis**: Making the incumbent the explicit narrative center at every stage will make
the displacement logic easier to follow and harder to skip, without adding structural
complexity that would conflict with a minimalist prompt body.

---

Topic: {topic}
Date: {date}

You are building the displacement case: does {topic} give teams a credible reason to stop
using {status_quo_comparator}?

Every stage answers the same question from a new angle. Run them in order.

**Before Stage 1 — Identify and locate.**

Name the incumbent:
- incumbent: {status_quo_comparator}
- incumbent_strength: [one sentence — why {status_quo_comparator} currently wins]
- incumbent_vulnerability: [one sentence — where {status_quo_comparator} is most exposed]

Locate the scout artifact: glob for `simulations/scout/{topic}-scout-*.md`
SCOUT READY cannot fire without a found file.
If absent: emit "SCOUT READY: BLOCKED." Do not proceed.
If found: emit "SCOUT READY: [path]"

STAGE 1 cannot begin until SCOUT READY fires.

---

**Stage 1 — Hypothesis**

Entry: SCOUT READY fired.

Read the scout artifact. Frame the hypothesis as a displacement claim:
- hypothesis: [falsifiable claim that {topic} can displace {status_quo_comparator} on [dimension]]
- counter_hypothesis: [the incumbent's best defense — grounded in incumbent_strength]
- displacement_dimension: [the single axis where the displacement case is strongest]

Frontmatter must include:
  scout_source: [SCOUT READY path]
  incumbent: {status_quo_comparator}
  displacement_dimension: [value]

Write: simulations/prove/{topic}-hypothesis-{date}.md
Confirm write. Emit: STAGE 1 COMPLETE.

---

**Stage 2 — Web Search**

Entry: STAGE 1 COMPLETE.

Gather minimum 3 external sources. For each:
1. Cite source (URL or reference).
2. Summarize in one sentence.
3. Displacement check: does this support displacing {status_quo_comparator} with {topic}
   on [displacement_dimension]? Yes / No / Inconclusive

If evidence is thin or absent in any area: note THIN: [area] — [gap] at point of discovery.
Do not defer to synthesis.

Write: simulations/prove/{topic}-websearch-{date}.md
Confirm write. Emit: STAGE 2 COMPLETE.

---

**Stage 3 — Intelligence**

Entry: STAGE 2 COMPLETE.

Search internal sources (simulations/, specs, existing artifacts). For each finding:
- File path (exact).
- Relevant passage or summary.
- Displacement check: does this internal evidence support or undermine {topic}
  displacing {status_quo_comparator}? Yes / No / Inconclusive

If evidence is thin or absent: note THIN: [area] — [gap] at point of discovery.
Do not defer.

Write: simulations/prove/{topic}-intelligence-{date}.md
Confirm write. Emit: STAGE 3 COMPLETE.

---

**Stage 4 — Analysis**

Entry: STAGE 3 COMPLETE.

Analyze patterns across Stage 2 and Stage 3 evidence.
Distinguish causation from correlation.

Displacement verdict: considering all evidence, does {topic} make a credible case for
displacing {status_quo_comparator}? Answer: Yes / No / Pending.
Explain in 1-2 sentences, naming the incumbent's residual strength where verdict is not Yes.

Write: simulations/prove/{topic}-analysis-{date}.md
Confirm write. Emit: STAGE 4 COMPLETE.

---

**Stage 5 — Synthesis**

Entry: STAGE 4 COMPLETE.

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED — and why in 2-3 sentences.

Then address the incumbent directly:
- What does {status_quo_comparator} still do better? (primary adoption risk)
- For each THIN-flagged claim from Stages 2-3: name the source stage, the weakened claim,
  and your adjusted confidence.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/{topic}-synthesis-{date}.md
Confirm write.

---

## V-02 — Axis: Output Format (All-Table with Evidence Strength Scale)

**Variation axis**: Output format only — every stage body produces a structured table.
Evidence is captured with explicit columns. A three-point strength scale (Strong /
Moderate / Weak) scores each evidence item. No prose blocks inside stage bodies;
structure carries the semantics.

**Hypothesis**: All-table formatting forces every evidence item to be explicit and
comparable across stages, making thin-evidence gaps immediately visible as incomplete
rows rather than deferred prose notes. This may satisfy C-08 more reliably than
inline THIN: flags in prose.

---

Topic: {topic}
Date: {date}

You are running the full prove evidence campaign for {topic} against {status_quo_comparator}.

## SETUP

| Field | Value |
|-------|-------|
| topic | {topic} |
| date | {date} |
| incumbent | {status_quo_comparator} |
| scout_artifact | [glob simulations/scout/{topic}-scout-*.md — record path or ABSENT] |

If scout_artifact = ABSENT: halt. Emit:
"CAMPAIGN BLOCKED — no scout artifact found for {topic}. Run /scout first."
Do not proceed.

## STAGE 1 — HYPOTHESIS

Entry: scout_artifact path confirmed above.

Read scout artifact. Complete:

| Field | Value |
|-------|-------|
| hypothesis | [falsifiable displacement claim] |
| counter_hypothesis | [incumbent's best defense] |
| scout_source | [exact path from SETUP] |

Write: simulations/prove/{topic}-hypothesis-{date}.md
Frontmatter must include scout_source.
Confirm write. Emit: STAGE 1 COMPLETE.

## STAGE 2 — WEB SEARCH

Entry: STAGE 1 COMPLETE.

Gather minimum 3 external sources. Complete evidence table:

| # | Source | Summary (1 sentence) | Supports displacement? | Strength | Gap |
|---|--------|----------------------|------------------------|----------|-----|
| 1 | [URL or citation] | | Yes / No / Inconclusive | Strong / Moderate / Weak | [THIN: area or —] |
| 2 | | | | | |
| 3 | | | | | |

Record THIN: [area] in the Gap column at point of discovery. Do not defer.

Write: simulations/prove/{topic}-websearch-{date}.md
Confirm write. Emit: STAGE 2 COMPLETE.

## STAGE 3 — INTELLIGENCE

Entry: STAGE 2 COMPLETE.

Search internal sources. Complete:

| # | File Path | Relevant Passage | Supports displacement? | Strength | Gap |
|---|-----------|-----------------|------------------------|----------|-----|
| 1 | [path] | [passage] | Yes / No / Inconclusive | Strong / Moderate / Weak | [THIN: area or —] |
| 2 | | | | | |

Record THIN: [area] in the Gap column at point of discovery. Do not defer.

Write: simulations/prove/{topic}-intelligence-{date}.md
Confirm write. Emit: STAGE 3 COMPLETE.

## STAGE 4 — ANALYSIS

Entry: STAGE 3 COMPLETE.

| Field | Value |
|-------|-------|
| primary_pattern | [dominant pattern across Stage 2 + Stage 3] |
| causation_note | [correlation vs causation assessment] |
| displacement_verdict | Yes / No / Pending |
| verdict_explanation | [1-2 sentences] |

Write: simulations/prove/{topic}-analysis-{date}.md
Confirm write. Emit: STAGE 4 COMPLETE.

## STAGE 5 — SYNTHESIS

Entry: STAGE 4 COMPLETE.

| Field | Value |
|-------|-------|
| hypothesis_verdict | SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED |
| evidence_summary | [2-3 sentences integrating Stages 2-4] |
| confidence | High / Medium / Low |
| thin_adjustments | [for each THIN: source stage — weakened claim — adjusted confidence] |
| primary_risk | [residual incumbent strength framed as adoption barrier] |
| readiness | Evidence brief for {topic} is ready for /topic-story. |

Write: simulations/prove/{topic}-synthesis-{date}.md
Confirm write.

---

## V-03 — Axis: Phrasing Register (Conversational / Second-Person)

**Variation axis**: Phrasing register only — conversational second-person imperative
throughout. Low formality. "Your job is...", "Start here...", "Before you move on..."
No section headers, no checkbox entry conditions, no formal exit signals. The structural
constraints are expressed as natural-language gates.

**Hypothesis**: Conversational phrasing reduces cognitive overhead for a first-time
reader at the cost of some structural explicitness. If all rubric criteria can be
satisfied in plain prose, the result is a more inviting prompt that a non-technical
PM can follow without referencing a style guide.

---

Topic: {topic}
Date: {date}

Your job in this session: find out whether {topic} can displace {status_quo_comparator}.
You'll run five investigation stages, write one artifact per stage, and close with a brief
that's ready to hand off to /topic-story.

Start by finding the scout artifact.

Search for: simulations/scout/{topic}-scout-*.md

If you can't find it — stop. Don't guess, don't skip ahead. Say:
"No scout artifact found for {topic}. Stopping here."

If you find it — read it. You'll use it to frame your hypothesis.

---

Stage 1: Hypothesis

What do you believe is true about {topic}'s ability to replace {status_quo_comparator}?
Write a falsifiable claim — something you can check against evidence.
Also write the strongest counterargument: why might {status_quo_comparator} still win?

In your artifact, make sure to include:
- scout_source: [path to the scout artifact you just read]

Write to: simulations/prove/{topic}-hypothesis-{date}.md
Say "Hypothesis written." before moving to Stage 2.

---

Stage 2: Web Search

Find at least 3 external sources that bear on your hypothesis.
For each one: where did you find it, what does it say in one sentence, and does it support
or undermine the case for {topic} displacing {status_quo_comparator}?

If a source area feels thin or is just missing — note it right here, right now.
Don't save the gap for later. Write: THIN: [area] — [what's missing]

Write to: simulations/prove/{topic}-websearch-{date}.md
Say "Web search written." before moving to Stage 3.

---

Stage 3: Intelligence

Now dig into your own project files. Search simulations/, specs, and existing artifacts
for anything relevant to your hypothesis.
For each finding: give the file path and the relevant passage or summary.
Same rule on gaps — if something's thin or absent, note it now: THIN: [area] — [gap]

Write to: simulations/prove/{topic}-intelligence-{date}.md
Say "Intelligence written." before moving to Stage 4.

---

Stage 4: Analysis

Step back from the individual sources. What patterns do you see across Stage 2 and Stage 3?
Be honest about what's correlation vs causation.

Give a displacement verdict: does the evidence support {topic} displacing
{status_quo_comparator}? Answer: Yes / No / Pending — and explain why in one or two sentences.

Write to: simulations/prove/{topic}-analysis-{date}.md
Say "Analysis written." before moving to Stage 5.

---

Stage 5: Synthesis

Lead with your answer: SUPPORTED, PARTIALLY SUPPORTED, or UNSUPPORTED.
Explain in 2-3 sentences using evidence from Stages 2, 3, and 4.

For every THIN-flagged claim from Stages 2-3: name the stage, the weakened claim, and
your adjusted confidence in that piece of the argument.

Name the biggest residual risk: what does {status_quo_comparator} still do better?

End with this exact sentence:
Evidence brief for {topic} is ready for /topic-story.

Write to: simulations/prove/{topic}-synthesis-{date}.md
Done.

---

## V-04 — Combined: Role Sequence + Lifecycle Emphasis

**Variation axes**: Role sequence (three named roles with explicit handoff ownership) combined
with lifecycle emphasis (each phase boundary is a table-structured handoff block; stage
bodies are tightly compressed to the essential operations only). Role architecture satisfies
C-02/C-06/C-10 by construction; compressed stage bodies test whether the rubric
criteria survive radical lifecycle compression.

**Hypothesis**: Three-role framing (SCOUT → ANALYST → SYNTHESIZER) with structured handoff
tables makes the structural scout-before-hypothesis constraint architectural rather than
instructional, while compressed stage bodies demonstrate how little prose is needed to satisfy
all ten criteria when the structure does the work.

---

Topic: {topic}
Date: {date}

Three roles run this campaign in order. Each role completes before the next begins.

---

### SCOUT

SCOUT owns pre-campaign setup. ANALYST does not begin until SCOUT HANDOFF is emitted.

1. Glob: simulations/scout/{topic}-scout-*.md
   If absent: emit "SCOUT HANDOFF: BLOCKED — no scout artifact." Campaign halts.
   If found: continue.

2. Read the scout artifact. Extract 3 key signals relevant to the displacement question:
   can {topic} displace {status_quo_comparator}?

SCOUT HANDOFF:
| Field | Value |
|-------|-------|
| scout_source | [exact file path] |
| incumbent | {status_quo_comparator} |
| signal_1 | [key finding] |
| signal_2 | [key finding] |
| signal_3 | [key finding] |

Emit: "SCOUT HANDOFF COMPLETE. ANALYST begins."

---

### ANALYST

Entry: SCOUT HANDOFF COMPLETE received. scout_source confirmed present.

Run four stages. Each stage writes one artifact. Stage N+1 does not begin until
stage N write is confirmed.

**Stage 1 — Hypothesis**
Frame falsifiable claim about {topic} displacing {status_quo_comparator}.
Include counter_hypothesis (incumbent's best defense).
Frontmatter: scout_source: [from SCOUT HANDOFF]
Write: simulations/prove/{topic}-hypothesis-{date}.md. Confirm.

**Stage 2 — Web Search**
Minimum 3 external sources. Per source: cite, summarize, state displacement relevance.
Flag thin or absent evidence at point of discovery: THIN: [area] — [gap]
Write: simulations/prove/{topic}-websearch-{date}.md. Confirm.

**Stage 3 — Intelligence**
Search internal files. Per finding: file path, passage, displacement relevance.
Flag thin or absent evidence at point of discovery: THIN: [area] — [gap]
Write: simulations/prove/{topic}-intelligence-{date}.md. Confirm.

**Stage 4 — Analysis**
Cross-stage patterns. Causation vs correlation. Displacement verdict: Yes / No / Pending.
Write: simulations/prove/{topic}-analysis-{date}.md. Confirm.

ANALYST HANDOFF:
| Field | Value |
|-------|-------|
| hypothesis | [claim from Stage 1] |
| displacement_verdict | [Yes/No/Pending from Stage 4] |
| thin_flags | [THIN items from Stages 2-3, or "none"] |
| artifacts_written | hypothesis, websearch, intelligence, analysis |

Emit: "ANALYST HANDOFF COMPLETE. SYNTHESIZER begins."

---

### SYNTHESIZER

Entry: ANALYST HANDOFF COMPLETE received. All four artifacts confirmed.

**Stage 5 — Synthesis**

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED.
Integrate evidence from Stages 2-4 in 2-3 sentences with explicit displacement verdict.
For each THIN-flagged item from ANALYST HANDOFF: name source stage, weakened claim,
adjusted confidence.
State primary adoption risk as residual incumbent strength.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/{topic}-synthesis-{date}.md
Confirm write.

---

## V-05 — Combined: Inertia Framing + Exit-Signal Chaining + Two-Write Synthesis

**Variation axes**: Exit-signal chaining (R2 V-02 pattern: SCOUT READY + STAGE N cannot
begin until prior signal fires), two-write synthesis (R2 V-04 pattern: Write A = claim-
evidence map with per-claim thin adjustments; Write B = readiness signal), and strong
inertia framing throughout (incumbent named at open, displacement check at every stage,
synthesis centers on the displacement verdict). All three R2 excellence patterns combined
with the untested inertia axis.

**Hypothesis**: Combining exit-signal chaining (structural enforcement), two-write synthesis
(thin-evidence propagation by construction), and inertia framing (displacement narrative
coherence) produces a prompt where every rubric criterion is satisfied architecturally —
no criterion relies solely on a prose reminder that could be omitted at execution time.

---

Topic: {topic}
Date: {date}

This campaign answers one question: can {topic} displace {status_quo_comparator}?

## CAMPAIGN OPEN

Name the incumbent before any stage runs.

  incumbent: {status_quo_comparator}
  incumbent_strength: [one sentence — why {status_quo_comparator} currently wins]
  incumbent_vulnerability: [one sentence — where {status_quo_comparator} is most exposed]

Locate the scout artifact: glob for simulations/scout/{topic}-scout-*.md
SCOUT READY cannot fire without a found file.
If absent: emit "SCOUT READY: BLOCKED." Stop here.
If found: emit "SCOUT READY: [path]"

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 — HYPOTHESIS

Entry: SCOUT READY fired.

Read the scout artifact. Frame the displacement hypothesis:
- hypothesis: [falsifiable claim that {topic} displaces {status_quo_comparator} on [dimension]]
- counter_hypothesis: [incumbent's best defense — grounded in incumbent_strength above]
- displacement_dimension: [the axis where displacement is most credible]

Frontmatter must include:
  scout_source: [SCOUT READY path]
  incumbent: {status_quo_comparator}
  displacement_dimension: [value]

Write: simulations/prove/{topic}-hypothesis-{date}.md
Emit: "STAGE 1 COMPLETE: [path]"

STAGE 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 — WEB SEARCH

Entry: STAGE 1 COMPLETE fired.

Gather minimum 3 external sources. Per source:
- Cite (URL or reference).
- Summarize in one sentence.
- Displacement check: does this advance the case for displacing {status_quo_comparator}
  with {topic}? Yes / No / Inconclusive
- If evidence is thin: note THIN: [area] — [gap] at point of discovery. Do not defer.

Write: simulations/prove/{topic}-websearch-{date}.md
Emit: "STAGE 2 COMPLETE: [path]"

STAGE 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 — INTELLIGENCE

Entry: STAGE 2 COMPLETE fired.

Search internal sources (simulations/, specs, artifacts). Per finding:
- Exact file path.
- Relevant passage or summary.
- Displacement check: does this internal evidence support or undermine {topic}
  displacing {status_quo_comparator}? Yes / No / Inconclusive
- If evidence is thin: note THIN: [area] — [gap] at point of discovery. Do not defer.

Write: simulations/prove/{topic}-intelligence-{date}.md
Emit: "STAGE 3 COMPLETE: [path]"

STAGE 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 — ANALYSIS

Entry: STAGE 3 COMPLETE fired.

Analyze patterns across Stage 2 and Stage 3 evidence.
Distinguish causation from correlation.
Displacement verdict: considering all evidence, does {topic} make a credible case for
displacing {status_quo_comparator}? State Yes / No / Pending and explain in 1-2 sentences.

Write: simulations/prove/{topic}-analysis-{date}.md
Emit: "STAGE 4 COMPLETE: [path]"

STAGE 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 — SYNTHESIS

Entry: STAGE 4 COMPLETE fired.

### Write A — Claim-Evidence Map

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED — and why.
For each major claim in the hypothesis:
- State the claim.
- Cite supporting evidence (stage + source).
- If the claim was THIN-flagged in Stages 2 or 3: name the source stage, the weakened
  claim, and your adjusted confidence.
State the incumbent's residual strength: what does {status_quo_comparator} still do better?
State the primary adoption risk as the most significant remaining incumbent advantage.

Write A: simulations/prove/{topic}-synthesis-{date}.md
Confirm Write A.

### Write B — Readiness Signal

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

Write B: simulations/prove/{topic}-handoff-{date}.md
Confirm Write B.
