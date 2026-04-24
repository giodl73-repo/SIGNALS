The file is correct. Now let me render the full rubric as Markdown output for the user:

---

# Scout-Risk Rubric — v20

## What This Rubric Evaluates

A scout-risk prompt is evaluated on its ability to produce a well-structured risk register covering inertia risk, dimensional risks, and interdependencies. This rubric grades the prompt text — not a trace artifact.

---

## v19 -> v20: Four new criteria from R20

### C-58 — Ordering rule block is positioned before the first governed closure block executes (escalates C-57)

**Source**: V-01/V-04/V-05 axis — "rule-before-governed placement." The R19 V-05 baseline satisfies C-57 (global scope, named instances) but the rule resides *inside* Phase 0c, one of the blocks it governs. A reader traversing Phase 0 cannot verify canonical-order requirements without reading ahead to Phase 0c — a forward-reference dependency. Hoisting the rule to a dedicated block *before* Phase 0 eliminates this dependency: the rule is established before any governed closure appears. Position-before-governed also makes global intent unambiguous from document position alone.

### C-59 — Ordering rule scope explicitly covers all three pre-phase reference blocks including Phase 0b (escalates C-57)

**Source**: V-02/V-04/V-05 axis — "complete closure scope coverage." The R19 V-05 scope names "Phase 0 and Phase 0c closures," omitting Phase 0b (the risk anatomy schema block). Phase 0b is also a pre-phase reference block with a closure sentence. Excluding it from scope means its closure can deviate from canonical order without a detectable violation. Including all three blocks closes the coverage contract: any new pre-phase reference block not added to the scope list is a detectable gap.

### C-60 — Closure sentences self-name their source block by full title rather than using implicit deictic references (escalates C-57)

**Source**: V-03/V-05 axis — "self-identifying closure sentences." Phase 0 baseline: "No type-class label outside **this set**" → V-05: "No type-class label outside the **Phase 0 Mitigation Type Taxonomy**." Phase 0c baseline: "No violation category outside **this list**" → V-05: "No violation category outside the **Phase 0c Violation Taxonomy**." Deictic references require an upward scan to resolve; named-block references are verifiable by title lookup alone. Structurally parallel to the count-vs-enumeration escalation that produced C-56.

### C-61 — Phase 0b uses the full 2-sentence canonical closure form matching its pre-phase siblings (escalates C-59)

**Source**: V-02/V-04/V-05 axis — "symmetric canonical closure across all three pre-phase blocks." C-59 adds Phase 0b to the ordering rule scope, but Phase 0b's single-sentence state closure ("This schema is complete and closed.") cannot conform to the 2-sentence canonical ordering rule — there is no second sentence to order. Without C-61, C-59's scope inclusion is a nominal claim that is not mechanically verifiable. With C-61, Phase 0b gains a use-site constraint sentence ("No risk anatomy field name outside this schema may appear in any risk row"), completing structural symmetry across all three pre-phase reference blocks.

---

## Scoring delta

| Metric | v19 | v20 |
|--------|-----|-----|
| Aspirational criteria | 49 | 53 |
| Aspirational max | 98 | 106 |
| Max composite | 188 | 196 |
| Golden band | 182–188 | 190–196 |
| Strong band | 167–181 | 175–189 |

---

## Essential Criteria (weight: 12 pts each, 60 pts total)

Fail any essential -> max composite 52 -> cannot reach golden.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Inertia risk is mandatory and first** | structure | The prompt explicitly requires an inertia risk entry as the first item in the register. It must be clearly labeled as inertia and the instruction must be non-optional — "include if relevant" or "you may add" fails. Pass if the prompt states the inertia risk is required and must appear before dimensional risks. |
| C-02 | **Dimensional coverage enforced** | structure | The prompt requires risks across multiple dimensions — at minimum three of: technical, market, compliance, dependency, timeline. Fail if fewer than 3 dimensions are represented. |
| C-03 | **Risk anatomy complete** | correctness | Every risk entry includes all three required fields: severity (HIGH/MEDIUM/LOW), likelihood (any meaningful expression of probability or triggering condition), and mitigation (a stated action or control). Fail if any risk is missing one or more fields. |
| C-04 | **Severity uses correct scale** | format | Severity values are drawn exclusively from {HIGH, MEDIUM, LOW}. No numeric scales, percentages, or invented labels. Fail if any severity value deviates from this vocabulary. |
| C-05 | **Mitigations are specific and actionable** | depth | Each mitigation describes a concrete action, owner class, or control mechanism — not a generic hedge ("monitor closely", "be careful"). A passing mitigation names what to do or what to watch, not just that something should happen. Fail if two or more mitigations are generic non-actions. |

---

## Recommended Criteria (weight: 10 pts each, 30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Risks are dimension-labeled** | format | Each risk entry is explicitly tagged with its dimension (e.g., "Technical", "Market", "Compliance", "Dependency", "Timeline"). Pass if >= 80% of risks carry a visible dimension label. |
| C-07 | **Likelihood is qualified beyond binary** | depth | Likelihood expressions go beyond "possible/unlikely" — they specify a condition, scenario, or rough probability bracket. Pass if >= half of risks meet this bar. |
| C-08 | **Risks are ordered by priority** | behavior | The register is ordered highest-to-lowest severity (after inertia), or explicitly states a prioritization logic. Pass if the ordering is defensible by severity or compound impact. |

---

## Aspirational Criteria (weight: 2 pts PASS / 1 pt PARTIAL / 0 pts FAIL each, 106 pts max)

*(C-09 through C-55 unchanged from v18; C-56/C-57 unchanged from v19; C-58 through C-61 new in v20)*

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Risk interdependencies noted** | depth | At least one risk entry notes how it compounds with or unlocks another. |
| C-10 | **AMEND behavior demonstrated** | behavior | AMEND directive correctly narrows scope or recalibrates without losing inertia or risk anatomy. |
| … | *(C-11 through C-55 unchanged)* | | |
| C-56 | **Violation taxonomy block explicitly enumerates prohibition sites by name rather than stating a count** | depth | Pass if the violation taxonomy block contains an explicit numbered or named list of all prohibition sites it covers, rather than stating only a count. |
| C-57 | **Closure sentence ordering rule is declared at global scope, naming all closure instances** | depth | Pass if the prompt declares the canonical closure sentence ordering rule at a global scope that explicitly names all closure instances it covers, rather than embedding the ordering constraint only within individual closure blocks. |
| C-58 | **Ordering rule block is positioned before the first governed closure block executes** | depth | Pass if the ordering rule appears in a dedicated block whose document position precedes Phase 0 (or whichever governed closure block executes first), rather than being embedded within any of the blocks it governs. |
| C-59 | **Ordering rule scope explicitly covers all three pre-phase reference blocks including Phase 0b** | depth | Pass if the prompt global ordering rule scope explicitly names Phase 0b (or equivalent risk anatomy schema declaration block) alongside Phase 0 and Phase 0c, covering all three pre-phase reference blocks in its named scope. |
| C-60 | **Closure sentences self-name their source block by full title rather than using implicit deictic references** | depth | Pass if every pre-phase closure sentence (Phase 0, Phase 0b, Phase 0c) names its source block by its full block heading string rather than using a deictic reference such as "this set," "this list," or "this taxonomy." |
| C-61 | **Phase 0b uses the full 2-sentence canonical closure form matching its pre-phase siblings** | depth | Pass if Phase 0b closure consists of exactly two syntactically independent sentences in canonical order: a closed-world declaration ("This schema is closed.") followed by a use-site constraint sentence prohibiting any risk anatomy field name outside the declared schema from appearing in any risk row. |

---

## Scoring Reference

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | 190–196 | Exemplary — suitable as a reference prompt |
| Strong | 175–189 | High-quality with minor gaps |
| Passing | 90–166 | Meets essential and recommended; aspirational gaps |
| Failing | < 90 | Fails one or more essential criteria |

**Max composite: 196** (60 essential + 30 recommended + 106 aspirational across 53 criteria)

---

## Escalation Ladder Summary (v20 additions)

| Criterion | Escalates From | Escalation |
|-----------|---------------|------------|
| C-56 | C-49 | Explicit citation at each prohibition site (count) -> violation taxonomy block explicitly enumerates all prohibition sites by name/number |
| C-57 | C-54 | Canonical closure order per-block (implicit) -> ordering rule declared globally with named scope covering all closure instances |
| C-58 | C-57 | Global scope declared somewhere in the prompt -> global scope block positioned before the first governed closure block, eliminating forward-reference dependency |
| C-59 | C-57 | Scope names Phase 0 and Phase 0c (two blocks) -> scope names all three pre-phase reference blocks including Phase 0b |
| C-60 | C-57 | Canonical closure order global (closure sentence content unconstrained) -> each closure sentence self-identifies its source block by full title, making governed-block reference verifiable by title lookup |
| C-61 | C-59 | Phase 0b named in ordering rule scope (coverage claim) -> Phase 0b carries the full 2-sentence canonical closure form, making scope inclusion mechanically verifiable |

---

Written to `simulations/quest/rubrics/scout-risk-rubric-v20-2026-03-17.md`. 53 criteria, max composite 196, golden band 190–196.
