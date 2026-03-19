## discover-competitors-alt — R1 Scorecard

### Evaluation Method

Each variation is evaluated on whether its instructions **structurally enforce** each criterion, not merely mention it. PASS = instruction clearly prevents the failure mode. PARTIAL = instruction present but relies on model memory/goodwill without structural prevention.

PARTIAL = 0.5 for composite calculation.

---

### Per-Variation Criterion Scores

#### V-01 — Inertia Framing (step-structured)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | C0 first | PASS | "Before naming any market competitor…" + "Put C0 first. Always." Ordering is explicit at both the preamble and step level. |
| C-02 | Named competitors + threat levels | PASS | "Name: A proper name. No generic labels." + "Threat level: HIGH / MEDIUM / LOW — explicit, not implied." |
| C-03 | Focus woven not appended | PARTIAL | Opening says "weave…do not isolate in a trailing section" and each step has a focus sub-instruction, but no structural (column/block) enforcement. A model could still drift. |
| C-04 | Whitespace identified | PASS | "**GAP:** [specific uncontested dimension]" + explicit anti-pattern: "A generic statement… does not pass." |
| C-05 | Auto-detect | PASS | Opening fragment implies read-from-context; consistent with design intent and all other variations; no instruction to ask the user. |
| C-06 | Mechanism-level inertia | PASS | Three-option taxonomy (switching cost / habit lock-in / workaround satisfaction) + "This mechanism phrase becomes the inertia reference for the rest of the analysis. Every competitor and every finding will be evaluated against it." Strong. |
| C-07 | Web-verified inline citation | PASS | "Run a WebSearch on at least one named competitor. Add an inline citation… within that competitor's entry — not in a trailing footnote." |
| C-08 | AMEND with both columns | PASS | Example table with three populated rows, both "Input change" and "Output effect" columns. |
| C-09 | Cross-dimensional whitespace | PASS | "show that combining the competitive map with the focus lens produces a finding neither alone would surface." |
| C-10 | Grounded findings | PASS | "Reference at least one named competitor by its row label… Free-floating findings that do not require the competitive analysis to support them do not pass." |

**Essential: 4.5 / 5 | Recommended: 3 / 3 | Aspirational: 2 / 2**
**Composite: (4.5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 54 + 30 + 10 = 94**
**Grade: Strong**

---

#### V-02 — Output Format (table-first with conditional Focus column)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | C0 first | PASS | "Row 0 must be C0." Structural row ordering — syntactic constraint. |
| C-02 | Named competitors + threat levels | PASS | Table schema has explicit Threat column. "Minimum 3. Every row gets an explicit HIGH / MEDIUM / LOW threat level. No generic category labels." |
| C-03 | Focus woven not appended | PASS | Column presence/absence is structural. If focus is inactive the column is absent from the header entirely. A column cannot be appended — it is either in the schema or it is not. |
| C-04 | Whitespace identified | PASS | "**GAP:** [specific uncontested dimension]" + "A generic statement… does not pass." |
| C-05 | Auto-detect | PASS | "Read the repo context… Do not ask the user for the topic, competitors, or market category." |
| C-06 | Mechanism-level inertia | PARTIAL | "Why cell for C0 must name a specific stickiness mechanism." Criterion met for C0 row, but the Inertia delta column in other rows says "reinforce, challenge, or contextualize" without requiring the mechanism to be named by reference. The link back to the named mechanism is instructional, not structural. |
| C-07 | Web-verified inline citation | PASS | "Inline citation in that row's Why cell (URL or publication name). Not in a footnote below the table." Cell-level specification. |
| C-08 | AMEND with both columns | PASS | "Minimum 2 rows. Each row must name both the input change and the output effect." Template with explicit placeholders. |
| C-09 | Cross-dimensional whitespace | PASS | "Demonstrate that the gap requires both the competitive map and the focus lens to surface — it is not visible from either alone." |
| C-10 | Grounded findings | PASS | "Each must reference at least one named row label from the competitive map. No free-floating findings." |

**Essential: 5 / 5 | Recommended: 2.5 / 3 | Aspirational: 2 / 2**
**Composite: (5/5 × 60) + (2.5/3 × 30) + (2/2 × 10) = 60 + 25 + 10 = 95**
**Grade: Exceptional**

---

#### V-03 — Phrasing Register (conversational imperative)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | C0 first | PASS | "Put C0 first. Always." Direct imperative. |
| C-02 | Named competitors + threat levels | PASS | "actual products or tools, not category labels" + "Say what their threat level is (HIGH / MEDIUM / LOW) — be explicit, not implied." |
| C-03 | Focus woven not appended | PARTIAL | "that dimension gets woven into the competitor rows and the gap finding — not added as a section at the end." Clear instruction but no structural enforcement. Conversational register increases drift risk. |
| C-04 | Whitespace identified | PASS | "Label it clearly. Don't just say 'there's room to innovate' — say what the specific uncontested dimension is." |
| C-05 | Auto-detect | PASS | "Start by reading the repo to figure out what topic you're analyzing… Don't ask the user what the topic is." |
| C-06 | Mechanism-level inertia | PARTIAL | "name one concrete mechanism — what would users lose if they switched, what habit would be interrupted, or what workaround already solves most of the problem. This mechanism is the anchor the rest of the analysis refers back to." Good instruction but the mechanism has no named reference handle (no INERTIA-REF label), so re-referencing it in later findings relies on model memory. |
| C-07 | Web-verified inline citation | PASS | "Look up at least one competitor with WebSearch. Put the citation right next to that competitor — not in a footnote at the bottom." |
| C-08 | AMEND with both columns | PASS | "'You can adjust the focus dimension' is not enough — say what changes when they do." Anti-pattern explicitly named. Strong instruction. |
| C-09 | Cross-dimensional whitespace | PASS | "the gap should only be visible when you combine the competitive map with the focus lens. A gap you could spot without the focus doesn't count." |
| C-10 | Grounded findings | PASS | "Don't write general observations about the domain that could have been written without doing the competitive analysis." Matches rubric failure condition. |

**Essential: 4.5 / 5 | Recommended: 2.5 / 3 | Aspirational: 2 / 2**
**Composite: (4.5/5 × 60) + (2.5/3 × 30) + (2/2 × 10) = 54 + 25 + 10 = 89**
**Grade: Strong**

---

#### V-04 — Inertia Framing + Output Format (combination)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | C0 first | PASS | Phase 1 is an entire named block (`C0: / Threat: / Stickiness mechanism:`) that executes before any table row is written. Structurally impossible to place a competitor before C0. |
| C-02 | Named competitors + threat levels | PASS | Table schema enforces Threat column. "Minimum 3 external competitor rows. Every row: explicit HIGH / MEDIUM / LOW threat." |
| C-03 | Focus woven not appended | PASS | Column present/absent in table schema. Phase 1 block includes `Focus (C0):` entry when active. Both the table structure and the pre-table block enforce weaving at two levels. |
| C-04 | Whitespace identified | PASS | "**GAP:** [specific uncontested dimension]" with explicit anti-pattern and requirement to name C0 and all competitors as non-owners. |
| C-05 | Auto-detect | PASS | "Read repo context (README, CLAUDE.md, package.json) to identify the topic. Do not prompt the user. Resolve `focus:` state before building any table." |
| C-06 | Mechanism-level inertia | PASS | Phase 1 block has `Stickiness mechanism: [switching cost | habit lock-in | workaround satisfaction] — [specific description tied to what C0 does]`. This produces `INERTIA-REF`, which appears in every table column header as "Why (vs INERTIA-REF)". The mechanism name is propagated structurally through the column label — the model must name it in each row. |
| C-07 | Web-verified inline citation | PASS | Dedicated Source column: "for at least one external row, inline WebSearch citation (URL or publication name) — in the cell, not a footnote." Most structural citation enforcement of any variation. |
| C-08 | AMEND with both columns | PASS | Enhanced table with three columns: "Input change," "What changes in output," and "INERTIA-REF stable?" Three populated example rows. Exceeds minimum requirement. |
| C-09 | Cross-dimensional whitespace | PASS | "gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Show the intersection — state what the focus lens adds that the competitive map alone would not surface." |
| C-10 | Grounded findings | PASS | Findings format is a template: `[Finding statement referencing named competitor or C0] — [attribute being claimed] — [how this relates to INERTIA-REF]`. Competitor reference and inertia reference are both structurally required by the format. |

**Essential: 5 / 5 | Recommended: 3 / 3 | Aspirational: 2 / 2**
**Composite: (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 60 + 30 + 10 = 100**
**Grade: Exceptional**

---

#### V-05 — Lifecycle Emphasis + Inertia Framing (maximum combination)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | C0 first | PASS | ROOT phase executes before Phase 1 (topic/scope), which executes before Phase 2 (competitors). C0 is the ROOT output. Most extreme ordering enforcement of any variation. |
| C-02 | Named competitors + threat levels | PASS | Table schema + "Rows 1–N: minimum 3 named external competitors. No generic category labels. Every row: explicit HIGH / MEDIUM / LOW threat." |
| C-03 | Focus woven not appended | PASS | Focus state declared at pre-execution level ("focus is ACTIVE / INACTIVE"). Column in table schema. Both focus column and `INERTIA-REF Focus:` in ROOT block enforce weaving structurally. |
| C-04 | Whitespace identified | PASS | "**GAP:** [specific dimension not owned by C0 or any Phase 2 competitor]" with branch logic for active/inactive focus. |
| C-05 | Auto-detect | PASS | "Auto-detect: Read repo context… Do not ask the user for any of these. Proceed immediately." Strongest phrasing of any variation. |
| C-06 | Mechanism-level inertia | PASS | ROOT block outputs `INERTIA-REF: [C0 name] — [mechanism type]: [specific description]`. Named reference propagated to `vs INERTIA-REF` column in Phase 2. |
| C-07 | Web-verified inline citation | PASS | "Citation: run WebSearch on at least one external row. Inline citation in that row's Why cell." |
| C-08 | AMEND with both columns | PASS | Three-row example with named input changes and output effects: focus dimension, depth, narrowed competitor set. All rows specify output scope (which phases are affected). |
| C-09 | Cross-dimensional whitespace | PASS | "gap must be uncontested across BOTH competitive and focus dimensions simultaneously. Show intersection — the finding must require both the Phase 2 map and the focus column to produce. A gap visible from the competitive map alone does not qualify." |
| C-10 | Grounded findings | PASS | "Name at least one labeled competitor from Phase 2 (or C0 from ROOT) as its anchor. State a specific attribute… Findings that could be written without having run Phase 2 fail the grounding test." |

**Essential: 5 / 5 | Recommended: 3 / 3 | Aspirational: 2 / 2**
**Composite: (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 60 + 30 + 10 = 100**
**Grade: Exceptional**

---

### Composite Scores Summary

| Variation | Essential | Recommended | Aspirational | Composite | Grade |
|-----------|-----------|-------------|--------------|-----------|-------|
| V-04 | 5/5 | 3/3 | 2/2 | **100** | Exceptional |
| V-05 | 5/5 | 3/3 | 2/2 | **100** | Exceptional |
| V-02 | 5/5 | 2.5/3 | 2/2 | **95** | Exceptional |
| V-01 | 4.5/5 | 3/3 | 2/2 | **94** | Strong |
| V-03 | 4.5/5 | 2.5/3 | 2/2 | **89** | Strong |

All essential pass: **V-04, V-05** (both score 5/5 essential)

---

### Rank Order

1. **V-04 / V-05 (100)** — V-04 wins the tiebreak on C-10: the findings format template (`[competitor] — [attribute] — [vs INERTIA-REF]`) is the most structural enforcement of finding grounding. V-05 wins on C-01 enforcement (ROOT before Phase 1 before Phase 2). Functionally equivalent scores.
2. **V-02 (95)** — Full essential coverage via table structure. Docked on C-06: the Inertia delta column doesn't require naming the mechanism; it just asks for "reinforce / challenge / contextualize" without anchoring to the named mechanism.
3. **V-01 (94)** — Best narrative instruction quality. Loses one point (C-03 PARTIAL) because focus weaving relies on per-step reminders rather than structural enforcement.
4. **V-03 (89)** — All criteria addressed; conversational register is effective at preventing gate-narration. Loses points on C-03 and C-06 for lack of structural anchors.

---

### Excellence Signals (from V-04/V-05)

Three patterns distinguish the top-scoring variations from the rest:

**1. INERTIA-REF as a named, propagated anchor**
The mechanism isn't just described in C0 — it's given a label (`INERTIA-REF`) that appears in table column headers (`Why (vs INERTIA-REF)`). Every row must explicitly relate to it. This converts C-06 and C-10 from instructional requirements to structural ones: the model cannot write a competitor row without engaging the mechanism reference.

**2. C0 as a pre-table block, not just table row 0**
Phase 1 (V-04) and ROOT (V-05) establish C0 as a named output block before any table is constructed. This does two things: it forces the mechanism to be named before the table schema is resolved, and it makes C-01 a structural dependency rather than an ordering instruction. The C0 block cannot appear after a competitor because it's a precondition for building the table.

**3. Findings as a format template, not a rule**
V-04's findings format (`[statement referencing competitor] — [attribute] — [how this relates to INERTIA-REF]`) encodes the grounding requirement into the output template itself. A model following the template cannot produce a free-floating finding: the template syntax requires a competitor reference slot to be filled.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["INERTIA-REF as a named propagated anchor in table column headers — converts C-06 and C-10 from instructional to structural enforcement", "C0 established as a pre-table block (Phase 1 / ROOT) before table schema is resolved — makes C-01 a structural dependency rather than an ordering instruction", "Findings format template requiring inline competitor reference slot — prevents free-floating findings by making the grounding requirement syntactic"]}
```
