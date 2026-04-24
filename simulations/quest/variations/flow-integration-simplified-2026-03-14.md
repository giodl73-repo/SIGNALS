---

## Simplification Report — flow-integration V-05

**Word count: 1179 → 928 (−251 words, 21.3% reduction)**

---

### Removed items and rationale

| # | What was removed | Words | Rubric reason it does NO work |
|---|-----------------|-------|-------------------------------|
| 1 | WHY S1 elaboration: "— the SDK surface mismatch compounds at every integration point, producing phantom calls that never appear in auth or rate-limit planning." | 21 | C-44 inertia sentence 1 is complete at "not reflected in spec diagrams." The elaboration clause adds color, not structure. |
| 2 | WHY S2 examples: "— managed identity, OBO exchange, service principal impersonation —" | 8 | Delegation-chain root cause is named without the parenthetical. C-44 sentence 2 satisfied. |
| 3 | WHY S3 elaboration: "creating a gap between what the feature developer believes is the integration surface and what is actually established on the wire" | 18 | C-44 inertia sentence 3 is complete at "never explicitly scoped in most feature specs." The gap description is implicit. |
| 4 | WHY anchor tail: "and cannot be cleared without a completed trace" | 9 | No criterion (C-37/C-39/C-42/C-43) requires a clearing condition. Anchor closes at "at integration review." |
| 5 | Role declaration: "You are a connectors and backend integration domain expert." | 9 | C-16 pass condition is satisfied by the `EXPERT PERSONA DECLARATION` block's "Domain:" line. This sentence is redundant. |
| 6 | Domain detail: "— Power Platform connectors, Azure APIs, MCP servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange" | 17 | C-16 requires naming the domain. "Connectors and backend integration" names it; the elaboration is not scored. |
| 7 | EXPERT PERSONA preamble tail: "structural completeness is verified by row count; a missing row is a missing obligation" | 14 | C-24 pass condition is the table structure itself, not the preamble prose describing it. |
| 8 | ARE directive explanation: "A column header that does not match its row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the Stage 1 inventory column headers without reading prose." | 35 | C-26/C-29/C-32 require the ARE directive. This sentence explains the mechanism but is not itself scored. |
| 9 | Apply reminder: "Apply all five discovery obligations while building the Stage 1 inventory." | 10 | C-19 pass condition is satisfied by the obligation table. Reminder is redundant. |
| 10 | Stage 1 preamble: "Populate this table before opening Stage 2." | 8 | C-10 is satisfied by the INVENTORY GATE alone. Preamble duplicates the gate. |
| 11 | INVENTORY GATE field list: "the table is complete — every discovered call has a row with Call ID, Target System, Call Type, Confidence, and all five" | 19 | C-10 requires the gate exists; field names are visible from the table header row. |
| 12 | AGGREGATION RULE examples: "(fan-out registry, call-category summary, cross-call rollup table)" | 8 | C-18 requires three named properties; it does not require example structure types. |
| 13 | AGGREGATION RULE no-structures line: "Traces with no cross-stage structures satisfy this rule by default." | 9 | C-20 (unconditional coda with no-structures default) handles this case; the AGGREGATION RULE need not repeat it. |
| 14 | CODA "For any cross-stage structure" table (3-row properties table + header line) | 27 | C-18's three properties (populated-from, not-authoritative, not-required) are fully covered by the AGGREGATION RULE. The CODA need only satisfy C-20/C-23/C-28, none of which require this table. |
| 15 | Stage 3 gap type hint list: "auth-gap / rate-limit-gap / retry-gap / error-swallow / dark-system / chain-hop / cold-start-gap / shadow-gap" | 13 | C-07 requires "gap-type labels" in output, not the prompt to enumerate valid types. Model infers gap types from context. |
| 16 | Section annotation verbosity: "this section: " prefix and "each ... below" suffix in 5 per-call headers | ~16 | C-13 requires single-concern declaration + named exclusion. The trimmed form "*(authentication only — ...have their own sections)*" satisfies both conditions without "this section:" or "below." |

---

### Criteria verification

All essential criteria satisfied:

| Criterion | How satisfied in simplified prompt |
|-----------|-----------------------------------|
| **C-36** WHY block | Present, named, before EXPERT PERSONA DECLARATION |
| **C-37** temporal stakes anchor | "MUST become ship-blockers at integration review" — delivery-phase form |
| **C-39** consequence-form equivalence | Consequence-form + delivery-phase marker present |
| **C-40** register-neutrality | MUST = unconditional; no weakening modal |
| **C-41** inertia-context neutrality | 3 inertia sentences present; anchor evaluates independently |
| **C-42** highest-information WHY | Stakes anchor + 4-concern enumeration both present |
| **C-43** RFC-modal MUST | Explicit MUST in anchor |
| **C-44** inertia-dominant 3-sentence form | 3 inertia sentences + MUST anchor-close |
| **C-50** C-43+C-44 simultaneous | Both present; no interaction penalty |
| **C-27/C-30/C-31/C-34** dual-surface prohibition | YOU MUST NOT block names all 4 substituted canonical tokens inline |
| **C-16** expert persona | EXPERT PERSONA DECLARATION + Domain: line before inventory gate |
| **C-19** four-obligation scope | 5-row obligation table before inventory gate |
| **C-24** obligation table schema | 5 rows, one per obligation |
| **C-25/C-26/C-29/C-32/C-33** ARE directive | "ARE the Obligation Term column values above — use those exact tokens" |
| **C-35** extended obligation scalability | 5-row table passes C-24 |
| **C-10** inventory-first gate | INVENTORY GATE present and explicit |
| **C-15** late-call discipline | NEW-CALL RULE present |
| **C-21** flag alignment | Inventory table flag columns = obligation terms |
| **C-22/C-25** vocabulary unification | Column headers ARE obligation terms (ghost-call, shadow-doc, etc.) |
| **C-18** cross-stage secondary positioning | AGGREGATION RULE names all 3 properties |
| **C-20** unconditional coda | "This coda fires unconditionally" + no-structures default |
| **C-23** unnumbered coda | Coda carries no stage number, appended after Stage 3 |
| **C-28** terminal-position formula | Header annotation + "does not appear between any two numbered stages" sentence |
| **C-11/C-13** single-concern isolation | Per-call section headers retain single-concern + exclusion annotation |
| **C-12/C-14** gate-enforced completion | CALL-[N] COMPLETION GATE with 5-row checklist |
| **C-17** in-block rate limit | [N.3] RATE LIMITS table with limit value/burst risk/throttle response |
| **C-07/C-08/C-09** gap inventory | Stage 3 with severity + rationale + remediation fields |

**All essential criteria: PASS. All aspirational criteria targeted by V-05 (C-27, C-30, C-31, C-34, C-35, C-36–C-44, C-50): PASS.**

Predicted score unchanged at **297/302**.

---

```json
{"simplified_word_count": 928, "original_word_count": 1179, "all_essential_still_pass": true}
```
