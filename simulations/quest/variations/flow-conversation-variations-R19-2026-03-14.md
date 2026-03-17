Written to `simulations/quest/rubrics/flow-conversation-rubric-v18-variations-R19-2026-03-15.md`.

---

## Round 19 Variations — flow-conversation (v18 rubric, max 250)

### Axes selected

| Axis | Label | Criteria targeted |
|------|-------|-------------------|
| Z | Lifecycle single-source closure | C-76 |
| Y | Gate self-description completeness | C-75 |
| Phrasing register | CONSTRAINT/MUST/PROHIBITED language | control |

---

### V-01 — Axis Z: Single-Source Closure (C-76 target)

**Hypothesis:** R18 achieved C-73 (LIFECYCLE_POINTER_AUDIT) and C-70 (pointer-only role instructions) as independent passes, but never named C-76 — the *property* that together they close two distinct enforcement layers. This variation makes the closure framing explicit: LIFECYCLE_PROTOCOL section = declaration layer (no re-declarations); LIFECYCLE_POINTER_AUDIT = reference layer (no dangling pointers). Gate uses simple sweep toggle (C-69, no scope) and simple parenthetical toggle (C-71, no citation) — C-75 is not introduced.

---

### V-02 — Axis Y: Gate Self-Description (C-75 target)

**Hypothesis:** R18 V-02 had sweep-scope citation only (C-72); R18 V-03 had parenthetical declaration citation only (C-74). C-75 requires both simultaneously in the same gate. This variation introduces the combined gate format for the first time: WRONG_SCHEMA_RESIDUAL_SWEEP names its scope AND PARENTHETICAL_VERIFICATION names its declarations and row counts in the same CONTRACT_AUDIT_GATE_HONORED block. Lifecycle is inline — C-76 not addressed.

---

### V-03 — Phrasing register: Formal CONSTRAINT language (control)

**Hypothesis:** CONSTRAINT/MUST/PROHIBITED framing throughout all role boundaries and schema requirements may improve essential/recommended criterion adherence without introducing C-75 or C-76. Tests whether phrasing register is compositionally independent from the two structural axes, enabling clean combination in V-05.

---

### V-04 — Axes Z + Y (C-76 + C-75)

Combines V-01's LIFECYCLE_PROTOCOL / LIFECYCLE_POINTER_AUDIT (Axis Z) with V-02's self-describing gate format (Axis Y). First variation to target both new R19 criteria simultaneously.

---

### V-05 — Axes Z + Y + Phrasing register (full R19 combination)

All three axes. SOLE_AUTHORITY + pointer-only + LIFECYCLE_POINTER_AUDIT (C-76); both citation axes in gate (C-75); CONSTRAINT/MUST/PROHIBITED framing throughout. Tests whether phrasing register reinforces enforceability of both new criteria beyond the structural axes alone.

---

### Chain coverage summary

| New criterion | Chain | Variations that activate it |
|---|---|---|
| C-75 | C-72 ∧ C-74 (dual-axis convergence in gate) | V-02, V-04, V-05 |
| C-76 | C-73 → C-70 → C-66 → C-63 (reference-layer closure) | V-01, V-04, V-05 |
