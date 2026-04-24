---
skill: quest-rubric
skill_target: org-chart
date: 2026-03-16
version: 1
---

# Scoring Rubric -- org-chart

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60 pts, 12 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Inertia Assessment present and complete** | behavior | Output contains all four sub-sections in order: (1) Case for Staying Flat with a mechanism table of >= 2 rows using only the closed Type vocabulary (Channel / Informal Role / Recurring Cadence / Shared Artifact), (2) How We Coordinate Today, (3) Rebuttal naming a specific observable failure mode (not just "the team is growing"), (4) VERDICT opening with a `FLAT-CASE-PRESSURE:` line using a rating from the closed set (Strong / Moderate / Weak / Negligible / Insufficient) followed by exactly one of `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED` and a re-assessment trigger with a concrete threshold. The inertia assessment MUST appear before any ASCII org diagram. |
| C-02 | **Roles block grounded in .roles/** | correctness | Output opens with either a `ROLES-LOADED:` block listing roles read from `.roles/` files, or a `ROLES-NOTE:` block stating no files were found and listing inferred roles. Every role name appearing in the org diagram, headcount table, or committee charters must have been declared in this block. No role name may be introduced later in the document. |
| C-03 | **ASCII org diagram with hierarchy** | format | An ASCII org hierarchy is present after the inertia assessment phase gate. It shows >= 2 levels of hierarchy (not a flat bulleted list of names). Committees appear as distinct labeled nodes separate from area boxes. All role names in the diagram match names from the ROLES-LOADED or ROLES-NOTE block. |
| C-04 | **Operating rhythm table with >= 3 distinct rows** | coverage | A cadence table is present with columns `Cadence | Frequency | DRI / Owner | Purpose`. It contains >= 3 rows covering at minimum: an ROB, a shiproom or gate review, and a governance meeting. No two distinct meetings are merged into one row. The DRI/Owner column references a role from the roles block where possible. |
| C-05 | **Committee charters with all five fields including N-of-M quorum** | correctness | A charter exists for every governance meeting listed in the rhythm table. Each charter contains all five fields: Purpose, Membership, Decides, Escalates, Quorum. The Quorum field uses the fraction format `Quorum: [N] of [M] member roles required for binding decisions`. The Escalates field names a destination role or forum (not a generic phrase such as "everything not listed under Decides"). Membership lists >= 2 roles each annotated with a domain type. |

---

## Recommended Criteria (weight: 30 pts, 10 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Headcount by area with split Decides/Escalates columns** | depth | A headcount table is present with columns `Area | Headcount | Key Roles | Decides | Escalates`. Decides and Escalates are separate columns (not merged into a single Decision Scope column). The table contains >= 2 area rows plus a `**Total**` row with the summed headcount. Each Key Roles cell is annotated in the format `[role name] ([domain type])`. |
| C-07 | **Phase gates present in correct sequence** | format | All four phase gate lines appear in the output in the exact specified order: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`, then `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`, then `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`, then `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`. No section that follows a gate appears before that gate line in the output. |
| C-08 | **ROLE-TYPE-CLASSIFICATION block with closed-set domain types** | correctness | A `ROLE-TYPE-CLASSIFICATION:` block appears immediately after the ROLES-LOADED or ROLES-NOTE block. Every role is assigned exactly one type from the closed set: Engineering / PM / Design / Operations / Research / Other. Roles are listed in three-tier order: all Engineering types first, then Operations, then remaining types; no interleaving across tiers. |

---

## Aspirational Criteria (weight: 10 pts, 5 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **ORG-ELEMENT REGISTER and Anti-Pattern Watch with typed cat-N citations** | depth | An ORG-ELEMENT REGISTER block is present after the charters phase gate with all four categories populated: cat-1 (Areas), cat-2 (Committees/Cadences), cat-3 (Headcount), cat-4 (DRI Roles). An Anti-Pattern Watch section follows with >= 2 rows, each `Why It Applies Here` cell opening with typed citation syntax `[element name] (cat-N) -- [one sentence]` using only cat codes defined in the register. No cell names an element without the (cat-N) annotation. |
| C-10 | **Org Evolution Roadmap with two triggers from distinct categories** | depth | An Org Evolution Roadmap trigger table is present with columns `Trigger | Structural Change | Type` and >= 2 rows. Row 1 is a headcount threshold trigger. Row 2 comes from a different category: a workload signal, structural symptom, or milestone event. The two rows do not both use headcount thresholds. |

---

## Scoring Reference

| Band | Composite | Meaning |
|------|-----------|---------|
| Golden | >= 80 AND all essential pass | Accepted as golden candidate |
| Near-golden | >= 70 AND all essential pass | One recommended criterion away |
| Partial | >= 60 OR <= 1 essential fail | Structurally present, needs fixing |
| Failing | < 60 OR >= 2 essential fail | Not usable; rework required |

---

## Known Failure Modes (seed list for quest-score)

- **Org-before-inertia**: ASCII diagram appears before the inertia assessment -- fails C-01 and C-03.
- **Invented roles**: Role names appear in the diagram or charters that were not declared in the roles block -- fails C-02.
- **Merged decides/escalates**: Headcount table uses a single `Decision Scope` column -- fails C-06.
- **Short quorum form**: Quorum written as `N roles required` instead of the fraction `N of M member roles` -- fails C-05.
- **Missing charter**: Governance meeting appears in the rhythm table with no corresponding charter -- fails C-05.
- **Flat diagram**: Org diagram is a bulleted list with no visual hierarchy -- fails C-03.
- **Generic rebuttal**: Rebuttal says only "the team is growing" without naming a specific failure mode -- fails C-01.
- **cat-N mismatch**: Anti-Pattern Watch cites a cat code not defined in the ORG-ELEMENT REGISTER -- fails C-09.
- **Pressure line absent**: VERDICT opens without the `FLAT-CASE-PRESSURE:` line -- fails C-01.
- **Mechanism table undercount**: Case for Staying Flat has only 1 data row in the mechanism table -- fails C-01.
