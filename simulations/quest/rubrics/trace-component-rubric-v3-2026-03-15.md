Looking at the Round 2 scorecard, I'll extract the new excellence patterns before writing the updated rubric.

**Pattern 1 — Explicit incompleteness tokens (C-12)**
All four Golden variations cite "UNKNOWN permitted, omission not" in C-01 evidence, and all use MISSING-LOADING/MISSING-ERROR tokens in C-05. This pattern recurs across every mechanism (citation auditor, row protocol, phase registry, combined) but is not a standalone criterion. It's the clearest new signal: making gaps structurally visible rather than absent-by-silence.

**Pattern 2 — Active framework-neutrality enforcement (C-13)**
C-09 never reaches PASS across any Round 2 variation. The blocker is identical in every case: a role-setup directive saying "use framework vocabulary throughout" contradicts the Framework Notes section's requirement for a neutral core trace. The Framework Notes section is present (PARTIAL, not FAIL), but the role gives the model an escape route. The new criterion captures what PASS actually requires: the core trace sections must be free of framework-specific vocabulary, measurable directly from the artifact.

---

```markdown
# trace-component Rubric — v3 (2026-03-15)

**13 criteria across 3 tiers | 120 pts total**

v3 adds two aspirational criteria (C-12, C-13) extracted from Round 2 excellence signals.
C-12 captures the explicit-incompleteness-token pattern present in all four Round 2 Golden
variations. C-13 captures the active framework-neutrality enforcement gap that prevented C-09
from reaching PASS in any Round 2 variation.
Scoring bands scaled proportionally from v2 (x/110 → x/120).

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

## Aspirational Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Optimization opportunities called out** | depth | aspirational | Beyond flagging issues, the trace identifies at least one concrete optimization: a memoization candidate (useMemo, React.memo, reselect selector), a batching opportunity, or a render-scope reduction. The suggestion references the specific component and the expected render reduction. If no unnecessary re-renders exist, the section must state this explicitly and cite the relevant C-04 entries rather than being silently absent. |
| C-09 | **Framework-portable annotations** | format | aspirational | The trace uses framework-neutral vocabulary in a dedicated annotation layer (e.g., a "Framework Notes" section) so the core trace reads the same whether the reader knows React, Vue, Svelte, or Angular — with framework-specific mechanics called out separately. |
| C-10 | **Gap-visible format for essential sections** | format | aspirational | The trace uses a structured format (table or explicit numbered enumeration) for at least C-01 (event chain) and C-04 (re-render list) such that a missing entry is visually apparent to any reader without consulting the source code. A handler row that ends abruptly or a re-render list that omits skipped components is structurally obvious. Prose narrative alone does not satisfy this criterion. |
| C-11 | **Cross-section evidence chaining** | correctness | aspirational | At least two downstream sections (C-04, C-05, C-06, or C-07) explicitly cite upstream findings by reference — naming the specific state key, component name, or step established in an earlier section — rather than re-narrating from scratch. The final UI state (C-07) must trace back to at least one named row in C-03. The derivation chain event -> state delta -> re-render list -> final UI state is traceable by reference throughout the artifact. |
| C-12 | **Explicit incompleteness tokens** | correctness | aspirational | Every gap in the trace — a handler whose behavior cannot be determined, a loading branch whose existence is unconfirmed, an error path not yet verified — is marked with an explicit named token (UNKNOWN, MISSING-LOADING, MISSING-ERROR, or equivalent) rather than silently omitted. The reader must be able to distinguish "this entry does not exist" from "this entry was not determined." A trace passes if it contains at least one such token, or affirmatively states "no unknowns detected" after exhausting all known inputs. A trace that reaches a gap and simply ends the list without marking it fails this criterion. |
| C-13 | **Framework-neutral core trace enforcement** | format | aspirational | The core trace sections (C-01 through C-07) contain no framework-specific vocabulary in their narrative body. Framework-specific terms (e.g., useState, useEffect, v-model, @Input(), $store) are confined to the Framework Notes section or equivalent annotation layer. A trace where framework jargon appears in the event chain, state delta, or re-render list narrative — outside the designated annotation section — fails this criterion. Presence of a Framework Notes section is necessary but not sufficient: the core sections must themselves be clean. |

---

## Scoring Reference

| Band | Composite | Meaning |
|------|-----------|---------|
| Golden | all essential pass + >= 96 | Artifact is ground-truth quality |
| Acceptable | all essential pass + >= 79 | Useful with minor gaps |
| Marginal | all essential pass + < 79 | Essential covered but thin |
| Failing | any essential fails | Output not fit for purpose |

**Per-criterion points**: Essential 15 pts x 4 = 60 | Recommended 10 pts x 3 = 30 | Aspirational 5 pts x 6 = 30 | Total 120

---

## Rubric Notes

- C-01 and C-02 are the backbone: without a complete event chain and explicit component path the trace cannot be verified or used as a golden reference.
- C-03 and C-04 together constitute the state/render contract. An artifact that names state changes but omits which components re-render (or vice versa) fails both criteria.
- C-06 rewards honest issue analysis. Passing requires visible reasoning, not just absence of findings.
- C-10 and C-11 were added from Round 1 scorecard data. V-02 (structured tables) reached Golden because tabular format made gaps in C-06 and C-07 self-auditing. V-03 (lifecycle phases) reached Golden because phase completion gates and MISSING-token flow enforced cross-section evidence chaining across C-04, C-05, and C-07.
- C-12 was added from Round 2 scorecard data. All four Round 2 Golden variations cite "UNKNOWN permitted, omission not" in their C-01 evidence and use explicit MISSING-LOADING/MISSING-ERROR tokens in C-05. The pattern was present across every mechanism (citation auditor, row-citation protocol, phase registry, combined) but not yet a standalone criterion. Silent omission and explicit marking are not equivalent: a trace that omits an unknown handler is unauditable; a trace that marks it UNKNOWN is complete with a named gap.
- C-13 was added from Round 2 scorecard data. C-09 received PARTIAL in V-02, V-03, and V-04 — and FAIL in V-01 — because a Framework Notes section appeared in the artifact but the generating role instruction simultaneously directed "use framework vocabulary throughout." The contradiction gives the model an escape route: it can apply framework-specific terms in the core trace body and point to the Framework Notes as compliance evidence. C-13 closes this loophole by making the core trace sections themselves the evidence: if useState appears in the event chain narrative (not the Framework Notes), C-13 fails regardless of what annotation layer exists. C-09 and C-13 are complementary: C-09 requires the annotation layer; C-13 requires the core to be clean.
- C-08 was tightened in v3: the optional-section-with-no-justification pattern that produced PARTIAL across all four Round 2 variations is no longer acceptable. An absent optimization section must now state its reason and cite the C-04 entries that support skipping. This does not change the aspirational weight but raises the bar for PARTIAL → PASS.
- The composite is not a simple average — essential criteria carry 50% of the weight intentionally. A perfect recommended + aspirational score cannot rescue a trace with essential gaps.

---

**What changed from v2 → v3:**

Two new aspirational criteria extracted from the Round 2 differential. One criterion tightened.

- **C-12 (explicit incompleteness tokens)** — All four Round 2 Golden variations use UNKNOWN for undetermined handlers and MISSING-LOADING/MISSING-ERROR tokens for absent async branches. The pattern is mechanism-independent: it appears in the citation auditor design (V-01), the row-citation protocol (V-02), the phase registry (V-03), and the combined design (V-04). Silent omission of a gap is not the same as marking it explicitly, and a reader cannot distinguish the two from prose alone. This criterion rewards any trace that makes incompleteness structurally visible rather than invisible.

- **C-13 (framework-neutral core trace enforcement)** — C-09 (Framework-portable annotations) never reached PASS in any Round 2 variation. The blocker was identical in every case: the presence of a Framework Notes section in the artifact coexisted with a role-setup directive that said "use framework vocabulary throughout," giving the model license to embed framework-specific terms in the core trace body. C-13 makes the core sections themselves the evidence of neutrality. A trace where the event chain or state delta narrative is free of framework jargon passes; a trace where useState or equivalent appears outside the annotation layer fails. C-09 and C-13 together form a two-gate test: the annotation layer must exist (C-09) and the core must be clean (C-13).

- **C-08 tightened** — Optional sections that are silently absent produced PARTIAL across all Round 2 variations. v3 requires that a skipped optimization section include an explicit justification citing C-04 entries. This raises the PARTIAL → PASS bar without changing the criterion weight.

The total moves from 110 to 120 pts. Band thresholds scale proportionally: Golden ≥ 96 (was 88), Acceptable ≥ 79 (was 72).
```
