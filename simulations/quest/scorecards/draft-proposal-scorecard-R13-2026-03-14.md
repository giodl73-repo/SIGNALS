# /quest:score — draft-proposal | Round 13 | Rubric v13

## Scoring Reference

Formula: `composite = 90 + (aspirational_pass / 30 × 10)` (when all E + R pass)
Denominator: /30 (added C-36, C-37 to /28 baseline)

---

## V-01 — Architect-First | Designed fail: C-36

**Hypothesis confirmed**: Phase 9b fully structured with dual-domain indexed enumeration. Domain 1 uses `[R-NN pending] → [R-NN IDs applicable to this option]` — per-site arrows present, P×I compound scores absent. Domain 2 uses explicit per-column attribution: `[OPTION-A column: R-NN IDs | OPTION-B column: R-NN IDs | do-nothing column: R-NN IDs]`.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| E-01 | PASS | "ROLE SEQUENCE: Architect → PM" declared as typed header; sequence applied in every phase header |
| E-02 | PASS | Phase 2 has OPTION/PROBLEM/RISK/RATIONALE anatomy; ≥3 options; do-nothing labeled |
| E-03 | PASS | Phase 4 comparison matrix with Architect (technical) and PM (adoption) dimensions |
| E-04 | PASS | Phase 9 recommendation with qualifying conditions and PM/Architect confirmation |
| R-01 | PASS | Phase 3 risk register: R-NN \| RISK \| P \| I \| P×I \| MITIGATION; ≥3 entries; PM adoption row |
| R-02 | PASS | Phase 7 prerequisites check: option count, do-nothing, register count, Phase 9b complete |
| R-03 | PASS | Phase 10 finalization: coverage table to terminal state |
| C-01 | PASS | PROBLEM field verbatim across options |
| C-02 | PASS | Do-nothing labeled explicitly |
| C-03 | PASS | Architect owns technical; PM owns adoption — non-interchangeable roles |
| C-04 | PASS | PM adds adoption/schedule risk entries to register |
| C-05 | PASS | Amendment table initialized at Phase 0 before content phases |
| C-06 | PASS | `{{signal_artifacts}}` referenced at document open |
| C-07 | PASS | Options → register → comparison matrix → recommendation lifecycle respected |
| C-08..C-20 | PASS | Standard baseline satisfies; no axis modification targeting these criteria |
| C-21 | PASS | Phase 5 gate audit verifies all phase headers carry [GATE: X-NN] citations |
| C-22 | PASS | Coverage table built with CRITERION \| STATUS \| CLOSED BY columns |
| C-23 | PASS | Phase 9b back-fills R-NN IDs into all RISK fields; no inline P×I in final output |
| C-24 | PASS | T-01..T-37 exactly 37 rows; T-36 and T-37 defined |
| C-25 | PASS | Phase 10: explicitly numbered Step 1 / Step 2 / Step 3 / Step 4 |
| C-26 | PASS | Phase 9b is a named dedicated phase |
| C-27 | PASS | Coverage table populated for all criteria rows |
| C-28 | PASS | Recommendation includes qualifying conditions |
| C-29 | PASS | PHASE column in amendment table; every row populated |
| C-30 | PASS | "Finding N: T-NN — [criterion ID and full name]" format; Finding 1: T-36 |
| C-31 | PASS | Phase 2 RISK uses `[R-NN pending]` placeholder; no inline P×I |
| C-32 | PASS | Phase 9b names both structural domains explicitly |
| C-33 | PASS | "Do not compute P×I in Phase 2 RISK fields" prohibition adjacent to `[R-NN pending]` |
| C-34 | PASS | "Domain 1 —" / "Domain 2 —" numeric index prefixes on all domain headers |
| C-35 | PASS | `[R-NN pending] → [R-NN IDs applicable to this option]` arrow notation at each Domain 1 site |
| **C-36** | **FAIL** | Arrow notation present but targets contain only R-NN IDs; P×I compound scores absent from Domain 1 transitions. Note explicitly states "reference the register for compound scores" — designed omission |
| C-37 | PASS | Domain 2 uses `[OPTION-A column: R-NN IDs \| OPTION-B column: R-NN IDs \| do-nothing column: R-NN IDs]` — per-column attribution explicit |

**Aspirational passes: 29/30 | Composite: 99.67**
One open trigger: T-36. Finding 1: T-36 — C-36.

---

## V-02 — PM-First, Compact Tables | Designed fail: C-37

**Hypothesis confirmed**: Domain 1 carries full P×I transitions `[R-NN pending] → [R-03 (P:n × I:n = n), R-07 (P:n × I:n = n)]`. Domain 2 confirms row-level only: "Risk row: R-NN IDs applied to risk row. Confirm applicable register entries present." — no per-column attribution. CLOSED BY preserved even in compact format.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| E-01 | PASS | "ROLE SEQUENCE: PM → Architect" declared; applied in all phase headers |
| E-02 | PASS | Compact option blocks retain full OPTION/PROBLEM/RISK/RATIONALE anatomy |
| E-03 | PASS | Phase 4 compact matrix with PM-selected and Architect-validated dimensions |
| E-04 | PASS | Phase 9 recommendation with qualifying conditions |
| R-01 | PASS | Phase 3 compact risk register; PM adds 1-2 adoption entries |
| R-02 | PASS | Phase 7 confirms: options ≥3, do-nothing, register ≥3, Phase 9b complete |
| R-03 | PASS | Phase 10 finalization complete |
| C-01..C-07 | PASS | Standard baseline; no axis modifications target mandatory tier |
| C-08..C-20 | PASS | Standard baseline |
| C-21 | PASS | Phase 5 gate audit |
| C-22 | PASS | CLOSED BY column preserved "even in compact form for traceability" |
| C-23 | PASS | Phase 9b back-fills R-NN IDs into all RISK fields |
| C-24 | PASS | T-01..T-37 exactly 37 rows |
| C-25 | PASS | Phase 10 numbered Step 1 / Step 2 / Step 3 / Step 4 |
| C-26 | PASS | Dedicated Phase 9b present |
| C-27..C-30 | PASS | Standard baseline |
| C-31 | PASS | `[R-NN pending]` placeholder in Phase 2 RISK |
| C-32 | PASS | "Domain 1 — Option RISK fields" and "Domain 2 — Comparison matrix risk column" both named |
| C-33 | PASS | "Do not compute P×I in Phase 2 RISK fields" prohibition adjacent to placeholder |
| C-34 | PASS | "Domain 1 —" / "Domain 2 —" numeric index prefixes present |
| C-35 | PASS | `[OPTION-A label] RISK field: [R-NN pending] → [R-03 (P:n × I:n = n), ...]` per-site arrow notation |
| C-36 | PASS | P×I compound scores embedded in Domain 1 transition targets alongside R-NN IDs |
| **C-37** | **FAIL** | "Risk row: R-NN IDs applied to risk row." — Domain 2 names the domain (C-32 PASS) and is indexed (C-34 PASS) but provides only row-level confirmation. No per-option-column attribution. T-37 note in amendment spec explicitly says "row-level confirmation 'R-NN IDs applied to risk row' fires T-37" |

**Aspirational passes: 29/30 | Composite: 99.67**
One open trigger: T-37. Finding 1: T-37 — C-37.

---

## V-03 — Lifecycle-Heavy, Stale Table | Designed fails: C-24 + C-36 + C-37

**Hypothesis confirmed**: Amendment table built from C-01..C-35 (35 rows). T-36 and T-37 absent. T-24 fires at PRE-DOCUMENT (35 ≠ 37). Phase 9b uses per-site arrows but Domain 1 omits P×I; Domain 2 row-level only. Only one ordinal finding because T-36/T-37 rows don't exist to fire.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| E-01..E-04 | PASS | Standard baseline |
| R-01..R-03 | PASS | Standard baseline |
| C-01..C-07 | PASS | Standard baseline |
| C-08..C-20 | PASS | Standard baseline |
| C-21 | PASS | Phase 5 gate audit present |
| C-22 | PASS | Coverage table has CLOSED BY column |
| C-23 | PASS | Phase 9b back-fills R-NN IDs |
| **C-24** | **FAIL** | Amendment table initialized with "C-01 through C-35" — explicitly 35 rows. T-24 fires at PRE-DOCUMENT: 35 ≠ 37. Designed: the prompt says "Build trigger rules from C-01 through C-35. Each criterion generates one trigger row (T-01..T-35). Total: 35 rows." |
| C-25 | PASS | Phase 10 explicitly numbered four-step list |
| C-26..C-30 | PASS | Standard baseline |
| C-31 | PASS | `[R-NN pending]` placeholder and "Do not compute P×I" prohibition in Phase 2 |
| C-32 | PASS | Phase 9b has "Domain 1 —" and "Domain 2 —" labels |
| C-33 | PASS | Prohibition adjacent to placeholder |
| C-34 | PASS | "Domain 1 —" / "Domain 2 —" prefixes present |
| C-35 | PASS | `[OPTION-A label] RISK field: [R-NN pending] → [R-NN IDs applicable to this option]` — arrow notation present at each site |
| **C-36** | **FAIL** | Domain 1 transitions: `[R-NN pending] → [R-NN IDs applicable to this option]` — R-NN IDs present, P×I compound scores absent. T-36 not in stale table → no trigger fires, but criterion fails behaviorally |
| **C-37** | **FAIL** | Domain 2: "R-NN IDs confirmed in risk row. Confirm applicable register entries are referenced." — row-level only. T-37 not in stale table → no trigger fires, but criterion fails behaviorally |

**Note on findings**: Only Finding 1: T-24 (PRE-DOCUMENT). C-36 and C-37 fail behaviorally but produce no ordinal findings because T-36/T-37 rows were never authored.

**Aspirational passes: 27/30 | Composite: 99.00**

---

## V-04 — Conversational Register | Designed fails: C-25 + C-33; C-36 + C-37 both PASS

**Hypothesis confirmed**: Finalization as prose narrative ("Walk through coverage verification as a narrative discussion"). Phase 2 RISK template includes `[R-NN pending]` placeholder but no "Do not compute P×I" prohibition. Phase 9b demonstrates both C-36 and C-37 passing in natural language register.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| E-01..E-04 | PASS | Standard baseline; conversational style doesn't affect essential criteria |
| R-01..R-03 | PASS | Standard baseline |
| C-01..C-07 | PASS | Standard baseline |
| C-08..C-20 | PASS | Standard baseline |
| C-21 | PASS | Phase 5 gate audit |
| C-22 | PASS | Coverage table with CLOSED BY |
| C-23 | PASS | Phase 9b back-fills R-NN IDs |
| C-24 | PASS | T-01..T-37 exactly 37 rows |
| **C-25** | **FAIL** | Phase 10: "Walk through coverage verification as a narrative discussion." No numbered steps (Step 1 / Step 2 / Step 3 / Step 4). T-25 PHASE = FINALIZATION fires. |
| C-26..C-29 | PASS | Standard baseline |
| C-30 | PASS | "produce a named finding inline in the narrative using the label format 'Finding N: T-NN'" — ordinal format specified even within narrative |
| C-31 | PASS | `[R-NN pending]` placeholder present in Phase 2 RISK |
| C-32 | PASS | "Domain 1 — Option RISK fields" and "Domain 2 — Comparison matrix risk column" both named |
| **C-33** | **FAIL** | Phase 2 RISK template: `[R-NN pending] — Placeholder for risk register linkage; will be resolved in Phase 9b.` — placeholder present but "Do not compute P×I" prohibition absent from the same template block. T-33 fires. |
| C-34 | PASS | "Domain 1 —" / "Domain 2 —" prefixes present |
| C-35 | PASS | `[OPTION-A label] RISK field: [R-NN pending] → [R-03 (P:n × I:n = n), R-07 (P:n × I:n = n)]` arrow notation |
| C-36 | PASS | "Include each register entry's P×I compound score in the back-fill notation so that option anatomy is self-contained at review time." — P×I scores embedded in Domain 1 transition targets |
| C-37 | PASS | "Risk row: [OPTION-A column: R-03, R-07 \| OPTION-B column: R-01, R-04 \| do-nothing column: R-02]" — explicit per-column attribution |

Two open triggers: T-25 and T-33. Finding 1: T-25. Finding 2: T-33.

**Aspirational passes: 28/30 | Composite: 99.33**

---

## V-05 — Inertia Framing + C-36 + C-37 Dual Fail | Designed fails: C-36 + C-37

**Hypothesis confirmed**: Phase 9b structurally complete (C-32/C-33/C-34/C-35 all PASS), inertia framing leads to Domain 1 ID-only transitions and Domain 2 aggregate attribution. Explicit note: "the register is the authoritative source for compound scoring — option anatomy carries the register IDs, not redundant score copies."

| Criterion | Result | Evidence |
|-----------|--------|----------|
| E-01..E-04 | PASS | Standard baseline; inertia framing doesn't affect essential criteria structure |
| R-01..R-03 | PASS | Standard baseline; inertia-related risks added for Option A |
| C-01..C-07 | PASS | Standard baseline |
| C-08..C-20 | PASS | Standard baseline |
| C-21 | PASS | Phase 5 gate audit |
| C-22 | PASS | Coverage table with CLOSED BY |
| C-23 | PASS | Phase 9b back-fills R-NN IDs |
| C-24 | PASS | T-01..T-37 exactly 37 rows; T-36 and T-37 both defined |
| C-25 | PASS | Phase 10 numbered four-step list |
| C-26..C-30 | PASS | Standard baseline |
| C-31 | PASS | "Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending]" |
| C-32 | PASS | "Domain 1 — Option RISK fields" and "Domain 2 — Comparison matrix risk column" both named |
| C-33 | PASS | Prohibition explicitly adjacent to `[R-NN pending]` placeholder |
| C-34 | PASS | "Domain 1 —" / "Domain 2 —" numeric index prefixes |
| C-35 | PASS | `[OPTION-A label] RISK field: [R-NN pending] → [R-NN IDs applicable to Option A]` — arrow notation at each Domain 1 site |
| **C-36** | **FAIL** | Domain 1 transitions: `[R-NN pending] → [R-NN IDs applicable to Option A]` — R-NN IDs listed, P×I compound scores absent. Design note: "the register is the authoritative source for compound scoring" provides explicit semantic justification for the omission. T-36 fires. |
| **C-37** | **FAIL** | Domain 2: "Risk row: R-NN IDs applied by option. Applicable register entries referenced in risk row." — aggregate option-level attribution without column labels. T-37 fires. Contrast with C-32 PASS (domain named) and C-34 PASS (indexed). |

Two open triggers: T-36 and T-37. Finding 1: T-36. Finding 2: T-37.

**Aspirational passes: 28/30 | Composite: 99.33**

---

## Ranked Results

| Rank | Variation | Fails | A/30 | Composite |
|------|-----------|-------|------|-----------|
| 1 | **V-01** (Architect-First) | C-36 | 29/30 | **99.67** |
| 1 | **V-02** (PM-First Compact) | C-37 | 29/30 | **99.67** |
| 3 | V-04 (Conversational) | C-25, C-33 | 28/30 | 99.33 |
| 3 | V-05 (Inertia Framing) | C-36, C-37 | 28/30 | 99.33 |
| 5 | V-03 (Stale Table) | C-24, C-36, C-37 | 27/30 | 99.00 |

All essential criteria pass across all five variations. No variation falls below Golden threshold.

---

## Cascade Verification

**C-36 cascade invariant**: Confirmed by V-03 non-cascade case — V-03 has C-35 PASS (arrows present) and C-36 FAIL (no P×I). This proves C-36 fails independently when C-35 passes, not only through cascade. The cascade fires only when C-35 fails (as in V-05 R12 aggregate form). R13 provides no new cascade evidence since all R13 variations pass C-35.

**C-37 independent fail**: Confirmed by V-02 — C-32 PASS (domain named), C-34 PASS (indexed), C-37 FAIL (row-level only). Per-column attribution is a dimension of C-37 orthogonal to both C-32 and C-34. The independent-fail pattern first confirmed by V-04 R12 is reinforced here with the added observation that C-36 can simultaneously PASS when C-37 independently fails.

**T-36/T-37 coverage gap in V-03**: Confirmed — stale 35-row table allows C-36 and C-37 to fail behaviorally without producing named trigger findings. The criterion failures are detectable by rubric evaluation but invisible to the amendment table's trigger-firing mechanism.

---

## Excellence Signals from V-01 and V-02

**Signal 1 — Role sequence is orthogonal to Phase 9b depth criteria**: V-01 (Architect-first) and V-02 (PM-first) both achieve 99.67 with single-criterion failures on opposite axes. The Architect-first framing does not prevent per-column Domain 2 attribution (C-37 PASS in V-01). The PM-first compact format does not prevent P×I self-contained transitions (C-36 PASS in V-02). Neither role sequence nor output density is a structural barrier to the depth criteria introduced in v13.

**Signal 2 — CLOSED BY preserved as traceability invariant under format compression**: V-02 explicitly notes "kept even in compact form for traceability" for the CLOSED BY column. Compact-table format that compresses cell values still preserves the audit column. This suggests CLOSED BY is a structural requirement with different weight than cell-level depth criteria — format axes compress content, not audit structure.

**Signal 3 — P×I self-containment value proposition articulated**: V-04 explicitly names the rationale: "Include each register entry's P×I compound score in the back-fill notation so that option anatomy is self-contained at review time." V-01 articulates the opposing semantic: "reference the register for compound scores rather than repeating them in the transition notation." The tension between these two design philosophies (self-contained anatomy vs. register-as-authority) is now fully documented through contrast across R13 variations.

---

```json
{"top_score": 99.67, "all_essential_pass": true, "new_patterns": ["Role sequence axis (Architect-first vs PM-first) is orthogonal to Phase 9b depth criteria: C-37 passes in Architect-first register (V-01) while C-36 fails; C-36 passes in PM-first compact format (V-02) while C-37 fails — neither role assignment nor output density structurally prevents either criterion", "CLOSED BY column is preserved as a traceability invariant under format compression: compact-table format compresses cell values but not audit structure, suggesting CLOSED BY has higher structural weight than depth criteria like C-36/C-37"]}
```
