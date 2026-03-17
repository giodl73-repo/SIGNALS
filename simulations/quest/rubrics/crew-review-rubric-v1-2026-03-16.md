---
skill: quest-rubric
skill_target: crew-review
date: 2026-03-16
version: 1
---

# crew-review — Scoring Rubric v1

`crew-review` runs any artifact through the full org. It reads `.craft/roles/`, selects
relevant reviewers based on artifact type, and produces a **review matrix**: role, findings,
severity, recommendation. `--depth deep` runs all roles; standard runs relevant roles only.
`AMEND` adds a specific reviewer or changes scope.

This rubric covers the v1 output contract. The org-review skill (which shares the same
underlying mechanism) has a separate rubric tracking the DISPOSITION_CONTRACT v1 structure.
This rubric scores the simpler matrix-first output form described in the crew-review spec.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential pass AND composite >= 80.

Max score: 100 (all pass). Minimum for golden: 60 + 20 + 0 = 80 (all essential, 2/3 recommended).

---

## Essential Criteria

All 5 must pass. A single essential failure disqualifies golden regardless of composite score.

---

### C-01 — Role Selection Grounded in .craft/roles/

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

### C-02 — Review Matrix Structure Present

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

### C-03 — Severity Uses Defined Semantics

| Field | Value |
|-------|-------|
| ID | C-03 |
| Weight | essential |
| Category | correctness |

**Text**: All severity values in the matrix are HIGH, MEDIUM, or LOW — matching the
standard semantics: HIGH blocks commitment, MEDIUM conditions commitment, LOW is advisory.
No freestyle severity labels (e.g., "Critical", "Minor", "Warning").

**Pass condition**: Every severity cell contains exactly HIGH, MEDIUM, or LOW. At least one
severity assignment is justified by finding content (a HIGH finding describes something that
would block commitment; a LOW finding describes something advisory). No severity cell is
blank or uses a non-standard label.

---

### C-04 — Each Role Reviews from Its Own Perspective

| Field | Value |
|-------|-------|
| ID | C-04 |
| Weight | essential |
| Category | depth |

**Text**: Each reviewer's findings are traceable to that role's documented `lens.verify`
and `expertise.depth`. Findings are not copy-pasted across roles. A PM finding should not
appear identically in an architect row.

**Pass condition**: For each reviewer row, at least one finding is identifiably from that
role's lens — i.e., it references a concern that only that role's frame would surface (PM:
commitment threshold, signal sufficiency; architect: system boundary, contract correctness;
inertia-advocate: null hypothesis, switching cost). Findings across rows are distinguishable
by perspective.

---

### C-05 — Recommendations are Concrete and Role-Specific

| Field | Value |
|-------|-------|
| ID | C-05 |
| Weight | essential |
| Category | depth |

**Text**: Each recommendation in the matrix is actionable and names what to change — not
generic ("needs improvement"). It references the finding's specific surface, field, or gap.

**Pass condition**: No recommendation row contains only a generic directive. Each
recommendation names a specific artifact surface, section, or action (e.g., "Add switching
cost estimate to §3 before committing", not "Review the proposal"). At least 80% of
recommendation cells meet this standard.

---

## Recommended Criteria

Output is better with all three. Missing recommended criteria lower the composite score
but do not disqualify golden on their own.

---

### C-06 — Depth Flag Respected

| Field | Value |
|-------|-------|
| ID | C-06 |
| Weight | recommended |
| Category | behavior |

**Text**: Standard depth selects only artifact-relevant roles (2-4 roles for typical
artifacts). Deep depth includes all roles from `.craft/roles/`. Output reflects the correct
scope for the invoked depth — neither over-selects (standard) nor under-selects (deep).

**Pass condition**: Standard: reviewer count is 2-4 unless the artifact type warrants more.
Deep: reviewer count equals the full `.craft/roles/` registry size. If depth is unstated,
standard is assumed and the standard pass condition applies.

---

### C-07 — Cross-Role Signal Surfaced

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

### C-08 — AMEND Options Listed

| Field | Value |
|-------|-------|
| ID | C-08 |
| Weight | recommended |
| Category | format |

**Text**: Output ends with an AMEND section listing at least 2 named amendment options:
add a specific reviewer, change the scope, change the depth. This follows the
signal-lifecycle amend phase.

**Pass condition**: AMEND section present. At least 2 options named (add reviewer / change
scope / change depth). Options are specific — "add signal:strategy reviewer" not "add more
reviewers". Missing AMEND section = FAIL.

---

## Aspirational Criteria

Raise the bar once essential and recommended are stable.

---

### C-09 — Inertia-Advocate Leads as Challenger

| Field | Value |
|-------|-------|
| ID | C-09 |
| Weight | aspirational |
| Category | depth |

**Text**: Even in standard depth, the inertia-advocate appears as the first reviewer and
opens with a null hypothesis statement: what the team does today instead of building this.
The challenger bracket pattern is honored — the first review challenges the artifact from
the "do nothing" frame before any constructive domain review.

**Pass condition**: inertia-advocate (or equivalent challenger role from `.craft/roles/`)
appears first in the matrix. That row includes a null hypothesis statement or explicit
"do nothing" framing. The null hypothesis specifies what the team currently does as the
alternative to the artifact.

---

### C-10 — Finding Specificity: Named Surface

| Field | Value |
|-------|-------|
| ID | C-10 |
| Weight | aspirational |
| Category | depth |

**Text**: Each finding names a specific surface, section, or component of the artifact
being reviewed — not abstract observations. "The §3 scope enumeration is missing a surface
for edge-case handling" is specific. "This needs more detail" is not.

**Pass condition**: >= 80% of all finding cells in the matrix name a specific artifact
section, field, named concept, or component. Generic observations without a named surface
count as failing the 80% bar. An output where every finding is surface-specific passes.

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
| C-09 | Inertia-advocate leads as challenger | aspirational | depth | First row; null hypothesis stated |
| C-10 | Finding specificity: named surface | aspirational | depth | 80%+ findings name a specific artifact surface |

---

## Score Examples

| Scenario | E pass | R pass | A pass | Composite | Golden? |
|----------|--------|--------|--------|-----------|---------|
| All pass | 5/5 | 3/3 | 2/2 | 100 | YES |
| All essential + 2 recommended | 5/5 | 2/3 | 0/2 | 60+20+0=80 | YES (at threshold) |
| All essential + 1 recommended | 5/5 | 1/3 | 0/2 | 60+10+0=70 | NO |
| 4 essential + all recommended | 4/5 | 3/3 | 0/2 | 48+30+0=78 | NO (essential gap) |
| All essential + all recommended | 5/5 | 3/3 | 0/2 | 60+30+0=90 | YES |

---

## Notes

- This rubric covers the **matrix-first** output form of crew-review. It does not score
  DISPOSITION_CONTRACT v1 structure (see org-review rubric series for that).
- The distinction: crew-review produces a review matrix; org-review produces a gated
  commitment disposition. Same underlying mechanism, different output contracts.
- C-09 and C-10 are stable once org-review rubric patterns have been validated. They can
  be promoted to recommended in v2 if consistent excellence patterns emerge.
