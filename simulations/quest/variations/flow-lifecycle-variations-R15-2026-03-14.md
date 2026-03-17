Written to `simulations/quest/rubrics/flow-lifecycle-rubric-v15-variate-R15-2026-03-15.md`.

---

# flow-lifecycle — R15 Variations (Rubric v15)

## What changed R14 → R15

R14 V-05 scored C-46 and C-47 **implicitly** — a per-phase "Incumbent reference" comment at SECTION A level, and IM-ID wording inside EX Trigger/Why Problematic prose. R15 escalates both to **explicit named sub-fields** in their canonical locations, making them format-verifiable by string comparison without prose inference.

| Criterion | R14 mechanism (implicit) | R15 mechanism (explicit) |
|-----------|-------------------------|--------------------------|
| C-46 | "Incumbent reference" comment at top of SECTION A | `IM Reference:` named sub-field in **PHASE ENTRY CONTRACT** |
| C-47 | IM-ID wording in EX Trigger/Why Problematic fields | `IM Ref:` named sub-field in every **EX block** (dual-cite alongside `Bottleneck Ref:`) |

---

## Variation Matrix

| V | Axes | C-44 | C-45 | C-46 | C-47 | Predicted |
|---|------|:----:|:----:|:----:|:----:|-----------|
| V-01 | Role sequence (default ordering) | FAIL | FAIL | FAIL | FAIL | ~34/39 = 8.718 |
| V-02 | Output format (isolated per-block Exception Refs) | **PASS** | FAIL | FAIL | FAIL | ~35/39 = 8.974 |
| V-03 | Lifecycle emphasis (dedicated PHASE GATE CONTRACT SUMMARY) | FAIL | **PASS** | FAIL | FAIL | ~36/39 = 9.231 |
| V-04 | Inertia framing (`IM Reference:` in PHASE ENTRY CONTRACT) | FAIL | FAIL | **PASS** | FAIL | ~37/39 = 9.487 |
| V-05 | Full combination | **PASS** | **PASS** | **PASS** | **PASS** | 39/39 = 10.000 |

---

## Key Structural Additions Per Variation

**V-02 adds to B-NN blocks** (C-44):
```
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] — [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation)...
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-01, or NONE.]
```

**V-03 adds** a dedicated `Phase Gate Contract Summary` section before PHASE 1 declaring all three fields as a named unit with explicit orthogonality declaration (C-45).

**V-04 adds to PHASE ENTRY CONTRACT** (C-46):
```
- IM Reference: [List every IM-ID from INCUMBENT BASELINE whose failure mode represents
  an active risk entering this phase... NONE if no incumbent risk is active at entry.]
```
And adds `Baseline→Phase` direction to CHAIN STATUS.

**V-05 adds to every EX block** (C-47):
```
> - IM Ref: [IM-ID from INCUMBENT BASELINE whose failure mode this exception traces, or NONE.
>   Dual-citation: `Bottleneck Ref:` (C-42 B-NN link) + `IM Ref:` (C-47 baseline link).
>   EX blocks become the convergence point for all three chains: Role, B-NN, Baseline.]
```
Plus adds `Baseline→Exception` direction to CHAIN STATUS (12 total directions).

---

## Design Notes

**Single-axis choices**: Output format (C-44), Lifecycle emphasis (C-45), Inertia framing (C-46) — the three axes that individually close one dark traceability direction each.

**V-05 composition**: The four structural additions are architecturally orthogonal — they extend different document sections with independent named fields. No interaction risk. CHAIN STATUS grows from 11 to 13 directions with `Baseline→Phase` (V-04) and `Baseline→Exception` (V-05).

**Ceiling confidence**: R14 V-05 already scored 39/39 under v15 retroactively. R15 V-05 makes the same signals explicit rather than implicit, which should produce *more* reliable scoring, not less.
