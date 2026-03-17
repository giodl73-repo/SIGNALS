Rubric written to `simulations/quest/rubrics/scout-size-rubric-2026-03-16.md`.

**Summary of what was designed:**

**5 Essential criteria** (60 pts):
- C-01: Surface area enumerated — named integration points with count
- C-02: Complexity tier on-scale — exactly LOW/MEDIUM/HIGH/XL with justification
- C-03: Inertia check present — names the workaround and gives directional cost comparison
- C-04: Confidence level with basis — not a bare label
- C-05: Signal boundary respected — no task breakdown, no owners, no milestone dates

**3 Recommended** (30 pts):
- C-06: Team-size signal names specialist types, not just headcount
- C-07: Timeline as sprint range (not a point estimate or calendar date)
- C-08: Primary complexity driver identified (not generic justification)

**2 Aspirational** (10 pts):
- C-09: Sensitivity — what pushes the tier up or down
- C-10: Confidence calibration — what investigation would change the confidence level

**Golden threshold**: all 5 essential pass + composite >= 80.

The four failure patterns section captures the most likely ways a model will miss — plan creep (C-05), wrong vocabulary (C-02), silent inertia (C-03), and bare confidence (C-04).
ly compares building the feature against the cost of maintaining the current workaround (or absence of the feature). The comparison must name what the workaround is and give a directional cost judgment (cheaper / comparable / more expensive). Omitting the check entirely fails; a one-liner that names the workaround and cost direction passes. |
| C-04 | **Confidence level stated with basis** | correctness | Output states a confidence level (HIGH / MEDIUM / LOW, or a percentage band) and identifies what drives that confidence — e.g., "MEDIUM — surface area is clear but integration behavior with the legacy auth layer is unverified." A bare "confidence: HIGH" with no basis fails. |
| C-05 | **Signal boundary respected** | behavior | Output does NOT contain task breakdowns, sprint assignments, owner names, or milestone dates. It is a sizing signal, not a plan. Presence of any assigned task ("Sprint 1: implement X") fails this criterion. |

### Recommended (30 pts total — output is better with these)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Team-size signal names specialist types** | depth | Output identifies the specialist disciplines needed (e.g., "1 backend, 1 platform, 0.5 PM") not just a headcount. "3 engineers" alone fails; "1 backend engineer, 1 frontend engineer, 0.5 PM" passes. |
| C-07 | **Timeline signal given as sprint range** | depth | Output gives a sprint range estimate (e.g., "3–5 sprints") — not a calendar date, not a single fixed number. A range communicates uncertainty appropriately; a point estimate or calendar date fails. |
| C-08 | **Primary complexity driver identified** | depth | Output names the one or two factors that most drive the complexity tier rating (e.g., "complexity is HIGH primarily because the state machine has 12 transition paths and no existing test harness"). Generic justification ("it's complex") fails. |

### Aspirational (10 pts total — raise the bar)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Sensitivity: what changes the tier** | depth | Output states at least one condition that would push the complexity tier up and one that would push it down (e.g., "drops to MEDIUM if the auth integration is already spec'd; rises to XL if offline support is required"). |
| C-10 | **Confidence calibration: what would change it** | depth | Output states what information or investigation result would materially raise or lower the stated confidence level (e.g., "confidence rises to HIGH if a spike confirms the webhook delivery contract"). |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

### Score Table

| Essential pass | Recommended pass | Aspirational pass | Composite |
|---------------|-----------------|-------------------|-----------|
| 5/5 | 3/3 | 2/2 | 100 |
| 5/5 | 3/3 | 1/2 | 95 |
| 5/5 | 3/3 | 0/2 | 90 |
| 5/5 | 2/3 | 2/2 | 90 |
| 5/5 | 2/3 | 1/2 | 85 |
| 5/5 | 2/3 | 0/2 | 80 ← golden threshold |
| 5/5 | 1/3 | 2/2 | 80 ← golden threshold |
| 5/5 | 1/3 | 1/2 | 75 (below golden) |
| 5/5 | 0/3 | 0/2 | 60 (below golden) |
| 4/5 | 3/3 | 2/2 | 88 (fails golden — essential incomplete) |

---

## Failure Patterns to Watch

- **Plan creep**: outputs that drift into task breakdowns satisfy the domain PM instinct but
  violate C-05. This is the most likely failure mode for a sizing skill.
- **Tier without scale**: outputs that use "MODERATE" or numeric scores instead of the
  LOW/MEDIUM/HIGH/XL vocabulary fail C-02. The vocabulary is load-bearing — it must feed
  downstream skills that parse it.
- **Silent inertia**: outputs that focus entirely on the new build and mention the workaround
  only in passing ("users currently use a spreadsheet") fail C-03. The check requires a
  cost comparison, not just a name.
- **Bare confidence**: stating "confidence: HIGH" with no basis is common. C-04 requires
  a reason — the basis is what makes the confidence actionable.
