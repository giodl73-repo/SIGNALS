Here are the 5 complete variations for Round 10:

---

## R10 Context

No R9 variation satisfies all three new criteria simultaneously — R9 V-01/V-04 had no completion conditions but used numbered lists (fails C-28/C-29); R9 V-02/V-05 had native tables with TOKEN columns but retained completion conditions (fails C-27).

**R10 floor for all 5 variations:** leading REQUIRED OUTPUTS native tables + no completion conditions + TOKEN-required column.

---

## Variation Summary

| # | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Output format — 2-col, generic `"TOKEN required?"` header | Generic column satisfies C-29 by structure; committed value appears in the Yes cell, not the header |
| **V-02** | Output format — 2-col, declared-value `[TOKEN] required?` (bracket-notation substitution) | C-29's "by its committed value" requires the actual declared identifier in the column header |
| **V-03** | Output format — 3-col `(Output \| Format \| TOKEN required?)`, generic header | Format column adds per-row format guidance; header semantics same as V-01 |
| **V-04** | Combined: V-02 + V-03 — declared-value header + 3-col | Both format axes together; tests whether each contributes independently |
| **V-05** | Combined: V-02 + V-03 + manifest `"Required outputs (TOKEN)"` column | Dual-layer declaration — per-gate 3-col tables + manifest-level TOKEN contract |

**Predicted:** V-02, V-04, V-05 → **100** (21/21 aspirational). V-01, V-03 → **99.524** (20/21) — generic "TOKEN required?" likely fails C-29's strict "by its committed value" test.

**The decisive R10 question:** Does `"TOKEN required?"` satisfy C-29, or does the column header need to contain the actual committed token identifier (SIGNAL-LOCK, etc.)? V-01 vs. V-02 resolves this.

Each variation is a complete, standalone skill body prompt written to `discover-competitors-alt-variations-R10-2026-03-18.md`.
2 + V-03 + manifest) | Full integration: per-gate 3-col tables with declared-value column + manifest-level "Required outputs (TOKEN)" column |

**Predicted:** V-02, V-03, V-04, V-05 → **100**. V-01 → **99.524** (C-29 likely fails — "TOKEN required?" is not the committed value; the column uses the abstract word TOKEN rather than the declared identifier).

**The decisive R10 question:** Does "TOKEN required?" (generic column header) satisfy C-29's "explicitly declares TOKEN as required by its committed value"? If yes, V-01 scores 100. If no, V-01 drops one aspirational point (99.524).

---

## V-01 — Output format: 2-col REQUIRED OUTPUTS tables with generic TOKEN column

**Axis:** Each gate's REQUIRED OUTPUTS block is a 2-column native table — `Output | TOKEN required?` — with a generic column header. No completion conditions anywhere.
**Hypothesis:** Generic "TOKEN required?" satisfies C-29 because the column structurally marks TOKEN as required; "by its committed value" refers to the declared value appearing within the Yes cell content, not necessarily in the column header itself.

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

GATE-0 is unconditional; GATE-1 is the first gate where conditional logic executes. Any gate's execution mode is verifiable in this plan without reading its body.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | TOKEN required? |
|--------|----------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — by declared value; TOKEN required in every downstream REQUIRED OUTPUTS table** |

This gate is unconditional — no focus detection, auto-detect, section headers, or conditional branching precedes or runs during it. GATE-1 is the first gate with conditional logic. Write exactly these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL — first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | TOKEN required? |
|--------|----------------|
| `FOCUS: ACTIVE — [dimension] \| INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — TOKEN (value = TOKEN from GATE-0) confirmed as active inertia reference | **Yes — TOKEN by declared value; required in GATE-2, GATE-3, GATE-4 REQUIRED OUTPUTS** |

Read repo context. Do not ask the user for topic, competitors, or market category.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | TOKEN required? |
|--------|----------------|
| C0 section before any competitor row: `## C0 — [product name]` with `[TOKEN]: [mechanism type: switching cost \| habit lock-in \| workaround satisfaction] → [specific C0 behavior or feature]` | **Yes — TOKEN as C0 section field label** |
| Competitive map — native markdown table, pipe-and-hyphen, no code fence; C0 at row 0; `vs [TOKEN]` column header | **Yes — TOKEN by declared value in column header** |
| ≥3 named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| ≥1 inline WebSearch citation within a competitor entry | No |
| TOKEN by declared value in each competitor's `vs [TOKEN]` cell | **Yes** |

C0 must appear before any competitor row. Mechanism must name something C0 actually does — "Inertia is high" without a product-specific anchor fails. Run a WebSearch to verify at least one competitor claim. If focus is ACTIVE, weave the focus dimension into competitor rows — do not append it as a separate section.

```
## C0 — [product name]
[TOKEN]: [mechanism type] → [specific C0 behavior or feature — not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [key capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [how competitor erodes or bypasses TOKEN mechanism] | [inline WebSearch citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | TOKEN required? |
|--------|----------------|
| ≥3 findings — each references a named competitor row by table label; each includes `vs [TOKEN]:` line | **Yes — TOKEN by declared value in every `vs [TOKEN]:` line** |
| WHITESPACE finding — specific uncontested dimension (named, not generic); `[TOKEN] exposure:` field | **Yes — TOKEN by declared value in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) — gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows — findings readable without GATE-2 fail. Name the specific whitespace dimension; "room to innovate" without naming the dimension fails.

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by table label]
vs [TOKEN]: [how this finding relates to TOKEN mechanism — TOKEN by declared value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism — TOKEN by declared value]
```

If FOCUS ACTIVE: cross-dimensional gap must require both the competitive map and the focus lens simultaneously; show what the focus dimension reveals that the map alone cannot produce.

---

### GATE-4 [CONDITIONAL — AMEND]

**REQUIRED OUTPUTS:**

| Output | TOKEN required? |
|--------|----------------|
| AMEND schema declared before data rows — all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| ≥3 AMEND data rows — all four cells filled per row | No |
| Stability verdict cells — STABLE / UNSTABLE + reasoning naming TOKEN by declared value | **Yes — TOKEN by declared value in every Stability verdict cell** |
| Evidence cells — reasoning distinct from verdict text; "Stable." alone fails | No |

**AMEND entry schema — all four required components:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment — focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts — name it |
| 3 | Stability verdict | STABLE / UNSTABLE — does TOKEN shift? TOKEN by declared value required |
| 4 | Evidence | Reasoning supporting the verdict — logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [user adjustment] | [gate/section that shifts — named] | STABLE / UNSTABLE — [verdict; TOKEN by declared value] | [reasoning distinct from verdict] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |

---

## V-02 — Output format: 2-col REQUIRED OUTPUTS tables with declared-value `[TOKEN]` column header

**Axis:** Each gate's REQUIRED OUTPUTS table column header uses `[TOKEN] required?` — a bracket-notation placeholder instructing the model to substitute the committed TOKEN value. After GATE-0 declares `TOKEN: SIGNAL-LOCK`, subsequent gates produce columns headed `SIGNAL-LOCK required?`. GATE-0's own table retains `[TOKEN] required?` since the value is not yet committed when that table is written.
**Hypothesis:** C-29's "by its committed value" requires the actual declared identifier (SIGNAL-LOCK, WORKFLOW-ANCHOR) in the column header, not the abstract label "TOKEN." Bracket-notation substitution is the minimal mechanism that satisfies this without hardcoding a domain-specific value in the skill body template.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence. In every REQUIRED OUTPUTS table: `[TOKEN] required?` is the column header placeholder — **substitute the committed TOKEN value** (from GATE-0) in all gates after GATE-0. GATE-0's table uses `[TOKEN] required?` literally since TOKEN has not yet been declared.

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
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed before TOKEN; 2–3 product-domain expert terms from repo context; not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token; generic placeholder alone (MECH, LOCK) fails | **Yes — declared value becomes the substituted column header in all subsequent gates** |

This gate is unconditional — no focus detection, auto-detect, section headers, or conditional branching precedes or runs during it. GATE-1 is the first gate with conditional logic. Write exactly these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

After writing TOKEN, substitute its committed value for `[TOKEN]` in all subsequent REQUIRED OUTPUTS column headers.

---

### GATE-1 [CONDITIONAL — first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `FOCUS: ACTIVE — [dimension] \| INACTIVE` | No |
| `TOPIC: [inferred product domain]` | No |
| `MARKET: [inferred market category]` | No |
| TOKEN carry-forward — TOKEN (committed value from GATE-0) confirmed as active inertia reference | **Yes — committed value required in GATE-2, GATE-3, GATE-4 REQUIRED OUTPUTS** |

Read repo context. Do not ask the user.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| C0 section before any competitor row: `## C0 — [name]` with `[TOKEN]: [mechanism type] → [specific C0 behavior]` | **Yes — committed TOKEN value as C0 section field label** |
| Competitive map — native markdown table, no code fence; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in column header and in each vs-TOKEN cell** |
| ≥3 named external competitors with explicit threat levels (HIGH / MEDIUM / LOW) | No |
| ≥1 inline WebSearch citation within a competitor entry | No |
| TOKEN by committed value in each competitor's `vs [TOKEN]` cell | **Yes** |

C0 must appear before any competitor row. Mechanism must name something C0 actually does or provides. Run a WebSearch for at least one claim. If focus is ACTIVE, weave the focus dimension into competitor rows.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior — not a generic label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | [inline WebSearch citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| ≥3 findings — each references a named competitor row by label; each includes `vs [TOKEN]:` line with committed TOKEN value | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE finding — specific uncontested dimension; `[TOKEN] exposure:` field with committed value | **Yes — committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace (only if FOCUS ACTIVE) — gap uncontested across competitive + focus dimensions; TOKEN in intersection rationale | **Yes if FOCUS ACTIVE** |

Findings must reference named competitor rows. Specific whitespace dimension required.

```
**Finding [N]: [Title]**
[Observation — named competitor row by table label]
vs [TOKEN]: [connection — TOKEN by committed value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism — TOKEN by committed value]
```

---

### GATE-4 [CONDITIONAL — AMEND]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| AMEND schema before data rows — all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| ≥3 AMEND data rows — all four cells filled | No |
| Stability verdict cells — STABLE / UNSTABLE + TOKEN by committed value | **Yes — committed TOKEN in every Stability verdict cell** |
| Evidence cells — reasoning distinct from verdict text | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment — focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts — name it |
| 3 | Stability verdict | STABLE / UNSTABLE — does TOKEN shift? TOKEN by committed value required |
| 4 | Evidence | Reasoning supporting the verdict — logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate/section named] | STABLE / UNSTABLE — [verdict; TOKEN by committed value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |

---

## V-03 — Output format: 3-col REQUIRED OUTPUTS tables (Output | Format | TOKEN required?)

**Axis:** Each gate's REQUIRED OUTPUTS block is a 3-column native table — `Output | Format | TOKEN required?` — adding a Format column that specifies the expected output format per row alongside the content requirement. Column header retains generic "TOKEN required?".
**Hypothesis:** The Format column adds per-row output format guidance (what the output looks like, not just what it is) without adding completion conditions. This richer column structure improves C-28's structural clarity. The column is domain-neutral and does not affect C-22.

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

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| DOMAIN-TERMS | `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — one line, closed before TOKEN; 2–3 product-domain expert terms from repo context; not generic software vocabulary | No |
| TOKEN | `TOKEN: [domain-adaptive identifier]` — one line; at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR); generic placeholder alone (MECH, LOCK) fails | **Yes — by declared value; required in every downstream REQUIRED OUTPUTS table** |

This gate is unconditional. Write exactly these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL — first conditional gate, focus detection and topic resolution]

**REQUIRED OUTPUTS:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| FOCUS | `FOCUS: ACTIVE — [dimension] \| INACTIVE` | No |
| TOPIC | `TOPIC: [inferred product domain]` | No |
| MARKET | `MARKET: [inferred market category]` | No |
| TOKEN carry-forward | TOKEN (value = TOKEN from GATE-0) confirmed as active inertia reference | **Yes — TOKEN by declared value; required in GATE-2, GATE-3, GATE-4** |

Read repo context. Do not ask the user.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**REQUIRED OUTPUTS:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| C0 section | `## C0 — [name]` + `[TOKEN]: [mechanism type] → [specific C0 behavior]` before any competitor row | **Yes — TOKEN as field label in C0 section** |
| Competitive map | Native markdown table (pipe-and-hyphen, no code fence); C0 at row 0; `vs [TOKEN]` column header | **Yes — TOKEN by declared value in column header** |
| External competitors | ≥3 named with explicit threat levels; focus dimension woven in if ACTIVE | No |
| WebSearch citation | ≥1 inline URL or publication name in a competitor entry | No |
| vs-TOKEN cells | Each competitor's `vs [TOKEN]` cell references TOKEN mechanism | **Yes — TOKEN by declared value** |

C0 must appear before any competitor row. Mechanism must name something C0 actually does. Run a WebSearch for at least one claim.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| Findings | `**Finding N: Title**` / `[named competitor observation]` / `vs [TOKEN]: [connection]` — ≥3 total | **Yes — TOKEN by declared value in every `vs [TOKEN]:` line** |
| WHITESPACE finding | `WHITESPACE: [specific named dimension]` / `[TOKEN] exposure: [relationship]` | **Yes — TOKEN by declared value in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace | Gap uncontested across competitive + focus dimensions simultaneously (only if FOCUS ACTIVE); show intersection | **Yes if FOCUS ACTIVE** |

---

### GATE-4 [CONDITIONAL — AMEND]

**REQUIRED OUTPUTS:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| AMEND schema | Enumerated table before data rows; all four domain-neutral component names: Input change, Output effect, Stability verdict, Evidence | No |
| AMEND data rows | ≥3 rows; all four cells filled per row | No |
| Stability verdict | `STABLE / UNSTABLE — [verdict naming TOKEN by declared value]` per row | **Yes — TOKEN by declared value in every verdict cell** |
| Evidence | Reasoning distinct from verdict; "Stable." alone fails | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | The user adjustment — focus dimension, depth level, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts — name it |
| 3 | Stability verdict | STABLE / UNSTABLE — does TOKEN shift? TOKEN by declared value required |
| 4 | Evidence | Reasoning supporting the verdict — logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate named] | STABLE / UNSTABLE — [verdict; TOKEN by declared value] | [reasoning] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |

---

## V-04 — Combined: declared-value column + 3-col (V-02 + V-03)

**Axis:** REQUIRED OUTPUTS tables are 3-column (`Output | Format | [TOKEN] required?`) with bracket-notation declared-value column header. Combines V-02's declared-value axis with V-03's Format-column axis.
**Hypothesis:** Declared-value column header + Format column together satisfy C-29 at maximum specificity (committed value in header) while providing per-row format guidance (Format column). If V-04 scores the same as V-02 and V-03 individually, neither axis adds scoring value beyond the floor. If V-04 outperforms, the combination has structural synergy.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence. In every REQUIRED OUTPUTS table: `[TOKEN] required?` is the column header placeholder — **substitute the committed TOKEN value** (from GATE-0) in all gates after GATE-0.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations |
|------|----------------|--------------------|
| GATE-0 | UNCONDITIONAL — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic and market inference |
| GATE-2 | CONDITIONAL | C0 description, competitive map |
| GATE-3 | CONDITIONAL | Findings, whitespace |
| GATE-4 | CONDITIONAL | AMEND table |

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | Format | [TOKEN] required? |
|--------|--------|------------------|
| DOMAIN-TERMS | `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed before TOKEN; product-domain expert terms; not generic vocabulary | No |
| TOKEN | `TOKEN: [domain-adaptive identifier]` — ≥1 DOMAIN-TERMS term; copyable token; generic placeholder alone fails | **Yes — committed value becomes the substituted column header in all subsequent gates** |

This gate is unconditional. Write these two lines first — nothing before, nothing between:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

After declaring TOKEN, substitute its committed value for `[TOKEN]` in all subsequent REQUIRED OUTPUTS column headers.

---

### GATE-1 [CONDITIONAL — first conditional gate]

**REQUIRED OUTPUTS:**

| Output | Format | [TOKEN] required? |
|--------|--------|------------------|
| FOCUS | `FOCUS: ACTIVE — [dimension] \| INACTIVE` | No |
| TOPIC | `TOPIC: [inferred domain]` | No |
| MARKET | `MARKET: [inferred market category]` | No |
| TOKEN carry-forward | TOKEN (committed value from GATE-0) confirmed as active inertia reference | **Yes — committed value required in GATE-2, GATE-3, GATE-4** |

---

### GATE-2 [CONDITIONAL — C0 and competitive map]

**REQUIRED OUTPUTS:**

| Output | Format | [TOKEN] required? |
|--------|--------|------------------|
| C0 section | `## C0 — [name]` + `[TOKEN]: [mechanism type] → [specific behavior]` before any competitor row | **Yes — committed TOKEN as C0 field label** |
| Competitive map | Native markdown table; C0 at row 0; `vs [TOKEN]` column header using committed value | **Yes — committed value in header and in each vs-TOKEN cell** |
| Competitors | ≥3 named with explicit threat levels; focus woven in if ACTIVE | No |
| Citation | ≥1 inline WebSearch citation | No |

```
## C0 — [product name]
[TOKEN]: [mechanism type] → [specific behavior — not a generic label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN] | [citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | Format | [TOKEN] required? |
|--------|--------|------------------|
| Findings | `**Finding N: Title**` / `[named competitor observation]` / `vs [TOKEN]: [connection]` — ≥3 | **Yes — committed TOKEN in every `vs [TOKEN]:` line** |
| WHITESPACE | `WHITESPACE: [specific dimension]` / `[TOKEN] exposure: [relationship]` | **Yes — committed TOKEN in `[TOKEN] exposure:` field** |
| Cross-dimensional whitespace | Gap uncontested across competitive + focus simultaneously (if FOCUS ACTIVE) | **Yes if ACTIVE** |

---

### GATE-4 [CONDITIONAL — AMEND]

**REQUIRED OUTPUTS:**

| Output | Format | [TOKEN] required? |
|--------|--------|------------------|
| Schema | Enumerated table before data rows: Input change, Output effect, Stability verdict, Evidence | No |
| Data rows | ≥3 rows; all four cells filled | No |
| Stability verdict | `STABLE / UNSTABLE — [verdict; committed TOKEN value]` per row | **Yes — committed TOKEN in every verdict cell** |
| Evidence | Reasoning distinct from verdict | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | User adjustment — focus dimension, depth, competitor scope |
| 2 | Output effect | Gate or section that specifically shifts — name it |
| 3 | Stability verdict | STABLE / UNSTABLE — committed TOKEN affected? Required by committed value |
| 4 | Evidence | Reasoning distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate named] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |

---

## V-05 — Combined: declared-value column + 3-col + manifest TOKEN column

**Axis:** All of V-04 plus a "Required outputs (TOKEN)" column in the EXECUTION PLAN manifest, naming the committed TOKEN contract for each gate at the architecture level. Dual-layer TOKEN declaration: manifest column establishes the cross-gate contract; per-gate 3-col tables provide per-gate detail.
**Hypothesis:** Manifest-level TOKEN column adds a structural artifact that satisfies C-29 independently of any single gate's table — a reader consulting only the manifest can identify TOKEN as required per gate. Combined with 3-col declared-value per-gate tables, this is the maximum-redundancy TOKEN declaration architecture.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence. In every REQUIRED OUTPUTS table: `[TOKEN] required?` is the column header placeholder — **substitute the committed TOKEN value** (from GATE-0) throughout.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | Required outputs (TOKEN) |
|------|----------------|--------------------|--------------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | TOKEN declared by committed value — first unconditional output |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | TOKEN (from GATE-0) confirmed by committed value as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | TOKEN by committed value in C0 label, `vs [TOKEN]` column header, every vs-TOKEN cell |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | TOKEN by committed value in every `vs [TOKEN]:` line and `[TOKEN] exposure:` field |
| GATE-4 | **CONDITIONAL** | AMEND table | TOKEN by committed value in every Stability verdict cell |

GATE-0 is unconditional. GATE-1 is the first conditional gate. Any gate's execution mode and TOKEN contract is verifiable in this manifest without reading its body.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | Format | [TOKEN] required? |
|--------|--------|------------------|
| DOMAIN-TERMS | `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed before TOKEN; product-domain expert terms | No |
| TOKEN | `TOKEN: [domain-adaptive identifier]` — ≥1 DOMAIN-TERMS term; committed value substituted into all downstream column headers | **Yes — committed value is the manifest's TOKEN anchor; GATE-1 through GATE-4 inherit it** |

This gate is unconditional. Write these two lines first — nothing before, nothing between:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

Substitute committed TOKEN value for `[TOKEN]` in all subsequent REQUIRED OUTPUTS column headers and all `vs [TOKEN]` references.

---

### GATE-1 [CONDITIONAL — first conditional gate]

**REQUIRED OUTPUTS:**

| Output | Format | [TOKEN] required? |
|--------|--------|------------------|
| FOCUS | `FOCUS: ACTIVE — [dimension] \| INACTIVE` | No |
| TOPIC | `TOPIC: [inferred domain]` | No |
| MARKET | `MARKET: [inferred market category]` | No |
| TOKEN carry-forward | Committed TOKEN value confirmed active — required in GATE-2, GATE-3, GATE-4 | **Yes** |

---

### GATE-2 [CONDITIONAL — C0 and competitive map]

**REQUIRED OUTPUTS:**

| Output | Format | [TOKEN] required? |
|--------|--------|------------------|
| C0 section | `## C0 — [name]` + `[TOKEN]: [mechanism type] → [specific behavior]` before any competitor row | **Yes — committed TOKEN as C0 field label** |
| Competitive map | Native markdown table; C0 at row 0; `vs [TOKEN]` column using committed value | **Yes** |
| Competitors | ≥3 named with explicit threat levels; focus woven in if ACTIVE | No |
| Citation | ≥1 inline WebSearch citation | No |
| vs-TOKEN cells | Each row references committed TOKEN mechanism | **Yes** |

```
## C0 — [product name]
[TOKEN]: [mechanism type] → [specific behavior — not a generic label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN] | [citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

**REQUIRED OUTPUTS:**

| Output | Format | [TOKEN] required? |
|--------|--------|------------------|
| Findings | `**Finding N: Title**` / `[named competitor]` / `vs [TOKEN]: [connection]` — ≥3 | **Yes** |
| WHITESPACE | `WHITESPACE: [specific dimension]` / `[TOKEN] exposure: [relationship]` | **Yes** |
| Cross-dimensional whitespace | Intersection of competitive + focus gap (if FOCUS ACTIVE) | **Yes if ACTIVE** |

---

### GATE-4 [CONDITIONAL — AMEND]

**REQUIRED OUTPUTS:**

| Output | Format | [TOKEN] required? |
|--------|--------|------------------|
| Schema | Enumerated before data: Input change, Output effect, Stability verdict, Evidence | No |
| Data rows | ≥3 rows; all four cells filled | No |
| Stability verdict | `STABLE / UNSTABLE — [verdict; committed TOKEN]` per row | **Yes — committed TOKEN in every row** |
| Evidence | Reasoning distinct from verdict | No |

**AMEND entry schema:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | Input change | User adjustment — focus dimension, depth, competitor scope |
| 2 | Output effect | Gate or section that specifically shifts — name it |
| 3 | Stability verdict | STABLE / UNSTABLE — committed TOKEN affected? Required by committed value |
| 4 | Evidence | Reasoning distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [gate named] | STABLE / UNSTABLE — [verdict; committed TOKEN] | [reasoning] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |

---

## Composite Hypothesis Table

| Variation | C-27 strategy | C-28 strategy | C-29 strategy | Prediction | Critical question |
|-----------|---------------|---------------|---------------|------------|-------------------|
| V-01 | No completion conditions; REQUIRED OUTPUTS table is sole spec per gate | Native 2-col table per gate | "TOKEN required?" generic header; committed value appears in Yes cell content | **99.524** (20/21) | Does generic "TOKEN required?" satisfy C-29's "by its committed value"? If the criterion requires the actual token identifier in the column header, V-01 fails C-29. |
| V-02 | No completion conditions | Native 2-col table per gate | `[TOKEN] required?` bracket-notation header; substituted to committed value post-GATE-0 | **100** (21/21) | Is bracket-notation substitution a valid mechanism for C-29? Does the skill body's placeholder satisfy C-29 given the model produces committed-value headers at runtime? |
| V-03 | No completion conditions | Native 3-col table (Output \| Format \| TOKEN required?) per gate | "TOKEN required?" generic header — same semantics as V-01 | **99.524** (20/21) | Does adding a Format column change C-29 outcomes, or does the column header semantics dominate? If C-29 is strictly header-based, V-03 fails just like V-01. |
| V-04 | No completion conditions | Native 3-col table per gate | `[TOKEN] required?` declared-value header; 3-col structure | **100** (21/21) | Do declared-value column + Format column produce any synergy beyond V-02's 2-col? If both score 100, the Format column is a structural bonus with no scoring cost. |
| V-05 | No completion conditions | Native 3-col table per gate + manifest TOKEN column | `[TOKEN] required?` in per-gate tables + manifest "Required outputs (TOKEN)" column | **100** (21/21) | Does manifest-level TOKEN column satisfy C-29 independently, or does C-29 require the column to be within the per-gate REQUIRED OUTPUTS block specifically? Does dual-layer declaration add resilience or redundancy? |

**Predicted ranking:** V-02 = V-04 = V-05 = **100**. V-01 = V-03 = **99.524** — both use generic "TOKEN required?" and both likely fail C-29's "by its committed value" requirement.

**If V-01 and V-03 both fail C-29:** The decisive R10 learning is that the TOKEN column header must use the committed declared value, not the abstract label "TOKEN." Generic "TOKEN required?" satisfies C-28 (native table) but not C-29 (by its committed value).

**If V-01 and V-03 both pass C-29:** C-29 is structure-sufficient (a column that marks TOKEN as required satisfies the criterion regardless of whether the header contains the committed value). All five variations score 100.
