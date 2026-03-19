Written to `simulations/quest/variations/discover-competitors-alt-variations-R9-2026-03-17.md`.

---

## discover-competitors-alt — R9 Variations Summary

All 5 variations target **230/230** on rubric v8. C-34/C-35/C-36 are the universal baseline (absorbed from R8 V-01, V-02, V-03 respectively).

| Variation | Axis | Key structural innovation |
|-----------|------|--------------------------|
| **V-01** | Lifecycle emphasis | Phase 3 WHITESPACE as 4-row PASS/FAIL table: CANDIDATE → ABSENCE-EVIDENCE → GAP-CONFIRMED → vs-INERTIA-REF |
| **V-02** | Output format | AMEND as 6-column structured table: # / Adjustment / What user changes / What changes in output / Slots re-filled / Gates re-run |
| **V-03** | Inertia framing | EXECUTION DEPENDENCY table in PREFLIGHT (after OUTPUT CONTRACTS, before GATE 1): step-to-step DAG with Reads slot / Writes slot / Execution constraint |
| **V-04** | A + B | WHITESPACE table + AMEND table |
| **V-05** | Maximum | All three axes |

**C-34/C-35/C-36 universal baseline** — all 5 variations have the "Required by" column, pipe-delimited slot 5 template, and 4-row Phase 4 proof table.

**Three candidate new criteria exposed by R9 axes:**
- **C-37**: WHITESPACE phase as named 4-row PASS/FAIL table — CANDIDATE declared first by table row order (same principle as C-36 for SOURCE)
- **C-38**: AMEND as structured table — slot obligations and gate re-runs are queryable columns, not prose
- **C-39**: EXECUTION DEPENDENCY table in PREFLIGHT — step-level DAG complements C-34's slot-level "Required by" column
 THEREFORE: [...]` in all 5
- C-36: Phase 4 is a 4-row PASS/FAIL table (SOURCE / REDUCTION-1 / REDUCTION-2 / THEREFORE) with required value format and named failure state per row in all 5

**New single-axis targets (R9 innovation axes):**
- **Axis A** (V-01): WHITESPACE-VALIDATION table — Phase 3 gains same structural enforcement Phase 4 already has; CANDIDATE declared before evidence (enforced by table row order, not prose)
- **Axis B** (V-02): AMEND table — each adjustment is a machine-readable row; "Slots re-filled" and "Gates re-run" columns make C-08 and C-14 obligations checkable without prose parsing
- **Axis C** (V-03): EXECUTION DEPENDENCY table — step-to-step ordering is a contract property in PREFLIGHT, complementing the slot-to-slot "Required by" column (C-34); reads/writes/constraints visible at preflight-scan time

| | **V-01** | **V-02** | **V-03** | **V-04** | **V-05** |
|---|---|---|---|---|---|
| **C-36** (Phase 4 as PASS/FAIL table) | 4-row table | 4-row table | 4-row table | 4-row table | 4-row table |
| **C-35** (pipe-delimited slot 5 template) | Full template | Full template | Full template | Full template | Full template |
| **C-34** ("Required by" column) | YES | YES | YES | YES | YES |
| **Phase 3 WHITESPACE format** | 4-row PASS/FAIL table | Code block | Code block | 4-row PASS/FAIL table | 4-row PASS/FAIL table |
| **AMEND format** | Prose (3 items) | Structured 6-column table | Prose (3 items) | Structured 6-column table | Structured 6-column table |
| **EXECUTION DEPENDENCY** | NO | NO | YES — step table | NO | YES — step table |
| **GATE 3 NOT ACCEPTABLE** | YES (retroactive THEREFORE) | YES | YES | YES | YES |

---

## V-01 — Lifecycle emphasis (Phase 3 WHITESPACE as 4-row PASS/FAIL table)

**Axis:** Lifecycle emphasis — Phase 3 WHITESPACE is restructured as a named 4-row PASS/FAIL table with rows: CANDIDATE (the gap attribute under evaluation, declared before evidence), ABSENCE-EVIDENCE (per-row format requirement + failure state), GAP-CONFIRMED (confirmation statement format + failure state), and vs-INERTIA-REF (comparison format + failure state). This applies C-36's pattern — which restructured Phase 4 from a code-block instruction into a machine-checkable output grid — to Phase 3.

**Hypothesis:** CANDIDATE declaration first (enforced by table row order) prevents the common Phase 3 failure: writing a gap assertion before gathering per-row absence evidence. Currently Phase 3 is prose-ordered; a model can assert a gap, then list evidence selectively, then confirm. A 4-row table with CANDIDATE first and ABSENCE-EVIDENCE second makes selective evidence impossible without structural malformation. The vs-INERTIA-REF row as the final checkpoint also closes the gap where whitespace findings are left unconnected to the C0 baseline — an INERTIA-REF comparison is required before the whitespace validation table is complete.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first — the complete production specification, including slot dependency relationships, is readable before any gate constraint is encountered.

---

### OUTPUT CONTRACTS

All output slots required by this skill, declared before any gate. Each slot specifies its label, required structural format, the gate or phase responsible for filling it, and the upstream slots it depends on. INERTIA-REF (slot 1) is the root — no upstream dependency; all slots that use or compare against it name it in their "Required by" column.

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
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without per-row attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE block |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff — no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is the first row of the Phase 4 proof table; slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS) is filled before any reduction row | **Proof structure failure** — SOURCE must be the first table row; any ordering that places a REDUCTION row before SOURCE is structurally malformed |
| Both reductions answer NO | REDUCTION-1 row and REDUCTION-2 row each contain "NO" with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both rows required; if either answers YES, discard the gap and find a different one |
| THEREFORE blocked until reductions complete | THEREFORE row is written only after both REDUCTION rows answer NO | **Proof structure failure** — THEREFORE is blocked; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows of this gate before proceeding to Phase 1. The write row fills slot 1 (INERTIA-REF, root) in OUTPUT CONTRACTS above — slots 5 and 6 depend on this token per "Required by" column.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label such as "high familiarity" | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
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

For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table below. Rows must appear in order: CANDIDATE before ABSENCE-EVIDENCE before GAP-CONFIRMED before vs-INERTIA-REF. Complete all four rows before moving to the next candidate attribute. This table fills slot 3 (Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS).

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — the candidate gap attribute under evaluation; declared before any absence evidence is gathered | **Whitespace naming failure** — declare the candidate attribute as the first row; an absent or unnamed CANDIDATE row blocks the ABSENCE-EVIDENCE row |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row in the competitor table (including C0) — fills slot 3 (Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS) | **Whitespace gate failure** — per-row evidence required for every competitor row; a bare assertion without per-row attribute-level evidence does not satisfy; every row in the competitor table must appear |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}] — attribute-level uncontested` — or — `Gap not confirmed: Row C{N} provides [{non-absent value}]; select a different candidate` | **Whitespace gate failure** — if any competitor row provides a non-absent value, this candidate is not whitespace; stop, select a different attribute, restart the validation table |
| vs-INERTIA-REF | `vs. INERTIA-REF — {how the vacant attribute relates to the C0 mechanism phrase from slot 1}` | **Whitespace INERTIA-REF failure** — every gap finding must name its relationship to the INERTIA-REF mechanism; "N/A" is not permitted as the final row of a whitespace validation pass |

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion in ABSENCE-EVIDENCE row — **whitespace gate failure**
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before completing ABSENCE-EVIDENCE for all competitor rows — **whitespace gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. This phase fills two output contract slots. Execute all four rows in order before outputting. SOURCE is row 1 — it must appear before any reduction row. If REDUCTION-1 or REDUCTION-2 answers YES, stop and find a different gap before writing THEREFORE.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — named cell from the competitor table; fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row of this table | **Proof structure failure** — SOURCE row must appear first; absent or malformed SOURCE blocks all subsequent rows |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped; the competitive map alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the competitive map alone; discard and find a different gap |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped; the focus dimension alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the focus dimension alone; discard and find a different gap |
| THEREFORE | `{one sentence naming the gap that requires both the competitive map and the focus dimension simultaneously}` — fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS): `REDUCTION-1 NO: [REDUCTION-1 sentence] \| REDUCTION-2 NO: [REDUCTION-2 sentence] \| THEREFORE: [THEREFORE sentence]` | **Proof structure failure** — THEREFORE is blocked until both REDUCTION rows answer NO; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2–5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier — enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — apply GATE 4 (Write row — slot 1 must have been written before this phase runs per "Required by" column); a cell with only "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name.

For the cross-dimensional finding row: the Claim cell contains the THEREFORE sentence. The Anchor cell contains the SOURCE value. The full slot 5 pipe-delimited proof string fills an adjacent indented block — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot (PREFLIGHT > OUTPUT CONTRACTS — slot 4) with the new evidentiary anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus using the slot 5 format template (`REDUCTION-1 NO: [...] | REDUCTION-2 NO: [...] | THEREFORE: [...]`). Reconstruct THEREFORE. Apply GATE 3. Writing only a new THEREFORE without rerunning both reductions is a **proof rerun failure** — both reduction sentences must be rebuilt; slot 5 is re-filled only when all three components conform to the pipe-delimited format template.

2. **Add competitor**: Insert a new row after running WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, slot 2). Re-run Phase 3 WHITESPACE VALIDATION table for all candidate attributes — a new row may change vacancy status; apply GATE 2 (whitespace absence anchor, slot 3). Review INERTIA-REF-DELTA (slot 6): does the new row's mechanism phrase alter any existing finding comparison?

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4, Write row / OUTPUT CONTRACTS — slot 1, root): Re-execute the GATE 4 Write row with a more specific mechanism phrase — name a product feature, workflow step, or workaround behavior. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells (slot 6) referencing the old mechanism phrase; updated cells must conform to slot 6 format template. Review slot 5 (Focus-scope evidence, "Required by: slot 4 and slot 1"): if the new INERTIA-REF phrase shifts the cross-dimensional baseline, rebuild the Phase 4 proof table.

---

## V-02 — Output format (AMEND as structured 6-column table)

**Axis:** Output format — AMEND is restructured as a 3-row, 6-column table: # / Adjustment / What user changes / What changes in output / Slots re-filled / Gates re-run. Each adjustment row names the input change, the output change, which output contract slots are re-filled, and which gates re-run. This makes AMEND machine-readable at the same structural level as OUTPUT CONTRACTS.

**Hypothesis:** C-08 requires each adjustment to name what the user changes and what changes in the output. C-14 requires proof rerun prescription. A tabular AMEND encodes both as queryable columns: a reviewer can verify that slot 5 (Focus-scope evidence) appears in the "Slots re-filled" column for the focus-shift adjustment — satisfying C-14 at table-scan time rather than by reading prose. The "Gates re-run" column makes the GATE 3 rerun obligation explicit in the same format as the OUTPUT CONTRACTS "Filled by phase" column. This closes the AMEND enforcement gap: the table cannot be satisfied with a partial update that rebuilds THEREFORE without naming the slot.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first.

---

### OUTPUT CONTRACTS

All output slots required by this skill, declared before any gate. Each slot specifies its label, required structural format, the gate or phase responsible for filling it, and the upstream slots it depends on.

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
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without per-row attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE block |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "requires all integrations to use REST polling — no webhook delivery pathway available"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is the first row of the Phase 4 proof table; slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS) is filled before any reduction row | **Proof structure failure** — SOURCE must be the first table row; any ordering that places a REDUCTION row before SOURCE is structurally malformed |
| Both reductions answer NO | REDUCTION-1 row and REDUCTION-2 row each contain "NO" with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both rows required; if either answers YES, discard the gap and find a different one |
| THEREFORE blocked until reductions complete | THEREFORE row is written only after both REDUCTION rows answer NO | **Proof structure failure** — THEREFORE is blocked; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows of this gate before proceeding to Phase 1. The write row fills slot 1 (INERTIA-REF, root) in OUTPUT CONTRACTS above — slots 5 and 6 depend on this token per "Required by" column.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
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

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token (slot 1, root) — this data fills slot 6 (INERTIA-REF-DELTA, "Required by: slot 1") at Phase 5.

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

Apply GATE 3. Execute all four rows in order. SOURCE is row 1 — must appear before any reduction row. If REDUCTION-1 or REDUCTION-2 answers YES, stop and find a different gap before writing THEREFORE.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — named cell from the competitor table; fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row of this table | **Proof structure failure** — SOURCE row must appear first; absent or malformed SOURCE blocks all subsequent rows |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped; the competitive map alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the competitive map alone; discard and find a different gap |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped; the focus dimension alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is producible from the focus dimension alone; discard and find a different gap |
| THEREFORE | `{one sentence naming the gap that requires both dimensions simultaneously}` — fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS): `REDUCTION-1 NO: [REDUCTION-1 sentence] \| REDUCTION-2 NO: [REDUCTION-2 sentence] \| THEREFORE: [THEREFORE sentence]` | **Proof structure failure** — THEREFORE is blocked until both REDUCTION rows answer NO; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2–5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C2, focus-column: "no self-serve onboarding — requires sales call before trial access"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — every finding row must cite INERTIA-REF by token name; a cell with only "N/A" is malformed.

For the cross-dimensional finding row: Claim = THEREFORE sentence; Anchor = SOURCE value; an adjacent indented block contains the full slot 5 pipe-delimited proof string — apply GATE 3.

---

### AMEND

Execute exactly 3 adjustment rows. Each row names: the adjustment type, what the user changes, what changes in the output, which output contract slots are re-filled, and which gates re-run. A row that names the adjustment without specifying both "Slots re-filled" and "Gates re-run" does not conform to the table format.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` in FOCUS CHECK with a different focus value | SOURCE slot re-identified from the updated focus; Focus-scope evidence (slot 5) rebuilt from scratch: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` — both reduction sentences must be rebuilt; THEREFORE rewritten; any finding citing the cross-dimensional gap updated | 4 (SOURCE), 5 (Focus-scope evidence) | GATE 3 (all rows: SOURCE first, both reductions answer NO, THEREFORE blocked) — writing a new THEREFORE without rerunning both reductions is a **proof rerun failure**; slot 5 is re-filled only when all three components conform to the pipe-delimited format template |
| 2 | Add competitor | Competitor name + context for WebSearch | New competitor row added with Anchor `Row C{N}, {attribute}: "{value}"` (slot 2); whitespace absence evidence (slot 3) re-evaluated for all candidate attributes — a new row may change vacancy status; INERTIA-REF-DELTA (slot 6) reviewed for each existing finding — does the new row's mechanism phrase alter the comparison? | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation for new row), GATE 2 (anchor format for new row; whitespace absence evidence for all candidate attributes) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase — name a product feature, workflow step, or workaround behavior | INERTIA-REF token (slot 1) re-written at GATE 4 write row conforming to slot 1 format template; all Phase 5 INERTIA-REF-DELTA cells (slot 6) referencing the old mechanism phrase updated; Phase 4 proof table (slot 5) reviewed — if new mechanism phrase shifts cross-dimensional baseline, rebuild all four proof rows and re-fill slot 5 in pipe-delimited format | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA, all finding rows), 5 (Focus-scope evidence, if baseline shifts) | GATE 4 (all rows: stickiness check, write row, per-finding citation), GATE 3 (if slot 5 rebuild required — all rows: SOURCE, reductions, THEREFORE) |

---

## V-03 — Inertia framing (Execution Dependency table in PREFLIGHT)

**Axis:** Inertia framing — PREFLIGHT adds an EXECUTION DEPENDENCY section (after OUTPUT CONTRACTS, before GATE 1) containing a table that makes gate-to-phase ordering explicit as a structural constraint. The table columns are: Step / Reads slot / Writes slot / Execution constraint. GATE 4 appears as the root step with no upstream reads — making INERTIA-REF's centrality visible as a structural DAG property before any gate is read.

**Hypothesis:** The "Required by" column in OUTPUT CONTRACTS (C-34) makes slot-level dependencies readable at contract time. The EXECUTION DEPENDENCY table makes step-level ordering readable at the same point. A reader scanning PREFLIGHT sees two complementary views: which slots depend on which slots (OUTPUT CONTRACTS "Required by"), and which steps must execute before which steps (EXECUTION DEPENDENCY "Execution constraint"). These two views together close the remaining interpretive gap: the contract tells you the target; the DAG tells you the path. GATE 4 as the root step of the DAG reinforces the inertia-first design principle without requiring a prose explanation.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first. EXECUTION DEPENDENCY follows, making the execution ordering machine-readable before any gate constraint is encountered.

---

### OUTPUT CONTRACTS

All output slots required by this skill, declared before any gate. Each slot specifies its label, required structural format, the gate or phase responsible for filling it, and the upstream slots it depends on.

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

The table below makes the step-level execution ordering required to fulfill the output contracts above machine-readable before any gate is read. GATE 4 is the root step — it writes slot 1 (INERTIA-REF) with no upstream read. A step listed in "Reads slot" must not begin until the named slot has been written by the step that fills it (see "Filled by phase" in OUTPUT CONTRACTS above).

| Step | Reads slot | Writes slot | Execution constraint |
|------|-----------|------------|---------------------|
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and before all other phases**; no phase may produce output until slot 1 is written; this is the root step |
| Phase 2 (per competitor row) | 1 — INERTIA-REF (C0 row uses GATE 4 token for mechanism reference) | 2 — Anchor column value | Runs after GATE 4; GATE 1 (citation) and GATE 2 (anchor) applied per row; slot 2 is complete when all competitor rows have been output |
| Phase 3 | 2 — Anchor column value (competitor table must be complete before whitespace evaluation begins) | 3 — Absence evidence block | Runs after Phase 2 complete; GATE 2 (whitespace absence anchor) applied per candidate attribute |
| Phase 4, SOURCE row | 2 — Anchor column value (named cell from competitor table) | 4 — SOURCE slot | SOURCE row is row 1 of the Phase 4 proof table; must be written before any REDUCTION row |
| Phase 4, REDUCTION + THEREFORE rows | 4 — SOURCE slot (written), 1 — INERTIA-REF (comparator baseline) | 5 — Focus-scope evidence | Both REDUCTION rows must answer NO before THEREFORE; slot 5 filled as pipe-delimited string on THEREFORE completion |
| Phase 5 (per finding row) | 1 — INERTIA-REF (DELTA column), 2 — Anchor column value (Anchor column) | 6 — INERTIA-REF-DELTA | Runs after Phase 4 complete; GATE 4 row 3 (per-finding citation) applied per row |

A step that begins before its declared "Reads slot" value has been written constitutes an **execution dependency violation**.

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
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without per-row attribute-level evidence does not satisfy; per-row evidence required |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "enforces synchronous kickoff calls — no fully async onboarding path exists"`

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

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows of this gate before proceeding to Phase 1. The write row fills slot 1 (INERTIA-REF, root) in OUTPUT CONTRACTS above — slots 5 and 6 depend on this token per "Required by" column; GATE 4 is the root step per EXECUTION DEPENDENCY above.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF, root, PREFLIGHT > OUTPUT CONTRACTS); root step complete per PREFLIGHT > EXECUTION DEPENDENCY; token now available to all phases | **Inertia write failure** — token must be written at this gate row; return to this row and execute the write before Phase 1 begins |
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

Note which mechanism phrases relate to the INERTIA-REF token (slot 1, root) — this data fills slot 6 (INERTIA-REF-DELTA, "Required by: slot 1") at Phase 5 per PREFLIGHT > EXECUTION DEPENDENCY.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 2 (whitespace absence anchor). Reads slot 2 (Competitor Table complete) per PREFLIGHT > EXECUTION DEPENDENCY. For each candidate whitespace attribute, record per row:

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

Apply GATE 3. Reads slot 2 (named cell) and slot 1 (INERTIA-REF comparator) per PREFLIGHT > EXECUTION DEPENDENCY. Execute all four rows in order. SOURCE is row 1 — must appear before any reduction row.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — named cell from the competitor table; fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row | **Proof structure failure** — SOURCE row must appear first; absent or malformed SOURCE blocks all subsequent rows |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped; the competitive map alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is single-dimension sufficient from the map; discard and find a different gap |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped; the focus dimension alone does not produce this gap}` | **Proof structure failure** — if YES, the gap is single-dimension sufficient from focus; discard and find a different gap |
| THEREFORE | `{one sentence naming the gap requiring both dimensions simultaneously}` — fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS): `REDUCTION-1 NO: [REDUCTION-1 sentence] \| REDUCTION-2 NO: [REDUCTION-2 sentence] \| THEREFORE: [THEREFORE sentence]` | **Proof structure failure** — THEREFORE blocked until both REDUCTION rows answer NO; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first then constructing REDUCTION rows retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2–5 findings. Reads slot 1 (INERTIA-REF) and slot 2 (Anchor values) per PREFLIGHT > EXECUTION DEPENDENCY. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only entries are syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 3 reveals that...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, mechanism: "requires synchronous kickoff call — no fully async first-run path exists"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — every finding row must cite INERTIA-REF by token name.

For the cross-dimensional finding row: Claim = THEREFORE sentence; Anchor = SOURCE value; adjacent indented block contains slot 5 pipe-delimited proof string — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot (PREFLIGHT > OUTPUT CONTRACTS — slot 4; root step connection: EXECUTION DEPENDENCY Phase 4 SOURCE row). Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus (`REDUCTION-1 NO: [...] | REDUCTION-2 NO: [...] | THEREFORE: [...]`). Reconstruct THEREFORE. Apply GATE 3. Writing only a new THEREFORE without rerunning both reductions is a **proof rerun failure** — slot 5 re-filled only when all three pipe-delimited components are complete.

2. **Add competitor**: Insert a new row after running WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — slot 2). Update Phase 3 WHITESPACE for all candidate attributes — per PREFLIGHT > EXECUTION DEPENDENCY, slot 3 depends on slot 2 being complete; apply GATE 2 (whitespace absence anchor, slot 3). Review INERTIA-REF-DELTA (slot 6) for existing findings.

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4, Write row — root step, EXECUTION DEPENDENCY): Re-execute the write row with a more specific mechanism phrase. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells (slot 6); updated cells must conform to slot 6 format template. Review slot 5: if new INERTIA-REF phrase shifts the baseline, rebuild all four Phase 4 proof rows; re-fill slot 5 in pipe-delimited format.

---

## V-04 — Combined: Lifecycle emphasis + Output format (WHITESPACE table + AMEND table)

**Axis:** Lifecycle emphasis + Output format — Phase 3 WHITESPACE as 4-row PASS/FAIL validation table (V-01 axis) combined with AMEND as 6-column structured table (V-02 axis). No EXECUTION DEPENDENCY table.

**Hypothesis:** The two axes target complementary structural gaps. The WHITESPACE table closes Phase 3's sequential vulnerability — CANDIDATE-first ordering is structurally enforced for gap identification the same way SOURCE-first is enforced for Phase 4 proofs. The AMEND table closes the enforcement gap at the amendment boundary — slot obligations and gate re-runs are queryable columns rather than prose obligations. Together, they give both the evidence-gathering phase and the amendment lifecycle the same machine-readable structural enforcement as Phase 4 and OUTPUT CONTRACTS.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first.

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
| SOURCE row first | SOURCE row is the first row of the Phase 4 proof table; slot 4 filled before any reduction row | **Proof structure failure** — SOURCE must be the first table row; any ordering that places a REDUCTION row before SOURCE is structurally malformed |
| Both reductions answer NO | REDUCTION-1 row and REDUCTION-2 row each contain "NO" with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both rows required; if either answers YES, discard and find a different gap |
| THEREFORE blocked until reductions complete | THEREFORE row written only after both REDUCTION rows answer NO | **Proof structure failure** — THEREFORE is blocked; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows before Phase 1. The write row fills slot 1 (root) per "Required by" column in OUTPUT CONTRACTS.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF, root, PREFLIGHT > OUTPUT CONTRACTS above); slots 5 and 6 require this token per "Required by" column | **Inertia write failure** — token must be written at this gate row; return to this row and execute the write |
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

C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only cells are syntactically malformed; apply GATE 2 before outputting.

Note mechanism phrases and focus-column values relating to INERTIA-REF (slot 1, root) — fills slot 6 ("Required by: slot 1") at Phase 5.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table. Rows must appear in order: CANDIDATE before ABSENCE-EVIDENCE before GAP-CONFIRMED before vs-INERTIA-REF. Complete all four rows before moving to the next candidate attribute.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — the candidate gap attribute under evaluation; declared before any absence evidence is gathered | **Whitespace naming failure** — declare the candidate attribute as the first row; an absent or unnamed CANDIDATE row blocks the ABSENCE-EVIDENCE row |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every competitor row (including C0) — fills slot 3 (Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS) | **Whitespace gate failure** — per-row evidence required for every competitor row; a bare assertion does not satisfy; every row must appear before GAP-CONFIRMED |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}] — attribute-level uncontested` — or — `Gap not confirmed: Row C{N} provides [{non-absent value}]; select a different candidate` | **Whitespace gate failure** — if any row provides a non-absent value, this candidate is not whitespace; stop, select a different attribute, restart the validation table |
| vs-INERTIA-REF | `vs. INERTIA-REF — {how the vacant attribute relates to the C0 mechanism phrase from slot 1}` | **Whitespace INERTIA-REF failure** — every gap finding must name its relationship to the INERTIA-REF mechanism; "N/A" is not permitted as the final row |

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion in ABSENCE-EVIDENCE row — **whitespace gate failure**
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before completing ABSENCE-EVIDENCE for all competitor rows — **whitespace gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. Execute all four rows in order. SOURCE is row 1. If REDUCTION-1 or REDUCTION-2 answers YES, stop and find a different gap before writing THEREFORE.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — named cell from the competitor table; fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row | **Proof structure failure** — SOURCE row must appear first; absent or malformed SOURCE blocks all subsequent rows |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped; the competitive map alone does not produce this gap}` | **Proof structure failure** — if YES, gap is single-dimension sufficient from the map; discard and find a different gap |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped; the focus dimension alone does not produce this gap}` | **Proof structure failure** — if YES, gap is single-dimension sufficient from focus; discard and find a different gap |
| THEREFORE | `{one sentence naming the gap requiring both dimensions simultaneously}` — fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS): `REDUCTION-1 NO: [REDUCTION-1 sentence] \| REDUCTION-2 NO: [REDUCTION-2 sentence] \| THEREFORE: [THEREFORE sentence]` | **Proof structure failure** — THEREFORE blocked until both REDUCTION rows answer NO; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2–5 findings. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only entries are syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C2, focus-column: "requires annual contract — no month-to-month SMB tier available"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — every finding row must cite INERTIA-REF by token name; "N/A" is malformed.

For the cross-dimensional finding row: Claim = THEREFORE sentence; Anchor = SOURCE value; adjacent indented block = slot 5 pipe-delimited proof string — apply GATE 3.

---

### AMEND

Execute exactly 3 adjustment rows. Each row names: the adjustment, what the user changes, what changes in the output, which slots are re-filled, and which gates re-run.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` in FOCUS CHECK | SOURCE slot re-identified; Focus-scope evidence (slot 5) rebuilt from scratch: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` — both reduction sentences must be rebuilt; THEREFORE rewritten; cross-dimensional finding updated | 4 (SOURCE), 5 (Focus-scope evidence) | GATE 3 (all rows) — writing a new THEREFORE without rerunning both reductions is a **proof rerun failure**; slot 5 re-filled only when all three components conform to the pipe-delimited template |
| 2 | Add competitor | Competitor name + context for WebSearch | New competitor row (slot 2); WHITESPACE VALIDATION table re-run for all candidate attributes (slot 3 re-evaluated — a new row may change vacancy status); INERTIA-REF-DELTA (slot 6) reviewed for each existing finding | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation for new row), GATE 2 (anchor format for new row; ABSENCE-EVIDENCE for all whitespace candidate attributes) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase — product feature, workflow step, or workaround behavior | INERTIA-REF token (slot 1) re-written at GATE 4 write row; all Phase 5 INERTIA-REF-DELTA cells (slot 6) updated; Phase 4 proof table (slot 5) reviewed — if new mechanism phrase shifts cross-dimensional baseline, rebuild all four proof rows and re-fill slot 5 in pipe-delimited format | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA, all finding rows), 5 (if baseline shifts) | GATE 4 (all rows), GATE 3 (if slot 5 rebuild required) |

---

## V-05 — Combined maximum (WHITESPACE table + AMEND table + EXECUTION DEPENDENCY table)

**Axis:** Combined maximum — all three R9 innovation axes: Phase 3 WHITESPACE as 4-row PASS/FAIL table (V-01), AMEND as 6-column structured table (V-02), and EXECUTION DEPENDENCY table in PREFLIGHT (V-03). Every phase that produces a named output slot uses a PASS/FAIL table structure (Phase 3, Phase 4). PREFLIGHT exposes all execution constraints — slot dependencies (OUTPUT CONTRACTS "Required by"), step dependencies (EXECUTION DEPENDENCY), and gate constraints (GATE 1–4) — before Phase 1 begins.

**Hypothesis:** Maximum structural cohesion: every non-trivial production step has machine-checkable output structure (Phase 3 WHITESPACE table, Phase 4 proof table) and every amendment has machine-readable side effects (AMEND table "Slots re-filled" and "Gates re-run"). The EXECUTION DEPENDENCY table elevates PREFLIGHT from a checklist of constraints to a full execution specification: read PREFLIGHT, know the slot targets (OUTPUT CONTRACTS), know the dependency graph (EXECUTION DEPENDENCY), know the gate constraints (GATE 1–4) — all before executing a single phase. INERTIA-REF as the root step of the DAG and the root slot of the "Required by" column makes the inertia-first design principle architecturally enforced rather than conventionally observed.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first — slot targets and dependencies readable before any gate. EXECUTION DEPENDENCY follows — step ordering readable before Phase 1. Gates 1–4 follow.

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

Step-level execution ordering, making the dependency chain machine-readable before any gate is read. GATE 4 is the root step. A step listed in "Reads slot" must not begin until that slot has been written.

| Step | Reads slot | Writes slot | Execution constraint |
|------|-----------|------------|---------------------|
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and before all other phases**; no phase may produce output until slot 1 is written |
| Phase 2 (per competitor row) | 1 — INERTIA-REF (C0 row mechanism reference) | 2 — Anchor column value | Runs after GATE 4; GATE 1 and GATE 2 applied per row; slot 2 complete when all rows output |
| Phase 3 (per whitespace candidate) | 2 — Anchor column value (Competitor Table complete) | 3 — Absence evidence block | Runs after Phase 2 complete; WHITESPACE VALIDATION table (4 rows) executed per candidate attribute |
| Phase 4, SOURCE row | 2 — Anchor column value (named cell from competitor table) | 4 — SOURCE slot | SOURCE row is row 1 of proof table; must be written before any REDUCTION row |
| Phase 4, REDUCTION + THEREFORE rows | 4 — SOURCE slot (written), 1 — INERTIA-REF (comparator baseline) | 5 — Focus-scope evidence | Both REDUCTION rows answer NO before THEREFORE; slot 5 filled as pipe-delimited string on THEREFORE completion |
| Phase 5 (per finding row) | 1 — INERTIA-REF (DELTA column), 2 — Anchor column value | 6 — INERTIA-REF-DELTA | Runs after Phase 4 complete; GATE 4 row 3 (per-finding citation) applied per row |

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
| Both reductions answer NO | REDUCTION-1 row and REDUCTION-2 row each contain "NO" with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both rows required; if either answers YES, discard and find a different gap |
| THEREFORE blocked until reductions complete | THEREFORE row written only after both REDUCTION rows answer NO | **Proof structure failure** — THEREFORE is blocked; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows before Phase 1. This is the root step (PREFLIGHT > EXECUTION DEPENDENCY): slot 1 (INERTIA-REF) is the root dependency for slots 5 and 6 (PREFLIGHT > OUTPUT CONTRACTS, "Required by" column).

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before executing the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF, root, PREFLIGHT > OUTPUT CONTRACTS); root step complete (PREFLIGHT > EXECUTION DEPENDENCY); token now available to all phases; slots 5 and 6 require this token per "Required by" column | **Inertia write failure** — token must be written at this gate row; return to this row and execute the write before Phase 1 begins |
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

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token (slot 1, root, PREFLIGHT > OUTPUT CONTRACTS) — this data fills slot 6 (INERTIA-REF-DELTA, "Required by: slot 1") at Phase 5 per PREFLIGHT > EXECUTION DEPENDENCY.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 2 (Competitor Table complete) per PREFLIGHT > EXECUTION DEPENDENCY. For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table. Rows must appear in order: CANDIDATE before ABSENCE-EVIDENCE before GAP-CONFIRMED before vs-INERTIA-REF. Complete all four rows before moving to the next candidate attribute.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — the candidate gap attribute under evaluation; declared before any absence evidence is gathered | **Whitespace naming failure** — declare the candidate attribute as the first row; an absent or unnamed CANDIDATE row blocks the ABSENCE-EVIDENCE row |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every competitor row (including C0) — fills slot 3 (Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS) | **Whitespace gate failure** — per-row evidence required for every competitor row; a bare assertion does not satisfy; every row must appear before GAP-CONFIRMED |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}] — attribute-level uncontested` — or — `Gap not confirmed: Row C{N} provides [{non-absent value}]; select a different candidate` | **Whitespace gate failure** — if any row provides a non-absent value, this candidate is not whitespace; stop, select a different attribute, restart the validation table |
| vs-INERTIA-REF | `vs. INERTIA-REF — {how the vacant attribute relates to the C0 mechanism phrase from slot 1}` | **Whitespace INERTIA-REF failure** — every gap finding must name its relationship to the INERTIA-REF mechanism; "N/A" is not permitted as the final row |

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before completing ABSENCE-EVIDENCE for all competitor rows — **whitespace gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. Reads slot 2 (named cell) and slot 1 (INERTIA-REF comparator) per PREFLIGHT > EXECUTION DEPENDENCY. Execute all four rows in order. SOURCE is row 1 — must appear before any reduction row.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — named cell from the competitor table; fills slot 4 (SOURCE slot, PREFLIGHT > OUTPUT CONTRACTS); must be the first row of this table | **Proof structure failure** — SOURCE row must appear first; absent or malformed SOURCE blocks all subsequent rows |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped; the competitive map alone does not produce this gap}` | **Proof structure failure** — if YES, gap is single-dimension sufficient from the map; discard and find a different gap |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped; the focus dimension alone does not produce this gap}` | **Proof structure failure** — if YES, gap is single-dimension sufficient from focus; discard and find a different gap |
| THEREFORE | `{one sentence naming the gap requiring both dimensions simultaneously}` — fills slot 5 (Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS): `REDUCTION-1 NO: [REDUCTION-1 sentence] \| REDUCTION-2 NO: [REDUCTION-2 sentence] \| THEREFORE: [THEREFORE sentence]` | **Proof structure failure** — THEREFORE blocked until both REDUCTION rows answer NO; writing THEREFORE first and adding reduction rows retroactively is a proof structure failure |

NOT ACCEPTABLE: Writing the THEREFORE row first and then constructing REDUCTION-1 and REDUCTION-2 rows to justify it retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2–5 findings. Reads slot 1 (INERTIA-REF) and slot 2 (Anchor values) per PREFLIGHT > EXECUTION DEPENDENCY. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only entries are syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier — enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, PREFLIGHT > OUTPUT CONTRACTS — "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — every finding row must cite INERTIA-REF by token name; "N/A" is malformed.

For the cross-dimensional finding row: Claim = THEREFORE sentence; Anchor = SOURCE value; adjacent indented block = slot 5 pipe-delimited proof string — apply GATE 3.

---

### AMEND

Execute exactly 3 adjustment rows. Each row names the adjustment, what the user changes, what changes in the output, which output contract slots are re-filled, and which gates re-run.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` in FOCUS CHECK | SOURCE slot re-identified from updated focus; Focus-scope evidence (slot 5) rebuilt from scratch: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` — both reduction sentences must be rebuilt per PREFLIGHT > EXECUTION DEPENDENCY (Phase 4 REDUCTION + THEREFORE step reads slot 1 and slot 4); THEREFORE rewritten; cross-dimensional finding row updated in Phase 5 | 4 (SOURCE), 5 (Focus-scope evidence) | GATE 3 (all rows: SOURCE first, both reductions answer NO, THEREFORE blocked) — writing a new THEREFORE without rerunning both reductions is a **proof rerun failure**; slot 5 re-filled only when all three components conform to pipe-delimited format |
| 2 | Add competitor | Competitor name + context for WebSearch | New competitor row (slot 2: `Row C{N}, {attribute}: "{value}"`); WHITESPACE VALIDATION table re-run for all candidate attributes (slot 3 re-evaluated per PREFLIGHT > EXECUTION DEPENDENCY Phase 3 constraint — slot 2 must be complete; a new row may change vacancy status); INERTIA-REF-DELTA (slot 6) reviewed for each existing finding | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation for new row), GATE 2 (anchor format for new row; ABSENCE-EVIDENCE rows in WHITESPACE VALIDATION table for all candidate attributes) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase — product feature, workflow step, or workaround behavior | INERTIA-REF token (slot 1) re-written at GATE 4 write row per PREFLIGHT > EXECUTION DEPENDENCY root step; all Phase 5 INERTIA-REF-DELTA cells (slot 6) updated to new mechanism phrase; Phase 4 proof table (slot 5) reviewed — if new mechanism phrase shifts cross-dimensional baseline, rebuild all four proof rows and re-fill slot 5 in pipe-delimited format | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA, all finding rows), 5 (Focus-scope evidence, if baseline shifts) | GATE 4 (all rows: stickiness check, write row, per-finding citation), GATE 3 (if slot 5 rebuild required: SOURCE, both reductions, THEREFORE) |

---

```json
{"round": "R9", "rubric": "v8", "target_score": 230, "universal_baseline": ["C-34 (Required-by column)", "C-35 (pipe-delimited slot 5 template)", "C-36 (Phase 4 as PASS/FAIL table)"], "new_axes": ["Axis A: Phase 3 WHITESPACE as 4-row PASS/FAIL table (V-01, V-04, V-05)", "Axis B: AMEND as 6-column structured table (V-02, V-04, V-05)", "Axis C: EXECUTION DEPENDENCY table in PREFLIGHT (V-03, V-05)"], "candidate_new_criteria": ["C-37: WHITESPACE identification phase structured as a named 4-row PASS/FAIL table (CANDIDATE / ABSENCE-EVIDENCE / GAP-CONFIRMED / vs-INERTIA-REF) — analogous to C-36 for Phase 3", "C-38: AMEND structured as a table with Adjustment / What user changes / What changes in output / Slots re-filled / Gates re-run columns — machine-readable at contract level", "C-39: PREFLIGHT includes an EXECUTION DEPENDENCY table showing step-to-step ordering (Reads slot / Writes slot / Execution constraint) — complementing C-34 slot dependencies with step-level DAG"]}
```
