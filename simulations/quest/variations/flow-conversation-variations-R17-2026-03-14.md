Written to `simulations/quest/rubrics/flow-conversation-rubric-v16-variations-R17-2026-03-15.md`.

---

## Quest Variations — flow-conversation — Round 17 (v16 rubric)

**Date:** 2026-03-15 | **Rubric version:** v16 | **Max score:** 240

---

### Variation Axes Selected

Three single-axis, two combined — targeting C-69, C-70, C-71:

| Axis | Criterion | Mechanism |
|------|-----------|-----------|
| S — Lifecycle single-source | C-70 | SOLE_AUTHORITY declaration in LIFECYCLE_PROTOCOL section; role instructions drop all inline HANDOFF_TO/Received strings and use pointer-only references ("per LIFECYCLE_PROTOCOL Transition N") |
| T — Gate sweep precondition | C-69 | WRONG_SCHEMA_RESIDUAL_SWEEP becomes the **first field** in CONTRACT_AUDIT_GATE_HONORED, not a parallel block the gate ignores; sweep FINDINGS_PRESENT forces NOT_CONFIRMED and gate FAIL |
| U — Gate parenthetical precondition | C-71 | PARENTHETICAL_VERIFICATION becomes the **second gate field** in CONTRACT_AUDIT_GATE_HONORED, paired with the sweep field; a gate without it has not covered the full Phase 0-CA-1 output contract |

---

### V-01 — Axis S (Lifecycle single-source, C-70 target)

**Key move:** LIFECYCLE_PROTOCOL section adds `SOLE_AUTHORITY` — explicitly forbids any HANDOFF_TO or Received string outside the section. Every role instruction uses pointer language only: "Close per LIFECYCLE_PROTOCOL Transition 1 outgoing." The actual tokens appear in exactly one place.

**Hypothesis:** R16 V-01/V-04/V-05 had dedicated sections but still re-declared token values inline ("Close with LIFECYCLE_PROTOCOL Transition 1 token: **HANDOFF_TO: ...**"). C-70 identifies this as two-source — section and role instruction both carry the token. Removing all inline values and declaring SOLE_AUTHORITY satisfies C-70 while C-69/C-71 remain unaddressed (gate uses standalone blocks only, sweep/parenthetical not embedded in gate assertion).

---

### V-02 — Axis T (Gate sweep precondition, C-69 target)

**Key move:** WRONG_SCHEMA_RESIDUAL_CHECK runs as a standalone table first (C-67 satisfied). Its `WRONG_SCHEMA_RESIDUAL_SWEEP` result is then consumed as the **first field** in CONTRACT_AUDIT_GATE_HONORED — before PRE_FLIGHT_MANIFEST_STATUS. Lifecycle protocol stays inline (C-70 unaddressed). No parenthetical field in gate (C-71 unaddressed).

**Hypothesis:** In R16 V-02/V-04 the standalone block ran but the gate did not reference it. C-69 requires structural consumption — the gate's first assertion must be the sweep confirmation, making it impossible for the gate to assert HONORED while ignoring a sweep finding.

---

### V-03 — Axis U (Gate parenthetical precondition, C-71 target)

**Key move:** Parallel to V-02 but for parentheticals. PARENTHETICAL_PRESENCE_VERIFICATION runs as a standalone table; its `PARENTHETICAL_VERIFICATION` status appears as the second field in CONTRACT_AUDIT_GATE_HONORED (after WRONG_SCHEMA_RESIDUAL_SWEEP). Uses formal imperative constraint phrasing throughout (MUST NOT, PROHIBITED, CONSTRAINT VIOLATION, INCOMPLETE_GATE_ASSERTION). Inline protocol (C-70 unaddressed).

**Hypothesis:** R16 V-03 had a standalone parenthetical table but the gate didn't reference it. C-71 requires parenthetical status to propagate into the gate assertion as a named precondition field. The imperative phrasing axis strengthens the structural obligation signal.

---

### V-04 — Axes S+T (C-70+C-69)

**Key move:** Dedicated LIFECYCLE_PROTOCOL section with SOLE_AUTHORITY (C-70) + WRONG_SCHEMA_RESIDUAL_SWEEP as first gate field (C-69). PARENTHETICAL_VERIFICATION stays standalone-only (C-71 unaddressed).

**Hypothesis:** S and T are independent enforcement channels — protocol structure and gate structure. Combined they satisfy two of three new criteria. Leaving C-71 out isolates the gate parenthetical field as the remaining delta for V-05.

---

### V-05 — Axes S+T+U (Full R17, C-70+C-69+C-71)

**Key move:** All three axes. SOLE_AUTHORITY section + pointer-only roles (C-70). WRONG_SCHEMA_RESIDUAL_SWEEP as Block 3 first gate field (C-69). PARENTHETICAL_VERIFICATION as Block 3 second gate field (C-71). Phase 6-A is explicitly structured as three sequential blocks — Blocks 1 and 2 run first and their results are consumed by Block 3's gate assertion. A gate without both precondition fields confirmed is `INCOMPLETE_GATE_ASSERTION`.

**Hypothesis:** The two gate precondition fields form a logical pair — Block 1 checks schema-type compliance (WRONG_SCHEMA), Block 2 checks declaration completeness (row count parentheticals). Together they constitute the full Phase 0-CA-1 output audit summary embedded in the gate. V-05 should satisfy C-70 + C-69 + C-71 simultaneously.

---

### Chain Structure

```
C-70 → C-66: single-source token authority → dedicated section prerequisite
C-69 → C-67 → C-64: gate first field → Phase 6-A sweep → manifest detection
C-71 → C-68 → C-65: gate second field → Phase 6-A parenthetical check → CA output contract
```

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| **C-70** (SOLE_AUTHORITY; pointer-only role instructions) | TARGET | — | — | TARGET | TARGET |
| **C-69** (sweep as first gate field) | — | TARGET | — | TARGET | TARGET |
| **C-71** (parenthetical as gate field) | — | — | TARGET | — | TARGET |
| C-66 (dedicated LIFECYCLE_PROTOCOL section) | PASS | — | — | PASS | PASS |
| C-67 (WRONG_SCHEMA_RESIDUAL_CHECK with findings) | PASS | PASS | PASS | PASS | PASS |
| C-68 (PARENTHETICAL_PRESENCE_VERIFICATION with findings) | PASS | PASS | PASS | PASS | PASS |
