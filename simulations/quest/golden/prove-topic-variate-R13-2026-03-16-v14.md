---
skill: quest-variate
skill_target: prove-topic
round: R13
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [count_gated_exit_language, claim_traceability_chain, displacement_framing]
  combined: [V-04 (count_gated + claim_traceability), V-05 (all_three + full_R12_V05_baseline)]
r12_anchor: >
  R12 V-05 predicted 100 on all 10 rubric v14 criteria using: ARTIFACT PATH TABLE,
  scout gate with scout_source in hypothesis frontmatter, CLAIM INDEX (3-5 CLAIM-N IDs)
  at Stage 1, THIN flags with inline "weakens: CLAIM-N" at discovery, CLAIM IMPACT TABLE
  at Stage 4, PER-CLAIM CONFIDENCE TABLE at Stage 5, per-stage STAGE-N CLEARED emits.
  All R13 variations carry these as the structural baseline.
r13_context: >
  R12 V-05 closes all 10 v14 criteria. R13 probes three axes that are NOT covered by
  v14 but that represent candidate excellence patterns for a v15 rubric:

  V-01 (single: count_gated_exit_language): Evidence stages specify a minimum source count
  (Stage 2: 3+ external; Stage 3: 2+ internal) and the exit emit is count-gated: "Do not
  fire STAGE-N CLEARED until count >= N." R12 V-05 does not quantify minimum evidence.
  This axis tests whether a hard count floor at exit improves evidence completeness.

  V-02 (single: claim_traceability_chain): R12 V-05 creates CLAIM-N IDs at Stage 1 and
  THIN flags reference them. But there is no cross-stage chain audit at synthesis that
  reconstructs the full path: hypothesis_claim -> THIN_flag_stage -> analysis_status ->
  synthesis_confidence. V-02 adds a CLAIM CHAIN TABLE at Stage 5 that closes this loop
  explicitly per claim, making traceability auditable from hypothesis to verdict.

  V-03 (single: displacement_framing): R12 V-05 does not name the status quo being
  displaced. Prove evidence campaigns exist to make a displacement case. V-03 adds a
  SETUP step that names status_quo_comparator and requires each evidence stage to assess
  whether evidence supports displacement of the incumbent. This is purely framing — the
  structural mechanics remain identical — but the displacement lens sharpens claim formation
  and evidence assessment.

  V-04 (combined: count_gated_exit_language + claim_traceability_chain): V-01 + V-02.
  Tests whether fixing evidence quantity gates and adding chain auditability together
  produce new excellence patterns without disturbing R12 V-05's 100-scoring mechanisms.

  V-05 (full: all three + complete R12 V-05 baseline): Count-gated exits + claim chain
  table + displacement framing on top of the full R12 V-05 structural stack. Tests whether
  all three new axes simultaneously produce a cleaner, more auditable prompt that still
  scores 100 on v14 while surfacing candidate criteria for v15.
---

# prove-topic Variations — Round 13 (Rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01 through C-10)
**Date**: 2026-03-16
**Round**: R13

---

## Context: what informed this round

R12 V-05 is the structural floor for all R13 variations. All ten v14 criteria predicted
to pass. Three axes not covered by v14 are probed here as candidate v15 patterns:

| Axis | What R12 V-05 lacks | R13 probe | Candidate v15 criterion |
|------|---------------------|-----------|------------------------|
| count_gated_exit_language | No minimum source count per stage | V-01, V-04, V-05 | count-gated exits required per evidence stage |
| claim_traceability_chain | No end-to-end chain from hypothesis to synthesis verdict | V-02, V-04, V-05 | synthesis reconstructs full claim chain |
| displacement_framing | No incumbent named; no displacement verdict | V-03, V-05 | displacement case explicitly named and assessed |

---

## V-01 — count_gated_exit_language

**Axis**: count_gated_exit_language (single)
**Hypothesis**: R12 V-05 requires evidence stages to gather sources but does not set
a minimum count or embed the count requirement in the exit signal. Adding "Do not fire
STAGE-N CLEARED until count >= N" as a structural gate — not a prose suggestion — prevents
premature exit with thin coverage. If this count-gated exit language produces an evidence
brief with more complete source coverage without any v14 criteria regressions, it is a
candidate excellence pattern for C-11 in v15.

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

## ARTIFACT PATH TABLE (declared at campaign open; each WRITE echoes the exact path)

| Stage | Signal             | Full path                                                                      |
|-------|--------------------|--------------------------------------------------------------------------------|
| 1     | prove-hypothesis   | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md          |
| 2     | prove-websearch    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md            |
| 3     | prove-intelligence | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md      |
| 4     | prove-analysis     | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md              |
| 5     | prove-synthesize   | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md          |

---

## SETUP -- Scout Gate

1. Glob `simulations/scout/{topic}-scout-*.md`.
2. If no file found:
   Emit: BLOCKED. No scout artifact for `{topic}`. Run a scout skill first. Halt.
3. Set scout_source = full path of found file (most recent if multiple). Read it.
4. Emit:
   SCOUT GATE CLEARED.
   scout_source: [full path]

Stage 1 is structurally blocked until SCOUT GATE CLEARED is emitted with
scout_source named.

---

## STAGE 1 -- HYPOTHESIS

GATE CHECK:
  [ ] SCOUT GATE CLEARED emitted.
  [ ] scout_source named.
  If either missing: BLOCKED at Stage 1. Halt.

Load scout_source. Frame the hypothesis for {topic} grounded in the scout findings.

The artifact body must include:

1. MAIN CLAIM: one falsifiable sentence about {topic}.
2. CLAIM INDEX:
   CLAIM-1: [sub-claim -- one sentence, testable by evidence]
   CLAIM-2: [sub-claim -- one sentence, testable by evidence]
   CLAIM-3: [sub-claim -- one sentence, testable by evidence]
   (3-5 claims total)
   THIN flags at Stages 2 and 3 must reference these IDs.

Reference scout_source explicitly in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [full path from SETUP -- copied verbatim, not inferred]

Emit: STAGE-1 CLEARED.

---

## STAGE 2 -- WEBSEARCH

GATE CHECK: STAGE-1 CLEARED emitted? If not: BLOCKED. Halt.

Gather external evidence for each claim in the CLAIM INDEX. Minimum 3 external
sources. For each source, assess strength of evidence. When evidence is thin,
conflicting, or absent for any claim, flag immediately at point of discovery:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

Do not defer. Emit the THIN flag where the gap is found.

COUNT GATE: Do not fire STAGE-2 CLEARED until 3 or more sources have been assessed.
If fewer than 3 sources found, gather additional sources before proceeding.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: STAGE-2 CLEARED. (sources assessed: [N])

---

## STAGE 3 -- INTELLIGENCE

GATE CHECK: STAGE-2 CLEARED emitted? If not: BLOCKED. Halt.

Search internal sources -- existing signal artifacts, related topics, prior runs --
for evidence relevant to each claim. Minimum 2 internal sources. Apply the same
THIN annotation:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

COUNT GATE: Do not fire STAGE-3 CLEARED until 2 or more internal sources have been
assessed. If fewer than 2 sources found, widen the search before proceeding.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: STAGE-3 CLEARED. (sources assessed: [N])

---

## STAGE 4 -- ANALYSIS

GATE CHECK: STAGE-3 CLEARED emitted? If not: BLOCKED. Halt.

Aggregate all THIN flags from Stages 2 and 3 into a CLAIM IMPACT TABLE:

| Flag    | Source Stage | Area | Gap | Claim Weakened |
|---------|-------------|------|-----|----------------|
| THIN-01 | S2          | ...  | ... | CLAIM-N        |

If no THIN flags: one row -- "no THIN flags found across Stages 2-3".

For each claim in the CLAIM INDEX, state evidence status:
  SUPPORTED / WEAKENED (has one or more THIN flags) / UNSUPPORTED

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: STAGE-4 CLEARED.

---

## STAGE 5 -- SYNTHESIZE

GATE CHECK: STAGE-4 CLEARED emitted? If not: BLOCKED. Halt.

State the overall verdict: supported / partially supported / not supported.

PER-CLAIM CONFIDENCE TABLE (required -- one row per claim in the CLAIM INDEX):

| Claim ID | Claim (one sentence) | Source Stage of THIN Flags | Gap | Adjusted Confidence |
|----------|----------------------|---------------------------|-----|---------------------|
| CLAIM-1  | ...                  | S2 / S3 / none            | ... | Low / Med / High    |
| CLAIM-2  | ...                  | ...                       | ... | ...                 |
| CLAIM-3  | ...                  | ...                       | ... | ...                 |

Rules:
- Source Stage must match the origin in Stage 4's CLAIM IMPACT TABLE.
- Gap must restate the Stage 4 gap text for that claim -- not a new assessment.
- Claims with one or more THIN flags: confidence = Low (or Med if Stage 4 analysis
  provides specific positive evidence justifying the upgrade).
- Claims with no THIN flags: confidence = High.

State overall verdict and confidence in one sentence.

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-02 — claim_traceability_chain

**Axis**: claim_traceability_chain (single)
**Hypothesis**: R12 V-05 creates CLAIM-N IDs at Stage 1, propagates THIN flags through
Stages 2-3, and produces a per-claim confidence table at Stage 5. But no stage
reconstructs the full path from each claim's origin through all evidence stages to the
final confidence verdict. Adding a CLAIM CHAIN TABLE at Stage 5 that shows, per claim,
the hypothesis source, the THIN flags found, the Stage 4 status, and the final confidence
makes the traceability auditable end-to-end. This chain table is a candidate aspirational
criterion for v15 because it proves the per-claim assessment was grounded in evidence,
not retrospective judgment.

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

## ARTIFACT PATH TABLE

| Stage | Signal             | Full path                                                                      |
|-------|--------------------|--------------------------------------------------------------------------------|
| 1     | prove-hypothesis   | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md          |
| 2     | prove-websearch    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md            |
| 3     | prove-intelligence | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md      |
| 4     | prove-analysis     | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md              |
| 5     | prove-synthesize   | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md          |

---

## SETUP -- Scout Gate

1. Glob `simulations/scout/{topic}-scout-*.md`.
2. If no file found:
   Emit: BLOCKED. No scout artifact for `{topic}`. Run a scout skill first. Halt.
3. Set scout_source = full path of found file (most recent if multiple). Read it.
4. Emit:
   SCOUT GATE CLEARED.
   scout_source: [full path]

Stage 1 is structurally blocked until SCOUT GATE CLEARED is emitted.

---

## STAGE 1 -- HYPOTHESIS

GATE CHECK:
  [ ] SCOUT GATE CLEARED emitted.
  [ ] scout_source named.
  If either missing: BLOCKED at Stage 1. Halt.

Load scout_source. Frame the hypothesis for {topic} grounded in the scout findings.

The artifact body must include:

1. MAIN CLAIM: one falsifiable sentence about {topic}.
2. CLAIM INDEX:
   CLAIM-1: [sub-claim -- one sentence, testable by evidence]
   CLAIM-2: [sub-claim -- one sentence, testable by evidence]
   CLAIM-3: [sub-claim -- one sentence, testable by evidence]
   (3-5 claims total)
   THIN flags at Stages 2 and 3 reference these IDs.
   The CLAIM CHAIN TABLE at Stage 5 closes the loop per claim.

Reference scout_source explicitly in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [full path from SETUP -- copied verbatim, not inferred]

Emit: STAGE-1 CLEARED.

---

## STAGE 2 -- WEBSEARCH

GATE CHECK: STAGE-1 CLEARED emitted? If not: BLOCKED. Halt.

Gather external evidence for each claim in the CLAIM INDEX. Assess each source.
When evidence is thin, conflicting, or absent for any claim, flag immediately:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

Do not defer THIN flags to synthesis.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: STAGE-2 CLEARED.

---

## STAGE 3 -- INTELLIGENCE

GATE CHECK: STAGE-2 CLEARED emitted? If not: BLOCKED. Halt.

Search internal sources -- existing signal artifacts, related topics, prior runs --
for evidence relevant to each claim. Same THIN annotation:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: STAGE-3 CLEARED.

---

## STAGE 4 -- ANALYSIS

GATE CHECK: STAGE-3 CLEARED emitted? If not: BLOCKED. Halt.

Aggregate all THIN flags from Stages 2 and 3:

| Flag    | Source Stage | Area | Gap | Claim Weakened |
|---------|-------------|------|-----|----------------|
| THIN-01 | S2          | ...  | ... | CLAIM-N        |

If no THIN flags: one row -- "no THIN flags found across Stages 2-3".

For each claim in the CLAIM INDEX, state evidence status:
  SUPPORTED / WEAKENED (has one or more THIN flags) / UNSUPPORTED

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: STAGE-4 CLEARED.

---

## STAGE 5 -- SYNTHESIZE

GATE CHECK: STAGE-4 CLEARED emitted? If not: BLOCKED. Halt.

State the overall verdict: supported / partially supported / not supported.

CLAIM CHAIN TABLE (required -- one row per claim; traces hypothesis to verdict):

| Claim ID | Claim (one sentence) | THIN Flags Found | Source Stage | Stage 4 Status | Adjusted Confidence |
|----------|----------------------|-----------------|-------------|----------------|---------------------|
| CLAIM-1  | ...                  | THIN-01, ...    | S2 / S3     | SUPPORTED / WEAKENED / UNSUPPORTED | Low / Med / High |
| CLAIM-2  | ...                  | none            | n/a         | SUPPORTED      | High                |
| CLAIM-3  | ...                  | ...             | ...         | ...            | ...                 |

Rules:
- "THIN Flags Found" must cite the flag IDs from Stage 4's CLAIM IMPACT TABLE.
  Write "none" if no THIN flags for this claim.
- "Source Stage" must match Stage 4's CLAIM IMPACT TABLE.
- "Stage 4 Status" must copy the exact status word from Stage 4 -- do not reassess.
- Claims with WEAKENED or UNSUPPORTED status: confidence = Low or Med only.
- Claims with SUPPORTED status and no THIN flags: confidence = High.

State overall verdict and confidence in one sentence.

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-03 — displacement_framing

**Axis**: displacement_framing (single)
**Hypothesis**: Prove evidence campaigns build a case for adopting {topic} over the
current approach teams already use. R12 V-05 does not name the incumbent or require
evidence stages to assess displacement viability — it only assesses whether the
hypothesis is supported. Adding a DISPLACEMENT FRAME in SETUP (name the
status_quo_comparator) and a displacement verdict line in the synthesis ("Does the
evidence support displacing {status_quo_comparator} with {topic}?") sharpens the
entire campaign because claim formation, evidence weighting, and the final verdict all
have a concrete incumbent to position against. This is framing only — no structural
mechanics change — but it is a candidate v15 criterion because displacement is the
operative goal of the prove namespace.

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

The campaign builds a displacement case: evidence that {topic} should replace
{status_quo_comparator} as the approach teams use.

Stages: hypothesis -> websearch -> intelligence -> analysis -> synthesize

---

## ARTIFACT PATH TABLE

| Stage | Signal             | Full path                                                                      |
|-------|--------------------|--------------------------------------------------------------------------------|
| 1     | prove-hypothesis   | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md          |
| 2     | prove-websearch    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md            |
| 3     | prove-intelligence | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md      |
| 4     | prove-analysis     | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md              |
| 5     | prove-synthesize   | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md          |

---

## SETUP -- Displacement Frame + Scout Gate

Name the displacement frame before any stage begins:

  status_quo_comparator: [name the incumbent approach {topic} must displace]
  displacement_question: "Does the evidence support displacing {status_quo_comparator}
                          with {topic}? [Yes / Partially / No]"

Then load the scout artifact:

1. Glob `simulations/scout/{topic}-scout-*.md`.
2. If no file found:
   Emit: BLOCKED. No scout artifact for `{topic}`. Run a scout skill first. Halt.
3. Set scout_source = full path of found file (most recent if multiple). Read it.
4. Emit:
   SCOUT GATE CLEARED.
   scout_source: [full path]
   status_quo_comparator: [value from above]

Stage 1 is blocked until SCOUT GATE CLEARED is emitted.

---

## STAGE 1 -- HYPOTHESIS

GATE CHECK:
  [ ] SCOUT GATE CLEARED emitted.
  [ ] scout_source named.
  [ ] status_quo_comparator named.
  If any missing: BLOCKED at Stage 1. Halt.

Load scout_source. Frame the hypothesis for {topic} grounded in the scout findings.
The hypothesis must be framed as a displacement claim: what makes {topic} a credible
replacement for {status_quo_comparator}?

The artifact body must include:

1. MAIN CLAIM: one falsifiable sentence about {topic}'s advantage over
   {status_quo_comparator}.
2. CLAIM INDEX:
   CLAIM-1: [sub-claim -- one sentence, testable by evidence]
   CLAIM-2: [sub-claim -- one sentence, testable by evidence]
   CLAIM-3: [sub-claim -- one sentence, testable by evidence]
   (3-5 claims total)
   THIN flags at Stages 2 and 3 reference these IDs.

Reference scout_source explicitly in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [full path from SETUP -- copied verbatim, not inferred]

Emit: STAGE-1 CLEARED.

---

## STAGE 2 -- WEBSEARCH

GATE CHECK: STAGE-1 CLEARED emitted? If not: BLOCKED. Halt.

Gather external evidence for each claim in the CLAIM INDEX. For each source, assess
whether it supports displacement of {status_quo_comparator} by {topic}. When evidence
is thin, conflicting, or absent for any claim, flag immediately:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

Do not defer THIN flags.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: STAGE-2 CLEARED.

---

## STAGE 3 -- INTELLIGENCE

GATE CHECK: STAGE-2 CLEARED emitted? If not: BLOCKED. Halt.

Search internal sources for evidence relevant to each claim. Assess whether internal
evidence supports the displacement case. Same THIN annotation:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: STAGE-3 CLEARED.

---

## STAGE 4 -- ANALYSIS

GATE CHECK: STAGE-3 CLEARED emitted? If not: BLOCKED. Halt.

Aggregate all THIN flags from Stages 2 and 3:

| Flag    | Source Stage | Area | Gap | Claim Weakened |
|---------|-------------|------|-----|----------------|
| THIN-01 | S2          | ...  | ... | CLAIM-N        |

If no THIN flags: one row -- "no THIN flags found across Stages 2-3".

For each claim, state evidence status: SUPPORTED / WEAKENED / UNSUPPORTED.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: STAGE-4 CLEARED.

---

## STAGE 5 -- SYNTHESIZE

GATE CHECK: STAGE-4 CLEARED emitted? If not: BLOCKED. Halt.

State the overall verdict: supported / partially supported / not supported.

PER-CLAIM CONFIDENCE TABLE (one row per claim in the CLAIM INDEX):

| Claim ID | Claim (one sentence) | Source Stage of THIN Flags | Gap | Adjusted Confidence |
|----------|----------------------|---------------------------|-----|---------------------|
| CLAIM-1  | ...                  | S2 / S3 / none            | ... | Low / Med / High    |
| CLAIM-2  | ...                  | ...                       | ... | ...                 |
| CLAIM-3  | ...                  | ...                       | ... | ...                 |

Rules:
- Source Stage must match Stage 4's CLAIM IMPACT TABLE.
- Gap must restate Stage 4's gap text -- not a new assessment.
- Claims with THIN flags: confidence = Low unless Stage 4 justifies Med with specific evidence.
- Claims with no THIN flags: confidence = High.

DISPLACEMENT VERDICT (required):
  displacement_question: [copy from SETUP]
  displacement_verdict:  [Yes / Partially / No -- one sentence of justification]

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-04 — count_gated_exit_language + claim_traceability_chain (combined)

**Axis**: count_gated_exit_language + claim_traceability_chain
**Hypothesis**: V-01's count-gated exits prevent thin coverage. V-02's CLAIM CHAIN TABLE
closes the traceability loop. Combined, they address two orthogonal quality dimensions:
evidence quantity (count floors) and evidence lineage (chain auditability). Neither
requires the other to function, so the combination should produce additive improvements
without structural conflict. If the combination still scores 100 on v14 and produces
clean CLAIM CHAIN TABLEs, both mechanisms are candidate v15 criteria.

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

## ARTIFACT PATH TABLE

| Stage | Signal             | Full path                                                                      |
|-------|--------------------|--------------------------------------------------------------------------------|
| 1     | prove-hypothesis   | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md          |
| 2     | prove-websearch    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md            |
| 3     | prove-intelligence | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md      |
| 4     | prove-analysis     | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md              |
| 5     | prove-synthesize   | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md          |

---

## SETUP -- Scout Gate

1. Glob `simulations/scout/{topic}-scout-*.md`.
2. If no file found:
   Emit: BLOCKED. No scout artifact for `{topic}`. Run a scout skill first. Halt.
3. Set scout_source = full path of found file (most recent if multiple). Read it.
4. Emit:
   SCOUT GATE CLEARED.
   scout_source: [full path]

Stage 1 is blocked until SCOUT GATE CLEARED fires.

---

## STAGE 1 -- HYPOTHESIS

GATE CHECK:
  [ ] SCOUT GATE CLEARED emitted.
  [ ] scout_source named.
  If either missing: BLOCKED at Stage 1. Halt.

Load scout_source. Frame the hypothesis for {topic} grounded in the scout findings.

The artifact body must include:

1. MAIN CLAIM: one falsifiable sentence about {topic}.
2. CLAIM INDEX:
   CLAIM-1: [sub-claim -- one sentence, testable by evidence]
   CLAIM-2: [sub-claim -- one sentence, testable by evidence]
   CLAIM-3: [sub-claim -- one sentence, testable by evidence]
   (3-5 claims total)
   THIN flags at Stages 2 and 3 reference these IDs.
   CLAIM CHAIN TABLE at Stage 5 traces each claim from hypothesis to verdict.

Reference scout_source explicitly in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [full path from SETUP -- copied verbatim, not inferred]

Emit: STAGE-1 CLEARED.

---

## STAGE 2 -- WEBSEARCH

GATE CHECK: STAGE-1 CLEARED emitted? If not: BLOCKED. Halt.

Gather external evidence for each claim. Minimum 3 external sources. Assess each.
When evidence is thin, conflicting, or absent for any claim, flag immediately:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

Do not defer THIN flags.

COUNT GATE: Do not fire STAGE-2 CLEARED until 3 or more sources have been assessed.
If fewer than 3 found, gather additional sources before proceeding.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: STAGE-2 CLEARED. (sources assessed: [N])

---

## STAGE 3 -- INTELLIGENCE

GATE CHECK: STAGE-2 CLEARED emitted? If not: BLOCKED. Halt.

Search internal sources -- existing signal artifacts, related topics, prior runs.
Minimum 2 internal sources. Same THIN annotation:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

COUNT GATE: Do not fire STAGE-3 CLEARED until 2 or more internal sources have been
assessed. If fewer than 2 found, widen the search before proceeding.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: STAGE-3 CLEARED. (sources assessed: [N])

---

## STAGE 4 -- ANALYSIS

GATE CHECK: STAGE-3 CLEARED emitted? If not: BLOCKED. Halt.

Aggregate all THIN flags from Stages 2 and 3:

| Flag    | Source Stage | Area | Gap | Claim Weakened |
|---------|-------------|------|-----|----------------|
| THIN-01 | S2          | ...  | ... | CLAIM-N        |

If no THIN flags: one row -- "no THIN flags found across Stages 2-3".

For each claim, state evidence status: SUPPORTED / WEAKENED / UNSUPPORTED.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: STAGE-4 CLEARED.

---

## STAGE 5 -- SYNTHESIZE

GATE CHECK: STAGE-4 CLEARED emitted? If not: BLOCKED. Halt.

State the overall verdict: supported / partially supported / not supported.

CLAIM CHAIN TABLE (required -- one row per claim; traces hypothesis to verdict):

| Claim ID | Claim (one sentence) | THIN Flags Found | Source Stage | Stage 4 Status | Adjusted Confidence |
|----------|----------------------|-----------------|-------------|----------------|---------------------|
| CLAIM-1  | ...                  | THIN-01, ...    | S2 / S3     | SUPPORTED / WEAKENED / UNSUPPORTED | Low / Med / High |
| CLAIM-2  | ...                  | none            | n/a         | SUPPORTED      | High                |
| CLAIM-3  | ...                  | ...             | ...         | ...            | ...                 |

Rules:
- "THIN Flags Found" must cite flag IDs from Stage 4's CLAIM IMPACT TABLE. Write "none" if none.
- "Source Stage" must match Stage 4's table.
- "Stage 4 Status" must copy the exact status word from Stage 4 analysis -- no reassessment.
- Claims with WEAKENED or UNSUPPORTED status: confidence = Low or Med only.
- Claims with SUPPORTED status and no THIN flags: confidence = High.

State overall verdict and confidence in one sentence.

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-05 — Full Integration (all three axes + R12 V-05 baseline)

**Axis**: count_gated_exit_language + claim_traceability_chain + displacement_framing
**Structural baseline**: full R12 V-05 (ARTIFACT PATH TABLE, scout gate, CLAIM INDEX,
inline weakens, per-stage emits, CLAIM IMPACT TABLE at Stage 4)

**Hypothesis**: All three new axes are additive and non-conflicting when layered on the
R12 V-05 baseline. Count-gated exits prevent thin coverage (V-01). CLAIM CHAIN TABLE
closes end-to-end traceability (V-02). Displacement framing sharpens claim formation and
adds a displacement verdict to synthesis (V-03). The combined prompt scores 100 on v14
because all R12 V-05 structural guarantees are preserved, and it surfaces three candidate
v15 criteria: C-11 (count-gated exits), C-12 (claim chain traceability), C-13
(displacement verdict at synthesis).

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

The campaign builds a displacement case: evidence that {topic} should replace
{status_quo_comparator} as the approach teams currently use.

Stages: hypothesis -> websearch -> intelligence -> analysis -> synthesize

---

## ARTIFACT PATH TABLE (declared at campaign open; each WRITE echoes the exact path)

| Stage | Signal             | Full path                                                                      |
|-------|--------------------|--------------------------------------------------------------------------------|
| 1     | prove-hypothesis   | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md          |
| 2     | prove-websearch    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md            |
| 3     | prove-intelligence | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md      |
| 4     | prove-analysis     | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md              |
| 5     | prove-synthesize   | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md          |

---

## SETUP -- Displacement Frame + Scout Gate

Name the displacement frame first:

  status_quo_comparator: [name the incumbent approach {topic} must displace]
  displacement_question: "Does the evidence support displacing {status_quo_comparator}
                          with {topic}? [Yes / Partially / No]"

Then load the scout artifact:

1. Glob `simulations/scout/{topic}-scout-*.md`.
2. If no file found:
   Emit: BLOCKED. No scout artifact for `{topic}`. Run a scout skill first. Halt.
3. Set scout_source = full path of found file (most recent if multiple). Read it.
4. Emit:
   SCOUT GATE CLEARED.
   scout_source: [full path]
   status_quo_comparator: [value from above]

Stage 1 is structurally blocked until SCOUT GATE CLEARED fires.

---

## STAGE 1 -- HYPOTHESIS

GATE CHECK:
  [ ] SCOUT GATE CLEARED emitted.
  [ ] scout_source named.
  [ ] status_quo_comparator named.
  If any missing: BLOCKED at Stage 1. Halt.

Load scout_source. Frame the hypothesis for {topic} grounded in the scout findings.
The hypothesis is a displacement claim: what makes {topic} a credible replacement
for {status_quo_comparator}?

The artifact body must include:

1. MAIN CLAIM: one falsifiable sentence about {topic}'s advantage over
   {status_quo_comparator}.
2. CLAIM INDEX:
   CLAIM-1: [sub-claim -- one sentence, testable by evidence]
   CLAIM-2: [sub-claim -- one sentence, testable by evidence]
   CLAIM-3: [sub-claim -- one sentence, testable by evidence]
   (3-5 claims total)
   THIN flags at Stages 2 and 3 must reference these IDs.
   CLAIM CHAIN TABLE at Stage 5 closes the loop per claim from hypothesis to verdict.

Reference scout_source explicitly in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [full path from SETUP -- copied verbatim, not inferred]

Emit: STAGE-1 CLEARED.

---

## STAGE 2 -- WEBSEARCH

GATE CHECK: STAGE-1 CLEARED emitted? If not: BLOCKED. Halt.

Gather external evidence for each claim in the CLAIM INDEX. Minimum 3 external
sources. For each source, assess whether it supports displacement of
{status_quo_comparator} by {topic}. When evidence is thin, conflicting, or absent
for any claim, flag immediately at point of discovery:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

Do not defer THIN flags. Emit at point of discovery.

COUNT GATE: Do not fire STAGE-2 CLEARED until 3 or more sources have been assessed.
If fewer than 3 sources found, gather additional sources before proceeding.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: STAGE-2 CLEARED. (sources assessed: [N])

---

## STAGE 3 -- INTELLIGENCE

GATE CHECK: STAGE-2 CLEARED emitted? If not: BLOCKED. Halt.

Search internal sources -- existing signal artifacts, related topics, prior runs --
for evidence relevant to each claim. Minimum 2 internal sources. Assess whether
internal evidence supports the displacement case. Same THIN annotation:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

COUNT GATE: Do not fire STAGE-3 CLEARED until 2 or more internal sources have been
assessed. If fewer than 2 found, widen the search before proceeding.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: STAGE-3 CLEARED. (sources assessed: [N])

---

## STAGE 4 -- ANALYSIS

GATE CHECK: STAGE-3 CLEARED emitted? If not: BLOCKED. Halt.

Aggregate all THIN flags from Stages 2 and 3 into a CLAIM IMPACT TABLE:

| Flag    | Source Stage | Area | Gap | Claim Weakened |
|---------|-------------|------|-----|----------------|
| THIN-01 | S2          | ...  | ... | CLAIM-N        |

If no THIN flags: one row -- "no THIN flags found across Stages 2-3".

For each claim in the CLAIM INDEX, state evidence status:
  SUPPORTED / WEAKENED (has one or more THIN flags) / UNSUPPORTED

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: STAGE-4 CLEARED.

---

## STAGE 5 -- SYNTHESIZE

GATE CHECK: STAGE-4 CLEARED emitted? If not: BLOCKED. Halt.

State the overall verdict: supported / partially supported / not supported.

CLAIM CHAIN TABLE (required -- one row per claim; traces hypothesis to verdict):

| Claim ID | Claim (one sentence) | THIN Flags Found | Source Stage | Stage 4 Status | Adjusted Confidence |
|----------|----------------------|-----------------|-------------|----------------|---------------------|
| CLAIM-1  | ...                  | THIN-01, ...    | S2 / S3     | SUPPORTED / WEAKENED / UNSUPPORTED | Low / Med / High |
| CLAIM-2  | ...                  | none            | n/a         | SUPPORTED      | High                |
| CLAIM-3  | ...                  | ...             | ...         | ...            | ...                 |

Rules:
- "THIN Flags Found" must cite flag IDs from Stage 4's CLAIM IMPACT TABLE. Write "none" if none.
- "Source Stage" must match Stage 4's CLAIM IMPACT TABLE.
- "Stage 4 Status" must copy the exact status word from Stage 4 -- no new assessment.
- Claims with WEAKENED or UNSUPPORTED status: confidence = Low or Med only.
- Claims with SUPPORTED status and no THIN flags: confidence = High.

DISPLACEMENT VERDICT (required):
  displacement_question: [copy from SETUP verbatim]
  displacement_verdict:  [Yes / Partially / No -- one sentence of justification citing
                          the CLAIM CHAIN TABLE verdict pattern]

State overall verdict and confidence in one sentence.

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## Scoring Prediction

Axis comparison against rubric v14 (C-01 through C-10):

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 all five stages in sequence | PASS | PASS | PASS | PASS | PASS |
| C-02 scout named before hypothesis | PASS | PASS | PASS | PASS | PASS |
| C-03 one write per stage | PASS | PASS | PASS | PASS | PASS |
| C-04 synthesis names topic-story | PASS | PASS | PASS | PASS | PASS |
| C-05 full paths on every write | PASS | PASS | PASS | PASS | PASS |
| C-06 forward-only with scout gate | PASS | PASS | PASS | PASS | PASS |
| C-07 scout anchor in hypothesis artifact | PASS | PASS | PASS | PASS | PASS |
| C-08 evidence gaps flagged at discovery | PASS | PASS | PASS | PASS | PASS |
| C-09 thin-evidence propagates to synthesis | PASS | PASS+ | PASS | PASS+ | PASS+ |
| C-10 hypothesis structurally blocked | PASS | PASS | PASS | PASS | PASS |
| **Candidate C-11** count-gated exits | YES | - | - | YES | YES |
| **Candidate C-12** claim chain traceability | - | YES | - | YES | YES |
| **Candidate C-13** displacement verdict | - | - | YES | - | YES |

**V-01**: Count-gated exits add a hard floor on evidence quantity. No structural change
to the R12 V-05 traceability mechanics. All 10 v14 criteria maintain PASS. Candidate
C-11 fires. C-09 PASS (not PASS+) because no additional chain table beyond R12 V-05 PER-CLAIM.

**V-02**: CLAIM CHAIN TABLE closes the end-to-end loop per claim with flag IDs, source
stage, Stage 4 status, and confidence -- auditable in a single table. C-09 PASS+ because
the chain table explicitly enforces the THIN -> Stage 4 status -> confidence path (not
just source stage of flags). Candidate C-12 fires.

**V-03**: Displacement framing sharpens claim formation and adds a displacement verdict
at synthesis. All v14 mechanics preserved. DISPLACEMENT VERDICT is a new output element
not tested by any v14 criterion -- it does not regress any v14 criterion. Candidate C-13
fires. C-09 standard PASS.

**V-04**: V-01 + V-02 combined. Count-gated exits + CLAIM CHAIN TABLE. Both candidates
(C-11, C-12) fire. C-09 PASS+ from the chain table. Expected: 100 on v14 + candidates.

**V-05**: All three axes on R12 V-05 baseline. All three candidates (C-11, C-12, C-13)
fire simultaneously. C-09 PASS+ from CLAIM CHAIN TABLE. Displacement framing sharpens
every stage without breaking any v14 criterion. Expected: 100 on v14 + all three candidates.

**R13 thesis**: If V-04 and V-05 both score 100 on v14, the three new axes are confirmed
additive. V-05 becomes the proposed v15 baseline with three new criteria: count-gated
evidence exits (C-11), claim chain traceability table (C-12), and displacement verdict
at synthesis (C-13).
