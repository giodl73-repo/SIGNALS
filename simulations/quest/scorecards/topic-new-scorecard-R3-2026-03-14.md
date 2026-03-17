# topic-new R3 Scorecard

## Summary

| Rank | Variation | Composite | Aspirational | Fails |
|------|-----------|-----------|--------------|-------|
| 1 | **V-05** | **100** | 8/8 | -- |
| 2 | V-01 | 97.5 | 6/8 | C-15, C-16 |
| 3 | V-02 | 97.5 | 6/8 | C-15, C-16 |
| 4 | V-03 | 97.5 | 6/8 | C-14, C-16 |
| 5 | V-04 | 97.5 | 6/8 | C-15, C-16 |

All five variations pass all 5 essential and all 3 recommended criteria. The score separates entirely on C-14 + C-15 + C-16.

## R3 Diagnostic

The hypothesis is confirmed. The failure pattern is diagnostic:

- **V-01/V-02/V-04** pass C-14 (consequence framing structural) but fail C-15 (no stakeholder-risk opener) → 97.5
- **V-03** passes C-15 (fill-in opener) but fails C-14 (Namespace/Skill/Item name column headers have no consequence framing) → 97.5
- **V-05** passes both → C-16 follows → 100

C-16 is a dependent criterion: it passes if and only if C-14 and C-15 are both structurally enforced. Satisfying only one of C-14/C-15 is not sufficient — the ceiling requires both.

## New Patterns

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["mandatory fill-in opener enforces C-15 structurally -- making the stakeholder-risk section an active output production step (not a static paragraph) derives role differentiation from the model's own first output rather than imposing it via a late checklist", "schema separation as constraint registry -- FIELD SCHEMA and COVERAGE SCHEMA with Consequence columns create a two-tier structure where every constraint has exactly one structural home and pre-write gate checkboxes cite schema rows by reference, making C-14 + C-16 co-satisfiable in one compact structure"]}
```
02 Correct path | PASS | STEP 4: "Write simulations/{topic}/strategy.md:" |
| C-03 All five fields | PASS | Signal plan table has all five columns; column header row lists all five |
| C-04 Valid priority vocab | PASS | Column header: "Priority (essential/recommended/optional -- any other value: strategy treated as advisory-only, commit gate logic fails)" |
| C-05 At least one essential | PASS | Pre-write gate: ">=1 signal marked essential -- zero essential: gate has no blocking condition, strategy is invalid" |
| C-06 Multi-namespace coverage | PASS | Pre-write gate: ">=2 distinct namespaces -- single namespace: investigation blind to other signal dimensions" |
| C-07 Narrative rationale | PASS | STEP 4 template: "## Rationale [2-4 sentences: what assumption is the team relying on?...]" |
| C-08 Differentiated roles | PASS | Pre-write gate: ">=2 distinct owner roles -- single role: single-perspective risk, cross-functional gaps undetected" |
| C-09 Commit gate defined | PASS | "## Commit Gate / Design commit is permitted when: [minimum signal set, as a testable condition -- not 'enough evidence gathered']" |
| C-10 Naming convention | PASS | "## Naming Reference / All item names in this strategy follow: {topic}-{slug}-{date}.md" |
| C-11 Checkbox-gate before transition | PASS | Five-item pre-write gate with checkbox syntax before STEP 4: "Do not proceed to STEP 4 until all five checks pass." |
| C-12 Invalid vocab = operational consequence | PASS | Column header: "any other value: strategy treated as advisory-only, commit gate logic fails" -- consequence is structural loss of gating function |
| C-13 Dedicated sections per aspiration | PASS | "## Commit Gate" and "## Naming Reference" are dedicated named sections in the strategy template |
| C-14 Pervasive consequence framing | PASS | All five column headers carry their deviation consequence (unroutable / no execution path / missed lookup / no accountability / advisory-only). Pre-write gate items carry inline consequences. Every enforced constraint states what breaks. |
| C-15 Stakeholder-risk-first opener | FAIL | Prompt opens with STEP 1 -- COLLECT INPUT. No WHO IS AT RISK section or equivalent. Role differentiation is imposed by late pre-write gate checklist, not derived from a stakeholder opener. |
| C-16 Every criterion structural | FAIL | C-15 has no structural element -- there is no stakeholder-risk section. Since C-15 is absent from the structural inventory, C-16 cannot pass. |

**Aspirational pass**: C-09, C-10, C-11, C-12, C-13, C-14 = 6 / 8
**Composite**: (5/5 x 60) + (3/3 x 30) + (6/8 x 10) = 60 + 30 + 7.5 = **97.5**
**All essential pass**: YES

---

## V-02: Consequence Table

**Mechanism**: Dedicated CONSTRAINT CONSEQUENCES TABLE before signal planning -- consequences live in a table column (C-14 structural).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 TOPICS.md entry | PASS | STEP 2: "Open simulations/TOPICS.md. Create if absent. Append one row and write the file." |
| C-02 Correct path | PASS | STEP 4: "Write simulations/{topic}/strategy.md:" |
| C-03 All five fields | PASS | Signal plan table has all five columns; CONSTRAINT CONSEQUENCES TABLE enumerates Namespace, Item name, Owner role, Priority vocab explicitly |
| C-04 Valid priority vocab | PASS | CONSTRAINT CONSEQUENCES row: "Priority vocab | Exactly: essential / recommended / optional | Strategy treated as advisory-only; commit gate logic cannot function; team has no enforceable threshold" |
| C-05 At least one essential | PASS | CONSTRAINT CONSEQUENCES row + pre-write gate checkbox: ">=1 essential signal" |
| C-06 Multi-namespace coverage | PASS | CONSTRAINT CONSEQUENCES row + pre-write gate checkbox: ">=2 distinct namespaces" |
| C-07 Narrative rationale | PASS | STEP 4: "## Rationale [2-4 sentences: what is the team currently assuming?...]" |
| C-08 Differentiated roles | PASS | CONSTRAINT CONSEQUENCES row + pre-write gate checkbox: ">=2 distinct owner roles" |
| C-09 Commit gate defined | PASS | "## Commit Gate / Design commit is permitted when: [minimum signal set, stated as a testable condition]." |
| C-10 Naming convention | PASS | "## Naming Reference / All item names in this strategy follow: {topic}-{slug}-{date}.md" |
| C-11 Checkbox-gate before transition | PASS | Eight-item pre-write gate referencing the CONSTRAINT CONSEQUENCES table: "Do not write the strategy file until all eight checks pass." |
| C-12 Invalid vocab = operational consequence | PASS | CONSTRAINT CONSEQUENCES table row consequence column: "advisory-only; commit gate logic cannot function; team has no enforceable threshold" -- in a table column |
| C-13 Dedicated sections per aspiration | PASS | "## Commit Gate" and "## Naming Reference" are dedicated named sections |
| C-14 Pervasive consequence framing | PASS | CONSTRAINT CONSEQUENCES TABLE has a "Downstream failure if violated" column covering all 8 constraint classes (Namespace, Item name, Owner role, Priority vocab, Essential count, Namespace coverage, Role coverage, Cell completeness). Every constraint carries its failure mode in a single structural table. |
| C-15 Stakeholder-risk-first opener | FAIL | Prompt opens with STEP 1 -- COLLECT INPUT. No stakeholder-risk section. Role differentiation is imposed by CONSTRAINT CONSEQUENCES row and pre-write gate, not derived from a stakeholder opener. |
| C-16 Every criterion structural | FAIL | C-15 has no structural element. The CONSTRAINT CONSEQUENCES TABLE is a constraint table, not a stakeholder-risk enumeration. C-15 is unenforced, so C-16 fails. |

**Aspirational pass**: C-09, C-10, C-11, C-12, C-13, C-14 = 6 / 8
**Composite**: (5/5 x 60) + (3/3 x 30) + (6/8 x 10) = 60 + 30 + 7.5 = **97.5**
**All essential pass**: YES

**Note**: V-02 satisfies C-14 more explicitly than V-01 -- consequences are in a dedicated table column rather than in column header cells. Both satisfy C-14; V-02's mechanism is easier to audit and harder to omit. The score is identical because the same two criteria (C-15, C-16) fail.

---

## V-03: Mandatory Stakeholder-Risk Fill-In

**Mechanism**: WHO IS AT RISK becomes STEP 1 with a required fill-in table output. Signal ownership must trace to that table.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 TOPICS.md entry | PASS | STEP 3: "Open simulations/TOPICS.md. Create if absent. Append one row and write the file." |
| C-02 Correct path | PASS | STEP 5: "Write simulations/{topic}/strategy.md:" |
| C-03 All five fields | PASS | Signal plan table has all five columns. Column header row provides format templates. |
| C-04 Valid priority vocab | PASS | Dedicated prose block: "Priority -- three values only: essential / recommended / optional. Any other value... makes this strategy invalid as a commit gate. The downstream system treats it as advisory-only." |
| C-05 At least one essential | PASS | Pre-write gate: ">=1 signal marked essential -- zero essential: gate has no blocking condition" |
| C-06 Multi-namespace coverage | PASS | Pre-write gate: ">=2 distinct namespaces -- single namespace: investigation blind to other dimensions" |
| C-07 Narrative rationale | PASS | STEP 5 template: "## Rationale [2-4 sentences: which stakeholders are at risk if this design is wrong?...]" |
| C-08 Differentiated roles | PASS | Pre-write gate: "All owner roles trace to a row in the STEP 1 table" -- enforces >=2 distinct named roles (STEP 1 gate requires >=2) |
| C-09 Commit gate defined | PASS | "## Commit Gate / Design commit is permitted when: [minimum signal set, as a testable condition]." |
| C-10 Naming convention | PASS | "## Naming Reference / All item names in this strategy follow: {topic}-{slug}-{date}.md" |
| C-11 Checkbox-gate before transition | PASS | Five-item pre-write gate with "Do not proceed to STEP 5 until all five checks pass." |
| C-12 Invalid vocab = operational consequence | PASS | Prose block: "The downstream system treats it as advisory-only. The team loses the ability to hold design commit at an enforceable threshold." -- clear operational consequence |
| C-13 Dedicated sections per aspiration | PASS | "## Commit Gate" and "## Naming Reference" are dedicated named sections in strategy template |
| C-14 Pervasive consequence framing | FAIL | Priority has a full prose consequence block. Pre-write gate items carry inline consequence notes for gate-level violations. However: the Namespace column header shows only "(scout/draft/...)" -- no downstream failure stated. The Skill column shows only "{skill}" -- no failure. The Item name column shows only the format template -- no failure mode. Not every enforced constraint carries its downstream failure at its point of declaration. |
| C-15 Stakeholder-risk-first opener | PASS | STEP 1 -- STAKEHOLDERS AT RISK is the first step. "Before planning any signals, identify who is harmed if this design is wrong. Fill in the table below. This is the first deliverable of this skill." "Do not proceed to STEP 2 until this table contains at least 2 distinct named roles." Fill-in table is required output before signal planning. Role differentiation is a structural output, not a late checklist item. |
| C-16 Every criterion structural | FAIL | C-14 is not fully satisfied: per-field constraints on Namespace, Skill, and Item name lack structural consequence elements (no table column, no checkpoint note carrying the failure mode). Since C-14's enforcement is incomplete at the structural level, C-16 fails -- not every criterion is enforced by a structural element. |

**Aspirational pass**: C-09, C-10, C-11, C-12, C-13, C-15 = 6 / 8
**Composite**: (5/5 x 60) + (3/3 x 30) + (6/8 x 10) = 60 + 30 + 7.5 = **97.5**
**All essential pass**: YES

**Note**: V-03 is the mirror of V-01/V-02 -- it passes C-15 but fails C-14, exactly the opposite failure pattern. This confirms the R3 diagnostic: satisfying one of C-14/C-15 structurally (but not the other) still produces 97.5. The ceiling is not reached without both.

---

## V-04: Field Schema + Coverage Schema

**Mechanism**: Two schema tables with "Consequence if violated" columns -- FIELD SCHEMA (per-row) and COVERAGE SCHEMA (whole-plan). C-14 + C-16 in one structure.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 TOPICS.md entry | PASS | STEP 2: "Open simulations/TOPICS.md. Create if absent. Append one row and write the file." |
| C-02 Correct path | PASS | STEP 4: "Write simulations/{topic}/strategy.md:" |
| C-03 All five fields | PASS | Signal plan table has all five columns. FIELD SCHEMA enumerates all five fields with allowed values and consequences. |
| C-04 Valid priority vocab | PASS | FIELD SCHEMA row 5: "Priority | essential / recommended / optional | Any other value: strategy treated as advisory-only; commit gate logic fails; team has no enforceable threshold before design commit" |
| C-05 At least one essential | PASS | COVERAGE SCHEMA row 1 + pre-write gate: ">=1 essential signal (COVERAGE SCHEMA row 1)" |
| C-06 Multi-namespace coverage | PASS | COVERAGE SCHEMA row 2 + pre-write gate: ">=2 distinct namespaces (COVERAGE SCHEMA row 2)" |
| C-07 Narrative rationale | PASS | STEP 4: "## Rationale [2-4 sentences: what is the team currently assuming?...]" |
| C-08 Differentiated roles | PASS | COVERAGE SCHEMA row 3 + pre-write gate: ">=2 distinct owner roles (COVERAGE SCHEMA row 3)" |
| C-09 Commit gate defined | PASS | "## Commit Gate / Design commit is permitted when: [minimum signal set, stated as a testable condition -- not 'enough evidence']." |
| C-10 Naming convention | PASS | "## Naming Reference / All item names in this strategy follow: {topic}-{slug}-{date}.md" |
| C-11 Checkbox-gate before transition | PASS | Eight-item pre-write gate with explicit FIELD SCHEMA / COVERAGE SCHEMA row citations: "Do not proceed to STEP 4 until all eight checks pass." |
| C-12 Invalid vocab = operational consequence | PASS | FIELD SCHEMA row 5 consequence column: "strategy treated as advisory-only; commit gate logic fails; team has no enforceable threshold" -- in a table column |
| C-13 Dedicated sections per aspiration | PASS | "## Commit Gate" and "## Naming Reference" as dedicated named sections |
| C-14 Pervasive consequence framing | PASS | FIELD SCHEMA has a "Consequence if violated" column covering all five fields (Namespace, Skill, Item name, Owner role, Priority). COVERAGE SCHEMA has a "Consequence if not met" column covering all four coverage requirements. Every enforced constraint appears in one of the two schema tables and carries its failure mode in the consequence column. |
| C-15 Stakeholder-risk-first opener | FAIL | Prompt opens with STEP 1 -- COLLECT INPUT. No stakeholder-risk or WHO IS AT RISK section. Role differentiation is enforced by COVERAGE SCHEMA row 3 and the pre-write gate, not derived from a stakeholder opener. |
| C-16 Every criterion structural | FAIL | C-15 is completely absent from the prompt -- there is no stakeholder-risk section. Since C-15 has no structural element, C-16 cannot pass. All other criteria are enforced structurally (schema tables, checkboxes, section headers), but the absence of C-15 breaks the "every criterion" requirement. |

**Aspirational pass**: C-09, C-10, C-11, C-12, C-13, C-14 = 6 / 8
**Composite**: (5/5 x 60) + (3/3 x 30) + (6/8 x 10) = 60 + 30 + 7.5 = **97.5**
**All essential pass**: YES

**Note**: V-04 is the strongest C-14 implementation in R3 (two-table schema with consequence columns covering all 9 constraints) and has the cleanest pre-write gate (checkboxes cite parent schema rows by number). But it fails C-15 for the same reason as V-01 and V-02. Excellent structural coverage of C-14/C-16 for every criterion except C-15 still produces 97.5.

---

## V-05: Full Structural Contract

**Mechanism**: Every criterion C-01 through C-16 maps to exactly one structural element. Stakeholder-risk opener is a mandatory fill-in table. Field Schema + Coverage Schema carry consequences as table columns. Checkpoint gate references schema rows.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 TOPICS.md entry | PASS | "## Inputs" section: "Register in simulations/TOPICS.md -- create if absent, append row and write file:" with template row |
| C-02 Correct path | PASS | "## Strategy File / Write simulations/{topic}/strategy.md with these exact sections:" -- explicit path + full section template |
| C-03 All five fields | PASS | Field Schema enumerates all five fields with allowed values. Signal Plan table has all five columns. Pre-write gate checks all five field constraints. |
| C-04 Valid priority vocab | PASS | Field Schema row 5: "Priority | essential / recommended / optional | Any other value: strategy treated as advisory-only; commit gate logic fails; team has no enforceable threshold" |
| C-05 At least one essential | PASS | Coverage Schema row 1 + pre-write gate: ">=1 essential signal (Coverage Schema row 1)" |
| C-06 Multi-namespace coverage | PASS | Coverage Schema row 2 + pre-write gate: ">=2 distinct namespaces (Coverage Schema row 2)" |
| C-07 Narrative rationale | PASS | "### Rationale [2-4 sentences: which stakeholders are at risk? What assumption does the team currently hold?...]" -- section header in strategy template |
| C-08 Differentiated roles | PASS | Coverage Schema row 3 + pre-write gate: ">=2 distinct owner roles from Stakeholders table (Coverage Schema row 3)" -- roles traced to Stakeholders opener, not just counted |
| C-09 Commit gate defined | PASS | "### Commit Gate / Design commit is permitted when: [...]. A testable condition names specific signals. 'Enough evidence gathered' is not testable." |
| C-10 Naming convention | PASS | "### Naming Reference / All item names in this strategy follow: {topic}-{slug}-{date}.md [...] Deviation from this format: artifact will not match registry lookup pattern; downstream skills cannot find it." -- only R3 variation to carry consequence framing inside the Naming Reference section itself |
| C-11 Checkbox-gate before transition | PASS | Nine-item pre-write gate with explicit schema row citations: "Do not write any file until all nine checks pass." |
| C-12 Invalid vocab = operational consequence | PASS | Field Schema row 5 consequence column: "strategy treated as advisory-only; commit gate logic fails; team has no enforceable threshold" -- structural table column |
| C-13 Dedicated sections per aspiration | PASS | "### Commit Gate" and "### Naming Reference" are dedicated section headers in the strategy template |
| C-14 Pervasive consequence framing | PASS | Field Schema covers all five fields with a "Consequence if violated" column. Coverage Schema covers all four coverage requirements with a "Consequence if not met" column. Naming Reference section carries its own inline consequence. Every enforced constraint -- field-level and plan-level -- states its downstream failure mode in a structural element. |
| C-15 Stakeholder-risk-first opener | PASS | "## Stakeholders at Risk" is the opening section before Inputs and before signal planning. "Identify who is harmed if this design is wrong. Fill this table now. This is the first required output of this skill." Fill-in table with empty cells to complete. "Do not proceed until this table contains >=2 distinct named roles. Signal ownership in the Signal Plan must reference roles from this table." Role differentiation is a structural output requirement, not a late checklist item. |
| C-16 Every criterion structural | PASS | Verified per criterion: C-01 (TOPICS.md template row in Inputs section), C-02 (explicit path + section list in Strategy File header), C-03 (Field Schema table + Signal Plan columns), C-04 (Field Schema row 5 consequence column), C-05 (Coverage Schema row 1 + gate checkbox), C-06 (Coverage Schema row 2 + gate checkbox), C-07 (### Rationale section header), C-08 (Coverage Schema row 3 + gate checkbox), C-09 (### Commit Gate section header), C-10 (### Naming Reference section header with inline consequence), C-11 (pre-write gate section), C-12 (Field Schema row 5 consequence column), C-13 (dedicated section headers), C-14 (two schema tables with consequence columns), C-15 (## Stakeholders at Risk fill-in table), C-16 (self-satisfied: no criterion is enforced by prose instruction alone). |

**Aspirational pass**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16 = 8 / 8
**Composite**: (5/5 x 60) + (3/3 x 30) + (8/8 x 10) = 60 + 30 + 10 = **100**
**All essential pass**: YES

---

## Rankings

| Rank | Variation | Composite | All Essential | Aspirational | Fails |
|------|-----------|-----------|---------------|--------------|-------|
| 1 | **V-05** | **100** | YES | 8/8 | -- |
| 2 | V-01 | 97.5 | YES | 6/8 | C-15, C-16 |
| 3 | V-02 | 97.5 | YES | 6/8 | C-15, C-16 |
| 4 | V-03 | 97.5 | YES | 6/8 | C-14, C-16 |
| 5 | V-04 | 97.5 | YES | 6/8 | C-15, C-16 |

**Score gap**: V-05 scores 100; V-01 through V-04 all score 97.5. The gap is 2.5 points (one aspirational criterion pair: C-15 + C-16 require each other to both pass).

**Sub-rankings within 97.5**:
- V-04 > V-02 > V-01 on C-14 implementation quality: two schema tables (V-04) > dedicated consequence table (V-02) > column header encoding (V-01)
- V-03 uniquely passes C-15 at 97.5 -- opposite pattern from the other three

---

## R3 Diagnostic Result

The R3 hypothesis is confirmed. Structural enforcement of C-14 AND C-15 together is a meaningfully different mechanism from satisfying only one.

- V-01/V-02/V-04: satisfy C-14 structurally (column headers / consequence table / schema tables) but have no structural element for C-15. Score: 97.5.
- V-03: satisfies C-15 structurally (fill-in table at opener) but does not satisfy C-14 structurally (Priority consequence is a prose block; Namespace/Skill/Item name column headers lack consequence framing). Score: 97.5.
- V-05: satisfies both C-14 and C-15 structurally, and therefore satisfies C-16. Score: 100.

**C-16 is a dependent criterion**: It passes if and only if C-14 and C-15 both pass structurally. C-16 is the verification check that the structural contract is complete, not an independently achievable criterion. A prompt that satisfies C-16 is fully structuralized; one that fails C-16 has at least one unstructured criterion.

**The R3 finding extends R2**: R2 showed C-11/C-12/C-13 are necessary and sufficient for a 13-criterion rubric. R3 shows C-14/C-15/C-16 require the full structural contract -- satisfying only one of C-14 or C-15 structurally is not sufficient. Both must be structural, and when they are, C-16 follows.

---

## Excellence Signals (R3)

1. **Mandatory fill-in as structural enforcement for stakeholder-risk opener** (V-05 vs V-03) -- R2's V-04 had a static WHO IS AT RISK paragraph (structural in form, passive in content). V-03/V-05 make the opener an active output production step: the model fills the table, and the gate enforces >=2 named roles before proceeding. Role differentiation emerges from the model's own STEP 1 output, making C-08 a downstream consequence of the opener rather than an independent checklist item. This is the mechanism that closes C-15 and explains why V-03's C-15 passes where R2's V-04's was only framing.

2. **Schema separation as complete constraint registry** (V-04/V-05) -- Separating FIELD SCHEMA (per-row field rules) from COVERAGE SCHEMA (whole-plan coverage rules), each with a Consequence column, produces a two-tier registry where every constraint has exactly one home. Pre-write gate checkboxes that cite parent schema rows by number ("Field Schema row 5", "Coverage Schema row 1") create structural dependency: removing any schema row breaks a named gate check. This is the most compact encoding of C-14 + C-16 found in R3. V-04 demonstrates it for C-14 alone; V-05 adds C-15 to complete the structural contract.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["mandatory fill-in opener enforces C-15 structurally -- making the stakeholder-risk section an active output production step (not a static paragraph) derives role differentiation from the model's own first output rather than imposing it via a late checklist", "schema separation as constraint registry -- FIELD SCHEMA and COVERAGE SCHEMA with Consequence columns create a two-tier structure where every constraint has exactly one structural home and pre-write gate checkboxes cite schema rows by reference, making C-14 + C-16 co-satisfiable in one compact structure"]}
```
