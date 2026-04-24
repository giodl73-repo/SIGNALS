---
skill: quest-variate
skill_target: prove-topic
round: R15
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [role_sequence, output_format, lifecycle_emphasis]
  combined: [V-04 (phrasing_register + inertia_framing), V-05 (all_four)]
r14_anchor: >
  R14 V-05 (the current T3 champion) satisfies a deep stack of structural criteria
  (C-01 through C-39 under rubric v13) using SESSION INVARIANTS, ROLE OWNERSHIP TABLE,
  ATOMIC DUAL-LOCK, and INCUMBENT CHECK tables. However the T3 champion uses
  hypothesis -> websearch -> interview -> prototype -> synthesis, which FAILS rubric v14
  C-01: the correct sequence is prove-hypothesis -> prove-websearch -> prove-intelligence
  -> prove-analysis -> prove-synthesize. All R15 variations use the correct sequence and
  rebuild structural machinery around intelligence (internal source scan) and analysis
  (pattern/causation analysis) replacing interview and prototype.
r15_targets: >
  R15 variation axes:

  V-01 (single: role_sequence): Three named roles execute in numbered dependency order
  before Stage 1. ROLE 1 = SCOUT LOADER (names scout artifact, gates Stage 1). ROLE 2 =
  INERTIA ANALYST (names comparator, runs after ROLE 1). ROLE 3 = CAMPAIGN DIRECTOR
  (confirms both roles, opens campaign). Tests whether pre-stage role sequence makes
  C-02 (scout named before hypothesis) structurally enforced rather than advisory.

  V-02 (single: output_format): Every stage outputs a structured Markdown table with
  rated columns. Stage 2 table: Source | Key Quote | Strength (Strong/Moderate/Weak) |
  Supports? (Y/N/Partial). Stage 3 table: File | Section | Finding | Relevant? Stage 4
  table: Pattern | Sources | Causal? | Confidence. Synthesis confidence expressed as
  1-10 score with explicit calculation (base minus counter-evidence penalty). Tests
  whether table format improves evidence traceability (C-03, depth criteria).

  V-03 (single: lifecycle_emphasis): Every stage has three explicit structural markers:
  ENTRY CONDITIONS (checklist), STAGE BODY, and EXIT SIGNAL with named handoff field.
  Gate before Stage 1 holds campaign until scout_loaded = true. Stage progression is
  explicit: a stage body may not begin until its EXIT SIGNAL from the prior stage is
  printed. Tests whether explicit forward-sequence gating maximizes C-01 and C-03
  compliance.

  V-04 (combined: phrasing_register + inertia_framing): Conversational/imperative
  register — short sentences, direct commands, minimal structural decoration. Status-quo
  comparator named in SETUP as "what teams do today instead of {topic}." Each stage ends
  with a displacement read question ("does this evidence support replacing
  {status_quo_comparator}?"). Synthesis opens with a direct verdict and explicitly names
  the displacement conclusion. Tests whether plain-language orchestration preserves
  essential criteria while reducing prompt complexity.

  V-05 (combined: all_four): Numbered dependency chain for pre-stage roles (V-01 role
  structure), table format for all evidence stages (V-02 output format), entry
  conditions + exit signals at every boundary (V-03 lifecycle), displacement question
  template applied verbatim to each evidence row (V-04 inertia framing). Tests whether
  maximum structural density can satisfy the full v14 criterion stack in a single prompt.
---

# prove-topic — Variate Round 15

**Skill**: prove-topic
**Rubric**: v14 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-10 aspirational)
**Date**: 2026-03-16
**Round**: 15

---

## Context: what informed this round

The R14 T3 champion (`prove-topic.t3/SKILL.md`) satisfies deep structural criteria
(SESSION INVARIANTS, ROLE OWNERSHIP, ATOMIC DUAL-LOCK) but uses the **wrong stage
sequence**: hypothesis -> websearch -> **interview** -> **prototype** -> synthesis.

Rubric v14 C-01 requires: hypothesis -> websearch -> **intelligence** -> **analysis** ->
synthesize.

R15 resets the stage sequence to the correct v14 target and rebuilds structural
innovations (roles, gates, exit signals, inertia framing) around the two corrected
evidence stages:

- **Stage 3**: prove-intelligence — internal source scan with file-path citations
- **Stage 4**: prove-analysis — data pattern analysis, causation vs correlation

| Var | Axis | Primary criteria targeted |
|-----|------|--------------------------|
| V-01 | Role sequence | C-01, C-02 |
| V-02 | Output format | C-01, C-03, depth criteria |
| V-03 | Lifecycle emphasis | C-01, C-03, C-04 |
| V-04 | Phrasing register + Inertia framing | C-01, C-02, C-04, inertia depth |
| V-05 | All four axes combined | C-01 through C-04 + aspirational |

**Artifact paths (all variations)**:

| Stage | Sub-skill | Artifact path |
|-------|-----------|---------------|
| 1 | prove-hypothesis | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` |
| 2 | prove-websearch | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` |
| 3 | prove-intelligence | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |
| 4 | prove-analysis | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` |
| 5 | prove-synthesize | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md` |

---

## V-01 — Role Sequence

**Axis**: Role sequence
**Hypothesis**: Making the scout load a structural gate owned by a named role (ROLE 1),
followed by a separate inertia analysis role (ROLE 2), followed by a campaign director
(ROLE 3) that confirms both — enforces C-02 (scout named before hypothesis) as a
blocking dependency rather than advisory text.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Orchestrates five stages in order:
prove-hypothesis -> prove-websearch -> prove-intelligence -> prove-analysis ->
prove-synthesize. Three named roles execute pre-stage in numbered dependency order.
One artifact written per stage. Final output: evidence brief ready for /topic-story.

---

## CAMPAIGN OPEN

  topic:  {topic}
  date:   {date}

### PRE-STAGE ROLE EXECUTION

Three roles execute in numbered order. Each role owns one gate field. A later role
cannot execute until the prior role confirms its field. All three must confirm before
Stage 1 begins.

ROLE 1 — SCOUT LOADER (Step 1 of 3 — executes first)
  Responsibility: Locate and confirm the scout artifact for this topic.
  scout_artifact:  [{topic}-scout-record-{date}.md — or most recent scout signal for {topic}]
  scout_loaded:    [true / false]
  ROLE 1 STATUS:   [CONFIRMED — scout_artifact named and scout_loaded = true]
                   [BLOCKED — record which file was searched; halt campaign]

ROLE 2 — INERTIA ANALYST (Step 2 of 3 — requires ROLE 1 CONFIRMED)
  Dependency: ROLE 1 must be CONFIRMED before ROLE 2 executes.
  Responsibility: Name what {topic} must displace and analyze the incumbent.
  status_quo_comparator:  [incumbent approach {topic} replaces]
  comparator_strength:    [one sentence: why the incumbent wins today]
  comparator_exposure:    [one sentence: where the incumbent is most vulnerable to {topic}]
  ROLE 2 STATUS:          [CONFIRMED]

ROLE 3 — CAMPAIGN DIRECTOR (Step 3 of 3 — requires ROLES 1 and 2 CONFIRMED)
  Dependency: ROLES 1 and 2 must both be CONFIRMED before ROLE 3 executes.
  Responsibility: Confirm pre-stage checks complete and open the campaign.
  role_1_confirmed:  [true]
  role_2_confirmed:  [true]
  PRE-STAGE EXIT:    "PRE-STAGE COMPLETE — All three roles confirmed. Campaign open.
                      Advancing to Stage 1."

Do not begin Stage 1 until PRE-STAGE EXIT is printed.

---

## STAGE 1 — HYPOTHESIS

Load scout_artifact confirmed by ROLE 1. Read signals. Frame hypothesis.

  source_artifact:    [path — copied from ROLE 1 output, not re-inferred]
  hypothesis:         [falsifiable claim derived from scout signals]
  counter_hypothesis: [strongest argument that {topic} fails to displace the incumbent,
                       grounded in ROLE 2 comparator_strength]
  confidence_prior:   [Low / Medium / High — before gathering evidence]

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. STAGE 1 COMPLETE.

---

## STAGE 2 — WEB SEARCH

Gather minimum 3 external sources. For each source record the item, summary, and whether
it supports the hypothesis.

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | SUPPORTS? (Y / N / Partial)
  1    | [source]                 | [summary]            | [verdict]
  2    | [source]                 | [summary]            | [verdict]
  3    | [source]                 | [summary]            | [verdict]
  add  |                          |                      |

  s2_support_tally:  [N support / M counter / P partial]
  s2_key_gap:        [what external evidence does not cover]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. STAGE 2 COMPLETE.

---

## STAGE 3 — INTELLIGENCE

Search internal sources: codebase, specs, docs, prior signal artifacts.
For each internal source, record the file path, relevant section, and finding.

  FILE PATH          | SECTION         | FINDING (1 sentence) | RELEVANT? (Y/N)
  [path]             | [section]       | [finding]            | [verdict]
  add rows as needed

  s3_sources_found:  [N internal sources with relevant evidence]
  s3_alignment:      [ALIGNED / CONTRADICTS / MIXED — vs Stage 2 web evidence]
  s3_key_gap:        [what internal sources do not address]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. STAGE 3 COMPLETE.

---

## STAGE 4 — ANALYSIS

Analyze patterns across the full evidence set (Stages 2 + 3).
Distinguish correlation from causation. Cite sources for each claim.

  PATTERN            | EVIDENCE SOURCES (S2 item# / S3 filepath) | CAUSAL?        | CONFIDENCE
  [pattern]          | [sources]                                  | Yes/No/Unknown | Low/Med/High
  add rows as needed

  s4_primary_finding:   [1-2 sentences: dominant pattern across all evidence]
  s4_counter_evidence:  [strongest evidence that contradicts the hypothesis — cite artifact]
  s4_causal_claim:      [what can be asserted causal vs correlational]

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. STAGE 4 COMPLETE.

---

## STAGE 5 — SYNTHESIS

Resolve the hypothesis against the full evidence record. Answer first.

  hypothesis_verdict:   [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:     [2-3 sentences integrating Stages 2, 3, 4]
  confidence_final:     [Low / Medium / High — with one-sentence reasoning]
  key_risk:             [primary risk to adoption or correctness]

Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write. CAMPAIGN COMPLETE.

STAGE 5 EXIT: synthesis_complete — Evidence brief complete. Ready for /topic-story.
```

---

## V-02 — Output Format

**Axis**: Output format
**Hypothesis**: Structured Markdown tables with rated columns at every evidence stage —
plus a numerical 1-10 confidence score with explicit calculation at synthesis — improve
evidence traceability and make scoring against depth criteria more reliable.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Five stages in order:
prove-hypothesis -> prove-websearch -> prove-intelligence -> prove-analysis ->
prove-synthesize. Scout artifact named before hypothesis. One artifact written per stage.
Final output: evidence brief ready for /topic-story.

---

## CAMPAIGN HEADER

| Field | Value |
|-------|-------|
| topic | {topic} |
| date | {date} |
| scout_artifact | [{topic}-scout-record-{date}.md — locate most recent scout signal for {topic}] |
| status_quo_comparator | [name the incumbent approach {topic} must displace] |

Load scout_artifact now. If not found, halt and record which file was searched.
Fill status_quo_comparator before advancing.

---

## STAGE 1 — HYPOTHESIS

Read the scout artifact from the Campaign Header. Use its signals to frame the hypothesis.

| Field | Value |
|-------|-------|
| source_artifact | [scout_artifact path — copied from header, not re-inferred] |
| hypothesis | [falsifiable claim derived from scout signals] |
| counter_hypothesis | [incumbent's best defense against {topic}] |
| confidence_prior | [1-10 scale — before evidence gathering] |

Write: `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`
Confirm write before advancing to Stage 2.

---

## STAGE 2 — WEB SEARCH

Gather minimum 3 external sources. Enter each row fully before proceeding.

| # | Source (URL or citation) | Key Quote or Finding | Strength | Supports Hypothesis? |
|---|--------------------------|----------------------|----------|----------------------|
| 1 | | | Strong / Moderate / Weak | Y / N / Partial |
| 2 | | | Strong / Moderate / Weak | Y / N / Partial |
| 3 | | | Strong / Moderate / Weak | Y / N / Partial |
| + | add rows as needed | | | |

| Summary Field | Value |
|---------------|-------|
| s2_evidence_count | [N rows total] |
| s2_strength_tally | [Strong: N, Moderate: M, Weak: P] |
| s2_support_tally | [Y: N, N: M, Partial: P] |
| s2_key_gap | [what external evidence does not address] |

Write: `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`
Confirm write before advancing to Stage 3.

---

## STAGE 3 — INTELLIGENCE

Search internal sources: codebase, specs, docs, prior signal artifacts.
Enter each row fully before proceeding.

| # | File or Artifact | Section | Finding (1 sentence) | Relevant? | Aligns with Web? |
|---|-----------------|---------|----------------------|-----------|-----------------|
| 1 | | | | Y / N | Y / N / Contradicts |
| 2 | | | | Y / N | Y / N / Contradicts |
| 3 | | | | Y / N | Y / N / Contradicts |
| + | add rows as needed | | | | |

| Summary Field | Value |
|---------------|-------|
| s3_sources_scanned | [N files/artifacts examined] |
| s3_relevant_count | [M sources with relevant findings] |
| s3_alignment | [ALIGNED / CONTRADICTS / MIXED — vs Stage 2 web evidence] |
| s3_key_gap | [what internal sources do not address] |

Write: `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`
Confirm write before advancing to Stage 4.

---

## STAGE 4 — ANALYSIS

Analyze patterns across the full evidence set (Stages 2 + 3).
Distinguish causation from correlation. Cite by stage and item number or file path.

| # | Pattern | Evidence Sources | Causal? | Confidence (1-10) |
|---|---------|-----------------|---------|-------------------|
| 1 | | S2-row# / S3-file | Yes / No / Unknown | |
| 2 | | | | |
| 3 | | | | |
| + | add rows as needed | | | |

| Summary Field | Value |
|---------------|-------|
| s4_primary_finding | [dominant pattern, 1-2 sentences] |
| s4_counter_evidence | [strongest evidence against hypothesis — cite artifact + section] |
| s4_causation_claim | [what is asserted causal vs correlational] |

Write: `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`
Confirm write before advancing to Stage 5.

---

## STAGE 5 — SYNTHESIS

Produce the answer-first evidence brief with numerical confidence scoring.

| Field | Value |
|-------|-------|
| hypothesis_verdict | SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED |
| confidence_base | [1-10 — from strength of primary evidence] |
| counter_evidence_penalty | [-N — one point per strong counter-evidence item found] |
| confidence_final | [confidence_base + counter_evidence_penalty] |
| confidence_calculation | base: [N], penalty: -[M], final: [P] |
| evidence_summary | [2-3 sentences integrating Stages 2, 3, 4] |
| key_risk | [primary adoption or correctness risk] |
| readiness | Evidence brief complete. Ready for /topic-story. |

Write: `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`
Confirm write. CAMPAIGN COMPLETE.

EXIT: synthesis_complete — evidence brief ready for /topic-story.
```

---

## V-03 — Lifecycle Emphasis

**Axis**: Lifecycle emphasis
**Hypothesis**: Three-site enforcement per stage — ENTRY CONDITIONS checklist before the
stage body, STAGE WRITE confirmation inside the body, and a named EXIT SIGNAL with a
handoff field after it — maximizes forward-sequence compliance (C-01) and progressive
write compliance (C-03) by making each boundary a blocking gate rather than advisory
text.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Five stages in strict forward sequence:
prove-hypothesis -> prove-websearch -> prove-intelligence -> prove-analysis ->
prove-synthesize. Scout artifact loaded and named before Stage 1. One artifact written
per stage; write confirmed before stage exit. Final output: evidence brief ready for
/topic-story.

Interrupted campaigns: find the most recent artifact for this topic in simulations/prove/.
Identify the last stage that confirmed a write. Resume from the first stage whose
artifact is missing.

---

## CAMPAIGN OPEN

  topic:  {topic}
  date:   {date}

SCOUT LOAD — complete before entering the gate:
  scout_artifact:  [{topic}-scout-record-{date}.md — or most recent scout signal for {topic}]
  scout_loaded:    [true if artifact found; false if not found — record search path if false]

CAMPAIGN GATE:
  [ ] topic and date filled
  [ ] scout_artifact identified and scout_loaded = true
  [ ] status_quo_comparator named: [incumbent approach {topic} must displace]

If any gate item is unchecked: CAMPAIGN BLOCKED — record which item halted the campaign.

GATE EXIT: campaign_open
  "GATE CLEAR — scout loaded, comparator named. Advancing to Stage 1."
Do not begin Stage 1 until GATE EXIT is printed.

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] GATE EXIT received: campaign_open
  [ ] scout_artifact path available from SCOUT LOAD

STAGE 1 BODY:
Load scout_artifact. Read its signals. Frame hypothesis grounded in those signals.

  source_artifact:    [path — copied from SCOUT LOAD above, not re-inferred]
  hypothesis:         [falsifiable claim derived from scout signals]
  counter_hypothesis: [incumbent's best defense — grounded in status_quo_comparator]
  confidence_prior:   [Low / Medium / High]

STAGE 1 WRITE:
  Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Confirm write: [{topic}-prove-hypothesis-{date}.md written]

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked — {topic}-prove-hypothesis-{date}.md written.
   Stage 2 entry conditions satisfied."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] hypothesis artifact confirmed written

STAGE 2 BODY:
Gather minimum 3 external sources. For each source record the item and its relevance.

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | SUPPORT (Y / N / Partial) | STRENGTH
  1    | [source]                 | [summary]            | [verdict]                 | [S/M/W]
  2    | [source]                 | [summary]            | [verdict]                 | [S/M/W]
  3    | [source]                 | [summary]            | [verdict]                 | [S/M/W]
  add  |                          |                      |                           |

  s2_support_tally:  [N support / M counter / P partial]
  s2_key_gap:        [what external evidence does not cover]

STAGE 2 WRITE:
  Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Confirm write: [{topic}-prove-websearch-{date}.md written]

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete — s2_support_tally = [value].
   Stage 3 entry conditions satisfied."

---

## STAGE 3 — INTELLIGENCE

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_support_tally recorded (not blank)

STAGE 3 BODY:
Search internal sources: codebase, specs, docs, prior signal artifacts.
For each relevant source, record file path, section, and finding.

  FILE PATH          | SECTION         | FINDING (1 sentence) | RELEVANCE (High/Med/Low)
  [path]             | [section]       | [finding]            | [relevance]
  add rows as needed

  s3_sources_found:  [N internal sources with relevant evidence]
  s3_alignment:      [ALIGNED / CONTRADICTS / MIXED — vs Stage 2 web evidence]
  s3_key_gap:        [what internal sources do not address]

STAGE 3 WRITE:
  Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Confirm write: [{topic}-prove-intelligence-{date}.md written]

STAGE 3 EXIT SIGNAL: intelligence_complete
  "STAGE 3 EXIT: intelligence_complete — s3_sources_found = [N].
   Stage 4 entry conditions satisfied."

---

## STAGE 4 — ANALYSIS

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: intelligence_complete
  [ ] s3_sources_found recorded (not blank)

STAGE 4 BODY:
Analyze patterns across Stages 2 + 3. Distinguish correlation from causation.
For each pattern, cite the evidence sources that establish it.

  PATTERN            | SOURCES (S2 item# / S3 filepath) | CAUSAL?        | CONFIDENCE
  [pattern]          | [sources]                        | Yes/No/Unknown | Low/Med/High
  add rows as needed

  s4_primary_finding:   [dominant pattern across all evidence, 1-2 sentences]
  s4_counter_evidence:  [strongest evidence against hypothesis — cite artifact + section]
  s4_causal_claim:      [what is asserted causal vs correlational]

STAGE 4 WRITE:
  Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Confirm write: [{topic}-prove-analysis-{date}.md written]

STAGE 4 EXIT SIGNAL: analysis_complete
  "STAGE 4 EXIT: analysis_complete — s4_primary_finding locked.
   Stage 5 entry conditions satisfied."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: analysis_complete
  [ ] counter_hypothesis from Stage 1 available for resolution
  [ ] s4_primary_finding recorded

STAGE 5 BODY:

COUNTER-HYPOTHESIS RESOLUTION:
  counter_hypothesis:  [from Stage 1]
  resolution_verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  resolution_evidence: [cite stage artifact that resolves it]

Open Risk: if resolution_verdict = OPEN RISK, note the unresolved risk explicitly in key_risk.

SYNTHESIS:
  hypothesis_verdict:  [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:    [2-3 sentences integrating Stages 2, 3, 4]
  confidence_final:    [Low / Medium / High — with one-sentence reasoning]
  key_risk:            [primary risk remaining after evidence review]

STAGE 5 WRITE:
  Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
  Confirm write: [{topic}-prove-synthesize-{date}.md written]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief complete. Ready for /topic-story."

CAMPAIGN COMPLETE.
```

---

## V-04 — Phrasing Register + Inertia Framing

**Axis**: Phrasing register (conversational/imperative) + inertia framing
**Hypothesis**: A conversational, imperative-mode register — short sentences, direct
commands, minimal structural decoration — with the status-quo comparator named up front
and a displacement read question at the close of each evidence stage preserves the
essential criteria with lower prompt complexity and better signal-to-noise.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

You're running a full evidence campaign for {topic}. The campaign builds the case that
{topic} is worth building — which means proving it's better than what teams use today.

Run five stages in this exact order. Do not skip stages. Do not reorder them.
  1. Frame the hypothesis
  2. Search the web for evidence
  3. Scan internal sources
  4. Analyze the patterns
  5. Synthesize the answer

Write one artifact after each stage. Do not batch writes.

---

## SETUP

Fill this before running any stage.

  topic:                  {topic}
  date:                   {date}
  status_quo_comparator:  [what teams currently do instead of {topic}]
  comparator_strength:    [one sentence: why the status quo works well enough]
  comparator_weakness:    [one sentence: where the status quo fails]

Now find the scout artifact for this topic. It is named something like
`{topic}-scout-record-{date}.md`. If you have a different scout signal file, name it.
You must name the file before running Stage 1.

  scout_artifact: [path to the scout signal file]

If you cannot find a scout artifact: stop here. Record what you searched and halt.

---

## STAGE 1 — FRAME THE HYPOTHESIS

Read the scout artifact named above. Use its signals.

Write a hypothesis: a single falsifiable claim about {topic}.
Write the counter-hypothesis: the best argument that {topic} will not displace
{status_quo_comparator}.

  hypothesis:         [your claim — falsifiable, derived from scout signals]
  counter_hypothesis: [the incumbent's best defense]

Write to: `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`
Confirm the write before moving to Stage 2.

---

## STAGE 2 — SEARCH THE WEB

Find at least 3 external sources that bear on the hypothesis.

For each source:
- What is the source?
- What does it say in one sentence?
- Does it support the hypothesis? Yes / No / Partial

After you have all sources, answer: does the web evidence support replacing
{status_quo_comparator} with {topic}?

  s2_displacement_read: [web evidence says: support / counter / mixed]

Write to: `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`
Confirm the write before moving to Stage 3.

---

## STAGE 3 — SCAN INTERNAL SOURCES

Search the repo: specs, docs, code, prior signal artifacts. Find what is relevant to
the hypothesis.

For each source you find, record:
- File path
- What you found (one sentence)
- Whether it strengthens or weakens the case for {topic}

After scanning, answer: does the internal evidence support replacing
{status_quo_comparator} with {topic}?

  s3_displacement_read: [internal evidence says: support / counter / mixed]
  s3_new_vs_web:        [did you find something not covered by web evidence? yes / no]

Write to: `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`
Confirm the write before moving to Stage 4.

---

## STAGE 4 — ANALYZE THE PATTERNS

Pull together everything from Stages 2 and 3.

For each pattern you identify:
- What is the pattern?
- Is it causal or correlational? Be honest about the distinction.
- Which sources establish it? Cite by stage and item.

Then address the counter-hypothesis directly. Does the evidence refute it, partly refute
it, or leave it as an open risk?

  s4_counter_hypothesis_status: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  s4_primary_pattern:           [the clearest signal across all evidence, 1-2 sentences]

Write to: `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`
Confirm the write before moving to Stage 5.

---

## STAGE 5 — SYNTHESIZE

Answer first.

  verdict:            [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  confidence:         [Low / Medium / High]
  displacement_case:  [1-2 sentences: does the evidence support replacing
                        {status_quo_comparator} with {topic}? Say yes, no, or conditional.]
  summary:            [2-3 sentences: what the evidence established]
  key_risk:           [what could still prevent {topic} from displacing {status_quo_comparator}]

Write to: `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`
Confirm the write.

Evidence brief complete. Ready for /topic-story.
```

---

## V-05 — All Four Axes Combined

**Axes**: Role sequence + Output format + Lifecycle emphasis + Inertia framing
**Hypothesis**: Combining numbered dependency-chain roles (V-01), table evidence format
with displacement check columns (V-02/V-04), and explicit entry conditions + exit signals
at every boundary (V-03) produces a prompt that satisfies the full v14 essential stack
plus recommended/aspirational criteria in a single coherent prompt.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Three named roles execute pre-stage
in numbered dependency order. Five evidence stages in strict sequence:
prove-hypothesis -> prove-websearch -> prove-intelligence -> prove-analysis ->
prove-synthesize. Each stage has entry conditions, a table-format evidence body, and
a named exit signal. One artifact written per stage. Final output: evidence brief
ready for /topic-story.

---

## CAMPAIGN OPEN

  topic:  {topic}
  date:   {date}

---

### PRE-STAGE: NAMED ROLE EXECUTION (Steps 1–3)

Three roles execute in numbered order. Each role owns one field. A later role cannot
execute until the prior role confirms its field. All three must confirm before Stage 1.

---

**ROLE 1 — SCOUT LOADER** (Step 1 of 3 — executes first)

Rationale: The scout artifact must be found before ROLE 2 can ground the incumbent
analysis, and before the hypothesis can be framed from real signals.

| Field | Value |
|-------|-------|
| scout_artifact | [{topic}-scout-record-{date}.md — or most recent scout signal for {topic}] |
| scout_loaded | [true / false] |
| ROLE 1 STATUS | [CONFIRMED] or [BLOCKED — record search path] |

If scout_loaded = false: halt. CAMPAIGN BLOCKED. Do not advance to ROLE 2.

---

**ROLE 2 — INERTIA ANALYST** (Step 2 of 3 — requires ROLE 1 CONFIRMED)

Rationale: The incumbent must be named and analyzed before displacement checks can be
applied to evidence, and before ROLE 3 can register the displacement question template.

| Field | Value |
|-------|-------|
| status_quo_comparator | [incumbent approach {topic} must displace] |
| comparator_strength | [one sentence: why the incumbent wins today] |
| comparator_vulnerability | [one sentence: where the incumbent is most exposed to {topic}] |
| ROLE 2 STATUS | [CONFIRMED] |

---

**ROLE 3 — CAMPAIGN DIRECTOR** (Step 3 of 3 — requires ROLES 1 + 2 CONFIRMED)

Rationale: Confirms pre-stage complete. Registers the displacement question template
used verbatim in every evidence stage's displacement check column.

Displacement question template (active for all stages):
  "Does [evidence item] support the displacement of {status_quo_comparator}
   by {topic}? [Yes / No / Inconclusive]"

| Field | Value |
|-------|-------|
| role_1_confirmed | true |
| role_2_confirmed | true |
| displacement_template_registered | true |
| CAMPAIGN STATUS | OPEN |

**PRE-STAGE EXIT: campaign_open — "Roles 1, 2, 3 confirmed. Displacement template registered.
Advancing to Stage 1."**

Do not begin Stage 1 until PRE-STAGE EXIT is printed.

---

## STAGE 1 — HYPOTHESIS

**STAGE 1 ENTRY CONDITIONS:**
- [ ] PRE-STAGE EXIT received: campaign_open
- [ ] scout_artifact path available from ROLE 1

**STAGE 1 BODY:**

Load scout_artifact. Read its signals.

| Field | Value |
|-------|-------|
| source_artifact | [path — copied from ROLE 1, not re-inferred] |
| hypothesis | [falsifiable claim derived from scout signals] |
| counter_hypothesis | [incumbent's best defense — grounded in ROLE 2 comparator analysis] |
| confidence_prior | [Low / Medium / High] |

**WRITE:** `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`
Confirm write.

**STAGE 1 EXIT: hypothesis_locked — "{topic}-prove-hypothesis-{date}.md written. Stage 2 ready."**

---

## STAGE 2 — WEB SEARCH

**STAGE 2 ENTRY CONDITIONS:**
- [ ] STAGE 1 EXIT received: hypothesis_locked

**STAGE 2 BODY:**

Gather minimum 3 external sources. Apply displacement template to each evidence row.

| # | Source (URL or citation) | Key Finding (1 sentence) | Strength | Displacement Check |
|---|--------------------------|--------------------------|----------|--------------------|
| 1 | | | Strong/Moderate/Weak | Does [item 1] support displacement of {status_quo_comparator} by {topic}? [Yes/No/Inconclusive] |
| 2 | | | Strong/Moderate/Weak | Does [item 2] support displacement of {status_quo_comparator} by {topic}? [Yes/No/Inconclusive] |
| 3 | | | Strong/Moderate/Weak | Does [item 3] support displacement of {status_quo_comparator} by {topic}? [Yes/No/Inconclusive] |
| + | add as needed | | | |

| Summary Field | Value |
|---------------|-------|
| s2_tally | [N Yes / M No / P Inconclusive] |
| s2_strength_tally | [Strong: N, Moderate: M, Weak: P] |
| s2_key_gap | [what external evidence does not address] |

**WRITE:** `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`
Confirm write.

**STAGE 2 EXIT: websearch_complete — "s2_tally = [value]. Stage 3 ready."**

---

## STAGE 3 — INTELLIGENCE

**STAGE 3 ENTRY CONDITIONS:**
- [ ] STAGE 2 EXIT received: websearch_complete
- [ ] s2_tally recorded (not blank)

**STAGE 3 BODY:**

Search internal sources: codebase, specs, docs, prior signal artifacts.
Apply displacement template to each internal finding.

| # | File Path | Section | Finding (1 sentence) | Strength | Displacement Check |
|---|-----------|---------|----------------------|----------|--------------------|
| 1 | | | | Strong/Moderate/Weak | Does [finding 1] support displacement of {status_quo_comparator} by {topic}? [Yes/No/Inconclusive] |
| 2 | | | | Strong/Moderate/Weak | Does [finding 2] support displacement of {status_quo_comparator} by {topic}? [Yes/No/Inconclusive] |
| 3 | | | | Strong/Moderate/Weak | Does [finding 3] support displacement of {status_quo_comparator} by {topic}? [Yes/No/Inconclusive] |
| + | add as needed | | | | |

| Summary Field | Value |
|---------------|-------|
| s3_tally | [N Yes / M No / P Inconclusive] |
| s3_alignment | [ALIGNED / CONTRADICTS / MIXED — vs Stage 2] |
| s3_key_gap | [what internal sources do not address] |

**WRITE:** `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`
Confirm write.

**STAGE 3 EXIT: intelligence_complete — "s3_tally = [value]. Stage 4 ready."**

---

## STAGE 4 — ANALYSIS

**STAGE 4 ENTRY CONDITIONS:**
- [ ] STAGE 3 EXIT received: intelligence_complete
- [ ] s3_tally recorded (not blank)

**STAGE 4 BODY:**

Analyze patterns across Stages 2 + 3. Distinguish causation from correlation.

| # | Pattern | Evidence Sources (S2-# / S3-filepath) | Causal? | Confidence |
|---|---------|---------------------------------------|---------|------------|
| 1 | | | Yes/No/Unknown | Low/Med/High |
| 2 | | | | |
| 3 | | | | |
| + | add as needed | | | |

Aggregate displacement verdict (apply displacement template to full evidence set):
  "Does the aggregate evidence pattern support the displacement of {status_quo_comparator}
   by {topic}? [Yes / No / Inconclusive]"
  s4_aggregate_displacement_verdict: [Yes / No / Inconclusive]

| Summary Field | Value |
|---------------|-------|
| s4_primary_finding | [dominant pattern across all evidence, 1-2 sentences] |
| s4_counter_evidence | [strongest evidence against hypothesis — cite artifact + section] |
| s4_aggregate_displacement_verdict | [Yes / No / Inconclusive] |

**WRITE:** `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`
Confirm write.

**STAGE 4 EXIT: analysis_complete — "s4_aggregate_displacement_verdict = [value]. Stage 5 ready."**

---

## STAGE 5 — SYNTHESIS

**STAGE 5 ENTRY CONDITIONS:**
- [ ] STAGE 4 EXIT received: analysis_complete
- [ ] counter_hypothesis from Stage 1 present for resolution
- [ ] s4_aggregate_displacement_verdict recorded

**STAGE 5 BODY:**

COUNTER-HYPOTHESIS RESOLUTION:

| Counter-Hypothesis | Verdict | Evidence Citation |
|--------------------|---------|-------------------|
| [from Stage 1] | REFUTED / PARTIALLY REFUTED / OPEN RISK | [cite stage artifact] |

SYNTHESIS:

| Field | Value |
|-------|-------|
| hypothesis_verdict | SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED |
| displacement_conclusion | Does the evidence support replacing {status_quo_comparator} with {topic}? [Yes / No / Conditional — one sentence] |
| confidence_final | Low / Medium / High |
| evidence_summary | [2-3 sentences integrating Stages 2, 3, 4] |
| key_risk | [primary risk remaining after evidence review] |

**WRITE:** `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`
Confirm write.

**STAGE 5 EXIT: synthesis_complete — "Evidence brief complete. Ready for /topic-story."**

CAMPAIGN COMPLETE.
```
