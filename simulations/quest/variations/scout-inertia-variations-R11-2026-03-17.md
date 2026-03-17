---

# scout-inertia — Quest Variate R11 (session 2)

**Rubric**: v11 (ceiling 180) | **Date**: 2026-03-17
**Context**: R11 session 1 confirmed 180/180 across 5 axes. Session 2 explores new structural
patterns identified as excellence signals: A-27 (decision-question gate heading), A-26 (axis
vocabulary in subtitles), A-28 (criterion IDs in checklist items), remediation dispatch column.

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Decision-question gate heading | `## BRIDGE COMPLETION GATE -- ALL ARTIFACTS POPULATED?` satisfies A-27; A-25 via separate directive inside block; A-23 bracket-prefix |
| V-02 | Axis vocabulary in section subtitles | `-- NAMING THE UNNAMED COMPETITOR` on FAIL-FIRST + `-- THE UNNAMED COMPETITOR'S WEAKNESSES:` on FM Inventory; domain-prefix A-23 labels; gate `-- READY TO PROCEED?` |
| V-03 | Control: no A-28 prefix | Standard lifecycle with binary checklist and NO `C-0N:` item prefix -- confirms A-28 is new, not default |
| V-04 | Remediation dispatch bridge | Three-column gate table (`Artifact / Populated? / If N: action required`); heading-as-directive A-25 |
| V-05 | All new signals combined | A-26 + A-27 + A-28 + remediation column + COMMAND phrasing; predicted 195/195 on v12 |

---

## V-01 — Decision-question gate heading axis

**Axis**: Gate section heading carries explicit binary decision question (`-- ALL ARTIFACTS POPULATED?`). A-25 via separate `[BRIDGE COMPLETION COMMAND]` directive inside gate block.
**Hypothesis**: A-27 (gate heading question) and A-25 (internal command directive) address different structural layers — both can be satisfied simultaneously in the same gate block without conflict.
**Predicted score**: 180/180

```
## FAIL-FIRST DECLARATION

The current workaround is this feature's primary competitor. Defeat conditions and switching
cost thresholds can only be derived from documented workaround failures. Populate Stage 1 before
any other stage is authored.

Authoring sequence:
- Stage 1 -- FAILURE MODE INVENTORY (C-05): where the workaround breaks
- Stage 2 -- BRIDGE STAGE: Q3 (FM->actor, closes C-05 -> R-02) + Q4 (FM->trigger, closes C-05 -> C-04) + completion gate
- Stage 3 -- WORKAROUND PROFILE (C-01): specific tool, role, ongoing cost
- Stage 4 -- SWITCHING COST (C-02): quantified cost to abandon the workaround
- Stage 5A -- THREAT ASSESSMENT (C-03): inertia threat score
- Stage 5B -- DEFEAT CONDITIONS (C-04): conditions under which the workaround loses
- Stage 6 -- COMPLETENESS CHECK

Stage 2 gate must show Y for both artifacts before Stage 3 is authored.

---

## STAGE 1 -- FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround fail, produce errors, cause
> rework, or hit a scale ceiling? Name the exact failure mode -- not "it's slow." Minimum 2 rows.
> "Manual is slow" fails; "CSV export silently truncates rows above 65,536 with no error message"
> passes.

> **[A-16 PRIMARY KEY RULE]**: No FM-[N] identifier may appear in any later section of this
> document unless it has an assigned row in this table. Assign identifiers here first.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger condition (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|---------------------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                                       |                             |
| FM-2   |                                                                                       |                                    |                                       |                             |

---

## STAGE 2 -- BRIDGE STAGE

### Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

| FM-[N] | Actor / role experiencing this failure (e.g., data-ops team) | Role-level consequence |
|--------|--------------------------------------------------------------|------------------------|
| FM-1   |                                                              |                        |
| FM-2   |                                                              |                        |

### Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                          |                                                      |
| FM-2   |                                                          |                                                      |

### BRIDGE COMPLETION GATE -- ALL ARTIFACTS POPULATED?

[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding to Stage 3. Both rows must
show Y before Stage 3 through Stage 5B are authored. If either is N, return to Stage 1.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

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
> Deviations from HIGH must be justified with a specific, quantified condition.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## STAGE 5B -- DEFEAT CONDITIONS

> **C-04 question**: Under what specific, testable conditions do teams abandon this workaround?
> Each condition must be falsifiable and must cite an FM-[N] from Stage 1.

> **[A-19 CITATION INTEGRITY RULE]**: Every FM-[N] cited in this table must have a corresponding
> assigned row in the FM Inventory (Stage 1). Do not reference FM identifiers not assigned above.
> Verify before filling each row.

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

## V-02 — Axis vocabulary in section subtitles axis

**Axis**: "Unnamed competitor" vocabulary propagated into the subtitle text of the FAIL-FIRST and FM Inventory headings. Domain-prefixed A-23 rule labels carry matching vocabulary. Gate heading carries `-- READY TO PROCEED?`.
**Hypothesis**: A-26 is a coherence criterion — the template's analytical frame should be readable from section headings alone. V-02 stress-tests whether the domain-prefix vocabulary on rule labels (`UNNAMED COMPETITOR LOCK RULE [A-16]`) reads as coherent or cluttered alongside axis subtitle headings.
**Predicted score**: 180/180

```
## FAIL-FIRST DECLARATION -- NAMING THE UNNAMED COMPETITOR

Every feature competes against an unnamed competitor: the current workaround. It has no pricing
page, no product manager, and no roadmap. It wins by default unless teams can name a specific,
observable condition under which it fails. This analysis names the unnamed competitor and answers:
when does the status quo lose?

Document where the unnamed competitor breaks before analyzing anything else. Defeat conditions
cannot be derived without documented failure modes.

Bridge artifacts required before Section 5 is authored:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): which role experiences each failure
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): what condition triggers each failure

---

## SECTION 1 -- THE UNNAMED COMPETITOR'S WEAKNESSES: FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround fail, produce errors, cause
> rework, or hit a scale ceiling? These are the unnamed competitor's vulnerabilities. Minimum 2
> rows. "It's manual and slow" fails. "CSV export silently truncates rows above 65,536 with no
> error message" passes.

> **UNNAMED COMPETITOR LOCK RULE [A-16]**: Assign all FM-[N] identifiers in this table first.
> No FM-[N] may appear in any later section without a corresponding row assigned here.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Who experiences it (e.g., data-ops team) | What triggers it (e.g., file > 10MB) | How often (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------------|---------------------------------------|-----------------------------|
| FM-1   |                                                                                       |                                          |                                       |                             |
| FM-2   |                                                                                       |                                          |                                       |                             |

---

## Q3 -- FM->ACTOR BRIDGE: WHO FEELS EACH FAILURE (closes C-05 -> R-02)

| FM-[N] | Role experiencing the failure (e.g., data-ops team) | Impact on that role |
|--------|-----------------------------------------------------|---------------------|
| FM-1   |                                                     |                     |
| FM-2   |                                                     |                     |

---

## Q4 -- FM->TRIGGER BRIDGE: WHAT ACTIVATES EACH FAILURE (closes C-05 -> C-04)

| FM-[N] | Triggering condition | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|---------------------|------------------------------------------------------|
| FM-1   |                     |                                                      |
| FM-2   |                     |                                                      |

---

## BRIDGE COMPLETION GATE -- READY TO PROCEED?

[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before authoring Sections 2 through 5. If
either row is N, return to Section 1.

| Artifact                                        | Complete? (Y / N) |
|-------------------------------------------------|-------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)   |                   |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04) |                   |

---

## SECTION 2 -- HOW THE UNNAMED COMPETITOR PERSISTS: WORKAROUND PROFILE

> **C-01 question**: What is the specific name of the current workaround -- the exact tool,
> file type, or procedure? Not "a manual process." Who performs it? What is its ongoing cost
> per sprint or per week, with a number and a unit?

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 3 -- THE COST OF LEAVING THE UNNAMED COMPETITOR: SWITCHING ANALYSIS

> **C-02 question**: What does it cost a team to abandon the unnamed competitor? Identify at
> least two cost categories. Every estimate must carry a number and a unit.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 4 -- HOW STRONG IS THE UNNAMED COMPETITOR: THREAT RATING

> **C-03 question**: How strong is the unnamed competitor? Assign a threat score. Default is
> HIGH. Deviations require a specific quantified condition.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- WHEN THE UNNAMED COMPETITOR LOSES: DEFEAT CONDITIONS

> **C-04 question**: Under what specific, observable conditions does a team leave the unnamed
> competitor? Derive each condition from Q4. Each must be falsifiable and cite its FM-[N].

> **UNNAMED COMPETITOR CITATION RULE [A-19]**: Every FM-[N] cited in this table must have an
> assigned row in Section 1. Verify before filling each row.

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
| C-05: At least two specific failure modes in Section 1, each non-generic                       |                    |
```

---

## V-03 — Control: no A-28 prefix (standard lifecycle)

**Axis**: Standard lifecycle stage structure. Binary checklist with full coverage (A-18 PASS) but WITHOUT `C-0N:` criterion ID prefixes on checklist items (A-28 FAIL). Bracket-prefix A-23. This is the control variation: confirms A-28 is a new structural requirement not satisfied by default binary checklist.
**Hypothesis**: V-03 scores 180/180 on v11 (A-28 is not a v11 criterion). Paired with V-05, it enables precise A-28 discrimination in v12 scoring — same template structure, only the checklist item labels differ.
**Predicted score**: 180/180 (v11); 190/195 (v12, A-28 FAIL)

```
## FAIL-FIRST DECLARATION

The current workaround is this feature's primary competitor. Defeat conditions and switching
cost thresholds can only be derived from documented workaround failures. Complete Stage 1 before
any other stage.

Authoring sequence:
- Stage 1 -- FAILURE MODE INVENTORY (C-05): where the workaround breaks
- Stage 2 -- BRIDGE STAGE: Q3 (closes C-05 -> R-02) + Q4 (closes C-05 -> C-04) + gate
- Stage 3 -- WORKAROUND PROFILE (C-01): specific name, role, ongoing cost
- Stage 4 -- SWITCHING COST (C-02): quantified cost to leave the workaround
- Stage 5A -- THREAT ASSESSMENT (C-03): inertia threat score
- Stage 5B -- DEFEAT CONDITIONS (C-04): when the workaround loses
- Stage 6 -- COMPLETENESS CHECK

Stage 2 gate must show Y for both artifacts before Stage 3 is authored.

---

## STAGE 1 -- FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround fail, produce errors, cause
> rework, or hit a scale ceiling? Name the exact failure -- not "it's slow." Minimum 2 rows.
> "Manual is slow" fails; "CSV export silently truncates rows above 65,536 with no error" passes.

> **[A-16 PRIMARY KEY RULE]**: No FM-[N] identifier may appear in any later section unless it
> has an assigned row in this table. Assign FM-[N] identifiers here first.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## STAGE 2 -- BRIDGE STAGE

### Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

| FM-[N] | Actor / role experiencing this failure (e.g., data-ops team) | Role-level consequence |
|--------|--------------------------------------------------------------|------------------------|
| FM-1   |                                                              |                        |
| FM-2   |                                                              |                        |

### Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

| FM-[N] | Triggering condition | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|---------------------|------------------------------------------------------|
| FM-1   |                     |                                                      |
| FM-2   |                     |                                                      |

### BRIDGE COMPLETION STATUS

[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding to Stage 3. If either row
is N, return to Stage 1.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

---

## STAGE 3 -- WORKAROUND PROFILE

> **C-01 question**: What is the exact name of the workaround -- the specific tool, file type,
> or procedure? Not "a manual process." Who performs it? What is the ongoing cost per week or
> sprint, with a unit?

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## STAGE 4 -- SWITCHING COST

> **C-02 question**: What does it cost to abandon this workaround? Identify at least two cost
> categories. Every estimate must carry a number and a unit.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

> **C-03 question**: What is the inertia threat score? Default is HIGH. Deviations require a
> specific quantified condition.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## STAGE 5B -- DEFEAT CONDITIONS

> **C-04 question**: Under what specific, testable conditions do teams abandon this workaround?
> Each condition must be falsifiable. Each row must cite an FM-[N] from Stage 1.

> **[A-19 CITATION INTEGRITY RULE]**: Every FM-[N] cited in this table must have a corresponding
> row in the FM Inventory (Stage 1). Do not reference FM identifiers not assigned above.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type or segment |
|--------|------------------------------------------|-------------------|------------------------------------------------------|----------------------|
| DC-1   |                                          |                   |                                                      |                      |
| DC-2   |                                          |                   |                                                      |                      |

---

## STAGE 6 -- COMPLETENESS CHECK

| Criterion                                                                                      | Check (Y / N) |
|------------------------------------------------------------------------------------------------|---------------|
| Workaround named specifically with role and ongoing cost (number + unit)                       |               |
| At least two switching cost categories quantified with numbers and units                       |               |
| Inertia threat score declared (HIGH by default; deviation requires quantified condition)       |               |
| At least two defeat conditions identified, each falsifiable, each citing FM-[N]                |               |
| At least two failure modes identified, each specific and non-generic                           |               |
```

---

## V-04 — Remediation dispatch bridge axis

**Axis**: Bridge gate verdict table carries a third column — "If N: action required" — specifying the prescribed return action per artifact. Heading-as-directive A-25 form (`### [BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE STAGE 3`).
**Hypothesis**: The three-column gate converts binary status check to action dispatch. An author seeing N has an immediate prescription in the same row — no instruction re-reading required. Heading-as-directive was confirmed in R11 V-04; V-04 session 2 confirms the remediation column adds value alongside that form.
**Predicted score**: 180/180

```
## FAIL-FIRST DECLARATION

The current workaround is this feature's primary competitor. Enumerate its failure modes before
analyzing switching costs or defeat conditions. Defeat conditions require failure triggers;
switching cost calibration requires known failure scale.

Bridge artifacts required before Stage 5B:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the actor experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering condition

Stage structure enforces authoring order. Stage 2 gate opens Stage 3.

---

## STAGE 1 -- FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround fail, produce errors, cause
> rework, or hit a scale ceiling? Name the exact failure mode. Minimum 2 rows. "CSV export
> silently truncates rows above 65,536 with no error message" passes. "Manual is slow" fails.

> **[A-16 PRIMARY KEY CONSTRAINT]**: Assign all FM-[N] identifiers in this table first.
> No FM-[N] identifier may appear in the Defeat Conditions table (Stage 5B) or any other
> downstream section without a corresponding row assigned here.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## STAGE 2 -- BRIDGE STAGE

### Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

| FM-[N] | Actor / role experiencing this failure (e.g., data-ops team) | Role-level impact |
|--------|--------------------------------------------------------------|-------------------|
| FM-1   |                                                              |                   |
| FM-2   |                                                              |                   |

### Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

| FM-[N] | Triggering condition | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|---------------------|------------------------------------------------------|
| FM-1   |                     |                                                      |
| FM-2   |                     |                                                      |

### [BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE STAGE 3

| Artifact                                        | Populated? (Y / N) | If N: action required                              |
|-------------------------------------------------|--------------------|-----------------------------------------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)   |                    | Return to Stage 1. Add actor column for each FM row.|
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04) |                    | Return to Stage 1. Add trigger threshold per FM row.|

Do not proceed to Stage 3 unless both rows show Y.

---

## STAGE 3 -- WORKAROUND PROFILE

> **C-01 question**: What is the exact name of the workaround -- the specific tool, file type,
> or procedure? Not "a manual process." Who performs it? What is the ongoing cost per week or
> sprint, with a unit?

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## STAGE 4 -- SWITCHING COST

> **C-02 question**: What does it cost to abandon this workaround and adopt the feature? Identify
> at least two cost categories. Every estimate must carry a number and a unit.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

> **C-03 question**: What is the inertia threat score? Default is HIGH. Deviations require a
> specific quantified condition -- qualitative judgments do not justify deviation.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## STAGE 5B -- DEFEAT CONDITIONS

> **C-04 question**: Under what specific, testable conditions do teams abandon this workaround?
> Each condition must be falsifiable. Each row must cite an FM-[N] from Stage 1.

> **[A-19 CITATION INTEGRITY CONSTRAINT]**: Every FM-[N] cited in this table must have a
> corresponding row in the FM Inventory (Stage 1). Verify before filling each row.

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

## V-05 — All new signals combined axis

**Axis**: A-26 (axis vocab in subtitles) + A-27 (interrogative gate heading) + A-28 (`C-0N:` prefix on all checklist items) + remediation dispatch column + COMMAND phrasing. Rule labels: `STATUS QUO LOCK RULE [A-16]`, `STATUS QUO CITATION RULE [A-19]`.
**Hypothesis**: All three v12 candidate criteria are orthogonal — A-26 (heading subtitles), A-27 (gate heading question), A-28 (checklist item labels) address distinct structural layers and can coexist without tension. V-05 is predicted 195/195 on v12 if scoring confirms A-28 as criterion-ID-in-label on checklist items.
**Predicted score**: 180/180 (v11); 195/195 (v12)

```
## FAIL-FIRST DECLARATION -- NAMING THE UNNAMED COMPETITOR

Every feature competes against an unnamed competitor: the current workaround. It wins by
default unless teams can name specific conditions under which it fails. This analysis names
the unnamed competitor and answers: when does the status quo lose?

[FAIL-FIRST RULE]: ENUMERATE failure modes before switching costs or defeat conditions. Every
DC row must trace to a documented FM row. Nothing else is worth analyzing until the unnamed
competitor's failure modes are on record.

Bridge artifacts required before defeat conditions are authored:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering condition

---

## SECTION 1 -- THE UNNAMED COMPETITOR'S WEAKNESSES: FAILURE MODE INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the current workaround breaks, produces
errors, causes rework, or hits a scale ceiling. ASSIGN FM-[N] identifiers. MINIMUM 2 rows.
REJECT generic descriptions -- "slow" or "manual" alone fails; "CSV export silently truncates
rows at 65,536 with no error message" passes.

> **STATUS QUO LOCK RULE [A-16]**: ASSIGN all FM-[N] identifiers in this table first. NO FM-[N]
> reference may appear in any later section without a corresponding row assigned here.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

[BRIDGE Q3 COMMAND]: MAP each FM-[N] to the specific role experiencing the failure.
REJECT "users" or "the team" -- role title required.

| FM-[N] | Role experiencing the failure (e.g., data-ops team) | Role-level impact |
|--------|-----------------------------------------------------|-------------------|
| FM-1   |                                                     |                   |
| FM-2   |                                                     |                   |

---

## Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

[BRIDGE Q4 COMMAND]: MAP each FM-[N] to its triggering condition and measurable threshold.

| FM-[N] | Triggering condition | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|---------------------|------------------------------------------------------|
| FM-1   |                     |                                                      |
| FM-2   |                     |                                                      |

---

## BRIDGE COMPLETION GATE -- READY TO PROCEED?

[BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE AUTHORING SECTIONS 2 THROUGH 5. Both
rows must show Y. If either is N, DO NOT PROCEED -- return to Section 1.

| Artifact                                        | Populated? (Y / N) | If N: action required                                    |
|-------------------------------------------------|--------------------|----------------------------------------------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)   |                    | Return to Section 1. Add actor for every FM row.         |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04) |                    | Return to Section 1. Add trigger threshold for every FM. |

---

## SECTION 2 -- HOW THE UNNAMED COMPETITOR PERSISTS: WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific workaround -- exact tool name, file type, or procedure.
NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost with a number
and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 3 -- THE COST OF LEAVING THE UNNAMED COMPETITOR: SWITCHING ANALYSIS

[C-02 COMMAND]: IDENTIFY at least two cost categories. QUANTIFY each with a number and a unit.
NAME the role bearing each cost.

> **[UNIT RULE]**: EVERY estimate must carry a number and a unit. "Significant" without a number
> is REJECTED.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 4 -- HOW STRONG IS THE UNNAMED COMPETITOR: THREAT RATING

[C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH. IF deviating from HIGH,
STATE a specific quantified condition -- qualitative justification is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- WHEN THE UNNAMED COMPETITOR LOSES: DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from Q4 trigger
mapping. CITE FM-[N] driving each. "Teams switch when they see the value" fails.

> **STATUS QUO CITATION RULE [A-19]**: EVERY FM-[N] cited in this table MUST have an assigned
> row in Section 1. DO NOT introduce FM references not assigned above. VERIFY before each row.

| DC-[N] | Defeat condition (falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team segment |
|--------|-------------------------------|-------------------|------------------------------------------------------|--------------|
| DC-1   |                               |                   |                                                      |              |
| DC-2   |                               |                   |                                                      |              |

---

## SECTION 6 -- COMPLETENESS VERIFICATION

| Criterion                                                                                              | Satisfied? (Y / N) |
|--------------------------------------------------------------------------------------------------------|--------------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                         |                    |
| C-02: At least two switching cost categories, each with number and unit                                |                    |
| C-03: Inertia threat score declared HIGH by default; if not HIGH, quantified justification given       |                    |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Section 1             |                    |
| C-05: At least two specific failure modes in Section 1, each non-generic                               |                    |
```

---

## Design Notes

### V-01 vs V-02: Two independent paths to A-27

V-01 uses `-- ALL ARTIFACTS POPULATED?` (completion-status question). V-02 uses `-- READY TO PROCEED?` (proceed-or-stop question). Both satisfy A-27's "binary decision question in heading line" requirement. The distinction matters for rubric refinement: if only one form passes, A-27's "binary decision question" definition needs tightening. If both pass, A-27 is form-agnostic on question phrasing.

### V-03 as control variation

V-03's checklist deliberately omits `C-0N:` prefixes to isolate the A-28 signal. It will score 180/180 on v11. Under v12 it should score 190/195 (A-28 FAIL). V-05 scores 195/195. The V-03/V-05 pair is the cleanest possible A-28 ablation — every other structural element is identical between them.

### V-04 remediation column: two implementations compared

R11 V-04 (session 1) used the heading-as-directive with prescriptive action instructions in prose below the table. V-04 session 2 moves the prescriptions into the table itself as a dedicated column. The table-column form is more auditable — the prescription is co-located with the status cell it addresses, not in a separate prose block that an author might skim. This is the excess signal from R11 V-04 formalized.

### V-05 predicted 195/195 on v12

V-05 carries all three v12 candidate criteria simultaneously:
- A-26: `-- NAMING THE UNNAMED COMPETITOR` (FAIL-FIRST subtitle) + `-- THE UNNAMED COMPETITOR'S WEAKNESSES:` (FM Inventory subtitle)
- A-27: `## BRIDGE COMPLETION GATE -- READY TO PROCEED?`
- A-28: All five checklist items carry `C-0N:` prefix in item label

If v12 scoring confirms 195/195 on V-05, R11 session 2 has found the first perfect-score template two rubric versions ahead of the current ceiling.
