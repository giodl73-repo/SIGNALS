Scorecard written. Summary:

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-03 Conversational | **100** | YES |
| 1 | V-04 Minimal | **100** | YES |
| 1 | V-05 Spec-forward | **100** | YES |
| 4 | V-01 Prose templates | **98.75** | NO |
| 4 | V-02 Compact registry | **98.75** | NO |

**All 5 predictions confirmed. Prediction accuracy: 100%.**

---

**Key findings:**

**C-15 and C-16 are clean, orthogonal discriminants.** V-01 has F-01..F-10 coverage but fails C-15 on prose templates. V-02 has key=value syntax but fails C-16 on the compact registry. Each fires independently — you can have one without the other.

**Minimalism probe passed (V-04).** The extra prose in R3 V-04 was commentary, not enforcement load. The mechanism floor is: 10-item F-ID registry + one F-ID per block + `Line`/`Sev` table columns + key=value verdict template. Everything above that floor scores identically.

**Register is neutral (V-03).** Wrapping F-IDs in explanation ("without one, a finding becomes a research task") scores identically to stating them as commands ("triggers F-02"). Register can be chosen for audience without compliance cost.

**V-05 introduces a new structural pattern.** Pre-review spec claims make C-06 contractually enforceable — the discipline's claim in Block 3 is the commitment, the `spec-gaps=` in the verdict is the audit. This is qualitatively stronger than any post-hoc verdict annotation. Three golden candidates available for promotion.
gistry F-01..F-10 covers all recommended criteria (F-06 severity, F-07 count, F-08 amend, F-09 root cause, F-10 spec).

**V-02 -- 98.75 (C-16 FAIL)**
- C-16 FAIL: Registry covers only F-01..F-05. F-06 (severity), F-07 (count), F-08 (amend scope), F-09 (root cause), F-10 (spec mapping) absent -- recommended criteria have no F-ID anchor at their enforcement points.
- C-15 PASS: Step 4 `total=[N] CRIT=[n] MAJ=[n] MIN=[n] spec-gaps=[list or "n/a"]`; Step 2 `Name: [expert name] Signal: [exact code signal]`.
- C-13 PASS (nuanced): F-01..F-05 ARE co-located at their enforcement points. Sev warning at Step 3 ("loses severity differentiation") names no F-ID because F-06 is absent from registry -- but the criterion passes on co-location of existing labels.

**V-03 -- 100 (register test confirmed)**
- All 16 criteria pass. Explanatory framing ("without one, a finding becomes a research task (F-02)") does not dilute F-ID signal at enforcement points -- the label still fires. Register is cosmetic; mechanism presence is what scores.
- C-13 evidence: F-05 at Block 2; F-02/F-03/F-06 at Block 3; F-01/F-07/F-10 at Block 4; F-04/F-09 at Block 5; F-08 at Block 6 -- all wrapped in explanatory prose but structurally co-located.

**V-04 -- 100 (minimalism confirmed)**
- All 16 criteria pass with minimum prompt weight. One-line registry entries, one F-ID annotation per block, no explanatory bullets. Explanatory prose in R3 V-04 was commentary, not enforcement load.
- C-10 evidence: `Why: [structural or process root cause -- not a symptom]` -- the "not a symptom" constraint is explicit without a causal explanation of why symptoms fail.

**V-05 -- 100 (spec-forward confirmed)**
- All 16 criteria pass. Strongest C-06 enforcement in any variation: Block 3 (pre-review spec claims) + Block 5 (spec-gaps verdict). Two-phase enforcement: discipline declares owned spec sections before code review; an absent implementation in Block 5 is caught by the prior claim.
- C-11 evidence: three format-encoded fields -- `Line` column (C-02), `Sev` column (C-07), `sections=` key in Block 3 (C-06) -- only variation with three-way structural encoding.
- C-15 evidence: Block 3 `sections=[list]`; Block 5 `total=[N] CRIT=[n] MAJ=[n] MIN=[n] spec-gaps=[list or "n/a"]`; Block 2 `Name: [x] Signal: [y]` -- all structured fields use key=value.

---

### Excellence Signals

**Mechanism floor (V-04):** 10-item F-ID registry + one F-ID per block + table columns is the minimum viable structure for 100/100. Prompt weight above this floor adds no criterion score. Context dilution risk decreases as prompt weight decreases -- V-04 is the preferred base for new variations when token budget matters.

**Contractual spec enforcement (V-05):** Pre-review spec claims create a structural enforcement contract that post-hoc verdict fields cannot match. When a discipline declares `sections=[S1, S2]` before reviewing code, an absent implementation in Block 5 `spec-gaps=` is caught by the prior claim -- the claim is the commitment, the verdict is the audit. This is the only variation where C-06 compliance is structurally impossible to satisfy silently.

**Register neutrality (V-03):** Explanatory register does not erode criterion compliance. F-IDs wrapped in rationale ("without one, a finding becomes a research task") score identically to F-IDs stated as commands ("triggers F-02"). Audience-tuning (imperative vs. explanatory) is free -- choose by consumer, not by compliance concern.

---

### Round Summary

R4 closes the 16-criterion rubric. All predicted scores confirmed. Two new criteria (C-15, C-16) are stable discriminants: C-15 fires on prose templates, C-16 fires on compact F-01..F-05 registries. Three variations achieve 100. The rubric is complete through 8 aspirational levels; no ceiling gaps remain.

Golden candidates for promotion: V-03 (audience-friendly), V-04 (minimal), V-05 (spec-forward).
