Written to `simulations/quest/golden/campaign-track-variate-R8-2026-03-16.md`.

---

## campaign-track / R8 — Variation Summary

All five target the four new v8 criteria that came from R7 V-05's excellence signals. The delta artifact (delta.md) is the common axis — each criterion attacks a different failure mode:

| ID | Axis | New Criteria | Key move |
|----|------|---|---|
| **V-01** | Two-pass delta update | C-25 | Phase 3 Step B writes placeholder `NOT YET REACHED`; post-Phase-4 step overwrites with actual verdict_verb; terminal item is the only order-dependent check |
| **V-02** | Dual-contract active-role annotation | C-26 | Phase 3 header names both contracts; normative rule: "naming one contract and omitting others is a structural defect" |
| **V-03** | Conjunction progression gate | C-27 | Phase 3 postcondition: `status.md AND delta.md BOTH present`; "writing status.md alone does not satisfy this postcondition" |
| **V-04** | V-01 + V-02 + V-03 combined | C-25+C-26+C-27 | Three-axis enforcement on delta — gate ensures existence, annotation ensures visibility, two-pass ensures order; C-28 still missing |
| **V-05** | Full stack | C-25+C-26+C-27+C-28 | Adds type-tightening: `signals_added = []` (empty list), string `"NONE"` explicitly rejected; Empty-State section contrasts `signals_added = []` vs `verdict_before = "NONE"` since those two fields have different types |

**Predicted leaderboard**: V-05 > V-04 > V-03 > V-01 ≥ V-02

**Open question for scoring**: Does C-25 require a named Post-Phase-4 update section, or is the order-dependent terminal checklist item alone sufficient? V-01/V-04/V-05 all have both. If the terminal item alone satisfies C-25, V-03's implicit-pass risk drops; if the named section is required, the score split between V-04 and V-03 widens.
