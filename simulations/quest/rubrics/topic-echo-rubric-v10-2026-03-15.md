## Rubric: `topic-echo` — v10

Written to `simulations/quest/rubrics/topic-echo-rubric-v10-2026-03-16.md`.

---

### What changed

**Two new aspirational criteria** extracted from Round 9 V-04/V-05 differential:

**C-28 | Category-Field Audit Propagation** (schema)
Source: C-16 V-04 vs V-05. V-04 failed C-16 (no taxonomy); V-05 passed C-16 and went further — the `{CATEGORY}` field propagated from synthesis into the Rules of Thumb audit row schema. C-16 only tests that the synthesis section names categories; C-28 tests that those categories appear as typed fields in downstream audit passes. Requires C-16 PASS; PARTIAL if categories stay isolated to synthesis.

**C-29 | Synthesis-Step Budget Contract** (enforcement)
Source: C-20 V-04 vs V-05. V-04 passed C-20 with `WORD BUDGET:` headers on data-collection steps. V-05 extended coverage to Step 9 itself: `One classification line per surprise + synthesis ≤120 words`. C-20 tests phase scope contracts; C-29 tests specifically that the synthesis/output step carries its own formal budget field. PARTIAL if a prose word-count guide exists but no `WORD BUDGET:` contract header.

---

### Formula delta

| Version | Aspirational denominator | Per-criterion weight |
|---------|--------------------------|----------------------|
| v8 | 18 | 0.56 pts |
| v9 | 20 | 0.50 pts |
| **v10** | **22** | **0.45 pts** |
