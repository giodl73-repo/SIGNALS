Here is the complete updated rubric:

---

## `trace-request-rubric-v3-2026-03-14.md`

**Changes from v2:**

Two new aspirational criteria, expanding the tier from 4 → 6 criteria (20 → 30 pts). Total scale 110 → 120. Golden threshold unchanged at >= 80.

---

### New Criteria

**C-12 — Per-boundary latency budget table** (depth, 5 pts)

Extracted from V-04/V-05's structured budget column pattern. C-05 requires prose latency annotation on individual sources. C-10 requires naming the critical-path sequence with a total p50/p99 estimate. C-12 requires the traversal itself to carry a dedicated p50/p99 budget column per boundary — visible, structured, and additive. The per-boundary values must be consistent with the critical-path total from C-10: non-parallel segments sum correctly, parallel segments are not double-counted. A trace that annotates latency in prose or provides only a total estimate without per-boundary budget rows fails.

**C-13 — Threat class catalog** (depth, 5 pts)

Extracted from V-04's threat enumeration table, flagged in the C-07 row as earning only partial credit because the table covered concurrency but not batch/pagination. The underlying mechanism — a structured catalog mapping threat classes to the boundaries where they manifest — is an excellence signal not captured by C-09 (at least one adversarial path showing divergence) or C-07 (batch edge-case analysis). C-13 requires the trace to include a structured threat catalog: at minimum a table mapping at least four distinct threat classes (e.g., malformed input, credential expiry, concurrent mutation, missing permission scope, network partition) to the specific boundaries where each applies. A trace that explores adversarial scenarios ad-hoc without a class-level catalog fails.

---

### Why these two, not others

| Signal considered | Disposition |
|---|---|
| V-04/V-05 budget column structurally integrated into traversal table | C-12 |
| V-04 threat enumeration table (C-07 partial credit signal) | C-13 |
| V-05 R1 boundary gate precondition | Evaluation/structural enforcement mechanism — belongs in variation design guidance, not a response criterion |
| V-03 universal DISQUALIFIER blocks | Variation design pattern, not a response criterion |
| V-04 PHASE 4 dedicated auth re-walk | Already C-11 (v2) |
| V-02/V-04 critical path + p50 estimate | Already C-10 (v2) |

---

### Scoring recap

| Tier | Criteria | Pts Each | Available |
|---|---|---|---|
| Essential | C-01--C-04 | 15 | 60 |
| Recommended | C-05--C-07 | 10 | 30 |
| Aspirational | C-08--C-13 | 5 | 30 |
| **Total** | | | **120** |

Golden: all 4 essential + composite >= 80.

---

**Two signals rejected:** V-05's R1 boundary gate and V-03's DISQUALIFIER blocks are both structural enforcement mechanisms that improve *variation design* — they constrain what a prompt variation demands from the responder, not what the response itself must contain. Neither translates cleanly to a binary pass/fail criterion on a trace artifact, so both belong in variation design guidance rather than the rubric.

**Why C-12 and C-13 don't overlap with existing criteria:** C-12 is additive math on a structured column, distinct from C-05 (prose annotation) and C-10 (naming the sequence). C-13 is a class-level catalog, distinct from C-09 (single adversarial divergence trace) and C-07 (batch edge-case analysis). Each criterion occupies a gap the prior tiers leave open.
tion). Generic "may fail" without a named mechanism fails. |
| C-04 | **Authorization gaps surfaced** | correctness | The trace explicitly identifies where authorization is checked (or not), names the permission/scope/role evaluated, and flags any boundary where authorization is absent or assumed. A trace that never mentions auth fails. |

---

## Recommended Criteria (weight: 30 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Latency sources identified** | depth | Each boundary or processing step contributing non-trivial latency is annotated (e.g., "synchronous Dataverse read -- p99 ~200ms", "token cache miss -- +40ms"). At least three distinct latency sources named. |
| C-06 | **Error path traced end-to-end** | coverage | At least one full error path is traced from origination point to caller response, showing how errors propagate, transform, or get swallowed across boundaries. A trace that covers only the happy path fails this criterion. |
| C-07 | **Batch and edge-case handling** | depth | Batch operations, pagination, or concurrent-request edge cases relevant to the request type are called out explicitly -- not just mentioned but analyzed (e.g., "batch of 1000 items: Dataverse 5000-record limit not hit, but per-request overhead multiplies"). |

---

## Aspirational Criteria (weight: 30 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Actionable remediation per failure point** | behavior | Every failure point from C-03 is paired with a concrete mitigation or design change (retry policy, circuit breaker, permission scope addition, payload validation guard). Generic "add error handling" fails; a specific mechanism passes. |
| C-09 | **Adversarial path comparison** | depth | Trace includes at least one adversarial scenario (malformed payload, expired token, concurrent mutation, missing required field) and shows how it diverges from the nominal path -- naming the specific boundary where divergence occurs and its outcome. |
| C-10 | **Critical path named** | depth | Beyond listing individual latency sources (C-05), the trace identifies the critical path: the specific sequence of boundaries whose cumulative latency determines worst-case response time. Parallel or cached paths are distinguished from the critical path. Total critical-path latency is estimated (p50 and p99). A trace that lists sources but does not name which sequence drives worst-case fails. |
| C-11 | **Authorization re-walk audit** | correctness | After the primary boundary traversal, the trace performs a dedicated second-pass authorization audit: walks the full boundary list from C-02 again, focused exclusively on privilege escalation paths, missing scope validations, and auth that is assumed but never verified. The audit must name at least one gap or escalation path not surfaced in the primary C-04 pass, or explicitly confirm that the re-walk found none. A trace that relies solely on per-boundary auth fields in the primary pass fails. |
| C-12 | **Per-boundary latency budget table** | depth | The traversal carries a dedicated p50/p99 budget column for every boundary -- not prose annotation but a structured column whose rows are individually sourced and collectively consistent with the critical-path total from C-10. Non-parallel segments sum to the total; parallel segments are not double-counted. A trace that annotates latency in prose or provides only a total estimate without per-boundary budget rows fails. |
| C-13 | **Threat class catalog** | depth | The trace includes a structured threat catalog: a table mapping at least four distinct threat classes (e.g., malformed input, credential expiry, concurrent mutation, missing permission scope, network partition) to the specific boundaries where each manifests. Threat classes must be enumerated systematically, not surfaced incidentally through one adversarial scenario. A trace that explores threats ad-hoc without a class-level catalog fails. |

---

## Scoring Worksheet

| Tier | Criteria | Pts Each | Points Available | Points Earned |
|------|----------|----------|-----------------|---------------|
| Essential | C-01, C-02, C-03, C-04 | 15 | 60 | -- |
| Recommended | C-05, C-06, C-07 | 10 | 30 | -- |
| Aspirational | C-08, C-09, C-10, C-11, C-12, C-13 | 5 | 30 | -- |
| **Total** | | | **120** | -- |

All criteria are binary: pass = full points, fail = 0.

**Golden**: all 4 essential pass AND composite >= 80.
