Here are the five complete variations for **flow-dataflow Round 17 (Rubric v14)**:

---

## What R17 targets

Three new criteria extracted from R16 evidence:

| Criterion | What it requires | R16 gap |
|-----------|-----------------|---------|
| **C-32** | `T-07 APPEND CHECKPOINT [Stage ID] COMPLETE — [N] rows appended` count statement | R16 V-01/V-03/V-04/V-05 had checkpoints but no count |
| **C-33** | Scaffold column header reads `Mandatory Columns (exact names)` — binding, not descriptive | R16 V-02 used `Key Columns`; others were inconsistent |
| **C-34** | Named gate block at end of each phase: per-artifact Required Table \| Population Status \| Go/No-Go table | R16 V-02 had prose "PHASE N COMPLETE when..." — not a structured gate |

---

## Variation map

| Var | Axis | Primary delta from R16 |
|-----|------|------------------------|
| **V-01** | Output format | PG-NN gate tables pre-declared in scaffold; scaffold completeness becomes an undeclared-artifact risk |
| **V-02** | Lifecycle emphasis | Six phases with named gate tables + running total in checkpoints (`[N] this stage, [M] total`) — Phase 3 gate verifies count parity |
| **V-03** | Phrasing register | CMD-01–CMD-18 with explicit DO NOT language against gate-skip and count omission |
| **V-04** | Role sequence + lifecycle | Finance Controller / Operations Analyst two-role; Gate A checks T-07 count parity across FC stages before handoff |
| **V-05** | Inertia framing + count-chain | Baseline before scaffold; phase gates verify IB-NN availability before recovery phase; Recovery Framing is leftmost column in T-09 |

---

**Key structural insight for C-34**: The difference between R16 V-02 and C-34 compliance is the difference between *stating a completion condition in prose* (`PHASE 2 COMPLETE when T-01 through T-06 populated`) and *producing a verification table* where each required artifact has its own Population Status cell. The table makes an empty or unpopulated artifact structurally visible as a gap — the prose condition does not.

File saved to `simulations/quest/golden/flow-dataflow-variate-R17-2026-03-15.md`.
