Here are the 5 variations for `discover-competitors-alt` Round 6:

---

## Summary

**Baseline:** R5 V-05 scored 100. R6 adds C-21 and C-22, which V-05 R5 already implicitly satisfied. The variations confirm and probe those patterns.

| Variation | Axis | Key architectural choice |
|-----------|------|--------------------------|
| **V-01** | Lifecycle | Direct V-05 R5 clone — GATE-0 header states both C-21 conditions in one sentence; domain-neutral AMEND columns |
| **V-02** | Role sequence | Pre-execution phase manifest table pre-declares all gates before GATE-0 executes; gate bodies are compact |
| **V-03** | Phrasing register | Conversational steps replace gates; both C-21 conditions stated in prose; tests whether prose = architectural declaration |
| **V-04** | Inertia framing | V-01 architecture + TOKEN required by name in every section (column header, every finding line, whitespace field, AMEND verdict) |
| **V-05** | Combined | Manifest + gates + TOKEN propagation + explicit schema declaration block before AMEND table |

**The decisive R6 question:** C-21 requires the boundary to be "architecturally declared." V-01/V-04/V-05 declare it via gate headers. V-02 declares it via manifest only. V-03 declares it via prose. The scorecard will determine whether gate-header markers are required or whether manifest/prose declarations are structurally equivalent.

**Predicted winner:** V-01, V-02, V-04, V-05 at 100. V-03 at risk for C-21 PARTIAL — ~99.286 if prose-based C-21 conditions don't satisfy "architecturally declared."
nal status before GATE-0 executes; individual gate sections are compact | C-21 satisfied at manifest level before any gate opens; does manifest-level declaration count as "architecturally declared" per C-21 or is it redundant prose? |
| **V-03** | Phrasing register | Conversational imperative throughout; GATE labels replaced with Step labels; both C-21 conditions stated in direct prose | Tests whether conversational "Step 1 is unconditional; Step 2 is where conditional logic begins" satisfies C-21's "architecturally declared" requirement or yields PARTIAL |
| **V-04** | Inertia framing | GATE-0/GATE-1 architecture from V-01; TOKEN propagation explicitly required in every gate — `vs [TOKEN]` column header, TOKEN by name in every finding line, TOKEN in whitespace note, TOKEN named in AMEND verdict column description | TOKEN propagation maximization deepens C-11; tests whether explicit per-gate TOKEN requirements produce richer or formulaic downstream analysis |
| **V-05** | Combined | Phase manifest (V-02) + GATE-0/GATE-1 architecture (V-01) + TOKEN propagation requirements (V-04) + AMEND schema with explicit rubric-standard component names | Strongest C-21 signal (manifest + gate headers); maximum C-11 propagation; AMEND schema names explicitly matched to rubric-standard terminology |

**Structural choices by variation:**

- **V-01:** GATE-0 header reads "unconditional — GATE-1 is the first conditional operation." Completion condition per gate. 4-column AMEND with `Input change | Output effect | Stability verdict | Evidence`.
- **V-02:** Phase manifest table at the top: `GATE-0 = UNCONDITIONAL | GATE-1 = CONDITIONAL (first)` before any gate body executes. Gate bodies are compact; C-21 relies primarily on manifest rather than gate-header labeling.
- **V-03:** Steps, not gates. "Step 1 is unconditional. Step 2 is the first conditional step." Numbered AMEND with bold domain-neutral component labels. No architectural gate headers.
- **V-04:** GATE-0/GATE-1 from V-01. Every gate section adds a TOKEN-reference requirement: `vs [TOKEN]` column header mandatory, TOKEN by name in every finding line, whitespace has a `[TOKEN] exposure:` field, AMEND verdict column description explicitly names TOKEN.
- **V-05:** Phase manifest as outer wrapper + GATE bodies inside + TOKEN-reference requirements in every gate + AMEND schema that quotes all four rubric-standard component names plus column headers.

---

## V-01 — Lifecycle emphasis: direct V-05 R5 evolution

**Axis:** Lifecycle emphasis — gated phases with completion conditions, GATE-0 explicitly declares both C-21 conditions in its header, domain-neutral AMEND schema.
**Hypothesis:** V-05 R5's architecture already satisfies C-21 (GATE-0 unconditional + GATE-1 named as first conditional) and C-22 (domain-neutral schema). Replicating it cleanly under R6 should score 100. Both C-21 conditions appear in the same GATE-0 header sentence, leaving no ambiguity.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if one was provided. Execute each gate in sequence. Do not begin a gate until the previous gate's completion condition is satisfied.

---

### GATE-0 [unconditional — GATE-1 is the first conditional operation]

This gate is unconditional — no focus detection, no auto-detect, no section headers, no branching of any kind. GATE-1 is the first gate where conditional logic executes. GATE-0 must complete before GATE-1 opens.

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
vs [TOKEN]: [how this finding relates to the TOKEN mechanism declared in GATE-2]
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

## V-02 — Role sequence: pre-execution phase manifest

**Axis:** Role sequence — a phase manifest table pre-declares all gates and their conditional status before any gate body executes. C-21 is satisfied at the manifest declaration level, before GATE-0 begins output.
**Hypothesis:** Pre-declaring `GATE-0 = UNCONDITIONAL | GATE-1 = CONDITIONAL (first)` in a manifest before execution establishes the C-21 boundary at the schema level. The individual gate bodies are more compact. The secondary question: does manifest-level C-21 declaration satisfy the criterion when gate-body headers are less explicit about the unconditional/conditional distinction?

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. The execution structure is declared below. Work through each gate in order.

---

### Phase manifest

| Gate | Condition type | Operations | Conditional successor |
|---|---|---|---|
| GATE-0 | **UNCONDITIONAL** | Domain vocabulary extraction → TOKEN declaration | GATE-1 |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference | GATE-2 |
| GATE-2 | CONDITIONAL | C0 description, competitive map | GATE-3 |
| GATE-3 | CONDITIONAL | Findings, whitespace | GATE-4 |
| GATE-4 | CONDITIONAL | AMEND table | — |

GATE-0 is the only unconditional gate. GATE-1 is the first gate where conditional logic executes. No conditional operation begins before GATE-0 is complete.

---

### GATE-0

Write exactly these two output lines — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — must include at least one term from DOMAIN-TERMS]
```

Read the repo context (README, CLAUDE.md, package.json, or equivalent) first. DOMAIN-TERMS: extract 2–3 product-domain terms and close the line before writing TOKEN. TOKEN: must include at least one DOMAIN-TERMS term. Generic placeholder alone (MECH, LOCK) fails. Copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-ANCHOR) passes. TOKEN is declared here before any competitive content or conditional logic.

**Completion condition:** DOMAIN-TERMS closed. TOKEN closed. Both lines before any other output.

---

### GATE-1

```
FOCUS: ACTIVE — [dimension] | INACTIVE
TOPIC: [inferred product domain]
MARKET: [inferred market category]
```

Read repo context. Do not ask the user for topic, competitors, or market category.

**Completion condition:** FOCUS, TOPIC, MARKET written.

---

### GATE-2

**C0 — before any competitor row:**

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [product-specific description — what C0 does or provides that creates this mechanism]
```

Run a WebSearch to verify at least one competitor. C0 is row 0.

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |

Minimum 3 named competitors with explicit threat levels. At least one inline WebSearch citation in Source cell — not a footnote.

**Completion condition:** C0 section before competitor rows. Table: row 0 = C0, at least 3 external rows, at least 1 inline citation.

---

### GATE-3

**Findings (3) — each references a named competitor row:**

```
**Finding [N]: [Title]**
[Observation — name the competitor row label]
vs [TOKEN]: [how this finding connects to the TOKEN mechanism]
```

TOKEN must appear by name in at least one `vs [TOKEN]` line. Findings that could be written without GATE-2 fail.

**Whitespace:** Name one uncontested gap no competitor owns. State the specific dimension.

If FOCUS is ACTIVE: gap must be uncontested across competitive + focus dimensions. Show the intersection — what does the focus lens reveal that the competitive map alone would not?

**Completion condition:** 3 grounded findings with competitor references. Labeled whitespace finding with specific dimension.

---

### GATE-4

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts] | [which gate or section shifts — be specific] | STABLE / UNSTABLE — [verdict on whether TOKEN is affected] | [reasoning for verdict — not a restatement] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict] | [reasoning] |

Minimum 3 rows. Every cell filled. Evidence must contain reasoning — "Stable." alone fails.

**Completion condition:** At least 3 data rows. Every row: all four cells with verdict and reasoning.

---

## V-03 — Phrasing register: conversational imperative with explicit C-21 conditions

**Axis:** Phrasing register — direct imperative conversational voice throughout. Steps replace gates. Both C-21 conditions stated in prose: the unconditional nature of Step 1 and Step 2 as the first conditional step. Domain-neutral AMEND component names preserved.
**Hypothesis:** Conversational register can satisfy C-21 if both conditions appear explicitly in prose — "Step 1 is unconditional; Step 2 is the first conditional step." The risk: absence of architectural gate headers means the boundary is described rather than declared. R5 V-03 failed C-19 by asserting DOMAIN-TERMS was "your first line" — this variation avoids that failure mode while testing whether prose-based C-21 conditions are sufficient.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project. If a focus dimension was provided, weave it in — don't append it as a separate section. Work through each step in order.

---

**Step 1 — Extract domain vocabulary and declare the token.**

This step is unconditional. Step 2 is the first step where conditional logic runs. No detection, no branching, no headers appear before or during this step.

Before any other output, read the repo context — README, CLAUDE.md, package.json, or whatever is available. Identify 2–3 terms that are specific to this product's domain: terms a domain expert would use, not generic software words. Output the vocabulary commitment as a closed artifact:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
```

Write it and close it. Now construct the token: pick an identifier that includes at least one term from the DOMAIN-TERMS line you just wrote. That's how the token becomes domain-specific.

```
TOKEN: [domain-adaptive identifier]
```

DOMAIN-TERMS then TOKEN — both unconditional, nothing between them. Do not ask the user for topic or context before completing this step.

---

**Step 2 — Resolve the focus dimension and infer the topic. First conditional step.**

Check whether a focus dimension was provided. Write one of:
- `FOCUS: ACTIVE — [the dimension provided]`
- `FOCUS: INACTIVE`

Read the repo context and write:
- `TOPIC: [inferred product domain]`
- `MARKET: [inferred market category]`

Do not prompt the user for any of these.

---

**Step 3 — Describe the current solution (C0) before naming any competitor.**

Open a C0 section. Use TOKEN by name to label the inertia mechanism:

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [specific description tied to what C0 does or provides]
```

The mechanism must tie to a real behavior or feature of C0. A category label applied generically ("inertia is high") does not satisfy this step.

---

**Step 4 — Build the competitive map.**

C0 goes in row 0. Run a WebSearch to verify at least one competitor claim.

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [comparison to TOKEN mechanism] | — |

Name at least 3 external competitors — no generic buckets. Every row gets an explicit threat level. Put the WebSearch citation inline in the Source cell for at least one row — not in a footnote.

---

**Step 5 — Write 3 findings.**

Each finding must reference at least one named competitor row by label. Include a `vs [TOKEN]` line in each:

```
**Finding [N]: [Title]**
[Observation — name the competitor row]
vs [TOKEN]: [how this finding connects to the inertia mechanism]
```

A finding that could be written without the competitive map doesn't count.

---

**Step 6 — Identify the whitespace.**

Name one uncontested gap no competitor on the map owns. Give it a specific label — a generic "room to innovate" statement doesn't pass.

If FOCUS is ACTIVE: the gap must be uncontested across both the competitive dimension and the focus dimension at the same time. Show what the focus lens reveals that the competitive map alone couldn't surface.

---

**Step 7 — Write the AMEND section.**

List at least 3 amendments. Every amendment requires exactly four named components — all four must appear explicitly:

1. **Input change:** what the user would adjust
2. **Output effect:** which step or section shifts as a result — be specific
3. **Stability verdict:** STABLE or UNSTABLE — whether TOKEN is affected by this change
4. **Evidence:** reasoning that supports the stability verdict — not a restatement of the verdict

Write each amendment in this form:

```
**Amendment [N]**
1. Input change: [description]
2. Output effect: [description]
3. Stability verdict: STABLE | UNSTABLE — [one sentence]
4. Evidence: [reasoning]
```

"Stable." alone in the evidence slot doesn't pass. Every amendment needs all four pieces.

---

## V-04 — Inertia framing: GATE architecture with TOKEN propagation maximized

**Axis:** Inertia framing — GATE-0/GATE-1 architecture identical to V-01, but TOKEN propagation is explicitly required in every gate section: `vs [TOKEN]` column header uses TOKEN by name, every finding line must include TOKEN by declared value, the whitespace finding has a required `[TOKEN] exposure:` field, and the AMEND verdict column description explicitly names TOKEN.
**Hypothesis:** Mandating TOKEN references by name in every gate's output — not just C0 and optional finding lines — makes C-11 propagation structural rather than incidental. The risk: explicit per-gate TOKEN requirements may produce formulaic rather than analytical downstream usage, where TOKEN appears mechanically rather than meaningfully.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project, weaving in the focus dimension if provided. The inertia mechanism token declared in GATE-0 threads through every gate — it is the structural reference for competitive analysis throughout.

Execute each gate in sequence. Do not begin a gate until the previous gate's completion condition is satisfied.

---

### GATE-0 [unconditional — GATE-1 is the first conditional operation]

This gate is unconditional. No focus detection, no auto-detect, no section headers, no conditional branching before or during it. GATE-1 is the first gate with conditional logic.

Write exactly these two lines as your opening output — nothing before them, nothing between them:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — must include at least one term from DOMAIN-TERMS above]
```

Read the repo context (README, CLAUDE.md, package.json, or equivalent) before writing. DOMAIN-TERMS: 2–3 product-domain terms, closed before TOKEN. TOKEN: at least one DOMAIN-TERMS term embedded; generic placeholder alone (MECH, LOCK) fails; a copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-LOCK, PLUGIN-ANCHOR) passes.

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

### GATE-2 [C0 and competitive map — TOKEN anchors the map]

**C0 — before any competitor row:**

```
## C0 — [product name]
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction] → [Specific description tied to a real C0 behavior or feature — not a generic category label]
```

Run a WebSearch to verify at least one competitor claim.

**Competitive map — `vs [TOKEN]` column uses TOKEN by name:**

| Competitor | Threat | Differentiator | vs [TOKEN] | Source |
|---|---|---|---|---|
| C0 — [product name] | — | [key capability] | ROOT | — |
| [Competitor 1] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | [inline WebSearch citation] |
| [Competitor 2] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | — |
| [Competitor 3] | HIGH / MEDIUM / LOW | [differentiator] | [how this competitor erodes or bypasses TOKEN mechanism] | — |

- Minimum 3 named external competitors with explicit threat levels.
- At least one inline WebSearch citation in Source cell — not a footnote.
- `vs [TOKEN]` column descriptions must address how each competitor affects the TOKEN mechanism specifically.

**GATE-2 completion condition:** C0 section before competitor rows. Table: row 0 = C0, at least 3 external rows, at least 1 inline citation, `vs [TOKEN]` column header uses TOKEN by name.

---

### GATE-3 [findings and whitespace — TOKEN by name in every finding and whitespace]

**Findings — 3 required:**

Each finding must: (1) reference at least one named competitor row by table label, and (2) include a `vs [TOKEN]` line where TOKEN appears by its declared value — not by role description ("the inertia mechanism" without naming TOKEN fails).

```
**Finding [N]: [Title]**
[Observation — reference named competitor row by label]
vs [TOKEN]: [how this finding relates to the TOKEN mechanism — TOKEN must appear verbatim here]
```

Findings that could be written without GATE-2 fail. A `vs [TOKEN]` line that describes the mechanism without naming TOKEN by value fails C-11.

**Whitespace finding:**

Name one uncontested gap no listed competitor owns. Include a TOKEN exposure field:

```
WHITESPACE: [specific uncontested dimension — not a generic statement]
[TOKEN] exposure: [whether TOKEN's mechanism reinforces, defines, or is irrelevant to this gap — TOKEN must appear by name]
```

If FOCUS is ACTIVE: gap must be uncontested across competitive + focus dimensions simultaneously. Show the intersection and include TOKEN in the intersection rationale.

**GATE-3 completion condition:** 3 findings with named competitor references and `vs [TOKEN]` lines using TOKEN by declared value. Labeled whitespace finding with TOKEN exposure field.

---

### GATE-4 [AMEND — TOKEN named in stability verdict column description]

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts — focus dimension, depth level, competitor scope] | [which gate or section specifically shifts] | STABLE / UNSTABLE — [one-sentence verdict on whether [TOKEN] is affected by this change] | [reasoning that supports the verdict — must be distinct from the verdict itself] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |

- Minimum 3 rows. Every cell filled.
- Stability verdict: TOKEN must be referenced by its declared value in the verdict sentence or the immediately adjacent Evidence cell.
- Evidence: reasoning distinct from verdict. "Stable." alone fails.

**GATE-4 completion condition:** At least 3 data rows. Every row fills all four cells with verdict and evidence.

---

## V-05 — Combined: phase manifest + GATE architecture + TOKEN propagation + domain-neutral schema

**Axis:** Combined — phase manifest pre-declaration (V-02), GATE-0/GATE-1 architecture (V-01/V-04), TOKEN propagation required in every gate (V-04), and AMEND schema with the most explicit possible domain-neutral four-component enumeration including a schema declaration block.
**Hypothesis:** Double C-21 declaration (manifest + gate header) produces the strongest possible architectural signal. Maximum TOKEN propagation deepens C-11 without compromising C-19/C-21 compliance. Explicit schema declaration block before the AMEND table (naming all four rubric-standard component names) eliminates any ambiguity in C-20/C-22 compliance.

---

You are running `discover-competitors-alt`. Produce a unified competitive analysis for the current project. If a focus dimension was provided, weave it throughout — do not append it as a separate section. Execute each gate in sequence.

---

### Phase manifest

| Gate | Condition type | Primary operations | Notes |
|---|---|---|---|
| GATE-0 | **UNCONDITIONAL** | DOMAIN-TERMS extraction → TOKEN declaration | Executes first, always; GATE-1 is the first conditional successor |
| GATE-1 | CONDITIONAL (first) | Focus detection, topic inference | No conditional logic precedes GATE-1 |
| GATE-2 | CONDITIONAL | C0 description, competitive map | C0 written before any competitor row |
| GATE-3 | CONDITIONAL | Findings (TOKEN-grounded), whitespace | TOKEN by name in every finding and whitespace field |
| GATE-4 | CONDITIONAL | AMEND table | Domain-neutral schema: Input change, Output effect, Stability verdict, Evidence |

GATE-0 is unconditional. GATE-1 is the first gate where conditional operations execute. No conditional logic precedes GATE-0's completion.

---

### GATE-0 [unconditional — GATE-1 is the first conditional operation]

This gate is unconditional — no focus detection, no auto-detect, no section headers, no conditional branching. GATE-1 is the first gate with conditional logic. This gate produces exactly two outputs: DOMAIN-TERMS then TOKEN. Nothing precedes DOMAIN-TERMS. Nothing appears between DOMAIN-TERMS and TOKEN.

Write exactly these two lines as your opening output:

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
TOKEN: [domain-adaptive identifier — must include at least one term from DOMAIN-TERMS above]
```

Read the repo context (README, CLAUDE.md, package.json, or equivalent) before writing. DOMAIN-TERMS: 2–3 product-domain terms — terms a domain expert would use, not generic software terms. Write and close before TOKEN. TOKEN: must include at least one DOMAIN-TERMS term. Generic placeholder alone (MECH, LOCK, INERTIA-REF) fails. A copyable domain-specific identifier (SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK) passes.

TOKEN is declared here before all competitive content, before all conditional logic, before all section structure. It appears by name in every subsequent gate.

**GATE-0 completion condition:** DOMAIN-TERMS written and closed. TOKEN written and closed. Both lines before any other output. No other content in this gate.

---

### GATE-1 [first conditional — focus detection and topic resolution]

```
FOCUS: ACTIVE — [dimension] | INACTIVE
TOPIC: [inferred product domain]
MARKET: [inferred market category]
```

Read repo context. Do not ask the user for topic, competitor names, or market category.

**GATE-1 completion condition:** FOCUS, TOPIC, MARKET written.

---

### GATE-2 [C0 and competitive map]

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

### GATE-3 [findings and whitespace — TOKEN by name in every output]

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

### GATE-4 [AMEND]

**AMEND entry schema — all four required components enumerated by their domain-neutral rubric-standard names:**

| Component | Rubric-standard name | Description |
|---|---|---|
| 1 | **Input change** | The adjustment the user makes — focus dimension, depth level, competitor scope |
| 2 | **Output effect** | The specific change in output that results — name the gate or section |
| 3 | **Stability verdict** | Whether TOKEN is affected — STABLE / UNSTABLE verdict required |
| 4 | **Evidence** | Reasoning that supports the stability verdict, distinct from the verdict itself |

**AMEND table — one row per amendment, minimum 3:**

| # | Input change | Output effect | Stability verdict | Evidence |
|---|---|---|---|---|
| 1 | [what the user adjusts] | [which gate or section specifically shifts — name it] | STABLE / UNSTABLE — [one-sentence verdict on whether [TOKEN] is affected] | [reasoning that supports the verdict — logically distinct from the verdict statement] |
| 2 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |
| 3 | [input change] | [output effect] | STABLE / UNSTABLE — [verdict on [TOKEN]] | [reasoning] |

Minimum 3 rows. Every cell must be filled. Evidence column must contain reasoning — "Stable." alone fails. Every Stability verdict cell must contain a verdict.

**GATE-4 completion condition:** Table has at least 3 data rows. Every row: all four cells with verdict and evidence.

---

## Composite hypothesis table

| Variation | C-21 prediction | C-22 prediction | Critical question |
|-----------|----------------|----------------|-------------------|
| V-01 | PASS — GATE-0 header states (1) unconditional AND (2) "GATE-1 is the first conditional operation" in one sentence | PASS — column headers: `Input change \| Output effect \| Stability verdict \| Evidence` — all domain-neutral rubric-standard | Does V-05 R5's architecture hold at 100 under R6? |
| V-02 | PASS — manifest pre-declares GATE-0 = UNCONDITIONAL and GATE-1 = CONDITIONAL (first) before any gate body executes | PASS — same domain-neutral column headers as V-01 | Does manifest-level C-21 declaration satisfy the criterion when gate-body headers don't repeat the unconditional/conditional language? Or does C-21 require gate-body labeling as well? |
| V-03 | PASS or PARTIAL — "Step 1 is unconditional; Step 2 is the first conditional step" in prose; no architectural gate-header markers | PASS — numbered AMEND with domain-neutral bold component labels (Input change, Output effect, Stability verdict, Evidence) | Is prose-stated C-21 compliance "architecturally declared" or merely described? Does absence of gate-header structural markers yield PARTIAL? |
| V-04 | PASS — same GATE-0 headers as V-01; both C-21 conditions identical | PASS — `Stability verdict` column header is domain-neutral; TOKEN named in verdict cell description but not as column label | Does mandating TOKEN by name in every gate section produce richer C-11 propagation or formulaic downstream output? |
| V-05 | PASS — double-declared: manifest pre-declares GATE-0 unconditional + GATE-1 conditional first, then GATE-0 header repeats both conditions | PASS — schema declaration block explicitly names all four components with rubric-standard labels; column headers also domain-neutral | Does double C-21 declaration (manifest + gate header) produce any scoring benefit, or is single declaration sufficient? Does explicit schema declaration block before AMEND table strengthen C-20/C-22? |

**The R6 decisive question:** V-05 R5 already satisfies C-21 and C-22. The R6 scorecard will reveal whether:
1. All five variations achieve 100 (since V-05 R5's architecture is the baseline)
2. V-03's prose-based C-21 conditions yield PARTIAL (the conversational register risk)
3. V-02's manifest-level C-21 declaration satisfies the criterion without gate-body repetition
4. V-04's TOKEN propagation requirements produce measurably richer or formulaic C-11 analysis
5. V-05's double C-21 declaration + schema declaration block produces any additional scoring advantage

**Predicted winner:** V-01, V-02, V-04, V-05 at 100. V-03 at risk for C-21 PARTIAL — predicted ~99.286 (13.5/14 aspirational) if the prose C-21 argument yields PARTIAL due to absence of architectural gate-header markers.
