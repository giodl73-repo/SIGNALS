# Quest Variate — campaign-evidence R10

Five complete, runnable prompt variations. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

---

## V-01 — Axis: Role Sequence
**Variation**: Intelligence-first ordering (Intel → Web → Hypothesis → Analysis → Synthesis)  
**Hypothesis**: Leading with intelligence (domain framing) before websearch reduces anchoring bias — the domain model is built from first principles before current-moment search results can contaminate the frame.

---

```markdown
You are running a Campaign-Evidence investigation for the topic: {{TOPIC}}.

This campaign executes five named stages in strict sequence. Intelligence framing precedes
websearch so the domain model is not contaminated by current-moment search results. All
evidence stages complete before hypotheses are declared.

---

## GOVERNANCE PREAMBLE

All rules declared here are peers. No rule is primary. Rules are invoked by identifier at
every applicable stage — positively where they apply, negatively where they do not.

**ATTRIBUTION RULE** [invoked at: Stage 1, Stage 2, Stage 4, Stage 5]
Every material claim carries its source stage ("per Stage N"). At least 70% of material
claims in any stage must carry attribution. An unattributed claim is not evidence.

**FALSIFICATION RULE** [invoked at: Stage 3, Stage 5]
Every hypothesis carries an explicit falsification condition — a stated criterion that would
cause rejection. A hypothesis without a falsification condition is not a hypothesis; it is
a preference.

**CALIBRATION RULE** [invoked at: Stage 4, Stage 5]
Confidence ratings must vary. If all findings carry the same confidence level, calibration
is insufficient. Anti-uniformity guard: at least two distinct levels (High / Medium / Low)
must appear across findings. A uniform distribution triggers mandatory recalibration.

**SEQUENCING RULE** [invoked at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
Evidence stages (Stage 1 and Stage 2) must complete before hypothesis formation (Stage 3).
A hypothesis anchored before evidence gathering is a bias, not a hypothesis. This rule
governs every stage boundary in the campaign.

---

## COVERAGE MAP
*Finalized before Stage 1. Cannot be modified after execution begins.*

| Rule          | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|---------------|---------|---------|---------|---------|---------|
| ATTRIBUTION   | ✓       | ✓       | —       | ✓       | ✓       |
| FALSIFICATION | —       | —       | ✓       | —       | ✓       |
| CALIBRATION   | —       | —       | —       | ✓       | ✓       |
| SEQUENCING    | ✓       | ✓       | ✓       | ✓       | ✓       |

All 4 rules are peers. Row count = 13 positive invocations + 7 negative invocations = 20
total invocation artifacts. Adding a new peer rule propagates automatically; no static count
is updated.

---

## GATE RECORD TEMPLATE
*Pre-instantiated. Fill each cell as its stage completes. An unfilled cell signals a gap.*

| Stage | Role | Entry Condition | Entry | Exit Condition | Exit |
|-------|------|----------------|-------|---------------|------|
| 1 | Intelligence Analyst | Topic confirmed; campaign initialized | [ ] | ≥5 domain concepts mapped with attribution | [ ] |
| 2 | Web Evidence Collector | Stage 1 exit: Pass | [ ] | ≥5 web findings with attribution | [ ] |
| 3 | Hypothesis Architect | Stages 1+2 exit: Pass | [ ] | ≥2 hypotheses with falsification conditions | [ ] |
| 4 | Pattern Analyst | Stage 3 exit: Pass | [ ] | Hypotheses analyzed; ≥2 confidence levels | [ ] |
| 5 | Synthesis Director | Stage 4 exit: Pass | [ ] | Self-contained brief; audit table complete | [ ] |

---

## STAGE 1 OF 5 — Intelligence Analyst

**Entry condition**: Topic confirmed; campaign initialized.
**Role handoff from**: (opening stage — no predecessor)
**Role passes to**: Stage 2 — Web Evidence Collector

Execute prove-intelligence for {{TOPIC}}. Map the domain: identify key concepts, actors,
forces, structural tensions, and assumptions that frame the topic. Do not state hypotheses.
Do not draw conclusions. This stage produces the lens through which web evidence will be read.

**Rule invocations:**
- ATTRIBUTION RULE [Stage 1 of 5]: Are ≥70% of domain claims attributed to "per intelligence
  review"? [ Yes / No ]
- FALSIFICATION RULE [Stage 1 of 5]: N/A — evidence stage; no hypotheses declared.
- CALIBRATION RULE [Stage 1 of 5]: N/A — no confidence ratings at this stage.
- SEQUENCING RULE [Stage 1 of 5]: Is this an evidence stage with hypothesis formation still
  pending? [ Yes / No ]

**Exit condition**: ≥5 domain concepts mapped. Fill Gate Record Stage 1 cells.

---

## STAGE 2 OF 5 — Web Evidence Collector

**Entry condition**: Stage 1 exit: Pass.
**Role handoff from**: Stage 1 — Intelligence Analyst
**Role passes to**: Stage 3 — Hypothesis Architect

Execute prove-websearch for {{TOPIC}}. Gather current external evidence: published data,
market signals, research findings, named examples. Interpret findings through the domain
model built in Stage 1 — note where web evidence confirms, extends, or challenges the
intelligence frame. Attribute every claim to its web source.

**Rule invocations:**
- ATTRIBUTION RULE [Stage 2 of 5]: Are ≥70% of web claims attributed to their source? [ Yes / No ]
- FALSIFICATION RULE [Stage 2 of 5]: N/A — evidence stage; no hypotheses declared.
- CALIBRATION RULE [Stage 2 of 5]: N/A — no confidence ratings at this stage.
- SEQUENCING RULE [Stage 2 of 5]: Is hypothesis formation still pending? [ Yes / No ]

**Exit condition**: ≥5 web-sourced findings with attribution. Fill Gate Record Stage 2 cells.

---

## STAGE 3 OF 5 — Hypothesis Architect

**Entry condition**: Stages 1 and 2 exit: Pass.
**Role handoff from**: Stage 2 — Web Evidence Collector
**Role passes to**: Stage 4 — Pattern Analyst

Execute prove-hypothesis. Declare hypotheses now that evidence exists. Each hypothesis must
include: (a) a statement, (b) an explicit falsification condition, (c) the Stage 1/Stage 2
evidence row(s) that ground it — cited as [S1] or [S2].

Note: hypotheses are formed here, not at campaign outset, because a hypothesis anchored
before evidence gathering is a bias, not a hypothesis.

**Rule invocations:**
- ATTRIBUTION RULE [Stage 3 of 5]: N/A — hypotheses cite prior stage evidence; attribution
  satisfied upstream.
- FALSIFICATION RULE [Stage 3 of 5]: Does every hypothesis carry an explicit falsification
  condition? [ Yes / No ]
- CALIBRATION RULE [Stage 3 of 5]: N/A — no confidence ratings at this stage.
- SEQUENCING RULE [Stage 3 of 5]: Were Stages 1 and 2 completed before this stage opened?
  [ Yes / No ]

**Exit condition**: ≥2 hypotheses, each with a falsification condition and S1/S2 grounding
citation. Fill Gate Record Stage 3 cells.

---

## STAGE 4 OF 5 — Pattern Analyst

**Entry condition**: Stage 3 exit: Pass.
**Role handoff from**: Stage 3 — Hypothesis Architect
**Role passes to**: Stage 5 — Synthesis Director

Execute prove-analysis. Evaluate each hypothesis against Stage 1 and Stage 2 evidence.
Assign confidence levels (High / Medium / Low). At least two distinct levels must appear —
if they do not, recalibrate before closing this stage. Surface patterns, tensions,
corroborating chains, and disconfirming evidence.

**Rule invocations:**
- ATTRIBUTION RULE [Stage 4 of 5]: Are analysis claims linked to their source stage (S1/S2)?
  [ Yes / No ]
- FALSIFICATION RULE [Stage 4 of 5]: N/A — falsification verdict rendered at synthesis.
- CALIBRATION RULE [Stage 4 of 5]: Do confidence ratings include ≥2 distinct levels? [ Yes / No ]
- SEQUENCING RULE [Stage 4 of 5]: Are all analysis findings grounded only in S1/S2/S3
  evidence? [ Yes / No ]

**Exit condition**: All hypotheses analyzed; ≥2 distinct confidence levels present. Fill
Gate Record Stage 4 cells.

---

## STAGE 5 OF 5 — Synthesis Director

**Entry condition**: Stage 4 exit: Pass.
**Role handoff from**: Stage 4 — Pattern Analyst
**Role passes to**: (closing stage — output is the evidence brief)

Execute prove-synthesize. Produce the final evidence brief. Required sections:

1. **Consensus vs. Conflict** — Explicitly identify where Stage 1 (intelligence) and Stage 2
   (websearch) agree vs. diverge. Do not list findings side by side; name the agreement or
   tension directly.
2. **Hypothesis verdicts** — For each hypothesis, state whether evidence supports, challenges,
   or falsifies it against its falsification condition.
3. **Calibration note** — Confirm ≥2 distinct confidence levels appear. If all findings
   share one level, recalibrate here before closing.
4. **Gaps and open questions** — What remains unknown after this campaign? Frame for
   follow-up pickup.
5. **Decision readiness** — One sentence only: state whether evidence is sufficient to
   proceed and, if not, name the specific gap.

**Rule invocations:**
- ATTRIBUTION RULE [Stage 5 of 5]: Are ≥70% of synthesis claims attributed to their source
  stage? [ Yes / No ]
- FALSIFICATION RULE [Stage 5 of 5]: Is a verdict rendered on every hypothesis's
  falsification condition? [ Yes / No ]
- CALIBRATION RULE [Stage 5 of 5]: Are ≥2 distinct confidence levels present in the final
  brief? [ Yes / No ]
- SEQUENCING RULE [Stage 5 of 5]: Are all synthesis conclusions grounded in S1–S4 evidence
  only? [ Yes / No ]

**Exit condition**: Self-contained brief with completed gate record and audit table. Fill
Gate Record Stage 5 cells.

---

## FINAL OUTPUT ASSEMBLY

Assemble in this order:
1. Title and topic context
2. Governance preamble (rules + coverage map + completed gate record)
3. Stage 1: Intelligence findings
4. Stage 2: Web evidence findings
5. Stage 3: Hypotheses with falsification conditions
6. Stage 4: Analysis with confidence levels
7. Stage 5: Synthesis (consensus/conflict, verdicts, calibration, gaps, decision readiness)
8. Consolidated invocation audit table (below)

### Consolidated Invocation Audit Table

| Rule | Stage | Form | Result |
|------|-------|------|--------|
| ATTRIBUTION | 1 | Binary | [ ] |
| ATTRIBUTION | 2 | Binary | [ ] |
| ATTRIBUTION | 4 | Binary | [ ] |
| ATTRIBUTION | 5 | Binary | [ ] |
| FALSIFICATION | 3 | Binary | [ ] |
| FALSIFICATION | 5 | Binary | [ ] |
| CALIBRATION | 4 | Binary | [ ] |
| CALIBRATION | 5 | Binary | [ ] |
| SEQUENCING | 1 | Binary | [ ] |
| SEQUENCING | 2 | Binary | [ ] |
| SEQUENCING | 3 | Binary | [ ] |
| SEQUENCING | 4 | Binary | [ ] |
| SEQUENCING | 5 | Binary | [ ] |
| FALSIFICATION | 1 | Negative | N/A — evidence stage |
| FALSIFICATION | 2 | Negative | N/A — evidence stage |
| FALSIFICATION | 4 | Negative | N/A — analysis stage |
| CALIBRATION | 1 | Negative | N/A — no confidence ratings |
| CALIBRATION | 2 | Negative | N/A — no confidence ratings |
| CALIBRATION | 3 | Negative | N/A — no confidence ratings |
| ATTRIBUTION | 3 | Negative | N/A — hypotheses cite upstream stages |
```

---

## V-02 — Axis: Output Format
**Variation**: Table-dominant evidence structure — all findings captured as structured rows with explicit stage-index and confidence columns, making sequencing machine-verifiable as a column sort.  
**Hypothesis**: Forcing findings into a shared evidence table with a `stage` column makes C-28 (machine-verifiable sequencing) pass naturally as a structural property rather than a governance assertion — violations become visible by sorting the column, not by re-reading prose.

---

```markdown
You are running a Campaign-Evidence investigation for the topic: {{TOPIC}}.

This campaign produces a structured evidence table as its core artifact. All findings across
five stages are entered as rows in a shared table with explicit stage-index values. Sequencing
compliance is verifiable by sorting the stage column — hypothesis rows may only reference
evidence rows from Stage 1 or Stage 2.

---

## GOVERNANCE PREAMBLE

Four rules govern this campaign. All are peers. Each is declared with inline stage scope.

**ATTRIBUTION RULE** [invoked at: Stage 1, Stage 2, Stage 4, Stage 5]
Every evidence row carries a `source` field (web URL, named source, or "per intelligence
review"). At least 70% of rows must have a populated source field.

**FALSIFICATION RULE** [invoked at: Stage 3, Stage 5]
Every hypothesis row carries a `falsification_condition` field. An empty falsification_
condition field is a structural violation — the row cannot be closed without it.

**CALIBRATION RULE** [invoked at: Stage 4, Stage 5]
The `confidence` column must contain at least two distinct values (High / Medium / Low)
across evidence and analysis rows. A calibration check is a GROUP BY on the confidence
column — a single-value result triggers mandatory recalibration.

**SEQUENCING RULE** [invoked at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
The `stage` column enforces ordering. Hypothesis rows (stage = S3) may reference only
rows where stage = S1 or S2 in their `evidence_ref` field. A hypothesis row referencing
S3+ evidence is a sequencing violation detectable by column inspection.

---

## COVERAGE MAP
*Finalized before Stage 1. Immutable. Row count derived from map; no static integer stored.*

| Rule          | S1 | S2 | S3 | S4 | S5 |
|---------------|----|----|----|----|----|
| ATTRIBUTION   | ✓  | ✓  | —  | ✓  | ✓  |
| FALSIFICATION | —  | —  | ✓  | —  | ✓  |
| CALIBRATION   | —  | —  | —  | ✓  | ✓  |
| SEQUENCING    | ✓  | ✓  | ✓  | ✓  | ✓  |

---

## EVIDENCE TABLE SCHEMA
*All stages write to this shared table. Do not deviate from column names.*

| row_id | stage | role | type | claim | source | evidence_ref | confidence | falsification_condition | status |
|--------|-------|------|------|-------|--------|--------------|------------|------------------------|--------|

**Column definitions:**
- `stage`: S1 / S2 / S3 / S4 / S5 — the stage that produced this row
- `role`: Intelligence Analyst / Web Collector / Hypothesis Architect / Pattern Analyst /
  Synthesis Director
- `type`: domain-concept / web-finding / hypothesis / analysis / synthesis-finding
- `claim`: the finding or statement
- `source`: attribution (required for S1, S2, S4, S5 rows)
- `evidence_ref`: for hypothesis rows, cite S1/S2 row IDs; for analysis rows, cite S1-S3 IDs
- `confidence`: High / Medium / Low (required for S4, S5 rows)
- `falsification_condition`: required for hypothesis rows only
- `status`: Open / Supported / Challenged / Falsified (populated at S5)

---

## GATE RECORD TEMPLATE
*Pre-instantiated. Fill each cell as the stage completes.*

| Stage | Entry Condition | Entry | Exit Condition | Exit |
|-------|----------------|-------|---------------|------|
| S1: Intelligence Analyst | Topic confirmed | [ ] | ≥5 domain rows with attribution in table | [ ] |
| S2: Web Collector | S1 exit: Pass | [ ] | ≥5 web rows with attribution in table | [ ] |
| S3: Hypothesis Architect | S1+S2 exit: Pass | [ ] | ≥2 hypothesis rows with falsification_condition | [ ] |
| S4: Pattern Analyst | S3 exit: Pass | [ ] | All hypotheses analyzed; ≥2 confidence values | [ ] |
| S5: Synthesis Director | S4 exit: Pass | [ ] | Synthesis rows complete; audit table filled | [ ] |

---

## STAGE EXECUTION

### Stage 1 — Intelligence Analyst (S1)
**Entry**: Topic confirmed. **Role passes to**: S2 — Web Collector.

Run prove-intelligence. Write ≥5 domain-concept rows to the evidence table (stage = S1).
Populate: claim, source ("per intelligence review"), role, type. Leave confidence and
falsification_condition blank for S1 rows.

**Rule invocations:**
- ATTRIBUTION [S1 of 5]: Do ≥70% of S1 rows have a populated `source` field? [ Yes / No ]
- FALSIFICATION [S1 of 5]: N/A — no hypothesis rows at S1.
- CALIBRATION [S1 of 5]: N/A — confidence field blank at S1.
- SEQUENCING [S1 of 5]: Are all rows in the table at this point stage = S1? [ Yes / No ]

Fill Gate Record S1 cells.

---

### Stage 2 — Web Evidence Collector (S2)
**Entry**: S1 exit: Pass. **Role passes to**: S3 — Hypothesis Architect.

Run prove-websearch. Append ≥5 web-finding rows to the evidence table (stage = S2).
Populate: claim, source (URL or publication name), role, type. Leave confidence blank.

**Rule invocations:**
- ATTRIBUTION [S2 of 5]: Do ≥70% of S2 rows have a populated `source` field? [ Yes / No ]
- FALSIFICATION [S2 of 5]: N/A — no hypothesis rows at S2.
- CALIBRATION [S2 of 5]: N/A — confidence field blank at S2.
- SEQUENCING [S2 of 5]: Are all rows with stage = S3+ still absent from the table? [ Yes / No ]

Fill Gate Record S2 cells.

---

### Stage 3 — Hypothesis Architect (S3)
**Entry**: S1+S2 exit: Pass. **Role passes to**: S4 — Pattern Analyst.

Run prove-hypothesis. Append ≥2 hypothesis rows to the evidence table (stage = S3).
For each row, populate: claim (hypothesis statement), falsification_condition (required —
leave blank only if you accept a structural violation), evidence_ref (cite S1/S2 row IDs
only — no forward references). Leave confidence blank.

Note: hypotheses are declared here, after evidence, because a hypothesis formed before
evidence is a bias. The evidence_ref constraint enforces this structurally.

**Rule invocations:**
- ATTRIBUTION [S3 of 5]: N/A — S3 rows reference upstream evidence; attribution upstream.
- FALSIFICATION [S3 of 5]: Does every S3 row have a non-empty `falsification_condition`
  field? [ Yes / No ]
- CALIBRATION [S3 of 5]: N/A — confidence field blank at S3.
- SEQUENCING [S3 of 5]: Do all S3 `evidence_ref` values reference only S1/S2 row IDs?
  [ Yes / No ]

Fill Gate Record S3 cells.

---

### Stage 4 — Pattern Analyst (S4)
**Entry**: S3 exit: Pass. **Role passes to**: S5 — Synthesis Director.

Run prove-analysis. For each S3 hypothesis, append one or more analysis rows (stage = S4).
Populate: claim (analytical finding), confidence (High/Medium/Low), evidence_ref (S1/S2/S3
row IDs), source ("per pattern analysis"). Perform a GROUP BY on the confidence column
across all S4 rows — if only one value appears, recalibrate before closing.

**Rule invocations:**
- ATTRIBUTION [S4 of 5]: Do ≥70% of S4 rows have a populated `source` field? [ Yes / No ]
- FALSIFICATION [S4 of 5]: N/A — falsification verdict at S5.
- CALIBRATION [S4 of 5]: Does GROUP BY(confidence) on S4 rows return ≥2 distinct values?
  [ Yes / No ]
- SEQUENCING [S4 of 5]: Do all S4 `evidence_ref` values reference only S1/S2/S3 row IDs?
  [ Yes / No ]

Fill Gate Record S4 cells.

---

### Stage 5 — Synthesis Director (S5)
**Entry**: S4 exit: Pass. **Role passes to**: (closing stage — output is the evidence brief).

Run prove-synthesize. Append synthesis rows (stage = S5) and produce narrative sections.

**Evidence table additions:**
- One synthesis-finding row per major conclusion, with confidence and evidence_ref
- Set `status` field on all S3 hypothesis rows: Supported / Challenged / Falsified

**Narrative sections required:**
- **Consensus vs. Conflict**: WHERE stage IN (S1, S2) — identify rows where S1 and S2 agree
  vs. where they diverge. Name the tension; do not merely list.
- **Hypothesis verdicts**: For each S3 row, state the falsification verdict against its
  `falsification_condition` field.
- **Gaps**: What claim types are absent from the table? What would a follow-up S1/S2 run
  need to add?
- **Decision readiness**: One sentence — proceed or name the gap.

**Rule invocations:**
- ATTRIBUTION [S5 of 5]: Do ≥70% of S5 rows have a populated `source` field? [ Yes / No ]
- FALSIFICATION [S5 of 5]: Has `status` been set on every S3 hypothesis row? [ Yes / No ]
- CALIBRATION [S5 of 5]: Does GROUP BY(confidence) across S4+S5 rows return ≥2 distinct
  values? [ Yes / No ]
- SEQUENCING [S5 of 5]: Do all S5 `evidence_ref` values reference only S1–S4 row IDs?
  [ Yes / No ]

Fill Gate Record S5 cells.

---

## FINAL OUTPUT

Produce in this order:
1. Title and topic context
2. Governance preamble + coverage map + completed gate record
3. Complete evidence table (all rows, all stages)
4. Consensus vs. Conflict narrative
5. Hypothesis verdicts
6. Gaps and open questions
7. Decision readiness (one sentence)
8. Consolidated invocation audit table

### Consolidated Invocation Audit Table

| Rule | Stage | Form | Result |
|------|-------|------|--------|
| ATTRIBUTION | S1 | Binary | [ ] |
| ATTRIBUTION | S2 | Binary | [ ] |
| ATTRIBUTION | S4 | Binary | [ ] |
| ATTRIBUTION | S5 | Binary | [ ] |
| FALSIFICATION | S3 | Binary | [ ] |
| FALSIFICATION | S5 | Binary | [ ] |
| CALIBRATION | S4 | Binary | [ ] |
| CALIBRATION | S5 | Binary | [ ] |
| SEQUENCING | S1 | Binary | [ ] |
| SEQUENCING | S2 | Binary | [ ] |
| SEQUENCING | S3 | Binary | [ ] |
| SEQUENCING | S4 | Binary | [ ] |
| SEQUENCING | S5 | Binary | [ ] |
| FALSIFICATION | S1 | Negative | N/A — evidence stage |
| FALSIFICATION | S2 | Negative | N/A — evidence stage |
| FALSIFICATION | S4 | Negative | N/A — analysis stage |
| CALIBRATION | S1 | Negative | N/A — no confidence column |
| CALIBRATION | S2 | Negative | N/A — no confidence column |
| CALIBRATION | S3 | Negative | N/A — no confidence column |
| ATTRIBUTION | S3 | Negative | N/A — hypotheses cite upstream |
```

---

## V-03 — Axis: Lifecycle Emphasis
**Variation**: Gate-heavy structure — entry/exit conditions are the primary organizing principle, not role names or rule invocations. Each stage is defined by what must be true before it opens and what it must produce before the next stage opens.  
**Hypothesis**: When gate conditions are the structural spine rather than a trailing governance detail, C-24/C-25/C-27 become structural properties of the campaign rather than separately-enforced criteria — an executor reads gates before reading anything else.

---

```markdown
You are running a Campaign-Evidence investigation for the topic: {{TOPIC}}.

This campaign is gate-driven. Before each stage opens, you confirm its entry condition.
Before each stage closes, you confirm its exit condition. The gate record is the primary
artifact — every other output is secondary to it.

---

## GOVERNANCE PREAMBLE

Four peer rules govern this campaign. Each rule is declared with its stage applicability
scope inline. All rules are invoked positively where applicable and negatively where not.

**ATTRIBUTION RULE** [scope: Stage 1, Stage 2, Stage 4, Stage 5]
Claims carry source attribution. 70% threshold. Attribution tag: "per Stage N / source name."
Ungated stages: attribution is explicitly N/A.

**FALSIFICATION RULE** [scope: Stage 3, Stage 5]
Every hypothesis carries a falsification condition. The condition must be a specific criterion
that would cause rejection — not a restatement of the hypothesis as a negative.
Ungated stages: falsification is explicitly N/A.

**CALIBRATION RULE** [scope: Stage 4, Stage 5]
Confidence ratings must be non-uniform. Anti-uniformity guard: if all ratings are identical,
recalibrate before closing the stage. Levels: High / Medium / Low.
Ungated stages: calibration is explicitly N/A.

**SEQUENCING RULE** [scope: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
Evidence precedes hypotheses. Stages 1 and 2 must reach exit-condition Pass before Stage 3
may open. This rule applies at every stage because every stage either produces evidence,
forms hypotheses, or builds on them — each must know its position in the chain.

---

## COVERAGE MAP
*Declared now. Immutable after this point.*

| Rule          | S1 | S2 | S3 | S4 | S5 |
|---------------|----|----|----|----|----|
| ATTRIBUTION   | ✓  | ✓  | —  | ✓  | ✓  |
| FALSIFICATION | —  | —  | ✓  | —  | ✓  |
| CALIBRATION   | —  | —  | —  | ✓  | ✓  |
| SEQUENCING    | ✓  | ✓  | ✓  | ✓  | ✓  |

Positive invocations: 13. Negative invocations: 7. Total: 20. Row count derives from map.

---

## GATE RECORD — MASTER TABLE
*Pre-instantiated with blank cells. This table is the primary output artifact.*
*Fill each cell as the stage completes. An unfilled cell is a visible compliance gap.*

| Stage | Role | Entry Gate | ENTRY | Exit Gate | EXIT |
|-------|------|-----------|-------|----------|------|
| 1 | Websearch Collector | Campaign open; topic confirmed | [ ] | ≥5 attributed web findings produced | [ ] |
| 2 | Intelligence Analyst | S1 Exit = Pass | [ ] | ≥5 attributed domain concepts produced | [ ] |
| 3 | Hypothesis Architect | S1 Exit = Pass AND S2 Exit = Pass | [ ] | ≥2 hypotheses with falsification conditions | [ ] |
| 4 | Pattern Analyst | S3 Exit = Pass | [ ] | All hypotheses analyzed; ≥2 confidence levels | [ ] |
| 5 | Synthesis Director | S4 Exit = Pass | [ ] | Brief complete; gate record fully populated | [ ] |

*Note: Stage 1 is Websearch (external evidence first) and Stage 2 is Intelligence (domain
framing informed by what external evidence exists). Both complete before Stage 3 opens.*

---

## STAGE EXECUTION — GATE-FIRST FORMAT

Each stage begins with a GATE CHECK block. Do not produce stage content until the entry
gate passes.

---

### GATE CHECK — Stage 1

```
ENTRY GATE: Campaign open; topic confirmed
Status: [ Pass / Fail ]
If Fail: stop. State which entry condition is unmet.
```

**Stage 1 — Websearch Collector**
Execute prove-websearch for {{TOPIC}}. Gather external evidence: data, publications, market
signals, named examples. Attribute each finding to its source.

**Rule invocations [Stage 1 of 5]:**
- ATTRIBUTION: Are ≥70% of S1 findings attributed to a named source? [ Yes / No ]
- FALSIFICATION: N/A — evidence stage; no hypotheses declared.
- CALIBRATION: N/A — no confidence ratings at this stage.
- SEQUENCING: Is hypothesis formation still pending (S3 not yet open)? [ Yes / No ]

```
EXIT GATE: ≥5 attributed web findings produced
Status: [ Pass / Fail ]
If Fail: produce additional findings before advancing.
```

Fill Gate Record Stage 1: Entry = [ Pass / Fail ], Exit = [ Pass / Fail ]

---

### GATE CHECK — Stage 2

```
ENTRY GATE: S1 Exit = Pass
Confirm: [ Confirmed / Blocked ]
If Blocked: Stage 2 cannot open. Return to Stage 1.
```

**Stage 2 — Intelligence Analyst**
Execute prove-intelligence for {{TOPIC}} informed by the web landscape discovered in Stage 1.
Map the domain: concepts, actors, forces, tensions. Note where the intelligence frame extends
or reframes Stage 1 findings.

**Rule invocations [Stage 2 of 5]:**
- ATTRIBUTION: Are ≥70% of S2 concepts attributed to "per intelligence review"? [ Yes / No ]
- FALSIFICATION: N/A — evidence stage; no hypotheses declared.
- CALIBRATION: N/A — no confidence ratings at this stage.
- SEQUENCING: Is hypothesis formation still pending (S3 not yet open)? [ Yes / No ]

```
EXIT GATE: ≥5 attributed domain concepts produced
Status: [ Pass / Fail ]
```

Fill Gate Record Stage 2: Entry = [ Pass / Fail ], Exit = [ Pass / Fail ]

---

### GATE CHECK — Stage 3

```
ENTRY GATE: S1 Exit = Pass AND S2 Exit = Pass
Confirm both: S1 [ Pass / Fail ] | S2 [ Pass / Fail ]
If either Fail: Stage 3 cannot open. Remedy the failing stage.
```

**Stage 3 — Hypothesis Architect**
Execute prove-hypothesis. With web evidence (S1) and intelligence framing (S2) complete,
declare hypotheses. For each hypothesis: (a) hypothesis statement, (b) falsification
condition — a criterion that would cause rejection, (c) evidence citation from S1 or S2.

**Rule invocations [Stage 3 of 5]:**
- ATTRIBUTION: N/A — hypotheses reference upstream evidence; attribution upstream.
- FALSIFICATION: Does every hypothesis carry an explicit falsification condition? [ Yes / No ]
- CALIBRATION: N/A — no confidence ratings at this stage.
- SEQUENCING: Were S1 and S2 gates confirmed before this stage opened? [ Yes / No ]

```
EXIT GATE: ≥2 hypotheses, each with a falsification condition and S1/S2 evidence citation
Status: [ Pass / Fail ]
```

Fill Gate Record Stage 3: Entry = [ Pass / Fail ], Exit = [ Pass / Fail ]

---

### GATE CHECK — Stage 4

```
ENTRY GATE: S3 Exit = Pass
Confirm: [ Confirmed / Blocked ]
```

**Stage 4 — Pattern Analyst**
Execute prove-analysis. Evaluate each hypothesis against S1 and S2 evidence. Assign
confidence levels. Calibration check: if GROUP BY on confidence returns a single value,
recalibrate before this stage closes.

**Rule invocations [Stage 4 of 5]:**
- ATTRIBUTION: Are S4 findings attributed to their source stage (S1/S2)? [ Yes / No ]
- FALSIFICATION: N/A — falsification verdict at S5.
- CALIBRATION: Do confidence ratings include ≥2 distinct values? [ Yes / No ]
- SEQUENCING: Are all S4 findings grounded only in S1/S2/S3 evidence? [ Yes / No ]

```
EXIT GATE: All hypotheses analyzed; confidence column contains ≥2 distinct levels
Status: [ Pass / Fail ]
```

Fill Gate Record Stage 4: Entry = [ Pass / Fail ], Exit = [ Pass / Fail ]

---

### GATE CHECK — Stage 5

```
ENTRY GATE: S4 Exit = Pass
Confirm: [ Confirmed / Blocked ]
```

**Stage 5 — Synthesis Director**
Execute prove-synthesize. Produce the final evidence brief with these required sections:

1. **Consensus vs. Conflict** — Where do S1 (web) and S2 (intelligence) agree or diverge?
   Name the specific tension; do not list findings side by side.
2. **Hypothesis verdicts** — For each hypothesis, assess its falsification condition against
   S4 analysis. State: Supported / Challenged / Falsified.
3. **Calibration confirmation** — State the confidence distribution. If uniform, recalibrate.
4. **Gaps and open questions** — What cannot be answered from this evidence set?
5. **Decision readiness** — One sentence: "Ready to proceed" or "Needs [specific gap]."

**Rule invocations [Stage 5 of 5]:**
- ATTRIBUTION: Are ≥70% of synthesis claims attributed to their source stage? [ Yes / No ]
- FALSIFICATION: Has a verdict been rendered on every hypothesis's falsification condition?
  [ Yes / No ]
- CALIBRATION: Are ≥2 distinct confidence levels present in the synthesis? [ Yes / No ]
- SEQUENCING: Are all synthesis conclusions grounded in S1–S4 evidence only? [ Yes / No ]

```
EXIT GATE: Brief complete; gate record Master Table fully populated; audit table present
Status: [ Pass / Fail ]
```

Fill Gate Record Stage 5: Entry = [ Pass / Fail ], Exit = [ Pass / Fail ]

---

## FINAL OUTPUT ORDER

1. Title and topic context
2. Governance preamble + coverage map
3. **Gate Record — Master Table** (fully populated — this is the primary artifact)
4. Stage 1: Web evidence findings
5. Stage 2: Intelligence findings
6. Stage 3: Hypotheses with falsification conditions
7. Stage 4: Analysis with confidence levels
8. Stage 5: Synthesis narrative (consensus/conflict, verdicts, gaps, decision readiness)
9. Consolidated invocation audit table

### Consolidated Invocation Audit Table

| Rule | Stage | Form | Result |
|------|-------|------|--------|
| ATTRIBUTION | S1 | Binary | [ ] |
| ATTRIBUTION | S2 | Binary | [ ] |
| ATTRIBUTION | S4 | Binary | [ ] |
| ATTRIBUTION | S5 | Binary | [ ] |
| FALSIFICATION | S3 | Binary | [ ] |
| FALSIFICATION | S5 | Binary | [ ] |
| CALIBRATION | S4 | Binary | [ ] |
| CALIBRATION | S5 | Binary | [ ] |
| SEQUENCING | S1 | Binary | [ ] |
| SEQUENCING | S2 | Binary | [ ] |
| SEQUENCING | S3 | Binary | [ ] |
| SEQUENCING | S4 | Binary | [ ] |
| SEQUENCING | S5 | Binary | [ ] |
| FALSIFICATION | S1 | Negative | N/A — evidence stage |
| FALSIFICATION | S2 | Negative | N/A — evidence stage |
| FALSIFICATION | S4 | Negative | N/A — analysis stage |
| CALIBRATION | S1 | Negative | N/A — no confidence ratings |
| CALIBRATION | S2 | Negative | N/A — no confidence ratings |
| CALIBRATION | S3 | Negative | N/A — no confidence ratings |
| ATTRIBUTION | S3 | Negative | N/A — hypotheses cite upstream |
```

---

## V-04 — Axes: Role Sequence + Output Format (Combination)
**Variation**: Intelligence-first role ordering combined with table-dominant output. Hypothesis rows carry grounding constraints that enforce sequencing as a structural column property.  
**Hypothesis**: Combining intelligence-first ordering with a structured evidence table eliminates two separate failure modes at once — anchoring bias (V-01's concern) and sequencing drift (V-02's concern) — because each row's `stage` and `evidence_ref` columns make both violations mechanically detectable.

---

```markdown
You are running a Campaign-Evidence investigation for the topic: {{TOPIC}}.

This campaign uses intelligence-first ordering and a shared evidence table as its primary
data structure. All findings across five stages are rows in the table. Stage ordering is
enforced by the `stage` column — sort it to verify no hypothesis row predates its evidence.

---

## GOVERNANCE PREAMBLE

Four peer rules. Each declared with inline scope. All rules are peers; none is primary.

**ATTRIBUTION RULE** [scope: S1, S2, S4, S5]
Every table row at these stages carries a populated `source` field. 70% threshold per stage.

**FALSIFICATION RULE** [scope: S3, S5]
Every S3 row carries a non-empty `falsification_condition` field. A hypothesis row without
a falsification_condition is a structural violation — the field cannot be omitted.

**CALIBRATION RULE** [scope: S4, S5]
The `confidence` column across S4/S5 rows must contain ≥2 distinct values. Anti-uniformity
guard: GROUP BY(confidence) returning one value triggers mandatory recalibration.

**SEQUENCING RULE** [scope: S1, S2, S3, S4, S5]
The `stage` column is the enforcement mechanism. S3 rows (`evidence_ref`) may reference only
rows where stage ∈ {S1, S2}. S4 rows may reference S1/S2/S3. S5 rows may reference S1–S4.
Forward references are structural violations detectable by column inspection.

Peer declaration: all 4 rules occupy identical structural tier. No rule governs another.
Rule count is dynamic — adding a rule propagates to coverage map and audit table without
updating static integers.

---

## COVERAGE MAP
*Finalized before Stage 1. Immutable.*

| Rule          | S1 | S2 | S3 | S4 | S5 |
|---------------|----|----|----|----|----|
| ATTRIBUTION   | ✓  | ✓  | —  | ✓  | ✓  |
| FALSIFICATION | —  | —  | ✓  | —  | ✓  |
| CALIBRATION   | —  | —  | —  | ✓  | ✓  |
| SEQUENCING    | ✓  | ✓  | ✓  | ✓  | ✓  |

---

## GATE RECORD TEMPLATE
*Pre-instantiated. Stage order: S1=Intelligence, S2=Websearch, S3=Hypothesis, S4=Analysis,
S5=Synthesis. Fill cells during execution.*

| Stage | Entry Gate | Entry | Exit Gate | Exit |
|-------|-----------|-------|----------|------|
| S1: Intelligence Analyst | Topic confirmed | [ ] | ≥5 domain rows in table; `source` populated | [ ] |
| S2: Websearch Collector | S1 Exit = Pass | [ ] | ≥5 web rows in table; `source` populated | [ ] |
| S3: Hypothesis Architect | S1+S2 Exit = Pass | [ ] | ≥2 hypothesis rows; `falsification_condition` non-empty | [ ] |
| S4: Pattern Analyst | S3 Exit = Pass | [ ] | Analysis rows present; ≥2 distinct `confidence` values | [ ] |
| S5: Synthesis Director | S4 Exit = Pass | [ ] | Synthesis rows present; gate record complete | [ ] |

---

## EVIDENCE TABLE SCHEMA

| row_id | stage | role | type | claim | source | evidence_ref | confidence | falsification_condition | status |
|--------|-------|------|------|-------|--------|--------------|------------|------------------------|--------|

**Constraints (enforced at row creation):**
- S3 rows: `evidence_ref` must cite only row_ids where stage = S1 or S2
- S4 rows: `evidence_ref` must cite only row_ids where stage ∈ {S1, S2, S3}
- S5 rows: `evidence_ref` must cite only row_ids where stage ∈ {S1, S2, S3, S4}
- S3 rows: `falsification_condition` must be non-empty
- S4/S5 rows: `confidence` must be non-empty

---

## STAGE EXECUTION

### Stage 1 — Intelligence Analyst [S1]
**Entry**: Topic confirmed. **Handoff from**: (opening stage). **Passes to**: S2.

Run prove-intelligence. Write ≥5 domain-concept rows (stage = S1). Populate: claim (concept
or structural finding), source ("per intelligence review"), type = domain-concept. Do not
open hypothesis rows. Do not populate confidence or falsification_condition.

**Rule invocations [S1 of 5]:**
- ATTRIBUTION [S1 of 5]: Do ≥70% of S1 rows have `source` populated? [ Yes / No ]
- FALSIFICATION [S1 of 5]: N/A — evidence stage; no hypothesis rows.
- CALIBRATION [S1 of 5]: N/A — `confidence` field blank at S1.
- SEQUENCING [S1 of 5]: Are all rows in the table at this point stage = S1 only? [ Yes / No ]

Fill Gate Record S1.

---

### Stage 2 — Websearch Collector [S2]
**Entry**: S1 Exit = Pass. **Handoff from**: S1. **Passes to**: S3.

Run prove-websearch. Append ≥5 web-finding rows (stage = S2). Populate: claim (finding),
source (URL or named publication), type = web-finding. Note where S2 findings confirm,
extend, or challenge S1 domain-concept rows (populate `evidence_ref` with S1 row_ids).

**Rule invocations [S2 of 5]:**
- ATTRIBUTION [S2 of 5]: Do ≥70% of S2 rows have `source` populated? [ Yes / No ]
- FALSIFICATION [S2 of 5]: N/A — evidence stage; no hypothesis rows.
- CALIBRATION [S2 of 5]: N/A — `confidence` field blank at S2.
- SEQUENCING [S2 of 5]: Are S3+ rows still absent from the table? [ Yes / No ]

Fill Gate Record S2.

---

### Stage 3 — Hypothesis Architect [S3]
**Entry**: S1 Exit = Pass AND S2 Exit = Pass. **Handoff from**: S2. **Passes to**: S4.

Run prove-hypothesis. Append ≥2 hypothesis rows (stage = S3). Required fields per row:
- `claim`: hypothesis statement
- `falsification_condition`: the specific criterion that would cause rejection (required)
- `evidence_ref`: comma-separated list of S1/S2 row_ids that ground this hypothesis
  (forward references to S3+ are structural violations)
- `type`: hypothesis

Note: hypotheses form here because a hypothesis anchored before evidence is a bias, not
a hypothesis. The `evidence_ref` constraint enforces the sequencing rule structurally.

**Rule invocations [S3 of 5]:**
- ATTRIBUTION [S3 of 5]: N/A — S3 rows cite upstream evidence; attribution upstream.
- FALSIFICATION [S3 of 5]: Is `falsification_condition` non-empty on every S3 row? [ Yes / No ]
- CALIBRATION [S3 of 5]: N/A — `confidence` field blank at S3.
- SEQUENCING [S3 of 5]: Do all S3 `evidence_ref` values reference only S1/S2 row_ids?
  [ Yes / No ]

Fill Gate Record S3.

---

### Stage 4 — Pattern Analyst [S4]
**Entry**: S3 Exit = Pass. **Handoff from**: S3. **Passes to**: S5.

Run prove-analysis. For each S3 hypothesis, append analysis rows (stage = S4). Required
fields: claim (analytical finding), confidence (High/Medium/Low), evidence_ref (S1/S2/S3
row_ids), source ("per pattern analysis"). Calibration check: GROUP BY(confidence) on S4
rows — if single value, recalibrate before closing.

**Rule invocations [S4 of 5]:**
- ATTRIBUTION [S4 of 5]: Do ≥70% of S4 rows have `source` populated? [ Yes / No ]
- FALSIFICATION [S4 of 5]: N/A — falsification verdict at S5.
- CALIBRATION [S4 of 5]: Does GROUP BY(confidence) on S4 rows return ≥2 distinct values?
  [ Yes / No ]
- SEQUENCING [S4 of 5]: Do all S4 `evidence_ref` values reference only S1/S2/S3 row_ids?
  [ Yes / No ]

Fill Gate Record S4.

---

### Stage 5 — Synthesis Director [S5]
**Entry**: S4 Exit = Pass. **Handoff from**: S4. **Passes to**: (closing stage).

Run prove-synthesize. Append synthesis rows (stage = S5). Set `status` on each S3 row:
Supported / Challenged / Falsified. Produce narrative sections:

1. **Consensus vs. Conflict** — Filter table: stage IN (S1, S2). Where do S1 and S2 rows
   agree vs. diverge? Name the tension explicitly.
2. **Falsification verdicts** — For each S3 row, state verdict against `falsification_
   condition`. Populate `status` field.
3. **Calibration confirmation** — Report confidence distribution. Recalibrate if uniform.
4. **Gaps** — What query would extend this table meaningfully?
5. **Decision readiness** — One sentence only.

**Rule invocations [S5 of 5]:**
- ATTRIBUTION [S5 of 5]: Do ≥70% of S5 rows have `source` populated? [ Yes / No ]
- FALSIFICATION [S5 of 5]: Has `status` been set on every S3 row? [ Yes / No ]
- CALIBRATION [S5 of 5]: Does confidence distribution across S4+S5 rows contain ≥2 distinct
  values? [ Yes / No ]
- SEQUENCING [S5 of 5]: Do all S5 `evidence_ref` values reference only S1–S4 row_ids?
  [ Yes / No ]

Fill Gate Record S5.

---

## FINAL OUTPUT ORDER

1. Title and topic context
2. Governance preamble + coverage map + completed gate record
3. Full evidence table (all rows, all stages)
4. Consensus vs. Conflict narrative
5. Hypothesis verdicts
6. Gaps and open questions
7. Decision readiness (one sentence)
8. Consolidated invocation audit table

### Consolidated Invocation Audit Table

| Rule | Stage | Form | Result |
|------|-------|------|--------|
| ATTRIBUTION | S1 | Binary | [ ] |
| ATTRIBUTION | S2 | Binary | [ ] |
| ATTRIBUTION | S4 | Binary | [ ] |
| ATTRIBUTION | S5 | Binary | [ ] |
| FALSIFICATION | S3 | Binary | [ ] |
| FALSIFICATION | S5 | Binary | [ ] |
| CALIBRATION | S4 | Binary | [ ] |
| CALIBRATION | S5 | Binary | [ ] |
| SEQUENCING | S1 | Binary | [ ] |
| SEQUENCING | S2 | Binary | [ ] |
| SEQUENCING | S3 | Binary | [ ] |
| SEQUENCING | S4 | Binary | [ ] |
| SEQUENCING | S5 | Binary | [ ] |
| FALSIFICATION | S1 | Negative | N/A — evidence stage |
| FALSIFICATION | S2 | Negative | N/A — evidence stage |
| FALSIFICATION | S4 | Negative | N/A — analysis stage |
| CALIBRATION | S1 | Negative | N/A — no confidence ratings |
| CALIBRATION | S2 | Negative | N/A — no confidence ratings |
| CALIBRATION | S3 | Negative | N/A — no confidence ratings |
| ATTRIBUTION | S3 | Negative | N/A — hypotheses cite upstream |
```

---

## V-05 — Axes: Lifecycle Emphasis + Phrasing Register (Combination)
**Variation**: Gate-heavy lifecycle structure expressed in conversational register — imperative prose, second-person, explains *why* each gate exists rather than just declaring it.  
**Hypothesis**: A conversational register makes the governance machinery more legible to first-time executors without sacrificing rubric compliance — the "why" embedded in each instruction reduces silent rule violations caused by rote execution without comprehension.

---

```markdown
You are running a Campaign-Evidence investigation for the topic: {{TOPIC}}.

Here's what you're doing and why: you're gathering evidence from five different angles,
in a specific order, before forming any hypotheses. The order matters because a hypothesis
formed before evidence is just a dressed-up assumption. Four rules keep the investigation
honest. Gates keep the stages from bleeding into each other.

Read the preamble carefully — it's not just scaffolding. The rules you declare here are
the same ones you'll invoke at each stage, and the gate record you fill in here is the
primary proof that the campaign ran correctly.

---

## GOVERNANCE PREAMBLE

These four rules apply throughout the campaign. They're listed here so you can refer to
them by name when you invoke them at each stage — not just cite them as prose warnings.

**ATTRIBUTION RULE** [applies at: Stage 1, Stage 2, Stage 4, Stage 5]
When you report a finding, say where it came from. "Per intelligence review" counts.
A URL counts. A named publication counts. "I found this" does not count.
Why this rule: findings without attribution cannot be weighted — they're just assertions.
Threshold: 70% of claims must be attributed.

**FALSIFICATION RULE** [applies at: Stage 3, Stage 5]
When you declare a hypothesis, also state what would falsify it — a specific condition
that, if true, would cause you to reject it. Not a vague hedge. A real criterion.
Why this rule: without a falsification condition, a hypothesis can survive any evidence
because it has no stated failure mode. That's not investigation; it's confirmation.

**CALIBRATION RULE** [applies at: Stage 4, Stage 5]
When you assign confidence levels, use more than one. If you give every finding "Medium"
confidence, you haven't calibrated anything — you've just labeled things.
Why this rule: uniform confidence is the same as no confidence. You must distinguish.
Anti-uniformity guard: if all your confidence ratings are identical, stop and recalibrate.

**SEQUENCING RULE** [applies at: Stage 1, Stage 2, Stage 3, Stage 4, Stage 5]
Evidence comes before hypotheses. Stages 1 and 2 must finish before Stage 3 opens.
Why this rule: a hypothesis formed before evidence gathering is a bias, not a hypothesis.
You need to know what the world looks like before you theorize about it.

All four rules are peers. No rule outranks another. Adding a new rule in the future just
adds a row — nothing else changes.

---

## COVERAGE MAP
*Write this now, before you start Stage 1. Once you begin Stage 1, this map is locked.*
*It tells you, for every stage, which rules are active.*

| Rule          | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|---------------|----|----|----|----|----|
| ATTRIBUTION   | ✓  | ✓  | —  | ✓  | ✓  |
| FALSIFICATION | —  | —  | ✓  | —  | ✓  |
| CALIBRATION   | —  | —  | —  | ✓  | ✓  |
| SEQUENCING    | ✓  | ✓  | ✓  | ✓  | ✓  |

The "—" cells aren't omissions — they're explicit negatives. You'll acknowledge them at each
stage so a reader knows you checked, not that you forgot.

---

## GATE RECORD
*Fill this in before Stage 1 opens, then complete each row as you go.*
*This is the most important table in the brief — if the gates aren't filled, the
campaign isn't complete regardless of how good the evidence is.*

| Stage | Who runs it | To enter, you need... | Did you enter? | When you leave, you must have... | Did you leave cleanly? |
|-------|------------|----------------------|---------------|--------------------------------|----------------------|
| 1 | Websearch Collector | Topic confirmed; campaign started | [ ] | ≥5 external findings with attribution | [ ] |
| 2 | Intelligence Analyst | Stage 1 exit confirmed | [ ] | ≥5 domain concepts with attribution | [ ] |
| 3 | Hypothesis Architect | Both Stage 1 and Stage 2 exit confirmed | [ ] | ≥2 hypotheses with falsification conditions | [ ] |
| 4 | Pattern Analyst | Stage 3 exit confirmed | [ ] | All hypotheses analyzed; ≥2 confidence levels used | [ ] |
| 5 | Synthesis Director | Stage 4 exit confirmed | [ ] | Final brief complete; gate record fully filled | [ ] |

---

## STAGE 1 — Websearch Collector

Before you start Stage 1, check your entry gate:
- Is the topic confirmed? If not, stop and confirm it before proceeding.
- Mark the Stage 1 Entry cell in the gate record: [ Pass / Fail ]

**What to do:** Run prove-websearch for {{TOPIC}}. Find external evidence — data, published
research, market signals, named examples. For each finding, note where you found it.

**What not to do:** Don't form hypotheses here. Don't draw conclusions. You're gathering
raw material, not building a theory.

**Rule check — you're at Stage 1 of 5:**
- ATTRIBUTION RULE: Are at least 70% of your findings attributed to a named source?
  [ Yes / No ] — If No, add attribution before moving on.
- FALSIFICATION RULE: Not active at this stage (evidence stage; no hypotheses).
  Explicit check: N/A.
- CALIBRATION RULE: Not active at this stage (no confidence ratings yet).
  Explicit check: N/A.
- SEQUENCING RULE: Are you in an evidence stage, with hypothesis formation still ahead?
  [ Yes / No ]

When you have ≥5 attributed findings, check your exit gate and mark Stage 1 Exit: [ Pass / Fail ]

---

## STAGE 2 — Intelligence Analyst

Before you start Stage 2, check your entry gate:
- Did Stage 1 exit cleanly? If not, go back and complete Stage 1 first.
- Mark Stage 2 Entry in the gate record: [ Pass / Fail ]

**What to do:** Run prove-intelligence for {{TOPIC}}. Map the intellectual landscape —
key concepts, actors, structural forces, tensions, assumptions. Use Stage 1's web evidence
as context: note where what you found online aligns with or challenges the domain structure
you're mapping.

**What not to do:** Still no hypotheses. Still no conclusions. You're completing the
evidence picture before forming any theories.

**Rule check — Stage 2 of 5:**
- ATTRIBUTION RULE: Are at least 70% of domain concepts attributed ("per intelligence
  review" is fine)? [ Yes / No ]
- FALSIFICATION RULE: Not active here. Explicit check: N/A.
- CALIBRATION RULE: Not active here. Explicit check: N/A.
- SEQUENCING RULE: Is hypothesis formation still ahead (Stage 3 not yet open)?
  [ Yes / No ]

When you have ≥5 attributed domain concepts, mark Stage 2 Exit: [ Pass / Fail ]

---

## STAGE 3 — Hypothesis Architect

Before you start Stage 3, check your entry gate:
- Did Stage 1 exit cleanly? [ Pass / Fail ]
- Did Stage 2 exit cleanly? [ Pass / Fail ]
- Both must be Pass before Stage 3 opens.
- Mark Stage 3 Entry: [ Pass / Fail ]

**What to do:** Now that you have evidence, form hypotheses. For each hypothesis write:
1. The hypothesis itself
2. The falsification condition — what specific thing, if true, would cause you to reject
   this hypothesis? Be concrete. "Evidence doesn't support it" is not a condition.
3. Which Stage 1 or Stage 2 findings ground this hypothesis (cite them by reference)

Note: you're doing this now, not at the start of the campaign, because a hypothesis formed
before evidence is a bias wearing hypothesis clothes. The sequencing is intentional.

**Rule check — Stage 3 of 5:**
- ATTRIBUTION RULE: Not active here (hypotheses cite upstream evidence; attribution is
  upstream). Explicit check: N/A.
- FALSIFICATION RULE: Does every hypothesis carry an explicit falsification condition?
  [ Yes / No ] — If No, add one before closing this stage.
- CALIBRATION RULE: Not active here. Explicit check: N/A.
- SEQUENCING RULE: Were Stages 1 and 2 both confirmed complete before this stage opened?
  [ Yes / No ]

When you have ≥2 hypotheses each with a falsification condition, mark Stage 3 Exit:
[ Pass / Fail ]

---

## STAGE 4 — Pattern Analyst

Before you start Stage 4:
- Did Stage 3 exit cleanly? Mark Stage 4 Entry: [ Pass / Fail ]

**What to do:** Run prove-analysis. Take each hypothesis and look at it against the Stage 1
and Stage 2 evidence. Assign a confidence level — High, Medium, or Low — to each finding.
Keep the calibration rule in mind as you work: if you're about to mark everything "Medium,"
that's a signal to look harder for what's genuinely strong and what's genuinely weak.

**Calibration check:** When you've assigned all confidence levels, look at the distribution.
If every finding has the same level, you haven't calibrated — stop and differentiate before
continuing.

**Rule check — Stage 4 of 5:**
- ATTRIBUTION RULE: Are analysis findings attributed to the evidence they draw on (Stage 1
  or Stage 2 references)? [ Yes / No ]
- FALSIFICATION RULE: Not active here (final verdicts come at Stage 5). Explicit check: N/A.
- CALIBRATION RULE: Do your confidence ratings include at least two distinct levels?
  [ Yes / No ]
- SEQUENCING RULE: Are all your analysis conclusions grounded in S1/S2/S3 evidence only?
  [ Yes / No ]

When all hypotheses are analyzed and you have ≥2 confidence levels, mark Stage 4 Exit:
[ Pass / Fail ]

---

## STAGE 5 — Synthesis Director

Before you start Stage 5:
- Did Stage 4 exit cleanly? Mark Stage 5 Entry: [ Pass / Fail ]

**What to do:** Run prove-synthesize. Pull everything together into a readable brief.
Here's what the brief must include:

**Consensus vs. Conflict** — Look at your Stage 1 (web) and Stage 2 (intelligence) findings
side by side. Where do they agree? Where do they point in different directions? Don't just
list them — name the agreement or the tension explicitly. This is the most important
synthesis move.

**Hypothesis verdicts** — Go through each hypothesis. Look at its falsification condition.
Look at the Stage 4 analysis. State what happened: Supported, Challenged, or Falsified.
This is why you wrote the falsification condition — now you use it.

**Calibration check** — State your confidence distribution across the brief. If it's
uniform, recalibrate here before closing.

**Gaps** — What did this campaign not answer? What would a follow-up investigation need to
run? Be specific — "more research needed" is not a gap; a named missing question is.

**Decision readiness** — One sentence. Either you're ready to proceed, or you name the one
thing that needs to be resolved first. No multi-paragraph hedging. The compression is
the point — if you can't say it in one sentence, you don't know your answer yet.

**Rule check — Stage 5 of 5:**
- ATTRIBUTION RULE: Are ≥70% of synthesis claims attributed to their source stage?
  [ Yes / No ]
- FALSIFICATION RULE: Has a verdict been rendered on every hypothesis's falsification
  condition? [ Yes / No ]
- CALIBRATION RULE: Are ≥2 distinct confidence levels present in the brief? [ Yes / No ]
- SEQUENCING RULE: Are all synthesis conclusions grounded in S1–S4 evidence only?
  [ Yes / No ]

Mark Stage 5 Exit: [ Pass / Fail ]

---

## PUTTING IT ALL TOGETHER

Now assemble the final brief in this order:

1. Title and topic context (what was investigated and why)
2. Governance preamble (the rules and coverage map)
3. Gate record (fully filled — this is your proof the campaign ran correctly)
4. Stage 1 findings (web evidence)
5. Stage 2 findings (intelligence domain model)
6. Stage 3 hypotheses (with falsification conditions)
7. Stage 4 analysis (with confidence levels)
8. Stage 5 synthesis (consensus/conflict, verdicts, gaps, decision readiness)
9. Consolidated invocation audit table (below)

### Consolidated Invocation Audit Table

You logged a rule check at every stage. Consolidate them here.
Row count comes from the coverage map — you can't add or remove rows independently.

| Rule | Stage | Form | Result |
|------|-------|------|--------|
| ATTRIBUTION | S1 | Binary | [ ] |
| ATTRIBUTION | S2 | Binary | [ ] |
| ATTRIBUTION | S4 | Binary | [ ] |
| ATTRIBUTION | S5 | Binary | [ ] |
| FALSIFICATION | S3 | Binary | [ ] |
| FALSIFICATION | S5 | Binary | [ ] |
| CALIBRATION | S4 | Binary | [ ] |
| CALIBRATION | S5 | Binary | [ ] |
| SEQUENCING | S1 | Binary | [ ] |
| SEQUENCING | S2 | Binary | [ ] |
| SEQUENCING | S3 | Binary | [ ] |
| SEQUENCING | S4 | Binary | [ ] |
| SEQUENCING | S5 | Binary | [ ] |
| FALSIFICATION | S1 | Negative | N/A — evidence stage; no hypotheses |
| FALSIFICATION | S2 | Negative | N/A — evidence stage; no hypotheses |
| FALSIFICATION | S4 | Negative | N/A — analysis stage; falsification at S5 |
| CALIBRATION | S1 | Negative | N/A — no confidence ratings at S1 |
| CALIBRATION | S2 | Negative | N/A — no confidence ratings at S2 |
| CALIBRATION | S3 | Negative | N/A — no confidence ratings at S3 |
| ATTRIBUTION | S3 | Negative | N/A — hypotheses reference upstream evidence |
```

---

## Variation Summary

| ID | Axis | Ordering | Primary Structural Element | Register | Key Rubric Bets |
|----|------|----------|---------------------------|----------|-----------------|
| V-01 | Role sequence | Intel → Web → Hypo → Analysis → Synth | Named handoff actors | Formal | C-30, C-14 (rationale for sequencing encoded as principle) |
| V-02 | Output format | Web → Intel → Hypo → Analysis → Synth | Evidence table with `stage` column | Formal | C-28, C-26 (table-native compliance) |
| V-03 | Lifecycle emphasis | Web → Intel → Hypo → Analysis → Synth | Gate record as primary artifact | Formal | C-24, C-25, C-27 (gate-first) |
| V-04 | Sequence + Format | Intel → Web → Hypo → Analysis → Synth | Evidence table with role handoffs | Formal | C-28, C-29, C-30 |
| V-05 | Lifecycle + Register | Web → Intel → Hypo → Analysis → Synth | Gate record with embedded "why" prose | Conversational | C-14, C-31 (negative invocations explicitly explained) |
