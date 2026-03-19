Scorecard written. Now the output with the required JSON block:

---

# /quest:score — signal-check Round 12

## Summary Table

| Var | C-37 | C-38 | Asp Pass | Composite | Rank |
|-----|------|------|----------|-----------|------|
| V-05 | PASS | PASS | 30/30 | 100.00 | 1 |
| V-01 | FAIL | PASS | 29/30 | 99.67 | 2 (tie) |
| V-02 | PASS | FAIL | 29/30 | 99.67 | 2 (tie) |
| V-03 | PASS | FAIL | 29/30 | 99.67 | 2 (tie) |
| V-04 | FAIL | FAIL | 28/30 | 99.33 | 5 |

---

## Criterion Evaluation

### Essential C-01 to C-05: PASS all variations

All five carry the complete v11 baseline. No essential failures.

### Recommended C-06 to C-08: PASS all variations

### Aspirational C-09 to C-36: PASS all variations

All variations inherit the v11 V-05 ceiling. C-34 and C-35 confirmed: top-level rule headings encode failure class in all variations (`Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:`, etc.). C-36 confirmed: Rule 3's non-substitutability declaration names "a committing engineer reading for what to fix" and "a reviewer reading for what is already lost" in all variations.

### C-37 — ENFORCEMENT STACK NOTE forward-reference deduplication

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **FAIL** | NOTE uses inline label `Rule 1 (absence declaration)` -- C-35 satisfied (top-level headings encode failure class) but note re-asserts inline rather than pointing to the heading |
| V-02 | PASS | NOTE uses `Rule 1 -- failure class: see Rule 1 heading above` -- forward-reference pointer replaces inline label |
| V-03 | PASS | Same forward-ref pattern as V-02 |
| V-04 | **FAIL** | NOTE uses `Rule 1 (absence declaration)` -- R11 V-05 verbatim; same defect as V-01 |
| V-05 | PASS | Same forward-ref pattern as V-02 |

Precondition confirmed: C-35 PASS in all variations (top-level headings available to point to). V-01 and V-04 demonstrate C-35 does not imply C-37 — the note can still re-assert inline.

### C-38 — Per-rule reader-position keyed to each rule's failure mode

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Rule 1: "A committing engineer checking for missing absence declarations consults this rule..."; Rule 2: "A skill-reference consumer disambiguating a reference consults this rule..."; Rule 3: C-36 framing retained. All three -- universal quantifier discharged |
| V-02 | **FAIL** | Rules 1 and 2 carry no reader-position statement. Rule 3 satisfies C-36. C-36 PASS does not imply C-38 PASS -- universal quantifier requires every rule |
| V-03 | **FAIL** | Rule 1 names reader; Rule 2 absent; Rule 3 retains C-36. Two-out-of-three does not satisfy the universal quantifier -- Rule 2's consulting reader (skill-reference consumer) is missing |
| V-04 | **FAIL** | Rules 1 and 2 absent; only Rule 3 named (C-36). Same as V-02 |
| V-05 | PASS | Identical to V-01 -- all three rules name consulting readers keyed to their failure modes |

V-03 boundary confirmed: C-38 is a genuine universal quantifier. Two out of three is insufficient.

---

## Per-Variation Scores

### V-01: 29/30 aspirational → 99.67
C-37 FAIL (inline note labels retained despite C-35 satisfied). C-38 PASS (all three rules carry reader-position). Shows C-38 does not imply C-37.

### V-02: 29/30 aspirational → 99.67
C-37 PASS (note forward-refs). C-38 FAIL (Rules 1 and 2 absent). Shows C-37 does not imply C-38. C-36 PASS (Rule 3 alone sufficient for C-36, not sufficient for C-38).

### V-03: 29/30 aspirational → 99.67
C-37 PASS. C-38 FAIL — Rule 2 has no reader-position framing. Boundary: Rules 1+3 named, Rule 2 absent. Universal quantifier fails at 2/3 coverage.

### V-04: 28/30 aspirational → 99.33
Both FAIL. R11 V-05 verbatim. Deficit = V-01 deficit + V-02 deficit = 1 + 1 = 2. Confirms independent contribution of exactly one point each.

### V-05: 30/30 aspirational → 100.00
Both PASS. Forward-ref note + all-rules reader-position. Full ceiling.

---

## Ranking

| Rank | Var | Composite | Test |
|------|-----|-----------|------|
| 1 | V-05 | 100.00 | Full ceiling |
| 2 | V-01 | 99.67 | C-38 without C-37 |
| 2 | V-02 | 99.67 | C-37 without C-38 |
| 2 | V-03 | 99.67 | C-38 boundary (2/3 rules) |
| 5 | V-04 | 99.33 | Regression baseline |

---

## Excellence Signals from V-05

**EX-01: Forward-reference deduplication makes the top-level heading the single source of truth for failure-class information.** Once C-35 encodes the failure class in the heading, the ENFORCEMENT STACK NOTE becomes a redundant second copy. Replacing inline labels with forward-reference pointers (`failure class: see Rule N heading above`) eliminates the duplication without losing information — a reader scanning headings gets the taxonomy; a reader consulting the note is directed to the canonical location.

**EX-02: Per-rule reader-position resolves generic "you" to a named role at each rule's point of declaration.** Rule 3's C-36 framing named two reader positions in the dual-register context. Extending this pattern to Rules 1 and 2 — each keyed to that rule's specific failure mode — gives every rule a concrete entry-point for the team member most likely to consult it. A committing engineer goes to Rule 1 for absence-drift; a developer integrating output programmatically goes to Rule 2 for reference-resolution; engineers and reviewers both have explicit handles in Rule 3.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Forward-reference deduplication in ENFORCEMENT STACK NOTE: once top-level rule headings encode the failure class (C-35), the note collapses inline labels to heading pointers, making the heading the single source of truth and the note a pure interdependency statement", "Per-rule reader-position keyed to each rule's failure mode: every rule names its own specific consulting reader and decision act (Rule 1 names the committing engineer checking for missing absence declarations; Rule 2 names the skill-reference consumer disambiguating a reference; Rule 3 retains the dual-register C-36 framing), resolving generic 'you' to a named role at each rule's point of declaration"]}
```
ENFORCEMENT STACK NOTE. |
| V-04 | FAIL | NOTE reads: "Rule 1 (absence declaration) -- prevents silent omissions:" -- same as V-01; R11 V-05 verbatim; no forward-refs. |
| V-05 | PASS | Same forward-ref pattern as V-02 in ENFORCEMENT STACK NOTE. |

C-37 precondition confirmed for all: C-35 is satisfied in all five variations (failure
class in top-level headings). C-37 independently requires the NOTE to eliminate
redundancy. V-01 and V-04 satisfy C-35 but not C-37 -- precondition-not-subsumption
confirmed.

### C-38 -- Per-rule reader-position keyed to each rule's specific failure mode

Pass condition: Every rule in the STANDING RULES block names its own consulting reader
and decision act keyed to that rule's failure mode -- not only Rule 3's
non-substitutability declaration.

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Rule 1 body: "A committing engineer checking for missing absence declarations consults this rule to determine which Finding locations require verbatim phrases when no evidence exists." Rule 2 body: "A skill-reference consumer disambiguating a reference consults this rule to determine whether a skill name in the output can be resolved to a runnable skill." Rule 3: retains C-36 framing. All three rules named -- universal quantifier discharged. |
| V-02 | FAIL | Rules 1 and 2 carry no reader-position consulting statement. Only Rule 3 names reader positions (C-36 framing). Universal quantifier requires every rule; two rules absent -- C-38 fails. C-36 passes (Rule 3 alone sufficient for C-36). |
| V-03 | FAIL | Rule 1 body carries reader-position ("A committing engineer checking for missing absence declarations..."). Rule 3 retains C-36 framing. Rule 2 body carries no reader-position statement. Two out of three does not discharge the universal quantifier. C-38 fails. |
| V-04 | FAIL | Rules 1 and 2 carry no reader-position consulting statements. Only Rule 3 names readers (C-36). Same as V-02 failure. R11 V-05 verbatim -- no per-rule reader framing was present at R11 ceiling. |
| V-05 | PASS | Identical to V-01 for per-rule reader framing: all three rules name their specific consulting reader keyed to their failure mode. Universal quantifier fully discharged. |

V-03 boundary test confirmed: C-38 means every rule -- not most rules. Rule 2's
consulting reader (a skill-reference consumer disambiguating a reference) is distinct
and was present in V-01 and V-05 but absent in V-02 and V-03. The absence of Rule 2
reader-position in V-03 is the operative failure.

---

## Per-Variation Scores

### V-01: C-37 FAIL, C-38 PASS

```
Essential (C-01 to C-05):  5/5 PASS
Recommended (C-06 to C-08): 3/3 PASS
Aspirational (C-09 to C-36): 28/28 PASS
Aspirational C-37: FAIL
Aspirational C-38: PASS

Aspirational pass: 29/30
Composite: 90 + (29/30) * 10 = 90 + 9.6667 = 99.67
```

Failure source: ENFORCEMENT STACK NOTE retains inline failure-class labels despite
C-35 being satisfied. C-38 is independently satisfied -- per-rule reader framing is
present and correct. Demonstrates C-37 and C-38 are independently testable: satisfying
C-38 (body-level reader framing) does not automatically satisfy C-37 (note-level
structural deduplication).

### V-02: C-37 PASS, C-38 FAIL

```
Essential (C-01 to C-05):  5/5 PASS
Recommended (C-06 to C-08): 3/3 PASS
Aspirational (C-09 to C-36): 28/28 PASS
Aspirational C-37: PASS
Aspirational C-38: FAIL

Aspirational pass: 29/30
Composite: 90 + (29/30) * 10 = 90 + 9.6667 = 99.67
```

Failure source: Rules 1 and 2 carry no reader-position consulting statement. C-36
remains satisfied (Rule 3 alone sufficient). Demonstrates C-38 is not discharged by
C-36 alone: the universal quantifier in C-38 requires every rule, and Rules 1 and 2
are absent. Satisfying C-37 (note-level) does not automatically satisfy C-38 (per-rule
body-level).

### V-03: C-37 PASS, C-38 FAIL (boundary)

```
Essential (C-01 to C-05):  5/5 PASS
Recommended (C-06 to C-08): 3/3 PASS
Aspirational (C-09 to C-36): 28/28 PASS
Aspirational C-37: PASS
Aspirational C-38: FAIL

Aspirational pass: 29/30
Composite: 90 + (29/30) * 10 = 90 + 9.6667 = 99.67
```

Failure source: Rule 2 body carries no reader-position statement. Rules 1 and 3 both
name consulting readers. The C-38 universal quantifier is not discharged by two-out-of-
three coverage. Rule 2's failure mode (reference ambiguity) has a distinct consulting
reader -- a skill-reference consumer disambiguating a reference -- but that reader is
not named in Rule 2's body. Boundary test confirmed: partial coverage does not pass.

### V-04: C-37 FAIL, C-38 FAIL (regression baseline)

```
Essential (C-01 to C-05):  5/5 PASS
Recommended (C-06 to C-08): 3/3 PASS
Aspirational (C-09 to C-36): 28/28 PASS
Aspirational C-37: FAIL
Aspirational C-38: FAIL

Aspirational pass: 28/30
Composite: 90 + (28/30) * 10 = 90 + 9.3333 = 99.33
```

This is R11 V-05 verbatim. Both new criteria fail: ENFORCEMENT STACK NOTE uses inline
labels; only Rule 3 names reader positions. C-35 and C-36 pass (headings encode failure
class; Rule 3 non-substitutability names reader roles). The deficit is exactly
V-01-deficit + V-02-deficit = 1 + 1 = 2 points below V-05, confirming the two criteria
contribute exactly one aspirational point each and are independently isolable.

### V-05: C-37 PASS, C-38 PASS (full ceiling)

```
Essential (C-01 to C-05):  5/5 PASS
Recommended (C-06 to C-08): 3/3 PASS
Aspirational (C-09 to C-38): 30/30 PASS

Aspirational pass: 30/30
Composite: 90 + (30/30) * 10 = 90 + 10.00 = 100.00
```

ENFORCEMENT STACK NOTE: "Rule 1 -- failure class: see Rule 1 heading above -- prevents
silent omissions:" -- forward-reference pointer replaces inline label; top-level heading
is single source of truth. Rule 1 body: "A committing engineer checking for missing
absence declarations consults this rule..." Rule 2 body: "A skill-reference consumer
disambiguating a reference consults this rule..." Rule 3: retains C-36 dual-register
framing. All 30 aspirational criteria satisfied.

---

## Ranking

| Rank | Variation | Composite | What it tested |
|------|-----------|-----------|----------------|
| 1 | V-05 | 100.00 | Full ceiling: C-37 PASS + C-38 PASS |
| 2 | V-01 | 99.67 | C-38 only: per-rule reader-position without note dedup |
| 2 | V-02 | 99.67 | C-37 only: note dedup without per-rule reader-position |
| 2 | V-03 | 99.67 | C-38 boundary: 2/3 rules covered does not satisfy universal quantifier |
| 5 | V-04 | 99.33 | Regression baseline: both new criteria fail (R11 V-05 verbatim) |

V-01, V-02, V-03 are score-tied at 99.67 but test structurally distinct hypotheses.
V-01 shows C-38 does not imply C-37. V-02 shows C-36 does not imply C-38. V-03
demonstrates C-38 is a genuine universal quantifier over all rules, not a majority
condition.

---

## Excellence Signals from V-05

These patterns from V-05 caused it to score above all other variations.

### EX-01: Forward-reference deduplication eliminates redundant failure-class encoding

Once C-35 makes the top-level rule heading the source of truth for failure-class
information, the ENFORCEMENT STACK NOTE becomes the second copy. V-05 resolves this
by replacing inline labels with forward-reference pointers ("failure class: see Rule N
heading above"). The heading is now the single location containing the failure-class
label; the note points to it rather than duplicating it. A reader scanning headings
gets the diagnostic taxonomy; a reader consulting the note is directed to the canonical
location. No information is lost; the duplication is eliminated.

Structural location: ENFORCEMENT STACK NOTE per-rule entries.
Triggering condition: C-35 satisfied (failure class in top-level heading) + redundant
inline label present in note = C-37 becomes testable.

### EX-02: Per-rule reader-position makes every rule's consulting use-case concrete

Rule 3's C-36 framing names two reader positions (committing engineer and reviewer) in
the context of the dual-register obligation/existence-condition distinction. V-05
extends this pattern to Rules 1 and 2 by adding a consulting-reader statement keyed
to each rule's own failure mode:

- Rule 1 (absence drift): "A committing engineer checking for missing absence
  declarations consults this rule to determine which Finding locations require verbatim
  phrases when no evidence exists."
- Rule 2 (reference ambiguity): "A skill-reference consumer disambiguating a reference
  consults this rule to determine whether a skill name in the output can be resolved to
  a runnable skill."

The effect: each rule now has a named entry-point for the specific team member
consulting it. A reviewer looking for absence-drift issues goes to Rule 1; a developer
integrating output programmatically goes to Rule 2; engineers and reviewers both have
explicit handles in Rule 3. Generic "you" is resolved to a role at each rule's point
of declaration.

Structural location: Rule 1 and Rule 2 body text, before the Applies-to line.
Triggering condition: C-36 satisfied (Rule 3 named) + Rules 1 and 2 absent = C-38
becomes testable.

---

## R13 Signals Flagged in V-05

Two structural tensions identified that did not yet resolve into rubric criteria:

1. ENFORCEMENT STACK NOTE now contains forward-refs + interdependency declaration +
   three inline failure descriptions ("prevents silent omissions", "prevents reference
   ambiguity", "prevents constraint scope gaps"). After C-37, these descriptions are the
   note's only remaining inline substantive content. Candidate: should they migrate to
   rule body text, making the note a pure interdependency statement with all substantive
   content in rule bodies?

2. Per-rule reader-position consulting statements in Rules 1 and 2 are structurally
   unlabeled prose (appended before Applies-to). Rule 3 has structurally labeled sections
   ("Obligation:", "Existence condition:"). Candidate: should Rules 1 and 2 gain a
   structural label (e.g., "Consulting reader:") parallel to Rule 3's labeled sections,
   making per-rule reader framing surface-parseable across all three rules?

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-05 | 5/5 | 3/3 | 30/30 | 100.00 |
| V-01 | 5/5 | 3/3 | 29/30 | 99.67 |
| V-02 | 5/5 | 3/3 | 29/30 | 99.67 |
| V-03 | 5/5 | 3/3 | 29/30 | 99.67 |
| V-04 | 5/5 | 3/3 | 28/30 | 99.33 |
