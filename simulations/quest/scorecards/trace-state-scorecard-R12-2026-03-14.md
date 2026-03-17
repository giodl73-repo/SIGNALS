# trace-state Quest Score — Round 12

## Variation Scoring

### V-01: Output Format — Three Separate ID Columns

**Target**: C-17

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | PART 2 template has Before state / After state per step |
| C-02 | PASS | Preconditions checked + Postconditions verified in every step slot |
| C-03 | PASS | INV-ID registry in 1C with falsifiable threshold requirement |
| C-04 | PASS | Five-phase sweep drives anomaly discovery |
| C-05 | PASS | Sales / Customer Service / Finance domain selection |
| C-06 | PASS | `[REJECTED]` step required; rejection immutability constraint (C-39) |
| C-07 | PASS | Step N: numbered sequential trace |
| C-08 | PASS | Phase 3D race condition sweep |
| C-09 | PASS | All four anomaly types (3A–3D) + undeclared references (3E) |
| C-10 | PASS | State Registry table + Operation Registry table |
| C-11 | PASS | Sweep table with row-level verdicts |
| C-12 | PASS | OP-ID cross-referenced in declaration and trace |
| C-13 | PASS | Entry Condition column in 1A State Registry |
| C-14 | PASS | Minimum-found threshold (evidence strength gate per phase) |
| C-15 | PASS | S-IDs, OP-IDs, INV-IDs all declared and cross-referenced |
| C-16 | PASS | Phase 3E elevated as fifth anomaly class |
| C-17 | **PASS** | Three separate OP-ID / S-ID / INV-ID columns; blank cell in found-verdict row = detectable structural gap |
| C-18 | PASS | PART 3 pre-sweep hypothesis table locked before sweep |
| C-19 | PASS | Evidence strength gate per phase (≥ 1 at strength ≥ 2 OR Gap Record explains) |
| C-20 | PASS | 1C requires at least one numeric or temporal invariant with falsifiable threshold |
| C-21 | **FAIL** | No PART 5 reconciliation; no Surprise column |
| C-22 | PASS | Scoring protocol: "I am scoring this [1/2/3] because [reference]" at point of discovery |
| C-23 | PASS | Score-aloud self-correction gate: incomplete sentence = not recordable |
| C-24 | PASS | Phase exit certification checkboxes as hard gates |
| C-25 | **FAIL** | No C/FP/FN taxonomy; no calibration score |
| C-26 | PASS | Five numbered top-level phases in sequential lock chain |
| C-27 | PASS | Acquittal naming: "name the specific (OP-ID, S-ID) pairs you examined and why each cleared" |
| C-28 | PASS | Dual-mode: Pass 1 Declaration-Only + Pass 2 Trace-Diff |
| C-29 | PASS | Role B Acquittal Advocate unconditional per phase |
| C-30 | PASS | Parallel dual-column finding table (Declaration-Only Finding / Trace-Diff Finding) |
| C-31 | PASS | LOCKED/OPEN status labels + PHASE N: COMPLETE unlock signal |
| C-32 | PASS | Role B fires on every phase regardless of finding count |
| C-33 | PASS | Symmetric output contract: findings + Gap Record per phase |
| C-34 | PASS | "The Gap Record is the unlock signal for the Phase exit gate" |
| C-35 | PASS | Pre-detection commitment: verbatim restate of PART 0 registry row before passes begin |
| C-36 | **PARTIAL** | Phase 3E abbreviated in a paragraph; structural elements referenced but not written out as explicit slots |
| C-37 | PASS | Evidence strength threshold as named exit gate checkbox |
| C-38 | PASS | PART 0 Standards Registry sealed before PART 1; "STANDARDS REGISTRY: SEALED" declaration |
| C-39 | PASS | REJECTED step template: "entity must remain in its before-state after rejection... any deviation is a detectable anomaly" |

**Score**: 98.97 + 0.323 (C-17 FAIL→PASS) = **99.29**

---

### V-02: Lifecycle Emphasis — Phase 3E Fully Expanded

**Target**: C-36

| Criterion | Delta | Evidence |
|-----------|-------|----------|
| C-17 | FAIL | Combined `OP-ID / S-ID affected` column — no 3-column split |
| C-21 | FAIL | No PART 5 |
| C-25 | FAIL | No PART 5 |
| C-36 | **PASS** | Phase 3E written with complete expanded template: explicit Role B pre-detection verbatim commitment, THE SCORING PROTOCOL written out with self-correction gate, Pass 1 with systematic cross-reference scan instructions per cell type, Pass 2 with per-step trace audit, Finding Table with inline "None requires explanation" annotation, Role B Gap Record [UNCONDITIONAL] with structured field template, Phase 3E Exit Certification with three named checkbox gates |
| All others | PASS | Unchanged from R11 baseline |

**Score**: 98.97 + 0.323 (C-36 PARTIAL→PASS) = **99.29**

---

### V-03: Role Sequence — Post-Sweep Reconciliation

**Target**: C-21 + C-25

| Criterion | Delta | Evidence |
|-----------|-------|----------|
| C-17 | FAIL | Combined ID column |
| C-21 | **PASS** | PART 5 Reconciliation Table has `Surprising? (E / S)` column with E (Expected) / S (Surprising) classification per prediction row |
| C-25 | **PASS** | Three-value C/FP/FN taxonomy fully defined; Calibration Score = (C outcomes) / total rows; <60% threshold triggers 3-step structural diagnosis: (1) name FP-heavy vs FN-heavy types, (2) identify bias mechanism (confirmation / anchoring / scope-tunnel), (3) state concrete improvement |
| C-36 | PARTIAL | Phase 3E abbreviated in V-03 ("Apply complete phase mechanics: ...→ Phase 3E Exit Certification") — structural elements named but not written as independent slots |
| All others | PASS | Unchanged |

**Score**: 98.97 + 2×0.323 (C-21, C-25) = **99.62**

---

### V-04: Compound — Output Format + Lifecycle Emphasis

**Target**: C-17 + C-36

| Criterion | Delta | Evidence |
|-----------|-------|----------|
| C-17 | **PASS** | Three separate OP-ID / S-ID / INV-ID columns in all finding tables including Phase 3E; blank cell rule stated |
| C-21 | FAIL | No PART 5 |
| C-25 | FAIL | No PART 5 |
| C-36 | **PASS** | Phase 3E fully expanded with every structural element written out: Role B pre-detection verbatim commitment, score-aloud protocol with cross-reference-specific sentence template, Pass 1 systematic scan, Pass 2 per-step scan, Finding Table with "None requires inline explanation" note, Role B Gap Record [UNCONDITIONAL] with five named fields, Phase 3E Exit Certification three-gate |
| All others | PASS | Unchanged |

**Score**: 98.97 + 2×0.323 (C-17, C-36) = **99.62**

---

### V-05: Compound — All Four Gaps + Conversational Register

**Target**: C-17 + C-21 + C-25 + C-36

| Criterion | Delta | Evidence |
|-----------|-------|----------|
| C-17 | **PASS** | Three separate OP-ID / S-ID / INV-ID columns in all five finding tables; "Use `—` only when genuinely not applicable (explain why)" |
| C-21 | **PASS** | PART 5 Reconciliation Table `E / S` column per prediction row; "E (Expected) / S (Surprising)" with definitions |
| C-25 | **PASS** | C/FP/FN taxonomy; Calibration Score = (C count) / 5; <60% diagnosis requires naming FP-heavy vs FN-heavy, naming bias type from four-type taxonomy (confirmation / anchoring / scope-tunnel / domain-blind), stating what to change in hypothesis practice |
| C-36 | **PASS** | Phase 3E fully expanded with: Role B verbatim restate, score-aloud rule with registry-specific sentence template, Pass 1 systematic cell-by-cell cross-reference scan (four specific check types listed), Pass 2 per-step + per-prior-finding-table audit, Finding Table with three separate ID columns + "None needs inline explanation", Role B Gap Record [UNCONDITIONAL] with cell-counting audit template, three-gate exit certification, PHASE 3E: COMPLETE → PART 5 now OPEN |
| C-38 | PASS | PART 0: "Once you declare 'SEALED,' you cannot touch it again — not at phase entry, not after you see a finding" — pre-game commitment framing preserved |
| C-39 | PASS | REJECTED step: "It must match the before-state field-for-field — the entity doesn't move when rejected. If it does move, that's a finding, not a valid rejection." |
| All others | PASS | Conversational register preserves every structural element; no regression detected |

**V-05 Excellence Signals:**

1. **Cell-counting audit contract in Phase 3E Gap Record** — the Gap Record template requires explicit counts of cells checked per registry: `1A: N states × 2 columns = N cells checked`, `1B: N operations × Valid From + Valid To = N ID references`, `1C: N invariants × Scope field = N references`. Converts coverage claims from qualitative ("I scanned the registries") to countable audit facts.

2. **Domain-blind as fourth calibration bias type** — V-05 extends C-25's bias taxonomy from three types (confirmation, anchoring, scope-tunnel) to four by adding `domain-blind (missing knowledge about the domain's real failure modes)`. This targets a failure mode orthogonal to the procedural biases: the model searches correctly but in the wrong places because it does not know where the domain's failure modes actually live.

3. **Conversational first-person imperative register** — instructions reframed as direct imperatives ("lock your standard now", "grade yourself") reduce parsing friction on complex mechanics without removing any structural slot. Evidence that register choice affects compliance on high-constraint multi-role protocols.

**Score**: 98.97 + 4×0.323 = 100.26 → capped at **100.00**

---

## Rankings

| Rank | Variation | Score | Gaps Closed |
|------|-----------|-------|-------------|
| 1 | **V-05** | **100.00** | C-17, C-21, C-25, C-36 |
| 2 | V-03 | 99.62 | C-21, C-25 |
| 2 | V-04 | 99.62 | C-17, C-36 |
| 4 | V-01 | 99.29 | C-17 |
| 4 | V-02 | 99.29 | C-36 |

V-03 and V-04 tie at 99.62. V-04 is the preferred base for the next rubric version if C-21/C-25 need further refinement, because it locks the structural output format (3 columns + full Phase 3E) which is prerequisite to PART 5 being auditable. V-03 adds PART 5 without fixing the output format — the reconciliation table works but the ID columns in the sweep phases remain combined.

V-05 is the 100/100 candidate. No regression on any passing criterion. Conversational register confirmed non-destructive.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Cell-counting audit contract in Phase 3E Gap Record — requires explicit counts of cells checked per registry section (N states x 2 columns = N cells) making gap coverage quantifiable and auditable", "Domain-blind as fourth calibration bias type in PART 5 diagnostic — targets missing domain knowledge about where real failure modes live, orthogonal to the procedural biases of confirmation anchoring and scope-tunnel"]}
```
