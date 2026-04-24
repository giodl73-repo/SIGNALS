Written to `simulations/quest/rubrics/scout-stakeholders-rubric-v20-2026-03-15.md`.

---

## scout-stakeholders rubric — v20

**Three new criteria extracted from Round 19 excellence signals:**

| ID | Name | Failure Mode | Dependency |
|----|------|-------------|------------|
| C-51 | Source staleness band calibration | `FAIL_UNCALIBRATED_STALENESS` | C-46 |
| C-52 | Synthesis field depth gate | `FAIL_SHALLOW_SYNTHESIS` | C-42 |
| C-53 | Competitor response track | `FAIL_NO_RESPONSE_TRACK` | C-50 |

**Updated totals:** 45 aspirational × 5 = 225 pts; **max 315 pts**. Golden threshold (>= 80%) unchanged.

**Under v20 (Round 19 re-scored):**
- V-01, V-02, V-03 → 305/315 (one new criterion each)
- V-04 (V-01 + V-02) → 310/315
- V-05 (all three) → 315/315 — **GOLDEN**

---

### Structural notes baked into the distinction logic

**C-51** is the eighth calibration-motif instance, extending coverage to the temporal-reliability layer of the source evidence stack. The prior seven: C-38 (veto probability), C-41 (trajectory velocity), C-44 (champion behavioral anchor), C-45 (conflict severity), C-46 (source typology), C-48 (comms priority), C-50 (competitor dual-band). C-51 introduces a **joint amendment obligation**: EXPIRED Source Age entries join ASSUMED Source cells as mandatory Step 8 targets — the first criterion to make two independent source-quality axes (epistemic basis from C-46 and temporal reliability from C-51) simultaneously mandatory.

**C-52** closes the structural gap between field presence (C-32) and field depth. The existing chain — C-32 (field exists) → C-42 (row exists) — has no gate that fires when a field is structurally present but carries an undocumented placeholder. Step 9b mirrors Step 8b's coverage-audit pattern but operates post-synthesis on content depth rather than pre-synthesis on row coverage. A row can carry all 7 columns (C-32 PASS), represent every stakeholder (C-42 PASS), cite all sources (C-35 PASS), and still fail C-52 if a field's value is empty without a reason code.

**C-53** is the first Step 0b attribute to classify **strategic intent** (CONVERT/CONTAIN/CO-EXIST) rather than market position (Adoption Band) or switching friction (Switching Cost Band). It is the first criterion to propagate a Step 0b attribute through **three downstream steps** — Step 2b, Step 6b, Step 9 — and the first to impose a content-alignment constraint on the Step 6b displacement-acknowledgment message, distinct from C-30 (framing sequence) and C-47 (timing sequence).
