Reading the R8 scorecard to extract the three new patterns before writing.

**Three new excellence signals from R8:**

1. **V-01 R8** — Because block converted from bullet list to 4-column named-column table (Phase | Label | Citation | Claim). C-23 enforces column-schema in evidence phases; this enforces it in the *synthesis layer itself*. New criterion.

2. **V-02 R8** — Phase 1b rivals table gains a fifth column: "Response Strategy (how we win vs. this rival)." Rivals analysis now prescribes, not just describes. New criterion.

3. **V-03 R8** — All 24 v7 criteria pass with instructional prose stripped. Column headers, gate annotations, and section ordering alone carry every semantic requirement. Prose-free compressibility demonstrated as a design property. New criterion.

Scoring model update: 16 → 19 aspirational criteria, denominator /19, each worth 10/19 ≈ 0.526 pts.

---

```markdown
# campaign-decide-rubric-v8-2026-03-16.md

**Quest**: campaign-decide
**Version**: v8
**Date**: 2026-03-16
**Denominator**: /19 aspirational (10 pts total — 0.526 pts each)
**Max composite**: 100.0

---

## Version History

| Version | Date | Change Summary |
|---------|------|----------------|
| v1–v5 | 2026-03-14 | Initial criteria through V-04 R7 base |
| v6 | 2026-03-15 | C-14..C-22 added (V-04 R7 structural criteria); aspirational denominator /14 |
| v7 | 2026-03-16 | C-23 (column-header schema enforcement) and C-24 (sub-phase synthesis slot alignment) extracted from R6; C-17 updated: when C-21 in effect, 6-slot pass condition applies; denominator /16 |
| v8 | 2026-03-16 | C-25 (Because block column-schema enforcement), C-26 (per-rival response-strategy column), C-27 (prose-free structural sufficiency) extracted from R8; denominator /19 |

---

## Scoring Model

| Tier | IDs | Pts each | Total | Condition |
|------|-----|----------|-------|-----------|
| Essential | C-01..C-05 | 12 | 60 | All must pass — any fail = output fails |
| Recommended | C-06..C-08 | 10 | 30 | Output is better with these |
| Aspirational | C-09..C-27 | 0.526 | 10 | Raise the bar |
| **Max composite** | | | **100.0** | |

---

## v8 Changelog — New Criteria from Round 8

### C-25 — Because block column-schema enforcement (format)

V-01 R8's conversion of the Because bullet list into a 4-column named-column table
(Phase | Label | Citation | Claim) demonstrates that the synthesis layer can carry the same
column-schema discipline as the evidence layer. C-23 enforces column-schema in per-phase
evidence tables; C-25 requires the Because block itself to be a named-column table, making
synthesis-layer schema violations structurally visible without reading row content. A
6-slot bullet list — even one with labeled Phase 1a/1b slots (C-24 PASS) and hybrid
citations (C-12 PASS) — fails C-25. The Because block must have a header row with named
columns; the minimum viable schema is (Phase, Label, Citation, Claim) or a superset.
Prerequisites: C-12, C-23, C-24.

### C-26 — Per-rival response-strategy column (depth)

V-02 R8's addition of a fifth column "Response Strategy (how we win vs. this rival)" to
the Phase 1b rivals table demonstrates that rival analysis can prescribe, not just
describe. Competitors analysis currently records rival identity, positioning, and
weakness (C-11 schema); C-26 requires Phase 1b to carry an explicit response strategy
per rival — how the feature under evaluation wins against each listed competitor. A
four-column rivals table with no response column fails C-26. The response strategy must
appear as a named column in the Phase 1b table, not as prose in the synthesis block.
Prerequisite: C-11. No interaction with C-04 (inertia-first ordering is about Phase 1a
preceding Phase 1b — adding columns to Phase 1b does not contaminate inertia-first
sequencing).

### C-27 — Prose-free structural sufficiency (format)

V-03 R8's minimal-prompt experiment demonstrates that all 24 v7 criteria are purely
structural: they score column headers, gate annotations, section ordering, citation
formats, and slot counts — none require instructional prose. C-27 is satisfied when the
template is informationally complete without prose wrappers: every semantic requirement
is carried by a column header, a gate annotation, a section label, or a citation-format
token. A template that requires prose to communicate a criterion's intent fails C-27 —
the structure itself must be the instruction. Concretely: FINDING REGISTER preamble
compressed to one line; Phase 0 and Phase 5 sub-table prose labels removed; gate
annotations, phase tables, domain column headers, and Because block retained. All 24
prior criteria continue to pass in this compressed form. No prerequisites (tests a
property of the full template, not an additive feature).

---

### Score impacts under v8 (denominator /19, 0.526 pts each)

| Variant | C-25 | C-26 | C-27 | Aspirational pts | v8 Composite |
|---------|------|------|------|-----------------|--------------|
| V-01 R8 (Because table; no response-strategy; prose present) | PASS | FAIL | FAIL | 17/19 × 10 = 8.95 | **98.95** |
| V-02 R8 (response-strategy column; bullet Because; prose present) | FAIL | PASS | FAIL | 17/19 × 10 = 8.95 | **98.95** |
| V-03 R8 (prose-free; bullet Because; no response-strategy) | FAIL | FAIL | PASS | 17/19 × 10 = 8.95 | **98.95** |

All three R8 variants converge at 98.95 by structurally distinct paths. The first template
combining C-25 (Because table) + C-26 (response-strategy column) + C-27 (prose-free
compressibility) on the full 24-criterion v7 base reaches 100.0 under v8.

Note on prior versions: V-01 R8 held 100.0 under v7 (16/16 aspirational). Under v8 it
drops to 98.95 (17/19). V-01, V-02, and V-03 R8 each hold one of the three new criteria;
none holds all three.

---

## Essential Criteria (60 pts total — output must pass all five)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Recommendation stated** | correctness | essential | Output includes an explicit, labeled build/no-build (commit/pause/pivot/abandon) recommendation. Absence of a stated recommendation is an automatic fail. |
| C-02 | **Confidence level stated** | correctness | essential | Recommendation is accompanied by a stated confidence (e.g., High/Medium/Low or a numeric percentage). A recommendation without confidence is incomplete. |
| C-03 | **All six sub-skill domains represented** | coverage | essential | Output contains distinct sections or evidence blocks attributable to each of the six orchestrated skills: competitors, feasibility, market, hypothesis, web-search evidence, and synthesis. Missing any domain means the campaign is incomplete. |
| C-04 | **Inertia-first competitor framing** | correctness | essential | The competitor analysis leads with incumbent/inertia forces (status-quo cost, switching cost, or "why people don't change") before listing named rivals. The orchestration spec requires this ordering. |
| C-05 | **Evidence-to-recommendation traceability** | correctness | essential | The recommendation is visibly grounded in evidence from the brief (citations, section references, or explicit "because" statements). A recommendation that floats free of its evidence base fails. |

---

## Recommended Criteria (30 pts total — output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Structured decision brief format** | format | recommended | Output uses a consistent document structure: titled sections, a summary block, and a clear recommendation block. Prose-only dumps without section hierarchy do not pass. |
| C-07 | **Risk and counter-evidence acknowledged** | depth | recommended | Brief surfaces at least one risk, caveat, or piece of counter-evidence that could undermine the recommendation. A one-sided brief fails this criterion. |
| C-08 | **Hypothesis disposition explicit** | depth | recommended | Each hypothesis entered into prove-hypothesis has an explicit outcome (confirmed / refuted / inconclusive). Hypotheses that disappear without resolution fail this criterion. |

---

## Aspirational Criteria (10 pts total — 0.526 pts each — denominator /19)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Confidence calibration narrative** | depth | Brief explains *why* confidence is rated as it is — naming the specific evidence gaps or strength factors that drove the rating, not just asserting a level. |
| C-10 | **Actionable next steps conditioned on recommendation** | behavior | If build: output includes a concrete next step (e.g., scope spike, prototype). If no-build: output includes an exit condition or revisit trigger. Generic "further research needed" does not pass. |
| C-11 | **Per-phase required-field schema** | format | Each evidence phase has its own structured schema with required named rows (not just an overall summary block). The brief is verifiable at the phase level. A single recommendation block with no per-phase field structure does not pass. |
| C-12 | **Templated citation syntax in recommendation** | correctness | The recommendation's evidence citations follow a prescribed format (e.g., "because Phase [N], [section reference]"), making traceability mechanically auditable at a glance. Free-prose citations such as "as shown above" or "based on the evidence" do not pass. |
| C-13 | **Hypothesis-prior anchoring** | behavior | The hypothesis is committed as an explicit prior belief before any evidence phase executes (Phase 1 or equivalent). Synthesis then reports whether evidence confirmed, refuted, or left the hypothesis inconclusive — as a genuine experimental outcome. A hypothesis first stated in the synthesis phase, or inferred post-hoc from findings, does not pass. |
| C-14 | **FINDING REGISTER header block** | format | Output opens with a named FINDING REGISTER section that precedes all phase sections. Findings identified anywhere in the document are registered here by FID. |
| C-15 | **FID citation discipline** | correctness | Every claim in the synthesis and recommendation blocks cites at least one FID from the FINDING REGISTER. Unanchored synthesis claims fail. |
| C-16 | **Gate annotation on Phase 1a** | format | Phase 1a carries an explicit gate annotation (`[COMPLETE BEFORE PHASE 1b]` or equivalent) enforcing inertia-evidence-first ordering at the structural level, not just by prose instruction. |
| C-17 | **Synthesis slot count matches skill + sub-phase splits** | format | The Because block has one slot per orchestrated skill phase. When C-21 is in effect, Phase 1 splits into 1a (Inertia) and 1b (Rivals), yielding 6 slots (Phase 1a + Phase 1b + Phases 2/3/4/5). A template with C-21 in effect that retains a single "Phase 1" slot fails this criterion. Without C-21, 5 slots (Phases 1–5) satisfies. Prerequisite: C-21 when 6 slots are required. |
| C-18 | **Counter-evidence registered as FID** | depth | The counter-evidence block (C-07) is not prose-only — it has a FID entry in the FINDING REGISTER, making it addressable by downstream criteria. Prerequisite: C-14, C-07. |
| C-19 | **Recommendation block as named-column table** | format | The Phase 5 recommendation row (F5-02 or equivalent) is a named-column table with at minimum: COMMIT/PAUSE/PIVOT/ABANDON column, Confidence column, Rationale column. A prose recommendation block without column headers fails. |
| C-20 | **Conditioned next-step row present** | behavior | A distinct row or table (F5-04 or equivalent) carries conditioned next steps: COMMIT branch and no-build branch as separate labeled cells. A single merged next-step field fails. Prerequisite: C-10. |
| C-21 | **Phase 1 split into 1a (Inertia) and 1b (Rivals)** | format | Phase 1 is structurally divided into two sub-phases with distinct section headers: Phase 1a for inertia/incumbent forces and Phase 1b for named rivals. A monolithic Phase 1 section fails. Prerequisite: C-04. |
| C-22 | **Phase 0 hypothesis record at pre-evidence position** | behavior | Phase 0 is a structurally distinct section that precedes Phase 1. It contains the hypothesis prior commitment as a named-column record (FID, Hypothesis Claim, Outcome). A hypothesis first appearing inside Phase 1 or later fails. Prerequisite: C-13. |
| C-23 | **Column-header schema enforcement** | format | Every per-phase evidence table uses column headers to enumerate required fields — schema lives in the header row, not in data-cell row labels. `\| Field \| Value \|` two-column layouts explicitly fail; the field names must be column headers. Named rows (C-11 PASS) are insufficient — the column header must carry the schema. Prerequisite: C-11. |
| C-24 | **Sub-phase synthesis slot alignment** | format | When Phase 1a/1b exist (C-21 in effect), the Because block carries two labeled slots — `Phase 1a (Inertia)` and `Phase 1b (Rivals)` — not a merged `Phase 1` slot. The synthesis layer mirrors the evidence layer's structural split. Prerequisites: C-17 and C-21. |
| C-25 | **Because block column-schema enforcement** | format | The Because block is a named-column table (minimum schema: Phase, Label, Citation, Claim) — not a bullet list, even a labeled one. C-23 enforces column-schema in per-phase evidence tables; C-25 enforces it in the synthesis layer itself. A bullet list that passes C-12 (templated citation syntax) and C-24 (1a/1b slot labels) still fails C-25 if the Because layer has no column headers. Prerequisites: C-12, C-23, C-24. |
| C-26 | **Per-rival response-strategy column** | depth | Phase 1b rivals table carries a named "Response Strategy" column (or equivalent) specifying how the feature under evaluation wins against each listed rival. Rivals analysis must prescribe, not only describe. The response strategy appears as a column header in the Phase 1b table — prose discussion of response in the synthesis block does not pass. Prerequisite: C-11. No interaction with C-04: adding columns to Phase 1b does not contaminate inertia-first sequencing. |
| C-27 | **Prose-free structural sufficiency** | format | The template is informationally complete without instructional prose: every semantic requirement is carried by a column header, gate annotation, section label, or citation-format token. Specifically: FINDING REGISTER preamble compressed to one line; Phase 0 and Phase 5 sub-table prose labels removed; gate annotations, phase tables, domain column headers, and Because block retained. All 24 prior criteria continue to pass in this compressed form. A template that requires prose wrappers to communicate any criterion's intent fails C-27 — structure is the instruction. No prerequisites (tests a property of the full template). |
```
