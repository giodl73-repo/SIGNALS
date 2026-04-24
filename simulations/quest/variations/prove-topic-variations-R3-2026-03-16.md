Now I have all context needed. R1+R2 explored: lifecycle gates, output format tables, phrasing register, inertia framing, minimalism, exit-signal chaining, role sequence, two-write synthesis. R2 hit 100 on 4/5 variants. R3 needs new axes that can produce new excellence signals or confirm the golden form.

---

```markdown
---
skill: quest-variate
skill_target: prove-topic
round: R3
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [compact_canonical_repair, stage_io_contracts, artifact_manifest_first, imperative_checklist]
  combined: [V-05 (io_contracts + two_write_synthesis)]
r2_scores:
  V-01: 97.5  # minimalism -- C-10 PARTIAL (prose block, no signal)
  V-02: 100   # exit-signal framing
  V-03: 100   # role sequence
  V-04: 100   # two-write synthesis
  V-05: 100   # minimalism + exit-signal + two-write
r2_excellence_signals:
  - "Exit-signal chain satisfies C-10 without GATE headers"
  - "Two-write synthesis makes C-09 structural by construction"
  - "Role-sequence satisfies C-02/C-07 by architecture"
r3_context: >
  R2 reached rubric v14 ceiling with four 100/100 variations across three structurally
  distinct forms (exit-signal, role-sequence, two-write). R3 goals:
  (1) Repair V-01 minimalism to 100/100 with minimal change
  (2) Test two structurally novel forms (I/O contracts, artifact manifest) not explored
      in R1 or R2 -- do they produce new excellence signals or rubric gaps?
  (3) Test checklist form for action-atomic C-03/C-05 compliance
  (4) Confirm integration candidate with I/O contracts + two-write synthesis
---

# prove-topic -- Variate Round 3 (Rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-10 aspirational)
**Date**: 2026-03-16
**Round**: 3

---

## Context: what informed this round

Round 1 and Round 2 explored seven single-axis variations plus two integration candidates:

| Round | Var | Axis                    | Score  | Key finding                                    |
|-------|-----|-------------------------|--------|------------------------------------------------|
| R1    | V-01| Lifecycle emphasis      | 100    | GATE blocks + chained emits; both asp. pass    |
| R1    | V-02| Output format           | 97     | Path table helps C-05; C-10 partial            |
| R1    | V-03| Phrasing register       | 93     | Soft tone weakened C-06/C-10                   |
| R1    | V-04| Inertia framing         | 97     | Strong C-02/C-08; C-10 partial                 |
| R1    | V-05| Combined (3 axes)       | 100    | First integration candidate                    |
| R2    | V-01| Minimalism              | 97.5   | C-10 PARTIAL -- prose abort, no signal         |
| R2    | V-02| Exit-signal framing     | 100    | Two-signal chain: new structural block form    |
| R2    | V-03| Role sequence           | 100    | Two-layer block by architecture                |
| R2    | V-04| Two-write synthesis     | 100    | C-09 by construction                           |
| R2    | V-05| Mini+exit-signal+2write | 100    | R2 integration candidate                       |

Round 3 probes four new axes plus one new integration:

| Var  | Axis                             | Primary target criteria                                   |
|------|----------------------------------|-----------------------------------------------------------|
| V-01 | Compact canonical repair         | C-10 (close R2 V-01 gap), C-01, C-03 (smallest 100/100)  |
| V-02 | Stage I/O contracts              | C-02, C-03, C-05, C-06, C-10 (data-dependency form)      |
| V-03 | Artifact manifest first          | C-05, C-07 (front-loaded path contract)                   |
| V-04 | Imperative checklist             | C-01, C-03, C-05 (action-atomic form)                     |
| V-05 | I/O contracts + two-write synth. | All 10 criteria -- integration candidate                  |

**Artifact paths** (all variations):

| Stage | Signal              | Path                                                                          |
|-------|---------------------|-------------------------------------------------------------------------------|
| 1     | prove-hypothesis    | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`       |
| 2     | prove-websearch     | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`         |
| 3     | prove-intelligence  | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`   |
| 4     | prove-analysis      | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`           |
| 5     | prove-synthesize    | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`       |

---

## V-01 -- Compact Canonical Repair

**Axis**: Compact canonical repair
**Hypothesis**: R2 V-01 (minimalism) scored 97.5/100 because its SETUP abort was
functional prose ("stop and emit... Do not proceed") without a named two-step signal
chain. Adding exactly two sentences to SETUP -- "SCOUT READY cannot fire without a
found file" and "Stage 1 cannot begin until SCOUT READY fires" -- closes the C-10 gap
while preserving V-01's minimal style. If this repair reaches 100/100, minimalist prose
+ two-signal chain is the smallest prompt form that satisfies all 10 v14 criteria, and
any structural machinery added in other variations is a matter of style, not necessity.

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

Before Stage 1: locate the scout artifact at `simulations/scout/{topic}-scout-*.md`.
SCOUT READY cannot fire without a found file. If no file is found, stop and emit:
"No scout artifact for {topic} -- run a scout skill first."
Do not proceed without a named scout artifact. Read the file before forming the
hypothesis. Stage 1 cannot begin until SCOUT READY fires.

Emit: SCOUT READY. scout_source = simulations/scout/{topic}-scout-{date}.md

---

Stage 1 -- Hypothesis

Frame a falsifiable claim for {topic} grounded in the scout artifact. Cite the scout
artifact path in the body. Include `scout_source: simulations/scout/{topic}-scout-{date}.md`
in the frontmatter.

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

Stage 2 -- Web search

Gather external evidence. Assess each source. If evidence is thin or absent in any area,
note it at the point of discovery -- do not defer to synthesis:
  THIN: [area] -- [gap]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

Stage 3 -- Intelligence

Search internal sources -- existing signal artifacts and related topic runs -- for evidence
relevant to the hypothesis. Note thin or absent evidence inline when found:
  THIN: [area] -- [gap]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

Stage 4 -- Analysis

Aggregate all THIN flags from Stages 2 and 3. Map each gap to the specific hypothesis
claim it weakens. Assess the overall evidence case.

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

## V-02 -- Stage I/O Contracts

**Axis**: Stage I/O contracts
**Hypothesis**: Formalizing each stage as an explicit I/O contract -- four labeled
sub-sections per stage: INPUT (what this stage receives), PROCESS (what it does),
OUTPUT (what it writes with full path), EMIT (what signal it fires forward) -- makes
C-01, C-02, C-03, C-05, C-06, and C-10 pass by construction. The INPUT section names
the required predecessor artifact or signal; a stage that reads its INPUT sub-section
cannot skip its dependency check. The OUTPUT sub-section carries the full artifact path
by definition. This differs from exit-signal framing (R2 V-02) in that it is a
data-dependency declaration, not a sequence-lock declaration -- the model sees what data
flows in and out of each stage, not just which locks must clear.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages. Each stage has an
explicit I/O contract: INPUT declares what it requires; OUTPUT declares what it
produces; EMIT declares what it signals forward. No stage begins without its INPUT
confirmed.

---

## SETUP

INPUT:
  - {topic} parameter

PROCESS:
  - Glob: simulations/scout/{topic}-scout-*.md
  - If absent: halt. Emit "No scout artifact for {topic} -- run scout first."
    SCOUT LOADED cannot fire without a found file.
  - Read the found file. Set scout_source = full path of found file.

OUTPUT:
  (no artifact written at setup)

EMIT:
  SCOUT LOADED. scout_source = simulations/scout/{topic}-scout-{date}.md

Stage 1 cannot begin until SCOUT LOADED is emitted.

---

## STAGE 1 -- HYPOTHESIS

INPUT:
  - SCOUT LOADED confirmed. If not confirmed: halt. Do not begin Stage 1.
  - scout_source (from SETUP emit)

PROCESS:
  - Read scout_source.
  - Frame the central falsifiable claim for {topic}, grounded in the scout findings.
  - Include scout_source in artifact frontmatter and body.

OUTPUT:
  Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Required frontmatter field:
    scout_source: simulations/scout/{topic}-scout-{date}.md

EMIT:
  HYPOTHESIS WRITTEN. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Stage 2 cannot begin until HYPOTHESIS WRITTEN is emitted.

---

## STAGE 2 -- WEBSEARCH

INPUT:
  - HYPOTHESIS WRITTEN confirmed. If not confirmed: halt.
  - The hypothesis claim (from Stage 1 OUTPUT)

PROCESS:
  - Gather external evidence for the hypothesis. Assess each source.
  - Flag thin or absent evidence at point of discovery -- do not defer:
      THIN: [area] -- [gap]

OUTPUT:
  Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

EMIT:
  WEBSEARCH WRITTEN. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Stage 3 cannot begin until WEBSEARCH WRITTEN is emitted.

---

## STAGE 3 -- INTELLIGENCE

INPUT:
  - WEBSEARCH WRITTEN confirmed. If not confirmed: halt.
  - The hypothesis claim (from Stage 1 OUTPUT)

PROCESS:
  - Search internal sources -- existing signal artifacts and related topic runs --
    for evidence relevant to the hypothesis.
  - Flag thin or absent evidence inline at point of discovery:
      THIN: [area] -- [gap]

OUTPUT:
  Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

EMIT:
  INTELLIGENCE WRITTEN. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Stage 4 cannot begin until INTELLIGENCE WRITTEN is emitted.

---

## STAGE 4 -- ANALYSIS

INPUT:
  - INTELLIGENCE WRITTEN confirmed. If not confirmed: halt.
  - All THIN flags from Stage 2 and Stage 3 artifacts

PROCESS:
  - Aggregate all THIN flags. Map each flag to the specific hypothesis claim it weakens.
  - Assess the overall evidence case: strong / moderate / thin.

OUTPUT:
  Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

EMIT:
  ANALYSIS WRITTEN. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Stage 5 cannot begin until ANALYSIS WRITTEN is emitted.

---

## STAGE 5 -- SYNTHESIZE

INPUT:
  - ANALYSIS WRITTEN confirmed. If not confirmed: halt.
  - All prior stage artifacts (hypothesis, websearch, intelligence, analysis)

PROCESS:
  - Synthesize evidence across all stages.
  - State verdict: supported / partially supported / not supported.
  - For each THIN-flagged claim: name the source stage and state adjusted confidence.
  - Close with: Evidence brief for {topic} is ready for /topic-story.

OUTPUT:
  Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

EMIT:
  CAMPAIGN COMPLETE. Evidence brief for {topic} is ready for /topic-story.
```

---

## V-03 -- Artifact Manifest First

**Axis**: Artifact manifest first
**Hypothesis**: Declaring all five artifacts up front in a CAMPAIGN MANIFEST section --
listing each artifact's full path, required frontmatter fields, and key content
requirement before any stage instruction begins -- satisfies C-05 and C-07 by
construction: the paths and required fields are established once, authoritatively, before
any stage can omit them. Stages are then terse: they reference artifact slots by name
("write ARTIFACT-1"), do the work, and write. The manifest becomes the source of truth
for both the model executing the skill and a reader verifying compliance. This differs
from the path-declaration table in R1 V-02 in that it includes required frontmatter
fields in the manifest, not just paths -- the manifest is a full artifact contract.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages in forward sequence.
One artifact written per stage per the CAMPAIGN MANIFEST below.

---

## CAMPAIGN MANIFEST

All artifact contracts declared before Stage 1. Each stage writes the artifact
declared for its slot. No deviation from declared paths or required fields.

| Slot | Stage               | Full Path                                                                         | Required Frontmatter Fields              | Key Content Requirement                         |
|------|---------------------|-----------------------------------------------------------------------------------|------------------------------------------|-------------------------------------------------|
| A-1  | prove-hypothesis    | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md             | scout_source: (full path of scout file)  | Falsifiable claim grounded in scout artifact    |
| A-2  | prove-websearch     | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md               | (none required beyond standard fields)   | External evidence with THIN flags at discovery  |
| A-3  | prove-intelligence  | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md         | (none required beyond standard fields)   | Internal evidence with THIN flags at discovery  |
| A-4  | prove-analysis      | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md                 | (none required beyond standard fields)   | THIN flag aggregate mapped to hypothesis claims |
| A-5  | prove-synthesize    | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md             | (none required beyond standard fields)   | Verdict + confidence adjustments + story handoff|

---

## SETUP -- Scout Load

Before Stage 1:

1. Glob: simulations/scout/{topic}-scout-*.md
2. If absent: halt. Emit "No scout artifact for {topic} -- run scout first."
   Do not proceed without a named scout artifact.
3. Set scout_source = found file path. Read the file.
4. Record scout_source value for A-1 frontmatter (see CAMPAIGN MANIFEST, Slot A-1).

Scout load must complete before Stage 1 begins.

---

## STAGE 1 -- HYPOTHESIS

Work: Read scout artifact. Frame the central falsifiable claim for {topic} grounded
in the scout findings. Cite scout_source in the artifact body.

Write ARTIFACT A-1: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Required frontmatter field per manifest: scout_source: simulations/scout/{topic}-scout-{date}.md

---

## STAGE 2 -- WEBSEARCH

Precondition: A-1 written.

Work: Gather external evidence. Assess each source against the hypothesis. Flag thin
or absent evidence at point of discovery -- do not defer:
  THIN: [area] -- [gap]

Write ARTIFACT A-2: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 -- INTELLIGENCE

Precondition: A-2 written.

Work: Search internal sources -- existing signal artifacts and related topic runs.
Flag thin or absent evidence inline when found:
  THIN: [area] -- [gap]

Write ARTIFACT A-3: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 -- ANALYSIS

Precondition: A-3 written.

Work: Aggregate all THIN flags from A-2 and A-3. Map each gap to the specific
hypothesis claim it weakens. Assess the overall evidence case.

Write ARTIFACT A-4: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 -- SYNTHESIZE

Precondition: A-4 written.

Work: Synthesize evidence across all stages. State verdict: supported / partially
supported / not supported. For each THIN-flagged claim, state adjusted confidence
naming the source stage and the weakened claim.

Close with this exact statement: Evidence brief for {topic} is ready for /topic-story.

Write ARTIFACT A-5: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-04 -- Imperative Checklist

**Axis**: Imperative checklist
**Hypothesis**: Rendering every action in the skill as a discrete, numbered or bulleted
action item -- with no prose narration between actions -- makes sequential compliance
(C-01, C-03) and per-instruction path citation (C-05) more reliable because each
instruction is atomic and self-contained. A model that reads a bulleted checklist cannot
easily skip a step by folding two steps together in prose. The scout-abort action and
the "STAGE 1 cannot begin" sentinel are both discrete bullets in the checklist, making
C-10 a checklist item the model must check off, not a paragraph it may skim. This differs
from R1 V-01 (lifecycle emphasis) in that GATE blocks are replaced by checklist items;
the structure is flat, not hierarchical.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Complete every action below in the
order listed. Do not proceed to a later action until the current action is complete.

---

## SETUP

- [ ] 1. Glob: `simulations/scout/{topic}-scout-*.md`
- [ ] 2. If no file found: emit "No scout artifact for {topic} -- run scout first." HALT. Do not proceed to action 3.
- [ ] 3. Set scout_source = full path of the found file (most recent if multiple).
- [ ] 4. Read the file at scout_source.
- [ ] 5. Confirm: SCOUT LOADED. Stage 1 cannot begin until action 5 is complete.

---

## STAGE 1 -- HYPOTHESIS

- [ ] 6. Confirm SCOUT LOADED (action 5 complete). If not: HALT.
- [ ] 7. Frame the central falsifiable claim for {topic}, grounded in the scout findings read at action 4.
- [ ] 8. Draft hypothesis artifact body. Cite scout_source path in the body.
- [ ] 9. Include `scout_source: simulations/scout/{topic}-scout-{date}.md` in artifact frontmatter.
- [ ] 10. Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 -- WEBSEARCH

- [ ] 11. Confirm Stage 1 artifact written (action 10 complete). If not: HALT.
- [ ] 12. Search for external evidence relevant to the hypothesis.
- [ ] 13. For each source found: assess strength of evidence.
- [ ] 14. For each area where evidence is thin or absent: emit THIN: [area] -- [gap] at this point. Do not defer.
- [ ] 15. Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 -- INTELLIGENCE

- [ ] 16. Confirm Stage 2 artifact written (action 15 complete). If not: HALT.
- [ ] 17. Search internal sources: existing signal artifacts and related topic runs.
- [ ] 18. For each area where internal evidence is thin or absent: emit THIN: [area] -- [gap] at this point. Do not defer.
- [ ] 19. Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 -- ANALYSIS

- [ ] 20. Confirm Stage 3 artifact written (action 19 complete). If not: HALT.
- [ ] 21. Collect all THIN flags emitted at actions 14 and 18.
- [ ] 22. For each THIN flag: identify the specific hypothesis claim it weakens.
- [ ] 23. Assess the overall evidence case.
- [ ] 24. Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 -- SYNTHESIZE

- [ ] 25. Confirm Stage 4 artifact written (action 24 complete). If not: HALT.
- [ ] 26. Synthesize evidence across all stages.
- [ ] 27. State verdict: supported / partially supported / not supported.
- [ ] 28. For each THIN-flagged claim: name the source action (14 or 18), the weakened hypothesis claim, and the adjusted confidence level.
- [ ] 29. Write this exact closing line in the artifact: "Evidence brief for {topic} is ready for /topic-story."
- [ ] 30. Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-05 -- I/O Contracts + Two-Write Synthesis

**Axis**: Combined (Stage I/O contracts + two-write synthesis)
**Hypothesis**: V-02's I/O contract structure (INPUT / PROCESS / OUTPUT / EMIT per
stage) combined with R2 V-04's two-write synthesis (Write A = claim-evidence map,
Write B = final evidence brief with topic-story handoff) produces a 100/100 score via
a structurally distinct path from R2 V-05 (exit-signal + minimalism + two-write) and
R1 V-01 (GATE blocks). The I/O contract makes C-10 structural via an explicit INPUT
dependency check; the two-write synthesis makes C-09 structural via Write A's per-claim
contract definition; Write B isolates C-04 from C-09 so neither crowds out the other.
A third structurally independent 100/100 form would confirm that the rubric criteria
are well-specified, not dependent on a specific structural pattern.

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
artifacts: a claim-evidence map (Write A) and a final evidence brief (Write B).
Each stage has an explicit I/O contract. No stage begins without its INPUT confirmed.

---

## SETUP

INPUT:
  - {topic} parameter

PROCESS:
  - Glob: simulations/scout/{topic}-scout-*.md
  - If absent: halt. Emit "No scout artifact for {topic} -- run scout first."
    SCOUT LOADED cannot fire without a found file.
  - Read the found file. Set scout_source = full path of found file.

OUTPUT:
  (no artifact written)

EMIT:
  SCOUT LOADED. scout_source = simulations/scout/{topic}-scout-{date}.md

Stage 1 cannot begin until SCOUT LOADED is emitted.

---

## STAGE 1 -- HYPOTHESIS

INPUT:
  - SCOUT LOADED confirmed. If not confirmed: halt.
  - scout_source (path of the scout artifact)

PROCESS:
  - Read scout_source.
  - Frame the central falsifiable claim for {topic}, grounded in the scout findings.
  - Include scout_source in artifact frontmatter and body.

OUTPUT:
  Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Required frontmatter: scout_source: simulations/scout/{topic}-scout-{date}.md

EMIT:
  HYPOTHESIS WRITTEN. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Stage 2 cannot begin until HYPOTHESIS WRITTEN is emitted.

---

## STAGE 2 -- WEBSEARCH

INPUT:
  - HYPOTHESIS WRITTEN confirmed. If not confirmed: halt.
  - Hypothesis claim (from Stage 1 OUTPUT)

PROCESS:
  - Gather external evidence. Assess each source against the hypothesis.
  - Flag thin or absent evidence at point of discovery -- not deferred:
      THIN: [area] -- [gap]

OUTPUT:
  Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

EMIT:
  WEBSEARCH WRITTEN. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Stage 3 cannot begin until WEBSEARCH WRITTEN is emitted.

---

## STAGE 3 -- INTELLIGENCE

INPUT:
  - WEBSEARCH WRITTEN confirmed. If not confirmed: halt.
  - Hypothesis claim (from Stage 1 OUTPUT)

PROCESS:
  - Search internal sources -- existing signal artifacts and related topic runs.
  - Flag thin or absent evidence inline at point of discovery:
      THIN: [area] -- [gap]

OUTPUT:
  Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

EMIT:
  INTELLIGENCE WRITTEN. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Stage 4 cannot begin until INTELLIGENCE WRITTEN is emitted.

---

## STAGE 4 -- ANALYSIS

INPUT:
  - INTELLIGENCE WRITTEN confirmed. If not confirmed: halt.
  - All THIN flags from Stage 2 and Stage 3 artifacts

PROCESS:
  - Aggregate all THIN flags. Map each to the specific hypothesis claim it weakens.
  - Assess overall evidence case: strong / moderate / thin.

OUTPUT:
  Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

EMIT:
  ANALYSIS WRITTEN. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Stage 5 cannot begin until ANALYSIS WRITTEN is emitted.

---

## STAGE 5 -- SYNTHESIZE

INPUT:
  - ANALYSIS WRITTEN confirmed. If not confirmed: halt.
  - All prior stage artifacts (hypothesis, websearch, intelligence, analysis)

PROCESS (Write A first, Write B second -- do not combine):

### Write A -- Claim Evidence Map

For each hypothesis claim:
- State evidence strength: strong / moderate / thin
- If thin: name the source stage (Stage 2 or Stage 3) and the adjusted confidence
  (e.g., "Confidence reduced -- Stage 2 found no peer data for claim X")

OUTPUT Write A:
  Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-draft-{date}.md

### Write B -- Evidence Brief

State verdict: supported / partially supported / not supported.
Reference Write A for claim-level detail.
Close with this exact statement: Evidence brief for {topic} is ready for /topic-story.

OUTPUT Write B:
  Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

EMIT:
  CAMPAIGN COMPLETE. Evidence brief for {topic} is ready for /topic-story.
```
```
