I now have everything needed to score all five variations. Let me compile the full analysis.

---

# flow-lifecycle — Round 13 Scorecard (Rubric v13)

## Baseline State Entering R13

All five R13 variations inherit the complete R12 V-05 architecture: C-01 through C-41 all PASS across every variation. The base carries:
- Full SECTION A/B ordinal structure (C-15, C-18, C-21)
- Role Registry Gate with all four anti-generic checks including Role→Exception gate (C-40)
- PHASE ENTRY CONTRACT with `Prior phase:` and `Prior phase blocked bottleneck:` sub-fields (C-41, C-37)
- EX block `Bottleneck Ref: B-NN` and `Role Ref: R-ID` sub-fields (C-13, C-40)
- Nine-direction CHAIN STATUS including Phase-sequence and Role→Exception directions
- Dual-Cite Fail Conditions A+B in B-NN preamble (C-39)
- Evidence field with dual-location concrete example and labeled axes (C-24, C-27, C-28)
- SCAFFOLD REQUIREMENT for all B-NN blocks (C-29)

**Open criteria entering R13: C-42 and C-43.**

---

## Essential Criteria (C-01–C-05)

All five variations PASS all essential criteria. The incumbant baseline, terminal state table with completeness check, phase-scoped exception traces, domain role registry, and gap MISSING: field with IM-ID rationale are structural constants across all variations.

**Essential: 5/5 for all variations.**

---

## Recommended Criteria (C-06–C-08)

All five variations PASS all recommended criteria. FORK/JOIN with labeled join condition (C-06), EC-N constructed-answer blocks with three sub-fields (C-07), DS-[S-ID] decision supplement blocks with Fallback sub-field (C-08) are structural constants.

**Recommended: 3/3 for all variations.**

---

## Aspirational Criteria — New Criteria for R13

### C-42 — Exception Block Bottleneck Cross-Reference

**Pass condition requires:**
1. EX block `Bottleneck Ref: B-NN` sub-field (Exception→B direction) — **already in base from R11**
2. Bottleneck Analysis preamble gate check verifying every declared B-ID appears in ≥1 EX block `Bottleneck Ref:` field (B-NN→Exception direction)
3. CHAIN STATUS `B-NN→Exception` direction enumerating pairs and naming dark bottlenecks

**C-42 structural analysis:**

The key difference from R12's C-40 situation: for C-40, BOTH axes (Axis D: EX block `Role Ref:` and Axis E: registry gate fourth check) were newly added in R12. For C-42, the Exception→B direction (EX block `Bottleneck Ref:`) was established in R11 and is already in the base. The discriminating new element is the preamble gate check closing the B-NN→Exception direction (Axis G1).

This means V-01 (Axis G1 only) already provides FULL bidirectional closure for C-42 — the existing `Bottleneck Ref:` carries Exception→B; the new gate check carries B-NN→Exception. V-01 is the **minimum for C-42**, unlike the R12 situation where V-01 (Axis D only) was PARTIAL.

| Variation | Gate check in preamble | B-NN→Exception CHAIN STATUS | EX block Bottleneck Ref (base) | C-42 verdict |
|-----------|:---:|:---:|:---:|------|
| V-01 | YES | YES | YES (base) | **PASS** — Gate closes B-NN→Exception; base provides Exception→B; bidirectional closure achieved |
| V-02 | YES | YES (enhanced) | YES (base) | **PASS** — Gate + per-block Exception Refs; enhanced block-level navigation |
| V-03 | NO | NO | YES (base) | **FAIL** — No preamble gate check; B-NN→Exception direction absent from CHAIN STATUS |
| V-04 | YES | YES | YES (base) | **PASS** — Gate check present; CHAIN STATUS B-NN→Exception direction present |
| V-05 | YES | YES (enhanced) | YES (base) | **PASS** — Maximum strength: gate + per-block Exception Refs + consistency check |

---

### C-43 — Phase Exit Gate Forward Phase Sequential Linkage

**Pass condition requires:**
1. Each PHASE EXIT GATE carries `Next phase:` sub-field with literal phase identifier
2. Last phase carries NONE or END sentinel
3. CHAIN STATUS gains `Phase-exit-sequence` direction

**C-43 structural analysis:**

C-43 is symmetric to C-41 on the exit side. C-41 put `Prior phase:` in entry contracts (backward). C-43 puts `Next phase:` in exit gates (forward). V-03 provides the minimum: the sub-field is present, the sentinel is specified, CHAIN STATUS Phase-exit-sequence direction verifies string comparability. C-41 is already in the base for all variations (inherited from R12 base), so the `Prior phase:`/`Next phase:` bidirectional pair is complete in V-03, V-04, V-05.

| Variation | Next phase: sub-field in exit gate | Sentinel on last phase | CHAIN STATUS Phase-exit-sequence | C-43 verdict |
|-----------|:---:|:---:|:---:|------|
| V-01 | NO | N/A | NO | **FAIL** — No Next phase: sub-field; exit gate lacks forward linkage |
| V-02 | NO | N/A | NO | **FAIL** — No Next phase: sub-field |
| V-03 | YES | YES (NONE/END) | YES | **PASS** — Next phase: sub-field + sentinel + CHAIN STATUS direction; orthogonality to Blocked bottleneck: confirmed |
| V-04 | YES | YES (NONE/END) | YES | **PASS** — Both sub-fields in exit gate; explicit preamble clarifying B-ID vs Phase label independence |
| V-05 | YES | YES (NONE/END) | YES | **PASS** — Three-field system described explicitly (Prior phase: / Prior phase blocked bottleneck: / Next phase:) |

---

## Aspirational Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09–C-39 (31 criteria) | 31 PASS | 31 PASS | 31 PASS | 31 PASS | 31 PASS |
| C-40 Exception Block Role Cross-Reference | PASS | PASS | PASS | PASS | PASS |
| C-41 Phase Entry Prior-Phase Linkage | PASS | PASS | PASS | PASS | PASS |
| C-42 Exception Block Bottleneck Cross-Reference | **PASS** | **PASS** | **FAIL** | **PASS** | **PASS** |
| C-43 Phase Exit Gate Forward Linkage | **FAIL** | **FAIL** | **PASS** | **PASS** | **PASS** |
| **Aspirational PASS total** | **34/35** | **34/35** | **34/35** | **35/35** | **35/35** |

---

## Composite Scores

Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/35 × 10)`

```
V-01: (5/5 × 60) + (3/3 × 30) + (34/35 × 10) = 60 + 30 + 9.71 = 99.71
V-02: (5/5 × 60) + (3/3 × 30) + (34/35 × 10) = 60 + 30 + 9.71 = 99.71
V-03: (5/5 × 60) + (3/3 × 30) + (34/35 × 10) = 60 + 30 + 9.71 = 99.71
V-04: (5/5 × 60) + (3/3 × 30) + (35/35 × 10) = 60 + 30 + 10.00 = 100.0
V-05: (5/5 × 60) + (3/3 × 30) + (35/35 × 10) = 60 + 30 + 10.00 = 100.0
```

---

## Scorecard

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-04 Axes G1+H | 5/5 | 3/3 | 35/35 | **100.0** | YES |
| 1 | V-05 Axes G1+G2+H | 5/5 | 3/3 | 35/35 | **100.0** | YES |
| 3 | V-01 Axis G1 | 5/5 | 3/3 | 34/35 | **99.71** | YES |
| 3 | V-02 Axes G1+G2 | 5/5 | 3/3 | 34/35 | **99.71** | YES |
| 3 | V-03 Axis H | 5/5 | 3/3 | 34/35 | **99.71** | YES |

**C-42 minimum**: V-01. The preamble gate check alone is sufficient — the EX block `Bottleneck Ref:` was already in the base from R11, providing the Exception→B direction; the gate check provides the B-NN→Exception direction. Full bidirectional closure achieved with Axis G1 only. Contrast with R12's C-40: both Axis D and Axis E were new in R12, so BOTH were required simultaneously. For C-42, only the gate is new.

**C-43 minimum**: V-03. `Next phase:` sub-field in exit gates alone is sufficient. C-41's `Prior phase:` is already in the base, so the bidirectional Phase→Phase pair is complete with V-03's addition.

**Both simultaneously**: V-04 (minimum), V-05 (maximum). Both achieve 100.0; they compose cleanly — no shared state between the B-NN→Exception gate axis and the Phase-exit-sequence axis.

---

## Within the 100 Cluster: Structural Guarantee Differences

| Property | V-04 | V-05 |
|----------|------|------|
| B-NN→Exception direction | Preamble gate check only (scan required) | Preamble gate + per-block `Exception Refs:` (block-level navigation, no scan) |
| Exception Refs: consistency check | None | CHAIN STATUS verifies listed EX IDs have matching Bottleneck Ref (bidirectional string-compare at block level) |
| Three-field architectural description | Implicit (two fields noted as independent) | Explicit: "three sub-fields: Prior phase: / Prior phase blocked bottleneck: / Next phase:" — the complete bidirectional system named as a formal architectural property |
| CHAIN STATUS directions | 11 (B-NN→Exception as scan-based gate result) | 11 (B-NN→Exception as per-block consistency verification) |

V-05 provides lower structural risk: a reviewer using V-04 must scan all EX blocks to verify B-NN→Exception closure; a reviewer using V-05 can navigate directly from the B-NN block's `Exception Refs:` field to the cited EX blocks by string comparison without scanning.

---

## Excellence Signals (from V-05 — maximum architectural density)

1. **Per-block `Exception Refs:` as navigation-complete bidirectional closure**: V-04's preamble gate check requires scanning all EX blocks to confirm a B-ID is cited. V-05's per-block `Exception Refs:` makes each B-NN block self-contained for forward navigation — the reviewer reads `Exception Refs: EX-1A, EX-2B` and navigates directly to those blocks by string comparison. This is structurally identical to how V-02 in R12 improved on V-01's C-40 architecture: the gate verifies presence; the per-block field enables navigation. The pattern generalizes: when a gate check validates "does artifact A appear in artifact B?", an explicit reverse-reference field in A listing its B citations converts the gate from a scan-dependent verification to a block-level string comparison.

2. **Three-field bidirectional Phase system declared as named architecture**: V-05 explicitly identifies the complete Phase linkage system across entry contract and exit gate: `Prior phase:` (C-41, backward Phase→Phase), `Prior phase blocked bottleneck:` (C-37, B-NN boundary continuity, orthogonal), and `Next phase:` (C-43, forward Phase→Phase). This three-field description names the full bidirectional Phase→Phase pair as a formal architectural property rather than two independently noted sub-fields. Out-of-order rendering is now detectable from both the exit gate (forward check) and entry contract (backward check) by string comparison, with the B-NN continuity field on an independent axis — three independently verifiable traceability directions in two template blocks.

---

## C-42 and C-43 Independence Confirmation

V-01 passes C-42 without C-43. V-03 passes C-43 without C-42. V-04 confirms composability — both pass simultaneously with no cross-field interference. The B-NN→Exception gate operates exclusively on the bottleneck-to-exception axis (within Bottleneck Analysis preamble and CHAIN STATUS); `Next phase:` operates exclusively on the phase-sequence axis (within PHASE EXIT GATE and CHAIN STATUS). Neither axis touches the other's structural elements. CHAIN STATUS simply accumulates both new directions (11 total in V-04/V-05 vs 9 in R12 base).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Per-block Exception Refs: in B-NN blocks creates navigation-complete bidirectional B-NN<->Exception closure without requiring a scan of all EX blocks — the gate check verifies presence but per-block listing enables direct string-comparable navigation from B-NN block to EX blocks; this generalizes the R12 Role Ref pattern: when a gate validates artifact A cites artifact B, a reverse-reference field in A listing its B citations converts scan-dependent verification into block-level string comparison", "Three-field Phase system (Prior phase: / Prior phase blocked bottleneck: / Next phase:) across entry contract and exit gate constitutes a complete bidirectional Phase->Phase plus B-NN boundary continuity architecture when named explicitly — Prior phase: and Next phase: form a symmetric Phase->Phase pair independently verifiable from both directions; Prior phase blocked bottleneck: is orthogonal (B-ID axis, not Phase label axis); V-05 names this three-field relationship as a formal architectural property rather than individually noted sub-fields"]}
```
