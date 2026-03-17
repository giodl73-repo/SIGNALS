Scorecard written to `simulations/quest/scorecards/flow-integration-scorecard-R1-2026-03-14.md`.

---

**Round 1 Results — flow-integration**

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-04 Gated Phase Lifecycle | **100** | YES |
| 1 | V-01 Per-Call Table | **100** | YES |
| 3 | V-02 Sequential Domain Experts | **95** | YES |
| 4 | V-05 Table + Happy Path Column | **93** | NO |
| 5 | V-03 Imperative Register | **81** | YES (barely) |

**4 of 5 golden.**

**Key finding:** V-05 fails golden on C-03. The "Request / Response" combined column — compressing method + headers + body + response into a single table cell — is the structural trade-off that the happy-path framing doesn't compensate for. V-05's HAPPY PATH GAP SUMMARY is its standout contribution to C-07, but a single-column for C-03 is too compressed.

**Predicted candidate confirmed:** V-04 tied for the top. Gated phase lifecycle with single-concern isolation produces the strongest structural guarantees.

**Surprise:** V-01 (the control) ties V-04 at 100. Pre-printed sections with mandatory coverage are sufficient for this rubric — the within-100 differentiation is call-undercounting risk, which the rubric doesn't deduct for directly.

**New patterns from V-04:**
1. Inventory-first phase gate — inventory completes before any analysis begins
2. Single-concern phase isolation — each phase is forbidden from covering any other concern
3. Gate-enforced completion per call — the gate is a completion condition, not a suggestion

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inventory-first phase gate: dedicate a full phase to call enumeration before any per-call analysis begins", "single-concern phase isolation: each phase is permitted exactly one concern; cross-concern bleeding is structurally impossible", "gate-enforced completion per call: gate fires only when the one concern is complete for every call in the inventory"]}
```
ctions.
- C-03: PASS -- Dedicated REQUEST AND RESPONSE FORMAT section; "One entry per Call ID. Do not omit any call." Partial schemas acceptable.
- C-04: PASS -- Fixed "Error disposition" column; "Do not write 'handles errors' without a disposition type" explicitly stated.
- C-05: PASS -- Pre-printed RATE LIMIT EXPOSURE table; "No -- exposure rows are findings for GAP INVENTORY."
- C-06: PASS -- Pre-printed RETRY AND IDEMPOTENCY table with all columns including jitter and mitigation-if-not.
- C-07: PASS -- Pre-printed GAP INVENTORY; minimum requirements enumerate every mandatory finding category.
- C-08: PASS -- SEVERITY AND REMEDIATION table; ordering stated (HIGH first).
- C-09: PASS -- "Remediation (HIGH only)" column; three concrete call-context examples in template.

**V-02 -- Sequential Domain Experts**
- C-01: PASS -- Pass 1 builds definitive call inventory; explicit call types listed; gate before Pass 2 fires.
- C-02: PASS -- Pass 1 auth + Pass 3 Security Engineer full auth audit (token expiry, delegation chain, rotation policy). Dual coverage -- strongest C-02 treatment of all five variations.
- C-03: PASS -- Pass 1 REQUEST AND RESPONSE FORMAT section per call ID; partial schemas acceptable.
- C-04: PASS -- Pass 2 Reliability Engineer reviews every Call ID from Pass 1 for error fate; gate fires when every call has an error disposition.
- C-05: PASS -- Pass 2 per-call rate limit; "Not documented -- exposure" format present.
- C-06: PASS -- Pass 2 per-call retry strategy + idempotency; "flag as GAP" instructions.
- C-07: PARTIAL -- Unified GAP INVENTORY collects from all passes (correct), but Pass 3 Security Engineer's "Security Gap Summary" is a separate structured table that precedes the unified collection. Split collection risk: findings may appear in Security Gap Summary but not be carried forward to GAP INVENTORY. Pass condition technically met but structural split creates completeness risk.
- C-08: PASS -- SEVERITY AND REMEDIATION with ordering; HIGH/MEDIUM/LOW.
- C-09: PASS -- HIGH-specific remediation; "specific, call-context fix. Not generic advice."

**V-03 -- Imperative Register**
- C-01: PASS -- Step 0 call-list gate; "Do not begin Step 1 until every call is listed"; call type enumeration present. No table structure increases undercounting risk vs. inventory-first designs, but imperative is explicit.
- C-02: PASS -- Step 1 "Name the auth"; labeled mechanisms; "Do not write 'authenticated' without a mechanism"; token expiry handling instruction included.
- C-03: PASS -- Step 2 "State the request and response shape"; method, headers, body fields, response all required; "Do not write 'sends a request' without stating what is in it."
- C-04: PASS -- Step 3 "State the error fate"; enumerated dispositions; Swallowed and No handling flagged as explicit gaps; "Do not skip this step."
- C-05: PARTIAL -- Step 4 covers rate limits but merged with idempotency in a single step; no pre-printed table; "If not documented: say so" instruction present but structural enforcement weaker than all other variations.
- C-06: PARTIAL -- Step 4 covers idempotency but merged with rate limits; risk that rate limit dominates Step 4 output and idempotency is compressed. No pre-printed idempotency table.
- C-07: PARTIAL -- Findings collected in bulleted list format, not structured table; no pre-printed minimum requirements beyond instruction to "list every gap flagged in Steps 1--4." Gap type taxonomy enumerated in template but less enforced.
- C-08: PARTIAL -- "Rank by severity" instruction present but only HIGH findings have a rationale prompt ("Why HIGH:"). MEDIUM and LOW findings have no rationale structure. Rubric pass condition requires rationale for each finding.
- C-09: PARTIAL -- HIGH findings require "a concrete fix" with "specific action for this call -- not generic advice"; present but no pre-printed column, no specificity examples to anchor quality.

**V-04 -- Gated Phase Lifecycle**
- C-01: PASS -- Phase 1 is inventory-only; explicit gate before any analysis fires; table format with system/protocol/type; "minimum two rows required"; includes "assumed to work" and unknown system calls. Strongest C-01 guarantee -- inventory cannot bleed into analysis.
- C-02: PASS -- Phase 2 dedicated entirely to auth; "Every call must have an explicit entry"; token expiry handling and credential rotation per call; gate fires when all entries are present.
- C-03: PASS -- Phase 3 dedicated entirely to format; "Omission is not acceptable"; gate fires when every call has method, headers, body, and response summary. No other content allowed in this phase.
- C-04: PASS -- Phase 4 dedicated solely to error-disposition; "no other concern allowed in that phase"; gate fires when every call has an error-fate statement; "A call that 'never fails' still requires a disposition." Strongest structural guarantee for C-04 of all five variations.
- C-05: PASS -- Phase 5 dedicated to rate limits and idempotency; per-system rate limit entries; burst behavior, throttle response, and integration handling all documented.
- C-06: PASS -- Phase 5 per-call idempotency; "Idempotent by design?" + "Mitigation" fields; gate fires when all systems have rate limit entries and all non-read calls have idempotency assessments.
- C-07: PASS -- GAP INVENTORY after Phase 5; minimum requirements explicit: every "Unknown" auth (Phase 2), every "Swallowed" or "No handling" (Phase 4), every "Not documented" rate limit, every non-idempotent call without mitigation. Phase-sourced findings are traceable.
- C-08: PASS -- SEVERITY AND REMEDIATION with HIGH/MEDIUM/LOW and ordering. Gap flags feed naturally into severity from per-phase gate detail.
- C-09: PASS -- HIGH-specific remediation with the most specific call-context examples of all variations: exact header names, exact backoff parameters ("initial=500ms, factor=2, max=30s, jitter=uniform(0, 500ms)"), specific flow replacement.

**V-05 -- Table + Happy Path Column**
- C-01: PASS -- Same base as V-01; table rows with Call ID, system + protocol; "minimum two rows"; includes success-path-only calls. Moderate undercounting risk -- call list is self-generated.
- C-02: PASS -- Fixed "Auth mechanism" column; "Unknown -- gap" label required.
- C-03: PARTIAL -- "Request / Response" is a single combined column rather than a dedicated section. Column instructions cover method, headers, body, and response, but fitting all four in a single markdown table cell compresses documentation under a real integration. Rubric minimum will likely be met but schema completeness is at greater risk from cell compression than V-01 (dedicated section) or V-04 (dedicated phase).
- C-04: PASS -- Fixed "Error disposition" column + "Happy path only?" column -- dual flagging is the strongest C-04 surface of all table-format variations. Both columns independently flag swallowed errors.
- C-05: PASS -- RATE LIMITS AND IDEMPOTENCY section; "Happy path risk" column surfaces rate limit exposure at sustained volume.
- C-06: PASS -- Idempotency section with "Happy path risk" column; "None -- gap" mitigation format.
- C-07: PASS -- HAPPY PATH GAP SUMMARY pre-collects all "Yes -- gap" and "Partial -- gap" rows before the GAP INVENTORY. Two-stage collection means hardening gaps cannot be omitted. Strongest C-07 completeness guarantee of all table-format variations.
- C-08: PASS -- SEVERITY AND REMEDIATION with ordering; "Happy path exposure summary" quantifies the collective gap as N/M calls unhardened -- a format no other variation pre-prints.
- C-09: PASS -- HIGH-specific remediation with "specific, call-context fix. Not generic advice." Three examples provided.

---

### Composite Scores

**Point mapping:** PASS = full points, PARTIAL = half points, FAIL = 0.

| Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-02 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-03 | 15 | 15 | 15 | 15 | 15 | 8 |
| C-04 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-05 | 10 | 10 | 10 | 5 | 10 | 10 |
| C-06 | 10 | 10 | 10 | 5 | 10 | 10 |
| C-07 | 10 | 10 | 5 | 5 | 10 | 10 |
| C-08 | 5 | 5 | 5 | 3 | 5 | 5 |
| C-09 | 5 | 5 | 5 | 3 | 5 | 5 |
| **Total** | **100** | **100** | **95** | **81** | **100** | **93** |
| All essential PASS? | -- | YES | YES | YES | YES | NO (C-03 PARTIAL) |
| **GOLDEN?** | -- | **YES** | **YES** | **YES** | **YES** | **NO** |

---

### Ranking

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | **V-04** Gated Phase Lifecycle | **100** | YES |
| 1 | **V-01** Per-Call Table | **100** | YES |
| 3 | **V-02** Sequential Domain Experts | **95** | YES |
| 4 | **V-05** Table + Happy Path Column | **93** | NO (C-03 PARTIAL) |
| 5 | **V-03** Imperative Register | **81** | YES (barely) |

**Top score: 100** (V-04 and V-01 tied)
**All essential PASS in top variation: YES**

---

### Surprise Findings

**V-05 fails golden** despite being predicted as a strong golden candidate. The combined "Request / Response" column is the specific failure point -- compressing method + headers + body + response into a single markdown table cell is a structural trade-off that the happy-path inertia framing does not compensate for. V-05's HAPPY PATH GAP SUMMARY is its strongest feature (C-07), but C-03 PARTIAL disqualifies it from golden status.

**V-01 ties V-04 at 100** -- the control variation reaches the top score without gating, phasing, or role sequence. This validates that pre-printed sections with mandatory coverage are sufficient for this rubric. The within-100 differentiation is call-undercounting risk: V-04's inventory-first Phase 1 gate is structurally stronger at runtime, but the rubric does not deduct for risk -- only for missing coverage.

**V-03 is barely golden at 81** -- the imperative register alone clears the threshold but provides no margin. All five recommended and aspirational criteria land at PARTIAL, confirming the design hypothesis: register alone produces floor coverage, not depth.

---

### Excellence Signals from V-04

Three patterns from V-04 that drove its ceiling score:

1. **Inventory-first phase gate** -- Phase 1 dedicates an entire pass to call enumeration before any per-call analysis fires. This structurally prevents the most common failure mode: the call that is "obvious background" and gets analyzed without being inventoried. No other variation forces inventory to complete before analysis begins.

2. **Single-concern phase isolation** -- Each phase is permitted exactly one concern (auth, format, error fate, rate limits). Cross-concern bleeding -- where error handling is partially documented during format documentation -- is structurally impossible. The phase gate fires only when its one concern is complete for all calls.

3. **Gate-enforced completion per call** -- Each phase gate is a completion condition ("Every call has an error-fate statement. All 'Swallowed' entries are flagged"), not a coverage suggestion. The gate fires only when the one concern is complete for every call in the inventory.

---

### Open Questions for R2

1. V-05's C-03 failure is structural -- can a dedicated "Request and Response" subsection below the main table preserve the happy-path column's inertia value while fixing C-03 compression? Would that variation reach golden?
2. Does V-03's 81 hold under actual execution, or does the imperative register produce tighter but complete output that clears 90?
3. V-02's Security Engineer pass produces auth depth (token expiry, delegation chain, rotation) that no other variation captures. Does this translate to higher C-02 quality in practice, or is the finding split between Security Gap Summary and GAP INVENTORY a real problem?
