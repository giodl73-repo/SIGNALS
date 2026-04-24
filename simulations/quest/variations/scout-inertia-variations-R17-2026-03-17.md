The R17 variations are written to `simulations/quest/variations/scout-inertia-variations-R17-2026-03-17.md`.

---

## R17 Summary

**5 variations, all predicted prior criteria pass + C-54 pass.**

### Variation axes

| V | Axis | Key C-54 change from R16 |
|---|------|--------------------------|
| **V-01** | C-54 only, section-based scaffold (Section 1A/1B) | `Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N; return to Section 1B (FM->TRIGGER BRIDGE) if Q4 shows N.` |
| **V-02** | C-54 only, stage-based scaffold (Stage 2A/2B) — reference form | `Return to Stage 2A (FM->ACTOR BRIDGE) if Q3 shows N; return to Stage 2B (FM->TRIGGER BRIDGE) if Q4 shows N.` |
| **V-03** | C-54 on phrasing-register scaffold (domain-prefix A-23) | Same Section 1A/1B annotation form; tests C-54 register-agnosticism against bracket-suffix style |
| **V-04** | C-54 on consolidated-bridge scaffold (bracket-prefix A-23, A-36 combined heading) | Same Stage 2A/2B annotation form; combined heading unchanged, body routing independently annotated |
| **V-05** | C-54 reference form (all-caps, all-axes-combined) | Carry R16 V-05 unchanged — source of the C-54 excellence signal; all-caps artifact-name-based targets with class annotation |

### Design rationale

The single change across V-01 through V-04 is adding the parenthetical class label to each bare return target from R16. The annotation form `(FM->ACTOR BRIDGE)` / `(FM->TRIGGER BRIDGE)` mirrors the vocabulary already present in the bridge section headings — no new terminology is introduced. V-05 is carried unchanged as the rubric's reference annotated example, confirming that the lowercase forms in V-01 through V-04 are the minimum form while V-05's all-caps form is the extended form.

### Open questions for scoring

- Is `(FM->ACTOR BRIDGE)` sufficient, or does C-54 require exact vocabulary matching the section heading? (All variations echo section heading vocabulary.)
- Is the annotation's position significant — must it attach to the return target noun phrase inside the conditional clause? (All variations place it there directly.)
- Is register significant for C-54 — lowercase vs. all-caps? (C-53 was register-agnostic; C-54 expected to be the same.)
rtifact decomposition requirement.

**V-05 unchanged from R16**: R16 V-05 was the source of the C-54 excellence signal. Carrying it unchanged into R17 confirms it as the reference form and avoids masking the signal by introducing new axes.

### Open questions for scoring

- Does `(FM->ACTOR BRIDGE)` satisfy C-54, or does the annotation need to use the exact artifact-class vocabulary from the bridge heading (e.g., `FM->ACTOR BRIDGE` vs `FM-ACTOR-BRIDGE` vs `Actor Bridge`)?
- Does C-54 require the class annotation to appear inside the conditional clause itself (attached to the return target noun phrase), or can it appear elsewhere in the gate body paragraph?
- V-01/V-02 use lowercase annotations; V-05 uses uppercase. Is register significant for C-54, or is it register-agnostic like C-53?

---

## V-01 -- C-54 on section-based scaffold (Section 1A/1B form)

**Axis**: Single-axis: C-54 parenthetical class annotation on return routing targets, applied
to R16 V-01's section-based scaffold (Section 1A/1B naming). All R16 passing elements
carried unchanged. Single change: gate body return routing upgraded from bare targets
(`Return to Section 1A if Q3 shows N; return to Section 1B if Q4 shows N.`) to annotated
targets (`Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N; return to Section 1B
(FM->TRIGGER BRIDGE) if Q4 shows N.`).
**Hypothesis**: Adding `(FM->ACTOR BRIDGE)` and `(FM->TRIGGER BRIDGE)` parenthetical
annotations to the return targets satisfies C-54 -- each conditional routing clause now
self-documents the artifact class at the return location, making the backward path
informative beyond just naming the target section. The section headings already carry
`FM->ACTOR BRIDGE` and `FM->TRIGGER BRIDGE` vocabulary (from A-33 artifact class), so
the annotation is consistent with existing document vocabulary and not a new term
introduction.
**Predicted score**: all prior criteria pass + C-54 pass

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

## SECTION 2 COMPLETION GATE -- BOTH BRIDGE ARTIFACTS COMPLETE?

[BRIDGE COMPLETION COMMAND]: Complete Section 1A (Q3) and Section 1B (Q4) before
proceeding to Sections 3 through 6. Do not author the workaround profile or defeat
conditions unless both rows below show Y. An incomplete bridge means defeat conditions
lack their actor and trigger chains.
Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N; return to Section 1B
(FM->TRIGGER BRIDGE) if Q4 shows N.

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

## V-02 -- C-54 on stage-based scaffold (Stage 2A/2B reference form)

**Axis**: Single-axis: C-54 parenthetical class annotation on return routing targets, applied
to R16 V-02's stage-based scaffold (Stage 2A/2B naming). All R16 passing elements carried
unchanged. Single change: gate body return routing upgraded from bare targets (`Return to
Stage 2A if Q3 shows N; return to Stage 2B if Q4 shows N.`) to annotated targets (`Return
to Stage 2A (FM->ACTOR BRIDGE) if Q3 shows N; return to Stage 2B (FM->TRIGGER BRIDGE) if
Q4 shows N.`). This is the R17 reference form -- minimal single-axis change on the confirmed
R16 stage-based reference scaffold.
**Hypothesis**: `Return to Stage 2A (FM->ACTOR BRIDGE) if Q3 shows N; return to Stage 2B
(FM->TRIGGER BRIDGE) if Q4 shows N.` passes C-54 -- each conditional routing clause names
a distinct target (C-53) AND annotates that target with its artifact class in parenthetical
form. The stage headings `STAGE 2A -- Q3 -- FM->ACTOR BRIDGE` and `STAGE 2B -- Q4 --
FM->TRIGGER BRIDGE` already establish the artifact-class vocabulary; the gate body
annotation replicates it at the return routing location, making each return path
self-documenting.
**Predicted score**: all prior criteria pass + C-54 pass

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

### STAGE 2 COMPLETION GATE -- BOTH BRIDGE ARTIFACTS COMPLETE?

[BRIDGE COMPLETION COMMAND]: Complete Stage 2A (Q3) and Stage 2B (Q4) before proceeding
to Stage 3. Do not author Stage 3 through Stage 5B unless both rows below show Y. Defeat
conditions without bridge artifacts lack their actor and trigger chains.
Return to Stage 2A (FM->ACTOR BRIDGE) if Q3 shows N; return to Stage 2B
(FM->TRIGGER BRIDGE) if Q4 shows N.

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

## V-03 -- C-54 on phrasing-register scaffold (domain-prefix A-23)

**Axis**: C-54 parenthetical class annotation on return routing targets, applied to R16
V-03's domain-prefix phrasing-register scaffold (INERTIA THREAT RULE / INERTIA THREAT
CITATION RULE bracket-suffix style, Section 1A/1B naming). All R16 passing elements carried
unchanged. Single change: gate body return routing upgraded from bare annotated targets to
class-annotated form. Domain-prefix bracket-suffix A-23 style (`INERTIA THREAT RULE [A-16]`,
`INERTIA THREAT CITATION RULE [A-19]`, `[BRIDGE Q3 COMMAND]:`, `[BRIDGE Q4 COMMAND]:`)
maintained throughout unchanged.
**Hypothesis**: C-54 is register-agnostic -- the parenthetical class annotation in return
routing satisfies C-54 regardless of whether the surrounding scaffold uses domain-prefix
bracket-suffix notation, standard bracket-prefix commands, or all-caps commands. The
annotation `(FM->ACTOR BRIDGE)` / `(FM->TRIGGER BRIDGE)` is a standalone addition to the
conditional routing clause and does not interact with bracket-label style.
**Predicted score**: all prior criteria pass + C-54 pass

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

INERTIA THREAT FAIL-FIRST RULE [A-31]: The inertia threat is the current workaround.
It competes without a name, a vendor, or a roadmap. It wins by default. This analysis
exposes the inertia threat's failure surface -- the specific ways it breaks -- before
deriving any defeat conditions. Every DC row must trace to a row in the failure surface
inventory.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role
  experiencing it (housed in Section 1A)
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition (housed in Section 1B)

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

## SECTION 1A -- Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

[BRIDGE Q3 COMMAND]: MAP each FM-[N] to the specific role experiencing the failure.
VERIFY that each actor name is a specific role title, not "users" or "the team."

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

---

## SECTION 1B -- Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

[BRIDGE Q4 COMMAND]: MAP each FM-[N] to its triggering condition. QUANTIFY the measurable
threshold that activates the failure.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

---

## SECTION 2 COMPLETION GATE -- BOTH BRIDGE ARTIFACTS BUILT?

[BRIDGE COMPLETION COMMAND]: CONFIRM Section 1A (Q3) AND Section 1B (Q4) ARE POPULATED
BEFORE AUTHORING SECTIONS 3 THROUGH 6. An incomplete bridge leaves defeat conditions
without actor or trigger chains.
Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N; return to Section 1B
(FM->TRIGGER BRIDGE) if Q4 shows N.

| Bridge artifact                                | Built? (Y / N) |
|------------------------------------------------|----------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)  |                |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                |

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

> [C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH -- the inertia threat
> always starts with home-field advantage. IF deviating from HIGH, STATE a specific quantified
> condition; a qualitative judgment ("low friction") is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 6 -- DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the
> Section 1B (Q4) trigger mapping. CITE the FM-[N] driving each condition. "Teams switch
> when they see the value" fails -- every DC row must name a testable, measurable condition.

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

## V-04 -- C-54 on consolidated-bridge scaffold (bracket-prefix A-23)

**Axis**: C-54 parenthetical class annotation on return routing targets, applied to R16
V-04's consolidated-bridge scaffold (bracket-prefix A-23 style, Stage 2A/2B sub-stage
naming within Stage 2, combined gate heading A-36). All R16 passing elements carried
unchanged. Single change: gate body return routing upgraded from bare targets (`Return to
Stage 2A if Q3 shows N; return to Stage 2B if Q4 shows N.`) to annotated targets (`Return
to Stage 2A (FM->ACTOR BRIDGE) if Q3 shows N; return to Stage 2B (FM->TRIGGER BRIDGE) if
Q4 shows N.`). Combined gate heading `STAGE 2 -- [BRIDGE COMPLETION COMMAND]: CONFIRM --
ALL BRIDGE ARTIFACTS COMPLETE?` carried unchanged (A-36, A-33, A-25 all preserved).
**Hypothesis**: The combined gate heading and the gate body return routing are structurally
independent. C-54 annotates only the gate body's return routing clauses -- the combined
heading form (A-36) is unaffected. The bracket-prefix A-23 style (`[A-16 PRIMARY KEY
CONSTRAINT]`, `[A-19 CITATION INTEGRITY CONSTRAINT]`) is orthogonal to the class annotation
in the return routing. C-54 can be satisfied within a consolidated-bridge structure where
Q3/Q4 are sub-headings within Stage 2 rather than standalone sections.
**Predicted score**: all prior criteria pass + C-54 pass

---

```
## FAIL-FIRST DECLARATION -- THE INCUMBENT WORKAROUND

[A-31 FAIL-FIRST ORDERING RULE]: The incumbent workaround is the competitor already
deployed. It has no marketing, no roadmap, and no champion -- but it is already paid for,
already trained on, and already embedded in every workflow. Map the incumbent's
failure points before constructing any defeat condition. A defeat condition without a
traceable failure point is speculation, not analysis.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the specific role
  experiencing it (authored in Stage 2A)
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition (authored in Stage 2B)

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

### STAGE 2A -- Q3 -- FM->ACTOR BRIDGE (closes C-05 -> R-02)

Map each failure mode to the specific role experiencing it. Bridge closes C-05 to R-02.

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

### STAGE 2B -- Q4 -- FM->TRIGGER BRIDGE (closes C-05 -> C-04)

Map each failure mode to its triggering condition and measurable threshold. Bridge closes
C-05 to C-04.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

### STAGE 2 -- [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL BRIDGE ARTIFACTS COMPLETE?

Do not proceed to Stage 3 unless both Stage 2A (Q3) and Stage 2B (Q4) show Y below.
Return to Stage 2A (FM->ACTOR BRIDGE) if Q3 shows N; return to Stage 2B
(FM->TRIGGER BRIDGE) if Q4 shows N.

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

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Stage
> 2B (Q4) trigger mapping. CITE the FM-[N] driving each condition. Every condition must be
> measurable and testable -- "teams switch when they see the value" fails.

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

## V-05 -- C-54 reference form (all-axes-combined, all-caps COMMAND register)

**Axis**: Carry R16 V-05 body unchanged. R16 V-05 was the source of the C-54 excellence
signal -- it already satisfied C-54 with per-artifact all-caps conditional routing with
parenthetical class annotations: `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR
BRIDGE) AND COMPLETE THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION
(FM->TRIGGER BRIDGE) AND COMPLETE THE TRIGGER MAPPING.` V-05's form uses artifact-name-
based section references (`Q3 SECTION`, `Q4 SECTION`) rather than ordinal labels (Section
1A, Stage 2A), with class annotations carried in all-caps uppercase to match the surrounding
register. Carrying V-05 unchanged into R17 establishes it as the reference form for C-54
and confirms that V-01 through V-04's lowercase annotation form is the minimum form while
V-05's full-caps form is the extended form.
**Hypothesis**: R16 V-05 already passes C-54 as the source of the criterion. Carrying it
unchanged confirms criterion fidelity and serves as the rubric's reference annotated example.
All prior criteria pass (established in R16). C-54 pass confirmed by criterion origin.
**Predicted score**: all prior criteria pass + C-54 pass (reference form)

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
| C-01 through C-05 | PASS x5 | PASS x5 | PASS x5 | PASS x5 | PASS x5 |
| A-08 through A-36 | PASS carried from R16 | PASS carried from R16 | PASS carried from R16 | PASS carried from R16 | PASS carried from R16 |
| C-37 through C-53 | PASS carried from R16 | PASS carried from R16 | PASS carried from R16 | PASS carried from R16 | PASS carried from R16 |
| **C-54** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS (source)** |

### C-54 annotation forms by variation

| V | Return routing clause (annotated form) |
|---|----------------------------------------|
| V-01 | `Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N; return to Section 1B (FM->TRIGGER BRIDGE) if Q4 shows N.` |
| V-02 | `Return to Stage 2A (FM->ACTOR BRIDGE) if Q3 shows N; return to Stage 2B (FM->TRIGGER BRIDGE) if Q4 shows N.` |
| V-03 | `Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N; return to Section 1B (FM->TRIGGER BRIDGE) if Q4 shows N.` |
| V-04 | `Return to Stage 2A (FM->ACTOR BRIDGE) if Q3 shows N; return to Stage 2B (FM->TRIGGER BRIDGE) if Q4 shows N.` |
| V-05 | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE THE TRIGGER MAPPING.` |

### C-54 design questions surfaced

| Question | Assessment |
|----------|------------|
| Does `(FM->ACTOR BRIDGE)` satisfy C-54, or must annotation match the exact heading vocabulary? | V-01/V-03 use `(FM->ACTOR BRIDGE)` matching the section heading; V-05 uses all-caps. If C-54 requires vocabulary fidelity, V-01/V-03/V-04 satisfy by direct section-heading echo. |
| Does C-54 require the annotation to be inside the conditional clause (attached to return target noun), or can it be elsewhere in the gate body? | All five variations attach the annotation directly to the return target noun phrase within the conditional clause -- the most restrictive interpretation is satisfied. |
| Is register significant for C-54? (lowercase V-01/V-02/V-03/V-04 vs. all-caps V-05) | C-53 was established as register-agnostic (R16 confirmed). C-54 should be register-agnostic for the same reason -- the structural property is the presence and placement of the annotation, not its case. |
| Can a single sentence carry two C-54-passing clauses? | V-01/V-02/V-03/V-04 use semicolon-joined two-clause form; V-05 uses separate sentences in ALL-CAPS. Both forms pass C-53 (per-artifact decomposition). C-54 requires annotation on each target; both forms satisfy this. |
