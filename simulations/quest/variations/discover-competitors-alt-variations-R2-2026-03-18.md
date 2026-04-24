Written to `simulations/quest/variations/discover-competitors-alt-variations-R2-2026-03-18.md`.

---

## R2 Variations — Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Inertia propagation (findings template slot) | Mandatory `vs INERTIA-REF:` slot in the findings template makes C-11 a format requirement — the model cannot drop the mechanism because the slot is unfilled |
| V-02 | AMEND stability column (single-axis) | Isolates the V-04-R1 AMEND column: does `INERTIA-REF stable?` alone produce reliable C-12 coverage without the full Phase/ROOT scaffolding? |
| V-03 | Conversational register (C-11+C-12 in plain English) | Fixes V-03-R1's C-11 failure by explicitly instructing: give the mechanism a label, use it in findings, and state stability per AMEND entry — all in natural language |
| V-04 | Propagation template + AMEND stability (direct combination) | Minimum overhead path to both new criteria: findings slot (C-11) + stability column (C-12), no full lifecycle required |
| V-05 | Role sequence + full propagation chain (consumption declarations) | Extends V-05-R1 with `consumes: INERTIA-REF` in every phase header — makes C-11 an architectural dependency and C-12 part of AMEND's declared output contract |

**Key design decisions for R2:**

- **Single-axis isolates the enforcement mechanism, not the criterion.** V-01 isolates the findings slot; V-02 isolates the AMEND column. Either could satisfy the criterion — the question is which vehicle is more reliable.
- **V-03 tests whether instructions can substitute for structure.** V-03-R1 failed C-11 because the mechanism had no label to re-reference. Adding "give it a short label" and "use that label in every finding" is the minimal fix — if it works, lighter prompts are viable.
- **V-04 is the pragmatic combination.** Two surgical additions to a clean baseline, targeting exactly the two R1 failure points.
- **V-05 is the architectural bet.** If consumption declarations make INERTIA-REF a live dependency rather than a past instruction, propagation becomes automatic — not something the model has to remember.
-R1's phase structure, adding consumption declarations per phase as the propagation mechanism — the hypothesis is that explicit "consumes: INERTIA-REF" labels in each phase header make C-11 an architectural property rather than an authorial callback.

**C-09 and C-10 carry-over:** All variations inherit the cross-dimensional gap instruction (C-09) and the no-free-floating-findings rule (C-10) from R1. These are stable and not the axis of variation in R2.

---

## V-01 -- Inertia Propagation (findings template slot)

**Axis:** Inertia propagation enforced via a mandatory three-part findings template. The template's third slot -- "vs INERTIA-REF" -- structurally requires the model to link each finding back to the mechanism named in C0. A finding that does not fill this slot fails the template.

**Hypothesis:** If the findings section has an explicit named slot for the INERTIA-REF connection, the model cannot abandon the mechanism after C0. C-11 becomes a format requirement ("fill the third slot") rather than an instruction the model may or may not follow.

---

You are running **discover-competitors-alt**.

Read the repo context (README, CLAUDE.md, package.json, or equivalent) to identify the topic. Do not ask the user for the topic, competitors, or market category. Proceed immediately.

**Focus detection:** Check `focus:` parameter before producing any output.
- `focus: market` -- Focus column is ACTIVE with market segment values.
- `focus: positioning` -- Focus column is ACTIVE with positioning claim values.
- Not set -- Focus column is INACTIVE; omit it.

---

### C0 -- Inertia Anchor

Before mapping any external competitor, characterize the status quo.

Write a named block:

```
C0: [Actual name of the status-quo behavior, tool, or workaround -- not "inertia" or "incumbent"]
Threat: HIGH (or justified lower rating)
INERTIA-REF: [mechanism type: switching cost | habit lock-in | workaround satisfaction]
  -> [Specific description tied to what C0 does or provides]
```

The phrase under `INERTIA-REF` is the named mechanism for this analysis. It will be referenced by that label in the competitive map, the gap finding, and the third slot of every finding in the Findings section.

If `focus:` is ACTIVE, add:
```
C0 Focus: [market segment C0 occupies] OR [positioning claim C0 holds implicitly]
```

---

### Competitive Map

Build the table. Row 0 is C0 (re-states the INERTIA-REF mechanism). Rows 1-N are named external competitors -- minimum 3. Every row receives an explicit HIGH / MEDIUM / LOW threat level. Generic category labels without a proper name do not count.

**If focus is INACTIVE:**

| Label | Name | Threat | Why | vs INERTIA-REF |
|-------|------|--------|-----|----------------|

**If focus is ACTIVE (market):**

| Label | Name | Threat | Why | Market segment | vs INERTIA-REF |
|-------|------|--------|-----|----------------|----------------|

**If focus is ACTIVE (positioning):**

| Label | Name | Threat | Why | Positioning claim | vs INERTIA-REF |
|-------|------|--------|-----|-------------------|----------------|

Column notes:
- **vs INERTIA-REF**: Does this competitor reinforce, challenge, or contextualize the C0 mechanism? For C0 row: `[ROOT]`.
- **Why**: One sentence naming a concrete behavior or capability. For at least one external row, include an inline citation (URL or publication name) from a WebSearch result -- in the cell, not a footnote.

---

### Whitespace Finding

Write a labeled finding:

**GAP:** [specific uncontested dimension not owned by C0 or any named competitor]

The gap must name the specific dimension -- not "there is room to innovate."

If focus is ACTIVE: the gap must be uncontested across BOTH the competitive dimension AND the focus dimension simultaneously. Show the intersection -- demonstrate that neither the competitive map alone nor the focus column alone would surface this gap.

---

### Findings

Write 3-5 findings. Each finding uses this three-part template:

> **[Competitor label or C0]** -- [specific claim about this competitor's behavior or capability] -- *vs INERTIA-REF: [how this finding relates to the mechanism named in the C0 block]*

The third slot is mandatory. A finding without the `vs INERTIA-REF` connection does not pass. Do not write general domain observations -- each finding must require the competitive map to support it.

---

### AMEND

List at least 2 adjustments. For each, name both the input change and the output effect:

| # | Input change | Output effect |
|---|-------------|---------------|
| 1 | Shift `focus:` from `market` to `positioning` | Focus column headers and values replaced in competitive map; whitespace finding recalculated on positioning axis |
| 2 | Add a named competitor | New row in competitive map; whitespace finding verified against expanded set; findings updated if gap closes |
| 3 | Adjust depth to `brief` | Findings condensed to 3 entries; AMEND section omitted |

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-02 -- AMEND Stability Column (single-axis)

**Axis:** AMEND section format -- adds an explicit `INERTIA-REF stable?` column to the AMEND table. This is the only structural addition compared to a minimal baseline; the rest of the prompt does not change the R1 pattern.

**Hypothesis:** The V-04-R1 AMEND stability column was the sole variation to satisfy C-12 in R1. The question is whether the column alone is sufficient -- without the full Phase/ROOT scaffolding -- to reliably produce stability reasoning. If yes, lighter-weight prompts can satisfy C-12 without requiring the full lifecycle structure.

---

You are running **discover-competitors-alt**.

Read the repo context (README, CLAUDE.md, package.json, or equivalent) to identify the topic. Do not ask the user for the topic, competitors, or market category. Proceed immediately.

**Focus detection:** Check `focus:` parameter.
- `focus: market` -- market segment column ACTIVE.
- `focus: positioning` -- positioning claim column ACTIVE.
- Not set -- focus column INACTIVE.

---

### C0 -- Inertia Anchor

Before mapping any market competitor, establish C0. Name the actual status-quo behavior or tool -- not "inertia" or "incumbent." Assign a threat level (almost always HIGH). Name the specific stickiness mechanism -- one of: switching cost, habit lock-in, workaround satisfaction -- tied to something C0 does or provides. This is the **inertia mechanism** for the analysis.

---

### Competitive Map

| Label | Name | Threat | Why | [Focus column if active] | Inertia delta |
|-------|------|--------|-----|--------------------------|---------------|

- Row 0: C0. Inertia delta: `[ROOT]`.
- Rows 1-N: minimum 3 named external competitors. No generic labels.
- Every row: explicit HIGH / MEDIUM / LOW threat.
- Focus column: populated for every row if active.
- Why cell: for at least one external row, include an inline WebSearch citation -- in the cell, not a footnote.
- Inertia delta: does this competitor reinforce, challenge, or contextualize the C0 stickiness mechanism?

---

### Whitespace Finding

**GAP:** [specific uncontested dimension not owned by C0 or any listed competitor]

Name the specific dimension. A generic statement does not pass.

If focus is active: the gap must be uncontested across both dimensions simultaneously. Demonstrate that combining the competitive map and the focus lens surfaces a gap neither alone would produce.

---

### Findings

3-5 findings. Each must reference at least one named competitor label from the competitive map (or C0). No finding may be free-floating prose that does not require the competitive analysis to support it.

---

### AMEND

| # | Input change | Output effect | INERTIA-REF stable? |
|---|-------------|---------------|---------------------|
| 1 | Shift `focus:` dimension | Focus column headers and values replaced; whitespace finding recalculated on new axis | Yes -- the C0 mechanism does not change when the focus lens rotates |
| 2 | Add a named competitor | New row in map; whitespace finding verified against expanded set | Yes -- unless the new competitor fundamentally reframes why users avoid switching |
| 3 | Deepen inertia analysis | C0 mechanism block expanded with second-order switching costs; findings re-anchored | No -- INERTIA-REF updates to reflect expanded mechanism |

Minimum 2 rows. The `INERTIA-REF stable?` column must be answered for every row -- Yes, No, or conditional with explanation. A silent entry does not satisfy C-12.

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-03 -- Phrasing Register (conversational, C-11+C-12 in plain English)

**Axis:** Phrasing register -- plain English with no formal notation, gate labels, or slot syntax. The two new criteria (C-11, C-12) are encoded as explicit natural language obligations: "use this mechanism name in your findings" and "for each amendment, say whether it would change the inertia anchor."

**Hypothesis:** The V-03-R1 register failed C-11 because no named handle was established. If the conversational prompt explicitly instructs the model to (a) give the mechanism a short label and (b) use that label in each finding, and (c) address stability in each AMEND entry, C-11 and C-12 can be satisfied without structural enforcement.

---

You are running **discover-competitors-alt**.

Start by reading the repo to figure out what topic you're analyzing -- look at the README, CLAUDE.md, or package.json. Don't ask the user what the topic is.

If `focus:` is set to `market` or `positioning`, that dimension gets woven into the competitor rows and the gap finding -- not added as a section at the end.

---

**First: nail the inertia competitor -- and give the mechanism a name.**

The most important competitor is C0 -- what users do today instead of using this feature. Name it specifically (the actual tool, habit, or workaround -- not "the status quo" or "incumbent"). Assign it a threat level (usually HIGH). Then explain *why* it's sticky: name one concrete mechanism -- what would users lose if they switched, what habit would be interrupted, or what workaround already solves most of the problem.

Give this mechanism a short label you'll use for the rest of the analysis -- something like "spreadsheet-habit" or "CLI-workflow-lock". Write it as:

> **Inertia mechanism (MECH): [your label] -- [specific description]**

Use this label in the competitor map and in every finding below. Don't drop it after this section.

Put C0 first. Always.

---

**Then: map the real competitors.**

Name at least 3 external competitors -- actual products or tools, not category labels. For each one:

- Say what their threat level is (HIGH / MEDIUM / LOW) -- be explicit.
- Say why they're a real alternative in one sentence.
- Say how they relate to the MECH you named -- do they reinforce why users stick with C0, challenge that stickiness, or add a new angle on it? Use the MECH label when you say this.
- If `focus: market` is set: add a note on what market segment this competitor owns.
- If `focus: positioning` is set: add a note on how this competitor positions themselves.

Look up at least one competitor with WebSearch. Put the citation right next to that competitor -- not in a footnote at the bottom.

---

**Then: find the whitespace.**

Name one specific gap that none of the listed competitors -- including C0 -- own. Label it clearly. Don't just say "there's room to innovate" -- say what the specific uncontested dimension is.

If `focus:` is active: the gap should only be visible when you combine the competitive map with the focus lens. A gap you could spot without the focus doesn't count. Show what the focus dimension adds.

---

**Then: write the findings.**

3-5 findings. For each one:

- Point back to a specific named competitor from the map (or C0).
- Reference the MECH label -- say how this finding connects to the inertia mechanism you named at the start. Don't drop the thread.
- Don't write general observations about the domain that could have been written without doing the competitive analysis.

---

**Finally: tell the user how to amend -- and whether the inertia anchor would change.**

Give at least 2 adjustments. For each one:

- Say what the user changes as input.
- Say what happens to the output as a result. "You can adjust the focus dimension" is not enough -- say what changes when they do.
- Say whether the amendment would change the MECH (the inertia anchor) or leave it stable. If the anchor would change, say why.

---

Write the artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-04 -- Propagation Template + AMEND Stability Column (direct combination)

**Axis:** Direct structural enforcement at both C-11 and C-12 failure points: (1) a three-part findings template with a mandatory INERTIA-REF slot (C-11), and (2) an explicit `INERTIA-REF stable?` AMEND column (C-12). Minimum overhead -- no full Phase/ROOT lifecycle, just the two enforcement structures added to a clean baseline.

**Hypothesis:** The strongest path to C-11 + C-12 is structural enforcement at exactly the two points where R1 variations failed. Template enforcement in findings prevents mechanism abandonment. The stability column in AMEND prevents silent anchor shifts. Together they close both gaps without requiring the full lifecycle scaffolding.

---

You are running **discover-competitors-alt**.

Read the repo context (README, CLAUDE.md, package.json, or equivalent) to identify the topic. Do not prompt the user. Resolve `focus:` state before producing any output.

**Focus state:**
- `focus: market` -- market segment column ACTIVE
- `focus: positioning` -- positioning claim column ACTIVE
- Not set -- focus column INACTIVE

---

### C0 -- Inertia Anchor

Before any table, characterize C0 as a named block:

```
C0: [Actual name of status-quo behavior or tool -- not "inertia" or "incumbent"]
Threat: HIGH (or justified lower)
INERTIA-REF: [switching cost | habit lock-in | workaround satisfaction]
  -> [Specific description tied to what C0 does or provides]
```

If `focus:` is ACTIVE:
```
C0 Focus: [market segment C0 occupies] OR [positioning claim C0 holds implicitly]
```

The `INERTIA-REF` block names the mechanism. It is referenced in the competitive map's `vs INERTIA-REF` column and in the third slot of every finding.

---

### Competitive Map

**If focus INACTIVE:**

| Label | Name | Threat | Why | vs INERTIA-REF | Source |
|-------|------|--------|-----|----------------|--------|

**If `focus: market`:**

| Label | Name | Threat | Why | Market segment | vs INERTIA-REF | Source |
|-------|------|--------|-----|----------------|----------------|--------|

**If `focus: positioning`:**

| Label | Name | Threat | Why | Positioning claim | vs INERTIA-REF | Source |
|-------|------|--------|-----|-------------------|----------------|--------|

Rules:
- Row 0: C0 re-states INERTIA-REF. `vs INERTIA-REF` = `[ROOT]`. Source = n/a.
- Rows 1-N: minimum 3 named external competitors. No generic category labels.
- Every row: explicit HIGH / MEDIUM / LOW threat.
- **vs INERTIA-REF**: How does this competitor's appeal relate to the C0 mechanism? Name the mechanism -- don't write a generic relationship label.
- **Source**: For at least one external row, inline WebSearch citation (URL or publication name) in this cell. Not a footnote.

---

### Whitespace Finding

**GAP:** [specific dimension not owned by C0 or any named competitor in the table]

The gap must name the specific dimension.

If focus ACTIVE: gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Show the intersection -- state what the focus lens adds that the competitive map alone would not surface.

---

### Findings

Write 3-5 findings. Each finding uses this template:

> **[Competitor label or C0]** -- [specific claim about this competitor's behavior or capability] -- *vs INERTIA-REF: [how this finding relates to the mechanism named in the C0 block]*

The third slot is mandatory. Do not write general domain observations. Each finding must require the competitive map to support it. The `vs INERTIA-REF` slot must reference the mechanism by its description -- not as a generic callback.

---

### AMEND

| # | Input change | Output effect | INERTIA-REF stable? |
|---|-------------|---------------|---------------------|
| 1 | Shift `focus:` from `market` to `positioning` | Focus column headers and values replaced throughout competitive map; GAP recalculated on positioning axis; findings referencing focus dimension re-evaluated | Yes -- the C0 mechanism does not depend on the focus lens |
| 2 | Add a named competitor | New row in table; GAP verified against expanded set; findings updated if gap closes | Yes -- unless the new competitor reframes the primary switching barrier |
| 3 | Deepen inertia analysis | C0 INERTIA-REF block expanded with second-order effects; all `vs INERTIA-REF` cells re-evaluated; findings re-anchored | No -- INERTIA-REF updates; downstream references must propagate |

Minimum 2 rows. `INERTIA-REF stable?` must be answered for every row -- Yes, No, or conditional. A silent entry does not pass C-12.

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-05 -- Role Sequence + Full Propagation Chain (consumption declarations)

**Axis:** Role sequence combined with explicit consumption declarations per phase. INERTIA-REF is resolved as a root-level dependency before Phase 1. Each subsequent phase declares which prior outputs it consumes -- including INERTIA-REF. The AMEND phase's output contract explicitly includes stability assessment. Propagation is architectural, not instructional.

**Hypothesis:** When each phase header declares "consumes: INERTIA-REF," the model treats the mechanism as a live dependency throughout execution -- not as an early-section detail that fades. C-11 becomes a consequence of the dependency declaration (Phase 3 and Phase 4 must consume INERTIA-REF to fulfill their output contracts). C-12 becomes the AMEND phase's declared output contract: stability assessment is what AMEND produces, not an optional addition.

---

You are running **discover-competitors-alt**.

**Auto-detect:** Read repo context (README, CLAUDE.md, package.json, or equivalent). Identify topic, market domain, and plausible competitor categories. Do not prompt the user. Proceed immediately.

**Focus resolution (pre-execution):** Resolve `focus:` state now and write it as a declaration before any output:

```
Focus state: [ACTIVE: market | ACTIVE: positioning | INACTIVE]
```

- ACTIVE -- Focus column included in Phase 2 table; Phase 3 gap requires cross-dimensional proof.
- INACTIVE -- Focus column omitted; Phase 3 gap requires competitive proof only.

---

### ROOT -- INERTIA-REF

**Produces:** `INERTIA-REF` -- consumed by Phase 2, Phase 3, Phase 4, AMEND.

**Executes before Phase 1.**

Name the status-quo behavior or tool (C0). Assign threat level. Name the stickiness mechanism -- one of: switching cost, habit lock-in, workaround satisfaction -- tied to a specific behavior or capability C0 does or provides.

Write:

```
INERTIA-REF: [C0 name] -- [mechanism type]: [specific description]
Threat: [HIGH / MEDIUM / LOW]
```

If focus is ACTIVE:
```
INERTIA-REF Focus: [market segment C0 occupies] OR [positioning claim C0 holds]
```

ROOT complete when: C0 named specifically, mechanism type declared, specific description provided.

---

### Phase 1 -- Topic & Scope

**Consumes:** repo context.
**Produces:** topic declaration -- consumed by Phase 2 (competitor identification boundary).

Write:
- Market domain
- Primary user persona
- Decision context: what is the user choosing between?

---

### Phase 2 -- Competitive Map

**Consumes:** Phase 1 topic declaration, ROOT INERTIA-REF, focus state.
**Produces:** competitor table -- consumed by Phase 3 (gap candidates), Phase 4 (findings anchors), AMEND (scope of entries).

Table schema:

**If focus INACTIVE:**

| Label | Name | Threat | Why | vs INERTIA-REF | Source |
|-------|------|--------|-----|----------------|--------|

**If focus ACTIVE (market):**

| Label | Name | Threat | Why | Market segment | vs INERTIA-REF | Source |
|-------|------|--------|-----|----------------|----------------|--------|

**If focus ACTIVE (positioning):**

| Label | Name | Threat | Why | Positioning claim | vs INERTIA-REF | Source |
|-------|------|--------|-----|-------------------|----------------|--------|

Constraints:
- Row 0: C0 re-states ROOT INERTIA-REF. `vs INERTIA-REF` = `[ROOT]`.
- Rows 1-N: minimum 3 named external competitors. No generic labels.
- Every row: explicit HIGH / MEDIUM / LOW threat.
- **vs INERTIA-REF**: How does this competitor's appeal interact with the mechanism described in ROOT? Reference the mechanism description -- not a generic label.
- Focus column: populated for every row if focus ACTIVE.
- Source: for at least one external row, inline WebSearch citation in this cell. Not a footnote.

Phase 2 complete when: C0 at row 0, >= 3 external rows, every row has threat level, citation present, every `vs INERTIA-REF` cell references ROOT mechanism.

---

### Phase 3 -- Whitespace

**Consumes:** Phase 2 competitor table, ROOT INERTIA-REF (for gap rationale), focus state.
**Produces:** labeled GAP finding -- consumed by Phase 4 (findings set).

Write:

**GAP:** [specific dimension not owned by C0 or any Phase 2 competitor]

If focus INACTIVE: gap is uncontested across the competitive map. State why ROOT INERTIA-REF does not cover this gap.

If focus ACTIVE: gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Show intersection -- name what the focus lens adds that the competitive map alone would not surface. Confirm that ROOT INERTIA-REF does not cover this gap either.

---

### Phase 4 -- Findings

**Consumes:** Phase 2 competitor table, Phase 3 GAP, ROOT INERTIA-REF.
**Produces:** findings -- consumed by output artifact.

Write 3-5 findings. Each finding uses this template:

> **[Competitor label or C0 from Phase 2]** -- [specific claim] -- *INERTIA-REF: [connection to the ROOT mechanism]*

Rules:
- Third slot is mandatory -- the finding must name how it relates to the ROOT mechanism.
- Findings that could be written without having run Phase 2 fail the grounding test.
- Findings that do not fill the INERTIA-REF slot fail the propagation test.

---

### AMEND

**Consumes:** all phases.
**Produces:** amendment table with input-to-output pairs and stability declarations.

Output contract: for every row, name (1) the input change, (2) the output effect across affected phases, and (3) whether the amendment would alter INERTIA-REF or leave it stable.

| # | Input change | Output effect | INERTIA-REF stable? |
|---|-------------|---------------|---------------------|
| 1 | Shift `focus:` dimension | Phase 2 focus column headers and values replaced; Phase 3 GAP recalculated on new axis; Phase 4 findings referencing focus re-evaluated | Yes -- ROOT mechanism is independent of focus lens |
| 2 | Adjust depth to `brief` | Phase 4 condensed to 3 findings; AMEND omitted | Yes |
| 3 | Narrow competitor set to a specific tier or domain | Phase 1 scope boundary updates; Phase 2 repopulated within narrowed scope; Phase 3 GAP rechecked against contracted set | Yes -- unless narrowing reframes what C0 competes against |
| 4 | Deepen inertia analysis | ROOT block expanded with second-order effects; Phase 2 `vs INERTIA-REF` column re-evaluated; Phase 4 findings re-anchored | No -- INERTIA-REF updates; all consuming phases must propagate |

Minimum 2 rows. `INERTIA-REF stable?` required for every row. A silent cell does not satisfy the AMEND output contract.

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.
