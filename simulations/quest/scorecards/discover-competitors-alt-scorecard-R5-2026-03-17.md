Now I have everything needed. Let me score all five variations against rubric v4.

---

## discover-competitors-alt — R5 Scorecard

**Baseline:** R4 = 140/140 (all 18 criteria PASS across all five variations). Rubric v4 adds C-19–C-22 (4 new aspirational criteria). Max composite moves from 140 to 160.

---

### C-01 through C-18 — Inherited from R4

All five R5 variations preserve the full structural foundation of R4: competitor table with C0 row, per-row citation gate, WHITESPACE block with attribute-absence evidence, CROSS-DIMENSIONAL proof block (SOURCE / REDUCTION-1 / REDUCTION-2 / THEREFORE), findings section with claim-level anchor instructions, AMEND with exactly 3 adjustments including proof rerun on focus shift, INERTIA-REF mechanism section with specific mechanism requirement, NOT ACCEPTABLE examples for name-only anchoring, named failure states throughout, and the SOURCE slot declared before reduction arguments. **All 18 criteria: PASS across all five variations** (same evidence basis as R4; no structural regression introduced).

---

### C-19 — Synthesis-first output contracts

Pass condition: At least one output slot requirement named by label stated within the data-collection phase instruction, not only at the synthesis phase.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Dedicated "OUTPUT CONTRACTS" section between Phase 0 and Phase 1, before any collection, names three labeled slots: "WHITESPACE absence evidence," "ANCHOR cell value," "INERTIA-REF-DELTA phrase." Phase 3 heading explicitly references "(fills WHITESPACE absence evidence slot — see OUTPUT CONTRACTS)." |
| V-02 | **PASS** | "OUTPUT CONTRACT — collect during this phase" note opens Phase 3 (the collection phase), naming slots by label: "Anchor cell value," "INERTIA-REF-DELTA cell value." States "they cannot be synthesized at Phase 6 time." Embedded within the collection phase instruction itself. |
| V-03 | **PASS** | Standalone "OUTPUT CONTRACTS" section after PREFLIGHT and before Phase 1 names three labeled slots: "WHITESPACE absence evidence (required by Phase 4)," "ANCHOR cell value (required by Phase 5)," "INERTIA-REF-DELTA phrase (required by Phase 5 per GATE 4)." All named before any collection phase. |
| V-04 | **PASS** | "OUTPUT CONTRACT" table appears before Phase 1 with five named rows: INERTIA-REF, Anchor column, Absence evidence block, SOURCE slot, INERTIA-REF-DELTA. Each row has label and required format. Phases reference these slots by name ("fills Absence evidence slot — OUTPUT CONTRACT"). |
| V-05 | **PASS** | "OUTPUT CONTRACT — collect during this phase" note opens Phase 3, naming "(a) Anchor cell values in `Row C{N}, {attribute}: \"{value}\"` format, (b) INERTIA-REF-DELTA phrases contrasting each competitor against the C0 mechanism, and (c) URL citations per external row." Named by label within the collection phase. |

**C-19: PASS — all five.**

---

### C-20 — Structural column coercion for anchoring

Pass condition: Column format/template makes name-only entries syntactically non-conforming without rule evaluation; prohibition-only does not satisfy.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Anchor column: "`Row C{N}, {attribute}: \"{value}\"`" with explicit statement "a cell containing only a competitor name is syntactically malformed and must be rewritten before the row is output." Format template defined; malformation is structural, not rule-evaluated. ACCEPTABLE/NOT ACCEPTABLE examples provided. |
| V-02 | **PASS** | Two structural coercions: (1) Competitor table Anchor column: same `Row C{N}` format template, "syntactically malformed." (2) Findings table INERTIA-REF-DELTA column: "`vs. INERTIA-REF — {verdict}: {phrase}`" — "a cell with only 'N/A' or a competitor name is malformed." Both columns defined as structural format shapes, not prohibition rules. |
| V-03 | **PASS** | Anchor column in Phase 3 with format template; "syntactically malformed cells trigger GATE 2 before rule evaluation." Explicit statement that malformation precedes rule evaluation — this is the purest structural coercion framing in R5. |
| V-04 | **PASS** | "Anchor column format (OUTPUT CONTRACT — Anchor slot): `Row C{N}, {attribute}: \"{value}\"` — cells containing only a competitor name are syntactically malformed; rewrite before outputting." Format constraint tied to the OUTPUT CONTRACT slot. |
| V-05 | **PASS** | Three structural coercions: (1) Competitor table Anchor column with format template; (2) Findings table Anchor column with same template; (3) Findings table INERTIA-REF-DELTA column: `vs. INERTIA-REF — {verdict}: {phrase}` — "N/A or empty is malformed." Maximum coercion density across two independent tables. |

**C-20: PASS — all five.**

---

### C-21 — Gate-as-section with PASS/FAIL table

Pass condition: At least one gate is a named section with 3-column table (Check / Pass condition / Failure state), 2+ rows.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | "CITATION GATE" named section heading with table: Check / Pass condition / Failure state, 2 rows (Citation cell populated; Citation location). Section heading + 3-column table + ≥2 rows. |
| V-02 | **PASS** | "CITATION GATE — NAMED SECTION" with table: Check / Pass condition / Failure state, 2 rows (Citation cell populated; Citation in row, not footnote). Section heading + 3-column table + ≥2 rows. |
| V-03 | **PASS** | PREFLIGHT block with four named gate sections each containing a 3-column table: GATE 1 (2 rows), GATE 2 (2 rows), GATE 3 (3 rows), GATE 4 (2 rows). Most extensive gate architecture in R5; four independent named gate sections. |
| V-04 | **PASS** | "CITATION GATE" named section with table: Check / Pass condition / Failure state, 2 rows (Citation present; Citation in row, not footnote). Section heading + 3-column table + ≥2 rows. |
| V-05 | **PASS** | Four named gate sections: CITATION GATE (3 rows), ANCHOR GATE — COMPETITOR TABLE (2 rows), PROOF GATE (3 rows), ANCHOR GATE — FINDINGS TABLE (2 rows). Each is a named section heading with 3-column table. Most gate sections of any R5 variation. |

**C-21: PASS — all five.**

---

### C-22 — INERTIA-REF per-finding citation

Pass condition: Named inertia reference token defined once; each finding must cite it by name as a mandatory baseline; definition without per-finding citation requirement does not satisfy.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Token defined in Phase 0: `INERTIA-REF = [C0 name]: [specific mechanism]`. Mandatory per-finding citation stated in Phase 0: "Every finding in Phase 5 must cite **INERTIA-REF** by token name." Phase 5 confirms: "A finding that does not cite INERTIA-REF by name is an **inertia citation failure**." Token defined + explicit per-finding mandate + named failure state. |
| V-02 | **PASS** | Token defined in Phase 2. Per-finding requirement satisfied via column coercion: INERTIA-REF-DELTA column in findings table requires "`vs. INERTIA-REF — {verdict}: {phrase}`" — the token name appears in the column template for every row. "Every finding row must carry a comparison against INERTIA-REF." Column shape enforces per-finding citation; token cited by name in the template itself. Indirect mechanism confirmed PASS by variation author. |
| V-03 | **PASS** | Token defined in Phase 2. GATE 4 (INERTIA-REF GATE) specifies as a table row: "Per-finding citation: Each finding cites INERTIA-REF by token name with reinforces/challenges/contextualizes verdict and specific C0 mechanism phrase — **Inertia citation failure**." Phase 6 applies GATE 4 per finding. Most explicit per-finding gate enforcement of any variation. |
| V-04 | **PASS** | Token defined in "INERTIA-REF DEFINITION" section before Phase 1. "Every finding in Phase 5 must cite INERTIA-REF by token name and state whether the finding reinforces, challenges, or contextualizes the mechanism." Phase 5 confirms: "A finding missing this clause is an **inertia citation failure**." Token defined + per-finding mandate + named failure state. |
| V-05 | **PASS** | Token defined in Phase 2. Stated explicitly: "INERTIA-REF is a required citation in every finding in Phase 6." Findings table INERTIA-REF-DELTA column coerces by format. ANCHOR GATE — FINDINGS TABLE includes row: "INERTIA-REF-DELTA format conforms — `vs. INERTIA-REF — {verdict}: {phrase}` — verdict word and C0 mechanism phrase both present — **Inertia citation failure**." Triple-layer enforcement: instruction + column coercion + gate table. |

**C-22: PASS — all five.**

---

### Per-criterion summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Status quo competitor | PASS | PASS | PASS | PASS | PASS |
| **C-02** Minimum external competitors | PASS | PASS | PASS | PASS | PASS |
| **C-03** Focus dimension support | PASS | PASS | PASS | PASS | PASS |
| **C-04** Whitespace finding present | PASS | PASS | PASS | PASS | PASS |
| **C-05** Findings section present | PASS | PASS | PASS | PASS | PASS |
| **C-06** Inertia stickiness reasoning | PASS | PASS | PASS | PASS | PASS |
| **C-07** Web-verified competitive claim | PASS | PASS | PASS | PASS | PASS |
| **C-08** AMEND — 3 actionable adjustments | PASS | PASS | PASS | PASS | PASS |
| **C-09** Cross-dimensional whitespace | PASS | PASS | PASS | PASS | PASS |
| **C-10** Table-stakes grounding per finding | PASS | PASS | PASS | PASS | PASS |
| **C-11** Fully-cited competitor table | PASS | PASS | PASS | PASS | PASS |
| **C-12** Self-negating cross-dimensional | PASS | PASS | PASS | PASS | PASS |
| **C-13** Claim-level finding anchors | PASS | PASS | PASS | PASS | PASS |
| **C-14** AMEND as proof validator | PASS | PASS | PASS | PASS | PASS |
| **C-15** Inline anchor tag before proof | PASS | PASS | PASS | PASS | PASS |
| **C-16** Gate failure naming | PASS | PASS | PASS | PASS | PASS |
| **C-17** WHITESPACE by attribute absence | PASS | PASS | PASS | PASS | PASS |
| **C-18** NOT ACCEPTABLE anchoring example | PASS | PASS | PASS | PASS | PASS |
| **C-19** Synthesis-first output contracts | PASS | PASS | PASS | PASS | PASS |
| **C-20** Structural column coercion | PASS | PASS | PASS | PASS | PASS |
| **C-21** Gate-as-section PASS/FAIL table | PASS | PASS | PASS | PASS | PASS |
| **C-22** INERTIA-REF per-finding citation | PASS | PASS | PASS | PASS | PASS |

---

### Composite scores

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---:|---:|---:|---:|---:|
| Essential (5/5 × 60) | 60 | 60 | 60 | 60 | 60 |
| Recommended (3/3 × 30) | 30 | 30 | 30 | 30 | 30 |
| Aspirational (14/14 × 70) | 70 | 70 | 70 | 70 | 70 |
| **Composite** | **160** | **160** | **160** | **160** | **160** |
| **Grade** | Exceptional | Exceptional | Exceptional | Exceptional | Exceptional |
| **Golden threshold** | YES | YES | YES | YES | YES |

---

### Projected vs. actual

| Variation | Projected | Actual | Delta | Note |
|-----------|----------:|-------:|------:|------|
| V-01 | ~160 | 160 | 0 | On target |
| V-02 | ~157.5 | 160 | +2.5 | C-22 via column coercion confirmed PASS; indirect mechanism satisfies "cite by name" in template |
| V-03 | ~160 | 160 | 0 | On target |
| V-04 | ~160 | 160 | 0 | On target |
| V-05 | ~160 | 160 | 0 | On target |

**Why V-02 PARTIAL? projection did not hold:** The C-22 uncertainty was whether column-shape coercion satisfies "cite by name." The INERTIA-REF-DELTA column template contains the literal string "vs. INERTIA-REF" — every row that fills the column format cites the token by name. The rubric requires "compare against that token by name." A cell reading `vs. INERTIA-REF — challenges: C0 uses...` does compare against it by name. PASS.

---

### Key interactions — resolved

| Interaction | Resolution |
|---|---|
| V-02 C-22 via structural coercion vs. V-01/V-03/V-04/V-05 C-22 via instruction | Both mechanisms PASS. Column template containing "vs. INERTIA-REF" satisfies "cite by name" as directly as an explicit instructional requirement. |
| V-03 PREFLIGHT gates (before Phase 1) vs. V-01/V-04 gates (within collection phases) | Both PASS C-21. PREFLIGHT architecture achieves cleaner rules/execution separation but no scoring differential. |
| V-05 triple coercion (C-20 × 3) vs. V-01/V-03/V-04 single coercion | C-20 requires at least one structural template. V-05 exceeds minimum; no scoring differential but mechanism strength is highest. |
| V-04 OUTPUT CONTRACT as table vs. V-01/V-03 as bulleted list | Both PASS C-19. Table form is more scannable; no scoring differential but structural clarity advantage to V-04. |

---

### Excellence signals

Patterns from this round representing genuine structural advances over R4:

**1. Phase 0 INERTIA-REF as gravitational frame (V-01)**
Defining INERTIA-REF before reading any repository context makes every downstream phase reference the C0 mechanism naturally. The output contracts note explicitly requires identifying INERTIA-REF-DELTA phrases during Phase 2 collection — data is gathered against the reference frame from the moment it enters the table. Compared to defining INERTIA-REF mid-Phase (V-02/V-03/V-05), Phase 0 placement eliminates any collection phase where the frame is absent.

**2. INERTIA-REF-DELTA as structural column in findings table (V-02, V-05)**
Applying C-20's column coercion to the INERTIA-REF-DELTA column in the findings table satisfies C-22 through form rather than instruction. The column template contains the token name — any row that conforms to the template has cited INERTIA-REF. This is the same adversarial robustness argument that makes structural coercion stronger than prohibition for C-13/C-20: compliance is enforced by the shape before any rule evaluation occurs.

**3. OUTPUT CONTRACT as structured table with slot labels + required formats (V-04)**
V-04's output contract is a table (Slot / Label / Required format) rather than a bulleted list. Each output requirement is a named row with a format specification. This makes each slot checkable as a discrete row — the same debuggability argument that drove C-21 gate tables over prose gates. The table form also makes the contract scannable as a pre-flight checklist.

**4. Multi-gate PREFLIGHT block before Phase 1 (V-03)**
Declaring all four gates (CITATION, ANCHOR, PROOF, INERTIA-REF) as named sections with PASS/FAIL tables before any execution phase creates the clearest possible rules/execution separation. Phases are concise execution instructions that reference gates by name. This is the inverse of the inline-gate pattern: instead of rules embedded in each phase, a single PREFLIGHT section contains all gates, and phases defer to them by reference. Most debuggable overall structure in R5.

**5. C-20 applied to both tables simultaneously (V-05)**
Applying structural column coercion to the competitor table Anchor column, the findings table Anchor column, AND the INERTIA-REF-DELTA column produces three independent enforcement points. Name-only anchoring is rejected in two separate tables before any rule evaluation; per-finding INERTIA-REF citation is coerced by column shape in the findings table. Maximum form-based compliance density — adversarial robustness is highest for C-13 and C-22 simultaneously.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["INERTIA-REF established in Phase 0 before context is read makes the C0 mechanism the gravitational frame for all collection phases", "INERTIA-REF-DELTA as a structural column in the findings table satisfies C-22 via form rather than instruction — column template contains the token name, coercing per-row citation before rule evaluation", "OUTPUT CONTRACT as a structured table (Slot / Label / Required format) makes each output slot a checkable discrete row, extending gate-table debuggability to the output contract declaration", "multi-gate PREFLIGHT block before Phase 1 separates all rule declarations from execution phases — phases reference gates by name, creating the clearest rules/execution boundary in any R5 variation"]}
```
