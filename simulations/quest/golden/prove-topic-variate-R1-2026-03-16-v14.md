# prove-topic — Variate Round 1 (Rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-10 aspirational)
**Date**: 2026-03-16
**Round**: 1

---

## Context: what informed this round

Rubric v14 is a reset to 10 criteria from the 37-criteria v11. The v14 essentials are
simpler and more focused on the basics: 5 stages in sequence, scout artifact named before
hypothesis, one write per stage, synthesis names topic-story, full artifact paths on every
write. This round generates the first 5 variations calibrated specifically to v14.

Prior rounds (R1–R14) optimized for v11's 37 criteria. Some of that machinery satisfies
v14 criteria as a byproduct — but v14 variations need not carry all of it. The goal is
clean, minimal prompts that pass all 10 v14 criteria without over-engineering.

Variation axes (single-axis for V-01 through V-04; combined for V-05):

| Var  | Axis                         | Primary target criteria                         |
|------|------------------------------|-------------------------------------------------|
| V-01 | Lifecycle emphasis           | C-06 (gate block), C-10 (structural block)      |
| V-02 | Output format                | C-05 (paths per instruction), C-07 (scout anchor in artifact) |
| V-03 | Phrasing register            | C-01, C-03, C-04 (compliance under soft register) |
| V-04 | Inertia framing              | C-02 (scout grounding), C-08 (gap flagging)     |
| V-05 | Lifecycle + format + inertia | All 10 criteria — integration candidate         |

**Artifact paths** (all variations):

| Stage | Signal              | Path                                                                          |
|-------|---------------------|-------------------------------------------------------------------------------|
| 1     | prove-hypothesis    | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`       |
| 2     | prove-websearch     | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`         |
| 3     | prove-intelligence  | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`   |
| 4     | prove-analysis      | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`           |
| 5     | prove-synthesize    | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`       |

---

## V-01 — Lifecycle Emphasis

**Axis**: Lifecycle emphasis
**Hypothesis**: Making stage gates explicit and blocking structures visible at each
boundary — GATE checks before each stage, BLOCKED emits when preconditions fail —
satisfies C-06 and C-10 while keeping everything else minimal. A model that sees a GATE
check before Stage 1 cannot enter the hypothesis stage without clearing the scout
confirmation. This is sufficient for the structural block criterion.

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
forward sequence. One artifact written per stage. Final output: evidence brief
ready for /topic-story.

Stages: hypothesis -> websearch -> intelligence -> analysis -> synthesize

---

## STAGE 0 — SCOUT CHECK

Before any stage begins:

1. Glob: `simulations/scout/{topic}-scout-*.md`
2. If no file found:
   Emit: BLOCKED. No scout artifact for `{topic}`. Run a scout skill first.
   Halt. Do not proceed to Stage 1.
3. Set scout_source = full path of the found file (most recent if multiple).
4. Emit: SCOUT CONFIRMED. scout_source = simulations/scout/{topic}-scout-{date}.md

Stage 1 cannot begin until SCOUT CONFIRMED is emitted.

---

## STAGE 1 — HYPOTHESIS

GATE-1 CHECK:
  [ ] SCOUT CONFIRMED emitted with scout_source named.
  If not: BLOCKED at Stage 1. Scout confirmation required. Halt.

WORK:
Read scout_source. Frame the central testable claim for {topic}. Ground the
hypothesis in the scout findings. Reference scout_source explicitly in the
artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Frontmatter must include:
  scout_source: simulations/scout/{topic}-scout-{date}.md

Emit: GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 — WEBSEARCH

GATE-2 CHECK:
  [ ] GATE-1 CLEARED emitted.
  If not: BLOCKED at Stage 2. Halt.

WORK:
Gather external evidence for the hypothesis. For each source, assess strength of
evidence. If evidence is thin or absent, flag at point of discovery:
  THIN: [area] — [gap found]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

GATE-3 CHECK:
  [ ] GATE-2 CLEARED emitted.
  If not: BLOCKED at Stage 3. Halt.

WORK:
Scan internal sources — existing signal artifacts, related topic runs — for evidence
relevant to the hypothesis. Flag thin or absent evidence at point of discovery:
  THIN: [area] — [gap found]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

GATE-4 CHECK:
  [ ] GATE-3 CLEARED emitted.
  If not: BLOCKED at Stage 4. Halt.

WORK:
Aggregate all THIN flags from Stages 2-3. Map each flag to the specific hypothesis
claim it weakens. Assess the overall evidence case.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIZE

GATE-5 CHECK:
  [ ] GATE-4 CLEARED emitted.
  If not: BLOCKED at Stage 5. Halt.

WORK:
Synthesize all evidence across stages 1-4. State the verdict: supported / partially
supported / not supported. For any THIN-flagged claims, state adjusted confidence.

State: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

Emit: GATE-5 CLEARED. Campaign complete.
```

---

## V-02 — Output Format

**Axis**: Output format
**Hypothesis**: A path-declaration table at the campaign open — listing all five
artifact paths before Stage 1 begins — combined with per-stage write blocks that
echo the declared path, ensures every write instruction carries the full path
(C-05) and makes the scout anchor field visible as a required frontmatter key
in the hypothesis artifact (C-07). Table-first layout reduces path inconsistency.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Full prove evidence campaign for {topic}. Run all five evidence stages in order.
Write one artifact per stage. Deliver a synthesized evidence brief ready for /topic-story.

---

## ARTIFACT PATH DECLARATIONS

All artifact paths declared before Stage 1. Each stage write instruction must echo
the exact path declared here.

| Stage | Artifact name     | Full path                                                                        |
|-------|-------------------|----------------------------------------------------------------------------------|
| 1     | hypothesis        | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md            |
| 2     | websearch         | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md              |
| 3     | intelligence      | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md        |
| 4     | analysis          | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md                |
| 5     | synthesize        | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md            |

---

## SETUP — Scout Artifact

Locate the scout artifact before Stage 1:

1. Glob: `simulations/scout/{topic}-scout-*.md`
2. If absent: halt and emit "No scout artifact for {topic}. Run a scout skill first."
3. Set scout_source = path of the found file.
4. Read the file.

scout_source must be named in Stage 1's frontmatter and body. Stages cannot begin
without a named scout_source.

---

## STAGE 1 — HYPOTHESIS

Precondition: scout_source confirmed from setup above.

Frame the central testable hypothesis for {topic}, grounded in the scout findings.
Cite scout_source in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter fields:

| Field        | Value                                               |
|--------------|-----------------------------------------------------|
| signal       | prove-hypothesis                                    |
| topic        | {topic}                                             |
| date         | {date}                                              |
| scout_source | simulations/scout/{topic}-scout-{date}.md           |

---

## STAGE 2 — WEBSEARCH

Precondition: Stage 1 artifact written.

Gather external evidence for the hypothesis. Assess strength of each source.
Flag evidence gaps immediately when found — do not defer to synthesis:

  THIN: [area] — [specific gap]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

Precondition: Stage 2 artifact written.

Search internal sources (existing signal artifacts, related topics) for evidence
relevant to the hypothesis. Flag thin evidence immediately when found:

  THIN: [area] — [specific gap]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

Precondition: Stage 3 artifact written.

Aggregate THIN flags from Stages 2-3 into a summary table:

| Flag    | Stage | Area | Gap | Hypothesis Claim Weakened |
|---------|-------|------|-----|---------------------------|
| THIN-01 | 2     | ...  | ... | ...                       |

Map each flag to the specific hypothesis claim it undermines. Assess overall
evidence strength.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIZE

Precondition: Stage 4 artifact written.

Synthesize evidence from all prior stages. State verdict. For each THIN-flagged
claim, provide adjusted confidence:

| Claim | Source Stage | Gap | Confidence |
|-------|-------------|-----|------------|
| ...   | ...         | ... | Low/Med/High |

Close with the explicit statement: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-03 — Phrasing Register

**Axis**: Phrasing register
**Hypothesis**: A conversational, descriptive register — "in this stage you'll" rather
than "WORK: Do X", no caps section headers — can still produce all five artifacts with
full paths and scout grounding. If it cannot, the failure reveals that imperative
register is load-bearing for C-03 and C-05 compliance, not just stylistic preference.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

You're running a full prove evidence campaign for {topic}. This means working through
five evidence stages in order — hypothesis, web search, intelligence, analysis, and
synthesis — writing one artifact after each stage. At the end you'll have a complete
evidence brief ready to hand off to /topic-story.

Run the stages in the order shown below. Do not skip or reorder them. Do not write
a single combined artifact at the end — write as you go, one artifact per stage.

---

## Before you start — find the scout artifact

Before forming any hypothesis, locate the scout artifact for this topic:

  simulations/scout/{topic}-scout-*.md

If no scout artifact exists, stop here and let the user know they should run a scout
skill first. Do not proceed without a named scout artifact.

Once you have it, read it. The hypothesis you form in Stage 1 should be grounded in
what the scout found. You'll also need to carry the scout artifact path into the
hypothesis artifact as a named field.

---

## Stage 1 — Hypothesis

Read the scout artifact. Based on what it found, frame the central testable claim for
{topic}. This should be falsifiable — a claim that evidence could either support or
undermine.

Cite the scout artifact path in the artifact body. Include a `scout_source` field in
the frontmatter pointing to the scout artifact path.

When you're done framing the hypothesis, write it to:
  simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## Stage 2 — Web search

Search for external evidence relevant to the hypothesis you just wrote. For each source
you find, assess how strongly it supports or challenges the claim. If evidence is thin
or missing in an area, note it right then — don't save it for the synthesis:

  THIN: [area] — [what's missing]

Write your web search findings to:
  simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## Stage 3 — Intelligence

Search internal sources — existing signal artifacts, prior runs for related topics —
for any evidence relevant to the hypothesis. Same rule as above: if something is thin
or absent, flag it inline:

  THIN: [area] — [what's missing]

Write your internal findings to:
  simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## Stage 4 — Analysis

Now pull together everything from the previous two stages. Collect all the THIN flags
you emitted. Map each one to the specific hypothesis claim it weakens. Assess how
strong the overall evidence case is.

Write the analysis to:
  simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## Stage 5 — Synthesis

With all four stages complete, synthesize the full picture. State clearly whether the
evidence supports the hypothesis, partially supports it, or doesn't support it. For
each claim that had weak evidence (THIN flags), say how confident you are in that
claim given what you found.

Close the synthesis with this explicit statement:
  Evidence brief for {topic} is ready for /topic-story.

Write the synthesis to:
  simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-04 — Inertia Framing

**Axis**: Inertia framing
**Hypothesis**: Opening the campaign by explicitly identifying the status-quo comparator
(the incumbent solution the topic must displace) and threading that comparator through
every stage — including THIN flag format and synthesis verdict — strengthens C-02 (scout
grounding is purposeful, not procedural) and C-08 (evidence gaps are flagged as
displacement weaknesses, not generic gaps). The inertia frame gives every stage a
concrete target to build evidence against.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. The purpose is to build a displacement
case: does {topic} provide a reason to move away from the status quo? Five stages in
order. One artifact per stage. Final output: evidence brief ready for /topic-story.

---

## CAMPAIGN OPEN — Identify the Incumbent

Before Stage 1:

1. Locate the scout artifact: `simulations/scout/{topic}-scout-*.md`
   - If absent: halt. Emit "BLOCKED — no scout artifact for {topic}. Run scout first."
2. Read the scout artifact.
3. Identify:
   - status_quo: the specific incumbent solution {topic} must displace. Concrete name —
     not "existing tools" or "current approach". If the scout artifact does not name it
     explicitly, infer from the signals and flag the inference.
   - inertia: the specific friction point that makes displacement non-trivial (e.g.,
     "workflow dependency on existing format", "migration cost", "team familiarity").

Emit:
  CAMPAIGN OPEN.
  scout: simulations/scout/{topic}-scout-{date}.md
  status_quo: [named incumbent]
  inertia: [named friction point]

No stage begins until CAMPAIGN OPEN is emitted with all three fields named.

---

## STAGE 1 — HYPOTHESIS

Frame the hypothesis as a displacement claim:
  "{topic} displaces {status_quo} because [mechanism], despite {inertia}."

Ground the claim in the scout artifact. Reference the scout path in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: simulations/scout/{topic}-scout-{date}.md
  status_quo:   [named incumbent]
  inertia:      [named friction point]

---

## STAGE 2 — WEBSEARCH

Gather external evidence for the displacement hypothesis. For each source, assess
how well it supports the case that {topic} outperforms {status_quo}. Flag missing or
weak evidence at point of discovery — name the displacement claim it weakens:

  THIN: [area] — [gap] — weakens: "{specific claim vs {status_quo}}"

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

Search internal sources for evidence relevant to the displacement hypothesis. Flag
thin evidence inline, naming the displacement claim weakened:

  THIN: [area] — [gap] — weakens: "{specific claim vs {status_quo}}"

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

Aggregate all THIN flags from Stages 2-3. Final column names the displacement claim
weakened against {status_quo}:

| Flag    | Stage | Area | Gap | Displacement Claim Weakened                  |
|---------|-------|------|-----|----------------------------------------------|
| THIN-01 | 2     | ...  | ... | vs {status_quo}: [specific claim]            |

Map each flag to the specific displacement claim. Assess whether the overall
displacement case holds despite {inertia}.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIZE

State the displacement verdict: proven / partially proven / not proven.

For each THIN-flagged displacement claim, name the weakened claim and assign
adjusted confidence:

| Displacement Claim (vs {status_quo}) | Gap Source | Adjusted Confidence |
|--------------------------------------|------------|---------------------|
| ...                                  | Stage N    | Low / Med / High    |

If zero THIN flags: state "no evidence gaps — full confidence in displacement case."

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-05 — Combined (Lifecycle + Format + Inertia)

**Axis**: Lifecycle emphasis + Output format + Inertia framing
**Hypothesis**: Combining the structural gate machinery of V-01 (blocking GATE checks
before each stage, C-06/C-10) with the table-first path declarations of V-02 (path
table at campaign open, per-stage frontmatter tables, C-05/C-07) and the incumbent
framing of V-04 (status_quo named at CAMPAIGN OPEN, THIN flags reference displacement
claims, C-02/C-08) produces a prompt that satisfies all 10 v14 criteria without
carrying the 37-criteria complexity of the v11 architecture.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages in strict forward
sequence. One artifact written per stage. Final output: evidence brief ready for
/topic-story.

Stages: hypothesis -> websearch -> intelligence -> analysis -> synthesize

---

## ARTIFACT PATHS (declared once; each write instruction echoes the matching path)

| Stage | Signal             | Full path                                                                      |
|-------|--------------------|--------------------------------------------------------------------------------|
| 1     | prove-hypothesis   | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md          |
| 2     | prove-websearch    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md            |
| 3     | prove-intelligence | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md      |
| 4     | prove-analysis     | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md              |
| 5     | prove-synthesize   | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md          |

---

## CAMPAIGN OPEN

Before Stage 1:

1. Glob `simulations/scout/{topic}-scout-*.md`.
   - If absent: emit BLOCKED. No scout artifact for `{topic}`. Run scout first. Halt.
2. Set scout_source = full path of found file (most recent if multiple).
3. Read the file. Extract:
   - status_quo: the named incumbent solution {topic} must displace. Concrete name.
   - inertia: the named friction point making displacement non-trivial. Concrete.
   If the scout artifact does not make these explicit, infer and flag the inference.

Emit:
  CAMPAIGN OPEN.
  scout_source: simulations/scout/{topic}-scout-{date}.md
  status_quo:   [named incumbent]
  inertia:      [named friction point]

Stage 1 entry is blocked until CAMPAIGN OPEN is emitted with all three fields present.

---

## STAGE 1 — HYPOTHESIS

GATE CHECK:
  [ ] CAMPAIGN OPEN emitted.
  [ ] scout_source, status_quo, inertia all named.
  If not: BLOCKED at Stage 1. Halt.

Frame the hypothesis as a displacement claim:
  "{topic} displaces {status_quo} because [mechanism], despite {inertia}."

Ground the claim in the scout artifact. Cite scout_source in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:

| Field        | Value                                             |
|--------------|---------------------------------------------------|
| signal       | prove-hypothesis                                  |
| topic        | {topic}                                           |
| date         | {date}                                            |
| scout_source | simulations/scout/{topic}-scout-{date}.md         |
| status_quo   | [named incumbent]                                 |
| inertia      | [named friction point]                            |

Emit: GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 — WEBSEARCH

GATE CHECK:
  [ ] GATE-1 CLEARED emitted.
  If not: BLOCKED at Stage 2. Halt.

Gather external evidence for the displacement hypothesis. Assess each source.
Flag thin or absent evidence at point of discovery — name the displacement claim weakened:

  THIN: [area] — [gap] — weakens: [specific claim vs {status_quo}]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

GATE CHECK:
  [ ] GATE-2 CLEARED emitted.
  If not: BLOCKED at Stage 3. Halt.

Search internal sources — existing signal artifacts, related topics — for evidence
relevant to the displacement hypothesis. Flag thin evidence inline:

  THIN: [area] — [gap] — weakens: [specific claim vs {status_quo}]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

GATE CHECK:
  [ ] GATE-3 CLEARED emitted.
  If not: BLOCKED at Stage 4. Halt.

Aggregate all THIN flags from Stages 2-3:

| Flag    | Stage | Area | Gap | Displacement Claim Weakened (vs {status_quo})  |
|---------|-------|------|-----|------------------------------------------------|
| THIN-01 | 2     | ...  | ... | ...                                            |

If no THIN flags: one row — "no THIN findings — — —"

Map each flag to the specific displacement claim. Assess whether the overall
displacement case holds despite {inertia}.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIZE

GATE CHECK:
  [ ] GATE-4 CLEARED emitted.
  If not: BLOCKED at Stage 5. Halt.

Synthesize all evidence. State displacement verdict: proven / partially proven / not proven.

For each THIN-flagged claim, provide adjusted confidence:

| Displacement Claim (vs {status_quo}) | Source Stage | Gap | Adjusted Confidence |
|--------------------------------------|-------------|-----|---------------------|
| ...                                  | Stage N     | ... | Low / Med / High    |

If zero THIN flags: "no evidence gaps — full confidence in displacement case."

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

Emit: GATE-5 CLEARED. Campaign complete.
```
