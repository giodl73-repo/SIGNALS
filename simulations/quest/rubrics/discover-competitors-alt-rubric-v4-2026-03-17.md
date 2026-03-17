Written and verified. Here is the complete updated rubric:

---

## `discover-competitors-alt-rubric-v4-2026-03-17.md`

**One new criterion from R3:**

| ID | Criterion | Category | Points |
|----|-----------|----------|--------|
| C-17 | Symmetric structural enforcement signature | structure | 5 / 2.5 |

**What C-17 captures:** The R3 finding was that the V-02→V-03 5-point jump came entirely from a numbered structural requirements block declared at prompt start — not from improving individual phase-level mechanisms. When a prompt declares all structural requirements as a unified checklist before phase instructions, the output shows symmetric enforcement rigor across C-11, C-12, and C-13: each constraint shows the same apparatus (table schema, labeled mandatory slots or dual-line template, named rejection examples). A C-14 pass with one hard-enforced constraint and two narratively-soft ones fails C-17.

**R3 pattern mapping:**

| Pattern | Criterion |
|---------|-----------|
| Meta-constraint declaration is load-bearing | C-17 (new) |
| Table column > inline text field | C-15 (v3, confirmed) |
| Portability test operationalizes domain-exclusivity | C-16 (v3, confirmed) |

**Scoring changes:**

| | v3 | v4 |
|--|----|----|
| Aspirational pts | 40 (8 criteria) | 45 (9 criteria) |
| Max composite | 130 | 135 |
| Breakthrough threshold | >115 | >120 |
| V-05 score | 130/130 | 135/135 |
plicable algorithmic check where generic restatements fail automatically | C-16 (added in v3) |

**Scoring impact:** Aspirational band expands from 40 to 45 pts. Max composite 130 to 135. Breakthrough threshold raises to >120 (previously >115). V-05 retroactively scores 135/135 under v4 -- the V-03 component of the R3 stack satisfies C-17.

---

## Essential Criteria (weight = 60 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Inertia-first assessment | correctness | "None / status quo" is assessed as the first competitor entry. Threat level is explicitly HIGH. Analysis explains why teams do nothing. |
| C-02 | Focus woven, not appended | behavior | When a focus dimension (market or positioning) is provided, that content is distributed throughout the output -- visible in competitor rows, findings, and narrative -- not isolated in a trailing section. |
| C-03 | Threat level assigned per competitor | correctness | Every named competitor and inertia receive an explicit HIGH / MEDIUM / LOW threat rating. No competitor is rated without a threat level. |
| C-04 | Whitespace identified | coverage | Output includes an uncontested space or gap that no listed competitor owns. Stated in its own finding or clearly labeled. |
| C-05 | Auto-detect without prompting | behavior | Topic domain is inferred from context (README, CLAUDE.md, package.json, etc.). Output does not ask the user to supply domain or competitor names. |

---

## Recommended Criteria (weight = 30 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Inertia stickiness reasoning | depth | Inertia section explains at least one concrete mechanism -- switching cost, habit lock-in, or workaround satisfaction -- not just "inertia is high." |
| C-07 | Web-verified competitive claim | correctness | At least one named competitor's characterization is supported by an inline citation (URL or publication) from a WebSearch result. |
| C-08 | AMEND section with 3 actionable adjustments | format | AMEND lists exactly 3 adjustments. Each names both what the user changes and what changes in the output. |

---

## Aspirational Criteria (weight = 45 points total)

*C-09 and C-10 carried forward from v1. C-11 to C-13 added from R1 excellence signals. C-14 to C-16 added from R2 excellence signals. C-17 added from R3 excellence signals.*

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional insight | depth | At least one finding ties the focus dimension to a competitive gap in a way that would not appear in a parameterized output (e.g., market size estimate linked to a specific competitor's weak segment; positioning whitespace grounded in feature overlap scores). |
| C-10 | Table stakes cross-referenced with focus data | coverage | Table stakes section references at least one data point from the focus dimension (market segment threshold, positioning category requirement) to justify why each stake matters. |
| C-11 | Focus lens pre-map precedes competitor evaluation | structure | Output contains an explicit focus lens artifact -- a market segment inventory (with sizes or growth stage) or a positioning category map (with current ownership) -- established before competitor rows are populated. Competitors are subsequently positioned on or evaluated against this map. |
| C-12 | Dual-axis whitespace identification | depth | Whitespace finding names the uncontested space along both axes simultaneously: competitive (no named competitor owns it) and focus (market segment unaddressed or positioning category unoccupied). Both axes are stated explicitly in the same finding. |
| C-13 | All three inertia mechanisms named | depth | Inertia section names and explains all three stickiness mechanisms -- workaround satisfaction, switching cost, and habit lock-in -- each specific to the product domain. C-06 requires one mechanism; C-13 requires all three. |
| C-14 | Hard-stacked structural constraint enforcement | structure | The output simultaneously satisfies C-11, C-12, and C-13 as visible format constraints -- pre-map table present before competitor rows, dual-axis whitespace slots both populated, and all three inertia mechanism slots populated. Any one empty slot or absent table is an observable format failure that disqualifies this criterion. A soft pass on any of the three (narrative compliance without labeled mandatory slots) does not qualify. |
| C-15 | Focus map position recorded inline per competitor | structure | Each competitor row, including inertia, includes an explicit inline field or column recording its specific position on the focus lens pre-map -- the segment it occupies, contests, or ignores; or the positioning category it claims or vacates. Whitespace findings reference named cell values from this column rather than general focus observations. A competitor matrix without this column does not qualify. |
| C-16 | Domain-exclusive slot content | depth | Every mandatory inertia slot contains content that is product-specific enough to fail a portability test: if the slot content were dropped into a competitor analysis for a different product category, it would be obviously inapplicable. Generic formulations ("teams face switching costs," "habit lock-in is common") disqualify regardless of mechanism name presence. Escalates C-13 from domain-specific to domain-exclusive. Canonical pass: slot names the exact workaround tool, behavior, or workflow tied to this product's competitive context. |
| C-17 | Symmetric structural enforcement signature | structure | All three structural constraints (C-11, C-12, C-13) show identical enforcement rigor in the output: each uses a table schema, labeled mandatory slots, or dual-line template -- not a mix where one constraint is hard-enforced (table schema present, rejection examples named) while another is narratively soft (prose instruction, no format failure language). Observable test: C-11 pre-map uses a table schema; C-12 whitespace uses a two-slot template with both lines declared mandatory; C-13 has three labeled slots with named rejection examples. Any asymmetry in enforcement rigor -- one constraint hard, another soft -- fails this criterion even if C-14 passes. Symmetric enforcement is the output-observable signature of a prompt that declared all structural requirements in a unified numbered block before phase-level instructions. C-14 requires all three to be satisfied; C-17 requires all three to be satisfied with the same structural mechanism. |

---

## Scoring

| Band | Criteria | Points each | Partial | Total |
|------|----------|-------------|---------|-------|
| Essential | C-01 to C-05 | 12 | 6 | 60 |
| Recommended | C-06 to C-08 | 10 | 5 | 30 |
| Aspirational | C-09 to C-17 | 5 | 2.5 | 45 |
| **Max composite** | | | | **135** |

Composites above 120 indicate full-stack structural integration with symmetric constraint activation -- the output enforces every focus-woven and inertia-depth constraint simultaneously as hard format requirements of identical rigor. C-17 pass is the primary proof: it requires C-11, C-12, and C-13 to be hard-enforced through the same structural mechanism, not just all three satisfied.

Composites above 115 remain the v3 breakthrough threshold -- structural proof of full-stack constraint integration regardless of enforcement symmetry.

Composites above 100 remain the legacy threshold -- structural proof that the unified `discover-competitors-alt` skill outperforms parameterized `discover-competitors` on the same topic.

---

## Scoring Examples

| Scenario | Essential | Recommended | Aspirational | Composite |
|----------|-----------|-------------|--------------|-----------|
| Full v4 stack (all pass) | 5/5 | 3/3 | 9/9 | 135 |
| R3 V-05 baseline (C-17 PASS via V-03 component) | 5/5 | 3/3 | 9/9 | 135 |
| v3-era perfect (C-14 + C-15 + C-16, no C-17) | 5/5 | 3/3 | 8/9 | 132.5 |
| v2-era perfect (C-09 to C-13 hard, no C-14 to C-17) | 5/5 | 3/3 | 5/9 | 115 |
| v1-era perfect (C-09 + C-10 only) | 5/5 | 3/3 | 2/9 | 100 |
| No focus provided, base only | 4/5 (C-02 N/A) | 3/3 | 0/9 | 90* |
| Missing inertia-first | 4/5 | 3/3 | 1/9 | 48+30+5 = 83 -- FAIL (essential gap) |
| Focus appended not woven | 4/5 | 2/3 | 0/9 | 48+20+0 = 68 -- FAIL |

*When focus is not provided, C-02 is scored N/A and excluded from the essential denominator (4 essentials total, max essential score = 48, rescaled to 60 for composite). C-11, C-12, C-15, and C-17 are also N/A; max aspirational rescales to 25 (C-09, C-10, C-13, C-16 only).

---

## Evaluator Notes

**C-02 (focus woven):** This is the defining criterion separating `discover-competitors-alt` from `discover-competitors`. Fail if: focus content appears only in a clearly delimited appended section (e.g., "## Market Analysis" bolted on after the matrix). Pass if: market or positioning data appears inside competitor rows, informs whitespace/table-stakes sections, or is cited in narrative findings.

**C-09 (cross-dimensional insight):** Do not award if the insight is trivially additive (e.g., "Competitor X is strong AND the market is large"). Award only when the insight would require both the competitive and focus lenses simultaneously to derive. The V-02 pattern -- "the segment no one addresses, the category position no one owns" -- is the canonical pass example.

**C-11 (focus lens pre-map):** The map must be a distinct artifact established before competitor evaluation begins -- not inferred from scattered focus references later. A market segment inventory lists segments with quantitative attributes (size, growth stage, or ownership share); a positioning category map lists categories with current ownership or vacancy status. A prose paragraph that names segments without structure does not qualify. The V-04 mechanism -- where every subsequent competitor is evaluated "through the lens from Step 1" -- is the intended structural pattern.

**C-12 (dual-axis whitespace):** Both axes must appear in the same finding, not in separate findings that happen to coexist. "No competitor addresses the SME segment (competitive gap) and no one owns the workflow-native positioning category (focus gap)" qualifies. "Gap: no one does X. Also, market Y is large." does not qualify. C-12 subsumes but does not replace C-04 -- C-04 can pass on competitive-axis whitespace alone.

**C-13 (all three inertia mechanisms):** All three must be domain-specific -- not generic restatements of the mechanism name. "Workaround satisfaction: teams use Notion + Sheets duct-taped together and consider that solved" qualifies. "Workaround satisfaction: teams use workarounds" does not. C-13 is an escalation of C-06, not a replacement; C-06 can pass with one mechanism while C-13 requires all three.

**C-14 (hard-stacked constraint enforcement):** This is a meta-criterion -- it cannot pass unless C-11, C-12, and C-13 each pass as hard format constraints (labeled mandatory slots, visible format failures on empty or generic content). Narrative-level compliance on any of the three converts C-14 to a FAIL even if C-11/C-12/C-13 individually pass. A variation that hard-enforces only two of the three scores C-14 PARTIAL at 2.5 pts. The V-05 pattern -- three hard constraints combined in a single variation -- is the canonical pass. C-14 pass is the output-observable proof that hard-stacking was applied in the variation that produced it.

**C-15 (focus map position inline per competitor):** The column must be explicitly populated for every competitor row, including inertia (Competitor 0). A general focus section that discusses segments or categories does not qualify; the focus map position must be a per-row field in the competitor matrix. The V-04 "Phase 1 row" mechanism is the canonical implementation: each competitor carries a "Phase 1 row: [segment or category]" field that cross-references the pre-map table. When C-15 passes, whitespace findings can reference specific pre-map cells by name rather than by general focus category -- that structural grounding is what this criterion is designed to capture.

**C-16 (domain-exclusive slot content):** The portability test is the evaluation heuristic -- ask: could this exact slot content appear unchanged in a competitor analysis for a clearly different product (e.g., a payroll tool vs. a developer plugin)? If yes, the slot fails C-16 even if it passes C-13. The distinction: C-13 requires all three mechanisms to be named and domain-specific. C-16 requires the domain-specificity to be strong enough that the content is recognizably wrong for any other domain. Embedded slot rejection criteria in the prompt (e.g., "Generic restatements do not satisfy this slot") produce C-16-passing outputs by design; C-16 is the output-observable signature of that prompt technique.

**C-17 (symmetric structural enforcement signature):** C-14 tests whether all three constraints are satisfied; C-17 tests whether all three are satisfied through the same structural mechanism. A C-14 pass with asymmetric enforcement (one constraint uses a table schema, another uses prose instruction) fails C-17. The canonical enforcement signature: C-11 has a named table schema with a format-failure declaration; C-12 has a two-slot template with both slots labeled mandatory; C-13 has three labeled slots (WORKAROUND SATISFACTION / SWITCHING COST / HABIT LOCK-IN) with named rejection examples. When all three use the same structural apparatus -- named artifact plus format-failure label plus rejection example -- C-17 passes. The V-03 prompt mechanism that produces this is a numbered structural requirements block (Structural Requirement 1, Structural Requirement 2, Structural Requirement 3) declared before all phase instructions. The output-observable proof is that every constraint shows the same enforcement fingerprint, with no weaker-mechanism outlier among the three.

**A/B test context:** When comparing against `discover-competitors` output on the same topic, a `discover-competitors-alt` output scoring C-11 PASS with composite >= 100 is strong evidence that unified > parameterized for that run. C-14 PASS (composite >= 115) is strong evidence that full-stack hard-stacking is structurally superior to soft-instruction integration. C-17 PASS (composite >= 120) is strong evidence that a unified structural requirements block is the generative mechanism -- not individual phase-level constraints applied independently.
