Written to `simulations/quest/golden/corps-scan-variate-R3-2026-03-16.md`.

---

# Variate R3 — corps-scan

5 complete prompt body variations targeting the v3 rubric (130 pts). C-13/C-14/C-15/C-16 are structural invariants across all variations.

---

## Variation Axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Role sequence | Compliance Officer as Role 1 forces C-13 (self-confirming pre-check item 2 confirms item 1) and C-14 (Role 1 pre-check + Role 3 post-write) by construction. Role ordering makes C-13 mechanically unskippable. |
| **V-02** | Output format | 5-column Signal-to-YAML Schema replaces inventory — each row specifies team name + roles + evidence in one artifact. Self-referential confirmation embedded in schema header. Pre/post YAML notes bracket the artifact. |
| **V-03** | Phrasing register | Formal numbered requirements with inline verification clauses. "Requirement 1 is satisfied by this line" — the clause IS the satisfaction. Non-compliance consequence notation per amend option for C-16. |
| **V-04** | Pre-check + debt amends (ceiling fix) | R2 V-04 scored 125, missed only C-16. This variation takes V-04's proven C-13/C-14/C-15 structure and adds debt framing to all 3 amend options. Designed to hit 130/130. |
| **V-05** | Phase gates + distributed compliance | Compliance spread across lifecycle: each phase has ENTRY CHECK + EXIT CHECK. C-13 lands in Phase 3 ENTRY CHECK; C-14 is the Phase 3 ENTRY+EXIT pair; C-15 is each phase CHECK naming its criterion. |

---

## Key R3 Invariants (new in every variation)

**C-13** — Each variation includes a self-confirming item: `"Draft-only boundary is line 1 of this output. STATUS: CONFIRMED."` The model can only write CONFIRMED after having written the boundary.

**C-14** — Every variation has both a pre-YAML check block AND a post-YAML checklist/verification note. The YAML is bracketed on both sides.

**C-15** — Every variation names 5+ criteria explicitly by behavior (mapping to C-04, C-05, C-07, C-11, C-12 at minimum).

**C-16** — Every variation debt-frames at least 2 amend options: `"Debt if skipped: [downstream consequence]."` V-04 and V-05 debt-frame all 3.

---

## Projected R3 Scores

All 5 variations are designed to hit 130/130. V-04 is the strongest ceiling candidate (directly fixes R2's only miss). V-01 is strongest for C-13/C-15 (role ordering enforces criterion naming). V-03 is strongest for C-15 (8 numbered requirements = 8 criteria declared).
