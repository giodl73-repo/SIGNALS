Written to `simulations/quest/variations/scout-inertia-variations-R10-2026-03-17.md`.

---

**R10 Variations Summary**

| Variation | Axis | Key structural delta targeting C-30/C-31 |
|-----------|------|------------------------------------------|
| V-01 | Output format | FAIL-FIRST DECLARATION → manifest TABLE with "Governed sections" column; verbatim directives stay in section bodies. C-30 target; C-31 miss. |
| V-02 | Lifecycle emphasis | SCAFFOLD MANIFEST table: criterion IDs + governed sections + verbatim directives all in one pre-document block. C-30 + C-31 primary target. |
| V-03 | Phrasing register | Prose manifest with "CONSTRAINT-[N] [criterion] governs Section [N]:" labeled prefixes + verbatim conditions in prose body. C-30 prose test; C-31 format-agnostic test. |
| V-04 | Output format + lifecycle | SCAFFOLD MANIFEST (C-30 + C-31) + [COMMAND] register + remediation-column bridge gate. |
| V-05 | All axes | SCAFFOLD MANIFEST + full [COMMAND] register + all-column inline examples + lifecycle staging. Maximum 23-criterion convergence. |

**The primary discriminator for C-31 across this round:** V-01 deliberately misses it (verbatim directives not in manifest). V-02/V-04/V-05 target it via tabular manifest. V-03 tests whether prose-form co-location is sufficient. The scoring will resolve whether C-31's "verbatim-alignment directives co-located with canonical strings" requires table structure or accepts prose.
+ C-31) paired with lifecycle stage declarations and imperative [COMMAND] register. Each section body references manifest entries by ID (M-XX). Remediation-column bridge gate from R10 V-04 pattern. |
| V-05 | All three axes | C-30 + C-31 + all 23 criteria | Maximum convergence: SCAFFOLD MANIFEST (C-30 + C-31) + full [COMMAND] imperative register + all-column inline examples (extending A-20 to non-unit fields) + lifecycle declaration + A-22 bridge gate with remediation column + A-21 dual-type DC threshold + criterion-code labeled rules. |

---

## V-01

**Axis**: Output format — FAIL-FIRST DECLARATION replaced with a scope-annotated constraint manifest TABLE. Each row carries an explicit "Governed sections" column naming the analysis sections where that constraint applies. Everything else from R10 V-05 is retained (imperative [COMMAND] labels, [A-16]/[A-19] criterion-code labeled rules, A-21 DC threshold dual-type example, A-22 bridge completion gate, all-column inline examples).

**Hypothesis**: A manifest TABLE with a "Governed sections" column satisfies C-30's scope annotation requirement — each constraint entry explicitly declares its governed sites, making the constraint graph navigable without a document scan. C-31 fails: the verbatim directives remain in section bodies, not co-located in the manifest block itself.

---

```
You are running /scout:inertia for the feature: {TOPIC}.

PRODUCE the complete inertia analysis below. FILL every table cell.
FOLLOW every labeled command. A blank cell is a visible structural failure.
Do not hedge or generalize. Specific evidence only.

---

# INERTIA ANALYSIS — {TOPIC}

---

## [FAIL-FIRST DECLARATION] — STRUCTURAL CONSTRAINT MANIFEST

Every constraint governing this analysis is declared below with the sections
it governs. Read before authoring any section.

| Entry | Criterion | Governed sections | Constraint summary |
|-------|-----------|------------------|--------------------|
| M-01 | C-05 | Section 1 — FM Inventory | Failure modes: minimum 2 rows, each naming a specific error event, a named role, and a falsifiable trigger. Generic entries fail. |
| M-02 | A-16 | Sections 1 (source) and 5 (citation) | FM primary key: all FM-[N] identifiers assigned in Section 1 only. No FM-[N] may appear in Section 5 without an assigned row in Section 1. |
| M-03 | Q3 (closes C-05 → R-02) | Section 1 (Actor column), Section 3 (role attribution), Section 5 (team scoping) | Actor naming: every FM row names a specific role — not "users", not "the team". Unroled failure modes cannot scope defeat conditions. |
| M-04 | Q4 (closes C-05 → C-04) | Section 1 (Trigger column), Section 5 (threshold derivation) | Trigger falsifiability: every FM row carries a specific, falsifiable trigger. Non-falsifiable triggers cannot generate defeat conditions. |
| M-05 | C-01 | Section 2 — Workaround Profile | Workaround specificity: name the tool, file type, or procedure — not "a manual process". Name the role. Quantify cost with a number and unit. |
| M-06 | C-02 | Section 3 — Switching Cost | Unit requirement: every cost estimate carries a number and a unit. "Significant" without a number fails. Minimum 2 categories. |
| M-07 | C-03 | Section 4 — Threat Assessment | Threat score default: HIGH. Deviation requires a specific quantified condition — not a qualitative judgment. |
| M-08 | C-04 | Section 5 — Defeat Conditions | Defeat condition traceability: minimum 2 rows, each citing FM-[N] and stating a measurable threshold. Falsifiable conditions only. |
| M-09 | A-19 | Section 5 — Defeat Conditions | Citation integrity: every FM-[N] cited in Section 5 must have an assigned row in Section 1. No FM references not assigned above. |

Bridge artifacts Q3 [M-03] and Q4 [M-04] must both be verified after Section 1
before Section 2.

---

## SECTION 1 — FAILURE MODE INVENTORY

**[C-05 COMMAND]**: NAME every specific failure mode. For each: NAME what goes
wrong (the error event, not "is slow"). NAME the role experiencing it (not "users").
NAME the falsifiable trigger. ASSIGN an FM-[N] identifier.

> **[A-16 PRIMARY KEY RULE]**: ASSIGN all FM-[N] identifiers here. NO FM-[N]
> reference may appear in any later section without a corresponding row in this
> table.

> **C-05 question**: For {TOPIC}, where specifically does the current workaround
> fail, produce errors, cause rework, or hit a scale ceiling? What goes wrong,
> who experiences it, what triggers it?

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2×/sprint) |
|--------|-------------------------------------------------------------------------|-----------------------------------|----------------------------|----------------------------|
| FM-01  |                                                                         |                                   |                            |                            |
| FM-02  |                                                                         |                                   |                            |                            |

MINIMUM 2 rows [M-01]. REJECT generic descriptions — name the specific error or event.

---

## BRIDGE COMPLETION GATE

**[BRIDGE Q3 COMMAND — closes C-05 → R-02 — M-03]**: REVIEW the Actor / role
column above. VERIFY every FM-[N] names a specific role. MARK each row Y or N.
REVISE N rows before proceeding.

| FM-[N] | Named role present? (Y / N) | Revision needed (e.g., "users" → "data-ops team") |
|--------|-----------------------------|---------------------------------------------------|
| FM-01  |                             |                                                   |
| FM-02  |                             |                                                   |

**[BRIDGE Q4 COMMAND — closes C-05 → C-04 — M-04]**: REVIEW the Trigger column
above. VERIFY every trigger is a specific, falsifiable condition. MARK each row
Y or N. REVISE N rows before proceeding.

| FM-[N] | Falsifiable trigger present? (Y / N) | Revision needed (e.g., "sometimes" → "file > 10MB") |
|--------|--------------------------------------|-----------------------------------------------------|
| FM-01  |                                      |                                                     |
| FM-02  |                                      |                                                     |

**BRIDGE COMPLETION STATUS**

| Bridge artifact | Populated? (Y / N) |
|-----------------|-------------------|
| Q3 — FM→ACTOR BRIDGE (closes C-05 → R-02) [M-03] |  |
| Q4 — FM→TRIGGER BRIDGE (closes C-05 → C-04) [M-04] |  |

Both rows must show Y before Section 2.

---

## SECTION 2 — WORKAROUND PROFILE

**[C-01 COMMAND — M-05]**: NAME the specific workaround — tool name, file type,
or procedure name. NAME the role performing it. QUANTIFY the ongoing cost with
a number and unit.

> **C-01 question**: What is the exact name of the workaround — the specific
> tool, file type, or procedure name? Who performs it? What is the ongoing cost
> with a unit?

| Workaround name (specific tool / file / procedure — not "a manual process") | Role performing it (e.g., data-ops team) | Ongoing cost (e.g., 2 hours/week) | Duration in use (e.g., 18 months) |
|-----------------------------------------------------------------------------|------------------------------------------|-----------------------------------|-----------------------------------|
|                                                                             |                                          |                                   |                                   |

REJECT "teams export data manually" [M-05]. NAME the tool. NAME the role. GIVE the unit.

---

## SECTION 3 — SWITCHING COST ANALYSIS

**[C-02 COMMAND — M-06]**: IDENTIFY at least two cost categories. QUANTIFY each
with a number and unit. NAME the role bearing each cost.

> **[UNIT RULE — M-06]**: EVERY estimate carries a number and unit.
> "Significant" without a unit is REJECTED.

> **C-02 question**: If this team adopted {TOPIC} today, what would migration,
> training, and disruption cost? Who bears each cost? Every estimate must carry
> a number and a unit.

| Cost category | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) | Confidence level |
|---------------|------------------------|--------------------------------------|-----------------|
| Migration effort |                     |                                      |                 |
| Training overhead (e.g., 4 hours/person) |  |                           |                 |
| Process disruption (e.g., 1 sprint delay) | |                           |                 |
| In-flight work at risk (e.g., $8,000) |    |                           |                 |

---

## SECTION 4 — INERTIA THREAT ASSESSMENT

**[C-03 COMMAND — M-07]**: DECLARE the inertia threat score. DEFAULT IS HIGH.
IF deviating from HIGH, STATE a specific quantified condition — a number,
percentage, or measurable threshold.

> **C-03 question**: Given the total switching cost above, what is the inertia
> threat level for {TOPIC}? If deviating from HIGH, state a specific quantified
> condition.

| Threat score (HIGH / MEDIUM / LOW) | Deviation justification — quantified, required if not HIGH |
|------------------------------------|-------------------------------------------------------------|
|                                    |                                                             |

---

## SECTION 5 — DEFEAT CONDITIONS

> **[A-19 CITATION INTEGRITY RULE — M-09]**: EVERY FM-[N] cited in this table
> MUST have an assigned row in the FM Inventory (Section 1). DO NOT introduce
> FM references not assigned above. VERIFY before filling.

**[C-04 COMMAND — M-08]**: DERIVE at least two specific, falsifiable defeat
conditions from Q4 triggers. CITE the FM-[N] driving each. GIVE a measurable
threshold. SCOPE each to a named team type.

> **C-04 question**: Under what specific, measurable conditions does a team
> abandon the workaround and adopt {TOPIC}? Cite the FM-[N] driving the pressure.

| DC-[N] | FM-[N] cited | Defeat condition — specific and falsifiable | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type / segment |
|--------|-------------|--------------------------------------------|----------------------------------------------------|---------------------|
| DC-01  |             |                                            |                                                    |                     |
| DC-02  |             |                                            |                                                    |                     |

"When they see value" FAILS [M-08]. "When FM-01 causes silent data loss for the
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

## V-02

**Axis**: Lifecycle emphasis — the SCAFFOLD MANIFEST is the lifecycle declaration. Each manifest row carries a criterion-ID label, governed section(s), and the verbatim directive that applies at that site — all in one pre-document block. Section bodies contain streamlined stubs that quote the manifest entry and add a criterion question.

**Hypothesis**: A single pre-document block that (1) precedes Section 1, (2) uses criterion-ID labels on each entry, and (3) contains verbatim directives co-located with canonical acceptance/rejection strings satisfies C-31's triple convergence. C-30 also passes via the "Governed sections" column. A-11/A-17 preserved via criterion questions in section stubs; A-22 bridge gate and A-21 DC threshold retained.

---

```
You are running /scout:inertia for the feature: {TOPIC}.

The central question is: **Why does inertia lose?** Every section demands a
specific answer. If you cannot fill a section with specifics, mark it BLOCKED.
The SCAFFOLD MANIFEST governs every section. Read it first.

---

# INERTIA ANALYSIS — {TOPIC}

---

## SCAFFOLD MANIFEST

This block is placed before all governed sections. Every structural rule,
verbatim directive, and acceptance/rejection condition for every section is
declared here. Read before authoring any section. Do not reorder sections.

| Entry | Criterion | Governed sections | Verbatim directive — applies exactly at governed site |
|-------|-----------|------------------|------------------------------------------------------|
| M-01 | C-05 | Section 1 — FM Inventory | "MINIMUM 2 rows required. 'Manual is slow' fails — name the specific error, truncation, silent failure, or data loss event." |
| M-02 | A-16 | Sections 1 (source) and 5 (citation) | "PRIMARY KEY CONSTRAINT: No FM-[N] identifier may appear in any downstream section unless it has an assigned row in the FM Inventory. All FM-[N] identifiers are assigned in Section 1 only." |
| M-03 | Q3 (closes C-05 → R-02) | Section 1 (Actor column), Section 3 (role attribution), Section 5 (team scoping) | "Every FM row names a specific role — not 'users', not 'the team'. Unroled failure modes cannot support role-scoped defeat conditions in Section 5." |
| M-04 | Q4 (closes C-05 → C-04) | Section 1 (Trigger column), Section 5 (threshold derivation) | "Every FM row carries a falsifiable trigger — a specific threshold or named event. 'Sometimes' and 'when usage grows' are not triggers. Triggers without thresholds cannot generate falsifiable defeat conditions." |
| M-05 | C-01 | Section 2 — Workaround Profile | "'Teams export data manually' fails — name the tool, the role, and quantify the cost with a number and unit." |
| M-06 | C-02 | Section 3 — Switching Cost | "Every estimate carries a number and a unit. 'Significant' without a number fails C-02. Minimum 2 cost categories." |
| M-07 | C-03 | Section 4 — Threat Assessment | "Default is HIGH. Deviation requires a specific quantified condition — not a qualitative judgment." |
| M-08 | C-04 | Section 5 — Defeat Conditions | "'When they see value' fails. Each row cites FM-[N] and states a measurable threshold. Minimum 2 rows." |
| M-09 | A-19 | Section 5 — Defeat Conditions | "REFERENTIAL INTEGRITY: Every FM-[N] cited in Section 5 must have an assigned row in Section 1. Do not introduce FM references not assigned there." |

Lifecycle order: Section 1 → Bridge Gate → Section 2 → Section 3 → Section 4 →
Section 5. Do not reorder.

---

## SECTION 1 — FAILURE MODE INVENTORY

> **C-05 [M-01]**: "MINIMUM 2 rows required. 'Manual is slow' fails — name the
> specific error, truncation, silent failure, or data loss event."
>
> **A-16 [M-02]**: "PRIMARY KEY CONSTRAINT: No FM-[N] identifier may appear in
> any downstream section unless it has an assigned row here."
>
> **C-05 question**: For {TOPIC}, where specifically does the current workaround
> fail, produce errors, cause rework, or hit a scale ceiling? What goes wrong,
> who experiences it, what triggers it?

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2×/sprint) |
|--------|-------------------------------------------------------------------------|-----------------------------------|----------------------------|----------------------------|
| FM-01  |                                                                         |                                   |                            |                            |
| FM-02  |                                                                         |                                   |                            |                            |

---

## BRIDGE COMPLETION GATE

**Q3 VERIFICATION [M-03]**: Review the Actor column in Section 1. Every FM-[N]
must name a specific role as stated in M-03. Confirm or revise.

| FM-[N] | Named role present? (Y / N) | Revision needed |
|--------|-----------------------------|-----------------|
| FM-01  |                             |                 |
| FM-02  |                             |                 |

**Q4 VERIFICATION [M-04]**: Review the Trigger column in Section 1. Every FM-[N]
must carry a falsifiable trigger as stated in M-04. Confirm or revise.

| FM-[N] | Falsifiable trigger present? (Y / N) | Revision needed |
|--------|--------------------------------------|-----------------|
| FM-01  |                                      |                 |
| FM-02  |                                      |                 |

**BRIDGE COMPLETION STATUS**

| Bridge artifact | Populated? (Y / N) |
|-----------------|-------------------|
| Q3 — FM→ACTOR BRIDGE (closes C-05 → R-02) [M-03] |  |
| Q4 — FM→TRIGGER BRIDGE (closes C-05 → C-04) [M-04] |  |

Both rows must show Y before Section 2.

---

## SECTION 2 — WORKAROUND PROFILE

> **C-01 [M-05]**: "'Teams export data manually' fails — name the tool, the
> role, and quantify the cost with a number and unit."
>
> **C-01 question**: What is the exact name of the workaround — the specific
> tool, file type, or procedure name? Who performs it? What is the ongoing cost
> with a unit?

| Workaround name (specific tool / file / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in use (e.g., 18 months) |
|---------------------------------------------------|--------------------|-----------------------------------|-----------------------------------|
|                                                   |                    |                                   |                                   |

---

## SECTION 3 — SWITCHING COST ANALYSIS

> **C-02 [M-06]**: "Every estimate carries a number and a unit. 'Significant'
> without a number fails C-02. Minimum 2 cost categories."
>
> **C-02 question**: If this team adopted {TOPIC} today, what would migration,
> training, and disruption cost? Who bears each cost?

| Cost category | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) | Confidence level |
|---------------|------------------------|--------------------------------------|-----------------|
| Migration effort |                     |                                      |                 |
| Training overhead (e.g., 4 hours/person) |  |                           |                 |
| Process disruption (e.g., 1 sprint delay) | |                           |                 |
| In-flight work at risk (e.g., $8,000) |    |                           |                 |

---

## SECTION 4 — INERTIA THREAT ASSESSMENT

> **C-03 [M-07]**: "Default is HIGH. Deviation requires a specific quantified
> condition — not a qualitative judgment."
>
> **C-03 question**: Given the total switching cost above, what is the inertia
> threat level for {TOPIC}? If deviating from HIGH, state a specific quantified
> condition.

| Threat score (HIGH / MEDIUM / LOW) | Deviation justification — quantified (required if not HIGH) |
|------------------------------------|-------------------------------------------------------------|
|                                    |                                                             |

---

## SECTION 5 — DEFEAT CONDITIONS

> **A-19 [M-09]**: "REFERENTIAL INTEGRITY: Every FM-[N] cited in Section 5 must
> have an assigned row in Section 1. Do not introduce FM references not assigned
> there."
>
> **C-04 [M-08]**: "'When they see value' fails. Each row cites FM-[N] and states
> a measurable threshold. Minimum 2 rows."
>
> **C-04 question**: Under what specific, measurable conditions does a team abandon
> the workaround and adopt {TOPIC}? Cite the FM-[N] driving the pressure.

| DC-[N] | FM-[N] cited | Defeat condition — specific and falsifiable | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type / segment |
|--------|-------------|--------------------------------------------|----------------------------------------------------|---------------------|
| DC-01  |             |                                            |                                                    |                     |
| DC-02  |             |                                            |                                                    |                     |

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

## V-03

**Axis**: Phrasing register — formal prose narrative scope declarations. Each constraint is declared using "CONSTRAINT-[N] [criterion] governs Section [N]:" labeled prefix with verbatim acceptance and rejection conditions embedded in the prose body. Tests whether C-30's scope annotation requirement can be satisfied without a tabular governed-sections column, and whether C-31's verbatim co-location requirement is format-agnostic.

**Hypothesis**: Prose "CONSTRAINT-[N] [criterion] governs Section [N]" declarations satisfy C-30. C-31 is the key test: each CONSTRAINT entry contains the canonical verbatim strings co-located with the constraint criteria, and the manifest block is pre-document — but the criterion-ID label is a named prefix rather than a table column. C-31 may pass if the criterion-ID-label requirement accepts a labeled prefix; it may fail if a structured table ID column is required.

---

```
You are running /scout:inertia for the feature: {TOPIC}.

The central question of this analysis is: **Why does inertia lose?**

This analysis follows a governed structure. The constraints governing each
section are declared in the STRUCTURAL MANIFEST below. Produce the full
analysis with specific evidence throughout.

---

# INERTIA ANALYSIS — {TOPIC}

---

## STRUCTURAL MANIFEST

The following constraints are declared before Section 1. Each constraint
identifies the section(s) it governs, the criterion it satisfies, and the
verbatim acceptance and rejection conditions that apply at each governed site.

**CONSTRAINT-01 [C-05] governs Section 1 (FM Inventory):**
A failure mode entry passes when it names (a) a specific error event —
not "is slow" or "has limitations", (b) a named role as the actor, and
(c) a falsifiable trigger condition. The verbatim rejection string is:
"MINIMUM 2 rows required. 'Manual is slow' fails — name the specific error,
truncation, silent failure, or data loss event."

**CONSTRAINT-02 [A-16/A-19] governs Sections 1 (source) and 5 (citation):**
FM-[N] identifiers are assigned exclusively in Section 1. The verbatim
acceptance string at Section 1 is: "PRIMARY KEY CONSTRAINT: No FM-[N]
identifier may appear in any downstream section unless it has an assigned
row here." The verbatim requirement at Section 5 is: "REFERENTIAL INTEGRITY:
Every FM-[N] cited in Section 5 must have an assigned row in Section 1."

**CONSTRAINT-03 [Q3 — closes C-05 → R-02] governs Section 1 (Actor column),
Section 3 (role attribution), and Section 5 (team scoping):**
Every FM row names a specific role in the Actor column. The verbatim rejection
string is: "Every FM row names a specific role — not 'users', not 'the team'.
Unroled failure modes cannot scope defeat conditions to team types."

**CONSTRAINT-04 [Q4 — closes C-05 → C-04] governs Section 1 (Trigger column)
and Section 5 (threshold derivation):**
Every FM row carries a falsifiable trigger. The verbatim rejection string is:
"Every FM row carries a falsifiable trigger — a specific threshold or named
event. 'Sometimes' and 'when usage grows' are not triggers."

**CONSTRAINT-05 [C-01] governs Section 2 (Workaround Profile):**
The workaround name identifies a specific tool, file type, or procedure. The
verbatim rejection string is: "'Teams export data manually' fails — name the
tool, the role, and quantify the cost with a number and unit."

**CONSTRAINT-06 [C-02] governs Section 3 (Switching Cost):**
Every cost estimate carries a number and a unit. The verbatim rejection string
is: "Every estimate carries a number and a unit. 'Significant' without a number
fails C-02. Minimum 2 cost categories."

**CONSTRAINT-07 [C-03] governs Section 4 (Threat Assessment):**
The inertia threat score is HIGH by default. The verbatim acceptance condition
for deviation is: "Deviation requires a specific quantified condition — not a
qualitative judgment."

**CONSTRAINT-08 [C-04] governs Section 5 (Defeat Conditions):**
Each defeat condition cites FM-[N] and states a measurable threshold. The
verbatim rejection string is: "'When they see value' fails. Each row cites
FM-[N] and states a measurable threshold. Minimum 2 rows."

Bridge artifacts Q3 [CONSTRAINT-03] and Q4 [CONSTRAINT-04] are verified after
Section 1, before Section 2.

---

## SECTION 1 — FAILURE MODE INVENTORY

> **C-05 question** [CONSTRAINT-01 governs this section]: Where specifically
> does the current workaround for {TOPIC} fail, produce errors, cause rework,
> or hit a scale ceiling? What goes wrong, who experiences it, what triggers it?
>
> PRIMARY KEY CONSTRAINT [CONSTRAINT-02 governs this section]: No FM-[N]
> identifier may appear in any downstream section unless it has an assigned row
> in this table. Assign all identifiers here first.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2×/sprint) |
|--------|-------------------------------------------------------------------------|-----------------------------------|----------------------------|----------------------------|
| FM-01  |                                                                         |                                   |                            |                            |
| FM-02  |                                                                         |                                   |                            |                            |

Minimum 2 rows. See CONSTRAINT-01 for verbatim acceptance condition.

---

## BRIDGE COMPLETION GATE

**Q3 verification [CONSTRAINT-03]**: Does every FM row name a specific role?

| FM-[N] | Named role present? (Y / N) | Revision if N |
|--------|-----------------------------|---------------|
| FM-01  |                             |               |
| FM-02  |                             |               |

**Q4 verification [CONSTRAINT-04]**: Does every FM row carry a falsifiable trigger?

| FM-[N] | Falsifiable trigger present? (Y / N) | Revision if N |
|--------|--------------------------------------|---------------|
| FM-01  |                                      |               |
| FM-02  |                                      |               |

**BRIDGE COMPLETION STATUS**

| Bridge artifact | Populated? (Y / N) |
|-----------------|-------------------|
| Q3 — FM→ACTOR BRIDGE (closes C-05 → R-02) [CONSTRAINT-03] |  |
| Q4 — FM→TRIGGER BRIDGE (closes C-05 → C-04) [CONSTRAINT-04] |  |

Both rows must show Y before Section 2.

---

## SECTION 2 — WORKAROUND PROFILE

> **C-01 question** [CONSTRAINT-05 governs this section]: What is the exact
> name of the workaround — the specific tool, file type, or procedure name?
> Who performs it? What is the ongoing cost with a unit?

| Workaround name (specific tool / file / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in use (e.g., 18 months) |
|---------------------------------------------------|--------------------|-----------------------------------|-----------------------------------|
|                                                   |                    |                                   |                                   |

---

## SECTION 3 — SWITCHING COST ANALYSIS

> **C-02 question** [CONSTRAINT-06 governs this section]: If this team adopted
> {TOPIC} today, what would migration, training, and disruption cost? Who bears
> each cost? Every estimate must carry a number and a unit.

| Cost category | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) | Confidence level |
|---------------|------------------------|--------------------------------------|-----------------|
| Migration effort |                     |                                      |                 |
| Training overhead (e.g., 4 hours/person) |  |                           |                 |
| Process disruption (e.g., 1 sprint delay) | |                           |                 |
| In-flight work at risk (e.g., $8,000) |    |                           |                 |

---

## SECTION 4 — INERTIA THREAT ASSESSMENT

> **C-03 question** [CONSTRAINT-07 governs this section]: Given the total
> switching cost above, what is the inertia threat level for {TOPIC}? If
> deviating from HIGH, state a specific quantified condition — not a qualitative
> judgment.

| Threat score (HIGH / MEDIUM / LOW) | Deviation justification — quantified (required if not HIGH) |
|------------------------------------|-------------------------------------------------------------|
|                                    |                                                             |

---

## SECTION 5 — DEFEAT CONDITIONS

> **C-04 question** [CONSTRAINT-08 and CONSTRAINT-02 govern this section]:
> Under what specific, measurable conditions does a team abandon the workaround
> and adopt {TOPIC}? Cite the FM-[N] driving the pressure. The condition must
> be falsifiable. Referential integrity [CONSTRAINT-02] requires every FM-[N]
> cited here to have an assigned row in Section 1.

| DC-[N] | FM-[N] cited | Defeat condition — specific and falsifiable | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type / segment |
|--------|-------------|--------------------------------------------|----------------------------------------------------|---------------------|
| DC-01  |             |                                            |                                                    |                     |
| DC-02  |             |                                            |                                                    |                     |

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

**Axis**: Output format + lifecycle combined — SCAFFOLD MANIFEST table (targeting C-30 + C-31) paired with lifecycle stage declarations and imperative [COMMAND] register. Each section body [COMMAND] references its manifest entry by ID (M-XX). Bridge gate includes remediation column from R10 V-04 pattern.

**Hypothesis**: SCAFFOLD MANIFEST table satisfies C-31 (pre-document + criterion-ID labeled entries + verbatim directives in one block) and C-30 (governed-sections column). Imperative [COMMAND] labels with M-XX back-references preserve A-11/A-17. Remediation-column bridge gate satisfies A-22. All existing criteria pass unchanged.

---

```
You are running /scout:inertia for the feature: {TOPIC}.

PRODUCE the complete inertia analysis below. FILL every table cell.
FOLLOW the lifecycle order. FOLLOW every labeled command.
A blank cell is a visible structural failure.

---

# INERTIA ANALYSIS — {TOPIC}

---

## [FAIL-FIRST DECLARATION] — SCAFFOLD MANIFEST

Every structural constraint is declared below before all governed sections.
Each entry identifies its criterion, the sections it governs, and the verbatim
directive that applies at each governed site. Read before authoring any section.
Do not reorder sections.

| Entry | Criterion | Governed sections | Verbatim directive — applies verbatim at governed site |
|-------|-----------|------------------|------------------------------------------------------|
| M-01 | C-05 | Section 1 — FM Inventory | "MINIMUM 2 rows required. 'Manual is slow' fails — name the specific error, truncation, silent failure, or data loss event." |
| M-02 | A-16 | Sections 1 (source) and 5 (citation) | "PRIMARY KEY CONSTRAINT: No FM-[N] may appear in Section 5 without an assigned row in Section 1. Assign all FM-[N] identifiers in Section 1 only." |
| M-03 | Q3 (closes C-05 → R-02) | Section 1 (Actor column), Section 3 (role attribution), Section 5 (team scoping) | "Every FM row names a specific role — not 'users', not 'the team'. Unroled failure modes cannot scope defeat conditions." |
| M-04 | Q4 (closes C-05 → C-04) | Section 1 (Trigger column), Section 5 (threshold derivation) | "Every FM row carries a falsifiable trigger — a specific threshold or named event. 'Sometimes' is not a trigger." |
| M-05 | C-01 | Section 2 — Workaround Profile | "'Teams export data manually' fails — name the tool, the role, and quantify the cost with a number and unit." |
| M-06 | C-02 | Section 3 — Switching Cost | "Every estimate carries a number and a unit. 'Significant' without a number fails C-02. Minimum 2 cost categories." |
| M-07 | C-03 | Section 4 — Threat Assessment | "Default is HIGH. Deviation requires a specific quantified condition — not a qualitative judgment." |
| M-08 | C-04 | Section 5 — Defeat Conditions | "'When they see value' fails. Each row cites FM-[N] and states a measurable threshold. Minimum 2 rows." |
| M-09 | A-19 | Section 5 — Defeat Conditions | "REFERENTIAL INTEGRITY: Every FM-[N] cited in Section 5 must have an assigned row in Section 1. Do not introduce FM references not assigned there." |

Lifecycle: Section 1 → Bridge Gate → Section 2 → Section 3 → Section 4 →
Section 5. Q3 [M-03] and Q4 [M-04] must both be verified at the Bridge Gate
before Section 2.

---

## SECTION 1 — FAILURE MODE INVENTORY

**[C-05 COMMAND — M-01]**: NAME every specific failure mode. For each: NAME what
goes wrong (error event, not "is slow"). NAME the role (not "users"). NAME the
falsifiable trigger. ASSIGN an FM-[N] identifier.

> **[A-16 PRIMARY KEY RULE — M-02]**: ASSIGN all FM-[N] identifiers here. NO
> FM-[N] reference may appear in any later section without a row in this table.

> **C-05 question**: For {TOPIC}, where specifically does the current workaround
> fail, produce errors, cause rework, or hit a scale ceiling? What goes wrong,
> who experiences it, what triggers it?

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2×/sprint) |
|--------|-------------------------------------------------------------------------|-----------------------------------|----------------------------|----------------------------|
| FM-01  |                                                                         |                                   |                            |                            |
| FM-02  |                                                                         |                                   |                            |                            |

MINIMUM 2 rows [M-01]. REJECT generic descriptions — name the specific error or event.

---

## BRIDGE COMPLETION GATE

**[BRIDGE Q3 COMMAND — closes C-05 → R-02 — M-03]**: REVIEW the Actor / role
column. VERIFY every FM-[N] names a specific role. MARK Y or N. REVISE N rows.

| FM-[N] | Named role present? (Y / N) | Revision needed (e.g., "users" → "data-ops team") |
|--------|-----------------------------|---------------------------------------------------|
| FM-01  |                             |                                                   |
| FM-02  |                             |                                                   |

**[BRIDGE Q4 COMMAND — closes C-05 → C-04 — M-04]**: REVIEW the Trigger column.
VERIFY every trigger is specific and falsifiable. MARK Y or N. REVISE N rows.

| FM-[N] | Falsifiable trigger present? (Y / N) | Revision needed (e.g., "sometimes" → "file > 10MB") |
|--------|--------------------------------------|-----------------------------------------------------|
| FM-01  |                                      |                                                     |
| FM-02  |                                      |                                                     |

**BRIDGE COMPLETION STATUS**

| Bridge artifact | Populated? (Y / N) | If N: action required |
|-----------------|-------------------|-----------------------|
| Q3 — FM→ACTOR BRIDGE (closes C-05 → R-02) [M-03] |  | Revise Actor column in Section 1 — replace with named role |
| Q4 — FM→TRIGGER BRIDGE (closes C-05 → C-04) [M-04] |  | Revise Trigger column in Section 1 — add specific threshold or event |

Both rows must show Y before Section 2.

---

## SECTION 2 — WORKAROUND PROFILE

**[C-01 COMMAND — M-05]**: NAME the specific workaround — tool name, file type,
or procedure. NAME the role. QUANTIFY the ongoing cost with a number and unit.

> **C-01 question**: What is the exact name of the workaround — the specific
> tool, file type, or procedure name? Who performs it? What is the ongoing cost
> with a unit?

| Workaround name (specific tool / file / procedure — not "a manual process") | Role performing it (e.g., data-ops team) | Ongoing cost (e.g., 2 hours/week) | Duration in use (e.g., 18 months) |
|-----------------------------------------------------------------------------|------------------------------------------|-----------------------------------|-----------------------------------|
|                                                                             |                                          |                                   |                                   |

REJECT "teams export data manually" [M-05]. NAME the tool. NAME the role. GIVE the unit.

---

## SECTION 3 — SWITCHING COST ANALYSIS

**[C-02 COMMAND — M-06]**: IDENTIFY at least two cost categories. QUANTIFY each
with a number and unit. NAME the role bearing each cost.

> **[UNIT RULE — M-06]**: EVERY estimate carries a number and unit.
> "Significant" without a unit is REJECTED.

> **C-02 question**: If this team adopted {TOPIC} today, what would migration,
> training, and disruption cost? Who bears each cost? Every estimate must carry
> a number and a unit.

| Cost category | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) | Confidence level |
|---------------|------------------------|--------------------------------------|-----------------|
| Migration effort |                     |                                      |                 |
| Training overhead (e.g., 4 hours/person) |  |                           |                 |
| Process disruption (e.g., 1 sprint delay) | |                           |                 |
| In-flight work at risk (e.g., $8,000) |    |                           |                 |

---

## SECTION 4 — INERTIA THREAT ASSESSMENT

**[C-03 COMMAND — M-07]**: DECLARE the inertia threat score. DEFAULT IS HIGH.
IF deviating from HIGH, STATE a specific quantified condition.

> **C-03 question**: Given the total switching cost above, what is the inertia
> threat level for {TOPIC}? If deviating from HIGH, state a specific quantified
> condition — not a qualitative judgment.

| Threat score (HIGH / MEDIUM / LOW) | Deviation justification — quantified (required if not HIGH) |
|------------------------------------|-------------------------------------------------------------|
|                                    |                                                             |

---

## SECTION 5 — DEFEAT CONDITIONS

> **[A-19 CITATION INTEGRITY RULE — M-09]**: EVERY FM-[N] cited in this table
> MUST have an assigned row in Section 1 [M-02]. DO NOT introduce FM references
> not assigned above. VERIFY before filling.

**[C-04 COMMAND — M-08]**: DERIVE at least two specific, falsifiable defeat
conditions from Q4 triggers [M-04]. CITE FM-[N]. GIVE measurable threshold.
SCOPE to named team type.

> **C-04 question**: Under what specific, measurable conditions does a team
> abandon the workaround and adopt {TOPIC}? Cite FM-[N] driving the pressure.

| DC-[N] | FM-[N] cited | Defeat condition — specific and falsifiable | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type / segment |
|--------|-------------|--------------------------------------------|----------------------------------------------------|---------------------|
| DC-01  |             |                                            |                                                    |                     |
| DC-02  |             |                                            |                                                    |                     |

"When they see value" FAILS [M-08]. "When FM-01 causes silent data loss for the
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

## V-05

**Axis**: All three axes — output format (SCAFFOLD MANIFEST table with C-30 scope annotations + C-31 triple-convergence verbatim directives) + lifecycle emphasis (manifest as lifecycle declaration; stages named; each section body references manifest ID) + phrasing register (imperative [COMMAND] labels throughout; criterion-code labeled rules). Extends A-20 all-column inline example pattern to non-unit fields including bridge gate revision columns.

**Hypothesis**: Maximum structural convergence. SCAFFOLD MANIFEST satisfies C-30 (governed-sections column) and C-31 (pre-document + criterion-ID labels + verbatim directives in one block). Full [COMMAND] register satisfies A-11/A-17. All-column inline examples satisfy A-20 extension. Dual-type DC threshold satisfies A-21. Remediation-column bridge gate satisfies A-22. Criterion-code labeled rules satisfy A-16/A-19 pattern. All 23 criteria targeted simultaneously.

---

```
You are running /scout:inertia for the feature: {TOPIC}.

PRODUCE the complete inertia analysis below. FILL every table cell.
FOLLOW every labeled command. A blank cell is a visible structural failure.
Do not hedge or generalize. Specific evidence only.

---

# INERTIA ANALYSIS — {TOPIC}

---

## [FAIL-FIRST DECLARATION] — SCAFFOLD MANIFEST

Every structural constraint for this analysis is declared below before all
governed sections. Each entry identifies its criterion, the sections it governs,
and the verbatim directive that applies at each governed site. Read before
authoring any section. Do not reorder sections.

| Entry | Criterion | Governed sections | Verbatim directive — applies verbatim at governed site |
|-------|-----------|------------------|------------------------------------------------------|
| M-01 | C-05 | Section 1 — FM Inventory | "MINIMUM 2 rows required. 'Manual is slow' fails — name the specific error, truncation, silent failure, or data loss event." |
| M-02 | A-16 | Sections 1 (source) and 5 (citation) | "PRIMARY KEY CONSTRAINT: No FM-[N] may appear in Section 5 without an assigned row in Section 1. Assign all FM-[N] identifiers in Section 1 only." |
| M-03 | Q3 (closes C-05 → R-02) | Section 1 (Actor column), Section 3 (role attribution), Section 5 (team scoping) | "Every FM row names a specific role — not 'users', not 'the team'. Unroled failure modes cannot support role-scoped defeat conditions in Section 5." |
| M-04 | Q4 (closes C-05 → C-04) | Section 1 (Trigger column), Section 5 (threshold derivation) | "Every FM row carries a falsifiable trigger — a specific threshold or named event. 'Sometimes' and 'when usage grows' are not triggers. Triggers without thresholds cannot generate falsifiable defeat conditions." |
| M-05 | C-01 | Section 2 — Workaround Profile | "'Teams export data manually' fails — name the tool, the role, and quantify the cost with a number and unit." |
| M-06 | C-02 | Section 3 — Switching Cost | "Every estimate carries a number and a unit. 'Significant' without a number fails C-02. Minimum 2 cost categories." |
| M-07 | C-03 | Section 4 — Threat Assessment | "Default is HIGH. Deviation requires a specific quantified condition — not a qualitative judgment." |
| M-08 | C-04 | Section 5 — Defeat Conditions | "'When they see value' fails. Each row cites FM-[N] and states a measurable threshold. Minimum 2 rows." |
| M-09 | A-19 | Section 5 — Defeat Conditions | "REFERENTIAL INTEGRITY: Every FM-[N] cited in Section 5 must have an assigned row in Section 1. Do not introduce FM references not assigned there." |

Lifecycle: Section 1 → Bridge Gate → Section 2 → Section 3 → Section 4 →
Section 5. Bridge artifacts Q3 [M-03] and Q4 [M-04] must both be verified at
the Bridge Gate before Section 2.

---

## SECTION 1 — FAILURE MODE INVENTORY

**[C-05 COMMAND — M-01]**: NAME every specific failure mode. For each: NAME what
goes wrong (the error event, not "is slow"). NAME the role experiencing it (not
"users"). NAME the falsifiable trigger. ASSIGN an FM-[N] identifier.

> **[A-16 PRIMARY KEY RULE — M-02]**: ASSIGN all FM-[N] identifiers here. NO
> FM-[N] reference may appear in any later section without a row in this table.

> **C-05 question**: For {TOPIC}, where specifically does the current workaround
> fail, produce errors, cause rework, or hit a scale ceiling? What goes wrong,
> who experiences it, what triggers it?

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows) | Actor / role (e.g., data-ops team) | Trigger (e.g., pipeline ingests file > 10MB) | Frequency (e.g., 2×/sprint) |
|--------|-------------------------------------------------------------------------|-----------------------------------|---------------------------------------------|----------------------------|
| FM-01  |                                                                         |                                   |                                             |                            |
| FM-02  |                                                                         |                                   |                                             |                            |

MINIMUM 2 rows [M-01]. REJECT generic descriptions — name the specific error or event.

---

## BRIDGE COMPLETION GATE

**[BRIDGE Q3 COMMAND — closes C-05 → R-02 — M-03]**: REVIEW the Actor / role
column above. VERIFY every FM-[N] names a specific role — not "users", not
"the team". MARK each row Y or N. REVISE N rows before proceeding.

| FM-[N] | Named role present? (Y / N) | Revision needed (e.g., "users" → "data-ops team") |
|--------|-----------------------------|---------------------------------------------------|
| FM-01  |                             |                                                   |
| FM-02  |                             |                                                   |

**[BRIDGE Q4 COMMAND — closes C-05 → C-04 — M-04]**: REVIEW the Trigger column
above. VERIFY every trigger is a specific, falsifiable condition — a threshold or
named event. MARK each row Y or N. REVISE N rows before proceeding.

| FM-[N] | Falsifiable trigger present? (Y / N) | Revision needed (e.g., "sometimes" → "pipeline ingests file > 10MB") |
|--------|--------------------------------------|----------------------------------------------------------------------|
| FM-01  |                                      |                                                                      |
| FM-02  |                                      |                                                                      |

**BRIDGE COMPLETION STATUS**

| Bridge artifact | Populated? (Y / N) | If N: action required |
|-----------------|-------------------|-----------------------|
| Q3 — FM→ACTOR BRIDGE (closes C-05 → R-02) [M-03] |  | Revise Actor / role column in Section 1 — replace with named role |
| Q4 — FM→TRIGGER BRIDGE (closes C-05 → C-04) [M-04] |  | Revise Trigger column in Section 1 — add specific threshold or event |

Both rows must show Y before Section 2.

---

## SECTION 2 — WORKAROUND PROFILE

**[C-01 COMMAND — M-05]**: NAME the specific workaround — tool name, file type,
or procedure name. NAME the role performing it. QUANTIFY the ongoing cost with
a number and unit.

> **C-01 question**: What is the exact name of the workaround — the specific
> tool, file type, or procedure name? Who performs it? What is the ongoing cost
> with a unit?

| Workaround name (specific tool / file / procedure — not "a manual process") | Role performing it (e.g., data-ops team) | Ongoing cost (e.g., 2 hours/week) | Duration in use (e.g., 18 months) |
|-----------------------------------------------------------------------------|------------------------------------------|-----------------------------------|-----------------------------------|
|                                                                             |                                          |                                   |                                   |

REJECT "teams export data manually" [M-05]. NAME the tool. NAME the role. GIVE the unit.

---

## SECTION 3 — SWITCHING COST ANALYSIS

**[C-02 COMMAND — M-06]**: IDENTIFY at least two cost categories. QUANTIFY each
with a number and unit. NAME the role bearing each cost.

> **[UNIT RULE — M-06]**: EVERY estimate carries a number and unit.
> "Significant" without a unit is REJECTED.

> **C-02 question**: If this team adopted {TOPIC} today, what would migration,
> training, and disruption cost? Who bears each cost? Every estimate must carry
> a number and a unit.

| Cost category | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) | Confidence level (e.g., medium) |
|---------------|------------------------|--------------------------------------|--------------------------------|
| Migration effort |                     |                                      |                                |
| Training overhead (e.g., 4 hours/person) |  |                           |                                |
| Process disruption (e.g., 1 sprint delay) | |                           |                                |
| In-flight work at risk (e.g., $8,000) |    |                           |                                |

---

## SECTION 4 — INERTIA THREAT ASSESSMENT

**[C-03 COMMAND — M-07]**: DECLARE the inertia threat score. DEFAULT IS HIGH.
IF deviating from HIGH, STATE a specific quantified condition — a number,
percentage, or measurable threshold.

> **C-03 question**: Given the total switching cost above, what is the inertia
> threat level for {TOPIC}? If deviating from HIGH, state a specific quantified
> condition — not a qualitative judgment.

| Threat score (HIGH / MEDIUM / LOW) | Deviation justification — quantified, required if not HIGH (e.g., "switching cost < 2 days for teams < 5 engineers") |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------|
|                                    |                                                                                                                      |

---

## SECTION 5 — DEFEAT CONDITIONS

> **[A-19 CITATION INTEGRITY RULE — M-09]**: EVERY FM-[N] cited in this table
> MUST have an assigned row in Section 1 [M-02]. DO NOT introduce FM references
> not assigned above. VERIFY before filling.

**[C-04 COMMAND — M-08]**: DERIVE at least two specific, falsifiable defeat
conditions from Q4 triggers [M-04]. CITE the FM-[N] driving each. GIVE a
measurable threshold. SCOPE each to a named team type.

> **C-04 question**: Under what specific, measurable conditions does a team
> abandon the workaround and adopt {TOPIC}? Cite the FM-[N] driving the pressure.

| DC-[N] | FM-[N] cited | Defeat condition — specific and falsifiable (e.g., "FM-01 causes silent data loss for data-ops teams on files > 10MB") | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type / segment (e.g., data-ops teams > 20 pipelines) |
|--------|-------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------|
| DC-01  |             |                                                                                                                       |                                                     |                                                          |
| DC-02  |             |                                                                                                                       |                                                     |                                                          |

"When they see value" FAILS [M-08]. "When FM-01 causes silent data loss for the
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
| **C-30 Manifest Scope Annotation** | **PASS?** | **PASS?** | **PASS? (prose)** | **PASS?** | **PASS?** |
| **C-31 Triple-Constraint Manifest Convergence** | **FAIL** | **PASS?** | **UNCLEAR** | **PASS?** | **PASS?** |
| A-10 Fail-first declaration | PASS | PASS | PASS | PASS | PASS |
| A-11 Question per criterion (3+) | PASS | PASS | PASS | PASS | PASS |
| A-12 BRIDGE dual-closure | PASS | PASS | PASS | PASS | PASS |
| A-13 Tabular schema | PASS | PASS | PASS | PASS | PASS |
| A-14 FM inventory dedicated table | PASS | PASS | PASS | PASS | PASS |
| A-15 Trailing completeness checklist | PASS | PASS | PASS | PASS | PASS |
| A-16 Primary key constraint | PASS | PASS | PASS | PASS | PASS |
| A-17 Question coverage all 5 | PASS | PASS | PASS | PASS | PASS |
| A-18 Binary checklist format | PASS | PASS | PASS | PASS | PASS |
| A-19 Bidirectional referential integrity | PASS | PASS | PASS | PASS | PASS |
| A-20 Inline example unit-bearing columns | PASS | PASS | PASS | PASS | PASS |
| A-21 DC threshold dual-type inline example | PASS | PASS | PASS | PASS | PASS |
| A-22 Bridge completion status check | PASS | PASS | PASS | PASS | PASS |
| **Predicted score (v10, /23)** | **~21/23** | **~22-23/23** | **~21-22/23** | **~22-23/23** | **~23/23** |

**C-30/C-31 structural position across variations:**

- V-01: Manifest as scoped constraint TABLE with governed-sections column (C-30 target); verbatim directives remain in section bodies (C-31 miss — single manifest block lacks verbatim directives co-located with canonical strings)
- V-02: SCAFFOLD MANIFEST with criterion IDs + governed sections + verbatim directives in single pre-document table (C-30 + C-31 primary target)
- V-03: Prose STRUCTURAL MANIFEST with "CONSTRAINT-[N] [criterion] governs Section [N]" labeled prefix + verbatim acceptance/rejection conditions in prose body (C-30 prose form; C-31 uncertain — all three properties present but in prose not tabular form)
- V-04: SCAFFOLD MANIFEST table (C-30 + C-31) + lifecycle stages + [COMMAND] register + remediation-column bridge gate (dual-axis)
- V-05: SCAFFOLD MANIFEST table (C-30 + C-31) + full imperative register + all-column inline examples + lifecycle declaration + extended bridge gate (all-axes maximum convergence)

**Primary discriminator for C-31:** Whether criterion-ID-labeled entries + governed-sections + verbatim directives must be co-located in a TABLE (V-02/V-04/V-05) or can be satisfied by prose with labeled prefixes (V-03). If C-31 requires table structure, V-03 fails C-31. If format-agnostic, V-03 may pass both.
