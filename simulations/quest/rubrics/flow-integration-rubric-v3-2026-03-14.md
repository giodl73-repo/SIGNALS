# flow-integration Rubric — v3

**Version:** 3 (updated from Round 2 excellence signals)
**Quest:** flow-integration
**Date:** 2026-03-14

---

## Overview

An integration trace maps every call a feature makes to external systems and accounts for auth, shape, error fate, rate limits, idempotency, and the gaps that threaten production reliability. This rubric measures whether a trace is complete, analytical, actionable, and structurally disciplined.

**Tier philosophy:**

- **Essential** (C-01–C-04): documentation completeness — every call accounted for with its auth, shape, and error fate; the minimum for any useful integration trace.
- **Recommended** (C-05–C-07): analysis quality — did the trace catch the integration failure modes that matter in production?
- **Aspirational** (C-08–C-15): actionability and structural discipline — ranked risk, concrete fixes, and organizational guarantees that make the other criteria structurally reliable rather than convention-dependent.

**New in v2:** C-10, C-11, C-12 codify the structural patterns that produced perfect essential coverage in Round 1 (V-04 Gated Phase Lifecycle). These criteria reward traces that cannot accidentally omit a call or bleed concerns across sections.

**New in v3:** C-13, C-14, C-15 codify the structural patterns that broke the 110-point ceiling in Round 2 (V-05 Per-Call Gate Blocks). C-13 makes C-11 violations structurally impossible at the section level. C-14 extends the per-call completion gate from 3-of-5 concerns to all-five-concern scope. C-15 extends the inventory-first guarantee from initial enumeration to runtime completeness.

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

## Aspirational Criteria (33 pts total)

| ID | Criterion | Category | Tier | Pass Condition |
|----|-----------|----------|------|----------------|
| C-08 | **Severity ranking** — Findings from C-07 are ranked by operational risk (e.g., data loss vs. latency vs. security). | depth | aspirational | Each finding carries a severity label (high/medium/low) with a one-line rationale; ordering reflects risk, not discovery order; MEDIUM and LOW findings have rationale, not only HIGH. |
| C-09 | **Remediation sketch** — For each high-severity finding, a concrete mitigation is proposed. | behavior | aspirational | At least one actionable fix per high-severity finding; fix is specific to the call context, not generic advice; concrete parameters (header names, timing values, replacement patterns) are preferred over instructions. |
| C-10 | **Inventory-first gate** — The trace opens with a completed, named call inventory before any per-call analysis section begins. All subsequent sections cite calls by ID from that inventory; no analysis precedes the inventory's completion. | format | aspirational | An inventory section appears first and is complete before any per-call analysis; at least one subsequent section cites call IDs from it; analysis sections that appear before the inventory do not pass. |
| C-11 | **Single-concern phase isolation** — Each named analysis section addresses exactly one integration concern (auth, format, error fate, rate limits, idempotency). No section mixes concerns. | format | aspirational | Each section can be labeled with exactly one concern; the reviewer can locate all content for any given concern without scanning elsewhere; sections addressing two or more concerns simultaneously do not pass. |
| C-12 | **Gate-enforced per-call completion** — For at least one analysis section, the completion condition explicitly references all calls in the inventory: the section is not considered complete until every call has an entry. | format | aspirational | At least one section uses an explicit all-calls-covered completion condition (gate statement, "one row per Call ID — omission is not acceptable", or per-call checklist); the completion condition is not implicit or voluntary. |
| C-13 | **Per-call section-level concern exclusion** — Each concern section within a call block carries an explicit exclusion statement naming the one concern it covers and the concerns it must not contain (e.g., `"Concern: authentication only. Do not document format, error handling, or rate limits here."`). | format | aspirational | Every concern section in at least one call block carries an explicit single-concern declaration and a named exclusion of all other concerns; a phase-level label alone does not pass; the exclusion statement must appear within the section itself, not only in a preamble. |
| C-14 | **Five-concern per-call completion checklist** — A named checklist covering all five integration concerns (auth, format, error fate, rate limits, idempotency) appears within each call block and gates both the next call block and final trace completion. | format | aspirational | A checklist with exactly five concern items appears in every call block; the checklist is explicitly tied to a gate condition that blocks the next call block until all five are checked; a checklist covering three or fewer concerns does not pass. |
| C-15 | **Late-call inventory discipline** — Calls discovered during per-call analysis (not present in the initial inventory) must be added to the inventory table before their call block is written. The inventory-first guarantee extends to runtime completeness, not only initial enumeration. | format | aspirational | The trace contains an explicit instruction or gate statement requiring that newly discovered calls be entered into the inventory before their block is opened; a rule that permits late additions to be absorbed directly into analysis sections does not pass. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 60 |
| Recommended | C-05, C-06, C-07 | 30 |
| Aspirational | C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-15 | 33 |
| **Total** | | **123** |

**Golden**: all of C-01 through C-04 pass, composite >= 80.

---

## v3 Change Log

**C-13 added — per-call section-level concern exclusion (4 pts).** V-05 was the only Round 2 variation to achieve full C-11 credit. It did so by placing an explicit exclusion statement inside each concern section: `"Concern: X only. Do not document Y here."` V-01, V-02, and V-04 relied on phase-level naming alone — a convention that fails when a phase header names two concerns or when a call block groups unrelated fields. C-13 rewards the structural mechanism that makes C-11 violations impossible rather than merely discouraged.

**C-14 added — five-concern per-call completion checklist (4 pts).** V-03 received C-12 PARTIAL because its CALL COMPLETE marker covered only 3 of 5 integration concerns — rate limits and idempotency had no completion signal. V-05 demonstrated that a per-call checklist covering all five concerns both instantiates C-12 at full scope and structurally prevents any concern from being skipped. C-14 rewards checklists that cover all five concerns and gate the next call block on their completion.

**C-15 added — late-call inventory discipline (3 pts).** C-10 (inventory-first gate) guarantees that the initial enumeration is complete before per-call analysis begins. It does not address calls discovered mid-analysis. V-05's inventory GATE with late-call discipline extends this guarantee: any call found during per-call work must be entered into the inventory table before its block is written. C-15 rewards traces that make this runtime-completeness rule explicit, closing the gap where late-discovered calls could bypass the inventory gate entirely.
