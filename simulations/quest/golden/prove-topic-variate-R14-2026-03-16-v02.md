---
skill: quest-variate
skill_target: prove-topic
round: R14
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [counter_hypothesis_resolution, scout_signal_mapping, evidence_type_tagging]
  combined: [V-04 (counter_hypothesis + scout_signal), V-05 (all_three + full_R13_V05_baseline)]
r13_anchor: >
  R13 V-05 predicted 100 on all 10 rubric v14 criteria using: ARTIFACT PATH TABLE,
  displacement frame in SETUP (status_quo_comparator + displacement_question),
  scout gate with scout_source in hypothesis frontmatter, CLAIM INDEX (3-5 CLAIM-N IDs),
  THIN flags with inline "weakens: CLAIM-N" at discovery, COUNT GATEs (3+ at S2, 2+ at S3),
  CLAIM IMPACT TABLE at Stage 4, CLAIM CHAIN TABLE at Stage 5, DISPLACEMENT VERDICT at S5.
  R13 proposed three candidate v15 criteria: C-11 (count-gated exits), C-12 (claim chain
  traceability), C-13 (displacement verdict). All R14 variations carry this as the floor.
r14_context: >
  R13 V-05 closes all 10 v14 criteria and proposes three candidate v15 criteria.
  R14 probes axes that are orthogonal to the R13 set and represent the next layer
  of excellence patterns for a v16 rubric:

  V-01 (single: counter_hypothesis_resolution): R13 V-05 names the incumbent and asks
  whether evidence supports displacement, but never formally commits to the incumbent's
  best rebuttal nor requires Stage 5 to resolve it. Adding a COUNTER-HYPOTHESIS at Stage 1
  (the incumbent's strongest single-sentence rebuttal to the displacement claim) and a
  COUNTER-HYPOTHESIS RESOLUTION TABLE at Stage 5 (REFUTED / PARTIALLY REFUTED / OPEN RISK
  with artifact citation) closes the adversarial loop. If resolution = OPEN RISK, the overall
  verdict is capped at "partially supported." This axis is a candidate v16 criterion because
  it forces the campaign to engage the incumbent's defense, not just build the prosecution case.

  V-02 (single: scout_signal_mapping): R13 V-05 requires scout_source in the hypothesis
  artifact frontmatter and references it in the body. But it does not require each CLAIM-N
  to trace to a specific scout finding. A claim untethered from the scout is speculation,
  not grounded hypothesis. Adding a SCOUT SIGNAL MAP at Stage 1 (one row per claim, citing
  the scout section and the exact signal text) makes the scout-to-hypothesis link auditable.
  At Stage 5, the CLAIM CHAIN TABLE gains a "Scout Anchor" column. Ungrounded claims are
  flagged UNGROUNDED and excluded from the verdict calculation.

  V-03 (single: evidence_type_tagging): R13 V-05 requires minimum source counts at Stages 2
  and 3 but does not require diversity of evidence type. A campaign with 3 external sources
  all from the same category (e.g., three market analyst reports) has a narrower evidential
  base than one drawing from MARKET, TECHNICAL, and USER sources. Adding a TYPE tag per
  source (MARKET / TECHNICAL / USER / ACADEMIC) and requiring Stage 5 to verify that at
  least 2 distinct types appear across Stages 2-3 prevents single-category bias without
  changing the count floor mechanics.

  V-04 (combined: counter_hypothesis_resolution + scout_signal_mapping): V-01 + V-02.
  The counter-hypothesis closes the adversarial loop; scout signal mapping closes the
  grounding loop. Together they cover both directions of the evidence quality gap: what
  the incumbent says (counter) and what the scout said (anchor). Non-conflicting.

  V-05 (full: all three + complete R13 V-05 baseline): Counter-hypothesis resolution +
  scout signal mapping + evidence type tagging on the full R13 V-05 stack. Tests whether
  all three new axes simultaneously produce a cleaner, more defensible campaign prompt
  that still scores 100 on v14 while surfacing three candidate v16 criteria.
---

# prove-topic Variations -- Round 14 (Rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01 through C-10)
**Date**: 2026-03-16
**Round**: R14

---

## Context: what informed this round

R13 V-05 is the structural floor for all R14 variations. All ten v14 criteria
predicted to pass. Three axes not covered by v14 are probed here as candidate
v16 patterns (v15 will formalize the R13 C-11/C-12/C-13 set; v16 targets are R14's
discoveries):

| Axis | What R13 V-05 lacks | R14 probe | Candidate v16 criterion |
|------|---------------------|-----------|------------------------|
| counter_hypothesis_resolution | Incumbent rebuttal committed at Stage 1; resolution required at Stage 5 | V-01, V-04, V-05 | Stage 5 must resolve counter-hypothesis with REFUTED/PARTIALLY REFUTED/OPEN RISK |
| scout_signal_mapping | Each claim traces to a named scout section | V-02, V-04, V-05 | Every claim in CLAIM INDEX cites the scout section that grounds it |
| evidence_type_tagging | Evidence sources tagged by type; breadth verified at synthesis | V-03, V-05 | At least 2 distinct evidence types across Stages 2-3 |

---

## V-01 -- counter_hypothesis_resolution

**Axis**: counter_hypothesis_resolution (single)
**Hypothesis**: R13 V-05 names the incumbent and requires a displacement verdict at
Stage 5. But it never requires the campaign to articulate the incumbent's best rebuttal
upfront nor to resolve it explicitly at synthesis. A campaign that only builds the
prosecution case — without staging the defense — risks confirmation bias: evidence is
filtered for support, not tested against the best counter-argument. Adding a
COUNTER-HYPOTHESIS at Stage 1 (one sentence: the incumbent's strongest single argument
against displacement) and a COUNTER-HYPOTHESIS RESOLUTION at Stage 5 (REFUTED /
PARTIALLY REFUTED / OPEN RISK with artifact citation and verdict cap rule) forces the
campaign to engage the strongest opposing argument at both ends. If this produces
sharper claim formation and a more calibrated displacement verdict without any v14
regressions, it is a candidate v16 criterion.

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
2. COUNTER-HYPOTHESIS: the incumbent's strongest single-sentence rebuttal -- why
   {status_quo_comparator} will resist displacement. This is the claim the evidence
   campaign must engage and resolve. Write it before forming the CLAIM INDEX; it
   may sharpen or constrain the claims.
3. CLAIM INDEX:
   CLAIM-1: [sub-claim -- one sentence, testable by evidence]
   CLAIM-2: [sub-claim -- one sentence, testable by evidence]
   CLAIM-3: [sub-claim -- one sentence, testable by evidence]
   (3-5 claims total)
   THIN flags at Stages 2 and 3 must reference these IDs.
   CLAIM CHAIN TABLE at Stage 5 closes the loop per claim.

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
{status_quo_comparator} by {topic}. Also assess whether any source supports or
refutes the COUNTER-HYPOTHESIS from Stage 1. When evidence is thin, conflicting,
or absent for any claim, flag immediately at point of discovery:

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
for evidence relevant to each claim and to the COUNTER-HYPOTHESIS. Minimum 2
internal sources. Same THIN annotation:

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

COUNTER-HYPOTHESIS RESOLUTION (required):
  counter_hypothesis: [restate from Stage 1 verbatim -- do not paraphrase]
  resolution:         [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  evidence:           [cite the stage artifact(s) -- by path -- that support this resolution]

  Verdict cap rule: If resolution = OPEN RISK, the overall verdict cannot exceed
  "partially supported". Apply before stating the overall verdict.

DISPLACEMENT VERDICT (required):
  displacement_question: [copy from SETUP verbatim]
  displacement_verdict:  [Yes / Partially / No -- one sentence citing the CLAIM CHAIN TABLE
                          pattern and the COUNTER-HYPOTHESIS RESOLUTION outcome]

State overall verdict and confidence in one sentence.

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-02 -- scout_signal_mapping

**Axis**: scout_signal_mapping (single)
**Hypothesis**: R13 V-05 requires the scout artifact to be named in the hypothesis
frontmatter (`scout_source`) and referenced in the artifact body. But "referenced"
is loose: a paragraph mentioning the scout file satisfies C-02 and C-07, even if
none of the CLAIM-N sub-claims can be traced to a specific scout finding. A claim
that is not grounded in a scout signal is speculation, not grounded hypothesis. Adding
a SCOUT SIGNAL MAP at Stage 1 (one row per claim, citing the scout section and the
exact 1-sentence signal text that grounds it) makes the scout-to-hypothesis link
structurally auditable. A CLAIM without a scout anchor is flagged UNGROUNDED and
excluded from the verdict calculation. The CLAIM CHAIN TABLE at Stage 5 gains a
"Scout Anchor" column. If this axis produces a provably grounded CLAIM INDEX without
any v14 regressions, it is a candidate v16 criterion: every claim in the CLAIM INDEX
must trace to a named scout signal.

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
   CLAIM CHAIN TABLE at Stage 5 closes the loop per claim.
3. SCOUT SIGNAL MAP (required -- one row per claim):

   | Claim ID | Scout Section           | Scout Signal (1 sentence -- direct from scout) |
   |----------|-------------------------|------------------------------------------------|
   | CLAIM-1  | [section name or header]| [exact finding or signal from scout artifact]  |
   | CLAIM-2  | ...                     | ...                                            |
   | CLAIM-3  | ...                     | ...                                            |

   Rule: Every claim must trace to a named section in scout_source. A claim with no
   scout anchor is speculation, not grounded hypothesis. Do not include it in the
   CLAIM INDEX. Write UNGROUNDED in "Scout Section" if no anchor can be found; that
   claim is excluded from the verdict calculation at Stage 5.

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
for evidence relevant to each claim. Minimum 2 internal sources. Same THIN annotation:

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
  SUPPORTED / WEAKENED (has one or more THIN flags) / UNSUPPORTED / UNGROUNDED

Note: Any claim marked UNGROUNDED in Stage 1's SCOUT SIGNAL MAP carries UNGROUNDED
status here. Do not assess evidence for ungrounded claims.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: STAGE-4 CLEARED.

---

## STAGE 5 -- SYNTHESIZE

GATE CHECK: STAGE-4 CLEARED emitted? If not: BLOCKED. Halt.

State the overall verdict: supported / partially supported / not supported.
Exclude UNGROUNDED claims from the verdict calculation.

CLAIM CHAIN TABLE (required -- one row per claim; traces hypothesis to verdict):

| Claim ID | Claim (one sentence) | Scout Anchor    | THIN Flags Found | Source Stage | Stage 4 Status | Adjusted Confidence |
|----------|----------------------|-----------------|-----------------|-------------|----------------|---------------------|
| CLAIM-1  | ...                  | [scout section] | THIN-01, ...    | S2 / S3     | SUPPORTED / WEAKENED / UNSUPPORTED | Low / Med / High |
| CLAIM-2  | ...                  | [scout section] | none            | n/a         | SUPPORTED      | High                |
| CLAIM-3  | ...                  | UNGROUNDED      | n/a             | n/a         | UNGROUNDED     | excluded            |

Rules:
- "Scout Anchor" must copy the scout section from Stage 1's SCOUT SIGNAL MAP.
- "THIN Flags Found" must cite flag IDs from Stage 4's CLAIM IMPACT TABLE. Write "none" if none.
- "Source Stage" must match Stage 4's CLAIM IMPACT TABLE.
- "Stage 4 Status" must copy the exact status word from Stage 4 -- no new assessment.
- Claims with WEAKENED or UNSUPPORTED status: confidence = Low or Med only.
- Claims with SUPPORTED status and no THIN flags: confidence = High.
- Claims with UNGROUNDED status: confidence = excluded. Do not include in overall verdict.

DISPLACEMENT VERDICT (required):
  displacement_question: [copy from SETUP verbatim]
  displacement_verdict:  [Yes / Partially / No -- one sentence citing the CLAIM CHAIN TABLE
                          pattern, excluding UNGROUNDED claims]

State overall verdict and confidence in one sentence.

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-03 -- evidence_type_tagging

**Axis**: evidence_type_tagging (single)
**Hypothesis**: R13 V-05 requires a minimum source count at Stages 2 and 3 (3 external,
2 internal) via COUNT GATEs. Count floors prevent thin coverage. But they do not prevent
single-category coverage: three external sources drawn entirely from market analyst
reports create a narrower evidential base than three sources across market, technical,
and user domains. A campaign that confirms a claim only from one angle is less robust
than one that triangulates across evidence types. Adding a TYPE tag per source (MARKET /
TECHNICAL / USER / ACADEMIC) at Stages 2 and 3, and requiring Stage 5 to verify that
at least 2 distinct evidence types appear across the combined source set, prevents
single-category bias without changing count floor mechanics or any other v14-passing
structure. If this produces demonstrably broader evidence coverage without v14 regressions,
it is a candidate v16 criterion: at least 2 distinct evidence types required across Stages 2-3.

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

## EVIDENCE TYPE REGISTER (declared at campaign open)

Valid evidence types: MARKET / TECHNICAL / USER / ACADEMIC
Minimum breadth rule: at least 2 distinct types must appear across Stages 2 and 3 combined.
Stage 5 verifies. If fewer than 2 types: emit EVIDENCE BREADTH WARNING before verdict.

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
   CLAIM CHAIN TABLE at Stage 5 closes the loop per claim.

Reference scout_source explicitly in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [full path from SETUP -- copied verbatim, not inferred]

Emit: STAGE-1 CLEARED.

---

## STAGE 2 -- WEBSEARCH

GATE CHECK: STAGE-1 CLEARED emitted? If not: BLOCKED. Halt.

Gather external evidence for each claim in the CLAIM INDEX. Minimum 3 external
sources. For each source:
- Assess whether it supports displacement of {status_quo_comparator} by {topic}.
- Tag the source with its evidence type: MARKET / TECHNICAL / USER / ACADEMIC

When evidence is thin, conflicting, or absent for any claim, flag immediately:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

Do not defer THIN flags. Emit at point of discovery.

Running type set: [types seen so far this stage]

COUNT GATE: Do not fire STAGE-2 CLEARED until 3 or more sources have been assessed.
If fewer than 3 sources found, gather additional sources before proceeding.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: STAGE-2 CLEARED. (sources assessed: [N], types: [set of types seen])

---

## STAGE 3 -- INTELLIGENCE

GATE CHECK: STAGE-2 CLEARED emitted? If not: BLOCKED. Halt.

Search internal sources -- existing signal artifacts, related topics, prior runs --
for evidence relevant to each claim. Minimum 2 internal sources. For each source:
- Tag the source with its evidence type: MARKET / TECHNICAL / USER / ACADEMIC
- Apply the same THIN annotation if evidence is thin or absent:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

Running type set: [types seen so far -- cumulative across Stages 2 and 3]

COUNT GATE: Do not fire STAGE-3 CLEARED until 2 or more internal sources have been
assessed. If fewer than 2 found, widen the search before proceeding.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: STAGE-3 CLEARED. (sources assessed: [N], cumulative types: [set])

---

## STAGE 4 -- ANALYSIS

GATE CHECK: STAGE-3 CLEARED emitted? If not: BLOCKED. Halt.

Aggregate all THIN flags from Stages 2 and 3 into a CLAIM IMPACT TABLE:

| Flag    | Source Stage | Evidence Type | Area | Gap | Claim Weakened |
|---------|-------------|---------------|------|-----|----------------|
| THIN-01 | S2          | MARKET        | ...  | ... | CLAIM-N        |

If no THIN flags: one row -- "no THIN flags found across Stages 2-3".

For each claim in the CLAIM INDEX, state evidence status:
  SUPPORTED / WEAKENED (has one or more THIN flags) / UNSUPPORTED

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: STAGE-4 CLEARED.

---

## STAGE 5 -- SYNTHESIZE

GATE CHECK: STAGE-4 CLEARED emitted? If not: BLOCKED. Halt.

EVIDENCE BREADTH CHECK (required before verdict):
  types_seen: [list all distinct evidence types across Stages 2 and 3]
  breadth_count: [number of distinct types]
  If breadth_count < 2:
    Emit: EVIDENCE BREADTH WARNING -- only [N] evidence type(s) represented.
    Verdict confidence is capped at Medium.
  Else:
    Emit: EVIDENCE BREADTH CONFIRMED -- [N] distinct types.

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
- If EVIDENCE BREADTH WARNING fired: no claim may carry High confidence.

DISPLACEMENT VERDICT (required):
  displacement_question: [copy from SETUP verbatim]
  displacement_verdict:  [Yes / Partially / No -- one sentence citing the CLAIM CHAIN TABLE
                          pattern and evidence breadth status]

State overall verdict and confidence in one sentence.

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-04 -- counter_hypothesis_resolution + scout_signal_mapping (combined)

**Axis**: counter_hypothesis_resolution + scout_signal_mapping
**Hypothesis**: V-01's COUNTER-HYPOTHESIS closes the adversarial loop: the campaign
must engage the incumbent's best rebuttal and resolve it at synthesis. V-02's SCOUT
SIGNAL MAP closes the grounding loop: every claim must trace to a named scout finding.
These two axes address orthogonal quality dimensions. The counter-hypothesis axis
ensures the campaign is not confirmation-biased (it must reckon with the defense).
The scout signal mapping axis ensures claims are not speculation (they must trace to
prior research). Combined, they enforce that the displacement case is both grounded
(scout-anchored claims) and adversarially tested (resolved counter-hypothesis). Neither
mechanism conflicts with the other or with any R13 V-05 structural element. If V-04
scores 100 on v14 and both mechanisms produce clean output, they are confirmed as
additive candidate v16 criteria.

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
2. COUNTER-HYPOTHESIS: the incumbent's strongest single-sentence rebuttal -- why
   {status_quo_comparator} will resist displacement. Write this before forming the
   CLAIM INDEX; it may sharpen or constrain the claims. Stage 5 resolves it explicitly.
3. CLAIM INDEX:
   CLAIM-1: [sub-claim -- one sentence, testable by evidence]
   CLAIM-2: [sub-claim -- one sentence, testable by evidence]
   CLAIM-3: [sub-claim -- one sentence, testable by evidence]
   (3-5 claims total)
   THIN flags at Stages 2 and 3 must reference these IDs.
   CLAIM CHAIN TABLE at Stage 5 closes the loop per claim.
4. SCOUT SIGNAL MAP (required -- one row per claim):

   | Claim ID | Scout Section           | Scout Signal (1 sentence -- direct from scout) |
   |----------|-------------------------|------------------------------------------------|
   | CLAIM-1  | [section name or header]| [exact finding or signal from scout artifact]  |
   | CLAIM-2  | ...                     | ...                                            |
   | CLAIM-3  | ...                     | ...                                            |

   Rule: Every claim must trace to a named section in scout_source. A claim with no
   scout anchor is speculation. Mark it UNGROUNDED; it is excluded from the verdict.

Reference scout_source explicitly in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [full path from SETUP -- copied verbatim, not inferred]

Emit: STAGE-1 CLEARED.

---

## STAGE 2 -- WEBSEARCH

GATE CHECK: STAGE-1 CLEARED emitted? If not: BLOCKED. Halt.

Gather external evidence for each claim in the CLAIM INDEX. Minimum 3 external
sources. Assess displacement support and note evidence bearing on the
COUNTER-HYPOTHESIS. When evidence is thin, conflicting, or absent for any claim,
flag immediately at point of discovery:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

Do not defer THIN flags. Emit at point of discovery.

COUNT GATE: Do not fire STAGE-2 CLEARED until 3 or more sources have been assessed.
If fewer than 3 sources found, gather additional sources before proceeding.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: STAGE-2 CLEARED. (sources assessed: [N])

---

## STAGE 3 -- INTELLIGENCE

GATE CHECK: STAGE-2 CLEARED emitted? If not: BLOCKED. Halt.

Search internal sources for evidence relevant to each claim and to the
COUNTER-HYPOTHESIS. Minimum 2 internal sources. Same THIN annotation:

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
  SUPPORTED / WEAKENED (has one or more THIN flags) / UNSUPPORTED / UNGROUNDED

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: STAGE-4 CLEARED.

---

## STAGE 5 -- SYNTHESIZE

GATE CHECK: STAGE-4 CLEARED emitted? If not: BLOCKED. Halt.

State the overall verdict: supported / partially supported / not supported.
Exclude UNGROUNDED claims from the verdict calculation.

CLAIM CHAIN TABLE (required -- one row per claim):

| Claim ID | Claim (one sentence) | Scout Anchor    | THIN Flags Found | Source Stage | Stage 4 Status | Adjusted Confidence |
|----------|----------------------|-----------------|-----------------|-------------|----------------|---------------------|
| CLAIM-1  | ...                  | [scout section] | THIN-01, ...    | S2 / S3     | SUPPORTED / WEAKENED / UNSUPPORTED | Low / Med / High |
| CLAIM-2  | ...                  | [scout section] | none            | n/a         | SUPPORTED      | High                |
| CLAIM-3  | ...                  | UNGROUNDED      | n/a             | n/a         | UNGROUNDED     | excluded            |

Rules:
- "Scout Anchor" must copy the section from Stage 1's SCOUT SIGNAL MAP.
- "THIN Flags Found" must cite flag IDs from Stage 4's CLAIM IMPACT TABLE. Write "none" if none.
- "Source Stage" must match Stage 4's CLAIM IMPACT TABLE.
- "Stage 4 Status" must copy the exact status word from Stage 4 -- no new assessment.
- WEAKENED or UNSUPPORTED claims: confidence = Low or Med only.
- SUPPORTED claims with no THIN flags: confidence = High.
- UNGROUNDED claims: confidence = excluded; do not factor into overall verdict.

COUNTER-HYPOTHESIS RESOLUTION (required):
  counter_hypothesis: [restate from Stage 1 verbatim -- do not paraphrase]
  resolution:         [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  evidence:           [cite stage artifact(s) by path that support this resolution]

  Verdict cap rule: If resolution = OPEN RISK, the overall verdict cannot exceed
  "partially supported". Apply before stating the overall verdict.

DISPLACEMENT VERDICT (required):
  displacement_question: [copy from SETUP verbatim]
  displacement_verdict:  [Yes / Partially / No -- one sentence citing the CLAIM CHAIN
                          TABLE pattern, counter-hypothesis resolution, and grounded
                          claims only]

State overall verdict and confidence in one sentence.

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-05 -- Full Integration (all three axes + complete R13 V-05 baseline)

**Axis**: counter_hypothesis_resolution + scout_signal_mapping + evidence_type_tagging
**Structural baseline**: full R13 V-05 (ARTIFACT PATH TABLE, displacement frame in SETUP,
scout gate with scout_source in hypothesis frontmatter, CLAIM INDEX, inline THIN flags with
weakens: CLAIM-N, COUNT GATEs at Stages 2-3, CLAIM IMPACT TABLE at Stage 4, CLAIM CHAIN
TABLE at Stage 5, DISPLACEMENT VERDICT at Stage 5)

**Hypothesis**: All three new axes are additive on the R13 V-05 baseline. Counter-hypothesis
resolution adds adversarial testing without changing evidence mechanics (V-01). Scout signal
mapping adds grounding traceability without changing the stage structure (V-02). Evidence type
tagging adds breadth verification without changing count floor mechanics (V-03). The combined
prompt scores 100 on v14 because all R13 V-05 structural guarantees are preserved, and it
surfaces three candidate v16 criteria: C-14 (counter-hypothesis resolved at Stage 5), C-15
(every claim scout-anchored), C-16 (at least 2 evidence types across Stages 2-3).

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

## EVIDENCE TYPE REGISTER (declared at campaign open)

Valid evidence types: MARKET / TECHNICAL / USER / ACADEMIC
Minimum breadth rule: at least 2 distinct types must appear across Stages 2 and 3 combined.
Stage 5 verifies. If fewer than 2 types: emit EVIDENCE BREADTH WARNING and cap confidence at Medium.

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
2. COUNTER-HYPOTHESIS: the incumbent's strongest single-sentence rebuttal -- why
   {status_quo_comparator} will resist displacement. Write before forming the CLAIM
   INDEX; let the counter-hypothesis sharpen or constrain the claims. Stage 5 resolves
   it explicitly.
3. CLAIM INDEX:
   CLAIM-1: [sub-claim -- one sentence, testable by evidence]
   CLAIM-2: [sub-claim -- one sentence, testable by evidence]
   CLAIM-3: [sub-claim -- one sentence, testable by evidence]
   (3-5 claims total)
   THIN flags at Stages 2 and 3 must reference these IDs.
   CLAIM CHAIN TABLE at Stage 5 closes the loop per claim from hypothesis to verdict.
4. SCOUT SIGNAL MAP (required -- one row per claim):

   | Claim ID | Scout Section           | Scout Signal (1 sentence -- direct from scout) |
   |----------|-------------------------|------------------------------------------------|
   | CLAIM-1  | [section name or header]| [exact finding from scout artifact]            |
   | CLAIM-2  | ...                     | ...                                            |
   | CLAIM-3  | ...                     | ...                                            |

   Rule: Every claim must trace to a named section in scout_source. A claim with no
   scout anchor is speculation. Mark it UNGROUNDED; it is excluded from the verdict.

Reference scout_source explicitly in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [full path from SETUP -- copied verbatim, not inferred]

Emit: STAGE-1 CLEARED.

---

## STAGE 2 -- WEBSEARCH

GATE CHECK: STAGE-1 CLEARED emitted? If not: BLOCKED. Halt.

Gather external evidence for each claim in the CLAIM INDEX. Minimum 3 external
sources. For each source:
- Assess whether it supports displacement of {status_quo_comparator} by {topic}.
- Note evidence bearing on the COUNTER-HYPOTHESIS.
- Tag the source with its evidence type: MARKET / TECHNICAL / USER / ACADEMIC

When evidence is thin, conflicting, or absent for any claim, flag immediately:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

Do not defer THIN flags. Emit at point of discovery.

Running type set: [types seen so far this stage]

COUNT GATE: Do not fire STAGE-2 CLEARED until 3 or more sources have been assessed.
If fewer than 3 sources found, gather additional sources before proceeding.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: STAGE-2 CLEARED. (sources assessed: [N], types: [set of types seen])

---

## STAGE 3 -- INTELLIGENCE

GATE CHECK: STAGE-2 CLEARED emitted? If not: BLOCKED. Halt.

Search internal sources -- existing signal artifacts, related topics, prior runs --
for evidence relevant to each claim and to the COUNTER-HYPOTHESIS. Minimum 2
internal sources. For each source:
- Tag the source with its evidence type: MARKET / TECHNICAL / USER / ACADEMIC
- Apply the same THIN annotation:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

Running type set: [cumulative distinct types across Stages 2 and 3]

COUNT GATE: Do not fire STAGE-3 CLEARED until 2 or more internal sources have been
assessed. If fewer than 2 found, widen the search before proceeding.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: STAGE-3 CLEARED. (sources assessed: [N], cumulative types: [set])

---

## STAGE 4 -- ANALYSIS

GATE CHECK: STAGE-3 CLEARED emitted? If not: BLOCKED. Halt.

Aggregate all THIN flags from Stages 2 and 3 into a CLAIM IMPACT TABLE:

| Flag    | Source Stage | Evidence Type | Area | Gap | Claim Weakened |
|---------|-------------|---------------|------|-----|----------------|
| THIN-01 | S2          | MARKET        | ...  | ... | CLAIM-N        |

If no THIN flags: one row -- "no THIN flags found across Stages 2-3".

For each claim in the CLAIM INDEX, state evidence status:
  SUPPORTED / WEAKENED (has one or more THIN flags) / UNSUPPORTED / UNGROUNDED

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: STAGE-4 CLEARED.

---

## STAGE 5 -- SYNTHESIZE

GATE CHECK: STAGE-4 CLEARED emitted? If not: BLOCKED. Halt.

EVIDENCE BREADTH CHECK (required before verdict):
  types_seen: [list all distinct evidence types across Stages 2 and 3]
  breadth_count: [number of distinct types]
  If breadth_count < 2:
    Emit: EVIDENCE BREADTH WARNING -- only [N] evidence type(s) represented.
    Verdict confidence is capped at Medium across all claims.
  Else:
    Emit: EVIDENCE BREADTH CONFIRMED -- [N] distinct types.

State the overall verdict: supported / partially supported / not supported.
Exclude UNGROUNDED claims from the verdict calculation.

CLAIM CHAIN TABLE (required -- one row per claim):

| Claim ID | Claim (one sentence) | Scout Anchor    | THIN Flags Found | Source Stage | Stage 4 Status | Adjusted Confidence |
|----------|----------------------|-----------------|-----------------|-------------|----------------|---------------------|
| CLAIM-1  | ...                  | [scout section] | THIN-01, ...    | S2 / S3     | SUPPORTED / WEAKENED / UNSUPPORTED | Low / Med / High |
| CLAIM-2  | ...                  | [scout section] | none            | n/a         | SUPPORTED      | High                |
| CLAIM-3  | ...                  | UNGROUNDED      | n/a             | n/a         | UNGROUNDED     | excluded            |

Rules:
- "Scout Anchor" must copy the section from Stage 1's SCOUT SIGNAL MAP.
- "THIN Flags Found" must cite flag IDs from Stage 4's CLAIM IMPACT TABLE. Write "none" if none.
- "Source Stage" must match Stage 4's CLAIM IMPACT TABLE.
- "Stage 4 Status" must copy the exact status word from Stage 4 -- no new assessment.
- WEAKENED or UNSUPPORTED claims: confidence = Low or Med only.
- SUPPORTED claims with no THIN flags: confidence = High.
- UNGROUNDED claims: confidence = excluded.
- If EVIDENCE BREADTH WARNING fired: no claim may carry High confidence.

COUNTER-HYPOTHESIS RESOLUTION (required):
  counter_hypothesis: [restate from Stage 1 verbatim -- do not paraphrase]
  resolution:         [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  evidence:           [cite stage artifact(s) by path that support this resolution]

  Verdict cap rule: If resolution = OPEN RISK, the overall verdict cannot exceed
  "partially supported". Apply before stating the overall verdict.

DISPLACEMENT VERDICT (required):
  displacement_question: [copy from SETUP verbatim]
  displacement_verdict:  [Yes / Partially / No -- one sentence citing the CLAIM CHAIN
                          TABLE pattern, counter-hypothesis resolution outcome, and
                          evidence breadth status]

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
| C-07 scout anchor in hypothesis artifact | PASS | PASS+ | PASS | PASS+ | PASS+ |
| C-08 evidence gaps flagged at discovery | PASS | PASS | PASS | PASS | PASS |
| C-09 thin-evidence propagates to synthesis | PASS+ | PASS+ | PASS+ | PASS+ | PASS+ |
| C-10 hypothesis structurally blocked | PASS | PASS | PASS | PASS | PASS |
| **Candidate C-14** counter-hypothesis resolved | YES | - | - | YES | YES |
| **Candidate C-15** claims scout-anchored | - | YES | - | YES | YES |
| **Candidate C-16** 2+ evidence types | - | - | YES | - | YES |

**V-01**: COUNTER-HYPOTHESIS at Stage 1 + COUNTER-HYPOTHESIS RESOLUTION at Stage 5 with
verdict cap rule. All 10 v14 criteria maintain PASS. C-07 standard PASS (scout_source in
frontmatter, body reference). C-09 PASS+ because the counter-hypothesis resolution adds
a second tracked thread to the synthesis alongside the CLAIM CHAIN TABLE. Candidate C-14 fires.

**V-02**: SCOUT SIGNAL MAP at Stage 1 makes every claim trace to a named scout section.
CLAIM CHAIN TABLE at Stage 5 gains "Scout Anchor" column. C-07 PASS+ because the scout
anchor is now auditable per-claim, not just as a file reference. C-09 PASS+ because the
UNGROUNDED exclusion rule makes the claim chain structurally tighter. Candidate C-15 fires.

**V-03**: Evidence type tagging at Stages 2-3, running type set in CLEARED emits, EVIDENCE
BREADTH CHECK at Stage 5, breadth-based confidence cap. All v14 mechanics preserved.
CLAIM IMPACT TABLE gains an Evidence Type column. C-09 PASS+ because the breadth warning
and confidence cap add a new dimension to thin-evidence propagation. Candidate C-16 fires.

**V-04**: V-01 + V-02. Counter-hypothesis resolution + scout signal mapping. Both candidates
(C-14, C-15) fire. C-07 PASS+ from scout signal map. C-09 PASS+ from both threads (counter
resolution + CLAIM CHAIN with scout anchors). Expected: 100 on v14 + candidates.

**V-05**: All three axes on R13 V-05 baseline. All three candidates (C-14, C-15, C-16) fire
simultaneously. C-07 PASS+ from scout signal map. C-09 PASS+ from all three reinforcing
threads. Displacement framing from R13 V-05 baseline sharpens every stage. Expected: 100
on v14 + all three candidates.

**R14 thesis**: If V-04 and V-05 both score 100 on v14, the three new axes are confirmed
additive. V-05 becomes the proposed v15-stack baseline with six candidate criteria total:
C-11 (count-gated exits), C-12 (claim chain), C-13 (displacement verdict) from R13, plus
C-14 (counter-hypothesis resolution), C-15 (scout-anchored claims), C-16 (evidence breadth)
from R14. Next step: quest-rubric to formalize which of the six candidates earn promotion.
