import pathlib

golden_path = pathlib.Path(r"C:\src\sim\simulations\quest\golden\prove-topic-variate-R13-2026-03-16.md")

golden_content = r"""# prove-topic — Variate Round 13

**Skill**: prove-topic
**Rubric**: v10 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-34 aspirational)
**Date**: 2026-03-16
**Round**: 13

---

## Context: what informed this round

The existing `prove-topic.t3/SKILL.md` (R12 champion) uses a different stage sequence
(hypothesis → websearch → interview → prototype → synthesis) and does not have:
- `stages_completed` YAML accumulation (C-21)
- PATH CHAIN VERIFICATION tables (C-30)
- Dual-output trigger embedded inside completion checklists (C-31)
- `status_quo_comparator` + `inertia_vulnerability` in every artifact's YAML (C-34)
- THIN flags naming displacement claims against the incumbent (C-33)
- Consistent naming root between write paths and `stages_completed` identifiers (C-27)

R13 targets the correct rubric sequence (prove-hypothesis → prove-websearch →
prove-intelligence → prove-analysis → prove-synthesize) and pushes on three axes:

| Var | Axis | Primary criteria targeted |
|-----|------|--------------------------|
| V-01 | Lifecycle emphasis | C-15, C-19, C-21, C-22, C-25, C-26, C-27, C-29, C-30, C-31 |
| V-02 | Inertia framing | C-32, C-33, C-34 |
| V-03 | Role sequence (scout as structural gate) | C-06, C-07, C-10 |
| V-04 | Lifecycle + Inertia (combined) | C-15, C-19–C-22, C-25–C-27, C-29–C-34 |
| V-05 | Role sequence + Format (combined) | C-10, C-18, C-19, C-24, C-28, C-30 |

**Artifact paths** (all variations):

| Stage | Signal | Path |
|-------|--------|------|
| 1 | prove-hypothesis | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` |
| 2 | prove-websearch | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` |
| 3 | prove-intelligence | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |
| 4 | prove-analysis | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` |
| 5 | prove-synthesize | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md` |

---

## V-01 — Lifecycle Emphasis

**Axis**: Lifecycle emphasis
**Hypothesis**: Making every stage boundary mechanically explicit — named completion
checklists, gate clearance strings carrying artifact paths, PATH CHAIN VERIFICATION
tables at each transition, and a dual-output trigger embedded as the final checklist
item — maximizes structural/format criterion coverage without adding displacement framing.

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

1. Locate: `simulations/scout/{topic}-scout-*.md` — use most recent by date if multiple.
   - If none found: emit BLOCKED. No scout artifact for topic `{topic}`. Run a scout
     skill first. Halt.
2. Set scout_anchor = full path of found file.
3. Read the artifact. Note the key feasibility finding that will ground Stage 1.

Emit:

  CAMPAIGN OPEN.
  scout_anchor: simulations/scout/{topic}-scout-{date}.md

Stage 1 cannot begin until CAMPAIGN OPEN is emitted with scout_anchor confirmed.

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN emitted. scout_anchor confirmed.
  [ ] (Or: RESUMING CAMPAIGN with `stage-1-hypothesis` absent from stages_completed.)

WORK: Frame the central testable claim for {topic}. Ground the hypothesis in the
scout artifact. Reference scout_anchor as a cited path in the artifact body AND in
the `scout_anchor:` YAML frontmatter field.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-hypothesis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis]

STAGE 1 COMPLETION CHECKLIST:
  [ ] Hypothesis stated as a falsifiable claim
  [ ] scout_anchor path cited in artifact body
  [ ] scout_anchor field present in YAML frontmatter
  [ ] stages_completed: [stage-1-hypothesis] in YAML frontmatter
  [ ] Artifact written to simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  [ ] When all items above are checked: (1) confirm stage-1-hypothesis in stages_completed;
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
  [ ] (Or: RESUMING CAMPAIGN with stage-2-websearch absent from stages_completed.)

WORK: Gather external evidence relevant to the hypothesis. Assess each source.
Flag thin or absent evidence immediately at the point of discovery — do not defer flags:

  THIN: [area] — [what is weak or absent] — weakens sub-claim: [hypothesis element]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-websearch
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch]

STAGE 2 COMPLETION CHECKLIST:
  [ ] Minimum 3 external sources gathered and assessed
  [ ] All THIN flags emitted inline at point of discovery (not deferred)
  [ ] scout_anchor carried in YAML frontmatter
  [ ] stages_completed accumulates stage-2-websearch
  [ ] Artifact written to simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  [ ] When all items above are checked: (1) confirm stage-2-websearch appended to
      stages_completed; (2) emit GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
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
  [ ] (Or: RESUMING CAMPAIGN with stage-3-intelligence absent from stages_completed.)

WORK: Scan internal sources — existing signal artifacts, prior runs, related topics —
for evidence relevant to the hypothesis. Flag thin or absent evidence immediately:

  THIN: [area] — [what is weak or absent] — weakens sub-claim: [hypothesis element]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-intelligence
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]

STAGE 3 COMPLETION CHECKLIST:
  [ ] Internal sources scanned and assessed
  [ ] All THIN flags emitted inline at point of discovery (not deferred)
  [ ] scout_anchor carried in YAML frontmatter
  [ ] stages_completed accumulates stage-3-intelligence
  [ ] Artifact written to simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  [ ] When all items above are checked: (1) confirm stage-3-intelligence appended to
      stages_completed; (2) emit GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
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
  [ ] (Or: RESUMING CAMPAIGN with stage-4-analysis absent from stages_completed.)

WORK: Two parts separated by GATE-4A.

PART A — Flag Aggregation:
Collect all THIN flags from Stages 2 and 3 into the aggregation table:

  Flag ID | Source Stage | Area | Evidence Gap | Hypothesis Sub-Claim Weakened
  --------|-------------|------|--------------|------------------------------
  THIN-01 | Stage 2     | ...  | ...          | ...
  THIN-02 | Stage 3     | ...  | ...          | ...

If no THIN flags exist, output the table with one row: no THIN findings — — —

Emit: GATE-4A CLEARED.
Part B cannot begin until GATE-4A CLEARED. is emitted.

PART B — Hypothesis Mapping:
Map each THIN entry to the hypothesis element it weakens. Analyze overall evidence
patterns and signal quality.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-analysis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]

STAGE 4 COMPLETION CHECKLIST:
  [ ] GATE-4A emitted (aggregation table complete before mapping begins)
  [ ] All THIN flags mapped to hypothesis elements
  [ ] Data pattern analysis complete
  [ ] scout_anchor carried in YAML frontmatter
  [ ] stages_completed accumulates stage-4-analysis
  [ ] Artifact written to simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  [ ] When all items above are checked: (1) confirm stage-4-analysis appended to
      stages_completed; (2) emit GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
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
  [ ] Stage 4 completion checklist satisfied (GATE-4A emitted, all THIN flags mapped).
  [ ] (Or: RESUMING CAMPAIGN with stage-5-synthesize absent from stages_completed.)

WORK: Synthesize all evidence into a final brief. Output the confidence adjustment
table in its named form.

CONFIDENCE ADJUSTMENT TABLE — output exactly one of:

FORM A (one or more THIN flags exist):

  Weak Claim | Source Stage | Evidence Gap | Adjusted Confidence
  -----------|-------------|--------------|--------------------
  [claim]    | Stage N      | [gap]        | [Low / Medium / High]

FORM B (zero THIN flags):

  Weak Claim    | Source Stage | Evidence Gap | Adjusted Confidence
  --------------|-------------|--------------|--------------------
  no THIN findings | —         | —            | n/a

Label the form: FORM A or FORM B appears as a heading above the table.

State explicitly: This evidence brief is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-synthesize
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence,
                     stage-4-analysis, stage-5-synthesize]

STAGE 5 COMPLETION CHECKLIST:
  [ ] All evidence synthesized
  [ ] Confidence adjustment table output as FORM A or FORM B (form name labeled above table)
  [ ] /topic-story named as explicit next step
  [ ] scout_anchor carried in YAML frontmatter
  [ ] All 5 stage identifiers present in stages_completed
  [ ] Artifact written to simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
  [ ] When all items above are checked: emit GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
      Campaign complete.
```

---

## V-02 — Inertia Framing

**Axis**: Inertia framing
**Hypothesis**: Opening with a CAMPAIGN OPEN block that extracts `status_quo_comparator`
and `inertia_vulnerability` from the scout artifact, then threading both fields through
every stage's YAML and framing all THIN flags as displacement claims against the named
incumbent, achieves maximum displacement-framing criterion coverage (C-32, C-33, C-34)
with minimal structural overhead.

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
prove-analysis -> prove-synthesize. Opens with CAMPAIGN OPEN to name the incumbent
and its vulnerability before hypothesis work begins. Writes one artifact per stage.
Final output: a synthesized evidence brief ready for /topic-story.

---

## CAMPAIGN OPEN

Before Stage 1 begins:

1. Locate: `simulations/scout/{topic}-scout-*.md` — most recent by date if multiple.
   - If none: emit BLOCKED. No scout artifact for `{topic}`. Run a scout skill first. Halt.
2. Set scout_anchor = full path of found file.
3. Read the artifact. Extract two named fields:
   - status_quo_comparator — the incumbent solution or practice that {topic} would
     displace. Name it concretely (e.g., "manual spreadsheet tracking", "existing
     API gateway vendor", "ad-hoc CLI tooling"). Do not use abstract terms.
   - inertia_vulnerability — the specific resistance point that makes displacement
     non-trivial (e.g., "team familiarity with current tooling", "migration cost",
     "existing vendor contracts"). Concretely named.
   If the scout artifact does not make these explicit, infer from available signals
   and flag the inference.

Emit:

  CAMPAIGN OPEN.
  scout_anchor:            simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator:   [named incumbent]
  inertia_vulnerability:   [named resistance point]

No stage work begins until CAMPAIGN OPEN is emitted with both fields named.
All subsequent evidence framing, THIN flags, and synthesis claims are framed as
displacement claims against status_quo_comparator.

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN emitted. status_quo_comparator and inertia_vulnerability named.

WORK: Frame the central testable claim for {topic} as a displacement claim:
"{topic} displaces {status_quo_comparator} because [mechanism], despite
{inertia_vulnerability}."

Reference scout_anchor as a cited path in both the artifact body and the
`scout_anchor:` YAML frontmatter field. Ground the hypothesis in the scout finding
that makes displacement plausible.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-hypothesis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent from CAMPAIGN OPEN]
  inertia_vulnerability: [named resistance point from CAMPAIGN OPEN]
  stages_completed: [stage-1-hypothesis]

Emit: GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 — WEBSEARCH

ENTRY CONDITIONS:
  [ ] GATE-1 CLEARED.

WORK: Gather external evidence. For each source, assess whether it supports the
displacement claim against status_quo_comparator.

Flag thin or absent evidence immediately at the point of discovery. Every THIN flag
body must name the incumbent explicitly:

  THIN: [area] — [gap] — weakens displacement claim against {status_quo_comparator}: [specific claim element]

Generic sub-claim references without naming the incumbent are not sufficient.
Do not defer flags to synthesis.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-websearch
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [named incumbent]
  inertia_vulnerability: [named resistance point]
  stages_completed: [stage-1-hypothesis, stage-2-websearch]

Emit: GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

ENTRY CONDITIONS:
  [ ] GATE-2 CLEARED.

WORK: Scan internal sources — existing signal artifacts, prior runs, related topics —
for evidence relevant to the displacement hypothesis. Flag thin or absent evidence
immediately, naming the incumbent in every flag body:

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

Emit: GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

ENTRY CONDITIONS:
  [ ] GATE-3 CLEARED.

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

Emit: GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIZE

ENTRY CONDITIONS:
  [ ] GATE-4 CLEARED.

WORK: Synthesize all evidence. State whether the displacement case is proven,
partially proven, or not proven. For THIN-flagged claims, assign adjusted confidence.

CONFIDENCE ADJUSTMENT TABLE — output exactly one named form:

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

Emit: GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Campaign complete.
```

---

## V-03 — Role Sequence (Scout as Structural Gate)

**Axis**: Role sequence
**Hypothesis**: Elevating the scout review to a named SCOUT ANCHOR REVIEW role with
its own identity, structured outputs, and a named clearance string (SCOUT-GATE CLEARED.)
that Stage 1 entry conditions must list explicitly makes the forward-only gate structural
rather than advisory — the dependency is enforced by named output requirements, not
prose guidance.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Executes six roles in strict sequence:
scout-anchor-review -> prove-hypothesis -> prove-websearch -> prove-intelligence ->
prove-analysis -> prove-synthesize. The Scout Anchor Review role is a structural
first-class gate: no hypothesis work begins until SCOUT-GATE CLEARED. is emitted.
Writes one artifact per evidence role (Roles 1–5). Final output: a synthesized
evidence brief ready for /topic-story.

---

## ROLE 0 — SCOUT ANCHOR REVIEW

This role is the campaign entry gate. Roles 1–5 cannot begin until SCOUT-GATE CLEARED.
is emitted. This is a structural block: Stage 1 entry conditions list SCOUT-GATE CLEARED.
as a required named output, not as advisory guidance.

WORK:
1. Locate: `simulations/scout/{topic}-scout-*.md`
   - Multiple files: select most recent by date in filename.
   - None found: emit BLOCKED. Scout Anchor Review cannot complete — no scout artifact
     for `{topic}`. Run a scout skill first. Halt.
2. Read the artifact fully.
3. Extract and state:
   - key_finding: the central feasibility conclusion (one sentence)
   - signal_strength: strong / moderate / weak / absent (your assessment of evidence quality)
   - scout_anchor: full file path

Emit the Scout Anchor Review clearance:

  SCOUT ANCHOR REVIEW COMPLETE.
  topic:            {topic}
  scout_anchor:     simulations/scout/{topic}-scout-{date}.md
  key_finding:      [one-sentence summary]
  signal_strength:  [strong | moderate | weak | absent]
  SCOUT-GATE CLEARED.

Role 1 entry condition names SCOUT-GATE CLEARED. as a required string. If that
string is absent from context, Role 1 emits: BLOCKED at Role 1 — SCOUT-GATE CLEARED.
required. Ensure Role 0 has run.

---

## ROLE 1 — PROVE-HYPOTHESIS

ENTRY CONDITIONS:
  [ ] SCOUT-GATE CLEARED. received (Role 0 complete).
  [ ] scout_anchor, key_finding, and signal_strength named in Role 0 output.

If SCOUT-GATE CLEARED. is absent: emit BLOCKED at Role 1 — SCOUT-GATE CLEARED.
required. Do not proceed.

WORK: Frame the central testable claim for {topic}. Ground the hypothesis in
key_finding from Role 0. Note any confidence impact if signal_strength is weak
or absent. Reference scout_anchor as a cited path in both the artifact body and
in the `scout_anchor:` YAML frontmatter field.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-hypothesis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  scout_signal_strength: [strong | moderate | weak | absent]
  stages_completed: [stage-1-hypothesis]

Emit: GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## ROLE 2 — PROVE-WEBSEARCH

ENTRY CONDITIONS:
  [ ] GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
      received.

WORK: Gather external evidence relevant to the hypothesis. Assess each source.
Flag thin or absent evidence immediately at the point of discovery:

  THIN: [area] — [gap] — weakens sub-claim: [hypothesis element]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-websearch
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch]

Emit: GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## ROLE 3 — PROVE-INTELLIGENCE

ENTRY CONDITIONS:
  [ ] GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
      received.

WORK: Scan internal sources — existing signal artifacts, prior runs, related topics —
for evidence relevant to the hypothesis. Flag thin or absent evidence immediately:

  THIN: [area] — [gap] — weakens sub-claim: [hypothesis element]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-intelligence
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]

Emit: GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## ROLE 4 — PROVE-ANALYSIS

ENTRY CONDITIONS:
  [ ] GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
      received.

WORK: Two parts.

PART A — Flag Aggregation:
Collect all THIN flags from Roles 2–3:

  Flag ID | Role | Area | Evidence Gap | Hypothesis Sub-Claim Weakened
  --------|------|------|--------------|------------------------------
  THIN-01 | 2    | ...  | ...          | ...
  THIN-02 | 3    | ...  | ...          | ...

If no THIN flags: no THIN findings row.

Emit: GATE-4A CLEARED.

PART B — Hypothesis Mapping (requires GATE-4A CLEARED.):
Map each THIN flag to the hypothesis element it weakens. Analyze patterns.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-analysis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]

Emit: GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## ROLE 5 — PROVE-SYNTHESIZE

ENTRY CONDITIONS:
  [ ] GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
      received. Role 4 completion checklist satisfied: GATE-4A emitted and all THIN
      flags mapped.

WORK: Synthesize all evidence. For THIN-flagged claims, assign adjusted confidence.

CONFIDENCE ADJUSTMENT TABLE:

FORM A (THIN flags exist):

  Weak Claim | Source Role | Evidence Gap | Adjusted Confidence
  -----------|-------------|--------------|--------------------
  [claim]    | Role N       | [gap]        | [Low / Med / High]

FORM B (no THIN flags):

  Weak Claim       | Source Role | Evidence Gap | Adjusted Confidence
  -----------------|-------------|--------------|--------------------
  no THIN findings | —           | —            | n/a

State explicitly: This evidence brief is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

YAML FRONTMATTER (required):
  topic: {topic}
  date: {date}
  signal: prove-synthesize
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence,
                     stage-4-analysis, stage-5-synthesize]

Emit: GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Campaign complete.
```

---

## V-04 — Lifecycle + Inertia (Combined)

**Axis**: Lifecycle emphasis + Inertia framing
**Hypothesis**: Combining full checklist/gate machinery (PATH CHAIN VERIFICATION tables,
dual-output trigger inside each checklist, consistent naming roots, Stage N+1 entry
conditions naming Stage N's checklist outputs) with CAMPAIGN OPEN displacement framing
(status_quo_comparator + inertia_vulnerability in every artifact's YAML, THIN flags
naming the incumbent) achieves the widest aspirational criterion coverage of any
single variation.

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
prove-analysis -> prove-synthesize. Opens with CAMPAIGN OPEN to name the incumbent
and resistance point. Writes one artifact per stage with full gate/checklist machinery.
Final output: a synthesized evidence brief ready for /topic-story.

---

## INTERRUPTED CAMPAIGN RECOVERY

If resuming a campaign that was interrupted:

1. Find the most recent artifact in `simulations/prove/` for this topic.
2. Read its `stages_completed` YAML field — this is the machine-readable audit trail.
3. Also read status_quo_comparator and inertia_vulnerability from that artifact's YAML
   to recover displacement framing without re-parsing the preamble.
4. Check which gate clearance strings are absent from context to identify the next stage.
5. Resume from the first stage whose identifier is absent from `stages_completed`.
6. Emit: RESUMING CAMPAIGN. stages_completed = [...]. status_quo_comparator = [value].
   Next stage: Stage N — [name].
7. Apply normal entry conditions from that stage forward.

---

## CAMPAIGN OPEN

Before Stage 1 begins:

1. Locate: `simulations/scout/{topic}-scout-*.md` — most recent by date if multiple.
   - If none: emit BLOCKED. No scout artifact for `{topic}`. Run a scout skill first. Halt.
2. Set scout_anchor = full path of found file.
3. Read the artifact. Extract:
   - status_quo_comparator — the incumbent solution this topic displaces. Name it
     concretely. Do not use abstract terms.
   - inertia_vulnerability — the specific resistance point making displacement
     non-trivial. Concretely named.
   If not explicit in the scout artifact, infer and flag the inference.

Emit:

  CAMPAIGN OPEN.
  scout_anchor:            simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator:   [named incumbent]
  inertia_vulnerability:   [named resistance point]

Stage 1 cannot begin until CAMPAIGN OPEN is emitted with all three fields confirmed.
All THIN flags in Stages 2–3 frame evidence gaps as displacement claims against
status_quo_comparator. Both fields carry into every stage's YAML frontmatter.

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN emitted. scout_anchor, status_quo_comparator, inertia_vulnerability confirmed.
  [ ] (Or: RESUMING CAMPAIGN with stage-1-hypothesis absent from stages_completed.)

WORK: Frame the central testable claim as a displacement claim:
"{topic} displaces {status_quo_comparator} because [mechanism], despite
{inertia_vulnerability}."
Reference scout_anchor as a cited path in the artifact body AND in `scout_anchor:`
YAML frontmatter field. Ground the claim in the scout finding.

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
  [ ] Hypothesis stated as displacement claim naming status_quo_comparator
  [ ] scout_anchor path cited in artifact body
  [ ] scout_anchor field in YAML frontmatter
  [ ] status_quo_comparator and inertia_vulnerability in YAML frontmatter
  [ ] stages_completed: [stage-1-hypothesis] in YAML frontmatter
  [ ] Artifact written to simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  [ ] When all items above are checked: (1) confirm stage-1-hypothesis in stages_completed;
      (2) emit GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
      Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 1 -> 2:

  Channel                    | Path
  ---------------------------|---------------------------------------------------------------------------
  Write instruction (Stg 1)  | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Gate clearance (GATE-1)    | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Stage 2 entry confirmation | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## STAGE 2 — WEBSEARCH

ENTRY CONDITIONS:
  [ ] GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
      received and path confirmed.
  [ ] Stage 1 completion checklist satisfied: hypothesis stated, scout_anchor cited,
      status_quo_comparator and inertia_vulnerability in YAML, stages_completed updated,
      artifact written to path in GATE-1 clearance string.
  [ ] (Or: RESUMING CAMPAIGN with stage-2-websearch absent from stages_completed.)

WORK: Gather external evidence. For each source, assess whether it supports the
displacement claim against status_quo_comparator.

Flag thin or absent evidence immediately at the point of discovery. Every THIN flag
body names the incumbent explicitly:

  THIN: [area] — [gap] — weakens displacement claim against {status_quo_comparator}: [specific claim element]

Do not defer flags. Do not use generic sub-claim references without naming the incumbent.

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
  [ ] Minimum 3 external sources gathered and assessed
  [ ] All THIN flags emitted inline, each naming status_quo_comparator
  [ ] scout_anchor, status_quo_comparator, inertia_vulnerability in YAML frontmatter
  [ ] stages_completed accumulates stage-2-websearch
  [ ] Artifact written to simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  [ ] When all items above are checked: (1) confirm stage-2-websearch appended to
      stages_completed; (2) emit GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
      Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 2 -> 3:

  Channel                    | Path
  ---------------------------|--------------------------------------------------------------------------
  Write instruction (Stg 2)  | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Gate clearance (GATE-2)    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Stage 3 entry confirmation | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 — INTELLIGENCE

ENTRY CONDITIONS:
  [ ] GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
      received and path confirmed.
  [ ] Stage 2 completion checklist satisfied: sources gathered, THIN flags naming
      status_quo_comparator emitted, YAML fields carried, stages_completed updated,
      artifact written to path in GATE-2 clearance string.
  [ ] (Or: RESUMING CAMPAIGN with stage-3-intelligence absent from stages_completed.)

WORK: Scan internal sources for evidence relevant to the displacement hypothesis.
Flag thin or absent evidence immediately, naming the incumbent in every flag body:

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
  [ ] Internal sources scanned and assessed
  [ ] All THIN flags emitted inline, each naming status_quo_comparator
  [ ] scout_anchor, status_quo_comparator, inertia_vulnerability in YAML frontmatter
  [ ] stages_completed accumulates stage-3-intelligence
  [ ] Artifact written to simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  [ ] When all items above are checked: (1) confirm stage-3-intelligence appended to
      stages_completed; (2) emit GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
      Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 3 -> 4:

  Channel                    | Path
  ---------------------------|-----------------------------------------------------------------------------
  Write instruction (Stg 3)  | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Gate clearance (GATE-3)    | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Stage 4 entry confirmation | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 — ANALYSIS

ENTRY CONDITIONS:
  [ ] GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
      received and path confirmed.
  [ ] Stage 3 completion checklist satisfied: sources scanned, THIN flags naming
      status_quo_comparator emitted, YAML fields carried, stages_completed updated,
      artifact written to path in GATE-3 clearance string.
  [ ] (Or: RESUMING CAMPAIGN with stage-4-analysis absent from stages_completed.)

WORK: Two parts separated by GATE-4A.

PART A — Flag Aggregation:
Collect all THIN flags from Stages 2–3. The final column names the displacement
claim against status_quo_comparator that is weakened:

  Flag ID | Stage | Area | Evidence Gap | Displacement Claim Weakened (vs. {status_quo_comparator})
  --------|-------|------|--------------|----------------------------------------------------------
  THIN-01 | 2     | ...  | ...          | ...
  THIN-02 | 3     | ...  | ...          | ...

If no THIN flags: one row — no THIN findings — — —

Emit: GATE-4A CLEARED.
Part B cannot begin until GATE-4A CLEARED. is emitted.

PART B — Hypothesis Mapping:
Map each THIN entry to the displacement claim it weakens against status_quo_comparator.
Assess the overall case that {topic} outperforms {status_quo_comparator} despite
{inertia_vulnerability}.

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
  [ ] GATE-4A emitted (aggregation table complete before mapping begins)
  [ ] All THIN flags mapped to displacement claims vs. status_quo_comparator
  [ ] Data pattern analysis complete
  [ ] scout_anchor, status_quo_comparator, inertia_vulnerability in YAML frontmatter
  [ ] stages_completed accumulates stage-4-analysis
  [ ] Artifact written to simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  [ ] When all items above are checked: (1) confirm stage-4-analysis appended to
      stages_completed; (2) emit GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
      Single event, both outputs.

PATH CHAIN VERIFICATION — Transition 4 -> 5:

  Channel                    | Path
  ---------------------------|-------------------------------------------------------------------
  Write instruction (Stg 4)  | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Gate clearance (GATE-4)    | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Stage 5 entry confirmation | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 — SYNTHESIZE

ENTRY CONDITIONS:
  [ ] GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
      received and path confirmed.
  [ ] Stage 4 completion checklist satisfied: GATE-4A emitted, all THIN flags mapped
      to displacement claims, YAML fields carried, stages_completed updated, artifact
      written to path in GATE-4 clearance string.
  [ ] (Or: RESUMING CAMPAIGN with stage-5-synthesize absent from stages_completed.)

WORK: Synthesize all evidence. State whether the displacement case is proven,
partially proven, or not proven. For THIN-flagged claims, assign adjusted confidence.

CONFIDENCE ADJUSTMENT TABLE — output exactly one named form:

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
  [ ] All evidence synthesized
  [ ] Confidence adjustment table output as FORM A or FORM B (form name labeled above table)
  [ ] /topic-story named as explicit next step
  [ ] scout_anchor, status_quo_comparator, inertia_vulnerability in YAML frontmatter
  [ ] All 5 stage identifiers present in stages_completed
  [ ] Artifact written to simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
  [ ] When all items above are checked: emit GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
      Campaign complete.
```

---

## V-05 — Role Sequence + Format (Combined)

**Axis**: Role sequence + Output format (table-forward presentation)
**Hypothesis**: Structuring the skill as a table-first execution guide — where each
role's inputs, outputs, write target, and gate clearance are declared in named tables
before prose instructions — makes the campaign auditable from a visual scan, hits
C-18 (named dual-form schema), C-24 (recovery as a table), and C-30 (path chain as
a named table) while the elevated scout role (V-03 axis) ensures the structural
gate dependency is visible at a glance.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Six roles in strict order:
scout-anchor-review -> prove-hypothesis -> prove-websearch -> prove-intelligence ->
prove-analysis -> prove-synthesize. Each role declared via a ROLE CARD table before
execution. Writes one artifact per evidence role (Roles 1–5). Final output: a
synthesized evidence brief ready for /topic-story.

---

## CAMPAIGN REGISTRY TABLE

  Role | Name                | Entry Requires          | Write Path                                                               | Gate Emitted
  -----|---------------------|-------------------------|--------------------------------------------------------------------------|-------------
  R0   | Scout Anchor Review | — (first)               | none                                                                     | SCOUT-GATE CLEARED.
  R1   | Prove-Hypothesis    | SCOUT-GATE CLEARED.     | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md    | GATE-1 CLEARED.
  R2   | Prove-Websearch     | GATE-1 CLEARED.         | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md      | GATE-2 CLEARED.
  R3   | Prove-Intelligence  | GATE-2 CLEARED.         | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md | GATE-3 CLEARED.
  R4   | Prove-Analysis      | GATE-3 CLEARED.         | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md        | GATE-4 CLEARED.
  R5   | Prove-Synthesize    | GATE-4 CLEARED.         | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md    | GATE-5 CLEARED.

Every gate clearance string carries the artifact path written at that role:
  GATE-N CLEARED. -> {write path from row N above}

---

## RECOVERY TABLE

To resume an interrupted campaign:

  Step | Action
  -----|-------
  1    | Find most recent artifact in `simulations/prove/` for this topic
  2    | Read its `stages_completed` YAML field — identify completed stages
  3    | Find first stage identifier absent from `stages_completed` — that is the resume point
  4    | Check CAMPAIGN REGISTRY TABLE row for that stage — confirm gate clearance from prior row
  5    | Emit: RESUMING CAMPAIGN. stages_completed = [...]. Next: Role N — [name].
  6    | Execute from resume point with normal entry conditions applied

---

## ROLE 0 — SCOUT ANCHOR REVIEW

ROLE CARD:

  Field          | Value
  ---------------|----------------------------------------------------------
  Entry requires | — (first role)
  Outputs        | scout_anchor path, key_finding, signal_strength
  Gate emitted   | SCOUT-GATE CLEARED.
  Blocks         | All roles 1–5 (structural dependency, not advisory)

EXECUTION:
Locate `simulations/scout/{topic}-scout-*.md`. Select most recent by date.
If none: emit BLOCKED. No scout artifact for `{topic}`. Halt.

Read the artifact. Fill the Scout Anchor Review output:

  SCOUT ANCHOR REVIEW COMPLETE.
  scout_anchor:    simulations/scout/{topic}-scout-{date}.md
  key_finding:     [one-sentence feasibility conclusion]
  signal_strength: [strong | moderate | weak | absent]
  SCOUT-GATE CLEARED.

Role 1 entry condition requires the string SCOUT-GATE CLEARED. in context.

---

## ROLE 1 — PROVE-HYPOTHESIS

ROLE CARD:

  Field                | Value
  ---------------------|----------------------------------------------------------------------
  Entry requires       | SCOUT-GATE CLEARED. + scout_anchor, key_finding, signal_strength named
  Write target         | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  stages_completed id  | stage-1-hypothesis
  Gate emitted         | GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

EXECUTION:
If SCOUT-GATE CLEARED. absent: emit BLOCKED at Role 1. Do not proceed.

Frame the central testable claim for {topic}, grounded in key_finding. Reference
scout_anchor in the artifact body and in `scout_anchor:` YAML field.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

YAML FRONTMATTER:
  topic: {topic}
  date: {date}
  signal: prove-hypothesis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  scout_signal_strength: [value from R0]
  stages_completed: [stage-1-hypothesis]

PATH CHAIN — R1 -> R2:

  Channel                   | Path
  --------------------------|--------------------------------------------------------------------------
  Write instruction (R1)    | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Gate clearance (GATE-1)   | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  R2 entry confirmation     | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Emit: GATE-1 CLEARED. -> simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

---

## ROLE 2 — PROVE-WEBSEARCH

ROLE CARD:

  Field                | Value
  ---------------------|-------------------------------------------------------------------
  Entry requires       | GATE-1 CLEARED. -> [path]. Path confirmed against PATH CHAIN R1->R2.
  Write target         | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  stages_completed id  | stage-2-websearch
  Gate emitted         | GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

EXECUTION:
Gather external evidence. Flag thin evidence immediately:

  THIN: [area] — [gap] — weakens sub-claim: [hypothesis element]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

YAML FRONTMATTER:
  topic: {topic}
  date: {date}
  signal: prove-websearch
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch]

PATH CHAIN — R2 -> R3:

  Channel                   | Path
  --------------------------|-------------------------------------------------------------------------
  Write instruction (R2)    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Gate clearance (GATE-2)   | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  R3 entry confirmation     | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: GATE-2 CLEARED. -> simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## ROLE 3 — PROVE-INTELLIGENCE

ROLE CARD:

  Field                | Value
  ---------------------|-------------------------------------------------------------------
  Entry requires       | GATE-2 CLEARED. -> [path]. Path confirmed against PATH CHAIN R2->R3.
  Write target         | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  stages_completed id  | stage-3-intelligence
  Gate emitted         | GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

EXECUTION:
Scan internal sources. Flag thin evidence immediately:

  THIN: [area] — [gap] — weakens sub-claim: [hypothesis element]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

YAML FRONTMATTER:
  topic: {topic}
  date: {date}
  signal: prove-intelligence
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence]

PATH CHAIN — R3 -> R4:

  Channel                   | Path
  --------------------------|-----------------------------------------------------------------------------
  Write instruction (R3)    | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Gate clearance (GATE-3)   | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  R4 entry confirmation     | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: GATE-3 CLEARED. -> simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## ROLE 4 — PROVE-ANALYSIS

ROLE CARD:

  Field                | Value
  ---------------------|-------------------------------------------------------------------
  Entry requires       | GATE-3 CLEARED. -> [path]. Path confirmed against PATH CHAIN R3->R4.
  Write target         | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  stages_completed id  | stage-4-analysis
  Gate emitted         | GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

EXECUTION:

PART A — Flag Aggregation (required before Part B):

  Flag ID | Role | Area | Evidence Gap | Hypothesis Sub-Claim Weakened
  --------|------|------|--------------|------------------------------
  THIN-01 | R2   | ...  | ...          | ...
  THIN-02 | R3   | ...  | ...          | ...

If no THIN flags: one row — no THIN findings

Emit: GATE-4A CLEARED. (Part B requires this string.)

PART B — Hypothesis Mapping:
Map each THIN flag to the hypothesis element it weakens. Analyze overall patterns.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

YAML FRONTMATTER:
  topic: {topic}
  date: {date}
  signal: prove-analysis
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence, stage-4-analysis]

PATH CHAIN — R4 -> R5:

  Channel                   | Path
  --------------------------|-------------------------------------------------------------------
  Write instruction (R4)    | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Gate clearance (GATE-4)   | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  R5 entry confirmation     | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: GATE-4 CLEARED. -> simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## ROLE 5 — PROVE-SYNTHESIZE

ROLE CARD:

  Field                | Value
  ---------------------|-------------------------------------------------------------------
  Entry requires       | GATE-4 CLEARED. -> [path]. Path confirmed against PATH CHAIN R4->R5.
                       | R4 completion: GATE-4A emitted and all THIN flags mapped.
  Write target         | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
  stages_completed id  | stage-5-synthesize
  Gate emitted         | GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

EXECUTION:
Synthesize all evidence. Assign adjusted confidence to THIN-flagged claims.

CONFIDENCE ADJUSTMENT TABLE — output exactly one named form:

FORM A (one or more THIN flags):

  Weak Claim | Source Role | Evidence Gap | Adjusted Confidence
  -----------|-------------|--------------|--------------------
  [claim]    | RN          | [gap]        | [Low / Med / High]

FORM B (zero THIN flags):

  Weak Claim       | Source Role | Evidence Gap | Adjusted Confidence
  -----------------|-------------|--------------|--------------------
  no THIN findings | —           | —            | n/a

State explicitly: This evidence brief is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

YAML FRONTMATTER:
  topic: {topic}
  date: {date}
  signal: prove-synthesize
  scout_anchor: simulations/scout/{topic}-scout-{date}.md
  stages_completed: [stage-1-hypothesis, stage-2-websearch, stage-3-intelligence,
                     stage-4-analysis, stage-5-synthesize]

Emit: GATE-5 CLEARED. -> simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Campaign complete.
```
"""

golden_path.parent.mkdir(parents=True, exist_ok=True)
golden_path.write_text(golden_content, encoding='utf-8')
print(f"Written: {golden_path}")
print(f"Size: {len(golden_content)} bytes")
