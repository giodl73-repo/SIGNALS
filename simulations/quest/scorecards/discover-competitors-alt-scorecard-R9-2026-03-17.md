# discover-competitors-alt — Round 9 Scorecard

**All 5 variations: 230/230 — Exceptional**

## Summary

Every criterion C-01 through C-36 passes for all 5 variations. The rubric v8 ceiling is saturated.

Key evidence points:
- **C-01**: GATE 4 executes before Phase 1 in all variations
- **C-31**: Write-token as structural gate row — "Inertia write failure" independently reviewable
- **C-32**: OUTPUT CONTRACTS is first subsection in PREFLIGHT in all variations (V-03/V-05 insert EXECUTION DEPENDENCY between OUTPUT CONTRACTS and GATE 1, but OUTPUT CONTRACTS remains first)
- **C-34/C-35/C-36**: Universal baseline — all variations have "Required by" column, pipe-delimited slot 5 template, and 4-row Phase 4 proof table

## Differential — Candidate New Criteria (R9 Axes)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-37** WHITESPACE as 4-row PASS/FAIL table | PASS | FAIL | FAIL | PASS | PASS |
| **C-38** AMEND as structured table | FAIL | PASS | FAIL | PASS | PASS |
| **C-39** EXECUTION DEPENDENCY table | FAIL | FAIL | PASS | FAIL | PASS |

V-05 is the only variation covering all three. Rankings: V-05 > V-04 > V-01 = V-02 = V-03.

## Excellence Signals (3 new patterns)

1. **WHITESPACE-VALIDATION table (C-37)** — CANDIDATE-first by row order is to Phase 3 what SOURCE-first is to Phase 4 (C-36). Structural position enforces declaration-before-evidence without instruction.

2. **AMEND as machine-readable contract (C-38)** — "Slots re-filled" and "Gates re-run" columns make C-08/C-14 obligations verifiable at table-scan time; C-35 format constraint propagates into the amendment lifecycle.

3. **EXECUTION DEPENDENCY table (C-39)** — step-level DAG in PREFLIGHT complements C-34's slot-level "Required by" column. GATE 4 as root step makes inertia-first a structural DAG property, not a prose convention.

---

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": ["WHITESPACE phase as 4-row PASS/FAIL table — CANDIDATE declared first by table row order enforces evidence-after-declaration, applying C-36's structural isomorphism principle to Phase 3 and closing the selective-evidence loophole that prose-ordered whitespace allows", "AMEND as 6-column structured table (Adjustment / What user changes / What changes in output / Slots re-filled / Gates re-run) makes C-08 and C-14 obligations verifiable by column inspection at the same structural level as OUTPUT CONTRACTS — prose enforcement eliminated from the amendment boundary", "EXECUTION DEPENDENCY table in PREFLIGHT provides step-level DAG complementing C-34's slot-level Required-by column — PREFLIGHT becomes a full execution specification: slot targets, inter-slot dependencies, step ordering, and gate constraints all readable before Phase 1"]}
```
| V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-09 | Cross-dimensional whitespace finding | PASS | PASS | PASS | PASS | PASS | Phase 4 proof table requires both competitive map and focus dimension; REDUCTION-1/REDUCTION-2 structure forces cross-dimensional necessity |
| C-10 | Table-stakes grounding per finding | PASS | PASS | PASS | PASS | PASS | Phase 5 Anchor column `Row C{N}, {attribute}: "{value}"` structurally prevents free-floating prose; NOT ACCEPTABLE examples remove escape hatch |
| C-11 | Fully-cited competitor table | PASS | PASS | PASS | PASS | PASS | GATE 1 applied per row; Phase 2 requires WebSearch per external competitor before row output |
| C-12 | Self-negating cross-dimensional finding | PASS | PASS | PASS | PASS | PASS | Phase 4: REDUCTION-1 "what is lost if the focus dimension is dropped"; REDUCTION-2 "what is lost if the competitive map is dropped" — both single-dimension reductions required |
| C-13 | Claim-level finding anchors | PASS | PASS | PASS | PASS | PASS | Anchor format `Row C{N}, {attribute}: "{value}"` requires row + attribute + quoted value; NOT ACCEPTABLE: "Competitor 2 reveals that..." |
| C-14 | AMEND as proof validator | PASS | PASS | PASS | PASS | PASS | V-01/03 prose: "Rewrite REDUCTION-1 and REDUCTION-2 from scratch...Writing only a new THEREFORE without rerunning both reductions is a **proof rerun failure**". V-02/04/05 table: "Gates re-run" column explicitly names GATE 3 with proof rerun failure warning |
| C-15 | Inline anchor tag before proof block | PASS | PASS | PASS | PASS | PASS | SOURCE row is first row of Phase 4 table; C-36 implies C-15 |
| C-16 | Gate failure naming | PASS | PASS | PASS | PASS | PASS | Named failure states present in all gates: Citation gate failure, Anchor gate failure, Whitespace gate failure, Proof structure failure, Whitespace naming failure, Whitespace INERTIA-REF failure, Inertia naming failure, Inertia write failure, Inertia citation failure |
| C-17 | WHITESPACE grounded by attribute absence | PASS | PASS | PASS | PASS | PASS | V-01/04/05: ABSENCE-EVIDENCE row requires `Row C{N} — {attribute}: {absent/None/N/A/uncontested}` per row. V-02/03: same format in code block before GAP-CONFIRMED. All require attribute-level per-row absence evidence |
| C-18 | NOT ACCEPTABLE examples for anchoring | PASS | PASS | PASS | PASS | PASS | All variations: NOT ACCEPTABLE "Competitor 2 reveals that..." and "As Competitor 1 demonstrates..." — name-only failure pattern explicitly named |
| C-19 | Synthesis-first output contracts | PASS | PASS | PASS | PASS | PASS | Phase 2: "(fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS)"; Phase 3: "(fills slot 3 — Absence evidence block, PREFLIGHT > OUTPUT CONTRACTS)" |
| C-20 | Structural column coercion for anchoring | PASS | PASS | PASS | PASS | PASS | Phase 2 Anchor column: "a cell containing only a competitor name is syntactically malformed and must be rewritten" — format shape makes name-only entries non-conforming without rule evaluation |
| C-21 | Gate-as-section with PASS/FAIL table | PASS | PASS | PASS | PASS | PASS | All four gates are named subsections with 3-column tables (Check / Pass condition / Failure state), each with ≥2 rows |
| C-22 | INERTIA-REF per-finding citation | PASS | PASS | PASS | PASS | PASS | GATE 4 defines INERTIA-REF token; Phase 5 INERTIA-REF-DELTA column enforces per-finding citation (C-31 implies C-22) |
| C-23 | Output contract slot format specification | PASS | PASS | PASS | PASS | PASS | All 6 slots in OUTPUT CONTRACTS specify both label and required structural format template |
| C-24 | Phase-to-contract back-references | PASS | PASS | PASS | PASS | PASS | Phase headings: "(fills slot N — [label], PREFLIGHT > OUTPUT CONTRACTS)" in all producing phases |
| C-25 | Cross-table structural coercion | PASS | PASS | PASS | PASS | PASS | Anchor column format enforced independently in Phase 2 (competitor table) and Phase 5 (findings table) — coercion spans collection-to-synthesis boundary |
| C-26 | Consolidated PREFLIGHT gate block | PASS | PASS | PASS | PASS | PASS | All 4 gates within PREFLIGHT (satisfied via C-28) |
| C-27 | Machine-readable phase assignment in output contract | PASS | PASS | PASS | PASS | PASS | OUTPUT CONTRACTS "Filled by phase" column names producing phase for every slot |
| C-28 | OUTPUT CONTRACTS co-located within PREFLIGHT | PASS | PASS | PASS | PASS | PASS | OUTPUT CONTRACTS is a named subsection within PREFLIGHT in all variations |
| C-29 | Full-path back-reference labels in producing phases | PASS | PASS | PASS | PASS | PASS | All phase headings use "PREFLIGHT > OUTPUT CONTRACTS" as the navigable path; C-28 satisfied so path prefix is required and present |
| C-30 | Write-token instruction within INERTIA-REF gate | PASS | PASS | PASS | PASS | PASS | GATE 4 "Write INERTIA-REF token" row: "Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]`" — write bound to gate execution (C-31 implies C-30) |
| C-31 | Write-token encoded as structural gate row | PASS | PASS | PASS | PASS | PASS | GATE 4 write instruction is a dedicated table row: Check "Write INERTIA-REF token", Pass condition with write directive and token format, Failure state "Inertia write failure" — independently reviewable checkpoint |
| C-32 | OUTPUT CONTRACTS declared first within PREFLIGHT | PASS | PASS | PASS | PASS | PASS | OUTPUT CONTRACTS is the first subsection in PREFLIGHT in all variations (before EXECUTION DEPENDENCY in V-03/V-05, before GATE 1 in all) |
| C-33 | Forward-declared cross-dimensional proof slot in output contract | PASS | PASS | PASS | PASS | PASS | Slot 5 "Focus-scope evidence" in OUTPUT CONTRACTS declares the cross-dimensional proof requirement with format template before Phase 4 runs (C-35 implies C-33) |
| C-34 | Inter-slot dependency column in output contract | PASS | PASS | PASS | PASS | PASS | "Required by" column populated for all 6 slots: slot 1 = "Root — no upstream dependency; slots 5 and 6 require this token"; downstream slot dependencies named per slot |
| C-35 | Syntactic format template for cross-dimensional proof slot | PASS | PASS | PASS | PASS | PASS | Slot 5 format: `REDUCTION-1 NO: [{...}] \| REDUCTION-2 NO: [{...}] \| THEREFORE: [{...}]` — pipe-delimited parse-ready template in all variations |
| C-36 | Cross-dimensional proof encoded as structural PASS/FAIL table | PASS | PASS | PASS | PASS | PASS | Phase 4 is a 4-row table (SOURCE / REDUCTION-1 / REDUCTION-2 / THEREFORE) with Required value and Failure state per row; SOURCE position enforced by table structure (first row) |

**Aspirational subtotal: 140/140 all variations**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | Grade |
|-----------|-----------|-------------|--------------|-----------|-------|
| V-01 | 60/60 | 30/30 | 140/140 | **230/230** | Exceptional |
| V-02 | 60/60 | 30/30 | 140/140 | **230/230** | Exceptional |
| V-03 | 60/60 | 30/30 | 140/140 | **230/230** | Exceptional |
| V-04 | 60/60 | 30/30 | 140/140 | **230/230** | Exceptional |
| V-05 | 60/60 | 30/30 | 140/140 | **230/230** | Exceptional |

All variations achieve maximum score. Grade band: Exceptional ≥ 216.

---

## Differential Analysis — Candidate New Criteria (R9 Axes)

Rubric v8 criteria are fully satisfied by all variations. The R9 axes expose three candidate criteria not yet formally scored:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-37**: WHITESPACE phase as 4-row PASS/FAIL table (CANDIDATE first by row order — C-36 applied to Phase 3) | PASS | FAIL | FAIL | PASS | PASS |
| **C-38**: AMEND as structured table with Slots re-filled and Gates re-run as queryable columns | FAIL | PASS | FAIL | PASS | PASS |
| **C-39**: EXECUTION DEPENDENCY table in PREFLIGHT — step-level DAG complementing C-34's slot-level Required-by column | FAIL | FAIL | PASS | FAIL | PASS |

V-05 is the only variation satisfying all three candidate criteria.

---

## Excellence Signals

The three R9 axes each apply an existing structural principle to a domain that previously relied on prose enforcement:

**Pattern 1 — C-37 (V-01 axis): Structural isomorphism between Phase 3 and Phase 4**
C-36 restructured Phase 4 from a prose-ordered code block into a 4-row PASS/FAIL table, enforcing SOURCE-first by table row position. V-01 applies the same pattern to Phase 3: CANDIDATE must be the first row of the WHITESPACE VALIDATION table, making evidence-before-candidate structurally malformed without rule evaluation. GAP-CONFIRMED cannot be reached without ABSENCE-EVIDENCE for all rows — the table enforces this by row order, not instruction. The vs-INERTIA-REF row as the mandatory final row closes the Phase 3 INERTIA-REF disconnection failure: whitespace cannot be confirmed without naming the C0 relationship. CANDIDATE-first is to Phase 3 what SOURCE-first is to Phase 4.

**Pattern 2 — C-38 (V-02 axis): AMEND elevated to machine-readable contract level**
OUTPUT CONTRACTS is already a structured table with phase-assignment and Required-by columns. AMEND was the one remaining prose boundary. V-02's 6-column table makes C-08 and C-14 obligations verifiable by column inspection: a reviewer confirms that slot 5 appears in "Slots re-filled" for the focus-shift row (C-08) and GATE 3 appears in "Gates re-run" with proof-rerun failure warning (C-14) — without reading prose. The "slot 5 re-filled only when all three components conform to the pipe-delimited format template" condition in the table cell makes the C-35 format constraint active at amendment time. The AMEND table operates at the same structural level as OUTPUT CONTRACTS, completing the machine-readable contract coverage from data collection through synthesis through amendment.

**Pattern 3 — C-39 (V-03 axis): PREFLIGHT elevated from checklist to full execution specification**
C-34's "Required by" column makes slot-to-slot dependencies queryable at contract time. The EXECUTION DEPENDENCY table makes step-to-step ordering queryable at the same point. These are orthogonal views: OUTPUT CONTRACTS names what is produced and what each slot depends on; EXECUTION DEPENDENCY names when each step runs and what each step reads before writing. Together, PREFLIGHT exposes the complete execution contract before Phase 1. GATE 4 as the root step (no Reads slot) makes the inertia-first design principle architecturally visible: the DAG has a root, and the root is C0 stickiness resolution. This elevates the inertia-first convention from a prose instruction to a structural property of the dependency graph.

**V-05 combined effect:** Every non-trivial production step has machine-checkable output structure (Phase 3 WHITESPACE table, Phase 4 proof table) and every amendment has machine-readable side effects (AMEND table). PREFLIGHT exposes slot targets, inter-slot dependencies, step ordering, and gate constraints before Phase 1. Prose enforcement is eliminated from all consequential decision points.

---

## Rankings

All 5 variations tied at 230/230 on rubric v8. Ranked by candidate new criteria coverage:

| Rank | Variation | New criteria satisfied | Score |
|------|-----------|----------------------|-------|
| 1 | V-05 | C-37 + C-38 + C-39 | 230/230 |
| 2 | V-04 | C-37 + C-38 | 230/230 |
| 3 | V-01 | C-37 | 230/230 |
| 3 | V-02 | C-38 | 230/230 |
| 3 | V-03 | C-39 | 230/230 |

---

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": ["WHITESPACE phase as 4-row PASS/FAIL table — CANDIDATE declared first by table row order enforces evidence-after-declaration, applying C-36's structural isomorphism principle to Phase 3 and closing the selective-evidence loophole that prose-ordered whitespace allows", "AMEND as 6-column structured table (Adjustment / What user changes / What changes in output / Slots re-filled / Gates re-run) makes C-08 and C-14 obligations verifiable by column inspection at the same structural level as OUTPUT CONTRACTS — prose enforcement eliminated from the amendment boundary", "EXECUTION DEPENDENCY table in PREFLIGHT provides step-level DAG complementing C-34's slot-level Required-by column — PREFLIGHT becomes a full execution specification: slot targets, inter-slot dependencies, step ordering, and gate constraints all readable before Phase 1"]}
```
