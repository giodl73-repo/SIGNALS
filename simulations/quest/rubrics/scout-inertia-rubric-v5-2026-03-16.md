Here is the complete v5 rubric:

---

```markdown
---
skill: quest-rubric
skill_target: scout-inertia
date: 2026-03-16
version: 5
---

# Scoring Rubric — scout-inertia

> Inertia is the primary competitor for every feature. This rubric enforces the central contract of
> scout-inertia: the output must answer "why does inertia lose?" If it cannot, the analysis fails
> regardless of quality elsewhere.

## Composite Score Formula

score = (essential_pass * 10)
      + (recommended_pass * 10)
      + (aspirational_new_pass * 5)

Where `aspirational_new_pass` counts only A-05 through A-10. A-01 through A-04 are structural
baseline; they do not contribute to the score but their presence is expected in all outputs.

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

**Score ceiling**: 110 (5 essential + 3 recommended + 6 aspirational-new).
```

---

## Changes from v4 to v5

| # | Change | Source |
|---|--------|--------|
| 1 | Formula revised: `aspirational_pass / 8 * 10` → `aspirational_new_pass * 5` | R4 scorecard formula |
| 2 | A-01 through A-04 reclassified as structural baseline (expected, not scored) | R4 scorecard |
| 3 | Score ceiling updated: 100 → 110 | formula change |
| 4 | **A-09** — FM-to-trigger chain citation | R4 V-04 pattern |
| 5 | **A-10** — Structure declaration | R4 combination-testing pattern |

---

**New aspirational criteria:**

**A-09 — FM-to-trigger chain citation** (traceability, 5 pts)
Each defeat condition (C-04) must name the specific failure mode (C-05) that makes switching possible. "Teams switch when FM-2 (weekly CSV silently drops rows above 65k) causes delivery failures" passes; "teams switch when costs become unsustainable" fails. V-04 scored 95 with A-05+A-06+A-08 but left this chain implicit. A-06 bridges enforce actor propagation (FM reveals actor); A-09 enforces mechanism propagation (FM drives trigger). Together they close the full chain: FM symptom → named actor → quantified cost → FM-grounded trigger.

**A-10 — Structure declaration** (auditability, 5 pts)
Output opens with a single line declaring which structural techniques are applied — e.g., "Structure: fail-first | question-primed | bridges." The declared techniques must match the actual structure. R4 tested five combinations distinguishable only by reading the full output. A declaration makes the gap between stated intent and actual execution a first-class quality signal: an analyst who declares "fail-first | bridges" and produces a linear checklist has produced a *structural* failure, detectable at a glance rather than on full read.

---

**Formula note**: The R4 scorecard already used `* 5` per aspirational (not the v4 `/8 * 10` formula), so this formalizes what R4 was already measuring. A-01–A-04 are reclassified as baseline (expected in all outputs) rather than scored, which matches how R4 treated them — V-01 through V-04 never earned points for them.
pecific, distinct, and testable conditions under
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

### Baseline (A-01 through A-04) — expected in all outputs, not scored separately

| ID | Criterion | Category |
|----|-----------|----------|
| A-01 | **Per-section revision gate** | enforcement |
| A-02 | **Column-level structural constraint** | enforcement |
| A-03 | **Composite gate with back-pointers** | enforcement |
| A-04 | **Role precision as continuation gate** | enforcement |

### Scored aspirational (A-05 through A-10) — 5 points each

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| A-05 | **Question-primed entry before table** | enforcement | aspirational |
| A-06 | **Cognitive linkage between adjacent sections** | structure | aspirational |
| A-07 | **ID-referenced synthesis across segments** | structure | aspirational |
| A-08 | **Fail-first ordering** | structure | aspirational |
| A-09 | **FM-to-trigger chain citation** | traceability | aspirational |
| A-10 | **Structure declaration** | auditability | aspirational |

---

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

### A-09 — FM-to-trigger chain citation

**Pass condition**: Each defeat condition (C-04) in the output must name the specific failure mode
(from C-05) that makes switching possible. The chain must be explicit: "teams switch when FM-2
(weekly CSV export silently drops rows above 65k) causes delivery failures" passes; "teams switch
when manual costs become unsustainable" fails. The reference must cite an observable FM symptom,
not a cost-tolerance threshold. Outputs without this citation leave the FM→trigger link implicit —
a reviewer cannot verify that triggers are grounded in failure evidence rather than in the
analyst's prior model of value.

The criterion is most naturally satisfied when A-08 (fail-first ordering) is also applied: if FMs
are numbered in Section 1, defeat conditions in Section 4 can cite FM numbers directly. Without
A-08, FMs and defeat conditions may be interleaved in a way that makes citation awkward — this is
expected and acceptable; the citation must still be present regardless of section order.

*Source*: R4 pattern — V-04 (A-05+A-06+A-08) scores 95 but leaves the FM-to-trigger chain
implicit even with bridges and fail-first in place. Bridges enforce actor propagation (FM
reveals actor); this criterion enforces mechanism propagation (FM drives trigger). The two
together close the full chain: FM symptom → named actor → quantified cost → FM-grounded trigger.

### A-10 — Structure declaration

**Pass condition**: Output opens with a single line declaring which structural techniques are
applied. Acceptable form: "Structure: fail-first | question-primed | bridges | segmented." The
declared techniques must match the actual structure of the output — if "fail-first" is declared,
Section 1 must be a failure-mode section; if "bridges" is declared, explicit transition
instructions must be present at section boundaries. A declaration that does not match the actual
structure fails. An output with no declaration and correct structure passes all other aspirationals
but fails A-10.

The declaration serves two purposes: (1) it forces the analyst to commit to structural choices
before filling content, making technique-drift detectable by comparing declared against actual;
(2) it allows a reviewer to evaluate aspirational criteria against a stated intent rather than
reconstructing the structure from the text.

*Source*: R4 pattern — R4 tested five structural combinations (V-01 through V-05), each
distinguishable only by reading the full section structure. In practice, the declared combination
is a quality signal in itself: analysts who declare "fail-first | bridges" and then produce a
linear checklist have produced a detectable failure at the structural level, not just at the
content level. The declaration makes aspirational technique application auditable at a glance.

---

## Scoring Reference

| Variation | Essential | Recommended | Aspirational-new | Score | Golden? |
|-----------|-----------|-------------|------------------|-------|---------|
| Perfect | 5/5 = 50 | 3/3 = 30 | 6/6 = 30 | **110** | YES |
| R4 max (V-04) | 5/5 = 50 | 3/3 = 30 | 3/6 = 15 | **95** | YES |
| R4 high (V-02) | 5/5 = 50 | 3/3 = 30 | 2/6 = 10 | **90** | YES |
| R4 mid (V-01, V-03) | 5/5 = 50 | 3/3 = 30 | 1/6 = 5 | **85** | YES |
| Min golden | 5/5 = 50 | 3/3 = 30 | 0/6 = 0 | **80** | YES |
| Recommended gap | 5/5 = 50 | 2/3 = 20 | 0/6 = 0 | **70** | NO — fails >= 80 |
| Essential only | 5/5 = 50 | 0/3 = 0 | 0/6 = 0 | **50** | NO — fails >= 80 |

---

## Changes from v4 to v5

| # | Change | Source |
|---|--------|--------|
| 1 | Formula revised: `aspirational_pass / 8 * 10` → `aspirational_new_pass * 5` | R4 scorecard formula |
| 2 | A-01 through A-04 reclassified as structural baseline (expected, not scored) | R4 scorecard |
| 3 | Score ceiling updated: 100 → 110 (6 scored aspirationals * 5 pts) | formula change |
| 4 | **A-09** — FM-to-trigger chain citation | R4 V-04 pattern |
| 5 | **A-10** — Structure declaration | R4 combination-testing pattern |

**New aspirational criteria in brief:**

- **A-09**: Each defeat condition must cite the specific failure mode that drives it. The FM→trigger
  link must be named explicitly — an observable symptom, not a cost-tolerance claim. Closes the
  chain that A-08 (fail-first) and A-06 (bridges) set up: FM symptom → named actor → quantified
  cost → FM-grounded trigger. V-04 scored 95 without this link; adding it closes the remaining
  implicit inference.

- **A-10**: Output opens with a one-line declaration of which structural techniques are applied.
  Forces analyst commitment before content entry; makes aspirational technique application auditable
  by comparison of declared vs actual structure. R4 tested five structural combinations — each was
  distinguishable only by reading the full output. A declaration makes the gap between stated intent
  and actual execution a first-class quality signal.
```
