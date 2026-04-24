File written to `simulations/quest/variations/discover-competitors-alt-variations-R8-2026-03-18.md`.

---

Here are the 5 R8 variations for `discover-competitors-alt`:

---

### Summary

**R8 context:** R7 V-01/V-02/V-04/V-05 all scored 100. R7 V-03 scored 99.667 — C-23 PARTIAL on code-fence manifest. R8 adds:
- **C-24**: Native markdown table for the manifest (closes the V-03 loophole)
- **C-25**: TOKEN named by declared value in every gate's output specification

The aspirational pool grows 15 → 17 criteria (0.588 pts each).

**C-25 gap in R7 V-01:** GATE-1 and GATE-4 completion conditions don't name TOKEN. GATE-2 has it in the template but not the completion condition text.

---

### Variation axes

| Variation | Axis | C-25 strategy |
|-----------|------|---------------|
| **V-01** | Lifecycle emphasis | TOKEN added to GATE-1, GATE-2, GATE-4 completion conditions — minimum viable form |
| **V-02** | Role sequence | Manifest completion-signal column names TOKEN for every gate row — manifest as sole C-25 source |
| **V-03** | Output format | Code-fence → native table (direct C-24 fix) + same completion-condition C-25 additions as V-01 |
| **V-04** | Inertia framing | Per-gate REQUIRED OUTPUTS blocks list TOKEN explicitly — most unambiguous form |
| **V-05** | Combined | EXECUTION CONTRACT with dedicated "Required TOKEN output" column + per-gate REQUIRED OUTPUTS blocks + AMEND schema declaration table |

**Decisive questions for R8 scorecard:**
1. Does completion-condition prose naming TOKEN satisfy C-25? (V-01, V-03) — minimum viable form
2. Does the manifest completion-signal column serve as the output spec? (V-02) — manifest-as-contract extended to C-25
3. Are REQUIRED OUTPUTS blocks necessary vs. prose sufficient? (V-04 vs V-01)
4. Does dual-source TOKEN declaration produce any advantage? (V-05)

**Predicted:** V-01 through V-05 all at **100** (17/17 aspirational).
|
|-----------|------|---------------|---------------|
| **V-01** | Lifecycle emphasis | Native table maintained (R7 V-01 baseline) | TOKEN added to GATE-1, GATE-2, and GATE-4 completion conditions by name |
| **V-02** | Role sequence | Native table in EXECUTION MANIFEST | Manifest completion-signal column names TOKEN for every gate row |
| **V-03** | Output format | Convert R7 V-03 code-fence to native markdown table — minimum viable C-24 fix | TOKEN in completion conditions (GATE-1, GATE-2, GATE-4) |
| **V-04** | Inertia framing | Native table maintained | Per-gate REQUIRED OUTPUTS blocks list TOKEN as a named required element |
| **V-05** | Combined | EXECUTION CONTRACT native table with dedicated "Required TOKEN output" column | Dual-source: manifest column + per-gate REQUIRED OUTPUTS blocks both name TOKEN |

---

### The decisive R8 questions

1. Does adding TOKEN to GATE-1 and GATE-4 completion conditions satisfy C-25? (V-01, V-03)
2. Does the manifest completion-signal column serve as the output specification for C-25? (V-02)
3. Are explicit REQUIRED OUTPUTS blocks a stronger C-25 form than completion-condition prose? (V-04)
4. Does dual-source TOKEN declaration (manifest column + per-gate blocks) produce any advantage over single-source? (V-05)
5. Does the native-table conversion for V-03 produce a full score, or does some other element remain at risk?

**Predicted:** V-01 through V-05 all at **100** (17/17 aspirational). The minimal C-25 fix — adding TOKEN to GATE-1 and GATE-4 completion conditions — is sufficient; all variations apply this fix or a structurally stronger form.

---

## V-01 — Lifecycle emphasis: TOKEN in every completion condition

**Axis:** Lifecycle emphasis — full gate bodies + TOKEN added by name to every completion condition. Direct evolution of R7 V-01: the only structural change is that GATE-1, GATE-2, and GATE-4 completion conditions now explicitly name TOKEN, closing the C-25 gap identified in the baseline analysis.
**Hypothesis:** The completion condition is the gate's output specification for C-25 purposes. Adding one phrase per gate ("TOKEN carries forward as the active reference" in GATE-1; "`vs [TOKEN]` uses TOKEN by declared value" strengthened in GATE-2; "every Stability verdict cell references TOKEN by its declared value" in GATE-4) satisfies C-25 at minimal structural cost. If this passes, it establishes that completion-condition prose naming TOKEN is the minimum viable C-25 form.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Execute gates in sequence. Do not begin a gate until the previous gate's completion condition is satisfied.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | Notes |
|------|---------------|--------------------|-------|
| GATE-0 | UNCONDITIONAL | DOMAIN-TERMS extraction -> TOKEN declaration | Only unconditional gate; GATE-1 is its conditional successor |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference | First gate where conditional logic executes |
| GATE-2 | CONDITIONAL | C0 description, competitive map | C0 before any competitor row; `vs [TOKEN]` column uses TOKEN by declared value |
| GATE-3 | CONDITIONAL | Findings, whitespace | TOKEN by name in every `vs [TOKEN]` line; TOKEN in whitespace exposure field |
| GATE-4 | CONDITIONAL | AMEND table | TOKEN by declared value in every Stability verdict cell |

GATE-0 is the only unconditional gate. GATE-1 is the first gate where conditional operations execute. Any gate's execution mode can be verified in this manifest without reading its body.

---

### GATE-0 [unconditional -- GATE-1 is the first conditional operation]

This gate is unconditional -- no focus detection, no auto-detect, no section headers, no conditional branching before or during it. GATE-1 is the first gate with conditional logic.

Write exactly these two lines as your opening output -- nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier -- must include at least one term from DOMAIN-TERMS above]
```

**DOMAIN-TERMS rules:** Read repo context (README, CLAUDE.md, package.json). Extract 2-3 product-domain terms -- terms a domain expert would use, not generic software vocabulary. Write and close before TOKEN.

**TOKEN rules:** Must include at least one DOMAIN-TERMS term. Generic placeholder alone (MECH, LOCK, INERTIA-REF) fails. A copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK) passes. Declared before all competitive content and all conditional logic.

**GATE-0 completion condition:** `DOMAIN-TERMS:` written and closed. `TOKEN:` written and closed. Both lines before any other output.

---

### GATE-1 [first conditional -- focus detection and topic resolution]

Detect focus dimension and infer topic from repo context. Do not ask the user.

```
FOCUS: ACTIVE -- [dimension] | INACTIVE
TOPIC: [inferred product domain]
MARKET: [inferred market category]
```

**GATE-1 completion condition:** FOCUS, TOPIC, MARKET written. TOKEN (value declared in GATE-0) confirmed as the active inertia reference -- TOKEN by its declared value is required in every subsequent gate's output.

---

### GATE-2 [C0 and competitive map]

**C0 -- before any competitor row:**

```
## C0 -- [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [Specific description tied to a real C0 behavior or feature -- not a generic category label]
```

Mechanism must name something C0 actually does or provides. "Inertia is high" without a product-specific anchor fails.

Run a WebSearch to verify at least one competitor claim before completing this gate.

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 -- [product name] | -- | [key capability] | ROOT | -- |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | -- |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | -- |

Min 3 named competitors, explicit threat levels, 1+ inline Source citation -- not a footnote.

**GATE-2 completion condition:** C0 section before any competitor row. Table: row 0 = C0, 3+ named external rows, 1+ inline citation. `vs [TOKEN]` column header uses TOKEN by its declared value.

---

### GATE-3 [findings and whitespace]

**Findings -- 3 required, each anchored to a named competitor row:**

```
**Finding [N]: [Title]**
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [how this finding relates to the TOKEN mechanism -- TOKEN by its declared value, not a role description]
```

TOKEN must appear by its declared value in every `vs [TOKEN]` line. Findings readable without GATE-2 fail the grounding test.

**Whitespace -- one labeled finding:**

```
WHITESPACE: [specific uncontested dimension -- not a generic statement]
[TOKEN] exposure: [how TOKEN's mechanism relates to this gap -- TOKEN by name]
```

If FOCUS is ACTIVE: gap must be uncontested across both competitive + focus dimensions simultaneously; show what the focus lens adds that the competitive map alone cannot surface.

**GATE-3 completion condition:** 3 findings with named competitor references and `vs [TOKEN]` lines using TOKEN by declared value. Whitespace finding with labeled dimension and `[TOKEN] exposure:` field naming TOKEN.

---

### GATE-4 [AMEND]

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts -- focus dimension, depth level, competitor scope] | [which gate or section specifically shifts -- name it] | STABLE / UNSTABLE -- [one-sentence verdict on whether [TOKEN] is affected -- TOKEN must appear by its declared value] | [reasoning distinct from verdict] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE -- [verdict on [TOKEN]] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE -- [verdict on [TOKEN]] | [reasoning] |

Min 3 rows. Every cell filled. Evidence must contain reasoning -- "Stable." alone fails.

**GATE-4 completion condition:** 3+ data rows. Every row fills all four cells. Every Stability verdict cell references TOKEN by its declared value.

---

## V-02 -- Role sequence: manifest completion-signal column as C-25 contract

**Axis:** Role sequence -- the manifest's completion-signal column names TOKEN for every gate, making the manifest the single C-25 compliance source. Compact gate bodies. Tests whether the manifest completion-signal column qualifies as "the gate's output specification" for C-25 purposes -- extending the R7 result that the manifest is the consultable contract for C-23.
**Hypothesis:** When every row of the EXECUTION MANIFEST specifies a completion signal that explicitly names TOKEN, the manifest functions as a distributed output specification across all gates. Gate bodies can remain minimal -- the consultable contract for both C-23 and C-25 lives entirely in the manifest. If V-02 passes C-25, it confirms that the manifest completion-signal column is the operative output specification and gate-body completion-condition prose is redundant for C-25.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Execute gates in sequence.

---

### EXECUTION MANIFEST

| Gate | Execution mode | Completion signal |
|------|---------------|------------------|
| GATE-0 | UNCONDITIONAL | `DOMAIN-TERMS:` written and closed. `TOKEN:` written and closed -- TOKEN by its declared value is the required first-declared output. Both lines before any other output. |
| GATE-1 | CONDITIONAL (first) | FOCUS, TOPIC, MARKET written. TOKEN (from GATE-0) confirmed as the active inertia reference -- TOKEN by its declared value carries to every subsequent gate's required output. |
| GATE-2 | CONDITIONAL | C0 section before any competitor row. Competitive table: row 0 = C0, 3+ external rows, 1+ inline citation. `vs [TOKEN]` column header uses TOKEN by its declared value. |
| GATE-3 | CONDITIONAL | 3 grounded findings each with a `vs [TOKEN]` line naming TOKEN by declared value. Whitespace finding: specific dimension + `[TOKEN] exposure:` field naming TOKEN by declared value. |
| GATE-4 | CONDITIONAL | 3+ AMEND rows. All four cells filled per row. Every Stability verdict cell references TOKEN by its declared value with evidence distinct from verdict. |

GATE-0 is unconditional and executes first, always. GATE-1 is the first gate where conditional operations execute. Any gate's execution mode and TOKEN output requirement can be verified in this manifest without reading the gate's body.

---

### GATE-0

Write these two lines as your opening output -- nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier -- at least one DOMAIN-TERMS term embedded]
```

Read repo context first (README, CLAUDE.md, package.json). DOMAIN-TERMS: 2-3 product-domain expert terms -- not generic software vocabulary. Write and close before TOKEN. TOKEN: domain-specific identifier (SIGNAL-GRIP, WORKFLOW-ANCHOR); generic placeholder alone (MECH, LOCK) fails.

**Completion:** Per manifest row GATE-0.

---

### GATE-1

```
FOCUS: ACTIVE -- [dimension] | INACTIVE
TOPIC: [inferred domain]
MARKET: [inferred market category]
```

Read repo context. Do not ask the user.

**Completion:** Per manifest row GATE-1.

---

### GATE-2

C0 before any competitor row:

```
## C0 -- [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior or feature -- not a generic category label]
```

Run WebSearch to verify at least one competitor claim.

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 -- [name] | -- | [capability] | ROOT | -- |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |

**Completion:** Per manifest row GATE-2.

---

### GATE-3

3 findings -- each references a named competitor row by label:

```
**Finding [N]: [Title]**
[Observation -- name competitor row by table label]
vs [TOKEN]: [connection to TOKEN mechanism -- TOKEN by declared value]
```

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [relationship to TOKEN mechanism -- TOKEN by name]
```

If FOCUS ACTIVE: gap must be uncontested across competitive + focus dimensions simultaneously; show the intersection.

**Completion:** Per manifest row GATE-3.

---

### GATE-4

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [user adjustment] | [which gate/section shifts] | STABLE / UNSTABLE -- [verdict; TOKEN by declared value] | [reasoning distinct from verdict] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE -- [verdict; TOKEN] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE -- [verdict; TOKEN] | [reasoning] |

**Completion:** Per manifest row GATE-4.

---

## V-03 -- Output format: native table replaces code-fence (direct C-24 fix)

**Axis:** Output format -- R7 V-03 scored C-23 PARTIAL because its code-fenced pipe-aligned manifest sat on the "table or equivalent" boundary. C-24 closes the loophole explicitly. This variation makes the minimum changes to R7 V-03: (1) convert the code-fence manifest to a native markdown table -- the direct C-24 fix; (2) add TOKEN to GATE-1, GATE-2, and GATE-4 completion conditions for C-25.
**Hypothesis:** R7 V-03 was correct in all other respects. The direct native-table conversion plus the C-25 completion-condition additions should produce a full score. The minimum-change approach isolates C-24 and C-25 as the sole variables -- if anything else in R7 V-03 was at risk, this variation will surface it.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Execute gates in sequence.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations |
|------|---------------|--------------------|
| GATE-0 | UNCONDITIONAL | DOMAIN-TERMS extraction -> TOKEN declaration |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference |
| GATE-2 | CONDITIONAL | C0 description, competitive map |
| GATE-3 | CONDITIONAL | Findings, whitespace |
| GATE-4 | CONDITIONAL | AMEND table |

GATE-0 is unconditional -- always runs first. GATE-1 is the first conditional gate. No conditional logic precedes GATE-0's completion. Any gate's execution mode is verifiable here without reading its body.

---

### GATE-0 [unconditional -- GATE-1 is the first conditional operation]

This gate is unconditional -- no focus detection, no auto-detect, no section headers, no conditional branching before or during it. GATE-1 is the first gate where conditional logic executes.

Write exactly these two lines as your opening output -- nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier -- at least one DOMAIN-TERMS term embedded]
```

Read repo context (README, CLAUDE.md, package.json) first. DOMAIN-TERMS: 2-3 product-domain expert terms -- not generic software vocabulary. Write and close before TOKEN. TOKEN: copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-ANCHOR); generic placeholder alone (MECH, LOCK) fails. TOKEN declared before all competitive content and all conditional logic.

**GATE-0 completion condition:** DOMAIN-TERMS closed. TOKEN closed. Both appear before all other output.

---

### GATE-1 [first conditional -- focus detection]

```
FOCUS: ACTIVE -- [dimension] | INACTIVE
TOPIC: [inferred domain]
MARKET: [inferred market category]
```

Read repo context. Do not ask the user.

**GATE-1 completion condition:** FOCUS, TOPIC, MARKET written. TOKEN (value declared in GATE-0) is the active inertia reference -- required by its declared value in every subsequent gate's output specification.

---

### GATE-2 [C0 and competitive map]

**C0 first -- before any competitor row:**

```
## C0 -- [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [specific C0 behavior or feature]
```

Mechanism must tie to a real C0 behavior. Generic category label alone fails.

Run WebSearch to verify at least one competitor claim.

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 -- [name] | -- | [capability] | ROOT | -- |
| [Comp 1] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | [inline citation] |
| [Comp 2] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |
| [Comp 3] | HIGH / MEDIUM / LOW | [differentiator] | [vs TOKEN mechanism] | -- |

Min 3 named competitors, explicit threat levels, 1+ inline citation.

**GATE-2 completion condition:** C0 first. Table: row 0 = C0, 3+ external rows, 1+ inline citation. `vs [TOKEN]` column header uses TOKEN by its declared value.

---

### GATE-3 [findings and whitespace]

**3 findings -- each references a named competitor row:**

```
**Finding [N]: [Title]**
[Observation -- name competitor row by label]
vs [TOKEN]: [finding's connection to TOKEN mechanism -- TOKEN by declared value]
```

No finding reads without GATE-2. TOKEN appears by its declared value, not by role description.

**Whitespace:**

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [how TOKEN mechanism relates to this gap -- TOKEN by name]
```

If FOCUS ACTIVE: gap uncontested across competitive + focus dimensions simultaneously; show what the focus lens reveals beyond the map.

**GATE-3 completion condition:** 3 findings with competitor references and `vs [TOKEN]` lines using TOKEN by declared value. Labeled whitespace with `[TOKEN] exposure:` field naming TOKEN.

---

### GATE-4 [AMEND]

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [user adjustment] | [which gate/section shifts] | STABLE / UNSTABLE -- [verdict; TOKEN by declared value] | [reasoning distinct from verdict] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE -- [verdict; TOKEN] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE -- [verdict; TOKEN] | [reasoning] |

Min 3 rows. Every cell filled. Evidence contains reasoning -- "Stable." alone fails.

**GATE-4 completion condition:** 3+ data rows, all four cells per row. Every Stability verdict cell references TOKEN by its declared value.

---

## V-04 -- Inertia framing: per-gate REQUIRED OUTPUTS blocks as explicit output specifications

**Axis:** Inertia framing -- each gate has an explicit REQUIRED OUTPUTS block that lists TOKEN as a named required output element. The REQUIRED OUTPUTS block is architecturally distinct from the completion condition text and serves as the unambiguous output specification for C-25. Inertia is maximally prominent: TOKEN threads through every gate's declared output requirements, not just its body instructions.
**Hypothesis:** An explicit numbered REQUIRED OUTPUTS list is the most defensible C-25 form -- consulting only the REQUIRED OUTPUTS block (not body prose, not the completion condition), a reader can confirm TOKEN is a named required element. This eliminates interpretive ambiguity about whether completion-condition prose qualifies as "the output specification." If V-01 (completion-condition prose) and V-04 (REQUIRED OUTPUTS block) both pass C-25, both forms are valid. If V-01 fails but V-04 passes, REQUIRED OUTPUTS blocks are the necessary form.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. The inertia mechanism token declared in GATE-0 threads through every gate -- it anchors the competitive map, grounds every finding, and frames every AMEND stability judgment. Execute gates in sequence.

---

### EXECUTION PLAN

| Gate | Execution mode | Primary operations | Notes |
|------|---------------|--------------------|-------|
| GATE-0 | UNCONDITIONAL | DOMAIN-TERMS extraction -> TOKEN declaration | Only unconditional gate; TOKEN declared before all conditional logic |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference | First conditional gate; TOKEN carries forward as active reference |
| GATE-2 | CONDITIONAL | C0 description, competitive map | `vs [TOKEN]` column header uses TOKEN by declared value |
| GATE-3 | CONDITIONAL | Findings, whitespace | TOKEN by name in every `vs [TOKEN]` line and `[TOKEN] exposure:` field |
| GATE-4 | CONDITIONAL | AMEND table | TOKEN by declared value in every Stability verdict cell |

GATE-0 is the only unconditional gate. GATE-1 is the first conditional gate. Any gate's mode is verifiable in this manifest without reading its body.

---

### GATE-0 [unconditional -- GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**
1. `DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]` -- closed on its own line before TOKEN
2. `TOKEN: [domain-adaptive identifier]` -- portable inertia reference; must include at least one DOMAIN-TERMS term; declared before all conditional logic

Write these as your opening output -- nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier -- at least one DOMAIN-TERMS term embedded]
```

Read repo context (README, CLAUDE.md, package.json) first. DOMAIN-TERMS: product-domain expert terms, not generic software vocabulary. TOKEN: copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-ANCHOR); generic placeholder alone (MECH, LOCK) fails.

This gate is unconditional -- no conditional branching before or during it. GATE-1 is the first gate with conditional logic.

---

### GATE-1 [first conditional -- focus detection and topic resolution]

**REQUIRED OUTPUTS:**
1. `FOCUS: ACTIVE -- [dimension] | INACTIVE`
2. `TOPIC: [inferred product domain]`
3. `MARKET: [inferred market category]`
4. TOKEN (value = TOKEN from GATE-0) -- the active inertia reference; required by its declared value in GATE-2, GATE-3, and GATE-4 output specifications

Read repo context. Do not ask the user for topic, competitor names, or market category.

---

### GATE-2 [C0 and competitive map -- TOKEN anchors the comparison column]

**REQUIRED OUTPUTS:**
1. C0 section before any competitor row: `[TOKEN]: [mechanism type] -> [specific C0 behavior]`
2. Competitive map table: row 0 = C0; `vs [TOKEN]` column header uses TOKEN by its declared value; min 3 external rows; min 1 inline WebSearch citation
3. TOKEN appears by declared value in: C0 section label, `vs [TOKEN]` column header, each competitor row's TOKEN comparison cell

**C0 -- before any competitor row:**

```
## C0 -- [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [Specific description tied to a real C0 behavior or feature -- not a generic category label]
```

Mechanism must name something C0 actually does or provides. "Inertia is high" without a product-specific anchor fails.

Run a WebSearch to verify at least one competitor claim.

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 -- [product name] | -- | [key capability] | ROOT | -- |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | -- |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | -- |

Min 3 named external competitors. No generic labels. Every row: explicit threat level.

---

### GATE-3 [findings and whitespace -- TOKEN by declared value in every required output field]

**REQUIRED OUTPUTS:**
1. 3 findings: each references a named competitor row by table label; each includes `vs [TOKEN]:` line with TOKEN by its declared value
2. Whitespace finding: specific uncontested dimension + `[TOKEN] exposure:` field naming TOKEN by declared value
3. If FOCUS ACTIVE: cross-dimensional whitespace finding naming the gap uncontested across competitive + focus dimensions simultaneously; TOKEN in the intersection rationale

```
**Finding [N]: [Title]**
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [how this finding relates to the TOKEN mechanism -- TOKEN must appear verbatim, by declared value]
```

Findings readable without GATE-2 fail.

```
WHITESPACE: [specific uncontested dimension -- not a generic statement]
[TOKEN] exposure: [how TOKEN mechanism relates to this gap -- TOKEN by name]
```

If FOCUS ACTIVE: gap must require both the competitive map and the focus lens to produce; show the intersection.

---

### GATE-4 [AMEND -- TOKEN in every output specification]

**REQUIRED OUTPUTS:**
1. AMEND schema: Input change, Output effect, Stability verdict, Evidence -- all four domain-neutral component names declared before data rows
2. 3+ data rows: every Stability verdict cell names TOKEN by its declared value; every Evidence cell contains reasoning distinct from verdict

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts -- focus dimension, depth level, competitor scope] | [which gate or section specifically shifts -- name it] | STABLE / UNSTABLE -- [verdict on whether [TOKEN] is affected -- TOKEN by declared value] | [reasoning distinct from verdict] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE -- [verdict on [TOKEN]] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE -- [verdict on [TOKEN]] | [reasoning] |

Min 3 rows. Every cell filled. Evidence distinct from verdict.

---

## V-05 -- Combined: EXECUTION CONTRACT with TOKEN column + dual-source REQUIRED OUTPUTS + schema declaration table

**Axis:** Combined -- lifecycle (EXECUTION CONTRACT heading + per-gate REQUIRED OUTPUTS blocks), inertia framing (dedicated "Required TOKEN output" column in manifest), output format (pre-AMEND schema declaration table retained from R7 V-05). Dual-source C-25 contract: TOKEN is named as a required output in both the manifest's dedicated column AND each gate's REQUIRED OUTPUTS block.
**Hypothesis:** The manifest's dedicated "Required TOKEN output" column makes C-25 contractually declared at the manifest level: a reader consulting the manifest for C-23 compliance simultaneously sees TOKEN's required-output status for every gate. The REQUIRED OUTPUTS blocks provide gate-level confirmation. If V-04 (REQUIRED OUTPUTS alone) and V-02 (manifest completion signal alone) both pass C-25, V-05's dual-source approach is maximally robust -- the decisive question is whether "Required TOKEN output" as an explicit manifest column label produces any scoring difference over "Completion signal" (V-02) that happens to name TOKEN.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project. Weave in the focus dimension if provided -- do not append it as a separate section. Execute each gate in sequence.

---

### EXECUTION CONTRACT

| Gate | Execution mode | Primary operations | Required TOKEN output |
|------|---------------|--------------------|----------------------|
| GATE-0 | UNCONDITIONAL | DOMAIN-TERMS extraction -> TOKEN declaration | TOKEN declared by name -- the literal first declared output |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference | TOKEN (from GATE-0) confirmed as active reference by its declared value |
| GATE-2 | CONDITIONAL | C0 description, competitive map | `vs [TOKEN]` column header names TOKEN by its declared value |
| GATE-3 | CONDITIONAL | Findings, whitespace | TOKEN by declared value in every `vs [TOKEN]` line and `[TOKEN] exposure:` field |
| GATE-4 | CONDITIONAL | AMEND table | TOKEN by declared value in every Stability verdict cell |

GATE-0 is unconditional and executes first, always. GATE-1 is the first gate where conditional operations execute. No conditional logic precedes GATE-0's completion. Any gate's execution mode and required TOKEN output can be verified in this contract without reading the gate's body.

---

### GATE-0 [UNCONDITIONAL -- GATE-1 is the first conditional operation]

**REQUIRED OUTPUTS:**
1. `DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]` -- closed on its own line, before TOKEN
2. `TOKEN: [domain-adaptive identifier]` -- must embed at least one DOMAIN-TERMS term; declared before all conditional logic

Write exactly these two lines as your opening output -- nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier -- must include at least one term from DOMAIN-TERMS above]
```

Read repo context (README, CLAUDE.md, package.json, or equivalent) before writing. DOMAIN-TERMS: 2-3 product-domain expert terms -- not generic software vocabulary. TOKEN: copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK); generic placeholder alone (MECH, LOCK) fails.

This gate is unconditional. No conditional branching, no focus detection, no auto-detect, no section structure before or during it. GATE-1 is the first gate with conditional logic.

---

### GATE-1 [CONDITIONAL, first -- focus detection and topic resolution]

**REQUIRED OUTPUTS:**
1. `FOCUS: ACTIVE -- [dimension] | INACTIVE`
2. `TOPIC: [inferred product domain]`
3. `MARKET: [inferred market category]`
4. TOKEN (value: TOKEN from GATE-0) -- active inertia reference; required by its declared value in every subsequent gate's required output

Read repo context. Do not ask the user for topic, competitor names, or market category.

---

### GATE-2 [CONDITIONAL -- C0 description and competitive map]

**REQUIRED OUTPUTS:**
1. C0 section: `[TOKEN]: [mechanism type] -> [specific C0 behavior]` -- before any competitor row
2. Competitive map: row 0 = C0; `vs [TOKEN]` column header uses TOKEN by declared value; 3+ external rows; 1+ inline citation

**C0 -- before any competitor row:**

```
## C0 -- [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] -> [Specific description tied to a real C0 behavior or feature -- not a generic category label]
```

Mechanism must name something C0 actually does or provides. "Inertia is high" without a product-specific anchor fails.

Run a WebSearch to verify at least one competitor claim before completing this gate.

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 -- [product name] | -- | [key capability] | ROOT | -- |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | -- |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | -- |

Min 3 named external competitors. No generic labels. Every row: explicit threat level.

---

### GATE-3 [CONDITIONAL -- findings and whitespace]

**REQUIRED OUTPUTS:**
1. 3 findings: each references a named competitor row by table label; each includes `vs [TOKEN]:` line with TOKEN by declared value
2. Whitespace finding: specific dimension + `[TOKEN] exposure:` field naming TOKEN by declared value
3. If FOCUS ACTIVE: cross-dimensional gap named as uncontested across competitive + focus dimensions simultaneously; TOKEN in intersection rationale

```
**Finding [N]: [Title]**
[Observation -- reference named competitor row by table label]
vs [TOKEN]: [connection to TOKEN mechanism -- TOKEN must appear by its declared value]
```

Findings readable without GATE-2 fail.

```
WHITESPACE: [specific uncontested dimension]
[TOKEN] exposure: [how TOKEN mechanism relates to this gap -- TOKEN by name]
```

If FOCUS ACTIVE: gap must require both the competitive map and the focus lens; show what the focus dimension adds that the map alone cannot surface; include TOKEN in the intersection rationale.

---

### GATE-4 [CONDITIONAL -- AMEND]

**AMEND entry schema -- all four required components enumerated by rubric-standard names:**

| # | Component | Rubric-standard name | Description |
|---|-----------|---------------------|-------------|
| 1 | Input | **Input change** | The adjustment the user makes -- focus dimension, depth level, competitor scope |
| 2 | Effect | **Output effect** | The specific change in output -- name the gate or section affected |
| 3 | Verdict | **Stability verdict** | Whether TOKEN is affected -- STABLE / UNSTABLE required; TOKEN by declared value |
| 4 | Support | **Evidence** | Reasoning supporting the stability verdict -- logically distinct from the verdict |

**REQUIRED OUTPUTS:**
1. Schema declaration (above) present before data rows
2. 3+ data rows: every Stability verdict cell names TOKEN by its declared value; Evidence cell contains reasoning distinct from verdict

**AMEND data table:**

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts -- focus dimension, depth level, competitor scope] | [which gate or section specifically shifts -- name it] | STABLE / UNSTABLE -- [verdict on whether [TOKEN] is affected -- TOKEN by declared value] | [reasoning distinct from verdict] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE -- [verdict on [TOKEN]] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE -- [verdict on [TOKEN]] | [reasoning] |

Min 3 rows. Every cell filled. Evidence distinct from verdict.

---

## Composite hypothesis table

| Variation | C-24 prediction | C-25 prediction | Critical question |
|-----------|----------------|----------------|-------------------|
| V-01 | PASS -- native markdown table (R7 V-01 baseline) | PASS -- TOKEN added by name to GATE-1 ("TOKEN by its declared value is required in every subsequent gate's output"), GATE-2 ("`vs [TOKEN]` column header uses TOKEN by its declared value"), and GATE-4 ("every Stability verdict cell references TOKEN by its declared value") completion conditions | Does "TOKEN by its declared value" in a completion-condition phrase satisfy C-25's "output specification"? Establishes the minimum viable form. |
| V-02 | PASS -- native markdown table in EXECUTION MANIFEST | PASS -- Manifest completion-signal column explicitly names TOKEN for every gate row; a reader consulting only the manifest sees TOKEN's required-output status for all 5 gates | Does the manifest completion-signal column qualify as each gate's "output specification" for C-25, or must TOKEN appear in gate body text? |
| V-03 | PASS -- direct conversion: R7 V-03 code-fence to native pipe-and-hyphen table; eliminates the "or equivalent" boundary that caused C-24 FAIL | PASS -- TOKEN added to GATE-1, GATE-2, GATE-4 completion conditions; same strategy as V-01 | Does the native-table conversion plus minimal C-25 additions produce a full score? Are there other elements of R7 V-03 at risk beyond C-24? |
| V-04 | PASS -- native markdown table in EXECUTION PLAN | PASS -- Explicit REQUIRED OUTPUTS blocks for every gate list TOKEN as a numbered required element; most unambiguous form -- consulting only the REQUIRED OUTPUTS block confirms TOKEN is required | Are REQUIRED OUTPUTS blocks a stronger C-25 form than completion-condition phrases, or do both satisfy equally? |
| V-05 | PASS -- native markdown table in EXECUTION CONTRACT; dedicated "Required TOKEN output" column makes C-25 status visible in the manifest itself | PASS -- Dual-source: manifest "Required TOKEN output" column names TOKEN for every gate AND per-gate REQUIRED OUTPUTS blocks name TOKEN; pre-AMEND schema declaration retained | Does dual-source TOKEN declaration produce any advantage over single-source? Does "Required TOKEN output" as an explicit manifest column label add clarity over a completion-signal column naming TOKEN? |

**R8 decisive questions resolved by scorecard:**
1. V-01/V-03: Does adding TOKEN to completion-condition phrases satisfy C-25? Establishes the minimum viable form.
2. V-02: Does the manifest completion-signal column serve as the gate output specification? Extends manifest-as-contract to C-25.
3. V-04: Are REQUIRED OUTPUTS blocks necessary, or is completion-condition prose sufficient? Strongest vs. minimal C-25 form.
4. V-05: Does dual-source declaration produce redundancy value? Does "Required TOKEN output" as an explicit column label add anything beyond a completion-signal column that names TOKEN?
5. V-03: Are there elements of R7 V-03 at risk beyond C-24?

**Predicted winner:** V-01 through V-05 all at 100 (17/17 aspirational = 10 pts, 0.588 each).
