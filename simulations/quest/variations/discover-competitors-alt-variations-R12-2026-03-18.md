Written to `simulations/quest/variations/discover-competitors-alt-variations-R12-2026-03-18.md`.

---

## R12 Variations — Summary

**Single axis:** How the manifest TOKEN-propagation column (C-32) distinguishes GATE-0 as the declaration site from GATE-1+ as substitution/inheritance sites. All 5 carry C-31 (R11 V-04 compact cell form) except V-05, which uses the R11 V-02 dedicated row for maximum dual-layer coverage.

| # | Axis | Manifest TOKEN-propagation column | C-32 pred | Composite pred |
|---|------|-----------------------------------|-----------|----------------|
| V-01 | Binary `DECLARE` / `INHERIT` labels | `DECLARE — committed here; propagates to GATE-1+` / `INHERIT — committed TOKEN substituted` | PASS | 100 |
| V-02 | Full prose per cell (rubric vocabulary) | Sentence per cell using "declaration site" / "substitution/inheritance site" | PASS | 100 |
| V-03 | Pre-manifest contract block + compact `DECLARE` / `SUBSTITUTE` labels | TOKEN-PROPAGATION ARCHITECTURE block before manifest + compact labels in manifest column | PASS | 100 |
| V-04 | Bracket notation in manifest column header `[TOKEN] propagation` | Column header participates in bracket-substitution lifecycle; extended substitution rule | PASS | 100 |
| V-05 | Maximum dual-layer: verbose manifest + dedicated GATE-0 propagation row | Full prose manifest column (V-02 style) + R11 V-02 dedicated row in GATE-0 table | PASS | 100 |

**All 5 predicted 100.** C-32 appears non-separating at this level — any reasonable implementation of the manifest TOKEN-propagation column should satisfy it. The decisive questions are:

1. **V-01** — Does `INHERIT` vocabulary satisfy C-32's "substitution/inheritance sites" clause, or does "substitution" need to appear explicitly?
2. **V-04** — Does the model substitute the committed value into `[TOKEN] propagation` in the manifest column header, or output it literally (revealing substitution is scoped to REQUIRED OUTPUTS tables only)?
3. **All-5-pass case** — If no separation occurs, R13 will need a stricter criterion: e.g., manifest column must carry both a STATUS label (DECLARE/SUBSTITUTE) and a SCOPE field naming which output artifacts TOKEN appears in per gate.
ight enough?
2. **V-01 vs V-02** — Does verbose prose (rubric vocabulary echoed verbatim) vs compact binary labels produce different model compliance, or are both equally reliable?
3. **V-03** — Does a pre-manifest TOKEN-PROPAGATION ARCHITECTURE block prime model compliance with correct compact column content, or is it redundant noise the compact column already handles?
4. **V-04** — Does bracket notation in the manifest column header cause the model to substitute the committed value there, or does it output `[TOKEN] propagation` literally (revealing that substitution is scoped to REQUIRED OUTPUTS tables only)?

---

## V-01 — Binary DECLARE / INHERIT Labels in Manifest TOKEN Column

**Axis:** Manifest TOKEN-propagation column uses two-value binary vocabulary: `DECLARE` for GATE-0 (declaration site) and `INHERIT` for GATE-1+ (substitution/inheritance sites). Per-cell content is compact with a brief rationale clause.
**Hypothesis:** C-32 PASS — `DECLARE` names GATE-0 as the declaration site; `INHERIT` names GATE-1+ as substitution/inheritance sites. Minimal but unambiguous. The manifest column satisfies C-32's operative test (a reader consulting only the manifest can identify which gate declares and which consume by substitution) without prose overhead. Decisive test: does `INHERIT` satisfy "substitution/inheritance site" or does the rubric require the word "substitution" to appear?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the TOKEN row Yes-cell declares the propagation contract.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | TOKEN propagation |
|------|----------------|--------------------|-------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | DECLARE — TOKEN committed here; committed value propagates to GATE-1+ REQUIRED OUTPUTS column headers by substitution |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | INHERIT — committed TOKEN substituted into REQUIRED OUTPUTS column header; carry-forward active |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | INHERIT — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label, `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | INHERIT — committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` line, `[TOKEN] exposure:` field |
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

## V-02 — Full Prose Per Manifest Cell (Rubric Vocabulary)

**Axis:** Manifest TOKEN-propagation column uses a full sentence per cell with "declaration site" / "substitution/inheritance site" language that echoes C-32's exact operative test vocabulary. The GATE-0 cell also names the `[TOKEN] required?` column header retention and the substitution rule in one clause — making the manifest column independently sufficient to understand the complete propagation architecture.
**Hypothesis:** C-32 PASS — the rubric says "GATE-0 is identified as the declaration site, and GATE-1+ are identified as substitution/inheritance sites." V-02 echoes that language verbatim in every relevant cell. Most verbose manifest form. Should produce the most reliable model compliance because the column cells pre-answer the C-32 operative test without inference. Decisive question: does V-02 prose produce meaningfully different model behavior vs V-01 binary labels, or are both equally reliable?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the TOKEN row Yes-cell declares the propagation contract.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | TOKEN propagation |
|------|----------------|--------------------|-------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
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

## V-03 — Pre-Manifest TOKEN-PROPAGATION ARCHITECTURE Block + Compact DECLARE / SUBSTITUTE Labels

**Axis:** An explicit labeled TOKEN-PROPAGATION ARCHITECTURE block is declared before the EXECUTION PLAN table. The block names GATE-0 as the declaration site and GATE-1+ as substitution/inheritance sites in full prose. The manifest then uses compact labels (`DECLARE` / `SUBSTITUTE`) in the TOKEN propagation column — redundant with the block but satisfying C-32's "dedicated column in the manifest" structural requirement independently.
**Hypothesis:** C-32 PASS — the manifest column is present with compact labels satisfying the "dedicated column" requirement. The pre-manifest block is architecture-level priming that makes the propagation contract visible before even reading the manifest. Decisive question: does declaring the propagation architecture in a standalone block before the manifest table prime model compliance with correct compact column content, or is it redundant noise the column handles alone?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the TOKEN row Yes-cell declares the propagation contract.

**TOKEN-PROPAGATION ARCHITECTURE (declared before execution begins):**
- GATE-0 [declaration site]: TOKEN is committed to a domain-adaptive identifier in this gate. `[TOKEN] required?` is retained as the template column header in GATE-0's own REQUIRED OUTPUTS table. The committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers.
- GATE-1 through GATE-4 [substitution/inheritance sites]: Each gate's REQUIRED OUTPUTS column header uses the committed TOKEN value by substitution. TOKEN carry-forward is required in every gate output. A reader consulting the manifest TOKEN propagation column can verify each gate's role without reading per-gate REQUIRED OUTPUTS tables or gate body prose.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | TOKEN propagation |
|------|----------------|--------------------|-------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | DECLARE (declaration site) — TOKEN committed; `[TOKEN] required?` retained in GATE-0 REQUIRED OUTPUTS column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | SUBSTITUTE (substitution/inheritance site) — committed TOKEN in REQUIRED OUTPUTS column header |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | SUBSTITUTE (substitution/inheritance site) — committed TOKEN in REQUIRED OUTPUTS column header |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | SUBSTITUTE (substitution/inheritance site) — committed TOKEN in REQUIRED OUTPUTS column header |
| GATE-4 | **CONDITIONAL** | AMEND table | SUBSTITUTE (substitution/inheritance site) — committed TOKEN in REQUIRED OUTPUTS column header |

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

## V-04 — Bracket Notation `[TOKEN] propagation` in Manifest Column Header

**Axis:** The manifest TOKEN-propagation column header uses bracket notation — `[TOKEN] propagation` — extending the substitution contract from REQUIRED OUTPUTS column headers to the EXECUTION PLAN manifest column header itself. The preamble substitution rule is explicitly extended to cover the manifest column header: after GATE-0 commits (e.g., TOKEN = SIGNAL-LOCK), the manifest column header also substitutes to `SIGNAL-LOCK propagation`. Per-cell content uses intermediate prose (declaration site / substitution/inheritance site vocabulary).
**Hypothesis:** C-32 PASS — the manifest column is present and distinguishes declaration from substitution sites. The bracket notation in the column header is an architectural consistency bonus: `[TOKEN]` notation propagates uniformly across every structural artifact (manifest and REQUIRED OUTPUTS tables alike). Decisive question: does the model correctly substitute the committed TOKEN value into the manifest column header, or does it output `[TOKEN] propagation` literally — revealing that bracket-notation substitution is scoped to REQUIRED OUTPUTS tables only and does not extend to the pre-execution manifest?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the TOKEN row Yes-cell declares the propagation contract. After GATE-0 commits (e.g., TOKEN = SIGNAL-LOCK), this manifest column header also becomes `SIGNAL-LOCK propagation`.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | [TOKEN] propagation |
|------|----------------|--------------------|---------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` retained in GATE-0 REQUIRED OUTPUTS column header; committed value propagates to GATE-1+ REQUIRED OUTPUTS column headers and to this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward active |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label, and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, findings lines, and whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header and Stability verdict cells |

GATE-0 is unconditional; GATE-1 is the first conditional gate. `[TOKEN] propagation` in the column header substitutes to the committed value after GATE-0 commits. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose.

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

## V-05 — Maximum Dual-Layer: Verbose Manifest Column + Dedicated GATE-0 Propagation Row

**Axis:** Combines (1) R11 V-02 pattern — dedicated third row "Propagation contract" in GATE-0's own REQUIRED OUTPUTS table, and (2) V-02 verbose manifest column style. Both artifacts independently satisfy C-31 (GATE-0 table row) and C-32 (manifest column). A reader consulting only the manifest learns the full propagation architecture (C-32); a reader consulting only GATE-0's REQUIRED OUTPUTS table also finds the complete declaration and propagation contract (C-31). Neither artifact requires the other.
**Hypothesis:** C-31 PASS (dedicated propagation row in GATE-0 table — same as R11 V-02); C-32 PASS (verbose manifest column — same as V-02). Maximum redundancy across both structural layers. Should be the canonical R12 maximum-score form: both the per-gate declaration (C-31) and the manifest-level declaration (C-32) are independently verifiable from their respective artifacts, with no cross-reference required.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract. In every REQUIRED OUTPUTS table after GATE-0: `[TOKEN] required?` is a column header placeholder — substitute the committed TOKEN value (from GATE-0) in all gates after GATE-0.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | TOKEN propagation |
|------|----------------|--------------------|-------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers; propagation contract is self-contained in GATE-0's own REQUIRED OUTPUTS table |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — TOKEN committed in this gate** |
| Propagation contract — `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK → GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); GATE-0 is the declaration site; GATE-1+ are substitution/inheritance sites | **Contract — readable from this table in isolation** |

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

| Variation | C-31 mechanism | C-32 mechanism | C-31 pred | C-32 pred | Asp pred | Composite pred |
|-----------|----------------|----------------|-----------|-----------|----------|----------------|
| **V-01** | TOKEN row Yes-cell: "Yes — GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ column headers" | Manifest `TOKEN propagation` column with `DECLARE` / `INHERIT` binary labels + brief rationale clauses | PASS | PASS | 24/24 | **100.000** |
| **V-02** | TOKEN row Yes-cell: same as V-01 | Manifest `TOKEN propagation` column with full prose per cell using "declaration site" / "substitution/inheritance site" vocabulary | PASS | PASS | 24/24 | **100.000** |
| **V-03** | TOKEN row Yes-cell: same as V-01 | Pre-manifest TOKEN-PROPAGATION ARCHITECTURE block + manifest column with `DECLARE` / `SUBSTITUTE` labels + parenthetical site labels | PASS | PASS | 24/24 | **100.000** |
| **V-04** | TOKEN row Yes-cell: same as V-01 but also names manifest column header substitution | Manifest `[TOKEN] propagation` column header (bracket notation); per-cell prose with "declaration site" / "substitution/inheritance site" vocabulary | PASS | PASS | 24/24 | **100.000** |
| **V-05** | GATE-0 REQUIRED OUTPUTS table: dedicated 3rd row "Propagation contract" with full substitution rule and site labels (R11 V-02 form) | Manifest `TOKEN propagation` column with full prose per cell (V-02 style) | PASS | PASS | 24/24 | **100.000** |

**Predicted ranking:** V-01 = V-02 = V-03 = V-04 = V-05 = **100** (all 5 predicted to satisfy C-31 and C-32)

**If V-01 passes C-32 with DECLARE/INHERIT labels:** R12 learning — binary vocabulary satisfies "explicitly declares TOKEN's status for each gate" at the minimum form. `INHERIT` = inheritance site is sufficient; the rubric's "substitution/inheritance sites" phrasing is inclusive of both SUBSTITUTE and INHERIT as valid label vocabulary.

**If V-01 fails C-32 (INHERIT insufficient):** R12 learning — C-32 requires "substitution" to appear explicitly in GATE-1+ manifest cells. `INHERIT` alone does not satisfy "GATE-1+ are identified as substitution/inheritance sites" because the substitution path is not named. V-02 and V-05 would still pass via "substitution/inheritance site" prose; V-01 would reveal the vocabulary floor for C-32.

**If V-04 model output shows literal `[TOKEN] propagation` in manifest column header:** R12 learning — bracket-notation substitution is scoped to REQUIRED OUTPUTS column headers only. The model does not extend the substitution contract to the pre-execution manifest column header because the manifest is produced before TOKEN is committed. The manifest is a template; the REQUIRED OUTPUTS tables are execution-time artifacts. Bracket substitution is an execution-time mechanism, not a template mechanism.

**If all 5 score 100 (expected):** C-32 is additive but non-separating at this level. All reasonable implementations of the manifest TOKEN-propagation column satisfy C-32. R13 will need a stricter criterion — e.g., requiring the manifest column to carry both a STATUS label (DECLARE/SUBSTITUTE) and a SCOPE field naming which output artifacts TOKEN appears in per gate — to separate further.
