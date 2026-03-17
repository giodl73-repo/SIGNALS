# scout-inertia -- Quest Variate R17

**Rubric**: v17 (ceiling 260 = 100 essential base + 32 advanced criteria x 5 pts)
**Date**: 2026-03-17
**Previous round**: R16 all 5 variations predicted 250/250 under v16. V-02 introduced
STRUCTURAL FAULTS (TYPE=structural, LOCUS=faults) as a compound-noun A-38 form on the STAGE
scaffold. V-01 carried STRUCTURAL WEAKNESSES (TYPE=structural, LOCUS=weaknesses). V-03 tested
EACH cardinality with FAILURE SURFACE. V-04 tested FAILURE VECTORS. V-05 fixed A-37 schema
inconsistency and tested COLLAPSE POINTS + BOTH READY?.
**R17 target**: First 260/260 candidates. Under v17, only STRUCTURAL FAULTS satisfies both
A-40 (engineering-register locus: FAULTS = specific defect plane) and A-41 (architectural-
scope TYPE: STRUCTURAL = architectural/systemic category). STRUCTURAL WEAKNESSES satisfies
A-41 but fails A-40. All FAILURE-TYPE forms (FAILURE SURFACE, FAILURE VECTORS, FAILURE POINTS,
COLLAPSE POINTS) fail A-41 (event-descriptor TYPE, not architectural-scope TYPE). Therefore
STRUCTURAL FAULTS is the only confirmed form reaching 260/260. R16 V-02 carries STRUCTURAL
FAULTS on STAGE scaffold -- confirmed as 260/260 reference under v17. V-01 upgrades R16 V-01
(STRUCTURAL WEAKNESSES on SECTION scaffold) to STRUCTURAL FAULTS. V-03 combines STRUCTURAL
FAULTS with EACH cardinality on SECTION scaffold. V-04 and V-05 test combined axes on STAGE
and SECTION scaffolds respectively with novel axis vocabulary.
**New criteria**: A-40 + A-41

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | A-40+A-41 single-axis upgrade on R16 V-01 SECTION scaffold | R16 V-01 had STRUCTURAL WEAKNESSES (A-41 pass, A-40 fail, 255/260 under v17); upgrade FM heading subtitle WEAKNESSES -> FAULTS -- tests STRUCTURAL FAULTS on SECTION 1-7 schema as first 260/260 SECTION candidate |
| V-02 | Reference carry -- R16 V-02 (STAGE scaffold, STRUCTURAL FAULTS confirmed) | R16 V-02 introduced STRUCTURAL FAULTS on STAGE scaffold, predicted 250/250 under v16; under v17 rubric STRUCTURAL FAULTS satisfies both A-40 and A-41 -- 260/260 confirmed carry |
| V-03 | A-39 single-axis EACH variant with STRUCTURAL FAULTS on SECTION scaffold | R16 V-03 tested EACH with FAILURE SURFACE (A-39 candidate, A-40+A-41 both fail); upgrade to STRUCTURAL FAULTS -- tests whether EACH + STRUCTURAL FAULTS simultaneously achieves both A-39 and A-40+A-41 on SECTION schema |
| V-04 | Combined: novel axis vocabulary + STRUCTURAL FAULTS + BOTH READY? on STAGE scaffold | Novel framing "THE INCUMBENT'S STRUCTURAL FAULTS"; STAGE schema from R16 V-02; BOTH BRIDGE ARTIFACTS READY? tests READY? completion verb alongside confirmed BOTH cardinality |
| V-05 | Combined: novel axis vocabulary + STRUCTURAL FAULTS + BOTH BUILT? on SECTION scaffold | Novel framing "THE DEFAULT OPTION'S STRUCTURAL FAULTS"; SECTION schema; BOTH BRIDGE ARTIFACTS BUILT? tests BUILT? completion verb alongside confirmed BOTH cardinality -- closes out completion-verb space |

---

## R17 Design Notes

### A-40 -- Engineering-register locus noun status across R16 forms

| Form | A-38 | A-40 | A-41 | v17 score |
|------|------|------|------|-----------|
| STRUCTURAL WEAKNESSES | PASS | FAIL (WEAKNESSES = general vulnerability, not fault-taxonomy) | PASS (STRUCTURAL = architectural scope) | +5 A-41 only |
| STRUCTURAL FAULTS | PASS | PASS (FAULTS = specific defect planes, engineering register) | PASS (STRUCTURAL = architectural scope) | +10 A-40+A-41 |
| FAILURE SURFACE | PASS | FAIL (SURFACE = spatial metaphor, not fault-taxonomy) | FAIL (FAILURE = event descriptor) | 0 |
| FAILURE VECTORS | PASS | FAIL (VECTORS = propagation metaphor, not fault-taxonomy) | FAIL (FAILURE = event descriptor) | 0 |
| COLLAPSE POINTS | PASS | FAIL (POINTS = general loci, not fault-taxonomy) | FAIL (COLLAPSE = mechanism descriptor, not architectural scope) | 0 |

Only STRUCTURAL FAULTS satisfies both new criteria. V-01 in R16 scored 250/250 but would
score 255/260 under v17 (A-40 miss). V-02 in R16 already has STRUCTURAL FAULTS and scores
260/260 under v17.

### A-41 -- Architectural-scope TYPE: why STRUCTURAL passes and FAILURE/COLLAPSE fail

STRUCTURAL signals that the FM Inventory catalogues architecturally-scoped vulnerabilities --
failures that require architectural change to resolve. FAILURE names a failure event at
unspecified abstraction level. COLLAPSE names a failure mechanism (total breakdown). Neither
FAILURE nor COLLAPSE classifies failures at the architectural scope level that signals to a
reader: "these are the design-level faults, not implementation incidents."

STRUCTURAL + any locus noun produces an A-41-passing form. But only STRUCTURAL + an
engineering-fault-taxonomy locus (FAULTS, FAILURE PLANES, FRACTURE ZONES) also passes A-40.
STRUCTURAL FAULTS is the minimal form satisfying both.

### R16 incoming state on new criteria

| Variation | A-38 | A-40 | A-41 | v17 predicted score |
|-----------|------|------|------|---------------------|
| V-01 (STRUCTURAL WEAKNESSES, SECTION) | PASS | FAIL | PASS | 255/260 |
| V-02 (STRUCTURAL FAULTS, STAGE) | PASS | PASS | PASS | 260/260 |
| V-03 (FAILURE SURFACE, SECTION) | PASS | FAIL | FAIL | 250/260 |
| V-04 (FAILURE VECTORS, STAGE) | PASS | FAIL | FAIL | 250/260 |
| V-05 (COLLAPSE POINTS, STAGE) | PASS | FAIL | FAIL | 250/260 |

### Cardinality forms under test in R17

| Variation | Form | Status |
|-----------|------|--------|
| V-01 | ALL BRIDGE ARTIFACTS COMPLETE? | Confirmed (R16 V-01) |
| V-02 | ALL BRIDGE ARTIFACTS COMPLETE? | Confirmed (R16 V-02) |
| V-03 | EACH BRIDGE ARTIFACT VERIFIED? | Candidate (tested R16 V-03, unconfirmed vs A-40+A-41) |
| V-04 | BOTH BRIDGE ARTIFACTS READY? | READY? completion verb new; BOTH confirmed (R16 V-03 BOTH BUILT?) |
| V-05 | BOTH BRIDGE ARTIFACTS BUILT? | BUILT? carry from R16 V-03 base; SECTION schema new context |

---

## V-01 -- A-40+A-41 single-axis upgrade on R16 V-01 SECTION scaffold

**Axis**: Single-axis A-40+A-41 upgrade on R16 V-01. R16 V-01 achieved 250/250 under v16
with STRUCTURAL WEAKNESSES (A-38 pass) on SECTION 1-7 schema. Under v17 it scores 255/260
(A-41 pass, A-40 fail). The single change: FM Inventory heading subtitle STRUCTURAL WEAKNESSES
replaced by STRUCTURAL FAULTS. FAIL-FIRST body text updated to "structural faults" for A-26
axis vocabulary coherence. All other elements carry unchanged.
**Hypothesis**: STRUCTURAL FAULTS on SECTION scaffold achieves 260/260. A-40 PASS: FAULTS is
an engineering-fault-taxonomy locus noun (specific defect plane, fault-tree analysis register).
A-41 PASS: STRUCTURAL is architectural-scope TYPE (unchanged from STRUCTURAL WEAKNESSES).
A-37 PASS: SECTION 1-7 schema throughout + SECTION 2 gate, schema unchanged from R16 V-01
(confirmed). A-39 PASS: ALL BRIDGE ARTIFACTS COMPLETE? unchanged from R16 V-01 (confirmed).
**Predicted score**: 260/260

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

FAIL-FIRST CONSTRAINT [A-31]: The inertia threat is the current workaround. It competes
without a vendor, a demo, or a champion. It wins by default unless teams encounter a
specific, observable reason to leave. Map the inertia threat's structural faults first.
Every defeat condition and every switching cost threshold derives only from a documented
structural fault. No defeat condition is valid without a traceable structural fault behind it.

Bridge artifacts required before defeat conditions are authored:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the specific role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## SECTION 1 -- THE INERTIA THREAT'S STRUCTURAL FAULTS: FAILURE MODE INVENTORY

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

## V-02 -- Reference carry: R16 V-02 (STRUCTURAL FAULTS, STAGE scaffold)

**Axis**: Reference carry. R16 V-02 introduced STRUCTURAL FAULTS on STAGE scaffold as an
A-38 single-axis upgrade, predicted 250/250 under v16. Under v17: STRUCTURAL FAULTS satisfies
both A-40 (FAULTS = engineering-register locus, specific defect plane) and A-41 (STRUCTURAL =
architectural-scope TYPE). No changes from R16 V-02. STAGE 1-6 schema throughout. "THE STATUS
QUO'S STRUCTURAL FAULTS" FM heading subtitle. ALL BRIDGE ARTIFACTS COMPLETE? gate
interrogative. All 250/250 criteria from R16 V-02 carry intact.
**Hypothesis**: R16 V-02 achieves 260/260 under v17 -- the first confirmed 260/260 reference
form. A-40 PASS: FAULTS is explicitly confirmed in the v17 rubric A-40 criterion description
("Confirmed by R16 V-02 (STRUCTURAL FAULTS, explicit scoring note: FAULTS is a technically
more precise locus noun -- fault = specific defect plane vs. weakness = general vulnerable
zone)"). A-41 PASS: STRUCTURAL confirmed by A-41 criterion ("Confirmed by R16 V-01 and V-02
(both STRUCTURAL TYPE; scoring note: TYPE=structural (architectural/systemic category))").
A-37 PASS: STAGE 1-6 throughout + STAGE 2 gate = STAGE/STAGE schema consistent (confirmed
R16). A-39 PASS: ALL BRIDGE ARTIFACTS COMPLETE? confirmed R16.
**Predicted score**: 260/260

---

```
## FAIL-FIRST DECLARATION -- THE STATUS QUO AS UNNAMED COMPETITOR

FAIL-FIRST CONSTRAINT [A-31]: Map the status quo's structural faults before writing a single
defeat condition. The status quo is the unnamed competitor -- no name, no sales team, no
roadmap. It persists because switching costs are real and structural faults are invisible.
This analysis makes both visible. Failure modes first; defeat conditions follow from them.

Authoring sequence:
- Stage 1 -- FAILURE MODE INVENTORY (C-05): the status quo's structural faults
- Stage 2 -- BRIDGE STAGE: Q3 (FM->actor, closes C-05 -> R-02) + Q4 (FM->trigger, closes
  C-05 -> C-04) + completion gate
- Stage 3 -- WORKAROUND PROFILE (C-01): specific tool, role, ongoing cost
- Stage 4 -- SWITCHING COST (C-02): quantified cost to abandon the status quo
- Stage 5A -- THREAT ASSESSMENT (C-03): inertia threat score
- Stage 5B -- DEFEAT CONDITIONS (C-04): conditions under which the status quo loses
- Stage 6 -- COMPLETENESS CHECK

The Stage 2 gate must show Y for both bridge artifacts before Stage 3 is authored.

---

## STAGE 1 -- THE STATUS QUO'S STRUCTURAL FAULTS: FAILURE MODE INVENTORY

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

## V-03 -- A-39 single-axis EACH variant with STRUCTURAL FAULTS on SECTION scaffold

**Axis**: Single-axis A-39 on SECTION scaffold with STRUCTURAL FAULTS. R16 V-03 tested EACH
BRIDGE ARTIFACT VERIFIED? cardinality form with FAILURE SURFACE compound noun -- EACH was an
A-39 candidate but FAILURE SURFACE failed A-40+A-41, so the v17 score would be 250/260.
R17 V-03 upgrades the compound noun from FAILURE SURFACE to STRUCTURAL FAULTS (satisfying
A-40+A-41), keeping EACH BRIDGE ARTIFACT VERIFIED? as the A-39 cardinality form. SECTION 1-6
schema. Axis vocabulary: "THE INERTIA THREAT'S STRUCTURAL FAULTS." All other elements carry
from R16 V-03 (domain-prefix rule labels, INERTIA THREAT RULE [A-16], INERTIA THREAT CITATION
RULE [A-19]).
**Hypothesis**: EACH + STRUCTURAL FAULTS achieves 260/260. A-40 PASS: FAULTS = engineering-
register locus (fault-taxonomy term). A-41 PASS: STRUCTURAL = architectural-scope TYPE. A-39
PASS: EACH is a universal per-element quantifier -- "EACH BRIDGE ARTIFACT VERIFIED?" names the
artifact class (BRIDGE ARTIFACT) and encodes that every member of the class must be verified
(EACH = distributive universal), confirming the required count is total-set, not partial.
A-37 PASS: SECTION 1-6 hierarchy throughout + SECTION 2 gate = SECTION/SECTION schema
consistent (carried from R16 V-03 confirmation inference).
**Predicted score**: 260/260

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

INERTIA THREAT FAIL-FIRST RULE [A-31]: The inertia threat is the current workaround.
It competes without a name, a vendor, or a roadmap. It wins by default. This analysis
exposes the inertia threat's structural faults -- the specific architectural defects that
make it brittle -- before deriving any defeat conditions. Every DC row must trace to a
row in the structural faults inventory.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## SECTION 1 -- THE INERTIA THREAT'S STRUCTURAL FAULTS: FAILURE MODE INVENTORY

> [C-05 COMMAND]: NAME every specific failure mode where the inertia threat (current
> workaround) breaks, produces errors, causes rework, or hits a scale ceiling. ASSIGN an
> FM-[N] identifier to each row. MINIMUM 2 rows. REJECT generic descriptions -- "slow" or
> "manual" alone fails; "CSV export silently truncates rows at 65,536 with no error message"
> passes.

> **INERTIA THREAT RULE [A-16]**: ASSIGN all FM-[N] identifiers here first. NO FM-[N]
> reference may appear in any later section without a corresponding row assigned in this
> table. The structural faults inventory is the sole source of FM identifiers.

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

## SECTION 2 COMPLETION GATE -- EACH BRIDGE ARTIFACT VERIFIED?

[BRIDGE COMPLETION COMMAND]: CONFIRM EACH BRIDGE ARTIFACT IS POPULATED BEFORE AUTHORING
SECTIONS 3 THROUGH 6. If either row is N, DO NOT PROCEED. Return to Section 1 and complete
the missing bridge artifact. An incomplete bridge leaves defeat conditions without actor or
trigger chains.

| Bridge artifact                                | Verified? (Y / N) |
|------------------------------------------------|-------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                   |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                   |

---

## SECTION 3 -- WORKAROUND PROFILE

> [C-01 COMMAND]: NAME the specific inertia threat -- the exact tool name, file type, or
> procedure. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost
> with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 4 -- SWITCHING COST

> [C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a
> number and a unit. NAME the role bearing each cost.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 5 -- THREAT ASSESSMENT

> [C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH -- the inertia threat
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

## V-04 -- Combined: novel axis vocabulary + STRUCTURAL FAULTS + BOTH READY? on STAGE scaffold

**Axis**: Two combined axes on STAGE scaffold. (1) Novel inertia framing: "THE INCUMBENT'S
STRUCTURAL FAULTS" -- uses THE INCUMBENT as the axis subject (tests a new vocabulary token
against confirmed STRUCTURAL FAULTS compound noun). (2) A-39 cardinality variant: BOTH BRIDGE
ARTIFACTS READY? -- BOTH is a confirmed cardinality quantifier (R16 V-03 base form), READY? is
a new completion verb replacing COMPLETE?. Base scaffold: R16 V-04 structure (STAGE 1-6,
consolidated bridge stage) with compound noun upgraded from FAILURE VECTORS to STRUCTURAL
FAULTS.
**Hypothesis**: 260/260. A-40 PASS: FAULTS = engineering-register locus (unchanged from V-01
and V-02 analysis). A-41 PASS: STRUCTURAL = architectural-scope TYPE (unchanged). A-38 PASS:
STRUCTURAL FAULTS is a confirmed compound failure noun (TYPE+LOCUS). A-37 PASS: STAGE 1-6
hierarchy throughout + STAGE 2 gate = STAGE/STAGE schema consistent (same pattern as R16
V-02, confirmed). A-39 PASS: BOTH is a confirmed cardinality quantifier (R16 V-03 base);
READY? as completion verb does not affect A-39 (the criterion requires a cardinality quantifier
alongside the artifact class name -- the completion verb is not evaluated by A-39).
**Predicted score**: 260/260

---

```
## FAIL-FIRST DECLARATION -- THE INCUMBENT WORKAROUND

[A-31 FAIL-FIRST ORDERING RULE]: The incumbent workaround is the competitor already
deployed. It has no marketing, no roadmap, and no champion -- but it is already paid for,
already trained on, and already embedded in every workflow. Map the incumbent's structural
faults before constructing any defeat condition. A defeat condition without a traceable
structural fault is speculation, not analysis.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the specific role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## STAGE 1 -- THE INCUMBENT'S STRUCTURAL FAULTS: FAILURE MODE INVENTORY

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

### STAGE 2 COMPLETION GATE -- BOTH BRIDGE ARTIFACTS READY?

[BRIDGE COMPLETION COMMAND]: Do not proceed to Stage 3 unless both Q3 and Q4 show Y below.
An incomplete bridge leaves defeat conditions without actor and trigger chains.

| Bridge artifact                                | Ready? (Y / N) |
|------------------------------------------------|----------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                |

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

## V-05 -- Combined: novel axis vocabulary + STRUCTURAL FAULTS + BOTH BUILT? on SECTION scaffold

**Axis**: Two combined axes on SECTION scaffold. (1) Novel inertia framing: "THE DEFAULT
OPTION'S STRUCTURAL FAULTS" -- uses THE DEFAULT OPTION as the axis subject, naming the
inertia competitor from the decision-frame perspective (the option that wins when teams make
no decision). Distinct from INERTIA THREAT (R16 V-01, V-03), STATUS QUO (R16 V-02), UNNAMED
COMPETITOR (R16 V-03 base), INCUMBENT (R16 V-04). (2) A-39 cardinality variant: BOTH BRIDGE
ARTIFACTS BUILT? -- BOTH is a confirmed cardinality quantifier; BUILT? is a new completion
verb not yet tested in the SECTION schema context (R16 V-03 base used BUILT? on SECTION
scaffold before being replaced by VERIFIED? for the EACH test). SECTION 1-6 schema throughout
(Q3 and Q4 are unnumbered bridge sections between Section 1 and Section 2 gate).
**Hypothesis**: 260/260. A-40 PASS: FAULTS = engineering-register locus. A-41 PASS:
STRUCTURAL = architectural-scope TYPE. A-38 PASS: STRUCTURAL FAULTS compound noun confirmed
across V-01 through V-04. A-37 PASS: SECTION 1-6 hierarchy + SECTION 2 gate = SECTION/SECTION
schema consistent. A-39 PASS: BOTH is a confirmed cardinality quantifier alongside BRIDGE
ARTIFACTS; BUILT? as the completion verb does not affect A-39 scoring (criterion evaluates
the quantifier alongside the class name, not the completion verb). Domain-prefix rule labels
("DEFAULT OPTION RULE [A-16]", "DEFAULT OPTION CITATION RULE [A-19]") provide axis vocabulary
coherence under A-26 and contribute to A-23 criterion-ID-in-label coverage.
**Predicted score**: 260/260

---

```
## FAIL-FIRST DECLARATION -- THE DEFAULT OPTION

DEFAULT OPTION FAIL-FIRST RULE [A-31]: The default option is what teams keep when they make
no decision. It requires no evaluation, no approval, and no transition plan. It wins by
inaction. Map the default option's structural faults before writing a single defeat condition.
A defeat condition without a traceable structural fault is a claim without evidence.
STRUCTURAL FAULTS FIRST. DEFEAT CONDITIONS SECOND.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the specific role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition

---

## SECTION 1 -- THE DEFAULT OPTION'S STRUCTURAL FAULTS: FAILURE MODE INVENTORY

> [C-05 COMMAND]: NAME every specific failure mode where the default option (current
> workaround) breaks, produces errors, causes rework, or hits a scale ceiling. ASSIGN an
> FM-[N] identifier to each row. MINIMUM 2 rows. REJECT generic descriptions -- "slow" or
> "manual" alone fails; "batch job silently skips records exceeding memory limit with no
> alert" passes.

> **DEFAULT OPTION RULE [A-16]**: ASSIGN all FM-[N] identifiers here first. NO FM-[N]
> reference may appear in any later section without a corresponding row assigned in this
> table. The structural faults inventory is the sole source of FM identifiers for this
> document.

| FM-[N] | Failure description (e.g., batch job silently skips records exceeding memory limit -- no alert) | Actor / role (e.g., data-ops team) | Trigger (e.g., dataset > 500MB) | Frequency (e.g., 3x/week) |
|--------|------------------------------------------------------------------------------------------------|------------------------------------|----------------------------------|---------------------------|
| FM-1   |                                                                                                |                                    |                                  |                           |
| FM-2   |                                                                                                |                                    |                                  |                           |

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

| FM-[N] | Triggering condition (e.g., dataset ingested exceeds 500MB) | Measurable threshold (e.g., >500MB, >3 skips/week) |
|--------|-------------------------------------------------------------|-----------------------------------------------------|
| FM-1   |                                                             |                                                     |
| FM-2   |                                                             |                                                     |

---

## SECTION 2 COMPLETION GATE -- BOTH BRIDGE ARTIFACTS BUILT?

[BRIDGE COMPLETION COMMAND]: CONFIRM BOTH BRIDGE ARTIFACTS ARE BUILT BEFORE AUTHORING
SECTIONS 3 THROUGH 6. If either row shows N, DO NOT PROCEED. Return to Section 1 and
complete the missing bridge artifact. Defeat conditions without built bridge artifacts
lack their actor and trigger chains.

| Bridge artifact                                | Built? (Y / N) |
|------------------------------------------------|----------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                |

---

## SECTION 3 -- WORKAROUND PROFILE

> [C-01 COMMAND]: NAME the specific default option -- the exact tool name, file type, or
> procedure. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost
> with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 4 hours/week) | Duration in active use (e.g., 14 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 4 -- SWITCHING COST

> [C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a
> number and a unit. NAME the role bearing each cost.

| Cost category          | Description | Estimate (e.g., 5 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 5 -- THREAT ASSESSMENT

> [C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH -- the default option
> always starts with home-field advantage. IF deviating from HIGH, STATE a specific
> quantified condition; a qualitative judgment is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 6 -- DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
> trigger mapping. CITE the FM-[N] driving each condition. "Teams switch when they see value"
> fails -- every DC row must name a testable, measurable condition.

> **DEFAULT OPTION CITATION RULE [A-19]**: EVERY FM-[N] cited in this table MUST have an
> assigned row in Section 1 (FM Inventory). DO NOT introduce FM references not assigned
> above. VERIFY before filling each row.

| DC-[N] | Defeat condition (falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >500MB, >3 skips/week) | Team type or segment |
|--------|-------------------------------|-------------------|----------------------------------------------------|----------------------|
| DC-1   |                               |                   |                                                    |                      |
| DC-2   |                               |                   |                                                    |                      |

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
