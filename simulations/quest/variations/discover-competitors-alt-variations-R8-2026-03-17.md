Written to `simulations/quest/variations/discover-competitors-alt-variations-R8-2026-03-17.md`.

---

## discover-competitors-alt — R8 Variations Summary

All five variations target 215/215 on rubric v7 (C-01 through C-33). C-31, C-32, C-33 are satisfied as a universal baseline across all variations.

| Variation | Axis | Key structural innovation |
|-----------|------|--------------------------|
| **V-01** | Inertia framing | "Required by" column in OUTPUT CONTRACTS — INERTIA-REF is the root slot (slot 1); slots 5 and 6 name their upstream dependency explicitly in the contract table |
| **V-02** | Output format | Focus-scope evidence (C-33) gets a full C-23-compliant format template: `REDUCTION-1 NO: [...] | REDUCTION-2 NO: [...] | THEREFORE: [...]` — proof structure is contract-declared before Phase 4 runs |
| **V-03** | Lifecycle emphasis | Phase 4 proof block restructured as a 4-row PASS/FAIL table (SOURCE, REDUCTION-1, REDUCTION-2, THEREFORE) — each row has a required value format and a named failure state; output-verifiable at the phase level |
| **V-04** | Inertia framing + Lifecycle emphasis | "Required by" column (V-01) + Phase 4 proof table (V-03); GATE 4 write row names slot 1 by number, label, and dependent slots |
| **V-05** | Combined maximum | All three + AMEND explicitly requires slot 5 refill on focus shift + GATE 3 NOT ACCEPTABLE examples close the retroactive reduction construction escape |

**C-31 through C-33 universal baseline:**
- C-31: GATE 4 has a dedicated write-token table row with "Inertia write failure" in all 5
- C-32: OUTPUT CONTRACTS is the first subsection in PREFLIGHT in all 5 — before GATE 1, 2, 3, 4
- C-33: 6-slot contract table includes "Focus-scope evidence" / "Cross-dimensional proof" row in all 5

**New variation axes vs R7:** R7 introduced C-31/C-32/C-33 patterns as isolated innovations. R8 builds on them — V-01 adds dependency provenance to the contract table; V-02 applies C-23's format-specification standard to the new C-33 slot specifically; V-03 restructures Phase 4 as a machine-checkable output table rather than a code-block instruction; V-04 and V-05 combine these to test maximum bidirectional enforcement.
-scope evidence" row; format varies: proof block description (V-01/V-03/V-04), full template (V-02/V-05) |

**Single-axis variations (V-01, V-02, V-03):** Each explores one structural degree of freedom — dependency chain visibility (V-01), slot format specification for the C-33 slot (V-02), proof block output shape (V-03) — while holding all other variables at the C-31/C-32/C-33 baseline.

**Combined variations (V-04, V-05):** V-04 combines derivation chain visibility with the structured proof table. V-05 combines all three axes plus extended enforcement in AMEND and GATE 3.

| | **V-01** | **V-02** | **V-03** | **V-04** | **V-05** |
|---|---|---|---|---|---|
| **C-32** (OUTPUT CONTRACTS first) | First subsection | First subsection | First subsection | First subsection | First subsection |
| **C-31** (write-token gate row) | Write row fills "slot 1" by label | Write row "conforms to slot 1 format template" | Write row fills "slot 1 (INERTIA-REF)" | Write row names slot number + label + dependents | Write row names slot number + label + "Required by" cascade |
| **C-33** (Focus-scope evidence slot) | Slot 5, proof block description | Slot 5, full pipe-delimited format template | Slot 5, "proof table rows" description | Slot 5, proof table + "Required by: slot 4 + slot 1" | Slot 5, full template + "Required by" |
| **"Required by" column** | YES — 5-column contract table | NO | NO | YES | YES |
| **Phase 4 format** | Code block | Code block | 4-row PASS/FAIL table | 4-row PASS/FAIL table | 4-row PASS/FAIL table |
| **Slot 5 format template** | Description only | Full pipe-delimited template | Description only | Description only | Full pipe-delimited template |
| **AMEND slot 5 rerun** | Named (slot 5 refill obligation) | Named (slot 5 format template rerun) | Named (4-row table rebuild) | Named (table rebuild + "Required by") | Explicitly required + GATE 3 NOT ACCEPTABLE applies to AMEND |
| **GATE 3 NOT ACCEPTABLE** | NO | NO | NO | NO | YES — retroactive construction named |

---

## V-01 — Inertia framing ("Required by" column in OUTPUT CONTRACTS)

**Axis:** Inertia framing — the OUTPUT CONTRACTS table adds a fifth column, "Required by", that makes INERTIA-REF's role as the gravitational reference frame structurally explicit at contract-read time. INERTIA-REF is listed as the root slot (slot 1) with no upstream dependency. Every slot that depends on it names the dependency in the "Required by" column: the INERTIA-REF-DELTA slot states "Derived from slot 1 (root)"; the Focus-scope evidence slot states "Requires slot 4 (SOURCE) and slot 1 (INERTIA-REF) as comparator baseline". The inertia-first execution order is a visible contract constraint, not an implicit convention.

**Hypothesis:** When the contract table shows which slots depend on which, a model reading OUTPUT CONTRACTS sees the full execution dependency chain before encountering any gate. It cannot fill slot 6 (INERTIA-REF-DELTA) without slot 1 (INERTIA-REF); it cannot fill slot 5 (Focus-scope evidence) without both slot 4 (SOURCE) and slot 1. The "Required by" column adds zero new rules — it makes existing dependencies explicit at the earliest readable moment, reinforcing the inertia-as-root design across all downstream phases.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first — the complete production specification, including dependency relationships, is readable before any gate constraint is encountered.

---

### OUTPUT CONTRACTS

All output slots required by this skill, declared before any gate. The "Required by" column names upstream dependencies: slots that cannot be filled until a prior slot is written. INERTIA-REF (slot 1) is the root — no upstream dependency; all slots that use or compare against it name it in their "Required by" column.

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root — slots 5 and 6 depend on this token; must be written before any phase begins |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table | Source data for finding anchors at Phase 5; compared against slot 1 at slot 6 |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires completed slot 2 (Competitor Table); per-attribute absence evidence per row |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` | Phase 4 — Cross-Dimensional Finding | Required by slot 5; must be declared as the first element of the Phase 4 proof block |
| 5 | Focus-scope evidence | Proof block: `SOURCE + REDUCTION-1 NO + REDUCTION-2 NO + THEREFORE` | Phase 4 — Cross-Dimensional Finding | Requires slot 4 (SOURCE) and slot 1 (INERTIA-REF) as comparator baseline; both must be written before THEREFORE |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | Phase 5 — Findings Table | Derived from slot 1 (INERTIA-REF, root) — slot 1 must be written at GATE 4 before this slot can be filled |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row before outputting |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite the cell before outputting |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE block |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside PR diff — no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value (row label, attribute name, quoted value) appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must precede all reduction arguments; constructing an argument before naming the evidence is not allowed |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both reductions required; one alone does not establish cross-dimensionality |
| Both reductions answer NO | Neither single-dimension reduction produces the gap | **Proof structure failure** — if either answers YES, find a different gap before outputting THEREFORE |

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows of this gate before proceeding to Phase 1. The write row fills slot 1 (INERTIA-REF, root) in OUTPUT CONTRACTS above — slots 5 and 6 depend on this token per "Required by" column.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label such as "high familiarity" or "users are accustomed" | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF, root, PREFLIGHT > OUTPUT CONTRACTS above); token is now available to all phases; slots 5 and 6 require this token per "Required by" column | **Inertia write failure** — token must be written at this gate row, not deferred to a later phase; return to this row and execute the write |
| Per-finding citation required | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — fills slot 6 (INERTIA-REF-DELTA) per finding row | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

C0 is the entity whose stickiness was resolved in GATE 4. C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten; apply GATE 2 before outputting.

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token (slot 1, root, PREFLIGHT > OUTPUT CONTRACTS) — this data fills slot 6 (INERTIA-REF-DELTA, "Required by: slot 1") at Phase 5.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 2 (whitespace absence anchor). For each candidate whitespace attribute, record per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism from GATE 4}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. This phase fills two output contract slots: slot 4 (SOURCE) and slot 5 (Focus-scope evidence). Per the "Required by" column in OUTPUT CONTRACTS, slot 5 requires slot 4 (SOURCE) and slot 1 (INERTIA-REF). Declare SOURCE before writing any reduction argument.

```
SOURCE: {named cell — row label, attribute name, quoted value — fills slot 4; declare before
REDUCTION-1 per PREFLIGHT > OUTPUT CONTRACTS, slot 4 format}

REDUCTION-1: Competitive map alone — does the gap appear without the focus dimension?
[NO + one sentence showing what is lost when focus is dropped]

REDUCTION-2: Focus dimension alone — does the gap appear without the competitive map?
[NO + one sentence showing what is lost when the map is dropped]

If either answers YES, find a different gap — proceeding is a **proof structure failure**.

THEREFORE: {one sentence — the gap that requires both dimensions simultaneously}
```

The completed SOURCE + REDUCTION-1 + REDUCTION-2 + THEREFORE block fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 4 and slot 1").

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier — enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4 (Write row — slot 1 must have been written before this phase runs per "Required by" column); a cell with only "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name.

For the cross-dimensional finding row: the Claim cell contains the THEREFORE sentence. An adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot (PREFLIGHT > OUTPUT CONTRACTS — slot 4, SOURCE) with the new evidentiary anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus; the completed proof refills slot 5 (Focus-scope evidence — per "Required by" column: slot 4 and slot 1 must both be present before THEREFORE). Reconstruct THEREFORE. Apply GATE 3. Writing only a new conclusion without rerunning both reductions is a **proof rerun failure** — both single-dimension reduction arguments must be rebuilt.

2. **Add competitor**: Insert a new row after running WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, slot 2). Update Phase 3 WHITESPACE absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor, slot 3); a new row may change vacancy status. Review INERTIA-REF-DELTA (slot 6, derived from slot 1): does the new row's mechanism phrase alter the comparison for any existing finding row?

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4, Write row / OUTPUT CONTRACTS — slot 1, root): Re-execute the GATE 4 Write row with a more specific mechanism phrase — name a product feature, workflow step, or workaround behavior. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells (slot 6, "Required by: slot 1") referencing the old mechanism phrase; updated cells must conform to column format. Review slot 5 (Focus-scope evidence, "Required by: slot 4 and slot 1"): if the new INERTIA-REF phrase shifts the cross-dimensional baseline, rebuild the Phase 4 proof block.

---

## V-02 — Output format (Focus-scope evidence with full C-23-compliant format template)

**Axis:** Output format — the Focus-scope evidence slot in OUTPUT CONTRACTS specifies a complete structural format template, applying C-23's standard specifically to the cross-dimensional proof slot (as C-33 intends). The template is: `REDUCTION-1 NO: [{one sentence — what is lost if focus dimension is dropped}] | REDUCTION-2 NO: [{one sentence — what is lost if competitive map is dropped}] | THEREFORE: [{gap sentence requiring both dimensions simultaneously}]`. All 6 slots have format templates. The Focus-scope evidence template is the most structurally novel: it makes the proof output syntactically checkable before Phase 4 runs.

**Hypothesis:** When the contract declares the exact format for the proof output, Phase 4 knows before it runs that both reduction sentences and the THEREFORE sentence are required output fields — not rationale or commentary. A fully-specified format template makes the Focus-scope evidence slot as mechanical as the Anchor column: conformance is syntactically detectable without reading the gate logic. A slot producing `REDUCTION-1 NO: [...] | REDUCTION-2 NO: [...] | THEREFORE: [...]` is structurally distinguishable from a free-form paragraph without rule evaluation. This is the C-23 upgrade applied directly to C-33.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first — every slot specifies a required structural format template; a label alone is insufficient. The Focus-scope evidence slot declares the proof structure before Phase 4 runs.

---

### OUTPUT CONTRACTS

All output slots required by this skill, declared before any gate. Each slot specifies its label and a required structural format template. A slot filled in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

| Slot | Label | Required format | Filled by phase |
|------|-------|-----------------|-----------------|
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction; not a category label]` | GATE 4 (Write row, below) |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — declared before any reduction argument | Phase 4 — Cross-Dimensional Finding |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence — what is lost if the focus dimension is dropped from the analysis}] \| REDUCTION-2 NO: [{one sentence — what is lost if the competitive map is dropped from the analysis}] \| THEREFORE: [{gap sentence naming what requires both dimensions simultaneously}]` | Phase 4 — Cross-Dimensional Finding |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 — Findings Table |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row before outputting |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite the cell before outputting |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE block |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "requires all integrations to use REST polling — no webhook delivery pathway available"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value (row label, attribute name, quoted value) appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must precede all reduction arguments; constructing an argument before naming the evidence is not allowed |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both reductions required; one alone does not establish cross-dimensionality |
| Both reductions answer NO | Neither single-dimension reduction produces the gap | **Proof structure failure** — if either answers YES, find a different gap before outputting THEREFORE |

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows of this gate before proceeding to Phase 1.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — conforms to slot 1 format template (PREFLIGHT > OUTPUT CONTRACTS above); token is now available to all phases | **Inertia write failure** — token must be written at this gate row; return to this row and execute the write before Phase 1 begins |
| Per-finding citation required | Each finding in Phase 5 cites INERTIA-REF by token name, conforming to slot 6 format template: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

C0 is the entity whose stickiness was resolved in GATE 4. C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten; apply GATE 2 before outputting.

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token (slot 1) — this data fills slot 6 (INERTIA-REF-DELTA) at Phase 5; the slot 6 format template is declared in OUTPUT CONTRACTS above.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 2 (whitespace absence anchor). For each candidate whitespace attribute, record per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism from GATE 4}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. This phase fills two output contract slots. Slot 4 (SOURCE) must be declared before any reduction argument is written. Slot 5 (Focus-scope evidence) requires the exact format template from OUTPUT CONTRACTS above:

`REDUCTION-1 NO: [{one sentence — what is lost if the focus dimension is dropped}] | REDUCTION-2 NO: [{one sentence — what is lost if the competitive map is dropped}] | THEREFORE: [{gap sentence requiring both dimensions simultaneously}]`

Execute the proof block:

```
SOURCE: {named cell — row label, attribute name, quoted value — fills slot 4; declare before
REDUCTION-1 per PREFLIGHT > OUTPUT CONTRACTS, slot 4 format}

REDUCTION-1 NO: {one sentence showing what is lost if the focus dimension is dropped from
the analysis — why the competitive map alone does not produce the gap}

REDUCTION-2 NO: {one sentence showing what is lost if the competitive map is dropped from
the analysis — why the focus dimension alone does not produce the gap}

If either reduction answers YES, find a different gap — proceeding is a **proof structure failure**.

THEREFORE: {one sentence naming the gap that requires both dimensions simultaneously}
```

The completed block fills slot 5 (Focus-scope evidence) in the pipe-delimited format declared at PREFLIGHT > OUTPUT CONTRACTS.

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 3 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 2 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, mechanism: "requires synchronous kickoff call before any async handoff — no fully async onboarding path exists"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — apply GATE 4 (Write row — token must have been written before this phase runs); a cell with only "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name. Conform to slot 6 format template declared in OUTPUT CONTRACTS above.

For the cross-dimensional finding row: the Claim cell contains the THEREFORE sentence. An adjacent indented block contains the full proof block conforming to the slot 5 format template — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot (PREFLIGHT > OUTPUT CONTRACTS — slot 4) with the new evidentiary anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus using the slot 5 format template (`REDUCTION-1 NO: [...] | REDUCTION-2 NO: [...] | THEREFORE: [...]`). Reconstruct THEREFORE. Apply GATE 3. Writing only a new THEREFORE without rerunning both reductions is a **proof rerun failure** — both reduction sentences must be rebuilt to slot 5 format; slot 5 is refilled only when all three components are complete.

2. **Add competitor**: Insert a new row after running WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, slot 2). Update Phase 3 WHITESPACE absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor, slot 3); a new row may change vacancy status.

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4, Write row / OUTPUT CONTRACTS — slot 1): Re-execute the GATE 4 Write row with a more specific mechanism phrase — name a product feature, workflow step, or workaround behavior, conforming to the slot 1 format template. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells (slot 6) referencing the old mechanism phrase; updated cells must conform to slot 6 format template.

---

## V-03 — Lifecycle emphasis (Phase 4 as a 4-row structured proof table)

**Axis:** Lifecycle emphasis — Phase 4's proof block is restructured as a 4-row PASS/FAIL table (SOURCE, REDUCTION-1, REDUCTION-2, THEREFORE). Each row specifies a required value format and a named failure state. This restructuring elevates Phase 4 from a code-block instruction to a machine-checkable output grid: the proof is independently verifiable at the phase level without reading PREFLIGHT's GATE 3. The "SOURCE first" constraint becomes structural — the SOURCE row appears before REDUCTION rows by table position, not by prose instruction alone.

**Hypothesis:** When the proof block is a structured table, each cell has an explicit format constraint and a named failure mode. A reviewer scans the Phase 4 output table the same way they scan the competitor table: row by row, checking format compliance and failure state. Code-block proof formats are prose-shaped: they can be read as guidance or rationale. A 4-row table is output-shaped: it is a deliverable with checkable rows. The table also eliminates positional ambiguity for SOURCE: in a table, "first row" is unambiguous; in a code block, "declared first" requires prose interpretation.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first — the complete production specification is readable before any gate constraint is encountered.

---

### OUTPUT CONTRACTS

All output slots required by this skill, declared before any gate. Each slot specifies its label, required structural format, and the gate or phase responsible for filling it.

| Slot | Label | Required format | Filled by phase |
|------|-------|-----------------|-----------------|
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding |
| 5 | Focus-scope evidence | Phase 4 proof table: SOURCE row (slot 4) + REDUCTION-1 row (NO) + REDUCTION-2 row (NO) + THEREFORE row — all four rows required | Phase 4 — Cross-Dimensional Finding |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | Phase 5 — Findings Table |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row before outputting |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite the cell before outputting |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE block |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "enforces daily standup via calendar lock — no async standup pathway in the product"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row present first | SOURCE row appears as the first row in the Phase 4 proof table; slot 4 (SOURCE, PREFLIGHT > OUTPUT CONTRACTS) is filled | **Proof structure failure** — SOURCE row must precede REDUCTION rows; table position is the constraint; an absent or malformed SOURCE row constitutes a proof structure failure |
| Both reduction rows answer NO | REDUCTION-1 row and REDUCTION-2 row each contain "NO" with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — a YES answer means the gap is single-dimension sufficient; discard and find a different gap |
| THEREFORE row present | THEREFORE row contains a single complete sentence naming the cross-dimensional gap; may not be filled until both reduction rows answer NO | **Proof structure failure** — THEREFORE row is blocked until both REDUCTION-1 and REDUCTION-2 answer NO |

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows of this gate before proceeding to Phase 1.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF) in PREFLIGHT > OUTPUT CONTRACTS above; token is now available to all phases | **Inertia write failure** — token must be written at this gate row, not deferred to a later phase; return to this row and execute the write |
| Per-finding citation required | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

C0 is the entity whose stickiness was resolved in GATE 4. C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten; apply GATE 2 before outputting.

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token (slot 1) — this data fills slot 6 (INERTIA-REF-DELTA) at Phase 5.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 2 (whitespace absence anchor). For each candidate whitespace attribute, record per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism from GATE 4}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. The proof is structured as a four-row table. Rows must appear in order: SOURCE before REDUCTION-1 before REDUCTION-2 before THEREFORE. Complete all four rows before outputting. If REDUCTION-1 or REDUCTION-2 answers YES, stop and find a different gap before writing THEREFORE.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — named cell from the competitor table; fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row of this table | **Proof structure failure** — SOURCE row must appear first; absent or malformed SOURCE constitutes a proof structure failure before any reduction is evaluated |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped from the analysis; the competitive map alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the competitive map alone; discard and find a different gap |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped from the analysis; the focus dimension alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the focus dimension alone; discard and find a different gap |
| THEREFORE | `{one sentence naming the gap that requires both the competitive map and the focus dimension simultaneously}` | **Proof structure failure** — THEREFORE row is blocked until both REDUCTION-1 and REDUCTION-2 answer NO; may not be written before both reduction rows are complete |

The completed four-row proof table fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS).

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, threat: "high — real-time collaborative editing eliminates the async-first gap we plan to occupy"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4 (Write row — slot 1 must have been written before this phase runs); a cell with only "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name.

For the cross-dimensional finding row: the Claim cell contains the THEREFORE sentence (from the Phase 4 proof table, THEREFORE row). An adjacent indented section reproduces the full Phase 4 proof table — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Rebuild the Phase 4 proof table from scratch: replace the SOURCE row (fills slot 4, PREFLIGHT > OUTPUT CONTRACTS) with the new evidentiary anchor; rewrite REDUCTION-1 and REDUCTION-2 rows against the updated focus; reconstruct the THEREFORE row. Apply GATE 3. Writing only a new THEREFORE row without rerunning both reduction rows is a **proof rerun failure** — the full 4-row proof table must be rebuilt; slot 5 (Focus-scope evidence) is refilled only when all four rows are complete.

2. **Add competitor**: Insert a new row after running WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, slot 2). Update Phase 3 WHITESPACE absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor, slot 3); a new row may change vacancy status.

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4, Write row / OUTPUT CONTRACTS — slot 1): Re-execute the GATE 4 Write row with a more specific mechanism phrase — name a product feature, workflow step, or workaround behavior. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells (slot 6) referencing the old mechanism phrase; updated cells must conform to column format.

---

## V-04 — Combined: Inertia framing + Lifecycle emphasis

**Axis:** Inertia framing + Lifecycle emphasis — combines V-01's "Required by" column in OUTPUT CONTRACTS with V-03's 4-row Phase 4 proof table. The GATE 4 write row explicitly names both the slot number and the label it fills ("fills slot 1 — INERTIA-REF, root slot, PREFLIGHT > OUTPUT CONTRACTS above") and names the dependent slots ("slots 5 and 6 require this token per 'Required by' column"). The Phase 4 proof table's SOURCE row names the slot it fills by number and label; the completed table names the slot 5 it satisfies.

**Hypothesis:** Combining the dependency chain (V-01) with the structured proof table (V-03) produces the tightest bidirectional specification in this round. Every slot has a forward declaration in OUTPUT CONTRACTS (including "Required by" provenance) and a back-reference at the point of production (GATE 4 write row naming slot 1; Phase 4 table rows naming slots 4 and 5). The "Required by" column makes the INERTIA-REF dependency chain visible at contract-read time; the Phase 4 proof table makes the Focus-scope evidence structure output-verifiable. Together, no slot's dependency is implicit: provenance is traceable in both directions for every slot.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first. The "Required by" column names upstream slot dependencies — INERTIA-REF (slot 1) is the root; all slots that cite or compare against it list it in "Required by".

---

### OUTPUT CONTRACTS

All output slots required by this skill, declared before any gate. The "Required by" column names upstream dependencies. INERTIA-REF (slot 1) is the root slot — no upstream dependency; all slots derived from or compared against it name it explicitly.

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root — slots 5 and 6 depend on this token; must be written before any phase begins |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table | Source data for Phase 5 finding anchors |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires completed slot 2; per-attribute absence evidence per competitor row |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding | Required by slot 5; SOURCE row must be the first row of the proof table |
| 5 | Focus-scope evidence | Phase 4 proof table: SOURCE row (slot 4) + REDUCTION-1 row (NO) + REDUCTION-2 row (NO) + THEREFORE row — all four rows required | Phase 4 — Cross-Dimensional Finding | Requires slot 4 (SOURCE) and slot 1 (INERTIA-REF) as comparator baseline; all four table rows required |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | Phase 5 — Findings Table | Derived from slot 1 (INERTIA-REF, root) — slot 1 must be written at GATE 4 before this slot can be filled |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row before outputting |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite the cell before outputting |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE block |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "routes all support tickets through a shared queue — no per-team inbox routing available"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row present first | SOURCE row appears as the first row in the Phase 4 proof table; slot 4 (SOURCE, PREFLIGHT > OUTPUT CONTRACTS) is filled | **Proof structure failure** — SOURCE row must precede REDUCTION rows; table position enforces this constraint |
| Both reduction rows answer NO | REDUCTION-1 row and REDUCTION-2 row each contain "NO" with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — a YES answer means the gap is single-dimension sufficient; discard and find a different gap |
| THEREFORE row present | THEREFORE row contains a single complete sentence naming the cross-dimensional gap; may not be written until both reduction rows answer NO | **Proof structure failure** — THEREFORE row is blocked until both reductions answer NO |

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows of this gate before proceeding to Phase 1.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF, root slot, PREFLIGHT > OUTPUT CONTRACTS above); slots 5 and 6 depend on this token per "Required by" column; token is now available to all phases | **Inertia write failure** — token must be written at this gate row; slots 5 (Focus-scope evidence) and 6 (INERTIA-REF-DELTA) cannot be filled until slot 1 is written; return to this row and execute the write |
| Per-finding citation required | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — fills slot 6 (INERTIA-REF-DELTA, "Required by: slot 1") per finding row | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

C0 is the entity whose stickiness was resolved in GATE 4. C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten; apply GATE 2 before outputting.

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token (slot 1, root, PREFLIGHT > OUTPUT CONTRACTS) — this data fills slot 6 (INERTIA-REF-DELTA, "Required by: slot 1") at Phase 5.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 2 (whitespace absence anchor). For each candidate whitespace attribute, record per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism from GATE 4}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. The proof is structured as a four-row table. Rows must appear in order: SOURCE before REDUCTION-1 before REDUCTION-2 before THEREFORE. Per the "Required by" column in OUTPUT CONTRACTS, slot 5 requires slot 4 (SOURCE) and slot 1 (INERTIA-REF, root) — verify slot 1 was written at GATE 4 before running REDUCTION-1.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — named cell from the competitor table; fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row of this table | **Proof structure failure** — SOURCE row must appear first; absent or malformed SOURCE constitutes a proof structure failure before any reduction is evaluated |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped; the competitive map alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the competitive map alone; discard and find a different gap |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped; the focus dimension alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the focus dimension alone; discard and find a different gap |
| THEREFORE | `{one sentence naming the gap that requires both dimensions simultaneously}` | **Proof structure failure** — THEREFORE row is blocked until both REDUCTION-1 and REDUCTION-2 answer NO; may not be written before both rows are complete |

The completed four-row proof table fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 4 and slot 1").

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 3 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C2, focus-column: "charges per-seat regardless of usage frequency — no consumption-based pricing tier"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4 (Write row — slot 1 must have been written before this phase runs per "Required by" column); a cell with only "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name.

For the cross-dimensional finding row: the Claim cell contains the THEREFORE sentence (from the Phase 4 proof table, THEREFORE row). An adjacent indented section reproduces the full Phase 4 proof table — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Rebuild the Phase 4 proof table from scratch: replace the SOURCE row (fills slot 4, PREFLIGHT > OUTPUT CONTRACTS); rewrite REDUCTION-1 and REDUCTION-2 rows against the updated focus (slot 5 "Required by: slot 4 and slot 1" per OUTPUT CONTRACTS); reconstruct the THEREFORE row. Apply GATE 3. Writing only a new THEREFORE row without rerunning both reduction rows is a **proof rerun failure** — the full 4-row proof table must be rebuilt; slot 5 is refilled only when all four rows are complete.

2. **Add competitor**: Insert a new row after running WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, slot 2). Update Phase 3 WHITESPACE absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor, slot 3); a new row may change vacancy status. Review INERTIA-REF-DELTA (slot 6, "Required by: slot 1"): does the new row's mechanism phrase alter the comparison for any existing finding row?

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4, Write row / OUTPUT CONTRACTS — slot 1, root): Re-execute the GATE 4 Write row with a more specific mechanism phrase — name a product feature, workflow step, or workaround behavior. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells (slot 6, "Required by: slot 1") referencing the old mechanism phrase; updated cells must conform to column format. Review slot 5 (Focus-scope evidence, "Required by: slot 4 and slot 1"): if the new INERTIA-REF phrase shifts the cross-dimensional baseline, rebuild the Phase 4 proof table to update the REDUCTION arguments.

---

## V-05 — Combined maximum (all three axes + AMEND slot 5 obligation + GATE 3 NOT ACCEPTABLE)

**Axis:** Combined maximum — all three single-axis innovations plus two enforcement extensions. V-01's "Required by" column makes dependency provenance contract-visible. V-02's full format template for slot 5 makes the proof structure syntactically specified before Phase 4 runs. V-03's 4-row Phase 4 proof table makes the output verifiable by table structure. Extension 1: AMEND explicitly requires re-filling slot 5 (Focus-scope evidence) when the focus dimension shifts, making the C-33 slot a mandatory named AMEND target. Extension 2: GATE 3 includes NOT ACCEPTABLE examples naming the most common proof construction failure — writing THEREFORE first and adding reductions retroactively — closing the escape hatch left open by code-block proof formats.

**Hypothesis:** The combined variation tests the ceiling of the R8 design space. Every structural enforcement surface is active simultaneously: the "Required by" column prevents implicit dependency skipping; the slot 5 format template makes the proof syntactically checkable; the Phase 4 proof table makes it output-verifiable; the AMEND extension makes slot 5 a required named target on focus shift; the GATE 3 NOT ACCEPTABLE examples close the retroactive reduction construction failure. A skill satisfying all these constraints provides the maximum enforcement depth without requiring additional rubric criteria.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first. The "Required by" column names upstream slot dependencies. Every slot specifies a required structural format template.

---

### OUTPUT CONTRACTS

All output slots required by this skill, declared before any gate. Each slot specifies its label, required structural format, the gate or phase responsible for filling it, and its upstream dependencies. A slot filled in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction; not a category label]` | GATE 4 (Write row, below) | Root — slots 5 and 6 depend on this token; must be written before any phase begins |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Source data for finding anchors at Phase 5 |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires completed slot 2; per-attribute evidence per competitor row |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; SOURCE row must appear before all REDUCTION rows |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence -- what is lost if focus dimension is dropped}] \| REDUCTION-2 NO: [{one sentence -- what is lost if competitive map is dropped}] \| THEREFORE: [{gap sentence requiring both dimensions simultaneously}]` | Phase 4 -- Cross-Dimensional Finding | Requires slot 4 (SOURCE) and slot 1 (INERTIA-REF) as comparator baseline; all three components required |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (INERTIA-REF, root) — slot 1 must be written at GATE 4 before this slot can be filled |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row before outputting |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite the cell before outputting |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE block |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "requires annual contract renewal to access data export — no self-serve export on monthly plan"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row present first | SOURCE row appears as the first row in the Phase 4 proof table; fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS) | **Proof structure failure** — SOURCE row must precede all REDUCTION rows; table position is the constraint; absent or malformed SOURCE is a proof structure failure |
| Both reduction rows answer NO | REDUCTION-1 and REDUCTION-2 rows each contain "NO" with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — a YES answer means the gap is single-dimension sufficient; discard and find a different gap |
| THEREFORE row present | THEREFORE row contains a single complete sentence naming the cross-dimensional gap; may not be filled until both reductions answer NO | **Proof structure failure** — THEREFORE row is blocked until both REDUCTION-1 and REDUCTION-2 answer NO |

NOT ACCEPTABLE (proof construction): Writing THEREFORE first and then adding REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**; SOURCE must be declared first, reduction rows must answer NO independently before THEREFORE is written.
NOT ACCEPTABLE (proof construction): Citing both dimensions in the THEREFORE row without dedicated REDUCTION-1 and REDUCTION-2 rows each answering NO — assertion-only cross-dimensionality — **proof structure failure**; both reduction rows are required and must precede THEREFORE.

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows of this gate before proceeding to Phase 1.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label such as "high familiarity" or "users are accustomed" | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — conforms to slot 1 format template; fills slot 1 (root slot, PREFLIGHT > OUTPUT CONTRACTS above); slots 5 and 6 depend on this token per "Required by" column; token is now available to all phases | **Inertia write failure** — token must be written at this gate row; slots 5 (Focus-scope evidence) and 6 (INERTIA-REF-DELTA) cannot be filled until slot 1 is written; return to this row and execute the write |
| Per-finding citation required | Each finding in Phase 5 cites INERTIA-REF by token name, conforming to slot 6 format template: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

C0 is the entity whose stickiness was resolved in GATE 4. C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten; apply GATE 2 before outputting.

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token (slot 1, root) — this data fills slot 6 (INERTIA-REF-DELTA, "Required by: slot 1") at Phase 5; the slot 6 format template is declared in OUTPUT CONTRACTS above.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 2 (whitespace absence anchor). For each candidate whitespace attribute, record per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism from GATE 4}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. The proof is structured as a four-row table. Rows must appear in order: SOURCE before REDUCTION-1 before REDUCTION-2 before THEREFORE. Slot 5 format template from OUTPUT CONTRACTS above defines the required output: `REDUCTION-1 NO: [...] | REDUCTION-2 NO: [...] | THEREFORE: [...]`. Slot 5 requires slot 4 (SOURCE) and slot 1 (INERTIA-REF, root) per "Required by" column — verify slot 1 was written at GATE 4 before executing REDUCTION-1. See GATE 3 NOT ACCEPTABLE examples before writing any row.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row of this table; declared before any reduction argument | **Proof structure failure** — SOURCE row must appear first; absent or malformed SOURCE constitutes a proof structure failure; retroactive SOURCE addition after REDUCTION rows is not allowed |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped; the competitive map alone does not produce this gap}` — conforms to "REDUCTION-1 NO: [...]" component of slot 5 format template | **Proof structure failure** — if YES, the gap is producible from the competitive map alone; discard and restart; writing THEREFORE before this row answers NO is a proof structure failure (see GATE 3 NOT ACCEPTABLE) |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped; the focus dimension alone does not produce this gap}` — conforms to "REDUCTION-2 NO: [...]" component of slot 5 format template | **Proof structure failure** — if YES, the gap is producible from the focus dimension alone; discard and restart |
| THEREFORE | `{one sentence naming the gap that requires both dimensions simultaneously}` — conforms to "THEREFORE: [...]" component of slot 5 format template | **Proof structure failure** — THEREFORE row is blocked until both REDUCTION-1 and REDUCTION-2 answer NO; retroactive construction from THEREFORE backward is a proof structure failure (see GATE 3 NOT ACCEPTABLE) |

The completed four-row proof table fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS — format: `REDUCTION-1 NO: [...] | REDUCTION-2 NO: [...] | THEREFORE: [...]`).

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C2, mechanism: "all exports are batch-only — no streaming API for real-time data access"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — apply GATE 4 (Write row — slot 1 must have been written before this phase runs per "Required by" column); a cell with only "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name; conform to slot 6 format template.

For the cross-dimensional finding row: the Claim cell contains the THEREFORE sentence (from the Phase 4 proof table, THEREFORE row). An adjacent indented section reproduces the full Phase 4 proof table conforming to the slot 5 format template — apply GATE 3 and GATE 3 NOT ACCEPTABLE examples.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Rebuild the Phase 4 proof table from scratch — replace the SOURCE row (refills slot 4, PREFLIGHT > OUTPUT CONTRACTS); rewrite REDUCTION-1 and REDUCTION-2 rows against the updated focus; reconstruct the THEREFORE row. The completed table refills slot 5 (Focus-scope evidence) in the pipe-delimited format template from PREFLIGHT > OUTPUT CONTRACTS. Apply GATE 3 — the GATE 3 NOT ACCEPTABLE construction ("THEREFORE first, reductions retroactively") applies to AMEND updates as well. Writing only a new THEREFORE row without rerunning both reduction rows is a **proof rerun failure** — the full 4-row proof table must be rebuilt and slot 5 explicitly refilled.

2. **Add competitor**: Insert a new row after running WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, slot 2). Update Phase 3 WHITESPACE absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor, slot 3); a new row may change vacancy status. Review INERTIA-REF-DELTA (slot 6, "Required by: slot 1"): does the new row's mechanism phrase alter the comparison for any existing finding row?

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4, Write row / OUTPUT CONTRACTS — slot 1, root): Re-execute the GATE 4 Write row with a more specific mechanism phrase — name a product feature, workflow step, or workaround behavior; conform to slot 1 format template. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells (slot 6, "Required by: slot 1") referencing the old mechanism phrase; updated cells must conform to slot 6 format template. If the new INERTIA-REF phrase shifts the cross-dimensional baseline, rebuild the Phase 4 proof table (refills slot 5 — "Required by: slot 4 and slot 1") applying the slot 5 format template and GATE 3 NOT ACCEPTABLE constraints.
