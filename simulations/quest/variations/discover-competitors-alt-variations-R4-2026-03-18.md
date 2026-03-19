Written to `simulations/quest/variations/discover-competitors-alt-variations-R4-2026-03-18.md`.

---

## R4 Variations — Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Single-axis C-17 via domain term extraction | DOMAIN-TERMS micro-step commits product vocabulary before token naming — model cannot drift to MECH when it has written domain terms in the output |
| **V-02** | Single-axis C-16 via single-line verdict+evidence | `STABILITY: [verdict] — [evidence]` with explicit "a verdict without a reason does not pass" — tests whether C-16 enforcement is format-agnostic |
| **V-03** | Single-axis C-15 strictness — token as absolute first output | TOKEN is the literal first output line, before focus detection and setup — eliminates all ordering ambiguity |
| **V-04** | Minimal combination of all three | Three surgical additions to R3 V-04 baseline: extraction step + pre-declaration + two-tag AMEND (STABILITY + EVIDENCE) — minimum overhead for all new criteria |
| **V-05** | Full lifecycle with structural enforcement of all three | ROOT phase: Step A extracts domain terms, Step B commits token, Step C writes C0. AMEND: two-column verdict+evidence matrix with explicit contract. Maximum structural guarantees. |

---

**Design rationale:**

**R3 failure pattern for C-16:** All R3 variations except V-05 satisfied the STABILITY: tag requirement but left evidence unenforceable — a model can write "Stable" on every entry mechanically. R4 tests three evidence-enforcement mechanisms: two-tag (STABILITY/EVIDENCE separate lines in V-01/V-03/V-04), single-line with mandatory dash-clause (`STABILITY: verdict — reason` in V-02), and two-column table (V-05).

**R3 failure pattern for C-17:** V-01/V-04 explicitly named MECH and CLI-HABIT as valid tokens, inviting generic choices. V-02 hardcoded INERTIA-REF (generic). R4 enforces domain-specificity via extraction in V-01/V-04/V-05 (commit vocabulary first) and via negative-example instruction in V-02/V-03.

**C-15 spectrum tested:** V-03 is the strictest (TOKEN before everything), V-01/V-02/V-04 use a labeled "before anything else" step, V-05 uses ROOT phase ordering. The scoring question is whether any of these interpretations fall short of "before the first sentence of C0 mechanism prose."
verdict column + evidence column, both required).

**C-15 failure mode** is structural ambiguity — "declared before C0" is satisfied if TOKEN appears anywhere before C0 prose, but a model might embed the declaration mid-C0 or just prior to the mechanism sentence. V-03 tests maximum strictness: TOKEN is the absolute first model output, before focus detection and before any other setup. All other variations use a pre-declaration step clearly prior to C0 section.

**R3 carry-overs** (C-09 through C-14) are treated as solved. All five variations inherit: domain-specific token (C-17 closes C-13 gap for generic tokens), pre-declaration (C-15 closes remaining C-13/C-15 gap), findings template slot (C-10/C-11), per-entry stability enforcement (C-12/C-14), evidence per entry (C-16).

---

## V-01 — Domain term extraction before token declaration (single-axis: C-17)

**Axis:** C-17 enforcement — domain term extraction. A DOMAIN-TERMS micro-step forces the model to name product-specific vocabulary from repo context before choosing a token. The token must incorporate at least one extracted term. Inherits C-15 (pre-declaration step before C0), C-16 (two-tag AMEND: STABILITY + EVIDENCE per entry).

**Hypothesis:** C-17 fails through drift toward template labels. Requiring the model to explicitly extract domain-specific terms (naming SIGNAL, PLUGIN, TOPIC, NAMESPACE, etc.) before choosing the token makes domain-specificity structural. The model cannot write MECH or INERTIA-REF when it has just committed to product vocabulary in writing. Extraction eliminates the drift path that instruction-only approaches leave open.

---

You are running **discover-competitors-alt**.

Read the repo context (README, CLAUDE.md, package.json, or equivalent) to identify the topic. Do not ask the user for the topic, competitors, or market category. Proceed immediately.

**Focus detection:** Resolve `focus:` state before producing any output.
- `focus: market` — market segment column ACTIVE.
- `focus: positioning` — positioning claim column ACTIVE.
- Not set — focus column INACTIVE.

---

### Token Declaration

**Execute this step before writing anything else.**

**Step 1: Extract domain terms.**

From the repo context, list 2-3 terms that are specific to this product's domain — drawn from product names, workflow concepts, category terms, or namespace labels in README, CLAUDE.md, or package.json. These are the vocabulary the token must draw from.

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
```

**Step 2: Declare a domain-adaptive token.**

Choose a short, standalone identifier for the status-quo stickiness mechanism. The token must include at least one term from DOMAIN-TERMS. A generic placeholder alone (MECH, LOCK, INERTIA-REF) does not pass — the token must encode product context.

Valid structure examples: `[DOMAIN-TERM]-LOCK`, `[DOMAIN-TERM]-HABIT`, `[DOMAIN-TERM]-GRIP` — e.g., `SIGNAL-LOCK`, `WORKFLOW-HABIT`, `SHEET-GRIP`.

A role description is not a token. "The inertia mechanism," "the stickiness factor," and "the C0 lock-in" do not qualify regardless of how they are formatted.

Write:

```
TOKEN: [domain-adaptive identifier including at least one DOMAIN-TERMS term]
```

This token is the portable label for the inertia mechanism throughout this analysis. Use it verbatim in:
- The C0 block field label
- The competitive map column header (`vs [TOKEN]`)
- The third slot of every finding
- The STABILITY: and EVIDENCE: lines of every AMEND entry

---

### C0 — Inertia Anchor

Name the actual status-quo behavior, tool, or workaround — not "inertia" or "incumbent." Assign a threat level (almost always HIGH). Describe the stickiness mechanism — what would users lose if they switched, what habit would be interrupted, or what workaround already solves most of the problem.

Use the token from Token Declaration as the field label:

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

Row 0 is C0. Rows 1-N are named external competitors — minimum 3. Every row: explicit HIGH / MEDIUM / LOW threat. No generic category labels.

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
- **vs [TOKEN]**: Use the Token Declaration identifier as the column header. C0 row: `[ROOT]`. External rows: how does this competitor's appeal interact with the mechanism named in TOKEN? Reference the mechanism description — not a generic relationship label.
- **Why**: For at least one external row, include an inline citation (URL or publication name) from a WebSearch result in this cell. Not a footnote.

---

### Whitespace Finding

**GAP:** [specific uncontested dimension not owned by C0 or any listed competitor]

Name the specific dimension. A generic statement ("there is room to innovate") does not pass.

If focus ACTIVE: the gap must be uncontested across BOTH the competitive dimension AND the focus dimension simultaneously. Show the intersection — demonstrate that neither the competitive map alone nor the focus column alone would surface this gap.

---

### Findings

Write 3-5 findings. Each uses this template:

> **[Competitor label or C0]** — [specific claim about this competitor's behavior or capability] — *[TOKEN]: [how this finding connects to the mechanism named in Token Declaration]*

The third slot is mandatory. Use the Token Declaration identifier as the slot label. A finding that does not fill this slot does not pass. Do not write general domain observations — each finding must require the competitive map to support it.

---

### AMEND

Write at least 2 amendments as a numbered list. Each amendment requires three parts:

1. **[Input change]** — bold heading naming what the user would change.
2. **Output effect:** [What changes in the analysis — specific to sections that update].
3. **STABILITY:** [Stable | Shifts | Conditional]
4. **EVIDENCE:** [Reasoning that supports the verdict — why the TOKEN's referent changes or stays stable].

Both STABILITY: and EVIDENCE: lines are required for every amendment entry. An entry that omits either line does not pass. A STABILITY: verdict without EVIDENCE: is not sufficient — the reasoning must be present.

Example:

```
1. **Shift `focus:` from `market` to `positioning`**
   Output effect: Focus column headers and values replaced throughout the competitive map;
   whitespace finding recalculated on the positioning axis; findings referencing market
   segments re-evaluated.
   STABILITY: Stable
   EVIDENCE: The C0 stickiness mechanism is independent of which focus lens is active —
   rotating from market to positioning does not change what users lose by switching away
   from C0.

2. **Add a named competitor**
   Output effect: New row added to competitive map; whitespace finding verified against
   expanded set; findings updated if gap closes or a new threat reframes the landscape.
   STABILITY: Conditional
   EVIDENCE: Stable unless the new competitor directly targets the mechanism named in
   TOKEN — a competitor that reframes what users lose by switching would require TOKEN
   to be re-described.

3. **Deepen inertia analysis**
   Output effect: TOKEN block expanded with second-order effects; all `vs [TOKEN]` cells
   re-evaluated; findings re-anchored to the updated mechanism.
   STABILITY: Shifts
   EVIDENCE: TOKEN's referent updates to reflect the expanded mechanism description;
   the identifier may remain the same but the description it names changes — all consuming
   sections must propagate.
```

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-02 — Single-line verdict+evidence AMEND format (single-axis: C-16)

**Axis:** C-16 enforcement — `STABILITY: [verdict] — [evidence]` single-line format with explicit instruction that the dash-separated evidence clause is required. All other sections use the proven Token Declaration → C0 → Competitive Map → Whitespace → Findings → AMEND structure. C-17 addressed via strong naming instruction with negative examples.

**Hypothesis:** V-05-R3's two-column table is the proven C-16 mechanism, but it forces table format on AMEND. A single `STABILITY: [verdict] — [evidence]` line with explicit prohibition "a verdict without a reason does not pass" achieves the same enforcement in prose format. The dash-separated structure is lighter than a table column but more constrained than a bare `STABILITY:` tag. Tests whether C-16 evidence enforcement is format-agnostic — i.e., whether the structural requirement is about the evidence being present, not about the container format.

---

You are running **discover-competitors-alt**.

Read the repo context (README, CLAUDE.md, package.json, or equivalent) to identify the topic. Do not ask the user for the topic, competitors, or market category. Proceed immediately.

**Focus detection:** Resolve `focus:` state before producing any output.
- `focus: market` — market segment column ACTIVE.
- `focus: positioning` — positioning claim column ACTIVE.
- Not set — focus column INACTIVE.

---

### Token Declaration

**Execute before writing anything else.**

Declare a short, domain-specific token for the status-quo stickiness mechanism. The token must:
1. Be a standalone copyable identifier — it can appear verbatim in a column header, finding slot, or AMEND entry without surrounding context.
2. Encode at least one product-domain term specific to this repo — not a generic placeholder.

**Fails C-17 — generic labels:**
- `MECH`
- `INERTIA-REF`
- `LOCK`
- `HABIT` (alone, without a domain qualifier)

**Passes C-17 — domain-specific tokens:**
- `SIGNAL-LOCK` (for a signal-gathering tool)
- `WORKFLOW-GRIP` (for a workflow automation tool)
- `SHEET-HABIT` (for a spreadsheet-replacing tool)
- `CLI-INERTIA` (for a CLI-first developer tool)

A role description is not a token. "The inertia mechanism," "the stickiness factor," and "the C0 lock-in" cannot appear verbatim in a column header without interpretation — they do not qualify.

Write:

```
TOKEN: [domain-specific identifier]
```

Use this token verbatim in: the C0 block field label, the `vs [TOKEN]` column header, the third slot of every finding, and the `STABILITY:` line of every AMEND entry.

---

### C0 — Inertia Anchor

```
C0: [Actual name — not "inertia" or "incumbent"]
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
- **vs [TOKEN]**: Use the declared token as the column header. C0 row: `[ROOT]`. External rows: how does this competitor's appeal interact with the declared mechanism? Name the mechanism — not a generic relationship label.
- **Why**: For at least one external row, inline WebSearch citation (URL or publication name) in this cell. Not a footnote.

---

### Whitespace Finding

**GAP:** [specific uncontested dimension not owned by C0 or any named competitor]

Name the specific dimension. A generic statement does not pass.

If focus ACTIVE: gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Demonstrate that combining the competitive map and focus lens surfaces a gap neither alone would produce.

---

### Findings

Write 3-5 findings. Each uses this template:

> **[Competitor label or C0]** — [specific claim about behavior or capability] — *[TOKEN]: [how this finding relates to the mechanism named in Token Declaration]*

The third slot is mandatory. Do not write general domain observations — each finding must require the competitive map to support it.

---

### AMEND

Write at least 2 amendments as a numbered list. Each amendment has three required parts:

1. **[Input change]** — bold heading.
2. **Output effect:** [Specific sections that update and how].
3. **STABILITY:** [verdict] — [evidence].

The `STABILITY:` line is required for every amendment. It must include both a verdict (Stable / Shifts / Conditional) AND a dash-separated evidence clause explaining why. A verdict without a reason does not pass — "STABILITY: Stable" alone is not sufficient; "STABILITY: Stable — [reason]" is the minimum.

Example:

```
1. **Shift `focus:` from `market` to `positioning`**
   Output effect: Focus column headers and values replaced throughout the competitive map;
   whitespace finding recalculated on the positioning axis.
   STABILITY: Stable — the C0 mechanism is independent of which focus lens is active;
   rotating focus does not alter what users lose by switching away from C0.

2. **Add a named competitor**
   Output effect: New row in competitive map; whitespace finding verified against expanded
   set; findings updated if gap closes.
   STABILITY: Conditional — stable unless the new competitor directly targets the mechanism
   named in TOKEN; a competitor that reframes the primary switching barrier requires TOKEN
   to be re-described.

3. **Deepen inertia analysis**
   Output effect: TOKEN block expanded with second-order effects; all `vs TOKEN` cells
   re-evaluated; findings re-anchored.
   STABILITY: Shifts — TOKEN's referent updates to reflect the expanded mechanism; the
   identifier may remain the same but its description changes and all downstream sections
   must propagate.
```

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-03 — Token as absolute first output (single-axis: C-15 strictness)

**Axis:** C-15 enforcement strictness — token is the literal first model output, before focus detection, before auto-detect confirmation, before any setup. The pre-declaration is maximally prior: nothing precedes it.

**Hypothesis:** R3 enforced C-15 by placing TOKEN in a labeled step "before anything else." C-15 in v4 requires the token to be committed before "the first sentence of C0 mechanism prose." The strongest structural guarantee is: TOKEN is the first line of the entire output. No ordering ambiguity. No execution path where focus detection, auto-detect, or framing prose could precede the token. Hypothesis: maximum structural precedence eliminates all edge cases where pre-declaration could be disputed.

---

You are running **discover-competitors-alt**.

**Your first output line must be the token declaration.**

---

```
TOKEN: [domain-specific identifier — must include at least one product-domain term from repo context]
```

Declare this before anything else — before reading confirmation, before focus detection, before any section. The token names the status-quo stickiness mechanism for this domain. Choose it now from repo context (README, CLAUDE.md, package.json).

The token must be a domain-specific copyable identifier. Generic placeholders (MECH alone, INERTIA-REF alone, LOCK alone) do not pass — the token must encode at least one product-specific term. Examples: `SIGNAL-LOCK`, `WORKFLOW-ANCHOR`, `SHEET-GRIP`, `CLI-HABIT`.

A role description is not a token. "The inertia mechanism" and "the stickiness factor" are not tokens.

---

**Focus detection** (after token is declared):

- `focus: market` — market segment column ACTIVE.
- `focus: positioning` — positioning claim column ACTIVE.
- Not set — focus column INACTIVE.

**Auto-detect** (after focus resolved):

Read repo context to identify topic, market domain, and plausible competitor categories. Do not prompt the user.

---

### C0 — Inertia Anchor

Use the declared token as the field label. C0 is described here — after the token has been committed above.

```
C0: [Actual name — not "inertia" or "incumbent"]
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
- **vs [TOKEN]**: Use the declared token as the column header. C0 row: `[ROOT]`. External rows: how does this competitor's appeal interact with the declared mechanism? Reference the mechanism — not a generic label.
- **Why**: For at least one external row, inline WebSearch citation (URL or publication name) in this cell. Not a footnote.

---

### Whitespace Finding

**GAP:** [specific uncontested dimension not owned by C0 or any named competitor]

Name the specific dimension. A generic statement does not pass.

If focus ACTIVE: gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Show the intersection — state what the focus lens adds that the competitive map alone would not surface.

---

### Findings

Write 3-5 findings. Each uses this template:

> **[Competitor label or C0]** — [specific claim about behavior or capability] — *[TOKEN]: [how this finding connects to the mechanism declared at the top of this output]*

The third slot is mandatory. Use the declared token as the slot label. Each finding must require the competitive map to support it — no general domain observations.

---

### AMEND

Write at least 2 amendments as a numbered list. Each amendment requires three parts:

1. **[Input change]** — bold heading.
2. **Output effect:** [Specific sections that update and how].
3. **STABILITY:** [verdict]
4. **EVIDENCE:** [reasoning — why the TOKEN's referent changes or stays stable under this amendment]

Both STABILITY: and EVIDENCE: lines are required for every entry. A verdict without supporting evidence does not pass.

Example:

```
1. **Shift `focus:` dimension**
   Output effect: Focus column headers and values replaced throughout the competitive map;
   whitespace finding recalculated on the new focus axis.
   STABILITY: Stable
   EVIDENCE: The mechanism the TOKEN names belongs to C0 and does not depend on which focus
   lens is applied — rotating the focus dimension does not alter what users lose by leaving C0.

2. **Add a named competitor**
   Output effect: New row in competitive map; whitespace finding verified against expanded
   set; findings updated if gap closes.
   STABILITY: Conditional
   EVIDENCE: Stable unless the new competitor directly targets the switching barrier named in
   TOKEN — if the new competitor makes the stickiness mechanism obsolete or reframes it, TOKEN
   must be re-evaluated.

3. **Deepen inertia analysis**
   Output effect: TOKEN mechanism expanded with second-order effects; all `vs [TOKEN]` cells
   re-evaluated; findings re-anchored.
   STABILITY: Shifts
   EVIDENCE: TOKEN's referent updates — the mechanism description becomes more specific or
   multi-layered; all downstream references (column cells, finding slots) must reflect the
   revised description.
```

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-04 — Minimal combination: domain extraction + pre-declaration + two-tag evidence

**Axis:** Minimal combination of C-15, C-16, C-17. Three targeted additions to the proven R3 V-04 baseline: (1) DOMAIN-TERMS extraction micro-step for C-17, (2) pre-declared TOKEN code block for C-15, (3) STABILITY: + EVIDENCE: two-tag AMEND for C-16. No lifecycle scaffolding, no phase headers.

**Hypothesis:** R3 V-04 scored 100 on 14 criteria but would fail C-15 (partially satisfied), C-16, and C-17 under v4. The minimum sufficient prompt for all three new criteria requires exactly three additions: domain extraction forces C-17, pre-declaration forces C-15, and a second EVIDENCE: tag per AMEND entry forces C-16. Together they add minimal overhead while satisfying the complete v4 rubric. Tests whether surgical additions can achieve 9/9 aspirational without architectural changes.

---

You are running **discover-competitors-alt**.

Read the repo context (README, CLAUDE.md, package.json, or equivalent) to identify the topic. Do not prompt the user. Resolve `focus:` state before producing any output.

**Focus state:**
- `focus: market` — market segment column ACTIVE
- `focus: positioning` — positioning claim column ACTIVE
- Not set — focus column INACTIVE

---

### Token Declaration

**Execute before anything else.**

**Step 1 — Extract domain vocabulary.**

List 2-3 product-domain terms from repo context — specific names, workflow concepts, or category terms drawn from README, CLAUDE.md, or package.json.

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
```

**Step 2 — Declare domain-adaptive token.**

Choose a short, standalone token for the status-quo stickiness mechanism. The token must include at least one term from DOMAIN-TERMS — a generic placeholder alone (MECH, LOCK, INERTIA-REF) does not pass.

Valid tokens include at least one DOMAIN-TERMS term: `SIGNAL-LOCK`, `WORKFLOW-HABIT`, `TOPIC-GRIP`.

Role descriptions are not tokens: "the inertia mechanism," "the stickiness factor," "the C0 lock-in."

```
TOKEN: [domain-adaptive identifier]
```

Use this token verbatim in: the C0 block field label, the `vs [TOKEN]` column header, the third slot of every finding, and the STABILITY:/EVIDENCE: lines of every AMEND entry.

---

### C0 — Inertia Anchor

```
C0: [Actual name — not "inertia" or "incumbent"]
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
- **vs [TOKEN]**: Use the declared token as the column header. C0 row: `[ROOT]`. External rows: how does this competitor's appeal interact with the declared mechanism? Reference the mechanism — not a generic label.
- **Why**: For at least one external row, inline WebSearch citation (URL or publication name) in this cell. Not a footnote.

---

### Whitespace Finding

**GAP:** [specific uncontested dimension not owned by C0 or any named competitor]

Name the specific dimension.

If focus ACTIVE: gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Show the intersection — state what the focus lens adds that the competitive map alone would not surface.

---

### Findings

Write 3-5 findings. Each uses this template:

> **[Competitor label or C0]** — [specific claim about behavior or capability] — *[TOKEN]: [how this finding connects to the mechanism declared in Token Declaration]*

The third slot is mandatory. Use the declared token as the slot label. Each finding must require the competitive map — no general domain observations.

---

### AMEND

Write at least 2 amendments as a numbered list. Each amendment requires four parts:

1. **[Input change]** — bold heading naming what the user would change.
2. **Output effect:** [Specific sections that update and how — not just "you can adjust"].
3. **STABILITY:** [Stable | Shifts | Conditional]
4. **EVIDENCE:** [Reasoning that supports the STABILITY verdict — why the TOKEN's referent changes or stays stable. A STABILITY verdict without EVIDENCE does not pass.]

Example:

```
1. **Shift `focus:` dimension**
   Output effect: Focus column headers and values replaced throughout the competitive map;
   whitespace finding recalculated on the new axis; findings referencing the old focus
   dimension re-evaluated.
   STABILITY: Stable
   EVIDENCE: The C0 mechanism belongs to the status-quo behavior — it is independent of
   which focus lens is applied. Rotating focus does not change what users lose by leaving C0.

2. **Add a named competitor**
   Output effect: New row in competitive map; whitespace finding verified against expanded
   set; findings updated if gap closes or a new threat reframes the landscape.
   STABILITY: Conditional
   EVIDENCE: Stable unless the new competitor directly targets the switching barrier TOKEN
   names. A competitor that reframes what users lose by switching requires TOKEN to be
   re-described.

3. **Deepen inertia analysis**
   Output effect: TOKEN mechanism block expanded with second-order effects; all `vs TOKEN`
   cells re-evaluated; findings re-anchored to the updated mechanism.
   STABILITY: Shifts
   EVIDENCE: TOKEN's referent changes — the mechanism description becomes more specific;
   the identifier abbreviation may remain the same but what it names is updated. All
   consuming sections must propagate the revised description.
```

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.

---

## V-05 — Full lifecycle with deep structural enforcement of C-15 + C-16 + C-17

**Axis:** Full phase structure combined with structural enforcement of all three new criteria. ROOT phase: Step A extracts domain vocabulary, Step B pre-declares domain-adaptive token, Step C describes C0 using the declared token. AMEND: two-column stability matrix with explicit contract requiring both verdict and evidence columns populated. C-17 enforced at Step A (extraction) and Step B (domain term must appear in token). C-15 enforced by ROOT ordering (Steps A+B complete before C0 prose begins at Step C). C-16 enforced by evidence column contract.

**Hypothesis:** The fully scaffolded reference implementation for v4. Phase-based architecture makes all three new criteria structurally prior: domain terms extracted before token is named (C-17), token named before C0 prose begins (C-15), each AMEND row contracts for both verdict and evidence columns (C-16). No new criterion is enforced by instruction alone — each has a structural mechanism. Tests whether full lifecycle overhead produces more consistent model behavior than targeted minimal approaches.

---

You are running **discover-competitors-alt**.

**Auto-detect:** Read repo context (README, CLAUDE.md, package.json, or equivalent). Identify topic, market domain, and plausible competitor categories. Do not prompt the user. Proceed immediately.

**Focus resolution (pre-execution):** Resolve `focus:` state and write it as a declaration before any analysis:

```
Focus state: [ACTIVE: market | ACTIVE: positioning | INACTIVE]
```

- ACTIVE — Focus column included in Phase 2; Phase 3 gap requires cross-dimensional proof.
- INACTIVE — Focus column omitted; Phase 3 gap requires competitive proof only.

---

### ROOT — Domain Extraction + Token Pre-Declaration + Inertia Anchor

**Executes before Phase 1. Produces TOKEN and C0 block — consumed by all subsequent phases.**

**Step A: Extract domain vocabulary.**

From repo context, list 2-3 product-domain terms — specific names, workflow concepts, or category terms drawn from README, CLAUDE.md, or package.json. These are the vocabulary the token must draw from.

```
DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]
```

**Step B: Pre-declare domain-adaptive token.**

Choose a short, standalone identifier for the status-quo stickiness mechanism. The token must include at least one term from DOMAIN-TERMS. A generic placeholder alone (MECH, LOCK, INERTIA-REF) fails C-17 — the token must encode product context.

Valid structure: `[DOMAIN-TERM]-[STICKINESS-CATEGORY]` — e.g., `SIGNAL-LOCK`, `WORKFLOW-HABIT`, `TOPIC-GRIP`.

A role description is not a token. "The inertia mechanism" and "the stickiness factor" cannot appear verbatim in a column header without interpretation.

Write:

```
TOKEN: [domain-adaptive identifier]
```

**Token is committed. C0 description begins in Step C — not before.**

**Step C: Name C0 and describe the mechanism.**

Name the status-quo behavior or tool (not "inertia" or "incumbent"). Assign threat level. Describe the stickiness mechanism — one of: switching cost, habit lock-in, workaround satisfaction — tied to a specific behavior or capability C0 does or provides. Use the Step B token as the field label.

```
C0: [Actual name]
Threat: [HIGH / MEDIUM / LOW]
[TOKEN]: [mechanism type]: [specific description tied to C0's behavior]
```

If focus is ACTIVE:
```
[TOKEN] Focus: [market segment C0 occupies] OR [positioning claim C0 holds]
```

ROOT complete when: DOMAIN-TERMS listed; TOKEN is domain-adaptive and includes at least one DOMAIN-TERMS term; TOKEN declared before Step C begins; C0 named specifically; mechanism type declared with specific description.

---

### Phase 1 — Topic & Scope

**Consumes:** repo context.
**Produces:** topic declaration — consumed by Phase 2 (competitor identification boundary).

Write:
- Market domain
- Primary user persona
- Decision context: what is the user choosing between?

---

### Phase 2 — Competitive Map

**Consumes:** Phase 1 topic declaration, ROOT TOKEN, focus state.
**Produces:** competitor table — consumed by Phase 3, Phase 4, AMEND.

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
- **vs [TOKEN]**: Use ROOT token as column header. How does this competitor's appeal interact with the ROOT mechanism? Reference the mechanism description — not a generic label.
- Focus column: populated for every row if focus ACTIVE.
- Source: for at least one external row, inline WebSearch citation in this cell. Not a footnote.

Phase 2 complete when: C0 at row 0, >= 3 external rows, every row has threat level, citation present, every `vs [TOKEN]` cell references ROOT mechanism.

---

### Phase 3 — Whitespace

**Consumes:** Phase 2 competitor table, ROOT TOKEN (for gap rationale), focus state.
**Produces:** labeled GAP finding — consumed by Phase 4.

Write:

**GAP:** [specific dimension not owned by C0 or any Phase 2 competitor]

If focus INACTIVE: state why the ROOT mechanism does not cover this gap.

If focus ACTIVE: gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Show intersection — name what the focus lens adds that the competitive map alone would not surface. Confirm that the ROOT mechanism does not cover this gap either.

---

### Phase 4 — Findings

**Consumes:** Phase 2 competitor table, Phase 3 GAP, ROOT TOKEN.
**Produces:** findings — consumed by output artifact.

Write 3-5 findings. Each uses this template:

> **[Competitor label or C0 from Phase 2]** — [specific claim] — *[TOKEN]: [connection to the ROOT mechanism]*

Rules:
- Third slot is mandatory — use the ROOT token as the slot label.
- Findings that could be written without Phase 2 fail the grounding test.
- Findings that do not fill the TOKEN slot fail the propagation test.

---

### AMEND — Stability Matrix

**Consumes:** all phases.
**Produces:** stability matrix with input-to-output pairs, per-entry stability verdicts, and per-entry supporting evidence.

Output contract: for every row, all four columns are required — (1) input change, (2) output effect across affected phases, (3) stability verdict (Stable / Shifts / Conditional), and (4) evidence supporting the verdict. A row with a verdict but no evidence does not satisfy the output contract. A row with evidence but no verdict does not satisfy the output contract. "Stable" without reasoning does not satisfy the Evidence column.

| # | Input change | Output effect | [TOKEN] verdict | Evidence |
|---|--------------|---------------|-----------------|----------|
| 1 | Shift `focus:` dimension | Phase 2 focus column headers and values replaced; Phase 3 GAP recalculated on new axis; Phase 4 findings referencing old focus re-evaluated | Stable | The C0 mechanism belongs to the status-quo behavior — it is independent of which focus lens is applied. Rotating focus does not alter what users lose by switching away from C0. |
| 2 | Add a named competitor | Phase 1 scope boundary may update; Phase 2 repopulated with new row; Phase 3 GAP verified against expanded set; Phase 4 updated if gap closes | Conditional | Stable unless the new competitor directly targets the switching barrier TOKEN names. A competitor that reframes the primary stickiness mechanism requires ROOT Step C to be revised. |
| 3 | Narrow competitor set to a specific tier | Phase 1 scope boundary updates; Phase 2 repopulated within narrowed scope; Phase 3 GAP rechecked | Conditional | If narrowing reframes the decision context, ROOT mechanism may need revision — verify whether C0 still holds the dominant position in the narrowed scope before declaring TOKEN stable. |
| 4 | Deepen inertia analysis | ROOT Step C expanded with second-order effects; Phase 2 `vs [TOKEN]` column re-evaluated; Phase 4 findings re-anchored | Shifts | TOKEN's referent updates — the mechanism description becomes more specific or multi-layered. The identifier abbreviation may remain the same but what it names changes; all consuming phases must propagate. |

Minimum 2 rows. Both `[TOKEN] verdict` AND `Evidence` columns are required for every row. A stability answer without reasoning does not satisfy the Evidence column requirement.

---

### Output

Write artifact to `simulations/discover/competitors/{topic}-competitors-alt-{date}.md`.
