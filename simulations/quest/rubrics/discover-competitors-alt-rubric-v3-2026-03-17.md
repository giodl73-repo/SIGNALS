Written to `simulations/quest/rubrics/discover-competitors-alt-rubric-v3-2026-03-17.md`.

---

## What changed in v3

Three new aspirational criteria from R2 patterns, converting the meta-observations about what made V-05 win into scoreable output properties:

| ID | Criterion | Source | What it captures |
|----|-----------|--------|-----------------|
| C-14 | Hard-stacked structural constraint enforcement | V-05 hard-stacking | All three of C-11/C-12/C-13 must be simultaneously hard-enforced (labeled mandatory slots, visible format failures). A soft pass on any one disqualifies. V-04 (two hard) scores PARTIAL; V-05 (three hard) is the canonical pass. |
| C-15 | Focus map position recorded inline per competitor | V-04 Phase 1 row column | Each competitor row (including inertia) carries an explicit field recording its pre-map position. Whitespace findings then reference named map cells, not general focus observations. Structural grounding without special instruction. |
| C-16 | Domain-exclusive slot content | V-03/V-04/V-05 slot rejection criteria | Inertia slots must pass the portability test — content would be recognizably wrong if transplanted to a different product. Escalates C-13 (domain-specific) to domain-exclusive. Output-observable signature of embedded slot rejection criteria in the prompt. |

**Scoring impact:** Aspirational band expands from 25 → 40 pts. Max composite 115 → 130. Breakthrough threshold raises to >115 (previously >100). V-05 retroactively scores ~127.5 under v3 (passes C-14 and C-15; C-16 depends on slot content in the unprovided V-05 detail).
ric answer before evaluation |

**Scoring change:** Aspirational expands from 25 pts (5 criteria) to 40 pts (8 criteria). Max composite is now 130. Scores above 115 are the v3 breakthrough signal — structural proof of full-stack constraint integration. V-05 would retroactively pass C-14 and C-15 under v3.

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

## Aspirational Criteria (weight = 40 points total)

*C-09 and C-10 carried forward from v1. C-11–C-13 added from R1 excellence signals. C-14–C-16 added from R2 excellence signals.*

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

---

## Scoring

| Band | Criteria | Points each | Partial | Total |
|------|----------|-------------|---------|-------|
| Essential | C-01–C-05 | 12 | 6 | 60 |
| Recommended | C-06–C-08 | 10 | 5 | 30 |
| Aspirational | C-09–C-16 | 5 | 2.5 | 40 |
| **Max composite** | | | | **130** |

Composites above 115 indicate full-stack structural integration — the output enforces every focus-woven and inertia-depth constraint simultaneously as hard format requirements, not quality suggestions. C-14 pass is the primary proof: it requires C-11, C-12, and C-13 to all be hard-enforced, not just narratively present.

Composites above 100 remain the legacy threshold — structural proof that the unified `discover-competitors-alt` skill outperforms parameterized `discover-competitors` on the same topic.

---

## Scoring Examples

| Scenario | Essential | Recommended | Aspirational | Composite |
|----------|-----------|-------------|--------------|-----------|
| Full v3 stack (all pass) | 5/5 | 3/3 | 8/8 | 130 |
| V-05 baseline (v2 perfect + C-14 + C-15) | 5/5 | 3/3 | 7/8 | 127.5 |
| v2-era perfect (C-09–C-13 hard, no C-14–C-16) | 5/5 | 3/3 | 5/8 | 115 |
| v1-era perfect (C-09 + C-10 only) | 5/5 | 3/3 | 2/8 | 100 |
| No focus provided, base only | 4/5 (C-02 N/A) | 3/3 | 0/8 | 90* |
| Missing inertia-first | 4/5 | 3/3 | 1/8 | 48+30+5 = 83 — FAIL (essential gap) |
| Focus appended not woven | 4/5 | 2/3 | 0/8 | 48+20+0 = 68 — FAIL |

*When focus is not provided, C-02 is scored N/A and excluded from the essential denominator (4 essentials total, max essential score = 48 → rescaled to 60 for composite). C-11, C-12, C-15 are also N/A; max aspirational rescales to 25 (C-09, C-10, C-13, C-16 only).

---

## Evaluator Notes

**C-02 (focus woven):** This is the defining criterion separating `discover-competitors-alt` from `discover-competitors`. Fail if: focus content appears only in a clearly delimited appended section (e.g., "## Market Analysis" bolted on after the matrix). Pass if: market or positioning data appears inside competitor rows, informs whitespace/table-stakes sections, or is cited in narrative findings.

**C-09 (cross-dimensional insight):** Do not award if the insight is trivially additive (e.g., "Competitor X is strong AND the market is large"). Award only when the insight would require both the competitive and focus lenses simultaneously to derive. The V-02 pattern — "the segment no one addresses, the category position no one owns" — is the canonical pass example.

**C-11 (focus lens pre-map):** The map must be a distinct artifact established before competitor evaluation begins — not inferred from scattered focus references later. A market segment inventory lists segments with quantitative attributes (size, growth stage, or ownership share); a positioning category map lists categories with current ownership or vacancy status. A prose paragraph that names segments without structure does not qualify. The V-04 mechanism — where every subsequent competitor is evaluated "through the lens from Step 1" — is the intended structural pattern.

**C-12 (dual-axis whitespace):** Both axes must appear in the same finding, not in separate findings that happen to coexist. "No competitor addresses the SME segment (competitive gap) and no one owns the 'workflow-native' positioning category (focus gap)" qualifies. "Gap: no one does X. Also, market Y is large." does not qualify. C-12 subsumes but does not replace C-04 — C-04 can pass on competitive-axis whitespace alone.

**C-13 (all three inertia mechanisms):** All three must be domain-specific — not generic restatements of the mechanism name. "Workaround satisfaction: teams use Notion + Sheets duct-taped together and consider that solved" qualifies. "Workaround satisfaction: teams use workarounds" does not. C-13 is an escalation of C-06, not a replacement; C-06 can pass with one mechanism while C-13 requires all three.

**C-14 (hard-stacked constraint enforcement):** This is a meta-criterion — it cannot pass unless C-11, C-12, and C-13 each pass as hard format constraints (labeled mandatory slots, visible format failures on empty or generic content). Narrative-level compliance on any of the three converts C-14 to a FAIL even if C-11/C-12/C-13 individually pass. A variation that hard-enforces only two of the three (e.g., V-04) scores C-14 PARTIAL at 2.5 pts. The V-05 pattern — three hard constraints combined in a single variation — is the canonical pass. C-14 pass is the output-observable proof that hard-stacking was applied in the variation that produced it.

**C-15 (focus map position inline per competitor):** The column must be explicitly populated for every competitor row, including inertia (Competitor 0). A general focus section that discusses segments or categories does not qualify; the focus map position must be a per-row field in the competitor matrix. The V-04 "Phase 1 row" mechanism is the canonical implementation: each competitor carries a "Phase 1 row: [segment or category]" field that cross-references the pre-map table. When C-15 passes, whitespace findings can reference specific pre-map cells by name rather than by general focus category — that structural grounding is what this criterion is designed to capture.

**C-16 (domain-exclusive slot content):** The portability test is the evaluation heuristic — ask: could this exact slot content appear unchanged in a competitor analysis for a clearly different product (e.g., a payroll tool vs. a developer plugin)? If yes, the slot fails C-16 even if it passes C-13. The distinction: C-13 requires all three mechanisms to be named and domain-specific. C-16 requires the domain-specificity to be strong enough that the content is recognizably wrong for any other domain. Embedded slot rejection criteria in the prompt (e.g., "Generic restatements do not satisfy this slot") produce C-16-passing outputs by design; C-16 is the output-observable signature of that prompt technique.

**A/B test context:** When comparing against `discover-competitors` output on the same topic, a `discover-competitors-alt` output scoring C-11 PASS with composite >= 100 is strong evidence that unified > parameterized for that run. C-14 PASS (composite >= 115 under v3) is strong evidence that full-stack hard-stacking is structurally superior to soft-instruction integration.
