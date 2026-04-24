Written to `simulations/quest/rubrics/flow-resilience-rubric-v10-variate-R15-2026-03-15.md`.

---

## Round 15 — Five Variations

**Context**: All R14 variations hit 32/35 (99.14) under v14. The three new criteria (C-41/C-42/C-43) are the only open ceiling. R15 targets 100.00 by implementing them across single-, dual-, and triple-axis variations.

---

### Variation Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **Axis** | Inertia framing | Lifecycle emphasis | Role sequence | Output format | Phrasing register |
| **C-41** (sub-part labels) | PASS | — | — | PASS | PASS |
| **C-42** (SLA Budget) | — | PASS | — | PASS | PASS |
| **C-43** (Failure Signature) | — | — | PASS | — | PASS |
| **Predicted** | 33/35 | 33/35 | 33/35 | 34/35 | **35/35** |

---

### Axis Decisions

**V-01 — Single-axis: C-41 (1a/1b/1c Inertia sub-part labeling)**
Adds three explicitly labeled sub-parts to Step 1 — `Step 1a` (Domain Fragility Framing), `Step 1b` (Per-Class Carrying Costs), `Step 1c` (Tipping Point Signals). Row descriptors cross-reference by sub-part label: "Status Quo Risk = Class 1 **Step 1b** carrying cost." Satisfies the C-41 falsifiability requirement: a fill citing only "the Inertia Assessment" without "Step 1b" is a visible contract violation.

**V-02 — Single-axis: C-42 (SLA Budget pre-commitment)**
Adds a dedicated `Step 2: SLA Budget` section — a class × stage table pre-committing TTD/TTC/TTR/TTV for all three failure classes before the scenario table. Column Contract Recovery Path entry names Step 2 as the reference source. Row descriptors cite "SLA Budget Step 2, Class N row." Closes the per-row SLA invention escape that C-30 alone permits.

**V-03 — Single-axis: C-43 (Failure Signature column first in D-phase)**
Positions Failure Signature as the first column in the D-phase. Fill requirement: behavioral fingerprint *during* the failure with ≥2 named actor viewpoints (`client view`/`server view` or `node-A`/`node-B`), explicitly distinguished from Trigger Condition (entry threshold) and State (pre-failure config). Class 3 requires node-A/node-B framing showing *diverging committed state* — closing the Class 2/3 collapse escape.

**V-04 — Dual-axis: C-41 + C-42 (Investment Memo Acts I–IV)**
Structures the pre-table work as an Investment Memo with four named acts: Act I (Domain Fragility Framing), Act II (Per-Class Carrying Costs), Act III (Tipping Point Signals), Act IV (SLA Budget as class × stage table). Row descriptors cite "Class N Act II carrying cost" and "SLA Budget Act IV, Class N row." Uses narrative Act labeling (C-41 alternative variant) plus the same SLA Budget table as V-02.

**V-05 — Triple-axis: C-41 + C-42 + C-43, compact formal register**
All three axes in minimum-token form. Pre-commitment document has four sub-parts (1a/1b/1c/1d) each as a structured table. Failure Signature is Column Contract row 1 in D-phase with class-boundary discriminator instruction. Row descriptors sequence: Failure Signature first → remaining D-phase → C-phase → Chaos Block. Every constraint is pre-committed; per-row independent authoring of any value established in Step 1a–1d is explicitly named as a contract violation.

---

### Key Structural Additions per Criterion

**C-41 satisfaction pattern** (V-01, V-04, V-05):
```
Status Quo Risk column fill requirement:
"Must reference Step 1b by sub-part label.
Form: 'Class N Step 1b carrying cost: [metric] [rate] [horizon].'
Citing only 'the Inertia Assessment' without 'Step 1b' fails."
```

**C-42 satisfaction pattern** (V-02, V-04, V-05):
```
Recovery Path column fill requirement:
"SLA targets must reference the SLA Budget (Step 1d / Step 2 / Act IV above),
citing class row and stage column — do not author independently.
Per-row SLA invention is a contract violation."
```

**C-43 satisfaction pattern** (V-03, V-05):
```
Failure Signature column fill requirement:
"Behavioral fingerprint WHILE the failure is in progress.
NOT the entry threshold (Trigger Condition). NOT pre-failure config (State).
Name ≥2 actor viewpoints per row. Each: named observable during the failure.
Generic fills ('system unavailable') without actor differentiation fail.
Class 3 requires node-A/node-B framing showing diverging committed state."
```
