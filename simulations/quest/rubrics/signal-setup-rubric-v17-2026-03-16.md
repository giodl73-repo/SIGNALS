Written to `simulations/quest/rubrics/signal-setup-rubric-v17-2026-03-17.md`.

---

**What changed in v17:**

Two new criteria extracted from R18 C-31 excellence patterns — both addressing multi-level sub-gate identifier encoding:

| ID | Pattern | Source | Denomination |
|----|---------|--------|--------------|
| C-41 | Depth-2 sub-gate identifiers extend the parent chain by one encoding unit per level | V-04 `GATE 6AA/6AB`; V-05 `GATE 6CP-Found/6CP-Write` | Structural extension: letter-slot uses letter-concatenation (`6A → 6AA`); word-suffix uses number+abbreviation+word (`6-Copilot → 6CP-Found`) — same recursive principle, scheme-appropriate form |
| C-42 | In word-suffix schemes, depth-2 parent abbreviations are unambiguous among siblings | V-05 `6CP` for `6-Copilot` — unambiguous because no other branch of GATE 6 compresses to the same prefix | Integrity constraint: C-41 requires the abbreviation to exist; C-42 requires it to be interpretable — two sibling branches that both compress to the same prefix fail even if each individually satisfies C-41 |

**Denominator: A=40 → A=42**

The C-41/C-42 pair extends the C-25/C-31 pair one level deeper: C-25 requires first-level parent encoding; C-41 requires that to hold recursively at every depth. C-31 requires scheme uniformity; C-42 requires that the abbreviation step word-suffix schemes introduce for nesting remains non-colliding. Letter-slot specs pass C-42 vacuously — no abbreviation step, no collision risk.
