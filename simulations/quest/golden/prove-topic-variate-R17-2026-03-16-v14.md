---
skill: quest-variate
skill_target: prove-topic
round: R17
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [per_stage_inertia_displacement, resume_audit, confidence_chain_count_gated]
  combined: [V-04 (per_stage_inertia + resume_audit), V-05 (all_three + full_structural_stack)]
r2_anchor: >
  R2 V-05 (100/100 against v14) established the structural stack now carried as the R17
  baseline: SCOUT READY exit signal (cannot fire without found file) + STAGE N cannot begin
  until prior signal fires + two-write Stage 5 (Write A = claim-evidence map with per-claim
  confidence, Write B = final brief + topic-story handoff) + THIN: [area] -- [gap] flags at
  point of discovery in Stages 2 and 3 + scout_source frontmatter in Stage 1 artifact.
  All five R2 100-scoring variations passed C-01 through C-10. Three new excellence signals
  emerged: exit-signal chaining as a portable C-10 block, two-write synthesis as a structural
  C-09 enforcer, role-sequence as a C-02/C-07 architecture. R2 closed v14 discrimination at
  the ceiling. R3-R16 upgraded the rubric to v15-v16. R17 revisits v14 to probe three
  post-R2 axes never applied at v14 level: per-stage inertia displacement (extend inertia
  framing from pre-stage to every evidence stage), resume audit (glob + skip completed
  stages before Stage 1), and confidence chain with count gates (numeric 1-10 chain with
  minimum source thresholds blocking stage completion).
r17_targets: >
  V-01 (single: per_stage_inertia_displacement): R1 V-04 introduced an INERTIA ANCHOR in
  the pre-stage setup. R17 V-01 extends this: each evidence stage (2, 3, 4) includes an
  INERTIA DELTA check -- a one-line structured question "Does this evidence change the
  displacement case against [status_quo]? If yes: delta = [+/-N, reason]." Stage 4 analysis
  aggregates all deltas into a displacement_verdict field. Stage 5 Write B references the
  displacement_verdict. Tests whether per-stage displacement tracking is a natural
  extension of inertia framing that surfaces a new pattern for rubric v15.

  V-02 (single: resume_audit): Before Stage 1 opens, a RESUME AUDIT globs for all five
  stage artifacts. Completed stages are marked RESUME-SKIP. The campaign resumes from the
  first RUN stage. If Stage 1 is RESUME-SKIP, the confidence prior is read from the existing
  Stage 1 artifact. Tests whether resume capability adds meaningful structural enforcement
  (a campaign that can resume must have artifact paths at every stage -- making C-05 a
  necessary precondition for resumability, not just a formatting choice).

  V-03 (single: confidence_chain_count_gated): Numeric confidence 1-10 flows through a
  chain: Stage 1 sets confidence_prior, Stages 2/3 each add a delta (s2_delta, s3_delta),
  Stage 4 sets s4_delta, Stage 5 computes confidence_final = prior + s2 + s3 + s4. Each
  evidence stage has a count gate: Stage 2 requires min 3 web sources before WEBSEARCH
  WRITTEN fires, Stage 3 requires min 2 internal signals before INTELLIGENCE WRITTEN fires.
  Count gates appear in the exit signal payload alongside confidence. Tests whether numeric
  confidence + count gates add enough structural weight to warrant new aspirational criteria.

  V-04 (combined: per_stage_inertia + resume_audit): V-01 + V-02. Inertia delta at every
  evidence stage AND resume audit before Stage 1. The INERTIA ANCHOR from pre-stage setup
  is carried into the resume state so a resumed campaign retains the displacement framing.

  V-05 (full: all_three + full_structural_stack): V-01 + V-02 + V-03 on top of the complete
  R2 V-05 structural stack (exit-signal chain, two-write synthesis, scout_source frontmatter,
  THIN-flag format). Tests whether all three new axes simultaneously produce a variation that
  saturates v14 at 100/100 AND surfaces patterns for at least two new aspirational criteria.
---

# prove-topic Variations -- Round 17 (Rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-10 aspirational)
**Date**: 2026-03-16
**Round**: R17

---

## Context: what informed this round

R2 (v14) hit the ceiling. Four of five variations scored 100/100. The R2 V-05 structural
stack (exit-signal chain + two-write synthesis + THIN flags at discovery + scout_source
frontmatter) is carried as the R17 baseline. R17 explores three new single-axis patterns
never applied at v14 level, each probing a different structural dimension:

| Var  | Axis                            | Primary target           | New pattern hypothesis                                    |
|------|---------------------------------|--------------------------|-----------------------------------------------------------|
| V-01 | Per-stage inertia displacement  | C-08, new aspirational   | INERTIA DELTA per evidence stage -> displacement_verdict  |
| V-02 | Resume audit                    | C-03, C-05, new asp.     | Resumability requires artifact paths by construction      |
| V-03 | Confidence chain + count gates  | C-09, new aspirational   | Numeric chain + count thresholds -> structural confidence |
| V-04 | V-01 + V-02                     | C-02, C-07, C-08         | Inertia anchored across resume boundary                   |
| V-05 | All three + full structural stack | All 10 + new patterns  | v15 aspirational surface attempt                          |

**Artifact paths** (all variations):

| Stage | Signal             | Path                                                                        |
|-------|--------------------|-----------------------------------------------------------------------------|
| 1     | prove-hypothesis   | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`     |
| 2     | prove-websearch    | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`       |
| 3     | prove-intelligence | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |
| 4     | prove-analysis     | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`         |
| 5     | prove-synthesize   | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`     |

---

## V-01 -- Per-Stage Inertia Displacement

**Axis**: per_stage_inertia_displacement (single)
**Hypothesis**: R1 V-04 named a status-quo comparator in the pre-stage setup. That anchor
was static -- named once, not revisited. V-01 extends inertia framing to every evidence
stage by adding a one-line INERTIA DELTA check at the end of each evidence stage (2, 3, 4).
Each check asks: "Does this evidence change the displacement case? If yes: delta = [+/-N,
reason]." Stage 4 analysis aggregates these into a displacement_verdict field. Stage 5
Write B references displacement_verdict. The hypothesis: per-stage displacement tracking
produces a more defensible displacement conclusion and surfaces a new pattern -- that
inertia framing is a first-class evidence dimension, not a setup note.

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
artifacts. Each stage has a declared exit signal. No stage begins without the prior stage's
exit signal. Inertia framing runs throughout: every evidence stage checks whether findings
shift the displacement case against the status-quo comparator.

---

## SETUP

Exit signal: SCOUT READY

To fire SCOUT READY:
- Glob `simulations/scout/{topic}-scout-*.md`
- If absent: emit "BLOCKED -- no scout artifact for {topic}. Run scout first." Halt.
  SCOUT READY cannot fire without a found file.
- Read file. Set scout_source = found path.
- Name the status-quo comparator: the incumbent approach {topic} must displace.
  inertia_anchor: [status_quo_comparator -- one sentence: why it wins today]
- Emit: SCOUT READY. scout_source = [path]. inertia_anchor = [comparator]

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 -- HYPOTHESIS

Exit signal: HYPOTHESIS WRITTEN

ENTRY: SCOUT READY must have fired. If not: halt.

Frame the central falsifiable claim for {topic}. Ground it in the scout artifact.
State clearly what evidence would falsify the hypothesis.

Frontmatter:
  scout_source: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [inertia_anchor value from SETUP]

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Emit: HYPOTHESIS WRITTEN

STAGE 2 cannot begin until HYPOTHESIS WRITTEN fires.

---

## STAGE 2 -- WEBSEARCH

Exit signal: WEBSEARCH WRITTEN

ENTRY: HYPOTHESIS WRITTEN must have fired. If not: halt.

Gather external evidence supporting or refuting the hypothesis. Assess each source.
Flag thin or absent evidence at the point of discovery -- not deferred:
  THIN: [area] -- [gap]

INERTIA DELTA: Does this external evidence change the displacement case against
[status_quo_comparator]? State:
  s2_inertia_delta: [strengthens / weakens / neutral -- one sentence reason]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Emit: WEBSEARCH WRITTEN. s2_inertia_delta = [value]

STAGE 3 cannot begin until WEBSEARCH WRITTEN fires.

---

## STAGE 3 -- INTELLIGENCE

Exit signal: INTELLIGENCE WRITTEN

ENTRY: WEBSEARCH WRITTEN must have fired. If not: halt.

Search internal signal artifacts and related topic runs for evidence relevant to
the hypothesis. Flag thin evidence inline when found:
  THIN: [area] -- [gap]

INERTIA DELTA: Does this internal evidence change the displacement case against
[status_quo_comparator]? State:
  s3_inertia_delta: [strengthens / weakens / neutral -- one sentence reason]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Emit: INTELLIGENCE WRITTEN. s3_inertia_delta = [value]

STAGE 4 cannot begin until INTELLIGENCE WRITTEN fires.

---

## STAGE 4 -- ANALYSIS

Exit signal: ANALYSIS WRITTEN

ENTRY: INTELLIGENCE WRITTEN must have fired. If not: halt.

Aggregate THIN flags from Stages 2 and 3. Map each gap to the hypothesis claim it weakens.

DISPLACEMENT AGGREGATE: Combine s2_inertia_delta and s3_inertia_delta. State the
overall displacement verdict:
  displacement_verdict: [favors {topic} / favors status_quo / inconclusive -- two sentences]

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Emit: ANALYSIS WRITTEN. displacement_verdict = [value]

STAGE 5 cannot begin until ANALYSIS WRITTEN fires.

---

## STAGE 5 -- SYNTHESIS

Exit signal: CAMPAIGN COMPLETE

ENTRY: ANALYSIS WRITTEN must have fired. If not: halt.

### Write A -- Claim Evidence Map

For each hypothesis claim:
- State evidence strength: strong / moderate / thin
- If thin: name source stage, weakened claim, and adjusted confidence
  (e.g., "Confidence reduced -- Stage 2 found no peer data for claim X")

Write A: simulations/prove/prove-synthesize/{topic}-prove-synthesize-draft-{date}.md

### Write B -- Evidence Brief

State verdict: supported / partially supported / not supported.
Reference Write A for claim-level detail.
Reference displacement_verdict from Stage 4 analysis.

Close: Evidence brief for {topic} is ready for /topic-story.

Write B: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Emit: CAMPAIGN COMPLETE
```

---

## V-02 -- Resume Audit

**Axis**: resume_audit (single)
**Hypothesis**: Adding a RESUME AUDIT before Stage 1 -- glob all five stage artifact paths,
mark each DONE or MISSING, resume from the first MISSING -- makes the artifact paths in
C-05 a structural necessity rather than a formatting choice. A campaign that can resume
must have deterministic artifact paths; resumability enforces path discipline by
construction. The audit also changes the scout-loading behavior: if Stage 1 is DONE,
confidence_prior is read from the existing Stage 1 artifact, preserving chain integrity
across sessions.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages. Resumable: a pre-run audit
marks completed stages RESUME-SKIP. Stage 5 produces two artifacts. Each stage has a
declared exit signal. No stage begins without the prior stage's exit signal.

---

## SETUP

Exit signal: SCOUT READY

To fire SCOUT READY:
- Glob `simulations/scout/{topic}-scout-*.md`
- If absent: emit "BLOCKED -- no scout artifact for {topic}. Run scout first." Halt.
  SCOUT READY cannot fire without a found file.
- Read file. Set scout_source = found path.
- Emit: SCOUT READY. scout_source = [path]

RESUME AUDIT cannot begin until SCOUT READY fires.

---

## RESUME AUDIT

Glob for existing stage artifacts:

  s1: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  s2: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  s3: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  s4: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  s5: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

Mark each DONE or MISSING.

  s1_status: [RESUME-SKIP / RUN]
  s2_status: [RESUME-SKIP / RUN]
  s3_status: [RESUME-SKIP / RUN]
  s4_status: [RESUME-SKIP / RUN]
  s5_status: [RESUME-SKIP / RUN]

Resume from the first RUN stage. If s1_status = RESUME-SKIP: read the Stage 1 artifact
and carry its scout_source value forward.

Emit: AUDIT COMPLETE. resuming_from = Stage [N]

STAGE 1 cannot begin until AUDIT COMPLETE fires.

---

## STAGE 1 -- HYPOTHESIS

Exit signal: HYPOTHESIS WRITTEN

ENTRY: AUDIT COMPLETE must have fired. If not: halt.
If s1_status = RESUME-SKIP: emit HYPOTHESIS WRITTEN (prior artifact found). Advance to Stage 2.

Frame the central falsifiable claim for {topic}. Ground it in the scout artifact.

Frontmatter:
  scout_source: simulations/scout/{topic}-scout-{date}.md

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Emit: HYPOTHESIS WRITTEN

STAGE 2 cannot begin until HYPOTHESIS WRITTEN fires.

---

## STAGE 2 -- WEBSEARCH

Exit signal: WEBSEARCH WRITTEN

ENTRY: HYPOTHESIS WRITTEN must have fired. If not: halt.
If s2_status = RESUME-SKIP: emit WEBSEARCH WRITTEN (prior artifact found). Advance to Stage 3.

Gather external evidence. Flag thin findings at point of discovery -- not deferred:
  THIN: [area] -- [gap]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Emit: WEBSEARCH WRITTEN

STAGE 3 cannot begin until WEBSEARCH WRITTEN fires.

---

## STAGE 3 -- INTELLIGENCE

Exit signal: INTELLIGENCE WRITTEN

ENTRY: WEBSEARCH WRITTEN must have fired. If not: halt.
If s3_status = RESUME-SKIP: emit INTELLIGENCE WRITTEN (prior artifact found). Advance to Stage 4.

Search internal signal artifacts for evidence relevant to the hypothesis. Flag thin findings:
  THIN: [area] -- [gap]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Emit: INTELLIGENCE WRITTEN

STAGE 4 cannot begin until INTELLIGENCE WRITTEN fires.

---

## STAGE 4 -- ANALYSIS

Exit signal: ANALYSIS WRITTEN

ENTRY: INTELLIGENCE WRITTEN must have fired. If not: halt.
If s4_status = RESUME-SKIP: emit ANALYSIS WRITTEN (prior artifact found). Advance to Stage 5.

Aggregate THIN flags from Stages 2 and 3. Map each gap to the hypothesis claim it weakens.

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Emit: ANALYSIS WRITTEN

STAGE 5 cannot begin until ANALYSIS WRITTEN fires.

---

## STAGE 5 -- SYNTHESIS

Exit signal: CAMPAIGN COMPLETE

ENTRY: ANALYSIS WRITTEN must have fired. If not: halt.

### Write A -- Claim Evidence Map

For each hypothesis claim:
- State evidence strength: strong / moderate / thin
- If thin: name source stage and adjusted confidence

Write A: simulations/prove/prove-synthesize/{topic}-prove-synthesize-draft-{date}.md

### Write B -- Evidence Brief

State verdict: supported / partially supported / not supported.
Reference Write A for claim-level detail.

Close: Evidence brief for {topic} is ready for /topic-story.

Write B: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Emit: CAMPAIGN COMPLETE
```

---

## V-03 -- Confidence Chain with Count Gates

**Axis**: confidence_chain_count_gated (single)
**Hypothesis**: Adding a numeric confidence chain (1-10, flowing from Stage 1 through Stage
5 as a running sum of deltas) AND per-stage count gates (Stage 2 requires at least 3 web
sources before WEBSEARCH WRITTEN fires; Stage 3 requires at least 2 internal signals) makes
C-09 structural by chain construction and introduces a new pattern -- that evidence
sufficiency is enforced numerically before synthesis begins. The count gate appears in the
exit signal payload, making it visible at every stage boundary.

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
artifacts. Confidence flows numerically 1-10 as a running chain. Each evidence stage has
a minimum count gate; the exit signal cannot fire until the gate clears. No stage begins
without the prior stage's exit signal.

---

## SETUP

Exit signal: SCOUT READY

To fire SCOUT READY:
- Glob `simulations/scout/{topic}-scout-*.md`
- If absent: emit "BLOCKED -- no scout artifact for {topic}. Run scout first." Halt.
  SCOUT READY cannot fire without a found file.
- Read file. Set scout_source = found path.
- Emit: SCOUT READY. scout_source = [path]

CONFIDENCE CHAIN REGISTER (initialized here, written by each stage):
  confidence_prior: [set in Stage 1]
  s2_delta:         [set in Stage 2]
  s3_delta:         [set in Stage 3]
  s4_delta:         [set in Stage 4]
  confidence_final: [computed in Stage 5]

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 -- HYPOTHESIS

Exit signal: HYPOTHESIS WRITTEN

ENTRY: SCOUT READY must have fired. If not: halt.

Frame the central falsifiable claim for {topic}. Ground it in the scout artifact.
Set initial confidence that the hypothesis is correct (1-10, based on scout evidence).

Frontmatter:
  scout_source: simulations/scout/{topic}-scout-{date}.md
  confidence_prior: [N]

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Emit: HYPOTHESIS WRITTEN. confidence_prior = [N]

STAGE 2 cannot begin until HYPOTHESIS WRITTEN fires.

---

## STAGE 2 -- WEBSEARCH

Exit signal: WEBSEARCH WRITTEN

ENTRY: HYPOTHESIS WRITTEN must have fired. confidence_prior received. If not: halt.

Gather external evidence. Assess each source against the hypothesis.
Flag thin or absent evidence at the point of discovery -- not deferred:
  THIN: [area] -- [gap]

COUNT GATE: Identify at least 3 distinct web sources before this stage can close.
  source_count: [N]
  If source_count < 3: note "THIN COVERAGE -- only [N] web sources found" and continue.
  Gate clears at source_count >= 3 OR explicit thin-coverage note recorded.

Set s2_delta: confidence adjustment from web evidence (-3 to +3).

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Emit: WEBSEARCH WRITTEN. s2_delta = [N]. source_count = [N]

STAGE 3 cannot begin until WEBSEARCH WRITTEN fires.

---

## STAGE 3 -- INTELLIGENCE

Exit signal: INTELLIGENCE WRITTEN

ENTRY: WEBSEARCH WRITTEN must have fired. s2_delta received. If not: halt.

Search internal signal artifacts and related topic runs for evidence.
Flag thin evidence inline when found:
  THIN: [area] -- [gap]

COUNT GATE: Identify at least 2 distinct internal signals before this stage can close.
  signal_count: [N]
  If signal_count < 2: note "THIN INTERNAL -- only [N] internal signals found" and continue.
  Gate clears at signal_count >= 2 OR explicit thin-internal note recorded.

Set s3_delta: confidence adjustment from internal evidence (-3 to +3).

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Emit: INTELLIGENCE WRITTEN. s3_delta = [N]. signal_count = [N]

STAGE 4 cannot begin until INTELLIGENCE WRITTEN fires.

---

## STAGE 4 -- ANALYSIS

Exit signal: ANALYSIS WRITTEN

ENTRY: INTELLIGENCE WRITTEN must have fired. s3_delta received. If not: halt.

Aggregate THIN flags from Stages 2 and 3. Map each gap to the hypothesis claim it weakens.
Set s4_delta: confidence adjustment from gap analysis (-3 to +3).

running_confidence = confidence_prior + s2_delta + s3_delta + s4_delta
If running_confidence < 1: running_confidence = 1
If running_confidence > 10: running_confidence = 10

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Emit: ANALYSIS WRITTEN. s4_delta = [N]. running_confidence = [N]

STAGE 5 cannot begin until ANALYSIS WRITTEN fires.

---

## STAGE 5 -- SYNTHESIS

Exit signal: CAMPAIGN COMPLETE

ENTRY: ANALYSIS WRITTEN must have fired. running_confidence received. If not: halt.

### Write A -- Claim Evidence Map

For each hypothesis claim:
- State evidence strength: strong / moderate / thin
- If thin: name source stage, weakened claim, and adjusted confidence delta
  (e.g., "Stage 2 source_count = 1: -1 confidence on claim X")

confidence_final = running_confidence [state equation: prior + s2 + s3 + s4 = final]

Write A: simulations/prove/prove-synthesize/{topic}-prove-synthesize-draft-{date}.md

### Write B -- Evidence Brief

State verdict: supported / partially supported / not supported.
State confidence_final and the chain equation.
Reference Write A for claim-level detail.

Close: Evidence brief for {topic} is ready for /topic-story.

Write B: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Emit: CAMPAIGN COMPLETE. confidence_final = [N]
```

---

## V-04 -- Per-Stage Inertia + Resume Audit

**Axis**: per_stage_inertia_displacement + resume_audit (combined)
**Hypothesis**: V-01 (per-stage inertia delta) and V-02 (resume audit) are independent
structural additions. V-04 combines them: the INERTIA ANCHOR is written into the SETUP
exit signal payload, the RESUME AUDIT carries the inertia_anchor forward if Stage 1 is
RESUME-SKIP, and each evidence stage (2, 3, 4) continues the inertia delta check. The
combination tests whether two independent structural patterns co-exist without conflict
and whether the inertia anchor survives the resume boundary.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages. Resumable: pre-run audit
marks completed stages RESUME-SKIP. Stage 5 produces two artifacts. Each stage has a
declared exit signal. No stage begins without the prior stage's exit signal. Inertia
framing runs throughout: every evidence stage checks displacement case against the
status-quo comparator.

---

## SETUP

Exit signal: SCOUT READY

To fire SCOUT READY:
- Glob `simulations/scout/{topic}-scout-*.md`
- If absent: emit "BLOCKED -- no scout artifact for {topic}. Run scout first." Halt.
  SCOUT READY cannot fire without a found file.
- Read file. Set scout_source = found path.
- Name the status-quo comparator -- the incumbent approach {topic} must displace:
  inertia_anchor: [status_quo_comparator -- one sentence why it wins today]
- Emit: SCOUT READY. scout_source = [path]. inertia_anchor = [comparator]

RESUME AUDIT cannot begin until SCOUT READY fires.

---

## RESUME AUDIT

Glob for existing stage artifacts:

  s1: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  s2: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  s3: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  s4: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  s5: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

Mark each DONE or MISSING.

  s1_status: [RESUME-SKIP / RUN]
  s2_status: [RESUME-SKIP / RUN]
  s3_status: [RESUME-SKIP / RUN]
  s4_status: [RESUME-SKIP / RUN]
  s5_status: [RESUME-SKIP / RUN]

If s1_status = RESUME-SKIP: read Stage 1 artifact. Carry scout_source forward.
Also carry inertia_anchor from SETUP into resumed stages.

Emit: AUDIT COMPLETE. resuming_from = Stage [N]. inertia_anchor = [value carried forward]

STAGE 1 cannot begin until AUDIT COMPLETE fires.

---

## STAGE 1 -- HYPOTHESIS

Exit signal: HYPOTHESIS WRITTEN

ENTRY: AUDIT COMPLETE must have fired. If not: halt.
If s1_status = RESUME-SKIP: emit HYPOTHESIS WRITTEN (prior artifact found). Advance.

Frame the central falsifiable claim for {topic}. Ground it in the scout artifact.

Frontmatter:
  scout_source: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [inertia_anchor value]

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Emit: HYPOTHESIS WRITTEN

STAGE 2 cannot begin until HYPOTHESIS WRITTEN fires.

---

## STAGE 2 -- WEBSEARCH

Exit signal: WEBSEARCH WRITTEN

ENTRY: HYPOTHESIS WRITTEN must have fired. If not: halt.
If s2_status = RESUME-SKIP: emit WEBSEARCH WRITTEN (prior artifact found). Advance.

Gather external evidence. Flag thin findings at point of discovery -- not deferred:
  THIN: [area] -- [gap]

INERTIA DELTA: Does this external evidence change the displacement case against
[inertia_anchor]?
  s2_inertia_delta: [strengthens / weakens / neutral -- one sentence reason]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Emit: WEBSEARCH WRITTEN. s2_inertia_delta = [value]

STAGE 3 cannot begin until WEBSEARCH WRITTEN fires.

---

## STAGE 3 -- INTELLIGENCE

Exit signal: INTELLIGENCE WRITTEN

ENTRY: WEBSEARCH WRITTEN must have fired. If not: halt.
If s3_status = RESUME-SKIP: emit INTELLIGENCE WRITTEN (prior artifact found). Advance.

Search internal signal artifacts for evidence. Flag thin findings:
  THIN: [area] -- [gap]

INERTIA DELTA: Does this internal evidence change the displacement case against
[inertia_anchor]?
  s3_inertia_delta: [strengthens / weakens / neutral -- one sentence reason]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Emit: INTELLIGENCE WRITTEN. s3_inertia_delta = [value]

STAGE 4 cannot begin until INTELLIGENCE WRITTEN fires.

---

## STAGE 4 -- ANALYSIS

Exit signal: ANALYSIS WRITTEN

ENTRY: INTELLIGENCE WRITTEN must have fired. If not: halt.
If s4_status = RESUME-SKIP: emit ANALYSIS WRITTEN (prior artifact found). Advance.

Aggregate THIN flags from Stages 2 and 3. Map each gap to the hypothesis claim it weakens.

DISPLACEMENT AGGREGATE: Combine s2_inertia_delta and s3_inertia_delta. State overall verdict:
  displacement_verdict: [favors {topic} / favors status_quo / inconclusive -- two sentences]

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Emit: ANALYSIS WRITTEN. displacement_verdict = [value]

STAGE 5 cannot begin until ANALYSIS WRITTEN fires.

---

## STAGE 5 -- SYNTHESIS

Exit signal: CAMPAIGN COMPLETE

ENTRY: ANALYSIS WRITTEN must have fired. If not: halt.

### Write A -- Claim Evidence Map

For each hypothesis claim:
- State evidence strength: strong / moderate / thin
- If thin: name source stage and adjusted confidence

Write A: simulations/prove/prove-synthesize/{topic}-prove-synthesize-draft-{date}.md

### Write B -- Evidence Brief

State verdict: supported / partially supported / not supported.
Reference displacement_verdict from Stage 4.
Reference Write A for claim-level detail.

Close: Evidence brief for {topic} is ready for /topic-story.

Write B: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Emit: CAMPAIGN COMPLETE
```

---

## V-05 -- All Three + Full Structural Stack

**Axis**: per_stage_inertia_displacement + resume_audit + confidence_chain_count_gated + full R2 V-05 stack (combined)
**Hypothesis**: The three new axes (V-01/V-02/V-03) combined with the full R2 V-05
structural stack (SCOUT READY exit-signal chain, two-write Stage 5, THIN flags at discovery,
scout_source frontmatter) produces a variation that: (a) passes all 10 v14 criteria at
100/100, (b) surfaces at least two new excellence patterns that could become aspirational
criteria in rubric v15 -- specifically, INERTIA DELTA chaining as a displacement-tracking
mechanism and numeric confidence chain with count-gate enforcement as a sufficiency
mechanism.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages. Resumable: pre-run audit
marks completed stages RESUME-SKIP. Stage 5 produces two artifacts (Write A = claim-evidence
map, Write B = final brief). Confidence flows numerically 1-10 through a chain. Each
evidence stage has a count gate and an inertia delta check. Each stage has a declared exit
signal. No stage begins without the prior stage's exit signal.

---

## SETUP

Exit signal: SCOUT READY

To fire SCOUT READY:
- Glob `simulations/scout/{topic}-scout-*.md`
- If absent: emit "BLOCKED -- no scout artifact for {topic}. Run scout first." Halt.
  SCOUT READY cannot fire without a found file.
- Read file. Set scout_source = found path.
- Name the status-quo comparator -- the incumbent approach {topic} must displace:
  inertia_anchor: [status_quo_comparator -- one sentence why it wins today]
- Initialize confidence chain register:
    confidence_prior: [to be set in Stage 1]
    s2_delta:         [to be set in Stage 2]
    s3_delta:         [to be set in Stage 3]
    s4_delta:         [to be set in Stage 4]
    confidence_final: [to be computed in Stage 5]
- Emit: SCOUT READY. scout_source = [path]. inertia_anchor = [comparator]

RESUME AUDIT cannot begin until SCOUT READY fires.

---

## RESUME AUDIT

Glob for existing stage artifacts:

  s1: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  s2: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  s3: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  s4: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  s5: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

Mark each DONE or MISSING.

  s1_status: [RESUME-SKIP / RUN]   s2_status: [RESUME-SKIP / RUN]
  s3_status: [RESUME-SKIP / RUN]   s4_status: [RESUME-SKIP / RUN]
  s5_status: [RESUME-SKIP / RUN]

If s1_status = RESUME-SKIP: read Stage 1 artifact. Carry scout_source and confidence_prior.
Carry inertia_anchor from SETUP into all resumed stages.

Emit: AUDIT COMPLETE. resuming_from = Stage [N]

STAGE 1 cannot begin until AUDIT COMPLETE fires.

---

## STAGE 1 -- HYPOTHESIS

Exit signal: HYPOTHESIS WRITTEN

ENTRY: AUDIT COMPLETE must have fired. If not: halt.
If s1_status = RESUME-SKIP: read confidence_prior from existing artifact. Emit HYPOTHESIS WRITTEN. Advance.

Frame the central falsifiable claim for {topic}. Ground it in the scout artifact.
Set confidence_prior (1-10) -- initial confidence the hypothesis is correct based on scout evidence.

Frontmatter:
  scout_source: simulations/scout/{topic}-scout-{date}.md
  status_quo_comparator: [inertia_anchor value]
  confidence_prior: [N]

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Emit: HYPOTHESIS WRITTEN. confidence_prior = [N]

STAGE 2 cannot begin until HYPOTHESIS WRITTEN fires.

---

## STAGE 2 -- WEBSEARCH

Exit signal: WEBSEARCH WRITTEN

ENTRY: HYPOTHESIS WRITTEN must have fired. confidence_prior received. If not: halt.
If s2_status = RESUME-SKIP: carry s2_delta from existing artifact. Emit WEBSEARCH WRITTEN. Advance.

Gather external evidence against the hypothesis. Flag thin findings at point of discovery:
  THIN: [area] -- [gap]

COUNT GATE: Identify at least 3 distinct web sources.
  source_count: [N]
  If source_count < 3: note "THIN WEB COVERAGE -- [N] sources found" at discovery point.
  Gate clears at source_count >= 3 OR explicit note recorded.

INERTIA DELTA:
  s2_inertia_delta: [strengthens / weakens / neutral -- one sentence against inertia_anchor]

Set s2_delta: confidence adjustment from web evidence (-3 to +3).

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Emit: WEBSEARCH WRITTEN. s2_delta = [N]. source_count = [N]. s2_inertia_delta = [value]

STAGE 3 cannot begin until WEBSEARCH WRITTEN fires.

---

## STAGE 3 -- INTELLIGENCE

Exit signal: INTELLIGENCE WRITTEN

ENTRY: WEBSEARCH WRITTEN must have fired. s2_delta received. If not: halt.
If s3_status = RESUME-SKIP: carry s3_delta from existing artifact. Emit INTELLIGENCE WRITTEN. Advance.

Search internal signal artifacts for evidence. Flag thin evidence inline:
  THIN: [area] -- [gap]

COUNT GATE: Identify at least 2 distinct internal signals.
  signal_count: [N]
  If signal_count < 2: note "THIN INTERNAL -- [N] signals found" at discovery point.
  Gate clears at signal_count >= 2 OR explicit note recorded.

INERTIA DELTA:
  s3_inertia_delta: [strengthens / weakens / neutral -- one sentence against inertia_anchor]

Set s3_delta: confidence adjustment from internal evidence (-3 to +3).

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Emit: INTELLIGENCE WRITTEN. s3_delta = [N]. signal_count = [N]. s3_inertia_delta = [value]

STAGE 4 cannot begin until INTELLIGENCE WRITTEN fires.

---

## STAGE 4 -- ANALYSIS

Exit signal: ANALYSIS WRITTEN

ENTRY: INTELLIGENCE WRITTEN must have fired. s3_delta received. If not: halt.
If s4_status = RESUME-SKIP: carry s4_delta and displacement_verdict from existing artifact. Emit ANALYSIS WRITTEN. Advance.

Aggregate THIN flags from Stages 2 and 3. Map each gap to the hypothesis claim it weakens.
Set s4_delta: confidence adjustment from gap analysis (-3 to +3).

DISPLACEMENT AGGREGATE: Combine s2_inertia_delta and s3_inertia_delta:
  displacement_verdict: [favors {topic} / favors status_quo / inconclusive -- two sentences]

running_confidence = confidence_prior + s2_delta + s3_delta + s4_delta
(clamp to 1-10)

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Emit: ANALYSIS WRITTEN. s4_delta = [N]. running_confidence = [N]. displacement_verdict = [value]

STAGE 5 cannot begin until ANALYSIS WRITTEN fires.

---

## STAGE 5 -- SYNTHESIS

Exit signal: CAMPAIGN COMPLETE

ENTRY: ANALYSIS WRITTEN must have fired. running_confidence received. If not: halt.

### Write A -- Claim Evidence Map

For each hypothesis claim:
- State evidence strength: strong / moderate / thin
- If thin: name source stage, weakened claim, and confidence delta
  (e.g., "Stage 2 THIN WEB COVERAGE: s2_delta = -1 on claim X")

confidence_final = running_confidence
Chain equation: [confidence_prior] + [s2_delta] + [s3_delta] + [s4_delta] = [confidence_final]

Write A: simulations/prove/prove-synthesize/{topic}-prove-synthesize-draft-{date}.md

### Write B -- Evidence Brief

State verdict: supported / partially supported / not supported.
State confidence_final and show the chain equation.
State displacement_verdict from Stage 4.
Reference Write A for claim-level detail.

Close: Evidence brief for {topic} is ready for /topic-story.

Write B: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Emit: CAMPAIGN COMPLETE. confidence_final = [N]
```
