Written to `simulations/quest/variations/discover-competitors-alt-variations-R11-2026-03-18.md`.

---

## R11 Variations — Summary

**Single axis:** Where and how the propagation declaration appears relative to GATE-0's REQUIRED OUTPUTS table. All 5 use `[TOKEN] required?` bracket notation throughout (C-30 bracket form secured from R10).

| # | Axis | GATE-0 table form | C-30 | C-31 | Predicted |
|---|------|-------------------|------|------|-----------|
| V-01 | Preamble-only substitution instruction | TOKEN row: "Yes — committed value declared here" (no propagation in table) | PASS | FAIL | 99.565 |
| V-02 | Dedicated propagation row in GATE-0 table | 3 rows: DOMAIN-TERMS / TOKEN / Propagation contract (with before→after example) | PASS | PASS | 100 |
| V-03 | Bracket notation, zero substitution instruction | TOKEN row: "Yes — domain-adaptive token declared" | FAIL | FAIL | 99.130 |
| V-04 | TOKEN row Yes-cell carries full propagation contract | TOKEN row: "Yes — GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ column headers" | PASS | PASS | 100 |
| V-05 | Triple-layer: preamble + TOKEN cell + manifest column | Same as V-04 + manifest "TOKEN propagation" column | PASS | PASS | 100 |

**Three decisive questions resolved by this round:**

1. **V-01 vs V-02** — Does preamble-only instruction satisfy C-31's "from the table in isolation"? If V-01 fails, C-31 requires a row/cell inside the table — preamble is insufficient.
2. **V-03** — Does bracket notation without instruction fail C-30? If yes, the "with an explicit substitution instruction" clause in C-30 is an independent requirement, not implied by bracket syntax.
3. **V-04 vs V-02** — Does the TOKEN row Yes-cell (compact) satisfy C-31 equally to a dedicated row (verbose)? The rubric says "row or cell" — both should pass, confirming V-04 as the minimal compliant form.
 | 100.000 (23/23 asp) |
| **V-03** | `[TOKEN]` bracket notation present but NO substitution instruction anywhere | No instruction to substitute committed value in column headers — bracket notation is structural decoration only | FAIL | FAIL | 99.130 (21/23 asp) |
| **V-04** | TOKEN row Yes-cell carries full propagation contract (compact form) | No dedicated propagation row; propagation declared inside the TOKEN row's Yes-cell | PASS | PASS | 100.000 (23/23 asp) |
| **V-05** | Triple-layer: preamble + TOKEN row propagation cell + manifest TOKEN column | Maximum redundancy across all declaration locations | PASS | PASS | 100.000 (23/23 asp) |

**Predicted ranking:** V-02 = V-04 = V-05 = **100** > V-01 = **99.565** > V-03 = **99.130**

**Decisive R11 questions:**
1. Does preamble-only placement satisfy C-30's "explicit substitution instruction" but still fail C-31 because "consulting only GATE-0's table" yields no propagation contract?
2. Does bracket notation without any instruction fail C-30? If yes, V-03 drops to 21/23.
3. Does a Yes-cell in the TOKEN row (V-04) satisfy C-31's "row or cell" requirement as fully as a dedicated row (V-02)?

---

## V-01 — Substitution instruction in preamble only; no propagation inside GATE-0 table

**Axis:** Substitution rule declared in preamble only (before EXECUTION PLAN). GATE-0's REQUIRED OUTPUTS table uses `[TOKEN] required?` as column header and the TOKEN row's Yes-cell carries no propagation contract.
**Hypothesis:** C-30 is satisfied — bracket notation plus preamble instruction. C-31 fails — "consulting only GATE-0's REQUIRED OUTPUTS table" yields the declaration (TOKEN committed here) but not the propagation contract (substitutes `[TOKEN]` in GATE-1+ headers). Table is incomplete as standalone contract.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule (applies from GATE-1 onward):** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4. GATE-0's own column header retains `[TOKEN] required?` — do not substitute in GATE-0's own table.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations |
|------|----------------|--------------------|
| GATE-0 | UNCONDITIONAL — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic and market inference |
| GATE-2 | CONDITIONAL | C0 description, competitive map |
| GATE-3 | CONDITIONAL | Findings, whitespace |
| GATE-4 | CONDITIONAL | AMEND table |

GATE-0 is unconditional; GATE-1 is the first conditional gate.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — committed value declared here** |

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

C0 must appear before any competitor row. Mechanism must name something C0 actually does — "Inertia is high" without a product-specific anchor fails. Run a WebSearch to verify at least one competitor claim. Weave focus dimension into competitor rows if ACTIVE.

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

## V-02 — Dedicated propagation row in GATE-0 table (most explicit form)

**Axis:** GATE-0's REQUIRED OUTPUTS table has a dedicated third row — "Propagation contract" — stating the full substitution contract inside the table. No preamble substitution instruction; all propagation information is inside the table and extractable without reading any prose.
**Hypothesis:** A dedicated propagation row is the clearest C-31 form — declaration and propagation are structurally distinct rows, each independently verifiable. C-30 is satisfied by the row body containing the explicit substitution statement. A reader consulting only GATE-0's table finds both the declaration (TOKEN committed in row 2) and the propagation rule (row 3 names the substitution contract for GATE-1+ headers).

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract. In every REQUIRED OUTPUTS table after GATE-0: `[TOKEN] required?` is a column header placeholder — substitute the committed TOKEN value (from GATE-0) in all gates after GATE-0.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations |
|------|----------------|--------------------|
| GATE-0 | UNCONDITIONAL — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic and market inference |
| GATE-2 | CONDITIONAL | C0 description, competitive map |
| GATE-3 | CONDITIONAL | Findings, whitespace |
| GATE-4 | CONDITIONAL | AMEND table |

GATE-0 is unconditional; GATE-1 is the first conditional gate.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context; not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — committed value declared in this gate** |
| Propagation contract — `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK → GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header) | **Contract — readable from this table in isolation** |

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

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if ACTIVE.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior — not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [key capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| ≥3 findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding — specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes — committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) — gap uncontested across competitive + focus dimensions simultaneously | **Yes if FOCUS ACTIVE** |

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

## V-03 — `[TOKEN]` bracket notation present but NO substitution instruction anywhere

**Axis:** All REQUIRED OUTPUTS tables use `[TOKEN] required?` bracket-notation column headers throughout. No instruction — not in the preamble, not in any gate body, not in any table cell — tells the model to substitute the committed value into GATE-1+ column headers. Bracket notation is structural; it is unaccompanied by a substitution rule.
**Hypothesis:** C-30 requires both bracket notation AND an explicit substitution instruction. "Uses `[TOKEN]` bracket-notation syntax with an explicit substitution instruction" — the "with" clause is not optional. Without the instruction, C-30 fails even if bracket notation is present. C-31 fails by dependency. Additionally, without a substitution instruction, the model likely outputs `[TOKEN] required?` literally in GATE-1+ column headers, also failing C-29.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations |
|------|----------------|--------------------|
| GATE-0 | UNCONDITIONAL — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic and market inference |
| GATE-2 | CONDITIONAL | C0 description, competitive map |
| GATE-3 | CONDITIONAL | Findings, whitespace |
| GATE-4 | CONDITIONAL | AMEND table |

GATE-0 is unconditional; GATE-1 is the first conditional gate.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context; not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — domain-adaptive token declared** |

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
| TOKEN carry-forward — TOKEN (value from GATE-0) confirmed as active inertia reference | **Yes — TOKEN by declared value required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] → [specific C0 behavior]` | **Yes — TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header | **Yes — TOKEN by declared value in column header and every vs-TOKEN cell** |
| ≥3 named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| ≥1 inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if ACTIVE.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [key capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| ≥3 findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line | **Yes — TOKEN by declared value in every `vs [TOKEN]:` line** |
| WHITESPACE finding — specific named uncontested dimension; `[TOKEN] exposure:` field | **Yes — TOKEN by declared value in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) — gap uncontested across competitive + focus dimensions | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows. Specific whitespace dimension required.

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by table label]
vs [TOKEN]: [connection — TOKEN by declared value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism — TOKEN by declared value]
```

---

### GATE-4 [CONDITIONAL — AMEND]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema before data rows — all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| ≥3 AMEND data rows — all four cells filled per row | No |
| Stability verdict cells — STABLE / UNSTABLE + TOKEN by declared value | **Yes — TOKEN by declared value in every Stability verdict cell** |
| Evidence cells — reasoning distinct from verdict text | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment — focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts — name it |
| 3 | Stability verdict | STABLE / UNSTABLE — does TOKEN shift? TOKEN by declared value required |
| 4 | Evidence | Reasoning supporting the verdict — logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE — [verdict; TOKEN by declared value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |

---

## V-04 — TOKEN row Yes-cell carries full propagation contract (compact form)

**Axis:** No dedicated propagation row; no preamble substitution instruction. The TOKEN row's Yes-cell in GATE-0's REQUIRED OUTPUTS table explicitly declares the full propagation contract: "Yes — GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers." Declaration and propagation are co-located in a single cell.
**Hypothesis:** C-31 says "a row or cell" — a cell is explicitly sufficient. The TOKEN row's Yes-cell is inside the table structure, readable in isolation, and carries both the declaration (TOKEN committed here) and the propagation contract (committed value substitutes in GATE-1+ headers). This is the most compact form that fully satisfies C-31 without a dedicated row. C-30 is satisfied because the cell IS the explicit substitution instruction.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract. In every REQUIRED OUTPUTS table after GATE-0: `[TOKEN] required?` is a column header placeholder — substitute the committed TOKEN value (from GATE-0) in all gates after GATE-0.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations |
|------|----------------|--------------------|
| GATE-0 | UNCONDITIONAL — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic and market inference |
| GATE-2 | CONDITIONAL | C0 description, competitive map |
| GATE-3 | CONDITIONAL | Findings, whitespace |
| GATE-4 | CONDITIONAL | AMEND table |

GATE-0 is unconditional; GATE-1 is the first conditional gate.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context; not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers** |

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

Read repo context. Do not ask the user.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] → [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| ≥3 named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| ≥1 inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if ACTIVE.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior — not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [key capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| ≥3 findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding — specific named uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes — committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) — gap uncontested across competitive + focus dimensions simultaneously | **Yes if FOCUS ACTIVE** |

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

## V-05 — Triple-layer: preamble + TOKEN row propagation cell + manifest TOKEN column

**Axis:** Maximum declaration redundancy across three distinct structural locations: (1) preamble states the substitution rule explicitly, (2) GATE-0's TOKEN row Yes-cell declares the full propagation contract (same as V-04), (3) EXECUTION PLAN manifest has a "TOKEN propagation" column specifying per-gate TOKEN commitment status. Any single layer independently satisfies C-30; the table layer satisfies C-31. The manifest layer adds architecture-level TOKEN contract visibility.
**Hypothesis:** C-30 and C-31 are satisfied by the table layer (same mechanism as V-04). The manifest column adds C-23-level structural redundancy — a reader consulting only the manifest learns the gate-by-gate TOKEN inheritance chain; a reader consulting only GATE-0's table learns both the committed value and the propagation rule. Neither alone is required for the rubric, but dual-layer declaration creates a resilient contract: the mechanism is verifiable from two independent artifacts.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4. GATE-0's own column header retains `[TOKEN] required?` — the TOKEN row cell declares the propagation contract.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | TOKEN propagation |
|------|----------------|--------------------|-------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | TOKEN declared — `[TOKEN] required?` retained in GATE-0 column header; committed value propagates to GATE-1+ |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Committed TOKEN value substituted into column header; TOKEN carry-forward confirmed |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Committed TOKEN in column header, C0 field label, `vs [TOKEN]` column, every vs-TOKEN cell |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Committed TOKEN in column header, every `vs [TOKEN]:` line, `[TOKEN] exposure:` field |
| GATE-4 | **CONDITIONAL** | AMEND table | Committed TOKEN in column header, every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context; not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers** |

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

Read repo context. Do not ask the user.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] → [specific C0 behavior]` | **Yes — committed TOKEN as C0 field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and every vs-TOKEN cell** |
| ≥3 named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| ≥1 inline WebSearch citation within a competitor entry | No |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — generic label fails. Run a WebSearch for at least one claim. Weave focus dimension into competitor rows if ACTIVE.

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

| Variation | C-30 mechanism | C-31 mechanism | C-30 pred | C-31 pred | Asp pred | Composite pred |
|-----------|----------------|----------------|-----------|-----------|----------|----------------|
| V-01 | `[TOKEN]` bracket notation + preamble substitution instruction | GATE-0 table retains `[TOKEN] required?`; TOKEN row only says "Yes — committed value declared here" — no propagation in table | PASS | FAIL | 22/23 | **99.565** |
| V-02 | `[TOKEN]` bracket notation + dedicated propagation row body contains explicit substitution rule | GATE-0 table retains `[TOKEN] required?`; dedicated Propagation contract row inside table with full substitution rule and example | PASS | PASS | 23/23 | **100.000** |
| V-03 | `[TOKEN]` bracket notation only — no substitution instruction anywhere | GATE-0 table retains `[TOKEN] required?`; TOKEN row only says "Yes — domain-adaptive token declared" | FAIL | FAIL (dep) | 21/23 | **99.130** |
| V-04 | `[TOKEN]` bracket notation + TOKEN row Yes-cell carries full substitution instruction | GATE-0 table retains `[TOKEN] required?`; TOKEN row Yes-cell: "Yes — GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ column headers" | PASS | PASS | 23/23 | **100.000** |
| V-05 | `[TOKEN]` bracket notation + preamble instruction + TOKEN row cell propagation (same as V-04) | GATE-0 table retains `[TOKEN] required?`; TOKEN row Yes-cell carries full propagation contract (same as V-04); manifest adds architecture-level TOKEN column | PASS | PASS | 23/23 | **100.000** |

**Predicted ranking:** V-02 = V-04 = V-05 = **100** > V-01 = **99.565** > V-03 = **99.130**

**If V-01 fails C-31 as predicted:** R11 learning — C-31's "from the table in isolation" requires the propagation contract to be a row or cell INSIDE the table structure. Preamble placement satisfies C-30 (instruction is declared) but not C-31 (contract not readable from table alone). The table must be a self-contained specification of both TOKEN declaration and TOKEN propagation.

**If V-03 fails C-30 as predicted:** R11 learning — bracket notation is necessary but not sufficient for C-30. The "with an explicit substitution instruction" clause imposes an independent requirement. A skill body using `[TOKEN]` syntax throughout but providing no substitution instruction produces bracket-form column headers that the model may output literally as `[TOKEN] required?` — satisfying neither C-29 (committed value not in header) nor C-30 (instruction absent).

**If V-04 = V-02 = 100:** R11 learning — compact (TOKEN row cell) and explicit (dedicated propagation row) satisfy C-31 equally. The "row or cell" formulation is not a ranking; both forms pass. The compact form is preferred unless clarity-of-separation between declaration and propagation rows is independently valued.
