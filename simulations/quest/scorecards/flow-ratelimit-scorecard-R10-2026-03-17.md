Now I have all the evidence needed. Writing the scorecard:

---

# Flow-Ratelimit — Round 10 Scorecard

**Skill:** `flow-ratelimit` | **Rubric:** v10 | **Date:** 2026-03-17
**Scoring denominator:** `/21` aspirational (pool grew from 18 → 21 with C-27, C-28, C-29)

---

## Rubric v10 — New Criteria Summary

**C-27 (V-02 signal):** Schema B declared as a named structural schema in the Format Contract with its own STRUCTURAL REJECTION CLAUSE. Terminal Reconciler must include an explicit Schema B audit as check (d), distinct from the gate audit. Requires C-16, C-19, C-26.

**C-28 (V-03 signal A):** Claim (d) in the Verdict block commits to UX template completeness and tier count. A tier added mid-analysis triggers a REVISED marker on Claim (d) at the gate boundary of the revising role — not deferred to terminal reconciliation. Requires C-15, C-18, C-22, C-26.

**C-29 (V-03 signal B):** Gate 6→7 extends to six explicitly named blocking conditions: (a)–(d) per FIELD, (e) tier-count verification against the Role 4 burst path audit section (not the two-tier minimum), (f) structure-compliance as a separately named blocking condition. Items (e) and (f) must each be named separately — collapsing into a compound condition fails both. Requires C-26.

---

## V-01: Role Sequence — Verdict Claim (d)

**Axis:** ROLE 0 gains Claim (d) committing to N tiers and four-field template coverage, with a revision rule requiring REVISED marker at the gate boundary of the revising role.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Binding Constraint | PASS | ROLE 3 identifies binding constraint with explicit reasoning ("why this limit, not a higher-capacity one"). |
| C-02 | Causal Chain | PASS | ROLE 7 traces complete chain from trigger through rate-limited endpoint to failure mode; every link explicit. |
| C-03 | UX Differentiation | PASS | ROLE 6 requires at least two distinct tiers with observable behavior using four-field template. |
| C-04 | Burst Path | PASS | ROLE 4 identifies structurally unprotected burst paths; STRUCTURAL vs. INCIDENTAL classification required. |
| C-05 | Retry-After Gap | PASS | ROLE 5 evaluates Retry-After/x-ms-ratelimit-remaining at every throttled endpoint; failure mode required. |
| C-06 | Cascading Throttle | PASS | ROLE 8 constructs specific cascade with causal linkage and compounding effect; Gate 8→9 enforces delivery. |
| C-07 | Numeric Specificity | PASS | ROLE 2 requires at least one concrete numeric threshold; estimates labeled. |
| C-08 | Volume Mapping | PASS | ROLE 9 produces structured BASELINE \| PROTECTED \| DERIVATION CHAIN \| DELTA table. |
| C-09 | Per-bottleneck Mitigations | PASS | ROLE 10 requires specific named mitigations per bottleneck with before/after states referencing Schema A columns. |
| C-10 | Quantified Impact | PASS | ROLE 9 requires four-step arithmetic chain for load spike tier; Steps 1–4 explicitly shown. |
| C-11 | Burst Gap Classification | PASS | ROLE 4 requires STRUCTURAL vs. INCIDENTAL classification stated and justified per path. |
| C-12 | Dual-state Volume Mapping | PASS | Schema A in ROLE 1 declares BASELINE and PROTECTED as dual-state columns across all quantified tables. |
| C-13 | Verdict-before-Evidence | PASS | ROLE 0 precedes ROLE 2 rate limit registry; Verdict written before any analytical section. |
| C-14 | Baseline-delta Mitigation | PASS | ROLE 10 requires "before-state: baseline behavior at this bottleneck" and "after-state: with mitigation applied." |
| C-15 | Document-head Verdict | PASS | ROLE 0 has (a) binding constraint, (b) primary gap, (c) system status — self-contained before evidence. |
| C-16 | Format Contract Preamble | PASS | ROLE 1 declares BASELINE \| PROTECTED \| DERIVATION CHAIN \| DELTA schema plus STRUCTURAL and CONTENT rejection clauses. |
| C-17 | Cascading Gate Enforcement | PASS | All gates from 0→1 through 10→11 name prior role's specific deliverables. Gate language at every transition. |
| C-18 | Bidirectional Verdict Revision | PASS | Every role carries "REVISED — see Role N" instruction; Role 0 states revision rule explicitly. |
| C-19 | Four-Field UX Template | PASS | ROLE 6 applies FIELD-A through FIELD-D to every tier; template structure required, not free prose. |
| C-20 | Arithmetic Trace Explicitness | PASS | Steps 1–4 shown inline in DERIVATION CHAIN cell; conclusion-only cell triggers CONTENT REJECTION CLAUSE. |
| C-21 | Full Gate Chain Closure | PASS | All 11 role transitions (Gates 0→1 through 10→11) are explicitly gated with named deliverables. |
| C-22 | Gate-checkpoint Verdict Currency | PASS | Every role beyond ROLE 0 includes Verdict currency check; REVISED marker must be inserted before gate unblocks. |
| C-23 | Schema-column Arithmetic | PASS | DERIVATION CHAIN declared as mandatory fourth column in Format Contract; absence triggers STRUCTURAL REJECTION CLAUSE. |
| C-24 | Terminal Reconciler | PASS | ROLE 11 performs checks (a) Verdict audit, (b) gate audit, (c) derivation chain audit; produces named finding record. |
| C-25 | Two-Tier Violation Taxonomy | PASS | Format Contract names STRUCTURAL (scan-time, column absent) and CONTENT (read-time, conclusion-only) as distinct clause types with separate detection methods and remediations. |
| C-26 | Explicit UX Role Gated Four-Field | PASS | Gate 6→7 names FIELD-A through FIELD-D as items (a)–(d), each individually blocking, scoped to "EVERY tier described in this document, not only the minimum two tiers." |
| **C-27** | Schema B as Named Format Contract Schema | **FAIL** | ROLE 1 Format Contract contains only Schema A (table). No Schema B declaration, no STRUCTURAL REJECTION CLAUSE for UX fields, no Reconciler check (d). |
| **C-28** | UX Completeness as Named Verdict Claim | **PASS** | ROLE 0 Claim (d): "N tiers described; all tiers use the four-field UX template." Revision rule: "insert REVISED on Claim (d) at the gate of the role where the new tier was discovered. Do not defer." |
| **C-29** | Six-Item UX Gate | **FAIL** | Gate 6→7 has items (a)–(e) plus two unlabeled checkboxes. Item (e) checks against Verdict Claim (d), not the Role 4 burst path audit count directly. Structure-compliance is present as an unlabeled checkbox — not named as a separately blocking condition (f). |

**V-01 Composite:** 60 + 30 + (19/21 × 30) = **117.14/120**
Essential: 5/5 | Recommended: 3/3 | Aspirational: 19/21

---

## V-02: Output Format — Schema B in Format Contract

**Axis:** FORMAT CONTRACT declares Schema B as a named structural schema with its own STRUCTURAL REJECTION CLAUSE. Terminal Reconciler adds check (d) for independent Schema B audit. Verdict Block has only claims (a)–(c); no Claim (d).

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Binding Constraint | PASS | Section 2 identifies binding constraint with explicit reasoning. |
| C-02 | Causal Chain | PASS | Section 6 traces complete causal chain; every link explicit. |
| C-03 | UX Differentiation | PASS | Section 5 requires at least two tiers under Schema B template structure. |
| C-04 | Burst Path | PASS | Section 3 identifies burst paths with STRUCTURAL vs. INCIDENTAL classification. |
| C-05 | Retry-After Gap | PASS | Section 4 evaluates Retry-After handling at every throttled endpoint. |
| C-06 | Cascading Throttle | PASS | Section 7 constructs specific cascade with causal linkage and compounding effect. |
| C-07 | Numeric Specificity | PASS | Section 1 requires at least one concrete numeric threshold. |
| C-08 | Volume Mapping | PASS | Section 8 produces Schema A table with all four columns. |
| C-09 | Per-bottleneck Mitigations | PASS | Section 9 requires specific named mitigations per bottleneck referencing Schema A BASELINE and PROTECTED columns. |
| C-10 | Quantified Impact | PASS | Section 8 requires Steps 1–4 in DERIVATION CHAIN cell for load spike tier. |
| C-11 | Burst Gap Classification | PASS | Section 3 requires STRUCTURAL vs. INCIDENTAL classification stated and justified. |
| C-12 | Dual-state Volume Mapping | PASS | Schema A declares BASELINE and PROTECTED for all comparative tables. |
| C-13 | Verdict-before-Evidence | PASS | Verdict Block precedes Format Contract and all analysis sections. |
| C-14 | Baseline-delta Mitigation | PASS | Section 9 references Schema A BASELINE and PROTECTED columns for before/after states. |
| C-15 | Document-head Verdict | PASS | Verdict Block has (a) binding constraint, (b) primary gap, (c) system status — self-contained. |
| C-16 | Format Contract Preamble | PASS | FORMAT CONTRACT section before Section 1 declares Schema A with rejection clauses. |
| C-17 | Cascading Gate Enforcement | PASS | Each section carries explicit gate language naming prior section's deliverables. |
| C-18 | Bidirectional Verdict Revision | PASS | Each section includes "REVISED — see Section N" instruction for Verdict block. |
| C-19 | Four-Field UX Template | PASS | Section 5 requires Schema B four-field template for every tier; free prose explicitly prohibited. |
| C-20 | Arithmetic Trace Explicitness | PASS | Steps 1–4 required in DERIVATION CHAIN; conclusion-only cell triggers CONTENT REJECTION CLAUSE (Schema A). |
| C-21 | Full Gate Chain Closure | PASS | All section transitions gated with named deliverables from prior section. |
| C-22 | Gate-checkpoint Verdict Currency | PASS | Each section includes explicit Verdict currency check before gate. |
| C-23 | Schema-column Arithmetic | PASS | Schema A declares DERIVATION CHAIN as mandatory fourth column with STRUCTURAL REJECTION CLAUSE. |
| C-24 | Terminal Reconciler | PASS | Section 10 performs checks (a) Verdict, (b) gate, (c) derivation chain, (d) Schema B audit; produces named finding record referencing all four checks. |
| C-25 | Two-Tier Violation Taxonomy | PASS | Format Contract names STRUCTURAL (Schema A scan-time) and CONTENT (Schema A read-time) clause types, each with distinct detection method and marker. Schema B also gets STRUCTURAL and CONTENT clauses — four total rejection clauses named. |
| C-26 | Explicit UX Role Gated Four-Field | PASS | Section 5 Gate: "all four field labels present and substantively populated for every tier" via Schema B structure, scoped beyond minimum to every tier. Schema B in Format Contract individually names FIELD-A through FIELD-D as the field-label targets. |
| **C-27** | Schema B as Named Format Contract Schema | **PASS** | Format Contract declares Schema B as "a named structural schema, not a formatting suggestion" with STRUCTURAL REJECTION CLAUSE (scan-time: count field labels) and CONTENT REJECTION CLAUSE (read-time). Reconciler check (d) performs independent Schema B structural scan distinct from gate audit. |
| **C-28** | UX Completeness as Named Verdict Claim | **FAIL** | Verdict Block has only (a), (b), (c). No Claim (d) committing to tier count or four-field template coverage. Reconciler check (a) scans claims (a)–(c) only. V-02 is deliberately C-28-absent. |
| **C-29** | Six-Item UX Gate | **FAIL** | Gate 5→6 reads: "At least two tiers described using Schema B template structure; all four field labels present and substantively populated for every tier; Verdict current." This is a collective gate condition, not six separately named blocking items (a)–(f). No separately named (e) or (f). |

**V-02 Composite:** 60 + 30 + (19/21 × 30) = **117.14/120**
Essential: 5/5 | Recommended: 3/3 | Aspirational: 19/21

---

## V-03: Lifecycle Emphasis — Six-Item UX Gate (a)–(f)

**Axis:** Gate 6→7 restructured as a six-item gate where each condition is separately named and blocking: (a)–(d) per FIELD, (e) tier-count against Role 4 burst path audit count, (f) structure-compliance as a separately named blocking condition. Verdict has only (a)–(c). No Schema B in Format Contract.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Binding Constraint | PASS | ROLE 3 identifies binding constraint with explicit reasoning. |
| C-02 | Causal Chain | PASS | ROLE 7 traces complete causal chain; every link explicit. |
| C-03 | UX Differentiation | PASS | ROLE 6 requires full four-field template for every tier. |
| C-04 | Burst Path | PASS | ROLE 4 identifies burst paths with STRUCTURAL vs. INCIDENTAL classification. |
| C-05 | Retry-After Gap | PASS | ROLE 5 evaluates Retry-After handling at every throttled endpoint. |
| C-06 | Cascading Throttle | PASS | ROLE 8 constructs cascade with causal linkage and compounding effect. |
| C-07 | Numeric Specificity | PASS | ROLE 2 requires at least one concrete numeric threshold. |
| C-08 | Volume Mapping | PASS | ROLE 9 produces Schema A comparative table. |
| C-09 | Per-bottleneck Mitigations | PASS | ROLE 10 requires specific named mitigations with before/after states. |
| C-10 | Quantified Impact | PASS | ROLE 9 requires Steps 1–4 in DERIVATION CHAIN for load spike tier. |
| C-11 | Burst Gap Classification | PASS | ROLE 4 requires STRUCTURAL vs. INCIDENTAL classification. |
| C-12 | Dual-state Volume Mapping | PASS | Schema A declares BASELINE and PROTECTED for all comparative tables. |
| C-13 | Verdict-before-Evidence | PASS | ROLE 0 Verdict Block precedes ROLE 1 Format Contract and all analysis roles. |
| C-14 | Baseline-delta Mitigation | PASS | ROLE 10 requires before-state and after-state per mitigation. |
| C-15 | Document-head Verdict | PASS | ROLE 0 has (a) binding constraint, (b) primary gap, (c) system status — self-contained. |
| C-16 | Format Contract Preamble | PASS | ROLE 1 declares table schema with BASELINE \| PROTECTED \| DERIVATION CHAIN \| DELTA plus STRUCTURAL and CONTENT rejection clauses. |
| C-17 | Cascading Gate Enforcement | PASS | All gates from 0→1 through 10→11 name prior role's specific deliverables. |
| C-18 | Bidirectional Verdict Revision | PASS | Every role includes "REVISED — see Role N" instruction for Verdict. |
| C-19 | Four-Field UX Template | PASS | ROLE 6 requires FIELD-A through FIELD-D for every tier; free prose prohibited. |
| C-20 | Arithmetic Trace Explicitness | PASS | Steps 1–4 in DERIVATION CHAIN cell; conclusion-only triggers CONTENT REJECTION CLAUSE. |
| C-21 | Full Gate Chain Closure | PASS | All 11 role transitions gated with named deliverables. |
| C-22 | Gate-checkpoint Verdict Currency | PASS | Each role includes Verdict currency check embedded at gate boundary. |
| C-23 | Schema-column Arithmetic | PASS | DERIVATION CHAIN declared as mandatory column in Format Contract. |
| C-24 | Terminal Reconciler | PASS | ROLE 11 performs checks (a), (b), (c); check (b) for Gate 6→7 explicitly audits all six conditions (a)–(f). Produces named finding record. |
| C-25 | Two-Tier Violation Taxonomy | PASS | Format Contract names STRUCTURAL (scan-time) and CONTENT (read-time) rejection clause types with distinct detection methods. |
| C-26 | Explicit UX Role Gated Four-Field | PASS | Gate 6→7 items (a)–(d) each name a specific field individually as a separately blocking condition, scoped to "EVERY tier described in this document." |
| **C-27** | Schema B as Named Format Contract Schema | **FAIL** | ROLE 1 Format Contract has only Schema A table. No Schema B declaration, no Schema B STRUCTURAL REJECTION CLAUSE, no Reconciler check (d) for Schema B audit. |
| **C-28** | UX Completeness as Named Verdict Claim | **FAIL** | ROLE 0 has only (a), (b), (c). No Claim (d) for UX tier count or template commitment. V-03 is deliberately C-28-absent. |
| **C-29** | Six-Item UX Gate | **PASS** | Gate 6→7 labeled "SIX-ITEM UX GATE [ALL SIX CONDITIONS ARE SEPARATELY BLOCKING]." Items (a)–(f) each carry a distinct named label. (e): "matches the count of distinct throttle tiers identified in the Role 4 burst path audit. The two-tier minimum is a floor, not the verification target." (f): "separately named blocking condition; it does not merge with conditions (a)–(d)." Explicit anti-compound rule stated. |

**V-03 Composite:** 60 + 30 + (19/21 × 30) = **117.14/120**
Essential: 5/5 | Recommended: 3/3 | Aspirational: 19/21

---

## V-04: Combined — Role Sequence + Output Format (C-28 + C-27)

**Axis:** Verdict Block gains Claim (d) (C-28) AND Format Contract gains Schema B as named structural schema with STRUCTURAL REJECTION CLAUSE (C-27) AND Terminal Reconciler gains check (d) for Schema B audit (C-27 terminal requirement). Gate 6→7 remains (a)–(e) plus unlabeled checkboxes — C-29 not targeted.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | All essential + recommended | PASS | Same as V-01 through V-03; all structural roles present. |
| C-09–C-26 | All prior aspirational | PASS | Same enforcement mechanisms as V-01; Schema B adds coverage but doesn't break prior criteria. |
| **C-27** | Schema B as Named Format Contract Schema | **PASS** | ROLE 1 declares Schema B: "a named structural schema" parallel to Schema A, with table showing FIELD-A through FIELD-D. STRUCTURAL REJECTION CLAUSE: "count field labels without reading field content." Reconciler check (d) performs document-level Schema B scan distinct from gate audit in check (b). |
| **C-28** | UX Completeness as Named Verdict Claim | **PASS** | ROLE 0 Claim (d): "N tiers; all use Schema B (FIELD-A through FIELD-D)." Revision rule: "insert the REVISED marker at the gate of the role where the tier count diverges — not at terminal reconciliation." Gate 0→1 requires Claim (d) written before ROLE 1 begins. |
| **C-29** | Six-Item UX Gate | **FAIL** | Gate 6→7 has items (a)–(e) plus two unlabeled checkboxes ("Schema B template structure used for every tier" and "Verdict updated"). Item (e) checks against Verdict Claim (d), not against the Role 4 burst path audit count directly. Structure-compliance is present but not named as a separately labeled condition (f). |

**V-04 Composite:** 60 + 30 + (20/21 × 30) = **118.57/120**
Essential: 5/5 | Recommended: 3/3 | Aspirational: 20/21

---

## V-05: Combined — All Three Axes (C-27 + C-28 + C-29)

**Axis:** Verdict Block gains Claim (d) (C-28) + Format Contract gains Schema B with STRUCTURAL REJECTION CLAUSE (C-27) + Gate 6→7 becomes six-item gate with (a)–(f) separately named (C-29) + Terminal Reconciler audits all six gate conditions and runs independent Schema B document scan.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | All essential + recommended | PASS | All analysis roles present; full derivation chain; cascade; numeric thresholds. |
| C-09–C-26 | All prior aspirational | PASS | Mitigations with before/after states; full gate chain; bidirectional revision marking; terminal reconciler; two-tier violation taxonomy; explicit UX role with gated four-field. |
| **C-27** | Schema B as Named Format Contract Schema | **PASS** | ROLE 1 declares Schema B: "a named structural schema, parallel in authority to Schema A." STRUCTURAL REJECTION CLAUSE: "Detection: scan-time — count field labels without reading field content." Reconciler check (d): "independent document-level scan, distinct from gate audit in check (b)" — runs fresh structural scan, reports violations regardless of whether gate caught them. |
| **C-28** | UX Completeness as Named Verdict Claim | **PASS** | ROLE 0 Claim (d): "N tiers; all use Schema B four-field template." Revision rule: "at the gate boundary of the role where the discovery occurred — not deferred to terminal reconciliation." Reconciler check (a): "Confirm Claim (d) matches the actual tier count in Role 6 — count Role 6 tiers and compare to Claim (d)." |
| **C-29** | Six-Item UX Gate | **PASS** | Gate 6→7: "Each of the following six conditions is a separately named blocking gate condition. Combining any two into a compound condition does not satisfy both." (e): "matches the count of distinct throttle tiers identified in the Role 4 burst path audit. The two-tier minimum is a floor, not the verification target." (f): "separately named blocking condition; it does not merge with conditions (a)–(d)." ROLE 4 records "exact count of distinct throttle tiers" explicitly for Gate 6→7 item (e). |

**V-05 Composite:** 60 + 30 + (21/21 × 30) = **120.00/120**
Essential: 5/5 | Recommended: 3/3 | Aspirational: 21/21

---

## Composite Score Summary

| Variation | Axis | Essential | Rec. | Asp. (21) | Composite | vs. Predicted |
|-----------|------|-----------|------|-----------|-----------|---------------|
| **V-05** | C-27 + C-28 + C-29 | 60/60 | 30/30 | 30.00/30 | **120.00/120** | 120 ✓ |
| **V-04** | C-27 + C-28 | 60/60 | 30/30 | 28.57/30 | **118.57/120** | ~119 (predicted 120) |
| **V-01** | C-28 only | 60/60 | 30/30 | 27.14/30 | **117.14/120** | ~117 (predicted 118) |
| **V-02** | C-27 only | 60/60 | 30/30 | 27.14/30 | **117.14/120** | ~117 (predicted 118) |
| **V-03** | C-29 only | 60/60 | 30/30 | 27.14/30 | **117.14/120** | ~117 (predicted 118) |

*Predicted values used 18-criterion denominator; v10's /21 denominator yields fractional aspirational scores that land below round-number predictions.*

---

## Ranking

1. **V-05** — 120.00/120 — Only variation that closes all three bypass paths simultaneously. All three new criteria PASS.
2. **V-04** — 118.57/120 — Closes reader-facing (C-28) and scanner-facing (C-27) gaps but leaves gate-level bypass path (C-29) open: structure-compliance unnamed as (f), tier-count cross-check indirect through Claim (d).
3. **V-01, V-02, V-03** — 117.14/120 (tied) — Each closes exactly one of the three new bypass paths. Single-mechanism variations that leave two paths open.

*All essential criteria pass in all five variations. Golden threshold (all essential + composite ≥ 95) satisfied by all five.*

---

## Excellence Signals from V-05

**Signal 1 — Three-mechanism closed loop with no shared bypass path.**
C-27 is scanner-facing (Format Contract structural authority). C-28 is reader-facing (Verdict commitment visible at document head). C-29 is gate-facing (enumerated blocking conditions at the section boundary). Each closes a distinct bypass path that survives when the other two are present but the third is absent. V-04 shows C-27 + C-28 alone is insufficient: a gate reader can still undercount tiers or accept prose-format tiers without (e) and (f) named.

**Signal 2 — Burst-path-audit count as (e) verification target, not Claim (d) as intermediary.**
V-01 and V-04 run tier-count verification against Verdict Claim (d). V-05 runs it directly against "the count of distinct throttle tiers identified in the Role 4 burst path audit." ROLE 4 explicitly records "the exact count" for this purpose. This eliminates the indirection: if Role 4 finds N tiers but Claim (d) was never revised, V-01/V-04's (e) could pass a stale Claim (d). V-05's (e) targets the authoritative source.

**Signal 3 — Anti-compound rule stated explicitly in the gate.**
V-05 Gate 6→7 opens with: "Each of the following six conditions is a separately named blocking gate condition. Combining any two into a compound condition does not satisfy both." This is the C-29 precision: the separation rule is in the gate text itself, not only in the criterion description, making it enforceable at runtime without consulting the rubric.

**Signal 4 — Schema B parallel-authority declaration in Format Contract.**
V-05 ROLE 1 states: "Schema B is a named structural schema, parallel in authority to Schema A." This phrasing makes the structural authority explicit — not a role-level formatting suggestion, not a best-practice template, but a Format Contract commitment with the same scan-time enforcement weight as Schema A's column structure.

**Signal 5 — Terminal Reconciler check (d) as fresh independent scan, not gate replay.**
V-05 Reconciler check (d): "Perform a fresh structural scan... This scan is independent of what Gate 6→7 found — Schema B violations are reported here regardless of whether they were caught at the gate." V-02 and V-04 have similar language, but V-05's reconciler is the only one that also audits all six Gate 6→7 conditions independently in check (b) while running the Schema B scan independently in check (d). Two independent enforcement passes with non-overlapping scope.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["burst-path-audit-as-tier-count-target: (e) in Gate 6→7 verifies tier count against the Role 4 burst path audit count, not against Verdict Claim (d) as intermediary, eliminating stale-Claim bypass", "anti-compound-rule-in-gate-text: the gate opens with an explicit statement that combining any two conditions into a compound check does not satisfy both — making C-29 separation enforceable at runtime without consulting the rubric", "three-mechanism-closed-loop: C-27 (scanner-facing Format Contract), C-28 (reader-facing Verdict), and C-29 (gate-facing enumeration) each close a distinct bypass path that survives when the other two are present but the third is absent"]}
```
