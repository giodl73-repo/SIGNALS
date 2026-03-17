Written to `simulations/quest/rubrics/flow-conversation-rubric-v8-variations-R9-2026-03-14.md`.

---

## Round 9 Variations — flow-conversation (v8 rubric)

**Variation axes used:**
- Single-axis A: Role sequence
- Single-axis B: Lifecycle emphasis (new artifact)
- Single-axis C: Output format (remediation table)
- Combined A+B
- Combined C + phrasing register

---

### V-01 — Topology Architect Role (Axis A, role sequence)
Inserts a `TOPOLOGY_ARCHITECT` role before Developer. Produces a **signed topology contract** that both Developer and Auditor are downstream consumers of. Developer must declare `CONTRACT_GAPS` if it discovers topology elements absent from the Phase 0-A contract. Auditor validates consistency back to the Architect's artifact, not to Developer declarations.

**New structural pattern:** Separates topology authorship from execution tracing — prevents the Developer from implicitly constructing graph structure while tracing, and eliminates Auditor inference from execution evidence. Introduces `SLOT_PATH_MAP` as a Phase 0-A-4 pre-computation (six defect classes: adds `SLOT_GAP`). Phase 6-D audits `REMEDIATION_SEQUENCE` topological order.

**Candidate criterion:** `C-25` — Topology contract provenance: Developer trace bound to a prior-role artifact, `CONTRACT_GAPS` typed enum, multi-role chain.

---

### V-02 — Slot-Path Coverage Map (Axis B, lifecycle emphasis)
Adds `Phase 0-D-7 SLOT_PATH_MAP` as a **third pre-computation artifact** orthogonal to REACHABILITY_MAP (C-19) and TRANSITION_MAP (C-22). Tracks canonical and short-circuit slot-fill paths. Phase 1-S reports `EXERCISED | UNEXERCISED | PARTIAL` per declared path. Phase 5 adds a third ratio: `slot_paths_exercised / total_declared`.

**New structural pattern:** Unexercised canonical slot-fill path = `SLOT_GAP` defect — sixth structural defect class at slot-graph level, invisible to both topic-level (C-19) and edge-level (C-22) coverage. Short-circuit paths (user provides all entities upfront) are a distinct sub-class with their own coverage signal.

**Candidate criterion:** `C-25` — SLOT_PATH_MAP with `SLOT_GAP` defect class and three-ratio coverage (topic + edge + slot-path).

---

### V-03 — Remediation Sequence Table (Axis C, output format)
Adds `Phase 4-R REMEDIATION_SEQUENCE` — an ordered fix table derived from C-23 ENTANGLEMENT_MAP. Rules: `ISOLATED` defects have no blocking dependency; `ENABLES` sources must be fixed in causal order; `MASKED_BY` defects cannot be addressed until the masking defect is fixed. Phase 6-D audits for topological validity and cycle detection.

**New structural pattern:** Converts entanglement metadata into an actionable, ordered work plan with explicit `DEPENDS_ON_FIX_ORDERS` and `UNBLOCKS_FIX_ORDERS`. `REMEDIATION_CYCLE` is a named structural failure (escalated to P0). Phase 5 adds `REMEDIATION_DEPTH = defects_with_dependency / total_found`.

**Candidate criterion:** `C-26` — REMEDIATION_SEQUENCE with topological ordering, cycle detection, and Phase 6-D audit gate.

---

### V-04 — Topology Architect + Session Timeline (Combined A+B)
Topology Architect adds `Phase 0-A-6 SESSION_VARIABLE_TIMELINE_CONTRACT` declaring each variable's lifecycle: first-write topic, persistence, cleared-by topic, `READ_AFTER_CLEARED: FORBIDDEN | ALLOWED`. Developer produces `Phase 1-S SESSION_TIMELINE` — turn-indexed log of every state mutation (WRITE | READ | CLEAR | NO_CHANGE), additive to Phase 1 and Phase 1-T. `TIMELINE_ANOMALY: YES` when a variable is read after contract-declared clearing.

**New structural pattern:** `TIMELINE_ANOMALY` = seventh structural defect class at state-ordering level — invisible to topic, edge, and slot-path coverage. Phase 6-E audits SESSION_TIMELINE consistency against Phase 1 SESSION_STATE column. Phase 5 adds `TIMELINE_ANOMALY_RATE = anomalies / total_mutations`.

**Candidate criterion:** `C-27` — SESSION_TIMELINE with TIMELINE_ANOMALY defect class and Phase 6-E audit.

---

### V-05 — Remediation Sequence, Conversational Register (Combined C + phrasing)
Keeps full structural typing from v8 but delivers Phase 4-R in **conversational, second-person imperative register**: numbered fix blocks in plain English with two-sentence rationale, explicit "depends on / unblocks" in prose, ending with a compact `FIX_ORDER | DEFECT_CLASS | DEPENDS_ON | UNBLOCKS` structural record. Phase 6 Audit 4 verifies topological order and rationale presence.

**Axis hypothesis:** Does the developer-facing section of the artifact read better in conversational register without sacrificing the structural typing constraints that C-13 and C-15 require? The structural record at the end of each fix block preserves machine-checkability; the prose rationale is the human signal.

**Candidate criterion:** Same as V-03 (`C-26`), testing register sensitivity independently.

---

### Summary Table

| Var | Axis | New Pattern | Candidate |
|-----|------|-------------|-----------|
| V-01 | Role sequence | Topology Architect contract provenance + `SLOT_GAP` | C-25 |
| V-02 | Lifecycle emphasis | `SLOT_PATH_MAP` + three-ratio coverage | C-25 |
| V-03 | Output format | `REMEDIATION_SEQUENCE` + topological ordering + cycle detection | C-26 |
| V-04 | Role + Lifecycle | `SESSION_TIMELINE` + `TIMELINE_ANOMALY` defect class | C-27 |
| V-05 | Output format + register | `REMEDIATION_SEQUENCE` in conversational imperative | C-26 |

V-01 and V-02 both target `C-25` from different entry angles — the Topology Architect makes SLOT_PATH_MAP a contract artifact, while V-02 makes it a Developer pre-declaration. If both pass, the stronger implementation (pre-role vs pre-declaration) informs whether contract provenance is a structurally necessary gate or just an organizational preference.
