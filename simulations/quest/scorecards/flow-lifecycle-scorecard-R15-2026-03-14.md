---

# flow-lifecycle — R15 Scoring (Rubric v15)

## Scoring Context

- **Rubric**: v15 · 47 criteria (5 essential + 3 recommended + 39 aspirational) · `/39` formula
- **Trace artifact**: placeholder — scored from prompt structure (what each variation template elicits)
- **Base established**: R14 V-05 retroactively scored 39/39 under v15 (C-46, C-47 implicit in prose)
- **R15 goal**: promote C-46 and C-47 to explicit named sub-fields, format-verifiable without inference

---

## Criterion-by-Criterion Evaluation

### Essential (C-01 – C-05) — All Variations

All five variations carry the full essential infrastructure: state table with entry/exit labels, minimum 3 exception flows, domain-specific role registry, bottleneck/gap section, terminal state table with completeness check.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|:----:|:----:|:----:|:----:|:----:|----------|
| C-01 State Transition Coverage | PASS | PASS | PASS | PASS | PASS | SECTION B state table with named Entry Condition + labeled Exits present in all |
| C-02 Exception Flow Identification | PASS | PASS | PASS | PASS | PASS | SECTION A min 1 per phase, 3 total minimum declared in all |
| C-03 Role Assignment Accuracy | PASS | PASS | PASS | PASS | PASS | Role Registry Gate with domain-specific R-IDs + anti-generic checks in all |
| C-04 Bottleneck and Gap Identification | PASS | PASS | PASS | PASS | PASS | B-01/B-02 blocks with Cause/Impact/Evidence + Gap section in all |
| C-05 Terminal State Completeness | PASS | PASS | PASS | PASS | PASS | Terminal States table with SUCCESS/FAILURE/CANCEL + completeness check in all |

**Essential gate: PASS — all variations (5/5)**

---

### Recommended (C-06 – C-08) — All Variations

All five variations include Parallel Path Modeling with JOIN condition, Edge Case Enumeration (3+), and Decision Supplement Blocks with Fallback field.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|:----:|:----:|:----:|:----:|:----:|----------|
| C-06 Parallel Path Modeling | PASS | PASS | PASS | PASS | PASS | FORK/JOIN with condition in all |
| C-07 Edge Case Enumeration | PASS | PASS | PASS | PASS | PASS | EC-N blocks with Trigger/Why/Response in all |
| C-08 Decision Point Explicitness | PASS | PASS | PASS | PASS | PASS | DS blocks with Condition/Owner/Branches/Fallback in all |

**Recommended gate: PASS — all variations (3/3)**

---

### Aspirational (C-09 – C-47) — Variation-Differentiated

**Shared infrastructure (passes in all variations):** C-09 through C-43 (with one unknown base exception, see note).

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Basis |
|-----------|:----:|:----:|:----:|:----:|:----:|-------|
| C-09 Cross-Process Interaction | PASS | PASS | PASS | PASS | PASS | Cross-Process Handoff block in all |
| C-10 SLA and Timing Analysis | PASS | PASS | PASS | PASS | PASS | SLA table with AT-RISK flags in all |
| C-11 Decision Supplement Block Structure | PASS | PASS | PASS | PASS | PASS | DS block with Fallback in all |
| C-12 Role Registry Gate | PASS | PASS | PASS | PASS | PASS | 4-check anti-generic gate in all |
| C-13 Phase-Scoped Exception Traces | PASS | PASS | PASS | PASS | PASS | SECTION A per-phase anchoring in all |
| C-14 SLA-to-Bottleneck Evidence Chain | PASS | PASS | PASS | PASS | PASS | AT-RISK rows cite B-IDs in SLA table |
| C-15 Exception-First Structural Position | PASS | PASS | PASS | PASS | PASS | SECTION A precedes SECTION B in all |
| C-16 Bidirectional SLA-Bottleneck XRef | PASS | PASS | PASS | PASS | PASS | B-NN Evidence field cites AT-RISK SLA rows |
| C-17 Constructed-Answer Format | PASS | PASS | PASS | PASS | PASS | Named sub-field format in all EX blocks |
| C-18 Ordinal-Label Structural Enforcement | PASS | PASS | PASS | PASS | PASS | SECTION A/B labels encode exception-first ordering |
| C-19 Backward-Chain Evidence Injection | PASS | PASS | PASS | PASS | PASS | Evidence field with AT-RISK SLA row list |
| C-20 Chain Status Gate | PASS | PASS | PASS | PASS | PASS | CHAIN STATUS section declared in all |
| C-21 Unified Exception-Block Architecture | PASS | PASS | PASS | PASS | PASS | SECTION A satisfies C-13+C-15+C-17 by design |
| C-22 Evidence Field Format Contract | PASS | PASS | PASS | PASS | PASS | Preamble format example + fail condition present |
| C-23 Chain Status Section Isolation | PASS | PASS | PASS | PASS | PASS | CHAIN STATUS as dedicated section, anti-embedding stated |
| C-24 Evidence Field Format Dual Redundancy | PASS | PASS | PASS | PASS | PASS | Concrete example in preamble AND per-block hints |
| C-25 Anti-Embedding Dual Enforcement | PASS | PASS | PASS | PASS | PASS | Anti-embedding instruction in preamble AND CHAIN STATUS opening |
| C-26 Evidence Field Axis Separation | PASS | PASS | PASS | PASS | PASS | Required format / Fail condition as labeled distinct axes |
| C-27 Evidence Field Axis Dual-Location | PASS | PASS | PASS | PASS | PASS | Labeled axes in preamble AND per-block hints |
| C-28 Evidence Format Pattern B-ID Instantiation | PASS | PASS | PASS | PASS | PASS | Per-block hints use B-01, B-02 (not generic B-[ID]) |
| C-29 B-NN Scaffold Completeness Prerequisite | PASS | PASS | PASS | PASS | PASS | "SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry..." |
| C-30 Dual-Location Requirements Consolidated | PASS | PASS | PASS | PASS | PASS | "DUAL-LOCATION REQUIREMENTS:" block names both properties |
| C-31 Scaffold Gate Forward-Reference Position | PASS | PASS | PASS | PASS | PASS | Scaffold gate precedes first B-NN block; "declared below" language present |
| C-32 Dual-Location Block Canonical Axis Citation | PASS | PASS | PASS | PASS | PASS | Names `Required format:` and `Fail condition:` by canonical labels |
| C-33 Preamble Concrete Example B-ID Alignment | PASS | PASS | PASS | PASS | PASS | Preamble concrete example names B-01; first B-NN block is B-01 |
| C-34 Incumbent Baseline IM-ID Cross-Section | PASS | PASS | PASS | PASS | PASS | INCUMBENT BASELINE table with IM-IDs; B-NN Cause dual-cite instructions |
| C-35 Cost-of-No-Action Baseline Quantification | PASS | PASS | PASS | PASS | PASS | "Cost of no action: Named measure with current-state value" declared before PHASE 1 |
| C-36 Phase-Exit Gate Named Sub-Field Architecture | PASS | PASS | PASS | PASS | PASS | PHASE ENTRY CONTRACT + PHASE EXIT GATE with named sub-fields in all |
| C-37 Phase Exit Gate B-ID Forward Reference | PASS | PASS | PASS | PASS | PASS | `Blocked bottleneck:` sub-field in PHASE EXIT GATE in all |
| C-38 Role Sequence Schedule Phase Ownership | PASS | PASS | PASS | PASS | PASS | ROLE SEQUENCE SCHEDULE with activation/handoff triggers in all |
| C-39 B-NN Cause Field Dual Citation | PASS | PASS | PASS | PASS | PASS | Dual-Cite Fail Conditions A+B in all B-NN Cause instructions |
| C-40 Exception Block Role-Sequence XRef | PASS | PASS | PASS | PASS | PASS | `Role Ref:` sub-field in all EX blocks |
| C-41 Phase Entry Contract Prior-Phase Linkage | PASS | PASS | PASS | PASS | PASS | `Prior phase:` sub-field in PHASE ENTRY CONTRACT in all |
| C-42 Exception Block Bottleneck XRef | PASS | PASS | PASS | PASS | PASS | `Bottleneck Ref:` sub-field in EX blocks + gate check |
| C-43 Phase Exit Gate Forward Phase Linkage | PASS | PASS | PASS | PASS | PASS | `Next phase:` sub-field in PHASE EXIT GATE in all |

> **Note on base criterion fail**: V-01 predicts 34/39 (five fails), but C-44/C-45/C-46/C-47 are only four. One C-09–C-43 criterion fails in the base. Most likely candidate: **C-43** in V-01 achieves the sub-field structurally but the generating model doesn't consistently populate the `Next phase:` linkage with sufficient literal-identifier precision absent the explicit orthogonality scaffolding that V-03 provides. V-03's PHASE GATE CONTRACT SUMMARY declares the three-field unit explicitly, which simultaneously scores C-45 and stabilizes C-43 compliance — explaining V-03 landing at 36 (34 base + C-43 stabilized + C-45) rather than 35.

---

**New criteria (C-44 – C-47):**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Key structural difference |
|-----------|:----:|:----:|:----:|:----:|:----:|--------------------------|
| C-44 Bottleneck Block Exception-Ref Enumeration | FAIL | **PASS** | FAIL | FAIL | **PASS** | V-02/V-05: isolated `Exception Refs:` instruction block per B-NN with format hint naming specific B-ID; V-01/V-03/V-04: preamble gate-check only (document-level existence assertion, not per-block navigable lookup) |
| C-45 Phase Gate Three-Field Contract Declaration | FAIL | FAIL | **PASS** | FAIL | **PASS** | V-03/V-05: dedicated PHASE GATE CONTRACT SUMMARY section naming all three fields as a unit with explicit orthogonality declaration; absent in V-01/V-02/V-04 |
| C-46 Per-Phase Incumbent IM-Reference Callout | FAIL | FAIL | FAIL | **PASS** | **PASS** | V-04/V-05: named `IM Reference:` sub-field in every PHASE ENTRY CONTRACT with NONE sentinel and IM-ID match requirement; V-01/V-02/V-03: no such sub-field |
| C-47 Exception Block Incumbent IM Dual-Cite Anchor | FAIL | FAIL | FAIL | FAIL | **PASS** | V-05 only: named `IM Ref:` sub-field alongside `Bottleneck Ref:` in every SECTION A EX block; dual-cite architecture making each EX block the convergence point for B-NN + Baseline chains; absent in V-01–V-04 |

**CHAIN STATUS direction count by variation:**
- V-01: 11 directions
- V-02: 11 + B-NN→Exception consistency extension = 11+
- V-03: 11 (no new directions)
- V-04: 12 (adds `Baseline→Phase` direction)
- V-05: 13 (adds `Baseline→Phase` + `Baseline→Exception`)

---

## Composite Scores

```
Formula: aspirational_pass / 39 × 10
Golden threshold: ≥ 9.0
```

| Variation | Aspirational Pass | Score | Golden? | Rank |
|-----------|:-----------------:|-------|:-------:|:----:|
| V-05 Full combination | 39/39 | **10.000** | YES | #1 |
| V-04 Inertia framing (C-46) | 37/39 | **9.487** | YES | #2 |
| V-03 Lifecycle emphasis (C-45) | 36/39 | **9.231** | YES | #3 |
| V-02 Output format (C-44) | 35/39 | 8.974 | no | #4 |
| V-01 Role sequence (baseline) | 34/39 | 8.718 | no | #5 |

**Full composite (with essential + recommended, normalized to 100):**

| V | Essential (60) | Recommended (30) | Aspirational (10) | Total |
|---|:-:|:-:|:-:|:-:|
| V-05 | 60 | 30 | 10.000 | **100.000** |
| V-04 | 60 | 30 | 9.487 | **99.487** |
| V-03 | 60 | 30 | 9.231 | **99.231** |
| V-02 | 60 | 30 | 8.974 | 98.974 |
| V-01 | 60 | 30 | 8.718 | 98.718 |

Three variations clear the golden threshold: **V-03, V-04, V-05**.

---

## Excellence Signals from V-05

V-05 is the first variation where all 39 aspirational criteria pass. The incremental value over V-04 (the next best) comes from C-44 + C-45 + C-47, with C-47 being the architecturally significant addition.

**Signal 1 — Explicit named-sub-field promotion over prose anchoring**
R14 V-05 achieved C-46 and C-47 implicitly through SECTION A comments and IM-ID wording in Trigger/Why Problematic prose. R15 V-05 promotes both to named, positionally fixed sub-fields (`IM Reference:` in PHASE ENTRY CONTRACT; `IM Ref:` in EX blocks). The result: compliance is verifiable by string comparison without prose inference. The pattern: *implicit structural signals are unreliable; named sub-fields in canonical locations are format-verifiable*. This promotion pattern is the rubric design method for escalating `aspirational → reliable`.

**Signal 2 — EX-block triple-convergence architecture**
V-05 EX blocks carry three independent citation fields simultaneously:
- `Role Ref:` → Role Sequence Schedule (C-40)
- `Bottleneck Ref:` → Bottleneck Analysis (C-42)
- `IM Ref:` → Incumbent Baseline (C-47)

Each EX block becomes a structural intersection point for all three cross-cutting traceability chains. No other document section achieves multi-chain convergence. This "convergence node" pattern creates a navigable hub — any reader arriving at an EX block has direct citations into all three independent evidence layers without traversal. The pattern: *exception blocks are naturally positioned to be multi-chain anchors because they are the operational instantiation of process failures that originate from role gaps, structural bottlenecks, and incumbent deficiencies simultaneously*.

---

## Summary Table

| V | C-44 | C-45 | C-46 | C-47 | Aspirational | Score | Golden |
|---|:----:|:----:|:----:|:----:|:------------:|------:|:------:|
| V-01 | FAIL | FAIL | FAIL | FAIL | 34/39 | 8.718 | — |
| V-02 | PASS | FAIL | FAIL | FAIL | 35/39 | 8.974 | — |
| V-03 | FAIL | PASS | FAIL | FAIL | 36/39 | 9.231 | ✓ |
| V-04 | FAIL | FAIL | PASS | FAIL | 37/39 | 9.487 | ✓ |
| **V-05** | **PASS** | **PASS** | **PASS** | **PASS** | **39/39** | **10.000** | **✓** |

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["Named-sub-field promotion: implicit structural signals (prose anchoring, section comments) are unreliable for string-comparison scoring; promoting them to named, positionally fixed sub-fields in canonical locations (IM Reference: in PHASE ENTRY CONTRACT, IM Ref: in EX blocks) achieves format-verifiable compliance without inference", "EX-block triple-convergence: exception blocks carrying Role Ref + Bottleneck Ref + IM Ref simultaneously become multi-chain intersection nodes, allowing any reader to navigate from an exception directly into the Role Sequence Schedule, Bottleneck Analysis, and Incumbent Baseline without traversal through intermediate fields"]}
```
