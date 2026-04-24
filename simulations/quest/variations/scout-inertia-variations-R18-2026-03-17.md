The R18 variations are written to `simulations/quest/variations/scout-inertia-variations-R18-2026-03-17.md`.

---

## R18 Summary

**New criteria: C-55 (completion-action directive) and C-56 (artifact-name routing). Each is a new dimension on the gate body backward routing clause.**

### Variation axes

| V | Single-axis | C-55 | C-56 | Key routing clause |
|---|-------------|------|------|--------------------|
| **V-01** | C-55 on section-based scaffold | PASS | FAIL | `If Q3 shows N, return to Section 1A (FM->ACTOR BRIDGE) and complete the actor mapping.` |
| **V-02** | C-55 on stage-based scaffold | PASS | FAIL | `If Q3 shows N, return to Stage 2A (FM->ACTOR BRIDGE) and complete the actor mapping.` |
| **V-03** | C-56 on artifact-name scaffold | FAIL | PASS | `Return to the Q3 section (FM->ACTOR BRIDGE) if Q3 shows N;` |
| **V-04** | C-55 + C-56 combined, domain-prefix register | PASS | PASS | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING.` |
| **V-05** | Reference form (R17 V-05 unchanged) | PASS (source) | PASS (source) | Same as V-04 — the criterion origin |

### Structural notes

- **C-56 applicability**: V-01 and V-02 use ordinal scaffolds (Section 1A, Stage 2A) — these cannot satisfy C-56 by structural necessity. The applicability condition requires Q3/Q4 to be standalone sections whose primary label IS the artifact ID.
- **V-03 isolation**: R17 V-05 structure minus the completion-action — tests whether C-56 is independently satisfiable.
- **V-04 register test**: domain-prefix bracket-suffix notation throughout (`INERTIA THREAT RULE [A-16]`, `[BRIDGE Q3 COMMAND]:`) with the V-05 gate body form — tests C-55+C-56 register-agnosticism.
- **V-05 unchanged**: source of both C-55 and C-56 excellence signals; carried unchanged as the reference form.
ete the actor mapping` / `and complete the trigger mapping`
as completion-action directives appended to each annotated return clause. The ordinal target
forms (Section 1A, Stage 2A) are preserved unchanged — these cannot satisfy C-56 (ordinal
label requires author to mentally map from artifact ID to section name).

V-03 is the C-56 isolation test. It uses the R17 V-05 scaffold structure (Q3/Q4 as standalone
top-level sections) but removes the completion-action directive from the gate body routing.
This tests whether C-56 (artifact-name routing via `the Q3 section`) is independently satisfied
without C-55 (completion-action).

V-04 tests C-55 + C-56 in the domain-prefix bracket-suffix register (phrasing-axis variation on
the combined criteria). The scaffold restructures Q3/Q4 as standalone top-level sections (required
for C-56) while using domain-prefix bracket-suffix notation throughout (INERTIA THREAT RULE [A-16],
[BRIDGE Q3 COMMAND]:, etc.). The gate body is all-caps to match R17 V-05's register, satisfying
both C-55 and C-56 in this alternative stylistic environment.

V-05 is carried unchanged from R17. It was the source of C-55 and C-56 excellence signals and
remains the reference form for both criteria. Carrying it unchanged into R18 confirms criterion
fidelity and avoids masking the signal by introducing new axes on the reference scaffold.

### Open questions for scoring

- Does C-55 require a specific verb (`COMPLETE`, `complete`) or does any task-naming directive
  satisfy it? V-01/V-02 use lowercase `complete the actor mapping`; V-04/V-05 use all-caps
  `AND COMPLETE THE ACTOR MAPPING`. C-54 and C-53 were register-agnostic; C-55 expected to be
  the same.
- Does C-55 require the completion-action to appear AFTER the return-target annotation, or can it
  precede the parenthetical class? All variations place the completion-action after `(FM->ACTOR
  BRIDGE)` — the most restrictive interpretation is satisfied.
- Does C-56 require exact identifier matching (`THE Q3 SECTION` matching `Q3` in the artifact ID)
  or is partial matching (`the Q3 section` lowercase) sufficient? V-03 uses lowercase `the Q3
  section`; V-04/V-05 use all-caps `THE Q3 SECTION`. C-56 is expected to be register-agnostic.
- Can C-55 be satisfied when the conditional key is lowercase (`if Q3 shows N`) vs. all-caps
  (`IF Q3 SHOWS N`)? V-01/V-02 use lowercase keys; V-04/V-05 use all-caps. The completion-action
  criterion governs the presence of the task directive, not the register of the conditional key.

---

## V-01 -- C-55 on section-based scaffold (Section 1A/1B form)

**Axis**: Single-axis: C-55 completion-action directive added to gate body return routing,
applied to R17 V-01's section-based scaffold (Section 1A/1B naming, lowercase conditional
form). All R17 V-01 passing elements carried unchanged. Single change: gate body return routing
upgraded from annotated targets (`Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N;
return to Section 1B (FM->TRIGGER BRIDGE) if Q4 shows N.`) to completion-action form (`If Q3
shows N, return to Section 1A (FM->ACTOR BRIDGE) and complete the actor mapping. If Q4 shows
N, return to Section 1B (FM->TRIGGER BRIDGE) and complete the trigger mapping.`).
**Hypothesis**: Adding `and complete the actor mapping` / `and complete the trigger mapping`
as completion-action directives after each annotated return target satisfies C-55 -- each
conditional routing clause now delivers destination + artifact class + specific task in a
single self-contained instruction. C-56 is NOT satisfied because the return targets remain
ordinal labels (`Section 1A`, `Section 1B`) -- the author must still mentally map from
artifact ID Q3 to Section 1A. C-55 and C-56 are independently evaluable per the rubric.
**Predicted score**: all prior criteria pass + C-55 pass; C-56 fail

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
If Q3 shows N, return to Section 1A (FM->ACTOR BRIDGE) and complete the actor mapping.
If Q4 shows N, return to Section 1B (FM->TRIGGER BRIDGE) and complete the trigger mapping.

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

## V-02 -- C-55 on stage-based scaffold (Stage 2A/2B reference form)

**Axis**: Single-axis: C-55 completion-action directive added to gate body return routing,
applied to R17 V-02's stage-based scaffold (Stage 2A/2B naming, lowercase conditional form).
All R17 V-02 passing elements carried unchanged. Single change: gate body return routing
upgraded from annotated targets (`Return to Stage 2A (FM->ACTOR BRIDGE) if Q3 shows N;
return to Stage 2B (FM->TRIGGER BRIDGE) if Q4 shows N.`) to completion-action form (`If Q3
shows N, return to Stage 2A (FM->ACTOR BRIDGE) and complete the actor mapping. If Q4 shows
N, return to Stage 2B (FM->TRIGGER BRIDGE) and complete the trigger mapping.`). This is the
R18 reference form for minimum-viable C-55 -- smallest possible change from R17 on the
confirmed stage-based reference scaffold.
**Hypothesis**: `If Q3 shows N, return to Stage 2A (FM->ACTOR BRIDGE) and complete the actor
mapping.` passes C-55 -- the clause names a return location (Stage 2A), annotates it with an
artifact class (FM->ACTOR BRIDGE per C-54), and names the specific work to be completed on
arrival (and complete the actor mapping per C-55). Stage headings already establish `FM->ACTOR
BRIDGE` vocabulary; the completion-action `complete the actor mapping` introduces no new
terminology. C-56 is NOT satisfied -- `Stage 2A` is an ordinal label that requires the author
to know Q3 maps to Stage 2A. C-55 and C-56 address orthogonal properties of the routing
clause and can be satisfied independently.
**Predicted score**: all prior criteria pass + C-55 pass; C-56 fail

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

## V-03 -- C-56 only on artifact-name scaffold (Q3/Q4 standalone sections, no C-55)

**Axis**: Single-axis: C-56 artifact-name routing tested in isolation. Based on R17 V-05
scaffold structure (Q3 and Q4 as standalone top-level sections whose primary label IS the
artifact ID) but with the completion-action directive removed from the gate body. The gate
body uses artifact-name return targets (`the Q3 section`, `the Q4 section`) with class
annotations present (satisfying C-54 and C-56) but no completion-action directive (failing
C-55). This variation tests whether C-56 is independently satisfiable without C-55.
**Hypothesis**: `Return to the Q3 section (FM->ACTOR BRIDGE) if Q3 shows N; return to the
Q4 section (FM->TRIGGER BRIDGE) if Q4 shows N.` satisfies C-56 -- the return target
(`the Q3 section`) uses the artifact ID (Q3) as the section reference, matching the
conditional key (`Q3 shows N`) with zero mapping overhead. C-53 satisfied (per-artifact
decomposition with distinct targets). C-54 satisfied (class annotation present). C-56
satisfied (artifact-name routing: Q3 and Q4 occupy standalone sections whose primary label
IS the artifact ID; `the Q3 section` is isomorphic with the artifact ID). C-55 NOT satisfied
-- the clause does not name the specific work to be completed on arrival. C-55 and C-56 are
orthogonal dimensions and can be satisfied independently per the rubric.
**Predicted score**: all prior criteria pass + C-56 pass; C-55 fail

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

## STAGE 2 COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?

[BRIDGE COMPLETION COMMAND]: Complete the Q3 section and the Q4 section before proceeding
to Sections 2 through 5. Do not author the workaround profile or defeat conditions unless
both rows below show Y. An incomplete bridge leaves defeat conditions without actor or
trigger chains.
Return to the Q3 section (FM->ACTOR BRIDGE) if Q3 shows N; return to the Q4 section
(FM->TRIGGER BRIDGE) if Q4 shows N.

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

## V-04 -- C-55 + C-56 combined on domain-prefix bracket-suffix scaffold

**Axis**: Combined C-55 + C-56 on the domain-prefix bracket-suffix phrasing-register
scaffold (INERTIA THREAT RULE [A-16], INERTIA THREAT CITATION RULE [A-19], [BRIDGE Q3
COMMAND]:, [BRIDGE Q4 COMMAND]: notation). The scaffold restructures Q3 and Q4 as
standalone top-level sections whose primary label IS the artifact ID (required for C-56 --
applicability condition satisfied). Gate body uses all-caps completion-action form with
artifact-name routing, satisfying both C-55 and C-56 within the domain-prefix bracket-suffix
register. Tests whether C-55 + C-56 are register-agnostic when applied together (previous
rounds confirmed C-53 and C-54 are register-agnostic; this variation extends that test to
C-55 and C-56 in the combined form).
**Hypothesis**: `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE
THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND
COMPLETE THE TRIGGER MAPPING.` satisfies both C-55 and C-56 within the domain-prefix
bracket-suffix register. The gate body form is identical to R17 V-05's reference form --
only the surrounding scaffold register differs (domain-prefix bracket-suffix throughout:
INERTIA THREAT RULE [A-16] instead of [A-16 PRIMARY KEY RULE]; [BRIDGE Q3 COMMAND]: instead
of standard [C-05 COMMAND]: notation for the bridge sections). C-55 and C-56 are governed by
the gate body routing clause form, not the surrounding register; both criteria should be
register-agnostic and satisfied here.
**Predicted score**: all prior criteria pass + C-55 pass + C-56 pass

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

## V-05 -- C-55 + C-56 reference form (all-axes-combined, all-caps COMMAND register)

**Axis**: Carry R17 V-05 body unchanged. R17 V-05 was the source of both the C-55 and C-56
excellence signals. The gate body `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR
BRIDGE) AND COMPLETE THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION
(FM->TRIGGER BRIDGE) AND COMPLETE THE TRIGGER MAPPING.` satisfies C-51 (named return path),
C-53 (per-artifact decomposition), C-54 (class annotation at each return target), C-55
(completion-action directive at each return target), and C-56 (artifact-name routing:
THE Q3 SECTION and THE Q4 SECTION use the artifact IDs as section references). Carrying
V-05 unchanged into R18 establishes it as the reference form for both C-55 and C-56 and
confirms that V-01/V-02's lowercase ordinal-target completion-action form is the minimum
C-55 form while V-05's all-caps artifact-name form is the extended form satisfying both.
**Hypothesis**: R17 V-05 already satisfies C-55 and C-56 as the source of both criteria.
Carrying it unchanged confirms criterion fidelity. All prior criteria pass (established
across R01-R17). C-55 and C-56 confirmed by criterion origin.
**Predicted score**: all prior criteria pass + C-55 pass + C-56 pass (reference form)

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
| C-01 through C-05 | PASS | PASS | PASS | PASS | PASS |
| A-08 through A-36 | PASS carried from R17 | PASS carried from R17 | PASS carried from R17 | PASS carried from R17 | PASS carried from R17 |
| C-37 through C-54 | PASS carried from R17 | PASS carried from R17 | PASS carried from R17 | PASS carried from R17 | PASS carried from R17 |
| **C-55** | **PASS** | **PASS** | FAIL | **PASS** | **PASS (source)** |
| **C-56** | FAIL | FAIL | **PASS** | **PASS** | **PASS (source)** |

### C-55 and C-56 routing clause forms by variation

| V | Gate body routing clause | C-55 | C-56 |
|---|--------------------------|------|------|
| V-01 | `If Q3 shows N, return to Section 1A (FM->ACTOR BRIDGE) and complete the actor mapping. If Q4 shows N, return to Section 1B (FM->TRIGGER BRIDGE) and complete the trigger mapping.` | PASS (completion-action present) | FAIL (Section 1A -- ordinal) |
| V-02 | `If Q3 shows N, return to Stage 2A (FM->ACTOR BRIDGE) and complete the actor mapping. If Q4 shows N, return to Stage 2B (FM->TRIGGER BRIDGE) and complete the trigger mapping.` | PASS (completion-action present) | FAIL (Stage 2A -- ordinal) |
| V-03 | `Return to the Q3 section (FM->ACTOR BRIDGE) if Q3 shows N; return to the Q4 section (FM->TRIGGER BRIDGE) if Q4 shows N.` | FAIL (no completion-action) | PASS (Q3 section -- artifact-name) |
| V-04 | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE THE TRIGGER MAPPING.` | PASS (completion-action present) | PASS (THE Q3 SECTION -- artifact-name) |
| V-05 | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE THE TRIGGER MAPPING.` | PASS (source) | PASS (source) |

### C-56 applicability notes

V-01 and V-02 use ordinal scaffold structures (Section 1A/1B and Stage 2A/2B respectively).
These cannot satisfy C-56 by structural necessity: the applicability condition for C-56
requires bridge artifacts to occupy standalone sections whose primary label IS the artifact ID.
Section 1A and Stage 2A are ordinal labels; the mapping from `Q3 -> Section 1A` requires
external knowledge. V-03, V-04, and V-05 satisfy the applicability condition by placing Q3 and
Q4 as standalone top-level sections whose primary label is the artifact ID (`## Q3 -- FM->ACTOR
BRIDGE`). In these scaffolds `THE Q3 SECTION` is isomorphic with `Q3` -- the same base
identifier appears in the artifact row, the conditional key, and the return target.

### Design questions surfaced for R18 scoring

| Question | Assessment |
|----------|------------|
| Does C-55 require all-caps `AND COMPLETE THE` or is lowercase `and complete the` sufficient? | V-01/V-02 use lowercase; V-04/V-05 use all-caps. C-53 and C-54 were register-agnostic (confirmed in prior rounds). C-55 expected to be register-agnostic for the same reason. |
| Does C-55 require the conditional key to precede the return instruction (`IF Q3 SHOWS N, RETURN`)? | V-01/V-02 use post-conditional form (`return to X if Q3 shows N`); V-04/V-05 use pre-conditional form (`IF Q3 SHOWS N, RETURN`). C-55 governs the presence and content of the completion-action directive, not the grammatical position of the conditional key. |
| Does C-56 require exact identifier case (`THE Q3 SECTION` matching `Q3`) or is case-insensitive matching sufficient? | V-03 uses lowercase `the Q3 section`; V-04/V-05 use all-caps `THE Q3 SECTION`. C-56 is expected to be register-agnostic -- the structural property is the isomorphism between artifact ID and section reference, not the case of the reference. |
| Can V-04's combined gate heading satisfy both C-50 (three-segment heading) and C-49 (per-artifact class annotation in interrogative)? | V-04's gate heading `BRIDGE COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH Q3 (FM->ACTOR BRIDGE) AND Q4 (FM->TRIGGER BRIDGE) BEEN POPULATED?` carries three `--`-separated segments (structural label, enforcement command, binary question) satisfying C-50, and per-artifact parenthetical class annotations in the interrogative satisfying C-49. Both criteria independently satisfied. |
