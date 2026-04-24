Written to `simulations/quest/golden/topic-echo-variate-R15-2026-03-15.md`.

**R15 summary:**

- **rubric_max:** 213 (up from 204)
- **3 new criteria:** C-50, C-51, C-52 -- all sourced from R14 V-05 excellence signals
- **17 nodes, 14 deps** (V-01/V-04/V-05) or **13 deps** (V-02/V-03)

**Variation axes:**

| Variation | Axis | C-50 | C-51 | C-52 | Deps |
|-----------|------|------|------|------|------|
| V-01 | Per-site dep entries | PASS | FAIL | FAIL | 14 |
| V-02 | Ordering annotation | FAIL | PASS | FAIL | 13 |
| V-03 | Self-inventorying tag | FAIL | FAIL | PASS | 13 |
| V-04 | Per-site + ordering | PASS | PASS | FAIL | 14 |
| V-05 | Full synthesis | PASS | PASS | PASS | 14 |

**Key structural changes per criterion:**
- **C-50:** NODE 14 `consumed by` splits into two separate per-site lines (step header vs. authority block) -- replaces the combined entry
- **C-51:** Authority block gains `[C-51: C-48 citation is LINE 1 -- precondition before compliance footprint]` annotation; C-47 block tagged `[C-51: positioned AFTER C-48]`
- **C-52:** Dep closure enumeration's closing tag gains `C-52 self-inventorying closure -- this tag names C-52` making the tag self-referential
