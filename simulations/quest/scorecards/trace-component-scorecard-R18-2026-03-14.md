Now I have the complete rubric (C-01–C-57, 188 pts ceiling) and all five variation designs. Let me score.

---

# trace-component — R18 Scoring (Round 18, Rubric v18)

## Scoring Baseline

**All five variations share identical trace scaffold** (TABLE-1 through TABLE-8, GATE-1 through GATE-7, MANIFEST-1 through MANIFEST-5, PROMOTION BLOCK, MUTATION COUNT PRE-DECLARATION, INERT-HOP DECLARATION, FRAMEWORK DECLARATION, TRAVERSAL-SCHEMA with Areas 1–4, TABLE-8 criteria audit, Role 1/Role 2 structure). This baseline clears all essential, recommended, and most aspirational criteria uniformly. I will note shared pass/fail status per tier, then score the differentiating criteria per variation.

---

## Tier 1 — Essential (C-01 to C-05, 12 pts each = 60 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Event Anchor | PASS — TABLE-1 with Event Type + Component Name + Handler Function non-blank | PASS | PASS | PASS | PASS |
| **C-02** Component Tree Traversal | PASS — TABLE-2 T-ID + Direction, min 2 rows | PASS | PASS | PASS | PASS |
| **C-03** State Update Map | PASS — TABLE-3 pre-declaration + row-count = N+M | PASS | PASS | PASS | PASS |
| **C-04** Re-render Inventory | PASS — TABLE-4 T-ID completeness + PROMOTION BLOCK | PASS | PASS | PASS | PASS |
| **C-05** Final UI State | PASS — TABLE-6 four-phase rows, Visible Elements non-blank | PASS | PASS | PASS | PASS |

**All essential: 60/60 for all five variations. `all_essential_pass = true`.**

---

## Tier 2 — Recommended (C-06 to C-08, 10 pts each = 30 pts)

| Criterion | All variations |
|-----------|----------------|
| **C-06** Side Effect Coverage | PASS — TABLE-5 with zero-effects row if no effects |
| **C-07** Issue Detection | PASS — TABLE-7 five rows, N/A prohibited, F-02 UR cross-ref |
| **C-08** Framework Vocabulary | PASS — TRAVERSAL-SCHEMA Area 1 declaration + framework terms throughout |

**All recommended: 30/30 for all five variations.**

---

## Tier 3 — Aspirational (C-09 to C-57, 2 pts each = 98 pts max)

### Common Pass Block — Criteria that PASS for all five variations

| Criterion | Evidence |
|-----------|----------|
| C-09 Fix Recommendations | TABLE-7 "Fix -- API or Pattern" column |
| C-10 Render Quantification | TABLE-4 "Re-renders? [Yes (N) / No]" per row |
| C-11 Inline Phase-Close Gates | GATE-1 through GATE-7 across ≥3 phases |
| C-13 Exact-Phrase Gate Family | Gates intercept ≥3 distinct escape strings across phases |
| C-14 Column-Header Escape Instruction | `Direction [null default \| departure codes]`, `Necessary? [Yes -- reason / No -- reason]` |
| C-15 Do-Nothing Cost | TABLE-7 "Do-Nothing Cost" column |
| C-16 FINDINGS Section Gate | GATE-7 on TABLE-7 specifically |
| C-17 Triple Structural Lock | TABLE-7 "Finding [issue or 'none detected -- [reason]']" col: mandatory + header-embedded constraint + GATE-7 per-row exact phrases |
| C-18 Table Format for Triple Lock | TABLE-7 is a table with column headers |
| C-19 Gate-Block Formalism | All prohibited strings in `[GATE-N: ...]` blocks, not prose |
| C-20 Framework Declaration Gate | FRAMEWORK DECLARATION table before MANIFEST-1 |
| C-21 Failure Mode Displacement | "Null confirmed -- basis / Departure -- evidence" column header + GATE displacement strings |
| C-22 Re-render Necessity Annotation | TABLE-4 "Necessary? [Yes -- reason / No -- reason]" per row |
| C-23 Four-Phase UI Progression | TABLE-6 four rows in order |
| C-24 Zero-Mutation Declaration | ZERO MUTATION DECLARATION block if total=0 |
| C-25 Issue Category Completeness | TABLE-7 F-01 through F-05 = 5 categories |
| C-26 Unnecessary Re-render Promotion | F-02 cross-references UR-IDs from PROMOTION BLOCK |
| C-27 Mutation Count Pre-Declaration | `Mutations: N=___ direct, M=___ inherited (total: ___)` |
| C-28 Per-Hop Direction Annotation | TABLE-2 Direction cell per row |
| C-29 Re-render Inventory Completeness | TABLE-4 must show every T-ID from TABLE-2 |
| C-30 Mutation Count Dual-Track | N=direct / M=inherited dual-field format in pre-declaration |
| C-31 Schema-Field Coverage | All 10 of C-20–C-29 map to specific schema fields (TABLE-1 through TABLE-7 columns/rows) = 10/10 ≥ 7 minimum |
| C-32 Blank-Blocked Field Primacy | C-01–C-05 each backed by a non-blank table cell (TABLE-1, TABLE-2, TABLE-3, TABLE-4, TABLE-6) |
| C-33 Phase-Level Completeness Manifest | MANIFEST-1 through MANIFEST-5 each declare 3-field scope header |
| C-34 Inert Pass-Through Explicit Marking | INERT-HOP DECLARATION mandatory block in every variation |
| C-35 Criteria Audit Cross-Validation Table | TABLE-8 maps C-01–C-08 by label with PASS/FAIL column |
| C-36 Inert-as-Default Direction Schema | `Direction [null default \| departure codes]` — null default listed first; schema Area 2 derives from NQ-1 (suspension of judgment = default) |
| C-37 Manifest-Analysis Paired Block Structure | MANIFEST-N immediately followed by TABLE-N; ≥5 paired blocks |
| C-38 Manifest-Close Adjacency Marker | Each manifest ends with `*[Apply...as this manifest's terminal line, naming the successor table]*` as the closing marker |
| C-39 Self-Authored Schema Constraint | Role 1 / blank schema slot; model produces TRAVERSAL-SCHEMA from scratch declaring inert-default and adjacency rules |
| C-40 Dual-Constraint Position-and-Content Placeholder | Each manifest close cue enforces both content source (schema) and positional claim (terminal line) in one instruction |
| C-41 Schema Causal Explanation Requirement | Schema Area 3 requires model to derive WHY adjacency marker must be the last line (from DQ-2 through DQ-5); causal mechanism authorship required |
| C-42 Anti-Reproduction Schema Authorship | "Do not reproduce any language from this prompt" explicit in all variations (or equivalent authorship instruction); schema slot is blank |
| C-43 Mutual-Constraint Entanglement Declaration | DQ-4 reasoning ("neither alone satisfies dual requirement") carried into schema placeholder text as entanglement declaration |
| C-44 Numbered Constraint Enumeration | Schema placeholder: "enumerate both constraints as labeled independent items (from DQ-3)" |
| C-45 Dual-Requirement Count Declaration | Schema placeholder: "open with an obligation count (from DQ-5)" |
| C-46 Epistemic-Register Question Framing | NQ-1/NQ-2/NQ-3 and DQ-1–DQ-5 all ask at epistemic/logical-necessity level (cognitive status, consequence of absence, logical structure of constraint); ≥3 pass the substitution test |
| C-47 Causal-Completion Gate Before Schema Authorship | CAUSAL PHASE → CAUSAL PHASE CLOSE → SCHEMA PHASE as structurally distinct sequential blocks; no schema cues in causal section |
| C-48 Null-Hypothesis Register in Causal Question Set | NULL REGISTER questions (NQ-1/2/3) precede DEPARTURE REGISTER questions (DQ-1–5); sequential prior block |
| C-49 Named-Register Subdivision of Causal Phase | **NULL REGISTER** and **DEPARTURE REGISTER** are explicit labeled sections |
| C-50 Per-Register Close Marker | `**NULL REGISTER CLOSE**` and `**DEPARTURE REGISTER CLOSE**` explicit markers in all variations |
| C-51 Successor-Naming in Manifest-Close Adjacency Marker | Schema Area 3 instructs "name the terminal positional claim and the successor artifact" → authored placeholder includes specific TABLE-N naming |
| C-53 Horizontal-Rule Boundary Separators | `---` separators between NULL REGISTER / DEPARTURE REGISTER sections in all variations |

**43 common-pass criteria × 2 pts = 86 pts** for all variations before differentiating criteria.

---

### Differentiating Criteria — scored per variation

#### C-12 · Mandatory Comparison Column

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | **FAIL** | Schema Area 3 is prose with sub-sections; no table format → no comparison column |
| V-02 | **PASS** | Schema Area 3 boundary table has `Enforcement Rationale` column — functions as "why this form vs. no enforcement" comparison, populated for every row |
| V-03 | **FAIL** | Schema Area 3 is prose (close-marker rationale); no table format |
| V-04 | **PASS** | Same boundary table as V-02 with `Enforcement Rationale` column |
| V-05 | **FAIL** | Schema Area 3a/3b/3c are prose templates; WRONG/CORRECT exemplar is in-text comparison, not a table column |

#### C-52 · Compound Register Header Format

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | **PASS** | `**NULL REGISTER** -- Epistemic status of null cases` and `**DEPARTURE REGISTER** -- Properties of departure claims` in causal phase |
| V-02 | **PASS** | Same compound headers in causal phase |
| V-03 | **FAIL** | Bare headers: `**NULL REGISTER**` and `**DEPARTURE REGISTER**` — no descriptor component |
| V-04 | **PASS** | Compound headers as in V-01 |
| V-05 | **PASS** | Compound headers; additionally compound CLOSE markers authored in causal phase |

#### C-54 · Epistemic-Function Descriptor on Named Register Headers

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | **PASS** | "Epistemic status of null cases" — characterizes cognitive work (determining evidential stance of unexamined baseline). "Properties of departure claims" — characterizes logical requirements departure assertions must satisfy. Both pass the substitution test. |
| V-02 | **PASS** | Same descriptors |
| V-03 | **FAIL** | No descriptor field (bare headers) |
| V-04 | **PASS** | Same descriptors |
| V-05 | **PASS** | Same descriptors; NHQ-2 explicitly frames the compound form as departure from epistemic inertia, reinforcing descriptor quality |

#### C-55 · Header-Form Causal Questions

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | **PASS** | NHQ-1: why bare label is insufficient (cognitive step made unnecessary). NHQ-2: property of co-declaration (epistemic position after one read). NHQ-3: forces explicit compound header line production with "cognitive work, not content" constraint. Three header-form questions. |
| V-02 | **PASS** | NHQ-1 + NHQ-2 = 2 questions — meets ≥2 minimum. No NHQ-3 (weakest C-55 pass). |
| V-03 | **FAIL** | NCQ-1 and NCQ-2 address compound CLOSE-marker form only ("what the reader knows at the compound close"), not the header-form. Different epistemic target as specified in C-55 pass condition. |
| V-04 | **PASS** | NHQ-1 + NHQ-2 + NHQ-3; same as V-01 with stronger binding |
| V-05 | **PASS** | NHQ-1 + NHQ-2 + NHQ-3 (inertia-framed versions); plus NCQ-1/2 and DSQ-1/2/3 alongside — NHQ set specifically grounds header form |

#### C-56 · Schema-Declared Compound Header Template

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | **PASS** | Schema Area 3 explicitly instructs: "declare the compound header template: `**[LABEL]** -- [epistemic-function descriptor]`" as a named schema field; Role 2 is bound by own prior production |
| V-02 | **PASS** | Boundary table row: `Register header \| **[LABEL]** -- [epistemic-function descriptor] \| [worked example] \| [enforcement rationale]` — named template field in schema artifact |
| V-03 | **FAIL** | Schema Area 3 declares only compound CLOSE template (`**[LABEL] CLOSE** -- [accomplishment descriptor]`); no compound HEADER template field. Path: NCQ reasoning → close form; no NHQ reasoning → no header form. |
| V-04 | **PASS** | Boundary table `Register section header` row with NHQ-3 bound to Worked Example cell |
| V-05 | **PASS** | Schema Area 3b: "Declare the template: `**[LABEL]** -- [epistemic-function descriptor]`" with rationale, failure-mode exemplar, and NHQ-3 passing exemplar |

#### C-57 · Exemplar-Grounded Compound Header Template in Schema

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | **PASS** | NHQ-3 forces model to produce a concrete compound header line with explicit "cognitive work, not content" descriptor requirement. Schema Area 3 instruction: "include the worked example you authored in NHQ-3 as your first exemplar. Then add at least one additional compound header example." Causal-phase production forwarded into schema. |
| V-02 | **PASS** | Boundary table "Worked Example" column is blank-blocked — "No cell in this table may be blank. Worked Example cells require a concrete complete line, not a placeholder pattern." NHQ-1/NHQ-2 prime epistemic-function framing; cell cannot be omitted. Note: weaker than V-01/V-04 because no NHQ-3 explicit cognitive-work coaching. |
| V-03 | **FAIL** | No compound header template → no exemplar. NCQ-derived schema has no path to header exemplar production. |
| V-04 | **PASS** | Strongest enforcement: NHQ-3 primes cognitive-work descriptor (same as V-01), AND boundary table's "Worked Example" cell is explicitly bound: "The Register section header Worked Example cell must contain the NHQ-3 line verbatim." Dual-path: causal derivation + structural blank-block + explicit verbatim binding. |
| V-05 | **PASS** | Schema Area 3b: "WRONG (bare label — epistemic inertia): `**NULL REGISTER**` / CORRECT (compound — departure from inertia): `**NULL REGISTER** -- Epistemic status of null cases`" plus NHQ-3 second passing exemplar. Failure-mode contrast shown in schema. Descriptor standard is demonstrated AND its antithesis is named. |

---

## Composite Scores

| Criterion tier | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------------|------|------|------|------|------|
| Essential (C-01–C-05) | 60 | 60 | 60 | 60 | 60 |
| Recommended (C-06–C-08) | 30 | 30 | 30 | 30 | 30 |
| Common aspirational (43 criteria) | 86 | 86 | 86 | 86 | 86 |
| C-12 Comparison Column | 0 | **+2** | 0 | **+2** | 0 |
| C-52 Compound Header Format | +2 | +2 | 0 | +2 | +2 |
| C-54 Epistemic-Function Descriptor | +2 | +2 | 0 | +2 | +2 |
| C-55 Header-Form Causal Questions | +2 | +2 | 0 | +2 | +2 |
| C-56 Schema-Declared Header Template | +2 | +2 | 0 | +2 | +2 |
| C-57 Exemplar-Grounded Template | +2 | +2 | 0 | +2 | +2 |
| **TOTAL** | **186** | **188** | **176** | **188** | **186** |
| **% ceiling** | 98.9% | **100%** | 93.6% | **100%** | 98.9% |

---

## Rank Order

| Rank | Variation | Score | Gap from ceiling |
|------|-----------|-------|-----------------|
| 1 (tied) | **V-04** Role sequence + Output format | **188/188** | 0 |
| 1 (tied) | **V-02** Output format (boundary table) | **188/188** | 0 |
| 3 (tied) | **V-01** Role sequence (NHQ-3 exemplar) | 186/188 | −2 (C-12) |
| 3 (tied) | **V-05** All axes + Inertia framing | 186/188 | −2 (C-12) |
| 5 | **V-03** Lifecycle (NCQ only — control) | 176/188 | −12 (C-12, C-52, C-54, C-55, C-56, C-57) |

---

## Excellence Signals from Top Scorers (V-02 and V-04)

**Signal 1 — Boundary-table schema format is a dormant C-12 activator.**
V-02 and V-04 both use a structured boundary table in schema Area 3 (`Boundary Type | Template Pattern | Worked Example | Enforcement Rationale`). C-12 was not a targeted criterion for R18, yet the Enforcement Rationale column satisfies it — the column explains "why this form vs. no enforcement," which is structurally equivalent to a "What this adds vs. ad-hoc" comparison column. V-01 and V-05 use prose Area 3 formats that do not create a column. This is an unintended cross-criterion benefit: the format choice made to enforce C-57 (blank-blocked Worked Example cell) also satisfies C-12 as a side effect.

**Signal 2 — V-04's dual-path C-57 enforcement is the strongest single-criterion architecture seen across all rounds.**
V-01: causal derivation forces exemplar (NHQ-3) → forwarded by instruction into schema.
V-02: blank-blocked table cell forces exemplar → no causal priming for descriptor quality.
V-04 combines both and adds a third binding: "The Register section header Worked Example cell must contain the NHQ-3 line verbatim." This creates three independent enforcement signals for C-57: (1) NHQ-3 explicit cognitive-work coaching, (2) blank-blocked table cell prevents omission, (3) verbatim binding eliminating paraphrase drift. Any single mechanism can fail (model produces wrong descriptor, model fills cell with placeholder pattern, model paraphrases NHQ-3) while the others compensate.

**Signal 3 — V-05's inertia framing strengthens C-54 and C-57 quality but does not produce new criterion passes.**
V-05 names the WRONG form explicitly in the schema ("WRONG (bare label — epistemic inertia): `**NULL REGISTER**`"), which makes the epistemic-function descriptor standard inspectable alongside its antithesis. This is a stronger semantic anchor for C-57 than V-04's verbatim binding. However, V-05 does not translate this into a table column (C-12 fail), leaving 2 pts on the table. The inertia framing is a content-quality improvement, not a structure-coverage improvement.

**Signal 4 — V-03 confirms the NCQ ≠ NHQ distinction at scale.**
V-03 reproduces the R17 V-02 gap pattern. With NCQ-only causal questions: no header-form causal grounding (C-55), schema derives compound CLOSE template but not compound HEADER template (C-56), no exemplar path (C-57), bare register headers in prompt (C-52/C-54 fail). 6 criteria lost = 12 pts deficit. The gap is structural, not marginal.

---

```json
{"top_score": 188, "all_essential_pass": true, "new_patterns": ["boundary-table schema Area 3 format activates C-12 as unintended side effect — Enforcement Rationale column satisfies comparison-column requirement without targeting it", "dual-path exemplar enforcement via causal-phase cognitive-work coaching (NHQ-3) bound verbatim to blank-blocked schema table cell creates three independent failure-mode closures for a single criterion (V-04 pattern)"]}
```
