Written to `simulations/quest/golden/quest-rubric-variate-v19-R19-2026-03-16.md`.

---

**Round 19 — 5 variations targeting C-49 and C-50**

**What changed from R18 baseline (R18 V-04, which passes C-47 + C-48):**

**C-49** requires: Phase 8.5 failure-mode clause governed by a FORMAT TEMPLATE with a mandatory `[C-NN]` slot — omission is visible as an unfilled bracket, not a silent prose absence.

**C-50** requires: Each STATUS QUO foil item enumerates **every** passing criterion in the span between consecutive failure points — not cumulative-from-start range notation, not a partial subset.

---

**V-01 — Lifecycle emphasis (C-49 probe, C-50 ablated)**
Installs the R18-V-03 `PER-NOTE FORMAT TEMPLATE` in Phase 8.5 with the mandatory `[C-NN]` slot and a STOP condition. STATUS QUO keeps R18 V-04's cumulative range notation ("passes C-01 through C-08 while failing C-09"). Prediction: **PASS C-49, FAIL C-50**.

**V-02 — Inertia framing (C-50 probe, C-49 ablated)**
STATUS QUO foil items rewritten with per-span explicit enumeration — e.g., "passes C-04 and C-05 while failing C-06" where C-04, C-05 are the *only* criteria in the span from C-03 to C-06. The span bounds are co-located as inline annotations. Phase 8.5 retains prose criterion IDs (C-47 PASS, no template). Prediction: **FAIL C-49, PASS C-50**.

**V-03 — Output format (C-50 via SPAN DEFINITION pre-step, C-49 ablated)**
Different structural mechanism for C-50: a `SPAN DEFINITION` slot precedes each STATUS QUO foil item, requiring the builder to compute `Previous failure → Current failure → Pass side: [list every C-NN]` before writing the foil item. The foil item is then transcribed from the pass-side list. Tests whether intermediate computation scaffold yields different C-50 pass rates than V-02's direct instruction. Prediction: **FAIL C-49, PASS C-50** (via different mechanism than V-02).

**V-04 — Combined lifecycle + inertia (C-49 + C-50)**
FORMAT TEMPLATE from V-01 + per-span enumeration from V-02. Joint satisfiability test. Prediction: **PASS C-49, PASS C-50**.

**V-05 — Combined + phrasing register (ceiling form)**
V-04 mechanisms plus a `SLOT-FILL STOP` in Phase 8.5 (names the unfilled bracket as a distinct defect class from prose-only omission) and a `FULL-SPAN STOP` in STATUS QUO (names range notation as a non-compliant form with a compliant-form example). Phrasing register shifts from instruction to defect-class declaration at both sites. Prediction: **PASS C-49, PASS C-50** with highest defect-detection specificity.
