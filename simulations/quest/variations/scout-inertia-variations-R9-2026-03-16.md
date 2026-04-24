Good — no prior R9 golden files. Writing fresh. Here are the 5 complete variations.

---

# scout-inertia — R9 Variations (V-01 through V-05)

## Variation Axis Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | Output format | A-12 + A-19 + A-20 over A-10+A-13+A-14+A-16 scaffold | Q3/Q4 as named rows in a dedicated BRIDGE ARTIFACTS section with explicit criterion-chain references satisfies A-12; no embedded questions (A-11/A-17 will fail — tests the tabular axis cleanly) |
| V-02 | Lifecycle emphasis | A-12 + A-10 + A-11 + A-17 | Q3/Q4 named as lifecycle stages in the FAIL-FIRST DECLARATION preamble (before FM content), echoed as post-FM verification; embedded criterion questions drive lifecycle ordering |
| V-03 | Phrasing register | A-11 + A-17 + A-12 | Imperative criterion-labeled commands throughout; Q3 and Q4 as labeled BRIDGE COMMANDs with chain references embedded in the FM section itself |
| V-04 | Output format + lifecycle | A-12 + A-11 + A-17 + A-19 + A-20 | Q3/Q4 named in lifecycle preamble AND as structured verification tables; full tabular schema + embedded questions stacked |
| V-05 | All three axes | All 12 advanced criteria | Tables + lifecycle preamble + imperative commands + Q3/Q4 everywhere + A-19 + A-20 + binary checklist |

---

## V-01

**Axis**: Output format — entire output is a structured table template; Q3 and Q4 are named items in a dedicated BRIDGE ARTIFACTS section positioned between the FM Inventory and the Workaround Profile, each carrying an explicit criterion-chain reference.

**Hypothesis**: Making Q3 and Q4 explicit named artifacts in the template body — not column headers, not implied by ordering — with the text "(closes C-05 → R-02)" and "(closes C-05 → C-04)" satisfies A-12's named-artifact requirement. The A-10 + A-13 + A-14 + A-16 + A-19 scaffold surrounds them. A-11 and A-17 will fail (no embedded questions) — this is the clean single-axis test.

---

```
You are running /scout:inertia for the feature: {TOPIC}.

Produce the complete inertia analysis below. Fill every table cell. A blank cell
in any table is a visible structural failure. Do not describe what you will do;
produce the output directly.

---

# INERTIA ANALYSIS — {TOPIC}

## FAIL-FIRST DECLARATION

Failure modes are enumerated before the workaround profile. Every defeat condition
and switching cost threshold depends on what breaks first. Populate Section 1 before
any other section.

---

## SECTION 1 — FAILURE MODE INVENTORY

> **PRIMARY KEY CONSTRAINT**: No FM-[N] identifier may appear in any downstream
> section of this document unless it has an assigned row in this table. Assign all
> FM-[N] identifiers here first before referencing them elsewhere.

| FM-[N] | Failure description — what specifically goes wrong | Actor / role experiencing it | Trigger condition — what specifically causes it | Frequency (e.g., 3×/month) |
|--------|---------------------------------------------------|-----------------------------|-------------------------------------------------|---------------------------|
| FM-01  |                                                   |                             |                                                 |                           |
| FM-02  |                                                   |                             |                                                 |                           |

Minimum 2 rows required. "Manual is slow" fails — name the specific error,
truncation, silent failure, or data loss event.

---

## BRIDGE ARTIFACTS

Two bridge artifacts are required before Section 2. They verify structural closure
between the FM Inventory and the downstream analysis.

**Q3 — FM→ACTOR CLOSURE** (closes C-05 → R-02): Verify that every FM-[N] row
in Section 1 names a specific role in the Actor column — not "the team", not
"users", not "engineers". The actor must be a named role (e.g., "data-ops team",
"QA engineer", "on-call SRE"). FM rows with unroled actors cannot support
role-level defeat conditions in Section 5.

| FM-[N] | Named role present? (Y / N) | Revision required if N |
|--------|-----------------------------|------------------------|
| FM-01  |                             |                        |
| FM-02  |                             |                        |

**Q4 — FM→TRIGGER CLOSURE** (closes C-05 → C-04): Verify that every FM-[N]
row in Section 1 carries a falsifiable trigger condition — not "sometimes",
not "when usage grows", but a specific event or threshold ("when file > 10MB",
"on the third concurrent write"). Triggers are the raw material for defeat
conditions in Section 5. A trigger without a threshold cannot generate a
falsifiable defeat condition.

| FM-[N] | Falsifiable trigger present? (Y / N) | Revision required if N |
|--------|--------------------------------------|------------------------|
| FM-01  |                                      |                        |
| FM-02  |                                      |                        |

Both verification tables must show all Y before proceeding to Section 2.

---

## SECTION 2 — WORKAROUND PROFILE

| Workaround name (specific: tool / file type / procedure — not "a manual process") | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|-----------------------------------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                                                   |                    |                                   |                                          |

"Teams export data" fails on all columns. Name the tool, name the role, give
the unit cost.

---

## SECTION 3 — SWITCHING COST ANALYSIS

> Every estimate must carry a number and a unit. "Significant" without a number
> fails C-02.

| Cost category | Estimate (e.g., 3 days) | Role bearing the cost | Confidence level |
|---------------|------------------------|----------------------|------------------|
| Migration effort |                     |                      |                  |
| Training overhead (e.g., 4 hours/person) |  |               |                  |
| Process disruption (e.g., 1 sprint delay) | |               |                  |
| In-flight work at risk (e.g., $8,000) |    |               |                  |

---

## SECTION 4 — INERTIA THREAT ASSESSMENT

| Threat score (HIGH / MEDIUM / LOW) | Deviation justification — quantified, required if not HIGH | Primary cost driver from Section 3 |
|------------------------------------|-------------------------------------------------------------|-------------------------------------|
|                                    |                                                             |                                     |

Default is HIGH. Deviations require a specific number, threshold, or measurable
state — not a qualitative judgment.

---

## SECTION 5 — DEFEAT CONDITIONS

> **REFERENTIAL INTEGRITY RULE**: Every FM-[N] cited in this table must have a
> corresponding assigned row in the FM Inventory (Section 1). Do not introduce
> FM references here that were not assigned above. Verify Section 1 before filling.

| DC-[N] | FM-[N] reference | Defeat condition — specific and falsifiable | Measurable threshold | Team type / segment |
|--------|-----------------|--------------------------------------------|-----------------------|---------------------|
| DC-01  |                 |                                            |                       |                     |
| DC-02  |                 |                                            |                       |                     |

"When they see value" fails. "When FM-01 causes data loss on files > 10MB for
the data-ops team" passes. Minimum 2 rows, each with an FM reference.

---

## COMPLETENESS CHECK

| Criterion | Check (Y / N) |
|-----------|---------------|
| C-01 — Workaround named with role and unit cost |  |
| C-02 — Two or more switching cost categories with units |  |
| C-03 — Inertia threat score declared (HIGH default) |  |
| C-04 — Two or more falsifiable defeat conditions with FM references |  |
| C-05 — Two or more specific failure modes with named actors and triggers |  |
```

---

## V-02

**Axis**: Lifecycle emphasis — the FAIL-FIRST DECLARATION is an extended structural section that names Q3 and Q4 explicitly as lifecycle bridge stages with criterion-chain references, before any FM content is authored. The lifecycle ordering and bridge naming both derive from this declaration. Each analysis stage has an embedded criterion question to enforce authoring completeness.

**Hypothesis**: Announcing Q3 and Q4 as named artifacts in the lifecycle preamble — with the chain references "(closes C-05 → R-02)" and "(closes C-05 → C-04)" — satisfies A-12 because the named artifacts appear at the structural entry point of the template, not as a post-hoc section. Combined with embedded criterion questions, A-11 and A-17 also pass.

---

```
You are running /scout:inertia for the feature: {TOPIC}.

The central question is: **Why does inertia lose?** Every team that keeps their
current workaround is a lost adoption. This analysis maps where the workaround
cracks, what it costs to abandon it, and the specific conditions under which
teams switch. If you cannot answer the central question with evidence, stop.

Produce the output below. Fill every section. If a section cannot be answered
with specifics, mark it BLOCKED and state what is missing.

---

# INERTIA ANALYSIS — {TOPIC}

---

## FAIL-FIRST DECLARATION

This analysis follows a six-stage lifecycle. The stages are fixed. Do not reorder.

**Stage 1 — FM Inventory** (C-05): Enumerate where the current workaround breaks.
This is the structural foundation. Nothing else is authored until Stage 1 has at
least two rows.

**Stage 2 — Bridge verification**:

- **Q3 — FM→ACTOR BRIDGE** (closes C-05 → R-02): Each failure mode names a
  specific role. Q3 is verified when every FM row carries a named role. These
  actors appear in Section 3 (switching cost attribution) and Section 5 (defeat
  condition team scoping). Unverified Q3 leaves R-02 structurally open.

- **Q4 — FM→TRIGGER BRIDGE** (closes C-05 → C-04): Each failure mode names a
  specific, falsifiable trigger. Q4 is verified when every FM row carries a
  falsifiable trigger. These triggers are the raw material for defeat conditions
  in Stage 5. An unverified Q4 means defeat conditions cannot be traced back
  to evidence.

**Stage 3 — Workaround profile** (C-01): Name the workaround, the role, and the
ongoing cost with a unit.

**Stage 4 — Switching cost** (C-02): Quantify what abandonment costs with numbers
and units, cited to the roles bearing them.

**Stage 5 — Threat assessment and defeat conditions** (C-03 + C-04): Aggregate
into a threat score. Derive falsifiable conditions from Stage 2 triggers.

*Execute in lifecycle order. Q3 and Q4 must both be verified before Stage 3.*

---

## STAGE 1 — FAILURE MODE INVENTORY

> **C-05 question**: For {TOPIC}, where specifically does the current workaround
> fail, produce errors, cause rework, or hit a scale ceiling? For each failure:
> what goes wrong exactly, who experiences it, and what triggers it?
>
> **PRIMARY KEY CONSTRAINT**: No FM-[N] identifier may appear in any later section
> unless it has an assigned row here. Assign identifiers in this table first.

| FM-[N] | What specifically goes wrong | Role experiencing it | Trigger — specific condition | Frequency |
|--------|------------------------------|----------------------|------------------------------|-----------|
| FM-01  |                              |                      |                              |           |
| FM-02  |                              |                      |                              |           |

Minimum 2 rows. Generic entries ("it is slow") fail C-05 — name the error,
truncation, or data loss event.

---

## STAGE 2 — BRIDGE VERIFICATION

**Q3 — FM→ACTOR BRIDGE** (closes C-05 → R-02):

Does every FM row above name a specific role — not "the team", not "users"?

Q3 STATUS: [ ] All FM rows carry named roles — proceed to Stage 3
           [ ] Rows needing revision: FM-___. Revise Section 1 before continuing.

**Q4 — FM→TRIGGER BRIDGE** (closes C-05 → C-04):

Does every FM row above carry a falsifiable trigger with a specific threshold
or named event?

Q4 STATUS: [ ] All FM rows carry falsifiable triggers — proceed to Stage 3
           [ ] Rows needing revision: FM-___. Revise Section 1 before continuing.

---

## STAGE 3 — WORKAROUND PROFILE

> **C-01 question**: What is the exact name of the workaround — the specific tool,
> file type, or procedure name? Not "a manual process." Who performs it? What is
> the ongoing cost per week or sprint, with a unit?

| Workaround name (specific) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Time in use |
|---------------------------|--------------------|-----------------------------------|-------------|
|                           |                    |                                   |             |

---

## STAGE 4 — SWITCHING COST ANALYSIS

> **C-02 question**: If this team adopted {TOPIC} today, what would migration cost?
> Who bears each cost? What in-flight work is at risk? Every estimate must carry
> a number and a unit — "significant" fails.

| Cost category | Estimate (e.g., 5 days) | Role bearing the cost | Basis |
|---------------|------------------------|----------------------|-------|
| Migration effort |                     |                      |       |
| Training overhead |                    |                      |       |
| Process disruption |                   |                      |       |
| In-flight work at risk |               |                      |       |

---

## STAGE 5A — INERTIA THREAT ASSESSMENT

> **C-03 question**: Given the total switching cost above, what is the inertia
> threat level for {TOPIC}? Default is HIGH. If deviating from HIGH, state a
> specific quantified condition — a percentage, threshold, or measurable state.

| Threat score (HIGH / MEDIUM / LOW) | Deviation justification (quantified — required if not HIGH) |
|------------------------------------|-------------------------------------------------------------|
|                                    |                                                             |

---

## STAGE 5B — DEFEAT CONDITIONS

> **REFERENTIAL INTEGRITY RULE** (citation point): Every FM-[N] cited here must
> have a corresponding assigned row in the FM Inventory (Stage 1). Verify before
> filling.
>
> **C-04 question**: Under what specific, measurable conditions does a team abandon
> the workaround and adopt {TOPIC}? Cite the FM-[N] driving the pressure. Is the
> condition falsifiable?

| DC-[N] | FM-[N] cited | Defeat condition — specific and falsifiable | Measurable threshold | Team type scoped |
|--------|-------------|--------------------------------------------|-----------------------|------------------|
| DC-01  |             |                                            |                       |                  |
| DC-02  |             |                                            |                       |                  |

---

## COMPLETENESS CHECK

| Criterion | Check (Y / N) |
|-----------|---------------|
| C-01 — Workaround named with role and unit cost |  |
| C-02 — Two or more cost categories with units |  |
| C-03 — Inertia threat score declared (HIGH default) |  |
| C-04 — Two or more falsifiable defeat conditions with FM references |  |
| C-05 — Two or more specific failure modes with named actors and triggers |  |
```

---

## V-03

**Axis**: Phrasing register — every structural element is a direct imperative command co-located with its criterion label. Q3 and Q4 appear as labeled BRIDGE COMMANDs with explicit criterion-chain references embedded within the FM section itself, not in a separate section. The register enforces authoring completeness through mandatory-feeling commands rather than structural constraints.

**Hypothesis**: Imperative criterion-labeled commands ("[C-05 COMMAND]: NAME every specific failure mode") satisfy A-11 and A-17 without requiring tabular-only enforcement. Q3 and Q4 as "[BRIDGE Q3 COMMAND — closes C-05 → R-02]" labels with chain text satisfy A-12 via in-context naming during authoring, before the author reaches the DC table.

---

```
You are running /scout:inertia for the feature: {TOPIC}.

STOP. Read before writing:

The central question is: **Why does inertia lose?**

This is not rhetorical. Every section below demands a specific answer with
evidence. If you cannot fill a section with specifics, mark it BLOCKED.
Do not produce vague output. Vague output cannot support a feature decision.

Produce the output below. Follow every labeled command exactly.

---

# INERTIA ANALYSIS — {TOPIC}

---

**[FAIL-FIRST DECLARATION]**: Start with failure modes. The workaround's failure
is the only evidence that inertia can be beaten. If you cannot name where it
breaks, you cannot identify conditions under which teams switch. ENUMERATE
failures first.

---

## 1. FAILURE MODE INVENTORY

**[C-05 COMMAND]**: NAME every specific failure mode for the current workaround
used instead of {TOPIC}. For each failure:
- NAME what goes wrong — the specific error, truncation, data loss, or scale
  limit. Not "is slow." Name the event.
- NAME the role experiencing it — not "the team", not "users". A named role.
- NAME the trigger — the specific condition that causes the failure.
- ASSIGN an FM-[N] identifier.

**[A-16 PRIMARY KEY RULE]**: ASSIGN all FM-[N] identifiers here. NO FM-[N]
reference may appear in any later section without a corresponding row in this
table.

| FM-[N] | What goes wrong (specific event) | Who experiences it (named role) | What triggers it (specific condition) | How often |
|--------|----------------------------------|---------------------------------|--------------------------------------|-----------|
| FM-01  |                                  |                                 |                                      |           |
| FM-02  |                                  |                                 |                                      |           |

MINIMUM 2 rows. REJECT any entry where the failure description is generic.

---

**[BRIDGE Q3 COMMAND — closes C-05 → R-02]**: VERIFY the "Who experiences it"
column above. CONFIRM every FM-[N] row names a specific role. CORRECT any row
where the actor is "users", "the team", or another non-role label before
proceeding. Q3 bridges failure mode identity (C-05) to role-level precision
(R-02). An unroled failure mode cannot support role-scoped defeat conditions.

Q3 RESULT: [ ] All rows carry named roles — PROCEED
           [ ] Rows without named roles: FM-___. REVISE before continuing.

**[BRIDGE Q4 COMMAND — closes C-05 → C-04]**: VERIFY the "What triggers it"
column above. CONFIRM every FM-[N] row names a falsifiable trigger — a specific
event or threshold, not "sometimes" or "when it gets busy". CORRECT any row
without a falsifiable trigger before proceeding. Q4 bridges failure mode triggers
(C-05) to defeat condition derivation (C-04). Triggers without thresholds cannot
generate falsifiable defeat conditions.

Q4 RESULT: [ ] All rows carry falsifiable triggers — PROCEED
           [ ] Rows without falsifiable triggers: FM-___. REVISE before continuing.

---

## 2. WORKAROUND PROFILE

**[C-01 COMMAND]**: NAME the specific workaround. Not "a manual process." The
specific tool, file type, or named procedure. NAME the role performing it.
QUANTIFY the ongoing cost with a number and unit.

| Workaround name (specific tool / file / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in use |
|---------------------------------------------------|--------------------|-----------------------------------|-----------------|
|                                                   |                    |                                   |                 |

REJECT "teams export data manually". NAME the tool. NAME the role. GIVE the unit.

---

## 3. SWITCHING COST ANALYSIS

**[C-02 COMMAND]**: IDENTIFY at least two cost categories. QUANTIFY each with a
number and unit. NAME the role bearing each cost. IDENTIFY any in-flight work
at risk.

> UNIT RULE: EVERY estimate carries a number and unit. "Significant" is REJECTED.

| Cost category | Estimate (e.g., 4 days) | Role bearing it | Notes |
|---------------|------------------------|-----------------|-------|
| Migration effort |                     |                 |       |
| Training overhead |                    |                 |       |
| Process disruption |                   |                 |       |
| In-flight work at risk |               |                 |       |

---

## 4. INERTIA THREAT ASSESSMENT

**[C-03 COMMAND]**: DECLARE the inertia threat score. DEFAULT IS HIGH. IF
deviating from HIGH, STATE a specific quantified condition — a number, percentage,
or measurable threshold. A qualitative statement does not justify deviation from
the default.

| Threat score (HIGH / MEDIUM / LOW) | Deviation justification (quantified — required if not HIGH) |
|------------------------------------|-------------------------------------------------------------|
|                                    |                                                             |

---

## 5. DEFEAT CONDITIONS

**[A-19 CITATION INTEGRITY RULE]**: EVERY FM-[N] cited in this table MUST have
an assigned row in the FM Inventory above. DO NOT introduce FM references not
assigned in Section 1.

**[C-04 COMMAND]**: DERIVE at least two specific, falsifiable defeat conditions
from the Q4 triggers above. CITE the FM-[N] driving each. GIVE a measurable
threshold. SCOPE each condition to a named team type.

| DC-[N] | FM-[N] cited | Defeat condition (falsifiable) | Measurable threshold | Team type |
|--------|-------------|-------------------------------|----------------------|-----------|
| DC-01  |             |                               |                      |           |
| DC-02  |             |                               |                      |           |

"When they see value" FAILS. "When FM-01 causes data loss on files > 10MB for
the data-ops team" PASSES.

---

## COMPLETENESS CHECK

| Criterion | Check (Y / N) |
|-----------|---------------|
| C-01 — Workaround named with role and unit cost |  |
| C-02 — Two or more cost categories with units and roles |  |
| C-03 — Inertia threat score declared (HIGH default) |  |
| C-04 — Two or more falsifiable defeat conditions with FM references |  |
| C-05 — Two or more specific failure modes with named actors and triggers |  |
```

---

## V-04

**Axis**: Output format + lifecycle emphasis — Q3 and Q4 are named with criterion-chain references in the FAIL-FIRST DECLARATION preamble (establishing them as lifecycle artifacts before FM content begins) AND echoed as structured verification tables after the FM Inventory (establishing them as output artifacts the reader can check). Full tabular schema + embedded criterion questions + bidirectional referential integrity (A-19) + inline examples in unit-bearing column labels (A-20).

**Hypothesis**: Naming Q3/Q4 at two structural positions — the lifecycle declaration AND the verification tables — makes the named-artifact requirement of A-12 doubly observable. The lifecycle naming establishes intent; the verification tables establish execution. Combined with embedded criterion questions (A-11/A-17), the full scaffold (A-13/A-14/A-16/A-19), and inline examples (A-20), this is the highest-probability path to all advanced criteria simultaneously.

---

```
You are running /scout:inertia for the feature: {TOPIC}.

Produce the complete inertia analysis below. Fill every table cell. A blank cell
is a visible structural failure. Follow the lifecycle order exactly.

---

# INERTIA ANALYSIS — {TOPIC}

---

## FAIL-FIRST DECLARATION

This analysis follows a structured lifecycle with two required bridge artifacts.
Both artifacts are named here and verified after Section 1.

**Q3 — FM→ACTOR BRIDGE** (closes C-05 → R-02): Verifies that every failure mode
names a specific role as the actor experiencing it. Required before switching
costs can be attributed to roles and before defeat conditions can be scoped to
team types.

**Q4 — FM→TRIGGER BRIDGE** (closes C-05 → C-04): Verifies that every failure
mode names a specific, falsifiable trigger condition. These triggers are the
evidentiary foundation for defeat conditions. A defeat condition without a
verified FM trigger is unsupported.

*Populate Section 1 fully. Verify Q3 and Q4. Then proceed in order.*

---

## SECTION 1 — FAILURE MODE INVENTORY

> **C-05 question**: Where specifically does the current workaround for {TOPIC}
> fail, produce errors, cause rework, or hit a scale ceiling? For each failure:
> what goes wrong, who experiences it, what triggers it?
>
> **PRIMARY KEY CONSTRAINT**: No FM-[N] identifier may appear in any downstream
> section unless it has an assigned row in this table. All FM-[N] identifiers
> are assigned here.

| FM-[N] | Failure description (specific error / data loss / scale event) | Actor / role experiencing it | Trigger — specific, falsifiable condition | Frequency (e.g., 2×/sprint) |
|--------|----------------------------------------------------------------|------------------------------|------------------------------------------|-----------------------------|
| FM-01  |                                                                |                              |                                          |                             |
| FM-02  |                                                                |                              |                                          |                             |

Minimum 2 rows. "Manual is slow" fails — name the specific error or failure event.

---

## BRIDGE ARTIFACT VERIFICATION

**Q3 — FM→ACTOR BRIDGE** (closes C-05 → R-02):

Review the Actor column in Section 1. Every FM-[N] must name a specific role —
not "the team", not "users". Confirm or revise.

| FM-[N] | Actor — named role present? (Y / N) | Named role or needed revision |
|--------|-------------------------------------|-------------------------------|
| FM-01  |                                     |                               |
| FM-02  |                                     |                               |

All rows must show Y before proceeding.

**Q4 — FM→TRIGGER BRIDGE** (closes C-05 → C-04):

Review the Trigger column in Section 1. Every FM-[N] must carry a falsifiable
trigger — a specific event or threshold, not "sometimes". Confirm or revise.

| FM-[N] | Trigger — falsifiable condition present? (Y / N) | Trigger text or needed revision |
|--------|--------------------------------------------------|----------------------------------|
| FM-01  |                                                  |                                  |
| FM-02  |                                                  |                                  |

All rows must show Y before proceeding.

---

## SECTION 2 — WORKAROUND PROFILE

> **C-01 question**: What is the exact name of the workaround — the specific tool,
> file type, or procedure name? Who performs it? What is the ongoing cost with
> a unit?

| Workaround name (specific: tool / file / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use |
|----------------------------------------------------|--------------------|-----------------------------------|------------------------|
|                                                    |                    |                                   |                        |

---

## SECTION 3 — SWITCHING COST ANALYSIS

> **C-02 question**: What would it cost this team to switch from the workaround
> to {TOPIC} today? Give at least two categories with numbers and units. Who bears
> each cost?
>
> Every estimate must carry a number and unit. "Significant" fails C-02.

| Cost category | Estimate (e.g., 3 days) | Role bearing the cost (e.g., data-ops team) | Confidence |
|---------------|------------------------|---------------------------------------------|------------|
| Migration effort |                     |                                             |            |
| Training overhead (e.g., 4 hours/person) |  |                                  |            |
| Process disruption (e.g., 1 sprint) |      |                                             |            |
| In-flight work at risk (e.g., $8,000) |    |                                             |            |

---

## SECTION 4 — INERTIA THREAT ASSESSMENT

> **C-03 question**: Given the total switching cost above, what is the inertia
> threat level for {TOPIC}? Default is HIGH. If not HIGH, state a specific
> quantified condition — not a qualitative judgment.

| Threat score (HIGH / MEDIUM / LOW) | Deviation justification — quantified threshold (required if not HIGH) |
|------------------------------------|-----------------------------------------------------------------------|
|                                    |                                                                       |

---

## SECTION 5 — DEFEAT CONDITIONS

> **REFERENTIAL INTEGRITY RULE** (citation point): Every FM-[N] cited in this
> table must have a corresponding assigned row in the FM Inventory (Section 1).
> Do not reference FM identifiers not assigned above.
>
> **C-04 question**: Under what specific, measurable conditions does a team
> abandon the workaround and adopt {TOPIC}? Cite the FM-[N] driving the pressure.
> The condition must be falsifiable.

| DC-[N] | FM-[N] reference | Defeat condition — specific and falsifiable | Threshold (e.g., >10MB, >3 failures/week) | Team type / segment |
|--------|-----------------|--------------------------------------------|--------------------------------------------|---------------------|
| DC-01  |                 |                                            |                                            |                     |
| DC-02  |                 |                                            |                                            |                     |

---

## COMPLETENESS CHECK

| Criterion | Check (Y / N) |
|-----------|---------------|
| C-01 — Workaround named with role and unit cost |  |
| C-02 — Two or more cost categories with units and roles |  |
| C-03 — Inertia threat score declared (HIGH default) |  |
| C-04 — Two or more falsifiable defeat conditions with FM references |  |
| C-05 — Two or more specific failure modes with named actors and triggers |  |
```

---

## V-05

**Axis**: All three axes combined — output format (full tabular schema with inline examples) + lifecycle emphasis (FAIL-FIRST DECLARATION names Q3/Q4 as lifecycle artifacts) + phrasing register (imperative criterion-labeled commands throughout). Every structural element is enforced three ways: by table structure, by lifecycle position, and by direct command. Targets all 12 advanced criteria simultaneously.

**Hypothesis**: Stacking all three axes produces a coherent template because each axis enforces different failure modes — tables catch blank cells, the lifecycle declaration catches sequencing failures, and imperative commands catch authoring-time omissions. Q3/Q4 appear in the lifecycle declaration AND as BRIDGE COMMANDs in the authoring flow. A-19 and A-20 are both present. If this variation fails A-12, the named-artifact criterion requires a fundamentally different structural element not yet identified.

---

```
You are running /scout:inertia for the feature: {TOPIC}.

PRODUCE the complete inertia analysis below. FILL every table cell.
FOLLOW every labeled command. A blank cell is a visible structural failure.
Do not hedge or generalize. Specific evidence only.

---

# INERTIA ANALYSIS — {TOPIC}

---

## [FAIL-FIRST DECLARATION]

Two bridge artifacts govern this analysis. They are named below and must be
verified before the workaround profile is authored.

**Q3 — FM→ACTOR BRIDGE** (closes C-05 → R-02): Confirms named roles per failure
mode. Required before defeat conditions can be scoped to team types.

**Q4 — FM→TRIGGER BRIDGE** (closes C-05 → C-04): Confirms falsifiable triggers
per failure mode. These triggers become defeat condition evidence.

*ENUMERATE failures first. VERIFY Q3 and Q4. THEN proceed to Section 2.*

---

## SECTION 1 — FAILURE MODE INVENTORY

**[C-05 COMMAND]**: NAME every specific failure mode. For each: NAME what goes
wrong (the error event, not "is slow"). NAME the role experiencing it (not "users").
NAME the falsifiable trigger. ASSIGN an FM-[N] identifier.

> **[A-16 PRIMARY KEY RULE]**: ASSIGN all FM-[N] identifiers here. NO FM-[N]
> reference may appear in any later section without a row in this table.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2×/sprint) |
|--------|-------------------------------------------------------------------------|-----------------------------------|----------------------------|----------------------------|
| FM-01  |                                                                         |                                   |                            |                            |
| FM-02  |                                                                         |                                   |                            |                            |

MINIMUM 2 rows. REJECT generic descriptions — name the specific error or event.

---

**[BRIDGE Q3 COMMAND — closes C-05 → R-02]**: REVIEW the Actor column above.
VERIFY every FM-[N] names a specific role — not "users", not "the team".
MARK each row Y or N. REVISE N rows before proceeding.

| FM-[N] | Named role present? (Y / N) | Revision needed |
|--------|-----------------------------|-----------------|
| FM-01  |                             |                 |
| FM-02  |                             |                 |

**[BRIDGE Q4 COMMAND — closes C-05 → C-04]**: REVIEW the Trigger column above.
VERIFY every trigger is a specific, falsifiable condition — a threshold or named
event. MARK each row Y or N. REVISE N rows before proceeding.

| FM-[N] | Falsifiable trigger present? (Y / N) | Revision needed |
|--------|--------------------------------------|-----------------|
| FM-01  |                                      |                 |
| FM-02  |                                      |                 |

Both tables must show all Y before Section 2.

---

## SECTION 2 — WORKAROUND PROFILE

**[C-01 COMMAND]**: NAME the specific workaround — tool name, file type, or
procedure name. NAME the role performing it. QUANTIFY the ongoing cost with
a number and unit.

| Workaround name (specific tool / file / procedure — not "a manual process") | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in use (e.g., 18 months) |
|-----------------------------------------------------------------------------|--------------------|-----------------------------------|-----------------------------------|
|                                                                             |                    |                                   |                                   |

REJECT "teams export data manually". NAME the tool. NAME the role. GIVE the unit.

---

## SECTION 3 — SWITCHING COST ANALYSIS

**[C-02 COMMAND]**: IDENTIFY at least two cost categories. QUANTIFY each with a
number and unit. NAME the role bearing each cost.

> **[UNIT RULE]**: EVERY estimate carries a number and unit.
> "Significant" without a unit is REJECTED.

| Cost category | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) | Confidence level |
|---------------|------------------------|--------------------------------------|-----------------|
| Migration effort |                     |                                      |                 |
| Training overhead (e.g., 4 hours/person) |  |                           |                 |
| Process disruption (e.g., 1 sprint delay) | |                           |                 |
| In-flight work at risk (e.g., $8,000) |    |                           |                 |

---

## SECTION 4 — INERTIA THREAT ASSESSMENT

**[C-03 COMMAND]**: DECLARE the inertia threat score. DEFAULT IS HIGH. IF
deviating from HIGH, STATE a specific quantified condition — a number,
percentage, or measurable threshold.

| Threat score (HIGH / MEDIUM / LOW) | Deviation justification — quantified (required if not HIGH) |
|------------------------------------|-------------------------------------------------------------|
|                                    |                                                             |

---

## SECTION 5 — DEFEAT CONDITIONS

> **[A-19 CITATION INTEGRITY RULE]**: EVERY FM-[N] cited in this table MUST
> have an assigned row in the FM Inventory (Section 1). DO NOT introduce FM
> references not assigned above. VERIFY before filling.

**[C-04 COMMAND]**: DERIVE at least two specific, falsifiable defeat conditions
from Q4 triggers. CITE the FM-[N] driving each. GIVE a measurable threshold.
SCOPE each to a named team type.

| DC-[N] | FM-[N] cited | Defeat condition — specific and falsifiable | Threshold (e.g., >10MB) | Team type / segment |
|--------|-------------|--------------------------------------------|--------------------------|--------------------|
| DC-01  |             |                                            |                          |                    |
| DC-02  |             |                                            |                          |                    |

"When they see value" FAILS. "When FM-01 causes silent data loss for the
data-ops team on files > 10MB" PASSES.

---

## COMPLETENESS CHECK

| Criterion | Check (Y / N) |
|-----------|---------------|
| C-01 — Workaround named with role and unit cost |  |
| C-02 — Two or more cost categories with units and roles |  |
| C-03 — Inertia threat score declared (HIGH default) |  |
| C-04 — Two or more falsifiable defeat conditions with FM references |  |
| C-05 — Two or more specific failure modes with named actors and triggers |  |
```

---

## Predicted Criteria Coverage Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| A-10 Fail-first declaration | PASS | PASS | PASS | PASS | PASS |
| A-11 Question per criterion (3+) | FAIL | PASS | PASS | PASS | PASS |
| **A-12 BRIDGE dual-closure** | **PASS?** | **PASS?** | **PASS?** | **PASS?** | **PASS?** |
| A-13 Tabular column schema | PASS | PASS | PASS | PASS | PASS |
| A-14 FM Inventory dedicated table | PASS | PASS | PASS | PASS | PASS |
| A-15 Trailing completeness checklist | PASS | PASS | PASS | PASS | PASS |
| A-16 Primary key constraint declared | PASS | PASS | PASS | PASS | PASS |
| A-17 Question coverage all 5 | FAIL | PASS | PASS | PASS | PASS |
| A-18 Binary checklist format + full coverage | PASS | PASS | PASS | PASS | PASS |
| A-19 Bidirectional referential integrity | PASS | PASS | FAIL | PASS | PASS |
| A-20 Inline example in unit-bearing labels | PASS | FAIL | FAIL | PASS | PASS |
| **Predicted score** | **~135/155** | **~145/155** | **~130/155** | **~150/155** | **~155/155** |

**R9 primary discriminator**: A-12. All five variations name Q3 and Q4 in the template body with explicit criterion-chain references "(closes C-05 → R-02)" and "(closes C-05 → C-04)". Each varies the structural position and phrasing register of that naming. If A-12 passes anywhere, the position/phrasing combination that satisfied it is the R10 target for isolation.

**A-12 structural positions across variations**:
- V-01: Q3/Q4 as named items in a dedicated BRIDGE ARTIFACTS section after FM Inventory (post-inventory verification)
- V-02: Q3/Q4 named in the FAIL-FIRST DECLARATION preamble before FM content (pre-announced lifecycle stages), echoed as status markers after FM
- V-03: Q3/Q4 as `[BRIDGE Qn COMMAND]` labels embedded inline after the FM table, before Section 2
- V-04: Q3/Q4 named in FAIL-FIRST DECLARATION AND as dedicated verification tables after FM Inventory (dual naming)
- V-05: Q3/Q4 named in FAIL-FIRST DECLARATION AND as `[BRIDGE Qn COMMAND]` labels AND as verification tables (triple naming)
