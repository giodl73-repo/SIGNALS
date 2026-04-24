Rubric updated to v2. Here's what changed and why:

---

## Three new aspirational criteria (C-11, C-12, C-13)

**C-11 — Phase as first-class ticket field** (5 pts)
V-03 and V-04 both promoted Phase to a declared metadata field alongside the standard 6. This is what turned C-06 from PARTIAL to PASS in those variants — phase tracking happened at generation time, making the distribution auditable per-ticket rather than inferred from body language.

**C-12 — Fallback-grounded severity rationale** (5 pts)
The critical insight from V-03/V-04: severity isn't a property of the problem, it's a property of the adoption position. "I can still fall back to [prior tool]" → P2/P3. "I can no longer use [prior tool]" → P0/P1. This is what turned C-07 from PARTIAL to PASS — the inference was mechanical, not asserted.

**C-13 — Mid-output verification block** (5 pts)
V-03 STEP 4 and V-04 STEP 4 both fire a PASS/FAIL self-audit block before the gap analysis, tabulating phase counts and role diversity. The verification block appears in the output, making it observable. This is the structural mechanism that locks in C-06 and C-08 compliance rather than leaving them as soft constraints.

---

## Scoring impact

- Aspirational bucket: 2 criteria → 5 criteria, 10 pts → 25 pts
- Max composite: 100 → 115
- Golden threshold unchanged: all essential pass + composite >= 80
- V-03/V-04 retroactively score 110/115 under v2 (C-10 still fails — no pre-commitment table)
