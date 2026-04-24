Written to `simulations/quest/variations/discover-competitors-alt-variations-R12-2026-03-17.md`.

---

## R12 Variations Summary

**Base**: V-05 from R11 (C-43 now rubric; C-44 + C-45 inherited). Three new single-axis innovations, two combos.

| Variation | Axis | Innovation |
|-----------|------|-----------|
| **V-01** | Lifecycle emphasis | Phase 2 "Reads slot" explicitly declares `0 -- FOCUS-STATE (Focus column inclusion)` alongside slot 1 — closing the gap between declared EXECUTION DEPENDENCY reads and actual runtime branches |
| **V-02** | Role sequence | Phase 4 gains a **PATH row as row 0** — structural branch router that reads slot 0 and exits inactive path *before* SOURCE is written, making the active/inactive decision a table-level checkpoint |
| **V-03** | Output format | PREFLIGHT gains a **WRITE-TOKEN REGISTRY** table (after OUTPUT CONTRACTS, before GATE 0) — dedicated index of all write-token gate events by gate name, token, slot, and pre-DAG/DAG classification |
| **V-04** | A+B | V-01 + V-02 |
| **V-05** | Maximum | All three |

---

**Three candidate new criteria:**

- **C-44** (V-01): EXECUTION DEPENDENCY "Reads slot" column must exhaustively declare all slot reads including conditional reads. Phase 2 conditionally branches on slot 0 for Focus column inclusion — omitting slot 0 from Phase 2's "Reads slot" cell is an **execution dependency gap**.

- **C-45** (V-02): Phase 4 proof table includes a PATH row as row 0 declaring both branches (active: proceed to SOURCE; inactive: write `VACUOUS-5: focus-inactive` and exit). Extends the C-37 declaration-before-execution principle to Phase 4. Phase 4 without a PATH row does not satisfy even if branching is described in the phase header.

- **C-46** (V-03): PREFLIGHT includes a named WRITE-TOKEN REGISTRY table listing every write-token gate event. The write-token schedule must be discoverable in O(1) from a dedicated table — not only derivable by scanning EXECUTION DEPENDENCY "Writes slot". Structurally complementary to OUTPUT CONTRACTS (slot inventory) and EXECUTION DEPENDENCY (step ordering).

**Key structural property of V-05**: slot 0's complete lifecycle (write → Focus column read → PATH routing → path selection) is now encoded in **five independent structural positions**: OUTPUT CONTRACTS slot 0 "Required by", WRITE-TOKEN REGISTRY row 1, EXECUTION DEPENDENCY Phase 2 "Reads slot", EXECUTION DEPENDENCY Phase 4 PATH row step, and Phase 4 table row 0.
 in Phase 3 and the PATH row in Phase 4. C-45 does not imply C-37; C-37 does not imply C-45.
- C-46 is independent of C-27 (machine-readable phase assignment column) and C-42 (EXECUTION DEPENDENCY): all three encode different facets of execution structure. C-46 encodes the write-token schedule as a first-class table; C-27 encodes slot-fill phase assignment; C-42 encodes step ordering.

| | **V-01** | **V-02** | **V-03** | **V-04** | **V-05** |
|---|---|---|---|---|---|
| **C-43** (FOCUS-STATE as slot 0) | YES | YES | YES | YES | YES |
| **C-44 (R11)** (VACUOUS-5 token) | YES | YES | YES | YES | YES |
| **C-45 (R11)** (GATE 0 in EXEC DEP pre-DAG) | YES | YES | YES | YES | YES |
| **Phase 2 declares slot 0 in Reads slot** | YES (new) | NO | NO | YES | YES |
| **Phase 4 PATH row as row 0** | NO | YES (new) | NO | YES | YES |
| **WRITE-TOKEN REGISTRY in PREFLIGHT** | NO | NO | YES (new) | NO | YES |

---

## V-01 -- Lifecycle emphasis (Phase 2 declares slot 0 as conditional read)

**Axis:** Lifecycle emphasis -- Phase 2's "Reads slot" column in EXECUTION DEPENDENCY gains `0 -- FOCUS-STATE (Focus column inclusion)` alongside `1 -- INERTIA-REF`. V-05 from R11 declared slot 0 as the path-selector for Phase 4 REDUCTION+THEREFORE rows but left Phase 2's conditional read of slot 0 (Focus column presence/absence) invisible in the "Reads slot" column. The rule becomes: every step that conditionally branches on a slot value must declare that slot in its "Reads slot" column.

**Hypothesis:** The "Reads slot" column in EXECUTION DEPENDENCY is the primary mechanism for expressing data-flow edges. Phase 2 branches on slot 0 to decide Focus column inclusion -- a real data-flow edge -- but R11 V-05 lists only slot 1 in Phase 2's "Reads slot" cell. Adding slot 0 closes this gap: a reader of EXECUTION DEPENDENCY can reconstruct the complete data-flow graph by column inspection alone, including conditional reads, without reading phase instruction prose.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first (slots 0-6). GATE 0 follows -- writes slot 0 (FOCUS-STATE). EXECUTION DEPENDENCY follows; Phase 2 "Reads slot" declares both slot 0 (conditional) and slot 1 (primary); GATE 0 is Step 0 (-- (pre-DAG)); GATE 4 is root (None (root)). Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row, below) | No upstream dependency; slot 5 reads slot 0 to select format (active: pipe-delimited proof string; inactive: `VACUOUS-5: focus-inactive`); Phase 2 reads slot 0 for Focus column inclusion |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root -- no upstream dependency; slots 5 and 6 require this token |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5 |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first row of Phase 4 proof table | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; must appear first |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | Requires slot 0 (path selector); active also requires slot 4 (SOURCE) and slot 1 (INERTIA-REF); any other value is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate or phase named in "Filled by phase".

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows before proceeding. Listed as Step 0 in PREFLIGHT > EXECUTION DEPENDENCY (Prerequisite steps: -- (pre-DAG)). Fills slot 0 -- read by Phase 2 (Focus column) and Phase 4 (slot 5 path selection).

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` is set to a recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- unrecognized or ambiguous value; resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0 (PREFLIGHT > OUTPUT CONTRACTS); token available to Phase 2 Focus column and Phase 4 path selection | **Focus write failure** -- token must be written at this row; slot 5 format and Phase 2 Focus column undefined until slot 0 is written |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table (Phase 2 reads slot 0 per EXECUTION DEPENDENCY); slot 5 fills as pipe-delimited proof string; GATE 3 applies | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited when slot 0 = active |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; slot 5 = `VACUOUS-5: focus-inactive`; empty or prose slot 5 does not satisfy | **Focus inactivation failure** -- Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell -- **collection gate failure**
NOT ACCEPTABLE (slot 5, inactive): "Focus not active; vacuous satisfaction." -- prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Step-level execution ordering. Step 0 (GATE 0) is a pre-DAG step. GATE 4 is the data-dependency root (None (root)). The "Reads slot" column declares all slot reads -- including conditional reads. A step that conditionally branches on a slot value must declare that slot in its "Reads slot" column. An omitted conditional read is an **execution dependency gap**.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG step; determines slot 5 format and Phase 2 Focus column inclusion | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all other phases**; data-dependency root | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context before Phase 2 | GATE 4 |
| Phase 2 (per competitor row) | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 row mechanism reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row; Focus column when slot 0 = active; absent when slot 0 = inactive | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF uses slot 6 ternary-token format | Phase 2 |
| Phase 4, SOURCE row | 2 -- Anchor column value (named cell) | 4 -- SOURCE slot | SOURCE row is row 1; before any REDUCTION row | Phase 3 |
| Phase 4, REDUCTION + THEREFORE rows | 0 -- FOCUS-STATE (path selector), 4 -- SOURCE slot, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: both REDUCTION rows NO before THEREFORE; slot 5 pipe-delimited. Inactive: slot 5 = `VACUOUS-5: focus-inactive`. Empty or prose slot 5 is a **collection gate failure** | Phase 4 SOURCE row |
| Phase 5 (per finding row) | 1 -- INERTIA-REF (DELTA column), 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 4 row 3 per row | Phase 4 |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column | **Citation gate failure** -- suppress row; run WebSearch |
| Citation in row, not footnote | URL inline in the table row | **Citation gate failure** -- relocate into row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` -- row reference, attribute name, and quoted value all present | **Anchor gate failure** -- name-only entries do not conform |
| Whitespace absence anchor | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** -- bare assertion does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` -- name-only -- **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff -- no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE row is first in Phase 4 proof table; slot 4 filled before any reduction row | **Proof structure failure** -- SOURCE must be first |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: Writing THEREFORE first and constructing REDUCTION rows retroactively -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root: Prerequisite steps: None (root) per PREFLIGHT > EXECUTION DEPENDENCY; GATE 0 (Step 0, pre-DAG) wrote slot 0 before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- category label not accepted; resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` -- fills slot 1 (root); root step complete | **Inertia write failure** -- must be written here; return before Phase 1 begins |
| Per-finding citation required | Each finding in Phase 5: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` -- fills slot 6 | **Inertia citation failure** -- add comparison clause before outputting |

---

### PHASE 1: CONTEXT

Runs after GATE 4 (Prerequisite steps: GATE 4). Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 1 (Prerequisite steps: Phase 1). Reads slot 0 (FOCUS-STATE, written by GATE 0, Step 0) and slot 1 (INERTIA-REF, data-dependency root) per PREFLIGHT > EXECUTION DEPENDENCY. C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column when slot 0 = active; absent when slot 0 = inactive.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural -- fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` -- name-only cells syntactically malformed; apply GATE 2.

---

### PHASE 3: WHITESPACE (fills slot 3 -- Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 2 (Prerequisite steps: Phase 2). 4-row WHITESPACE VALIDATION table per candidate attribute. CANDIDATE row first.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` -- declared before any absence evidence is gathered | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row (including C0) -- fills slot 3 | **Whitespace gate failure** -- bare assertion does not satisfy |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}]` or `Gap not confirmed: Row C{N} provides [{value}]; select a different candidate` | **Whitespace gate failure** -- non-absent value stops the candidate |
| vs-INERTIA-REF | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` -- ternary token required; same format as slot 6 | **Whitespace INERTIA-REF format failure** -- prose without ternary token; "N/A" not permitted |

NOT ACCEPTABLE: Bare assertion -- **whitespace gate failure**
NOT ACCEPTABLE: Prose without ternary token in vs-INERTIA-REF -- **whitespace INERTIA-REF format failure**
ACCEPTABLE (vs-INERTIA-REF): `vs. INERTIA-REF -- challenges: [C0 mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 -- SOURCE slot, and slot 5 -- Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 3 (Prerequisite steps: Phase 3 / Phase 4 SOURCE row). Reads slot 0 (FOCUS-STATE, GATE 0, Step 0, PREFLIGHT > EXECUTION DEPENDENCY) for path selection. Apply GATE 3. SOURCE is row 1. When slot 0 = inactive: output `VACUOUS-5: focus-inactive` in the THEREFORE row position; skip REDUCTION rows.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; must be row 1 | **Proof structure failure** -- SOURCE must appear first |
| REDUCTION-1 | `NO -- {one sentence showing what is lost if focus dimension dropped}` -- skip when slot 0 = inactive | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {one sentence showing what is lost if competitive map dropped}` -- skip when slot 0 = inactive | **Proof structure failure** -- if YES, discard |
| THEREFORE | Active: `{gap sentence}` -> slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`. Inactive: `VACUOUS-5: focus-inactive` -> slot 5 | Active: THEREFORE blocked until both NO. Inactive: empty or prose slot 5 is a **collection gate failure** |

NOT ACCEPTABLE: Writing THEREFORE first -- **proof structure failure**
NOT ACCEPTABLE: Empty THEREFORE when slot 0 = inactive -- output `VACUOUS-5: focus-inactive` -- **collection gate failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 -- Anchor column value, and slot 6 -- INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 4 (Prerequisite steps: Phase 4). Write 2-5 findings. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.
**INERTIA-REF-DELTA column** (structural -- fills slot 6): `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` -- every row; "N/A" malformed.

For cross-dimensional finding row: Claim = THEREFORE; Anchor = SOURCE; adjacent block = slot 5 -- apply GATE 3. When slot 0 = inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row (Step 0, pre-DAG): `FOCUS-STATE = {active: {new_dimension}}`; Phase 2 re-reads slot 0 (declared in EXECUTION DEPENDENCY "Reads slot" column) for Focus column update; slot 4 SOURCE re-identified; slot 5 rebuilt as pipe-delimited string (activating: changes from `VACUOUS-5: focus-inactive` to proof string; Focus column added per slot 0 = active) | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows including Write row -- new slot 0 required before Phase 2 and Phase 4 re-run), GATE 3 (all rows: SOURCE first, both reductions NO, THEREFORE blocked) -- proof rerun failure if THEREFORE written without rerunning reductions |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); WHITESPACE VALIDATION re-run; vs-INERTIA-REF ternary format; slot 3 re-evaluated | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation), GATE 2 (anchor; ABSENCE-EVIDENCE for all whitespace candidates) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row (data-dependency root, None (root)); slot 6 updated; Phase 3 vs-INERTIA-REF re-classified; Phase 4 proof reviewed | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows), 5 (if baseline shifts) | GATE 4 (all rows), GATE 3 (if slot 5 rebuild required) |

---

## V-02 -- Role sequence (Phase 4 PATH row as structural branch router)

**Axis:** Role sequence -- Phase 4's proof table gains a PATH row as row 0, before SOURCE. The PATH row reads slot 0 and routes: when slot 0 = active, proceed to SOURCE; when slot 0 = inactive, write `VACUOUS-5: focus-inactive` and exit Phase 4 immediately. Previously the active/inactive branching decision was declared in the phase instruction header -- a reader executing Phase 4 had to consult the header to know which path applies. The PATH row makes the branching decision a table-level checkpoint.

**Hypothesis:** C-37 established CANDIDATE-first ordering for Phase 3: declaration-before-execution prevents selective evidence assembly. The same principle applies to Phase 4: the active/inactive branch decision (PATH) should appear before the proof scaffold (SOURCE, REDUCTION, THEREFORE). A PATH row at row 0 makes Phase 4 self-contained -- both branches are table-row checkpoints reviewable without reading the phase header. The inactive path now exits at row 0 rather than the THEREFORE row, making clear that SOURCE is not required when slot 0 = inactive.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS declared first (slots 0-6). GATE 0 follows -- writes slot 0. EXECUTION DEPENDENCY follows; GATE 0 is Step 0 (-- (pre-DAG)); GATE 4 is root (None (root)); Phase 4 PATH row listed as its own step. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row, below) | No upstream dependency; slot 5 reads slot 0 to select format; Phase 4 PATH row reads slot 0 for branch routing |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root -- no upstream dependency; slots 5 and 6 require this token |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5 |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first data row of Phase 4 proof table (after PATH row) | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; must follow PATH row |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | Requires slot 0 (path selector); active also requires slot 4 and slot 1; any other value is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate or phase named in "Filled by phase".

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows before proceeding. Listed as Step 0 (-- (pre-DAG)). Fills slot 0 -- Phase 4 PATH row reads slot 0 for branch routing.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` is set to a recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; Phase 4 PATH row reads slot 0 for routing | **Focus write failure** -- token must be written at this row; Phase 4 PATH routing undefined until slot 0 is written |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table; Phase 4 PATH row routes to SOURCE; slot 5 fills as pipe-delimited proof string; GATE 3 applies | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited when slot 0 = active |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; Phase 4 PATH row writes `VACUOUS-5: focus-inactive` and exits; empty or prose slot 5 does not satisfy | **Focus inactivation failure** -- Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell -- **collection gate failure**
NOT ACCEPTABLE (slot 5, inactive): "Focus not active." -- prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Step-level execution ordering. Step 0 (GATE 0) is a pre-DAG step. GATE 4 is the data-dependency root. Phase 4 PATH row is listed as its own step because it reads slot 0 and determines whether the remaining Phase 4 rows execute.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG step; Phase 4 PATH row reads slot 0 to route active/inactive branch | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all other phases**; data-dependency root | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context before Phase 2 | GATE 4 |
| Phase 2 (per competitor row) | 1 -- INERTIA-REF | 2 -- Anchor column value | GATE 1 and GATE 2 per row; Focus column per slot 0 (written by GATE 0, Step 0) | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF ternary-token format | Phase 2 |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table: active routes to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits; evaluated before SOURCE | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately follows PATH row; slot 4 before any REDUCTION row | Phase 4 PATH row |
| Phase 4, REDUCTION + THEREFORE rows | 4 -- SOURCE slot, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: both NO before THEREFORE; slot 5 pipe-delimited | Phase 4 SOURCE row |
| Phase 5 (per finding row) | 1 -- INERTIA-REF, 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 4 row 3 per row | Phase 4 |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column | **Citation gate failure** -- suppress row; run WebSearch |
| Citation in row, not footnote | URL inline in the table row | **Citation gate failure** -- relocate into row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` -- row reference, attribute name, and quoted value all present | **Anchor gate failure** -- name-only entries do not conform |
| Whitespace absence anchor | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** -- bare assertion does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` -- name-only -- **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff -- no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE is first data row after PATH | SOURCE immediately follows PATH row in Phase 4 table; slot 4 filled before any REDUCTION row | **Proof structure failure** -- SOURCE must follow PATH |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: Writing THEREFORE first and constructing REDUCTION rows retroactively -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root (None (root)); GATE 0 (Step 0, pre-DAG) wrote slot 0 before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` -- fills slot 1 (root) | **Inertia write failure** -- must be written here; return before Phase 1 |
| Per-finding citation required | Each finding: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- fills slot 6 | **Inertia citation failure** -- add before outputting |

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column per slot 0 (FOCUS-STATE, GATE 0, Step 0).

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural -- fills slot 2): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

---

### PHASE 3: WHITESPACE (fills slot 3 -- Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

4-row WHITESPACE VALIDATION table per candidate. CANDIDATE row first.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` -- declared before evidence | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row | **Whitespace gate failure** -- bare assertion fails |
| GAP-CONFIRMED | `Gap confirmed: ...` or `Gap not confirmed: ...; select a different candidate` | **Whitespace gate failure** |
| vs-INERTIA-REF | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` -- ternary token required | **Whitespace INERTIA-REF format failure** -- "N/A" not permitted |

NOT ACCEPTABLE: Bare assertion -- **whitespace gate failure**; prose without ternary token -- **whitespace INERTIA-REF format failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 -- SOURCE slot, and slot 5 -- Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Runs after Phase 3. Apply GATE 3. Row 0 is PATH -- evaluated first; reads slot 0 and routes. Active path continues to SOURCE; inactive path writes `VACUOUS-5: focus-inactive` to slot 5 and exits Phase 4. SOURCE must immediately follow PATH.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| PATH | Read slot 0 (FOCUS-STATE): `slot 0 = active -> proceed to SOURCE; slot 0 = inactive -> write VACUOUS-5: focus-inactive to slot 5; exit Phase 4` | **Path routing failure** -- PATH absent or not evaluated as row 0; any row written before PATH is a **proof structure failure** |
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; immediately after PATH | **Proof structure failure** -- SOURCE must follow PATH immediately |
| REDUCTION-1 | `NO -- {what is lost if focus dimension dropped}` | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if competitive map dropped}` | **Proof structure failure** -- if YES, discard |
| THEREFORE | `{gap sentence}` -> slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` | **Proof structure failure** -- THEREFORE blocked until both NO |

NOT ACCEPTABLE: SOURCE before PATH evaluation -- **proof structure failure**
NOT ACCEPTABLE: THEREFORE first -- **proof structure failure**
NOT ACCEPTABLE: Empty or prose slot 5 when PATH routes inactive -- must write `VACUOUS-5: focus-inactive` at PATH row -- **collection gate failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 -- Anchor column value, and slot 6 -- INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. Apply GATE 2 and GATE 4 row 3 per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column**: `Row C{N}, {attribute}: "{value}"` -- name-only malformed.
**INERTIA-REF-DELTA column** (fills slot 6): `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` -- every row; "N/A" malformed.

For cross-dimensional finding: Claim = THEREFORE; Anchor = SOURCE; adjacent block = slot 5 proof string -- apply GATE 3. When slot 0 = inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO.

---

### AMEND

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row; Phase 4 PATH row re-evaluated with updated slot 0; activating: PATH routes active, slot 5 rebuilt as pipe-delimited proof string, Focus column added | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows including Write row), GATE 3 (all rows: PATH first, SOURCE follows, both reductions NO, THEREFORE blocked) -- proof rerun failure if THEREFORE written without rerunning reductions |
| 2 | Add competitor | Name + WebSearch context | New row (slot 2); WHITESPACE re-run; vs-INERTIA-REF ternary format; slot 3 re-evaluated | 2, 3 | GATE 1, GATE 2 |
| 3 | Refine INERTIA-REF | More specific C0 mechanism | Slot 1 re-written; slot 6 updated; Phase 3 vs-INERTIA-REF re-classified; Phase 4 proof reviewed | 1, 6, 3, 5 (if shifts) | GATE 4, GATE 3 (if slot 5 rebuild) |

---

## V-03 -- Output format (WRITE-TOKEN REGISTRY in PREFLIGHT)

**Axis:** Output format -- PREFLIGHT gains a WRITE-TOKEN REGISTRY table immediately after OUTPUT CONTRACTS and before GATE 0. The table indexes all write-token gate events: gate name, token written, slot number, and pre-DAG or DAG classification. Previously the write-token schedule was derivable by scanning EXECUTION DEPENDENCY "Writes slot" column for named slots -- a multi-step scan. The registry makes the two write events independently discoverable from a dedicated table.

**Hypothesis:** PREFLIGHT contains three structural tables: OUTPUT CONTRACTS (slot inventory), EXECUTION DEPENDENCY (step ordering), and individual gate tables (constraint logic). A reader asking "which gates produce named token writes?" must scan EXECUTION DEPENDENCY. The WRITE-TOKEN REGISTRY makes this query O(1): two rows indexed by gate name with pre-DAG/DAG classification. Structurally analogous to OUTPUT CONTRACTS answering "what are the output slots?" -- the registry answers "what are the write-token gates?" from the same PREFLIGHT section, before any gate is read.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. OUTPUT CONTRACTS declared first (slots 0-6). WRITE-TOKEN REGISTRY follows -- indexes all write-token gate events. GATE 0 follows (registry row 1). EXECUTION DEPENDENCY follows; GATE 0 is Step 0 (-- (pre-DAG)); GATE 4 is root (None (root)). Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row -- WRITE-TOKEN REGISTRY row 1) | No upstream dependency; slot 5 reads slot 0 to select format (active: pipe-delimited; inactive: `VACUOUS-5: focus-inactive`) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row -- WRITE-TOKEN REGISTRY row 2) | Root -- no upstream dependency; slots 5 and 6 require this token |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5 |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first row of Phase 4 proof table | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; must appear first |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | Requires slot 0 (path selector); active also requires slot 4 and slot 1; any other value is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate or phase named in "Filled by phase".

---

### WRITE-TOKEN REGISTRY

All write-token gate events in this skill. A write-token event is a gate row that writes a named token to a declared output contract slot. No phase outside GATE 0 and GATE 4 performs a write-token event. An omitted registry row is a **write-token registry gap**.

| # | Gate | Token written | Slot | Pre-DAG? | Execution constraint |
|---|------|--------------|------|---------|---------------------|
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes -- executes before GATE 4 and Phase 1 | Must complete before Phase 2 reads slot 0 for Focus column inclusion; must complete before Phase 4 reads slot 0 for path selection |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) prerequisite | Must complete before Phase 1 and all phases; slot 1 required by all downstream phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows before proceeding. Listed as Step 0 (-- (pre-DAG)) and as WRITE-TOKEN REGISTRY row 1. Fills slot 0.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` is set to market-sizing or positioning-framework -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- unrecognized or ambiguous value; resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; WRITE-TOKEN REGISTRY row 1 complete | **Focus write failure** -- token must be written at this row; registry row 1 incomplete until written |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table; slot 5 fills as pipe-delimited proof string; GATE 3 applies | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited when slot 0 = active |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; slot 5 = `VACUOUS-5: focus-inactive`; empty or prose does not satisfy | **Focus inactivation failure** -- Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell -- **collection gate failure**
NOT ACCEPTABLE (slot 5, inactive): "Focus not active." -- prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Step-level execution ordering. Step 0 (GATE 0) is a pre-DAG step; write-token event per WRITE-TOKEN REGISTRY row 1. GATE 4 is the data-dependency root; write-token event per WRITE-TOKEN REGISTRY row 2.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG step; write-token event (WRITE-TOKEN REGISTRY row 1); determines slot 5 format and Phase 2 Focus column | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all other phases**; data-dependency root; write-token event (WRITE-TOKEN REGISTRY row 2) | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context before Phase 2 | GATE 4 |
| Phase 2 (per competitor row) | 1 -- INERTIA-REF | 2 -- Anchor column value | GATE 1 and GATE 2 per row; Focus column per slot 0 (WRITE-TOKEN REGISTRY row 1, GATE 0, pre-DAG) | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF ternary-token format | Phase 2 |
| Phase 4, SOURCE row | 2 -- Anchor column value (named cell) | 4 -- SOURCE slot | SOURCE row is row 1; before any REDUCTION row | Phase 3 |
| Phase 4, REDUCTION + THEREFORE rows | 0 -- FOCUS-STATE (path selector), 4 -- SOURCE slot, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: both NO before THEREFORE; slot 5 pipe-delimited. Inactive: slot 5 = `VACUOUS-5: focus-inactive`. Empty or prose is a **collection gate failure** | Phase 4 SOURCE row |
| Phase 5 (per finding row) | 1 -- INERTIA-REF, 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 4 row 3 per row | Phase 4 |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column | **Citation gate failure** -- suppress row; run WebSearch |
| Citation in row, not footnote | URL inline in the table row | **Citation gate failure** -- relocate into row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` -- row reference, attribute name, quoted value | **Anchor gate failure** -- name-only does not conform |
| Whitespace absence anchor | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` per row | **Whitespace gate failure** -- bare assertion does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff -- no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE row first | SOURCE is first in Phase 4 proof table; slot 4 before any REDUCTION row | **Proof structure failure** |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: THEREFORE first -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root (None (root)); WRITE-TOKEN REGISTRY row 2; GATE 0 (registry row 1, pre-DAG) wrote slot 0 before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1 (root); WRITE-TOKEN REGISTRY row 2 complete | **Inertia write failure** -- registry row 2 incomplete; return before Phase 1 |
| Per-finding citation required | Each finding: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- fills slot 6 | **Inertia citation failure** |

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column per slot 0 (WRITE-TOKEN REGISTRY row 1, GATE 0, pre-DAG).

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural -- fills slot 2): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

---

### PHASE 3: WHITESPACE (fills slot 3 -- Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

4-row WHITESPACE VALIDATION table per candidate. CANDIDATE row first.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` -- declared before evidence | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row | **Whitespace gate failure** |
| GAP-CONFIRMED | `Gap confirmed: ...` or `Gap not confirmed: ...; select a different candidate` | **Whitespace gate failure** |
| vs-INERTIA-REF | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- ternary token required | **Whitespace INERTIA-REF format failure** |

NOT ACCEPTABLE: Bare assertion -- **whitespace gate failure**; prose without ternary token -- **whitespace INERTIA-REF format failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 -- SOURCE slot, and slot 5 -- Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 0 (FOCUS-STATE, WRITE-TOKEN REGISTRY row 1, GATE 0, pre-DAG) for path selection. Apply GATE 3. SOURCE is row 1. When slot 0 = inactive: output `VACUOUS-5: focus-inactive` in THEREFORE row position; skip REDUCTION rows.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; must be row 1 | **Proof structure failure** -- SOURCE must appear first |
| REDUCTION-1 | `NO -- {what is lost if focus dimension dropped}` -- skip when slot 0 = inactive | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if competitive map dropped}` -- skip when slot 0 = inactive | **Proof structure failure** -- if YES, discard |
| THEREFORE | Active: `{gap sentence}` -> slot 5 pipe-delimited. Inactive: `VACUOUS-5: focus-inactive` -> slot 5 | Active: THEREFORE blocked until both NO. Inactive: empty or prose is a **collection gate failure** |

---

### PHASE 5: FINDINGS TABLE (fills slot 2 -- Anchor column value, and slot 6 -- INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. Apply GATE 2 and GATE 4 row 3 per row. Reads slot 1 (WRITE-TOKEN REGISTRY row 2) and slot 2.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column**: `Row C{N}, {attribute}: "{value}"` -- name-only malformed.
**INERTIA-REF-DELTA column** (fills slot 6): `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` -- every row; "N/A" malformed.

When slot 0 = inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO.

---

### AMEND

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row (WRITE-TOKEN REGISTRY row 1, pre-DAG); slot 4 SOURCE re-identified; slot 5 rebuilt (activating: changes from `VACUOUS-5: focus-inactive` to proof string; Focus column added) | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows including Write row -- registry row 1 re-executed; slot 0 updated before Phase 4 re-runs), GATE 3 (all rows) -- proof rerun failure if THEREFORE written without rerunning reductions |
| 2 | Add competitor | Name + WebSearch context | New row (slot 2); WHITESPACE re-run; vs-INERTIA-REF ternary; slot 3 re-evaluated | 2, 3 | GATE 1, GATE 2 |
| 3 | Refine INERTIA-REF | More specific C0 mechanism | Slot 1 re-written at GATE 4 write row (WRITE-TOKEN REGISTRY row 2, data-dependency root); slot 6 updated; Phase 3 vs-INERTIA-REF re-classified; Phase 4 proof reviewed | 1, 6, 3, 5 (if shifts) | GATE 4 (registry row 2 re-executed), GATE 3 (if slot 5 rebuild) |

---

## V-04 -- Combined A+B (Phase 2 reads slot 0 + Phase 4 PATH row)

**Axis:** Combined A+B -- V-01's Phase 2 "Reads slot" declares slot 0 explicitly, plus V-02's Phase 4 PATH row as row 0. Every step that conditionally reads slot 0 declares it in "Reads slot" (Phase 2 and Phase 4 REDUCTION+THEREFORE rows); Phase 4's branching gate is a structural table-row checkpoint (PATH row) rather than a prose condition.

**Hypothesis:** V-01 closes the EXECUTION DEPENDENCY gap for Phase 2's conditional read. V-02 closes the Phase 4 table structure gap with a PATH row. Together, slot 0's full consumption path is machine-readable from two independent structural positions: the "Reads slot" column (complete declared reads) and the Phase 4 PATH row (in-table branch checkpoint).

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6). GATE 0 follows. EXECUTION DEPENDENCY: Phase 2 declares slot 0 in "Reads slot"; Phase 4 PATH row listed as its own step; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row, below) | No upstream dependency; Phase 2 reads slot 0 for Focus column inclusion; Phase 4 PATH row reads slot 0 for branch routing; slot 5 reads slot 0 for format selection |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row, below) | Root -- no upstream dependency; slots 5 and 6 require this token |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5 |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first data row of Phase 4 proof table (after PATH row) | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; must follow PATH row immediately |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | Requires slot 0 (path and format selector); active also requires slot 4 and slot 1; any other value is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (root) |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before any numbered gate. Execute all four rows. Step 0 (-- (pre-DAG)). Fills slot 0 -- read by Phase 2 (Focus column, per EXECUTION DEPENDENCY "Reads slot") and Phase 4 PATH row (branch routing).

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; read by Phase 2 and Phase 4 PATH row | **Focus write failure** -- token must be written here; Phase 2 Focus column and Phase 4 PATH routing undefined until slot 0 is written |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table (Phase 2 "Reads slot" declares slot 0); Phase 4 PATH row routes to SOURCE; slot 5 fills as pipe-delimited proof string; GATE 3 applies | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent; Phase 4 PATH row writes `VACUOUS-5: focus-inactive` and exits; empty or prose slot 5 fails | **Focus inactivation failure** -- Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell or prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Step-level execution ordering. "Reads slot" declares all reads including conditional reads. An omitted conditional read is an **execution dependency gap**.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG step; determines Phase 2 Focus column and Phase 4 PATH branch | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all other phases**; data-dependency root | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context | GATE 4 |
| Phase 2 (per competitor row) | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 row reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row; Focus column when slot 0 = active | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF ternary-token format | Phase 2 |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table: active routes to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately after PATH row; slot 4 before any REDUCTION row | Phase 4 PATH row |
| Phase 4, REDUCTION + THEREFORE rows | 0 -- FOCUS-STATE (path selector), 4 -- SOURCE slot, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: both NO before THEREFORE; slot 5 pipe-delimited | Phase 4 SOURCE row |
| Phase 5 (per finding row) | 1 -- INERTIA-REF, 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 4 row 3 per row | Phase 4 |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column | **Citation gate failure** -- suppress row; run WebSearch |
| Citation in row, not footnote | URL inline in the table row | **Citation gate failure** -- relocate |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` | **Anchor gate failure** -- name-only does not conform |
| Whitespace absence anchor | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` per row | **Whitespace gate failure** |

NOT ACCEPTABLE: `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff -- no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE follows PATH row | SOURCE is first data row after PATH; slot 4 before any REDUCTION row | **Proof structure failure** |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE only after both REDUCTION rows answer NO | **Proof structure failure** -- retroactive construction fails |

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root (None (root)); slot 0 written pre-DAG by GATE 0.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1 (root) | **Inertia write failure** |
| Per-finding citation required | Each finding: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- fills slot 6 | **Inertia citation failure** |

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 0 and slot 1 per EXECUTION DEPENDENCY. C0 as Row C0. WebSearch per external competitor. GATE 1 and GATE 2 per row. Focus column when slot 0 = active.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural): `Row C{N}, {attribute}: "{value}"` -- name-only malformed.

---

### PHASE 3: WHITESPACE (fills slot 3 -- Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

4-row WHITESPACE VALIDATION per candidate. CANDIDATE first.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row | **Whitespace gate failure** |
| GAP-CONFIRMED | `Gap confirmed: ...` or `Gap not confirmed: ...; select a different candidate` | **Whitespace gate failure** |
| vs-INERTIA-REF | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` | **Whitespace INERTIA-REF format failure** |

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 -- SOURCE slot, and slot 5 -- Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. Row 0 is PATH -- evaluated first; reads slot 0; routes active to SOURCE or inactive to `VACUOUS-5: focus-inactive`.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| PATH | `slot 0 = active -> proceed to SOURCE; slot 0 = inactive -> VACUOUS-5: focus-inactive -> slot 5; exit Phase 4` | **Path routing failure** -- PATH absent or not evaluated as row 0 |
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; immediately after PATH | **Proof structure failure** -- SOURCE must follow PATH |
| REDUCTION-1 | `NO -- {what is lost if focus dropped}` | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if map dropped}` | **Proof structure failure** -- if YES, discard |
| THEREFORE | `{gap sentence}` -> slot 5 pipe-delimited | **Proof structure failure** -- THEREFORE blocked until both NO |

NOT ACCEPTABLE: SOURCE before PATH -- **proof structure failure**; empty/prose slot 5 when inactive -- **collection gate failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 -- Anchor column value, and slot 6 -- INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. GATE 2 and GATE 4 row 3 per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column**: `Row C{N}, {attribute}: "{value}"` -- name-only malformed.
**INERTIA-REF-DELTA column**: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- every row.
When slot 0 = inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO.

---

### AMEND

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row; Phase 2 re-reads slot 0 (declared in EXECUTION DEPENDENCY "Reads slot"); Phase 4 PATH row re-evaluated; activating: PATH routes active, Focus column added, slot 5 rebuilt as proof string | 0, 4, 5 | GATE 0 (all rows), GATE 3 (all rows) -- proof rerun failure if THEREFORE written without rerunning reductions |
| 2 | Add competitor | Name + WebSearch | New row (slot 2); WHITESPACE re-run; ternary format; slot 3 re-evaluated | 2, 3 | GATE 1, GATE 2 |
| 3 | Refine INERTIA-REF | More specific C0 mechanism | Slot 1 re-written; slot 6 updated; Phase 3 re-classified; Phase 4 reviewed | 1, 6, 3, 5 (if shifts) | GATE 4, GATE 3 (if rebuild) |

---

## V-05 -- Combined maximum (Phase 2 reads slot 0 + Phase 4 PATH row + WRITE-TOKEN REGISTRY)

**Axis:** Maximum -- all three R12 axes. V-01: Phase 2 "Reads slot" declares slot 0. V-02: Phase 4 PATH row. V-03: WRITE-TOKEN REGISTRY. Together, slot 0's complete lifecycle -- write, declaration, routing, consumption -- is visible from five independent structural positions: OUTPUT CONTRACTS slot 0 "Required by" (all consumers named); WRITE-TOKEN REGISTRY row 1 (write event indexed); EXECUTION DEPENDENCY Phase 2 "Reads slot" (conditional read declared); EXECUTION DEPENDENCY Phase 4 PATH row (branch routing step); Phase 4 table row 0 (in-table checkpoint). A reader of PREFLIGHT reconstructs the full token lifecycle without reading any phase instruction prose.

**Hypothesis:** R11 V-05 left three structural gaps: Phase 2's conditional read of slot 0 undeclared in "Reads slot"; Phase 4's inactive-path exit a prose condition rather than a table-level checkpoint; write-token schedule requiring EXECUTION DEPENDENCY scan rather than a dedicated table. V-01, V-02, and V-03 address each gap. V-05 maximum combines them: every read and write of slot 0 and slot 1 is encoded in at least two independent structural positions, making the complete token lifecycle reconstructable by table and column inspection alone.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6). WRITE-TOKEN REGISTRY follows. GATE 0 follows (registry row 1); writes slot 0; read by Phase 2 (Focus column, declared in EXECUTION DEPENDENCY "Reads slot") and Phase 4 PATH row (branch routing). EXECUTION DEPENDENCY: Phase 2 declares slot 0 as conditional read; Phase 4 PATH row listed as its own step; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row -- WRITE-TOKEN REGISTRY row 1) | No upstream dependency; Phase 2 reads slot 0 for Focus column inclusion (declared in EXECUTION DEPENDENCY "Reads slot"); Phase 4 PATH row reads slot 0 for branch routing; slot 5 reads slot 0 for format selection (active: pipe-delimited; inactive: `VACUOUS-5: focus-inactive`) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row -- WRITE-TOKEN REGISTRY row 2) | Root -- no upstream dependency; slots 5 and 6 require this token |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5 |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first data row of Phase 4 proof table (follows PATH row) | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; must follow PATH row immediately |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | Requires slot 0 (path and format selector); active also requires slot 4 and slot 1; any other value is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate or phase named in "Filled by phase".

---

### WRITE-TOKEN REGISTRY

All write-token gate events. No phase outside GATE 0 and GATE 4 performs a write-token event. An omitted registry row is a **write-token registry gap**.

| # | Gate | Token written | Slot | Pre-DAG? | Execution constraint |
|---|------|--------------|------|---------|---------------------|
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes -- executes before GATE 4 and Phase 1 | Must complete before Phase 2 reads slot 0 (Focus column, declared in EXECUTION DEPENDENCY); must complete before Phase 4 PATH row reads slot 0 (branch routing) |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) | Must complete before Phase 1 and all phases; slot 1 required by all downstream phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows. Listed as Step 0 (-- (pre-DAG)) and WRITE-TOKEN REGISTRY row 1. Fills slot 0 -- read by Phase 2 (Focus column, EXECUTION DEPENDENCY "Reads slot" column declares this), Phase 4 PATH row (branch routing), Phase 4 REDUCTION+THEREFORE rows (format selection).

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; WRITE-TOKEN REGISTRY row 1 complete; token available to Phase 2 Focus column, Phase 4 PATH row, and Phase 4 path selection | **Focus write failure** -- token must be written here; registry row 1 incomplete; Phase 2 and Phase 4 PATH routing undefined |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table (Phase 2 declares slot 0 in EXECUTION DEPENDENCY "Reads slot"); Phase 4 PATH row routes to SOURCE; slot 5 as pipe-delimited proof string; GATE 3 applies | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; Phase 4 PATH row writes `VACUOUS-5: focus-inactive` and exits; empty or prose slot 5 fails | **Focus inactivation failure** -- Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell or prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Full lifecycle from focus-gate to findings. Step 0 (GATE 0) is pre-DAG; write-token event per WRITE-TOKEN REGISTRY row 1. GATE 4 is data-dependency root; write-token event per WRITE-TOKEN REGISTRY row 2. "Reads slot" declares all reads including conditional reads. An omitted conditional read is an **execution dependency gap**.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG; WRITE-TOKEN REGISTRY row 1; determines Phase 2 Focus column and Phase 4 PATH branch | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all phases**; data-dependency root; WRITE-TOKEN REGISTRY row 2 | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context | GATE 4 |
| Phase 2 (per competitor row) | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 row reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row; Focus column when slot 0 = active; absent when slot 0 = inactive | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF ternary-token format | Phase 2 |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table: active routes to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits; evaluated before SOURCE | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately after PATH row; slot 4 before any REDUCTION row | Phase 4 PATH row |
| Phase 4, REDUCTION + THEREFORE rows | 0 -- FOCUS-STATE (path selector), 4 -- SOURCE slot, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: both NO before THEREFORE; slot 5 pipe-delimited. Inactive: slot 5 written at PATH row | Phase 4 SOURCE row |
| Phase 5 (per finding row) | 1 -- INERTIA-REF, 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 4 row 3 per row | Phase 4 |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column | **Citation gate failure** -- suppress row; run WebSearch |
| Citation in row, not footnote | URL inline in table row | **Citation gate failure** -- relocate |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` -- row reference, attribute name, quoted value | **Anchor gate failure** -- name-only does not conform |
| Whitespace absence anchor | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` per row | **Whitespace gate failure** -- bare assertion fails |

NOT ACCEPTABLE: `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` -- name-only -- **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff -- no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE follows PATH row | SOURCE is first data row after PATH; slot 4 before any REDUCTION row | **Proof structure failure** -- SOURCE must follow PATH |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE only after both REDUCTION rows answer NO | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: SOURCE before PATH -- **proof structure failure**; THEREFORE first -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root (None (root)); WRITE-TOKEN REGISTRY row 2; GATE 0 (registry row 1, pre-DAG) wrote slot 0 before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1 (root); WRITE-TOKEN REGISTRY row 2 complete | **Inertia write failure** -- registry row 2 incomplete; return before Phase 1 |
| Per-finding citation required | Each finding: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- fills slot 6 | **Inertia citation failure** |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 0 (WRITE-TOKEN REGISTRY row 1, GATE 0, pre-DAG) and slot 1 (WRITE-TOKEN REGISTRY row 2, GATE 4, root) per EXECUTION DEPENDENCY. C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column when slot 0 = active; absent when slot 0 = inactive.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural -- fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

Note which mechanism phrases and focus-column values relate to INERTIA-REF (slot 1) -- fills slot 6 at Phase 5.

---

### PHASE 3: WHITESPACE (fills slot 3 -- Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

4-row WHITESPACE VALIDATION per candidate. CANDIDATE first.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` -- declared before evidence | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row (including C0) -- fills slot 3 | **Whitespace gate failure** -- bare assertion fails |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}]` or `Gap not confirmed: Row C{N} provides [{value}]; select a different candidate` | **Whitespace gate failure** |
| vs-INERTIA-REF | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` -- ternary token required; same format as slot 6 | **Whitespace INERTIA-REF format failure** -- prose without ternary token; "N/A" not permitted |

NOT ACCEPTABLE: Bare assertion -- **whitespace gate failure**; prose without ternary token -- **whitespace INERTIA-REF format failure**
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before ABSENCE-EVIDENCE is complete for all rows -- **whitespace gate failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 -- SOURCE slot, and slot 5 -- Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. Row 0 is PATH -- evaluated first; reads slot 0 (WRITE-TOKEN REGISTRY row 1, GATE 0, pre-DAG); routes: active continues to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits. SOURCE must immediately follow PATH.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| PATH | Read slot 0 (FOCUS-STATE): `slot 0 = active -> proceed to SOURCE; slot 0 = inactive -> write VACUOUS-5: focus-inactive to slot 5; exit Phase 4` | **Path routing failure** -- PATH absent or not row 0; any row written before PATH evaluation is a **proof structure failure** |
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; immediately after PATH | **Proof structure failure** -- SOURCE must follow PATH; slot 4 before any REDUCTION |
| REDUCTION-1 | `NO -- {what is lost if focus dimension dropped}` | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if competitive map dropped}` | **Proof structure failure** -- if YES, discard |
| THEREFORE | `{gap sentence}` -> slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` | **Proof structure failure** -- THEREFORE blocked until both NO |

NOT ACCEPTABLE: SOURCE before PATH -- **proof structure failure**; THEREFORE first -- **proof structure failure**; empty/prose slot 5 when inactive -- **collection gate failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 -- Anchor column value, and slot 6 -- INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. Reads slot 1 (WRITE-TOKEN REGISTRY row 2) and slot 2. Apply GATE 2 and GATE 4 row 3 per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural -- fills slot 2): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier -- enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural -- fills slot 6): `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` -- every row; "N/A" malformed.

For cross-dimensional finding row: Claim = THEREFORE; Anchor = SOURCE; adjacent block = slot 5 proof string -- apply GATE 3. When slot 0 = inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row (WRITE-TOKEN REGISTRY row 1, pre-DAG); Phase 2 re-reads slot 0 (declared in EXECUTION DEPENDENCY "Reads slot") for Focus column update; Phase 4 PATH row re-evaluated with updated slot 0; activating: PATH routes active, Focus column added, slot 5 rebuilt as pipe-delimited proof string; deactivating: PATH routes inactive, Focus column removed, slot 5 = `VACUOUS-5: focus-inactive` | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows including Write row -- registry row 1 re-executed; slot 0 updated before Phase 2 and Phase 4 PATH re-run), GATE 3 (all rows: PATH first, SOURCE follows, both reductions NO, THEREFORE blocked) -- proof rerun failure if THEREFORE written without rerunning reductions |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); WHITESPACE VALIDATION re-run; vs-INERTIA-REF ternary; slot 3 re-evaluated | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation), GATE 2 (anchor; ABSENCE-EVIDENCE for all whitespace candidates) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row (WRITE-TOKEN REGISTRY row 2, data-dependency root, None (root)); slot 6 updated; Phase 3 vs-INERTIA-REF re-classified; Phase 4 proof reviewed -- if baseline shifts, rebuild all proof rows | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows), 5 (if baseline shifts) | GATE 4 (all rows: registry row 2 re-executed), GATE 3 (if slot 5 rebuild required) |

---

```json
{"round": 12, "baseline": "R11 V-05 (C-43 + C-44 + C-45 + all prior)", "new_axes": ["Phase 2 Reads slot declares slot 0 as conditional read -- EXECUTION DEPENDENCY Reads slot column must exhaustively declare all slot reads including conditional branches; Phase 2 reads slot 0 for Focus column inclusion but R11 V-05 listed only slot 1; adding slot 0 makes Phase 2s conditional dependency machine-readable at the column level", "Phase 4 PATH row as structural branch router -- row 0 of Phase 4 table reads slot 0 and routes: active proceeds to SOURCE; inactive writes VACUOUS-5: focus-inactive and exits; active/inactive branching is now a table-row checkpoint independent of phase instruction prose; extends declaration-before-execution principle (C-37 for Phase 3) to Phase 4", "WRITE-TOKEN REGISTRY table in PREFLIGHT -- dedicated index of write-token gate events with gate, token, slot, and pre-DAG/DAG classification; makes the two write events discoverable in O(1) without scanning EXECUTION DEPENDENCY; structurally complementary to OUTPUT CONTRACTS (slot inventory) and EXECUTION DEPENDENCY (step ordering)"], "candidate_criteria": ["C-44: EXECUTION DEPENDENCY Reads slot column must exhaustively declare all slot reads -- including conditional reads; Phase 2 must declare slot 0 (FOCUS-STATE) in its Reads slot entry when it conditionally includes a Focus column based on slot 0; a step omitting a conditional slot read has an execution dependency gap and does not satisfy", "C-45: Phase 4 proof table includes a PATH row as row 0 that declares both execution branches (active: proceed to SOURCE; inactive: write VACUOUS-5: focus-inactive and exit) as independently reviewable checkpoint rows; Phase 4 without a PATH row does not satisfy even if active/inactive branching is described in the phase instruction header or GATE 0 narrative", "C-46: PREFLIGHT includes a named WRITE-TOKEN REGISTRY (or equivalent) table listing every write-token gate event with gate name, token written, slot number, and pre-DAG or DAG classification; a skill whose write-token schedule is only derivable by scanning EXECUTION DEPENDENCY Writes slot column does not satisfy; the registry must be a first-class queryable table within PREFLIGHT"]}
```
