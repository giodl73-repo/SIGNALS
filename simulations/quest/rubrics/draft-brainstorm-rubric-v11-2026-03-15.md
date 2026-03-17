All additions are in place. Here's the complete v11 rubric as output:

---

# draft-brainstorm Rubric — v11

*(1,047 lines, written to `simulations/quest/rubrics/draft-brainstorm-rubric-v11-2026-03-16.md`)*

## What changed from v10

**Two new criteria extracted from R10 excellence signals:**

### C-33 — Dual-Anchor Verbatim Full Parity *(r11 aspirational, 2.5 pts)*

Sharpens C-31. Signal: V-03 R10 scorecard explicitly notes **"Both anchors fully verbatim."** C-31 only requires verbatim at phase-entry anchor (b). C-33 additionally requires anchor (a) — the schema-definition point (column rule, Registry spec) — to also carry the full verbatim condition text with schema element names.

- V-03 R10 PASS: Selected? column rule states "(a) all 5 rows...AND (b) Selected? is blank" verbatim + GATE block at phase entry same conditions verbatim
- V-04 R10 PASS: Step 5 column rule verbatim + Step 8 GATE block verbatim
- V-02 R10 FAIL: anchor (b) verbatim (C-31 PASS) but anchor (a) carries schema property by name without full condition set
- V-01 R10 FAIL: both anchors are label-references

### C-34 — Negation Frame Comparison-Goal Qualification *(r11 aspirational, 2.5 pts)*

Sharpens C-32. Signal: V-01/V-03/V-04 R10 all use "the impulse to revise **so the comparison can pass** is not permission to reopen the comparison" — the "so the comparison can pass" qualifier names the *goal* of the negated impulse. C-32 passes with any negation+affirmation frame alongside the C-30 causal trigger; C-34 passes only when the negation frame is comparison-goal-qualified, eliminating residual latitude where the prohibition could apply to unrelated revision impulses.

- V-01/V-03/V-04 R10 PASS: "so the comparison can pass" present in negation frame
- V-02 R10 FAIL: "the desire to revise" — no comparison-goal qualifier (also fails C-30/C-32)

**Lineage:**
```
C-31  phase-entry verbatim?
  C-33  both anchors verbatim?

C-32  dual-frame: negation + affirmation?
  C-34  negation frame names comparison-goal ("so the comparison can pass")?
```

**Max raised: 155 → 160.**

**R10 projected scores under v11:**
- V-03 R10: **160** (C-33 PASS + C-34 PASS — first to achieve 160, tied with V-04)
- V-04 R10: **160** (C-33 PASS + C-34 PASS)
- V-01 R10: **155** (C-33 FAIL, C-34 PASS)
- V-02 R10: **150** (C-33 FAIL, C-34 FAIL)
