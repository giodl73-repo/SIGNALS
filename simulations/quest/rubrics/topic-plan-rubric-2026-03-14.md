Rubric written to `simulations/quest/rubrics/topic-plan-rubric-2026-03-14.md`.

**Summary — topic-plan v1 rubric:**

| Tier | Count | Points | Criteria |
|------|-------|--------|---------|
| Essential | 5 | 60 | Read strategy, read signals, identify delta, type proposals, confirm gate |
| Recommended | 3 | 30 | Evidence citations, before/after view, all three change types |
| Aspirational | 2 | 10 | Namespace gap detection, conflicting signal detection |

**Design rationale:**

- **C-01/C-02** (reads inputs first) are separated because a skill could read `strategy.md` and fabricate signals, or cite real signals while ignoring the current strategy — both are failure modes worth detecting independently.
- **C-03** (delta, not inventory) is the core correctness gate: a model can easily list all signals without ever answering "what did the strategy miss?"
- **C-04** (typed proposals) enforces the three-type mandate at output time; untyped observations are a common mode failure.
- **C-05** (confirmation gate) is essential because auto-applying to `strategy.md` is destructive.
- **C-09/C-10** are aspirational because they require reasoning beyond the immediate diff — namespace awareness and contradiction detection are ceiling behaviors, not baseline.
 | essential | correctness | Output explicitly names what has changed or been learned *since the strategy was written* — not just what signals exist, but what they revealed that the strategy did not anticipate. A plain inventory of signals without naming the gap fails. |
| C-04 | **Proposes typed changes** | essential | correctness | Each proposed change is typed as one of: addition (new skill or coverage area), removal (obsolete coverage), or re-prioritization (shift in order or weight). Untyped observations without actionable proposals fail. |
| C-05 | **Requires user confirmation before writing** | essential | behavior | Output presents proposals and waits for user approval before modifying `strategy.md`. Any output that auto-applies changes or omits the confirmation gate fails. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **Cites signal evidence per change** | recommended | depth | Each proposed addition, removal, or re-prioritization is linked to at least one specific signal artifact that motivated it. Proposals without signal citations are present but weakly supported. |
| C-07 | **Before/after strategy summary** | recommended | format | Output shows a concise before/after view (or diff-style summary) of how the strategy would change — not just prose description. Makes it easy for the user to confirm the scope of changes without re-reading the full file. |
| C-08 | **Addresses all three change types** | recommended | coverage | Output considers additions *and* removals *and* re-prioritizations — even if the conclusion is "no changes needed" in a category. Proposals that cover only one type miss the full revision mandate. |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Detects namespace coverage gaps** | aspirational | depth | Output identifies which of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) have thin or missing signal coverage relative to the topic's current stage, and flags these as candidate additions. A flat coverage count without stage-relative framing is a partial pass. |
| C-10 | **Surfaces conflicting signals** | aspirational | depth | When two or more signals point in opposite directions (e.g., one feasibility signal says viable, another says blocked), output names the conflict and recommends how the revised strategy should handle it. Conflicts silently ignored in the proposal set fail. |

---

## Scoring Formula

- **Essential** (C-01–C-05): 60 pts total. All five must pass; any essential failure caps the score below passing regardless of recommended or aspirational performance.
- **Recommended** (C-06–C-08): 30 pts total. Each criterion contributes 10 pts equally.
- **Aspirational** (C-09–C-10): 10 pts total. Each criterion contributes 5 pts equally.
- **Composite**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`
- **Golden threshold**: all essential pass + composite ≥ 80.
