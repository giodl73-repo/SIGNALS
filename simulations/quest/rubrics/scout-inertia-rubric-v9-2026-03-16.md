`scout-inertia-rubric-v9-2026-03-16.md` written. Summary of changes:

**v8 -> v9: two new criteria, ceiling 145 -> 155**

| # | Criterion | Source signal |
|---|-----------|---------------|
| A-19 | **Bidirectional referential integrity enforcement** | Primary key constraint at FM Inventory source (A-16) AND a separately stated rule at the DC table citation point -- both ends guarded. A-19 implies A-16. |
| A-20 | **Inline example co-located with unit-bearing column label** | Format example embedded directly in the column label ("(e.g., 2 hours/week)"), not in a separate rules block -- format reminder lives at the authoring point. Requires A-13 as precondition. |

**Implication chain updated**: A-19 implies A-16 implies A-14 implies A-08. A-20 requires A-13.

**R9 target note**: A-12 still unresolved after R8. V-01's column-level FM->actor/FM->trigger closure demonstrates the scaffold exists but does not satisfy A-12's named-artifact requirement. R9 needs a variation that explicitly names Q3/Q4 bridge artifacts with criterion-chain references over the A-10 + A-13 + A-14 + A-16 + A-19 scaffold.
: one explicit question/prompt per essential criterion; unanswered prompt = structurally visible missing criterion, not a content gap caught on full read |
| 4 | **A-12 -- BRIDGE dual-closure** | R5 bridge-marker pattern: two named bridge artifacts -- Q3 closes A-06 (FM->actor), Q4 closes A-09 baseline (FM->trigger); structural guarantee, not output property |
| 5 | **Ceiling 110 -> 115** | A-09 exits scoring (-5); A-11 +5; A-12 +5 |

## Changes from v6 to v7

| # | Change | Source |
|---|--------|--------|
| 1 | **A-13 -- Tabular column schema structural visibility** | R6 V-02 excellence signal: table columns make criterion gaps visible as blank cells without full-read; prose descriptions cannot satisfy this even if comprehensive |
| 2 | **A-14 -- FM inventory as dedicated named table** | R6 V-02 excellence signal: FM# pre-assignment in a titled table before the defeat condition table enforces A-08 structurally -- FM-[N] identifiers exist as typed references before DC-[N] can cite them |
| 3 | **A-15 -- Trailing completeness checklist** | R6 V-02 excellence signal: per-criterion binary checkboxes at output end convert content gaps into visible unchecked items; distinguishes post-hoc verification (A-15) from per-criterion embedded prompts (A-11) |
| 4 | **Ceiling 115 -> 130** | A-13 +5; A-14 +5; A-15 +5 |

## Changes from v7 to v8

| # | Change | Source |
|---|--------|--------|
| 1 | **A-16 -- FM Inventory primary key constraint declared** | R7 V-02 A-14 PARTIAL: FM Inventory table was titled and ordered correctly but carried no stated rule preventing FM-[N] identifiers from appearing downstream without prior row assignment; the constraint must be written in the template body to enforce referential integrity structurally |
| 2 | **A-17 -- Question-per-criterion full coverage (all 5 essentials)** | R7 V-03 A-11 PARTIAL: embedded SELF-CHECK covered C-05, C-02, C-04 but omitted explicit questions for C-01 and C-03; full coverage requires one named question per each of the five essential criteria -- any gap leaves a criterion without structural enforcement during authoring |
| 3 | **A-18 -- Trailing checklist binary format and full coverage** | R7 V-03 A-15 PARTIAL: SELF-CHECK was trailing and verification-oriented but used essay prompts ("answer with one sentence") and covered only 3 of 5 essential criteria; A-18 requires binary checkboxes (Y/N or checkbox) and complete mapping of all five essential criteria -- essay format and partial coverage both fail |
| 4 | **Ceiling 130 -> 145** | A-16 +5; A-17 +5; A-18 +5 |

## Changes from v8 to v9

| # | Change | Source |
|---|--------|--------|
| 1 | **A-19 -- Bidirectional referential integrity enforcement** | R8 V-01 excellence signal: primary key constraint stated at FM Inventory source point (A-16) AND reinforced as a separate named rule at the DC table citation point; A-16 captures only the source end; an author violating the constraint at either end sees a named rule -- source enforcement alone leaves the citation point unguarded |
| 2 | **A-20 -- Inline example co-located with unit-bearing column label** | R8 V-01 excellence signal: unit-bearing column labels (e.g., "Ongoing cost with unit") embed a concrete format example directly in the label definition ("(e.g., 2 hours/week)"), structurally co-located with the cell that must be filled; prior criteria require that units are present -- A-20 requires that the format reminder lives at the authoring point, not in a separate prose block |
| 3 | **Ceiling 145 -> 155** | A-19 +5; A-20 +5 |

**Key structural note on A-14 vs A-16**: A-14 requires the FM Inventory to be a dedicated named table whose first column assigns FM-[N] identifiers, positioned before the Defeat Conditions table. A-16 requires that table to additionally carry an explicit stated constraint -- visible in the template body -- that no FM-[N] may appear in the DC table without prior assignment here. A-16 implies A-14; A-14 does not imply A-16.

**Key structural note on A-16 vs A-19**: A-16 requires the primary key constraint to be stated at the FM Inventory source point. A-19 requires the enforcement to appear at both ends of the identifier chain -- source AND citation point. A template satisfying A-16 does not pass A-19 unless the constraint also appears as a named rule at the DC table. A-19 implies A-16; A-16 does not imply A-19.

**Key structural note on A-11 vs A-17**: A-11 requires at least one embedded question per essential criterion to make unanswered prompts visible during authoring. A-17 requires complete coverage -- all five essential criteria (C-01 through C-05) each have a named, criterion-labeled question. An output that embeds questions for three criteria passes A-11 at PARTIAL and fails A-17. Full A-11 and A-17 can be satisfied by the same question set if and only if all five are present.

**Key structural note on A-15 vs A-18**: A-15 requires a trailing named section with per-criterion verification items. A-18 requires that section to use binary observable format (checkbox or Y/N per item, not a prose prompt) and to cover all five essential criteria. An output with a trailing SELF-CHECK using essay prompts scores A-15 PARTIAL and fails A-18 entirely. A-18 implies A-15; A-15 does not imply A-18.

**Key structural note on A-13 vs A-20**: A-13 requires that all major sections use column schemas so that blank cells expose criterion gaps. A-20 requires that unit-bearing columns additionally embed a concrete format example in the label itself. A-13 PASS does not imply A-20; a table with a column labeled "Cost" satisfies A-13 but fails A-20. A-20 strengthens the format prompt without changing the structural visibility requirement.

**R9 target**: A-12 (BRIDGE dual-closure) has never passed across R5-R8. R8 V-01 demonstrated that A-10 + A-13 + A-14 + A-16 provide the structural scaffold but column-level FM->actor and FM->trigger closure does not satisfy A-12's named-artifact requirement. The untested combination for R9 is A-10 + A-13 + A-14 + A-16 + A-19 + A-12 -- bidirectional integrity enforcement (A-19) closes the referential scaffold at both ends, and a variation that explicitly names Q3/Q4 bridge artifacts with criterion-chain references over that scaffold is the remaining structural move for A-12.

---

## Essential Criteria

*All five must pass. Any essential failure caps the output as non-useful regardless of advanced scores.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-01 | **Workaround named specifically** | specificity | essential |
| C-02 | **Switching cost quantified** | quantification | essential |
| C-03 | **Inertia threat score declared** | assessment | essential |
| C-04 | **Defeat conditions identified** | analysis | essential |
| C-05 | **Workaround failure modes identified** | analysis | essential |

### C-01 -- Workaround named specifically

**Pass condition**: Output names the specific workaround currently in use (not "a manual process" but "weekly CSV export to shared drive"), names the role that performs it, and quantifies the ongoing cost with a unit. "The data-ops team spends 2 hours per week exporting and cleaning CSV files before pipeline ingestion" passes. "Teams use manual methods" fails on every dimension.

### C-02 -- Switching cost quantified

**Pass condition**: Output identifies and quantifies at least two categories of switching cost: migration effort (time or money, cited to a role), and at least one of: training overhead, process disruption, or in-flight work at risk. Costs must carry units -- "significant" without a number or unit fails.

### C-03 -- Inertia threat score declared

**Pass condition**: Output declares an explicit inertia threat score (HIGH / MEDIUM / LOW) for the feature. The default is HIGH; any deviation from HIGH must be justified with a quantified condition. An output that lists switching costs without aggregating them into a threat level has not completed the analysis.

### C-04 -- Defeat conditions identified

**Pass condition**: Output identifies at least two specific, distinct, and testable conditions under which teams abandon the workaround in favor of the feature. Conditions must be falsifiable ("teams switch when workaround fails to handle files > 10MB" passes; "teams switch when they see the value" fails). This is the central question of the skill -- if it is absent, the output is not useful.

### C-05 -- Workaround failure modes identified

**Pass condition**: Output identifies at least two specific scenarios where the current workaround breaks, produces errors, causes re-work, or cannot scale. These are the observable cracks in the inertia armor. Generic pain points ("manual is slow") do not pass; concrete failure modes ("CSV export silently truncates rows over 65,536 -- no error message") pass.

---

## Recommended Criteria

*Strong outputs satisfy all three. Missing one is a quality signal, not a blocker.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| R-01 | **Trigger scoped to team type** | precision | recommended |
| R-02 | **Role-level precision** | precision | recommended |
| R-03 | **At least one cost cited to role** | depth | recommended |

### R-01 -- Trigger scoped to team type

**Pass condition**: Defeat conditions (from C-04) name a specific team type or segment rather than applying uniformly to all users. "Engineering teams switch when..." or "PMs in regulated industries switch when..." passes. "Users switch when..." fails. Different team types face different inertia profiles; a trigger that ignores team type is underspecified.

### R-02 -- Role-level precision

**Pass condition**: Output names specific roles (not "users" or "the team") when attributing failure modes and switching costs. At minimum, the role that owns the workaround (from C-01) appears again when listing failure modes (C-05) and switching costs (C-02).

### R-03 -- At least one cost cited to role

**Pass condition**: At least one switching cost category is explicitly attributed to the role bearing it. "3 days of migration effort for the data-ops team" passes. "3 days of migration effort" without a role attribution fails.

---

## Advanced Criteria

*Structural excellence markers. Each requires a named structural element in the template -- not an output property.*

| ID | Criterion | Category | Points |
|----|-----------|----------|--------|
| A-08 | **FM before DC** | ordering | 5 |
| A-10 | **Fail-first declaration** | ordering | 5 |
| A-11 | **Question-per-criterion mapping** | completeness | 5 |
| A-12 | **BRIDGE dual-closure** | closure | 5 |
| A-13 | **Tabular column schema structural visibility** | format | 5 |
| A-14 | **FM inventory as dedicated named table** | format | 5 |
| A-15 | **Trailing completeness checklist** | verification | 5 |
| A-16 | **FM Inventory primary key constraint declared** | integrity | 5 |
| A-17 | **Question-per-criterion full coverage (all 5 essentials)** | completeness | 5 |
| A-18 | **Trailing checklist binary format and full coverage** | verification | 5 |
| A-19 | **Bidirectional referential integrity enforcement** | integrity | 5 |
| A-20 | **Inline example co-located with unit-bearing column label** | format | 5 |

### A-08 -- FM before DC

**Pass condition**: The template enforces positional ordering such that failure modes (C-05) are authored before defeat conditions (C-04). Role ordering, section numbering, or table sequence all satisfy this -- the mechanism is irrelevant as long as an author following the template cannot write DC rows before FM rows.

### A-10 -- Fail-first declaration

**Pass condition**: The template carries an explicit structural label -- "FAIL-FIRST DECLARATION" or equivalent -- as the first named section or block, followed by a one-sentence statement of why failure modes are enumerated before costs and defeat conditions. The label must be a structural element, not a comment or instruction note. Templates where FM content appears first via role ordering without an explicit declaration do not pass; the label is the criterion, not the ordering alone.

### A-11 -- Question-per-criterion mapping

**Pass condition**: The template body contains at least one explicitly labeled question or prompt per essential criterion such that an unanswered prompt is a visible gap during authoring rather than a content gap caught only on full read. Three or more criteria covered qualifies for PARTIAL; all five covered satisfies A-17, not A-11 alone. A-11 PASS requires coverage of at least three essential criteria with named prompts.

### A-12 -- BRIDGE dual-closure

**Pass condition**: The template names two distinct bridge artifacts -- Q3 (or equivalent) closing the FM->actor chain from C-05 to R-02, and Q4 (or equivalent) closing the FM->trigger chain from C-05 to C-04. Each artifact must be named in the template body with an explicit reference to the criterion chain it closes. Column-level closure (FM->actor and FM->trigger as required columns) does not satisfy A-12; the named artifacts and their chain references are the criterion.

### A-13 -- Tabular column schema structural visibility

**Pass condition**: All major output sections use named column schemas such that a blank cell is a visible criterion gap without requiring a full read of prose. At minimum, the FM section and the DC section must be tables with named columns. An output where criterion gaps require reading complete prose to detect fails A-13 regardless of content quality.

### A-14 -- FM inventory as dedicated named table

**Pass condition**: The template contains a titled FM Inventory table (name visible in the output) whose first column assigns FM-[N] identifiers. This table must appear before the Defeat Conditions table in template structure. FM enumerated only in prose blocks, or FM column in a mixed table not dedicated to inventory, does not pass. A-14 implies A-08.

### A-15 -- Trailing completeness checklist

**Pass condition**: The template contains a named trailing section positioned after all content sections, with one verification item per essential criterion. Items may be prose prompts, essay questions, or binary checkboxes -- format is not a criterion here (see A-18). The section must be structurally last and criterion-labeled. A SELF-CHECK block mid-template does not pass; position is the criterion.

### A-16 -- FM Inventory primary key constraint declared

**Pass condition**: The FM Inventory table (from A-14) carries an explicitly stated rule, written in the template body (not in a comment or instructions section), that no FM-[N] identifier may appear in the Defeat Conditions table without a corresponding row in the FM Inventory. The rule must be visible to an author using the template. Templates where the constraint is implied by ordering but not stated fail A-16. A-16 implies A-14.

### A-17 -- Question-per-criterion full coverage (all 5 essentials)

**Pass condition**: The template body contains one explicitly labeled question or prompt for each of the five essential criteria -- C-01, C-02, C-03, C-04, and C-05 -- such that an unanswered prompt for any criterion is a visible gap during authoring. Coverage of fewer than all five fails A-17 regardless of A-11 result. A-17 implies A-11 PASS.

### A-18 -- Trailing checklist binary format and full coverage

**Pass condition**: The trailing checklist (from A-15) satisfies two independent conditions: (1) each item uses binary observable format -- checkbox or Y/N -- not an essay prompt or open-ended question; and (2) all five essential criteria are mapped, one item each, with no essential criterion absent. Failure on either condition is a full fail. A-15 PARTIAL with essay prompts and 3/5 coverage fails A-18 on both dimensions. A-18 implies A-15 PASS.

### A-19 -- Bidirectional referential integrity enforcement

**Pass condition**: The template enforces the FM-[N] referential integrity rule at both ends of the identifier chain: (1) the source constraint at the FM Inventory (from A-16 -- no FM-[N] may appear downstream without prior row assignment), AND (2) a separately stated referential integrity rule at the DC table definition point, explicitly requiring that every FM-[N] cited in the DC table must have a prior assigned row in the FM Inventory. Both rules must be visible in the template body. A template satisfying A-16 alone passes only the source end; A-19 requires the citation-point rule to be present as a named, separate statement. A-19 implies A-16.

### A-20 -- Inline example co-located with unit-bearing column label

**Pass condition**: Every column label that requires a unit-bearing value (e.g., "Ongoing cost", "Migration effort", "Training overhead") embeds a concrete format example directly within the label definition -- "(e.g., 2 hours/week)", "(e.g., $4,000)", "(e.g., 3 days)" -- such that the format reminder is structurally co-located with the cell the author must fill. A separate "Rules" or "Instructions" block stating that units are required does not satisfy A-20; the example must live in the label. A-20 requires A-13 (tabular format) as a precondition but does not imply it -- A-20 adds the co-location constraint on top of structural visibility.
