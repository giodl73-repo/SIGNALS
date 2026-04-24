Written to `simulations/quest/variations/discover-competitors-alt-variations-R5-2026-03-18.md`.

---

## discover-competitors-alt — Variations R5

**Baseline:** R4 V-01/V-04/V-05 scored 100. Three new criteria for R5: **C-18**, **C-19**, **C-20**.

**The structural tension R5 exposes:** C-18 requires DOMAIN-TERMS as an output artifact *before* TOKEN. C-19 requires TOKEN as the *literal first output* — before focus detection, auto-detect, section headers, and conditional branching. These criteria pull in opposite directions. Every variation makes a bet on how to resolve it.

| Variation | Axis | Architecture | Key bet |
|-----------|------|---|---|
| **V-01** | Role sequence | `DOMAIN-TERMS → TOKEN → FOCUS → auto-detect → C0 → map → findings → whitespace → AMEND` (numbered 4-part schema) | DOMAIN-TERMS is not "conditional/procedural logic" per C-19's prohibited list — satisfies *both* C-18 and C-19 |
| **V-02** | Output format | `TOKEN → DOMAIN-CHECK → FOCUS → auto-detect → C0 → ...` AMEND as explicit 4-column table | TOKEN absolute first satisfies C-19; DOMAIN-CHECK post-TOKEN means C-18 fails; 4-column headers satisfy C-20 |
| **V-03** | Phrasing register | Same DOMAIN-TERMS → TOKEN architecture as V-01, conversational imperative throughout | Conversational "write and close DOMAIN-TERMS before TOKEN" is contractual enough for C-18; C-20 risk — does inline prose schema satisfy "schema a reader can consult"? |
| **V-04** | Inertia framing | DOMAIN-TERMS → ROOT (TOKEN renamed ROOT, gravitational framing), every section orbits ROOT, AMEND as 4-column table with ROOT VERDICT column | ROOT framing deepens C-11 propagation; same C-18/C-19 bet as V-01 |
| **V-05** | Lifecycle emphasis | GATE-0 (unconditional: DOMAIN-TERMS then TOKEN) → GATE-1 (first conditional: focus) → GATE-2 → GATE-3 → GATE-4 | Cleanest structural argument for both C-18 and C-19: GATE-0 names itself as pre-logic; GATE-1 is the first conditional gate; TOKEN is the last output before any logic |

**The decisive scoring question:** Does "the literal first output" in C-19 mean (a) the first line written overall — making DOMAIN-TERMS a C-19 violation in V-01/V-03/V-04/V-05 — or (b) the first output before conditional/procedural operations — making DOMAIN-TERMS unconditional vocabulary extraction that doesn't count? V-05's GATE-0 architecture makes the strongest structural argument for interpretation (b).
n-formal prose? |
| **V-04** | Inertia framing — gravitational anchor, ROOT replaces TOKEN, C-18 priority, AMEND as 4-column table | ~99.17 | Does ROOT terminology with DOMAIN-TERMS → ROOT sequencing deepen C-11 inertia propagation while retaining C-18 structural compliance? Do ROOT references throughout findings produce richer or formulaic downstream anchoring? |
| **V-05** | Lifecycle emphasis — gated phases, GATE-0 pairs DOMAIN-TERMS + TOKEN before all logic | ~100 | Does a two-output GATE-0 (DOMAIN-TERMS then TOKEN, both unconditional) satisfy C-19 by argument that "conditional or procedural logic" refers to GATE-1+ operations, while satisfying C-18 by structural artifact sequencing within GATE-0? |

**Structural choices by variation:**

- **V-01:** `STEP 0` produces `DOMAIN-TERMS:` then `TOKEN:` as a dedicated pre-phase, both before focus detection. Hypothesis: DOMAIN-TERMS is not on C-19's prohibited list. AMEND uses inline numbered 4-part schema.
- **V-02:** `TOKEN:` is the first output line with no preamble. DOMAIN-TERMS appears as a post-TOKEN verification note. AMEND is a 4-column table with headers functioning as the C-20 schema.
- **V-03:** Conversational voice throughout. "Your first line must be DOMAIN-TERMS: ... Your second line must be TOKEN: ..." AMEND uses numbered list with bold component labels.
- **V-04:** DOMAIN-TERMS → ROOT (token renamed ROOT throughout). Phase 0 = "orbit initialization." Every section header references ROOT. AMEND 4-column table includes ROOT VERDICT column.
- **V-05:** Four gates. GATE-0 is unconditional — produces only DOMAIN-TERMS then TOKEN. GATE-1 = focus resolution (first conditional operation). GATE-2 = auto-detect + C0 + map. GATE-3 = findings + whitespace. GATE-4 = AMEND 4-column table.

---

## V-01 — Role sequence: DOMAIN-TERMS first, TOKEN second, named AMEND schema

**Axis:** Role sequence — pre-logic extraction block before any conditional operations.
**Hypothesis:** DOMAIN-TERMS → TOKEN is the correct sequence for satisfying both C-18 and C-19. DOMAIN-TERMS extraction is not "focus detection, auto-detect, a section header, or conditional branching" — it is an unconditional vocabulary commitment. TOKEN follows immediately. Focus detection comes third. This sequence satisfies C-19 if the four prohibited operations in C-19 are interpreted as the exhaustive prohibited set.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if one was provided. Work through the following steps in order. Do not reorder them.

---

### STEP 0 — Vocabulary and token commitment (unconditional)

This step runs before any focus detection, auto-detect, or section output. It has no branches. Execute it first, always.

Write these two lines as your opening output — nothing before them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available from repo context]
TOKEN: [domain-adaptive identifier — must include at least one term from DOMAIN-TERMS above]
```

**DOMAIN-TERMS rules:**
- Read the repo context (README, CLAUDE.md, package.json, or equivalent).
- Extract 2–3 product-domain terms that are specific to this repo and its function.
- Write `DOMAIN-TERMS:` and close the line before writing anything else.
- Do not move to TOKEN until DOMAIN-TERMS is written.

**TOKEN rules:**
- TOKEN is the portable inertia reference. It will appear in every downstream section by name.
- The token must include at least one term from the DOMAIN-TERMS line you just wrote.
- A generic placeholder alone (MECH, LOCK, INERTIA-REF) fails — the token must be domain-adaptive.
- Valid examples given DOMAIN-TERMS containing "SIGNAL, PLUGIN, TOPIC": `SIGNAL-GRIP`, `PLUGIN-LOCK`, `TOPIC-ANCHOR`.
- A role description ("the inertia mechanism," "the C0 stickiness factor") is not a token. A copyable identifier is.
- Write `TOKEN:` immediately after DOMAIN-TERMS. Nothing between them.

---

### STEP 1 — Focus resolution

After TOKEN is declared, resolve the focus dimension:

- If a focus dimension was provided as input: write `FOCUS: ACTIVE — [dimension]`
- If no focus dimension was provided: write `FOCUS: INACTIVE`

Do not ask the user for the focus. Proceed immediately.

---

### STEP 2 — Topic auto-detection

Read the repo context to identify the product domain and plausible competitor categories. Write:

```
TOPIC: [inferred product domain]
MARKET: [inferred market category]
```

Do not ask the user for the topic, competitor names, or market category. Proceed immediately.

---

### STEP 3 — C0 (current solution)

Describe the current solution **before naming any external competitor.**

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [Specific description tied to what C0 does or provides — not a generic category label]
```

The mechanism must be tied to a specific behavior or feature of C0. "Inertia is high" or a category name without a product-specific description does not pass.

---

### STEP 4 — Competitive map

Produce a comparison table. Row 0 is C0:

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | [inline citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |

**Rules:**
- Minimum 3 named external competitors. No generic labels ("various startups," "open-source tools").
- Every row: explicit HIGH / MEDIUM / LOW threat level.
- At least one external row: inline WebSearch citation (URL or publication name) in the Source cell. Not a footnote block.
- The `vs [TOKEN]` column header uses TOKEN by name.

---

### STEP 5 — Findings

Produce exactly 3 findings. Each finding must reference at least one named competitor row by its table label. No finding may be free-floating prose that could be written without the competitive map.

```
**Finding 1: [Title]**
[Observation] (ref: [Competitor row label])
vs [TOKEN]: [How this finding relates to the inertia mechanism named in STEP 3]

**Finding 2: [Title]**
[Observation] (ref: [Competitor row label])
vs [TOKEN]: [How this finding relates to the inertia mechanism]

**Finding 3: [Title]**
[Observation] (ref: [Competitor row label])
vs [TOKEN]: [How this finding relates to the inertia mechanism]
```

Findings that read as general domain knowledge without tying back to a specific competitor entry do not pass.

---

### STEP 6 — Whitespace

Name one uncontested space or gap that no listed competitor owns. State it as a labeled finding. Do not use a generic statement — name the specific uncontested dimension.

**If FOCUS is INACTIVE:** Name the whitespace in competitive terms only.

**If FOCUS is ACTIVE:** The gap must be uncontested across both the competitive dimension and the focus dimension simultaneously. The finding cannot be produced by dropping the focus lens — show the intersection. State what the focus dimension adds that the competitive map alone would not surface.

---

### STEP 7 — AMEND

List 3 adjustments. Each entry must follow this schema exactly — all four components are required by name. An entry missing any component does not pass.

```
**Amendment 1**
1. Input change: [what the user adjusts — e.g., shift focus dimension, adjust depth, narrow competitor set]
2. Output effect: [what changes in the output as a result — name the specific section or content that shifts]
3. Stability verdict: STABLE | UNSTABLE — [one-sentence verdict on whether [TOKEN] is affected]
4. Evidence: [reasoning that supports the stability verdict — not a restatement of the verdict]

**Amendment 2**
1. Input change: ...
2. Output effect: ...
3. Stability verdict: STABLE | UNSTABLE — ...
4. Evidence: ...

**Amendment 3**
1. Input change: ...
2. Output effect: ...
3. Stability verdict: STABLE | UNSTABLE — ...
4. Evidence: ...
```

A stability verdict without evidence does not pass. An entry that lists only input change and output effect without addressing [TOKEN] stability does not pass.

---

## V-02 — Output format: TOKEN absolute first, 4-column table AMEND

**Axis:** Output format — TOKEN as the literal first output line; AMEND rendered as a 4-column table whose headers function as the C-20 schema enumeration.
**Hypothesis:** Placing TOKEN as the absolute first output line satisfies C-19 fully. DOMAIN-TERMS extraction moves to a post-TOKEN verification step (C-18 will fail — no artifact before TOKEN). The AMEND table headers `Input change | Output effect | Stability verdict | Evidence` are themselves a named schema that satisfies C-20 without requiring a numbered list.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if one was provided.

---

### Output Step 1 — Token declaration (FIRST OUTPUT LINE)

Your first output line — before any section, before any detection, before any logic — must be:

```
TOKEN: [domain-adaptive identifier for the inertia mechanism]
```

**Rules for TOKEN:**
- Read the repo context before writing. Identify the product domain and extract a domain-specific term for the token identifier.
- The token must include at least one product-domain term specific to this repo. Generic placeholders alone (MECH, LOCK, INERTIA-REF) fail.
- Valid examples for a signal-gathering developer tool: `SIGNAL-LOCK`, `WORKFLOW-GRIP`, `PLUGIN-ANCHOR`.
- A role description is not a token. A copyable identifier is.
- Write TOKEN as the literal first line of your output. Nothing precedes it.

After TOKEN is written, confirm the domain term you used:

```
DOMAIN-CHECK: [the repo-context term embedded in TOKEN] — confirmed
```

---

### Output Step 2 — Focus resolution

```
FOCUS: ACTIVE — [dimension] | INACTIVE
```

Do not ask the user for the focus dimension. Proceed immediately.

---

### Output Step 3 — Topic auto-detection

```
TOPIC: [inferred product domain]
MARKET: [inferred market category]
```

Read the repo context (README, CLAUDE.md, package.json, or equivalent). Do not prompt the user.

---

### Output Step 4 — C0 (current solution)

Describe the current solution before naming any external competitor.

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [Specific description tied to C0's behavior or feature set]
```

The mechanism must be tied to something C0 does or provides — not a category label applied generically.

---

### Output Step 5 — Competitive map

Row 0 is C0:

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [comparison] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [comparison] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [comparison] | — |

Minimum 3 named external competitors with explicit threat levels. At least one row carries an inline WebSearch citation in the Source cell — not a footnote.

---

### Output Step 6 — Findings

Produce 3 findings. Each references at least one named competitor row by label. No free-floating claims.

```
**Finding 1: [Title]**
[Observation] (ref: [Competitor]) — vs [TOKEN]: [inertia relevance]

**Finding 2: [Title]**
[Observation] (ref: [Competitor]) — vs [TOKEN]: [inertia relevance]

**Finding 3: [Title]**
[Observation] (ref: [Competitor]) — vs [TOKEN]: [inertia relevance]
```

---

### Output Step 7 — Whitespace

Name one uncontested gap no listed competitor owns. State it as a labeled finding with the specific uncontested dimension.

If FOCUS is ACTIVE: gap must be uncontested across both the competitive dimension and the focus dimension. Show the intersection.

---

### Output Step 8 — AMEND

The AMEND section uses a 4-column table. The column headers are the required schema — a reader consulting only the headers can identify all four required components. Every row must fill all four cells. A Stability verdict cell containing only a verdict tag without reasoning in the Evidence cell does not pass.

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts] | [what section or content shifts] | STABLE / UNSTABLE | [reasoning for verdict] |
| 2 | [what the user adjusts] | [what section or content shifts] | STABLE / UNSTABLE | [reasoning for verdict] |
| 3 | [what the user adjusts] | [what section or content shifts] | STABLE / UNSTABLE | [reasoning for verdict] |

**Rules:**
- Minimum 3 rows.
- Every row: explicit STABLE / UNSTABLE verdict and supporting reasoning in the Evidence cell.
- "Stable" alone fails the Evidence column — the cell must contain the reason.
- The Stability verdict column addresses whether TOKEN is affected by the input change.

---

## V-03 — Phrasing register: conversational imperative, C-18 priority, inline schema

**Axis:** Phrasing register — all instructions written in direct conversational imperative. Same structural architecture as V-01 (DOMAIN-TERMS → TOKEN → focus), but language register shifts from formal numbered steps to direct address.
**Hypothesis:** Conversational register is sufficient to maintain C-18 structural compliance if the extraction contract is stated explicitly. The secondary test: whether an inline 4-part schema in numbered prose satisfies C-20 when compared to a formal template block.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project. If a focus dimension was provided, weave it into the analysis — don't append it separately.

Here is how to produce the output, step by step.

---

**Before writing anything else, extract domain vocabulary and declare the token.**

Read the repo context — README, CLAUDE.md, package.json, or whatever equivalent exists. Identify 2–3 terms that are specific to this product's domain and function. Write them out first:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
```

Write that line and close it. Once DOMAIN-TERMS is written, pick a token identifier. The token must include at least one term from the DOMAIN-TERMS line you just wrote — this is how you make it domain-specific rather than generic. Write:

```
TOKEN: [your domain-adaptive identifier]
```

That's the entire preamble. Do not write anything else before these two lines. Do not ask the user for a topic, competitor list, or market category.

---

**Resolve the focus dimension.**

After TOKEN is written, check whether a focus dimension was provided. Write one of:
- `FOCUS: ACTIVE — [the dimension provided]`
- `FOCUS: INACTIVE`

---

**Auto-detect the topic.**

Read the repo context and write:
- `TOPIC: [inferred domain]`
- `MARKET: [inferred market category]`

Do not prompt the user.

---

**Describe the current solution (C0) before naming any competitor.**

Open a C0 section. Use TOKEN by name to label the inertia mechanism:

```
## C0 — [product name]
[TOKEN]: [mechanism type — switching cost, habit lock-in, or workaround satisfaction] → [a specific description tied to what C0 does or provides]
```

The mechanism description must tie to a real behavior or feature of C0. A category label applied generically ("inertia is high") does not satisfy this. Pick the mechanism type that fits, then explain exactly why it holds for this product.

---

**Build the competitive map.**

Produce a table. Put C0 in row 0. The `vs [TOKEN]` column header uses TOKEN by name.

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT | — |
| [name] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | [inline citation if available] |

Name at least 3 external competitors — no generic buckets like "open-source alternatives." Every row gets an explicit threat level. For at least one external row, add an inline WebSearch citation (URL or publication name) right in the Source cell — not in a footnote below the table.

---

**Write 3 findings.**

Each finding must reference at least one named competitor row by label. If a finding could be written without looking at the competitive map, it doesn't count.

For each finding, include a `vs [TOKEN]` line connecting back to the inertia mechanism:

```
**Finding [N]: [Title]**
[Observation — name the competitor row]
vs [TOKEN]: [how this finding relates to the inertia mechanism]
```

---

**Identify the whitespace.**

Name one uncontested gap — a space no competitor on the map owns. Give it a label. Don't use a generic statement; name the specific uncontested dimension.

If FOCUS is ACTIVE: the gap must be uncontested across both the competitive dimension and the focus dimension at the same time. Show what the focus lens adds that the competitive map alone couldn't surface.

---

**Write the AMEND section.**

List 3 amendments. For each one, you need exactly four things — all four are required and all four must be named explicitly:

1. **Input change:** what the user would adjust
2. **Output effect:** what changes in the output as a result — be specific about which section shifts
3. **Stability verdict:** whether TOKEN is affected — state STABLE or UNSTABLE with a one-sentence verdict
4. **Evidence:** the reasoning that supports the stability verdict — not a restatement of the verdict

Write each amendment in this form:

```
**Amendment [N]**
1. Input change: [description]
2. Output effect: [description]
3. Stability verdict: STABLE | UNSTABLE — [one sentence]
4. Evidence: [reasoning]
```

A stability verdict without evidence doesn't pass. If you write "Stable" without saying why, the entry is incomplete. Every amendment must include all four named components.

---

## V-04 — Inertia framing: gravitational anchor, ROOT token, DOMAIN-TERMS priority

**Axis:** Inertia framing — the inertia mechanism is framed as a gravitational center (ROOT) rather than a reference token. DOMAIN-TERMS → ROOT sequencing identical to V-01, but ROOT terminology and "orbit" framing reinforce C-11 propagation throughout. AMEND as 4-column table with ROOT VERDICT column.
**Hypothesis:** Renaming TOKEN to ROOT and framing every section as orbiting the gravitational anchor deepens C-11 inertia propagation. DOMAIN-TERMS → ROOT before focus detection carries the same C-18/C-19 structural bet as V-01. The secondary test: does gravitational framing produce richer or formulaic downstream ROOT references in findings and AMEND?

---

You are running `discover-competitors-alt`. Produce a competitive analysis centered on the inertia mechanism of the current solution. Every section of the output orbits this mechanism. A focus dimension may be woven in if provided.

---

### Phase 0 — Establish the gravitational center

Before any other output, establish the two-line gravitational anchor. This phase is unconditional — no branches, no detection.

**Line 1 — Orbit initialization:**

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
```

Read the repo context (README, CLAUDE.md, package.json, or equivalent). Extract the domain vocabulary that defines this product's identity. Write and close the DOMAIN-TERMS line before proceeding to ROOT.

**Line 2 — ROOT declaration:**

```
ROOT: [domain-adaptive identifier including at least one DOMAIN-TERMS term]
```

ROOT is the inertia mechanism identifier. It will appear in every downstream section by name — column headers, finding labels, and AMEND stability columns. ROOT functions identically to a portable token: it is a copyable identifier, not a role description. A generic placeholder (MECH, LOCK, INERTIA-REF alone) fails. A domain-adaptive identifier (SIGNAL-LOCK, WORKFLOW-ANCHOR, PLUGIN-GRIP) passes.

Do not write any other output before DOMAIN-TERMS and ROOT.

---

### Phase 1 — Focus and topic resolution

After ROOT is established, resolve focus and topic. These are the first operations with conditional logic.

```
FOCUS: ACTIVE — [dimension] | INACTIVE
TOPIC: [inferred product domain]
MARKET: [inferred market category]
```

Read the repo context. Do not prompt the user.

---

### Phase 2 — C0: the gravitational mass

Describe C0 before naming any external competitor. C0 is the host of ROOT — the current solution whose inertia mechanism anchors the entire analysis.

```
## C0 — [product name]
ROOT ([ROOT]): [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [Specific description — tied to a real behavior or feature of C0, not a generic label]
```

---

### Phase 3 — Competitive orbits

Produce a competitive map. Row 0 is C0. The `vs [ROOT]` column header uses ROOT by name. Every external competitor is assessed against ROOT's gravitational pull.

| Competitor | Threat | Differentiator | vs [ROOT] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT origin | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [displacement relative to ROOT] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [displacement relative to ROOT] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [displacement relative to ROOT] | — |

**Rules:**
- Minimum 3 named external competitors. No generic labels.
- Every row: explicit HIGH / MEDIUM / LOW threat level.
- At least one row: inline WebSearch citation in the Source cell (not a footnote).

---

### Phase 4 — Orbital findings

Produce 3 findings. Each finding references at least one named competitor row by label. Each finding includes a ROOT reference that names ROOT and states how the finding relates to the gravitational mechanism.

```
**Finding [N]: [Title]**
[Observation — reference competitor row label]
ROOT orbit: vs [ROOT] — [how this finding connects to the ROOT mechanism]
```

Findings that could be written without Phase 3 fail the grounding test.

---

### Phase 5 — Escape velocity (whitespace)

Name the gap — the space no listed competitor has claimed. This is the territory where ROOT's gravitational influence is weakest.

**If FOCUS is INACTIVE:** Identify the gap in competitive terms only. Name the specific uncontested dimension — a generic statement fails.

**If FOCUS is ACTIVE:** The gap must be uncontested across both the competitive map and the focus dimension. Show the intersection. Explain what ROOT's mechanism does not cover that the focus lens exposes.

---

### Phase 6 — AMEND

The AMEND table enumerates all four required components as column headers. A reader consulting only the headers can identify what each row must contain. Every cell in every row must be filled. A ROOT VERDICT cell without supporting reasoning in the Evidence cell does not pass.

| # | Input change | Output effect | ROOT verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts — focus dimension, depth, competitor scope] | [which section or content shifts — be specific] | STABLE / UNSTABLE | [reasoning for ROOT verdict — why does or doesn't ROOT shift?] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE | [evidence] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE | [evidence] |

**Rules:**
- Minimum 3 rows.
- `ROOT verdict` column uses ROOT by name.
- Evidence column must contain reasoning — "Stable" alone fails.
- Every row addresses ROOT stability.

---

## V-05 — Lifecycle emphasis: gated phases, GATE-0 pairs DOMAIN-TERMS and TOKEN before all logic

**Axis:** Lifecycle emphasis — explicit gated phases with PASS conditions per gate. GATE-0 is unconditional and produces exactly two outputs: DOMAIN-TERMS then TOKEN. All conditional operations are in GATE-1 and later.
**Hypothesis:** GATE-0 satisfies C-18 (DOMAIN-TERMS before TOKEN as a structural artifact) by placing both lines as the sole outputs of an unconditional pre-phase. GATE-0 satisfies C-19 (TOKEN before conditional logic) because GATE-1 is the first gate containing conditional operations — TOKEN is produced before GATE-1 opens. Whether "literal first output" in C-19 means the single first line overall (in which case DOMAIN-TERMS blocks C-19) or "first committed identifier before conditional logic" (in which case both pass) is the key scoring question this variation surfaces.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. Execute each gate in sequence. Do not open a gate until the previous gate's completion condition is satisfied.

---

### GATE-0 — Pre-declaration (unconditional)

**What this gate produces:** DOMAIN-TERMS and TOKEN. No focus detection, no auto-detect, no section headers, no branching of any kind. This gate runs unconditionally before any logic.

**GATE-0 output contract — write these two lines and nothing else:**

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — must include at least one term from DOMAIN-TERMS above]
```

**Rules:**
- Read the repo context before producing GATE-0 output. Identify the product vocabulary.
- DOMAIN-TERMS is the first line. Write it and close it before writing TOKEN.
- TOKEN follows immediately on the next line. Nothing between DOMAIN-TERMS and TOKEN.
- TOKEN must include at least one term from the DOMAIN-TERMS line. Generic placeholders alone (MECH, LOCK, INERTIA-REF) fail.
- No section header, no preamble, no conditional logic before or between these two lines.

**GATE-0 completion condition:** `DOMAIN-TERMS:` line written and closed. `TOKEN:` line written and closed. Both lines appear before any other output. Nothing else appears in this gate.

---

### GATE-1 — Focus and topic resolution

**What this gate produces:** Focus verdict and topic identification. This is the first gate with conditional logic.

```
FOCUS: ACTIVE — [dimension] | INACTIVE
TOPIC: [inferred product domain]
MARKET: [inferred market category]
```

Read the repo context. Do not ask the user for topic, competitor names, or market category.

**GATE-1 completion condition:** FOCUS verdict written. TOPIC and MARKET written.

---

### GATE-2 — C0 and competitive map

**What this gate produces:** C0 description (first) then the competitive table.

**C0 — current solution (produced before any competitor is named):**

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [Specific description tied to C0's behavior or feature set — not a generic label]
```

**Competitive map:**

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |

Rules: minimum 3 named external competitors; no generic labels; every row has an explicit threat level; at least one row carries an inline WebSearch citation in the Source cell.

**GATE-2 completion condition:** C0 section written before competitor rows. Competitive table has row 0 = C0 and at least 3 named external rows. At least one Source cell carries an inline citation.

---

### GATE-3 — Findings and whitespace

**What this gate produces:** 3 grounded findings and one labeled whitespace finding.

**Findings:** Each finding references at least one named competitor row by label. Each finding includes a `vs [TOKEN]` line connecting back to the TOKEN mechanism.

```
**Finding [N]: [Title]**
[Observation — name competitor row label]
vs [TOKEN]: [how this finding relates to the TOKEN mechanism from GATE-2]
```

Findings that could be written without GATE-2 fail the grounding test.

**Whitespace:** Name one uncontested gap no listed competitor owns. State the specific uncontested dimension — a generic statement fails.

If FOCUS is INACTIVE: competitive whitespace only.

If FOCUS is ACTIVE: the gap must be uncontested across both the competitive dimension and the focus dimension. Show the intersection — state what the focus lens adds that the competitive map alone would not surface.

**GATE-3 completion condition:** 3 findings written, each with a competitor reference and a `vs [TOKEN]` line. Whitespace finding labeled and specific.

---

### GATE-4 — AMEND

**What this gate produces:** An amendment table with all four required components enumerated as column headers.

The column headers function as the schema — a reader consulting only the headers can identify all four required components without reading the rows.

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts — focus dimension, depth level, competitor scope] | [which section or content shifts — name the gate or section] | STABLE / UNSTABLE — [one-sentence verdict on whether [TOKEN] is affected] | [reasoning that supports the verdict — not a restatement of it] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [one-sentence verdict] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [one-sentence verdict] | [reasoning] |

**Rules:**
- Minimum 3 rows.
- Every cell must be filled. A verdict without evidence does not pass. "Stable" alone fails the Evidence column.
- Stability verdict column uses TOKEN by name in the header.
- Every Evidence cell provides reasoning distinct from the verdict.

**GATE-4 completion condition:** Table has at least 3 data rows. Every row fills all four cells. Every Stability verdict cell contains a verdict. Every Evidence cell contains reasoning.

---

## Composite hypothesis table

| Variation | C-18 prediction | C-19 prediction | C-20 prediction | Critical question |
|-----------|----------------|----------------|----------------|-------------------|
| V-01 | PASS — DOMAIN-TERMS artifact closes before TOKEN | PASS or FAIL — depends on whether DOMAIN-TERMS is classified as "conditional/procedural logic" in C-19's prohibited list | PASS — numbered schema names all four components with explicit labels | Is DOMAIN-TERMS classified as conditional/procedural logic? |
| V-02 | FAIL — no DOMAIN-TERMS artifact before TOKEN; DOMAIN-CHECK is a post-TOKEN note, not a prior artifact | PASS — TOKEN is literal first output, nothing before it | PASS — 4-column table headers explicitly name all four components | Does C-20 pass via table-header enumeration alone without numbered schema? |
| V-03 | PASS — DOMAIN-TERMS artifact before TOKEN in conversational form; "write and close DOMAIN-TERMS" is contractual | PASS or FAIL — same C-19 question as V-01 | PASS or PARTIAL — "all four are required and all four must be named explicitly" may satisfy C-20; risk is that conversational list reads as instructional rather than schema | Does conversational numbered list satisfy C-20's "schema a reader can consult" test? |
| V-04 | PASS — DOMAIN-TERMS before ROOT (ROOT = TOKEN equivalent) | PASS or FAIL — same C-19 question as V-01 | PASS — 4-column table headers with ROOT VERDICT label enumerate all four | Does ROOT reframing produce deeper C-11 propagation without sacrificing C-18 compliance? |
| V-05 | PASS — DOMAIN-TERMS in GATE-0 before TOKEN in GATE-0; structural gate contract enforces ordering | PASS or FAIL — GATE-0 produces DOMAIN-TERMS then TOKEN; TOKEN precedes GATE-1's conditional logic; the question is whether DOMAIN-TERMS as GATE-0 line 1 violates "literal first output" | PASS — 4-column table headers in GATE-4 enumerate all four | Does GATE-0's two-output structure satisfy both C-18 (DOMAIN-TERMS before TOKEN) and C-19 (TOKEN before conditional logic in GATE-1+)? |

**The decisive R5 scoring question:** C-19 states "The TOKEN declaration is the literal first output." All five variations produce DOMAIN-TERMS before TOKEN — V-01, V-03, V-04, V-05 explicitly, V-02 not at all. If "literal first output" means the first line written overall, then V-01/V-03/V-04/V-05 all fail C-19 (DOMAIN-TERMS precedes TOKEN). If "literal first output" means the first output before conditional/procedural operations (with DOMAIN-TERMS classified as unconditional vocabulary extraction, not conditional logic), then DOMAIN-TERMS → TOKEN satisfies C-19 in V-01/V-03/V-04/V-05. V-02 satisfies C-19 under either interpretation but fails C-18 in all cases. V-05's GATE-0 framing makes the strongest structural argument for the permissive interpretation by naming GATE-0 as an unconditional pre-phase and naming GATE-1 as the first conditional gate.
