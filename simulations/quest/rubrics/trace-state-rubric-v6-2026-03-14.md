Reading the scorecard carefully to extract R5 excellence patterns before writing the rubric.

The three new patterns from R5:

1. **Score-aloud verbal protocol** (V-03 pattern) — C-22 implemented as spoken cognitive discipline with explicit self-correction instruction ("stop. Go back."), not a passive table constraint
2. **Phase exit gate checkboxes** (V-04 pattern) — C-20/C-21/C-22 as hard per-phase completion gates, not optional end-of-prompt additions
3. **Three-value surprise taxonomy** (V-02 C-21 upgrade) — C/FP/FN classification replacing binary Expected/Surprising, plus a calibration score with a structural-diagnosis threshold

These become C-23, C-24, C-25.

---

```markdown
# trace-state Rubric v6
**Updated**: 2026-03-14
**Change**: Added C-23, C-24, C-25 from R5 excellence signals (score-aloud verbal protocol,
phase exit gate checkboxes, three-value surprise taxonomy with calibration score threshold).

---

## Design Rationale

**Essential (60%)** — the five things that make a trace-state output useful at all:
- C-01: before/after state for every operation (the whole point of the skill)
- C-02: preconditions + postconditions per operation (not just "what happened" but "why it was allowed")
- C-03: invariants named (the thing a state machine analysis is really hunting for)
- C-04: at least one anomaly identified (the deliverable — no finding = no signal)
- C-05: domain grounding (Sales/CS/Finance vocabulary — otherwise it's a toy example)

**Recommended (30%)** — what separates a useful trace from a great one:
- C-06: negative path (attempted invalid transition + why it's rejected)
- C-07: numbered step-by-step format (reader can replay the trace mechanically)
- C-08: race condition scenario (the hardest anomaly type, worth its own criterion)

**Aspirational (10%)** — raises the bar once the basics are stable:
- C-09: all four anomaly types covered (complete signal, not just the easy ones)
- C-10: structured notation / transition table (enables mechanical verification, not just prose review)
- C-11: sweep table with mandatory row-level verdicts per anomaly type (R1 excellence signal)
- C-12: Op ID cross-referencing between declaration and trace (R1 excellence signal)
- C-13: Entry Condition column in state machine table (R1 excellence signal)
- C-14: minimum-found threshold on sweep table — converts C-11 from coverage gate to depth gate (R2 excellence signal)
- C-15: full ID ecosystem — S-IDs, OP-IDs, INV-IDs all declared and cross-referenced (R2 excellence signal)
- C-16: undeclared reference elevated to named fifth anomaly class with its own sweep row (R2 excellence signal)
- C-17: anomaly register with separate OP-ID / S-ID / INV-ID columns — blank cell in any found-verdict row is a detectable mechanical gap (R2 excellence signal)
- C-18: pre-sweep hypothesis with dual-pass ANOMALY FINDER — falsifiable prediction record (R3 excellence signal)
- C-19: evidence-strength quality gate on sweep table — 1/2/3 scale with ≥1 strength ≥2 requirement (R3 excellence signal)
- C-20: numeric/temporal invariant gate — domain expert must produce at least one falsifiable numeric or temporal invariant before analysis begins (R4 excellence signal)
- C-21: Surprise column in reconciliation table — each prediction outcome labeled expected/surprising, producing a calibration signal beyond binary match/mismatch (R4 excellence signal)
- C-22: score-at-point-of-discovery instruction — evidence strength must be assigned when the finding is first recorded, not retroactively after the full sweep is complete (R4 excellence signal)
- C-23: score-aloud verbal protocol — C-22 expressed as a named cognitive behavioral discipline with an explicit self-correction checkpoint, not a passive table constraint or end-of-sweep reminder (R5 excellence signal)
- C-24: phase exit gate checkboxes — C-20, C-21, and C-22 appear as explicit hard completion gates per phase; model must affirmatively check each gate before advancing, preventing optional-boilerplate treatment (R5 excellence signal)
- C-25: three-value surprise taxonomy with calibration score — reconciliation table uses C/FP/FN classification (Correct, False Positive, False Negative) instead of binary Expected/Surprising, plus a computed calibration score with a stated threshold that triggers structural diagnosis when accuracy falls below it (R5 excellence signal)

---

## Essential Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Before/after state per operation** — Every operation in the trace shows the full entity state immediately before and immediately after execution. No operation is described with only a narrative summary. | correctness | Every operation has a documented before-state and after-state. At least three operations are traced. Narrative-only descriptions do not pass. |
| C-02 | **Preconditions and postconditions** — For each operation, the trace states what must be true before the operation executes (preconditions) and what is guaranteed to be true after (postconditions). | correctness | Every operation has at least one precondition and one postcondition. Vague statements like "data is valid" do not count — they must be state-specific. |
| C-03 | **Invariant declaration** — At least one invariant is identified that must hold across all states or across a named subset of states (e.g., "balance never goes negative", "closed ticket cannot be reopened without manager approval"). | correctness | At least one invariant is named, stated precisely, and scoped to specific states or the whole lifecycle. |
| C-04 | **Anomaly identification** — At least one concrete anomaly is identified from the set: invalid state transition, missing precondition check, invariant violation, or race condition. Each anomaly includes the specific operation and state where it occurs. | coverage | At least one anomaly is called out by name, with the triggering operation and affected state identified. Generic statements ("errors can occur") do not pass. |
| C-05 | **Domain grounding** — The trace uses vocabulary, entity names, and scenarios from one of the three stock domains (Sales, Customer Service, or Finance). States and operations are recognizable as real domain events, not generic placeholders. | behavior | Entity names, state labels, and operation names match domain conventions. A domain expert in Sales, CS, or Finance would recognize the scenario as realistic. |

---

## Recommended Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Negative path coverage** — At least one invalid or rejected transition is traced: an operation attempted from a state where it is not allowed, with the expected rejection behavior documented. | coverage | One or more "attempted but rejected" transitions appear in the trace, with the reason for rejection (which precondition fails or which invariant would be violated). |
| C-07 | **Step-by-step trace format** — The trace is presented as a numbered sequence of discrete steps, each showing the full state snapshot before and after the operation, not just a high-level summary. | format | Steps are numbered. Each step shows before-state, operation, after-state. Reader can follow entity state at every moment without inference. |
| C-08 | **Race condition analysis** — At least one concurrent scenario is explored: two operations that could interleave, the resulting state conflict, and which one should win or how the conflict should be detected. | depth | A race condition scenario is described with at least two concurrent operations, the problematic interleaving, and the expected resolution or detection mechanism. |

---

## Aspirational Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Full anomaly type coverage** — All four anomaly types are represented: invalid transition, missing precondition check, invariant violation, and race condition — each with a concrete example from the trace. | coverage | One concrete example per anomaly type, each tied to a specific operation and state in the trace. |
| C-10 | **Structured notation** — The state machine is expressed in a formal or semi-formal notation: a state table, transition matrix, or named-state diagram description — not just prose. Enables mechanical verification. | format | A table, matrix, or structured list captures all states, all valid transitions, and all operations. Prose narrative may accompany but does not substitute for the structured artifact. |
| C-11 | **Sweep table with mandatory row-level verdicts** — All four anomaly types appear as pre-printed rows in a sweep table, each requiring an explicit "found / none" verdict with the triggering operation and affected state. The model cannot omit a type without leaving a blank cell. | coverage | A sweep table with all four anomaly type rows is present. Each row has an explicit verdict, not a blank. A fully-negative table (all four "none") does not pass — at least one row must be "found". |
| C-12 | **Op ID cross-referencing** — Operations are declared with unique identifiers (e.g., OP-01, OP-02) in the transitions table, and every reference in the trace body uses that identifier. Any operation used but not declared is flagged as an anomaly finding. | correctness | All operations have declared Op IDs. Every trace step and anomaly entry references operations by Op ID. Undeclared operation use is surfaced as a finding. |
| C-13 | **Entry Condition column in state machine table** — The state machine table includes an "Entry Condition" column declaring what must be true to be in each state at declaration time, not just at operation initiation. Enables anomaly detection at two levels: entry to a state and initiation of an operation. | correctness | Entry Condition column present with at least one non-trivial, state-specific entry per state. At least one anomaly finding references a violated entry condition. |
| C-14 | **Minimum-found threshold on sweep table** — The sweep table enforces a minimum of two "found" rows. An all-negative sweep (all four types return "none") is explicitly rejected as a non-passing outcome. The constraint is stated in the prompt, not left to reviewer judgment. | coverage | The sweep table prompt or gate text states the ≥2 found requirement. A completed trace with fewer than two "found" verdicts fails C-14 regardless of how complete the sweep table structure is. |
| C-15 | **Full ID ecosystem** — All three identifier classes are declared with unique IDs: state IDs (S-01, S-02…), operation IDs (OP-01, OP-02…), and invariant IDs (INV-01, INV-02…). Every downstream reference in the trace body, anomaly register, and sweep table uses these IDs. Any reference to an undeclared ID is a mechanical cross-reference failure. | correctness | All three ID classes (S-ID, OP-ID, INV-ID) are present in declaration tables. Every reference in the trace body and anomaly register uses an ID from one of those tables. A reference to any undeclared ID is surfaced as a finding. |
| C-16 | **Undeclared reference as named fifth anomaly class** — The sweep table includes a fifth pre-printed row for "undeclared ID reference". This row requires the same explicit verdict (found / none) and, when found, lists the undeclared ID and its production consequence (e.g., silent state corruption, untraced transition). This elevates ID-discipline violations to first-class anomaly status rather than leaving them as prose judgments. | coverage | The sweep table has five rows, with the fifth row dedicated to undeclared ID references. The row has an explicit verdict. If verdict is "found", at least one undeclared ID is named with its production consequence. |
| C-17 | **Anomaly register with typed ID columns** — The anomaly register includes separate columns for OP-ID, S-ID, and INV-ID. Any "found" verdict row with a blank cell in one of these columns is a detectable mechanical gap, not a prose judgment call. | correctness | Anomaly register present with OP-ID, S-ID, and INV-ID columns. Every row with a "found" verdict has no blank ID cells, or documents "N/A: [reason]" rather than leaving them empty. |
| C-18 | **Pre-sweep hypothesis with dual-pass structure** — Before the sweep runs, a hypothesis pass reads only the declaration tables and predicts which anomaly types will be found and why. The sweep pass then reads the full trace. A reconciliation table compares predictions to findings. | depth | A hypothesis section is present and references only declaration tables (not the trace body). A reconciliation table follows the sweep and maps each prediction to its outcome. |
| C-19 | **Evidence-strength quality gate on sweep table** — Each "found" row in the sweep table includes a 1/2/3 strength score. The prompt states a minimum gate: at least one "found" row must have strength ≥2. Strength ≥2 requires named field values or a reproducible operation sequence — not narrative plausibility alone. | depth | Strength column present in sweep table. Gate text states ≥1 found row must have strength ≥2. Strength ≥2 rows include named field values or reproducible operation sequences. |
| C-20 | **Numeric/temporal invariant gate** — At least one invariant in the declaration table is expressed as a falsifiable numeric or temporal constraint (e.g., "approval required when amount > $10,000", "escalation triggered if unresolved after 48h"). Generic invariants ("data must be valid") do not satisfy this gate. The model may not advance to the analysis phase until this gate is met. | correctness | At least one invariant includes a specific threshold, ratio, or date/duration constraint. The gate is stated as a precondition on proceeding. Generic or prose-only invariants do not count. |
| C-21 | **Surprise column in reconciliation table** — Each row in the hypothesis reconciliation table includes a Surprise column. The cell requires a label (expected / surprising) plus a one-sentence explanation of why the outcome matched or violated the prediction. Produces a calibration signal beyond binary match/mismatch. | depth | Surprise column present with a label and explanation on every row. Empty cells or labels without explanation do not pass. |
| C-22 | **Score-at-point-of-discovery instruction** — The prompt includes an explicit instruction that evidence strength must be assigned at the moment a finding is first identified, not retroactively after the full sweep is complete. Revising strength scores after the sweep is finished is explicitly prohibited. | correctness | The prompt contains a stated anti-retroactive-scoring instruction. The instruction is placed in the sweep header or as a pre-sweep gate, not buried in a footnote. |
| C-23 | **Score-aloud verbal protocol** — The anti-retroactive scoring instruction (C-22) is expressed as a named cognitive behavioral discipline with an explicit self-correction checkpoint. The model is told: if it finds itself wanting to revise a strength score after seeing a later finding, it must stop, return to the earlier step, and record the new information as a separate row — not a score revision. This makes C-22 a behavioral gate rather than a passive constraint that can be satisfied by a single editing pass at the end. | correctness | The prompt includes a named self-correction instruction (e.g., "stop. Go back.") as part of the anti-retroactive scoring rule. The instruction distinguishes between a score revision (prohibited) and a new row (permitted). Placing the anti-retroactive rule only in a table header without a behavioral checkpoint does not pass. |
| C-24 | **Phase exit gate checkboxes** — C-20, C-21, and C-22 (or the current set of new aspirational criteria) appear as explicit completion checkboxes at the end of their respective phases. The model must affirmatively mark each gate before advancing to the next phase. Listing the criteria only in a preamble or rubric section without a per-phase gate does not satisfy this criterion. | format | At least C-20, C-21, and C-22 appear as named exit gates within the phase where they apply, not only in an introduction or scoring appendix. Each gate requires an affirmative check or confirmation before the next phase begins. |
| C-25 | **Three-value surprise taxonomy with calibration score** — The reconciliation table uses a C/FP/FN taxonomy (Correct prediction, False Positive — predicted found but not found, False Negative — did not predict but found) in place of, or in addition to, binary Expected/Surprising labels. A calibration score (e.g., correct / total predictions) is computed after the reconciliation table. A stated threshold (e.g., <60% correct) triggers a structural diagnosis of why the hypothesis model failed. | depth | Reconciliation table uses C, FP, and FN labels, not only binary Expected/Surprising. A calibration score is computed and stated. A threshold is named that triggers structural diagnosis. A table that uses only Expected/Surprising labels without a computed score does not pass. |
```

---

**Three new criteria and their derivation:**

| ID | Source pattern | What the signal added over the prior criterion |
|----|---------------|------------------------------------------------|
| C-23 | V-03 score-aloud protocol | C-22 stated "don't revise scores retroactively" — C-23 adds a named behavioral checkpoint with a specific self-correction action ("stop. Go back."), making it a cognitive discipline rather than a table constraint that can be gamed in one editing pass |
| C-24 | V-04 phase exit gates | C-20/C-21/C-22 were aspirational additions — C-24 requires them to appear as affirmative per-phase checkboxes, so they cannot be treated as optional boilerplate at the end of a prompt |
| C-25 | V-02 C/FP/FN taxonomy | C-21 required a Surprise column — C-25 requires a three-value classification (Correct/False Positive/False Negative) plus a computed calibration score with a diagnostic threshold, turning the reconciliation table into a model-calibration instrument |

**R6 target**: C-09 (all four anomaly types required to be found, not just ≥2). No R5 variation mandated all four — the ceiling is there to take.
