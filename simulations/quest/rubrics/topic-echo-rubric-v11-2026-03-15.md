Written to `simulations/quest/rubrics/topic-echo-rubric-v11-2026-03-16.md`.

---

**Two new criteria added:**

**C-30 | Belief-Set Entry Schema Propagation** (schema)
Source: R11 V-01 — `defeats: CB-{n}` as a typed slot in the entry template. C-23 ensures the belief inventory exists pre-gate; C-30 tests whether the CB-IDs propagate as a required field in the entry schema itself. Same propagation pattern as C-28 (category taxonomy → audit schemas), but for belief IDs → entry schemas. Requires C-23 PASS.

**C-31 | Pre-Investigation Belief Freeze Contract** (epistemic)
Source: R11 V-01 — explicit "CB-ID freeze before Step 1." C-23 tests timing (pre-gate); C-31 tests that the prompt contains an explicit immutability constraint locking the CB-set before artifact reading. Without the freeze, a C-23-passing agent could still silently revise beliefs mid-investigation and no criterion would catch it. Requires C-23 PASS.

**Formula delta:**

| Version | Aspirational denominator | Per-criterion weight |
|---------|--------------------------|----------------------|
| v10 | 22 | 0.45 pts |
| **v11** | **24** | **0.42 pts** |

**V-01 R11 score under v11:** C-30 PASS + C-31 PASS → 19.5/24 aspirational → **98.13** (up from 97.95 under v10).

**V-02 R11 score under v11:** C-30 FAIL + C-31 FAIL (both require C-23 PASS; V-02 is C-23 PARTIAL) → 17/24 aspirational → **97.08** (down from 97.73 under v10 — v11 correctly penalizes the post-read belief pattern more sharply).
