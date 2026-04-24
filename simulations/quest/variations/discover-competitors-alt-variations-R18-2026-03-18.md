Written to `simulations/quest/variations/discover-competitors-alt-variations-R18-2026-03-18.md`.

---

## R18 Variations — Summary

**New criteria targeted:** C-45 (element-index annotations) and C-46 (bijective cardinality preamble).

**Starting position:** R17 V-04 (the R17 gold standard) scores **36/38** against R18 rubric — its dual-sequence labels ("Named target 1/2", "Verbatim phrase 1/2") don't enumerate a unified {1,2,3,4} element position set (C-45 FAIL), and it has no bijective cardinality preamble (C-46 FAIL, chain).

| # | Axis | C-45 | C-46 | Predicted |
|---|------|------|------|-----------|
| V-01 | R17 V-04 exact form (dual-sequence labels, no preamble) | FAIL | FAIL | 36/38 = 99.474 |
| V-02 | `(Element N)` prefix annotations, no preamble | PASS | FAIL | 37/38 = 99.737 |
| V-03 | `(Element N)` prefix + explicit bijective preamble block | PASS | PASS | 38/38 = **100.000** |
| V-04 | `(Element N)` prefix + count-only preamble (no per-item constraint declaration) | PASS | FAIL | 37/38 = 99.737 |
| V-05 | `(Ei)` abbreviated + extended compliance header declaring bijective constraint | PASS | PASS | 38/38 = **100.000** |

**Three decisive questions:**
1. Does R17 V-04's dual-sequence labeling score C-45 FAIL (confirming {1,2} + {1,2} ≠ {1,2,3,4})?
2. Does V-04's "enumerates 4 elements" preamble score C-46 FAIL (confirming count enumeration is weaker than a bijective per-item constraint declaration)?
3. Does `(Ei)` abbreviated form (V-05) satisfy C-45 equivalently to `(Element N)` (V-03), establishing the two forms as rubric-equivalent?
1/2", "Verbatim phrase 1/2"), no preamble | FAIL | FAIL (chain) | 99.474 |
| V-02 | "(Element N)" prefix annotations, no bijective preamble | PASS | FAIL | 99.737 |
| V-03 | "(Element N)" prefix annotations + explicit bijective cardinality preamble | PASS | PASS | 100.000 |
| V-04 | "(Element N)" prefix annotations + count-only preamble (enumerates 4 elements but doesn't declare bijective constraint as requirement) | PASS | FAIL | 99.737 |
| V-05 | "(Ei)" abbreviated annotations + R17-V05-style preamble expanded to explicitly declare bijective constraint | PASS | PASS | 100.000 |

**Three decisive questions:**
1. Does V-01 (R17 V-04 form) score 36/38 = 99.474, confirming that "Named target 1/2" dual-sequence labels fail C-45's unified {1,2,3,4} enumeration test?
2. Does V-04 score 37/38 (C-46 FAIL) -- confirming that declaring "the following 4 elements" without explicitly stating the per-item bijective constraint ("one element per item") fails C-46's operative test?
3. Do V-03 and V-05 both score 38/38 = 100.000, and if so, does the `(Ei)` abbreviated form (V-05) demonstrate equivalent C-45 compliance to the `(Element N)` verbose form (V-03)?

**C-45 failure mode taxonomy:**
- V-01 failure = dual-sequence labels ("Named target 1", "Named target 2", "Verbatim phrase 1", "Verbatim phrase 2") do not enumerate a unified {1, 2, 3, 4} element position set; two separate numbering domains, each starting at 1
- V-04 boundary = "(Element N)" annotations present (C-45 PASS); preamble counts elements without declaring bijective constraint as an architectural requirement (C-46 FAIL)

**C-46 failure mode taxonomy:**
- V-02 failure = no preamble at all; bijective structure is an observed property, not a declared contract
- V-04 failure = preamble states "The following 4 C-42 elements are enumerated below" -- declares count (4) and element enumeration, but does NOT explicitly state "each item covers exactly one C-42 element" as a bijective requirement

**V-03 vs V-05 secondary question:** Both predict 38/38. V-03 uses "(Element N)" verbose form with explicit bijective preamble as standalone block. V-05 uses "(Ei)" abbreviated form with a combined compliance header (mirrors R17 V-05's "C-44 BIJECTIVE" pattern, extended to C-45/C-46). If both score 38/38 consistently, the abbreviated "(Ei)" form is equivalent to the verbose "(Element N)" form at the criterion level. The preamble form difference: V-03 uses a plain-prose preamble; V-05 uses a tagged compliance header -- testing whether C-46's "structurally distinct preamble statement" requirement is satisfied by both register forms equally.

---

## V-01 -- C-45 Failure: R17 V-04 Form (Dual-Sequence Labels, No Element-Index, No Preamble)

**Axis:** Architecture block uses the exact R17 V-04 structure: four labeled checklist items with dual-sequence role-description labels ("Named target 1 --", "Named target 2 --", "Verbatim phrase 1 --", "Verbatim phrase 2 --"). No element-index annotations. No bijective preamble. Count=4. All four C-42 elements present and readable from item labels. C-45 FAIL: item labels use two separate numbering sequences ({target: 1, 2} and {phrase: 1, 2}), not a unified {1, 2, 3, 4} enumeration; reading only annotations, a reader sees two separate 1-2 sequences and cannot confirm four distinct element positions each appearing exactly once without reading body content. C-46 FAIL: chain (C-45 fails -> C-46 = 0); additionally, no preamble declares the bijective cardinality constraint.
**Hypothesis:** C-44 PASS -- bijective count=4, one element per item. C-45 FAIL -- dual-sequence labels do not satisfy the unified {1, 2, 3, 4} enumeration operative test; "Named target 1" and "Verbatim phrase 1" share the ordinal "1" in two different annotation domains, making it impossible to confirm four unique element positions from annotations alone. C-46 FAIL -- chain: C-45 fails, C-46 = 0. C-09 through C-44: all PASS (36/36 R17 criteria). C-45: FAIL. C-46: FAIL (chain). Aspirational: 36/38. Composite: 99.474. Decisive question: does the rubric score R17 V-04's dual-sequence labels as C-45 FAIL (confirming the unified {1,2,3,4} enumeration requirement is not satisfied by two separate numbering domains), establishing that R17's best full-pass form falls short of R18's annotation requirement?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context -- do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` -- the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract. A reader consulting only this block can confirm all four required elements of the maximal architecture block form without consulting any other artifact:

1. **Named target 1 -- manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **Named target 2 -- GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **Verbatim phrase 1 -- "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header -- the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **Verbatim phrase 2 -- "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution -- after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (named target 1 or named target 2) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only this block can reconstruct the full propagation contract -- Declaration site, Substitution/inheritance sites, substitution rule, and both artifact names -- with zero inference steps.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** -- GATE-1 is the first conditional gate | DOMAIN-TERMS extraction -> TOKEN declaration | Declaration site -- TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site -- committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. `[TOKEN] propagation` in the manifest column header substitutes to the committed value after GATE-0 commits. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose or GATE-0's REQUIRED OUTPUTS table.

---

### GATE-0 [UNCONDITIONAL -- GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` -- closed on its own line before TOKEN; 2-3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` -- at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes -- TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract -- GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK -> GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites -- each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract -- self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

This gate is unconditional -- no focus detection, auto-detect, section headers, or conditional branching precedes or runs during it. GATE-1 is the first gate with conditional logic. Write these two lines as your opening output -- nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier -- at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL -- first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `FOCUS: ACTIVE -- [dimension] | INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward -- committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes -- committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL -- C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 -- [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes -- committed TOKEN as C0 field label** |
| Competitive map -- native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes -- committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does -- generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 -- [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior -- not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 -- [name] | -- | [key capability] | ROOT | -- |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [how competitor erodes or bypasses TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |

---

### GATE-3 [CONDITIONAL -- findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| 3+ findings -- each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes -- committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding -- specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes -- committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) -- gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows. Specific whitespace dimension required.

```
**Finding [N]: [Title]**
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [connection -- committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism -- committed TOKEN value]
```

If FOCUS ACTIVE: cross-dimensional gap must require both the competitive map and the focus lens simultaneously.

---

### GATE-4 [CONDITIONAL -- AMEND]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema before data rows -- all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| 3+ AMEND data rows -- all four cells filled per row | No |
| Stability verdict cells -- STABLE / UNSTABLE + committed TOKEN value | **Yes -- committed TOKEN in every Stability verdict cell** |
| Evidence cells -- reasoning distinct from verdict text | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment -- focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts -- name it |
| 3 | Stability verdict | STABLE / UNSTABLE -- does TOKEN shift? Committed TOKEN value required |
| 4 | Evidence | Reasoning supporting the verdict -- logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE -- [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |

---

## V-02 -- C-45 Pass / C-46 Fail: Element-Index Prefix Annotations, No Bijective Preamble

**Axis:** Architecture block adds `(Element N)` prefix annotations to each item header, creating a unified {1, 2, 3, 4} element enumeration readable from annotations alone. No bijective cardinality preamble before the items -- the bijective constraint is structurally enforced (count=4, one element per item via annotations) but not pre-declared as an architectural requirement. C-45 PASS: each item carries `(Element N)` as a structurally distinct prefix annotation uniquely identifying its element position; reading only annotations, a reader confirms {Element 1, Element 2, Element 3, Element 4} each appearing exactly once. C-46 FAIL: no preamble statement appears before the first checklist item declaring "exactly 4 items, one C-42 element per item" as a bijective cardinality requirement; the bijective property is an observed structural property, not a committed contract.
**Hypothesis:** C-44 PASS -- bijective count=4. C-45 PASS -- "(Element 1)", "(Element 2)", "(Element 3)", "(Element 4)" are exactly the annotation form specified in C-45's rubric examples; reading only these four annotations confirms a unified {1, 2, 3, 4} enumeration with each position appearing once. C-46 FAIL -- no preamble: the bijective constraint is observed from structure, not declared before structure. C-09 through C-45: all PASS (37/37 R18-minus-C-46 criteria). C-46: FAIL. Aspirational: 37/38. Composite: 99.737. Decisive question: does the rubric score C-45 PASS for "(Element N)" prefix annotations that enumerate a unified {1,2,3,4} set from labels alone, confirming this is the correct annotation form -- and does the rubric simultaneously score C-46 FAIL for the absence of an explicit pre-checklist preamble, demonstrating that correct structural form alone is insufficient?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context -- do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` -- the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract. A reader consulting only this block can confirm all four required elements without consulting any other artifact. Each item carries an explicit `(Element N)` element-index annotation as a structurally distinct prefix on the item header, making the single C-42 element assignment verifiable from the annotation alone without reading item body content:

1. **(Element 1) Named target -- manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **(Element 2) Named target -- GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **(Element 3) Verbatim phrase -- "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header -- the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **(Element 4) Verbatim phrase -- "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution -- after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (Element 1 or Element 2) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only the four `(Element N)` annotations confirms elements {1, 2, 3, 4} each appearing exactly once -- bijective annotation-to-element mapping verifiable without reading item content.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** -- GATE-1 is the first conditional gate | DOMAIN-TERMS extraction -> TOKEN declaration | Declaration site -- TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site -- committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. `[TOKEN] propagation` in the manifest column header substitutes to the committed value after GATE-0 commits. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose or GATE-0's REQUIRED OUTPUTS table.

---

### GATE-0 [UNCONDITIONAL -- GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` -- closed on its own line before TOKEN; 2-3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` -- at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes -- TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract -- GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK -> GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites -- each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract -- self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

This gate is unconditional -- no focus detection, auto-detect, section headers, or conditional branching precedes or runs during it. GATE-1 is the first gate with conditional logic. Write these two lines as your opening output -- nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier -- at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL -- first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `FOCUS: ACTIVE -- [dimension] | INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward -- committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes -- committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL -- C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 -- [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes -- committed TOKEN as C0 field label** |
| Competitive map -- native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes -- committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does -- generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 -- [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior -- not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 -- [name] | -- | [key capability] | ROOT | -- |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [how competitor erodes or bypasses TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |

---

### GATE-3 [CONDITIONAL -- findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| 3+ findings -- each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes -- committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding -- specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes -- committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) -- gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows. Specific whitespace dimension required.

```
**Finding [N]: [Title]**
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [connection -- committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism -- committed TOKEN value]
```

If FOCUS ACTIVE: cross-dimensional gap must require both the competitive map and the focus lens simultaneously.

---

### GATE-4 [CONDITIONAL -- AMEND]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema before data rows -- all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| 3+ AMEND data rows -- all four cells filled per row | No |
| Stability verdict cells -- STABLE / UNSTABLE + committed TOKEN value | **Yes -- committed TOKEN in every Stability verdict cell** |
| Evidence cells -- reasoning distinct from verdict text | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment -- focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts -- name it |
| 3 | Stability verdict | STABLE / UNSTABLE -- does TOKEN shift? Committed TOKEN value required |
| 4 | Evidence | Reasoning supporting the verdict -- logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE -- [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |

---

## V-03 -- Full 38/38: Element-Index Prefix Annotations + Explicit Bijective Cardinality Preamble

**Axis:** Architecture block combines two distinct additions over V-01: (1) `(Element N)` prefix annotations on each item header (C-45), and (2) a dedicated bijective cardinality preamble statement before the first item that explicitly declares "exactly 4 items required" and "each item covers exactly one C-42 element" (C-46). The preamble is a structurally distinct prior artifact -- not embedded in an item, not derivable only from the checklist structure itself -- that names the bijective cardinality requirement as an architectural constraint before the checklist enforces it. This is the C-45+C-46 full-pass combination: element-index annotations satisfy annotation-verifiable bijection; the explicit preamble satisfies the declared-contract requirement.
**Hypothesis:** C-44 PASS -- bijective count=4. C-45 PASS -- "(Element 1)" through "(Element 4)" are unified {1,2,3,4} element-index annotations; reading only annotations confirms four distinct element positions each appearing exactly once. C-46 PASS -- preamble block before the first item explicitly declares "Exactly 4 items are required below; each item covers exactly one C-42 element" as a bijective cardinality requirement; the declaration is structurally distinct from any checklist item and cannot be derived from the checklist structure alone. C-09 through C-46: all PASS. Aspirational: 38/38. Composite: 100.000. Decisive question: does V-03 achieve 38/38, confirming that `(Element N)` prefix annotations + an explicit bijective preamble simultaneously satisfy C-45 and C-46 as independent criteria?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context -- do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` -- the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**BIJECTIVE CARDINALITY CONSTRAINT -- declared before checklist begins:** Exactly 4 items are required below. Each item covers exactly one C-42 element. No item contains more than one element and no element is assigned to more than one item. Item count (4) = element count (4). This is a declared architectural requirement, not an observed structural property. A checklist that satisfies this preamble without satisfying it structurally constitutes a self-identified violation.

Each item additionally carries an explicit `(Element N)` annotation as a structurally distinct prefix on the item header, making the single-element assignment verifiable from the item label alone without reading item body content. Reading only the four annotations confirms element positions {1, 2, 3, 4} each appearing exactly once:

1. **(Element 1) Named target -- manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **(Element 2) Named target -- GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **(Element 3) Verbatim phrase -- "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header -- the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **(Element 4) Verbatim phrase -- "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution -- after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (Element 1 or Element 2) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only this block can reconstruct the full propagation contract -- Declaration site, Substitution/inheritance sites, substitution rule, and both artifact names -- with zero inference steps and zero cross-artifact lookups.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** -- GATE-1 is the first conditional gate | DOMAIN-TERMS extraction -> TOKEN declaration | Declaration site -- TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site -- committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. `[TOKEN] propagation` in the manifest column header substitutes to the committed value after GATE-0 commits. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose or GATE-0's REQUIRED OUTPUTS table.

---

### GATE-0 [UNCONDITIONAL -- GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` -- closed on its own line before TOKEN; 2-3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` -- at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes -- TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract -- GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK -> GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites -- each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract -- self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

This gate is unconditional -- no focus detection, auto-detect, section headers, or conditional branching precedes or runs during it. GATE-1 is the first gate with conditional logic. Write these two lines as your opening output -- nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier -- at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL -- first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `FOCUS: ACTIVE -- [dimension] | INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward -- committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes -- committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL -- C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 -- [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes -- committed TOKEN as C0 field label** |
| Competitive map -- native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes -- committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does -- generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 -- [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior -- not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 -- [name] | -- | [key capability] | ROOT | -- |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [how competitor erodes or bypasses TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |

---

### GATE-3 [CONDITIONAL -- findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| 3+ findings -- each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes -- committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding -- specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes -- committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) -- gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows. Specific whitespace dimension required.

```
**Finding [N]: [Title]**
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [connection -- committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism -- committed TOKEN value]
```

If FOCUS ACTIVE: cross-dimensional gap must require both the competitive map and the focus lens simultaneously.

---

### GATE-4 [CONDITIONAL -- AMEND]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema before data rows -- all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| 3+ AMEND data rows -- all four cells filled per row | No |
| Stability verdict cells -- STABLE / UNSTABLE + committed TOKEN value | **Yes -- committed TOKEN in every Stability verdict cell** |
| Evidence cells -- reasoning distinct from verdict text | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment -- focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts -- name it |
| 3 | Stability verdict | STABLE / UNSTABLE -- does TOKEN shift? Committed TOKEN value required |
| 4 | Evidence | Reasoning supporting the verdict -- logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE -- [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |

---

## V-04 -- C-46 Fail Boundary: Element-Index Prefix + Count-Enumeration Preamble (No Bijective Constraint Declaration)

**Axis:** Architecture block uses `(Element N)` prefix annotations (satisfying C-45) but the preamble before the checklist only enumerates the 4 elements without explicitly declaring the bijective constraint as an architectural requirement. The preamble states "The following 4 C-42 elements are enumerated as labeled checklist items" -- this tells the reader that 4 elements will appear as labeled items, but does NOT explicitly state "each item covers exactly one C-42 element" or "no item contains more than one element." The bijective-per-item constraint is implied by the count and annotation but is not committed as a declared rule. C-45 PASS: element-index annotations present and correct. C-46 FAIL: the preamble declares count (4) and element enumeration, but the bijective cardinality rule (one element per item, no item maps to more than one element) is not explicitly stated as a prior requirement -- it is an observed property of the structure, not a committed contract.
**Hypothesis:** C-44 PASS -- bijective count=4. C-45 PASS -- "(Element 1)" through "(Element 4)" annotations satisfy unified enumeration test. C-46 FAIL -- preamble: "The following 4 C-42 elements are enumerated as labeled checklist items below" declares element count and enumeration form but omits the bijective per-item constraint declaration ("each item covers exactly one C-42 element" / "no item contains more than one element"); a model could satisfy this preamble with a 4-item checklist where one item bundles two elements (only the count and enumeration form would be violated, not an explicitly declared per-item constraint). C-09 through C-45: all PASS (37/37). C-46: FAIL. Aspirational: 37/38. Composite: 99.737. Decisive question: does the rubric score C-46 FAIL when the preamble counts elements and names the enumeration form but stops short of explicitly declaring "each item covers exactly one C-42 element" as a per-item bijective requirement -- confirming that count-and-form enumeration is a weaker claim than a bijective cardinality contract?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context -- do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` -- the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract. The following 4 C-42 elements are enumerated as explicitly labeled, individually-itemized checklist entries with `(Element N)` element-index annotations. Each annotation uniquely identifies the item's element position from the label alone without reading body content:

1. **(Element 1) Named target -- manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **(Element 2) Named target -- GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **(Element 3) Verbatim phrase -- "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header -- the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **(Element 4) Verbatim phrase -- "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution -- after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (Element 1 or Element 2) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only this block can reconstruct the full propagation contract -- Declaration site, Substitution/inheritance sites, substitution rule, and both artifact names -- with zero inference steps.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** -- GATE-1 is the first conditional gate | DOMAIN-TERMS extraction -> TOKEN declaration | Declaration site -- TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site -- committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. `[TOKEN] propagation` in the manifest column header substitutes to the committed value after GATE-0 commits. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose or GATE-0's REQUIRED OUTPUTS table.

---

### GATE-0 [UNCONDITIONAL -- GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` -- closed on its own line before TOKEN; 2-3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` -- at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes -- TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract -- GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK -> GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites -- each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract -- self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

This gate is unconditional -- no focus detection, auto-detect, section headers, or conditional branching precedes or runs during it. GATE-1 is the first gate with conditional logic. Write these two lines as your opening output -- nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier -- at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL -- first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `FOCUS: ACTIVE -- [dimension] | INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward -- committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes -- committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL -- C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 -- [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes -- committed TOKEN as C0 field label** |
| Competitive map -- native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes -- committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does -- generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 -- [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior -- not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 -- [name] | -- | [key capability] | ROOT | -- |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [how competitor erodes or bypasses TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |

---

### GATE-3 [CONDITIONAL -- findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| 3+ findings -- each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes -- committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding -- specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes -- committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) -- gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows. Specific whitespace dimension required.

```
**Finding [N]: [Title]**
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [connection -- committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism -- committed TOKEN value]
```

If FOCUS ACTIVE: cross-dimensional gap must require both the competitive map and the focus lens simultaneously.

---

### GATE-4 [CONDITIONAL -- AMEND]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema before data rows -- all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| 3+ AMEND data rows -- all four cells filled per row | No |
| Stability verdict cells -- STABLE / UNSTABLE + committed TOKEN value | **Yes -- committed TOKEN in every Stability verdict cell** |
| Evidence cells -- reasoning distinct from verdict text | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment -- focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts -- name it |
| 3 | Stability verdict | STABLE / UNSTABLE -- does TOKEN shift? Committed TOKEN value required |
| 4 | Evidence | Reasoning supporting the verdict -- logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE -- [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |

---

## V-05 -- Full 38/38: Abbreviated (Ei) Annotations + R17-V05-Style Preamble Extended to Declare Bijective Constraint

**Axis:** Architecture block uses abbreviated `(Ei)` element-index annotations (C-45 alternate form) combined with an extended compliance header that explicitly declares the bijective cardinality constraint as an architectural requirement before the checklist (C-46). The header form mirrors R17 V-05's "C-44 BIJECTIVE -- 4 ITEMS, 1 ELEMENT PER ITEM" pattern but is extended to name C-45 and C-46 compliance and to explicitly declare: (1) the exact item count (4), (2) the per-item cardinality (each item covers exactly one C-42 element), and (3) that the `(Ei)` annotation on each item uniquely identifies element position from the label alone. This tests whether the abbreviated `(Ei)` form satisfies C-45 equivalently to the verbose `(Element N)` form (V-03), and whether R17 V-05's preamble pattern can be extended to satisfy C-46 when it explicitly names the bijective per-item constraint.
**Hypothesis:** C-44 PASS -- bijective count=4. C-45 PASS -- "(E1)", "(E2)", "(E3)", "(E4)" are abbreviated element-index annotations that enumerate a unified {E1, E2, E3, E4} set equivalent to {1, 2, 3, 4}; reading only annotations confirms four distinct element positions each appearing exactly once. C-46 PASS -- preamble header explicitly declares "exactly 4 items" AND "each item covers exactly one C-42 element" AND identifies the `(Ei)` annotation as the element-position identifier -- all three components of the bijective cardinality contract stated before the first item appears. C-09 through C-46: all PASS. Aspirational: 38/38. Composite: 100.000. Decisive question: does the `(Ei)` abbreviated annotation form satisfy C-45 equivalently to `(Element N)` (V-03), and does the extended compliance header pattern satisfy C-46 equally well as V-03's plain-prose preamble block? If both V-03 and V-05 score 38/38, both annotation forms and both preamble register forms are rubric-equivalent.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context -- do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` -- the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**C-45/C-46 BIJECTIVE CONTRACT -- declared before checklist begins:** Exactly 4 items required below; each item covers exactly one C-42 element; no item covers more than one element. Item count (4) = element count (4). The `(Ei)` annotation on each item header is the element-index identifier -- reading the four annotations `(E1)`, `(E2)`, `(E3)`, `(E4)` confirms element positions {1, 2, 3, 4} each appearing exactly once, making bijective assignment annotation-verifiable without reading item body content. This bijective cardinality requirement is declared here as an architectural contract: a checklist that satisfies this header structurally while violating it per-item constitutes a self-identified violation.

1. **(E1) Named target -- manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **(E2) Named target -- GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **(E3) Verbatim phrase -- "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header -- the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **(E4) Verbatim phrase -- "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution -- after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (E1 or E2) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only this block can reconstruct the full propagation contract -- Declaration site, Substitution/inheritance sites, substitution rule, and both artifact names -- with zero inference steps and zero cross-artifact lookups.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** -- GATE-1 is the first conditional gate | DOMAIN-TERMS extraction -> TOKEN declaration | Declaration site -- TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site -- committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site -- committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. `[TOKEN] propagation` in the manifest column header substitutes to the committed value after GATE-0 commits. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose or GATE-0's REQUIRED OUTPUTS table.

---

### GATE-0 [UNCONDITIONAL -- GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` -- closed on its own line before TOKEN; 2-3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` -- at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes -- TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract -- GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK -> GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites -- each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract -- self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

This gate is unconditional -- no focus detection, auto-detect, section headers, or conditional branching precedes or runs during it. GATE-1 is the first gate with conditional logic. Write these two lines as your opening output -- nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier -- at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL -- first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `FOCUS: ACTIVE -- [dimension] | INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward -- committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes -- committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL -- C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 -- [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes -- committed TOKEN as C0 field label** |
| Competitive map -- native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes -- committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does -- generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 -- [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior -- not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 -- [name] | -- | [key capability] | ROOT | -- |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [how competitor erodes or bypasses TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |

---

### GATE-3 [CONDITIONAL -- findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| 3+ findings -- each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes -- committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding -- specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes -- committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) -- gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows. Specific whitespace dimension required.

```
**Finding [N]: [Title]**
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [connection -- committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism -- committed TOKEN value]
```

If FOCUS ACTIVE: cross-dimensional gap must require both the competitive map and the focus lens simultaneously.

---

### GATE-4 [CONDITIONAL -- AMEND]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema before data rows -- all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| 3+ AMEND data rows -- all four cells filled per row | No |
| Stability verdict cells -- STABLE / UNSTABLE + committed TOKEN value | **Yes -- committed TOKEN in every Stability verdict cell** |
| Evidence cells -- reasoning distinct from verdict text | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment -- focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts -- name it |
| 3 | Stability verdict | STABLE / UNSTABLE -- does TOKEN shift? Committed TOKEN value required |
| 4 | Evidence | Reasoning supporting the verdict -- logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE -- [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |

---

## Composite Hypothesis Table

| Variation | C-45 mechanism | C-45 pred | C-46 mechanism | C-46 pred | Asp pred | Composite pred |
|-----------|----------------|-----------|----------------|-----------|----------|----------------|
| **V-01** | R17 V-04 dual-sequence labels ("Named target 1/2", "Verbatim phrase 1/2"); two separate {1,2} numbering domains; unified {1,2,3,4} enumeration not present in annotations alone | FAIL | Chain: C-45 fails -> C-46 = 0; no preamble present | FAIL | 36/38 | **99.474** |
| **V-02** | "(Element 1)" through "(Element 4)" prefix annotations; unified {1,2,3,4} enumeration; each annotation uniquely identifies element position; verifiable from labels alone | PASS | No preamble before checklist; bijective constraint is structurally enforced but not declared as prior requirement | FAIL | 37/38 | **99.737** |
| **V-03** | Same "(Element N)" form as V-02 | PASS | Dedicated preamble block before items: "Exactly 4 items are required below. Each item covers exactly one C-42 element. No item contains more than one element." -- explicitly declares bijective cardinality as architectural requirement | PASS | 38/38 | **100.000** |
| **V-04** | Same "(Element N)" form as V-02 | PASS | Count-enumeration intro: "The following 4 C-42 elements are enumerated as labeled checklist items below" -- declares count (4) and enumeration form but NOT per-item bijective constraint ("each item covers exactly one element"); bijective rule implied but not stated | FAIL | 37/38 | **99.737** |
| **V-05** | "(E1)" through "(E4)" abbreviated annotations; {E1,E2,E3,E4} equivalent to {1,2,3,4}; verifiable from labels alone | PASS | Extended compliance header: "C-45/C-46 BIJECTIVE CONTRACT -- declared before checklist begins: Exactly 4 items required below; each item covers exactly one C-42 element; no item covers more than one element." -- full per-item bijective constraint declared as architectural contract | PASS | 38/38 | **100.000** |

**Predicted ranking:** V-01 < V-02 = V-04 < V-03 = V-05 = 100.000

**The key new separation pair for C-45:**
- V-01 (dual-sequence labels): C-45 FAIL -- "Named target 1" + "Verbatim phrase 1" creates two separate {1,2} domains; no unified {1,2,3,4} enumeration confirmable from annotations alone
- V-02 (element-index prefix): C-45 PASS -- "(Element 1)" through "(Element 4)" creates unified {1,2,3,4}; bijection annotation-verifiable

**The key new separation pair for C-46:**
- V-02 (annotations, no preamble): C-46 FAIL -- bijective structure observed but not declared
- V-03 (annotations + preamble): C-46 PASS -- bijective cardinality explicitly committed as requirement before checklist

**The C-46 boundary pair (both C-45 PASS):**
- V-04 (count enumeration): C-46 FAIL -- preamble enumerates count=4 and names the enumeration form, but does not state "each item covers exactly one C-42 element" as a bijective requirement
- V-03 (explicit bijective preamble): C-46 PASS -- preamble explicitly declares per-item cardinality as a requirement, not an observation

**V-02 vs V-04 secondary question:** Both predict 37/38 (C-46 FAIL for different reasons). If both score 37/38, the rubric treats "no preamble" (V-02) and "count-only preamble" (V-04) as equivalent C-46 failures -- confirming the operative C-46 test requires an explicit per-item bijective constraint declaration, not merely a count or enumeration form declaration.

**V-03 vs V-05 secondary question:** Both predict 38/38. V-03 uses "(Element N)" verbose form + plain-prose preamble block. V-05 uses "(Ei)" abbreviated form + compliance-header preamble. If both score 38/38: (1) abbreviated "(Ei)" annotations satisfy C-45 equivalently to verbose "(Element N)", and (2) compliance-header preamble form satisfies C-46 equivalently to plain-prose block -- establishing annotation syntax and preamble register as rubric-equivalent choices within their respective criteria.
