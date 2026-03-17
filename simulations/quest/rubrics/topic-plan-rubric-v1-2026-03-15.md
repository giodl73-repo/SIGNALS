---
skill: quest-rubric
skill_target: topic-plan
date: 2026-03-15
version: 1
---

# Scoring Rubric -- topic:plan (v1)

**Skill**: Revise the signal strategy as new information arrives. Read
current strategy.md and all gathered signals. Identify what has changed
since the strategy was written. Propose additions, removals,
re-prioritizations. User confirms. strategy.md updated.

**Composite score formula**:
`(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`

**Golden threshold**: all 5 essential criteria pass AND composite >= 80

---

## Essential Criteria

Must all pass. If any essential criterion fails, the output is not useful
regardless of score.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Read strategy.md** | essential | correctness | Output explicitly references content from the current strategy.md (dimensions, scope, sequencing, or completion criteria) -- not a generic placeholder. Reading is evidenced by at least one concrete reference to the strategy's existing structure. |
| C-02 | **Signal inventory** | essential | coverage | Output produces a list of gathered signal artifacts for the topic, with artifact filenames and dates, drawn from simulations/. All 9 namespaces are explicitly assessed (even if absent). |
| C-03 | **Delta detection** | essential | correctness | Output distinguishes NEW artifacts (artifact date > strategy.md last-modified date) from PRIOR artifacts. Only NEW artifacts drive change proposals. PRIOR artifacts are not used as evidence for change. The strategy date is named explicitly. |
| C-04 | **Typed change proposals** | essential | behavior | Proposals are categorized as ADD, REMOVE, or REPRIORITIZE (not prose observations or generic "updates"). If no changes are warranted, the output says so explicitly -- the null is not silence. |
| C-05 | **Confirmation gate** | essential | behavior | Output stops before modifying strategy.md and presents proposals for user review. The output contains a visible gate asking for YES/NO/REVISED confirmation. strategy.md is not modified until the user replies. |

---

## Recommended Criteria

Output is better with these. At least 2 of 3 are needed to reach the
golden threshold alongside all essential criteria passing.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **Evidence citation** | recommended | depth | Each proposal row names the specific signal artifact(s) that motivate the change -- not generic reasoning. An artifact filename appears in every non-null proposal. |
| C-07 | **Before/after diff** | recommended | format | For each proposed change, output shows the current strategy state (Before) and the proposed new state (After), making the delta concrete and auditable. A diff table or equivalent structure is present. |
| C-08 | **Inertia justification** | recommended | depth | Each proposal addresses why NO CHANGE is not sufficient. The burden of proof rests on change, not on stability. A "vs. NO CHANGE" column or equivalent justification is present in every non-null proposal row. |

---

## Aspirational Criteria

Raises the bar once essential and recommended are stable.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Type-labeled null declarations** | aspirational | format | When a change type has no proposals (e.g., no removals warranted), the output declares it explicitly with a type label: "REMOVALS: none -- inertia holds." Silence or a single unlabeled "no changes" covering multiple types does not pass. |
| C-10 | **Conflict detection** | aspirational | depth | Output identifies any NEW artifacts that contradict each other on the same strategy dimension before finalizing proposals. A conflict audit table or equivalent is present, even if it contains no conflicts (null declared explicitly). |

---

## Scoring Reference

| All essential pass | Recommended pass | Aspirational pass | Composite | Golden? |
|--------------------|-----------------|-------------------|-----------|---------|
| Yes | 3/3 | 2/2 | 100 | Yes |
| Yes | 3/3 | 0/2 | 90 | Yes |
| Yes | 2/3 | 2/2 | 90 | Yes |
| Yes | 2/3 | 0/2 | 80 | Yes (exactly) |
| Yes | 1/3 | 2/2 | 80 | Yes (exactly) |
| Yes | 1/3 | 0/2 | 70 | No |
| Yes | 0/3 | 2/2 | 70 | No |
| No (4/5) | any | any | max 72 | No |

---

## Criterion Notes

**C-03 (Delta detection)** is the criterion that separates a strategy
revision from a strategy rewrite. An output that treats all signals
equally -- ignoring the strategy date -- will propose changes based on
evidence already incorporated when the strategy was written. This produces
noise, not signal.

**C-05 (Confirmation gate)** is non-negotiable: the skill's contract with
the user is that strategy.md will not change without explicit confirmation.
An output that silently applies changes or omits the gate entirely fails
regardless of the quality of its proposals.

**C-08 (Inertia justification)** distinguishes preferences from decisions.
A proposal that cannot name a concrete consequence of leaving strategy.md
unchanged is a preference, not a decision. The "vs. NO CHANGE" test is the
core judgment required of this skill.
