---

## Round 2 Results — flow-integration

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | **V-05** Per-Call Gate Blocks | **112** | YES |
| 2 | **V-01** Repaired V-05 | **110** | YES |
| 2 | **V-02** Minimal Gated Phases | **110** | YES |
| 2 | **V-04** Embedded Security | **110** | YES |
| 5 | **V-03** Imperative Upgraded | **108** | YES |

**5 of 5 golden** — first round where every variation clears golden.

---

## Score Breakdown

| Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 Call inventory | 15 | 15 | 15 | 15 | 15 | 15 |
| C-02 Auth documentation | 15 | 15 | 15 | 15 | 15 | 15 |
| C-03 Request/response format | 15 | 15 | 15 | 15 | 15 | 15 |
| C-04 Error propagation | 15 | 15 | 15 | 15 | 15 | 15 |
| C-05 Rate limits | 10 | 10 | 10 | 10 | 10 | 10 |
| C-06 Retry/idempotency | 10 | 10 | 10 | 10 | 10 | 10 |
| C-07 Gap inventory | 10 | 10 | 10 | 10 | 10 | 10 |
| C-08 Severity ranking | 5 | 5 | 5 | 5 | 5 | 5 |
| C-09 Remediation sketch | 5 | 5 | 5 | 5 | 5 | 5 |
| C-10 Inventory-first gate | 4 | 4 | 4 | 4 | 4 | 4 |
| C-11 Single-concern isolation | 4 | **2** | **2** | **2** | **2** | **4** |
| C-12 Gate-enforced completion | 4 | 4 | 4 | **2** | 4 | 4 |
| **Total** | **112** | **110** | **110** | **108** | **110** | **112** |

---

## Why V-05 Wins

C-11 is the 110 ceiling. V-01, V-02, and V-04 all get PARTIAL because:
- **V-01**: CALL INVENTORY table mixes enumeration + auth + error disposition in one section
- **V-02 / V-04**: Phase 5 header names two concerns ("RATE LIMITS AND IDEMPOTENCY")

V-05 fixes this by moving from phase-level to within-call section-level isolation. Each of the five sections (A-E) carries an explicit exclusion statement: `"Concern: authentication only. Do not document format, error handling, or rate limits here."` Rate limits (Section D) and retry/idempotency (Section E) are in separate sections.

V-03 gets C-12 PARTIAL because the CALL COMPLETE marker covers only 3/5 concerns — no completion signal for rate limits or idempotency.

---

## Excellence Signals (new in R2)

1. **Per-call section-level concern exclusion** — each section carries its own `"Concern: X only. Do not document Y here."` statement, making C-11 violations structurally impossible rather than convention-dependent.

2. **Five-concern per-call completion checklist** — covers all five integration concerns within each call block; gates the next block and trace completion. C-12 at all-five-concern scope, not 3-of-5.

3. **Inventory GATE with late-call discipline** — calls discovered during Stage 2 must be added to the inventory table before their block is written, extending the inventory-first guarantee to runtime completeness.

```json
{"top_score": 112, "all_essential_pass": true, "new_patterns": ["per-call section-level concern exclusion: each concern section carries its own 'Concern: X only. Do not document Y here.' exclusion statement -- makes C-11 violations structurally impossible at the section level rather than relying on phase-level convention", "five-concern per-call completion checklist: a named checklist covering all five integration concerns within each call block gates the next block and trace completion -- directly instantiates C-12 at all-concern scope, not 3-of-5 scope", "inventory GATE with late-call discipline: calls discovered during per-call analysis must be added to the inventory table before their block is written -- extends inventory-first guarantee from initial enumeration to runtime completeness"]}
```
- GAP INVENTORY with HAPPY PATH GAP SUMMARY pre-collection step; at-minimum requirements enumerate every mandatory finding category; call-ID and gap-type references.
- **C-08: PASS** -- "ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale." Explicit in table instructions.
- **C-09: PASS** -- Remediation column with HIGH-specific concrete examples (header names, backoff parameters, identity flow replacement).
- **C-10: PASS** -- "Complete this table before writing any per-call subsections below" + "Do not write per-call subsections below until this table has a row for every call." Inventory gate is explicit.
- **C-11: PARTIAL** -- CALL INVENTORY section mixes call enumeration (C-01 concern), auth mechanism (C-02), and error disposition (C-04) in a single table. Section cannot be labeled with exactly one concern. All other sections are single-concern.
- **C-12: PASS** -- REQUEST AND RESPONSE FORMAT says "Repeat for each Call ID. Omission is not acceptable." Matches the rubric's explicit all-calls-covered pass condition.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 2 | 4 | **110** |

**Golden: YES** (all essential PASS; composite 110 >= 80)

---

### V-02 -- Lifecycle: Minimal Gated Phases

**Design:** Five phases, each with a single gate condition and one pre-printed example row. No instructional prose -- enforcement carried entirely by gate statement text.

- **C-01: PASS** -- Phase 1 inventory with GATE 1 explicit; "No per-call analysis of any kind appears in Phase 1." Named system, protocol, call type columns. Unknown system entries. Minimum two rows.
- **C-02: PASS** -- Phase 2 dedicated to auth; full auth type set per call; token expiry and credential rotation columns; GATE 2 fires when every Call ID has an entry.
- **C-03: PASS** -- Phase 3 dedicated to format; four separate labeled fields per call; GATE 3 explicitly: "A single merged 'Request / Response' field does not fire this gate."
- **C-04: PASS** -- Phase 4 dedicated to error fate; every call requires a disposition entry; "Swallowed" and "No handling" require explicit gap flags; GATE 4.
- **C-05: PASS** -- Phase 5 rate limit table per system with limit, burst behavior, throttle response; "No -- exposure" rows are gap findings.
- **C-06: PASS** -- Phase 5 retry/idempotency table per call; "None -- gap" mitigation format; non-idempotent write calls without mitigation are findings.
- **C-07: PASS** -- GAP INVENTORY collects from Phases 2, 4, and 5 with Phase source column; at-minimum requirements explicit; call-ID and gap-type references.
- **C-08: PASS** -- "ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale." Explicit with severity order instruction.
- **C-09: PASS** -- HIGH-specific remediation with concrete examples (backoff parameters, idempotency key format, identity flow replacement).
- **C-10: PASS** -- GATE 1 fires before Phase 2 begins. "Phase 2 does not begin until this gate fires." No analysis in Phase 1.
- **C-11: PARTIAL** -- Phase 5 is labeled "PHASE 5: RATE LIMITS AND IDEMPOTENCY" -- two concerns in one named phase. Sub-sections (Rate Limits and Retry and Idempotency) are present but share a phase header. Pass condition requires each named section to address exactly one concern.
- **C-12: PASS** -- Each gate condition: "Phase N is complete when every Call ID from Phase 1 has X." E.g., GATE 2: "complete when every Call ID from Phase 1 has an auth mechanism entry." Explicit all-calls-covered completion condition.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 2 | 4 | **110** |

**Golden: YES** (all essential PASS; composite 110 >= 80)

**Verbosity hypothesis confirmed:** V-02 and V-04 score identically (110). Gate conditions alone carry the structural guarantees. V-04's verbose phase descriptions are aesthetic, not structural.

---

### V-03 -- Phrasing Register: Imperative Upgraded

**Design:** Step 0 (call list) -> Steps 1-3 (per-call auth/format/error with CALL COMPLETE marker) -> Step 4 (rate limits table) -> Step 5 (idempotency table) -> Step 6 (gap inventory) -> Step 7 (severity/remediation).

- **C-01: PASS** -- Step 0 call-list gate; "Do not begin Step 1 until every call is listed"; inclusive enumeration instructions; minimum two entries; INT-NN IDs.
- **C-02: PASS** -- Step 1 per-call auth with specific mechanism types, token expiry, credential rotation; "Do not write 'presumably uses auth' without a mechanism."
- **C-03: PASS** -- Step 2 four separate labeled lines; "Do not compress them." All four fields required per call.
- **C-04: PASS** -- Step 3 per-call error fate with explicit types and gap flag; "A call that 'never fails' still requires a disposition."
- **C-05: PASS** -- Step 4 pre-printed rate limit table per system with limit, burst, throttle columns. (R1 PARTIAL repaired.)
- **C-06: PASS** -- Step 5 pre-printed retry/idempotency table per call with all columns. (R1 PARTIAL repaired.)
- **C-07: PASS** -- Step 6 collects all gaps with INT-NN references and gap type taxonomy; "Do not leave findings inline in the steps above." (R1 PARTIAL repaired.)
- **C-08: PASS** -- Step 7: "ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale." Explicit examples for MEDIUM and LOW. (R1 PARTIAL repaired.)
- **C-09: PASS** -- Step 7 HIGH-specific remediation with "specific, call-context" instruction. (R1 PARTIAL repaired.)
- **C-10: PASS** -- Step 0 explicitly precedes Step 1; "Do not begin Step 1 until every call is listed here"; subsequent steps reference INT-NN.
- **C-11: PARTIAL** -- Step 3 includes a CALL COMPLETE marker: "[ ] Auth (Step 1) [ ] Format (Step 2) [ ] Error fate (Step 3)". This marker tracks multi-concern completion within the error-fate section, causing Step 3 to address both error fate analysis and multi-concern completion tracking simultaneously. Steps 4 and 5 are separately single-concern.
- **C-12: PARTIAL** -- "Every INT-NN must reach CALL COMPLETE before Step 4 begins" is an explicit per-call completion enforcement, but CALL COMPLETE covers only 3/5 concerns (Auth, Format, Error fate). Rate limits (Step 4) and idempotency (Step 5) have no per-call completion condition. Incomplete scope.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 2 | 2 | **108** |

**Golden: YES** (all essential PASS; composite 108 >= 80)

**V-03 improvement vs. R1:** Jumped from 81 to 108. All five R1 PARTIALs are now PASS. Remaining gap: CALL COMPLETE covers 3/5 concerns; expanding to 5 is a one-line change.

---

### V-04 -- Role Sequence + Lifecycle: Security Embedded

**Design:** Phase 1 (Inventory) -> Phase 2 (Auth: Part A Architect + Part B Security Engineer) -> Phase 3 (Format) -> Phase 4 (Error Fate) -> Phase 5 (Rate Limits + Idempotency) -> GAP INVENTORY -> SEVERITY AND REMEDIATION.

- **C-01: PASS** -- Phase 1 inventory-only with GATE 1; "No per-call analysis of any kind appears in Phase 1." Named system, protocol, call type. Unknown system entries. Minimum two rows.
- **C-02: PASS** -- Phase 2 Part A documents auth per call; Part B Security Engineer audits for delegation chain risk, application identity recommendation, token expiry, credential rotation, missing auth. Strongest C-02 coverage of all five variations.
- **C-03: PASS** -- Phase 3 dedicated to format; four separate labeled lines; GATE 3 explicitly rejects "A single merged field."
- **C-04: PASS** -- Phase 4 dedicated to error fate; "A call that 'never fails' still requires a disposition"; gap flag mandatory for swallowed/no-handling entries.
- **C-05: PASS** -- Phase 5 rate limit table with Retry-After column; "No -- exposure" rows are gap findings.
- **C-06: PASS** -- Phase 5 retry/idempotency table with detailed backoff parameters (initial / factor / max / jitter).
- **C-07: PASS** -- Single GAP INVENTORY collects all phases; GAP-S-NN findings from Phase 2 Part B are renumbered into GAP-NN sequence; "No separate security table exists." Eliminates R1 V-02's split-finding risk.
- **C-08: PASS** -- "ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale. Rationale is mandatory for every row."
- **C-09: PASS** -- Most specific remediation examples of all variations: exact header format, exact backoff parameters, specific flow replacement.
- **C-10: PASS** -- GATE 1 before Phase 2. Phase 1 contains enumeration only.
- **C-11: PARTIAL** -- Phase 5 is labeled "PHASE 5: RATE LIMITS AND IDEMPOTENCY" -- two concerns in one named phase. Sub-sections are present but share the phase header. Same structural weakness as V-02.
- **C-12: PASS** -- Gate conditions: "complete when every Call ID from Phase 1 has X." GATE 3: "every Call ID from Phase 1 has method, key request headers, body key fields, and expected response documented." Explicit all-calls-covered completion condition.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 2 | 4 | **110** |

**Golden: YES** (all essential PASS; composite 110 >= 80)

---

### V-05 -- Output Format + Lifecycle: Per-Call Gate Blocks

**Design:** STAGE 1: Call Inventory (INVENTORY GATE) -> STAGE 2: Per-call analysis blocks (Sections A-E, each single-concern, each with named completion checklist) -> GAP INVENTORY -> SEVERITY AND REMEDIATION.

- **C-01: PASS** -- Stage 1 inventory table with INVENTORY GATE: "Stage 2 does not begin until this table has a row for every cross-system call." Inclusive enumeration instructions. Minimum two rows. Late-discovered calls must be added to inventory before block is written.
- **C-02: PASS** -- Section A per call covers auth mechanism, token expiry, credential rotation, security note. "Concern: authentication only."
- **C-03: PASS** -- Section B per call covers four separate labeled lines. "All four fields are required as separate labeled lines." No merged cell possible in block structure.
- **C-04: PASS** -- Section C per call covers error disposition and gap flag. "Concern: error disposition only."
- **C-05: PASS** -- Section D per call covers rate limit for the call's target system. Limit, burst, throttle, gap flag. "Concern: rate limit exposure for this call's target system only."
- **C-06: PASS** -- Section E per call covers retry strategy and idempotency. Strategy, jitter, idempotency, mitigation, gap flag. "Concern: retry logic and idempotency only."
- **C-07: PASS** -- GAP INVENTORY collects all gap flags from all blocks with Call ID + section letter references. Gap type taxonomy. At-minimum requirements enumerate every mandatory finding category.
- **C-08: PASS** -- "ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale. Rationale is not optional for any row." Explicit examples for all three severity levels.
- **C-09: PASS** -- HIGH-specific remediation with three concrete examples including idempotency key format, backoff parameters, and identity flow replacement.
- **C-10: PASS** -- INVENTORY GATE before Stage 2. "A call discovered during Stage 2 must be added to this table and assigned a Call ID before its block is written." Strictest inventory-first enforcement of all five variations.
- **C-11: PASS** -- Each section within a block carries its own concern label and exclusion statement: "Concern: authentication only. Do not document format, error handling, or rate limits here." Rate limits (Section D) and retry/idempotency (Section E) are in separate sections -- fixing V-02/V-04's Phase 5 mixing.
- **C-12: PASS** -- Per-call completion checklist covers all five concerns: "[ ] Section A (Auth) [ ] Section B (Format) [ ] Section C (Error fate) [ ] Section D (Rate limit) [ ] Section E (Retry/Idempotency)." "Do not begin the next block until this checklist is fully marked." "The trace is not complete until every Call ID from Stage 1 has a fully checked completion checklist."

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | **112** |

**Golden: YES** (all essential PASS; composite 112/112)

---

## Composite Scores

| Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-02 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-03 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-04 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-05 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-06 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-07 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-08 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-09 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-10 | 4 | 4 | 4 | 4 | 4 | 4 |
| C-11 | 4 | 2 | 2 | 2 | 2 | 4 |
| C-12 | 4 | 4 | 4 | 2 | 4 | 4 |
| **Total** | **112** | **110** | **110** | **108** | **110** | **112** |
| All essential PASS? | -- | YES | YES | YES | YES | YES |
| **GOLDEN?** | -- | **YES** | **YES** | **YES** | **YES** | **YES** |

---

## Ranking

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | **V-05** Per-Call Gate Blocks | **112** | YES |
| 2 | **V-01** Repaired V-05 | **110** | YES |
| 2 | **V-02** Minimal Gated Phases | **110** | YES |
| 2 | **V-04** Embedded Security | **110** | YES |
| 5 | **V-03** Imperative Upgraded | **108** | YES |

**Top score: 112** (V-05)
**All essential PASS in top variation: YES**
**All five golden.**

---

## C-11 Analysis: The 110 Ceiling

V-01, V-02, and V-04 all stall at C-11 PARTIAL (2/4 pts). Each fails for a different reason:

| Variation | C-11 failure mode |
|-----------|-------------------|
| V-01 | CALL INVENTORY table mixes call enumeration + auth + error disposition in one section |
| V-02 | Phase 5 header "RATE LIMITS AND IDEMPOTENCY" names two concerns in one phase |
| V-04 | Same as V-02: Phase 5 mixes two concerns despite sub-sections |

V-05 is the only variation that achieves C-11 PASS. Moving from section-level concern isolation to within-call section-level isolation is the fix. Each section carries an explicit exclusion statement. Rate limits (Section D) and retry/idempotency (Section E) are in separate sections, not a combined phase. Mixed-concern sections become structurally impossible.

---

## Excellence Signals from V-05

Three patterns from V-05 that produced the first perfect 112/112:

1. **Per-call section-level concern exclusion** -- Each section within a per-call block carries its own concern label and a "Do not document X here" exclusion statement. This makes C-11 violations structurally impossible at the section level, not just the phase level. The fix for V-02/V-04's Phase 5 mixing is splitting rate limits (Section D) and retry/idempotency (Section E) into distinct sections within the block.

2. **Five-concern per-call completion checklist** -- The completion checklist covers all five concerns (A through E) within each call block. "Do not begin the next block until this checklist is fully marked." This is gate-enforced per-call completion at all-five-concern scope. Prior designs had section-level gates (V-02, V-04) or 3-concern CALL COMPLETE markers (V-03).

3. **Inventory GATE with late-call discipline** -- "A call discovered during Stage 2 must be added to this table and assigned a Call ID before its block is written." This extends the inventory-first guarantee from initial enumeration to runtime completeness, preventing calls from appearing in blocks without inventory registration.

---

## Open Questions for R3

1. **V-05 per-call rate limit redundancy:** Section D is per-call, but rate limits are per-system. If three calls go to the same system, the rate limit entry repeats three times. Does this redundancy produce divergence in practice? A hybrid -- per-call blocks for auth/format/error, per-system table for rate limits -- may produce cleaner C-05 output without losing C-12.

2. **V-02 == V-04 at 110:** Verbosity hypothesis confirmed. Should R3 test a minimal-gates variation with Phase 5 split into Phase 5a (Rate Limits) and Phase 5b (Idempotency) to fix the C-11 PARTIAL without adopting V-05's full block structure?

3. **V-03 C-12 repair path:** Expanding CALL COMPLETE to five concerns ("[ ] Rate limits (Step 4) [ ] Idempotency (Step 5)") is a one-line addition. Would this single change lift V-03 from 108 to 110 or 112?

```json
{"top_score": 112, "all_essential_pass": true, "new_patterns": ["per-call section-level concern exclusion: each concern section carries its own 'Concern: X only. Do not document Y here.' exclusion statement -- makes C-11 violations structurally impossible at the section level rather than relying on phase-level convention", "five-concern per-call completion checklist: a named checklist covering all five integration concerns within each call block gates the next block and trace completion -- directly instantiates C-12 at all-concern scope, not 3-of-5 scope", "inventory GATE with late-call discipline: calls discovered during per-call analysis must be added to the inventory table before their block is written -- extends inventory-first guarantee from initial enumeration to runtime completeness"]}
```
