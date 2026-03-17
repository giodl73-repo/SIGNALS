Written to `simulations/quest/golden/campaign-blueprint-variate-R3-2026-03-16.md`.

---

## campaign-blueprint R3 — Five Variations

### What changed in v3 that R3 must address

Two new aspirational criteria (C-15 + C-16) add up to 10 pts, raising the ceiling from 108 to 118. All R2 variations would score partial on these under v3. R3 tests mechanisms that earn both at full credit.

---

### V-01 — Contract Matrix Axis

**Hypothesis:** Declaring all three artifact contracts as a single table during setup — before any execution — makes READ/WRITE/PRESERVE/CARRIES FORWARD obligations visible at a glance. Reduces per-artifact word cost while maximizing C-15 coverage. Tests whether grouped visibility outperforms per-artifact inline declarations.

**C-15 mechanism:** Unified 4×3 contract table, all fields, all artifacts, printed before Artifact 1.
**C-16 mechanism:** `FINDINGS (write this block after the pitch file is written, not before)` — explicit label + post-execution timing.

---

### V-02 — FINDINGS Template Axis

**Hypothesis:** Named FINDINGS sub-fields (CONVICTION DELTA / NEAR-DUPLICATE CONTENT / RESIDUAL QUESTIONS) force post-execution placement structurally — CONVICTION DELTA asks per-version, requiring the completed pitch to exist. Harder to satisfy pre-execution or with a checklist than an open prompt. Targets C-16 and C-13 full credit simultaneously.

**C-15 mechanism:** Per-artifact inline READ/WRITE/PRESERVE/CARRIES FORWARD headers.
**C-16 mechanism:** FINDINGS template with three named sub-fields; timing instruction explicit.

---

### V-03 — Carries-Forward Cascade Axis

**Hypothesis:** CF declared at the close of each artifact — after execution, as a filled-in handoff block — puts the inheritance declaration immediately before the GATE, so the consuming artifact sees it first. Tests whether proximity to consumer matters more than completeness of the upfront contract for C-07 compliance.

**C-15 mechanism:** Per-artifact inline READ/PRESERVE + CARRIES FORWARD filled-in values at close.
**C-16 mechanism:** `FINDINGS (write this block after the pitch file is written, not before)`.

---

### V-04 — Contract Matrix + FINDINGS Template *(V-01 + V-02 combined)*

**Hypothesis:** Upfront matrix (pre-execution visibility) and structured FINDINGS template (post-execution structure) are complementary. The matrix eliminates C-15 gaps; the sub-field template eliminates C-16 placement ambiguity. Combined, they close both aspirational criteria without ceremony.

---

### V-05 — Cascade + FINDINGS Template + Minimal Density *(V-03 + V-02 + R2 V-03 skeleton)*

**Hypothesis:** R2 V-03 tied for 108 at ~40% fewer words — trigger phrases carry weight, ceremony is optional. R3 tests whether the same compression principle applies to C-15 and C-16: CF cascade at close time + structured FINDINGS in the densest possible form. The diagnostic question is whether the template earns C-16 full credit where a compressed open prompt might earn partial.

---

### R3 Diagnostic Questions

| # | Question |
|---|----------|
| 1 | Does contract matrix (V-01) vs per-artifact inline (V-02/V-03) affect C-15 partial vs full? |
| 2 | Does the FINDINGS template (V-02/V-04/V-05) earn C-16 full more reliably than the open prompt (V-01/V-03)? |
| 3 | Does CF at close time (V-03/V-05) vs upfront matrix (V-01/V-04) change C-07 compliance? |
| 4 | Does minimal density (V-05) retain C-16 full credit or regress to partial when space is compressed? |
