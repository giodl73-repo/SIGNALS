I have the full context. Round 1 (V-01 through V-05) covered: lifecycle emphasis, output format (path-declaration table), phrasing register, inertia framing, and a combined integration. Round 2 should explore fresh axes: minimalism, exit-signal framing, role sequence, and two-write synthesis.

Generating Round 2 variations now.

---

# prove-topic — Variate Round 2 (Rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-10 aspirational)
**Date**: 2026-03-16
**Round**: 2

---

## Context: what informed this round

Round 1 explored four single-axis variations plus one integration: lifecycle emphasis (GATE blocks), output format (path-declaration table), phrasing register (conversational), inertia framing (status-quo threading), and V-05 combining all three structural axes.

Round 2 explores axes that Round 1 left untouched:

| Var  | Axis                         | Primary target criteria                         |
|------|------------------------------|-------------------------------------------------|
| V-01 | Minimalism                   | C-01, C-03, C-04, C-05 (can bare-bones pass?)   |
| V-02 | Exit-signal framing          | C-06 (gate structure), C-10 (structural block)  |
| V-03 | Role sequence                | C-02, C-06, C-07 (named role owns scout load)   |
| V-04 | Two-write synthesis          | C-04, C-07, C-09 (handoff separation)           |
| V-05 | Minimalism + exit-signal + two-write | All 10 criteria — integration candidate |

**Artifact paths** (all variations):

| Stage | Signal              | Path                                                                          |
|-------|---------------------|-------------------------------------------------------------------------------|
| 1     | prove-hypothesis    | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`       |
| 2     | prove-websearch     | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`         |
| 3     | prove-intelligence  | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`   |
| 4     | prove-analysis      | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`           |
| 5     | prove-synthesize    | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`       |

---

## V-01 — Minimalism

**Axis**: Minimalism
**Hypothesis**: The v14 criteria can all be satisfied by a prompt with no GATE headers, no tables, no role declarations, and no THIN-flag format templates — only linear prose instructions that name the scout artifact, the five stages in order, one write per stage with a full path, the topic-story handoff statement, and a scout_source frontmatter field. If it passes, complexity added in other variations is optional. If it fails, the failure identifies which criteria actually need structural support.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}.

Before Stage 1: locate the scout artifact at `simulations/scout/{topic}-scout-*.md`. If no
file is found, stop and emit: "No scout artifact for {topic} — run a scout skill first."
Do not proceed without a named scout artifact. Read the file before forming the hypothesis.

---

Stage 1 — Hypothesis

Frame a falsifiable claim for {topic} grounded in the scout artifact. Cite the scout
artifact path in the body. Include `scout_source: simulations/scout/{topic}-scout-{date}.md`
in the frontmatter. Do not begin this stage without a confirmed scout artifact.

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

Stage 2 — Web search

Gather external evidence. Assess each source. If evidence is thin or absent in any area,
note it at the point of discovery — do not defer to synthesis. Write the results.

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

Stage 3 — Intelligence

Search internal sources — existing signal artifacts and related topic runs — for evidence
relevant to the hypothesis. Note thin or absent evidence inline when found.

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

Stage 4 — Analysis

Aggregate all thin-evidence notes from Stages 2 and 3. Map each gap to the specific
hypothesis claim it weakens. Assess the overall evidence case.

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

Stage 5 — Synthesis

Synthesize evidence across all stages. State the verdict: supported, partially supported,
or not supported. For any claim with thin evidence, state your adjusted confidence
explicitly, naming the source stage and the weakened claim.

Close with this exact statement: Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-02 — Exit-Signal Framing

**Axis**: Exit-signal framing
**Hypothesis**: Framing each stage around its exit signal first — declaring what must be produced for the stage to close before describing how to produce it — creates a different structural enforcement than entry-gate checks. The model commits to an output contract before it begins working, which may produce tighter C-03 compliance (exactly one artifact per stage, not more or fewer) and make C-06 legible as a completion signal rather than a precondition check. The scout block's exit signal also provides C-10's structural block more naturally than a GATE CHECK.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages in strict forward sequence.
Each stage has a declared exit signal. The exit signal fires when the stage artifact is
written. No stage begins without the prior stage's exit signal confirmed.

---

## SETUP

Exit signal: SCOUT READY

To fire SCOUT READY:
- Glob `simulations/scout/{topic}-scout-*.md`
- If absent: emit "BLOCKED — no scout artifact for {topic}. Run scout first." Halt. SCOUT READY
  cannot fire without a found file.
- Set scout_source = full path of found file.
- Read the file.
- Emit: SCOUT READY. scout_source = simulations/scout/{topic}-scout-{date}.md

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 — HYPOTHESIS

Exit signal: HYPOTHESIS WRITTEN

To fire HYPOTHESIS WRITTEN:
- SCOUT READY must have fired. If not: halt.
- Frame the central falsifiable claim, grounded in the scout artifact.
- Include `scout_source` in the frontmatter pointing to the scout artifact path.
- Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
- Emit: HYPOTHESIS WRITTEN -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

STAGE 2 cannot begin until HYPOTHESIS WRITTEN fires.

---

## STAGE 2 — WEBSEARCH

Exit signal: WEBSEARCH WRITTEN

To fire WEBSEARCH WRITTEN:
- HYPOTHESIS WRITTEN must have fired. If not: halt.
- Gather external evidence. Assess each source against the hypothesis.
- Flag thin or absent evidence at the point of discovery — not deferred:
    THIN: [area] — [gap]
- Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
- Emit: WEBSEARCH WRITTEN -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

STAGE 3 cannot begin until WEBSEARCH WRITTEN fires.

---

## STAGE 3 — INTELLIGENCE

Exit signal: INTELLIGENCE WRITTEN

To fire INTELLIGENCE WRITTEN:
- WEBSEARCH WRITTEN must have fired. If not: halt.
- Search internal sources for evidence relevant to the hypothesis.
- Flag thin or absent evidence inline when found:
    THIN: [area] — [gap]
- Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
- Emit: INTELLIGENCE WRITTEN -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

STAGE 4 cannot begin until INTELLIGENCE WRITTEN fires.

---

## STAGE 4 — ANALYSIS

Exit signal: ANALYSIS WRITTEN

To fire ANALYSIS WRITTEN:
- INTELLIGENCE WRITTEN must have fired. If not: halt.
- Collect all THIN flags from Stages 2–3. Map each to the hypothesis claim it weakens.
  Assess overall evidence strength.
- Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
- Emit: ANALYSIS WRITTEN -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

STAGE 5 cannot begin until ANALYSIS WRITTEN fires.

---

## STAGE 5 — SYNTHESIZE

Exit signal: CAMPAIGN COMPLETE

To fire CAMPAIGN COMPLETE:
- ANALYSIS WRITTEN must have fired. If not: halt.
- Synthesize all evidence. State verdict: supported / partially supported / not supported.
- For each THIN-flagged claim: name the weakened claim, the source stage, and adjusted confidence.
- Close with the explicit statement: Evidence brief for {topic} is ready for /topic-story.
- Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
- Emit: CAMPAIGN COMPLETE.
```

---

## V-03 — Role Sequence

**Axis**: Role sequence
**Hypothesis**: Assigning named roles with a declared execution order before the stages begin — a SCOUT LOADER who must confirm the scout artifact, a HYPOTHESIS ARCHITECT who frames the claim, an EVIDENCE ANALYST who runs Stages 2–4, and a SYNTHESIS AUTHOR who closes Stage 5 — makes criterion ownership explicit before work begins. This may improve C-02 (scout load is a named role's job, not an implicit precondition), C-06 (role sequence is the gate), and C-07 (the hypothesis artifact carries the scout anchor because HYPOTHESIS ARCHITECT's job includes it). The roles run in fixed sequence; a role cannot execute until the prior role confirms handoff.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Full prove evidence campaign for {topic}. Four roles execute in sequence. Roles cannot
start until the prior role confirms handoff. Each role writes one or more stage artifacts.

---

## ROLE REGISTRY

| Order | Role                | Owns                  | Stages     | Handoff field          |
|-------|---------------------|-----------------------|------------|------------------------|
| 1     | SCOUT LOADER        | scout_source          | Setup      | scout_confirmed        |
| 2     | HYPOTHESIS ARCHITECT| hypothesis artifact   | Stage 1    | hypothesis_written     |
| 3     | EVIDENCE ANALYST    | web, intelligence,    | Stages 2–4 | analysis_written       |
|       |                     | analysis artifacts    |            |                        |
| 4     | SYNTHESIS AUTHOR    | synthesis artifact    | Stage 5    | campaign_complete      |

Roles execute in order 1 → 2 → 3 → 4. No role begins until the prior role's handoff
field is confirmed.

---

## ROLE 1 — SCOUT LOADER

Handoff target: scout_confirmed

1. Glob `simulations/scout/{topic}-scout-*.md`.
   - If absent: emit BLOCKED — no scout artifact for {topic}. Campaign halts. scout_confirmed = false.
   - If absent: do not proceed. The remaining roles cannot execute.
2. Set scout_source = full path of found file (most recent if multiple).
3. Read the scout artifact.
4. Confirm: scout_confirmed = true. scout_source = simulations/scout/{topic}-scout-{date}.md

ROLE 2 cannot begin until scout_confirmed = true.

---

## ROLE 2 — HYPOTHESIS ARCHITECT

Precondition: scout_confirmed = true from ROLE 1. If not: halt.
Handoff target: hypothesis_written

Frame the central falsifiable claim for {topic} grounded in the scout artifact. The
hypothesis must cite the scout artifact path in the body. The artifact frontmatter must
include:

  scout_source: simulations/scout/{topic}-scout-{date}.md

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Confirm: hypothesis_written = true.

ROLE 3 cannot begin until hypothesis_written = true.

---

## ROLE 3 — EVIDENCE ANALYST

Precondition: hypothesis_written = true from ROLE 2. If not: halt.
Handoff target: analysis_written

Run three evidence stages in order: web search, intelligence, analysis.
Each stage produces one artifact. Stages run in sequence. Analysis cannot run before
intelligence; intelligence cannot run before web search.

**Stage 2 — Web search**
Gather external evidence. Assess each source. Flag thin or absent evidence immediately:
  THIN: [area] — [gap]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

**Stage 3 — Intelligence**
Search internal sources. Flag thin evidence inline:
  THIN: [area] — [gap]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

**Stage 4 — Analysis**
Aggregate all THIN flags from Stages 2–3. Map each to the hypothesis claim it weakens.
Assess overall evidence strength.

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Confirm: analysis_written = true.

ROLE 4 cannot begin until analysis_written = true.

---

## ROLE 4 — SYNTHESIS AUTHOR

Precondition: analysis_written = true from ROLE 3. If not: halt.
Handoff target: campaign_complete

Synthesize all evidence. State verdict: supported / partially supported / not supported.
For each THIN-flagged claim, name the weakened claim and adjusted confidence:

  Claim: [claim] | Source stage: N | Gap: [gap] | Confidence: Low / Med / High

Close with the explicit statement: Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

Confirm: campaign_complete = true.
```

---

## V-04 — Two-Write Synthesis

**Axis**: Two-write synthesis
**Hypothesis**: Splitting Stage 5 into two artifacts — a synthesis brief (evidence verdict, THIN propagation, adjusted confidence) and a handoff record (structured fields for downstream consumption by /topic-story) — makes C-04 (readiness for topic-story) structurally explicit rather than a closing sentence, strengthens C-07 (the handoff record carries scout_source as a named field, visible to the downstream consumer, not just in the hypothesis artifact frontmatter), and improves C-09 (adjusted confidence appears as a structured field in the handoff record, not prose). The handoff record is the artifact that /topic-story reads; the synthesis brief is the human-readable evidence case.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five evidence stages, six total
artifacts (one per stage for Stages 1–4; two at Stage 5 — synthesis brief and
handoff record). Final output: handoff record ready for /topic-story.

Stages: hypothesis -> websearch -> intelligence -> analysis -> synthesize

---

## SETUP — Scout Artifact

Before Stage 1:

1. Glob `simulations/scout/{topic}-scout-*.md`
2. If absent: halt and emit "BLOCKED — no scout artifact for {topic}. Run scout first."
   Stage 1 cannot begin without a confirmed scout_source.
3. Set scout_source = full path of found file. Read it.
4. Emit: SCOUT CONFIRMED. scout_source = simulations/scout/{topic}-scout-{date}.md

---

## STAGE 1 — HYPOTHESIS

Precondition: SCOUT CONFIRMED emitted with scout_source named.

Frame the falsifiable hypothesis grounded in the scout findings. The artifact must
reference the scout path in the body. Required frontmatter:

  scout_source: simulations/scout/{topic}-scout-{date}.md

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 — WEBSEARCH

Precondition: Stage 1 artifact written.

Gather external evidence. Flag thin or absent evidence at point of discovery:
  THIN: [area] — [gap]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

Precondition: Stage 2 artifact written.

Search internal sources. Flag thin evidence inline:
  THIN: [area] — [gap]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

Precondition: Stage 3 artifact written.

Aggregate THIN flags from Stages 2–3. Map each to the hypothesis claim it weakens.
Assess overall evidence strength.

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIS

Precondition: Stage 4 artifact written.

Two artifacts. Write both before closing the campaign.

**Artifact 5a — Synthesis Brief**

Human-readable evidence case. State the verdict: supported / partially supported /
not supported. For each THIN-flagged claim, state the adjusted confidence and name
the source stage and the weakened claim.

Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

**Artifact 5b — Handoff Record**

Structured fields for /topic-story. Required fields:

  ---
  skill: prove-topic
  topic: {topic}
  date: {date}
  scout_source: simulations/scout/{topic}-scout-{date}.md
  hypothesis_artifact: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  synthesis_artifact: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
  verdict: [supported / partially supported / not supported]
  confidence: [high / medium / low]
  thin_claims:
    - claim: [claim text]
      source_stage: [2 / 3 / 4]
      adjusted_confidence: [low / medium / high]
  ready_for: topic-story
  ---

  Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/prove-topic/{topic}-prove-handoff-{date}.md
```

---

## V-05 — Combined (Minimalism + Exit-Signal Framing + Two-Write Synthesis)

**Axis**: Minimalism + exit-signal framing + two-write synthesis
**Hypothesis**: The most compliant prompt is the least complex one that still satisfies all 10 criteria. Combining the bare-prose structure of V-01 (no tables, no role headers, direct instructions), the exit-signal framing of V-02 (each stage declares its exit before beginning — making forward-only order and structural blocking legible without GATE header noise), and the two-artifact synthesis of V-04 (handoff record as the explicit /topic-story readiness signal) produces a prompt that covers all 10 criteria without the overhead of role tables, GATE headers, or path-declaration tables. The scout block's exit signal is the structural block for C-10. The handoff record frontmatter satisfies C-07 at the downstream boundary. Exit signals enforce C-06 without headers.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five evidence stages in strict
forward order. One artifact per stage for Stages 1–4, two artifacts at Stage 5.
Each stage fires an exit signal when its artifact is written. No stage begins without
the prior exit signal confirmed.

---

Setup — Scout load

Glob `simulations/scout/{topic}-scout-*.md`. If absent: halt and emit "BLOCKED — no
scout artifact for {topic}. Run scout first. SCOUT READY cannot fire." Do not proceed.
Set scout_source = full path of found file. Read it.
Emit: SCOUT READY. scout_source = simulations/scout/{topic}-scout-{date}.md

Stage 1 cannot begin until SCOUT READY fires.

---

Stage 1 — Hypothesis

SCOUT READY must have fired. If not: halt.

Frame the falsifiable hypothesis grounded in the scout findings. Cite scout_source in
the body. Include in frontmatter: `scout_source: simulations/scout/{topic}-scout-{date}.md`

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Emit: HYPOTHESIS WRITTEN -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Stage 2 cannot begin until HYPOTHESIS WRITTEN fires.

---

Stage 2 — Web search

HYPOTHESIS WRITTEN must have fired. If not: halt.

Gather external evidence for the hypothesis. Assess each source. If evidence is thin
or absent in any area, note it at the point of discovery — do not defer:
  THIN: [area] — [gap]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Emit: WEBSEARCH WRITTEN -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Stage 3 cannot begin until WEBSEARCH WRITTEN fires.

---

Stage 3 — Intelligence

WEBSEARCH WRITTEN must have fired. If not: halt.

Search internal sources for evidence relevant to the hypothesis. Note thin or absent
evidence inline when found:
  THIN: [area] — [gap]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Emit: INTELLIGENCE WRITTEN -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Stage 4 cannot begin until INTELLIGENCE WRITTEN fires.

---

Stage 4 — Analysis

INTELLIGENCE WRITTEN must have fired. If not: halt.

Collect all THIN flags from Stages 2–3. Map each to the hypothesis claim it weakens.
Assess the overall evidence case.

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Emit: ANALYSIS WRITTEN -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Stage 5 cannot begin until ANALYSIS WRITTEN fires.

---

Stage 5 — Synthesis (two artifacts)

ANALYSIS WRITTEN must have fired. If not: halt.

Write artifact 5a — synthesis brief:

State the verdict: supported / partially supported / not supported. For each THIN-flagged
claim, name the weakened claim, the source stage, and adjusted confidence.

Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Emit: SYNTHESIS WRITTEN -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

Write artifact 5b — handoff record:

Required frontmatter fields:

  ---
  skill: prove-topic
  topic: {topic}
  date: {date}
  scout_source: simulations/scout/{topic}-scout-{date}.md
  synthesis_artifact: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
  verdict: [supported / partially supported / not supported]
  confidence: [high / medium / low]
  thin_claims:
    - claim: [text]
      source_stage: [2 / 3 / 4]
      adjusted_confidence: [low / medium / high]
  ready_for: topic-story
  ---

  Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/prove-topic/{topic}-prove-handoff-{date}.md
Emit: CAMPAIGN COMPLETE.
```

---

## Round 2 — Variation Summary

| Var  | Axis                              | Key structural choices                                                    | Expected strengths vs R1 |
|------|-----------------------------------|---------------------------------------------------------------------------|--------------------------|
| V-01 | Minimalism                        | No tables, no gate headers, linear prose only                             | Tests bare-minimum compliance; reveals which criteria need structure |
| V-02 | Exit-signal framing               | Each stage declares exit signal before work; prior signal is entry condition | C-06/C-10 via completion contracts vs entry guards |
| V-03 | Role sequence                     | Named roles with execution order; role owns criterion compliance           | C-02 (scout load is a role's job), C-07 (hypothesis architect carries anchor) |
| V-04 | Two-write synthesis               | Stage 5 splits into synthesis brief + handoff record with structured frontmatter | C-04 structurally explicit; C-07 visible to downstream consumer; C-09 in handoff fields |
| V-05 | Minimalism + exit-signal + 2-write | Prose instructions + exit signals + handoff record; no tables, no role headers | All 10 criteria, minimal overhead; integration candidate |

**Axes not yet explored** (candidates for Round 3):
- Depth parameter branching (`quick` vs `standard` vs `deep` affecting stage rigor)
- Inline verdict scoring (numeric confidence scale, not Low/Med/High)
- Adversarial lock: explicit counter-hypothesis section that must be falsified before synthesis verdict fires
