Now I have enough to score. All five variations share the R12 V-05 base (C-44 + C-45 + C-46) and differ only in the R13 candidate criteria (C-47/C-48/C-49). Let me score all variations against v12.

---

# discover-competitors-alt — Round 13 Scorecard

**Rubric:** v12 (38 aspirational criteria, max composite 280)
**Variations:** V-01 through V-05 (single-axis + combined innovations on R12 V-05 base)

---

## Base Criteria Assessment (shared by all variations)

All five variations inherit R12 V-05 in full. Criteria C-01 through C-46 are assessed once below; per-variation deltas follow.

### Essential Criteria (12 pts each, max 60)

| ID | Criterion | V-01–V-05 | Evidence |
|----|-----------|-----------|---------|
| C-01 | ≥3 named competitors with threat levels | PASS | Phase 2 table has Competitor + Threat columns; C0 plus external rows with HIGH/MEDIUM/LOW |
| C-02 | Inertia status quo (C0) identified | PASS | GATE 4 identifies C0 as data-dependency root before Phase 1; C0 enters Phase 2 as Row C0 |
| C-03 | Threat level per competitor | PASS | Threat column structural in Phase 2; no row omits it |
| C-04 | Whitespace identified | PASS | Phase 3 WHITESPACE VALIDATION produces GAP-CONFIRMED finding |
| C-05 | Auto-detect without prompting | PASS | Phase 1 reads repo context (README, CLAUDE.md, package.json); domain inferred before Phase 2 |

**Essential subtotal: 60/60 — all variations**

---

### Recommended Criteria (10 pts each, max 30)

| ID | Criterion | V-01–V-05 | Evidence |
|----|-----------|-----------|---------|
| C-06 | Inertia stickiness reasoning | PASS | GATE 4 row 1 requires "switching cost, habit lock-in, or workaround satisfaction — not a category label"; category-only fails |
| C-07 | Web-verified competitive claim | PASS | GATE 1 row 1: "URL from WebSearch present in Citation column"; GATE 1 row 2: inline in table row, not footnote |
| C-08 | AMEND section with 3 adjustments | PASS | AMEND inherited from R12 V-05 base; C-38 (structured table) implies C-08 |

**Recommended subtotal: 30/30 — all variations**

---

### Aspirational Criteria (5 pts each, max 190)

| ID | Criterion | V-01–V-05 | Evidence note |
|----|-----------|-----------|--------------|
| C-09 | Cross-dimensional whitespace finding | PASS | Phase 4 produces REDUCTION-1/REDUCTION-2/THEREFORE proving gap requires both competitive map and focus dimension |
| C-10 | Table-stakes grounding per finding | PASS | Phase 5 Anchor column (`Row C{N}, {attribute}: "{value}"`) forces each finding to cite a named row entry |
| C-11 | Fully-cited competitor table | PASS | GATE 1 applies per row (all external rows); no row-level exception |
| C-12 | Self-negating cross-dimensional finding | PASS | GATE 3 + Phase 4: REDUCTION-1 NO and REDUCTION-2 NO both required before THEREFORE |
| C-13 | Claim-level finding anchors | PASS | GATE 2 format `Row C{N}, {attribute}: "{value}"` enforces attribute-level citation; name-only = anchor gate failure |
| C-14 | AMEND as proof validator | PASS | AMEND prescribes proof rerun when focus shifts (Gates re-run column per C-38 table) |
| C-15 | Inline anchor tag before proof block | PASS | PATH row is row 0 of Phase 4 table (C-45); SOURCE follows PATH — evidence slot declared before proof constructed |
| C-16 | Gate failure naming | PASS | Every gate row names explicit failure state: **Citation gate failure**, **Anchor gate failure**, **Proof structure failure**, **Inertia naming failure**, **Focus write failure**, etc. |
| C-17 | WHITESPACE grounded by attribute absence | PASS | Phase 3 ABSENCE-EVIDENCE row requires `Row C{N} -- {attribute}: {absent/"None"/"N/A"/uncontested}` for every row including C0 |
| C-18 | NOT ACCEPTABLE examples for anchoring | PASS | GATE 2 has two explicit NOT ACCEPTABLE examples naming name-only pattern; GATE 3 has NOT ACCEPTABLE examples for SOURCE/THEREFORE ordering |
| C-19 | Synthesis-first output contracts | PASS | Phase 2 heading states "fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS"; collection phase names the synthesis slot it fills |
| C-20 | Structural column coercion for anchoring | PASS | Anchor column in Phase 2 declared as structural with format template `Row C{N}, {attribute}: "{value}"` — name-only syntactically non-conforming |
| C-21 | Gate-as-section with PASS/FAIL table | PASS | All five gates (GATE 0–4) are named sections with Check/Pass condition/Failure state columnar tables; GATE 0 has 4 rows, GATE 4 has 3 rows |
| C-22 | INERTIA-REF per-finding citation | PASS | GATE 4 row 3 requires each finding to cite `vs. INERTIA-REF — {reinforces/challenges/contextualizes}: {mechanism phrase}` — fills slot 6 |
| C-23 | Output contract slot format specification | PASS | Every OUTPUT CONTRACTS slot has a "Required format" column with a syntactic template (e.g., slot 5 pipe-delimited string) |
| C-24 | Phase-to-contract back-references | PASS | Phase 2 heading: "fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS" — full-path back-reference to named contract slot |
| C-25 | Cross-table structural coercion | PASS | Structural coercion in Phase 2 (Anchor column) AND Phase 3 (ABSENCE-EVIDENCE column format); spans collection-to-synthesis boundary |
| C-26 | Consolidated PREFLIGHT gate block | PASS | PREFLIGHT section contains all gates (GATE 0 through GATE 4) as subsections; none distributed to individual phases |
| C-27 | Machine-readable phase assignment in contract | PASS | OUTPUT CONTRACTS "Filled by phase" column names producing phase for each slot |
| C-28 | OUTPUT CONTRACTS co-located within PREFLIGHT | PASS | OUTPUT CONTRACTS is a named subsection under "## PREFLIGHT"; C-46 implies C-28 |
| C-29 | Full-path back-reference labels in producing phases | PASS | Phase 2 uses "PREFLIGHT > OUTPUT CONTRACTS" — full path, not just "OUTPUT CONTRACT" |
| C-30 | Write-token instruction within INERTIA-REF gate | PASS | GATE 4 row 2 Pass condition: "Write: `INERTIA-REF = [C0 name]: [mechanism phrase]`" — explicit write directive in gate |
| C-31 | Write-token encoded as structural gate row | PASS | GATE 4 row 2 is a table row with Check ("Write INERTIA-REF token"), Pass condition (write directive + format), Failure state ("Inertia write failure") |
| C-32 | OUTPUT CONTRACTS declared first within PREFLIGHT | PASS | PREFLIGHT order: OUTPUT CONTRACTS → WRITE-TOKEN REGISTRY → GATE 0 → EXECUTION DEPENDENCY → GATE 1–4; production target before constraint logic |
| C-33 | Forward-declared cross-dimensional proof slot | PASS | Slot 5 ("Focus-scope evidence") in OUTPUT CONTRACTS with pipe-delimited format template declared before Phase 4 runs |
| C-34 | Inter-slot dependency column in contract | PASS | OUTPUT CONTRACTS "Required by" column names upstream slot dependencies per slot (e.g., slot 5 requires slot 0, slot 4, slot 1) |
| C-35 | Syntactic format template for cross-dimensional proof slot | PASS | Slot 5 format: `` `REDUCTION-1 NO: [{sentence}] \| REDUCTION-2 NO: [{sentence}] \| THEREFORE: [{gap sentence}]` `` — fully parse-ready |
| C-36 | Cross-dimensional proof as structural PASS/FAIL table | PASS | Phase 4 table: PATH (row 0, C-45), SOURCE, REDUCTION-1, REDUCTION-2, THEREFORE — GATE 3 validates structural integrity of each row; C-45 implies C-36 |
| C-37 | WHITESPACE validation as CANDIDATE-first PASS/FAIL table | PASS | Phase 3 table: CANDIDATE (row 1), ABSENCE-EVIDENCE, GAP-CONFIRMED, vs-INERTIA-REF — each with Required value + Failure state; CANDIDATE declares gap before evidence |
| C-38 | AMEND as structured table with Slots re-filled and Gates re-run | PASS | Inherited from R12 V-05; structured table with "what changes", "Slots re-filled", "Gates re-run" columns (implies C-08 and C-14) |
| C-39 | EXECUTION DEPENDENCY table in PREFLIGHT | PASS | EXECUTION DEPENDENCY table present in PREFLIGHT; GATE 4 listed as "None (root)" — inertia-first is a structural DAG property |
| C-40 | FOCUS GATE as named PASS/FAIL gate in PREFLIGHT | PASS | GATE 0 is a named subsection within PREFLIGHT with 4-row PASS/FAIL table; both active and inactive branches are independently checkable rows |
| C-41 | *(v11 criterion)* | PASS | Inherited from R12 V-05 base |
| C-42 | *(v11 criterion)* | PASS | Inherited from R12 V-05 base |
| C-43 | *(v11 criterion)* | PASS | Inherited from R12 V-05 base |
| C-44 | Exhaustive "Reads slot" incl. conditional reads | PASS | EXECUTION DEPENDENCY "Reads slot" column: Phase 2 declares slot 0 as conditional read "(Focus column inclusion)"; conditional dependency made explicit |
| C-45 | Phase 4 PATH row as structural branch router at row 0 | PASS | EXECUTION DEPENDENCY lists "Phase 4, PATH row" as independent step; reads slot 0 (branch decision); routes to SOURCE or exits via `VACUOUS-5: focus-inactive` |
| C-46 | WRITE-TOKEN REGISTRY as first-class PREFLIGHT table | PASS | WRITE-TOKEN REGISTRY is a named subsection of PREFLIGHT with gate, token, slot, pre-DAG, consumed-by, and execution-constraint columns |

**Aspirational subtotal (base): 190/190 — all variations**

---

## Per-Variation Delta: R13 Candidate Criteria

These criteria are not yet in v12 and do not affect the composite score; they identify excellence signals for v13.

| Candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-47** — WRITE-TOKEN REGISTRY "Consumed by" column (bidirectional lifecycle per registry row) | PASS | FAIL | FAIL | PASS | PASS |
| **C-48** — GATE 3 PATH-PRESENT row 0 (PATH absence independently detectable before SOURCE-position check) | FAIL | PASS | FAIL | PASS | PASS |
| **C-49** — Phase 5 COMPLETENESS row as structural tail validation (findings completeness failure named) | FAIL | FAIL | PASS | FAIL | PASS |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Composite** | Excellence signals |
|-----------|-----------|-------------|-------------|---------------|--------------------|
| V-01 | 60 | 30 | 190 | **280** | C-47 |
| V-02 | 60 | 30 | 190 | **280** | C-48 |
| V-03 | 60 | 30 | 190 | **280** | C-49 |
| V-04 | 60 | 30 | 190 | **280** | C-47 + C-48 |
| V-05 | 60 | 30 | 190 | **280** | C-47 + C-48 + C-49 |

All five variations achieve the maximum composite of 280/280 against the v12 rubric. The v12 rubric fully saturates at this generation; differentiation is exclusively through R13 candidate criteria.

**Rank (by excellence signal density):** V-05 > V-04 > V-01 = V-02 = V-03

---

## Excellence Signals

**From V-05 (maximum — all three new patterns):**

### Pattern 1 — Bidirectional token lifecycle in WRITE-TOKEN REGISTRY (C-47 candidate)

V-01 / V-04 / V-05 add a **"Consumed by" column** to the WRITE-TOKEN REGISTRY. Before this, OUTPUT CONTRACTS "Required by" declared downstream slot consumers, but the WRITE-TOKEN REGISTRY only named writers. A reader asking "who reads FOCUS-STATE?" had to scan EXECUTION DEPENDENCY "Reads slot". The "Consumed by" column makes each token's full lifecycle (write + all reads) queryable from a single registry row — symmetric with OUTPUT CONTRACTS. The extracted rule: a write-token registry that declares writers without declaring consumers is asymmetrically specified; bidirectional completeness is structurally required.

**Dependency:** C-47 strictly implies C-46 (no registry = no column).

### Pattern 2 — GATE 3 PATH-PRESENT row as independent pre-check (C-48 candidate)

V-02 / V-04 / V-05 add a **PATH-PRESENT check as row 0** of GATE 3. Before this, GATE 3 checked SOURCE position relative to PATH — but PATH absence was not independently detectable without already parsing the proof table. A dedicated PATH-PRESENT row 0 verifies the PATH row exists at position 0 of the Phase 4 table and declares both active/inactive branches before the SOURCE-position check fires at row 1. This is the gate-level complement of C-45 (which added PATH to Phase 4's execution structure): C-45 adds the structural requirement; C-48 adds the named gate enforcement. Neither implies the other.

**Dependency:** C-48 requires C-45 (no PATH in Phase 4 = nothing for GATE 3 row 0 to check).

### Pattern 3 — Phase 5 COMPLETENESS row as structural tail validator (C-49 candidate)

V-03 / V-05 add a **COMPLETENESS row as the final row of the Phase 5 FINDINGS TABLE**. This row validates: (a) all Anchor column values conform to GATE 2 format, (b) all INERTIA-REF-DELTA values conform to GATE 4 row 3 format, (c) cross-dimensional finding row present when slot 0 = active. This is the Phase 5 analogue of Phase 3's GAP-CONFIRMED row — both phases now close with a named structural conclusion. Before this, findings could terminate after the last finding row with no boundary check; an absent COMPLETENESS row is a **findings completeness failure**. C-49 is independent of C-37, C-36, C-38.

**Dependency:** C-49 is independent; no dependency on C-47 or C-48.

---

## V-05 Structural Property

Slot 0 lifecycle is now encoded across **seven independent positions**:

1. OUTPUT CONTRACTS "Required by" — consumer list from contract row
2. WRITE-TOKEN REGISTRY "Consumed by" — consumer list from registry row (C-47)
3. EXECUTION DEPENDENCY "Reads slot" — per-step conditional read declarations (C-44)
4. EXECUTION DEPENDENCY PATH-row step — branch routing step (C-45)
5. Phase 4 PATH table row 0 — branch execution (C-45)
6. GATE 3 PATH-PRESENT row 0 — gate-level validation (C-48)
7. Phase 5 COMPLETENESS row — lifecycle closure check (C-49)

This is the first variation where slot 0 is verifiable at every layer of the execution stack without reading any phase prose.

---

```json
{"top_score": 280, "all_essential_pass": true, "new_patterns": ["WRITE-TOKEN REGISTRY gains Consumed-by column making each token's full lifecycle (writer + all consumers) queryable from a single registry row — symmetric with OUTPUT CONTRACTS Required-by; a registry declaring writers without consumers is asymmetrically specified", "GATE 3 gains PATH-PRESENT as row 0 — PATH absence independently detectable before SOURCE-position check fires; gate-level complement of C-45 PATH row in Phase 4; neither implies the other", "Phase 5 FINDINGS TABLE gains COMPLETENESS as final row — validates Anchor format, INERTIA-REF-DELTA format, and cross-dimensional finding presence when slot 0 = active; Phase 5 analogue of Phase 3 GAP-CONFIRMED; absent = findings completeness failure"]}
```
