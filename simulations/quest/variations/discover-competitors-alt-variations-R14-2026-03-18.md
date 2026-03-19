Written to `simulations/quest/variations/discover-competitors-alt-variations-R14-2026-03-18.md`.

---

## R14 Variations — Summary

**Baseline situation:** R13 V-05 scored 100 (28/28 aspirational) under the old rubric. Under R14 (31 aspirational criteria), it scores **30/31** — it passes C-37 and C-39 automatically, but **fails C-38** because its architecture block never explicitly names "the manifest TOKEN-propagation column" as a target artifact by label.

**Three new separating axes:**

| # | Axis | C-36 | C-37 | C-38 | C-39 | Asp | Composite pred |
|---|------|------|------|------|------|-----|----------------|
| V-01 | C-37 isolation — R13 V-04 structure (compact Yes-cell), verbatim vocab in block | FAIL | PASS | FAIL (dep) | PASS | 29/31 | **99.355** |
| V-02 | C-38 isolation — explicit dual-target naming, synonyms in block | PASS | PASS | PASS | FAIL | 30/31 | **99.677** |
| V-03 | C-39 isolation — verbatim vocab in block, no explicit dual-target naming | PASS | PASS | FAIL | PASS | 30/31 | **99.677** |
| V-04 | C-38 + C-39 — explicit dual-target + verbatim vocab (prose form) | PASS | PASS | PASS | PASS | 31/31 | **100.000** |
| V-05 | All new + structured mini-table dual-target declaration | PASS | PASS | PASS | PASS | 31/31 | **100.000** |

**Key design decisions:**

- **V-01** uses R13 V-04 structure (compact Yes-cell, no dedicated propagation row) — C-36 FAIL, so C-38 is blocked by its dependency chain. Tests whether C-37 produces a visible 0.323-pt separation from 30/31 variations.

- **V-02** introduces the critical new addition for C-38: architecture block explicitly names **"the manifest TOKEN-propagation column"** and **"GATE-0's REQUIRED OUTPUTS table"** by label, so a reader consulting only the block knows which specific structural artifacts carry the contract. Uses synonyms ("declaring gate" / "consuming gates") to keep C-39 failing cleanly.

- **V-03** is the R13 V-05 architecture block form — verbatim vocabulary throughout ("Declaration site" / "Substitution/inheritance site"), dedicated propagation row, but no explicit artifact-name targets. C-38 FAIL, C-39 PASS.

- **V-04** combines both: explicit artifact names AND verbatim vocabulary in the same prose paragraph. First variation predicted to reach 31/31.

- **V-05** uses a structured native markdown mini-table in the architecture block to enumerate both target artifacts as table rows (output format axis), then follows with verbatim vocabulary prose. Tests whether format affects C-38 compliance.

**Three decisive questions:**
1. V-01: Does the 0.323-pt C-37 margin produce visible scorecard separation?
2. V-02 vs V-03: Are C-38 and C-39 symmetric orthogonal axes at equal composite weight?
3. V-04 vs V-05: Does the mini-table format of dual-target declaration produce stronger or different C-38 compliance than prose form?
S | PASS | PASS | PASS | 31/31 | 100.000 |

**Three decisive questions:**
1. **V-01** — Does C-37 scoring produce any visible composite separation when C-36 fails and C-38 is blocked by its dep? (0.323 pts margin between 29/31 and 30/31)
2. **V-02 vs V-03** — Do explicit dual-target naming (C-38) and verbatim vocabulary co-registration (C-39) produce the same compliance pattern, or does one axis generate model failures the other does not?
3. **V-04 vs V-05** — Does the structured mini-table format in the architecture block achieve stronger C-38 compliance than the prose form, or are both equivalent?

---

## V-01 — C-37: Triple-Mechanism Hardening Isolation, Compact Independence

**Axis:** R13 V-04 structure — C-33 (verbatim manifest cells), C-34 (architecture block), and C-35 (bracket-notation manifest header) all simultaneously present, forming the complete triple-mechanism hardening stack (C-37). Architecture block uses "Declaration site" and "Substitution/inheritance site" verbatim (so C-39 also passes). GATE-0 REQUIRED OUTPUTS uses the compact Yes-cell form — no dedicated propagation row — so C-36 FAIL, and by dependency chain C-38 is scored 0.
**Hypothesis:** C-37 PASS — all three manifest hardening mechanisms simultaneously active; triple-mechanism stack complete with no gaps. C-36 FAIL (compact Yes-cell insufficient for independence test). C-38 FAIL (C-36 dep fails, scored 0). C-39 PASS (C-33 PASS, C-34 PASS, architecture block uses both verbatim terms). Aspirational: 29/31 = 99.355. Decisive question: does the 0.323-pt difference between 29/31 and 30/31 produce a visible composite separation in the scorecard?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the TOKEN row Yes-cell declares the propagation contract.

**TOKEN-PROPAGATION ARCHITECTURE**

GATE-0 is the Declaration site: TOKEN is committed to a domain-adaptive identifier in this gate. GATE-0's own REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed. The committed value substitutes `[TOKEN]` in all GATE-1 through GATE-4 REQUIRED OUTPUTS column headers and in the `[TOKEN] propagation` manifest column header. GATE-1 through GATE-4 are Substitution/inheritance sites: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution. TOKEN carry-forward is a required output element for every gate after GATE-0. A reader consulting this block can reconstruct the full propagation contract — Declaration site, Substitution/inheritance sites, and substitution rule — without consulting the manifest or per-gate tables.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers and in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward active |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. `[TOKEN] propagation` in the manifest column header substitutes to the committed value after GATE-0 commits. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers and in the manifest `[TOKEN] propagation` column header** |

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
| `FOCUS: ACTIVE — [dimension] \| INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — committed TOKEN value confirmed as active inertia reference | **Yes — committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] → [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| ≥3 named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| ≥1 inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — "Inertia is high" or generic category label fails. Run a WebSearch to verify at least one competitor claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior — not a generic category label]
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
| ≥3 findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding — specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes — committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) — gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows — findings readable without the competitive map fail. Specific whitespace dimension required; "room to innovate" alone fails.

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
| ≥3 AMEND data rows — all four cells filled per row | No |
| Stability verdict cells — STABLE / UNSTABLE + committed TOKEN value | **Yes — committed TOKEN in every Stability verdict cell** |
| Evidence cells — reasoning distinct from verdict text; "Stable." alone fails | No |

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

## V-02 — C-38: Explicit Dual-Target Naming, Synonym Vocabulary

**Axis:** Architecture block explicitly names both "the manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" as the specific downstream artifacts carrying the propagation contract — the operative test for C-38. But the block uses synonyms ("declaring gate" / "consuming gates") rather than rubric-vocabulary verbatim, so C-39 FAIL. GATE-0 REQUIRED OUTPUTS uses the dedicated propagation row (R13 V-05 form) — C-36 PASS. Manifest cells use verbatim vocabulary (C-33 PASS). Manifest header bracket notation (C-35 PASS). Architecture block present (C-34 PASS).
**Hypothesis:** C-37 PASS (C-33+C-34+C-35 simultaneously active). C-38 PASS — architecture block explicitly names both artifacts by label; a reader consulting only the block can identify the manifest TOKEN-propagation column and GATE-0's REQUIRED OUTPUTS table as the specific structural targets. C-39 FAIL — "declaring gate" and "consuming gates" are synonyms, not the verbatim terms "Declaration site" / "Substitution/inheritance site." C-36 PASS (dedicated propagation row independently self-contained). Aspirational: 30/31 = 99.677. Decisive question: does naming both target artifacts by label (without verbatim vocabulary) satisfy C-38's operative test? If yes, V-02 and V-03 score the same (30/31) and the two axes are symmetric. If no, C-38 requires both explicit naming AND something else.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This propagation contract is independently carried by two structural artifacts: (1) **the manifest TOKEN-propagation column** — the `[TOKEN] propagation` column in the EXECUTION PLAN table, where each row's cell identifies whether that gate is the declaring gate or a consuming gate — and (2) **GATE-0's REQUIRED OUTPUTS table** — specifically the Propagation contract row, which independently states the declaring gate, the consuming gates, and the substitution rule. Neither artifact is load-bearing for the other: a reader consulting only the manifest TOKEN-propagation column can reconstruct the full contract; a reader consulting only GATE-0's REQUIRED OUTPUTS table can also reconstruct the full contract.

GATE-0 is the declaring gate: TOKEN is committed to a domain-adaptive identifier here. GATE-0's own REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved. The committed value substitutes `[TOKEN]` in all GATE-1 through GATE-4 REQUIRED OUTPUTS column headers and in the `[TOKEN] propagation` manifest column header. GATE-1 through GATE-4 are consuming/inheritance gates: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution. A reader consulting only this architecture block — or only the manifest TOKEN-propagation column — or only GATE-0's REQUIRED OUTPUTS table — can independently reconstruct the full contract.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
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
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — TOKEN committed in this gate; GATE-0 is the declaring gate** |
| Propagation contract — GATE-0 is the declaring gate: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK → GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are consuming/inheritance gates — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest | **Contract — self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

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
| `FOCUS: ACTIVE — [dimension] \| INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes — committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] → [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| ≥3 named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| ≥1 inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior — not a generic category label]
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
| ≥3 findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
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
| ≥3 AMEND data rows — all four cells filled per row | No |
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

## V-03 — C-39: Verbatim Vocabulary Co-Registration, No Explicit Dual-Target

**Axis:** Architecture block uses "Declaration site" and "Substitution/inheritance site" verbatim in its plain-prose description — co-registering block vocabulary with manifest column cell vocabulary (C-39). But the block does NOT explicitly name "the manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" as target artifacts by those labels — a reader consulting only the block can reconstruct the full contract but cannot identify which specific named artifacts carry it. This is the R13 V-05 architecture block form with clearer verbatim vocabulary emphasis. C-38 FAIL (no explicit dual-target artifact naming). GATE-0 REQUIRED OUTPUTS uses dedicated propagation row (C-36 PASS).
**Hypothesis:** C-37 PASS (all three mechanisms simultaneously active). C-38 FAIL — architecture block describes the propagation contract completely but does not identify the manifest TOKEN-propagation column and GATE-0's REQUIRED OUTPUTS table as named structural targets; a reader consulting the block knows the contract but not which artifacts to consult. C-39 PASS — "Declaration site" and "Substitution/inheritance site" appear verbatim; same vocabulary scan that confirms C-33 manifest cells applies to block prose with zero translation step. Aspirational: 30/31 = 99.677. Decisive question: is the vocabulary co-registration between architecture block and manifest cells sufficient to demonstrate C-39, or does the rubric require additional priming?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

GATE-0 is the Declaration site: TOKEN is committed to a domain-adaptive identifier in this gate. GATE-0's own REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed — and carries a dedicated Propagation contract row that names GATE-0 as the Declaration site and GATE-1+ as Substitution/inheritance sites, with the full substitution rule stated explicitly. A reader consulting only GATE-0's REQUIRED OUTPUTS table can reconstruct the full propagation contract without reading the manifest. GATE-1 through GATE-4 are Substitution/inheritance sites: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution. TOKEN carry-forward is a required output element for every gate after GATE-0. A reader consulting only this architecture block can also reconstruct the full propagation contract — Declaration site, Substitution/inheritance sites, and substitution rule — without reading either the manifest or per-gate tables.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
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
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract — GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK → GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest | **Contract — self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

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
| `FOCUS: ACTIVE — [dimension] \| INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes — committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] → [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| ≥3 named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| ≥1 inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior — not a generic category label]
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
| ≥3 findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
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
| ≥3 AMEND data rows — all four cells filled per row | No |
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

## V-04 — C-38 + C-39: Explicit Dual-Target + Verbatim Vocabulary

**Axis:** Architecture block satisfies both C-38 and C-39 simultaneously: (1) explicitly names "the manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" as target artifacts (C-38), and (2) uses "Declaration site" and "Substitution/inheritance site" verbatim in the same prose, co-registering block vocabulary with manifest cell vocabulary (C-39). The two requirements combine in a single architecture block paragraph — the explicit artifact names and the verbatim vocabulary appear in the same sentences. GATE-0 REQUIRED OUTPUTS uses the dedicated propagation row (C-36 PASS). All three manifest hardening mechanisms active (C-37 PASS). This is the first variation to reach 31/31 aspirational.
**Hypothesis:** C-37 PASS (triple-mechanism stack: verbatim cells + architecture block + bracket header simultaneously). C-38 PASS — architecture block explicitly names both "the manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" as the specific structural artifacts that carry the propagation contract; a reader consulting only the block can identify both by label. C-39 PASS — architecture block prose uses "Declaration site" and "Substitution/inheritance site" verbatim, forming a closed vocabulary ring with C-33 manifest cells: same terms in both artifacts, zero translation step. C-36 PASS (dedicated propagation row independently self-contained). Aspirational: 31/31 = 100.000. Decisive question for V-04 vs V-05: does prose-form dual-target naming achieve the same C-38 compliance as V-05's structured mini-table form?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This propagation contract is independently declared in two structural artifacts: (1) **the manifest TOKEN-propagation column** — the `[TOKEN] propagation` column in the EXECUTION PLAN table, where GATE-0 is labeled "Declaration site" and GATE-1+ are labeled "Substitution/inheritance site"; and (2) **GATE-0's REQUIRED OUTPUTS table** — the dedicated Propagation contract row, which independently names GATE-0 as the Declaration site, names GATE-1+ as Substitution/inheritance sites, and states the substitution rule in full. Each artifact independently carries the complete propagation contract without referencing the other.

GATE-0 is the Declaration site: TOKEN is committed to a domain-adaptive identifier here. GATE-0's own REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed. The committed value substitutes `[TOKEN]` in all GATE-1 through GATE-4 REQUIRED OUTPUTS column headers and in the `[TOKEN] propagation` manifest column header. GATE-1 through GATE-4 are Substitution/inheritance sites: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution. A reader consulting only this architecture block — or only the manifest TOKEN-propagation column — or only GATE-0's REQUIRED OUTPUTS table — can independently reconstruct the full contract.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
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
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract — GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK → GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract — self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

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
| `FOCUS: ACTIVE — [dimension] \| INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes — committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] → [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| ≥3 named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| ≥1 inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior — not a generic category label]
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
| ≥3 findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
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
| ≥3 AMEND data rows — all four cells filled per row | No |
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

## V-05 — All New Criteria + Structured Mini-Table Dual-Target Declaration

**Axis:** Architecture block uses a structured native markdown mini-table to explicitly enumerate both target artifacts — the manifest TOKEN-propagation column and GATE-0's REQUIRED OUTPUTS table — with their roles and contract content, then follows with prose that uses "Declaration site" and "Substitution/inheritance site" verbatim. The mini-table format makes the dual-target declaration machine-verifiable from the architecture block alone: each row names one artifact, its propagation role, and what the full contract looks like in that artifact. C-38 and C-39 both pass. Output format axis: structured table vs. V-04's prose form.
**Hypothesis:** C-37 PASS (triple-mechanism: verbatim cells + architecture block + bracket header). C-38 PASS — mini-table explicitly names "manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" as separate rows; a reader consulting only the block can identify both target artifacts by label, role, and contract content simultaneously. C-39 PASS — architecture block prose section uses "Declaration site" and "Substitution/inheritance site" verbatim; same vocabulary scan confirms both artifacts. C-36 PASS (dedicated propagation row independently self-contained). Aspirational: 31/31 = 100.000. Decisive question vs V-04: does the structured mini-table form of dual-target declaration produce stronger C-38 compliance than V-04's prose form, or are both equivalent? A secondary question: does adding a structured mini-table to the architecture block create any overhead that reduces model accuracy on other criteria (regression risk)?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This architecture block is the declared primer for two independent structural artifacts that carry the propagation contract:

| Structural artifact | Propagation role | Contract content readable from artifact alone |
|---------------------|------------------|-----------------------------------------------|
| Manifest TOKEN-propagation column (`[TOKEN] propagation` column in EXECUTION PLAN table) | Declaration site (GATE-0 row) + Substitution/inheritance sites (GATE-1+ rows) | GATE-0 cell: "Declaration site — TOKEN committed here; `[TOKEN] required?` retained; committed value substitutes `[TOKEN]` in GATE-1+ REQUIRED OUTPUTS column headers and this manifest column header." GATE-1+ cells: "Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header." |
| GATE-0's REQUIRED OUTPUTS table (Propagation contract row) | Declaration site + explicit substitution rule declared | "GATE-0 is the Declaration site: committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers and in the `[TOKEN] propagation` manifest column header; GATE-1+ are Substitution/inheritance sites — each independently carries the committed value in its REQUIRED OUTPUTS column header without referencing this table or the manifest column." |

Neither artifact is load-bearing for the other. Both are targets of this architecture block.

GATE-0 is the Declaration site: TOKEN is committed to a domain-adaptive identifier in this gate. GATE-0's own REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed. The committed value substitutes `[TOKEN]` in all GATE-1 through GATE-4 REQUIRED OUTPUTS column headers and in the `[TOKEN] propagation` manifest column header. GATE-1 through GATE-4 are Substitution/inheritance sites: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution. A reader consulting only this architecture block — or only the manifest TOKEN-propagation column — or only GATE-0's REQUIRED OUTPUTS table — can independently reconstruct the full contract.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `[TOKEN]` in this manifest column header |
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
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract — GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK → GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are Substitution/inheritance sites — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract — self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

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
| `FOCUS: ACTIVE — [dimension] \| INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — committed TOKEN value confirmed as active inertia reference for all downstream gates | **Yes — committed value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] → [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| ≥3 named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| ≥1 inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior — not a generic category label]
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
| ≥3 findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
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
| ≥3 AMEND data rows — all four cells filled per row | No |
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

## Composite Hypothesis Table

| Variation | C-36 | C-37 mechanism | C-38 mechanism | C-39 mechanism | C-37 pred | C-38 pred | C-39 pred | Asp pred | Composite pred |
|-----------|------|---------------|---------------|---------------|-----------|-----------|-----------|----------|----------------|
| **V-01** | FAIL (compact Yes-cell) | C-33+C-34+C-35 all present; triple-mechanism complete | FAIL — C-36 dep fails, scored 0 | Architecture block uses "Declaration site" / "Substitution/inheritance site" verbatim; C-33+C-34 both pass | PASS | FAIL | PASS | 29/31 | **99.355** |
| **V-02** | PASS (dedicated row) | C-33+C-34+C-35 all present | Architecture block names "manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" explicitly; synonyms in block prose | Block uses synonyms: "declaring gate" / "consuming gates" — not verbatim rubric vocabulary | PASS | PASS | FAIL | 30/31 | **99.677** |
| **V-03** | PASS (dedicated row) | C-33+C-34+C-35 all present | Architecture block does not name both artifacts by label; describes contract but not artifact targets | Block uses "Declaration site" / "Substitution/inheritance site" verbatim; same vocabulary as C-33 manifest cells | PASS | FAIL | PASS | 30/31 | **99.677** |
| **V-04** | PASS (dedicated row) | C-33+C-34+C-35 all present | Architecture block names both artifacts explicitly in prose; uses verbatim vocabulary simultaneously | Block uses "Declaration site" / "Substitution/inheritance site" verbatim; vocabulary co-registration closed | PASS | PASS | PASS | 31/31 | **100.000** |
| **V-05** | PASS (dedicated row) | C-33+C-34+C-35 all present | Architecture block mini-table names both artifacts as rows with roles and contract content; then prose uses verbatim vocabulary | Block prose uses "Declaration site" / "Substitution/inheritance site" verbatim after mini-table; full vocabulary ring | PASS | PASS | PASS | 31/31 | **100.000** |

**Predicted ranking:** V-01 = 99.355 < V-02 = V-03 = 99.677 < V-04 = V-05 = 100.000

**If V-01 and V-02/V-03 do not separate on composite score but do separate on aspirational pass count:** The 0.323-pt difference (29/31 vs 30/31) is real but small; scorecards should separate by aspirational count. If scorecards do not separate, either C-37 is trivially satisfied by all forms above a baseline or the 0.323-pt weight is below measurement resolution.

**If V-02 and V-03 score the same (both 30/31):** C-38 and C-39 are orthogonal axes that contribute identical composite weight. The scorecard must distinguish by criterion pass/fail pattern — V-02: C-38 PASS / C-39 FAIL vs. V-03: C-38 FAIL / C-39 PASS.

**If V-04 and V-05 score the same (both 100.000):** The structured mini-table format in V-05 adds no compliance advantage over V-04's prose form for C-38. The architecture block is an instruction layer, not an output artifact — its format (prose vs. table) does not affect which criteria pass as long as the content requirements are met. R15 would then focus on other gaps, if any remain.

**If V-04 passes C-38 but V-05 does not (unexpected regression):** The mini-table in V-05's architecture block may cause the model to treat the architecture block itself as an output artifact and attempt to render it in the actual analysis output, creating structural confusion. If this regression occurs, V-04's prose form is the stable maximum and V-05 reveals a format overhead failure mode.
