## flow-resilience Round 4 Scorecard

**Rankings:**

| Rank | Variation | Score | New Criteria |
|------|-----------|-------|--------------|
| 1 | V-05 | 100.0 | C-17 + C-18 + C-19 + C-20 |
| 2 | V-04 | 99.2 | C-17 + C-18 + C-20 |
| 3 | V-01 = V-02 = V-03 | 98.3 | C-17 + one other each |

**Key findings:**

- **C-17 is now baseline** — all five variations pass unified row indexing. The R4 design correctly identified it as achievable across multiple architectures.
- **V-05 is the first to satisfy all four new criteria simultaneously**, confirming the central R4 hypothesis: anti-boundary instruction + phase gates + slot imperatives + ownership column are additive with no mechanism conflicts.
- **C-19 is the sole discriminator between V-04 (99.2) and V-05 (100)** — confirmed exactly as predicted. Phase gates (section-level) do not substitute for in-row slot imperatives (slot-level).
- **V-01/V-02/V-03 tie at 98.3** with clean single-axis failure patterns exactly matching the design logic.

**Three new excellence signals:**

1. **E-5**: Layered granularity — four criteria, four structural levels (table/section/slot/column), no conflicts
2. **E-6**: Anti-boundary instruction enables C-17+C-20 coexistence by naming the failure mode by symptom
3. **E-7**: In-row bold imperative text is genuine slot-level co-location — read at cell construction time, below section gates

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Layered granularity architecture satisfies C-17+C-18+C-19+C-20 simultaneously -- each new criterion addresses a distinct omission risk at a distinct structural level (table / section / slot / column) with no mechanism conflicts", "Anti-boundary instruction decouples ownership column from unified row index -- naming the failure mode by structural symptom ('not a sub-table boundary, not a role-sequence trigger') prevents the model from treating the SME-to-ChaosEng ownership transition at row 5 as a section boundary", "In-row bold imperative text in the Content field descriptor is slot-level co-location -- the model reads 'Write this row now. [requirement]. Do not advance to row N until [condition].' exactly when constructing that cell, operating below section gates and above-table blockquotes"]}
```
posite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 5/5 → 60 | 3/3 → 30 | 10/12 → 8.3 | **98.3** |
| V-02 | 5/5 → 60 | 3/3 → 30 | 10/12 → 8.3 | **98.3** |
| V-03 | 5/5 → 60 | 3/3 → 30 | 10/12 → 8.3 | **98.3** |
| V-04 | 5/5 → 60 | 3/3 → 30 | 11/12 → 9.2 | **99.2** |
| V-05 | 5/5 → 60 | 3/3 → 30 | 12/12 → 10.0 | **100.0** |

**Ranking**: V-05 > V-04 > V-01 = V-02 = V-03

---

## Summary

V-05 is the first variation to satisfy all four new v4 criteria simultaneously, confirming the central R4 hypothesis: the anti-boundary instruction (targeting C-17/C-20 tension) and in-row slot imperatives (targeting C-19) are independently additive to the phase-gate architecture (C-18). No mechanism conflicts with any other.

V-04 falls one criterion short: it has the ownership column, phase gates, and unified index but no slot-level imperatives in the Content descriptors. The score gap is V-05 (100) - V-04 (99.2) = 0.8 points, confirming C-19 as the sole discriminating criterion between the two.

V-01, V-02, V-03 each pass two of the four new criteria (C-17 is universal across all five) and tie at 98.3 -- exactly as predicted by the R4 design logic. Their failures are clean single-axis omissions: V-01 misses C-18/C-19, V-02 misses C-19/C-20, V-03 misses C-18/C-20.

**C-17 is now baseline** -- all five variations pass it. The R4 design logic correctly identified that unified row indexing was achievable in multiple architectures (column-owned tables, phase-gated tables, imperative-row tables). The v4 rubric ceiling requires all four new criteria simultaneously, which only V-05 achieves.

---

## Detailed Criterion Evaluations

### V-01 -- Output Format (Ownership Column + Anti-Boundary Instruction)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage | PASS | Three distinct named scenarios: Full Connectivity Loss / Dependent Service Unavailable / Eventual Consistency Conflict |
| C-02 | Four-field structure | PASS | Rows 1-4 (State / Capability / Data at risk / Recovery) in every table with fill-in descriptors |
| C-03 | Gap identification | PASS | Section 4 with three labeled mandatory subsections (GAP / DCV / MRF), minimum-one enforcement per subsection |
| C-04 | Distributed systems accuracy | PASS | Controlled conflict vocabulary (last-write-wins / merge / manual-reconcile / reject-stale) + actor chain notation + chaos injection layer specification |
| C-05 | Commerce domain grounding | PASS | "cashier / customer / operator" in Capability descriptor; named commerce service in Scenario 2 |
| C-06 | Severity + blast radius | PASS | Rows 5-6 in every table |
| C-07 | Recovery path specificity | PASS | Actor chain notation required: "each step must begin with one of these four labels" |
| C-08 | Conflict resolution | PASS | Scenario 3 row 5: constrained vocabulary + adequacy assessment; "Select exactly one. Do not paraphrase." |
| C-09 | Chaos test cases | PASS | Rows 7-10 inside same contract table as trace rows |
| C-10 | Observability hooks | PASS | Per-finding inline hooks on line immediately after each entry |
| C-11 | Named actor chain | PASS | Actor chain notation defined; required in all Recovery rows |
| C-12 | Constrained conflict vocabulary | PASS | "Select exactly one. Do not paraphrase." |
| C-13 | Gap-merge prevention | PASS | "(mandatory -- do not omit or merge with scenarios)" annotation |
| C-14 | Chaos co-located | PASS | Rows 7-10 inside same contract table; "do not split into sub-tables; do not move chaos rows to a separate section" |
| C-15 | Per-finding hook | PASS | Hook on line immediately after each finding; "Do not collect hooks into a separate observability section" |
| C-16 | Completeness checklist | PASS | "Include this block in the artifact. Fill all boxes and the count before writing the file." |
| C-17 | Unified sequential index | PASS | Anti-boundary instruction + "Fill all rows in order (1 through 10) in a single top-to-bottom pass. Do not group rows by role. Do not insert a horizontal rule, blank row, or section header between rows where the Owned by value changes." Tables show rows 1-10/1-11 with no structural boundary between rows 4 and 5 |
| C-18 | Phase-gate sequencing | **FAIL** | No named phase gates. Completeness check annotation ("Do not write the artifact until all three boxes are checked") is a compliance instruction, not a named gate with explicit stop condition. Fails pass condition: "at least two named phase gates appear with explicit advance conditions" |
| C-19 | Slot-level imperatives | **FAIL** | Content descriptors for rows 7 and 10/11 are generic fill-in brackets: "[exact failure injection: what to break, at which layer (OS / network / application), for how long...]". No bold imperative text, no "Write this row now" or "Do not advance until" co-located at slot granularity |
| C-20 | Role-ownership column | PASS | Four-column table (Row / Field / Content / Owned by) with SME/Chaos Eng per row. Anti-boundary instruction: "The 'Owned by' column is a per-row metadata tag -- it is not a section marker, not a sub-table boundary, and not a role-sequence trigger." |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 10/12

```
composite = (5/5 * 60) + (3/3 * 30) + (10/12 * 10)
          = 60 + 30 + 8.33
          = 98.3
```

**Score: 98.3 / 100**

---

### V-02 -- Lifecycle (Phase Gates Verify Structural Integrity)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage | PASS | Three distinct scenarios in Phase 1 |
| C-02 | Four-field structure | PASS | Rows 1-4 in every table; Phase 1 Gate condition 1 verifies all cells filled |
| C-03 | Gap identification | PASS | Phase 2 is a mandatory phase with its own gate; three subsections with minimum-one enforcement |
| C-04 | Distributed systems accuracy | PASS | "Commerce / Distributed Systems domain expert" persona; chaos injection rows require layer-specific technical content |
| C-05 | Commerce domain grounding | PASS | "cashier / customer / operator" in Capability; named service in Scenario 2 |
| C-06 | Severity + blast radius | PASS | Rows 5-6 in every table |
| C-07 | Recovery path specificity | PASS | Actor chain notation required; "Every Recovery row must prefix each step with one of these four labels" |
| C-08 | Conflict resolution | PASS | Constrained vocabulary + adequacy assessment; "Select exactly one in Scenario 3 row 5. Do not paraphrase." |
| C-09 | Chaos test cases | PASS | Rows 7-10 inside same contract table; Phase 1 Gate condition 3 verifies no separator between rows 1-6 and rows 7-10 |
| C-10 | Observability hooks | PASS | Phase 2: "Every finding carries an inline observability hook on the line immediately following it"; Phase 2 Gate verifies |
| C-11 | Named actor chain | PASS | Actor chain notation defined; required in all Recovery rows |
| C-12 | Constrained conflict vocabulary | PASS | "Select exactly one... Do not paraphrase." |
| C-13 | Gap-merge prevention | PASS | Phase 2 is a separate mandatory phase; Phase 2 Gate verifies all three subsections present |
| C-14 | Chaos co-located | PASS | Rows 7-10 are rows in the same table; Phase 1 Gate condition 3: "No sub-table header, no horizontal rule, and no blank separator line appears between rows 1-6 and rows 7-10 in any scenario table" |
| C-15 | Per-finding hook | PASS | Phase 2 Gate condition 2: "Every finding entry is followed immediately by a hook line containing metric=, alert=, and owner=" |
| C-16 | Completeness checklist | PASS | Phase 3: "Fill this checklist now. Include it in the artifact. Do not write the artifact file until all three boxes are checked and the count reads '3 of 3'." Named phase with stop condition |
| C-17 | Unified sequential index | PASS | "Fill rows in sequence from 1 to 10 (or 1 to 11 for Scenario 3) without inserting headers, horizontal rules, or blank separator lines between rows." Phase 1 Gate condition 2: "Row numbers are sequential and unbroken: Scenarios 1-2 rows 1-10, Scenario 3 rows 1-11" and condition 3 explicitly names structural violations by observable symptom ("no horizontal rule appears between rows 1-6 and rows 7-10") |
| C-18 | Phase-gate sequencing | PASS | PHASE 1 GATE (5 explicit advance conditions) + PHASE 2 GATE (4 explicit advance conditions). Both include explicit stop language: "Do not begin Phase 2 until all five conditions are verified." Gate 1 converts C-17 from format instruction to verifiable stop condition |
| C-19 | Slot-level imperatives | **FAIL** | No slot-level imperatives in Content descriptors. Rows 7 and 10/11 have generic brackets "[exact failure injection: layer (OS / network / application), failure type, duration]". Phase gates are section-level stop conditions -- they verify properties of completed tables, not co-located at slot granularity within a row |
| C-20 | Role-ownership column | **FAIL** | Three-column table (Row / Field / Content) only. No "Owned by" or equivalent ownership column. Roles are implicit from topic assignment in prompt header, not structurally traceable per row |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 10/12

```
composite = (5/5 * 60) + (3/3 * 30) + (10/12 * 10)
          = 60 + 30 + 8.33
          = 98.3
```

**Score: 98.3 / 100**

Note: V-02's Phase 1 Gate names structural violations by observable symptom ("no horizontal rule appears between rows 1-6 and rows 7-10") -- the strongest C-17 gate formulation in R4 outside of V-05.

---

### V-03 -- Phrasing Register (Slot-Level Imperatives Inside Table Rows)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage | PASS | Three distinct named scenarios |
| C-02 | Four-field structure | PASS | Rows 1-4 in every table |
| C-03 | Gap identification | PASS | Section 4 mandatory with three labeled subsections |
| C-04 | Distributed systems accuracy | PASS | Chaos injection rows require layer + failure type + duration; constrained conflict vocabulary |
| C-05 | Commerce domain grounding | PASS | Named commerce operations; "cashier / customer / operator" vocabulary |
| C-06 | Severity + blast radius | PASS | Rows 5-6 in every table |
| C-07 | Recovery path specificity | PASS | Actor chain notation required; "Each step must begin with one of these four labels" |
| C-08 | Conflict resolution | PASS | Controlled vocabulary + adequacy assessment in Scenario 3 row 5 |
| C-09 | Chaos test cases | PASS | Rows 7-10 inside same contract table; "do not split into sub-tables, do not move chaos rows to a separate section" |
| C-10 | Observability hooks | PASS | Per-finding inline hooks immediately after each finding |
| C-11 | Named actor chain | PASS | Actor chain notation required throughout |
| C-12 | Constrained conflict vocabulary | PASS | Constrained list + adequacy assessment + "Select exactly one" |
| C-13 | Gap-merge prevention | PASS | "(mandatory -- do not omit or merge with scenarios)" annotation |
| C-14 | Chaos co-located | PASS | Rows 7-10 in same table as rows 1-4 |
| C-15 | Per-finding hook | PASS | "Each finding carries an observability hook on the line immediately after the finding entry. Do not collect hooks into a separate observability section." |
| C-16 | Completeness checklist | PASS | "Include this block in the artifact. Fill all boxes and the count before writing the file. Do not write the artifact until all three boxes are checked and the count reads '3 of 3'." |
| C-17 | Unified sequential index | PASS | "Fill every row. The four-field trace, severity, blast radius, and chaos test rows are all rows in the same table -- do not split into sub-tables, do not move chaos rows to a separate section." Tables show rows 1-10/1-11 sequential with no structural boundary |
| C-18 | Phase-gate sequencing | **FAIL** | No named phase gates. "(mandatory -- do not omit or merge with scenarios)" is a compliance annotation; completeness check is an instruction. No named gate with explicit advance condition as required by pass condition |
| C-19 | Slot-level imperatives | PASS | Bold imperative text embedded in Content descriptor for rows 7 and 10/11 across all three scenarios. Scenario 1 row 7: "**Write this row now. Name the injection layer (OS / network / application), the failure type, and the duration. Do not advance to row 8 until this field contains all three.**"; Scenario 1 row 10: "**Write this row now. Name a specific observable failure indicator. Do not advance to Scenario 2 until row 10 contains a named, non-generic outcome.**"; Scenario 2 rows 7 and 10 carry equivalent imperatives; Scenario 3 rows 8 and 11 carry equivalent imperatives. First and last chaos row per scenario satisfied for all three scenarios |
| C-20 | Role-ownership column | **FAIL** | Three-column table (Row / Field / Content) only. No ownership column. Roles are defined in prompt header, not per-row column values |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 10/12

```
composite = (5/5 * 60) + (3/3 * 30) + (10/12 * 10)
          = 60 + 30 + 8.33
          = 98.3
```

**Score: 98.3 / 100**

Note: V-03 is the isolated C-19 proof. Its slot-level imperatives also provide content-level guidance ("Name the injection layer, the failure type, and the duration") rather than generic write-now commands -- strongest content-specificity mechanism among R4 variations.

---

### V-04 -- Combined: Unified Table + Phase Gates + Ownership Column (C-17 + C-18 + C-20)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage | PASS | Three distinct scenarios in Phase 1 |
| C-02 | Four-field structure | PASS | Rows 1-4 in every four-column table; Phase 1 Gate condition 1 verifies |
| C-03 | Gap identification | PASS | Phase 2 mandatory phase; three subsections with minimum-one enforcement |
| C-04 | Distributed systems accuracy | PASS | CAP theorem analysis + retry semantics + idempotency requirements in Chaos Engineer role description; constrained vocabulary |
| C-05 | Commerce domain grounding | PASS | Commerce SME role fills rows 1-4; named commerce operations |
| C-06 | Severity + blast radius | PASS | Rows 5-6 in every table; Chaos Engineer role owns |
| C-07 | Recovery path specificity | PASS | Actor chain notation required; "No prose recovery" |
| C-08 | Conflict resolution | PASS | Constrained vocabulary in Scenario 3 row 5; adequacy assessment |
| C-09 | Chaos test cases | PASS | Rows 7-10 inside same four-column table |
| C-10 | Observability hooks | PASS | Per-finding inline hooks; Phase 2 Gate condition 2 verifies |
| C-11 | Named actor chain | PASS | Actor chain notation defined; "Every Recovery row must prefix each step" |
| C-12 | Constrained conflict vocabulary | PASS | "Select exactly one in Scenario 3 row 5. Do not paraphrase." |
| C-13 | Gap-merge prevention | PASS | Phase 2 is a separate mandatory phase; Phase 2 Gate condition 4: "Each gap is distinct" |
| C-14 | Chaos co-located | PASS | Chaos Engineer owns rows 7-10 in the SAME four-column table as SME's rows 1-4 |
| C-15 | Per-finding hook | PASS | Phase 2 Gate condition 2: "Every finding entry is followed immediately by a hook line containing metric=, alert=, and owner=" |
| C-16 | Completeness checklist | PASS | Phase 3: "Fill this checklist now. Include it in the artifact. Do not write the artifact file until all three boxes are checked and the count reads '3 of 3'." |
| C-17 | Unified sequential index | PASS | Anti-boundary instruction: "Fill all rows in order (1 through 10) in a single top-to-bottom pass. Do not group rows by role or insert any structural separator between rows where the Owned by value changes." Phase 1 Gate condition 3: "No sub-table header, horizontal rule, or blank separator line appears between any two consecutive rows in any scenario table" |
| C-18 | Phase-gate sequencing | PASS | PHASE 1 GATE (6 conditions) + PHASE 2 GATE (4 conditions). Phase 1 Gate condition 4 also verifies C-20 jointly: "Every row has a non-blank 'Owned by' value (SME or Chaos Eng)." Gates are the joint verifier of C-17 and C-20 structural integrity |
| C-19 | Slot-level imperatives | **FAIL** | Content descriptors for rows 7 and 10/11 are generic brackets: "[exact failure injection: layer, failure type, duration]" with no bold imperative text. Phase gates verify properties of completed cells but are not co-located at slot granularity within the row fill sequence |
| C-20 | Role-ownership column | PASS | Four-column table (Row / Field / Content / Owned by) with SME/Chaos Eng per row. Anti-boundary instruction present. Phase 1 Gate condition 4 verifies all rows have non-blank Owned by value |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 11/12

```
composite = (5/5 * 60) + (3/3 * 30) + (11/12 * 10)
          = 60 + 30 + 9.17
          = 99.2
```

**Score: 99.2 / 100**

V-04 is the highest-scoring non-ceiling variation. Sole failure (C-19) is the expected discriminator -- confirms C-17, C-18, and C-20 are structurally compatible without slot-level imperatives.

---

### V-05 -- Full Synthesis: All Four New Axes (C-17 + C-18 + C-19 + C-20)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage | PASS | Three distinct scenarios in Phase 1 |
| C-02 | Four-field structure | PASS | Rows 1-4 in every four-column table; Phase 1 Gate condition 1; "Fill every row in every table. If a row's Content cell is empty in your output, stop and fill it before continuing." |
| C-03 | Gap identification | PASS | Phase 2 mandatory phase; blockquote imperatives ("Write GAP-01 now. Write the observability hook on the next line."); Phase 2 Gate verifies |
| C-04 | Distributed systems accuracy | PASS | Commerce / Distributed Systems persona; chaos injection rows require injection layer + failure type + duration; CAP/retry/idempotency in Chaos Engineer role |
| C-05 | Commerce domain grounding | PASS | Commerce SME owns rows 1-4 in every table; "cashier / customer / operator" in Capability; named commerce service in Scenario 2 |
| C-06 | Severity + blast radius | PASS | Rows 5-6 in every table; Chaos Engineer role; "Fill every row" covers these |
| C-07 | Recovery path specificity | PASS | "Every Recovery row must prefix each step with one of these four labels. No prose recovery." Prose recovery explicitly prohibited -- strongest C-07 mechanism |
| C-08 | Conflict resolution | PASS | "`-> Selected: ___`" fill-in field; "Select exactly one in Scenario 3 row 5. Do not paraphrase." Controlled vocabulary with adequacy assessment |
| C-09 | Chaos test cases | PASS | Rows 7-10 inside same four-column table; Phase 1 Gate lists chaos rows by name; "Do not advance to Scenario 2 until row 10 is filled" |
| C-10 | Observability hooks | PASS | "Write the observability hook on the next line" as blockquote imperative per gap subsection; Phase 2 Gate condition 2 verifies inline co-location |
| C-11 | Named actor chain | PASS | "Every Recovery row must prefix each step with one of these four labels. No prose recovery." Fill-in slot per actor label |
| C-12 | Constrained conflict vocabulary | PASS | "`-> Selected: ___`" fill-in eliminates template pass-through; "Do not paraphrase" closes paraphrase path |
| C-13 | Gap-merge prevention | PASS | Phase 2 is a separate mandatory phase; Phase 2 Gate + Phase 3 certification; "Empty rows are failures, not placeholders" |
| C-14 | Chaos co-located | PASS | "The chaos rows are part of the scenario table." Phase 1 Gate lists chaos rows by name. "Do not advance to Scenario 2 until row 10 is filled." Co-location + per-row advance condition -- strongest C-14 mechanism |
| C-15 | Per-finding hook | PASS | "Write GAP-01 now. Write the observability hook on the next line." Blockquote imperative co-located at each finding slot; Phase 2 Gate verifies every finding has inline hook |
| C-16 | Completeness checklist | PASS | "Fill this checklist now. Check each box. Write the count. Include this block in the artifact exactly as filled. Do not write the artifact file until the count reads '3 of 3'." "Exactly as filled" prevents template pass-through -- strongest C-16 |
| C-17 | Unified sequential index | PASS | Anti-boundary instruction: "Fill all rows in order (1 through 10, or 1 through 11 for Scenario 3) in a single top-to-bottom pass. Do not group rows by role or insert any structural separator between rows where the Owned by value changes." Phase 1 Gate condition 3: no sub-table header / horizontal rule / blank separator between consecutive rows |
| C-18 | Phase-gate sequencing | PASS | PHASE 1 GATE (6 conditions) + PHASE 2 GATE (4 conditions). Phase 1 Gate verifies: unified row index, no structural boundaries, Owned by completeness, actor chain notation, controlled vocabulary. Each gate is a named stop condition with explicit advance conditions |
| C-19 | Slot-level imperatives | PASS | Bold imperative text in Content descriptor for the first and last chaos row of each scenario: Scenario 1 rows 7 and 10, Scenario 2 rows 7 and 10, Scenario 3 rows 8 and 11. Example (Scenario 1, row 7): "**Write this row now. Name the injection layer (OS / network / application), the failure type, and the duration. Do not advance to row 8 until all three are present in this field.**" Model reads this command exactly when constructing that cell -- slot-level co-location at generation time |
| C-20 | Role-ownership column | PASS | Four-column table (Row / Field / Content / Owned by) with SME/Chaos Eng per row. Anti-boundary instruction: "The 'Owned by' column is a per-row metadata tag -- not a section break, sub-table boundary, or role-sequence trigger." Phase 1 Gate condition 4 verifies all rows have non-blank Owned by value |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 12/12

```
composite = (5/5 * 60) + (3/3 * 30) + (12/12 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

V-05 holds the tightest mechanism at every criterion. C-07/C-11 add "No prose recovery" as an explicit prohibition. C-08/C-12 use a fill-in field to eliminate the template-unchanged output path. C-16 adds "exactly as filled" to prevent checklist template pass-through. C-19 in-row imperatives operate below section gates and above-table blockquotes -- they are read at the moment of cell construction.

---

## Excellence Signals -- Round 4

### E-5 (R4): Layered granularity architecture satisfies all four new criteria simultaneously

V-05 works because each new criterion addresses a distinct omission risk at a distinct structural level with no mechanism overlap or conflict:

- **C-17 (table-level)**: Unified sequential row index prevents the model from treating chaos rows as a structural decision -- they are rows in the same table, numbered after trace rows.
- **C-18 (section-level)**: Phase gates enforce processing sequence as named stop conditions -- the model cannot advance to the gap registry without completing all scenario tables.
- **C-19 (slot-level)**: Bold imperative text co-located in the Content descriptor at rows 7 and 10/11 provides per-row omission prevention that operates below section-level gates.
- **C-20 (column-level)**: The "Owned by" column makes role accountability structurally traceable per row without creating a section boundary.

None of these mechanisms occupy the same structural level, so combining all four is additive without redundancy.

### E-6 (R4): Anti-boundary instruction is the enabling mechanism for C-17+C-20 coexistence

V-01 R4 and V-04/V-05 R4 confirm the R4 hypothesis: V-04 R3's C-17 failure was caused by the range-based role preamble ("SME owns rows 1-4"), not by the ownership column itself. The anti-boundary instruction ("The 'Owned by' column is a per-row metadata tag -- not a section break, sub-table boundary, or role-sequence trigger") prevents the model from treating the ownership transition at row 5 as a structural signal. The instruction names the failure mode by its structural symptom rather than only prohibiting it.

### E-7 (R4): In-row bold imperative text is the correct slot-level co-location mechanism for C-19

V-03 and V-05 confirm that embedding bold imperative commands in the Content field descriptor of specific rows satisfies C-19's slot-level requirement. The mechanism format: "**Write this row now. [specific content requirement]. Do not advance to row N until [condition].**" placed in the table template at the target row. This is distinct from:
- Section-level "do not omit" annotations (apply to whole table, not a specific row)
- Phase gate conditions (verify completed table properties after the fact, not co-located at fill time)
- Above-table blockquotes from R3 (V-05 R3 -- apply to the entire table, not individual row slots)

The slot-level imperative is read by the model at the exact moment it constructs the cell content for that row -- genuinely co-located at generation time.

---

## Ranking Summary

| Rank | Variation | Score | New Criteria Passed | Key Mechanism |
|------|-----------|-------|---------------------|---------------|
| 1 | V-05 | 100.0 | C-17 + C-18 + C-19 + C-20 | All four layered -- anti-boundary + phase gates + slot imperatives + ownership column |
| 2 | V-04 | 99.2 | C-17 + C-18 + C-20 | Three of four -- missing slot-level imperatives (C-19) |
| 3 | V-01 | 98.3 | C-17 + C-20 | Anti-boundary + ownership column; no gates, no slot imperatives |
| 3 | V-02 | 98.3 | C-17 + C-18 | Phase gates verify structural integrity; no ownership column, no slot imperatives |
| 3 | V-03 | 98.3 | C-17 + C-19 | Slot-level imperatives in row Content descriptors; no gates, no ownership column |

**V-05** is the recommended golden candidate. Ceiling confirmed at 100/100 under v4 rubric.

**V-04** is the recommended production default for contexts where slot-level imperative verbosity is undesirable -- three of four new criteria at 99.2 with a clean four-column table + phase gate structure.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Layered granularity architecture satisfies C-17+C-18+C-19+C-20 simultaneously -- each new criterion addresses a distinct omission risk at a distinct structural level (table / section / slot / column) with no mechanism conflicts", "Anti-boundary instruction decouples ownership column from unified row index -- naming the failure mode by structural symptom ('not a sub-table boundary, not a role-sequence trigger') prevents the model from treating the SME-to-ChaosEng ownership transition at row 5 as a section boundary", "In-row bold imperative text in the Content field descriptor is slot-level co-location -- the model reads 'Write this row now. [requirement]. Do not advance to row N until [condition].' exactly when constructing that cell, operating below section gates and above-table blockquotes"]}
```
