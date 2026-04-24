Here is the complete v17 rubric written to `simulations/quest/rubrics/trace-deployment-rubric-v17-2026-03-15.md`.

---

**Two new criteria promoted from R20 excellence patterns:**

| ID | Pattern | Condition |
|----|---------|-----------|
| C-43 | `stage-2-primary-domain-quality-review` | Stage 2 sub-questions explicitly target Stage 1's intra-domain quality defects: unbounded thresholds, underspecified ordering dependencies, missing numeric trigger conditions, unverified rollback states. Distinct from C-40's cross-domain extension. Requires C-40. |
| C-44 | `declarative-disqualifier-phase-section-placement` | C-31 passes AND the declarative disqualifier (C-29) is confirmed within a named phase section body — not in general instructions preceding the phases. V-04's 10-pt loss (C-31 + C-32 both fail) traced directly to general-instructions placement. Requires C-31; prose-path only. |

**Ceiling changes:**

| Path | v16 | v17 |
|------|-----|-----|
| Template + two-stage | 195/260 | 200/270 (C-43 +5; C-44 blocked) |
| **Prose structural-adoption + two-stage** | **205/260** | **215/270** (C-43 +5 + C-44 +5) |
| Two-stage only (no C-14/C-21) | 160/260 | 165/270 (C-43 +5; C-44 blocked) |

**R21 target**: 215/270 — prose structural-adoption + two-stage + stage-2-intra-domain-quality-review (C-43) + declarative disqualifier in phase section (C-44).
