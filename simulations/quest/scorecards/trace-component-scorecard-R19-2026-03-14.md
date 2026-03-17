## trace-component · Round 19 · Scoring

### Scoring Methodology

Scoring is structural: each criterion is evaluated against what the prompt architecture produces when executed, not against hypothetical output. Criteria C-01 through C-08 require specific table structures to be present; C-09 through C-58 require specific design mechanisms.

---

### Criterion-by-Criterion Analysis

#### Essential Tier (C-01 through C-05) -- 60 pts total, 12 pts each

All 5 variations include TABLE-1 through TABLE-8, MANIFEST-1 through MANIFEST-5, and the full gate apparatus. Essential criteria are satisfied structurally by all variations.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01 Event Anchor | PASS | PASS | PASS | PASS | PASS | TABLE-1 has Event Type / Component Name / Handler Function / File Location columns; GATE-1 blocks blank cells and generic strings |
| C-02 Component Tree Traversal | PASS | PASS | PASS | PASS | PASS | TABLE-2 with T-ID + Direction column schema, minimum 2 rows enforced by GATE-2 |
| C-03 State Update Map | PASS | PASS | PASS | PASS | PASS | TABLE-3 with MUTATION COUNT PRE-DECLARATION; GATE-3 blocks vague strings; ZERO MUTATION DECLARATION for total=0 |
| C-04 Re-render Inventory | PASS | PASS | PASS | PASS | PASS | TABLE-4 with "Every T-ID from TABLE-2 must appear"; PROMOTION BLOCK mandatory; GATE-4 blocks omissions |
| C-05 Final UI State | PASS | PASS | PASS | PASS | PASS | TABLE-6 four-phase; GATE-6 explicitly blocks 3-phase collapse and vague strings |

**Essential tier: all 5 variations PASS all 5 criteria. Essential tier: 60/60 for all.**

---

#### Recommended Tier (C-06 through C-08) -- 30 pts total, 10 pts each

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-06 Side Effect Coverage | PASS | PASS | PASS | PASS | PASS | TABLE-5 with zero-effects row template |
| C-07 Issue Detection | PASS | PASS | PASS | PASS | PASS | TABLE-7 five fixed rows; N/A prohibited; F-02 UR cross-reference; GATE-7 blocks summarize-away strings |
| C-08 Framework Vocabulary | PASS | PASS | PASS | PASS | PASS | TRAVERSAL-SCHEMA Area 1 declaration required; TABLE-2 direction codes are framework vocabulary |

**Recommended tier: all 5 variations PASS all 3 criteria. Recommended tier: 30/30 for all.**

---

#### Aspirational Tier (C-09 through C-58) -- 100 pts total, 2 pts each

For criteria C-09 through C-56 I will note the shared structural evidence and flag any variation-specific differentials. Then C-57 and C-58 receive full individual analysis.

**C-09 Fix Recommendations** -- PASS all: TABLE-7 "Fix -- API or Pattern" column mandatory.

**C-10 Render Quantification** -- PASS all: TABLE-4 "Re-renders? [Yes (N) / No]" co-locates count and verdict in same row cell.

**C-11 Inline Phase-Close Gates** -- PASS all: [GATE-1] through [GATE-7] terminate each phase section with named exclusion strings.

**C-12 Mandatory Comparison Column** -- PASS all:
- V-01/V-03: TABLE-7 "Do-Nothing Cost" column compares fixing vs. leaving unaddressed; TABLE-8 maps criteria to satisfying fields.
- V-02/V-04/V-05: additionally, Area 3 enforcement table has "Enforcement Rationale" column explicitly framed as "why this form vs. simpler alternatives" -- a direct comparison column satisfying C-12 from multiple sources.

**C-13 Exact-Phrase Gate Family** -- PASS all: GATE-1 through GATE-7 intercept "the button", "a click", "state updates", "the store is modified", "several components re-render", "UI updates accordingly", "no major issues", "minor issue", "low risk" -- more than 3 distinct escape strings across multiple phases.

**C-14 Column-Header Escape Instruction** -- PASS all: "Direction [null default | departure codes]", "Role [Null confirmed -- basis / Departure -- evidence]", "Necessary? [Yes -- reason / No -- reason]" embed fill constraints in column headers.

**C-15 Do-Nothing Cost** -- PASS all: TABLE-7 "Do-Nothing Cost" column.

**C-16 FINDINGS Section Gate** -- PASS all: GATE-7 intercepts "no major issues", "no impact", "minor issue", "low risk", "no concerns found" at TABLE-7.

**C-17 Triple Structural Lock** -- PASS all: TABLE-7 satisfies all three simultaneously: (1) present as mandatory template, (2) "Finding [issue or 'none detected -- [reason]']" header embeds constraint, (3) GATE-7 names specific escape strings per row.

**C-18 Table Format Required for Triple Lock** -- PASS all: TABLE-7 is table format with column headers.

**C-19 Gate-Block Formalism** -- PASS all: all exclusions appear in [GATE-N: ...] blocks. V-04 adds DIRECTIVE/REQUIREMENT labels but these supplement, not replace, gate formalism.

**C-20 Framework Declaration Gate** -- PASS all: FRAMEWORK DECLARATION table required before MANIFEST-1 in all variations; "Do not begin MANIFEST-1 until this header is complete" is an explicit positional gate.

**C-21 Failure Mode Displacement** -- PASS all: MUTATION COUNT PRE-DECLARATION shows exact replacement for vague state descriptions; ZERO MUTATION DECLARATION block provides explicit displacement for the zero-mutation case; TABLE-3 GATE-3 intercepts forbidden strings; "Role [Null confirmed -- basis / Departure -- evidence]" displaces missing-role pattern.

**C-22 Re-render Necessity Annotation** -- PASS all: TABLE-4 "Necessary? [Yes -- reason / No -- reason]" column is mandatory per row.

**C-23 Four-Phase UI Progression** -- PASS all: TABLE-6 explicitly requires rows 1-4 covering pre-action baseline, synchronous/optimistic, async success, async error; GATE-6 blocks 3-phase collapse.

**C-24 Zero-Mutation Declaration** -- PASS all: ZERO MUTATION DECLARATION block in TABLE-3 template for total=0 case.

**C-25 Issue Category Completeness** -- PASS all: TABLE-7 has five fixed rows (F-01 render performance, F-02 unnecessary re-renders, F-03 accessibility, F-04 async error handling, F-05 memory leaks); "none detected -- [reason]" format required for cleared categories.

**C-26 Unnecessary Re-render Promotion** -- PASS all: PROMOTION BLOCK in TABLE-4 feeds F-02 in TABLE-7 via explicit UR-ID cross-reference column.

**C-27 Mutation Count Pre-Declaration** -- PASS all: MUTATION COUNT PRE-DECLARATION code block required before TABLE-3.

**C-28 Per-Hop Direction Annotation** -- PASS all: TABLE-2 Direction column is per-row; "null default | departure codes" schema requires annotation at every hop.

**C-29 Re-render Inventory Completeness by Traversal** -- PASS all: "Every T-ID from TABLE-2 must appear -- including inert pass-through hops" is an explicit completeness gate.

**C-30 Mutation Count Dual-Track** -- PASS all: "Mutations: N=___ direct, M=___ inherited (total: ___)" is the required pre-declaration format.

**C-31 Schema-Field Coverage of Aspirational Criteria** -- PASS all: all 10 criteria C-20 through C-29 map to specific schema fields (FRAMEWORK DECLARATION, TABLE-3 format, TABLE-4 Necessary column, TABLE-6 four phases, zero-mutation block, TABLE-7 five rows, PROMOTION BLOCK, mutation pre-declaration, TABLE-2 Direction column, TABLE-4 T-ID completeness).

**C-32 Blank-Blocked Field Primacy** -- PASS all: TABLE-1 columns, TABLE-2 Direction+Role columns, TABLE-4 T-ID+Necessary columns, TABLE-6 Visible Elements -- all enforced by gate blocks naming blank cell as non-closer.

**C-33 Phase-Level Completeness Manifest** -- PASS all: MANIFEST-1 through MANIFEST-5 each declare components in scope / state keys / side effects; "Do not begin MANIFEST-1 until..." is a positional gate. V-03/V-05 additionally have per-phase vocabulary lines reinforcing this.

**C-34 Inert Pass-Through Explicit Marking** -- PASS all: INERT-HOP DECLARATION is mandatory regardless of count; the zero-case text "No inert pass-through hops -- all traversal components have supported departure codes" is explicitly present as a template requirement.

**C-35 Criteria Audit Cross-Validation Table** -- PASS all: TABLE-8 maps C-01 through C-08 to satisfying schema fields with PASS/FAIL verdict column.

**C-36 Inert-as-Default Direction Schema** -- PASS all: TRAVERSAL-SCHEMA Area 2 derives from NQ-1/NQ-2 requiring the null default to be the starting position; "Direction [null default | departure codes]" column header positions null default first; Role 2 instruction reinforces: "Every departure code is a supported claim; every hop without evidence of departure carries the null default."

**C-37 Manifest-Analysis Paired Block Structure** -- PASS all: MANIFEST-N immediately precedes TABLE-N in every case (N=1 through 5); "Do not begin MANIFEST-1 until the TRAVERSAL-SCHEMA is complete" is the positional gate at the outermost level.

**C-38 Manifest-Close Adjacency Marker** -- PASS all: each manifest ends with "*[Apply your TRAVERSAL-SCHEMA Area 3 placeholder instruction here -- verbatim, as this manifest's terminal line, naming TABLE-N as successor. Reproduce now.]*" (V-01/V-03) or equivalent REQUIREMENT-labeled form (V-04/V-05). The self-authored schema contains the exact close-line text which is then reproduced verbatim. Minimum 5 manifest close markers across all 5 manifests.

**C-39 Self-Authored Schema Constraint** -- PASS all: TRAVERSAL-SCHEMA slot is blank ("Author the complete schema here"); explicit "Do not reproduce any language from this prompt" instruction present in all variations; model must produce the schema artifact from CAUSAL PHASE reasoning.

**C-40 Dual-Constraint Position-and-Content Placeholder** -- PASS all: placeholder instructions co-locate both the content constraint ("verbatim" / "Worked Example cell") and the positional constraint ("as this manifest's terminal line") in single instruction. The model authors the full dual-constraint placeholder text in the schema, which is then reproduced verbatim at each manifest. DQ-3/DQ-4 ensure the dual form is reasoned before schema authorship.

**C-41 Schema Causal Explanation Requirement** -- PASS all: Area 3 authorship instruction requires "write the structural rationale for the close-line mechanism (NQ-3, DQ-2)" and "write the structural rationale for the dual-constraint form (DQ-3 through DQ-5)" before declaring the close-line text -- explicit causal explanation required.

**C-42 Anti-Reproduction Schema Authorship** -- PASS all: "Do not reproduce any language from this prompt -- not in paraphrase, not by reformatting question text into schema format" (V-01) or "Author in your own words from your CAUSAL PHASE reasoning. Do not reproduce any language from this prompt" (V-02 through V-05).

**C-43 Mutual-Constraint Entanglement Declaration** -- PASS all: DQ-4 forces model to articulate why satisfying one constraint alone leaves partial satisfaction structurally untenable; the self-authored close-line placeholder will embed this entanglement language; Role 2 instruction reinforces "Satisfying only one of the two placeholder requirements does not satisfy it."

**C-44 Numbered Constraint Enumeration in Placeholder** -- PASS all: DQ-3 asks for information enabling a verifier to distinguish neither/one/both constraints satisfied independently; DQ-5 asks about obligation count declaration; schema authorship derives numbered enumeration from these.

**C-45 Dual-Requirement Count Declaration in Placeholder** -- PASS all: DQ-5 explicitly targets the obligation count declaration at the instruction opening; schema authorship embeds this in the close-line placeholder.

**C-46 Epistemic-Register Question Framing** -- PASS all: NQ-1 ("warranted epistemic stance"), NQ-2 ("epistemic difference between omit vs. confirm-inactive"), NQ-3 ("epistemically correct characterization of the space"), DQ-1 ("epistemic relationship between departure code and evidence") are all epistemic-level -- none name specific schema artifact types as answers. More than 3 pass the substitution test.

**C-47 Causal-Completion Gate Before Schema Authorship** -- PASS all: "CAUSAL PHASE CLOSE -- All questions answered. No schema artifact produced. SCHEMA PHASE begins." is an explicit structural boundary between causal and schema phases. The causal phase has no schema slots; the schema phase opens after the close marker.

**C-48 Null-Hypothesis Register in Causal Question Set** -- PASS all: NULL REGISTER (NQ-1/NQ-2/NQ-3) appears before DEPARTURE REGISTER (DQ-1 through DQ-5) in all variations.

**C-49 Named-Register Subdivision of Causal Phase** -- PASS all: at minimum NULL REGISTER and DEPARTURE REGISTER are named sections with labeled headers. V-03 adds PHASE REGISTER; V-05 adds INERTIA REGISTER.

**C-50 Per-Register Close Marker Within Causal Phase** -- PASS all: "NULL REGISTER CLOSE" and "DEPARTURE REGISTER CLOSE" explicit markers present in all variations. V-03 adds "PHASE REGISTER CLOSE"; V-05 has compound close markers with accomplishment descriptors ("**NULL REGISTER CLOSE** -- Null baseline established", etc.).

**C-51 Successor-Naming in Manifest-Close Adjacency Marker** -- PASS all: every placeholder instruction names the specific successor: "naming TABLE-1 as successor", "naming TABLE-2 as successor" through TABLE-5. All five manifest close-lines name their phase-keyed successors.

**C-52 Compound Register Header Format** -- PASS all: "**NULL REGISTER** -- Epistemic status of null cases" and "**DEPARTURE REGISTER** -- Properties of departure claims" are present in all variations in compound form. V-03 additionally has "**PHASE REGISTER** -- Phase scope and boundary liabilities"; V-05 additionally has "**INERTIA REGISTER** -- Departure from structural inertia" and compound close markers.

**C-53 Horizontal-Rule Boundary Separators** -- PASS all: `---` horizontal rules delimit each named register section in all variations.

**C-54 Epistemic-Function Descriptor on Named Register Headers** -- PASS all:
- "Epistemic status of null cases" -- characterizes cognitive work: determining evidential standing of baseline before any departure is asserted. ✓
- "Properties of departure claims" -- characterizes cognitive work: identifying the logical properties departure-state assertions must satisfy. ✓
Both descriptors name cognitive work, not topic or position. Minimum two required; all variations carry at least two qualifying headers.

V-03's "**PHASE REGISTER** -- Phase scope and boundary liabilities" is borderline (names topic area more than cognitive function) but does not reduce the count below 2 for any variation.

**C-55 Header-Form Causal Questions** -- PASS all:
- V-01/V-03/V-04/V-05: NHQ-1 and NHQ-2 explicitly ground the compound header form ("A register section can be introduced by a bare bold label or by a compound label -- what information does the compound form provide...?"). Both address the header artifact: why the identifier and epistemic-function descriptor must co-occur.
- V-02: NHQ-1 and NHQ-2 present (no NHQ-3 needed for C-55). At least 2 header-form questions required; satisfied.

---

#### C-56 through C-58 -- Full Individual Analysis

**C-56 Schema-Declared Compound Header Template**

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | PASS | Area 3 explicitly instructs: "Then declare the compound header template: `**[LABEL]** -- [epistemic-function descriptor]`" as a named schema area requirement. Template appears as dedicated Area 3 field in self-authored schema. |
| V-02 | PASS | Area 3 boundary enforcement table Register section header row declares `**[LABEL]** -- [epistemic-function descriptor]` as Template Pattern column value. Named table row in self-authored schema satisfies "named schema field" requirement. |
| V-03 | PASS | Area 3 prose instructs: "Then declare the compound header template: `**[LABEL]** -- [epistemic-function descriptor]`" as the closing step of schema Area 3 authorship. |
| V-04 | PASS | Area 3 enforcement table Register section header row declares compound template as Template Pattern. The NHQ-3 forward-binding instruction reinforces the schema field's authority. |
| V-05 | PASS | Area 3 3-row enforcement table Register section header row declares compound template. The table structure elevates the template to a row in the enforcement schema artifact. |

**C-57 Exemplar-Grounded Compound Header Template in Schema**

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | PASS | Area 3 authorship instruction: "Then include the worked example you authored in NHQ-3 as your first exemplar. Then add at least one additional compound header example using a different register." NHQ-3 produces a real compound header line that is explicitly carried into schema prose as an exemplar. Two exemplars required; NHQ-3 is the anchoring derivation path. |
| V-02 | PASS | Area 3 enforcement table Worked Example cell has "No cell may be blank" enforcement rule and "Worked Example cells require a complete concrete line, not a placeholder pattern." The blank-blocked Worked Example cell in the Register section header row structurally enforces exemplar presence. |
| V-03 | **FAIL** | Area 3 authorship instruction closes with "Then declare the compound header template: `**[LABEL]** -- [epistemic-function descriptor]`" -- no exemplar requirement follows. NHQ-3 is absent from V-03 causal phase (the NHQ set contains only NHQ-1 and NHQ-2), so no exemplar-derivation step exists. The schema can declare the abstract pattern but has no causal production to forward as a worked example. |
| V-04 | PASS | Area 3 enforcement table Register section header row Worked Example cell: "paste the compound header line you authored in NHQ-3 here verbatim -- exact text, no reformulation." Enforcement rule: "The Register section header Worked Example cell must contain the NHQ-3 line verbatim." Dual-path enforcement: NHQ-3 production in causal phase + explicit cell-binding instruction. |
| V-05 | PASS | Area 3 enforcement table Register section header row Worked Example cell: "WRONG (inertia): `**[bare label only]**` / CORRECT (departure): [NHQ-3 line verbatim]." Both failure-mode and passing exemplar required in a single cell. The WRONG form (from NHQ-1/NHQ-2 inertia analysis) and CORRECT form (from NHQ-3 derivation) appear together, making the competitor structurally visible. |

**C-58 Schema Area 3 Structured Enforcement Table**

Pass condition: Schema Area 3 is a structured table with at minimum a template-element column and an Enforcement Rationale column populated for every row. At least two rows must carry a populated Enforcement Rationale cell naming a specific simpler alternative and the failure mode it produces. Prose Area 3 -- however complete -- does not pass.

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | **FAIL** | Area 3 is prose with labeled sub-sections. Authorship instruction uses "First write...", "Then write...", "Then declare..." prose sequence. Enforcement rationale for each template component is embedded in narrative text. No table structure, no Enforcement Rationale column, no row-addressable rationale cell. All C-57 requirements (exemplar, template declaration) are met in prose -- the failure is strictly format-level. |
| V-02 | PASS | Area 3 is a `\| Boundary Type \| Template Pattern \| Worked Example \| Enforcement Rationale \|` table with 2 rows (Manifest close-line; Register section header). Enforcement Rationale column enforcement rule: "must state the reasoning derived from your CAUSAL PHASE answers -- not a restatement of the template pattern itself." Both rows carry Enforcement Rationale cells. The register header row's rationale derives from NHQ-1/NHQ-2 (why compound form eliminates the two-read requirement). Simpler alternative (bare bold label) is the named alternative in the register header row; failure mode (deferred epistemic function declaration) is the named consequence. Two rows with populated Enforcement Rationale cells: PASS. |
| V-03 | **FAIL** | Area 3 is prose. "Then write the structural rationale for the close-line mechanism", "Then write the structural rationale for the dual-constraint form", "Then write the register header format rationale" are all prose authorship steps. No enforcement table is produced. Structurally identical to V-01 failure mode. |
| V-04 | PASS | Area 3 is the same enforcement table as V-02: `\| Boundary Type \| Template Pattern \| Worked Example \| Enforcement Rationale \|` with 2 rows. Enforcement Rationale cells derive from NHQ-1/NHQ-2 and DQ-3/DQ-4. NHQ-3 is additionally cell-bound via the explicit verbatim instruction, reinforcing the Worked Example cell's constraint. Table format with 2 populated Enforcement Rationale cells: PASS. |
| V-05 | PASS | Area 3 is a 3-row enforcement table (Manifest close-line; Register section header; Register close marker). Three Enforcement Rationale cells derive from DQ-3/DQ-4/IQ-1 (manifest close row), NHQ-1/NHQ-2/IQ-2 (register header row), and IQ-1 (register close row). The Register section header row includes WRONG/CORRECT exemplar pair in Worked Example cell. All three rows carry populated Enforcement Rationale cells naming specific simpler alternatives (bare positional close, bare bold label, positional-only close marker) and their failure modes. Three rows with populated Enforcement Rationale cells: PASS. |

---

### Aspirational Tier Score Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 through C-56 (48 criteria) | PASS | PASS | PASS | PASS | PASS |
| C-57 | PASS | PASS | **FAIL** | PASS | PASS |
| C-58 | **FAIL** | PASS | **FAIL** | PASS | PASS |

Aspirational tier: 50 criteria × 2 pts = 100 pts max
- V-01: -2 (C-58 fail) = 98/100
- V-02: 100/100
- V-03: -4 (C-57, C-58 fail) = 96/100
- V-04: 100/100
- V-05: 100/100

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | / 190 |
|-----------|-----------|-------------|--------------|-------|-------|
| V-01 | 60 | 30 | 98 | **188** | 98.9% |
| V-02 | 60 | 30 | 100 | **190** | 100% |
| V-03 | 60 | 30 | 96 | **186** | 97.9% |
| V-04 | 60 | 30 | 100 | **190** | 100% |
| V-05 | 60 | 30 | 100 | **190** | 100% |

### Ranking

1. **V-02, V-04, V-05** -- 190/190 (tied)
2. **V-01** -- 188/190
3. **V-03** -- 186/190

---

### Differential Analysis

**V-01 vs. V-02 (C-58 isolation):** V-01 carries identical causal grounding (plus NHQ-3, which V-02 lacks) but Area 3 is prose. The enforcement rationale for each template component is embedded in narrative text -- a verifier must parse sub-sections to find it. V-02 makes the same rationale a discrete table cell: independently addressable, impossible to leave blank. The information content is equivalent; the structural addressability is not. C-58 fails on format, not substance.

**V-03 vs. V-01 (C-57 isolation within prose design):** V-03 adds PHASE REGISTER (PQ-1/PQ-2) but removes NHQ-3. Without NHQ-3, the causal phase produces no compound header exemplar. Area 3 can declare the abstract template but has nothing to forward as a worked example. Per-phase vocabulary in Role 2 reinforces lifecycle terminology but does not supply the missing exemplar. Net: V-03 gains lifecycle causal grounding at the cost of the exemplar derivation path, yielding the lowest score.

**V-04 vs. V-02 (dual-path enforcement):** V-04 adds NHQ-3 with explicit cell-binding ("paste the compound header line you authored in NHQ-3 here verbatim"). This creates two independent enforcement paths for C-57: the causal production (NHQ-3 answer) and the schema cell binding (verbatim instruction). V-02 has a single path (blank-blocked Worked Example cell). Both score identically on the v19 rubric because C-57 and C-58 are binary -- the dual-path mechanism is a robustness improvement not captured by a current criterion.

**V-05 vs. V-02/V-04 (three-row enforcement table + inertia framing):** V-05 extends the enforcement table to three rows (adds Register close marker), introduces the INERTIA REGISTER (IQ-1/IQ-2) grounding failure-mode causal reasoning, includes the WRONG/CORRECT exemplar pair in the Worked Example cell, and applies compound descriptors to close markers. All three score 190/190 -- V-05's extensions are qualitatively richer but do not trip additional v19 criteria. They are strong candidates for R20+ promotion.

---

### Excellence Signals (from top-scoring variations)

**Signal 1 -- WRONG/CORRECT exemplar pair in a single table cell (V-05)**
Making the inertia competitor (bare-label form) structurally visible alongside the correct form within the Worked Example cell of the enforcement table. A model reading this cell cannot claim ignorance of the failure mode -- it is present in the schema it authored. The current rubric requires at least one worked exemplar (C-57) but does not require the failure-mode exemplar; V-05 promotes this to a table-cell standard. Candidate criterion: "Schema Area 3 Worked Example cell contains a WRONG/CORRECT pair -- the simpler alternative (inertia state) and the compound form (departure state) both as complete lines in the same cell."

**Signal 2 -- Register close marker as a third enforcement table row type (V-05)**
V-02 and V-04 cover two boundary types (manifest close-line, register section header). V-05 adds the register close marker row, meaning every structural boundary type in the trace document has a corresponding enforcement table row. The Register close marker Worked Example requires a complete compound close marker with accomplishment descriptor. This completes the enforcement table from a boundary-type perspective: open, close, phase-gate are all covered. Candidate criterion: "Schema Area 3 enforcement table covers at least three boundary types: manifest close-line, register section header, and register close marker."

**Signal 3 -- Compound accomplishment descriptor on register close markers (V-05)**
V-05's close markers use the compound form with accomplishment descriptor: "**NULL REGISTER CLOSE** -- Null baseline established", "**INERTIA REGISTER CLOSE** -- Inertia failure modes identified", "**DEPARTURE REGISTER CLOSE** -- Departure contract established". The accomplishment descriptor names what the register established, not just that the register closed. This is the close-marker analogue of C-54's epistemic-function descriptor requirement for headers -- applying the same compound-form standard to close markers. Candidate criterion: "Every named register close marker uses the compound form -- `**[LABEL] CLOSE** -- [accomplishment descriptor]` -- where the descriptor characterizes what the register's completion established."

---

### Scorecard Summary

| Variation | Score | All Essential Pass | Key differentiator |
|-----------|-------|-------------------|-------------------|
| V-01 | 188/190 | Yes | C-58 FAIL -- prose Area 3; strong NHQ-1/2/3 causal structure |
| V-02 | 190/190 | Yes | C-58 PASS -- 2-row enforcement table; clean single-axis design |
| V-03 | 186/190 | Yes | C-57 + C-58 FAIL -- no NHQ-3, prose Area 3; adds lifecycle PQ questions |
| V-04 | 190/190 | Yes | C-58 PASS -- 2-row enforcement table; NHQ-3 cell-bound to table |
| V-05 | 190/190 | Yes | C-58 PASS -- 3-row enforcement table; INERTIA REGISTER; WRONG/CORRECT pair |

```json
{"top_score": 190, "all_essential_pass": true, "new_patterns": ["WRONG/CORRECT exemplar pair in single Worked Example table cell -- inertia competitor (bare-label form) and correct form both present as complete lines in the same cell, making the failure mode structurally visible in the schema artifact rather than described only in Enforcement Rationale prose", "Register close marker as third enforcement table row type -- extends compound-form standard to close markers, covering all three boundary types (manifest close-line, register section header, register close marker) in the enforcement table so no structural boundary is enforced only by two of the three types", "Compound accomplishment descriptor on register close markers -- applying the epistemic-function descriptor pattern to close markers: **[LABEL] CLOSE** -- [accomplishment descriptor] names what the register established rather than marking position only, making close markers departure-from-inertia artifacts rather than positional signals"]}
```
