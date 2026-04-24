## `/quest:score` — `trace-request` Round 2 Scorecard

---

### Evaluation Method

The trace artifact is a placeholder; scoring evaluates each variation's structural mechanisms against the rubric — asking whether the prompt design makes each criterion structurally inescapable, reliable, or left to chance.

---

### Per-Criterion Evidence

#### C-01 — Entry point declared (Essential, 15 pts)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | **PASS** | STEP 1 requires all four fields explicitly: method/path/event, payload shape, caller identity, auth evidence at entry |
| V-02 | **PASS** | PASS 1 traversal opens with entry point declaration |
| V-03 | **PASS** | Entry section present; DISQUALIFIER blocks reinforce "vague entry point fails" |
| V-04 | **PASS** | Carries through two-pass structure with entry declaration |
| V-05 | **PASS** | R1 boundary gate structure preserved; entry point is gate condition for the table |

---

#### C-02 — All service boundaries crossed (Essential, 15 pts)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | **PASS** | STEP 3 traverses in order, explicitly names token validation, gateway routing, and audit emission as required inclusions |
| V-02 | **PASS** | PASS 1 traversal lists all boundaries for PASS 2 to re-walk — structural dependency forces completeness |
| V-03 | **PASS** | Traversal section present; DISQUALIFIER for skipped boundaries |
| V-04 | **PASS** | PASS 1 boundary list feeds PASS 2 re-walk — any skipped boundary would leave a hole in the re-walk |
| V-05 | **PASS** | R1 boundary gate requires boundary enumeration before any per-boundary analysis |

---

#### C-03 — Failure point at each boundary (Essential, 15 pts)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | **PASS** | STEP 3 field definition explicitly states: `"May fail" or "could error" without a named mechanism fails this field` |
| V-02 | **PASS** | Traversal requires failure modes per boundary; no universal disqualifier but field is required |
| V-03 | **PASS** | Universal DISQUALIFIER block at section header names `"may fail"` as a disqualifying pattern — strongest enforcement |
| V-04 | **PASS** | Inherits from two-pass traversal + DISQUALIFIER combination |
| V-05 | **PASS** | R1 carry-forward + universal disqualifiers; field-level and header-level enforcement both present |

---

#### C-04 — Authorization gaps surfaced (Essential, 15 pts)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | **PASS** | STEP 3 Authorization field: `Yes -- [exact permission/scope/role]` or `No -- AUTH GAP: [reason]` — binary with mandatory justification |
| V-02 | **PASS** | Authorization field per boundary in PASS 1; gaps feed PASS 2 re-walk |
| V-03 | **PASS** | DISQUALIFIER: `"standard auth"` as a disqualifying pattern — forces specific permission naming |
| V-04 | **PASS** | Scorecard notes "strongest single-criterion enforcement for C-04 across all variations" — PHASE 4 dedicated auth re-walk surfaces gaps missed by primary pass |
| V-05 | **PASS** | All mechanisms combined |

---

#### C-05 — Latency sources identified (Recommended, 10 pts)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | **PASS** | Each boundary draws budget at p50/p99; budget-draw input = latency annotation; at least as many distinct sources as boundaries |
| V-02 | **PASS** | Latency annotation per boundary in PASS 1 traversal |
| V-03 | **PASS** | DISQUALIFIER: `"fast"` as a disqualifying annotation — forces concrete latency naming |
| V-04 | **PASS** | Budget column in traversal table; budget framing inherited |
| V-05 | **PASS** | Budget column structurally integrated into boundary table |

---

#### C-06 — Error path traced end-to-end (Recommended, 10 pts)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | **PASS** | STEP 6 traces highest-probability failure from origination through every boundary to caller; "Do not jump steps" enforced |
| V-02 | **PASS** | Error path step present as dedicated section |
| V-03 | **PASS** | Error path present; DISQUALIFIER for happy-path-only traces |
| V-04 | **PASS** | Error path step present |
| V-05 | **PASS** | Error path step preserved from R1 |

---

#### C-07 — Batch and edge-case handling (Recommended, 10 pts)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | **FAIL** | No dedicated batch/pagination section; adversarial step offers concurrent mutation but does not require batch analysis |
| V-02 | **FAIL** | Two-pass structure has no explicit batch handling section |
| V-03 | **FAIL** | DISQUALIFIER blocks cover auth and latency failure modes; no batch-specific mechanism |
| V-04 | **PARTIAL (5)** | Threat enumeration table includes concurrency as a threat class; concurrent mutation scenario partially covers edge cases but doesn't require pagination or batch analysis specifically |
| V-05 | **PASS** | R1 V-05 comprehensive structure includes batch/pagination edge case section as explicit output requirement |

---

#### C-08 — Actionable remediation per failure point (Aspirational, 5 pts)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | **PASS** | STEP 8 names specific algorithm (exponential backoff with jitter), error rate thresholds, exact scope to add; `"Add error handling"` explicitly fails |
| V-02 | **PASS** | Remediation step present with mechanism specificity required |
| V-03 | **PASS** | DISQUALIFIER for generic remediation language |
| V-04 | **PASS** | Inherited + per-threat-class remediation pairing |
| V-05 | **PASS** | All mechanisms |

---

#### C-09 — Adversarial path comparison (Aspirational, 5 pts)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | **PASS** | STEP 7 provides four adversarial options; requires naming the divergence boundary and outcome |
| V-02 | **PASS** | Adversarial scenario step present; no threat enumeration forcing class coverage |
| V-03 | **PASS** | Adversarial step present; disqualifiers improve scenario quality |
| V-04 | **PASS** | Threat enumeration table (token abuse / payload abuse / concurrency / scope creep / trust abuse) evaluated before selection; model must pick highest-risk class overlapping PASS 2 findings |
| V-05 | **PASS** | Threat table + PASS 2 overlap requirement; adversarial scenario targets a real gap, not the easiest option |

---

#### C-10 — Critical path named (Aspirational, 5 pts)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | **PASS** | STEP 4 explicitly computes: sequential chain sum, parallel branch exclusions, cached-step exclusions, p50 and p99 totals with headroom; critical path emerges from accounting during traversal |
| V-02 | **FAIL** | Two-pass structure has no latency budget; PASS 1 annotates latency sources but doesn't name the sequential chain that determines worst-case; C-10 pass condition requires naming the *sequence*, not just the sources |
| V-03 | **PASS** | DISQUALIFIER: `"lists sources without naming the chain"` — forces the model to identify the sequential sequence, not just annotate boundaries |
| V-04 | **PASS** | Budget exhaustion mechanism inherited from V-01 axis; critical path = the chain that exhausts the declared budget |
| V-05 | **PASS** | Budget column in boundary table + STEP 4 accounting + DISQUALIFIER for source-listing-only |

---

#### C-11 — Authorization re-walk audit (Aspirational, 5 pts)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | **PASS** | STEP 5 is a dedicated re-walk with three structured questions per boundary; requires naming one gap missed in STEP 3, or explicitly confirming each high-risk boundary is clean |
| V-02 | **PASS** | PASS 2 as coequal top-level sweep; structurally inescapable; cannot be skipped or collapsed into PASS 1 |
| V-03 | **PASS** | Auth re-walk step present; DISQUALIFIER prevents mirroring inline auth fields as a re-walk |
| V-04 | **PASS** | PASS 2 inherited; threat enumeration findings feed re-walk targeting |
| V-05 | **PASS** | PASS 2 + DISQUALIFIER + threat-overlap targeting |

---

### Composite Scores

| Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-02 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-03 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-04 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-05 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-06 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-07 | 10 | 0 | 0 | 0 | 5 | 10 |
| C-08 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-09 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-10 | 5 | 5 | 0 | 5 | 5 | 5 |
| C-11 | 5 | 5 | 5 | 5 | 5 | 5 |
| **Total** | **110** | **100** | **95** | **100** | **105** | **110** |
| All essential pass | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| Golden (≥80) | — | ✓ | ✓ | ✓ | ✓ | ✓ |

**Ranking**: V-05 (110) > V-04 (105) > V-01 = V-03 (100) > V-02 (95)

---

### Excellence Signals — V-05

**1. Budget-integrated critical path (C-10):** The latency budget is declared *before* the traversal begins. Each boundary draws from it sequentially or shares a slot (parallel branches). The critical path is not a post-hoc analytical task — it is the arithmetic output of the traversal itself. The model cannot complete the traversal without performing critical path analysis implicitly.

**2. Parallel branch slot rule:** Concurrent paths share a single budget slot; only the longest draws. This collapses the "list all latency sources" failure mode — the model must decide which parallel branch is the critical one, not simply enumerate both.

**3. PASS 2 as coequal sweep (C-11):** The auth re-walk is not a phase *within* the traversal (as in R1) but a separate named pass at the same structural level. This prevents it from being absorbed into PASS 1's per-boundary fields and called complete.

**4. Threat enumeration table before adversarial scenario selection (C-09):** The model fills a five-class threat table (token abuse / payload abuse / concurrency / scope creep / trust abuse) and marks which apply *before* choosing an adversarial scenario. The selected scenario must be the highest-risk class that overlaps PASS 2 findings — preventing selection of the easiest scenario instead of the structurally most dangerous one.

**5. Universal DISQUALIFIER headers:** Specific failure text patterns (`"may fail"`, `"standard auth"`, `"fast"`, `"lists sources without naming the chain"`) are named at the top of each section. This separates enforcement from field definitions — the model is told to avoid exact failure strings, not just to "be specific."

**6. Boundary gate from R1 preserved:** All boundaries must be enumerated in a table before per-boundary analysis begins. This forces C-02 completeness before C-03/C-04/C-05 have any input to work with.

---

### Single Gap Across All Variations

**C-07 (batch/edge-case handling)** is the only criterion no variation below V-05 addresses structurally. V-01 through V-03 miss it entirely. V-04 earns partial credit via the concurrency threat class, but pagination and per-record overhead analysis require explicit structural inclusion (as in R1 V-05's comprehensive section). Any future variation targeting 110/110 without V-05's full synthesis must add an explicit batch/pagination step.

---

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["Latency budget declared before traversal; sequential boundary draws sum to critical path via accounting rather than post-hoc identification", "Parallel branch slot rule: concurrent paths share one budget slot and only the longest draws, forcing explicit critical-path branch selection during traversal", "PASS 2 elevated to coequal top-level sweep: auth re-walk is a named pass at the same structural level as the primary traversal, not a subordinate phase within it", "Threat enumeration table evaluated before adversarial scenario selection: model marks all five threat classes, then selects the highest-risk class overlapping PASS 2 findings", "Universal DISQUALIFIER headers with explicit failure text patterns named at section openings, separating failure-mode enforcement from field-level definitions"]}
```
