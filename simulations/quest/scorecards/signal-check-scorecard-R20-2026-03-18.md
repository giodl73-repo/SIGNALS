## signal-check Round 20 Scorecard

**Rubric**: v19 — 45 aspirational, formula = `90 + (asp/45) * 10`

| Var | Axis | Asp. | Composite | Rank |
|-----|------|------|-----------|------|
| V-01 | G (verdict block) | 45/45 | 100.00 | T-1 |
| V-02 | H (quality column) | 45/45 | 100.00 | T-1 |
| V-03 | I (prior check) | 45/45 | 100.00 | T-1 |
| V-04 | G+H | 45/45 | 100.00 | T-1 |
| V-05 | G+H+I + live | 45/45 | 100.00 | **T-1 (excellence leader)** |

**Why all tie**: The R20 axes (VERDICT, Quality column, Prior check, Evidence trace) target untouched structural slots — none map to any criterion in C-01 through C-53. No scoring differential is possible under v19. The differentiator is C-54 (candidate), which only V-05 passes.

**C-54 boundary**:

| Var | Verdict block | Evidence trace | C-54 |
|-----|--------------|----------------|------|
| V-01 | YES | NO | FAIL |
| V-02 | NO | NO | FAIL |
| V-03 | NO | NO | FAIL |
| V-04 | YES | NO | FAIL |
| V-05 | YES | YES | PASS |

**Excellence signals (V-05)**:
- Verdict-to-source closed loop: VERDICT names blocking dim → Evidence trace maps to Row N → Row N names artifact (or confirms absence)
- Inventory row stability contract: row numbers in GATHER YOUR SIGNALS are functional, not cosmetic — Evidence trace cross-references them
- Absence at verdict level: OPEN dimensions write "not represented in inventory" in Evidence trace, not just in preflight items
- Machine-readable: `blocking_dims` + `evidence_trace` frontmatter fields enable automated cross-checks

**v20 extraction candidates**: C-54 (Evidence trace), C-55 (VERDICT section), C-56 (Quality column), C-57 (Prior check field) — denominator grows from 45 to 48–49.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Evidence trace field in VERDICT maps each blocking dimension to the exact inventory row number and artifact path creating a closed structural loop from decision to source without entering any preflight item", "Inventory row number stability contract makes row numbering functional not cosmetic -- Evidence trace references require row numbers to match GATHER YOUR SIGNALS table assignments", "Absence declaration at verdict level writes not-represented-in-inventory for OPEN dimensions so absence is declared at the verdict level not only within the preflight item body", "machine-readable evidence_trace frontmatter enables automated cross-checks between blocking_dims and inventory row contents without prose parsing"]}
```
---|-----------|------|------|------|------|------|-------|
| C-09 | Named STANDING RULES block with block title | PASS | PASS | PASS | PASS | PASS | All: `STANDING RULES [STANDING RULES -- Constraints that persist...]` |
| C-10 | Rule 1 and Rule 2 named | PASS | PASS | PASS | PASS | PASS | Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity |
| C-11 | Pilot-briefing language in READINESS SUMMARY | PASS | PASS | PASS | PASS | PASS | "Does not decide; frames what the team is walking into"; "The team decides" |
| C-12 | Four dimensions consistent labeling | PASS | PASS | PASS | PASS | PASS | CAUSAL GAP / SEQUENCE / STALENESS / COHERENCE uniform across all items |
| C-13 | MISSING SIGNAL GUIDE names signal types | PASS | PASS | PASS | PASS | PASS | All: dimension + skill per gap line, not generic phrasing |
| C-14 | STANDING RULES precedes artifact inventory | PASS | PASS | PASS | PASS | PASS | STANDING RULES -> GATHER YOUR SIGNALS ordering held in all |
| C-15 | Verbatim absence phrase specified per dimension | PASS | PASS | PASS | PASS | PASS | All: required phrases in scan index and at each preflight item |
| C-16 | Every constraint enumerates all output locations | PASS | PASS | PASS | PASS | PASS | V-01/V-04: Rule 1+2 Applies-to adds VERDICT; V-02: VERDICT absent, omitted correctly; V-03: adds Prior check fields; V-05: adds both Prior check fields and Evidence trace |
| C-17 | Verbatim absence phrases embedded at point of use | PASS | PASS | PASS | PASS | PASS | Phrases appear in scan index AND within each preflight item body |
| C-18 | Advisory register carried structurally | PASS | PASS | PASS | PASS | PASS | Pilot-briefing, coaching, "team decides" in section headings and prose |
| C-19 | Triple enforcement stack declared as unit | PASS | PASS | PASS | PASS | PASS | ENFORCEMENT STACK NOTE names all three rules, states non-substitutability, declares all-three-must-pass |

---

### Meta-rule chain (C-20 to C-32) -- all variations: PASS

| ID | Criterion | Evidence |
|----|-----------|----------|
| C-20 | Location-enumeration as named meta-rule | Rule 3: "RULES WITHOUT DECLARED SCOPE DO NOT EXIST" |
| C-21 | Each rule assigned named failure class | Rule 1: Absence Drift; Rule 2: Reference Ambiguity; Rule 3: Constraint Scope Gaps |
| C-22 | Meta-rule includes temporal activation gate | "Scope must be discharged at rule-creation time, not retroactively" |
| C-23 | Meta-rule declares self-application | "This requirement self-applies: Rule 3 itself declares its scope below" |
| C-24 | Activation gate framed as validity condition | "A rule without scope has no force, no scope, and no standing. It does not exist as an active rule." |
| C-25 | Self-application includes proximate scope pointer | "Rule 3 itself declares its scope below" points to Applies-to field |
| C-26 | Activation gate carries both obligation and validity framing | Obligation paragraph + Existence condition paragraph co-present |
| C-27 | Validity condition uses rule-existence framing | "does not exist as an active rule" |
| C-28 | Rule name encodes existence assertion | "RULES WITHOUT DECLARED SCOPE DO NOT EXIST" |
| C-29 | Dual register as labeled sections | "Obligation:" and "Existence condition:" independently labeled |
| C-30 | Validity condition in separate labeled field | "Existence condition:" independently labeled |
| C-31 | Activation gate in labeled field | "Obligation:" labeled, activation gate is its content |
| C-32 | Meta-rule names its own document position | Rule 3 self-applies; it resides within the STANDING RULES block it governs |

---

### Rule 3 and failure class chain (C-33 to C-46) -- all variations: PASS

| ID | Criterion | Evidence |
|----|-----------|----------|
| C-33 | STANDING RULES contains named Rule 3 | "Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST" |
| C-34 | Each failure class includes definition | All three rules define their failure mode in the rule body |
| C-35 | Each failure class includes example | Rule 2: correct/wrong examples; Rule 1: "Silence in any governed location constitutes absence drift"; Rule 3: "does not exist as an active rule" |
| C-36 | Rule 3 includes explicit Applies-to | "Applies to: all Rule declarations in this STANDING RULES block, including Rule 3 itself and any rule added in the future" |
| C-37 | Each failure class includes detection instruction | "A committing engineer... consults this rule to determine which Finding locations require verbatim phrases" |
| C-38 | Applies-to carry location-specific scope | Rule 2: "CAUSAL GAP action, SEQUENCE action" names fields within sections; V-05: "VERDICT (Condition field only)" is field-level |
| C-39 | Each failure class includes prevention instruction | Rule 1: "Do not leave a Finding field blank. Do not hedge."; Rule 2: /namespace:skill format |
| C-40 | Applies-to includes cross-section reach | Rule 1 spans readiness summary, four dimension Findings, cross-item patterns, and guide |
| C-41 | Each failure class includes recovery instruction | Rule 1: "write the absence explicitly using the required verbatim phrases"; Rule 2: use /namespace:skill format |
| C-42 | Applies-to includes field-level granularity | Rule 2: "CAUSAL GAP action" is field-level; V-05: "VERDICT (Condition field only)" |
| C-43 | Applies-to consolidated under labeled sub-structure | Each rule ends with "Applies to:" as consolidated labeled field |
| C-44 | Applies-to uses list or table format | Comma-separated enumeration: individually parseable without prose |
| C-45 | Failure class as standalone labeled entry with sub-fields | Rule headings encode class name; rule bodies contain definition, example, detection, prevention, recovery |
| C-46 | STANDING RULES contains FAILURE CLASS REGISTER | ENFORCEMENT STACK NOTE consolidates all three failure classes with interdependency declaration |

---

### Readiness summary and advisory saturation (C-47 to C-49)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-47 | READINESS SUMMARY includes dimensional-status preamble | PASS | PASS | PASS | PASS | PASS | All: four-line STATUS block before pilot-briefing prose |
| C-48 | Every section header carries function annotation | PASS | PASS | PASS | PASS | PASS | All sections carry `[FUNCTION: ...]`; V-01/V-04/V-05 add VERDICT `[FUNCTION: ...]` |
| C-49 | Advisory register at all three structural levels | PASS | PASS | PASS | PASS | PASS | C-18 + C-47 + C-48 co-present in all variations |

---

### R19 new criteria (C-50 to C-53)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-50 | Dims column in inventory table | PASS | PASS | PASS | PASS | PASS | All retain Dims column; V-02/V-04/V-05 extend to 7-column table (Dims + Quality) |
| C-51 | CROSS-ITEM PATTERNS uses labeled pattern blocks | PASS | PASS | PASS | PASS | PASS | All retain Pattern:/Items implicated:/Root cause:/Single action: block |
| C-52 | MISSING SIGNAL GUIDE severity-ordered | PASS | PASS | PASS | PASS | PASS | All retain "Items ordered by severity: OPEN before FLAG" with invariant ordering clause |
| C-53 | STATUS vocabulary five-state taxonomy | PASS | PASS | PASS | PASS | PASS | OK-STRONG/OK-WEAK/FLAG/OPEN retained; covers all diagnostic categories |

---

### C-54 candidate (live R20 axis -- not in v19 rubric denominator)

| Var | Verdict block | Evidence trace | C-54 |
|-----|--------------|----------------|------|
| V-01 | YES | NO | FAIL -- precondition met; trace absent |
| V-02 | NO | NO | FAIL -- precondition unmet |
| V-03 | NO | NO | FAIL -- precondition unmet |
| V-04 | YES | NO | FAIL -- G+H without trace |
| V-05 | YES | YES | **PASS** |

Boundary confirmed clean across all four negative cases. C-54 requires VERDICT section as precondition; VERDICT alone does not imply C-54.

---

### Excellence signals (V-05)

V-05 introduces the Evidence trace field in the VERDICT block, creating four structural advances:

1. **Verdict-to-source closed loop** -- VERDICT names blocking dimension -> Evidence trace maps to Row N -> Row N in inventory names artifact (or confirms absence). Reader navigates from decision to source without entering preflight items.

2. **Inventory row stability contract** -- GATHER YOUR SIGNALS assigns numbered rows; Evidence trace references those row numbers. Row numbering becomes functional, not cosmetic -- a cross-section integrity check.

3. **Absence declaration at verdict level** -- when a dimension is OPEN, Evidence trace writes "not represented in inventory -- no artifact carries {abbrev} in Dims" rather than leaving the verdict-to-source link dangling. Rule 1 explicitly governs the Evidence trace field.

4. **Machine-readable verdict loop** -- frontmatter adds `blocking_dims` and `evidence_trace` per-dimension fields, enabling automated cross-check between verdict and inventory row contents without prose parsing.

**Why V-04 fails C-54**: V-04 carries G+H (verdict + quality) but no Evidence trace. The blocking dimension named in Verdict/Condition is not mapped to any inventory row. The reader must enter the preflight items to find the source artifact. The closed loop is broken.

---

### v20 rubric extraction candidates

| Candidate | Axis | Precondition | Description |
|-----------|------|-------------|-------------|
| C-54 | live (V-05) | VERDICT section (Axis G) | Evidence trace maps blocking dims to inventory rows |
| C-55 | G | none | VERDICT section with GO/CONDITIONAL/NO-GO + Condition per blocking dim |
| C-56 | H | C-50 (Dims column) | Quality column annotates per-artifact reliability before preflight analysis |
| C-57 | I | C-47 (status preamble) | Prior check field per dimension with IMPROVING/STABLE/DEGRADING/NEW |

Aspirational denominator will grow from 45 to 48-49 depending on extraction decisions.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Evidence trace field in VERDICT maps each blocking dimension to the exact inventory row number and artifact path creating a closed structural loop from decision to source without entering any preflight item", "Inventory row number stability contract makes row numbering functional not cosmetic -- Evidence trace references require row numbers to match GATHER YOUR SIGNALS table assignments", "Absence declaration at verdict level writes not-represented-in-inventory for OPEN dimensions so absence is declared at the verdict level not only within the preflight item body", "machine-readable evidence_trace frontmatter enables automated cross-checks between blocking_dims and inventory row contents without prose parsing"]}
```
