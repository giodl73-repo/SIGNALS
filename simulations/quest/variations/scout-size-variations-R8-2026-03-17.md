Written to `simulations/quest/golden/scout-size-variate-R8-2026-03-17.md`.

---

## scout-size — Prompt Variations R8

**R8 gap being closed**: R7 V-04/V-05 score 18/19 under v8 — fail C-26 only. R7 V-02 passes C-26 but fails C-27. No single R7 variation has both.

**R8 design**: Both new criteria are orthogonal and have different structural homes — C-26 lives entirely in SYNTHESIS; C-27 lives in OPEN UNKNOWNS and SYNTHESIS simultaneously.

---

### V-01 — Axis: Structural AMEND re-evaluation directive (C-26)

**Base**: R7 V-03. **Single addition**: SYNTHESIS gains a `**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**` that states the requirement applies on every invocation — not conditional on AMEND firing, not framed as a criterion reference. **C-27 intentionally absent**: SYNTHESIS retains inline `> **Anti-pattern**:` blockquote; OPEN UNKNOWNS retains inline "A generic placeholder fails."

**Discriminator from R7 AMEND INSTRUCTION**: R7 V-04/V-05 say "If an AMEND directive is present in this invocation...it fails C-16" — conditional scope + criterion reference = fails C-26. R8 V-01 says "applies on every invocation, independent of whether an AMEND directive is present...structural failure of this section's integrity" — unconditional scope + structural framing = passes C-26.

**Expected**: 18/19 (fails C-27 only)

---

### V-02 — Axis: Dedicated FAILURE MODE blocks (C-27)

**Base**: R7 V-03. **Single addition**: both OPEN UNKNOWNS and SYNTHESIS gain a dedicated `> **FAILURE MODE FOR THIS SECTION**:` blockquote as a standalone structural element placed before the field requirements. **C-26 intentionally absent**: no AMEND directive appears in SYNTHESIS.

**Discriminator from inline failure-mode text**: R7 V-03 SYNTHESIS has `> **Anti-pattern**: Restating...` (inline annotation inside instruction prose) and OPEN UNKNOWNS has "A generic placeholder fails" (trailing sentence). Both pass C-17 (at least one section names failure mode) but fail C-27 because neither is a structurally separate labeled block whose absence leaves a visible gap.

**Expected**: 18/19 (fails C-26 only)

---

### V-03 — Axes: C-26 + C-27 minimal combination

**Base**: R7 V-03 (passes C-01–C-25). Both new mechanisms added: STRUCTURAL AMEND RE-EVALUATION DIRECTIVE in SYNTHESIS + dedicated FAILURE MODE blockquotes in both OPEN UNKNOWNS and SYNTHESIS. No self-check. If clean, this is the new minimum prompt for the v8 rubric.

**Expected**: 19/19

---

### V-04 — All R8 mechanisms + 27-criterion self-check

**Base**: R7 V-04 step-labeled structure. Changes: AMEND INSTRUCTION replaced with STRUCTURAL AMEND RE-EVALUATION DIRECTIVE (C-26); FAILURE MODE blocks retained (C-27 already present); self-check extended to 27 criteria with definition-level C-26/C-27 items.

**C-26 self-check item calls out the exact disqualifying form**: a directive ending "it fails C-16" fails C-26 even if present in synthesis.

**Expected**: 19/19

---

### V-05 — Full integration + structural definitions for C-26/C-27

**Base**: R7 V-05. Same changes as V-04 + self-check items for C-26 and C-27 extended with exact structural disqualifying conditions:

- **C-26 disqualifying form**: `**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation...it fails C-16` — "in this invocation" = conditional; "it fails C-16" = criterion-referenced. Both disqualifiers must be absent.
- **C-27 disqualifying form**: `> **Anti-pattern**: Restating sections in sequence is juxtaposition` in SYNTHESIS fails C-27 even if C-17 passes — embedded in instruction prose, not a standalone block. Same for "A generic placeholder fails" trailing sentence in OPEN UNKNOWNS.

**Expected**: 19/19

---

| ID | C-26 | C-27 | Expected score |
|----|------|------|----------------|
| V-01 | PASS | FAIL (intentional) | 99.47 |
| V-02 | FAIL (intentional) | PASS | 99.47 |
| V-03 | PASS | PASS | **100** |
| V-04 | PASS | PASS | **100** |
| V-05 | PASS | PASS | **100** |
