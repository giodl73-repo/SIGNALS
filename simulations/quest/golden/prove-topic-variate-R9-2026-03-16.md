---
skill: quest-variate
skill_target: prove-topic
round: R9
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [claim_decomposition, scout_extraction_protocol, phased_read_back_blocking]
  combined: [V-04 (claim_decomposition+evidence_strength_tiering), V-05 (scout_extraction+phased_blocking+backward_citation_chain)]
r8_context: >
  R8 explored three single axes: inertia_framing, confidence_gate, evidence_gap_inventory.
  V-04 combined inertia_framing with exit_signal_chaining (proven 100/100 from R2).
  V-05 combined confidence_gate + staged_hypothesis_sharpening + two_write_synthesis.
  R9 explores three axes not yet tried under v14:
  (1) claim_decomposition -- Stage 1 hypothesis is decomposed into 2-3 falsifiable
  sub-claims; evidence stages track support per sub-claim; Stage 4 analysis grades each
  sub-claim independently; synthesis derives the overall verdict from the binding
  constraint (weakest sub-claim grade). Distinct from staged_hypothesis_sharpening
  (revising a single claim) and competing_explanation_protocol (alternative causes).
  (2) scout_extraction_protocol -- Stage 0 does not merely locate and block; it actively
  reads the scout and extracts four named fields (key_insight, open_question, named_gap,
  status_quo_implied) into the campaign record. Hypothesis frontmatter must carry all four.
  Distinct from scout_source anchor (C-07): requires structured extraction of content,
  not just a path reference.
  (3) phased_read_back_blocking -- each stage has two blocking conditions: (a) previous
  artifact exists, AND (b) a verbatim sentence is quoted from it. Enforces evidence chain
  continuity differently from GATE blocks (which verify presence): verifies consumption.
  V-04 combines claim_decomposition (V-01) with evidence_strength_tiering (R7-V01):
  each sub-claim's evidence is tiered Strong/Moderate/Weak; Stage 4 produces a verdict
  matrix (sub-claim x tier profile); synthesis derives the verdict from the weakest
  sub-claim and reports the aggregate tier distribution as evidence quality signal.
  V-05 combines scout_extraction_protocol (V-02) + phased_read_back_blocking (V-03) +
  backward_citation_chain (R6-V02): extracted scout fields anchor every stage; read-back
  blocking ensures artifact consumption at each boundary; backward citation ensures
  synthesis is traceable. Three independent failure modes addressed: scout content unused,
  prior artifacts not read, synthesis claims not traceable.
  All R9 variations carry: (1) explicit scout-blocking before Stage 1, (2) per-stage
  artifact writes with full paths, (3) scout_source in hypothesis frontmatter, (4) THIN:
  flagging at point of discovery, (5) exact readiness statement closing synthesis.
---

# prove-topic -- Variate Round 9 (Rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-10 aspirational)
**Date**: 2026-03-16
**Round**: 9

---

## Artifact Paths (all variations)

| Stage | Signal             | Path                                                                        |
|-------|--------------------|-----------------------------------------------------------------------------|
| 1     | prove-hypothesis   | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`     |
| 2     | prove-websearch    | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`       |
| 3     | prove-intelligence | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |
| 4     | prove-analysis     | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`         |
| 5     | prove-synthesize   | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`     |

---

## V-01 -- Axis: Claim Decomposition

**Variation axis**: Claim decomposition only -- the Stage 1 hypothesis is not a single
top-level assertion but a set of 2-3 falsifiable sub-claims. Evidence stages track
supporting and opposing evidence per sub-claim, not just per hypothesis overall. Stage 4
analysis grades each sub-claim independently: Supported / Partially Supported / Unsupported.
Synthesis derives the overall verdict from the weakest sub-claim grade (the binding
constraint) and explicitly names which sub-claim caps the verdict.

**Hypothesis**: A single top-level hypothesis encourages investigators to treat mixed
evidence as net positive or negative without exposing which specific component drives
the verdict. Decomposing into sub-claims forces the investigator to discover and report
which aspects of {topic} are well-evidenced and which are not. The binding-constraint
framing in synthesis makes the verdict explainable: "PARTIALLY SUPPORTED because sub-claim
B has only weak external evidence" is more useful than an undifferentiated label. It also
reveals the minimal intervention: the team knows exactly what evidence would change the
verdict.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic}. The hypothesis is decomposed into
sub-claims. Evidence is tracked per sub-claim. The synthesis verdict derives from the
weakest sub-claim.

## SETUP

Locate the scout artifact: glob `simulations/scout/{topic}-scout-*.md`

SCOUT READY cannot fire without a found file.
If absent: emit "SCOUT READY: BLOCKED. No scout artifact for {topic}. Run scout first."
Halt. Stage 1 cannot begin.
If found: emit "SCOUT READY: [path]"
  scout_source: [path]

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 -- HYPOTHESIS WITH SUB-CLAIMS

Entry: SCOUT READY fired.

Read the scout artifact. Frame the central hypothesis, then decompose it into exactly
2-3 falsifiable sub-claims:

  hypothesis: [top-level claim -- what does {topic} enable or displace?]
  sub_claim_A: [first falsifiable component -- e.g., performance dimension]
  sub_claim_B: [second falsifiable component -- e.g., adoption dimension]
  sub_claim_C: [third falsifiable component, if applicable -- otherwise omit]

Each sub-claim must be independently falsifiable: evidence against A cannot
automatically disprove B. Include a falsification condition for each sub-claim.

Frontmatter must include:
  scout_source: [SCOUT READY path]
  sub_claims: [A, B, C]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path]"

STAGE 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH (per sub-claim)

Entry: STAGE 1 COMPLETE fired.

Gather external evidence. For each source, record which sub-claim it addresses:

  | Sub-Claim | Source | One-line summary | Supports / Opposes / Inconclusive |
  |-----------|--------|-----------------|-----------------------------------|

Note THIN: [sub_claim] -- [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path]"

STAGE 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE (per sub-claim)

Entry: STAGE 2 COMPLETE fired.

Search internal sources (simulations/, specs, artifacts). For each finding:

  | Sub-Claim | File Path | Passage summary | Supports / Opposes / Inconclusive |
  |-----------|-----------|----------------|-----------------------------------|

Note THIN: [sub_claim] -- [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path]"

STAGE 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS (per sub-claim verdict)

Entry: STAGE 3 COMPLETE fired.

Grade each sub-claim using combined Stage 2 + Stage 3 evidence:

  | Sub-Claim | Supporting | Opposing | THIN flags | Grade |
  |-----------|-----------|---------|------------|-------|
  | A         | N sources  | N sources | N        | Supported / Partially Supported / Unsupported |
  | B         | ...        | ...      | ...       | ...   |
  | C (if any)| ...       | ...      | ...       | ...   |

Identify the binding constraint: the sub-claim with the weakest grade. If grades are
equal, the sub-claim with the most THIN flags is the binding constraint.

  binding_constraint: [sub-claim identifier] -- [one sentence: why this is the ceiling]

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path]"

STAGE 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS (verdict from binding constraint)

Entry: STAGE 4 COMPLETE fired.

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

State the binding constraint in one sentence:
  The verdict is [label] because [binding_constraint sub-claim] [grade and reason].

For each sub-claim, state the grade and one supporting sentence.

For each THIN flag from Stages 2-3: name the sub-claim, the weakened assertion,
and adjusted confidence for that sub-claim.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

---

## V-02 -- Axis: Scout Extraction Protocol

**Variation axis**: Scout extraction protocol only -- Stage 0 does not merely locate
the scout artifact and block on its presence; it actively reads the file and extracts
four named fields into the campaign record. The hypothesis frontmatter must carry all
four extracted fields. Hypothesis formation explicitly builds on the extracted fields.

**Hypothesis**: Requiring only a path reference to the scout (C-07) permits investigators
to acknowledge the source without actually using its content. Scout extraction forces a
structured read before any hypothesis forms. The four fields -- key_insight, open_question,
named_gap, status_quo_implied -- make the scout's contribution to the hypothesis legible
and auditable: a hypothesis that cannot trace its components to an extracted field is
ungrounded even if it names the scout path. The open_question field is particularly
valuable: it focuses Stages 2 and 3 on what the scout could not resolve, not just on
what it already found.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic}. Before forming any hypothesis,
extract structured content from the scout artifact. Subsequent stages build on the
extracted fields.

## STAGE 0 -- SCOUT EXTRACTION

1. Glob `simulations/scout/{topic}-scout-*.md`.
   If absent: emit "STAGE 0 BLOCKED. No scout artifact for {topic}. Run scout first."
   Halt. Stage 1 cannot begin.

2. Read the scout artifact at [found path].

3. Extract and record all five fields:

  scout_source: [exact path]
  key_insight: [the single most relevant finding from the scout to the hypothesis]
  open_question: [the most important thing the scout surfaced but could not resolve]
  named_gap: [evidence or information explicitly absent from the scout]
  status_quo_implied: [the incumbent named or clearly implied by the scout -- concrete]

4. Emit:
STAGE 0 COMPLETE.
  scout_source: [path]
  key_insight: [value]
  open_question: [value]
  named_gap: [value]
  status_quo_implied: [value]

Stage 1 cannot begin until STAGE 0 COMPLETE fires with all five fields populated.

---

## STAGE 1 -- HYPOTHESIS

Entry: STAGE 0 COMPLETE fired with all five extraction fields.

Frame the hypothesis using the extracted fields -- do not re-read the scout file:
- Build on key_insight as primary grounding
- Address open_question as the specific uncertainty this campaign will resolve
- Acknowledge named_gap as a known limitation of the evidence base
- Frame the claim against status_quo_implied as the incumbent

Frontmatter must carry all five extraction fields:

  scout_source: [from STAGE 0]
  key_insight: [from STAGE 0]
  open_question: [from STAGE 0]
  named_gap: [from STAGE 0]
  status_quo_implied: [from STAGE 0]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path]"

STAGE 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH

Entry: STAGE 1 COMPLETE fired.

Gather external evidence. Priority: evidence addressing open_question and filling
named_gap from Stage 0.

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path]"

STAGE 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE

Entry: STAGE 2 COMPLETE fired.

Search internal sources (simulations/, specs, artifacts). Priority: sources addressing
open_question or filling named_gap.

Note THIN: [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path]"

STAGE 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS

Entry: STAGE 3 COMPLETE fired.

Analyze evidence from Stages 2-3. Report resolution status for the extraction fields:

  open_question_resolved: [Yes / Partially / No] -- [one sentence]
  named_gap_status: [Filled / Partially Filled / Still Open] -- [one sentence]

Aggregate THIN flags. Displacement verdict: Yes / No / Pending. Explain in 1-2 sentences.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path]"

STAGE 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS

Entry: STAGE 4 COMPLETE fired.

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Report the extraction-to-verdict chain:
  key_insight used: [how it grounded the hypothesis]
  open_question outcome: [resolved / unresolved -- effect on verdict confidence]
  named_gap outcome: [filled / still open -- effect on verdict confidence]

For each THIN flag: name source stage, weakened claim, adjusted confidence.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

---

## V-03 -- Axis: Phased Read-Back Blocking

**Variation axis**: Phased read-back blocking only -- each stage has two blocking
conditions: (a) the previous stage artifact exists, AND (b) a verbatim sentence from
that artifact is quoted, proving it was read. Both conditions must clear before the next
stage begins.

**Hypothesis**: Standard GATE blocks prevent out-of-order execution but do not prevent
investigators from writing a new artifact without referencing the prior one's content.
An investigator can confirm STAGE 1 COMPLETE and then conduct Stage 2 from scratch
without consulting what Stage 1 actually said. Read-back blocking makes content
consumption observable: a verbatim sentence from the Stage 1 artifact at the Stage 2
entry point is evidence that Stage 1 content informed Stage 2 work. Without this
requirement, stages can chain in the correct order while each one effectively reinvents
the evidence independently. Read-back blocking makes the evidence chain cumulative rather
than parallel.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic}. Each stage boundary requires two
conditions: (1) previous artifact exists, AND (2) a verbatim sentence from it is quoted.

## SETUP

Locate the scout artifact: glob `simulations/scout/{topic}-scout-*.md`

If absent: emit "SETUP BLOCKED. No scout artifact for {topic}. Run scout first." Halt.

If found:
  scout_source: [path]
  Read the file.
  Quote one sentence that will ground the hypothesis:
    scout_read_confirmation: "[verbatim sentence from scout artifact]"

Emit: "SETUP COMPLETE. scout_source: [path]"

Stage 1 cannot begin until SETUP COMPLETE fires with scout_read_confirmation quoted.

---

## STAGE 1 -- HYPOTHESIS

Entry: SETUP COMPLETE fired. scout_read_confirmation quoted above.

Frame the hypothesis grounded in the scout content confirmed above.

Frontmatter must include:
  scout_source: [path from SETUP]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path]"

Stage 2 blocking conditions -- both required:
  [ ] STAGE 1 COMPLETE fired.
  [ ] hypothesis_read_confirmation: "[verbatim sentence from hypothesis artifact]"

---

## STAGE 2 -- WEBSEARCH

Entry: Stage 2 blocking conditions cleared.
Testing claim: "[hypothesis_read_confirmation]"

Gather external evidence for the claim confirmed above.
Note THIN: [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path]"

Stage 3 blocking conditions -- both required:
  [ ] STAGE 2 COMPLETE fired.
  [ ] websearch_read_confirmation: "[verbatim sentence from websearch artifact]"

---

## STAGE 3 -- INTELLIGENCE

Entry: Stage 3 blocking conditions cleared.
Following up on: "[websearch_read_confirmation]"

Search internal sources (simulations/, specs, artifacts). Build on the websearch finding
confirmed above.
Note THIN: [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path]"

Stage 4 blocking conditions -- both required:
  [ ] STAGE 3 COMPLETE fired.
  [ ] intelligence_read_confirmation: "[verbatim key finding from intelligence artifact]"

---

## STAGE 4 -- ANALYSIS

Entry: Stage 4 blocking conditions cleared.
Key internal finding: "[intelligence_read_confirmation]"

Aggregate all THIN flags from Stages 2-3. Map each to the hypothesis claim it weakens.
State displacement verdict: Yes / No / Pending. Explain in 1-2 sentences.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path]"

Stage 5 blocking conditions -- both required:
  [ ] STAGE 4 COMPLETE fired.
  [ ] analysis_read_confirmation: "[verbatim displacement verdict sentence from analysis artifact]"

---

## STAGE 5 -- SYNTHESIS

Entry: Stage 5 blocking conditions cleared.
Verdict confirmed: "[analysis_read_confirmation]"

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Summarize the evidence chain in 2-3 sentences. For each THIN flag: name source stage,
weakened claim, adjusted confidence.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

---

## V-04 -- Combined: Claim Decomposition + Evidence Strength Tiering

**Variation axes**: Claim decomposition (V-01 single axis this round) combined with
evidence strength tiering (R7-V01 proven pattern). Each sub-claim from Stage 1 is
evaluated with tiered evidence (Strong / Moderate / Weak). Stage 4 produces a verdict
matrix (sub-claim x tier profile). Synthesis derives the overall verdict from the
sub-claim with the weakest aggregate tier profile.

**Hypothesis**: Claim decomposition (V-01) surfaces which component of the hypothesis
is the binding constraint on the verdict. Evidence strength tiering (R7) surfaces whether
the verdict rests on strong or weak sources. Combined, they answer two questions
simultaneously: "which sub-claim fails?" and "why does it fail -- weak sources or
active opposition?" The verdict matrix makes both dimensions visible at once, producing
a synthesis that is not only traceable but shows the quality of the evidence behind each
component. A SUPPORTED verdict resting on Weak-tier evidence is qualitatively different
from one resting on Strong-tier evidence -- the matrix makes this explicit.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic}. The hypothesis is decomposed into
2-3 sub-claims. Evidence is tiered Strong/Moderate/Weak per sub-claim. Stage 4 builds
a verdict matrix. Synthesis derives the verdict from the binding constraint sub-claim.

## SETUP

Locate the scout artifact: glob `simulations/scout/{topic}-scout-*.md`

SCOUT READY cannot fire without a found file.
If absent: emit "SCOUT READY: BLOCKED." Stop.
If found: emit "SCOUT READY: [path]"
  scout_source: [path]

STAGE 1 cannot begin until SCOUT READY fires.

---

## STAGE 1 -- HYPOTHESIS WITH SUB-CLAIMS

Entry: SCOUT READY fired.

Read the scout artifact. Frame the top-level hypothesis and decompose into 2-3
independently falsifiable sub-claims. Include a falsification condition for each.

  hypothesis: [top-level claim]
  sub_claim_A: [first component with falsification condition]
  sub_claim_B: [second component with falsification condition]
  sub_claim_C: [third, if applicable]

Frontmatter must include:
  scout_source: [SCOUT READY path]
  sub_claims: [A, B, C]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path]"

STAGE 2 cannot begin until STAGE 1 COMPLETE fires.

---

## STAGE 2 -- WEBSEARCH (tiered, per sub-claim)

Entry: STAGE 1 COMPLETE fired.

Gather external evidence. For each source assign tier:
  Strong: primary source, direct evidence, published within 2 years
  Moderate: secondary source, indirect evidence, or 2-5 years old
  Weak: anecdotal, tertiary, older than 5 years, or single-point data

Record per source:

  | Sub-Claim | Source | Tier | Direction | One-line summary |
  |-----------|--------|------|-----------|-----------------|
  |           |        | S/M/W| Sup/Opp/Inc |               |

Note THIN: [sub_claim] -- [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path]"

STAGE 3 cannot begin until STAGE 2 COMPLETE fires.

---

## STAGE 3 -- INTELLIGENCE (tiered, per sub-claim)

Entry: STAGE 2 COMPLETE fired.

Search internal sources (simulations/, specs, artifacts). Apply same tier definitions.

  | Sub-Claim | File Path | Tier | Direction | One-line summary |
  |-----------|-----------|------|-----------|-----------------|
  |           |           | S/M/W| Sup/Opp/Inc |               |

Note THIN: [sub_claim] -- [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path]"

STAGE 4 cannot begin until STAGE 3 COMPLETE fires.

---

## STAGE 4 -- ANALYSIS (verdict matrix)

Entry: STAGE 3 COMPLETE fired.

Build the verdict matrix from combined Stage 2 + Stage 3 evidence:

  | Sub-Claim | Strong | Moderate | Weak | Opposing | THIN | Tier Profile | Grade |
  |-----------|--------|----------|------|----------|------|--------------|-------|
  | A         | N      | N        | N    | N        | N    | [dominant tier] | Supported / Partially / Unsupported |
  | B         | ...    | ...      | ...  | ...      | ...  | ...          | ...   |
  | C (if any)| ...    | ...      | ...  | ...      | ...  | ...          | ...   |

Tier profile note: if a sub-claim's evidence is predominantly Weak even if Direction
is Supports, note "weak tier profile -- confident verdict requires stronger sourcing."

Binding constraint:
  binding_constraint: [sub-claim with weakest grade] -- [one sentence: why]

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path]"

STAGE 5 cannot begin until STAGE 4 COMPLETE fires.

---

## STAGE 5 -- SYNTHESIS (verdict from binding constraint)

Entry: STAGE 4 COMPLETE fired.

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Binding constraint statement:
  The verdict is [label] because sub-claim [X] [grade and tier profile in one sentence].

For each sub-claim: state grade, tier profile, and one supporting sentence.

Evidence quality note: summarize aggregate tier distribution across all sub-claims
(e.g., "8 of 11 evidence items Strong or Moderate -- verdict rests on solid base").

For each THIN flag: name sub-claim, weakened assertion, adjusted confidence.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

---

## V-05 -- Combined: Scout Extraction + Phased Read-Back Blocking + Backward Citation Chain

**Variation axes**: Scout extraction protocol (V-02 single axis this round), phased
read-back blocking (V-03 single axis this round), and backward citation chain (R6-V02
proven pattern under v14). Three axes addressing three independent failure modes in the
evidence chain: (1) scout content extracted but unused, (2) prior artifacts written but
not consumed, (3) synthesis claims not traceable to specific stage artifacts.

**Hypothesis**: R6's backward citation chain ensures synthesis traceability but does
not address whether the scout was actually used or whether each stage built on the prior
one. Scout extraction (V-02) closes the first gap at Stage 0. Read-back blocking (V-03)
closes the second at each stage boundary. Backward citation (R6) closes the third in
Stage 5. None of these axes competes with another: extraction ensures input quality,
read-back ensures continuity, backward citation ensures traceability. Together they harden
the complete evidence chain from scout through synthesis, with each mechanism operating
at a different point in the chain.

---

Topic: {topic}
Date: {date}

Run the full prove evidence campaign for {topic}. Stage 0 extracts structured content
from the scout. Each stage boundary requires a quoted read-back from the prior artifact.
Synthesis cites each stage artifact by path with a representative quoted passage.

## STAGE 0 -- SCOUT EXTRACTION

1. Glob `simulations/scout/{topic}-scout-*.md`.
   If absent: emit "STAGE 0 BLOCKED. No scout artifact for {topic}. Run scout first."
   Halt. Stage 1 cannot begin.

2. Read the scout artifact at [found path].

3. Extract and record:

  scout_source: [exact path]
  key_insight: [most relevant finding to the hypothesis]
  open_question: [most important unresolved question the scout surfaced]
  named_gap: [evidence or information explicitly absent from the scout]
  status_quo_implied: [incumbent named or clearly implied by the scout -- concrete]
  scout_read_confirmation: "[verbatim sentence from scout artifact]"

4. Emit:
STAGE 0 COMPLETE.
  scout_source: [path]
  key_insight: [value]
  open_question: [value]
  named_gap: [value]
  status_quo_implied: [value]
  scout_read_confirmation: "[verbatim sentence]"

Stage 1 entry blocked until STAGE 0 COMPLETE fires with all six fields.

---

## STAGE 1 -- HYPOTHESIS

Entry: STAGE 0 COMPLETE fired.

Frame the hypothesis grounded in the extraction fields. Must reference key_insight
as primary grounding and address open_question as the central uncertainty.

Frontmatter must include:
  scout_source: [from STAGE 0]
  key_insight: [from STAGE 0]
  open_question: [from STAGE 0]
  named_gap: [from STAGE 0]
  status_quo_implied: [from STAGE 0]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write. Emit: "STAGE 1 COMPLETE: [path]"

Stage 2 blocking conditions -- both required:
  [ ] STAGE 1 COMPLETE fired.
  [ ] hypothesis_read_confirmation: "[verbatim hypothesis sentence websearch will test]"

---

## STAGE 2 -- WEBSEARCH

Entry: Stage 2 blocking conditions cleared.
Testing: "[hypothesis_read_confirmation]"

Priority: evidence addressing open_question and filling named_gap from Stage 0.
Note THIN: [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write. Emit: "STAGE 2 COMPLETE: [path]"

Stage 3 blocking conditions -- both required:
  [ ] STAGE 2 COMPLETE fired.
  [ ] websearch_read_confirmation: "[verbatim sentence from websearch artifact]"

---

## STAGE 3 -- INTELLIGENCE

Entry: Stage 3 blocking conditions cleared.
Following up on: "[websearch_read_confirmation]"

Search internal sources. Priority: sources addressing open_question or filling named_gap.
Note THIN: [area] -- [gap] at point of discovery. Do not defer.

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write. Emit: "STAGE 3 COMPLETE: [path]"

Stage 4 blocking conditions -- both required:
  [ ] STAGE 3 COMPLETE fired.
  [ ] intelligence_read_confirmation: "[verbatim key finding from intelligence artifact]"

---

## STAGE 4 -- ANALYSIS

Entry: Stage 4 blocking conditions cleared.
Key internal finding: "[intelligence_read_confirmation]"

Report open_question and named_gap resolution:
  open_question_resolved: [Yes / Partially / No] -- [one sentence]
  named_gap_status: [Filled / Partially Filled / Still Open] -- [one sentence]

Aggregate THIN flags. Map each to the hypothesis claim it weakens. Displacement verdict:
Yes / No / Pending. Explain in 1-2 sentences.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write. Emit: "STAGE 4 COMPLETE: [path]"

Stage 5 blocking conditions -- both required:
  [ ] STAGE 4 COMPLETE fired.
  [ ] analysis_read_confirmation: "[verbatim displacement verdict sentence from analysis]"

---

## STAGE 5 -- SYNTHESIS (with backward citation chain)

Entry: Stage 5 blocking conditions cleared.
Verdict received: "[analysis_read_confirmation]"

Lead with: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

Report the scout-to-verdict chain with backward citations to each stage artifact:

  Stage 0 scout:      simulations/scout/{topic}-scout-{date}.md
    key_insight used: [how it grounded the hypothesis]
    open_question:    [resolved / unresolved -- effect on confidence]
    named_gap:        [filled / still open -- effect on confidence]

  Stage 1 hypothesis: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
    cited: "[verbatim hypothesis sentence]"

  Stage 2 websearch:  simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
    cited: "[verbatim finding most relevant to verdict]"

  Stage 3 intelligence: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
    cited: "[verbatim internal finding most relevant to verdict]"

  Stage 4 analysis:   simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
    cited: "[verbatim displacement verdict sentence]"

For each THIN flag: name source stage, weakened claim, adjusted confidence.

Close with exactly:
Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.
