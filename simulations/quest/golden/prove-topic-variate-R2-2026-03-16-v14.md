---
skill: quest-variate
skill_target: prove-topic
round: R2
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [minimalism, exit_signal_framing, role_sequence, two_write_synthesis]
  combined: [V-05 (minimalism + exit_signal + two_write)]
r1_scores:
  V-01: 100  # lifecycle emphasis -- GATE blocks + forward-only sequence
  V-02: 97   # output format -- path-declaration table
  V-03: 93   # phrasing register -- conversational; C-06/C-10 weakened
  V-04: 97   # inertia framing -- status-quo anchor
  V-05: 100  # lifecycle + format + inertia -- full integration
round_context: >
  R1 (v14) showed all 10 criteria are reachable. Five variations pass all or nearly all.
  Criterion C-10 (structural block) is the most discriminating -- informal prose blocked
  V-03 (phrasing register) from full PASS.
  R2 explores: can minimalism reach 100 without formal GATE blocks? Can exit-signal framing
  produce C-10 compliance differently from GATE blocks? Does role-sequence framing satisfy
  C-02/C-07 by construction? Does two-write synthesis satisfy C-09 by architecture?
---

# prove-topic -- Variate Round 2 (Rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-10 aspirational)
**Date**: 2026-03-16
**Round**: 2

---

## Context: what informed this round

Round 1 explored four single-axis variations plus one integration:

| R1 Var | Axis              | Score | Notes                                     |
|--------|-------------------|-------|-------------------------------------------|
| V-01   | Lifecycle emphasis | 100  | GATE blocks + chained emits; both asp. pass |
| V-02   | Output format     | 97    | Path table helps C-05; C-10 partial        |
| V-03   | Phrasing register | 93    | Soft tone weakened C-06/C-10               |
| V-04   | Inertia framing   | 97    | Strong C-02/C-08; C-10 partial             |
| V-05   | All three         | 100   | Combined; rubric ceiling tested            |

Round 2 probes whether simpler structures can also reach 100, and what new patterns emerge.

| Var  | Axis                         | Primary target criteria                         |
|------|------------------------------|-------------------------------------------------|
| V-01 | Minimalism                   | C-01, C-03, C-04, C-05 (can bare-bones pass?)   |
| V-02 | Exit-signal framing          | C-06 (gate structure), C-10 (structural block)  |
| V-03 | Role sequence                | C-02, C-06, C-07 (named role owns scout load)   |
| V-04 | Two-write synthesis          | C-04, C-07, C-09 (handoff separation)           |
| V-05 | Minimalism + exit-signal + two-write | All 10 criteria -- integration candidate |

**Artifact paths** (all variations):

| Stage | Signal              | Path                                                                          |
|-------|---------------------|-------------------------------------------------------------------------------|
| 1     | prove-hypothesis    | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`       |
| 2     | prove-websearch     | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`         |
| 3     | prove-intelligence  | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`   |
| 4     | prove-analysis      | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`           |
| 5     | prove-synthesize    | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`       |

---

## V-01 -- Minimalism

**Axis**: Minimalism
**Hypothesis**: The v14 criteria can all be satisfied by a prompt with no GATE headers, no
tables, no role declarations, and no THIN-flag format templates -- only linear prose
instructions that name the scout artifact, the five stages in order, one write per stage
with a full path, the topic-story handoff statement, and a scout_source frontmatter field.
If it passes, complexity added in other variations is optional. If it fails, the failure
identifies which criteria actually need structural support.

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
file is found, stop and emit: "No scout artifact for {topic} -- run a scout skill first."
Do not proceed without a named scout artifact. Read the file before forming the hypothesis.

---

Stage 1 -- Hypothesis

Frame a falsifiable claim for {topic} grounded in the scout artifact. Cite the scout
artifact path in the body. Include `scout_source: simulations/scout/{topic}-scout-{date}.md`
in the frontmatter. Do not begin this stage without a confirmed scout artifact.

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

Stage 2 -- Web search

Gather external evidence. Assess each source. If evidence is thin or absent in any area,
note it at the point of discovery -- do not defer to synthesis. Write the results.

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

Stage 3 -- Intelligence

Search internal sources -- existing signal artifacts and related topic runs -- for evidence
relevant to the hypothesis. Note thin or absent evidence inline when found.

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

Stage 4 -- Analysis

Aggregate all thin-evidence notes from Stages 2 and 3. Map each gap to the specific
hypothesis claim it weakens. Assess the overall evidence case.

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

Stage 5 -- Synthesis

Synthesize evidence across all stages. State the verdict: supported, partially supported,
or not supported. For any claim with thin evidence, state your adjusted confidence
explicitly, naming the source stage and the weakened claim.

Close with this exact statement: Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-02 -- Exit-Signal Framing

**Axis**: Exit-signal framing
**Hypothesis**: Framing each stage around its exit signal first -- declaring what must be
produced for the stage to close before describing how to produce it -- creates a different
structural enforcement than entry-gate checks. The model commits to an output contract
before it begins working, which may produce tighter C-03 compliance (exactly one artifact
per stage) and make C-06 legible as a completion signal rather than a precondition check.
The scout block's exit signal also provides C-10's structural block more naturally.

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
- If absent: emit "BLOCKED -- no scout artifact for {topic}. Run scout first." Halt.
  SCOUT READY cannot fire without a found file.
- Set scout_source = full path of found file.
- Read the file.
- Emit: SCOUT READY. scout_source = simulations/scout/{topic}-scout-{date}.md

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 -- HYPOTHESIS

Exit signal: HYPOTHESIS WRITTEN

To fire HYPOTHESIS WRITTEN:
- SCOUT READY must have fired. If not: halt.
- Frame the central falsifiable claim, grounded in the scout artifact.
- Include `scout_source` in the frontmatter pointing to the scout artifact path.
- Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
- Emit: HYPOTHESIS WRITTEN -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

STAGE 2 cannot begin until HYPOTHESIS WRITTEN fires.

---

## STAGE 2 -- WEBSEARCH

Exit signal: WEBSEARCH WRITTEN

To fire WEBSEARCH WRITTEN:
- HYPOTHESIS WRITTEN must have fired. If not: halt.
- Gather external evidence. Assess each source against the hypothesis.
- Flag thin or absent evidence at the point of discovery -- not deferred:
    THIN: [area] -- [gap]
- Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
- Emit: WEBSEARCH WRITTEN -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

STAGE 3 cannot begin until WEBSEARCH WRITTEN fires.

---

## STAGE 3 -- INTELLIGENCE

Exit signal: INTELLIGENCE WRITTEN

To fire INTELLIGENCE WRITTEN:
- WEBSEARCH WRITTEN must have fired. If not: halt.
- Search internal sources for evidence relevant to the hypothesis.
- Flag thin or absent evidence inline when found:
    THIN: [area] -- [gap]
- Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
- Emit: INTELLIGENCE WRITTEN -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

STAGE 4 cannot begin until INTELLIGENCE WRITTEN fires.

---

## STAGE 4 -- ANALYSIS

Exit signal: ANALYSIS WRITTEN

To fire ANALYSIS WRITTEN:
- INTELLIGENCE WRITTEN must have fired. If not: halt.
- Aggregate THIN flags from Stages 2 and 3. Map each gap to the hypothesis claim it weakens.
- Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
- Emit: ANALYSIS WRITTEN -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

STAGE 5 cannot begin until ANALYSIS WRITTEN fires.

---

## STAGE 5 -- SYNTHESIZE

Exit signal: CAMPAIGN COMPLETE

To fire CAMPAIGN COMPLETE:
- ANALYSIS WRITTEN must have fired. If not: halt.
- Synthesize evidence across all stages. Verdict: supported / partially supported / not supported.
- For each THIN-flagged claim: name the source stage and adjusted confidence.
- Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
- Emit: CAMPAIGN COMPLETE. Evidence brief for {topic} is ready for /topic-story.
```

---

## V-03 -- Role Sequence

**Axis**: Role sequence
**Hypothesis**: Naming three roles explicitly (SCOUT-LOADER, ANALYST, SYNTHESIZER) with
formal role-transfer handoffs -- where SCOUT-LOADER owns scout loading and must pass
scout_source to ANALYST before Stage 1 opens -- makes C-02 and C-07 satisfied by
construction rather than by instruction. The ANALYST cannot receive scout_source if
SCOUT-LOADER halts, making C-10 structural via role-based blocking rather than a GATE.
C-06 becomes the role-transition boundary rather than a labeled gate.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Three named roles execute in order.
SCOUT-LOADER runs first. ANALYST runs Stages 1-4. SYNTHESIZER runs Stage 5.

---

## ROLES

SCOUT-LOADER:
- Locates and loads the scout artifact before any stage begins.
- Emits scout_source to ANALYST.
- If scout artifact is absent: emit "BLOCKED -- no scout artifact for {topic}. Run scout first."
  Halt. Do not pass control to ANALYST if scout artifact is absent.

ANALYST:
- Receives scout_source from SCOUT-LOADER.
- Cannot begin Stage 1 without scout_source confirmed.
- Carries scout_source into the hypothesis artifact frontmatter.
- Runs Stages 1-4 in strict forward order.

SYNTHESIZER:
- Receives Stage 4 artifact from ANALYST.
- Cannot begin Stage 5 without Stage 4 artifact confirmed written.
- Closes campaign with explicit topic-story handoff.

---

## SCOUT-LOADER -- Run First

Glob: `simulations/scout/{topic}-scout-*.md`

If absent:
  Emit: BLOCKED. No scout artifact for {topic}. Run a scout skill first.
  Halt. ANALYST does not receive control.

Read the found file.
Emit: scout_source = simulations/scout/{topic}-scout-{date}.md
Control passes to ANALYST.

---

## STAGE 1 -- HYPOTHESIS [ANALYST]

ENTRY: scout_source must be confirmed received from SCOUT-LOADER.
If not confirmed: halt. Do not begin Stage 1.

Frame the central falsifiable claim for {topic}. Ground the hypothesis in the scout artifact.

Frontmatter must include:
  scout_source: simulations/scout/{topic}-scout-{date}.md

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 -- WEBSEARCH [ANALYST]

ENTRY: Stage 1 artifact confirmed written.

Gather external evidence against the hypothesis. Flag thin findings at point of discovery:
  THIN: [area] -- [gap]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 -- INTELLIGENCE [ANALYST]

ENTRY: Stage 2 artifact confirmed written.

Search internal signal artifacts and related topic runs for evidence. Flag thin findings:
  THIN: [area] -- [gap]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 -- ANALYSIS [ANALYST]

ENTRY: Stage 3 artifact confirmed written.

Aggregate THIN flags from Stages 2 and 3. Map each gap to the hypothesis claim it weakens.
Assess overall evidence strength.

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Control passes to SYNTHESIZER.

---

## STAGE 5 -- SYNTHESIZE [SYNTHESIZER]

ENTRY: Stage 4 artifact must be confirmed written by ANALYST.
If not confirmed: SYNTHESIZER blocked. Halt.

Synthesize evidence across all stages. Verdict: supported / partially supported / not supported.

For each THIN-flagged claim:
- Name the source stage
- Name the weakened hypothesis claim
- State the adjusted confidence level

Close: Evidence brief for {topic} is ready for /topic-story.

Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-04 -- Two-Write Synthesis

**Axis**: Two-write synthesis
**Hypothesis**: Splitting Stage 5 into two writes -- Write A (claim-evidence map with per-claim
confidence adjustments) and Write B (final evidence brief with verdict and topic-story handoff)
-- satisfies C-09 by construction (Write A must enumerate claims with confidence) and
separates C-04 from C-09 so neither crowds out the other. The two-write structure also
makes the handoff artifact name distinct, making C-04 more legible as a named artifact
rather than a closing line in a combined synthesis.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages. Stage 5 produces two
artifacts: a claim-evidence map and a final evidence brief.

---

## SETUP

Glob: simulations/scout/{topic}-scout-*.md

If absent: halt. Emit "No scout artifact for {topic}. Run a scout skill first." Do not proceed.

Set scout_source = found path. Read file before Stage 1.

---

## STAGE 1 -- HYPOTHESIS

Frame the central falsifiable claim for {topic}. Ground in scout artifact.

Frontmatter:
  scout_source: simulations/scout/{topic}-scout-{date}.md

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 -- WEBSEARCH

Gather external evidence. Flag thin findings at point of discovery:
  THIN: [area] -- [gap]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 -- INTELLIGENCE

Search internal sources for evidence. Flag thin findings at point of discovery:
  THIN: [area] -- [gap]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 -- ANALYSIS

Aggregate THIN flags from Stages 2 and 3. Map each gap to the hypothesis claim it weakens.

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 -- SYNTHESIS (two writes)

### Write A -- Claim Evidence Map

For each hypothesis claim:
- State evidence strength: strong / moderate / thin
- If thin: name source stage and adjusted confidence
  (e.g., "Confidence reduced -- Websearch found no peer data for claim X")
- Reference the specific stage artifact that contains the thin finding

Write A: simulations/prove/prove-synthesize/{topic}-prove-synthesize-draft-{date}.md

### Write B -- Evidence Brief

State verdict: supported / partially supported / not supported.
Reference Write A for claim-level detail.

Close: Evidence brief for {topic} is ready for /topic-story.

Write B: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-05 -- Minimalism + Exit-Signal + Two-Write Synthesis

**Axis**: Combined
**Hypothesis**: Minimalist prose (V-01) + exit-signal chaining (V-02) + two-write synthesis (V-04)
produces a prompt that is both compact and structurally complete across all 10 criteria. The
exit-signal chain handles C-06/C-10 without GATE block headers. The two-write synthesis
handles C-09/C-04 without separate instructions. V-01's prose style prevents bloat. This
combination is the integration candidate for a potential golden output.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages. Stage 5 produces two artifacts.
Each stage has a declared exit signal. No stage begins without the prior stage's exit signal.

---

## SETUP

Exit signal: SCOUT READY

To fire SCOUT READY:
- Glob `simulations/scout/{topic}-scout-*.md`
- If absent: emit "BLOCKED -- no scout artifact for {topic}. Run scout first." Halt.
  SCOUT READY cannot fire without a found file.
- Read file. Set scout_source = found path.
- Emit: SCOUT READY. scout_source = simulations/scout/{topic}-scout-{date}.md

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 -- HYPOTHESIS

Exit signal: HYPOTHESIS WRITTEN

ENTRY: SCOUT READY must have fired. If not: halt.

Frame central falsifiable claim. Ground in scout artifact.
Frontmatter: scout_source: simulations/scout/{topic}-scout-{date}.md

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Emit: HYPOTHESIS WRITTEN

STAGE 2 cannot begin until HYPOTHESIS WRITTEN fires.

---

## STAGE 2 -- WEBSEARCH

Exit signal: WEBSEARCH WRITTEN

ENTRY: HYPOTHESIS WRITTEN must have fired. If not: halt.

Gather external evidence. Flag thin findings at point of discovery:
  THIN: [area] -- [gap]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Emit: WEBSEARCH WRITTEN

STAGE 3 cannot begin until WEBSEARCH WRITTEN fires.

---

## STAGE 3 -- INTELLIGENCE

Exit signal: INTELLIGENCE WRITTEN

ENTRY: WEBSEARCH WRITTEN must have fired. If not: halt.

Search internal sources. Flag thin findings inline:
  THIN: [area] -- [gap]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Emit: INTELLIGENCE WRITTEN

STAGE 4 cannot begin until INTELLIGENCE WRITTEN fires.

---

## STAGE 4 -- ANALYSIS

Exit signal: ANALYSIS WRITTEN

ENTRY: INTELLIGENCE WRITTEN must have fired. If not: halt.

Aggregate THIN flags. Map each gap to hypothesis claim it weakens.

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Emit: ANALYSIS WRITTEN

STAGE 5 cannot begin until ANALYSIS WRITTEN fires.

---

## STAGE 5 -- SYNTHESIS

Exit signal: CAMPAIGN COMPLETE

ENTRY: ANALYSIS WRITTEN must have fired. If not: halt.

### Write A -- Claim Evidence Map

For each hypothesis claim: state evidence strength. If thin: name source stage and adjusted confidence.

Write A: simulations/prove/prove-synthesize/{topic}-prove-synthesize-draft-{date}.md

### Write B -- Evidence Brief

State verdict: supported / partially supported / not supported.
Reference Write A for claim-level detail.
Close: Evidence brief for {topic} is ready for /topic-story.

Write B: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Emit: CAMPAIGN COMPLETE
```
