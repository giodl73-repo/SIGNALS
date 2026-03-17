**signal-check-rubric v2** — 12 criteria across 3 tiers.

**What changed from v1:**

- **C-11** (aspirational) — CAUSAL GAP presented first. Captured from V-03/V-04's cost-free ordering signal. Pass: CAUSAL GAP section leads the per-dimension analysis.

- **C-12** (aspirational) — Inertia check inside CAUSAL GAP. Captured from V-05's depth gain that no other variation reached. Pass: CAUSAL GAP explicitly asks whether doing nothing also produces the claimed outcome. A section that only evaluates the direct mechanism = fail.

- **Scoring formula**: aspirational denominator bumped from `/ 2` to `/ 4`. Each aspirational criterion now worth 2.5 points (was 5). The 10% aspirational weight is unchanged.

**Re-scoring R1 under v2** (spot check):
- V-02, V-03, V-04: had both old aspirational (C-09, C-10). C-11 — V-03/V-04 pass, V-02 depends on ordering. C-12 — none pass except V-05. So top score drops from 100 to ~97.5 for V-03/V-04, which is the right behavior — v2 raises the bar.
- V-05: gains C-12, loses nothing new. Score moves from 90 toward ~92.5 — correctly rewarding the inertia depth.
dence** | correctness | States explicitly whether artifact evidence exists for the causal pathway and names what is present or missing. A section that only restates the hypothesis = fail. |
| C-05 | **Output is coaching, not verdictive** | behavior | Surfaces issues as observations the team can decide to address — not blocking failures or binary PASS/FAIL judgments. "You must fix X before proceeding" = fail. |

---

## Recommended Criteria (30% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **STALENESS finding applies a concrete threshold** | depth | Uses an explicit recency criterion (e.g., 30 days) rather than a subjective impression. No threshold stated = fail. |
| C-07 | **Each flagged issue includes a suggested next action** | behavior | Every flagged dimension gets at least one concrete action (e.g., "run discover-competitors again"). Flags without actions = fail. |
| C-08 | **Report opens with a readiness summary** | format | Output begins with a brief summary of clean vs. flagged dimensions and overall readiness before diving into per-dimension detail. Diving straight into per-dimension analysis without any summary = fail. |

---

## Aspirational Criteria (10% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Cross-dimension pattern is named when present** | depth | When multiple dimensions flag the same root weakness, the output names the pattern explicitly. Four separate flags with no root identification = fail when the pattern is obvious. |
| C-10 | **Missing signal types are identified and characterized by namespace** | coverage | Lists namespaces for which no artifact exists and characterizes each gap as expected or concerning given the topic stage. "Inventory" alone without characterization = fail. |
| C-11 | **CAUSAL GAP is presented first among the four dimensions** | format | Report leads with the CAUSAL GAP section (not the summary) before the other three dimensions. Any other dimension-first ordering = fail. |
| C-12 | **CAUSAL GAP includes an inertia check** | depth | Explicitly asks whether doing nothing — or the current approach without the feature — would also produce the claimed outcome. A CAUSAL GAP section that only evaluates the direct mechanism without addressing the null-action alternative = fail. |

---

## Scoring Formula

```
composite = (essential_pass / 5) * 60
          + (recommended_pass / 3) * 30
          + (aspirational_pass / 4) * 10

golden threshold: all 5 essential pass AND composite >= 80
```

| Grade | Composite |
|-------|-----------|
| A+    | >= 95     |
| A     | >= 85     |
| B     | >= 70     |
| C     | >= 55     |
| D     | < 55      |

---

## Criterion Change Log

| Version | Change |
|---------|--------|
| v1 | Initial: C-01–C-10, aspirational denominator = 2 |
| v2 | Added C-11 (CAUSAL GAP-first ordering) from R1 V-03/V-04 excellence signal. Added C-12 (inertia check) from R1 V-05 excellence signal — addresses null-action alternative inside CAUSAL GAP. Aspirational denominator updated to 4. |
