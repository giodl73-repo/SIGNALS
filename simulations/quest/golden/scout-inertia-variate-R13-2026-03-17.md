# scout-inertia -- Quest Variate R13

**Rubric**: v13 (ceiling 210 = 100 essential base + 22 advanced criteria x 5 pts)
**Date**: 2026-03-17
**Previous round**: R12 all 5 variations predicted 195/195 (A-26+A-27+A-28 confirmed across
five vocabulary families and five interrogative forms)
**R13 target**: First 210/210 candidate
**New criteria**: A-29 (criterion ID in per-criterion authoring prompt label) + A-30 (COMMAND-
register keyword in per-criterion prompt label) + A-31 (named structural rule in FAIL-FIRST
declaration body)

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Inertia framing | Blockquote-wrapped `> [C-0N COMMAND]:` form satisfies A-29+A-30; A-31 via minimal `[FAIL-FIRST RULE]` without criterion ID in label |
| V-02 | Lifecycle emphasis | Stage-based structure; inline `[C-0N COMMAND]:` in each stage; A-31 via bracket-suffix `FAIL-FIRST CONSTRAINT [A-31]` -- extends A-23 to FAIL-FIRST rule layer |
| V-03 | Phrasing register (reference form) | R12 V-03 scaffold carried forward; confirms `[C-0N COMMAND]:` + `[FAIL-FIRST RULE]` as the R13 reference form; 210/210 baseline |
| V-04 | Output format (consolidated bridge) | Inline `[C-0N COMMAND]:` form; A-31 via bracket-prefix `[A-31 FAIL-FIRST ORDERING RULE]` carrying criterion ID -- extends A-23 to FAIL-FIRST rule layer with bracket-prefix form |
| V-05 | All axes combined | `[C-0N COMMAND]:` throughout; A-31 via domain-prefix `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` -- extends the domain-prefix A-23 pattern established for FM Inventory rules to the FAIL-FIRST rule layer |

---

## R13 Design Notes

### A-29 -- Criterion ID in per-criterion authoring prompt label

A-29 requires the criterion ID (C-01 through C-05) to appear in each per-criterion authoring
prompt label. R12 V-01 through V-04 used forms like `> **C-05 question**:` and `> **C-01
question**:` which carry the criterion ID but in non-COMMAND register (register is "question"
or "prompt"). R12 V-03 and V-05 already used `[C-05 COMMAND]:` through `[C-04 COMMAND]:` forms,
confirming A-29 in the bracket-label context.

R13 stress test: does A-29 pass when the criterion ID appears in a blockquote-wrapped bracket
label (`> [C-05 COMMAND]:`), or does it require the bare inline bracket form? V-01 tests the
blockquote-bracket form; all other variations use inline bracket form.

### A-30 -- COMMAND-register keyword in per-criterion prompt label

A-30 requires the COMMAND keyword to appear in the bracket-label form of each per-criterion
authoring prompt. R12 V-03/V-05 confirmed `[C-0N COMMAND]:` as the canonical COMMAND-register
form. R13 applies this form across all five variations.

Key A-30 questions R13 answers:
1. Does blockquote wrapping (`> [C-05 COMMAND]:`) satisfy A-30 or does the bracket form need
   to be bare inline? (V-01 vs all others)
2. Does the COMMAND keyword need to come after the criterion ID (e.g., `[C-05 COMMAND]:`) or
   can it precede it? R13 uses criterion-ID-first order across all variations.
3. Is the COMMAND form compatible with stage-based lifecycle structure (V-02) and consolidated
   bridge output format (V-04)?

### A-31 -- Named structural rule in FAIL-FIRST declaration body

A-31 requires a named rule label in the FAIL-FIRST body. R12 V-03 confirmed `[FAIL-FIRST RULE]`
as a passing form; R12 V-05 used `[FAIL-FIRST DECLARATION]` as the section heading label
(not a body rule), which may not satisfy A-31 since A-31 requires a rule in the BODY, not the
heading. R13 tests four distinct A-31 rule label forms:

1. **Minimal label, no criterion ID** (V-01, V-03): `[FAIL-FIRST RULE]`
   - Satisfies A-31; does not additionally carry A-31 criterion ID in label
2. **Bracket-suffix with criterion ID** (V-02): `FAIL-FIRST CONSTRAINT [A-31]`
   - Satisfies A-31; extends A-23's criterion-ID-in-label pattern to the FAIL-FIRST rule layer
3. **Bracket-prefix with criterion ID** (V-04): `[A-31 FAIL-FIRST ORDERING RULE]`
   - Satisfies A-31; extends A-23 via bracket-prefix form to the FAIL-FIRST layer
4. **Domain-prefix with criterion ID** (V-05): `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]`
   - Satisfies A-31; extends the domain-prefix A-23 pattern (established in R12 V-03 for FM
     Inventory rules as "INERTIA THREAT RULE [A-16]") to the FAIL-FIRST rule layer

A-31 + A-23 interaction: the A-31 rubric pass condition notes that "once the A-31 rule label
exists and carries the A-31 criterion ID in its label text, it also satisfies the A-23 criterion-
ID-in-label requirement." V-02, V-04, and V-05 test whether A-23 explicitly extends to the
FAIL-FIRST rule layer when the label carries the A-31 ID. V-01 and V-03 test whether A-31
passes with a minimal label that does not carry the criterion ID.

### R12 incoming state on new criteria

From R12 criterion matrix (A-29/A-30/A-31 were not yet criteria in v12 rubric, but the
structural evidence was present in some variations):

- V-03: A-29 PASS (`[C-0N COMMAND]:` labels carry C-01 through C-05 IDs), A-30 PASS (COMMAND
  keyword present in all five labels), A-31 PASS (`[FAIL-FIRST RULE]` in FAIL-FIRST body)
- V-05: A-29 PASS (`[C-0N COMMAND]:` labels present), A-30 PASS (COMMAND keyword present),
  A-31 UNCERTAIN -- `[FAIL-FIRST DECLARATION]` is a section heading label, not a body rule;
  A-31 requires a rule label in the body
- V-01, V-02, V-04: A-29 PARTIAL -- criterion IDs present but in "question"/"prompt" register,
  not COMMAND register; A-30 FAIL (no COMMAND keyword in any per-criterion label); A-31 FAIL
  (no named rule in FAIL-FIRST body)

R13 fixes A-29/A-30/A-31 gaps across all five variations. V-03 serves as the reference form
carried forward unchanged. V-05 upgrades from the uncertain `[FAIL-FIRST DECLARATION]` heading
form to an explicit `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` body rule.

---

## V-01 -- Inertia framing axis

**Axis**: Blockquote-wrapped COMMAND prompt form (`> [C-0N COMMAND]:`); "inertia threat"
vocabulary for A-26 (from R12 V-01 confirmed); bracket-prefix A-23 (from R12 V-01 confirmed);
"READY TO PROCEED?" gate heading for A-27 (confirmed form); `[BRIDGE COMPLETION COMMAND]:`
inline directive for A-25; A-31 via minimal `[FAIL-FIRST RULE]` without criterion ID in label.
**Hypothesis**: Blockquote-wrapped `> [C-0N COMMAND]:` satisfies A-29 and A-30 -- the criterion
ID and COMMAND keyword appear in the label regardless of the blockquote wrapper. A-31 minimal
form `[FAIL-FIRST RULE]` (without carrying the criterion ID in the label) satisfies A-31 without
simultaneously extending A-23 to the FAIL-FIRST layer. The scaffold is otherwise identical to
R12 V-01 plus these three targeted additions.
**Predicted score**: 210/210

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

[FAIL-FIRST RULE]: The inertia threat is the current workaround. It competes without a
vendor, a demo, or a champion. It wins by default unless teams encounter a specific,
observable reason to leave. Map the inertia threat's failure modes first. Every defeat
condition and every switching cost threshold derives only from a documented failure mode.
No defeat condition is valid without a traceable failure mode behind it.

Bridge artifacts required before defeat conditions are authored:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the specific role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## SECTION 1 -- THE INERTIA THREAT'S STRUCTURAL WEAKNESSES: FAILURE MODE INVENTORY

> [C-05 COMMAND]: NAME every specific failure mode where the inertia threat (current
> workaround) breaks, produces errors, causes rework, or hits a scale ceiling. REJECT generic
> descriptions -- "slow" or "manual" alone fails. "CSV export silently truncates rows at
> 65,536 with no error message" passes. MINIMUM 2 rows required.

> **[A-16 PRIMARY KEY RULE]**: Assign all FM-[N] identifiers in this table first. No FM-[N]
> may appear in any later section of this document without a corresponding row assigned here.
> Every downstream reference must trace back to a row in this inventory.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger condition (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|---------------------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                                       |                             |
| FM-2   |                                                                                       |                                    |                                       |                             |

---

## Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

Map each failure mode to the specific role experiencing it. This bridge closes the chain
from failure documentation to role-level attribution required by R-02.

| FM-[N] | Role experiencing the failure (e.g., data-ops team) | Role-level consequence |
|--------|-----------------------------------------------------|------------------------|
| FM-1   |                                                     |                        |
| FM-2   |                                                     |                        |

---

## Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

Map each failure mode to its triggering condition and measurable threshold. This bridge
closes the chain from failure documentation to defeat condition construction required by
C-04.

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

> [C-01 COMMAND]: NAME the specific inertia threat -- the exact tool name, file type, or
> procedure currently in use. NOT "a manual process." NAME the role performing it. QUANTIFY
> the ongoing cost with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 3 -- SWITCHING COST

> [C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a
> number and a unit -- "significant" without a number fails. NAME the role bearing each cost.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 4 -- THREAT ASSESSMENT

> [C-03 COMMAND]: DECLARE the inertia threat score. The default is HIGH -- the inertia
> threat always starts with home-field advantage. IF deviating from HIGH, STATE a specific
> quantified condition; a qualitative judgment does not justify deviation.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the
> triggers in Q4. CITE the FM-[N] driving each condition. "Teams switch when they see the
> value" fails -- every DC row must name a testable, measurable condition.

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
vocabulary for A-26 (from R12 V-02); inline `[C-0N COMMAND]:` per-criterion prompts within each
stage; A-31 via bracket-suffix `FAIL-FIRST CONSTRAINT [A-31]` -- carries A-31 criterion ID,
extending A-23's criterion-ID-in-label pattern to the FAIL-FIRST rule layer; bracket-suffix A-23
(`PRIMARY KEY RULE [A-16]`, `CITATION INTEGRITY RULE [A-19]`); "ALL BRIDGE ARTIFACTS COMPLETE?"
gate heading for A-27.
**Hypothesis**: Inline `[C-0N COMMAND]:` within stage sections satisfies A-29 and A-30 in a
lifecycle-emphasis frame -- the stage boundary structure and COMMAND-register prompts are mutually
reinforcing, each stage making the per-criterion command explicit at the stage entry point.
`FAIL-FIRST CONSTRAINT [A-31]` satisfies A-31 and simultaneously extends A-23's coverage to the
FAIL-FIRST rule layer: the rule carries the A-31 criterion ID in bracket-suffix form, consistent
with the bracket-suffix A-23 style of this variation.
**Predicted score**: 210/210

---

```
## FAIL-FIRST DECLARATION -- THE STATUS QUO AS UNNAMED COMPETITOR

FAIL-FIRST CONSTRAINT [A-31]: Map the status quo's failure modes before writing a single
defeat condition. The status quo is the unnamed competitor -- no name, no sales team, no
roadmap. It persists because switching costs are real and failure modes are invisible. This
analysis makes both visible. Failure modes first; defeat conditions follow from them.

Authoring sequence:
- Stage 1 -- FAILURE MODE INVENTORY (C-05): where the status quo breaks
- Stage 2 -- BRIDGE STAGE: Q3 (FM->actor, closes C-05 -> R-02) + Q4 (FM->trigger, closes
  C-05 -> C-04) + completion gate
- Stage 3 -- WORKAROUND PROFILE (C-01): specific tool, role, ongoing cost
- Stage 4 -- SWITCHING COST (C-02): quantified cost to abandon the status quo
- Stage 5A -- THREAT ASSESSMENT (C-03): inertia threat score
- Stage 5B -- DEFEAT CONDITIONS (C-04): conditions under which the status quo loses
- Stage 6 -- COMPLETENESS CHECK

The Stage 2 gate must show Y for both bridge artifacts before Stage 3 is authored.

---

## STAGE 1 -- WHERE THE STATUS QUO BREAKS: FAILURE MODE INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the status quo (current workaround)
fails, produces errors, causes rework, or hits a scale ceiling. REJECT generic descriptions
-- "manual is slow" fails. "CSV export silently truncates rows above 65,536 with no error
message" passes. MINIMUM 2 rows required.

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
shows N, do not author Stage 3 through Stage 5B. Return to Stage 1 and complete the missing
artifact. Defeat conditions without bridge artifacts lack their actor and trigger chains.

| Bridge artifact                                | Complete? (Y / N) |
|------------------------------------------------|-------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                   |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                   |

---

## STAGE 3 -- WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific status quo workaround -- the exact tool name, file type,
or procedure. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost
with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## STAGE 4 -- SWITCHING COST

[C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a number
and a unit -- "significant" without a number fails. NAME the role bearing each cost.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

[C-03 COMMAND]: DECLARE the inertia threat score. The default is HIGH -- the status quo
always starts with home-field advantage. IF deviating from HIGH, STATE a specific quantified
condition; a qualitative judgment ("low friction") is rejected.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## STAGE 5B -- DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
trigger mapping. CITE the FM-[N] driving each condition. "Teams switch when they see the
value" fails -- each DC row must name a testable, measurable condition.

> **CITATION INTEGRITY RULE [A-19]**: Every FM-[N] cited in this table must have an assigned
> row in Stage 1 (FM Inventory). Do not reference FM identifiers not assigned above. Verify
> before filling each row.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type or segment |
|--------|------------------------------------------|-------------------|------------------------------------------------------|----------------------|
| DC-1   |                                          |                   |                                                      |                      |
| DC-2   |                                          |                   |                                                      |                      |

---

## STAGE 6 -- COMPLETENESS CHECK

| Criterion                                                                                      | Check (Y / N) |
|------------------------------------------------------------------------------------------------|---------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                 |               |
| C-02: At least two switching cost categories, each quantified with number and unit             |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition) |               |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Stage 1       |               |
| C-05: At least two specific, non-generic failure modes documented in Stage 1                  |               |
```

---

## V-03 -- Phrasing register axis (reference form)

**Axis**: Full COMMAND phrasing throughout; "unnamed competitor failure surface" vocabulary for
A-26 (from R12 V-03 confirmed); domain-prefix bracket-suffix A-23 ("INERTIA THREAT RULE [A-16]",
"INERTIA THREAT CITATION RULE [A-19]"); "BOTH BRIDGES BUILT?" gate heading for A-27; A-31 via
`[FAIL-FIRST RULE]` in FAIL-FIRST body (minimal form, no criterion ID in label); A-29+A-30 via
`[C-0N COMMAND]:` bracket-prefix form (carried forward unchanged from R12 V-03).
**Hypothesis**: R12 V-03 scaffold already satisfies A-29, A-30, and A-31 -- this variation
carries it forward as the R13 reference form. `[FAIL-FIRST RULE]` in FAIL-FIRST body satisfies
A-31 without additionally extending A-23 to the FAIL-FIRST layer (criterion ID not in label).
`[C-0N COMMAND]:` in all five per-criterion positions satisfies A-29 and A-30. All 31 criteria
satisfied. 210/210 target confirmed by this scaffold.
**Predicted score**: 210/210

---

```
## FAIL-FIRST DECLARATION -- THE UNNAMED COMPETITOR

[FAIL-FIRST RULE]: The unnamed competitor is the current workaround. It competes without
a name, a vendor, or a roadmap. It wins by default. This analysis exposes the unnamed
competitor's failure surface -- the specific ways it breaks -- before deriving any defeat
conditions. Every DC row must trace to a row in the failure surface inventory.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

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

## V-04 -- Output format axis (consolidated bridge)

**Axis**: Consolidated triple-block bridge (Q3, Q4, and gate as sub-sections within a single
BRIDGE STAGE section); "incumbent workaround" vocabulary for A-26 (from R12 V-04 confirmed);
combined A-25+A-27 gate heading `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS
COMPLETE?` (from R12 V-04 confirmed); bracket-prefix variant A-23 (`[A-16 PRIMARY KEY
CONSTRAINT]`, `[A-19 CITATION INTEGRITY CONSTRAINT]`); inline `[C-0N COMMAND]:` per-criterion
prompts within each stage; A-31 via `[A-31 FAIL-FIRST ORDERING RULE]` in FAIL-FIRST body --
bracket-prefix form carrying A-31 criterion ID.
**Hypothesis**: Inline `[C-0N COMMAND]:` within stage sections satisfies A-29 and A-30 in a
consolidated-bridge format. `[A-31 FAIL-FIRST ORDERING RULE]` satisfies A-31 and simultaneously
extends A-23 to the FAIL-FIRST rule layer via bracket-prefix form with criterion ID -- consistent
with the bracket-prefix A-23 style (`[A-16 PRIMARY KEY CONSTRAINT]`) of this variation. The
combined A-25+A-27 gate heading from R12 V-04 is preserved unchanged.
**Predicted score**: 210/210

---

```
## FAIL-FIRST DECLARATION -- THE INCUMBENT WORKAROUND

[A-31 FAIL-FIRST ORDERING RULE]: The incumbent workaround is the competitor already deployed.
It has no marketing, no roadmap, and no champion -- but it is already paid for, already
trained on, and already embedded in every workflow. Map the incumbent's vulnerabilities before
constructing any defeat condition. A defeat condition without a traceable vulnerability is
speculation, not analysis.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the specific role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## STAGE 1 -- THE INCUMBENT'S VULNERABILITIES: FAILURE MODE INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the incumbent workaround (current
process or tool) breaks, produces errors, causes rework, or hits a scale ceiling. ASSIGN an
FM-[N] identifier to each row. MINIMUM 2 rows. Generic descriptions ("it is slow") fail --
name the specific condition where it breaks.

> **[A-16 PRIMARY KEY CONSTRAINT]**: Assign all FM-[N] identifiers in this table first. No
> FM-[N] may appear in Stage 3 or any downstream section without a prior row assigned here.
> Every downstream reference must trace back to a row in this inventory.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## STAGE 2 -- BRIDGE STAGE

### Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

Map each failure mode to the specific role experiencing it. Bridge closes C-05 to R-02.

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

### Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

Map each failure mode to its triggering condition and measurable threshold. Bridge closes
C-05 to C-04.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?

Do not proceed to Stage 3 unless both Q3 and Q4 show Y below.

| Bridge artifact                                | Complete? (Y / N) |
|------------------------------------------------|-------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                   |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                   |

---

## STAGE 3 -- WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific incumbent workaround -- the exact tool name, file type, or
procedure. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost
with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## STAGE 4 -- SWITCHING COST

[C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a number
and a unit -- "significant" without a number fails. NAME the role bearing each cost.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

[C-03 COMMAND]: DECLARE the inertia threat score. The default is HIGH -- the incumbent
workaround always starts with home-field advantage. IF deviating from HIGH, STATE a specific
quantified condition; a qualitative judgment is rejected.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## STAGE 5B -- DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
trigger mapping. CITE the FM-[N] driving each condition. Every condition must be measurable
and testable -- "teams switch when they see the value" fails.

> **[A-19 CITATION INTEGRITY CONSTRAINT]**: Every FM-[N] cited in this table must have an
> assigned row in Stage 1 (FM Inventory). Do not reference FM identifiers not assigned above.
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
| C-02: At least two switching cost categories, each quantified with number and unit             |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition) |               |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Stage 1       |               |
| C-05: At least two specific, non-generic failure modes documented in Stage 1                  |               |
```

---

## V-05 -- All axes combined

**Axis**: COMMAND phrasing throughout (`[C-0N COMMAND]:` per-criterion + all-caps body text);
"default competitor" vocabulary for A-26 (from R12 V-05 confirmed); domain-prefix bracket-suffix
A-23 ("INERTIA LOCK RULE [A-16]", "INERTIA LOCK CITATION RULE [A-19]"); "PASS BEFORE
CONTINUING?" gate heading for A-27; `[BRIDGE COMPLETION COMMAND]:` all-caps directive for A-25;
A-31 via `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` in FAIL-FIRST body -- domain-prefix with
criterion ID, extending the domain-prefix A-23 pattern to the FAIL-FIRST rule layer.
**Hypothesis**: `[C-0N COMMAND]:` form (confirmed in R12 V-05) satisfies A-29 and A-30 across
all five criterion positions. `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` satisfies A-31 and
extends the domain-prefix A-23 pattern -- consistent with the "INERTIA LOCK RULE [A-16]" and
"INERTIA LOCK CITATION RULE [A-19]" domain-prefix forms in this variation -- to the FAIL-FIRST
rule layer. The A-26 vocabulary family ("default competitor") and the A-31 domain prefix ("DEFAULT
COMPETITOR") are drawn from the same axis vocabulary, confirming internal coherence. All three
new criteria fire simultaneously alongside the full R12 V-05 195/195 scaffold.
**Predicted score**: 210/210

---

```
## [FAIL-FIRST DECLARATION] -- THE DEFAULT COMPETITOR

DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]: The default competitor is the current workaround.
It wins by default -- it needs no demo, no sales cycle, and no champion. Every team that does
not switch keeps the default competitor deployed. Map the default competitor's breaking points
before deriving any defeat condition. A defeat condition without a traceable breaking point is
an assumption, not an analysis. FAIL FIRST. THEN DERIVE.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role experiencing
  it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## SECTION 1 -- THE DEFAULT COMPETITOR'S BREAKING POINTS: FAILURE MODE INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the default competitor (current
workaround) breaks, produces errors, causes rework, or hits a scale ceiling. ASSIGN an FM-[N]
identifier to each row. MINIMUM 2 rows. REJECT generic descriptions -- "slow" or "manual"
alone fails; "CSV export silently truncates rows at 65,536 with no error message" passes.

> **INERTIA LOCK RULE [A-16]**: ASSIGN all FM-[N] identifiers here first. NO FM-[N] reference
> may appear in any later section without a corresponding row assigned in this table. The
> breaking-points inventory is the sole source of FM identifiers for this document.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

[BRIDGE Q3 COMMAND]: MAP each FM-[N] to the specific role experiencing the failure. VERIFY
that each actor entry is a specific role title -- "users" or "the team" fails.

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

## BRIDGE COMPLETION GATE -- PASS BEFORE CONTINUING?

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING SECTIONS 2
THROUGH 5. IF EITHER ROW IS N, DO NOT PROCEED. RETURN TO SECTION 1 AND COMPLETE THE MISSING
BRIDGE ARTIFACT. AN INCOMPLETE BRIDGE LEAVES DEFEAT CONDITIONS WITHOUT ACTOR OR TRIGGER
CHAINS.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

---

## SECTION 2 -- WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific default competitor -- the exact tool name, file type, or
procedure. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost
with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 3 -- SWITCHING COST

[C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a number
and a unit. NAME the role bearing each cost. REJECT any estimate without a number and unit.

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
condition; a qualitative judgment is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
trigger mapping. CITE the FM-[N] driving each condition. EVERY DC row must name a testable,
measurable condition -- "teams switch when they see the value" is REJECTED.

> **INERTIA LOCK CITATION RULE [A-19]**: EVERY FM-[N] cited in this table MUST have an
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

## Criterion Coverage Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| A-08 | via A-14 | via A-14 | via A-14 | via A-14 | via A-14 |
| A-10 | PASS: FAIL-FIRST DECLARATION section heading | PASS: FAIL-FIRST DECLARATION section heading | PASS: FAIL-FIRST DECLARATION section heading | PASS: FAIL-FIRST DECLARATION section heading | PASS: [FAIL-FIRST DECLARATION] label in heading |
| A-11 | PASS: 5 COMMAND prompts carry criterion IDs (C-01 through C-05) | PASS: 5 COMMAND prompts carry criterion IDs (C-01 through C-05) | PASS: 5 COMMAND prompts carry criterion IDs (C-01 through C-05) | PASS: 5 COMMAND prompts carry criterion IDs (C-01 through C-05) | PASS: 5 COMMAND prompts carry criterion IDs (C-01 through C-05) |
| A-12 | PASS: FAIL-FIRST names Q3/Q4 with chain refs | PASS: FAIL-FIRST names Q3/Q4 with chain refs | PASS: FAIL-FIRST names Q3/Q4 with chain refs | PASS: FAIL-FIRST names Q3/Q4 with chain refs | PASS: FAIL-FIRST names Q3/Q4 with chain refs |
| A-13 | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular | PASS: all sections tabular |
| A-14 | PASS: SECTION 1 FM Inventory, FM-[N] first column | PASS: STAGE 1 FM Inventory, FM-[N] first column | PASS: SECTION 1 FM Inventory, FM-[N] first column | PASS: STAGE 1 FM Inventory, FM-[N] first column | PASS: SECTION 1 FM Inventory, FM-[N] first column |
| A-15 | PASS: SECTION 6 COMPLETENESS CHECKLIST trailing | PASS: STAGE 6 COMPLETENESS CHECK trailing | PASS: COMPLETENESS CHECK trailing | PASS: STAGE 6 COMPLETENESS CHECK trailing | PASS: COMPLETENESS CHECK trailing |
| A-16 | PASS: `[A-16 PRIMARY KEY RULE]` bracket-prefix | PASS: `PRIMARY KEY RULE [A-16]` bracket-suffix | PASS: `INERTIA THREAT RULE [A-16]` domain-prefix | PASS: `[A-16 PRIMARY KEY CONSTRAINT]` bracket-prefix variant | PASS: `INERTIA LOCK RULE [A-16]` domain-prefix |
| A-17 | PASS: C-01 through C-05 each have `[C-0N COMMAND]:` label | PASS: C-01 through C-05 each have `[C-0N COMMAND]:` label | PASS: C-01 through C-05 each have `[C-0N COMMAND]:` label | PASS: C-01 through C-05 each have `[C-0N COMMAND]:` label | PASS: C-01 through C-05 each have `[C-0N COMMAND]:` label |
| A-18 | PASS: Section 6 Y/N binary, all 5 criteria | PASS: Stage 6 Y/N binary, all 5 criteria | PASS: COMPLETENESS CHECK Y/N binary, all 5 criteria | PASS: Stage 6 Y/N binary, all 5 criteria | PASS: COMPLETENESS CHECK Y/N binary, all 5 criteria |
| A-19 | PASS: `[A-19 REFERENTIAL INTEGRITY RULE]` bracket-prefix | PASS: `CITATION INTEGRITY RULE [A-19]` bracket-suffix | PASS: `INERTIA THREAT CITATION RULE [A-19]` domain-prefix | PASS: `[A-19 CITATION INTEGRITY CONSTRAINT]` bracket-prefix variant | PASS: `INERTIA LOCK CITATION RULE [A-19]` domain-prefix |
| A-20 | PASS: Ongoing cost (e.g., 2 hours/week); Duration (e.g., 18 months); Estimate (e.g., 3 days); Trigger (e.g., file > 10MB); Frequency (e.g., 2x/sprint) | PASS: same column set with inline examples | PASS: same column set with inline examples | PASS: same column set with inline examples | PASS: same column set with inline examples |
| A-21 | PASS: DC threshold column `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column `(e.g., >10MB, >3 failures/week)` | PASS: DC threshold column `(e.g., >10MB, >3 failures/week)` |
| A-22 | PASS: BRIDGE COMPLETION GATE block between Section 1 and Section 2 | PASS: STAGE 2 COMPLETION GATE block between Stage 1 and Stage 3 | PASS: BRIDGE COMPLETION GATE block between Section 1 and Section 2 | PASS: `[BRIDGE COMPLETION COMMAND]: CONFIRM` sub-section in STAGE 2 between Stage 1 and Stage 3 | PASS: BRIDGE COMPLETION GATE block between Section 1 and Section 2 |
| A-23 | PASS: `[A-16 PRIMARY KEY RULE]` + `[A-19 REFERENTIAL INTEGRITY RULE]` (bracket-prefix) | PASS: `PRIMARY KEY RULE [A-16]` + `CITATION INTEGRITY RULE [A-19]` (bracket-suffix) | PASS: `INERTIA THREAT RULE [A-16]` + `INERTIA THREAT CITATION RULE [A-19]` (domain-prefix) | PASS: `[A-16 PRIMARY KEY CONSTRAINT]` + `[A-19 CITATION INTEGRITY CONSTRAINT]` (bracket-prefix variant) | PASS: `INERTIA LOCK RULE [A-16]` + `INERTIA LOCK CITATION RULE [A-19]` (domain-prefix) |
| A-24 | PASS: `>10MB` (size) + `>3 failures/week` (frequency) -- two distinct threshold types | PASS: same dual-type | PASS: same dual-type | PASS: same dual-type | PASS: same dual-type |
| A-25 | PASS: `[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding...` inline directive | PASS: `[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding...` inline directive | PASS: `[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED...` all-caps directive | PASS: `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?` sub-section heading | PASS: `[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED...` all-caps directive |
| A-26 | PASS: `FAIL-FIRST DECLARATION -- THE INERTIA THREAT` + `SECTION 1 -- THE INERTIA THREAT'S STRUCTURAL WEAKNESSES:` | PASS: `FAIL-FIRST DECLARATION -- THE STATUS QUO AS UNNAMED COMPETITOR` + `STAGE 1 -- WHERE THE STATUS QUO BREAKS:` | PASS: `FAIL-FIRST DECLARATION -- THE UNNAMED COMPETITOR` + `SECTION 1 -- THE UNNAMED COMPETITOR'S FAILURE SURFACE:` | PASS: `FAIL-FIRST DECLARATION -- THE INCUMBENT WORKAROUND` + `STAGE 1 -- THE INCUMBENT'S VULNERABILITIES:` | PASS: `[FAIL-FIRST DECLARATION] -- THE DEFAULT COMPETITOR` + `SECTION 1 -- THE DEFAULT COMPETITOR'S BREAKING POINTS:` |
| A-27 | PASS: `BRIDGE COMPLETION GATE -- READY TO PROCEED?` (confirmed form) | PASS: `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` (confirmed form) | PASS: `BRIDGE COMPLETION GATE -- BOTH BRIDGES BUILT?` (confirmed form) | PASS: `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?` (combined A-25+A-27 heading) | PASS: `BRIDGE COMPLETION GATE -- PASS BEFORE CONTINUING?` (confirmed form) |
| A-28 | PASS: C-01: through C-05: in all checklist item labels | PASS: C-01: through C-05: in all checklist item labels | PASS: C-01: through C-05: in all checklist item labels | PASS: C-01: through C-05: in all checklist item labels | PASS: C-01: through C-05: in all checklist item labels |
| A-29 | PASS: `> [C-01 COMMAND]:` through `> [C-05 COMMAND]:` (blockquote-wrapped bracket-label form) | PASS: `[C-01 COMMAND]:` through `[C-05 COMMAND]:` (inline bracket-label form) | PASS: `[C-01 COMMAND]:` through `[C-05 COMMAND]:` (inline bracket-label form, reference form) | PASS: `[C-01 COMMAND]:` through `[C-05 COMMAND]:` (inline bracket-label form) | PASS: `[C-01 COMMAND]:` through `[C-05 COMMAND]:` (inline bracket-label form) |
| A-30 | PASS: COMMAND keyword in `> [C-0N COMMAND]:` blockquote-wrapped labels; COMMAND present in bracket-label regardless of blockquote wrapper | PASS: COMMAND keyword in `[C-0N COMMAND]:` inline labels | PASS: COMMAND keyword in `[C-0N COMMAND]:` inline labels (reference form) | PASS: COMMAND keyword in `[C-0N COMMAND]:` inline labels | PASS: COMMAND keyword in `[C-0N COMMAND]:` inline labels |
| A-31 | PASS: `[FAIL-FIRST RULE]` named rule label in FAIL-FIRST body (minimal form; does not carry criterion ID) | PASS: `FAIL-FIRST CONSTRAINT [A-31]` named rule label in FAIL-FIRST body (bracket-suffix form; carries A-31 criterion ID; extends A-23 to FAIL-FIRST rule layer) | PASS: `[FAIL-FIRST RULE]` named rule label in FAIL-FIRST body (minimal form; does not carry criterion ID) | PASS: `[A-31 FAIL-FIRST ORDERING RULE]` named rule label in FAIL-FIRST body (bracket-prefix form; carries A-31 criterion ID; extends A-23 to FAIL-FIRST rule layer) | PASS: `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` named rule label in FAIL-FIRST body (domain-prefix form; carries A-31 criterion ID; extends domain-prefix A-23 pattern to FAIL-FIRST rule layer) |
| **Predicted** | **210/210** | **210/210** | **210/210** | **210/210** | **210/210** |

---

## A-29/A-30 Prompt Form Taxonomy

| Form | Example | Variation |
|------|---------|-----------|
| Blockquote-wrapped bracket-prefix | `> [C-05 COMMAND]: NAME every specific failure mode...` | V-01 |
| Inline bracket-prefix | `[C-05 COMMAND]: NAME every specific failure mode...` | V-02, V-03, V-04, V-05 |

A-29/A-30 stress test: Does the blockquote wrapper (`>`) on the bracket-label form affect whether
A-29 and A-30 pass? The criterion IDs and COMMAND keyword are present in the bracket label
regardless of the blockquote wrapper. V-01 tests whether the structural wrapper context changes
the rubric evaluation. V-02 through V-05 use the bare inline form confirmed in R12 V-03/V-05.

## A-31 Rule Label Form Taxonomy

| Form | Label | Criterion ID in label | Extends A-23? | Variations |
|------|-------|----------------------|---------------|------------|
| Minimal (no criterion ID) | `[FAIL-FIRST RULE]` | No | No | V-01, V-03 |
| Bracket-suffix with criterion ID | `FAIL-FIRST CONSTRAINT [A-31]` | Yes | Yes (bracket-suffix) | V-02 |
| Bracket-prefix with criterion ID | `[A-31 FAIL-FIRST ORDERING RULE]` | Yes | Yes (bracket-prefix) | V-04 |
| Domain-prefix with criterion ID | `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` | Yes | Yes (domain-prefix) | V-05 |

A-31 + A-23 interaction: The A-31 rubric notes that "once the A-31 rule label exists and
carries the A-31 criterion ID in its label text, it also satisfies the A-23 criterion-ID-in-
label requirement." V-02, V-04, and V-05 test this extension across three A-23 label form
categories. V-01 and V-03 test whether A-31 passes without the criterion ID extension to A-23.

## A-26 Vocabulary Family Taxonomy (full R13 confirmation)

| Family | FAIL-FIRST subtitle | FM Inventory subtitle | Variation |
|--------|--------------------|-----------------------|-----------|
| Inertia threat | `-- THE INERTIA THREAT` | `-- THE INERTIA THREAT'S STRUCTURAL WEAKNESSES:` | V-01 |
| Status quo as unnamed competitor | `-- THE STATUS QUO AS UNNAMED COMPETITOR` | `-- WHERE THE STATUS QUO BREAKS:` | V-02 |
| Unnamed competitor failure surface | `-- THE UNNAMED COMPETITOR` | `-- THE UNNAMED COMPETITOR'S FAILURE SURFACE:` | V-03 |
| Incumbent workaround | `-- THE INCUMBENT WORKAROUND` | `-- THE INCUMBENT'S VULNERABILITIES:` | V-04 |
| Default competitor | `-- THE DEFAULT COMPETITOR` | `-- THE DEFAULT COMPETITOR'S BREAKING POINTS:` | V-05 |

All five vocabulary families confirmed from R12. R13 carries these forward unchanged. A-26 is
confirmed as vocabulary-agnostic: any internally coherent axis vocabulary whose core noun appears
in both the FAIL-FIRST and FM Inventory heading subtitles satisfies the criterion.

## A-27 Interrogative Form Taxonomy (full R13 confirmation)

| Form | Gate heading | Variation |
|------|-------------|-----------|
| Readiness check | `BRIDGE COMPLETION GATE -- READY TO PROCEED?` | V-01 |
| Artifact inventory | `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` | V-02 |
| Structural completeness | `BRIDGE COMPLETION GATE -- BOTH BRIDGES BUILT?` | V-03 |
| Combined directive+question | `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL ARTIFACTS COMPLETE?` | V-04 |
| Gate-pass | `BRIDGE COMPLETION GATE -- PASS BEFORE CONTINUING?` | V-05 |

All five interrogative forms confirmed from R12. R13 carries them forward. A-27 is confirmed as
interrogative-form-agnostic: any binary decision question (readiness, artifact inventory,
structural completeness, gate-pass, or combined directive+question) satisfies the criterion.
