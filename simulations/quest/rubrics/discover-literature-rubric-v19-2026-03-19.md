Written to `simulations/quest/rubrics/discover-literature-rubric-v19-2026-03-20.md`.

**What changed v18 → v19:**

**C-37 — Chain-Completion Statement Extended to C-36 as Current Terminal** (5 pts)

The C-35 chain `C-14 + C-23 -> ... -> C-33 complete` must be extended to `... -> C-33 -> C-34 -> C-35 -> C-36 complete`. Exact parallel to C-35 catching R17's wrong-terminal failure (chain not updated from C-32 to C-33); C-37 catches the R18 equivalent.

**R18 boundary confirmations added** (four C-36 failure modes):
- V-01: both pairs named, analogy outside boundary — sub-clause (c) fails independently
- V-02: inside boundary, current pair only — sub-clause (b) fails (no reference anchor)
- V-03: inside boundary, reference pair only — sub-clause (a) fails (no named subject)
- V-04: combination of (a)+(c) — both fail independently, either alone sufficient

**Scoring delta:**

| | v18 | v19 |
|--|-----|-----|
| Aspirational criteria | 28 | 29 |
| Aspirational ceiling | 140 | 145 |
| Total ceiling | 230 | **235** |
