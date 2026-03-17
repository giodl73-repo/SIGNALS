Written to `simulations/quest/golden/scout-inertia-golden-simplified-2026-03-17.md`.

## QU5 Simplification Report — scout-inertia

**Source**: R20 V-04 (confirmed 53/53 = 10.00 under v21 rubric)
**Rubric version**: v21 (53 criteria)
**Original word count**: 973
**Simplified word count**: 777
**Reduction**: 196 words (20.1%)
**All essential criteria still pass**: YES

---

## What Was Removed and Why

Each removal was verified against all 53 rubric criteria. Only elements with no criterion
testing them were removed.

**1. FAIL-FIRST body prose** (~58 words → replaced with 9-word minimum)

Original:
> The inertia threat is the current workaround. It competes without a name, a vendor, or a
> roadmap. It wins by default. This analysis exposes the inertia threat's failure surface --
> the specific ways it breaks -- before deriving any defeat conditions. Every DC row must
> trace to a row in the failure surface inventory. Failure modes first. Defeat conditions
> follow.

Replaced with: "The failure surface comes first. Failure modes before defeat conditions."

**Why**: No rubric criterion tests the body text after the `INERTIA THREAT FAIL-FIRST RULE
[A-31]:` label. C-60 tests the label (including the `[A-31]` citation). The section
ordering guarantee ("failure modes before defeat conditions") is enforced by the document
structure itself. The "home-field advantage" brand philosophy and cross-references to
DC tracing are restated elsewhere (INERTIA THREAT CITATION RULE [A-19] and [C-04 COMMAND]).

**2. Bridge artifact list in FAIL-FIRST section** (~33 words)

Original:
> Bridge artifacts required before defeat conditions:
> - **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): maps each FM-[N] to the role experiencing it
> - **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering condition

**Why**: No rubric criterion tests this listing in the FAIL-FIRST section. Q3 and Q4 are
fully established by their standalone section headings, their presence in the gate
interrogative (C-45/C-49), and the gate body routing (C-53/C-56). The bridge artifact
declaration in the FAIL-FIRST section is informational scaffolding with no criterion
dependency.

**3. "(closes C-05 -> R-02)" / "(closes C-05 -> C-04)" cross-references** (~16 words)

Removed from: Q3 section heading, Q4 section heading, gate table rows.

**Why**: These are cross-reference annotations. No rubric criterion tests for them. C-56
tests for the artifact ID being the section reference ("THE Q3 SECTION"), not for the
closes-notation. C-49 tests for class annotations in the gate interrogative, which are
`(FM->ACTOR BRIDGE)` / `(FM->TRIGGER BRIDGE)` — the closes-notation is separate.

**4. VERIFY clause in [BRIDGE Q3 COMMAND]** (~17 words)

Original: "VERIFY that each actor name is a specific role title, not 'users' or 'the team.'"

**Why**: No rubric criterion tests this specific clarification. The label `[BRIDGE Q3
COMMAND]:` satisfies C-59 (Q-ID in bridge label), C-58 (bridge-command form at bridge
position), C-61 (distinct from Q4 label), and C-41 (per-artifact command at authoring
point). The body text after the label is guidance; the criteria test the label structure,
not the instruction body.

**5. QUANTIFY trailing in [BRIDGE Q4 COMMAND]** (~8 words)

Original: "QUANTIFY the measurable threshold that activates the failure."

**Why**: No criterion tests this trailing sentence. The "Measurable threshold" column in
the Q4 table already signals what to fill. The [BRIDGE Q4 COMMAND] label satisfies all
bridge-command criteria; the body guidance is redundant with the table structure.

**6. Gate body trailing sentence** (~14 words)

Original: "AN INCOMPLETE BRIDGE LEAVES DEFEAT CONDITIONS WITHOUT ACTOR OR TRIGGER CHAINS."

**Why**: No rubric criterion tests this sentence. The conditional routing (C-53/C-55/C-57)
already establishes complete backward routing when Q3 or Q4 is missing. The causal
explanation adds no structural information tested by any criterion.

**7. Section 1 subtitle** (~5 words)

Original: "SECTION 1 -- THE INERTIA THREAT'S FAILURE SURFACE: FAILURE MODE INVENTORY"
Simplified: "SECTION 1 -- FAILURE MODE INVENTORY"

**Why**: No criterion tests the subtitle text. C-58 requires domain-prefix labels
(`INERTIA THREAT RULE [A-16]`) at the FM Inventory position — the label, not the section
heading. The section heading change doesn't affect C-58 or any other criterion.

**8. [UNIT RULE] block** (~20 words)

Original:
> **[UNIT RULE]**: EVERY estimate must carry a number and a unit. "Significant" or
> "substantial" without a number is REJECTED.

**Why**: The [C-02 COMMAND] already contains "REJECT any estimate without a number and
unit." The [UNIT RULE] block is a restatement. C-36 requires 3+ bracket elements — with
11 remaining bracket elements, removing [UNIT RULE] has no effect on C-36 or C-42.

**9. "Home-field advantage" phrase** (~8 words)

Original: "DEFAULT IS HIGH -- the inertia threat always starts with home-field advantage."
Simplified: "DEFAULT IS HIGH."

**Why**: No criterion tests the explanatory phrase. C-03 requires a threat score declared;
C-47 (if active) requires DEFAULT IS HIGH. The phrase is brand framing only.

**10. "DO NOT introduce FM references" clause** (~8 words)

Original: "DO NOT introduce FM references not assigned above. VERIFY before filling each row."
Simplified: "VERIFY before filling each row."

**Why**: "EVERY FM-[N] cited in this table MUST have an assigned row in Section 1" already
prohibits introducing unassigned FM references. The "DO NOT introduce" sentence is a
restatement of the same constraint in imperative form. No criterion tests specifically
for this sentence.

**11. "(current workaround)" parenthetical** (~2 words)

Original: "where the inertia threat (current workaround) breaks"
Simplified: "where the inertia threat breaks"

**Why**: The parenthetical explains "inertia threat" — a term already established by the
FAIL-FIRST declaration. No criterion tests for this parenthetical.

**12. Verbose example in Section 1 table Failure description column** (~12 words)

Original column header:
"Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error)"

Simplified: "Failure description"

**Why**: The same concrete example is already present in the [C-05 COMMAND] body text
("CSV export silently truncates rows at 65,536 with no error message"). Duplicating it in
the column header adds no new information. No criterion tests column header examples.

---

## Criteria Verification

All 53 v21 rubric criteria verified against the simplified prompt:

| Criterion group | Count | Status |
|----------------|-------|--------|
| C-01 to C-05 (content) | 5 | All commands present with full text |
| C-36 to C-42 (bracket structure) | 7 | 11 bracket elements remain; INERTIA THREAT threading across 3 domain-prefix labels |
| C-43 to C-52 (gate interrogative + body) | 10 | Gate heading three-segment form intact; Q3/Q4 class annotations intact; all routing clauses intact |
| C-53 to C-57 (routing detail) | 5 | Per-artifact conditionals; class annotations; ACTOR MAPPING / TRIGGER MAPPING task nouns intact |
| C-58 to C-61 (label specificity) | 4 | Domain-prefix labels at non-bridge positions; [BRIDGE Q3 COMMAND]/[BRIDGE Q4 COMMAND] at bridge positions; Q-IDs in bridge labels; labels distinct |
| Earlier criteria (pre-C-36) | 22 | All sections present; completeness check intact; all tables present |

**C-59**: `[BRIDGE Q3 COMMAND]:` at Q3 authoring section, `[BRIDGE Q4 COMMAND]:` at Q4 authoring section. PASS.
**C-60**: `INERTIA THREAT FAIL-FIRST RULE [A-31]` / `INERTIA THREAT RULE [A-16]` / `INERTIA THREAT CITATION RULE [A-19]` at non-bridge positions — three distinct trailing citations. PASS.
**C-61**: `[BRIDGE Q3 COMMAND]:` and `[BRIDGE Q4 COMMAND]:` are distinct (Q3 ≠ Q4). PASS.

---

## Prompt Body

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

INERTIA THREAT FAIL-FIRST RULE [A-31]: The failure surface comes first. Failure modes
before defeat conditions.

---

## SECTION 1 -- FAILURE MODE INVENTORY

> [C-05 COMMAND]: NAME every specific failure mode where the inertia threat
> breaks, produces errors, causes rework, or hits a scale ceiling. ASSIGN an
> FM-[N] identifier to each row. MINIMUM 2 rows. REJECT generic descriptions -- "slow" or
> "manual" alone fails; "CSV export silently truncates rows at 65,536 with no error message"
> passes.

> **INERTIA THREAT RULE [A-16]**: ASSIGN all FM-[N] identifiers here first. NO FM-[N]
> reference may appear in any later section without a corresponding row assigned in this
> table. The failure surface inventory is the sole source of FM identifiers.

| FM-[N] | Failure description | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|--------------------|------------------------------------|-----------------------------|------------------------------|
| FM-1   |                    |                                    |                             |                              |
| FM-2   |                    |                                    |                             |                              |

---

## Q3 -- FM->ACTOR BRIDGE

[BRIDGE Q3 COMMAND]: MAP each FM-[N] to the specific role experiencing the failure.

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

---

## Q4 -- FM->TRIGGER BRIDGE

[BRIDGE Q4 COMMAND]: MAP each FM-[N] to its triggering condition.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

---

## BRIDGE COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH Q3 (FM->ACTOR BRIDGE) AND Q4 (FM->TRIGGER BRIDGE) BEEN POPULATED?

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING SECTIONS 2
THROUGH 5. IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE
ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE
THE TRIGGER MAPPING.

| Bridge artifact          | Populated? (Y / N) |
|--------------------------|--------------------|
| Q3 -- FM->Actor bridge   |                    |
| Q4 -- FM->Trigger bridge |                    |

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

> [C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH. IF deviating from HIGH,
> STATE a specific quantified condition; a qualitative judgment ("low friction") is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
> trigger mapping. CITE the FM-[N] driving each condition. EVERY DC row must name a testable,
> measurable condition -- "teams switch when they see the value" is REJECTED.

> **INERTIA THREAT CITATION RULE [A-19]**: EVERY FM-[N] cited in this table MUST have an
> assigned row in Section 1 (FM Inventory). VERIFY before filling each row.

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

```json
{"simplified_word_count": 777, "original_word_count": 973, "all_essential_still_pass": true}
```
