Here are the 5 variations for `discover-competitors-alt` Round 7:

---

## Summary

**Baseline state:** R6 V-01/V-02/V-04/V-05 scored 100 on 14 aspirational criteria (C-01 through C-22). R7 adds **C-23**: the skill prompt must contain a pre-execution gate manifest — a standalone structured artifact enumerating **every** gate with execution-mode labels before any gate runs. C-21's inline GATE-0 bracket (R6 V-01/V-04 style) satisfies C-21 but fails C-23 (only declares one gate, not all). R6 V-02/V-05's manifest tables would have passed C-23.

---

### Variation axes

| Variation | Axis | Architectural choice |
|-----------|------|--------------------|
| **V-01** | Lifecycle emphasis | Full gate bodies + standalone "EXECUTION PLAN" heading with all 5 gates in a markdown table; C-21 double-declared at manifest + bracket level |
| **V-02** | Role sequence | Manifest-centric: full manifest table + minimal gate bodies — manifest alone carries the structural contract |
| **V-03** | Output format | Manifest as code-fence pipe-delimited block — tests C-23's "table or equivalent" language |
| **V-04** | Inertia framing | Full manifest + TOKEN required by declared value in every gate output field (column header, every finding, whitespace exposure field, AMEND verdict) |
| **V-05** | Combined | "EXECUTION CONTRACT" heading + gate bracket mode annotations + TOKEN propagation + pre-AMEND schema declaration table |

---

### The decisive R7 questions

1. **V-03:** Does `code-fence pipe-aligned block` satisfy "table or equivalent" for C-23?
2. **V-02 vs V-01:** Does manifest-only C-21 (no gate bracket) hold, or do brackets add scoring signal?
3. **V-04:** Does per-gate TOKEN mandates produce richer C-11 propagation or formulaic repetition?
4. **V-05:** Does a separate schema declaration table before the AMEND data table strengthen C-20/C-22 beyond column headers alone?
5. **All variations:** Does "EXECUTION CONTRACT" heading label add C-23 confidence over "EXECUTION PLAN"?

**Predicted:** V-01, V-02, V-04, V-05 at **100**. V-03 at risk for C-23 PARTIAL — **~99.333** if code-fence doesn't satisfy "table or equivalent."

File written to `simulations/quest/variations/discover-competitors-alt-variations-R7-2026-03-18.md`.
e by the manifest; gate bodies are consulted for details only.
- **V-03:** Manifest as code-fenced pipe-aligned block — `GATE-N | MODE | OPERATIONS` — with UNCONDITIONAL/CONDITIONAL mode labels for all 5 gates. Same gate bodies as V-01. Decisive C-23 question: does "table or equivalent" accept a code-fenced tabular format?
- **V-04:** Manifest table (V-01 format) + every gate's output section explicitly requires TOKEN by its declared value: `vs [TOKEN]` column header mandatory, every finding includes `vs [TOKEN]` line with TOKEN by value, whitespace has `[TOKEN] exposure:` labeled field, AMEND verdict column description references TOKEN by name.
- **V-05:** Manifest with "EXECUTION CONTRACT" heading (strongest standalone-artifact signal) + gate bracket annotations include execution-mode labels + TOKEN propagation + pre-AMEND schema declaration table that enumerates all 4 components with rubric-standard names + notes + C-23 named in GATE-0 completion condition.

**The decisive R7 questions:**
1. Does a code-fence tabular format satisfy C-23's "table or equivalent" (V-03)?
2. Does a compact manifest + minimal gate bodies satisfy all downstream criteria equally well as full gate bodies (V-02)?
3. Does double-declaring C-21 at manifest + gate-header level provide any advantage over manifest alone (V-01 vs V-02)?
4. Does TOKEN propagation maximization produce richer or formulaic downstream output (V-04)?
5. Does an AMEND schema declaration table (separate from the AMEND data table) improve C-20/C-22 confidence (V-05)?

**Predicted winners:** V-01, V-02, V-04, V-05 at 100. V-03 at risk for C-23 PARTIAL (~99.333) if code-fence is not accepted as "table or equivalent."

---

## V-01 — Lifecycle emphasis: full gate bodies with standalone EXECUTION PLAN manifest

**Axis:** Lifecycle emphasis — every phase has a full body with completion conditions; the manifest appears as a standalone heading artifact before any gate begins; GATE-0 bracket header also double-declares the C-21 conditions. Direct evolution of R6 V-05 with C-23 compliance made explicit.
**Hypothesis:** The cleanest C-23 form: a markdown table under "EXECUTION PLAN" heading enumerating all 5 gates with UNCONDITIONAL/CONDITIONAL mode labels, appearing before any gate executes. Combined with GATE-0 bracket header restating both C-21 conditions, C-23 and C-21 are each double-declared from two independent structural signals.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if one was provided. Execute each gate in sequence. Do not begin a gate until the previous gate's completion condition is satisfied.

---

### EXECUTION PLAN

The following manifest enumerates every gate and its execution mode. This artifact is declared before any gate executes. Any gate's execution mode can be verified by consulting this manifest without reading the gate's own body.

| Gate | Execution mode | Primary operations | Notes |
|------|---------------|-------------------|-------|
| GATE-0 | UNCONDITIONAL | DOMAIN-TERMS extraction → TOKEN declaration | Only unconditional gate; GATE-1 is its conditional successor |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference | First gate where conditional logic executes |
| GATE-2 | CONDITIONAL | C0 description, competitive map | C0 section before any competitor row |
| GATE-3 | CONDITIONAL | Findings, whitespace | TOKEN by name in every finding |
| GATE-4 | CONDITIONAL | AMEND table | Domain-neutral schema: Input change, Output effect, Stability verdict, Evidence |

GATE-0 is the only unconditional gate. GATE-1 is the first gate where conditional operations execute. No conditional logic precedes GATE-0's completion.

---

### GATE-0 [unconditional — GATE-1 is the first conditional operation]

This gate is unconditional — no focus detection, no auto-detect, no section headers, no conditional branching before or during it. GATE-1 is the first gate with conditional logic. GATE-0 must complete before GATE-1 opens.

Write exactly these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — must include at least one term from DOMAIN-TERMS above]
```

**DOMAIN-TERMS rules:**
- Read the repo context (README, CLAUDE.md, package.json, or equivalent).
- Extract 2–3 terms specific to this product's domain — terms a domain expert would use to describe the current solution, not generic software words.
- Write `DOMAIN-TERMS:` and close the line before writing TOKEN.

**TOKEN rules:**
- TOKEN is the portable inertia reference. It appears by name in every downstream gate.
- Must include at least one term from the DOMAIN-TERMS line. Generic placeholder alone (MECH, LOCK, INERTIA-REF) does not satisfy this — the token must encode domain context.
- A copyable identifier (e.g., SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK) passes. A role description ("the inertia mechanism") does not.
- Declared here, before any competitive content, before any conditional logic.

**GATE-0 completion condition:** `DOMAIN-TERMS:` written and closed. `TOKEN:` written and closed. Both lines appear before any other output. Nothing else in this gate.

---

### GATE-1 [first conditional — focus detection and topic resolution]

Detect the focus dimension and infer the topic. These are the first conditional operations.

```
FOCUS: ACTIVE — [dimension] | INACTIVE
TOPIC: [inferred product domain]
MARKET: [inferred market category]
```

Read the repo context. Do not ask the user for topic, competitor names, or market category.

**GATE-1 completion condition:** FOCUS verdict written. TOPIC and MARKET written.

---

### GATE-2 [C0 and competitive map]

**C0 — describe the current solution before naming any external competitor:**

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [Specific description tied to a real behavior or feature of C0 — not a generic category label]
```

The inertia mechanism must name something C0 does or provides. "Inertia is high" or an unanchored category label does not pass.

**Competitive map — C0 at row 0:**

Run a WebSearch to verify at least one competitor claim before completing this gate.

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |

- Minimum 3 named external competitors. No generic labels ("various startups," "open-source tools").
- Every row: explicit HIGH / MEDIUM / LOW threat level.
- At least one external row: inline WebSearch citation (URL or publication name) in the Source cell — not a footnote block.
- `vs [TOKEN]` column header uses TOKEN by its declared value.

**GATE-2 completion condition:** C0 section written before any competitor row. Table: row 0 = C0, at least 3 named external rows, at least one Source cell with inline citation.

---

### GATE-3 [findings and whitespace]

**Findings — 3 required, each anchored to a competitor row:**

```
**Finding [N]: [Title]**
[Observation — reference at least one named competitor row by its table label]
vs [TOKEN]: [how this finding relates to the TOKEN mechanism declared in GATE-0]
```

- Each finding references at least one named competitor by label.
- TOKEN must appear by its declared value in at least one `vs [TOKEN]` line across the finding set.
- Findings that could be written without the GATE-2 competitive map fail the grounding test.

**Whitespace — one labeled gap:**

Name one uncontested dimension that no listed competitor owns. State the specific gap — a generic statement ("there is room to innovate") does not pass.

If FOCUS is INACTIVE: competitive whitespace only.

If FOCUS is ACTIVE: the gap must be uncontested across both the competitive dimension and the focus dimension simultaneously. Show what the focus lens adds that the competitive map alone could not surface.

**GATE-3 completion condition:** 3 findings with competitor references and `vs [TOKEN]` lines. Whitespace finding labeled with a specific uncontested dimension.

---

### GATE-4 [AMEND]

Column headers enumerate all four required schema components by their domain-neutral names. A reader consulting only the headers can identify all four required components without reading the rows.

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts — focus dimension, depth level, competitor scope] | [which gate or section specifically shifts] | STABLE / UNSTABLE — [one-sentence verdict on whether [TOKEN] is affected] | [reasoning that supports the verdict — must be distinct from the verdict itself] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict] | [reasoning] |

- Minimum 3 rows. Every cell must be filled.
- Stability verdict: addresses whether TOKEN is affected. Verdict and evidence required in every row.
- Evidence: reasoning distinct from the verdict. "Stable." alone fails.

**GATE-4 completion condition:** Table has at least 3 data rows. Every row fills all four cells with a verdict and evidence.

---

## V-02 — Role sequence: manifest-centric with compact gate bodies

**Axis:** Role sequence — the manifest does the structural work; gate bodies are stripped to minimum viable form: one key structural rule + completion condition. Tests whether a comprehensive manifest is sufficient for C-23 when gate bodies contain no redundant structural declarations.
**Hypothesis:** When the manifest enumerates all 5 gates with modes and completion signals, gate bodies can be compact — the consultable contract lives in the manifest, not the gate headers. The risk: minimal gate bodies may underspecify instructions, producing weaker analysis even when structural criteria pass.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Work through each gate in order — do not start a gate until the previous one completes.

---

### EXECUTION MANIFEST

| Gate | Execution mode | Completion signal | Notes |
|------|---------------|------------------|-------|
| GATE-0 | UNCONDITIONAL | DOMAIN-TERMS closed + TOKEN closed | Executes first, always — the only unconditional gate; GATE-1 is the first conditional successor |
| GATE-1 | CONDITIONAL (first) | FOCUS + TOPIC + MARKET written | First gate where conditional logic (focus detection, topic inference) executes |
| GATE-2 | CONDITIONAL | C0 section + competitive table with 3+ external rows + inline citation | C0 before any competitor row; C0 at row 0 |
| GATE-3 | CONDITIONAL | 3 grounded findings with TOKEN references + labeled whitespace | TOKEN by name in at least one finding; specific uncontested gap named |
| GATE-4 | CONDITIONAL | AMEND table with 3+ rows, all four cells filled per row | Domain-neutral schema: Input change, Output effect, Stability verdict, Evidence |

GATE-0 is unconditional — it always executes first regardless of context. GATE-1 is the first gate where conditional logic executes. No conditional operation begins before GATE-0 is complete. Any gate's execution mode and completion signal can be verified in this manifest without reading the gate's body.

---

### GATE-0

Write these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

Read repo context first (README, CLAUDE.md, package.json). DOMAIN-TERMS: 2–3 product-domain terms — terms an expert would use, not generic software vocabulary. Write and close before TOKEN. TOKEN: must embed at least one DOMAIN-TERMS term. A copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-LOCK, ARTIFACT-HOLD) passes; a role description ("the inertia mechanism") does not. TOKEN appears by name in every downstream gate.

**Completion:** DOMAIN-TERMS closed. TOKEN closed. Both precede all other output.

---

### GATE-1

```
FOCUS: ACTIVE — [dimension] | INACTIVE
TOPIC: [inferred domain]
MARKET: [inferred market category]
```

Read repo context. Do not prompt the user for any of these.

**Completion:** FOCUS, TOPIC, MARKET written.

---

### GATE-2

C0 before any competitor row:

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [product-specific mechanism — what C0 does or provides]
```

Run WebSearch to verify at least one competitor claim. C0 at row 0:

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |

Min 3 named competitors, explicit threat levels, at least 1 inline Source citation — not a footnote.

**Completion:** C0 first. Table: row 0 = C0, 3+ external rows, 1+ inline citation.

---

### GATE-3

3 findings — each references a named competitor row by label:

```
**Finding [N]: [Title]**
[Observation — name the competitor row label]
vs [TOKEN]: [finding's connection to the TOKEN mechanism]
```

TOKEN must appear by its declared value in at least one `vs [TOKEN]` line. Findings that read without GATE-2 fail.

**Whitespace:** One uncontested gap — name the specific dimension. If FOCUS ACTIVE: gap must be uncontested across competitive + focus dimensions simultaneously; show what the focus lens reveals that the map alone could not surface.

**Completion:** 3 grounded findings with TOKEN references. Labeled whitespace with specific dimension.

---

### GATE-4

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [user adjustment] | [which gate/section shifts — name it] | STABLE / UNSTABLE — [verdict on whether [TOKEN] is affected] | [reasoning distinct from verdict] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict] | [reasoning] |

Min 3 rows. Every cell filled. Evidence must contain reasoning — "Stable." alone fails.

**Completion:** 3+ data rows, all four cells per row with verdict and reasoning.

---

## V-03 — Output format: manifest as code-fence pipe-delimited block

**Axis:** Output format — the execution manifest is presented as a code-fenced pipe-aligned block rather than a markdown table. All other structural elements (GATE-0 bracket headers, full gate bodies, AMEND schema) are identical to V-01. Tests whether C-23's "table or equivalent" accepts a code-fence tabular format as the consultable contract.
**Hypothesis:** A code-fence pipe block that enumerates every gate with explicit UNCONDITIONAL/CONDITIONAL labels — `GATE-N | MODE | OPERATIONS` — is structurally equivalent to a markdown table: it has rows, aligned columns, and mode labels for every gate. The risk: "table or equivalent" may require rendered-markdown structure specifically, and a code fence may fail as an unrendered format. If this passes C-23, it broadens the acceptable manifest formats.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Execute gates in sequence.

---

### EXECUTION PLAN

```
GATE-0 | UNCONDITIONAL       | DOMAIN-TERMS extraction → TOKEN declaration
GATE-1 | CONDITIONAL (first) | Focus detection, topic inference
GATE-2 | CONDITIONAL         | C0 description, competitive map
GATE-3 | CONDITIONAL         | Findings, whitespace
GATE-4 | CONDITIONAL         | AMEND table
```

Every gate is enumerated above with its execution mode. GATE-0 is unconditional — always runs first. GATE-1 is the first conditional gate. No conditional logic precedes GATE-0's completion. Any gate's execution mode is verifiable here without reading its body.

---

### GATE-0 [unconditional — GATE-1 is the first conditional operation]

This gate is unconditional — no focus detection, no auto-detect, no section headers, no conditional branching before or during it. GATE-1 is the first gate where conditional logic executes.

Your opening output — exactly these two lines, nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — at least one DOMAIN-TERMS term embedded]
```

Read repo context (README, CLAUDE.md, package.json) first. DOMAIN-TERMS: 2–3 product-domain expert terms — not generic software words. Write and close before TOKEN. TOKEN: copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-ANCHOR); generic placeholder alone (MECH, LOCK) fails. TOKEN declared before all competitive content and all conditional logic.

**GATE-0 completion:** DOMAIN-TERMS closed. TOKEN closed. Both appear before all other output.

---

### GATE-1 [first conditional — focus detection]

```
FOCUS: ACTIVE — [dimension] | INACTIVE
TOPIC: [inferred domain]
MARKET: [inferred market category]
```

Read repo context. Do not ask the user.

**GATE-1 completion:** FOCUS, TOPIC, MARKET written.

---

### GATE-2 [C0 and competitive map]

**C0 first — before any competitor row:**

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific C0 behavior or feature that creates this mechanism]
```

The mechanism must tie to a real C0 behavior. A generic category label ("inertia is high") does not pass.

Run WebSearch to verify at least one competitor claim.

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [capability] | ROOT | — |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | — |

Min 3 named competitors, explicit threat levels, 1+ inline Source citation — not a footnote.

**GATE-2 completion:** C0 first. Table: C0 at row 0, 3+ external rows, 1+ inline citation.

---

### GATE-3 [findings and whitespace]

**3 findings — each references a named competitor row:**

```
**Finding [N]: [Title]**
[Observation — name competitor row by label]
vs [TOKEN]: [finding's connection to TOKEN mechanism — TOKEN by declared value]
```

No finding reads without the GATE-2 map. TOKEN appears by its declared value.

**Whitespace:** Name one uncontested gap with specific dimension. If FOCUS ACTIVE: gap uncontested across competitive + focus dimensions simultaneously; show what the focus lens reveals that the map alone could not surface.

**GATE-3 completion:** 3 grounded findings with TOKEN references. Labeled whitespace with specific dimension.

---

### GATE-4 [AMEND]

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [adjustment] | [which gate/section shifts — name it] | STABLE / UNSTABLE — [verdict on whether [TOKEN] is affected] | [supporting reasoning] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict] | [reasoning] |

Min 3 rows. Every cell filled. Evidence distinct from verdict.

**GATE-4 completion:** 3+ data rows, all four cells per row with verdict and evidence.

---

## V-04 — Inertia framing: manifest + TOKEN propagation maximized

**Axis:** Inertia framing — the status-quo competitor's mechanism is maximally prominent across every gate output. Full manifest for C-23; GATE-0 bracket also declares both C-21 conditions. TOKEN is required by name in: the `vs [TOKEN]` column header (using TOKEN's declared value), every finding's `vs [TOKEN]` line, the whitespace `[TOKEN] exposure:` labeled field, and the AMEND stability verdict column description.
**Hypothesis:** Mandating TOKEN references by name at every structural output point — not just in optional `vs` lines — makes C-11 propagation architectural rather than incidental. The risk: per-gate TOKEN requirements may produce formulaic downstream output (TOKEN appears mechanically) rather than analytical usage (TOKEN shapes the competitive reasoning). Compare findings quality vs. V-01/V-02.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. The inertia mechanism token declared in GATE-0 is the structural reference that threads through every gate — it anchors the competitive map, grounds every finding, and frames the AMEND stability judgments.

Execute each gate in sequence. Do not begin a gate until the previous gate's completion condition is satisfied.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | Notes |
|------|---------------|-------------------|-------|
| GATE-0 | UNCONDITIONAL | DOMAIN-TERMS extraction → TOKEN declaration | Only unconditional gate; TOKEN declared here, before all conditional logic |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference | First conditional gate — GATE-1 is TOKEN's first downstream context |
| GATE-2 | CONDITIONAL | C0 description, competitive map | `vs [TOKEN]` column header uses TOKEN by declared value |
| GATE-3 | CONDITIONAL | Findings, whitespace | TOKEN by name in every `vs [TOKEN]` line; `[TOKEN] exposure:` in whitespace |
| GATE-4 | CONDITIONAL | AMEND table | Stability verdict references TOKEN by name in every row |

GATE-0 is the only unconditional gate. GATE-1 is the first gate where conditional logic executes. Any gate's mode is verifiable in this manifest without reading the gate body.

---

### GATE-0 [unconditional — GATE-1 is the first conditional operation]

This gate is unconditional — no focus detection, no auto-detect, no section headers, no conditional branching before or during it. GATE-1 is the first gate with conditional logic.

Write exactly these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — must include at least one term from DOMAIN-TERMS above]
```

Read the repo context (README, CLAUDE.md, package.json) before writing. DOMAIN-TERMS: 2–3 product-domain terms — terms an expert would use, not generic software vocabulary. Write and close before TOKEN. TOKEN: at least one DOMAIN-TERMS term embedded; generic placeholder alone (MECH, LOCK) fails; a copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-LOCK, PLUGIN-ANCHOR) passes.

TOKEN will appear by its declared value in: C0 mechanism label, `vs [TOKEN]` column header, every finding's `vs [TOKEN]` line, the whitespace TOKEN exposure field, and the AMEND stability verdict column.

**GATE-0 completion condition:** DOMAIN-TERMS closed. TOKEN closed. Both lines before any other output.

---

### GATE-1 [first conditional — focus detection]

```
FOCUS: ACTIVE — [dimension] | INACTIVE
TOPIC: [inferred product domain]
MARKET: [inferred market category]
```

Read repo context. Do not ask the user.

**GATE-1 completion condition:** FOCUS, TOPIC, MARKET written.

---

### GATE-2 [C0 and competitive map — TOKEN anchors the table]

**C0 — before any competitor row:**

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [Specific description tied to a real C0 behavior or feature — not a generic category label]
```

The mechanism must name something C0 actually does or provides. "Inertia is high" without a product-specific anchor fails.

Run a WebSearch to verify at least one competitor claim.

**Competitive map — `vs [TOKEN]` column header uses TOKEN by its declared value:**

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses the TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses the TOKEN mechanism] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses the TOKEN mechanism] | — |

- Minimum 3 named external competitors. No generic labels.
- Every row: explicit HIGH / MEDIUM / LOW threat level.
- At least one external row: inline WebSearch citation in Source cell — not a footnote.
- `vs [TOKEN]` column header must use TOKEN by its declared value, not a generic label.

**GATE-2 completion condition:** C0 section before any competitor row. Table: row 0 = C0, at least 3 external rows, at least 1 inline citation, `vs [TOKEN]` header using TOKEN by declared value.

---

### GATE-3 [findings and whitespace — TOKEN by name in every output field]

**Findings — 3 required:**

Each finding must: (1) reference at least one named competitor row by table label, and (2) include a `vs [TOKEN]` line where TOKEN appears by its declared value — not by role description ("the inertia mechanism" without naming TOKEN fails).

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by label]
vs [TOKEN]: [how this finding relates to the TOKEN mechanism — TOKEN must appear verbatim here, by declared value]
```

Findings that could be written without GATE-2 fail the grounding test. A `vs [TOKEN]` line that names the mechanism without TOKEN's value fails C-11.

**Whitespace finding — TOKEN exposure field required:**

Name one uncontested gap no listed competitor owns. Include the TOKEN exposure field:

```
WHITESPACE: [specific uncontested dimension — not a generic statement]
[TOKEN] exposure: [whether TOKEN's mechanism reinforces, defines, or is irrelevant to this gap — TOKEN must appear by name]
```

If FOCUS is ACTIVE: gap must be uncontested across competitive + focus dimensions simultaneously. Show the intersection and include TOKEN in the intersection rationale.

**GATE-3 completion condition:** 3 findings with named competitor references and `vs [TOKEN]` lines using TOKEN by declared value. Whitespace finding with labeled dimension and `[TOKEN] exposure:` field.

---

### GATE-4 [AMEND — TOKEN named in stability verdict column]

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts — focus dimension, depth level, competitor scope] | [which gate or section specifically shifts — name it] | STABLE / UNSTABLE — [one-sentence verdict on whether [TOKEN] is affected by this change — TOKEN must appear by its declared value] | [reasoning that supports the verdict — logically distinct from the verdict] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |

- Minimum 3 rows. Every cell filled.
- Stability verdict: TOKEN must be referenced by its declared value in the verdict sentence or immediately adjacent Evidence cell.
- Evidence: reasoning distinct from verdict. "Stable." alone fails.

**GATE-4 completion condition:** At least 3 data rows. Every row fills all four cells with verdict and evidence.

---

## V-05 — Combined: EXECUTION CONTRACT manifest + gate annotations + TOKEN propagation + schema declaration block

**Axis:** Combined — lifecycle (explicit "EXECUTION CONTRACT" heading, per-gate mode annotations in brackets), inertia framing (TOKEN propagation in all sections), output format (AMEND schema declaration table before the AMEND data table). Strongest possible C-23 signal: "EXECUTION CONTRACT" makes the manifest a named artifact; gate brackets also annotate modes; schema declaration block explicitly enumerates all 4 rubric-standard component names before the AMEND data table.
**Hypothesis:** Three independent structural markers for C-23 (manifest heading, all gates enumerated with modes, gate brackets annotating execution mode) produce maximum consultability confidence. Pre-AMEND schema declaration table ensures a reader can identify all four required components from the schema alone, not just from column headers. C-23 compliance is overkill-hardened — no reasonable interpretation of "standalone structured artifact" can fail.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project. If a focus dimension was provided, weave it throughout — do not append it as a separate section. Execute each gate in sequence.

---

### EXECUTION CONTRACT

| Gate | Execution mode | Primary operations | Completion signal |
|------|---------------|-------------------|------------------|
| GATE-0 | UNCONDITIONAL | DOMAIN-TERMS extraction → TOKEN declaration | DOMAIN-TERMS closed + TOKEN closed — both before any other output |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference | FOCUS + TOPIC + MARKET written |
| GATE-2 | CONDITIONAL | C0 description, competitive map | C0 before competitors; table: row 0 = C0, 3+ external rows, 1+ inline citation |
| GATE-3 | CONDITIONAL | Findings (TOKEN-grounded), whitespace | 3 findings with `vs [TOKEN]` lines; labeled whitespace with TOKEN exposure |
| GATE-4 | CONDITIONAL | AMEND table | 3+ data rows; all four schema components present in every row |

GATE-0 is unconditional and executes first, always. GATE-1 is the first gate where conditional operations execute. No conditional logic precedes GATE-0's completion. This contract is a consultable artifact — any gate's execution mode and completion signal can be verified here without reading the gate's body.

---

### GATE-0 [UNCONDITIONAL — GATE-1 is the first conditional operation]

This gate is unconditional. No focus detection, no auto-detect, no section headers, no conditional branching before or during it. GATE-1 is the first gate with conditional logic. This gate produces exactly two outputs: DOMAIN-TERMS then TOKEN. Nothing precedes DOMAIN-TERMS. Nothing appears between DOMAIN-TERMS and TOKEN.

Write exactly these two lines as your opening output:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — must include at least one term from DOMAIN-TERMS above]
```

Read repo context (README, CLAUDE.md, package.json, or equivalent) before writing. DOMAIN-TERMS: 2–3 product-domain expert terms — not generic software vocabulary. Write and close before TOKEN. TOKEN: must include at least one DOMAIN-TERMS term. Generic placeholder alone (MECH, LOCK, INERTIA-REF) fails. A copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK) passes.

TOKEN is declared here before all competitive content, before all conditional logic, before all section structure. It appears by name in every subsequent gate. The EXECUTION CONTRACT above enumerates all gates with execution modes — this is GATE-0's unconditional output.

**GATE-0 completion condition:** DOMAIN-TERMS written and closed. TOKEN written and closed. Both lines before any other output. No other content in this gate.

---

### GATE-1 [CONDITIONAL, first — focus detection and topic resolution]

```
FOCUS: ACTIVE — [dimension] | INACTIVE
TOPIC: [inferred product domain]
MARKET: [inferred market category]
```

Read repo context. Do not ask the user for topic, competitor names, or market category.

**GATE-1 completion condition:** FOCUS, TOPIC, MARKET written.

---

### GATE-2 [CONDITIONAL — C0 description and competitive map]

**C0 — produced before any competitor row:**

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [Specific description tied to a real C0 behavior or feature — not a generic category label]
```

Mechanism must name something C0 actually does or provides. "Inertia is high" without a product-specific anchor fails.

Run a WebSearch to verify at least one competitor claim before completing this gate.

**Competitive map — C0 at row 0:**

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | — |

- Minimum 3 named external competitors. No generic labels.
- Every row: explicit HIGH / MEDIUM / LOW threat level.
- At least one external row: inline WebSearch citation in Source cell — not a footnote block.
- `vs [TOKEN]` column header uses TOKEN by its declared value.

**GATE-2 completion condition:** C0 section before any competitor row. Table: row 0 = C0, at least 3 external rows, at least 1 inline citation.

---

### GATE-3 [CONDITIONAL — findings and whitespace, TOKEN by name in every output]

**Findings — 3 required:**

Each finding must reference at least one named competitor row by table label AND include a `vs [TOKEN]` line with TOKEN appearing by its declared value.

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by label]
vs [TOKEN]: [how this finding relates to the TOKEN mechanism — TOKEN must appear by its declared value, not by role description]
```

Findings that could be written without GATE-2 fail. "The inertia mechanism" without TOKEN's name fails C-11.

**Whitespace — one labeled finding:**

Name one uncontested gap no listed competitor owns. State the specific dimension.

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [how TOKEN's mechanism relates to this gap — TOKEN by name]
```

If FOCUS is ACTIVE: gap must be uncontested across competitive + focus dimensions simultaneously. Show what the focus lens adds that the competitive map alone would not surface. Include TOKEN in the intersection rationale.

**GATE-3 completion condition:** 3 findings with named competitor references and `vs [TOKEN]` lines using TOKEN by declared value. Labeled whitespace finding with TOKEN exposure field.

---

### GATE-4 [CONDITIONAL — AMEND]

**AMEND entry schema — all four required components enumerated by rubric-standard names:**

| # | Component | Rubric-standard name | Description |
|---|-----------|---------------------|-------------|
| 1 | Input | **Input change** | The adjustment the user makes — focus dimension, depth level, competitor scope |
| 2 | Effect | **Output effect** | The specific change in output that results — name the gate or section |
| 3 | Verdict | **Stability verdict** | Whether TOKEN is affected — STABLE / UNSTABLE required, with TOKEN referenced by name |
| 4 | Support | **Evidence** | Reasoning that supports the stability verdict, logically distinct from the verdict itself |

**AMEND data table — minimum 3 rows:**

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts — focus dimension, depth level, competitor scope] | [which gate or section specifically shifts — name it] | STABLE / UNSTABLE — [one-sentence verdict on whether [TOKEN] is affected] | [reasoning that supports the verdict — logically distinct from the verdict statement] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |

Minimum 3 rows. Every cell must be filled. Evidence column must contain reasoning — "Stable." alone fails. Every Stability verdict cell must contain TOKEN by name.

**GATE-4 completion condition:** Schema declaration present before data table. Data table has at least 3 rows. Every row: all four cells with verdict and evidence.

---

## Composite hypothesis table

| Variation | C-21 prediction | C-23 prediction | Critical question |
|-----------|----------------|----------------|-------------------|
| V-01 | PASS — GATE-0 bracket: `[unconditional — GATE-1 is the first conditional operation]`; also declared in manifest Notes column | PASS — "EXECUTION PLAN" markdown table enumerates all 5 gates with UNCONDITIONAL/CONDITIONAL mode labels; standalone heading artifact before any gate executes | Does double-declaring C-21 (manifest + bracket) produce any advantage over manifest alone? |
| V-02 | PASS — manifest declares "GATE-0 is unconditional… GATE-1 is the first conditional successor" in narrative below table; Notes column also states the boundary | PASS — manifest table enumerates all 5 gates with execution modes and completion signals; narrative confirms unconditional/conditional boundary | Does compact gate bodies reduce analytical quality even when structural criteria pass? Is manifest-only C-21 declaration (no gate bracket) sufficient? |
| V-03 | PASS — GATE-0 bracket: `[unconditional — GATE-1 is the first conditional operation]` | PASS or PARTIAL — code-fence pipe block enumerates all 5 gates with UNCONDITIONAL/CONDITIONAL labels; "table or equivalent" — tests whether code-fence tabular format qualifies as the consultable artifact | Does "table or equivalent" in C-23 accept a code-fenced pipe-delimited format, or does it require markdown table syntax specifically? |
| V-04 | PASS — GATE-0 bracket states both conditions; manifest also declares both | PASS — "EXECUTION PLAN" markdown table enumerates all 5 gates with modes; same manifest format as V-01 | Does TOKEN propagation maximization (TOKEN required verbatim in every output field) produce richer C-11 analysis or formulaic repetition? |
| V-05 | PASS — strongest signal: "EXECUTION CONTRACT" manifest heading + GATE brackets annotate modes + narrative confirms boundary | PASS — "EXECUTION CONTRACT" manifest is the most explicitly labeled standalone artifact: heading + all 5 gates with modes + completion signals; three independent structural markers for consultability | Does the AMEND schema declaration table (separate from data table) strengthen C-20/C-22? Does the "EXECUTION CONTRACT" heading label add C-23 confidence over "EXECUTION PLAN"? |

**R7 decisive questions resolved by scorecard:**
1. V-03: Does code-fence tabular format satisfy "table or equivalent" for C-23? → determines acceptable manifest formats
2. V-02: Does manifest-only C-21 declaration (no gate bracket) hold the PASS from R6? → confirms whether gate brackets are required alongside manifest
3. V-04 vs V-01: Does TOKEN propagation produce measurably richer C-11 analysis or formulaic satisfaction?
4. V-05: Does a schema declaration table before the AMEND data table provide any C-20/C-22 advantage beyond column headers alone?
5. V-01 vs V-02: Does double-declaring C-21 (manifest + bracket vs. manifest only) produce any scoring difference?

**Predicted winner:** V-01, V-02, V-04, V-05 at 100. V-03 at risk for C-23 PARTIAL — predicted 99.333 (14.5/15 aspirational) if code-fence is not accepted as "table or equivalent."
