Done. Here is the complete v5 rubric output:

---

# trace-component Rubric — v5 (2026-03-15)

**17 criteria across 3 tiers | 140 pts total**

v5 adds two aspirational criteria (C-16, C-17) extracted from Round 4 excellence signals.
C-16 captures the PASS-THROUGH designation pattern from V-01, which prevents vocabulary
contracts from inventing artificial neutral aliases for codebase proper names (component
names, handler names, store slices) that must remain navigable in the source. C-15 as
written makes stamp discrepancy a failure; C-17 captures the active mismatch correction
protocol demonstrated in V-01's Role 3, which turns stamp maintenance into a verifiable
correction workflow rather than a static pass/fail gate.
Scoring bands scaled proportionally from v4 (x/130 -> x/140).

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

## Aspirational Criteria (50 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Optimization opportunities called out** | depth | aspirational | Beyond flagging issues, the trace identifies at least one concrete optimization: a memoization candidate (useMemo, React.memo, reselect selector), a batching opportunity, or a render-scope reduction. The suggestion references the specific component and the expected render reduction. If no unnecessary re-renders exist, the section must state this explicitly and cite the relevant C-04 entries rather than being silently absent. |
| C-09 | **Framework-portable annotations** | format | aspirational | The trace uses framework-neutral vocabulary in a dedicated annotation layer (e.g., a "Framework Notes" section) so the core trace reads the same whether the reader knows React, Vue, Svelte, or Angular — with framework-specific mechanics called out separately. |
| C-10 | **Gap-visible format for essential sections** | format | aspirational | The trace uses a structured format (table or explicit numbered enumeration) for at least C-01 (event chain) and C-04 (re-render list) such that a missing entry is visually apparent to any reader without consulting the source code. A handler row that ends abruptly or a re-render list that omits skipped components is structurally obvious. Prose narrative alone does not satisfy this criterion. |
| C-11 | **Cross-section evidence chaining** | correctness | aspirational | At least two downstream sections (C-04, C-05, C-06, or C-07) explicitly cite upstream findings by reference — naming the specific state key, component name, or step established in an earlier section — rather than re-narrating from scratch. The final UI state (C-07) must trace back to at least one named row in C-03. The derivation chain event -> state delta -> re-render list -> final UI state is traceable by reference throughout the artifact. |
| C-12 | **Explicit incompleteness tokens** | correctness | aspirational | Every gap in the trace — a handler whose behavior cannot be determined, a loading branch whose existence is unconfirmed, an error path not yet verified — is marked with an explicit named token (UNKNOWN, MISSING-LOADING, MISSING-ERROR, or equivalent) rather than silently omitted. The reader must be able to distinguish "this entry does not exist" from "this entry was not determined." A trace passes if it contains at least one such token, or affirmatively states "no unknowns detected" after exhausting all known inputs. A trace that reaches a gap and simply ends the list without marking it fails this criterion. |
| C-13 | **Framework-neutral core trace enforcement** | format | aspirational | The core trace sections (C-01 through C-07) contain no framework-specific vocabulary in their narrative body. Framework-specific terms (e.g., useState, useEffect, v-model, @Input(), $store) are confined to the Framework Notes section or equivalent annotation layer. A trace where framework jargon appears in the event chain, state delta, or re-render list narrative — outside the designated annotation section — fails this criterion. Presence of a Framework Notes section is necessary but not sufficient: the core sections must themselves be clean. |
| C-14 | **Vocabulary Contract as pre-trace artifact** | format | aspirational | Before any trace content is written, the generating role produces a named vocabulary-contract table that maps every framework-specific term present in the codebase to its framework-neutral equivalent. The core trace sections (C-01 through C-07) are explicitly bound to the neutral column of that table; framework-specific terms from the contract appear only in the designated annotation section (§8/Framework Notes or equivalent). A subsequent audit role or step verifies that no framework term from the vocabulary contract leaked into core sections and reports any violations. A trace where the vocabulary mapping exists only as prose intent (not a named table artifact), where the binding constraint is stated but not audited, or where the audit step is absent does not pass. |
| C-15 | **Machine-readable incompleteness inventory** | correctness | aspirational | The artifact includes a trace-level completeness stamp that aggregates all incompleteness tokens from the body sections into observable counts by category (e.g., UNKNOWN: N / MISSING-LOADING: M / MISSING-ERROR: K / issues flagged: J). The stamp appears at the end of the artifact or in a designated summary section and is formatted as a structured summary line or block — not buried in prose. A trace that marks individual gaps per C-12 but has no aggregate summary fails this criterion. A trace with no gaps passes if the stamp affirmatively reads "0 UNKNOWN / 0 MISSING tokens" rather than omitting the stamp. The inventory must be derivable by counting the tokens in the body: any discrepancy between stamp counts and body token count is a failure. |
| C-16 | **Vocabulary contract PASS-THROUGH designation** | format | aspirational | The vocabulary contract produced per C-14 includes an explicit PASS-THROUGH designation for codebase proper names — component names, handler names, selector names, store slices, and any other identifiers that must appear unchanged in the trace to remain navigable in the source. The pass-through set is declared as a named column, addendum table, or labeled list within the vocabulary contract before any trace content is written. Core sections (§1–§7) use these names exactly as declared; no neutral alias is invented for a PASS-THROUGH name. A trace where the vocabulary contract neutralizes actual codebase identifiers (e.g., aliasing `useProductStore` to `StateManager`) fails, as does a trace that declares a vocabulary contract without a PASS-THROUGH section. The designation must be explicit and named, not implied by the presence of codebase names in the body. |
| C-17 | **Completeness stamp with active mismatch correction** | correctness | aspirational | The completeness stamp required by C-15 includes an active correction protocol: if any discrepancy is detected between the stamp's aggregate counts and the body token count during the audit role or step, the stamp is corrected in place and the correction is recorded inline (e.g., "Corrected: UNKNOWN count 3 -> 4; found additional UNKNOWN at §5 row 2"). A stamp that passively reports counts without a correction mechanism — or that silently accepts any count without cross-checking against the body — does not pass. The correction notation must identify the category corrected, the before/after counts, and the location of the discrepancy; a generic acknowledgment that a correction occurred is not sufficient. A trace with no gaps passes if the stamp records the cross-check result affirmatively (e.g., "Cross-checked: counts match body; no corrections required") rather than omitting the protocol. |

---

## Scoring Reference

| Band | Composite | Meaning |
|------|-----------|---------|
| Golden | all essential pass + >= 112 | Artifact is ground-truth quality |
| Acceptable | all essential pass + >= 93 | Useful with minor gaps |
| Marginal | all essential pass + < 93 | Essential covered but thin |
| Failing | any essential fails | Output not fit for purpose |

**Per-criterion points**: Essential 15 pts x 4 = 60 | Recommended 10 pts x 3 = 30 | Aspirational 5 pts x 10 = 50 | Total 140

---

## Rubric Notes

- C-01 and C-02 are the backbone: without a complete event chain and explicit component path the trace cannot be verified or used as a golden reference.
- C-03 and C-04 together constitute the state/render contract. An artifact that names state changes but omits which components re-render (or vice versa) fails both criteria.
- C-06 rewards honest issue analysis. Passing requires visible reasoning, not just absence of findings.
- C-10 and C-11 were added from Round 1 scorecard data. V-02 (structured tables) reached Golden because tabular format made gaps in C-06 and C-07 self-auditing. V-03 (lifecycle phases) reached Golden because phase completion gates and MISSING-token flow enforced cross-section evidence chaining across C-04, C-05, and C-07.
- C-14 and C-15 were added from Round 3 scorecard data. V-01 (Vocabulary Contract as R1 blocking gate) reached Golden (123/130) by making vocabulary mapping non-skippable at the role level and by introducing an aggregate completeness stamp in Role 3.
- C-16 and C-17 were added from Round 4 scorecard data. V-01 scored 123/130; both gaps (C-08 absent, C-11 partial) are addressed by prompt structure, not new criteria. The two new patterns are PASS-THROUGH designation — which prevents vocabulary contracts from inventing neutral aliases for actual codebase identifiers — and active mismatch correction, which turns the completeness stamp from a passive count into a cross-checked, correctable audit record. V-02 scored 83/130 (Marginal) because the Format Contract mechanism addresses structural completeness (C-01–C-04, C-10) but leaves all vocabulary, token, and citation criteria unaddressed; the Format Contract alone is not sufficient for high aspirational scores.
- C-16 depends on C-14: a trace without a vocabulary contract cannot have a PASS-THROUGH designation. C-17 depends on C-15: a trace without a completeness stamp cannot have a correction protocol. Awarding C-16 or C-17 without their parent criteria is a scoring error.

---

**Two new criteria extracted:**

**C-16 (PASS-THROUGH designation)** closes the over-correction failure mode: a vocabulary contract that neutralizes `useProductStore` -> `StateManager` satisfies C-14 literally but makes the trace unnavigable in the codebase. C-16 requires explicit exemption of proper names — the contract must declare what is in-scope for neutralization and what is not.

**C-17 (active mismatch correction)** elevates C-15 from audit gate to correction workflow. C-15 makes a count mismatch a failure; C-17 rewards the design pattern where the audit role detects, corrects, and records discrepancies inline, making the stamp itself a trustworthy artifact rather than a number that happened to match.

The dependency notes at the end prevent partial credit errors — C-16 without C-14 and C-17 without C-15 are incoherent combinations that would inflate scores on under-specified traces.
