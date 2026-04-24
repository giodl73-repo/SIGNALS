`scout-inertia-variations-R20-2026-03-17.md` written.

---

## R20 Summary

**5 variations, 3 single-axis + 2 combined. Criteria under test: C-59 and C-60.**

| V | Axis | C-59 | C-60 | Predicted |
|---|------|------|------|-----------|
| V-01 | Single: C-59 fail via generic `[BRIDGE COMMAND]:` | FAIL | PASS | 51/52 = 9.81 |
| V-02 | Single: C-59 fail via class-vocab `[BRIDGE ACTOR COMMAND]:` | FAIL | PASS | 51/52 = 9.81 |
| V-03 | Single: C-60 fail via absent trailing citations | PASS | FAIL | 51/52 = 9.81 |
| V-04 | Combined: both pass (R19 V-04 carried) | PASS | PASS | **52/52 = 10.00** |
| V-05 | Combined: both fail (generic + no citations) | FAIL | FAIL | 50/52 = 9.62 |

**Design rationale:**

- **V-01 vs V-02** isolate the two named C-59 failure forms from the rubric: V-01's generic `[BRIDGE COMMAND]:` is identical at both positions (author can't distinguish Q3 from Q4); V-02's `[BRIDGE ACTOR COMMAND]:` / `[BRIDGE TRIGGER COMMAND]:` are per-artifact but use class vocabulary, not Q-IDs. Both fail C-59, score identically, but establish distinct failure modes.

- **V-03** tests C-60 in isolation: `INERTIA THREAT` vocabulary threading intact (C-42/C-46 PASS), positional segregation intact (C-58 PASS), bridge labels carry Q-IDs (C-59 PASS) — sole change is dropping `[A-31]` / `[A-16]` / `[A-19]` from the domain-prefix labels.

- **V-04** is R19 V-04 carried unchanged — the confirmed 10.00 reference.

- **V-05** confirms additivity: C-59 + C-60 both fail independently (different structural positions, no precondition between them), landing at 50/52 = 9.62.
 by its Q-identifier from the label alone.
- **C-60 boundary (V-03)**: `INERTIA THREAT FAIL-FIRST RULE:` / `INERTIA THREAT RULE:` /
  `INERTIA THREAT CITATION RULE:` -- vocabulary threads (C-42 PASS), compound domain-axis vocabulary
  present (C-46 PASS), positional segregation maintained (C-58 PASS), but no `[A-NN]` trailing
  citation on any label. C-60 FAIL: labels are structural-role indicators but not audit-traceable to
  specific rules -- evaluator cannot locate the governing rule from the label bracket alone.
- **V-01 vs V-02 discrimination**: both fail C-59 but by distinct mechanisms. V-01 uses a single
  generic label for both artifacts (labels are identical -- author cannot distinguish Q3 from Q4
  authoring point). V-02 uses per-artifact labels with class vocabulary (labels are distinct -- author
  can distinguish the two artifacts by class name but not by Q-ID). V-01 and V-02 score identically
  under v20 (51/52 = 9.81) but establish the two distinct C-59 failure modes named in the rubric.
- **V-04 vs V-03 discrimination**: V-04 passes C-60 (3 non-bridge domain-prefix labels each carry a
  distinct trailing `[A-NN]` citation); V-03 fails C-60 (same 3 labels with vocabulary threading
  intact but no trailing citations). The labels are otherwise structurally identical -- C-60 is the
  sole discriminant between V-03 (51/52 = 9.81) and V-04 (52/52 = 10.00).
- **V-05 combined fail**: C-59 FAIL (generic `[BRIDGE COMMAND]:`) + C-60 FAIL (absent citations).
  Establishes the double-fail form that scores 50/52 = 9.62 -- lowest in R20 -- confirming both
  criteria contribute independently and additively.

---

## V-01 -- C-59 fail via generic bridge-command label (no Q-ID)

**Axis**: Single-axis: C-59 boundary test -- generic `[BRIDGE COMMAND]:` used at both bridge
authoring positions instead of `[BRIDGE Q3 COMMAND]:` / `[BRIDGE Q4 COMMAND]:`. One change from
R19 V-04: both bridge-position labels replaced with the generic form. All other R19 V-04 elements
carried unchanged, including the three domain-prefix labels with their distinct trailing citations
(C-60 PASS). This isolates C-59: does the bracket-command label at each bridge authoring position
incorporate the artifact's Q-ID?
**Hypothesis**: `[BRIDGE COMMAND]:` satisfies C-41 (two per-artifact bracket commands -- one per
section) and C-58 (bridge-command form at bridge authoring positions -- `BRIDGE` vocabulary, not
domain-prefix vocabulary). C-59 FAILS -- the same label `[BRIDGE COMMAND]:` appears at both the Q3
and Q4 authoring positions; neither label contains Q3 or Q4. An author scanning for the Q3 authoring
point cannot determine from the label alone which artifact it governs. The cross-document Q-ID
coherence chain (Q-IDs in gate interrogative C-45/C-49, gate body conditional key C-53, gate body
return target C-56) is broken at the authoring-point label. C-60 PASSES -- `INERTIA THREAT FAIL-FIRST
RULE [A-31]` / `INERTIA THREAT RULE [A-16]` / `INERTIA THREAT CITATION RULE [A-19]` carry distinct
trailing citations unchanged.
**Predicted score**: all prior criteria pass + C-57 pass + C-58 pass; C-59 fail; C-60 pass --
51/52 = 9.81

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

[BRIDGE COMMAND]: MAP each FM-[N] to the specific role experiencing the failure. VERIFY
that each actor name is a specific role title, not "users" or "the team."

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

---

## Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

[BRIDGE COMMAND]: MAP each FM-[N] to its triggering condition. QUANTIFY the measurable
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

## V-02 -- C-59 fail via class-vocabulary bridge-command label

**Axis**: Single-axis: C-59 boundary test -- class-vocabulary bridge-command labels
`[BRIDGE ACTOR COMMAND]:` / `[BRIDGE TRIGGER COMMAND]:` used at bridge authoring positions instead
of `[BRIDGE Q3 COMMAND]:` / `[BRIDGE Q4 COMMAND]:`. One change from R19 V-04: the Q-ID in each
bridge-position label is replaced with the class-discriminating vocabulary from the artifact type
annotation. All other R19 V-04 elements carried unchanged, including distinct trailing citations
(C-60 PASS). This isolates the second named C-59 failure form: class vocabulary is not the artifact
Q-ID.
**Hypothesis**: `[BRIDGE ACTOR COMMAND]:` at Q3 authoring position satisfies C-41 (per-artifact
bracket command at authoring point) and C-58 (bridge-command form: `BRIDGE` vocabulary not
domain-prefix vocabulary; labels are per-artifact with distinct content). C-59 FAILS -- `ACTOR` is
the class-discriminating vocabulary from the type annotation `FM->ACTOR BRIDGE`, not the artifact
Q-identifier `Q3`. An author scanning for the Q3 authoring point sees `[BRIDGE ACTOR COMMAND]:`
and must perform an external mapping (`ACTOR` class corresponds to Q3) rather than recognizing Q3
directly from the label. The Q-ID coherence chain is broken: Q3 appears in the gate interrogative
(C-45/C-49), the conditional key (C-53), and the return target (C-56) but not in the authoring-point
bracket label. C-60 PASSES -- domain-prefix labels carry `[A-31]` / `[A-16]` / `[A-19]` unchanged.
**Predicted score**: all prior criteria pass + C-57 pass + C-58 pass; C-59 fail; C-60 pass --
51/52 = 9.81

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

[BRIDGE ACTOR COMMAND]: MAP each FM-[N] to the specific role experiencing the failure.
VERIFY that each actor name is a specific role title, not "users" or "the team."

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

---

## Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

[BRIDGE TRIGGER COMMAND]: MAP each FM-[N] to its triggering condition. QUANTIFY the
measurable threshold that activates the failure.

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

## V-03 -- C-60 fail via absent trailing citations on domain-prefix labels

**Axis**: Single-axis: C-60 boundary test -- trailing `[A-NN]` citations removed from all three
domain-prefix labels. Three changes from R19 V-04: `INERTIA THREAT FAIL-FIRST RULE [A-31]` becomes
`INERTIA THREAT FAIL-FIRST RULE:` (colon-terminated, no citation); `INERTIA THREAT RULE [A-16]`
becomes `INERTIA THREAT RULE:`; `INERTIA THREAT CITATION RULE [A-19]` becomes `INERTIA THREAT
CITATION RULE:`. All other R19 V-04 elements carried unchanged, including `[BRIDGE Q3 COMMAND]:` /
`[BRIDGE Q4 COMMAND]:` (C-59 PASS). This isolates C-60: does each vocabulary-threaded domain-prefix
label carry a distinct trailing bracket rule-ID citation?
**Hypothesis**: Vocabulary threading is intact -- `INERTIA THREAT` appears in all three non-bridge
domain-prefix labels (C-42 PASS). Compound domain-axis vocabulary is present (C-46 PASS). Positional
segregation is maintained -- domain-prefix labels at non-bridge positions, bridge-command labels at
bridge positions (C-58 PASS). Bridge labels `[BRIDGE Q3 COMMAND]:` / `[BRIDGE Q4 COMMAND]:` carry
Q-IDs (C-59 PASS). C-60 FAILS -- `INERTIA THREAT FAIL-FIRST RULE:` / `INERTIA THREAT RULE:` /
`INERTIA THREAT CITATION RULE:` are structurally coherent role indicators but cite no specific rule
ID. An evaluator scanning for the rule governing FM identifier assignment sees `INERTIA THREAT RULE:`
and must read the label body to identify which annotation is being enforced; no audit-traceable
`[A-NN]` bracket is present in the label itself.
**Predicted score**: all prior criteria pass + C-57 pass + C-58 pass + C-59 pass; C-60 fail --
51/52 = 9.81

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

INERTIA THREAT FAIL-FIRST RULE: The inertia threat is the current workaround. It competes
without a name, a vendor, or a roadmap. It wins by default. This analysis exposes the
inertia threat's failure surface -- the specific ways it breaks -- before deriving any
defeat conditions. Every DC row must trace to a row in the failure surface inventory.
Failure modes first. Defeat conditions follow.

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

> **INERTIA THREAT RULE**: ASSIGN all FM-[N] identifiers here first. NO FM-[N] reference
> may appear in any later section without a corresponding row assigned in this table. The
> failure surface inventory is the sole source of FM identifiers.

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

> **INERTIA THREAT CITATION RULE**: EVERY FM-[N] cited in this table MUST have an assigned
> row in Section 1 (FM Inventory). DO NOT introduce FM references not assigned above. VERIFY
> before filling each row.

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

## V-04 -- C-59 + C-60 combined pass (domain-prefix positional segregation reference) -- R19 V-04 carried unchanged

**Axis**: Combined C-59 + C-60 on the domain-prefix bracket-suffix scaffold. R19 V-04 carried
unchanged. V-04 is the 10.00 reference form under v20: `[BRIDGE Q3 COMMAND]:` and
`[BRIDGE Q4 COMMAND]:` at bridge positions satisfy C-59 (Q-IDs Q3 and Q4 present in labels);
`INERTIA THREAT FAIL-FIRST RULE [A-31]` / `INERTIA THREAT RULE [A-16]` / `INERTIA THREAT CITATION
RULE [A-19]` at non-bridge positions satisfy C-60 (three distinct trailing citations). Carrying V-04
unchanged into R20 confirms C-59 and C-60 fidelity and establishes V-04 as the 52/52 = 10.00
reference form.
**Hypothesis**: C-59 PASS -- `[BRIDGE Q3 COMMAND]:` at Q3 authoring position incorporates `Q3`;
`[BRIDGE Q4 COMMAND]:` at Q4 authoring position incorporates `Q4`. Q-IDs appear at every
per-artifact structural position: gate interrogative (C-45/C-49), conditional key (C-53), return
target section name (C-56), and the authoring-point bracket-command label (C-59) -- the coherence
loop is closed. C-60 PASS -- `[A-31]`, `[A-16]`, `[A-19]` are three distinct trailing citations on
three vocabulary-threaded domain-prefix labels at non-bridge positions. Evaluator can locate each
specific governing rule from the label bracket alone without reading the label body.
**Predicted score**: all criteria pass including C-59 and C-60 -- 52/52 = 10.00

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

## V-05 -- C-59 fail (generic) + C-60 fail (absent citations) combined

**Axis**: Combined double-fail: C-59 FAIL via generic `[BRIDGE COMMAND]:` + C-60 FAIL via absent
trailing citations. Two sets of changes from R19 V-04: (1) `[BRIDGE Q3 COMMAND]:` and
`[BRIDGE Q4 COMMAND]:` replaced with `[BRIDGE COMMAND]:` at both bridge authoring positions;
(2) trailing `[A-NN]` citations removed from all three domain-prefix labels. C-58 is maintained --
bridge-command form at bridge positions and domain-prefix labels at non-bridge positions (positional
segregation intact). This establishes the double-fail reference form scoring 50/52 = 9.62,
confirming both criteria contribute independently and additively.
**Hypothesis**: C-58 PASS -- `[BRIDGE COMMAND]:` is bridge-command vocabulary (not domain-prefix);
domain-prefix labels remain at non-bridge positions. Positional segregation intact. C-59 FAIL --
generic `[BRIDGE COMMAND]:` at both bridge positions; neither label contains Q3 or Q4. C-60 FAIL --
`INERTIA THREAT FAIL-FIRST RULE:` / `INERTIA THREAT RULE:` / `INERTIA THREAT CITATION RULE:` carry
no trailing `[A-NN]` citations. Two points lost: one for C-59 (bridge-label Q-ID absent), one for
C-60 (label citations absent). C-59 and C-60 address distinct structural positions (bridge authoring
labels vs. non-bridge domain-prefix labels) and fail independently -- no precondition relationship
between them in either direction.
**Predicted score**: all prior criteria pass + C-57 pass + C-58 pass; C-59 fail; C-60 fail --
50/52 = 9.62

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

INERTIA THREAT FAIL-FIRST RULE: The inertia threat is the current workaround. It competes
without a name, a vendor, or a roadmap. It wins by default. This analysis exposes the
inertia threat's failure surface -- the specific ways it breaks -- before deriving any
defeat conditions. Every DC row must trace to a row in the failure surface inventory.
Failure modes first. Defeat conditions follow.

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

> **INERTIA THREAT RULE**: ASSIGN all FM-[N] identifiers here first. NO FM-[N] reference
> may appear in any later section without a corresponding row assigned in this table. The
> failure surface inventory is the sole source of FM identifiers.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                       |                                    |                             |                             |
| FM-2   |                                                                                       |                                    |                             |                             |

---

## Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

[BRIDGE COMMAND]: MAP each FM-[N] to the specific role experiencing the failure. VERIFY
that each actor name is a specific role title, not "users" or "the team."

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

---

## Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

[BRIDGE COMMAND]: MAP each FM-[N] to its triggering condition. QUANTIFY the measurable
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

> **INERTIA THREAT CITATION RULE**: EVERY FM-[N] cited in this table MUST have an assigned
> row in Section 1 (FM Inventory). DO NOT introduce FM references not assigned above. VERIFY
> before filling each row.

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
