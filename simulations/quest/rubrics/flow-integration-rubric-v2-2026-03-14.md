Here is the complete updated rubric:

---

# flow-integration Rubric — v2

**Version:** 2 (updated from Round 1 excellence signals)
**Quest:** flow-integration
**Date:** 2026-03-14

---

## Overview

An integration trace maps every call a feature makes to external systems and accounts for auth, shape, error fate, rate limits, idempotency, and the gaps that threaten production reliability. This rubric measures whether a trace is complete, analytical, actionable, and structurally disciplined.

**Tier philosophy:**

- **Essential** (C-01–C-04): documentation completeness — every call accounted for with its auth, shape, and error fate; the minimum for any useful integration trace.
- **Recommended** (C-05–C-07): analysis quality — did the trace catch the integration failure modes that matter in production?
- **Aspirational** (C-08–C-12): actionability and structural discipline — ranked risk, concrete fixes, and organizational guarantees that make the other criteria structurally reliable rather than convention-dependent.

**New in v2:** C-10, C-11, C-12 codify the structural patterns that produced perfect essential coverage in Round 1 (V-04 Gated Phase Lifecycle). These criteria reward traces that cannot accidentally omit a call or bleed concerns across sections.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Tier | Pass Condition |
|----|-----------|----------|------|----------------|
| C-01 | **Call inventory** — Every external call the feature makes is enumerated in a named inventory: system, protocol, call type (read/write/webhook/etc.). Calls that are assumed to work and calls to unknown systems are included, not omitted. | correctness | essential | At minimum two calls documented; call types are explicit; "unknown system" and "assumed to work" entries are present when applicable rather than silently absent. |
| C-02 | **Authentication documentation** — For each call in the inventory, the auth mechanism is stated (API key, OAuth token, service identity, none). Token expiry handling and credential rotation policy are noted where known. | correctness | essential | Every call in C-01 has an explicit auth entry; "unknown" is acceptable only if the trace explicitly flags it as a gap. |
| C-03 | **Request and response format** — For each call, the request shape (method, headers, body schema) and expected response shape are described in a dedicated section or column. All four elements — method, headers, body, response — have their own labeled fields; they are not compressed into a single cell. | correctness | essential | At minimum method + key fields documented per call in separate labeled positions; partial schemas are acceptable when the trace notes incompleteness; a single combined "Request / Response" cell that merges all four elements does not pass. |
| C-04 | **Error propagation path** — For each call, the trace shows what happens to an error: is it surfaced, transformed, swallowed, or retried? | correctness | essential | Each call has an explicit error-disposition statement; calls with no error handling are flagged as gaps, not omitted; "a call that never fails" still requires a disposition. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Tier | Pass Condition |
|----|-----------|----------|------|----------------|
| C-05 | **Rate limit exposure** — Rate limits (or their absence) are documented for each external call; burst risk and throttling behavior are identified. | depth | recommended | At least one rate-limit entry per external system; systems with no documented limit are explicitly called out as exposure. |
| C-06 | **Retry and idempotency analysis** — Retry logic is described (backoff strategy, max attempts, jitter); calls lacking idempotency guarantees are flagged. | depth | recommended | Retry strategy stated for each call that can fail transiently; non-idempotent calls without mitigation are listed as findings. |
| C-07 | **Gap inventory** — Authentication gaps, rate limit exposure, error swallowing, and missing idempotency are collected into a named finding list; each finding references the call ID from C-01 and states the gap type. | format | recommended | At least one structured finding section exists with call-ID references and gap-type labels; findings are not left inline in per-call sections only. |

---

## Aspirational Criteria (22 pts total)

| ID | Criterion | Category | Tier | Pass Condition |
|----|-----------|----------|------|----------------|
| C-08 | **Severity ranking** — Findings from C-07 are ranked by operational risk (e.g., data loss vs. latency vs. security). | depth | aspirational | Each finding carries a severity label (high/medium/low) with a one-line rationale; ordering reflects risk, not discovery order; **MEDIUM and LOW findings have rationale, not only HIGH.** |
| C-09 | **Remediation sketch** — For each high-severity finding, a concrete mitigation is proposed. | behavior | aspirational | At least one actionable fix per high-severity finding; fix is specific to the call context, not generic advice; concrete parameters (header names, timing values, replacement patterns) are preferred over instructions. |
| C-10 | **Inventory-first gate** — The trace opens with a completed, named call inventory before any per-call analysis section begins. All subsequent sections cite calls by ID from that inventory; no analysis precedes the inventory's completion. | format | aspirational | An inventory section appears first and is complete before any per-call analysis; at least one subsequent section cites call IDs from it; analysis sections that appear before the inventory do not pass. |
| C-11 | **Single-concern phase isolation** — Each named analysis section addresses exactly one integration concern (auth, format, error fate, rate limits, idempotency). No section mixes concerns. | format | aspirational | Each section can be labeled with exactly one concern; the reviewer can locate all content for any given concern without scanning elsewhere; sections addressing two or more concerns simultaneously do not pass. |
| C-12 | **Gate-enforced per-call completion** — For at least one analysis section, the completion condition explicitly references all calls in the inventory: the section is not considered complete until every call has an entry. | format | aspirational | At least one section uses an explicit all-calls-covered completion condition (gate statement, "one row per Call ID — omission is not acceptable", or per-call checklist); the completion condition is not implicit or voluntary. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 60 |
| Recommended | C-05, C-06, C-07 | 30 |
| Aspirational | C-08, C-09, C-10, C-11, C-12 | 22 |
| **Total** | | **112** |

**Golden**: all of C-01 through C-04 pass, composite >= 80.

---

## v2 Change Log

**C-03 tightened.** Pass condition now explicitly rejects a single combined "Request / Response" cell. V-05 failed golden on C-03 because compressing method + headers + body + response into one markdown cell creates schema incompleteness risk under real integrations. The rubric now names that failure mode directly.

**C-08 tightened.** Pass condition now requires rationale for MEDIUM and LOW findings, not only HIGH. V-03 received PARTIAL because only HIGH findings had a "Why HIGH:" prompt. Now all three severity levels require rationale.

**C-10 added — inventory-first gate (4 pts).** V-04 demonstrated that opening with a closed inventory structurally prevents call undercounting: analysis cannot proceed until the inventory is complete, so late-discovered calls cannot be silently absorbed into analysis sections.

**C-11 added — single-concern phase isolation (4 pts).** V-04 demonstrated that permitting each section exactly one concern makes cross-concern bleeding structurally impossible. A reader or checker can verify completeness per concern without disambiguation.

**C-12 added — gate-enforced per-call completion (4 pts).** V-04 demonstrated that an explicit per-call gate ("gate fires only when every call has an entry") is a stronger guarantee than a pre-printed template that a writer may partially fill. At least one section must use this pattern to pass.

**Point total:** 100 → 112 (aspirational tier 10 → 22). Golden condition unchanged.

---

Three decisions worth noting:

1. **C-10/C-11/C-12 are aspirational, not essential.** A trace can be fully correct (all C-01–C-04 pass) without structural isolation — V-01 (the control) proved this. The new criteria reward the structural discipline that makes correctness *guaranteed* rather than *achieved*, which is a higher bar.

2. **C-03 tightening is retroactive.** V-05 would have failed C-03 under v1 as written, but the v1 pass condition didn't explicitly name the single-cell failure. v2 closes that ambiguity so future variations can't exploit the same compression.

3. **Total 112, not 100.** The aspirational tier expanded from 10 to 22 to accommodate three new 4-pt criteria without compressing existing signals. Golden threshold (>=80 with all essential passing) is unaffected.
