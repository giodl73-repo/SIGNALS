Written to `simulations/quest/variations/discover-competitors-alt-variations-R17-2026-03-18.md`.

---

## R17 Variations Summary

**New criterion driving this round: C-44** — bijective element-to-item mapping (exactly 4 items, one C-42 element per item). C-44 closes the gap that R16 V-02's 3-item list exposed: C-43 requires a checklist form, C-44 requires the bijective distribution within that form.

**5 variations across 3 axes:**

| # | Architecture block form | C-43 | C-44 | Composite |
|---|------------------------|------|------|-----------|
| V-01 | 4-item list, item 1 bundles elements 1+4; item 4 = non-C-42 independence note | PASS | FAIL | 99.722 |
| V-02 | 3-item list, item 1 bundles elements 1+2 (both artifact names) | FAIL | FAIL (chain) | 99.444 |
| V-03 | 5-item list, items 1-4 carry elements 1-4, item 5 = labeled non-C-42 note | ??? | FAIL | 99.444 or 99.722 |
| V-04 | Standard 4-item bijective labeled checklist (R16 V-04 form) | PASS | PASS | 100.000 |
| V-05 | V-04 + "C-44 BIJECTIVE -- 4 ITEMS, 1 ELEMENT PER ITEM" pre-declaration header | PASS | PASS | 100.000 |

**Three decisive questions:**
1. Does V-01 score 99.722 (C-43 PASS / C-44 FAIL), confirming they are distinct criteria at distinct score levels?
2. Does V-03 (count=5) match V-02 at 99.444 (C-43 symmetric on cardinality), or V-01 at 99.722 (C-43 tolerates extra items)?
3. Does V-05's bijective pre-declaration header add multi-run drift resistance beyond V-04, or are both equally stable at 36/36?
t=4 satisfies C-43 count-verification; bijective fails because one item carries two C-42 elements. The key C-43-PASS / C-44-FAIL boundary case.
- **Under-cardinality with element bundling** (V-02): count=3, elements 1+2 bundled in item 1. Both C-43 and C-44 fail. Tests whether the rubric differentiates the 3-item double-fail (V-02) from the 4-item bijective-only fail (V-01) by scoring one criterion gap vs two.
- **Over-cardinality with non-C-42 extra item** (V-03): count=5, items 1-4 each carry exactly one element, item 5 is a labeled independence note. C-44 FAIL (count > 4). C-43 ambiguous: items 1-4 individually satisfy element-per-item discipline, but count=5 breaks "completeness verifiable by item count alone."

**Combined axes:** V-05 = V-04 bijective labeled checklist + explicit C-44 bijective compliance pre-declaration header.

**Three decisive questions:**
1. Does V-01 score exactly 35/36 = 99.722 (C-43 PASS, C-44 FAIL atomic, no partial credit), confirming that a 4-item checklist with one bundled item satisfies C-43 but fails C-44 as distinct criteria?
2. Does V-03 (5-item, count > 4) score 35/36 (C-43 PASS, C-44 FAIL) or 34/36 (both fail) -- revealing whether C-43 "completeness verifiable by item count alone" is broken by count > 4 as well as count < 4?
3. Does V-05's bijective pre-declaration header create any scoring or reliability advantage over V-04, or are they equivalent at 36/36?

---

## V-01 -- C-44 Failure: 4-Item Checklist with Item 1 Bundling Elements 1+4

**Axis:** Architecture block uses a 4-item numbered checklist with explicit labels. Item 1 bundles two C-42 elements: the manifest TOKEN-propagation column name (element 1) and the verbatim phrase "Substitution/inheritance site" (element 4) in item 1's description. Items 2 and 3 each carry one element (elements 2 and 3 respectively). Item 4 is an explicitly-labeled independence confirmation (non-C-42 structural note). Count=4. All four C-42 elements are readable from the block by label scan. C-43 PASS: four labeled items, all four C-42 elements present and confirmable by label scan without parsing item prose. C-44 FAIL: item 1 maps to two C-42 elements (elements 1+4), item 4 maps to zero C-42 elements -- bijective constraint violated, item count (4) does not equal the number of per-item C-42 elements (4 items but elements distributed 2+1+1+0 rather than 1+1+1+1).
**Hypothesis:** C-43 PASS -- four labeled items, all four C-42 elements identifiable by label scan; item count=4 passes the count-verification test because C-43 does not enforce per-item cardinality. C-44 FAIL -- item 1 carries elements 1 and 4 simultaneously; bijective mapping breaks: a reader counting 4 items cannot confirm that each item carries exactly one element without reading content. C-09 through C-43: all PASS (all 35 R16 criteria satisfied). C-44: FAIL. Aspirational: 35/36. Composite: 99.722. Decisive question: does the rubric score C-43 PASS for this 4-item list (because count=4 and all elements present) while scoring C-44 FAIL (because bijective mapping breaks), confirming C-44 adds cardinality enforcement that C-43 alone cannot provide?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context -- do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` -- the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract. A reader consulting only this block can confirm all four required elements of the maximal architecture block form without consulting any other artifact:

1. **Named target 1 -- manifest TOKEN-propagation column and "Substitution/inheritance site" verbatim:** The `[TOKEN] propagation` column in the EXECUTION PLAN table independently carries the complete propagation contract. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site" -- the verbatim rubric-vocabulary term for every gate where the committed TOKEN value substitutes `[TOKEN]` in REQUIRED OUTPUTS column headers. Which gate declares TOKEN and which gates consume it is verifiable from this column alone.

2. **Named target 2 -- GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **Verbatim phrase 1 -- "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header -- the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **Independence confirmation -- dual-layer contract:** Neither artifact (named target 1 or named target 2) is load-bearing for the other. Both are independently self-contained. A reader consulting only this block can reconstruct the full propagation contract -- Declaration site, Substitution/inheritance sites, and substitution rule -- with zero inference steps and zero cross-artifact lookups.

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

## V-02 -- C-43 Failure / C-44 Failure: 3-Item Checklist, Elements 1+2 Bundled in Item 1

**Axis:** Architecture block uses a 3-item numbered checklist with explicit per-item labels. Item 1 bundles both C-42 artifact-name elements (elements 1 and 2) under a single label: "Named targets -- manifest TOKEN-propagation column and GATE-0's REQUIRED OUTPUTS table." Items 2 and 3 each carry one verbatim phrase (elements 3 and 4 respectively). Count=3. All four C-42 elements are present and readable. C-43 FAIL: count=3 means a reader verifying completeness by item count finds only 3 items -- cannot confirm all four elements are present without reading item 1's content to discover both artifact names. C-44 FAIL: chain dependency (C-43 fails -> C-44 scored 0); additionally, count=3 != 4 breaks the bijective constraint from below.
**Hypothesis:** C-43 FAIL -- count=3 fails the "completeness verifiable by item count alone" test; a reader counting 3 items cannot confirm 4 elements are present. C-44 FAIL -- chain: C-43 fails, C-44 = 0. All 34 R15 criteria: PASS. C-43: FAIL. C-44: FAIL (chain). Aspirational: 34/36. Composite: 99.444. This is the under-cardinality failure analog to V-01's over-distribution failure: both V-01 and V-02 violate bijective mapping, but V-01 does so at count=4 (C-43 PASS boundary) while V-02 does so at count=3 (C-43 FAIL territory). Decisive question: does the rubric score V-01 and V-02 differently (99.722 vs 99.444) because V-01 passes C-43 while V-02 fails both -- confirming C-43 and C-44 are distinct criteria at distinct score levels?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context -- do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` -- the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract. A reader consulting only this block can confirm all four required elements without consulting any other artifact:

1. **Named targets -- manifest TOKEN-propagation column and GATE-0's REQUIRED OUTPUTS table:** These are the two structural artifacts that independently carry the propagation contract. The `[TOKEN] propagation` column in the EXECUTION PLAN table (GATE-0 row: "Declaration site"; GATE-1+ rows: "Substitution/inheritance site") and the dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table each independently state which gate declares TOKEN, which gates consume it by substitution, and what substitution rule applies. Neither is load-bearing for the other. Both are targets of this architecture block.

2. **Verbatim phrase 1 -- "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header -- the template form is preserved so the substitution rule is explicit rather than already consumed. The committed value propagates to all downstream gates.

3. **Verbatim phrase 2 -- "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution -- after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier. Each gate independently carries the TOKEN value without referencing GATE-0's table or the manifest column.

A reader consulting only this block can reconstruct the full propagation contract -- Declaration site, Substitution/inheritance sites, both artifact names, and substitution rule -- with zero inference steps.

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

## V-03 -- C-44 Failure (Upper Cardinality): 5-Item Checklist with Extra Labeled Independence Item

**Axis:** Architecture block uses a 5-item numbered checklist with explicit per-item labels. Items 1-4 each carry exactly one C-42 element (one element per item, bijective within the first four items). Item 5 is an explicitly-labeled structural closure note: "Independence confirmation -- dual-layer contract" with non-C-42 content about artifact independence. Count=5. All four C-42 elements are present and individually labeled (items 1-4). C-44 FAIL: count=5 != 4; the bijective constraint requires exactly 4 items, one per element -- the extra item breaks count-verification (a reader counting 5 items cannot determine 4 elements are present without reading content to identify which item is the non-C-42 one). C-43 status is the decisive ambiguity: items 1-4 each individually carry one element with explicit labels (satisfying element-per-item discipline and individual labeling), but count=5 breaks "completeness verifiable by item count alone."
**Hypothesis:** C-44 FAIL -- count=5 != 4; bijective constraint violated from above. C-43 AMBIGUOUS -- two interpretations compete: (a) C-43 FAIL because count=5 breaks "completeness verifiable by item count alone" (counting 5 items does not confirm exactly 4 elements are present, since one item may be non-C-42 or duplicated); (b) C-43 PASS because "a reader can identify four labeled items and match each to one of the four C-42 required elements" is satisfied by items 1-4 regardless of item 5. If (a): Aspirational 34/36. Composite: 99.444. If (b): Aspirational 35/36. Composite: 99.722. Decisive question: does C-43's "completeness verifiable by item count alone" require count=4 as a necessary condition, or does it only require that all four elements be individually identifiable by label (in which case extra items are tolerated)?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context -- do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` -- the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract. A reader consulting only this block can confirm all four required elements without consulting any other artifact:

1. **Named target 1 -- manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **Named target 2 -- GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row.

3. **Verbatim phrase 1 -- "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header -- the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **Verbatim phrase 2 -- "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution -- after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

5. **Independence confirmation -- dual-layer contract:** Neither artifact (named target 1 or named target 2) is load-bearing for the other. Both are independently self-contained. A reader consulting only this block can reconstruct the full propagation contract -- Declaration site, Substitution/inheritance sites, and substitution rule -- with zero inference steps and zero cross-artifact lookups.

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

## V-04 -- Full 36/36: Standard 4-Item Bijective Labeled Checklist (R16 V-04 Form)

**Axis:** Architecture block uses a 4-item numbered checklist with explicit per-item labels -- the R16 V-04 structure confirmed as the baseline full-pass for C-43 and now also C-44. Item labels: "Named target 1 -- manifest TOKEN-propagation column," "Named target 2 -- GATE-0's REQUIRED OUTPUTS table," "Verbatim phrase 1 -- 'Declaration site'," "Verbatim phrase 2 -- 'Substitution/inheritance site'" -- exactly one C-42 element per item, bijective mapping enforced by structure. Count=4. Item count = element count = 4. C-43 PASS: four labeled items, all four C-42 elements present and confirmable by label scan without reading item prose. C-44 PASS: exactly 4 items, one element per item; bijective constraint satisfied; item count (4) is the sole verification mechanism.
**Hypothesis:** C-43 PASS -- four items, each explicitly labeled by element type; item count=4 verifies all four elements present. C-44 PASS -- bijective: exactly 4 items, one element each; no item bundles two elements; item count = element count = 4; count-verification works. C-09 through C-43: all PASS (35/35 R16 criteria). C-44: PASS. Aspirational: 36/36. Composite: 100.000. Decisive question for V-04 vs V-05: does the explicit bijective compliance pre-declaration in V-05 create any scoring or reliability advantage, or is V-04's structural form alone sufficient for 36/36?

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

## V-05 -- Full 36/36: 4-Item Bijective Labeled Checklist with Explicit C-44 Bijective Pre-Declaration

**Axis:** Architecture block uses the same 4-item labeled checklist as V-04, but adds an explicit bijective compliance header before the items: **`C-44 BIJECTIVE -- 4 ITEMS, 1 ELEMENT PER ITEM.`** The header pre-declares both the exact count (4) and the bijective constraint (1 element per item) before any item is read. Item count = element count = 4 is machine-verifiable from the header alone without counting items or reading content. C-43 PASS: labeled items, count verifiable. C-44 PASS: bijective constraint pre-declared and structurally enforced. Combined axis: V-04 bijective labeled checklist + explicit C-44 bijective compliance pre-declaration header.
**Hypothesis:** C-43 PASS -- four labeled items, element identity verifiable by label scan. C-44 PASS -- header "C-44 BIJECTIVE -- 4 ITEMS, 1 ELEMENT PER ITEM" pre-declares the bijective constraint; four items follow with one element each; count-verification works from header alone. C-09 through C-44: all PASS. Aspirational: 36/36. Composite: 100.000. Decisive question: does the bijective pre-declaration header provide measurable reliability advantage over V-04's structure-only form (i.e., does it reduce model drift in multi-run testing), or does it add overhead that risks structural confusion at adjacent criteria? Is V-05's header analogous in function to R16 V-05's C-43 compliance header -- a declared count anchor that stabilizes the downstream item form?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context -- do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` -- the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**C-44 BIJECTIVE -- 4 ITEMS, 1 ELEMENT PER ITEM.** The following four elements are enumerated as explicitly labeled, individually-itemized checklist entries. Exactly one C-42 element is assigned to each item -- no item contains more than one element. Item count (4) = element count (4). Completeness is verifiable by item count alone without reading item prose:

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

## Composite Hypothesis Table

| Variation | C-43 mechanism | C-43 pred | C-44 mechanism | C-44 pred | Asp pred | Composite pred |
|-----------|----------------|-----------|----------------|-----------|----------|----------------|
| **V-01** | 4-item labeled list; item 1 bundles elements 1+4; item 4 = independence note (non-C-42); count=4; all elements readable by label scan | PASS | Item 1 maps to 2 elements (1+4); item 4 maps to 0 C-42 elements; bijective distribution = 2+1+1+0, not 1+1+1+1 | FAIL | 35/36 | **99.722** |
| **V-02** | 3-item labeled list; item 1 bundles elements 1+2 (both artifact names); items 2+3 each carry one phrase; count=3 | FAIL | Chain: C-43 fails -> C-44 = 0; additionally count=3 < 4 | FAIL | 34/36 | **99.444** |
| **V-03** | 5-item labeled list; items 1-4 each carry one element; item 5 = labeled independence note (non-C-42); count=5 | ??? | Count=5 != 4; bijective breaks from above | FAIL | 34/36 or 35/36 | **99.444 or 99.722** |
| **V-04** | 4-item labeled list; items 1-4 each carry one element; count=4; label-scan verifies all four elements; standard R16 V-04 form | PASS | Exactly 4 items, one element per item; bijective 1+1+1+1; item count = element count = 4 | PASS | 36/36 | **100.000** |
| **V-05** | Same 4-item labeled list as V-04; bijective header pre-declares count and constraint before items | PASS | Header "C-44 BIJECTIVE -- 4 ITEMS, 1 ELEMENT PER ITEM" pre-declares bijective constraint; 4 items follow with one element each | PASS | 36/36 | **100.000** |

**Predicted ranking:** V-02 <= V-03 <= V-01 < V-04 = V-05 = 100.000

**The key new separation:** C-43 and C-44 are distinct criteria at distinct score levels. V-01 and V-02 are the decisive pair:
- V-01 (C-43 PASS, C-44 FAIL): 99.722 -- 4-item list passes C-43's count test, fails C-44's bijective constraint
- V-02 (C-43 FAIL, C-44 FAIL): 99.444 -- 3-item list fails C-43's count test AND C-44 by chain

If scorecards confirm V-01 at 99.722 and V-02 at 99.444, the rubric correctly treats C-43 and C-44 as independent criteria with separate scoring paths. The 0.278-point gap between V-01 and V-02 is exactly one criterion's weight -- confirming C-44 is atomic and C-43 is separately atomic.

**V-03 as the diagnostic pivot:** V-03 tests whether C-43 is symmetrical on cardinality violations -- whether "completeness verifiable by item count alone" breaks for count > 4 (V-03) just as it breaks for count < 4 (V-02). Three outcomes are possible:
- V-03 = 99.444 (same as V-02): C-43 is count-symmetric -- exactly 4 items required; both under- and over-cardinality fail C-43. C-44 adds only the per-item distribution constraint.
- V-03 = 99.722 (same as V-01): C-43 tolerates extra items -- items 1-4 each individually match one element, satisfying the operative test regardless of item 5. C-44 is the only criterion that enforces count=4 as a ceiling as well as a floor.
- V-03 > 99.722: unexpected; would suggest C-43 requires strictly fewer than 5 items while V-01 (which is also C-43 PASS) requires no such constraint -- an internal inconsistency in the rubric.

**C-44 failure mode taxonomy for R17:**
- V-01 failure = bijective distribution violation at count=4 (item bundles two elements; non-C-42 placeholder occupies fourth slot; upper-bound count satisfied but per-item cardinality fails)
- V-02 failure = under-cardinality with element bundling (count < 4; C-43 also fails; two criteria missed simultaneously)
- V-03 failure = over-cardinality with structurally benign extra item (count > 4; items 1-4 individually correct; C-43 ambiguous; C-44 fails regardless)

**V-04 vs V-05 secondary question:** Both predict 36/36. V-05's bijective header mirrors R16 V-05's C-43 compliance header pattern. If both score 36/36 consistently, the bijective header is structurally redundant at the criterion level but potentially valuable for multi-run drift resistance -- the same conclusion R16 reached about the C-43 compliance header in R16 V-05. If V-05 maintains 36/36 in later rounds while V-04 drifts to 35/36 (C-44 fails when model collapses a checklist item under pressure), the bijective pre-declaration is the differentiating mechanism.
