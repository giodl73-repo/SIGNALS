Rubric written to `simulations/quest/rubrics/flow-integration-rubric-2026-03-14.md`.

**Structure:**

- **4 essential** (C-01–C-04): call inventory, auth, request/response format, error propagation — the minimum for any useful integration trace
- **3 recommended** (C-05–C-07): rate limit exposure, retry/idempotency analysis, collected gap inventory
- **2 aspirational** (C-08–C-09): severity ranking of gaps, remediation sketches for high-severity findings

The essential tier deliberately focuses on *documentation completeness* — every call must be accounted for with its auth, shape, and error fate. The recommended tier shifts to *analysis quality* — did the trace catch the integration failure modes that matter in production? The aspirational tier requires *actionability* — ranked risk and concrete fixes.
*Authentication documentation** -- For each call in the inventory, the auth mechanism is stated (API key, OAuth token, service identity, none). | correctness | essential | Every call in C-01 has an explicit auth entry; "unknown" is acceptable only if the trace explicitly flags it as a gap. |
| C-03 | **Request and response format** -- For each call, the request shape (method, headers, body schema) and expected response shape are described. | correctness | essential | At minimum method + key fields documented per call; partial schemas are acceptable when the trace notes incompleteness. |
| C-04 | **Error propagation path** -- For each call, the trace shows what happens to an error: is it surfaced, transformed, swallowed, or retried? | correctness | essential | Each call has an explicit error-disposition statement; calls with no error handling are flagged as gaps, not omitted. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Rate limit exposure** -- Rate limits (or their absence) are documented for each external call; burst risk and throttling behavior are identified. | depth | recommended | At least one rate-limit entry per external system; systems with no documented limit are explicitly called out as exposure. |
| C-06 | **Retry and idempotency analysis** -- Retry logic is described (backoff strategy, max attempts, jitter); calls lacking idempotency guarantees are flagged. | depth | recommended | Retry strategy stated for each call that can fail transiently; non-idempotent calls without mitigation are listed as findings. |
| C-07 | **Gap inventory** -- Authentication gaps, rate limit exposure, error swallowing, and missing idempotency are collected into a named finding list. | format | recommended | At least one structured finding section exists; each finding references the call ID from C-01 and states the gap type. |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Severity ranking** -- Findings from C-07 are ranked by operational risk (e.g., data loss vs. latency vs. security). | depth | aspirational | Each finding carries a severity label (high/medium/low) with a one-line rationale; ordering reflects risk, not discovery order. |
| C-09 | **Remediation sketch** -- For each high-severity finding, a concrete mitigation is proposed (e.g., add idempotency key, implement exponential backoff with jitter, rotate credential scope). | behavior | aspirational | At least one actionable fix per high-severity finding; fix is specific to the call context, not generic advice. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 60 |
| Recommended | C-05, C-06, C-07 | 30 |
| Aspirational | C-08, C-09 | 10 |
| **Total** | | **100** |

**Golden**: all of C-01 through C-04 pass, composite >= 80.
