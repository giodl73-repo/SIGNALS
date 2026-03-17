Written to `simulations/quest/rubrics/crew-review-rubric-v8-2026-03-16.md`.

---

**What changed v7 -> v8:**

Two new aspirational criteria extracted from R8 V-01 and V-02:

| ID | Pattern | Source | Extends |
|----|---------|--------|---------|
| C-26 | Criterion-check table is self-referentially complete | V-01 R8 | C-24 |
| C-27 | Per-slot synthesis coverage contract | V-02 R8 | C-07, C-22 |

**C-26** -- V-05 R7's criterion-check table covered C-11 through C-23 but didn't include rows for C-24 and C-25 themselves. V-01 R8 closes that gap: the table now carries explicit rows verifying its own existence (C-24) and the schema's anti-pattern exhaustiveness (C-25). A table that ends at C-23 passes C-24 but fails C-26.

**C-27** -- C-07 requires at least one convergence/conflict signal (minimum-count). V-02 R8 replaces that with a per-slot coverage contract: every slot gets an explicit convergence/conflict/unique verdict addressed by slot number. The same escalation from minimum-count to exhaustive that C-25 applied to schema anti-patterns, now applied to synthesis.

**Scoring:** 16 aspirational x 2.5 = 40, max **160** (was 155). Golden threshold unchanged at 80.

**R8 scores under v8:** V-01 = 157.5 | V-02 = 157.5

**New chain tails:**
- Validation: C-13 -> C-23 -> C-24 -> **C-26**
- Synthesis coverage: C-07 -> C-22 -> **C-27**
her than a minimum-count alert. V-01
R8 meets C-07 via the R3 minimum-count contract; V-02 R8 replaces minimum-count with
per-slot exhaustive verdicts.

**Scoring:** 16 aspirational x 2.5 = 40, max 160 (was 155). Golden threshold unchanged at 80.

**R8 scores under v8:**
- V-01: 60 + 60 + 37.5 = **157.5** (C-26 PASS; C-27 FAIL -- minimum-count synthesis, not per-slot)
- V-02: 60 + 60 + 37.5 = **157.5** (C-27 PASS; C-26 FAIL -- criterion-check table present but not self-inclusive)

**New relationship chains:**
- Criterion-check completeness: C-23 (validation as named phase) -> C-24 (phase contains
  criterion-check table) -> C-26 (table includes its own governing criteria --
  self-referential completeness).
- Synthesis coverage: C-07 (at least one cross-role signal) -> C-22 (slot-anchored matrix
  with numbered cross-references) -> C-27 (every slot receives a synthesis verdict --
  exhaustive slot-anchored coverage contract).

---

## Essential Criteria

All five must pass for golden to be possible. A FAIL on any essential criterion is
disqualifying regardless of composite score.

---

### C-01 -- Role Selection Grounded in .craft/roles/

| Field | Value |
|-------|-------|
| ID | C-01 |
| Weight | essential |
| Category | correctness |

**Text**: All reviewer roles are drawn exclusively from the `.craft/roles/` registry. The
registry is read at execution time. No roles are fabricated, invented from memory, or
substituted from prior run defaults. Every role name in the output corresponds to an entry
that exists in the registry at review time.

**Pass condition**: Every role named in the output has a corresponding file in
`.craft/roles/`. No fabricated roles. Reviewer selection reflects the requested depth:
standard selects artifact-relevant roles (2-4 for typical artifacts); deep selects all
roles in the registry. If the registry cannot be read, review does not proceed (see C-14).

---

### C-02 -- Review Matrix Structure Present

| Field | Value |
|-------|-------|
| ID | C-02 |
| Weight | essential |
| Category | format |

**Text**: Output contains a review matrix with all four required columns: **role, findings,
severity, recommendation**. No column is absent. Each selected reviewer occupies at least
one matrix row.

**Pass condition**: Matrix structure is present. Four columns visible (role, findings,
severity, recommendation). Row count >= number of selected reviewers. No reviewer in the
selected set is absent from the matrix. A superset schema (e.g., 5-column with an
additional Slot column, or 6-column with Slot and Lens) passes if the four required columns
are present.

---

### C-03 -- Severity Uses Defined Semantics

| Field | Value |
|-------|-------|
| ID | C-03 |
| Weight | essential |
| Category | correctness |

**Text**: All severity values in the matrix are HIGH, MEDIUM, or LOW -- matching the
standard semantics: HIGH blocks commitment, MEDIUM conditions commitment, LOW is advisory.
No freestyle severity labels (e.g., "Critical", "Minor", "Warning").

**Pass condition**: Every severity cell contains exactly HIGH, MEDIUM, or LOW. At least one
severity assignment is justified by finding content (a HIGH finding describes something that
would block commitment; a LOW finding describes something advisory). No severity cell is
blank or uses a non-standard label.

---

### C-04 -- Each Role Reviews from Its Own Perspective

| Field | Value |
|-------|-------|
| ID | C-04 |
| Weight | essential |
| Category | depth |

**Text**: Each reviewer's findings are traceable to that role's documented `lens.verify`
and `expertise.depth`. Findings are not copy-pasted across roles. A PM finding should not
appear identically in an architect row.

**Pass condition**: For each reviewer row, at least one finding is identifiably from that
role's lens -- i.e., it references a concern that only that role's frame would surface (PM:
commitment threshold, signal sufficiency; architect: system boundary, contract correctness;
inertia-advocate: null hypothesis, switching cost). Findings across rows are distinguishable
by perspective.

---

### C-05 -- Recommendations are Concrete and Role-Specific

| Field | Value |
|-------|-------|
| ID | C-05 |
| Weight | essential |
| Category | depth |

**Text**: Each recommendation in the matrix is actionable and names what to change -- not
generic ("needs improvement"). It references the finding's specific surface, field, or gap.

**Pass condition**: No recommendation row contains only a generic directive. Each
recommendation names a specific artifact surface, section, or action (e.g., "Add switching
cost estimate to Section 3 before committing", not "Review the proposal"). At least 80% of
recommendation cells meet this standard.

---

## Recommended Criteria

Output is better with all six. Missing recommended criteria lower the composite score but
do not disqualify golden on their own.

---

### C-06 -- Depth Flag Respected

| Field | Value |
|-------|-------|
| ID | C-06 |
| Weight | recommended |
| Category | behavior |

**Text**: Standard depth selects only artifact-relevant roles (2-4 roles for typical
artifacts). Deep depth includes all roles from `.craft/roles/`. Output reflects the correct
scope for the invoked depth -- neither over-selects (standard) nor under-selects (deep).

**Pass condition**: Standard: reviewer count is 2-4 unless the artifact type warrants more.
Deep: reviewer count equals the full `.craft/roles/` registry size. If depth is unstated,
standard is assumed and the standard pass condition applies.

---

### C-07 -- Cross-Role Signal Surfaced

| Field | Value |
|-------|-------|
| ID | C-07 |
| Weight | recommended |
| Category | coverage |

**Text**: At least one conflict or convergence across reviewers is identified. When two or
more roles independently raise the same concern, it is labeled convergence and treated as
the highest-confidence signal in the review.

**Pass condition**: Output includes a cross-role signals section (or equivalent inline
callout) with at least one convergence note OR one conflict note. Convergence names which
roles agree and on what. Conflict names which roles disagree and what the tension is.
"None detected" is acceptable only if the matrix findings are genuinely non-overlapping.

---

### C-08 -- AMEND Options Listed

| Field | Value |
|-------|-------|
| ID | C-08 |
| Weight | recommended |
| Category | format |

**Text**: Output ends with an AMEND section listing at least 2 named amendment options:
add a specific reviewer, change the scope, change the depth. This follows the
signal-lifecycle amend phase.

**Pass condition**: AMEND section present. At least 2 options named (add reviewer / change
scope / change depth). Options are specific -- "add signal:strategy reviewer" not "add more
reviewers". Missing AMEND section = FAIL.

---

### C-09 -- Inertia-Advocate Leads as Challenger

| Field | Value |
|-------|-------|
| ID | C-09 |
| Weight | recommended |
| Category | depth |

**Text**: Even in standard depth, the inertia-advocate appears as the first reviewer and
opens with a null hypothesis statement: what the team does today instead of building this.
The challenger bracket pattern is honored -- the first review challenges the artifact from
the "do nothing" frame before any constructive domain review.

**Pass condition**: inertia-advocate (or equivalent challenger role from `.craft/roles/`)
appears first in the matrix. That row includes a null hypothesis statement or explicit
"do nothing" framing. The null hypothesis specifies what the team currently does as the
alternative to the artifact.

**Promoted from aspirational in v2**: Stable across R1 variations. Three of four scored
variations passed; the single failure (V-02) was a missing-feature gap, not criterion
ambiguity.

---

### C-10 -- Finding Specificity: Named Surface

| Field | Value |
|-------|-------|
| ID | C-10 |
| Weight | recommended |
| Category | depth |

**Text**: Each finding names a specific surface, section, or component of the artifact
being reviewed -- not abstract observations. "The Section 3 scope enumeration is missing
a surface for edge-case handling" is specific. "This needs more detail" is not.

**Pass condition**: >= 80% of all finding cells in the matrix name a specific artifact
section, field, named concept, or component. Generic observations without a named surface
count as failing the 80% bar. An output where every finding is surface-specific passes.

**Promoted from aspirational in v2**: Stable across R1 variations. All four scored
variations passed with strong evidence; no criterion ambiguity found.

---

### C-14 -- Registry ERROR Halt on Missing or Malformed Data

| Field | Value |
|-------|-------|
| ID | C-14 |
| Weight | recommended |
| Category | correctness |

**Text**: The prompt includes an explicit hard stop -- an ERROR halt, not a soft warning --
if `.craft/roles/` is absent, unreadable, or any role file is missing required fields
(e.g., `lens.verify`, `archetype`). The halt is unconditional: the review does not proceed
with partial data or invented substitutes. This is a defensive mechanism beyond C-01's
name-matching requirement.

**Pass condition**: Output or prompt structure contains an ERROR branch that fires if the
registry read returns an empty set, missing files, or files without required fields. The
ERROR message is explicit (e.g., "ERROR: .craft/roles/ not found -- cannot proceed") and
the review output is suppressed until the condition is resolved. A soft fallback ("if no
roles found, proceed with defaults") does not pass.

**Promoted from aspirational in v4**: 5/5 PASS across all R3 variations. First aspirational
criterion to achieve full-round stability after introduction. V-04 R3 added "unconditional,
no soft fallback" as an explicit label, confirming the intent is well-understood across
implementations.

---

## Aspirational Criteria

Raise the bar once essential and recommended are stable. C-11 through C-13 and C-15
through C-16 are from R1-R2. C-17 through C-19 are from R3. C-20 through C-21 are from
R4. C-22 through C-23 are from R6. C-24 through C-25 are from R7. C-26 through C-27 are
new from R8.

---

### C-11 -- Null Hypothesis Uses Structured Template

| Field | Value |
|-------|-------|
| ID | C-11 |
| Weight | aspirational |
| Category | depth |

**Text**: The inertia-advocate's null hypothesis is not free-form prose -- it is a
structured fill-in template with 3 or more named blanks that the model must complete:
e.g., "We currently do [X] instead of building this. The switching cost is [Y]. The risk
of not acting is [Z]." A template forces articulation where C-09 only requires statement.

**Pass condition**: Inertia-advocate row (or challenger block) contains a template with
3+ named fill-in slots, all completed. Generic statements ("the team does the existing
workflow") without a slot structure do not pass. The template scaffolding must be visible
in the output -- completed slots, not a free-form paragraph.

**Origin**: V-01 R1 "3-blank null hypothesis template" (structural, not instructional);
V-04 R1 "null hypothesis template explicitly required."

---

### C-12 -- Per-Role Lens-Lock Declaration

| Field | Value |
|-------|-------|
| ID | C-12 |
| Weight | aspirational |
| Category | depth |

**Text**: Before writing any finding for a role, the output contains an explicit
one-sentence perspective declaration: "What does someone in this role actually care about?"
The lens statement precedes that role's findings and is visible as a declared constraint.
This is a structural protection beyond C-04's output check -- it forces perspective
articulation before finding generation.

**Pass condition**: Each reviewer row is preceded by or opens with a one-sentence lens
declaration traceable to that role's perspective (e.g., "As an architect, I care about
system boundary correctness and contract stability."). Declaration must be present for at
least all non-challenger reviewers. Lens statements that merely restate the role name
("As a PM, I am reviewing this as a PM.") do not pass.

**Origin**: V-03 R1 "per-role lens-lock step forces perspective before finding"; V-04 R1
"Apply only that role's lens.verify perspective" as an explicit named step in the prompt
structure, not a background instruction. R7 breakthrough: C-12 is reliably achieved when
Lens is a required output schema column rather than an execution instruction (V-02, V-03,
V-05 all PASS with Lens column; V-01, V-04 FAIL without it).

---

### C-13 -- Typed Column Contracts with Per-Row Validation

| Field | Value |
|-------|-------|
| ID | C-13 |
| Weight | aspirational |
| Category | format |

**Text**: The matrix is constructed as a typed schema -- each column carries an explicit
type contract (e.g., severity: "enum -- Exactly one of: HIGH, MEDIUM, LOW. No other
values permitted.") and rows are validated against these contracts before output is
written. The validation step is visible (a pre-output validation pass, inline column-type
annotation, or per-row constraint check). This extends C-02 (matrix presence) and C-03
(semantic severity) to matrix-correct-by-construction.

**Pass condition**: Output shows evidence of column-level type enforcement: explicit column
contract annotations, a visible validation phase, or per-row checks. A severity column that
uses the right values but shows no enforcement mechanism does not pass. The constraint must
be visible, not inferred.

**Origin**: V-02 R1 "column type: enum -- Exactly one of: HIGH, MEDIUM, LOW. No other
values -- strongest enforcement"; V-05 R1 "per-row validation table enforced before row is
written."

---

### C-15 -- Challenger Bracket as a Named Execution Phase

| Field | Value |
|-------|-------|
| ID | C-15 |
| Weight | aspirational |
| Category | depth |

**Text**: The challenger pass is declared as an explicit, named execution phase -- not an
exception clause or a priority hint. The prompt separates execution into (1) challenger
bracket: run all roles with `archetype: challenger` first, then (2) domain review: run
remaining roles. This phase boundary guarantees challenger priority structurally, not by
instruction proximity. C-09 requires that the inertia-advocate leads; C-15 requires that
the mechanism making it lead is a named phase, not an "always include" exception.

**Pass condition**: Prompt or output structure names a challenger phase as a discrete step
before domain review begins. The challenger phase is identified by a named bracket
condition (e.g., "Before any domain review, run all roles with `archetype: challenger`"),
not by a parenthetical or footnote. The domain review phase is also named as a separate
step that begins after the challenger bracket closes. An "always included" exception clause
in a single flat role-selection step does not pass.

**Origin**: V-02 R2 "challenger bracket as named execution phase" -- "Before any domain
review, run all roles with `archetype: challenger`" + "Challenger row appears first" as an
explicit structural rule. Contrast: V-01 R2 used "always included in standard depth"
exception clause, which produced a C-09 PARTIAL score (phase ordering not guaranteed).

---

### C-16 -- Slot-Level Failure Escalation in Null Hypothesis Template

| Field | Value |
|-------|-------|
| ID | C-16 |
| Weight | aspirational |
| Category | depth |

**Text**: An unfilled slot in the null hypothesis template is not treated as a warning,
a soft gap, or a prose approximation -- it is escalated to a named HIGH finding logged in
the matrix. The escalation rule makes the template self-enforcing: the model cannot satisfy
C-11 by silence or by collapsing multiple slots into one sentence. Each slot must be filled
or the gap becomes a visible, scored finding. This extends C-11 (structured template) to
structured template with mandatory slot completion.

**Pass condition**: The null hypothesis template includes an explicit escalation rule for
empty slots: an unfilled slot produces a logged finding of the form "[not stated in
artifact]" with severity HIGH. The rule must cover each slot individually -- a single
"template must be complete" instruction does not pass if there is no per-slot escalation
path. The escalation must produce a HIGH finding, not a note or a warning.

**Origin**: V-02 R2 "4-slot null hypothesis form with slot-level escalation" -- "All four
blanks must be filled. Empty slot -> `[not stated in artifact -- HIGH finding]` + logged
as HIGH. Do not collapse multiple blanks into one sentence." V-01 R2 had no slot-level
escalation rule and scored C-11 FAIL (0/2.5) despite having a template structure.

---

### C-17 -- Challenger Phase Gate: Formal Exit Condition

| Field | Value |
|-------|-------|
| ID | C-17 |
| Weight | aspirational |
| Category | depth |

**Text**: The challenger bracket does not merely have a name -- it has an explicit exit
condition that structurally blocks domain review from beginning until the condition is
satisfied. C-15 requires the challenger phase to be a named discrete step; C-17 requires
that phase to carry an enforced gate: domain review is blocked until the challenger phase
exits. "Then run domain reviewers" is a sequence description. "Domain review does not
begin until PHASE 2 exits" is a gate.

**Pass condition**: The challenger phase definition includes a stated exit condition -- an
explicit rule that domain review cannot begin until the challenger bracket is complete.
The exit condition must be written as a structural constraint ("Domain review does not
begin until X exits" or "X must close before Y opens"), not as a narrative sequence
instruction. Entry conditions are optional; the exit gate is required for pass. An
"execute challengers first" instruction without a stated blocking condition does not pass.

**Origin**: V-04 R3 "PHASE 2 CHALLENGER BRACKET with entry/exit conditions. 'Domain review
does not begin until PHASE 2 exits.' Strongest phase-gate statement across all R3
variations." Contrast: V-01, V-03, V-05 R3 named challenger phases without formal exit
conditions; all scored C-15 PASS but would score C-17 FAIL under this criterion.

---

### C-18 -- Empty-Slot Escalation as Separate Matrix Row

| Field | Value |
|-------|-------|
| ID | C-18 |
| Weight | aspirational |
| Category | depth |

**Text**: An unfilled null hypothesis slot escalates to a separately-logged,
independently-scored HIGH finding row in the review matrix -- the same matrix that holds
all domain findings. C-16 requires that empty slots produce a logged HIGH finding; C-18
requires that finding to be a distinct matrix row, not an inline annotation, appended note,
or narrative comment. The unfilled slot becomes a visible, independently scorable review
artifact in the matrix itself.

**Pass condition**: For each unfilled null hypothesis slot, the output contains a dedicated
HIGH-severity row in the review matrix. The row follows the same schema as domain findings
(role/lens, finding, severity, recommendation). The finding cell identifies which slot was
empty and names the specific gap. A finding appended as a note below the challenger row,
or embedded as a sentence within a finding cell, does not pass. Each unfilled slot must
produce its own separate row.

**Origin**: V-05 R3 "Per-slot escalation (applies to each slot individually)... log a
**separate** HIGH finding row. Separate row is the strongest escalation form: the unfilled
slot becomes an independently scored matrix entry." Contrast: V-01, V-03, V-04 R3 logged
HIGH findings for empty slots (C-16 PASS) but produced inline annotations rather than
separate matrix rows.

---

### C-19 -- Anti-Pattern Exclusion in Typed Column Constraints

| Field | Value |
|-------|-------|
| ID | C-19 |
| Weight | aspirational |
| Category | format |

**Text**: Typed schema column definitions include not only what IS valid (positive
constraint) but also an explicit named anti-pattern that is excluded. The exclusion is
written inside the constraint definition itself, making it part of the schema contract --
not a separate general instruction. C-13 requires typed column contracts with visible
enforcement; C-19 requires those contracts to name the specific failure mode they prohibit.
The anti-pattern exclusion tells the model exactly what a bad value looks like before it
writes one.

**Pass condition**: At least one column constraint in the typed schema includes a named
anti-pattern exclusion stated within the column definition (e.g., "Lens: free-text, one
sentence -- no generic restatements"; "Findings: named surface required -- not abstract
observations"). The exclusion must be part of the column definition, not a separately
listed general instruction. A constraint that states only what IS valid without naming
what is not does not pass this criterion (though it may pass C-13). At least one column
must carry an explicit exclusion clause.

**Origin**: V-02 R3 Lens column definition: "free-text, one sentence -- no generic
restatements" as a typed constraint with an anti-pattern exclusion built in. The exclusion
("no generic restatements") is inside the column's type constraint, not a separate
instruction, making the schema self-documenting about its own failure modes.

---

### C-20 -- Multi-Condition Gate Closure with Named States

| Field | Value |
|-------|-------|
| ID | C-20 |
| Weight | aspirational |
| Category | depth |

**Text**: The challenger phase gate is not a boolean barrier -- it is a typed state machine
with explicitly named states (e.g., OPEN/CLOSED) and a multi-condition closure predicate:
the gate transitions from OPEN to CLOSED only when all enumerated conditions are satisfied.
C-17 requires a formal exit condition that blocks domain review; C-20 requires that exit
condition to be an explicit state machine with named states and a conjunction of closure
conditions. A gate that says "domain review does not begin until challengers complete" is
C-17. A gate that names its states and requires multiple enumerated conditions all satisfied
before transitioning to CLOSED is C-20.

**Pass condition**: The challenger phase gate definition includes: (1) at least two
explicitly named gate states (e.g., OPEN and CLOSED), and (2) a multi-condition closure
predicate listing 2 or more enumerated conditions that must all hold before the gate
closes. The closure conditions must be individually listed -- a single "challengers
complete" condition does not pass. The state names must appear in the gate definition,
not only implied by context. An exit condition without named states, or named states with
a single closure condition, does not pass.

**Origin**: V-01 R4 "G1 with named OPEN/CLOSED state; 5-condition closure; 'Domain review
does not begin until G1 closes.'" The gate is a typed artifact: it has a label (G1), two
named states, and five enumerated closure conditions. This is structurally stronger than
C-17's single blocking statement -- the model must enumerate what "closed" means, not just
assert that a block exists. Contrast: C-17 requires the gate; C-20 requires the gate to
have a type.

---

### C-21 -- Anti-Pattern Exclusion in Escalation Rules

| Field | Value |
|-------|-------|
| ID | C-21 |
| Weight | aspirational |
| Category | depth |

**Text**: The escalation rule for unfilled null hypothesis slots names the prohibited
output form inside the escalation rule definition itself -- not in a separate general
instruction. C-18 requires that each unfilled slot produce a separate dedicated matrix row;
C-21 requires the escalation rule to explicitly state what does NOT constitute a row (e.g.,
"Do not embed the finding as a sentence within another finding cell"). This applies C-19's
anti-pattern exclusion principle from column constraints to escalation rules. The escalation
rule documents both the required form (a dedicated row) and the prohibited form (an inline
sentence), making the rule self-documenting about its own failure mode.

**Pass condition**: The escalation rule for empty slots contains an explicit statement
naming the prohibited output form within the rule itself. The prohibition must be specific
("Do not embed as a sentence within a finding cell", "Do not append as a note to the
challenger row") rather than a general admonition ("do not skip"). The prohibited form
must be stated inside the escalation rule, not in a separate instruction block. Cardinality
evidence ("two unfilled slots = two rows") may accompany but does not substitute for the
explicit exclusion clause. An escalation rule that names only the required form (dedicated
row) without naming the prohibited form does not pass.

**Origin**: V-02 R4 escalation rule: "Produce a **separate, dedicated matrix row**"; "Do
not embed... as a sentence"; "Two unfilled slots = two rows -- fully specified." The
prohibition ("Do not embed as a sentence") is stated inside the escalation rule definition,
making the rule self-documenting about its own failure mode. This is the escalation analog
of C-19's column-constraint exclusion pattern -- the same structural technique applied one
level deeper in the output contract.

---

### C-22 -- Slot-Anchored Matrix with Numbered Cross-References

| Field | Value |
|-------|-------|
| ID | C-22 |
| Weight | aspirational |
| Category | format |

**Text**: The review matrix includes a Slot column that assigns a stable numbered position
to every reviewer row. Downstream elements -- synthesis, AMEND options, escalation notes
-- reference findings by slot number (e.g., "Slot 1", "Slot 3") rather than by role name
alone. The Slot column makes every reviewer position a named, machine-checkable anchor:
slot numbers are stable across runs with the same depth configuration, role names are not.
C-02 allows superset schemas to pass; C-22 requires the superset to include the Slot
column AND requires downstream cross-references to use slot numbers for traceability.

**Pass condition**: The review matrix contains a Slot column (or equivalent numbered
position field) that assigns a distinct number to each reviewer row. At least one
downstream element outside the matrix body (synthesis section, AMEND options, or
escalation note) references a finding or role by slot number. A Slot column that is
present but never referenced downstream does not pass -- the criterion requires the column
to be used as an anchor, not merely declared. Role-name-only references ("the architect
finds...") without slot numbers do not pass this criterion (though they pass C-07).

**Origin**: V-03 R6 C-02 evidence: "Step 5 OUTPUT: 5-column table (Slot, Role, Findings,
Severity, Recommendation) -- superset passes." V-03 R6 C-07 evidence: "cross-role synthesis
required, references slot numbers." The Slot column turns reviewer positions into numbered
anchors; synthesis and AMEND inherit slot-number traceability. This is the matrix-structure
extension of C-02 (4-column minimum -> numbered-slot matrix) and elevates C-07's
cross-role signals from role-named to slot-numbered.

---

### C-23 -- Validation as a Named Discrete Execution Phase

| Field | Value |
|-------|-------|
| ID | C-23 |
| Weight | aspirational |
| Category | format |

**Text**: The validation step is declared as a named, numbered execution phase in the
skill's execution model -- architecturally equivalent in status to the CHALLENGE phase and
the REVIEW phase. C-13 requires visible validation (any of: column contracts, visible
phase, per-row checks); C-23 requires that validation be a first-class named phase, not
merely a visible gate or inline constraint embedded within the output step. The structural
principle is identical to how C-15 extended C-09: C-09 requires that the inertia-advocate
leads (output check); C-15 requires the mechanism to be a named phase (structural
mechanism). C-13 requires visible validation (output check); C-23 requires validation to
be a named phase (structural mechanism). A skill that validates rows as part of its output
step passes C-13; a skill that names validation as a discrete phase (e.g., PHASE 4
VALIDATE) passes C-23.

**Pass condition**: The skill's execution model names a validation step as a discrete,
labeled phase -- not a sub-step within the output phase, not an inline constraint check,
not an annotation on column definitions. The phase must have a name that identifies it as
validation (e.g., "PHASE 4 VALIDATE", "Step 3: Validate Matrix") and must be listed at the
same structural level as other named phases (LOAD, CHALLENGE, REVIEW). The validation
phase must precede the output or synthesis phase, producing a validated intermediate that
feeds the next phase. A per-row check embedded in "Step 5: Write output" does not pass;
a named "Step 4: Validate" phase that precedes "Step 5: Write output" does pass.

**Origin**: V-02 R6 C-13 evidence: "PHASE 4 VALIDATE is a visible validation phase with
per-cell checks before matrix is written." V-02's execution model names five phases: PHASE
1 LOAD, PHASE 2 CHALLENGE, PHASE 3 REVIEW, PHASE 4 VALIDATE, PHASE 5 AMEND. Validation
is at the same structural level as challenge and review -- not a gate within output. This
mirrors exactly the C-09 -> C-15 elevation: C-09 requires challenger to lead; C-15
requires the mechanism to be a named phase. C-13 requires visible validation; C-23 requires
validation to be a named phase. Contrast: V-03 R6 had column constraints in Step 5 but no
named validation phase (C-13 PARTIAL, C-23 FAIL). V-01 R6 had implicit contract enforcement
only (C-13 PARTIAL, C-23 FAIL).

---

### C-24 -- Criterion-Check Table Embedded in VALIDATE Phase

| Field | Value |
|-------|-------|
| ID | C-24 |
| Weight | aspirational |
| Category | format |

**Text**: The VALIDATE phase contains a structured self-verification table that lists each
aspirational criterion the skill is designed to satisfy, with YES/NO/PARTIAL status and
evidence citations from the draft matrix. This turns the validation phase into a
self-documenting aspirational-criteria audit: the model must check its own output against
each designed-to-satisfy criterion before writing the final matrix. C-23 requires
validation to be a named discrete execution phase; C-24 requires that phase to carry an
embedded criterion-check table auditing all designed-to-satisfy aspirational criteria.
The check table produces a visible audit trail that makes criterion-slip detectable at
execution time rather than at score time.

**Pass condition**: The VALIDATE phase contains a structured table (or equivalent list)
that: (1) enumerates each aspirational criterion the skill is designed to satisfy by ID,
(2) assigns a YES/NO/PARTIAL status to each, and (3) provides evidence citations from the
draft matrix rather than bare status flags. The table must cover all aspirational criteria
the skill targets -- a subset check table (e.g., only severity validation) does not pass.
Evidence must be citation-style ("G1 state machine present with 4 conditions" not just
"YES"). A VALIDATE phase that checks only column constraints against schema types passes
C-13 but not C-24. A VALIDATE phase with a criterion-check table but no evidence citations
(bare YES/NO without supporting evidence) does not pass.

**Origin**: V-05 R7 PHASE 4 VALIDATE: "a self-verification table that explicitly checks
C-11 through C-23 with YES/NO/PARTIAL status and evidence citations before the final matrix
is written." V-05's criterion-check table covers all aspirational criteria the skill targets
and exports the audit trace in the output, making criterion-slip visible to scorers. C-24
extends C-23: the named VALIDATE phase becomes a meta-criterion checkpoint, not merely a
column-contract gate. No variation before V-05 R7 satisfied this criterion.

---

### C-25 -- Exhaustive Anti-Pattern Coverage Across All Schema Columns

| Field | Value |
|-------|-------|
| ID | C-25 |
| Weight | aspirational |
| Category | format |

**Text**: Every column in the review matrix schema carries an explicit anti-pattern
exclusion clause inside its column definition -- including structural columns like Slot and
behavioral columns like Severity. C-19 requires at least one column definition to name its
anti-form; C-25 requires every column to carry an anti-pattern exclusion. The schema
becomes a complete failure-mode specification: every cell type documents what a bad value
looks like before the model writes one. The Slot column's anti-pattern ("NOT: non-integer
labels; NOT: Slot values that conflict with the manifest") is structurally identical to the
Lens column's ("NOT: generic role restatements") -- the technique is applied uniformly
across the full schema rather than selectively.

**Pass condition**: Every column in the declared matrix schema carries an anti-pattern
exclusion stated within that column's definition. For a 4-column schema, all four columns
must carry exclusions. For a 5- or 6-column schema, all five or six columns must carry
exclusions -- no column is exempt. Structural columns (Slot, Severity) must carry
exclusions that name the specific prohibited form (e.g., Slot: "NOT: non-integer labels",
Severity: "NOT: freestyle labels; NOT: combinations"). A schema where 5 of 6 columns carry
anti-patterns does not pass (though it may pass C-19). The exclusion must be inside the
column definition, not a separate general instruction.

**Origin**: V-05 R7 C-19 evidence: "All six column definitions carry anti-pattern
exclusions. Includes Slot column ('NOT: absent Slot cells; NOT: non-integer labels; NOT:
Slot values that conflict with the manifest') -- the most comprehensive anti-pattern
coverage across all variations." Prior variations (V-01 through V-04 R7) had anti-patterns
in 2-4 of their 5-column schemas; V-05 extended the pattern to all six columns including
Slot. This is the C-19 escalation: C-19 requires at least one exclusion to anchor the
pattern; C-25 requires exhaustive coverage to make the schema fully self-documenting.

---

### C-26 -- Criterion-Check Table Is Self-Referentially Complete

| Field | Value |
|-------|-------|
| ID | C-26 |
| Weight | aspirational |
| Category | format |

**Text**: The criterion-check table inside the VALIDATE phase explicitly includes rows for
C-24 and C-25 themselves -- the two criteria that govern the table's own existence and the
schema's anti-pattern exhaustiveness. The table audits its own completeness: it verifies
that the criterion-check mechanism is present (C-24 row) and that every column carries an
anti-pattern exclusion (C-25 row). C-24 requires the VALIDATE phase to carry a
criterion-check table covering all designed-to-satisfy aspirational criteria; C-26 requires
that coverage to include the meta-criteria that make the table complete, closing the
self-referential gap. A table that checks C-11 through C-23 but omits rows for C-24 and
C-25 passes C-24 but fails C-26.

**Pass condition**: The criterion-check table inside the VALIDATE phase contains an
explicit row for C-24 (criterion-check table embedded in VALIDATE) with status and evidence
confirming the table's presence, AND an explicit row for C-25 (exhaustive anti-pattern
coverage) with status and evidence confirming all-column anti-pattern coverage. Both rows
must appear in the table body as first-class criterion entries -- not as footnotes or
appended comments. A table that ends at C-23 without C-24 and C-25 rows does not pass.
A table that mentions C-24/C-25 only in a summary section without structured row entries
does not pass.

**Origin**: V-01 R8 axis: "Criterion-check self-inclusion -- adds C-24 and C-25 as explicit
rows in the PHASE 4 table, closing the meta-completeness gap in V-05 R7." V-05 R7 was the
first perfect score under v7; its criterion-check table covered C-11 through C-23 but did
not include rows that would verify C-24 and C-25 themselves. V-01 R8 extends the table by
adding those rows, making the table self-auditing: it now confirms not only that the matrix
columns are correct but also that the table checking those columns is structurally complete.
C-26 extends C-24: C-24 requires the table to exist and cover all targets; C-26 requires
coverage to include the criteria governing the table and the schema.

---

### C-27 -- Per-Slot Synthesis Coverage Contract

| Field | Value |
|-------|-------|
| ID | C-27 |
| Weight | aspirational |
| Category | coverage |

**Text**: The synthesis section provides an explicit verdict (convergence, conflict, or
unique) for every reviewer slot in the matrix -- not just for the slots where signals
happen to overlap. C-07 requires at least one cross-role signal to be surfaced; C-22
requires the Slot column to be used as a numbered anchor in downstream cross-references;
C-27 requires the synthesis to be exhaustively slot-anchored: every slot receives its own
synthesis verdict, making the synthesis a complete slot-coverage contract rather than a
minimum-count alert. A synthesis that covers 4 of 6 slots and reports two convergence
signals satisfies C-07 but not C-27.

**Pass condition**: The synthesis section (or cross-role signals section) contains an
explicit verdict for every reviewer slot in the matrix, addressed by slot number. The
verdict for each slot must be one of: convergence (named roles agree on a concern),
conflict (named roles disagree on a concern), or unique (this role raised a concern no
other role surfaced). Every slot must appear in the synthesis -- gaps are not acceptable
even if the slot's findings are unremarkable. The verdict must be slot-addressed by number
(e.g., "Slot 3: unique -- only the architect surfaced the contract boundary concern"),
not role-name-only. A synthesis that identifies convergence across three roles without
individually addressing every slot does not pass.

**Origin**: V-02 R8 axis: "Per-slot synthesis coverage contract -- replaces minimum-count
synthesis with exhaustive slot-anchored verdicts." V-02 R8 C-07 evidence: "Per-slot
synthesis guarantees convergence/conflict/unique verdict for every slot -- strictly stronger
than C-07's minimum-count requirement." C-27 is the synthesis analog of how C-25 extends
C-19: C-07 requires at least one signal (minimum-count); C-27 requires every slot to carry
a verdict (exhaustive coverage). The chain: C-07 (minimum-count signal) -> C-22 (slot
column enables slot-numbered anchoring) -> C-27 (every slot receives a synthesis verdict).

---

## Summary Table

| ID | Text (short) | Weight | Category | Pass Condition (short) |
|----|-------------|--------|----------|------------------------|
| C-01 | Role selection grounded in .craft/roles/ | essential | correctness | All role names exist in registry; depth-appropriate selection |
| C-02 | Review matrix structure present | essential | format | 4 columns, all reviewers present |
| C-03 | Severity uses HIGH/MEDIUM/LOW only | essential | correctness | No freestyle labels; semantics match finding content |
| C-04 | Each role reviews from its own perspective | essential | depth | Findings traceable to that role's lens; non-overlapping |
| C-05 | Recommendations are concrete | essential | depth | Named surface/action; 80% non-generic |
| C-06 | Depth flag respected | recommended | behavior | Standard 2-4 roles; deep = full registry |
| C-07 | Cross-role signal surfaced | recommended | coverage | At least one convergence or conflict named |
| C-08 | AMEND options listed | recommended | format | 2+ specific options; section present |
| C-09 | Inertia-advocate leads as challenger | recommended | depth | First row; null hypothesis stated |
| C-10 | Finding specificity: named surface | recommended | depth | 80%+ findings name a specific artifact surface |
| C-14 | Registry ERROR halt on missing/malformed data | recommended | correctness | Explicit ERROR halt -- no soft fallback; covers absent/empty/malformed |
| C-11 | Null hypothesis uses structured template | aspirational | depth | 3+ named fill-in slots, all completed |
| C-12 | Per-role lens-lock declaration | aspirational | depth | One-sentence lens declared before findings per role |
| C-13 | Typed column contracts with per-row validation | aspirational | format | Column type contracts visible; per-row validation gate present |
| C-15 | Challenger bracket as named execution phase | aspirational | depth | Challenger declared as discrete pre-domain phase; not an exception clause |
| C-16 | Slot-level failure escalation in null hypothesis | aspirational | depth | Empty slot -> logged HIGH finding; per-slot escalation rule present |
| C-17 | Challenger phase gate: formal exit condition | aspirational | depth | Challenger phase has explicit exit gate; domain review structurally blocked until gate clears |
| C-18 | Empty-slot escalation as separate matrix row | aspirational | depth | Each unfilled slot -> dedicated HIGH row in review matrix; not inline annotation |
| C-19 | Anti-pattern exclusion in typed column constraints | aspirational | format | At least one column definition names an explicit anti-pattern exclusion |
| C-20 | Multi-condition gate closure with named states | aspirational | depth | Gate has named states (OPEN/CLOSED) and 2+ enumerated closure conditions |
| C-21 | Anti-pattern exclusion in escalation rules | aspirational | depth | Escalation rule names prohibited output form inside the rule definition itself |
| C-22 | Slot-anchored matrix with numbered cross-references | aspirational | format | Matrix has Slot column; downstream elements reference findings by slot number |
| C-23 | Validation as a named discrete execution phase | aspirational | format | Validation declared as named phase at same structural level as CHALLENGE and REVIEW |
| C-24 | Criterion-check table embedded in VALIDATE phase | aspirational | format | VALIDATE phase contains structured table checking all aspirational criteria with YES/NO/PARTIAL + evidence citations |
| C-25 | Exhaustive anti-pattern coverage across all schema columns | aspirational | format | Every column definition carries an anti-pattern exclusion; no column exempt |
| C-26 | Criterion-check table is self-referentially complete | aspirational | format | Criterion-check table includes explicit rows for C-24 and C-25; table audits its own existence and anti-pattern exhaustiveness |
| C-27 | Per-slot synthesis coverage contract | aspirational | coverage | Every reviewer slot receives an explicit convergence/conflict/unique verdict addressed by slot number |

---

## Scoring Parameters

| Tier | Count | Per Criterion | Max |
|------|-------|--------------|-----|
| Essential | 5 | 12 | 60 |
| Recommended | 6 | 10 | 60 |
| Aspirational | 16 | 2.5 | 40 |
| **Total** | | | **160** |

PARTIAL = half points. Golden threshold: composite >= 80 with all essential passing.

---

## Score Examples

| Scenario | E pass | R pass | A pass | Composite | Golden? |
|----------|--------|--------|--------|-----------|---------|
| All pass | 5/5 | 6/6 | 16/16 | 60+60+40=160 | YES |
| All essential + 2 recommended | 5/5 | 2/6 | 0/16 | 60+20+0=80 | YES (at threshold) |
| All essential + all recommended | 5/5 | 6/6 | 0/16 | 60+60+0=120 | YES |
| All essential + 1 recommended | 5/5 | 1/6 | 0/16 | 60+10+0=70 | NO |
| 4 essential + all recommended | 4/5 | 6/6 | 0/16 | 48+60+0=108 | NO (essential gap) |
| All essential + 3 rec + 3 asp | 5/5 | 3/6 | 3/16 | 60+30+7.5=97.5 | YES |
| V-05 R7 equivalent (v7 perfect) | 5/5 | 6/6 | 14/16 | 60+60+35.0=155.0 | YES |
| V-01 R8 equivalent | 5/5 | 6/6 | 15/16 | 60+60+37.5=157.5 | YES |
| V-02 R8 equivalent | 5/5 | 6/6 | 15/16 | 60+60+37.5=157.5 | YES |
| Perfect (v8) | 5/5 | 6/6 | 16/16 | 60+60+40.0=160.0 | YES |

---

## Notes

- This rubric covers the **matrix-first** output form of crew-review. It does not score
  DISPOSITION_CONTRACT v1 structure (see org-review rubric series for that).
- The distinction: crew-review produces a review matrix; org-review produces a gated
  commitment disposition. Same underlying mechanism, different output contracts.
- C-09 and C-10 were promoted from aspirational to recommended in v2 based on R1 stability.
- C-14 was promoted from aspirational to recommended in v4 based on R3 stability (5/5
  PASS). It retains its original ID and moves into the recommended section after C-10.
- C-11 through C-13 and C-15 through C-16 are construction-time excellence signals from
  R1-R2: they capture how the prompt is structured, not just what the output contains.
  They are harder to score from output alone and may require prompt inspection.
- C-17 through C-19 are construction-time excellence signals from R3. C-17 extends C-15
  at the enforcement level (gate vs. named phase). C-18 extends C-16 at the structural
  level (matrix row vs. logged finding). C-19 extends C-13 at the precision level
  (exclusion clause vs. positive constraint).
- C-20 and C-21 are construction-time excellence signals from R4. C-20 extends C-17 at
  the state-machine level (named states + multi-condition closure vs. single exit
  condition). C-21 extends C-18 and C-19 jointly: the escalation rule applies C-19's
  exclusion pattern to the row-escalation contract.
- C-22 and C-23 are construction-time excellence signals from R6. C-22 extends C-02 and
  C-07: the matrix gains a Slot column that makes reviewer positions numbered anchors, and
  downstream cross-references use slot numbers for traceability. C-23 extends C-13 using
  the same structural elevation that C-15 applied to C-09: visible validation becomes a
  named discrete execution phase.
- C-24 and C-25 are construction-time excellence signals from R7 V-05 (first perfect score:
  155.0 under v7). C-24 extends C-23: the named VALIDATE phase becomes a meta-criterion
  checkpoint, embedding a structured table that audits all designed-to-satisfy aspirational
  criteria with YES/NO/PARTIAL status and evidence citations before the final matrix is
  written. C-25 extends C-19: the at-least-one-column anti-pattern exclusion pattern is
  applied exhaustively to every column -- including structural columns like Slot -- making
  the schema a complete failure-mode specification.
- C-26 and C-27 are construction-time excellence signals from R8. C-26 extends C-24:
  the criterion-check table closes its own self-referential gap by including explicit rows
  for C-24 and C-25, the two criteria that govern the table's existence and the schema's
  anti-pattern exhaustiveness. V-05 R7's table checked C-11 through C-23; V-01 R8 extends
  it to include C-24 and C-25 as first-class rows -- the table now audits its own
  completeness. C-27 extends C-07 and C-22: the minimum-count synthesis signal (at least
  one convergence/conflict) becomes an exhaustive slot-anchored coverage contract (every
  slot receives a verdict). This mirrors how C-25 extends C-19 from minimum-count to
  exhaustive coverage -- the same escalation discipline applied to the synthesis section.
- R7 breakthrough: C-12 (per-role lens-lock) is reliably achieved by making Lens a required
  output schema column rather than an execution instruction. V-02, V-03, and V-05 all
  achieved C-12 PASS via the Lens column; V-01 and V-04 failed without it. The mechanism
  is structural: a schema column violation is detectable; an ignored execution instruction
  is not.
- The full relationship chains:
  - Challenger phase: C-09 (challenger leads) -> C-15 (leads because phase) ->
    C-17 (phase because gate) -> C-20 (gate because state machine with named closure).
  - Null hypothesis template: C-11 (templated) -> C-16 (template enforced by escalation)
    -> C-18 (escalation is a matrix row) -> C-21 (row rule names its anti-form).
  - Schema quality: C-13 (typed column contracts) -> C-19 (contracts name failure modes)
    -> C-25 (all columns name failure modes -- exhaustive coverage).
    C-21 is the escalation analog of C-19 -- the same exclusion discipline applied to the
    escalation rule itself.
  - Matrix structure: C-02 (4-column matrix) -> C-22 (numbered-slot matrix with
    downstream cross-references).
  - Validation phase: C-13 (visible validation -- any mechanism) -> C-23 (validation as
    named discrete phase) -> C-24 (named phase contains embedded criterion-check audit)
    -> C-26 (criterion-check table includes its own governing criteria --
    self-referential completeness).
  - Synthesis coverage: C-07 (minimum-count signal) -> C-22 (slot column anchors
    downstream cross-references) -> C-27 (every slot receives a synthesis verdict --
    exhaustive coverage contract).
  - Each step in each chain makes the prior criterion correct-by-construction rather than
    by instruction.
- V-05 R7 equivalent under v8: E=60, R=60, A=C-11 through C-25 all PASS (35.0) +
  C-26 FAIL(0) + C-27 FAIL(0) = 35.0. Composite = 155.0.
- V-01 R8 equivalent under v8: E=60, R=60, A=C-11 through C-25 all PASS (35.0) +
  C-26 PASS(2.5) + C-27 FAIL(0) = 37.5. Composite = 157.5.
- V-02 R8 equivalent under v8: E=60, R=60, A=C-11 through C-25 all PASS (35.0) +
  C-26 FAIL(0) + C-27 PASS(2.5) = 37.5. Composite = 157.5.
- Scoring formula in v8: Essential 5 x 12 = 60, Recommended 6 x 10 = 60, Aspirational
  16 x 2.5 = 40. Max is 160. Golden threshold is composite >= 80 with all essential
  passing.
