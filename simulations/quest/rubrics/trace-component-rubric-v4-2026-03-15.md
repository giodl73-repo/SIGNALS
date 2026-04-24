Two new patterns from Round 3:

1. **C-14 — Vocabulary Contract as Role 1 artifact** — before any trace content, Role 1 produces a named table mapping framework terms → neutral equivalents; §1-§7 are bound to the neutral column; §8 is the sole framework zone; Role 3 audits for leakage. This inverts the R2 escape route where a role-level "use framework vocabulary throughout" instruction coexisted with a Framework Notes section.

2. **C-15 — Machine-readable incompleteness inventory** — Role 3 stamps the artifact with an aggregate count of all incompleteness tokens (UNKNOWN / MISSING-LOADING / MISSING-ERROR). Extends C-12 (individual gap marking) to a trace-level observable that can be compared across artifacts without reading every row.

Scoring: 13 criteria × existing weights + 2 × 5 pts aspirational = **130 pts total**. Golden threshold scales from 96/120 (80%) → **104/130**.

---

```markdown
# trace-component Rubric — v4 (2026-03-15)

**15 criteria across 3 tiers | 130 pts total**

v4 adds two aspirational criteria (C-14, C-15) extracted from Round 3 excellence signals.
C-14 captures the Vocabulary Contract first pattern from V-01, which closed the R2 escape
route where a role-level vocabulary directive coexisted with a Framework Notes section and
gave models a path to framework jargon in core trace sections. C-15 captures the
machine-readable incompleteness inventory from V-01's Role 3 stamp, which extends C-12's
per-gap token marking into a trace-level aggregate observable without reading every row.
Scoring bands scaled proportionally from v3 (x/120 → x/130).

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

## Aspirational Criteria (40 pts total)

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

---

## Scoring Reference

| Band | Composite | Meaning |
|------|-----------|---------|
| Golden | all essential pass + >= 104 | Artifact is ground-truth quality |
| Acceptable | all essential pass + >= 86 | Useful with minor gaps |
| Marginal | all essential pass + < 86 | Essential covered but thin |
| Failing | any essential fails | Output not fit for purpose |

**Per-criterion points**: Essential 15 pts x 4 = 60 | Recommended 10 pts x 3 = 30 | Aspirational 5 pts x 8 = 40 | Total 130

---

## Rubric Notes

- C-01 and C-02 are the backbone: without a complete event chain and explicit component path the trace cannot be verified or used as a golden reference.
- C-03 and C-04 together constitute the state/render contract. An artifact that names state changes but omits which components re-render (or vice versa) fails both criteria.
- C-06 rewards honest issue analysis. Passing requires visible reasoning, not just absence of findings.
- C-10 and C-11 were added from Round 1 scorecard data. V-02 (structured tables) reached Golden because tabular format made gaps in C-06 and C-07 self-auditing. V-03 (lifecycle phases) reached Golden because phase completion gates and MISSING-token flow enforced cross-section evidence chaining across C-04, C-05, and C-07.
- C-12 was added from Round 2 scorecard data. All four Round 2 Golden variations cite "UNKNOWN permitted, omission not" in their C-01 evidence and use explicit MISSING-LOADING/MISSING-ERROR tokens in C-05. The pattern was present across every mechanism (citation auditor, row-citation protocol, phase registry, combined) but not yet a standalone criterion. Silent omission and explicit marking are not equivalent: a trace that omits an unknown handler is unauditable; a trace that marks it UNKNOWN is complete with a named gap.
- C-13 was added from Round 2 scorecard data. C-09 received PARTIAL in V-02, V-03, and V-04 — and FAIL in V-01 — because a Framework Notes section appeared in the artifact but the generating role instruction simultaneously directed "use framework vocabulary throughout." The contradiction gives the model an escape route: it can apply framework-specific terms in the core trace body and point to the Framework Notes as compliance evidence. C-13 closes this loophole by making the core trace sections themselves the evidence: if useState appears in the event chain narrative (not the Framework Notes), C-13 fails regardless of what annotation layer exists. C-09 and C-13 are complementary: C-09 requires the annotation layer; C-13 requires the core to be clean.
- C-14 was added from Round 3 scorecard data. V-01 achieved the first PASS on C-13 via a three-layer mechanism: Role 1 produces a Vocabulary Contract table (framework term → neutral term) before the Trace Analyst runs; Role 2 binds §1-§7 to the neutral column of that contract; Role 3 audits for leakage and reports any violations. This inverts the R2 pattern where a role-level directive ("use framework vocabulary throughout") and a Framework Notes section coexisted with no enforcement. The key structural difference is that the Vocabulary Contract is a named artifact produced at invocation time, not a constraint buried in prose — the model cannot satisfy the constraint without producing the table, and the audit closes the loop. C-14 and C-13 are complementary: C-13 measures cleanliness of the output artifact; C-14 measures the presence of the production mechanism that makes cleanliness achievable.
- C-15 was added from Round 3 scorecard data. V-01's Role 3 stamp ("TRACE COMPLETE — {N} UNKNOWN tokens / {M} MISSING tokens / {K} issues flagged") makes the completeness level of the trace observable as a trace-level aggregate rather than requiring a reader to scan every row. This extends C-12 (which governs individual gap marking) to a quality-pipeline-grade signal: stamp counts can be compared across artifact variants, tracked across rounds, and used as a completeness gate in review pipelines without reading the full artifact body. C-12 is necessary but not sufficient for C-15: a trace can satisfy C-12 (all gaps marked) but fail C-15 (no aggregate summary). The zero-gap case is explicitly covered: an artifact with no gaps must still produce a stamp reading "0 UNKNOWN / 0 MISSING" rather than omitting the stamp, ensuring the absence of a stamp cannot be confused with a clean trace.
- C-08 was tightened in v3: the optional-section-with-no-justification pattern that produced PARTIAL across all four Round 2 variations is no longer acceptable. An absent optimization section must now state its reason and cite the C-04 entries that support skipping. Round 3 confirms this gap persists: both V-01 and V-02 scored PARTIAL because neither required render-reduction quantification in remediation hints. The v4 pass condition is unchanged from v3 — the quantification requirement was already present — but future variation templates should explicitly require the render-reduction estimate rather than allowing "one-line remediation hint" to satisfy the criterion with component name alone.
- The composite is not a simple average — essential criteria carry ~46% of the weight intentionally. A perfect recommended + aspirational score cannot rescue a trace with essential gaps.
```
