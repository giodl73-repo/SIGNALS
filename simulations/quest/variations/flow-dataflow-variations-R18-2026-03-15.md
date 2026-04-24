Here are the five R18 variations:

---

## R18 Design Notes

R18 targets C-35, C-36, C-37 — the three criteria added from R17 evidence. All five variations co-declare all three new artifacts (CMD register, T-PARITY gate, PG-NN entries) in the scaffold simultaneously; the variation is *which structural axis governs their ordering and enforcement relationship*.

---

## V-01 — Output Format: CMD Register First in Scaffold

**Axis**: The CMD register is the scaffold's first declared artifact (row 0 before T-01) and the first table produced. Every subsequent scaffold row carries a `CMD Binding` field naming the CMD-NN entries that govern its production.

**Hypothesis**: CMD-first makes the meta-contract the structural anchor — every T-NN artifact commits to a named CMD obligation before stage traces begin, converting structural shortfalls from oversight into named CMD breaches citable without re-reading the prompt.

---

## V-02 — Lifecycle Emphasis: Per-Phase Parity Accumulation + Standalone T-PARITY

**Axis**: Each PG-NN gate table carries a `T-07 Running Total` verification column tracking the cumulative checkpoint sum at every phase boundary. T-PARITY is a standalone post-trace table with explicit per-stage enumeration and arithmetic.

**Hypothesis**: per-phase running totals in PG-NN create a two-tier parity audit — drift detectable at each phase boundary, not only post-trace. T-PARITY's final arithmetic is retroactively verifiable against the committed phase-gate trail.

---

## V-03 — Role Sequence: Finance → Operations → Commerce with Role-Owned CMD Slices

**Axis**: Three named roles with a stage assignment map (T-00). CMD entries carry an `Owner Role` column; each role's handoff gate (PG-FC, PG-OA, PG-CDA) enforces its CMD slice before transfer. T-PARITY attributes per-stage counts to their owner role.

**Hypothesis**: role-specific CMD slices eliminate responsibility ambiguity — a CMD breach is attributable to a named role, and each handoff gate enforces its slice before the next role begins.

---

## V-04 — Phrasing Register + Inertia Framing: Conversational with IB-NN-Anchored CMD

**Axis**: Narrative "walk through" framing. Incumbent baseline (T-IB) is produced as Section 0 before the scaffold. CMD DO NOT prohibitions explicitly reference IB-NN step identifiers (e.g., "DO NOT write recovery guidance without naming IB-01, IB-02, or another specific step from T-IB").

**Hypothesis**: anchoring CMD prohibitions to IB-NN identifiers that exist before the scaffold converts the incumbent baseline from a depth requirement into a contract anchor — a recovery row missing an IB-NN step is simultaneously a C-16 violation and a named CMD breach.

---

## V-05 — Combined: Criterion-Annotated Scaffold with Three-Way Binding

**Axis**: The scaffold includes a `Satisfies Criterion` column. CMD is marked C-37, T-PARITY is marked C-36, and PG-01–PG-04 are all marked C-35. PG-03's gate table includes a `CMD-NN Verified` column. PG-01's gate verifies C-35/C-36/C-37 coverage before Phase 2 begins.

**Hypothesis**: making the criterion-to-artifact mapping explicit in the scaffold converts rubric compliance from evaluator inference into structural verification — an evaluator confirms C-35 by reading PG-NN scaffold rows, C-36 by reading T-PARITY's row, C-37 by reading CMD's row, without inspecting trace content.

---

File written to `simulations/quest/golden/flow-dataflow-variate-R18-2026-03-15.md`.
