`simulations/quest/rubrics/org-review-rubric-v18-2026-03-17.md` written.

---

**v18 summary:**

**New criterion: C-50** (5 pts, aspirational)

| ID | Name | Source | PASS variants |
|----|------|--------|---------------|
| C-50 | §0-CID PIPELINE CONTRACT Self-Auditable Axis Back-References | V-05 R19 | 1/5 |

**Chain logic:**
- C-49 closes the three-layer loop with *inbound* edges: schema → pipeline and behavioral → pipeline.
- C-50 adds the *outbound* edges: pipeline → schema (each axis block names the TABLE FORMAT CONTRACT field it governs) and pipeline → behavioral (each axis block names the §§ behavioral contract that enforces it).
- With C-50 PASS, the §0-CID PIPELINE THREADING CONTRACT becomes the complete audit hub — an auditor reading only that block can reach all other structural layers. The six-direction explicit directed graph is complete.
- C-50 is vacuous without C-49 PASS (which requires C-48 PASS). V-01/V-02/V-03 have C-48 PARTIAL → C-49 vacuous → C-50 vacuous. V-04 has C-49 PASS but pipeline axis blocks carry no back-references → C-50 FAIL.

**C-48 pass condition clarified in v18:** Single-sided cross-referencing (schema leg only or behavioral leg only) is PARTIAL (0 pts). Both legs must be independently present. The R19 ablation isolates exactly this: V-02 = schema-only → PARTIAL; V-03 = behavioral-only → PARTIAL; V-04 and V-05 = both legs → PASS.

**Score changes:** Aspirational 41 → 42 | Max 295 → 300 | Gold threshold 260 → 265

**R19 ranking under v18:**

| Rank | Variant | Score |
|------|---------|-------|
| 1 | V-05 | **300/300** |
| 2 | V-04 | **295/300** |
| 3 (tie) | V-01/V-02/V-03 | **285/300** |

R19 floor advances from R18's predicted 270 to actual 285. Next round target: V-04+C-50 (add pipeline axis back-references) = 300/300.
