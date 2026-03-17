Three new criteria from the R4 signals:

- **C-20** — Numeric/temporal invariant gate (Signal 1)
- **C-21** — Surprise column in reconciliation table (Signal 2)
- **C-22** — Score at point of discovery, anti-retroactive (Signal 3)

```markdown
# trace-state Rubric v5
**Updated**: 2026-03-14
**Change**: Added C-20, C-21, C-22 from R4 excellence signals (numeric/temporal invariant gate,
Surprise column in reconciliation table, score-at-point-of-discovery anti-retroactive instruction).

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
| C-17 | **Anomaly register with full ID columns** — The anomaly register includes separate OP-ID, S-ID, and INV-ID columns in addition to the anomaly description. A blank cell in any found-verdict row is a detectable mechanical gap; "N/A: [reason]" is required where genuinely inapplicable. | correctness | Register columns include A-ID, Type, OP-ID, S-ID, INV-ID, Description, and Severity. No found-verdict row has a blank ID cell — either a declared ID or "N/A: [reason]" appears in every cell. |
| C-18 | **Pre-sweep hypothesis with dual-pass ANOMALY FINDER** — The ANOMALY FINDER runs in two passes: Pass 1 reads only the declaration tables and records predicted anomalies with a `Predicted?` column; Pass 2 reads the full trace and completes the sweep. A reconciliation table compares predictions to findings. | coverage | Pass 1 and Pass 2 are structurally distinct. The sweep table includes a `Predicted?` column. A reconciliation table is present showing which predictions matched findings and which did not. |
| C-19 | **Evidence-strength quality gate on sweep table** — Each "found" row in the sweep table carries a Strength score (1 = weak / circumstantial, 2 = direct / documented, 3 = confirmed / independently verified). The quality gate requires at least one "found" row with Strength ≥ 2, not merely any finding. | coverage | A Strength column appears in the sweep table. The quality gate text explicitly states the ≥1 Strength ≥ 2 requirement. A sweep with only Strength-1 findings fails C-19. |
| C-20 | **Numeric/temporal invariant gate** — The domain expert role (or equivalent declaration step) must produce at least one invariant that constrains a numeric or temporal value — e.g., `payment amount ≤ budget line remaining`, `approval date ≥ submission date`. Generic structural invariants ("data must be consistent") do not satisfy this gate. | correctness | At least one declared invariant contains an explicit numeric or temporal bound. The bound references a real domain value (amount, date, count, duration), not a placeholder. Structural or tautological invariants do not pass even if an INV-ID is assigned. |
| C-21 | **Surprise column in reconciliation table** — The Pass 1 / Pass 2 reconciliation table (C-18) includes a `Surprise` column that labels each outcome as "Expected" or "Surprising". This produces a calibration signal beyond binary match/mismatch: the model must annotate whether each prediction result was anticipated, enabling inspection of prediction quality rather than just prediction accuracy. | depth | The reconciliation table has a `Surprise` column. Every row carries an "Expected" or "Surprising" label. At least one row is labeled "Surprising" with a brief explanation of why the outcome differed from prediction. A reconciliation table with only "Expected" labels fails C-21 unless the prompt requires a justification for the all-expected outcome. |
| C-22 | **Score at point of discovery** — The evidence-strength score (C-19) must be assigned when the finding is first recorded, not retroactively after the full sweep is complete. The prompt explicitly states this anti-retroactive instruction — e.g., "assign Strength before moving to the next row" or "do not revise Strength scores after Pass 2 completes". This prevents the model from post-hoc rationalizing all findings to Strength 2+ to clear the quality gate. | correctness | The prompt contains an explicit instruction to score Strength at the time of discovery, before the sweep continues. A prompt that defines the Strength scale without the anti-retroactive instruction does not pass C-22, even if the output happens to score correctly. |
```

---

**What changed in v5:**

| New ID | Source | What it gates |
|--------|--------|---------------|
| C-20 | R4 Signal 1 | Invariants that can actually be violated — numeric/temporal bounds only |
| C-21 | R4 Signal 2 | Prediction calibration quality, not just prediction existence |
| C-22 | R4 Signal 3 (V-02) | Strength scoring discipline — anti-retroactive instruction in the prompt |

C-20 closes the loophole where a model satisfies C-03 with a structural truism ("status must be set") that no trace operation can actually violate. C-21 upgrades C-18's reconciliation table from a coverage artifact to a calibration artifact. C-22 is the mirror of C-19: C-19 gates the output, C-22 gates the scoring process itself.
