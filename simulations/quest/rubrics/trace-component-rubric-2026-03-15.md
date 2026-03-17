Written to `simulations/quest/rubrics/trace-component-rubric-2026-03-15.md`.

**9 criteria across 3 tiers:**

**Essential (4, 60 pts)**
- C-01: Event chain — every handler named in order, no gaps
- C-02: Component tree traversal — exact component names, prop/callback path, direction of flow
- C-03: State delta — key/slice + before/after for every update, including derived state
- C-04: Re-render list — all re-renders with reason, memoized skips explicitly noted

**Recommended (3, 30 pts)**
- C-05: Side effects — API calls, subscriptions, timers; loading + error branches named
- C-06: Issue flags — one of {unnecessary re-renders, missing loading states, error gaps, a11y} explicitly evaluated
- C-07: Final UI state — observable end state derivable from the state delta in C-03

**Aspirational (2, 10 pts)**
- C-08: Optimization candidates — concrete memoization or batching suggestion with component reference
- C-09: Framework-portable annotations — neutral core trace + framework mechanics in a separate section

The essential tier is intentionally heavy (60%) because a trace missing the event chain or component path can't be verified against code — it's not useful as a golden reference regardless of how rich the issue analysis is.
 | **State delta shown** | correctness | essential | Every state update triggered by the action is listed with: (a) the state key or slice, (b) the value before, (c) the value after. Selectors or derived state that depend on the changed key are also identified. |
| C-04 | **Re-render list complete** | coverage | essential | All components that re-render as a result of the state delta are enumerated. For each: the reason it re-rendered (prop change, context change, selector subscription). Components that did NOT re-render due to memoization or selector equality are explicitly noted as skipped. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Side effects and async calls identified** | depth | recommended | Every side effect triggered (API call, subscription update, timer, storage write) is named with: when it fires (sync vs deferred), what component or middleware owns it, and what UI state it updates on completion. Loading and error branches are both named. |
| C-06 | **Issue flags present** | depth | recommended | At least one of the four issue categories is explicitly evaluated: (a) unnecessary re-renders, (b) missing loading states, (c) error state gaps, (d) accessibility failures. Each issue found includes: component name, nature of the gap, and a one-line remediation hint. A "no issues found" conclusion is only passing if the trace is detailed enough to support it. |
| C-07 | **Final UI state described** | correctness | recommended | After the full trace, the artifact states the observable final UI state: which elements are visible/hidden, what text or data is displayed, what interactive state (disabled, focused, selected) components are in. The final state must be derivable from the state delta shown in C-03. |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Optimization opportunities called out** | depth | aspirational | Beyond flagging issues, the trace identifies at least one concrete optimization: a memoization candidate (useMemo, React.memo, reselect selector), a batching opportunity, or a render-scope reduction. The suggestion references the specific component and the expected render reduction. |
| C-09 | **Framework-portable annotations** | format | aspirational | The trace uses framework-neutral vocabulary in a dedicated annotation layer (e.g., a "Framework Notes" section) so the core trace reads the same whether the reader knows React, Vue, Svelte, or Angular -- with framework-specific mechanics called out separately. |

---

## Scoring Reference

| Band | Composite | Meaning |
|------|-----------|---------|
| Golden | all essential pass + >= 80 | Artifact is ground-truth quality |
| Acceptable | all essential pass + >= 65 | Useful with minor gaps |
| Marginal | all essential pass + < 65 | Essential covered but thin |
| Failing | any essential fails | Output not fit for purpose |

## Rubric Notes

- C-01 and C-02 are the backbone: without a complete event chain and explicit component path the trace cannot be verified or used as a golden reference.
- C-03 and C-04 together constitute the state/render contract. An artifact that names state changes but omits which components re-render (or vice versa) fails both criteria.
- C-06 rewards honest issue analysis. Passing requires visible reasoning, not just absence of findings.
- The composite is not a simple average -- essential criteria carry 60% of the weight intentionally. A perfect recommended + aspirational score cannot rescue a trace with essential gaps.
