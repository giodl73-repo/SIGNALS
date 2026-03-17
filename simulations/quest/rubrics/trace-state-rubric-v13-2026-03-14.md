Looking at the R13 scorecard, I need to identify what genuinely new structural patterns the evidence reveals beyond v12's C-01–C-41.

**New patterns from R13:**

**V-02 (C-36 PASS, fully expanded)** introduces two structural specifics not named in any existing criterion:

- `"THE SCORING PROTOCOL with registry-specific scoring sentence"` — C-35 mandates verbatim restate of the Standards Registry row before detection begins. V-02 adds a distinct *application sentence* that maps the registry standard to the specific phase's anomaly type. Restating `"Strength ≥ 2 required"` is not the same as stating `"For OP-ID race conditions, strength ≥ 2 means: two concurrent trace steps must share the same S-ID with no intervening lock assertion."` The restate is passive; the application sentence is an active mechanical binding of the generic threshold to the phase-specific evidence shape.

- `"Pass 2 with three independent entity-class sub-scans (P2-S/P2-O/P2-I)"` — C-41 mandates Pass 1 in Phase 3E is stratified per entity class. V-02 extends stratification to Pass 2 (Trace-Diff scan) as well, with P2-S, P2-O, P2-I as independent sub-scans. Without this, a passing P1-S scan can mask a completely absent Pass 2 OP-ID trace-diff check — the same structural loophole C-41 closes for Pass 1 now reappears in Pass 2.

These are **C-42** and **C-43**. Point value: 10 / 35 = 0.286 pts each (aspirational bucket grows from 33 to 35 criteria).

---

```markdown
# trace-state Rubric v13
**Updated**: 2026-03-15
**Change**: Added C-42, C-43 from R13 excellence signals (phase scoring protocol
with registry-specific application sentence making the per-phase evidence standard
mechanically traceable beyond verbatim restate; Phase 3E Pass 2 entity-type
stratification mirroring C-41's Pass 1 requirement so Trace-Diff checking cannot
mask absent OP-ID or INV-ID coverage behind a passing S-ID sub-scan).
Aspirational point value updated: 10 / 35 = 0.286 pts each.

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
- C-11 through C-43: see full list below (accumulated from R1–R13 excellence signals)

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
- **C-40**: Gap Record structured field template — the Gap Record uses a fixed named-field template (e.g., `Examined:`, `Evidence Standard Applied:`, `What Was Not Found:`, `What Would Constitute a Finding:`, `Verdict:`) rather than free-form prose; the field structure makes Gap Records machine-comparable across phases and transforms the absence record from a written acquittal into a structured diagnostic artifact; a Gap Record that omits a required field is a detectable mechanical error, not a prose judgment call; elevates C-34's artifact-driven gate from "a record exists" to "a structurally complete record exists" (R12 excellence signal)
- **C-41**: Phase 3E entity-type-stratified scan — Pass 1 in Phase 3E issues distinct scanning instructions per reference entity class (S-ID scan, OP-ID scan, INV-ID scan) rather than a single generic "scan for undeclared references"; each entity class receives its own sweep row in the Phase 3E finding table with Declaration-Only and Trace-Diff columns; a sweep verdict on one entity class cannot satisfy the sweep requirement for another; closes the loophole where detecting S-ID undeclared references masks a complete absence of OP-ID or INV-ID checking, and makes Phase 3E coverage gaps detectable by row rather than requiring full-trace inspection (R12 excellence signal)
- **C-42**: phase scoring protocol with registry-specific application sentence — beyond verbatim restating the Standards Registry row (C-35), each phase contains a named scoring protocol section (e.g., "THE SCORING PROTOCOL") that includes a registry-specific application sentence explicitly mapping the generic evidence threshold to the phase's anomaly type (e.g., "For OP-ID race conditions, strength ≥ 2 means: two concurrent trace steps share the same S-ID with no intervening lock assertion"); the application sentence is a distinct artifact from the restate and cannot be satisfied by the restate alone; transforms C-35's passive reference into an active standard-application statement where the evaluator's intended threshold for that specific anomaly class is mechanically traceable rather than inferred from the generic registry entry (R13 excellence signal)
- **C-43**: Phase 3E Pass 2 entity-type stratification — Pass 2 (Trace-Diff scan) in Phase 3E issues distinct scanning instructions per reference entity class (P2-S, P2-O, P2-I) mirroring C-41's Pass 1 stratification requirement; each entity class receives its own independent Trace-Diff sub-scan; a Trace-Diff verdict on one entity class cannot satisfy the Trace-Diff requirement for another; closes the loophole where C-41's Pass 1 stratification is fully satisfied but Pass 2 uses a single unified scan that absorbs absent OP-ID or INV-ID trace-diff checking into a passing S-ID verdict — the same structural gap C-41 closes for Pass 1 reappears in Pass 2 unless both passes are independently stratified (R13 excellence signal)
```
