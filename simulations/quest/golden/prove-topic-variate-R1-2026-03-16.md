---
skill: quest-variate
skill_target: prove-topic
round: R1
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [lifecycle_emphasis, output_format, inertia_framing]
  combined: [V-04 (phrasing_register + output_format), V-05 (all_four)]
rubric_anchor: >
  v14 is a fresh 10-criterion stack: 5 essential (sequence, scout-named-before-hyp,
  one-write-per-stage, synthesis-names-topic-story, full-paths-per-write), 3 recommended
  (gate before S1, scout anchor in hyp artifact, evidence-gaps-at-stage), 2 aspirational
  (thin-evidence traces to claim, structural block before hyp). Round 1 starts clean —
  no v12/v13 role/invariant machinery is assumed. Each variation is designed to satisfy
  all 5 essential criteria and push toward recommended/aspirational through its axis.
round_targets: >
  The v14 rubric opens three opportunities that prior rounds did not target:
  (1) C-06 gate before Stage 1 is recommended but has a low structural bar — a single
  explicit gate line clears it. V-01 and V-05 use lifecycle phases to make the gate
  a labeled section rather than an inline note.
  (2) C-07 scout anchor in hypothesis artifact frontmatter is new — all variations
  must include a `scout_source:` field in the write instruction for Stage 1.
  (3) C-08 per-stage evidence-gap flagging is a recommended criterion that prior
  simple prompts ignored. V-03, V-04, V-05 thread a gap-flag prompt at each
  evidence stage to satisfy C-08 and push toward C-09.
---

## V-01 — Axis: Lifecycle Emphasis

**Variation axis**: Each stage is divided into three explicit sub-sections — ENTER,
WORK, and CLOSE — with labeled headers. The GATE before Stage 1 is a named section
(`## GATE — Scout Confirmation Required`) with a required check. The CLOSE sub-section
at each stage issues the write instruction, making the artifact-per-stage rhythm visible
as a structural rhythm rather than an instruction embedded in prose.

**Hypothesis**: C-03 (one write per stage, not batched) and C-06 (forward-only gate)
are easier to satisfy when stage lifecycle is explicit in the prompt structure. A prompt
that names ENTER/WORK/CLOSE makes it hard to defer the write: CLOSE is defined as
the write step. The gate becomes a stage rather than a sentence, making it a structural
block rather than a named anchor — addressing C-10 directly.

---

```
Topic: {topic}
Date:  {date}
Scout artifact: {topic}-scout-record-{date}.md

You are running the full prove evidence campaign for {topic}.
Five stages. One artifact write per stage. Forward order only.

---

## GATE — Scout Confirmation Required

Before Stage 1 begins, confirm:

  scout_record_path: simulations/scout/record/{topic}-scout-record-{date}.md
  scout_record_present: [ ] YES   (if NO — stop here, run prove-topic only after scouting)

Do not proceed to Stage 1 until this box is checked YES.

---

## STAGE 1 — Hypothesis

### ENTER
Load {topic}-scout-record-{date}.md. Identify the core claim the scout evidence supports.
Name the status-quo comparator the topic must displace.

### WORK
Frame the hypothesis: one sentence stating what {topic} enables that {status_quo_comparator}
cannot. State the counter-hypothesis in one sentence.

### CLOSE
Write artifact:

  path: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  frontmatter:
    topic: {topic}
    date: {date}
    scout_source: simulations/scout/record/{topic}-scout-record-{date}.md
    hypothesis: [your one-sentence claim]
    counter_hypothesis: [strongest opposing claim]

---

## STAGE 2 — Web Search

### ENTER
Load the hypothesis from simulations/prove/hypothesis/{topic}-hypothesis-{date}.md.
Identify 3–5 search queries that test the hypothesis against external evidence.

### WORK
Run searches. For each result: does it support or challenge the hypothesis? If evidence
is thin or absent, flag it now: "THIN EVIDENCE: [what is missing]."

### CLOSE
Write artifact:

  path: simulations/prove/websearch/{topic}-websearch-{date}.md
  frontmatter:
    topic: {topic}
    date: {date}
    hypothesis_source: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  body: sources found, support/challenge verdict per source, thin-evidence flags

---

## STAGE 3 — Intelligence (Internal Sources)

### ENTER
Identify internal source types relevant to {topic}: specs, transcripts, prior research,
patterns, metrics. Name which sources you will scan.

### WORK
Scan each source. For each: relevant finding or "no signal." If a source type is absent
or yields no signal, flag it now: "THIN EVIDENCE: [what is missing]."

### CLOSE
Write artifact:

  path: simulations/prove/intelligence/{topic}-intelligence-{date}.md
  frontmatter:
    topic: {topic}
    date: {date}
    hypothesis_source: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  body: findings per source type, thin-evidence flags

---

## STAGE 4 — Analysis

### ENTER
Load websearch and intelligence artifacts. Review findings across both external and
internal evidence.

### WORK
Assess: does the combined evidence support the hypothesis? Where are gaps? Where is
evidence strong? If any prior thin-evidence flag now looks definitive, escalate it:
"WEAK CLAIM: [the hypothesis element this undermines]."

### CLOSE
Write artifact:

  path: simulations/prove/analysis/{topic}-analysis-{date}.md
  frontmatter:
    topic: {topic}
    date: {date}
    websearch_source: simulations/prove/websearch/{topic}-websearch-{date}.md
    intelligence_source: simulations/prove/intelligence/{topic}-intelligence-{date}.md
  body: synthesis of support/gap findings, weak-claim escalations

---

## STAGE 5 — Synthesize

### ENTER
Load all four prior artifacts. Review hypothesis, evidence, and analysis together.

### WORK
Write the evidence brief: claim supported by evidence, claims weakened by thin evidence
(name the stage that flagged it and the specific weakened assertion), overall confidence.

### CLOSE
Write artifact:

  path: simulations/prove/synthesize/{topic}-synthesize-{date}.md
  frontmatter:
    topic: {topic}
    date: {date}
    hypothesis_source: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
    confidence: [high | medium | low]
  body: evidence brief, per-claim confidence, thin-evidence qualifications

End with: "Evidence brief ready for topic-story."
```

---

## V-02 — Axis: Output Format (Table-Dominant)

**Variation axis**: All structured campaign metadata, stage entry conditions, and write
instructions use 3-column tables with explicit column headers. The GATE block is a
2-row table (condition / status / action). Each stage opens with a STAGE SUMMARY table
(input artifact / stage product / write path) before any prose instruction. Write
instructions are tables rather than indented blocks.

**Hypothesis**: The per-stage write instruction in C-05 requires the full artifact path
at every stage. A table format where `Write path` is a named column makes it structurally
impossible to omit the path — the column must be filled or the table is visibly
incomplete. The STAGE SUMMARY table also surfaces C-07 (scout anchor) as a required
`Input artifact` column entry at Stage 1, making omission visible.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for {topic}.
Five stages produce five artifacts. Read the GATE before beginning Stage 1.

---

## GATE — Required Before Stage 1

| Condition | Required value | Action if missing |
|-----------|---------------|-------------------|
| scout_record present | simulations/scout/record/{topic}-scout-record-{date}.md | STOP — complete scouting first |

Do not begin Stage 1 if this condition is unmet.

---

## STAGE 1 — Hypothesis

| Field | Value |
|-------|-------|
| Input artifact | simulations/scout/record/{topic}-scout-record-{date}.md |
| Stage product | Hypothesis + counter-hypothesis |
| Write path | simulations/prove/hypothesis/{topic}-hypothesis-{date}.md |

Load the scout artifact. Extract the strongest signal it provides for {topic}.
State the hypothesis: one sentence. State the counter-hypothesis: one sentence.

Write artifact at the path shown in the STAGE SUMMARY table. Include in frontmatter:

| Frontmatter field | Value |
|------------------|-------|
| topic | {topic} |
| date | {date} |
| scout_source | simulations/scout/record/{topic}-scout-record-{date}.md |
| hypothesis | [one-sentence claim] |
| counter_hypothesis | [one-sentence opposing claim] |

---

## STAGE 2 — Web Search

| Field | Value |
|-------|-------|
| Input artifact | simulations/prove/hypothesis/{topic}-hypothesis-{date}.md |
| Stage product | External evidence summary |
| Write path | simulations/prove/websearch/{topic}-websearch-{date}.md |

Generate 3–5 queries from the hypothesis. Run them. For each source:

| Source | Supports / Challenges | Evidence quality |
|--------|----------------------|-----------------|
| [source 1] | | thin / adequate / strong |
| [source N] | | |

Flag any thin row now: "THIN EVIDENCE: [what is absent]."

Write artifact at simulations/prove/websearch/{topic}-websearch-{date}.md.

---

## STAGE 3 — Intelligence

| Field | Value |
|-------|-------|
| Input artifact | simulations/prove/hypothesis/{topic}-hypothesis-{date}.md |
| Stage product | Internal source scan |
| Write path | simulations/prove/intelligence/{topic}-intelligence-{date}.md |

Scan internal sources. For each source type:

| Source type | Finding | Evidence quality |
|-------------|---------|-----------------|
| [type 1] | | thin / adequate / strong |
| [type N] | | |

Flag any thin row now: "THIN EVIDENCE: [what is absent]."

Write artifact at simulations/prove/intelligence/{topic}-intelligence-{date}.md.

---

## STAGE 4 — Analysis

| Field | Value |
|-------|-------|
| Input artifacts | simulations/prove/websearch/{topic}-websearch-{date}.md, simulations/prove/intelligence/{topic}-intelligence-{date}.md |
| Stage product | Gap and strength assessment |
| Write path | simulations/prove/analysis/{topic}-analysis-{date}.md |

Combine web and intelligence findings. Identify: what is strong, what is thin,
what is absent. For any thin-evidence flag carried forward:

| Thin finding | Hypothesis element it weakens | Stage flagged |
|-------------|------------------------------|--------------|
| [finding] | [claim] | Stage 2 or 3 |

Write artifact at simulations/prove/analysis/{topic}-analysis-{date}.md.

---

## STAGE 5 — Synthesize

| Field | Value |
|-------|-------|
| Input artifacts | All four prior artifacts |
| Stage product | Evidence brief |
| Write path | simulations/prove/synthesize/{topic}-synthesize-{date}.md |

Write the evidence brief. For each hypothesis element, give a confidence verdict.
For any element weakened by a Stage 2–4 thin-evidence flag, name the stage and the
specific weakened claim.

Write artifact at simulations/prove/synthesize/{topic}-synthesize-{date}.md.

End the artifact with: "Evidence brief ready for topic-story."
```

---

## V-03 — Axis: Inertia Framing

**Variation axis**: The status-quo comparator is named as a persistent antagonist
throughout the campaign. CAMPAIGN OPEN includes an INCUMBENT block. Stages 2, 3,
and 4 each contain a dedicated INCUMBENT CHECK prompt: "Does this evidence help
displace {incumbent}?" The synthesis is framed as "The case against {incumbent}."
Evidence gaps are flagged in displacement terms: "THIN EVIDENCE: [what the incumbent's
defenders will say remains unanswered]."

**Hypothesis**: C-08 (evidence gaps flagged at point of discovery) is easier to satisfy
when the gap-flag prompt is built into each stage. Framing the gap as "what the
incumbent's defenders will say" makes the flag feel organic rather than a checklist item.
The per-stage INCUMBENT CHECK also naturally surfaces C-09 (thin evidence traces to a
specific claim) because the incumbent's strongest defense is the gap that matters most.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for {topic}.
The goal: build the case for displacing {status_quo_comparator} with {topic}.
Five stages. Each stage asks: does this evidence help unseat {status_quo_comparator}?

---

## CAMPAIGN OPEN

Before Stage 1, fill:

  topic:                  {topic}
  date:                   {date}
  incumbent:              {status_quo_comparator}
  incumbent_strength:     [what makes {status_quo_comparator} hard to displace]
  scout_record:           simulations/scout/record/{topic}-scout-record-{date}.md

If scout_record is absent — stop. Evidence campaign requires prior scouting.

---

## STAGE 1 — Hypothesis

Load simulations/scout/record/{topic}-scout-record-{date}.md.

From the scout findings, frame the displacement claim: what does {topic} deliver that
{incumbent} cannot? State the counter-hypothesis as the incumbent's strongest defense.

Write: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md

Frontmatter must include:
  scout_source: simulations/scout/record/{topic}-scout-record-{date}.md
  hypothesis:   [displacement claim]
  counter_hypothesis: [incumbent's strongest defense]

---

## STAGE 2 — Web Search

Load simulations/prove/hypothesis/{topic}-hypothesis-{date}.md.

Run 3–5 searches. For each result, ask: does this evidence support the displacement claim,
or does it reinforce {incumbent}'s position?

INCUMBENT CHECK:
  - Does the evidence address {incumbent}'s stated strength? [ ] YES  [ ] NO
  - If NO — flag: "THIN EVIDENCE: [{incumbent}'s defenders will say: ___]"

Write: simulations/prove/websearch/{topic}-websearch-{date}.md

Include all INCUMBENT CHECK verdicts and THIN EVIDENCE flags in the artifact.

---

## STAGE 3 — Intelligence

Scan internal sources (specs, research, patterns, metrics) for signals relevant to
the displacement claim.

INCUMBENT CHECK:
  - Does internal evidence show a concrete advantage over {incumbent}? [ ] YES  [ ] NO
  - If NO — flag: "THIN EVIDENCE: [{incumbent}'s defenders will say: ___]"

Write: simulations/prove/intelligence/{topic}-intelligence-{date}.md

Include all INCUMBENT CHECK verdicts and THIN EVIDENCE flags in the artifact.

---

## STAGE 4 — Analysis

Load simulations/prove/websearch/{topic}-websearch-{date}.md and
simulations/prove/intelligence/{topic}-intelligence-{date}.md.

Assess: what evidence supports displacement? What remains unanswered in {incumbent}'s
favor? Escalate any THIN EVIDENCE flag to a WEAK CLAIM if it undermines a specific
element of the hypothesis.

INCUMBENT CHECK:
  - Does the combined analysis favor displacement over continuity? [ ] YES  [ ] NO
  - For each WEAK CLAIM, name: which hypothesis element it weakens.

Write: simulations/prove/analysis/{topic}-analysis-{date}.md

---

## STAGE 5 — Synthesize

Load all four prior artifacts. Frame the synthesis as: "The case against {incumbent}."

Structure:
1. The displacement claim (from hypothesis)
2. Evidence supporting displacement (from web + intelligence + analysis)
3. Remaining gaps — for each THIN EVIDENCE flag carried forward, name the stage it
   originated, the hypothesis element it weakens, and the adjusted confidence level
4. Overall verdict: displacement supported / contested / insufficient evidence

Write: simulations/prove/synthesize/{topic}-synthesize-{date}.md

End with: "Evidence brief ready for topic-story."
```

---

## V-04 — Combined: Phrasing Register + Output Format

**Variation axes**: (1) Phrasing register: second-person imperatives throughout —
"Read the scout file now.", "Flag this here:", "Write the artifact before moving on."
No SESSION INVARIANT or formal register. Direct commands with no preamble. (2) Output
format: mixed — prose instructions use imperative sentences, structured data uses
compact inline blocks (not tables). Write instructions are single-line `Write:` commands.

**Hypothesis**: A conversational, direct register reduces the distance between the prompt
and the practitioner's action. "Write the artifact before moving on" is harder to ignore
than "A write instruction is issued at each stage." Per-stage `Write:` lines as
single-command instructions test whether the C-05 full-path requirement is easier to
satisfy in a terse format than in a table or block format.

---

```
Topic: {topic}
Date:  {date}

Run the full prove evidence campaign for {topic}. Five stages. Write one artifact per
stage before moving to the next. All five writes happen as you go — not at the end.

---

## Before you start

Check: does simulations/scout/record/{topic}-scout-record-{date}.md exist?
If NO — stop here. Run scouting first.
If YES — continue.

---

## Stage 1 — Hypothesis

Open simulations/scout/record/{topic}-scout-record-{date}.md. Read it now.

What is the strongest signal in the scout record for {topic}? Use it to frame one
hypothesis sentence. Then write the counter-hypothesis: the strongest argument for
leaving {status_quo_comparator} in place.

Write: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md

Put these fields in the frontmatter:
  scout_source: simulations/scout/record/{topic}-scout-record-{date}.md
  hypothesis: [your one-sentence claim]
  counter_hypothesis: [strongest opposing claim]

Write the artifact. Then move to Stage 2.

---

## Stage 2 — Web Search

Open simulations/prove/hypothesis/{topic}-hypothesis-{date}.md. Read the hypothesis.

Run 3–5 searches that test the hypothesis against external sources. For each source:
say whether it supports or challenges the hypothesis. If any search area comes back
empty or weak, flag it here: "THIN EVIDENCE: [what's missing]."

Write: simulations/prove/websearch/{topic}-websearch-{date}.md

Write the artifact. Then move to Stage 3.

---

## Stage 3 — Intelligence

Scan internal sources: specs, transcripts, prior research, metrics. Name which source
types you are checking. For each: what did you find? If a source type is absent or
empty, flag it here: "THIN EVIDENCE: [what's missing]."

Write: simulations/prove/intelligence/{topic}-intelligence-{date}.md

Write the artifact. Then move to Stage 4.

---

## Stage 4 — Analysis

Open simulations/prove/websearch/{topic}-websearch-{date}.md and
simulations/prove/intelligence/{topic}-intelligence-{date}.md.

Look at both sets of findings together. What's strong? What's thin? For any
thin-evidence flag from Stage 2 or 3 that undermines a specific part of the hypothesis,
escalate it: "WEAK CLAIM: [the assertion this evidence gap leaves unsupported]."

Write: simulations/prove/analysis/{topic}-analysis-{date}.md

Write the artifact. Then move to Stage 5.

---

## Stage 5 — Synthesize

Open all four artifacts. Write the evidence brief.

Cover: the main claim, the supporting evidence, the weak claims (name which stage
flagged each one and which hypothesis element it weakens), and the overall confidence.

Write: simulations/prove/synthesize/{topic}-synthesize-{date}.md

End the artifact with this exact line: "Evidence brief ready for topic-story."
```

---

## V-05 — Combined: All Four Axes

**Variation axes**: (1) Lifecycle emphasis: explicit ENTER/CLOSE sub-sections per stage.
(2) Output format: GATE as a named section, write instructions as labeled `Write:` lines
with full frontmatter block. (3) Inertia framing: incumbent named in CAMPAIGN OPEN and
checked at Stages 2, 3, 4. (4) Phrasing register: formal label headers (CAMPAIGN OPEN,
GATE, ENTER, CLOSE) but imperative instructions within each sub-section.

**Hypothesis**: All four axes serve different rubric criteria. Lifecycle emphasis serves
C-03 and C-10 (CLOSE makes the write mandatory, GATE makes hypothesis entry structural).
Output format serves C-05 (full path on every write) and C-07 (scout_source in frontmatter
block). Inertia framing serves C-08 and C-09 (per-stage INCUMBENT CHECK forces gap-flag
at each stage; escalation to WEAK CLAIM surfaces C-09). Phrasing register serves C-06
(GATE is a labeled section, not an inline sentence). The hypothesis is that all four axes
can coexist without inflating the prompt past the point where a practitioner will read it
carefully — structural density without structural noise.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for {topic}.
Goal: build the case for displacing {status_quo_comparator} with {topic}.
Five stages. Each stage: ENTER (load inputs), WORK (gather or analyze), CLOSE (write artifact).

---

## CAMPAIGN OPEN

Fill before any stage begins:

  topic:              {topic}
  date:               {date}
  incumbent:          {status_quo_comparator}
  incumbent_strength: [what makes the incumbent hard to displace]
  scout_record:       simulations/scout/record/{topic}-scout-record-{date}.md

---

## GATE

Required before Stage 1:

  scout_record present at simulations/scout/record/{topic}-scout-record-{date}.md?
  [ ] YES — proceed to Stage 1
  [ ] NO  — STOP. Complete scouting before running this campaign.

This gate does not have a fallback. If the scout record is absent, the campaign
cannot begin.

---

## STAGE 1 — Hypothesis

### ENTER
Load simulations/scout/record/{topic}-scout-record-{date}.md.
Identify the strongest signal the scout provides for {topic}.
Name the incumbent: {status_quo_comparator}.

### WORK
Frame the hypothesis: one sentence stating what {topic} delivers that {incumbent} cannot.
Frame the counter-hypothesis: {incumbent}'s strongest defense in one sentence.

### CLOSE
Write: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md

  frontmatter:
    topic: {topic}
    date: {date}
    scout_source: simulations/scout/record/{topic}-scout-record-{date}.md
    hypothesis: [displacement claim]
    counter_hypothesis: [incumbent's strongest defense]

---

## STAGE 2 — Web Search

### ENTER
Load simulations/prove/hypothesis/{topic}-hypothesis-{date}.md.
Prepare 3–5 search queries that test the hypothesis.

### WORK
Run searches. For each result, record support or challenge.

INCUMBENT CHECK — Does this evidence address {incumbent}'s stated strength?
  [ ] YES — record how
  [ ] NO  — flag now: "THIN EVIDENCE: [{incumbent}'s defenders will say: ___]"

### CLOSE
Write: simulations/prove/websearch/{topic}-websearch-{date}.md

  frontmatter:
    topic: {topic}
    date: {date}
    hypothesis_source: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  body: findings, INCUMBENT CHECK verdicts, THIN EVIDENCE flags

---

## STAGE 3 — Intelligence

### ENTER
Identify internal source types: specs, transcripts, research, patterns, metrics.
Load simulations/prove/hypothesis/{topic}-hypothesis-{date}.md.

### WORK
Scan each source type. Record findings.

INCUMBENT CHECK — Does internal evidence show concrete advantage over {incumbent}?
  [ ] YES — record the finding
  [ ] NO  — flag now: "THIN EVIDENCE: [{incumbent}'s defenders will say: ___]"

### CLOSE
Write: simulations/prove/intelligence/{topic}-intelligence-{date}.md

  frontmatter:
    topic: {topic}
    date: {date}
    hypothesis_source: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  body: findings per source type, INCUMBENT CHECK verdicts, THIN EVIDENCE flags

---

## STAGE 4 — Analysis

### ENTER
Load simulations/prove/websearch/{topic}-websearch-{date}.md and
simulations/prove/intelligence/{topic}-intelligence-{date}.md.

### WORK
Assess combined findings. Identify strong evidence and gaps.

INCUMBENT CHECK — Does the combined evidence favor displacement over continuity?
  [ ] YES — proceed
  [ ] NO  — flag now: "THIN EVIDENCE: [what remains unanswered in {incumbent}'s favor]"

For each THIN EVIDENCE flag carried forward from Stages 2 or 3:
  Escalate to WEAK CLAIM if it undermines a specific hypothesis element.
  Format: "WEAK CLAIM: [which assertion] — evidence gap from [Stage N]"

### CLOSE
Write: simulations/prove/analysis/{topic}-analysis-{date}.md

  frontmatter:
    topic: {topic}
    date: {date}
    websearch_source: simulations/prove/websearch/{topic}-websearch-{date}.md
    intelligence_source: simulations/prove/intelligence/{topic}-intelligence-{date}.md
  body: strength assessment, INCUMBENT CHECK verdict, WEAK CLAIM escalations

---

## STAGE 5 — Synthesize

### ENTER
Load all four prior artifacts:
  simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  simulations/prove/websearch/{topic}-websearch-{date}.md
  simulations/prove/intelligence/{topic}-intelligence-{date}.md
  simulations/prove/analysis/{topic}-analysis-{date}.md

### WORK
Frame the evidence brief as: "The case against {incumbent}."

Structure:
1. The displacement claim
2. Supporting evidence (strong findings from Stages 2–4)
3. Qualifications — for each WEAK CLAIM: name the originating stage, the specific
   hypothesis element it weakens, and the adjusted confidence for that element
4. Overall confidence: high / medium / low

### CLOSE
Write: simulations/prove/synthesize/{topic}-synthesize-{date}.md

  frontmatter:
    topic: {topic}
    date: {date}
    confidence: [high | medium | low]
    hypothesis_source: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md

End the artifact body with: "Evidence brief ready for topic-story."
```
