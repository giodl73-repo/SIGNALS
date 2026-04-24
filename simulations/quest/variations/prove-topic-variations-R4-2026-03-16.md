The file already has content from a prior Round 4 session (rubric v4). I'll output the new Round 4 variations for rubric v14 directly here, as this is a different quest session.

The rubric v14 canonical sequence (C-01: hypothesis → web-search → intelligence → analysis → synthesize) differs from the T3's evolved stages (interview + prototype in stages 3-4). All five variations below restore alignment to the rubric's expected sequence.

---

## V-01 — Phrasing Register: Conversational + Imperative

**Axis**: phrasing_register (single)
**Hypothesis**: The T3 uses formal structured tables and invariant-table syntax. Plain imperative prose produces more complete stage execution because instructions read as direct commands, not spec entries that can be treated as optional.

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

You are running the full prove evidence campaign for {topic}.
Five evidence stages in sequence: hypothesis -> web-search -> intelligence ->
analysis -> synthesize. One artifact per stage. Scout artifact loaded before
Stage 1. Final output: evidence brief ready for /topic-story.

---

## Setup

Before running any stage, do three things:

1. Name the incumbent. {status_quo_comparator} is what {topic} must displace.
   Write one sentence on why it is currently winning.
   Write one sentence on where it is most exposed.

2. Load the scout artifact. Find {topic}-scout-record-{date}.md or nearest match.
   If not found: stop. CAMPAIGN BLOCKED — no scout artifact.
   Record: scout_artifact = [path]

3. Register the campaign question: "Can {topic} build a stronger case than
   {status_quo_comparator}?" This question travels through all five stages.

---

## Stage 1 — Hypothesis

Entry: scout artifact loaded and path recorded.

Load the scout artifact. Read its signals.

Frame a falsifiable claim about {topic}: what do you believe is true, and what
would change your mind?

Frame the counter-hypothesis: what is {status_quo_comparator}'s best argument
against this claim? Ground it in the incumbent's known strengths.

  source_scout_artifact: [path from Setup — copy, do not infer]
  hypothesis: [falsifiable claim about {topic}]
  counter_hypothesis: [{status_quo_comparator}'s strongest defense]
  confidence_prior: [1-10 — your confidence before external evidence]

Write: {topic}-hypothesis-{date}.md
Announce: "Stage 1 done — hypothesis locked. Confidence prior: [N]. Stage 2 ready."

---

## Stage 2 — Web Search

Entry: Stage 1 complete, hypothesis written.

Search for at least 3 external sources. For each, record:
  - Source (URL or citation)
  - One-sentence summary of the key finding
  - Does this support or challenge the hypothesis?
  - Displacement check: "Does [source] support displacing {status_quo_comparator}
    with {topic}? [Yes / No / Inconclusive]"

Tally: [N support] / [M challenge] / [P inconclusive]
Counter-evidence? ce_s2 = [citation or null].
Confidence delta: confidence_delta_s2 = [+1 / -1 / 0]

Write: {topic}-websearch-{date}.md
Announce: "Stage 2 done — web search complete. ce_s2 = [value]. Delta: [N].
Stage 3 ready."

---

## Stage 3 — Intelligence (internal sources)

Entry: Stage 2 complete, websearch artifact written.

Search internal sources: codebase files, specs, prior research, design docs,
prior signals. Find at least 3 relevant internal references. For each, record:
  - File path or document name
  - One-sentence relevance summary
  - Does this support or challenge the hypothesis?
  - Does this reveal how {status_quo_comparator} is currently implemented
    or relied upon internally? (transition friction note — or N/A)

Tally: [N support] / [M challenge] / [P inconclusive]
Counter-evidence? ce_s3 = [file path/section or null].
Confidence delta: confidence_delta_s3 = [+1 / -1 / 0]

If no internal sources exist: note explicitly. ce_s3 = null. confidence_delta_s3 = -1.

Write: {topic}-intelligence-{date}.md
Announce: "Stage 3 done — intelligence complete. ce_s3 = [value]. Delta: [N].
Stage 4 ready."

---

## Stage 4 — Analysis

Entry: Stage 3 complete, intelligence artifact written.

Analyze patterns across Stages 2 and 3. Distinguish correlation from causation.
Address the displacement question: does the combined evidence make a credible case
for displacing {status_quo_comparator} with {topic}?

Cover:
  - What pattern appears consistently across both web and internal evidence?
  - What is the strongest single piece of evidence for the hypothesis?
  - What is the strongest single piece of evidence against it?
  - Transition friction: how entrenched is {status_quo_comparator}? [Low / Medium / High]
  - Aggregate displacement verdict: [Supported / Partial / Insufficient]

ce_s4 = [new counter-evidence found here, or null]
confidence_delta_s4 = [+1 / -1 / 0]

Write: {topic}-analysis-{date}.md
Announce: "Stage 4 done — analysis complete. Displacement: [verdict]. Delta: [N].
Stage 5 ready."

---

## Stage 5 — Synthesis

Entry: Stage 4 complete, analysis artifact written.

Open with the answer: is the hypothesis supported?

### Counter-hypothesis resolution
Take the counter-hypothesis from Stage 1. Rule on it using evidence from Stages 2-4.
  verdict: REFUTED / PARTIALLY REFUTED / OPEN RISK
  evidence: [cite stage artifact]
  If OPEN RISK: note in key_risk and subtract 1 from confidence.

### Confidence chain
Show the derivation:
  confidence_final = confidence_prior + delta_s2 + delta_s3 + delta_s4 [+/- risk_adj]
  [prior=N] + [s2=N] + [s3=N] + [s4=N] [risk=N] = [final=N]

### Synthesis fields
  hypothesis_verdict: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED
  evidence_summary: [2-3 sentences integrating Stages 2, 3, and 4 — include
    the displacement verdict from Stage 4]
  confidence_final: [value from chain, show derivation]
  key_risk: [primary adoption risk framed as residual incumbent strength —
    what {status_quo_comparator} still does better]

Write: {topic}-synthesis-{date}.md
Announce: "Stage 5 done — synthesis complete. Evidence brief ready for /topic-story.
Campaign complete."
```

---

## V-02 — Lifecycle Emphasis: Stage-Body-First

**Axis**: lifecycle_emphasis (single)
**Hypothesis**: The T3 expends ~40 lines on pre-stage apparatus before Stage 0. If that overhead is compressed to a single SETUP block and each stage body is expanded with required sub-questions and minimum counts, the model allocates effort to evidence work rather than meta-structure.

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Full prove evidence campaign for {topic}.
Displacing: {status_quo_comparator}
Date: {date}

Sequence: Gate -> Hypothesis -> WebSearch -> Intelligence -> Analysis -> Synthesize.
One artifact per evidence stage. Final output: evidence brief for /topic-story.

---

## SETUP (complete before Gate)

  incumbent:             {status_quo_comparator}
  incumbent_strength:    [one sentence — why they are currently winning]
  incumbent_vulnerability: [one sentence — where they are most exposed]
  scout_artifact:        [{topic}-scout-record-{date}.md or nearest glob — path]
  campaign_question:     "Can {topic} displace {status_quo_comparator}?"

If scout_artifact not found: BLOCKED. Record missing path.
Announce: "Setup complete. Scout: [path]. Advancing to Gate."

---

## GATE

Check: incumbent filled? scout_artifact loaded? campaign_question registered?
If all: "Gate cleared. Stage 1 ready."
If any fail: BLOCKED — record which.

---

## STAGE 1 — HYPOTHESIS

Load the scout artifact (path from Setup — copy, do not re-derive).
Read signals. The hypothesis must emerge from those signals, not general knowledge.

Required output:

**Hypothesis** (falsifiable displacement claim):
  "We believe {topic} displaces {status_quo_comparator} on [dimension] because
   [scout signal]. We would revise this if [falsification condition]."

**Counter-hypothesis** (incumbent's best defense, grounded in incumbent_strength):
  "{status_quo_comparator} retains its position because [strongest argument
   based on known incumbent strengths]."

**Confidence prior**: [1-10 — your confidence in the displacement claim before
any external evidence]

**Scout anchor**: [key signal from scout artifact that grounds the hypothesis —
cite the specific section or finding]

Artifact fields: source_scout_artifact, hypothesis, counter_hypothesis,
confidence_prior, scout_anchor.

Write: {topic}-hypothesis-{date}.md
Exit: "STAGE 1 COMPLETE — hypothesis locked (confidence_prior = [N])."

---

## STAGE 2 — WEB SEARCH

Required: minimum 4 sources (direct quotes or specific data points, not paraphrases).

For each source — all five fields required:
  a) Full citation or URL
  b) One direct quote or specific data point
  c) Strength of evidence: Strong / Moderate / Weak
  d) Direction: Supports hypothesis / Challenges hypothesis / Neutral
  e) Displacement check: "Does [source] support displacing {status_quo_comparator}
     with {topic}? [Yes / No / Inconclusive]"

After all sources:
  web_support_count:   [N sources supporting]
  web_challenge_count: [M sources challenging]
  strongest_source:    [citation — highest strength-of-evidence]
  ce_s2:               [null OR strongest counter-evidence citation]
  confidence_delta_s2: [+1 if 3+ strong-support / -1 if ce found / 0 otherwise]

Write: {topic}-websearch-{date}.md
Exit: "STAGE 2 COMPLETE — websearch done (ce_s2 = [value], delta = [N])."

---

## STAGE 3 — INTELLIGENCE (internal sources)

Required: minimum 3 internal sources (file paths, spec sections, prior signals,
design docs).

For each — all five fields required:
  a) Full file path or document reference (not approximate)
  b) Relevant excerpt or 2-sentence summary
  c) Relevance to hypothesis: Direct / Indirect / Tangential
  d) Transition friction note: does this source show how {status_quo_comparator}
     is currently implemented or relied upon internally? [note or N/A]
  e) Direction: Supports / Challenges / Neutral

After all sources:
  internal_support_count:   [N]
  internal_challenge_count: [M]
  strongest_internal:       [file path — most directly relevant]
  ce_s3:                    [null OR strongest internal counter-evidence citation]
  confidence_delta_s3:      [+1 if 2+ direct-support / -1 if ce found / 0 otherwise]

If no internal sources exist: note explicitly. ce_s3 = null. confidence_delta_s3 = -1.

Write: {topic}-intelligence-{date}.md
Exit: "STAGE 3 COMPLETE — intelligence done (ce_s3 = [value], delta = [N])."

---

## STAGE 4 — ANALYSIS

Cross-stage analysis of Stages 2 and 3.

Required sections — no skipping:

**Cross-stage pattern**
What pattern holds across BOTH web and internal evidence? One sentence.
Is this correlational or structural? Explain briefly.

**Strongest evidence**
Best evidence FOR displacement (cite S2 or S3): [citation + one sentence]
Best evidence AGAINST displacement (cite S2 or S3, or name gap): [citation + one sentence]

**Displacement assessment**
Direct comparison: on the hypothesis dimension, how does {topic} perform relative
to {status_quo_comparator}? [cite evidence]

Transition friction: [Low / Medium / High + one sentence rationale]

Aggregate displacement verdict: [Supported / Partial / Insufficient]
Rationale (one sentence, cite S2 and S3): [...]

ce_s4:                [null OR new counter-evidence from this analysis step]
confidence_delta_s4:  [+1 Supported / 0 Partial / -1 Insufficient]

Write: {topic}-analysis-{date}.md
Exit: "STAGE 4 COMPLETE — analysis done (displacement = [verdict], delta = [N])."

---

## STAGE 5 — SYNTHESIS

Required sections in order:

**Counter-hypothesis resolution**
Quote the counter-hypothesis from Stage 1 exactly.
Cite evidence from Stages 2-4 that bears on it.
Verdict: REFUTED / PARTIALLY REFUTED / OPEN RISK
If OPEN RISK: add to key_risk. Reduce confidence by 1 before chain calculation.

**Confidence chain**
Show the equation:
  confidence_final = confidence_prior + delta_s2 + delta_s3 + delta_s4 [+ risk_adj]
  [prior=N] + [s2=N] + [s3=N] + [s4=N] [risk=N] = [final=N]

**Synthesis statement**
  hypothesis_verdict:  SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED
  evidence_summary:    [2-3 sentences integrating all stages — explicitly state
    displacement verdict from Stage 4 and whether counter-hypothesis holds]
  confidence_final:    [value from chain, full derivation shown]
  key_risk:            [framed as residual incumbent strength: what
    {status_quo_comparator} still does better, and why that is the primary
    adoption risk]

story_ready: "Evidence brief ready for /topic-story."

Write: {topic}-synthesis-{date}.md
Exit: "STAGE 5 COMPLETE — synthesis done. Evidence brief ready for /topic-story.
Campaign complete."
```

---

## V-03 — Inertia Framing: Displacement-First

**Axis**: inertia_framing (single)
**Hypothesis**: The T3 treats the status-quo comparator as secondary. If the incumbent is foregrounded — every stage opens with the displacement question as its organizing principle and synthesis closes with an explicit displacement verdict — the skill produces stronger signals for recommended criteria around competitive positioning.

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic — Displacement Campaign

You are building the case for displacing {status_quo_comparator} with {topic}.
Every stage asks: does this evidence support the displacement?
The campaign ends with a displacement verdict the /topic-story author can act on.

Topic: {topic}
Date: {date}
Must displace: {status_quo_comparator}

---

## DISPLACEMENT BASELINE

Before any evidence stage, establish the incumbent frame.

  incumbent:               {status_quo_comparator}
  incumbent_strength:      [one sentence — why {status_quo_comparator} currently wins]
  incumbent_vulnerability: [one sentence — where {status_quo_comparator} is most exposed]

Load the scout artifact: {topic}-scout-record-{date}.md or nearest glob match.
  scout_artifact: [path]
  If not found: CAMPAIGN BLOCKED. No scout, no campaign.

This baseline travels unchanged through all five stages.

---

## Stage 1 — Hypothesis: the displacement claim

vs {status_quo_comparator}: what specifically does {topic} do better?

Read the scout artifact. Identify the dimension on which {topic} plausibly
outperforms {status_quo_comparator}.

Frame the hypothesis as a displacement claim:
  "We believe {topic} displaces {status_quo_comparator} on [dimension] because
   [reason from scout signals]. Falsification: if [condition], the displacement
   case fails."

Frame the counter-hypothesis as the incumbent's best defense (grounded in
incumbent_strength):
  "{status_quo_comparator} retains its position because [strongest argument]."

  source_scout_artifact: [path — copied, not inferred]
  hypothesis: [the displacement claim]
  counter_hypothesis: [the incumbent defense]
  confidence_prior: [1-10 — confidence in displacement before external evidence]

Write: {topic}-hypothesis-{date}.md
Announce: "Stage 1 CLOSED: displacement claim locked (confidence_prior = [N]).
Stage 2 ready."

---

## Stage 2 — Web Search: external displacement evidence

vs {status_quo_comparator}: does the web confirm this is a real displacement story?

Gather minimum 3 external sources. For each:
  - Source (URL or citation)
  - Key finding (one sentence)
  - Displacement check (applied verbatim): "Does [source] support the displacement
    of {status_quo_comparator} by {topic} on [dimension]? [Yes / No / Inconclusive]"

Summary after all sources:
  s2_displacement_support:   [N sources Yes]
  s2_displacement_challenge: [M sources No or Inconclusive]
  ce_s2:                     [null or citation]
  confidence_delta_s2:       [+1 / -1 / 0]

Write: {topic}-websearch-{date}.md
Announce: "Stage 2 CLOSED: web search done. Displacement signal: [N support /
M challenge]. ce_s2 = [value]. Stage 3 ready."

---

## Stage 3 — Intelligence: internal displacement evidence

vs {status_quo_comparator}: does our codebase or research support this displacement?

Search internal sources: files, specs, prior signals, design docs.
Minimum 3 references. For each:
  - File path or document
  - Key finding (one sentence)
  - Displacement check (applied verbatim): "Does [source] reveal internal evidence
    of {topic} outperforming {status_quo_comparator} on [dimension]?
    [Yes / No / Inconclusive]"
  - Incumbent embedding: does this source show how {status_quo_comparator} is
    currently used internally? [note transition friction, or N/A]

Summary:
  s3_displacement_support:   [N]
  s3_displacement_challenge: [M]
  ce_s3:                     [null or citation]
  confidence_delta_s3:       [+1 / -1 / 0]

Write: {topic}-intelligence-{date}.md
Announce: "Stage 3 CLOSED: intelligence done. Internal signal: [N support /
M challenge]. ce_s3 = [value]. Stage 4 ready."

---

## Stage 4 — Analysis: displacement verdict

vs {status_quo_comparator}: synthesize the evidence into a displacement judgment.

**Cross-stage pattern**
What consistent pattern emerges across Stages 2 and 3 regarding {status_quo_comparator}
and {topic}? One sentence. Distinguish correlation from causation.

**Transition friction**
How entrenched is {status_quo_comparator}? [Low / Medium / High]
Rationale (one sentence): [what makes switching easy or hard]

**Aggregate displacement verdict**
Direct statement: "The evidence [supports / partially supports / does not support]
the displacement of {status_quo_comparator} by {topic} on [dimension]."
Verdict: [Supported / Partial / Insufficient]

  ce_s4:                [null or new counter-evidence identified in analysis]
  confidence_delta_s4:  [+1 Supported / 0 Partial / -1 Insufficient]

Write: {topic}-analysis-{date}.md
Announce: "Stage 4 CLOSED: displacement verdict = [value]. Stage 5 ready."

---

## Stage 5 — Synthesis: the displacement brief

Open with the verdict: is the displacement case made?

### Counter-hypothesis resolution
[Quote counter-hypothesis from Stage 1 exactly]
Evidence response (cite Stages 2-4): [what was found]
Verdict: REFUTED / PARTIALLY REFUTED / OPEN RISK
If OPEN RISK: reduce confidence by 1. Document in key_risk.

### Displacement conclusion
  displacement_verdict:  [Supported / Partial / Insufficient — from Stage 4,
    confirmed or revised after counter-hypothesis resolution]
  hypothesis_verdict:    SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED
  evidence_summary:      [2-3 sentences: what the evidence shows about the
    displacement case — explicitly state whether {topic} can displace
    {status_quo_comparator} and on what terms]
  confidence_final:      [1-10; derivation: prior + delta_s2 + delta_s3 +
    delta_s4 +/- risk_adj = final]
  key_risk:              [what {status_quo_comparator} still does better —
    the residual retention argument — framed as an adoption risk for {topic}]

Write: {topic}-synthesis-{date}.md
Announce: "Stage 5 CLOSED: displacement brief complete. Evidence brief ready
for /topic-story. Campaign complete."
```

---

## V-04 — Combined: Lifecycle Emphasis + Output Format (Table)

**Axes**: lifecycle_emphasis + output_format (combined)
**Hypothesis**: V-02 compresses setup and expands stage bodies. If stage structure is additionally expressed as a table (ENTRY | BODY | EXIT), each cell functions as a mandatory completion checkpoint — harder to leave blank than prose paragraphs — producing more consistent field coverage.

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Five-stage prove campaign for {topic} vs {status_quo_comparator}.
Date: {date}

Each stage: ENTRY CONDITIONS | BODY | EXIT SIGNAL.
Sequence: Setup -> Gate -> Stage 1 (Hypothesis) -> Stage 2 (WebSearch) ->
Stage 3 (Intelligence) -> Stage 4 (Analysis) -> Stage 5 (Synthesis).
One artifact per evidence stage. No stage begins until ENTRY CONDITIONS met.

---

## PRE-STAGE SETUP

| ITEM | ACTION | REQUIRED |
|------|--------|----------|
| Incumbent | Name {status_quo_comparator}. Record: strength (one sentence), vulnerability (one sentence). | true |
| Scout artifact | Glob for {topic}-scout-record-{date}.md or nearest match. Record exact path. | true — BLOCKED if missing |
| Campaign question | Register: "Can {topic} displace {status_quo_comparator}?" | registered |

Announce: "Setup complete. Scout: [path]. Advancing to Gate."

---

## GATE

| ENTRY | BODY | EXIT |
|-------|------|------|
| Setup fields filled | Check: incumbent named and framed? scout_artifact path recorded? campaign_question registered? | All confirmed: "Gate CLEARED. Stage 1 ready." Any fail: "BLOCKED — [item] missing." |

---

## STAGE 1 — HYPOTHESIS

| ENTRY | BODY | EXIT |
|-------|------|------|
| Gate CLEARED. Scout artifact path available. | Load scout artifact (path from Setup — copy, do not re-derive). Read signals. Frame hypothesis: falsifiable displacement claim about {topic}. Frame counter_hypothesis: incumbent's best defense grounded in incumbent_strength. Rate confidence_prior (1-10). Record scout_anchor (key signal cited). Artifact fields: source_scout_artifact, hypothesis, counter_hypothesis, confidence_prior, scout_anchor. Write: {topic}-hypothesis-{date}.md. Confirm write. | "STAGE 1 EXIT: hypothesis_locked (confidence_prior = [N]). Stage 2 ready." |

---

## STAGE 2 — WEB SEARCH

| ENTRY | BODY | EXIT |
|-------|------|------|
| STAGE 1 EXIT received: hypothesis_locked. | Gather min 3 external sources. For each row: source URL/citation / 1-sentence finding / displacement check verbatim: "Does [source] support displacing {status_quo_comparator} with {topic}? [Yes/No/Inconclusive]". Fill after table: s2_support_count, s2_challenge_count, ce_s2 (null or citation), confidence_delta_s2 (+1/-1/0). Write: {topic}-websearch-{date}.md. Confirm write. | "STAGE 2 EXIT: websearch_complete (ce_s2=[value], delta=[N]). Stage 3 ready." |

---

## STAGE 3 — INTELLIGENCE

| ENTRY | BODY | EXIT |
|-------|------|------|
| STAGE 2 EXIT received: websearch_complete. | Search internal sources (files, specs, prior signals). Min 3. For each row: file path / 1-sentence relevance / displacement check verbatim: "Does [source] support displacing {status_quo_comparator} with {topic}? [Yes/No/Inconclusive]" / transition friction note (how {status_quo_comparator} is embedded internally, or N/A). Fill: s3_support_count, s3_challenge_count, ce_s3 (null or citation), confidence_delta_s3. Write: {topic}-intelligence-{date}.md. Confirm write. | "STAGE 3 EXIT: intelligence_complete (ce_s3=[value], delta=[N]). Stage 4 ready." |

---

## STAGE 4 — ANALYSIS

| ENTRY | BODY | EXIT |
|-------|------|------|
| STAGE 3 EXIT received: intelligence_complete. | Required sections: (1) Cross-stage pattern: one sentence holding across S2+S3; correlation vs causation call. (2) Strongest FOR evidence: cite S2 or S3. (3) Strongest AGAINST evidence: cite S2 or S3 or name gap. (4) Transition friction: Low/Medium/High + one-sentence rationale. (5) Aggregate displacement verdict: Supported/Partial/Insufficient, one-sentence rationale citing S2+S3. Fill: ce_s4 (null or description), confidence_delta_s4 (+1/-1/0). Write: {topic}-analysis-{date}.md. Confirm write. | "STAGE 4 EXIT: analysis_complete (displacement=[verdict], ce_s4=[value], delta=[N]). Stage 5 ready." |

---

## STAGE 5 — SYNTHESIS

| ENTRY | BODY | EXIT |
|-------|------|------|
| STAGE 4 EXIT received: analysis_complete. Counter-hypothesis from Stage 1 present. | COUNTER-HYPOTHESIS RESOLUTION: quote counter_hypothesis from S1; cite S2-S4 evidence; verdict REFUTED/PARTIALLY REFUTED/OPEN RISK; if OPEN RISK: key_risk note + risk_adj = -1; else risk_adj = 0. CONFIDENCE CHAIN: show equation — confidence_prior + delta_s2 + delta_s3 + delta_s4 + risk_adj = confidence_final. SYNTHESIS FIELDS: hypothesis_verdict (SUPPORTED/PARTIALLY SUPPORTED/UNSUPPORTED), evidence_summary (2-3 sentences integrating S2+S3+S4 with explicit displacement verdict), confidence_final (show derivation), key_risk (residual incumbent strength as adoption risk). Write: {topic}-synthesis-{date}.md. Confirm write. | "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for /topic-story. Campaign complete." |
```

---

## V-05 — Combined: Role Sequence + Inertia Framing + Lifecycle Emphasis

**Axes**: role_sequence + inertia_framing + lifecycle_emphasis (full integration)
**Hypothesis**: Three-role pre-stage (DISPLACEMENT ANALYST first, SCOUT LOADER second, CAMPAIGN DIRECTOR third) + displacement question anchoring every evidence stage + compact lifecycle markers produces the strongest aspirational performance. The displacement template is registered pre-stage and applied verbatim at Stages 2, 3, and 4 — making it a structural invariant rather than a free-text suggestion.

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Topic: {topic}
Date: {date}
Must displace: {status_quo_comparator}

Full prove campaign. Three named roles execute pre-stage in sequence.
Five evidence stages: hypothesis -> web-search -> intelligence -> analysis -> synthesize.
The displacement question anchors every evidence stage. One artifact per stage.
Final output: evidence brief ready for /topic-story.

---

## PRE-STAGE ROLES

Three roles execute in order. Each owns specific fields. No stage begins until
all three complete and campaign_open = true.

---

### ROLE 1 — DISPLACEMENT ANALYST (executes first)

You establish the competitive frame and register the displacement check template.

Fill now:
  incumbent:               {status_quo_comparator}
  incumbent_strength:      [one sentence — why {status_quo_comparator} currently wins]
  incumbent_vulnerability: [one sentence — where {status_quo_comparator} is most exposed]
  displacement_template:   "Does [evidence item] support the displacement of
    {status_quo_comparator} by {topic} on [dimension]? [Yes / No / Inconclusive]"

The displacement_template applies VERBATIM at Stages 2, 3, and 4.
Any deviation from the template is a format error.

displacement_baseline_locked: [true when all fields above filled]

---

### ROLE 2 — SCOUT LOADER (executes second)

You load the prior scout research.

  scout_artifact: [{topic}-scout-record-{date}.md or nearest glob match — exact path]
  scout_loaded:   [true / false]

If scout_loaded = false: CAMPAIGN BLOCKED. Record missing path.
If scout_loaded = true: announce "Scout loaded: [path]."

gate_cleared: [= scout_loaded]

---

### ROLE 3 — CAMPAIGN DIRECTOR (executes third)

You confirm both roles completed and open the campaign.

Confirm:
  displacement_baseline_locked: [value from ROLE 1]
  gate_cleared:                 [value from ROLE 2]

If either not true: BLOCKED — record which role failed.
If both confirmed:
  campaign_question: "Can {topic} displace {status_quo_comparator}?"
  campaign_open: true

Announce: "Campaign open. All pre-stage roles complete. Stage 1 ready."

---

## STAGE 1 — HYPOTHESIS

Entry: campaign_open = true. Scout path available from ROLE 2.

Load scout artifact (ROLE 2 path — copy, do not re-derive).
Read signals. Frame the displacement hypothesis grounded in those signals:
  "We believe {topic} displaces {status_quo_comparator} on [dimension] because
   [scout signal]. We would revise this if [falsification condition]."

Frame counter-hypothesis as the incumbent defense (grounded in ROLE 1 incumbent_strength):
  "{status_quo_comparator} retains its position because [strongest defense]."

  source_scout_artifact: [ROLE 2 path]
  hypothesis:            [displacement claim]
  counter_hypothesis:    [incumbent defense]
  confidence_prior:      [1-10]

Write: {topic}-hypothesis-{date}.md
Exit: "STAGE 1 EXIT: hypothesis_locked (confidence_prior=[N]). Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

Entry: Stage 1 EXIT received. ROLE 1 displacement_template active.

Gather minimum 3 external sources. For each, fill all three columns:

  | SOURCE | FINDING | DISPLACEMENT CHECK |
  |--------|---------|-------------------|
  | [URL or citation] | [1 sentence] | [ROLE 1 template verbatim + verdict] |
  | [add rows] | | |

Summary:
  s2_yes:              [N sources Yes]
  s2_no_inconclusive:  [M sources No or Inconclusive]
  ce_s2:               [null or citation]
  confidence_delta_s2: [+1 majority Yes / -1 ce found / 0 mixed]
  running_confidence:  [confidence_prior + delta_s2]

Write: {topic}-websearch-{date}.md
Exit: "STAGE 2 EXIT: websearch_complete (ce_s2=[value], running_confidence=[N]).
Stage 3 ready."

---

## STAGE 3 — INTELLIGENCE

Entry: Stage 2 EXIT received. ROLE 1 displacement_template active.

Search internal sources: codebase files, specs, prior signals, design docs.
Minimum 3 references. For each, fill all four columns:

  | SOURCE | FINDING | DISPLACEMENT CHECK | INCUMBENT EMBEDDING |
  |--------|---------|-------------------|--------------------|
  | [file path] | [1 sentence] | [ROLE 1 template verbatim + verdict] | [how {status_quo_comparator} is used here, or N/A] |
  | [add rows] | | | |

Summary:
  s3_yes:              [N]
  s3_no_inconclusive:  [M]
  ce_s3:               [null or file path/section]
  confidence_delta_s3: [+1/-1/0]
  running_confidence:  [prior_running + delta_s3]

Write: {topic}-intelligence-{date}.md
Exit: "STAGE 3 EXIT: intelligence_complete (ce_s3=[value], running_confidence=[N]).
Stage 4 ready."

---

## STAGE 4 — ANALYSIS

Entry: Stage 3 EXIT received. ROLE 1 displacement_template active.

**Cross-stage pattern**
Pattern holding across S2 and S3 (one sentence): [...]
Correlation or structural? [assess]

**Displacement verdict table**

  | DIMENSION | S2 SIGNAL | S3 SIGNAL | VERDICT |
  |-----------|-----------|-----------|---------|
  | [dimension from hypothesis] | [Yes/No/Inc] | [Yes/No/Inc] | Supported/Partial/Insufficient |

Aggregate template application (ROLE 1 template verbatim):
  "Does [aggregate evidence from S2 and S3] support the displacement of
   {status_quo_comparator} by {topic} on [dimension]? [verdict]"

**Transition friction**: [Low / Medium / High + one-sentence rationale]

  ce_s4:                [null or new counter-evidence]
  confidence_delta_s4:  [+1 Supported / 0 Partial / -1 Insufficient]
  running_confidence:   [prior_running + delta_s4]

Write: {topic}-analysis-{date}.md
Exit: "STAGE 4 EXIT: analysis_complete (displacement_verdict=[value],
running_confidence=[N]). Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

Entry: Stage 4 EXIT received. Counter-hypothesis from Stage 1 present.
running_confidence available.

### COUNTER-HYPOTHESIS RESOLUTION

  | COUNTER-HYPOTHESIS | EVIDENCE RESPONSE | VERDICT |
  |--------------------|-------------------|---------|
  | [quote from Stage 1 verbatim] | [cite S2-S4 artifacts] | REFUTED / PARTIALLY REFUTED / OPEN RISK |

If OPEN RISK: risk_adj = -1. Add to key_risk.
Else: risk_adj = 0.

### CONFIDENCE CHAIN RESOLUTION

Show full derivation:
  confidence_prior + delta_s2 + delta_s3 + delta_s4 + risk_adj = confidence_final
  [N]             + [N]       + [N]       + [N]       + [N]      = [N]

### DISPLACEMENT CONCLUSION

  displacement_conclusion: [Supported / Partial / Insufficient — Stage 4 verdict
    confirmed or revised after counter-hypothesis resolution]
  hypothesis_verdict:      SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED
  evidence_summary:        [2-3 sentences integrating S2+S3+S4 — explicitly state
    whether the evidence supports displacing {status_quo_comparator} and on what terms]
  confidence_final:        [value from chain]
  key_risk:                [what {status_quo_comparator} still does better — residual
    retention argument framed as the primary adoption risk for {topic}]

Write: {topic}-synthesis-{date}.md
Exit: "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for /topic-story.
Campaign complete."
```

---

## Variation Summary

| Var | Axis | Key structural difference | C-01 risk | Aspirational potential |
|-----|------|--------------------------|-----------|----------------------|
| V-01 | phrasing_register | All tables/invariants as imperative prose; same logic | Low | Low — no explicit chain |
| V-02 | lifecycle_emphasis | Compressed pre-stage; expanded stage bodies with required sub-questions + min counts | Low | Medium — confidence chain at S5 |
| V-03 | inertia_framing | Incumbent-first at every stage header; displacement check verbatim S2-S4; explicit displacement_verdict in synthesis | Low | Medium — displacement loop present |
| V-04 | lifecycle_emphasis + output_format | Table format per stage; ENTRY\|BODY\|EXIT enforces field completion | Low | Medium — compact chain at S5 |
| V-05 | role_sequence + inertia_framing + lifecycle_emphasis | DISPLACEMENT ANALYST registers template pre-stage; verbatim at S2/S3/S4; running_confidence chain; S5 dual-block COUNTER-HYPOTHESIS RESOLUTION + CONFIDENCE CHAIN RESOLUTION | Low | High — displacement loop + chain + dual-block |

**Design note**: All five variations align to rubric v14's canonical sequence (intelligence + analysis in Stages 3-4), replacing the T3's evolved interview + prototype. The scoring round should reveal whether the displacement-anchoring axis (V-03/V-05) or the stage-body depth axis (V-02) drives recommended/aspirational coverage.
