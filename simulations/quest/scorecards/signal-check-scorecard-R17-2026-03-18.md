Scorecard written to `simulations/quest/scorecards/signal-check-scorecard-R17-2026-03-18.md`.

---

## R17 Scoring Summary

| Var | Asp | Composite | Key finding |
|-----|-----|-----------|-------------|
| V-01 | 35/38 | 99.21 | Dual baseline: no count (C-44 FAIL), no index (C-45 FAIL) |
| V-02 | 36/38 | 99.47 | C-44 PASS only -- proves C-44 alone cannot reach C-46 |
| V-03 | 36/38 | 99.47 | C-45 PASS only -- proves C-45 alone cannot reach C-46 |
| V-04 | 37/38 | 99.74 | C-44+C-45 PASS, C-46 FAIL -- counts mismatch (4 != 3); critical boundary |
| **V-05** | **38/38** | **100.00** | C-46 PASS -- counts match (3 = 3) from two independent structures |

**All essential pass**: true | **New patterns**: none (C-46 closes the cross-count loop; no R18 axis identified from V-05)

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": []}
```
-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Four-item preflight structure (CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE) | PASS | PASS | PASS | PASS | PASS |
| C-02 | STATUS field with three canonical states (OK / FLAG / OPEN) | PASS | PASS | PASS | PASS | PASS |
| C-03 | Advisory framing declared at output header | PASS | PASS | PASS | PASS | PASS |
| C-04 | Not-a-verdict framing in readiness summary | PASS | PASS | PASS | PASS | PASS |
| C-05 | Advisory register maintained throughout output | PASS | PASS | PASS | PASS | PASS |

Evidence (same across all): Header declares "Think of this as a preflight check... Nothing here blocks you from proceeding." READINESS SUMMARY section instructions frame as "pilot briefing -- not a verdict. The team decides." STATUS field defined as OK/FLAG/OPEN in all variations.

### Recommended (C-06 to C-08) -- All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Readiness summary section present | PASS | PASS | PASS | PASS | PASS |
| C-07 | CROSS-ITEM PATTERNS section present | PASS | PASS | PASS | PASS | PASS |
| C-08 | MISSING SIGNAL GUIDE section present | PASS | PASS | PASS | PASS | PASS |

Evidence: `=== READINESS SUMMARY ===`, `=== CROSS-ITEM PATTERNS ===`, `=== MISSING SIGNAL GUIDE ===` all present in the invariant body across all variations.

### Aspirational C-09 through C-43 -- All Variations (Invariant Block)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|-----------|------|------|------|------|------|---------------|
| C-09 | Named STANDING RULES block present | PASS | PASS | PASS | PASS | PASS | `STANDING RULES` heading present |
| C-10 | STANDING RULES block contains Rule 1 and Rule 2 | PASS | PASS | PASS | PASS | PASS | `Rule 1 -- Absence Drift`, `Rule 2 -- Reference Ambiguity` present |
| C-11 | Readiness summary uses pilot-briefing language | PASS | PASS | PASS | PASS | PASS | "Frame as pilot briefing -- not a verdict" embedded in section instructions |
| C-12 | Four dimensions with consistent labeling | PASS | PASS | PASS | PASS | PASS | Items 1-4: CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE with STATUS/Basis/Finding/Action structure |
| C-13 | MISSING SIGNAL GUIDE names each missing signal type | PASS | PASS | PASS | PASS | PASS | Guide lines name dimension gap + `/namespace:skill` + output produced |
| C-14 | STANDING RULES block precedes all inventory and analysis | PASS | PASS | PASS | PASS | PASS | STANDING RULES -> GATHER YOUR SIGNALS -> READINESS SUMMARY -> PREFLIGHT CHECK ordering |
| C-15 | Each dimension specifies required verbatim absence phrases | PASS | PASS | PASS | PASS | PASS | Each of the four items carries a "Required verbatim absence phrase" block with exact wording |
| C-16 | Every constraint enumerates all output locations it governs | PASS | PASS | PASS | PASS | PASS | Rule 1 Applies-to: 7 locations; Rule 2 Applies-to: 6 locations; Rule 3 Applies-to: self + future rules |
| C-17 | Verbatim absence phrases embedded at point of use | PASS | PASS | PASS | PASS | PASS | Each dimension carries its phrase inline, not only in a reference table |
| C-18 | Advisory register carried structurally through framing vocabulary | PASS | PASS | PASS | PASS | PASS | Section headers: "=== GATHER YOUR SIGNALS ===", "preflight check", "pilot", "The team decides" |
| C-19 | Triple enforcement stack declared as a unit with interdependency named | PASS | PASS | PASS | PASS | PASS | ENFORCEMENT STACK NOTE: "form a coordinated enforcement stack... No layer substitutes for another" |
| C-20 | Location-enumeration requirement expressed as named meta-rule | PASS | PASS | PASS | PASS | PASS | Rule 3 in STANDING RULES block is a named meta-rule governing all rule declarations |
| C-21 | Each rule assigned a named failure class | PASS | PASS | PASS | PASS | PASS | Rule 1 = Absence Drift; Rule 2 = Reference Ambiguity; Rule 3 = Constraint Scope Gaps |
| C-22 | Meta-rule includes temporal activation gate | PASS | PASS | PASS | PASS | PASS | "Scope must be discharged at rule-creation time, not retroactively" |
| C-23 | Meta-rule self-application declared in rule body | PASS | PASS | PASS | PASS | PASS | "This requirement self-applies: Rule 3 itself declares its scope below." |
| C-24 | Activation gate framed as rule-validity condition | PASS | PASS | PASS | PASS | PASS | "a Rule that has not declared its scope does not exist as an active rule" |
| C-25 | Body self-application includes proximate scope pointer | PASS | PASS | PASS | PASS | PASS | "Rule 3 itself declares its scope below" -- directional pointer "below" commits to co-location |
| C-26 | Activation gate carries both obligation and validity framing | PASS | PASS | PASS | PASS | PASS | Obligation: "every Rule... must declare all output locations"; Validity: "does not exist as an active rule" |
| C-27 | Validity condition uses rule-existence framing | PASS | PASS | PASS | PASS | PASS | "It does not exist as an active rule" (ontological, not status-suspension) |
| C-28 | Rule name encodes existence assertion from heading alone | PASS | PASS | PASS | PASS | PASS | Rule 3 heading: "RULES WITHOUT DECLARED SCOPE DO NOT EXIST" |
| C-29 | Dual register expressed as structurally labeled named sections | PASS | PASS | PASS | PASS | PASS | "Obligation:" and "Existence condition:" labeled sections with non-substitutability declaration |
| C-30 | Rule body names inadequacy of status framing before existence framing | PASS | PASS | PASS | PASS | PASS | "'Not operative' understates the condition -- an inoperative rule is still a declared object with suspended force." |
| C-31 | Temporal gate expressed as "at rule-creation time" | PASS | PASS | PASS | PASS | PASS | "Scope must be discharged at rule-creation time, not retroactively." |
| C-32 | Location annotation explicitly covers rules not yet written | PASS | PASS | PASS | PASS | PASS | "Applies to: all Rule declarations... including Rule 3 itself and any rule added in the future." |
| C-33 | Non-substitutability assigns distinct function description to each register | PASS | PASS | PASS | PASS | PASS | "the obligation tells a committing engineer reading for what to fix; the existence condition tells a reviewer reading for what is already lost" |
| C-34 | Each rule heading encodes failure class | PASS | PASS | PASS | PASS | PASS | "Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:", "Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:", "Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:" |
| C-35 | Failure class in top-level rule heading | PASS | PASS | PASS | PASS | PASS | All three top-level rule headings embed failure class label |
| C-36 | Reader position named in function framing | PASS | PASS | PASS | PASS | PASS | Rule 3: "the obligation tells a committing engineer reading for what to fix; the existence condition tells a reviewer reading for what is already lost" |
| C-37 | ENFORCEMENT STACK NOTE collapses per-rule labels to forward-references | PASS | PASS | PASS | PASS | PASS | "failure class encoded in each rule's heading above" -- forward-reference, not inline restatement |
| C-38 | Each rule names its own reader position keyed to its failure mode | PASS | PASS | PASS | PASS | PASS | Rule 1: "A committing engineer checking for missing absence declarations consults this rule"; Rule 2: "A skill-reference consumer disambiguating a reference consults this rule"; Rule 3: C-36 framing |
| C-39 | NOTE reduced to pure interdependency statement | PASS | PASS | PASS | PASS | PASS | NOTE content: coordinated stack + no-layer-substitutes + independent failure modes + attribution pointer only |
| C-40 | Per-rule reader positions surfaced as consulting directory | PASS | PASS | PASS | PASS | PASS | Named "Consulting Directory:" block routes committing engineers -> Rule 1, skill-reference consumers -> Rule 2, committing engineers and reviewers -> Rule 3 |
| C-41 | Pure interdependency NOTE attributes failure-mode ownership to top-level headings | PASS | PASS | PASS | PASS | PASS | "failure class encoded in each rule's heading above" -- self-explaining transfer attribution present in all variations' NOTE |
| C-42 | Consulting directory carries explicit completeness assertion | PASS | PASS | PASS | PASS | PASS | All variations have a completeness assertion as the directory's final line (form varies by variation) |
| C-43 | Completeness assertion uses all-roles claim form (not count-annotation) | PASS | PASS | PASS | PASS | PASS | V-01: "All reader roles for this block are listed above." -- propositional form, no count required |

C-09 through C-43 subtotal: 35/35 for all five variations.

---

### Aspirational C-44 to C-46 -- Per-Variation Discriminators

#### C-44: All-roles claim includes embedded count qualifier

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | "All reader roles for this block are listed above." -- no count qualifier embedded; propositional form only; satisfies C-43, not C-44 |
| V-02 | PASS | "All 3 reader roles for this block are listed above." -- count "3" nested as numeral qualifier within the noun phrase; propositional form preserved with arithmetic redundancy added |
| V-03 | FAIL | "All reader roles for this block are listed above." -- unqualified, identical to V-01 directory footer; C-44 precondition absent means C-46 unreachable regardless of C-45 |
| V-04 | PASS | "All 4 reader roles for this block are listed above." -- count "4" nested as numeral qualifier; propositional form preserved; count present and arithmetically cross-checkable even though the count overstates the actual three directory entries |
| V-05 | PASS | "All 3 reader roles for this block are listed above." -- count "3" nested as numeral qualifier; propositional form preserved; count matches NOTE entry count (see C-46) |

#### C-45: Failure-mode ownership attribution extended with parenthetical heading index

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | "failure class encoded in each rule's heading above." -- general attribution, headings named as a set; no parenthetical specifying which heading owns which class; satisfies C-41, not C-45 |
| V-02 | FAIL | "failure class encoded in each rule's heading above." -- identical to V-01 NOTE; C-44 PASS but C-45 FAIL; confirms C-44 and C-45 are independently testable; C-46 unreachable (C-45 precondition absent) |
| V-03 | PASS | "failure class encoded in each rule's heading above (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)." -- parenthetical heading index embedded as extension of attribution phrase; 3 entries; heading-index content only, NOTE pure-interdependency character preserved |
| V-04 | PASS | "(Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)" parenthetical present; 3 entries; identical NOTE form to V-03/V-05 |
| V-05 | PASS | "(Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)" parenthetical present; 3 entries; NOTE pure-interdependency form preserved |

#### C-46: Dual count consistency -- C-44 count and C-45 entry count numerically consistent

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | Precondition failure: C-44 FAIL (no count in directory) and C-45 FAIL (no index in NOTE); neither structure carries a count to compare; C-46 cannot fire |
| V-02 | FAIL | Precondition failure: C-44 PASS (directory count = 3) but C-45 FAIL (no countable index in NOTE); the C-45 precondition is absent; no NOTE entry count to compare against directory count "3"; C-46 cannot fire |
| V-03 | FAIL | Precondition failure: C-45 PASS (NOTE index = 3 entries) but C-44 FAIL (no count in directory claim); the C-44 precondition is absent; no directory count to compare against NOTE entry count "3"; C-46 cannot fire |
| V-04 | FAIL | Both preconditions satisfied: C-44 PASS (directory count = 4), C-45 PASS (NOTE entries = 3). Counts mismatched: 4 != 3. Inconsistency detectable from two structures alone without reading any rule body; neither structure is individually malformed but they cannot both be correct. C-46 FAIL: cross-count consistency violated. Critical R17 discriminator proving C-44 + C-45 != C-46. |
| V-05 | PASS | Both preconditions satisfied: C-44 PASS (directory count = 3), C-45 PASS (NOTE entries = 3). Counts match: 3 = 3. Cross-check passes: directory counts reader roles; NOTE counts STANDING RULES rules; structurally independent but numerically consistent. Reader can verify without reading any rule body. |

---

## Summary Score Table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 to C-05 (Essential) | 5/5 PASS | 5/5 PASS | 5/5 PASS | 5/5 PASS | 5/5 PASS |
| C-06 to C-08 (Recommended) | 3/3 PASS | 3/3 PASS | 3/3 PASS | 3/3 PASS | 3/3 PASS |
| C-09 to C-43 (Asp.) | 35 PASS | 35 PASS | 35 PASS | 35 PASS | 35 PASS |
| C-44 | FAIL | PASS | FAIL | PASS | PASS |
| C-45 | FAIL | FAIL | PASS | PASS | PASS |
| C-46 | FAIL | FAIL | FAIL | FAIL | PASS |
| Asp. pass / 38 | 35/38 | 36/38 | 36/38 | 37/38 | 38/38 |
| Composite | 99.21 | 99.47 | 99.47 | 99.74 | 100.00 |
| All essential pass? | YES | YES | YES | YES | YES |
| Meets golden threshold? | YES | YES | YES | YES | YES |

---

## Ranking

1. V-05 -- 100.00 (38/38) -- R17 ceiling; C-46 satisfied; counts 3=3 across both structures
2. V-04 -- 99.74 (37/38) -- C-44 PASS + C-45 PASS; C-46 fails on count mismatch (4 != 3); critical boundary variation
3. V-02 -- 99.47 (36/38) -- C-44 axis only; C-45/C-46 absent
3. V-03 -- 99.47 (36/38) -- C-45 axis only; C-44/C-46 absent
5. V-01 -- 99.21 (35/38) -- Dual regression baseline; neither C-44 nor C-45 satisfied

V-02 and V-03 tie at 99.47, ranked jointly at position 3.

---

## Excellence Signals from V-05

**Pattern 1: Count as qualifier, not assertion mechanism.** V-05 preserves C-43's propositional form ("All reader roles... are listed above") while nesting a count within the noun phrase ("All 3 reader roles..."). The count is subordinate to the proposition -- a qualifier that adds arithmetic redundancy without replacing the claim. V-04 demonstrates this form is satisfiable with a wrong count, which is why C-46 is an independent criterion.

**Pattern 2: Cross-count consistency from structurally independent sources.** V-05 produces count "3" from two structures that count different things: the directory counts reader roles (3 entries: committing engineers / skill-reference consumers / committing engineers and reviewers); the NOTE parenthetical counts STANDING RULES rules (3 entries: Rule 1 / Rule 2 / Rule 3). These counts happen to match and are independently derivable -- they are not mutually derived. A reader cross-checking the two structures can verify consistency without reading any rule body.

**Pattern 3: V-04 as the distinguishing boundary.** The structural element that makes C-46 a separately testable criterion is V-04's mismatched counts (directory claims 4, NOTE has 3). Without V-04, C-46 would be indistinguishable from "C-44 AND C-45" by any example in the series. V-04's deliberate count mismatch proves that C-44 PASS + C-45 PASS does not imply C-46 PASS.

**Live R18 axis**: None identified. C-46 closes the cross-count consistency loop. No further structural element visible in V-05 that would warrant extraction. The two independent count structures (directory footer and NOTE parenthetical) are fully populated and consistent.

---

## Result JSON

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": []}
```
