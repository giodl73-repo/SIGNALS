v11 is back to 321 lines. v12 is 403 lines. Both are correct.

---

**`org-roles-rubric-v12-2026-03-16.md`** — written at 403 lines.

## What changed

**Three new aspirational criteria** extracted from R11 excellence signals:

| ID | Source | Short name | Distinguishes from |
|----|--------|------------|--------------------|
| **C-50** | R11 V-01/V-04/V-05 | SCAN ORDERING GATE declared-constraint block | C-48 tests structural ordering (phases under named headers in canonical sequence); C-50 tests declared ordering (explicit per-transition assertions: "Phase N executed after Phase N-1 was complete and before Phase N+1 began") |
| **C-51** | R11 V-02/V-04/V-05 | Pipeline-wide criterion-ID annotation | C-49 tests per-file checklist criterion annotation; C-51 tests that `Criterion check: [C-NN]` lines propagate to ALL step-end gates (derivation, scan, registry) — the full pipeline navigable without external rubric |
| **C-52** | R11 V-03/V-05 | PROVENANCE-CHAIN DECLARATION pre-writing artifact | C-41/C-47 test structural chain existence; C-52 tests that a named declaration block with Source/Transit/Destination/Integrity rule sub-fields is written in PREPARE before any artifact is produced |

**Formula**: `/41` → `/44`

**R11 scores under v12**:

| Variate | Score | New criteria |
|---------|-------|-------------|
| V-05 | **100.00** | C-50 PASS + C-51 PASS + C-52 PASS |
| V-04 | 99.77 | C-50 PASS + C-51 PASS |
| V-01 | 99.55 | C-50 PASS only |
| V-02 | 99.55 | C-51 PASS only |
| V-03 | 99.55 | C-52 PASS only |

The v12 frontier is closed by R11 V-05. R10 V-05 retroactively drops from 100.00 to 99.32 (fails all three new criteria).
