# discover-competitors-alt — Round 12 Scorecard

## Scoring Parameters (v11 Rubric)

Max composite: **265** | Grade bands: Exceptional ≥ 250 · Strong ≥ 223

---

## Per-Variation Scores

| Criterion range | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------------|------|------|------|------|------|
| C-01–C-05 Essential | 60 | 60 | 60 | 60 | 60 |
| C-06–C-08 Recommended | 30 | 30 | 30 | 30 | 30 |
| C-09–C-43 Aspirational | 175 | 175 | 175 | 175 | 175 |
| **TOTAL** | **265** | **265** | **265** | **265** | **265** |
| **Grade** | Exceptional | Exceptional | Exceptional | Exceptional | Exceptional |

**All five variations tie at 265/265.** R11's key differentiator — C-34 partial (no slot 0) — is closed: C-43 is now rubric and all R12 variations carry FOCUS-STATE as slot 0, making slot 5's "Requires slot 0" dependency machine-readable by slot reference in all variations.

---

## Key Criterion Notes

- **C-34** (inter-slot dependency column): PASS for all — slot 5 "Required by" names "slot 0 (path selector)" in every variation. The R11 PARTIAL gap (V-02/V-03 couldn't express focus dependency as a slot reference) is structurally closed.
- **C-36** (proof as PASS/FAIL table): PASS for V-02/V-04/V-05 with PATH row — SOURCE is still present with required value + failure state; "at least four rows -- SOURCE, REDUCTION-1, REDUCTION-2, THEREFORE" is satisfied even with PATH as row 0.
- **C-32** (OUTPUT CONTRACTS first in PREFLIGHT): PASS for V-03 — WRITE-TOKEN REGISTRY sits between OUTPUT CONTRACTS and GATE 0 but is not a gate subsection; OUTPUT CONTRACTS remains first.

---

## Ranking

| Rank | Variation | Score | Candidate criteria |
|------|-----------|-------|--------------------|
| **1** | **V-05** | **265** | C-44 + C-45 + C-46 |
| 2 | V-04 | 265 | C-44 + C-45 |
| 3 | V-01 | 265 | C-44 |
| 4 | V-02 | 265 | C-45 |
| 5 | V-03 | 265 | C-46 |

---

## Excellence Signals (V-05)

**C-44 — Exhaustive "Reads slot" including conditional reads**
Phase 2 conditionally branches on slot 0 for Focus column inclusion — a real data-flow edge — but R11 V-05 listed only slot 1. V-01/V-04/V-05 declare `0 -- FOCUS-STATE (Focus column inclusion)` alongside slot 1. Rule: every step that conditionally branches on a slot value must declare it in "Reads slot". Omission = **execution dependency gap**.

**C-45 — Phase 4 PATH row extends declaration-before-execution to proof table**
C-37 established CANDIDATE-first for Phase 3. V-02/V-04/V-05 apply the same principle to Phase 4: PATH row as row 0 makes the active/inactive branch decision a table-level checkpoint before SOURCE. Both paths (active → SOURCE; inactive → `VACUOUS-5: focus-inactive` + exit) are independently reviewable without reading phase header prose.

**C-46 — WRITE-TOKEN REGISTRY as first-class PREFLIGHT table**
V-03/V-05 add a dedicated registry table (after OUTPUT CONTRACTS, before GATE 0) indexing all write-token events: gate, token, slot, pre-DAG/DAG. Makes the write-token schedule O(1)-discoverable. Completes the three-table PREFLIGHT specification: OUTPUT CONTRACTS (slot inventory) + EXECUTION DEPENDENCY (step ordering) + WRITE-TOKEN REGISTRY (write-event schedule). V-05 encodes slot 0's complete lifecycle in **five independent structural positions**.

---

```json
{"top_score": 265, "all_essential_pass": true, "new_patterns": ["Exhaustive Reads slot declaration including conditional reads: Phase 2 conditionally branches on slot 0 (FOCUS-STATE) for Focus column inclusion but R11 V-05 omitted slot 0 from Phase 2's Reads slot cell -- V-01/V-04/V-05 add slot 0 as a declared conditional read, closing the execution dependency gap and making the full data-flow graph reconstructable by column inspection without reading phase prose", "Phase 4 PATH row as structural branch router at row 0: V-02/V-04/V-05 add a PATH row before SOURCE that reads slot 0 and declares both execution branches as independently reviewable table checkpoints (active: proceed to SOURCE; inactive: write VACUOUS-5: focus-inactive and exit) -- extends C-37 declaration-before-execution principle from Phase 3 whitespace validation to Phase 4 proof construction", "WRITE-TOKEN REGISTRY as first-class PREFLIGHT table: V-03/V-05 add a dedicated WRITE-TOKEN REGISTRY table (after OUTPUT CONTRACTS, before GATE 0) indexing all write-token gate events by gate name, token, slot, and pre-DAG/DAG classification -- makes the write-token schedule O(1)-discoverable without scanning EXECUTION DEPENDENCY, completing the three-table PREFLIGHT specification: OUTPUT CONTRACTS (slot inventory) + EXECUTION DEPENDENCY (step ordering) + WRITE-TOKEN REGISTRY (write-event schedule)"]}
```
es; minimum 2 rows with Check / Pass condition / Failure state |
| C-22 | INERTIA-REF per-finding citation | GATE 4 row 3: per-finding `vs. INERTIA-REF -- {reinforces/challenges/contextualizes}: {specific C0 mechanism phrase}` required; fills slot 6 |
| C-23 | Output contract slot format specification | Slots 1–6 carry format templates; slot 5 carries full pipe-delimited template; slot 0 carries `{active: {focus_dimension}}` or `{inactive}` |
| C-24 | Phase-to-contract back-references | Phase headings use full-path "fills slot N -- [label], PREFLIGHT > OUTPUT CONTRACTS" at point of production |
| C-25 | Cross-table structural coercion | Anchor coercion in Phase 2 table AND Phase 5 findings table; spans collection-to-synthesis boundary |
| C-26 | Consolidated PREFLIGHT gate block | All gates (GATE 0–4) in single PREFLIGHT block; no gate outside the block |
| C-27 | Machine-readable phase assignment | OUTPUT CONTRACTS "Filled by phase" column: GATE 0, GATE 4, Phase 2, Phase 3, Phase 4, Phase 5 per slot |
| C-28 | OUTPUT CONTRACTS within PREFLIGHT | OUTPUT CONTRACTS is first named subsection of PREFLIGHT; all gates within same block. V-03 adds WRITE-TOKEN REGISTRY between OUTPUT CONTRACTS and GATE 0 — still within PREFLIGHT; C-28 satisfied |
| C-29 | Full-path back-reference labels | Phase headings use "PREFLIGHT > OUTPUT CONTRACTS" — full navigable path to nested contract declaration |
| C-30 | Write-token instruction within INERTIA-REF gate | GATE 4 row 2 contains write directive: "Write: `INERTIA-REF = [C0 name]: [mechanism phrase]`" within gate table |
| C-31 | Write-token encoded as structural gate row | GATE 4 write instruction is a dedicated table row with distinct Check, Pass condition (write directive + format), and Failure state ("Inertia write failure") |
| C-32 | OUTPUT CONTRACTS declared first within PREFLIGHT | OUTPUT CONTRACTS precedes GATE 0 in all variations. V-03: WRITE-TOKEN REGISTRY is between OUTPUT CONTRACTS and GATE 0 but is not a gate subsection — OUTPUT CONTRACTS remains first; C-32 satisfied |
| C-33 | Forward-declared cross-dimensional proof slot | Slot 5 (Focus-scope evidence) in OUTPUT CONTRACTS with full pipe-delimited format template declared before Phase 4 executes |

All C-09–C-33: **PASS / 5 pts — all five variations**

---

#### C-34 — Uniform PASS (all variations — C-43 now in rubric)

**C-34: Inter-slot dependency column in output contract**

All R12 variations inherit slot 0 = FOCUS-STATE as a named output contract slot (C-43 now satisfies C-34 for focus-dependent slots). Slot 5 "Required by" in all variations names "slot 0 (path selector)" — dependency chain complete by slot reference.

| Variation | Slot 0 in contract? | Slot 5 "Required by" uses slot reference? | C-34 verdict |
|-----------|--------------------|--------------------------------------------|-------------|
| **V-01** | YES (FOCUS-STATE, `{active}` or `{inactive}`) | "Requires slot 0 (path selector); active also requires slot 4 (SOURCE) and slot 1 (INERTIA-REF)" | **PASS** |
| **V-02** | YES (inherited) | "Requires slot 0 (path selector); active also requires slot 4 and slot 1" | **PASS** |
| **V-03** | YES (inherited) | "Requires slot 0 (path selector); active also requires slot 4 and slot 1" | **PASS** |
| **V-04** | YES (inherited) | "Requires slot 0 (path and format selector); active also requires slot 4 and slot 1" | **PASS** |
| **V-05** | YES (inherited) | "Requires slot 0 (path and format selector); active also requires slot 4 and slot 1" | **PASS** |

**C-34: PASS / 5 pts — all variations** (R11 PARTIAL gap closed by C-43)

---

#### C-35 through C-43 — Uniform PASS (all variations)

| ID | Criterion | Evidence summary | Verdict (all) |
|----|-----------|-----------------|---------------|
| C-35 | Syntactic format template for cross-dim proof slot | Slot 5: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` — pipe-delimited, parse-ready | PASS |
| C-36 | Cross-dim proof as structural PASS/FAIL table | Phase 4 has SOURCE / REDUCTION-1 / REDUCTION-2 / THEREFORE rows with Required value and Failure state. V-02/V-04/V-05 add PATH as row 0 (SOURCE still structurally positioned by table; C-36 pass condition requires "at least four rows -- SOURCE, REDUCTION-1, REDUCTION-2, THEREFORE" — all present) | PASS |
| C-37 | WHITESPACE validation as CANDIDATE-first PASS/FAIL table | Phase 3: CANDIDATE → ABSENCE-EVIDENCE → GAP-CONFIRMED → vs-INERTIA-REF; CANDIDATE is first row by table position; each row has Required value and Failure state | PASS |
| C-38 | AMEND as structured table with Slots re-filled and Gates re-run | All AMEND tables have "Slots re-filled" and "Gates re-run" columns; focus-shift row names GATE 0 + GATE 3 in "Gates re-run"; proof rerun explicitly required | PASS |
| C-39 | EXECUTION DEPENDENCY table in PREFLIGHT | Present in all variations; GATE 4 listed as root step (None (root)); GATE 0 as pre-DAG step; step-level ordering machine-readable | PASS |
| C-40 | FOCUS GATE as named PASS/FAIL gate in PREFLIGHT | GATE 0 is named subsection within PREFLIGHT with 4-row PASS/FAIL table (Focus value detected / Write FOCUS-STATE / Focus-active branch / Focus-inactive branch) | PASS |
| C-41 | Phase 3 vs-INERTIA-REF uses slot 6 ternary-token format | Phase 3 vs-INERTIA-REF requires `vs. INERTIA-REF -- {reinforces / challenges / contextualizes}: {mechanism phrase from slot 1}` — same ternary format as slot 6; prose fails | PASS |
| C-42 | EXECUTION DEPENDENCY includes explicit Prerequisite steps column | "Prerequisite steps" column present; GATE 4 = "None (root)" by declaration; GATE 0 = "-- (pre-DAG)" by declaration; all steps name upstream steps | PASS |
| C-43 | FOCUS-STATE declared as named output contract slot | Slot 0 = FOCUS-STATE with format template `{active: {focus_dimension}}` or `{inactive}` in OUTPUT CONTRACTS table; fills slot 0 at GATE 0 Write row; downstream slots name "Requires slot 0" | PASS |

All C-35–C-43: **PASS / 5 pts — all five variations**

---

## Composite Scores

| Criterion range | Points each | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------------|------------|------|------|------|------|------|
| C-01–C-05 (Essential) | ~12 | 60 | 60 | 60 | 60 | 60 |
| C-06–C-08 (Recommended) | 10 | 30 | 30 | 30 | 30 | 30 |
| C-09–C-33 (Aspirational) | 5 | 125 | 125 | 125 | 125 | 125 |
| **C-34** | 5 | **5** | **5** | **5** | **5** | **5** |
| C-35–C-43 (Aspirational) | 5 | 45 | 45 | 45 | 45 | 45 |
| **TOTAL** | | **265** | **265** | **265** | **265** | **265** |
| **Grade** | | **Exceptional** | **Exceptional** | **Exceptional** | **Exceptional** | **Exceptional** |

All five variations tie at 265/265. R11's C-34 differentiator (slot 0 existence) is closed — C-43 is now rubric and all R12 variations carry slot 0.

---

## Ranking

| Rank | Variation | Score | Rubric advantage | Candidate criteria present |
|------|-----------|-------|-----------------|---------------------------|
| **1** | **V-05** | **265** | All C-09–C-43 PASS | C-44 + C-45 + C-46 (maximum) |
| **2** | **V-04** | **265** | All C-09–C-43 PASS | C-44 + C-45 |
| **3** | **V-01** | **265** | All C-09–C-43 PASS | C-44 |
| **4** | **V-02** | **265** | All C-09–C-43 PASS | C-45 |
| **5** | **V-03** | **265** | All C-09–C-43 PASS | C-46 |

Rubric scores are identical. V-05 leads on candidate criterion coverage with all three R12 innovations. Tie-breaking within V-01/V-02/V-03 (single candidate criterion each) is alphabetical; no rubric basis to rank them against each other.

**Candidate criteria satisfied per variation:**

| Candidate criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------|------|------|------|------|------|
| C-44 (Phase 2 Reads slot declares slot 0) | YES | NO | NO | YES | YES |
| C-45 (Phase 4 PATH row as row 0) | NO | YES | NO | YES | YES |
| C-46 (WRITE-TOKEN REGISTRY in PREFLIGHT) | NO | NO | YES | NO | YES |

---

## Excellence Signals — V-05

**1. Exhaustive "Reads slot" declaration including conditional reads (→ C-44)**

The EXECUTION DEPENDENCY "Reads slot" column is the primary mechanism for expressing data-flow edges. Phase 2 branches on slot 0 (FOCUS-STATE) to determine Focus column inclusion — a real conditional read — but R11 V-05 listed only slot 1 in Phase 2's "Reads slot" cell. V-01/V-04/V-05 add `0 -- FOCUS-STATE (Focus column inclusion)` alongside `1 -- INERTIA-REF`. The rule extracted: every step that conditionally branches on a slot value must declare that slot in its "Reads slot" column. An omission is an **execution dependency gap** that makes the data-flow graph incomplete by column inspection alone. V-05 codifies this as a named failure state in the EXECUTION DEPENDENCY header.

**2. Phase 4 PATH row extends declaration-before-execution to proof table (→ C-45)**

C-37 established CANDIDATE-first ordering for Phase 3: declaration before evidence prevents selective assembly. V-02/V-04/V-05 apply the same principle to Phase 4: the active/inactive branch decision (PATH) becomes table row 0, before SOURCE. Previously, Phase 4's branching logic lived in the phase header prose — a reader had to leave the table to determine which path applied. PATH row makes both branches (active: proceed to SOURCE; inactive: write `VACUOUS-5: focus-inactive` and exit) independently reviewable table-level checkpoints. The inactive path now exits at row 0 rather than the THEREFORE row, making clear that SOURCE is not required when slot 0 = inactive. C-45 extends C-37's structural principle from whitespace validation to proof construction.

**3. WRITE-TOKEN REGISTRY as first-class PREFLIGHT table (→ C-46)**

V-03/V-05 add a WRITE-TOKEN REGISTRY table to PREFLIGHT (after OUTPUT CONTRACTS, before GATE 0) indexing all write-token gate events by gate name, token written, slot, and pre-DAG/DAG classification. Previously the write-token schedule required scanning EXECUTION DEPENDENCY "Writes slot" for named slots — an O(N) scan. The registry makes the schedule O(1)-discoverable from a single dedicated table, structurally parallel to OUTPUT CONTRACTS (slot inventory) and EXECUTION DEPENDENCY (step ordering). The three tables together cover the three facets of execution specification: output targets, step ordering, and write-event schedule. V-05 encodes slot 0's complete lifecycle in five independent structural positions: OUTPUT CONTRACTS "Required by" (all consumers named), WRITE-TOKEN REGISTRY row 1 (write event indexed), EXECUTION DEPENDENCY Phase 2 "Reads slot" (conditional read declared), EXECUTION DEPENDENCY Phase 4 PATH row (branch routing step), Phase 4 table row 0 (in-table checkpoint).

---

```json
{"top_score": 265, "all_essential_pass": true, "new_patterns": ["Exhaustive Reads slot declaration including conditional reads: Phase 2 conditionally branches on slot 0 (FOCUS-STATE) for Focus column inclusion but R11 V-05 omitted slot 0 from Phase 2's Reads slot cell -- V-01/V-04/V-05 add slot 0 as a declared conditional read, closing the execution dependency gap and making the full data-flow graph reconstructable by column inspection without reading phase prose", "Phase 4 PATH row as structural branch router at row 0: V-02/V-04/V-05 add a PATH row before SOURCE that reads slot 0 and declares both execution branches as independently reviewable table checkpoints (active: proceed to SOURCE; inactive: write VACUOUS-5: focus-inactive and exit) -- extends C-37 declaration-before-execution principle from Phase 3 whitespace validation to Phase 4 proof construction", "WRITE-TOKEN REGISTRY as first-class PREFLIGHT table: V-03/V-05 add a dedicated WRITE-TOKEN REGISTRY table (after OUTPUT CONTRACTS, before GATE 0) indexing all write-token gate events by gate name, token, slot, and pre-DAG/DAG classification -- makes the write-token schedule O(1)-discoverable without scanning EXECUTION DEPENDENCY, completing the three-table PREFLIGHT specification: OUTPUT CONTRACTS (slot inventory) + EXECUTION DEPENDENCY (step ordering) + WRITE-TOKEN REGISTRY (write-event schedule)"]}
```
