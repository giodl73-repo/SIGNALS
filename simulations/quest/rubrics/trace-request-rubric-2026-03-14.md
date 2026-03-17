Rubric written to `simulations/quest/rubrics/trace-request-rubric-2026-03-14.md`.

**Structure:**

- **4 Essential (C-01–C-04, 60 pts):** Entry point declared, all service boundaries enumerated, failure point at each boundary, authorization gaps surfaced. These are the core of hand-compilation — a trace missing any one of these is not useful.
- **3 Recommended (C-05–C-07, 30 pts):** Latency sources, end-to-end error path, batch/edge-case handling. These separate a good trace from a minimal one.
- **2 Aspirational (C-08–C-09, 10 pts):** Actionable remediation per failure point, adversarial path comparison. These push toward a trace that drives design action, not just documentation.

The binary scoring keeps evaluation fast — no partial credit debates. Golden requires all 4 essential + composite >= 80, meaning at least ~2 of 3 recommended must also pass.
, path, payload shape, and caller identity. Missing or vague entry point fails. |
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

## Aspirational Criteria (weight: 10 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Actionable remediation per failure point** | behavior | Every failure point from C-03 is paired with a concrete mitigation or design change (retry policy, circuit breaker, permission scope addition, payload validation guard). Generic "add error handling" fails; a specific mechanism passes. |
| C-09 | **Adversarial path comparison** | depth | Trace includes at least one adversarial scenario (malformed payload, expired token, concurrent mutation, missing required field) and shows how it diverges from the nominal path -- naming the specific boundary where divergence occurs and its outcome. |

---

## Scoring Worksheet

| Tier | Criteria | Pts Each | Points Available | Points Earned |
|------|----------|----------|-----------------|---------------|
| Essential | C-01, C-02, C-03, C-04 | 15 | 60 | -- |
| Recommended | C-05, C-06, C-07 | 10 | 30 | -- |
| Aspirational | C-08, C-09 | 5 | 10 | -- |
| **Total** | | | **100** | -- |

All criteria are binary: pass = full points, fail = 0.

**Golden**: all 4 essential pass AND composite >= 80.
