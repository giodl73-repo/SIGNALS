Here is the complete v6 rubric with all changes applied.

---

## Changes from v5 to v6

| # | Change | Source |
|---|--------|--------|
| 1 | **A-09 → baseline** | Universally passed R5; no longer a scoring differentiator |
| 2 | **A-10 strengthened** | "fail-first" declaration requires C-05 section structurally first; advocacy-first use is a vocabulary collision, now explicitly named with V-02/V-04 as the canonical example |
| 3 | **A-11 — Question-per-criterion mapping** | R5 V-05 pattern: one explicit question/prompt per essential criterion; unanswered prompt = structurally visible missing criterion, not a content gap caught on full read |
| 4 | **A-12 — BRIDGE dual-closure** | R5 bridge-marker pattern: two named bridge artifacts — Q3 closes A-06 (FM→actor), Q4 closes A-09 baseline (FM→trigger); structural guarantee, not output property |
| 5 | **Ceiling 110 → 115** | A-09 exits scoring (−5); A-11 +5; A-12 +5 |

**Key structural note on A-12**: The criterion distinguishes between *output property* (a well-written response happens to contain both chains) and *structural guarantee* (bridge markers are in the template and cannot be omitted without visible damage). Satisfying A-06 and A-09 via prose logic does not pass A-12.

**R6 target**: R5 uniformly failed A-08. The high-potential untested combination is A-08 + A-12 — fail-first numbers the FMs before defeat conditions are written, then BRIDGE dual-closure uses those numbered FMs to close both chains in one named artifact.
 names the specific workaround currently in use (not "a manual process"
but "weekly CSV export to shared drive"), names the role that performs it, and quantifies the
ongoing cost with a unit. "The data-ops team spends 2 hours per week exporting and cleaning CSV
files before pipeline ingestion" passes. "Teams use manual methods" fails on every dimension.

### C-02 — Switching cost quantified

**Pass condition**: Output identifies and quantifies at least two categories of switching cost:
migration effort (time or money, cited to a role), and at least one of: training overhead,
process disruption, or in-flight work at risk. Costs must carry units — "significant" without a
number or unit fails.

### C-03 — Inertia threat score declared

**Pass condition**: Output declares an explicit inertia threat score (HIGH / MEDIUM / LOW) for the
feature. The default is HIGH; any deviation from HIGH must be justified with a quantified
condition. An output that lists switching costs without aggregating them into a threat level has
not completed the analysis.

### C-04 — Defeat conditions identified

**Pass condition**: Output identifies at least two specific, distinct, and testable conditions
under which teams abandon the workaround in favor of the feature. Conditions must be falsifiable
("teams switch when workaround fails to handle files > 10MB" passes; "teams switch when they see
the value" fails). This is the central question of the skill — if it is absent, the output is not
useful.

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

### Baseline (A-01 through A-04, A-09) — expected in all outputs, not scored separately

| ID | Criterion | Category |
|----|-----------|----------|
| A-01 | **Per-section revision gate** | enforcement |
| A-02 | **Column-level structural constraint** | enforcement |
| A-03 | **Composite gate with back-pointers** | enforcement |
| A-04 | **Role precision as continuation gate** | enforcement |
| A-09 | **FM-to-trigger chain citation** | traceability |

A-09 is reclassified from scored to baseline in v6: all five R5 variations passed it without
explicit optimization. An output that fails A-09 is below baseline expectation regardless of
score; it is a structural deficit, not an aspirational miss.

### Scored aspirational (A-05 through A-08, A-10 through A-12) — 5 points each

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| A-05 | **Question-primed entry before table** | enforcement | aspirational |
| A-06 | **Cognitive linkage between adjacent sections** | structure | aspirational |
| A-07 | **ID-referenced synthesis across segments** | structure | aspirational |
| A-08 | **Fail-first ordering** | structure | aspirational |
| A-10 | **Structure declaration with vocabulary enforcement** | auditability | aspirational |
| A-11 | **Question-per-criterion mapping** | auditability | aspirational |
| A-12 | **BRIDGE dual-closure** | traceability | aspirational |

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

### A-09 — FM-to-trigger chain citation *(baseline — expected, not scored)*

**Pass condition**: Each defeat condition (C-04) in the output must name the specific failure mode
(from C-05) that makes switching possible. The chain must be explicit: "teams switch when FM-2
(weekly CSV export silently drops rows above 65k) causes delivery failures" passes; "teams switch
when manual costs become unsustainable" fails. The reference must cite an observable FM symptom,
not a cost-tolerance threshold. Outputs without this citation leave the FM→trigger link implicit —
a reviewer cannot verify that triggers are grounded in failure evidence rather than in the
analyst's prior model of value.

Reclassified to baseline in v6: all five R5 variations passed without explicit optimization. Failing
A-09 is a structural deficit below baseline, not an aspirational miss; it is equivalent to an output
that fails to name roles at all. The citation requirement is now a precondition for golden status,
not a scoring differentiator.

*Source*: R4 pattern; universally satisfied in R5.

### A-10 — Structure declaration with vocabulary enforcement

**Pass condition**: Output opens with a single line declaring which structural techniques are
applied. Acceptable form: "Structure: fail-first | question-primed | bridges | segmented." The
declared techniques must match the actual structure of the output under rubric vocabulary
definitions, not the analyst's local terminology:

- If **"fail-first"** is declared, **Section 1 must be a failure-mode section (C-05)**. Declaring
  "fail-first" to mean "I argue for the status quo before critiquing it" is a vocabulary collision
  that fails A-10. R5 V-02 and V-04 both declared "fail-first" in the advocacy sense while
  placing workaround identity (C-01) first; A-10 flagged both at a glance.
- If **"bridges"** is declared, explicit named transition instructions must appear at section
  boundaries.
- If **"question-primed"** is declared, each critical table must be preceded by a prose-first
  question prompt.

An output with no declaration and correct structure passes all other aspirationals but fails A-10.
An output that declares a technique and fulfills it under rubric vocabulary passes A-10 regardless
of whether other aspirationals are satisfied.

The declaration serves two purposes: (1) it forces the analyst to commit to structural choices
before filling content, making technique-drift detectable by comparing declared against actual;
(2) it allows a reviewer to evaluate aspirational criteria against a stated intent rather than
reconstructing the structure from the text.

*Source*: R4 pattern — five structural combinations distinguishable only on full read. R5 strengthened:
V-02 and V-04 vocabulary collisions on "fail-first" confirmed that the declared technique must be
evaluated against rubric definitions, not the analyst's intent.

### A-11 — Question-per-criterion mapping

**Pass condition**: The output's question or prompt structure maps one-to-one to the essential
criteria. Each essential criterion (C-01 through C-05) corresponds to exactly one explicit
question or prompt in the template; no criterion is satisfied implicitly by a section that
addresses it without naming it. The mapping must be recoverable without reading section content:
a reviewer who sees five explicitly labeled prompts knows that all five essentials have a
corresponding structural slot. An unanswered prompt is a *structurally visible missing criterion*,
detectable before reading the section content; a section that satisfies a criterion without an
explicit prompt produces coverage that is invisible until full review.

The strongest form combines A-11 with A-06: when each question is followed by a bridge instruction
naming which downstream criterion the answer constrains, the Q-per-criterion structure also enforces
the causal chain across sections.

*Source*: R5 V-05 (Q-primed + bridges + roles) — highest-scoring R5 variation. The scorecard
identified "question-per-criterion mapping makes rubric coverage gaps structurally visible — each
question corresponds to an essential criterion; an unanswered question is a visible missing
criterion rather than a content deficit caught only at review."

### A-12 — BRIDGE dual-closure

**Pass condition**: The output contains at least two explicitly named bridge markers — one
establishing the FM-to-actor chain (A-06 direction) and one establishing the FM-to-trigger chain
(A-09 baseline direction) — as named structural artifacts in the template, not as prose summaries
reconstructed from content. Acceptable form:

> **Q3 bridge** — "FM-2 (silent row truncation above 65k) reveals who owns the workaround cost:
> [Data-Ops lead, 2h/week]. Use this actor in Section 4."
>
> **Q4 bridge** — "FM-2 (silent row truncation above 65k) makes the trigger possible: [teams
> switch when delivery SLA breaks]. Enter this as the defeat condition in Section 5."

The Q3 bridge closes A-06 (actor propagation from FM). The Q4 bridge simultaneously satisfies
A-09 baseline (mechanism propagation: FM drives trigger). Together they enforce the full causal
sequence — FM symptom → named actor → quantified cost → FM-grounded trigger — as named structural
elements rather than reviewer-reconstructed inferences.

An output that satisfies A-06 and A-09 via prose logic without named bridge markers does not pass
A-12. The criterion tests whether the dual-chain is a *structural guarantee* (bridges are present
in the template and cannot be omitted without visible structural damage) rather than an *output
property* (a well-written output happens to contain both chains).

*Source*: R5 pattern — "BRIDGE marker as structural artifact closes A-06 and A-09 simultaneously —
Q3 bridge establishes FM-to-actor chain; Q4 bridge establishes FM-to-trigger chain; together they
enforce the full causal sequence without requiring reviewer reconstruction." V-05 earned A-06 via
bridges; A-12 tests whether the bridge markers are explicitly dual-labeled, closing both chains in
one named artifact.

---

## Scoring Reference

| Variation | Essential | Recommended | Aspirational-new | Score | Golden? |
|-----------|-----------|-------------|------------------|-------|---------|
| Perfect | 5/5 = 50 | 3/3 = 30 | 7/7 = 35 | **115** | YES |
| R5 V-05 (v6 scoring) | 5/5 = 50 | 3/3 = 30 | A-06 + A-10 = 10 | **90** | YES |
| R5 V-01, V-03 (v6 scoring) | 5/5 = 50 | 3/3 = 30 | A-10 = 5 | **85** | YES |
| R5 V-02, V-04 (v6 scoring) | 5/5 = 50 | 3/3 = 30 | 0/7 = 0 | **80** | YES — floor |
| Min golden | 5/5 = 50 | 3/3 = 30 | 0/7 = 0 | **80** | YES |
| Recommended gap | 5/5 = 50 | 2/3 = 20 | 0/7 = 0 | **70** | NO |
| Essential only | 5/5 = 50 | 0/3 = 0 | 0/7 = 0 | **50** | NO |

*R5 scores retroactively applied under v6 formula (A-09 exits scoring; A-11/A-12 not yet tested).*

---

## Changes from v5 to v6

| # | Change | Source |
|---|--------|--------|
| 1 | **A-09** reclassified as structural baseline (expected, not scored) | R5 universal pass |
| 2 | **A-10** pass condition strengthened: vocabulary enforcement added — "fail-first" declaration requires C-05 section structurally first | R5 V-02/V-04 vocabulary collision |
| 3 | **A-11** — Question-per-criterion mapping | R5 V-05 pattern |
| 4 | **A-12** — BRIDGE dual-closure | R5 bridge-marker pattern |
| 5 | Score ceiling updated: 110 → 115 (A-09 exits scoring −5; A-11 +5; A-12 +5; net +5) | formula change |

**New aspirational criteria in brief:**

- **A-11**: Template maps one explicit question or prompt to each essential criterion (C-01 through
  C-05). An unanswered prompt is a structurally visible missing criterion detectable before reading
  section content, rather than a coverage gap caught only at review. Strongest when combined with
  A-06 — each question followed by a bridge instruction naming the downstream constraint.

- **A-12**: Two explicitly named bridge markers appear in the template as structural artifacts:
  Q3 bridge (FM → actor, closes A-06 direction) and Q4 bridge (FM → trigger, satisfies A-09
  baseline direction). Dual-labeling the bridges makes the full causal chain — FM symptom → named
  actor → quantified cost → FM-grounded trigger — a structural guarantee rather than an output
  property that happens to be present in well-written responses. An output satisfying A-06 and A-09
  via prose logic without named bridge markers does not pass A-12.

**R6 target combinations**: R5 variations uniformly failed A-08 (fail-first ordering). R6 should
pair A-08 with the new criteria — specifically: A-08 + A-11 (fail-first with Q-per-criterion
mapping) and A-08 + A-12 (fail-first with BRIDGE dual-closure). The A-08 + A-12 combination is the
highest-potential untested structure: fail-first ensures FMs are numbered before defeat conditions
are written; BRIDGE dual-closure uses those numbered FMs to close both the actor chain (A-06) and
the trigger chain (A-09 baseline) in the same named artifact.
