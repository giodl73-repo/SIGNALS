# trace-contract — Round 10 Variation Scorecard (v10 Rubric, C-01–C-38, denominator /30)

**New criteria targeted:** C-35 (Phase Dependency Reference Table), C-36 (Named Inertia Correction Route Table), C-37 (Per-Finding Harm Propagation Fill Form), C-38 (STOP-Gate Execution Sequence Protocol — already achieved in R9 V-05; preserved in all R10 variations).

**Baseline:** R9 V-05 scores 26.5/30 — C-38 PASS, C-35 FAIL, C-36 FAIL, C-37 PARTIAL, C-17 FAIL.

**Single-axis variations (V-01 to V-04):** Each targets one open criterion against the R9 V-05 base.
**Combination variation (V-05):** Full integration of all four axes — Platinum target 30/30.

---

## Predicted Scores

| Variation | Axis | C-17 | C-35 | C-36 | C-37 | C-38 | Aspirational Total (/30) | Notes |
|-----------|------|------|------|------|------|------|--------------------------|-------|
| V-01 | Interrogative Primer | PASS | FAIL | FAIL | PARTIAL | PASS | 27/30 | C-17 closed; C-35/C-36/C-37 unchanged from R9 V-05 baseline |
| V-02 | Per-Finding Harm Fill Form | FAIL | FAIL | FAIL | PASS | PASS | 27.5/30 | C-37 upgraded from PARTIAL to PASS; C-17/C-35/C-36 unchanged |
| V-03 | Phase Dependency Reference Table | FAIL | PASS | FAIL | PARTIAL | PASS | 27.5/30 | C-35 closed via standalone pre-phase table with "Unblocked By" column; all others unchanged |
| V-04 | Named Inertia Correction Route Table | FAIL | FAIL | PASS | PARTIAL | PASS | 27.5/30 | C-36 closed via INERTIA CORRECTION ROUTES section with ROUTE-A/ROUTE-B; CASCADE GATE still present as per-finding tracker |
| V-05 | Combined (all four) | PASS | PASS | PASS | PASS | PASS | 30/30 | Platinum: all four R10 criteria closed; R9 V-05 base architecture preserved |

---

## Criterion-Level Analysis

### C-17 — Interrogative Primer Before Fill Form

**V-01 PASS mechanism:** "Ask first: [question]..." sentences appear as the first line of every phase containing a fill form (Phase 0, 1A, 1B, 2, 3, 4, 4B, 5). Each interrogative is a complete standalone sentence — not a gate item, not a label, not a heading. The sentence precedes the fill table or scaffold; it is structurally distinct. The question forces judgment resolution before execution: a writer who reads "Ask first: What does the spec say..." must state an answer before filling the form.

**V-02/V-03/V-04 FAIL:** These variations carry the R9 V-05 architecture with no interrogative primer modifications. The "CANNOT BEGIN UNTIL:" and "Inertia risk:" headers are not interrogatives — they are declarative guards. C-17 requires a distinct interrogative sentence, not a guard or instruction.

**V-05 PASS:** Inherits V-01's "Ask first: ..." structure applied consistently across all phases.

---

### C-35 — Phase Dependency Reference Table

**V-03 PASS mechanism:** A standalone `## Phase Dependency Reference Table` section appears before Phase 0 body and before any phase content. The table lists every phase as a row with an "Unblocked By" column populated with the specific prior gate each phase depends on. The table is structurally independent of the inline phase dependency chain that follows it — the two serve different purposes: the reference table provides global pre-execution visibility; the inline chain records cascade paths and gate key names. A reader consulting the reference table before entering any phase knows the full ordering without reading phase bodies.

**V-01/V-02/V-04 FAIL:** These variations carry R9 V-05's inline phase dependency chain. The chain has an "Unblocked By" column, but it is embedded after the role table, interleaved with cascade path rows (CASCADE-A, CASCADE-B), and is not a standalone upstream-of-all-phases table. C-35 requires the table to be upstream of all phase content and standalone.

**V-05 PASS:** Inherits V-03's standalone Phase Dependency Reference Table, positioned before Phase 0 body. The inline phase dependency chain is also retained for cascade path documentation.

---

### C-36 — Named Inertia Correction Route Table

**V-04 PASS mechanism:** A dedicated `## INERTIA CORRECTION ROUTES` section appears before Phase 4 (after Phase 3 and before the Phase 4 body). The section contains ROUTE-A (in-boundary) and ROUTE-B (out-of-boundary) as individually labeled routes, each carrying: (1) triggering condition, (2) complete step sequence in arrow notation from failure point to re-entry, (3) explicit upstream anchor for ROUTE-B. The section is standalone — not dispersed across gate repair blocks. The CASCADE GATE continues to exist as the per-finding execution tracker; the INERTIA CORRECTION ROUTES section is the global reference consulted before routing decisions are made. The two are structurally distinct: one defines routes; the other executes them per finding.

**V-01/V-02/V-03 FAIL:** These variations carry R9 V-05's CASCADE GATE with inline "Must NOT Visit" columns. The CASCADE GATE satisfies C-30 (branched repair cascade) and C-34 (negative route prohibition) but not C-36. C-36 requires a standalone named-route section that is its own reference, not a per-finding routing table.

**V-05 PASS:** Inherits V-04's INERTIA CORRECTION ROUTES section. CASCADE GATE also retained for per-finding route assignment.

---

### C-37 — Per-Finding Harm Propagation Fill Form

**V-02 PASS mechanism:** The finding scaffold includes "Harm if unresolved:" as a mandatory, structurally distinct field (separate labeled line, not a parenthetical inside Root Cause). The field is required for all inertia-classified findings. A Phase 4 gate check verifies that all inertia-classified findings have the field populated and that no field uses generic language. The field must name: (1) specific affected user, flow, or contract guarantee; (2) nature of the persistent deviation. This upgrades C-12 from PARTIAL (batch note) to C-37 PASS (per-finding fill form).

**V-01/V-03/V-04 PARTIAL:** These carry the R9 V-05 finding scaffold, which has Severity/Spec Ref/Root Cause/Resolution but no separate "Harm if unresolved:" field. The inertia-framing batch note at Phase 4B/Phase 5 level satisfies C-12 PARTIAL but not C-37.

**V-05 PASS:** Inherits V-02's "Harm if unresolved:" field in every finding scaffold, with Phase 4 gate check.

---

### C-38 — STOP-Gate Execution Sequence Protocol

**All variations PASS:** Every variation inherits R9 V-05's STOP markers at every phase transition. The STOP sequence forms an ordered execution protocol: a reader following STOP points in order encounters (1) the full phase sequence, (2) every gate closure confirmation, (3) every cascade re-entry point. The STOP markers carry enough context at each stop point (gate key name, phase identity, cascade destination if failed) that a second engineer can reconstruct the trace execution from the STOP sequence alone. This criterion was achieved in R9 V-05 and is preserved across all R10 variations.

---

## R10 Platinum gap (forward)

V-05 closes all four remaining gaps (C-17, C-35, C-36, C-37). Expected: 30/30.

If any criterion fails in V-05, the most likely candidates are:
- C-37 partial failure: "Harm if unresolved:" field populated but generic language used ("spec drift will continue") — gate check language addresses this but requires model compliance
- C-35 partial failure: Phase Dependency Reference Table present but incomplete (missing some phases) — the table template lists all phases explicitly, mitigating this risk
- C-17 partial failure: "Ask first: ..." present in some phases but missing in Phase 4 (most complex phase with multiple sub-elements) — the prompt applies it to Phase 4 explicitly

R11 axes to explore if V-05 falls short:
- C-37 enforcement: promote "Harm if unresolved:" to a required column in the DIFF TABLE (Phase 3), not just a scaffold field in Phase 4 — structural enforcement via empty-cell visibility
- C-35 extension: add "Cascade Route" column to Phase Dependency Reference Table to merge reference table and cascade routing into one global schema
- C-17 coverage: verify the interrogative appears at Phase 4's cascade sub-section (CASCADE GATE), not only at Phase 4 findings top
