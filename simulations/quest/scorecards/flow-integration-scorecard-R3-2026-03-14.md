Scorecard written to `simulations/quest/scorecards/flow-integration-scorecard-R3-2026-03-14.md`.

---

## Round 3 Results — flow-integration

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | **V-01** Expert-First | **123/123** | YES |
| 1 | **V-05** Maximally Explicit | **123/123** | YES |
| 3 | **V-02** Hybrid Registry | **121/123** | YES |
| 4 | **V-04** Imperative + 5-Concern CALL COMPLETE | **117/123** | YES |
| 5 | **V-03** Minimal Gates + Phase 5 Split | **115/123** | YES |

**5 of 5 golden.** First round where every variation clears golden at the full 123-point ceiling.

---

### Key R3 findings

**V-01 and V-05 tie at ceiling.** The expert persona in V-01 is structurally inert — it enriches call discovery semantics without touching any of the structural guarantees (C-10–C-15). "Do not document X" vs "You MUST NOT document X" makes no difference to rubric score. C-13's pass condition is satisfied by both.

**V-02 C-14 hypothesis confirmed.** A registry-confirmation item does satisfy C-14's fifth-concern slot. The cost is C-11 PARTIAL (-2 pts): rate limit content lives in Stage 3, not in the call block — "without scanning elsewhere" is violated. Trade-off is now quantified.

**V-03 and V-04 confirm the per-call block boundary.** Phase 5 split resolves C-11 for V-03. But neither phase-based (V-03) nor step-based (V-04) structures can satisfy C-13 or C-14 — both require the per-call block architecture. V-04's R2 Open Q3 answered: expanding CALL COMPLETE to 5 concerns fixes C-12 but costs 6 points total (C-13 FAIL + C-14 PARTIAL), not 4 as hypothesized.

```json
{"top_score": 123, "all_essential_pass": true, "new_patterns": ["expert-persona-zero-cost-enrichment: declaring a domain expert role before Stage 1 enriches call discovery (forgotten calls, assumed-to-work entries) and auth depth (delegation chains) without altering structural guarantees -- additive with any per-call block template at zero scoring cost", "registry-cross-reference-C14-pass-C11-partial: a rate limit registry-confirmation item satisfies five-concern checklist scope (C-14 PASS) but moving rate limit content out of the call block creates a scanning-elsewhere violation (C-11 PARTIAL, -2 pts) -- quantified trade-off between fan-out redundancy elimination and per-call completeness"]}
```
oken expiry, credential rotation, security note, gap flag. "Do not let familiarity with a system cause you to skip fields."
- **C-03: PASS** -- Section B: method, headers, body, response as four separate labeled lines. "A single merged cell is not acceptable."
- **C-04: PASS** -- Section C: disposition, transformation detail, gap flag. "A call that 'never fails' is not exempt."
- **C-05: PASS** -- Section D per call: documented limit, burst risk, throttle response, gap flag. Absence of limit = RATE-EXPOSURE gap.
- **C-06: PASS** -- Section E: retry strategy, parameters, max attempts, idempotency guarantee, mitigation, gap flag.
- **C-07: PASS** -- Stage 3: Finding ID, Call ID, Section, Gap Type, Description. At-minimum requirements (one AUTH, one RATE, one RETRY/IDEMPOTENCY finding).
- **C-08: PASS** -- Stage 4: rationale required for ALL findings (HIGH, MEDIUM, LOW). HIGH-first ordering.
- **C-09: PASS** -- Concrete HIGH remediation: exact header names, backoff parameters, specific flow replacements. Generic advice excluded.
- **C-10: PASS** -- INVENTORY GATE: "Stage 2 does not begin until this table has a row for every cross-system call the feature makes. No per-call analysis of any kind appears in Stage 1."
- **C-11: PASS** -- Every section: "Concern: X only. Do not document Y, Z, A, B here." Five sections, five distinct concerns, no mixing. Rate limits (Section D) and retry/idempotency (Section E) in separate sections.
- **C-12: PASS** -- "Do not open the next call block until all five boxes are checked." + "The trace is not complete until every Call ID from Stage 1 has a call block with a fully checked completion checklist."
- **C-13: PASS** -- Every section carries explicit concern declaration + named exclusion of all other concerns within the section body. Not preamble-only. All four excluded concerns named per section. Section A: "Concern: authentication only. Do not document request format, error handling, rate limits, or retry logic here."
- **C-14: PASS** -- Five items (A--E): auth, format, error fate, rate limit, retry/idempotency. "Do not open the next call block until all five boxes are checked."
- **C-15: PASS** -- LATE-CALL RULE: "you must STOP, add it to this table with the next available Call ID, and THEN write its call block. You may not write a call block for a call that has no inventory entry."

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | **123** |

**Golden: YES** (all essential PASS; composite 123/123)

---

### V-02 -- Hybrid Per-Call Blocks + Rate Limit Registry

**Design:** Per-call blocks with four concern sections (A--D: auth, format, error fate, retry/idempotency). Rate limit content extracted to shared per-system Stage 3 registry. Section E = registry confirmation only. Five-concern checklist uses registry confirmation as fifth item.

- **C-01: PASS** -- Stage 1 table; INVENTORY GATE; LATE-CALL RULE covering Stage 2 and Stage 3 discovery.
- **C-02: PASS** -- Section A: all five auth fields with gap flag.
- **C-03: PASS** -- Section B: four separate labeled lines. "All four fields are required as separate labeled lines."
- **C-04: PASS** -- Section C: disposition, gap flag. "Retried -- see Section D" defers correctly. "Never fails" requires disposition.
- **C-05: PASS** -- Stage 3 Rate Limit Registry: one row per system, documented limit, burst risk, throttle response, gap flag. Exposure gap for undocumented limits.
- **C-06: PASS** -- Section D (Retry Logic and Idempotency): strategy, parameters, max attempts, idempotency, mitigation, gap flag.
- **C-07: PASS** -- Stage 4 Gap Inventory: Finding ID, Source, Section/Stage, Gap Type, Description. Covers both Stage 2 and Stage 3 gaps.
- **C-08: PASS** -- Stage 5: rationale for ALL findings.
- **C-09: PASS** -- Concrete HIGH remediation with specific examples.
- **C-10: PASS** -- INVENTORY GATE blocks Stage 2 call blocks AND Stage 3 registry entries until table complete.
- **C-11: PARTIAL** -- Each section is single-concern labeled. But C-11 requires "the reviewer can locate all content for any given concern without scanning elsewhere." Rate limit *content* (actual limit, burst, throttle response) lives entirely in Stage 3 -- Section E contains only registry confirmation. A reviewer reading a call block cannot find complete rate limit data without cross-referencing Stage 3. -2 pts.
- **C-12: PASS** -- Five-item checklist gates next block and trace completion.
- **C-13: PASS** -- Every section carries explicit exclusion statement within the section body. Section E: "Do not document the rate limit value here -- rate limit content belongs in Stage 3. Do not document authentication, format, error handling, or retry logic here."
- **C-14: PASS** -- Five items: A (Auth), B (Format), C (Error fate), D (Retry/Idempotency), E (Rate limit registry confirmed). Rate limit concern represented via registry-confirmation item. C-14 hypothesis confirmed: registry cross-reference satisfies five-concern scope.
- **C-15: PASS** -- "If a call is identified during Stage 2 or Stage 3 that is not in this table, add it here with the next available Call ID before writing its block or registry entry."

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 2 | 4 | 4 | 4 | 3 | **121** |

**Golden: YES** (all essential PASS; composite 121 >= 80)

**V-02 finding:** Hybrid registry achieves C-14 (cross-reference as fifth concern) but creates C-11 PARTIAL. Rate limit content is not locatable within a call block -- the reviewer must scan Stage 3. 2-point cost is the quantified trade-off for eliminating rate limit redundancy in fan-out call patterns.

---

### V-03 -- Minimal Gates + Phase 5 Split

**Design:** Phase-based structure. Phase 5 split into Phase 5a (Rate Limits) and Phase 5b (Retry/Idempotency). Concern exclusion at phase header level. Per-call completion checklist table at end of all analysis.

- **C-01: PASS** -- Phase 1 table; GATE 1 blocks Phase 2 until complete; LATE-CALL RULE.
- **C-02: PASS** -- Phase 2: auth mechanism, token expiry, credential rotation, security note, gap flag per call.
- **C-03: PASS** -- Phase 3: four separate labeled fields per call. GATE 3 rejects merged cells.
- **C-04: PASS** -- Phase 4: disposition, detail, gap flag. "A call that never fails is not a valid disposition."
- **C-05: PASS** -- Phase 5a: per-system rate limit table with limit, burst, throttle, gap flag.
- **C-06: PASS** -- Phase 5b: per-call retry/idempotency table with all columns.
- **C-07: PASS** -- GAP INVENTORY with Finding ID, Phase, Call ID/System, Gap Type, Description.
- **C-08: PASS** -- Severity table with rationale required for all.
- **C-09: PASS** -- Concrete remediations with backoff parameter examples.
- **C-10: PASS** -- GATE 1 before Phase 2. All subsequent phases reference Phase 1 Call IDs.
- **C-11: PASS** -- Phase 5a: "Concern: rate limit exposure only. Do not document authentication, request format, error handling, or retry logic in this phase." Phase 5b: "Concern: retry logic and idempotency only." The Phase 5 split is the minimum structural fix for R2's C-11 PARTIAL. All five concern phases single-concern.
- **C-12: PASS** -- PER-CALL COMPLETION CHECKLIST table (five columns: Ph 2 Auth, Ph 3 Format, Ph 4 Error, Ph 5a Rate, Ph 5b Idempotency). COMPLETION GATE: "GAP INVENTORY does not begin until every Call ID row shows Complete = YES."
- **C-13: FAIL** -- C-13 requires concern exclusion statements within each concern section inside a call block. V-03 is phase-based: exclusion statements appear at the phase header level (preamble for all calls in that phase). Per-call entries within a phase do not carry their own exclusion statements. C-13 pass condition explicitly states "a phase-level label alone does not pass." No call blocks exist in V-03. 0 pts.
- **C-14: FAIL** -- C-14 requires "A checklist with exactly five concern items appears in every call block; the checklist is explicitly tied to a gate condition that blocks the next call block." V-03's PER-CALL COMPLETION CHECKLIST is a summary table at the end of all analysis, not within each call block. There are no call blocks. The COMPLETION GATE blocks GAP INVENTORY, not the next call block. 0 pts.
- **C-15: PASS** -- "Any call identified during Phases 2--5b that is not in this table must be added here with the next available Call ID before its phase entry is written."

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 0 | 0 | 3 | **115** |

**Golden: YES** (all essential PASS; composite 115 >= 80)

**V-03 finding:** Phase 5 split resolves C-11 entirely (R2 open Q2 answered). But phase-based architecture cannot satisfy C-13 or C-14 regardless of how finely phases are subdivided. Per-call block architecture is a hard prerequisite for both criteria.

---

### V-04 -- Imperative Register + 5-Concern CALL COMPLETE

**Design:** Steps 0--7 with imperative phrasing. Steps 1--3 process per-call sequentially (one concern per step). CALL COMPLETE marker per INT-NN after Steps 1--3 with boxes 4--5 filled post-Steps 4--5. Steps 4--5 are cross-call tables.

- **C-01: PASS** -- Step 0 gate; LATE-CALL RULE with stop/add/return procedure.
- **C-02: PASS** -- Step 1 per-call: auth mechanism, token expiry, credential rotation, gap flag. "Do not write 'presumably uses auth' without naming the mechanism."
- **C-03: PASS** -- Step 2 per-call: four separate labeled lines. "Do not compress these four fields into one line."
- **C-04: PASS** -- Step 3 per-call: disposition, detail, gap flag. "A call that 'never fails' still requires a disposition."
- **C-05: PASS** -- Step 4: per-system rate limit table. Undocumented limits = RATE-EXPOSURE gap.
- **C-06: PASS** -- Step 5: per-call retry/idempotency table with strategy, max attempts, jitter, idempotency, mitigation, gap flag.
- **C-07: PASS** -- Step 6: named gap list with INT-NN references and gap-type taxonomy.
- **C-08: PASS** -- Step 7: rationale for all findings; exact remediation examples.
- **C-09: PASS** -- Concrete remediations with named headers and exact backoff parameters.
- **C-10: PASS** -- Step 0 complete before Step 1. LATE-CALL RULE defers discovered calls.
- **C-11: PASS** -- Each step: "Step N concern: X only. Do not document Y, Z, A, B in this step." Steps 1--5 each single-concern. The separate Steps 4 and 5 resolve R2's Phase 5 mixing.
- **C-12: PASS** -- CALL COMPLETE marker per INT-NN with five boxes. "Do not begin Step 6 until every INT-NN CALL COMPLETE marker has all five boxes checked."
- **C-13: FAIL** -- Steps 1--5 each process all calls within that step. Concern exclusion statements are at the step header level -- preambles for all calls in the step. Per-call entries ("For **INT-NN**: - Auth mechanism:...") do not carry individual exclusion statements. No call blocks exist -- there is no per-call structural unit within which per-section exclusions can appear. "A phase-level label alone does not pass." 0 pts.
- **C-14: PARTIAL** -- CALL COMPLETE marker has exactly five items covering all five concerns. But: (1) no call blocks exist; (2) gate fires after boxes 1--3 are checked ("Do not process the NEXT INT-NN's Steps 1--3 until the current INT-NN has the first three boxes checked"), but boxes 4--5 are filled only after global Steps 4--5 complete. When writing INT-02's Steps 1--3, INT-01's five-concern gate is structurally incomplete. The gate does not block the next call's processing until all five concerns are satisfied. 2 pts.
- **C-15: PASS** -- "If you discover a call during Steps 1--5 that is not in Step 0, stop, add it here with the next Call ID, and then return to the step where you found it."

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 0 | 2 | 3 | **117** |

**Golden: YES** (all essential PASS; composite 117 >= 80)

**V-04 finding (R2 Open Q3 answered):** Expanding CALL COMPLETE from 3 to 5 concerns achieves C-12 PASS. It does NOT lift to ceiling. C-13 FAIL (step-level exclusions are preambles) and C-14 PARTIAL (gate fires before boxes 4--5 are checkable, no call blocks) together cost 6 points -- more than the 4 originally hypothesized.

---

### V-05 -- Maximally Explicit C-13/C-14/C-15

**Design:** V-05 R2's per-call block structure with "You MUST NOT" exclusion statements, named LATE-CALL RULE box with no-exception language, and five-concern checklist explicitly gating both the next block and trace completion.

- **C-01: PASS** -- Stage 1 table; INVENTORY GATE; LATE-CALL RULE named box. UNKNOWN-SYSTEM entries. "No per-call analysis of any kind appears in Stage 1."
- **C-02: PASS** -- Section A: auth mechanism, token expiry, credential rotation, security note, gap flag.
- **C-03: PASS** -- Section B: four separate labeled lines. "A merged cell that combines method, headers, body, and response is not acceptable."
- **C-04: PASS** -- Section C: disposition, transformation detail, gap flag. "'This call never fails' is not a valid disposition."
- **C-05: PASS** -- Section D per call: documented limit, burst risk, throttle response, gap flag. "Absence of documented rate limits is itself a gap."
- **C-06: PASS** -- Section E: retry strategy, parameters, max attempts, idempotency guarantee, mitigation, gap flag.
- **C-07: PASS** -- Stage 3: Finding ID, Call ID, Section, Gap Type, Description. At-minimum requirements.
- **C-08: PASS** -- "ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale. Rationale is not optional for any row, including LOW findings."
- **C-09: PASS** -- Three concrete example formats: exact header, exact backoff parameters, specific flow replacement. Generic advice explicitly excluded.
- **C-10: PASS** -- INVENTORY GATE + LATE-CALL RULE named box. Strictest inventory-first enforcement.
- **C-11: PASS** -- "**Concern: X only.**\n**You MUST NOT document Y, Z, A, B in this section.**" in every section. Five sections, five distinct concerns, no mixing.
- **C-12: PASS** -- "This checklist gates two things: (1) the next call block -- do not open it until all five boxes are checked; (2) trace completion -- the trace is not complete until every Call ID from Stage 1 has a call block with all five boxes checked here."
- **C-13: PASS** -- "**You MUST NOT document [other four concerns] in this section.**" appears within every section in every call block. "**Concern: X only.**" is the single-concern declaration. All four excluded concerns named per section. Not preamble-only.
- **C-14: PASS** -- Exactly five items (A--E). Dual gate: next block AND trace completion. "do not open it" + "the trace is not complete until."
- **C-15: PASS** -- Named LATE-CALL RULE box, numbered 3-step procedure. "There are no exceptions -- a call discovered on the last block is subject to the same rule as a call discovered on the first."

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | **123** |

**Golden: YES** (all essential PASS; composite 123/123)

---

## Why V-01 and V-05 Tie at Ceiling

V-01 is structurally identical to V-05. The expert persona prepended before Stage 1 is a role declaration -- it does not precede the inventory and does not violate C-10. "Do not" vs "You MUST NOT" is aesthetic: both satisfy C-13's pass condition identically. The expert persona is additive: enriches C-01 inventory richness and C-02 delegation chain depth without trading any structural guarantee.

---

## C-13/C-14 Analysis: The Per-Call Block Boundary

The defining R3 finding: C-13 and C-14 require the per-call block architecture. Phase-based and step-based structures cannot satisfy them.

| Variation | Architecture | C-13 | C-14 | Gap |
|-----------|-------------|------|------|-----|
| V-01 | Per-call blocks | PASS (4) | PASS (4) | 0 |
| V-02 | Per-call blocks | PASS (4) | PASS (4) | 0 |
| V-03 | Phase-based | FAIL (0) | FAIL (0) | 8 |
| V-04 | Step-based | FAIL (0) | PARTIAL (2) | 6 |
| V-05 | Per-call blocks | PASS (4) | PASS (4) | 0 |

**Root cause for V-03/V-04 failures:** C-13 requires the exclusion statement to appear within the concern section itself, inside a per-call block. Phase headers and step headers are preambles for all calls in that phase/step -- not per-call-section exclusions. C-14 requires the five-concern checklist to appear within each call block and gate the next block. Neither V-03 nor V-04 has call blocks as a structural unit. V-04's CALL COMPLETE marker cannot be fully checked at the time the next call's early steps begin (boxes 4--5 require global steps 4--5 to complete first).

**Minimum change to ceiling from V-03/V-04:** Adopt the per-call block wrapper containing all five concern sections with individual concern exclusions. Phase-level or step-level restructuring alone cannot close the C-13/C-14 gap.

---

## Excellence Signals (R3)

**New in R3:**

**Expert persona as zero-cost inventory enrichment** -- Declaring a domain expert role before Stage 1 enriches call discovery (forgotten call categories: health checks, token acquisition, webhooks; "assumed to work" reframed as gap category) and auth depth (delegation chain, token expiry flagged proactively) without altering structural guarantees. Additive with any per-call block template at zero scoring cost. Prepend the persona, keep the structure intact, score ceiling.

**Registry cross-reference passes C-14 at cost of C-11 PARTIAL** -- V-02 confirms that a registry-confirmation item satisfies five-concern checklist scope (C-14 PASS). Moving rate limit content out of the call block creates a "scanning elsewhere" violation (C-11 PARTIAL, -2 pts). The trade-off is quantified: useful when per-system rate limit consolidation is worth more than 2 rubric points; not useful when C-11 completeness is required.

**Confirmed from R2 (structural prerequisites for C-13/C-14):**
- Per-call block architecture is the hard prerequisite for C-13 and C-14. Phase splits and step-per-concern structures achieve C-11 but cannot satisfy C-13 or C-14.
- "You MUST NOT" vs "Do not" makes no difference to rubric score. Imperative strength is aesthetic, not structural.

---

## Open Questions for R4

1. **V-01 semantic enrichment unmeasured:** V-01 and V-05 tie at 123 on the structural rubric, but the expert persona likely produces richer C-01 inventories and deeper C-02 analysis. A semantic quality rubric for call discovery richness and auth depth would differentiate them.

2. **V-02 hybrid registry at ceiling minus 2:** Can the C-11 PARTIAL be resolved while preserving the rate limit registry? One path: add a rate-limit summary field within Section D of each call block ("Rate limit: see Stage 3 / [System] / [limit value]"), making complete rate limit data accessible within the call block without duplicating the full registry row.

3. **V-03/V-04 per-call block adoption:** Does adding a call block wrapper (CALL BLOCK: INT-NN with all five sections) to an otherwise phase-based or step-based structure score ceiling?

```json
{"top_score": 123, "all_essential_pass": true, "new_patterns": ["expert-persona-zero-cost-enrichment: declaring a domain expert role before Stage 1 enriches call discovery (forgotten calls, assumed-to-work entries) and auth depth (delegation chains) without altering structural guarantees -- additive with any per-call block template at zero scoring cost", "registry-cross-reference-C14-pass-C11-partial: a rate limit registry-confirmation item satisfies five-concern checklist scope (C-14 PASS) but moving rate limit content out of the call block creates a scanning-elsewhere violation (C-11 PARTIAL, -2 pts) -- quantified trade-off between fan-out redundancy elimination and per-call completeness"]}
```
