---

## `trace-request-rubric-v2-2026-03-14.md`

**Changes from v1:**

Two new aspirational criteria, expanding the tier from 2 → 4 criteria (10 → 20 pts). Total scale 100 → 110. Golden threshold unchanged at >= 80.

---

### New Criteria

**C-10 — Critical path named** (depth, 5 pts)

Extracted from V-04's p50/p99 + critical path annotation and V-02's latency column. C-05 already requires three named latency sources — C-10 requires naming the *sequence* whose cumulative latency determines worst-case response time, with parallel/cached paths explicitly distinguished, and a p50/p99 total estimate. A trace that lists sources but doesn't identify which sequence drives worst-case fails.

**C-11 — Authorization re-walk audit** (correctness, 5 pts)

Extracted from V-04's dedicated PHASE 4, called out in the scorecard as "strongest single-criterion enforcement for C-04 across all variations." C-04 surfaces auth gaps per-boundary during the primary traversal. C-11 requires a *dedicated second pass* over the full boundary list from C-02, focused exclusively on privilege escalation paths, missing scope validations, and assumed-but-unverified auth. Must name at least one gap the primary pass missed — or explicitly confirm the re-walk found none. A trace that relies solely on the primary traversal fails.

---

### Why these two, not others

| Signal considered | Disposition |
|---|---|
| V-02 disqualifying text pattern ("may fail" explicitly named as failing) | Evaluation mechanism, not a new criterion — belongs in variation design guidance |
| V-04 PHASE 4 dedicated auth re-walk | C-11 |
| V-02/V-04 critical path + p50 estimate | C-10 |
| V-02 four-field adversarial structure | Already captured by C-09; structure belongs in variation design |

### Scoring recap

| Tier | Criteria | Pts Each | Available |
|---|---|---|---|
| Essential | C-01–C-04 | 15 | 60 |
| Recommended | C-05–C-07 | 10 | 30 |
| Aspirational | C-08–C-11 | 5 | 20 |
| **Total** | | | **110** |

Golden: all 4 essential + composite >= 80.
)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Entry point declared** | coverage | The trace names the exact entry point: HTTP method, path, payload shape, and caller identity. Missing or vague entry point fails. |
| C-02 | **All service boundaries crossed** | coverage | Every distinct service boundary in the request path is enumerated in traversal order (e.g., gateway -> auth service -> domain API -> storage). Any boundary skipped -- including a well-known step like token validation -- fails. |
| C-03 | **Failure point at each boundary** | correctness | For every boundary listed in C-02, at least one concrete failure mode is identified (timeout, 4xx/5xx, auth rejection, payload mismatch, throttle, network partition). Generic "may fail" without a named mechanism fails. |
| C-04 | **Authorization gaps surfaced** | correctness | The trace explicitly identifies where authorization is checked (or not), names the permission/scope/role evaluated, and flags any boundary where authorization is absent or assumed. A trace that never mentions auth fails. |

---

## Recommended Criteria (weight: 30 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Latency sources identified** | depth | Each boundary or processing step contributing non-trivial latency is annotated (e.g., "synchronous Dataverse read -- p99 ~200ms", "token cache miss -- +40ms"). At least three distinct latency sources named. |
| C-06 | **Error path traced end-to-end** | coverage | At least one full error path is traced from origination point to caller response, showing how errors propagate, transform, or get swallowed across boundaries. A trace that covers only the happy path fails this criterion. |
| C-07 | **Batch and edge-case handling** | depth | Batch operations, pagination, or concurrent-request edge cases relevant to the request type are called out explicitly -- not just mentioned but analyzed (e.g., "batch of 1000 items: Dataverse 5000-record limit not hit, but per-request overhead multiplies"). |

---

## Aspirational Criteria (weight: 20 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Actionable remediation per failure point** | behavior | Every failure point from C-03 is paired with a concrete mitigation or design change (retry policy, circuit breaker, permission scope addition, payload validation guard). Generic "add error handling" fails; a specific mechanism passes. |
| C-09 | **Adversarial path comparison** | depth | Trace includes at least one adversarial scenario (malformed payload, expired token, concurrent mutation, missing required field) and shows how it diverges from the nominal path -- naming the specific boundary where divergence occurs and its outcome. |
| C-10 | **Critical path named** | depth | Beyond listing individual latency sources (C-05), the trace identifies the critical path: the specific sequence of boundaries whose cumulative latency determines worst-case response time. Parallel or cached paths are distinguished from the critical path. Total critical-path latency is estimated (p50 and p99). A trace that lists sources but does not name which sequence drives worst-case fails. |
| C-11 | **Authorization re-walk audit** | correctness | After the primary boundary traversal, the trace performs a dedicated second-pass authorization audit: walks the full boundary list from C-02 again, focused exclusively on privilege escalation paths, missing scope validations, and auth that is assumed but never verified. The audit must name at least one gap or escalation path not surfaced in the primary C-04 pass, or explicitly confirm that the re-walk found none. A trace that relies solely on per-boundary auth fields in the primary pass fails. |

---

## Scoring Worksheet

| Tier | Criteria | Pts Each | Points Available | Points Earned |
|------|----------|----------|-----------------|---------------|
| Essential | C-01, C-02, C-03, C-04 | 15 | 60 | -- |
| Recommended | C-05, C-06, C-07 | 10 | 30 | -- |
| Aspirational | C-08, C-09, C-10, C-11 | 5 | 20 | -- |
| **Total** | | | **110** | -- |

All criteria are binary: pass = full points, fail = 0.

**Golden**: all 4 essential pass AND composite >= 80.
