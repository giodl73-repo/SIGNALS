Written to `simulations/quest/variations/discover-competitors-alt-variations-R10-2026-03-17.md`.

---

## R10 Variations Summary

All 5 variations target **245/245** on rubric v9. Baseline is R9 V-05 (all C-37/38/39 included in every variation).

| Variation | Axis | Innovation |
|-----------|------|-----------|
| **V-01** | Role sequence | FOCUS CHECK → GATE 0 inside PREFLIGHT (3-row PASS/FAIL table: detection / active branch / inactive branch) |
| **V-02** | Output format | Phase 3 vs-INERTIA-REF row coerced to slot 6 ternary-token format (`reinforces / challenges / contextualizes`) |
| **V-03** | Inertia framing | EXECUTION DEPENDENCY gains "Prerequisite steps" column — step ordering readable without slot-tracing |
| **V-04** | A + B | FOCUS GATE + ternary vs-INERTIA-REF |
| **V-05** | Maximum | All three axes |

**Three candidate new criteria:**

- **C-40** (V-01): FOCUS GATE as named gate within PREFLIGHT — prose FOCUS CHECK outside PREFLIGHT does not satisfy even if logic is identical; activation/inactivation branches name slot consequences explicitly
- **C-41** (V-02): Phase 3 vs-INERTIA-REF row uses slot 6 format template — ternary token required; "vs. INERTIA-REF — this gap is adjacent to C0's workflow" fails; whitespace and finding comparisons become syntactically isomorphic
- **C-42** (V-03): EXECUTION DEPENDENCY "Prerequisite steps" column — GATE 4 has "None (root)" in both Reads slot and Prerequisite steps; root confirmed from two orthogonal angles independently

**Notable V-05 structural property:** GATE 4's root status is now confirmed from four independent positions — OUTPUT CONTRACTS "Required by" (slot level), EXECUTION DEPENDENCY "Reads slot" (data level), EXECUTION DEPENDENCY "Prerequisite steps: None" (step level), and GATE 0 which determines the execution start state before the DAG is read.
EXECUTION DEPENDENCY includes "Prerequisite steps" column — step ordering readable by step name without slot-tracing; GATE 4 has "None (root)" in both Reads slot and Prerequisite steps, confirming root status from two independent angles

| | **V-01** | **V-02** | **V-03** | **V-04** | **V-05** |
|---|---|---|---|---|---|
| **C-37** (Phase 3 as 4-row PASS/FAIL table) | YES | YES | YES | YES | YES |
| **C-38** (AMEND as structured table) | YES | YES | YES | YES | YES |
| **C-39** (EXECUTION DEPENDENCY in PREFLIGHT) | YES | YES | YES | YES | YES |
| **FOCUS CHECK format** | GATE 0 inside PREFLIGHT | Prose (pre-PREFLIGHT) | Prose (pre-PREFLIGHT) | GATE 0 inside PREFLIGHT | GATE 0 inside PREFLIGHT |
| **Phase 3 vs-INERTIA-REF format** | Prose (C-37 baseline) | Slot 6 template (ternary token) | Prose (C-37 baseline) | Slot 6 template (ternary token) | Slot 6 template (ternary token) |
| **EXECUTION DEPENDENCY columns** | 4 columns | 4 columns | 5 columns (+ Prerequisite steps) | 4 columns | 5 columns (+ Prerequisite steps) |

---

## V-01 — Role sequence (FOCUS CHECK as GATE 0 inside PREFLIGHT)

**Axis:** Role sequence — the FOCUS CHECK moves from a prose block before PREFLIGHT into a named gate (GATE 0: FOCUS GATE) within PREFLIGHT, placed after OUTPUT CONTRACTS and before EXECUTION DEPENDENCY. The gate contains a 3-row PASS/FAIL table: focus value detection (with explicit failure for unrecognized values), focus-active branch (naming which slots fill as non-vacuous values), and focus-inactive branch (naming which slots satisfy by vacuous satisfaction). This makes the focus-dimension conditionality machine-readable at the same structural level as the other gates.

**Hypothesis:** The prose FOCUS CHECK is the one remaining pre-execution constraint that lives outside PREFLIGHT. A model reading PREFLIGHT today encounters slot targets (OUTPUT CONTRACTS), step ordering (EXECUTION DEPENDENCY), and gate constraints (GATE 1-4) — but must look outside PREFLIGHT to know which slots activate under focus. Moving focus detection inside PREFLIGHT as GATE 0 closes this gap: the activation/inactivation consequences for slot 5 (Focus-scope evidence) are declared at gate level before any phase reads them. The failure states name branch violations that currently have no explicit failure name — activating focus without the column, or adding a focus column when inactive.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first. GATE 0 (FOCUS GATE) follows — focus state resolved before the execution dependency graph is read. EXECUTION DEPENDENCY follows. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

All output slots required by this skill, declared before any gate. Each slot specifies its label, required structural format, the gate or phase responsible for filling it, and the upstream slots it depends on.

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root — no upstream dependency; slots 5 and 6 require this token before they can be filled |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 values at Phase 5 |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires slot 2 (Competitor Table complete before whitespace evaluation begins) |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding | Required by slot 5; must appear as the first row of the proof table before any reduction row |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence — what is lost if the focus dimension is dropped}] \| REDUCTION-2 NO: [{one sentence — what is lost if the competitive map is dropped}] \| THEREFORE: [{gap sentence requiring both dimensions simultaneously}]` — or vacuous satisfaction when GATE 0 focus-inactive branch applies | Phase 4 — Cross-Dimensional Finding | Requires slot 4 (SOURCE) and slot 1 (INERTIA-REF) when focus is active (see GATE 0); vacuous when focus is inactive |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 — Findings Table | Derived from slot 1 (INERTIA-REF, root) — slot 1 must be written at GATE 4 before Phase 5 runs |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### GATE 0: FOCUS GATE

Resolve focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all three rows before proceeding. The focus state determines which branch of slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS) applies.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` is set to a recognized value (`market-sizing`, `positioning-framework`) — OR — `focus:` is not set; infer from repo context (README, CLAUDE.md) before defaulting to none | **Focus detection failure** — unrecognized or ambiguous focus value; resolve to a recognized value or omit before proceeding; do not execute Phase 2 until focus state is confirmed |
| Focus-active branch | When focus is set: Focus column added to Phase 2 competitor table header; slot 5 (Focus-scope evidence) fills as full pipe-delimited proof string (`REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`); Phase 4 proof table required; GATE 3 applies; cross-dimensional criteria are live | **Focus activation failure** — focus is active but Focus column omitted from Phase 2 table or slot 5 declared vacuously; both column and full proof string required when focus is set |
| Focus-inactive branch | When focus is not set: Focus column not added to Phase 2 table; slot 5 satisfies by vacuous satisfaction; Phase 4 still runs; THEREFORE does not require cross-dimensional necessity argument; cross-dimensional criteria pass by vacuous satisfaction | **Focus inactivation failure** — Focus column present in competitor table when focus is not set; remove column from Phase 2 header before outputting |

---

### EXECUTION DEPENDENCY

Step-level execution ordering machine-readable before any numbered gate is read. GATE 4 is the root step. A step listed in "Reads slot" must not begin until that slot has been written.

| Step | Reads slot | Writes slot | Execution constraint |
|------|-----------|------------|---------------------|
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and all other phases**; no phase may produce output until slot 1 is written |
| Phase 1 | — | TOPIC, FOCUS tokens | Runs after GATE 4; reads repo context before Phase 2 |
| Phase 2 (per competitor row) | 1 — INERTIA-REF (C0 row mechanism reference) | 2 — Anchor column value | Runs after Phase 1; GATE 1 and GATE 2 applied per row; slot 2 complete when all rows output; Focus column per GATE 0 |
| Phase 3 (per whitespace candidate) | 2 — Anchor column value (Competitor Table complete) | 3 — Absence evidence block | Runs after Phase 2 complete; WHITESPACE VALIDATION table (4 rows) executed per candidate attribute |
| Phase 4, SOURCE row | 2 — Anchor column value (named cell from competitor table) | 4 — SOURCE slot | SOURCE row is row 1 of proof table; must be written before any REDUCTION row |
| Phase 4, REDUCTION + THEREFORE rows | 4 — SOURCE slot (written), 1 — INERTIA-REF (comparator baseline) | 5 — Focus-scope evidence | Both REDUCTION rows answer NO before THEREFORE; slot 5 filled as pipe-delimited string on THEREFORE completion; vacuous if GATE 0 focus-inactive |
| Phase 5 (per finding row) | 1 — INERTIA-REF (DELTA column), 2 — Anchor column value (Anchor column) | 6 — INERTIA-REF-DELTA | Runs after Phase 4 complete; GATE 4 row 3 (per-finding citation) applied per row |

An **execution dependency violation** occurs when a step begins before its declared "Reads slot" value has been written.

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
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without per-row attribute-level evidence does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff — no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is the first row of the Phase 4 proof table; slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS) is filled before any reduction row | **Proof structure failure** — SOURCE must be the first table row; any ordering that places a REDUCTION row before SOURCE is structurally malformed |
| Both reductions answer NO | REDUCTION-1 row and REDUCTION-2 row each contain "NO" with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both rows required; if either answers YES, discard the gap and find a different one |
| THEREFORE blocked until reductions complete | THEREFORE row written only after both REDUCTION rows answer NO | **Proof structure failure** — THEREFORE is blocked; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows before Phase 1. The write row fills slot 1 (INERTIA-REF, root) in PREFLIGHT > OUTPUT CONTRACTS — slots 5 and 6 depend on this token per "Required by" column; GATE 4 is the root step per PREFLIGHT > EXECUTION DEPENDENCY.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF, root, PREFLIGHT > OUTPUT CONTRACTS); root step complete (PREFLIGHT > EXECUTION DEPENDENCY); token now available to all phases; slots 5 and 6 require this token per "Required by" column | **Inertia write failure** — token must be written at this gate row, not deferred to a later phase; return to this row and execute the write before Phase 1 begins |
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

C0 is the entity whose stickiness was resolved in GATE 4 (root step, PREFLIGHT > EXECUTION DEPENDENCY). C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting. Focus column present or absent per GATE 0 (PREFLIGHT).

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten; apply GATE 2 before outputting.

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token (slot 1, root, PREFLIGHT > OUTPUT CONTRACTS) — this data fills slot 6 (INERTIA-REF-DELTA, "Required by: slot 1") at Phase 5 per PREFLIGHT > EXECUTION DEPENDENCY.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 2 (Competitor Table complete) per PREFLIGHT > EXECUTION DEPENDENCY. For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table. Rows must appear in order: CANDIDATE before ABSENCE-EVIDENCE before GAP-CONFIRMED before vs-INERTIA-REF. Complete all four rows before moving to the next candidate attribute.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — the candidate gap attribute under evaluation; declared before any absence evidence is gathered | **Whitespace naming failure** — declare the candidate attribute as the first row; an absent or unnamed CANDIDATE row blocks the ABSENCE-EVIDENCE row |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every competitor row (including C0) — fills slot 3 (Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS) | **Whitespace gate failure** — per-row evidence required for every competitor row; a bare assertion does not satisfy; every row must appear before GAP-CONFIRMED |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}] — attribute-level uncontested` — or — `Gap not confirmed: Row C{N} provides [{non-absent value}]; select a different candidate` | **Whitespace gate failure** — if any row provides a non-absent value, this candidate is not whitespace; stop, select a different attribute, restart the validation table |
| vs-INERTIA-REF | `vs. INERTIA-REF — {how the vacant attribute relates to the C0 mechanism phrase from slot 1}` | **Whitespace INERTIA-REF failure** — every gap finding must name its relationship to the INERTIA-REF mechanism; "N/A" is not permitted as the final row of a whitespace validation pass |

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion in ABSENCE-EVIDENCE row — **whitespace gate failure**
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before completing ABSENCE-EVIDENCE for all competitor rows — **whitespace gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. Reads slot 2 (named cell) and slot 1 (INERTIA-REF comparator) per PREFLIGHT > EXECUTION DEPENDENCY. Execute all four rows in order. SOURCE is row 1. If GATE 0 focus-inactive branch applies, slot 5 satisfies by vacuous satisfaction.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — named cell from the competitor table; fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row of this table | **Proof structure failure** — SOURCE row must appear first; absent or malformed SOURCE blocks all subsequent rows |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped; the competitive map alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the competitive map alone; discard and find a different gap |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped; the focus dimension alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the focus dimension alone; discard and find a different gap |
| THEREFORE | `{one sentence naming the gap that requires both dimensions simultaneously}` — fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS): `REDUCTION-1 NO: [REDUCTION-1 sentence] \| REDUCTION-2 NO: [REDUCTION-2 sentence] \| THEREFORE: [THEREFORE sentence]` | **Proof structure failure** — THEREFORE is blocked until both REDUCTION rows answer NO; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. Reads slot 1 (INERTIA-REF) and slot 2 (Anchor values) per PREFLIGHT > EXECUTION DEPENDENCY. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier — enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — every finding row must cite INERTIA-REF by token name; a cell with only "N/A" is malformed.

For the cross-dimensional finding row: Claim = THEREFORE sentence; Anchor = SOURCE value; adjacent indented block contains slot 5 pipe-delimited proof string — apply GATE 3.

---

### AMEND

Execute exactly 3 adjustment rows. Each row names the adjustment, what the user changes, what changes in the output, which output contract slots are re-filled, and which gates re-run.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` — re-run GATE 0 focus-active branch with new value | SOURCE slot re-identified from updated focus; Focus-scope evidence (slot 5) rebuilt from scratch: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` — both reduction sentences rebuilt; THEREFORE rewritten; cross-dimensional finding row updated in Phase 5 | 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (focus-active branch re-confirmed with new focus value), GATE 3 (all rows: SOURCE first, both reductions answer NO, THEREFORE blocked) — writing a new THEREFORE without rerunning both reductions is a **proof rerun failure**; slot 5 re-filled only when all three pipe-delimited components conform |
| 2 | Add competitor | Competitor name + context for WebSearch | New competitor row (slot 2: `Row C{N}, {attribute}: "{value}"`); WHITESPACE VALIDATION table re-run for all candidate attributes (slot 3 re-evaluated — a new row may change vacancy status); INERTIA-REF-DELTA (slot 6) reviewed for existing findings | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation for new row), GATE 2 (anchor format for new row; ABSENCE-EVIDENCE rows in WHITESPACE VALIDATION table for all candidate attributes) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase — product feature, workflow step, or workaround behavior | INERTIA-REF token (slot 1) re-written at GATE 4 write row (root step, PREFLIGHT > EXECUTION DEPENDENCY); all Phase 5 INERTIA-REF-DELTA cells (slot 6) updated; Phase 4 proof table (slot 5) reviewed — if new mechanism phrase shifts cross-dimensional baseline, rebuild all four proof rows and re-fill slot 5 in pipe-delimited format | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA, all finding rows), 5 (Focus-scope evidence, if baseline shifts) | GATE 4 (all rows: stickiness check, write row, per-finding citation), GATE 3 (if slot 5 rebuild required: SOURCE, both reductions, THEREFORE) |

---

## V-02 — Output format (Phase 3 vs-INERTIA-REF row coerced to slot 6 format template)

**Axis:** Output format — the vs-INERTIA-REF row in the Phase 3 WHITESPACE VALIDATION table is updated to require the same ternary-token format as slot 6: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}`. Previously the Required value was generic prose (`{how the vacant attribute relates to the C0 mechanism phrase from slot 1}`), allowing any relationship description without categorical commitment. The ternary token constraint makes whitespace-level and finding-level INERTIA-REF comparisons syntactically isomorphic — both require exactly one of reinforces, challenges, or contextualizes before the mechanism phrase.

**Hypothesis:** Slot 6 (INERTIA-REF-DELTA) already enforces the ternary token at the finding level. Phase 3's vs-INERTIA-REF row uses a looser format that accepts prose descriptions like "this gap is adjacent to C0's workflow" — which pass C-37 structurally but carry no information about the C0 relationship type. Applying the slot 6 format template to Phase 3 forces the model to commit to a relationship category before confirming the gap, not just name a vague relevance. This closes the format asymmetry: both phases now use the same ternary classification for INERTIA-REF comparisons, making either one reviewable by the same token-presence check.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first. EXECUTION DEPENDENCY follows. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root — no upstream dependency; slots 5 and 6 require this token before they can be filled |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 values at Phase 5 |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires slot 2 (Competitor Table complete before whitespace evaluation begins) |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding | Required by slot 5; must appear as the first row of the proof table before any reduction row |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence — what is lost if the focus dimension is dropped}] \| REDUCTION-2 NO: [{one sentence — what is lost if the competitive map is dropped}] \| THEREFORE: [{gap sentence requiring both dimensions simultaneously}]` | Phase 4 — Cross-Dimensional Finding | Requires slot 4 (SOURCE, first row) and slot 1 (INERTIA-REF) as comparator baseline; both must be written before THEREFORE |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 — Findings Table | Derived from slot 1 (INERTIA-REF, root) — slot 1 must be written at GATE 4 before Phase 5 runs |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### EXECUTION DEPENDENCY

Step-level execution ordering machine-readable before any gate is read. GATE 4 is the root step. A step listed in "Reads slot" must not begin until that slot has been written.

| Step | Reads slot | Writes slot | Execution constraint |
|------|-----------|------------|---------------------|
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and all other phases**; no phase may produce output until slot 1 is written |
| Phase 1 | — | TOPIC, FOCUS tokens | Runs after GATE 4; reads repo context before Phase 2 |
| Phase 2 (per competitor row) | 1 — INERTIA-REF (C0 row mechanism reference) | 2 — Anchor column value | Runs after Phase 1; GATE 1 and GATE 2 applied per row; slot 2 complete when all rows output |
| Phase 3 (per whitespace candidate) | 2 — Anchor column value (Competitor Table complete) | 3 — Absence evidence block | Runs after Phase 2 complete; WHITESPACE VALIDATION table (4 rows) per candidate attribute |
| Phase 4, SOURCE row | 2 — Anchor column value (named cell) | 4 — SOURCE slot | SOURCE row is row 1 of proof table; before any REDUCTION row |
| Phase 4, REDUCTION + THEREFORE rows | 4 — SOURCE slot (written), 1 — INERTIA-REF (comparator baseline) | 5 — Focus-scope evidence | Both REDUCTION rows answer NO before THEREFORE; slot 5 as pipe-delimited string on THEREFORE completion |
| Phase 5 (per finding row) | 1 — INERTIA-REF (DELTA column), 2 — Anchor column value (Anchor column) | 6 — INERTIA-REF-DELTA | Runs after Phase 4; GATE 4 row 3 applied per row |

An **execution dependency violation** occurs when a step begins before its declared "Reads slot" value has been written.

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
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without per-row attribute-level evidence does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "enforces synchronous kickoff calls — no fully async onboarding path exists"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is the first row of the Phase 4 proof table; slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS) is filled before any reduction row | **Proof structure failure** — SOURCE must be the first table row; any ordering that places a REDUCTION row before SOURCE is structurally malformed |
| Both reductions answer NO | REDUCTION-1 row and REDUCTION-2 row each contain "NO" with one sentence | **Proof structure failure** — both rows required; if either answers YES, discard the gap and find a different one |
| THEREFORE blocked until reductions complete | THEREFORE row written only after both REDUCTION rows answer NO | **Proof structure failure** — THEREFORE is blocked; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows before Phase 1. The write row fills slot 1 (INERTIA-REF, root, PREFLIGHT > OUTPUT CONTRACTS) — slots 5 and 6 depend on this token per "Required by" column; GATE 4 is the root step per PREFLIGHT > EXECUTION DEPENDENCY.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF, root, PREFLIGHT > OUTPUT CONTRACTS); root step complete (PREFLIGHT > EXECUTION DEPENDENCY); token now available to all phases; slots 5 and 6 require this token per "Required by" column | **Inertia write failure** — token must be written at this gate row, not deferred; return to this row and execute the write before Phase 1 begins |
| Per-finding citation required | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — fills slot 6 per finding row | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

C0 is the entity whose stickiness was resolved in GATE 4 (root step, PREFLIGHT > EXECUTION DEPENDENCY). C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2 before outputting.

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token (slot 1, root) — this data fills slot 6 (INERTIA-REF-DELTA) at Phase 5.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 2 (Competitor Table complete) per PREFLIGHT > EXECUTION DEPENDENCY. For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table. Rows must appear in order: CANDIDATE before ABSENCE-EVIDENCE before GAP-CONFIRMED before vs-INERTIA-REF. Complete all four rows before moving to the next candidate attribute.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — the candidate gap attribute under evaluation; declared before any absence evidence is gathered | **Whitespace naming failure** — declare the candidate attribute as the first row; an absent or unnamed CANDIDATE row blocks the ABSENCE-EVIDENCE row |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every competitor row (including C0) — fills slot 3 (Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS) | **Whitespace gate failure** — per-row evidence required for every competitor row; a bare assertion does not satisfy; every row must appear before GAP-CONFIRMED |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}] — attribute-level uncontested` — or — `Gap not confirmed: Row C{N} provides [{non-absent value}]; select a different candidate` | **Whitespace gate failure** — if any row provides a non-absent value, this candidate is not whitespace; stop, select a different attribute, restart the validation table |
| vs-INERTIA-REF | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — ternary token required; same format as slot 6 (INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS); one of the three tokens required before the mechanism phrase | **Whitespace INERTIA-REF format failure** — prose relationship description without ternary token does not satisfy; use slot 6 format template; "N/A" not permitted; "vs. INERTIA-REF — this gap is adjacent to C0's workflow" is not acceptable |

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion in ABSENCE-EVIDENCE row — **whitespace gate failure**
NOT ACCEPTABLE: "vs. INERTIA-REF — the vacant attribute is adjacent to C0's core workflow" — prose without ternary token — **whitespace INERTIA-REF format failure**
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before completing ABSENCE-EVIDENCE for all competitor rows — **whitespace gate failure**
ACCEPTABLE (vs-INERTIA-REF): `vs. INERTIA-REF — contextualizes: [C0 mechanism phrase] — the vacant attribute is absent even from C0, indicating a pre-market gap rather than a competitor-specific omission`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. Reads slot 2 (named cell) and slot 1 (INERTIA-REF comparator) per PREFLIGHT > EXECUTION DEPENDENCY. Execute all four rows in order. SOURCE is row 1.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — named cell from the competitor table; fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row | **Proof structure failure** — SOURCE must appear first; absent or malformed SOURCE blocks all subsequent rows |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped; the competitive map alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the competitive map alone; discard and find a different gap |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped; the focus dimension alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the focus dimension alone; discard and find a different gap |
| THEREFORE | `{one sentence naming the gap requiring both dimensions simultaneously}` — fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS): `REDUCTION-1 NO: [REDUCTION-1 sentence] \| REDUCTION-2 NO: [REDUCTION-2 sentence] \| THEREFORE: [THEREFORE sentence]` | **Proof structure failure** — THEREFORE blocked until both REDUCTION rows answer NO; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. Reads slot 1 (INERTIA-REF) and slot 2 (Anchor values) per PREFLIGHT > EXECUTION DEPENDENCY. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only entries are syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C2, focus-column: "no self-serve trial — requires sales-qualified lead before demo access"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — every finding row must cite INERTIA-REF by token name; "N/A" is malformed.

For the cross-dimensional finding row: Claim = THEREFORE sentence; Anchor = SOURCE value; adjacent indented block = slot 5 pipe-delimited proof string — apply GATE 3.

---

### AMEND

Execute exactly 3 adjustment rows. Each row names the adjustment, what the user changes, what changes in the output, which output contract slots are re-filled, and which gates re-run.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` in FOCUS CHECK | SOURCE slot re-identified; Focus-scope evidence (slot 5) rebuilt from scratch: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` — both reduction sentences rebuilt; THEREFORE rewritten; cross-dimensional finding row updated | 4 (SOURCE), 5 (Focus-scope evidence) | GATE 3 (all rows: SOURCE first, both reductions answer NO, THEREFORE blocked) — writing a new THEREFORE without rerunning both reductions is a **proof rerun failure**; slot 5 re-filled only when all three pipe-delimited components conform |
| 2 | Add competitor | Competitor name + context for WebSearch | New competitor row (slot 2); WHITESPACE VALIDATION table re-run for all candidate attributes — vs-INERTIA-REF row in each table instance must use slot 6 ternary-token format; slot 3 re-evaluated; INERTIA-REF-DELTA (slot 6) reviewed for existing findings | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation for new row), GATE 2 (anchor format for new row; ABSENCE-EVIDENCE rows for all whitespace candidate attributes) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase — product feature, workflow step, or workaround behavior | INERTIA-REF token (slot 1) re-written at GATE 4 write row; all Phase 5 INERTIA-REF-DELTA cells (slot 6) updated; Phase 3 vs-INERTIA-REF rows reviewed — each re-classified using updated phrase in slot 6 ternary-token format; Phase 4 proof table reviewed — if baseline shifts, rebuild all four proof rows | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA, all finding rows), 3 (vs-INERTIA-REF rows re-classified against updated phrase), 5 (Focus-scope evidence, if baseline shifts) | GATE 4 (all rows: stickiness check, write row, per-finding citation), GATE 3 (if slot 5 rebuild required) |

---

## V-03 — Inertia framing (EXECUTION DEPENDENCY gains "Prerequisite steps" column)

**Axis:** Inertia framing — the EXECUTION DEPENDENCY table gains a fifth column: "Prerequisite steps." This column names, for each step, which steps (by step name) must have completed before it begins — independently of which slots it reads. GATE 4 has "None (root)" in both Reads slot and Prerequisite steps, confirming root status from two orthogonal angles without requiring inference. Other steps name the specific prior step. This makes step-level ordering doubly machine-readable: ordering is verifiable by tracing either slot dependencies (Reads/Writes) or step dependencies (Prerequisite steps) without cross-referencing.

**Hypothesis:** The current EXECUTION DEPENDENCY table makes step ordering readable via slot dependencies — to determine if Phase 3 follows Phase 2, a reader traces that Phase 2 writes slot 2, and Phase 3 reads slot 2. This requires two-row cross-reference. The "Prerequisite steps" column eliminates the cross-reference: Phase 3's row directly says "Phase 2." GATE 4's "None (root)" in this column is a structural declaration requiring zero inference. Together, GATE 4 is confirmed as the execution root from three independent structural positions: OUTPUT CONTRACTS "Required by" (slot root), EXECUTION DEPENDENCY "Reads slot" (data root), and EXECUTION DEPENDENCY "Prerequisite steps: None" (step root). No other step has triple root confirmation.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first. EXECUTION DEPENDENCY follows — step ordering and step prerequisites readable before Phase 1. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root — no upstream dependency; slots 5 and 6 require this token before they can be filled |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 values at Phase 5 |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires slot 2 (Competitor Table complete before whitespace evaluation begins) |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding | Required by slot 5; must appear as the first row of the proof table before any reduction row |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence — what is lost if the focus dimension is dropped}] \| REDUCTION-2 NO: [{one sentence — what is lost if the competitive map is dropped}] \| THEREFORE: [{gap sentence requiring both dimensions simultaneously}]` | Phase 4 — Cross-Dimensional Finding | Requires slot 4 (SOURCE, first row) and slot 1 (INERTIA-REF) as comparator baseline; both must be written before THEREFORE |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 — Findings Table | Derived from slot 1 (INERTIA-REF, root) — slot 1 must be written at GATE 4 before Phase 5 runs |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### EXECUTION DEPENDENCY

Step-level execution ordering with two independent readability paths: "Reads slot" (data dependency) and "Prerequisite steps" (step dependency). GATE 4 is confirmed as root from both columns — "None (root)" in each. An **execution dependency violation** occurs when a step begins before its "Reads slot" slot is written OR before its "Prerequisite steps" step has completed.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and all other phases**; no phase may produce output until slot 1 is written | None (root) |
| Phase 1 | — | TOPIC, FOCUS tokens | Reads repo context; outputs TOPIC and FOCUS before Phase 2 | GATE 4 |
| Phase 2 (per competitor row) | 1 — INERTIA-REF (C0 row mechanism reference) | 2 — Anchor column value | GATE 1 and GATE 2 applied per row; slot 2 complete when all rows output | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 — Anchor column value (Competitor Table complete) | 3 — Absence evidence block | WHITESPACE VALIDATION table (4 rows) per candidate attribute; all rows complete before next attribute | Phase 2 |
| Phase 4, SOURCE row | 2 — Anchor column value (named cell from competitor table) | 4 — SOURCE slot | SOURCE row is row 1 of proof table; must be written before any REDUCTION row | Phase 3 |
| Phase 4, REDUCTION + THEREFORE rows | 4 — SOURCE slot (written), 1 — INERTIA-REF (comparator baseline) | 5 — Focus-scope evidence | Both REDUCTION rows answer NO before THEREFORE; slot 5 as pipe-delimited string on THEREFORE completion | Phase 4 SOURCE row |
| Phase 5 (per finding row) | 1 — INERTIA-REF (DELTA column), 2 — Anchor column value (Anchor column) | 6 — INERTIA-REF-DELTA | GATE 4 row 3 (per-finding citation) applied per row; all finding rows complete before AMEND | Phase 4 |

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
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without per-row attribute-level evidence does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "requires all integrations to use REST polling — no webhook delivery pathway available"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is the first row of the Phase 4 proof table; slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS) is filled before any reduction row | **Proof structure failure** — SOURCE must be the first table row; any ordering that places a REDUCTION row before SOURCE is structurally malformed |
| Both reductions answer NO | REDUCTION-1 row and REDUCTION-2 row each contain "NO" with one sentence | **Proof structure failure** — both rows required; if either answers YES, discard the gap and find a different one |
| THEREFORE blocked until reductions complete | THEREFORE row written only after both REDUCTION rows answer NO | **Proof structure failure** — THEREFORE is blocked; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows before Phase 1. This is the root step: PREFLIGHT > EXECUTION DEPENDENCY, Prerequisite steps column: "None (root)"; slot 1 (INERTIA-REF) is the root dependency per PREFLIGHT > OUTPUT CONTRACTS "Required by" column.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF, root, PREFLIGHT > OUTPUT CONTRACTS); root step complete (PREFLIGHT > EXECUTION DEPENDENCY — "Prerequisite steps: None (root)"); token now available to all phases | **Inertia write failure** — token must be written at this gate row; return to this row and execute the write before Phase 1 begins |
| Per-finding citation required | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — fills slot 6 per finding row | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### PHASE 1: CONTEXT

Runs after GATE 4 (PREFLIGHT > EXECUTION DEPENDENCY, Prerequisite steps: GATE 4). Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 1 (PREFLIGHT > EXECUTION DEPENDENCY, Prerequisite steps: Phase 1). C0 is the entity whose stickiness was resolved in GATE 4 (root step — "Prerequisite steps: None (root)"). C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2 before outputting.

Note which mechanism phrases and focus-column values relate to INERTIA-REF (slot 1, root) — fills slot 6 ("Required by: slot 1") at Phase 5 per PREFLIGHT > EXECUTION DEPENDENCY.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 2 (PREFLIGHT > EXECUTION DEPENDENCY, Prerequisite steps: Phase 2). Reads slot 2 (Competitor Table complete). For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table. Rows in order: CANDIDATE before ABSENCE-EVIDENCE before GAP-CONFIRMED before vs-INERTIA-REF.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — the candidate gap attribute; declared before any absence evidence is gathered | **Whitespace naming failure** — declare the candidate attribute as the first row; absent or unnamed CANDIDATE blocks the ABSENCE-EVIDENCE row |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every competitor row (including C0) — fills slot 3 (PREFLIGHT > OUTPUT CONTRACTS) | **Whitespace gate failure** — per-row evidence required for every row; bare assertion does not satisfy; every row must appear before GAP-CONFIRMED |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}] — attribute-level uncontested` — or — `Gap not confirmed: Row C{N} provides [{non-absent value}]; select a different candidate` | **Whitespace gate failure** — if any row provides a non-absent value, stop, select a different attribute, restart the validation table |
| vs-INERTIA-REF | `vs. INERTIA-REF — {how the vacant attribute relates to the C0 mechanism phrase from slot 1}` | **Whitespace INERTIA-REF failure** — every gap finding must name its relationship to the INERTIA-REF mechanism; "N/A" not permitted as the final row |

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before completing ABSENCE-EVIDENCE for all competitor rows — **whitespace gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 3 (PREFLIGHT > EXECUTION DEPENDENCY, Prerequisite steps: Phase 3 / Phase 4 SOURCE row). Apply GATE 3. Execute all four rows in order. SOURCE is row 1.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row | **Proof structure failure** — SOURCE must appear first; absent or malformed SOURCE blocks all subsequent rows |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped; the competitive map alone does not produce this gap}` | **Proof structure failure** — if YES, gap is single-dimension sufficient from the map; discard |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped; the focus dimension alone does not produce this gap}` | **Proof structure failure** — if YES, gap is single-dimension sufficient from focus; discard |
| THEREFORE | `{one sentence naming the gap requiring both dimensions simultaneously}` — fills slot 5: `REDUCTION-1 NO: [REDUCTION-1 sentence] \| REDUCTION-2 NO: [REDUCTION-2 sentence] \| THEREFORE: [THEREFORE sentence]` | **Proof structure failure** — THEREFORE blocked until both REDUCTION rows answer NO; retroactive construction is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 4 (PREFLIGHT > EXECUTION DEPENDENCY, Prerequisite steps: Phase 4). Write 2-5 findings. Reads slot 1 (INERTIA-REF) and slot 2 (Anchor values). Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only entries are malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no API tier in SMB plan — webhook access gated behind enterprise contract"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — every finding row must cite INERTIA-REF by token name; "N/A" is malformed.

For the cross-dimensional finding row: Claim = THEREFORE sentence; Anchor = SOURCE value; adjacent indented block = slot 5 pipe-delimited proof string — apply GATE 3.

---

### AMEND

Execute exactly 3 adjustment rows. Slot re-fill and gate re-run are queryable columns — a row without both populated does not conform.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` in FOCUS CHECK | SOURCE slot re-identified; Focus-scope evidence (slot 5) rebuilt: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` — both reductions rebuilt per PREFLIGHT > EXECUTION DEPENDENCY (Phase 4 REDUCTION + THEREFORE rows, Prerequisite steps: Phase 4 SOURCE row); THEREFORE rewritten; cross-dimensional finding updated | 4 (SOURCE), 5 (Focus-scope evidence) | GATE 3 (all rows: SOURCE first, both reductions answer NO, THEREFORE blocked) — writing a new THEREFORE without rerunning both reductions is a **proof rerun failure** |
| 2 | Add competitor | Competitor name + context for WebSearch | New competitor row (slot 2); WHITESPACE VALIDATION table re-run per PREFLIGHT > EXECUTION DEPENDENCY (Phase 3, Prerequisite steps: Phase 2 complete); slot 3 re-evaluated; INERTIA-REF-DELTA (slot 6) reviewed | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation for new row), GATE 2 (anchor format for new row; ABSENCE-EVIDENCE rows for all whitespace candidate attributes) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase — product feature, workflow step, or workaround behavior | INERTIA-REF token (slot 1) re-written at GATE 4 write row (root step, PREFLIGHT > EXECUTION DEPENDENCY — Prerequisite steps: None (root)); all Phase 5 INERTIA-REF-DELTA cells (slot 6) updated; Phase 4 proof table reviewed — if baseline shifts, rebuild all four rows per PREFLIGHT > EXECUTION DEPENDENCY step sequence | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA, all finding rows), 5 (Focus-scope evidence, if baseline shifts) | GATE 4 (all rows: stickiness check, write row, per-finding citation), GATE 3 (if slot 5 rebuild required) |

---

## V-04 — Combined: FOCUS GATE + vs-INERTIA-REF slot 6 format (Axes A + B)

**Axis:** Role sequence + Output format — FOCUS CHECK as GATE 0 inside PREFLIGHT (V-01 axis) combined with Phase 3 vs-INERTIA-REF row coerced to slot 6 format template (V-02 axis). No Prerequisite steps column added to EXECUTION DEPENDENCY.

**Hypothesis:** GATE 0 closes the PREFLIGHT completeness gap: the focus conditionality is now a gate with named failure states. The vs-INERTIA-REF format coercion closes the Phase 3 format asymmetry: whitespace-level and finding-level INERTIA-REF comparisons use identical ternary-token syntax. These two axes target different enforcement boundaries (pre-execution state determination and per-candidate evidence format) and compose without interaction. Together, every gate-level decision and every INERTIA-REF comparison in the skill has a machine-readable specification.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first. GATE 0 (FOCUS GATE) follows. EXECUTION DEPENDENCY follows. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root — no upstream dependency; slots 5 and 6 require this token before they can be filled |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 values at Phase 5 |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires slot 2 (Competitor Table complete before whitespace evaluation begins) |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding | Required by slot 5; must appear as the first row of the proof table before any reduction row |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence — what is lost if the focus dimension is dropped}] \| REDUCTION-2 NO: [{one sentence — what is lost if the competitive map is dropped}] \| THEREFORE: [{gap sentence requiring both dimensions simultaneously}]` — or vacuous satisfaction when GATE 0 focus-inactive branch applies | Phase 4 — Cross-Dimensional Finding | Requires slot 4 (SOURCE) and slot 1 (INERTIA-REF) when focus is active (see GATE 0); vacuous when focus is inactive |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 — Findings Table | Derived from slot 1 (INERTIA-REF, root) — slot 1 must be written at GATE 4 before Phase 5 runs |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### GATE 0: FOCUS GATE

Resolve focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all three rows before proceeding.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` is set to a recognized value (`market-sizing`, `positioning-framework`) — OR — `focus:` is not set; infer from repo context before defaulting to none | **Focus detection failure** — unrecognized or ambiguous focus value; resolve to a recognized value or omit before proceeding |
| Focus-active branch | When focus is set: Focus column added to Phase 2 competitor table header; slot 5 fills as full pipe-delimited proof string; Phase 4 proof table required; GATE 3 applies; cross-dimensional criteria are live | **Focus activation failure** — focus is active but Focus column omitted or slot 5 declared vacuously; both required when focus is set |
| Focus-inactive branch | When focus is not set: Focus column not added to Phase 2 table; slot 5 satisfies by vacuous satisfaction; Phase 4 still runs; THEREFORE does not require cross-dimensional necessity argument | **Focus inactivation failure** — Focus column present in competitor table when focus is not set; remove before outputting |

---

### EXECUTION DEPENDENCY

Step-level execution ordering machine-readable before any numbered gate is read. GATE 4 is the root step.

| Step | Reads slot | Writes slot | Execution constraint |
|------|-----------|------------|---------------------|
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and all other phases**; no phase may produce output until slot 1 is written |
| Phase 1 | — | TOPIC, FOCUS tokens | Runs after GATE 4; reads repo context |
| Phase 2 (per competitor row) | 1 — INERTIA-REF | 2 — Anchor column value | Runs after Phase 1; GATE 1 and GATE 2 applied per row; Focus column per GATE 0 |
| Phase 3 (per whitespace candidate) | 2 — Anchor column value | 3 — Absence evidence block | Runs after Phase 2 complete; WHITESPACE VALIDATION table (4 rows) per candidate; vs-INERTIA-REF row uses slot 6 ternary-token format |
| Phase 4, SOURCE row | 2 — Anchor column value | 4 — SOURCE slot | SOURCE row 1 of proof table; before any REDUCTION row |
| Phase 4, REDUCTION + THEREFORE rows | 4 — SOURCE slot, 1 — INERTIA-REF | 5 — Focus-scope evidence | Both reductions NO before THEREFORE; slot 5 as pipe-delimited; vacuous if GATE 0 focus-inactive |
| Phase 5 (per finding row) | 1 — INERTIA-REF, 2 — Anchor column value | 6 — INERTIA-REF-DELTA | Runs after Phase 4; GATE 4 row 3 per finding row |

An **execution dependency violation** occurs when a step begins before its declared "Reads slot" value has been written.

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
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without per-row attribute-level evidence does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "no persistent async record — review feedback lives only inside the PR diff"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is the first row of the Phase 4 proof table; slot 4 filled before any reduction row | **Proof structure failure** — SOURCE must be the first table row |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** — both rows required; if either answers YES, discard |
| THEREFORE blocked until reductions complete | THEREFORE row written only after both REDUCTION rows answer NO | **Proof structure failure** — retroactive construction is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows before Phase 1. The write row fills slot 1 (root) per PREFLIGHT > OUTPUT CONTRACTS "Required by" column; GATE 4 is the root step per PREFLIGHT > EXECUTION DEPENDENCY.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve before the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF, root, PREFLIGHT > OUTPUT CONTRACTS); root step complete (PREFLIGHT > EXECUTION DEPENDENCY); token now available to all phases | **Inertia write failure** — token must be written at this gate row; return to this row before Phase 1 begins |
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

C0 is the entity whose stickiness was resolved in GATE 4 (root step). C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column present or absent per GATE 0.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only cells are syntactically malformed; apply GATE 2.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 2 (Competitor Table complete). For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table. Rows in order: CANDIDATE before ABSENCE-EVIDENCE before GAP-CONFIRMED before vs-INERTIA-REF.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — declared before any absence evidence is gathered | **Whitespace naming failure** — declare the candidate attribute as the first row; absent or unnamed CANDIDATE blocks ABSENCE-EVIDENCE |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every competitor row (including C0) — fills slot 3 (PREFLIGHT > OUTPUT CONTRACTS) | **Whitespace gate failure** — per-row evidence required for every row; bare assertion does not satisfy; every row before GAP-CONFIRMED |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}] — attribute-level uncontested` — or — `Gap not confirmed: Row C{N} provides [{non-absent value}]; select a different candidate` | **Whitespace gate failure** — if any row provides a non-absent value, stop, select a different attribute, restart the validation table |
| vs-INERTIA-REF | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — ternary token required; same format as slot 6 (INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS) | **Whitespace INERTIA-REF format failure** — prose relationship description without ternary token does not satisfy; use slot 6 format template; "N/A" not permitted |

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "vs. INERTIA-REF — this gap does not directly relate to C0's workflow" — prose without ternary token — **whitespace INERTIA-REF format failure**
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before completing ABSENCE-EVIDENCE for all rows — **whitespace gate failure**
ACCEPTABLE (vs-INERTIA-REF): `vs. INERTIA-REF — reinforces: [C0 mechanism phrase] — the vacant attribute is the same gap C0 exploits; no competitor has addressed it either`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. Execute all four rows in order. SOURCE is row 1. If GATE 0 focus-inactive branch applies, slot 5 satisfies by vacuous satisfaction.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — fills slot 4 (PREFLIGHT > OUTPUT CONTRACTS); must be the first row | **Proof structure failure** — SOURCE must appear first; absent or malformed SOURCE blocks all subsequent rows |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped}` | **Proof structure failure** — if YES, gap is single-dimension sufficient from the map; discard |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped}` | **Proof structure failure** — if YES, gap is single-dimension sufficient from focus; discard |
| THEREFORE | `{one sentence naming the gap requiring both dimensions simultaneously}` — fills slot 5: `REDUCTION-1 NO: [REDUCTION-1 sentence] \| REDUCTION-2 NO: [REDUCTION-2 sentence] \| THEREFORE: [THEREFORE sentence]` | **Proof structure failure** — THEREFORE blocked until both reductions answer NO; retroactive construction is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. Reads slot 1 (INERTIA-REF) and slot 2 (Anchor values). Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only entries are malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C2, mechanism: "bundles feedback inside PR diff — no async record outside PR lifecycle"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — every finding row must cite INERTIA-REF by token name; "N/A" is malformed.

For the cross-dimensional finding row: Claim = THEREFORE sentence; Anchor = SOURCE value; adjacent indented block = slot 5 pipe-delimited proof string — apply GATE 3.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` — re-run GATE 0 focus-active branch | SOURCE slot re-identified; Focus-scope evidence (slot 5) rebuilt: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` — both reduction sentences rebuilt; THEREFORE rewritten; cross-dimensional finding updated | 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (focus-active branch re-confirmed), GATE 3 (all rows) — writing a new THEREFORE without rerunning both reductions is a **proof rerun failure** |
| 2 | Add competitor | Competitor name + context for WebSearch | New competitor row (slot 2); WHITESPACE VALIDATION table re-run — vs-INERTIA-REF row must use slot 6 ternary-token format; slot 3 re-evaluated; INERTIA-REF-DELTA (slot 6) reviewed | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation for new row), GATE 2 (anchor format; ABSENCE-EVIDENCE for all whitespace attributes) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | INERTIA-REF token (slot 1) re-written at GATE 4 write row; all Phase 5 INERTIA-REF-DELTA cells (slot 6) updated; Phase 3 vs-INERTIA-REF rows re-classified using updated phrase in ternary-token format; Phase 4 proof reviewed — if baseline shifts, rebuild all four proof rows | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows re-classified), 5 (Focus-scope evidence, if baseline shifts) | GATE 4 (all rows), GATE 3 (if slot 5 rebuild required) |

---

## V-05 — Combined maximum (FOCUS GATE + vs-INERTIA-REF slot 6 format + Prerequisite steps column)

**Axis:** Combined maximum — all three R10 innovation axes. FOCUS CHECK as GATE 0 inside PREFLIGHT (V-01). Phase 3 vs-INERTIA-REF row coerced to slot 6 ternary-token format (V-02). EXECUTION DEPENDENCY gains "Prerequisite steps" column (V-03). Every pre-execution decision is a gate. Every INERTIA-REF comparison uses the same ternary syntax. Step ordering is readable from two independent columns.

**Hypothesis:** GATE 0 moves the last prose pre-execution check into the gate system. The ternary-token format coercion makes Phase 3 and Phase 5 INERTIA-REF comparisons syntactically isomorphic. The "Prerequisite steps" column makes the step DAG readable by step name without slot-tracing. GATE 4's root status is now confirmed from four independent structural positions: OUTPUT CONTRACTS "Required by" (slot root), EXECUTION DEPENDENCY "Reads slot" (data root), EXECUTION DEPENDENCY "Prerequisite steps: None" (step root), and GATE 0 which determines the execution start state before the DAG is read. A reader can reconstruct the complete execution contract by reading PREFLIGHT alone — no phase instruction required.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first. GATE 0 (FOCUS GATE) follows — focus state resolved before step ordering is read. EXECUTION DEPENDENCY follows. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root — no upstream dependency; slots 5 and 6 require this token before they can be filled |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 values at Phase 5 |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires slot 2 (Competitor Table complete before whitespace evaluation begins) |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding | Required by slot 5; must appear as the first row of the proof table before any reduction row |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence — what is lost if the focus dimension is dropped}] \| REDUCTION-2 NO: [{one sentence — what is lost if the competitive map is dropped}] \| THEREFORE: [{gap sentence requiring both dimensions simultaneously}]` — or vacuous satisfaction when GATE 0 focus-inactive branch applies | Phase 4 — Cross-Dimensional Finding | Requires slot 4 (SOURCE) and slot 1 (INERTIA-REF) when focus is active (see GATE 0); vacuous when focus is inactive |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 — Findings Table | Derived from slot 1 (INERTIA-REF, root) — slot 1 must be written at GATE 4 before Phase 5 runs |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### GATE 0: FOCUS GATE

Resolve focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all three rows before proceeding. The focus state determines which branch of slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS) applies.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` is set to a recognized value (`market-sizing`, `positioning-framework`) — OR — `focus:` is not set; infer from repo context (README, CLAUDE.md) before defaulting to none | **Focus detection failure** — unrecognized or ambiguous focus value; resolve to a recognized value or omit before proceeding; do not proceed until focus state is confirmed |
| Focus-active branch | When focus is set: Focus column added to Phase 2 competitor table header; slot 5 (Focus-scope evidence) fills as full pipe-delimited proof string (`REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`); Phase 4 proof table required; GATE 3 applies; cross-dimensional criteria are live | **Focus activation failure** — focus is active but Focus column omitted from Phase 2 table or slot 5 declared vacuously; both required when focus is set |
| Focus-inactive branch | When focus is not set: Focus column not added to Phase 2 table; slot 5 satisfies by vacuous satisfaction; Phase 4 still runs; THEREFORE does not require cross-dimensional necessity argument | **Focus inactivation failure** — Focus column present in competitor table when focus is not set; remove column from Phase 2 header before outputting |

---

### EXECUTION DEPENDENCY

Step-level execution ordering with two independent readability paths. GATE 4 is confirmed as root from both "Reads slot" (empty = root) and "Prerequisite steps: None (root)". An **execution dependency violation** occurs when a step begins before its "Reads slot" slot is written OR before its "Prerequisite steps" step has completed.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and all other phases**; no phase may produce output until slot 1 is written | None (root) |
| Phase 1 | — | TOPIC, FOCUS tokens | Reads repo context; outputs TOPIC and FOCUS before Phase 2 | GATE 4 |
| Phase 2 (per competitor row) | 1 — INERTIA-REF (C0 row mechanism reference) | 2 — Anchor column value | GATE 1 and GATE 2 applied per row; slot 2 complete when all rows output; Focus column per GATE 0 | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 — Anchor column value (Competitor Table complete) | 3 — Absence evidence block | WHITESPACE VALIDATION table (4 rows) per candidate; vs-INERTIA-REF row uses slot 6 ternary-token format | Phase 2 |
| Phase 4, SOURCE row | 2 — Anchor column value (named cell from competitor table) | 4 — SOURCE slot | SOURCE row is row 1 of proof table; before any REDUCTION row | Phase 3 |
| Phase 4, REDUCTION + THEREFORE rows | 4 — SOURCE slot (written), 1 — INERTIA-REF (comparator baseline) | 5 — Focus-scope evidence | Both REDUCTION rows answer NO before THEREFORE; slot 5 as pipe-delimited; vacuous if GATE 0 focus-inactive | Phase 4 SOURCE row |
| Phase 5 (per finding row) | 1 — INERTIA-REF (DELTA column), 2 — Anchor column value (Anchor column) | 6 — INERTIA-REF-DELTA | GATE 4 row 3 (per-finding citation) applied per row | Phase 4 |

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
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without per-row attribute-level evidence does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff — no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is the first row of the Phase 4 proof table; slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS) is filled before any reduction row | **Proof structure failure** — SOURCE must be the first table row; any ordering that places a REDUCTION row before SOURCE is structurally malformed |
| Both reductions answer NO | REDUCTION-1 row and REDUCTION-2 row each contain "NO" with one sentence | **Proof structure failure** — both rows required; if either answers YES, discard the gap and find a different one |
| THEREFORE blocked until reductions complete | THEREFORE row written only after both REDUCTION rows answer NO | **Proof structure failure** — THEREFORE is blocked; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows before Phase 1. Root step: "Prerequisite steps: None (root)" per PREFLIGHT > EXECUTION DEPENDENCY; slot 1 (INERTIA-REF) is the root slot per PREFLIGHT > OUTPUT CONTRACTS "Required by" column; GATE 0 determined the execution start state.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF, root, PREFLIGHT > OUTPUT CONTRACTS); root step complete (PREFLIGHT > EXECUTION DEPENDENCY — Prerequisite steps: None (root)); token now available to all phases; slots 5 and 6 require this token per "Required by" column | **Inertia write failure** — token must be written at this gate row, not deferred; return to this row and execute the write before Phase 1 begins |
| Per-finding citation required | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — fills slot 6 (INERTIA-REF-DELTA) per finding row | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### PHASE 1: CONTEXT

Runs after GATE 4 (PREFLIGHT > EXECUTION DEPENDENCY, Prerequisite steps: GATE 4). Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 1 (PREFLIGHT > EXECUTION DEPENDENCY, Prerequisite steps: Phase 1). C0 is the entity whose stickiness was resolved in GATE 4 (root step — "Prerequisite steps: None (root)"). C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting. Focus column present or absent per GATE 0 (PREFLIGHT).

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2 before outputting.

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token (slot 1, root) — fills slot 6 (INERTIA-REF-DELTA, "Required by: slot 1") at Phase 5 per PREFLIGHT > EXECUTION DEPENDENCY.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 2 (PREFLIGHT > EXECUTION DEPENDENCY, Prerequisite steps: Phase 2). Reads slot 2 (Competitor Table complete). For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table. Rows in order: CANDIDATE before ABSENCE-EVIDENCE before GAP-CONFIRMED before vs-INERTIA-REF. Complete all four rows before the next candidate attribute.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — the candidate gap attribute; declared before any absence evidence is gathered | **Whitespace naming failure** — declare the candidate attribute as the first row; absent or unnamed CANDIDATE blocks the ABSENCE-EVIDENCE row |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every competitor row (including C0) — fills slot 3 (Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS) | **Whitespace gate failure** — per-row evidence required for every competitor row; bare assertion does not satisfy; every row before GAP-CONFIRMED |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}] — attribute-level uncontested` — or — `Gap not confirmed: Row C{N} provides [{non-absent value}]; select a different candidate` | **Whitespace gate failure** — if any row provides a non-absent value, stop, select a different attribute, restart the validation table |
| vs-INERTIA-REF | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — ternary token required; same format as slot 6 (INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS); one of three tokens required before the mechanism phrase | **Whitespace INERTIA-REF format failure** — prose relationship description without ternary token does not satisfy; use slot 6 format template; "N/A" not permitted; arbitrary prose without ternary token not permitted |

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion in ABSENCE-EVIDENCE row — **whitespace gate failure**
NOT ACCEPTABLE: "vs. INERTIA-REF — the vacant attribute is adjacent to C0's core workflow" — prose without ternary token — **whitespace INERTIA-REF format failure**
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before completing ABSENCE-EVIDENCE for all competitor rows — **whitespace gate failure**
ACCEPTABLE (vs-INERTIA-REF): `vs. INERTIA-REF — challenges: [C0 mechanism phrase] — the vacant attribute would displace the C0 workaround if a competitor offered it`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 3 (PREFLIGHT > EXECUTION DEPENDENCY, Prerequisite steps: Phase 3 / Phase 4 SOURCE row). Apply GATE 3. Execute all four rows in order. SOURCE is row 1. If GATE 0 focus-inactive branch applies, slot 5 satisfies by vacuous satisfaction.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — named cell from the competitor table; fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row | **Proof structure failure** — SOURCE row must appear first; absent or malformed SOURCE blocks all subsequent rows |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped; the competitive map alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the competitive map alone; discard and find a different gap |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped; the focus dimension alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the focus dimension alone; discard and find a different gap |
| THEREFORE | `{one sentence naming the gap that requires both dimensions simultaneously}` — fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS): `REDUCTION-1 NO: [REDUCTION-1 sentence] \| REDUCTION-2 NO: [REDUCTION-2 sentence] \| THEREFORE: [THEREFORE sentence]` | **Proof structure failure** — THEREFORE is blocked until both REDUCTION rows answer NO; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 4 (PREFLIGHT > EXECUTION DEPENDENCY, Prerequisite steps: Phase 4). Write 2-5 findings. Reads slot 1 (INERTIA-REF) and slot 2 (Anchor values) per PREFLIGHT > EXECUTION DEPENDENCY. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only entries are syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier — enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — every finding row must cite INERTIA-REF by token name; "N/A" is malformed.

For the cross-dimensional finding row: Claim = THEREFORE sentence; Anchor = SOURCE value; adjacent indented block contains slot 5 pipe-delimited proof string — apply GATE 3.

---

### AMEND

Execute exactly 3 adjustment rows. Each row names the adjustment, what the user changes, what changes in the output, which output contract slots are re-filled, and which gates re-run. A row without populated "Slots re-filled" and "Gates re-run" columns does not conform.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` — re-run GATE 0 focus-active branch with new value | SOURCE slot re-identified from updated focus; Focus-scope evidence (slot 5) rebuilt: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` — both reduction sentences rebuilt per PREFLIGHT > EXECUTION DEPENDENCY (Phase 4 REDUCTION + THEREFORE rows, Prerequisite steps: Phase 4 SOURCE row); THEREFORE rewritten; cross-dimensional finding row updated in Phase 5 | 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (focus-active branch re-confirmed with new focus value), GATE 3 (all rows: SOURCE first, both reductions answer NO, THEREFORE blocked) — writing a new THEREFORE without rerunning both reductions is a **proof rerun failure**; slot 5 re-filled only when all three pipe-delimited components conform |
| 2 | Add competitor | Competitor name + context for WebSearch | New competitor row (slot 2); WHITESPACE VALIDATION table re-run for all candidate attributes per PREFLIGHT > EXECUTION DEPENDENCY (Phase 3, Prerequisite steps: Phase 2 complete) — vs-INERTIA-REF row in each table instance must use slot 6 ternary-token format; slot 3 re-evaluated; INERTIA-REF-DELTA (slot 6) reviewed for existing findings | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation for new row), GATE 2 (anchor format for new row; ABSENCE-EVIDENCE rows for all whitespace candidate attributes) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase — product feature, workflow step, or workaround behavior | INERTIA-REF token (slot 1) re-written at GATE 4 write row (root step, PREFLIGHT > EXECUTION DEPENDENCY — Prerequisite steps: None (root)); all Phase 5 INERTIA-REF-DELTA cells (slot 6) updated; Phase 3 vs-INERTIA-REF rows reviewed — each re-classified using updated phrase in slot 6 ternary-token format; Phase 4 proof table reviewed — if new phrase shifts cross-dimensional baseline, rebuild all four proof rows | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA, all finding rows), 3 (vs-INERTIA-REF rows re-classified against updated phrase), 5 (Focus-scope evidence, if baseline shifts) | GATE 4 (all rows: stickiness check, write row, per-finding citation), GATE 3 (if slot 5 rebuild required: SOURCE, both reductions, THEREFORE) |

---

```json
{"round": 10, "baseline": "R9 V-05 (C-37 + C-38 + C-39)", "new_axes": ["FOCUS GATE as named gate within PREFLIGHT — focus conditionality machine-readable at gate level with explicit activation/inactivation branch failure states; moves last prose pre-execution check into the structural gate system", "Phase 3 vs-INERTIA-REF row coerced to slot 6 ternary-token format — whitespace-level and finding-level INERTIA-REF comparisons syntactically isomorphic; ternary commitment required before confirming gap", "EXECUTION DEPENDENCY Prerequisite steps column — step ordering doubly readable from slot-read traces and step-name prerequisites; GATE 4 root confirmed from four independent structural positions"], "candidate_criteria": ["C-40: FOCUS GATE as named gate in PREFLIGHT with PASS/FAIL table (detection + activation + inactivation rows, slot consequences per branch)", "C-41: Phase 3 vs-INERTIA-REF row uses slot 6 ternary-token format (reinforces / challenges / contextualizes + mechanism phrase)", "C-42: EXECUTION DEPENDENCY Prerequisite steps column names upstream steps by step name; GATE 4 = None (root)"]}
```
