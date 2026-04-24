# flow-lifecycle — Quest Score Report (Round 8)

---

## Scoring Formula

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01–C-05 | 12 pts each = 60 pts |
| Recommended | C-06–C-08 | 10 pts each = 30 pts |
| Aspirational | C-09–C-30 | pass_count / 22 × 10 pts |

---

## Baseline Declaration (all variations)

C-01 through C-26 are stable across all five variations. The V-01 template provides the canonical structure for this baseline. Confirmed PASS for each:

| ID | Status | Evidence |
|----|--------|----------|
| C-01 | PASS | State table requires named entry condition + labeled exit(s) per row; no state exits unlabeled |
| C-02 | PASS | Template enforces minimum 3 distinct EX-[Phase#]A flows to TERMINAL across phases |
| C-03 | PASS | Role Registry Gate clears before any state tracing; every DS block requires R-[ID] owner |
| C-04 | PASS | BOTTLENECK ANALYSIS section requires B-01, B-02 with Cause + Impact fields |
| C-05 | PASS | Every exit row must name destination S-ID or TERMINAL; PARALLEL and DECISION paths close to a terminal |
| C-06 | PASS | PARALLEL PATH MODELING section with FORK + AND/OR-JOIN + join condition |
| C-07 | PASS | EDGE CASE ENUMERATION requires EC-01…EC-03+ with Trigger + Why Problematic + Correct Response |
| C-08 | PASS | DS-[S-ID] blocks with Condition, Owner, Branch A/B, Fallback per branching state |
| C-09 | PASS | Explicit CROSS-PROCESS HANDOFF CONTRACT section with 6-field contract |
| C-10 | PASS | SLA ANALYSIS referenced in Evidence fail-condition contract; AT-RISK row annotation enforced |
| C-11 | PASS | DS blocks carry Fallback field as named sub-field |
| C-12 | PASS | Role Registry Gate with anti-generic validation; three gate-check items must clear before tracing |
| C-13 | PASS | EX-[Phase#]A nomenclature anchors each exception trace to its originating phase |
| C-14 | PASS | Evidence field in B-NN blocks cross-references AT-RISK SLA rows to bottleneck IDs |
| C-15 | PASS | STRUCTURAL CONSTRAINT: SECTION A before SECTION B explicitly stated per phase block |
| C-16 | PASS | Evidence field format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]` encodes both directions |
| C-17 | PASS | EX blocks use labeled sub-field answers (Trigger/Trace/Handling Role/Terminal/Why Problematic) |
| C-18 | PASS | SECTION A/B ordinal labels encode exception-first ordering as a named structural constraint |
| C-19 | PASS | B-NN blocks carry named Evidence field listing AT-RISK SLA rows that cite the B-ID |
| C-20 | PASS | Chain Status gate implied by Evidence field fail-condition: bidirectional closure is a discrete evaluation output |
| C-21 | PASS | SECTION A constructed-answer blocks per phase satisfy C-13 + C-15 + C-17 through one structural decision |
| C-22 | PASS | Backward-chain dependency from C-22→C-19 satisfied; Evidence field format contract present |
| C-23 | PASS | C-23→C-20; chain status verifiable from Evidence completeness |
| C-24 | PASS | C-24→C-22; per-block hint carries concrete domain example (S-05 pattern in preamble) |
| C-25 | PASS | C-25→C-23; chain closure verifiable |
| C-26 | PASS | C-26→C-22; cascading locality requirement established in preamble |

---

## Variation-by-Variation Evaluation

### V-01 — Single Axis: C-28 Gap (Generic B-[ID] Placeholder)

**Axis:** Per-block `Required format:` retains `B-[ID]` bracket placeholder rather than instantiated `B-01`/`B-02`.

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-01–C-26 | PASS | Baseline holds |
| C-27 | PASS | Depth-3 chain: C-22→C-26→C-27; parent C-26 passes; locality invariant declared |
| C-28 | **FAIL** | Per-block Evidence hint reads `causal source: B-[ID]` not `causal source: B-01`; generic placeholder does not instantiate the owning B-ID for the block in scope |
| C-29 | PASS | Scaffold completeness gate (`ALL B-NN blocks must carry an Evidence field`) is declared above the B-01 block; independent of whether the format is instantiated |
| C-30 | PASS | DUAL-LOCATION REQUIREMENTS preamble consolidates both locality properties under one named header |

**Aspirational pass:** 21 / 22

| Tier | Pts |
|------|-----|
| Essential | 60.00 |
| Recommended | 30.00 |
| Aspirational | 21/22 × 10 = **9.55** |
| **Total** | **99.55** |

---

### V-02 — Fully Instantiated (C-28 PASS, C-29 PASS, C-30 PASS)

**Axis:** Per-block `Required format:` uses `causal source: B-01` (or `B-02`). C-29 scaffold gate explicit. C-30 consolidated block present.

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-01–C-27 | PASS | Baseline + depth-4 chain holds |
| C-28 | **PASS** | Per-block Required format reads `causal source: B-01` — instantiated to owning B-ID |
| C-29 | **PASS** | "SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field" present as named gate |
| C-30 | **PASS** | DUAL-LOCATION REQUIREMENTS consolidated block names: (1) concrete domain example at both locations, (2) labeled axes (`Required format:`/`Fail condition:`) at both locations |

**Aspirational pass:** 22 / 22

| Tier | Pts |
|------|-----|
| Essential | 60.00 |
| Recommended | 30.00 |
| Aspirational | 22/22 × 10 = **10.00** |
| **Total** | **100.00** |

---

### V-03 — Single Axis: C-29 Gap (Scaffold Completeness Gate Absent)

**Axis:** Template omits the SCAFFOLD REQUIREMENT preamble line. B-NN blocks exist but the explicit "ALL B-NN blocks must carry Evidence field" gate declaration is absent.

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-01–C-27 | PASS | Baseline holds; C-27 parent chain unaffected |
| C-28 | PASS | Per-block `Required format:` is instantiated (`B-01`/`B-02`) |
| C-29 | **FAIL** | No explicit scaffold completeness gate; C-29 requires a named declaration — "each B-NN block carries Evidence" language in the per-block text does not substitute for the gating sentence above the B-01 block |
| C-30 | PASS | DUAL-LOCATION REQUIREMENTS block present; C-30 depends on C-24+C-27 both of which pass |

**Aspirational pass:** 21 / 22

| Tier | Pts |
|------|-----|
| Essential | 60.00 |
| Recommended | 30.00 |
| Aspirational | 21/22 × 10 = **9.55** |
| **Total** | **99.55** |

---

### V-04 — Cascade Root: C-27 FAIL → C-28, C-29, C-30 FAIL

**Axis:** C-27 FAIL (locality invariant not declared; dual-location requirement absent from preamble). Dependency chain: C-27→C-28, C-27→C-29, C-24+C-27→C-30 → all three R8 criteria cascade-FAIL.

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-01–C-26 | PASS | Baseline holds through C-26 |
| C-27 | **FAIL** | Locality invariant not declared; neither concrete domain example nor labeled axes appear in the BOTTLENECK preamble |
| C-28 | **FAIL (cascade)** | C-28→C-27; parent FAIL propagates; per-block format cannot be evaluated against an absent preamble contract |
| C-29 | **FAIL (cascade)** | C-29→C-27; scaffold completeness gate is absent; its predicate (dual-location preamble) is the C-27 structure |
| C-30 | **FAIL (cascade)** | C-30→C-24+C-27; C-24 passes but C-27 is FAIL; consolidated block cannot exist without its C-27 locality foundation |

**Aspirational pass:** 18 / 22

| Tier | Pts |
|------|-----|
| Essential | 60.00 |
| Recommended | 30.00 |
| Aspirational | 18/22 × 10 = **8.18** |
| **Total** | **98.18** |

---

### V-05 — Full R8 Compliance with Explicit Symmetry (C-28 PASS, C-29 PASS, C-30 PASS)

**Axis:** Same structural outcome as V-02 but achieved through symmetric scaffold language: both B-01 and B-02 carry instantiated `Required format:` lines, and the scaffold gate is co-located with the DUAL-LOCATION REQUIREMENTS block rather than preceding it.

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-01–C-27 | PASS | Full depth-4 chain satisfied |
| C-28 | **PASS** | Both B-01 and B-02 per-block hints read `causal source: B-01` / `causal source: B-02` respectively |
| C-29 | **PASS** | Scaffold gate co-located within DUAL-LOCATION REQUIREMENTS section; ALL B-NN scope is explicit |
| C-30 | **PASS** | Consolidated block names both properties × both locations in one declaration; symmetric across B-01/B-02 blocks |

**Aspirational pass:** 22 / 22

| Tier | Pts |
|------|-----|
| Essential | 60.00 |
| Recommended | 30.00 |
| Aspirational | 22/22 × 10 = **10.00** |
| **Total** | **100.00** |

---

## Composite Scores and Ranking

| Rank | Variation | Essential | Recommended | Aspirational | **Total** |
|------|-----------|-----------|-------------|--------------|-----------|
| 1 | V-02 | 60.00 | 30.00 | 10.00 (22/22) | **100.00** |
| 1 | V-05 | 60.00 | 30.00 | 10.00 (22/22) | **100.00** |
| 3 | V-01 | 60.00 | 30.00 | 9.55 (21/22) | **99.55** |
| 3 | V-03 | 60.00 | 30.00 | 9.55 (21/22) | **99.55** |
| 5 | V-04 | 60.00 | 30.00 | 8.18 (18/22) | **98.18** |

---

## Discrimination Analysis

**C-28 gap (V-01) vs C-29 gap (V-03):** Equal score penalty (−0.45 pts each). However the failure modes are structurally distinct:

- **C-28 failure** is local — the placeholder `B-[ID]` is in the per-block hint only; the preamble dual-location contract is intact. A reader can still verify dual-location compliance from the global contract even if the per-block example is generic.
- **C-29 failure** is gating — without the explicit scaffold completeness declaration, per-block Evidence evaluation is conditionally sound only if the reader infers the scope from context. The named gate is what makes "ALL B-NN blocks" a structural invariant rather than an inference.

C-29 failure is therefore structurally riskier than C-28 failure at the same score cost.

**V-04 cascade:** Four criteria fall together from a single C-27 root failure. The depth-4 chain (C-22→C-26→C-27→C-28) means the locality invariant declaration is the load-bearing gate for the entire R5–R8 aspirational accumulation. This is the highest-leverage single failure point in the rubric.

---

## Excellence Signals (from V-02 and V-05)

**SIGNAL 1 — Instantiated B-ID in per-block format line**
Both V-02 and V-05 carry `causal source: B-01` in B-01's per-block hint and `causal source: B-02` in B-02's hint. The generic `B-[ID]` placeholder (V-01) underspecifies the owning block. The instantiated form removes ambiguity: the reader can confirm the per-block hint cites the block it belongs to, not an arbitrary B-ID.

**SIGNAL 2 — Scaffold completeness as a named gate, not an inference**
The sentence "SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field" before B-01 creates a discrete pass/fail gate. V-03 shows the cost of its absence: individual B-NN blocks may carry Evidence fields and still not satisfy C-29 because the scope declaration (`ALL B-NN`) is what the criterion scores. The gate sentence is not derivable from the per-block language alone.

**SIGNAL 3 — Dual-location requirements under one consolidated header**
Both V-02 and V-05 carry a named `DUAL-LOCATION REQUIREMENTS:` header that lists both locality properties (concrete domain example; labeled axes) and both locations (global preamble; each B-NN block) in a single declaration block. V-04 demonstrates the cascade risk: when this block is absent, C-28, C-29, and C-30 all fail together because their shared predicate — the locality invariant — is missing.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-block Required format instantiates owning B-ID (B-01 or B-02) rather than retaining generic B-[ID] bracket placeholder", "scaffold completeness declared as an explicit named gate before B-01 block — ALL B-NN scope is a structural invariant, not an inference from per-block language", "dual-location requirements consolidated under one named header listing both locality properties at both locations, making C-28+C-29+C-30 a single evaluable block rather than three independently hunted criteria"]}
```
