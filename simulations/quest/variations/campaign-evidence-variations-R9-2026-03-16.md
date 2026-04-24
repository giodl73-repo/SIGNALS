## Quest Variate — campaign-evidence (Round 9)

Five single-axis variations, then one combination. Each is a complete, runnable prompt body.

---

## V-01 — Role Sequence Axis

**Variation axis**: Stage ordering and handoff framing  
**Hypothesis**: Making each stage a named handoff with an explicit "role passes to…" transition prevents hypothesis pre-commitment because the executor cannot open the hypothesis stage without seeing the evidence-receiver role named — the sequence becomes a social contract between named actors, not a structural convention.

```markdown
You are running the full evidence campaign for the topic provided by the user.

The campaign has five named stages executed in strict role-handoff order:

  Stage 1 — Web Researcher        (prove-websearch)
  Stage 2 — Intelligence Analyst  (prove-intelligence)
  Stage 3 — Hypothesis Architect  (prove-hypothesis)
  Stage 4 — Evidence Analyst      (prove-analysis)
  Stage 5 — Synthesis Director    (prove-synthesize)

Role passes left-to-right. No role may begin until the preceding role has closed its output.

---

## GOVERNANCE PREAMBLE

Four rules govern this campaign. All four are peers — none is primary.

ATTRIBUTION RULE [invoked at: Stage 1, Stage 2, Stage 4, Stage 5]
Every material claim must carry a stage-source tag: (S1), (S2), (S3), (S4), or (S5).
At least 70% of material claims in the final brief must carry an attribution tag.

SEQUENCING RULE [invoked at: Stage 3, Stage 4, Stage 5]
Hypotheses may be declared only after Stage 1 and Stage 2 have closed their outputs.
A hypothesis anchored before evidence gathering is a bias, not a hypothesis.
Machine-verifiable enforcement: the evidence table carries a Stage column (S1/S2/S3/S4/S5);
any hypothesis row may reference only S1 or S2 source rows.

FALSIFICATION RULE [invoked at: Stage 3, Stage 5]
Every hypothesis carries an explicit falsification condition — a stated criterion that would
cause the hypothesis to be rejected. A hypothesis without a falsification condition is
a statement of belief, not a testable claim.

CALIBRATION RULE [invoked at: Stage 4, Stage 5]
Confidence ratings must span at least two distinct levels across findings.
A brief where every finding carries the same confidence rating fails calibration.
Anti-pattern guard: before closing Stage 5, confirm that at least two distinct levels appear.

Rule count: 4. Coverage map row count = 4 × applicable-stages (derived, not hardcoded).
Adding a peer rule automatically extends the row count without requiring edits to static integers.

---

## PRE-DECLARED COVERAGE MAP (immutable after this point)

| Rule | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|------|---------|---------|---------|---------|---------|
| ATTRIBUTION  | ✓ | ✓ | — | ✓ | ✓ |
| SEQUENCING   | — | — | ✓ | ✓ | ✓ |
| FALSIFICATION| — | — | ✓ | — | ✓ |
| CALIBRATION  | — | — | — | ✓ | ✓ |

This map is finalized before Stage 1 begins and cannot be modified after any stage executes.
Applicable-stage count per rule: ATTRIBUTION=4, SEQUENCING=3, FALSIFICATION=2, CALIBRATION=2.
Total audit rows = 11.

---

## PRE-TEMPLATED GATE RECORD (blank — fill as each stage closes)

| Stage | Role | Entry Gate | Exit Gate |
|-------|------|-----------|-----------|
| 1 | Web Researcher | Topic received | Web findings documented |
| 2 | Intelligence Analyst | S1 output present | Intelligence synthesis documented |
| 3 | Hypothesis Architect | S1 + S2 output present | Hypotheses + falsification conditions declared |
| 4 | Evidence Analyst | S3 hypotheses present | Per-hypothesis evidence table complete |
| 5 | Synthesis Director | S4 analysis complete | Final brief with verdict produced |

| Stage | Entry Pass/Fail | Exit Pass/Fail |
|-------|----------------|----------------|
| 1     |                |                |
| 2     |                |                |
| 3     |                |                |
| 4     |                |                |
| 5     |                |                |

---

## STAGE EXECUTION

### Stage 1 — Web Researcher [Stage 1 of 5]

Entry condition: User has provided the investigation topic.
Exit condition: Web findings documented with source attribution.

Execute prove-websearch for the topic. Gather primary web evidence.
Tag every material claim: (S1).

ATTRIBUTION RULE invoked [Stage 1 of 5]: Are at least 70% of Stage 1 claims tagged (S1)? [ Yes / No ]
SEQUENCING RULE invoked [Stage 1 of 5]: No — this is an evidence stage; sequencing rule does not apply here.

Gate 1 entry: [ Pass / Fail ]
Gate 1 exit: [ Pass / Fail ]

Role passes to: Stage 2 — Intelligence Analyst.

---

### Stage 2 — Intelligence Analyst [Stage 2 of 5]

Entry condition: Stage 1 web findings present.
Exit condition: Intelligence synthesis documented with source attribution.

Execute prove-intelligence. Review industry signals, expert perspectives, and prior art.
Tag every material claim: (S2).

ATTRIBUTION RULE invoked [Stage 2 of 5]: Are at least 70% of Stage 2 claims tagged (S2)? [ Yes / No ]

Gate 2 entry: [ Pass / Fail ]
Gate 2 exit: [ Pass / Fail ]

Role passes to: Stage 3 — Hypothesis Architect.

---

### Stage 3 — Hypothesis Architect [Stage 3 of 5]

Entry condition: Stage 1 AND Stage 2 outputs both present.
Exit condition: Each hypothesis carries a falsification condition.

Execute prove-hypothesis. Declare hypotheses grounded in S1/S2 evidence.
Evidence table: include a Stage column — each hypothesis row references only S1 or S2 source rows.

SEQUENCING RULE invoked [Stage 3 of 5]: Do all hypothesis rows reference only S1/S2 stage values? [ Yes / No ]
FALSIFICATION RULE invoked [Stage 3 of 5]: Does every hypothesis carry an explicit falsification condition? [ Yes / No ]

Gate 3 entry: [ Pass / Fail ]
Gate 3 exit: [ Pass / Fail ]

Role passes to: Stage 4 — Evidence Analyst.

---

### Stage 4 — Evidence Analyst [Stage 4 of 5]

Entry condition: Stage 3 hypotheses with falsification conditions present.
Exit condition: Per-hypothesis evidence table with confidence ratings populated.

Execute prove-analysis. For each hypothesis, evaluate evidence and assign a confidence level.
Include stage column in evidence table (S1/S2/S3/S4).

ATTRIBUTION RULE invoked [Stage 4 of 5]: Are material claims tagged with stage source? [ Yes / No ]
SEQUENCING RULE invoked [Stage 4 of 5]: Does the stage column confirm no hypothesis row precedes evidence rows? [ Yes / No ]
CALIBRATION RULE invoked [Stage 4 of 5]: Do confidence ratings span at least two distinct levels so far? [ Yes / No ]

Gate 4 entry: [ Pass / Fail ]
Gate 4 exit: [ Pass / Fail ]

Role passes to: Stage 5 — Synthesis Director.

---

### Stage 5 — Synthesis Director [Stage 5 of 5]

Entry condition: Stage 4 analysis complete.
Exit condition: Final brief with decision verdict and consolidated audit table produced.

Execute prove-synthesize. Distinguish consensus from conflict between S1 and S2.
Surface gaps and open questions. Issue a single decision-readiness verdict sentence.

ATTRIBUTION RULE invoked [Stage 5 of 5]: Does synthesis attribute consensus/conflict findings to S1 and S2? [ Yes / No ]
SEQUENCING RULE invoked [Stage 5 of 5]: Does final brief confirm evidence preceded hypothesis declaration throughout? [ Yes / No ]
FALSIFICATION RULE invoked [Stage 5 of 5]: Are falsification outcomes stated for each hypothesis? [ Yes / No ]
CALIBRATION RULE invoked [Stage 5 of 5]: Do final confidence ratings span at least two distinct levels? [ Yes / No ]
Anti-pattern guard: if every finding carries the same confidence level, calibration has failed — revise before closing.

Gate 5 entry: [ Pass / Fail ]
Gate 5 exit: [ Pass / Fail ]

---

## FINAL OUTPUT BRIEF

Produce a single self-contained document containing:

1. **Title and topic context**
2. **Findings** — S1 and S2 findings with stage attribution
3. **Hypotheses** — each with falsification condition and outcome
4. **Analysis** — evidence table with Stage column, confidence levels
5. **Synthesis** — consensus vs conflict, S1/S2 distinguished explicitly
6. **Gaps and open questions** — what remains unknown
7. **Decision readiness** — one sentence: posture + blocking gap if not ready
8. **Gate Record** — filled table from the pre-template above
9. **Consolidated Invocation Audit Table**

### Consolidated Invocation Audit Table

| Rule | Stage | Stage Index | Form | Pass/Fail |
|------|-------|-------------|------|-----------|
| ATTRIBUTION | Stage 1 | 1 of 5 | Binary | |
| ATTRIBUTION | Stage 2 | 2 of 5 | Binary | |
| ATTRIBUTION | Stage 4 | 4 of 5 | Binary | |
| ATTRIBUTION | Stage 5 | 5 of 5 | Binary | |
| SEQUENCING | Stage 3 | 3 of 5 | Binary | |
| SEQUENCING | Stage 4 | 4 of 5 | Binary | |
| SEQUENCING | Stage 5 | 5 of 5 | Binary | |
| FALSIFICATION | Stage 3 | 3 of 5 | Binary | |
| FALSIFICATION | Stage 5 | 5 of 5 | Binary | |
| CALIBRATION | Stage 4 | 4 of 5 | Binary | |
| CALIBRATION | Stage 5 | 5 of 5 | Binary | |

Row count: 11 (derived from coverage map: ATTRIBUTION×4 + SEQUENCING×3 + FALSIFICATION×2 + CALIBRATION×2).
```

---

## V-02 — Output Format Axis

**Variation axis**: Table-first output format with machine-verifiable stage columns  
**Hypothesis**: Structuring the entire brief as a set of typed tables with a mandatory Stage column converts sequencing compliance from a prose assertion into a sort-verifiable property — any row out of order is detectable without interpretation.

```markdown
You are running campaign-evidence for the topic the user provides.

The output is a structured brief built from typed tables. Narrative is permitted only in
the Synthesis and Decision sections. Every evidence, hypothesis, and analysis row carries
a Stage column value (S1–S5) enabling sort-based sequencing verification.

---

## GOVERNANCE PREAMBLE

Four peer governance rules. No rule is primary. All four are declared at the same tier.
Adding a fifth rule does not require editing any static count — the audit table row count
is computed as Σ(applicable stages per rule), recalculated automatically.

ATTRIBUTION RULE [invoked at: S1, S2, S4, S5]
Tag every material claim with its stage of origin. ≥70% coverage required.
Inline scope: applicable at every evidence-gathering stage.

SEQUENCING RULE [invoked at: S3, S4, S5]
Hypotheses declared after S1 and S2 close. A hypothesis anchored before evidence is a bias.
Machine enforcement: Stage column in evidence table — hypothesis rows may cite only S1/S2 values.
Inline scope: applicable at every stage that may produce or reference hypothesis rows.

FALSIFICATION RULE [invoked at: S3, S5]
Every hypothesis row carries a Falsification Condition column.
Inline scope: applicable at hypothesis declaration and final audit.

CALIBRATION RULE [invoked at: S4, S5]
Confidence column must contain at least two distinct values across rows.
Anti-uniformity guard: a table where every row shows the same confidence level fails.
Inline scope: applicable at analysis and synthesis.

---

## PRE-DECLARED COVERAGE MAP

Finalized before Stage 1. Immutable — cannot be modified after execution begins.

| Rule | S1 | S2 | S3 | S4 | S5 | Applicable Count |
|------|----|----|----|----|----|-----------------|
| ATTRIBUTION   | ✓ | ✓ | — | ✓ | ✓ | 4 |
| SEQUENCING    | — | — | ✓ | ✓ | ✓ | 3 |
| FALSIFICATION | — | — | ✓ | — | ✓ | 2 |
| CALIBRATION   | — | — | — | ✓ | ✓ | 2 |
| **Audit rows** | | | | | | **11** |

---

## PRE-TEMPLATED GATE RECORD

| Stage | Entry Condition | Exit Condition | Entry | Exit |
|-------|----------------|----------------|-------|------|
| S1 | Topic received | Web findings table populated | | |
| S2 | S1 table present | Intelligence findings table populated | | |
| S3 | S1+S2 tables present | Hypothesis table with falsification column populated | | |
| S4 | S3 hypothesis table present | Analysis table with Stage + Confidence columns populated | | |
| S5 | S4 analysis table present | Final brief sections complete | | |

---

## STAGE EXECUTION

### Stage S1 — prove-websearch [Stage 1 of 5]

Entry: [ Pass / Fail ] — topic received?
Run prove-websearch. Populate the Web Findings Table.

**Web Findings Table**

| # | Finding | Source | Stage |
|---|---------|--------|-------|
| 1 | | | S1 |
| … | | | S1 |

ATTRIBUTION RULE [Stage 1 of 5]: Are ≥70% of rows tagged S1? [ Yes / No ]
Exit: [ Pass / Fail ] — table populated?

---

### Stage S2 — prove-intelligence [Stage 2 of 5]

Entry: [ Pass / Fail ] — S1 table present?
Run prove-intelligence. Populate the Intelligence Findings Table.

**Intelligence Findings Table**

| # | Finding | Source | Stage |
|---|---------|--------|-------|
| 1 | | | S2 |
| … | | | S2 |

ATTRIBUTION RULE [Stage 2 of 5]: Are ≥70% of rows tagged S2? [ Yes / No ]
Exit: [ Pass / Fail ] — table populated?

---

### Stage S3 — prove-hypothesis [Stage 3 of 5]

Entry: [ Pass / Fail ] — S1 AND S2 tables both present?
Run prove-hypothesis. Declare hypotheses grounded in S1/S2 rows only.

**Hypothesis Table**

| # | Hypothesis | Evidence Row(s) | Evidence Stage | Falsification Condition | Stage |
|---|-----------|-----------------|----------------|------------------------|-------|
| H1 | | (row #, S1 or S2) | S1/S2 only | | S3 |
| … | | | | | S3 |

SEQUENCING RULE [Stage 3 of 5]: Do all Evidence Stage cells contain only S1 or S2? [ Yes / No ]
FALSIFICATION RULE [Stage 3 of 5]: Does every hypothesis row carry a non-empty Falsification Condition? [ Yes / No ]
Exit: [ Pass / Fail ] — hypothesis table with falsification column complete?

---

### Stage S4 — prove-analysis [Stage 4 of 5]

Entry: [ Pass / Fail ] — S3 hypothesis table present?
Run prove-analysis. Evaluate each hypothesis against accumulated evidence.

**Analysis Table**

| H# | Hypothesis | Supporting Evidence | Contradicting Evidence | Confidence | Falsified? | Stage |
|----|-----------|--------------------|-----------------------|------------|-----------|-------|
| H1 | | (S1/S2 refs) | (S1/S2/S3 refs) | High/Med/Low | Y/N | S4 |
| … | | | | | | S4 |

ATTRIBUTION RULE [Stage 4 of 5]: Do evidence reference cells cite stage-tagged rows? [ Yes / No ]
SEQUENCING RULE [Stage 4 of 5]: Does sort on Stage column confirm no analysis precedes its evidence source? [ Yes / No ]
CALIBRATION RULE [Stage 4 of 5]: Does the Confidence column contain at least two distinct values? [ Yes / No ]
Exit: [ Pass / Fail ] — analysis table with Confidence column complete?

---

### Stage S5 — prove-synthesize [Stage 5 of 5]

Entry: [ Pass / Fail ] — S4 analysis table present?
Run prove-synthesize. Produce narrative Synthesis and Decision sections.

ATTRIBUTION RULE [Stage 5 of 5]: Does synthesis narrative attribute consensus/conflict findings to S1/S2 explicitly? [ Yes / No ]
SEQUENCING RULE [Stage 5 of 5]: Does the stage column audit confirm no hypothesis row preceded its evidence rows? [ Yes / No ]
FALSIFICATION RULE [Stage 5 of 5]: Does every H# row in Analysis Table have a Falsified? value? [ Yes / No ]
CALIBRATION RULE [Stage 5 of 5]: Does the Confidence column span ≥2 distinct levels across all rows? [ Yes / No ]
Exit: [ Pass / Fail ] — final brief complete?

---

## FINAL OUTPUT BRIEF

Assemble all tables plus the following narrative sections:

**Synthesis** (prose permitted)
State where S1 and S2 agree and where they diverge. Do not list findings side-by-side — name the conflict or the consensus explicitly.

**Gaps and Open Questions**
Bulleted list of what remains unknown after the full campaign.

**Decision Readiness**
One sentence. Format: "[Posture]: [reason / blocking gap]."
Examples: "Ready to proceed: evidence across S1 and S2 converges on core claim."
          "Needs more investigation: regulatory timeline data absent from both S1 and S2."

**Gate Record** — filled table from preamble template.

**Consolidated Invocation Audit Table**

| Rule | Stage | Stage Index | Form | Pass/Fail |
|------|-------|-------------|------|-----------|
| ATTRIBUTION | S1 | 1 of 5 | Binary | |
| ATTRIBUTION | S2 | 2 of 5 | Binary | |
| ATTRIBUTION | S4 | 4 of 5 | Binary | |
| ATTRIBUTION | S5 | 5 of 5 | Binary | |
| SEQUENCING | S3 | 3 of 5 | Binary | |
| SEQUENCING | S4 | 4 of 5 | Binary | |
| SEQUENCING | S5 | 5 of 5 | Binary | |
| FALSIFICATION | S3 | 3 of 5 | Binary | |
| FALSIFICATION | S5 | 5 of 5 | Binary | |
| CALIBRATION | S4 | 4 of 5 | Binary | |
| CALIBRATION | S5 | 5 of 5 | Binary | |

Row count = 11 (derived from coverage map; recalculates if a peer rule is added).
```

---

## V-03 — Lifecycle Emphasis Axis

**Variation axis**: Gate conditions as the load-bearing structural element  
**Hypothesis**: When entry/exit gates are the *primary* structure and stages hang from them (rather than gates being annotations on stages), C-24/C-25/C-27 compliance becomes mechanically inevitable — the executor is filling a pre-existing form, not remembering to add gate notation.

```markdown
You are running campaign-evidence for the topic the user provides.

This prompt is structured as a sequence of gates. Each gate has an entry condition,
a work block, and an exit condition. Stages are the work that happens between gates.
The gate record is the primary document; the stage outputs are its evidence.

---

## GOVERNANCE PREAMBLE

Four peer governance rules. All four occupy the same structural tier.

ATTRIBUTION RULE [invoked at: Gate 1→2, Gate 2→3, Gate 4→5, Gate 5→close]
At least 70% of material claims carry a stage-source tag: (S1), (S2), (S4), or (S5).

SEQUENCING RULE [invoked at: Gate 2→3, Gate 3→4, Gate 4→5]
Hypotheses are declared only after Gate 1→2 and Gate 2→3 produce closed evidence outputs.
A hypothesis anchored before evidence is a bias, not a hypothesis.
Machine verification: stage column in evidence table; hypothesis rows reference S1/S2 only.

FALSIFICATION RULE [invoked at: Gate 2→3, Gate 5→close]
Every hypothesis carries an explicit falsification condition.

CALIBRATION RULE [invoked at: Gate 3→4, Gate 5→close]
Confidence ratings span at least two distinct levels. Anti-uniformity guard enforced.

Rule count: 4. Audit rows = 11 (ATTRIBUTION×4 + SEQUENCING×3 + FALSIFICATION×2 + CALIBRATION×2).
Adding a peer rule recalculates the count automatically — no static integers to update.

---

## PRE-DECLARED COVERAGE MAP (immutable from this point)

| Rule | Gate 1→2 | Gate 2→3 | Gate 3→4 | Gate 4→5 | Gate 5→close |
|------|---------|---------|---------|---------|-------------|
| ATTRIBUTION   | ✓ | ✓ | — | ✓ | ✓ |
| SEQUENCING    | — | ✓ | ✓ | ✓ | — |
| FALSIFICATION | — | ✓ | — | — | ✓ |
| CALIBRATION   | — | — | ✓ | — | ✓ |

---

## PRE-TEMPLATED GATE RECORD

| Gate | Entry Condition | Exit Condition | Entry | Exit |
|------|----------------|----------------|-------|------|
| OPEN → 1 | Topic received | — | | |
| 1 → 2 | Topic present | Web findings documented | | |
| 2 → 3 | Web + Intel findings present | — | | |
| 3 → 4 | S1+S2 closed | Hypotheses + falsification conditions declared | | |
| 4 → 5 | Hypotheses present | Analysis table with confidence ratings complete | | |
| 5 → CLOSE | Analysis complete | Final brief with verdict, gate record, audit table | | |

---

## GATE EXECUTION

### OPEN → Gate 1

Entry check: Has the user provided the investigation topic?
OPEN entry: [ Pass / Fail ]

---

### Gate 1 → Gate 2: prove-websearch [Stage 1 of 5]

**Work**: Run prove-websearch. Gather web evidence for the topic.
Tag all material claims (S1).

ATTRIBUTION RULE invoked [Gate 1→2, Stage 1 of 5]: Are ≥70% of web claims tagged (S1)? [ Yes / No ]

Gate 1→2 exit: Web findings documented? [ Pass / Fail ]

---

### Gate 2 → Gate 3: prove-intelligence [Stage 2 of 5]

Entry check: Gate 1→2 exit status?
Gate 2→3 entry: [ Pass / Fail ]

**Work**: Run prove-intelligence. Gather industry signals and expert perspectives.
Tag all material claims (S2).

ATTRIBUTION RULE invoked [Gate 2→3, Stage 2 of 5]: Are ≥70% of intelligence claims tagged (S2)? [ Yes / No ]
SEQUENCING RULE invoked [Gate 2→3, Stage 2 of 5]: Are S1 findings present before S2 work begins? [ Yes / No ]
FALSIFICATION RULE invoked [Gate 2→3, Stage 2 of 5]: No hypotheses declared yet — sequencing intact? [ Yes / No ]

Gate 2→3 exit: Intelligence findings documented? [ Pass / Fail ]

---

### Gate 3 → Gate 4: prove-hypothesis [Stage 3 of 5]

Entry check: Gate 1→2 AND Gate 2→3 both closed?
Gate 3→4 entry: [ Pass / Fail ]

**Work**: Run prove-hypothesis. Declare hypotheses grounded in S1/S2 evidence only.
For each hypothesis: state the falsification condition.
Evidence table: Stage column required — hypothesis rows may reference S1/S2 only.

| # | Hypothesis | Evidence Source | Evidence Stage | Falsification Condition |
|---|-----------|-----------------|----------------|------------------------|
| H1 | | | S1 or S2 only | |

SEQUENCING RULE invoked [Gate 3→4, Stage 3 of 5]: Do all Evidence Stage cells contain only S1 or S2? [ Yes / No ]
FALSIFICATION RULE invoked [Gate 3→4, Stage 3 of 5]: Does every hypothesis row carry a falsification condition? [ Yes / No ]
CALIBRATION RULE invoked [Gate 3→4, Stage 3 of 5]: No confidence ratings yet — calibration check deferred to Gate 4→5. [ Deferred ]

Gate 3→4 exit: Hypothesis table with falsification column complete? [ Pass / Fail ]

---

### Gate 4 → Gate 5: prove-analysis [Stage 4 of 5]

Entry check: Gate 3→4 closed?
Gate 4→5 entry: [ Pass / Fail ]

**Work**: Run prove-analysis. Evaluate each hypothesis against accumulated evidence.
Assign a confidence level (High / Medium / Low) to each hypothesis.

| H# | Hypothesis | Supporting | Contradicting | Confidence | Falsified? | Stage |
|----|-----------|-----------|--------------|------------|-----------|-------|
| H1 | | | | | | S4 |

ATTRIBUTION RULE invoked [Gate 4→5, Stage 4 of 5]: Do evidence references cite stage-tagged sources? [ Yes / No ]
SEQUENCING RULE invoked [Gate 4→5, Stage 4 of 5]: Does stage column sort confirm sequencing? [ Yes / No ]
CALIBRATION RULE invoked [Gate 4→5, Stage 4 of 5]: Does the Confidence column contain ≥2 distinct values? [ Yes / No ]

Gate 4→5 exit: Analysis table with confidence ratings complete? [ Pass / Fail ]

---

### Gate 5 → CLOSE: prove-synthesize [Stage 5 of 5]

Entry check: Gate 4→5 closed?
Gate 5→close entry: [ Pass / Fail ]

**Work**: Run prove-synthesize. Synthesize across all stages.

**Synthesis**: State explicitly where S1 and S2 agree and where they diverge.
**Gaps**: List what remains unknown after the full campaign.
**Decision Readiness**: One sentence — posture + blocking gap if not ready.

ATTRIBUTION RULE invoked [Gate 5→close, Stage 5 of 5]: Does synthesis attribute consensus/conflict to named stage sources? [ Yes / No ]
FALSIFICATION RULE invoked [Gate 5→close, Stage 5 of 5]: Are falsification outcomes stated for all hypotheses? [ Yes / No ]
CALIBRATION RULE invoked [Gate 5→close, Stage 5 of 5]: Do final confidence ratings span ≥2 distinct levels? [ Yes / No ]
Anti-pattern guard: if every hypothesis carries the same confidence level, calibration has failed — revise.

Gate 5→close exit: Final brief with verdict, gate record, audit table complete? [ Pass / Fail ]

---

## FINAL OUTPUT BRIEF

Sections:
1. Title and topic context
2. Web Findings (S1 table)
3. Intelligence Findings (S2 table)
4. Hypotheses with falsification conditions (S3 table)
5. Analysis with confidence ratings (S4 table)
6. Synthesis — consensus vs conflict, S1 vs S2 named explicitly
7. Gaps and open questions
8. Decision Readiness — one sentence
9. Gate Record (filled)
10. Consolidated Invocation Audit Table

**Consolidated Invocation Audit Table**

| Rule | Gate | Stage Index | Form | Pass/Fail |
|------|------|-------------|------|-----------|
| ATTRIBUTION | 1→2 | 1 of 5 | Binary | |
| ATTRIBUTION | 2→3 | 2 of 5 | Binary | |
| ATTRIBUTION | 4→5 | 4 of 5 | Binary | |
| ATTRIBUTION | 5→close | 5 of 5 | Binary | |
| SEQUENCING | 2→3 | 2 of 5 | Binary | |
| SEQUENCING | 3→4 | 3 of 5 | Binary | |
| SEQUENCING | 4→5 | 4 of 5 | Binary | |
| FALSIFICATION | 2→3 | 2 of 5 | Binary | |
| FALSIFICATION | 5→close | 5 of 5 | Binary | |
| CALIBRATION | 3→4 | 3 of 5 | Binary | |
| CALIBRATION | 5→close | 5 of 5 | Binary | |

Row count = 11 (derived from coverage map).
```

---

## V-04 — Phrasing Register Axis

**Variation axis**: Conversational / imperative register  
**Hypothesis**: Writing governance rules as active commands ("Do this now. Ask this question.") rather than formal policy declarations reduces the cognitive distance between reading a rule and applying it — the executor hears the rule as an instruction in the moment, not as a policy they must remember to implement.

```markdown
Run the full evidence campaign for the topic the user gives you.

You'll move through five stages. Do them in order. Don't skip ahead.

Here's the rule: you can't write down a hypothesis until you've finished the web search and the intelligence review. If you think of a hypothesis early, write it in a scratch note — don't commit it. A hypothesis written before the evidence is just a guess with a fancy name.

---

## The Four Rules

Before you start, read these four rules. They're all equally important — don't treat any of them as more fundamental than the others.

**ATTRIBUTION RULE** — applies at Stages 1, 2, 4, and 5
When you write a claim, tag where it came from: (S1) for web, (S2) for intelligence, (S3) for hypothesis, (S4) for analysis, (S5) for synthesis. You need to tag at least 70% of material claims. At Stage 5, ask yourself: "Did I actually tag most of my claims, or did I drift?"

**SEQUENCING RULE** — applies at Stages 3, 4, and 5
When you write a hypothesis, it has to be traceable to web or intelligence findings, not to thin air. In your evidence table, include a Stage column — if a hypothesis row references anything later than S2, that's a sequencing violation. Sort the table mentally: does every hypothesis appear after its evidence? If not, reorder.

**FALSIFICATION RULE** — applies at Stages 3 and 5
Every hypothesis needs a falsification condition: a one-sentence statement of what evidence would cause you to reject the hypothesis. No falsification condition = not a hypothesis = don't include it.

**CALIBRATION RULE** — applies at Stages 4 and 5
When you assign confidence levels, make sure you actually have at least two different levels across your findings. If everything comes out Medium, that's not calibration — that's hedging. Ask yourself: "Is my highest-confidence finding genuinely more supported than my lowest? Am I actually distinguishing them?"

---

## Before You Begin: Fill Out These Two Tables

These two tables go in the preamble. Fill them before you run Stage 1.

**Coverage Map** (this is fixed once you start — don't change it)

| Rule | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|------|---------|---------|---------|---------|---------|
| ATTRIBUTION   | ✓ | ✓ | — | ✓ | ✓ |
| SEQUENCING    | — | — | ✓ | ✓ | ✓ |
| FALSIFICATION | — | — | ✓ | — | ✓ |
| CALIBRATION   | — | — | — | ✓ | ✓ |

Total audit rows: 11. If you add a fifth rule later, recalculate from the table — don't update a hardcoded number.

**Gate Record** (fill each row as you complete each stage)

| Stage | What you need going in | What you produce going out | Did you have what you needed? | Did you produce what was required? |
|-------|----------------------|--------------------------|------------------------------|-----------------------------------|
| S1 | The topic | Web findings | | |
| S2 | S1 web findings | Intelligence findings | | |
| S3 | S1 + S2 findings | Hypotheses with falsification conditions | | |
| S4 | S3 hypotheses | Analysis table with confidence ratings | | |
| S5 | S4 analysis | Final brief, decision sentence, audit table | | |

---

## Stage 1 — Web Search [Stage 1 of 5]

What to do: Run prove-websearch on the topic. Write down what you find.

Tag every claim with (S1) as you write it. Don't wait until the end.

Ask yourself now:
- ATTRIBUTION RULE check [Stage 1 of 5]: Did you tag ≥70% of your claims? [ Yes / No ]

Fill in Gate Record row for S1 before moving on.

---

## Stage 2 — Intelligence Review [Stage 2 of 5]

What to do: Run prove-intelligence. Look at industry signals, expert takes, prior art.

Tag every claim with (S2).

Ask yourself now:
- ATTRIBUTION RULE check [Stage 2 of 5]: Did you tag ≥70% of your claims? [ Yes / No ]

Fill in Gate Record row for S2.

---

## Stage 3 — Hypotheses [Stage 3 of 5]

Check: Do you have both S1 and S2 outputs? If not, go back.

What to do: Run prove-hypothesis. Now — only now — write down your hypotheses.

For each one: write a one-sentence falsification condition. If you can't write one, drop the hypothesis.

Put your hypotheses in a table. Include a "Source Stage" column. It should say S1 or S2 only.

Ask yourself:
- SEQUENCING RULE check [Stage 3 of 5]: Do all Source Stage entries say S1 or S2? [ Yes / No ]
- FALSIFICATION RULE check [Stage 3 of 5]: Does every hypothesis have a falsification condition? [ Yes / No ]

Fill in Gate Record row for S3.

---

## Stage 4 — Analysis [Stage 4 of 5]

Check: Do you have S3 hypotheses with falsification conditions? If not, go back.

What to do: Run prove-analysis. For each hypothesis: what supports it, what contradicts it, how confident are you?

Build a table with columns: Hypothesis, Supporting Evidence, Contradicting Evidence, Confidence, Falsified Y/N, Stage (S4).

Ask yourself:
- ATTRIBUTION RULE check [Stage 4 of 5]: Are evidence references tagged to specific stages? [ Yes / No ]
- SEQUENCING RULE check [Stage 4 of 5]: If you sort by the Stage column, does everything line up right? [ Yes / No ]
- CALIBRATION RULE check [Stage 4 of 5]: Is there genuine variation in your confidence levels, or are they all the same? [ Yes / No ]

Fill in Gate Record row for S4.

---

## Stage 5 — Synthesis and Verdict [Stage 5 of 5]

Check: Do you have the S4 analysis table? If not, go back.

What to do: Run prove-synthesize. Pull the campaign together.

**Synthesis section**: Don't just list findings. Say explicitly where the web search (S1) and intelligence review (S2) agree — and where they don't. Name the disagreements.

**Gaps section**: List what you still don't know after all five stages. Be honest.

**Decision sentence**: Write one sentence. Either you're ready to proceed, or you name the specific thing that has to be resolved first. Don't write a paragraph — the discipline of a single sentence is the signal that you've actually made a decision.

Ask yourself:
- ATTRIBUTION RULE check [Stage 5 of 5]: Does the synthesis trace consensus/conflict back to S1 and S2 by name? [ Yes / No ]
- SEQUENCING RULE check [Stage 5 of 5]: Does the final brief confirm no hypothesis was written before its evidence? [ Yes / No ]
- FALSIFICATION RULE check [Stage 5 of 5]: Does every hypothesis have a stated falsification outcome? [ Yes / No ]
- CALIBRATION RULE check [Stage 5 of 5]: Do your confidence levels actually vary? [ Yes / No ]
- Calibration anti-pattern guard: if every hypothesis is "Medium", you haven't calibrated — go back and distinguish them.

Fill in Gate Record row for S5.

---

## What the Final Brief Looks Like

Write it as a single document a stranger could read and understand. Include:

1. Title and topic
2. Web findings (tagged S1)
3. Intelligence findings (tagged S2)
4. Hypotheses with falsification conditions
5. Analysis table with confidence ratings and Stage column
6. Synthesis — say where S1 and S2 agree and disagree
7. Gaps and open questions
8. Decision readiness sentence
9. Gate Record (filled in)
10. Audit table

**Audit Table**

| Rule | Stage | Stage Index | Form | Pass/Fail |
|------|-------|-------------|------|-----------|
| ATTRIBUTION | S1 | 1 of 5 | Binary | |
| ATTRIBUTION | S2 | 2 of 5 | Binary | |
| ATTRIBUTION | S4 | 4 of 5 | Binary | |
| ATTRIBUTION | S5 | 5 of 5 | Binary | |
| SEQUENCING | S3 | 3 of 5 | Binary | |
| SEQUENCING | S4 | 4 of 5 | Binary | |
| SEQUENCING | S5 | 5 of 5 | Binary | |
| FALSIFICATION | S3 | 3 of 5 | Binary | |
| FALSIFICATION | S5 | 5 of 5 | Binary | |
| CALIBRATION | S4 | 4 of 5 | Binary | |
| CALIBRATION | S5 | 5 of 5 | Binary | |

Row count: 11. Recompute from coverage map if rules change — this is a derived value.
```

---

## V-05 — Combination Axis (Role Sequence + Extensibility-First Governance)

**Variation axis**: Role sequence framing (V-01) combined with extensibility-first governance architecture (C-29)  
**Hypothesis**: When governance rules are encoded as a formula (count = Σ applicable stages per rule) rather than a fixed structure, and stages are named by role so handoff is explicit, a new rule can be added mid-design without triggering a structural rewrite — the formula absorbs the new rule and the handoff chain absorbs the new role automatically.

```markdown
You are running campaign-evidence for the topic the user provides.

The campaign is a five-role relay. Each role produces an output, hands it to the next role,
and closes. Governance is formula-driven — the coverage map and audit table row count are
computed from a rule registry, not stored as static integers. Adding a rule to the registry
automatically propagates to the coverage map, gate record, and audit table without edits elsewhere.

---

## GOVERNANCE REGISTRY

Register each rule here. Coverage map and audit row count are computed from this registry.

| Rule ID | Rule Name | Applicable Roles | Applicable Count |
|---------|-----------|-----------------|-----------------|
| R1 | ATTRIBUTION RULE | Roles 1, 2, 4, 5 | 4 |
| R2 | SEQUENCING RULE | Roles 3, 4, 5 | 3 |
| R3 | FALSIFICATION RULE | Roles 3, 5 | 2 |
| R4 | CALIBRATION RULE | Roles 4, 5 | 2 |
| **Total** | | | **11** |

To add a new peer rule: add a row to this registry. The coverage map gains a new row.
The audit table row count increases by the rule's applicable count. No static integers to update.
All registered rules are peers — the registry encodes no primary/secondary distinction.

### Rule Declarations (all four at peer tier)

**R1 — ATTRIBUTION RULE** [invoked at: Roles 1, 2, 4, 5]
Tag every material claim with its source role: (R1), (R2), (R3), (R4), or (R5).
≥70% of material claims carry a role-source tag.
Adding a new evidence-gathering role extends this rule's applicable count automatically.

**R2 — SEQUENCING RULE** [invoked at: Roles 3, 4, 5]
Hypotheses are declared only after Role 1 and Role 2 have closed their outputs.
A hypothesis anchored before evidence is a bias, not a hypothesis.
Machine enforcement: Stage column in evidence table — hypothesis rows reference R1/R2 only.
Sorting the Stage column must confirm this at any point.

**R3 — FALSIFICATION RULE** [invoked at: Roles 3, 5]
Every hypothesis carries a falsification condition.
A hypothesis without a falsification condition is a statement of belief, not a testable claim.

**R4 — CALIBRATION RULE** [invoked at: Roles 4, 5]
Confidence ratings span at least two distinct levels across all findings.
Anti-uniformity guard: a brief where every finding carries the same confidence level fails calibration.

---

## PRE-DECLARED COVERAGE MAP (derived from registry, immutable after this point)

| Rule | Role 1 | Role 2 | Role 3 | Role 4 | Role 5 |
|------|--------|--------|--------|--------|--------|
| R1 ATTRIBUTION   | ✓ | ✓ | — | ✓ | ✓ |
| R2 SEQUENCING    | — | — | ✓ | ✓ | ✓ |
| R3 FALSIFICATION | — | — | ✓ | — | ✓ |
| R4 CALIBRATION   | — | — | — | ✓ | ✓ |

Audit row count = 11 (computed: 4+3+2+2). Recomputed if registry changes.
This map is finalized before Role 1 begins and cannot be modified after execution starts.

---

## PRE-TEMPLATED GATE RECORD

| Role | Title | Entry Condition | Exit Condition | Entry | Exit |
|------|-------|----------------|----------------|-------|------|
| 1 | Web Researcher | Topic received | Web findings documented (R1-tagged) | | |
| 2 | Intelligence Analyst | Role 1 output present | Intelligence findings documented (R2-tagged) | | |
| 3 | Hypothesis Architect | Role 1 + Role 2 outputs present | Hypotheses + falsification conditions declared | | |
| 4 | Evidence Analyst | Role 3 hypothesis table present | Analysis table with Stage column + confidence ratings | | |
| 5 | Synthesis Director | Role 4 analysis complete | Final brief with verdict, gate record, audit table | | |

---

## RELAY EXECUTION

### Role 1 — Web Researcher [Stage 1 of 5]

Relay baton received from: Campaign Start.
Entry gate: Topic present? [ Pass / Fail ]

Run prove-websearch. Tag all material claims (R1).

R1 ATTRIBUTION RULE invoked [Role 1, Stage 1 of 5]: Are ≥70% of claims tagged (R1)? [ Yes / No ]

Exit gate: Web findings documented? [ Pass / Fail ]
Relay baton passes to: Role 2 — Intelligence Analyst.

---

### Role 2 — Intelligence Analyst [Stage 2 of 5]

Relay baton received from: Role 1.
Entry gate: Role 1 output present? [ Pass / Fail ]

Run prove-intelligence. Tag all material claims (R2).

R1 ATTRIBUTION RULE invoked [Role 2, Stage 2 of 5]: Are ≥70% of Role 2 claims tagged (R2)? [ Yes / No ]

Exit gate: Intelligence findings documented? [ Pass / Fail ]
Relay baton passes to: Role 3 — Hypothesis Architect.

---

### Role 3 — Hypothesis Architect [Stage 3 of 5]

Relay baton received from: Role 2.
Entry gate: Role 1 AND Role 2 outputs both present? [ Pass / Fail ]

Run prove-hypothesis. Declare hypotheses grounded in Role 1 / Role 2 evidence only.
Evidence table includes Stage column — all hypothesis rows must reference R1 or R2 only.

| # | Hypothesis | Evidence Source | Stage | Falsification Condition |
|---|-----------|-----------------|-------|------------------------|
| H1 | | | R1/R2 | |

R2 SEQUENCING RULE invoked [Role 3, Stage 3 of 5]: Do all Stage cells contain R1 or R2? [ Yes / No ]
R3 FALSIFICATION RULE invoked [Role 3, Stage 3 of 5]: Does every hypothesis carry a falsification condition? [ Yes / No ]

Exit gate: Hypothesis table with falsification conditions complete? [ Pass / Fail ]
Relay baton passes to: Role 4 — Evidence Analyst.

---

### Role 4 — Evidence Analyst [Stage 4 of 5]

Relay baton received from: Role 3.
Entry gate: Role 3 hypothesis table present? [ Pass / Fail ]

Run prove-analysis. Evaluate each hypothesis; assign confidence level.

| H# | Hypothesis | Supporting | Contradicting | Confidence | Falsified? | Stage |
|----|-----------|-----------|--------------|------------|-----------|-------|
| H1 | | | | High/Med/Low | Y/N | R4 |

R1 ATTRIBUTION RULE invoked [Role 4, Stage 4 of 5]: Do evidence references cite stage-tagged sources? [ Yes / No ]
R2 SEQUENCING RULE invoked [Role 4, Stage 4 of 5]: Does Stage column sort confirm sequencing? [ Yes / No ]
R4 CALIBRATION RULE invoked [Role 4, Stage 4 of 5]: Does Confidence column contain ≥2 distinct values? [ Yes / No ]

Exit gate: Analysis table with Stage column and confidence ratings complete? [ Pass / Fail ]
Relay baton passes to: Role 5 — Synthesis Director.

---

### Role 5 — Synthesis Director [Stage 5 of 5]

Relay baton received from: Role 4.
Entry gate: Role 4 analysis complete? [ Pass / Fail ]

Run prove-synthesize.

**Synthesis**: State explicitly where Role 1 (web) and Role 2 (intelligence) agree vs. diverge.
Do not list findings side-by-side — name the consensus or the conflict.

**Gaps**: List what remains unknown after the full relay.

**Decision Readiness**: One sentence — posture + blocking gap if not ready.
Compressed form required: if the sentence runs to multiple clauses, compress further.

R1 ATTRIBUTION RULE invoked [Role 5, Stage 5 of 5]: Does synthesis attribute consensus/conflict to R1 and R2 explicitly? [ Yes / No ]
R2 SEQUENCING RULE invoked [Role 5, Stage 5 of 5]: Does final brief confirm evidence preceded hypothesis declaration? [ Yes / No ]
R3 FALSIFICATION RULE invoked [Role 5, Stage 5 of 5]: Are falsification outcomes declared for all hypotheses? [ Yes / No ]
R4 CALIBRATION RULE invoked [Role 5, Stage 5 of 5]: Do final confidence ratings span ≥2 distinct levels? [ Yes / No ]
Anti-uniformity guard: if every hypothesis carries the same confidence level, revise before closing.

Exit gate: Final brief with verdict, gate record, audit table complete? [ Pass / Fail ]
Relay complete. Baton deposited: Final Output Brief.

---

## FINAL OUTPUT BRIEF

Produce one self-contained document:

1. Title and topic context
2. Relay summary — five roles, outputs produced
3. Hypotheses table with falsification conditions and outcomes
4. Analysis table with Stage column and confidence ratings
5. Synthesis — R1 vs R2 consensus and conflict named
6. Gaps and open questions
7. Decision Readiness — one sentence
8. Gate Record (filled)
9. Consolidated Invocation Audit Table

**Consolidated Invocation Audit Table**

Row count = Σ(applicable roles per rule) = 11.
Recomputed from governance registry if a rule is added — not a stored integer.

| Rule | Role | Stage Index | Form | Pass/Fail |
|------|------|-------------|------|-----------|
| R1 ATTRIBUTION | Role 1 | 1 of 5 | Binary | |
| R1 ATTRIBUTION | Role 2 | 2 of 5 | Binary | |
| R1 ATTRIBUTION | Role 4 | 4 of 5 | Binary | |
| R1 ATTRIBUTION | Role 5 | 5 of 5 | Binary | |
| R2 SEQUENCING | Role 3 | 3 of 5 | Binary | |
| R2 SEQUENCING | Role 4 | 4 of 5 | Binary | |
| R2 SEQUENCING | Role 5 | 5 of 5 | Binary | |
| R3 FALSIFICATION | Role 3 | 3 of 5 | Binary | |
| R3 FALSIFICATION | Role 5 | 5 of 5 | Binary | |
| R4 CALIBRATION | Role 4 | 4 of 5 | Binary | |
| R4 CALIBRATION | Role 5 | 5 of 5 | Binary | |

Extensibility check: adding a new peer rule R5 applicable at Roles 1, 3, 5 would add 3 rows,
bringing the total to 14. No other changes required.
```

---

## Variation Summary

| ID | Axis | Single-Axis | Hypothesis |
|----|------|-------------|------------|
| V-01 | Role sequence | Yes | Named handoff chain prevents hypothesis pre-commitment via social contract between named actors |
| V-02 | Output format | Yes | Table-first format with Stage column converts sequencing compliance from assertion to sort-verifiable property |
| V-03 | Lifecycle emphasis | Yes | Gate-first structure makes C-24/C-25/C-27 inevitable — executor fills a pre-existing form, not a remembered annotation |
| V-04 | Phrasing register | Yes | Imperative/conversational register reduces cognitive distance between reading a rule and applying it in the moment |
| V-05 | Role sequence + extensibility | Combination | Formula-driven governance registry absorbs new rules without structural rewrites; relay framing makes new roles natural |
