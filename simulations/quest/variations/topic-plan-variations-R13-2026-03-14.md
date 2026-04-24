Written to `simulations/quest/rubrics/topic-plan-rubric-v12-variate-R13-2026-03-15.md`.

---

## Round 13 Variations — topic-plan

**Floor requirements** (C-40 + C-41 in all 5 variations):
- C-40: Every null-case site labels the template with "(Rule 3)" — the null row itself is the citation
- C-41: All enumerated-value columns in the schema carry `[Rule N: ...]` inline annotations

**Three single-axis dimensions:**

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| **V-01** | **Inertia framing** — Status Quo Defender role (Step 7b) challenges every active proposal before the diff; Architect rebuts or withdraws | Counter-argument pressure eliminates preference-only proposals and sharpens `If unchanged` cells |
| **V-02** | **Output format — scoring scale** — 5-level Urgency (U-1…U-5) in Proposals + Signal quality (H/M/L) in Inventory as Rule 5 | Separating confidence from urgency forces the model to distinguish "I'm sure this is right" from "this gets worse if we wait"; calibration constraint U-4/U-5 must match Reversibility (2)/(3) |
| **V-03** | **Role sequence — prediction-first** — Step 2b commits to specific delta predictions (with source A-NN) before any signal is read; Step 4b audits prediction accuracy | Pre-commitment prevents reverse-engineered deltas; surprise findings surface genuine blindspots |
| **V-04** | **V-01 + V-02** — Defender + urgency scores | Proposals that survive counter-argument AND carry calibrated urgency; tests for redundancy vs ratchet |
| **V-05** | **Full ceiling** — V-01 + V-02 + V-03 + expanded per-rule CONTRACT rationale; urgency predictions in Step 2b; Step 4b compares predicted vs actual urgency | Four independent mechanisms; tests composition without interference |

**New structural elements introduced in R13:**

- `Defender Challenge Table` schema (Proposal ID, strongest no-change case, cost of changing, Architect response, Defender verdict `[Rule 1: Withdrawn/Strengthened/Unchanged]`)
- `Urgency [Rule 5: U-1/U-2/U-3/U-4/U-5]` column in Proposals with 5-point scale definition in CONTRACT
- `Signal quality [Rule 5: H/M/L]` column in Signal Inventory
- `Prediction Table` schema (Prediction ID, assumption source, predicted X, predicted Y, predicted urgency, confidence before reading)
- `Prediction Accuracy Audit` table (Step 4b) comparing predictions to actual findings
- `Prediction match [Rule 1: Predicted — P-NN / Surprise]` column in Delta Findings
