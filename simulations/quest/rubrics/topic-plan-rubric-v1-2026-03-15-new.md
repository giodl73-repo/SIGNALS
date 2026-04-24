---
skill: quest-rubric
skill_target: topic-plan
date: 2026-03-15
version: 1
---

# Scoring Rubric — topic:plan

**Skill**: Revise the signal strategy as new information arrives. Read current
strategy.md and all gathered signals. Identify what has changed since the
strategy was written. Propose additions, removals, re-prioritizations. User
confirms. strategy.md updated.

---

## Essential Criteria

Must all pass. If any essential criterion fails the output is not useful
regardless of score.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Read strategy.md** | essential | correctness | Output explicitly references content from the current strategy.md — dimensions, scope, sequencing, or completion criteria. At least one concrete reference to the strategy's existing structure is present. A generic placeholder or invented content fails. |
| C-02 | **Signal inventory** | essential | coverage | Output lists gathered signal artifacts for the topic with artifact filenames and dates drawn from simulations/. All 9 namespaces are explicitly assessed (even when absent): scout / draft / review / flow / trace / prove / listen / program / topic. |
| C-03 | **Delta detection** | essential | correctness | Output distinguishes NEW artifacts (artifact date > strategy.md last-modified date) from PRIOR artifacts. Only NEW artifacts drive change proposals. PRIOR artifacts are not used as evidence for change. The strategy date is named explicitly in the output. |
| C-04 | **Typed change proposals** | essential | behavior | Proposals are categorized as ADD, REMOVE, or REPRIORITIZE — not prose observations or generic updates. If no changes are warranted for a change type, the output declares it explicitly with a type label (e.g., "ADDITIONS: none"). Silence is not a valid null declaration. |
| C-05 | **Confirmation gate** | essential | behavior | Output stops before modifying strategy.md and presents proposals for user review. A visible gate asks for YES / NO / REVISED confirmation. strategy.md is not modified until the user replies. Any output that applies changes without confirmation fails. |

---

## Recommended Criteria

Output is better with these. At least 2 of 3 are needed to reach the golden
threshold alongside all essential criteria passing.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **Evidence citation** | recommended | depth | Each non-null proposal row names the specific signal artifact(s) motivating the change — not generic reasoning. An artifact filename appears in every proposal row that is not a null declaration. |
| C-07 | **Before/after diff** | recommended | format | For each proposed change, output shows the current strategy state (Before) and the proposed new state (After), making the delta concrete and auditable. A diff table or equivalent Before/After structure is present. |
| C-08 | **Inertia justification** | recommended | depth | Each proposal addresses why NO CHANGE is not sufficient. The burden of proof rests on change, not on stability. A dedicated column or equivalent per-row justification is present naming specific signal evidence or consequence of deferral. |

---

## Aspirational Criteria

Raises the bar once essential and recommended are stable.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Type-labeled null declarations** | aspirational | format | When a change type has no proposals, the output declares it explicitly with a type label per change type: "ADDITIONS: none — inertia holds", "REMOVALS: none — inertia holds", "REPRIORITIZATIONS: none — inertia holds". A single unlabeled "No changes proposed" covering multiple change types fails. Each absent change type has its own independently labeled declaration. |
| C-10 | **Conflict detection** | aspirational | depth | Output identifies any NEW artifacts that contradict each other on the same strategy dimension before finalizing proposals. A conflict audit table or equivalent is present. When no conflicts exist, the null is declared explicitly (e.g., "CONFLICT AUDIT: none — no contradictions detected"). Absence of the section does not constitute a null declaration. |

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all essential pass AND composite >= 80.

| All essential pass | Recommended pass | Aspirational pass | Composite | Golden? |
|--------------------|-----------------|-------------------|-----------|---------|
| Yes | 3/3 | 2/2 | 100 | Yes |
| Yes | 3/3 | 1/2 | 95 | Yes |
| Yes | 3/3 | 0/2 | 90 | Yes |
| Yes | 2/3 | 2/2 | 90 | Yes |
| Yes | 2/3 | 1/2 | 85 | Yes |
| Yes | 2/3 | 0/2 | 80 | Yes (exactly) |
| Yes | 1/3 | 2/2 | 80 | Yes (exactly) |
| Yes | 1/3 | 1/2 | 75 | No |
| Yes | 1/3 | 0/2 | 70 | No |
| Yes | 0/3 | 2/2 | 70 | No |
| No (4/5) | any | any | max 72 | No |
