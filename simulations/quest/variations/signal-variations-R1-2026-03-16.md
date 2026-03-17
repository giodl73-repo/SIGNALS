Written to `simulations/quest/golden/signal-variate-R1-2026-03-16.md`.

---

## Quest Variate — /signal (Round 1)

5 complete variations generated. Each is a runnable SKILL.md body.

### Variation Summary

| ID | Axis | Key Hypothesis | C-09 | C-10 | C-08 |
|----|------|----------------|------|------|------|
| **V-01** | Output format: indented list | CLAUDE.md-familiar format, visual hierarchy built-in | No | No | Yes |
| **V-02** | Phrasing register: declarative/imperative | Explicit rules produce less-drifting, more complete output | No | No | Yes |
| **V-03** | Visual hierarchy: section headers with counts | Count-in-header satisfies C-09 aspirational natively | Yes | No | Yes |
| **V-04** | Routing-first + count headers | Front-loaded routing guide collapses nav time | Yes | No | Yes* |
| **V-05** | Full integration | All axes combined — highest expected composite | Yes | Yes | Yes |

### Design notes

**Single-axis choices** (V-01/V-02/V-03): Each isolates one hypothesis about what drives rubric score. V-01 vs V-02 test whether _format familiarity_ or _imperative precision_ better controls output fidelity. V-03 tests whether count-in-header improves scannability enough to justify the structural change.

**Combinations** (V-04/V-05): V-04 adds a routing decision tree at the top — tests whether global routing guidance is more usable than per-section tips alone. V-05 stacks everything including T3 annotations, targeting the two aspirational criteria (C-09, C-10).

**Expected leaderboard**: V-05 > V-03 > V-04 > V-01 > V-02, but V-02's precision may surface correctness advantages on the essential criteria that format-heavy variations miss.
