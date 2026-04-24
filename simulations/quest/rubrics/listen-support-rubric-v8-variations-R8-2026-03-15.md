# listen-support Round 8 — Skill Body Prompt Variations

**Rubric target**: v8 (185 pts)
**New criterion in scope**: C-27 (Named inertia competitor phase framing)
**Base**: All prior mechanisms from R7 V-05 (C-01 through C-26 at ceiling)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Inertia framing** — how prominently the named competitor appears and how early: weak (named once in STATUS QUO, used loosely in body) vs. strong (full INERTIA section, competitor threaded into every phase-bearing instruction) — (V-01)
2. **Lifecycle emphasis** — whether phase-differentiated body templates are instructed vs. pre-printed as a table before body generation, and how explicitly the phase boundary drives template selection — (V-02)
3. **Output format** — whether the pre-commitment vocabulary table carries a competitor-reference column that pre-locks the tool-name phrase before card bodies are written — (V-03)
4. **Inertia framing (strong) + Lifecycle emphasis (pre-printed templates)** combined — (V-04)
5. **Full synthesis**: Inertia framing (strong) + Lifecycle emphasis (pre-printed) + Performance-mode integration (competitor named in mode declaration itself) — (V-05)

---

## V-01: Single-Axis — Inertia Framing (Weak)

**Axis**: Inertia framing — minimal: competitor named once in STATUS QUO, referenced loosely in body instruction, switching-friction gap embedded inside existing doc/design/operational taxonomy rather than as its own sub-section.

**Hypothesis**: Tool-name fidelity in STATUS QUO alone is insufficient for C-27. Without explicit phase-differentiated body templates, property 2 will not appear reliably — the model will name the competitor in some bodies but will not differentiate by adoption-curve phase. Switching-friction embedded in C-04's three-bucket taxonomy will be present but not structurally distinguishable from other gap types, failing C-27 property 3. This variation establishes the baseline failure mode for all three C-27 properties simultaneously.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — STATUS QUO

Write a concrete current-state baseline before predicting any tickets.

Answer these four questions in 3–5 sentences total:
1. What are users doing today to accomplish the job this feature addresses?
2. **Name the specific tool or workflow they currently rely on by product name.**
   Prohibited: "existing tooling", "their current system", "legacy workflow", or any phrase
   that does not produce a grep-checkable product name string.
3. Where is friction highest in the current approach?
4. What workarounds exist, and what is their daily cost in time or steps?

The STATUS QUO is a description of the world before this feature ships. It is not a prediction.
Every volume rating and ticket body in Steps 4 and 5 must trace back to a specific element
of this baseline.

---

## STEP 2 — PHASE MAP TABLE

Produce the following table before generating any tickets. Do not change the column names.

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P0/P1 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P2/P3 | medium/low |

You will reference this table when assigning severity and volume in Step 4.
A Phase 1 ticket assigned P3/low is a phase-character violation.

---

## STEP 3 — PERFORMANCE MODE DECLARATION

Before writing any ticket body, enter performance mode.

**You ARE the persona named on each ticket card.**

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I".**

This instruction applies to every ticket body in Step 5.

---

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

Before writing full card bodies, lock all controlled-vocabulary values in a summary table.

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |
| T-08 | | | | | |

Fill every cell. Allowed values:
- Category: {how-to, bug, feature-request, config, integration}
- Volume: {high, medium, low}
- Severity: {P0, P1, P2, P3}

No other values are permitted. Synonyms ("configuration", "High", "blocker") fail C-02.

**Lock vocabulary values here. Full card bodies follow in Step 5.**

---

## STEP 4B — COLLECTIVE DISTRIBUTION AUDIT

After completing the summary table and before writing any card body,
audit these four constraints:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels (high, medium, low) present.
4. **Phase-character compliance** — each row's volume and severity match the Phase Map from Step 2.

State the result for each constraint: PASS or FAIL.

**If any constraint fails, correct the summary table and re-run this audit.
Name the correction made. Do not proceed until all four constraints pass.**

---

## STEP 5 — FULL CARD BODIES

For each row in the summary table, write a full ticket card using this exact structure:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

Body:
[Written in first person as the named persona. Every action belongs to "I".
Reference the STATUS QUO from Step 1: name what you were doing before,
what changed, and where friction remains.
Where the inertia competitor named in Step 1 naturally fits the persona's
experience, use the product name directly in the body.]
```

Repeat for every ticket ID in the summary table.

---

## STEP 6 — CROSS-TICKET PATTERNS

Identify at least one systemic pattern across multiple tickets.
For each pattern, use this flat field structure with no parent "Consequence:" container:

```
Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion" or any event not specific to this pattern.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence -- Adoption cost:
Prohibited: generic friction statements not specific to this cohort.
[One sentence quantifying or qualifying the friction for the named segment]
```

---

## STEP 7 — GAP ANALYSIS

Produce a gap analysis with three explicitly labeled sub-sections.
Each sub-section must contain at least one identified gap.

### Doc Gaps
[At least one documentation gap. Name what is missing or incorrect.]

### Design Gaps
[At least one product or UX design gap. Name the incomplete or wrong decision.]

### Operational Gaps
[At least one runbook, monitoring, or process gap. Name what is absent.]

Within these three sections, include at least one gap that names the inertia competitor
from Step 1 explicitly and frames it as a friction point for users coming from that tool.
Example form: "Users moving from [TOOL] expect [behavior]; the current design
does not address this, creating adoption friction."

### Pre-Launch Priority
State which single gap to close first and why.
Tie the recommendation explicitly to the severity and volume of the tickets it would prevent.
Example: "Close [gap] first — it directly drives T-01 (P1/high) and T-03 (P1/medium)."

---

## STEP 8 — DUAL-PASS VERIFICATION

### PASS 1 — Coverage Trace Table

Produce a table with one row per ticket:

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|
| T-01 | | |
| T-02 | | |
| T-03 | | |
| T-04 | | |
| T-05 | | |
| T-06 | | |
| T-07 | | |
| T-08 | | |

Fill every cell. No ticket row may have a blank STATUS QUO element.
After completing the table, state explicitly:
**"No gap from the Gap Analysis is absent from this table."**

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 — Frontmatter Verify

Confirm that the summary table from Step 4 matches every Ticket ID, Phase,
Category, Persona, Volume, and Severity in the full card bodies from Step 5.
Check field by field.

State: **"All Ticket IDs, phases, categories, personas, volumes, and severities
match between Step 4 and Step 5."**
If any mismatch is found, name it and correct it before finalizing.
```

---

## V-02: Single-Axis — Lifecycle Emphasis (Explicit Phase Body Template Table)

**Axis**: Lifecycle emphasis — an explicit two-row phase body template table is generated as STEP 2B, immediately after the phase map, before performance mode is declared. The table pre-prints one sentence template per phase (P1/P3) that includes a competitor placeholder. Card body instructions reference the table by step number and require the filing persona to use the appropriate phase template.

**Hypothesis**: The phase template table is the load-bearing structural mechanism for C-27 property 2. When the model is given pre-printed template sentences by phase before any card is written, it will consistently produce phase-differentiated body framing. Without this table, even explicit body instructions to "differentiate by phase" produce post-hoc calibration rather than structural compliance. The table makes phase-template selection grep-checkable (the sentence pattern appears in the body) rather than a matter of tonal interpretation.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — STATUS QUO

Write a concrete current-state baseline before predicting any tickets.

Answer these four questions in 3–5 sentences total:
1. What are users doing today to accomplish the job this feature addresses?
2. **Name the specific tool or workflow they currently rely on by product name.**
   Prohibited: "existing tooling", "their current system", or any non-product-name phrase.
   This name is the INERTIA COMPETITOR. You will reference it by name in Steps 2B and 5.
3. Where is friction highest in the current approach?
4. What workarounds exist, and what is their daily cost in time or steps?

---

## STEP 2 — PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P0/P1 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P2/P3 | medium/low |

You will reference this table when assigning severity and volume in Step 4.

---

## STEP 2B — PHASE BODY TEMPLATE TABLE

Before writing any ticket body, pre-print the two body stance templates below.
Replace [INERTIA COMPETITOR] with the product name from Step 1.
These templates are the required opening stance for card bodies in their respective phases.

| Phase | Adoption position | Required body template sentence |
|-------|------------------|----------------------------------|
| Phase 1 | Early adopter — dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while I'm working through this..." |
| Phase 3 | Late adopter — parity gap | "In [INERTIA COMPETITOR] I could do [specific action]; here I cannot find a way to do it." |

**Instructions for Step 5:**
- Every Phase 1 card body must open with or contain the Phase 1 template sentence
  (competitor name substituted).
- Every Phase 3 card body must open with or contain the Phase 3 template sentence
  (competitor name substituted, [specific action] replaced with a concrete action).
- Phase 2 bodies are not required to use either template but may reference the competitor
  if it naturally fits the persona's experience.

---

## STEP 3 — PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any role title preceding a verb.

**Every action in this ticket was taken by "I".**

---

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |
| T-08 | | | | | |

Allowed values:
- Category: {how-to, bug, feature-request, config, integration}
- Volume: {high, medium, low}
- Severity: {P0, P1, P2, P3}

**Lock vocabulary values here. Full card bodies follow in Step 5.**

---

## STEP 4B — COLLECTIVE DISTRIBUTION AUDIT

Audit four constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 — FULL CARD BODIES

For each row in the summary table, write a full ticket card:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

Body:
[Written in first person as the named persona.
- Phase 1 tickets: open with or include the Phase 1 template sentence from Step 2B,
  with [INERTIA COMPETITOR] replaced by the product name.
- Phase 3 tickets: open with or include the Phase 3 template sentence from Step 2B,
  with [INERTIA COMPETITOR] replaced and [specific action] replaced by a concrete action.
- All tickets: reference the STATUS QUO element from Step 1 that drives this ticket's
  volume and severity. No third-person references to yourself.]
```

---

## STEP 6 — CROSS-TICKET PATTERNS

For each pattern, use this flat field structure:

```
Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence -- Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying the friction for the named segment]
```

---

## STEP 7 — GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
At least one gap must be explicitly framed as a migration barrier for users
coming from the INERTIA COMPETITOR named in Step 1.

Required format for each switching-friction gap:
```
Gap: [short name]
Competitor: [product name from Step 1]
Barrier: [one sentence describing what the competitor provided that this feature does not]
Migration impact: [one sentence on what users must change or lose when switching]
```

### Pre-Launch Priority
Name the single gap to close first. Tie the recommendation to specific ticket IDs,
their severity, and their volume.

---

## STEP 8 — DUAL-PASS VERIFICATION

### PASS 1 — Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|
| T-01 | | |
| T-02 | | |
| T-03 | | |
| T-04 | | |
| T-05 | | |
| T-06 | | |
| T-07 | | |
| T-08 | | |

After completing the table, confirm:
**"No gap from the Gap Analysis is absent from this table."**

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 — Frontmatter Verify

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.

State: **"All Ticket IDs, phases, categories, personas, volumes, and severities
match between Step 4 and Step 5."**
Name and correct any mismatch before finalizing.
```

---

## V-03: Single-Axis — Output Format (Competitor Reference Column in Pre-Commitment Table)

**Axis**: Output format — the vocabulary pre-commitment table gains a sixth column: "Competitor reference phrase". Before any card body is written, the model locks the specific sentence fragment that will appear in that card's body referencing the inertia competitor. This column is filled at the same time as category/persona/volume/severity. The body instruction references the column by name and requires the pre-committed phrase to appear verbatim.

**Hypothesis**: Pre-committing the exact competitor reference phrase forces tool-name fidelity (C-27 property 1) to propagate into every card body by structural necessity rather than per-card instruction compliance. However, without phase-differentiated body templates, the pre-committed phrases may be uniform across phases — satisfying C-27 property 1 but not property 2. The column forces the model to decide upfront whether the phrase is phase-appropriate, which may produce emergent phase differentiation without explicit templates. Whether this emergent differentiation is consistent enough to pass C-27 is the testable question.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — STATUS QUO

Write a concrete current-state baseline before predicting any tickets.

Answer these four questions in 3–5 sentences total:
1. What are users doing today to accomplish the job this feature addresses?
2. **Name the specific tool or workflow they currently rely on by product name.**
   This product name is the INERTIA COMPETITOR. Record it here; you will use it in
   Steps 4 and 5.
   Prohibited: "existing tooling", "their current system", or any non-product-name phrase.
3. Where is friction highest in the current approach?
4. What workarounds exist, and what is their daily cost?

---

## STEP 2 — PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P0/P1 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P2/P3 | medium/low |

---

## STEP 3 — PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any role title preceding a verb.

**Every action in this ticket was taken by "I".**

---

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

Before writing full card bodies, lock all controlled-vocabulary values AND
the competitor reference phrase for each ticket.

| Ticket ID | Phase | Category | Persona | Volume | Severity | Competitor reference phrase |
|-----------|-------|----------|---------|--------|----------|-----------------------------|
| T-01 | | | | | | |
| T-02 | | | | | | |
| T-03 | | | | | | |
| T-04 | | | | | | |
| T-05 | | | | | | |
| T-06 | | | | | | |
| T-07 | | | | | | |
| T-08 | | | | | | |

**Competitor reference phrase** rules:
- Must contain the INERTIA COMPETITOR product name from Step 1 verbatim.
- Must be a fragment that can appear naturally in first-person ticket body prose.
- Must reflect the persona's relationship to the competitor at this adoption phase.
  Phase 1 example: "I still have [PRODUCT] open and I ran the same operation there first..."
  Phase 3 example: "In [PRODUCT] I could configure this in two steps; here I cannot."
- Prohibited: "as mentioned previously", "per existing tooling", or any phrase that
  does not contain the product name.

Allowed vocabulary values:
- Category: {how-to, bug, feature-request, config, integration}
- Volume: {high, medium, low}
- Severity: {P0, P1, P2, P3}

**Lock all values here, including the competitor reference phrase.
Full card bodies follow in Step 5. Do not generate a competitor reference phrase
for the first time inside a card body.**

---

## STEP 4B — COLLECTIVE DISTRIBUTION AUDIT

Audit four constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2.

Additionally audit:
5. **Competitor phrase fidelity** — every "Competitor reference phrase" cell contains
   the product name from Step 1 as a verbatim string. Scan the column.
   State: PASS if all cells contain the product name. FAIL if any cell is missing it.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 — FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

Body:
[Written in first person as the named persona.
Include the exact competitor reference phrase from Step 4's "Competitor reference phrase"
column for this ticket. The phrase must appear verbatim.
Reference the STATUS QUO element from Step 1 that drives this ticket's volume and severity.
No third-person references to yourself.]
```

---

## STEP 6 — CROSS-TICKET PATTERNS

For each pattern, use this flat field structure:

```
Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence -- Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying the friction for the named segment]
```

---

## STEP 7 — GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
At least one gap must be explicitly framed as a barrier for users migrating from
the INERTIA COMPETITOR named in Step 1. Name the competitor in the gap description.
Example: "Users migrating from [PRODUCT] expect [behavior]; the current design does
not provide it, creating a switching-friction barrier."

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.

---

## STEP 8 — DUAL-PASS VERIFICATION

### PASS 1 — Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|
| T-01 | | |
| T-02 | | |
| T-03 | | |
| T-04 | | |
| T-05 | | |
| T-06 | | |
| T-07 | | |
| T-08 | | |

Confirm: **"No gap from the Gap Analysis is absent from this table."**

Additionally: scan the "STATUS QUO element referenced" column and confirm that
the competitor product name from Step 1 appears in at least two rows.
State: **"Competitor name [PRODUCT] appears in rows: [T-NN, T-NN, ...]."**

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 — Frontmatter Verify

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, Severity, and Competitor reference phrase in the full card bodies.

State: **"All values in Step 4 match Step 5 card bodies, including competitor
reference phrases."**
Name and correct any mismatch before finalizing.
```

---

## V-04: Combination — Inertia Framing (Strong) + Lifecycle Emphasis (Pre-Printed Templates)

**Axes**: Inertia framing (strong: STATUS QUO restructured as a full INERTIA section with adoption-curve context; competitor threaded into every phase-bearing step) + Lifecycle emphasis (STEP 2B pre-prints both phase template sentences with competitor placeholder, making selection mandatory by phase assignment).

**Hypothesis**: Combining a structured INERTIA section with pre-printed phase templates closes all three C-27 properties simultaneously with no per-card instruction dependency. Property 1 (tool-name fidelity) is enforced by the INERTIA section's explicit prohibition on non-product-name phrases. Property 2 (phase-differentiated templates) is enforced by the STEP 2B table's pre-printed sentences, which the body instruction requires to appear verbatim. Property 3 (switching-friction gap) is enforced by a required sub-section in STEP 7 with a structural format. No property requires the model to make a judgment call about when or whether to name the competitor — all three are pre-committed before any ticket is written.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — INERTIA: STATUS QUO

Establish two things before predicting any tickets: the current-state baseline
and the inertia competitor.

**1a. Current-state baseline**
Describe in 2–3 sentences: what are users doing today to accomplish the job
this feature addresses? Where is friction highest? What workarounds exist?

**1b. Inertia competitor**
Name the specific tool or workflow users currently rely on.

```
INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.
```

**1c. Adoption-curve position**
Describe where your user base sits on the adoption curve for this feature.
Are most users still fully on the inertia competitor (early phase)?
Or are some users already mid-migration (late phase)?
This context drives volume distribution across phases in Steps 2 and 4.

Every volume rating and ticket body in Steps 4 and 5 must trace back to a specific
element of this baseline.

---

## STEP 2 — PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P0/P1 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P2/P3 | medium/low |

Phase 1 users are early adopters running dual-tool workflows.
Phase 3 users are late adopters expecting feature parity with the inertia competitor.
Both populations create structurally different tickets. The body templates in Step 2B
reflect this difference.

---

## STEP 2B — PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b before writing this table.
These are the required body stance templates for Phase 1 and Phase 3 tickets.

| Phase | Adoption stance | Required body template sentence |
|-------|----------------|----------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while I'm working through this — I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] in [N] steps; here I cannot find a way to do it at all." |

**Instructions for Step 5:**
- Every Phase 1 card body must contain the Phase 1 template sentence with
  [INERTIA COMPETITOR] replaced and [specific scenario] replaced with the scenario
  driving this ticket.
- Every Phase 3 card body must contain the Phase 3 template sentence with
  [INERTIA COMPETITOR] replaced, [specific action] and [N] filled in concretely.
- Phase 2 bodies may reference the competitor where it fits naturally but are not
  required to use either template.

---

## STEP 3 — PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any role title preceding a verb.

**Every action in this ticket was taken by "I".**

---

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |
| T-08 | | | | | |

Allowed values:
- Category: {how-to, bug, feature-request, config, integration}
- Volume: {high, medium, low}
- Severity: {P0, P1, P2, P3}

**Lock vocabulary values here. Full card bodies follow in Step 5.**

---

## STEP 4B — COLLECTIVE DISTRIBUTION AUDIT

Audit four constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
   Required: at least two Phase 1 tickets to generate at least two dual-tool-tension
   bodies using the Phase 1 template from Step 2B.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 — FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

Body:
[Written in first person as the named persona.
- Phase 1 tickets: include the Phase 1 template sentence from Step 2B verbatim
  (with placeholders filled).
- Phase 3 tickets: include the Phase 3 template sentence from Step 2B verbatim
  (with placeholders filled).
- All tickets: reference the STATUS QUO element from Step 1 that drives
  this ticket's volume and severity.
- No third-person references to yourself.]
```

---

## STEP 6 — CROSS-TICKET PATTERNS

For each pattern, use this flat field structure:

```
Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence -- Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying the friction for the named segment]
```

---

## STEP 7 — GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
This sub-section is required. At least one gap must describe a barrier specific to
users migrating from the INERTIA COMPETITOR named in Step 1b.

Required format:
```
Switching-friction gap: [short name]
Inertia competitor: [product name from Step 1b — must appear verbatim]
What the competitor provided: [one sentence — what users could do in the competitor
  that they cannot do here]
Migration barrier: [one sentence — the specific friction users encounter
  when they try to replicate their competitor workflow here]
```

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether closing it also reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 — DUAL-PASS VERIFICATION

### PASS 1 — Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|
| T-01 | | |
| T-02 | | |
| T-03 | | |
| T-04 | | |
| T-05 | | |
| T-06 | | |
| T-07 | | |
| T-08 | | |

After completing the table, confirm:
**"No gap from the Gap Analysis — including switching-friction gaps — is absent
from this table."**

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 — Frontmatter Verify

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.

Also confirm: **"Phase 1 ticket bodies contain the Phase 1 template sentence
from Step 2B. Phase 3 ticket bodies contain the Phase 3 template sentence from Step 2B."**

State: **"All values match between Step 4 and Step 5. Phase template sentences verified."**
Name and correct any mismatch before finalizing.
```

---

## V-05: Full Synthesis — Inertia Framing + Lifecycle Emphasis + Performance-Mode Integration

**Axes**: Inertia framing (strong: INERTIA COMPETITOR declared in Step 1, referenced throughout) + Lifecycle emphasis (pre-printed phase templates in Step 2B) + Performance-mode integration (the performance mode declaration in Step 3 anchors the persona's identity to their migration from the named competitor — "You ARE [persona] who recently started using this product. Your previous workflow used [INERTIA COMPETITOR]." This single stance shift makes all three C-27 properties emerge from one structural anchor rather than three independent instructions).

**Hypothesis**: Integrating the inertia competitor into the performance-mode declaration itself is the strongest structural guarantee for C-27. When the persona's declared identity includes migration from a named tool, phase-differentiated body framing becomes a natural consequence of the stance rather than a requirement the model must remember to apply. The P1 template ("I still have [tool] open") emerges from a persona who has just started migrating. The P3 template ("In [tool] I could do X") emerges from a persona whose migration is incomplete. The switching-friction gap emerges from the same persona describing what they cannot yet do. All three properties share one structural root: the identity declaration. This is the minimal-instruction path to C-27 compliance.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — INERTIA: STATUS QUO

Establish the current-state baseline and name the inertia competitor.

**1a. Current-state baseline**
Describe in 2–3 sentences: what are users doing today? Where is friction highest?
What workarounds exist and what do they cost?

**1b. Inertia competitor declaration**

```
INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.
```

This product name will be embedded in the performance mode declaration in Step 3.
It will appear verbatim in every Phase 1 and Phase 3 ticket body and in at least one
gap from the Gap Analysis. Record it once here; reference it by name everywhere else.

**1c. Adoption-curve context**
Note where the user population sits: early (mostly still on the competitor, dual-tool phase)
or late (partially migrated, parity-gap phase). This drives phase distribution in Step 4.

---

## STEP 2 — PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P0/P1 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P2/P3 | medium/low |

---

## STEP 2B — PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b now.
These pre-printed template sentences are the required opening stance for
Phase 1 and Phase 3 card bodies. Placeholders must be filled concretely in Step 5.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this — I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

Instructions:
- Phase 1 bodies: include the Phase 1 sentence with all placeholders filled concretely.
- Phase 3 bodies: include the Phase 3 sentence with all placeholders filled concretely.
- Phase 2 bodies: reference the competitor where it naturally fits; no template required.

---

## STEP 3 — PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — insert product name from Step 1b].
You recently started using this new product. You are in some stage of migration:
Phase 1 tickets are written when you still have the old tool open. Phase 3 tickets
are written when you have committed to the new tool but are discovering what it cannot do.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |
| T-08 | | | | | |

Allowed values:
- Category: {how-to, bug, feature-request, config, integration}
- Volume: {high, medium, low}
- Severity: {P0, P1, P2, P3}

**Lock vocabulary values here. Full card bodies follow in Step 5.**

---

## STEP 4B — COLLECTIVE DISTRIBUTION AUDIT

Audit four constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
   Rationale: the adoption-curve context from Step 1c must produce at least two
   dual-tool-tension bodies and at least one parity-gap body.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 — FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

Body:
[You ARE this persona. You previously used [INERTIA COMPETITOR — product name].
- Phase 1 tickets: open with the Phase 1 template sentence from Step 2B,
  placeholders filled concretely.
- Phase 3 tickets: open with the Phase 3 template sentence from Step 2B,
  placeholders filled concretely.
- All tickets: reference the STATUS QUO element from Step 1 that drives
  this ticket's volume and severity.
- No third-person references to yourself. No unnamed references to the old tool —
  use the product name from Step 1b every time you mention it.]
```

---

## STEP 6 — CROSS-TICKET PATTERNS

For each pattern, use this flat field structure with no parent "Consequence:" container:

```
Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence -- Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying the friction for the named segment]
```

If a pattern involves migration from the inertia competitor, name the competitor
in the root cause or consequence fields.

---

## STEP 7 — GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
Required sub-section. At least one gap must be a switching-friction gap:
a specific barrier for users migrating from the INERTIA COMPETITOR named in Step 1b.

Required format:
```
Switching-friction gap: [short name]
Inertia competitor: [product name from Step 1b — verbatim]
What the competitor provided: [what users could do in the competitor
  that this product does not yet support]
Migration barrier: [the specific friction users hit when trying to replicate
  their competitor workflow here]
Not closing this means: [one sentence on the adoption cost if this gap persists —
  name the affected cohort and the migration stage where they stall]
```

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 — DUAL-PASS VERIFICATION

### PASS 1 — Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|
| T-01 | | |
| T-02 | | |
| T-03 | | |
| T-04 | | |
| T-05 | | |
| T-06 | | |
| T-07 | | |
| T-08 | | |

After completing the table:
1. Confirm: **"No gap from the Gap Analysis — including switching-friction gaps —
   is absent from this table."**
2. Confirm: **"The inertia competitor product name from Step 1b appears in at least
   two STATUS QUO element cells in this table."**

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 — Frontmatter Verify

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.

Also confirm the following three C-27 properties hold in the completed output:
1. **Tool-name fidelity** — the inertia competitor product name from Step 1b
   appears verbatim in Step 1b, at least two card bodies, and at least one
   switching-friction gap. State: **"[PRODUCT NAME] appears in Step 1b: YES.
   Card bodies: T-NN, T-NN (at minimum). Switching-friction gap: YES."**
2. **Phase-differentiated templates** — at least two Phase 1 bodies contain the
   Phase 1 template sentence from Step 2B, and at least one Phase 3 body contains
   the Phase 3 template sentence. State: **"Phase 1 template confirmed in: T-NN, T-NN.
   Phase 3 template confirmed in: T-NN."**
3. **Switching-friction gap** — the Switching-Friction Gaps sub-section in Step 7
   contains at least one gap with the competitor product name in the
   "Inertia competitor:" field. State: **"Switching-friction gap present: YES."**

State: **"All Step 4 values match Step 5. All three C-27 properties verified."**
Name and correct any mismatch before finalizing.
```

---

## Variation Summary

| Variation | Primary axis | C-27 P1: Tool name | C-27 P2: Phase templates | C-27 P3: Switching-friction gap | Hypothesis |
|-----------|-------------|-------------------|--------------------------|--------------------------------|------------|
| V-01 | Inertia framing (weak) | Named in Step 1, used loosely in body | None — no template table | Embedded in C-04 taxonomy, no own sub-section | P1 fails without template table; P3 passes via loose embedding |
| V-02 | Lifecycle emphasis | Named in Step 1, referenced in template table | Pre-printed table in Step 2B, verbatim required | Own sub-section in Step 7 | Template table is load-bearing mechanism for P2 |
| V-03 | Output format (pre-commit column) | Named in Step 1, locked per-ticket in pre-commit table | No template table — emergent from pre-committed phrases | Own sub-section in Step 7 | Pre-commitment may produce emergent phase-differentiation but not guaranteed |
| V-04 | Inertia (strong) + Lifecycle | INERTIA section with explicit prohibition | Pre-printed table in Step 2B | Required sub-section with structured format | Structural combination closes all three properties with no per-card judgment |
| V-05 | Full synthesis (inertia + lifecycle + perf-mode) | Named in INERTIA + embedded in perf-mode declaration | Pre-printed table in Step 2B + perf-mode stance shift | Required sub-section with "Not closing this means:" field | Perf-mode integration makes phase-differentiation a stance consequence, not a remembered rule |

**Expected C-27 outcomes**:
- V-01: FAIL P2 (no phase templates), PARTIAL P3 (gap present but not structurally labeled as switching-friction)
- V-02: PASS all three (template table + own gap sub-section)
- V-03: PARTIAL P2 (emergent phrases may not differentiate by phase), PASS P3
- V-04: PASS all three (strongest structural separation)
- V-05: PASS all three (strongest single-anchor guarantee, C-27 properties emerge from one root)
