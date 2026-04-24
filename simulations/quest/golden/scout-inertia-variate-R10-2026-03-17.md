# scout-inertia -- Quest Variate R10

**Rubric**: v10 (ceiling 165 = 100 essential base + 13 advanced criteria x 5 pts)
**Date**: 2026-03-17
**Previous round**: R9 V-05 scored 155/155 on v9 rubric
**R10 target**: 165/165 -- first simultaneous pass on A-21 and A-22 alongside full v9 scaffold
**New criteria**: A-21 (DC threshold column inline example) + A-22 (mid-template bridge completion gate)

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle emphasis | 6-stage lifecycle; Stage 2 = Bridge Stage containing Q3/Q4 tables + binary BRIDGE COMPLETION STATUS gate; stage boundary enforces A-22 |
| V-02 | Phrasing register | Imperative COMMAND phrasing throughout; [C-XX COMMAND] questions; criterion-code labeled rules [A-16]/[A-19]; [BRIDGE COMPLETION COMMAND] gate |
| V-03 | Inertia framing | "Status-quo competitor" metaphor reframes all section names; FAIL-FIRST anchors the metaphor; bridge gate named "BRIDGE COMPLETION GATE -- READY TO PROCEED?" |
| V-04 | Lifecycle + Output format | Stage structure + consolidated bridge triple-block (Q3 table, Q4 table, BRIDGE GATE VERDICT table with remediation column); dual-position Q3/Q4 naming |
| V-05 | All axes | V-05 R9 section structure + COMMAND phrasing + criterion-code labels + inertia framing in FAIL-FIRST + A-21 dual-example threshold + A-22 explicit gate + all-column concrete examples |

---

## R10 Design Notes

### A-22 mechanism

Three implementations across the variations:

1. **Stage gate** (V-01, V-04): Gate lives at the end of the dedicated Bridge Stage, before the next content stage opens. Stage boundary is the structural enforcer.
2. **Command gate** (V-02, V-05): "BRIDGE COMPLETION COMMAND" or "BRIDGE COMPLETION GATE" labeled binary table, positioned as a named standalone section after Q3/Q4 tables.
3. **Status-framed gate** (V-03): "BRIDGE COMPLETION GATE -- READY TO PROCEED?" -- same structure but framed as a go/no-go readiness check for the status-quo analysis.

All three satisfy A-22 if they: (a) are a named structural element, (b) explicitly name Q3 and Q4, (c) use binary-observable format, (d) are positioned after FM Inventory and before DC section.

### A-21 mechanism

All five variations include the DC table threshold column with a dual-type inline example demonstrating comparison operator + value + unit format. "(e.g., >10MB, >3 failures/week)" demonstrates both a size threshold and a frequency threshold, making the operator+value+unit expectation explicit at the authoring point.

The Q4 bridge table also carries a threshold column in V-01 through V-05. This is an authoring convenience (helps populate DC thresholds from bridge triggers) but does not satisfy A-21 -- A-21 specifically targets the DC table column.

### Implication chain

For 165/165, the following must hold simultaneously:
- A-22 implies A-12 (bridge artifacts named in body)
- A-21 requires A-20 and A-13 as preconditions
- A-19 implies A-16 implies A-14 implies A-08
- A-18 implies A-15
- A-17 implies A-11

---

## V-01 -- Lifecycle emphasis axis

**Axis**: How lifecycle stage boundaries are drawn; bridge stage as a first-class authoring stage with a gate at its end.
**Hypothesis**: Making Stage 2 a named Bridge Stage with three sub-elements (Q3 table, Q4 table, completion gate) means the gate is structurally inseparable from bridge authoring. An author cannot complete the stage without passing the gate. A-22 is enforced by stage structure, not just by a reminder.
**Predicted score**: 165/165

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

This is the structural foundation. Stage 2 gate must show Y for both artifacts before Stage 3 is authored.

---

## STAGE 1 -- FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround fail, produce errors, cause
> rework, or hit a scale ceiling? Name the exact failure mode -- not "it's slow." Minimum 2 rows
> required. "Manual is slow" fails; "CSV export silently truncates rows above 65,536 with no
> error message" passes.

> **PRIMARY KEY CONSTRAINT**: No FM-[N] identifier may appear in any later section of this
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

| FM-[N] | Triggering condition | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|---------------------|------------------------------------------------------|
| FM-1   |                     |                                                      |
| FM-2   |                     |                                                      |

### BRIDGE COMPLETION STATUS

Before proceeding to Stage 3, confirm both bridge artifacts have been populated. Do not author
Stage 3 through Stage 5 unless both rows show Y.

| Bridge artifact                               | Populated? (Y / N) |
|-----------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02) |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                   |

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
|------------------------|-------------|------------------------|---------------------------------------|
| Migration effort       |             |                        |                                       |
| Training overhead      |             |                        |                                       |
| Process disruption     |             |                        |                                       |
| In-flight work at risk |             |                        |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

> **C-03 question**: What is the inertia threat score for this feature? Default is HIGH.
> Deviations from HIGH must be justified with a specific, quantified condition -- a qualitative
> judgment does not justify deviation.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|--------------------------|
|                                            |                          |

---

## STAGE 5B -- DEFEAT CONDITIONS

> **C-04 question**: Under what specific, testable conditions do teams abandon this workaround
> in favor of the feature? Each condition must be falsifiable. "Teams switch when they see the
> value" fails. Each row must cite an FM-[N] from Stage 1.

> **REFERENTIAL INTEGRITY RULE (citation point)**: Every FM-[N] cited in this table must have
> a corresponding assigned row in the FM Inventory (Stage 1). Do not reference FM identifiers
> not assigned above. Verify before filling each row.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type or segment |
|--------|------------------------------------------|-------------------|------------------------------------------------------|---------------------|
| DC-1   |                                          |                   |                                                      |                     |
| DC-2   |                                          |                   |                                                      |                     |

---

## STAGE 6 -- COMPLETENESS CHECK

| Criterion                                                                                     | Check (Y / N) |
|-----------------------------------------------------------------------------------------------|---------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                |               |
| C-02: At least two switching cost categories quantified with numbers and units                |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition)|               |
| C-04: At least two defeat conditions identified, each falsifiable, each citing FM-[N]         |               |
| C-05: At least two failure modes identified, each specific and non-generic                    |               |
```

---

## V-02 -- Phrasing register axis

**Axis**: Imperative COMMAND phrasing for all questions and rules; criterion-code labels link rules to rubric.
**Hypothesis**: COMMAND phrasing makes the action unambiguous at each authoring point -- the author cannot read a command without knowing exactly what to do. Criterion-code labels ([A-16 PRIMARY KEY RULE], [A-19 CITATION INTEGRITY RULE]) create explicit traceability between each rule and its rubric criterion. The [BRIDGE COMPLETION COMMAND] gate is the same binary structure as V-01 but voiced as a directive rather than a status form.
**Predicted score**: 165/165

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

> **[A-16 PRIMARY KEY RULE]**: ASSIGN all FM-[N] identifiers in this table first. NO FM-[N]
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

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 and Q4 are populated before authoring Section 2
through Section 5. If either row is N, DO NOT PROCEED. Return to Section 1.

| Artifact                                      | Populated? (Y / N) |
|-----------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02) |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                   |

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
|------------------------|-------------|------------------------|---------------------------------------|
| Migration effort       |             |                        |                                       |
| Training overhead      |             |                        |                                       |
| Process disruption     |             |                        |                                       |
| In-flight work at risk |             |                        |                                       |

---

## SECTION 4 -- THREAT ASSESSMENT

[C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH. IF deviating from HIGH,
STATE a specific quantified condition -- a qualitative judgment ("low friction") is REJECTED
as justification.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|--------------------------|
|                                            |                          |

---

## SECTION 5 -- DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4 trigger
mapping above. CITE the FM-[N] driving each. "Teams switch when they see the value" fails --
every DC row must name a testable condition.

> **[A-19 CITATION INTEGRITY RULE]**: EVERY FM-[N] cited in this table MUST have an assigned
> row in Section 1 (FM Inventory). DO NOT introduce FM references not assigned above.
> VERIFY before filling each row.

| DC-[N] | Defeat condition (falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type |
|--------|-------------------------------|-------------------|------------------------------------------------------|-----------|
| DC-1   |                               |                   |                                                      |           |
| DC-2   |                               |                   |                                                      |           |

---

## COMPLETENESS CHECK

| Criterion                                                                                     | Check (Y / N) |
|-----------------------------------------------------------------------------------------------|---------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                |               |
| C-02: At least two switching cost categories, each with number and unit                       |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition)|               |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Section 1    |               |
| C-05: At least two specific, non-generic failure modes in Section 1                          |               |
```

---

## V-03 -- Inertia framing axis

**Axis**: The status-quo competitor is named and foregrounded throughout; section names reframe every analytical step as competitive intelligence on the unnamed opponent.
**Hypothesis**: Naming the status quo as "the unnamed competitor" in FAIL-FIRST primes the author to treat inertia as a real competitive threat requiring rigorous defeat analysis, not a formality. The framing does not change structural coverage -- all 13 advanced criteria are met -- but raises the quality floor of defeat condition writing by making the analytical frame explicit.
**Predicted score**: 165/165

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

## SECTION 1 -- THE STATUS QUO'S WEAK POINTS: FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround fail, produce errors, cause
> rework, or hit a scale ceiling? These are the status quo's vulnerabilities. Name each failure
> precisely -- not "it's slow." Minimum 2 rows.

> **PRIMARY KEY CONSTRAINT [A-16]**: Assign all FM-[N] identifiers in this table first.
> No FM-[N] may appear in any later section without a corresponding row assigned here.

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

Before profiling the status quo, confirm both bridge artifacts are complete. These bridges
supply the actor and trigger chains that defeat conditions require. An N in either row means
the status quo analysis is incomplete -- return to Section 1.

| Artifact                                      | Complete? (Y / N) |
|-----------------------------------------------|------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02) |                  |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                 |

---

## SECTION 2 -- HOW THE STATUS QUO PERSISTS: WORKAROUND PROFILE

> **C-01 question**: What exactly is the current workaround? Name the specific tool, file
> format, or procedure -- not "a manual process." Who performs it? What is its ongoing cost
> per week or per sprint, with a number and unit?

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Time in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------|
|                                                          |                    |                                   |                                    |

---

## SECTION 3 -- THE COST OF DEFECTING: SWITCHING ANALYSIS

> **C-02 question**: What would it cost a team to abandon this workaround? Identify at least
> two cost categories. Every estimate must have a number and a unit.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|------------------------|---------------------------------------|
| Migration effort       |             |                        |                                       |
| Training overhead      |             |                        |                                       |
| Process disruption     |             |                        |                                       |
| In-flight work at risk |             |                        |                                       |

---

## SECTION 4 -- HOW STRONG IS THE STATUS QUO: THREAT RATING

> **C-03 question**: How strong is the unnamed competitor? Score it. Default threat score
> is HIGH -- the status quo always has home-field advantage. Deviations from HIGH require
> a specific quantified condition, not a qualitative judgment.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|--------------------------|
|                                            |                          |

---

## SECTION 5 -- WHEN THE STATUS QUO LOSES: DEFEAT CONDITIONS

> **C-04 question**: Under what specific, observable conditions does a team switch from the
> workaround to this feature? Derive each condition from the triggers in Q4. Every condition
> must be falsifiable -- "teams switch when they see the value" fails.

> **REFERENTIAL INTEGRITY RULE (citation point) [A-19]**: Every FM-[N] cited in this table
> must have an assigned row in Section 1. No FM identifier may be introduced here without
> prior assignment. Verify before filling each row.

| DC-[N] | Defeat condition (falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team segment |
|--------|-------------------------------|-------------------|------------------------------------------------------|--------------|
| DC-1   |                               |                   |                                                      |              |
| DC-2   |                               |                   |                                                      |              |

---

## SECTION 6 -- COMPLETENESS VERIFICATION

| Criterion                                                                                     | Satisfied? (Y / N) |
|-----------------------------------------------------------------------------------------------|-------------------|
| C-01: Workaround named specifically, with role, with cost in number + unit                    |                   |
| C-02: At least two switching cost categories, each quantified with number + unit              |                   |
| C-03: Inertia threat score declared; if not HIGH, a quantified justification is given         |                   |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Section 1    |                   |
| C-05: At least two specific failure modes in Section 1, each non-generic                     |                   |
```

---

## V-04 -- Lifecycle + Output format (two axes)

**Axis**: Stage structure (V-01 base) combined with a consolidated bridge triple-block -- Q3 table, Q4 table, and BRIDGE GATE VERDICT table with a remediation column, all contained within a single dedicated BRIDGE STAGE. Dual-position Q3/Q4 naming: declared in FAIL-FIRST and echoed as Stage 2 sub-section headers.
**Hypothesis**: The BRIDGE GATE VERDICT table's third column ("If N: action required") eliminates ambiguity about what to do when a bridge is incomplete -- the remediation path is visible at the gate, not in a separate instruction block. Dual-position naming (FAIL-FIRST + Stage 2) satisfies A-12 with maximum redundancy.
**Predicted score**: 165/165

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

### BRIDGE GATE VERDICT

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
|------------------------|-------------|------------------------|---------------------------------------|
| Migration effort       |             |                        |                                       |
| Training overhead      |             |                        |                                       |
| Process disruption     |             |                        |                                       |
| In-flight work at risk |             |                        |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

> **C-03 question**: What is the inertia threat score? Default is HIGH. Deviations from HIGH
> must be justified with a specific quantified condition -- a qualitative statement does not
> justify deviation.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|--------------------------|
|                                            |                          |

---

## STAGE 5B -- DEFEAT CONDITIONS

> **C-04 question**: Under what specific, testable conditions do teams abandon this workaround
> in favor of the feature? Each condition must be falsifiable -- derive it from Q4 triggers.
> Cite the FM-[N] driving each defeat condition.

> **[A-19 REFERENTIAL INTEGRITY RULE -- citation point]**: Every FM-[N] cited in this table
> must have an assigned row in the FM Inventory (Stage 1). Do not reference FM identifiers
> not assigned in Stage 1. Verify before filling each row.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type |
|--------|------------------------------------------|-------------------|------------------------------------------------------|-----------|
| DC-1   |                                          |                   |                                                      |           |
| DC-2   |                                          |                   |                                                      |           |

---

## STAGE 6 -- COMPLETENESS CHECK

| Criterion                                                                                     | Check (Y / N) |
|-----------------------------------------------------------------------------------------------|---------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                |               |
| C-02: At least two switching cost categories quantified with number and unit                  |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition)|               |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Stage 1      |               |
| C-05: At least two specific, non-generic failure modes in Stage 1                            |               |
```

---

## V-05 -- All axes combined

**Axis**: V-05 R9 section structure + COMMAND phrasing + criterion-code labeled rules + inertia framing in FAIL-FIRST + A-21 dual-example threshold + A-22 explicit completion gate + all-column concrete examples (extends R9 V-05 excellence signal to non-unit columns).
**Hypothesis**: This is the minimal extension of R9 V-05 (155/155) that achieves 165/165. R9 V-05 passed A-21 with a single threshold example "(e.g., >10MB)"; V-05 R10 extends this to a dual-type example "(e.g., >10MB, >3 failures/week)" making the operator+value+unit format unambiguous across threshold types. R9 V-05's bridge Q3/Q4 command tables were authoring spaces; V-05 R10 adds an explicit binary gate section after the bridge tables, before the Defeat Conditions section, that explicitly checks completion rather than providing authoring space.
**Predicted score**: 165/165

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

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 and Q4 are populated before authoring Section 2
through Section 5. If either row is N, DO NOT PROCEED. Return to Section 1.

| Artifact                                      | Populated? (Y / N) |
|-----------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02) |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                   |

---

## SECTION 2 -- WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific workaround -- the exact tool name, file type, or procedure
name. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost with
a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it (e.g., data-ops team) | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|------------------------------------------|-----------------------------------|------------------------------------------|
|                                                          |                                          |                                   |                                          |

---

## SECTION 3 -- SWITCHING COST

[C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a number
and a unit. NAME the role bearing each cost.

> **[UNIT RULE]**: EVERY estimate must carry a number and a unit. "Significant" without
> a number is REJECTED.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|------------------------|---------------------------------------|
| Migration effort       |             |                        |                                       |
| Training overhead      |             |                        |                                       |
| Process disruption     |             |                        |                                       |
| In-flight work at risk |             |                        |                                       |

---

## SECTION 4 -- THREAT ASSESSMENT

[C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH -- the unnamed competitor
(status quo) always starts with home-field advantage. IF deviating from HIGH, STATE a
specific quantified condition.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|--------------------------|
|                                            |                          |

---

## SECTION 5 -- DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
trigger mapping. CITE the FM-[N] driving each condition. "Teams switch when they see
the value" fails -- every DC row must name a testable condition.

> **[A-19 CITATION INTEGRITY RULE]**: EVERY FM-[N] cited in this table MUST have an assigned
> row in Section 1 (FM Inventory). DO NOT introduce FM references not assigned above.
> VERIFY before filling each row.

| DC-[N] | Defeat condition (falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type or segment |
|--------|-------------------------------|-------------------|------------------------------------------------------|---------------------|
| DC-1   |                               |                   |                                                      |                     |
| DC-2   |                               |                   |                                                      |                     |

---

## COMPLETENESS CHECK

| Criterion                                                                                     | Check (Y / N) |
|-----------------------------------------------------------------------------------------------|---------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                |               |
| C-02: At least two switching cost categories, each quantified with number and unit            |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition)|               |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Section 1    |               |
| C-05: At least two specific, non-generic failure modes documented in Section 1               |               |
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
| A-10 | PASS: Stage lifecycle names FM-first | PASS: [FAIL-FIRST RULE] | PASS: FAIL-FIRST -- THE UNNAMED COMPETITOR | PASS: FAIL-FIRST declaration | PASS: [FAIL-FIRST DECLARATION] -- THE UNNAMED COMPETITOR |
| A-11 | PASS: 5 labeled questions | PASS: 5 COMMAND prompts | PASS: 5 labeled questions | PASS: 5 labeled questions | PASS: 5 COMMAND prompts |
| A-12 | PASS: FAIL-FIRST names Q3/Q4 with chain refs | PASS: FAIL-FIRST names Q3/Q4 with chain refs | PASS: FAIL-FIRST names Q3/Q4 with chain refs | PASS: FAIL-FIRST + Stage 2 sub-headers (dual-position) | PASS: FAIL-FIRST names Q3/Q4 with chain refs |
| A-13 | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular |
| A-14 | PASS: Stage 1 -- FM INVENTORY titled, FM-[N] first | PASS: Section 1 -- FM INVENTORY titled, FM-[N] first | PASS: Section 1 -- FAILURE MODE INVENTORY in title, FM-[N] first | PASS: Stage 1 -- FM INVENTORY titled, FM-[N] first | PASS: Section 1 -- FM INVENTORY titled, FM-[N] first |
| A-15 | PASS: Stage 6 trailing | PASS: COMPLETENESS CHECK trailing | PASS: Section 6 trailing | PASS: Stage 6 trailing | PASS: COMPLETENESS CHECK trailing |
| A-16 | PASS: PRIMARY KEY CONSTRAINT in Stage 1 | PASS: [A-16 PRIMARY KEY RULE] in Section 1 | PASS: PRIMARY KEY CONSTRAINT [A-16] in Section 1 | PASS: [A-16 PRIMARY KEY CONSTRAINT] in Stage 1 | PASS: [A-16 PRIMARY KEY RULE] in Section 1 |
| A-17 | PASS: C-01 through C-05 each have labeled question | PASS: C-01 through C-05 each have COMMAND | PASS: C-01 through C-05 each have labeled question | PASS: C-01 through C-05 each have labeled question | PASS: C-01 through C-05 each have COMMAND |
| A-18 | PASS: Y / N binary, all 5 criteria | PASS: Y / N binary, all 5 criteria | PASS: Y / N binary, all 5 criteria | PASS: Y / N binary, all 5 criteria | PASS: Y / N binary, all 5 criteria |
| A-19 | PASS: PRIMARY KEY CONSTRAINT (source) + REFERENTIAL INTEGRITY RULE citation point | PASS: [A-16] source + [A-19 CITATION INTEGRITY RULE] citation | PASS: [A-16] source + [A-19] citation | PASS: [A-16] source + [A-19] citation | PASS: [A-16 PRIMARY KEY RULE] source + [A-19 CITATION INTEGRITY RULE] citation |
| A-20 | PASS: Frequency, Ongoing cost, Duration, Estimate, Role bearing it all have inline examples | PASS: same columns covered | PASS: same columns covered | PASS: same columns covered | PASS: all columns including non-unit (Actor/role, Trigger, Impact) |
| A-21 | PASS: Stage 5B Measurable threshold (e.g., >10MB, >3 failures/week) | PASS: Section 5 Measurable threshold (e.g., >10MB, >3 failures/week) | PASS: Section 5 Measurable threshold (e.g., >10MB, >3 failures/week) | PASS: Stage 5B Measurable threshold (e.g., >10MB, >3 failures/week) | PASS: Section 5 Measurable threshold (e.g., >10MB, >3 failures/week) |
| A-22 | PASS: BRIDGE COMPLETION STATUS binary table, end of Stage 2, between Stage 1 and Stage 5B | PASS: BRIDGE COMPLETION GATE binary table, after Q4, before Section 2 | PASS: BRIDGE COMPLETION GATE binary table, after Q4, before Section 2 | PASS: BRIDGE GATE VERDICT binary table with remediation column, end of Stage 2 Bridge | PASS: BRIDGE COMPLETION GATE binary table, after Q4, before Section 2 |
| **Predicted total** | **165/165** | **165/165** | **165/165** | **165/165** | **165/165** |

---

## Differentiating signals to watch in scoring

1. **A-10 at risk in V-03**: FAIL-FIRST DECLARATION subtitle contains framing text. Scorer should confirm "FAIL-FIRST DECLARATION" prefix satisfies the label criterion regardless of subtitle.

2. **A-14 at risk in V-03**: Section 1 title is "THE STATUS QUO'S WEAK POINTS: FAILURE MODE INVENTORY" -- the FM INVENTORY name appears as a suffix. Scorer should confirm that a titled, dedicated FM table with FM-[N] as first column satisfies A-14 regardless of the full section title.

3. **A-22 position in V-02/V-03/V-05**: Gate is between Q4 and Section 2 (Workaround Profile) -- this is between FM Inventory section and DC section (Section 5), satisfying the A-22 position requirement. Not immediately before DC section but within the required range.

4. **A-22 in V-04**: Gate named "BRIDGE GATE VERDICT" with a remediation column (third column) rather than a note. The binary observable column is "Populated? (Y / N)" -- binary criterion satisfied regardless of third column.

5. **V-05 non-unit column examples**: V-05 includes inline examples in non-unit columns (Actor/role, Trigger, Impact) following the R9 V-05 excellence signal. This exceeds A-20 requirements but does not conflict with any criterion.
