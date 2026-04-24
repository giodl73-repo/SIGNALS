Here is the complete v9 rubric, saved to `simulations/quest/rubrics/draft-spec-rubric-v9-2026-03-15.md`.

---

**What changed from v8 to v9:**

| | v8 | v9 |
|-|----|----|
| Version | v8 | v9 |
| Source rounds | R1–R7 | R1–R8 |
| Aspirational count | 19 | 21 |
| Total criteria | 27 | 29 |
| Composite formula denominator | 19 | 21 |

**Two new aspirational criteria from R8:**

**C-28 — PM pre-assignment phase structurally ordered before inertia analysis** (structure)
The PM pre-assignment phase (producing `[PM-COVERAGE-TABLE]`) must precede the inertia analysis phase via a named gate dependency — not just by document position. Inertia analysis that runs before or concurrently with PM pre-assignment does not satisfy. Source signal: V-03 and V-05 both demonstrated that PM-first ordering is a structurally independent axis; V-05's win over V-04 in the 175-tie turned on this ordering being present.

**C-29 — Inertia Elimination Paths reference pre-assigned requirement IDs** (depth)
Each `[IG-REGISTER]` Elimination Path cell names at least one specific requirement ID from `[PM-COVERAGE-TABLE]`. When Risk Signal is AMPLIFIED, the path must name both the risk dimension and a requirement ID. This criterion is only achievable after C-28 passes — PM-first ordering is what makes requirement IDs available when inertia rows are written. Upgrades C-28; C-28 can pass without C-29.
