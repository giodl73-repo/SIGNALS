## campaign-track R10 — Quest Score

### Scoring Framework

All five variations inherit R9 V-05's 122/122 baseline. Only the three new criteria (C-33, C-34, C-35) differentiate them. Max possible = 122 + 9 = **131**.

---

### Per-Variation Scoring

#### V-01 — Phase 4 Obligation Header (C-33 only)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-32 | PASS (all) | Inherited from R9 V-05 baseline |
| **C-33** | **PASS** | Phase 4 header declares delta.md Post-Phase-4 write as an obligation before Phase 4 execution begins. Forward declaration at activation site — model enters Phase 4 knowing the post-write is mandatory, not optional |
| **C-34** | FAIL | No terminal section opening protocol present |
| **C-35** | FAIL | No cascade invalidation rule present |

**Score: 125/131**

---

#### V-02 — Terminal Opening Protocol (C-34 only)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-32 | PASS (all) | Inherited from R9 V-05 baseline |
| **C-33** | FAIL | No Phase 4 obligation header present |
| **C-34** | **PASS** | Terminal section opens with execution-order protocol naming: normal order + verdict_after exception. Brackets the checklist from the opening side; C-31's closing note brackets from the end |
| **C-35** | FAIL | No cascade invalidation rule present |

**Score: 125/131**

---

#### V-03 — Cascade Invalidation Rule (C-35 only)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-32 | PASS (all) | Inherited from R9 V-05 baseline |
| **C-33** | FAIL | No Phase 4 obligation header present |
| **C-34** | FAIL | No terminal opening protocol present |
| **C-35** | **PASS** | Cascade rule names: trigger condition (Phase 3 Step B re-run), cascade target (verdict_after only), scope exclusion (other delta.md fields not affected). Adds enforcement beyond the Pass 2 section by naming the trigger→target chain |

**Score: 125/131**

---

#### V-04 — C-33 + C-34 Combined

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-32 | PASS (all) | Inherited from R9 V-05 baseline |
| **C-33** | **PASS** | Phase 4 obligation declaration at header (same as V-01) |
| **C-34** | **PASS** | Terminal opening protocol present (same as V-02) |
| **C-35** | FAIL | No cascade invalidation rule present |

**Score: 128/131**

Structural note: V-04 closes the checklist bracket — C-34 opens the terminal section with execution order; C-31 closes it with the causal note. V-04 is the minimum-sufficient combination that fully brackets the terminal checklist.

---

#### V-05 — Full Stack, Extended (C-33 + C-34 + C-35 extended)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-32 | PASS (all) | Inherited from R9 V-05 baseline |
| **C-33** | **PASS+** | Phase 4 header declares obligation AND names the stale-value consequence: verdict_after in delta.md becomes stale if Phase 4 completes without the post-write. Causal framing at declaration site — assertion → named consequence. Mirrors C-32's failure-path framing at Phase 3 header |
| **C-34** | **PASS** | Terminal opening protocol present (same form as V-02/V-04) |
| **C-35** | **PASS+** | Cascade rule names trigger, target, AND explains WHY non-cascade fields are excluded: they were finalized at Phase 3, so Phase 4 cannot change them. Causal scope justification vs. bare enumeration. Mirrors C-31's upstream-dependency explanation |

**Score: 131/131**

Two PASS+ signals detected — both follow the assertion→causal-explanation pattern established by C-31/C-32, applied at two new declaration sites.

---

### Ranking

| Rank | Variation | Score | Delta vs baseline |
|------|-----------|-------|-------------------|
| 1 | **V-05** | **131/131** | +9 |
| 2 | **V-04** | **128/131** | +6 |
| 3 | V-01, V-02, V-03 (tied) | 125/131 | +3 each |

---

### Excellence Signals from V-05

**PASS+ signal on C-33**: The Phase 4 obligation header names the specific stale-value consequence — `delta.md verdict_after becomes stale` — if Phase 4 completes without the post-write. This moves beyond bare obligation declaration to causal framing at the Phase 4 activation site. Structural parallel: C-32 names the failure path at Phase 3 header; this names the stale-value failure at Phase 4 header.

**PASS+ signal on C-35**: The cascade rule explains WHY non-cascade fields are excluded from re-verification: they were finalized at Phase 3 and Phase 4 cannot change them. This moves beyond naming the cascade target to justifying the scope boundary. Structural parallel: C-31 names the upstream dependency that creates the ordering constraint; this names the finalization point that creates the cascade boundary.

Both PASS+ signals are candidates for C-36 and C-37 in a future rubric revision.

---

```json
{"top_score": 131, "all_essential_pass": true, "new_patterns": ["Phase 4 obligation header names stale-value consequence (verdict_after becomes stale if Phase 4 completes without post-write) — causal framing at Phase 4 activation site, mirrors C-32 failure-path pattern at Phase 3", "Cascade rule names WHY non-cascade fields are excluded (finalized at Phase 3, Phase 4 cannot change them) — causal scope justification vs bare enumeration, mirrors C-31 upstream-dependency pattern"]}
```
