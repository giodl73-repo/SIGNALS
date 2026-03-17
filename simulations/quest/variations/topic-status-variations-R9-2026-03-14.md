Written to `simulations/quest/rubrics/topic-status-rubric-v9-variations-R9-2026-03-14.md`.

---

## Round 9 Variations: `topic:status`

**R9 gap:** C-32 (named exits) and C-34 (axis-enumerated preamble) were not jointly satisfied in any R8 variant. V-04 had C-32 but its preamble failed C-34 (multi-sentence criterion-citing form). V-05 had C-34 but failed C-32 (numbered GUARD entries) plus carried a transcription error.

---

### V-01 — Single-axis: C-34 canonical preamble (minimum delta from R8 V-04)
**Axis:** Preamble form only. Replaces R8 V-04's multi-sentence criterion-citing preamble with the canonical single-declaration: `PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct stop conditions with distinct messages`. Exit A / Exit B labels unchanged.
**Hypothesis:** Pure preamble upgrade from R8 V-04 → 225. Isolates whether the canonical form is the sole missing element.

### V-02 — Single-axis: C-34 withheld (isolation test)
**Axis:** Preamble names the structural property (`PHASE 2 implements the dual-axis exit as an architectural invariant`) without axis enumeration. C-33 PASS, C-34 FAIL. Named exits retained (C-32 PASS).
**Hypothesis:** Scores 220. Gap between V-01/V-02 confirms axis enumeration is independently necessary beyond property naming alone.

### V-03 — Single-axis: Lifecycle emphasis (named GUARD exits + C-34 preamble)
**Axis:** Phase contract blocks with `Exit A -- file absent ->` / `Exit B -- topic not registered ->` inside GUARD fields. C-34 canonical preamble precedes phase blocks.
**Hypothesis:** Scores 225. Confirms C-32 is form-agnostic — named labels satisfy C-32 in GUARD contract fields as well as inline prose.

### V-04 — Combination: C-34 + C-32 + explicit trigger characterization + inertia framing
**Axes:** Canonical C-34 declaration PLUS supplementary per-axis trigger sentences + PRIMARY ADVERSARY framing.
**Hypothesis:** Scores 225. Tests whether supplementary trigger characterization is C-34-compatible or confounds it. If both V-01 and V-04 pass C-34, the canonical sentence is sufficient and extra sentences are compatible — potential Tier 9 embryo.

### V-05 — Combination: Lifecycle + C-34 + named GUARD exits + multi-site + transcription repair
**Axes:** R8 V-05 repaired — numbered GUARD entries replaced with named exits, erroneous `(C-31)` citation removed from dual-axis preamble line. OUTPUT block echoes axis-enumeration claim at a second structural site.
**Hypothesis:** Scores 225. Maximum auditability — the invariant is visible at three sites: preamble (C-33/C-34), GUARD entry names (C-32), OUTPUT block echo.

---

**Predicted Tier 8 outcome:**

| Variant | C-32 | C-33 | C-34 | Score |
|---------|------|------|------|-------|
| V-01 | PASS | PASS | PASS | 225 |
| V-02 | PASS | PASS | FAIL | 220 |
| V-03 | PASS | PASS | PASS | 225 |
| V-04 | PASS | PASS | PASS | 225 |
| V-05 | PASS | PASS | PASS | 225 |
