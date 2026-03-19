Here are the R20 variations — written to `simulations/quest/variations/discover-competitors-alt-variations-R20-2026-03-18.md`.

---

## R20 Summary

**Starting position:** R19 was 100.000 on all 5 variations — but against v18 (38 aspirational criteria). Rubric v19 adds C-47 and C-48, and all R19 variations score at best 99.750 against it.

**The gap:** C-47 and C-48 each require C-46 but are independent of each other:
- C-47 = annotation form declared in preamble (prose can do this, table doesn't if it lacks a form row)
- C-48 = preamble must be a native markdown table (prose fails this)

No R19 variation satisfies both simultaneously.

**R20 solution:** A **3-row bijective cardinality preamble table** — adding a third row that declares the element-index annotation form and maps its symbol set to the four-position index set. This is the minimal structural change that can satisfy both criteria at once.

---

### Variation axes

| # | Axis | Single/Combined | Primary test |
|---|------|-----------------|-------------|
| **V-01** | `(Element N)` + 3-row table | Single | Does table row 3 satisfy C-47? |
| **V-02** | Roman numeral `(i)–(iv)` + 3-row table | Single | Does Roman form in row 3 satisfy C-47 + C-45? |
| **V-03** | `(Ei)` + 3-row table + inertia-forward | Combined | C-47+C-48 stable under inertia framing? |
| **V-04** | `(Element N)` + 3-row table + compact items | Combined | C-42/C-38/C-39 survive item compression? |
| **V-05** | `(Ei)` + 3-row table + conversational register | Combined | C-47+C-48 stable across register shift? |

**The decisive question:** Does embedding the annotation form declaration as a table row satisfy C-47's "reading only the C-46 preamble" test — when the preamble IS the table? If yes, all 5 score 100.000. If no (C-47 requires a prose sentence), all 5 score 99.750 and the next round tests a hybrid (2-row C-48 table + prose annotation sentence + checklist).
form + maps to {i,ii,iii,iv} | Native table preamble | 100.000 |
| **V-03** | `(Ei)` + 3-row table + inertia-forward framing | Table row 3 names `(Ei)` form + maps to {E1,E2,E3,E4} | Native table preamble | 100.000 |
| **V-04** | `(Element N)` + 3-row table + compact architecture items | Table row 3 names `(Element N)` form; items compressed | Native table preamble | 100.000 |
| **V-05** | `(Ei)` + 3-row table + conversational register | Table row 3 names `(Ei)` form; Steps replace GATES | Native table preamble | 100.000 |

**Decisive question:** Does placing the annotation form declaration as a dedicated third row inside the bijective cardinality preamble table satisfy C-47's "explicitly names the annotation form being used — identifying the symbol set (...) and declaring its mapping to the four-position element-index set — as part of the cardinality constraint declaration"?

- **If yes:** All 5 variations score 100.000. The 3-row table is the canonical C-47+C-48 combined form.
- **If no:** C-47 requires annotation form to appear in a prose artifact, not a table row — failing all 5 at C-47. Score: 99.750. Next round would test whether a prose annotation declaration between the table and the first checklist item satisfies C-47 when the table satisfies C-48.

**Secondary question (V-02):** Does Roman numeral form `(i)–(iv)` satisfy C-45 when declared via table row 3 rather than prose preamble? R19 V-01 proved Roman numerals satisfy C-45 via prose declaration. V-02 tests whether the same mapping declared in a table row achieves the same result.

---

## V-01 — 3-Row Table Preamble: `(Element N)` Annotation Form

**Axis:** Single-axis C-47+C-48 combined. The bijective cardinality preamble block is a 3-row native markdown table. Row 1: Required item count (Exactly 4). Row 2: C-42 elements per item (Exactly 1). Row 3: Element-index annotation form (`(Element N)` prefix where N ∈ {1, 2, 3, 4} — symbol set maps to the four-position element-index set). No post-table prose before the first checklist item — the table is the complete preamble. Everything else unchanged from R19 V-02 (table preamble baseline). R19 V-02 used a 2-row table and satisfied C-46/C-48 but not C-47; V-01 adds row 3 to close C-47.

**Hypothesis:** C-47 PASS — table row 3 explicitly names the annotation form (`(Element N)`) and declares its mapping to the four-position set {1, 2, 3, 4}; "reading only the C-46 preamble, a reader can identify (1) the bijective cardinality constraint and (2) the annotation symbol set and its declared mapping to element positions {1,2,3,4}." C-48 PASS — native markdown table preamble (same form as R19 V-02). C-45 PASS — `(Element N)` annotation form proven in R18 and R19. C-46 PASS — table declares both cardinality conditions before first checklist item (extends R19 V-02 PASS; row 3 is additive, not replacive). All other criteria: same as R19 baseline (100.000 on v18). Predicted composite: **100.000**.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**BIJECTIVE CARDINALITY CONSTRAINT — declared before checklist begins:**

| Cardinality requirement | Declared value |
|-------------------------|----------------|
| Required item count | Exactly 4 — item count = element count; a checklist with fewer items is a self-identified violation of this declared architectural contract |
| C-42 elements per item | Exactly 1 — no item covers more than one C-42 element; no element is assigned to more than one item; bijective mapping enforced |
| Element-index annotation form | `(Element N)` prefix where N ∈ {1, 2, 3, 4} — symbol set maps directly to the four-position element-index set {1, 2, 3, 4}; reading only the four item annotations confirms each position appearing exactly once; bijective assignment verifiable from annotations alone without reading item body content |

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

## V-02 — 3-Row Table Preamble: Roman Numeral Annotation Form

**Axis:** Single-axis C-47+C-48 combined, Roman numeral variant. Architecture block preamble is a 3-row native markdown table. Row 3 declares: Roman numeral form `(i)`, `(ii)`, `(iii)`, `(iv)` — forming a unified {i, ii, iii, iv} four-position index set. Checklist items use `(i)` through `(iv)` annotations. Everything else unchanged from V-01. Tests whether Roman numeral form declared via table row (rather than prose) satisfies both C-47 (annotation form named and mapped) and C-45 (element-index annotations "or equivalent").

**Hypothesis:** C-47 PASS — table row 3 names the Roman numeral symbol set {i, ii, iii, iv} and declares its mapping to the four-position element-index set; the "reading only the C-46 preamble" test is satisfied because the preamble IS the table and row 3 is within it. C-48 PASS — native markdown table preamble. C-45 PASS — R19 V-01 established Roman numeral `(i)–(iv)` satisfies "or equivalent" when the preamble declares the four-position mapping; the table row performs the same declaration. C-46 PASS — table rows commit both cardinality conditions before checklist. All 40 aspirational criteria: PASS. Predicted composite: **100.000**.

**Secondary question:** R19 V-01 proved Roman numerals satisfy C-45 via prose preamble declaration. Does the same mapping declared as a table row (row 3) achieve identical C-45 pass? C-47 requires "reading only the C-46 preamble" — if the preamble is the table, then row 3 IS part of the preamble; C-47 PASS. If C-47 requires a prose sentence specifically, row 3 form might fail even though the content is equivalent.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**BIJECTIVE CARDINALITY CONSTRAINT — declared before checklist begins:**

| Cardinality requirement | Declared value |
|-------------------------|----------------|
| Required item count | Exactly 4 — item count = element count; a checklist with fewer items is a self-identified violation of this declared architectural contract |
| C-42 elements per item | Exactly 1 — no item covers more than one C-42 element; no element is assigned to more than one item; bijective mapping enforced |
| Element-index annotation form | Roman numeral form `(i)`, `(ii)`, `(iii)`, `(iv)` — forming a unified {i, ii, iii, iv} four-position index set; symbol set maps directly to element positions {1, 2, 3, 4}; reading only the four item annotations confirms each position appearing exactly once; bijective assignment verifiable from annotations alone without reading item body content |

1. **(i) Named target — manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **(ii) Named target — GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **(iii) Verbatim phrase — "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **(iv) Verbatim phrase — "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution — after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (i) nor (ii) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only this block can reconstruct the full propagation contract — Declaration site, Substitution/inheritance sites, substitution rule, and both artifact names — with zero inference steps and zero cross-artifact lookups.

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

## V-03 — `(Ei)` Annotations + 3-Row Table + Inertia-Forward Framing

**Axis:** Combined — annotation style (`(Ei)`) + 3-row table preamble + inertia-forward framing. Row 3 declares `(Ei)` abbreviated form. Opening instruction names TOKEN as the primary inertia anchor. GATE-2 positions C0 mechanism as the reference frame before competitors. GATE-3 templates lead with `vs [TOKEN]:` as the first line of each finding. GATE-4 AMEND schema describes Stability verdict as the primary criterion. Adapts R19 V-03 (proven 100.000 inertia framing) with the 3-row table preamble replacing its prose BIJECTIVE CARDINALITY CONSTRAINT block.

**Hypothesis:** C-47 PASS — table row 3 names `(Ei)` abbreviated form and maps {E1, E2, E3, E4} to the four-position element-index set. C-48 PASS — native markdown table. C-45 PASS — `(Ei)` form proven equivalent in R18 and R19 (R18 first pass, R19 V-05 confirmed). Inertia-forward framing: strengthens C-11 (TOKEN propagates downstream — `vs [TOKEN]:` leads every finding), C-12/C-14 (AMEND evaluates TOKEN stability — primary criterion emphasis), C-16 (stability verdict with evidence — independence reinforced). No regressions expected. All 40 aspirational criteria: PASS. Predicted composite: **100.000**.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. The inertia competitor (C0, the current solution) is assessed first in every gate; TOKEN names its lock-in mechanism and propagates through all downstream gates as the primary analysis anchor. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**BIJECTIVE CARDINALITY CONSTRAINT — declared before checklist begins:**

| Cardinality requirement | Declared value |
|-------------------------|----------------|
| Required item count | Exactly 4 — item count = element count; a checklist with fewer items is a self-identified violation of this declared architectural contract |
| C-42 elements per item | Exactly 1 — no item covers more than one C-42 element; no element is assigned to more than one item; bijective mapping enforced |
| Element-index annotation form | Abbreviated `(Ei)` form where i ∈ {1, 2, 3, 4} — symbol set {E1, E2, E3, E4} maps directly to the four-position element-index set; reading only the four item annotations `(E1)`, `(E2)`, `(E3)`, `(E4)` confirms each position appearing exactly once; bijective assignment verifiable from annotations alone without reading item body content |

1. **(E1) Named target — manifest TOKEN-propagation column:** The `[TOKEN] propagation` column in the EXECUTION PLAN table. GATE-0's row cell is labeled "Declaration site." GATE-1+ row cells are labeled "Substitution/inheritance site." This column independently carries the complete propagation contract: which gate declares TOKEN, which gates consume it, and what substitution rule applies.

2. **(E2) Named target — GATE-0's REQUIRED OUTPUTS table (Propagation contract row):** The dedicated Propagation contract row in GATE-0's REQUIRED OUTPUTS table. This row independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, states the committed-value substitution rule for all downstream REQUIRED OUTPUTS column headers, and does not reference the manifest column. The row is structurally distinct from the TOKEN commitment row and carries only the propagation contract.

3. **(E3) Verbatim phrase — "Declaration site":** GATE-0 is the Declaration site. TOKEN is committed in this gate. GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed.

4. **(E4) Verbatim phrase — "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites. Each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution — after GATE-0 declares TOKEN, every downstream REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier.

Neither artifact (E1 or E2) is load-bearing for the other. Both are targets of this architecture block. A reader consulting only this block can reconstruct the full propagation contract — Declaration site, Substitution/inheritance sites, substitution rule, and both artifact names — with zero inference steps and zero cross-artifact lookups.

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

TOKEN is the organizing lens for all findings. Start each finding with the TOKEN reference — what does the named competitor's position mean for the inertia mechanism? Reference named competitor rows by their table labels. Whitespace requires a specific named uncontested dimension.

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

## V-04 — `(Element N)` + 3-Row Table + Compact Architecture Block Items

**Axis:** Combined — 3-row table preamble (C-47+C-48) + compact single-sentence architecture block items. Adapts R19 V-04 (compact items, proven 100.000) with the 3-row table preamble. Each of the four checklist items is compressed to a single sentence while preserving all four C-42 required elements: both artifact names (manifest column, GATE-0 REQUIRED OUTPUTS table) and both verbatim phrases ("Declaration site," "Substitution/inheritance site"). `(Element N)` annotations retained. Risk: compression of items might reduce redundancy that supports C-38 (both targets named) or C-39 (verbatim phrases present); each is mitigated by explicit preservation in the compressed form.

**Hypothesis:** C-47 PASS — table row 3 declares `(Element N)` form and maps to {1,2,3,4}. C-48 PASS — native table. C-44 PASS — 4 items, one element each. C-45 PASS — `(Element N)` annotations. C-46 PASS — 3-row table is the preamble. C-38 PASS — compact items still name manifest column (E1) and GATE-0 REQUIRED OUTPUTS table (E2). C-39 PASS — compact items still contain "Declaration site" (E3) and "Substitution/inheritance site" (E4) verbatim. C-42 PASS — all four elements readable without consulting other artifacts. All 40: PASS. Predicted composite: **100.000**.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This block is the declared primer for two independent structural artifacts that carry the propagation contract.

**BIJECTIVE CARDINALITY CONSTRAINT — declared before checklist begins:**

| Cardinality requirement | Declared value |
|-------------------------|----------------|
| Required item count | Exactly 4 — item count = element count; fewer items = self-identified violation |
| C-42 elements per item | Exactly 1 — bijective mapping; no item covers more than one element |
| Element-index annotation form | `(Element N)` prefix where N ∈ {1, 2, 3, 4} — symbol set maps to four-position index set {1, 2, 3, 4}; reading the four annotations confirms each position exactly once; bijection annotation-verifiable without reading item content |

Each item carries an explicit `(Element N)` annotation as a structurally distinct item header prefix:

1. **(Element 1) Named target — manifest `[TOKEN] propagation` column:** GATE-0 cell labeled "Declaration site"; GATE-1+ cells labeled "Substitution/inheritance site"; column is independently complete — carries full propagation contract without referencing GATE-0's REQUIRED OUTPUTS table.

2. **(Element 2) Named target — GATE-0 REQUIRED OUTPUTS table (Propagation contract row):** Dedicated row names GATE-0 as Declaration site and GATE-1+ as Substitution/inheritance sites; states substitution rule for all downstream REQUIRED OUTPUTS column headers; does not reference the manifest column; structurally distinct from TOKEN commitment row.

3. **(Element 3) Verbatim phrase — "Declaration site":** GATE-0 is the Declaration site; TOKEN committed in GATE-0; GATE-0's REQUIRED OUTPUTS table retains `[TOKEN] required?` column header — template form preserved so substitution rule is explicit rather than already consumed.

4. **(Element 4) Verbatim phrase — "Substitution/inheritance site":** GATE-1 through GATE-4 are Substitution/inheritance sites; each gate's REQUIRED OUTPUTS column header replaces `[TOKEN]` with the committed identifier after GATE-0 declares TOKEN.

Neither artifact (Element 1 or Element 2) is load-bearing for the other. Both are named targets of this architecture block. A reader consulting only this block identifies all four C-42 elements without consulting any other artifact.

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

## V-05 — `(Ei)` + 3-Row Table + Conversational Register

**Axis:** Combined — `(Ei)` annotations + 3-row table preamble + full conversational register. Steps replace GATE labels; instructions phrased as direct guidance rather than formal specifications; overall tone is less technical. All structural elements preserved: REQUIRED OUTPUTS tables remain native markdown tables, Step Manifest remains a native markdown table, TOKEN-PROPAGATION ARCHITECTURE retains all four C-42 elements, the 3-row preamble table explicitly declares all three cardinality conditions (item count, elements per item, annotation form), AMEND component names kept domain-neutral (C-22 risk mitigated explicitly). Adapts R19 V-05 (conversational register, proven 100.000) with the 3-row table preamble replacing its prose bijective contract block.

**Hypothesis:** C-47 PASS — table row 3 names `(Ei)` abbreviated form and maps {E1, E2, E3, E4} to four-position index set. C-48 PASS — native markdown table. C-45 PASS — `(Ei)` proven equivalent (R18 first pass, R19 V-05 confirmed). C-21 PASS — "unconditional" keyword retained in conversational form; Step 1 named as first conditional. C-22 PASS — AMEND component names explicitly kept domain-neutral (Input change, Output effect, Stability verdict, Evidence). C-24 PASS — Step Manifest retains native markdown. C-28 PASS — REQUIRED OUTPUTS tables retained. Architecture block retains "Declaration site" and "Substitution/inheritance site" verbatim in conversational prose. All 40: PASS. Predicted composite: **100.000**.

---

Use this skill to map the competitive landscape for your current project. If you've provided a focus dimension (market sizing, positioning framework, competitive positioning angle), it gets woven into the analysis — not appended at the end. Figure out the domain, likely competitors, and market from the repo; don't ask the user. Each step produces specific outputs; complete the steps in order.

**How TOKEN substitution works:** Step 0 commits a domain-specific TOKEN identifier. From Step 1 onward, every REQUIRED OUTPUTS table column that tracks TOKEN requirements uses the committed value instead of `[TOKEN]` — e.g., if TOKEN = SIGNAL-LOCK, Steps 1-4 produce `SIGNAL-LOCK required?` as their column header. The `[TOKEN] propagation` column in the Step Manifest header also substitutes the committed value. Step 0's own REQUIRED OUTPUTS column keeps `[TOKEN] required?` — the Propagation contract row in Step 0's table explains why.

**TOKEN-PROPAGATION ARCHITECTURE**

This block primes two independent structural artifacts that carry the propagation contract. Either artifact independently tells you which step declares TOKEN and which steps inherit it.

**BIJECTIVE CARDINALITY CONSTRAINT — declared before checklist begins:**

| Cardinality requirement | Declared value |
|-------------------------|----------------|
| Required item count | Exactly 4 — item count = element count; a checklist with fewer items is a self-identified violation of this declared contract |
| C-42 elements per item | Exactly 1 — no item covers more than one element; bijective mapping; a checklist item that bundles two elements violates this contract |
| Element-index annotation form | Abbreviated `(Ei)` form where i ∈ {1, 2, 3, 4} — symbol set {E1, E2, E3, E4} maps to the four-position element-index set; reading only the four item annotations `(E1)`, `(E2)`, `(E3)`, `(E4)` confirms each position appearing exactly once; bijective assignment verifiable from annotations alone |

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

| Variation | C-47 mechanism | C-47 pred | C-48 mechanism | C-48 pred | Asp pred (40) | Composite pred |
|-----------|---------------|-----------|---------------|-----------|---------------|----------------|
| **V-01** | Table row 3: `(Element N)` form, N ∈ {1,2,3,4}, mapped to four-position set | PASS | 3-row native table preamble | PASS | 40/40 | **100.000** |
| **V-02** | Table row 3: Roman numeral `(i)–(iv)`, mapped to {i,ii,iii,iv} | PASS | 3-row native table preamble | PASS | 40/40 | **100.000** |
| **V-03** | Table row 3: `(Ei)` form, i ∈ {1,2,3,4}, mapped to {E1,E2,E3,E4} | PASS | 3-row native table preamble | PASS | 40/40 | **100.000** |
| **V-04** | Table row 3: `(Element N)` form; compact items preserve C-38/C-39/C-42 | PASS | 3-row native table preamble | PASS | 40/40 | **100.000** |
| **V-05** | Table row 3: `(Ei)` form in conversational preamble table | PASS | 3-row native table preamble | PASS | 40/40 | **100.000** |

**Decisive question:** Does table row 3 in the bijective cardinality preamble satisfy C-47's content requirement — "explicitly names the annotation form being used — identifying the symbol set (...) and declaring its mapping to the four-position element-index set"? C-47 tests content; C-48 tests form. A table row IS content. The "reading only the C-46 preamble" operative test is satisfied if the preamble is the table — row 3 is within the preamble and is readable without consulting the checklist items.

**C-47 failure mode (if row 3 fails):** The rubric's operative test for C-47 says "reading only the C-46 preamble." If the rubric interprets the C-46 preamble as only the bijective cardinality content (item count + elements per item) and treats annotation form as requiring a separate prose sentence, then row 3 satisfies C-46's conditions but not C-47's extension. A C-47 FAIL for all 5 variations would establish that annotation form declaration requires a prose artifact outside the cardinality table — the next round would test a hybrid form (2-row C-48 table + 1 prose sentence for C-47 + checklist).

**C-47/C-48 co-satisfiability conclusion (if all pass):** The 3-row table is the canonical combined form. Any annotation style (Element N, Roman numeral, Ei) embedded as table row 3 simultaneously satisfies C-47 (annotation form declared within preamble) and C-48 (preamble is a native table). The annotation form declaration is a table content property, not a prose-form requirement.

**R19 retroactive score against v19 rubric:**

| R19 Variation | C-47 (v19) | C-48 (v19) | v19 Score |
|---------------|------------|------------|-----------|
| V-01 (Roman, prose preamble) | PASS — prose names `(i)–(iv)` form | FAIL — prose, not table | 99.750 |
| V-02 (Element N, table preamble) | FAIL — table rows omit annotation form | PASS — native table | 99.750 |
| V-03 (Element N, prose preamble, inertia) | FAIL — prose preamble has no annotation form | FAIL — prose, not table | 99.500 |
| V-04 (Element N, prose preamble, compact) | FAIL — prose preamble has no annotation form | FAIL — prose, not table | 99.500 |
| V-05 (Ei, prose preamble, conversational) | PASS — prose names `(Ei)` form | FAIL — prose, not table | 99.750 |
