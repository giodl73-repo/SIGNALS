Looking at the R11 scorecard for V-01, I need to identify what genuinely new patterns it achieved beyond the existing criteria.

**V-01's three variation axes:**
1. Standards Registry (sealed pre-game) — went beyond C-35's per-phase pre-commitment to a global PART 0 seal before any analysis begins
2. Fully expanded Phase 3E peer template — PARTIAL, not achieved
3. Mandatory negative-path step in trace — C-06 moved PARTIAL→PASS via explicit rejection immutability constraint

New patterns to extract:
- **C-38**: Global PART 0 Standards Registry with pre-game seal (elevates C-35 from per-phase to global pre-commitment)
- **C-39**: Rejection immutability as mandatory trace step constraint (strengthens C-06 by making after-state documentation mechanically required on rejected operations)

Point value shifts: 10 / 31 = 0.323 pts each

---

```markdown
# trace-state Rubric v11
**Updated**: 2026-03-15
**Change**: Added C-38, C-39 from R11 excellence signals (global pre-game standards
registry seal covering all phases before any analysis begins, rejection immutability
as mandatory trace step structural constraint). Aspirational point value updated:
10 / 31 = 0.323 pts each.

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
- C-35: pre-detection Role B evidence standard commitment — before either detection pass runs in a phase, Role B explicitly commits to the minimum evidence standard it will hold for that phase's anomaly type (e.g., "I require direct trace-step or state-condition evidence at strength ≥ 2"); this commitment is recorded as a named artifact in the phase header, separate from and prior to the post-detection Gap Record; makes the Gap Record's reasoning auditable against a pre-stated standard rather than post-hoc, and elevates Role B from reactive gap-documenter to proactive standard-setter whose commitment cannot be adjusted after findings are known (R9 excellence signal)
- C-36: undeclared reference as fifth peer phase — undeclared references receive a dedicated top-level numbered phase (e.g., Phase 3E) structurally identical to the four anomaly-type phases: its own sweep table with Declaration-Only and Trace-Diff columns, Role B pre-detection commitment, Role B Gap Record, LOCKED/OPEN status label, and PHASE 3E: COMPLETE unlock signal; not a verification gate item in exit certification or a subsection of another phase, but a full sequential peer in the lock chain; restores the Phase 5 pattern as first-class, ensuring the fifth anomaly class receives the same mechanical enforcement as the other four (R9 excellence signal)
- C-37: evidence strength threshold as hard phase exit gate — the evidence strength threshold (at least one finding at strength ≥ 2, or Role B Gap Record explicitly explains why no finding met the standard) is expressed as a named exit gate condition per phase — a checkbox item in the phase exit certification that blocks PHASE N: COMPLETE from being declared and thus keeps Phase N+1 LOCKED until satisfied; creates a three-gate model per phase exit (Findings List gate + Evidence Strength gate + Gap Record gate), making C-19's quality requirement mechanically parallel to C-34's Gap Record gate rather than a per-step reminder or aspirational note (R9 excellence signal)
- C-38: global standards registry with pre-game seal — all phase evidence standards are consolidated into a PART 0 Standards Registry that is sealed before PART 1 opens; each phase restates its exact registry row verbatim at phase entry before detection begins; the seal is explicitly declared (e.g., "REGISTRY SEALED — standards cannot be revised after this point"); elevates C-35's per-phase pre-commitment to a global pre-game commitment covering all phases simultaneously, so no standard can be set or adjusted after the first analysis artifact is produced; makes cross-phase standard consistency mechanically auditable from the registry entry alone (R11 excellence signal)
- C-39: rejection immutability as mandatory trace step constraint — negative-path steps must explicitly document that the entity remains in its before-state after rejection; the requirement appears as a named structural element in the trace step template (e.g., "The entity must remain in its before-state after rejection") rather than a general recommendation; closes the gap where a narrative rejection description omits the after-state entirely, and makes guard-condition state immutability mechanically verifiable from the trace record — a rejected operation that changes entity state is a detectable anomaly, not an inference (R11 excellence signal)

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
| C-06 | **Negative path** — At least one operation is traced where a guard condition fires and the operation is rejected. The trace shows the before-state, the rejection reason, and confirms the entity remains in its before-state after rejection. | correctness | At least one rejected operation is present with before-state documented, rejection reason stated, and entity state confirmed unchanged. Narrative "this would fail" without state documentation does not pass. |
| C-07 | **Numbered step-by-step format** — The trace is presented as a numbered sequence of discrete steps. Each step names the operation, shows state transitions, and can be replayed mechanically by a reader following only the trace document. | behavior | Steps are numbered. Each step contains enough information to replay the operation in isolation. A reader with no prior context could reconstruct the state machine from the trace alone. |
| C-08 | **Race condition scenario** — At least one race condition is identified: a scenario where two concurrent operations on the same entity produce an anomalous outcome not present when operations execute sequentially. | coverage | At least one race condition is named with the specific concurrent operations identified and the anomalous outcome described. A timing narrative ("if A and B happen simultaneously") without the specific state consequence does not pass. |

---

## Aspirational Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **All four anomaly types covered** — The trace identifies at least one instance of each anomaly type: invalid state transition, missing precondition check, invariant violation, and race condition. | coverage | One finding per anomaly type present. |
| C-10 | **Structured notation / transition table** — The state machine is expressed as a formal transition table or structured notation (not prose only), enabling mechanical verification of which transitions are valid. | behavior | A table or formal notation maps (state, operation) → next-state. |
| C-11 | **Sweep table with mandatory row-level verdicts** — Each anomaly type has a sweep table with explicit row-level verdicts; an empty row signals no finding for that type, making coverage gaps detectable from table structure alone. | coverage | Sweep table present for at least one anomaly type with row-level verdicts. No verdict row = no finding — not omitted. |
| C-12 | **Op ID cross-referencing** — Operations are assigned unique IDs (OP-IDs) declared in a registry and cross-referenced in finding tables and trace steps; a finding without an OP-ID is a detectable gap. | correctness | OP-IDs declared in registry and appear in both finding tables and trace steps. |
| C-13 | **Entry Condition column in state machine table** — The state registry includes an Entry Condition column stating what must be true for the entity to enter each state. | correctness | State registry has Entry Condition column with non-trivial content for each state. |
| C-14 | **Minimum-found threshold on sweep table** — The sweep table carries a minimum threshold (e.g., "at least one finding required before phase closes"), converting the table from a coverage gate into a depth gate. | coverage | Explicit minimum threshold stated; phase cannot close on zero findings without a documented exception. |
| C-15 | **Full ID ecosystem** — S-IDs, OP-IDs, and INV-IDs are all declared in named registries and cross-referenced in finding tables and trace steps; a reference to an undeclared ID is itself a detectable anomaly. | correctness | All three ID types declared in registries and referenced consistently. |
| C-16 | **Undeclared reference as named fifth anomaly class** — References to states, operations, or invariants that appear in the trace or documentation but are absent from the declaration registries are treated as a distinct named anomaly class with its own sweep row, not folded into the four primary types. | coverage | Undeclared reference has its own named sweep row separate from the four primary anomaly types. |
| C-17 | **Anomaly register with separate ID columns** — The anomaly register has separate columns for OP-ID, S-ID, and INV-ID; a blank cell in any found-verdict row is a detectable mechanical gap, not an acceptable omission. | correctness | Three separate ID columns present; blank in a found-verdict row is scored as a gap. |
| C-18 | **Pre-sweep hypothesis with dual-pass ANOMALY FINDER** — Before the sweep runs, predictions are recorded for each anomaly type: expected count, confidence, and specific scenario; the post-sweep reconciliation compares actuals to predictions, producing a falsifiable record. | behavior | Hypothesis table present before sweep; reconciliation table present after sweep. |
| C-19 | **Evidence-strength quality gate** — Each finding is assigned a strength score (1/2/3 scale); a phase may not close unless at least one finding reaches strength ≥ 2 or the Gap Record explicitly explains why none did. | correctness | Strength scores present on findings; phase exit gate references the ≥ 2 threshold explicitly. |
| C-20 | **Numeric/temporal invariant gate** — At least one invariant must be numeric or temporal with a precise falsifiable threshold (e.g., "any decrease > $0.00 is a violation") before analysis begins; vague or directional invariants alone do not satisfy this gate. | correctness | At least one invariant has a numeric or temporal threshold that could be evaluated mechanically. |
| C-21 | **Surprise column in reconciliation table** — After the sweep, the reconciliation table pairs each prediction to its outcome with a Surprise label (Expected / Surprising), producing a calibration signal that distinguishes correct predictions from lucky ones. | behavior | Reconciliation table present with Surprise column populated for each prediction. |
| C-22 | **Score-at-point-of-discovery instruction** — Evidence strength is assigned the moment a finding is first recorded, not after the full sweep is complete; the rubric or template states this as an explicit instruction at the detection entry point. | correctness | Instruction to score at point of discovery present at detection entry; not only at end-of-sweep or in a general note. |
| C-23 | **Score-aloud verbal protocol** — C-22 is expressed as a named cognitive behavioral discipline: the scorer vocalizes the strength rationale (e.g., "I am scoring this 2 because...") and a self-correction gate blocks recording if the sentence cannot be completed; not a passive table constraint. | behavior | Named verbal protocol present with self-correction gate; incomplete rationale blocks recording. |
| C-24 | **Phase exit gate checkboxes** — C-20, C-21, and C-22 appear as explicit named checkboxes in the phase exit certification; each must be affirmatively checked before the phase may close. | correctness | Three checkboxes (numeric/temporal invariant, reconciliation, score-at-discovery) present in phase exit certification. |
| C-25 | **Three-value surprise taxonomy with calibration score** — The reconciliation table classifies each prediction outcome as C (Correct), FP (False Positive), or FN (False Negative); a computed calibration score is derived and a stated threshold triggers structural diagnosis when accuracy falls below it. | behavior | C/FP/FN taxonomy present; calibration score computed; diagnostic threshold stated. |
| C-26 | **Anomaly-type-as-top-level-phase with sequential commitment** — Each of the four anomaly types is a numbered top-level phase with its own exit gate; sequential ordering prevents the model from advancing to the next type until the current phase is complete. | behavior | Four numbered phases present (not subsections); sequential gate enforced; evidence of inability to skip phases. |
| C-27 | **Prejudice-dismissal naming protocol** — An acquittal ("no finding") explicitly names the specific trace steps, state conditions, or evidence that would need to exist to produce the finding; bare "None" declarations or generic written acquittals do not pass. | correctness | Every "no finding" verdict includes specific counterfactual evidence description. |
| C-28 | **Dual-mode doc-vs-trace detection** — Each anomaly type is swept in two independent passes: one against declaration tables alone, one diffing declared behavior against the traced step sequence; a declaration present in documentation but absent from the trace is itself a finding type. | coverage | Two named detection passes per phase; declaration-present-but-trace-absent is an explicit finding category. |
| C-29 | **Acquittal-advocate sub-role with activation gate** — A dedicated named sub-role activates when a phase reaches a "no finding" verdict and must produce a Gap Record before the phase exit gate opens; the sub-role cannot be bypassed. | behavior | Named sub-role present; activation on no-finding verdict; Gap Record required before gate opens. |
| C-30 | **Parallel dual-mode verdict columns with inline gap records** — C-28's two detection passes appear as two separate named columns per anomaly-type row in the sweep table; a "None" entry in either column requires an inline gap record in that cell, not a separate section. | correctness | Two named columns present in sweep table; inline gap record required for "None" entries. |
| C-31 | **Phase LOCKED/OPEN status with explicit COMPLETE declaration** — Each phase carries an explicit LOCKED/OPEN status label; Phase N remains locked until Phase N-1 emits a named "PHASE N-1: COMPLETE" declaration as the unlock signal. | behavior | LOCKED/OPEN labels present on all phases; COMPLETE declaration present as named unlock artifact. |
| C-32 | **Unconditional gap documentation per phase** — Role B fires on every phase regardless of finding count; the conditional "activates on no-finding" trigger is removed; even phases with findings produce a Gap Record documenting what was not found. | correctness | Gap Record present on every phase; no conditional exemption for phases with findings. |
| C-33 | **Symmetric phase output contract** — Every phase emits a structurally identical pair: `{findings list} + {Gap Record}`; the absence of either component is a detectable mechanical error. | correctness | Both components present on every phase; absence of either scored as a structural gap. |
| C-34 | **Gap Record as mechanical unlock signal** — The Gap Record is not a precondition to the exit gate; it is the exit gate unlock signal itself; "The Gap Record is the unlock signal for the phase exit gate" promotes the artifact from documentation to the literal gate trigger. | behavior | Template or rubric explicitly states Gap Record is the unlock signal, not merely a precondition. |
| C-35 | **Pre-detection Role B evidence standard commitment** — Before either detection pass runs in a phase, Role B explicitly commits to the minimum evidence standard it will hold for that phase's anomaly type; this commitment is recorded as a named artifact in the phase header, separate from and prior to the post-detection Gap Record. | correctness | Named pre-detection commitment artifact present in each phase header; commitment cannot be revised after findings are known. |
| C-36 | **Undeclared reference as fifth peer phase** — Undeclared references receive a dedicated top-level numbered phase structurally identical to the four anomaly-type phases: its own sweep table with Declaration-Only and Trace-Diff columns, Role B pre-detection commitment, Role B Gap Record, LOCKED/OPEN status label, and PHASE COMPLETE unlock signal; not a verification gate item or a subsection of another phase. | coverage | Phase 3E (or equivalent) present as a top-level numbered phase with all five structural components fully expanded in the template body. |
| C-37 | **Evidence strength threshold as hard phase exit gate** — The evidence strength threshold (at least one finding at strength ≥ 2, or Gap Record explains why none did) is a named checkbox in the phase exit certification that blocks PHASE N: COMPLETE and keeps Phase N+1 LOCKED until satisfied; creates a three-gate model per phase (Findings List gate + Evidence Strength gate + Gap Record gate). | correctness | Evidence Strength named as a checkbox exit gate; three-gate model present per phase. |
| C-38 | **Global standards registry with pre-game seal** — All phase evidence standards are consolidated into a PART 0 Standards Registry that is sealed before PART 1 opens; each phase restates its exact registry row verbatim at phase entry before detection begins; the seal is explicitly declared (e.g., "REGISTRY SEALED — standards cannot be revised after this point"); elevates C-35's per-phase pre-commitment to a global pre-game commitment covering all phases simultaneously, so no standard can be set or adjusted after the first analysis artifact is produced; makes cross-phase standard consistency mechanically auditable from the registry entry alone. | correctness | PART 0 Standards Registry present and sealed before Part 1; each phase restates its registry row verbatim; seal declaration present and precedes all analysis artifacts. |
| C-39 | **Rejection immutability as mandatory trace step constraint** — Negative-path steps must explicitly document that the entity remains in its before-state after rejection; the requirement appears as a named structural element in the trace step template (e.g., "The entity must remain in its before-state after rejection"), not as a general recommendation; makes guard-condition state immutability mechanically verifiable from the trace record; a rejected operation that shows entity state change is a detectable anomaly, not an inference. | correctness | Named immutability constraint present in trace step template; rejected operations include explicit after-state confirming no change; absence of after-state on a rejected operation is a scoreable gap. |
```

---

**Summary of changes:**

| | v10 | v11 |
|---|---|---|
| New criteria | — | C-38, C-39 |
| Total aspirationals | 29 | 31 |
| Aspirational point value | 0.345 | 0.323 |
| Source round | R9 signals | R11 signals |

**C-38** captures V-01's key structural innovation: moving from C-35's per-phase pre-commitment to a global PART 0 registry sealed before any analysis begins. The distinction matters — per-phase commitment still allows the first phase's standard to be set after the overall framing is known; a pre-game seal removes that gap entirely.

**C-39** captures the rejection immutability constraint that pushed C-06 from PARTIAL to PASS. The criterion is distinct from C-06 (which requires a negative path to exist) — C-39 requires that the after-state on rejected operations be explicitly documented and confirmed unchanged, making guard-condition immutability a checkable structural property of the trace record.
