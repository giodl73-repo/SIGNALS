Written to `simulations/quest/golden/prove-topic-variate-R9-2026-03-16-v9.md`.

---

## prove-topic -- Variation Round R9 (rubric v9)

Five complete, runnable prompts targeting **C-33** and **C-34** -- the two new v9 criteria.

---

### Variation axes

| Var | Axis | Key structural change |
|-----|------|-----------------------|
| **V-01** | CAMPAIGN CLOSURE CANONICAL FORM | Adds a pre-registered block (before roles execute) naming the exact terminal form. Stage 5 EXIT SIGNAL echoes it with "Echoing registered CAMPAIGN CLOSURE CANONICAL FORM:" -- two-layer enforcement for C-33, analogous to C-14 for inline labels. |
| **V-02** | Synthesis Evidence Mandate as Invariant E | Adds a 5th SESSION INVARIANTS row (Invariant E: SYNTHESIS EVIDENCE MANDATE, failure label `SYNTHESIS-FAIL`). SYNTHESIS DECLARATIONS evidence_summary echoes "SESSION INVARIANTS Invariant E active" inline -- two-layer enforcement for C-34. |
| **V-03** | Stage 0 EXIT SIGNAL pre-commits closure + mandate | Stage 0 `gate_open` EXIT SIGNAL registers two named forward-commitments (`synthesis_closure_form: 'Chain closed.'` and `synthesis_mandate_label: Omission = FAIL`). Stage 5 ENTRY CONDITIONS verify them by name -- Stage 0 → Stage 5 closure chain. |
| **V-04** | V-01 + V-02 | CAMPAIGN CLOSURE CANONICAL FORM + Invariant E combined. |
| **V-05** | V-01 + V-02 + V-03 + dual-lock label precision | Full integration. Block 3 dual-lock now appends `"(DUAL-LOCK ERROR if bypassed)"` at each lock step, precisely echoing the registered label from SESSION INVARIANTS A and B -- fixes the C-14 partial from R8. |

### All 5 pass C-33 and C-34 by design
Every variation carries the R8 V-05 baseline: `"Chain closed."` terminal in EXIT SIGNAL (C-33) and `"Omission of any artifact Displacement read = FAIL."` in evidence_summary instruction (C-34).

### New excellence signal candidates (potential C-35+)
- **V-01/V-04/V-05**: Stage 5 EXIT SIGNAL cites the CAMPAIGN CLOSURE CANONICAL FORM by registered name -- full two-layer enforcement for C-33
- **V-02/V-04/V-05**: evidence_summary echoes "Invariant E" by registered name -- full two-layer enforcement for C-34
- **V-03/V-05**: Stage 0 EXIT SIGNAL names `synthesis_closure_form` and `synthesis_mandate_label` as explicit forward-commitments verified at Stage 5 entry
- **V-05 only**: Block 3 dual-lock echoes `"DUAL-LOCK ERROR"` precisely at each lock step -- fixes C-14 partial
