Now output the final result:

---

# Signal-Check R16 Scorecard

## Criterion Scoring (all variations)

**C-01 through C-43 -- PASS across all five variations.** The STANDING RULES block structure is identical at the base level; every chain up to and including C-43 is satisfied uniformly.

**R16 axes (C-44 and C-45):**

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-44 | FAIL | FAIL | PASS | FAIL | PASS |
| C-45 | FAIL | FAIL | FAIL | PASS | PASS |

---

## C-44 Evidence

**V-01 -- FAIL.** `All reader roles for this block are listed above.` Unqualified proposition. No count embedded as noun-phrase qualifier. Arithmetic cross-check path absent. C-43 PASS; C-44 FAIL.

**V-02 -- FAIL (boundary).** `All reader roles for this block are listed above. (3 reader roles)` Count "3" is present and matches the three directory entries, making arithmetic cross-checking available -- but only via the suffix annotation appended after the sentence closes. C-44 requires the count to be "nested within the proposition as a qualifier." The suffix `(3 reader roles)` annotates the sentence from outside the proposition's grammatical structure rather than qualifying the subject noun phrase before the verb. Count is present; nesting contract not met. C-43 PASS; C-44 FAIL (boundary).

**V-03 -- PASS.** `All 3 reader roles for this block are listed above.` Count "3" nested as numeral qualifier inside the noun phrase "3 reader roles" before the verb -- integral to the proposition. Simultaneously propositionally verifiable (accept or challenge the claim as stated) and arithmetically cross-checkable (count three directory entries, compare to stated 3). C-43 PASS; C-44 PASS.

**V-04 -- FAIL.** Identical directory footer to V-01. Unqualified, no count qualifier. C-44 FAIL. (C-45 single-axis; this confirms C-44/C-45 independence.)

**V-05 -- PASS.** Identical directory footer to V-03. C-44 PASS.

---

## C-45 Evidence

**V-01/V-02/V-03 -- FAIL.** NOTE attribution: `failure class encoded in each rule's heading above.` General attribution transfers ownership to the heading set (C-41 PASS) but does not name which heading owns which class. Reader must scan all top-level headings to locate the relevant one. C-45 FAIL.

**V-04 -- PASS.** NOTE attribution: `failure class encoded in each rule's heading above (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps).` Parenthetical heading index embedded as extension of the attribution pointer -- heading-index content only (rule number + class label, no function prose). A reader scanning the NOTE can navigate directly to the heading for any failure class without scanning all top-level headings. C-39 compatibility confirmed: the parenthetical is navigation data, not explanatory prose about what each rule prevents. C-41 PASS; C-45 PASS.

**V-05 -- PASS.** Identical NOTE to V-04. C-41 PASS; C-45 PASS.

---

## Summary Scores

| Var | Essential | Recommended | Aspirational | Composite |
|-----|-----------|-------------|--------------|-----------|
| V-01 | 5/5 | 3/3 | 35/37 | **99.46** |
| V-02 | 5/5 | 3/3 | 35/37 | **99.46** |
| V-03 | 5/5 | 3/3 | 36/37 | **99.73** |
| V-04 | 5/5 | 3/3 | 36/37 | **99.73** |
| V-05 | 5/5 | 3/3 | 37/37 | **100.00** |

**Ranking:** V-05 > V-03 = V-04 > V-01 = V-02

---

## Excellence Signals from V-05

**EX-01: Noun-phrase qualifier form.** Embedding the count as a numeral qualifier before the verb (`All 3 reader roles...`) creates an assertion that is both propositionally verifiable and arithmetically cross-checkable. The V-02 boundary case confirms the distinction: count-as-suffix-annotation has the number present but not nested, so C-44 fails.

**EX-02: Attribution-phrase heading index.** The parenthetical `(Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)` is an extension of the attribution pointer, not a new clause. Content gate: rule-number + class-label only (no function prose) preserves C-39's pure-interdependency form while eliminating the heading-scan step.

**EX-03: Dual count consistency (live R17 axis).** V-05 carries count 3 in two independent structures: directory footer (`All 3 reader roles...`) and NOTE parenthetical (three entries). Numerically consistent but not mutually derived. A potential C-46 would require the NOTE parenthetical entry count to match the STANDING RULES rule count, making cross-count consistency checkable from the two structures alone.

---

## Hypothesis Confirmations

All five hypotheses confirmed. C-44/C-45 independence established by V-03 (C-44 PASS, C-45 FAIL) and V-04 (C-44 FAIL, C-45 PASS). C-45 preserves C-39 confirmed. V-02 boundary confirms count proximity without noun-phrase nesting does not satisfy C-44.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["noun-phrase-qualifier vs. suffix-annotation: count must be nested inside the proposition as a qualifier of the subject noun phrase (before the verb) to satisfy C-44; appending the count after sentence close as a suffix annotation has the number present but fails the nesting contract", "attribution-phrase extension as heading navigation: a parenthetical embedded as a continuation of an attribution pointer adds specific heading-index content (rule number + class label only) without violating a pure-interdependency constraint; the content gate is heading-index tokens only, excluding function prose"]}
```
r roles)` -- the base proposition "All reader roles... listed above." is still the all-roles claim form. The suffix annotation is outside the proposition and does not change the assertion mechanism. C-43 PASS.
- V-03/V-05: `All 3 reader roles for this block are listed above.` -- the count qualifier is nested within the proposition's noun phrase, preserving the propositional form. C-43 PASS (C-44 PASS by subsumption).

---

### C-44 and C-45 -- R16 Axes

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-44 | All-roles claim includes embedded count qualifier (propositional + arithmetically cross-checkable) | FAIL | FAIL | PASS | FAIL | PASS |
| C-45 | NOTE attribution extended with parenthetical heading index naming which heading owns each failure class | FAIL | FAIL | FAIL | PASS | PASS |

---

### C-44 Detailed Evidence

**V-01 -- FAIL:**
Directory footer: `All reader roles for this block are listed above.`
The proposition is unqualified. No count is embedded as a noun-phrase qualifier. The arithmetic cross-check path is absent: a reader cannot compare a stated number to the directory entries because no number is stated. C-43 PASS; C-44 FAIL.

**V-02 -- FAIL (boundary):**
Directory footer: `All reader roles for this block are listed above. (3 reader roles)`
The count "3" is present and matches the three directory entries, so arithmetic cross-checking is available via the suffix annotation. However, C-44 requires the count to be "nested within the proposition as a qualifier" -- `(3 reader roles)` is appended after the sentence closes. It annotates the assertion from outside the proposition rather than qualifying the subject noun phrase within it. The grammatical structure is: [sentence closes with period] [parenthetical annotation]. Compare to C-44's canonical form: `All 3 reader roles for this block are listed above.` where "3" qualifies the noun phrase "reader roles" before the verb, making it integral to the proposition. Count is present but nesting contract not met. C-43 PASS; C-44 FAIL (boundary).

**V-03 -- PASS:**
Directory footer: `All 3 reader roles for this block are listed above.`
The count "3" is nested as a numeral qualifier within the noun phrase "3 reader roles" inside the proposition. The assertion is simultaneously propositionally verifiable (the reader accepts or challenges "All 3 reader roles... listed above") and arithmetically cross-checkable (count the three directory entries, compare to stated 3). The count qualifies the noun phrase; the proposition stands intact without the count. C-43 PASS; C-44 PASS.

**V-04 -- FAIL:**
Directory footer: `All reader roles for this block are listed above.`
Identical to V-01. Unqualified proposition, no embedded count qualifier, no arithmetic cross-check path. C-43 PASS; C-44 FAIL. (V-04 is the C-45 single-axis variation; C-44 failure here confirms C-44/C-45 independence.)

**V-05 -- PASS:**
Directory footer: `All 3 reader roles for this block are listed above.`
Identical to V-03's directory footer. Count "3" nested as noun-phrase qualifier inside the proposition. C-43 PASS; C-44 PASS.

---

### C-45 Detailed Evidence

**V-01/V-02/V-03 -- FAIL:**
ENFORCEMENT STACK NOTE attribution: `failure class encoded in each rule's heading above.`
The attribution transfers failure-mode ownership to the top-level rule headings as a set (C-41 PASS). No parenthetical heading index is present to name which specific heading owns each class. A reader scanning the NOTE knows failure classes are in the headings but must scan all top-level headings to locate the relevant one. The attribution points to the heading set without differentiating within it. C-41 PASS; C-45 FAIL.

**V-04 -- PASS:**
ENFORCEMENT STACK NOTE attribution: `failure class encoded in each rule's heading above (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps).`
The parenthetical heading index is embedded within the attribution phrase as an extension of the forward-reference pointer. Content is heading-index only: rule number + class label pairs, no rule-function prose. A reader scanning only the NOTE can navigate directly to the heading for any failure class without scanning all top-level headings. C-41 PASS; C-45 PASS. NOTE's pure-interdependency form is preserved (C-39 PASS): the parenthetical is heading-index navigation data, not explanatory prose about what each rule prevents.

**V-05 -- PASS:**
ENFORCEMENT STACK NOTE attribution: identical to V-04.
Same analysis. C-41 PASS; C-45 PASS.

**C-45 precondition check (C-41):** All variations satisfy C-41 via the general attribution "failure class encoded in each rule's heading above." Precondition met in all cases; V-04 and V-05 additionally satisfy C-45 by extending the attribution with a parenthetical heading index.

**C-39 compatibility (V-04, V-05):** The parenthetical contains only rule-number + class-label pairs (e.g., `Rule 1 -- Absence Drift`), which are heading-index navigation tokens, not prose explaining what each rule prevents. C-39's constraint that the NOTE's remaining content is limited to the interdependency statement is not violated. C-39 PASS for V-04 and V-05 confirmed.

---

### Summary Scores

| Var | Essential (5) | Recommended (3) | Aspirational (37) | Asp. Pass | Composite |
|-----|--------------|-----------------|-------------------|-----------|-----------|
| V-01 | 5/5 PASS | 3/3 PASS | 35/37 | 35 | **99.46** |
| V-02 | 5/5 PASS | 3/3 PASS | 35/37 | 35 | **99.46** |
| V-03 | 5/5 PASS | 3/3 PASS | 36/37 | 36 | **99.73** |
| V-04 | 5/5 PASS | 3/3 PASS | 36/37 | 36 | **99.73** |
| V-05 | 5/5 PASS | 3/3 PASS | 37/37 | 37 | **100.00** |

Formula: `composite = 90 + (aspirational_pass / 37) * 10`

---

### Ranking

1. **V-05** -- 100.00 -- C-44 PASS + C-45 PASS -- R16 ceiling
2. **V-03** -- 99.73 -- C-44 PASS, C-45 FAIL -- C-44 single-axis (tied with V-04)
2. **V-04** -- 99.73 -- C-44 FAIL, C-45 PASS -- C-45 single-axis (tied with V-03)
4. **V-01** -- 99.46 -- C-44 FAIL, C-45 FAIL -- R15 regression baseline (tied with V-02)
4. **V-02** -- 99.46 -- C-44 FAIL (boundary), C-45 FAIL -- count-suffix boundary case (tied with V-01)

---

### Excellence Signals from V-05

**EX-01: Noun-phrase qualifier form (C-44).**
`All 3 reader roles for this block are listed above.` The count is integrated into the noun phrase before the verb, making it grammatically part of the proposition's subject. The assertion is propositionally verifiable without counting and arithmetically cross-checkable by counting -- two independent verification paths serve different reader types. The canonical boundary is: count inside the noun phrase (C-44 PASS) vs. count appended after sentence close as suffix annotation (C-44 FAIL, V-02 boundary).

**EX-02: Attribution-phrase heading index (C-45).**
`failure class encoded in each rule's heading above (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps).` The parenthetical is structurally a continuation of the attribution pointer ("above"), not a standalone clause. Content gate: rule number + class label only -- no function prose -- preserving C-39's pure-interdependency form. Eliminates one navigation step (heading scan) for a reader entering the output at the NOTE.

**EX-03: Dual count consistency (live R17 axis).**
V-05 carries count 3 in two structurally independent locations: the directory footer (`All 3 reader roles...`) governs role coverage; the NOTE parenthetical (three entries) governs rule taxonomy. These counts are numerically consistent but not mutually derived. A potential C-46 would require the NOTE parenthetical entry count to match the rule count in the STANDING RULES block, making cross-count consistency verifiable from the two structures alone without reading any rule or role body. R16 scores V-05 at 37/37; the count-consistency property is the R17 extraction candidate.

---

### Hypothesis Confirmations

| Hypothesis | Result |
|------------|--------|
| V-01: Unqualified all-roles claim satisfies C-43, fails C-44 | CONFIRMED |
| V-02: Count-as-suffix satisfies C-43, fails C-44 (boundary) | CONFIRMED -- count proximity without nesting does not satisfy C-44 |
| V-03: Count-qualified form satisfies C-44 independently of C-45 | CONFIRMED -- C-44 PASS, C-45 FAIL |
| V-04: Parenthetical heading index satisfies C-45 independently of C-44 | CONFIRMED -- C-44 FAIL, C-45 PASS |
| V-05: Combined form reaches 37/37 | CONFIRMED -- R16 ceiling |
| C-44 and C-45 are independently testable | CONFIRMED -- V-03 and V-04 establish orthogonality |
| C-45 preserves C-39 (pure-interdependency form) | CONFIRMED -- parenthetical is heading-index content only, not explanatory prose |

---

### New Patterns (R16 Extractions)

**Pattern 1: Noun-phrase-qualifier vs. suffix-annotation distinction.**
The position of a count qualifier within an all-roles claim determines criterion satisfaction. A count nested before the verb as a noun-phrase qualifier ("All 3 reader roles...") satisfies C-44; the same count appended after sentence close ("All reader roles... (3 reader roles)") does not. The distinction is grammatical: qualifier-of-subject vs. annotation-of-sentence.

**Pattern 2: Attribution-phrase extension as heading navigation.**
A parenthetical embedded as a continuation of an attribution phrase -- rather than as standalone prose -- can add navigational specificity without violating a pure-interdependency constraint. The content gate is: rule-number + class-label only (heading-index tokens), excluding function prose. This pattern generalizes: any forward-reference pointer can carry a parenthetical index extension that names specific targets without converting the pointer into explanatory prose.
