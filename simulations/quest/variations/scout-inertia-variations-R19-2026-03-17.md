`scout-inertia-variations-R19-2026-03-17.md` written.

---

## R19 Summary

**5 variations, 3 single-axis + 2 combined. Two new criteria under test: C-57 and C-58.**

| V | Axis | C-57 | C-58 | Predicted score |
|---|------|------|------|-----------------|
| **V-01** | Single: C-57 fail isolation — generic task noun `and complete the bridge artifact` | FAIL | FAIL | ~9.40 |
| **V-02** | Single: C-57 pass + C-58 fail — stage scaffold, standard notation (R18 V-02 carried) | PASS | FAIL | ~9.60 |
| **V-03** | Single: C-58 fail via domain-prefix conflation — `INERTIA THREAT Q3 MAPPING RULE:` at bridge position | PASS | FAIL | ~9.80 |
| **V-04** | Combined: C-57 + C-58 both pass (R18 V-04 carried — 10.00 reference) | PASS | PASS | **10.00** |
| **V-05** | Combined: C-57 pass + C-58 fail (R18 V-05 carried — mixed non-bridge vocabulary) | PASS | FAIL | **9.80** |

**Key discriminators:**

- **C-57 boundary**: `bridge artifact` (derives from non-discriminating `BRIDGE` shared by both classes) vs `actor mapping` (derives from discriminating `ACTOR` in `FM->ACTOR BRIDGE`). V-01 is the first explicit C-57 fail case.
- **C-58 boundary**: V-03 vs V-04 isolates positional segregation. Both have `INERTIA THREAT` threading through 5+ labels (C-42 passes in both). V-03 fails C-58 because 2 of those labels are at bridge positions. V-04 passes because the domain-prefix labels are exclusively at non-bridge positions.
- **V-04 vs V-05 discrimination**: R19 scores V-04 at 50/50 and V-05 at 49/50 — first round where these two diverge.
notations present (C-54 PASS, C-55 PASS) but generic task noun
  (C-57 FAIL). The discriminating test: does the task noun derive from the discriminating component
  of the class label? `(FM->ACTOR BRIDGE)` -> discriminating component `ACTOR` -> task noun must be
  `ACTOR MAPPING` or equivalent. Task noun `BRIDGE ARTIFACT` derives only from `BRIDGE`, which is
  present in both `FM->ACTOR BRIDGE` and `FM->TRIGGER BRIDGE` -- non-discriminating. C-57 fails.
- **C-58 precondition**: C-42 must pass (bracket vocabulary threading across 3+ elements). V-01
  and V-02 use standard notation without a consistent domain prefix threading 3+ elements -- they
  fail C-42 and C-58 by precondition. V-03 passes C-42 (INERTIA THREAT threads through 5 labels)
  but fails C-58 (2 of those labels are at bridge positions -- positional segregation violated).
- **V-04 C-58 pass mechanism**: INERTIA THREAT domain-prefix labels confined exclusively to
  non-bridge positions (FAIL-FIRST, FM Inventory, Defeat Conditions); bridge positions carry only
  `[BRIDGE Q3 COMMAND]:` and `[BRIDGE Q4 COMMAND]:`. Positional segregation complete.
- **V-05 C-58 fail mechanism**: Non-bridge labels use mixed vocabulary (`DEFAULT COMPETITOR
  FAIL-FIRST RULE [A-31]` + `INERTIA LOCK RULE [A-16]` + `INERTIA LOCK CITATION RULE [A-19]`).
  `DEFAULT COMPETITOR` threads through 1 label only; `INERTIA LOCK` through 2 labels only. No
  single domain prefix achieves 3+ element threading at non-bridge positions. C-42 precondition
  for C-58 is not satisfied.

---

## V-01 -- C-57 fail isolation (section scaffold, generic task noun)

**Axis**: Single-axis: C-57 boundary test. Based on R18 V-01 section scaffold (Section 1A/1B
naming, lowercase conditional register). One change from R18 V-01: completion-action task noun
replaced from class-derived form (`and complete the actor mapping`) to class-generic form
(`and complete the bridge artifact`). All other R18 V-01 elements carried unchanged. This isolates
the C-57 criterion: C-55 requires a task to be named; C-57 requires the task noun to be lexically
derived from the discriminating vocabulary of the class annotation.
**Hypothesis**: `If Q3 shows N, return to Section 1A (FM->ACTOR BRIDGE) and complete the bridge
artifact.` passes C-55 -- a return location, class annotation, and named task are all present.
It fails C-57 -- `bridge artifact` derives from `BRIDGE`, which is the non-discriminating
component shared by both `FM->ACTOR BRIDGE` and `FM->TRIGGER BRIDGE`; it does not derive from
the discriminating noun `ACTOR` or `TRIGGER`. An author cannot determine from `complete the bridge
artifact` alone which artifact-type work is required. C-56 NOT satisfied -- `Section 1A` is an
ordinal label. C-58 NOT satisfied -- standard `[A-16]` / `[A-19]` notation lacks domain-prefix
vocabulary threading.
**Predicted score**: all prior criteria pass + C-55 pass; C-56 fail; C-57 fail; C-58 fail

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
  experiencing it (housed in Section 1A)
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition (housed in Section 1B)

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

## SECTION 1A -- Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

Map each failure mode to the specific role experiencing it. This bridge closes the chain
from failure documentation to role-level attribution required by R-02.

| FM-[N] | Role experiencing the failure (e.g., data-ops team) | Role-level consequence |
|--------|-----------------------------------------------------|------------------------|
| FM-1   |                                                     |                        |
| FM-2   |                                                     |                        |

---

## SECTION 1B -- Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

Map each failure mode to its triggering condition and measurable threshold. This bridge
closes the chain from failure documentation to defeat condition construction required by
C-04.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

---

## SECTION 2 COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?

[BRIDGE COMPLETION COMMAND]: Complete Section 1A (Q3) and Section 1B (Q4) before
proceeding to Sections 3 through 6. Do not author the workaround profile or defeat
conditions unless both rows below show Y. An incomplete bridge means defeat conditions
lack their actor and trigger chains.
If Q3 shows N, return to Section 1A (FM->ACTOR BRIDGE) and complete the bridge artifact.
If Q4 shows N, return to Section 1B (FM->TRIGGER BRIDGE) and complete the bridge artifact.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

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
> triggers in Section 1B (Q4). CITE the FM-[N] driving each condition. "Teams switch when
> they see the value" fails -- every DC row must name a testable, measurable condition.

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

## V-02 -- C-57 pass + C-58 fail (stage scaffold, standard notation) -- R18 V-02 carried unchanged

**Axis**: Single-axis: C-57 pass confirmation on stage-based scaffold. R18 V-02 carried unchanged.
The stage-based scaffold uses `PRIMARY KEY RULE [A-16]` and `CITATION INTEGRITY RULE [A-19]` at
non-bridge positions -- standard label notation without unified domain-prefix vocabulary threading
across 3+ elements. Confirms C-57 is register-agnostic (lowercase routing clause passes C-57
identically to all-caps forms) while confirming C-58 requires the specific domain-prefix vocabulary
threading that this scaffold lacks.
**Hypothesis**: `If Q3 shows N, return to Stage 2A (FM->ACTOR BRIDGE) and complete the actor
mapping.` passes C-57 -- `actor mapping` derives from discriminating vocabulary `ACTOR` in class
label `FM->ACTOR BRIDGE`. The stage scaffold cannot satisfy C-56 (Stage 2A is an ordinal label).
C-58 fails -- `PRIMARY KEY RULE [A-16]` and `CITATION INTEGRITY RULE [A-19]` do not share a
domain-prefix vocabulary (`PRIMARY KEY` and `CITATION INTEGRITY` are distinct vocabularies,
neither threading through 3+ elements). C-42 precondition for C-58 not satisfied.
**Predicted score**: all prior criteria pass + C-55 pass + C-57 pass; C-56 fail; C-58 fail

---

```
## FAIL-FIRST DECLARATION -- THE STATUS QUO AS UNNAMED COMPETITOR

FAIL-FIRST CONSTRAINT [A-31]: Map the status quo's failure modes before writing a single
defeat condition. The status quo is the unnamed competitor -- no name, no sales team, no
roadmap. It persists because switching costs are real and failure modes are invisible. This
analysis makes both visible. Failure modes first; defeat conditions follow from them.

Authoring sequence:
- Stage 1 -- FAILURE MODE INVENTORY (C-05): where the status quo breaks
- Stage 2A -- Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02): maps each FM-[N] to the role
  experiencing it
- Stage 2B -- Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04): maps each FM-[N] to its
  triggering condition
- Stage 2 COMPLETION GATE: confirm both Stage 2A and Stage 2B before Stage 3
- Stage 3 -- WORKAROUND PROFILE (C-01): specific tool, role, ongoing cost
- Stage 4 -- SWITCHING COST (C-02): quantified cost to abandon the status quo
- Stage 5A -- THREAT ASSESSMENT (C-03): inertia threat score
- Stage 5B -- DEFEAT CONDITIONS (C-04): conditions under which the status quo loses
- Stage 6 -- COMPLETENESS CHECK

The Stage 2 gate must show Y for both Stage 2A and Stage 2B before Stage 3 is authored.

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

### STAGE 2A -- Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

Map each failure mode to the specific role experiencing it.

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

### STAGE 2B -- Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

Map each failure mode to its triggering condition and measurable threshold.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

### STAGE 2 COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?

[BRIDGE COMPLETION COMMAND]: Complete Stage 2A (Q3) and Stage 2B (Q4) before proceeding
to Stage 3. Do not author Stage 3 through Stage 5B unless both rows below show Y. Defeat
conditions without bridge artifacts lack their actor and trigger chains.
If Q3 shows N, return to Stage 2A (FM->ACTOR BRIDGE) and complete the actor mapping.
If Q4 shows N, return to Stage 2B (FM->TRIGGER BRIDGE) and complete the trigger mapping.

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

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Stage
> 2B (Q4) trigger mapping. CITE the FM-[N] driving each condition. "Teams switch when they
> see the value" fails -- each DC row must name a testable, measurable condition.

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

## V-03 -- C-58 fail via domain-prefix conflation at bridge positions

**Axis**: Single-axis: C-58 boundary test -- domain-prefix vocabulary appears at bridge authoring
positions, violating positional segregation. Uses standalone Q3/Q4 top-level sections (C-56
applicability condition satisfied). Non-bridge positions carry `INERTIA THREAT` domain-prefix
labels (FAIL-FIRST, FM Inventory, Defeat Conditions). Bridge positions also carry `INERTIA THREAT`
vocabulary: `INERTIA THREAT Q3 MAPPING RULE:` at Q3 section, `INERTIA THREAT Q4 MAPPING RULE:` at
Q4 section. Single change from V-04: `[BRIDGE Q3 COMMAND]:` and `[BRIDGE Q4 COMMAND]:` replaced
with `INERTIA THREAT Q3 MAPPING RULE:` and `INERTIA THREAT Q4 MAPPING RULE:` at bridge positions.
Gate body is identical to V-04 (C-55, C-56, C-57 all pass).
**Hypothesis**: C-42 passes -- `INERTIA THREAT` vocabulary threads through 5 bracket labels:
`INERTIA THREAT FAIL-FIRST RULE [A-31]`, `INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION
RULE [A-19]`, `INERTIA THREAT Q3 MAPPING RULE:`, `INERTIA THREAT Q4 MAPPING RULE:`. C-46 passes --
compound domain-axis vocabulary present. C-58 FAILS -- bridge authoring positions (Q3 section, Q4
section) carry domain-rule labels (`INERTIA THREAT Q3 MAPPING RULE:`) rather than separate
bridge-command labels (`[BRIDGE Q3 COMMAND]:`). The `INERTIA THREAT` vocabulary domain is not
positionally confined to non-bridge positions; it spans both analysis and bridge locations.
Positional segregation required by C-58 is violated. C-57 passes -- gate body uses class-derived
task nouns (ACTOR MAPPING from FM->ACTOR BRIDGE; TRIGGER MAPPING from FM->TRIGGER BRIDGE).
**Predicted score**: all prior criteria pass + C-55 pass + C-56 pass + C-57 pass; C-58 fail

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

INERTIA THREAT FAIL-FIRST RULE [A-31]: The inertia threat is the current workaround.
It competes without a name, a vendor, or a roadmap. It wins by default. This analysis
exposes the inertia threat's failure surface -- the specific ways it breaks -- before
deriving any defeat conditions. Every DC row must trace to a row in the failure surface
inventory. Failure modes first. Defeat conditions follow.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## SECTION 1 -- THE INERTIA THREAT'S FAILURE SURFACE: FAILURE MODE INVENTORY

> [C-05 COMMAND]: NAME every specific failure mode where the inertia threat (current
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

INERTIA THREAT Q3 MAPPING RULE: MAP each FM-[N] to the specific role experiencing the
failure. VERIFY that each actor name is a specific role title, not "users" or "the team."

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

---

## Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

INERTIA THREAT Q4 MAPPING RULE: MAP each FM-[N] to its triggering condition. QUANTIFY
the measurable threshold that activates the failure.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

---

## BRIDGE COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH Q3 (FM->ACTOR BRIDGE) AND Q4 (FM->TRIGGER BRIDGE) BEEN POPULATED?

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING SECTIONS 2
THROUGH 5. IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE
ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE
THE TRIGGER MAPPING. AN INCOMPLETE BRIDGE LEAVES DEFEAT CONDITIONS WITHOUT ACTOR OR TRIGGER
CHAINS.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

---

## SECTION 2 -- WORKAROUND PROFILE

> [C-01 COMMAND]: NAME the specific inertia threat -- the exact tool name, file type, or
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

> [C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH -- the inertia threat
> always starts with home-field advantage. IF deviating from HIGH, STATE a specific quantified
> condition; a qualitative judgment ("low friction") is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
> trigger mapping. CITE the FM-[N] driving each condition. EVERY DC row must name a testable,
> measurable condition -- "teams switch when they see the value" is REJECTED.

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

## V-04 -- C-57 + C-58 combined pass (domain-prefix positional segregation reference) -- R18 V-04 carried unchanged

**Axis**: Combined C-57 + C-58 on the domain-prefix bracket-suffix phrasing-register scaffold.
R18 V-04 carried unchanged. V-04 is the first scaffold to achieve 10.00 in the domain-prefix
register and the first confirmed C-58 pass. The enabling structural property: `INERTIA THREAT`
domain-prefix labels are confined exclusively to non-bridge structural analysis positions
(FAIL-FIRST declaration, FM Inventory table, defeat conditions table), while `[BRIDGE Q3 COMMAND]:`
and `[BRIDGE Q4 COMMAND]:` occupy the bridge artifact authoring positions. Carrying V-04 unchanged
into R19 confirms C-58 fidelity and establishes V-04 as the 50/50 = 10.00 reference form.
**Hypothesis**: V-04 satisfies C-57 -- `AND COMPLETE THE ACTOR MAPPING` derives from `ACTOR` in
class `FM->ACTOR BRIDGE`; `AND COMPLETE THE TRIGGER MAPPING` derives from `TRIGGER` in class
`FM->TRIGGER BRIDGE`. V-04 satisfies C-58 -- `INERTIA THREAT RULE [A-16]` at FM Inventory
(non-bridge), `INERTIA THREAT CITATION RULE [A-19]` at defeat conditions (non-bridge), `INERTIA
THREAT FAIL-FIRST RULE [A-31]` in FAIL-FIRST (non-bridge); `[BRIDGE Q3 COMMAND]:` at Q3 section
(bridge), `[BRIDGE Q4 COMMAND]:` at Q4 section (bridge). Domain-prefix labels exclusively at
non-bridge positions; bridge-command labels exclusively at bridge positions. Positional segregation
complete.
**Predicted score**: all criteria pass including C-57 and C-58 -- 50/50 = 10.00

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

INERTIA THREAT FAIL-FIRST RULE [A-31]: The inertia threat is the current workaround.
It competes without a name, a vendor, or a roadmap. It wins by default. This analysis
exposes the inertia threat's failure surface -- the specific ways it breaks -- before
deriving any defeat conditions. Every DC row must trace to a row in the failure surface
inventory. Failure modes first. Defeat conditions follow.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## SECTION 1 -- THE INERTIA THREAT'S FAILURE SURFACE: FAILURE MODE INVENTORY

> [C-05 COMMAND]: NAME every specific failure mode where the inertia threat (current
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

[BRIDGE Q3 COMMAND]: MAP each FM-[N] to the specific role experiencing the failure. VERIFY
that each actor name is a specific role title, not "users" or "the team."

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

## BRIDGE COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH Q3 (FM->ACTOR BRIDGE) AND Q4 (FM->TRIGGER BRIDGE) BEEN POPULATED?

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING SECTIONS 2
THROUGH 5. IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE
ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE
THE TRIGGER MAPPING. AN INCOMPLETE BRIDGE LEAVES DEFEAT CONDITIONS WITHOUT ACTOR OR TRIGGER
CHAINS.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

---

## SECTION 2 -- WORKAROUND PROFILE

> [C-01 COMMAND]: NAME the specific inertia threat -- the exact tool name, file type, or
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

> [C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH -- the inertia threat
> always starts with home-field advantage. IF deviating from HIGH, STATE a specific quantified
> condition; a qualitative judgment ("low friction") is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
> trigger mapping. CITE the FM-[N] driving each condition. EVERY DC row must name a testable,
> measurable condition -- "teams switch when they see the value" is REJECTED.

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

## V-05 -- C-57 pass + C-58 fail (mixed vocabulary, no unified domain-prefix at non-bridge positions) -- R18 V-05 carried unchanged

**Axis**: Combined C-57 pass + C-58 fail. R18 V-05 carried unchanged. R17 V-05 was the source of
both the C-55 and C-56 excellence signals; R18 V-05 confirmed C-55 and C-56; R19 V-05 confirms C-57
while serving as the explicit C-58 fail reference that discriminates V-05 (49/50 = 9.80) from V-04
(50/50 = 10.00) for the first time. C-58 fail mechanism: non-bridge positions use mixed vocabulary
(`DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` in FAIL-FIRST; `INERTIA LOCK RULE [A-16]` at FM
Inventory; `INERTIA LOCK CITATION RULE [A-19]` at defeat conditions). `DEFAULT COMPETITOR` threads
through 1 label only; `INERTIA LOCK` threads through 2 labels only. No single domain prefix achieves
3+ element threading at non-bridge positions -- C-42 precondition for C-58 is not satisfied.
**Hypothesis**: Gate body `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE
THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE THE
TRIGGER MAPPING.` passes C-57 -- `ACTOR MAPPING` derives from `ACTOR` in `FM->ACTOR BRIDGE`;
`TRIGGER MAPPING` derives from `TRIGGER` in `FM->TRIGGER BRIDGE`. C-58 fails -- `INERTIA LOCK`
threads through only 2 non-bridge labels; `DEFAULT COMPETITOR` through only 1. Neither vocabulary
satisfies the C-42 three-element threading precondition at non-bridge positions. Bridge positions
(`[BRIDGE Q3 COMMAND]:`, `[BRIDGE Q4 COMMAND]:`) are correct but insufficient to satisfy C-58
without the corresponding domain-prefix threading at non-bridge positions.
**Predicted score**: all prior criteria pass + C-55 pass + C-56 pass + C-57 pass; C-58 fail -- 49/50 = 9.80

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

## STAGE 2 COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH Q3 (FM->ACTOR BRIDGE) AND Q4 (FM->TRIGGER BRIDGE) BEEN POPULATED?

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING SECTIONS 2
THROUGH 5. IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE
ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE
THE TRIGGER MAPPING. AN INCOMPLETE BRIDGE LEAVES DEFEAT CONDITIONS WITHOUT ACTOR OR TRIGGER
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
| C-01 through C-05 | PASS | PASS | PASS | PASS | PASS |
| A-08 through A-36 | PASS carried from R18 | PASS carried from R18 | PASS carried from R18 | PASS carried from R18 | PASS carried from R18 |
| C-37 through C-54 | PASS carried from R18 | PASS carried from R18 | PASS carried from R18 | PASS carried from R18 | PASS carried from R18 |
| **C-55** | PASS | PASS | PASS | PASS | PASS (source) |
| **C-56** | FAIL | FAIL | PASS | PASS | PASS (source) |
| **C-57** | **FAIL** | **PASS** | **PASS** | **PASS** | **PASS** |
| **C-58** | FAIL | FAIL | **FAIL** | **PASS** | FAIL |

### C-57 routing clause forms by variation

| V | Gate body routing clause | C-57 verdict | Reason |
|---|--------------------------|--------------|--------|
| V-01 | `If Q3 shows N, return to Section 1A (FM->ACTOR BRIDGE) and complete the bridge artifact.` | FAIL | `bridge artifact` derives from non-discriminating `BRIDGE` component shared by both class labels |
| V-02 | `If Q3 shows N, return to Stage 2A (FM->ACTOR BRIDGE) and complete the actor mapping.` | PASS | `actor mapping` derives from discriminating `ACTOR` in `FM->ACTOR BRIDGE` |
| V-03 | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING.` | PASS | `ACTOR MAPPING` derives from `ACTOR` in `FM->ACTOR BRIDGE` |
| V-04 | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING.` | PASS | identical to V-03 routing clause |
| V-05 | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING.` | PASS (source) | criterion origin form |

### C-58 label placement by variation

| V | Non-bridge position labels | Bridge position labels | C-58 verdict | Reason |
|---|---------------------------|------------------------|--------------|--------|
| V-01 | `[A-16 PRIMARY KEY RULE]`, `[A-19 REFERENTIAL INTEGRITY RULE]` | `[BRIDGE COMPLETION COMMAND]` | FAIL | No domain-prefix vocabulary at non-bridge positions; C-42 precondition not met |
| V-02 | `PRIMARY KEY RULE [A-16]`, `CITATION INTEGRITY RULE [A-19]` | `[BRIDGE COMPLETION COMMAND]` | FAIL | No unified domain-prefix threading at non-bridge positions; C-42 precondition not met |
| V-03 | `INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]`, `INERTIA THREAT FAIL-FIRST RULE [A-31]` | `INERTIA THREAT Q3 MAPPING RULE:`, `INERTIA THREAT Q4 MAPPING RULE:` | FAIL | Domain-prefix vocabulary appears at bridge positions; positional segregation violated |
| V-04 | `INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]`, `INERTIA THREAT FAIL-FIRST RULE [A-31]` | `[BRIDGE Q3 COMMAND]:`, `[BRIDGE Q4 COMMAND]:` | PASS | Domain-prefix exclusively at non-bridge; bridge-command labels exclusively at bridge |
| V-05 | `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]`, `INERTIA LOCK RULE [A-16]`, `INERTIA LOCK CITATION RULE [A-19]` | `[BRIDGE Q3 COMMAND]:`, `[BRIDGE Q4 COMMAND]:` | FAIL | Mixed prefixes at non-bridge; no single vocabulary threads 3+ non-bridge elements; C-42 not met |

### Design questions surfaced for R19 scoring

| Question | Assessment |
|----------|------------|
| Does C-57 fail when the task noun derives from the shared (non-discriminating) component of the class label? | V-01 uses `bridge artifact` where `BRIDGE` appears in BOTH `FM->ACTOR BRIDGE` and `FM->TRIGGER BRIDGE`. Since `BRIDGE` is common to every class label, it cannot discriminate between artifact types. C-57 should fail: the task noun must derive from the discriminating component (`ACTOR`, `TRIGGER`), not the shared component. |
| Does C-58 require the specific prefix `INERTIA THREAT`, or will any consistent 3+ element domain-prefix threading satisfy it? | V-04 uses `INERTIA THREAT`. C-58 extends C-42 (vocabulary threading). The criterion should be satisfiable with any consistent domain prefix that threads through 3+ non-bridge elements exclusively -- `INERTIA THREAT` is the confirmed instance but the structural property (positional segregation) is prefix-agnostic. |
| Does V-03's C-58 fail apply even though C-42 passes (5 INERTIA THREAT elements)? | Yes. C-58 adds a positional constraint on C-42. C-42 evaluates vocabulary consistency regardless of position; C-58 evaluates whether the domain-prefix labels are positionally confined to non-bridge sections. V-03 satisfies C-42 but 2 of the 5 INERTIA THREAT labels are at bridge positions -- positional segregation violated. C-42 pass is necessary but not sufficient for C-58. |
| Does the STAGE 2 COMPLETION GATE label in V-05 satisfy C-50 (three-segment heading)? | V-05's gate heading `STAGE 2 COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH Q3 (FM->ACTOR BRIDGE) AND Q4 (FM->TRIGGER BRIDGE) BEEN POPULATED?` has three `--`-separated segments: structural label (1), enforcement command (2), binary question (3). C-50 satisfied. |
