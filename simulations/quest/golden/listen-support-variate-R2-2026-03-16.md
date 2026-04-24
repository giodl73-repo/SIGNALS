# listen-support Round 2 — Skill Body Prompt Variations

**Date:** 2026-03-16
**Rubric target:** v2 (115 pts ceiling — C-01 through C-13)
**Base:** R1 V-05 (C-01 through C-10 passing)

**What v2 adds over v1:**
- **C-11** — Phase as first-class ticket field (5 pts)
- **C-12** — Fallback-grounded severity rationale (5 pts)
- **C-13** — Mid-output verification block (5 pts)
- Aspirational bucket: 2 criteria → 5 criteria, 10 pts → 25 pts max
- Max composite: 100 → 115

**Axes explored this round:**

1. **Output format — Phase as declared field** (V-01): Phase column in pre-commitment
   table + Phase field on every card; tests whether C-11 compliance is structural
   (auditable from field values) vs inferential (requires reading body text)
2. **Inertia framing — Fallback rationale as severity mechanism** (V-02): each ticket
   requires an explicit Fallback Rationale: line before the Severity field; tests whether
   mechanical inference beats asserted severity for C-12 compliance
3. **Lifecycle emphasis — Mid-output verification block** (V-03): mandatory PASS/FAIL
   audit fires between ticket bodies and gap analysis; tests C-13 structural mechanism
4. **Combined — Phase field + Fallback rationale** (V-04 = V-01 + V-02): tests whether
   C-11 + C-12 stack cleanly without either constraining the other
5. **Full synthesis** (V-05 = V-01 + V-02 + V-03): all three v2 criteria simultaneously;
   tests stacking without essential criteria degrading

**Axes deferred (already explored in R1 2026-03-16):**
- Phrasing register — imperative/technical (V-01)
- Phrasing register — performance/conversational (V-02)
- Inertia framing — front-loaded competitor (V-03)
- Performance + inertia combined (V-04)
- Performance + inertia + pre-commitment table (V-05)

**v2 rubric criterion hypothesis matrix:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 field completeness | YES | YES | YES | YES | YES |
| C-02 vocab validity | YES | YES | YES | YES | YES |
| C-03 first-person voice | YES | YES | YES | YES | YES |
| C-04 three-axis gap | YES | YES | YES | YES | YES |
| C-05 min ticket count | YES | YES | YES | YES | YES |
| C-06 phase distribution | YES | YES | YES | YES | YES |
| C-07 phase-severity alignment | YES | YES | YES | YES | YES |
| C-08 role diversity | YES | YES | YES | YES | YES |
| C-09 inertia competitor grounding | YES | YES | YES | YES | YES |
| C-10 pre-commitment table | YES | YES | YES | YES | YES |
| C-11 phase as first-class field | YES | — | — | YES | YES |
| C-12 fallback-grounded severity | — | YES | — | YES | YES |
| C-13 mid-output verification block | — | — | YES | — | YES |

---

## V-01: Single-Axis — Phase as First-Class Ticket Field (C-11)

**Axis:** Output format — Phase is elevated from a body label to a declared metadata
field at the same level as Category, Persona, Volume, and Severity. It appears as a
column in the pre-commitment table and as a named field on every card. The distribution
is auditable from field values without reading body text.

**Probe (C-11 structural guarantee):** In R1 prompts, Phase was declared in the table
and stamped on cards, but the field was treated as a layout decorator rather than a
first-class auditable field. The rubric credits Phase as first-class when it appears
alongside the standard 6 fields AND when the verification check reads from field
values, not body language. This variation makes Phase structurally equivalent to
Severity — it has a controlled vocabulary, it is locked in the pre-commitment table,
and it is checked in the post-body verification by field-value count, not prose scan.

**Hypothesis:** Elevating Phase to a named field with a controlled vocabulary
(Phase 1 | Phase 2 | Phase 3) produces auditable distribution at generation time. The
table check fires on Phase column values before any body is written, making C-11
compliance observable without navigating card bodies. Secondary effect: phase-severity
alignment (C-07) improves because the model sees Phase and Severity as co-declared
fields in the same row — violations are visible as table-level inconsistencies.

---

```
# listen-support: Predict First-90-Day Support Tickets

You are predicting support tickets for a feature that replaces an existing workflow.
You will write these tickets yourself — as the people who filed them.

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — PRIOR TOOL DECLARATION

Name the tool this feature replaces:

  PRIOR TOOL: [product name — real, named tool; not a generic description]

In 2-3 sentences: what does [PRIOR TOOL] do that users depend on? What expectations
does it create that will show up as support tickets in the first 90 days?

Transition curve:
  Phase 1 (Day 0-30):  [PRIOR TOOL] still available. Fallback exists. Severity floor: P2/P3.
  Phase 2 (Day 31-60): Partial migration. Some workflows moved; others still on [PRIOR TOOL].
  Phase 3 (Day 61-90): Fully committed. [PRIOR TOOL] gone for this workflow. Severity ceiling: P0/P1.

---

## STEP 2 — PERSONA ACTIVATION LIST

Before filling the table, list the personas who will file tickets.
At least 3 distinct personas from: Support | SRE | PM | UX | C-01 through C-12.

For each:
  Persona: [name]
  Transition friction: [one sentence — what they expected from [PRIOR TOOL] that
                        this feature does not deliver the same way]
  Peak phase: [Phase 1 | Phase 2 | Phase 3]

---

## STEP 3 — VOCABULARY PRE-COMMITMENT TABLE

Before writing any ticket body, fill in this table. Lock all field values here.
Bodies written in Step 5 must match this table exactly.

Phase is a required field — declared here, not inferred from body text.

Allowed values:
  Phase:    Phase 1 | Phase 2 | Phase 3
  Category: how-to | bug | feature-request | config | integration
  Persona:  Support | SRE | PM | UX | C-01..C-12
  Volume:   high | medium | low
  Severity: P0 | P1 | P2 | P3

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |

After completing the table, run the TABLE CHECK:

TABLE CHECK:
  Total rows: [N] (required: >= 7) — PASS / FAIL
  Distinct Category values: [N] (required: >= 3) — PASS / FAIL
  Distinct Persona values: [N] (required: >= 3) — PASS / FAIL
  Phase 1 rows: [N] (required: >= 2) — PASS / FAIL
  Phase 2 rows: [N] (required: >= 1) — PASS / FAIL
  Phase 3 rows: [N] (required: >= 1) — PASS / FAIL
  Phase 1 Severity values: [list] — all must be P2 or P3 — PASS / FAIL
  Phase 3 Severity values: [list] — all must be P0 or P1 — PASS / FAIL
  Overall: PASS / FAIL

If any check FAILS, revise the table before continuing. Do not proceed with a FAIL.

---

## STEP 4 — PERSONA ACTIVATION

For each row in the table, activate the persona before writing the body.

  T-NN ACTIVATION:
  I AM: [persona from table]
  MY SITUATION: [one sentence — what I am trying to accomplish today]
  MY FRUSTRATION: [one sentence — what broke, what was missing, what surprised me]
  MY PHASE STATE: [one sentence — am I still running [PRIOR TOOL] in parallel (Phase 1),
                   partly committed (Phase 2), or fully committed with no fallback (Phase 3)?]

Complete all activations before writing any body.

---

## STEP 5 — TICKET BODIES

For each ticket, write the body using the activation from Step 4 and the metadata
from Step 3. Do not change any field values from the table.

Ticket T-NN
Phase: [from table — Phase 1 | Phase 2 | Phase 3]
Category: [from table]
Persona: [from table]
Volume: [from table]
Severity: [from table]

Body:
[Write as me — first person throughout. No role titles in body text. Just I.
 At least one body must name [PRIOR TOOL] by its exact name from Step 1.
 2-5 sentences.]

---

## STEP 6 — POST-BODY VERIFICATION

After writing all bodies, confirm field values match Step 3 table:

  Phase field present on all cards: YES / NO
  Phase distribution:
    Phase 1: [N] (table committed: [N]) — MATCH / MISMATCH
    Phase 2: [N] (table committed: [N]) — MATCH / MISMATCH
    Phase 3: [N] (table committed: [N]) — MATCH / MISMATCH
  [PRIOR TOOL] named in at least one body: [T-NN list] — PASS / FAIL
  All bodies written in first person (no role titles in body text): PASS / FAIL
  All body field values match Step 3 table: PASS / FAIL

If any FAIL, correct before continuing.

---

## STEP 7 — GAP ANALYSIS

Three sections required. Each entry must name a specific artifact.

### Documentation Gaps
[At least one entry. Name the specific doc, section, or reference article missing.]

### Design Gaps
[At least one entry. Name the specific UI element, config field, or workflow step
that needs to change.]

### Operational Gaps
[At least one entry. Name the specific runbook, alert rule, monitoring endpoint,
or deployment checklist item that is absent.]
```

---

## V-02: Single-Axis — Fallback-Grounded Severity Rationale (C-12)

**Axis:** Inertia framing — severity is mechanically derived from fallback availability,
not asserted as a judgment. Every ticket card requires a Fallback Rationale: field that
states whether the prior tool is available as fallback and names the resulting severity.
The inference is shown in the output, not implied.

**Probe (C-12 mechanical vs asserted):** The common failure: a prompt says "Phase 3
tickets are P0/P1" and the model follows the rule but produces severity assignments
that look correct without being traceable. A scorer cannot tell whether severity was
assigned from the adoption-position rule or from a problem-type heuristic (e.g.,
"auth failures are always P1"). This variation requires the rationale to appear as a
named field on every card — the model must state "I can still fall back to [PRIOR TOOL]"
or "I can no longer use [PRIOR TOOL] for this workflow" before the severity value.

**Hypothesis:** When fallback availability is a required field output, the severity
assignment becomes auditable regardless of whether the body text mentions the prior
tool. A scorer can verify C-12 compliance by reading the Fallback Rationale: field
alone — no body parsing required. The secondary effect: the prior tool (from Step 1)
appears in at least as many Fallback Rationale fields as C-09 requires in body text,
making C-09 compliance a near-automatic byproduct of C-12 compliance.

---

```
# listen-support: Predict First-90-Day Support Tickets

You are predicting support tickets for a feature that replaces an existing workflow.
You will write these tickets yourself — as the people who filed them.

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — PRIOR TOOL DECLARATION

Name the tool this feature replaces:

  PRIOR TOOL: [product name — real, named tool; not a generic description]

In 2-3 sentences: what does [PRIOR TOOL] do that users depend on? What expectations
does it create that will show up as support tickets in the first 90 days?

Transition curve:
  Day 0-30:  [PRIOR TOOL] still available. Fallback exists.
  Day 31-60: Partial migration. Some workflows moved; others still on [PRIOR TOOL].
  Day 61-90: Fully committed. [PRIOR TOOL] gone for this workflow.

---

## STEP 1B — SEVERITY INFERENCE RULE (STATED)

Copy this rule exactly. You will apply it to every severity assignment in this output.

  INFERENCE RULE: Severity is a property of adoption position, not problem type.
  - Fallback available ([PRIOR TOOL] still running): P2 or P3.
  - Fallback gone ([PRIOR TOOL] no longer an option for this workflow): P0 or P1.

State the rule in your own words: [paraphrase in one sentence]

---

## STEP 2 — PERSONA ACTIVATION LIST

At least 3 distinct personas from: Support | SRE | PM | UX | C-01 through C-12.

For each:
  Persona: [name]
  Transition friction: [one sentence]
  Peak window: [Day 0-30 | Day 31-60 | Day 61-90]

---

## STEP 3 — VOCABULARY PRE-COMMITMENT TABLE

Before writing any ticket body, fill in this table. Lock all field values here.

Allowed values:
  Category: how-to | bug | feature-request | config | integration
  Persona:  Support | SRE | PM | UX | C-01..C-12
  Volume:   high | medium | low
  Severity: P0 | P1 | P2 | P3
  Phase:    Phase 1 (Day 0-30) | Phase 2 (Day 31-60) | Phase 3 (Day 61-90)

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |

TABLE CHECK:
  Total rows: [N] (required: >= 7) — PASS / FAIL
  Distinct Category values: [N] (required: >= 3) — PASS / FAIL
  Distinct Persona values: [N] (required: >= 3) — PASS / FAIL
  Phase 1 rows: [N] (required: >= 2) — PASS / FAIL
  Phase 3 rows: [N] (required: >= 1) — PASS / FAIL
  Phase 1 Severity values: [list] — all must be P2 or P3 — PASS / FAIL
  Phase 3 Severity values: [list] — all must be P0 or P1 — PASS / FAIL
  Overall: PASS / FAIL

If any check FAILS, revise the table before continuing.

---

## STEP 4 — PERSONA ACTIVATION

For each ticket row in the table, activate the persona.

  T-NN ACTIVATION:
  I AM: [persona from table]
  MY SITUATION: [one sentence]
  MY FRUSTRATION: [one sentence]
  MY TRANSITION STATE: [one sentence — am I still running [PRIOR TOOL] in parallel,
                        or am I fully committed to this feature?]

Complete all activations before writing any body.

---

## STEP 5 — TICKET BODIES

For each ticket, write using the activation from Step 4 and the metadata from Step 3.
Do not change any field values from the table.

Every ticket requires a Fallback Rationale: field. This field states whether [PRIOR TOOL]
is available as fallback and derives the severity from that position. Complete Fallback
Rationale: before writing the body for each ticket.

Ticket T-NN
Category: [from table]
Persona: [from table]
Volume: [from table]
Fallback Rationale: [one sentence — "I can still fall back to [PRIOR TOOL]" OR
                     "I can no longer use [PRIOR TOOL] for this workflow"]
                    → Severity: [P0 | P1 | P2 | P3] (must match table)

Body:
[Write as me — first person throughout. No role titles in body text. Just I.
 At least one body must name [PRIOR TOOL] by its exact name from Step 1.
 2-5 sentences.]

---

## STEP 6 — POST-BODY VERIFICATION

After writing all bodies:

  Fallback Rationale: field present on all cards: YES / NO
  Fallback Rationale: values consistent with phase-severity table:
    Phase 1 cards (fallback available → P2/P3): [T-NN list] — PASS / FAIL
    Phase 3 cards (no fallback → P0/P1): [T-NN list] — PASS / FAIL
  [PRIOR TOOL] name appears in Fallback Rationale: fields: [N] cards — PASS / FAIL
  All bodies written in first person: PASS / FAIL
  All body field values match Step 3 table: PASS / FAIL

If any FAIL, correct before continuing.

---

## STEP 7 — GAP ANALYSIS

Three sections required. Each entry must name a specific artifact.

### Documentation Gaps
[At least one entry. Name the specific doc, section, or reference article missing.]

### Design Gaps
[At least one entry. Name the specific UI element, config field, or workflow step
that needs to change.]

### Operational Gaps
[At least one entry. Name the specific runbook, alert rule, monitoring endpoint,
or deployment checklist item that is absent.]
```

---

## V-03: Single-Axis — Mid-Output Verification Block (C-13)

**Axis:** Lifecycle emphasis — a mandatory PASS/FAIL self-audit block fires between
ticket body generation and gap analysis. The block tabulates phase counts and role
diversity from the just-generated ticket set and is visible in the output. Gap analysis
does not begin until the verification block runs.

**Probe (C-13 structural lock):** Without a mid-output gate, a model may produce a
skewed phase distribution (all Phase 1) or thin role coverage (all customer personas)
and proceed directly to gap analysis — the gap analysis then reflects a biased sample.
The verification block fires at the moment when correction is still cheap: bodies
already exist, but the analysis phase has not started. A FAIL forces correction before
gap analysis, making the structural compliance visible to a reviewer without requiring
them to re-read the ticket set.

**Hypothesis:** The mid-output verification block is the structural mechanism that
locks C-06 (phase distribution) and C-08 (role diversity) compliance rather than
leaving them as soft constraints. The block must appear in the output — not in a
system comment or trailing note — to satisfy C-13. The tabulation format (counts per
phase, counts per role) is what makes the compliance observable. This variation
isolates C-13 without adding Phase field (C-11) or Fallback Rationale (C-12), to
test whether the verification block alone is sufficient to produce passing C-06/C-08
without those structural aids.

---

```
# listen-support: Predict First-90-Day Support Tickets

You are predicting support tickets for a feature that replaces an existing workflow.
You will write these tickets yourself — as the people who filed them.

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — PRIOR TOOL DECLARATION

Name the tool this feature replaces:

  PRIOR TOOL: [product name — real, named tool; not a generic description]

In 2-3 sentences: what does [PRIOR TOOL] do that users depend on? What expectations
does it create that will show up as support tickets in the first 90 days?

Transition curve:
  Day 0-30:  [PRIOR TOOL] still available. Fallback exists. Severity floor: P2/P3.
  Day 31-60: Partial migration. Some workflows moved; others still on [PRIOR TOOL].
  Day 61-90: Fully committed. [PRIOR TOOL] gone for this workflow. Severity ceiling: P0/P1.

---

## STEP 2 — PERSONA ACTIVATION LIST

At least 3 distinct personas from: Support | SRE | PM | UX | C-01 through C-12.

For each:
  Persona: [name]
  Transition friction: [one sentence]
  Peak window: [Day 0-30 | Day 31-60 | Day 61-90]

---

## STEP 3 — VOCABULARY PRE-COMMITMENT TABLE

Before writing any ticket body, fill in this table. Lock all field values here.

Allowed values:
  Category: how-to | bug | feature-request | config | integration
  Persona:  Support | SRE | PM | UX | C-01..C-12
  Volume:   high | medium | low
  Severity: P0 | P1 | P2 | P3
  Phase:    Phase 1 (Day 0-30) | Phase 2 (Day 31-60) | Phase 3 (Day 61-90)

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |

TABLE CHECK:
  Total rows: [N] (required: >= 7) — PASS / FAIL
  Distinct Category values: [N] (required: >= 3) — PASS / FAIL
  Distinct Persona values: [N] (required: >= 3) — PASS / FAIL
  Phase 1 rows: [N] (required: >= 2) — PASS / FAIL
  Phase 3 rows: [N] (required: >= 1) — PASS / FAIL
  Phase 1 Severity values: [list] — all must be P2 or P3 — PASS / FAIL
  Phase 3 Severity values: [list] — all must be P0 or P1 — PASS / FAIL
  Overall: PASS / FAIL

If any check FAILS, revise the table before continuing.

---

## STEP 4 — PERSONA ACTIVATION

For each ticket row in the table, activate the persona.

  T-NN ACTIVATION:
  I AM: [persona from table]
  MY SITUATION: [one sentence]
  MY FRUSTRATION: [one sentence]
  MY TRANSITION STATE: [one sentence — am I still running [PRIOR TOOL] in parallel,
                        or am I fully committed to this feature?]

Complete all activations before writing any body.

---

## STEP 5 — TICKET BODIES

For each ticket, write using the activation from Step 4 and the metadata from Step 3.
Do not change any field values from the table.

Ticket T-NN
Title: [descriptive subject line]
Category: [from table]
Persona: [from table]
Volume: [from table]
Severity: [from table]

Body:
[Write as me — first person throughout. No role titles in body text. Just I.
 At least one body must name [PRIOR TOOL] by its exact name from Step 1.
 2-5 sentences.]

---

## STEP 5B — MID-OUTPUT VERIFICATION BLOCK

Run this verification block now. Do not begin gap analysis until this block is complete
and all checks pass.

VERIFICATION BLOCK — PHASE AND ROLE AUDIT

Phase distribution (count from card bodies above):
  Phase 1 (Day 0-30): [N] tickets — required: >= 2 — PASS / FAIL
  Phase 2 (Day 31-60): [N] tickets — required: >= 1 — PASS / FAIL
  Phase 3 (Day 61-90): [N] tickets — required: >= 1 — PASS / FAIL
  Total: [N] tickets

Phase-severity compliance scan:
  Phase 1 tickets — Severity values: [list] — all P2 or P3: PASS / FAIL
  Phase 3 tickets — Severity values: [list] — all P0 or P1: PASS / FAIL

Role diversity (count from Persona field of card bodies above):
  Distinct Persona values used: [list] — count: [N] — required: >= 3 — PASS / FAIL

[PRIOR TOOL] coverage:
  Bodies naming [PRIOR TOOL] by exact name: [T-NN list] — count: [N] — required: >= 1 — PASS / FAIL

OVERALL VERIFICATION: PASS / FAIL

If any check FAILS: correct the affected ticket(s) before proceeding to gap analysis.
Do not begin gap analysis with a FAIL in this block.

---

## STEP 6 — GAP ANALYSIS

Three sections required. Each entry must name a specific artifact.

### Documentation Gaps
[At least one entry. Name the specific doc, section, or reference article missing.]

### Design Gaps
[At least one entry. Name the specific UI element, config field, or workflow step
that needs to change.]

### Operational Gaps
[At least one entry. Name the specific runbook, alert rule, monitoring endpoint,
or deployment checklist item that is absent.]
```

---

## V-04: Combined — Phase as First-Class Field + Fallback-Grounded Severity (C-11 + C-12)

**Axes combined:** Phase as a declared metadata field (V-01) + fallback-grounded severity
rationale as a required card field (V-02).

**Combination hypothesis:** Phase field makes the distribution auditable from table
values; fallback severity makes the phase-severity relationship mechanical rather than
asserted. Together, a Phase 3 ticket with severity P3 is a double violation — visible
as a Phase column / Severity column mismatch in the table AND as a contradicted
Fallback Rationale: field in the body. Without either mechanism alone, one violation
might hide behind the other. With both, the table fires on the Phase/Severity pair
before body generation, and the Fallback Rationale: field fires a second check during
body generation. The combination tests whether C-11 and C-12 are mutually reinforcing
rather than redundant.

**Risk:** Adding both Phase (as a named field) and Fallback Rationale (as a required
field) to the card format increases per-ticket field count from 5 to 7. The additional
fields may flatten card bodies — the model spends cognitive budget on structured fields
rather than authentic voice. The variation checks whether essential criteria C-01
through C-05 are maintained under the additional structural load.

---

```
# listen-support: Predict First-90-Day Support Tickets

You are predicting support tickets for a feature that replaces an existing workflow.
You will write these tickets yourself — as the people who filed them.

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — PRIOR TOOL DECLARATION

Name the tool this feature replaces:

  PRIOR TOOL: [product name — real, named tool; not a generic description]

In 2-3 sentences: what does [PRIOR TOOL] do that users depend on? What expectations
does it create that will show up as support tickets in the first 90 days?

Transition curve:
  Phase 1 (Day 0-30):  [PRIOR TOOL] still available. Fallback exists.
  Phase 2 (Day 31-60): Partial migration. Some workflows moved; others still on [PRIOR TOOL].
  Phase 3 (Day 61-90): Fully committed. [PRIOR TOOL] gone for this workflow.

---

## STEP 1B — SEVERITY INFERENCE RULE (STATED)

Copy this rule. Apply it to every severity assignment in this output.

  INFERENCE RULE: Severity is a property of adoption position, not problem type.
  - Fallback available ([PRIOR TOOL] still running in parallel): P2 or P3.
  - Fallback gone ([PRIOR TOOL] no longer an option for this workflow): P0 or P1.

State the rule in your own words: [paraphrase in one sentence]

---

## STEP 2 — PERSONA ACTIVATION LIST

At least 3 distinct personas from: Support | SRE | PM | UX | C-01 through C-12.

For each:
  Persona: [name]
  Transition friction: [one sentence]
  Peak phase: [Phase 1 | Phase 2 | Phase 3]

---

## STEP 3 — VOCABULARY PRE-COMMITMENT TABLE

Before writing any ticket body, fill in this table. Lock all field values here.
Phase is a required field — declared here, not inferred from body text.

Allowed values:
  Phase:    Phase 1 | Phase 2 | Phase 3
  Category: how-to | bug | feature-request | config | integration
  Persona:  Support | SRE | PM | UX | C-01..C-12
  Volume:   high | medium | low
  Severity: P0 | P1 | P2 | P3

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |

TABLE CHECK:
  Total rows: [N] (required: >= 7) — PASS / FAIL
  Distinct Category values: [N] (required: >= 3) — PASS / FAIL
  Distinct Persona values: [N] (required: >= 3) — PASS / FAIL
  Phase 1 rows: [N] (required: >= 2) — PASS / FAIL
  Phase 2 rows: [N] (required: >= 1) — PASS / FAIL
  Phase 3 rows: [N] (required: >= 1) — PASS / FAIL
  Phase 1 Severity values: [list] — all must be P2 or P3 — PASS / FAIL
  Phase 3 Severity values: [list] — all must be P0 or P1 — PASS / FAIL
  Overall: PASS / FAIL

If any check FAILS, revise the table before continuing.

---

## STEP 4 — PERSONA ACTIVATION

For each ticket row in the table, activate the persona.

  T-NN ACTIVATION:
  I AM: [persona from table]
  MY SITUATION: [one sentence]
  MY FRUSTRATION: [one sentence]
  MY PHASE STATE: [one sentence — am I still running [PRIOR TOOL] in parallel (Phase 1),
                   partly committed (Phase 2), or fully committed with no fallback (Phase 3)?]

Complete all activations before writing any body.

---

## STEP 5 — TICKET BODIES

For each ticket, write using the activation from Step 4 and the metadata from Step 3.
Do not change any field values from the table.

Every ticket requires a Fallback Rationale: field. State whether [PRIOR TOOL] is
available as fallback and derive the severity from that position. The Fallback
Rationale: field must use the exact product name declared in Step 1.

Ticket T-NN
Phase: [from table — Phase 1 | Phase 2 | Phase 3]
Category: [from table]
Persona: [from table]
Volume: [from table]
Fallback Rationale: [one sentence — "I can still fall back to [PRIOR TOOL] for this
                     workflow" OR "I can no longer use [PRIOR TOOL] for this workflow"]
                    → Severity: [P0 | P1 | P2 | P3] (must match table)

Body:
[Write as me — first person throughout. No role titles in body text. Just I.
 At least one body must name [PRIOR TOOL] by its exact name from Step 1.
 2-5 sentences.]

---

## STEP 6 — POST-BODY VERIFICATION

After writing all bodies:

  Phase field present on all cards: YES / NO
  Phase distribution from Phase fields:
    Phase 1: [N] (table committed: [N]) — MATCH / MISMATCH
    Phase 2: [N] (table committed: [N]) — MATCH / MISMATCH
    Phase 3: [N] (table committed: [N]) — MATCH / MISMATCH
  Fallback Rationale: field present on all cards: YES / NO
  Fallback Rationale: values consistent with phase-severity:
    Phase 1 cards (fallback available → P2/P3): [T-NN list] — PASS / FAIL
    Phase 3 cards (no fallback → P0/P1): [T-NN list] — PASS / FAIL
  [PRIOR TOOL] name in Fallback Rationale: fields: [N] cards — PASS / FAIL
  All bodies written in first person: PASS / FAIL
  All body field values match Step 3 table: PASS / FAIL

If any FAIL, correct before continuing.

---

## STEP 7 — GAP ANALYSIS

Three sections required. Each entry must name a specific artifact.

### Documentation Gaps
[At least one entry. Name the specific doc, section, or reference article missing.]

### Design Gaps
[At least one entry. Name the specific UI element, config field, or workflow step
that needs to change.]

### Operational Gaps
[At least one entry. Name the specific runbook, alert rule, monitoring endpoint,
or deployment checklist item that is absent.]
```

---

## V-05: Full Synthesis — Phase Field + Fallback Severity + Mid-Output Verification (C-11 + C-12 + C-13)

**Axes combined:** Phase as declared metadata field (V-01) + fallback-grounded severity
rationale as required card field (V-02) + mid-output verification block before gap
analysis (V-03).

**Synthesis hypothesis:** The three mechanisms are mutually reinforcing without being
redundant. Phase as a field enables the verification block to count distribution from
field values — no body scan required (C-11 enables C-13 tabulation). Fallback Rationale
enables the verification block to audit severity-phase alignment mechanically — the
inference rule fires per-ticket, not per-phase (C-12 enables C-13 compliance check).
The verification block makes both compliance checks observable in the output and forces
correction before gap analysis contaminates its findings (C-13 locks C-11 + C-12 at
the right moment). The synthesis tests whether all three stack without any of the five
essential criteria degrading — specifically whether the increased card field count (7
fields + body) and the verification interruption produce flatter bodies and thinner
gap analysis.

**C-11 + C-12 + C-13 combined probe:** Does a prompt that pre-commits Phase as a field,
requires fallback rationale per card, and fires a mid-output audit block produce outputs
that pass all three new v2 criteria simultaneously, while maintaining C-01 through C-10
compliance inherited from R1 V-05?

---

```
# listen-support: Predict First-90-Day Support Tickets

You are predicting support tickets for a feature that replaces an existing workflow.
You will write these tickets yourself — as the people who filed them.

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — PRIOR TOOL DECLARATION

Name the tool this feature replaces:

  PRIOR TOOL: [product name — real, named tool; not a generic description]

In 2-3 sentences: what does [PRIOR TOOL] do that users depend on? What expectations
does it create that will show up as support tickets in the first 90 days?

Transition curve:
  Phase 1 (Day 0-30):  [PRIOR TOOL] still available. Fallback exists.
  Phase 2 (Day 31-60): Partial migration. Some workflows moved; others still on [PRIOR TOOL].
  Phase 3 (Day 61-90): Fully committed. [PRIOR TOOL] gone for this workflow.

---

## STEP 1B — SEVERITY INFERENCE RULE (STATED)

Copy this rule. Apply it to every severity assignment in this output.

  INFERENCE RULE: Severity is a property of adoption position, not problem type.
  - Fallback available ([PRIOR TOOL] still running in parallel): P2 or P3.
  - Fallback gone ([PRIOR TOOL] no longer an option for this workflow): P0 or P1.

State the rule in your own words: [paraphrase in one sentence]

---

## STEP 2 — PERSONA ACTIVATION LIST

At least 3 distinct personas from: Support | SRE | PM | UX | C-01 through C-12.

For each:
  Persona: [name]
  Transition friction: [one sentence]
  Peak phase: [Phase 1 | Phase 2 | Phase 3]

---

## STEP 3 — VOCABULARY PRE-COMMITMENT TABLE

Before writing any ticket body, fill in this table. Lock all field values here.
Phase is a required field — declared here, not inferred from body text.

Allowed values:
  Phase:    Phase 1 | Phase 2 | Phase 3
  Category: how-to | bug | feature-request | config | integration
  Persona:  Support | SRE | PM | UX | C-01..C-12
  Volume:   high | medium | low
  Severity: P0 | P1 | P2 | P3

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |

TABLE CHECK:
  Total rows: [N] (required: >= 7) — PASS / FAIL
  Distinct Category values: [N] (required: >= 3) — PASS / FAIL
  Distinct Persona values: [N] (required: >= 3) — PASS / FAIL
  Phase 1 rows: [N] (required: >= 2) — PASS / FAIL
  Phase 2 rows: [N] (required: >= 1) — PASS / FAIL
  Phase 3 rows: [N] (required: >= 1) — PASS / FAIL
  Phase 1 Severity values: [list] — all must be P2 or P3 — PASS / FAIL
  Phase 3 Severity values: [list] — all must be P0 or P1 — PASS / FAIL
  Overall: PASS / FAIL

If any check FAILS, revise the table before continuing. Do not proceed with a FAIL.

---

## STEP 4 — PERSONA ACTIVATION

For each ticket row in the table, activate the persona.

  T-NN ACTIVATION:
  I AM: [persona from table]
  MY SITUATION: [one sentence]
  MY FRUSTRATION: [one sentence]
  MY PHASE STATE: [one sentence — am I still running [PRIOR TOOL] in parallel (Phase 1),
                   partly committed (Phase 2), or fully committed with no fallback (Phase 3)?]

Complete all activations before writing any body.

---

## STEP 5 — TICKET BODIES

For each ticket, write using the activation from Step 4 and the metadata from Step 3.
Do not change any field values from the table.

Every ticket requires a Fallback Rationale: field. State whether [PRIOR TOOL] is
available as fallback at this adoption position, then derive the severity. The
Fallback Rationale: field must use the exact product name declared in Step 1.
Write the Fallback Rationale: field before the body for each ticket.

Ticket T-NN
Phase: [from table — Phase 1 | Phase 2 | Phase 3]
Category: [from table]
Persona: [from table]
Volume: [from table]
Fallback Rationale: [one sentence — "I can still fall back to [PRIOR TOOL] for this
                     workflow" OR "I can no longer use [PRIOR TOOL] for this workflow"]
                    → Severity: [P0 | P1 | P2 | P3] (must match table)

Body:
[Write as me — first person throughout. No role titles in body text. Just I.
 At least one body must name [PRIOR TOOL] by its exact name from Step 1.
 2-5 sentences.]

---

## STEP 5B — MID-OUTPUT VERIFICATION BLOCK

Run this verification block now. Do not begin gap analysis until this block is complete
and all checks pass. This block reads from field values declared above — not from
body text.

VERIFICATION BLOCK — PHASE, SEVERITY, AND ROLE AUDIT

Phase distribution (from Phase field values):
  Phase 1: [N] tickets — required: >= 2 — PASS / FAIL
  Phase 2: [N] tickets — required: >= 1 — PASS / FAIL
  Phase 3: [N] tickets — required: >= 1 — PASS / FAIL
  Total: [N] tickets

Severity-phase compliance (from Phase field + Severity field pairs):
  Phase 1 Severity values: [list] — all P2 or P3: PASS / FAIL
  Phase 3 Severity values: [list] — all P0 or P1: PASS / FAIL

Fallback Rationale alignment:
  Phase 1 Fallback Rationale: fields state fallback available: [T-NN list] — PASS / FAIL
  Phase 3 Fallback Rationale: fields state no fallback: [T-NN list] — PASS / FAIL

Role diversity (from Persona field values):
  Distinct Persona values: [list] — count: [N] — required: >= 3 — PASS / FAIL

[PRIOR TOOL] coverage:
  Fallback Rationale: fields naming [PRIOR TOOL] by exact name: [N] cards — PASS / FAIL
  Bodies naming [PRIOR TOOL] by exact name: [T-NN list] — required: >= 1 — PASS / FAIL

OVERALL VERIFICATION: PASS / FAIL

If any check FAILS: correct the affected ticket(s) before proceeding.
Do not begin gap analysis with a FAIL in this block.

---

## STEP 6 — GAP ANALYSIS

Three sections required. Each entry must name a specific artifact.

### Documentation Gaps
[At least one entry. Name the specific doc, section, or reference article missing.]

### Design Gaps
[At least one entry. Name the specific UI element, config field, or workflow step
that needs to change.]

### Operational Gaps
[At least one entry. Name the specific runbook, alert rule, monitoring endpoint,
or deployment checklist item that is absent.]
```
