Written to `simulations/quest/variations/discover-competitors-alt-variations-R1-2026-03-18.md`.

---

## R1 Variations — Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Inertia framing | C0 as analytical anchor before any market competitor; mechanism phrase established first and referenced throughout |
| V-02 | Output format | Table schema defined upfront with conditional Focus column; weaving becomes structural (a column cannot be appended) |
| V-03 | Phrasing register | Conversational imperative — no gate labels, no slot notation; plain English covering all 10 criteria |
| V-04 | Inertia framing + Output format | C0-anchored table with `vs INERTIA-REF` column per row; combination targets C-09 (cross-dimensional gap) |
| V-05 | Lifecycle emphasis + Inertia framing | Named phases with output contracts + ROOT-level inertia resolution; ordering and weaving become structural execution properties |

---

**Key design decisions:**

**Single-axis choices:** V-01 isolates how prominently C0 is foregrounded (narrative anchor vs. first row in a list). V-02 isolates whether the output format structurally prevents appending (column = present/absent, not a section bolted on). V-03 isolates register — does ceremony help or hurt?

**Combination logic:** V-04 combines the two axes most likely to interact: table structure enforces column presence (C-03) while the INERTIA-REF column enforces C-06 and C-10 simultaneously. V-05 adds lifecycle phase boundaries to V-01's inertia emphasis — the hypothesis is that ROOT-before-Phase-1 ordering makes C-01 (inertia first) an execution dependency rather than an instruction.

**C-09 targeting:** V-02 and V-04 both make the claim explicit in the gap-finding instructions: "the gap must require both the competitive map and the focus lens to produce." V-05 goes further by making the active/inactive branch a pre-execution declaration, so the model knows at Phase 3 whether it needs to prove intersection.
us:` is set to `market` or `positioning`, weave that dimension into the analysis — do not isolate it in a trailing section.

---

### Step 1 — Establish the Inertia Anchor (C0)

Before naming any market competitor, characterize what users do today instead of adopting this feature. This is C0 — the status quo — and it is the most dangerous competitor because it requires no decision.

Write C0 as a named entry (use the actual behavior or tool: "manual spreadsheet tracking," "existing CLI workflow," "copy-paste from browser," etc. — not the label "inertia" or "incumbent"). Assign a threat level: almost always HIGH. Then name the specific stickiness mechanism — one of:

- **Switching cost:** what the user would lose or have to rebuild
- **Habit lock-in:** a practiced behavior the feature would interrupt
- **Workaround satisfaction:** a workaround that already solves 80% of the need

This mechanism phrase becomes the inertia reference for the rest of the analysis. Every other competitor and every finding will be evaluated against it.

If `focus:` is active, add a Focus column to C0's entry and populate it now.

---

### Step 2 — Competitive Map

List at least 3 named external competitors. For each:

- **Name:** A proper name (product, tool, approach). No generic labels.
- **Threat level:** HIGH / MEDIUM / LOW — explicit, not implied.
- **Why they threaten:** One sentence, mechanism-level. What behavior or capability makes them a realistic alternative?
- **Inertia delta:** Does this competitor reinforce, challenge, or contextualize the C0 stickiness mechanism? Name which.
- **Focus column** (if `focus:` active): For `market` — estimated addressable segment this competitor owns. For `positioning` — the primary positioning claim this competitor holds.

Run a WebSearch on at least one named competitor. Add an inline citation (URL or publication name) within that competitor's entry — not in a trailing footnote.

---

### Step 3 — Whitespace

Name one uncontested gap that no listed competitor — including C0 — owns. State it as a labeled finding:

**GAP:** [specific uncontested dimension]

A generic statement ("there is room to innovate") does not pass. Name the dimension.

If `focus:` is active: the gap must be uncontested across both the competitive dimension AND the focus dimension simultaneously. A gap that is obvious without the focus lens does not qualify — show that combining the competitive map with the focus lens produces a finding neither alone would surface.

---

### Step 4 — Findings

Write 3–5 findings. Each finding must:

1. Reference at least one named competitor by its row label (e.g., "C0," "GitHub Copilot," the name used in Step 2).
2. State a specific attribute or behavior — not general domain knowledge.

Free-floating findings that do not require the competitive analysis to support them do not pass.

---

### AMEND

List at least 2 adjustments the user can make. For each, name both the input change and what changes in the output:

| # | Input change | Output effect |
|---|-------------|---------------|
| 1 | Shift focus from `market` to `positioning` | Focus column in Step 2 switches from segment estimates to positioning claims; Step 3 gap recalculates across positioning axis |
| 2 | Add a competitor name | New row added to Step 2 table; Step 3 gap rechecked against expanded set; findings updated if gap is closed |
| 3 | Adjust depth to `brief` | Findings condensed to 3 bullets; AMEND section omitted |

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-02 — Output Format (table-first with conditional Focus column)

**Axis:** Output format — the competitive map is a structured table with named columns defined upfront. The Focus column is declared in the table header and conditionally populated: present and filled when `focus:` is active, absent from the header when inactive. This makes weaving a structural property of the table rather than an authorial choice.

**Hypothesis:** A column cannot be "appended" — it is either in the table or it is not. Defining the table schema before execution eliminates the failure mode where focus content drifts into a trailing section. The schema also enforces ordering (C0 at row 0) and threat levels (explicit column) as syntactic requirements rather than instructions.

---

You are running **discover-competitors-alt**.

Read the repo context (README, CLAUDE.md, package.json, or equivalent) to identify the topic. Do not ask the user for the topic, competitors, or market category.

**Focus detection:** If `focus:` is set to `market` or `positioning`, add a Focus column to the competitive map table. If not set, omit the Focus column. Resolve this before building the table.

---

### Competitive Map Table

Build the table with this schema:

**If `focus:` is inactive:**

| Label | Name | Threat | Why | Inertia delta |
|-------|------|--------|-----|---------------|

**If `focus: market`:**

| Label | Name | Threat | Why | Market segment | Inertia delta |
|-------|------|--------|-----|----------------|---------------|

**If `focus: positioning`:**

| Label | Name | Threat | Why | Positioning claim | Inertia delta |
|-------|------|--------|-----|-------------------|---------------|

**Row ordering:**

- Row 0 must be C0. Label it `C0`. Name it with the actual status-quo behavior (not "inertia" or "incumbent"). Threat level: almost always HIGH. For Inertia delta: `[ROOT — all other rows measured against this]`.
- Rows 1–N: named external competitors. Minimum 3. Every row gets an explicit HIGH / MEDIUM / LOW threat level.
- C0 inertia reasoning: the Why cell for C0 must name a specific stickiness mechanism — switching cost, habit lock-in, or workaround satisfaction — tied to something C0 does or provides.

**Citation requirement:** Run a WebSearch on at least one named external competitor. Add an inline citation in that row's Why cell (URL or publication name). Not in a footnote below the table.

---

### Whitespace Finding

After the table, write a labeled finding:

**GAP:** [specific uncontested dimension no listed competitor owns]

If `focus:` is active, the gap must be uncontested across both dimensions simultaneously. Demonstrate that the gap requires both the competitive map and the focus lens to surface — it is not visible from either alone.

---

### Findings

3–5 findings. Each must reference at least one named row label from the competitive map (e.g., `C0`, `Competitor Name`). No free-floating findings.

---

### AMEND

| # | Input change | Output effect |
|---|-------------|---------------|
| 1 | [input change] | [what changes in output] |
| 2 | [input change] | [what changes in output] |

Minimum 2 rows. Each row must name both the input change and the output effect.

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-03 — Phrasing Register (conversational imperative)

**Axis:** Phrasing register — plain English instructions with no gate labels, slot notation, or formal lifecycle vocabulary. The prompt describes what to do and why, in the order it should be done. Requirements are stated as natural language constraints, not as pass/fail tables.

**Hypothesis:** A conversational register reduces the model's tendency to narrate the gate structure rather than do the work. When instructions are in plain language, the output mirrors the intent (analysis) rather than the structure (gate passing). All 10 rubric criteria can be satisfied without formal notation.

---

You are running **discover-competitors-alt**.

Start by reading the repo to figure out what topic you're analyzing — look at the README, CLAUDE.md, or package.json. Don't ask the user what the topic is.

If `focus:` is set to `market` or `positioning`, that dimension gets woven into the competitor rows and the gap finding — not added as a section at the end.

---

**First: nail the inertia competitor.**

The most important competitor is C0 — what users do today instead of using this feature. Name it specifically (the actual tool, habit, or workaround — not just "the status quo"). Assign it a threat level (usually HIGH). Then explain *why* it's sticky: name one concrete mechanism — what would users lose if they switched, what habit would be interrupted, or what workaround already solves most of the problem. This mechanism is the anchor the rest of the analysis refers back to.

Put C0 first. Always.

---

**Then: map the real competitors.**

Name at least 3 external competitors — actual products or tools, not category labels. For each one:

- Say what their threat level is (HIGH / MEDIUM / LOW) — be explicit, not implied.
- Say why they're a real alternative in one sentence.
- Say how they relate to the C0 mechanism — do they reinforce why users stick with C0, challenge that stickiness, or add a new angle on it?
- If `focus: market` is set: add a note on what market segment this competitor owns.
- If `focus: positioning` is set: add a note on how this competitor positions themselves.

Look up at least one competitor with WebSearch. Put the citation right next to that competitor — not in a footnote at the bottom.

---

**Then: find the whitespace.**

Name one specific gap that none of the listed competitors — including C0 — own. Label it clearly. Don't just say "there's room to innovate" — say what the specific uncontested dimension is.

If `focus:` is active: the gap should only be visible when you combine the competitive map with the focus lens. A gap you could spot without the focus doesn't count.

---

**Then: write the findings.**

3–5 findings. Each one should point back to a specific named competitor from the map. Don't write general observations about the domain that could have been written without doing the competitive analysis.

---

**Finally: tell the user how to amend.**

Give at least 2 adjustments. For each one, say what the user changes as input AND what happens to the output as a result. "You can adjust the focus dimension" is not enough — say what changes when they do.

---

Write the artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-04 — Inertia Framing + Output Format (combination)

**Axis:** C0-anchored analysis combined with a table schema that propagates the inertia mechanism across every row. The table's "Inertia delta" column is defined relative to C0's named mechanism — not as a generic relationship label.

**Hypothesis:** The combination produces the most reliable cross-dimensional whitespace finding (C-09) because the table enforces focus column population per row (preventing append) while the C0 mechanism anchor provides the specific reference point from which gap claims can be evaluated as genuinely cross-dimensional.

---

You are running **discover-competitors-alt**.

Read repo context (README, CLAUDE.md, package.json) to identify the topic. Do not prompt the user. Resolve `focus:` state before building any table.

---

### Phase 1 — Inertia Anchor

Before any table, write the C0 characterization as a named block:

```
C0: [Actual name of status-quo behavior or tool]
Threat: HIGH (or stated reason if lower)
Stickiness mechanism: [switching cost | habit lock-in | workaround satisfaction] — [specific description tied to what C0 does]
```

This mechanism phrase is the `INERTIA-REF` for the analysis. Every competitor row and every finding references it.

If `focus:` is active, add:

```
Focus (C0): [market segment C0 occupies] OR [positioning claim C0 holds implicitly]
```

---

### Phase 2 — Competitive Map

Table schema depends on `focus:` state.

**If `focus:` inactive:**

| Label | Name | Threat | Why (vs INERTIA-REF) | Source |
|-------|------|--------|----------------------|--------|

**If `focus: market`:**

| Label | Name | Threat | Why (vs INERTIA-REF) | Market segment | Source |
|-------|------|--------|----------------------|----------------|--------|

**If `focus: positioning`:**

| Label | Name | Threat | Why (vs INERTIA-REF) | Positioning claim | Source |
|-------|------|--------|----------------------|-------------------|--------|

Rules:
- Minimum 3 external competitor rows (not counting C0 Phase 1 block).
- Every row: explicit HIGH / MEDIUM / LOW threat.
- "Why (vs INERTIA-REF)" column: how this competitor's appeal relates to the C0 stickiness mechanism named in Phase 1.
- Focus column: if active, populated for every row including re-stating C0's entry.
- Source column: for at least one external row, inline WebSearch citation (URL or publication name) — in the cell, not a footnote.

---

### Phase 3 — Whitespace

Write labeled finding:

**GAP:** [specific uncontested dimension]

If `focus:` inactive: gap must be uncontested by any competitor row or C0.

If `focus:` active: gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Show the intersection — state what the focus lens adds that the competitive map alone would not surface.

The GAP must explicitly state that neither C0 nor any named competitor in Phase 2 owns this dimension.

---

### Phase 4 — Findings

3–5 findings. Format:

> [Finding statement referencing named competitor or C0] — [attribute being claimed] — [how this relates to INERTIA-REF]

Each finding must name at least one row label from Phase 2 (or C0 from Phase 1). No finding may stand without a competitive anchor.

---

### AMEND

| # | Input change | What changes in output | INERTIA-REF stable? |
|---|-------------|------------------------|---------------------|
| 1 | Shift `focus:` from `market` to `positioning` | Focus column headers and values replaced throughout Phase 2; Phase 3 GAP recalculated on positioning axis | Yes |
| 2 | Add a named competitor | New row in Phase 2 table; Phase 3 GAP verified against expanded set; findings updated if gap closes | Yes |
| 3 | Deepen inertia analysis | Phase 1 mechanism block expanded with second-order switching cost; all findings re-anchored to new INERTIA-REF | No — INERTIA-REF updates |

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-05 — Lifecycle Emphasis + Inertia Framing (maximum combination)

**Axis:** Explicit named phases with phase-level output specifications, combined with C0 as the root reference node. Each phase names what it produces and which downstream phase consumes it. Inertia is resolved as a root-level computation before Phase 1 runs.

**Hypothesis:** When inertia is resolved before the competitive map is constructed (root dependency) and each phase declares its output contract, the model cannot reorder, skip inertia, or produce focus content in the wrong location. The lifecycle emphasis forces ordering (C-01) and weaving (C-03) to be structural properties of execution, not authorial choices.

---

You are running **discover-competitors-alt**.

**Auto-detect:** Read repo context (README, CLAUDE.md, package.json, or equivalent). Identify topic, market domain, and plausible competitor categories. Do not ask the user for any of these. Proceed immediately.

**Focus resolution (pre-execution):** Check `focus:` parameter. Write focus state now:
- If `focus: market` or `focus: positioning` → focus is ACTIVE; Focus column is included in Phase 2 table and Phase 3 gap.
- If `focus:` not set → focus is INACTIVE; Focus column is omitted; Phase 3 gap does not require cross-dimensional proof.

---

### ROOT — Inertia Reference

Executes before Phase 1. Produces `INERTIA-REF` consumed by all phases.

Name the status quo behavior (C0) specifically. Assign threat level. Name the stickiness mechanism — one of: switching cost, habit lock-in, workaround satisfaction — tied to a specific behavior or capability C0 provides.

Write:

```
INERTIA-REF: [C0 name] — [mechanism type]: [specific description]
Threat: [HIGH / MEDIUM / LOW]
```

If focus is ACTIVE:
```
INERTIA-REF Focus: [market segment C0 occupies] OR [positioning claim C0 holds]
```

---

### Phase 1 — Topic & Scope

Confirm topic detected from repo. Name:
- Market domain
- Primary user persona
- The decision context (what is the user choosing between?)

Consumed by: Phase 2 (scope boundary for competitor identification)

---

### Phase 2 — Competitive Map

Produces the competitor table. Consumed by: Phase 3 (gap candidates), Phase 4 (findings anchors).

**Table schema:**

If focus is INACTIVE:

| Label | Name | Threat | Why | vs INERTIA-REF |
|-------|------|--------|-----|----------------|

If focus is ACTIVE (`market`):

| Label | Name | Threat | Why | Market segment | vs INERTIA-REF |
|-------|------|--------|-----|----------------|----------------|

If focus is ACTIVE (`positioning`):

| Label | Name | Threat | Why | Positioning claim | vs INERTIA-REF |
|-------|------|--------|-----|-------------------|----------------|

Constraints:
- Row 0: C0 (re-states INERTIA-REF; `vs INERTIA-REF` = `[ROOT]`).
- Rows 1–N: minimum 3 named external competitors. No generic category labels.
- Every row: explicit HIGH / MEDIUM / LOW threat.
- Focus column: if active, populated for every row.
- `vs INERTIA-REF`: for non-C0 rows — does this competitor reinforce, challenge, or contextualize the C0 mechanism named in ROOT?
- Citation: run WebSearch on at least one external row. Inline citation in that row's Why cell.

Phase 2 complete when: C0 at row 0, >= 3 external rows, all rows have threat level, citation present.

---

### Phase 3 — Whitespace

Consumed by: Phase 4 (findings set).

Identify the uncontested gap. Write labeled finding:

**GAP:** [specific dimension not owned by C0 or any Phase 2 competitor]

If focus is INACTIVE: gap is uncontested across the competitive map.

If focus is ACTIVE: gap must be uncontested across BOTH competitive and focus dimensions simultaneously. Show intersection — the finding must require both the Phase 2 map and the focus column to produce. A gap visible from the competitive map alone does not qualify.

---

### Phase 4 — Findings

Consumed by: output artifact.

Write 3–5 findings. Each finding must:

1. Name at least one labeled competitor from Phase 2 (or C0 from ROOT) as its anchor.
2. State a specific attribute, behavior, or claim — not general domain knowledge.
3. Findings that could be written without having run Phase 2 fail the grounding test.

---

### AMEND

Consumed by: user (amendment entry point).

| # | Input change | Output effect |
|---|-------------|---------------|
| 1 | Shift `focus:` dimension | Focus column headers and values replaced in Phase 2 table; Phase 3 gap recalculated on new axis; Phase 4 findings referencing focus re-evaluated |
| 2 | Adjust depth | Brief: Phase 4 condensed to 3 findings, AMEND omitted. Full (default): all phases. Deep: Phase 2 expanded with 2+ additional competitor rows; Phase 3 gap verified against expanded set |
| 3 | Narrow competitor set | Specify domain or tier; Phase 1 scope boundary updates; Phase 2 repopulated within narrowed scope; Phase 3 gap rechecked |

Minimum 2 rows. Each row must name both input change and output effect.

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.
