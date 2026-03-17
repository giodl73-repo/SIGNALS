Here are the 5 complete variations for `quest-score` Round 13, written to `simulations/quest/golden/quest-score-variate-R13-variations-2026-03-15.md`.

---

## Design summary

**Forced infrastructure change (all 5 variations):** formula `/25 * 220` → `/28 * 220`

### V-01 — EPI axis (C-33 isolation)
Inherits R12 V-01 anchor architecture (Failure Modes A–E, Mechanisms 1–5, sequential 1:1 pairing). Intentionally preserves C-34 FAIL (general routing, no terminal assertion) and C-35 FAIL (combined single Specificity block field). Proves C-33 stability under formula update.

**Predicted open:** C-34, C-35

### V-02 — NCA axis (C-34 isolation)
Inherits R12 V-02 PROHIBITED architecture (per-entry routing annotations + terminal assertion "No prohibited content category lacks a named destination"). No anchor. Intentionally preserves C-33 FAIL and C-35 FAIL (combined Specificity field). Proves C-34 stability.

**Predicted open:** C-33, C-35

### V-03 — DSC axis (C-35 isolation)
Inherits R12 V-03 VERIFIER TABLE (separate `Type-level` and `Intra-run` columns, each independently PASS/FAIL). No anchor, general routing. Proves C-35 stability.

**Predicted open:** C-33, C-34

### V-04 — R13 ceiling (EPI + NCA + DSC combined)
Combines V-01 anchor + V-02 PROHIBITED (per-entry routing + terminal assertion) + V-03 VERIFIER TABLE dual-column schema. The three axes target orthogonal sites: anchor block, PROHIBITED list boundary, VERIFIER output schema. No cross-contamination expected.

**Predicted:** all 28 aspirationals PASS, composite 310/310

### V-05 — Inertia-framing register on R13 ceiling base
Same architectural features as V-04. Rewritten so every structural constraint is introduced as an explicit override of a named **inertia path** — what the model does by default without the constraint. Each field definition names the inertia behavior it defeats (e.g., *"models omit the `*Change*` field when the verdict matches baseline — this field is always required"*). The PROHIBITED section entries each name the inertia pull that makes the category tempting. Tests whether visceral inertia framing changes execution behavior without altering the criterion profile.

**Predicted:** same as V-04 (all 28 PASS) — discriminator is behavioral, not structural
