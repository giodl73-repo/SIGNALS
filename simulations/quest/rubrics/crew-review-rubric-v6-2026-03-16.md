Written to `simulations/quest/rubrics/crew-review-rubric-v6-2026-03-16.md`.

---

**What changed v5 -> v6:**

Two new aspirational criteria extracted from R6 scorecard evidence:

| ID | Pattern | Source | Extends |
|----|---------|--------|---------|
| C-22 | Slot-anchored matrix with numbered cross-references | V-03 R6 | C-02, C-07 |
| C-23 | Validation as a named discrete execution phase | V-02 R6 | C-13 |

**C-22** — V-03 R6's 5-column schema (Slot, Role, Findings, Severity, Recommendation) + synthesis "references slot numbers." The Slot column makes every reviewer position a numbered anchor; downstream cross-references use slot numbers rather than role names, making traceability machine-checkable. C-02 allows superset schemas to pass silently; C-22 requires the superset to include a Slot column AND use it.

**C-23** — V-02 R6's PHASE 4 VALIDATE: a first-class named execution phase at the same structural level as PHASE 1 LOAD, PHASE 2 CHALLENGE, PHASE 3 REVIEW. C-13 requires visible validation (any mechanism passes); C-23 requires validation to be a named phase. The structural elevation is the exact same move C-15 made on C-09: "challenger leads" → "challenger is a named phase" :: "validation is visible" → "validation is a named phase."

**Scoring:** Aspirational 12 × 2.5 = 30, max 150 (was 145). Golden threshold unchanged at 80.

**R6 scores under v6:**
- V-01: 54 + 60 + 23.75 = **137.75** (C-22 FAIL, C-23 FAIL)
- V-02: 60 + 60 + 23.75 = **143.75** (C-23 PASS +2.5)
- V-03: 60 + 60 + 21.25 = **141.25** (C-22 PASS +2.5)

**New relationship chains:**
- Matrix structure: C-02 → C-22
- Validation phase: C-13 → C-23 (mirroring C-09 → C-15)
 FAIL, C-23 FAIL -- no slot column, no named validation phase)
- V-02: 60 + 60 + 23.75 = **143.75** (C-23 PASS adds 2.5; C-22 FAIL)
- V-03: 60 + 60 + 21.25 = **141.25** (C-22 PASS adds 2.5; C-23 FAIL)

The relationship chains now extend:
- Challenger phase chain: C-09 (challenger leads) -> C-15 (leads because phase) ->
  C-17 (phase because gate) -> C-20 (gate because state machine with named closure).
- Null hypothesis template chain: C-11 (templated) -> C-16 (template enforced by escalation)
  -> C-18 (escalation is a matrix row) -> C-21 (row rule names its anti-form).
- Schema quality chain: C-13 (typed column contracts) -> C-19 (contracts name failure modes).
  C-21 is the escalation analog of C-19.
- Matrix structure chain: C-02 (4-column matrix) -> C-22 (matrix with numbered slot anchors).
- Validation phase chain: C-13 (visible validation) -> C-23 (validation as named phase).
  C-23 mirrors C-15: it elevates visible validation to a structural phase exactly as C-15
  elevated "challenger leads" to "challenger is a named phase."

---

## Essential Criteria

All five must pass for golden to be possible. A FAIL on any essential criterion is
disqualifying regardless of composite score.

---

### C-01 -- Role Selection Grounded in .roles/

| Field | Value |
|-------|-------|
| ID | C-01 |
| Weight | essential |
| Category | correctness |

**Text**: All reviewer roles are drawn exclusively from the `.roles/` registry. The
registry is read at execution time. No roles are fabricated, invented from memory, or
substituted from prior run defaults. Every role name in the output corresponds to an entry
that exists in the registry at review time.

**Pass condition**: Every role named in the output has a corresponding file in
`.roles/`. No fabricated roles. Reviewer selection reflects the requested depth:
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
additional Slot column) passes if the four required columns are present.

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
artifacts). Deep depth includes all roles from `.roles/`. Output reflects the correct
scope for the invoked depth -- neither over-selects (standard) nor under-selects (deep).

**Pass condition**: Standard: reviewer count is 2-4 unless the artifact type warrants more.
Deep: reviewer count equals the full `.roles/` registry size. If depth is unstated,
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

**Pass condition**: inertia-advocate (or equivalent challenger role from `.roles/`)
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
if `.roles/` is absent, unreadable, or any role file is missing required fields
(e.g., `lens.verify`, `archetype`). The halt is unconditional: the review does not proceed
with partial data or invented substitutes. This is a defensive mechanism beyond C-01's
name-matching requirement.

**Pass condition**: Output or prompt structure contains an ERROR branch that fires if the
registry read returns an empty set, missing files, or files without required fields. The
ERROR message is explicit (e.g., "ERROR: .roles/ not found -- cannot proceed") and
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
R4. C-22 through C-23 are new from R6.

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
structure, not a background instruction.

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

## Summary Table

| ID | Text (short) | Weight | Category | Pass Condition (short) |
|----|-------------|--------|----------|------------------------|
| C-01 | Role selection grounded in .roles/ | essential | correctness | All role names exist in registry; depth-appropriate selection |
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

---

## Scoring Parameters

| Tier | Count | Per Criterion | Max |
|------|-------|--------------|-----|
| Essential | 5 | 12 | 60 |
| Recommended | 6 | 10 | 60 |
| Aspirational | 12 | 2.5 | 30 |
| **Total** | | | **150** |

PARTIAL = half points. Golden threshold: composite >= 80 with all essential passing.

---

## Score Examples

| Scenario | E pass | R pass | A pass | Composite | Golden? |
|----------|--------|--------|--------|-----------|---------|
| All pass | 5/5 | 6/6 | 12/12 | 60+60+30=150 | YES |
| All essential + 2 recommended | 5/5 | 2/6 | 0/12 | 60+20+0=80 | YES (at threshold) |
| All essential + all recommended | 5/5 | 6/6 | 0/12 | 60+60+0=120 | YES |
| All essential + 1 recommended | 5/5 | 1/6 | 0/12 | 60+10+0=70 | NO |
| 4 essential + all recommended | 4/5 | 6/6 | 0/12 | 48+60+0=108 | NO (essential gap) |
| All essential + 3 rec + 3 asp | 5/5 | 3/6 | 3/12 | 60+30+7.5=97.5 | YES |
| V-01 R6 equivalent | 4.5/5 | 6/6 | 9.5/12 | 54+60+23.75=137.75 | YES |
| V-02 R6 equivalent | 5/5 | 6/6 | 9.5/12 | 60+60+23.75=143.75 | YES |
| V-03 R6 equivalent | 5/5 | 6/6 | 8.5/12 | 60+60+21.25=141.25 | YES |

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
- The full relationship chains:
  - Challenger phase: C-09 (challenger leads) -> C-15 (leads because phase) ->
    C-17 (phase because gate) -> C-20 (gate because state machine with named closure).
  - Null hypothesis template: C-11 (templated) -> C-16 (template enforced by escalation)
    -> C-18 (escalation is a matrix row) -> C-21 (row rule names its anti-form).
  - Schema quality: C-13 (typed column contracts) -> C-19 (contracts name failure modes).
    C-21 is the escalation analog of C-19 -- the same exclusion discipline applied to the
    escalation rule itself.
  - Matrix structure: C-02 (4-column matrix) -> C-22 (numbered-slot matrix with
    downstream cross-references).
  - Validation phase: C-13 (visible validation -- any mechanism) -> C-23 (validation as
    named discrete phase -- structural elevation mirroring C-09 -> C-15).
  - Each step in each chain makes the prior criterion correct-by-construction rather than
    by instruction.
- V-01 R6 equivalent: E=54 (C-04 PARTIAL=6), R=60, A=C-11 PASS(2.5)+C-12 FAIL(0)+
  C-13 PARTIAL(1.25)+C-15 PASS(2.5)+C-16 PASS(2.5)+C-17 PASS(2.5)+C-18 PASS(2.5)+
  C-19 PASS(2.5)+C-20 PASS(2.5)+C-21 PASS(2.5)+C-22 FAIL(0)+C-23 FAIL(0) = 23.75.
  Composite = 137.75.
- V-02 R6 equivalent: E=60, R=60, A=C-11 PASS(2.5)+C-12 FAIL(0)+C-13 PASS(2.5)+
  C-15 PASS(2.5)+C-16 PASS(2.5)+C-17 PASS(2.5)+C-18 PASS(2.5)+C-19 PARTIAL(1.25)+
  C-20 PASS(2.5)+C-21 PASS(2.5)+C-22 FAIL(0)+C-23 PASS(2.5) = 23.75. Composite = 143.75.
- V-03 R6 equivalent: E=60, R=60, A=C-11 PASS(2.5)+C-12 FAIL(0)+C-13 PARTIAL(1.25)+
  C-15 PASS(2.5)+C-16 PASS(2.5)+C-17 PASS(2.5)+C-18 PASS(2.5)+C-19 FAIL(0)+
  C-20 PASS(2.5)+C-21 PASS(2.5)+C-22 PASS(2.5)+C-23 FAIL(0) = 21.25. Composite = 141.25.
- Scoring formula in v6: Essential 5 x 12 = 60, Recommended 6 x 10 = 60, Aspirational
  12 x 2.5 = 30. Max is 150. Golden threshold is composite >= 80 with all essential
  passing.
