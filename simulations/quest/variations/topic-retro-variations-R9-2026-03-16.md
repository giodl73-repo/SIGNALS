## topic-retro Variations — Round 9

---

## V-01: Lifecycle Emphasis

**Variation axis:** Lifecycle emphasis — maximally explicit numbered phases, declared boundary markers, Phase 0 as sealed standalone prior-belief capture  
**Hypothesis:** Structural enforcement of phase sequence (sealed Phase 0, LOCKED Echo before accuracy, explicit boundary declarations) drives pass rate on C-18, C-19, C-23 and reduces post-hoc rationalization of the Echo.

---

```markdown
You are running /topic-retro for [TOPIC].

Produce artifact: `[TOPIC]-topic-retro-[DATE].md`

If an AMEND instruction is present, honor its scope constraint throughout all phases.

---

## Execution Protocol

Execute six numbered phases in strict sequence. Complete and seal each phase before
opening the next. Do not look ahead. Do not revise a sealed phase.

---

### PHASE 0 — Prior Belief Capture

This phase is a sealed standalone phase. It must be completed before any signal
artifact is opened or examined.

State, in three sentences or fewer:
- What the team predicted about this feature's outcomes before signals were gathered
- What signal coverage was assumed to exist
- What prediction accuracy was assumed going in

Label the block exactly:

> **PHASE 0 — PRIOR BELIEF (SEALED)**

Once written, this block is permanently sealed.

**Phase boundary: Phase 0 is now sealed. Prior belief is immutable. Proceed to Phase 1.**

---

### PHASE 1 — Echo Identification

Identify the single most surprising finding from this retrospective — the one thing
that genuinely was not expected at signal-gather time.

Rules:
- Exactly one Echo. Not a list. Not "the main surprises were."
- One sentence. Complete sentence.
- Write it now, before any accuracy scoring.

Label the block exactly:

> **ECHO (LOCKED): [one sentence]**

This Echo is now immutable. Nothing in Phase 2, 3, 4, or 5 may revise it.

**Phase boundary: Echo is now locked. Proceed to Phase 2.**

---

### PHASE 2 — Signal Inventory and Accuracy Scoring

Produce a complete signal inventory. One row per artifact. No artifact may be omitted.

| Namespace | Artifact | Date | Prediction Made at Signal Time | Outcome | Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|----------|------|-------------------------------|---------|------|

Outcome codes: C = Correct, P = Partial, W = Wrong.

Then produce a per-namespace summary:

| Namespace | C | P | W | Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|---|---|---|------|

Overall accuracy judgment: state a ratio and qualitative rating grounded in the
per-namespace scores.

**Conflict audit (mandatory — always emits a result):**
Compare Phase 2 findings against the LOCKED Echo from Phase 1.
- If any accuracy finding creates tension with the Echo: write
  `Conflict detected: [describe tension]. Echo preserved unchanged.`
- If no tension: write
  `Conflict audit: no tension detected between accuracy findings and LOCKED Echo.`

Silence is not a valid result. The audit must emit one of the two forms above.

**Phase boundary: Accuracy scoring complete. Conflict audit recorded. Proceed to Phase 3.**

---

### PHASE 3 — Gap Analysis

Identify signal types that were absent for this topic.

| Gap | Namespace | Signal Type Absent | Concrete Action |
|-----|-----------|--------------------|-----------------|

Each row must name: the namespace, the specific signal type missing, and one
concrete action (skill to run, question to ask, or threshold to set). Generic
advice ("gather more signals") does not satisfy this.

**Phase boundary: Gap analysis complete. Proceed to Phase 4.**

---

### PHASE 4 — Calibration

If a prior retro exists for this team or namespace:
- State whether prediction quality is improving, degrading, or stable.
- Cite the prior retro by name and its overall accuracy score.

If no prior retro exists, emit exactly:

> **Calibration baseline established here.** No prior retro available.
> This retro's overall accuracy of [X] is the forward baseline for future comparison.

Do not skip or mark this section conditional. It must emit an explicit result
in all cases.

**Phase boundary: Calibration recorded. Proceed to Phase 5.**

---

### PHASE 5 — Status-Quo Foil and Echo Feedback

**Foil table** — contrast default assumption against actual finding across exactly
three named dimensions:

| Dimension | Without This Retro | With This Retro |
|-----------|--------------------|-----------------|
| Signal accuracy assumption | | |
| Echo assumption | | |
| Signal design default | | |

**Echo feedback (C-10):**
Translate the LOCKED Echo into a concrete change proposal. Use this form:

> Because the Echo revealed [X], the signal design change is [Y] —
> specifically: [new skill / rubric amendment / threshold adjustment].

---

Save artifact to: `simulations/topic/[TOPIC]-topic-retro-[DATE].md`
Register topic in: `simulations/TOPICS.md`
```

---

## V-02: Output Format

**Variation axis:** Output format — table-heavy, formula embedded in column headers as executable instruction, worked examples inline in headers  
**Hypothesis:** Placing the scoring formula directly in the column header (not prose) forces the model to compute mechanically rather than qualitatively, driving C-11, C-13, C-15 pass rates while keeping prose minimal.

---

```markdown
You are running /topic-retro for [TOPIC].

Produce artifact: `[TOPIC]-topic-retro-[DATE].md`

If an AMEND instruction is present, honor its scope throughout every table.

---

## Output Structure

Produce the following seven tables in order. No section may be skipped.
Prose is limited to one sentence per section heading. All findings live in tables.

---

### Table 0 — Prior Belief Record

Capture prior beliefs before examining any signal artifacts.

| Dimension | Prior Belief (before signals opened) |
|-----------|--------------------------------------|
| Predicted outcome | |
| Assumed signal coverage | |
| Assumed accuracy rate | |

Seal this table before proceeding.

---

### Table 1 — Echo (LOCKED)

Identify the single most surprising finding. One row. One sentence.

| ECHO (LOCKED) |
|---------------|
| [one sentence — the thing genuinely not expected] |

This row is immutable for the rest of this artifact.

---

### Table 2 — Signal Inventory

One row per artifact. No artifact may be omitted.

| Namespace | Artifact | Date | Prediction Made at Signal Time | Outcome (C/P/W) | Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|----------|------|-------------------------------|-----------------|------|

---

### Table 3 — Per-Namespace Accuracy

| Namespace | C | P | W | Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5] | Reliability |
|-----------|---|---|---|------|-------------|

Overall accuracy judgment (one sentence below table): ratio + qualitative rating.

**Conflict audit row** — append to this table:

| CONFLICT AUDIT | — | — | — | — | [Conflict detected: (describe) / No tension detected] |

The audit row is mandatory. Silence is not valid.

---

### Table 4 — Gap Analysis

| Gap # | Namespace | Signal Type Absent | Concrete Action (skill / question / threshold) |
|-------|-----------|--------------------|------------------------------------------------|

---

### Table 5 — Calibration

| Prior Retro | Prior Accuracy Score | This Retro Accuracy | Trend |
|-------------|---------------------|---------------------|-------|

If no prior retro exists, populate with:

| No prior retro | N/A | [this retro score] | Baseline established — forward baseline recorded here |

Do not leave this table empty or absent.

---

### Table 6 — Status-Quo Foil

| Dimension | Without This Retro (default assumption) | With This Retro (actual finding) |
|-----------|-----------------------------------------|----------------------------------|
| Signal accuracy assumption | | |
| Echo assumption | | |
| Signal design default | | |

**Echo feedback** (one sentence below table):

> Because the Echo revealed [X], the signal design change is [Y]: [new skill / rubric amendment / threshold].

---

Save artifact to: `simulations/topic/[TOPIC]-topic-retro-[DATE].md`
Register topic in: `simulations/TOPICS.md`
```

---

## V-03: Inertia Framing

**Variation axis:** Inertia framing — cost-of-inaction foil leads the artifact before accuracy scoring; the status-quo competitor is foregrounded as the structural anchor against which all findings are measured  
**Hypothesis:** Opening with "without this retro, we would assume..." before examining signals makes the foil an active framing device rather than an appendix, driving C-20 and C-24 pass rates and preventing accuracy analysis from being reported in isolation.

---

```markdown
You are running /topic-retro for [TOPIC].

Produce artifact: `[TOPIC]-topic-retro-[DATE].md`

If an AMEND instruction is present, honor its scope throughout.

---

## Execution Protocol

This retro opens with the status-quo foil — what the team would have assumed had
this retrospective never been run. Every finding that follows is measured against
that baseline. The foil is not an appendix; it is the frame.

---

## Step 1 — Prior Belief (before signals)

Before opening any signal artifact, state in two to three sentences:
what outcomes, coverage, and accuracy the team would have assumed by default
if no signals had been gathered and no retro had been run.

Label:

> **Prior Belief (SEALED):** [2-3 sentences]

---

## Step 2 — Status-Quo Foil (cost-of-inaction)

Define the inaction baseline across three named dimensions. This table is filled
from prior belief and domain default — not from signals yet to be examined.

| Dimension | Without This Retro (status-quo assumption) | With This Retro (TBD — fill in Step 5) |
|-----------|--------------------------------------------|----------------------------------------|
| Signal accuracy assumption | [fill now] | [fill in Step 5] |
| Echo assumption | [fill now] | [fill in Step 5] |
| Signal design default | [fill now] | [fill in Step 5] |

Note: the right column is intentionally empty. You will return to complete it in Step 5.

---

## Step 3 — Echo (LOCKED, before accuracy)

With the foil baseline defined, now identify the single most surprising finding —
the thing that most sharply breaks from the status-quo assumptions recorded in Step 2.

Exactly one Echo. One sentence.

> **ECHO (LOCKED): [one sentence]**

This is immutable. Accuracy scoring in Step 4 may not revise it.

---

## Step 4 — Signal Inventory and Accuracy Scoring

**Signal inventory** — one row per artifact, none omitted:

| Namespace | Artifact | Date | Prediction at Signal Time | Outcome (C/P/W) | Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|----------|------|--------------------------|-----------------|------|

**Per-namespace accuracy:**

| Namespace | C | P | W | Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|---|---|---|------|

Overall accuracy: one sentence — ratio plus qualitative rating.

**Conflict audit (mandatory):**
Does any accuracy finding create tension with the LOCKED Echo?
Emit exactly one of:
- `Conflict detected: [describe]. Echo preserved unchanged.`
- `Conflict audit: no tension detected.`

**Gap analysis** — signals absent from this topic:

| Namespace | Signal Type Absent | Concrete Action |
|-----------|--------------------|-----------------|

---

## Step 5 — Complete the Foil and Echo Feedback

Return to the foil table from Step 2. Fill in the right column ("With This Retro")
for all three dimensions based on actual findings from Step 4.

Then state the Echo feedback — what the LOCKED Echo means for future signal design:

> Because the Echo revealed [X], and the status-quo default would have assumed [Y]
> (see foil: Echo assumption row), the signal design change is [Z]:
> [new skill / rubric amendment / threshold].

---

## Step 6 — Calibration

Compare this retro's accuracy to a prior retro for this team or namespace.

If a prior retro exists: name it, cite its accuracy score, state the trend
(improving / degrading / stable).

If no prior retro exists:

> **Calibration baseline established here.** No prior retro available.
> This retro's overall accuracy of [X] is the forward baseline.

---

Save artifact to: `simulations/topic/[TOPIC]-topic-retro-[DATE].md`
Register topic in: `simulations/TOPICS.md`
```

---

## V-04: Phrasing Register

**Variation axis:** Phrasing register — direct imperative voice, short commands, minimal explanation of rationale, model told exactly what to produce with no hedging language  
**Hypothesis:** Removing explanatory prose from instructions and issuing short direct commands reduces model hallucination of extra Echoes (C-04) and forces the unconditional conflict audit (C-16) to emit rather than be skipped.

---

```markdown
You are running /topic-retro for [TOPIC].

Output file: `[TOPIC]-topic-retro-[DATE].md`

Honor any AMEND scope restriction. If AMEND is absent, cover all signals.

---

Do these steps in order. Do not skip any step.

---

**Step 1.** Write a Prior Belief block. Do it before you look at any signals.
Three sentences. What was assumed about outcomes, coverage, and accuracy before
signals were gathered. Label it `PHASE 0 — PRIOR BELIEF (SEALED)`. Seal it.

---

**Step 2.** Write the Echo. One sentence. The single most surprising thing.
Not a list. Not two things. One. Label it `ECHO (LOCKED)`. It cannot change
after this point. Write it now, before you touch the accuracy tables.

---

**Step 3.** Build the signal inventory table. Every artifact. No exceptions.

Columns: Namespace | Artifact | Date | Prediction Made at Signal Time | Outcome | Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5]

Outcome = C (Correct), P (Partial), or W (Wrong).

---

**Step 4.** Build the per-namespace accuracy table.

Columns: Namespace | C | P | W | Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5]

Write one sentence overall accuracy verdict: a ratio and a qualitative label.

---

**Step 5.** Run the conflict audit. Do not skip this. It always emits a result.

Look at your accuracy findings. Compare them to the LOCKED Echo.

Write one of these two lines, exactly:
- `Conflict detected: [describe the tension]. Echo preserved unchanged.`
- `Conflict audit: no tension detected.`

There is no third option. Silence is wrong.

---

**Step 6.** Build the gap table. What signal types were absent?

Columns: Namespace | Signal Type Absent | Concrete Action

Concrete action = a specific skill to run, question to ask, or threshold to set.
"Gather more data" is not a concrete action.

---

**Step 7.** Write the foil table. Three rows. Exactly three.

Columns: Dimension | Without This Retro | With This Retro

Rows:
- Signal accuracy assumption
- Echo assumption
- Signal design default

---

**Step 8.** Write the Echo feedback. One or two sentences.

Complete this sentence: "Because the Echo revealed [X], the signal design change is [Y]."
Name either a new skill, a rubric amendment, or a threshold adjustment.

---

**Step 9.** Write the calibration section.

If you have a prior retro to compare: name it, give its accuracy score, state the trend.

If you have no prior retro: write this exactly:
`Calibration baseline established here. No prior retro available. This retro's
overall accuracy of [X] is the forward baseline.`

Do not skip this section. Do not say "N/A." Emit a result.

---

Save to: `simulations/topic/[TOPIC]-topic-retro-[DATE].md`
Register in: `simulations/TOPICS.md`
```

---

## V-05: Combined (Phase Structure + Table Format + Inertia Framing)

**Variation axis:** Combined — V-01 phase structure with explicit boundary markers + V-02 formula-in-column-header table design + V-03 foil-first inertia framing  
**Hypothesis:** Combining sealed phases (C-18, C-19, C-23), formula-in-header tables (C-11, C-13, C-15), and foil-before-signals positioning (C-20, C-24) produces the highest overall rubric pass rate by enforcing all three structural axes simultaneously.

---

```markdown
You are running /topic-retro for [TOPIC].

Produce artifact: `[TOPIC]-topic-retro-[DATE].md`

If an AMEND instruction is present, honor its scope throughout all phases and tables.

---

## Execution Protocol

Seven phases in strict sequence. Each phase is sealed at its boundary.
A sealed phase cannot be revised by any later phase.
All scoring lives in tables; prose is limited to one sentence per phase header.

---

### PHASE 0 — Prior Belief and Status-Quo Foil (SEALED STANDALONE PHASE)

This phase must be completed before any signal artifact is opened.

**Prior belief table** — fill before signals:

| Dimension | Prior Belief (before signals opened) |
|-----------|--------------------------------------|
| Predicted outcome | |
| Assumed signal coverage | |
| Assumed accuracy rate | |

**Status-quo foil table** — fill the left column now; right column reserved for Phase 6:

| Dimension | Without This Retro (status-quo default) | With This Retro (fill in Phase 6) |
|-----------|----------------------------------------|-----------------------------------|
| Signal accuracy assumption | [fill now] | — |
| Echo assumption | [fill now] | — |
| Signal design default | [fill now] | — |

**Phase boundary: Phase 0 is sealed. Prior belief and status-quo defaults are
immutable. Proceed to Phase 1.**

---

### PHASE 1 — Echo (LOCKED)

Identify the single most surprising finding — the finding that most sharply
departs from the status-quo defaults recorded in Phase 0.

Exactly one Echo. One sentence. No list.

| ECHO (LOCKED) |
|---------------|
| [one sentence] |

**Phase boundary: Echo is now locked. No subsequent phase may revise it.
Proceed to Phase 2.**

---

### PHASE 2 — Signal Inventory

One row per artifact. No artifact may be omitted.

| Namespace | Artifact | Date | Prediction Made at Signal Time | Outcome (C/P/W) | Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|----------|------|-------------------------------|-----------------|------|

Outcome: C = Correct, P = Partial, W = Wrong.

**Phase boundary: Signal inventory sealed. Proceed to Phase 3.**

---

### PHASE 3 — Per-Namespace Accuracy and Conflict Audit

**Per-namespace accuracy:**

| Namespace | C | P | W | Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5] | Reliability |
|-----------|---|---|---|------|-------------|

Overall accuracy verdict (one sentence): ratio + qualitative label.

**Conflict audit — mandatory, always emits:**

Append a final row to the per-namespace table:

| CONFLICT AUDIT | — | — | — | — | [Conflict detected: (describe tension). Echo preserved. / No tension detected.] |

Silence is not a valid entry. The audit row must be present.

**Phase boundary: Accuracy and conflict audit complete. Proceed to Phase 4.**

---

### PHASE 4 — Gap Analysis

| Gap # | Namespace | Signal Type Absent | Concrete Action (skill / question / threshold) |
|-------|-----------|--------------------|------------------------------------------------|

Each concrete action must be specific. Generic advice does not satisfy this phase.

**Phase boundary: Gap analysis complete. Proceed to Phase 5.**

---

### PHASE 5 — Calibration

If a prior retro exists:

| Prior Retro | Prior Accuracy | This Retro Accuracy | Trend |
|-------------|---------------|---------------------|-------|

If no prior retro exists:

| Prior Retro | Prior Accuracy | This Retro Accuracy | Trend |
|-------------|---------------|---------------------|-------|
| None | N/A | [score] | Baseline established — forward baseline recorded here |

This table must be present and populated. Do not skip. Do not emit N/A without the
baseline record row.

**Phase boundary: Calibration recorded. Proceed to Phase 6.**

---

### PHASE 6 — Foil Completion and Echo Feedback

Return to the foil table from Phase 0. Fill the right column for all three rows
using actual findings from Phases 2–4.

| Dimension | Without This Retro | With This Retro |
|-----------|--------------------|-----------------|
| Signal accuracy assumption | [from Phase 0] | [from Phase 3] |
| Echo assumption | [from Phase 0] | [from Phase 1] |
| Signal design default | [from Phase 0] | [from Phase 4] |

**Echo feedback:**

> Because the Echo revealed [X], and the status-quo default would have assumed [Y]
> (foil: Echo assumption row), the signal design change is [Z]:
> [new skill name / rubric amendment description / threshold specification].

**Phase boundary: Foil complete. Echo feedback recorded. Proceed to Phase 7.**

---

### PHASE 7 — Artifact Seal

Confirm: Phase 0 prior belief was written before signals. Echo was written before
accuracy. Conflict audit emitted a result. Calibration emits a result (or baseline
record). Foil table has three named dimensions with both columns populated.

Emit one line:

> Retro complete. [N] signals reviewed. Overall accuracy: [X]. Echo: preserved
> through all phases. Calibration: [baseline established / trend: improving /
> degrading / stable].

---

Save artifact to: `simulations/topic/[TOPIC]-topic-retro-[DATE].md`
Register topic in: `simulations/TOPICS.md`
```

---

## Axis Coverage Map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-04 Exactly one Echo | phase rule | table (one row) | step rule | explicit command | table (one row) |
| C-11 Numeric formula | header | **header** | header | header | header |
| C-13 Formula in header | yes | **yes** | yes | yes | yes |
| C-15 Worked example in header | yes | **yes** | yes | yes | yes |
| C-16 Unconditional conflict audit | phase rule | audit row | step rule | explicit command | mandatory row |
| C-17 LOCKED label | yes | yes | yes | yes | yes |
| C-18 Named phases | **yes** | no (tables) | steps | steps | **yes** |
| C-19 Boundary markers | **yes** | no | no | no | **yes** |
| C-20 Status-quo foil | phase 5 | table 6 | **leads** | step 7 | **phase 0 + 6** |
| C-23 Phase 0 sealed standalone | **yes** | no | no | no | **yes** |
| C-24 Three-dimension foil | 3 rows | 3 rows | **3 rows** | 3 rows | **3 rows** |
| C-25 Calibration baseline | phase 4 | table 5 | step 6 | step 9 | phase 5 + row |
