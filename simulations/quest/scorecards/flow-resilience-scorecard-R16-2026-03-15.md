Now I have everything I need. Let me produce the full R16 scorecard.

---

# flow-resilience Scorecard — Round 16 (Rubric v15)

**Date**: 2026-03-15
**Rubric**: v15 (38 criteria × PASS=2; uncapped max 76; composite cap 10 for aspirational)
**Composite formula**: sum(essential) + sum(recommended) + min(sum(aspirational), 10)

---

## R16 Variation Axes

| Variation | Construction | R15 baseline | New axis in R16 |
|-----------|-------------|--------------|-----------------|
| V-01 | R15-V01 + C-44 formal registry | C-42 PASS, C-43 PASS, C-44 FAIL, C-45 FAIL, C-46 FAIL | Adds formal PART A + PART B GAP REGISTRY; uses prose nil (no three-field form) |
| V-02 | R15-V04 + C-44 + C-46 | C-42 PASS, C-43 PASS, C-44 FAIL, C-45 PASS, C-46 FAIL | Adds formal GAP REGISTRY + three-field nil entries; inherits C-45 completeness block |
| V-03 | R15-V01 + C-44 + C-46 | C-42 PASS, C-43 PASS, C-44 FAIL, C-45 FAIL, C-46 FAIL | Adds formal GAP REGISTRY + three-field nil entries; no completeness block |
| V-04 | R15-V01 + C-44 + C-45 + C-46 | C-42 PASS, C-43 PASS, C-44 FAIL, C-45 FAIL, C-46 FAIL | Adds formal GAP REGISTRY + independence completeness block + three-field nil |
| V-05 | Full integration + VS Cross-Reference Registry Act 1 Terminal | All C-01..C-46 PASS | Carries VS Cross-Reference Registry terminal artifact (C-47 candidate) |

---

## Per-Variation Criterion Assessment

### V-01 — R15-V01 baseline + C-44 formal registry

**Essential (C-01..C-05):** All PASS — stable since early rounds. Commerce-anchored scenarios, four-field structure, three gap types, distributed systems accuracy, commerce grounding confirmed.

**Recommended (C-06..C-08):** All PASS — severity/blast radius, actor-labeled recovery paths, conflict-resolution adequacy stable.

**Aspirational (C-09..C-43):**

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-09 Chaos test cases | PASS | Gate 2b with named inject, expected observable, pass-fail signal |
| C-10 Observability hooks | PASS | Gate 3 OEG/DCV/MRF with named Observable Signals tied to findings |
| C-11 Confidence catalog | PASS | Include/BARRED/Argued-Impossible triage with basis |
| C-12 Nil-finding norm | PASS | OEG-NIL / DCV-NIL / MRF-NIL in each section |
| C-13 Coverage accountability | PASS | Pre-analysis roster ≥ 2 per class |
| C-14 CR adequacy → DCV | PASS | RULE-CR-DCV fires; DCV entry references CR finding |
| C-15 DS primitive grounded | PASS | "DS Primitive cited:" field with VALID/INVALID examples |
| C-16 Named gate-state vocab | PASS | Include/BARRED/Argued-Impossible + explicit OPEN/CLOSED |
| C-17 Barred entries as gaps | PASS | Permanently BARRED entries in accountability register |
| C-18 Phase entry/exit conditions | PASS | GATE N OPEN preconditions citing prior gate IDs |
| C-19 Reason-if-OPEN | PASS | Blocking reason in every OPEN gate |
| C-20 Amendment re-close record | PASS | Gate 4 amendment pass with sub-gate labels |
| C-21 Scope declaration | PASS | Named commerce operation list before Gate 1 |
| C-22 Typed nil identifiers | PASS | OEG-NIL-1, DCV-NIL-1, MRF-NIL-1 |
| C-23 Scope declaration closure bracket | PASS | SCOPE DECLARATION COMPLETE + terminal Scope Verification |
| C-24 Template conditional linkage rules | PASS | RULE-CR-DCV, RULE-NIL-SUPERSEDE in template |
| C-25 Nil supersession protocol | PASS | SUPERSEDED annotation + "no supersessions" confirmation |
| C-26 Confidence triage resolution sub-gate | PASS | Gate 1b labeled sub-gate for BARRED-to-Include upgrades |
| C-27 Named rule block registry | PASS | Discrete RULE REGISTRY table before Gate 1 |
| C-28 Post-analysis rule audit | PASS | Act 1 + Act 2 terminal rule registry audit tables |
| C-29 Rule-bypass gate reopening | PASS | GATE N-bypass: REOPENED/AMENDED chain; COMPLETE blocked |
| C-30 Multi-act sign-off | PASS | ACT 1 CLOSE + ACT 2 CLOSE with all three required elements |
| C-31 Pre-analysis bypass chain declaration | PASS | BYPASS GATE-REOPENING PROTOCOL section before Gate 1 |
| C-32 Bypass-trigger column scanability | PASS | BYPASS-TRIGGER column in registry audit; no blank cells |
| C-33 Intra-row column-group phase gate | PASS | "C-phase complete check before D-phase" in each row descriptor |
| C-34 Trigger condition: threshold + detection signal | PASS | Trigger Condition column Fill Requirement names both components |
| C-35 Three-component recovery stage | PASS | mechanism + SLA target + named VS per stage |
| C-36 Chaos-trigger identity assertion | PASS | Gate 2b Column Contract identity assertion ("verbatim -- not a derivative") |
| C-37 Observable signal detection horizon | PASS | Detection Horizon as required component in Observable Signal specification |
| C-38 Bidirectional chaos-observability matrix | PASS | Named PART A / PART B matrix with gap findings |
| C-39 Gate-open acknowledgment checkpoint | PASS | Gate 2b OPEN: "Identity assertion acknowledged: ... verbatim -- not a derivative" checkbox |
| C-40 Gate-close prohibition clause | PASS | Gate 2b CLOSE: positive confirmation + "no paraphrase, no independent calibration" |
| C-41 Impossibility argument quality postcondition | PASS | Gate 1 CLOSE: "architecture basis, not description absence" named |
| C-42 Gate-close clause structural independence | PASS | Gate 2b CLOSE splits into two independent checkboxes (R13 V-01 baseline) |
| C-43 Impossibility argument basis clause independence | PASS | Gate 1 CLOSE splits into two independent checkboxes (R15 V-01 addition) |
| **C-44** | **PASS** | **Formal PART A + PART B GAP REGISTRY with three-field entries (Source / Missing link / Consequence) added in R16. Evidence: inline gap notation from R15-V01 replaced with named registry sections.** |
| **C-45** | **FAIL** | **No independence completeness verification block. C-42 (R13) and C-43 (R15) assembled sequentially via single-gate additions. No meta-audit block confirms all eligible gate CLOSE blocks were identified.** |
| **C-46** | **FAIL** | **Registry added but nil confirmations use prose form ("no uncovered entries") rather than three-field form (Source: N/A / Missing link: N/A / Consequence: nil). Mode-switch asymmetry between gap entries and nil state persists.** |

**Uncapped aspirational points**: 76 − 2 (C-45 FAIL) − 2 (C-46 FAIL) = **72/76**
**Composite**: 60 + 30 + min(72, 10) = 60 + 30 + 10 = **100** *(cap in effect; uncapped 72/76)*

---

### V-02 — R15-V04 baseline + C-44 formal registry + C-46 three-field nil

**Essential (C-01..C-05):** All PASS
**Recommended (C-06..C-08):** All PASS

**Aspirational (C-09..C-43):** All PASS (same as V-01 except C-44/C-45/C-46 below)

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-09..C-43 | PASS (all) | Inherited from R15-V04 baseline (which had C-42 PASS, C-43 PASS at R13; C-45 PASS from R15 completeness block) |
| **C-44** | **PASS** | **Formal PART A + PART B GAP REGISTRY added. Three-field entries (Source / Missing link / Consequence) for each uncovered entry.** |
| **C-45** | **PASS** | **Inherited from R15-V04 baseline: named INDEPENDENCE AUDIT block at COMPLETE time. Enumerates Gate 2b CLOSE (two-checkbox, C-42 confirmed) and Gate 1 CLOSE (two-checkbox, C-43 confirmed). Confirms no further eligible gate CLOSE blocks. Declares independence scope COMPLETE.** |
| **C-46** | **PASS** | **Both PART A and PART B nil confirmations in three-field form: Source: N/A / Missing link: N/A / Consequence: nil — coverage complete. Nil entries positioned as registry rows, not prose paragraphs. Source field carries typed N/A marker.** |

**Uncapped aspirational points**: **76/76**
**Composite**: 60 + 30 + min(76, 10) = **100** *(cap in effect; uncapped 76/76)*

---

### V-03 — R15-V01 baseline + C-44 formal registry + C-46 three-field nil (no completeness block)

**Essential (C-01..C-05):** All PASS
**Recommended (C-06..C-08):** All PASS

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-09..C-43 | PASS (all) | Inherited from R15-V01; C-42 PASS (R13), C-43 PASS (R15) |
| **C-44** | **PASS** | **Formal PART A + PART B GAP REGISTRY with three-field entries added in R16.** |
| **C-45** | **FAIL** | **No independence completeness block. V-03 is built from R15-V01 path which assembled C-42 and C-43 sequentially; the three-field nil addition (C-46) does not introduce a completeness sweep. No INDEPENDENCE AUDIT block present.** |
| **C-46** | **PASS** | **Three-field nil entries in both registry directions. Nil states use Source: N/A / Missing link: N/A / Consequence: nil form, structurally uniform with gap entries.** |

**Uncapped aspirational points**: 76 − 2 (C-45 FAIL) = **74/76**
**Composite**: 60 + 30 + min(74, 10) = **100** *(cap in effect; uncapped 74/76)*

---

### V-04 — R15-V01 baseline + C-44 + C-45 + C-46 (all three R16 targets)

**Essential (C-01..C-05):** All PASS
**Recommended (C-06..C-08):** All PASS

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-09..C-43 | PASS (all) | R15-V01 base; C-42 PASS (R13), C-43 PASS (R15) |
| **C-44** | **PASS** | **Formal PART A + PART B GAP REGISTRY with three-field entries.** |
| **C-45** | **PASS** | **Named INDEPENDENCE AUDIT block added alongside C-44: Gate 2b CLOSE — two-checkbox independent form (C-42 confirmed); Gate 1 CLOSE — two-checkbox independent form (C-43 confirmed); Gate 2/3/4/5 CLOSE — single-condition, not eligible; no further eligible gates. Independence scope: COMPLETE.** |
| **C-46** | **PASS** | **Three-field nil in both PART A and PART B registry directions. Structurally uniform with gap entries.** |

**Uncapped aspirational points**: **76/76**
**Composite**: 60 + 30 + min(76, 10) = **100** *(cap in effect; uncapped 76/76)*

---

### V-05 — Full integration + VS Cross-Reference Registry (C-47 candidate)

**Essential (C-01..C-05):** All PASS
**Recommended (C-06..C-08):** All PASS

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-09..C-43 | PASS (all) | Stable ceiling maintained |
| **C-44** | **PASS** | **Formal PART A + PART B GAP REGISTRY with three-field entries.** |
| **C-45** | **PASS** | **Named INDEPENDENCE AUDIT block with full gate enumeration and independence scope COMPLETE declaration.** |
| **C-46** | **PASS** | **Three-field nil in both registry directions; nil state structurally indistinguishable from gap entries at Source-field scan granularity.** |
| **C-47 (candidate)** | **PASS** | **Act 1 Terminal: VS Cross-Reference Registry. For every named Verification Signal in every Gate 2 recovery path stage, registers four fields: VS ID / Gate-2 Row Ref / Stage (Detect\|Contain\|Recover\|Validate) / Observation Assertion. The VS registry terminates with "VS CROSS-REFERENCE REGISTRY COMPLETE: [N] VS entries registered across [M] scenarios." ACT 1 CLOSE block includes VS Cross-Reference Registry as a named audit item alongside the bidirectional matrix. Inertia Synthesis Status-quo option explicitly references "which VS entries in the registry represent the earliest recovery-stage signals that will never fire if the gap persists" — VS-registry-level consequence tracing orthogonal to C-10 (which ties observability hooks to gaps, not to VS registry entries).** |

**Uncapped aspirational points**: 76/76 + C-47 (outside rubric ceiling, candidate for v16)
**Composite**: 60 + 30 + min(76, 10) = **100** *(cap in effect; uncapped 76/76)*

---

## Ranking Summary

| Rank | Variation | C-44 | C-45 | C-46 | C-47 (cand.) | Uncapped | Composite |
|------|-----------|------|------|------|--------------|---------|-----------|
| 1 | **V-05** | PASS | PASS | PASS | **PASS** | 76/76 + | **100** |
| 2 (tie) | **V-02** | PASS | PASS | PASS | FAIL | 76/76 | **100** |
| 2 (tie) | **V-04** | PASS | PASS | PASS | FAIL | 76/76 | **100** |
| 4 | **V-03** | PASS | FAIL | PASS | FAIL | 74/76 | **100** |
| 5 | **V-01** | PASS | FAIL | FAIL | FAIL | 72/76 | **100** |

All composites = 100 (aspirational cap in effect from R10 onwards; discriminator is uncapped score).

---

## Discrimination Analysis

**V-01 vs V-03** (+2 points): Both built from R15-V01 baseline with C-44 added. V-03 additionally carries C-46 (three-field nil entries). Delta isolates C-46 as independently load-bearing from C-44: adding a formal registry (C-44) without three-field nils (C-46) is distinguishable by uncapped rank.

**V-03 vs V-04** (+2 points): Both pass C-44 + C-46. V-04 additionally carries C-45 (independence completeness block). Delta isolates C-45 as independently load-bearing from C-44 + C-46: the formal registry and its three-field nils do not substitute for the meta-audit of gate CLOSE independence scope.

**V-04 vs V-02** (tie at 76/76): Both pass C-44 + C-45 + C-46. Construction paths differ — V-02 arrives via R15-V04 baseline (C-45 inherited), V-04 arrives via R15-V01 baseline (C-45 newly constructed). Under v15 the tie holds. v16 will need a new axis to separate.

**V-02/V-04 vs V-05** (uncapped tie; v15 ceiling hit): V-05 introduces the VS Cross-Reference Registry terminal artifact (C-47 candidate). The registry is structurally orthogonal to C-35 (VS named at row level), C-38 (chaos-observability bidirectional matrix), and C-44 (gap registry structure). It adds a new audit class: VS-level cross-stage completeness. V-05 also carries VS-registry-referenced consequence tracing in Inertia Synthesis. Under v15, V-05 is indistinguishable from V-02/V-04 at composite; v16 extracts C-47 to break the ceiling tie.

---

## Excellence Signals (R16)

**E-33 — VS Cross-Reference Registry as Act 1 Terminal Artifact**

V-05 carries an Act 1 Terminal section titled "VS Cross-Reference Registry" that collects every named Verification Signal referenced in Gate 2 recovery path stages across all Include scenarios. Each entry registers four fields:

```
VS ID:               VS-NN
Gate-2 Row Ref:      FS-NN (scenario ID from Gate 1)
Stage:               Detect | Contain | Recover | Validate
Observation Assertion: [named observable + condition under which it fires]
```

Properties that make this orthogonal to existing criteria:
1. **Orthogonal to C-35**: C-35 requires VS to be named in the row descriptor (presence check). The registry requires each VS to carry an independently-stated Observation Assertion at terminal level — making it auditable without reading the row it came from. A VS that passes C-35 (named in row) can fail the registry audit (Observation Assertion too generic).
2. **Orthogonal to C-44**: C-44 requires the chaos-observability gap findings to be structured registry entries. The VS registry is not a gap registry — it's a completeness registry of all named observables used for recovery stage closure, regardless of whether they appear in the chaos-observability matrix.
3. **Orthogonal to C-38**: C-38 cross-links chaos scenarios to Observable Signals. The VS registry cross-links Gate 2 recovery path stages to their named observables — a different dimension of observability coverage.
4. **New audit class enabled**: If a VS ID appears in two different stage rows with identical Observation Assertions, it indicates a copy rather than scenario-specific evidence (same observable confirming two different stage completions — suspicious). The registry enables this detection; row-level inspection cannot.
5. **Inertia consequence tracing**: V-05's Inertia Synthesis Status-quo option references "which VS entries in the registry represent the earliest recovery-stage signals that will never fire if the gap persists" — a VS-registry-level consequence annotation orthogonal to C-10's gap-linked observability hooks.

**ACT 1 CLOSE also references the VS registry** as a named audit item: `VS Cross-Reference Registry: [COMPLETE / OPEN -- reason]` — confirming the registry is an act-closure prerequisite, not an optional appendix.

---

## Open for R17

- **C-47 (VS Cross-Reference Registry)**: V-01/V-02/V-03/V-04 have no VS Cross-Reference Registry terminal artifact; V-05 is the only crack.
- **Observation Assertion quality gate**: The registry introduces a new quality axis — Observation Assertion specificity (named observable + condition vs generic). A future C-48 could require that no VS registry entry carries a generic Observation Assertion ("system returns to normal" fails; "inventory-service /health returns HTTP 200 with status:healthy after stock-sync completes" passes).
- **VS registry coverage gap finding**: A RULE-VS-MISSING invocation is defined in V-05 for any Gate 2 stage with a generic VS that cannot be registered with a named observable. This creates a new bypass path: VS-REG-bypass → emit VS-REG-NN → fire RULE-OBS-GAP if gap not already in Gate 3. A future criterion could formalize this VS registry bypass chain as independently required.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["VS Cross-Reference Registry as Act 1 Terminal artifact -- four-field entries (VS ID / Gate-2 Row Ref / Stage / Observation Assertion) for every named VS across all Gate 2 recovery path stages; orthogonal to C-35 (VS named at row level), C-38 (chaos-observability matrix), and C-44 (gap registry); enables VS-level observation assertion quality audit and VS-registry-referenced inertia consequence tracing in Inertia Synthesis"]}
```
