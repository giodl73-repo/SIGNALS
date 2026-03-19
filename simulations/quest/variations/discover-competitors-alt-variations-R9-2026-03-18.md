Here are the R9 variations for `discover-competitors-alt`:

---

### R9 context

R8 all-five scored 100 (17/17 aspirational). The key insight: REQUIRED OUTPUTS blocks are the most unambiguous C-25 form — R8 V-04 introduced them and R9 C-26 codifies that pattern as mandatory. R8 V-01/V-02/V-03 (completion-condition prose only) would now fail C-26.

---

### Variation summary

| # | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Inertia framing — blocks replace completion conditions | REQUIRED OUTPUTS blocks are self-sufficient; completing conditions are redundant |
| **V-02** | Output format — REQUIRED OUTPUTS as native markdown tables | Table format improves extractability; format-agnostic within "dedicated block" class |
| **V-03** | Lifecycle emphasis — REQUIRED OUTPUTS blocks trailing (after body prose) | **Critical position test** — does trailing placement fail C-26's "extractable without reading prose"? |
| **V-04** | Role sequence — lean gate bodies; REQUIRED OUTPUTS dominant | Minimal prose maximizes structural dominance of blocks |
| **V-05** | Combined — table blocks + manifest column + completion conditions retained | Triple-source TOKEN declaration (block + manifest + completion condition) |

**Predicted:** V-01, V-02, V-04, V-05 → **100**. V-03 → **99.444** (trailing position likely fails C-26's extractability standard).

**The decisive R9 question:** Does trailing REQUIRED OUTPUTS position satisfy C-26? If it fails, position (leading vs. trailing) becomes a structural constraint. If it passes, C-26 is location-agnostic within the gate.
les within each gate | Does table format for REQUIRED OUTPUTS improve structural extractability for C-26 vs. numbered list? |
| **V-03** | Lifecycle emphasis | REQUIRED OUTPUTS blocks trail each gate (after body prose) | Does trailing position satisfy C-26's "extractable without reading prose" — or does position matter? |
| **V-04** | Role sequence | Lean gate bodies — REQUIRED OUTPUTS block is primary content; prose reduced to one sentence | Does maximally lean body prose expose any hidden criterion dependencies on body prose content? |
| **V-05** | Combined | Table REQUIRED OUTPUTS + manifest "Required outputs" column + completion conditions retained | Does triple-source TOKEN declaration add structural resilience or create conflicting specification risk? |

**Predicted:** V-01, V-02, V-04, V-05 all at **100** (18/18 aspirational).
V-03 is the structural risk — trailing REQUIRED OUTPUTS blocks may fail C-26's "extractable without reading prose" test, scoring 17/18 aspirational (composite **99.444**).

**Decisive questions for R9 scorecard:**
1. V-01: Does removing completion conditions hurt any criterion (e.g., C-25, which in R8 used completion conditions as the output spec)?
2. V-03: Does trailing REQUIRED OUTPUTS position fail C-26's extractability standard? This is the critical new structural question for R9.
3. V-02/V-05: Does table format for REQUIRED OUTPUTS produce any C-26 advantage vs. numbered-list format?
4. V-04: Does lean-body design expose any criterion that required body prose for its evidence?
5. V-05: Does retaining completion conditions alongside REQUIRED OUTPUTS tables create conflicting specs or simply add robustness?

---

## V-01 — Inertia framing: REQUIRED OUTPUTS blocks replace completion conditions entirely

**Axis:** REQUIRED OUTPUTS blocks as the sole output specification per gate — completion conditions removed. In R8 V-04, gates had both REQUIRED OUTPUTS blocks AND completion conditions; C-25 used the completion-condition text as the output spec. R9 V-01 eliminates completion conditions entirely: the REQUIRED OUTPUTS block bears full weight for both C-25 and C-26.
**Hypothesis:** Removing completion conditions eliminates structural ambiguity about which artifact is "the gate's output specification" for C-25/C-26. If V-01 passes at 100, REQUIRED OUTPUTS blocks are self-sufficient output specifications. If any criterion drops, it identifies what completion conditions provided that blocks alone cannot.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations |
|------|----------------|--------------------|
| GATE-0 | UNCONDITIONAL — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference |
| GATE-2 | CONDITIONAL | C0 description, competitive map |
| GATE-3 | CONDITIONAL | Findings, whitespace |
| GATE-4 | CONDITIONAL | AMEND table |

GATE-0 is unconditional and executes first, always. GATE-1 is the first gate where conditional operations execute. Any gate's execution mode is verifiable in this plan without reading its body.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

This gate is unconditional. No conditional branching, focus detection, or section structure precedes or runs during it. GATE-1 is the first gate with conditional logic.

**Required outputs:**
1. `DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]` — closed on its own line before TOKEN; 2–3 product-domain expert terms from repo context (README, CLAUDE.md, package.json); not generic software vocabulary
2. `TOKEN: [domain-adaptive identifier]` — must include at least one DOMAIN-TERMS term; copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails; declared before all competitive content and all conditional logic; TOKEN appears by this declared value in every gate's Required outputs block below

Write exactly these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL — first conditional gate, focus detection and topic resolution]

Read repo context. Do not ask the user for topic, competitors, or market category.

**Required outputs:**
1. `FOCUS: ACTIVE — [dimension] | INACTIVE`
2. `TOPIC: [inferred product domain]`
3. `MARKET: [inferred market category]`
4. TOKEN (value = TOKEN from GATE-0) — active inertia reference; required by its declared value in GATE-2, GATE-3, and GATE-4 Required outputs

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

C0 must appear before any competitor row. Mechanism must tie to a real C0 behavior or feature — "Inertia is high" without a product-specific anchor fails. Run a WebSearch to verify at least one competitor claim.

**Required outputs:**
1. C0 section (before any competitor row): `## C0 — [product name]` / `[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior or feature]`
2. Competitive map (native markdown table, pipe-and-hyphen, no code fence): row 0 = C0; `vs [TOKEN]` column header uses TOKEN by its declared value; min 3 named external competitors; explicit threat levels (HIGH/MEDIUM/LOW); min 1 inline WebSearch citation
3. TOKEN appears by declared value in: C0 section label, `vs [TOKEN]` column header, and each competitor row's TOKEN comparison cell

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

Findings must reference named competitor rows by table label — findings readable without GATE-2 fail. TOKEN appears by its declared value, not by role description.

**Required outputs:**
1. 3 findings: each references a named competitor row by table label; each includes `vs [TOKEN]:` line with TOKEN by its declared value
2. Whitespace finding: specific uncontested dimension (not generic) + `[TOKEN] exposure:` field naming TOKEN by declared value
3. If FOCUS ACTIVE: cross-dimensional whitespace finding naming the gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by table label]
vs [TOKEN]: [how this finding relates to TOKEN mechanism — TOKEN by declared value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [how TOKEN mechanism relates to this gap — TOKEN by name]
```

If FOCUS ACTIVE: gap must require both the competitive map and the focus lens to produce; show the intersection.

---

### GATE-4 [CONDITIONAL — AMEND]

**Required outputs:**
1. AMEND schema declared before data rows — all four domain-neutral component names enumerated: Input change, Output effect, Stability verdict, Evidence
2. Min 3 data rows: every Stability verdict cell names TOKEN by its declared value; every Evidence cell contains reasoning distinct from verdict — "Stable." alone fails
3. TOKEN appears by declared value in every Stability verdict cell

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts — focus dimension, depth level, competitor scope] | [which gate or section specifically shifts — name it] | STABLE / UNSTABLE — [verdict on whether [TOKEN] is affected — TOKEN by declared value] | [reasoning distinct from verdict] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |

---

## V-02 — Output format: REQUIRED OUTPUTS as native markdown tables within each gate

**Axis:** REQUIRED OUTPUTS blocks rendered as native markdown tables (pipe-and-hyphen, no code fence) within each gate. R8 V-04 used numbered lists. V-02 replaces the numbered list with a table: columns `Output | Format | TOKEN required?` — making each output item independently consultable as a table row.
**Hypothesis:** Table format creates a more explicit structural boundary than a numbered list. A reader locating the table can extract it as a standalone artifact without reading surrounding prose, satisfying C-26's "extractable without reading instructional prose" requirement at maximum clarity. If table format produces the same score as numbered-list format, it confirms C-26 is format-agnostic within the "dedicated labeled block" class.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence. Each gate's Required outputs table is the gate's structural contract.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations |
|------|----------------|--------------------|
| GATE-0 | UNCONDITIONAL — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference |
| GATE-2 | CONDITIONAL | C0 description, competitive map |
| GATE-3 | CONDITIONAL | Findings, whitespace |
| GATE-4 | CONDITIONAL | AMEND table |

GATE-0 is unconditional. GATE-1 is the first conditional gate. Any gate's execution mode is verifiable in this plan without reading its body.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

This gate is unconditional — no conditional branching, focus detection, or section structure precedes or runs during it. GATE-1 is the first gate with conditional logic.

**Required outputs:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| DOMAIN-TERMS | `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed before TOKEN; 2–3 product-domain expert terms from repo context; not generic software vocabulary | Must include ≥1 term TOKEN will embed |
| TOKEN | `TOKEN: [domain-adaptive identifier]` — ≥1 DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | Yes — declared before all competitive content and all conditional logic; TOKEN by this value required in every gate's Required outputs table below |

Write exactly these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

Read repo context (README, CLAUDE.md, package.json) first.

**Completion condition:** `DOMAIN-TERMS:` written and closed. `TOKEN:` written and closed. Both lines before any other output.

---

### GATE-1 [CONDITIONAL — first conditional gate, focus detection and topic resolution]

Read repo context. Do not ask the user.

**Required outputs:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| FOCUS | `FOCUS: ACTIVE — [dimension] | INACTIVE` | — |
| TOPIC | `TOPIC: [inferred product domain]` | — |
| MARKET | `MARKET: [inferred market category]` | — |
| TOKEN carry-forward | TOKEN (value = TOKEN from GATE-0) confirmed as active inertia reference | Yes — TOKEN by declared value; required in GATE-2, GATE-3, GATE-4 Required outputs |

**Completion condition:** FOCUS, TOPIC, MARKET written. TOKEN (from GATE-0) confirmed as the active inertia reference — required by its declared value in every subsequent gate's Required outputs.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

C0 must appear before any competitor row. Mechanism must name a real C0 behavior or feature. Run a WebSearch to verify at least one competitor claim.

**Required outputs:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| C0 section | `## C0 — [name]` / `[TOKEN]: [mechanism type] → [specific C0 behavior]` — before any competitor row | Yes — TOKEN as C0 section field label |
| Competitive map | Native markdown table (pipe-and-hyphen, no code fence); C0 at row 0; `vs [TOKEN]` column header | Yes — TOKEN by declared value in column header |
| External competitors | Min 3 named with explicit threat levels (HIGH / MEDIUM / LOW) | — |
| Inline citation | Min 1 competitor row with WebSearch URL or publication name | — |
| TOKEN in vs-TOKEN cells | Each competitor row's `vs [TOKEN]` cell references TOKEN mechanism | Yes — TOKEN by declared value in each cell |

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |

**Completion condition:** C0 section before any competitor row. Table: row 0 = C0, 3+ external rows, 1+ inline citation. `vs [TOKEN]` column uses TOKEN by declared value.

---

### GATE-3 [CONDITIONAL — findings and whitespace]

Findings must reference named competitor rows by label — findings readable without GATE-2 fail. TOKEN appears by its declared value, not by role description.

**Required outputs:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| Findings (x3) | Each: `**Finding N: Title**` / `[observation — named competitor row by label]` / `vs [TOKEN]: [connection]` | Yes — TOKEN by declared value in each `vs [TOKEN]:` line |
| Whitespace | `WHITESPACE: [specific dimension]` / `[TOKEN] exposure: [relationship]` | Yes — TOKEN by declared value in `[TOKEN] exposure:` field |
| Cross-dimensional whitespace | Gap uncontested across competitive + focus dimensions simultaneously (only if FOCUS ACTIVE) | Yes — TOKEN in intersection rationale |

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by table label]
vs [TOKEN]: [connection to TOKEN mechanism — TOKEN by declared value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism — TOKEN by name]
```

If FOCUS ACTIVE: gap must require both the competitive map and the focus lens; show what the focus dimension reveals beyond the map alone.

**Completion condition:** 3 findings with named competitor references and `vs [TOKEN]` lines using TOKEN by declared value. Labeled whitespace with `[TOKEN] exposure:` naming TOKEN.

---

### GATE-4 [CONDITIONAL — AMEND]

**Required outputs:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| Schema declaration | Enumerated before data rows: Input change, Output effect, Stability verdict, Evidence — all four domain-neutral component names | — |
| AMEND data rows (min 3) | All four cells per row; no empty cells | — |
| Stability verdict cells | STABLE / UNSTABLE + one-sentence verdict naming TOKEN | Yes — TOKEN by declared value in every Stability verdict cell |
| Evidence cells | Reasoning distinct from verdict text — "Stable." alone fails | — |

**AMEND entry schema — all four components:**

| # | Component | Role |
|---|-----------|------|
| 1 | Input change | The user adjustment — focus dimension, depth, competitor scope |
| 2 | Output effect | Which gate or section specifically shifts — name it |
| 3 | Stability verdict | STABLE / UNSTABLE — does TOKEN shift? TOKEN by declared value required |
| 4 | Evidence | Reasoning supporting the verdict — logically distinct from verdict text |

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [user adjustment] | [gate/section that shifts — named] | STABLE / UNSTABLE — [verdict; TOKEN by declared value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |

**Completion condition:** 3+ data rows. Every cell filled. Every Stability verdict cell references TOKEN by its declared value with evidence distinct from verdict.

---

## V-03 — Lifecycle emphasis: trailing REQUIRED OUTPUTS position (after body prose)

**Axis:** REQUIRED OUTPUTS blocks positioned at the END of each gate — after body prose and templates — rather than leading. R8 V-04 led with REQUIRED OUTPUTS (block before prose). V-03 reverses the order: body prose and templates first, then the labeled REQUIRED OUTPUTS block. The block is still a dedicated, labeled section; only its position within the gate changes.
**Hypothesis:** C-26 requires the block to be "structurally distinct" and "extractable without reading instructional prose or completion conditions" — but does not explicitly require leading placement. If trailing blocks satisfy C-26, position is irrelevant and any placement that creates a labeled, extractable section passes. If trailing blocks fail, it establishes that leading placement is required for the structural separability test. This is the critical position-axis question for R9.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute gates in sequence.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations |
|------|----------------|--------------------|
| GATE-0 | UNCONDITIONAL — GATE-1 is the first conditional gate | DOMAIN-TERMS extraction → TOKEN declaration |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference |
| GATE-2 | CONDITIONAL | C0 description, competitive map |
| GATE-3 | CONDITIONAL | Findings, whitespace |
| GATE-4 | CONDITIONAL | AMEND table |

GATE-0 is unconditional and executes first, always. GATE-1 is the first gate where conditional operations execute. Any gate's execution mode is verifiable in this plan without reading its body.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

This gate is unconditional. No conditional branching, focus detection, or section structure precedes or runs during it. GATE-1 is the first gate with conditional logic.

Write exactly these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

Read repo context (README, CLAUDE.md, package.json) first. DOMAIN-TERMS: 2–3 product-domain expert terms — not generic software vocabulary. Write and close before TOKEN. TOKEN: copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails.

**Required outputs:**
1. `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed before TOKEN; product-domain expert terms from repo context
2. `TOKEN: [domain-adaptive identifier]` — ≥1 DOMAIN-TERMS term embedded; declared before all conditional logic; TOKEN by this value is required in every gate's Required outputs block below

---

### GATE-1 [CONDITIONAL — first conditional gate, focus detection]

```
FOCUS: ACTIVE — [dimension] | INACTIVE
TOPIC: [inferred product domain]
MARKET: [inferred market category]
```

Read repo context. Do not ask the user for topic, competitors, or market category.

**Required outputs:**
1. `FOCUS: ACTIVE — [dimension] | INACTIVE`
2. `TOPIC: [inferred domain]`
3. `MARKET: [inferred market category]`
4. TOKEN (from GATE-0) — active inertia reference; TOKEN by declared value required in GATE-2, GATE-3, GATE-4 Required outputs

---

### GATE-2 [CONDITIONAL — C0 and competitive map]

Describe C0 before any competitor row. Mechanism must name something C0 actually does or provides — "Inertia is high" without a product-specific anchor fails. Run a WebSearch to verify at least one competitor claim.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [Specific description tied to a real C0 behavior or feature — not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |

Min 3 named external competitors. No generic labels. Every row: explicit threat level. Min 1 inline citation.

**Required outputs:**
1. C0 section (before any competitor row): `## C0 — [name]` / `[TOKEN]: [mechanism type] → [specific C0 behavior]`
2. Competitive map (native markdown table, no code fence): row 0 = C0; `vs [TOKEN]` column header uses TOKEN by declared value; min 3 external rows; min 1 inline citation
3. TOKEN by declared value in: C0 section label, `vs [TOKEN]` column header, each competitor vs-TOKEN cell

---

### GATE-3 [CONDITIONAL — findings and whitespace]

Produce 3 findings grounded in named competitor rows — findings readable without GATE-2 fail. Name the whitespace gap explicitly; generic statements ("room to innovate") fail.

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by table label]
vs [TOKEN]: [how this finding relates to TOKEN mechanism — TOKEN by declared value, not role description]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [how TOKEN mechanism relates to this gap — TOKEN by name]
```

If FOCUS ACTIVE: gap must require both the competitive map and the focus lens; show what the focus dimension reveals beyond the map alone.

**Required outputs:**
1. 3 findings: each references a named competitor row by table label; each includes `vs [TOKEN]:` line with TOKEN by its declared value
2. Whitespace finding: specific uncontested dimension + `[TOKEN] exposure:` field naming TOKEN by declared value
3. If FOCUS ACTIVE: cross-dimensional whitespace naming the gap uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale

---

### GATE-4 [CONDITIONAL — AMEND]

Produce min 3 AMEND entries. Every Stability verdict must name TOKEN; every Evidence must contain reasoning distinct from the verdict — "Stable." alone fails.

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts — focus dimension, depth, competitor scope] | [which gate or section specifically shifts — name it] | STABLE / UNSTABLE — [verdict on whether [TOKEN] is affected — TOKEN by declared value] | [reasoning distinct from verdict] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |

**Required outputs:**
1. AMEND schema declared before data rows: Input change, Output effect, Stability verdict, Evidence — all four domain-neutral component names enumerated
2. Min 3 data rows: all four cells filled per row
3. TOKEN by declared value in every Stability verdict cell; Evidence contains reasoning distinct from verdict

---

## V-04 — Role sequence: lean gate bodies with REQUIRED OUTPUTS blocks as primary structure

**Axis:** Role sequence — REQUIRED OUTPUTS blocks lead each gate; body prose reduced to a single orienting sentence. In R8 V-04, gates had substantial body prose (mechanism rules, format guidance, anti-patterns) alongside REQUIRED OUTPUTS blocks. V-04 strips body prose to a minimum: one sentence of context, then immediately the REQUIRED OUTPUTS block. The block does the structural work.
**Hypothesis:** Lean bodies maximize REQUIRED OUTPUTS block dominance — the block is structurally dominant when body prose provides no competing specification. When there is less prose to compete with, C-26's "extractable without reading instructional prose" is more definitively satisfied. If V-04 scores 100, minimal-body design is a valid C-26 strategy. If any criterion drops, it identifies which body prose was load-bearing.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context. Execute gates in sequence — the Required outputs block is the complete structural contract for each gate.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations |
|------|----------------|--------------------|
| GATE-0 | UNCONDITIONAL — GATE-1 is the first conditional gate | DOMAIN-TERMS → TOKEN |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference |
| GATE-2 | CONDITIONAL | C0 description, competitive map |
| GATE-3 | CONDITIONAL | Findings, whitespace |
| GATE-4 | CONDITIONAL | AMEND |

GATE-0 is unconditional. GATE-1 is the first conditional gate.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

Read repo context (README, CLAUDE.md, package.json); write DOMAIN-TERMS then TOKEN as the first two lines of output — nothing before, nothing between them.

**Required outputs:**
1. `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — 2–3 product-domain expert terms; closed before TOKEN; not generic vocabulary
2. `TOKEN: [domain-adaptive identifier]` — embeds ≥1 DOMAIN-TERMS term; copyable portable token; generic placeholder alone (MECH, LOCK) fails; required by declared value in every downstream Required outputs block

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

---

### GATE-1 [CONDITIONAL — first conditional gate]

Infer topic and market from repo context; do not ask the user.

**Required outputs:**
1. `FOCUS: ACTIVE — [dimension] | INACTIVE`
2. `TOPIC: [inferred domain]`
3. `MARKET: [inferred market category]`
4. TOKEN (from GATE-0) — active inertia reference; TOKEN by declared value required in GATE-2, GATE-3, GATE-4 Required outputs

---

### GATE-2 [CONDITIONAL — C0 and competitive map]

C0 section before any competitor row; mechanism tied to real C0 behavior; WebSearch for ≥1 inline citation.

**Required outputs:**
1. C0 section (before any competitor row): `## C0 — [name]` / `[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior — not a generic label]`
2. Competitive map (native markdown table, no code fence): C0 at row 0; `vs [TOKEN]` column header using TOKEN by declared value; ≥3 named external competitors; explicit threat levels (HIGH/MEDIUM/LOW); ≥1 inline WebSearch citation
3. TOKEN by declared value in: C0 section label, `vs [TOKEN]` column header, each competitor's vs-TOKEN cell

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN] | — |

---

### GATE-3 [CONDITIONAL — findings and whitespace]

Each finding must reference a named map entry; TOKEN by declared value in every vs-TOKEN line; specific whitespace dimension required.

**Required outputs:**
1. ≥3 findings: each references a named competitor row by label; each includes `vs [TOKEN]:` line with TOKEN by declared value
2. Whitespace finding: `WHITESPACE: [specific named dimension]` + `[TOKEN] exposure: [relationship — TOKEN by name]`
3. If FOCUS ACTIVE: cross-dimensional whitespace finding (gap requires both competitive map and focus lens simultaneously); TOKEN in intersection rationale
4. TOKEN by declared value in every `vs [TOKEN]:` line and `[TOKEN] exposure:` field

```
**Finding [N]: [Title]**
[Observation — named competitor or map entry by label]
vs [TOKEN]: [connection — TOKEN by declared value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship — TOKEN by name]
```

---

### GATE-4 [CONDITIONAL — AMEND]

Schema declared before data; all four components per entry; TOKEN in every Stability verdict; Evidence distinct from verdict.

**Required outputs:**
1. Schema declaration (before data rows): Input change, Output effect, Stability verdict, Evidence — all four domain-neutral component names enumerated
2. ≥3 data rows: every Stability verdict cell names TOKEN by declared value; every Evidence cell contains reasoning distinct from verdict
3. TOKEN by declared value in every Stability verdict cell

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [user adjustment] | [gate/section that shifts] | STABLE / UNSTABLE — [verdict; TOKEN by declared value] | [reasoning distinct from verdict] |
| 2 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |
| 3 | [adjustment] | [effect] | STABLE / UNSTABLE — [verdict; TOKEN] | [reasoning] |

---

## V-05 — Combined: table REQUIRED OUTPUTS + manifest column + completion conditions retained

**Axis:** Combined — (1) REQUIRED OUTPUTS blocks rendered as native markdown tables within each gate (output format axis); (2) EXECUTION CONTRACT manifest includes a dedicated "Required outputs (TOKEN)" column (manifest integration); (3) completion conditions retained alongside REQUIRED OUTPUTS tables (dual-source). TOKEN is contractually declared in three independent locations per gate: the manifest column, the REQUIRED OUTPUTS table, and the completion condition.
**Hypothesis:** Triple-source TOKEN declaration (manifest column + REQUIRED OUTPUTS table + completion condition) provides maximum structural resilience — a reader verifying C-25/C-26 compliance can use any of the three sources independently. The manifest column naming TOKEN extends the R8 V-05 result (dual-source) by rendering per-gate blocks as tables. If V-05 scores 100, triple-source is robust; the decisive question is whether retaining completion conditions alongside REQUIRED OUTPUTS tables creates any conflicting specification, or simply adds redundancy.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Infer domain, competitors, and market from repo context — do not ask the user. Execute each gate in sequence.

---

### EXECUTION CONTRACT

| Gate | Execution mode | Primary operations | Required outputs (TOKEN) |
|------|----------------|--------------------|--------------------------|
| GATE-0 | **UNCONDITIONAL** — GATE-1 is first conditional | DOMAIN-TERMS extraction → TOKEN declaration | TOKEN declared by name — first declared inertia anchor; DOMAIN-TERMS closed before TOKEN |
| GATE-1 | **CONDITIONAL** (first) | Focus detection, topic inference | TOKEN (from GATE-0) confirmed as active reference by its declared value |
| GATE-2 | **CONDITIONAL** | C0 description, competitive map | `vs [TOKEN]` column header names TOKEN by declared value; TOKEN in C0 label and every competitor vs-TOKEN cell |
| GATE-3 | **CONDITIONAL** | Findings, whitespace | TOKEN by declared value in every `vs [TOKEN]:` line and `[TOKEN] exposure:` field |
| GATE-4 | **CONDITIONAL** | AMEND table | TOKEN by declared value in every Stability verdict cell |

GATE-0 is unconditional and executes first, always. GATE-1 is the first gate where conditional operations execute. No conditional logic precedes GATE-0's completion. Any gate's execution mode and required TOKEN output can be verified in this contract without reading the gate's body.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

This gate is unconditional — no conditional branching, focus detection, or section structure precedes or runs during it. GATE-1 is the first gate with conditional logic. Read repo context (README, CLAUDE.md, package.json) before writing.

**Required outputs:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| DOMAIN-TERMS | `DOMAIN-TERMS: [term-1], [term-2], [term-3]` — closed on its own line before TOKEN; 2–3 product-domain expert terms; not generic software vocabulary | Must include ≥1 term TOKEN will embed |
| TOKEN | `TOKEN: [domain-adaptive identifier]` — ≥1 DOMAIN-TERMS term embedded; copyable domain-specific token (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails | Yes — declared before all competitive content and all conditional logic; TOKEN by this value required in every gate's Required outputs table |

Write exactly these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — must include at least one term from DOMAIN-TERMS above]
```

**Completion condition:** `DOMAIN-TERMS:` written and closed. `TOKEN:` written and closed. Both lines before any other output.

---

### GATE-1 [CONDITIONAL — first conditional gate, focus detection and topic resolution]

Read repo context. Do not ask the user for topic, competitors, or market category.

**Required outputs:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| FOCUS | `FOCUS: ACTIVE — [dimension] | INACTIVE` | — |
| TOPIC | `TOPIC: [inferred product domain]` | — |
| MARKET | `MARKET: [inferred market category]` | — |
| TOKEN carry-forward | TOKEN (value = TOKEN from GATE-0) confirmed as active inertia reference | Yes — TOKEN by declared value; required in GATE-2, GATE-3, GATE-4 Required outputs |

**Completion condition:** FOCUS, TOPIC, MARKET written. TOKEN (from GATE-0) confirmed as the active inertia reference — required by its declared value in every subsequent gate's Required outputs.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

C0 must appear before any competitor row. Mechanism must name a real C0 behavior or feature. Run a WebSearch to verify at least one competitor claim.

**Required outputs:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| C0 section | `## C0 — [product name]` / `[TOKEN]: [mechanism type] → [specific C0 behavior]` — before any competitor row | Yes — TOKEN as field label in C0 section |
| Competitive map | Native markdown table (pipe-and-hyphen, no code fence); C0 at row 0; `vs [TOKEN]` column header | Yes — TOKEN by declared value in column header |
| External competitors | Min 3 named with explicit threat levels (HIGH / MEDIUM / LOW) | — |
| Inline citation | Min 1 competitor row with WebSearch URL or publication name | — |
| TOKEN in vs-TOKEN cells | Each competitor's `vs [TOKEN]` cell references TOKEN mechanism | Yes — TOKEN by declared value in each cell |

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [Specific description tied to a real C0 behavior or feature — not a generic category label]
```

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |

**Completion condition:** C0 section before any competitor row. Table: row 0 = C0, 3+ external rows, 1+ inline citation. `vs [TOKEN]` column uses TOKEN by declared value.

---

### GATE-3 [CONDITIONAL — findings and whitespace]

Findings must reference named competitor rows by table label — findings readable without GATE-2 fail. TOKEN appears by its declared value, not by role description.

**Required outputs:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| Findings (x3) | Each: `**Finding N: Title**` / `[observation — named competitor row by label]` / `vs [TOKEN]: [connection]` | Yes — TOKEN by declared value in each `vs [TOKEN]:` line |
| Whitespace | `WHITESPACE: [specific dimension]` / `[TOKEN] exposure: [relationship]` | Yes — TOKEN by declared value in `[TOKEN] exposure:` field |
| Cross-dimensional whitespace | Gap uncontested across competitive + focus dimensions simultaneously (only if FOCUS ACTIVE) | Yes — TOKEN in intersection rationale |

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by table label]
vs [TOKEN]: [connection to TOKEN mechanism — TOKEN by declared value, not role description]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [how TOKEN mechanism relates to this gap — TOKEN by name]
```

If FOCUS ACTIVE: gap must require both the competitive map and the focus lens simultaneously; show what the focus dimension reveals beyond the map alone; TOKEN in the intersection rationale.

**Completion condition:** 3 findings with named competitor references and `vs [TOKEN]` lines using TOKEN by declared value. Labeled whitespace with `[TOKEN] exposure:` naming TOKEN.

---

### GATE-4 [CONDITIONAL — AMEND]

**AMEND entry schema — all four required components enumerated by rubric-standard name:**

| # | Component | Rubric-standard name | Description |
|---|-----------|---------------------|-------------|
| 1 | Input | **Input change** | The user adjustment — focus dimension, depth level, competitor scope |
| 2 | Effect | **Output effect** | The specific change in output — name the gate or section affected |
| 3 | Verdict | **Stability verdict** | Whether TOKEN is affected — STABLE / UNSTABLE; TOKEN by declared value required |
| 4 | Support | **Evidence** | Reasoning supporting the stability verdict — logically distinct from the verdict |

**Required outputs:**

| Output | Format | TOKEN required? |
|--------|--------|----------------|
| Schema declaration | Enumerated before data rows: all four domain-neutral component names | — |
| AMEND data rows (min 3) | All four cells per row | — |
| Stability verdict cells | STABLE / UNSTABLE + one-sentence verdict naming TOKEN | Yes — TOKEN by declared value in every Stability verdict cell |
| Evidence cells | Reasoning distinct from verdict text — "Stable." alone fails | — |

**AMEND data table:**

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts — focus dimension, depth level, competitor scope] | [which gate or section specifically shifts — name it] | STABLE / UNSTABLE — [verdict on whether [TOKEN] is affected — TOKEN by declared value] | [reasoning distinct from verdict] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |

**Completion condition:** 3+ data rows. Every Stability verdict cell references TOKEN by its declared value. Every Evidence cell contains reasoning distinct from verdict.

---

## Composite hypothesis table

| Variation | C-26 strategy | C-26 prediction | Critical question |
|-----------|---------------|-----------------|-------------------|
| V-01 | REQUIRED OUTPUTS blocks are sole output spec per gate — no completion conditions | PASS — blocks present and labeled in every gate; TOKEN by declared value in every block; no competing completion-condition text | Does removing completion conditions hurt C-25 (which in R8 V-01/V-03 used completion-condition prose as the output spec)? Blocks-only is now both the C-25 and C-26 source. |
| V-02 | REQUIRED OUTPUTS as native markdown tables within each gate | PASS — table format is a labeled REQUIRED OUTPUTS block; TOKEN appears in "TOKEN required?" column; extractable as standalone table artifact | Does table format satisfy C-26 equally to numbered-list format? Is C-26 format-agnostic within the "dedicated labeled block" class? |
| V-03 | REQUIRED OUTPUTS blocks trail after body prose (position axis) | **UNCERTAIN** — block is structurally labeled and distinct, but body prose precedes it; C-26 requires "extractable without reading instructional prose" — does trailing placement satisfy this? | **Critical R9 question:** Does trailing REQUIRED OUTPUTS fail C-26's "can be extracted without reading prose" standard? This is the structural position test. |
| V-04 | Lean body prose (one sentence per gate); REQUIRED OUTPUTS block is primary gate content | PASS — blocks leading; body prose minimal and non-competing; extractability maximally clear | Does stripping body prose cause any criterion to lose its evidence base? (C-06 anti-pattern guidance lives in body prose; lean design removes it) |
| V-05 | Table REQUIRED OUTPUTS + manifest "Required outputs (TOKEN)" column + completion conditions retained (triple-source) | PASS — three independent TOKEN declaration sources; manifest column, REQUIRED OUTPUTS table, and completion condition all name TOKEN independently | Does triple-source provide structural resilience vs. dual-source (R8 V-05)? Does retaining completion conditions alongside table REQUIRED OUTPUTS create any conflicting specification risk? |

**Predicted winner:** V-01, V-02, V-04, V-05 all at **100** (18/18 aspirational = 10 pts, 0.556 each). V-03 predicted at **99.444** (17/18 aspirational) — trailing position likely fails C-26.
