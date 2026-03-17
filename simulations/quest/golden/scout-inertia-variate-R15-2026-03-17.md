# scout-inertia -- Quest Variate R15

**Rubric**: v15 (ceiling 235 = 100 essential base + 27 advanced criteria x 5 pts)
**Date**: 2026-03-17
**Previous round**: R14 all 5 variations predicted 220/220 (A-32+A-33 confirmed across all five)
**R15 target**: First 235/235 candidate combining A-34 (failure-context FM heading subtitle) +
A-35 (blockquote structural delimiter on per-criterion command prompts) + A-36 (template
position index in bridge completion gate heading name)
**New criteria**: A-34 + A-35 + A-36

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | A-36 only (section-based position index) | R14 V-01 scaffold already has A-34 + A-35; add A-36 via `SECTION 2 COMPLETION GATE` -- tests whether SECTION N index satisfies A-36 in a non-stage structure |
| V-02 | A-35 only (blockquote commands, stage-based reference form) | R14 V-02 scaffold already has A-34 + A-36; add A-35 by blockquoting all 5 inline `[C-0N COMMAND]:` prompts -- this is the R15 reference form combining all three new criteria |
| V-03 | A-35+A-36 on phrasing-register scaffold | A-35 via blockquoting C-0N commands; A-36 via `SECTION 2 COMPLETION GATE`; A-34 confirmed via `THE UNNAMED COMPETITOR'S FAILURE SURFACE` (explicit failure noun) |
| V-04 | A-34 upgrade + A-35+A-36 on consolidated-bridge scaffold | A-34 upgraded from `THE INCUMBENT'S VULNERABILITIES` to `THE INCUMBENT'S FAILURE POINTS`; A-35 via blockquoting C-0N commands; A-36 via `STAGE 2 --` prefix on combined A-25+A-27 gate heading |
| V-05 | A-35+A-36 on all-axes-combined scaffold | A-35 via blockquoting C-0N commands; A-36 via `STAGE 2 COMPLETION GATE`; A-34 confirmed via `THE DEFAULT COMPETITOR'S BREAKING POINTS` (explicit breaking verb) |

---

## R15 Design Notes

### A-34 -- Failure-context frame in FM Inventory heading subtitle

A-34 requires the FM Inventory heading to carry a subtitle that frames the section as the
place where the axis subject fails or breaks. R14 confirmed this criterion from V-01
(`THE INERTIA THREAT'S STRUCTURAL WEAKNESSES`) and V-02 (`WHERE THE STATUS QUO BREAKS`).
V-03 and V-05 carry subtitles with explicit failure nouns (`FAILURE SURFACE`,
`BREAKING POINTS`) and are treated as satisfying A-34 without change. V-04's
`THE INCUMBENT'S VULNERABILITIES` is the borderline case -- "vulnerabilities" is a
weakness frame but not an explicit failure or breaking frame; upgraded to
`THE INCUMBENT'S FAILURE POINTS` to close the gap.

A-34 subtitle forms under test in R15:

| # | Form | Variation | New in R15? |
|---|------|-----------|-------------|
| 1 | `THE INERTIA THREAT'S STRUCTURAL WEAKNESSES` | V-01 | No (confirmed R14 V-01) |
| 2 | `WHERE THE STATUS QUO BREAKS` | V-02 | No (confirmed R14 V-02) |
| 3 | `THE UNNAMED COMPETITOR'S FAILURE SURFACE` | V-03 | New (R14 V-03 unscored for A-34) |
| 4 | `THE INCUMBENT'S FAILURE POINTS` | V-04 | Yes (upgrades R14 V-04 "VULNERABILITIES" to explicit failure-noun form) |
| 5 | `THE DEFAULT COMPETITOR'S BREAKING POINTS` | V-05 | New (R14 V-05 unscored for A-34) |

### A-35 -- Blockquote structural delimiter on per-criterion command prompts

A-35 requires all five per-criterion `[C-0N COMMAND]:` prompts to be wrapped in Markdown
blockquote form (`> [C-0N COMMAND]:`). R14 V-01 was the confirmed source; all other
R14 variations used inline form. R15 converts V-02, V-03, V-04, V-05 to blockquote
form. The conversion applies only to the five C-0N criterion commands (C-01 through C-05).
Bridge-specific commands ([BRIDGE Q3 COMMAND], [BRIDGE Q4 COMMAND], [BRIDGE COMPLETION
COMMAND]) retain each variation's R14 structural form.

A-35 incoming state per variation:

| Variation | C-0N form in R14 | A-35 in R14 | R15 change |
|-----------|-----------------|-------------|------------|
| V-01 | `> [C-0N COMMAND]:` (blockquote) | PASS | None |
| V-02 | `[C-0N COMMAND]:` (inline) | FAIL | Convert 5 commands to blockquote |
| V-03 | `[C-0N COMMAND]:` (inline) | FAIL | Convert 5 commands to blockquote |
| V-04 | `[C-0N COMMAND]:` (inline) | FAIL | Convert 5 commands to blockquote |
| V-05 | `[C-0N COMMAND]:` (inline) | FAIL | Convert 5 commands to blockquote |

### A-36 -- Template position index in bridge completion gate heading name

A-36 requires the bridge completion gate heading to carry a template position index
(`STAGE 2`, `SECTION 2`, or equivalent) that self-locates the gate within the template
hierarchy. R14 V-02 was the confirmed source (`STAGE 2 COMPLETION GATE`). All other
R14 variations used `BRIDGE COMPLETION GATE` (no position index).

A-36 gate heading changes:

| Variation | R14 gate heading | R15 gate heading | A-36 form |
|-----------|-----------------|-----------------|-----------|
| V-01 | `BRIDGE COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` | `SECTION 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` | SECTION N prefix (section-based scaffold) |
| V-02 | `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` | unchanged | STAGE N prefix (confirmed) |
| V-03 | `BRIDGE COMPLETION GATE -- BOTH BRIDGE ARTIFACTS BUILT?` | `SECTION 2 COMPLETION GATE -- BOTH BRIDGE ARTIFACTS BUILT?` | SECTION N prefix (section-based scaffold) |
| V-04 | `### [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL BRIDGE ARTIFACTS COMPLETE?` | `### STAGE 2 -- [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL BRIDGE ARTIFACTS COMPLETE?` | STAGE N prefix prepended to combined A-25+A-27 heading |
| V-05 | `BRIDGE COMPLETION GATE -- ALL BRIDGE ARTIFACTS PASS?` | `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS PASS?` | STAGE N prefix (matches V-02 confirmed form; non-standard completion verb) |

A-36 forms under test in R15:

| # | Form | Variation | Test question |
|---|------|-----------|---------------|
| 1 | `SECTION 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` | V-01 | Does SECTION N index satisfy A-36 in a section-based (non-stage) structure? |
| 2 | `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` | V-02 | Reference form (confirmed R14 V-02) |
| 3 | `SECTION 2 COMPLETION GATE -- BOTH BRIDGE ARTIFACTS BUILT?` | V-03 | Does SECTION N index + non-standard verb satisfy A-36? |
| 4 | `STAGE 2 -- [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL BRIDGE ARTIFACTS COMPLETE?` | V-04 | Does STAGE N as prefix on a combined A-25+A-27 heading satisfy A-36? |
| 5 | `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS PASS?` | V-05 | Does STAGE N + non-standard "PASS?" verb satisfy A-36? |

### R14 incoming state on new criteria (summary)

| Variation | A-34 | A-35 | A-36 | R15 changes required |
|-----------|------|------|------|----------------------|
| V-01 | PASS | PASS | FAIL | A-36 only |
| V-02 | PASS | FAIL | PASS | A-35 only |
| V-03 | PASS (inferred) | FAIL | FAIL | A-35 + A-36 |
| V-04 | UNCERTAIN | FAIL | FAIL | A-34 upgrade + A-35 + A-36 |
| V-05 | PASS (inferred) | FAIL | FAIL | A-35 + A-36 |

---

## V-01 -- A-36 addition to inertia-framing scaffold

**Axis**: Single-axis: A-36 via `SECTION 2 COMPLETION GATE` position index in V-01's
section-based inertia-framing scaffold. A-34 carried from R14 V-01
(`THE INERTIA THREAT'S STRUCTURAL WEAKNESSES`). A-35 carried from R14 V-01 (blockquote
`> [C-0N COMMAND]:` form). A-32 via `FAIL-FIRST CONSTRAINT [A-31]` (confirmed R14 V-01).
A-33 via `SECTION 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` (artifact class
name carried into the now-position-indexed heading). A-26 via "inertia threat" axis
vocabulary. A-23 via bracket-prefix form (`[A-16 PRIMARY KEY RULE]`,
`[A-19 REFERENTIAL INTEGRITY RULE]`).
**Hypothesis**: `SECTION 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` satisfies
A-36 -- the `SECTION 2` prefix is a template position index that self-locates the gate
within the template hierarchy. A-36 cares about the presence of a position index in the
heading name, not specifically about the "STAGE" label type. V-01's section-based structure
uses `SECTION N` numbering consistently (Section 1 through Section 6); `SECTION 2` maps
unambiguously to the bridge section. A-33 remains satisfied -- "BRIDGE ARTIFACTS" is still
named in the interrogative clause of the position-indexed heading. A-34 carried unchanged
from R14 V-01; A-35 carried unchanged. All 36 criteria satisfied.
**Predicted score**: 235/235

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

FAIL-FIRST CONSTRAINT [A-31]: The inertia threat is the current workaround. It competes
without a vendor, a demo, or a champion. It wins by default unless teams encounter a
specific, observable reason to leave. Map the inertia threat's failure modes first. Every
defeat condition and every switching cost threshold derives only from a documented failure
mode. No defeat condition is valid without a traceable failure mode behind it.

Bridge artifacts required before defeat conditions are authored:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the specific role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## SECTION 1 -- THE INERTIA THREAT'S STRUCTURAL WEAKNESSES: FAILURE MODE INVENTORY

> [C-05 COMMAND]: NAME every specific failure mode where the inertia threat (current
> workaround) breaks, produces errors, causes rework, or hits a scale ceiling. REJECT
> generic descriptions -- "slow" or "manual" alone fails. "CSV export silently truncates
> rows at 65,536 with no error message" passes. MINIMUM 2 rows required.

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

## SECTION 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?

[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding to Sections 3 through 6.
Do not author the workaround profile or defeat conditions unless both rows below show Y.
An incomplete bridge means defeat conditions lack their actor and trigger chains.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

If either shows N: return to Section 1 and complete the missing artifact before proceeding.

---

## SECTION 3 -- WORKAROUND PROFILE

> [C-01 COMMAND]: NAME the specific inertia threat -- the exact tool name, file type, or
> procedure currently in use. NOT "a manual process." NAME the role performing it. QUANTIFY
> the ongoing cost with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 4 -- SWITCHING COST

> [C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a
> number and a unit -- "significant" without a number fails. NAME the role bearing each cost.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 5 -- THREAT ASSESSMENT

> [C-03 COMMAND]: DECLARE the inertia threat score. The default is HIGH -- the inertia
> threat always starts with home-field advantage. IF deviating from HIGH, STATE a specific
> quantified condition; a qualitative judgment does not justify deviation.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 6 -- DEFEAT CONDITIONS

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

## SECTION 7 -- COMPLETENESS CHECKLIST

| Criterion                                                                                      | Satisfied? (Y / N) |
|------------------------------------------------------------------------------------------------|--------------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                 |                    |
| C-02: At least two switching cost categories quantified with numbers and units                 |                    |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition) |                    |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Section 1     |                    |
| C-05: At least two specific, non-generic failure modes documented in Section 1                 |                    |
```

---

## V-02 -- A-35 addition to stage-based scaffold (reference form)

**Axis**: Single-axis: A-35 via blockquoting all 5 inline `[C-0N COMMAND]:` prompts in
V-02's stage-based scaffold. A-34 carried from R14 V-02 (`WHERE THE STATUS QUO BREAKS`).
A-36 carried from R14 V-02 (`STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?`).
A-32 via `FAIL-FIRST CONSTRAINT [A-31]` (confirmed R14 V-02). A-33 via `STAGE 2
COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` (confirmed R14 V-02). A-26 via
"status quo as unnamed competitor" vocabulary. A-23 via bracket-suffix form
(`PRIMARY KEY RULE [A-16]`, `CITATION INTEGRITY RULE [A-19]`).
**Hypothesis**: Blockquoting all 5 inline C-0N commands in V-02's stage-based scaffold
satisfies A-35 -- the blockquote structural delimiter upgrades from the label-register
form (A-30: inline COMMAND keyword) to block-level structural isolation. V-02 already
carries A-34 (`WHERE THE STATUS QUO BREAKS`) and A-36 (`STAGE 2 COMPLETION GATE`);
adding A-35 completes all three new criteria on V-02's unchanged stage-based structure.
This is the R15 reference form: the minimal combination of A-34 + A-35 + A-36 on a
single proven scaffold. All 36 criteria satisfied.
**Predicted score**: 235/235

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

> [C-05 COMMAND]: NAME every specific failure mode where the status quo (current workaround)
> fails, produces errors, causes rework, or hits a scale ceiling. REJECT generic descriptions
> -- "manual is slow" fails. "CSV export silently truncates rows above 65,536 with no error
> message" passes. MINIMUM 2 rows required.

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

> [C-01 COMMAND]: NAME the specific status quo workaround -- the exact tool name, file type,
> or procedure. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing
> cost with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## STAGE 4 -- SWITCHING COST

> [C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a
> number and a unit -- "significant" without a number fails. NAME the role bearing each cost.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

> [C-03 COMMAND]: DECLARE the inertia threat score. The default is HIGH -- the status quo
> always starts with home-field advantage. IF deviating from HIGH, STATE a specific
> quantified condition; a qualitative judgment ("low friction") is rejected.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## STAGE 5B -- DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
> trigger mapping. CITE the FM-[N] driving each condition. "Teams switch when they see the
> value" fails -- each DC row must name a testable, measurable condition.

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

## V-03 -- A-35+A-36 on phrasing-register scaffold

**Axis**: A-35 (blockquote C-0N commands) + A-36 (section-based position index) on V-03's
domain-prefix A-23 style scaffold. A-34 confirmed via `THE UNNAMED COMPETITOR'S FAILURE
SURFACE` (explicit failure noun satisfies failure-context frame requirement). A-32 via
`INERTIA THREAT FAIL-FIRST RULE [A-31]` (confirmed R14 V-03). A-33 via `SECTION 2
COMPLETION GATE -- BOTH BRIDGE ARTIFACTS BUILT?` (artifact class name carried into the
now-position-indexed heading). A-26 via "unnamed competitor failure surface" vocabulary.
A-23 via domain-prefix bracket-suffix (`INERTIA THREAT RULE [A-16]`,
`INERTIA THREAT CITATION RULE [A-19]`). Bridge-specific commands ([BRIDGE Q3 COMMAND],
[BRIDGE Q4 COMMAND], [BRIDGE COMPLETION COMMAND]) remain inline per V-03's structural
style -- A-35 applies to C-0N commands only.
**Hypothesis**: Blockquoting all 5 C-0N commands satisfies A-35 in V-03's phrasing-register
scaffold -- the blockquote form works independently of the A-23 domain-prefix style used
for the named structural rules. `SECTION 2 COMPLETION GATE -- BOTH BRIDGE ARTIFACTS BUILT?`
satisfies A-36 -- the `SECTION 2` position index self-locates the gate within V-03's
section-based structure. A-33 remains satisfied -- `BOTH BRIDGE ARTIFACTS BUILT?` carries
the typed artifact class in the interrogative (confirmed R14 V-03). A-34 is satisfied by
`THE UNNAMED COMPETITOR'S FAILURE SURFACE` -- "FAILURE SURFACE" is an explicit failure-
context noun. All 36 criteria satisfied.
**Predicted score**: 235/235

---

```
## FAIL-FIRST DECLARATION -- THE UNNAMED COMPETITOR

INERTIA THREAT FAIL-FIRST RULE [A-31]: The unnamed competitor is the current workaround.
It competes without a name, a vendor, or a roadmap. It wins by default. This analysis
exposes the unnamed competitor's failure surface -- the specific ways it breaks -- before
deriving any defeat conditions. Every DC row must trace to a row in the failure surface
inventory.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## SECTION 1 -- THE UNNAMED COMPETITOR'S FAILURE SURFACE: FAILURE MODE INVENTORY

> [C-05 COMMAND]: NAME every specific failure mode where the unnamed competitor (current
> workaround) breaks, produces errors, causes rework, or hits a scale ceiling. ASSIGN an
> FM-[N] identifier to each row. MINIMUM 2 rows. REJECT generic descriptions -- "slow" or
> "manual" alone fails; "CSV export silently truncates rows at 65,536 with no error message"
> passes.

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

## SECTION 2 COMPLETION GATE -- BOTH BRIDGE ARTIFACTS BUILT?

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING SECTIONS 3
THROUGH 6. If either row is N, DO NOT PROCEED. Return to Section 1 and complete the missing
bridge artifact. An incomplete bridge leaves defeat conditions without actor or trigger chains.

| Bridge artifact                                | Built? (Y / N) |
|------------------------------------------------|----------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                |

---

## SECTION 3 -- WORKAROUND PROFILE

> [C-01 COMMAND]: NAME the specific unnamed competitor -- the exact tool name, file type, or
> procedure. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost
> with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 4 -- SWITCHING COST

> [C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a
> number and a unit. NAME the role bearing each cost.

> **[UNIT RULE]**: EVERY estimate must carry a number and a unit. "Significant" or
> "substantial" without a number is REJECTED.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 5 -- THREAT ASSESSMENT

> [C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH -- the unnamed competitor
> always starts with home-field advantage. IF deviating from HIGH, STATE a specific quantified
> condition; a qualitative judgment ("low friction") is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 6 -- DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
> trigger mapping. CITE the FM-[N] driving each condition. "Teams switch when they see the
> value" fails -- every DC row must name a testable, measurable condition.

> **INERTIA THREAT CITATION RULE [A-19]**: EVERY FM-[N] cited in this table MUST have an
> assigned row in Section 1 (FM Inventory). DO NOT introduce FM references not assigned
> above. VERIFY before filling each row.

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
| C-05: At least two specific, non-generic failure modes in Section 1                            |               |
```

---

## V-04 -- A-34 upgrade + A-35+A-36 on consolidated-bridge scaffold

**Axis**: A-34 upgrade (`THE INCUMBENT'S VULNERABILITIES` -> `THE INCUMBENT'S FAILURE
POINTS`) + A-35 (blockquote C-0N commands) + A-36 (`STAGE 2 --` prefix on combined
A-25+A-27 gate heading) on V-04's consolidated-bridge scaffold. A-32 via
`[A-31 FAIL-FIRST ORDERING RULE]` (confirmed R14 V-04). A-33 via
`### STAGE 2 -- [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL BRIDGE ARTIFACTS COMPLETE?`
(artifact class name in combined heading, now also carrying A-36 position index). A-26 via
"incumbent workaround" vocabulary. A-23 via bracket-prefix form
(`[A-16 PRIMARY KEY CONSTRAINT]`, `[A-19 CITATION INTEGRITY CONSTRAINT]`). Bridge tables
remain inline per V-04's consolidated structure -- A-35 applies to C-0N commands only.
**Hypothesis**: `THE INCUMBENT'S FAILURE POINTS` satisfies A-34 -- "FAILURE POINTS" is an
explicit failure-context frame analogous to V-05's confirmed `BREAKING POINTS` and
V-03's confirmed `FAILURE SURFACE`, framing the FM Inventory as the place where the
incumbent workaround fails. `STAGE 2 -- [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL BRIDGE
ARTIFACTS COMPLETE?` satisfies A-36 -- the `STAGE 2 --` prefix self-locates the gate within
V-04's stage hierarchy; A-36 fires on the position index token regardless of what follows it
in the combined heading. A-33 remains satisfied -- "BRIDGE ARTIFACTS" is still named in the
interrogative clause of the combined heading. Blockquoting all 5 C-0N commands satisfies
A-35. All 36 criteria satisfied.
**Predicted score**: 235/235

---

```
## FAIL-FIRST DECLARATION -- THE INCUMBENT WORKAROUND

[A-31 FAIL-FIRST ORDERING RULE]: The incumbent workaround is the competitor already
deployed. It has no marketing, no roadmap, and no champion -- but it is already paid for,
already trained on, and already embedded in every workflow. Map the incumbent's
vulnerabilities before constructing any defeat condition. A defeat condition without a
traceable vulnerability is speculation, not analysis.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the specific role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## STAGE 1 -- THE INCUMBENT'S FAILURE POINTS: FAILURE MODE INVENTORY

> [C-05 COMMAND]: NAME every specific failure mode where the incumbent workaround (current
> process or tool) breaks, produces errors, causes rework, or hits a scale ceiling. ASSIGN
> an FM-[N] identifier to each row. MINIMUM 2 rows. Generic descriptions ("it is slow")
> fail -- name the specific condition where it breaks.

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

### STAGE 2 -- [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL BRIDGE ARTIFACTS COMPLETE?

Do not proceed to Stage 3 unless both Q3 and Q4 show Y below.

| Bridge artifact                                | Complete? (Y / N) |
|------------------------------------------------|-------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                   |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                   |

---

## STAGE 3 -- WORKAROUND PROFILE

> [C-01 COMMAND]: NAME the specific incumbent workaround -- the exact tool name, file type,
> or procedure. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing
> cost with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## STAGE 4 -- SWITCHING COST

> [C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a
> number and a unit -- "significant" without a number fails. NAME the role bearing each cost.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## STAGE 5A -- THREAT ASSESSMENT

> [C-03 COMMAND]: DECLARE the inertia threat score. The default is HIGH -- the incumbent
> workaround always starts with home-field advantage. IF deviating from HIGH, STATE a
> specific quantified condition; a qualitative judgment is rejected.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## STAGE 5B -- DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
> trigger mapping. CITE the FM-[N] driving each condition. Every condition must be measurable
> and testable -- "teams switch when they see the value" fails.

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

## V-05 -- A-35+A-36 on all-axes-combined scaffold

**Axis**: A-35 (blockquote C-0N commands) + A-36 (`STAGE 2 COMPLETION GATE` position index)
on V-05's all-axes-combined scaffold (COMMAND register + domain-prefix A-23 + all-caps
body text). A-34 confirmed via `THE DEFAULT COMPETITOR'S BREAKING POINTS` (explicit
"breaking" verb satisfies failure-context frame). A-32 via
`DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` (confirmed R14 V-05). A-33 via `STAGE 2
COMPLETION GATE -- ALL BRIDGE ARTIFACTS PASS?` (artifact class name carried into the now-
position-indexed heading). A-26 via "default competitor" vocabulary. A-23 via domain-prefix
bracket-suffix (`INERTIA LOCK RULE [A-16]`, `INERTIA LOCK CITATION RULE [A-19]`). Bridge-
specific commands ([BRIDGE Q3 COMMAND], [BRIDGE Q4 COMMAND], [BRIDGE COMPLETION COMMAND])
remain in V-05's all-caps inline form -- A-35 applies to C-0N commands only.
**Hypothesis**: `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS PASS?` satisfies both A-36
and A-33 -- `STAGE 2` is the position index (A-36) and `BRIDGE ARTIFACTS` is the typed
artifact class named in the interrogative (A-33). V-05's `PASS?` completion verb was
confirmed as an alternative to `COMPLETE?` for A-33 in R14; the addition of `STAGE 2`
as position index does not affect A-33. Blockquoting all 5 C-0N commands in V-05's all-caps
COMMAND-register context satisfies A-35 -- the blockquote structural delimiter works within
the all-caps phrasing register. A-34 is satisfied by `THE DEFAULT COMPETITOR'S BREAKING
POINTS` -- "BREAKING POINTS" is an explicit failure-context frame. All 36 criteria satisfied.
**Predicted score**: 235/235

---

```
## [FAIL-FIRST DECLARATION] -- THE DEFAULT COMPETITOR

DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]: The default competitor is the current
workaround. It wins by default -- it needs no demo, no sales cycle, and no champion.
Every team that does not switch keeps the default competitor deployed. Map the default
competitor's breaking points before deriving any defeat condition. A defeat condition
without a traceable breaking point is an assumption, not an analysis. FAIL FIRST.
THEN DERIVE.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## SECTION 1 -- THE DEFAULT COMPETITOR'S BREAKING POINTS: FAILURE MODE INVENTORY

> [C-05 COMMAND]: NAME every specific failure mode where the default competitor (current
> workaround) breaks, produces errors, causes rework, or hits a scale ceiling. ASSIGN an
> FM-[N] identifier to each row. MINIMUM 2 rows. REJECT generic descriptions -- "slow" or
> "manual" alone fails; "CSV export silently truncates rows at 65,536 with no error message"
> passes.

> **INERTIA LOCK RULE [A-16]**: ASSIGN all FM-[N] identifiers here first. NO FM-[N]
> reference may appear in any later section without a corresponding row assigned in this
> table. The breaking-points inventory is the sole source of FM identifiers for this
> document.

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

## STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS PASS?

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

> [C-01 COMMAND]: NAME the specific default competitor -- the exact tool name, file type, or
> procedure. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost
> with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 3 -- SWITCHING COST

> [C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a
> number and a unit. NAME the role bearing each cost. REJECT any estimate without a number
> and unit.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 4 -- THREAT ASSESSMENT

> [C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH -- the default competitor
> always starts with home-field advantage. IF deviating from HIGH, STATE a specific quantified
> condition; a qualitative judgment is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
> trigger mapping. CITE the FM-[N] driving each condition. EVERY DC row must name a testable,
> measurable condition -- "teams switch when they see the value" is REJECTED.

> **INERTIA LOCK CITATION RULE [A-19]**: EVERY FM-[N] cited in this table MUST have an
> assigned row in Section 1 (FM Inventory). DO NOT introduce FM references not assigned
> above. VERIFY before filling each row.

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
| C-05: At least two specific, non-generic failure modes in Section 1                            |               |
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
| A-10 | via A-34 | via A-34 | via A-34 | via A-34 | via A-34 |
| A-11 | via A-35 | via A-35 | via A-35 | via A-35 | via A-35 |
| A-12 | via A-36 | via A-36 | via A-36 | via A-36 | via A-36 |
| A-13 | PASS: all sections tabular | PASS: all stages tabular | PASS: all sections tabular | PASS: all stages tabular | PASS: all sections tabular |
| A-14 | via A-34 | via A-34 | via A-34 | via A-34 | via A-34 |
| A-15 | PASS: SECTION 7 COMPLETENESS CHECKLIST | PASS: STAGE 6 COMPLETENESS CHECK | PASS: COMPLETENESS CHECK (trailing) | PASS: STAGE 6 COMPLETENESS CHECK | PASS: COMPLETENESS CHECK (trailing) |
| A-16 | PASS: [A-16 PRIMARY KEY RULE] in Section 1 | PASS: PRIMARY KEY RULE [A-16] in Stage 1 | PASS: INERTIA THREAT RULE [A-16] in Section 1 | PASS: [A-16 PRIMARY KEY CONSTRAINT] in Stage 1 | PASS: INERTIA LOCK RULE [A-16] in Section 1 |
| A-17 | via A-35 | via A-35 | via A-35 | via A-35 | via A-35 |
| A-18 | PASS: Y/N column, all 5 criteria labeled | PASS: Y/N column, all 5 criteria labeled | PASS: Y/N column, all 5 criteria labeled | PASS: Y/N column, all 5 criteria labeled | PASS: Y/N column, all 5 criteria labeled |
| A-19 | PASS: [A-19 REFERENTIAL INTEGRITY RULE] in Section 6 | PASS: CITATION INTEGRITY RULE [A-19] in Stage 5B | PASS: INERTIA THREAT CITATION RULE [A-19] in Section 6 | PASS: [A-19 CITATION INTEGRITY CONSTRAINT] in Stage 5B | PASS: INERTIA LOCK CITATION RULE [A-19] in Section 5 |
| A-20 | PASS: "(e.g., ...)" in all unit-bearing column labels | PASS: "(e.g., ...)" in all unit-bearing column labels | PASS: "(e.g., ...)" in all unit-bearing column labels | PASS: "(e.g., ...)" in all unit-bearing column labels | PASS: "(e.g., ...)" in all unit-bearing column labels |
| A-21 | PASS: "(e.g., >10MB, >3 failures/week)" in DC threshold column | PASS: "(e.g., >10MB, >3 failures/week)" in DC threshold column | PASS: "(e.g., >10MB, >3 failures/week)" in DC threshold column | PASS: "(e.g., >10MB, >3 failures/week)" in DC threshold column | PASS: "(e.g., >10MB, >3 failures/week)" in DC threshold column |
| A-22 | via A-36 | via A-36 | via A-36 | via A-36 | via A-36 |
| A-23 | PASS: [A-16 PRIMARY KEY RULE], [A-19 REFERENTIAL INTEGRITY RULE] (bracket-prefix) | PASS: PRIMARY KEY RULE [A-16], CITATION INTEGRITY RULE [A-19] (bracket-suffix) | PASS: INERTIA THREAT RULE [A-16], INERTIA THREAT CITATION RULE [A-19] (domain-prefix bracket-suffix) | PASS: [A-16 PRIMARY KEY CONSTRAINT], [A-19 CITATION INTEGRITY CONSTRAINT] (bracket-prefix) | PASS: INERTIA LOCK RULE [A-16], INERTIA LOCK CITATION RULE [A-19] (domain-prefix bracket-suffix) |
| A-24 | PASS: two threshold types in DC column label | PASS: two threshold types in DC column label | PASS: two threshold types in DC column label | PASS: two threshold types in DC column label | PASS: two threshold types in DC column label |
| A-25 | PASS: [BRIDGE COMPLETION COMMAND] directive | PASS: [BRIDGE COMPLETION COMMAND] directive | PASS: [BRIDGE COMPLETION COMMAND] directive | PASS: [BRIDGE COMPLETION COMMAND] in combined heading | PASS: [BRIDGE COMPLETION COMMAND] directive |
| A-26 | PASS: "THE INERTIA THREAT'S STRUCTURAL WEAKNESSES" + "THE INERTIA THREAT" | PASS: "WHERE THE STATUS QUO BREAKS" + "THE STATUS QUO AS UNNAMED COMPETITOR" | PASS: "THE UNNAMED COMPETITOR'S FAILURE SURFACE" + "THE UNNAMED COMPETITOR" | PASS: "THE INCUMBENT'S FAILURE POINTS" + "THE INCUMBENT WORKAROUND" | PASS: "THE DEFAULT COMPETITOR'S BREAKING POINTS" + "THE DEFAULT COMPETITOR" |
| A-27 | via A-36 | via A-36 | via A-36 | via A-36 | via A-36 |
| A-28 | PASS: C-01 through C-05 in checklist item labels | PASS: C-01 through C-05 in checklist item labels | PASS: C-01 through C-05 in checklist item labels | PASS: C-01 through C-05 in checklist item labels | PASS: C-01 through C-05 in checklist item labels |
| A-29 | via A-35 | via A-35 | via A-35 | via A-35 | via A-35 |
| A-30 | via A-35 | via A-35 | via A-35 | via A-35 | via A-35 |
| A-31 | PASS: FAIL-FIRST CONSTRAINT [A-31] is named rule in FAIL-FIRST body | PASS: FAIL-FIRST CONSTRAINT [A-31] is named rule in FAIL-FIRST body | PASS: INERTIA THREAT FAIL-FIRST RULE [A-31] is named rule in FAIL-FIRST body | PASS: [A-31 FAIL-FIRST ORDERING RULE] is named rule in FAIL-FIRST body | PASS: DEFAULT COMPETITOR FAIL-FIRST RULE [A-31] is named rule in FAIL-FIRST body |
| A-32 | PASS: FAIL-FIRST CONSTRAINT [A-31] carries A-31 criterion ID (bracket-suffix) | PASS: FAIL-FIRST CONSTRAINT [A-31] carries A-31 criterion ID (bracket-suffix) | PASS: INERTIA THREAT FAIL-FIRST RULE [A-31] carries A-31 criterion ID (domain-prefix bracket-suffix) | PASS: [A-31 FAIL-FIRST ORDERING RULE] carries A-31 criterion ID (bracket-prefix) | PASS: DEFAULT COMPETITOR FAIL-FIRST RULE [A-31] carries A-31 criterion ID (domain-prefix) |
| A-33 | PASS: "ALL BRIDGE ARTIFACTS COMPLETE?" in SECTION 2 COMPLETION GATE heading | PASS: "ALL BRIDGE ARTIFACTS COMPLETE?" in STAGE 2 COMPLETION GATE sub-heading | PASS: "BOTH BRIDGE ARTIFACTS BUILT?" in SECTION 2 COMPLETION GATE heading | PASS: "ALL BRIDGE ARTIFACTS COMPLETE?" in STAGE 2 combined heading | PASS: "ALL BRIDGE ARTIFACTS PASS?" in STAGE 2 COMPLETION GATE heading |
| A-34 | PASS: "THE INERTIA THREAT'S STRUCTURAL WEAKNESSES" in Section 1 heading subtitle (failure-context frame via "WEAKNESSES") | PASS: "WHERE THE STATUS QUO BREAKS" in Stage 1 heading subtitle (explicit "BREAKS") | PASS: "THE UNNAMED COMPETITOR'S FAILURE SURFACE" in Section 1 heading subtitle (explicit failure noun) | PASS: "THE INCUMBENT'S FAILURE POINTS" in Stage 1 heading subtitle (explicit failure noun; upgraded from "VULNERABILITIES") | PASS: "THE DEFAULT COMPETITOR'S BREAKING POINTS" in Section 1 heading subtitle (explicit "BREAKING") |
| A-35 | PASS: > [C-05 COMMAND]:, > [C-01 COMMAND]:, > [C-02 COMMAND]:, > [C-03 COMMAND]:, > [C-04 COMMAND]: (blockquote form, carried from R14 V-01) | PASS: > [C-05 COMMAND]:, > [C-01 COMMAND]:, > [C-02 COMMAND]:, > [C-03 COMMAND]:, > [C-04 COMMAND]: (blockquote form, new in R15) | PASS: > [C-05 COMMAND]:, > [C-01 COMMAND]:, > [C-02 COMMAND]:, > [C-03 COMMAND]:, > [C-04 COMMAND]: (blockquote form, new in R15) | PASS: > [C-05 COMMAND]:, > [C-01 COMMAND]:, > [C-02 COMMAND]:, > [C-03 COMMAND]:, > [C-04 COMMAND]: (blockquote form, new in R15) | PASS: > [C-05 COMMAND]:, > [C-01 COMMAND]:, > [C-02 COMMAND]:, > [C-03 COMMAND]:, > [C-04 COMMAND]: (blockquote form, new in R15) |
| A-36 | PASS: "SECTION 2 COMPLETION GATE" carries SECTION 2 position index (new in R15; section-based index form) | PASS: "STAGE 2 COMPLETION GATE" carries STAGE 2 position index (carried from R14 V-02) | PASS: "SECTION 2 COMPLETION GATE" carries SECTION 2 position index (new in R15; section-based index form) | PASS: "STAGE 2 -- [BRIDGE COMPLETION COMMAND]:" carries STAGE 2 position index as heading prefix (new in R15; prepended to combined A-25+A-27 heading) | PASS: "STAGE 2 COMPLETION GATE" carries STAGE 2 position index (new in R15; non-standard completion verb preserved) |
| **Total** | **235/235** | **235/235** | **235/235** | **235/235** | **235/235** |
