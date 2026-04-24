Golden prompt written to `simulations/quest/golden/discover-competitors-alt-golden-2026-03-18.md`.

**What's in the file:**

- **Frontmatter** — skill, target, date, rounds: 20, rubric v20, score: 100.0, status: GOLDEN
- **Winning prompt body** — V-01 verbatim (3-row table preamble, `(Element N)` annotations, full GATE-0 through GATE-4 with REQUIRED OUTPUTS tables)
- **What made it golden** — 5 patterns:
  1. 3-row bijective preamble table as the minimal C-47+C-48 co-satisfying form
  2. "Preamble IS the table" — the C-47 operative test resolves cleanly with no prose sentence needed
  3. Explicit symbol-to-position mapping in row 3 eliminates convention dependency (C-50)
  4. DOMAIN-TERMS as a forced intermediate output artifact before TOKEN construction
  5. Belt-and-suspenders propagation contract — dual-layer independence, neither layer load-bearing for the other
- **Rubric criteria summary** — 5 Essential / 3 Recommended / 42 Aspirational, organized by chain (TOKEN identity, AMEND contract, REQUIRED OUTPUTS architecture, manifest hardening, bijective checklist), with C-49/C-50 highlighted as v20 additions
 content by definition.

**3. Explicit symbol-to-position mapping in row 3 eliminates convention dependency (C-50).**
Row 3 declares `(Element N)` form and maps its symbol set {1,2,3,4} to the four-position element-index set explicitly — not by convention. A reader consulting only the table can verify bijection from the annotations alone without domain knowledge. This pattern holds across annotation styles (Element N, Roman numeral, Ei) and closes the final gap between C-49 (row present) and C-50 (table self-contained).

**4. DOMAIN-TERMS extraction as a forced intermediate output artifact.**
GATE-0 requires DOMAIN-TERMS to be written and closed on its own line before TOKEN is constructed. This forces the model to commit vocabulary from repo context (README, CLAUDE.md, package.json) as an explicit artifact — not embed vocabulary selection silently inside TOKEN construction. Domain-specificity of the token identifier is verifiable from the DOMAIN-TERMS line alone (C-18).

**5. Belt-and-suspenders propagation contract — neither layer load-bearing for the other.**
The TOKEN propagation contract is declared at two independent structural layers: (1) the manifest `[TOKEN] propagation` column with verbatim "Declaration site" / "Substitution/inheritance site" cell vocabulary, and (2) GATE-0's REQUIRED OUTPUTS table with a dedicated Propagation contract row. Each layer satisfies its criterion independently with no cross-reference between them. The TOKEN-PROPAGATION ARCHITECTURE block primes both layers explicitly before the manifest table appears (C-34 through C-42 chain).

---

## Winning Prompt Body

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

## Final Rubric Criteria Summary (v20)

**Score: 100.000 | 20 rounds | 50 criteria total**

| Tier | Count | Weight | Points each |
|------|-------|--------|-------------|
| Essential | 5 | 60 pts | 12.000 |
| Recommended | 3 | 30 pts | 10.000 |
| Aspirational | 42 | 10 pts | 0.238 |

### Essential (C-01 to C-05)

| ID | Criterion |
|----|-----------|
| C-01 | C0 named before competitors |
| C-02 | 3+ named competitors with explicit threat levels (HIGH / MEDIUM / LOW) |
| C-03 | C0 at row 0 in competitive map table |
| C-04 | Grounded findings — each references a named competitor row by label |
| C-05 | AMEND section present and non-empty |

### Recommended (C-06 to C-08)

| ID | Criterion |
|----|-----------|
| C-06 | Mechanism-level inertia reasoning — switching cost / habit lock-in / workaround satisfaction tied to specific C0 behavior |
| C-07 | Web-verified competitive claim with inline citation within the competitor entry |
| C-08 | AMEND section with input-to-output pairs — 3+ rows, input change + output effect both named |

### Aspirational (C-09 to C-50)

**TOKEN identity chain (C-13 -> C-17 -> C-18 -> C-15 -> C-19 -> C-21):**
Domain-specific portable token declared before C0 prose; DOMAIN-TERMS extraction as a prior output artifact; token pre-declared before any conditional or procedural logic; unconditional gate names its conditional successor.

**AMEND contract chain (C-08 -> C-12 -> C-14 -> C-16 -> C-20 -> C-22):**
Every AMEND entry addresses TOKEN stability; schema enumerates all four domain-neutral components by name; evidence logically distinct from verdict in every row; naive reader can identify each component from label alone.

**REQUIRED OUTPUTS architecture chain (C-25 -> C-26 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31):**
Per-gate REQUIRED OUTPUTS blocks as native markdown tables; TOKEN-required column present; bracket-notation substitution rule declared; GATE-0 retains `[TOKEN] required?` template form with explicit Propagation contract row; completion conditions fully replaced.

**Manifest hardening chain (C-23 -> C-24 -> C-32 -> C-33 -> C-34 -> C-35 -> C-36 -> C-37 -> C-38 -> C-39):**
Pre-execution native markdown manifest enumerates all gates before any runs; `[TOKEN] propagation` column with verbatim "Declaration site" / "Substitution/inheritance site" cell vocabulary; TOKEN-PROPAGATION ARCHITECTURE block precedes manifest; dual-layer independence — manifest column and GATE-0 table each independently complete (C-36); full triple-mechanism hardening (C-37); architecture block explicitly primes both manifest column and GATE-0 table as named targets (C-38); vocabulary co-registration between block prose and manifest cells (C-39).

**Bijective checklist chain (C-43 -> C-44 -> C-45 -> C-46 -> C-47 -> C-48 -> C-49 -> C-50):**
Exactly 4 labeled items; one C-42 element per item (bijective); element-index annotations; preamble declared before checklist; preamble is a 3-row native markdown table; row 3 names annotation form and maps symbol set to four-position index set; annotation form occupies a dedicated table row (C-49); table constitutes a complete self-contained bijective contract — explicit symbol-to-position mapping eliminates convention dependency (C-50).

**New in v20 (C-49, C-50):** Closes the gap between annotation-form row present (C-49) and explicit mapping in that row (C-50). Stable across annotation styles (Element N, Roman numeral, Ei), item compression, and register shift.
