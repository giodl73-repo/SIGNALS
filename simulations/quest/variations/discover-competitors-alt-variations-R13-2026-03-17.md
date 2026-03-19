Written to `simulations/quest/variations/discover-competitors-alt-variations-R13-2026-03-17.md`.

---

**R13 Variations Summary**

Three single-axis innovations on V-05 R12 (C-44 + C-45 + C-46 base):

| Variation | Axis | Innovation | Candidate criterion |
|-----------|------|-----------|---------------------|
| V-01 | Output format | WRITE-TOKEN REGISTRY gains **"Consumed by" column** -- token read-side declared per registry row, symmetric with OUTPUT CONTRACTS "Required by" | C-47 |
| V-02 | Role sequence | GATE 3 gains **PATH-PRESENT check as row 0** -- PATH absence independently detectable before SOURCE-position check; gate-level complement of C-45 | C-48 |
| V-03 | Lifecycle emphasis | Phase 5 gains **COMPLETENESS row** as final row -- structural tail validation parallel to Phase 3's GAP-CONFIRMED; absent = **findings completeness failure** | C-49 |
| V-04 | A+B | V-01 + V-02 | C-47 + C-48 |
| V-05 | Maximum | All three | C-47 + C-48 + C-49 |

**Key structural property of V-05**: slot 0 lifecycle encoded across seven independent positions: OUTPUT CONTRACTS "Required by", WRITE-TOKEN REGISTRY "Consumed by", EXECUTION DEPENDENCY "Reads slot", EXECUTION DEPENDENCY PATH-row step, Phase 4 PATH table row 0, GATE 3 PATH-PRESENT row 0, Phase 5 COMPLETENESS row.
are derivable from "Execution constraint" prose or from EXECUTION DEPENDENCY "Reads slot" -- does not satisfy. The token lifecycle must be bidirectionally complete from the registry row: writer declared (Gate column) and all consumers declared ("Consumed by" column). An omitted or incomplete "Consumed by" entry for a declared consumer is a **write-token consumer gap**. C-47 is a strictly stronger form of C-46: C-47 satisfaction implies C-46; the converse is not true.

- **C-48** (V-02): GATE 3 includes a PATH-PRESENT check as its first row (row 0 in the gate table) that explicitly verifies the PATH row exists as row 0 of the Phase 4 proof table and declares both active and inactive branches. A GATE 3 that checks SOURCE position relative to PATH without a dedicated PATH-PRESENT row does not satisfy -- PATH absence must be independently detectable at GATE 3 row 0 before the SOURCE-position check at row 1. This is the gate-level complement of C-45 (which added PATH to Phase 4's execution table): C-45 adds the structural requirement in Phase 4; C-48 adds the named gate check for that requirement in GATE 3. Neither implies the other.

- **C-49** (V-03): Phase 5 FINDINGS TABLE includes a COMPLETENESS row as its final row (after all finding rows) that explicitly validates: all Anchor column values conform to GATE 2 format; all INERTIA-REF-DELTA column values conform to GATE 4 row 3 format; cross-dimensional finding row present when slot 0 = active. A findings table that ends with the last finding row without a named conclusion or validation row does not satisfy. The COMPLETENESS row is the Phase 5 analogue of Phase 3's GAP-CONFIRMED row: both close their respective phases with a named structural conclusion. An absent COMPLETENESS row is a **findings completeness failure**. C-49 is independent of C-37.

**Dependency notes:**
- C-47 requires C-46 (no registry = no "Consumed by" column); C-47 satisfaction implies C-46.
- C-48 requires C-45 (no PATH row in Phase 4 = nothing for GATE 3 to check); neither implies the other.
- C-49 is independent of C-37, C-36, C-38.

| | **V-01** | **V-02** | **V-03** | **V-04** | **V-05** |
|---|---|---|---|---|---|
| **C-44** (Phase 2 Reads slot 0) | YES | YES | YES | YES | YES |
| **C-45** (Phase 4 PATH row) | YES | YES | YES | YES | YES |
| **C-46** (WRITE-TOKEN REGISTRY) | YES | YES | YES | YES | YES |
| **"Consumed by" column in registry** | YES (new) | NO | NO | YES | YES |
| **GATE 3 PATH-PRESENT row 0** | NO | YES (new) | NO | YES | YES |
| **Phase 5 COMPLETENESS row** | NO | NO | YES (new) | NO | YES |

---

## V-01 -- Output format (WRITE-TOKEN REGISTRY "Consumed by" column)

**Axis:** Output format -- WRITE-TOKEN REGISTRY gains a "Consumed by" column listing all phases that read each written token by slot reference and role. R12 V-05 encoded token writers in the registry (GATE 0 writes slot 0; GATE 4 writes slot 1) and listed token readers in EXECUTION DEPENDENCY "Reads slot" -- two different tables. A reader asking "who reads FOCUS-STATE?" scans EXECUTION DEPENDENCY. "Consumed by" answers from the registry row itself.

**Hypothesis:** OUTPUT CONTRACTS "Required by" declares all downstream slot consumers from the contract row. WRITE-TOKEN REGISTRY currently has no equivalent: a reader reconstructing who reads a written token must leave the registry and scan EXECUTION DEPENDENCY "Reads slot". Adding "Consumed by" makes each token's complete lifecycle (write + all reads) table-queryable from a single row -- symmetric with OUTPUT CONTRACTS. The extracted rule: a registry that declares writers without declaring consumers is asymmetrically specified; bidirectional completeness is required.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6). WRITE-TOKEN REGISTRY follows -- indexes all write-token gate events; "Consumed by" column declares all phases that read each token. GATE 0 follows (registry row 1). EXECUTION DEPENDENCY follows; Phase 2 declares slot 0 as conditional read; Phase 4 PATH row listed as its own step; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row -- WRITE-TOKEN REGISTRY row 1) | No upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 1 "Consumed by": Phase 2 (Focus column), Phase 4 PATH row (branch routing), Phase 4 REDUCTION+THEREFORE rows (path selector), slot 5 (format selection) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row -- WRITE-TOKEN REGISTRY row 2) | Root -- no upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 2 "Consumed by" |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5 |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first data row of Phase 4 proof table (follows PATH row) | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; must follow PATH row immediately |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | Requires slot 0 (path and format selector); active also requires slot 4 and slot 1; any other value is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate or phase named in "Filled by phase".

---

### WRITE-TOKEN REGISTRY

All write-token gate events. No phase outside GATE 0 and GATE 4 performs a write-token event. An omitted registry row is a **write-token registry gap**. An omitted or incomplete "Consumed by" entry for a declared consumer is a **write-token consumer gap**.

| # | Gate | Token written | Slot | Pre-DAG? | Consumed by | Execution constraint |
|---|------|--------------|------|---------|-------------|---------------------|
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes -- executes before GATE 4 and Phase 1 | Phase 2 (slot 0 -- Focus column inclusion, declared in EXEC DEP "Reads slot"); Phase 4 PATH row (slot 0 -- branch decision); Phase 4 REDUCTION+THEREFORE rows (slot 0 -- path selector) | Must complete before Phase 2 reads slot 0; must complete before Phase 4 PATH row reads slot 0 |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) | Phase 2 (slot 1 -- C0 row mechanism reference); Phase 4 REDUCTION+THEREFORE rows (slot 1 -- cited in THEREFORE); Phase 5 (slot 1 -- INERTIA-REF-DELTA per finding row) | Must complete before Phase 1 and all phases; slot 1 required by all downstream phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows. Listed as Step 0 (-- (pre-DAG)) and WRITE-TOKEN REGISTRY row 1. Fills slot 0 -- all consumers declared in registry row 1 "Consumed by".

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; WRITE-TOKEN REGISTRY row 1 complete; token available to all "Consumed by" consumers | **Focus write failure** -- token must be written here; registry row 1 incomplete; Phase 2 Focus column and Phase 4 PATH routing undefined |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table (Phase 2 declares slot 0 in EXECUTION DEPENDENCY "Reads slot"); Phase 4 PATH row routes to SOURCE; slot 5 fills as pipe-delimited proof string; GATE 3 applies | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; Phase 4 PATH row writes `VACUOUS-5: focus-inactive` and exits; empty or prose slot 5 fails | **Focus inactivation failure** -- Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell or prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Full lifecycle from focus-gate to findings. Step 0 (GATE 0) is pre-DAG; write-token event per WRITE-TOKEN REGISTRY row 1 ("Consumed by" declares all slot 0 readers). GATE 4 is data-dependency root; write-token event per WRITE-TOKEN REGISTRY row 2 ("Consumed by" declares all slot 1 readers). "Reads slot" declares all reads including conditional reads. An omitted conditional read is an **execution dependency gap**.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG; WRITE-TOKEN REGISTRY row 1; "Consumed by": Phase 2, Phase 4 PATH row, Phase 4 REDUCTION+THEREFORE | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all phases**; data-dependency root; WRITE-TOKEN REGISTRY row 2; "Consumed by": Phase 2, Phase 4, Phase 5 | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context | GATE 4 |
| Phase 2 (per competitor row) | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 row reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row; Focus column when slot 0 = active; absent when slot 0 = inactive | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF ternary-token format | Phase 2 |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table: active routes to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits | Phase 3 |
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
| THEREFORE blocked | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: SOURCE before PATH -- **proof structure failure**; THEREFORE first -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root (None (root)); WRITE-TOKEN REGISTRY row 2; GATE 0 (registry row 1, pre-DAG) wrote slot 0 before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1 (root); WRITE-TOKEN REGISTRY row 2 complete; all "Consumed by" consumers will reference this token | **Inertia write failure** -- registry row 2 incomplete; return before Phase 1 |
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

Reads slot 0 (WRITE-TOKEN REGISTRY row 1, "Consumed by": Focus column inclusion) and slot 1 (WRITE-TOKEN REGISTRY row 2, "Consumed by": C0 row reference) per EXECUTION DEPENDENCY. C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column when slot 0 = active; absent when slot 0 = inactive.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural -- fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

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
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before ABSENCE-EVIDENCE complete for all rows -- **whitespace gate failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 -- SOURCE slot, and slot 5 -- Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. Row 0 is PATH -- evaluated first; reads slot 0 (WRITE-TOKEN REGISTRY row 1, "Consumed by": Phase 4 PATH row -- branch decision); routes: active continues to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits. SOURCE must immediately follow PATH.

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

Write 2-5 findings. Reads slot 1 (WRITE-TOKEN REGISTRY row 2, "Consumed by": Phase 5 -- INERTIA-REF-DELTA per finding) and slot 2. Apply GATE 2 and GATE 4 row 3 per row.

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
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row (WRITE-TOKEN REGISTRY row 1, pre-DAG); all "Consumed by" consumers re-execute: Phase 2 re-reads slot 0 for Focus column; Phase 4 PATH row re-evaluated; activating: PATH routes active, Focus column added, slot 5 rebuilt as proof string; deactivating: PATH routes inactive, Focus column removed, slot 5 = `VACUOUS-5: focus-inactive` | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows including Write row -- registry row 1 re-executed; slot 0 updated before Phase 2 and Phase 4 PATH re-run), GATE 3 (all rows) -- proof rerun failure if THEREFORE written without rerunning reductions |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); WHITESPACE VALIDATION re-run; vs-INERTIA-REF ternary; slot 3 re-evaluated | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation), GATE 2 (anchor) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row (WRITE-TOKEN REGISTRY row 2, data-dependency root); all registry row 2 "Consumed by" consumers re-execute: slot 6 updated, Phase 3 vs-INERTIA-REF re-classified, Phase 4 proof reviewed | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows), 5 (if baseline shifts) | GATE 4 (all rows -- registry row 2 re-executed), GATE 3 (if slot 5 rebuild required) |

---

## V-02 -- Role sequence (GATE 3 PATH-PRESENT check as row 0)

**Axis:** Role sequence -- GATE 3 gains a PATH-PRESENT check as its first row (row 0), before the existing SOURCE-follows-PATH check. Previously, GATE 3 implied PATH existence through the SOURCE position check: "SOURCE is first data row after PATH" presupposes PATH exists but does not independently verify it. The PATH-PRESENT row makes PATH absence a named, independently detectable failure at gate evaluation time.

**Hypothesis:** C-45 added PATH as row 0 of Phase 4's execution table -- a structural requirement. But GATE 3, which validates Phase 4's proof structure, has no dedicated check for that structural requirement. If PATH is absent, GATE 3's current row 1 ("SOURCE follows PATH") catches the failure only indirectly. An explicit PATH-PRESENT row 0 gives PATH absence its own failure state -- **path absent failure** -- independently checkable before SOURCE position is evaluated. This is the gate-level complement of C-45: C-45 adds PATH to Phase 4; C-48 adds the named gate check for PATH in GATE 3.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6). WRITE-TOKEN REGISTRY follows. GATE 0 follows (registry row 1). EXECUTION DEPENDENCY: Phase 2 declares slot 0 as conditional read; Phase 4 PATH row listed as its own step; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). GATE 3 has 4 rows -- PATH-PRESENT check at row 0 before SOURCE-position check. Gates 1-4 follow.

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
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes -- executes before GATE 4 and Phase 1 | Must complete before Phase 2 reads slot 0 (Focus column); must complete before Phase 4 PATH row reads slot 0 (branch routing) |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) | Must complete before Phase 1 and all phases; slot 1 required by all downstream phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows. Listed as Step 0 (-- (pre-DAG)) and WRITE-TOKEN REGISTRY row 1. Fills slot 0 -- read by Phase 2 (Focus column, EXECUTION DEPENDENCY "Reads slot"), Phase 4 PATH row (branch routing), Phase 4 REDUCTION+THEREFORE rows (format selection).

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; WRITE-TOKEN REGISTRY row 1 complete; token available to Phase 2 Focus column, Phase 4 PATH row, and Phase 4 path selection | **Focus write failure** -- token must be written here; registry row 1 incomplete; Phase 2 and Phase 4 PATH routing undefined |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table (Phase 2 declares slot 0 in EXECUTION DEPENDENCY "Reads slot"); Phase 4 PATH row routes to SOURCE (GATE 3 PATH-PRESENT will verify); slot 5 fills as pipe-delimited proof string; GATE 3 applies | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; Phase 4 PATH row writes `VACUOUS-5: focus-inactive` and exits (GATE 3 PATH-PRESENT will verify); empty or prose slot 5 fails | **Focus inactivation failure** -- Focus column present when slot 0 = inactive; or slot 5 empty or prose |

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
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table: active routes to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits; evaluated before SOURCE; GATE 3 PATH-PRESENT row verifies presence | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately after PATH row; slot 4 before any REDUCTION row; GATE 3 SOURCE-follows-PATH row verifies | Phase 4 PATH row |
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
| PATH row present | PATH row exists as row 0 of Phase 4 proof table; both active branch (proceed to SOURCE) and inactive branch (write `VACUOUS-5: focus-inactive` and exit) are declared | **Path absent failure** -- Phase 4 table has no PATH row at row 0; any row appearing before PATH evaluation is a **proof structure failure** |
| SOURCE follows PATH row | SOURCE is first data row after PATH; slot 4 before any REDUCTION row | **Proof structure failure** -- SOURCE must immediately follow PATH |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: Phase 4 table has no PATH row -- **path absent failure**
NOT ACCEPTABLE: SOURCE appears at Phase 4 row 0 without PATH -- **path absent failure** + **proof structure failure**
NOT ACCEPTABLE: THEREFORE first -- **proof structure failure**

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
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before ABSENCE-EVIDENCE complete for all rows -- **whitespace gate failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 -- SOURCE slot, and slot 5 -- Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3 (4-row: PATH-PRESENT, SOURCE-follows-PATH, both-NO, THEREFORE-blocked). Row 0 is PATH -- evaluated first; reads slot 0 (FOCUS-STATE, WRITE-TOKEN REGISTRY row 1, GATE 0, pre-DAG); routes: active continues to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits. SOURCE must immediately follow PATH.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| PATH | Read slot 0 (FOCUS-STATE): `slot 0 = active -> proceed to SOURCE; slot 0 = inactive -> write VACUOUS-5: focus-inactive to slot 5; exit Phase 4` | **Path routing failure** -- PATH absent or not row 0; GATE 3 PATH-PRESENT check (row 0) fails; any row written before PATH is a **proof structure failure** |
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; immediately after PATH | **Proof structure failure** -- SOURCE must follow PATH; slot 4 before any REDUCTION |
| REDUCTION-1 | `NO -- {what is lost if focus dimension dropped}` | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if competitive map dropped}` | **Proof structure failure** -- if YES, discard |
| THEREFORE | `{gap sentence}` -> slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` | **Proof structure failure** -- THEREFORE blocked until both NO |

NOT ACCEPTABLE: SOURCE before PATH -- **path absent failure** (GATE 3 row 0) + **proof structure failure**
NOT ACCEPTABLE: THEREFORE first -- **proof structure failure**; empty/prose slot 5 when inactive -- **collection gate failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 -- Anchor column value, and slot 6 -- INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. Reads slot 1 (WRITE-TOKEN REGISTRY row 2) and slot 2. Apply GATE 2 and GATE 4 row 3 per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural -- fills slot 2): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier -- enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural -- fills slot 6): `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` -- every row; "N/A" malformed.

For cross-dimensional finding row: Claim = THEREFORE; Anchor = SOURCE; adjacent block = slot 5 proof string -- apply GATE 3 (all 4 rows including PATH-PRESENT). When slot 0 = inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row (WRITE-TOKEN REGISTRY row 1, pre-DAG); Phase 2 re-reads slot 0 (declared in EXECUTION DEPENDENCY "Reads slot"); Phase 4 PATH row re-evaluated with updated slot 0; activating: PATH routes active, Focus column added, slot 5 rebuilt as proof string; deactivating: PATH routes inactive, Focus column removed, slot 5 = `VACUOUS-5: focus-inactive` | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows including Write row -- slot 0 updated before Phase 2 and Phase 4 re-run), GATE 3 (all 4 rows: PATH-PRESENT first, then SOURCE-follows-PATH, both-NO, THEREFORE-blocked) -- proof rerun failure if THEREFORE written without rerunning reductions |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); WHITESPACE VALIDATION re-run; vs-INERTIA-REF ternary; slot 3 re-evaluated | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation), GATE 2 (anchor) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row (WRITE-TOKEN REGISTRY row 2, data-dependency root, None (root)); slot 6 updated; Phase 3 vs-INERTIA-REF re-classified; Phase 4 proof reviewed | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows), 5 (if baseline shifts) | GATE 4 (all rows -- registry row 2 re-executed), GATE 3 (all 4 rows if slot 5 rebuild required) |

---

## V-03 -- Lifecycle emphasis (Phase 5 COMPLETENESS CHECK row)

**Axis:** Lifecycle emphasis -- Phase 5 gains a COMPLETENESS row as its final row, after all finding rows. Phase 3 closes with GAP-CONFIRMED: a named conclusion row that resolves the whitespace validation and classifies the result. Phase 5 has no equivalent: it ends after the last finding row with no structural conclusion. The COMPLETENESS row closes Phase 5 the same way GAP-CONFIRMED closes Phase 3.

**Hypothesis:** Phase 3's GAP-CONFIRMED forces an explicit conclusion before the next phase runs and provides an independently checkable row confirming all ABSENCE-EVIDENCE was gathered. Phase 5 has analogous per-row requirements (GATE 2 Anchor format, GATE 4 row 3 INERTIA-REF-DELTA format, cross-dim row presence when slot 0 = active) but no structural point at which these are collectively confirmed. The COMPLETENESS row is Phase 5's GAP-CONFIRMED: a named checkpoint after all finding rows that explicitly validates the full set before the skill exits. An absent COMPLETENESS row is a **findings completeness failure** -- the phase has no confirmed exit condition.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6). WRITE-TOKEN REGISTRY follows. GATE 0 follows (registry row 1). EXECUTION DEPENDENCY: Phase 2 declares slot 0 as conditional read; Phase 4 PATH row listed as its own step; Phase 5 split into finding rows + COMPLETENESS row; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row -- WRITE-TOKEN REGISTRY row 1) | No upstream dependency; Phase 2 reads slot 0 for Focus column inclusion (declared in EXECUTION DEPENDENCY "Reads slot"); Phase 4 PATH row reads slot 0 for branch routing; slot 5 reads slot 0 for format selection (active: pipe-delimited; inactive: `VACUOUS-5: focus-inactive`) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row -- WRITE-TOKEN REGISTRY row 2) | Root -- no upstream dependency; slots 5 and 6 require this token |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5; Phase 5 COMPLETENESS row validates format |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first data row of Phase 4 proof table (follows PATH row) | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; must follow PATH row immediately |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | Requires slot 0 (path and format selector); active also requires slot 4 and slot 1; any other value is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (root); Phase 5 COMPLETENESS row validates all rows |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate or phase named in "Filled by phase".

---

### WRITE-TOKEN REGISTRY

All write-token gate events. No phase outside GATE 0 and GATE 4 performs a write-token event. An omitted registry row is a **write-token registry gap**.

| # | Gate | Token written | Slot | Pre-DAG? | Execution constraint |
|---|------|--------------|------|---------|---------------------|
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes -- executes before GATE 4 and Phase 1 | Must complete before Phase 2 reads slot 0 (Focus column); must complete before Phase 4 PATH row reads slot 0 (branch routing) |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) | Must complete before Phase 1 and all phases; slot 1 required by all downstream phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows. Listed as Step 0 (-- (pre-DAG)) and WRITE-TOKEN REGISTRY row 1. Fills slot 0; Phase 5 COMPLETENESS row cross-dim? check depends on slot 0 value.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; WRITE-TOKEN REGISTRY row 1 complete; token available to Phase 2 Focus column, Phase 4 PATH row, and Phase 4 path selection | **Focus write failure** -- token must be written here; registry row 1 incomplete; Phase 2 and Phase 4 PATH routing undefined |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table (Phase 2 declares slot 0 in EXECUTION DEPENDENCY "Reads slot"); Phase 4 PATH row routes to SOURCE; slot 5 fills as pipe-delimited proof string; GATE 3 applies; Phase 5 COMPLETENESS cross-dim? = YES | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; Phase 4 PATH row writes `VACUOUS-5: focus-inactive` and exits; empty or prose slot 5 fails; Phase 5 COMPLETENESS cross-dim? = VACUOUS | **Focus inactivation failure** -- Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell or prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Full lifecycle from focus-gate to findings. Step 0 (GATE 0) is pre-DAG; write-token event per WRITE-TOKEN REGISTRY row 1. GATE 4 is data-dependency root; write-token event per WRITE-TOKEN REGISTRY row 2. "Reads slot" declares all reads including conditional reads. An omitted conditional read is an **execution dependency gap**. Phase 5 is split: finding rows followed by COMPLETENESS row -- a separate structural step.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG; WRITE-TOKEN REGISTRY row 1; determines Phase 2 Focus column and Phase 4 PATH branch; Phase 5 COMPLETENESS cross-dim? reads slot 0 | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all phases**; data-dependency root; WRITE-TOKEN REGISTRY row 2 | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context | GATE 4 |
| Phase 2 (per competitor row) | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 row reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row; Focus column when slot 0 = active; absent when slot 0 = inactive | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF ternary-token format | Phase 2 |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table: active routes to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately after PATH row; slot 4 before any REDUCTION row | Phase 4 PATH row |
| Phase 4, REDUCTION + THEREFORE rows | 0 -- FOCUS-STATE (path selector), 4 -- SOURCE slot, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: both NO before THEREFORE; slot 5 pipe-delimited. Inactive: slot 5 written at PATH row | Phase 4 SOURCE row |
| Phase 5, finding rows | 1 -- INERTIA-REF, 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 2 and GATE 4 row 3 per row | Phase 4 |
| Phase 5, COMPLETENESS row | 0 -- FOCUS-STATE (cross-dim? check), 2 -- Anchor column value (format validation), 6 -- INERTIA-REF-DELTA (format validation) | -- (validates; no slot write) | Final row of Phase 5: validates all prior finding rows for GATE 2 PASS, GATE 4 row 3 PASS, and cross-dim row present when slot 0 = active; absent COMPLETENESS = **findings completeness failure** | Phase 5 finding rows |

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
| THEREFORE blocked | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: SOURCE before PATH -- **proof structure failure**; THEREFORE first -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root (None (root)); WRITE-TOKEN REGISTRY row 2; GATE 0 (registry row 1, pre-DAG) wrote slot 0 before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1 (root); WRITE-TOKEN REGISTRY row 2 complete | **Inertia write failure** -- registry row 2 incomplete; return before Phase 1 |
| Per-finding citation required | Each finding in Phase 5 finding rows: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- fills slot 6; Phase 5 COMPLETENESS row validates all rows satisfy this | **Inertia citation failure** |

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
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before ABSENCE-EVIDENCE complete for all rows -- **whitespace gate failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 -- SOURCE slot, and slot 5 -- Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3. Row 0 is PATH -- evaluated first; reads slot 0 (FOCUS-STATE, WRITE-TOKEN REGISTRY row 1, GATE 0, pre-DAG); routes: active continues to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits. SOURCE must immediately follow PATH.

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

Write 2-5 findings followed by a COMPLETENESS row. Reads slot 1 (WRITE-TOKEN REGISTRY row 2) and slot 2. Apply GATE 2 and GATE 4 row 3 per finding row. COMPLETENESS row is required as the final row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|
| (2-5 finding rows) | ... | `Row C{N}, {attribute}: "{value}"` | `vs. INERTIA-REF -- {ternary}: {mechanism phrase}` | YES / NO |
| COMPLETENESS | `All {N} finding rows: Anchor GATE 2 PASS; INERTIA-REF-DELTA GATE 4 row 3 PASS; cross-dim row present when slot 0 = active` | `{N} rows GATE 2 PASS` | `{N} rows GATE 4 row 3 PASS` | `YES (slot 0 active) / VACUOUS (slot 0 inactive)` |

**Anchor column** (structural -- fills slot 2): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier -- enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural -- fills slot 6): `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` -- every finding row; "N/A" malformed. COMPLETENESS row validates all rows.

For cross-dimensional finding row: Claim = THEREFORE; Anchor = SOURCE; adjacent block = slot 5 proof string -- apply GATE 3. When slot 0 = inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO; COMPLETENESS cross-dim? = VACUOUS.

COMPLETENESS row is required. An absent COMPLETENESS row is a **findings completeness failure**. If any prior finding row fails GATE 2 or GATE 4 row 3, COMPLETENESS reports the row number and failure state before outputting.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row (WRITE-TOKEN REGISTRY row 1, pre-DAG); Phase 2 re-reads slot 0; Phase 4 PATH row re-evaluated; activating: Focus column added, slot 5 rebuilt as proof string, COMPLETENESS cross-dim? = YES; deactivating: Focus column removed, slot 5 = `VACUOUS-5: focus-inactive`, COMPLETENESS cross-dim? = VACUOUS | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows), GATE 3 (all rows) -- proof rerun failure if THEREFORE written without rerunning reductions; COMPLETENESS row re-executed after all finding rows re-validated |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); WHITESPACE VALIDATION re-run; vs-INERTIA-REF ternary; slot 3 re-evaluated; COMPLETENESS N incremented | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1, GATE 2; COMPLETENESS row re-run |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row (WRITE-TOKEN REGISTRY row 2, root); slot 6 updated; Phase 3 vs-INERTIA-REF re-classified; Phase 4 proof reviewed; COMPLETENESS re-validates all INERTIA-REF-DELTA values | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows), 5 (if baseline shifts) | GATE 4 (all rows), GATE 3 (if slot 5 rebuild required); COMPLETENESS row re-run |

---

## V-04 -- Combined A+B (WRITE-TOKEN REGISTRY "Consumed by" + GATE 3 PATH-PRESENT row 0)

**Axis:** Combined A+B -- V-01's "Consumed by" column makes each token's read-side machine-readable from the registry row; V-02's GATE 3 PATH-PRESENT check makes PATH row absence independently detectable at gate evaluation time before SOURCE position is checked.

**Hypothesis:** V-01 closes the WRITE-TOKEN REGISTRY read-side gap: a reader no longer needs to leave the registry to answer "who reads this token?" V-02 closes the GATE 3 structural gap: PATH absence is its own named failure state rather than an implication of SOURCE position. Combined, slot 0's consumption is bidirectionally complete in the registry and structurally enforced at the gate level.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6). WRITE-TOKEN REGISTRY follows -- "Consumed by" column declares all token readers per row. GATE 0 follows (registry row 1). EXECUTION DEPENDENCY: Phase 2 declares slot 0 as conditional read; Phase 4 PATH row listed as its own step; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). GATE 3 has 4 rows -- PATH-PRESENT at row 0. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row -- WRITE-TOKEN REGISTRY row 1) | No upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 1 "Consumed by": Phase 2 (Focus column), Phase 4 PATH row (branch routing), Phase 4 REDUCTION+THEREFORE rows (path selector), slot 5 (format selection) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row -- WRITE-TOKEN REGISTRY row 2) | Root -- no upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 2 "Consumed by" |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5 |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first data row of Phase 4 proof table (follows PATH row) | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; must follow PATH row immediately; GATE 3 PATH-PRESENT (row 0) and SOURCE-follows-PATH (row 1) verify |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | Requires slot 0 (path and format selector); active also requires slot 4 and slot 1; any other value is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate or phase named in "Filled by phase".

---

### WRITE-TOKEN REGISTRY

All write-token gate events. No phase outside GATE 0 and GATE 4 performs a write-token event. An omitted registry row is a **write-token registry gap**. An omitted or incomplete "Consumed by" entry for a declared consumer is a **write-token consumer gap**.

| # | Gate | Token written | Slot | Pre-DAG? | Consumed by | Execution constraint |
|---|------|--------------|------|---------|-------------|---------------------|
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes -- executes before GATE 4 and Phase 1 | Phase 2 (slot 0 -- Focus column inclusion, declared in EXEC DEP "Reads slot"); Phase 4 PATH row (slot 0 -- branch decision, GATE 3 PATH-PRESENT verifies presence); Phase 4 REDUCTION+THEREFORE rows (slot 0 -- path selector) | Must complete before Phase 2 reads slot 0; must complete before Phase 4 PATH row reads slot 0 |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) | Phase 2 (slot 1 -- C0 row mechanism reference); Phase 4 REDUCTION+THEREFORE rows (slot 1 -- cited in THEREFORE); Phase 5 (slot 1 -- INERTIA-REF-DELTA per finding row) | Must complete before Phase 1 and all phases; slot 1 required by all downstream phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows. Listed as Step 0 (-- (pre-DAG)) and WRITE-TOKEN REGISTRY row 1. Fills slot 0 -- all consumers declared in registry row 1 "Consumed by".

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; WRITE-TOKEN REGISTRY row 1 complete; token available to all "Consumed by" consumers | **Focus write failure** -- token must be written here; registry row 1 incomplete; Phase 2 Focus column and Phase 4 PATH routing undefined |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table (Phase 2 declares slot 0 in EXECUTION DEPENDENCY "Reads slot"); Phase 4 PATH row routes to SOURCE (GATE 3 PATH-PRESENT row 0 will verify); slot 5 fills as pipe-delimited proof string; GATE 3 applies | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; Phase 4 PATH row writes `VACUOUS-5: focus-inactive` and exits (GATE 3 PATH-PRESENT row 0 will verify); empty or prose slot 5 fails | **Focus inactivation failure** -- Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell or prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Full lifecycle from focus-gate to findings. Step 0 (GATE 0) is pre-DAG; write-token event per WRITE-TOKEN REGISTRY row 1 ("Consumed by" declares all slot 0 readers). GATE 4 is data-dependency root; write-token event per WRITE-TOKEN REGISTRY row 2 ("Consumed by" declares all slot 1 readers). "Reads slot" declares all reads including conditional reads. An omitted conditional read is an **execution dependency gap**.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG; WRITE-TOKEN REGISTRY row 1; "Consumed by": Phase 2, Phase 4 PATH row, Phase 4 REDUCTION+THEREFORE | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all phases**; data-dependency root; WRITE-TOKEN REGISTRY row 2; "Consumed by": Phase 2, Phase 4, Phase 5 | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context | GATE 4 |
| Phase 2 (per competitor row) | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 row reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row; Focus column when slot 0 = active; absent when slot 0 = inactive | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF ternary-token format | Phase 2 |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table: active routes to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits; GATE 3 PATH-PRESENT (row 0) verifies presence | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately after PATH row; GATE 3 SOURCE-follows-PATH (row 1) verifies | Phase 4 PATH row |
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
| PATH row present | PATH row exists as row 0 of Phase 4 proof table; both active branch (proceed to SOURCE) and inactive branch (write `VACUOUS-5: focus-inactive` and exit) are declared | **Path absent failure** -- Phase 4 table has no PATH row at row 0; any row appearing before PATH is a **proof structure failure** |
| SOURCE follows PATH row | SOURCE is first data row after PATH; slot 4 before any REDUCTION row | **Proof structure failure** -- SOURCE must immediately follow PATH |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: Phase 4 table has no PATH row -- **path absent failure**
NOT ACCEPTABLE: SOURCE appears at Phase 4 row 0 without PATH -- **path absent failure** + **proof structure failure**
NOT ACCEPTABLE: THEREFORE first -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root (None (root)); WRITE-TOKEN REGISTRY row 2; GATE 0 (registry row 1, pre-DAG) wrote slot 0 before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1 (root); WRITE-TOKEN REGISTRY row 2 complete; all "Consumed by" consumers will reference this token | **Inertia write failure** -- registry row 2 incomplete; return before Phase 1 |
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

Reads slot 0 (WRITE-TOKEN REGISTRY row 1, "Consumed by": Focus column inclusion) and slot 1 (WRITE-TOKEN REGISTRY row 2, "Consumed by": C0 row reference) per EXECUTION DEPENDENCY. C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column when slot 0 = active; absent when slot 0 = inactive.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural -- fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

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
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before ABSENCE-EVIDENCE complete for all rows -- **whitespace gate failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 -- SOURCE slot, and slot 5 -- Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3 (4-row: PATH-PRESENT, SOURCE-follows-PATH, both-NO, THEREFORE-blocked). Row 0 is PATH -- evaluated first; reads slot 0 (WRITE-TOKEN REGISTRY row 1, "Consumed by": Phase 4 PATH row -- branch decision); routes: active continues to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits. SOURCE must immediately follow PATH.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| PATH | Read slot 0 (FOCUS-STATE): `slot 0 = active -> proceed to SOURCE; slot 0 = inactive -> write VACUOUS-5: focus-inactive to slot 5; exit Phase 4` | **Path routing failure** -- PATH absent or not row 0; GATE 3 PATH-PRESENT check (row 0) fails; any row written before PATH is a **proof structure failure** |
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; immediately after PATH | **Proof structure failure** -- SOURCE must follow PATH; slot 4 before any REDUCTION |
| REDUCTION-1 | `NO -- {what is lost if focus dimension dropped}` | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if competitive map dropped}` | **Proof structure failure** -- if YES, discard |
| THEREFORE | `{gap sentence}` -> slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` | **Proof structure failure** -- THEREFORE blocked until both NO |

NOT ACCEPTABLE: SOURCE before PATH -- **path absent failure** (GATE 3 row 0) + **proof structure failure**
NOT ACCEPTABLE: THEREFORE first -- **proof structure failure**; empty/prose slot 5 when inactive -- **collection gate failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 -- Anchor column value, and slot 6 -- INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings. Reads slot 1 (WRITE-TOKEN REGISTRY row 2, "Consumed by": Phase 5 -- INERTIA-REF-DELTA per finding) and slot 2. Apply GATE 2 and GATE 4 row 3 per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural -- fills slot 2): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier -- enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural -- fills slot 6): `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` -- every row; "N/A" malformed.

For cross-dimensional finding row: Claim = THEREFORE; Anchor = SOURCE; adjacent block = slot 5 proof string -- apply GATE 3 (all 4 rows including PATH-PRESENT). When slot 0 = inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row (WRITE-TOKEN REGISTRY row 1, pre-DAG); all registry row 1 "Consumed by" consumers re-execute: Phase 2 re-reads slot 0 for Focus column; Phase 4 PATH row re-evaluated; activating: PATH routes active, Focus column added, slot 5 rebuilt as proof string; deactivating: PATH routes inactive, Focus column removed, slot 5 = `VACUOUS-5: focus-inactive` | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows -- registry row 1 re-executed; slot 0 updated before Phase 2 and Phase 4 re-run), GATE 3 (all 4 rows: PATH-PRESENT first, SOURCE-follows-PATH, both-NO, THEREFORE-blocked) -- proof rerun failure if THEREFORE written without rerunning reductions |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); WHITESPACE VALIDATION re-run; vs-INERTIA-REF ternary; slot 3 re-evaluated | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation), GATE 2 (anchor) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row (WRITE-TOKEN REGISTRY row 2, data-dependency root); all registry row 2 "Consumed by" consumers re-execute: slot 6 updated, Phase 3 vs-INERTIA-REF re-classified, Phase 4 proof reviewed | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows), 5 (if baseline shifts) | GATE 4 (all rows -- registry row 2 re-executed), GATE 3 (all 4 rows if slot 5 rebuild required) |

---

## V-05 -- Combined maximum ("Consumed by" + GATE 3 PATH-PRESENT + Phase 5 COMPLETENESS)

**Axis:** Maximum -- all three R13 axes. V-01: "Consumed by" column makes token read-side machine-readable from the registry row. V-02: GATE 3 PATH-PRESENT check makes PATH absence independently detectable before SOURCE position is checked. V-03: Phase 5 COMPLETENESS row closes the findings lifecycle with a named structural conclusion. Together, slot 0 and slot 1 lifecycle completeness is encoded across seven independent structural positions: OUTPUT CONTRACTS "Required by", WRITE-TOKEN REGISTRY "Consumed by", EXECUTION DEPENDENCY "Reads slot", EXECUTION DEPENDENCY PATH-row step, Phase 4 PATH table row 0, GATE 3 PATH-PRESENT row 0, and Phase 5 COMPLETENESS row.

**Hypothesis:** R12 V-05 left three structural gaps: WRITE-TOKEN REGISTRY declared token writers without declaring readers (asymmetric lifecycle); GATE 3 could not detect PATH absence independently of SOURCE position (implicit failure state); Phase 5 ended without a structural conclusion row (per-row validation obligations unconfirmed at phase level). V-01, V-02, and V-03 address each gap. V-05 maximum combines them: every token's read-write lifecycle is bidirectionally complete in the registry; PATH presence is named-checkable at GATE 3 row 0; Phase 5 closes with COMPLETENESS structurally parallel to Phase 3's GAP-CONFIRMED.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6). WRITE-TOKEN REGISTRY follows -- "Consumed by" column declares all token readers per row. GATE 0 follows (registry row 1); writes slot 0; consumers: Phase 2 (Focus column), Phase 4 PATH row, Phase 4 REDUCTION+THEREFORE rows. EXECUTION DEPENDENCY: Phase 2 declares slot 0 as conditional read; Phase 4 PATH row listed as its own step; Phase 5 split into finding rows + COMPLETENESS row; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). GATE 3 has 4 rows -- PATH-PRESENT at row 0. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row -- WRITE-TOKEN REGISTRY row 1) | No upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 1 "Consumed by": Phase 2 (Focus column), Phase 4 PATH row (branch routing), Phase 4 REDUCTION+THEREFORE rows (path selector), slot 5 (format selection) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row -- WRITE-TOKEN REGISTRY row 2) | Root -- no upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 2 "Consumed by" |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5; Phase 5 COMPLETENESS row validates format |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first data row of Phase 4 proof table (follows PATH row) | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; must follow PATH row immediately; GATE 3 PATH-PRESENT (row 0) and SOURCE-follows-PATH (row 1) verify |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | Requires slot 0 (path and format selector); active also requires slot 4 and slot 1; any other value is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (root); Phase 5 COMPLETENESS row validates all rows |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate or phase named in "Filled by phase".

---

### WRITE-TOKEN REGISTRY

All write-token gate events. No phase outside GATE 0 and GATE 4 performs a write-token event. An omitted registry row is a **write-token registry gap**. An omitted or incomplete "Consumed by" entry for a declared consumer is a **write-token consumer gap**.

| # | Gate | Token written | Slot | Pre-DAG? | Consumed by | Execution constraint |
|---|------|--------------|------|---------|-------------|---------------------|
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes -- executes before GATE 4 and Phase 1 | Phase 2 (slot 0 -- Focus column inclusion, declared in EXEC DEP "Reads slot"); Phase 4 PATH row (slot 0 -- branch decision, GATE 3 PATH-PRESENT verifies); Phase 4 REDUCTION+THEREFORE rows (slot 0 -- path selector); Phase 5 COMPLETENESS row (slot 0 -- cross-dim? check) | Must complete before Phase 2 reads slot 0 (Focus column); must complete before Phase 4 PATH row reads slot 0 (branch routing) |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) | Phase 2 (slot 1 -- C0 row mechanism reference); Phase 4 REDUCTION+THEREFORE rows (slot 1 -- cited in THEREFORE); Phase 5 finding rows (slot 1 -- INERTIA-REF-DELTA); Phase 5 COMPLETENESS row (slot 1 -- validates all INERTIA-REF-DELTA values) | Must complete before Phase 1 and all phases; slot 1 required by all downstream phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows. Listed as Step 0 (-- (pre-DAG)) and WRITE-TOKEN REGISTRY row 1. Fills slot 0 -- all consumers declared in registry row 1 "Consumed by".

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; WRITE-TOKEN REGISTRY row 1 complete; token available to all "Consumed by" consumers | **Focus write failure** -- token must be written here; registry row 1 incomplete; Phase 2 Focus column and Phase 4 PATH routing undefined |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table (Phase 2 declares slot 0 in EXECUTION DEPENDENCY "Reads slot"); Phase 4 PATH row routes to SOURCE (GATE 3 PATH-PRESENT row 0 will verify); slot 5 fills as pipe-delimited proof string; Phase 5 COMPLETENESS cross-dim? = YES | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; Phase 4 PATH row writes `VACUOUS-5: focus-inactive` and exits (GATE 3 PATH-PRESENT row 0 will verify); empty or prose slot 5 fails; Phase 5 COMPLETENESS cross-dim? = VACUOUS | **Focus inactivation failure** -- Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell or prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Full lifecycle from focus-gate to findings. Step 0 (GATE 0) is pre-DAG; write-token event per WRITE-TOKEN REGISTRY row 1 ("Consumed by" declares all slot 0 readers). GATE 4 is data-dependency root; write-token event per WRITE-TOKEN REGISTRY row 2 ("Consumed by" declares all slot 1 readers). "Reads slot" declares all reads including conditional reads. An omitted conditional read is an **execution dependency gap**. Phase 5 is split: finding rows followed by COMPLETENESS row.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG; WRITE-TOKEN REGISTRY row 1; "Consumed by": Phase 2, Phase 4 PATH row, Phase 4 REDUCTION+THEREFORE, Phase 5 COMPLETENESS | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all phases**; data-dependency root; WRITE-TOKEN REGISTRY row 2; "Consumed by": Phase 2, Phase 4, Phase 5 finding rows, Phase 5 COMPLETENESS | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context | GATE 4 |
| Phase 2 (per competitor row) | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 row reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row; Focus column when slot 0 = active; absent when slot 0 = inactive | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF ternary-token format | Phase 2 |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table: active routes to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits; GATE 3 PATH-PRESENT (row 0) verifies presence before SOURCE is evaluated | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately after PATH row; slot 4 before any REDUCTION row; GATE 3 SOURCE-follows-PATH (row 1) verifies | Phase 4 PATH row |
| Phase 4, REDUCTION + THEREFORE rows | 0 -- FOCUS-STATE (path selector), 4 -- SOURCE slot, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: both NO before THEREFORE; slot 5 pipe-delimited. Inactive: slot 5 written at PATH row | Phase 4 SOURCE row |
| Phase 5, finding rows | 1 -- INERTIA-REF, 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 2 and GATE 4 row 3 per row | Phase 4 |
| Phase 5, COMPLETENESS row | 0 -- FOCUS-STATE (cross-dim? check), 2 -- Anchor column value (format validation), 6 -- INERTIA-REF-DELTA (format validation) | -- (validates; no slot write) | Final row of Phase 5: validates all prior finding rows for GATE 2 PASS, GATE 4 row 3 PASS, and cross-dim row present when slot 0 = active; absent COMPLETENESS = **findings completeness failure** | Phase 5 finding rows |

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
| PATH row present | PATH row exists as row 0 of Phase 4 proof table; both active branch (proceed to SOURCE) and inactive branch (write `VACUOUS-5: focus-inactive` and exit) are declared | **Path absent failure** -- Phase 4 table has no PATH row at row 0; any row appearing before PATH is a **proof structure failure** |
| SOURCE follows PATH row | SOURCE is first data row after PATH; slot 4 before any REDUCTION row | **Proof structure failure** -- SOURCE must immediately follow PATH |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: Phase 4 table has no PATH row -- **path absent failure**
NOT ACCEPTABLE: SOURCE appears at Phase 4 row 0 without PATH -- **path absent failure** + **proof structure failure**
NOT ACCEPTABLE: THEREFORE first -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root (None (root)); WRITE-TOKEN REGISTRY row 2; GATE 0 (registry row 1, pre-DAG) wrote slot 0 before this gate runs.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1 (root); WRITE-TOKEN REGISTRY row 2 complete; all "Consumed by" consumers will reference this token | **Inertia write failure** -- registry row 2 incomplete; return before Phase 1 |
| Per-finding citation required | Each finding in Phase 5 finding rows: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- fills slot 6; Phase 5 COMPLETENESS row validates all rows satisfy this | **Inertia citation failure** |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 0 (WRITE-TOKEN REGISTRY row 1, "Consumed by": Focus column inclusion) and slot 1 (WRITE-TOKEN REGISTRY row 2, "Consumed by": C0 row reference) per EXECUTION DEPENDENCY. C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column when slot 0 = active; absent when slot 0 = inactive.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural -- fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

Note which mechanism phrases and focus-column values relate to INERTIA-REF (slot 1) -- fills slot 6 at Phase 5 finding rows; Phase 5 COMPLETENESS row validates all INERTIA-REF-DELTA values.

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
NOT ACCEPTABLE: Proceeding to GAP-CONFIRMED before ABSENCE-EVIDENCE complete for all rows -- **whitespace gate failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 -- SOURCE slot, and slot 5 -- Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3 (4-row: PATH-PRESENT, SOURCE-follows-PATH, both-NO, THEREFORE-blocked). Row 0 is PATH -- evaluated first; reads slot 0 (WRITE-TOKEN REGISTRY row 1, "Consumed by": Phase 4 PATH row -- branch decision); routes: active continues to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits. SOURCE must immediately follow PATH.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| PATH | Read slot 0 (FOCUS-STATE): `slot 0 = active -> proceed to SOURCE; slot 0 = inactive -> write VACUOUS-5: focus-inactive to slot 5; exit Phase 4` | **Path routing failure** -- PATH absent or not row 0; GATE 3 PATH-PRESENT check (row 0) fails; any row written before PATH is a **proof structure failure** |
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; immediately after PATH | **Proof structure failure** -- SOURCE must follow PATH; slot 4 before any REDUCTION |
| REDUCTION-1 | `NO -- {what is lost if focus dimension dropped}` | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if competitive map dropped}` | **Proof structure failure** -- if YES, discard |
| THEREFORE | `{gap sentence}` -> slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` | **Proof structure failure** -- THEREFORE blocked until both NO |

NOT ACCEPTABLE: SOURCE before PATH -- **path absent failure** (GATE 3 row 0) + **proof structure failure**
NOT ACCEPTABLE: THEREFORE first -- **proof structure failure**; empty/prose slot 5 when inactive -- **collection gate failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 -- Anchor column value, and slot 6 -- INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings followed by a COMPLETENESS row. Reads slot 1 (WRITE-TOKEN REGISTRY row 2, "Consumed by": Phase 5 finding rows and COMPLETENESS row) and slot 2. Apply GATE 2 and GATE 4 row 3 per finding row. COMPLETENESS row is required as the final row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|
| (2-5 finding rows) | ... | `Row C{N}, {attribute}: "{value}"` | `vs. INERTIA-REF -- {ternary}: {mechanism phrase}` | YES / NO |
| COMPLETENESS | `All {N} finding rows: Anchor GATE 2 PASS; INERTIA-REF-DELTA GATE 4 row 3 PASS; cross-dim row present when slot 0 = active` | `{N} rows GATE 2 PASS` | `{N} rows GATE 4 row 3 PASS` | `YES (slot 0 active) / VACUOUS (slot 0 inactive)` |

**Anchor column** (structural -- fills slot 2): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier -- enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural -- fills slot 6): `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` -- every finding row; "N/A" malformed. COMPLETENESS row validates all rows.

For cross-dimensional finding row: Claim = THEREFORE; Anchor = SOURCE; adjacent block = slot 5 proof string -- apply GATE 3 (all 4 rows including PATH-PRESENT). When slot 0 = inactive: slot 5 = `VACUOUS-5: focus-inactive`; no proof block; Cross-dim? = NO; COMPLETENESS cross-dim? = VACUOUS.

COMPLETENESS row is required. An absent COMPLETENESS row is a **findings completeness failure**. If any prior finding row fails GATE 2 or GATE 4 row 3, COMPLETENESS reports the row number and failure state before outputting.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row (WRITE-TOKEN REGISTRY row 1, pre-DAG); all registry row 1 "Consumed by" consumers re-execute: Phase 2 re-reads slot 0 for Focus column; Phase 4 PATH row re-evaluated; activating: PATH routes active, Focus column added, slot 5 rebuilt as proof string, COMPLETENESS cross-dim? = YES; deactivating: PATH routes inactive, Focus column removed, slot 5 = `VACUOUS-5: focus-inactive`, COMPLETENESS cross-dim? = VACUOUS | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows -- registry row 1 re-executed; slot 0 updated before Phase 2 and Phase 4 re-run), GATE 3 (all 4 rows: PATH-PRESENT first, SOURCE-follows-PATH, both-NO, THEREFORE-blocked) -- proof rerun failure if THEREFORE written without rerunning reductions; Phase 5 COMPLETENESS row re-run after all finding rows re-validated |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); WHITESPACE VALIDATION re-run; vs-INERTIA-REF ternary; slot 3 re-evaluated; COMPLETENESS N incremented | 2 (Anchor column value), 3 (Absence evidence block) | GATE 1 (citation), GATE 2 (anchor); COMPLETENESS row re-run |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row (WRITE-TOKEN REGISTRY row 2, data-dependency root); all registry row 2 "Consumed by" consumers re-execute: slot 6 updated, Phase 3 vs-INERTIA-REF re-classified, Phase 4 proof reviewed; Phase 5 COMPLETENESS re-validates all INERTIA-REF-DELTA values | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows), 5 (if baseline shifts) | GATE 4 (all rows -- registry row 2 re-executed), GATE 3 (all 4 rows if slot 5 rebuild required); COMPLETENESS row re-run |

---

```json
{"round": 13, "baseline": "R12 V-05 (C-44 + C-45 + C-46 + all prior)", "new_axes": ["WRITE-TOKEN REGISTRY Consumed by column -- adds read-side to the registry; a reader asking who reads FOCUS-STATE or INERTIA-REF no longer needs to scan EXECUTION DEPENDENCY Reads slot; symmetric with OUTPUT CONTRACTS Required by column; an omitted Consumed by entry for a declared consumer = write-token consumer gap", "GATE 3 PATH-PRESENT check as row 0 -- explicitly verifies PATH row exists as row 0 of Phase 4 table before SOURCE-position check; PATH absence previously detectable only indirectly through SOURCE position check; named failure state = path absent failure; gate-level complement of C-45", "Phase 5 COMPLETENESS row as final row -- structural tail validation closing Phase 5 with a named conclusion analogous to Phase 3 GAP-CONFIRMED; validates all finding rows collectively for GATE 2 Anchor format, GATE 4 row 3 INERTIA-REF-DELTA format, and cross-dim row presence when slot 0 = active; absent COMPLETENESS = findings completeness failure; Phase 5 COMPLETENESS row listed as its own step in EXECUTION DEPENDENCY"], "candidate_criteria": ["C-47: WRITE-TOKEN REGISTRY includes a dedicated Consumed by column listing all phases that read each written token by slot reference and role; a registry without Consumed by does not satisfy even if consumers are derivable from EXECUTION DEPENDENCY Reads slot; C-47 satisfaction implies C-46; omitted consumer entry = write-token consumer gap", "C-48: GATE 3 includes a PATH-PRESENT check as row 0 explicitly verifying PATH row exists as row 0 of Phase 4 proof table and declares both branches; GATE 3 that checks SOURCE position without dedicated PATH-PRESENT row does not satisfy; requires C-45; failure state = path absent failure", "C-49: Phase 5 FINDINGS TABLE includes a COMPLETENESS row as final row validating all Anchor values (GATE 2), all INERTIA-REF-DELTA values (GATE 4 row 3), and cross-dim row presence when slot 0 = active; findings table ending at last finding row without a named conclusion row does not satisfy; absent COMPLETENESS = findings completeness failure; independent of C-37"]}
```
