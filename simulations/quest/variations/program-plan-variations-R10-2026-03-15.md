# program:plan — Round 10 Variates (v10 rubric)

Written to `simulations/quest/golden/program-plan-variate-R10-2026-03-16.md`.

---

## Overview

Two new R10 criteria to cover: **C-34** (compound `gate_fail:` annotation — both `# WRONG C-XX` tag AND `Why:` explanation at the same field line) and **C-35** (dual error-format recommended coverage — C-31 AND C-29 both passing simultaneously).

---

## Variation summary

| Variate | Axis | C-34 | C-35 | C-33 | C-31 | C-29 | Register |
|---------|------|------|------|------|------|------|----------|
| V-01 | C-34 single-axis | **target** | absent (control) | preserved | absent (control) | absent (control) | technical/imperative |
| V-02 | C-35 single-axis | absent (control) | **target** | present | target | target | descriptive/intent-forward |
| V-03 | C-34 + inertia framing | **target** | absent (control) | present | absent (control) | absent (control) | conversational |
| V-04 | C-34 + C-35 combination | **target** | **target** | preserved | target | target | formal/technical |
| V-05 | Golden synthesis | **target** | **target** | preserved | preserved | preserved | descriptive/intent-forward |

---

## Key structural innovation in R10

**C-34 pattern** — the compound annotation at `gate_fail:` looks like:
```yaml
gate_fail: "drafts complete"   # WRONG C-07 — Why: completion-state framing names execution, not artifact existence
```

Both the criterion tag and the `Why:` must be readable if you isolate just that field line. V-01/V-03 introduce this on top of essential-only BAD PLAN (isolating the axis). V-02 uses criterion-tagged `gate_fail:` without `Why:` as the C-34 control.

**C-35 dependency** — requires C-29 (correction table has C-05/C-06/C-07 rows) AND C-31 (BAD PLAN has all 7 criteria tagged). V-02/V-04/V-05 carry the full recommended-tier correction table; V-01/V-03 hold it back as the control.
