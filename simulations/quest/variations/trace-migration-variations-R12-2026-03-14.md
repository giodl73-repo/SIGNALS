Written to `simulations/quest/rubrics/trace-migration-rubric-v10-variate-R12-2026-03-15.md`.

---

# trace-migration — Round 12 Variations (Rubric v10)

## Overview

Rubric: v10 · 34 criteria · 220 pts · Golden threshold 176 (80%).
New criterion: **C-34** Phase Boundary Dual-Anchor Gate Block.

---

## Variation Summary

| V | Axes | Key structural change | C-34 | New signal | Predicted |
|---|------|-----------------------|------|------------|-----------|
| V-01 | Phrasing register: EXIT BLOCK advisory | Entry references at phase tops preserved; exit blocks removed from phase bottoms | FAIL | none | 215/220 |
| V-02 | Phrasing register: ENTRY REFERENCE advisory | Exit blocks at phase bottoms preserved; entry references removed from phase tops | FAIL | none | 215/220 |
| V-03 | Lifecycle emphasis: BOUNDARY PROTOCOL block | Both EXIT BLOCK + ENTRY REFERENCE named as fields in a self-contained BOUNDARY PROTOCOL block at every boundary | PASS | C-35 candidate: gate coverage computable from BOUNDARY PROTOCOL block count alone | 220/220 |
| V-04 | V-03 + Inertia framing | V-03 + STATUS QUO COST section before Q1 anchors three-part inertia baseline before role analysis begins | PASS | V-03 signal + inertia density elevated | 220/220 |
| V-05 | V-03 + V-04 + Role sequence | All of V-04 + Operations-first in Phase A; STATUS QUO COST has infrastructure orientation; B2 seeds cross-role inertia chain (Operations cause → Commerce consequence) | PASS | V-03 + inertia signals + C-36 candidate: cross-role inertia chain as structural artifact | 220/220 |

---

## V-01 — Axis A: C-34 EXIT BLOCK Advisory (regression)

**What changes**: EXIT BLOCK annotations at the bottom of each preceding phase are absent. Every phase transition carries only an ENTRY REFERENCE at the top of the succeeding phase. C-21, C-17, C-23, C-24, C-26 are preserved in full.

**Hypothesis**: Without exit blocks, C-34 FAILS because gate compliance is only detectable from one side (the succeeding phase's opening). C-21/C-17 still PASS — every transition is gated and every gate field carries `(BINARY FIELD)` — but the bilateral detectability requirement is broken. A reader who only reads Phase A cannot determine whether the A→B gate was set; they must look at Phase B's opening. **Predicted: 215/220** (−5 for C-34).

**C-34 ablation point**: The PARSE PHASE, Phase A, and every internal Phase B section close without an EXIT BLOCK. Entry references at the top of succeeding phases are present and annotated with `(BINARY FIELD)`.

---

## V-02 — Axis B: C-34 ENTRY REFERENCE Advisory (regression)

**What changes**: ENTRY REFERENCE annotations at the top of each succeeding phase are absent. Exit blocks at the bottom of preceding phases are present and annotated. C-21/C-17/C-23/C-24/C-26 preserved.

**Hypothesis**: Without entry references, C-34 FAILS — compliance is detectable only from the preceding phase's exit, not from reading the succeeding phase's opening. Gate state could be satisfied without the reader or evaluator needing to open Phase B at all. **Predicted: 215/220** (−5 for C-34).

**C-34 ablation point**: The PARSE PHASE closes with a full EXIT BLOCK; Phase A opens without an entry reference. Likewise for every intra-Phase B boundary.

---

## V-03 — Axis C: BOUNDARY PROTOCOL Block (single-axis)

**What changes**: Every phase boundary carries a named `BOUNDARY PROTOCOL` code block containing two explicit fields — `EXIT BLOCK` at the bottom of the preceding phase and `ENTRY REFERENCE` at the top of the succeeding phase — both annotated with `(BINARY FIELD)`. The block is a self-contained unit: a reader at either phase can find the gate specification without cross-referencing.

**Hypothesis**: C-34 PASS. The BOUNDARY PROTOCOL block as a named artifact creates a new excellence signal: gate coverage is computable from protocol-block count rather than by reading all phase transitions. If 5 boundaries exist, 5 BOUNDARY PROTOCOL blocks must appear; a missing block is a named-section gap. **C-35 candidate**. **Predicted: 220/220 + new signal**.

---

## V-04 — Axes C + D: BOUNDARY PROTOCOL + Inertia-First Framing

**What changes**: V-03 BOUNDARY PROTOCOL blocks at every boundary + a named `STATUS QUO COST` section inserted before Q1 in Phase A. The STATUS QUO COST section requires three parts: (a) current schema condition, (b) business process that currently works despite it, (c) accumulation trajectory if migration is abandoned (rate + horizon + named metric). Phase A questions are instructed to anchor examples back to this established baseline.

**Hypothesis**: Leading Phase A with an inertia baseline forces cause-level reasoning before the role-specific analysis starts, improving inertia-contrast density across Q1/Q2/Q3 and seeding a richer Phase B B2 example that names a distinct step. **Predicted: 220/220 + dual signal (BOUNDARY PROTOCOL count + STATUS QUO COST pre-commitment as inertia anchor)**.

---

## V-05 — Axes C + D + E: BOUNDARY PROTOCOL + Inertia-First + Operations-First Role Sequence

**What changes**: V-04 in full + Operations Expert leads Phase A as Q1 (Commerce = Q2, Finance = Q3). The STATUS QUO COST section is oriented toward infrastructure risk first. Phase B B2 is required to seed a **cross-role inertia chain**: an Operations-grounded cause from Q1/STATUS QUO COST expressed as a Commerce or Finance consequence — establishing a cause-consequence pair that neither role section alone provides.

**Hypothesis**: Operations-first exposes the STATUS QUO COST baseline to an infrastructure lens before commerce framing applies, generating a richer three-part anchor. The cross-role inertia chain in B2 (Operations cause → Commerce consequence) is a new structural artifact not achievable by single-role examples. **Predicted: 220/220 + three signals (BOUNDARY PROTOCOL count, STATUS QUO COST pre-commitment, C-36 candidate: cross-role inertia chain)**.
