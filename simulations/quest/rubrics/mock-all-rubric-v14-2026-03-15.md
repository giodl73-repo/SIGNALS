Written to `simulations/quest/rubrics/mock-all-rubric-v14-2026-03-15.md`.

---

# mock-all Quest Rubric -- v14

## New criterion extracted from Round 13

**C-30** -- *ROLE 2 REAL-REQUIRED rationale content is pre-authored in the skill template body, not delegated to model-time generation*

Extracted from V-03 C-13 PARTIAL. C-13 requires a ROLE 2 rationale block for REAL-REQUIRED namespaces. V-03's template supplies only a delegation instruction (`{one sentence explaining why real artifacts are required for this namespace}`) with no seed content — authorship is delegated to model execution. V-01 passes C-13 because the template pre-authors `"prove: requires actual experiment data; listen: requires real user feedback; compliance namespace: requires traceable real-world sources."` V-02 passes C-13 because its placeholder embeds seed text: `"Evidence validity depends on authentic signals -- synthetic data cannot substitute..."` C-30 adds the provenance condition: same requirement as C-13 (rationale block present), plus authorship must reside in the template. C-30 is the authorship-residency ceiling above C-13, parallel to C-29 for skeleton gap phrases. C-30 is a strict refinement of C-13 (C-30 pass implies C-13 pass; C-13 pass does not imply C-30 pass).

---

**Denominator: 21 → 22**
**Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational/22 × 10)`**
**C-30 is in the rationale-authorship chain. Not part of the identity staircase.**

---

Key structural additions in v14:

**Authorship-Residency Pair (C-29, C-30):** Two parallel criteria applying the same design principle to different template fields. C-29 governs skeleton gap phrase provenance; C-30 governs rationale content provenance. Neither is a ceiling of the other — they govern independent fields.

**Rationale-authorship chain:** New third sub-chain in the table-coupling cluster: C-13 (rationale block present) → C-30 (rationale pre-authored in template).

**Table-coupling cluster expands** from 12 to 14 criteria (adding C-13 and C-30), derivable from three structural design choices instead of two.

**Round 14 primary hypothesis:** Confirm C-30 three-way separation — (C-13 PASS + C-30 PASS), (C-13 PASS + C-30 FAIL), (C-13 PARTIAL + C-30 FAIL).
0 is in the rationale-authorship chain. It is not part of the identity staircase.**

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

**v12** added two aspirational criteria (C-26 to C-27) extracted from Round 11 excellence
signals: inertia gap skeleton column entries authored per-namespace at classification time
(C-26; prerequisite for the C-21 + C-10 + C-17 three-criteria structural coupling -- V-05
demonstrated that per-namespace specificity in the table rows at construction time is what
makes the coupling pass, not merely the column's presence), and stop-gate field enumeration
names the classification table's own column headers verbatim (C-27; V-05 pattern: "the
enumerated fields ARE the table columns -- C-16 compliance comes naturally when the stop-
gate condition mirrors the table structure," making C-16 + C-11 + C-14 self-reinforcing
from one structural choice). Denominator +2 (17 --> 19).

**v13** added two aspirational criteria (C-28 to C-29) extracted from Round 12 excellence
signals: stop-gate self-annotation explicitly declares its enumerated field list as the
required verbatim column names (C-28; V-02 R12 excellence -- the gate annotation "The
column names above are the required field names -- use them verbatim" makes the table-gate
coupling self-documenting and machine-readable, elevating C-27 from a naming constraint to
a structural declaration), and inertia gap skeleton seed content is pre-authored in the
skill template body rather than delegated to model-time generation (C-29; V-01 vs V-02 R12
contrast -- V-01 C-26 PASS because skill template provides seed phrases model copies
verbatim; V-02 C-26 PARTIAL because template delegates generation to model, structural
guarantee absent; C-29 is the authorship-residency ceiling above C-26). Denominator +2
(19 --> 21).

**v14** added one aspirational criterion (C-30) extracted from Round 13 excellence signals:
ROLE 2 REAL-REQUIRED rationale content is pre-authored in the skill template body rather
than delegated to model-time generation (C-30; V-03 R13 C-13 PARTIAL -- template supplies
only a delegation instruction "one sentence explaining why real artifacts are required for
this namespace" with no seed content; V-01 and V-02 pass C-13 because their templates pre-
author rationale seed text the model copies or minimally adapts; C-30 applies the same
authorship-residency principle that C-29 applies to skeleton gap phrases, but to the ROLE 2
rationale field; both criteria share the structural guarantee logic: template-authored
content gives deterministic quality, model-generated content gives probabilistic quality).
Denominator +1 (21 --> 22).

---

## Identity Staircase (C-18 through C-25)

Five rungs, each a strict refinement of the one below:

- **C-18**: named role + any violation mechanism
- **C-22**: violation mechanism must be ontological (not behavioral)
- **C-23**: affirmation must appear at each activation (not only preamble)
- **C-24**: affirmation must be syntactically first (not just present)
- **C-25**: affirmation must use being-language (not occupancy-language)

C-26 through C-30 are not part of the identity staircase. They belong to the table-coupling
cluster and rationale-authorship chain, which govern the inertia/classification table
structural design and ROLE 2 content provenance.

---

## Table-Coupling Cluster (C-10, C-11, C-13 to C-17, C-19 to C-21, C-26 to C-30)

Three sub-chains govern the classification table and ROLE 2 template structural integrity:

**Gap-content chain (C-21, C-26, C-29):**
- C-21: skeleton column present and non-empty
- C-26: entries are namespace-specific and authored at classification time
- C-29: entries are pre-authored in the skill template (not model-generated at runtime)

Each rung is a strict refinement: C-29 pass implies C-26 pass implies C-21 pass.
Downstream beneficiaries: C-10 (inertia-derived next steps) and C-17 (vocabulary
co-location) pass automatically when C-26 and C-29 pass.

**Gate-structure chain (C-16, C-27, C-28):**
- C-16: stop-gate present with enumerated field conditions
- C-27: gate names the table's own column headers verbatim
- C-28: gate includes self-annotation declaring its field list as required verbatim column
  names

Each rung is a strict refinement: C-28 pass implies C-27 pass implies C-16 pass.
Downstream beneficiaries: C-11 (table before bodies) and C-14 (upfront commitment) pass
automatically when C-27 and C-28 pass.

**Rationale-authorship chain (C-13, C-30):**
- C-13: ROLE 2 rationale block present with content template for REAL-REQUIRED namespaces
- C-30: rationale content is pre-authored in the skill template (not model-generated at
  runtime)

Each rung is a strict refinement: C-30 pass implies C-13 pass; C-13 pass does not imply
C-30 pass. C-30 is the authorship-residency ceiling for the rationale field, parallel to
C-29 for the skeleton gap field. The two criteria together establish the full provenance
guarantee: both the namespace's missing-signal description (C-29) and the justification for
requiring real artifacts (C-30) must originate in the skill template, not in model execution.

**Authorship-Residency Pair (C-29, C-30):**
C-29 and C-30 are structurally parallel criteria applying the same design principle to
different template fields. In both cases: template-authored content (skill is the author)
gives a structural guarantee of quality; model-generated content (model is the author)
gives a probabilistic guarantee dependent on model execution quality. C-29 governs the
inertia gap skeleton column entries. C-30 governs the ROLE 2 REAL-REQUIRED rationale
content. Neither is a ceiling of the other -- they govern independent fields. Both refine
a parent criterion (C-26 and C-13 respectively) by adding the provenance requirement.

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

**C-08** -- REAL-REQUIRED propagates to downstream role templates for compliance-tagged
namespaces
- Weight: recommended
- Category: behavior
- Pass condition: For every namespace that carries a REAL-REQUIRED flag, the downstream role
  templates (GENERATOR, SUMMARIZER, or equivalent) also carry or reference the REAL-REQUIRED
  constraint. A namespace flagged REAL-REQUIRED at the classification table that has no
  downstream propagation of that constraint fails C-08.

---

### Aspirational (10% weight, denominator 22)

**C-09** -- Tier read from TOPICS.md drives tier-dependent flag rules
- Weight: aspirational
- Category: behavior
- Pass condition: Output reads or references TOPICS.md to determine the topic's tier, and
  the tier value drives flag rule application (e.g., TIER-2-CRITICAL and TIER-3-CRITICAL
  flags are applied when tier >= 2 or >= 3 respectively). A response that applies flags
  without tier-derivation fails C-09.

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

**C-12** -- HANDOFF WRITER role is a dedicated, labelled section
- Weight: aspirational
- Category: format
- Pass condition: The handoff instructions appear in a section explicitly labelled as a
  HANDOFF WRITER role (e.g., "ROLE 4 HANDOFF WRITER" or "You ARE the HANDOFF WRITER"),
  not embedded in general closing remarks. A handoff present but not labelled as a distinct
  role fails C-12.

**C-13** -- REAL-REQUIRED rationale present in ROLE 2 template
- Weight: aspirational
- Category: behavior
- Pass condition: The ROLE 2 (GENERATOR or equivalent) template includes an explicit
  rationale statement for REAL-REQUIRED namespaces -- a clause that explains why real
  artifacts are required rather than mocked (e.g., "evidence validity depends on authentic
  signals"). A REAL-REQUIRED propagation with no rationale fails C-13.

**C-14** -- Upfront commitment: classification table column structure declared before
artifact bodies
- Weight: aspirational
- Category: format
- Pass condition: The output declares the column structure of the classification table
  (names its columns explicitly) before generating any artifact body. A table that appears
  after artifact bodies, or whose column headers are introduced mid-output, fails C-14.

**C-15** -- MUST use and DO NOT use prohibition columns present in classification table
- Weight: aspirational
- Category: format
- Pass condition: The upfront classification table includes both a "MUST use" column
  (vocabulary required in the artifact body) and a "DO NOT use" column (vocabulary
  prohibited in the artifact body). A table missing either column fails C-15.

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
- Pass condition: Each classifier role activation (CLASSIFIER, GENERATOR, SUMMARIZER,
  HANDOFF WRITER, and any additional role) has a dedicated header block that names the role
  and includes at least one explicit mechanism for handling a mis-classification or
  violation case. A role block with no violation mechanism is a fail.

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
  the affirmation second fails C-24, even if C-23 passes. V-02 R11 demonstrated the
  ceiling: "fires as syntactically first element at ROLE 1, ROLE 2, ROLE 3, and ROLE 4
  activations."

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

**C-28** -- Stop-gate self-annotation explicitly declares its enumerated field list as the
required verbatim column names
- Weight: aspirational
- Category: behavior
- Pass condition: The stop-gate instruction (which satisfies C-27) includes an explicit
  self-referential annotation that identifies its enumerated field list as the table's
  required column names and directs verbatim use -- for example: "The column names above
  are the required field names -- use them verbatim." The annotation must be a clause
  within or immediately adjacent to the gate, not a separate documentation note elsewhere.
  A gate that names column headers verbatim (passing C-27) but contains no such annotation
  fails C-28. The annotation elevates the gate from a naming constraint to a structural
  declaration: it makes the table-gate coupling self-documenting and machine-readable, so
  any reader of the gate instruction knows not only what fields are required but that those
  strings are the column names and must be used verbatim. V-02 R12 demonstrated the
  ceiling: gate text named verbatim column headers AND annotated "The column names above
  are the required field names -- use them verbatim."

**C-29** -- Inertia gap skeleton seed content is pre-authored in the skill template body,
not delegated to model-time generation
- Weight: aspirational
- Category: depth
- Pass condition: The inertia gap skeleton entries in the classification table originate
  from seed phrases authored in the skill template body -- phrases the model copies or
  minimally adapts verbatim, rather than generating from scratch in response to an
  instruction to "fill in namespace-specific gap content." A response where skeleton cells
  are model-generated at runtime receives at most PARTIAL for C-29, even if the content is
  namespace-specific (C-26 may pass or partially pass). Full C-29 pass requires evidence
  that the template provides the seed phrases: e.g., the skill instruction reads "copy
  these seed phrases into the skeleton column: [scout: no competitor signal captured yet;
  draft: spec not yet written; ...]" and the output mirrors those phrases. V-01 R12
  demonstrated the ceiling: "Seed phrases provided in template body; model copies verbatim
  -- skill is the author." V-02 R12 demonstrated the failure mode: "Instruction tells model
  to fill namespace-specific phrase; no seed phrases provided; content quality depends on
  model execution -- structural guarantee absent" (C-26 PARTIAL, C-29 FAIL). C-29 is the
  authorship-residency ceiling above C-26: same timing requirement (classification time),
  same specificity requirement (namespace-specific), plus provenance requirement
  (template-authored and model-copied, not model-generated).

**C-30** -- ROLE 2 REAL-REQUIRED rationale content is pre-authored in the skill template
body, not delegated to model-time generation
- Weight: aspirational
- Category: depth
- Pass condition: The ROLE 2 template's REAL-REQUIRED rationale block contains authorial
  seed content -- rationale text the model copies or minimally adapts verbatim -- rather
  than only an instruction directing the model to generate rationale (e.g., "write one
  sentence explaining why real artifacts are required"). A response where the rationale
  clause is model-generated from a delegation instruction receives at most PARTIAL for C-30,
  even if the resulting rationale is substantively correct (C-13 may pass). Full C-30 pass
  requires evidence that the template provides the rationale seed: e.g., the skill
  instruction includes "Evidence validity depends on authentic signals -- synthetic data
  cannot substitute for real experimental results or live user behavior measurements" as
  inline seed text within the rationale placeholder. V-01 R13 demonstrated the ceiling:
  template body provides "prove: requires actual experiment data; listen: requires real user
  feedback; compliance namespace: requires traceable real-world sources" -- skill is the
  author. V-03 R13 demonstrated the failure mode: template provides only "{one sentence
  explaining why real artifacts are required for this namespace}" -- authorship delegated to
  model execution, C-13 PARTIAL. C-30 is the authorship-residency ceiling above C-13:
  same position requirement (ROLE 2), same scope requirement (REAL-REQUIRED namespaces),
  plus the provenance requirement (template-authored and model-copied, not model-generated).
  C-30 is parallel to C-29 in design principle; both govern independent fields.

---

## Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational/22 * 10)
```

Where:
- `essential_pass` = number of essential criteria (C-01 to C-05) that pass (0--5)
- `recommended_pass` = number of recommended criteria (C-06 to C-08) that pass (0--3)
- `aspirational` = sum of aspirational criterion scores (C-09 to C-30), 0.0--22.0

PARTIAL = 0.5. Golden threshold: all 5 essential pass AND composite >= 80.

**Denominator:** 22 aspirational criteria as of v14.

---

## Round 14 Guidance

**C-30 independence hypothesis:** C-30 requires rationale content to be pre-authored in the
template; C-13 requires only that a rationale block be present. Three-way separation to
confirm:
- C-13 PASS + C-30 PASS: template pre-authors rationale seed text; model copies or minimally
  adapts
- C-13 PASS + C-30 FAIL: model generates rationale from a delegation instruction; content
  is substantively correct but structurally unguaranteed
- C-13 PARTIAL + C-30 FAIL: template has only a delegation instruction with no content;
  model output is model-dependent in both quality and presence

Confirming this three-way separation is the primary R14 hypothesis for the rationale-
authorship chain.

**Authorship-Residency Pair ceiling (updated):** With C-30 added, the pair governs two
independent template fields: skeleton gap phrases (C-29) and REAL-REQUIRED rationale (C-30).
A variation that pre-authors both fields simultaneously should pass both criteria. Confirming
this dual-field ceiling -- a single structural choice (template authors all seed content)
that satisfies both C-29 and C-30 in one pass -- is a secondary R14 objective.

**Table-coupling cluster ceiling (updated):** The cluster now spans C-10, C-11, C-13 to
C-17, C-19 to C-21, C-26 to C-30 -- 14 aspirational criteria derivable from three
structural design choices: (1) skill-authored seed phrases in the skeleton column (C-29 ->
C-26 -> C-21 -> C-10 + C-17 cascade), (2) gate naming those column headers verbatim with
self-annotation (C-28 -> C-27 -> C-16 -> C-11 + C-14 cascade), and (3) skill-authored
rationale seed content in ROLE 2 (C-30 -> C-13 chain). Confirming this 14-criterion ceiling
is a secondary R14 objective.

**Identity staircase (C-18 to C-25):** Confirmed stable through R13. R14 need not target
the staircase unless a new linguistic distinction above C-25 is identified.
