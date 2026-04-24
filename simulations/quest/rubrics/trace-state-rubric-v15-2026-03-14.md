Looking at the Round 16 scorecard, I can extract three distinct excellence signals beyond C-44 and C-45:

1. **V-03** — pre-game exit contract (PART 0.0C) sealing the 4-gate model globally
2. **V-03** — pre-game Phase 3E row independence contract (PART 0.0D) sealing anti-masking globally
3. **V-05** — imperative modal register (MUST/BLOCKED/ADVANCE) hardening all gate language

These become C-46, C-47, C-48. Aspirational bucket grows from 37 → 40 criteria; point value drops from 0.270 → 0.250.

---

# trace-state rubric — v15

**Scoring weights**: Essential 60% (5 × 12 pts) · Recommended 30% (3 × 10 pts) · Aspirational 10% (40 × 0.250 pts)

---

## Bucket Definitions

**Essential (60%)** — baseline correctness; a trace that misses any of these is not a trace:
- C-01: before/after state per operation
- C-02: preconditions and postconditions
- C-03: named invariants
- C-04: at least one anomaly identified (empty sweep table — no finding = no signal)
- C-05: domain grounding (Sales/CS/Finance vocabulary — otherwise it's a toy example)

**Recommended (30%)** — what separates a useful trace from a great one:
- C-06: negative path (attempted invalid transition + why it's rejected)
- C-07: numbered step-by-step format (reader can replay the trace mechanically)
- C-08: race condition scenario (the hardest anomaly type, worth its own criterion)

**Aspirational (10%)** — raises the bar once the basics are stable:
- C-09: all four anomaly types covered (complete signal, not just the easy ones)
- C-10: structured notation / transition table (enables mechanical verification, not just prose review)
- C-11 through C-48: see full list below (accumulated from R1–R16 excellence signals)

---

## Aspirational Criteria (Full List)

- **C-09**: all four anomaly types covered (complete signal, not just the easy ones)
- **C-10**: structured notation / transition table (enables mechanical verification, not just prose review)
- **C-11**: sweep table with mandatory row-level verdicts per anomaly type (R1 excellence signal)
- **C-12**: Op ID cross-referencing between declaration and trace (R1 excellence signal)
- **C-13**: Entry Condition column in state machine table (R1 excellence signal)
- **C-14**: minimum-found threshold on sweep table — converts C-11 from coverage gate to depth gate (R2 excellence signal)
- **C-15**: full ID ecosystem — S-IDs, OP-IDs, INV-IDs all declared and cross-referenced (R2 excellence signal)
- **C-16**: undeclared reference elevated to named fifth anomaly class with its own sweep row (R2 excellence signal)
- **C-17**: anomaly register with separate OP-ID / S-ID / INV-ID columns — blank cell in any found-verdict row is a detectable mechanical gap (R2 excellence signal)
- **C-18**: pre-sweep hypothesis with dual-pass ANOMALY FINDER — falsifiable prediction record (R3 excellence signal)
- **C-19**: evidence-strength quality gate on sweep table — 1/2/3 scale with ≥1 strength ≥2 requirement (R3 excellence signal)
- **C-20**: numeric/temporal invariant gate — domain expert must produce at least one falsifiable numeric or temporal invariant with threshold before analysis begins (R4 excellence signal)
- **C-21**: Surprise column in reconciliation table — each prediction outcome labeled expected/surprising, producing a calibration signal beyond binary match/mismatch (R4 excellence signal)
- **C-22**: score-at-point-of-discovery instruction — evidence strength must be assigned when the finding is first recorded, not retroactively after the full sweep is complete (R4 excellence signal)
- **C-23**: score-aloud verbal protocol — C-22 expressed as a named cognitive behavioral discipline with an explicit self-correction checkpoint, not a passive table constraint or end-of-sweep reminder (R5 excellence signal)
- **C-24**: phase exit gate checkboxes — C-20, C-21, and C-22 appear as explicit hard completion gates per phase; model must affirmatively check each gate before advancing, preventing optional-boilerplate treatment (R5 excellence signal)
- **C-25**: three-value surprise taxonomy with calibration score — reconciliation table uses C/FP/FN classification (Correct, False Positive, False Negative) instead of binary Expected/Surprising, plus a computed calibration score with a stated threshold that triggers structural diagnosis when accuracy falls below it (R5 excellence signal)
- **C-26**: anomaly-type-as-top-level-phase with sequential commitment — each of the four anomaly types becomes a numbered top-level phase (not a subsection within a shared sweep part), each with its own exit gate; sequential phase ordering forces linear commitment so the model cannot advance to the next type until the current phase is complete (R6 excellence signal)
- **C-27**: prejudice-dismissal naming protocol — acquittal ("no finding") requires explicitly naming the specific trace steps, state conditions, or evidence that would need to exist to produce the finding; transforms absence records into structural gap maps rather than bare "None" declarations or generic written acquittals (R6 excellence signal)
- **C-28**: dual-mode doc-vs-trace detection — the anomaly sweep runs in two independent passes: one against the declaration tables alone, and one diffing declared behavior against the traced step sequence; a claim appearing in the documentation that is not demonstrated in the trace is itself a finding; adds a second detection path to every anomaly type (R6 excellence signal)
- **C-29**: acquittal-advocate sub-role with activation gate — a dedicated named sub-role (e.g., "Role B: Acquittal Advocate") that activates only when an anomaly-type phase reaches a "no finding" verdict; the sub-role must produce a Gap Record before the phase exit gate opens and cannot be bypassed; converts C-27's naming protocol from a passive constraint into an active role-gated enforcement mechanism where the gate itself is the acquittal record (R7 excellence signal)
- **C-30**: parallel dual-mode verdict columns with inline gap records — C-28's two detection passes expressed as two separate named columns per anomaly-type row in the sweep table (e.g., `Declaration-Only Finding` and `Trace-Diff Finding`); a "None" entry in either column requires an inline gap record in that cell, not a separate section; makes both detection paths independently auditable and transforms a procedural instruction into a mechanical table constraint (R7 excellence signal)
- **C-31**: phase LOCKED/OPEN status with explicit COMPLETE declaration — each phase carries an explicit LOCKED/OPEN status label; Phase N remains locked until Phase N-1 emits a named "PHASE N-1: COMPLETE" declaration as the unlock signal; strengthens C-26's sequential commitment from a behavioral progression rule into a mechanical lock state where advancement requires a required named artifact, not merely finishing the work (R7 excellence signal)
- **C-32**: unconditional gap documentation per phase — Role B fires on every phase regardless of finding count; the conditional "activates on no-finding" trigger from C-29 is removed; even phases with findings must produce a Gap Record documenting what was not found; closes the loophole where a single weak finding bypasses gap documentation for everything else that was not detected (R8 excellence signal)
- **C-33**: symmetric phase output contract — every phase emits a structurally identical pair: `{findings list} + {Gap Record}`; the absence of either component is a detectable mechanical error, not a judgment call about whether one was warranted; enables machine-checkable verification across the full trace and removes phase-level structural variance (R8 excellence signal)
- **C-34**: Gap Record as mechanical unlock signal — the Gap Record is not optional documentation produced in advance of the exit gate opening; it is the exit gate unlock signal itself; "The Gap Record is the unlock signal for the phase exit gate" promotes the artifact from a precondition to the literal gate trigger, applying the same lock/unlock mechanic used by PHASE N: COMPLETE and creating a uniform artifact-driven gate model across both finding documentation and gap documentation (R8 excellence signal)
- **C-35**: pre-detection Role B evidence standard commitment — before either detection pass runs in a phase, Role B explicitly commits to the minimum evidence standard it will hold for that phase's anomaly type (e.g., "I require direct trace-step or state-condition evidence at strength ≥ 2"); this commitment is recorded as a named artifact in the phase header, separate from and prior to the post-detection Gap Record; makes the Gap Record's reasoning auditable against a pre-stated standard rather than post-hoc, and elevates Role B from reactive gap-documenter to proactive standard-setter whose commitment cannot be adjusted after findings are known (R9 excellence signal)
- **C-36**: undeclared reference as fifth peer phase — undeclared references receive a dedicated top-level numbered phase (e.g., Phase 3E) structurally identical to the four anomaly-type phases: its own sweep table with Declaration-Only and Trace-Diff columns, Role B pre-detection commitment, Role B Gap Record, LOCKED/OPEN status label, and PHASE 3E: COMPLETE unlock signal; not a verification gate item in exit certification or a subsection of another phase, but a full sequential peer in the lock chain; restores the Phase 5 pattern as first-class, ensuring the fifth anomaly class receives the same mechanical enforcement as the other four (R9 excellence signal)
- **C-37**: evidence strength threshold as hard phase exit gate — the evidence strength threshold (at least one finding at strength ≥ 2, or Role B Gap Record explicitly explains why no finding met the standard) is expressed as a named exit gate condition per phase — a checkbox item in the phase exit certification that blocks PHASE N: COMPLETE from being declared and thus keeps Phase N+1 LOCKED until satisfied; creates a three-gate model per phase exit (Findings List gate + Evidence Strength gate + Gap Record gate), making C-19's quality requirement mechanically parallel to C-34's Gap Record gate rather than a per-step reminder or aspirational note (R9 excellence signal)
- **C-38**: global standards registry with pre-game seal — all phase evidence standards are consolidated into a PART 0 Standards Registry that is sealed before PART 1 opens; each phase restates its exact registry row verbatim at phase entry before detection begins; the seal is explicitly declared (e.g., "REGISTRY SEALED — standards cannot be revised after this point"); elevates C-35's per-phase pre-commitment to a global pre-game commitment covering all phases simultaneously, so no standard can be set or adjusted after the first analysis artifact is produced; makes cross-phase standard consistency mechanically auditable from the registry entry alone (R11 excellence signal)
- **C-39**: rejection immutability as mandatory trace step constraint — negative-path steps must explicitly document that the entity remains in its before-state after rejection; the requirement appears as a named structural element in the trace step template (e.g., "The entity must remain in its before-state after rejection") rather than a general recommendation; closes the gap where a narrative rejection description omits the after-state entirely, and makes guard-condition state immutability mechanically verifiable from the trace record — a rejected operation that changes entity state is a detectable anomaly, not an inference (R11 excellence signal)
- **C-40**: Gap Record structured field template — the Gap Record uses a fixed named-field template (e.g., `Examined:`, `Evidence Standard Applied:`, `What Was Not Found:`, `What Would Constitute a Finding:`, `Verdict:`) rather than free-form prose; the field structure makes Gap Records machine-comparable across phases and transforms the absence record from a written acquittal into a structured diagnostic artifact; omitting a required field is a detectable mechanical error; elevates C-34's artifact-driven gate from "a record exists" to "a structurally complete record exists" (R12 excellence signal)
- **C-41**: Phase 3E entity-type-stratified scan — Pass 1 in Phase 3E issues distinct scanning instructions per reference entity class (S-ID scan, OP-ID scan, INV-ID scan) rather than a single generic "scan for undeclared references"; each entity class has its own sweep row in the Phase 3E finding table with Declaration-Only and Trace-Diff columns; a sweep verdict on one entity class does not satisfy the sweep requirement for another; closes the loophole where detecting S-ID undeclared references masks a complete absence of OP-ID or INV-ID checking (R12 excellence signal)
- **C-42**: APPLICATION SENTENCE as named second artifact in THE SCORING PROTOCOL — each phase's scoring protocol section contains two distinct artifacts: (1) the verbatim restate of the Standards Registry row (C-35/C-38), and (2) a separate APPLICATION SENTENCE that maps the generic threshold to the specific anomaly evidence shape for that phase (e.g., "For OP-ID race conditions, strength ≥ 2 means: two concurrent trace steps must share the same S-ID with no intervening lock assertion"); the APPLICATION SENTENCE is named and structurally distinct from the restate — a paraphrase of the registry row does not satisfy this criterion; makes the per-phase evidence standard mechanically traceable from registry threshold to phase-specific detection target (R13 excellence signal)
- **C-43**: Phase 3E Pass 2 entity-type stratification — Pass 2 (Trace-Diff scan) in Phase 3E is independently stratified per entity class into P2-S, P2-O, and P2-I sub-scans, mirroring C-41's Pass 1 stratification requirement; each P2 sub-scan is an independent sweep unit in the Phase 3E finding table; a Pass 2 finding or verdict in P2-S does not satisfy P2-O or P2-I; closes the structural loophole where a passing P1-S scan can mask a completely absent Pass 2 OP-ID or INV-ID trace-diff check — the same masking gap C-41 closes for Pass 1 now applied to Pass 2 (R13 excellence signal)
- **C-44**: APPLICATION SENTENCE as mandatory 4th phase exit gate — the APPLICATION SENTENCE (C-42) is expressed as a named checkpoint in the phase exit certification: "Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific, not a restate paraphrase"; this checkpoint blocks PHASE N: COMPLETE from being declared until satisfied, creating a four-gate per-phase exit model (Findings List gate + Evidence Strength gate + Gap Record gate + Scoring Protocol gate); elevates C-42's structural presence requirement to a mechanical gate parallel to C-37's Evidence Strength gate and C-34's Gap Record gate so the APPLICATION SENTENCE cannot be omitted or treated as optional boilerplate (R15 excellence signal)
- **C-45**: Phase 3E all-sub-scan-rows exit gate with explicit cross-row anti-masking rule — Phase 3E exit certification requires all six sub-scan rows (P1-S, P1-O, P1-I, P2-S, P2-O, P2-I) to be individually populated before PHASE 3E: COMPLETE can be declared; the phase header explicitly states the anti-masking rule as a named constraint (e.g., "A finding in any row does NOT satisfy any other row, regardless of shared entity class or pass number") before detection begins; elevates C-43's six-row table structure from a format requirement to a mechanical all-populated exit gate and transforms the row-independence guarantee from a structural implication into an auditable named rule (R15 excellence signal)
- **C-46**: per-phase exit contract seal in PART 0 — the four-gate per-phase exit model (Findings List gate + Evidence Strength gate + Gap Record gate + Scoring Protocol gate) is declared as a named pre-game contract in PART 0 (e.g., "PART 0.0C: Per-Phase Exit Contract") and sealed before PART 1 opens, at the same time as the Standards Registry (C-38); the PART 0 entry names all four gates explicitly so cross-phase gate consistency is auditable from the global registry without reading individual phase exit certifications; complements C-44's in-phase-certification requirement by establishing the exit gate structure as a global pre-game commitment whose terms cannot be revised after the first analysis artifact is produced (R16 excellence signal)
- **C-47**: Phase 3E row independence contract in PART 0 — the anti-masking rule for Phase 3E sub-scan rows is declared as a named pre-game contract in PART 0 (e.g., "PART 0.0D: Phase 3E Row Independence Contract") and sealed before PART 1 opens; the PART 0 entry explicitly states that no finding in any P1 or P2 sub-scan row satisfies any other row; complements C-45's in-phase-header requirement by establishing row independence as a global pre-game commitment anchored in both PART 0 and the Phase 3E header; makes the anti-masking guarantee doubly anchored so a reader can verify it from the global registry without reaching Phase 3E, and ensures the constraint cannot be introduced or softened at the phase level after analysis has begun (R16 excellence signal)
- **C-48**: imperative modal register throughout all gate language — every gate invocation, LOCKED/OPEN status label, and phase exit certification block uses imperative modals (MUST, BLOCKED, ADVANCE) rather than declarative, passive, or conditional framing; "BLOCKED until all gates are satisfied" replaces "complete when requirements are met"; "MUST emit Gap Record" replaces "Gap Record required"; the imperative register is consistent across all phases and all gate types, not applied selectively to a subset; makes any weakening of gate language — passive phrasing, conditional softening, hedged wording — a detectable deviation from the required modal register rather than a stylistic choice, and eliminates the optional-boilerplate loophole for all four gates simultaneously (R16 excellence signal)

---

## Essential Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Before/after state per operation** — Every operation in the trace shows the full entity state immediately before and immediately after execution. No operation is described with only a narrative summary. | correctness | Every operation has a documented before-state and after-state. At least three operations are traced. Narrative-only descriptions do not pass. |
| C-02 | **Preconditions and postconditions** — For each operation, the trace states what must be true before the operation executes (preconditions) and what is guaranteed to be true after (postconditions). | correctness | Every operation has at least one precondition and one postcondition. Vague statements like "data is valid" do not count — they must be state-specific. |
| C-03 | **Named invariants** — The trace identifies at least one named system invariant: a property that must hold across all states regardless of which operations execute. | correctness | At least one invariant is named and defined. Invariants stated only in passing within operation descriptions do not count — they must be declared as invariants. |
| C-04 | **At least one anomaly identified** — The trace produces at least one concrete finding: a violation, inconsistency, race condition, or undeclared reference discovered during analysis. | completeness | At least one anomaly is named with an anomaly type label, affected operation or state IDs, and a description of why it is a violation. "No anomalies found" does not pass. |
| C-05 | **Domain grounding** — The trace uses vocabulary from a real business domain (Sales, Customer Service, Finance, or equivalent). Entities, operations, and states are named for domain concepts, not generic placeholders. | quality | Entity names, operation names, and state labels are domain-specific. Placeholder names like Entity1 or Op_A do not pass. |

---

## Recommended Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Negative path** — The trace includes at least one attempted invalid state transition, documenting what was attempted, why the guard condition rejected it, and that the entity remained in its before-state. | completeness | One negative path with guard condition named and before-state confirmed unchanged. A narrative description of rejection without state confirmation does not pass. |
| C-07 | **Numbered step-by-step format** — The trace is organized as a numbered sequence of steps that a reader can follow and replay mechanically, not as prose paragraphs or a high-level summary. | quality | Steps are numbered. Each step names the operation, the actor, and the state transition. A reader following the steps arrives at the same state sequence the author did. |
| C-08 | **Race condition scenario** — The trace includes at least one scenario in which two operations execute concurrently, documenting the interleaving, the shared state under contention, and the resulting anomaly or demonstrated safety guarantee. | completeness | One race condition scenario with named concurrent operations, shared S-ID or resource, and an explicit verdict (anomaly found or guard confirmed safe). A description of potential concurrency without tracing an actual interleaving does not pass. |

---

## Scoring Reference

**Updated point values (v15):** 10 / 40 = **0.250 pts each** (aspirational bucket grows from 37 to 40 criteria)

| Bucket | Criteria | Weight | Max pts |
|--------|----------|--------|---------|
| Essential | C-01 to C-05 | 60% | 60.00 |
| Recommended | C-06 to C-08 | 30% | 30.00 |
| Aspirational | C-09 to C-48 | 10% | 10.00 |
| **Total** | | | **100.00** |

**Aspirational ceiling**: 40 × 0.250 = 10.00 pts

---

## Version History

| Version | Round | New Criteria | Change |
|---------|-------|-------------|--------|
| v1 | R1 | C-01–C-11 | Initial rubric |
| v2–v10 | R2–R10 | C-12–C-37 | Accumulated excellence signals |
| v11 | R11 | C-38–C-39 | Global standards registry, rejection immutability |
| v12 | R12 | C-40–C-41 | Gap Record field template, Phase 3E entity stratification |
| v13 | R13 | C-42–C-43 | APPLICATION SENTENCE, Phase 3E Pass 2 stratification |
| v14 | R15 | C-44–C-45 | APPLICATION SENTENCE gate, Phase 3E all-rows exit gate |
| **v15** | **R16** | **C-46–C-48** | **Per-phase exit contract seal (PART 0), Phase 3E row independence contract (PART 0), imperative modal register** |
