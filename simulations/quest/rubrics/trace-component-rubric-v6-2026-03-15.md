The two new patterns from Round 5 are clear from the scorecard differentials:

**C-18 — Role-level vocabulary enforcement gate**
Source: V-02 PARTIAL on C-09/C-13, V-04 PARTIAL on C-09/C-13. Both had the MAP constraint *stated* but no role-level blocking gate. V-01 passed both at full because it had "Role 2 binding constraint: 'Any MAP term appearing in §1–§7 outside §9 is a vocabulary violation'" — a named per-role transition check, not a passive instruction. The enforcement mechanism (can't proceed until check passes) is distinct from C-14 (contract exists) and C-13 (output is clean).

**C-19 — Pre-declared named column schemas for essential sections**
Source: V-03 PARTIAL on C-10 ("structured but no explicit table schemas declared"), V-04 PARTIAL on C-10 ("'Use a table' instruction but no schema declarations"). V-01/V-02 passed C-10 fully because they declared named schema blocks (TABLE-01, TABLE-02 with specific columns) before content generation. The schema-as-named-artifact pattern is distinct from C-10 (gap-visible format) — C-10 requires the output format to expose gaps; C-19 requires the schema to be declared in advance so the model fills named slots rather than inventing structure.

---

```markdown
# trace-component Rubric — v6 (2026-03-15)

**19 criteria across 3 tiers | 150 pts total**

v6 adds two aspirational criteria (C-18, C-19) extracted from Round 5 excellence signals.
C-18 captures the role-level vocabulary enforcement gate pattern from V-01, which turns the
vocabulary constraint from a passive instruction into a structural per-role transition check
that blocks core-section generation until the check passes. C-19 captures the pre-declared
named column schema pattern from V-01 and V-02, which turns format intent ("use a table")
into a named schema artifact that the generating role fills slot-by-slot — making absent
columns structurally apparent before any content is written. Both patterns were exposed by
partial scores on C-09, C-10, and C-13 in V-02, V-03, and V-04 where constraints were stated
but not enforced at the structural level. Scoring bands scaled proportionally from v5
(x/140 -> x/150).

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

## Aspirational Criteria (60 pts total)

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
| C-18 | **Role-level vocabulary enforcement gate** | format | aspirational | The vocabulary constraint established by the vocabulary contract (C-14) is enforced by an active, role-level gate: before the generating role outputs any core section (§1–§7), it must explicitly verify that no MAP entry from the vocabulary contract appears in that section's cell values. The gate takes the form of a named check step or transition condition in the role instructions — not a passive "use neutral vocabulary" instruction. A prompt where the vocabulary constraint is stated once and relies on the model to remember and self-apply it without a per-section or per-role gate does not pass. A prompt that includes a role-level gate condition — "verify: no MAP term appears in §N cell values before proceeding" or equivalent blanket pre-output check for the core-section generating role — passes if the gate is stated as a named, blocking constraint rather than advisory guidance. This criterion depends on C-14: a trace without a vocabulary contract cannot have an enforcement gate. |
| C-19 | **Pre-declared named column schemas for essential sections** | format | aspirational | Before any trace content is written, the schema for each essential section required by C-01 (event chain) and C-04 (re-render list) is declared as a named block — listing every column name, required token values (e.g., UNKNOWN, MISSING-LOADING), and fill rules. The schema block must appear before the first row of section content and must carry a name (e.g., "TABLE-01 SCHEMA:" or equivalent label). A section instruction that says "use a table with columns X, Y, Z" inline with content generation is not sufficient if the schema is not declared as a separate named block before content begins. A trace where the schema is implied by the output — recoverable by inspection but never declared — does not pass. This criterion builds on C-10: gap-visible format is necessary but not sufficient; the schema must be declared as a named pre-content artifact so the generating role fills into defined slots rather than inventing structure. |

---

## Scoring Reference

| Band | Composite | Meaning |
|------|-----------|---------|
| Golden | all essential pass + >= 120 | Artifact is ground-truth quality |
| Acceptable | all essential pass + >= 100 | Useful with minor gaps |
| Marginal | all essential pass + < 100 | Essential covered but thin |
| Failing | any essential fails | Output not fit for purpose |

**Per-criterion points**: Essential 15 pts x 4 = 60 | Recommended 10 pts x 3 = 30 | Aspirational 5 pts x 12 = 60 | Total 150

---

## Rubric Notes

- C-01 and C-02 are the backbone: without a complete event chain and explicit component path the trace cannot be verified or used as a golden reference.
- C-03 and C-04 together constitute the state/render contract. An artifact that names state changes but omits which components re-render (or vice versa) fails both criteria.
- C-06 rewards honest issue analysis. Passing requires visible reasoning, not just absence of findings.
- C-10 and C-11 were added from Round 1 scorecard data. V-02 (structured tables) reached Golden because tabular format made gaps in C-06 and C-07 self-auditing. V-03 (lifecycle phases) reached Golden because phase completion gates and MISSING-token flow enforced cross-section evidence chaining across C-04, C-05, and C-07.
- C-14 and C-15 were added from Round 3 scorecard data. V-01 (Vocabulary Contract as R1 blocking gate) reached Golden (123/130) by making vocabulary mapping non-skippable at the role level and by introducing an aggregate completeness stamp in Role 3.
- C-16 and C-17 were added from Round 4 scorecard data. V-01 scored 123/130; both gaps (C-08 absent, C-11 partial) are addressed by prompt structure, not new criteria. The two new patterns are PASS-THROUGH designation — which prevents vocabulary contracts from inventing neutral aliases for actual codebase identifiers — and active mismatch correction, which turns the completeness stamp from a passive count into a cross-checked, correctable audit record. V-02 scored 83/130 (Marginal) because the Format Contract mechanism addresses structural completeness (C-01–C-04, C-10) but leaves all vocabulary, token, and citation criteria unaddressed; the Format Contract alone is not sufficient for high aspirational scores.
- C-18 and C-19 were added from Round 5 scorecard data. V-01 scored 140/140 (perfect); the two new patterns are extracted from the partial gaps in V-02, V-03, and V-04. C-18 captures the role-level vocabulary enforcement gate: V-02 and V-04 each stated the MAP/vocabulary constraint but scored PARTIAL on C-09 and C-13 because the constraint was advisory — no per-role blocking check prevented jargon from appearing in cell values. V-01 passed at full because it declared "Role 2 binding constraint: 'Any MAP term appearing in §1–§7 outside §9 is a vocabulary violation'" as an active gate, not a passive instruction. C-19 captures the pre-declared named column schema: V-03 and V-04 each scored PARTIAL on C-10 because they had format intent ("use a table," "use a phase registry") without named schema declarations. V-01 and V-02 passed C-10 at full because they declared named schema blocks (TABLE-01, TABLE-02 with specific column names) before any content generation, so the generating role filled into defined slots rather than inventing structure.
- C-16 depends on C-14: a trace without a vocabulary contract cannot have a PASS-THROUGH designation. C-17 depends on C-15: a trace without a completeness stamp cannot have a correction protocol. C-18 depends on C-14: a trace without a vocabulary contract cannot have an enforcement gate. Awarding C-16, C-17, or C-18 without their parent criteria is a scoring error.
- C-19 builds on C-10 but does not strictly depend on it. A trace can have pre-declared schemas (C-19 passes) while still using list enumeration that fails to make gaps visually apparent (C-10 fails). However, pre-declared schemas without gap-visible format (C-10 fail, C-19 pass) would be unusual in practice.
```

---

Two new criteria extracted:

- **C-18 (role-level vocabulary enforcement gate)** — the discriminator between V-01's full pass on C-09/C-13 and V-02/V-04's partials. Stating the constraint once in a MAP instruction is not enforcement; a named per-role blocking check is. Depends on C-14.
- **C-19 (pre-declared named column schemas)** — the discriminator between V-01/V-02's full pass on C-10 and V-03/V-04's partials. "Use a table" is intent; a named TABLE-NN schema block declared before row 1 is a contract. Builds on C-10.

Totals move from 140 → 150 pts (12 aspirational × 5), bands scaled proportionally: Golden ≥ 120, Acceptable ≥ 100.
