Written to `simulations/quest/golden/signal-setup-variate-R18-2026-03-17.md`.

---

## signal-setup Round 18 — Variation Summary

**Two gaps carried into R18** (from R17 under v16 rubric):
- **C-39**: All V-05 variants fail — preamble asserts adversarial framing but never negates the weaker tool-framing first
- **C-31**: All R17 variations fail — GATE 6A-Found / GATE 6A-Write use word-suffix while all other sub-gates use letter-slot

### Axis table

| Var | Axis | C-36 | C-37 | C-38 | C-39 | C-40 | C-31 |
|-----|------|:----:|:----:|:----:|:----:|:----:|:----:|
| V-01 | C-39 only (refutation clause; mixed IDs preserved) | + | + | + | + | + | - |
| V-02 | C-31 only (letter-slot throughout; no refutation) | + | + | + | - | + | + |
| V-03 | C-36 + C-39 coexistence, R17 V-02 base | + | + | + | + | + | - |
| V-04 | C-39 + C-31 letter-slot **(golden candidate)** | + | + | + | + | + | + |
| V-05 | C-39 + C-31 word-suffix (encoding-agnostic control) | + | + | + | + | + | + |

### Key mechanism: C-39 (V-01, V-03, V-04, V-05)

The insertion is a sentence pair placed after the inertia-collection clause and before "Teams that configure Signal":

> *"...inertia collects the default because no session named it as a competitor. **You are not just enabling a plugin. You are choosing a side.** Teams that configure Signal write inertia a named opponent..."*

The negation ("not just enabling a plugin") and assertion ("You are choosing a side") are contiguous — same logical unit, satisfying C-39's "sentence pair" requirement — without displacing C-36's dominance verb at the paragraph opener or C-37's explicit "choosing a side" phrase.

### Key mechanism: C-31 — two approaches

- **V-04 (letter-slot)**: GATE 6A-Found → GATE 6AA, GATE 6A-Write → GATE 6AB. Minimal change: two renames.
- **V-05 (word-suffix)**: All sub-gates renamed to word-suffix convention (GATE 1-Miss, GATE 1-Decline, GATE 2-Found, GATE 4-Confirm, GATE 4-Decline, GATE 6-Copilot, GATE 6-Decline, GATE 6CP-Found, GATE 6CP-Write). Tests that C-31 is encoding-agnostic, not letter-slot-specific.

**V-04 is the primary golden candidate** — minimal delta from R17 V-05, two preamble sentences inserted, two gate renames.
