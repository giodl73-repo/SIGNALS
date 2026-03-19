5 complete variations written to `simulations/quest/variations/discover-competitors-alt-variations-R5-2026-03-17.md`.

---

## discover-competitors-alt — Variations R5

**Baseline:** R4 (140/140). New rubric v4 adds C-19–C-22. Every variation incorporates all four new structural patterns.

| Variation | Axis | Projected | Key test |
|-----------|------|----------:|----------|
| **V-01** | Role sequence — INERTIA-REF in Phase 0, before context is read | ~160 | Does establishing INERTIA-REF as the first act satisfy C-22 more naturally without a bolted-on per-finding rule? |
| **V-02** | Output format — tabular findings with structural coercion on both Anchor and INERTIA-REF-DELTA columns | ~157.5 | Does C-20 applied twice (competitor table + findings table) satisfy C-22 via form rather than instruction? |
| **V-03** | Lifecycle emphasis — all four gate sections (CITATION, ANCHOR, PROOF, INERTIA-REF) declared in PREFLIGHT before Phase 1 | ~160 | Can four PASS/FAIL tables coexist cleanly with a separate OUTPUT CONTRACTS block? |
| **V-04** | Combined: OUTPUT CONTRACT table + INERTIA-REF definition both before Phase 1 | ~160 | Does front-loading both the output shape and the reference frame produce a coherent preamble or a cluttered header? |
| **V-05** | Combined: C-20 in both tables + three named gate sections (CITATION, ANCHOR-COMPETITORS, ANCHOR-FINDINGS + PROOF) | ~160 | Can maximum structural density remain readable? |

**Key structural differences:**

- **C-19** (synthesis-first output contracts): V-01/V-03/V-04 use a dedicated OUTPUT CONTRACTS block; V-02/V-05 embed the contract as a note at the top of the collection phase. All name at least one output slot by label before collection ends.
- **C-20** (structural column coercion): V-01/V-03/V-04 apply format template to competitor table Anchor column only; V-02/V-05 apply it to both the competitor table Anchor column and the findings table Anchor column.
- **C-21** (gate-as-section with PASS/FAIL table): V-01/V-04 have one named gate section (CITATION GATE); V-02 has one (CITATION GATE); V-03 has four (PREFLIGHT block); V-05 has three (CITATION GATE, ANCHOR GATE — COMPETITOR TABLE, PROOF GATE + ANCHOR GATE — FINDINGS TABLE).
- **C-22** (INERTIA-REF per-finding citation): V-01/V-03/V-04/V-05 use instructional per-finding citation requirement; V-02 coerces via INERTIA-REF-DELTA column shape.

**V-02 uncertainty:** C-22 requires the token be "defined once" with "per-finding citation required by name." The column format constraint in V-02 structurally enforces the requirement — the token name appears in the column header template. PASS expected but indirect.
F-DELTA is a structural column in the findings table — the token is required by column shape, not by a standalone instruction. Rubric requires the token to be "defined once" with "per-finding citation required by name." Column-shape coercion satisfies the per-finding requirement; the definition still appears in Phase 2. PASS expected, but the indirect mechanism is the only uncertainty.

**Key structural decisions by variation:**

- **V-01:** INERTIA-REF defined in PHASE 0 before context is read. OUTPUT CONTRACTS block between Phase 0 and Phase 1. Focus dimension measured against INERTIA-REF from the moment it is introduced. Per-finding citation instructional.
- **V-02:** Findings are a structured table with two coerced columns — Anchor (`Row C{N}, {attribute}: "{value}"`) and INERTIA-REF-DELTA (`vs. INERTIA-REF — {verdict}: {phrase}`). Both columns are syntactically malformed without attribute-level values. CITATION GATE is the named section. OUTPUT CONTRACT note embedded in Phase 3 collection instruction.
- **V-03:** Four named gate sections (CITATION GATE, ANCHOR GATE, PROOF GATE, INERTIA-REF GATE) with PASS/FAIL tables in a PREFLIGHT block before Phase 1. Phases are concise execution instructions that reference gates by name. OUTPUT CONTRACTS before Phase 2.
- **V-04:** OUTPUT CONTRACT table appears before Phase 1; INERTIA-REF definition immediately after. Both preamble elements visible before any collection begins. Phases execute against the pre-declared contracts. CITATION GATE is the named section.
- **V-05:** C-20 applied to both competitor table Anchor column and findings table Anchor column. C-21 via three named gate sections — CITATION GATE, ANCHOR GATE (competitor table), PROOF GATE (findings). INERTIA-REF-DELTA also coerced via findings table column shape (C-22 via C-20). Most structurally dense variation.

---

## V-01 — Role sequence (inertia-first anchor)

**Axis:** Role sequence — INERTIA-REF established in Phase 0 before any context is read, before any external competitor is assessed, before the focus dimension is introduced.

**Hypothesis:** Establishing INERTIA-REF as the opening act makes every downstream instruction naturally reference it, satisfying C-22 without needing a separate per-finding citation rule bolted onto Phase 5. The gravitational center is declared before the universe is populated.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

### PHASE 0: ESTABLISH INERTIA-REF

Before reading any repository context, before assessing any external competitor, define the reference frame.

Identify the status quo — the behavior, tool, or approach the target user relies on today without the feature under analysis. This is **C0**: the inertia competitor.

Define the token:

```
INERTIA-REF = [C0 name]: [specific mechanism — name the switching cost, habit lock-in, or
workaround satisfaction that makes C0 sticky; the mechanism must be specific to C0's behavior
or product feature, not a category label applied generically]
```

**Inertia naming failure:** INERTIA-REF sentence uses a category label ("inertia is high," "users are accustomed to it," "strong lock-in") rather than a specific mechanism. Rewrite before continuing.

Every finding in Phase 5 must cite **INERTIA-REF** by token name and declare whether the finding reinforces, challenges, or contextualizes the mechanism named in this token.

---

### OUTPUT CONTRACTS

Before collecting any external competitor data, note what Phases 4 and 5 require from Phases 2–3. Collect data that fills each of these slots by name:

- **WHITESPACE absence evidence**: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per row per candidate whitespace attribute. Absence must be observed per row during Phase 2 — you cannot backfill this at synthesis time.
- **ANCHOR cell value**: `Row C{N}, {attribute}: "{value}"` per finding. Collect mechanism phrases, threat scores, and focus-column values per competitor row during Phase 2.
- **INERTIA-REF-DELTA phrase**: For each finding, identify the specific C0 mechanism phrase from INERTIA-REF that the finding contrasts with. Identify this during Phase 2 by noting where each external competitor's mechanism departs from or resembles the C0 mechanism.

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE

Run WebSearch for each external competitor before adding its row. C0 (INERTIA-REF) enters as Row C0 with all columns populated.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column format:** `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten before the row is output.

ACCEPTABLE: `Row C2, mechanism: "requires browser tab open for all review sessions"`
NOT ACCEPTABLE: `Competitor 2 — mechanism is high` — no quoted value, no `Row C{N}` prefix

**CITATION GATE**

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch appears in the Citation column of this row | **Citation gate failure** — suppress the row; run WebSearch and fill before outputting |
| Citation location | Citation is within the table row, not in a trailing footnote or reference block | **Citation gate failure** — relocate the citation into the row or remove the footnote |

---

### PHASE 3: WHITESPACE (fills WHITESPACE absence evidence slot — see OUTPUT CONTRACTS)

For each candidate whitespace attribute, record across all rows:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm the gap:

```
Gap confirmed: No row provides a non-absent value for [{attribute column(s)}] —
attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism from Phase 0}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion, no attribute-level evidence — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING

```
SOURCE: {name the specific cell value — row label, attribute name, and quoted value —
do not proceed to REDUCTION-1 until this slot is filled}

REDUCTION-1: Competitive map alone — does the gap appear without the focus dimension?
[YES/NO + one sentence showing what is lost when focus is dropped]

REDUCTION-2: Focus dimension alone — does the gap appear without the competitive map?
[YES/NO + one sentence showing what is lost when the map is dropped]

If either reduction cannot honestly answer NO, find a different gap. A gap that does not
fail both single-dimension reductions is not cross-dimensional — proceeding is a
**proof structure failure**.

THEREFORE: {one sentence — the gap that requires both dimensions simultaneously}
```

---

### PHASE 5: FINDINGS

Write 2–5 findings. Each finding must satisfy all three requirements:

1. **ANCHOR**: Cite a specific cell value from the competitor table: `Row C{N}, {attribute}: "{value}"`
   - NOT ACCEPTABLE: "Competitor 2 reveals that..." — name-only anchoring — **anchor gate failure**
   - NOT ACCEPTABLE: "As Competitor 1 demonstrates..." — name-only anchoring — **anchor gate failure**

2. **INERTIA-REF-DELTA**: Cite INERTIA-REF by token name:
   `vs. INERTIA-REF — [reinforces / challenges / contextualizes]: {specific C0 mechanism phrase from Phase 0}`
   A finding that does not cite INERTIA-REF by name is an **inertia citation failure** — add the comparison clause before outputting.

3. **Cross-dimensional finding**: Must include SOURCE, REDUCTION-1, REDUCTION-2, THEREFORE as structured in Phase 4.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Then: replace the SOURCE slot with the new evidentiary anchor, rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus dimension, reconstruct the THEREFORE clause. Writing only a new conclusion without rerunning both reductions is a **proof rerun failure** — the reconstruction of both single-dimension reduction arguments is what makes the proof valid, not the conclusion.

2. **Add a competitor**: Insert a new row into the competitor table after running WebSearch. Check the CITATION GATE. Recheck WHITESPACE absence evidence for all candidate attribute columns — a new row may change the vacancy status.

3. **Deepen INERTIA-REF mechanism**: Replace the INERTIA-REF mechanism sentence with a more specific phrasing — name a particular product feature, workflow step, or workaround behavior rather than a category. Update all INERTIA-REF-DELTA comparison clauses in Phase 5 findings that referenced the old mechanism phrase.

---

## V-02 — Output format (tabular findings with structural column coercion)

**Axis:** Output format — findings are produced as structured table rows, not prose paragraphs. Both the Anchor column and the INERTIA-REF-DELTA column use format templates that make name-only or empty entries syntactically non-conforming without requiring rule evaluation.

**Hypothesis:** Applying structural column coercion (C-20) to both the Anchor and the INERTIA-REF-DELTA column in the findings table satisfies C-13 and C-22 through form rather than instruction — the most adversarially robust mechanism for both criteria simultaneously.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set, the focus dimension is active. If not supplied, no focus column is added.

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: INERTIA ASSESSMENT

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Define:

```
INERTIA-REF = [C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround
satisfaction; specific to C0's product behavior or feature, not a generic category label]
```

**Inertia naming failure:** Mechanism sentence uses a category label. Rewrite before continuing.

C0 enters the competitor table as Row C0 with all columns populated, including Citation (URL or primary source).

---

### PHASE 3: COMPETITOR TABLE

**OUTPUT CONTRACT — collect during this phase:** The Phase 6 findings table requires (a) an Anchor cell value in `Row C{N}, {attribute}: "{value}"` format per finding, (b) an INERTIA-REF-DELTA cell value in `vs. INERTIA-REF — {verdict}: {phrase}` format per finding, and (c) a URL citation per external row. Collect mechanism phrases, focus-column values, and citation URLs now — they cannot be synthesized at Phase 6 time.

Run WebSearch per external competitor.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column format:** `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten before the row is output.

**CITATION GATE — NAMED SECTION**

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch first |
| Citation in row, not footnote | Citation within the table row, not a trailing reference block | **Citation gate failure** — relocate into the row |

---

### PHASE 4: WHITESPACE

For each candidate whitespace attribute, record per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Absence evidence: Row C{N} — {attribute}: {absent value}  (one line per row)
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 5: CROSS-DIMENSIONAL FINDING

```
SOURCE: {named cell — row label, attribute name, quoted value — declare before any reduction
argument; do not proceed to REDUCTION-1 until this slot is filled}

REDUCTION-1: Competitive map alone — does the gap appear without the focus dimension?
[YES/NO + one sentence showing what is lost]

REDUCTION-2: Focus dimension alone — does the gap appear without the competitive map?
[YES/NO + one sentence showing what is lost]

If either answers YES, find a different gap. Proceeding is a **proof structure failure**.

THEREFORE: {one sentence requiring both dimensions simultaneously}
```

---

### PHASE 6: FINDINGS TABLE

All findings are rows in the following table:

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Column format constraints (structural — entries not matching these shapes are syntactically malformed and must be rewritten before outputting the row):**

- **Anchor**: `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is malformed
  - NOT ACCEPTABLE: "Competitor 2 reveals that..." — name-only — **anchor gate failure**
  - NOT ACCEPTABLE: "As Competitor 1 demonstrates..." — name-only — **anchor gate failure**
  - ACCEPTABLE: `Row C3, focus-column: "no enterprise tier pricing visible on public page"`

- **INERTIA-REF-DELTA**: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — a cell with only "N/A" or a competitor name is malformed; every finding row must carry a comparison against INERTIA-REF

For the cross-dimensional finding row, the Claim cell contains the THEREFORE sentence. An adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot with new evidence; rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus; reconstruct THEREFORE. Writing only a new THEREFORE clause without rerunning both reductions is a **proof rerun failure**.

2. **Add competitor**: Insert a new row after WebSearch. Apply CITATION GATE. Verify the new row's Anchor cell conforms to column format. Update WHITESPACE absence evidence for all candidate attributes.

3. **Refine INERTIA-REF mechanism**: Replace the INERTIA-REF mechanism sentence with more specific phrasing. Rewrite all INERTIA-REF-DELTA cells in the findings table whose mechanism phrase references the old wording — the column format constraint applies to updated cells.

---

## V-03 — Lifecycle emphasis (preflight gate architecture)

**Axis:** Lifecycle emphasis — all gates are declared upfront as named sections with PASS/FAIL tables in a PREFLIGHT block before Phase 1 begins. Phases are concise execution instructions that reference gates by name.

**Hypothesis:** Declaring all four gates at the top of the skill before any collection begins produces the clearest separation between rules (PREFLIGHT) and execution (Phases). C-21 is maximally expressed (four named gate sections). C-19 is satisfied by an OUTPUT CONTRACTS block between PREFLIGHT and Phase 1.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set, the focus dimension is active. If not, no focus column is added.

---

## PREFLIGHT: GATE DEFINITIONS

The following gates apply throughout execution. Each is a named checkpoint. Phase instructions reference gates by name — apply the gate when directed.

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in the Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in trailing reference block | **Citation gate failure** — move citation into the row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite the cell before outputting |
| Whitespace absence anchor | Row-by-row absence evidence present: `Row C{N} — {attribute}: {absent}` per row | **Whitespace gate failure** — do not output WHITESPACE finding without attribute-level evidence |

NOT ACCEPTABLE: "Competitor 2 reveals that..." — name-only — **anchor gate failure**
NOT ACCEPTABLE: "As Competitor 1 demonstrates..." — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "embeds review comments into PR threads, locking workflow to GitHub UI"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value (row, attribute, quoted value) appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must be declared before any reduction argument is written |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence | **Proof structure failure** — both reductions required; one reduction does not establish cross-dimensionality |
| Both reductions answer NO | Neither single-dimension reduction alone produces the gap | **Proof structure failure** — if either answers YES, find a different gap before outputting THEREFORE |

---

### GATE 4: INERTIA-REF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| INERTIA-REF mechanism specific | Token names a switching cost, habit lock-in, or workaround satisfaction specific to C0's behavior or product feature | **Inertia naming failure** — category label is not a mechanism; rewrite INERTIA-REF before continuing |
| Per-finding citation | Each finding cites INERTIA-REF by token name with reinforces/challenges/contextualizes verdict and specific C0 mechanism phrase | **Inertia citation failure** — add the `vs. INERTIA-REF — {verdict}: {phrase}` clause before outputting the finding |

---

## OUTPUT CONTRACTS

Before collecting external competitor data, note what synthesis phases require. Phases 2–3 must gather data that fills these slots by name:

- **WHITESPACE absence evidence** (required by Phase 4): `Row C{N} — {attribute}: {absent}` per row per candidate attribute. Apply GATE 2 (whitespace absence anchor) at Phase 4.
- **ANCHOR cell value** (required by Phase 5): `Row C{N}, {attribute}: "{value}"` per finding. Collect mechanism phrases, threat scores, and focus-column values during Phase 2.
- **INERTIA-REF-DELTA phrase** (required by Phase 5 per GATE 4): Specific C0 mechanism phrase that each finding compares against. Identify contrasts during Phase 2.

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: INERTIA ASSESSMENT

Identify C0. Define INERTIA-REF. Apply GATE 4 (mechanism check) before continuing.

```
INERTIA-REF = [C0 name]: [specific mechanism]
```

C0 enters the competitor table as Row C0.

---

### PHASE 3: COMPETITOR TABLE

Run WebSearch per external competitor. Apply GATE 1 (CITATION GATE) per row before outputting. Apply GATE 2 (Anchor cell format) per row.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

Anchor column format: `Row C{N}, {attribute}: "{value}"` — syntactically malformed cells trigger GATE 2 before rule evaluation.

---

### PHASE 4: WHITESPACE

Apply GATE 2 (whitespace absence anchor — see OUTPUT CONTRACTS).

```
Absence evidence: Row C{N} — {attribute}: {absent value}  (one line per row per attribute)
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism}
```

---

### PHASE 5: CROSS-DIMENSIONAL FINDING

Apply GATE 3 (PROOF GATE).

```
SOURCE: {named cell — row, attribute, quoted value — fill before any reduction argument}

REDUCTION-1: Map alone — gap absent without focus? [YES/NO + one sentence showing what is lost]
REDUCTION-2: Focus alone — gap absent without map? [YES/NO + one sentence showing what is lost]

THEREFORE: {one sentence requiring both dimensions simultaneously}
```

---

### PHASE 6: FINDINGS

Write 2–5 findings. Apply GATE 2 (Anchor cell format) and GATE 4 (per-finding INERTIA-REF citation) to each finding before outputting.

Each finding:
1. **ANCHOR**: `Row C{N}, {attribute}: "{value}"` — apply GATE 2
2. **INERTIA-REF-DELTA**: `vs. INERTIA-REF — [reinforces / challenges / contextualizes]: {specific C0 mechanism phrase}` — apply GATE 4

Cross-dimensional finding also requires SOURCE / REDUCTION-1 / REDUCTION-2 / THEREFORE — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace SOURCE slot with new evidence. Rewrite REDUCTION-1 and REDUCTION-2 from scratch. Reconstruct THEREFORE. Apply GATE 3. "Update the finding" without rerunning both reductions is a **proof rerun failure**.

2. **Add competitor**: Add row after WebSearch. Apply GATE 1. Update WHITESPACE absence evidence — apply GATE 2 (whitespace absence anchor) for all candidate attributes.

3. **Refine INERTIA-REF mechanism**: Replace the mechanism sentence with more specific phrasing. Apply GATE 4 to all findings — update INERTIA-REF-DELTA comparisons referencing the old mechanism phrase.

---

## V-04 — Combined: synthesis-first output contracts + inertia-gravity center

**Axes combined:** Role sequence (OUTPUT CONTRACT before Phase 1) + inertia framing (INERTIA-REF defined immediately after OUTPUT CONTRACT, before context is read).

**Hypothesis:** Placing both the OUTPUT CONTRACT table and the INERTIA-REF definition before Phase 1 creates the strongest synthesis-first preamble: the full output shape (C-19) and the gravitational reference frame (C-22) are both visible before any collection begins. Phases execute against pre-declared contracts rather than re-specifying them.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set, the focus dimension is active. If not, no focus column is added.

---

## OUTPUT CONTRACT

Before any data collection, this skill commits to the following output slots. Every collection phase fills named slots declared here.

| Slot | Label | Required format |
|------|-------|-----------------|
| Inertia anchor | INERTIA-REF | `[C0 name]: [specific mechanism]` |
| Competitor row anchor | Anchor column (per external row) | `Row C{N}, {attribute}: "{value}"` |
| Whitespace absence evidence | Absence evidence block (Phase 3) | `Row C{N} — {attribute}: {absent}` per row |
| Cross-dimensional source | SOURCE slot (Phase 4) | Named cell: row, attribute, quoted value |
| Per-finding inertia comparison | INERTIA-REF-DELTA (Phase 5, per finding) | `vs. INERTIA-REF — {verdict}: {mechanism phrase}` |

Arriving at synthesis without the required slot data for any row or finding constitutes a **collection gate failure** — return to the relevant phase and fill the slot before continuing.

---

## INERTIA-REF DEFINITION

Before reading any repo context, identify the status quo competitor (C0) and define the reference frame:

```
INERTIA-REF = [C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround
satisfaction that is specific to C0's behavior or product feature; not a category label]
```

**Inertia naming failure:** Mechanism sentence applies a category label ("high inertia," "strong familiarity"). Rewrite before continuing.

Every finding in Phase 5 must cite INERTIA-REF by token name and state whether the finding reinforces, challenges, or contextualizes the mechanism in this token.

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE

Run WebSearch per external competitor. C0 is Row C0 (INERTIA-REF defined above).

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column format (OUTPUT CONTRACT — Anchor slot):** `Row C{N}, {attribute}: "{value}"` — cells containing only a competitor name are syntactically malformed; rewrite before outputting.

**CITATION GATE**

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation present | URL from WebSearch in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch first |
| Citation in row, not footnote | URL is within the table row | **Citation gate failure** — relocate into row |

---

### PHASE 3: WHITESPACE (fills Absence evidence slot — OUTPUT CONTRACT)

For each candidate whitespace attribute, record across all rows:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — OUTPUT CONTRACT)

```
SOURCE: {named cell — row label, attribute name, quoted value — declared first, before any
reduction argument; do not proceed to REDUCTION-1 until this slot is filled}

REDUCTION-1: Map alone — gap absent without focus? [YES/NO + one sentence showing what is lost]

REDUCTION-2: Focus alone — gap absent without map? [YES/NO + one sentence showing what is lost]

If either answers YES, find a different gap. A gap that does not fail both single-dimension
reductions is not cross-dimensional — proceeding is a **proof structure failure**.

THEREFORE: {one sentence requiring both dimensions simultaneously}
```

---

### PHASE 5: FINDINGS (fills Anchor and INERTIA-REF-DELTA slots — OUTPUT CONTRACT)

Write 2–5 findings. Each must fill both named slots from the OUTPUT CONTRACT:

1. **ANCHOR** (`Row C{N}, {attribute}: "{value}"`)
   - NOT ACCEPTABLE: "Competitor 2 reveals that..." — name-only — **anchor gate failure**
   - NOT ACCEPTABLE: "As Competitor 1 demonstrates..." — name-only — **anchor gate failure**

2. **INERTIA-REF-DELTA** (`vs. INERTIA-REF — [reinforces / challenges / contextualizes]: {specific C0 mechanism phrase}`)
   — A finding missing this clause is an **inertia citation failure** — add the comparison before outputting.

3. Cross-dimensional finding: SOURCE / REDUCTION-1 / REDUCTION-2 / THEREFORE as structured in Phase 4.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot (OUTPUT CONTRACT — SOURCE slot) with the new evidentiary anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus. Reconstruct THEREFORE. Writing only a new conclusion without rerunning both reductions is a **proof rerun failure** — the OUTPUT CONTRACT SOURCE slot must be refilled with updated evidence before either reduction is reconstructed.

2. **Add competitor**: Insert a new row after WebSearch. Check CITATION GATE. Fill the Anchor slot for the new row per OUTPUT CONTRACT format. Update Phase 3 WHITESPACE absence evidence — recheck all candidate attribute columns.

3. **Narrow INERTIA-REF mechanism**: Replace the INERTIA-REF mechanism sentence (OUTPUT CONTRACT — INERTIA-REF slot) with more specific phrasing. Update all INERTIA-REF-DELTA clauses in Phase 5 that reference the old mechanism phrase — each clause must reflect the current INERTIA-REF definition.

---

## V-05 — Combined: structural coercion maximized + gate architecture maximized

**Axes combined:** Output format (C-20 applied to competitor table Anchor AND findings table Anchor columns) + lifecycle emphasis (C-21 via three named gate sections — CITATION GATE, ANCHOR GATE, PROOF GATE).

**Hypothesis:** Applying structural column coercion to both tables and declaring three separate PASS/FAIL gate sections produces the most adversarially robust skill structure in R5 — form coerces compliance in two independent locations while gates make every failure state a checkable item. The test is whether this density remains readable.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set, the focus dimension is active. If not, no focus column is added.

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: INERTIA ASSESSMENT

Identify C0. Define:

```
INERTIA-REF = [C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround
satisfaction; name the C0 product feature or behavior specifically, not a category label]
```

**Inertia naming failure:** Mechanism is a category label. Rewrite before continuing.

INERTIA-REF is a required citation in every finding in Phase 6. C0 enters the competitor table as Row C0.

---

### PHASE 3: COMPETITOR TABLE

**OUTPUT CONTRACT — collect during this phase:** Phase 6 requires (a) Anchor cell values in `Row C{N}, {attribute}: "{value}"` format, (b) INERTIA-REF-DELTA phrases contrasting each competitor against the C0 mechanism, and (c) URL citations per external row. Collect mechanism phrases, focus-column values, and citation URLs now — they cannot be synthesized at Phase 6 time.

Run WebSearch per external competitor.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column format (structural):** `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten before the row is output.

**CITATION GATE**

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch first |
| Citation in row | URL is inline in the table row, not trailing footnote | **Citation gate failure** — relocate into row |
| URL not prose reference | Cell contains a URL, not "official site" or bare domain name | **Citation gate failure** — replace with direct URL from WebSearch |

**ANCHOR GATE — COMPETITOR TABLE**

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format conforms | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite before outputting |
| Attribute explicitly named | Anchor cell names the attribute type (threat, mechanism, focus column, etc.) | **Anchor gate failure** — attribute type must be present |

NOT ACCEPTABLE: `Competitor 2 — mechanism present` — no quoted value, no `Row C{N}` — **anchor gate failure**
NOT ACCEPTABLE: `Competitor 3` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "enforces daily standup via calendar lock, not async option"`

---

### PHASE 4: WHITESPACE

For each candidate whitespace attribute, record per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Absence evidence: Row C{N} — {attribute}: {absent value}  (one line per row)
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 5: CROSS-DIMENSIONAL FINDING

**PROOF GATE**

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must precede all reduction arguments |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence showing what is lost | **Proof structure failure** — both reductions required; one reduction does not establish cross-dimensionality |
| Both reductions answer NO | Neither single-dimension reduction alone produces the gap | **Proof structure failure** — if either answers YES, find a different gap |

```
SOURCE: {named cell — row label, attribute name, quoted value — declare before any reduction}

REDUCTION-1: Map alone — gap absent without focus? [YES/NO + one sentence showing what is lost]
REDUCTION-2: Focus alone — gap absent without map? [YES/NO + one sentence showing what is lost]

THEREFORE: {one sentence requiring both dimensions simultaneously}
```

---

### PHASE 6: FINDINGS TABLE

All findings are rows in the following table:

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Column format constraints (structural — entries not matching these shapes are syntactically malformed and must be rewritten before outputting the row):**

- **Anchor**: `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is malformed
- **INERTIA-REF-DELTA**: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — "N/A" or empty is malformed; every finding must compare against INERTIA-REF by token name

**ANCHOR GATE — FINDINGS TABLE**

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format conforms | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, quoted value all present | **Anchor gate failure** — rewrite before outputting the row |
| INERTIA-REF-DELTA format conforms | `vs. INERTIA-REF — {verdict}: {phrase}` — verdict word and C0 mechanism phrase both present | **Inertia citation failure** — add the clause before outputting the row |

NOT ACCEPTABLE (Anchor): "Competitor 2 reveals that..." — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): "As Competitor 1 demonstrates..." — name-only — **anchor gate failure**
NOT ACCEPTABLE (INERTIA-REF-DELTA): "N/A" or empty — **inertia citation failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier — enterprise-only positioning"`
ACCEPTABLE (INERTIA-REF-DELTA): `vs. INERTIA-REF — challenges: C0 uses spreadsheet lock-in; C3 uses enterprise contract lock-in instead`

For the cross-dimensional finding row, the Claim cell contains the THEREFORE sentence. An adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply PROOF GATE.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot with new evidence; rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus; reconstruct THEREFORE. Apply PROOF GATE to the rebuilt block. Writing only a new THEREFORE clause without rerunning both reductions is a **proof rerun failure** — the reconstruction of both single-dimension reduction arguments is what makes the proof valid, not the conclusion.

2. **Add competitor**: Insert a new row after WebSearch. Apply CITATION GATE and ANCHOR GATE — COMPETITOR TABLE to the new row. Update WHITESPACE absence evidence for all candidate attributes.

3. **Refine INERTIA-REF mechanism**: Replace the INERTIA-REF mechanism sentence with more specific phrasing — name a product feature or workaround behavior rather than a category. Rewrite all INERTIA-REF-DELTA cells in the findings table whose mechanism phrase references the old wording. Apply ANCHOR GATE — FINDINGS TABLE to the updated cells.
