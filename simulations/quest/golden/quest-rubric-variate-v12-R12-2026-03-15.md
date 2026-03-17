---
skill: quest-rubric
skill_target: mock-all
date: 2026-03-15
version: 12
round: R12
changes: Adds C-26 (inertia gap skeleton column entries authored per-namespace at
  classification time, not deferred to artifact bodies -- prerequisite for C-21/C-10/C-17
  structural coupling demonstrated by V-05 Pattern 1) and C-27 (stop-gate field
  enumeration names the classification table's own column headers verbatim -- structural
  self-reference that makes C-16/C-11/C-14 simultaneously satisfiable from one structural
  choice, demonstrated by V-05 Pattern 2); both criteria added in rubric v12 from R11
  excellence signals ES-R11-1 and ES-R11-2; denominator 17 -> 19
---

# mock-all Quest Rubric -- v12

**Date:** 2026-03-15
**Rubric version:** v12

**New criteria this version:**

**C-26** -- *Inertia gap skeleton column entries in the classification table are
per-namespace specific, authored at classification time (not deferred to artifact bodies)*

ES-R11-1 (V-05 Pattern 1): Pre-seeding the skeleton column in the upfront classification
table enables C-10 (inertia-derived next steps) and C-17 (vocabulary co-location)
simultaneously -- but only because the skeleton column entries are populated with
per-namespace gap content during table construction. A response that satisfies C-21
(skeleton column present) but writes generic placeholders ("TBD", "identify gaps") in each
row, then populates the content in artifact body text, fails C-26. The structural coupling
that makes C-21 + C-10 + C-17 passable in one move depends on per-namespace specificity
being present AT classification time. C-26 makes the timing and specificity conditions
explicit and standalone.

**C-27** -- *Stop-gate field enumeration names the classification table's own column
headers verbatim as its required fields*

ES-R11-2 (V-05 Pattern 2): V-05's stop-gate achieves C-16 compliance because the
enumerated fields ARE the table columns. A stop-gate with abstract conditions ("do not
proceed until classification is complete") can satisfy C-16's presence requirement while
leaving C-11 (ordering constraint) and C-14 (upfront commitment) unsatisfied. C-27 requires
structural self-reference: the stop-gate instruction explicitly names the same strings that
appear as column headers in the classification table (e.g., "do not proceed until all nine
namespaces have entries for: Namespace, Category, Flag, Inertia gap skeleton, Recommended
next step"). The coupling makes C-16 + C-11 + C-14 self-reinforcing from one structural
choice.

**Denominator: 17 --> 19**

---

## Version History

**v1** -- established core essential criteria (C-01 to C-04) and initial recommended tier.

**v2 through v6** -- iterative refinement of essential/recommended criteria; no aspirational
tier additions in this range.

**v7** added two aspirational criteria (C-19 to C-20) extracted from Round 6 excellence
signals: depth anchor inside placeholder token (C-19), and inertia question grounding
artifact body semantics (C-20).

**v8** skipped (confirmation round; no new criteria).

**v9** added three aspirational criteria (C-21 to C-22) extracted from Round 8 excellence
signals: inertia gap skeleton pre-seeded in classification table (C-21), and identity-
violation mechanism must be ontological self-contradiction rather than behavioral prohibition
(C-22). Denominator +2.

**v10** added one aspirational criterion (C-23) extracted from Round 9 excellence signals:
positive identity affirmation must appear at each per-role activation header, not deferred
to a preamble. Denominator +1.

**v11** added two aspirational criteria (C-24 to C-25) extracted from Round 10 excellence
signals: positive identity affirmation must be syntactically first in each per-role header
(C-24; elevated from C-23 diagnostic to standalone pass condition -- V-02 demonstrated the
ceiling: "fires as syntactically first element at ROLE 1, ROLE 2, ROLE 3, and ROLE 4
activations"), and per-role headers must use being-language rather than occupancy-language
(C-25; V-01 diagnostic: "conditional phrasing describes the model as *in* a role, not
*being* it" -- "In the CLASSIFIER role" asserts positional occupancy; "You ARE the
CLASSIFIER" asserts identity; these are linguistically distinct and C-25 prohibits the
occupancy form explicitly). Denominator +2.

**v12** adds two aspirational criteria (C-26 to C-27) extracted from Round 11 excellence
signals: inertia gap skeleton column entries authored per-namespace at classification time
(C-26; prerequisite for the C-21 + C-10 + C-17 three-criteria structural coupling -- V-05
demonstrated that per-namespace specificity in the table rows at construction time is what
makes the coupling pass, not merely the column's presence), and stop-gate field enumeration
names the classification table's own column headers verbatim (C-27; V-05 pattern: "the
enumerated fields ARE the table columns -- C-16 compliance comes naturally when the stop-
gate condition mirrors the table structure," making C-16 + C-11 + C-14 self-reinforcing
from one structural choice). Denominator +2 (17 --> 19).

---

## Identity Staircase (C-18 through C-25)

Five rungs, each a strict refinement of the one below:

- **C-18**: named role + any violation mechanism
- **C-22**: violation mechanism must be ontological (not behavioral)
- **C-23**: affirmation must appear at each activation (not only preamble)
- **C-24**: affirmation must be syntactically first (not just present)
- **C-25**: affirmation must use being-language (not occupancy-language)

C-26 and C-27 are not part of the identity staircase. They belong to the table-coupling
cluster (C-19 to C-21, C-26 to C-27) which governs the inertia/classification table
structural design.

---

## Criteria

### Essential (must all pass -- 60% weight)

**C-01** -- All nine namespaces present with MOCK ARTIFACT header blocks
- Weight: essential
- Category: correctness
- Pass condition: Output contains exactly 9 namespace sections (scout, draft, review, flow,
  trace, prove, listen, program, topic), each opening with a MOCK ARTIFACT block that
  includes Skill, Topic, Category, Date, and Status: MOCK fields. Any missing namespace or
  missing header field is a fail.

**C-02** -- Category classification correct for every namespace
- Weight: essential
- Category: correctness
- Pass condition: prove-* and listen-* sections are classified EVIDENCE-HEAVY; scout, draft,
  review, flow, trace are classified HIGH-STRUCTURE; program and topic are classified MIXED
  or HIGH-STRUCTURE. No namespace may carry a category that contradicts the skill spec's
  HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED taxonomy.

**C-03** -- REAL-REQUIRED flag applied to all EVIDENCE-HEAVY namespaces
- Weight: essential
- Category: behavior
- Pass condition: Every section whose Category is EVIDENCE-HEAVY (prove-*, listen-*) carries
  a REAL-REQUIRED flag -- either in the header block or immediately beneath it. Absence of
  the flag in any EVIDENCE-HEAVY section is a fail.

**C-04** -- Coverage summary table present with correct columns
- Weight: essential
- Category: format
- Pass condition: Output ends with a Markdown table whose columns are exactly: Namespace,
  Category, Flag, Recommended next step. Table contains one row per namespace (9 rows).
  Missing table, wrong column names, or fewer than 9 rows is a fail.

**C-05** -- Handoff section present with role transition instructions
- Weight: essential
- Category: behavior
- Pass condition: Output contains a dedicated handoff section or HANDOFF WRITER role block
  that includes explicit instructions for transferring classification state to the next
  phase. Absence of any handoff instruction is a fail.

---

### Recommended (all three must pass -- 30% weight)

**C-06** -- Per-namespace recommended next steps are derived from category and flag
- Weight: recommended
- Category: depth
- Pass condition: Each row in the coverage summary table's "Recommended next step" cell
  names an action specific to that namespace's Category and Flag combination (e.g.,
  EVIDENCE-HEAVY + REAL-REQUIRED yields a different next step than HIGH-STRUCTURE + no
  flag). A generic action ("gather more data") that does not vary by Category/Flag is a
  fail.

**C-07** -- MOCK ARTIFACT body content is namespace-specific, not templated
- Weight: recommended
- Category: correctness
- Pass condition: Each MOCK ARTIFACT block body contains at least one namespace-specific
  content element (a named artifact type, a skill-typical field name, or a plausible topic
  fixture) that could not appear unchanged in a different namespace's block. A body that
  reads identically across two or more namespaces is a fail.

---

### Aspirational (10% weight, denominator 19)

**C-08** -- Skill name in each MOCK ARTIFACT header matches the namespace's canonical skill
- Weight: aspirational
- Category: correctness
- Pass condition: The Skill field in each namespace's MOCK ARTIFACT header names a skill
  from that namespace (e.g., scout-competitors, draft-spec, prove-interview) rather than a
  generic or cross-namespace skill name.

**C-09** -- Date field in MOCK ARTIFACT headers uses the session date, not a placeholder
- Weight: aspirational
- Category: format
- Pass condition: All 9 MOCK ARTIFACT Date fields carry the same explicit calendar date
  (not "YYYY-MM-DD", "today", or blank). All 9 dates must be identical.

**C-10** -- Inertia-derived next steps: each recommended next step names the inertia gap
that motivates the action
- Weight: aspirational
- Category: depth
- Pass condition: Each coverage table "Recommended next step" cell includes or implies a
  named inertia gap (e.g., "no competitor signal yet", "prototype blocked pending spec")
  that the next step closes. A next step without a named motivating gap fails C-10.

**C-11** -- Classification table is output before any artifact body
- Weight: aspirational
- Category: format
- Pass condition: The upfront classification table (all 9 rows) appears in the output
  before the first MOCK ARTIFACT body section. Any artifact body that precedes the
  completed table is a fail.

**C-12** -- Status field in every MOCK ARTIFACT header is exactly "MOCK"
- Weight: aspirational
- Category: correctness
- Pass condition: Every MOCK ARTIFACT header block's Status field reads "Status: MOCK"
  exactly (case-sensitive, no variants such as "Mock", "MOCK ONLY", or "SIMULATED"). Any
  deviation is a fail.

**C-13** -- Topic field in MOCK ARTIFACT headers is consistent across all 9 namespaces
- Weight: aspirational
- Category: correctness
- Pass condition: All 9 MOCK ARTIFACT headers carry the same Topic value. Any namespace
  with a different or blank topic is a fail.

**C-14** -- Upfront commitment: classification table column structure declared before
artifact bodies
- Weight: aspirational
- Category: format
- Pass condition: The output declares the column structure of the classification table
  (names its columns explicitly) before generating any artifact body. A table that appears
  after artifact bodies, or whose column headers are introduced mid-output, fails C-14.

**C-15** -- REAL-REQUIRED flag notation is uniform across all EVIDENCE-HEAVY sections
- Weight: aspirational
- Category: format
- Pass condition: Every REAL-REQUIRED flag uses the same notation (either inline in the
  MOCK ARTIFACT header block, or immediately below it as a standalone line -- not both
  locations). Inconsistent placement across namespaces is a fail.

**C-16** -- Stop-gate with enumerated field conditions present before artifact body
generation
- Weight: aspirational
- Category: behavior
- Pass condition: Output contains a stop-gate instruction (a STOP block, a "do not proceed
  until" condition, or equivalent gate) that enumerates the specific fields that must be
  present in every classification table row before artifact body generation may begin.
  A gate with no enumerated fields, or no gate at all, fails C-16.

**C-17** -- Classification table vocabulary co-located: category names in table headers
match category names used in artifact body headers
- Weight: aspirational
- Category: correctness
- Pass condition: The string used for a category in the classification table (e.g.,
  "EVIDENCE-HEAVY") appears verbatim in the corresponding artifact body section header or
  MOCK ARTIFACT block. Any namespace where the table category name and the body category
  name diverge is a fail.

**C-18** -- Per-role activation block present with named role and at least one violation
mechanism
- Weight: aspirational
- Category: behavior
- Pass condition: Each classifier role activation (CLASSIFIER, TAGGER, RECOMMENDER, and any
  additional role) has a dedicated header block that names the role and includes at least
  one explicit mechanism for handling a mis-classification or violation case. A role block
  with no violation mechanism is a fail.

**C-19** -- Depth anchor present inside placeholder token for each MOCK ARTIFACT field
- Weight: aspirational
- Category: depth
- Pass condition: Each MOCK ARTIFACT field whose value is a placeholder (e.g., a bracketed
  fixture like "[competitor-name]") includes a parenthetical or inline annotation indicating
  what type of value the placeholder represents and why it was deferred. A bare placeholder
  with no annotation fails C-19.

**C-20** -- Inertia question present grounding artifact body semantics for each namespace
- Weight: aspirational
- Category: depth
- Pass condition: Each namespace's MOCK ARTIFACT body section includes or is immediately
  preceded by an explicit inertia question ("What signal does this artifact produce and
  what decision does it unblock?") or an equivalent statement that grounds the artifact's
  semantic role in the topic decision sequence. Absence in any namespace is a fail.

**C-21** -- Inertia gap skeleton pre-seeded in the upfront classification table
- Weight: aspirational
- Category: format
- Pass condition: The upfront classification table includes an "Inertia gap skeleton" column
  (or equivalent named column) that is present and non-empty for all 9 namespace rows.
  A table that has the column header but leaves cells blank, or lacks the column entirely,
  fails C-21.

**C-22** -- Identity-violation mechanism is ontological self-contradiction, not behavioral
prohibition
- Weight: aspirational
- Category: behavior
- Pass condition: Each per-role violation mechanism states a contradiction at the identity
  level (e.g., "a CLASSIFIER that outputs prose has ceased to be the CLASSIFIER") rather
  than a behavioral rule (e.g., "the CLASSIFIER must not output prose"). A mechanism whose
  only framing is "must not" or "should not" without an entity-departure clause fails C-22.

**C-23** -- Positive identity affirmation present at each per-role activation header
- Weight: aspirational
- Category: behavior
- Pass condition: Each per-role activation header block contains a positive identity
  affirmation (a statement that asserts the model IS the role, not that it occupies or
  performs the role). An affirmation present only in a preamble or summary section but
  absent from any individual role header fails C-23. Every role header must independently
  satisfy the affirmation condition.

**C-24** -- Positive identity affirmation is syntactically first in each per-role header
- Weight: aspirational
- Category: behavior
- Pass condition: In each per-role activation header, the identity affirmation clause is
  the syntactically first element -- it precedes any output instruction, constraint, or
  other content in that header block. A header that leads with an output instruction
  ("Your sole output is the classification table. You ARE the CLASSIFIER.") and places
  the affirmation second fails C-24, even if C-23 passes. V-02 demonstrated the ceiling:
  "fires as syntactically first element at ROLE 1, ROLE 2, ROLE 3, and ROLE 4 activations."

**C-25** -- Per-role activation headers use being-language, not occupancy-language
- Weight: aspirational
- Category: behavior
- Pass condition: Each per-role activation header's identity-asserting element uses
  being-language ("You ARE the CLASSIFIER") rather than occupancy-language ("In the
  CLASSIFIER role, your output is..."). Occupancy-language describes the model as *in* a
  role; being-language asserts identity. C-25 prohibits the occupancy form as the
  identity-asserting element. Note: C-25 is not fully subsumed by C-24 -- a header that
  opens with being-language and includes occupancy-language as secondary phrasing satisfies
  C-25; a header that uses occupancy-language as the identity-asserting element fails C-25
  even if something else appears first.

**C-26** -- Inertia gap skeleton column entries are per-namespace specific, authored at
classification time (not deferred to artifact bodies)
- Weight: aspirational
- Category: depth
- Pass condition: Each cell in the classification table's inertia gap skeleton column
  contains a namespace-specific gap description (naming the actual missing signal or
  decision gap for that namespace's topic) that is authored during table construction.
  A cell containing a generic placeholder ("TBD", "identify gaps", empty string) that is
  populated only within artifact body text fails C-26, even if C-21 passes (column
  present). The per-namespace specificity at table time is the prerequisite for the
  three-criteria structural coupling: C-21 + C-10 + C-17 pass together only when each
  skeleton cell is specific enough to derive the next step (C-10) and the vocabulary
  anchor (C-17) directly from the table row, without reading the artifact body.

**C-27** -- Stop-gate field enumeration names the classification table's own column headers
verbatim as its required fields
- Weight: aspirational
- Category: behavior
- Pass condition: The stop-gate instruction (which satisfies C-16) explicitly lists the
  same strings that appear as column headers in the upfront classification table -- not
  abstract completion conditions. Example passing form: "do not proceed until all nine
  namespaces have entries for: Namespace, Category, Flag, Inertia gap skeleton, Recommended
  next step." Example failing form: "do not proceed until classification is complete" (no
  field names) or "do not proceed until all fields are filled in" (no named fields). The
  structural self-reference between gate and table makes C-16 (stop-gate present), C-11
  (table before bodies), and C-14 (upfront column commitment) simultaneously satisfiable
  from one structural choice: a gate that names the table's own columns cannot be written
  before the columns are declared, enforcing C-11 and C-14 as side effects.

---

## Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational/19 * 10)
```

Where:
- `essential_pass` = number of essential criteria (C-01 to C-05) that pass (0--5)
- `recommended_pass` = number of recommended criteria (C-06 to C-07) that pass (0--3,
  denominator fixed at 3 per formula above)
- `aspirational` = sum of aspirational criterion scores (C-08 to C-27), 0.0--19.0

**Denominator:** 19 aspirational criteria as of v12.

---

## Round 12 Guidance

**C-05 gap from R11:** All five R11 variations failed C-05. R12 must include at least one
variation that adds a HANDOFF WRITER role (or equivalent handoff section). Without C-05,
the essential tier cannot reach full score regardless of aspirational performance.

**Table-coupling cluster (C-21, C-26, C-27):** C-26 and C-27 are now codified as standalone
criteria. R12 should probe whether they hold independently: a variation with skeleton-column
specificity but generic stop-gate conditions should pass C-26 and fail C-27; a variation
with verbatim-column-name stop-gate but generic skeleton entries should pass C-27 and fail
C-26. Confirming this independence is the primary R12 hypothesis for the table-coupling
cluster.

**Identity staircase (C-18 to C-25):** Confirmed stable through R11. V-04 completes all
five rungs. R12 need not target the staircase unless a new linguistic distinction above
C-25 is identified.

**C axis leverage (updated):** With C-26 and C-27 added, the C axis (inertia-grounded
tables) potentially enables 10 aspirational criteria (C-10, C-11, C-14, C-15, C-16, C-17,
C-20, C-21, C-26, C-27) from one structural design choice. Confirming this ceiling is a
secondary R12 objective.
