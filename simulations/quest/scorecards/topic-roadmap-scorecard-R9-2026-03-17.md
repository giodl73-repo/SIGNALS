## Round 9 Scorecard — `topic-roadmap`

### Baseline Assumptions

All five variations inherit **R8 V-05** as their base: all essential (C-01–C-05) pass, all recommended (C-06–C-08) pass, and aspirational C-09–C-20 score full 2/2 each (24 raw). Round 9 tests three new axes: C-21 (dual-site gate), C-22 (restart isolation), C-23 (standalone verdict block).

---

### Per-Variation Criterion Evaluation

#### C-01–C-08 (all variations)

| Criterion | All Vars | Evidence |
|-----------|----------|----------|
| C-01 Inertia prior enforced | PASS | Inherited from R8 V-05: zero-change default, proposals require named NEW artifacts |
| C-02 Signal delta before proposals | PASS | Inventory table with NEW/PRIOR classification precedes proposal block |
| C-03 Proposals concrete + action-typed | PASS | ADD/REMOVE/REPRIORITIZE with Before/After + artifact citation |
| C-04 User confirmation gate present | PASS | Gate enforced before write |
| C-05 (inferred essential) | PASS | Inherited |
| C-06 Recommended-1 | PASS | Inherited |
| C-07 Recommended-2 | PASS | Inherited |
| C-08 Recommended-3 | PASS | Inherited |

Essential: 5/5 → **60 pts**. Recommended: 3/3 → **30 pts** (shared).

---

#### Aspirational C-09–C-20 (all variations)

All 12 criteria score 2/2 (inherited from R8 V-05). Subtotal: **24 raw**.

---

#### C-21 Dual-site INERTIA-GATE enforcement

| Var | Score | Evidence |
|-----|-------|----------|
| V-01 | **2** | Explicitly adds `[Site 1 of 2 -- Phase 5 entry]` and `[Site 2 of 2 -- Phase 6 entry]` labels; Phase 6 carries independent enforcement clause |
| V-02 | **2** | Inherits V-01's dual-site implementation; both site labels present |
| V-03 | **2** | Inherits V-01's dual-site implementation; both site labels present |
| V-04 | **2** | Explicitly targets C-21; both labeled sites, integrated alongside restart clause |
| V-05 | **2** | All three mechanisms spatially separated; both gate sites carry independent enforcement |

---

#### C-22 Restart isolation clause in Phase 1 read-barrier

| Var | Score | Evidence |
|-----|-------|----------|
| V-01 | **0** | No restart clause; Phase 1 barrier covers first-run only |
| V-02 | **2** | Adds `RESTART ISOLATION` parallel clause alongside `FIRST-RUN ISOLATION`; names re-reading-to-reconstruct-state as explicit violation |
| V-03 | **0** | No restart clause; verdict vocabulary focus only |
| V-04 | **2** | Combined V-01+V-02 target; restart clause at Phase 1 barrier present |
| V-05 | **2** | Restart clause at Phase 1, spatially distinct from verdict block and gate sites |

---

#### C-23 Dedicated verdict vocabulary block before Phase 5

| Var | Score | Evidence |
|-----|-------|----------|
| V-01 | **0** | Verdict semantics embedded within Phase 5 instructions; no standalone block |
| V-02 | **0** | Verdict semantics remain embedded in Phase 5 |
| V-03 | **2** | `## Verdict Vocabulary` standalone block between Phase 4 and Phase 5; DEFEATED/HOLDS + forward paths defined; Phase 5 explicitly defers: "Apply the Verdict Vocabulary defined above. Do not redefine here." |
| V-04 | **0** | Verdict semantics remain embedded in Phase 5; only C-21+C-22 combined |
| V-05 | **2** | Standalone block at designated position; Phase 5 uses forward-reference only |

---

### Composite Scores

```
Composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_raw/30 * 10)
Shared base: 60 + 30 = 90 pts
```

| Var | C-21 | C-22 | C-23 | Aspirational raw | Aspirational pts | **Composite** | Golden? |
|-----|------|------|------|-----------------|-----------------|--------------|---------|
| V-01 | 2 | 0 | 0 | 26 | 8.67 | **98.7** | YES |
| V-02 | 2 | 2 | 0 | 28 | 9.33 | **99.3** | YES |
| V-03 | 2 | 0 | 2 | 28 | 9.33 | **99.3** | YES |
| V-04 | 2 | 2 | 0 | 28 | 9.33 | **99.3** | YES |
| V-05 | 2 | 2 | 2 | 30 | 10.00 | **100.0** | YES |

All variations clear the 80-point golden threshold (all essential pass + composite ≥ 80).

---

### Ranking

1. **V-05 — 100.0** — Full integration; all three mechanisms achieved and spatially separated
2. **V-02, V-03, V-04 — 99.3 (tied)** — Two of three new criteria each; separation is incomplete
3. **V-01 — 98.7** — Only C-21 target achieved; C-22 and C-23 remain at baseline

**V-02 vs V-04 tie note**: Both achieve C-21+C-22. V-04 is explicitly designed as a combined target; V-02 inherits C-21. Scoring is identical within current rubric — neither achieves C-23.

**V-03 vs V-02/V-04 tie note**: V-03 achieves C-21+C-23 (verdict block) but not C-22. Same raw score as V-02/V-04 since each adds exactly two of the three new criteria.

---

### Excellence Signals from V-05

**Signal 1 — Spatial separation of enforcement mechanisms**
Each mechanism occupies its own designated structural position: restart isolation lives at Phase 1 barrier, verdict vocabulary lives in a standalone pre-Phase-5 block, gate enforcement labels live at Phase 5 and Phase 6 boundaries. Nothing is co-located or embedded within a different mechanism's section. This makes each criterion independently auditable without reading surrounding context.

**Signal 2 — Forward-reference enforcement prevents semantic drift**
Defining verdict semantics once in a standalone block, then requiring downstream phases to reference rather than redefine ("Apply the Verdict Vocabulary defined above. Do not redefine here."), eliminates the possibility of Phase 5 silently reinterpreting DEFEATED/HOLDS. The prohibition on redefinition is an active enforcement clause, not passive omission.

**Signal 3 — Site-indexed gate labels make enforcement count auditable**
The `[Site 1 of 2]` / `[Site 2 of 2]` pattern at Phase 5 and Phase 6 entries turns enforcement presence into an explicit count contract. A reviewer can verify the count matches without reading the gate logic — structural completeness is visible from the label alone.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["spatial separation of enforcement mechanisms — each mechanism occupies its own dedicated structural position, independently auditable without surrounding context", "forward-reference enforcement — define-once vocabulary block with explicit downstream prohibition on redefinition prevents semantic drift across phases", "site-indexed gate labels — numbered site annotations make enforcement count auditable from structure alone, independent of gate logic content"]}
```
