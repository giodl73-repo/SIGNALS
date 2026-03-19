Written to `simulations/quest/variations/discover-competitors-alt-variations-R11-2026-03-17.md`.

---

## R11 Variations Summary

**Three single-axis innovations, then two combos. All satisfy C-40/C-41/C-42.**

| Variation | Axis | Innovation |
|-----------|------|-----------|
| **V-01** | Role sequence | FOCUS-STATE declared as slot 0 in OUTPUT CONTRACTS; GATE 0 gains Write row (mirrors GATE 4's write row pattern) |
| **V-02** | Output format | Slot 5 inactive path = `VACUOUS-5: focus-inactive` token — both paths now format-checkable by token presence, not prose permission |
| **V-03** | Lifecycle emphasis | GATE 0 listed as Step 0 in EXECUTION DEPENDENCY with `Prerequisite steps: -- (pre-DAG)` — full execution sequence machine-readable from a single table |
| **V-04** | A+B | V-01 + V-02 |
| **V-05** | Maximum | All three |

**Three candidate new criteria:**

- **C-43** (V-01): FOCUS-STATE declared as slot 0; GATE 0 Write row fills it before GATE 4 runs; slot 5 "Required by" names slot 0 as path selector. Prose GATE 0 with no Write row does not satisfy.
- **C-44** (V-02): Slot 5 inactive format is `VACUOUS-5: focus-inactive`; empty cell and prose descriptions both fail. Active path and inactive path are now symmetrically format-verifiable.
- **C-45** (V-03): GATE 0 listed as Step 0 in EXECUTION DEPENDENCY with `-- (pre-DAG)`; GATE 4 retains `None (root)`. GATE 0 absent from EXECUTION DEPENDENCY does not satisfy even if it is a named PREFLIGHT subsection.

**Notable V-05 structural property:** GATE 4's root status is now confirmed from five independent positions — OUTPUT CONTRACTS slot 1 "Required by: Root", EXECUTION DEPENDENCY "Reads slot: -- (root)", EXECUTION DEPENDENCY "Prerequisite steps: None (root)", OUTPUT CONTRACTS slot 0 "Required by: No upstream dependency" (pre-DAG), and EXECUTION DEPENDENCY Step 0 `-- (pre-DAG)` marking GATE 0 as prior to GATE 4 without creating a slot dependency.
t only from PREFLIGHT subsection position. GATE 4 retains `None (root)` as the data-dependency root; GATE 0 is distinguished as the pre-DAG root by the `-- (pre-DAG)` marker. A PREFLIGHT containing GATE 0 as a subsection before EXECUTION DEPENDENCY but absent from the EXECUTION DEPENDENCY table does not satisfy.

**Dependency notes:**
- C-43 is independent of C-44 and C-45
- C-44 strengthens GATE 0's inactive branch (C-40) by adding a required output format; C-44 satisfaction implies C-40 for the inactive branch
- C-45 requires C-40 (GATE 0 must exist as a named gate before it can be listed in EXECUTION DEPENDENCY)
- C-43 + C-45 together: when slot 0 is declared and GATE 0 appears in EXECUTION DEPENDENCY, Phase 4's "Reads slot" row can reference slot 0 explicitly — GATE 0's output is visible in two independent structural positions

| | **V-01** | **V-02** | **V-03** | **V-04** | **V-05** |
|---|---|---|---|---|---|
| **C-40** (FOCUS GATE in PREFLIGHT) | YES | YES | YES | YES | YES |
| **C-41** (Phase 3 vs-INERTIA-REF ternary) | YES | YES | YES | YES | YES |
| **C-42** (EXECUTION DEPENDENCY Prerequisite steps column) | YES | YES | YES | YES | YES |
| **FOCUS-STATE slot 0 + GATE 0 Write row** | YES (new) | NO | NO | YES | YES |
| **Slot 5 vacuous token** | NO | YES (new) | NO | YES | YES |
| **GATE 0 in EXECUTION DEPENDENCY** | NO | NO | YES (new) | NO | YES |

---

## V-01 — Role sequence (FOCUS-STATE as slot 0; GATE 0 gains Write row)

**Axis:** Role sequence — GATE 0 gains a Write row (structurally identical to GATE 4's write row), producing a named FOCUS-STATE token declared as slot 0 in OUTPUT CONTRACTS. Previously GATE 0 resolved focus state and named downstream consequences (slot 5 active vs. vacuous) but wrote no named artifact. Slot 5's "Required by" column now references slot 0 explicitly. Phase 4's EXECUTION DEPENDENCY row lists slot 0 as a dependency alongside slot 4 and slot 1.

**Hypothesis:** GATE 4 has a Write row producing slot 1 (INERTIA-REF) — this is what makes GATE 4 the data-dependency root. GATE 0 determines whether slot 5 fills actively or vacuously, but produces no named token — its resolution is control-flow only. Adding a Write row to GATE 0 makes focus-state determination an output-contract event: `FOCUS-STATE = {active: {dimension}} or {inactive}`. Slot 5's "Required by" can then name slot 0 as its path-selecting dependency. A reader of OUTPUT CONTRACTS sees the complete dependency chain for slot 5 — slot 0 (path), slot 4 (SOURCE), slot 1 (INERTIA-REF) — without reading any gate narrative.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first. GATE 0 (FOCUS GATE) follows — writes slot 0 (FOCUS-STATE) before step ordering is read. EXECUTION DEPENDENCY follows. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` — or — `{inactive}` | GATE 0 (Write row, below) | No upstream dependency; slot 5 reads slot 0 to determine active vs. vacuous path |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root — no upstream dependency; slots 5 and 6 require this token before they can be filled |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 values at Phase 5 |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires slot 2 (Competitor Table complete before whitespace evaluation begins) |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding | Required by slot 5; must appear as the first row of the proof table before any reduction row |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence — what is lost if the focus dimension is dropped}] \| REDUCTION-2 NO: [{one sentence — what is lost if the competitive map is dropped}] \| THEREFORE: [{gap sentence requiring both dimensions simultaneously}]` — or vacuous satisfaction when slot 0 = inactive | Phase 4 — Cross-Dimensional Finding | Requires slot 0 (FOCUS-STATE, written by GATE 0) to determine path; when active: requires slot 4 (SOURCE) and slot 1 (INERTIA-REF); when inactive: slot 5 satisfies by vacuous satisfaction |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 — Findings Table | Derived from slot 1 (INERTIA-REF, root) — slot 1 must be written at GATE 4 before Phase 5 runs |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows before proceeding. The Write row fills slot 0 (FOCUS-STATE, PREFLIGHT > OUTPUT CONTRACTS) — slot 5 reads slot 0 to select the active or vacuous path.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` is set to a recognized value (`market-sizing`, `positioning-framework`) — OR — `focus:` is not set; infer from repo context (README, CLAUDE.md) before defaulting to none | **Focus detection failure** — unrecognized or ambiguous focus value; resolve before proceeding; do not proceed until focus state is confirmed |
| Write FOCUS-STATE token | Write at this step: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` — fills slot 0 (FOCUS-STATE, PREFLIGHT > OUTPUT CONTRACTS); token now available to Phase 4 for slot 5 path selection and to AMEND row 1 for focus-shift re-run | **Focus write failure** — token must be written at this gate row; return to this row before GATE 4 begins; slot 5 path is undefined until slot 0 is written |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 competitor table header; slot 5 fills as full pipe-delimited proof string (`REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`); Phase 4 proof table required; GATE 3 applies | **Focus activation failure** — focus active but Focus column omitted from Phase 2 table or slot 5 not filled as pipe-delimited string; both required when slot 0 = active |
| Focus-inactive branch | When slot 0 = inactive: Focus column not added to Phase 2 table; slot 5 satisfies by vacuous satisfaction; Phase 4 still runs; THEREFORE does not require cross-dimensional necessity argument | **Focus inactivation failure** — Focus column present in competitor table when slot 0 = inactive; remove column from Phase 2 header before outputting |

---

### EXECUTION DEPENDENCY

Step-level execution ordering. GATE 4 is the data-dependency root (`Prerequisite steps: None (root)`). Slot 0 (FOCUS-STATE) is written by GATE 0 (pre-DAG, before GATE 4) — Phase 4 REDUCTION + THEREFORE rows read slot 0 to determine the active/vacuous path for slot 5. An **execution dependency violation** occurs when a step begins before its declared "Reads slot" value has been written.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and all other phases**; no phase may produce output until slot 1 is written | None (root) |
| Phase 1 | — | TOPIC, FOCUS tokens | Reads repo context before Phase 2 | GATE 4 |
| Phase 2 (per competitor row) | 1 — INERTIA-REF (C0 row mechanism reference) | 2 — Anchor column value | GATE 1 and GATE 2 applied per row; Focus column per slot 0 (FOCUS-STATE, written by GATE 0 pre-DAG) | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 — Anchor column value (Competitor Table complete) | 3 — Absence evidence block | WHITESPACE VALIDATION table (4 rows) per candidate; vs-INERTIA-REF row uses slot 6 ternary-token format | Phase 2 |
| Phase 4, SOURCE row | 2 — Anchor column value (named cell) | 4 — SOURCE slot | SOURCE row is row 1 of proof table; before any REDUCTION row | Phase 3 |
| Phase 4, REDUCTION + THEREFORE rows | 0 — FOCUS-STATE (active/vacuous path), 4 — SOURCE slot (written), 1 — INERTIA-REF (comparator baseline) | 5 — Focus-scope evidence | Both REDUCTION rows answer NO before THEREFORE when slot 0 = active; slot 5 satisfies by vacuous satisfaction when slot 0 = inactive | Phase 4 SOURCE row |
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
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite before outputting |
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

NOT ACCEPTABLE: Writing the THEREFORE row first and constructing REDUCTION rows retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute all three rows before Phase 1. Root step: `Prerequisite steps: None (root)` per PREFLIGHT > EXECUTION DEPENDENCY; slot 1 (INERTIA-REF) is the data-dependency root per PREFLIGHT > OUTPUT CONTRACTS; slot 0 (FOCUS-STATE) was written by GATE 0 before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve before the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (INERTIA-REF, root, PREFLIGHT > OUTPUT CONTRACTS); root step complete (`Prerequisite steps: None (root)`, PREFLIGHT > EXECUTION DEPENDENCY); token now available to all phases | **Inertia write failure** — token must be written at this gate row; return before Phase 1 begins |
| Per-finding citation required | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — fills slot 6 (INERTIA-REF-DELTA) per finding row | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### PHASE 1: CONTEXT

Runs after GATE 4 (`Prerequisite steps: GATE 4`). Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 1 (`Prerequisite steps: Phase 1`). C0 is the entity whose stickiness was resolved in GATE 4. C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column present or absent per slot 0 (FOCUS-STATE, written by GATE 0).

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only cells are syntactically malformed; apply GATE 2 before outputting.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 2 (`Prerequisite steps: Phase 2`). For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table. CANDIDATE row first.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — declared before any absence evidence is gathered | **Whitespace naming failure** — absent or unnamed CANDIDATE blocks ABSENCE-EVIDENCE |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every competitor row (including C0) — fills slot 3 | **Whitespace gate failure** — per-row evidence required; bare assertion does not satisfy |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}] — attribute-level uncontested` — or — `Gap not confirmed: Row C{N} provides [{non-absent value}]; select a different candidate` | **Whitespace gate failure** — non-absent value stops the candidate; select a different attribute |
| vs-INERTIA-REF | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — ternary token required; same format as slot 6 | **Whitespace INERTIA-REF format failure** — prose without ternary token does not satisfy; "N/A" not permitted |

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "vs. INERTIA-REF — adjacent to C0's workflow" — prose without ternary token — **whitespace INERTIA-REF format failure**
ACCEPTABLE (vs-INERTIA-REF): `vs. INERTIA-REF — challenges: [C0 mechanism phrase] — vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 3 (`Prerequisite steps: Phase 3 / Phase 4 SOURCE row`). Reads slot 0 (FOCUS-STATE, PREFLIGHT > EXECUTION DEPENDENCY) to determine active/vacuous path for slot 5. Apply GATE 3. SOURCE is row 1. When slot 0 = inactive, slot 5 satisfies by vacuous satisfaction.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — fills slot 4; must be the first row of this table | **Proof structure failure** — SOURCE must appear first; absent or malformed SOURCE blocks all subsequent rows |
| REDUCTION-1 | `NO — {one sentence showing what is lost if the focus dimension is dropped}` | **Proof structure failure** — if YES, gap producible from map alone; discard |
| REDUCTION-2 | `NO — {one sentence showing what is lost if the competitive map is dropped}` | **Proof structure failure** — if YES, gap producible from focus alone; discard |
| THEREFORE | `{one sentence naming the gap requiring both dimensions simultaneously}` — fills slot 5: `REDUCTION-1 NO: [sentence] \| REDUCTION-2 NO: [sentence] \| THEREFORE: [sentence]` | **Proof structure failure** — THEREFORE blocked until both reductions answer NO; retroactive construction is a proof structure failure |

NOT ACCEPTABLE: Writing THEREFORE first and constructing REDUCTION rows retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 4 (`Prerequisite steps: Phase 4`). Write 2-5 findings. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural): `Row C{N}, {attribute}: "{value}"` — name-only entries malformed; apply GATE 2.

**INERTIA-REF-DELTA column** (structural — fills slot 6, "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — every finding row cites INERTIA-REF by token name; "N/A" malformed.

For the cross-dimensional finding row: Claim = THEREFORE sentence; Anchor = SOURCE value; adjacent indented block = slot 5 proof string — apply GATE 3. When slot 0 = inactive, no proof block required.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` — re-run GATE 0 with new value | Slot 0 (FOCUS-STATE) re-written at GATE 0 Write row: `FOCUS-STATE = {active: {new_dimension}}`; SOURCE slot re-identified; slot 5 rebuilt: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`; if activating from inactive, slot 5 changes from vacuous to pipe-delimited proof string; Focus column added to Phase 2 table | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows including Write row — new slot 0 required before Phase 4 re-runs), GATE 3 (all rows) — writing new THEREFORE without rerunning both reductions is a **proof rerun failure** |
| 2 | Add competitor | Competitor name + context for WebSearch | New row (slot 2); WHITESPACE VALIDATION re-run — vs-INERTIA-REF uses ternary-token format; slot 3 re-evaluated | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation), GATE 2 (anchor format; ABSENCE-EVIDENCE for all whitespace candidates) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row; slot 6 cells updated; Phase 3 vs-INERTIA-REF rows re-classified in ternary-token format; Phase 4 proof reviewed — if baseline shifts, rebuild all four rows | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows), 5 (if baseline shifts) | GATE 4 (all rows), GATE 3 (if slot 5 rebuild required) |

---

## V-02 — Output format (slot 5 vacuous path as named structural token)

**Axis:** Output format — slot 5's inactive path is given a named structural token `VACUOUS-5: focus-inactive`. Previously the focus-inactive branch granted "vacuous satisfaction" — a prose permission with no required output format. A prose permission cannot be checked by token presence the way the active path is checked by pipe-delimiter count. The token `VACUOUS-5: focus-inactive` makes both paths of slot 5 format-verifiable.

**Hypothesis:** The active path of slot 5 is structurally strong: three pipe-delimited components, each with a required form, checked by GATE 3. The inactive path has no output format at all — "vacuous satisfaction" means the model is permitted to leave slot 5 empty or write anything. This asymmetry means the inactive path is verified by absence of a format violation rather than presence of a correct format. Adding `VACUOUS-5: focus-inactive` closes this asymmetry: a reviewer checks slot 5 by asking "is this the pipe-delimited proof string OR the vacuous token?" — either answer is a pass; any other value is a collection gate failure. GATE 0's inactive branch, slot 5's OUTPUT CONTRACTS entry, and Phase 4's table instruction all name the token explicitly.

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
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding | Required by slot 5; must appear first before any reduction row |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence — what is lost if the focus dimension is dropped}] \| REDUCTION-2 NO: [{one sentence — what is lost if the competitive map is dropped}] \| THEREFORE: [{gap sentence requiring both dimensions simultaneously}]` — or — `VACUOUS-5: focus-inactive` when GATE 0 focus-inactive branch applies | Phase 4 — Cross-Dimensional Finding | Requires slot 4 (SOURCE) and slot 1 (INERTIA-REF) when focus active; slot 5 = `VACUOUS-5: focus-inactive` when focus inactive; any value other than these two valid formats is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 — Findings Table | Derived from slot 1 (root) — slot 1 must be written at GATE 4 |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### GATE 0: FOCUS GATE

Resolve focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all three rows before proceeding. The focus state determines which of two valid formats slot 5 must take.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` is set to a recognized value (`market-sizing`, `positioning-framework`) — OR — `focus:` is not set; infer from repo context (README, CLAUDE.md) before defaulting to none | **Focus detection failure** — unrecognized or ambiguous focus value; resolve before proceeding |
| Focus-active branch | When focus is set: Focus column added to Phase 2 table; slot 5 fills as full pipe-delimited proof string (`REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`); Phase 4 proof table required; GATE 3 applies | **Focus activation failure** — Focus column omitted or slot 5 not pipe-delimited when focus is set |
| Focus-inactive branch | When focus is not set: Focus column not added to Phase 2 table; slot 5 = `VACUOUS-5: focus-inactive`; Phase 4 still runs but skips REDUCTION and THEREFORE rows; an empty slot 5 does not satisfy — the token must appear | **Focus inactivation failure** — Focus column present when focus not set; or slot 5 empty or prose instead of `VACUOUS-5: focus-inactive` |

NOT ACCEPTABLE (slot 5, inactive): empty cell — **collection gate failure**
NOT ACCEPTABLE (slot 5, inactive): "Focus not active; this slot passes by vacuous satisfaction." — prose — **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Step-level execution ordering. GATE 4 is the data-dependency root (`Prerequisite steps: None (root)`). An **execution dependency violation** occurs when a step begins before its declared "Reads slot" value has been written.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and all other phases** | None (root) |
| Phase 1 | — | TOPIC, FOCUS tokens | Reads repo context before Phase 2 | GATE 4 |
| Phase 2 (per competitor row) | 1 — INERTIA-REF (C0 row) | 2 — Anchor column value | GATE 1 and GATE 2 per row; Focus column per GATE 0 | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 — Anchor column value | 3 — Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF uses slot 6 ternary-token format | Phase 2 |
| Phase 4, SOURCE row | 2 — Anchor column value (named cell) | 4 — SOURCE slot | SOURCE row is row 1; before any REDUCTION row | Phase 3 |
| Phase 4, REDUCTION + THEREFORE rows | 4 — SOURCE slot (written), 1 — INERTIA-REF (comparator baseline) | 5 — Focus-scope evidence | Active: both REDUCTION rows NO before THEREFORE; slot 5 as pipe-delimited string. Inactive (GATE 0): slot 5 = `VACUOUS-5: focus-inactive`; skip REDUCTION and THEREFORE rows | Phase 4 SOURCE row |
| Phase 5 (per finding row) | 1 — INERTIA-REF (DELTA column), 2 — Anchor column value | 6 — INERTIA-REF-DELTA | GATE 4 row 3 per row | Phase 4 |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite before outputting |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff — no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is the first row of the Phase 4 proof table; slot 4 filled before any reduction row | **Proof structure failure** — SOURCE must be first |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** — both required; either YES means discard |
| THEREFORE blocked until reductions complete | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** — THEREFORE blocked; retroactive construction is a proof structure failure |

NOT ACCEPTABLE: Writing THEREFORE first and constructing REDUCTION rows retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root: `Prerequisite steps: None (root)` per PREFLIGHT > EXECUTION DEPENDENCY.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction — not a category label | **Inertia naming failure** — category label not accepted; resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (root, PREFLIGHT > OUTPUT CONTRACTS); root step complete | **Inertia write failure** — must be written here; return before Phase 1 begins |
| Per-finding citation required | Each finding in Phase 5: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — fills slot 6 | **Inertia citation failure** — add comparison clause before outputting |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

C0 enters as Row C0 with all columns. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column per GATE 0 (PREFLIGHT).

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural): `Row C{N}, {attribute}: "{value}"` — name-only cells malformed; apply GATE 2.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table. CANDIDATE row first.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — declared before evidence | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row | **Whitespace gate failure** — bare assertion does not satisfy |
| GAP-CONFIRMED | `Gap confirmed: ...` or `Gap not confirmed: ...; select a different candidate` | **Whitespace gate failure** — non-absent value stops the candidate |
| vs-INERTIA-REF | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — ternary token required | **Whitespace INERTIA-REF format failure** — prose without ternary token; "N/A" not permitted |

NOT ACCEPTABLE: Bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: Prose in vs-INERTIA-REF without ternary token — **whitespace INERTIA-REF format failure**
ACCEPTABLE (vs-INERTIA-REF): `vs. INERTIA-REF — contextualizes: [mechanism phrase] — vacant attribute absent even from C0`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. When GATE 0 focus-inactive branch applies: output `VACUOUS-5: focus-inactive` in the THEREFORE row position — fills slot 5; skip REDUCTION-1 and REDUCTION-2 rows. An empty slot 5 or prose does not satisfy (see GATE 0 inactive branch and PREFLIGHT > OUTPUT CONTRACTS slot 5 format).

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — fills slot 4; must be row 1 | **Proof structure failure** — SOURCE must appear first |
| REDUCTION-1 | `NO — {one sentence showing what is lost if focus dimension dropped}` — skip when focus inactive | **Proof structure failure** — if YES, discard |
| REDUCTION-2 | `NO — {one sentence showing what is lost if competitive map dropped}` — skip when focus inactive | **Proof structure failure** — if YES, discard |
| THEREFORE | Active: `{gap sentence}` — fills slot 5 as pipe-delimited string. Inactive: `VACUOUS-5: focus-inactive` — fills slot 5 | **Proof structure failure** (active): THEREFORE blocked until both reductions NO. **Collection gate failure** (inactive): empty or prose slot 5 not accepted |

NOT ACCEPTABLE: THEREFORE first, REDUCTION rows retroactively — **proof structure failure**
NOT ACCEPTABLE: Empty THEREFORE when focus inactive — output `VACUOUS-5: focus-inactive` — **collection gate failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column**: `Row C{N}, {attribute}: "{value}"` — name-only malformed; apply GATE 2.

**INERTIA-REF-DELTA column** (fills slot 6): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` — every row; "N/A" malformed.

For cross-dimensional finding row: Claim = THEREFORE; Anchor = SOURCE; adjacent block = slot 5 proof string — apply GATE 3. When focus inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate from inactive) | SOURCE slot re-identified; slot 5 rebuilt as pipe-delimited string (if activating from inactive: slot 5 changes from `VACUOUS-5: focus-inactive` to proof string; Focus column added to Phase 2 table) | 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (focus-active branch re-confirmed), GATE 3 (all rows) — writing new THEREFORE without rerunning both reductions is a **proof rerun failure** |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); WHITESPACE VALIDATION re-run — vs-INERTIA-REF uses ternary-token format; slot 3 re-evaluated | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation), GATE 2 (anchor format; ABSENCE-EVIDENCE for all whitespace candidates) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row; slot 6 cells updated; Phase 3 vs-INERTIA-REF rows re-classified; Phase 4 proof reviewed | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows), 5 (if baseline shifts) | GATE 4 (all rows), GATE 3 (if slot 5 rebuild required) |

---

## V-03 — Lifecycle emphasis (GATE 0 listed as Step 0 in EXECUTION DEPENDENCY)

**Axis:** Lifecycle emphasis — GATE 0 (FOCUS GATE) is added as Step 0 in the EXECUTION DEPENDENCY table with `Prerequisite steps: -- (pre-DAG)`. Previously GATE 0 was a named PREFLIGHT subsection before EXECUTION DEPENDENCY — its execution position was inferrable from section order but not recorded in the dependency table itself. Adding GATE 0 to the table makes the complete execution sequence machine-readable from a single table. A note distinguishes pre-DAG steps (executed in PREFLIGHT reading order) from DAG steps (executed in slot-dependency order). GATE 4 retains `None (root)` as the data-dependency root.

**Hypothesis:** The EXECUTION DEPENDENCY table has 7 rows capturing the data dependency DAG from GATE 4 (root) through Phase 5. GATE 0 is excluded because it produces no slot artifact — its execution is sequential by PREFLIGHT position, not by slot dependency. But GATE 0 determines the active/vacuous path for slot 5, so its execution position is material. Adding GATE 0 as Step 0 with `-- (pre-DAG)` closes the gap: the table covers the full execution lifecycle. The `-- (pre-DAG)` marker distinguishes GATE 0's execution logic from DAG steps, preventing misreading of GATE 0 as a data dependency prerequisite to GATE 4.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first. GATE 0 (FOCUS GATE) follows — focus state resolved before step ordering is read. EXECUTION DEPENDENCY follows; GATE 0 is listed as Step 0 to make the complete execution sequence machine-readable. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root — no upstream dependency; slots 5 and 6 require this token |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 values at Phase 5 |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding | Required by slot 5; must appear first |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence — what is lost if the focus dimension is dropped}] \| REDUCTION-2 NO: [{one sentence — what is lost if the competitive map is dropped}] \| THEREFORE: [{gap sentence requiring both dimensions simultaneously}]` — or vacuous satisfaction when GATE 0 focus-inactive branch applies (see EXECUTION DEPENDENCY Step 0) | Phase 4 — Cross-Dimensional Finding | Requires slot 4 (SOURCE) and slot 1 (INERTIA-REF) when focus active; vacuous when focus inactive |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 — Findings Table | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### GATE 0: FOCUS GATE

Resolve focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all three rows before proceeding. This gate is listed as Step 0 in PREFLIGHT > EXECUTION DEPENDENCY (`Prerequisite steps: -- (pre-DAG)`) to make its execution position machine-readable from the dependency table.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` is set to a recognized value (`market-sizing`, `positioning-framework`) — OR — `focus:` is not set; infer from repo context (README, CLAUDE.md) before defaulting to none | **Focus detection failure** — unrecognized or ambiguous value; resolve before proceeding |
| Focus-active branch | When focus is set: Focus column added to Phase 2 table; slot 5 fills as pipe-delimited proof string; Phase 4 proof table required; GATE 3 applies | **Focus activation failure** — Focus column omitted or slot 5 declared vacuously when focus is set |
| Focus-inactive branch | When focus is not set: Focus column not added to Phase 2 table; slot 5 satisfies by vacuous satisfaction; Phase 4 still runs | **Focus inactivation failure** — Focus column present when focus is not set |

---

### EXECUTION DEPENDENCY

Step-level execution ordering covering the full lifecycle. Step 0 (GATE 0) is a pre-DAG step: it executes in PREFLIGHT reading order before any numbered phase. DAG steps execute in slot-dependency order. GATE 4 is the data-dependency root (`Prerequisite steps: None (root)`). An **execution dependency violation** occurs when a DAG step begins before its "Reads slot" value is written; a **pre-DAG ordering violation** occurs when Phase 1 begins before GATE 0 and GATE 4 have both completed.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | — | — | Pre-DAG step: executes before any numbered phase; focus state resolved here determines slot 5 active/vacuous path | -- (pre-DAG) |
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and all other phases**; data-dependency root | None (root) |
| Phase 1 | — | TOPIC, FOCUS tokens | Reads repo context before Phase 2 | GATE 4 |
| Phase 2 (per competitor row) | 1 — INERTIA-REF (C0 row) | 2 — Anchor column value | GATE 1 and GATE 2 per row; Focus column per GATE 0 (Step 0) | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 — Anchor column value | 3 — Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF uses slot 6 ternary-token format | Phase 2 |
| Phase 4, SOURCE row | 2 — Anchor column value (named cell) | 4 — SOURCE slot | SOURCE row is row 1; before any REDUCTION row | Phase 3 |
| Phase 4, REDUCTION + THEREFORE rows | 4 — SOURCE slot (written), 1 — INERTIA-REF (comparator baseline) | 5 — Focus-scope evidence | Both REDUCTION rows NO before THEREFORE; slot 5 as pipe-delimited string; vacuous if GATE 0 focus-inactive (Step 0) | Phase 4 SOURCE row |
| Phase 5 (per finding row) | 1 — INERTIA-REF (DELTA column), 2 — Anchor column value | 6 — INERTIA-REF-DELTA | GATE 4 row 3 per row | Phase 4 |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite before outputting |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff — no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is the first row of the Phase 4 proof table; slot 4 filled before any reduction row | **Proof structure failure** — SOURCE must be first |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** — either YES means discard |
| THEREFORE blocked until reductions complete | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** — retroactive construction is a proof structure failure |

NOT ACCEPTABLE: Writing THEREFORE first and constructing REDUCTION rows retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root: `Prerequisite steps: None (root)` per PREFLIGHT > EXECUTION DEPENDENCY; GATE 0 (Step 0, pre-DAG) determined focus state before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction — not a category label | **Inertia naming failure** — category label not a mechanism; resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (root); root step complete | **Inertia write failure** — must be written here; return before Phase 1 begins |
| Per-finding citation required | Each finding in Phase 5: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — fills slot 6 | **Inertia citation failure** — add comparison clause before outputting |

---

### PHASE 1: CONTEXT

Runs after GATE 4 (`Prerequisite steps: GATE 4`). Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 1 (`Prerequisite steps: Phase 1`). C0 is the entity whose stickiness was resolved in GATE 4 (data-dependency root). C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column per GATE 0 result (Step 0, pre-DAG, PREFLIGHT > EXECUTION DEPENDENCY).

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural): `Row C{N}, {attribute}: "{value}"` — name-only cells malformed; apply GATE 2.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 2 (`Prerequisite steps: Phase 2`). For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table. CANDIDATE row first.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — declared before evidence | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row | **Whitespace gate failure** — bare assertion does not satisfy |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}]` or `Gap not confirmed: Row C{N} provides [{value}]; select a different candidate` | **Whitespace gate failure** — non-absent value stops the candidate |
| vs-INERTIA-REF | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — ternary token required | **Whitespace INERTIA-REF format failure** — prose without ternary token; "N/A" not permitted |

NOT ACCEPTABLE: Bare assertion in ABSENCE-EVIDENCE — **whitespace gate failure**
NOT ACCEPTABLE: Prose in vs-INERTIA-REF without ternary token — **whitespace INERTIA-REF format failure**
ACCEPTABLE: `vs. INERTIA-REF — reinforces: [mechanism phrase] — vacant attribute is same gap C0 exploits`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 3. Apply GATE 3. SOURCE is row 1. If GATE 0 focus-inactive branch applies (Step 0, pre-DAG, PREFLIGHT > EXECUTION DEPENDENCY), slot 5 satisfies by vacuous satisfaction.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — fills slot 4; must be first row | **Proof structure failure** — SOURCE must appear first |
| REDUCTION-1 | `NO — {one sentence showing what is lost if focus dimension dropped}` | **Proof structure failure** — if YES, discard |
| REDUCTION-2 | `NO — {one sentence showing what is lost if competitive map dropped}` | **Proof structure failure** — if YES, discard |
| THEREFORE | `{gap sentence requiring both dimensions}` — fills slot 5 as pipe-delimited string | **Proof structure failure** — THEREFORE blocked until both reductions NO |

NOT ACCEPTABLE: Writing THEREFORE first and constructing REDUCTION rows retroactively — **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 4 (`Prerequisite steps: Phase 4`). Write 2-5 findings. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column**: `Row C{N}, {attribute}: "{value}"` — name-only malformed; apply GATE 2.

**INERTIA-REF-DELTA column** (fills slot 6): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` — every row; "N/A" malformed.

For cross-dimensional finding: Claim = THEREFORE; Anchor = SOURCE; adjacent block = slot 5 — apply GATE 3.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` — re-run GATE 0 (Step 0, pre-DAG, PREFLIGHT > EXECUTION DEPENDENCY) focus-active branch | SOURCE slot re-identified; slot 5 rebuilt: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`; cross-dimensional finding updated | 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (focus-active branch — pre-DAG step re-runs before Phase 4), GATE 3 (all rows) — writing new THEREFORE without rerunning reductions is a **proof rerun failure** |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); WHITESPACE VALIDATION re-run — vs-INERTIA-REF uses ternary-token format; slot 3 re-evaluated | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation), GATE 2 (anchor format; ABSENCE-EVIDENCE for all whitespace candidates) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row (data-dependency root, `Prerequisite steps: None (root)`); slot 6 cells updated; Phase 3 vs-INERTIA-REF rows re-classified; Phase 4 proof reviewed | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows), 5 (if baseline shifts) | GATE 4 (all rows), GATE 3 (if slot 5 rebuild required) |

---

## V-04 — Combined A+B (FOCUS-STATE slot 0 + vacuous token)

**Axis:** Combined A+B — V-01's FOCUS-STATE slot 0 (GATE 0 gains Write row) plus V-02's `VACUOUS-5: focus-inactive` token. GATE 0 now both writes slot 0 (FOCUS-STATE) and prescribes the exact inactive-path format for slot 5. Slot 5's "Required by" column names slot 0 as its path-selecting dependency and specifies both valid formats explicitly.

**Hypothesis:** V-01 makes the focus-gate output contract-visible (slot 0 in OUTPUT CONTRACTS). V-02 makes the inactive path format-verifiable (named token rather than prose permission). Together, a reader of OUTPUT CONTRACTS sees: slot 0 (focus state, written by GATE 0), and slot 5 (two exact formats — one active, one inactive — path selection by slot 0). No gate narrative is required to understand either format or the path logic. AMEND row 1 names both format transitions, making the shift between `VACUOUS-5: focus-inactive` and the pipe-delimited proof string explicit.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first (slots 0-6). GATE 0 (FOCUS GATE) follows — writes slot 0 and prescribes both slot 5 formats. EXECUTION DEPENDENCY follows. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` — or — `{inactive}` | GATE 0 (Write row, below) | No upstream dependency; slot 5 reads slot 0 to select format: pipe-delimited proof string (active) or `VACUOUS-5: focus-inactive` (inactive) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root — no upstream dependency; slots 5 and 6 require this token |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5 |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding | Required by slot 5; must appear first |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence}] \| REDUCTION-2 NO: [{one sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active — or — `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 — Cross-Dimensional Finding | Requires slot 0 (path selector); active also requires slot 4 (SOURCE) and slot 1 (INERTIA-REF); any value other than these two formats is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 — Findings Table | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows before proceeding. Fills slot 0 (FOCUS-STATE) — slot 5 reads slot 0 for format selection.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` is set to a recognized value (`market-sizing`, `positioning-framework`) — OR — `focus:` is not set; infer from repo context before defaulting to none | **Focus detection failure** — unrecognized or ambiguous value; resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` — fills slot 0 (PREFLIGHT > OUTPUT CONTRACTS) | **Focus write failure** — token must be written at this row; slot 5 format undefined until slot 0 is written |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table; slot 5 fills as pipe-delimited proof string; Phase 4 proof table required; GATE 3 applies | **Focus activation failure** — Focus column omitted or slot 5 not pipe-delimited when slot 0 = active |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; slot 5 = `VACUOUS-5: focus-inactive`; empty slot 5 or prose does not satisfy | **Focus inactivation failure** — Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell — **collection gate failure**
NOT ACCEPTABLE (slot 5, inactive): "Focus not active." — prose — **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

GATE 4 is the data-dependency root (`Prerequisite steps: None (root)`). Slot 0 (FOCUS-STATE) is written by GATE 0 (pre-DAG) — Phase 4 reads slot 0 for path selection.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and all other phases** | None (root) |
| Phase 1 | — | TOPIC, FOCUS tokens | Reads repo context before Phase 2 | GATE 4 |
| Phase 2 (per competitor row) | 1 — INERTIA-REF | 2 — Anchor column value | GATE 1 and GATE 2 per row; Focus column per slot 0 | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 — Anchor column value | 3 — Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF uses ternary-token format | Phase 2 |
| Phase 4, SOURCE row | 2 — Anchor column value (named cell) | 4 — SOURCE slot | SOURCE row is row 1; before any REDUCTION row | Phase 3 |
| Phase 4, REDUCTION + THEREFORE rows | 0 — FOCUS-STATE (path selector), 4 — SOURCE slot, 1 — INERTIA-REF | 5 — Focus-scope evidence | Active: pipe-delimited string. Inactive: `VACUOUS-5: focus-inactive`. Empty or prose slot 5 is a **collection gate failure** | Phase 4 SOURCE row |
| Phase 5 (per finding row) | 1 — INERTIA-REF, 2 — Anchor column value | 6 — INERTIA-REF-DELTA | GATE 4 row 3 per row | Phase 4 |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column | **Citation gate failure** — suppress row; run WebSearch |
| Citation in row, not footnote | URL inline in the table row | **Citation gate failure** — relocate into row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` | **Whitespace gate failure** — bare assertion does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff — no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is first in Phase 4 proof table; slot 4 filled before any reduction row | **Proof structure failure** |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** — either YES means discard |
| THEREFORE blocked | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** — retroactive construction fails |

NOT ACCEPTABLE: THEREFORE first, REDUCTION rows retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root. Slot 0 written by GATE 0 before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction — not a category label | **Inertia naming failure** |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` — fills slot 1 (root) | **Inertia write failure** |
| Per-finding citation required | Each finding: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {mechanism phrase}` — fills slot 6 | **Inertia citation failure** |

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column per slot 0 (FOCUS-STATE, PREFLIGHT > OUTPUT CONTRACTS).

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural): `Row C{N}, {attribute}: "{value}"` — name-only cells malformed.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

4-row WHITESPACE VALIDATION table per candidate attribute. CANDIDATE row first.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row | **Whitespace gate failure** |
| GAP-CONFIRMED | `Gap confirmed: ...` or `Gap not confirmed: ...; select a different candidate` | **Whitespace gate failure** |
| vs-INERTIA-REF | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {mechanism phrase}` — ternary token required | **Whitespace INERTIA-REF format failure** |

NOT ACCEPTABLE: Bare assertion — **whitespace gate failure**; prose without ternary token — **whitespace INERTIA-REF format failure**
ACCEPTABLE (vs-INERTIA-REF): `vs. INERTIA-REF — contextualizes: [mechanism phrase] — vacant even from C0`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 0 (FOCUS-STATE) for path selection. Apply GATE 3. SOURCE is row 1. When slot 0 = inactive: output `VACUOUS-5: focus-inactive` in the THEREFORE row position; skip REDUCTION rows. Empty or prose slot 5 fails.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — fills slot 4; row 1 | **Proof structure failure** |
| REDUCTION-1 | `NO — {what is lost if focus dimension dropped}` — skip when slot 0 = inactive | **Proof structure failure** |
| REDUCTION-2 | `NO — {what is lost if competitive map dropped}` — skip when slot 0 = inactive | **Proof structure failure** |
| THEREFORE | Active: gap sentence → slot 5 pipe-delimited. Inactive: `VACUOUS-5: focus-inactive` → slot 5 | Active: THEREFORE blocked until both NO. Inactive: empty or prose is **collection gate failure** |

NOT ACCEPTABLE: THEREFORE first, REDUCTION rows retroactively — **proof structure failure**
NOT ACCEPTABLE: Empty slot 5 when slot 0 = inactive — output `VACUOUS-5: focus-inactive` — **collection gate failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column**: `Row C{N}, {attribute}: "{value}"` — name-only malformed.
**INERTIA-REF-DELTA column**: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {mechanism phrase}` — every row; "N/A" malformed.

When slot 0 = inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO.

---

### AMEND

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate focus) | Slot 0 re-written: `FOCUS-STATE = {active: {new_dimension}}`; slot 4 SOURCE re-identified; slot 5 rebuilt (activating: changes from `VACUOUS-5: focus-inactive` to pipe-delimited proof string; Focus column added to Phase 2 table) | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows including Write row), GATE 3 (all rows) — new THEREFORE without rerunning reductions is a **proof rerun failure** |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); WHITESPACE VALIDATION re-run; vs-INERTIA-REF uses ternary-token format; slot 3 re-evaluated | 2, 3 | GATE 1 (citation), GATE 2 (anchor; ABSENCE-EVIDENCE for all whitespace candidates) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written; slot 6 cells updated; Phase 3 vs-INERTIA-REF rows re-classified; Phase 4 proof reviewed | 1, 6, 3, 5 (if baseline shifts) | GATE 4 (all rows), GATE 3 (if slot 5 rebuild required) |

---

## V-05 — Combined maximum (FOCUS-STATE slot 0 + vacuous token + GATE 0 in EXECUTION DEPENDENCY)

**Axis:** Maximum — all three R11 innovation axes. V-01: FOCUS-STATE as slot 0, GATE 0 gains Write row. V-02: slot 5 inactive = `VACUOUS-5: focus-inactive`. V-03: GATE 0 listed as Step 0 in EXECUTION DEPENDENCY with `-- (pre-DAG)`. GATE 4's data-dependency root status is now confirmed from five independent structural positions: OUTPUT CONTRACTS slot 1 "Required by: Root" (data root); EXECUTION DEPENDENCY "Reads slot: -- (root)" (data root); EXECUTION DEPENDENCY "Prerequisite steps: None (root)" (step root); OUTPUT CONTRACTS slot 0 "Required by: No upstream dependency" (pre-DAG root, GATE 0); EXECUTION DEPENDENCY Step 0 `-- (pre-DAG)` (ordering that GATE 0 precedes GATE 4 without slot dependency).

**Hypothesis:** R10 V-05 left three residual gaps: GATE 0 produced no named artifact (control-flow only), slot 5's inactive path had no format requirement, and GATE 0 was absent from EXECUTION DEPENDENCY. V-01, V-02, and V-03 address each gap independently. V-05 combines them: a reader of PREFLIGHT can reconstruct the complete output contract (slots 0-6, two valid formats for slot 5), the complete execution sequence (EXECUTION DEPENDENCY rows 0-7, pre-DAG and DAG clearly labeled), and every gate's output artifact (GATE 0 writes slot 0, GATE 4 writes slot 1) — all without reading any phase instruction.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first (slots 0-6). GATE 0 (FOCUS GATE) follows — writes slot 0 (FOCUS-STATE) and prescribes both valid formats for slot 5. EXECUTION DEPENDENCY follows; GATE 0 is listed as Step 0 (`-- (pre-DAG)`), GATE 4 as data-dependency root (`None (root)`). Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` — or — `{inactive}` | GATE 0 (Write row, below) | No upstream dependency; slot 5 reads slot 0 to select format (active: pipe-delimited proof string; inactive: `VACUOUS-5: focus-inactive`) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root — no upstream dependency; slots 5 and 6 require this token |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5 |
| 3 | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — first row of the Phase 4 proof table | Phase 4 — Cross-Dimensional Finding | Required by slot 5; must appear first |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{one sentence}] \| REDUCTION-2 NO: [{one sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active — or — `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 — Cross-Dimensional Finding | Requires slot 0 (path selector); active also requires slot 4 (SOURCE) and slot 1 (INERTIA-REF); any value other than these two formats is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 — Findings Table | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the "Filled by phase" column.

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows before proceeding. Listed as Step 0 in PREFLIGHT > EXECUTION DEPENDENCY (`Prerequisite steps: -- (pre-DAG)`). Fills slot 0 (FOCUS-STATE) and determines which of the two valid formats slot 5 must take.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` is set to a recognized value (`market-sizing`, `positioning-framework`) — OR — `focus:` is not set; infer from repo context (README, CLAUDE.md) before defaulting to none | **Focus detection failure** — unrecognized or ambiguous value; resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` — fills slot 0 (PREFLIGHT > OUTPUT CONTRACTS); token available to Phase 4 for slot 5 path selection | **Focus write failure** — token must be written at this row; slot 5 format undefined until slot 0 is written |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table; slot 5 fills as pipe-delimited proof string; Phase 4 proof table required; GATE 3 applies | **Focus activation failure** — Focus column omitted or slot 5 not pipe-delimited when slot 0 = active |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; slot 5 = `VACUOUS-5: focus-inactive`; empty slot 5 or prose does not satisfy | **Focus inactivation failure** — Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell — **collection gate failure**
NOT ACCEPTABLE (slot 5, inactive): "Focus not active; vacuous satisfaction." — prose — **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Step-level execution ordering covering the full lifecycle from focus-gate evaluation through findings output. Step 0 (GATE 0) is a pre-DAG step: executes in PREFLIGHT reading order before any numbered phase. DAG steps execute in slot-dependency order. GATE 4 is the data-dependency root (`Prerequisite steps: None (root)`). An **execution dependency violation** occurs when a DAG step begins before its "Reads slot" value is written; a **pre-DAG ordering violation** occurs when Phase 1 begins before GATE 0 and GATE 4 have completed.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | — | 0 — FOCUS-STATE | Pre-DAG step: executes before any numbered phase; writes slot 0 (FOCUS-STATE); determines slot 5 format (active: pipe-delimited proof string; inactive: `VACUOUS-5: focus-inactive`) | -- (pre-DAG) |
| GATE 4 (Write row) | — (root) | 1 — INERTIA-REF | **Must execute before Phase 1 and all other phases**; data-dependency root | None (root) |
| Phase 1 | — | TOPIC, FOCUS tokens | Reads repo context before Phase 2 | GATE 4 |
| Phase 2 (per competitor row) | 1 — INERTIA-REF (C0 row) | 2 — Anchor column value | GATE 1 and GATE 2 per row; Focus column per slot 0 (written by GATE 0, Step 0) | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 — Anchor column value | 3 — Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF uses slot 6 ternary-token format | Phase 2 |
| Phase 4, SOURCE row | 2 — Anchor column value (named cell) | 4 — SOURCE slot | SOURCE row is row 1; before any REDUCTION row | Phase 3 |
| Phase 4, REDUCTION + THEREFORE rows | 0 — FOCUS-STATE (path: active vs. inactive), 4 — SOURCE slot, 1 — INERTIA-REF | 5 — Focus-scope evidence | Active (slot 0 = active): both REDUCTION rows NO before THEREFORE; slot 5 as pipe-delimited string. Inactive (slot 0 = inactive): slot 5 = `VACUOUS-5: focus-inactive`. Empty or prose slot 5 is a **collection gate failure** | Phase 4 SOURCE row |
| Phase 5 (per finding row) | 1 — INERTIA-REF (DELTA column), 2 — Anchor column value | 6 — INERTIA-REF-DELTA | GATE 4 row 3 per row | Phase 4 |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column | **Citation gate failure** — suppress row; run WebSearch |
| Citation in row, not footnote | URL inline in the table row | **Citation gate failure** — relocate into row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` | **Whitespace gate failure** — bare assertion does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff — no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is first in the Phase 4 proof table; slot 4 filled before any reduction row | **Proof structure failure** — SOURCE must be first |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** — either YES means discard |
| THEREFORE blocked | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** — retroactive construction fails |

NOT ACCEPTABLE: Writing THEREFORE first and constructing REDUCTION rows retroactively — **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root: `Prerequisite steps: None (root)` per PREFLIGHT > EXECUTION DEPENDENCY; slot 1 (INERTIA-REF) is the root per OUTPUT CONTRACTS; GATE 0 (Step 0, pre-DAG) wrote slot 0 (FOCUS-STATE) before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction — not a category label | **Inertia naming failure** — category label not accepted; resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — fills slot 1 (root); root step complete (`Prerequisite steps: None (root)`) | **Inertia write failure** — must be written here; return before Phase 1 begins |
| Per-finding citation required | Each finding in Phase 5: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — fills slot 6 | **Inertia citation failure** — add comparison clause before outputting |

---

### PHASE 1: CONTEXT

Runs after GATE 4 (`Prerequisite steps: GATE 4`). Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 1 (`Prerequisite steps: Phase 1`). C0 is the entity whose stickiness was resolved in GATE 4 (data-dependency root, Step 1, PREFLIGHT > EXECUTION DEPENDENCY). C0 enters as Row C0 with all columns. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column per slot 0 (FOCUS-STATE, written by GATE 0, Step 0, PREFLIGHT > EXECUTION DEPENDENCY).

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only cells syntactically malformed; apply GATE 2.

Note which mechanism phrases and focus-column values relate to INERTIA-REF (slot 1, root) — fills slot 6 (INERTIA-REF-DELTA) at Phase 5.

---

### PHASE 3: WHITESPACE (fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 2 (`Prerequisite steps: Phase 2`). For each candidate whitespace attribute, execute the 4-row WHITESPACE VALIDATION table. CANDIDATE row first.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` — declared before any absence evidence is gathered | **Whitespace naming failure** — unnamed CANDIDATE blocks ABSENCE-EVIDENCE |
| ABSENCE-EVIDENCE | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` for every competitor row (including C0) — fills slot 3 | **Whitespace gate failure** — per-row evidence required; bare assertion does not satisfy |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}] — attribute-level uncontested` — or — `Gap not confirmed: Row C{N} provides [{non-absent value}]; select a different candidate` | **Whitespace gate failure** — non-absent value stops the candidate; restart the validation table |
| vs-INERTIA-REF | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — ternary token required; same format as slot 6 (INERTIA-REF-DELTA) | **Whitespace INERTIA-REF format failure** — prose without ternary token; "N/A" not permitted |

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "vs. INERTIA-REF — adjacent to C0's workflow" — prose without ternary token — **whitespace INERTIA-REF format failure**
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before ABSENCE-EVIDENCE is complete for all rows — **whitespace gate failure**
ACCEPTABLE (vs-INERTIA-REF): `vs. INERTIA-REF — challenges: [C0 mechanism phrase] — vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 — SOURCE slot, and slot 5 — Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 3 (`Prerequisite steps: Phase 3 / Phase 4 SOURCE row`). Reads slot 0 (FOCUS-STATE, written by GATE 0, Step 0, PREFLIGHT > EXECUTION DEPENDENCY) for path selection. Apply GATE 3. SOURCE is row 1. When slot 0 = inactive: output `VACUOUS-5: focus-inactive` in the THEREFORE row position; skip REDUCTION rows. Empty slot 5 or prose does not satisfy.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` — fills slot 4; must be row 1 | **Proof structure failure** — SOURCE must appear first |
| REDUCTION-1 | `NO — {one sentence showing what is lost if focus dimension dropped}` — skip when slot 0 = inactive | **Proof structure failure** — if YES, discard |
| REDUCTION-2 | `NO — {one sentence showing what is lost if competitive map dropped}` — skip when slot 0 = inactive | **Proof structure failure** — if YES, discard |
| THEREFORE | Active: `{gap sentence}` → slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`. Inactive: `VACUOUS-5: focus-inactive` → slot 5 = `VACUOUS-5: focus-inactive` | Active: THEREFORE blocked until both NO. Inactive: empty or prose slot 5 is a **collection gate failure** |

NOT ACCEPTABLE: Writing THEREFORE first and constructing REDUCTION rows retroactively — **proof structure failure**
NOT ACCEPTABLE: Empty THEREFORE when slot 0 = inactive — must output `VACUOUS-5: focus-inactive` — **collection gate failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 — Anchor column value, and slot 6 — INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 4 (`Prerequisite steps: Phase 4`). Write 2-5 findings. Reads slot 1 (INERTIA-REF) and slot 2 (Anchor values). Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only entries syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier — enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural — fills slot 6, "Required by: slot 1, root"): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` — every finding row cites INERTIA-REF by token name; "N/A" malformed.

For the cross-dimensional finding row: Claim = THEREFORE sentence; Anchor = SOURCE value; adjacent indented block = slot 5 proof string — apply GATE 3. When slot 0 = inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate focus) | Slot 0 re-written at GATE 0 Write row (Step 0, pre-DAG, PREFLIGHT > EXECUTION DEPENDENCY): `FOCUS-STATE = {active: {new_dimension}}`; slot 4 SOURCE re-identified; slot 5 rebuilt as pipe-delimited string (activating: changes from `VACUOUS-5: focus-inactive` to proof string; Focus column added to Phase 2 table); cross-dimensional finding updated | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows including Write row — new slot 0 required before Phase 4 runs), GATE 3 (all rows: SOURCE first, both reductions NO, THEREFORE blocked) — writing new THEREFORE without rerunning both reductions is a **proof rerun failure** |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); WHITESPACE VALIDATION re-run for all candidate attributes — vs-INERTIA-REF uses ternary-token format; slot 3 re-evaluated; INERTIA-REF-DELTA (slot 6) reviewed | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation), GATE 2 (anchor format; ABSENCE-EVIDENCE for all whitespace candidates) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row (data-dependency root, `Prerequisite steps: None (root)`, PREFLIGHT > EXECUTION DEPENDENCY); slot 6 cells updated; Phase 3 vs-INERTIA-REF rows re-classified in ternary-token format; Phase 4 proof reviewed — if baseline shifts, rebuild all four proof rows | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA, all finding rows), 3 (vs-INERTIA-REF rows), 5 (Focus-scope evidence, if baseline shifts) | GATE 4 (all rows: stickiness check, write row, per-finding citation), GATE 3 (if slot 5 rebuild required) |

---

```json
{"round": 11, "baseline": "R10 V-05 (C-37 + C-38 + C-39 + C-40 + C-41 + C-42 + all prior)", "new_axes": ["FOCUS-STATE declared as slot 0 in OUTPUT CONTRACTS — GATE 0 gains Write row (same pattern as GATE 4 write row); slot 5 Required by references slot 0 as path-selector dependency; focus-gate output becomes a named data artifact traceable in the contract table", "Slot 5 vacuous-inactive path formatted as named structural token VACUOUS-5: focus-inactive — both slot 5 paths are format-verifiable by token presence; empty slot 5 does not satisfy; prose vacuous-satisfaction description does not satisfy; both paths now have a required output format", "GATE 0 listed as Step 0 in EXECUTION DEPENDENCY with Prerequisite steps: -- (pre-DAG) — complete execution sequence from focus-gate evaluation through Phase 5 is machine-readable from a single table; pre-DAG and DAG steps distinguished by Prerequisite steps marker; GATE 4 retains None (root) as data-dependency root"], "candidate_criteria": ["C-43: FOCUS-STATE declared as slot 0 in OUTPUT CONTRACTS; GATE 0 Write row fills it before GATE 4 runs; slot 5 Required by names slot 0 as path selector; prose GATE 0 with no Write row does not satisfy", "C-44: Slot 5 inactive-path format is VACUOUS-5: focus-inactive (named structural token); empty slot 5 and prose vacuous-satisfaction both fail; both slot 5 paths are format-checkable without prose parsing", "C-45: GATE 0 listed as Step 0 in EXECUTION DEPENDENCY with Prerequisite steps: -- (pre-DAG); GATE 4 retains None (root); GATE 0 absent from EXECUTION DEPENDENCY table does not satisfy even if it is a named PREFLIGHT subsection"]}
```
