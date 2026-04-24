Written to `simulations/quest/golden/scout-inertia-variate-R15-2026-03-17.md`.

---

## R15 Summary

**5 variations, all predicted 235/235.**

### Variation axes

| V | Axis | Changes from R14 |
|---|------|-----------------|
| V-01 | A-36 only (section-based index) | `BRIDGE COMPLETION GATE` → `SECTION 2 COMPLETION GATE` |
| V-02 | A-35 only (reference form) | 5 inline `[C-0N COMMAND]:` → blockquote `> [C-0N COMMAND]:` |
| V-03 | A-35+A-36 on phrasing-register scaffold | Blockquote C-0N + `SECTION 2 COMPLETION GATE` |
| V-04 | A-34 upgrade + A-35+A-36 on consolidated-bridge | `VULNERABILITIES` → `FAILURE POINTS`; blockquote C-0N; `STAGE 2 --` prefix on combined gate heading |
| V-05 | A-35+A-36 on all-axes-combined | Blockquote C-0N + `STAGE 2 COMPLETION GATE` |

### Key design decisions

**A-34 (FM heading subtitle)**: V-01/V-02 carried unchanged (confirmed). V-03 (`FAILURE SURFACE`) and V-05 (`BREAKING POINTS`) treated as satisfying A-34 without change — both have explicit failure-context nouns. V-04's `VULNERABILITIES` is the only borderline case, upgraded to `FAILURE POINTS` to ensure unambiguous satisfaction.

**A-35 (blockquote commands)**: Applied to all 5 C-0N criterion commands only. Bridge-specific commands ([BRIDGE Q3 COMMAND], [BRIDGE Q4 COMMAND], [BRIDGE COMPLETION COMMAND]) retain each variation's structural form — A-35 is scoped to per-criterion prompts.

**A-36 (position-indexed gate)**: V-01 and V-03 use `SECTION 2` (section-based structures). V-02 and V-05 use `STAGE 2 COMPLETION GATE`. V-04 uses `STAGE 2 --` as a prefix on the combined A-25+A-27 heading, testing whether the position index fires as a heading prefix rather than the heading's leading noun phrase.

### Open questions for scoring

- Does `SECTION N` satisfy A-36 equally to `STAGE N`, or does A-36 require "STAGE" specifically?
- Does `STAGE 2 --` as a prepended prefix on a combined heading satisfy A-36, or must the position index open the standalone gate heading?
- Does `FAILURE SURFACE` satisfy A-34 with the same confidence as `BREAKS` and `WEAKNESSES`?
