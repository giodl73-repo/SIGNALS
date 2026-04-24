Written to `simulations/quest/golden/corps-rob-variate-R5-2026-03-16.md`.

---

## Variate R5 -- corps-rob

**R5 focus**: The three new v5 criteria (C-19, C-20, C-21) were present as side-effects in R4 V-02 and V-03. R5 makes each the primary axis, promoting them from template artifacts to named formal rules with explicit anti-pattern prohibitions.

---

### Variation Axes

| Var | Axis | Target |
|-----|------|--------|
| V-01 | Universal zero-state declaration protocol — explicit NONE in every audit/gap-check section | C-19 |
| V-02 | Named-column enforcement audit table as formal requirement; prose explicitly prohibited | C-20 + C-19 (scoped) |
| V-03 | Named triage field labels as formal requirement; prose Triage Notes explicitly prohibited | C-21 + C-18 |
| V-04 | Zero-state universal protocol + named triage field vocabulary | C-19, C-21 |
| V-05 | Full R5 stack on R4 V-05 base — RULES A-K covering all v2-v5 aspirational criteria | C-11..C-21 |

---

### Key Design Decisions

**V-01** generalizes C-19 beyond R4's two locations. R4 V-02 got it in the Enforcement Summary; R4 V-03 got it in the Triage Note gap check. V-01 makes it a run-level rule: any section that checks and finds nothing must say `NONE` explicitly. Applied to three trailing sections: Calibration Errors, Role Concern Gaps, Triage Note Gaps.

**V-02** distinguishes template from rule. R4 V-02 showed the enforcement table as an example. V-02 states: "prose narrative does not satisfy this section" and names the four required column slots explicitly. The prohibition is the mechanism.

**V-03** targets the prose-vs-labels boundary for C-21. Shows a counter-example (prose that fails) and a passing example (labeled fields) side by side. Makes `HIGH DRIVER:` / `LOW ANCHOR:` / `DISTRIBUTION FACTOR:` the canonical vocabulary with the explicit prohibition that prose without labels fails even when content is correct.

**V-04** pairs the two prohibition-based rules (C-19 and C-21) as `RULE ZERO-STATE` + `RULE FIELD-LABELS`. Adds two trailing gap checks (Triage Note Gaps + Calibration Gaps) so both carry RULE ZERO-STATE obligations.

**V-05** extends R4 V-05's RULES A-H with RULES I/J/K, reaching all 11 aspirational criteria. Maximum expected composite under v5 rubric: 60 + 30 + (13 × 5) = 155. RULE J depends on RULE H; RULE K depends on RULE G — dependency ordering noted in the hypothesis and encoded in pass-condition language.
