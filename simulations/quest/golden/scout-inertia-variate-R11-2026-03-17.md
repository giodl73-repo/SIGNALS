# scout-inertia -- Quest Variate R11

**Rubric**: v11 (ceiling 180 = 100 essential base + 16 advanced criteria x 5 pts)
**Date**: 2026-03-17
**Previous round**: R10 V-02 and V-05 predicted 180/180 (A-23+A-24+A-25 all present)
**R11 target**: Confirmed first 180/180 across varied structural framings
**New criteria**: A-23 (criterion IDs in rule labels) + A-24 (dual-type threshold examples) + A-25 (active command directive on bridge gate)

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle emphasis | Stage-based; A-23 bracket-prefix on both rules; A-25 via `[BRIDGE COMPLETION COMMAND]` as directive inside BRIDGE COMPLETION STATUS sub-section |
| V-02 | Phrasing register | COMMAND phrasing; A-23 bracket-suffix form `RULE NAME [A-XX]`; A-25 via `[BRIDGE COMPLETION COMMAND]` all-caps directive before Y/N table |
| V-03 | Inertia framing | Status-quo competitor framing; A-23 domain-prefixed bracket-suffix `STATUS QUO RULE [A-XX]`; A-25 via `[ACTION REQUIRED: COMPLETE BRIDGE BEFORE PROCEEDING]` named block |
| V-04 | Output format | Consolidated triple-block bridge with remediation column; A-23 bracket-prefix; A-25 via `[BRIDGE COMPLETION COMMAND]` as sub-section heading on BRIDGE GATE VERDICT |
| V-05 | All axes | COMMAND phrasing + inertia framing + bracket-prefix A-23 + dual-type A-24 + `[BRIDGE COMPLETION COMMAND]` A-25; minimal extension of R10 V-05 to satisfy all three simultaneously |

---

## R11 Design Notes

### A-23 mechanism -- four forms tested

A-23 requires the criterion ID in the rule label text. The form is flexible -- bracket prefix, bracket suffix, domain-prefixed suffix all satisfy the criterion as long as the ID appears in the label itself. R11 tests four forms across five variations:

1. **Bracket-prefix** (V-01, V-04, V-05): `[A-16 PRIMARY KEY RULE]`, `[A-19 REFERENTIAL INTEGRITY RULE]`
2. **Bracket-suffix** (V-02): `PRIMARY KEY RULE [A-16]`, `CITATION INTEGRITY RULE [A-19]`
3. **Domain-prefixed bracket-suffix** (V-03): `STATUS QUO LOCK RULE [A-16]`, `STATUS QUO CITATION RULE [A-19]`
4. **Bracket-prefix variant label** (V-04): `[A-16 PRIMARY KEY CONSTRAINT]`, `[A-19 CITATION INTEGRITY CONSTRAINT]`

All four forms satisfy A-23 if the rubric scoring reads the criterion ID in the label regardless of surrounding words. The domain-prefix form in V-03 is the stress test -- the rule label is less conventional but the ID is unambiguous.

### A-24 mechanism -- confirmed pass from R10

All five variations use `(e.g., >10MB, >3 failures/week)` in the DC threshold column label. This was already present in R10 V-01/V-02/V-03. R11 carries it forward; scoring will confirm A-24 was passing in R10 and continues to pass here.

### A-25 mechanism -- four implementation forms

A-25 requires a named structural element (command directive) co-located with the Y/N bridge gate table. Four forms tested:

1. **Inline bracket-label + instruction** (V-01, V-05): `[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before...` as first element in gate block
2. **All-caps bracket-label** (V-02): `[BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE...`
3. **Action-phrase label** (V-03): `[ACTION REQUIRED: COMPLETE BRIDGE BEFORE PROCEEDING]:` as named block
4. **Sub-section heading** (V-04): `### [BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE STAGE 3` as heading above verdict table

The sub-section heading form in V-04 is the structural stress test -- the directive is the section title itself rather than a separate element within the section. A-25 requires the command to be "co-located with the status table at the gate position" -- the heading is co-located (immediately above the table) and is a named structural element.

### R10 state going into R11

From R10 scoring (predicted):
- V-02: A-23 PASS (`[A-16 PRIMARY KEY RULE]` + `[A-19 CITATION INTEGRITY RULE]`), A-24 PASS, A-25 PASS (`[BRIDGE COMPLETION COMMAND]`) -- 180/180
- V-05: A-23 PASS, A-24 PASS, A-25 PASS -- 180/180
- V-03: A-23 PASS (`PRIMARY KEY CONSTRAINT [A-16]` + `REFERENTIAL INTEGRITY RULE (citation point) [A-19]`), A-24 PASS, A-25 FAIL (gate was passive framing, no command label) -- 175/180
- V-04: A-23 PASS, A-24 PASS, A-25 FAIL (BRIDGE GATE VERDICT had no command label) -- 175/180
- V-01: A-23 FAIL (no criterion IDs in rule labels), A-24 PASS, A-25 FAIL -- 155/180

R11 fixes each deficit. All five R11 variations are predicted 180/180.

---

## V-01 -- Lifecycle emphasis axis

**Axis**: Stage-based lifecycle; A-23 adds criterion IDs to both integrity rules in bracket-prefix form; A-25 adds `[BRIDGE COMPLETION COMMAND]` directive to the BRIDGE COMPLETION STATUS sub-section within Stage 2.
**Hypothesis**: Stage-boundary enforcement (Stage 2 gate before Stage 3 opens) combined with an explicit command directive at the gate produces A-22 and A-25 simultaneously. Bracket-prefix form for A-23 is the most readable form -- ID leads the label. A-24 passes via `>10MB, >3 failures/week` in DC threshold column.
**Predicted score**: 180/180

---

```
## FAIL-FIRST DECLARATION

The current workaround is this feature's primary competitor. Defeat conditions and switching cost
thresholds can only be derived from documented workaround failures. Populate Stage 1 before any
other stage is authored.

Authoring sequence:
- Stage 1 -- FAILURE MODE INVENTORY (C-05): where the workaround breaks
- Stage 2 -- BRIDGE STAGE: Q3 (FM->actor, closes C-05 -> R-02) + Q4 (FM->trigger, closes C-05 -> C-04) + completion gate
- Stage 3 -- WORKAROUND PROFILE (C-01): specific tool, role, ongoing cost
- Stage 4 -- SWITCHING COST (C-02): quantified cost to abandon the workaround
- Stage 5A -- THREAT ASSESSMENT (C-03): inertia threat score
- Stage 5B -- DEFEAT CONDITIONS (C-04): conditions under which the workaround loses
- Stage 6 -- COMPLETENESS CHECK

This is the structural foundation. The Stage 2 gate must show Y for both artifacts before Stage 3
is authored.

---

## STAGE 1 -- FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround fail, produce errors, cause
> rework, or hit a scale ceiling? Name the exact failure mode -- not "it's slow." Minimum 2 rows
> required. "Manual is slow" fails; "CSV export silently truncates rows above 65,536 with no
> error message" passes.

> **[A-16 PRIMARY KEY RULE]**: No FM-[N] identifier may appear in any later section of this
> document unless it has an assigned row in this table. Assign identifiers here first.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger condition (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|---------------------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                                       |                             |
| FM-2   |                                                                                       |                                    |                                       |                             |

---

## STAGE 2 -- BRIDGE STAGE

### Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

Map each failure mode to the specific role experiencing it. This bridge closes the chain from
failure documentation to role attribution required by R-02.

| FM-[N] | Actor / role experiencing this failure (e.g., data-ops team) | Role-level consequence |
|--------|--------------------------------------------------------------|------------------------|
| FM-1   |                                                              |                        |
| FM-2   |                                                              |                        |

### Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

Map each failure mode to its triggering condition and measurable threshold. This bridge closes
the chain from failure documentation to defeat condition construction required by C-04.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

### BRIDGE COMPLETION STATUS

[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding to Stage 3. Do not author
Stages 3 through 5B unless both rows below show Y.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

If either is N: return to Stage 1. Complete the artifact before continuing.

---

## STAGE 3 -- WORKAROUND PROFILE

> **C-01 question**: What is the exact name of the workaround -- the specific tool, file type,
> or procedure name? Not "a manual process." Who performs it? What is the ongoing cost per week
> or sprint, with a unit?

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## STAGE 4 -- SWITCHING COST

> **C-02 question**: What does it cost to abandon this workaround and adopt the feature? Identify
> at least two cost categories. Every estimate must carry a number and a unit -- "significant"
> fails C-02.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

> **C-03 question**: What is the inertia threat score for this feature? Default is HIGH.
> Deviations from HIGH must be justified with a specific, quantified condition -- a qualitative
> judgment does not justify deviation.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## STAGE 5B -- DEFEAT CONDITIONS

> **C-04 question**: Under what specific, testable conditions do teams abandon this workaround
> in favor of the feature? Each condition must be falsifiable. "Teams switch when they see the
> value" fails. Each row must cite an FM-[N] from Stage 1.

> **[A-19 REFERENTIAL INTEGRITY RULE]**: Every FM-[N] cited in this table must have a
> corresponding assigned row in the FM Inventory (Stage 1). Do not reference FM identifiers
> not assigned in Stage 1. Verify before filling each row.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type or segment |
|--------|------------------------------------------|-------------------|------------------------------------------------------|----------------------|
| DC-1   |                                          |                   |                                                      |                      |
| DC-2   |                                          |                   |                                                      |                      |

---

## STAGE 6 -- COMPLETENESS CHECK

| Criterion                                                                                      | Check (Y / N) |
|------------------------------------------------------------------------------------------------|---------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                 |               |
| C-02: At least two switching cost categories quantified with numbers and units                 |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition) |               |
| C-04: At least two defeat conditions identified, each falsifiable, each citing FM-[N]          |               |
| C-05: At least two failure modes identified, each specific and non-generic                     |               |
```

---

## V-02 -- Phrasing register axis

**Axis**: Imperative COMMAND phrasing throughout; A-23 bracket-suffix form (`RULE NAME [A-XX]`) so the rule name leads and the ID trails; A-25 via all-caps `[BRIDGE COMPLETION COMMAND]` directive.
**Hypothesis**: Bracket-suffix form leaves the rule name semantically first and the criterion ID as a traceability annotation. This is the natural reading order: "what rule is this?" -- then "which criterion?" The all-caps command body (`COMPLETE Q3 AND Q4 BEFORE AUTHORING...`) is unambiguous about what the author must do. A-23 pass is form-independent; scoring confirms bracket-suffix is as valid as bracket-prefix.
**Predicted score**: 180/180

---

```
## FAIL-FIRST DECLARATION

[FAIL-FIRST RULE]: Enumerate failure modes before switching costs or defeat conditions. Every DC
row must trace to a documented FM row. The workaround's failure is the only structural evidence
that inertia can be beaten.

Bridge artifacts -- both required before Defeat Conditions are authored:
- Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02): maps each FM-[N] to the role experiencing it
- Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04): maps each FM-[N] to its triggering condition

---

## SECTION 1 -- FAILURE MODE INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the current workaround breaks, produces
errors, causes rework, or hits a scale ceiling. ASSIGN an FM-[N] identifier to each row.
MINIMUM 2 rows. REJECT any generic description -- "slow" or "manual" alone fails;
"CSV export silently truncates rows at 65,536 with no error message" passes.

> **PRIMARY KEY RULE [A-16]**: ASSIGN all FM-[N] identifiers in this table first. NO FM-[N]
> reference may appear in any later section of this document without a corresponding row
> assigned in this table.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

[BRIDGE Q3 COMMAND]: MAP each FM-[N] to the specific role experiencing the failure.
VERIFY each actor name is a specific role title, not "users" or "the team."

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

---

## Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

[BRIDGE Q4 COMMAND]: MAP each FM-[N] to its triggering condition. QUANTIFY the measurable
threshold that activates the failure.

| FM-[N] | Triggering condition | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|---------------------|------------------------------------------------------|
| FM-1   |                     |                                                      |
| FM-2   |                     |                                                      |

---

## BRIDGE COMPLETION GATE

[BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE AUTHORING SECTION 2 THROUGH SECTION 5.
If either row is N, DO NOT PROCEED. Return to Section 1.

| Artifact                                       | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

---

## SECTION 2 -- WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific workaround -- the exact tool name, file type, or procedure.
NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost with a number
and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 3 -- SWITCHING COST

[C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a number
and a unit. NAME the role bearing each cost.

> **[UNIT RULE]**: EVERY estimate must carry a number and a unit. "Significant" or "substantial"
> without a number is REJECTED.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 4 -- THREAT ASSESSMENT

[C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH. IF deviating from HIGH,
STATE a specific quantified condition -- a qualitative judgment ("low friction") is REJECTED
as justification.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4 trigger
mapping above. CITE the FM-[N] driving each. "Teams switch when they see the value" fails --
every DC row must name a testable condition.

> **CITATION INTEGRITY RULE [A-19]**: EVERY FM-[N] cited in this table MUST have an assigned
> row in Section 1 (FM Inventory). DO NOT introduce FM references not assigned above.
> VERIFY before filling each row.

| DC-[N] | Defeat condition (falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type |
|--------|-------------------------------|-------------------|------------------------------------------------------|-----------|
| DC-1   |                               |                   |                                                      |           |
| DC-2   |                               |                   |                                                      |           |

---

## COMPLETENESS CHECK

| Criterion                                                                                      | Check (Y / N) |
|------------------------------------------------------------------------------------------------|---------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                 |               |
| C-02: At least two switching cost categories, each with number and unit                        |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition) |               |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Section 1     |               |
| C-05: At least two specific, non-generic failure modes in Section 1                           |               |
```

---

## V-03 -- Inertia framing axis

**Axis**: Status-quo competitor framing throughout section names; A-23 domain-prefixed bracket-suffix (`STATUS QUO LOCK RULE [A-16]`, `STATUS QUO CITATION RULE [A-19]`); A-25 via `[ACTION REQUIRED: COMPLETE BRIDGE BEFORE PROCEEDING]` named block heading.
**Hypothesis**: Domain-prefixed rule labels reinforce the inertia framing while still carrying criterion IDs -- the label reads as domain language first (status quo analysis) and rubric traceability second. A-23 pass is form-independent so the domain prefix does not disqualify the ID. The `[ACTION REQUIRED:]` label form for A-25 is a different surface than `[BRIDGE COMPLETION COMMAND]` but satisfies the same structural requirement -- a named element co-located with the Y/N table.
**Predicted score**: 180/180

---

```
## FAIL-FIRST DECLARATION -- THE UNNAMED COMPETITOR

Every feature competes against an unnamed competitor: the current workaround. This competitor
has no demo, no pricing page, and no sales team. It wins by default unless teams have a
specific, observable reason to leave. This analysis names the unnamed competitor and answers:
why does the status quo lose?

Start with where the status quo breaks. Nothing else is worth analyzing until its failure
modes are documented.

Bridge artifacts -- required before defeat conditions are authored:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): which roles experience each failure
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): what specific conditions cause each failure

---

## SECTION 1 -- THE STATUS QUO'S VULNERABILITIES: FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround fail, produce errors, cause
> rework, or hit a scale ceiling? These are the status quo's weaknesses. Name each failure
> precisely -- not "it's slow." Minimum 2 rows.

> **STATUS QUO LOCK RULE [A-16]**: Assign all FM-[N] identifiers in this table first.
> No FM-[N] may appear in any later section without a corresponding row assigned here.
> Every downstream reference must trace back to a row in this table.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Who experiences it (e.g., data-ops team) | What triggers it (e.g., file > 10MB) | How often (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------------|---------------------------------------|-----------------------------|
| FM-1   |                                                                                       |                                          |                                       |                             |
| FM-2   |                                                                                       |                                          |                                       |                             |

---

## Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

Map each failure mode to the specific role experiencing it.

| FM-[N] | Role experiencing the failure (e.g., data-ops team) | Impact on that role |
|--------|-----------------------------------------------------|---------------------|
| FM-1   |                                                     |                     |
| FM-2   |                                                     |                     |

---

## Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

Map each failure mode to its triggering condition and measurable threshold.

| FM-[N] | Triggering condition | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|---------------------|------------------------------------------------------|
| FM-1   |                     |                                                      |
| FM-2   |                     |                                                      |

---

## BRIDGE COMPLETION GATE -- READY TO PROCEED?

[ACTION REQUIRED: COMPLETE BRIDGE BEFORE PROCEEDING]: Both Q3 and Q4 must be populated before
the status quo profile and defeat conditions are authored. An incomplete bridge means defeat
conditions lack their actor and trigger chains. An N in either row is a stop signal -- return
to Section 1 and complete the missing artifact.

| Artifact                                       | Complete? (Y / N) |
|------------------------------------------------|-------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                   |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                   |

---

## SECTION 2 -- HOW THE STATUS QUO PERSISTS: WORKAROUND PROFILE

> **C-01 question**: What exactly is the current workaround? Name the specific tool, file
> format, or procedure -- not "a manual process." Who performs it? What is its ongoing cost
> per week or per sprint, with a number and unit?

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Time in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|--------------------------------------|
|                                                          |                    |                                   |                                      |

---

## SECTION 3 -- THE COST OF DEFECTING: SWITCHING ANALYSIS

> **C-02 question**: What would it cost a team to abandon this workaround? Identify at least
> two cost categories. Every estimate must have a number and a unit.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 4 -- HOW STRONG IS THE STATUS QUO: THREAT RATING

> **C-03 question**: How strong is the unnamed competitor? Score it. Default threat score
> is HIGH -- the status quo always has home-field advantage. Deviations from HIGH require
> a specific quantified condition, not a qualitative judgment.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- WHEN THE STATUS QUO LOSES: DEFEAT CONDITIONS

> **C-04 question**: Under what specific, observable conditions does a team switch from the
> workaround to this feature? Derive each condition from the triggers in Q4. Every condition
> must be falsifiable -- "teams switch when they see the value" fails.

> **STATUS QUO CITATION RULE [A-19]**: Every FM-[N] cited in this table must have an assigned
> row in Section 1. No FM identifier may be introduced here without prior assignment in
> Section 1. Verify before filling each row.

| DC-[N] | Defeat condition (falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team segment |
|--------|-------------------------------|-------------------|------------------------------------------------------|--------------|
| DC-1   |                               |                   |                                                      |              |
| DC-2   |                               |                   |                                                      |              |

---

## SECTION 6 -- COMPLETENESS VERIFICATION

| Criterion                                                                                      | Satisfied? (Y / N) |
|------------------------------------------------------------------------------------------------|--------------------|
| C-01: Workaround named specifically, with role, with cost in number + unit                     |                    |
| C-02: At least two switching cost categories, each quantified with number + unit               |                    |
| C-03: Inertia threat score declared; if not HIGH, a quantified justification is given          |                    |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Section 1     |                    |
| C-05: At least two specific failure modes in Section 1, each non-generic                      |                    |
```

---

## V-04 -- Output format axis

**Axis**: Consolidated triple-block bridge (Q3 table, Q4 table, BRIDGE GATE VERDICT table with remediation column) all within a single Stage 2; A-23 bracket-prefix; A-25 via `[BRIDGE COMPLETION COMMAND]` as the sub-section heading on the BRIDGE GATE VERDICT block.
**Hypothesis**: The sub-section heading form for A-25 is the most structural implementation -- the directive is the section title itself, not a separate prose element within the section. The heading is co-located with the verdict table by definition (it names the section the table belongs to). The remediation column in the verdict table converts the gate from binary status check to prescriptive action plan. V-04 tests whether the heading-as-directive form satisfies A-25's "named structural element" requirement.
**Predicted score**: 180/180

---

```
## FAIL-FIRST DECLARATION

Enumerate failure modes before switching costs or defeat conditions. Defeat conditions cannot
be derived without documented failures. Switching cost thresholds cannot be calibrated without
knowing where the workaround breaks.

Bridge artifacts required before Stage 5B:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps FM-[N] to the actor experiencing each failure
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps FM-[N] to the triggering condition of each failure

Authoring order is enforced by stage structure. Stage 1 before Stage 2. Stage 2 gate before Stage 3.

---

## STAGE 1 -- FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround fail, produce errors, cause
> rework, or hit a scale ceiling? Name the exact failure mode -- not "it's slow." Minimum 2 rows.
> "Manual is slow" fails; "CSV export silently truncates rows above 65,536 with no error message"
> passes.

> **[A-16 PRIMARY KEY CONSTRAINT]**: Assign all FM-[N] identifiers in this table first. No FM-[N]
> identifier may appear in the Defeat Conditions table (Stage 5B) or any other downstream section
> without a corresponding row assigned here.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## STAGE 2 -- BRIDGE STAGE

### Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact on that actor |
|--------|------------------------------------|----------------------------------|
| FM-1   |                                    |                                  |
| FM-2   |                                    |                                  |

### Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

| FM-[N] | Triggering condition | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|---------------------|------------------------------------------------------|
| FM-1   |                     |                                                      |
| FM-2   |                     |                                                      |

### [BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE STAGE 3

| Artifact                                       | Populated? (Y / N) | If N: action required                          |
|------------------------------------------------|--------------------|------------------------------------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    | Return to Stage 1 and complete actor mapping   |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    | Return to Stage 1 and complete trigger mapping |

Do not proceed to Stage 3 unless both rows show Y.

---

## STAGE 3 -- WORKAROUND PROFILE

> **C-01 question**: What is the exact name of the workaround -- the specific tool, file type,
> or procedure name? Not "a manual process." Who performs it? What is the ongoing cost per week
> or sprint, with a unit?

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## STAGE 4 -- SWITCHING COST

> **C-02 question**: What does it cost to abandon this workaround and adopt the feature? Identify
> at least two cost categories. Every estimate must carry a number and a unit -- "significant"
> fails C-02.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

> **C-03 question**: What is the inertia threat score? Default is HIGH. Deviations from HIGH
> must be justified with a specific quantified condition -- a qualitative statement does not
> justify deviation.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## STAGE 5B -- DEFEAT CONDITIONS

> **C-04 question**: Under what specific, testable conditions do teams abandon this workaround
> in favor of the feature? Each condition must be falsifiable -- derive it from Q4 triggers.
> Cite the FM-[N] driving each defeat condition.

> **[A-19 CITATION INTEGRITY CONSTRAINT]**: Every FM-[N] cited in this table must have an assigned
> row in the FM Inventory (Stage 1). Do not reference FM identifiers not assigned in Stage 1.
> Verify before filling each row.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type |
|--------|------------------------------------------|-------------------|------------------------------------------------------|-----------|
| DC-1   |                                          |                   |                                                      |           |
| DC-2   |                                          |                   |                                                      |           |

---

## STAGE 6 -- COMPLETENESS CHECK

| Criterion                                                                                      | Check (Y / N) |
|------------------------------------------------------------------------------------------------|---------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                 |               |
| C-02: At least two switching cost categories quantified with number and unit                   |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition) |               |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Stage 1       |               |
| C-05: At least two specific, non-generic failure modes in Stage 1                             |               |
```

---

## V-05 -- All axes combined

**Axis**: COMMAND phrasing + inertia framing in FAIL-FIRST + bracket-prefix A-23 on both rules + dual-type A-24 threshold + `[BRIDGE COMPLETION COMMAND]` A-25 directive; extends R10 V-05 by fixing the one gap (R10 V-05 already passed A-23, A-24, A-25 -- V-05 R11 confirms all three are co-present with the combined-axes scaffold).
**Hypothesis**: The combined-axes variation is the highest structural density test. COMMAND phrasing, inertia framing, criterion IDs in rule labels, dual-type threshold examples, and explicit bridge command gate all fire simultaneously. No interference between them is expected. V-05 R11 is the R10 V-05 confirmation run with explicit A-23/A-25 signal verification.
**Predicted score**: 180/180

---

```
## [FAIL-FIRST DECLARATION] -- THE UNNAMED COMPETITOR

The status quo is this feature's primary competitor. It has no name, no vendor, and no
champion. It wins by default. This analysis answers: where does the status quo break,
and why does it lose?

Enumerate failure modes first. Every DC row derives from a documented FM row. The workaround's
failure modes are the only structural evidence that inertia can be beaten.

Bridge artifacts (required before Defeat Conditions):
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the specific actor experiencing the failure
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to the triggering condition

Authoring order: Section 1 -> Q3/Q4 -> BRIDGE COMPLETION GATE -> Section 2 -> Section 3 ->
Section 4 -> Section 5 -> Completeness Check. Section 1 must have at least two rows
before anything else is authored.

---

## SECTION 1 -- FAILURE MODE INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the current workaround breaks, produces
errors, causes rework, or hits a scale ceiling. ASSIGN FM-[N] identifiers. MINIMUM 2 rows.
REJECT generic descriptions -- "slow" or "manual" alone fails;
"CSV export silently truncates rows at 65,536 with no error message" passes.

> **[A-16 PRIMARY KEY RULE]**: ASSIGN all FM-[N] identifiers here first. NO FM-[N] reference
> may appear in any later section of this document without a corresponding row assigned
> in this table.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

[BRIDGE Q3 COMMAND]: MAP each FM-[N] to the specific role experiencing the failure.
VERIFY actor name is a specific role title, not "users" or "the team."

| FM-[N] | Actor / role (e.g., data-ops team) | Impact on that role (e.g., re-exports required each pipeline run) |
|--------|------------------------------------|-------------------------------------------------------------------|
| FM-1   |                                    |                                                                   |
| FM-2   |                                    |                                                                   |

---

## Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

[BRIDGE Q4 COMMAND]: MAP each FM-[N] to its triggering condition. QUANTIFY the measurable
threshold.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

---

## BRIDGE COMPLETION GATE

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING SECTION 2
THROUGH SECTION 5. If either row is N, DO NOT PROCEED. Return to Section 1 and complete
the missing artifact.

| Artifact                                       | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

---

## SECTION 2 -- WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific workaround -- the exact tool name, file type, or procedure
name. NOT "a manual process." NAME the role performing it -- the unnamed competitor's current
champion. QUANTIFY the ongoing cost with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it (e.g., data-ops team) | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|------------------------------------------|-----------------------------------|------------------------------------------|
|                                                          |                                          |                                   |                                          |

---

## SECTION 3 -- SWITCHING COST

[C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a number
and a unit. NAME the role bearing each cost. The unnamed competitor holds a switching cost
moat -- map it precisely.

> **[UNIT RULE]**: EVERY estimate must carry a number and a unit. "Significant" without
> a number is REJECTED.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 4 -- THREAT ASSESSMENT

[C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH -- the unnamed competitor
(status quo) always starts with home-field advantage. IF deviating from HIGH, STATE a
specific quantified condition.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
trigger mapping. CITE the FM-[N] driving each condition. "Teams switch when they see
the value" fails -- every DC row must name a testable condition.

> **[A-19 CITATION INTEGRITY RULE]**: EVERY FM-[N] cited in this table MUST have an assigned
> row in Section 1 (FM Inventory). DO NOT introduce FM references not assigned above.
> VERIFY before filling each row.

| DC-[N] | Defeat condition (falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type or segment |
|--------|-------------------------------|-------------------|------------------------------------------------------|----------------------|
| DC-1   |                               |                   |                                                      |                      |
| DC-2   |                               |                   |                                                      |                      |

---

## COMPLETENESS CHECK

| Criterion                                                                                      | Check (Y / N) |
|------------------------------------------------------------------------------------------------|---------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                 |               |
| C-02: At least two switching cost categories, each quantified with number and unit             |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition) |               |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Section 1     |               |
| C-05: At least two specific, non-generic failure modes documented in Section 1                |               |
```

---

## Criterion Coverage Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| A-08 | via A-14 | via A-14 | via A-14 | via A-14 | via A-14 |
| A-10 | PASS: FAIL-FIRST DECLARATION section | PASS: [FAIL-FIRST RULE] label | PASS: FAIL-FIRST -- THE UNNAMED COMPETITOR | PASS: FAIL-FIRST DECLARATION section | PASS: [FAIL-FIRST DECLARATION] -- THE UNNAMED COMPETITOR |
| A-11 | PASS: 5 labeled questions (C-01 through C-05) | PASS: 5 COMMAND prompts (C-01 through C-05) | PASS: 5 labeled questions (C-01 through C-05) | PASS: 5 labeled questions (C-01 through C-05) | PASS: 5 COMMAND prompts (C-01 through C-05) |
| A-12 | PASS: FAIL-FIRST stage listing names Q3/Q4 with chain refs | PASS: FAIL-FIRST bullet list names Q3/Q4 with chain refs | PASS: FAIL-FIRST bullet list names Q3/Q4 with chain refs | PASS: FAIL-FIRST bullet list names Q3/Q4 with chain refs | PASS: FAIL-FIRST bullet list names Q3/Q4 with chain refs |
| A-13 | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular |
| A-14 | PASS: STAGE 1 -- FAILURE MODE INVENTORY, FM-[N] first column | PASS: SECTION 1 -- FAILURE MODE INVENTORY, FM-[N] first column | PASS: SECTION 1 -- STATUS QUO'S VULNERABILITIES: FAILURE MODE INVENTORY | PASS: STAGE 1 -- FAILURE MODE INVENTORY, FM-[N] first column | PASS: SECTION 1 -- FAILURE MODE INVENTORY, FM-[N] first column |
| A-15 | PASS: STAGE 6 -- COMPLETENESS CHECK trailing | PASS: COMPLETENESS CHECK trailing | PASS: SECTION 6 -- COMPLETENESS VERIFICATION trailing | PASS: STAGE 6 -- COMPLETENESS CHECK trailing | PASS: COMPLETENESS CHECK trailing |
| A-16 | PASS: [A-16 PRIMARY KEY RULE] in Stage 1 | PASS: PRIMARY KEY RULE [A-16] in Section 1 | PASS: STATUS QUO LOCK RULE [A-16] in Section 1 | PASS: [A-16 PRIMARY KEY CONSTRAINT] in Stage 1 | PASS: [A-16 PRIMARY KEY RULE] in Section 1 |
| A-17 | PASS: C-01 through C-05 each have labeled question | PASS: C-01 through C-05 each have COMMAND label | PASS: C-01 through C-05 each have labeled question | PASS: C-01 through C-05 each have labeled question | PASS: C-01 through C-05 each have COMMAND label |
| A-18 | PASS: Stage 6 Y/N binary, all 5 criteria | PASS: COMPLETENESS CHECK Y/N binary, all 5 criteria | PASS: Section 6 Y/N binary, all 5 criteria | PASS: Stage 6 Y/N binary, all 5 criteria | PASS: COMPLETENESS CHECK Y/N binary, all 5 criteria |
| A-19 | PASS: [A-19 REFERENTIAL INTEGRITY RULE] in Stage 5B | PASS: CITATION INTEGRITY RULE [A-19] in Section 5 | PASS: STATUS QUO CITATION RULE [A-19] in Section 5 | PASS: [A-19 CITATION INTEGRITY CONSTRAINT] in Stage 5B | PASS: [A-19 CITATION INTEGRITY RULE] in Section 5 |
| A-20 | PASS: Ongoing cost (e.g., 2 hours/week); Estimate (e.g., 3 days); Duration (e.g., 18 months); Trigger (e.g., file > 10MB); Frequency (e.g., 2x/sprint) | PASS: same column set with inline examples | PASS: same column set with inline examples | PASS: same column set with inline examples | PASS: same column set with inline examples |
| A-21 | PASS: DC threshold column has `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column has `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column has `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column has `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column has `(e.g., >10MB, >3 failures/week)` |
| A-22 | PASS: BRIDGE COMPLETION STATUS block between Stage 1 and Stage 3 | PASS: BRIDGE COMPLETION GATE block between Section 1 and Section 2 | PASS: BRIDGE COMPLETION GATE -- READY TO PROCEED? between Section 1 and Section 2 | PASS: [BRIDGE COMPLETION COMMAND] sub-section between Stage 1 and Stage 3 | PASS: BRIDGE COMPLETION GATE block between Section 1 and Section 2 |
| A-23 | PASS: `[A-16 PRIMARY KEY RULE]` + `[A-19 REFERENTIAL INTEGRITY RULE]` (bracket-prefix) | PASS: `PRIMARY KEY RULE [A-16]` + `CITATION INTEGRITY RULE [A-19]` (bracket-suffix) | PASS: `STATUS QUO LOCK RULE [A-16]` + `STATUS QUO CITATION RULE [A-19]` (domain-prefix bracket-suffix) | PASS: `[A-16 PRIMARY KEY CONSTRAINT]` + `[A-19 CITATION INTEGRITY CONSTRAINT]` (bracket-prefix variant) | PASS: `[A-16 PRIMARY KEY RULE]` + `[A-19 CITATION INTEGRITY RULE]` (bracket-prefix) |
| A-24 | PASS: `>10MB` (size) + `>3 failures/week` (frequency) -- two distinct threshold types | PASS: same dual-type | PASS: same dual-type | PASS: same dual-type | PASS: same dual-type |
| A-25 | PASS: `[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding...` as directive in gate block | PASS: `[BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE AUTHORING...` all-caps directive | PASS: `[ACTION REQUIRED: COMPLETE BRIDGE BEFORE PROCEEDING]:` named block heading | PASS: `### [BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE STAGE 3` as sub-section heading | PASS: `[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING...` directive |
| **Predicted** | **180/180** | **180/180** | **180/180** | **180/180** | **180/180** |

---

## A-23 Form Taxonomy

| Form | Example | Variations using it |
|------|---------|---------------------|
| Bracket-prefix | `[A-16 PRIMARY KEY RULE]` | V-01, V-05 |
| Bracket-prefix variant label | `[A-16 PRIMARY KEY CONSTRAINT]` | V-04 |
| Bracket-suffix | `PRIMARY KEY RULE [A-16]` | V-02 |
| Domain-prefixed bracket-suffix | `STATUS QUO LOCK RULE [A-16]` | V-03 |

A-23 stress test: V-03's domain-prefix form is the most divergent from R10 precedent. If A-23 passes on V-03, the criterion is confirmed as label-content-only (ID present anywhere in label text) rather than positionally constrained.

## A-25 Form Taxonomy

| Form | Example | Variations using it |
|------|---------|---------------------|
| Inline bracket-label + sentence | `[BRIDGE COMPLETION COMMAND]: Complete Q3...` | V-01, V-05 |
| All-caps bracket-label + all-caps body | `[BRIDGE COMPLETION COMMAND]: COMPLETE Q3...` | V-02 |
| Action-phrase label | `[ACTION REQUIRED: COMPLETE BRIDGE BEFORE PROCEEDING]:` | V-03 |
| Sub-section heading | `### [BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE STAGE 3` | V-04 |

A-25 stress test: V-04's sub-section heading form -- the directive is the Markdown heading itself. If this passes, the criterion is confirmed as structural-element-type-agnostic (heading, label, inline directive all satisfy).
