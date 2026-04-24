Written to `simulations/quest/variations/discover-competitors-alt-variations-R13-2026-03-18.md`.

---

## R13 Variations — Summary

**Single axis (V-01, V-02, V-03)** each isolate exactly one of the three independently testable new criteria. C-36 (dual-layer independence) cannot be a single-axis variation because it requires belt-and-suspenders completion of both C-31 and C-32, which in turn require the full preceding chain — so the combination variations build toward it.

| # | Axis | Manifest header | Manifest cells | Pre-manifest block | GATE-0 table | C-33 | C-34 | C-35 | C-36 | Composite pred |
|---|------|-----------------|---------------|-------------------|--------------|------|------|------|------|----------------|
| V-01 | C-33 only | `TOKEN propagation` (static) | "Declaration site" / "Substitution/inheritance site" verbatim | None | Compact Yes-cell | PASS | FAIL | FAIL | FAIL | 98.929 |
| V-02 | C-34 only | `TOKEN propagation` (static) | `DECLARE` / `INHERIT` shorthand | Architecture block present | Compact Yes-cell | FAIL | PASS | FAIL | FAIL | 98.929 |
| V-03 | C-35 only | `[TOKEN] propagation` (bracket) | `DECLARE` / `INHERIT` shorthand | None | Compact Yes-cell | FAIL | FAIL | PASS | FAIL | 98.929 |
| V-04 | C-33 + C-34 + C-35 | `[TOKEN] propagation` (bracket) | Verbatim vocabulary | Architecture block present | Compact Yes-cell | PASS | PASS | PASS | ? | 99.643–100 |
| V-05 | C-33 + C-34 + C-35 + C-36 | `[TOKEN] propagation` (bracket) | Verbatim vocabulary | Architecture block present | Dedicated propagation row (R11 V-02 form) | PASS | PASS | PASS | PASS | 100.000 |

**Three decisive questions:**
1. **V-03** — Does the model substitute the committed value into `[TOKEN] propagation` in the manifest header, or output it literally? This is the C-35 diagnostic: literal output reveals substitution is REQUIRED OUTPUTS-scoped only.
2. **V-04 vs V-05** — Does the compact Yes-cell pass C-36's independence test, or does C-36 strictly require the dedicated propagation row? If compact Yes-cell passes, V-04 = 100 and V-05 adds no structural value.
3. **V-01 vs V-02** — Does the architecture block (V-02) produce different model compliance than pure verbatim vocabulary (V-01), or are both equally reliable at this level?
ling substitution is REQUIRED OUTPUTS-scoped only)?
3. **V-04 vs V-05** — Does the compact Yes-cell fail C-36's independence test, or does it independently carry the propagation contract without cross-reference to the manifest? If compact Yes-cell passes C-36, V-04 would also score 100.
4. **V-01 through V-03** — Are the single-axis variations clearly separating on the new criteria, or does including all three in V-04/V-05 produce a halo effect that makes individual attribution ambiguous?

---

## V-01 — C-33: Rubric-Vocabulary Verbatim in Manifest TOKEN-Propagation Cells

**Axis:** Manifest TOKEN-propagation column uses "Declaration site" and "Substitution/inheritance site" verbatim — the exact C-32 operative test vocabulary — in every cell. The column header remains a static label (`TOKEN propagation`, no bracket notation). No pre-manifest architecture block. GATE-0 REQUIRED OUTPUTS uses the compact Yes-cell form.
**Hypothesis:** C-33 PASS — manifest cells pre-answer the C-32 operative test phrasing without any interpretation step. C-34 FAIL (no pre-manifest architecture block). C-35 FAIL (static column header, no bracket notation). C-36 FAIL (compact Yes-cell; independence of GATE-0 table vs. manifest not established by a dedicated propagation row). Composite: 25/28 aspirational = 98.929.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the TOKEN row Yes-cell declares the propagation contract.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | TOKEN propagation |
|------|----------------|--------------------|-------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward active |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label, and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
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

C0 must appear before any competitor row. Mechanism must name something C0 actually does — "Inertia is high" without a product-specific anchor fails. Run a WebSearch to verify at least one competitor claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

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

## V-02 — C-34: Pre-Manifest TOKEN-PROPAGATION ARCHITECTURE Block, Compact Cells

**Axis:** A TOKEN-PROPAGATION ARCHITECTURE block is declared as a separate, closed prose artifact before the EXECUTION PLAN table. It states the full propagation contract in plain language — which gate is the declaration site, which are substitution/inheritance sites, and what substitution rule applies. The manifest column uses compact shorthand (`DECLARE` / `INHERIT`) — satisfying C-32's minimum viable form but not C-33's verbatim-vocabulary requirement. Manifest column header is a static label (`TOKEN propagation`, no bracket notation). No C-35 or C-36.
**Hypothesis:** C-34 PASS — architecture block is present, closed, and precedes the manifest table; a reader consulting only the block can reconstruct the full propagation contract. C-33 FAIL (compact `DECLARE`/`INHERIT` cells, not rubric-vocabulary verbatim). C-35 FAIL (static header). C-36 FAIL (compact Yes-cell, not independently complete dedicated propagation row). Composite: 25/28 aspirational = 98.929. Decisive question: does the pre-manifest architecture block prime model compliance with correct compact column content, or does it produce redundant noise the manifest column handles alone?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the TOKEN row Yes-cell declares the propagation contract.

**TOKEN-PROPAGATION ARCHITECTURE**

GATE-0 is the declaration site: TOKEN is committed to a domain-adaptive identifier in this gate. GATE-0's own REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed. The committed value substitutes `[TOKEN]` in all GATE-1 through GATE-4 REQUIRED OUTPUTS column headers. GATE-1 through GATE-4 are substitution/inheritance sites: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution. TOKEN carry-forward is a required output element for every gate after GATE-0. A reader consulting this block can reconstruct the full propagation contract — declaration gate, substitution gates, and substitution rule — without consulting the EXECUTION PLAN manifest column or any per-gate REQUIRED OUTPUTS table.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | TOKEN propagation |
|------|----------------|--------------------|-------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | DECLARE — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; committed value propagates to GATE-1+ REQUIRED OUTPUTS column headers by substitution |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | INHERIT — committed TOKEN substituted into REQUIRED OUTPUTS column header; carry-forward active |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | INHERIT — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label, and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | INHERIT — committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | INHERIT — committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
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

## V-03 — C-35: Bracket Notation `[TOKEN] propagation` in Manifest Column Header

**Axis:** The manifest TOKEN-propagation column header uses `[TOKEN] propagation` bracket notation, making the manifest header a participant in the same substitution lifecycle as REQUIRED OUTPUTS column headers. The substitution rule is extended to explicitly name the manifest column header as a substitution target. The manifest cells use compact shorthand (`DECLARE` / `INHERIT`) — C-32 minimum viable, not C-33 verbatim vocabulary. No pre-manifest architecture block (no C-34).
**Hypothesis:** C-35 PASS — bracket notation in manifest column header; after GATE-0 commits (e.g., TOKEN = SIGNAL-LOCK), the header substitutes to `SIGNAL-LOCK propagation`. C-33 FAIL (compact cells). C-34 FAIL (no architecture block). C-36 FAIL (compact Yes-cell). Composite: 25/28 aspirational = 98.929. Decisive question: does the model correctly substitute the committed TOKEN value into the manifest column header, or does it output `[TOKEN] propagation` literally — revealing bracket-notation substitution is scoped to REQUIRED OUTPUTS tables only and does not extend to the pre-execution manifest?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the TOKEN row Yes-cell declares the propagation contract. After GATE-0 commits (e.g., TOKEN = SIGNAL-LOCK), the manifest column header becomes `SIGNAL-LOCK propagation` by the same substitution rule.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | DECLARE — TOKEN committed here; `[TOKEN] required?` retained in GATE-0 REQUIRED OUTPUTS column header; committed value propagates to GATE-1+ REQUIRED OUTPUTS column headers and to this manifest `[TOKEN] propagation` column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | INHERIT — committed TOKEN substituted into REQUIRED OUTPUTS column header; carry-forward active |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | INHERIT — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label, and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | INHERIT — committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | INHERIT — committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

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

## V-04 — C-33 + C-34 + C-35: Verbatim Vocabulary + Architecture Block + Bracket Notation Header

**Axis:** Combines the three independently isolatable new criteria: (1) manifest cells use "Declaration site" / "Substitution/inheritance site" rubric vocabulary verbatim (C-33), (2) a TOKEN-PROPAGATION ARCHITECTURE block appears as a closed prose artifact before the manifest (C-34), and (3) the manifest column header uses `[TOKEN] propagation` bracket notation (C-35). GATE-0 REQUIRED OUTPUTS uses the compact Yes-cell form — not a dedicated propagation row — so C-36 independence is not explicitly guaranteed.
**Hypothesis:** C-33 PASS, C-34 PASS, C-35 PASS. C-36 uncertain — the compact Yes-cell may satisfy C-31 without explicitly claiming independence from the manifest, leaving C-36's non-delegation test ambiguous. If the rubric scores C-36 by consulting each layer in isolation and finds the compact Yes-cell self-contained, V-04 passes C-36 and scores 100. If the rubric requires the dedicated propagation row to confirm independence, V-04 fails C-36 and scores 99.643 (27/28 aspirational). Composite pred: 99.643 to 100.000.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the TOKEN row Yes-cell declares the propagation contract.

**TOKEN-PROPAGATION ARCHITECTURE**

GATE-0 is the declaration site: TOKEN is committed to a domain-adaptive identifier in this gate. GATE-0's own REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed. The committed value substitutes `[TOKEN]` in all GATE-1 through GATE-4 REQUIRED OUTPUTS column headers and in the `[TOKEN] propagation` manifest column header. GATE-1 through GATE-4 are substitution/inheritance sites: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution. TOKEN carry-forward is a required output element for every gate after GATE-0. A reader consulting this block can reconstruct the full propagation contract — declaration gate, substitution gates, and substitution rule — without consulting the EXECUTION PLAN manifest column or any per-gate REQUIRED OUTPUTS table.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers and in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
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

## V-05 — C-33 + C-34 + C-35 + C-36: All Four New Criteria, Maximum Dual-Layer Independence

**Axis:** Combines all four new R13 criteria. C-33: manifest cells use "Declaration site" / "Substitution/inheritance site" rubric vocabulary verbatim. C-34: TOKEN-PROPAGATION ARCHITECTURE block precedes the manifest. C-35: manifest column header is `[TOKEN] propagation` bracket notation. C-36: GATE-0 REQUIRED OUTPUTS table uses a dedicated third row ("Propagation contract" — R11 V-02 form) that independently carries the full propagation contract, making both layers (manifest column and GATE-0 table) fully self-contained with no cross-reference between them. A reader consulting only the manifest column learns the complete propagation architecture; a reader consulting only GATE-0's REQUIRED OUTPUTS table also learns the complete propagation architecture — neither layer is load-bearing for the other.
**Hypothesis:** C-33 PASS, C-34 PASS, C-35 PASS, C-36 PASS. The dedicated propagation row in GATE-0's REQUIRED OUTPUTS table satisfies C-31 independently — it explicitly names GATE-0 as the declaration site, names GATE-1+ as substitution/inheritance sites, and states the substitution rule, all without referencing the manifest. The manifest column satisfies C-32 independently with full prose and rubric vocabulary without referencing GATE-0's table. Belt-and-suspenders: each layer redundantly self-contained. Composite: 28/28 aspirational = 100.000.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

GATE-0 is the declaration site: TOKEN is committed to a domain-adaptive identifier in this gate. GATE-0's own REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed — and carries a dedicated Propagation contract row that names GATE-0 as the declaration site and GATE-1+ as substitution/inheritance sites. A reader consulting only GATE-0's REQUIRED OUTPUTS table can reconstruct the full propagation contract without reading the manifest. GATE-1 through GATE-4 are substitution/inheritance sites: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution. TOKEN carry-forward is a required output element for every gate after GATE-0. A reader consulting only this architecture block can also reconstruct the full propagation contract without reading either the manifest or per-gate tables.

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
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — TOKEN committed in this gate; GATE-0 is the declaration site** |
| Propagation contract — GATE-0 is the declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK → GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are substitution/inheritance sites — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest | **Contract — self-contained in this table; readable without consulting the manifest** |

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

| Variation | C-33 mechanism | C-34 mechanism | C-35 mechanism | C-36 mechanism | C-33 pred | C-34 pred | C-35 pred | C-36 pred | Asp pred | Composite pred |
|-----------|---------------|---------------|---------------|---------------|-----------|-----------|-----------|-----------|----------|----------------|
| **V-01** | "Declaration site" / "Substitution/inheritance site" verbatim in manifest cells; static `TOKEN propagation` header | None | None (static header) | None (compact Yes-cell) | PASS | FAIL | FAIL | FAIL | 25/28 | **98.929** |
| **V-02** | `DECLARE` / `INHERIT` shorthand in manifest cells | TOKEN-PROPAGATION ARCHITECTURE block before manifest | None (static header) | None (compact Yes-cell) | FAIL | PASS | FAIL | FAIL | 25/28 | **98.929** |
| **V-03** | `DECLARE` / `INHERIT` shorthand in manifest cells | None | `[TOKEN] propagation` bracket notation in manifest header + extended substitution rule | None (compact Yes-cell) | FAIL | FAIL | PASS | FAIL | 25/28 | **98.929** |
| **V-04** | "Declaration site" / "Substitution/inheritance site" verbatim; `[TOKEN] propagation` header | TOKEN-PROPAGATION ARCHITECTURE block before manifest | `[TOKEN] propagation` bracket notation in manifest header | Compact Yes-cell (independence uncertain) | PASS | PASS | PASS | ? | 27–28/28 | **99.643–100** |
| **V-05** | "Declaration site" / "Substitution/inheritance site" verbatim; `[TOKEN] propagation` header | TOKEN-PROPAGATION ARCHITECTURE block before manifest | `[TOKEN] propagation` bracket notation in manifest header | Dedicated Propagation contract row in GATE-0 table (R11 V-02 form); each layer independently complete | PASS | PASS | PASS | PASS | 28/28 | **100.000** |

**Predicted ranking:** V-01 = V-02 = V-03 = 98.929 < V-04 = 99.643 (or 100 if C-36 compact Yes-cell passes) < V-05 = 100.000

**If V-01 through V-03 are not separated by scorecards (all score same):** R13 criteria successfully isolate the three axes but model compliance on each is high enough that scorecards will not distinguish them. R14 may need to combine all four new criteria in a single variation and compare against V-05 belt-and-suspenders baseline.

**If V-04 passes C-36 (compact Yes-cell independently complete):** The dedicated propagation row (V-05) adds no structural value beyond the compact Yes-cell for C-36 purposes. R14 will need a criterion that tests independence more granularly — e.g., requiring each layer to name both the substitution rule AND the site vocabulary without any pointer to the other layer.

**If V-03 model output shows literal `[TOKEN] propagation` in manifest header:** R13 replicates the R12 V-04 finding — bracket-notation substitution is scoped to REQUIRED OUTPUTS column headers only. The pre-execution manifest is not an execution-time artifact; `[TOKEN]` placeholders in the manifest remain literal. This confirms that C-35 is a diagnostic separator: the model that produces the committed value in the manifest header has manifest-scoped substitution understanding; the model that outputs `[TOKEN] propagation` literally does not.
