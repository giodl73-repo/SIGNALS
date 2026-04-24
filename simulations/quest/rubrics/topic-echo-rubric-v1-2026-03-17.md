---
skill: quest-rubric
skill_target: topic-reflect
date: 2026-03-17
version: 1
---

# Rubric: topic-echo (topic-reflect)

Scoring rubric for the `topic-echo` skill — unexpected findings synthesis.
The skill answers one question: *What did we learn that we did not expect?*
The output is the institutional memory for the next team that walks this path.

---

## Composite Score Formula

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 2 * 10)
```

**Golden threshold:** all essential criteria pass AND composite >= 80.

Scoring table: each essential = 12 pts, each recommended = 10 pts, each aspirational = 5 pts.

---

## Essential Criteria

*Must all pass. Without these the output is not useful.*

### C-01 — Surprise Orientation
**Weight:** essential
**Category:** correctness
**Text:** Every Stage 4 surprise entry is a genuine deviation from a named prior belief
(B-#) and is not merely a summary of what a signal found. An entry that could have been
written before any signals were gathered fails this criterion.
**Pass condition:** Every surprise row in Stage 4 references a specific belief (B-#) from
Stage 1. At least one entry contradicts, not merely confirms, the opening model. No entry
reads as a restatement of the signal artifact summary without invoking a prior belief.

---

### C-02 — Symmetric Contract Present
**Weight:** essential
**Category:** correctness
**Text:** The output contains both halves of the Symmetric Contract: an opening collective
baseline (Stage 1) and a closing collective synthesis (Stage 6). Without both halves the
architecture is broken and the echo is incomplete.
**Pass condition:** Stage 1 contains an opening model (2+ sentences), an epistemic profile
entry, and at least 3 belief rows. Stage 6 contains the collective verdict table with
revision direction, epistemic dimensions shifted, and a COHERENT / CONTRADICTORY /
FOREKNOWLEDGE-FLAGGED verdict. Both stages are present and not empty.

---

### C-03 — Signal Tracing
**Weight:** essential
**Category:** correctness
**Text:** Every surprise in Stage 4 is traceable to a named signal artifact. Without
provenance the surprise cannot be verified by the next team and institutional memory is
unanchored.
**Pass condition:** The Signal Source column in Stage 4 contains a non-empty artifact
reference (name and/or namespace and/or date) for every row. No row may contain only
generic text such as "signal sweep" or "multiple sources."

---

### C-04 — Design Impact Specificity
**Weight:** essential
**Category:** depth
**Text:** Each surprise names a specific component, decision, or constraint it impacts.
Vague references ("the system", "the design", "our approach") do not constitute a design
impact and render the surprise non-actionable.
**Pass condition:** The Design Impact column in every Stage 4 row references a named
component, API, flow, schema, or design decision. No row may contain only "the system" or
equivalently vague language.

---

### C-05 — Adversarial Gate Executed
**Weight:** essential
**Category:** correctness
**Text:** Stage 3 is present and evaluates each deviation on all five checks (named prior
belief, traceable artifact, design-relevant, genuinely unexpected, flat-statement test).
Without this filter, entry inflation — recording confirmations as surprises — goes
unchecked and corrupts the output.
**Pass condition:** The Stage 3 table is present with all five check rows and at least one
deviation column. Each deviation column carries a VALID or INVALID verdict. GATE-CONFIRMED
or GATE-REJECTED tokens are present for each deviation. No deviation passes straight to
Stage 4 without a Stage 3 verdict.

---

## Recommended Criteria

*Output is better with these. Together they raise the composite score by up to 30 points.*

### C-06 — Epistemic Dimension Compliance
**Weight:** recommended
**Category:** correctness
**Text:** All Epistemic Dimension cells in Stage 1, Stage 4, and Stage 6 use only the five
canonical names declared in the Vocabulary Declaration. Synonym use causes cross-artifact
aggregation to fail.
**Pass condition:** Every Epistemic Dimension cell contains one of: `falsifiability`,
`observability`, `causal specificity`, `predictive precision`, `scope constraints`. None
of the excluded synonyms (`testability`, `confirmability`, `data-backed`, `verifiability`,
`measurability`) appear in any Epistemic Dimension cell.

---

### C-07 — Minimum Surprise Coverage
**Weight:** recommended
**Category:** coverage
**Text:** The echo surfaces at least 2 GATE-CONFIRMED surprises. A single surprise cannot
support the rank+cluster stage or the closing collective synthesis. The spec requires a
minimum of 2 rows.
**Pass condition:** Stage 4 contains at least 2 completed rows, each with a corresponding
GATE-CONFIRMED token in Stage 3. If fewer than 2 pass the gate, the spec requires
extending the sweep — the criterion fails if the sweep was not extended.

---

### C-08 — Cluster Map Actionability
**Weight:** recommended
**Category:** behavior
**Text:** The Stage 5 cluster map populates the Next Team / Skill column with at least one
concrete forward-looking routing recommendation. This is what converts the echo from a
historical record into institutional memory the next team can act on.
**Pass condition:** At least one cluster row in Stage 5 has a non-empty Next Team / Skill
entry that names a specific skill (e.g., `/draft-spec`, `/prove-hypothesis`) or team role
(e.g., "API contract owner"). Generic entries such as "follow up" or "investigate" do not
pass.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

### C-09 — Token Protocol Integrity
**Weight:** aspirational
**Category:** format
**Text:** GATE-CONFIRMED tokens use the naming format that identifies Stage 4 by name
(not merely "routes to Stage 4"), and COMMIT-ENTRY tokens are present at row granularity
in Stage 4. This prevents drift collapse and citation collapse — the two failure modes the
spec guards against with token-level enforcement.
**Pass condition:** Every GATE-CONFIRMED token follows the format
`GATE-CONFIRMED-[N]: VALID -- Stage 4.` (stage named, not described). Every Stage 4 row
is followed by a `COMMIT-ENTRY-[N]: entry committed.` token before the next row begins.
COMMIT-STAGE tokens (1 through 6) are all present in order.

---

### C-10 — Foreknowledge Integrity
**Weight:** aspirational
**Category:** depth
**Text:** Stage 6 explicitly evaluates the implausible-foreknowledge signal and records
CLEAR or FLAGGED. A FLAGGED verdict halts artifact writing and identifies the belief(s)
responsible. This safeguards the echo as reliable institutional memory — a set of beliefs
that collectively imply foreknowledge of the outcome is not a credible surprise record.
**Pass condition:** Stage 6 contains a non-empty Implausible-foreknowledge signal row with
either CLEAR or FLAGGED. If FLAGGED, the output does not write the artifact and instead
names the belief(s) responsible for the flag.

---

## Criteria Summary

| ID   | Text (short)                        | Weight        | Category    | Points |
|------|-------------------------------------|---------------|-------------|--------|
| C-01 | Surprise orientation — B-# trace    | essential     | correctness | 12     |
| C-02 | Symmetric Contract — Stage 1 + 6    | essential     | correctness | 12     |
| C-03 | Signal tracing — named artifact     | essential     | correctness | 12     |
| C-04 | Design impact — specific component  | essential     | depth       | 12     |
| C-05 | Adversarial gate — 5 checks present | essential     | correctness | 12     |
| C-06 | Epistemic dimension compliance      | recommended   | correctness | 10     |
| C-07 | Minimum 2 surprises                 | recommended   | coverage    | 10     |
| C-08 | Cluster map — next-team routing     | recommended   | behavior    | 10     |
| C-09 | Token protocol integrity            | aspirational  | format      | 5      |
| C-10 | Foreknowledge signal evaluated      | aspirational  | depth       | 5      |

**Maximum score:** 100
**Golden threshold:** all C-01 through C-05 pass AND composite >= 80
