Written to `simulations/quest/variations/discover-competitors-alt-variations-R3-2026-03-18.md`.

---

## R3 Variations — Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Inertia framing (token-first pre-declaration) | Declaring TOKEN before C0 makes C-13 structurally prior — model commits to a copyable identifier before describing the mechanism, eliminating role-description drift |
| V-02 | Output format (per-entry STABILITY tag in prose AMEND) | A mandatory `STABILITY:` tagged line per prose AMEND entry enforces C-14 without a table column — tests whether inline tag enforcement is as reliable as a column |
| V-03 | Phrasing register (portable token contract as opening obligation) | An opening contract with explicit token/role-description distinction by example makes C-13 fail-safe in conversational register; three-obligation structure closes C-14 simultaneously |
| V-04 | Token-first + per-entry STABILITY imperative (minimal combination) | Two surgical additions to a clean baseline: pre-declaration for C-13, prose STABILITY line for C-14 — no lifecycle overhead |
| V-05 | Role sequence + domain-adaptive token + stability matrix (full combination) | Domain-specific tokens encode context that generic labels don't; two-column stability matrix (verdict + evidence) prevents empty-form C-14 compliance |

---

**Key design decisions for R3:**

**C-13 failure mode** is role-description drift — the model writes "the inertia mechanism" and never assigns a referenceable handle. Three approaches tested: V-01 (token declared before C0, so it exists before any description is written), V-03 (negative examples — explicit list of what does NOT qualify), V-05 (domain-adaptive naming — token must encode product context, making generic labels structurally wrong).

**C-14 failure mode** is partial coverage — stability addressed for one or two AMEND entries but silent on others. R2's table column satisfies C-14 by construction. V-02 tests whether a prose `STABILITY:` tag achieves the same coverage without table format. V-05 adds a second evidence column to prevent mechanical "Stable" answers without reasoning.

**R2 carry-overs** (C-09, C-10, C-11, C-12) are treated as solved — all five variations inherit the findings template slot and per-entry stability enforcement.
applies to every row. V-02 tests whether a prose STABILITY tag achieves the same coverage without table format. V-04 is the minimal combination.

- **Single-axis isolations target the failure mode, not just the criterion.** V-01 isolates token ordering; V-02 isolates per-entry tag enforcement. Either could satisfy the criterion — the question is which mechanism is more robust to model variance.

- **V-05 introduces two genuinely new mechanisms.** Domain-adaptive tokens test whether domain-specific naming improves propagation consistency. The stability matrix (verdict + evidence) tests whether two-column enforcement prevents empty-form compliance where a model writes "Stable" without reasoning.

- **R2 carry-overs:** C-09 (cross-dimensional gap), C-10 (grounded findings), C-11 (propagation), C-12 (at-least-one stability) are treated as solved. Each variation inherits the findings template slot (C-11) and a per-entry stability enforcement mechanism (C-12 + C-14).

---

## V-01 -- Token-first inertia framing (pre-declaration before C0)

**Axis:** Inertia framing -- token ordering. The portable token is declared as the first model output, before any C0 description begins. C0 then uses the declared token as a field label. All downstream sections inherit the token name from this pre-declaration step.

**Hypothesis:** Requiring the model to choose and declare a copyable token BEFORE writing C0 makes C-13 structurally prior to all analysis. The token name exists before the mechanism description, so the description naturally uses the token as a label -- eliminating the failure mode where a model describes a mechanism and then refers to it only as "the inertia mechanism" or "the C0 stickiness factor" without assigning a referenceable handle.

---

You are running **discover-competitors-alt**.

Read the repo context (README, CLAUDE.md, package.json, or equivalent) to identify the topic. Do not ask the user for the topic, competitors, or market category. Proceed immediately.

**Focus detection:** Resolve `focus:` state before producing any output.
- `focus: market` -- market segment column ACTIVE.
- `focus: positioning` -- positioning claim column ACTIVE.
- Not set -- focus column INACTIVE.

---

### Step 0 -- Token Declaration

**Execute this step before writing anything else.**

Name a short, standalone token for the status-quo stickiness mechanism. The token must be a copyable identifier -- it can appear verbatim in a column header, finding slot, or AMEND row without surrounding context to interpret it.

Examples of valid tokens: `SPREADSHEET-LOCK`, `CLI-HABIT`, `WORKAROUND-FIT`, `MECH`, `GIT-LOCK`.

A role description is not a token. "The inertia mechanism," "the C0 stickiness factor," and "the current workflow's lock-in" do not qualify.

Write:

```
TOKEN: [short identifier]
```

This token is the portable label for the inertia mechanism throughout this analysis. Use it verbatim in:
- The C0 block field label
- The competitive map column header (`vs [TOKEN]`)
- The third slot of every finding
- The stability column header of the AMEND table

---

### C0 -- Inertia Anchor

Name the actual status-quo behavior, tool, or workaround -- not "inertia" or "incumbent." Assign a threat level (almost always HIGH). Describe the stickiness mechanism -- what would users lose if they switched, what habit would be interrupted, or what workaround already solves most of the problem. Use the token from Step 0 as the field label:

```
C0: [Actual name]
Threat: HIGH (or justified lower)
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction]
  -> [Specific description tied to what C0 does or provides]
```

If `focus:` is ACTIVE:
```
C0 Focus: [market segment C0 occupies] OR [positioning claim C0 holds implicitly]
```

---

### Competitive Map

Row 0 is C0. Rows 1-N are named external competitors -- minimum 3. Every row: explicit HIGH / MEDIUM / LOW threat. No generic category labels.

**If focus INACTIVE:**

| Label | Name | Threat | Why | vs [TOKEN] |
|-------|------|--------|-----|------------|

**If focus ACTIVE (market):**

| Label | Name | Threat | Why | Market segment | vs [TOKEN] |
|-------|------|--------|-----|----------------|------------|

**If focus ACTIVE (positioning):**

| Label | Name | Threat | Why | Positioning claim | vs [TOKEN] |
|-------|------|--------|-----|-------------------|------------|

Column notes:
- **vs [TOKEN]**: Use the Step 0 token as the column header. C0 row: `[ROOT]`. External rows: does this competitor reinforce, challenge, or contextualize the mechanism the token names? Reference the mechanism description -- not a generic relationship label.
- **Why**: For at least one external row, include an inline citation (URL or publication name) from a WebSearch result in this cell. Not a footnote.

---

### Whitespace Finding

**GAP:** [specific uncontested dimension not owned by C0 or any listed competitor]

Name the specific dimension. A generic statement ("there is room to innovate") does not pass.

If focus ACTIVE: the gap must be uncontested across BOTH the competitive dimension AND the focus dimension simultaneously. Show the intersection -- demonstrate that neither the competitive map alone nor the focus column alone would surface this gap.

---

### Findings

Write 3-5 findings. Each uses this template:

> **[Competitor label or C0]** -- [specific claim about this competitor's behavior or capability] -- *[TOKEN]: [how this finding connects to the mechanism named in Step 0]*

The third slot is mandatory. Use the Step 0 token as the slot label. A finding that does not fill this slot does not pass. Do not write general domain observations -- each finding must require the competitive map to support it.

---

### AMEND

List at least 2 adjustments. For each, name the input change, the output effect, and whether the TOKEN's referent would change or remain stable:

| # | Input change | Output effect | [TOKEN] stable? |
|---|--------------|---------------|-----------------|
| 1 | Shift `focus:` dimension | Focus column headers and values replaced; whitespace finding recalculated on new axis | Yes -- the C0 stickiness mechanism does not change when the focus lens rotates |
| 2 | Add a named competitor | New row in competitive map; whitespace finding verified against expanded set; findings updated if gap closes | Yes -- unless the new competitor fundamentally reframes the primary switching barrier |
| 3 | Deepen inertia analysis | [TOKEN] block expanded with second-order effects; all `vs [TOKEN]` cells re-evaluated; findings re-anchored | No -- [TOKEN] referent updates; downstream references must propagate |

Use the Step 0 token as the column header. The `[TOKEN] stable?` column is required for every row -- Yes, No, or conditional with explanation. A silent entry does not pass.

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-02 -- Per-entry tagged stability field in prose AMEND

**Axis:** Output format -- AMEND structure. All other sections are standard. The AMEND section uses a prose numbered-list format (not a table). Each entry has a mandatory `STABILITY:` tagged line. Tests whether inline tag enforcement in non-table format reliably satisfies C-14 across every entry.

**Hypothesis:** C-14 requires stability addressed in EVERY AMEND entry. R2's table-column approach works but is coupled to table format. A prose AMEND with a mandatory `STABILITY:` tag per entry decouples C-14 enforcement from table structure -- the tag is a format primitive that survives format variation. If the tag approach works, it establishes that C-14 enforcement is vehicle-agnostic, not table-specific.

---

You are running **discover-competitors-alt**.

Read the repo context (README, CLAUDE.md, package.json, or equivalent) to identify the topic. Do not ask the user for the topic, competitors, or market category. Proceed immediately.

**Focus detection:** Check `focus:` parameter before producing any output.
- `focus: market` -- market segment column ACTIVE.
- `focus: positioning` -- positioning claim column ACTIVE.
- Not set -- focus column INACTIVE.

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

`INERTIA-REF` is the portable token for this analysis. It appears verbatim in the competitive map's column header, in the third slot of every finding, and in the `STABILITY:` line of every AMEND entry.

If `focus:` is ACTIVE:
```
C0 Focus: [market segment C0 occupies] OR [positioning claim C0 holds implicitly]
```

---

### Competitive Map

Row 0 is C0. Rows 1-N are named external competitors -- minimum 3. Every row: explicit HIGH / MEDIUM / LOW threat. No generic category labels.

**If focus INACTIVE:**

| Label | Name | Threat | Why | vs INERTIA-REF |
|-------|------|--------|-----|----------------|

**If focus ACTIVE (market):**

| Label | Name | Threat | Why | Market segment | vs INERTIA-REF |
|-------|------|--------|-----|----------------|----------------|

**If focus ACTIVE (positioning):**

| Label | Name | Threat | Why | Positioning claim | vs INERTIA-REF |
|-------|------|--------|-----|-------------------|----------------|

Column notes:
- **vs INERTIA-REF**: C0 row: `[ROOT]`. External rows: how does this competitor's appeal relate to the mechanism described in `INERTIA-REF`? Name the mechanism -- don't use a generic relationship label.
- **Why**: For at least one external row, inline WebSearch citation (URL or publication name) in this cell. Not a footnote.

---

### Whitespace Finding

**GAP:** [specific uncontested dimension not owned by C0 or any named competitor]

Name the specific dimension. A generic statement does not pass.

If focus ACTIVE: the gap must be uncontested across BOTH the competitive dimension AND the focus dimension simultaneously. Demonstrate that combining the competitive map and the focus lens surfaces a gap neither alone would produce.

---

### Findings

Write 3-5 findings. Each uses this template:

> **[Competitor label or C0]** -- [specific claim about this competitor's behavior or capability] -- *vs INERTIA-REF: [how this finding relates to the mechanism named in the C0 block]*

The third slot is mandatory. Do not write general domain observations -- each finding must require the competitive map to support it.

---

### AMEND

Write at least 2 amendments as a numbered list. Each amendment has three required parts:

1. A bold heading naming the input change.
2. An `Output effect:` line stating what changes in the analysis as a result -- be specific, not just "you can adjust."
3. A `STABILITY:` line stating whether `INERTIA-REF` would change or remain stable, and why.

The `STABILITY:` line is required for every amendment. An amendment without it does not pass.

Example format:

```
1. **Shift `focus:` from `market` to `positioning`**
   Output effect: Focus column headers and values replaced throughout the competitive map;
   whitespace finding recalculated on the positioning axis; findings referencing market segments
   re-evaluated.
   STABILITY: Stable -- the C0 stickiness mechanism does not depend on which focus lens is active.

2. **Add a named competitor**
   Output effect: New row added to competitive map; whitespace finding verified against expanded
   set; findings updated if gap closes or a new threat reframes the landscape.
   STABILITY: Stable unless the new competitor directly reframes what users lose by switching
   away from C0.

3. **Deepen inertia analysis**
   Output effect: INERTIA-REF block expanded with second-order switching costs; all
   `vs INERTIA-REF` cells re-evaluated; findings re-anchored to the updated mechanism.
   STABILITY: Shifts -- INERTIA-REF updates to reflect the expanded mechanism description;
   all downstream references propagate.
```

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-03 -- Phrasing register -- Portable token contract as opening obligation

**Axis:** Phrasing register -- fully conversational, but opens with an explicit "portable token contract" that defines what a copyable token is, what it is NOT (with examples of each), and what three obligations the chosen token creates. The contract precedes all analysis.

**Hypothesis:** V-03-R2 achieved a perfect score by instructing the model to "give it a short label." R3's C-13 is stricter: role descriptions (which pass casual inspection) explicitly fail. An opening contract that draws the token/role-description distinction with negative examples -- before the model writes anything -- makes C-13 fail-safe in conversational register. The three-obligation structure (name it, use it everywhere, check stability per entry) simultaneously closes C-14. Conversational register with an explicit opening contract is a lighter-weight path to both new criteria than structured enforcement.

---

You are running **discover-competitors-alt**.

Start by reading the repo -- README, CLAUDE.md, or package.json -- to figure out what you're analyzing. Don't ask the user for the topic, competitors, or market category.

If `focus:` is set to `market` or `positioning`, weave that dimension into competitor rows and the gap finding from the start. Don't append it as a separate section at the end.

---

**Before writing anything: establish your portable token contract.**

You are about to name a stickiness mechanism. Before you describe it, give it a name -- a short, copyable token.

These are **not** tokens -- they are role descriptions and do not qualify:
- "the inertia mechanism"
- "the C0 stickiness factor"
- "the current workflow's lock-in"
- "the incumbent's advantage"

These **are** tokens -- standalone identifiers that can be copied verbatim:
- `SPREADSHEET-LOCK`
- `CLI-HABIT`
- `WORKAROUND-FIT`
- `MECH`
- `GIT-LOCK`

A token is something you can paste into a column header, a finding label, or an AMEND entry -- and anyone reading that column or entry knows exactly what it refers to, without needing the surrounding prose.

Choose your token now. Write it as:

> **Token: [YOUR-TOKEN]** -- [one sentence: what this token names]

Your token creates three obligations that apply for the rest of this analysis:
1. Use it in C0 to label the mechanism -- not as a role description, as the label itself.
2. Use it verbatim in every finding -- in the third slot, referencing how the finding connects to the mechanism.
3. For every amendment entry in AMEND: state whether your token's referent would change or stay stable.

Now proceed.

---

**First: nail C0.**

Name the actual status-quo tool, habit, or workaround -- not "the status quo" or "incumbent." Assign a threat level (usually HIGH). Then explain the stickiness: what would users lose if they switched, what habit would break, or what workaround already covers most of the need.

Label the mechanism with your token:

> **[Token]: [specific mechanism tied to what C0 does or provides]**

Write C0 first. Always.

---

**Then: map at least 3 external competitors.**

Name actual products or tools -- no category labels. For each:
- Threat level: HIGH / MEDIUM / LOW -- be explicit.
- One sentence on why they're a real alternative.
- How they relate to your token -- do they reinforce C0's stickiness, challenge it, or add a new angle? Use the token name when you describe this.
- If `focus: market`: add the market segment this competitor owns.
- If `focus: positioning`: add how this competitor positions themselves.

Look up at least one competitor with WebSearch. Put the citation right next to that competitor -- not in a footnote.

---

**Then: find the whitespace.**

Name one specific gap that none of the listed competitors -- including C0 -- own. Label it clearly. Don't say "there's room to innovate" -- name the specific uncontested dimension.

If `focus:` is active: the gap must only be visible when you combine the competitive map with the focus lens. Show what the focus dimension adds that the map alone wouldn't surface.

---

**Then: write 3-5 findings.**

For each:
- Name a specific competitor from the map (or C0).
- Reference your token -- say how this finding connects to the mechanism it names. Use the token label, not a role description.
- Don't write general domain observations that don't require the competitive analysis.

---

**Finally: tell the user how to amend -- and check the token for every entry.**

Give at least 2 adjustments. For each:
- Say what the user changes as input.
- Say what changes in the output as a result -- be specific, not just "you can adjust."
- Check your token: state whether the amendment would change what your token refers to, or leave it stable. If it shifts, say why. This check is required for every amendment -- not just one.

---

Write the artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-04 -- Token-first anchor + per-entry STABILITY imperative (minimal combination)

**Axis:** Inertia framing (token-first pre-declaration) combined with output format (per-entry STABILITY line in prose AMEND). Minimum overhead -- no full lifecycle scaffolding, no phase headers. Two targeted structural additions to a clean baseline: one for C-13, one for C-14.

**Hypothesis:** The minimum sufficient combination for C-13 and C-14: a pre-declaration step that forces a copyable token before C0 begins (eliminating the role-description failure mode), and a prose AMEND with a mandatory STABILITY line per entry (preventing silent entries). No lifecycle scaffolding required. Tests whether two surgical additions to a clean baseline achieve both criteria with less overhead than the full phase-based approach.

---

You are running **discover-competitors-alt**.

Read the repo context (README, CLAUDE.md, package.json, or equivalent) to identify the topic. Do not prompt the user. Resolve `focus:` state before producing any output.

**Focus state:**
- `focus: market` -- market segment column ACTIVE
- `focus: positioning` -- positioning claim column ACTIVE
- Not set -- focus column INACTIVE

---

### Token Declaration

**Execute before anything else.**

Declare a short, standalone token for the status-quo stickiness mechanism. The token must be a copyable identifier -- it stands alone without surrounding context. It can appear verbatim in a column header, finding label, or AMEND stability line.

Valid tokens: `SPREADSHEET-LOCK`, `MECH`, `CLI-HABIT`, `WORKAROUND-FIT`, `GIT-LOCK`.

Role descriptions are not tokens: "the inertia mechanism," "the stickiness factor," "the current lock-in."

Write:

```
TOKEN: [short identifier]
```

Use this token verbatim in: the C0 block field label, the competitive map's `vs [TOKEN]` column header, the third slot of every finding, and the `STABILITY:` line of every AMEND entry.

---

### C0 -- Inertia Anchor

```
C0: [Actual name -- not "inertia" or "incumbent"]
Threat: HIGH (or justified lower)
[TOKEN]: [mechanism type: switching cost | habit lock-in | workaround satisfaction]
  -> [Specific description tied to what C0 does or provides]
```

Use the declared token as the field label. If `focus:` is ACTIVE:
```
C0 Focus: [market segment C0 occupies] OR [positioning claim C0 holds implicitly]
```

---

### Competitive Map

Row 0 is C0. Rows 1-N: minimum 3 named external competitors. No generic labels. Every row: explicit HIGH / MEDIUM / LOW threat.

**If focus INACTIVE:**

| Label | Name | Threat | Why | vs [TOKEN] |
|-------|------|--------|-----|------------|

**If focus ACTIVE (market):**

| Label | Name | Threat | Why | Market segment | vs [TOKEN] |
|-------|------|--------|-----|----------------|------------|

**If focus ACTIVE (positioning):**

| Label | Name | Threat | Why | Positioning claim | vs [TOKEN] |
|-------|------|--------|-----|-------------------|------------|

Column notes:
- **vs [TOKEN]**: Use the declared token as the column header. C0 row: `[ROOT]`. External rows: how does this competitor's appeal interact with the declared mechanism? Reference the mechanism -- not a generic label.
- **Why**: For at least one external row, inline WebSearch citation (URL or publication name) in this cell. Not a footnote.

---

### Whitespace Finding

**GAP:** [specific uncontested dimension not owned by C0 or any named competitor]

Name the specific dimension.

If focus ACTIVE: gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Show the intersection -- state what the focus lens adds that the competitive map alone would not surface.

---

### Findings

Write 3-5 findings. Each uses this template:

> **[Competitor label or C0]** -- [specific claim about behavior or capability] -- *[TOKEN]: [how this finding connects to the mechanism declared in Token Declaration]*

The third slot is mandatory. Use the declared token as the slot label. Do not write general domain observations -- each finding must require the competitive map.

---

### AMEND

Write at least 2 amendments as a numbered list. Each amendment requires three parts:

1. **[Input change]** -- bold heading naming what the user would change.
2. **Output effect:** [What changes in the analysis -- be specific about what updates in the output].
3. **STABILITY:** [Stable | Shifts -- reason] -- state whether the TOKEN's referent would change.

The `STABILITY:` line is required for every amendment entry. An entry without it does not pass.

Example:

```
1. **Shift `focus:` from `market` to `positioning`**
   Output effect: Focus column headers and values replaced throughout the competitive map;
   whitespace finding recalculated on the positioning axis.
   STABILITY: Stable -- the C0 mechanism does not depend on which focus lens is active.

2. **Add a named competitor**
   Output effect: New row in competitive map; whitespace finding verified against expanded set;
   findings updated if gap closes.
   STABILITY: Stable unless the new competitor fundamentally reframes the primary switching
   barrier.

3. **Deepen inertia analysis**
   Output effect: TOKEN block expanded with second-order effects; all `vs TOKEN` cells
   re-evaluated; findings re-anchored.
   STABILITY: Shifts -- TOKEN's referent updates; downstream references must propagate.
```

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-05 -- Full lifecycle with domain-adaptive token and stability matrix

**Axis:** Role sequence combined with lifecycle emphasis and inertia framing. Extends V-05-R2 with: (1) explicit instruction to choose a domain-adaptive token (not always INERTIA-REF) meaningful to the specific product context, and (2) a two-column stability matrix for AMEND (verdict + evidence) that prevents empty-form C-14 compliance.

**Hypothesis:** Domain-adaptive tokens (e.g., `EXCEL-LOCK` for a spreadsheet-replacing tool) encode product context that generic labels don't -- the model can't accidentally produce generic stability reasoning because the token name itself frames the question. The stability matrix (verdict column + evidence column, both required) prevents a model from satisfying C-14 with a mechanical "Stable" without reasoning. Together they target the highest-variance failure modes of C-13 and C-14 at the architectural level.

---

You are running **discover-competitors-alt**.

**Auto-detect:** Read repo context (README, CLAUDE.md, package.json, or equivalent). Identify topic, market domain, and plausible competitor categories. Do not prompt the user. Proceed immediately.

**Focus resolution (pre-execution):** Resolve `focus:` state and write it as a declaration before any output:

```
Focus state: [ACTIVE: market | ACTIVE: positioning | INACTIVE]
```

- ACTIVE -- Focus column included in Phase 2; Phase 3 gap requires cross-dimensional proof.
- INACTIVE -- Focus column omitted; Phase 3 gap requires competitive proof only.

---

### ROOT -- Domain-Adaptive Token + Inertia Anchor

**Produces:** `TOKEN` -- consumed by Phase 2, Phase 3, Phase 4, AMEND.

**Executes before Phase 1.**

**Step A: Choose a domain-adaptive token.**

Name a short token for the status-quo stickiness mechanism that is specific to this product domain -- not a generic template label. The token must be a copyable standalone identifier: it appears verbatim in column headers, finding slots, and AMEND cells without additional context.

Choose a token that encodes domain context:
- For a spreadsheet-replacing tool: `SHEET-LOCK`
- For a CLI-first developer tool: `CLI-HABIT`
- For a workaround-satisfying integration tool: `WORKAROUND-FIT`
- For a habit-driven consumer tool: `DAILY-HABIT`
- When no clear domain term fits: `MECH`

A role description is not a token. "The inertia mechanism" and "the stickiness factor" cannot appear verbatim in a column header without interpretation.

Write:

```
TOKEN: [domain-specific identifier]
```

**Step B: Name C0 and the mechanism.**

Name the status-quo behavior or tool (not "inertia" or "incumbent"). Assign threat level. Name the stickiness mechanism -- one of: switching cost, habit lock-in, workaround satisfaction -- tied to a specific behavior or capability C0 does or provides.

Write:

```
C0: [Actual name]
Threat: [HIGH / MEDIUM / LOW]
[TOKEN]: [mechanism type]: [specific description]
```

If focus is ACTIVE:
```
[TOKEN] Focus: [market segment C0 occupies] OR [positioning claim C0 holds]
```

ROOT complete when: TOKEN is a standalone domain-specific identifier; C0 named specifically; mechanism type declared; specific description provided.

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

**Consumes:** Phase 1 topic declaration, ROOT TOKEN, focus state.
**Produces:** competitor table -- consumed by Phase 3, Phase 4, AMEND.

**If focus INACTIVE:**

| Label | Name | Threat | Why | vs [TOKEN] | Source |
|-------|------|--------|-----|------------|--------|

**If focus ACTIVE (market):**

| Label | Name | Threat | Why | Market segment | vs [TOKEN] | Source |
|-------|------|--------|-----|----------------|------------|--------|

**If focus ACTIVE (positioning):**

| Label | Name | Threat | Why | Positioning claim | vs [TOKEN] | Source |
|-------|------|--------|-----|-------------------|------------|--------|

Constraints:
- Row 0: C0 re-states ROOT mechanism. `vs [TOKEN]` = `[ROOT]`.
- Rows 1-N: minimum 3 named external competitors. No generic labels.
- Every row: explicit HIGH / MEDIUM / LOW threat.
- **vs [TOKEN]**: Use ROOT token as column header. How does this competitor's appeal interact with the ROOT mechanism? Reference the mechanism description -- not a generic label.
- Focus column: populated for every row if focus ACTIVE.
- Source: for at least one external row, inline WebSearch citation in this cell. Not a footnote.

Phase 2 complete when: C0 at row 0, >= 3 external rows, every row has threat level, citation present, every `vs [TOKEN]` cell references ROOT mechanism.

---

### Phase 3 -- Whitespace

**Consumes:** Phase 2 competitor table, ROOT TOKEN (for gap rationale), focus state.
**Produces:** labeled GAP finding -- consumed by Phase 4.

Write:

**GAP:** [specific dimension not owned by C0 or any Phase 2 competitor]

If focus INACTIVE: state why the ROOT mechanism does not cover this gap.

If focus ACTIVE: gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Show intersection -- name what the focus lens adds that the competitive map alone would not surface. Confirm that the ROOT mechanism does not cover this gap either.

---

### Phase 4 -- Findings

**Consumes:** Phase 2 competitor table, Phase 3 GAP, ROOT TOKEN.
**Produces:** findings -- consumed by output artifact.

Write 3-5 findings. Each uses this template:

> **[Competitor label or C0 from Phase 2]** -- [specific claim] -- *[TOKEN]: [connection to the ROOT mechanism]*

Rules:
- Third slot is mandatory -- use the ROOT token as the slot label.
- Findings that could be written without Phase 2 fail the grounding test.
- Findings that do not fill the TOKEN slot fail the propagation test.

---

### AMEND -- Stability Matrix

**Consumes:** all phases.
**Produces:** stability matrix with input-to-output pairs and per-entry stability verdicts with evidence.

Output contract: for every row, name (1) the input change, (2) the output effect across affected phases, (3) a stability verdict (Stable / Shifts / Conditional), and (4) evidence supporting the verdict.

| # | Input change | Output effect | [TOKEN] verdict | Evidence |
|---|--------------|---------------|-----------------|----------|
| 1 | Shift `focus:` dimension | Phase 2 focus column headers and values replaced; Phase 3 GAP recalculated; Phase 4 findings referencing focus re-evaluated | Stable | The C0 mechanism is independent of the focus lens -- rotating focus does not alter what users lose by switching away from C0 |
| 2 | Adjust depth to `brief` | Phase 4 condensed to 3 findings; AMEND omitted | Stable | Reducing output depth does not alter the underlying stickiness mechanism |
| 3 | Narrow competitor set to a specific tier | Phase 1 scope boundary updates; Phase 2 repopulated within narrowed scope; Phase 3 GAP rechecked | Conditional | If narrowing reframes the decision context, ROOT mechanism may need revision -- verify whether C0 still holds dominant position in the narrowed scope |
| 4 | Deepen inertia analysis | ROOT TOKEN block expanded with second-order effects; Phase 2 `vs [TOKEN]` column re-evaluated; Phase 4 findings re-anchored | Shifts | ROOT updates; TOKEN abbreviation may remain the same but its mechanism description changes; all consuming phases propagate |

Minimum 2 rows. Both `[TOKEN] verdict` AND `Evidence` columns are required for every row. A row with a verdict but no evidence does not satisfy the AMEND output contract. A row with evidence but no verdict does not satisfy the AMEND output contract. A stability answer without reasoning does not satisfy the Evidence column.

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.
