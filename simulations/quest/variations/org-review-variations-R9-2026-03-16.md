Written to `simulations/quest/golden/org-review-variate-R9-2026-03-17.md`.

---

# org-review -- Variate R9

**5 complete variations targeting C-33/C-34/C-35 (v11 rubric, 225 pt max).**

| Variant | Axis | New criteria | Predicted score |
|---------|------|-------------|----------------|
| V-01 | Lens Applicability Rating | C-33 | 215/225 |
| V-02 | NH Dimension Comparison Table | C-35 | 215/225 |
| V-03 | ADVISORY-GAP Domain Coverage | C-34 | 215/225 |
| V-04 | C-33 + C-35 | two-axis | 220/225 |
| V-05 | C-33 + C-34 + C-35 | three-axis | 225/225 |

**Key structural additions per variation:**

- **V-01**: §17 LENS APPLICABILITY RATING PROTOCOL in preamble; Applicability column (HIGH/MEDIUM/LOW, artifact-specific) added to §5.6 LENS COVERAGE TABLE. Coverage expectation tiers from the rating: HIGH+OPEN → mandatory ADVISORY-OPEN-LENS item; MEDIUM+OPEN → note only; LOW+OPEN → no action.

- **V-02**: §7 NULL HYPOTHESIS DERIVATION RULE updated to derive g_null mechanically from a dimension comparison table in BRACKET OPENING. Table columns: Dimension | Current State | Proposed State | Delta | Per-dim Verdict. Majority rule over per-dimension verdicts produces g_null(initial). Table values alone are sufficient — prose may not contradict them.

- **V-03**: §17 DOMAIN COVERAGE GAP-CHECK PROTOCOL in preamble; §5.7 section added to §9 SECTION ORDER CONTRACT (after §5.6). For each §1 domain: checks whether any reviewer has ADDRESSED coverage. UNCOVERED → ADVISORY-GAP in action register. Uses C-31 ADDRESSED/OPEN as proxy (no applicability column — C-33 absent).

- **V-04**: §17 LENS APPLICABILITY (V-01) + updated §7 NH derivation (V-02). The two additions are structurally independent (§5.6 vs BRACKET OPENING) with no integration conflict.

- **V-05**: All three. §18 DOMAIN COVERAGE GAP-CHECK PROTOCOL added alongside §17. C-34's §5.7 gap-check operates on C-33's Applicability column directly — COVERED = HIGH applicability + ADDRESSED; ADVISORY-GAP = no HIGH-app reviewer or HIGH-app reviewer with OPEN lens. Canonical architecture for 225/225.
