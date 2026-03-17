Written to `simulations/quest/golden/campaign-simulate-variate-R5-2026-03-17.md`.

---

## Round 5 Variations -- Summary

**Three new axes explored:**

| Axis | Description | Hypothesis |
|------|-------------|------------|
| **A** | Exception Path column in unified findings table | Moving C-21 coverage from entity manifest to a per-row column in the findings table makes exception path coverage verifiable across all 5 sub-skills, not just flow-lifecycle |
| **B** | Blast Rationale as a named column in ranked findings | Moving C-20 rationale from inline prose to a named column makes it verifiable by column scan rather than prose search |
| **C** | Mandatory Cross-Skill Synthesis Gate with sentinel | Promoting CROSS-SKILL PATTERNS from optional section to a gate with a sentinel (either P-ID row or explicit "none + justification") prevents silent omission |

**Variation assignments:**

| Variation | Axes | Base Architecture |
|-----------|------|-------------------|
| V-01 | Axis A alone | R4 V-04 base (entity manifest + type vocabulary) |
| V-02 | Axis B alone | R4 V-04 base |
| V-03 | Axis C alone | R4 V-04 base |
| V-04 | Axis A + Axis B | R4 V-05 full architecture |
| V-05 | Axis A + Axis B + Axis C | R4 V-05 full architecture + all three axes |

**Key design decision:** All three axes share the same structural pattern -- each replaces a prose compliance mechanism with a named structural element. V-05 extends the R4 V-05 principle ("every column has a mechanical compliance path") to three additional fields that R4 left as prose obligations. If V-05 scores 100/100 on v4, the three new axes are candidates for v5 rubric criteria C-22 (Exception Path column), C-23 (Blast Rationale column), and C-24 (Cross-Skill Synthesis Gate).
