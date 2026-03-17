`flow-integration-rubric-v5-2026-03-14.md` written. Here is the complete updated rubric:

---

# flow-integration Rubric — v5

**Version:** 5 (updated from Round 4 excellence signals)
**Quest:** flow-integration
**Date:** 2026-03-14

---

## Overview

An integration trace maps every call a feature makes to external systems and accounts for auth, shape, error fate, rate limits, idempotency, and the gaps that threaten production reliability. This rubric measures whether a trace is complete, analytical, actionable, and structurally disciplined.

**Tier philosophy:**

- **Essential** (C-01–C-04): documentation completeness — every call accounted for with its auth, shape, and error fate; the minimum for any useful integration trace.
- **Recommended** (C-05–C-07): analysis quality — did the trace catch the integration failure modes that matter in production?
- **Aspirational** (C-08–C-19): actionability and structural discipline — ranked risk, concrete fixes, and organizational guarantees that make the other criteria structurally reliable rather than convention-dependent.

**New in v2:** C-10, C-11, C-12 codify the structural patterns that produced perfect essential coverage in Round 1 (V-04 Gated Phase Lifecycle). These criteria reward traces that cannot accidentally omit a call or bleed concerns across sections.

**New in v3:** C-13, C-14, C-15 codify the structural patterns that broke the 110-point ceiling in Round 2 (V-05 Per-Call Gate Blocks). C-13 makes C-11 violations structurally impossible at the section level. C-14 extends the per-call completion gate from 3-of-5 concerns to all-five-concern scope. C-15 extends the inventory-first guarantee from initial enumeration to runtime completeness.

**New in v4:** C-16, C-17 codify the two structural patterns identified in Round 3. C-16 rewards expert persona declaration before Stage 1 — the zero-cost enrichment mechanism that sharpens call discovery and auth depth without touching any structural guarantee. C-17 rewards in-block rate limit completeness — the architecture that resolves the C-11/C-14 registry trade-off by keeping full rate limit data inside the call block rather than in an external registry, making both criteria simultaneously achievable at full score.

**New in v5:** C-18, C-19 codify the two structural patterns identified in Round 4. C-18 rewards explicit secondary positioning of any cross-stage aggregation structure — the instruction that a fan-out registry is populated FROM the call block and is not the authoritative source, which makes coexistence with C-17 permanently safe rather than convention-dependent. C-19 rewards expert persona four-obligation scope — the full declaration covering forgotten calls, assumed-to-work entries, unknown-system placeholders, and delegation chain risk, which reaches call categories that a minimal two-obligation persona structurally cannot discover.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Tier | Pass Condition |
|----|-----------|----------|------|----------------|
| C-01 | **Call inventory** | correctness | essential | At minimum two calls documented; call types explicit; "unknown system" and "assumed to work" entries present when applicable. |
| C-02 | **Authentication documentation** | correctness | essential | Every call in C-01 has an explicit auth entry; "unknown" acceptable only if flagged as a gap. |
| C-03 | **Request and response format** | correctness | essential | Method + key fields documented per call in separate labeled positions; single merged cell does not pass. |
| C-04 | **Error propagation path** | correctness | essential | Each call has an explicit error-disposition statement; "a call that never fails" still requires a disposition. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Tier | Pass Condition |
|----|-----------|----------|------|----------------|
| C-05 | **Rate limit exposure** | depth | recommended | At least one rate-limit entry per external system; no-limit systems called out as exposure. |
| C-06 | **Retry and idempotency analysis** | depth | recommended | Retry strategy stated for each transiently-failing call; non-idempotent calls without mitigation listed as findings. |
| C-07 | **Gap inventory** | format | recommended | At least one structured finding section with call-ID references and gap-type labels. |

---

## Aspirational Criteria (57 pts total)

| ID | Criterion | Category | Tier | Pass Condition |
|----|-----------|----------|------|----------------|
| C-08 | **Severity ranking** | depth | aspirational | Every finding carries a severity label with a one-line rationale; MEDIUM and LOW findings not exempt. |
| C-09 | **Remediation sketch** | behavior | aspirational | At least one actionable fix per HIGH finding; specific to call context, not generic advice. |
| C-10 | **Inventory-first gate** | format | aspirational | Inventory section appears first and is complete before any per-call analysis; analysis before inventory does not pass. |
| C-11 | **Single-concern phase isolation** | format | aspirational | Each section labeled with exactly one concern; reviewer can locate all content for any concern without scanning elsewhere. |
| C-12 | **Gate-enforced per-call completion** | format | aspirational | At least one section uses an explicit all-calls-covered completion condition; implicit or voluntary does not pass. |
| C-13 | **Per-call section-level concern exclusion** | format | aspirational | Every concern section in at least one call block carries a single-concern declaration and named exclusion of all other concerns within the section itself. |
| C-14 | **Five-concern per-call completion checklist** | format | aspirational | Five-item checklist in every call block; explicitly gates the next call block; three-or-fewer-concern checklist does not pass. |
| C-15 | **Late-call inventory discipline** | format | aspirational | Explicit instruction requiring newly discovered calls be entered into the inventory before their block is opened. |
| C-16 | **Expert persona declaration** | format | aspirational | Named expert persona appears before the inventory gate naming the domain and at least two discovery obligations; generic preamble without domain-specific obligations does not pass. |
| C-17 | **In-block rate limit completeness** | format | aspirational | Every call block contains a rate limit section with limit value, burst risk, and throttle response as separate labeled fields; registry-pointer-only section does not pass. |
| C-18 | **Cross-stage structure explicit secondary positioning** | format | aspirational | Every cross-stage aggregation structure carries an explicit source-of-truth demotion naming all three properties — populated-from, not-authoritative, not-required-for-assessment; structure present without this statement does not pass; traces with no cross-stage structures pass by default. |
| C-19 | **Expert persona four-obligation scope** | format | aspirational | Persona names all four discovery obligation categories — forgotten calls, assumed-to-work entries, unknown-system placeholders, delegation chain risk — before the inventory gate; two or three categories passes C-16 but not C-19. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-19 | 57 |
| **Total** | | **147** |

**Point allocation — aspirational:**

| C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 |
|------|------|------|------|------|------|------|------|------|------|------|------|
| 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | 5 | 5 |

**Golden**: all of C-01 through C-04 pass, composite >= 80.

---

## Two new criteria in plain terms

**C-18** (5 pts) — the fan-out registry drift problem. V-02 fixed the R3 registry design by adding one sentence: "this registry is populated FROM Section D of each call block — it is not the authoritative source." Without that sentence the registry is ambiguous and will eventually be treated as authoritative. C-18 rewards any trace that carries that explicit demotion inside the aggregation structure itself. Passes by default if no cross-stage structure exists.

**C-19** (5 pts) — the minimal-persona ceiling. V-01 passed C-16 with exactly 2 obligations; V-02 used 4. The two additions — delegation chain risk and unknown-system placeholders — reach call categories that a 2-obligation persona never enumerates: proxy tokens, orchestrator credentials, unidentified endpoints. C-19 rewards the full four-obligation persona. A 2-obligation persona still earns C-16; it just cannot earn C-19.
nly in a preamble. |
| C-14 | **Five-concern per-call completion checklist** — A named checklist covering all five integration concerns (auth, format, error fate, rate limits, idempotency) appears within each call block and gates both the next call block and final trace completion. | format | aspirational | A checklist with exactly five concern items appears in every call block; the checklist is explicitly tied to a gate condition that blocks the next call block until all five are checked; a checklist covering three or fewer concerns does not pass. |
| C-15 | **Late-call inventory discipline** — Calls discovered during per-call analysis (not present in the initial inventory) must be added to the inventory table before their call block is written. The inventory-first guarantee extends to runtime completeness, not only initial enumeration. | format | aspirational | The trace contains an explicit instruction or gate statement requiring that newly discovered calls be entered into the inventory before their block is opened; a rule that permits late additions to be absorbed directly into analysis sections does not pass. |
| C-16 | **Expert persona declaration** — Before Stage 1, the trace opens with an explicit named-domain expert role statement that governs call discovery scope, auth depth, and gap sensitivity throughout the trace. The persona must name the domain, the discovery obligations it imposes (e.g., forgotten calls, assumed-to-work entries, delegation chains), and the gap sensitivity it applies. | format | aspirational | A named expert persona statement appears before the inventory gate; the statement names the domain and at least two discovery obligations; a generic "I am an expert" preamble without domain-specific obligations does not pass. |
| C-17 | **In-block rate limit completeness** — The call block contains complete rate limit data — actual documented limit value, burst risk, and throttle response — as a fully populated concern section, not merely a cross-reference to an external registry. All five concern sections are self-contained within the call block; a reviewer can assess all five concerns without leaving the block. | format | aspirational | Every call block contains a rate limit section with limit value, burst risk, and throttle response as separate labeled fields; a section containing only a registry confirmation or cross-reference pointer does not pass; the absence of a known limit is documented as a gap within the block, not deferred to a registry. |
| C-18 | **Cross-stage structure explicit secondary positioning** — When the trace includes any cross-stage aggregation structure (fan-out registry, rate limit summary table, cross-call index) that mirrors or aggregates data already present in call blocks, that structure must carry an explicit statement: (a) it is populated FROM the call block data, not the reverse; (b) it is not the authoritative source for any concern; (c) no concern assessment requires consulting it. The statement must appear within the aggregation structure itself, not only in a preamble. | format | aspirational | Every cross-stage aggregation structure in the trace carries an explicit source-of-truth demotion naming all three properties — populated-from, not-authoritative, not-required-for-assessment; a supplementary registry present without this statement does not pass; traces with no cross-stage aggregation structures pass by default. |
| C-19 | **Expert persona four-obligation scope** — The expert persona declaration covers all four discovery obligation categories: (1) forgotten calls (token acquisition, health checks, webhook receipts, and other calls assumed present but not enumerated); (2) assumed-to-work gap entries (calls included in the inventory even when no failure scenario is known); (3) unknown-system placeholders (calls to systems whose identity or behavior is not yet confirmed); (4) delegation chain risk (calls that appear direct but route through intermediaries, proxies, or orchestrators). Each obligation category must be named explicitly; the trace may use different terminology but must cover the same scope. | format | aspirational | The expert persona statement names all four discovery obligation categories explicitly before the inventory gate; a persona naming two or three categories passes C-16 but not C-19; a persona that names all four using different terminology passes if each category is unambiguously identifiable. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 60 |
| Recommended | C-05, C-06, C-07 | 30 |
| Aspirational | C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19 | 57 |
| **Total** | | **147** |

**Point allocation — aspirational:**

| Criterion | Points | Notes |
|-----------|--------|-------|
| C-08 | 5 | |
| C-09 | 5 | |
| C-10 | 4 | |
| C-11 | 4 | |
| C-12 | 4 | |
| C-13 | 4 | |
| C-14 | 4 | |
| C-15 | 3 | |
| C-16 | 7 | new v4 |
| C-17 | 7 | new v4 |
| C-18 | 5 | new v5 |
| C-19 | 5 | new v5 |

**Golden**: all of C-01 through C-04 pass, composite >= 80.

---

## v5 Change Log

**C-18 added — cross-stage structure explicit secondary positioning (5 pts).** Round 4 V-02 demonstrated that a fan-out rate limit registry can coexist with C-17 (in-block completeness) and C-11 (single-concern isolation) without penalty, but only when the registry carries an explicit instruction: "The Stage 3 registry is a supplementary fan-out index populated from this section — it is not the authoritative source." Without that instruction, a registry that mirrors in-block data is ambiguous: a reviewer reading the trace cannot determine whether the registry is additive convenience or the authoritative copy. Over successive rounds, an undemoted registry tends to drift authoritative through convention — authors stop populating in-block fields because "the registry has it." C-18 closes this drift path by requiring the demotion statement within the aggregation structure itself, not only in a preamble. Traces with no cross-stage aggregation structures pass by default; the criterion only activates when such a structure is present. The 5-point reward reflects that this is a structural discipline criterion protecting C-17's guarantee rather than originating a new coverage obligation.

**C-19 added — expert persona four-obligation scope (5 pts).** Round 4 V-01 passed C-16 with exactly two discovery obligations (minimum threshold), naming forgotten calls and assumed-to-work entries. Round 4 V-02 used four obligations, adding delegation chain risk and unknown-system placeholders. Scoring analysis confirmed that the two additional obligations reach call categories that a two-obligation persona structurally cannot discover: delegation chains surface auth depth involving intermediary systems (proxy tokens, orchestrator credentials) that do not appear in a direct-call enumeration; unknown-system placeholders force the inventory to include calls to unidentified endpoints rather than silently omitting them. C-16 rewards the enrichment mechanism (any domain-specific persona declaration); C-19 rewards full scope coverage (all four obligation categories present). A trace with a two-obligation persona achieves C-16 but leaves delegation chain and unknown-system calls undiscovered. The 5-point reward reflects that C-19 is a scope extension of C-16 rather than an independent structural mechanism, and that full four-obligation coverage is the aspirational ideal, not the minimum.

---

## v4 Change Log (retained for history)

**C-16 added — expert persona declaration (7 pts).** V-01 was the only Round 3 variation to open with a named-domain expert role before Stage 1. The pattern proved structurally inert with respect to C-10–C-15 (the expert persona altered no gate, no exclusion statement, no checklist) — it is purely additive enrichment. The enrichment is non-trivial: V-01's call discovery included forgotten calls and assumed-to-work entries that phase-based and minimal-gate variations omitted; auth sections included delegation chains not found elsewhere. C-16 rewards the declaration that makes this enrichment explicit and repeatable rather than dependent on model memory. An undeclared expert perspective cannot be audited or reproduced; a declared one can.

**C-17 added — in-block rate limit completeness (7 pts).** V-02's Hybrid Registry design confirmed that a rate limit registry-confirmation item satisfies C-14's five-concern checklist scope (C-14 PASS) but creates a C-11 PARTIAL (-2 pts): rate limit content lives in Stage 3, so a reviewer reading a call block cannot find complete rate limit data without scanning elsewhere. The registry approach trades per-call redundancy elimination against per-call completeness, and the trade-off is now quantified at 2 points. C-17 rewards the architecture that avoids the trade-off entirely: full rate limit data (limit value, burst risk, throttle response) as a fully populated section inside the call block. A trace satisfying C-17 achieves both C-11 PASS and C-14 PASS simultaneously, at the cost of duplicating rate limit data across call blocks for fan-out patterns. The 7-point reward reflects that this is the structurally correct resolution and that per-call completeness is the more important property.

---

## v3 Change Log (retained for history)

**C-13 added — per-call section-level concern exclusion (4 pts).** V-05 was the only Round 2 variation to achieve full C-11 credit. It did so by placing an explicit exclusion statement inside each concern section: `"Concern: X only. Do not document Y here."` V-01, V-02, and V-04 relied on phase-level naming alone — a convention that fails when a phase header names two concerns or when a call block groups unrelated fields. C-13 rewards the structural mechanism that makes C-11 violations impossible rather than merely discouraged.

**C-14 added — five-concern per-call completion checklist (4 pts).** V-03 received C-12 PARTIAL because its CALL COMPLETE marker covered only 3 of 5 integration concerns — rate limits and idempotency had no completion signal. V-05 demonstrated that a per-call checklist covering all five concerns both instantiates C-12 at full scope and structurally prevents any concern from being skipped. C-14 rewards checklists that cover all five concerns and gate the next call block on their completion.

**C-15 added — late-call inventory discipline (3 pts).** C-10 (inventory-first gate) guarantees that the initial enumeration is complete before per-call analysis begins. It does not address calls discovered mid-analysis. V-05's inventory GATE with late-call discipline extends this guarantee: any call found during per-call work must be entered into the inventory table before its block is written. C-15 rewards traces that make this runtime-completeness rule explicit, closing the gap where late-discovered calls could bypass the inventory gate entirely.
