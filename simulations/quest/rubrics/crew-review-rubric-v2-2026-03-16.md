Written to `simulations/quest/rubrics/crew-review-rubric-v2-2026-03-16.md`.

---

**What changed from v1 to v2:**

**Promotions (aspirational -> recommended):**
- **C-09** (inertia-advocate leads) — 3/4 R1 variations passed; single failure was missing-feature, not ambiguity
- **C-10** (finding specificity) — 4/4 R1 variations passed; no ambiguity found

**New aspirational criteria from R1 excellence signals:**

| ID | Pattern | Source | What it captures beyond existing |
|----|---------|--------|-----------------------------------|
| C-11 | Null hypothesis template | V-01, V-04 | Structured 3+ slot fill-in, not free-form prose (extends C-09) |
| C-12 | Per-role lens-lock | V-03, V-04 | One-sentence perspective declaration *before* findings, visible in output (extends C-04) |
| C-13 | Typed column contracts | V-02, V-05 | Column type enforcement + per-row validation gate (extends C-02/C-03 to correct-by-construction) |
| C-14 | Registry ERROR halt | V-01, V-04 | Hard stop on missing/malformed registry — no soft fallback (extends C-01) |

**Scoring formula update:** Recommended now 5 criteria × 10 pts = 50 pts; aspirational 4 criteria × 2.5 pts = 10 pts. Max is 120. Golden threshold (all essential + composite >= 80) is unchanged — still achievable with all essential + 2/5 recommended (60 + 20 = 80).
--

## Essential Criteria

All 5 must pass. A single essential failure disqualifies golden regardless of composite score.

---

### C-01 -- Role Selection Grounded in .craft/roles/

| Field | Value |
|-------|-------|
| ID | C-01 |
| Weight | essential |
| Category | correctness |

**Text**: Every reviewer row in the matrix names a role that exists in `.craft/roles/`. No
roles are invented. For standard depth, selected roles are relevant to the artifact type
(not arbitrary). For deep depth, all roles in `.craft/roles/` appear.

**Pass condition**: All reviewer names in the matrix match entries in `.craft/roles/`. Zero
fabricated role names. Standard run: roles are artifact-type-appropriate (e.g., a spec
artifact selects architect + PM, not support or SRE). Deep run: full registry coverage.

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
selected set is absent from the matrix.

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

Output is better with all five. Missing recommended criteria lower the composite score but
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

## Aspirational Criteria

Raise the bar once essential and recommended are stable. These criteria capture structural
excellence patterns observed in R1 golden variations (V-01, V-03, V-04) that go beyond
the output contract into prompt construction quality.

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

**Origin**: V-01 "3-blank null hypothesis template" (structural, not instructional); V-04
"null hypothesis template explicitly required."

---

### C-12 -- Per-Role Lens-Lock Declaration

| Field | Value |
|-------|-------|
| ID | C-12 |
| Weight | aspirational |
| Category | depth |

**Text**: Before writing any finding for a role, the output contains an explicit one-sentence
perspective declaration: "What does someone in this role actually care about?" The lens
statement precedes that role's findings and is visible as a declared constraint. This is a
structural protection beyond C-04's output check -- it forces perspective articulation
before finding generation.

**Pass condition**: Each reviewer row is preceded by or opens with a one-sentence lens
declaration traceable to that role's perspective (e.g., "As an architect, I care about
system boundary correctness and contract stability."). Declaration must be present for at
least all non-challenger reviewers. Lens statements that merely restate the role name
("As a PM, I am reviewing this as a PM.") do not pass.

**Origin**: V-03 "per-role lens-lock step forces perspective before finding"; V-04
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

**Origin**: V-02 "column type: enum -- Exactly one of: HIGH, MEDIUM, LOW. No other values
-- strongest enforcement"; V-05 "per-row validation table enforced before row is written."

---

### C-14 -- Registry ERROR Halt on Missing or Malformed Data

| Field | Value |
|-------|-------|
| ID | C-14 |
| Weight | aspirational |
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

**Origin**: V-01 "ERROR halt + 'do not fabricate' rule" as a structural gate before
selection; V-04 "ERROR halt if absent" named as an explicit stop condition in the prompt.

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
| C-11 | Null hypothesis uses structured template | aspirational | depth | 3+ named fill-in slots, all completed |
| C-12 | Per-role lens-lock declaration | aspirational | depth | One-sentence lens declared before findings per role |
| C-13 | Typed column contracts with per-row validation | aspirational | format | Column type contracts visible; per-row validation gate present |
| C-14 | Registry ERROR halt on missing/malformed data | aspirational | correctness | Explicit ERROR halt -- no soft fallback |

---

## Score Examples

| Scenario | E pass | R pass | A pass | Composite | Golden? |
|----------|--------|--------|--------|-----------|---------|
| All pass | 5/5 | 5/5 | 4/4 | 120 | YES |
| All essential + 2 recommended | 5/5 | 2/5 | 0/4 | 60+20+0=80 | YES (at threshold) |
| All essential + all recommended | 5/5 | 5/5 | 0/4 | 60+50+0=110 | YES |
| All essential + 1 recommended | 5/5 | 1/5 | 0/4 | 60+10+0=70 | NO |
| 4 essential + all recommended | 4/5 | 5/5 | 0/4 | 48+50+0=98 | NO (essential gap) |
| All essential + 3 rec + 2 asp | 5/5 | 3/5 | 2/4 | 60+30+5=95 | YES |
| V-01 equivalent (all pass) | 5/5 | 5/5 | 4/4 | 120 | YES |
| V-02 equivalent (C-04 partial, no C-09) | 4.5/5 | 4/5 | 2/4 | 54+40+5=99 | NO (essential gap) |

---

## Notes

- This rubric covers the **matrix-first** output form of crew-review. It does not score
  DISPOSITION_CONTRACT v1 structure (see org-review rubric series for that).
- The distinction: crew-review produces a review matrix; org-review produces a gated
  commitment disposition. Same underlying mechanism, different output contracts.
- C-09 and C-10 were promoted from aspirational to recommended in v2 based on R1 stability.
- C-11 through C-14 are construction-time excellence signals: they capture how the prompt
  is structured, not just what the output contains. They are harder to score from output
  alone and may require prompt inspection.
- The scoring formula changed in v2: recommended expands to 5 criteria at 10 pts each
  (50 pts total); aspirational is 4 criteria at 2.5 pts each (10 pts total). Max is 120.
  Golden threshold is unchanged at composite >= 80 with all essential passing.
