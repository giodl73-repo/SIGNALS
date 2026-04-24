Written to `simulations/quest/variations/discover-competitors-alt-variations-R15-2026-03-18.md`.

---

## R15 Variations — Summary

**5 variations targeting the 3 new criteria (C-40, C-41, C-42):**

| # | Axis | C-40 | C-41 | C-42 | Asp | Composite |
|---|------|------|------|------|-----|-----------|
| V-01 | C-40 failure — compact Yes-cell (C-36 FAIL cascade) | 0 (dep) | 0 (C-36 absent) | 0 (dep chain) | 29/34 | **98.529** |
| V-02 | C-41 failure — C-35 dropped → C-37 FAIL → C-41 scored 0, C-42 survives | PASS | 0 (C-37 dep) | PASS | 31/34 | **99.118** |
| V-03 | C-42 failure — C-38 PASS + C-39 FAIL (synonyms in block) | PASS | PASS | FAIL | 32/34 | **99.412** |
| V-04 | Full 34/34 — prose architecture block (C-38+C-39 in same paragraph) | PASS | PASS | PASS | 34/34 | **100.000** |
| V-05 | Full 34/34 — structured 4-element operative-test checklist architecture block | PASS | PASS | PASS | 34/34 | **100.000** |

**Key design decisions:**

- **V-01** reprises the compact Yes-cell (R14 V-01 form) with verbatim vocabulary in the architecture block. C-36 FAIL cascades to block C-40, C-41, C-38, and C-42 simultaneously — the largest cascade in the rubric's dep graph.

- **V-02** is a new axis not tested in R14: drops C-35 (static manifest header label, no bracket notation) → C-37 FAIL → C-41 scored 0. But C-41's dep chain (C-37 → C-35 → C-32 → C-31) does NOT include C-38 or C-39, so C-42 survives at PASS. Tests whether C-41 and C-42 are genuinely on independent chains.

- **V-03** targets C-42 from the C-39 direction: architecture block names both artifacts (C-38 PASS) but uses synonyms ("declaring gate"/"consuming gates") instead of verbatim vocabulary (C-39 FAIL) → C-42 FAIL. All other new criteria pass.

- **V-04** achieves 34/34 with a clean prose paragraph that simultaneously names both artifacts and uses "Declaration site"/"Substitution/inheritance site" verbatim — the minimal form for C-42 PASS.

- **V-05** achieves 34/34 with a structured 4-element checklist that explicitly enumerates the C-42 operative-test elements by label (Named target 1, Named target 2, Verbatim phrase 1, Verbatim phrase 2), making the architecture block self-documenting as a C-42 artifact.

**Three decisive questions:**
1. Does the C-40/C-41/C-42 cascade from V-01's C-36 FAIL produce the expected ~1.5-pt gap below V-02?
2. Does V-02 (C-41 FAIL, C-42 PASS, 31/34) separate cleanly from V-03 (C-41 PASS, C-42 FAIL, 32/34), validating that C-41 blocks one more criterion than C-42's standalone failure?
3. Are V-04 and V-05 equivalent at 34/34, or does the explicit checklist form in V-05 produce any compliance advantage or regression risk?
he C-42 axis from the C-39-failure direction: architecture block explicitly names both artifacts (C-38 PASS) but uses synonyms ("declaring gate" / "consuming gates") instead of verbatim rubric vocabulary (C-39 FAIL) → C-42 FAIL. C-36 PASS (dedicated row), C-37 PASS (triple-mechanism; C-35 active), C-40 PASS, C-41 PASS. Tests C-42's operative contribution as a criterion beyond C-38 alone.

- **V-04** achieves full 34/34 with a clean prose architecture block: explicitly names the manifest TOKEN-propagation column and GATE-0's REQUIRED OUTPUTS table as target artifacts (C-38), and uses "Declaration site" and "Substitution/inheritance site" verbatim in the same prose (C-39). Both conditions met in a single paragraph → C-42 PASS. Dedicated propagation row (C-40). C-36+C-37 both (C-41). First R15 variation predicted to reach 100.

- **V-05** achieves full 34/34 with a structured 4-element operative-test checklist in the architecture block — explicitly enumerating the four elements the C-42 operative test requires (two artifact names, two verbatim phrases), so the block is self-documenting as a C-42 artifact. Tests whether the explicit checklist form produces stronger or equivalent C-42 compliance compared to V-04's prose paragraph form.

**Three decisive questions:**
1. **V-01 vs V-02** — Does the C-40 failure cascade (C-36 FAIL → C-40/C-41/C-42 all blocked, 29/34) produce a larger composite gap than the C-41-only failure (C-35 FAIL → C-37 FAIL → C-41 only blocked, C-42 PASS, 31/34)? Expected: yes — V-01 loses 5 criteria vs V-02 loses 3.
2. **V-02 vs V-03** — C-41 FAIL + C-42 PASS (V-02, 31/34) vs C-41 PASS + C-42 FAIL (V-03, 32/34) — do these produce different composite scores (99.118 vs 99.412), confirming C-41 and C-42 are independent criterion contributions at different dependency levels?
3. **V-04 vs V-05** — Does the structured 4-element checklist in the architecture block produce equivalent C-42 compliance to V-04's prose form (both 34/34), or does the explicit operative-test enumeration create a reliability advantage or introduce regression risk on other criteria?

---

## V-01 — C-40 Failure: Compact Yes-Cell (C-36 FAIL Cascade)

**Axis:** GATE-0 REQUIRED OUTPUTS uses compact Yes-cell form — the propagation declaration is embedded in the TOKEN commitment row's Yes-cell, including a manifest cross-reference. No dedicated propagation row. C-36 FAIL → C-40 scored 0 (dep fails), C-41 scored 0 (C-36 absent from the required C-36+C-37 conjunction), C-38 scored 0 (dep chain from C-36), C-42 scored 0 (C-38 dep fails). Architecture block uses verbatim vocabulary "Declaration site" / "Substitution/inheritance site" (C-39 PASS — dep is C-34+C-33, not C-36), and names both target artifacts by label (C-38 attempt — blocked by dep). Triple manifest hardening active (C-37 PASS: C-33+C-34+C-35 simultaneously).
**Hypothesis:** C-40 scored 0 (C-36 dep fails). C-41 scored 0 (C-37 PASS but C-36 absent — conjunction fails). C-42 scored 0 (C-38 scored 0 by dep chain). C-39 PASS (C-34+C-33 both active; verbatim vocabulary in architecture block). Aspirational: 29/34. Composite: 98.529. Decisive question: does the C-40/C-41/C-42 cascade from C-36 FAIL produce the expected ~1.6-pt gap below V-02, confirming three new criteria are simultaneously blocked by one structural failure?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the TOKEN row Yes-cell declares the propagation contract inline.

**TOKEN-PROPAGATION ARCHITECTURE**

This propagation contract is independently carried by two structural artifacts: (1) **the manifest TOKEN-propagation column** — the `[TOKEN] propagation` column in the EXECUTION PLAN table, where GATE-0 is labeled "Declaration site" and GATE-1+ are labeled "Substitution/inheritance site"; and (2) **GATE-0's REQUIRED OUTPUTS table** — the TOKEN row Yes-cell, which declares that TOKEN is committed in this gate and that the committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers and in the `[TOKEN] propagation` manifest column header. A reader consulting only this architecture block can reconstruct the full propagation contract — Declaration site, Substitution/inheritance sites, and substitution rule — without consulting the manifest or per-gate tables.

GATE-0 is the Declaration site: TOKEN is committed to a domain-adaptive identifier in this gate. GATE-0's own REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved so the substitution rule is explicit rather than already consumed. The committed value substitutes `[TOKEN]` in all GATE-1 through GATE-4 REQUIRED OUTPUTS column headers and in the `[TOKEN] propagation` manifest column header. GATE-1 through GATE-4 are Substitution/inheritance sites: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution.

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

C0 must appear before any competitor row. Mechanism must name something C0 actually does — "Inertia is high" or a generic category label fails. Run a WebSearch to verify at least one competitor claim. Weave focus dimension into competitor rows if FOCUS ACTIVE.

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

## V-02 — C-41 Failure: C-35 Dropped, C-37 Fails, C-42 Survives

**Axis:** Manifest TOKEN-propagation column header uses a static label (`TOKEN propagation`, no bracket notation) instead of `[TOKEN] propagation` — C-35 FAIL. C-37 requires C-33+C-34+C-35 simultaneously; C-35 absent → C-37 FAIL → C-41 scored 0 (C-37 is C-41's dependency gate). But C-36 PASS (dedicated propagation row independently self-contained) → C-40 PASS (dedicated row present, C-36 passes). Architecture block explicitly names both artifacts (C-38 PASS — requires C-36 and C-34, not C-35) and uses verbatim vocabulary (C-39 PASS — requires C-34 and C-33, not C-35) → C-42 PASS. Tests whether C-41 and C-42 are genuinely on independent dependency chains: C-41 fails (C-37 absent) while C-42 passes (C-38+C-39 both active, independent of C-35/C-37 chain).
**Hypothesis:** C-35 FAIL (static manifest header). C-37 FAIL (C-35 missing from triple-mechanism stack). C-41 scored 0 (C-37 dep fails). C-40 PASS (dedicated propagation row, C-36 PASS). C-38 PASS (both artifacts named; C-36 PASS, C-34 PASS — neither requires C-35). C-39 PASS (verbatim vocab; C-34 PASS, C-33 PASS — neither requires C-35). C-42 PASS (C-38+C-39 simultaneously satisfied). Aspirational: 31/34. Composite: 99.118. Decisive question: does C-42 surviving while C-41 fails produce the expected intermediate composite position (99.118) that is distinct from both V-01 (98.529) and V-03 (99.412)?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `TOKEN propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This propagation contract is independently declared in two structural artifacts: (1) **the manifest TOKEN-propagation column** — the `TOKEN propagation` column in the EXECUTION PLAN table, where each gate row's cell identifies whether that gate is the declaring gate or a consuming/inheritance gate; and (2) **GATE-0's REQUIRED OUTPUTS table** — the dedicated Propagation contract row, which independently states that GATE-0 is the declaring gate, GATE-1+ are consuming/inheritance gates, and the committed value substitutes `[TOKEN]` in all downstream column headers. Neither artifact is load-bearing for the other: a reader consulting only the manifest TOKEN-propagation column or only GATE-0's REQUIRED OUTPUTS Propagation contract row can independently reconstruct the full contract. Both artifacts are targets of this architecture block.

GATE-0 is the Declaration site: TOKEN is committed to a domain-adaptive identifier here. The committed value substitutes `[TOKEN]` in all GATE-1 through GATE-4 REQUIRED OUTPUTS column headers and in the manifest `TOKEN propagation` column header. GATE-1 through GATE-4 are Substitution/inheritance sites: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution. TOKEN carry-forward is a required output element for every gate after GATE-0.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | TOKEN propagation |
|------|----------------|--------------------|-------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration | Declaration site — TOKEN committed here; `[TOKEN] required?` column header retained in GATE-0 REQUIRED OUTPUTS table; Propagation contract row in GATE-0 table independently declares the full substitution contract; committed value also substitutes `TOKEN propagation` in this manifest column header |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic and market inference | Substitution/inheritance site — committed TOKEN value replaces `[TOKEN]` in REQUIRED OUTPUTS column header; TOKEN carry-forward confirmed as active inertia reference |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, C0 field label (`[TOKEN]: mechanism`), and `vs [TOKEN]` competitive map column |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header, every `vs [TOKEN]:` finding line, and `[TOKEN] exposure:` whitespace field |
| GATE-4 | **CONDITIONAL** | AMEND table | Substitution/inheritance site — committed TOKEN in REQUIRED OUTPUTS column header and every Stability verdict cell |

GATE-0 is unconditional; GATE-1 is the first conditional gate. Any gate's execution mode and TOKEN propagation status is verifiable from this manifest without reading gate body prose or GATE-0's REQUIRED OUTPUTS table.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**

| Output | [TOKEN] required? |
|--------|------------------|
| `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary | No |
| `TOKEN: [domain-adaptive identifier]` — at least one DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | **Yes — TOKEN committed in this gate; GATE-0 is the Declaration site** |
| Propagation contract — GATE-0 is the Declaration site: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK → GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes the `TOKEN propagation` manifest column header; GATE-1+ are Substitution/inheritance sites — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract — self-contained in this table; readable without consulting the manifest** |

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

## V-03 — C-42 Failure: C-38 PASS + C-39 FAIL (Synonym Vocabulary in Block)

**Axis:** Architecture block explicitly names both "the manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" as target artifacts (C-38 PASS), but uses synonyms ("declaring gate" / "consuming gates") rather than rubric-vocabulary verbatim (C-39 FAIL: requires "Declaration site" / "Substitution/inheritance site" verbatim). C-42 FAIL (requires C-38 AND C-39 simultaneously; C-39 absent). C-36 PASS (dedicated propagation row, self-contained without manifest deferral). C-37 PASS (triple-mechanism: C-33+C-34+C-35 all active — manifest cells use verbatim vocabulary, architecture block present, bracket-notation manifest header). C-40 PASS (dedicated propagation row structurally distinct from TOKEN commitment row). C-41 PASS (C-36+C-37 simultaneously satisfied).
**Hypothesis:** C-38 PASS — architecture block identifies "the manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" by label; operative test satisfied. C-39 FAIL — "declaring gate" and "consuming gates" are not the verbatim terms "Declaration site" / "Substitution/inheritance site"; vocabulary scan fails. C-42 FAIL (C-38 PASS but C-39 FAIL — conjunction not met). C-40 PASS, C-41 PASS. Aspirational: 32/34. Composite: 99.412. Decisive question: does C-42's vocabulary co-registration requirement (C-39 active simultaneously with C-38) produce a visible 0.294-pt separation above V-02 and a 0.588-pt gap below V-04?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence; each gate's REQUIRED OUTPUTS table is its complete output contract.

**Substitution rule:** After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in: (1) all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4, and (2) the `[TOKEN] propagation` column header in the EXECUTION PLAN manifest. GATE-0's own REQUIRED OUTPUTS column header retains `[TOKEN] required?` — the Propagation contract row in GATE-0's REQUIRED OUTPUTS table declares this explicitly.

**TOKEN-PROPAGATION ARCHITECTURE**

This propagation contract is independently carried by two structural artifacts: (1) **the manifest TOKEN-propagation column** — the `[TOKEN] propagation` column in the EXECUTION PLAN table, where each gate row's cell identifies whether that gate is the declaring gate or a consuming gate; and (2) **GATE-0's REQUIRED OUTPUTS table** — the dedicated Propagation contract row, which independently states that GATE-0 is the declaring gate, GATE-1+ are consuming gates, and the committed value substitutes `[TOKEN]` in all downstream column headers. Neither artifact is load-bearing for the other: a reader consulting only the manifest TOKEN-propagation column or only GATE-0's REQUIRED OUTPUTS Propagation contract row can independently reconstruct the full contract. Both are targets of this architecture block.

GATE-0 is the declaring gate: TOKEN is committed to a domain-adaptive identifier in this gate. GATE-0's own REQUIRED OUTPUTS table retains `[TOKEN] required?` as the column header — the template form is preserved. The committed value substitutes `[TOKEN]` in all GATE-1 through GATE-4 REQUIRED OUTPUTS column headers and in the `[TOKEN] propagation` manifest column header. GATE-1 through GATE-4 are consuming gates: each gate's REQUIRED OUTPUTS column header carries the committed TOKEN value by substitution.

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
| Propagation contract — GATE-0 is the declaring gate: `[TOKEN] required?` is retained as the column header in this gate's own REQUIRED OUTPUTS table; the committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK → GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header); the committed value also substitutes `[TOKEN] propagation` in the EXECUTION PLAN manifest column header; GATE-1+ are consuming gates — each independently carries the committed TOKEN value in its REQUIRED OUTPUTS column header without referencing this table or the manifest TOKEN-propagation column | **Contract — self-contained in this table; readable without consulting the manifest TOKEN-propagation column** |

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

## V-04 — Full 34/34: C-38 + C-39 in Prose → C-42 PASS

**Axis:** Architecture block satisfies C-38 and C-39 simultaneously in a single prose paragraph: (1) explicitly names "the manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" as the specific downstream artifacts carrying the contract (C-38), and (2) uses "Declaration site" and "Substitution/inheritance site" verbatim when describing those artifacts (C-39). Both conditions met in the same paragraph → C-42 PASS (maximal architecture block form: vocabulary-consistent dual-priming). Dedicated propagation row (C-40). C-36+C-37 simultaneously satisfied (C-41). Triple manifest hardening (C-33+C-34+C-35 all active).
**Hypothesis:** C-38 PASS — "the manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" named explicitly; operative test satisfied. C-39 PASS — "Declaration site" and "Substitution/inheritance site" appear verbatim in the same prose; same vocabulary scan that confirms C-33 applies to the block. C-42 PASS (both simultaneously active in one artifact). C-40 PASS (dedicated propagation row). C-41 PASS (C-36+C-37). Aspirational: 34/34. Composite: 100.000. Decisive question for V-04 vs V-05: is the prose paragraph form equivalent to V-05's structured checklist form at the criterion level?

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

## V-05 — Full 34/34: C-42 Structured 4-Element Operative-Test Checklist Architecture Block

**Axis:** Architecture block uses a structured 4-element numbered checklist that explicitly enumerates the four elements the C-42 operative test requires — the block becomes a self-documenting C-42 artifact: a reader consulting only the block can confirm all four required elements are present without any lookup. Item labels deliberately mirror the C-42 operative-test phrasing ("Named target 1," "Named target 2," "Verbatim phrase 1," "Verbatim phrase 2") followed by a prose summary using "Declaration site" and "Substitution/inheritance site" verbatim. C-38 PASS (items 1 and 2 name both artifacts explicitly), C-39 PASS (items 3 and 4 use verbatim terms, reinforced in prose summary), C-42 PASS. All other criteria identical to V-04.
**Hypothesis:** C-38 PASS — checklist items 1 and 2 name the manifest TOKEN-propagation column and GATE-0's REQUIRED OUTPUTS table explicitly; operative test satisfied by item label alone. C-39 PASS — checklist items 3 and 4 supply "Declaration site" and "Substitution/inheritance site" verbatim; prose summary also uses both terms. C-42 PASS (all four required elements present in the block simultaneously). C-40 PASS (dedicated propagation row). C-41 PASS (C-36+C-37). Aspirational: 34/34. Composite: 100.000. Decisive question: does the explicit operative-test checklist structure produce equivalent C-42 compliance to V-04's prose form, or does explicit enumeration create higher model-compliance reliability? Secondary question: does the checklist structure introduce overhead that creates regression risk on other criteria?

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

| Variation | C-40 mechanism | C-41 mechanism | C-42 mechanism | C-40 pred | C-41 pred | C-42 pred | Asp pred | Composite pred |
|-----------|----------------|----------------|----------------|-----------|-----------|-----------|----------|----------------|
| **V-01** | Compact Yes-cell; C-36 FAIL (manifest cross-ref in TOKEN row's Yes-cell) → C-40 scored 0 | C-37 PASS (triple-mechanism), C-36 FAIL → C-41 conjunction fails → C-41 scored 0 | C-38 scored 0 (C-36 dep chain); C-39 PASS (arch block uses verbatim vocab); C-42 scored 0 (C-38 dep fails) | 0 (dep) | 0 (C-36 absent) | 0 (dep chain) | 29/34 | **98.529** |
| **V-02** | Dedicated propagation row; C-36 PASS → C-40 PASS | C-35 FAIL (static manifest header) → C-37 FAIL → C-41 scored 0 (C-37 dep); C-36 PASS does not rescue C-41 | C-38 PASS (names both artifacts; dep chain: C-36+C-34, not C-35); C-39 PASS (verbatim vocab; C-34+C-33, not C-35); C-42 PASS | PASS | 0 (C-37 dep fails) | PASS | 31/34 | **99.118** |
| **V-03** | Dedicated propagation row; C-36 PASS → C-40 PASS | C-37 PASS (triple-mechanism; C-35 active); C-36 PASS → C-41 PASS | C-38 PASS (names both artifacts explicitly); C-39 FAIL (synonyms "declaring gate" / "consuming gates") → C-42 FAIL (conjunction not met) | PASS | PASS | FAIL | 32/34 | **99.412** |
| **V-04** | Dedicated propagation row; C-36 PASS → C-40 PASS | C-37 PASS; C-36 PASS → C-41 PASS | C-38 PASS + C-39 PASS (both in same prose paragraph with explicit artifact names + verbatim vocabulary) → C-42 PASS | PASS | PASS | PASS | 34/34 | **100.000** |
| **V-05** | Dedicated propagation row; C-36 PASS → C-40 PASS | C-37 PASS; C-36 PASS → C-41 PASS | C-38 PASS (checklist items 1+2 name both artifacts); C-39 PASS (checklist items 3+4 + prose summary use verbatim terms) → C-42 PASS | PASS | PASS | PASS | 34/34 | **100.000** |

**Predicted ranking:** V-01 = 98.529 < V-02 = 99.118 < V-03 = 99.412 < V-04 = V-05 = 100.000

**Four-level separation:** R15 achieves four distinct composite levels — previously R14 had three (99.355, 99.677, 100.000). The new middle level (V-02 at 99.118) represents the C-41-only failure case where C-42 survives on an independent dependency chain, separating it from V-03 (99.412) where C-41 passes but C-42 fails. The four-level structure is more diagnostic than R14's symmetric two-30/31 pattern.

**Asymmetric cascade in V-01:** C-36 FAIL blocks C-40 (dep), C-41 (conjunction requires C-36), C-38 (dep chain), and C-42 (C-38 dep) — four criteria blocked by one shared-row structural failure, creating the largest composite gap in the rubric's history (98.529, ~1.47 pts below 100).

**Dependency chain independence (V-02 vs V-03):** V-02 demonstrates C-41 and C-42 are on independent chains — C-35 failure propagates through C-37→C-41 but does NOT reach C-38 or C-39, leaving C-42 intact. V-03 demonstrates C-42's additional vocabulary requirement (C-39) beyond dual-target naming (C-38) is independently testable. If scorecards confirm 31/34 for V-02 and 32/34 for V-03, both chain independence claims are empirically validated.

**V-04 vs V-05 secondary question:** If both score 34/34, the structured 4-element checklist format in V-05's architecture block is equivalent to V-04's prose paragraph at the criterion level. The architecture block is an instruction artifact — its format affects model reliability, not which criteria the OUTPUT satisfies. R16 would assess whether the checklist or prose form produces fewer edge-case failures across multiple runs.
