# scout-inertia -- Quest Variate R11 (session 2)

**Rubric**: v11 (ceiling 180 = 100 essential base + 16 advanced criteria x 5 pts)
**Date**: 2026-03-17
**Context**: R11 session 1 confirmed 180/180 across 5 axes. Session 2 explores new structural
patterns identified as excellence signals in session 1 scoring: A-27 (decision-question gate
heading), A-26 (axis vocabulary in section subtitles), A-28 (criterion IDs in checklist items),
and the remediation dispatch column (V-04 excess signal). All five variations target 180/180 on
v11 and are expected to surface A-26/A-27/A-28 signals for v12 rubric construction.

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Decision-question gate heading | Gate heading in interrogative form (`-- ALL ARTIFACTS POPULATED?`); A-23 bracket-prefix; A-25 directive inside gate block |
| V-02 | Axis vocabulary in section subtitles | "Unnamed competitor" framing in FAIL-FIRST and FM Inventory heading subtitles; domain-prefixed A-23 rule labels; gate heading `-- READY TO PROCEED?` |
| V-03 | Criterion ID in trailing checklist | All 5 checklist items prefixed `C-0N:` for A-28 traceability; bracket-prefix A-23; lifecycle stage structure |
| V-04 | Remediation dispatch bridge | Bridge gate verdict table carries `If N: action required` column; heading-as-directive A-25 form |
| V-05 | All new signals combined | A-26 + A-27 + A-28 + remediation column + COMMAND phrasing |

---

## V-01 -- Decision-question gate heading axis

**Axis**: The bridge gate section heading carries an explicit binary decision question as part of
the heading line. All other structure follows R11 V-01 lifecycle pattern. A-23 via bracket-prefix
form. A-25 via `[BRIDGE COMPLETION COMMAND]` directive inside the gate block.
**Hypothesis**: The interrogative heading form (`## BRIDGE COMPLETION GATE -- ALL ARTIFACTS
POPULATED?`) satisfies A-22's named structural block requirement while adding A-27's decision
question in a single heading line. The question is visible in document outline without opening
the block. A-23 bracket-prefix is the clearest form; A-25 via inline directive is the cleanest
co-location.
**Predicted score**: 180/180

---

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

Map each failure mode to the specific role experiencing it.

| FM-[N] | Actor / role experiencing this failure (e.g., data-ops team) | Role-level consequence |
|--------|--------------------------------------------------------------|------------------------|
| FM-1   |                                                              |                        |
| FM-2   |                                                              |                        |

### Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

Map each failure mode to its triggering condition and measurable threshold.

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

## V-02 -- Axis vocabulary in section subtitles axis

**Axis**: The "unnamed competitor" framing propagates into the subtitle text of the FAIL-FIRST
heading and FM Inventory heading. Gate heading carries decision question. A-23 via domain-prefixed
bracket-suffix rule labels. Section content headings also carry axis vocabulary in subtitles.
**Hypothesis**: Embedding axis vocabulary in section heading subtitles (`-- NAMING THE UNNAMED
COMPETITOR`, `-- THE UNNAMED COMPETITOR'S WEAKNESSES:`) makes the template self-contextualizing
-- an author reading any section heading understands the analytical frame without re-reading the
FAIL-FIRST declaration. A-26 is a visible authoring aid, not decorative. Domain-prefixed A-23
labels (`UNNAMED COMPETITOR LOCK RULE [A-16]`) are semantically coherent with the axis vocabulary.
**Predicted score**: 180/180

---

```
## FAIL-FIRST DECLARATION -- NAMING THE UNNAMED COMPETITOR

Every feature competes against an unnamed competitor: the current workaround. It has no pricing
page, no product manager, and no roadmap. It wins by default unless teams can name a specific,
observable condition under which it fails. This analysis names the unnamed competitor and answers
one question: when does the status quo lose?

Document where the unnamed competitor breaks before analyzing anything else. Defeat conditions
cannot be derived without documented failure modes. Switching cost thresholds cannot be
calibrated without knowing the failure trigger.

Bridge artifacts required before Section 5 is authored:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): which role experiences each failure
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): what condition triggers each failure

---

## SECTION 1 -- THE UNNAMED COMPETITOR'S WEAKNESSES: FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround fail, produce errors, cause
> rework, or hit a scale ceiling? These are the unnamed competitor's vulnerabilities. Name each
> precisely. Minimum 2 rows. "It's manual and slow" fails. "CSV export silently truncates rows
> above 65,536 with no error message" passes.

> **UNNAMED COMPETITOR LOCK RULE [A-16]**: Assign all FM-[N] identifiers in this table first.
> No FM-[N] may appear in any later section without a corresponding row assigned here.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Who experiences it (e.g., data-ops team) | What triggers it (e.g., file > 10MB) | How often (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------------|---------------------------------------|-----------------------------|
| FM-1   |                                                                                       |                                          |                                       |                             |
| FM-2   |                                                                                       |                                          |                                       |                             |

---

## Q3 -- FM->ACTOR BRIDGE: WHO FEELS EACH FAILURE (closes C-05 -> R-02)

Map each failure mode to the specific role experiencing it.

| FM-[N] | Role experiencing the failure (e.g., data-ops team) | Impact on that role |
|--------|-----------------------------------------------------|---------------------|
| FM-1   |                                                     |                     |
| FM-2   |                                                     |                     |

---

## Q4 -- FM->TRIGGER BRIDGE: WHAT ACTIVATES EACH FAILURE (closes C-05 -> C-04)

Map each failure mode to its triggering condition and measurable threshold.

| FM-[N] | Triggering condition | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|---------------------|------------------------------------------------------|
| FM-1   |                     |                                                      |
| FM-2   |                     |                                                      |

---

## BRIDGE COMPLETION GATE -- READY TO PROCEED?

[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before authoring Sections 2 through 5. The
unnamed competitor's actor chain and trigger chain must be documented before its profile,
switching cost, and defeat conditions can be derived. If either row is N, return to Section 1.

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
> HIGH -- the unnamed competitor always has home-field advantage. Deviations from HIGH require
> a specific quantified condition, not a qualitative description.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- WHEN THE UNNAMED COMPETITOR LOSES: DEFEAT CONDITIONS

> **C-04 question**: Under what specific, observable conditions does a team leave the unnamed
> competitor behind? Derive each condition from the Q4 trigger mapping above. Each condition
> must be falsifiable and must cite the FM-[N] that drives it.

> **UNNAMED COMPETITOR CITATION RULE [A-19]**: Every FM-[N] cited in this table must have an
> assigned row in Section 1. No FM identifier may be introduced here without prior assignment.
> Verify before filling each row.

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

## V-03 -- Criterion ID in trailing checklist axis

**Axis**: Every item in the trailing completeness checklist carries its essential criterion ID
(C-01 through C-05) as a prefix in the item label, enabling direct rubric traceability from each
verification item to its criterion. Lifecycle stage structure. A-23 bracket-prefix. A-25 directive
inside gate block.
**Hypothesis**: Prefixing checklist items with criterion IDs (`C-01: Workaround named
specifically...`) applies the A-23 traceability pattern to the verification layer. An author
sees the rubric criterion ID at verification time without external reference. A-28 is the
extension of A-23 from integrity rule labels to checklist items -- V-03 tests whether the
criterion-ID-in-label pattern generalizes cleanly to the checklist structural layer.
**Predicted score**: 180/180

---

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

[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding to Stage 3. Do not author
Stages 3 through 5B unless both rows below show Y. If either is N, return to Stage 1.

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

> **C-03 question**: What is the inertia threat score? Default is HIGH. Deviations from HIGH
> must be justified with a specific quantified condition.

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
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                 |               |
| C-02: At least two switching cost categories quantified with numbers and units                 |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition) |               |
| C-04: At least two defeat conditions identified, each falsifiable, each citing FM-[N]          |               |
| C-05: At least two failure modes identified, each specific and non-generic                     |               |
```

---

## V-04 -- Remediation dispatch bridge axis

**Axis**: Bridge completion gate verdict table carries a third column: "If N: action required."
Each row specifies the exact prescribed action for a failed artifact. The gate heading is the
command directive itself (heading-as-directive A-25 form). A-23 via bracket-prefix labels.
**Hypothesis**: Adding a prescriptive action column to the gate table converts it from a binary
status check into an action dispatch table -- an author seeing N in any row has an immediate
prescription without re-reading instructions. The heading-as-directive form (`### [BRIDGE
COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE STAGE 3`) satisfies A-25 while making the
command structurally inseparable from the gate. V-04 tests whether the three-column remediation
form works alongside the heading-as-directive A-25 pattern.
**Predicted score**: 180/180

---

```
## FAIL-FIRST DECLARATION

The current workaround is this feature's primary competitor. Enumerate its failure modes before
analyzing switching costs or defeat conditions. Defeat conditions require failure triggers;
switching cost calibration requires known failure scale. Populate Stage 1 first.

Bridge artifacts required before Stage 5B:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the actor experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering condition

Stage structure enforces authoring order. Stage 2 gate opens Stage 3. No exceptions.

---

## STAGE 1 -- FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround fail, produce errors, cause
> rework, or hit a scale ceiling? Name the exact failure -- not "it's slow." Minimum 2 rows.
> "CSV export silently truncates rows above 65,536 with no error message" passes.
> "Manual is slow" fails.

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

| Artifact                                        | Populated? (Y / N) | If N: action required                            |
|-------------------------------------------------|--------------------|--------------------------------------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)   |                    | Return to Stage 1. Add actor column for each FM. |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04) |                    | Return to Stage 1. Add trigger threshold per FM. |

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

## V-05 -- All new signals combined axis

**Axis**: A-26 (axis vocabulary in heading subtitles) + A-27 (decision-question gate heading) +
A-28 (criterion IDs in checklist item labels) + remediation dispatch column + COMMAND phrasing.
Minimal combination of session 2's four new patterns on top of the full R11 180/180 scaffold.
Rule labels: `STATUS QUO LOCK RULE [A-16]`, `STATUS QUO CITATION RULE [A-19]`.
**Hypothesis**: All three v12 candidate criteria (A-26, A-27, A-28) can be satisfied simultaneously
in a single template that still clears all 25 v11 criteria. The v12 rubric note confirms A-26 and
A-27 are achievable from R11 V-03 patterns; A-28 is a traceability extrapolation. V-05 tests
whether carrying all three produces any structural tension or whether they are fully orthogonal.
**Predicted score**: 180/180 (v11); 195/195 (v12) -- first predicted perfect score on v12.

---

```
## FAIL-FIRST DECLARATION -- NAMING THE UNNAMED COMPETITOR

Every feature competes against an unnamed competitor: the current workaround. It wins by
default unless teams can name specific conditions under which it fails. This analysis names
the unnamed competitor and answers one question: when does the status quo lose?

[FAIL-FIRST RULE]: ENUMERATE failure modes before switching costs or defeat conditions. Every
DC row must trace to a documented FM row. Nothing else is worth analyzing until the unnamed
competitor's failure modes are on record.

Bridge artifacts required before defeat conditions are authored:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering condition

---

## SECTION 1 -- THE UNNAMED COMPETITOR'S WEAKNESSES: FAILURE MODE INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the current workaround breaks, produces
errors, causes rework, or hits a scale ceiling. ASSIGN an FM-[N] identifier to each row.
MINIMUM 2 rows. REJECT generic descriptions -- "slow" or "manual" alone fails; "CSV export
silently truncates rows at 65,536 with no error message" passes.

> **STATUS QUO LOCK RULE [A-16]**: ASSIGN all FM-[N] identifiers in this table first.
> NO FM-[N] reference may appear in any later section without a corresponding row assigned here.

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

[BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE AUTHORING SECTIONS 2 THROUGH 5.
Both rows must show Y. If either is N, DO NOT PROCEED -- return to Section 1 and complete
the missing artifact, then return to this gate.

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

> **[UNIT RULE]**: EVERY estimate must carry a number and a unit. "Significant" without a
> number is REJECTED.

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

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4 trigger
mapping. CITE the FM-[N] driving each. "Teams switch when they see the value" fails -- every
DC row must name a testable threshold.

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

### V-01: A-27 gate heading form

`### BRIDGE COMPLETION GATE -- ALL ARTIFACTS POPULATED?` satisfies A-22 (named structural block
in position) and A-27 (binary decision question in heading line). The interrogative appended via
`--` separator is the minimal form: gate heading + decision question without changing the naming
vocabulary. A-25 is carried separately as the `[BRIDGE COMPLETION COMMAND]` directive inside the
block -- V-01 confirms A-27 and A-25 are independently satisfied (heading question vs. internal
command directive addressing different structural layers).

### V-02: A-26 axis vocabulary distribution

Axis vocabulary appears in two heading subtitle positions: `-- NAMING THE UNNAMED COMPETITOR` on
the FAIL-FIRST heading and `-- THE UNNAMED COMPETITOR'S WEAKNESSES:` on the FM Inventory heading.
Both are in the heading line, not prose blocks below. Domain-prefixed A-23 rule labels carry the
same vocabulary: `UNNAMED COMPETITOR LOCK RULE [A-16]`, `UNNAMED COMPETITOR CITATION RULE [A-19]`.
Gate heading `-- READY TO PROCEED?` adds A-27. V-02 is the cleanest single-axis test of A-26.

### V-03: A-28 checklist traceability form

Checklist items WITHOUT criterion ID prefix satisfy A-18 (binary + full coverage) but fail A-28.
V-03 checklist items LACK the `C-0N:` prefix despite carrying full binary coverage -- this is a
deliberate control: V-03 tests whether the standard lifecycle form (no prefix) scores 180/180,
confirming A-28 is a new criterion and not already present by default. The structural contrast
between V-03 (no A-28) and V-05 (A-28 present) enables clean scoring discrimination.

### V-04: Remediation dispatch column

The three-column gate verdict table (`Artifact | Populated? | If N: action required`) is the V-04
excess signal from R11 session 1. V-04 session 2 keeps the three-column form and pairs it with
the heading-as-directive A-25 form proven in R11 V-04. The remediation column prescribes the
exact action at the row level: "Return to Stage 1. Add actor for every FM row." An author with N
in any row has an immediate return path without re-reading instructions.

### V-05: Predicted 195/195 on v12

V-05 is the first variation predicted to score 195/195 on v12. It carries:
- A-26: `-- NAMING THE UNNAMED COMPETITOR` (FAIL-FIRST) + `-- THE UNNAMED COMPETITOR'S
  WEAKNESSES:` (FM Inventory)
- A-27: `## BRIDGE COMPLETION GATE -- READY TO PROCEED?` (decision question in gate heading)
- A-28: All five checklist items carry `C-0N:` prefix
- Remediation column in gate table
- COMMAND phrasing throughout
- `STATUS QUO LOCK RULE [A-16]` + `STATUS QUO CITATION RULE [A-19]` (domain-prefix A-23 form)

If scoring confirms A-28 pass in V-05 and A-28 fail in V-03, the v12 rubric's A-28 criterion
is validated as real and its scoring threshold is the `C-0N:` prefix on all five checklist items.
