Written to `simulations/quest/variations/discover-competitors-alt-variations-R14-2026-03-17.md`.

---

**R14 Variations — Summary**

Three new candidate criteria, each a single-axis innovation on V-05 R13:

| Variation | Axis | Innovation | Candidate |
|-----------|------|-----------|-----------|
| V-01 | Lifecycle emphasis | **Phase 2 COMPLETENESS row** — structural tail validation after all competitor rows; confirms C0 present, >= 3 external rows, all GATE 1 + GATE 2 pass; absent = **competitor table completeness failure** | C-50 |
| V-02 | Output format | **OUTPUT CONTRACTS "Validated by" column** — names the gate/phase that enforces each slot's format; makes write + validate + consume readable from a single contract row | C-51 |
| V-03 | Format | **AMEND "Invariants" column** — names what must remain unchanged per adjustment row; formally completes the amendment boundary (delta + stable set both machine-readable) | C-52 |
| V-04 | A+B | V-01 + V-02 | C-50 + C-51 |
| V-05 | Maximum | All three | C-50 + C-51 + C-52 |

**Key structural rationale:**

- **C-50** closes the Phase 2 tail gap by analogy: Phase 3 → GAP-CONFIRMED, Phase 4 → THEREFORE, Phase 5 → COMPLETENESS (C-49). Phase 2 had no structural exit checkpoint.
- **C-51** adds validation-side symmetry to OUTPUT CONTRACTS. "Filled by phase" names who writes; "Validated by" names who checks. Together each slot's full lifecycle is a single row read.
- **C-52** implies C-38 (AMEND structured table); C-38 does not imply C-52. An AMEND without Invariants is a one-sided specification.
**C-51**: OUTPUT CONTRACTS "Validated by" adds validation-side symmetry to contract declarations. "Filled by phase" identifies the writer; "Validated by" identifies the checker. Together, each slot's full lifecycle (write + validate + consume) is machine-readable from a single contract row. C-51 is independent of C-27 ("Filled by phase") and C-34 ("Required by"): all three columns coexist; none implies another. C-51 is independent of C-47: C-47 adds "Consumed by" to WRITE-TOKEN REGISTRY; C-51 adds "Validated by" to OUTPUT CONTRACTS; both make lifecycle readable within PREFLIGHT from different tables.

- **C-52**: AMEND "Invariants" closes the stable-set gap. AMEND currently names what changes (Slots re-filled, Gates re-run) but not what must not change. An "Invariants" column closes this: every row declares its delta AND its stable set. C-52 implies C-38 (a table with Invariants necessarily has Slots re-filled and Gates re-run columns); C-38 does not imply C-52.

**Dependency notes:**
- C-50 requires Phase 2 to be a structured table (already present); independent of C-49.
- C-51 requires OUTPUT CONTRACTS within PREFLIGHT (C-32 already satisfied); additive: one new column.
- C-52 requires AMEND as structured table (C-38 already satisfied); additive: one new column.

| | **V-01** | **V-02** | **V-03** | **V-04** | **V-05** |
|---|---|---|---|---|---|
| **C-47** (WRITE-TOKEN REGISTRY "Consumed by") | YES | YES | YES | YES | YES |
| **C-48** (GATE 3 PATH-PRESENT row 0) | YES | YES | YES | YES | YES |
| **C-49** (Phase 5 COMPLETENESS row) | YES | YES | YES | YES | YES |
| **Phase 2 COMPLETENESS row** | YES (new) | NO | NO | YES | YES |
| **OUTPUT CONTRACTS "Validated by" column** | NO | YES (new) | NO | YES | YES |
| **AMEND "Invariants" column** | NO | NO | YES (new) | NO | YES |

---

## V-01 -- Lifecycle emphasis (Phase 2 COMPLETENESS row)

**Axis:** Lifecycle emphasis -- Phase 2 gains a COMPLETENESS row as its final row after all competitor rows. Phase 3 ends with GAP-CONFIRMED, Phase 4 ends with THEREFORE, Phase 5 ends with COMPLETENESS (C-49). Phase 2 ends after the last competitor row with no structural conclusion: it does not confirm C0 is present, citation and anchor requirements are met across all rows, or the competitor count is sufficient.

**Hypothesis:** Each phase that produces artifacts feeding downstream phases should close with a named structural checkpoint confirming collective readiness -- not leave that validation to downstream gates alone. Phase 2's COMPLETENESS row confirms: C0 present as row 0; at least 3 external competitors; all non-C0 rows GATE 1 citation pass; all rows GATE 2 Anchor format pass. An absent COMPLETENESS row is a **competitor table completeness failure** -- Phase 3 cannot confirm its slot 2 inputs are complete. The extracted rule: the production-side and validation-side of a phase's output should be co-located within the same table, parallel to GAP-CONFIRMED (Phase 3), THEREFORE (Phase 4), and COMPLETENESS (Phase 5).

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6). WRITE-TOKEN REGISTRY follows -- "Consumed by" column declares all token readers. GATE 0 follows (registry row 1). EXECUTION DEPENDENCY: Phase 2 split into per-row step + COMPLETENESS row step; Phase 4 PATH row listed as its own step; Phase 5 split into finding rows + COMPLETENESS row; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). GATE 3 has 4 rows -- PATH-PRESENT at row 0. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row -- WRITE-TOKEN REGISTRY row 1) | No upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 1 "Consumed by": Phase 2 per-row (Focus column), Phase 2 COMPLETENESS row (Focus-column-present check), Phase 4 PATH row (branch routing), Phase 4 REDUCTION+THEREFORE rows (path selector), slot 5 (format selection) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row -- WRITE-TOKEN REGISTRY row 2) | Root -- no upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 2 "Consumed by" |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5; Phase 2 COMPLETENESS row validates all anchor values conform to this format |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first data row of Phase 4 proof table (follows PATH row) | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; must follow PATH row immediately |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | Requires slot 0 (path and format selector); active also requires slot 4 and slot 1; any other value is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (root); Phase 5 COMPLETENESS row validates all rows |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate or phase named in "Filled by phase".

---

### WRITE-TOKEN REGISTRY

All write-token gate events. No phase outside GATE 0 and GATE 4 performs a write-token event. An omitted registry row is a **write-token registry gap**. An omitted or incomplete "Consumed by" entry for a declared consumer is a **write-token consumer gap**.

| # | Gate | Token written | Slot | Pre-DAG? | Consumed by | Execution constraint |
|---|------|--------------|------|---------|-------------|---------------------|
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes -- executes before GATE 4 and Phase 1 | Phase 2 per-row (slot 0 -- Focus column inclusion); Phase 2 COMPLETENESS row (slot 0 -- Focus-column-present check); Phase 4 PATH row (slot 0 -- branch decision); Phase 4 REDUCTION+THEREFORE rows (slot 0 -- path selector) | Must complete before Phase 2 reads slot 0; must complete before Phase 4 PATH row reads slot 0 |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) | Phase 2 per-row (slot 1 -- C0 row mechanism reference); Phase 4 REDUCTION+THEREFORE rows (slot 1 -- cited in THEREFORE); Phase 5 finding rows (slot 1 -- INERTIA-REF-DELTA per row) | Must complete before Phase 1 and all phases; slot 1 required by all downstream phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows. Listed as Step 0 (-- (pre-DAG)) and WRITE-TOKEN REGISTRY row 1. Fills slot 0 -- all consumers declared in registry row 1 "Consumed by" including Phase 2 COMPLETENESS row.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; WRITE-TOKEN REGISTRY row 1 complete; token available to all "Consumed by" consumers | **Focus write failure** -- token must be written here; registry row 1 incomplete |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table; Phase 4 PATH row routes to SOURCE; slot 5 fills as pipe-delimited proof string; GATE 3 applies; Phase 2 COMPLETENESS Focus-column-present = YES | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent from Phase 2 table; Phase 4 PATH row writes `VACUOUS-5: focus-inactive` and exits; empty or prose slot 5 fails; Phase 2 COMPLETENESS Focus-column-present = VACUOUS | **Focus inactivation failure** -- Focus column present when slot 0 = inactive; or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell or prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Full lifecycle from focus-gate to findings. Phase 2 split: per-row step + COMPLETENESS row step. Phase 5 split: finding rows + COMPLETENESS row. Step 0 (GATE 0) pre-DAG; GATE 4 data-dependency root. "Reads slot" declares all reads including conditional reads. An omitted conditional read is an **execution dependency gap**.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG; WRITE-TOKEN REGISTRY row 1; "Consumed by": Phase 2 per-row, Phase 2 COMPLETENESS, Phase 4 PATH row, Phase 4 REDUCTION+THEREFORE | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all phases**; data-dependency root; WRITE-TOKEN REGISTRY row 2; "Consumed by": Phase 2, Phase 4, Phase 5 | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context | GATE 4 |
| Phase 2, per competitor row | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 row reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row; Focus column when slot 0 = active | Phase 1 |
| Phase 2, COMPLETENESS row | 0 -- FOCUS-STATE (Focus-column-present check), 2 -- Anchor column value (format validation) | -- (validates; no slot write) | Final row of Phase 2: C0 present at row 0; external row count >= 3; all non-C0 rows GATE 1 PASS; all rows GATE 2 PASS; absent COMPLETENESS = **competitor table completeness failure** | Phase 2 per competitor rows |
| Phase 3, per whitespace candidate | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows; CANDIDATE first); vs-INERTIA-REF ternary-token format; executes after Phase 2 COMPLETENESS confirms table ready | Phase 2 COMPLETENESS row |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table: active routes to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately after PATH row; slot 4 before any REDUCTION row | Phase 4 PATH row |
| Phase 4, REDUCTION + THEREFORE rows | 0 -- FOCUS-STATE (path selector), 4 -- SOURCE slot, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: both NO before THEREFORE; slot 5 pipe-delimited; inactive: slot 5 written at PATH row | Phase 4 SOURCE row |
| Phase 5, finding rows | 1 -- INERTIA-REF, 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 2 and GATE 4 row 3 per row | Phase 4 |
| Phase 5, COMPLETENESS row | 0 -- FOCUS-STATE (cross-dim? check), 2 -- Anchor column value (format validation), 6 -- INERTIA-REF-DELTA (format validation) | -- (validates; no slot write) | Final row of Phase 5: all finding rows GATE 2 PASS, GATE 4 row 3 PASS, cross-dim row present when slot 0 = active; absent = **findings completeness failure** | Phase 5 finding rows |

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
NOT ACCEPTABLE: SOURCE at Phase 4 row 0 without PATH -- **path absent failure** + **proof structure failure**
NOT ACCEPTABLE: THEREFORE first -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root (None (root)); WRITE-TOKEN REGISTRY row 2.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1 (root); WRITE-TOKEN REGISTRY row 2 complete; all "Consumed by" consumers will reference this token | **Inertia write failure** -- registry row 2 incomplete; return before Phase 1 |
| Per-finding citation required | Each finding in Phase 5 finding rows: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- fills slot 6; Phase 5 COMPLETENESS validates all rows | **Inertia citation failure** |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 0 (WRITE-TOKEN REGISTRY row 1) and slot 1 (WRITE-TOKEN REGISTRY row 2) per EXECUTION DEPENDENCY. C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row. Focus column when slot 0 = active; absent when slot 0 = inactive. Final row is COMPLETENESS row -- required.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|
| (C0...C{N} rows) | ... | HIGH/MED/LOW | ... | ... | `Row C{N}, {attr}: "{val}"` | URL or C0-EXEMPT |
| COMPLETENESS | `C0 present: YES; external rows: {N} (>= 3); citations: all {N} non-C0 rows GATE 1 PASS; anchors: all {N+1} rows GATE 2 PASS` | -- | -- | `Focus column: {present / absent}` | `{N+1} rows GATE 2 PASS` | `{N} non-C0 rows GATE 1 PASS` |

**Anchor column** (structural -- fills slot 2, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

COMPLETENESS row is required as the final row of Phase 2. An absent COMPLETENESS row is a **competitor table completeness failure**. C0 is citation-exempt; COMPLETENESS GATE 1 check applies to non-C0 rows only. If any row fails GATE 1 or GATE 2, COMPLETENESS names the row and failure state before Phase 3 may proceed.

NOT ACCEPTABLE: Phase 2 ends at last competitor row without COMPLETENESS -- **competitor table completeness failure**

---

### PHASE 3: WHITESPACE (fills slot 3 -- Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

Executes after Phase 2 COMPLETENESS row confirms table ready. 4-row WHITESPACE VALIDATION per candidate. CANDIDATE first.

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` -- declared before evidence | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row (including C0) -- fills slot 3 | **Whitespace gate failure** -- bare assertion fails |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}]` or `Gap not confirmed: Row C{N} provides [{value}]; select a different candidate` | **Whitespace gate failure** |
| vs-INERTIA-REF | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` -- ternary token required; same format as slot 6 | **Whitespace INERTIA-REF format failure** -- prose without ternary token; "N/A" not permitted |

NOT ACCEPTABLE: Bare assertion -- **whitespace gate failure**; prose without ternary token -- **whitespace INERTIA-REF format failure**
NOT ACCEPTABLE: Proceeding before ABSENCE-EVIDENCE complete for all rows -- **whitespace gate failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 -- SOURCE slot, and slot 5 -- Focus-scope evidence, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3 (4-row: PATH-PRESENT, SOURCE-follows-PATH, both-NO, THEREFORE-blocked). Row 0 is PATH -- evaluated first; reads slot 0; routes: active continues to SOURCE; inactive writes `VACUOUS-5: focus-inactive` to slot 5 and exits. SOURCE must immediately follow PATH.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| PATH | Read slot 0 (FOCUS-STATE): `slot 0 = active -> proceed to SOURCE; slot 0 = inactive -> write VACUOUS-5: focus-inactive to slot 5; exit Phase 4` | **Path routing failure** -- PATH absent or not row 0; GATE 3 PATH-PRESENT (row 0) fails; any row written before PATH is a **proof structure failure** |
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; immediately after PATH | **Proof structure failure** -- SOURCE must follow PATH |
| REDUCTION-1 | `NO -- {what is lost if focus dimension dropped}` | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if competitive map dropped}` | **Proof structure failure** -- if YES, discard |
| THEREFORE | `{gap sentence}` -> slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` | **Proof structure failure** -- THEREFORE blocked until both NO |

NOT ACCEPTABLE: SOURCE before PATH -- **path absent failure** + **proof structure failure**; THEREFORE first -- **proof structure failure**

---

### PHASE 5: FINDINGS TABLE (fills slot 2 -- Anchor column value, and slot 6 -- INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings followed by a COMPLETENESS row. Reads slot 1 (WRITE-TOKEN REGISTRY row 2) and slot 2. Apply GATE 2 and GATE 4 row 3 per finding row. COMPLETENESS row required as final row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|
| (2-5 finding rows) | ... | `Row C{N}, {attribute}: "{value}"` | `vs. INERTIA-REF -- {ternary}: {mechanism phrase}` | YES / NO |
| COMPLETENESS | `All {N} finding rows: Anchor GATE 2 PASS; INERTIA-REF-DELTA GATE 4 row 3 PASS; cross-dim row present when slot 0 = active` | `{N} rows GATE 2 PASS` | `{N} rows GATE 4 row 3 PASS` | `YES (slot 0 active) / VACUOUS (slot 0 inactive)` |

**Anchor column** (structural -- fills slot 2): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier -- enterprise contract required for API access"`

**INERTIA-REF-DELTA column** (structural -- fills slot 6): `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` -- every finding row; "N/A" malformed. COMPLETENESS validates all rows.

An absent COMPLETENESS row is a **findings completeness failure**.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row; all "Consumed by" consumers re-execute: Phase 2 per-row re-reads slot 0; Phase 2 COMPLETENESS Focus-column-present re-evaluated; Phase 4 PATH re-evaluated; activating: Focus column added, slot 5 rebuilt, Phase 5 COMPLETENESS cross-dim? = YES; deactivating: Focus column removed, slot 5 = `VACUOUS-5: focus-inactive`, Phase 5 COMPLETENESS cross-dim? = VACUOUS | 0, 4, 5 | GATE 0 (all rows), GATE 3 (all 4 rows); Phase 2 COMPLETENESS re-run; Phase 5 COMPLETENESS re-run |
| 2 | Add competitor | Competitor name + WebSearch context | New row (slot 2); Phase 2 COMPLETENESS external row count incremented; WHITESPACE VALIDATION re-run; vs-INERTIA-REF ternary; slot 3 re-evaluated | 2, 3 | GATE 1, GATE 2; Phase 2 COMPLETENESS re-run |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row; all registry row 2 "Consumed by" consumers re-execute: slot 6 updated; Phase 3 vs-INERTIA-REF re-classified; Phase 4 proof reviewed; Phase 5 COMPLETENESS re-validates all INERTIA-REF-DELTA values | 1, 6, 3, 5 (if baseline shifts) | GATE 4 (all rows), GATE 3 (if slot 5 rebuild required); Phase 5 COMPLETENESS re-run |

---

## V-02 -- Output format (OUTPUT CONTRACTS "Validated by" column)

**Axis:** Output format -- OUTPUT CONTRACTS gains a "Validated by" column naming the gate or phase that validates each slot's format after it is produced. "Filled by phase" identifies who writes; there is no contract-level declaration of who checks. A reader verifying slot 6's format is enforced must read GATE 4 row 3; "Validated by" answers from the contract row itself.

**Hypothesis:** A slot contract that names its producer and consumers but not its validator is incompletely specified. The validation obligation is a first-class lifecycle event -- as significant as writing or consuming. Adding "Validated by" makes each slot's full lifecycle (write, validate, consume) readable from a single contract row, eliminating navigation to individual gate descriptions to understand format enforcement. The extracted rule: "Filled by phase" and "Validated by" are symmetric obligations; declaring one without the other yields a partial contract.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6) -- "Validated by" column names the gate or phase that enforces each slot's format. WRITE-TOKEN REGISTRY follows -- "Consumed by" column declares all token readers. GATE 0 follows (registry row 1). EXECUTION DEPENDENCY: Phase 2 declares slot 0 as conditional read; Phase 4 PATH row listed as its own step; Phase 5 split into finding rows + COMPLETENESS row; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). GATE 3 has 4 rows -- PATH-PRESENT at row 0. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Validated by | Required by |
|------|-------|-----------------|-----------------|--------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row -- WRITE-TOKEN REGISTRY row 1) | GATE 0 Write row (format enforced at write time; re-validated at GATE 0 re-run on focus shift) | No upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 1 "Consumed by": Phase 2 (Focus column), Phase 4 PATH row (branch routing), Phase 4 REDUCTION+THEREFORE rows (path selector), slot 5 (format selection) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row -- WRITE-TOKEN REGISTRY row 2) | GATE 4 row 1 (mechanism specificity check) + GATE 4 row 2 (write enforces format); re-validated at GATE 4 re-run on slot 1 refinement | Root -- no upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 2 "Consumed by" |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | GATE 2 row 1 (per-row anchor format check; applied per competitor row in Phase 2 and per finding row in Phase 5) | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5 |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Phase 3 ABSENCE-EVIDENCE row (format checked per row) + GATE 2 row 2 (absence anchor format) | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first data row of Phase 4 proof table (follows PATH row) | Phase 4 -- Cross-Dimensional Finding | GATE 3 row 2 (SOURCE-follows-PATH validates SOURCE position and format) | Required by slot 5; must follow PATH row immediately |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | GATE 3 rows 3-4 (reductions + THEREFORE) when slot 0 = active; Phase 4 PATH row validates `VACUOUS-5` format when slot 0 = inactive; any other value is a **collection gate failure** | Requires slot 0 (path and format selector); active also requires slot 4 and slot 1 |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | GATE 4 row 3 (per-finding format check per row); Phase 5 COMPLETENESS row (aggregate -- all rows) | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate named in "Validated by".

---

### WRITE-TOKEN REGISTRY

All write-token gate events. No phase outside GATE 0 and GATE 4 performs a write-token event. An omitted registry row is a **write-token registry gap**. An omitted or incomplete "Consumed by" entry is a **write-token consumer gap**.

| # | Gate | Token written | Slot | Pre-DAG? | Consumed by | Execution constraint |
|---|------|--------------|------|---------|-------------|---------------------|
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes -- executes before GATE 4 and Phase 1 | Phase 2 (slot 0 -- Focus column inclusion, declared in EXEC DEP "Reads slot"); Phase 4 PATH row (slot 0 -- branch decision); Phase 4 REDUCTION+THEREFORE rows (slot 0 -- path selector) | Must complete before Phase 2 reads slot 0; must complete before Phase 4 PATH row reads slot 0 |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) | Phase 2 (slot 1 -- C0 row mechanism reference); Phase 4 REDUCTION+THEREFORE rows (slot 1 -- cited in THEREFORE); Phase 5 finding rows (slot 1 -- INERTIA-REF-DELTA per row) | Must complete before Phase 1 and all phases; slot 1 required by all downstream phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows. Listed as Step 0 (-- (pre-DAG)) and WRITE-TOKEN REGISTRY row 1. Fills slot 0; validates slot 0 format per OUTPUT CONTRACTS "Validated by"; all consumers declared in registry row 1 "Consumed by".

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; validates slot 0 format per OUTPUT CONTRACTS "Validated by"; WRITE-TOKEN REGISTRY row 1 complete | **Focus write failure** -- slot 0 format unvalidated; registry row 1 incomplete |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table; Phase 4 PATH row routes to SOURCE (GATE 3 PATH-PRESENT row 0 will verify); slot 5 fills as pipe-delimited proof string; GATE 3 validates slot 5 per "Validated by" | **Focus activation failure** -- Focus column omitted or slot 5 not pipe-delimited |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent; Phase 4 PATH row writes `VACUOUS-5: focus-inactive` to slot 5 and exits; PATH row validates `VACUOUS-5` format per OUTPUT CONTRACTS slot 5 "Validated by" | **Focus inactivation failure** -- Focus column present or slot 5 empty or prose |

NOT ACCEPTABLE (slot 5, inactive): empty cell or prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Full lifecycle from focus-gate to findings. Step 0 (GATE 0) pre-DAG; validates slot 0 per OUTPUT CONTRACTS "Validated by". GATE 4 data-dependency root; validates slot 1. "Reads slot" declares all reads including conditional reads. Phase 5 split: finding rows + COMPLETENESS row. An omitted conditional read is an **execution dependency gap**.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG; WRITE-TOKEN REGISTRY row 1; validates slot 0 per OUTPUT CONTRACTS "Validated by"; "Consumed by": Phase 2, Phase 4 PATH row, Phase 4 REDUCTION+THEREFORE | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all phases**; data-dependency root; validates slot 1 per OUTPUT CONTRACTS "Validated by"; WRITE-TOKEN REGISTRY row 2 | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context | GATE 4 |
| Phase 2 (per competitor row) | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 row reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row; GATE 2 validates slot 2 per OUTPUT CONTRACTS "Validated by" | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows); slot 3 validated by Phase 3 ABSENCE-EVIDENCE + GATE 2 row 2 per OUTPUT CONTRACTS "Validated by" | Phase 2 |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table; inactive: validates slot 5 `VACUOUS-5` format per OUTPUT CONTRACTS "Validated by" | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately after PATH row; slot 4 validated by GATE 3 row 2 per OUTPUT CONTRACTS "Validated by" | Phase 4 PATH row |
| Phase 4, REDUCTION + THEREFORE rows | 0 -- FOCUS-STATE (path selector), 4 -- SOURCE slot, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: slot 5 validated by GATE 3 rows 3-4 per OUTPUT CONTRACTS "Validated by" | Phase 4 SOURCE row |
| Phase 5, finding rows | 1 -- INERTIA-REF, 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 4 row 3 validates slot 6 per row per OUTPUT CONTRACTS "Validated by" | Phase 4 |
| Phase 5, COMPLETENESS row | 0 -- FOCUS-STATE (cross-dim? check), 2, 6 | -- (validates; no slot write) | Aggregate slot 2 and slot 6 validation per OUTPUT CONTRACTS "Validated by"; absent = **findings completeness failure** | Phase 5 finding rows |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column | **Citation gate failure** -- suppress row; run WebSearch |
| Citation in row, not footnote | URL inline in table row | **Citation gate failure** -- relocate |

---

### GATE 2: ANCHOR GATE

Validates slot 2 (competitor Anchor column) and slot 3 (whitespace absence anchor) per OUTPUT CONTRACTS "Validated by".

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` -- row reference, attribute name, quoted value; validates slot 2 per OUTPUT CONTRACTS "Validated by" | **Anchor gate failure** -- name-only does not conform |
| Whitespace absence anchor | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` per row; validates slot 3 per OUTPUT CONTRACTS "Validated by" | **Whitespace gate failure** -- bare assertion fails |

NOT ACCEPTABLE: `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff -- no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

Validates slots 4 and 5 per OUTPUT CONTRACTS "Validated by".

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| PATH row present | PATH row exists as row 0 of Phase 4 proof table; both active and inactive branches declared | **Path absent failure** -- any row before PATH is a **proof structure failure** |
| SOURCE follows PATH row | SOURCE is first data row after PATH; slot 4 before any REDUCTION; validates slot 4 format per OUTPUT CONTRACTS "Validated by" | **Proof structure failure** -- SOURCE must immediately follow PATH |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE written only after both NO; slot 5 pipe-delimited string validated per OUTPUT CONTRACTS "Validated by" | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: Phase 4 table has no PATH row -- **path absent failure**
NOT ACCEPTABLE: THEREFORE first -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Validates slots 1 and 6 per OUTPUT CONTRACTS "Validated by". Execute all three rows before Phase 1. Data-dependency root (None (root)); WRITE-TOKEN REGISTRY row 2.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1; validates slot 1 format per OUTPUT CONTRACTS "Validated by"; WRITE-TOKEN REGISTRY row 2 complete | **Inertia write failure** -- slot 1 format unvalidated; registry row 2 incomplete |
| Per-finding citation required | Each finding: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- fills slot 6; validates slot 6 per row per OUTPUT CONTRACTS "Validated by"; Phase 5 COMPLETENESS validates aggregate | **Inertia citation failure** |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 0 (WRITE-TOKEN REGISTRY row 1) and slot 1 (WRITE-TOKEN REGISTRY row 2) per EXECUTION DEPENDENCY. C0 enters as Row C0. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row -- GATE 2 validates slot 2 per OUTPUT CONTRACTS "Validated by". Focus column when slot 0 = active; absent when slot 0 = inactive.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural -- fills slot 2, PREFLIGHT > OUTPUT CONTRACTS; validated by GATE 2 per OUTPUT CONTRACTS "Validated by"): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

---

### PHASE 3: WHITESPACE (fills slot 3 -- Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)

4-row WHITESPACE VALIDATION per candidate. CANDIDATE first. Slot 3 validated by Phase 3 ABSENCE-EVIDENCE and GATE 2 row 2 per OUTPUT CONTRACTS "Validated by".

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` -- declared before evidence | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row (including C0) -- fills slot 3; validated here per OUTPUT CONTRACTS "Validated by" | **Whitespace gate failure** -- bare assertion fails |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}]` or `Gap not confirmed: Row C{N} provides [{value}]; select a different candidate` | **Whitespace gate failure** |
| vs-INERTIA-REF | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` -- ternary token required | **Whitespace INERTIA-REF format failure** |

NOT ACCEPTABLE: Bare assertion -- **whitespace gate failure**; prose without ternary token -- **whitespace INERTIA-REF format failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 and slot 5, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3 (validates slots 4 and 5 per OUTPUT CONTRACTS "Validated by"; 4-row: PATH-PRESENT, SOURCE-follows-PATH, both-NO, THEREFORE-blocked). Row 0 is PATH; reads slot 0; routes active/inactive.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| PATH | Read slot 0: `active -> proceed to SOURCE; inactive -> write VACUOUS-5: focus-inactive to slot 5; exit` -- inactive PATH validates slot 5 per OUTPUT CONTRACTS "Validated by" | **Path routing failure** -- PATH absent or not row 0 |
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; validated by GATE 3 row 2 per OUTPUT CONTRACTS "Validated by" | **Proof structure failure** |
| REDUCTION-1 | `NO -- {what is lost if focus dimension dropped}` | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if competitive map dropped}` | **Proof structure failure** -- if YES, discard |
| THEREFORE | slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`; validated by GATE 3 row 4 per OUTPUT CONTRACTS "Validated by" | **Proof structure failure** -- THEREFORE blocked until both NO |

---

### PHASE 5: FINDINGS TABLE (fills slot 2 and slot 6, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings followed by COMPLETENESS row. GATE 4 row 3 validates slot 6 per row; Phase 5 COMPLETENESS validates aggregate -- both per OUTPUT CONTRACTS slot 6 "Validated by".

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|
| (2-5 finding rows) | ... | `Row C{N}, {attribute}: "{value}"` | `vs. INERTIA-REF -- {ternary}: {mechanism phrase}` | YES / NO |
| COMPLETENESS | `All {N} rows: Anchor GATE 2 PASS; INERTIA-REF-DELTA GATE 4 row 3 PASS; cross-dim present when slot 0 active` | `{N} rows GATE 2 PASS` | `{N} rows GATE 4 row 3 PASS` | `YES / VACUOUS` |

**Anchor column** validated by GATE 2 per OUTPUT CONTRACTS "Validated by": `Row C{N}, {attribute}: "{value}"`.
**INERTIA-REF-DELTA column** validated by GATE 4 row 3 per row, aggregate by COMPLETENESS per OUTPUT CONTRACTS "Validated by".

NOT ACCEPTABLE (Anchor): name-only -- **anchor gate failure**; "N/A" in INERTIA-REF-DELTA -- malformed.
An absent COMPLETENESS row is a **findings completeness failure**.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written and re-validated at GATE 0 per OUTPUT CONTRACTS "Validated by"; all "Consumed by" consumers re-execute; activating: slot 5 rebuilt as proof string, re-validated by GATE 3 per "Validated by"; deactivating: slot 5 = `VACUOUS-5`, re-validated by PATH row per "Validated by" | 0, 4, 5 | GATE 0 (slot 0 re-validated), GATE 3 (slots 4+5 re-validated per "Validated by"); proof rerun failure if THEREFORE written without rerunning reductions |
| 2 | Add competitor | Competitor name + WebSearch context | New row slot 2 re-validated by GATE 2 per "Validated by"; slot 3 re-validated by Phase 3 ABSENCE-EVIDENCE + GATE 2 row 2 per "Validated by" | 2, 3 | GATE 1, GATE 2 (slot 2 re-validated per "Validated by") |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written and re-validated at GATE 4 per "Validated by"; all registry row 2 "Consumed by" consumers re-execute; slot 6 re-validated by GATE 4 row 3 and Phase 5 COMPLETENESS per "Validated by" | 1, 6, 3, 5 (if baseline shifts) | GATE 4 (slot 1 re-validated per "Validated by"), GATE 3 (if slot 5 rebuild required) |

---

## V-03 -- Format (AMEND "Invariants" column)

**Axis:** Format -- AMEND gains an "Invariants" column listing what must remain unchanged after each adjustment. AMEND currently names what changes (Slots re-filled, Gates re-run) but not what must not change. Without an Invariants column, stable artifacts are implicitly assumed unchanged; the assumption is not checkable by column inspection. An amendment that silently corrupts a stable slot -- e.g., a focus shift that inadvertently rewrites INERTIA-REF -- is undetectable from the AMEND table alone.

**Hypothesis:** An amendment specification is formally complete when it names both its delta (what changes) and its stable set (what must not change). The Invariants column makes each adjustment's stability obligations machine-readable from the AMEND table, eliminating implicit assumptions about which slots and tokens are protected across each amendment type. The extracted rule: AMEND without Invariants is a one-sided specification; both sides -- change and stability -- must be co-declared as table columns for the amendment boundary to be fully checkable.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6). WRITE-TOKEN REGISTRY follows -- "Consumed by" column declares all token readers. GATE 0 follows (registry row 1). EXECUTION DEPENDENCY: Phase 2 declares slot 0 as conditional read; Phase 4 PATH row listed as its own step; Phase 5 split into finding rows + COMPLETENESS row; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). GATE 3 has 4 rows -- PATH-PRESENT at row 0. Gates 1-4 follow. AMEND has "Invariants" column.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Required by |
|------|-------|-----------------|-----------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row -- WRITE-TOKEN REGISTRY row 1) | No upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 1 "Consumed by": Phase 2 (Focus column), Phase 4 PATH row (branch routing), Phase 4 REDUCTION+THEREFORE rows (path selector), slot 5 (format selection) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row -- WRITE-TOKEN REGISTRY row 2) | Root -- no upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 2 "Consumed by" |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5 |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` -- first data row of Phase 4 proof table (follows PATH row) | Phase 4 -- Cross-Dimensional Finding | Required by slot 5; must follow PATH row immediately |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | Requires slot 0; active requires slots 4 and 1; any other value is a **collection gate failure** |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | Derived from slot 1 (root); Phase 5 COMPLETENESS row validates all rows |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate or phase named in "Filled by phase".

---

### WRITE-TOKEN REGISTRY

All write-token gate events. No phase outside GATE 0 and GATE 4 performs a write-token event. An omitted registry row is a **write-token registry gap**. An omitted or incomplete "Consumed by" entry is a **write-token consumer gap**.

| # | Gate | Token written | Slot | Pre-DAG? | Consumed by | Execution constraint |
|---|------|--------------|------|---------|-------------|---------------------|
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes -- executes before GATE 4 and Phase 1 | Phase 2 (slot 0 -- Focus column inclusion); Phase 4 PATH row (slot 0 -- branch decision); Phase 4 REDUCTION+THEREFORE rows (slot 0 -- path selector) | Must complete before Phase 2 reads slot 0; must complete before Phase 4 PATH row reads slot 0 |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) | Phase 2 (slot 1 -- C0 row mechanism reference); Phase 4 REDUCTION+THEREFORE rows (slot 1 -- cited in THEREFORE); Phase 5 finding rows (slot 1 -- INERTIA-REF-DELTA per row) | Must complete before Phase 1 and all phases; slot 1 required by all downstream phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows. Listed as Step 0 (-- (pre-DAG)) and WRITE-TOKEN REGISTRY row 1. Fills slot 0; all consumers declared in registry row 1 "Consumed by".

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; WRITE-TOKEN REGISTRY row 1 complete | **Focus write failure** -- token must be written here |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table; Phase 4 PATH row routes to SOURCE; slot 5 fills as pipe-delimited proof string; GATE 3 applies | **Focus activation failure** |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent; Phase 4 PATH row writes `VACUOUS-5: focus-inactive` and exits; empty or prose slot 5 fails | **Focus inactivation failure** |

NOT ACCEPTABLE (slot 5, inactive): empty cell or prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Full lifecycle from focus-gate to findings. Step 0 (GATE 0) pre-DAG. GATE 4 data-dependency root. Phase 5 split: finding rows + COMPLETENESS row. "Reads slot" declares all reads including conditional reads. An omitted conditional read is an **execution dependency gap**.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG; WRITE-TOKEN REGISTRY row 1; "Consumed by": Phase 2, Phase 4 PATH row, Phase 4 REDUCTION+THEREFORE | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all phases**; data-dependency root; WRITE-TOKEN REGISTRY row 2 | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context | GATE 4 |
| Phase 2 (per competitor row) | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 row reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row | Phase 1 |
| Phase 3 (per whitespace candidate) | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION table (4 rows); vs-INERTIA-REF ternary-token format | Phase 2 |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table: active routes to SOURCE; inactive writes `VACUOUS-5` and exits | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately after PATH row | Phase 4 PATH row |
| Phase 4, REDUCTION + THEREFORE rows | 0 -- FOCUS-STATE (path selector), 4 -- SOURCE slot, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: both NO before THEREFORE; slot 5 pipe-delimited | Phase 4 SOURCE row |
| Phase 5, finding rows | 1 -- INERTIA-REF, 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 2 and GATE 4 row 3 per row | Phase 4 |
| Phase 5, COMPLETENESS row | 0 -- FOCUS-STATE (cross-dim? check), 2, 6 | -- (validates; no slot write) | Final row: all finding rows GATE 2 PASS, GATE 4 row 3 PASS, cross-dim present when slot 0 active; absent = **findings completeness failure** | Phase 5 finding rows |

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
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff -- no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| PATH row present | PATH row exists as row 0 of Phase 4 proof table; both active and inactive branches declared | **Path absent failure** -- any row before PATH is a **proof structure failure** |
| SOURCE follows PATH row | SOURCE is first data row after PATH; slot 4 before any REDUCTION | **Proof structure failure** -- SOURCE must immediately follow PATH |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE written only after both REDUCTION rows answer NO | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: Phase 4 table has no PATH row -- **path absent failure**
NOT ACCEPTABLE: THEREFORE first -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Identify C0. Execute all three rows before Phase 1. Data-dependency root (None (root)); WRITE-TOKEN REGISTRY row 2.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1 (root); WRITE-TOKEN REGISTRY row 2 complete | **Inertia write failure** -- registry row 2 incomplete; return before Phase 1 |
| Per-finding citation required | Each finding: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- fills slot 6; Phase 5 COMPLETENESS validates all rows | **Inertia citation failure** |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 0 and slot 1 per EXECUTION DEPENDENCY. C0 as Row C0. WebSearch per external competitor before adding row. Apply GATE 1 and GATE 2 per row. Focus column when slot 0 = active; absent when slot 0 = inactive.

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
| vs-INERTIA-REF | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` -- ternary token required | **Whitespace INERTIA-REF format failure** |

NOT ACCEPTABLE: Bare assertion -- **whitespace gate failure**; prose without ternary token -- **whitespace INERTIA-REF format failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slot 4 and slot 5, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3 (4-row: PATH-PRESENT, SOURCE-follows-PATH, both-NO, THEREFORE-blocked). Row 0 is PATH; reads slot 0; routes active/inactive.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| PATH | Read slot 0: `active -> proceed to SOURCE; inactive -> write VACUOUS-5: focus-inactive to slot 5; exit` | **Path routing failure** -- PATH absent or not row 0; GATE 3 row 0 fails |
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; immediately after PATH | **Proof structure failure** |
| REDUCTION-1 | `NO -- {what is lost if focus dimension dropped}` | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if competitive map dropped}` | **Proof structure failure** -- if YES, discard |
| THEREFORE | slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` | **Proof structure failure** -- THEREFORE blocked until both NO |

---

### PHASE 5: FINDINGS TABLE (fills slot 2 and slot 6, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings followed by COMPLETENESS row. Apply GATE 2 and GATE 4 row 3 per finding row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|
| (2-5 finding rows) | ... | `Row C{N}, {attribute}: "{value}"` | `vs. INERTIA-REF -- {ternary}: {mechanism phrase}` | YES / NO |
| COMPLETENESS | `All {N} rows: Anchor GATE 2 PASS; INERTIA-REF-DELTA GATE 4 row 3 PASS; cross-dim present when slot 0 active` | `{N} rows GATE 2 PASS` | `{N} rows GATE 4 row 3 PASS` | `YES / VACUOUS` |

**Anchor column** (structural -- fills slot 2): `Row C{N}, {attribute}: "{value}"` -- name-only malformed.
**INERTIA-REF-DELTA column** (structural -- fills slot 6): ternary format required every row; "N/A" malformed.
COMPLETENESS row required. Absent = **findings completeness failure**.

---

### AMEND

Execute exactly 3 adjustment rows. "Invariants" column names slots and tokens that must remain unchanged after each adjustment -- violations are **amendment invariant failures**.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run | Invariants |
|---|-----------|-------------------|------------------------|-----------------|--------------|------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written at GATE 0 Write row; all "Consumed by" consumers re-execute: Phase 2 re-reads slot 0; Phase 4 PATH re-evaluated; activating: Focus column added, slot 5 rebuilt as proof string; deactivating: Focus column removed, slot 5 = `VACUOUS-5: focus-inactive` | 0 (FOCUS-STATE), 4 (SOURCE), 5 (Focus-scope evidence) | GATE 0 (all rows), GATE 3 (all 4 rows); proof rerun failure if THEREFORE written without rerunning reductions | INERTIA-REF stable (slot 1 unchanged; GATE 4 write row not re-run); existing competitor Anchor values stable (slot 2 values for rows C0...C{N} unchanged; GATE 1 and GATE 2 results unchanged); slot 3 stable (Phase 3 WHITESPACE not re-run; slot 2 inputs unchanged) |
| 2 | Add competitor | Competitor name + WebSearch context | New row appended (slot 2 extended); WHITESPACE VALIDATION re-run with new row; vs-INERTIA-REF ternary; slot 3 re-evaluated | 2 (Anchor column value for new row), 3 (Absence evidence block) | GATE 1 (new row), GATE 2 (new row) | FOCUS-STATE stable (slot 0 unchanged; GATE 0 not re-run); INERTIA-REF stable (slot 1 unchanged; GATE 4 not re-run); existing competitor Anchor values stable (rows C0...C{N} unchanged; only new row C{N+1} added); slot 4 stable (SOURCE unchanged; Phase 4 not re-run); slot 5 stable (Focus-scope evidence unchanged unless whitespace re-run changes cross-dim proof -- not possible without Phase 4 re-run) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written at GATE 4 write row; all registry row 2 "Consumed by" consumers re-execute: slot 6 updated per new mechanism phrase; Phase 3 vs-INERTIA-REF ternary re-classified; Phase 4 proof reviewed for THEREFORE alignment | 1 (INERTIA-REF), 6 (INERTIA-REF-DELTA), 3 (vs-INERTIA-REF rows), 5 (if THEREFORE baseline shifts) | GATE 4 (all rows; slot 1 re-written), GATE 3 (if slot 5 rebuild required) | FOCUS-STATE stable (slot 0 unchanged; GATE 0 not re-run; Phase 4 PATH routing unchanged); competitor Anchor values stable (slot 2 unchanged; GATE 1 and GATE 2 results unchanged; C0 row Mechanism cell stable -- INERTIA-REF refinement updates the token, not the table row); Phase 2 Focus column stable (slot 0 unchanged; Focus column inclusion unchanged) |

An amendment that writes to a slot or token listed in the Invariants column constitutes an **amendment invariant failure** -- return to the adjustment specification before proceeding.

---

## V-04 -- Combined A+B (Phase 2 COMPLETENESS + OUTPUT CONTRACTS "Validated by")

**Axis:** Combined A+B -- V-01's Phase 2 COMPLETENESS row makes Phase 2 self-validating at its tail, parallel to Phase 5; V-02's "Validated by" column makes each slot's format enforcement machine-readable from the contract table.

**Hypothesis:** V-01 closes the Phase 2 production tail gap: Phase 2 exits only after a structural checkpoint confirms the table is ready for Phase 3 to consume. V-02 closes the OUTPUT CONTRACTS validation-side gap: each slot's checker is co-declared with its writer and consumers in the contract table. Combined, every slot's full lifecycle (write, validate, consume) is readable within PREFLIGHT, and Phase 2's collective output is confirmed before Phase 3 reads it.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6) -- "Validated by" column names the gate or phase enforcing each slot's format. WRITE-TOKEN REGISTRY follows -- "Consumed by" column. GATE 0 follows (registry row 1). EXECUTION DEPENDENCY: Phase 2 split into per-row + COMPLETENESS row; Phase 4 PATH row listed as its own step; Phase 5 split into finding rows + COMPLETENESS row; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). GATE 3 has 4 rows -- PATH-PRESENT at row 0. Gates 1-4 follow.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Validated by | Required by |
|------|-------|-----------------|-----------------|--------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row -- WRITE-TOKEN REGISTRY row 1) | GATE 0 Write row (format enforced at write time; re-validated at GATE 0 re-run on focus shift) | No upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 1 "Consumed by": Phase 2 per-row (Focus column), Phase 2 COMPLETENESS (Focus-column-present check), Phase 4 PATH row (branch routing), Phase 4 REDUCTION+THEREFORE rows (path selector), slot 5 (format selection) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row -- WRITE-TOKEN REGISTRY row 2) | GATE 4 row 1 (mechanism specificity check) + GATE 4 row 2 (write enforces format); re-validated on refinement | Root -- no upstream dependency; all consumers listed in WRITE-TOKEN REGISTRY row 2 "Consumed by" |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | GATE 2 row 1 (per-row); Phase 2 COMPLETENESS row (aggregate) | Slot 3 requires slot 2 complete; slot 6 uses slot 2 at Phase 5; Phase 2 COMPLETENESS validates all anchor values conform |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Phase 3 ABSENCE-EVIDENCE row + GATE 2 row 2 | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` | Phase 4 -- Cross-Dimensional Finding | GATE 3 row 2 (SOURCE-follows-PATH) | Required by slot 5; must follow PATH row immediately |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | GATE 3 rows 3-4 (active); Phase 4 PATH row validates `VACUOUS-5` (inactive); any other value is a **collection gate failure** | Requires slot 0; active requires slots 4 and 1 |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | GATE 4 row 3 (per row); Phase 5 COMPLETENESS row (aggregate) | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate named in "Validated by".

---

### WRITE-TOKEN REGISTRY

All write-token gate events. An omitted registry row is a **write-token registry gap**. An omitted or incomplete "Consumed by" entry is a **write-token consumer gap**.

| # | Gate | Token written | Slot | Pre-DAG? | Consumed by | Execution constraint |
|---|------|--------------|------|---------|-------------|---------------------|
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes | Phase 2 per-row (Focus column); Phase 2 COMPLETENESS (Focus-column-present check); Phase 4 PATH row (branch decision); Phase 4 REDUCTION+THEREFORE rows (path selector) | Must complete before Phase 2 reads slot 0; must complete before Phase 4 PATH row reads slot 0 |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) | Phase 2 per-row (C0 row reference); Phase 4 REDUCTION+THEREFORE rows (cited in THEREFORE); Phase 5 finding rows (INERTIA-REF-DELTA per row) | Must complete before Phase 1 and all phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows. Listed as Step 0 (-- (pre-DAG)) and WRITE-TOKEN REGISTRY row 1. Fills slot 0; validates slot 0 format per OUTPUT CONTRACTS "Validated by"; all consumers declared in registry row 1 "Consumed by" including Phase 2 COMPLETENESS.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; validates format per OUTPUT CONTRACTS "Validated by"; WRITE-TOKEN REGISTRY row 1 complete | **Focus write failure** -- slot 0 format unvalidated; registry row 1 incomplete |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table; Phase 2 COMPLETENESS Focus-column-present = YES; Phase 4 PATH routes to SOURCE; slot 5 fills as pipe-delimited proof string; GATE 3 validates slots 4+5 per "Validated by" | **Focus activation failure** |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent; Phase 2 COMPLETENESS Focus-column-present = VACUOUS; Phase 4 PATH writes `VACUOUS-5` and exits; PATH validates slot 5 per "Validated by" | **Focus inactivation failure** |

NOT ACCEPTABLE (slot 5, inactive): empty cell or prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Full lifecycle. Phase 2 split: per-row + COMPLETENESS row. Phase 5 split: finding rows + COMPLETENESS row. Step 0 (GATE 0) pre-DAG; GATE 4 data-dependency root. "Reads slot" declares all reads including conditional reads. An omitted conditional read is an **execution dependency gap**.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG; validates slot 0 per OUTPUT CONTRACTS "Validated by"; WRITE-TOKEN REGISTRY row 1; "Consumed by": Phase 2 per-row, Phase 2 COMPLETENESS, Phase 4 PATH, Phase 4 REDUCTION+THEREFORE | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all phases**; validates slot 1 per OUTPUT CONTRACTS "Validated by"; data-dependency root; WRITE-TOKEN REGISTRY row 2 | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context | GATE 4 |
| Phase 2, per competitor row | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 row reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row; GATE 2 validates slot 2 per "Validated by" | Phase 1 |
| Phase 2, COMPLETENESS row | 0 -- FOCUS-STATE (Focus-column-present check), 2 -- Anchor column value (aggregate format validation) | -- (validates; no slot write) | Final row of Phase 2: C0 at row 0; external rows >= 3; all non-C0 GATE 1 PASS; all rows GATE 2 PASS per "Validated by"; absent = **competitor table completeness failure** | Phase 2 per competitor rows |
| Phase 3, per whitespace candidate | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION (4 rows); slot 3 validated by Phase 3 ABSENCE-EVIDENCE + GATE 2 row 2 per "Validated by"; executes after Phase 2 COMPLETENESS confirms table ready | Phase 2 COMPLETENESS row |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table; inactive: validates slot 5 `VACUOUS-5` format per "Validated by" | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately after PATH; slot 4 validated by GATE 3 row 2 per "Validated by" | Phase 4 PATH row |
| Phase 4, REDUCTION + THEREFORE rows | 0 -- FOCUS-STATE (path selector), 4 -- SOURCE, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: slot 5 validated by GATE 3 rows 3-4 per "Validated by" | Phase 4 SOURCE row |
| Phase 5, finding rows | 1 -- INERTIA-REF, 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 4 row 3 validates slot 6 per row per "Validated by" | Phase 4 |
| Phase 5, COMPLETENESS row | 0 -- FOCUS-STATE (cross-dim? check), 2, 6 | -- (validates; no slot write) | Aggregate slot 2 and slot 6 validation per "Validated by"; absent = **findings completeness failure** | Phase 5 finding rows |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column | **Citation gate failure** -- suppress row; run WebSearch |
| Citation in row, not footnote | URL inline in table row | **Citation gate failure** -- relocate |

---

### GATE 2: ANCHOR GATE

Validates slot 2 (competitor Anchor) and slot 3 (whitespace absence anchor) per OUTPUT CONTRACTS "Validated by".

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` -- validates slot 2 per OUTPUT CONTRACTS "Validated by" | **Anchor gate failure** -- name-only does not conform |
| Whitespace absence anchor | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` per row -- validates slot 3 per OUTPUT CONTRACTS "Validated by" | **Whitespace gate failure** -- bare assertion fails |

NOT ACCEPTABLE: `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff -- no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

Validates slots 4 and 5 per OUTPUT CONTRACTS "Validated by".

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| PATH row present | PATH row exists as row 0 of Phase 4 proof table; both active and inactive branches declared | **Path absent failure** -- any row before PATH is a **proof structure failure** |
| SOURCE follows PATH row | SOURCE is first data row after PATH; slot 4 validated by this row per OUTPUT CONTRACTS "Validated by" | **Proof structure failure** -- SOURCE must immediately follow PATH |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE written only after both NO; slot 5 pipe-delimited validated per OUTPUT CONTRACTS "Validated by" | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: Phase 4 has no PATH row -- **path absent failure**; THEREFORE first -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Validates slots 1 and 6 per OUTPUT CONTRACTS "Validated by". Execute all three rows before Phase 1. Data-dependency root; WRITE-TOKEN REGISTRY row 2.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1; validates slot 1 per OUTPUT CONTRACTS "Validated by"; WRITE-TOKEN REGISTRY row 2 complete | **Inertia write failure** -- slot 1 format unvalidated |
| Per-finding citation required | Each finding: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- validates slot 6 per row per "Validated by"; Phase 5 COMPLETENESS validates aggregate | **Inertia citation failure** |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 0 and slot 1 per EXECUTION DEPENDENCY. C0 as Row C0. WebSearch per external competitor. Apply GATE 1 and GATE 2 per row; GATE 2 validates slot 2 per OUTPUT CONTRACTS "Validated by". Focus column when slot 0 = active. Final row is COMPLETENESS row -- required; validates aggregate slot 2 per "Validated by".

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|
| (C0...C{N} rows) | ... | HIGH/MED/LOW | ... | ... | `Row C{N}, {attr}: "{val}"` | URL or C0-EXEMPT |
| COMPLETENESS | `C0 present: YES; external rows: {N} (>= 3); citations: {N} non-C0 GATE 1 PASS; anchors: all rows GATE 2 PASS per "Validated by"` | -- | -- | `Focus column: {present / absent}` | `{N+1} rows GATE 2 PASS` | `{N} non-C0 GATE 1 PASS` |

**Anchor column** (structural; validated by GATE 2 per OUTPUT CONTRACTS "Validated by"; aggregate by Phase 2 COMPLETENESS): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

COMPLETENESS required. Absent = **competitor table completeness failure**. C0 citation-exempt.

---

### PHASE 3: WHITESPACE (fills slot 3, PREFLIGHT > OUTPUT CONTRACTS)

Executes after Phase 2 COMPLETENESS confirms table ready. 4-row WHITESPACE VALIDATION per candidate. CANDIDATE first. Slot 3 validated by Phase 3 ABSENCE-EVIDENCE + GATE 2 row 2 per OUTPUT CONTRACTS "Validated by".

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` -- declared before evidence | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row -- fills and validates slot 3 per OUTPUT CONTRACTS "Validated by" | **Whitespace gate failure** -- bare assertion fails |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}]` or `Gap not confirmed: Row C{N} provides [{value}]; select a different candidate` | **Whitespace gate failure** |
| vs-INERTIA-REF | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` -- ternary token required | **Whitespace INERTIA-REF format failure** |

NOT ACCEPTABLE: Bare assertion -- **whitespace gate failure**; prose without ternary token -- **whitespace INERTIA-REF format failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slots 4 and 5, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3 (validates slots 4 and 5 per OUTPUT CONTRACTS "Validated by"). Row 0 is PATH; reads slot 0; routes active/inactive.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| PATH | Read slot 0: `active -> proceed to SOURCE; inactive -> write VACUOUS-5: focus-inactive to slot 5; exit` -- inactive PATH validates slot 5 per "Validated by" | **Path routing failure** -- GATE 3 row 0 fails |
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; validated by GATE 3 row 2 per "Validated by" | **Proof structure failure** |
| REDUCTION-1 | `NO -- {what is lost if focus dimension dropped}` | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if competitive map dropped}` | **Proof structure failure** -- if YES, discard |
| THEREFORE | slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`; validated by GATE 3 rows 3-4 per "Validated by" | **Proof structure failure** -- THEREFORE blocked until both NO |

---

### PHASE 5: FINDINGS TABLE (fills slots 2 and 6, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings followed by COMPLETENESS row. GATE 4 row 3 validates slot 6 per row; Phase 5 COMPLETENESS validates aggregate -- both per OUTPUT CONTRACTS "Validated by".

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|
| (2-5 finding rows) | ... | `Row C{N}, {attribute}: "{value}"` | `vs. INERTIA-REF -- {ternary}: {mechanism phrase}` | YES / NO |
| COMPLETENESS | `All {N} rows: Anchor GATE 2 PASS (per "Validated by"); INERTIA-REF-DELTA GATE 4 row 3 PASS (per "Validated by"); cross-dim present when slot 0 active` | `{N} rows GATE 2 PASS` | `{N} rows GATE 4 row 3 PASS` | `YES / VACUOUS` |

**Anchor column** (validated by GATE 2 per "Validated by"; aggregate by Phase 2 COMPLETENESS): `Row C{N}, {attribute}: "{value}"` -- name-only malformed.
**INERTIA-REF-DELTA column** (validated by GATE 4 row 3 per row, aggregate by Phase 5 COMPLETENESS per "Validated by"): ternary format required; "N/A" malformed.

NOT ACCEPTABLE (Anchor): name-only -- **anchor gate failure**. An absent COMPLETENESS row is a **findings completeness failure**.

---

### AMEND

Execute exactly 3 adjustment rows.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run |
|---|-----------|-------------------|------------------------|-----------------|--------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written and re-validated at GATE 0 per "Validated by"; all "Consumed by" consumers re-execute: Phase 2 re-reads slot 0; Phase 2 COMPLETENESS Focus-column-present re-evaluated; Phase 4 PATH re-evaluated; activating: slot 5 rebuilt, re-validated by GATE 3 per "Validated by"; Phase 5 COMPLETENESS cross-dim? = YES; deactivating: slot 5 = `VACUOUS-5`, re-validated by PATH per "Validated by"; Phase 5 COMPLETENESS cross-dim? = VACUOUS | 0, 4, 5 | GATE 0 (slot 0 re-validated per "Validated by"), GATE 3 (slots 4+5 re-validated per "Validated by"); proof rerun failure if THEREFORE written without rerunning reductions; Phase 2 COMPLETENESS re-run; Phase 5 COMPLETENESS re-run |
| 2 | Add competitor | Competitor name + WebSearch context | New row slot 2 re-validated by GATE 2 per "Validated by"; Phase 2 COMPLETENESS row count incremented; Phase 3 re-run; slot 3 re-validated per "Validated by" | 2, 3 | GATE 1, GATE 2 (slot 2 per "Validated by"); Phase 2 COMPLETENESS re-run |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written and re-validated at GATE 4 per "Validated by"; all registry row 2 "Consumed by" consumers re-execute; slot 6 re-validated by GATE 4 row 3 and Phase 5 COMPLETENESS per "Validated by" | 1, 6, 3, 5 (if baseline shifts) | GATE 4 (slot 1 re-validated per "Validated by"), GATE 3 (if slot 5 rebuild required); Phase 5 COMPLETENESS re-run |

---

## V-05 -- Maximum (Phase 2 COMPLETENESS + "Validated by" + AMEND Invariants)

**Axis:** Maximum -- V-01's Phase 2 COMPLETENESS closes the Phase 2 tail gap; V-02's "Validated by" column makes each slot's format enforcement readable from the contract table; V-03's AMEND Invariants column makes the amendment stable set machine-readable alongside the delta.

**Hypothesis:** Three symmetry gaps closed simultaneously. Phase 2 is now self-validating at its tail (parallel to Phases 3, 4, 5). OUTPUT CONTRACTS now declares write, validate, and consume for every slot in one table row. AMEND now declares both what changes and what must not change in every adjustment row. Together, the skill's PREFLIGHT is a complete formal specification: every slot's lifecycle is bidirectional (producer, validator, consumers), every phase exits through a named structural checkpoint, and every amendment is bounded by both its delta and its invariants.

---

You are running **discover-competitors-alt**.

---

## PREFLIGHT

All gates and output specifications defined here. OUTPUT CONTRACTS first (slots 0-6) -- "Validated by" column names the gate or phase enforcing each slot's format. WRITE-TOKEN REGISTRY follows -- "Consumed by" column. GATE 0 follows (registry row 1). EXECUTION DEPENDENCY: Phase 2 split into per-row + COMPLETENESS row; Phase 4 PATH row listed as its own step; Phase 5 split into finding rows + COMPLETENESS row; GATE 0 Step 0 (-- (pre-DAG)); GATE 4 root (None (root)). GATE 3 has 4 rows -- PATH-PRESENT at row 0. Gates 1-4 follow. AMEND includes "Invariants" column.

---

### OUTPUT CONTRACTS

| Slot | Label | Required format | Filled by phase | Validated by | Required by |
|------|-------|-----------------|-----------------|--------------|-------------|
| 0 | FOCUS-STATE | `{active: {focus_dimension}}` or `{inactive}` | GATE 0 (Write row -- WRITE-TOKEN REGISTRY row 1) | GATE 0 Write row (format enforced at write time; re-validated at GATE 0 re-run) | No upstream dependency; all consumers in WRITE-TOKEN REGISTRY row 1 "Consumed by": Phase 2 per-row (Focus column), Phase 2 COMPLETENESS (Focus-column-present check), Phase 4 PATH row (branch routing), Phase 4 REDUCTION+THEREFORE (path selector), slot 5 (format selection) |
| 1 | INERTIA-REF | `[C0 name]: [specific mechanism -- switching cost, habit lock-in, or workaround satisfaction]` | GATE 4 (Write row -- WRITE-TOKEN REGISTRY row 2) | GATE 4 row 1 (mechanism check) + GATE 4 row 2 (write enforces format); re-validated on refinement | Root -- no upstream dependency; all consumers in WRITE-TOKEN REGISTRY row 2 "Consumed by" |
| 2 | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 -- Competitor Table | GATE 2 row 1 (per-row); Phase 2 COMPLETENESS row (aggregate) | Slot 3 requires slot 2; slot 6 uses slot 2; Phase 2 COMPLETENESS validates all anchor values |
| 3 | Absence evidence block | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- one entry per row per candidate attribute | Phase 3 -- Whitespace | Phase 3 ABSENCE-EVIDENCE row + GATE 2 row 2 | Requires slot 2 |
| 4 | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` | Phase 4 -- Cross-Dimensional Finding | GATE 3 row 2 (SOURCE-follows-PATH) | Required by slot 5; must follow PATH row immediately |
| 5 | Focus-scope evidence | `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when slot 0 = active -- or -- `VACUOUS-5: focus-inactive` when slot 0 = inactive | Phase 4 -- Cross-Dimensional Finding | GATE 3 rows 3-4 (active); Phase 4 PATH row validates `VACUOUS-5` (inactive); any other value is a **collection gate failure** | Requires slot 0; active requires slots 4 and 1 |
| 6 | INERTIA-REF-DELTA | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase from slot 1}` | Phase 5 -- Findings Table | GATE 4 row 3 (per row); Phase 5 COMPLETENESS row (aggregate) | Derived from slot 1 (root) |

A slot arrived at in the wrong format constitutes a **collection gate failure** -- return to the gate named in "Validated by".

---

### WRITE-TOKEN REGISTRY

All write-token gate events. No phase outside GATE 0 and GATE 4 performs a write-token event. An omitted registry row is a **write-token registry gap**. An omitted or incomplete "Consumed by" entry is a **write-token consumer gap**.

| # | Gate | Token written | Slot | Pre-DAG? | Consumed by | Execution constraint |
|---|------|--------------|------|---------|-------------|---------------------|
| 1 | GATE 0 Write row | FOCUS-STATE | 0 | Yes -- executes before GATE 4 and Phase 1 | Phase 2 per-row (slot 0 -- Focus column inclusion); Phase 2 COMPLETENESS (slot 0 -- Focus-column-present check); Phase 4 PATH row (slot 0 -- branch decision); Phase 4 REDUCTION+THEREFORE rows (slot 0 -- path selector) | Must complete before Phase 2 reads slot 0; must complete before Phase 4 PATH row reads slot 0 |
| 2 | GATE 4 Write row | INERTIA-REF | 1 | No -- data-dependency root; None (root) | Phase 2 per-row (slot 1 -- C0 row mechanism reference); Phase 4 REDUCTION+THEREFORE rows (slot 1 -- cited in THEREFORE); Phase 5 finding rows (slot 1 -- INERTIA-REF-DELTA per row) | Must complete before Phase 1 and all phases; slot 1 required by all downstream phases |

---

### GATE 0: FOCUS GATE

Resolve and write focus state before reading EXECUTION DEPENDENCY or any numbered gate. Execute all four rows. Step 0 (-- (pre-DAG)); WRITE-TOKEN REGISTRY row 1. Fills slot 0; validates format per OUTPUT CONTRACTS "Validated by"; all consumers in registry row 1 "Consumed by" including Phase 2 COMPLETENESS.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Focus value detected | `focus:` set to recognized value (market-sizing, positioning-framework) -- OR -- not set; infer from repo context before defaulting to none | **Focus detection failure** -- resolve before proceeding |
| Write FOCUS-STATE token | Write: `FOCUS-STATE = {active: {focus_dimension}}` or `FOCUS-STATE = {inactive}` -- fills slot 0; validates format per OUTPUT CONTRACTS "Validated by"; WRITE-TOKEN REGISTRY row 1 complete | **Focus write failure** -- slot 0 format unvalidated; registry incomplete |
| Focus-active branch | When slot 0 = active: Focus column added to Phase 2 table; Phase 2 COMPLETENESS Focus-column-present = YES; Phase 4 PATH routes to SOURCE (GATE 3 row 0 verifies); slot 5 built as pipe-delimited proof string; GATE 3 validates slots 4+5 per "Validated by" | **Focus activation failure** |
| Focus-inactive branch | When slot 0 = inactive: Focus column absent; Phase 2 COMPLETENESS Focus-column-present = VACUOUS; Phase 4 PATH writes `VACUOUS-5` and exits; PATH validates slot 5 per "Validated by" | **Focus inactivation failure** |

NOT ACCEPTABLE (slot 5, inactive): empty cell or prose -- **collection gate failure**
ACCEPTABLE (slot 5, inactive): `VACUOUS-5: focus-inactive`

---

### EXECUTION DEPENDENCY

Full lifecycle. Phase 2 split: per-row + COMPLETENESS row. Phase 5 split: finding rows + COMPLETENESS row. Step 0 (GATE 0) pre-DAG; GATE 4 data-dependency root. "Reads slot" declares all reads including conditional reads. An omitted conditional read is an **execution dependency gap**.

| Step | Reads slot | Writes slot | Execution constraint | Prerequisite steps |
|------|-----------|------------|---------------------|-------------------|
| GATE 0 (Focus state) | -- | 0 -- FOCUS-STATE | Pre-DAG; validates slot 0 per OUTPUT CONTRACTS "Validated by"; WRITE-TOKEN REGISTRY row 1; "Consumed by": Phase 2 per-row, Phase 2 COMPLETENESS, Phase 4 PATH, Phase 4 REDUCTION+THEREFORE | -- (pre-DAG) |
| GATE 4 (Write row) | -- (root) | 1 -- INERTIA-REF | **Must execute before Phase 1 and all phases**; validates slot 1 per "Validated by"; data-dependency root; WRITE-TOKEN REGISTRY row 2 | None (root) |
| Phase 1 | -- | TOPIC, FOCUS tokens | Reads repo context | GATE 4 |
| Phase 2, per competitor row | 0 -- FOCUS-STATE (Focus column inclusion), 1 -- INERTIA-REF (C0 reference) | 2 -- Anchor column value | GATE 1 and GATE 2 per row; GATE 2 validates slot 2 per "Validated by" | Phase 1 |
| Phase 2, COMPLETENESS row | 0 -- FOCUS-STATE (Focus-column-present check), 2 -- Anchor column value (aggregate validation) | -- (validates; no slot write) | Final row of Phase 2: C0 at row 0; external rows >= 3; all non-C0 GATE 1 PASS; all rows GATE 2 PASS per "Validated by"; absent = **competitor table completeness failure** | Phase 2 per competitor rows |
| Phase 3, per whitespace candidate | 2 -- Anchor column value | 3 -- Absence evidence block | WHITESPACE VALIDATION (4 rows); slot 3 validated by Phase 3 ABSENCE-EVIDENCE + GATE 2 row 2 per "Validated by"; executes after Phase 2 COMPLETENESS confirms table ready | Phase 2 COMPLETENESS row |
| Phase 4, PATH row | 0 -- FOCUS-STATE (branch decision) | -- (routes; no slot write) | Row 0 of Phase 4 table; inactive: validates slot 5 `VACUOUS-5` per "Validated by" | Phase 3 |
| Phase 4, SOURCE row | 2 -- Anchor column value | 4 -- SOURCE slot | Immediately after PATH; slot 4 validated by GATE 3 row 2 per "Validated by" | Phase 4 PATH row |
| Phase 4, REDUCTION + THEREFORE rows | 0 -- FOCUS-STATE (path selector), 4 -- SOURCE, 1 -- INERTIA-REF | 5 -- Focus-scope evidence | Active: slot 5 validated by GATE 3 rows 3-4 per "Validated by" | Phase 4 SOURCE row |
| Phase 5, finding rows | 1 -- INERTIA-REF, 2 -- Anchor column value | 6 -- INERTIA-REF-DELTA | GATE 4 row 3 validates slot 6 per row per "Validated by" | Phase 4 |
| Phase 5, COMPLETENESS row | 0 -- FOCUS-STATE (cross-dim? check), 2, 6 | -- (validates; no slot write) | Aggregate slot 2 and slot 6 validation per "Validated by"; absent = **findings completeness failure** | Phase 5 finding rows |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column | **Citation gate failure** -- suppress row; run WebSearch |
| Citation in row, not footnote | URL inline in table row | **Citation gate failure** -- relocate |

---

### GATE 2: ANCHOR GATE

Validates slot 2 (competitor Anchor) and slot 3 (whitespace absence anchor) per OUTPUT CONTRACTS "Validated by".

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` -- validates slot 2 per OUTPUT CONTRACTS "Validated by"; Phase 2 COMPLETENESS validates aggregate | **Anchor gate failure** -- name-only does not conform |
| Whitespace absence anchor | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` -- validates slot 3 per OUTPUT CONTRACTS "Validated by" | **Whitespace gate failure** -- bare assertion fails |

NOT ACCEPTABLE: `Competitor 2 reveals that...` -- name-only -- **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "bundles review feedback inside the PR diff -- no persistent async record outside the PR lifecycle"`

---

### GATE 3: PROOF GATE

Validates slots 4 and 5 per OUTPUT CONTRACTS "Validated by".

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| PATH row present | PATH row exists as row 0 of Phase 4 proof table; both active and inactive branches declared | **Path absent failure** -- any row before PATH is a **proof structure failure** |
| SOURCE follows PATH row | SOURCE is first data row after PATH; slot 4 validated by this row per OUTPUT CONTRACTS "Validated by" | **Proof structure failure** -- SOURCE must immediately follow PATH |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 each contain "NO" with one sentence | **Proof structure failure** -- either YES means discard |
| THEREFORE blocked | THEREFORE only after both NO; slot 5 pipe-delimited validated per OUTPUT CONTRACTS "Validated by" | **Proof structure failure** -- retroactive construction fails |

NOT ACCEPTABLE: Phase 4 has no PATH row -- **path absent failure**; THEREFORE first -- **proof structure failure**

---

### GATE 4: INERTIA-REF GATE

Validates slots 1 and 6 per OUTPUT CONTRACTS "Validated by". Execute all three rows before Phase 1. Data-dependency root; WRITE-TOKEN REGISTRY row 2.

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | Concrete mechanism: switching cost, habit lock-in, or workaround satisfaction -- not a category label | **Inertia naming failure** -- resolve before write step |
| Write INERTIA-REF token | Write: `INERTIA-REF = [C0 name]: [mechanism phrase]` -- fills slot 1; validates slot 1 per OUTPUT CONTRACTS "Validated by"; WRITE-TOKEN REGISTRY row 2 complete | **Inertia write failure** -- slot 1 format unvalidated |
| Per-finding citation required | Each finding: `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase}` -- validates slot 6 per row per "Validated by"; Phase 5 COMPLETENESS validates aggregate | **Inertia citation failure** |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)

Reads slot 0 and slot 1 per EXECUTION DEPENDENCY. C0 as Row C0. WebSearch per external competitor. Apply GATE 1 and GATE 2 per row; GATE 2 validates slot 2 per OUTPUT CONTRACTS "Validated by". Focus column when slot 0 = active. Final row is COMPLETENESS row -- required; validates aggregate slot 2 per "Validated by".

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|
| (C0...C{N} rows) | ... | HIGH/MED/LOW | ... | ... | `Row C{N}, {attr}: "{val}"` | URL or C0-EXEMPT |
| COMPLETENESS | `C0 present: YES; external rows: {N} (>= 3); citations: {N} non-C0 GATE 1 PASS per "Validated by"; anchors: all rows GATE 2 PASS per "Validated by"` | -- | -- | `Focus column: {present / absent}` | `{N+1} rows GATE 2 PASS` | `{N} non-C0 GATE 1 PASS` |

**Anchor column** (structural; validated by GATE 2 per "Validated by"; aggregate by Phase 2 COMPLETENESS): `Row C{N}, {attribute}: "{value}"` -- name-only malformed; apply GATE 2.

COMPLETENESS required as final row. Absent = **competitor table completeness failure**. C0 citation-exempt.

---

### PHASE 3: WHITESPACE (fills slot 3, PREFLIGHT > OUTPUT CONTRACTS)

Executes after Phase 2 COMPLETENESS confirms table ready. 4-row WHITESPACE VALIDATION per candidate. CANDIDATE first. Slot 3 validated by Phase 3 ABSENCE-EVIDENCE + GATE 2 row 2 per OUTPUT CONTRACTS "Validated by".

| Whitespace step | Required value | Failure state |
|-----------------|----------------|---------------|
| CANDIDATE | `{attribute name}` -- declared before evidence | **Whitespace naming failure** |
| ABSENCE-EVIDENCE | `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row -- fills and validates slot 3 per OUTPUT CONTRACTS "Validated by" | **Whitespace gate failure** -- bare assertion fails |
| GAP-CONFIRMED | `Gap confirmed: No row provides a non-absent value for [{attribute}]` or `Gap not confirmed: Row C{N} provides [{value}]; select a different candidate` | **Whitespace gate failure** |
| vs-INERTIA-REF | `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` -- ternary token required | **Whitespace INERTIA-REF format failure** |

NOT ACCEPTABLE: Bare assertion -- **whitespace gate failure**; prose without ternary token -- **whitespace INERTIA-REF format failure**
ACCEPTABLE: `vs. INERTIA-REF -- challenges: [mechanism phrase] -- vacant attribute would displace C0 workaround if offered`

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills slots 4 and 5, PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3 (validates slots 4 and 5 per OUTPUT CONTRACTS "Validated by"; 4-row: PATH-PRESENT, SOURCE-follows-PATH, both-NO, THEREFORE-blocked). Row 0 is PATH; reads slot 0; routes active/inactive.

| Proof step | Required value | Failure state |
|------------|----------------|---------------|
| PATH | Read slot 0: `active -> proceed to SOURCE; inactive -> write VACUOUS-5: focus-inactive to slot 5; exit` -- inactive PATH validates slot 5 per OUTPUT CONTRACTS "Validated by" | **Path routing failure** -- PATH absent or not row 0; GATE 3 row 0 fails |
| SOURCE | `{row label}, {attribute}: "{quoted value}"` -- fills slot 4; validated by GATE 3 row 2 per "Validated by" | **Proof structure failure** -- SOURCE must follow PATH |
| REDUCTION-1 | `NO -- {what is lost if focus dimension dropped}` | **Proof structure failure** -- if YES, discard |
| REDUCTION-2 | `NO -- {what is lost if competitive map dropped}` | **Proof structure failure** -- if YES, discard |
| THEREFORE | slot 5 = `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`; validated by GATE 3 rows 3-4 per "Validated by" | **Proof structure failure** -- THEREFORE blocked until both NO |

---

### PHASE 5: FINDINGS TABLE (fills slots 2 and 6, PREFLIGHT > OUTPUT CONTRACTS)

Write 2-5 findings followed by COMPLETENESS row. GATE 4 row 3 validates slot 6 per row; Phase 5 COMPLETENESS validates aggregate -- both per OUTPUT CONTRACTS "Validated by".

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|
| (2-5 finding rows) | ... | `Row C{N}, {attribute}: "{value}"` | `vs. INERTIA-REF -- {ternary}: {mechanism phrase}` | YES / NO |
| COMPLETENESS | `All {N} rows: Anchor GATE 2 PASS (per "Validated by"); INERTIA-REF-DELTA GATE 4 row 3 PASS (per "Validated by"); cross-dim present when slot 0 active` | `{N} rows GATE 2 PASS` | `{N} rows GATE 4 row 3 PASS` | `YES / VACUOUS` |

**Anchor column** (validated by GATE 2 per "Validated by"; aggregate by Phase 2 COMPLETENESS): `Row C{N}, {attribute}: "{value}"` -- name-only malformed.
**INERTIA-REF-DELTA column** (validated by GATE 4 row 3 per row, aggregate by Phase 5 COMPLETENESS per "Validated by"): ternary format required; "N/A" malformed.

NOT ACCEPTABLE (Anchor): name-only -- **anchor gate failure**. Absent COMPLETENESS = **findings completeness failure**.

---

### AMEND

Execute exactly 3 adjustment rows. "Invariants" column names slots and tokens that must remain unchanged -- violations are **amendment invariant failures**.

| # | Adjustment | What user changes | What changes in output | Slots re-filled | Gates re-run | Invariants |
|---|-----------|-------------------|------------------------|-----------------|--------------|------------|
| 1 | Shift focus dimension | Replace `{focus_dimension}` (or activate/deactivate) | Slot 0 re-written and re-validated at GATE 0 per "Validated by"; all "Consumed by" consumers re-execute: Phase 2 re-reads slot 0; Phase 2 COMPLETENESS Focus-column-present re-evaluated; Phase 4 PATH re-evaluated; activating: Focus column added, slot 5 rebuilt as proof string, re-validated by GATE 3 per "Validated by", Phase 5 COMPLETENESS cross-dim? = YES; deactivating: Focus column removed, slot 5 = `VACUOUS-5`, re-validated by PATH per "Validated by", Phase 5 COMPLETENESS cross-dim? = VACUOUS | 0, 4, 5 | GATE 0 (all rows; slot 0 re-validated per "Validated by"), GATE 3 (all 4 rows; slots 4+5 re-validated per "Validated by"); proof rerun failure if THEREFORE written without rerunning reductions; Phase 2 COMPLETENESS re-run; Phase 5 COMPLETENESS re-run | INERTIA-REF stable (slot 1 unchanged; GATE 4 write row not re-run; registry row 2 not re-executed); competitor Anchor values stable (slot 2 values C0...C{N} unchanged; GATE 1 and GATE 2 results unchanged); slot 3 stable (Phase 3 not re-run; slot 2 inputs unchanged); Phase 2 COMPLETENESS citation/anchor counts unchanged |
| 2 | Add competitor | Competitor name + WebSearch context | New row appended (slot 2 extended; validated by GATE 2 per "Validated by"); Phase 2 COMPLETENESS row count incremented; Phase 3 re-run; slot 3 re-validated per "Validated by" | 2 (new row anchor), 3 | GATE 1 (new row), GATE 2 (new row; slot 2 per "Validated by"); Phase 2 COMPLETENESS re-run | FOCUS-STATE stable (slot 0 unchanged; GATE 0 not re-run); INERTIA-REF stable (slot 1 unchanged; GATE 4 not re-run); existing competitor Anchor values stable (rows C0...C{N} unchanged; only C{N+1} added); slot 4 stable (SOURCE unchanged; Phase 4 not re-run); slot 5 stable (Focus-scope evidence unchanged; Phase 4 not re-run) |
| 3 | Refine INERTIA-REF mechanism | More specific C0 mechanism phrase | Slot 1 re-written and re-validated at GATE 4 per "Validated by"; all registry row 2 "Consumed by" consumers re-execute: slot 6 updated and re-validated by GATE 4 row 3 per "Validated by"; Phase 3 vs-INERTIA-REF ternary re-classified; Phase 4 proof reviewed; Phase 5 COMPLETENESS re-validates all INERTIA-REF-DELTA values per "Validated by" | 1, 6, 3, 5 (if THEREFORE baseline shifts) | GATE 4 (all rows; slot 1 re-validated per "Validated by"), GATE 3 (if slot 5 rebuild required; slots 4+5 re-validated per "Validated by"); Phase 5 COMPLETENESS re-run | FOCUS-STATE stable (slot 0 unchanged; GATE 0 not re-run; Phase 4 PATH routing unchanged); competitor Anchor values stable (slot 2 unchanged; GATE 1 and GATE 2 results unchanged; Phase 2 COMPLETENESS citation/anchor counts unchanged); Phase 2 Focus column stable (slot 0 unchanged; Focus column inclusion unchanged); slot 4 stable unless slot 5 rebuild requires SOURCE re-evaluation |

An adjustment that writes to a slot or token listed in Invariants constitutes an **amendment invariant failure** -- return to the adjustment specification before proceeding.
