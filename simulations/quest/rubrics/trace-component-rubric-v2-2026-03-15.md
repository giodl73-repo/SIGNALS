Here is the complete updated rubric:

---

# trace-component Rubric — v2 (2026-03-15)

**11 criteria across 3 tiers | 110 pts total**

v2 adds two aspirational criteria (C-10, C-11) extracted from Round 1 excellence signals.
C-10 captures the gap-visible format property that drove V-02 to Golden.
C-11 captures the cross-section evidence chaining that drove V-03 to Golden.
Scoring bands scaled proportionally from v1 (x/100 -> x/110).

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Event chain complete** | coverage | essential | Every handler, middleware, and listener that fires between the triggering user action and final UI state is named in causal order. No gap is permitted: if handler A dispatches to handler B, both are listed with the dispatch shown between them. |
| C-02 | **Component tree traversal** | coverage | essential | Every component involved in the action is named with its exact codebase name. The direction of flow (parent -> child via props, child -> parent via callback, sibling via shared state) is explicit for each hop. The prop name or callback name that carries the signal is stated. |
| C-03 | **State delta shown** | correctness | essential | Every state update triggered by the action is listed with: (a) the state key or slice, (b) the value before, (c) the value after. Selectors or derived state that depend on the changed key are also identified. |
| C-04 | **Re-render list complete** | coverage | essential | All components that re-render as a result of the state delta are enumerated. For each: the reason it re-rendered (prop change, context change, selector subscription). Components that did NOT re-render due to memoization or selector equality are explicitly noted as skipped. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Side effects and async calls identified** | depth | recommended | Every side effect triggered (API call, subscription update, timer, storage write) is named with: when it fires (sync vs deferred), what component or middleware owns it, and what UI state it updates on completion. Loading and error branches are both named. |
| C-06 | **Issue flags present** | depth | recommended | At least one of the four issue categories is explicitly evaluated: (a) unnecessary re-renders, (b) missing loading states, (c) error state gaps, (d) accessibility failures. Each issue found includes: component name, nature of the gap, and a one-line remediation hint. A "no issues found" conclusion is only passing if the trace is detailed enough to support it. |
| C-07 | **Final UI state described** | correctness | recommended | After the full trace, the artifact states the observable final UI state: which elements are visible/hidden, what text or data is displayed, what interactive state (disabled, focused, selected) components are in. The final state must be derivable from the state delta shown in C-03. |

---

## Aspirational Criteria (20 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Optimization opportunities called out** | depth | aspirational | Beyond flagging issues, the trace identifies at least one concrete optimization: a memoization candidate (useMemo, React.memo, reselect selector), a batching opportunity, or a render-scope reduction. The suggestion references the specific component and the expected render reduction. |
| C-09 | **Framework-portable annotations** | format | aspirational | The trace uses framework-neutral vocabulary in a dedicated annotation layer (e.g., a "Framework Notes" section) so the core trace reads the same whether the reader knows React, Vue, Svelte, or Angular -- with framework-specific mechanics called out separately. |
| C-10 | **Gap-visible format for essential sections** | format | aspirational | The trace uses a structured format (table or explicit numbered enumeration) for at least C-01 (event chain) and C-04 (re-render list) such that a missing entry is visually apparent to any reader without consulting the source code. A handler row that ends abruptly or a re-render list that omits skipped components is structurally obvious. Prose narrative alone does not satisfy this criterion. |
| C-11 | **Cross-section evidence chaining** | correctness | aspirational | At least two downstream sections (C-04, C-05, C-06, or C-07) explicitly cite upstream findings by reference -- naming the specific state key, component name, or step established in an earlier section -- rather than re-narrating from scratch. The final UI state (C-07) must trace back to at least one named row in C-03. The derivation chain event -> state delta -> re-render list -> final UI state is traceable by reference throughout the artifact. |

---

## Scoring Reference

| Band | Composite | Meaning |
|------|-----------|---------|
| Golden | all essential pass + >= 88 | Artifact is ground-truth quality |
| Acceptable | all essential pass + >= 72 | Useful with minor gaps |
| Marginal | all essential pass + < 72 | Essential covered but thin |
| Failing | any essential fails | Output not fit for purpose |

**Per-criterion points**: Essential 15 pts x 4 = 60 | Recommended 10 pts x 3 = 30 | Aspirational 5 pts x 4 = 20 | Total 110

---

## Rubric Notes

- C-01 and C-02 are the backbone: without a complete event chain and explicit component path the trace cannot be verified or used as a golden reference.
- C-03 and C-04 together constitute the state/render contract. An artifact that names state changes but omits which components re-render (or vice versa) fails both criteria.
- C-06 rewards honest issue analysis. Passing requires visible reasoning, not just absence of findings.
- C-10 and C-11 were added from Round 1 scorecard data. V-02 (structured tables) reached Golden because tabular format made gaps in C-06 and C-07 self-auditing. V-03 (lifecycle phases) reached Golden because phase completion gates and MISSING-token flow enforced cross-section evidence chaining across C-04, C-05, and C-07. V-01 (role sequence) stayed Acceptable because prose format hid the same gaps that tables expose.
- The composite is not a simple average -- essential criteria carry 55% of the weight intentionally. A perfect recommended + aspirational score cannot rescue a trace with essential gaps.

---

**What changed from v1 → v2:**

Two new aspirational criteria extracted from the Round 1 differential. Both patterns were present in the Golden variations and absent in the Acceptable one:

- **C-10 (gap-visible format)** — V-02's tables gave C-06 and C-07 PASS because gaps are structurally impossible to hide in a table. V-01's prose gave both PARTIAL. This criterion rewards any structured format (table, numbered list) for the two highest-coverage-risk sections: event chain and re-render list.

- **C-11 (cross-section evidence chaining)** — V-03's phase-gate + token-passing design gave C-04, C-05, and C-07 PASS where V-01 got PARTIAL on all three. The mechanism was explicit: MISSING-LOADING/MISSING-ERROR tokens generated in Phase 5 were named and consumed in Phase 6; Phase 7 final UI state was required to derive from Phase 3. V-01 relied on the model "filling in" these connections. This criterion rewards any trace where downstream sections cite upstream findings by name.

The total moves from 100 to 110 pts. Band thresholds scale proportionally: Golden ≥ 88 (was 80), Acceptable ≥ 72 (was 65).
