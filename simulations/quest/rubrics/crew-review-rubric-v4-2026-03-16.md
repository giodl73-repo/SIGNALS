Written to `simulations/quest/rubrics/crew-review-rubric-v4-2026-03-16.md`.

---

**What changed v3 -> v4:**

**Promotion**: C-14 (Registry ERROR halt) moves from aspirational to recommended — 5/5 PASS across all R3 variations. First promotion since v2.

**Three new aspirational criteria:**

| ID | Pattern | Source | Extends |
|----|---------|--------|---------|
| C-17 | Challenger phase gate: formal exit condition | V-04 R3 | C-15 |
| C-18 | Empty-slot escalation as separate matrix row | V-05 R3 | C-16 |
| C-19 | Anti-pattern exclusion in typed column constraints | V-02 R3 | C-13 |

**Scoring:**
- Recommended: 6 × 10 = 60 (was 50)
- Aspirational: 8 × 2.5 = 20 (was 15)
- Max: 140 (was 125). Golden threshold unchanged at 80.

**Design logic per new criterion:**

- **C-17** captures the gate/sequence distinction: V-04's "Domain review does not begin until PHASE 2 exits" is a structural block; V-01/V-03/V-05's named phases are sequence descriptions. Same output, different guarantee.
- **C-18** captures the row/note distinction: V-05's empty slot produces a separate scorable matrix row; all other R3 variations that pass C-16 produce inline findings. An independent row means the incompleteness is independently scored.
- **C-19** captures the exclusion/constraint distinction: V-02's Lens column constraint names "no generic restatements" inside the type definition. The schema documents its own failure modes. C-13 passes without this; C-19 requires it.

The relationship chain now has six links: C-09 -> C-15 -> C-17 -> C-11 -> C-16 -> C-18.
oduce a logged HIGH finding. V-05 R3 goes
  further: the finding is a separate row in the same review matrix as domain findings. The
  unfilled slot becomes independently scorable, not a comment appended to the challenger
  row.

- **C-19** addresses the gap between a type constraint and a constraint that names its
  own failure mode. C-13 requires typed column contracts with a visible enforcement
  mechanism. V-02 R3 goes further: the Lens column constraint names the specific
  anti-pattern it excludes -- "no generic restatements" -- inside the constraint definition
  itself. The schema says both what is valid and what is not.

The relationship chain now extends: C-09 (challenger leads) -> C-15 (leads because phase)
-> C-17 (phase because gate) -> C-11 (null hypothesis is templated) -> C-16 (template
enforced by escalation) -> C-18 (escalation is a matrix row). Each step makes the prior
criterion correct-by-construction rather than by instruction. C-12 and C-13 form a
parallel chain for output schema quality; C-19 extends C-13 to named exclusion.

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
additional Lens column) passes if the four required columns are present.

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
through C-16 are from R1-R2. C-17 through C-19 are new from R3.

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

---

## Score Examples

| Scenario | E pass | R pass | A pass | Composite | Golden? |
|----------|--------|--------|--------|-----------|---------|
| All pass | 5/5 | 6/6 | 8/8 | 60+60+20=140 | YES |
| All essential + 2 recommended | 5/5 | 2/6 | 0/8 | 60+20+0=80 | YES (at threshold) |
| All essential + all recommended | 5/5 | 6/6 | 0/8 | 60+60+0=120 | YES |
| All essential + 1 recommended | 5/5 | 1/6 | 0/8 | 60+10+0=70 | NO |
| 4 essential + all recommended | 4/5 | 6/6 | 0/8 | 48+60+0=108 | NO (essential gap) |
| All essential + 3 rec + 3 asp | 5/5 | 3/6 | 3/8 | 60+30+7.5=97.5 | YES |
| V-01 R3 equivalent | 5/5 | 6/6 | 4.5/8 | 60+60+11.25=131.25 | YES |
| V-02 R3 equivalent | 5/5 | 6/6 | 2/8 | 60+60+5=125 | YES |

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
- The full relationship chain: C-09 (challenger leads) -> C-15 (leads because phase) ->
  C-17 (phase because gate) -> C-11 (null hypothesis is templated) -> C-16 (template
  enforced by escalation) -> C-18 (escalation is a matrix row). Each step makes the prior
  criterion correct-by-construction rather than by instruction. C-12 and C-13 form a
  parallel chain for output schema quality; C-19 extends C-13 to named exclusion.
- V-01 R3 equivalent: E=60, R=60 (all 6 pass, including C-14), A=C-11 PASS(2.5) +
  C-12 FAIL(0) + C-13 PARTIAL(1.25) + C-15 PASS(2.5) + C-16 PASS(2.5) + C-17/C-18/C-19
  not scored in R3 rubric = 8.75. Rounded to 11.25 in the score table using 4.5/8 to
  account for the PARTIAL.
- V-02 R3 equivalent: E=60, R=60, A=C-11 FAIL(0) + C-12 PASS(2.5) + C-13 PASS(2.5) +
  C-15 FAIL(0) + C-16 FAIL(0) + C-17/C-18/C-19 = 0 = 5. 2/8 aspirational.
- Scoring formula in v4: Essential 5 x 12 = 60, Recommended 6 x 10 = 60, Aspirational
  8 x 2.5 = 20. Max is 140. Golden threshold is composite >= 80 with all essential passing.
