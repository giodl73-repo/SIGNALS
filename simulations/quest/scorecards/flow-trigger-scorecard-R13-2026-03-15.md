## Flow-trigger Round 13 — Scoring (Rubric v10)

**Scenario:** Dynamics 365 Sales `account.statecode` changes Active (0) → Inactive (1).
**New criteria this round:** C-32 (unified Phase 0 obligation registry) and C-33 (constraint-propagating INERTIA CONTRAST failure mode labels).

---

## Per-Variation Scorecards

### V-01 — Inertia framing; consequence-language failure modes; separate obligation tables

| Criterion | Tier | Verdict | Evidence Note |
|-----------|------|---------|---------------|
| C-01 Trigger enumeration | Essential | PASS | Phase 2+3 templates require all candidates to resolve to FIRING or NON-FIRING entry; Phase 1 denominator enforces completeness |
| C-02 Execution order | Essential | PASS | EOR TABLE declared; Phase 2 requires ordering by EOR rules; sync/async split enforced by phase separation |
| C-03 Inputs/outputs per trigger | Essential | PASS | FIRING ENTRY schema has Input Fields and Output Action as required named slots; Invariant 5 mandates no empty slots |
| C-04 Three anomaly verdicts | Essential | PASS | Phase 5 explicitly declares all three verdict blocks; Phase 1 opens three anomaly slots |
| C-05 Platform grounding | Essential | PASS | Platform Term Contract defines approved vocabulary; FM-08 VOCAB FAIL marker enforces compliance |
| C-06 Circular trigger analysis | Recommended | PASS | Phase 4 applies back-edge detection; FM-19 [BACKTRACK MISS] enforces it |
| C-07 Conditional branch paths | Recommended | PASS | FIRING ENTRY has Condition (Taken) and Condition (Skipped); NON-FIRING ENTRY has both bilateral slots |
| C-08 Anomaly remediation | Recommended | PASS | Phase 5 verdict blocks require "Remediation (if confirmed)" per anomaly class |
| C-09 Execution tier / latency | Aspirational | PASS | Phase 3 Async table has Latency Tier column; FM-10 enforces timing annotation |
| C-10 Cascade completeness | Aspirational | PASS | Phase 4 Cascade Chain Table traces side-effect writes end-to-end |
| C-11 Candidate denominator | Aspirational | PASS | Phase 1 Denominator Pre-Scan declares N before Phase 2 |
| C-12 Gap tokens | Aspirational | PASS | NON-FIRING ENTRY schema; FM-01 [OMIT] handles silent omission |
| C-13 Verdict evidence citation | Aspirational | PASS | Phase 5 Evidence field required; FM-12 [INSUFFICIENT] fires on bare assertions |
| C-14 Scope gate | Aspirational | PASS | SCOPE GATE with entity/operation/field/values declared before Phase 1 |
| C-15 Bilateral counterfactual | Aspirational | PASS | Both entry types carry Condition (Taken) and Condition (Skipped) slots |
| C-16 Registration witness | Aspirational | **WEAK PASS** | Flow Type and Trigger Event provide partial grounding; no dedicated Registration Witness slot in entry schema; CLOSURE CHECK does not track it |
| C-17 EOR rule citation per entry | Aspirational | **WEAK PASS** | EOR TABLE declared; CLOSURE CHECK tracks "ART-03 EOR citations missing: 0"; but entry schema has no dedicated EOR citation column |
| C-18 Cascade depth budget | Aspirational | PASS | CASCADE DEPTH BUDGET (MAX=5) declared Phase 0; Phase 4 entries carry [Depth: N/5]; [DEPTH EXCEEDED] overflow marker defined |
| C-19 Exclusion log / verdict citation | Aspirational | **WEAK PASS** | EXCLUSION LOG covers 6 layers with dispositions; but Phase 5 verdict blocks have no "Exclusion log reference:" field |
| C-20 Zero-tolerance closure counters | Aspirational | PASS | CLOSURE CHECK block with 5 named counters all asserting must-be-zero |
| C-21 Role prohibition contracts | Aspirational | PASS | PROHIBITION CONTRACTS table with "Role Bound" and "Applies After" columns |
| C-22 Uniform slot mandate | Aspirational | PASS | Invariant 5: "Every named slot in every entry schema template is required. An empty named slot is a structural gap." |
| C-23 Pre-enumeration artifact lock | Aspirational | PASS | ARTIFACT MANIFEST with ART-NN IDs for all 6 artifacts declared before Phase 1 |
| C-24 Prohibition breach markers | Aspirational | PASS | BREACH TOKEN PROTOCOL defined; CLOSURE CHECK "PROHIBITION BREACHES: 0 \| 0" |
| C-25 Named lifecycle phase / exit conditions | Aspirational | PASS | Phase 0 with entry condition, 6-item exit obligation table, "6/6 SATISFIED" exit signal before Phase 1 |
| C-26 INERTIA CONTRAST | Aspirational | PASS | Consolidated INERTIA CONTRAST section; 2 mechanisms; weaker alternatives + concrete failure modes named |
| C-27 Computable exit signal | Aspirational | PASS | Status column in exit signal table; "6/6 SATISFIED" aggregate; evaluator can recompute by scanning Status column |
| C-28 Per-obligation refutation conditions | Aspirational | PASS | SCOPE GATE, EOR TABLE, CASCADE DEPTH BUDGET, PROHIBITION CONTRACTS, ARTIFACT MANIFEST tables each have Refutation Condition column |
| C-29 INERTIA CONTRAST as inline columns | Aspirational | **WEAK PASS** | Consolidated INERTIA CONTRAST section exists (C-26 pass); no Weaker Alternative or Failure Mode columns in individual obligation tables |
| C-30 Temporally-anchored prohibitions | Aspirational | PASS | PROHIBITION CONTRACTS "Applies After" column: "Denominator declaration (Phase 1)" and "Phase 0 exit signal" |
| C-31 Role-attributed artifact production | Aspirational | **WEAK PASS** | ARTIFACT MANIFEST has Producing Role + Producing Phase; CLOSURE CHECK counter only references ART-03 by ID — no role attribution in counters |
| C-32 Unified Phase 0 obligation registry | Aspirational | **FAIL** | 6 separate tables (SCOPE GATE, EXCLUSION LOG, EOR TABLE, CASCADE DEPTH BUDGET, PROHIBITION CONTRACTS, ARTIFACT MANIFEST) + Phase 0 Exit Signal table; cross-table navigation required |
| C-33 Constraint-propagating failure modes | Aspirational | **FAIL** | Failure modes are consequence-language: "scope gap produces false positive candidates," "global prohibition creates temporal ambiguity" — reader cannot derive pass condition from label alone |

**V-01 Aspirational summary:** 18 PASS + 5 WEAK PASS + 2 FAIL = (18 + 2.5)/25 = 20.5 eq-passes
**V-01 Composite:** 60 + 30 + (20.5/25 × 10) = 60 + 30 + **8.2** = **98.2**

---

### V-02 — Vertical OBLIGATION RECORD blocks; consequence-language failure modes

| Criterion | Tier | Verdict | Evidence Note |
|-----------|------|---------|---------------|
| C-01–C-08 | Essential/Recommended | PASS (all 8) | Identical structural provisions to V-01 for phases 1-6 |
| C-09–C-15 | Aspirational | PASS (all 7) | Identical to V-01 |
| C-16 | Aspirational | **WEAK PASS** | Same as V-01 — no Registration Witness slot |
| C-17 | Aspirational | **WEAK PASS** | Same as V-01 |
| C-18 | Aspirational | PASS | CASCADE DEPTH BUDGET in OBLIGATION RECORD block with activation event noted |
| C-19 | Aspirational | **WEAK PASS** | EXCLUSION LOG per obligation block; no verdict citation slot |
| C-20–C-25 | Aspirational | PASS (all 6) | All structural mechanisms present in obligation records |
| C-26 | Aspirational | **WEAK PASS** | Rationale is distributed across 6 separate OBLIGATION RECORD blocks rather than a consolidated INERTIA CONTRAST section; "inline comments scattered across role mandates" = weak pass per C-26 |
| C-27–C-28 | Aspirational | PASS (both) | Status and Refutation Condition slots present per obligation block |
| C-29 | Aspirational | **WEAK PASS** | Weaker Alternative and Failure Mode present as block slots, not as table columns in a registry row |
| C-30–C-31 | Aspirational | **WEAK PASS** (both) | C-30: activation events present in contract body; C-31: manifest has roles but CLOSURE CHECK has no role-attributed counters |
| C-32 | Aspirational | **WEAK PASS** | Vertical blocks co-locate all 6 metadata types per obligation; C-32 requires "at least 6 typed columns" — blocks are not a table column structure |
| C-33 | Aspirational | **FAIL** | Failure modes: "scope boundaries become unverifiable," "enforcement becomes unpredictable" — consequence language, no absent structural property named |

**V-02 Aspirational summary:** 17 PASS + 7 WEAK PASS + 1 FAIL = (17 + 3.5)/25 = 20.5 eq-passes
**V-02 Composite:** 60 + 30 + (20.5/25 × 10) = **98.2**

---

### V-03 — Role-split sub-phases; INERTIA CONTRAST names structural absences

| Criterion | Tier | Verdict | Evidence Note |
|-----------|------|---------|---------------|
| C-01–C-08 | Essential/Recommended | PASS (all 8) | Phase structure identical to V-01 for phases 1-6 |
| C-09–C-15 | Aspirational | PASS (all 7) | Same structural provisions |
| C-16 | Aspirational | **WEAK PASS** | No Registration Witness slot |
| C-17 | Aspirational | **WEAK PASS** | Same as V-01 |
| C-18 | Aspirational | PASS | CASCADE DEPTH BUDGET in sub-phase 0b |
| C-19 | Aspirational | **WEAK PASS** | EXCLUSION LOG in sub-phase 0a; no verdict citation slot |
| C-20–C-25 | Aspirational | PASS (all 6) | All mechanisms present |
| C-26 | Aspirational | PASS | Dedicated INERTIA CONTRAST section names 2 mechanisms with weaker alternatives and structural absence failure modes |
| C-27–C-28 | Aspirational | PASS (both) | Sub-phase tables carry Status and Refutation Condition columns |
| C-29 | Aspirational | **WEAK PASS** | Standalone INERTIA CONTRAST section; no contrast columns within sub-phase obligation tables |
| C-30–C-31 | Aspirational | **WEAK PASS** (both) | Temporal anchors present; role attribution in manifest but not in CLOSURE CHECK counters |
| C-32 | Aspirational | **FAIL** | Two separate sub-phase tables (0a and 0b) + separate INERTIA CONTRAST; cross-table navigation required to audit any single obligation's complete metadata |
| C-33 | Aspirational | **WEAK PASS** | Structural absence labels: "scope boundary is not a named structural artifact," "activation window is absent" — names absent property but requires one additional reasoning hop to derive minimum implementation |

**V-03 Aspirational summary:** 18 PASS + 6 WEAK PASS + 1 FAIL = (18 + 3.0)/25 = 21.0 eq-passes
**V-03 Composite:** 60 + 30 + (21.0/25 × 10) = 60 + 30 + **8.4** = **98.4**

---

### V-04 — Unified 6-column registry; structural-property-naming failure modes

| Criterion | Tier | Verdict | Evidence Note |
|-----------|------|---------|---------------|
| C-01–C-08 | Essential/Recommended | PASS (all 8) | Phases 1-6 identical to V-01 |
| C-09–C-15 | Aspirational | PASS (all 7) | Same structural provisions |
| C-16 | Aspirational | **WEAK PASS** | No Registration Witness slot |
| C-17 | Aspirational | **WEAK PASS** | EOR TABLE + CLOSURE CHECK enforcement; no dedicated entry schema slot |
| C-18 | Aspirational | PASS | CASCADE DEPTH BUDGET row in registry; MAX=5; Phase 4 depth counters |
| C-19 | Aspirational | **WEAK PASS** | EXCLUSION LOG in registry row; verdict blocks lack citation slot |
| C-20–C-28 | Aspirational | PASS (all 9) | CLOSURE CHECK, prohibition contracts, uniform slot mandate, artifact manifest, breach tokens, Phase 0 gate, INERTIA CONTRAST section, computable exit signal, per-obligation refutation conditions |
| C-29 | Aspirational | PASS | PHASE 0 OBLIGATION REGISTRY table has "Weaker Alternative" and "Failure Mode" as named columns; all 7 rows carry non-empty values in both contrast columns |
| C-30 | Aspirational | PASS | PROHIBITION CONTRACTS block with temporal anchors |
| C-31 | Aspirational | **WEAK PASS** | Producing Role column in registry and supplementary ARTIFACT MANIFEST; CLOSURE CHECK doesn't reference roles in counters (same format as V-01) |
| C-32 | Aspirational | PASS | PHASE 0 OBLIGATION REGISTRY: single named table, 6 typed columns (Status, Refutation Condition, Weaker Alternative, Failure Mode, Activation Event, Producing Role); all 7 rows non-empty with explicit N/A reasons |
| C-33 | Aspirational | **WEAK PASS** | Labels name absent structural properties: "anonymous scope boundary," "absent temporal anchor," "unattributed production gap"; INERTIA CONTRAST adds "What this forces" subtext. Reader still needs one reasoning hop: "absent temporal anchor" → must reason to "requires named Applies After field as mechanism" |

**V-04 Aspirational summary:** 20 PASS + 5 WEAK PASS + 0 FAIL = (20 + 2.5)/25 = 22.5 eq-passes
**V-04 Composite:** 60 + 30 + (22.5/25 × 10) = 60 + 30 + **9.0** = **99.0**

---

### V-05 — Unified registry + "anonymous [X]" convention + embedded DERIVATION TEST

| Criterion | Tier | Verdict | Evidence Note |
|-----------|------|---------|---------------|
| C-01–C-08 | Essential/Recommended | PASS (all 8) | Phases 1-6 fully structured; all schema slots defined |
| C-09–C-15 | Aspirational | PASS (all 7) | Latency tier column (C-09); cascade chain table (C-10); Phase 1 denominator (C-11); NON-FIRING ENTRY schema (C-12); FM-12 evidence enforcement (C-13); SCOPE GATE event tuple (C-14); bilateral conditions in both entry types (C-15) |
| C-16 | Aspirational | **WEAK PASS** | Flow Type + Trigger Event provide platform grounding but no explicit Registration Witness slot; not tracked in CLOSURE CHECK |
| C-17 | Aspirational | **WEAK PASS** | EOR TABLE declared; CLOSURE CHECK enforces "EOR citations missing: 0 [must be 0]"; entry schema table has no dedicated "Positioned because: EOR-NN" column |
| C-18 | Aspirational | PASS | CASCADE DEPTH BUDGET row in registry (MAX=5, activation noted); Phase 4 carries [Depth: N/5]; [DEPTH EXCEEDED] overflow marker defined |
| C-19 | Aspirational | **WEAK PASS** | EXCLUSION LOG table with 6 layers and named dispositions; Phase 5 verdict blocks have Evidence slot but no "Exclusion log reference:" field; CLOSURE CHECK does not track verdict-level log citation |
| C-20 | Aspirational | PASS | CLOSURE CHECK: 7 named counters all with must-be-zero or must-be-CLOSED assertions |
| C-21 | Aspirational | PASS | PROHIBITION CONTRACTS table with named prohibitions and Applies After column |
| C-22 | Aspirational | PASS | Invariant 5: global "all slots required" mandate applying to all entry types |
| C-23 | Aspirational | PASS | ARTIFACT MANIFEST with ART-01 through ART-06 declared before Phase 1; CLOSURE CHECK references "ART-01 through ART-06" |
| C-24 | Aspirational | PASS | BREACH TOKEN PROTOCOL defined; CLOSURE CHECK "PROHIBITION BREACHES: 0 \| 0" |
| C-25 | Aspirational | PASS | Phase 0 with entry condition; 7-item PHASE 0 OBLIGATION REGISTRY; "7/7 SATISFIED — enumeration authorized" exit signal |
| C-26 | Aspirational | PASS | INERTIA CONTRAST section with DERIVATION TEST; 6 mechanisms analyzed; makes rationale prescriptive rather than explanatory |
| C-27 | Aspirational | PASS | Status column with SATISFIED values; "7/7 SATISFIED" aggregate; evaluator can verify by scanning Status column |
| C-28 | Aspirational | PASS | Refutation Condition column in registry; all 7 rows carry specific inspectable conditions (e.g., "Violated if any candidate is named before event tuple appears in a named structural artifact") |
| C-29 | Aspirational | PASS | PHASE 0 OBLIGATION REGISTRY has Weaker Alternative and Failure Mode as typed columns; all 7 rows fully populated in both contrast columns; contrast is cell-level, not section-level |
| C-30 | Aspirational | PASS | PROHIBITION CONTRACTS table with "Applies After" column: "Denominator declaration (Phase 1 completion)" and "Phase 0 exit signal" |
| C-31 | Aspirational | PASS | ARTIFACT MANIFEST carries Producing Role + Producing Phase per entry; CLOSURE CHECK counter: "ART-01 through ART-06: all produced (Auditor/Domain Expert Phase 0) \| 6/6 \| 6/6" — producing roles named in counter |
| C-32 | Aspirational | PASS | PHASE 0 OBLIGATION REGISTRY: single named table with 6 typed columns; all 7 rows non-empty; every N/A cell carries bracketed explanation distinguishing intentional N/A from omission |
| C-33 | Aspirational | PASS | "anonymous [X]" / "invisible [X]" convention used for all 6 mechanisms; DERIVATION TEST formally maps each label → absent structural property → derived minimum implementation; constraint propagation explicitly verified: "A reader who reads only the Failure Mode column can derive the minimum implementation for every Phase 0 obligation" |

**V-05 Aspirational summary:** 22 PASS + 3 WEAK PASS + 0 FAIL = (22 + 1.5)/25 = 23.5 eq-passes
**V-05 Composite:** 60 + 30 + (23.5/25 × 10) = 60 + 30 + **9.4** = **99.4**

---

## Summary Table

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | All Essential Pass |
|-----------|---------------|-----------------|-------------------|-----------|-------------------|
| V-01 | 60.0 | 30.0 | 8.2 | **98.2** | YES |
| V-02 | 60.0 | 30.0 | 8.2 | **98.2** | YES |
| V-03 | 60.0 | 30.0 | 8.4 | **98.4** | YES |
| V-04 | 60.0 | 30.0 | 9.0 | **99.0** | YES |
| V-05 | 60.0 | 30.0 | 9.4 | **99.4** | YES |

**Rank:** V-05 > V-04 > V-03 > V-01 = V-02

All variations exceed the golden threshold (all essential pass AND composite >= 80). Differentiation is entirely in the aspirational section.

---

## C-32 / C-33 Criterion Detail

| Variation | C-32 | C-33 |
|-----------|------|------|
| V-01 | FAIL — 6 separate tables, cross-navigation required | FAIL — consequence language ("false positive candidates," "temporal ambiguity") |
| V-02 | WEAK PASS — all metadata co-located per block but blocks ≠ table columns | FAIL — consequence language ("boundaries become unverifiable") |
| V-03 | FAIL — two sub-phase tables + separate INERTIA CONTRAST, obligation audit crosses three locations | WEAK PASS — names absent property ("scope boundary not a named artifact") but one reasoning hop to mechanism |
| V-04 | PASS — single 6-column table, explicit N/A-with-reason, one row = complete audit record | WEAK PASS — "anonymous scope boundary" / "absent temporal anchor" names property; "What this forces" adds subtext; still requires one hop to specific mechanism field |
| V-05 | PASS — single 6-column table, all N/A cells bracketed, cross-navigation eliminated | PASS — "anonymous [X]" convention + DERIVATION TEST proves label alone derives minimum implementation |

---

## Excellence Signals from V-05

**Pattern 1 — "anonymous [X]" / "invisible [X]" failure mode naming convention**
Each failure mode label names the structural property whose absence creates the failure, using the pattern: `anonymous [property]` or `invisible [property]` or `absent [named field]`. The naming convention makes derivation one-step: "anonymous scope boundary" → scope boundary must be named → event tuple with named fields. Labels such as "anonymous prohibition," "anonymous artifact gap," "invisible breach," and "anonymous ordering rule" each specify the implementation constraint without requiring rubric access.

**Pattern 2 — Embedded DERIVATION TEST in INERTIA CONTRAST**
The INERTIA CONTRAST section contains a 4-column derivation test table (Mechanism | Failure Mode Label | Absent Structural Property | Derived Minimum Implementation) verifying constraint propagation for all 6 mechanisms. Followed by an explicit constraint propagation verification statement: "A reader who reads only the Failure Mode column can derive the minimum implementation for every Phase 0 obligation." This converts INERTIA CONTRAST from explanatory to prescriptive — it does not just explain why, it proves that the explanation is sufficient to reconstruct the requirement.

**Pattern 3 — Explicit N/A-with-reason bracketing in every N/A cell**
Every cell that holds N/A carries a parenthetical explanation of why N/A is appropriate (e.g., "row is N/A because the obligation exists outside phase sequencing" vs. "row is non-N/A because depth budget is only relevant from Phase 4 onward"). This makes N/A structurally distinguishable from omission at the cell level, removing the ambiguity that C-32 identifies as a weak pass condition.

**Pattern 4 — Role-attributed CLOSURE CHECK counter**
The CLOSURE CHECK counter for artifact production reads: "ART-01 through ART-06: all produced (Auditor/Domain Expert Phase 0) | 6/6 | 6/6" — naming the producing roles directly inside the counter. This makes the closure check role-traceable: a gap would read "ART-02 (EXCLUSION LOG) — Auditor, Phase 0: ABSENT" rather than "ART-02: not found."

---

```json
{"top_score": 99.4, "all_essential_pass": true, "new_patterns": ["anonymous-X failure mode naming convention: label names absent structural property using 'anonymous [X]' or 'invisible [X]' pattern, making pass condition derivable from label alone without rubric", "embedded DERIVATION TEST in INERTIA CONTRAST: formal 3-column table (label -> absent property -> minimum implementation) with explicit constraint propagation verification statement confirming Failure Mode column alone suffices to derive all mechanism requirements", "explicit N/A-with-reason bracketing: every N/A cell in unified registry carries parenthetical explanation distinguishing intentional N/A from omission, making cell emptiness structurally self-documenting", "role-attributed CLOSURE CHECK counter: artifact production counter names producing roles inline ('Auditor/Domain Expert Phase 0'), making production gaps role-traceable in the closure check itself"]}
```
