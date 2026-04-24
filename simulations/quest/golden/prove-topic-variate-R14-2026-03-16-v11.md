# prove-topic — Variate Round 14 (Rubric v11)

**Skill**: prove-topic
**Rubric**: v11 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-37 aspirational)
**Date**: 2026-03-16
**Round**: 14

---

## Context: what informed this round

R13 V-04 (lifecycle + inertia combined) is the R13 champion. It covers C-01 through C-34:
- CAMPAIGN OPEN extracts status_quo_comparator + inertia_vulnerability (C-32)
- THIN flags name displacement claims against incumbent (C-33)
- Displacement fields in every stage YAML (C-34)
- Full lifecycle machinery: named completion checklists (C-15), gate clearance strings
  with artifact paths (C-19/C-22), PATH CHAIN VERIFICATION tables (C-30), dual-output
  trigger inside checklist (C-31), stages_completed accumulation from Stage 1 (C-21),
  checklist drives both channels (C-25/C-29), cross-channel sync (C-23),
  interrupted campaign recovery (C-24), consistent naming root (C-27),
  three-way path chain (C-28), Stage N+1 entry cites Stage N checklist (C-26)

Rubric v11 adds three new criteria:

| New | Description |
|-----|-------------|
| C-35 | Recovery procedure names `status_quo_comparator` + `inertia_vulnerability` as YAML recovery targets |
| C-36 | Stage N+1 entry conditions enumerate each individual Stage N checklist output by name |
| C-37 | Each stage defined as a machine-readable ROLE CARD declaration table |

R14 variation axes:

| Var | Axis | Primary new criteria |
|-----|------|---------------------|
| V-01 | Lifecycle emphasis | C-36 (enumerated entry conditions) |
| V-02 | Output format | C-37 (ROLE CARD declaration tables) |
| V-03 | Role sequence | C-35 (displacement field recovery in recovery procedure) |
| V-04 | Lifecycle + Inertia (combined) | C-35 + C-36 |
| V-05 | All four axes | C-35 + C-36 + C-37 + inertia framing |

**Artifact paths** (all variations):

| Stage | Signal | Path |
|-------|--------|------|
| 1 | prove-hypothesis | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` |
| 2 | prove-websearch | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` |
| 3 | prove-intelligence | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |
| 4 | prove-analysis | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` |
| 5 | prove-synthesize | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md` |

---

## V-01 — Lifecycle Emphasis (C-36: Enumerated Entry Conditions)

**Axis**: Lifecycle emphasis
**Hypothesis**: Naming each individual Stage N checklist output explicitly at Stage N+1 entry
conditions — rather than a holistic "checklist satisfied" reference — creates verifiable
by-name handoffs at every stage boundary while leaving ROLE CARD format and recovery
procedure unchanged. This satisfies C-36 without structural overhead from C-37.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Orchestrates five stages in strict
forward sequence: prove-hypothesis -> prove-websearch -> prove-intelligence ->
prove-analysis -> prove-synthesize. Reads prior scout signals to ground the hypothesis.
Writes one artifact per stage as it executes. Final output: a synthesized evidence brief
ready for /topic-story.

---

## INTERRUPTED CAMPAIGN RECOVERY

If resuming a campaign that was interrupted:

1. Find the most recent artifact in `simulations/prove/` for this topic.
2. Read its `stages_completed` YAML field to identify which stages finished.
3. Check which gate clearance strings are absent from context to identify the next
   required stage.
4. Resume from the first stage whose identifier is absent from `stages_completed`.
5. Emit: RESUMING CAMPAIGN. stages_completed = [...]. Next stage: Stage N — [name].
6. Apply normal entry conditions from that stage forward.

This procedure applies before Stage 0 and at any point a prior partial run is detected.

---

## STAGE 0 — CAMPAIGN OPEN

Before any stage begins:

1. Locate: `simulations/scout/{topic}-scout-*.md` — most recent by date if multiple.
   - If none found: emit BLOCKED. No scout artifact for topic `{topic}`. Run a scout
     skill first. Halt.
2. Set scout_anchor = full path of found file.
3. Read the artifact. Extract two named fields:
   - status_quo_comparator — the incumbent solution this topic must displace. Concrete
     name (e.g., "manual spreadsheet tracking", "ad-hoc CLI tooling"). Not abstract.
   - inertia_vulnerability — the specific resistance point making displacement non-trivial
     (e.g., "team familiarity with current tooling", "migration cost"). Concrete.
   If the scout artifact does not make these explicit, infer from signals and flag the
   inference.

Emit:

  CAMPAIGN OPEN.
  scout_anchor:            simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator:   [named incumbent]
  inertia_vulnerability:   [named resistance point]

No stage work begins until CAMPAIGN OPEN is emitted with both fields named.
All THIN flags and synthesis claims are displacement claims against status_quo_comparator.

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN emitted.
  [ ] scout_anchor confirmed.
  [ ] status_quo_comparator named.
  [ ] inertia_vulnerability named.
  [ ] (Or: RESUMING CAMPAIGN with stage-1-hypothesis absent from stages_completed.)

WORK: Frame the central testable claim for {topic} as a displacement claim:
"{topic} displaces {status_quo_comparator} because [mechanism], despite
{inertia_vulnerability}." Ground the hypothesis in the scout artifact.
Reference scout_anchor as a cited path in both the artifact body and the
`scout_anchor:` YAML frontmatter field.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-hypothesis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent from CAMPAIGN OPEN]
  inertia_vulnerability: [named resistance point from CAMPAIGN OPEN]
  stages_completed: [stage-1-hypothesis]

STAGE 1 COMPLETION CHECKLIST:
  [ ] 1. Hypothesis stated as a falsifiable displacement claim
  [ ] 2. scout_anchor path cited in artifact body
  [ ] 3. scout_anchor field present in YAML frontmatter
  [ ] 4. status_quo_comparator in YAML frontmatter
  [ ] 5. inertia_vulnerability in YAML frontmatter
  [ ] 6. stages_completed: [stage-1-hypothesis] in YAML frontmatter
  [ ] 7. Artifact written to simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  [ ] 8. When all items above are checked: (1) append stage-1-hypothesis to stages_completed;
         (2) emit GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
         Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 1 -> 2:

  Channel                    | Path
  ---------------------------|--------------------------------------------------------------------
  Write instruction (Stg 1)  | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Gate clearance (GATE-1)    | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Stage 2 entry confirmation | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 — WEBSEARCH

ENTRY CONDITIONS — each Stage 1 checklist output confirmed by name:
  [ ] 1. Stage 1 checklist item 1: hypothesis stated as falsifiable displacement claim — confirmed
  [ ] 2. Stage 1 checklist item 2: scout_anchor cited in artifact body — confirmed
  [ ] 3. Stage 1 checklist item 3: scout_anchor field in YAML frontmatter — confirmed
  [ ] 4. Stage 1 checklist item 4: status_quo_comparator in YAML frontmatter — confirmed
  [ ] 5. Stage 1 checklist item 5: inertia_vulnerability in YAML frontmatter — confirmed
  [ ] 6. Stage 1 checklist item 6: stages_completed: [stage-1-hypothesis] in YAML — confirmed
  [ ] 7. Stage 1 checklist item 7: artifact written — confirmed
  [ ] 8. Stage 1 checklist item 8: GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md — emitted and path confirmed
  [ ] (Or: RESUMING CAMPAIGN with stage-2-websearch absent from stages_completed.)

WORK: Gather external evidence relevant to the displacement hypothesis. Assess each source.
Flag thin or absent evidence immediately at the point of discovery — name the incumbent:

  THIN: [area] — [gap] — weakens displacement claim against {status_quo_comparator}: [specific claim element]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-websearch
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch]

STAGE 2 COMPLETION CHECKLIST:
  [ ] 1. Minimum 3 external sources gathered and assessed
  [ ] 2. All THIN flags emitted inline (not deferred), each naming {status_quo_comparator}
  [ ] 3. scout_anchor carried in YAML frontmatter
  [ ] 4. status_quo_comparator carried in YAML frontmatter
  [ ] 5. inertia_vulnerability carried in YAML frontmatter
  [ ] 6. stages_completed accumulates stage-2-websearch
  [ ] 7. Artifact written to simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  [ ] 8. When all items above are checked: (1) append stage-2-websearch to stages_completed;
         (2) emit GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
         Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 2 -> 3:

  Channel                    | Path
  ---------------------------|-------------------------------------------------------------------
  Write instruction (Stg 2)  | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Gate clearance (GATE-2)    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Stage 3 entry confirmation | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

ENTRY CONDITIONS — each Stage 2 checklist output confirmed by name:
  [ ] 1. Stage 2 checklist item 1: minimum 3 sources gathered — confirmed
  [ ] 2. Stage 2 checklist item 2: all THIN flags naming incumbent emitted inline — confirmed
  [ ] 3. Stage 2 checklist item 3: scout_anchor in YAML — confirmed
  [ ] 4. Stage 2 checklist item 4: status_quo_comparator in YAML — confirmed
  [ ] 5. Stage 2 checklist item 5: inertia_vulnerability in YAML — confirmed
  [ ] 6. Stage 2 checklist item 6: stages_completed accumulates stage-2-websearch — confirmed
  [ ] 7. Stage 2 checklist item 7: artifact written — confirmed
  [ ] 8. Stage 2 checklist item 8: GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md — emitted and path confirmed
  [ ] (Or: RESUMING CAMPAIGN with stage-3-intelligence absent from stages_completed.)

WORK: Scan internal sources — existing signal artifacts, prior runs, related topics —
for evidence relevant to the displacement hypothesis. Flag thin or absent evidence
immediately, naming the incumbent:

  THIN: [area] — [gap] — weakens displacement claim against {status_quo_comparator}: [specific claim element]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-intelligence
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]

STAGE 3 COMPLETION CHECKLIST:
  [ ] 1. Internal sources scanned and assessed
  [ ] 2. All THIN flags emitted inline, each naming {status_quo_comparator}
  [ ] 3. scout_anchor carried in YAML frontmatter
  [ ] 4. status_quo_comparator carried in YAML frontmatter
  [ ] 5. inertia_vulnerability carried in YAML frontmatter
  [ ] 6. stages_completed accumulates stage-3-intelligence
  [ ] 7. Artifact written to simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  [ ] 8. When all items above are checked: (1) append stage-3-intelligence to stages_completed;
         (2) emit GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
         Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 3 -> 4:

  Channel                    | Path
  ----------------------------|------------------------------------------------------------------------
  Write instruction (Stg 3)  | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Gate clearance (GATE-3)    | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Stage 4 entry confirmation | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

ENTRY CONDITIONS — each Stage 3 checklist output confirmed by name:
  [ ] 1. Stage 3 checklist item 1: internal sources scanned — confirmed
  [ ] 2. Stage 3 checklist item 2: all THIN flags naming incumbent emitted inline — confirmed
  [ ] 3. Stage 3 checklist item 3: scout_anchor in YAML — confirmed
  [ ] 4. Stage 3 checklist item 4: status_quo_comparator in YAML — confirmed
  [ ] 5. Stage 3 checklist item 5: inertia_vulnerability in YAML — confirmed
  [ ] 6. Stage 3 checklist item 6: stages_completed accumulates stage-3-intelligence — confirmed
  [ ] 7. Stage 3 checklist item 7: artifact written — confirmed
  [ ] 8. Stage 3 checklist item 8: GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md — emitted and path confirmed
  [ ] (Or: RESUMING CAMPAIGN with stage-4-analysis absent from stages_completed.)

WORK: Two parts separated by GATE-4A.

PART A — Flag Aggregation:
Collect all THIN flags from Stages 2–3 into the aggregation table. The final column
names the displacement claim against status_quo_comparator that is weakened:

  Flag ID | Stage | Area | Evidence Gap | Displacement Claim Weakened (vs. {status_quo_comparator})
  --------|-------|------|--------------|----------------------------------------------------------
  THIN-01 | 2     | ...  | ...          | ...
  THIN-02 | 3     | ...  | ...          | ...

If no THIN flags: one row — no THIN findings — — —

Emit: GATE-4A CLEARED.
Part B cannot begin until GATE-4A CLEARED. is emitted.

PART B — Hypothesis Mapping:
Map each THIN flag to the specific displacement claim it weakens. Assess the overall
case that {topic} outperforms {status_quo_comparator} despite {inertia_vulnerability}.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-analysis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]

STAGE 4 COMPLETION CHECKLIST:
  [ ] 1. GATE-4A emitted (aggregation table complete before mapping begins)
  [ ] 2. Aggregation table final column names displacement claim vs {status_quo_comparator}
  [ ] 3. All THIN flags mapped to displacement claims
  [ ] 4. Data pattern analysis complete
  [ ] 5. scout_anchor carried in YAML frontmatter
  [ ] 6. status_quo_comparator carried in YAML frontmatter
  [ ] 7. inertia_vulnerability carried in YAML frontmatter
  [ ] 8. stages_completed accumulates stage-4-analysis
  [ ] 9. Artifact written to simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  [ ] 10. When all items above are checked: (1) append stage-4-analysis to stages_completed;
          (2) emit GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
          Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 4 -> 5:

  Channel                    | Path
  ---------------------------|----------------------------------------------------------------
  Write instruction (Stg 4)  | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Gate clearance (GATE-4)    | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Stage 5 entry confirmation | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIZE

ENTRY CONDITIONS — each Stage 4 checklist output confirmed by name:
  [ ] 1.  Stage 4 checklist item 1: GATE-4A emitted — confirmed
  [ ] 2.  Stage 4 checklist item 2: aggregation table names displacement claims — confirmed
  [ ] 3.  Stage 4 checklist item 3: all THIN flags mapped to displacement claims — confirmed
  [ ] 4.  Stage 4 checklist item 4: data pattern analysis complete — confirmed
  [ ] 5.  Stage 4 checklist item 5: scout_anchor in YAML — confirmed
  [ ] 6.  Stage 4 checklist item 6: status_quo_comparator in YAML — confirmed
  [ ] 7.  Stage 4 checklist item 7: inertia_vulnerability in YAML — confirmed
  [ ] 8.  Stage 4 checklist item 8: stages_completed accumulates stage-4-analysis — confirmed
  [ ] 9.  Stage 4 checklist item 9: artifact written — confirmed
  [ ] 10. Stage 4 checklist item 10: GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md — emitted and path confirmed
  [ ] (Or: RESUMING CAMPAIGN with stage-5-synthesize absent from stages_completed.)

WORK: Synthesize all evidence. State whether the displacement case is proven, partially
proven, or not proven. For THIN-flagged claims, assign adjusted confidence per weak claim.

CONFIDENCE ADJUSTMENT TABLE — output exactly one named form:

FORM A (one or more THIN flags exist):

  Displacement Claim (vs. {status_quo_comparator}) | Source Stage | Evidence Gap | Adjusted Confidence
  --------------------------------------------------|-------------|--------------|--------------------
  [claim]                                           | Stage N      | [gap]        | [Low / Med / High]

FORM B (zero THIN flags):

  Displacement Claim (vs. {status_quo_comparator}) | Source Stage | Evidence Gap | Adjusted Confidence
  --------------------------------------------------|-------------|--------------|--------------------
  no THIN findings                                  | —            | —            | n/a

State explicitly: This evidence brief is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-synthesize
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence,
                     stage-4-analysis, stage-5-synthesize]

STAGE 5 COMPLETION CHECKLIST:
  [ ] 1. All evidence synthesized
  [ ] 2. Displacement verdict stated (proven / partially proven / not proven)
  [ ] 3. Confidence adjustment table output as FORM A or FORM B (form label above table)
  [ ] 4. Each THIN-flagged claim has adjusted confidence level
  [ ] 5. /topic-story named as explicit next step
  [ ] 6. scout_anchor carried in YAML frontmatter
  [ ] 7. status_quo_comparator carried in YAML frontmatter
  [ ] 8. inertia_vulnerability carried in YAML frontmatter
  [ ] 9. All 5 stage identifiers present in stages_completed
  [ ] 10. Artifact written to simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
  [ ] 11. When all items above are checked: emit GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
          Campaign complete.
```

---

## V-02 — Output Format (C-37: ROLE CARD Declaration Tables)

**Axis**: Output format
**Hypothesis**: Defining each stage as a machine-readable ROLE CARD declaration table —
a structured schema block co-locating role number, task, artifact, path template,
stages_completed identifier, entry conditions summary, and exit gate in one scannable
structure — makes all stage-level fields statically parseable without executing the stage.
C-37 is satisfied while prior lifecycle machinery is preserved in the execution sections.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Five evidence stages in strict forward
sequence, each defined by a ROLE CARD declaration then executed below. Reads prior scout
signals to ground the hypothesis. Writes one artifact per stage. Final output: synthesized
evidence brief ready for /topic-story.

---

## INTERRUPTED CAMPAIGN RECOVERY

If resuming a campaign that was interrupted:

1. Find the most recent artifact in `simulations/prove/` for this topic.
2. Read its `stages_completed` YAML field to identify which stages finished.
3. Check which gate clearance strings are absent from context to identify the next
   required stage.
4. Resume from the first stage whose identifier is absent from `stages_completed`.
5. Emit: RESUMING CAMPAIGN. stages_completed = [...]. Next stage: Stage N — [name].
6. Apply normal entry conditions from that stage forward.

---

## CAMPAIGN OPEN

Before any stage begins:

1. Locate: `simulations/scout/{topic}-scout-*.md` — most recent by date if multiple.
   - If none found: emit BLOCKED. No scout artifact for `{topic}`. Run scout first. Halt.
2. Set scout_anchor = full path of found file.
3. Read the artifact. Extract:
   - status_quo_comparator — the incumbent solution this topic displaces. Concrete name.
   - inertia_vulnerability — the specific resistance point. Concrete name.

Emit:

  CAMPAIGN OPEN.
  scout_anchor:            simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator:   [named incumbent]
  inertia_vulnerability:   [named resistance point]

No stage work begins until CAMPAIGN OPEN is emitted with both fields named.

---

## ROLE CARD DECLARATIONS

All five stages declared before any stage executes.

| Field                   | STAGE 1 — HYPOTHESIS                                                            |
|-------------------------|---------------------------------------------------------------------------------|
| Role No.                | Stage 1 of 5                                                                    |
| Task                    | Frame displacement hypothesis grounded in scout artifact                        |
| Artifact                | prove-hypothesis                                                                |
| Path template           | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md           |
| stages_completed ID     | stage-1-hypothesis                                                              |
| Entry conditions        | CAMPAIGN OPEN emitted; scout_anchor, status_quo_comparator, inertia_vulnerability confirmed |
| Exit gate               | GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md |

| Field                   | STAGE 2 — WEBSEARCH                                                             |
|-------------------------|---------------------------------------------------------------------------------|
| Role No.                | Stage 2 of 5                                                                    |
| Task                    | Gather external evidence; flag THIN displacement gaps at point of discovery     |
| Artifact                | prove-websearch                                                                 |
| Path template           | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md             |
| stages_completed ID     | stage-2-websearch                                                               |
| Entry conditions        | GATE-1 CLEARED. received; path in gate matches Stage 1 path template            |
| Exit gate               | GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md |

| Field                   | STAGE 3 — INTELLIGENCE                                                          |
|-------------------------|---------------------------------------------------------------------------------|
| Role No.                | Stage 3 of 5                                                                    |
| Task                    | Scan internal sources; flag THIN displacement gaps at point of discovery        |
| Artifact                | prove-intelligence                                                              |
| Path template           | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md       |
| stages_completed ID     | stage-3-intelligence                                                            |
| Entry conditions        | GATE-2 CLEARED. received; path in gate matches Stage 2 path template            |
| Exit gate               | GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md |

| Field                   | STAGE 4 — ANALYSIS                                                              |
|-------------------------|---------------------------------------------------------------------------------|
| Role No.                | Stage 4 of 5                                                                    |
| Task                    | Aggregate THIN flags (GATE-4A), then map to displacement claims                 |
| Artifact                | prove-analysis                                                                  |
| Path template           | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md               |
| stages_completed ID     | stage-4-analysis                                                                |
| Entry conditions        | GATE-3 CLEARED. received; path in gate matches Stage 3 path template            |
| Exit gate               | GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md |

| Field                   | STAGE 5 — SYNTHESIZE                                                            |
|-------------------------|---------------------------------------------------------------------------------|
| Role No.                | Stage 5 of 5                                                                    |
| Task                    | Synthesize evidence; output FORM A or FORM B confidence table; name /topic-story |
| Artifact                | prove-synthesize                                                                |
| Path template           | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md           |
| stages_completed ID     | stage-5-synthesize                                                              |
| Entry conditions        | GATE-4 CLEARED. received; path in gate matches Stage 4 path template            |
| Exit gate               | GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md |

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN emitted. scout_anchor, status_quo_comparator, inertia_vulnerability confirmed.
  [ ] (Or: RESUMING CAMPAIGN with stage-1-hypothesis absent from stages_completed.)

WORK: Frame the central testable claim for {topic} as a displacement claim:
"{topic} displaces {status_quo_comparator} because [mechanism], despite
{inertia_vulnerability}." Reference scout_anchor in artifact body AND in YAML.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-hypothesis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis]

STAGE 1 COMPLETION CHECKLIST:
  [ ] Hypothesis stated as a falsifiable displacement claim
  [ ] scout_anchor cited in artifact body AND in YAML frontmatter
  [ ] status_quo_comparator + inertia_vulnerability in YAML frontmatter
  [ ] stages_completed: [stage-1-hypothesis] in YAML frontmatter
  [ ] Artifact written to path matching Stage 1 ROLE CARD path template
  [ ] When all items above are checked: (1) append stage-1-hypothesis to stages_completed;
      (2) emit GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
      Single event, both outputs. Path must match Stage 1 ROLE CARD path template.

PATH CHAIN VERIFICATION — Transition 1 -> 2:

  Channel                    | Path
  ---------------------------|--------------------------------------------------------------------
  ROLE CARD path template    | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Write instruction (Stg 1)  | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Gate clearance (GATE-1)    | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Stage 2 entry confirmation | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 — WEBSEARCH

ENTRY CONDITIONS:
  [ ] GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
      received; path confirmed matching Stage 2 ROLE CARD entry condition path.
  [ ] Stage 1 completion checklist satisfied.
  [ ] (Or: RESUMING CAMPAIGN with stage-2-websearch absent from stages_completed.)

WORK: Gather external evidence. Flag thin or absent evidence immediately, naming incumbent:

  THIN: [area] — [gap] — weakens displacement claim against {status_quo_comparator}: [claim element]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-websearch
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch]

STAGE 2 COMPLETION CHECKLIST:
  [ ] Minimum 3 sources gathered; all THIN flags name {status_quo_comparator}
  [ ] Displacement fields carried in YAML
  [ ] stages_completed accumulates stage-2-websearch
  [ ] Artifact written to path matching Stage 2 ROLE CARD path template
  [ ] When all items above are checked: (1) append stage-2-websearch to stages_completed;
      (2) emit GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
      Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 2 -> 3:

  Channel                    | Path
  ---------------------------|-------------------------------------------------------------------
  ROLE CARD path template    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Write instruction (Stg 2)  | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Gate clearance (GATE-2)    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Stage 3 entry confirmation | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

ENTRY CONDITIONS:
  [ ] GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
      received; path confirmed matching Stage 3 ROLE CARD entry condition path.
  [ ] Stage 2 completion checklist satisfied.
  [ ] (Or: RESUMING CAMPAIGN with stage-3-intelligence absent from stages_completed.)

WORK: Scan internal sources for displacement evidence. Flag thin evidence immediately,
naming incumbent in every flag body.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-intelligence
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]

STAGE 3 COMPLETION CHECKLIST:
  [ ] Internal sources scanned; all THIN flags name {status_quo_comparator}
  [ ] Displacement fields carried in YAML
  [ ] stages_completed accumulates stage-3-intelligence
  [ ] Artifact written to path matching Stage 3 ROLE CARD path template
  [ ] When all items above are checked: (1) append stage-3-intelligence to stages_completed;
      (2) emit GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
      Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 3 -> 4:

  Channel                    | Path
  ----------------------------|------------------------------------------------------------------------
  ROLE CARD path template    | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Write instruction (Stg 3)  | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Gate clearance (GATE-3)    | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Stage 4 entry confirmation | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

ENTRY CONDITIONS:
  [ ] GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
      received; path confirmed matching Stage 4 ROLE CARD entry condition path.
  [ ] Stage 3 completion checklist satisfied.
  [ ] (Or: RESUMING CAMPAIGN with stage-4-analysis absent from stages_completed.)

WORK: Two parts. PART A: aggregate THIN flags into table (final column: displacement claim
vs {status_quo_comparator}). Emit GATE-4A CLEARED. PART B cannot begin until emitted.
PART B: map flags to displacement claims; assess overall displacement case.

PART A — Aggregation table:

  Flag ID | Stage | Area | Evidence Gap | Displacement Claim Weakened (vs. {status_quo_comparator})
  --------|-------|------|--------------|----------------------------------------------------------
  THIN-01 | 2     | ...  | ...          | ...

If no THIN flags: one row — no THIN findings — — —
Emit: GATE-4A CLEARED.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-analysis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]

STAGE 4 COMPLETION CHECKLIST:
  [ ] GATE-4A emitted; aggregation table complete with displacement claim column
  [ ] All THIN flags mapped to displacement claims against {status_quo_comparator}
  [ ] Displacement fields carried in YAML
  [ ] stages_completed accumulates stage-4-analysis
  [ ] Artifact written to path matching Stage 4 ROLE CARD path template
  [ ] When all items above are checked: (1) append stage-4-analysis to stages_completed;
      (2) emit GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
      Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 4 -> 5:

  Channel                    | Path
  ---------------------------|----------------------------------------------------------------
  ROLE CARD path template    | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Write instruction (Stg 4)  | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Gate clearance (GATE-4)    | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Stage 5 entry confirmation | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIZE

ENTRY CONDITIONS:
  [ ] GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
      received; path confirmed matching Stage 5 ROLE CARD entry condition path.
  [ ] Stage 4 completion checklist satisfied (GATE-4A emitted, flags mapped).
  [ ] (Or: RESUMING CAMPAIGN with stage-5-synthesize absent from stages_completed.)

WORK: Synthesize all evidence. Output confidence adjustment table as FORM A or FORM B.

FORM A (one or more THIN flags):

  Displacement Claim (vs. {status_quo_comparator}) | Source Stage | Evidence Gap | Adjusted Confidence
  --------------------------------------------------|-------------|--------------|--------------------
  [claim]                                           | Stage N      | [gap]        | [Low / Med / High]

FORM B (zero THIN flags):

  Displacement Claim (vs. {status_quo_comparator}) | Source Stage | Evidence Gap | Adjusted Confidence
  --------------------------------------------------|-------------|--------------|--------------------
  no THIN findings                                  | —            | —            | n/a

State explicitly: This evidence brief is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-synthesize
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence,
                     stage-4-analysis, stage-5-synthesize]

STAGE 5 COMPLETION CHECKLIST:
  [ ] All evidence synthesized; displacement verdict stated
  [ ] FORM A or FORM B output (form label above table); per-claim adjusted confidence
  [ ] FORM B explicit empty row when no THIN findings
  [ ] /topic-story named as explicit next step
  [ ] Displacement fields + all 5 stage IDs in YAML
  [ ] Artifact written to path matching Stage 5 ROLE CARD path template
  [ ] When all items above are checked: emit GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
      Campaign complete.
```

---

## V-03 — Role Sequence (C-35: Displacement Field Recovery)

**Axis**: Role sequence
**Hypothesis**: An interrupted-campaign recovery procedure that includes an explicit named
step to read `status_quo_comparator` and `inertia_vulnerability` from the last written
artifact's YAML frontmatter — before resuming any stage work — ensures displacement framing
continuity from the YAML audit trail rather than requiring the campaign preamble to be
re-parsed. This satisfies C-35 while leaving the stage entry condition format unchanged.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Orchestrates five stages in strict
forward sequence: prove-hypothesis -> prove-websearch -> prove-intelligence ->
prove-analysis -> prove-synthesize. Reads prior scout signals to ground the hypothesis.
Writes one artifact per stage. Final output: a synthesized evidence brief ready for
/topic-story.

---

## INTERRUPTED CAMPAIGN RECOVERY

If resuming a campaign that was interrupted:

1. Find the most recent artifact in `simulations/prove/` for this topic.
2. Read its `stages_completed` YAML field to identify which stages finished.
3. Read `status_quo_comparator` and `inertia_vulnerability` from that artifact's YAML
   frontmatter to restore displacement framing before resuming any stage work. These
   fields are the displacement recovery targets. Do not re-parse the campaign preamble —
   the YAML fields are the authoritative source for interrupted campaigns.
4. Check which gate clearance strings are absent from context to identify the next
   required stage.
5. Resume from the first stage whose identifier is absent from `stages_completed`.
6. Emit: RESUMING CAMPAIGN. stages_completed = [...]. status_quo_comparator = [value].
   inertia_vulnerability = [value]. Next stage: Stage N — [name].
7. Apply normal entry conditions from that stage forward.

This procedure applies before Stage 0 and at any point a prior partial run is detected.

---

## STAGE 0 — CAMPAIGN OPEN

Before any stage begins:

1. Locate: `simulations/scout/{topic}-scout-*.md` — most recent by date if multiple.
   - If none found: emit BLOCKED. No scout artifact for `{topic}`. Run scout first. Halt.
2. Set scout_anchor = full path of found file.
3. Read the artifact. Extract:
   - status_quo_comparator — the incumbent solution this topic displaces. Concrete name.
   - inertia_vulnerability — the specific resistance point. Concrete name.

Emit:

  CAMPAIGN OPEN.
  scout_anchor:            simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator:   [named incumbent]
  inertia_vulnerability:   [named resistance point]

No stage work begins until CAMPAIGN OPEN is emitted with both fields named.
All THIN flags and synthesis claims are displacement claims against status_quo_comparator.

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN emitted. scout_anchor, status_quo_comparator, inertia_vulnerability confirmed.
  [ ] (Or: RESUMING CAMPAIGN — status_quo_comparator and inertia_vulnerability restored
      from last artifact YAML, stage-1-hypothesis absent from stages_completed.)

WORK: Frame the central testable claim for {topic} as a displacement claim:
"{topic} displaces {status_quo_comparator} because [mechanism], despite
{inertia_vulnerability}." Reference scout_anchor in artifact body AND YAML.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-hypothesis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis]

STAGE 1 COMPLETION CHECKLIST:
  [ ] Hypothesis stated as a falsifiable displacement claim
  [ ] scout_anchor cited in artifact body AND YAML frontmatter
  [ ] status_quo_comparator and inertia_vulnerability in YAML frontmatter
  [ ] stages_completed: [stage-1-hypothesis] in YAML frontmatter
  [ ] Artifact written to simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  [ ] When all items above are checked: (1) append stage-1-hypothesis to stages_completed;
      (2) emit GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
      Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 1 -> 2:

  Channel                    | Path
  ---------------------------|--------------------------------------------------------------------
  Write instruction (Stg 1)  | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Gate clearance (GATE-1)    | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Stage 2 entry confirmation | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 — WEBSEARCH

ENTRY CONDITIONS:
  [ ] GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
      received and path confirmed.
  [ ] Stage 1 completion checklist satisfied.
  [ ] (Or: RESUMING CAMPAIGN — status_quo_comparator and inertia_vulnerability restored
      from last artifact YAML, stage-2-websearch absent from stages_completed.)

WORK: Gather external evidence. Flag thin evidence immediately, naming incumbent:

  THIN: [area] — [gap] — weakens displacement claim against {status_quo_comparator}: [claim element]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-websearch
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch]

STAGE 2 COMPLETION CHECKLIST:
  [ ] Minimum 3 sources; all THIN flags name {status_quo_comparator}
  [ ] Displacement fields in YAML; stages_completed accumulates stage-2-websearch
  [ ] Artifact written to simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  [ ] When all items above are checked: (1) append stage-2-websearch to stages_completed;
      (2) emit GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
      Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 2 -> 3:

  Channel                    | Path
  ---------------------------|-------------------------------------------------------------------
  Write instruction (Stg 2)  | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Gate clearance (GATE-2)    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Stage 3 entry confirmation | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

ENTRY CONDITIONS:
  [ ] GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
      received and path confirmed.
  [ ] Stage 2 completion checklist satisfied.
  [ ] (Or: RESUMING CAMPAIGN — status_quo_comparator and inertia_vulnerability restored
      from last artifact YAML, stage-3-intelligence absent from stages_completed.)

WORK: Scan internal sources for displacement evidence. Flag thin evidence immediately,
naming incumbent in every flag body.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-intelligence
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]

STAGE 3 COMPLETION CHECKLIST:
  [ ] Internal sources scanned; all THIN flags name {status_quo_comparator}
  [ ] Displacement fields in YAML; stages_completed accumulates stage-3-intelligence
  [ ] Artifact written to simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  [ ] When all items above are checked: (1) append stage-3-intelligence to stages_completed;
      (2) emit GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
      Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 3 -> 4:

  Channel                    | Path
  ----------------------------|------------------------------------------------------------------------
  Write instruction (Stg 3)  | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Gate clearance (GATE-3)    | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Stage 4 entry confirmation | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

ENTRY CONDITIONS:
  [ ] GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
      received and path confirmed.
  [ ] Stage 3 completion checklist satisfied.
  [ ] (Or: RESUMING CAMPAIGN — status_quo_comparator and inertia_vulnerability restored
      from last artifact YAML, stage-4-analysis absent from stages_completed.)

WORK: PART A — aggregate THIN flags (displacement claim column names {status_quo_comparator}).
Emit GATE-4A CLEARED. PART B — map flags to displacement claims; assess overall case.

PART A aggregation table:

  Flag ID | Stage | Area | Evidence Gap | Displacement Claim Weakened (vs. {status_quo_comparator})
  --------|-------|------|--------------|----------------------------------------------------------
  THIN-01 | 2     | ...  | ...          | ...

If no THIN flags: one row — no THIN findings — — —
Emit: GATE-4A CLEARED.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-analysis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]

STAGE 4 COMPLETION CHECKLIST:
  [ ] GATE-4A emitted; aggregation table names displacement claims vs {status_quo_comparator}
  [ ] All flags mapped; displacement fields in YAML; stages_completed accumulates stage-4-analysis
  [ ] Artifact written to simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  [ ] When all items above are checked: (1) append stage-4-analysis to stages_completed;
      (2) emit GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
      Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 4 -> 5:

  Channel                    | Path
  ---------------------------|----------------------------------------------------------------
  Write instruction (Stg 4)  | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Gate clearance (GATE-4)    | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Stage 5 entry confirmation | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIZE

ENTRY CONDITIONS:
  [ ] GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
      received and path confirmed.
  [ ] Stage 4 completion checklist satisfied (GATE-4A emitted, all flags mapped).
  [ ] (Or: RESUMING CAMPAIGN — status_quo_comparator and inertia_vulnerability restored
      from last artifact YAML, stage-5-synthesize absent from stages_completed.)

WORK: Synthesize all evidence. Output FORM A or FORM B.

FORM A (one or more THIN flags):

  Displacement Claim (vs. {status_quo_comparator}) | Source Stage | Evidence Gap | Adjusted Confidence
  --------------------------------------------------|-------------|--------------|--------------------
  [claim]                                           | Stage N      | [gap]        | [Low / Med / High]

FORM B (zero THIN flags):

  Displacement Claim (vs. {status_quo_comparator}) | Source Stage | Evidence Gap | Adjusted Confidence
  --------------------------------------------------|-------------|--------------|--------------------
  no THIN findings                                  | —            | —            | n/a

State explicitly: This evidence brief is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-synthesize
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence,
                     stage-4-analysis, stage-5-synthesize]

STAGE 5 COMPLETION CHECKLIST:
  [ ] All evidence synthesized; displacement verdict stated
  [ ] FORM A or FORM B output; per-claim adjusted confidence; FORM B has explicit empty row
  [ ] /topic-story named as explicit next step
  [ ] Displacement fields + all 5 stage IDs in YAML
  [ ] Artifact written to simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
  [ ] When all items above are checked: emit GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
      Campaign complete.
```

---

## V-04 — Lifecycle + Inertia Combined (C-35 + C-36)

**Axis**: Lifecycle emphasis + Inertia framing
**Hypothesis**: Combining displacement-aware recovery (C-35 — names YAML fields as recovery
targets) with fully enumerated entry conditions (C-36 — each Stage N checklist output named
individually at Stage N+1) achieves both criteria simultaneously. The displacement framing
threads through both the recovery procedure (YAML recovery targets) and the stage boundary
handoffs (enumerated checklist outputs include displacement field YAML items), creating
interlocking enforcement at interrupted-campaign and normal-flow boundaries.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Orchestrates five stages in strict
forward sequence: prove-hypothesis -> prove-websearch -> prove-intelligence ->
prove-analysis -> prove-synthesize. Displacement framing from the scout artifact governs
all THIN flags and confidence assessments. Writes one artifact per stage. Final output:
a synthesized evidence brief ready for /topic-story.

---

## INTERRUPTED CAMPAIGN RECOVERY

If resuming a campaign that was interrupted:

1. Find the most recent artifact in `simulations/prove/` for this topic.
2. Read its `stages_completed` YAML field to identify which stages finished.
3. Read `status_quo_comparator` and `inertia_vulnerability` from that artifact's YAML
   frontmatter to restore displacement framing before resuming any stage work. These are
   the displacement recovery targets — the YAML fields are authoritative. Do not re-parse
   the campaign preamble.
4. Check which gate clearance strings are absent from context to identify the next stage.
5. Resume from the first stage whose identifier is absent from `stages_completed`.
6. Emit: RESUMING CAMPAIGN. stages_completed = [...]. status_quo_comparator = [value].
   inertia_vulnerability = [value]. Next stage: Stage N — [name].
7. Apply normal entry conditions from that stage forward.

---

## STAGE 0 — CAMPAIGN OPEN

Before any stage begins:

1. Locate: `simulations/scout/{topic}-scout-*.md` — most recent by date if multiple.
   - If none found: emit BLOCKED. No scout artifact for `{topic}`. Run scout first. Halt.
2. Set scout_anchor = full path of found file.
3. Read the artifact. Extract:
   - status_quo_comparator — the incumbent solution this topic displaces. Concrete name.
   - inertia_vulnerability — the specific resistance point. Concrete name.

Emit:

  CAMPAIGN OPEN.
  scout_anchor:            simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator:   [named incumbent]
  inertia_vulnerability:   [named resistance point]

No stage work begins until CAMPAIGN OPEN is emitted with both fields named.
All THIN flags and synthesis claims are displacement claims against status_quo_comparator.

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN emitted.
  [ ] scout_anchor confirmed.
  [ ] status_quo_comparator named.
  [ ] inertia_vulnerability named.
  [ ] (Or: RESUMING CAMPAIGN — status_quo_comparator + inertia_vulnerability restored
      from last artifact YAML; stage-1-hypothesis absent from stages_completed.)

WORK: Frame the central testable claim for {topic} as a displacement claim:
"{topic} displaces {status_quo_comparator} because [mechanism], despite
{inertia_vulnerability}." Reference scout_anchor in artifact body AND YAML.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-hypothesis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent from CAMPAIGN OPEN]
  inertia_vulnerability: [named resistance point from CAMPAIGN OPEN]
  stages_completed: [stage-1-hypothesis]

STAGE 1 COMPLETION CHECKLIST:
  [ ] 1. Hypothesis stated as a falsifiable displacement claim
  [ ] 2. scout_anchor path cited in artifact body
  [ ] 3. scout_anchor field present in YAML frontmatter
  [ ] 4. status_quo_comparator in YAML frontmatter
  [ ] 5. inertia_vulnerability in YAML frontmatter
  [ ] 6. stages_completed: [stage-1-hypothesis] in YAML frontmatter
  [ ] 7. Artifact written to simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  [ ] 8. When all items above are checked: (1) append stage-1-hypothesis to stages_completed;
         (2) emit GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
         Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 1 -> 2:

  Channel                    | Path
  ---------------------------|--------------------------------------------------------------------
  Write instruction (Stg 1)  | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Gate clearance (GATE-1)    | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Stage 2 entry confirmation | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 — WEBSEARCH

ENTRY CONDITIONS — each Stage 1 checklist output confirmed by name:
  [ ] 1. Stage 1 item 1: hypothesis stated as falsifiable displacement claim — confirmed
  [ ] 2. Stage 1 item 2: scout_anchor cited in artifact body — confirmed
  [ ] 3. Stage 1 item 3: scout_anchor field in YAML frontmatter — confirmed
  [ ] 4. Stage 1 item 4: status_quo_comparator in YAML frontmatter — confirmed
  [ ] 5. Stage 1 item 5: inertia_vulnerability in YAML frontmatter — confirmed
  [ ] 6. Stage 1 item 6: stages_completed: [stage-1-hypothesis] in YAML — confirmed
  [ ] 7. Stage 1 item 7: artifact written — confirmed
  [ ] 8. Stage 1 item 8: GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md — emitted and path confirmed
  [ ] (Or: RESUMING CAMPAIGN — displacement fields restored from YAML; stage-2-websearch absent.)

WORK: Gather external evidence relevant to the displacement hypothesis. Flag thin evidence
immediately, naming the incumbent in every THIN flag body:

  THIN: [area] — [gap] — weakens displacement claim against {status_quo_comparator}: [claim element]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-websearch
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch]

STAGE 2 COMPLETION CHECKLIST:
  [ ] 1. Minimum 3 external sources gathered and assessed
  [ ] 2. All THIN flags emitted inline, each naming {status_quo_comparator}
  [ ] 3. scout_anchor in YAML frontmatter
  [ ] 4. status_quo_comparator in YAML frontmatter
  [ ] 5. inertia_vulnerability in YAML frontmatter
  [ ] 6. stages_completed accumulates stage-2-websearch
  [ ] 7. Artifact written to simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  [ ] 8. When all items above are checked: (1) append stage-2-websearch to stages_completed;
         (2) emit GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
         Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 2 -> 3:

  Channel                    | Path
  ---------------------------|-------------------------------------------------------------------
  Write instruction (Stg 2)  | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Gate clearance (GATE-2)    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Stage 3 entry confirmation | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

ENTRY CONDITIONS — each Stage 2 checklist output confirmed by name:
  [ ] 1. Stage 2 item 1: minimum 3 sources gathered — confirmed
  [ ] 2. Stage 2 item 2: all THIN flags naming {status_quo_comparator} — confirmed
  [ ] 3. Stage 2 item 3: scout_anchor in YAML — confirmed
  [ ] 4. Stage 2 item 4: status_quo_comparator in YAML — confirmed
  [ ] 5. Stage 2 item 5: inertia_vulnerability in YAML — confirmed
  [ ] 6. Stage 2 item 6: stages_completed accumulates stage-2-websearch — confirmed
  [ ] 7. Stage 2 item 7: artifact written — confirmed
  [ ] 8. Stage 2 item 8: GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md — emitted and path confirmed
  [ ] (Or: RESUMING CAMPAIGN — displacement fields restored from YAML; stage-3-intelligence absent.)

WORK: Scan internal sources for displacement evidence. Flag thin evidence immediately,
naming {status_quo_comparator} in every THIN flag body.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-intelligence
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]

STAGE 3 COMPLETION CHECKLIST:
  [ ] 1. Internal sources scanned and assessed
  [ ] 2. All THIN flags emitted inline, each naming {status_quo_comparator}
  [ ] 3. scout_anchor in YAML frontmatter
  [ ] 4. status_quo_comparator in YAML frontmatter
  [ ] 5. inertia_vulnerability in YAML frontmatter
  [ ] 6. stages_completed accumulates stage-3-intelligence
  [ ] 7. Artifact written to simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  [ ] 8. When all items above are checked: (1) append stage-3-intelligence to stages_completed;
         (2) emit GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
         Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 3 -> 4:

  Channel                    | Path
  ----------------------------|------------------------------------------------------------------------
  Write instruction (Stg 3)  | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Gate clearance (GATE-3)    | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Stage 4 entry confirmation | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

ENTRY CONDITIONS — each Stage 3 checklist output confirmed by name:
  [ ] 1. Stage 3 item 1: internal sources scanned — confirmed
  [ ] 2. Stage 3 item 2: all THIN flags naming {status_quo_comparator} — confirmed
  [ ] 3. Stage 3 item 3: scout_anchor in YAML — confirmed
  [ ] 4. Stage 3 item 4: status_quo_comparator in YAML — confirmed
  [ ] 5. Stage 3 item 5: inertia_vulnerability in YAML — confirmed
  [ ] 6. Stage 3 item 6: stages_completed accumulates stage-3-intelligence — confirmed
  [ ] 7. Stage 3 item 7: artifact written — confirmed
  [ ] 8. Stage 3 item 8: GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md — emitted and path confirmed
  [ ] (Or: RESUMING CAMPAIGN — displacement fields restored from YAML; stage-4-analysis absent.)

WORK: PART A — aggregate THIN flags. PART B — map to displacement claims.

PART A aggregation table (displacement claim column names {status_quo_comparator}):

  Flag ID | Stage | Area | Evidence Gap | Displacement Claim Weakened (vs. {status_quo_comparator})
  --------|-------|------|--------------|----------------------------------------------------------
  THIN-01 | 2     | ...  | ...          | ...

If no THIN flags: one row — no THIN findings — — —
Emit: GATE-4A CLEARED. Part B cannot begin until emitted.

PART B: Map each flag to the displacement claim it weakens. Assess the overall case
that {topic} outperforms {status_quo_comparator} despite {inertia_vulnerability}.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-analysis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]

STAGE 4 COMPLETION CHECKLIST:
  [ ] 1.  GATE-4A emitted (aggregation complete before mapping begins)
  [ ] 2.  Aggregation table final column names displacement claim vs {status_quo_comparator}
  [ ] 3.  All THIN flags mapped to displacement claims
  [ ] 4.  Overall displacement case assessed
  [ ] 5.  scout_anchor in YAML frontmatter
  [ ] 6.  status_quo_comparator in YAML frontmatter
  [ ] 7.  inertia_vulnerability in YAML frontmatter
  [ ] 8.  stages_completed accumulates stage-4-analysis
  [ ] 9.  Artifact written to simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  [ ] 10. When all items above are checked: (1) append stage-4-analysis to stages_completed;
          (2) emit GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
          Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 4 -> 5:

  Channel                    | Path
  ---------------------------|----------------------------------------------------------------
  Write instruction (Stg 4)  | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Gate clearance (GATE-4)    | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Stage 5 entry confirmation | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIZE

ENTRY CONDITIONS — each Stage 4 checklist output confirmed by name:
  [ ] 1.  Stage 4 item 1: GATE-4A emitted — confirmed
  [ ] 2.  Stage 4 item 2: aggregation table names displacement claims — confirmed
  [ ] 3.  Stage 4 item 3: all THIN flags mapped to displacement claims — confirmed
  [ ] 4.  Stage 4 item 4: overall displacement case assessed — confirmed
  [ ] 5.  Stage 4 item 5: scout_anchor in YAML — confirmed
  [ ] 6.  Stage 4 item 6: status_quo_comparator in YAML — confirmed
  [ ] 7.  Stage 4 item 7: inertia_vulnerability in YAML — confirmed
  [ ] 8.  Stage 4 item 8: stages_completed accumulates stage-4-analysis — confirmed
  [ ] 9.  Stage 4 item 9: artifact written — confirmed
  [ ] 10. Stage 4 item 10: GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md — emitted and path confirmed
  [ ] (Or: RESUMING CAMPAIGN — displacement fields restored from YAML; stage-5-synthesize absent.)

WORK: Synthesize all evidence. State whether the displacement case is proven, partially
proven, or not proven. Assign adjusted confidence per THIN-flagged claim.

CONFIDENCE ADJUSTMENT TABLE — output exactly one named form:

FORM A (one or more THIN flags exist):

  Displacement Claim (vs. {status_quo_comparator}) | Source Stage | Evidence Gap | Adjusted Confidence
  --------------------------------------------------|-------------|--------------|--------------------
  [claim]                                           | Stage N      | [gap]        | [Low / Med / High]

FORM B (zero THIN flags):

  Displacement Claim (vs. {status_quo_comparator}) | Source Stage | Evidence Gap | Adjusted Confidence
  --------------------------------------------------|-------------|--------------|--------------------
  no THIN findings                                  | —            | —            | n/a

State explicitly: This evidence brief is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-synthesize
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence,
                     stage-4-analysis, stage-5-synthesize]

STAGE 5 COMPLETION CHECKLIST:
  [ ] 1.  All evidence synthesized; displacement verdict stated
  [ ] 2.  FORM A or FORM B output (form label above table)
  [ ] 3.  Each THIN-flagged claim has adjusted confidence level
  [ ] 4.  FORM B has explicit empty row when no THIN findings
  [ ] 5.  /topic-story named as explicit next step
  [ ] 6.  scout_anchor in YAML frontmatter
  [ ] 7.  status_quo_comparator in YAML frontmatter
  [ ] 8.  inertia_vulnerability in YAML frontmatter
  [ ] 9.  All 5 stage identifiers in stages_completed
  [ ] 10. Artifact written to simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
  [ ] 11. When all items above are checked: emit GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
          Campaign complete.
```

---

## V-05 — All Axes Combined (C-35 + C-36 + C-37 + Inertia Framing)

**Axis**: All four axes
**Hypothesis**: Maximum structural density — ROLE CARD declaration tables (C-37) establish
all stage fields statically before execution; enumerated entry conditions (C-36) name each
prior stage checklist output individually at every boundary; displacement-aware recovery
(C-35) names status_quo_comparator + inertia_vulnerability as explicit YAML recovery
targets; and full inertia framing (C-32–C-34) threads displacement claims through every
THIN flag and YAML field. The combined design achieves the widest possible criterion
coverage while remaining auditable as a single prompt.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Five evidence stages defined by ROLE
CARD declarations and executed in strict forward sequence: prove-hypothesis ->
prove-websearch -> prove-intelligence -> prove-analysis -> prove-synthesize. Displacement
framing governs all THIN flags and confidence assessments. Writes one artifact per stage.
Final output: a synthesized evidence brief ready for /topic-story.

---

## INTERRUPTED CAMPAIGN RECOVERY

If resuming a campaign that was interrupted:

1. Find the most recent artifact in `simulations/prove/` for this topic.
2. Read its `stages_completed` YAML field to identify which stages finished.
3. Read `status_quo_comparator` and `inertia_vulnerability` from that artifact's YAML
   frontmatter to restore displacement framing before resuming any stage work. These are
   the displacement recovery targets — the YAML fields are authoritative. Do not re-parse
   the campaign preamble.
4. Check which gate clearance strings are absent from context to identify the next stage.
5. Resume from the first stage whose identifier is absent from `stages_completed`.
6. Emit: RESUMING CAMPAIGN. stages_completed = [...]. status_quo_comparator = [value].
   inertia_vulnerability = [value]. Next stage: Stage N — [name].
7. Apply normal entry conditions from that stage forward.

---

## CAMPAIGN OPEN

Before any stage begins:

1. Locate: `simulations/scout/{topic}-scout-*.md` — most recent by date if multiple.
   - If none found: emit BLOCKED. No scout artifact for `{topic}`. Run scout first. Halt.
2. Set scout_anchor = full path of found file.
3. Read the artifact. Extract:
   - status_quo_comparator — the incumbent solution this topic displaces. Concrete name.
   - inertia_vulnerability — the specific resistance point. Concrete name.

Emit:

  CAMPAIGN OPEN.
  scout_anchor:            simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator:   [named incumbent]
  inertia_vulnerability:   [named resistance point]

No stage work begins until CAMPAIGN OPEN is emitted with both fields named.
All THIN flags and synthesis claims are displacement claims against status_quo_comparator.

---

## ROLE CARD DECLARATIONS

All five stages declared before any stage executes.
Path template, stages_completed ID, entry conditions, and exit gate are statically
parseable from these tables without executing any stage.

| Field                   | STAGE 1 — HYPOTHESIS                                                            |
|-------------------------|---------------------------------------------------------------------------------|
| Role No.                | Stage 1 of 5                                                                    |
| Task                    | Frame displacement hypothesis grounded in scout; carry displacement YAML fields  |
| Artifact                | prove-hypothesis                                                                |
| Path template           | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md           |
| stages_completed ID     | stage-1-hypothesis                                                              |
| Entry conditions        | CAMPAIGN OPEN emitted; scout_anchor, status_quo_comparator, inertia_vulnerability confirmed |
| Exit gate               | GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md |

| Field                   | STAGE 2 — WEBSEARCH                                                             |
|-------------------------|---------------------------------------------------------------------------------|
| Role No.                | Stage 2 of 5                                                                    |
| Task                    | Gather external evidence; THIN flags name displacement claim vs status_quo_comparator |
| Artifact                | prove-websearch                                                                 |
| Path template           | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md             |
| stages_completed ID     | stage-2-websearch                                                               |
| Entry conditions        | Stage 1 completion checklist items 1-8 each confirmed by name; GATE-1 path confirmed |
| Exit gate               | GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md |

| Field                   | STAGE 3 — INTELLIGENCE                                                          |
|-------------------------|---------------------------------------------------------------------------------|
| Role No.                | Stage 3 of 5                                                                    |
| Task                    | Scan internal sources; THIN flags name displacement claim vs status_quo_comparator |
| Artifact                | prove-intelligence                                                              |
| Path template           | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md       |
| stages_completed ID     | stage-3-intelligence                                                            |
| Entry conditions        | Stage 2 completion checklist items 1-8 each confirmed by name; GATE-2 path confirmed |
| Exit gate               | GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md |

| Field                   | STAGE 4 — ANALYSIS                                                              |
|-------------------------|---------------------------------------------------------------------------------|
| Role No.                | Stage 4 of 5                                                                    |
| Task                    | GATE-4A: aggregate THIN flags with displacement claim column; map to claims      |
| Artifact                | prove-analysis                                                                  |
| Path template           | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md               |
| stages_completed ID     | stage-4-analysis                                                                |
| Entry conditions        | Stage 3 completion checklist items 1-8 each confirmed by name; GATE-3 path confirmed |
| Exit gate               | GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md |

| Field                   | STAGE 5 — SYNTHESIZE                                                            |
|-------------------------|---------------------------------------------------------------------------------|
| Role No.                | Stage 5 of 5                                                                    |
| Task                    | Synthesize; FORM A or FORM B confidence table; name /topic-story                |
| Artifact                | prove-synthesize                                                                |
| Path template           | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md           |
| stages_completed ID     | stage-5-synthesize                                                              |
| Entry conditions        | Stage 4 completion checklist items 1-10 each confirmed by name; GATE-4 path confirmed |
| Exit gate               | GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md |

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN emitted.
  [ ] scout_anchor confirmed (matches Stage 1 ROLE CARD entry condition).
  [ ] status_quo_comparator named.
  [ ] inertia_vulnerability named.
  [ ] (Or: RESUMING CAMPAIGN — status_quo_comparator + inertia_vulnerability restored
      from last artifact YAML; stage-1-hypothesis absent from stages_completed.)

WORK: Frame the central testable claim as a displacement claim:
"{topic} displaces {status_quo_comparator} because [mechanism], despite
{inertia_vulnerability}." Reference scout_anchor in artifact body AND YAML.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-hypothesis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent from CAMPAIGN OPEN]
  inertia_vulnerability: [named resistance point from CAMPAIGN OPEN]
  stages_completed: [stage-1-hypothesis]

STAGE 1 COMPLETION CHECKLIST:
  [ ] 1. Hypothesis stated as a falsifiable displacement claim
  [ ] 2. scout_anchor path cited in artifact body
  [ ] 3. scout_anchor field present in YAML frontmatter
  [ ] 4. status_quo_comparator in YAML frontmatter
  [ ] 5. inertia_vulnerability in YAML frontmatter
  [ ] 6. stages_completed: [stage-1-hypothesis] in YAML frontmatter
  [ ] 7. Artifact written to path matching Stage 1 ROLE CARD path template
  [ ] 8. When all items above are checked: (1) append stage-1-hypothesis to stages_completed;
         (2) emit GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
         Single event, both outputs. Path must match Stage 1 ROLE CARD exit gate.

PATH CHAIN VERIFICATION — Transition 1 -> 2:

  Channel                    | Path
  ---------------------------|--------------------------------------------------------------------
  ROLE CARD path template    | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Write instruction (Stg 1)  | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Gate clearance (GATE-1)    | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Stage 2 entry confirmation | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 — WEBSEARCH

ENTRY CONDITIONS — each Stage 1 checklist output confirmed by name:
  [ ] 1. Stage 1 item 1: hypothesis stated as falsifiable displacement claim — confirmed
  [ ] 2. Stage 1 item 2: scout_anchor cited in artifact body — confirmed
  [ ] 3. Stage 1 item 3: scout_anchor field in YAML frontmatter — confirmed
  [ ] 4. Stage 1 item 4: status_quo_comparator in YAML frontmatter — confirmed
  [ ] 5. Stage 1 item 5: inertia_vulnerability in YAML frontmatter — confirmed
  [ ] 6. Stage 1 item 6: stages_completed: [stage-1-hypothesis] in YAML — confirmed
  [ ] 7. Stage 1 item 7: artifact written to ROLE CARD path template — confirmed
  [ ] 8. Stage 1 item 8: GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md — emitted and path confirmed, matching Stage 2 ROLE CARD entry condition
  [ ] (Or: RESUMING CAMPAIGN — displacement fields restored from YAML; stage-2-websearch absent.)

WORK: Gather external evidence. Flag thin evidence immediately. Every THIN flag body
names the incumbent explicitly:

  THIN: [area] — [gap] — weakens displacement claim against {status_quo_comparator}: [claim element]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-websearch
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch]

STAGE 2 COMPLETION CHECKLIST:
  [ ] 1. Minimum 3 external sources gathered and assessed
  [ ] 2. All THIN flags emitted inline, each naming {status_quo_comparator}
  [ ] 3. scout_anchor in YAML frontmatter
  [ ] 4. status_quo_comparator in YAML frontmatter
  [ ] 5. inertia_vulnerability in YAML frontmatter
  [ ] 6. stages_completed accumulates stage-2-websearch
  [ ] 7. Artifact written to path matching Stage 2 ROLE CARD path template
  [ ] 8. When all items above are checked: (1) append stage-2-websearch to stages_completed;
         (2) emit GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
         Single event, both outputs. Path must match Stage 2 ROLE CARD exit gate.

PATH CHAIN VERIFICATION — Transition 2 -> 3:

  Channel                    | Path
  ---------------------------|-------------------------------------------------------------------
  ROLE CARD path template    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Write instruction (Stg 2)  | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Gate clearance (GATE-2)    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Stage 3 entry confirmation | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

ENTRY CONDITIONS — each Stage 2 checklist output confirmed by name:
  [ ] 1. Stage 2 item 1: minimum 3 sources gathered — confirmed
  [ ] 2. Stage 2 item 2: all THIN flags naming {status_quo_comparator} — confirmed
  [ ] 3. Stage 2 item 3: scout_anchor in YAML — confirmed
  [ ] 4. Stage 2 item 4: status_quo_comparator in YAML — confirmed
  [ ] 5. Stage 2 item 5: inertia_vulnerability in YAML — confirmed
  [ ] 6. Stage 2 item 6: stages_completed accumulates stage-2-websearch — confirmed
  [ ] 7. Stage 2 item 7: artifact written to ROLE CARD path template — confirmed
  [ ] 8. Stage 2 item 8: GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md — emitted and path confirmed, matching Stage 3 ROLE CARD entry condition
  [ ] (Or: RESUMING CAMPAIGN — displacement fields restored from YAML; stage-3-intelligence absent.)

WORK: Scan internal sources for displacement evidence. Flag thin evidence immediately,
naming {status_quo_comparator} in every THIN flag body.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-intelligence
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]

STAGE 3 COMPLETION CHECKLIST:
  [ ] 1. Internal sources scanned and assessed
  [ ] 2. All THIN flags emitted inline, each naming {status_quo_comparator}
  [ ] 3. scout_anchor in YAML frontmatter
  [ ] 4. status_quo_comparator in YAML frontmatter
  [ ] 5. inertia_vulnerability in YAML frontmatter
  [ ] 6. stages_completed accumulates stage-3-intelligence
  [ ] 7. Artifact written to path matching Stage 3 ROLE CARD path template
  [ ] 8. When all items above are checked: (1) append stage-3-intelligence to stages_completed;
         (2) emit GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
         Single event, both outputs. Path must match Stage 3 ROLE CARD exit gate.

PATH CHAIN VERIFICATION — Transition 3 -> 4:

  Channel                    | Path
  ----------------------------|------------------------------------------------------------------------
  ROLE CARD path template    | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Write instruction (Stg 3)  | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Gate clearance (GATE-3)    | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Stage 4 entry confirmation | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

ENTRY CONDITIONS — each Stage 3 checklist output confirmed by name:
  [ ] 1. Stage 3 item 1: internal sources scanned — confirmed
  [ ] 2. Stage 3 item 2: all THIN flags naming {status_quo_comparator} — confirmed
  [ ] 3. Stage 3 item 3: scout_anchor in YAML — confirmed
  [ ] 4. Stage 3 item 4: status_quo_comparator in YAML — confirmed
  [ ] 5. Stage 3 item 5: inertia_vulnerability in YAML — confirmed
  [ ] 6. Stage 3 item 6: stages_completed accumulates stage-3-intelligence — confirmed
  [ ] 7. Stage 3 item 7: artifact written to ROLE CARD path template — confirmed
  [ ] 8. Stage 3 item 8: GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md — emitted and path confirmed, matching Stage 4 ROLE CARD entry condition
  [ ] (Or: RESUMING CAMPAIGN — displacement fields restored from YAML; stage-4-analysis absent.)

WORK: Two parts separated by GATE-4A.

PART A — Flag Aggregation:
Collect all THIN flags from Stages 2–3. Final column names the displacement claim against
status_quo_comparator that is weakened:

  Flag ID | Stage | Area | Evidence Gap | Displacement Claim Weakened (vs. {status_quo_comparator})
  --------|-------|------|--------------|----------------------------------------------------------
  THIN-01 | 2     | ...  | ...          | ...

If no THIN flags: one row — no THIN findings — — —
Emit: GATE-4A CLEARED. Part B cannot begin until emitted.

PART B — Hypothesis Mapping:
Map each THIN flag to the displacement claim it weakens. Assess the overall case
that {topic} outperforms {status_quo_comparator} despite {inertia_vulnerability}.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-analysis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]

STAGE 4 COMPLETION CHECKLIST:
  [ ] 1.  GATE-4A emitted (aggregation complete before mapping begins)
  [ ] 2.  Aggregation table final column names displacement claim vs {status_quo_comparator}
  [ ] 3.  All THIN flags mapped to displacement claims against {status_quo_comparator}
  [ ] 4.  Overall displacement case assessed (proven / partial / not proven)
  [ ] 5.  scout_anchor in YAML frontmatter
  [ ] 6.  status_quo_comparator in YAML frontmatter
  [ ] 7.  inertia_vulnerability in YAML frontmatter
  [ ] 8.  stages_completed accumulates stage-4-analysis
  [ ] 9.  Artifact written to path matching Stage 4 ROLE CARD path template
  [ ] 10. When all items above are checked: (1) append stage-4-analysis to stages_completed;
          (2) emit GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
          Single event, both outputs. Path must match Stage 4 ROLE CARD exit gate.

PATH CHAIN VERIFICATION — Transition 4 -> 5:

  Channel                    | Path
  ---------------------------|----------------------------------------------------------------
  ROLE CARD path template    | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Write instruction (Stg 4)  | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Gate clearance (GATE-4)    | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Stage 5 entry confirmation | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIZE

ENTRY CONDITIONS — each Stage 4 checklist output confirmed by name:
  [ ] 1.  Stage 4 item 1: GATE-4A emitted — confirmed
  [ ] 2.  Stage 4 item 2: aggregation table names displacement claims — confirmed
  [ ] 3.  Stage 4 item 3: all THIN flags mapped to displacement claims — confirmed
  [ ] 4.  Stage 4 item 4: overall displacement case assessed — confirmed
  [ ] 5.  Stage 4 item 5: scout_anchor in YAML — confirmed
  [ ] 6.  Stage 4 item 6: status_quo_comparator in YAML — confirmed
  [ ] 7.  Stage 4 item 7: inertia_vulnerability in YAML — confirmed
  [ ] 8.  Stage 4 item 8: stages_completed accumulates stage-4-analysis — confirmed
  [ ] 9.  Stage 4 item 9: artifact written to ROLE CARD path template — confirmed
  [ ] 10. Stage 4 item 10: GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md — emitted and path confirmed, matching Stage 5 ROLE CARD entry condition
  [ ] (Or: RESUMING CAMPAIGN — displacement fields restored from YAML; stage-5-synthesize absent.)

WORK: Synthesize all evidence. State whether the displacement case is proven, partially
proven, or not proven. Assign adjusted confidence per THIN-flagged claim.

CONFIDENCE ADJUSTMENT TABLE — output exactly one named form:

FORM A (one or more THIN flags exist):

  Displacement Claim (vs. {status_quo_comparator}) | Source Stage | Evidence Gap | Adjusted Confidence
  --------------------------------------------------|-------------|--------------|--------------------
  [claim]                                           | Stage N      | [gap]        | [Low / Med / High]

FORM B (zero THIN flags):

  Displacement Claim (vs. {status_quo_comparator}) | Source Stage | Evidence Gap | Adjusted Confidence
  --------------------------------------------------|-------------|--------------|--------------------
  no THIN findings                                  | —            | —            | n/a

State explicitly: This evidence brief is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-synthesize
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence,
                     stage-4-analysis, stage-5-synthesize]

STAGE 5 COMPLETION CHECKLIST:
  [ ] 1.  All evidence synthesized
  [ ] 2.  Displacement verdict stated (proven / partially proven / not proven)
  [ ] 3.  FORM A or FORM B output (form label as heading above table)
  [ ] 4.  Each THIN-flagged claim has adjusted confidence level
  [ ] 5.  FORM B has explicit empty row when no THIN findings
  [ ] 6.  /topic-story named as explicit next step
  [ ] 7.  scout_anchor in YAML frontmatter
  [ ] 8.  status_quo_comparator in YAML frontmatter
  [ ] 9.  inertia_vulnerability in YAML frontmatter
  [ ] 10. All 5 stage identifiers present in stages_completed
  [ ] 11. Artifact written to path matching Stage 5 ROLE CARD path template
  [ ] 12. When all items above are checked: emit GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
          Campaign complete. Path must match Stage 5 ROLE CARD exit gate.
```

---

## Criterion coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-01 through C-34 | Y | Y | Y | Y | Y | All inherit R13 V-04 baseline |
| C-35 (recovery names displacement YAML fields) | N | N | Y | Y | Y | V-03+ adds step 3 to recovery |
| C-36 (enumerated entry conditions by name) | Y | N | N | Y | Y | V-01+ names each checklist item |
| C-37 (ROLE CARD declaration tables) | N | Y | N | N | Y | V-02 and V-05 only |
| New criteria total | 1 | 1 | 1 | 2 | 3 | V-05 is full stack |

**Predicted champion**: V-05 — highest criterion coverage, all three new criteria satisfied,
ROLE CARD tables add zero execution overhead (declaration only), enumerated entry conditions
are mechanical and do not inflate stage body length.

**Risk in V-01/V-04**: Enumerated entry conditions at Stage 5 grow to 10 items — verify
that item count does not cause C-36 to be evaluated as "holistic reference" rather than
truly individual enumeration.

**Risk in V-02**: ROLE CARD entry condition cells are compressed summaries, not full
individual enumerations — C-36 may not pass for V-02 because the ROLE CARD row says
"Stage N checklist items 1-8 each confirmed" rather than enumerating them. V-05 resolves
this by having both ROLE CARD summary and full enumerated entry conditions in the stage
execution section.
