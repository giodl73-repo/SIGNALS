---
skill: quest-variate
skill_target: prove-topic
round: R1
date: 2026-03-15
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [role_sequence, output_format, lifecycle_emphasis]
  combined: [V-04, V-05]
---

# prove-topic — Variation Round R1

Five complete, runnable skill body prompts. Each is self-contained — no diff, no cross-references.

---

## V-01 — Axis: Role Sequence (scout-first, hypothesis-gated entry)

**Variation axis**: Role sequence — the orchestration opens with an explicit scout-loading pass before hypothesis formation begins. The scout handoff is a named gate, not an assumption.

**Hypothesis**: Forcing scout signal loading as an explicit first-class role — rather than a background reference — increases hypothesis grounding quality because the model commits to named scout findings before the claim is written.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic. Five stages execute in order.
Each stage writes its artifact before the next stage begins.

---

## STAGE 0 — SCOUT LOAD

Before writing any hypothesis, load the prior signal record for this topic.

Search for existing scout artifacts:
  simulations/scout/**/{topic}-*.md

For each artifact found, record:
  | Artifact slug | Namespace | Key finding (one sentence) |
  |--------------|-----------|---------------------------|
  | [slug]       | [ns]      | [finding]                 |

If no artifacts found, write:
  "No prior scout signals found. Hypothesis will proceed from stated assumptions."

GATE S: Scout record is on file before proceeding. Do not write the hypothesis
        until this gate is complete. Post-gate: scout findings are read-only input.

---

## STAGE 1 — prove-hypothesis

Frame the claim for this topic. The hypothesis MUST reference at least one finding
from the SCOUT LOAD table above (or explicitly note absence).

Complete the prove-hypothesis template:

  Scout anchor: [Artifact slug and finding from SCOUT LOAD that this claim extends or challenges.]
                If no scout signals: "No prior signals — proceeding from assumption: [state it]."

  Claim: [One sentence. Use "is" or "will". No hedging.]

  Status quo (what the team does today without this capability):
    [One sentence. Name the current practice.]

  F-00 (hypothesis is false if current practice is sufficient):
    Observable test: [Externally measurable outcome indicating current practice is sufficient.]

  Falsification conditions:
    | ID   | Observable outcome that would falsify the claim |
    |------|--------------------------------------------------|
    | F-01 | [outcome] |
    | F-02 | [outcome] |

  Confidence (0-100): [N]
  Rationale: [2-3 sentences citing scout anchor and status-quo gap.]

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, scout_anchor (slug or "none"),
             status_quo_verdict (INSUFFICIENT/SUFFICIENT), f_id_count.

Confirm artifact written, then proceed to STAGE 2.

---

## STAGE 2 — prove-websearch

Gather external evidence bearing on the claim from STAGE 1.

  Hypothesis (carry forward verbatim from STAGE 1 Claim field):
    [claim text]

  Status quo anchor (from STAGE 1):
    [status quo text]

  Falsification event:
    The hypothesis predicts [claim]. Falsification = evidence that [contrary result]
    under [conditions] — i.e., no improvement over status quo.

  Null hypothesis: The status quo is sufficient because: _____.

For each search block:
  Query: [search string]
  | # | Title | URL | Finding | Supports / Contradicts / Neutral |
  |---|-------|-----|---------|----------------------------------|

  Rule: Minimum 2 distinct source URLs per block. If fewer found, run supplemental
        search immediately. Document: Supplemental query: [string]. Source: [title — URL].

Verdict token (set before synthesis, copy forward verbatim to artifact):
  [ ] SUPPORTS hypothesis  [ ] CONTRADICTS hypothesis  [ ] INCONCLUSIVE
  Confidence delta: [+N / -N / 0]
  Key signals: [1-3 bullet points, each citing a source slug]

Write artifact: simulations/prove/websearch/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, verdict_token, confidence_delta, signal_count,
             source_count, inertia_named (true/false).

Confirm artifact written, then proceed to STAGE 3.

---

## STAGE 3 — prove-intelligence

Scan internal sources for signals bearing on the claim.

  Sources to check (in order):
    1. simulations/scout/**/{topic}-*.md    (already loaded in STAGE 0 — summarize, do not re-derive)
    2. simulations/trace/**/{topic}-*.md
    3. simulations/review/**/{topic}-*.md
    4. simulations/draft/**/{topic}-*.md

  For each source found:
    | Source slug | Finding (one sentence) | Phase | Role (Primary/Supporting) | Inertia (absent/present) |
    |-------------|----------------------|-------|--------------------------|--------------------------|

  If a namespace has no artifacts: write "No {namespace} artifacts found."

  Intelligence verdict:
    Internal signals: [N found]
    Strongest internal signal: [slug — one sentence on what it establishes]
    Gaps: [what the internal record cannot establish for this hypothesis]

Write artifact: simulations/prove/intelligence/{topic}-intelligence-{date}.md
Frontmatter: skill, topic, date, signal_count, primary_count, inertia_present_count,
             gaps_identified (count).

Confirm artifact written, then proceed to STAGE 4.

---

## STAGE 4 — prove-analysis

Analyze the combined signal set from STAGES 2 and 3.

  Signal inventory (enumerate all signals from websearch + intelligence stages):
    | Signal # | Source stage | Phase | Role | Inertia | Finding (one sentence) |
    |----------|-------------|-------|------|---------|----------------------|

  Confidence ceiling derivation:
    Evidence phase coverage: [phases present]
    Primary signals by phase: [count per phase]
    Inertia coverage: [absent / partial / present]
    Ceiling: read from table below.

    | Evidence phase  | Inertia absent | Inertia present |
    |-----------------|----------------|-----------------|
    | Explore only    | 25             | 35              |
    | Test reached    | 45             | 60              |
    | Validate reached| 72             | 72              |
    | All phases      | —              | none            |

  Pattern finding:
    [One paragraph. What does the combined signal set establish and where does it break down?
    Name specific signals by number from the inventory above.]

  Thin-signal check:
    If any evidence-gathering stage (websearch, intelligence) returned zero substantive
    findings, name the gap here and its effect on the ceiling.

Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, signal_count_total, ceiling_value, inertia_coverage,
             thin_signal_stages (list or "none").

Confirm artifact written, then proceed to STAGE 5.

---

## STAGE 5 — prove-synthesize

Write the final evidence brief. This is the terminal artifact. It takes a position.

  Ceiling (carry forward from STAGE 4 Ceiling field): [N or "none"]

  NOT: begin synthesis reasoning before stating the ceiling.
  NOT: end the campaign with an analysis artifact as the final output.

  Write seven prose sections under these headers:

  **Ceiling Declaration**
    Evidence phase coverage: [phases]. Primary signals by phase: [count per phase].
    Inertia coverage: [absent / partial / present]. Confidence ceiling: [N or "none"].

  **Verdict/Confidence**
    State yes, no, or maybe in the first sentence. Give score (0-100), must not exceed ceiling.
    Name which signals drove the score up, what held it down.

  **Key Evidence**
    Top 3 signals. For each: finding + why it outranks alternatives (phase, role, inertia).

  **Counter-Evidence**
    Strongest argument against the verdict. Name source, phase, role, inertia classification.
    Omitting this section is not permitted.

  **Adoption Boundaries**
    What inertia-present signals tested. What inertia-absent signals can and cannot establish.
    Contexts with no inertia-present signal — name the absence.

  **Principles**
    1-3 generalizable principles. Declarative: "X implies Y." Not restatements of verdict.

  **Handoff**
    ready_for_topic_story: true
    Topic: {topic}
    Confidence verdict: [score and yes/no/maybe]
    Recommended next skill: /topic:story

Write artifact: simulations/prove/synthesize/{topic}-synthesize-{date}.md
Frontmatter: skill, topic, date, verdict (yes/no/maybe), confidence, ceiling_applied,
             ready_for_topic_story: true, stages_completed: [hypothesis, websearch,
             intelligence, analysis, synthesize].

Confirm artifact written. Campaign complete.

---

## Campaign Completion Check

Before closing, verify:
- [ ] STAGE 0: Scout load table on file
- [ ] STAGE 1: prove-hypothesis artifact written ({topic}-hypothesis-{date}.md)
- [ ] STAGE 2: prove-websearch artifact written ({topic}-websearch-{date}.md)
- [ ] STAGE 3: prove-intelligence artifact written ({topic}-intelligence-{date}.md)
- [ ] STAGE 4: prove-analysis artifact written ({topic}-analysis-{date}.md)
- [ ] STAGE 5: prove-synthesize artifact written ({topic}-synthesize-{date}.md)
- [ ] All artifacts share the {topic}- prefix
- [ ] Synthesis contains Handoff section with ready_for_topic_story: true

If any item is unchecked, complete it before reporting done.
```

---

## V-02 — Axis: Output Format (scorecard-style stage gates, tabular artifact manifest)

**Variation axis**: Output format — each stage completion is confirmed via a structured scorecard row rather than a prose confirm line. The campaign closes with a tabular artifact manifest that serves as both a completion check and a downstream handoff record.

**Hypothesis**: A tabular artifact manifest at stage boundaries reduces silent-skip failures (C-01, C-03) because the model must fill a row before advancing, making omission visible as a blank cell rather than absent prose.

---

```
Topic: {topic}
Date:  {date}

Prove evidence campaign — five stages, one artifact per stage.
Complete stages in order. Fill the stage scorecard row before advancing.

---

## Artifact Manifest (fill as you go)

| Stage | Skill              | Artifact path                                    | Written | Verdict token |
|-------|--------------------|--------------------------------------------------|---------|---------------|
| 1     | prove-hypothesis   | simulations/prove/hypothesis/{topic}-hypothesis-{date}.md | [ ]     | —             |
| 2     | prove-websearch    | simulations/prove/websearch/{topic}-websearch-{date}.md   | [ ]     | —             |
| 3     | prove-intelligence | simulations/prove/intelligence/{topic}-intelligence-{date}.md | [ ] | —             |
| 4     | prove-analysis     | simulations/prove/analysis/{topic}-analysis-{date}.md     | [ ]     | —             |
| 5     | prove-synthesize   | simulations/prove/synthesize/{topic}-synthesize-{date}.md | [ ]     | —             |

Rule: Mark the Written cell [X] and fill Verdict token before beginning the next row's stage.
      A blank Written cell when a later stage is in progress is a campaign failure.

---

## Scout Signal Load

Check for prior scout artifacts: simulations/scout/**/{topic}-*.md

Scout record:
  | Artifact slug | Key finding |
  |--------------|-------------|
  | [slug]       | [finding]   |

  If none: "No scout artifacts found."

---

## Stage 1 — prove-hypothesis

Scout anchor: [Slug and one-sentence finding from Scout Signal Load, or "no prior signals".]

  Claim: [One sentence. "is" or "will". No hedging.]
  Status quo: [What the team does today. One sentence.]
  F-00: Hypothesis is false if status quo is sufficient.
    Observable test: [External measurement showing status quo is sufficient.]

  Falsification table:
    | ID   | Falsifying outcome (observable) |
    |------|--------------------------------|
    | F-01 | |
    | F-02 | |

  Confidence: [N]/100
  Rationale: [2-3 sentences. Line 1: scout anchor or absence note. Line 2: status-quo gap. Line 3: confidence basis.]

  Experiment plan:
    | Rank | Experiment | Sub-skill         | F-IDs tested |
    |------|------------|-------------------|--------------|
    | 1    |            | prove-websearch   |              |
    | 2    |            | prove-intelligence|              |

Write artifact. Then update Artifact Manifest row 1: Written = [X], Verdict token = claim summary (10 words).

---

## Stage 2 — prove-websearch

Hypothesis (verbatim from Stage 1 Claim): [carry forward]
Status quo (verbatim from Stage 1): [carry forward]

For each search block:
  Query design:
    | # | Query string | Inertia-test? (yes/no) |
    |---|-------------|----------------------|

  Evidence table:
    | # | Title | Source URL | Finding | Supports/Contradicts/Neutral | Phase |
    |---|-------|-----------|---------|------------------------------|-------|

  Evidence floor: minimum 2 distinct source URLs per block.
    If only 1 source found — run supplemental search immediately.
    Supplemental query: [string]  |  Source: [title — URL]

Verdict scorecard:
  | Dimension         | Value                           |
  |-------------------|---------------------------------|
  | Verdict token     | SUPPORTS / CONTRADICTS / INCONCLUSIVE |
  | Confidence delta  | +N / -N / 0                     |
  | Signal count      | [N]                             |
  | Inertia signals   | [N present / absent]            |
  | Key signals       | [1-3 slugs]                     |

Write artifact. Then update Artifact Manifest row 2: Written = [X], Verdict token = verdict token value.

---

## Stage 3 — prove-intelligence

Sources to scan (in order):
  1. simulations/scout/**/{topic}-*.md
  2. simulations/trace/**/{topic}-*.md
  3. simulations/review/**/{topic}-*.md
  4. simulations/draft/**/{topic}-*.md

Signal table:
  | # | Source slug | Finding | Phase | Role (P/S) | Inertia |
  |---|-------------|---------|-------|-----------|---------|

Namespace coverage:
  | Namespace | Artifacts found | Gaps |
  |-----------|----------------|------|
  | scout     |                |      |
  | trace     |                |      |
  | review    |                |      |
  | draft     |                |      |

Intelligence verdict:
  Signal count: [N]
  Strongest signal: [slug — finding]
  What internal record cannot establish: [gaps]

Write artifact. Then update Artifact Manifest row 3: Written = [X], Verdict token = signal count + strongest slug.

---

## Stage 4 — prove-analysis

Combined signal inventory (websearch + intelligence):
  | # | Stage source | Finding | Phase | Role | Inertia |
  |---|-------------|---------|-------|------|---------|

Ceiling derivation:
  | Dimension              | Value   |
  |------------------------|---------|
  | Highest phase present  |         |
  | Inertia coverage       | absent / partial / present |
  | Ceiling (from table)   |         |

  Ceiling table:
    | Evidence phase   | Inertia absent | Inertia present |
    |------------------|----------------|-----------------|
    | Explore only     | 25             | 35              |
    | Test reached     | 45             | 60              |
    | Validate reached | 72             | 72              |
    | All phases       | —              | none            |

Pattern finding:
  [1 paragraph. What the combined signal set establishes and where it breaks down.
   Reference specific signal numbers from inventory above.]

Thin-signal flag:
  [ ] All stages returned substantive findings
  [X] Thin evidence — stage(s): [list]. Effect on ceiling: [statement].

Write artifact. Then update Artifact Manifest row 4: Written = [X], Verdict token = ceiling value.

---

## Stage 5 — prove-synthesize

Ceiling (from Stage 4): [N or "none"]
NOT: begin synthesis reasoning before the Ceiling Declaration section appears.

  **Ceiling Declaration**
    Evidence phase coverage: [phases]. Primary signals by phase: [N per phase].
    Inertia coverage: [absent / partial / present]. Confidence ceiling: [N or "none"].

  **Verdict/Confidence**
    [yes / no / maybe]. Confidence: [N] (must not exceed ceiling).
    Drivers up: [signals]. Held down by: [phase gap / inertia absence].

  **Key Evidence**
    Signal 1: [name] — [finding] — outranks because [phase, role, inertia].
    Signal 2: [name] — [finding] — outranks because [phase, role, inertia].
    Signal 3: [name] — [finding] — outranks because [phase, role, inertia].

  **Counter-Evidence**
    [Strongest argument against verdict. Name source + phase + role + inertia.
     Not permitted to omit.]

  **Adoption Boundaries**
    Inertia-present signals tested: [contexts].
    Inertia-absent signals establish: [demand claim boundaries].
    Untested contexts: [list or "none"].

  **Principles**
    [1-3 declarative principles. "X implies Y." Not restatements of verdict.]

  **Handoff**
    ready_for_topic_story: true
    Topic: {topic}
    Confidence verdict: [N — yes/no/maybe]
    Recommended next: /topic:story

Write artifact. Then update Artifact Manifest row 5: Written = [X], Verdict token = verdict + confidence score.

---

## Final Manifest Check

Review the Artifact Manifest table at the top of this output.
All five Written cells must be [X]. All Verdict token cells must be filled.
If any cell is empty — complete the corresponding stage now before closing.

Report: "Campaign complete. 5/5 artifacts written. Manifest closed."
```

---

## V-03 — Axis: Lifecycle Emphasis (boundary markers are the structure, stages are subordinate)

**Variation axis**: Lifecycle emphasis — the skill body is structured around four named phase transitions (LOAD, HYPOTHESIZE, GATHER, SYNTHESIZE) rather than around five numbered skill stages. Stage boundaries are explicit decision points with forward conditions, not sequential section headers.

**Hypothesis**: Naming phase transitions as first-class structural units — rather than naming skills as structural units — reduces skipping risk because the model must cross a named forward condition before the phase boundary, whereas numbered stages can be advanced by counting.

---

```
Topic: {topic}
Date:  {date}

This skill runs a complete evidence campaign. The campaign has four phase transitions.
You may not cross a transition until its forward condition is met.
Each phase produces one or more named artifacts.

---

PHASE TRANSITION: LOAD → HYPOTHESIZE

Forward condition: Scout record for this topic is on file.

  Scan: simulations/scout/**/{topic}-*.md
  If found — record each artifact:
    Slug: [filename]  Finding: [one sentence]  Date: [artifact date]
  If none — write: "No scout record. Proceeding from zero prior signals."

  [ ] Scout record on file (or absence noted). Cross transition.

---

PHASE TRANSITION: HYPOTHESIZE → GATHER

Forward condition: A single falsifiable claim is written, grounded in the scout record,
and at least two domain falsification conditions (F-01, F-02) are present.

  Claim: [One sentence. Present tense. "is" or "will". No hedging.]

  Scout grounding:
    This claim extends / challenges scout finding: [slug + one-sentence finding]
    OR: No prior signals. Claim proceeds from assumption: [state assumption].

  Status quo (inertia framing):
    Current practice: [name it]  Achieves today: [what outcome]
    F-00: hypothesis is false if current practice is sufficient.
    F-00 observable test: [what external measurement would show sufficiency]

  Falsification conditions:
    F-01: [observable outcome falsifying claim]
    F-02: [observable outcome falsifying claim]

  Confidence: [N]/100
  Rationale: [Line 1: scout anchor or absence. Line 2: status-quo gap. Line 3: confidence basis.]

  Experiment plan (ranked by falsification risk):
    Rank 1 — prove-websearch — F-IDs: [list]
    Rank 2 — prove-intelligence — F-IDs: [list]
    Rank 3 (optional) — prove-analysis — F-IDs: [list]

  Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md

  [ ] Artifact written.  [ ] Claim is one sentence.  [ ] F-01 and F-02 present.
  [ ] Scout anchor named (or absence stated). Cross transition.

---

PHASE TRANSITION: GATHER → SYNTHESIZE

Forward condition: Both evidence-gathering stages (websearch and intelligence)
have written artifacts, AND the analysis stage has produced a signal inventory
with a confidence ceiling value.

GATHER has three sub-stages. Complete in order.

### Gather Sub-Stage A — prove-websearch

  Status quo anchor (from HYPOTHESIZE phase): [carry forward current practice + outcome]
  Hypothesis anchor (from HYPOTHESIZE phase): [carry forward claim verbatim]
  Falsification event: [what contrary external result would falsify — anchored to status quo]

  Search block(s):
    Query: [string]
    Evidence:
      | # | Title | URL | Finding | Verdict |
      |---|-------|-----|---------|---------|
    Evidence floor: 2 distinct URLs per block. Supplemental search if fewer found.

  Verdict token: [SUPPORTS / CONTRADICTS / INCONCLUSIVE]
  Confidence delta: [+N / -N / 0]

  Write artifact: simulations/prove/websearch/{topic}-websearch-{date}.md

  [ ] Artifact written.  [ ] Verdict token set.  Proceed to Sub-Stage B.

### Gather Sub-Stage B — prove-intelligence

  Sources scanned:
    | Namespace | Artifacts found | Gaps |
    |-----------|----------------|------|
    | scout     |                |      |
    | trace     |                |      |
    | review    |                |      |
    | draft     |                |      |

  Signal table:
    | # | Slug | Finding | Phase | Role | Inertia |
    |---|------|---------|-------|------|---------|

  Intelligence verdict: [N signals found. Strongest: slug. Gap: what record cannot establish.]

  Write artifact: simulations/prove/intelligence/{topic}-intelligence-{date}.md

  [ ] Artifact written.  [ ] All four namespaces checked.  Proceed to Sub-Stage C.

### Gather Sub-Stage C — prove-analysis

  Combined signal inventory (websearch + intelligence, all signals numbered):
    | # | Stage | Finding | Phase | Role | Inertia |
    |---|-------|---------|-------|------|---------|

  Ceiling derivation:
    Highest phase present: [Explore / Test / Validate / All]
    Inertia coverage: [absent / partial / present]
    Ceiling value: [N or "none"] — read from:
      | Phase         | Inertia absent | Inertia present |
      |---------------|----------------|-----------------|
      | Explore only  | 25             | 35              |
      | Test reached  | 45             | 60              |
      | Validate      | 72             | 72              |
      | All phases    | —              | none            |

  Thin-signal flag: [List any stage that returned zero substantive findings, or "none".]
  Ceiling effect of thin signal: [How does the thin stage affect the ceiling or confidence?]

  Write artifact: simulations/prove/analysis/{topic}-analysis-{date}.md

  [ ] Artifact written.  [ ] Ceiling value recorded.  [ ] Thin-signal flag complete.
  [ ] All three sub-stage artifacts written. Cross GATHER → SYNTHESIZE transition.

---

PHASE TRANSITION: SYNTHESIZE → DONE

Forward condition: prove-synthesize artifact written with ready_for_topic_story: true
in frontmatter. Synthesis contains all seven required sections.

  Ceiling (carry from Sub-Stage C): [N or "none"]
  NOT: write any synthesis reasoning section before the Ceiling Declaration appears.

  **Ceiling Declaration** [MUST appear first]
    Evidence phase coverage: [list]. Primary signals by phase: [N per phase].
    Inertia coverage: [state]. Confidence ceiling: [N or "none"].

  **Verdict/Confidence**
    [yes / no / maybe]. Score: [N]. Not above ceiling.
    Why up: [signals]. Why capped: [gap].

  **Key Evidence**
    Three signals. Each: finding + phase + role + inertia + why it outranks.

  **Counter-Evidence**
    Best argument against verdict. Source + phase + role + inertia. Not permitted to omit.

  **Adoption Boundaries**
    What inertia-present tested. What inertia-absent cannot establish.
    Contexts with no inertia-present signal — name them.

  **Principles**
    1-3 principles. Declarative. "X implies Y." No verdict restatements.

  **Handoff**
    ready_for_topic_story: true
    Topic: {topic}  Confidence: [N]  Verdict: [yes/no/maybe]
    Next skill: /topic:story

  Write artifact: simulations/prove/synthesize/{topic}-synthesize-{date}.md

  [ ] Artifact written.  [ ] All seven sections present.  [ ] ready_for_topic_story: true.

  Cross transition. Campaign complete.

---

Final verification: Five artifacts written. All share {topic}- prefix.
Synthesis is the last artifact written. Campaign closed.
```

---

## V-04 — Combined: Phrasing Register (conversational + imperative) + Inertia Framing (prominent)

**Variation axis (combined)**: Phrasing register — direct second-person imperative throughout, brief headers, no numbered sections — combined with inertia framing made structurally prominent at the campaign level (not just within prove-synthesize). The status-quo competitor anchors every stage from hypothesis through synthesis.

**Hypothesis**: Making inertia framing a campaign-level constraint — rather than a synthesize-only constraint — produces more consistent verdict scoping because the status-quo comparator is named early and carried forward as a reference anchor, reducing late-stage confidence inflation.

---

```
Topic: {topic}
Date:  {date}

Run the full prove campaign. Five skills in order. Write each artifact before starting the next.
The status quo is your anchor throughout. Name it once, carry it everywhere.

---

## Name the status quo first

Before writing anything else, answer: what does the team do today without this capability?

  Current practice: [name it — one phrase or sentence]
  What it achieves: [outcome it delivers today]
  What it cannot achieve: [the gap this topic is meant to close]

This is your campaign anchor. Every stage references it.

---

## Load scout signals

Check simulations/scout/**/{topic}-*.md. List what you find:
  - [slug]: [one-sentence finding]
  - (or: "no prior scout signals")

---

## Stage 1 — Write the hypothesis

Ground the claim in your scout load and your status-quo anchor.

  Scout anchor: [slug + finding, or "no prior signals — proceeding from: [assumption]"]
  Status quo anchor: [current practice from above]

  Claim: One sentence. State what this topic IS or WILL do. No hedging. No "may" or "might".

  It's false if:
    F-00: The current practice is already sufficient. Observable test: [how you'd know]
    F-01: [Observable outcome that disproves the claim]
    F-02: [Another observable outcome that disproves it]

  Confidence: [N]/100
  Why: [1-2 sentences. What's your status-quo gap? What scout signal moves the number?]

  Best experiments to test this:
    1. Web search — tests F-IDs: [list]
    2. Internal scan — tests F-IDs: [list]

Write: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, scout_anchor, status_quo_named: true.

Say "Stage 1 done — hypothesis written" before continuing.

---

## Stage 2 — Web search

You're searching for external evidence on the claim you just wrote.
Keep the status quo in view: you're looking for evidence that the alternative beats it — or doesn't.

  Null hypothesis (write it before searching): The status quo is sufficient because: _____.

  For each search:
    Query: [what you searched]
    What you found:
      | Title | URL | Finding | Does it beat the status quo? (yes/no/unclear) |
      |-------|-----|---------|----------------------------------------------|

    Minimum 2 sources per query. If you only found 1, search again immediately.
    Supplemental: [query] → [title — URL]

  After all searches:
    Verdict: [SUPPORTS / CONTRADICTS / INCONCLUSIVE]
    Confidence move: [+N / -N / 0] — because [brief reason]
    Status quo check: [Did external evidence directly compare vs. status quo, or only test in isolation?]

Write: simulations/prove/websearch/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, verdict_token, confidence_delta, inertia_tested (true/false).

Say "Stage 2 done — websearch written" before continuing.

---

## Stage 3 — Internal scan

Scan these internal namespaces for signals on the claim:
  - simulations/scout/**/{topic}-*.md
  - simulations/trace/**/{topic}-*.md
  - simulations/review/**/{topic}-*.md
  - simulations/draft/**/{topic}-*.md

For each signal found:
  | Slug | Finding | Does it reference the status quo? (yes/no) | Phase | Role |
  |------|---------|------------------------------------------|-------|------|

Gaps: [What namespaces returned nothing?]
Status quo coverage: [Did any internal signal directly test against current practice?]

Write: simulations/prove/intelligence/{topic}-intelligence-{date}.md
Frontmatter: skill, topic, date, signal_count, inertia_present_count.

Say "Stage 3 done — intelligence written" before continuing.

---

## Stage 4 — Analyze

Combine everything from Stages 2 and 3. Derive your confidence ceiling.

  All signals:
    | # | From stage | Finding | Phase | Role | Inertia — tests vs. status quo? |
    |---|-----------|---------|-------|------|--------------------------------|

  Ceiling (look up from this table):
    | Phase reached    | No status-quo test | Status-quo tested |
    |------------------|-------------------|-------------------|
    | Explore only     | 25                | 35                |
    | Test reached     | 45                | 60                |
    | Validate reached | 72                | 72                |
    | All phases       | —                 | none              |

  Your ceiling: [N] — because highest phase is [X] and status-quo is [tested/not tested].

  Warning: if ANY stage returned zero substantive findings, name it now.
    Thin stages: [list or "none"]. Effect on your verdict: [statement].

  Note on status-quo coverage: [What did your evidence set actually test against? Adoption
    prediction (vs. status quo) or demand prediction (interest absent comparator)?]

Write: simulations/prove/analysis/{topic}-analysis-{date}.md
Frontmatter: skill, topic, date, ceiling_value, inertia_coverage, thin_signal_stages.

Say "Stage 4 done — analysis written" before continuing.

---

## Stage 5 — Synthesize

Write the final brief. Take a position. Do not summarize — decide.

Start with the Ceiling Declaration. Do not write any verdict before this section appears.

  **Ceiling Declaration**
    Evidence phase coverage: [phases]. Primary signals by phase: [N per phase].
    Inertia coverage (status-quo testing): [absent / partial / present].
    Confidence ceiling: [N or "none"].

  **Verdict/Confidence**
    One word first: yes, no, or maybe.
    Confidence: [N]. Not above ceiling.
    What drove the number up: [signals, named].
    What capped it: [phase gap / no status-quo test / thin evidence].

  **Key Evidence**
    Three signals that most shaped your verdict.
    For each: what it found, why it matters more than the others.
    Name phase, role, and whether it tested against the status quo.

  **Counter-Evidence**
    What's the strongest argument you're wrong? Name it — signal, phase, role.
    Do not skip this section.

  **Adoption Boundaries**
    What contexts did status-quo-testing signals actually cover?
    What can the status-quo-absent signals predict (demand only, not adoption)?
    What contexts are untested?

  **Principles**
    1-3 things that generalize beyond this hypothesis.
    "X implies Y." No verdict restatements.

  **Handoff**
    ready_for_topic_story: true
    Topic: {topic}
    Confidence: [N] — [yes/no/maybe]
    Next: /topic:story

Write: simulations/prove/synthesize/{topic}-synthesize-{date}.md
Frontmatter: skill, topic, date, verdict, confidence, ready_for_topic_story: true,
             stages_completed: [hypothesis, websearch, intelligence, analysis, synthesize].

Say "Campaign complete — 5 artifacts written" and list all five artifact paths.

---

## Final check

Five files written. All start with {topic}-. Synthesis is the last one.
Synthesis contains ready_for_topic_story: true.
If not — fix it before closing.
```

---

## V-05 — Combined: Output Format (prose-first narrative) + Lifecycle Emphasis (stages as chapters, no checklists)

**Variation axis (combined)**: Output format — prose-forward, no standalone tables or checkbox lists, each stage reads as a narrative chapter with embedded structure — combined with lifecycle emphasis that puts stage transitions entirely in prose headers. No checkbox gates. The stage boundary is the paragraph break.

**Hypothesis**: Eliminating checkbox gates in favor of narrative stage headers produces more coherent synthesis reasoning because prose-forward stages require the model to hold prior context in running text rather than re-reading discrete filled cells, reducing context fragmentation across stages.

---

```
Topic: {topic}
Date:  {date}

You are running the full evidence campaign for this topic. The campaign has five stages.
Complete them in order. Write an artifact at the end of each stage before continuing.
Every artifact uses the prefix {topic}-.

---

## Opening: Load the signal record

Before writing anything, read what is already known about this topic.

Search simulations/scout/**/{topic}-*.md and read any artifacts you find. Then write a
brief summary — one paragraph, two to four sentences — of what prior scouting established
for this topic. If no scout artifacts exist, note this in one sentence and proceed.

This summary is your standing context for the campaign. Reference it in the stages that follow.

---

## Stage 1 — prove-hypothesis: Frame the claim

Open this stage by naming what the team currently does without this capability. Write one
sentence describing current practice and what it achieves. Then write one sentence describing
the specific gap that this topic is meant to close. This status-quo framing is your baseline;
the hypothesis is the alternative.

Write the claim in one declarative sentence. Use "is" or "will". State what this topic
achieves, not what it might or should achieve.

After the claim, write the status-quo falsification condition (F-00): the hypothesis is false
if current practice turns out to be sufficient. Make F-00 externally observable. Then write
two domain falsification conditions (F-01, F-02): specific, externally observable outcomes
that would disprove the claim independent of the status quo.

Close the stage with a confidence score from 0 to 100, followed by two to three sentences
explaining it. The explanation must reference (a) the scout summary you wrote in the Opening
and (b) the status-quo gap you named at the start of this stage.

End this stage by writing the hypothesis artifact and confirming it exists:
  Path: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  Frontmatter includes: skill, topic, date, claim_summary, confidence, scout_anchor (slug or "none"),
  status_quo_verdict (INSUFFICIENT/SUFFICIENT), f_id_count.

---

## Stage 2 — prove-websearch: Gather external evidence

Open this stage by restating the claim verbatim from Stage 1 and the status-quo baseline.
Then write the null hypothesis in one sentence: the status quo is sufficient because _____.
This framing anchors what external evidence must overcome.

Run searches designed to test whether the claim holds against external sources. For each
search, write the query string and then describe what you found in two to three sentences.
Name specific sources. Note whether each source directly compared the topic's approach against
current practice, or whether it tested the approach in isolation.

You must find at least two distinct sources per search. If a search returns only one source,
run an additional targeted query immediately and incorporate the result before continuing.

After all searches, write a verdict paragraph of three to five sentences: whether the
external evidence supports, contradicts, or is inconclusive on the claim; what confidence
adjustment the external evidence warrants; and whether any source tested directly against
the status quo or only in the absence of a comparator.

End this stage by writing the websearch artifact and confirming it exists:
  Path: simulations/prove/websearch/{topic}-websearch-{date}.md
  Frontmatter includes: skill, topic, date, verdict_token, confidence_delta, source_count,
  inertia_tested (true/false).

---

## Stage 3 — prove-intelligence: Scan the internal record

Open this stage by stating which internal namespaces you will scan and why each is relevant
to the claim from Stage 1.

Scan each of these locations in order:
  simulations/scout/**/{topic}-*.md
  simulations/trace/**/{topic}-*.md
  simulations/review/**/{topic}-*.md
  simulations/draft/**/{topic}-*.md

For each namespace, write one paragraph describing what you found and what it contributes to
the claim. If a namespace has no artifacts, note this in one sentence. Do not treat an empty
namespace as equivalent to a namespace with disconfirming evidence — absence and
disconfirmation are different.

After all namespaces, write a summary paragraph: how many signals total, which signal is
strongest and why, and what the internal record cannot establish about the claim.

End this stage by writing the intelligence artifact and confirming it exists:
  Path: simulations/prove/intelligence/{topic}-intelligence-{date}.md
  Frontmatter includes: skill, topic, date, signal_count, primary_count, inertia_present_count,
  gaps_identified.

---

## Stage 4 — prove-analysis: Read the ceiling

Open this stage by writing the combined signal inventory as a prose-embedded enumeration.
List every signal from Stages 2 and 3 by name, one per line, noting its evidence phase
(Explore / Test / Validate), its role (Primary / Supporting), and whether it tests against
the status quo (inertia-present) or in the absence of a comparator (inertia-absent).

Then derive the confidence ceiling. Write the highest evidence phase present across all
signals. Write the inertia coverage state (absent if no inertia-present signal, partial if
some, present if majority). Read the ceiling from the intersection:

  Explore-only + inertia-absent: 25. Explore-only + inertia-present: 35.
  Test-reached + inertia-absent: 45. Test-reached + inertia-present: 60.
  Validate-reached + inertia-any: 72. All-phases + inertia-present: no ceiling.

State the ceiling in one sentence. Then write a paragraph explaining what the ceiling
means for this campaign: which stages determined the phase level, which signals determined
the inertia state, and what evidence would be required to raise the ceiling.

If any evidence stage (websearch or intelligence) returned zero substantive findings, write
a paragraph explicitly naming the gap and describing how it affects the ceiling and any
downstream confidence claims. Do not proceed to Stage 5 if this paragraph is absent and a
thin stage exists.

End this stage by writing the analysis artifact and confirming it exists:
  Path: simulations/prove/analysis/{topic}-analysis-{date}.md
  Frontmatter includes: skill, topic, date, ceiling_value, inertia_coverage,
  highest_phase, thin_signal_stages (list or "none").

---

## Stage 5 — prove-synthesize: Write the brief

This is the terminal artifact. Write it as a document that takes a position on the claim.
Do not summarize the prior stages — interpret them and reach a verdict.

Begin with the Ceiling Declaration as the first named section. Do not write any verdict
reasoning before this section is complete:

  Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase].
  Inertia coverage: [absent / partial / present]. Confidence ceiling: [N or "none"].

Then write the remaining six sections in order. Each section is a prose paragraph or short
set of prose paragraphs under the named header — no bullets, no standalone tables.

  Verdict/Confidence — Open with yes, no, or maybe. Give the confidence score. Explain
  in three to four sentences which signals drove the score up and what held it to the ceiling.

  Key Evidence — Describe the three signals that most shaped the verdict. For each, write
  two sentences: what the signal found and why it ranks above the others. Name phase, role,
  and inertia classification as part of the argument, not as metadata tags.

  Counter-Evidence — Write the strongest case against your verdict. Name a specific signal
  or structural gap, with its phase, role, and inertia classification. Do not skip this
  section. Omission is a campaign failure.

  Adoption Boundaries — Write two to three sentences on each of the following:
  (1) what inertia-present signals tested directly; (2) what inertia-absent signals can
  predict (demand signals, not adoption predictions); (3) which contexts the campaign
  produced no inertia-present evidence for, and what that absence means for the verdict scope.
  If no inertia-present signal exists, open with: "No status-quo comparison signal present.
  The verdict is a demand claim, not an adoption prediction."

  Principles — State one to three principles that generalize beyond this hypothesis.
  Write each as a declarative sentence: "X implies Y." They may not restate the verdict.

  Handoff — Close the synthesis with:
    ready_for_topic_story: true
    Topic: {topic}
    Confidence verdict: [N — yes/no/maybe]
    Recommended next skill: /topic:story

End this stage by writing the synthesis artifact and confirming it exists:
  Path: simulations/prove/synthesize/{topic}-synthesize-{date}.md
  Frontmatter includes: skill, topic, date, verdict (yes/no/maybe), confidence,
  ceiling_applied, ready_for_topic_story: true,
  stages_completed: [hypothesis, websearch, intelligence, analysis, synthesize].

---

## Closing

All five stages complete. All five artifacts written. All share the {topic}- prefix.
The synthesis is the last artifact written and contains ready_for_topic_story: true.

List the five artifact paths to confirm the campaign record is complete.
```
