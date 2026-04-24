Reading the scorecard carefully to identify the R7 excellence patterns — the structural innovations in V-01, V-02, and V-03 that go beyond what C-26/C-27/C-28 already specify.

**R7 patterns extracted:**

- **V-01**: Acquittal Advocate as a *named sub-role with activation condition* — role activates on "no finding," produces a mandatory Gap Record before the exit gate opens; converts C-27's naming protocol from a passive constraint into an active role-gated enforcement mechanism.
- **V-02**: C-28 expressed as *parallel verdict columns in the sweep table* — `Declaration-Only Finding` + `Trace-Diff Finding` columns per row; "None" in either cell requires an inline gap record; makes both detection paths independently auditable.
- **V-03**: C-26 strengthened by *explicit LOCKED/OPEN phase status with a required COMPLETE declaration* — Phase N stays locked until Phase N-1 emits a named "PHASE N-1: COMPLETE" artifact; turns progression from a behavioral rule into a mechanical lock/unlock with a required unlock signal.

Those become C-29, C-30, C-31.

---

```markdown
# trace-state Rubric v8
**Updated**: 2026-03-14
**Change**: Added C-29, C-30, C-31 from R7 excellence signals (acquittal-advocate
sub-role activation gate, parallel dual-mode verdict columns with inline gap records,
phase LOCKED/OPEN status with explicit COMPLETE declaration).

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
- C-26: anomaly-type-as-top-level-phase with sequential commitment — each of the four anomaly types becomes a numbered top-level phase (not a subsection within a shared sweep part), each with its own exit gate; sequential phase ordering forces linear commitment so the model cannot advance to the next type until the current phase is complete (R6 excellence signal)
- C-27: prejudice-dismissal naming protocol — acquittal ("no finding") requires explicitly naming the specific trace steps, state conditions, or evidence that would need to exist to produce the finding; transforms absence records into structural gap maps rather than bare "None" declarations or generic written acquittals (R6 excellence signal)
- C-28: dual-mode doc-vs-trace detection — the anomaly sweep runs in two independent passes: one against the declaration tables alone, and one diffing declared behavior against the traced step sequence; a claim appearing in the documentation that is not demonstrated in the trace is itself a finding; adds a second detection path to every anomaly type (R6 excellence signal)
- C-29: acquittal-advocate sub-role with activation gate — a dedicated named sub-role (e.g., "Role B: Acquittal Advocate") that activates only when an anomaly-type phase reaches a "no finding" verdict; the sub-role must produce a Gap Record before the phase exit gate opens and cannot be bypassed; converts C-27's naming protocol from a passive constraint into an active role-gated enforcement mechanism where the gate itself is the acquittal record (R7 excellence signal)
- C-30: parallel dual-mode verdict columns with inline gap records — C-28's two detection passes expressed as two separate named columns per anomaly-type row in the sweep table (e.g., `Declaration-Only Finding` and `Trace-Diff Finding`); a "None" entry in either column requires an inline gap record in that cell, not a separate section; makes both detection paths independently auditable and transforms a procedural instruction into a mechanical table constraint (R7 excellence signal)
- C-31: phase LOCKED/OPEN status with explicit COMPLETE declaration — each phase carries an explicit LOCKED/OPEN status label; Phase N remains locked until Phase N-1 emits a named "PHASE N-1: COMPLETE" declaration as the unlock signal; strengthens C-26's sequential commitment from a behavioral progression rule into a mechanical lock state where advancement requires a required named artifact, not merely finishing the work (R7 excellence signal)

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
| C-11 | **Sweep table with row-level verdicts** — The anomaly sweep is expressed as a table with one row per anomaly type; each row carries a mandatory verdict (finding / no finding) before the sweep is considered complete. A table without verdicts does not pass. | format | A sweep table exists. Every anomaly-type row has a verdict cell. Rows without verdicts fail this criterion. |
| C-12 | **Op ID cross-referencing** — Operations are assigned IDs (e.g., OP-01) in the declaration table and those same IDs are used in every reference to that operation throughout the trace and sweep. | format | Every operation in the trace references its declared OP-ID. A single un-IDed operation reference fails this criterion. |
| C-13 | **Entry Condition column in state table** — The state declaration table includes an Entry Condition column that names the operation or event that moves the entity into each state. | format | State table has an Entry Condition column. Every row has a non-empty entry condition. |
| C-14 | **Minimum-found threshold on sweep table** — The sweep table specifies a minimum number of confirmed findings required per anomaly type before the sweep phase can be declared complete; converts coverage from a "did you look?" gate to a "did you find enough?" gate. | depth | A numeric minimum-found threshold is stated per row or globally. The phase cannot complete unless the threshold is met or a structural explanation is provided for falling below it. |
| C-15 | **Full ID ecosystem** — S-IDs (states), OP-IDs (operations), and INV-IDs (invariants) are all declared in their respective tables and cross-referenced consistently wherever those entities appear in the trace, sweep, and anomaly register. | format | All three ID namespaces are declared. Every reference to a state, operation, or invariant uses its ID. Unregistered references are flagged as violations. |
| C-16 | **Undeclared reference as named fifth anomaly class** — References to states, operations, or invariants that appear in the trace but were never declared in the corresponding declaration table are elevated to a named fifth anomaly class with its own dedicated sweep row. | coverage | A fifth sweep row labeled "Undeclared Reference" (or equivalent) exists. Every undeclared reference found in the trace appears as a finding in that row. |
| C-17 | **Anomaly register with separate ID columns** — The anomaly register includes separate columns for each ID type (OP-ID, S-ID, INV-ID); a blank cell in any of these columns for a non-acquittal verdict row is itself a detectable mechanical gap, not a prose omission. | format | Anomaly register has at least OP-ID, S-ID, and INV-ID columns. Every finding row has values in all applicable columns. Blank cells in finding rows fail this criterion. |
| C-18 | **Pre-sweep hypothesis with dual-pass ANOMALY FINDER** — Before the sweep begins, the analyst records a falsifiable prediction table: which anomaly types are expected, the structural reason for each prediction, and confidence level. Sweep results are then reconciled against predictions. | depth | A prediction table exists before the sweep section. Each row has anomaly type, structural reason, and confidence. A reconciliation step compares sweep results to predictions. |
| C-19 | **Evidence-strength quality gate on sweep table** — Each finding in the sweep table is assigned an evidence strength on a 1/2/3 scale; at least one finding must reach strength ≥2 before the phase can be closed. Strength assignments must be made per finding, not as a post-hoc summary. | depth | Every finding row has an evidence strength score. The phase exit gate includes a ≥strength-2 floor check. Post-hoc strength assignment fails this criterion. |
| C-20 | **Numeric/temporal invariant gate** — Before analysis begins, the analyst must produce at least one falsifiable invariant expressed with a numeric threshold or temporal bound (e.g., "SLA response time ≤ 4 hours", "balance delta never exceeds ±$10,000 in a single operation"). Prose-only invariants do not satisfy this gate. | depth | At least one invariant in the invariant table includes a numeric or temporal bound. The gate is checked before Phase 1 opens. Prose-only invariant declarations fail this criterion. |
| C-21 | **Surprise column in reconciliation table** — The reconciliation table that compares predictions to sweep findings includes a Surprise column; each row is labeled Expected or Surprising based on whether the outcome matched the pre-sweep prediction. This produces a calibration signal beyond binary match/mismatch. | depth | Reconciliation table has a Surprise column. Every row has a verdict. The count of Surprising outcomes is surfaced as a named signal at the end of the reconciliation section. |
| C-22 | **Score-at-point-of-discovery instruction** — Evidence strength (C-19) must be assigned at the moment a finding is first recorded, not after the full sweep is complete. The rubric or prompt must state this constraint explicitly, not rely on table ordering to enforce it. | depth | An explicit instruction appears in the sweep protocol stating that evidence strength is assigned at discovery time. Retroactive scoring instructions fail this criterion. |
| C-23 | **Score-aloud verbal protocol** — C-22 is expressed as a named cognitive behavioral discipline (e.g., "Score-Aloud Protocol") with an explicit self-correction checkpoint; the analyst is instructed to state the evidence strength aloud (or in writing) before recording any other content about the finding. Not a passive table constraint. | depth | A named protocol section exists. The instruction requires strength to be verbalized or written before finding details. A self-correction checkpoint is explicitly stated. |
| C-24 | **Phase exit gate checkboxes** — C-20, C-21, and C-22 appear as explicit hard completion gates expressed as checkboxes or equivalent binary pass/fail markers at the end of each phase; the model must affirmatively satisfy each gate before advancing to the next phase, preventing optional-boilerplate treatment. | format | Each phase ends with a gate checklist. C-20, C-21, and C-22 constraints each appear as a named gate item. Advancement without gate satisfaction fails this criterion. |
| C-25 | **Three-value surprise taxonomy with calibration score** — The reconciliation table uses a three-value classification (C = Correct, FP = False Positive, FN = False Negative) instead of binary Expected/Surprising; a calibration score is computed from the classification counts and a stated threshold triggers a structural diagnosis step when accuracy falls below it. | depth | Reconciliation table uses C/FP/FN labels. A calibration score formula is stated. A threshold value is named. Scores below the threshold trigger a named diagnosis step. |
| C-26 | **Anomaly-type-as-top-level-phase with sequential commitment** — Each of the four anomaly types becomes a numbered top-level phase (not a subsection within a shared sweep part), each with its own exit gate; sequential phase ordering forces linear commitment so the model cannot advance to the next type until the current phase is complete. | format | Four numbered phases, one per anomaly type, each at the top level of the document structure. Each phase has its own exit gate. No phase is a subsection of another. |
| C-27 | **Prejudice-dismissal naming protocol** — Acquittal ("no finding") requires explicitly naming the specific trace steps, state conditions, or evidence that would need to exist to produce the finding; transforms absence records into structural gap maps rather than bare "None" declarations or generic written acquittals. | depth | Every "no finding" verdict includes a named gap record specifying the missing evidence. Bare "None" or "not applicable" entries fail this criterion. Generic prose acquittals without named structural gaps fail this criterion. |
| C-28 | **Dual-mode doc-vs-trace detection** — The anomaly sweep runs in two independent passes: one against the declaration tables alone, and one diffing declared behavior against the traced step sequence; a claim appearing in the documentation that is not demonstrated in the trace is itself a finding; adds a second detection path to every anomaly type. | depth | Two named detection passes exist for each anomaly type. At least one finding is attributed specifically to the doc-vs-trace diff pass. A declaration-only claim with no trace demonstration is treated as a finding. |
| C-29 | **Acquittal-advocate sub-role with activation gate** — A dedicated named sub-role (e.g., "Role B: Acquittal Advocate") activates only when an anomaly-type phase reaches a "no finding" verdict; the sub-role must produce a Gap Record satisfying C-27's naming requirements before the phase exit gate opens; the gate cannot open without the Gap Record regardless of other phase work completed; converts C-27 from a passive constraint into a role-gated enforcement mechanism. | depth | A named sub-role exists with an explicit activation condition ("no finding" verdict). The phase exit gate is structurally blocked until the sub-role produces a Gap Record. The sub-role and its activation condition are named in the protocol, not left implicit. |
| C-30 | **Parallel dual-mode verdict columns with inline gap records** — C-28's two detection passes are expressed as two separate named columns per anomaly-type row in the sweep table (e.g., `Declaration-Only Finding` and `Trace-Diff Finding`); a "None" entry in either column requires an inline gap record in that cell satisfying C-27's naming requirements; transforms dual-mode detection from a procedural instruction into a mechanical table constraint where both detection paths are independently auditable. | format | Sweep table has two named verdict columns per anomaly-type row. A "None" cell in either column is only valid when accompanied by an inline gap record in that same cell. Column structure is present for every anomaly-type row. |
| C-31 | **Phase LOCKED/OPEN status with explicit COMPLETE declaration** — Each phase carries an explicit LOCKED/OPEN status label; Phase N remains locked until Phase N-1 emits a named "PHASE N-1: COMPLETE" declaration as the unlock signal; the COMPLETE declaration is a required named artifact, not implicit; strengthens C-26's sequential commitment from a behavioral progression rule into a mechanical lock state where the unlock artifact is itself the completion record. | format | Every phase has a LOCKED/OPEN status label. A "PHASE N: COMPLETE" declaration is required to unlock Phase N+1. The protocol states that Phase N+1 cannot open without the declaration. Advancing without the declaration fails this criterion. |
```
