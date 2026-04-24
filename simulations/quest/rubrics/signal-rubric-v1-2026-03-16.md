---
skill: quest-rubric
skill_target: signal
date: 2026-03-16
version: 1
---

# Scoring Rubric: /signal

The `signal` skill is a command index. It shows all available skills organized by namespace with
one-line descriptions. Three invocation modes: `/signal` (full index), `/signal <namespace>`
(filtered), `/signal --bare` (names only). Output is not a simulation artifact — it is a
navigation aid. Scoring reflects whether a user can orient and route from the output alone.

---

## Essential Criteria

All essential criteria must pass. A failing essential = output is not useful.

### C-01 — Namespace completeness
**Weight**: essential
**Category**: correctness
**Text**: All 12 namespaces are present in the full-index output.
**Pass condition**: Output contains all of: scout, draft, review, flow, trace, prove, listen,
program, topic, quest, mock, org. Missing any namespace = FAIL.

---

### C-02 — Sub-skill count accuracy
**Weight**: essential
**Category**: correctness
**Text**: Skill counts per namespace match the canonical registry.
**Pass condition**: Counts must match — scout(8), draft(4), review(4), flow(7), trace(7),
prove(9), listen(3), program(2), topic(6), quest(4), mock(3), org(4). Any namespace off by
more than one = FAIL.

---

### C-03 — One-line descriptions present
**Weight**: essential
**Category**: coverage
**Text**: Every listed sub-skill has a one-line description that names what the skill produces.
**Pass condition**: No sub-skill appears as a bare name with no description in non-bare mode.
Any namespace section with undescribed skills = FAIL.

---

### C-04 — Namespace filter behavior
**Weight**: essential
**Category**: behavior
**Text**: `/signal <namespace>` output contains only skills from that namespace, not all namespaces.
**Pass condition**: When invoked with a single namespace argument (e.g., `/signal flow`), output
lists only skills within that namespace. Output containing skills from other namespaces = FAIL.

---

### C-05 — Bare mode behavior
**Weight**: essential
**Category**: behavior
**Text**: `/signal --bare` produces only command names with no descriptions.
**Pass condition**: Output is a flat list of slash-command names (e.g., `/scout-competitors`).
No prose, no headers, no description text. Any non-name content in bare mode = FAIL.

---

## Recommended Criteria

Output is better with these. A failing recommended reduces score but does not disqualify.

### C-06 — Description specificity
**Weight**: recommended
**Category**: depth
**Text**: Descriptions are specific and differentiating — not generic phrases reused across skills.
**Pass condition**: No two skills in different namespaces share the same description text.
Descriptions name the concrete output artifact or method, not just "analyze X". Generic
descriptions on 3+ skills in a single namespace = FAIL.

---

### C-07 — Visual hierarchy
**Weight**: recommended
**Category**: format
**Text**: Sub-skills are visually subordinate to namespace headers — indented or prefixed.
**Pass condition**: Namespace headers appear at a higher visual level than sub-skill entries.
A flat undifferentiated list with no grouping cues = FAIL.

---

### C-08 — Routing guidance
**Weight**: recommended
**Category**: behavior
**Text**: Each namespace section includes a routing hint: describe your need and the most relevant
skill will run.
**Pass condition**: At least half of namespace sections include a phrase indicating the user can
describe their need instead of specifying a sub-skill name. No routing hints anywhere = FAIL.

---

## Aspirational Criteria

Raise the bar once essential and recommended are stable.

### C-09 — Skill count in namespace header
**Weight**: aspirational
**Category**: format
**Text**: Namespace headers include the skill count (e.g., "Scout namespace -- 8 skills").
**Pass condition**: Every namespace header includes a parenthetical or inline count of sub-skills.
Any header missing its count = FAIL.

---

### C-10 — T3 tier annotation
**Weight**: aspirational
**Category**: depth
**Text**: Skills with a full T3 runbook are annotated to indicate on-demand loading.
**Pass condition**: Skills known to be T3-only (e.g., `/flow-lifecycle`, `/trace-skill`) carry a
visible annotation such as `(T3 -- full runbook loaded on demand)` or equivalent. No T3
annotations in the output = FAIL.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band       | Composite | Meaning                                      |
|------------|-----------|----------------------------------------------|
| Golden     | >= 80     | All essential pass + recommended largely pass |
| Acceptable | 60-79     | All essential pass, recommended partial       |
| Marginal   | 40-59     | 1 essential fail or multiple recommended fail |
| Reject     | < 40      | 2+ essential fail — output not usable         |
