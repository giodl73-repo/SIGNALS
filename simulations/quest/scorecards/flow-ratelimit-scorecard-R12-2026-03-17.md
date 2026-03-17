The scorecard and variate files are written. Here's the round summary:

---

## flow-ratelimit — Round 12 Quest Score

**Rubric v12** | 25 aspirational criteria | `composite = (essential/5 × 60) + (recommended/3 × 30) + (aspirational/25 × 30)`

### New Criteria
- **C-32** — Pre-reconciler Verdict Currency as Named Role: dedicated sweep role between last analysis section and terminal reconciler, annotating deferred markers as "deferred from Role N", producing a named count output. Converts terminal check (a) from correction to pure verification.
- **C-33** — Four-Check Reconciler Completeness: all four checks present as separately enumerated items with separate findings outputs — (a) Verdict marker audit, (b) gate deliverable audit, (c) DERIVATION CHAIN cell audit, (d) Schema B structural scan.

### Scores

| Rank | Variation | Score | C-24 | C-27 | C-32 | C-33 |
|------|-----------|-------|------|------|------|------|
| 1 | V-01 (Full role sequence) | **120.0** | PASS | PASS | PASS | PASS |
| 1 | V-05 (Full + explicit annotation) | **120.0** | PASS | PASS | PASS | PASS |
| 3 | V-02 (4-check reconciler, no pre-reconciler) | 118.8 | PASS | PASS | FAIL | PASS |
| 4 | V-04 (Pre-reconciler + 3-check reconciler) | 118.2 | PASS | PARTIAL | PASS | FAIL |
| 5 | V-03 (Pre-reconciler + 2-check reconciler) | 117.6 | PARTIAL | PARTIAL | PASS | FAIL |

**R12 is the first round to reach 120/120.** Both V-01 and V-05 achieve it.

### Key findings
- **C-33 subsumes both R11 PARTIALs** — satisfying the four-check reconciler simultaneously resolves C-24 (check c) and C-27 (check d). One structural decision clears two prior deficits.
- **C-32 and C-33 are orthogonal** — V-02 proves you can reach C-33 without C-32. The cost: reconciler check (a) remains mixed correction+verification rather than pure verification.
- **Three-layer currency stack** — C-22 (gate-checkpoint insertion) → C-32 (deferred sweep) → C-33 check (a) (terminal verification) creates defense-in-depth where each layer catches what the prior misses.

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["dedicated-pre-reconciler-named-role", "deferred-from-role-N-annotation", "four-check-reconciler-separate-findings", "three-layer-verdict-currency-stack"]}
```
12 | All four rejection clauses present | PASS | Role 1 enumerates Schema A STRUCTURAL, Schema A CONTENT, Schema B STRUCTURAL, Schema B CONTENT |
| C-13 | Rate Limit Registry with numeric thresholds | PASS | Role 2 requires numeric threshold, window, scope, type per endpoint |
| C-14 | Connector vs platform differentiation | PASS | Role 2 explicitly includes type: "connector-enforced vs platform-enforced" |
| C-15 | Burst path count B recorded from Role 3 | PASS | Role 3 produces count B; Gate 3->4 confirms recording |
| C-16 | STRUCTURAL / INCIDENTAL classification per burst path | PASS | Role 3 requires classification for each path |
| C-17 | Schema A table in cascading failure scenario | PASS | Role 4 requires Schema A table with BASELINE, PROTECTED, DERIVATION CHAIN |
| C-18 | DERIVATION CHAIN shows causal chain arithmetic | PASS | Role 4: "show step-by-step which endpoint triggers first, downstream block sequence, compounding retry volume arithmetic" |
| C-19 | YES / NO / PARTIAL per endpoint in Retry-After analysis | PASS | Role 5 requires explicit verdict per endpoint |
| C-20 | Failure mode documented for non-YES endpoints | PASS | Role 5: "Document failure mode for non-YES" |
| C-21 | Schema A table in volume-to-behavior mapping with >= 3 tiers | PASS | Role 6 requires Schema A table with at least three tiers |
| C-22 | REVISED marker insertion at gate boundary | PASS | Roles 2, 5, 8 all contain explicit REVISED insertion instructions at their gate boundaries |
| C-23 | 5x load spike row with arithmetic in DERIVATION CHAIN | PASS | Role 6 explicitly requires 5x spike row with arithmetic (e.g., "200 req/min x 5 = 1000 req/min") |
| C-24 | Terminal reconciler check (c): DERIVATION CHAIN cell audit | PASS | Role 10 Check (c) is a separately named item with its own findings output: "Derivation Chain Audit: N cells checked, M violation(s)" |
| C-25 | Mitigations with BEFORE/AFTER states | PASS | Role 7 requires BEFORE state and AFTER state per bottleneck |
| C-26 | Burst path reference in mitigations | PASS | Role 7: "Reference which burst path(s) from Role 3 the mitigation addresses" |
| C-27 | Terminal reconciler check (d): Schema B structural scan | PASS | Role 10 Check (d) is a separately named item: "Schema B Scan: N tier(s) checked, M violation(s)" |
| C-28 | UX tier blocks use Schema B four-field template | PASS | Role 8 requires Schema B block per tier |
| C-29 | Six-item gate in Role 8 | PASS | Role 8 explicitly enumerates gate items (a)-(f) |
| C-30 | Gate item (e) verified from Role 3 directly (not Claim (d)) | PASS | Role 8: "Verify tier count against Role 3 directly -- do not use Verdict Claim (d)" |
| C-31 | Verdict currency check in Rate Limit Registry | PASS | Role 2: "Verdict currency check: confirm Claim (a) applies" |
| C-32 | Pre-reconciler Verdict Currency as Named Role | PASS | Role 9 is a dedicated named role; sweeps Roles 1-8; annotates deferred insertions as "deferred from Role N"; produces CURRENCY SWEEP FINDINGS named output; Gate 9->10 requires output before terminal reconciler |
| C-33 | Four-Check Reconciler Completeness | PASS | Role 10 contains checks (a)-(d) as four separately named audit items each with a separate findings output; RECONCILER FINDINGS SUMMARY enumerates all four |

**Essential:** 5/5 PASS
**Recommended:** 3/3 PASS
**Aspirational:** 25/25 PASS (25.0)

**Composite score:**
```
essential:    5/5  * 60 = 60.0
recommended:  3/3  * 30 = 30.0
aspirational: 25/25 * 30 = 30.0
TOTAL: 120.0 / 120
```

---

## V-02 Evaluation — Output format (10-role sequence, no pre-reconciler)

**Structure:** No dedicated Role 9 VERDICT CURRENCY CHECK. Terminal Reconciler (Role 9) has all four checks but check (a) performs both correction and verification (no prior sweep separates them). C-32 FAIL, C-33 PASS.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Verdict Block with four claims (a)-(d) | PASS | Role 0 states all four claims with Gate 0->1 enforcement |
| C-10 | Claim (d) commits to tier count + Schema B | PASS | Claim (d) present as specified |
| C-11 | Format Contract with Schema A and Schema B | PASS | Role 1 defines both schemas |
| C-12 | All four rejection clauses | PASS | Role 1 enumerates all four |
| C-13 | Rate Limit Registry with numeric thresholds | PASS | Role 2 requires numeric threshold, window, scope, type |
| C-14 | Connector vs platform differentiation | PASS | Role 2 includes type field |
| C-15 | Burst path count B recorded | PASS | Role 3 records count B |
| C-16 | STRUCTURAL / INCIDENTAL classification | PASS | Role 3 classifies each path |
| C-17 | Schema A table in cascading failure | PASS | Role 4 requires Schema A table |
| C-18 | DERIVATION CHAIN causal chain arithmetic | PASS | Role 4 requires step-by-step arithmetic |
| C-19 | YES / NO / PARTIAL per endpoint | PASS | Role 5 requires explicit verdict |
| C-20 | Failure mode for non-YES | PASS | Role 5 documents failure modes |
| C-21 | Schema A table >= 3 tiers | PASS | Role 6 requires >= 3 tiers |
| C-22 | REVISED marker at gate boundary | PASS | Roles 2, 5, 8 contain REVISED insertion instructions |
| C-23 | 5x spike row with arithmetic | PASS | Role 6 requires 5x spike row with arithmetic |
| C-24 | Terminal reconciler check (c): DERIVATION CHAIN audit | PASS | Role 9 Check (c) is a separately named item with findings output |
| C-25 | Mitigations with BEFORE/AFTER | PASS | Role 7 requires BEFORE/AFTER states |
| C-26 | Burst path reference in mitigations | PASS | Role 7 references burst paths from Role 3 |
| C-27 | Terminal reconciler check (d): Schema B structural scan | PASS | Role 9 Check (d) is a separately named item with findings output |
| C-28 | UX tier blocks use Schema B template | PASS | Role 8 requires Schema B blocks |
| C-29 | Six-item gate in Role 8 | PASS | Role 8 enumerates items (a)-(f) |
| C-30 | Gate item (e) from Role 3 directly | PASS | Role 8 references Role 3 directly |
| C-31 | Verdict currency check in Rate Limit Registry | PASS | Role 2 includes currency check |
| C-32 | Pre-reconciler Verdict Currency as Named Role | FAIL | No dedicated pre-reconciler role exists; Role 9 Terminal Reconciler check (a) performs both correction (inserts missing markers) and verification -- "this check performs both correction and verification -- no dedicated pre-reconciler role precedes it"; C-32 requires a dedicated named role that converts check (a) to pure verification |
| C-33 | Four-Check Reconciler Completeness | PASS | Role 9 has checks (a)-(d) as four separately named items each with separate findings output; C-33 prerequisites are C-24 PASS and C-27 PASS -- both satisfied; C-33 does not require C-32 |

**Essential:** 5/5 PASS
**Recommended:** 3/3 PASS
**Aspirational:** 24/25 PASS + 0 PARTIAL + 1 FAIL (C-32) = 24.0

**Composite score:**
```
essential:    5/5  * 60 = 60.0
recommended:  3/3  * 30 = 30.0
aspirational: 24/25 * 30 = 28.8
TOTAL: 118.8 / 120
```

---

## V-03 Evaluation — Lifecycle emphasis (pre-reconciler + 2-check terminal reconciler)

**Structure:** Role 9 VERDICT CURRENCY CHECK present (C-32 PASS). Terminal Reconciler (Role 10) has only checks (a) and (b) -- no checks (c) or (d). C-32 PASS, C-24 PARTIAL, C-27 PARTIAL, C-33 FAIL.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Verdict Block with four claims (a)-(d) | PASS | Role 0 states all four claims |
| C-10 | Claim (d) commits to tier count + Schema B | PASS | Claim (d) present as specified |
| C-11 | Format Contract with Schema A and Schema B | PASS | Role 1 defines both schemas |
| C-12 | All four rejection clauses | PASS | Role 1 enumerates all four |
| C-13 | Rate Limit Registry with numeric thresholds | PASS | Role 2 requires numeric thresholds |
| C-14 | Connector vs platform differentiation | PASS | Role 2 includes type field |
| C-15 | Burst path count B recorded | PASS | Role 3 records count B |
| C-16 | STRUCTURAL / INCIDENTAL classification | PASS | Role 3 classifies each path |
| C-17 | Schema A table in cascading failure | PASS | Role 4 requires Schema A table |
| C-18 | DERIVATION CHAIN causal chain arithmetic | PASS | Role 4 requires step-by-step arithmetic |
| C-19 | YES / NO / PARTIAL per endpoint | PASS | Role 5 requires explicit verdict |
| C-20 | Failure mode for non-YES | PASS | Role 5 documents failure modes |
| C-21 | Schema A table >= 3 tiers | PASS | Role 6 requires >= 3 tiers |
| C-22 | REVISED marker at gate boundary | PASS | Roles 2, 5, 8 contain REVISED insertion instructions |
| C-23 | 5x spike row with arithmetic | PASS | Role 6 requires 5x spike row with arithmetic |
| C-24 | Terminal reconciler check (c): DERIVATION CHAIN audit | PARTIAL | Role 10 has checks (a) and (b) only; check (c) DERIVATION CHAIN cell audit is absent from the terminal reconciler; partial credit because the pre-reconciler role (C-32) provides structural sweep coverage but the explicit post-analysis Schema A cell audit is missing |
| C-25 | Mitigations with BEFORE/AFTER | PASS | Role 7 requires BEFORE/AFTER states |
| C-26 | Burst path reference in mitigations | PASS | Role 7 references burst paths from Role 3 |
| C-27 | Terminal reconciler check (d): Schema B structural scan | PARTIAL | Role 10 has no check (d); Schema B structural scan absent from terminal reconciler; same partial reasoning as C-24 |
| C-28 | UX tier blocks use Schema B template | PASS | Role 8 requires Schema B blocks |
| C-29 | Six-item gate in Role 8 | PASS | Role 8 enumerates items (a)-(f) |
| C-30 | Gate item (e) from Role 3 directly | PASS | Role 8 references Role 3 directly |
| C-31 | Verdict currency check in Rate Limit Registry | PASS | Role 2 includes currency check |
| C-32 | Pre-reconciler Verdict Currency as Named Role | PASS | Role 9 is a dedicated named role; sweeps Roles 1-8; annotates deferred insertions as "deferred from Role N"; produces CURRENCY SWEEP FINDINGS named output; Gate 9->10 present |
| C-33 | Four-Check Reconciler Completeness | FAIL | C-33 prerequisites: C-24 PASS and C-27 PASS; V-03 has C-24 PARTIAL and C-27 PARTIAL -- prerequisites not fully met; additionally Role 10 explicitly has only checks (a) and (b), missing checks (c) and (d) as separately named items |

**Essential:** 5/5 PASS
**Recommended:** 3/3 PASS
**Aspirational:** 22 PASS + 2 PARTIAL (C-24, C-27) + 1 FAIL (C-33) = 22 + 1.0 = 23.0

**Composite score:**
```
essential:    5/5  * 60 = 60.0
recommended:  3/3  * 30 = 30.0
aspirational: 23/25 * 30 = 27.6
TOTAL: 117.6 / 120
```

---

## V-04 Evaluation — Role sequence + partial reconciler (pre-reconciler + 3-check terminal reconciler)

**Structure:** Role 9 VERDICT CURRENCY CHECK present (C-32 PASS). Terminal Reconciler (Role 10) has checks (a), (b), (c) but NOT (d). C-32 PASS, C-24 PASS, C-27 PARTIAL, C-33 FAIL.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Verdict Block with four claims (a)-(d) | PASS | Role 0 states all four claims |
| C-10 | Claim (d) commits to tier count + Schema B | PASS | Claim (d) present as specified |
| C-11 | Format Contract with Schema A and Schema B | PASS | Role 1 defines both schemas |
| C-12 | All four rejection clauses | PASS | Role 1 enumerates all four |
| C-13 | Rate Limit Registry with numeric thresholds | PASS | Role 2 requires numeric thresholds |
| C-14 | Connector vs platform differentiation | PASS | Role 2 includes type field |
| C-15 | Burst path count B recorded | PASS | Role 3 records count B |
| C-16 | STRUCTURAL / INCIDENTAL classification | PASS | Role 3 classifies each path |
| C-17 | Schema A table in cascading failure | PASS | Role 4 requires Schema A table |
| C-18 | DERIVATION CHAIN causal chain arithmetic | PASS | Role 4 requires step-by-step arithmetic |
| C-19 | YES / NO / PARTIAL per endpoint | PASS | Role 5 requires explicit verdict |
| C-20 | Failure mode for non-YES | PASS | Role 5 documents failure modes |
| C-21 | Schema A table >= 3 tiers | PASS | Role 6 requires >= 3 tiers |
| C-22 | REVISED marker at gate boundary | PASS | Roles 2, 5, 8 contain REVISED insertion instructions |
| C-23 | 5x spike row with arithmetic | PASS | Role 6 requires 5x spike row with arithmetic |
| C-24 | Terminal reconciler check (c): DERIVATION CHAIN audit | PASS | Role 10 Check (c) is present as a separately named item: "DERIVATION CHAIN CELL AUDIT" with its own findings output "Derivation Chain Audit: N cells checked, M violation(s)" |
| C-25 | Mitigations with BEFORE/AFTER | PASS | Role 7 requires BEFORE/AFTER states |
| C-26 | Burst path reference in mitigations | PASS | Role 7 references burst paths from Role 3 |
| C-27 | Terminal reconciler check (d): Schema B structural scan | PARTIAL | Role 10 has no check (d); Schema B structural scan absent from terminal reconciler; RECONCILER FINDINGS covers only (a)-(c) |
| C-28 | UX tier blocks use Schema B template | PASS | Role 8 requires Schema B blocks |
| C-29 | Six-item gate in Role 8 | PASS | Role 8 enumerates items (a)-(f) |
| C-30 | Gate item (e) from Role 3 directly | PASS | Role 8 references Role 3 directly |
| C-31 | Verdict currency check in Rate Limit Registry | PASS | Role 2 includes currency check |
| C-32 | Pre-reconciler Verdict Currency as Named Role | PASS | Role 9 is a dedicated named role; sweeps Roles 1-8; annotates deferred insertions as "deferred from Role N"; produces CURRENCY SWEEP FINDINGS named output; Gate 9->10 present |
| C-33 | Four-Check Reconciler Completeness | FAIL | C-33 prerequisite C-27 is PARTIAL (check d absent from reconciler); additionally Role 10 explicitly covers only checks (a)-(c) -- check (d) Schema B structural scan is absent as a separately named item; a reconciler covering three of four checks fails C-33 |

**Essential:** 5/5 PASS
**Recommended:** 3/3 PASS
**Aspirational:** 23 PASS + 1 PARTIAL (C-27) + 1 FAIL (C-33) = 23 + 0.5 = 23.5

**Composite score:**
```
essential:    5/5  * 60 = 60.0
recommended:  3/3  * 30 = 30.0
aspirational: 23.5/25 * 30 = 28.2
TOTAL: 118.2 / 120
```

---

## V-05 Evaluation — Full integration (explicit deferred-source annotation)

**Structure:** Identical to V-01 in structure (Role 9 pre-reconciler + Role 10 4-check terminal reconciler). Distinguishing detail: Role 9 uses explicit "deferred from Role N -- [reason gate-boundary insertion did not fire]" annotation format, making deferral source traceable. Both C-32 and C-33 satisfied with enhanced auditability.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Verdict Block with four claims (a)-(d) | PASS | Role 0 states all four claims with Gate 0->1 no-analysis enforcement |
| C-10 | Claim (d) commits to tier count + Schema B | PASS | Claim (d): "UX tier count will match burst path count from Role 3; Schema B four-field template applied to every tier" |
| C-11 | Format Contract with Schema A and Schema B | PASS | Role 1 defines both schemas with all required fields |
| C-12 | All four rejection clauses | PASS | Role 1 enumerates all four rejection clauses |
| C-13 | Rate Limit Registry with numeric thresholds | PASS | Role 2 requires numeric threshold, window, scope, type per endpoint |
| C-14 | Connector vs platform differentiation | PASS | Role 2 includes type: "connector vs platform type" |
| C-15 | Burst path count B recorded | PASS | Role 3 records count B as authoritative source |
| C-16 | STRUCTURAL / INCIDENTAL classification | PASS | Role 3 classifies each path |
| C-17 | Schema A table in cascading failure | PASS | Role 4 requires Schema A table |
| C-18 | DERIVATION CHAIN causal chain arithmetic | PASS | Role 4: "step-by-step which endpoint triggers first, downstream block sequence, compounding retry volume arithmetic" |
| C-19 | YES / NO / PARTIAL per endpoint | PASS | Role 5 requires explicit verdict |
| C-20 | Failure mode for non-YES | PASS | Role 5 documents failure modes for non-YES |
| C-21 | Schema A table >= 3 tiers | PASS | Role 6 requires >= 3 tiers |
| C-22 | REVISED marker at gate boundary | PASS | Roles 2, 5, 8 contain explicit REVISED insertion instructions |
| C-23 | 5x spike row with arithmetic | PASS | Role 6 explicit example: "200 req/min x 5 = 1000 req/min; limit = 500 req/min; overflow = 500 req/min" |
| C-24 | Terminal reconciler check (c): DERIVATION CHAIN audit | PASS | Role 10 Check (c) is a separately named item with its own findings output |
| C-25 | Mitigations with BEFORE/AFTER | PASS | Role 7 requires BEFORE state and AFTER state |
| C-26 | Burst path reference in mitigations | PASS | Role 7: "Reference which burst path(s) from Role 3" |
| C-27 | Terminal reconciler check (d): Schema B structural scan | PASS | Role 10 Check (d) is a separately named item with its own findings output |
| C-28 | UX tier blocks use Schema B template | PASS | Role 8 requires Schema B block per tier |
| C-29 | Six-item gate in Role 8 | PASS | Role 8 enumerates items (a)-(f) |
| C-30 | Gate item (e) from Role 3 directly | PASS | Role 8: "Verify tier count against Role 3 directly -- do not use Verdict Claim (d)" |
| C-31 | Verdict currency check in Rate Limit Registry | PASS | Role 2 includes currency check for Claim (a) |
| C-32 | Pre-reconciler Verdict Currency as Named Role | PASS | Role 9 is a dedicated named role with full C-32 compliance; the explicit "deferred from Role N -- [reason gate currency check did not fire at Role N's gate boundary]" annotation format exceeds the minimum requirement and makes the source of each deferral directly traceable during terminal verification |
| C-33 | Four-Check Reconciler Completeness | PASS | Role 10 contains checks (a)-(d) as four separately named audit items each with separate findings output; RECONCILER FINDINGS SUMMARY enumerates all four; check (a) is pure verification (Role 9 handles corrections) |

**Essential:** 5/5 PASS
**Recommended:** 3/3 PASS
**Aspirational:** 25/25 PASS (25.0)

**Composite score:**
```
essential:    5/5  * 60 = 60.0
recommended:  3/3  * 30 = 30.0
aspirational: 25/25 * 30 = 30.0
TOTAL: 120.0 / 120
```

---

## Rankings

| Rank | Variation | Composite | Aspirational | Band |
|------|-----------|-----------|--------------|------|
| 1st (tied) | V-01 -- role sequence | 120.0 / 120 | 25/25 | Aspirational ceiling |
| 1st (tied) | V-05 -- full integration | 120.0 / 120 | 25/25 | Aspirational ceiling |
| 3rd | V-02 -- output format | 118.8 / 120 | 24/25 | Near-ceiling (1 FAIL: C-32) |
| 4th | V-04 -- role seq + partial reconciler | 118.2 / 120 | 23.5/25 | Near-ceiling (1 PARTIAL: C-27, 1 FAIL: C-33) |
| 5th | V-03 -- lifecycle emphasis | 117.6 / 120 | 23.0/25 | Near-ceiling (2 PARTIAL: C-24 C-27, 1 FAIL: C-33) |

---

## Round-over-Round Progression

| Round | Top Score | PARTIALs Resolved | New Criteria |
|-------|-----------|-------------------|--------------|
| R11 | 118.7 / 120 (23 criteria) | -- | C-24 PARTIAL, C-27 PARTIAL |
| R12 | 120.0 / 120 (25 criteria) | C-24, C-27 both resolved | C-32, C-33 added |

R12 is the first round to reach 120/120. V-01 and V-05 both achieve it.

---

## Excellence Signals

**Signal 1: C-33 is the fastest path to resolving both R11 PARTIALs.**
C-33 (Four-Check Reconciler Completeness) subsumes C-24 and C-27 as prerequisites -- any variation satisfying C-33 must have check (c) and check (d) present as separately named items, which is exactly what C-24 and C-27 require. A single structural decision (commit to a four-check reconciler) resolves two prior PARTIALs simultaneously. This is visible in V-01 and V-05: adding the four-check reconciler for C-33 automatically satisfies C-24 and C-27 at full PASS.

**Signal 2: C-32 + C-33 create a three-layer enforcement stack for verdict currency.**
Each layer catches what the prior layer misses:
- Layer 1 (C-22): Gate-checkpoint currency insertion -- each role inserts REVISED markers at its own gate boundary when a revision occurs. Misses: roles that revise claims without triggering the gate condition explicitly.
- Layer 2 (C-32): Pre-reconciler deferred sweep -- a dedicated named role sweeps all prior roles for missed gate-boundary insertions and annotates any deferred marker with its source. Misses: only markers where the sweep itself fails (edge case).
- Layer 3 (C-33 check a): Terminal retroactive verification -- the reconciler's check (a) confirms all markers are present post-sweep. Because Layer 2 handles corrections, check (a) becomes pure verification rather than combined correction+verification.
The stack makes it structurally impossible for a missed revision to reach the final document without detection.

**Signal 3: V-05's explicit "deferred from Role N -- [reason]" annotation is the distinguishing detail.**
V-01 and V-05 both achieve 120/120, but V-05's annotation format -- "deferred from Role N -- [reason gate currency check did not fire at Role N's gate boundary]" -- provides two properties V-01's implicit annotation does not: (1) the source role is machine-readable (not buried in prose), and (2) the reason for the deferral is co-located with the marker, making terminal verification check (a) unambiguous. In a multi-run scoring context where a human auditor reviews the document, V-05's format reduces false-negative risk during check (a).

**Signal 4: V-02 illustrates that C-32 and C-33 are orthogonal.**
V-02 achieves C-33 (four checks present in reconciler) without C-32 (no pre-reconciler role). C-33 does not require C-32 -- it requires only C-24 and C-27 as prerequisites. This means a team can add the four-check reconciler without adding the pre-reconciler sweep and still satisfy C-33. The cost is that check (a) remains combined correction+verification, which reduces auditability but does not fail any criterion other than C-32.

---

```json
{
  "skill": "flow-ratelimit",
  "round": 12,
  "rubric_version": 12,
  "date": "2026-03-17",
  "top_score": 120.0,
  "top_score_variations": ["V-01", "V-05"],
  "all_essential_pass": true,
  "all_recommended_pass": true,
  "aspirational_pool": 25,
  "r11_baseline_score": 118.7,
  "r11_partials_resolved": ["C-24", "C-27"],
  "new_criteria": ["C-32", "C-33"],
  "new_patterns": [
    "dedicated-pre-reconciler-named-role",
    "deferred-from-role-N-annotation",
    "four-check-reconciler-separate-findings",
    "three-layer-verdict-currency-stack"
  ],
  "variation_scores": {
    "V-01": 120.0,
    "V-02": 118.8,
    "V-03": 117.6,
    "V-04": 118.2,
    "V-05": 120.0
  }
}
```
