# scout-inertia -- Quest Variate R12

**Rubric**: v12 (ceiling 195 = 100 essential base + 19 advanced criteria x 5 pts)
**Date**: 2026-03-17
**Previous round**: R11 all 5 variations predicted 180/180 (A-23+A-24+A-25 confirmed across four label forms)
**R12 target**: First 195/195 candidate
**New criteria**: A-26 (axis vocabulary in section heading subtitles) + A-27 (decision-question bridge gate heading) + A-28 (criterion IDs in trailing checklist item labels)

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Inertia framing | New "inertia threat" vocabulary family for A-26; "READY TO PROCEED?" confirmed interrogative for A-27; A-28 confirmed retroactive from R11 (all R11 checklist items already carry C-01: labels) |
| V-02 | Lifecycle emphasis | Stage-based structure; "status quo as unnamed competitor" vocabulary for A-26; "ALL BRIDGE ARTIFACTS COMPLETE?" as new A-27 interrogative; bracket-suffix A-23 |
| V-03 | Phrasing register | Full COMMAND phrasing; "unnamed competitor failure surface" vocabulary for A-26; "BOTH BRIDGES BUILT?" as new A-27 interrogative; domain-prefix A-23 ("INERTIA THREAT RULE [A-16]") |
| V-04 | Output format + Inertia framing | Consolidated triple-block bridge; "incumbent workaround" vocabulary for A-26; A-25 and A-27 co-located in single sub-section heading ("CONFIRM -- ALL ARTIFACTS COMPLETE?") |
| V-05 | All axes | COMMAND phrasing + "default competitor" vocabulary for A-26; "PASS BEFORE CONTINUING?" as new A-27 interrogative; new domain-prefix A-23 ("INERTIA LOCK RULE [A-16]"); all three new criteria fire simultaneously |

---

## R12 Design Notes

### A-26 -- Five vocabulary families tested

A-26 requires the template's declared analytical axis vocabulary to appear in the subtitle text of
both the FAIL-FIRST heading and the FM Inventory heading. R11 V-03 confirmed one vocabulary family
("status quo competitor": "-- THE UNNAMED COMPETITOR" and "-- THE STATUS QUO'S VULNERABILITIES:").
R12 tests five distinct vocabulary families, each declared in the FAIL-FIRST body and propagated
into both headings:

1. **Inertia threat** (V-01): "-- THE INERTIA THREAT" + "-- THE INERTIA THREAT'S STRUCTURAL WEAKNESSES:"
2. **Status quo as unnamed competitor** (V-02): "-- THE STATUS QUO AS UNNAMED COMPETITOR" + "-- WHERE THE STATUS QUO BREAKS:"
3. **Unnamed competitor failure surface** (V-03): "-- THE UNNAMED COMPETITOR" + "-- THE UNNAMED COMPETITOR'S FAILURE SURFACE:"
4. **Incumbent workaround** (V-04): "-- THE INCUMBENT WORKAROUND" + "-- THE INCUMBENT'S VULNERABILITIES:"
5. **Default competitor** (V-05): "-- THE DEFAULT COMPETITOR" + "-- THE DEFAULT COMPETITOR'S BREAKING POINTS:"

A-26 stress test: does the criterion pass on any internally coherent axis vocabulary, or is it
constrained to the specific R11 V-03 vocabulary? All five R12 families are structurally distinct.
R12 scoring determines whether A-26 is vocabulary-agnostic (pass on any coherent family) or
vocabulary-constrained (requires the specific "status quo competitor" terms).

### A-27 -- Five interrogative forms tested

A-27 requires the bridge completion gate heading to carry a binary decision question. R11 V-03
confirmed "-- READY TO PROCEED?" R12 tests four additional interrogative forms:

1. **"READY TO PROCEED?"** (V-01): Baseline confirmed form from R11 V-03.
2. **"ALL BRIDGE ARTIFACTS COMPLETE?"** (V-02): Artifact-inventory framing -- questions whether artifacts exist.
3. **"BOTH BRIDGES BUILT?"** (V-03): Structural completeness framing -- questions bridge construction state.
4. **Combined A-25+A-27 heading** (V-04): `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?` -- directive and decision question in single heading; A-25 and A-27 co-located.
5. **"PASS BEFORE CONTINUING?"** (V-05): Gate-pass framing -- questions whether the gate condition is satisfied.

A-27 independence note: A-27 is independent of A-25. Forms 1-3 and 5 implement A-25 as a
separate inline command directive, then add A-27 as the heading-level question. Form 4 (V-04)
tests whether a single heading element can satisfy both simultaneously.

### A-28 -- Retroactive confirmation from R11

A-28 requires criterion IDs (C-01 through C-05) in trailing checklist item labels. Examining
R11 V-01 through V-05 completeness sections: all five variations carry "C-01:", "C-02:", "C-03:",
"C-04:", "C-05:" prefixes in their checklist item labels (e.g.,
`| C-01: Workaround named specifically with role and ongoing cost (number + unit) |`).
A-28 was present in all R11 variations before the criterion was named -- parallel to A-24 being
retroactively confirmed from R10 data. R12 carries this pattern forward unchanged. R12 scoring
will confirm whether the R11 variations earn A-28 retroactively at 195/195.

### R11 incoming state on new criteria

From R11 criterion matrix:
- V-03: A-26 PASS (both headings carry subtitle), A-27 PASS ("READY TO PROCEED?"), A-28 PASS (C-01: labels present)
- V-05: A-26 PARTIAL (FAIL-FIRST heading has subtitle, FM Inventory heading does not), A-27 FAIL, A-28 PASS
- V-01, V-02, V-04: A-26 FAIL (FM Inventory heading has no subtitle), A-27 FAIL, A-28 PASS

R12 fixes the A-26 FM Inventory subtitle gap and the A-27 gate heading gap across all five
variations. A-28 requires no change -- it is confirmed as already present.

---

## V-01 -- Inertia framing axis

**Axis**: New "inertia threat" vocabulary family for A-26; bridge gate heading uses confirmed
"READY TO PROCEED?" for A-27; bracket-prefix A-23; inline `[BRIDGE COMPLETION COMMAND]`
directive for A-25. Minimal structural change from R11 V-01 -- only the heading subtitles
and gate heading are modified.
**Hypothesis**: A-26 is vocabulary-agnostic. "Inertia threat" vocabulary satisfies A-26 as
long as the declared axis terms appear in both headings. A-27 uses the R11 V-03 confirmed
form to isolate the A-26 vocabulary variable. A-28 passes retroactively with no change to
checklist structure.
**Predicted score**: 195/195

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

The current workaround is the inertia threat. It has no vendor, no demo, and no champion --
but it wins by default unless teams have a specific, observable reason to leave. The inertia
threat's strength is structural: already deployed, already paid for, already familiar. Map its
failure modes first. Defeat conditions and switching cost thresholds derive only from documented
failures. No defeat condition is valid without a documented failure mode behind it.

Bridge artifacts required before defeat conditions are authored:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the specific role experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering condition

---

## SECTION 1 -- THE INERTIA THREAT'S STRUCTURAL WEAKNESSES: FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the inertia threat (current workaround) fail,
> produce errors, cause rework, or hit a scale ceiling? Name each failure mode precisely --
> not "it is slow" or "it is manual." Minimum 2 rows required.
> "CSV export silently truncates rows above 65,536 with no error message" passes;
> "manual is slow" fails.

> **[A-16 PRIMARY KEY RULE]**: Assign all FM-[N] identifiers in this table first. No FM-[N]
> may appear in any later section of this document without a corresponding row assigned here.
> Every downstream reference must trace back to a row in this inventory.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger condition (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|---------------------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                                       |                             |
| FM-2   |                                                                                       |                                    |                                       |                             |

---

## Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

Map each failure mode to the specific role that experiences it. This bridge closes the chain
from failure documentation to role-level attribution required by R-02.

| FM-[N] | Role experiencing the failure (e.g., data-ops team) | Role-level consequence |
|--------|-----------------------------------------------------|------------------------|
| FM-1   |                                                     |                        |
| FM-2   |                                                     |                        |

---

## Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

Map each failure mode to its triggering condition and measurable threshold. This bridge closes
the chain from failure documentation to defeat condition construction required by C-04.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

---

## BRIDGE COMPLETION GATE -- READY TO PROCEED?

[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding to Sections 2 through 5.
Do not author the workaround profile or defeat conditions unless both rows below show Y.
An incomplete bridge means defeat conditions lack their actor and trigger chains.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

If either shows N: return to Section 1 and complete the missing artifact before proceeding.

---

## SECTION 2 -- WORKAROUND PROFILE

> **C-01 question**: What is the exact name of the inertia threat -- the specific tool, file
> type, or procedure currently in use? Not "a manual process." Who performs it? What is the
> ongoing cost per week or sprint, stated as a number with a unit?

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 3 -- SWITCHING COST

> **C-02 question**: What does it cost to abandon the inertia threat and adopt this feature?
> Identify at least two cost categories. Every estimate must carry a number and a unit --
> "significant" without a number fails C-02.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 4 -- THREAT ASSESSMENT

> **C-03 question**: How strong is the inertia threat? Declare an explicit score. The default
> is HIGH -- the inertia threat always starts with home-field advantage. Deviations from HIGH
> require a specific quantified condition; a qualitative judgment does not justify deviation.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

> **C-04 question**: Under what specific, testable conditions do teams abandon the inertia
> threat in favor of this feature? Derive each condition from the triggers in Q4. Every
> condition must be falsifiable -- "teams switch when they see the value" fails. Cite the
> FM-[N] driving each defeat condition.

> **[A-19 REFERENTIAL INTEGRITY RULE]**: Every FM-[N] cited in this table must have an
> assigned row in Section 1 (FM Inventory). Do not reference FM identifiers not assigned
> above. Verify before filling each row.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type or segment |
|--------|------------------------------------------|-------------------|------------------------------------------------------|----------------------|
| DC-1   |                                          |                   |                                                      |                      |
| DC-2   |                                          |                   |                                                      |                      |

---

## SECTION 6 -- COMPLETENESS CHECKLIST

| Criterion                                                                                      | Satisfied? (Y / N) |
|------------------------------------------------------------------------------------------------|--------------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                 |                    |
| C-02: At least two switching cost categories quantified with numbers and units                 |                    |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition) |                    |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Section 1     |                    |
| C-05: At least two specific, non-generic failure modes documented in Section 1                |                    |
```

---

## V-02 -- Lifecycle emphasis axis

**Axis**: Stage-based structure (STAGE 1 through STAGE 6); "status quo as unnamed competitor"
vocabulary family for A-26; "ALL BRIDGE ARTIFACTS COMPLETE?" as new A-27 interrogative form;
bracket-suffix A-23 (`PRIMARY KEY RULE [A-16]`, `CITATION INTEGRITY RULE [A-19]`); inline
`[BRIDGE COMPLETION COMMAND]` for A-25.
**Hypothesis**: Stage-boundary enforcement (Stage 2 gate before Stage 3 opens) combined with
axis vocabulary in both stage headings satisfies A-26 within a lifecycle-emphasis frame.
"ALL BRIDGE ARTIFACTS COMPLETE?" interrogative tests whether artifact-inventory framing satisfies
A-27 as clearly as the "READY TO PROCEED?" readiness framing. Bracket-suffix A-23 confirmed
from R11 V-02.
**Predicted score**: 195/195

---

```
## FAIL-FIRST DECLARATION -- THE STATUS QUO AS UNNAMED COMPETITOR

Every feature decision must first answer: why does the status quo lose? The status quo is the
unnamed competitor -- no name, no sales team, no roadmap. It persists because switching costs
are real and failure modes are invisible. This analysis makes both visible. Map the status quo's
failure modes before writing a single defeat condition.

Authoring sequence:
- Stage 1 -- FAILURE MODE INVENTORY (C-05): where the status quo breaks
- Stage 2 -- BRIDGE STAGE: Q3 (FM->actor, closes C-05 -> R-02) + Q4 (FM->trigger, closes C-05 -> C-04) + completion gate
- Stage 3 -- WORKAROUND PROFILE (C-01): specific tool, role, ongoing cost
- Stage 4 -- SWITCHING COST (C-02): quantified cost to abandon the status quo
- Stage 5A -- THREAT ASSESSMENT (C-03): inertia threat score
- Stage 5B -- DEFEAT CONDITIONS (C-04): conditions under which the status quo loses
- Stage 6 -- COMPLETENESS CHECK

The Stage 2 gate must show Y for both bridge artifacts before Stage 3 is authored.

---

## STAGE 1 -- WHERE THE STATUS QUO BREAKS: FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the status quo (current workaround) fail, produce
> errors, cause rework, or hit a scale ceiling? Name each failure mode precisely -- not generic
> pain. Minimum 2 rows. "CSV export silently truncates rows above 65,536 with no error message"
> passes; "manual is slow" fails.

> **PRIMARY KEY RULE [A-16]**: Assign all FM-[N] identifiers in this table first. No FM-[N]
> may appear in Stage 5B or any other downstream stage without a corresponding row assigned
> here. Assign identifiers here before writing any downstream reference.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## STAGE 2 -- BRIDGE STAGE

### Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

Map each failure mode to the specific role experiencing it.

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

### Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

Map each failure mode to its triggering condition and measurable threshold.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

### STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?

[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding to Stage 3. If either row
shows N, do not advance. Return to Stage 1 and complete the missing artifact.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

---

## STAGE 3 -- WORKAROUND PROFILE

> **C-01 question**: What is the exact name of the status quo workaround -- the specific tool,
> file type, or procedure name? Not "a manual process." Who performs it? What is the ongoing
> cost per week or sprint, stated as a number with a unit?

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## STAGE 4 -- SWITCHING COST

> **C-02 question**: What does it cost to abandon the status quo and adopt this feature?
> Identify at least two cost categories. Every estimate must carry a number and a unit --
> "significant" fails C-02.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

> **C-03 question**: How strong is the status quo as unnamed competitor? Declare the inertia
> threat score. Default is HIGH. Deviations require a specific quantified condition -- a
> qualitative statement does not justify deviation.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## STAGE 5B -- DEFEAT CONDITIONS

> **C-04 question**: Under what specific, testable conditions do teams abandon the status quo
> in favor of this feature? Each condition must be falsifiable -- derive from Q4 triggers. Cite
> the FM-[N] driving each condition.

> **CITATION INTEGRITY RULE [A-19]**: Every FM-[N] cited in this table must have an assigned
> row in Stage 1 (FM Inventory). Do not reference FM identifiers not assigned in Stage 1.
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

## V-03 -- Phrasing register axis

**Axis**: Full COMMAND phrasing throughout; "unnamed competitor failure surface" vocabulary
family for A-26; "BOTH BRIDGES BUILT?" as new A-27 interrogative form; domain-prefix bracket-
suffix A-23 with "INERTIA THREAT RULE" domain vocabulary (`INERTIA THREAT RULE [A-16]`,
`INERTIA THREAT CITATION RULE [A-19]`).
**Hypothesis**: COMMAND phrasing is compatible with A-26 axis vocabulary subtitles -- the
heading subtitle carries the declared axis vocabulary regardless of the body's phrasing register.
"BOTH BRIDGES BUILT?" tests a structural-completeness interrogative form for A-27. Domain-prefix
A-23 with a new domain vocabulary ("INERTIA THREAT RULE") extends the A-23 form taxonomy beyond
the R11 V-03 "STATUS QUO" domain prefix -- scoring confirms domain-prefix A-23 is vocabulary-
agnostic within the label.
**Predicted score**: 195/195

---

```
## FAIL-FIRST DECLARATION -- THE UNNAMED COMPETITOR

[FAIL-FIRST RULE]: The unnamed competitor is the current workaround. It competes without
a name, a vendor, or a roadmap. It wins by default. This analysis exposes the unnamed
competitor's failure surface -- the specific ways it breaks -- before deriving any defeat
conditions. Every DC row must trace to a row in the failure surface inventory.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering condition

---

## SECTION 1 -- THE UNNAMED COMPETITOR'S FAILURE SURFACE: FAILURE MODE INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the unnamed competitor (current
workaround) breaks, produces errors, causes rework, or hits a scale ceiling. ASSIGN an FM-[N]
identifier to each row. MINIMUM 2 rows. REJECT generic descriptions -- "slow" or "manual"
alone fails; "CSV export silently truncates rows at 65,536 with no error message" passes.

> **INERTIA THREAT RULE [A-16]**: ASSIGN all FM-[N] identifiers here first. NO FM-[N]
> reference may appear in any later section without a corresponding row assigned in this
> table. The failure surface inventory is the sole source of FM identifiers.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

[BRIDGE Q3 COMMAND]: MAP each FM-[N] to the specific role experiencing the failure.
VERIFY that each actor name is a specific role title, not "users" or "the team."

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

---

## Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

[BRIDGE Q4 COMMAND]: MAP each FM-[N] to its triggering condition. QUANTIFY the measurable
threshold that activates the failure.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

---

## BRIDGE COMPLETION GATE -- BOTH BRIDGES BUILT?

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING SECTIONS 2
THROUGH 5. If either row is N, DO NOT PROCEED. Return to Section 1 and complete the missing
bridge artifact. An incomplete bridge leaves defeat conditions without actor or trigger chains.

| Bridge artifact                                | Built? (Y / N) |
|------------------------------------------------|----------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                |

---

## SECTION 2 -- WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific unnamed competitor -- the exact tool name, file type, or
procedure. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost
with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 3 -- SWITCHING COST

[C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a number
and a unit. NAME the role bearing each cost.

> **[UNIT RULE]**: EVERY estimate must carry a number and a unit. "Significant" or
> "substantial" without a number is REJECTED.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 4 -- THREAT ASSESSMENT

[C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH -- the unnamed competitor
always starts with home-field advantage. IF deviating from HIGH, STATE a specific quantified
condition; a qualitative judgment ("low friction") is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
trigger mapping. CITE the FM-[N] driving each condition. "Teams switch when they see the
value" fails -- every DC row must name a testable, measurable condition.

> **INERTIA THREAT CITATION RULE [A-19]**: EVERY FM-[N] cited in this table MUST have an
> assigned row in Section 1 (FM Inventory). DO NOT introduce FM references not assigned above.
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
| C-05: At least two specific, non-generic failure modes in Section 1                           |               |
```

---

## V-04 -- Output format + Inertia framing (combined)

**Axis**: Consolidated triple-block bridge from R11 V-04 (Q3 table, Q4 table, and bridge gate
verdict as sub-sections of a single Stage 2); "incumbent workaround" vocabulary family for A-26;
A-25 and A-27 co-located in single sub-section heading: `### [BRIDGE COMPLETION COMMAND]: CONFIRM
-- ALL ARTIFACTS COMPLETE?`.
**Hypothesis**: The sub-section heading form for A-25 (confirmed in R11 V-04) can simultaneously
satisfy A-27 if the heading line carries a decision question alongside the command label. A heading
of `[BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?` is a named structural element
(satisfies A-25) whose text contains a binary decision question (satisfies A-27). Testing whether
the combined heading approach satisfies both independently-defined criteria.
**Predicted score**: 195/195

---

```
## FAIL-FIRST DECLARATION -- THE INCUMBENT WORKAROUND

The incumbent workaround is this feature's primary competition. It holds an incumbency advantage:
sunk investment, team familiarity, and no switching cost to remain. This analysis maps the
incumbent's vulnerabilities -- its specific failure modes -- before deriving defeat conditions.
Defeat conditions not grounded in documented failures are hypotheses, not analysis.

Bridge artifacts required before Stage 5B (Defeat Conditions):
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering condition

Authoring order enforced by stage structure: Stage 1 before Stage 2. Stage 2 gate before Stage 3.

---

## STAGE 1 -- THE INCUMBENT'S VULNERABILITIES: FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the incumbent workaround fail, produce errors,
> cause rework, or hit a scale ceiling? Name each failure mode precisely -- not generic pain.
> Minimum 2 rows. "CSV export silently truncates rows above 65,536 with no error message"
> passes; "manual is slow" fails.

> **[A-16 PRIMARY KEY CONSTRAINT]**: Assign all FM-[N] identifiers in this table first.
> No FM-[N] identifier may appear in Stage 5B or any downstream stage without a corresponding
> row assigned here.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## STAGE 2 -- BRIDGE STAGE

### Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level consequence |
|--------|------------------------------------|------------------------|
| FM-1   |                                    |                        |
| FM-2   |                                    |                        |

### Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?

| Artifact                                       | Populated? (Y / N) | If N: action required                           |
|------------------------------------------------|--------------------|------------------------------------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    | Return to Stage 1 and complete actor mapping    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    | Return to Stage 1 and complete trigger mapping  |

Do not proceed to Stage 3 unless both rows show Y.

---

## STAGE 3 -- WORKAROUND PROFILE

> **C-01 question**: What is the exact name of the incumbent workaround -- the specific tool,
> file type, or procedure name? Not "a manual process." Who performs it? What is the ongoing
> cost per week or sprint, with a number and a unit?

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## STAGE 4 -- SWITCHING COST

> **C-02 question**: What does it cost to displace the incumbent workaround and adopt this
> feature? Identify at least two cost categories. Every estimate must carry a number and a
> unit -- "significant" fails C-02.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

> **C-03 question**: How strong is the incumbent workaround as an inertia threat? Declare the
> inertia threat score. Default is HIGH. Deviations require a specific quantified condition;
> a qualitative statement does not justify deviation.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## STAGE 5B -- DEFEAT CONDITIONS

> **C-04 question**: Under what specific, testable conditions do teams displace the incumbent
> workaround in favor of this feature? Each condition must be falsifiable -- derive from Q4
> triggers and cite the FM-[N] driving it.

> **[A-19 CITATION INTEGRITY CONSTRAINT]**: Every FM-[N] cited in this table must have an
> assigned row in Stage 1 (FM Inventory). Do not reference FM identifiers not assigned in
> Stage 1. Verify before filling each row.

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

**Axis**: COMMAND phrasing + "default competitor" vocabulary family for A-26 + "PASS BEFORE
CONTINUING?" as A-27 interrogative form + new domain-prefix A-23 ("INERTIA LOCK RULE [A-16]",
"INERTIA LOCK CITATION RULE [A-19]") + `[BRIDGE COMPLETION COMMAND]` A-25 directive. Extends
R11 V-05 by applying A-26 vocabulary to the FM Inventory heading subtitle and adding the A-27
interrogative to the gate heading.
**Hypothesis**: The combined-axes scaffold from R11 V-05 (180/180) carries all three new
criteria with targeted additions: the FM Inventory heading gains an axis vocabulary subtitle
(A-26 FM gap from R11), the bridge gate heading gains "PASS BEFORE CONTINUING?" (A-27 gap from
R11), and A-28 is confirmed retroactive. A new domain vocabulary ("INERTIA LOCK") extends the
domain-prefix A-23 form taxonomy without disrupting any other criterion. No structural
interference between COMMAND phrasing, axis vocabulary headings, gate interrogative, and new
domain prefix is expected.
**Predicted score**: 195/195

---

```
## [FAIL-FIRST DECLARATION] -- THE DEFAULT COMPETITOR

The default competitor is the current workaround. It does not compete on features -- it competes
on inertia. Teams stay not because the workaround is good but because the cost to leave is
invisible. Enumerate the default competitor's breaking points first. Every DC row must trace to
a documented breaking point. Nothing else is worth analyzing until the default competitor's
failure modes exist on paper.

Bridge artifacts (required before Defeat Conditions):
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the specific actor experiencing the failure
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to the triggering condition

Authoring order: Section 1 -> Q3/Q4 -> BRIDGE COMPLETION GATE -> Section 2 -> Section 3 ->
Section 4 -> Section 5 -> Completeness Check. Section 1 must have at least two rows
before anything else is authored.

---

## SECTION 1 -- THE DEFAULT COMPETITOR'S BREAKING POINTS: FAILURE MODE INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the default competitor (current workaround)
breaks, produces errors, causes rework, or hits a scale ceiling. ASSIGN FM-[N] identifiers.
MINIMUM 2 rows. REJECT generic descriptions -- "slow" or "manual" alone fails;
"CSV export silently truncates rows at 65,536 with no error message" passes.

> **INERTIA LOCK RULE [A-16]**: ASSIGN all FM-[N] identifiers here first. NO FM-[N] reference
> may appear in any later section of this document without a corresponding row assigned in this
> table. The breaking points inventory is the sole source of FM identifiers in this document.

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

## BRIDGE COMPLETION GATE -- PASS BEFORE CONTINUING?

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING SECTIONS 2
THROUGH 5. If either row is N, DO NOT PROCEED. Return to Section 1 and complete the missing
bridge artifact. An incomplete bridge leaves defeat conditions without their actor and trigger
chain evidence.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

---

## SECTION 2 -- WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific default competitor -- the exact tool name, file type, or
procedure. NOT "a manual process." NAME the role performing it -- the default competitor's
current operator. QUANTIFY the ongoing cost with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it (e.g., data-ops team) | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|------------------------------------------|-----------------------------------|------------------------------------------|
|                                                          |                                          |                                   |                                          |

---

## SECTION 3 -- SWITCHING COST

[C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a number
and a unit. NAME the role bearing each cost. The default competitor holds a switching cost
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

[C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH -- the default competitor
always starts with home-field advantage. IF deviating from HIGH, STATE a specific quantified
condition. A qualitative judgment is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4 trigger
mapping. CITE the FM-[N] driving each condition. "Teams switch when they see the value" fails --
every DC row must name a testable, measurable condition.

> **INERTIA LOCK CITATION RULE [A-19]**: EVERY FM-[N] cited in this table MUST have an assigned
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
| A-10 | PASS: FAIL-FIRST DECLARATION section | PASS: FAIL-FIRST DECLARATION section | PASS: [FAIL-FIRST RULE] label | PASS: FAIL-FIRST DECLARATION section | PASS: [FAIL-FIRST DECLARATION] label |
| A-11 | PASS: 5 labeled questions (C-01 through C-05) | PASS: 5 labeled questions (C-01 through C-05) | PASS: 5 COMMAND prompts (C-01 through C-05) | PASS: 5 labeled questions (C-01 through C-05) | PASS: 5 COMMAND prompts (C-01 through C-05) |
| A-12 | PASS: FAIL-FIRST names Q3/Q4 with chain refs | PASS: FAIL-FIRST names Q3/Q4 with chain refs | PASS: FAIL-FIRST names Q3/Q4 with chain refs | PASS: FAIL-FIRST names Q3/Q4 with chain refs | PASS: FAIL-FIRST names Q3/Q4 with chain refs |
| A-13 | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular |
| A-14 | PASS: SECTION 1 FM Inventory, FM-[N] first column | PASS: STAGE 1 FM Inventory, FM-[N] first column | PASS: SECTION 1 FM Inventory, FM-[N] first column | PASS: STAGE 1 FM Inventory, FM-[N] first column | PASS: SECTION 1 FM Inventory, FM-[N] first column |
| A-15 | PASS: SECTION 6 COMPLETENESS CHECKLIST trailing | PASS: STAGE 6 COMPLETENESS CHECK trailing | PASS: COMPLETENESS CHECK trailing | PASS: STAGE 6 COMPLETENESS CHECK trailing | PASS: COMPLETENESS CHECK trailing |
| A-16 | PASS: `[A-16 PRIMARY KEY RULE]` bracket-prefix | PASS: `PRIMARY KEY RULE [A-16]` bracket-suffix | PASS: `INERTIA THREAT RULE [A-16]` domain-prefix bracket-suffix | PASS: `[A-16 PRIMARY KEY CONSTRAINT]` bracket-prefix variant | PASS: `INERTIA LOCK RULE [A-16]` domain-prefix bracket-suffix |
| A-17 | PASS: C-01 through C-05 each have labeled question | PASS: C-01 through C-05 each have labeled question | PASS: C-01 through C-05 each have COMMAND label | PASS: C-01 through C-05 each have labeled question | PASS: C-01 through C-05 each have COMMAND label |
| A-18 | PASS: Section 6 Y/N binary, all 5 criteria | PASS: Stage 6 Y/N binary, all 5 criteria | PASS: COMPLETENESS CHECK Y/N binary, all 5 criteria | PASS: Stage 6 Y/N binary, all 5 criteria | PASS: COMPLETENESS CHECK Y/N binary, all 5 criteria |
| A-19 | PASS: `[A-19 REFERENTIAL INTEGRITY RULE]` bracket-prefix | PASS: `CITATION INTEGRITY RULE [A-19]` bracket-suffix | PASS: `INERTIA THREAT CITATION RULE [A-19]` domain-prefix bracket-suffix | PASS: `[A-19 CITATION INTEGRITY CONSTRAINT]` bracket-prefix variant | PASS: `INERTIA LOCK CITATION RULE [A-19]` domain-prefix bracket-suffix |
| A-20 | PASS: Ongoing cost (e.g., 2 hours/week); Duration (e.g., 18 months); Estimate (e.g., 3 days); Role (e.g., data-ops team); Trigger (e.g., file > 10MB); Frequency (e.g., 2x/sprint) | PASS: same column set with inline examples | PASS: same column set with inline examples | PASS: same column set with inline examples | PASS: same column set with inline examples |
| A-21 | PASS: DC threshold column `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column `(e.g., >10MB, >3 failures/week)` |
| A-22 | PASS: BRIDGE COMPLETION GATE block between Section 1 and Section 2 | PASS: STAGE 2 COMPLETION GATE block between Stage 1 and Stage 3 | PASS: BRIDGE COMPLETION GATE block between Section 1 and Section 2 | PASS: `[BRIDGE COMPLETION COMMAND]: CONFIRM` sub-section between Stage 1 and Stage 3 | PASS: BRIDGE COMPLETION GATE block between Section 1 and Section 2 |
| A-23 | PASS: `[A-16 PRIMARY KEY RULE]` + `[A-19 REFERENTIAL INTEGRITY RULE]` (bracket-prefix) | PASS: `PRIMARY KEY RULE [A-16]` + `CITATION INTEGRITY RULE [A-19]` (bracket-suffix) | PASS: `INERTIA THREAT RULE [A-16]` + `INERTIA THREAT CITATION RULE [A-19]` (domain-prefix bracket-suffix, new domain) | PASS: `[A-16 PRIMARY KEY CONSTRAINT]` + `[A-19 CITATION INTEGRITY CONSTRAINT]` (bracket-prefix variant label) | PASS: `INERTIA LOCK RULE [A-16]` + `INERTIA LOCK CITATION RULE [A-19]` (domain-prefix bracket-suffix, new domain) |
| A-24 | PASS: `>10MB` (size) + `>3 failures/week` (frequency) -- two distinct threshold types | PASS: same dual-type | PASS: same dual-type | PASS: same dual-type | PASS: same dual-type |
| A-25 | PASS: `[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding...` inline directive | PASS: `[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding...` inline directive | PASS: `[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED...` all-caps directive | PASS: `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?` sub-section heading serves as directive | PASS: `[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED...` all-caps directive |
| A-26 | PASS: `FAIL-FIRST DECLARATION -- THE INERTIA THREAT` + `SECTION 1 -- THE INERTIA THREAT'S STRUCTURAL WEAKNESSES:` | PASS: `FAIL-FIRST DECLARATION -- THE STATUS QUO AS UNNAMED COMPETITOR` + `STAGE 1 -- WHERE THE STATUS QUO BREAKS:` | PASS: `FAIL-FIRST DECLARATION -- THE UNNAMED COMPETITOR` + `SECTION 1 -- THE UNNAMED COMPETITOR'S FAILURE SURFACE:` | PASS: `FAIL-FIRST DECLARATION -- THE INCUMBENT WORKAROUND` + `STAGE 1 -- THE INCUMBENT'S VULNERABILITIES:` | PASS: `[FAIL-FIRST DECLARATION] -- THE DEFAULT COMPETITOR` + `SECTION 1 -- THE DEFAULT COMPETITOR'S BREAKING POINTS:` |
| A-27 | PASS: `BRIDGE COMPLETION GATE -- READY TO PROCEED?` (confirmed form) | PASS: `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` (new form) | PASS: `BRIDGE COMPLETION GATE -- BOTH BRIDGES BUILT?` (new form) | PASS: `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?` (combined A-25+A-27 heading; decision question in heading text) | PASS: `BRIDGE COMPLETION GATE -- PASS BEFORE CONTINUING?` (new form) |
| A-28 | PASS: C-01: through C-05: in all checklist item labels (retroactive from R11) | PASS: C-01: through C-05: in all checklist item labels | PASS: C-01: through C-05: in all checklist item labels | PASS: C-01: through C-05: in all checklist item labels | PASS: C-01: through C-05: in all checklist item labels |
| **Predicted** | **195/195** | **195/195** | **195/195** | **195/195** | **195/195** |

---

## A-26 Vocabulary Family Taxonomy

| Family | FAIL-FIRST subtitle | FM Inventory subtitle | Variation |
|--------|--------------------|-----------------------|-----------|
| Inertia threat | `-- THE INERTIA THREAT` | `-- THE INERTIA THREAT'S STRUCTURAL WEAKNESSES:` | V-01 |
| Status quo as unnamed competitor | `-- THE STATUS QUO AS UNNAMED COMPETITOR` | `-- WHERE THE STATUS QUO BREAKS:` | V-02 |
| Unnamed competitor failure surface | `-- THE UNNAMED COMPETITOR` | `-- THE UNNAMED COMPETITOR'S FAILURE SURFACE:` | V-03 |
| Incumbent workaround | `-- THE INCUMBENT WORKAROUND` | `-- THE INCUMBENT'S VULNERABILITIES:` | V-04 |
| Default competitor | `-- THE DEFAULT COMPETITOR` | `-- THE DEFAULT COMPETITOR'S BREAKING POINTS:` | V-05 |

A-26 vocabulary coherence check: each family uses the same core noun across both headings
("inertia threat" / "status quo" / "unnamed competitor" / "incumbent workaround" / "default
competitor"). The coherence property is internal to the vocabulary family -- the FAIL-FIRST body
declares the term, the FAIL-FIRST heading subtitle carries it, and the FM Inventory heading
subtitle extends it with a domain-specific modifier ("structural weaknesses", "where it breaks",
"failure surface", "vulnerabilities", "breaking points").

## A-27 Interrogative Form Taxonomy

| Form | Gate heading | Variation |
|------|-------------|-----------|
| Readiness check | `BRIDGE COMPLETION GATE -- READY TO PROCEED?` | V-01 (confirmed from R11 V-03) |
| Artifact inventory | `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` | V-02 |
| Structural completeness | `BRIDGE COMPLETION GATE -- BOTH BRIDGES BUILT?` | V-03 |
| Combined directive+question | `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?` | V-04 |
| Gate-pass | `BRIDGE COMPLETION GATE -- PASS BEFORE CONTINUING?` | V-05 |

A-27 stress test: V-04's combined heading form differs structurally from V-01/V-02/V-03/V-05 --
the command label `[BRIDGE COMPLETION COMMAND]` leads the heading, and the decision question
follows within the same heading line. If A-27 requires only that a decision question appear
somewhere in the heading line, V-04 passes. If A-27 requires the gate heading to be primarily
decision-framed (question-leading rather than command-leading), V-04 may score differently.
R12 scoring will determine whether the combined heading satisfies A-27 independently of A-25.

## A-23 Domain-Prefix Form Taxonomy (updated)

| Form | A-16 label | A-19 label | Variations |
|------|-----------|-----------|------------|
| Bracket-prefix | `[A-16 PRIMARY KEY RULE]` | `[A-19 REFERENTIAL INTEGRITY RULE]` | V-01 |
| Bracket-suffix | `PRIMARY KEY RULE [A-16]` | `CITATION INTEGRITY RULE [A-19]` | V-02 |
| Domain-prefix bracket-suffix (INERTIA THREAT domain) | `INERTIA THREAT RULE [A-16]` | `INERTIA THREAT CITATION RULE [A-19]` | V-03 |
| Bracket-prefix variant label | `[A-16 PRIMARY KEY CONSTRAINT]` | `[A-19 CITATION INTEGRITY CONSTRAINT]` | V-04 |
| Domain-prefix bracket-suffix (INERTIA LOCK domain) | `INERTIA LOCK RULE [A-16]` | `INERTIA LOCK CITATION RULE [A-19]` | V-05 |

R12 adds two new domain prefixes ("INERTIA THREAT" in V-03, "INERTIA LOCK" in V-05) alongside
the R11 V-03 "STATUS QUO" prefix. Domain-prefix A-23 stress test expands: does the criterion
pass with any domain vocabulary prefix, confirming the label-content-only interpretation
(ID present anywhere in label text)?
