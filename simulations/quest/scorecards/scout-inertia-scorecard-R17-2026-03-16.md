Now I have everything needed to score. Let me evaluate all 5 variations systematically against the v17 rubric.

---

# scout-inertia — Quest Score R17

**Rubric**: v17 | **Ceiling**: 260 | **New criteria**: A-40 (engineering-register locus noun) + A-41 (architectural-scope TYPE)

---

## Essential Criteria — All Variations

All five variations are template scaffolds. The essential criteria are structural pass/fail based on whether the template contains the structural commands that enforce each criterion.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01: Workaround named specifically | PASS | PASS | PASS | PASS | PASS |
| C-02: Switching cost quantified | PASS | PASS | PASS | PASS | PASS |
| C-03: Inertia threat score declared | PASS | PASS | PASS | PASS | PASS |
| C-04: Defeat conditions identified | PASS | PASS | PASS | PASS | PASS |
| C-05: Failure modes identified | PASS | PASS | PASS | PASS | PASS |

All 5 variations: **essential PASS** — `[C-0N COMMAND]` prompts are present and blockquoted for all five criteria in every variation.

---

## Advanced Criteria — V-01 (STRUCTURAL FAULTS, SECTION 1-7, ALL COMPLETE?)

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| A-08 | FM before DC | PASS | SECTION 1 (FM) precedes SECTION 6 (DC) structurally |
| A-10 | Fail-first declaration | PASS | `## FAIL-FIRST DECLARATION -- THE INERTIA THREAT` is structural first element |
| A-11 | Question-per-criterion (≥3) | PASS | All 5 prompts present |
| A-12 | BRIDGE dual-closure | PASS | Q3 (closes C-05→R-02) and Q4 (closes C-05→C-04) both named with chain refs |
| A-13 | Tabular column schema | PASS | FM table, Q3, Q4, DC table, switching cost all tabular |
| A-14 | FM Inventory as named table | PASS | `SECTION 1 -- THE INERTIA THREAT'S STRUCTURAL FAULTS: FAILURE MODE INVENTORY` |
| A-15 | Trailing completeness checklist | PASS | `SECTION 7 -- COMPLETENESS CHECKLIST` is structurally last |
| A-16 | FM primary key constraint declared | PASS | `**[A-16 PRIMARY KEY RULE]**` in table body |
| A-17 | Question full coverage (all 5) | PASS | C-01 through C-05 all have explicit prompts |
| A-18 | Trailing checklist binary + full | PASS | Y/N column, all 5 criteria present |
| A-19 | Bidirectional referential integrity | PASS | `**[A-19 REFERENTIAL INTEGRITY RULE]**` at DC table |
| A-20 | Inline examples in unit columns | PASS | `(e.g., 2 hours/week)`, `(e.g., 2x/sprint)` in column labels |
| A-21 | Inline falsifiability in DC threshold | PASS | `(e.g., >10MB, >3 failures/week)` in threshold column |
| A-22 | Mid-template bridge completion gate | PASS | `SECTION 2 COMPLETION GATE` positioned between FM and DC |
| A-23 | Criterion ID in rule labels | PASS | `[A-16 PRIMARY KEY RULE]`, `[A-19 REFERENTIAL INTEGRITY RULE]`, `FAIL-FIRST CONSTRAINT [A-31]` all carry IDs |
| A-24 | Dual-type threshold example | PASS | `>10MB` (size) + `>3 failures/week` (frequency) — distinct unit families |
| A-25 | Active command directive on gate | PASS | `[BRIDGE COMPLETION COMMAND]` named label in gate block |
| A-26 | Axis vocab in section headings | PASS | "THE INERTIA THREAT" in FAIL-FIRST heading; "THE INERTIA THREAT'S STRUCTURAL FAULTS:" in FM heading |
| A-27 | Decision-question gate heading | PASS | `SECTION 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` |
| A-28 | Criterion ID in checklist labels | PASS | `C-01:`, `C-02:` through `C-05:` in SECTION 7 items |
| A-29 | Criterion ID in authoring prompts | PASS | `[C-05 COMMAND]`, `[C-01 COMMAND]` etc. present |
| A-30 | COMMAND-register keyword | PASS | All prompt labels use `[C-0N COMMAND]:` form |
| A-31 | Named rule in FAIL-FIRST body | PASS | `FAIL-FIRST CONSTRAINT [A-31]:` in declaration body |
| A-32 | Criterion ID in FAIL-FIRST rule | PASS | `[A-31]` in the rule label |
| A-33 | Artifact class in gate interrogative | PASS | "BRIDGE ARTIFACTS" named in `ALL BRIDGE ARTIFACTS COMPLETE?` |
| A-34 | Failure-context frame in FM heading | PASS | "STRUCTURAL FAULTS" is failure-context frame in subtitle |
| A-35 | Blockquote delimiter on all prompts | PASS | All five `> [C-0N COMMAND]:` prompts use `>` blockquote |
| A-36 | Position index in gate heading name | PASS | `SECTION 2 COMPLETION GATE` carries "SECTION 2" index |
| A-37 | Schema consistency of position index | PASS | SECTION 1-7 throughout; gate uses SECTION 2 — nomenclature consistent |
| A-38 | Compound failure noun | PASS | `STRUCTURAL FAULTS` — TYPE=STRUCTURAL + LOCUS=FAULTS |
| A-39 | Cardinality qualifier in interrogative | PASS | `ALL` is universal quantifier in `ALL BRIDGE ARTIFACTS COMPLETE?` |
| A-40 | Engineering-register locus noun | PASS | `FAULTS` = specific defect planes (fault-taxonomy register) |
| A-41 | Architectural-scope TYPE component | PASS | `STRUCTURAL` = architectural/systemic scope (not event-descriptor) |

**V-01 advanced score**: 32/32 × 5 = **160**
**V-01 total**: 100 + 160 = **260/260**

---

## Advanced Criteria — V-02 (STRUCTURAL FAULTS, STAGE 1-6, ALL COMPLETE?) — Reference Carry

| # | Key differentiators | Result | Evidence |
|---|---------------------|--------|----------|
| A-37 | Schema consistency | PASS | STAGE 1-6 throughout; gate uses `STAGE 2 COMPLETION GATE` — STAGE nomenclature consistent |
| A-40 | Engineering locus | PASS | "THE STATUS QUO'S STRUCTURAL FAULTS" — FAULTS confirmed A-40 source (R16 V-02 scoring note) |
| A-41 | Architectural TYPE | PASS | STRUCTURAL confirmed A-41 source (R16 V-01+V-02 scoring note) |
| A-31/A-32 | FAIL-FIRST rule + ID | PASS | `FAIL-FIRST CONSTRAINT [A-31]:` in body |
| A-16/A-23 | Primary key + ID | PASS | `PRIMARY KEY RULE [A-16]` in STAGE 1 body |
| A-19/A-23 | Citation rule + ID | PASS | `CITATION INTEGRITY RULE [A-19]` at STAGE 5B |
| A-39 | Cardinality | PASS | `ALL BRIDGE ARTIFACTS COMPLETE?` — ALL cardinality |
| A-35 | Blockquotes | PASS | All 5 `> [C-0N COMMAND]:` prompts present |

All 32 advanced criteria PASS — all R16 V-02 criteria carry intact; A-40 and A-41 both met by STRUCTURAL FAULTS on STAGE scaffold.

**V-02 total**: 100 + 160 = **260/260**

---

## Advanced Criteria — V-03 (STRUCTURAL FAULTS, SECTION 1-6, EACH VERIFIED?)

| # | Key differentiators | Result | Evidence |
|---|---------------------|--------|----------|
| A-39 | Cardinality — EACH variant | PASS | `EACH BRIDGE ARTIFACT VERIFIED?` — EACH is a distributive universal quantifier; the interrogative names the artifact class (BRIDGE ARTIFACT) and encodes per-element verification requirement |
| A-40 | Engineering locus | PASS | "THE INERTIA THREAT'S STRUCTURAL FAULTS" in SECTION 1 heading |
| A-41 | Architectural TYPE | PASS | STRUCTURAL in heading |
| A-37 | Schema consistency | PASS | SECTION 1-6 throughout; gate uses `SECTION 2 COMPLETION GATE` |
| A-31/A-32 | FAIL-FIRST rule + ID | PASS | `INERTIA THREAT FAIL-FIRST RULE [A-31]:` — domain-prefix form with [A-31] ID |
| A-16/A-23 | Primary key + ID | PASS | `INERTIA THREAT RULE [A-16]` — domain-prefix form with [A-16] ID |
| A-19/A-23 | Citation rule + ID | PASS | `INERTIA THREAT CITATION RULE [A-19]` — domain-prefix form with [A-19] ID |
| A-35 | Blockquotes | PASS | All 5 per-criterion command prompts blockquoted |

All 32 advanced criteria PASS.

**V-03 total**: 100 + 160 = **260/260**

---

## Advanced Criteria — V-04 (STRUCTURAL FAULTS, STAGE 1-6, BOTH READY?)

| # | Key differentiators | Result | Evidence |
|---|---------------------|--------|----------|
| A-39 | Cardinality — BOTH + READY? | PASS | `BOTH BRIDGE ARTIFACTS READY?` — BOTH is a confirmed dual quantifier; READY? completion verb is A-39-neutral (the criterion evaluates the quantifier + class name, not the verb) |
| A-40/A-41 | STRUCTURAL FAULTS | PASS | "THE INCUMBENT'S STRUCTURAL FAULTS" in STAGE 1 heading |
| A-37 | Schema consistency | PASS | STAGE 1-6 throughout; gate uses `STAGE 2 COMPLETION GATE` |
| A-31/A-32 | FAIL-FIRST rule + ID | PASS | `[A-31 FAIL-FIRST ORDERING RULE]:` in FAIL-FIRST body |
| A-16/A-23 | Primary key + ID | PASS | `[A-16 PRIMARY KEY CONSTRAINT]` in STAGE 1 body |
| A-19/A-23 | Citation rule + ID | PASS | `[A-19 CITATION INTEGRITY CONSTRAINT]` at STAGE 5B |
| A-26 | Axis vocab in headings | PASS | "THE INCUMBENT WORKAROUND" in FAIL-FIRST heading; "THE INCUMBENT'S STRUCTURAL FAULTS:" in STAGE 1 heading |
| A-35 | Blockquotes | PASS | All 5 `> [C-0N COMMAND]:` prompts blockquoted |

All 32 advanced criteria PASS.

**V-04 total**: 100 + 160 = **260/260**

---

## Advanced Criteria — V-05 (STRUCTURAL FAULTS, SECTION 1-6, BOTH BUILT?)

| # | Key differentiators | Result | Evidence |
|---|---------------------|--------|----------|
| A-39 | Cardinality — BOTH + BUILT? | PASS | `BOTH BRIDGE ARTIFACTS BUILT?` — BOTH dual quantifier; BUILT? is A-39-neutral (same as READY?) |
| A-40/A-41 | STRUCTURAL FAULTS | PASS | "THE DEFAULT OPTION'S STRUCTURAL FAULTS" in SECTION 1 heading |
| A-37 | Schema consistency | PASS | SECTION 1-6 throughout; gate uses `SECTION 2 COMPLETION GATE` |
| A-31/A-32 | FAIL-FIRST rule + ID | PASS | `DEFAULT OPTION FAIL-FIRST RULE [A-31]:` in body |
| A-16/A-23 | Primary key + ID | PASS | `DEFAULT OPTION RULE [A-16]` — domain-prefix form |
| A-19/A-23 | Citation rule + ID | PASS | `DEFAULT OPTION CITATION RULE [A-19]` — domain-prefix form |
| A-20/A-21/A-24 | Custom domain examples | PASS | FM table: `(e.g., dataset > 500MB)`, DC threshold: `(e.g., >500MB, >3 skips/week)` — domain-specific examples (not canonical CSV truncation) confirm A-20–A-24 are example-agnostic |
| A-35 | Blockquotes | PASS | All 5 `> [C-0N COMMAND]:` prompts blockquoted |

All 32 advanced criteria PASS.

**V-05 total**: 100 + 160 = **260/260**

---

## Composite Scores

| Variation | Essential | Advanced | Total | Rank |
|-----------|-----------|----------|-------|------|
| V-01 | 100 | 160 | **260/260** | T-1 |
| V-02 | 100 | 160 | **260/260** | T-1 |
| V-03 | 100 | 160 | **260/260** | T-1 |
| V-04 | 100 | 160 | **260/260** | T-1 |
| V-05 | 100 | 160 | **260/260** | T-1 |

All five variations achieve the 260/260 ceiling. The v17 rubric's design prediction was correct: STRUCTURAL FAULTS is the minimal compound noun form satisfying A-40 + A-41 simultaneously, and all five variations carry it.

---

## Excellence Signals

R17 produces four confirmed structural findings:

**1. 260/260 ceiling is scaffold-independent**
V-01 (SECTION 1-7) and V-02 (STAGE 1-6) both achieve 260/260. The A-40+A-41 ceiling is not a STAGE-schema property — it is a compound-noun property. Any scaffold carrying STRUCTURAL FAULTS in the FM Inventory heading achieves it.

**2. Completion-verb space is closed for BOTH cardinality**
V-04 (BOTH READY?) and V-05 (BOTH BUILT?) confirm that A-39 evaluates the cardinality quantifier (BOTH) and artifact class (BRIDGE ARTIFACTS) only — the completion verb is transparent to the criterion. COMPLETE?, VERIFIED?, READY?, BUILT? are all confirmed A-39-neutral. This closes the completion-verb space for BOTH cardinality on both SECTION and STAGE scaffolds.

**3. Domain-prefix rule label pattern is a confirmed A-23-satisfying form**
V-03 (`INERTIA THREAT RULE [A-16]`), V-05 (`DEFAULT OPTION RULE [A-16]`): rule labels that carry domain-vocabulary prefix before the criterion function name satisfy A-23 as long as the criterion ID bracket is present. This pattern achieves axis-vocabulary coherence (A-26) through the rule label itself — the domain prefix propagates the axis subject into the structural layer of the template.

**4. A-20/A-21/A-24 inline example criteria are example-agnostic**
V-05 uses domain-specific inline examples throughout (`dataset > 500MB`, `3x/week`, `>500MB, >3 skips/week`) distinct from the canonical `CSV truncates at 65,536 / >10MB / >3 failures/week` examples in earlier variations. All three format criteria pass. This confirms the criteria evaluate structural co-location of examples with column labels, not the content of the examples.

---

```json
{"top_score": 260, "all_essential_pass": true, "new_patterns": ["260/260 ceiling is scaffold-independent: STRUCTURAL FAULTS achieves A-40+A-41 on both SECTION and STAGE schemas without any scaffold-specific adjustment", "Completion-verb space closed for BOTH cardinality: COMPLETE?, VERIFIED?, READY?, BUILT? are all A-39-neutral — the criterion evaluates the quantifier and artifact class only, not the verb", "Domain-prefix rule label pattern is a confirmed A-23-satisfying form: labels such as DEFAULT OPTION RULE [A-16] propagate axis vocabulary into the structural rule layer while satisfying criterion-ID traceability", "A-20/A-21/A-24 inline example criteria are example-agnostic: domain-specific examples satisfy the criteria identically to canonical examples — structural co-location is the criterion, not example content"]}
```
