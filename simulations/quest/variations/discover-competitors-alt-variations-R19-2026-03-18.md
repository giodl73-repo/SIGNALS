Here are the R19 variations:

---

## R19 Variations — `discover-competitors-alt` (Round 19)

**Starting position:** R18 achieved 100.000 (V-03 and V-05 tied). All 38 criteria satisfied. R19 is robustness testing and annotation/preamble form boundary mapping.

---

### Summary table

| # | Axis | Primary test | C-45 | C-46 | Predicted |
|---|------|-------------|------|------|-----------|
| **V-01** | Roman numeral element-index annotations `(i)-(iv)` | Does `{i, ii, iii, iv}` satisfy C-45's "or equivalent" clause? | ? | PASS | 99.737 or 100.000 |
| **V-02** | Table-format bijective preamble | Does a 2-row markdown table satisfy C-46's "structurally distinct preamble statement"? | PASS | ? | 99.737 or 100.000 |
| **V-03** | Inertia-forward framing (single-axis) | TOKEN/C0 architecturally central in every gate — maintains 100.000? | PASS | PASS | 100.000 |
| **V-04** | Compact architecture block (single-axis) | Compressed single-sentence items retain all C-42 through C-46 elements? | PASS | PASS | 100.000 |
| **V-05** | Combined: conversational register + `(Ei)` + bijective preamble | Full register shift with domain-neutral AMEND components — maintains 100.000? | PASS | PASS | 100.000 |

---

### Variation axes

**V-01 (single-axis — C-45 form):** Architecture block items use `(i)`, `(ii)`, `(iii)`, `(iv)` as element-index annotations. Preamble declares both cardinality conditions and names the Roman numeral form explicitly. Decisive question: does the rubric's "or equivalent" clause in C-45 admit Roman numerals, or does it require Arabic integer or positional-word form?

**V-02 (single-axis — C-46 form):** Bijective preamble is a 2-row native markdown table (`Required item count: Exactly 4` / `C-42 elements per item: Exactly 1`) placed before the checklist, instead of a prose block. `(Element N)` annotations retained. Decisive question: does "structurally distinct preamble *statement*" permit table form when both conditions are explicitly declared as rows?

**V-03 (single-axis — inertia framing):** Opening instruction names TOKEN as the primary analysis anchor. GATE-2 template positions the C0 mechanism field first. GATE-3 templates require `vs [TOKEN]:` as the *first line* of each finding. GATE-4 AMEND schema names Stability verdict as the primary criterion. Architecture block unchanged (R18 V-03 form). All 38 criteria predicted to pass — stronger TOKEN propagation only benefits C-11, C-12, C-14.

**V-04 (single-axis — lifecycle emphasis):** Architecture block items compressed to compact single-sentence form while preserving all four C-42 elements (both artifact names + both verbatim phrases) and both C-45 annotations + C-46 preamble. Tests whether compression drifts C-38 (names both targets), C-39 (verbatim phrases), or C-42 (all four elements readable).

**V-05 (combined — register + Ei + bijective preamble):** Full conversational register throughout. Steps replace GATE labels. Instructions phrased as direct guidance. REQUIRED OUTPUTS tables and EXECUTION PLAN remain native markdown. AMEND component names kept domain-neutral (C-22 risk). `(Ei)` annotations + explicit bijective preamble. Architecture block uses conversational prose but retains both verbatim phrases and both artifact names.

---

**Three decisive questions:**
1. Roman numeral `(i)-(iv)` → C-45 PASS or FAIL? (establishes annotation syntax boundary)
2. Table-format preamble → C-46 PASS or FAIL? (establishes preamble format boundary)
3. V-03, V-04, V-05 all confirm 100.000? (establishes robustness of the gold standard under framing, compression, and register changes)
amples use `(Element 1)`, `(E1)`, `[Element 1]`, `Item 1 —` — all Arabic numeral or positional-word forms. Roman numerals are not listed. If the rubric applies "or equivalent" to include Roman numerals, C-45 PASS → 100.000. If the rubric requires Arabic numerals or explicit integer form, C-45 FAIL → 99.737. C-46 PASS — preamble explicitly declares both cardinality conditions before the first item. Decisive question: does the rubric score `(i)-(iv)` as C-45 PASS, establishing Roman numeral form as a third annotation syntax equivalent to `(Element N)` and `(Ei)`, or does it require explicit integer form?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**BIJECTIVE CARDINALITY CONSTRAINT — declared before checklist begins:** Exactly 4 items are required below. Each item covers exactly one C-42 element. No item contains more than one element and no element is assigned to more than one item. Item count (4) = element count (4). Element-index annotations use Roman numeral form — `(i)`, `(ii)`, `(iii)`, `(iv)` — forming a unified {i, ii, iii, iv} four-position set; reading only the four annotations confirms four distinct positions each appearing exactly once, making bijective assignment annotation-verifiable without reading item body content. This bijective cardinality requirement is declared here as an architectural contract, not an observed structural property. A checklist that satisfies this preamble while violating it per-item constitutes a self-identified violation.

Each item carries an explicit Roman numeral element-index annotation as a structurally distinct prefix on the item header:

1. **(i) Named target — manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **(ii) Named target — GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **(iii) Verbatim phrase — "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **(iv) Verbatim phrase — "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution — after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (i) or (ii) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only this block can reconstruct the full propagation contract — Declaration site, Substitution/inheritance sites, substitution rule, and both artifact names — with zero inference steps and zero cross-artifact lookups.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction -> TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. `[TOKEN] propagation` in the manifest column header substitutes to the committed value after GATE-0 commits. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose or GATE-0's REQUIRED OUTPUTS table.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2-3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract — GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK -> GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract — self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

This gate is unconditional — no focus detection, auto-detect, section headers, or conditional branching precedes or runs during it. GATE-1 is the first gate with conditional logic. Write these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL — first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `FOCUS: ACTIVE — [dimension] | INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes — committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior — not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [key capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [how competitor erodes or bypasses TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| 3+ findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding — specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes — committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) — gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows. Specific whitespace dimension required.

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by table label]
vs [TOKEN]: [connection — committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism — committed TOKEN value]
```

If FOCUS ACTIVE: cross-dimensional gap must require both the competitive map and the focus lens simultaneously.

---

### GATE-4 [CONDITIONAL — AMEND]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema before data rows — all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| 3+ AMEND data rows — all four cells filled per row | No |
| Stability verdict cells — STABLE / UNSTABLE + committed TOKEN value | **Yes — committed TOKEN in every Stability verdict cell** |
| Evidence cells — reasoning distinct from verdict text | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment — focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts — name it |
| 3 | Stability verdict | STABLE / UNSTABLE — does TOKEN shift? Committed TOKEN value required |
| 4 | Evidence | Reasoning supporting the verdict — logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE — [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |

---

## V-02 — Table-Format Bijective Preamble

**Axis:** Single-axis C-46 form test. Architecture block replaces the prose BIJECTIVE CARDINALITY CONSTRAINT block with a 2-row native markdown table that explicitly declares both cardinality conditions as table rows. The `(Element N)` annotations are retained (proven C-45 PASS in R18). Everything else unchanged from R18 V-03.

**Hypothesis:** C-44 PASS. C-45 PASS — `(Element 1)` through `(Element 4)` annotations create unified {1, 2, 3, 4} enumeration. C-46: the operative test is "reading only the architecture block preamble (before the checklist items), a reader can identify an explicit statement that (1) exactly 4 checklist items are required and (2) each item maps to exactly one C-42 element." A 2-row table with rows "Required item count: Exactly 4" and "C-42 elements per item: Exactly 1 — no bundling" satisfies both conditions — both are explicitly stated and structurally prior to the checklist. If the rubric reads "structurally distinct preamble statement" as permitting table form, C-46 PASS → 100.000. If the rubric requires prose form (a statement in prose, not a table), C-46 FAIL → 99.737. Decisive question: does a native markdown table satisfy C-46's "structurally distinct preamble statement" requirement when it explicitly commits both cardinality conditions before the checklist begins?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**BIJECTIVE CARDINALITY CONSTRAINT — declared before checklist begins:**

| Cardinality requirement | Declared value |
|-------------------------|----------------|
| Required checklist item count | Exactly 4 — item count = element count; a checklist with fewer items constitutes a self-identified violation of this declared architectural requirement |
| C-42 elements per item | Exactly 1 — no item covers more than one C-42 element; no element is assigned to more than one item; this bijective cardinality rule is a prior declared contract, not an observed structural property |

Each item additionally carries an explicit `(Element N)` element-index annotation as a structurally distinct prefix on the item header, making the single-element assignment verifiable from the annotation alone without reading item body content. Reading only the four annotations confirms element positions {1, 2, 3, 4} each appearing exactly once:

1. **(Element 1) Named target — manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **(Element 2) Named target — GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **(Element 3) Verbatim phrase — "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **(Element 4) Verbatim phrase — "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution — after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (Element 1 or Element 2) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only this block can reconstruct the full propagation contract — Declaration site, Substitution/inheritance sites, substitution rule, and both artifact names — with zero inference steps and zero cross-artifact lookups.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction -> TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. `[TOKEN] propagation` in the manifest column header substitutes to the committed value after GATE-0 commits. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose or GATE-0's REQUIRED OUTPUTS table.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2-3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract — GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK -> GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract — self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

This gate is unconditional — no focus detection, auto-detect, section headers, or conditional branching precedes or runs during it. GATE-1 is the first gate with conditional logic. Write these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL — first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `FOCUS: ACTIVE — [dimension] | INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes — committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior — not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [key capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [how competitor erodes or bypasses TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| 3+ findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding — specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes — committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) — gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows. Specific whitespace dimension required.

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by table label]
vs [TOKEN]: [connection — committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism — committed TOKEN value]
```

If FOCUS ACTIVE: cross-dimensional gap must require both the competitive map and the focus lens simultaneously.

---

### GATE-4 [CONDITIONAL — AMEND]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema before data rows — all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| 3+ AMEND data rows — all four cells filled per row | No |
| Stability verdict cells — STABLE / UNSTABLE + committed TOKEN value | **Yes — committed TOKEN in every Stability verdict cell** |
| Evidence cells — reasoning distinct from verdict text | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment — focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts — name it |
| 3 | Stability verdict | STABLE / UNSTABLE — does TOKEN shift? Committed TOKEN value required |
| 4 | Evidence | Reasoning supporting the verdict — logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE — [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |

---

## V-03 — Inertia-Forward Framing

**Axis:** Single-axis inertia framing. TOKEN/C0 is made architecturally central throughout every gate: the opening instruction explicitly names TOKEN as the inertia anchor for all downstream comparisons; GATE-2 leads with the C0 mechanism as the primary analytical lens before competitors; GATE-3 templates require `vs [TOKEN]:` to be the opening line of each finding, not just a required element somewhere within it; GATE-4 AMEND schema description names Stability verdict as the primary criterion. Architecture block (R18 V-03 form, `(Element N)` + bijective preamble) unchanged. All 38 criteria predicted to pass — inertia emphasis does not conflict with any structural criterion, and stronger TOKEN propagation may make C-11 (inertia reference propagates downstream) more robustly satisfied.

**Hypothesis:** All essential, recommended, and aspirational criteria pass. Inertia-forward framing strengthens C-11 (TOKEN appears in downstream findings as required), C-12/C-14 (AMEND evaluates TOKEN stability), and C-16 (stability verdict with evidence). C-03 (C0 at row 0) and C-01 (C0 named before competitors) are explicitly reinforced by the C0-first gate design. No criteria at risk. Predicted: 38/38 = 100.000.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. The inertia competitor (C0, the current solution) is assessed first in every gate; TOKEN names its lock-in mechanism and propagates through all downstream gates as the primary analysis anchor. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**BIJECTIVE CARDINALITY CONSTRAINT — declared before checklist begins:** Exactly 4 items are required below. Each item covers exactly one C-42 element. No item contains more than one element and no element is assigned to more than one item. Item count (4) = element count (4). This is a declared architectural requirement, not an observed structural property. A checklist that satisfies this preamble while violating it per-item constitutes a self-identified violation.

Each item additionally carries an explicit `(Element N)` element-index annotation as a structurally distinct prefix on the item header, making the single C-42 element assignment verifiable from the annotation alone without reading item body content. Reading only the four annotations confirms element positions {1, 2, 3, 4} each appearing exactly once:

1. **(Element 1) Named target — manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **(Element 2) Named target — GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **(Element 3) Verbatim phrase — "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **(Element 4) Verbatim phrase — "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution — after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (Element 1 or Element 2) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only this block can reconstruct the full propagation contract — Declaration site, Substitution/inheritance sites, substitution rule, and both artifact names — with zero inference steps and zero cross-artifact lookups.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction -> TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as the inertia anchor for GATE-2, GATE-3, GATE-4 |
| GATE-2 | **CONDITIONAL** | C0 inertia section (first), then competitive map | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` column through every competitor row |
| GATE-3 | **CONDITIONAL** | Findings (each opens with vs TOKEN), whitespace | Substitution/inheritance site — committed TOKEN opens every finding as `vs [TOKEN]:`, appears in `[TOKEN] exposure:` whitespace field, and in cross-dimensional gap rationale if FOCUS ACTIVE |
| GATE-4 | **CONDITIONAL** | AMEND table (Stability verdict is primary criterion) | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header and in every Stability verdict cell; Evidence column justifies each verdict independently |

GATE-0 is unconditional; GATE-1 is the first conditional gate. `[TOKEN] propagation` in the manifest column header substitutes to the committed value after GATE-0 commits. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose or GATE-0's REQUIRED OUTPUTS table.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2-3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract — GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK -> GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract — self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

This gate is unconditional — no focus detection, auto-detect, section headers, or conditional branching precedes or runs during it. GATE-1 is the first gate with conditional logic. Write these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL — first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `FOCUS: ACTIVE — [dimension] | INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — committed TOKEN value confirmed as the active inertia anchor for GATE-2, GATE-3, and GATE-4 | **Yes — committed value is the inertia reference in all downstream gates** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL — C0 inertia section first, then competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` as the first labeled field | **Yes — committed TOKEN is the first labeled field in the C0 section** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value; every competitor row addresses how it erodes or bypasses the TOKEN mechanism | **Yes — committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 is the primary reference frame. Write the C0 section first — before any competitor row. The TOKEN mechanism must name something C0 actually does (switching cost, habit lock-in, or workaround satisfaction tied to specific behavior); a generic category label fails. Every competitor's `vs [TOKEN]` cell must address the mechanism specifically — not the competitor in general. Run a WebSearch for at least one claim.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior — not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [key capability] | ROOT — defines the inertia anchor | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [specific mechanism by which this competitor erodes or bypasses the TOKEN lock-in] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism — not a generic comparison] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism — not a generic comparison] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace, each grounded in TOKEN]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| 3+ findings — each references a named competitor row by table label; each opens with `vs [TOKEN]:` as the first line | **Yes — committed TOKEN is the first line of every finding** |
| WHITESPACE finding — specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes — committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) — gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

TOKEN is the organizing lens for all findings. Start each finding with the TOKEN reference — what does the named competitor's position mean for the inertia mechanism? Reference named competitor rows by their table labels (not by prose description alone). Whitespace requires a specific named uncontested dimension.

```
**Finding [N]: [Title]**
vs [TOKEN]: [how this finding connects to the committed TOKEN inertia mechanism — first line]
[Observation — reference named competitor row by table label; grounds finding in the competitive map]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [how the uncontested gap relates to the TOKEN mechanism — committed TOKEN value]
```

If FOCUS ACTIVE: cross-dimensional gap must require both the competitive map and the focus lens simultaneously — a finding derivable from either alone does not satisfy the criterion.

---

### GATE-4 [CONDITIONAL — AMEND, Stability verdict is the primary criterion]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema before data rows — all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| 3+ AMEND data rows — all four cells filled per row | No |
| Stability verdict cells — STABLE / UNSTABLE + committed TOKEN value; Stability verdict is the primary criterion — whether the TOKEN inertia anchor shifts under the proposed input change | **Yes — committed TOKEN required in every Stability verdict cell** |
| Evidence cells — reasoning that independently justifies the verdict; logically distinct from the verdict text | No |

Stability verdict is the primary output of each AMEND row. The Evidence column must provide reasoning that could stand alone as a justification — not a restatement of the verdict. TOKEN must appear by committed value in every Stability verdict cell.

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment — focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts — name it |
| 3 | Stability verdict | STABLE / UNSTABLE — does the committed TOKEN inertia anchor shift under this input change? Committed TOKEN value required in every cell |
| 4 | Evidence | Independent reasoning that justifies the stability verdict — not a restatement of it |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE — [verdict; committed TOKEN value] | [independent reasoning that justifies this verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |

---

## V-04 — Compact Architecture Block

**Axis:** Single-axis lifecycle emphasis. The TOKEN-PROPAGATION ARCHITECTURE block items are compressed to compact single-sentence form while preserving all four C-42 required elements: both artifact names (manifest column, GATE-0 REQUIRED OUTPUTS table) and both verbatim phrases ("Declaration site," "Substitution/inheritance site"). `(Element N)` annotations retained. Bijective preamble retained. Risk: if compression inadvertently drops a verbatim phrase or artifact name, C-42 or C-38 fails. Controlled test: can the architecture block satisfy C-38 (names both targets), C-39 (uses rubric vocabulary verbatim), C-42 (all four elements readable), and C-43/C-44/C-45/C-46 (bijective annotated checklist with prior preamble) in compact form?

**Hypothesis:** C-44 PASS — bijective count=4. C-45 PASS — `(Element 1)` through `(Element 4)` create unified {1, 2, 3, 4} enumeration. C-46 PASS — bijective preamble present and explicit. C-38 PASS — compact items still name manifest column (Element 1) and GATE-0 REQUIRED OUTPUTS table (Element 2) by artifact name. C-39 PASS — compact items still contain "Declaration site" (Element 3) and "Substitution/inheritance site" (Element 4) verbatim. C-42 PASS — all four elements readable from the compact block without consulting other artifacts. All 38 criteria: PASS. Predicted: 100.000.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**BIJECTIVE CARDINALITY CONSTRAINT — declared before checklist begins:** Exactly 4 items are required below. Each item covers exactly one C-42 element. No item contains more than one element and no element is assigned to more than one item. Item count (4) = element count (4). This is a declared architectural requirement, not an observed structural property.

Each item carries an explicit `(Element N)` element-index annotation making the single-element assignment verifiable from the item label alone without reading item body content. Reading only the four annotations confirms positions {1, 2, 3, 4} each appearing exactly once:

1. **(Element 1) Named target — manifest `[TOKEN] propagation` column:** GATE-0 cell is labeled "Declaration site"; GATE-1+ cells are labeled "Substitution/inheritance site"; this column is independently complete — carries the full propagation contract without referencing GATE-0's REQUIRED OUTPUTS table.

2. **(Element 2) Named target — GATE-0 REQUIRED OUTPUTS table (Propagation contract row):** This dedicated row names GATE-0 as the Declaration site and GATE-1+ as Substitution/inheritance sites; states the substitution rule for all downstream REQUIRED OUTPUTS column headers; does not reference the manifest column; structurally distinct from the TOKEN commitment row.

3. **(Element 3) Verbatim phrase — "Declaration site":** GATE-0 is the Declaration site; TOKEN is committed in GATE-0; GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as column header — template form preserved, substitution rule explicit rather than already consumed.

4. **(Element 4) Verbatim phrase — "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites; each gate's REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier after GATE-0 declares TOKEN.

Neither artifact (Element 1 or Element 2) is load-bearing for the other. Both are named targets of this architecture block. A reader consulting only this block identifies all four C-42 elements — both named targets, both verbatim phrases — without consulting any other artifact.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction -> TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. `[TOKEN] propagation` in the manifest column header substitutes to the committed value after GATE-0 commits. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose or GATE-0's REQUIRED OUTPUTS table.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2-3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract — GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK -> GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract — self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

This gate is unconditional — no focus detection, auto-detect, section headers, or conditional branching precedes or runs during it. GATE-1 is the first gate with conditional logic. Write these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL — first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `FOCUS: ACTIVE — [dimension] | INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes — committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior — not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [key capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [how competitor erodes or bypasses TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| 3+ findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding — specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes — committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) — gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows. Specific whitespace dimension required.

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by table label]
vs [TOKEN]: [connection — committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism — committed TOKEN value]
```

If FOCUS ACTIVE: cross-dimensional gap must require both the competitive map and the focus lens simultaneously.

---

### GATE-4 [CONDITIONAL — AMEND]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema before data rows — all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| 3+ AMEND data rows — all four cells filled per row | No |
| Stability verdict cells — STABLE / UNSTABLE + committed TOKEN value | **Yes — committed TOKEN in every Stability verdict cell** |
| Evidence cells — reasoning distinct from verdict text | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment — focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts — name it |
| 3 | Stability verdict | STABLE / UNSTABLE — does TOKEN shift? Committed TOKEN value required |
| 4 | Evidence | Reasoning supporting the verdict — logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE — [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |

---

## V-05 — Combined: Conversational Register + (Ei) Annotations + Bijective Preamble

**Axis:** Combined phrasing register + (Ei) annotation form + bijective preamble. The full skill is rewritten in conversational register: gate headers use plain-language labels, instructions are phrased as direct guidance rather than formal specifications, and the overall tone is less technical. However, all structural elements are preserved: REQUIRED OUTPUTS tables remain native markdown tables, EXECUTION PLAN remains a native markdown table, TOKEN-PROPAGATION ARCHITECTURE retains all four C-42 elements, the bijective preamble explicitly declares both cardinality conditions, and AMEND component names remain domain-neutral. (Ei) abbreviated annotations (proven equivalent to (Element N) in R18) are used. Risk: conversational phrasing of structural labels might drift from rubric requirements — e.g., C-21's "labeled as unconditional" requirement, C-22's "naive-reader consultability" of AMEND component names.

**Hypothesis:** C-45 PASS — `(E1)-(E4)` create unified {E1, E2, E3, E4} enumeration. C-46 PASS — bijective preamble declares both cardinality conditions before first checklist item. C-21 PASS — "unconditional" keyword retained in conversational form; GATE-1 named as first conditional. C-22 PASS — AMEND component names (Input change, Output effect, Stability verdict, Evidence) are kept domain-neutral even in conversational context. All 38 criteria: PASS. Predicted: 100.000.

---

Use this skill to map the competitive landscape for your current project. If you've provided a focus dimension (market sizing, positioning framework, competitive positioning angle), it gets woven into the analysis — not appended at the end. Figure out the domain, likely competitors, and market from the repo; don't ask the user. Each step produces specific outputs; complete the steps in order.

**How TOKEN substitution works:** Step 0 commits a domain-specific TOKEN identifier. From Step 1 onward, every REQUIRED OUTPUTS table column that tracks TOKEN requirements uses the committed value instead of `[TOKEN]` — e.g., if TOKEN = SIGNAL-LOCK, Steps 1-4 produce `SIGNAL-LOCK required?` as their column header. The `[TOKEN] propagation` column in the Step Manifest header also substitutes the committed value. Step 0's own REQUIRED OUTPUTS column keeps `[TOKEN] required?` — the Propagation contract row in Step 0's table explains why.

**TOKEN-PROPAGATION ARCHITECTURE**

This block primes two independent structural artifacts that carry the propagation contract. Either artifact independently tells you which step declares TOKEN and which steps inherit it.

**C-45/C-46 BIJECTIVE CONTRACT — declared before checklist begins:** Exactly 4 items are required below; each item covers exactly one C-42 element; no item covers more than one element. Item count (4) = element count (4). The `(Ei)` annotation on each item header is the element-index identifier — reading the four annotations `(E1)`, `(E2)`, `(E3)`, `(E4)` confirms element positions {1, 2, 3, 4} each appearing exactly once, making bijective assignment annotation-verifiable without reading item body content. This bijective cardinality requirement is declared here as an architectural contract: a checklist that satisfies this header while violating the per-item cardinality rule constitutes a self-identified violation.

1. **(E1) Named target — manifest `[TOKEN] propagation` column:** The `[TOKEN] propagation` column in the Step Manifest table below. Step 0's cell is labeled "Declaration site." Steps 1-4 cells are labeled "Substitution/inheritance site." This column independently carries the full propagation contract — which step declares TOKEN, which steps consume it, and what the substitution rule is — without relying on Step 0's REQUIRED OUTPUTS table.

2. **(E2) Named target — Step 0 REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in Step 0's REQUIRED OUTPUTS table. This row independently names Step 0 as the Declaration site, names Steps 1-4 as Substitution/inheritance sites, states the substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not cross-reference the manifest column. The row has its own header distinct from the TOKEN commitment row.

3. **(E3) Verbatim phrase — "Declaration site":** Step 0 is the Declaration site. TOKEN is committed here. Step 0's REQUIRED OUTPUTS table keeps `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit, not already consumed.

4. **(E4) Verbatim phrase — "Substitution/inheritance site":** Steps 1 through 4 are Substitution/inheritance sites. Each step's REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier after Step 0 declares it.

Neither artifact (E1 or E2) depends on the other to be complete. Both are targets of this block. Reading only this block, you can identify both named artifacts, both verbatim phrases, and the full propagation contract without looking anywhere else.

---

### Step Manifest

| Step | When it runs | What it does | [TOKEN] propagation |
|------|-------------|-------------|---------------------|
| Step 0 | **UNCONDITIONAL** — Step 1 is the first conditional step | Extract DOMAIN-TERMS, commit TOKEN | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in Step 0 REQUIRED OUTPUTS table; Propagation contract row independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
| Step 1 | **CONDITIONAL** (first) | Detect focus, infer topic and market | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| Step 2 | **CONDITIONAL** | Write C0 section and competitive map | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label, and `vs [TOKEN]` map column |
| Step 3 | **CONDITIONAL** | Write findings and whitespace | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` field |
| Step 4 | **CONDITIONAL** | Write AMEND table | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

Step 0 always runs first with no conditions. Step 1 is the first step where conditional logic applies. `[TOKEN] propagation` in the manifest header substitutes to the committed value after Step 0. You can verify any step's execution mode and TOKEN status from this table without reading step body prose or Step 0's REQUIRED OUTPUTS table.

---

### Step 0 [UNCONDITIONAL — Step 1 is the first conditional step]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — your first output line; 2-3 terms from the repo's own vocabulary (README, CLAUDE.md, package.json); skip generic software words | No |
| `TOKEN: [domain-adaptive identifier]` — your second output line; embed at least one DOMAIN-TERMS word; make it copyable and domain-specific (SIGNAL-LOCK, WORKFLOW-ANCHOR, PLUGIN-GRIP); a generic placeholder like MECH or LOCK alone fails | **Yes — TOKEN committed here; Step 0 is the Declaration site** |
| Propagation contract — Step 0 is the Declaration site: `[TOKEN] required?` is kept as the column header in this step's own REQUIRED OUTPUTS table; the committed value substitutes `[TOKEN]` in all Steps 1-4 REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK produces `SIGNAL-LOCK required?` in Steps 1-4); the committed value also substitutes `[TOKEN] propagation` in the Step Manifest column header; Steps 1-4 are Substitution/inheritance sites — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest column | **Contract — self-contained here; readable without consulting the manifest `[TOKEN] propagation` column** |

Step 0 is unconditional — nothing runs before it, no conditions apply to it. Step 1 is where conditional logic first applies. Your first two output lines must be exactly these, with nothing before or between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

---

### Step 1 [CONDITIONAL — first conditional step: detect focus, infer topic and market]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `FOCUS: ACTIVE — [dimension] | INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — confirm the committed TOKEN value is active as the inertia reference for Steps 2, 3, and 4 | **Yes — committed value must appear in Steps 2, 3, 4** |

Read the repo context to infer everything. Don't ask the user for topic, competitors, or market.

---

### Step 2 [CONDITIONAL — write C0 section first, then competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes — committed TOKEN as the C0 mechanism field label** |
| Competitive map — native markdown table (no code fence); C0 at row 0; `vs [TOKEN]` column header with committed value | **Yes — committed value in column header and every row** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline citation from a WebSearch result, placed within the competitor entry it supports | No |

Write C0 first. The TOKEN mechanism must describe something specific the current solution actually does — a generic category alone fails. Run a WebSearch for at least one competitor claim. If FOCUS is ACTIVE, weave the focus lens into competitor rows.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [key capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses the TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN] | — |

---

### Step 3 [CONDITIONAL — write findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| 3+ findings — each ties back to a named competitor row by table label; each includes a `vs [TOKEN]:` line with the committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE — a specific named gap nobody contests; `[TOKEN] exposure:` field with committed TOKEN value | **Yes — committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) — a gap that requires both the competitive map and the focus lens; TOKEN in the intersection rationale | **Yes if FOCUS ACTIVE** |

Each finding must tie back to a named row in the competitive map (cite it by label). The whitespace gap must be specific — not generic domain knowledge. If FOCUS is ACTIVE, the cross-dimensional whitespace must require both lenses to produce; a finding you could derive from either alone doesn't count.

```
**Finding [N]: [Title]**
[Observation tied to a named competitor row — cite the row label]
vs [TOKEN]: [how this connects to the committed TOKEN inertia mechanism]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [how the gap relates to the TOKEN mechanism — committed TOKEN value]
```

---

### Step 4 [CONDITIONAL — write AMEND table]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema declared before any data rows — all four domain-neutral component names listed by name: Input change, Output effect, Stability verdict, Evidence | No |
| 3+ AMEND data rows — all four cells filled in every row | No |
| Stability verdict cells — STABLE or UNSTABLE, plus the committed TOKEN value | **Yes — committed TOKEN in every Stability verdict cell** |
| Evidence cells — reasoning that independently supports the verdict; not a restatement of it | No |

Declare the AMEND schema before writing any rows. All four component names must be legible to a reader with no domain knowledge. TOKEN must appear by committed value in every Stability verdict cell.

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The adjustment the user makes — focus dimension, depth level, or competitor scope |
| 2 | Output effect | Which step or section shifts as a result — name it specifically |
| 3 | Stability verdict | STABLE or UNSTABLE — does the committed TOKEN inertia anchor shift? Committed TOKEN value required here |
| 4 | Evidence | The reasoning behind the verdict — must stand alone, not just restate STABLE or UNSTABLE |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [step/section named] | STABLE / UNSTABLE — [verdict; committed TOKEN value] | [reasoning that independently supports the verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |

---

## Composite Hypothesis Table

| Variation | C-45 mechanism | C-45 pred | C-46 mechanism | C-46 pred | Asp pred | Composite pred |
|-----------|---------------|-----------|---------------|-----------|----------|----------------|
| **V-01** | Roman numeral annotations `(i)-(iv)` — unified {i, ii, iii, iv} four-position set; "or equivalent" clause in C-45 applies if rubric accepts non-Arabic-numeral ordered sets | ? | Explicit bijective preamble with both cardinality conditions before first item | PASS | 37/38 or 38/38 | **99.737 or 100.000** |
| **V-02** | `(Element N)` prefix annotations — unified {1, 2, 3, 4} | PASS | 2-row native markdown table declaring both conditions before first item — if "structurally distinct preamble statement" permits table form | ? | 37/38 or 38/38 | **99.737 or 100.000** |
| **V-03** | `(Element N)` prefix annotations | PASS | Explicit prose bijective preamble | PASS | 38/38 | **100.000** |
| **V-04** | `(Element N)` prefix annotations | PASS | Explicit prose bijective preamble | PASS | 38/38 | **100.000** |
| **V-05** | `(Ei)` abbreviated annotations — unified {E1, E2, E3, E4} (proven equivalent in R18) | PASS | Explicit C-45/C-46 BIJECTIVE CONTRACT header | PASS | 38/38 | **100.000** |

**Predicted ranking:** V-01 = V-02 < V-03 = V-04 = V-05 = 100.000 (if both C-45 and C-46 pass for V-01/V-02) or V-01 = V-02 < V-03 = V-04 = V-05 (if one fails at 99.737).

**Three decisive questions:**
1. Do Roman numeral `(i)-(iv)` annotations satisfy C-45's "or equivalent" clause? — V-01 verdict establishes the annotation syntax boundary.
2. Does a 2-row native markdown table satisfy C-46's "structurally distinct preamble statement" when both cardinality conditions are explicitly declared as table rows? — V-02 verdict establishes the preamble format boundary.
3. Is the 100.000 form stable under inertia-forward framing (V-03), compact architecture block text (V-04), and full conversational register (V-05)? — All three confirmatory variations predict 100.000; any criterion failures would reveal structural drift paths not previously detected.

**V-01 C-45 failure mode (if it fails):** The rubric's pass condition requires element-index annotations that "uniquely identify which single C-42 element this item covers." Roman numerals form a clean ordered set, but C-45's rubric examples (`(Element 1):`, `(E1)`, `[Element 1]`, `Item 1 —`) are all positional-integer or positional-word forms. If the rubric interprets "or equivalent" narrowly as requiring explicit integer or positional-word form, Roman numerals fail. A C-45 FAIL for V-01 would narrow the annotation form space to explicit integer or positional-word labels, ruling out Roman numerals.

**V-02 C-46 failure mode (if it fails):** The rubric says "structurally distinct preamble statement that appears before the first checklist item." A prose statement is unambiguously a statement. A markdown table is structurally distinct from the checklist but may be read as a data structure, not a "statement." If the rubric requires prose form for "statement," a table-format preamble fails C-46 even when it explicitly commits both cardinality conditions. A C-46 FAIL for V-02 would narrow the preamble form space to prose, ruling out table-format declarations.
