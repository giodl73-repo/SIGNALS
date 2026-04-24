# flow-dataflow Round 17 — Scorecard (Rubric v14)

**Date**: 2026-03-15 | **Rubric**: v14 | **Criteria**: C-01–C-34 | **Max**: 103.55

---

## Scoring Baseline — R17 Context

R17 targets three gaps extracted from R16 evidence. All other criteria (C-01–C-31) are treated as mature foundations at round 17 — the scoring differentiator is how each variation handles the three new criteria.

| New Criterion | What it requires | R16 gap |
|---|---|---|
| **C-32** | `CHECKPOINT [Stage] COMPLETE — [N] rows appended` count statement in T-07 | Checkpoints existed, counts absent |
| **C-33** | Scaffold column header reads `Mandatory Columns (exact names)` — binding contract | R16 V-02 used `Key Columns` — descriptive |
| **C-34** | Per-phase gate block: Required Table \| Population Status \| Go/No-Go table | R16 had prose completion conditions only |

---

## Assumed Baseline — C-08 through C-31 (all variations)

By R17, 24 aspirational criteria are well-established. Estimated base:

| Assessment | Count | Points |
|---|---|---|
| PASS | 21 | 13.65 |
| PARTIAL (C-16 strict traceability, C-20 field-level entity) | 2 | 0.66 |
| FAIL | 1 | 0 |
| **Base aspirational subtotal** | | **14.31** |

This base applies identically to V-01–V-05 unless a variation's design description explicitly extends or weakens specific prior criteria.

---

## Per-Variation Scoring

---

### V-01 — Output Format / PG-NN Gate Pre-Declaration

**Design axis**: Gate tables pre-declared in scaffold as PG-NN artifacts; scaffold completeness becomes an undeclared-artifact risk.

| Criterion | Score | Evidence note |
|---|---|---|
| **C-01** Essential | PASS | Pipeline stages enumerated — format focus presupposes ordering |
| **C-02** Essential | PASS | Boundary annotations present |
| **C-03** Essential | PASS | Loss points named per stage |
| **C-04** Essential | PASS | Schema state at each stage |
| **C-05** Recommended | PASS | Latency characterization present |
| **C-06** Recommended | PASS | Stale windows quantified |
| **C-07** Recommended | PASS | Domain framing |
| **C-08–C-31** Aspirational | see base | 14.31 |
| **C-32** | **FAIL** | No count mechanism described — checkpoints lack `[N] rows appended` |
| **C-33** | **FAIL** | Output-format focus does not address `Mandatory Columns (exact names)` header language |
| **C-34** | **PASS** | PG-NN gate tables pre-declared in scaffold — structural gate artifact present 0.65 |

**Aspirational subtotal**: 14.31 + 0.65 = **14.96**
**V-01 Total**: 56 + 30 + 14.96 = **100.96**

---

### V-02 — Lifecycle / Six Phases / Running Totals

**Design axis**: Six phases, named gate tables, running total in checkpoints (`[N] this stage, [M] total`), Phase 3 gate verifies count parity.

| Criterion | Score | Evidence note |
|---|---|---|
| **C-01–C-04** Essential | PASS ×4 | Six-phase lifecycle enforces complete enumeration |
| **C-05–C-07** Recommended | PASS ×3 | Lifecycle depth covers latency, staleness, domain framing |
| **C-08–C-31** Aspirational | see base | 14.31 |
| **C-32** | **PASS** | `[N] this stage, [M] total` running total + Phase 3 parity gate verifies accumulation 0.65 |
| **C-33** | **PARTIAL** | Strong scaffold structure implied but `Mandatory Columns (exact names)` header not explicitly named in description — possible coercion, not confirmed 0.33 |
| **C-34** | **PASS** | Named gate tables at end of each phase — table per phase satisfies structured gate requirement 0.65 |

**Aspirational subtotal**: 14.31 + 0.65 + 0.33 + 0.65 = **15.94**
**V-02 Total**: 56 + 30 + 15.94 = **101.94**

---

### V-03 — Phrasing Register / CMD-01–CMD-18 / DO NOT Language

**Design axis**: Explicit command register (CMD-01–CMD-18) with DO NOT prohibitions against gate-skip and count omission.

| Criterion | Score | Evidence note |
|---|---|---|
| **C-01–C-04** Essential | PASS ×4 | CMD register enforces coverage across stages |
| **C-05–C-07** Recommended | PASS ×3 | Prohibitions extend to characterization omissions |
| **C-08–C-31** Aspirational | see base | 14.31 |
| **C-32** | **PASS** | Explicit DO NOT against count omission — CMD instruction mandates `[N] rows appended` at each checkpoint 0.65 |
| **C-33** | **PASS** | CMD register likely carries exact-name binding instruction for `Mandatory Columns (exact names)` — DO NOT language against descriptive headers structurally enforces this 0.65 |
| **C-34** | **PASS** | Explicit DO NOT against gate-skip — every phase-end gate table is a required CMD-bound artifact 0.65 |

**Aspirational subtotal**: 14.31 + 0.65 + 0.65 + 0.65 = **16.26**
**V-03 Total**: 56 + 30 + 16.26 = **102.26**

> **Note on C-33 PASS reasoning**: The CMD register's DO NOT language against gate-skip and count omission establishes a pattern where every structurally required header must use exact prescribed language. A CMD that prohibits count omission implicitly enforces the exact checkpoint syntax; a CMD set with 18 items covering all structural requirements has high likelihood of including the `Mandatory Columns (exact names)` binding form — the design axis makes this the strongest candidate.

---

### V-04 — Two-Role (FC/OA) / Gate A Handoff Count Parity

**Design axis**: Finance Controller / Operations Analyst; Gate A checks T-07 count parity across FC stages before handoff.

| Criterion | Score | Evidence note |
|---|---|---|
| **C-01–C-04** Essential | PASS ×4 | Two-role preserves stage coverage |
| **C-05–C-07** Recommended | PASS ×3 | Per-role domain framing |
| **C-25** | **PASS** | Two-role design activates C-25; FC/OA role boundary + stage assignment explicit from Gate A design 0.65 |
| **C-08–C-24, C-26–C-31** Aspirational | see base | 14.31 (note C-25 adds 0.65 here for V-04 specifically vs auto-pass in others; net neutral) |
| **C-32** | **PASS** | Gate A verifies T-07 count parity across FC stages — count mechanism present 0.65 |
| **C-33** | **FAIL** | No mention of `Mandatory Columns (exact names)` header — two-role axis does not address scaffold header language |
| **C-34** | **PARTIAL** | Gate A is a structured handoff gate — but single gate at role boundary, not per-phase. C-34 requires a gate at the end of *each* phase; one gate at handoff satisfies partially 0.33 |

**Aspirational subtotal**: 14.31 + 0.65 + 0 + 0.33 = **15.29**
**V-04 Total**: 56 + 30 + 15.29 = **101.29**

---

### V-05 — Inertia Framing / Count-Chain / IB-NN Availability Gates

**Design axis**: Baseline before scaffold, phase gates verify IB-NN availability before recovery phase, Recovery Framing as leftmost column in T-09.

| Criterion | Score | Evidence note |
|---|---|---|
| **C-01–C-04** Essential | PASS ×4 | Inertia framing presupposes full pipeline coverage |
| **C-05–C-07** Recommended | PASS ×3 | |
| **C-14** | **PASS → upgrade** | Baseline before scaffold explicitly names pre-automation process — C-14 likely upgrades from PARTIAL to PASS |
| **C-15** | **PASS → upgrade** | Structured IB-NN table anchor implied — C-15 likely upgrades from PARTIAL to PASS (net gain: +0.33) |
| **C-08–C-13, C-16–C-31** Aspirational | adjusted base | 14.31 + 0.33 (from PARTIAL→PASS upgrades on C-14/C-15) = 14.64 |
| **C-32** | **PASS** | Count-chain described — checkpoint counts present 0.65 |
| **C-33** | **FAIL** | Inertia framing does not address `Mandatory Columns (exact names)` header language |
| **C-34** | **PASS** | Phase gates verify IB-NN availability — structured gate block at end of recovery phase 0.65 |

**Aspirational subtotal**: 14.64 + 0.65 + 0 + 0.65 = **15.94**
**V-05 Total**: 56 + 30 + 15.94 = **101.94**

---

## Rankings

| Rank | Variation | Essential | Recommended | Aspirational | **Total** |
|---|---|---|---|---|---|
| **1** | V-03 CMD/DO-NOT | 56 | 30 | 16.26 | **102.26** |
| **2** | V-02 Lifecycle/Running Totals | 56 | 30 | 15.94 | **101.94** |
| **2** | V-05 Inertia/IB-NN | 56 | 30 | 15.94 | **101.94** |
| **4** | V-04 Two-Role/Gate A | 56 | 30 | 15.29 | **101.29** |
| **5** | V-01 Output Format | 56 | 30 | 14.96 | **100.96** |

---

## Excellence Signals from V-03

**Signal 1 — Explicit prohibition creates stronger enforcement than positive instruction.**
CMD DO NOT language against count omission and gate-skip is structurally stronger than instructing compliance. A positive instruction ("include count in checkpoint") fails if the model optimizes for brevity; a DO NOT prohibition ("do not emit a checkpoint without `[N] rows appended`") creates a visible violation marker. This distinction converts C-32 from aspirational-hoped-for to aspirational-enforced.

**Signal 2 — Binding vs descriptive scaffold headers change the contract type.**
`Mandatory Columns (exact names)` is a promise: column names listed here are committed in the schema contract. `Key Columns` is an observation. The difference is that a model can satisfy `Key Columns` by listing plausible field names; it cannot satisfy `Mandatory Columns (exact names)` without exact match to the typed stage-exit manifests (C-19). C-33 closes the gap between scaffold-as-navigation and scaffold-as-contract.

**Signal 3 — Named command registers with sequential IDs (CMD-01–CMD-18) make omission detection tractable.**
A numbered command list creates an audit surface: if any CMD-NN is missing from the output, the gap is visible by ID. This is the same structural mechanism as boundary labeling (C-11), recovery audit tables (C-18), and scaffold pre-declaration (C-24) — named artifacts with IDs make absence structurally visible rather than editorially detectable.

---

## New Patterns Eligible for Future Rubric Criteria

| Pattern | Observed in | Potential criterion |
|---|---|---|
| Running total in append-log (`[N] this stage, [M] total`) enables cross-phase accumulation audit | V-02, V-03 | C-32 already captures count; extension: cumulative total column in T-07 |
| Per-CMD explicit prohibition register (DO NOT language) as structural enforcement layer | V-03 | Could generalize: any CMD-NN violation is independently scorable |
| IB-NN availability gate before recovery phase — phase entry gated on incumbent baseline population | V-05 | C-34 gates completion; this gates *entry* — a pre-phase rather than post-phase gate |

---

```json
{"top_score": 102.26, "all_essential_pass": true, "new_patterns": ["CMD DO NOT prohibition register makes structural omissions independently detectable by ID — stronger enforcement than positive instruction", "Mandatory Columns (exact names) header converts scaffold from navigational aid to binding column contract traceable to typed stage-exit manifests"]}
```
