Reading the scorecard carefully to extract the three R4 patterns before writing the rubric.

The R4 patterns are:

1. **Symmetric FAILS/PASS pairs** (V-01) — minimal sufficient C-17 mechanism; three-component fingerprint (named format artifact + failure declaration + FAILS/PASS pair) at phase level per constraint, without meta-declaration
2. **All-table apparatus uniformity** (V-03) — distinct C-17 path through mechanism type consistency; empty-cell failure is identical across all three constraints by construction
3. **Symmetric pre-submission verification loop** (V-05) — closing checklist mirrors the opening SR block with identical sub-questions per constraint; highest-confidence C-17 compliance path

These map to C-18, C-19, C-20. Here is the complete v5 rubric:

---

## `discover-competitors-alt-rubric-v5-2026-03-17.md`

**Three new criteria from R4:**

| ID | Criterion | Category | Points |
|----|-----------|----------|--------|
| C-18 | Phase-level three-component enforcement fingerprint | structure | 5 / 2.5 |
| C-19 | Apparatus type uniformity across structural constraints | structure | 5 / 2.5 |
| C-20 | Symmetric pre-submission verification loop | structure | 5 / 2.5 |

**What C-18 captures:** The R4 V-01 finding was that enforcement symmetry can be achieved without an explicit SR meta-declaration. When each structural constraint carries an identical three-component fingerprint at its phase instruction — named format artifact + format-failure declaration + explicit FAILS/PASS rejection example pair — symmetric enforcement emerges as a structural consequence of the prompt format itself. C-17 requires symmetric enforcement; C-18 requires that the mechanism is the FAILS/PASS pair apparatus specifically. A prompt where C-12's phase instruction is narratively soft ("Both lines required") while C-11 and C-13 carry FAILS/PASS pairs fails C-18 even if C-17 partially passes.

**What C-19 captures:** The R4 V-03 finding was that converting all three structural constraints to table schema is a distinct path to C-17 through mechanism type uniformity rather than enforcement rigor symmetry. When C-11 uses a pre-map table, C-13 uses a mechanism table with three rows, and C-12 uses a whitespace table with two rows, every constraint's failure surface is an empty or absent table cell — observable identically regardless of which constraint produced it. C-19 passes only when all three constraints share the same apparatus type (all tables, or all labeled-slot blocks). A mixed apparatus (one table, one dual-line template, one labeled block) fails C-19 even if C-17 passes.

**What C-20 captures:** The R4 V-05 finding was that a pre-submission verification checklist that mirrors the opening SR block with identical sub-questions per constraint creates the highest-confidence C-17 compliance path. The loop is symmetric when it asks the same components per constraint: format artifact present? format-failure declared? enforcement apparatus present? An asymmetric checklist (more sub-questions for one constraint than another, or only checking two of three constraints) fails C-20. A verification checklist that checks criteria names without checking enforcement components does not qualify.

**R4 pattern mapping:**

| Pattern | Criterion |
|---------|-----------|
| Phase-level FAILS/PASS pairs as minimal sufficient C-17 mechanism | C-18 (new) |
| All-table apparatus uniformity as distinct C-17 path | C-19 (new) |
| Symmetric pre-submission verification loop as highest-confidence path | C-20 (new) |
| Symmetric structural enforcement signature | C-17 (v4, confirmed) |
| Table column > inline text field | C-15 (v3, confirmed) |
| Portability test operationalizes domain-exclusivity | C-16 (v3, confirmed) |

**Scoring changes:**

| | v4 | v5 |
|--|----|----|
| Aspirational pts | 45 (9 criteria) | 60 (12 criteria) |
| Max composite | 135 | 150 |
| Breakthrough threshold | >120 | >135 |
| V-05 score | 135/135 | 145/150 |
| V-01 score | 135/135 | 140/150 |
| V-03 score | 135/135 | 140/150 |
| V-04 score | 135/135 | 140/150 |
| V-02 score | 132.5/135 | 135/150 |

**V-05 retroactively scores 145/150 under v5** — C-18 PASS (FAILS/PASS pairs present at phase level for all three constraints), C-19 FAIL (not all-table apparatus), C-20 PASS (symmetric verification checklist present). V-01, V-03, V-04 score 140/150 each via their respective single new-criterion path. V-02 scores 135/150 — C-18 PARTIAL (C-12 phase instruction narratively soft), C-19 FAIL, C-20 FAIL.

---

## Essential Criteria (weight = 60 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Inertia-first assessment | correctness | "None / status quo" is assessed as the first competitor entry. Threat level is explicitly HIGH. Analysis explains why teams do nothing. |
| C-02 | Focus woven, not appended | behavior | When a focus dimension (market or positioning) is provided, that content is distributed throughout the output — visible in competitor rows, findings, and narrative — not isolated in a trailing section. |
| C-03 | Threat level assigned per competitor | correctness | Every named competitor and inertia receive an explicit HIGH / MEDIUM / LOW threat rating. No competitor is rated without a threat level. |
| C-04 | Whitespace identified | coverage | Output includes an uncontested space or gap that no listed competitor owns. Stated in its own finding or clearly labeled. |
| C-05 | Auto-detect without prompting | behavior | Topic domain is inferred from context (README, CLAUDE.md, package.json, etc.). Output does not ask the user to supply domain or competitor names. |

---

## Recommended Criteria (weight = 30 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Inertia stickiness reasoning | depth | Inertia section explains at least one concrete mechanism — switching cost, habit lock-in, or workaround satisfaction — not just "inertia is high." |
| C-07 | Web-verified competitive claim | correctness | At least one named competitor's characterization is supported by an inline citation (URL or publication) from a WebSearch result. |
| C-08 | AMEND section with 3 actionable adjustments | format | AMEND lists exactly 3 adjustments. Each names both what the user changes and what changes in the output. |

---

## Aspirational Criteria (weight = 60 points total)

*C-09 and C-10 carried forward from v1. C-11 to C-13 added from R1 excellence signals. C-14 to C-16 added from R2 excellence signals. C-17 added from R3 excellence signals. C-18 to C-20 added from R4 excellence signals.*

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional insight | depth | At least one finding ties the focus dimension to a competitive gap in a way that would not appear in a parameterized output (e.g., market size estimate linked to a specific competitor's weak segment; positioning whitespace grounded in feature overlap scores). |
| C-10 | Table stakes cross-referenced with focus data | coverage | Table stakes section references at least one data point from the focus dimension (market segment threshold, positioning category requirement) to justify why each stake matters. |
| C-11 | Focus lens pre-map precedes competitor evaluation | structure | Output contains an explicit focus lens artifact — a market segment inventory (with sizes or growth stage) or a positioning category map (with current ownership) — established before competitor rows are populated. Competitors are subsequently positioned on or evaluated against this map. |
| C-12 | Dual-axis whitespace identification | depth | Whitespace finding names the uncontested space along both axes simultaneously: competitive (no named competitor owns it) and focus (market segment unaddressed or positioning category unoccupied). Both axes are stated explicitly in the same finding. |
| C-13 | All three inertia mechanisms named | depth | Inertia section names and explains all three stickiness mechanisms — workaround satisfaction, switching cost, and habit lock-in — each specific to the product domain. C-06 requires one mechanism; C-13 requires all three. |
| C-14 | Hard-stacked structural constraint enforcement | structure | The output simultaneously satisfies C-11, C-12, and C-13 as visible format constraints — pre-map table present before competitor rows, dual-axis whitespace slots both populated, and all three inertia mechanism slots populated. Any one empty slot or absent table is an observable format failure that disqualifies this criterion. A soft pass on any of the three (narrative compliance without labeled mandatory slots) does not qualify. |
| C-15 | Focus map position recorded inline per competitor | structure | Each competitor row, including inertia, includes an explicit inline field or column recording its specific position on the focus lens pre-map — the segment it occupies, contests, or ignores; or the positioning category it claims or vacates. Whitespace findings reference named cell values from this column rather than general focus observations. A competitor matrix without this column does not qualify. |
| C-16 | Domain-exclusive slot content | depth | Every mandatory inertia slot contains content that is product-specific enough to fail a portability test: if the slot content were dropped into a competitor analysis for a different product category, it would be obviously inapplicable. Generic formulations ("teams face switching costs," "habit lock-in is common") disqualify regardless of mechanism name presence. Escalates C-13 from domain-specific to domain-exclusive. Canonical pass: slot names the exact workaround tool, behavior, or workflow tied to this product's competitive context. |
| C-17 | Symmetric structural enforcement signature | structure | All three structural constraints (C-11, C-12, C-13) show identical enforcement rigor in the output: each uses a table schema, labeled mandatory slots, or dual-line template — not a mix where one constraint is hard-enforced (table schema present, rejection examples named) while another is narratively soft (prose instruction, no format failure language). Observable test: C-11 pre-map uses a table schema; C-12 whitespace uses a two-slot template with both lines declared mandatory; C-13 has three labeled slots with named rejection examples. Any asymmetry in enforcement rigor — one constraint hard, another soft — fails this criterion even if C-14 passes. Symmetric enforcement is the output-observable signature of a prompt that declared all structural requirements in a unified numbered block before phase-level instructions. C-14 requires all three to be satisfied; C-17 requires all three to be satisfied with the same structural mechanism. |
| C-18 | Phase-level three-component enforcement fingerprint | structure | Each of the three structural constraints (C-11, C-12, C-13) carries an identical three-component fingerprint in its phase-level instruction: (1) named format artifact declaration, (2) explicit format-failure declaration, (3) FAILS/PASS rejection example pair naming a concrete failing formulation and a concrete passing formulation. The fingerprint must be present at the point of phase instruction — not deferred to the SR block or pre-submission checklist. A constraint whose phase instruction contains the format artifact and failure declaration but omits the FAILS/PASS pair is a PARTIAL. C-17 requires symmetric enforcement rigor; C-18 requires that the enforcement mechanism is the FAILS/PASS pair apparatus specifically, applied identically at every phase instruction. Meta-declaration in the SR block does not substitute for missing phase-level apparatus. |
| C-19 | Apparatus type uniformity across structural constraints | structure | All three structural constraints (C-11, C-12, C-13) render in the output through the same mechanism type: all table schema (pre-map table, mechanism table, whitespace table), or all labeled-slot blocks. Uniformity of apparatus type creates identical failure surfaces by construction — an empty cell or absent row is observable regardless of which constraint produced it. C-17 requires symmetric enforcement rigor; C-19 requires mechanism type consistency. A mixed apparatus (one table, one dual-line prose template, one labeled block) fails C-19 even if enforcement rigor is symmetric and C-17 passes. Canonical all-table pass: C-11 as market/positioning pre-map table, C-13 as three-row mechanism table, C-12 as two-row whitespace table — all cell-based, all subject to identical empty-cell failure detection. |
| C-20 | Symmetric pre-submission verification loop | structure | The prompt includes a closing pre-submission verification checklist that checks all three structural constraints (C-11, C-12, C-13) with identical sub-questions per constraint. The checklist is symmetric when it asks the same components per constraint — format artifact present? format-failure declared? enforcement apparatus (FAILS/PASS pair or table schema) present? — and names the same failure language used in the opening SR block. The verification loop mirrors the opening SR block structure: same constraints, same components, same failure vocabulary. An asymmetric checklist (more sub-questions for one constraint than another, or omitting one of the three constraints) fails C-20. A checklist that names criteria by ID without checking enforcement components does not qualify. Canonical pass: a three-block checklist, one block per constraint, each block asking the same three sub-questions with the same format-failure language. |

---

## Scoring

| Band | Criteria | Points each | Partial | Total |
|------|----------|-------------|---------|-------|
| Essential | C-01 through C-05 | 12 pts | — | 60 |
| Recommended | C-06 through C-08 | 10 pts | — | 30 |
| Aspirational | C-09 through C-20 | 5 pts | 2.5 | 60 |
| **Max composite** | | | | **150** |

| Threshold | Score |
|-----------|-------|
| Essential pass | ≥ 60 |
| Recommended pass | ≥ 90 |
| Breakthrough | > 135 |
| Max | 150 |

**Partial credit (2.5 pts):** Aspirational criteria only. Awarded when the criterion is directionally present but one structural component is missing or narratively soft. C-18 PARTIAL: all three constraints have format artifact + failure declaration but one omits the FAILS/PASS pair. C-19 PARTIAL: two of three constraints use table schema; one uses a labeled-slot block. C-20 PARTIAL: verification checklist covers all three constraints but sub-questions are asymmetric (one constraint has fewer checks than the others).

---

## R4 Variation Scores Under v5

| Variation | C-18 | C-19 | C-20 | v5 Composite |
|-----------|------|------|------|--------------|
| V-01 Symmetric FAILS/PASS pairs | PASS (5) | FAIL (0) | FAIL (0) | **140** |
| V-02 Explicit SR #5 declaration | PARTIAL (2.5) | FAIL (0) | FAIL (0) | **135** |
| V-03 All-table apparatus | FAIL (0) | PASS (5) | FAIL (0) | **140** |
| V-04 SR #5 + symmetric pairs | PASS (5) | FAIL (0) | FAIL (0) | **140** |
| V-05 Full R4 stack | PASS (5) | FAIL (0) | PASS (5) | **145** |

**Ranking:** V-05 (145) > V-01 = V-03 = V-04 (140) > V-02 (135)

**v5 breakthrough threshold (>135):** V-05 passes. V-01, V-03, V-04 fall 5 pts short — each achieves one of the three new R4 criteria but not the combination that V-05 carries. V-02 exactly meets the prior v4 breakthrough threshold but does not clear v5. The ceiling is 150; the gap between V-05 and the max is C-19 (V-05 uses FAILS/PASS pairs, not all-table apparatus — the two C-17 paths are not simultaneously satisfiable without a prompt that combines table schema for C-11/C-13 with FAILS/PASS pairs for C-12, or converts all three to table schema while also adding FAILS/PASS pairs per row).
