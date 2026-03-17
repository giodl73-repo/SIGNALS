Here is the complete updated rubric:

---

**Changes from v3 to v4:**

| # | Change | Source |
|---|--------|--------|
| 1 | Formula denominator: `/ 4` → `/ 8` | tracks actual count |
| 2 | C-02 note: adversarial framing doesn't exempt from dimensional coverage | V-04 R3 C-02 FAIL |
| 3 | **A-05** — Question-primed entry before table | V-01 R3 |
| 4 | **A-06** — Cognitive linkage between adjacent sections | V-03 R3 |
| 5 | **A-07** — ID-referenced synthesis across segments | V-02 R3 |
| 6 | **A-08** — Fail-first ordering | V-03 R3 |

**New aspirational criteria in brief:**

- **A-05**: A prose-first question precedes each table, forcing the analyst to formulate the answer as a sentence before entering it — weak answers become visibly inconsistent with what was just written.
- **A-06**: Section transitions explicitly name what the prior section produced and how it constrains the next section's entries ("failures you found in Step 1 reveal who bears the cost — use those names in Step 2"). Prevents independent-checklist cognition.
- **A-07**: Segmented analyses (Pass A/B, team types) require synthesis to cite specific artifact IDs (DC-A2, DC-B1), not free-prose summaries. ID-referencing makes synthesis drift structurally detectable.
- **A-08**: Failure modes section precedes workaround identity. Ordering failure modes first makes FM quality determinative — the analyst cannot rationalize the workaround before naming what breaks it. Strongest when combined with A-06.

The V-04 adversarial framing pattern was captured as a C-02 note rather than a new aspirational criterion — it's a structural option, but its R3 implementation demonstrated it can silently drop dimensional coverage, making it a caution rather than a target.
tion"). Purely qualitative labels ("high", "low") do not pass. The AMEND requirement
is that costs are quantified; this criterion enforces it. Note: structural framing (e.g.,
adversarial advocate/rebuttal) does not exempt the output from dimensional coverage — at least two
distinct dimensions must be addressed regardless of the organizing structure.

### C-03 — Inertia threat score is HIGH

**Pass condition**: Output explicitly states the inertia threat score as HIGH. The default is always
HIGH — the output must not silently omit the score, and must not downgrade it without documented
evidence of an unusual mitigating factor with a named rationale. "Inertia is LOW because the feature
is compelling" fails; compelling features do not reduce inertia, they only affect adoption after
switching costs are paid.

### C-04 — "Why inertia loses" answered with specifics

**Pass condition**: Output provides at least two specific, distinct, and testable conditions under
which teams abandon the workaround in favor of the feature. Conditions must be falsifiable ("teams
switch when workaround fails to handle files > 10MB" passes; "teams switch when they see the value"
fails). This is the central question of the skill — if it is absent, the output is not useful.

### C-05 — Workaround failure modes identified

**Pass condition**: Output identifies at least two specific scenarios where the current workaround
breaks, produces errors, causes re-work, or cannot scale. These are the observable cracks in the
inertia armor. Generic pain points ("manual is slow") do not pass; concrete failure modes ("CSV
export silently truncates rows over 65,536 — no error message") pass.

---

## Recommended Criteria

*Strong outputs satisfy all three. Missing one is a quality signal, not a blocker.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| R-01 | **Trigger scoped to team type** | precision | recommended |
| R-02 | **Role-level precision** | precision | recommended |
| R-03 | **At least one cost cited to role** | depth | recommended |

### R-01 — Trigger scoped to team type

**Pass condition**: Defeat conditions (from C-04) name a specific team type or segment rather than
applying uniformly to all users. "Engineering teams switch when..." or "PMs in regulated industries
switch when..." passes. "Users switch when..." fails. Different team types face different inertia
profiles; a trigger that ignores team type is underspecified.

### R-02 — Role-level precision

**Pass condition**: Every actor named in the analysis (workaround performer, decision-maker,
affected party) is identified at role level, not department or group level. "The PM" or "a data
analyst" passes. "The team", "users", or "marketing" fails. Role-level precision is required because
switching cost and trigger conditions vary by role — a department label cannot carry that weight.

### R-03 — At least one cost cited to role

**Pass condition**: At least one quantified cost from C-02 is tied to a specific actor or role
named elsewhere in the analysis. A floating number with no actor is weaker than a number anchored
to a person who pays it. "2 hours per PM per week" with PMs named as the workaround performer
passes. "2 hours" with no role anchor is a partial pass.

---

## Aspirational Criteria

*Outputs that satisfy these are structurally self-enforcing — the analyst cannot produce a weak
output without the structure itself flagging the gap.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| A-01 | **Per-section revision gate** | enforcement | aspirational |
| A-02 | **Column-level structural constraint** | enforcement | aspirational |
| A-03 | **Composite gate with back-pointers** | enforcement | aspirational |
| A-04 | **Role precision as continuation gate** | enforcement | aspirational |
| A-05 | **Question-primed entry before table** | enforcement | aspirational |
| A-06 | **Cognitive linkage between adjacent sections** | structure | aspirational |
| A-07 | **ID-referenced synthesis across segments** | structure | aspirational |
| A-08 | **Fail-first ordering** | structure | aspirational |

### A-01 — Per-section revision gate

**Pass condition**: Each section of the output contains an explicit self-score with a defined pass
condition. An analyst who completes a section must actively mark it pass or fail before moving on.
Sections without self-scores allow the analyst to move forward on weak entries; sections with
self-scores create a local revision loop at the point where correction cost is lowest.

### A-02 — Column-level structural constraint

**Pass condition**: Every column or field in the output carries an explicit semantic contract
(e.g., "this cell must contain a role name, not a department"). Column headers that are labels only
("Who") do not pass; column headers with embedded type constraints ("Who [role, not department]")
pass. The constraint must be visible to the analyst at the moment of entry, not only at review.

### A-03 — Composite gate with back-pointers

**Pass condition**: The output includes a final gate section that aggregates all per-criterion
pass/fail results and, for each failure, names the specific section number to return to for
correction. An advisory self-score does not pass. The gate must function as a completion blocker:
an analyst cannot declare the artifact done while any criterion cell contains a failure without
being directed to the exact section that requires revision. A gate section that lists criteria
without section back-pointers is advisory, not structural.

*Source*: V-01 (R2) excellence signal — Section 6 as a cross-criterion completion gate rather than
a summary score.

### A-04 — Role precision as continuation gate

**Pass condition**: Role precision is enforced as a pre-condition for entering subsequent sections,
not as a scoring note at the end. The check must appear early in the output — at or before the
point where roles are first declared — with an explicit instruction to correct before continuing.
Acceptable form: *"If the 'who performs it' entry contains 'teams', 'users', 'people', or a
department name, replace it before continuing to the next section."* A role precision check that
appears only in a final review section or in the rubric rather than in the output template does not
pass; by that point the analyst has already built subsequent sections on an underspecified actor.

*Source*: V-01 (R2) excellence signal — role check in Section 1 as a pre-condition for Section 2
entry, enforced at the moment of lowest correction cost.

### A-05 — Question-primed entry before table

**Pass condition**: Each table that records a critical claim (workaround identity, failure mode,
defeat condition) is preceded by a prose-first prompt that requires the analyst to formulate the
answer as a sentence before transferring it into the table. The prompt must be structured so that a
weak answer (department-level actor, generic pain point, non-falsifiable condition) is visibly
inconsistent with the sentence already written. A table introduced only by a section heading does
not pass. A table introduced by a question that directs the analyst to name a specific actor,
mechanism, or observable threshold before entering the row passes.

*Source*: V-01 (R3) excellence signal — prose-first question in Section 1 forcing formulation of
the role-specific workaround before table entry, producing higher-precision first-pass entries than
tables entered cold.

### A-06 — Cognitive linkage between adjacent sections

**Pass condition**: Gate or transition instructions between sections explicitly name what was
learned in the preceding section and state how that learning should constrain or inform the
following section's entries. A section transition that says only "proceed to Section 2" does not
pass. A transition that says "the failures you identified in Section 1 reveal who bears the
workaround cost — use those specific actors to fill the role column in Section 2" passes. The
linkage must be directional (earlier output informs later input) and specific (names the prior
output and the downstream constraint it creates).

*Source*: V-03 (R3) excellence signal — A-04 gate instruction: "The failures from Step 1 reveal
who is responsible — use that to name the role precisely." This turned a role-precision gate into
a causal bridge, preventing analysts from treating sections as independent checklists.

### A-07 — ID-referenced synthesis across segments

**Pass condition**: When the analysis is divided into segments — by team type, by pass (A/B), by
persona, or by any other axis — the synthesis section is required to reference specific artifact
IDs from each segment (e.g., DC-A2, DC-B1) rather than restating conclusions in free prose. A
synthesis section that summarizes "both teams face similar switching costs" without citing the
specific defeat condition or cost entry it is summarizing does not pass. A synthesis section that
says "DC-A2 and DC-B1 share a data-volume trigger — teams switch when the workaround cannot handle
files above threshold" with IDs traceable to prior entries passes. ID-referencing prevents
synthesis from drifting to generic conclusions not supported by the segment-level evidence.

*Source*: V-02 (R3) excellence signal — mandatory synthesis section requiring references to DC-A
and DC-B IDs by name, with the "Do not skip it" directive and a dedicated synthesis self-score.
The scorecard noted that R-01 "cannot fail if synthesis references DC-A and DC-B IDs" — the
structural linkage made the recommended criterion structurally unreachable as a failure.

### A-08 — Fail-first ordering

**Pass condition**: The failure mode section (C-05) precedes the workaround identity section
(C-01) in the output's section order. Ordering failure modes first creates a cognitive constraint:
the analyst must name what breaks before constructing the narrative of what the workaround is and
who performs it. When workaround identity comes first, analysts tend to rationalize the workaround
before examining its failure points. When failure modes come first, the actor identity and
switching costs that follow are grounded in observed breakdowns rather than in the analyst's prior
model of the workaround. The ordering effect is strongest when the A-06 cognitive linkage
criterion is also satisfied — the gate instruction can then direct: "the failures you named in
Section 1 reveal which actors are responsible; use those names in Section 2."

*Source*: V-03 (R3) excellence signal — Step 1 (failure modes) before Step 2 (workaround
identity), with C-05 self-score blocking Step 2 entry until triggers are specific. The scorecard
noted this as the only variation with a cascading C-01 gate: C-01 failure in Step 2 redirected
back to Step 1 to find more specific failure modes before attempting to reconstruct the workaround
identity, making FM quality structurally determinative rather than advisory.

---

## Scoring Reference

| Variation | Essential | Recommended | Aspirational | Score | Golden? |
|-----------|-----------|-------------|--------------|-------|---------|
| Perfect | 5/5 → 60 | 3/3 → 30 | 8/8 → 10 | **100** | YES |
| Min golden (A) | 5/5 → 60 | 2/3 → 20 | 0/8 → 0 | **80** | YES |
| Min golden (B) | 5/5 → 60 | 1/3 → 10 | 4/8 → 5 | **75** | NO — fails >= 80 |
| Aspirational sweep | 5/5 → 60 | 3/3 → 30 | 4/8 → 5 | **95** | YES |
| Essential only | 5/5 → 60 | 0/3 → 0 | 0/8 → 0 | **60** | NO — fails >= 80 |
```

---

Four changes from v3:

1. **Formula**: `aspirational_pass / 4 * 10` → `aspirational_pass / 8 * 10` (denominator tracks
   actual count)
2. **C-02 note added**: adversarial framing does not exempt the output from three-dimension
   coverage — extracted from V-04 (R3) C-02 FAIL signal.
3. **Added A-05** (question-primed entry) from V-01 (R3) excellence signal — prose-first prompt
   before table forces formulation and makes weak answers visibly inconsistent before entry.
4. **Added A-06** (cognitive linkage) from V-03 (R3) excellence signal — section transitions that
   name what the prior section produced and how it constrains the next section's entries.
5. **Added A-07** (ID-referenced synthesis) from V-02 (R3) excellence signal — synthesis sections
   in segmented analyses must reference artifact IDs, preventing drift from segment-level evidence.
6. **Added A-08** (fail-first ordering) from V-03 (R3) excellence signal — failure modes precede
   workaround identity; ordering makes FM quality structurally determinative rather than advisory.
