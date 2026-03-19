## discover-competitors-alt — Round 14 Scorecard

**Result: All 5 variations score 295/295 on the v13 rubric.**

All R14 variations are built on the R13 V-05 baseline, which already satisfies every criterion through C-49. The differences between variations lie in three new candidate criteria not yet in the rubric:

---

### Per-Variation Feature Matrix

| Candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-50 Phase 2 COMPLETENESS row | PASS | FAIL | FAIL | PASS | PASS |
| C-51 OUTPUT CONTRACTS "Validated by" | FAIL | PASS | FAIL | PASS | PASS |
| C-52 AMEND "Invariants" column | FAIL | FAIL | PASS | FAIL | PASS |

---

### Composite Scores

| Variation | Composite | New candidates |
|-----------|-----------|----------------|
| V-05 | **295** | C-50 + C-51 + C-52 |
| V-04 | **295** | C-50 + C-51 |
| V-01 | **295** | C-50 |
| V-02 | **295** | C-51 |
| V-03 | **295** | C-52 |

**V-05 ranks first** by excellence signal richness.

---

### Excellence Signals (from V-05)

**Signal 1 — Phase 2 COMPLETENESS row (C-50):** Phase 2 was the only production phase without a structural tail checkpoint. The COMPLETENESS row confirms: C0 present at row 0; external row count >= 3; all non-C0 rows GATE 1 PASS; all rows GATE 2 PASS; Focus-column-present status. Phase 3's prerequisite step changes from "Phase 2" to "Phase 2 COMPLETENESS row." Absent = **competitor table completeness failure**.

**Signal 2 — OUTPUT CONTRACTS "Validated by" column (C-51):** The existing "Filled by phase" column names the writer; there was no contract-level declaration of who checks. "Validated by" completes the lifecycle — write → validate → consume — readable from a single contract row. Gates back-reference "per OUTPUT CONTRACTS 'Validated by'" throughout.

**Signal 3 — AMEND "Invariants" column (C-52):** AMEND named what changes (Slots re-filled, Gates re-run) but not what must not change. The Invariants column makes each adjustment's stable set machine-readable — violations are named **amendment invariant failures**. Implies C-38; C-38 does not imply C-52.

---

```json
{"top_score": 295, "all_essential_pass": true, "new_patterns": ["Phase 2 COMPLETENESS row as structural tail validation -- every phase that produces a multi-row artifact consumed by a downstream phase closes with a named structural checkpoint confirming collective readiness (C0 present, external row count >= 3, all GATE 1 + GATE 2 pass, Focus-column-present status); absent = competitor table completeness failure; Phase 3 prerequisite step changes to Phase 2 COMPLETENESS row", "OUTPUT CONTRACTS Validated by column -- contract table declares writer (Filled by phase), validator (Validated by), and consumers (Required by), making each slot full lifecycle (write -> validate -> consume) readable from a single row; gates back-reference per OUTPUT CONTRACTS Validated by to close the loop from gate back to contract", "AMEND Invariants column -- each amendment row declares its stable set (what must not change) alongside its delta (Slots re-filled, Gates re-run), formally completing the amendment boundary as a two-sided machine-checkable specification; violations named as amendment invariant failures"]}
```
05)

### C-09 to C-20

| ID | Criterion | All | Evidence note |
|----|-----------|-----|---------------|
| C-09 | Cross-dimensional whitespace finding | PASS | Phase 4 REDUCTION-1 (focus dropped) + REDUCTION-2 (competitive map dropped) required before THEREFORE; slot 5 pipe-delimited proof enforces both |
| C-10 | Table-stakes grounding per finding | PASS | Phase 5 Anchor column `Row C{N}, {attribute}: "{value}"` grounds each finding to a named row and specific attribute; GATE 2 applied per row |
| C-11 | Fully-cited competitor table | PASS | GATE 1 citation applied per external competitor row before row is added; Phase 2 COMPLETENESS validates all non-C0 rows GATE 1 PASS (V-01/V-04/V-05) or per-row enforcement (V-02/V-03) |
| C-12 | Self-negating cross-dimensional finding | PASS | REDUCTION-1 NO requires one sentence explaining what is lost if focus dimension is dropped; REDUCTION-2 NO requires one sentence explaining what is lost if competitive map is dropped; both before THEREFORE |
| C-13 | Claim-level finding anchors | PASS | Anchor column format requires attribute name AND quoted value: `Row C{N}, {attribute}: "{value}"`; name-only form is explicitly NOT ACCEPTABLE per GATE 2 examples |
| C-14 | AMEND as proof validator | PASS | AMEND row 1 (Shift focus) Gates re-run column requires GATE 3 all 4 rows; "proof rerun failure if THEREFORE written without rerunning reductions" named explicitly |
| C-15 | Inline anchor tag before proof block | PASS | Implied by C-45: SOURCE row follows PATH row immediately; both reductions follow SOURCE; evidence declared before proof constructed |
| C-16 | Gate failure naming | PASS | Every gate table names failure states explicitly: **Citation gate failure**, **Anchor gate failure**, **Path absent failure**, **Proof structure failure**, **Focus write failure**, **Inertia naming failure**, **Inertia write failure**, etc. |
| C-17 | WHITESPACE grounded by attribute absence | PASS | Phase 3 ABSENCE-EVIDENCE row requires `Row C{N} -- {attribute}: {absent / "None" / "N/A" / uncontested value}` for every row including C0; bare assertion explicitly NOT ACCEPTABLE |
| C-18 | NOT ACCEPTABLE examples for anchoring | PASS | GATE 2 has two NOT ACCEPTABLE examples naming name-only failures ("Competitor 2 reveals that..." and "As Competitor 1 demonstrates..."); Phase 5 repeats Anchor NOT ACCEPTABLE |
| C-19 | Synthesis-first output contracts | PASS | Phase 2 heading states "(fills slot 2 -- Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)"; collection phase explicitly names downstream slot |
| C-20 | Structural column coercion for anchoring | PASS | Anchor column defined with structural format `Row C{N}, {attribute}: "{value}"` in both Phase 2 and Phase 5; format shape makes name-only entries syntactically non-conforming |

### C-21 to C-34

| ID | Criterion | All | Evidence note |
|----|-----------|-----|---------------|
| C-21 | Gate-as-section with PASS/FAIL table | PASS | GATE 0 through GATE 4 each have named section heading + 3-column table (Check, Pass condition, Failure state) with >= 2 rows |
| C-22 | INERTIA-REF per-finding citation | PASS | Implied by C-31: GATE 4 row 3 requires per-finding ternary citation `vs. INERTIA-REF -- {ternary}: {mechanism phrase}`; Phase 5 COMPLETENESS row validates all rows |
| C-23 | Output contract slot format specification | PASS | "Required format" column in OUTPUT CONTRACTS provides parse-ready templates for all 7 slots (0-6) |
| C-24 | Phase-to-contract back-references | PASS | Phase headings use full-path label "(fills slot N -- [label], PREFLIGHT > OUTPUT CONTRACTS)" in all variations |
| C-25 | Cross-table structural coercion | PASS | Anchor column coercion with format template defined independently in Phase 2 (competitor table) AND in Phase 5 (findings table); coercion spans collection-to-synthesis boundary |
| C-26 | Consolidated PREFLIGHT gate block | PASS | Implied by C-32: GATE 0 through GATE 4 all within single PREFLIGHT section before Phase 1 |
| C-27 | Machine-readable phase assignment in output contract | PASS | "Filled by phase" column in OUTPUT CONTRACTS names producing gate or phase for each of the 7 slots |
| C-28 | OUTPUT CONTRACTS co-located within PREFLIGHT | PASS | Implied by C-32: OUTPUT CONTRACTS is a named subsection within PREFLIGHT in all five variations |
| C-29 | Full-path back-reference labels in producing phases | PASS | All phase headings use "PREFLIGHT > OUTPUT CONTRACTS" not just "OUTPUT CONTRACTS" |
| C-30 | Write-token instruction within INERTIA-REF gate | PASS | Implied by C-31: GATE 4 row 2 (Write INERTIA-REF token) contains explicit write directive and token format |
| C-31 | Write-token encoded as structural gate row | PASS | GATE 4 row 2: Check = "Write INERTIA-REF token"; Pass condition = write directive + slot format; Failure state = "Inertia write failure" -- independent structural table row |
| C-32 | OUTPUT CONTRACTS declared first within PREFLIGHT | PASS | OUTPUT CONTRACTS is first named subsection within PREFLIGHT in all variations, before WRITE-TOKEN REGISTRY and all gate subsections |
| C-33 | Forward-declared cross-dimensional proof slot in output contract | PASS | Implied by C-35: slot 5 "Focus-scope evidence" with pipe-delimited template declared in OUTPUT CONTRACTS before Phase 4 runs |
| C-34 | Inter-slot dependency column in output contract | PASS | "Required by" column present in all OUTPUT CONTRACTS tables; names upstream slots and tokens for each slot (e.g., slot 5 "Requires slot 0; active also requires slots 4 and 1") |

### C-35 to C-49

| ID | Criterion | All | Evidence note |
|----|-----------|-----|---------------|
| C-35 | Syntactic format template for cross-dimensional proof slot | PASS | Slot 5: `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` when active; `VACUOUS-5: focus-inactive` when inactive; both are parse-ready |
| C-36 | Cross-dimensional proof as structural PASS/FAIL table | PASS | Implied by C-45: Phase 4 table has PATH (row 0), SOURCE, REDUCTION-1, REDUCTION-2, THEREFORE rows each with Required value + Failure state |
| C-37 | WHITESPACE validation as CANDIDATE-first PASS/FAIL table | PASS | Phase 3: CANDIDATE (row 0 -- gap declared first), ABSENCE-EVIDENCE, GAP-CONFIRMED, vs-INERTIA-REF; each row has Required value + Failure state |
| C-38 | AMEND as structured table with Slots re-filled and Gates re-run columns | PASS | AMEND table columns: #, Adjustment, What user changes, What changes in output, Slots re-filled, Gates re-run (V-01/V-02/V-04); plus Invariants in V-03/V-05 |
| C-39 | EXECUTION DEPENDENCY table in PREFLIGHT | PASS | Implied by C-42: EXECUTION DEPENDENCY table present in PREFLIGHT; GATE 4 step has "None (root)" in Prerequisite steps; GATE 0 has "-- (pre-DAG)" |
| C-40 | FOCUS GATE as named PASS/FAIL gate in PREFLIGHT | PASS | GATE 0 is a named subsection within PREFLIGHT with 4-row table (Focus detection, Write token, Active branch, Inactive branch) |
| C-41 | Phase 3 vs-INERTIA-REF row uses slot 6 ternary-token format | PASS | vs-INERTIA-REF row requires `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` -- exact slot 6 ternary format; "N/A" not permitted |
| C-42 | EXECUTION DEPENDENCY includes explicit Prerequisite steps column | PASS | "Prerequisite steps" column present; GATE 4 = "None (root)"; GATE 0 = "-- (pre-DAG)"; all downstream steps name specific upstream steps |
| C-43 | FOCUS-STATE declared as named output contract slot | PASS | Slot 0 "FOCUS-STATE" with format template `{active: {focus_dimension}}` or `{inactive}` in all OUTPUT CONTRACTS tables |
| C-44 | Exhaustive "Reads slot" declaration including conditional reads | PASS | EXECUTION DEPENDENCY declares all conditional reads: Phase 2 per-row reads "0 -- FOCUS-STATE (Focus column inclusion)"; Phase 4 PATH reads "0 -- FOCUS-STATE (branch decision)"; Phase 4 REDUCTION+THEREFORE reads slot 0 as path selector; Phase 5 COMPLETENESS reads slot 0 for cross-dim check |
| C-45 | Phase 4 PATH row as structural branch router at row 0 | PASS | Phase 4 table row 0 = PATH; reads slot 0; active branch routes to SOURCE; inactive branch writes `VACUOUS-5: focus-inactive` and exits; both branches declared as independently reviewable table checkpoints |
| C-46 | WRITE-TOKEN REGISTRY as first-class PREFLIGHT table | PASS | Implied by C-47: WRITE-TOKEN REGISTRY is a named subsection within PREFLIGHT after OUTPUT CONTRACTS and before GATE 0 |
| C-47 | WRITE-TOKEN REGISTRY "Consumed by" column | PASS | "Consumed by" column in all WRITE-TOKEN REGISTRY tables; lists downstream consumers per token with slot reference and usage context (e.g., "Phase 2 per-row (slot 0 -- Focus column inclusion)") |
| C-48 | GATE 3 PATH-PRESENT row 0 before SOURCE-position check | PASS | GATE 3 row 0 = "PATH row present" with Check confirming PATH at row 0 and Failure state "Path absent failure"; row 1 = "SOURCE follows PATH row" (SOURCE-position check); PATH absence independently named before any positional check |
| C-49 | Phase 5 COMPLETENESS row as structural tail validation | PASS | Phase 5 final row = COMPLETENESS; confirms all finding rows: Anchor GATE 2 PASS, INERTIA-REF-DELTA GATE 4 row 3 PASS, cross-dim row present when slot 0 active; absent = **findings completeness failure** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational (v13, 41 criteria) | Composite | New candidate criteria satisfied |
|-----------|-----------|-------------|--------------------------------|-----------|----------------------------------|
| V-01 | 60/60 | 30/30 | 205/205 | **295** | C-50 |
| V-02 | 60/60 | 30/30 | 205/205 | **295** | C-51 |
| V-03 | 60/60 | 30/30 | 205/205 | **295** | C-52 |
| V-04 | 60/60 | 30/30 | 205/205 | **295** | C-50, C-51 |
| V-05 | 60/60 | 30/30 | 205/205 | **295** | C-50, C-51, C-52 |

All variations score 295/295 on the v13 rubric. The rubric criteria through C-49 are all satisfied by the shared R13 V-05 baseline. The R14 candidates (C-50, C-51, C-52) are not yet in the rubric -- they represent the excellence signals introduced by these variations.

---

## Ranking

All variations tie at 295/295 on the v13 rubric. Ranking by count of new candidate criteria introduced:

1. **V-05 (Maximum)** -- 295 + C-50 + C-51 + C-52 -- introduces all three new patterns; each of Phase 2, OUTPUT CONTRACTS, and AMEND gains a structural completeness dimension
2. **V-04 (A+B)** -- 295 + C-50 + C-51 -- lifecycle checkpoint (Phase 2 tail) + contract validation column (OUTPUT CONTRACTS); combined: every slot's full lifecycle (write, validate, consume) readable within PREFLIGHT AND Phase 2 self-validates its collective output before Phase 3 reads it
3. **V-01** -- 295 + C-50 -- Phase 2 COMPLETENESS row closes the only remaining phase-tail gap
4. **V-02** -- 295 + C-51 -- OUTPUT CONTRACTS "Validated by" column closes the validation-side declaration gap
5. **V-03** -- 295 + C-52 -- AMEND "Invariants" column formally completes the amendment boundary

**V-05 is the top variation** by excellence signal richness.

---

## Excellence Signals from V-05

Three new structural patterns appear in V-05 that are absent from the v13 rubric:

### Signal 1 -- Phase 2 COMPLETENESS row (C-50; source: V-01/V-04/V-05)

Phase 2 gains a COMPLETENESS row as its final row, closing the last remaining phase-tail gap. Pattern: Phase 3 ends with GAP-CONFIRMED; Phase 4 ends with THEREFORE; Phase 5 ends with COMPLETENESS (C-49). Phase 2 previously ended after the last competitor row with no structural conclusion.

The COMPLETENESS row confirms: C0 present at row 0; external row count >= 3; all non-C0 rows GATE 1 PASS; all rows GATE 2 PASS; Focus-column-present = YES / absent / VACUOUS per slot 0. Phase 3 prerequisite step changes from "Phase 2" to "Phase 2 COMPLETENESS row" -- Phase 3 cannot begin until Phase 2 declares collective readiness. An absent COMPLETENESS row is a **competitor table completeness failure**.

**Extracted rule:** Every phase that produces a multi-row artifact consumed by a downstream phase should close with a named structural checkpoint confirming collective readiness. Production-side and validation-side of a phase's output should be co-located within the same table.

### Signal 2 -- OUTPUT CONTRACTS "Validated by" column (C-51; source: V-02/V-04/V-05)

OUTPUT CONTRACTS gains a sixth column "Validated by" naming the gate or phase that enforces each slot's format after production. "Filled by phase" names the writer; "Validated by" names the checker. Together, each slot's full lifecycle (write -> validate -> consume) is readable from a single contract row without navigating to individual gate descriptions.

In V-05/V-02/V-04, gates back-reference the contract "Validated by" column: "validates slot N per OUTPUT CONTRACTS 'Validated by'" appears in GATE 0 description, GATE 2 preamble, GATE 3 preamble, GATE 4 preamble, and EXECUTION DEPENDENCY step constraints. The **collection gate failure** message points to "the gate named in 'Validated by'" rather than requiring the reader to locate the gate independently.

**Extracted rule:** A slot contract that names its producer and consumers but not its validator is incompletely specified. "Filled by phase" and "Validated by" are symmetric obligations; declaring one without the other yields a partial contract.

### Signal 3 -- AMEND "Invariants" column (C-52; source: V-03/V-05)

AMEND gains a seventh column "Invariants" listing what must remain unchanged after each adjustment. Current AMEND (C-38) names what changes (Slots re-filled, Gates re-run) but not what must not change. Without Invariants, stable artifacts are implicitly assumed unchanged -- the assumption is not checkable by column inspection.

V-05/V-03 enumerate explicit invariants per row: row 1 (Shift focus) -- INERTIA-REF stable (slot 1 unchanged); row 2 (Add competitor) -- FOCUS-STATE stable (slot 0 unchanged); row 3 (Refine INERTIA-REF) -- competitor Anchor values stable (slot 2 unchanged). Violations are named: **amendment invariant failure** -- return to the adjustment specification before proceeding.

**Extracted rule:** An amendment specification is formally complete when it names both its delta (Slots re-filled, Gates re-run) and its stable set (Invariants). A one-sided specification is checkable only for the change, not for unintended side effects.

---

## Dependency Notes for Candidate Criteria

- **C-50** is independent of C-49: C-49 targets Phase 5; C-50 targets Phase 2; neither implies the other. C-50 requires Phase 2 to be a structured table (established since C-21 era). C-50 requires EXECUTION DEPENDENCY to split Phase 2 into per-row step + COMPLETENESS row step (both present in V-01/V-04/V-05); independent of C-44.
- **C-51** is independent of C-27 (Filled by phase) and C-34 (Required by): all three columns coexist; none implies another. C-51 is independent of C-47: C-47 adds "Consumed by" to WRITE-TOKEN REGISTRY; C-51 adds "Validated by" to OUTPUT CONTRACTS; both make lifecycle readable within PREFLIGHT from different tables.
- **C-52** implies C-38 (a table with Invariants necessarily has Slots re-filled and Gates re-run columns); C-38 does not imply C-52. C-52 is independent of C-14 (C-14 requires proof rerun on focus shift; C-52 requires naming stable slots per amendment type; neither implies the other).

---

## Scoring Update Proposal (v13 -> v14)

| | v13 | v14 |
|--|-----|-----|
| Aspirational count | 41 | 44 |
| Aspirational max | 205 | 220 |
| Max composite | 295 | 310 |
| Exceptional | >= 280 | >= 295 |
| Strong | >= 253 | >= 266 |

New criteria for v14:
- C-50: Phase 2 COMPLETENESS row as structural tail validation (5 pts)
- C-51: OUTPUT CONTRACTS "Validated by" column for write-validate-consume lifecycle (5 pts)
- C-52: AMEND "Invariants" column as stable-set declaration (5 pts)

---

```json
{"top_score": 295, "all_essential_pass": true, "new_patterns": ["Phase 2 COMPLETENESS row as structural tail validation -- every phase that produces a multi-row artifact consumed by a downstream phase closes with a named structural checkpoint confirming collective readiness (C0 present, external row count >= 3, all GATE 1 + GATE 2 pass, Focus-column-present status); absent = competitor table completeness failure; Phase 3 prerequisite step changes to Phase 2 COMPLETENESS row", "OUTPUT CONTRACTS Validated by column -- contract table declares writer (Filled by phase), validator (Validated by), and consumers (Required by), making each slot full lifecycle (write -> validate -> consume) readable from a single row; gates back-reference per OUTPUT CONTRACTS Validated by to close the loop from gate back to contract", "AMEND Invariants column -- each amendment row declares its stable set (what must not change) alongside its delta (Slots re-filled, Gates re-run), formally completing the amendment boundary as a two-sided machine-checkable specification; violations named as amendment invariant failures"]}
```
