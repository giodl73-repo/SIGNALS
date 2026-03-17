Reading the R8 scorecard to extract the three named excellence signals before writing the rubric.

The three signals are:

- **Signal 1 — Always-on acquittal advocacy**: Role B fires unconditionally on every phase, not just on "no-finding" — closes the loophole where one weak finding bypasses gap documentation for everything else not found.
- **Signal 2 — Symmetric audit trail per phase**: Every phase emits an identical structural pair `{findings list} + {Gap Record}`; absence of either is a detectable mechanical error, not a judgment call.
- **Signal 3 — Gap Record as literal unlock artifact**: The Gap Record is not documentation produced before the exit gate opens — it *is* the exit gate unlock signal, applying the same lock/unlock mechanic as PHASE N: COMPLETE.

Those become C-32, C-33, C-34. Point value shifts from 0.435 to 0.385 (10 / 26 aspirationals).

```markdown
# trace-state Rubric v9
**Updated**: 2026-03-14
**Change**: Added C-32, C-33, C-34 from R8 excellence signals (unconditional
gap documentation per phase, symmetric phase output contract, Gap Record as
mechanical unlock signal). Aspirational point value updated: 10 / 26 = 0.385 pts each.

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
- C-32: unconditional gap documentation per phase — Role B fires on every phase regardless of finding count; the conditional "activates on no-finding" trigger from C-29 is removed; even phases with findings must produce a Gap Record documenting what was not found; closes the loophole where a single weak finding bypasses gap documentation for everything else that was not detected (R8 excellence signal)
- C-33: symmetric phase output contract — every phase emits a structurally identical pair: `{findings list} + {Gap Record}`; the absence of either component is a detectable mechanical error, not a judgment call about whether one was warranted; enables machine-checkable verification across the full trace and removes phase-level structural variance (R8 excellence signal)
- C-34: Gap Record as mechanical unlock signal — the Gap Record is not optional documentation produced in advance of the exit gate opening; it is the exit gate unlock signal itself; "The Gap Record is the unlock signal for the phase exit gate" promotes the artifact from a precondition to the literal gate trigger, applying the same lock/unlock mechanic used by PHASE N: COMPLETE and creating a uniform artifact-driven gate model across both finding documentation and gap documentation (R8 excellence signal)

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
| C-08 | **Race condition scenario** — At least one race condition is identified and traced: two concurrent operations whose interleaving produces an anomalous result, with the window of vulnerability identified. | coverage | One concurrent scenario is traced showing the problematic interleaving sequence, the specific state window where the race is possible, and the resulting anomaly. |

---

## Aspirational Criteria

*26 criteria — 0.385 pts each (full pass), 0.193 pts (partial), 0.000 pts (fail).*

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **All four anomaly types** — All four anomaly classes are covered: invalid state transition, missing precondition check, invariant violation, and race condition. | coverage | One finding per anomaly type, or an explicit documented verdict for each type. |
| C-10 | **Structured notation / transition table** — The state machine is presented with a formal transition table listing states, valid transitions, triggering operations, and guards. | format | A table exists with state, transition, operation, and guard columns. Prose-only descriptions do not pass. |
| C-11 | **Sweep table with mandatory row-level verdicts** — The anomaly sweep is presented as a table with one row per candidate, and each row carries an explicit verdict (found/not-found). | format | Sweep table present. Every row has a verdict cell. No row is left without a verdict. |
| C-12 | **Op ID cross-referencing** — Operations are assigned IDs (OP-01, OP-02, …) and those IDs are used consistently in the trace steps, the sweep table, and the exit gate checklist. | correctness | OP-IDs appear in the declaration table, at least three trace steps, and the sweep table. |
| C-13 | **Entry Condition column** — The state machine table includes an Entry Condition column listing what must be true for the system to enter each state. | format | Entry Condition column present in the state table. At least one entry condition is state-specific, not generic. |
| C-14 | **Minimum-found threshold** — The sweep table carries a stated minimum number of findings required before the phase exit gate opens, converting the sweep from a coverage gate into a depth gate. | coverage | A numeric minimum is stated per phase. Exit gate blocks advancement if the minimum is not met. |
| C-15 | **Full ID ecosystem** — S-IDs, OP-IDs, and INV-IDs are all declared in their respective registries and cross-referenced in trace steps and sweep table rows. | correctness | Three registry types present. IDs from all three appear in trace steps and sweep tables. |
| C-16 | **Undeclared reference as fifth anomaly class** — References to states, operations, or invariants that appear in the trace but were never declared in the registries are treated as a named fifth anomaly class with its own sweep phase. | coverage | A dedicated sweep phase or sweep section for undeclared references exists, with its own table and verdict. |
| C-17 | **Anomaly register with typed ID columns** — A standalone anomaly register exists with separate columns for OP-ID, S-ID, and INV-ID; a blank cell in any found-verdict row is a detectable mechanical gap. | format | Anomaly register is its own table (not embedded in sweep). Columns: finding ID, OP-ID, S-ID, INV-ID, verdict. Blank cell in a found row fails. |
| C-18 | **Pre-sweep hypothesis with dual-pass ANOMALY FINDER** — Before the sweep begins, the analyst records a falsifiable prediction of which anomaly types and specific operations are most likely to produce findings. | correctness | Hypothesis section present before sweep. At least three specific predictions named. Reconciliation stage present after sweep. |
| C-19 | **Evidence-strength quality gate** — Each finding is assigned an evidence strength on a 1/2/3 scale at point of recording; the phase exit gate requires at least one finding at strength ≥ 2 before advancement. | correctness | Strength scale defined. Each finding has a strength score. Exit gate explicitly checks the ≥ 2 requirement. |
| C-20 | **Numeric/temporal invariant gate** — At least one invariant must be numeric or temporal (e.g., "SLA ≤ 48 hours", "balance ≥ 0 after every credit") before the analysis phase begins; absence of such an invariant blocks advancement. | correctness | At least one numeric or temporal invariant declared in the registry. Exit gate confirms this before sweep. |
| C-21 | **Surprise column in reconciliation table** — The post-sweep reconciliation table includes a column labeling each prediction outcome as Expected or Surprising, producing a calibration signal beyond binary match/mismatch. | format | Reconciliation table present. Surprise column with Expected/Surprising labels populated for each prediction. |
| C-22 | **Score at point of discovery** — Evidence strength is assigned when the finding is first recorded, not retroactively; the instruction explicitly prohibits retroactive scoring after the full sweep is complete. | correctness | Instruction explicitly states "at point of discovery, not retroactively." Exit gate confirms per phase. |
| C-23 | **Score-aloud verbal protocol** — C-22 is expressed as a named cognitive behavioral discipline (not a passive table constraint), with an explicit self-correction checkpoint where the analyst must confirm they have not deferred any scoring. | behavior | Named discipline present (e.g., "Score-Aloud Protocol"). Self-correction checkpoint is a separate named step, not a bullet in an existing section. |
| C-24 | **Phase exit gate checkboxes** — C-20, C-21, and C-22 appear as explicit hard completion gates per phase; model must affirmatively check each gate before advancing; gates are not optional boilerplate. | format | Each phase has a checklist. C-20, C-21, C-22 appear as named checkbox items. No phase advances without all boxes checked. |
| C-25 | **Three-value surprise taxonomy with calibration score** — The reconciliation table uses C/FP/FN classification (Correct, False Positive, False Negative) instead of binary Expected/Surprising; a computed calibration score is produced with a stated threshold that triggers structural diagnosis when accuracy falls below it. | correctness | C/FP/FN column present. Calibration score formula defined. Threshold stated. Low-accuracy branch present in the instruction. |
| C-26 | **Anomaly-type-as-top-level-phase with sequential commitment** — Each anomaly type becomes a numbered top-level phase with its own exit gate; sequential ordering prevents advancement to Phase N until Phase N-1 is complete. | format | Four or more numbered top-level phases. Each has an exit gate. Phase order is fixed and enforced. |
| C-27 | **Prejudice-dismissal naming protocol** — An acquittal ("no finding") requires naming the specific trace steps, state conditions, or evidence that would need to exist to produce the finding; bare "None" or generic written acquittals do not pass. | correctness | Every "no finding" verdict includes a named absence map: what was looked for, where it was looked for, and what evidence would have constituted a finding. |
| C-28 | **Dual-mode doc-vs-trace detection** — The sweep runs two independent passes: one against declaration tables alone, and one diffing declared behavior against the traced step sequence; a declared claim not demonstrated in the trace is itself a finding. | coverage | Two named detection passes defined. Sweep table has two verdict columns (declaration-only and trace-diff). Both columns are populated per row. |
| C-29 | **Acquittal-advocate sub-role with activation gate** — A dedicated named sub-role (e.g., "Role B: Acquittal Advocate") activates when a phase reaches "no finding"; it must produce a Gap Record before the exit gate opens and cannot be bypassed. | format | Named sub-role defined. Activation condition stated. Gap Record produced per no-finding phase. Exit gate blocked until Gap Record present. |
| C-30 | **Parallel dual-mode verdict columns with inline gap records** — C-28's two detection passes are expressed as two separate named columns per row; a "None" in either column requires an inline gap record in that cell, not a separate section. | format | Two named columns per sweep row. Inline gap record required on any "None" cell. Gap record content is in the cell itself, not referenced externally. |
| C-31 | **Phase LOCKED/OPEN status with explicit COMPLETE declaration** — Each phase carries an explicit LOCKED/OPEN status label; Phase N remains locked until Phase N-1 emits a named "PHASE N-1: COMPLETE" declaration as the unlock signal. | format | LOCKED/OPEN labels present per phase. PHASE N: COMPLETE declaration is the literal unlock artifact. Phases do not open without it. |
| C-32 | **Unconditional gap documentation per phase** — Role B fires on every phase regardless of finding count; the conditional "activates on no-finding" trigger from C-29 is removed; phases with findings must still produce a Gap Record documenting what was not found; closes the loophole where a single weak finding bypasses gap documentation for everything else that was not detected. | coverage | Role B produces a Gap Record on every phase, including phases with at least one finding. No phase is exempt from gap documentation. Conditional activation language is absent. |
| C-33 | **Symmetric phase output contract** — Every phase emits a structurally identical pair: `{findings list} + {Gap Record}`; the absence of either component is a detectable mechanical error, not a judgment call about whether one was warranted; enables machine-checkable verification across the full trace. | format | Instruction explicitly states the two-component output contract for every phase. A phase missing either component is called out as a structural failure, not an omission. |
| C-34 | **Gap Record as mechanical unlock signal** — The Gap Record is not documentation produced in advance of exit gate opening; it is the exit gate unlock signal itself; this promotes the artifact from a precondition to the literal gate trigger, applying the same lock/unlock mechanic used by PHASE N: COMPLETE and creating a uniform artifact-driven gate model across both finding documentation and gap documentation. | format | Instruction explicitly states "The Gap Record is the unlock signal for the phase exit gate" or equivalent. Gap Record and PHASE N: COMPLETE are described under the same gate-unlock model. Precondition framing is absent. |
```
