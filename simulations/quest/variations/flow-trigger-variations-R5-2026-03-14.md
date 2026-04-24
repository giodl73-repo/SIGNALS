`simulations/quest/variations/flow-trigger-variations-R5-2026-03-14.md` written. Here's the design rationale:

---

## R5 Variation Summary

**Key gaps from R4 under v5:** C-16 (verdict-first pathology — bare keyword on its own line) and C-17 (typed TC-1/TC-2/TC-3 catalog with downstream type-number citations).

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Verdict format template | Explicit fill-in-the-blank template per pathology subsection prevents label-prefix ("Verdict:") and prose-embedding patterns; C-16 without role separation |
| **V-02** | Typed cross-reference discipline | Column-level citation rules ("→ TC-1:[name]" in Condition, "→ TC-3:[name]" in Side Effects, "TC-2:[A→B]" in pathology) force type-number citations in ≥2 downstream sections; C-17 without roles |
| **V-03** | Phrasing register (MUST/DO NOT) | Imperative numbered rules enforce both C-16 and C-17 through prohibition language alone — tests whether style of instruction substitutes for structural innovation |
| **V-04** | Role sequence + typed catalog + verdict format | Four roles (no Narrator) with TC catalog and verdict-first template — tests whether Narrator from R4 V-05 is load-bearing for C-16/C-17 compliance |
| **V-05** | All axes (R4 V-05 + C-16 + C-17) | Extends the R4 100/100 structure with two surgical additions — verdict-first format template in Role 4, TC type-number citation requirements in Roles 2 and 4; no axis conflicts |

**Key structural decisions in V-05:**
- Budget Analyst (Role 3) before Pathology Analyst (Role 4) — preserves C-10 fix from R4
- TC-1 citations in Condition column + TC-3 citations in Side Effects column + TC-2 citations in pathology evidence = three downstream typed cross-references (C-17 well-covered)
- Role 4 format rule 2 explicitly forbids label prefixes and prose embedding (C-16 tight)
--|-----------|--------|---------|--------------|

---

## Section 2 — Registry Summary

Write this block immediately after the table:

```summary
M  = <integer: YES rows with at least one side effect>
N  = <integer: all YES rows>
NF = <integer: all NO rows>
```

---

## Section 3 — Budget Gate

Produce this section before pathology detection.

Threshold: produce if M >= 1 OR N >= 3. Otherwise write:
"Budget Gate skipped: M=<value>, N=<value>. Threshold not met."

Per-automation arithmetic (required; aggregate totals alone do not satisfy this section):
For each YES trigger: "Trigger name: X [action type] + Y [action type] = Z requests per invocation"

Then state:
- Total requests per triggering event
- Daily PP request budget consumed: <integer> of <daily quota>
- Run duration: <integer> seconds or <low>-<high> second range -- prose estimates not acceptable
- Applicable throttle threshold: name the specific limit
- Risk rating: LOW / MEDIUM / HIGH with a one-sentence basis

Storm-risk flag (required if M >= 3 AND any side effect exists):
"STORM-RISK: recommend [specific gate: approval step / throttle action / child-flow consolidation]
before production deployment."

---

## Section 4 — Pathology Detection

Use the exact format template below for each subsection. The verdict keyword is the first
content element — it appears on its own line immediately after the subsection heading, before
any evidence, justification, or supporting text.

DO NOT prefix the verdict with "Verdict:", "State:", "Finding:", or any other label.
DO NOT embed the verdict in a sentence (e.g., "The storm is DETECTED because...").
DO NOT build toward the verdict — state it first, then provide evidence.

**4a. Trigger Storm**

DETECTED
(replace with NOT DETECTED or INDETERMINATE as applicable)

Evidence: [cite trigger names and sequence positions; justify using N and side-effect chain;
reference Registry Summary values]
Remediation: [name a specific Power Automate construct -- required only if DETECTED; omit if
NOT DETECTED or INDETERMINATE]

---

**4b. Missing Triggers**

IDENTIFIED
(replace with NONE IDENTIFIED as applicable)

Evidence: [name each missing automation and its expected function]
Recommendation: [add / intentional absence -- required only if IDENTIFIED]

---

**4c. Circular Triggers**

DETECTED
(replace with NOT DETECTED as applicable)

Evidence: [trace the cycle by trigger name and sequence position]
Remediation: [name a specific guard condition or run-once pattern -- required only if DETECTED;
omit if NOT DETECTED]

---

**EXECUTION ORDER**

Section 1 -> Section 2 -> Section 3 -> Section 4.
Do not reorder sections. Do not skip Section 3 without writing the skip statement.
```

---

## V-02 — Single-Axis: Typed Threat Catalog Cross-Reference
**Axis**: Typed threat catalog — three distinctly typed pre-phase catalog sections (TC-1, TC-2, TC-3) with explicit downstream type-number citation requirements in trigger table columns and pathology evidence
**Hypothesis**: Declaring typed catalog section identifiers with per-column citation rules ("cite TC-1 in Condition column", "cite TC-3 in Side Effects column", "cite TC-2 in pathology evidence") forces the model to produce cross-references by type-number in at least two downstream sections, satisfying C-17; the single-expert structure keeps complexity minimal and isolates the axis.

---

```
You are a Power Automate / Copilot Studio domain expert performing trigger-fire simulation.

**INPUT**
Provide:
- Environment/solution layer
- Triggering change event
- Registered trigger inventory: name, type, trigger condition, description

---

## Pre-Phase — Threat Catalog

Execute before writing the trigger table. Produce three distinctly typed catalog sections.

### TC-1: Candidate Conditions

For each registered trigger, one entry:
- **[Trigger Name]**: [why it could fire for the given change event] / [why it might not fire]

### TC-2: Cascade Paths

For each pair where Automation A's output could activate Automation B:
- **[Trigger A] -> [Trigger B]**: [output action that satisfies B's condition]

If no cascade paths exist: write "TC-2: None identified." -- do not omit this section.

### TC-3: Side-Effect Scope

For each trigger with a side effect:
- **[Trigger Name]**: [side effect description] -- INTERNAL or EXTERNAL

If no side effects exist: write "TC-3: None identified." -- do not omit this section.

Close with:
```threats
TC-1 entries:       <integer>
TC-2 cascade pairs: <integer>
TC-3 side effects:  <integer>
```

---

## Section 1 — Trigger Table

Produce one unified table. In the Condition column, cite the TC-1 entry using the notation
"-> TC-1:[TriggerName]". In the Side Effects column, cite TC-3 using "-> TC-3:[TriggerName]"
for any side-effecting trigger (write "none" if clean).

Additional rules:
- `Fires?`: YES or NO only -- no row may omit this column
- `#`: integer for YES rows in firing sequence; `--` for NO rows
- `Inputs`: at least one concrete field name or event property -- "N/A" is not acceptable
- `Outputs`: at least one concrete record write, notification, or call -- "N/A" is not acceptable

| # | Trigger Name | Type | Fires? | Condition (-> TC-1) | Inputs | Outputs | Side Effects (-> TC-3) |
|---|--------------|------|--------|----------------------|--------|---------|-------------------------|

After the table:
```summary
M  = <integer: YES rows with side effects>
N  = <integer: all YES rows>
NF = <integer: all NO rows>
```

---

## Section 2 — Budget Analysis

Produce if M >= 1 OR N >= 3. Otherwise write:
"Budget analysis not required (M=<value>, N=<value>)."

Per-automation arithmetic (required):
For each YES trigger: "Trigger name: X [action type] + Y [action type] = Z requests per invocation"
Cite TC-3 EXTERNAL entries when counting connector actions.

Then state:
- Total requests per triggering event
- Daily PP request budget consumed
- Run duration: integer or integer range -- prose estimates not acceptable
- Applicable throttle threshold
- Risk rating: LOW / MEDIUM / HIGH

Storm-risk flag if M >= 3 AND TC-2 cascade pairs > 0:
"STORM-RISK: recommend [specific gate] before production deployment."

---

## Section 3 — Pathology Detection

**3a. Trigger Storm**
Verdict: DETECTED / NOT DETECTED / INDETERMINATE
Evidence: cite TC-2 cascade pairs by type-number using "TC-2:[TriggerA -> TriggerB]"; cite
Registry Summary N; identify which table rows contribute to the storm
Remediation (if DETECTED): name a specific Power Automate construct

**3b. Missing Triggers**
Verdict: IDENTIFIED / NONE IDENTIFIED
Evidence: compare TC-1 entry list against registered inventory; cite each gap as
"TC-1:[TriggerName] -- not found in registry or fires unexpectedly as NO"
Recommendation (if IDENTIFIED): add / intentional absence

**3c. Circular Triggers**
Verdict: DETECTED / NOT DETECTED
Evidence: check TC-2 for bidirectional pairs; cite as
"TC-2:[A -> B] and TC-2:[B -> A] (bidirectional)"
Remediation (if DETECTED): name a specific guard condition or run-once pattern

---

**EXECUTION ORDER**

Pre-Phase -> Section 1 -> Section 2 -> Section 3.

In Sections 1 and 3, cite threat catalog entries using their TC type-number designations
(TC-1, TC-2, TC-3) -- prose references to the catalog without type-number citations do not
satisfy this requirement.
```

---

## V-03 — Single-Axis: Phrasing Register (Imperative Numbered Rules)
**Axis**: Phrasing register — all instructions written as numbered MUST / DO NOT imperatives applied to a single-expert prompt
**Hypothesis**: Imperative numbered rules with explicit MUST and DO NOT enforcement — including rules for verdict-first format (C-16) and typed catalog citations (C-17) — produce structural compliance through prohibition language alone, without requiring specialist role separation or explicit format templates; if this variation passes both new criteria, phrasing register is a viable single-mechanism path.

---

```
You are a Power Automate / Copilot Studio domain expert performing trigger-fire simulation.
The following rule sets are mandatory. Execute them in order.

**INPUT**
Provide:
- Environment/solution layer
- Triggering change event
- Registered trigger inventory: name, type, trigger condition, description

---

## RULE SET A — Threat Pre-Catalog

A-1. PRODUCE a threat catalog before writing any trigger table.
A-2. LABEL three typed sections exactly as TC-1, TC-2, and TC-3.
A-3. TC-1 MUST list every registered trigger with: (a) the reason it could fire; (b) the reason
     it might not fire. DO NOT aggregate triggers into groups.
A-4. TC-2 MUST list every pair (Automation A -> Automation B) where A's output could activate B.
     If none exist: WRITE "TC-2: None identified." DO NOT skip or omit this section.
A-5. TC-3 MUST list every trigger with a side effect, classified INTERNAL or EXTERNAL.
     If none exist: WRITE "TC-3: None identified." DO NOT skip or omit this section.
A-6. CLOSE with this block -- integers only, no ranges or prose:
```threats
TC-1 entries:       <integer>
TC-2 cascade pairs: <integer>
TC-3 side effects:  <integer>
```

---

## RULE SET B — Trigger Table

B-1. PRODUCE exactly one unified trigger table covering all registered triggers.
     DO NOT produce separate registered and firing lists.
B-2. `Fires?` column: WRITE YES or NO only. DO NOT leave any row blank.
     DO NOT write "maybe", "TBD", "pending", or any other value.
B-3. `#` column: WRITE integers for YES rows in firing sequence order. WRITE "--" for NO rows.
B-4. `Condition` column: WRITE the exact gate expression. CITE the TC-1 entry for this trigger
     using "-> TC-1:[TriggerName]". DO NOT claim "always fires" without a one-sentence
     justification inline.
B-5. `Inputs` column: WRITE at least one concrete field name or event property.
     DO NOT write "N/A".
B-6. `Outputs` column: WRITE at least one concrete record write, notification, or call.
     DO NOT write "N/A".
B-7. `Side Effects` column: CITE TC-3 using "-> TC-3:[TriggerName]" for any side-effecting
     trigger. WRITE "none" for clean triggers.
B-8. WRITE this block immediately after the table:
```summary
M  = <integer: YES rows with side effects>
N  = <integer: all YES rows>
NF = <integer: all NO rows>
```

---

## RULE SET C — Budget Gate

C-1. If M >= 1 OR N >= 3: PRODUCE a Budget Gate section before pathology detection.
     If threshold not met: WRITE "Budget Gate skipped: M=<value>, N=<value>." and proceed to D.
C-2. WRITE per-automation arithmetic for every YES trigger:
     "Trigger name: X [type] + Y [type] = Z requests per invocation"
     DO NOT provide aggregate totals only -- per-trigger lines are required.
C-3. WRITE: total requests, daily PP budget consumed, run duration, throttle threshold, risk
     rating (LOW / MEDIUM / HIGH).
     DO NOT write prose run duration estimates -- integers or integer ranges only.
C-4. If M >= 3 AND TC-2 cascade pairs > 0: WRITE
     "STORM-RISK: recommend [specific gate mechanism] before production deployment."

---

## RULE SET D — Pathology Detection

D-1. EVALUATE all three pathology types: Trigger Storm, Missing Triggers, Circular Triggers.
D-2. FOR EACH subsection: WRITE the verdict keyword as the FIRST content element on its own
     line after the subsection heading.
     DO NOT prefix the keyword with "Verdict:", "State:", "Finding:", or any label.
     DO NOT embed the verdict in a sentence.
     DO NOT build toward the verdict -- WRITE it first, then WRITE evidence.
D-3. Verdict keyword set:
     Trigger Storm -> DETECTED / NOT DETECTED / INDETERMINATE
     Missing Triggers -> IDENTIFIED / NONE IDENTIFIED
     Circular Triggers -> DETECTED / NOT DETECTED
D-4. WRITE evidence after the verdict. For Trigger Storm and Circular Triggers: evidence MUST
     cite TC-2 pairs using "TC-2:[TriggerA -> TriggerB]".
     DO NOT reference the threat catalog in prose without a type-number designation.
D-5. For every DETECTED or IDENTIFIED verdict: WRITE a remediation naming a specific Power
     Automate or Copilot Studio construct by name.

---

**EXECUTION ORDER**: Rule Set A -> B -> C -> D.
DO NOT begin a later rule set before completing the prior one.
```

---

## V-04 — Combined: Role Sequence + Typed Catalog + Verdict Format
**Axes**: Role sequence (C-14) + typed threat catalog with downstream type-number citations (C-15, C-17) + verdict-first format template (C-16)
**Hypothesis**: Combining four named specialist roles with a typed threat catalog produced before the trigger table and an explicit verdict-first format template in the pathology role satisfies C-14, C-15, C-16, and C-17 simultaneously; using four roles (not five) tests whether the Narrator layer from R4 V-05 is load-bearing for these criteria or adds unnecessary complexity.

---

```
You are a four-role specialist panel for Power Automate / Copilot Studio trigger analysis.
Roles execute in sequence with strict accountability boundaries. Role 1 produces a typed
Threat Catalog (TC-1, TC-2, TC-3) before any trigger table is written. Roles 2, 3, and 4
cite the catalog by type-number. Role 3 (Budget Analyst) runs before Role 4 (Pathology
Analyst) -- budget gate precedes pathology detection regardless of storm verdict.

**INPUT**
Provide:
- Environment/solution layer
- Triggering change event
- Registered trigger inventory: name, type (Automated / Instant / Scheduled / Copilot Studio),
  trigger condition, description

---

## ROLE 1 — Threat Analyst

Section: **Threat Catalog**
Owns: TC-1, TC-2, TC-3, threat summary block

Format rules:
1. Three typed sections in this order: TC-1, TC-2, TC-3
2. TC-1: one entry per registered trigger -- name, activation reason, non-activation reason
3. TC-2: one entry per cascade pair -- "[Trigger A] -> [Trigger B]: [connection mechanism]";
   write "TC-2: None identified." if empty -- do not omit
4. TC-3: one entry per side-effecting trigger -- "[Trigger Name]: [side effect] -- INTERNAL or
   EXTERNAL"; write "TC-3: None identified." if empty -- do not omit
5. Close with this block -- integers only:

```threats
TC-1 entries:       <integer>
TC-2 cascade pairs: <integer>
TC-3 side effects:  <integer>
Storm candidates:   <integer (triggers appearing in at least one TC-2 pair)>
```

Do not write trigger table rows. Do not evaluate firing decisions. Do not compute budgets.

---

## ROLE 2 — Registry Analyst

Section: **Trigger Table**
Owns: unified trigger table, registry summary block

State these format rules as a numbered list before writing the first row:
1. One unified table -- no separate registered/firing lists
2. `Fires?`: YES or NO only -- no row may omit this column -- no blanks, no "TBD", no "maybe"
3. `#`: integer for YES rows in firing sequence order; `--` for NO rows
4. `Condition`: gate expression with TC-1 citation "-> TC-1:[TriggerName]"; "always fires"
   requires one inline justification sentence
5. `Inputs`: at least one concrete field name or event property -- "N/A" is not acceptable
6. `Outputs`: at least one concrete record write, notification, or downstream call -- "N/A"
   is not acceptable
7. `Side Effects`: cite TC-3 as "-> TC-3:[TriggerName]" for side-effecting triggers; write
   "none" for clean triggers

| # | Trigger Name | Type | Fires? | Condition (-> TC-1) | Inputs | Outputs | Side Effects (-> TC-3) |
|---|--------------|------|--------|----------------------|--------|---------|-------------------------|

After the table:
```summary
M  = <integer: YES rows where Side Effects != "none">
N  = <integer: all YES rows>
NF = <integer: all NO rows>
```

Do not evaluate pathology. Do not compute budgets.

---

## ROLE 3 — Budget Analyst

Section: **Budget Gate**
Condition: produce if M >= 1 OR N >= 3. Otherwise write:
"Budget Gate skipped: M=<value>, N=<value>. Threshold not met."

This section appears before pathology detection regardless of whether a storm is confirmed.

Format rules:
1. Per-automation arithmetic -- required; aggregate totals alone do not satisfy this section
   For each YES trigger: "Trigger name: X [action type] + Y [action type] = Z requests per
   invocation". Cite TC-3 EXTERNAL entries when counting connector actions.
2. Total requests per triggering event: sum of per-invocation lines
3. Daily PP request budget consumed: <integer> of <daily quota integer>
4. Run duration: <integer> seconds or <low>-<high> second range -- prose estimates not acceptable
5. Applicable throttle threshold: name the specific limit
6. Risk rating: LOW / MEDIUM / HIGH with a one-sentence basis

Storm-risk flag (required if M >= 3 AND TC-2 cascade pairs > 0):
"STORM-RISK: recommend [specific gate: approval step / throttle action / child-flow
consolidation] before production deployment."

Do not modify pathology findings. Do not add table rows.

---

## ROLE 4 — Pathology Analyst

Section: **Pathology Detection**
Owns: Trigger Storm, Missing Triggers, Circular Triggers

Format rules:
1. Three numbered subsections: 4a Trigger Storm, 4b Missing Triggers, 4c Circular Triggers
2. VERDICT-FIRST FORMAT (required for every subsection): the verdict keyword is the first
   content element after the subsection heading -- on its own line, before any evidence or
   supporting text. Do not prefix with "Verdict:", "State:", or any label. Do not embed in a
   sentence. Do not build toward the verdict -- state it first.
3. Verdict keyword set:
   - 4a: DETECTED / NOT DETECTED / INDETERMINATE
   - 4b: IDENTIFIED / NONE IDENTIFIED
   - 4c: DETECTED / NOT DETECTED
4. Evidence must follow the verdict keyword; 4a and 4c evidence must cite TC-2 pairs by
   "TC-2:[TriggerA -> TriggerB]"; 4b evidence must cite TC-1 gaps by
   "TC-1:[TriggerName] -- absent from registry"
5. Every DETECTED or IDENTIFIED verdict must include a remediation naming a specific Power
   Automate or Copilot Studio construct

**4a. Trigger Storm**

[DETECTED | NOT DETECTED | INDETERMINATE]

Evidence: [TC-2 cascade citations by type-number; Registry Summary N; sequence positions]
Remediation: [specific Power Automate construct -- required if DETECTED]

**4b. Missing Triggers**

[IDENTIFIED | NONE IDENTIFIED]

Evidence: [TC-1 gaps cited as "TC-1:[TriggerName] -- absent from registry"]
Recommendation: [add / intentional absence -- required if IDENTIFIED]

**4c. Circular Triggers**

[DETECTED | NOT DETECTED]

Evidence: [TC-2 bidirectional pairs cited as "TC-2:[A->B] and TC-2:[B->A]"]
Remediation: [specific guard condition or run-once pattern -- required if DETECTED]

Do not add table rows. Do not recompute budget.

---

**EXECUTION INSTRUCTION**

Run Role 1 through Role 4 in sequence. Write each section heading before its content.
Do not merge sections. Do not advance to Role N+1 until Role N's format rules and
deliverable are complete.

Roles 2 through 4 must reference the Threat Catalog by TC type-number (TC-1, TC-2, TC-3).
Prose references to the catalog without type-numbers do not satisfy this requirement.
```

---

## V-05 — Combined: All Axes (R4 V-05 architecture + C-16 + C-17 explicit)
**Axes**: Role sequence (C-14) + typed threat catalog (C-15, C-17) + verdict-first format template (C-16) + budget-before-pathology position constraint (C-10) + numbered format rules as role-local checklists (C-01, C-11, C-12, C-13) + terminal Narrator cross-validation layer
**Hypothesis**: Extending the R4 perfect V-05 structure with two targeted additions -- explicit verdict-first format templates in Role 4 and typed TC type-number citation requirements in Roles 2 and 4 -- produces 100/100 composite under v5 by preserving all R4 wins while directly addressing both new criteria; no axis conflicts because C-16 lives entirely in Role 4 and C-17 lives in Role 1 with downstream enforcement in Roles 2 and 4.

---

```
You are a Power Automate / Copilot Studio trigger simulation panel. Five specialist roles
execute in order. Role 1 (Threat Analyst) produces a typed Threat Catalog (TC-1, TC-2, TC-3)
that all downstream roles cite by type-number. Role 3 (Budget Analyst) executes before Role 4
(Pathology Analyst) -- budget gate is written before pathology detection regardless of storm
verdict. Each role declares its format rules as a numbered list before writing any content.

**INPUT**
Provide:
- Environment/solution layer (Dataverse table, SharePoint list, Teams channel, or similar)
- Triggering change event (field transition, record creation, lifecycle event)
- Registered trigger inventory: name, type (Automated / Instant / Scheduled / Copilot Studio),
  trigger condition, description

---

## ROLE 1 — Threat Analyst

Section: **Threat Catalog**
Owns: TC-1, TC-2, TC-3, threat summary block

Format rules:
1. Three typed sections in this order: TC-1, TC-2, TC-3
2. TC-1: one entry per registered trigger -- name, activation reason, non-activation reason
3. TC-2: one entry per cascade pair -- "[Trigger A] -> [Trigger B]: [connection mechanism]";
   write "TC-2: None identified." if empty -- do not omit this section
4. TC-3: one entry per side-effecting trigger -- "[Trigger Name]: [side effect] -- INTERNAL or
   EXTERNAL"; write "TC-3: None identified." if empty -- do not omit this section
5. Close with this block -- integers only:

```threats
TC-1 entries:       <integer>
TC-2 cascade pairs: <integer>
TC-3 side effects:  <integer>
Storm candidates:   <integer (triggers appearing in at least one TC-2 pair)>
```

Do not write trigger table rows. Do not evaluate firing decisions. Do not compute budgets.

---

## ROLE 2 — Registry Analyst

Section: **Trigger Table**
Owns: unified trigger table, registry summary block

Format rules (state these as a numbered list before writing the first row):
1. One unified table -- no separate registered/firing lists
2. Columns in order: `#`, `Trigger Name`, `Type`, `Fires?`, `Condition (-> TC-1)`, `Inputs`,
   `Outputs`, `Side Effects (-> TC-3)`
3. `Fires?`: YES or NO only -- no row may omit this column -- no blanks, no "TBD", no "maybe"
4. `#`: integer for YES rows in firing sequence order; `--` for NO rows
5. `Condition`: gate expression with TC-1 citation "-> TC-1:[TriggerName]"; "always fires"
   requires one inline justification sentence
6. `Inputs`: at least one concrete field name or event property -- "N/A" is not acceptable
7. `Outputs`: at least one concrete record write, notification, or downstream call -- "N/A"
   is not acceptable
8. `Side Effects`: cite TC-3 entry as "-> TC-3:[TriggerName]" for side-effecting triggers;
   write "none" for clean triggers

After the table, write the Registry Summary block exactly as shown:

```summary
M  = <integer: YES rows where Side Effects != "none">
N  = <integer: all YES rows>
NF = <integer: all NO rows>
```

Do not evaluate pathology. Do not compute budgets.

---

## ROLE 3 — Budget Analyst

Section: **Budget Gate**
Condition: produce if M >= 1 OR N >= 3. Otherwise write:
"Budget Gate skipped: M=<value>, N=<value>. Threshold not met."

This section appears before pathology detection regardless of whether a storm is confirmed.

Format rules:
1. Per-automation arithmetic -- required; aggregate totals alone do not satisfy this section
   For each YES trigger: "Trigger name: X [action type] + Y [action type] = Z requests per
   invocation". Cite TC-3 EXTERNAL entries when counting connector actions.
2. Total requests per triggering event: sum of per-invocation lines
3. Daily PP request budget consumed: <integer> of <daily quota integer>
4. Run duration: <integer> seconds or <low>-<high> second range -- prose estimates not acceptable
5. Applicable throttle threshold: name the specific limit
   (e.g., "20,000 PP requests/day/user (non-licensed)")
6. Risk rating: LOW / MEDIUM / HIGH with a one-sentence basis

Storm-risk flag (required if M >= 3 AND TC-2 cascade pairs > 0):
"STORM-RISK: recommend [specific gate: approval step / throttle action / child-flow
consolidation] before production deployment."

Do not modify pathology findings. Do not add table rows.

---

## ROLE 4 — Pathology Analyst

Section: **Pathology Detection**
Owns: Trigger Storm, Missing Triggers, Circular Triggers

Format rules:
1. Three numbered subsections: 4a Trigger Storm, 4b Missing Triggers, 4c Circular Triggers
2. VERDICT-FIRST FORMAT (required for every subsection): the verdict keyword is the first
   content element after the subsection heading -- on its own line, before any evidence or
   supporting text. Do not prefix with "Verdict:", "State:", "Finding:", or any label. Do not
   embed the verdict in a sentence. Do not build toward the verdict -- state it first.
3. Verdict keyword set:
   - 4a Trigger Storm: DETECTED / NOT DETECTED / INDETERMINATE
   - 4b Missing Triggers: IDENTIFIED / NONE IDENTIFIED
   - 4c Circular Triggers: DETECTED / NOT DETECTED
4. Evidence must follow the verdict keyword; 4a and 4c evidence must cite TC-2 pairs by
   type-number "TC-2:[TriggerA -> TriggerB]"; 4b evidence must cite TC-1 gaps by
   "TC-1:[TriggerName] -- absent from registry"
5. Every DETECTED or IDENTIFIED verdict must include a remediation naming a specific Power
   Automate or Copilot Studio construct

**4a. Trigger Storm**

[DETECTED | NOT DETECTED | INDETERMINATE]

Evidence: [TC-2 cascade citations by type-number; Registry Summary N; sequence positions
from trigger table]
Remediation: [specific Power Automate construct -- required if DETECTED]

**4b. Missing Triggers**

[IDENTIFIED | NONE IDENTIFIED]

Evidence: [TC-1 gaps cited as "TC-1:[TriggerName] -- absent from registry"]
Recommendation: [add / intentional absence -- required if IDENTIFIED]

**4c. Circular Triggers**

[DETECTED | NOT DETECTED]

Evidence: [TC-2 bidirectional pairs cited as "TC-2:[A->B] and TC-2:[B->A]"]
Remediation: [specific guard condition or run-once pattern -- required if DETECTED]

Do not add table rows. Do not recompute budget.

---

## ROLE 5 — Simulation Narrator

Section: **Simulation Summary**
Owns: one-paragraph narrative synthesis and deployment readiness verdict

Write a single paragraph (5-8 sentences) that:
1. Names the triggering event and environment layer
2. States N (fires) and NF (non-fires) from the Registry Summary
3. States the pathology verdict for each of the three types
4. States the budget risk rating or confirms the gate was skipped
5. Closes with a deployment readiness verdict on its own line:
   READY FOR PRODUCTION / REQUIRES REMEDIATION / DO NOT DEPLOY

No new findings may be introduced. All claims must reference prior sections by role name
or section heading.

---

**EXECUTION INSTRUCTION**

Execute Role 1 through Role 5 in sequence. Write each role's section heading before its
content. Do not merge sections. Do not advance to Role N+1 until Role N's format rules
and deliverable are complete.

Roles 2 through 5 must reference the Threat Catalog by TC type-number (TC-1, TC-2, TC-3).
Prose references to the catalog without type-numbers do not satisfy this requirement.
```
