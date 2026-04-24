---
skill: quest-rubric
skill_target: scout-risk
date: 2026-03-16
version: 1
---

# Scoring Rubric: scout-risk

Risk register for a feature or decision. Evaluates whether the output correctly identifies and structures risks across the five required dimensions, leads with inertia, and provides actionable risk anatomy for each entry.

---

## Composite Score Formula

```
Score = (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Inertia risk listed first** | correctness | The first risk entry is the inertia risk — the risk that the status quo was sufficient and the feature was the wrong thing to build. Must appear before any technical/market/compliance/dependency/timeline risks. Fail if inertia is absent or buried. |
| C-02 | **Multi-dimensional coverage** | coverage | Output includes risks from at least 3 of the 5 required dimensions: technical, market, compliance, dependency, timeline. Fail if fewer than 3 dimensions are represented. |
| C-03 | **Risk anatomy complete** | correctness | Every risk entry includes all three required fields: severity (HIGH/MEDIUM/LOW), likelihood (any meaningful expression of probability or triggering condition), and mitigation (a stated action or control). Fail if any risk is missing one or more fields. |
| C-04 | **Severity uses correct scale** | format | Severity values are drawn exclusively from {HIGH, MEDIUM, LOW}. No numeric scales, percentages, or invented labels. Fail if any severity value deviates from this vocabulary. |
| C-05 | **Mitigations are specific and actionable** | depth | Each mitigation describes a concrete action, owner class, or control — not a generic hedge ("monitor closely", "be careful"). A passing mitigation names what to do or what to watch, not just that something should happen. Fail if two or more mitigations are generic non-actions. |

---

## Recommended Criteria (weight: 30 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Risks are dimension-labeled** | format | Each risk entry is explicitly tagged with its dimension (e.g., "Technical", "Market", "Compliance", "Dependency", "Timeline"). Pass if >= 80% of risks carry a visible dimension label. |
| C-07 | **Likelihood is qualified beyond binary** | depth | Likelihood expressions go beyond "possible/unlikely" — they specify a condition, scenario, or rough probability bracket (e.g., "high if team has no prior SDK experience", "~30% given current adoption curve"). Pass if >= half of risks meet this bar. |
| C-08 | **Risks are ordered by priority** | behavior | The register is ordered highest-to-lowest severity (after inertia), or explicitly states a prioritization logic. A randomly ordered flat list fails. Pass if the ordering is defensible by severity or compound impact. |

---

## Aspirational Criteria (weight: 10 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Risk interdependencies noted** | depth | At least one risk entry notes how it compounds with or unlocks another (e.g., "If C-03 materializes, timeline risk escalates to HIGH"). Pass if at least one cross-risk dependency is surfaced explicitly. |
| C-10 | **AMEND behavior demonstrated** | behavior | When an AMEND directive is present in the prompt (focus on one dimension, adjust severity thresholds), the output correctly narrows scope or recalibrates without losing inertia or risk anatomy. Pass if AMEND is applied correctly and inertia risk is retained even in a narrowed register. |

---

## Scoring Reference

| Outcome | Score Range |
|---------|-------------|
| Golden (all essential pass, composite >= 80) | 80-100 |
| Passing (all essential pass, composite < 80) | 60-79 |
| Failing (any essential fails) | 0-59 |

### Quick Failure Modes

- Inertia risk missing or not first → C-01 fail → max score 48 (cannot reach golden)
- Fewer than 3 dimensions covered → C-02 fail → cannot reach golden
- Any risk missing severity/likelihood/mitigation → C-03 fail → cannot reach golden
- All mitigations are generic → C-05 fail → cannot reach golden
