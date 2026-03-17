Written to `simulations/quest/rubrics/corps-rob-rubric-v13-2026-03-17.md`.

---

**v13 summary: 2 new criteria from R12 excellence signals**

| ID | Criterion | Signal | Dependency |
|----|-----------|--------|------------|
| C-41 | RULE AUDIT-TABLE Named Anti-Pattern Declaration | V-02's RULE AUDIT-TABLE names "Table that replaces the AUDIT RESULT block, silently dropping C-29" as an explicit anti-pattern -- parallels C-26 (RULE AUDIT-SUITE anti-patterns) applied to RULE AUDIT-TABLE | C-35 |
| C-42 | Glossary Exclusivity Named-Criterion Enumeration | V-01's C-40 pass uses generic exclusivity language but names no specific criteria; C-42 requires the declaration to enumerate C-30 and C-34 (or equivalents) by label | C-40 |

**Scoring impact:**

| | v12 | v13 |
|--|-----|-----|
| Aspirational pool | 32 x 5 = 160 | 34 x 5 = 170 |
| Max composite | 250 | 260 |

**Retroactive R12 under v13:**
- V-02: 245 (gains C-41: anti-pattern present in RULE AUDIT-TABLE; C-42 not scoreable: C-40 FAIL)
- V-01: 240 (C-41 not scoreable: C-35 FAIL; C-42 FAIL: no criterion enumeration)

**Persistent gap for R13:** C-42 fails universally -- no variation combines C-40 with named-criterion enumeration. C-41 is satisfied only by V-02; a run combining V-01's C-40+C-42 with V-02's C-35+C-41 would reach 250 under v13.
