Written to `simulations/quest/variations/discover-competitors-alt-variations-R16-2026-03-18.md`.

---

## R16 Variations — discover-competitors-alt (Round 16)

**New criterion: C-43** — Architecture block enumerates the four C-42 elements as explicitly labeled, individually-itemized checklist entries.

**5 variations, single-axis first:**

| # | Axis | C-43 | Asp | Composite |
|---|------|------|-----|-----------|
| V-01 | C-43 FAIL — prose architecture block (R15 V-04 form; all four elements present but not checklist-itemized) | FAIL | 34/35 | **99.714** |
| V-02 | C-43 FAIL — 3-item partial checklist (item 4 collapsed into item 1's prose; count = 3) | FAIL | 34/35 | **99.714** |
| V-03 | C-43 FAIL — 4 unlabeled bullet points (count = 4, one element per item, but no per-item label headers) | FAIL | 34/35 | **99.714** |
| V-04 | C-43 PASS — standard 4-item labeled checklist (R15 V-05 form promoted to primary full-pass) | PASS | 35/35 | **100.000** |
| V-05 | C-43 PASS — 4-item labeled checklist + `C-43 COMPLIANCE -- 4 ITEMS` count declaration header | PASS | 35/35 | **100.000** |

**Three variation axes tested:**
- **Architecture block form** (V-01): prose vs checklist — the primary C-43 distinction
- **Item count** (V-02): 3-item partial checklist — tests whether "individually-itemized" enforces element-per-item discipline
- **Label presence** (V-03): 4 unlabeled bullets — tests whether "explicitly labeled" is a distinct constraint from "individually-itemized"

**Combined axes:** V-05 = V-04 labeled checklist + explicit count pre-declaration header

**Three decisive questions:**
1. Do all three failure modes score identically at 99.714 (C-43 atomic, no partial credit), or does V-03's count-satisfied form score above V-01/V-02?
2. Does the rubric enforce "explicitly labeled" as distinct from "individually-itemized" when both requirements are written into C-43's pass condition?
3. Does V-05's count declaration header provide any reliability advantage over V-04 at the criterion level, or does it only matter for model-compliance consistency across multiple runs?
emized" requirement enforces element-per-item discipline, not just checklist presence.

- **V-03** is a second new axis: four bullet points in the architecture block, each carrying one C-42 element, but without per-item label headers ("Named target 1 —", "Verbatim phrase 1 —", etc.). Items are individually enumerable (count = 4) and each contains exactly one C-42 element. But the "explicitly labeled" requirement in C-43 requires each item to be identifiable by its label alone, without reading the item's prose. Unlabeled bullets fail this — the element identity is encoded in the content, not the structure. C-43 FAIL. Tests whether "explicitly labeled" is a distinct constraint from "individually-itemized."

- **V-04** is the R15 V-05 form elevated to R16's primary full-pass variation. 4-item numbered checklist with explicit labels ("Named target 1 — manifest TOKEN-propagation column:", "Named target 2 — GATE-0's REQUIRED OUTPUTS table:", "Verbatim phrase 1 — 'Declaration site':", "Verbatim phrase 2 — 'Substitution/inheritance site':") — completeness verifiable by item count (4) and by label scan. C-43 PASS. C-42 PASS. All other criteria active at their R15 V-05 level.

- **V-05** adds a structural count declaration above the checklist: a `C-43 COMPLIANCE — 4 ITEMS` bold header that pre-declares the count before any item is read. This makes the 4-element requirement machine-verifiable from the header alone — a reader need not count items to confirm the block satisfies C-43. Tests whether explicit count pre-declaration increases model-compliance reliability vs V-04's count-from-items approach, and whether the added header creates any regression risk on adjacent criteria.

**Three decisive questions:**
1. Do V-01, V-02, and V-03 all score identically at 34/35 = 99.714, confirming that prose, 3-item partial checklist, and 4-item unlabeled bullets are all C-43 failures regardless of how close they come to the criterion's structural form?
2. Does the rubric distinguish V-02 (count failure: 3 items when 4 required) from V-03 (label failure: 4 items, unlabeled) as two distinct failure modes within C-43's "explicitly labeled, individually-itemized" compound requirement?
3. Are V-04 and V-05 equivalent at 35/35, or does the explicit count pre-declaration in V-05 create a reliable advantage — or introduce overhead that risks structural confusion at adjacent criteria?

---

## V-01 — C-43 Failure: Prose Architecture Block (R15 V-04 Form)

**Axis:** Architecture block uses a prose paragraph that contains all four C-42 elements — both artifact names ("the manifest TOKEN-propagation column," "GATE-0's REQUIRED OUTPUTS table") and both verbatim phrases ("Declaration site," "Substitution/inheritance site") — but presents them as flowing prose rather than individually-itemized checklist entries. C-42 PASS (all four elements present and readable from the block without consulting any other artifact). C-43 FAIL (no checklist structure; a reader cannot verify completeness by item count — must parse prose to confirm all four elements are present). All other criteria identical to R15 V-05: dedicated propagation row (C-40), dual-layer independence (C-36), triple-mechanism manifest hardening (C-37), C-41 PASS, full AMEND schema (C-20 through C-22).
**Hypothesis:** C-42 PASS — operative test: (1) "the manifest TOKEN-propagation column" named, (2) "GATE-0's REQUIRED OUTPUTS table" named, (3) "Declaration site" verbatim, (4) "Substitution/inheritance site" verbatim — all four readable from the prose block. C-43 FAIL — operative test: four elements as explicitly labeled, individually-itemized checklist entries — prose paragraph fails structurally regardless of content completeness. All 34 R15 criteria: PASS. C-43: FAIL. Aspirational: 34/35. Composite: 99.714. Decisive question: does the rubric score C-43 as 0 on the basis of structural form alone (prose vs checklist), or does prose with clearly enumerable sentences satisfy the "individually-itemized" requirement?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This propagation contract is independently declared in two structural artifacts: (1) **the manifest TOKEN-propagation column** — the `[TOKEN] propagation` column in the EXECUTION PLAN table, where GATE-0 is labeled "Declaration site" and GATE-1+ are labeled "Substitution/inheritance site"; and (2) **GATE-0's REQUIRED OUTPUTS table** — the dedicated Propagation contract row, which independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, and states the full substitution rule without referencing the manifest column. Neither artifact is load-bearing for the other: a reader consulting only the manifest TOKEN-propagation column can reconstruct the complete contract; a reader consulting only GATE-0's REQUIRED OUTPUTS Propagation contract row can also reconstruct the complete contract independently. Both artifacts are targets of this architecture block.

GATE-0 is the Declaration site: TOKEN is committed to a domain-adaptive identifier in this gate. GATE-0's own REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed. The committed value substitutes `[TOKEN]` in all GATE-1 through GATE-4 REQUIRED OUTPUTS column headers and in the `[TOKEN] propagation` manifest column header. GATE-1 through GATE-4 are Substitution/inheritance sites: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution. A reader consulting only this architecture block can reconstruct the full propagation contract — Declaration site, Substitution/inheritance sites, and substitution rule — without consulting the manifest or per-gate tables.

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
| C0 section before any competitor row: `## C0 -- [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

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
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [connection -- committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism -- committed TOKEN value]
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
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE -- [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |

---

## V-02 — C-43 Failure: 3-Item Partial Checklist (Item Count = 3, Element 4 Collapsed)

**Axis:** Architecture block uses a numbered checklist, but with 3 items instead of 4. Items 1 and 2 carry the two artifact names. Item 3 carries "Declaration site" verbatim. The fourth C-42 element — "Substitution/inheritance site" verbatim — is embedded in item 1's prose description rather than occupying a dedicated fourth item. C-42 PASS (all four elements present and readable; "Substitution/inheritance site" appears in item 1's content). C-43 FAIL (count = 3 items; a reader verifying completeness by item count finds only 3; must parse item 1's prose to locate the fourth element). All other criteria identical to V-01 / R15 V-05.
**Hypothesis:** C-42 PASS — all four elements readable from the block: item 1 names the manifest column AND includes "Substitution/inheritance site" verbatim in its content prose; item 2 names GATE-0's REQUIRED OUTPUTS table; item 3 supplies "Declaration site" verbatim. Operative test: all four elements confirmable without consulting other artifacts. C-43 FAIL — only 3 items separately itemized; "Substitution/inheritance site" survives only by parsing item 1's content, not as a standalone item. Count-verification fails at 3. All 34 R15 criteria: PASS. Aspirational: 34/35. Composite: 99.714. Decisive question: does the rubric enforce item count (exactly 4 separately-itemized entries) as the primary C-43 test, correctly scoring FAIL when the fourth element is embedded in an existing item's prose?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract. A reader consulting only this block can confirm all four required C-42 elements without consulting any other artifact:

1. **Named target 1 — manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it by substitution, and what substitution rule applies.

2. **Named target 2 — GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as the inheritance sites where the committed TOKEN value substitutes `[TOKEN]` in all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row.

3. **Verbatim phrase — "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed. The committed value then propagates to all downstream gates, which are the Substitution/inheritance sites where each REQUIRED OUTPUTS column header carries the committed identifier.

Neither artifact (named target 1 or named target 2) is load-bearing for the other. Both are independently self-contained. A reader consulting only this block can reconstruct the full propagation contract with zero inference steps.

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
| C0 section before any competitor row: `## C0 -- [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

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
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [connection -- committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism -- committed TOKEN value]
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
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE -- [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |

---

## V-03 — C-43 Failure: 4 Unlabeled Bullet Points (Individually-Itemized but Not Explicitly Labeled)

**Axis:** Architecture block uses 4 bullet points, each carrying exactly one C-42 element — item count = 4, one element per item. But the bullets have no per-item label headers: no "Named target 1 —", no "Verbatim phrase 1 —", no structural identifier marking each bullet as a specific C-42 element type. C-42 PASS (all four elements present and readable; each bullet contains one element). C-43 FAIL — the "explicitly labeled" requirement is the failing condition; bullets are individually-itemized (count = 4, one element per item) but not explicitly labeled (no item label identifies which C-42 element each bullet carries). A reader must read each bullet's prose to determine which element it satisfies, rather than reading an item label. All other criteria identical to V-01 / R15 V-05.
**Hypothesis:** C-42 PASS — all four elements present in the block, individually discoverable by reading each bullet's prose. C-43 FAIL — "explicitly labeled" is distinct from "individually-itemized": unlabeled bullets satisfy the count and enumeration requirements but not the per-label identification requirement. Operative test: a reader cannot verify completeness by label scan (no labels to scan) — must read bullet content to confirm element identity. All 34 R15 criteria: PASS. Aspirational: 34/35. Composite: 99.714. Decisive question: does the rubric enforce "explicitly labeled" as a distinct test from individual itemization, or does one element per bullet (readable by prose) satisfy C-43 even without structural labels?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract. A reader consulting only this block can confirm all four required C-42 elements without consulting any other artifact:

- The `[TOKEN] propagation` column in the EXECUTION PLAN table (the manifest TOKEN-propagation column) independently carries the complete propagation contract: GATE-0's cell is labeled "Declaration site" and GATE-1+ cells are labeled "Substitution/inheritance site," so which gate declares TOKEN and which gates consume it is verifiable from the column alone without reading any other artifact.

- The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column — the row is structurally distinct from the TOKEN commitment row.

- "Declaration site" is the verbatim rubric-vocabulary term for the gate where TOKEN is committed. GATE-0 is the Declaration site. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed.

- "Substitution/inheritance site" is the verbatim rubric-vocabulary term for all gates where the committed TOKEN value substitutes `[TOKEN]` in REQUIRED OUTPUTS column headers. GATE-1 through GATE-4 are Substitution/inheritance sites: each gate's column header carries the committed TOKEN value by substitution, independently of any other gate.

Neither artifact (manifest column or GATE-0 REQUIRED OUTPUTS table) is load-bearing for the other. Both are targets of this architecture block.

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
| C0 section before any competitor row: `## C0 -- [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

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
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [connection -- committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism -- committed TOKEN value]
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
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE -- [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |

---

## V-04 — Full 35/35: Standard 4-Item Labeled Checklist (R15 V-05 Form)

**Axis:** Architecture block uses a 4-item numbered checklist with explicit per-item labels — the R15 V-05 structure promoted to R16's primary full-pass variation. Item labels: "Named target 1 — manifest TOKEN-propagation column," "Named target 2 — GATE-0's REQUIRED OUTPUTS table," "Verbatim phrase 1 — 'Declaration site'," "Verbatim phrase 2 — 'Substitution/inheritance site'" — mirroring C-42's operative-test phrasing so the block is self-documenting as a C-42 artifact. C-43 PASS: four elements, each in a dedicated explicitly-labeled item; completeness verifiable by item count (4) without parsing item prose. C-42 PASS. All other criteria at R15 V-05 level.
**Hypothesis:** C-43 PASS — four items, each explicitly labeled by element type; item count = 4 confirmable without reading item prose; label scan sufficient to verify all four C-42 elements are present and individually-itemized. C-42 PASS — operative test: all four elements independently readable from labeled items. C-40 PASS (dedicated propagation row). C-41 PASS (C-36+C-37). Aspirational: 35/35. Composite: 100.000. Decisive question for V-04 vs V-05: does explicit count pre-declaration (V-05's header) create any measurable compliance advantage, or is V-04's label-scan form sufficient?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract. A reader consulting only this block can confirm all four required elements of the maximal architecture block form without consulting any other artifact:

1. **Named target 1 — manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **Named target 2 — GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **Verbatim phrase 1 — "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **Verbatim phrase 2 — "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution — after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (named target 1 or named target 2) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only this block can reconstruct the full propagation contract — Declaration site, Substitution/inheritance sites, substitution rule, and both artifact names — with zero inference steps.

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
| C0 section before any competitor row: `## C0 -- [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

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
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [connection -- committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism -- committed TOKEN value]
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
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE -- [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |

---

## V-05 — Full 35/35: 4-Item Labeled Checklist with Structural Count Declaration

**Axis:** Architecture block uses the same 4-item labeled checklist as V-04 (R15 V-05 form), but adds a structural count declaration header before the items: **`C-43 COMPLIANCE -- 4 ITEMS`** in bold, followed by "The following four elements are enumerated as explicitly labeled, individually-itemized checklist entries:" The count (4) is pre-declared as a structural header — a reader verifies C-43 compliance from the header declaration alone, without counting items. C-43 PASS: labeled items + count pre-declared. C-42 PASS. Combined axis: labeled checklist form (V-04) + explicit count declaration header.
**Hypothesis:** C-43 PASS — structural count header "C-43 COMPLIANCE -- 4 ITEMS" pre-declares the exact count; four labeled items each carry one C-42 element; count verifiable from header alone; label scan confirms element-type mapping. C-42 PASS — all four elements present in the labeled items, each independently readable from its item label. C-40 PASS (dedicated propagation row). C-41 PASS (C-36+C-37). Aspirational: 35/35. Composite: 100.000. Decisive question: does the count-declaration header create any regression risk by adding non-standard structure before the 4-item list, or does it strengthen the block's C-43 reliability compared to V-04 without affecting other criteria?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**C-43 COMPLIANCE -- 4 ITEMS.** The following four elements are enumerated as explicitly labeled, individually-itemized checklist entries. Completeness is verifiable by item count (4) and by label scan without reading item prose:

1. **Named target 1 — manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **Named target 2 — GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **Verbatim phrase 1 — "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **Verbatim phrase 2 — "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution — after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (named target 1 or named target 2) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only this block can reconstruct the full propagation contract with zero inference steps.

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
| C0 section before any competitor row: `## C0 -- [name]` with `[TOKEN]: [mechanism type] -> [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| 3+ named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| 1+ inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

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
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [connection -- committed TOKEN value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism -- committed TOKEN value]
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
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE -- [verdict; committed TOKEN value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE -- [verdict; committed TOKEN] | [reasoning] |

---

## Composite Hypothesis Table

| Variation | C-43 mechanism | C-43 pred | All R15 pred | Asp pred | Composite pred |
|-----------|----------------|-----------|--------------|----------|----------------|
| **V-01** | Prose block — all four elements present in paragraph form; no individually-itemized checklist structure | FAIL | All 34 PASS | 34/35 | **99.714** |
| **V-02** | 3-item partial checklist — items 1+2 carry artifact names, item 3 carries "Declaration site"; "Substitution/inheritance site" embedded in item 1's content prose, not a separate item; count = 3 | FAIL | All 34 PASS | 34/35 | **99.714** |
| **V-03** | 4 unlabeled bullets — each carries exactly one C-42 element; count = 4; no per-item label headers; element identity requires reading item content | FAIL | All 34 PASS | 34/35 | **99.714** |
| **V-04** | 4-item labeled numbered list — item labels "Named target 1 --", "Named target 2 --", "Verbatim phrase 1 --", "Verbatim phrase 2 --"; count = 4; completeness verifiable by label scan | PASS | All 34 PASS | 35/35 | **100.000** |
| **V-05** | 4-item labeled list + count declaration header "C-43 COMPLIANCE -- 4 ITEMS" before items; count pre-declared; label scan + header both satisfy C-43 | PASS | All 34 PASS | 35/35 | **100.000** |

**Predicted ranking:** V-01 = V-02 = V-03 = 99.714 < V-04 = V-05 = 100.000

**Single criterion separates the field:** C-43 is the only varying criterion across all five variations. The three failure modes (V-01: prose, V-02: 3-item count, V-03: unlabeled bullets) all predict 34/35 at identical composite scores, testing whether the rubric enforces C-43 as a single atomic criterion rather than decomposing into sub-criteria for count vs labeling. If the scorecard assigns partial credit for V-03 (count = 4, label absent) above V-01 (no checklist structure at all), C-43 has implicit sub-structure — a finding that would inform R17 criterion splitting.

**C-43 failure mode taxonomy (diagnostic value):**
- V-01 failure = content-complete prose (C-42 PASS floor; C-43 form test)
- V-02 failure = element collapse (individually-itemized requirement violated; 3 of 4 elements as separate items)
- V-03 failure = label absence (explicitly-labeled requirement violated; 4 items present, no structural labels)

**V-04 vs V-05 secondary question:** If both score 35/35, the count-declaration header in V-05 is structurally redundant at the criterion level. Its value is model-compliance reliability across multiple independent runs — not single-run scoring. V-05's header makes the count a declared structural fact rather than an inferred count; if model drift is observed in later rounds (V-05 maintaining 35/35 while V-04 drifts to 34/35), the count-declaration is the differentiating mechanism.

**Three-failure-mode-same-score pattern:** All three failure variations scoring identically at 99.714 (0.286 pts below 100) is the expected outcome if C-43 is a single atomic criterion with no partial credit. If scorecards reveal differentiation within the three failure cases, R17 should consider whether C-43 should be split into C-43a (four elements individually-itemized) and C-43b (each item explicitly labeled), creating a dependency chain C-43a -> C-43b analogous to the C-42 -> C-43 chain established in R16.
