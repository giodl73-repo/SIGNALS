Written to `simulations/quest/rubrics/quest-rubric-mock-ns-v10-2026-03-15.md`.

**What changed in v10:**

Three new aspirational criteria extracted from Round 10 excellence signals:

**C-29 — Bidirectional navigation anchor** (depends on C-28)
The aspirational maximum seeded in v9 graduates to a pass condition. A-1 carries an explicit self-identification marker naming S-3 as the source of the cross-reference. 4/5 Round 10 variants demonstrated this (V-01, V-02, V-04, V-05). V-03 (forward-only) passes C-28 but fails C-29.

**C-30 — Bracket token notation** (depends on C-29)
Natural-language location descriptions replaced by structured identifiers (`[A-1:FC]`, `[S-3:CS]`) at both sites, forming a parseable token pair. V-02 and V-05 demonstrate this. Reduces navigation cost from prose parsing to token matching.

**C-31 — Pre-chain protocol preamble** (depends on C-30)
A dedicated orientation block before all prohibition rows names every token pair, states what each resolves to, and maps the complete bidirectional link structure before any row is read. V-05 uniquely demonstrates this. Reduces chain orientation from O(rows visited) to O(1).

**Scoring:** aspirational denominator 20 → 23 (`pass/23 * 10`).

**Escalation chain:** C-29 spans both sites (bidirectional); C-30 spans both sites (token pair); C-31 sits at the compute side (preamble precedes S-3 rows).
