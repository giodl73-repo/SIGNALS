Scorecard written. Here is the full output:

---

# /quest:score — signal-check Round 13

## Summary Table

| Var | C-39 | C-40 | Asp Pass | Composite | Rank |
|-----|------|------|----------|-----------|------|
| V-05 | PASS | PASS | 32/32 | 100.00 | 1 |
| V-01 | FAIL | PASS | 31/32 | 99.69 | 2 (tie) |
| V-02 | PASS | FAIL | 31/32 | 99.69 | 2 (tie) |
| V-03 | FAIL (boundary) | FAIL (boundary) | 30/32 | 99.38 | 4 (tie) |
| V-04 | FAIL | FAIL | 30/32 | 99.38 | 4 (tie) |

---

## Criterion Evaluation

### Essential C-01 to C-05: PASS all variations

All five carry the complete v12 baseline. No essential failures.

### Recommended C-06 to C-08: PASS all variations

### Aspirational C-09 to C-38: PASS all variations

All variations inherit the v12 V-05 ceiling. Key confirmations:
- **C-35**: Top-level rule headings encode failure class in all variations
- **C-37**: ENFORCEMENT STACK NOTE uses forward-reference pointers in all variations
- **C-38**: Per-rule reader positions present in all variations (Rule 1: "a committing engineer checking for missing absence declarations"; Rule 2: "a skill-reference consumer disambiguating a reference"; Rule 3: C-36 framing)
- **C-28, C-32**: Existence assertion in heading and forward-scope Applies-to confirmed in all variations

---

### C-39: ENFORCEMENT STACK NOTE reduced to pure interdependency statement

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **FAIL** | NOTE carries forward-refs (C-37 PASS) but retains all three "prevents..." sentences alongside them. Forward-refs present, NOTE not exclusively the interdependency statement. |
| V-02 | **PASS** | NOTE collapsed to pure interdependency: `"Each addresses an independent failure mode -- failure class encoded in each rule's heading above. No layer substitutes for another; the three rules address independent failure modes. All three must pass."` No "prevents..." prose retained. |
| V-03 | **FAIL** (boundary) | NOTE retains one "prevents..." sentence (Rule 1 only). C-39 tests total exclusion -- any retained "prevents..." prose fails regardless of partial cleanup. |
| V-04 | **FAIL** | NOTE retains all three "prevents..." sentences. Same failure as V-01 without the consulting directory. |
| V-05 | **PASS** | NOTE collapsed identically to V-02. Pure interdependency declaration, no supplementary content. |

**Independence test**: V-01 achieves C-40 PASS while retaining the "prevents..." prose (C-39 FAIL). The directory at block entrance and the NOTE after Rule 3 are structurally separate. Adding the directory does not trigger NOTE cleanup.

---

### C-40: Per-rule reader positions surfaced as an explicit consulting directory

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **PASS** | Named `Consulting Directory:` block at block entrance before Rule 1. All three routes listed: committing engineers (Rule 1), skill-reference consumers (Rule 2), committing engineers and reviewers (Rule 3). Role, rule number, and decision act named for each. |
| V-02 | **FAIL** | No consulting directory. Per-rule reader positions present in each rule body (C-38 PASS) but not consolidated. Reader must scan rule bodies to identify their rule. Confirms C-40 is not implied by C-38. |
| V-03 | **FAIL** (boundary) | Directory present but routes only 2 of 3 roles -- skill-reference consumers (Rule 2) omitted. C-40 requires all three routes together. Confirms criterion tests routing-map completeness, not mere directory presence. |
| V-04 | **FAIL** | No directory, no per-rule reader positions beyond C-36 baseline. Both C-39 and C-40 absent. |
| V-05 | **PASS** | Named `Consulting Directory:` block identical to V-01. All three roles, rules, and decision acts. C-38 per-rule positions also present in each rule body. |

**Independence test**: V-02 achieves C-39 PASS (pure NOTE) while failing C-40 (no directory). Collapsing the NOTE does not create a directory. Structurally separate locations confirmed.

---

## Composite Score Detail

| Var | Asp Pass | Composite |
|-----|----------|-----------|
| V-05 | 32/32 | **100.00** |
| V-01 | 31/32 | **99.69** |
| V-02 | 31/32 | **99.69** |
| V-03 | 30/32 | **99.38** |
| V-04 | 30/32 | **99.38** |

All variations pass the golden threshold.

---

## Boundary Case Analysis

**V-03 double boundary** confirms both criteria test total-coverage properties:
- C-39: "exclusively" -- any retained "prevents..." sentence fails, regardless of how many were removed
- C-40: "all three routes" -- any missing role fails, regardless of how many were included

The two boundary failures are structurally independent -- a partial NOTE cleanup cannot rescue a partial directory, and vice versa.

---

## Excellence Signals from V-05

**EX-01 -- Pure interdependency NOTE**: C-35 + C-37 transfer failure-mode ownership to the top-level headings. Once that transfer is complete, the "prevents..." prose in the NOTE is duplicating information the headings now own. V-05 makes the transfer explicit by eliminating it -- the NOTE's only remaining load-bearing content is the stack coordination claim.

**EX-02 -- Consulting directory as block-level routing map**: C-38 places reader positions inside each rule body -- a reader must enter the rule to find their position. C-40 lifts the routing map to the block entrance -- "which rule is mine?" is answerable by scanning the directory without entering any rule body. The "table of contents" pattern applied to multi-role consulting.

**EX-03 -- Structural independence of the two gains**: V-01 proves C-40 without C-39; V-02 proves C-39 without C-40. The two improvements operate at separate structural locations (block entrance vs. NOTE after Rule 3) and can be adopted independently.

---

## R14 Candidate Signals

1. **Directory entry granularity**: entries name role, rule, and decision-act -- candidate for also naming the specific output section (Finding field, action field) the reader will land on
2. **NOTE heading-index pointer**: `"failure class encoded in each rule's heading above"` references headings as a unit -- candidate for an explicit numbered heading index making the NOTE an explicit taxonomy pointer
3. **Directory scope annotation**: consulting directory is a structural block inside STANDING RULES but is not subject to a Rule 3 `Applies-to` annotation -- candidate for whether block-level declarations in the STANDING RULES context require their own scope declaration

---

## Rubric Health

Subsumption chains confirmed sound:
- C-37 <- C-39: V-01 and V-03 confirm C-37 PASS does not imply C-39 PASS
- C-38 <- C-40: V-02 and V-03 confirm C-38 PASS does not imply C-40 PASS
- Full upstream chain C-40 -> C-38 -> C-36 -> ... -> C-20 confirmed via inherited baseline

Denominator 32 confirmed correct. No scoring anomalies.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["pure-interdependency-note: once C-35+C-37 transfer failure-class ownership to top-level headings, the NOTE's only load-bearing content is the stack coordination claim -- any retained explanatory prose is now duplication", "consulting-directory-as-routing-map: lifting per-rule reader positions to a named block at the STANDING RULES entrance answers 'which rule is mine?' without rule-by-rule scanning -- the table-of-contents pattern for multi-role consulting", "structural-independence-of-note-cleanup-and-directory: V-01 proves C-40 without C-39; V-02 proves C-39 without C-40; the two improvements operate at separate structural locations and are independently achievable"]}
```
* |
| V-01 | 31/32 | 90 + (31/32)*10 | **99.69** |
| V-02 | 31/32 | 90 + (31/32)*10 | **99.69** |
| V-03 | 30/32 | 90 + (30/32)*10 | **99.38** |
| V-04 | 30/32 | 90 + (30/32)*10 | **99.38** |

All variations pass the golden threshold (all 5 essential pass + composite >= 80).

---

## Boundary Case Analysis

**V-03 double boundary**: Both C-39 and C-40 fail at their boundary conditions -- C-39 retains exactly one "prevents..." sentence (Rule 1 only, Rules 2 and 3 stripped); C-40 has a directory structure but covers only 2 of 3 reader roles. Both criteria test total-coverage properties:
- C-39: "exclusively" the interdependency statement -- any retained prose fails regardless of how much was cleaned up
- C-40: "all three reader routes" -- any missing route fails regardless of how many were included

**V-03 confirms isolability**: The boundary failures are structurally independent -- a partial NOTE cleanup and a partial directory cannot rescue each other. 30/32 is the correct score.

---

## Excellence Signals from V-05

**EX-01 -- Pure interdependency NOTE**: Once C-37 collapses failure-class labels to forward-refs, the NOTE has exactly one load-bearing function remaining: declaring how the three rules relate as a coordinated stack. V-05's NOTE discharges only that function. The "prevents..." prose was doing double duty -- naming failure modes and naming what the NOTE was "about." C-35 + C-37 together transfer failure-mode ownership to the top-level headings, making the "prevents..." prose in the NOTE redundant. V-05 makes this transfer explicit by eliminating it.

**EX-02 -- Consulting directory as block-level routing map**: The directory is structurally distinct from per-rule reader positions. C-38 places the reader position inside each rule body -- a reader must enter the rule to find it. C-40 lifts the routing map to the block entrance -- a reader can identify the right rule before entering any body. V-05's directory names role, rule number, and decision act in a single scannable block. This is the "table of contents" pattern applied to multi-role consulting: it answers "which rule is mine?" without requiring rule-by-rule scanning.

**EX-03 -- Structural independence of the two gains**: V-01 proves C-40 is achievable without C-39 (directory PASS, NOTE FAIL). V-02 proves C-39 is achievable without C-40 (NOTE PASS, directory FAIL). V-05 achieves both. The two improvements do not interfere or require each other. They operate at structurally separate locations and can be adopted independently -- this is the independence property the rubric requires.

---

## R14 Candidate Signals (from V-05)

Three patterns in V-05 that are passing but have untested refinements:

1. **Directory entry decision-act granularity**: Directory entries use short parenthetical decision-acts (`checking for undeclared absences before commit`). Candidate: should each entry also name the specific output section the reader will land on (e.g., `Rule 1 -- Finding fields for absence-drift dimensions`)? This would add a third-level routing pointer beyond role and rule.

2. **NOTE heading-index pointer**: The NOTE phrase `"failure class encoded in each rule's heading above"` references the heading collection as a unit without listing the headings. Candidate: should the NOTE carry an explicit numbered heading index (`Rule 1: Absence Drift, Rule 2: Reference Ambiguity, Rule 3: Constraint Scope Gaps`), making the NOTE an explicit taxonomy pointer rather than only an interdependency declaration? This would extend C-39 (pure interdependency) toward a richer taxonomic function.

3. **Directory scope annotation**: The consulting directory block is not itself subject to a Rule 3 `Applies-to` annotation. Candidate: should a block-level declaration inside the STANDING RULES context carry its own scope declaration? Rule 3 governs "all Rule declarations" -- the directory is not a Rule but is a structural block within the STANDING RULES context. Whether Rule 3's scope covers block-level declarations is untested.

---

## Rubric Health

All 40 criteria independently testable through the five-variation matrix. The subsumption chains are sound:
- C-37 <- C-39: V-01 and V-03 confirm C-37 PASS does not imply C-39 PASS
- C-38 <- C-40: V-02 and V-03 confirm C-38 PASS does not imply C-40 PASS
- C-40 -> C-38 -> C-36 -> C-33 -> C-29 -> C-26 -> C-24 -> C-22 -> C-20: all upstream criteria confirmed pass in all variations via inherited baseline

No scoring anomalies. Denominator 32 confirmed correct.
