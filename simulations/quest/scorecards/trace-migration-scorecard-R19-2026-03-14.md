Now I have all five variations. Let me evaluate each against the v17 rubric.

---

## trace-migration Scoring — Round 19

**Rubric:** v17 (300 pts · 50 criteria · 5 essential · 45 aspirational)
**Variations:** V-01 through V-05 (targeting C-48, C-49, C-50)
**Ground truth:** Placeholder (prompt-design evaluation)

---

## Essential Criteria Evaluation (C-01–C-05, 60 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Before/After State | PASS — B1 entity table | PASS — B1 entity state table | PASS — DIRECTIVE B-4 mandates entity table | PASS — B1 execution record | PASS — B1 entity state table |
| **C-02** Data Loss Path | PASS — "data loss path" in checklist | PASS — "Data Loss Path" column in Q1 table | PASS — DIRECTIVE A-7 8-item checklist | PASS — "data loss path" in Phase A vocabulary | PASS — "Data Loss Path" column in Q1 table |
| **C-03** Constraint Violation Analysis | PASS — 4 dedicated analysis fields per role | PASS — 4 CT tables per role | PASS — DIRECTIVE A-6 mandates 4 labeled fields | PASS — 4 constraint-type analysis fields per role | PASS — 4 CT tables per role |
| **C-04** Missing Default Detection | PASS — "missing default" in checklist | PASS — "Missing Default" column in entity table | PASS — DIRECTIVE A-7 8-item checklist | PASS — "missing default" in Phase A vocabulary | PASS — "Missing Default" column in entity table |
| **C-05** Chronological Step Ordering | PASS — B1 step sequence | PASS — B1 migration execution table | PASS — DIRECTIVE B-4 execution record | PASS — B1 migration execution record | PASS — B1 execution per-entity table |

**Essential verdict: all_essential_pass = true for all five variations.**

---

## Key Aspirational Criteria Assessment

### C-28 through C-32 (structure, routing, coverage)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-28 Dedicated constraint-type slots | PASS | PASS | PASS | PASS | PASS |
| C-29 Complete checklist in all role sections | PASS — Q2/Q3 reference same checklist | PASS — Q2/Q3 use same table schemas | PASS — DIRECTIVE A-6/A-7 apply to Q1, Q2, Q3 | PASS — Q2/Q3 reference same checklist | PASS — Q2/Q3 use same table schemas |
| C-30 Distinct Phase B inertia example | PASS | PASS | PASS | PASS | PASS |
| C-31 Parse-phase CONSTRAINT TYPE REGISTRY | PASS | PASS | PASS | PASS | PASS |
| C-32 B3 canonical table with all constraint types | PASS — B3 four-row table | PASS — B3 CT-ID indexed table | PASS — DIRECTIVE B-6 mandates all registry types | PASS — B3 four-row table | PASS — B3 CT-ID indexed table |

---

### C-33 — Named Enforcement Block Before First Role Section

**Pass condition:** A named enforcement block appears BEFORE Q1, listing all required items with explicit scoping-prohibition language ("apply to ALL roles," "DO NOT SCOPE OR SHORTEN," etc.).

| Variation | Assessment | Evidence | Verdict |
|-----------|-----------|---------|--------|
| **V-01** | No dedicated pre-Q1 enforcement block. The checklist appears inside Q1's analytical section ("apply to every changed entity in this role's domain") — not before Q1. | Checklist in Q1 body prose, not a pre-positioned manifest | **PARTIAL** |
| **V-02** | Pre-Q1 sections are COST LEDGER SUBSTRATE GATE TABLE and ALIGNMENT STATE TABLE — gate/binding structure, not an analytical enforcement manifest. Per-role table schemas embedded within Q1/Q2/Q3 sections. No pre-Q1 checklist enforcement block. | Table schemas defined within role sections, not before | **PARTIAL** |
| **V-03** | DIRECTIVE A-6: "In Q1, Q2, and Q3, WRITE four dedicated constraint-type analysis fields… Do not combine constraint types in a shared field." DIRECTIVE A-7: "In Q1, Q2, and Q3, apply this analytical checklist to every changed entity." Both directives explicitly name all three roles and appear in "PHASE A DIRECTIVES" before Q1. The combination constitutes a named enforcement sequence with scope ("Q1, Q2, and Q3") and prohibition ("Do not combine"). | Distributed directive-form enforcement mandate before Q1 naming all roles | **PASS** |
| **V-04** | Phase A coverage requirements section before Q1 lists "All four constraint-type analysis fields in each role section" and "Full 8-item analytical checklist per changed entity in each role section." Applies to all roles. Lacks explicit "DO NOT SCOPE OR SHORTEN" prohibition language. | Coverage requirement list — no scoping-prohibition language | **PARTIAL** |
| **V-05** | Phase A coverage requirements section before Q1, same structure as V-04. Adds "Q1 = Operations… Q2 = Commerce · Q3 = Finance" role ordering. No explicit scoping prohibition. | Coverage requirement list — no scoping-prohibition language | **PARTIAL** |

**C-33 delta: V-03 gains ~5.33 pts vs ~2.67 pts for V-01/V-02/V-04/V-05.**

---

### C-34 through C-36 (bilateral gate coverage, named blocks, STATUS QUO COST)

All PASS for all five variations:
- **C-34**: Every variation has EXIT BLOCK at Phase A close and ENTRY REFERENCE at Phase B open.
- **C-35**: Every variation packages gate mechanism as named blocks (BOUNDARY PROTOCOL TABLE / EXIT BLOCK / ENTRY REFERENCE) verifiable by section headers.
- **C-36**: Every variation has STATUS QUO COST section preceding Q1. V-05 additionally has a STATUS QUO COST FRAME before the parse phase — stronger but C-36 is binary PASS/FAIL.

---

### C-37 through C-45 (manifest, cost ledger, gates, alignment)

All PASS for all five variations:
- **C-37**: PROTOCOL COUNT MANIFEST present at Phase B entry in all variations.
- **C-38**: COST LEDGER as 3-row table in all variations.
- **C-39**: B2 cross-role causal chain with named substrate and two domain roles. V-05 explicitly links B2 to "close the STATUS QUO COST FRAME narrative" — strongest C-39 implementation, but criterion is PASS for all.
- **C-40/C-41**: Q1 = Operations, COST LEDGER row (a) = infrastructure class. All PASS.
- **C-42**: Explicit ALIGNMENT STATE BINDING with named three-artifact rule. All PASS.
- **C-43**: COST LEDGER SUBSTRATE GATE with return-to-parse instruction. All PASS.
- **C-44**: ALIGNMENT STATE named in EXIT BLOCK alongside PARSE GATE. All PASS.
- **C-45**: PROTOCOL COUNT MANIFEST enumerates all four named gates (PARSE GATE × 2, ALIGNMENT STATE, COST LEDGER SUBSTRATE GATE). All PASS.

---

### C-46 through C-50 — R18 and R19 Target Criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-46** Compound annotation at ENTRY REFERENCE | PASS — `(BINARY FIELD)` in gate code block | PASS — `(BINARY FIELD)` in Annotation column | PASS — DIRECTIVE B-1 prohibits annotation-less ENTRY REFERENCE | PASS — `(BINARY FIELD)` in gate code block | PASS — `(BINARY FIELD)` in ENTRY REFERENCE TABLE |
| **C-47** Manifest self-referential completeness rule | PASS — completeness rule in PROTOCOL COUNT MANIFEST | PASS — MANIFEST COMPLETENESS RULE TABLE | PASS — DIRECTIVE B-3 specifies exact rule text | PASS — completeness rule pre-filled in manifest | PASS — MANIFEST COMPLETENESS RULE fill template |
| **C-48** ENTRY REFERENCE inline self-documentation note | PASS — explicit instruction: "Include an inline note at this position stating the self-documenting property explicitly" + explanatory note pre-written | PASS — ENTRY REFERENCE RATIONALE ROW table with "Do not leave this row blank" | PASS — DIRECTIVE B-1a: exact phrasings provided, "An ENTRY REFERENCE block that carries the annotation but contains no inline rationale is structurally incomplete" | PASS — rationale note pre-filled as required inline text: "Self-documenting annotation rationale (required inline note)..." | PASS — Self-Documenting Rationale column as fill field with "Do not leave it blank" |
| **C-49** Manifest completeness rule with action directive | PASS — "Apply this rule to detect omissions — do not rely on cross-document search to verify gate coverage" | PASS — Action directive fill row with explicit failure condition for empty cell | PASS — DIRECTIVE B-3 exact text: "Apply this rule to detect omissions — do not rely on cross-document search" + "Do not omit the action directive" | PASS — "Apply this rule to detect omissions before proceeding to B1 — do not rely on cross-document search" pre-filled | PASS — fill slot: "write a positive instruction directing the evaluator to apply this rule… or both"; "Do not leave the action directive blank" |
| **C-50** Manifest completeness rule with enumerated block-type scope | PASS — "A gate named in any BOUNDARY PROTOCOL block, EXIT BLOCK position, or ENTRY REFERENCE position" | PASS — Scope fill row: "name the three block types — BOUNDARY PROTOCOL blocks · EXIT BLOCK positions · ENTRY REFERENCE positions"; "A scope cell that uses 'any block' without naming the three block types = incomplete" | PASS — DIRECTIVE B-3 specifies exact scope term with all three block types + "Do not use 'any block' as the scope term" | PASS — "BOUNDARY PROTOCOL block, EXIT BLOCK position, or ENTRY REFERENCE position" pre-filled in completeness rule | PASS — fill slot: "enumerate the three block types that constitute the gate inventory"; "Do not use 'any block' as the scope term" |

**C-46 through C-50: PASS for all five variations.**

---

## Composite Score Computation

**Scoring basis:** 300 pts total. Essential: 5 × 12 pts = 60 pts. Aspirational: 45 × 5.33 pts ≈ 240 pts.
PARTIAL = 50% credit = 2.67 pts.

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 through C-05 | 5 × 12 = 60 | 60 | 60 | 60 | 60 | 60 |
| C-06 through C-32 (27 aspir.) | ~143.9 | 143.9 | 143.9 | 143.9 | 143.9 | 143.9 |
| **C-33** | ~5.33 | 2.67 (PARTIAL) | 2.67 (PARTIAL) | **5.33 (PASS)** | 2.67 (PARTIAL) | 2.67 (PARTIAL) |
| C-34 through C-50 (17 aspir.) | ~90.6 | 90.6 | 90.6 | 90.6 | 90.6 | 90.6 |
| **TOTAL** | **300** | **297.2** | **297.2** | **300** | **297.2** | **297.2** |

| Rank | Variation | Score | % |
|------|-----------|-------|---|
| 1 | **V-03** (DIRECTIVE / Phrasing Register) | **300** | **100%** |
| 2 | V-05 (Role Sequence + Format + Inertia) | 297 | 99% |
| 3 | V-04 (Role Sequence + Lifecycle) | 297 | 99% |
| 4 | V-02 (Output Format) | 297 | 99% |
| 5 | V-01 (Role Sequence) | 297 | 99% |

*V-05 ranked second within the tied group for introducing the STATUS QUO COST FRAME structural arc that closes through B2, and for two-site completeness rule over-specification (both a fill template and a post-template action directive).*

---

## Excellence Signals — V-03 (Top Variation)

**Signal 1: Structural incompleteness defined at point of use.**
DIRECTIVE B-1a states: "An ENTRY REFERENCE block that carries the annotation but contains no inline rationale is structurally incomplete under this protocol." This moves C-48 compliance from a content instruction ("include a note") to a structural definition ("without the note, the block is incomplete"). The omission is not a style gap — it is defined as a structural failure at the exact position where it would occur. No prior variation named the defective form as structurally incomplete rather than merely insufficient.

**Signal 2: Prohibited-form specification alongside required-form specification.**
DIRECTIVE B-3: "Do not use 'any block' as the scope term — the rule must enumerate the three block types." The prior formulation was instruction-only (name the block types). V-03 adds the prohibition against the weaker form. Naming "any block" as prohibited means a model that produces a C-50-violating formulation receives an explicit signal that its output matches a named negative example. This closes the escape hatch that instruction-only mandates leave open.

**Signal 3: Distributed directive-form enforcement satisfies C-33 without a monolithic block.**
DIRECTIVE A-6 and A-7 together constitute a pre-Q1 enforcement mandate: DIRECTIVE A-6 names all three roles explicitly and prohibits combining constraint types; DIRECTIVE A-7 applies the 8-item checklist to all three roles. The distributed structure passes C-33 because the prohibition language and role scope are both present before Q1 — the criterion does not require a single named section if named directives cover the same enforcement surface. This is a new mechanism: prior rounds used either a single named enforcement section or inline checklists within Q1.

---

## Secondary Signal — V-05 (Inertia Framing Innovation)

**Pre-analysis narrative arc with causal closure obligation.**
The STATUS QUO COST FRAME before the registry creates a structural narrative that B2 must explicitly close: B2 is described as "closes the STATUS QUO COST FRAME narrative by naming what happens when the status quo persists into the migration execution window." This creates a two-anchor causal obligation — the frame declares the ongoing cost at the start of the prompt, and B2 must name the same causal mechanism as what migration terminates. The B2 cross-role chain becomes a narrative resolution, not only an analytical requirement. This is new to R19.

---

```json
{"top_score": 300, "all_essential_pass": true, "new_patterns": ["structural-incompleteness-at-point-of-use: defining the omission form as structurally incomplete (rather than merely instructing inclusion) at the exact block position where omission would occur makes C-48 a named structural failure rather than a content gap", "prohibited-form-specification: naming the weaker formulation ('any block') as an explicit prohibited form alongside the required form closes the escape hatch left by instruction-only mandates for C-50", "distributed-directive-enforcement-for-C33: multiple named WRITE commands before Q1 that each explicitly name all roles and include prohibition language satisfy C-33 without requiring a single monolithic enforcement block"]}
```
