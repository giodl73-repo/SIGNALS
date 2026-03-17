Written to `simulations/quest/golden/flow-trigger-variate-R16-2026-03-16.md`.

---

# flow-trigger — Round 16 (Rubric v13) Variations

**New criterion:** C-40 — detection-mechanism-bound attribution rationale. The C-39 dual-time attribution rationale must be embedded as a named note block *inside* the CLOSURE CHECK counter block, not in a separable section before or after it.

**R15 gap analysis:** All five R15 variations fail C-40. V-01–V-03 fail via C-39 non-pass (N/A path). V-04 and V-05 both achieve C-39 PASS but place the ATTRIBUTION CHAIN DESIGN RATIONALE section *after* the closing code fence — adjacent to the CLOSURE CHECK, not inside it. C-40 FAIL for both.

---

## Variation ladder

| V | C-38 | C-39 | C-40 | Axis | Structural mechanism |
|---|------|------|------|------|----------------------|
| V-01 | PASS | FAIL | N/A | Role sequence | Post-fence note = structural inventory only; no removal consequence |
| V-02 | WEAK PASS | WEAK PASS | WEAK PASS | Output format | Inline sentence appended to last counter line; no named block title |
| V-03 | PASS | PASS | FAIL | Lifecycle emphasis | Standalone ATTRIBUTION CHAIN section *before* the CLOSURE CHECK block |
| V-04 | PASS | PASS | WEAK PASS | Inertia framing | INERTIA CONTRAST entry covers attribution chain — outside CLOSURE CHECK |
| V-05 | PASS | PASS | **PASS** | Phrasing register + inseparability | `---- NOTE: ATTRIBUTION CHAIN DESIGN RATIONALE ----` embedded inside the code fence |

## Key structural insight

The C-40 ladder isolates three positions for the rationale:
- **Before** the CLOSURE CHECK block (V-03): C-39 PASS, C-40 FAIL
- **After** the closing fence (R15 V-04, V-05): C-39 PASS, C-40 FAIL  
- **Outside via INERTIA CONTRAST** (V-04): C-39 PASS, C-40 WEAK PASS
- **Inside the code fence** (V-05): C-39 PASS, C-40 PASS

V-05's `---- NOTE ... ---- END NOTE ----` structure makes the rationale structurally inseparable from the counters: removing it requires editing the CLOSURE CHECK fence content, converting silent deletion into a detectable structural change.
