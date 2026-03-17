# flow-resilience — Round 9 Scorecard (Rubric v8)

**Rubric**: v8 · 21 criteria · Denominator 21
**R8 Ceiling**: 13/21 → composite 96.19 (V-05)
**Open criteria entering R9**: None
**Scoring premise**: All variations are designed to hold the R8 V-05 baseline (13 passing criteria) while probing three unexplored axes. Score differentials arise only if a new axis happens to satisfy one of the 8 criteria not yet simultaneously achievable, or if a pattern exposes a crack in an existing criterion.

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (binary — all must pass for 60-point block)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Scenario Coverage | PASS | PASS | PASS | PASS | PASS |
| **C-02** Four-Field Structure per Scenario | PASS | PASS | PASS | PASS | PASS |
| **C-03** Gap Identification (3 gap types) | PASS | PASS | PASS | PASS | PASS |
| **C-04** Distributed Systems Accuracy | PASS | PASS | PASS | PASS | PASS |

**Evidence — C-01**: Every variation explicitly names three classes as distinct scenario rows with a class-label requirement ("Exactly one of: Class 1 / Class 2 / Class 3"). No collapse path exists.

**Evidence — C-02**: Every variation carries a Column Contract that lists all four fields (System State, User Capability, Data at Risk, Recovery Path) with non-trivial fill requirements. V-02 extends Recovery Path to TTD/TTC/TTR/TTV targets but does not remove any field — it strengthens the fill gate.

**Evidence — C-03**: All variations end with a Gap Register section requiring three labeled, actionable gap types. The prohibition on generic statements ("offline support may be limited" fails) is preserved verbatim across all.

**Evidence — C-04**: D-role ownership of System State, Data at Risk, and Recovery Path mechanics is present in all variations. V-01's register change is orthogonal to role assignment — "D" and "C" ownership columns are retained in conversational phrasing.

**All-essential block**: ✅ PASS across all five variations → 60 points.

---

### Excellence Criteria (C-05 through C-27: baseline from R8 V-05)

These 9 criteria were passing in R8 V-05 and are preserved in all R9 variations by design. Axis changes are additive — no existing mechanism is removed.

| Criterion block | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----------------|------|------|------|------|------|-------|
| C-05 through C-16 (structural mechanisms) | PASS | PASS | PASS | PASS | PASS | All four-level anti-omission architecture preserved: table / section / column / slot |
| C-17 — Anti-split instruction | PASS | PASS | PASS | PASS | PASS | "No sub-tables, no horizontal rules between rows" present in all variations |
| C-18 — Column Contract completeness | PASS | PASS | PASS | PASS | PASS | All 9 columns named with fill requirements |
| C-19 — Slot-level imperative (row descriptor) | PASS | PASS | PASS | PASS | PASS | Per-row imperatives at cell granularity in all |
| C-20 — Phase gate | PASS | PASS | PASS | PASS | PASS | "Write all rows before Gap Register" enforced in all |
| C-21 — Outcome branching (node A / B / naive) | PASS | PASS | PASS | PASS | PASS | Class 3 row descriptor carries all three consequence branches verbatim |

**Note on V-01 register shift**: Conversational imperative ("You're working as two specialists") replaces formal imperative ("Two specialist roles contribute") but all structural mechanisms survive the register change. The anti-omission architecture, column ownership, and row-level imperatives are unchanged. Register orthogonality hypothesis holds.

---

### Newest Criteria (C-28, C-29)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|---------|
| **C-28** Sub-Field Completeness Gate | PASS | PASS | PASS | PASS | PASS | Row Descriptor for all three rows carries "including all four Recovery Path stages (Detect/Contain/Recover/Validate)" as the named sub-field gate condition. V-02 strengthens this further with "(Detect/TTD, Contain/TTC, Recover/TTR, Validate/TTV)" — the four named stages are still present. |
| **C-29** Chronic Consequence Enumeration | PASS | PASS | PASS | PASS | PASS | Status Quo Risk column is present in all Column Contracts. All Row Descriptors name an accumulating metric with no-ceiling framing. V-03/V-04/V-05 further add rate + horizon components, which satisfy C-29 at a higher quality floor but do not change the PASS/FAIL verdict under current criterion text. |

---

### Criteria not yet simultaneously achievable (C-22 through C-27: 8 remaining)

No R9 variation introduces a structural mechanism that cracks these. V-02's SLA targets and V-03's three-component accumulation framing are candidates for **C-30+** but do not address the remaining uncracked criteria, which require design-level changes not represented in any R9 axis.

**Passing criteria across all variations**: 13/21

---

## Composite Score Computation

**Formula**: 60 (essential block) + 30 (structural excellence, criteria C-05 through C-27) + (13/21 × 10)

| Variation | Essential (60) | Excellence (30) | Criterion ratio | Composite |
|-----------|----------------|-----------------|-----------------|-----------|
| V-01 | 60 | 30 | 13/21 = 6.19 | **96.19** |
| V-02 | 60 | 30 | 13/21 = 6.19 | **96.19** |
| V-03 | 60 | 30 | 13/21 = 6.19 | **96.19** |
| V-04 | 60 | 30 | 13/21 = 6.19 | **96.19** |
| V-05 | 60 | 30 | 13/21 = 6.19 | **96.19** |

**All five variations tie at 96.19** — the R8 V-05 ceiling. None of the three probed axes (register, SLA stage, quantified accumulation) maps to an uncracked criterion in the current v8 rubric. The ceiling is numerically flat; differentiation is in pattern richness.

---

## Ranking

| Rank | Variation | Composite | Discriminating feature |
|------|-----------|-----------|----------------------|
| 1 | **V-05** | 96.19 | Both candidate C-30 patterns present + register neutrality confirmed |
| 2 | **V-04** | 96.19 | Both candidate C-30 patterns without register axis |
| 2 | **V-02** | 96.19 | Recovery Path SLA pattern only |
| 2 | **V-03** | 96.19 | Three-component chronic pattern only |
| 5 | **V-01** | 96.19 | Register orthogonality confirmed; no new patterns |

Tiebreaker logic: pattern richness for C-30+ expansion. V-05 > V-04 > V-02 = V-03 > V-01.

---

## Excellence Signals

### Signal 1 — Register Orthogonality (V-01)
Conversational second-person imperative ("You're working as two specialists") preserves full structural compliance. All 13 criteria pass identically. This means the anti-omission architecture is **semantically load-bearing, not tonally load-bearing** — the mechanisms survive register change. Design implication: the prompt can be adapted for chat-deployment contexts without compliance degradation.

### Signal 2 — Recovery Path SLA Budget (V-02) → Candidate C-30
The Column Contract's fill requirement for Recovery Path becomes: "named mechanism **AND** a time-budget target." Four slots become eight specifications (mechanism × stage + TTD/TTC/TTR/TTV). The row-descriptor imperatives enforce this at the cell level: "Do not advance to row 2 until TTD, TTC, TTR, TTV are all stated." This is a new structural layer — C-28 measures sub-field presence (stage names); a C-30 would measure sub-field quantification (stage + SLA). The pattern name: **Recovery Path Stage SLA Budget**.

### Signal 3 — Three-Component Chronic Enumeration (V-03/V-04/V-05) → Candidate C-31
C-29 requires a chronic consequence statement. V-03 strengthens the floor to require three named components: **metric** (what is measured), **rate** (how fast it grows), **horizon** (what it looks like if never resolved). This is a tighter specification than C-29's current form and would discriminate outputs that write "oversell rate accumulates" (satisfies C-29) from outputs that write "oversell rate accumulates at N units per deploy cycle; without intervention, reconciliation debt grows without ceiling" (satisfies candidate C-31). Pattern name: **Three-Component Chronic Enumeration**.

---

## R9 Rubric Expansion Signal

| Candidate | Axis | Pattern | Source variation | Status |
|-----------|------|---------|-----------------|--------|
| C-30 | V-02 | Recovery Path Stage SLA Budget — each stage names a mechanism AND a time-budget target (TTD/TTC/TTR/TTV) | V-02, V-04, V-05 | Ready to draft |
| C-31 | V-03 | Three-Component Chronic Enumeration — Status Quo Risk specifies metric + accumulation rate + temporal horizon | V-03, V-04, V-05 | Ready to draft |

**If C-30 and C-31 are added (denominator 23):**
- V-05 ceiling: 15/23 = 6.52 → composite 96.52
- V-04 ceiling: 15/23 = 6.52 → composite 96.52 (V-04 also carries both patterns)
- V-02 ceiling: 14/23 = 6.09 → composite 96.09 (SLA only)
- V-03 ceiling: 14/23 = 6.09 → composite 96.09 (accumulation only)
- V-01 ceiling: 13/23 = 5.65 → composite 95.65 (neither pattern)

This expansion would break the R9 tie and give V-04/V-05 the new ceiling.

---

```json
{"top_score": 96.19, "all_essential_pass": true, "new_patterns": ["Recovery Path Stage SLA Budget: each Recovery Path stage requires a named mechanism AND an explicit time-budget target (TTD/TTC/TTR/TTV), raising the fill gate from sub-field presence to sub-field quantification", "Three-Component Chronic Enumeration: Status Quo Risk column specifies a three-part structure — metric name, accumulation rate, and unresolved horizon — rather than a generic chronic consequence statement"]}
```
