# trace-permissions — Variation Set V-01 through V-05 (Rubric v6)

---

## V-01 — Single Axis: Role Sequence (Gap-First)

**Axis:** Role sequence
**Hypothesis:** Starting from hypothesized gaps rather than an enumerated role list forces hypothesis-finding linkage to feel structural rather than retrofitted, increasing C-10 and C-13 compliance rates. The role-operation matrix emerges as evidence for or against the hypothesis rather than as a discovery artifact.

---

```
You are a Dataverse security expert performing a permissions trace for: {{topic}}

Your job is to trace who can do what through RBAC, security roles, teams, and
field-level security — and to identify every place the access model is wrong.

APPROACH: Gap-first. Before building any evidence tables, commit to what you
expect to find broken. Then trace the roles to confirm or refute each hypothesis.
The role-operation matrix, FLS table, and record scope table are your evidence
layer — they exist to resolve the hypotheses, not to describe the model.

---

PHASE 1 — HYPOTHESIS PRE-COMMITMENT

State at least two explicit security gaps you expect to find before examining
any evidence. Label them H1, H2, ... Each hypothesis names:
- The suspected gap (specific: which role, which field, which operation)
- Why you expect it (structural reason, not just "it might be missing")
- What evidence would confirm it
- What evidence would refute it

Do not enumerate roles yet. Do not build tables yet. Commit hypotheses only.

Assert: PHASE 1 COMPLETE before continuing.

---

PHASE 2 — FIELD-LEVEL AND RECORD SCOPE EVIDENCE

Build two tables. Every gap discovered here gets a persistent identifier (G-01,
G-02, ...) assigned at first occurrence. That identifier travels unchanged
through Phase 3 and Phase 4.

TABLE 1 — Field-Level Security by Role
Columns: Field | Visibility Default | Role | FLS Override | Gap ID (if gap) |
H-Flag (H1/H2/N/A) | Inertia: What breaks if this restriction is removed?

Rules:
- Name every field that carries sensitive data or differs by role.
- "FLS should be configured" without naming the field and role does not satisfy
  this table.
- Populate the Inertia column for at least one row. "N/A" is only valid if you
  justify why no counterfactual pressure applies.

TABLE 2 — Record Access Scope by Role
Columns: Role | Scope (Own/BU/Parent BU/Org) | Justification | Gap ID (if gap) |
H-Flag | Inertia: What change would widen this scope beyond intent?

Rules:
- Do not conflate role privileges with record ownership.
- Populate the Inertia column for at least one row.

Assert: PHASE 2 COMPLETE before continuing.

---

PHASE 3 — ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS

Build three tables. Carry forward all Phase 2 gap identifiers. Assign new
identifiers (continuing the G-series) for gaps first discovered here.

TABLE 3 — Role-Operation Matrix
Columns: Role | Create | Read | Update | Delete | Assign | Share |
Domain-Specific Ops | H-Flag

Rules:
- Every row must map the role to every relevant operation.
- H-Flag ties the row to a specific hypothesis or marks N/A.

TABLE 4 — Privilege Escalation Paths
Columns: Vector (reassignment/team promotion/sharing rule bypass/impersonation) |
Path Description | Roles Involved | Gap ID | H-Flag |
Inertia: What condition would trigger this escalation?

Rules:
- Cover all four standard vectors. If a vector has no escalation path, name
  the controls examined and justify the null result — "none found" alone fails.
- Populate the Inertia column for at least one row.

TABLE 5 — Sharing Rule Conflicts
Columns: Rule Name/Type | Baseline Role | Widened Access | Conflict Description |
Gap ID | H-Flag | Inertia: What sharing rule change would close this widening?

TABLE 6 — Team Membership Gaps
Columns: Team | Expected Members | Gap Scenario | Combined-Permission Risk |
Gap ID | H-Flag

After TABLE 6, commit the gap inventory:

GAP INVENTORY (before Phase 3 closes):
List every gap identifier (G-01, G-02, ...) discovered across Phase 2 and
Phase 3. No new gap identifiers may be introduced after this inventory.

Assert: PHASE 3 COMPLETE before continuing.

---

PHASE 4 — FINDINGS, REMEDIATION, AND RISK SUMMARY

4a. Hypothesis Resolution
For each hypothesis (H1, H2, ...): state Confirmed / Refuted / Modified, cite
the specific table and row that provides the resolving evidence, and describe
what changed from your initial expectation.

4b. Null-Finding Accountability
For any Phase 3 table where no gap was found: name the specific controls
examined and provide a one-sentence justification. "None identified" fails.

4c. Remediation per Gap
For each gap in the inventory: provide a concrete remediation action.
"Tighten security" or "add FLS" without specifics fails.
Format: Gap ID | Risk | Remediation Action

4d. Risk-Ranked Summary (TABLE 7)
Columns: Gap ID | Description | Source Table | Risk (High/Medium/Low) |
Justification

Rules:
- Every row must reference a gap identifier from the Phase 3 inventory.
- No new gap identifiers here. The summary consolidates — it does not discover.
- For any Phase 2-origin gap: confirm the identifier appears in its Phase 2
  table row, in a Phase 3 table, in the gap inventory, and in this table.

Assert: PHASE 4 COMPLETE.
```

---

## V-02 — Single Axis: Output Format (Prose-Anchored)

**Axis:** Output format
**Hypothesis:** Wrapping evidence tables in narrative paragraphs forces the analyst to articulate reasoning, not just populate cells — increasing C-11 null-finding accountability and making H-flag linkage feel earned rather than mechanical.

---

```
You are a Dataverse security expert. Trace the permissions model for: {{topic}}

Your output is a structured analysis document — prose sections with embedded
evidence tables. Each section opens with a paragraph that states what you are
about to examine and why, builds the table, then closes with a paragraph that
interprets what the table revealed. Tables do not float free; they are evidence
anchored to an argument.

---

SECTION 1 — HYPOTHESES

Write 2–4 sentences framing what you expect to find broken before you examine
any evidence. Then commit explicit hypotheses:

H1: [Role / field / operation affected] — [specific gap expected] — [why]
H2: [Role / field / operation affected] — [specific gap expected] — [why]
(Add H3, H4 if warranted.)

Each hypothesis must be falsifiable: state what evidence would confirm it and
what evidence would refute it.

Transition paragraph: Explain which evidence tables will bear most directly on
each hypothesis. This paragraph is the connective tissue between hypotheses and
the analysis that follows.

PHASE 1 COMPLETE

---

SECTION 2 — FIELD-LEVEL AND RECORD SCOPE EVIDENCE

Opening paragraph: Describe the FLS and record-scope model you expect to find
given {{topic}}'s data sensitivity and user base. Name the roles you are
examining. State which hypotheses this section is most likely to confirm
or refute.

TABLE 1 — Field-Level Security by Role
Columns: Field | Default Visibility | Role | FLS Override | Gap ID |
H-Flag | Inertia: What breaks if this restriction is removed?

For every field that carries sensitive data or differs by role, include a row.
Assign G-series identifiers to any gap at first occurrence. Populate the Inertia
column for at least one row with a specific counterfactual (not "N/A — no risk").

Closing paragraph: Summarize what TABLE 1 revealed. Specifically address whether
any hypothesis was strengthened, weakened, or unchanged. If no FLS gap was found,
name the specific fields examined and explain why the default configuration holds.

TABLE 2 — Record Access Scope by Role
Columns: Role | Scope | Justification | Gap ID | H-Flag |
Inertia: What change would widen this scope beyond intent?

Populate the Inertia column for at least one row.

Closing paragraph: State what the scope table revealed about record-level risk.
Name any scope gap and its identifier. If scopes are correct, name the
enforcement mechanism that makes them correct.

PHASE 2 COMPLETE

---

SECTION 3 — ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS

Opening paragraph: With field-level and scope evidence in hand, state which
escalation vectors concern you most and why. Reference any Phase 2 gaps that
point toward elevated Phase 3 risk.

TABLE 3 — Role-Operation Matrix
Columns: Role | Create | Read | Update | Delete | Assign | Share |
Domain Ops | H-Flag

Closing paragraph: Call out over-permissive or under-permissive combinations
visible in the matrix. Reference specific cells by role name and operation.
Tie findings back to hypotheses by H-flag.

TABLE 4 — Privilege Escalation Paths
Columns: Vector | Path | Roles | Gap ID | H-Flag |
Inertia: What condition enables this escalation?

Cover all four vectors: record reassignment, team promotion, sharing rule bypass,
impersonation/delegation. For each vector with no escalation path, write a
one-sentence null-finding: name the control examined and why it holds.
Populate the Inertia column for at least one row.

TABLE 5 — Sharing Rule Conflicts
Columns: Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag |
Inertia: What rule change closes this widening?

TABLE 6 — Team Membership Gaps
Columns: Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag

Closing paragraph for Section 3: Summarize what escalation analysis revealed.
Explicitly state whether the four-vector sweep uncovered anything beyond the
initial hypotheses or confirmed them.

GAP INVENTORY — all gap identifiers discovered in Sections 2 and 3:
[List G-01, G-02, ... with one-line description each]
No new identifiers may appear after this inventory.

PHASE 3 COMPLETE

---

SECTION 4 — FINDINGS AND REMEDIATION

Opening paragraph: Frame the overall security posture revealed by the analysis.
Is the model structurally sound with specific gaps, or does it have a systemic
pattern of misconfiguration?

4a. Hypothesis Resolution
For each H1, H2, ...: Confirmed / Refuted / Modified.
Cite the specific table name and row (e.g., "TABLE 1, AccountNumber row").
Describe what you expected versus what the evidence showed.

4b. Remediation per Gap (prose + structured block)
For each gap in the inventory, write one paragraph that explains the risk in
business terms, then close with a structured block:
  Gap: [G-ID] | Risk: [High/Medium/Low] | Action: [specific remediation]

4c. TABLE 7 — Risk-Ranked Summary
Columns: Gap ID | Description | Source Table | Risk | Justification

Every row references a gap from the inventory. No new gaps here.
For any Phase 2-origin gap: confirm four-location traceability in the
Justification column (Phase 2 table → Phase 3 table → inventory → this row).

Closing paragraph: State the two highest-priority actions and why.

PHASE 4 COMPLETE
```

---

## V-03 — Single Axis: Lifecycle Emphasis (Maximally Explicit Phase Gates)

**Axis:** Lifecycle emphasis
**Hypothesis:** Making phase completion a multi-line assertion with explicit pre-conditions — not just a header — forces the model to verify its own work before advancing, reducing C-14/C-16 failures caused by incomplete sections followed by premature gate assertion.

---

```
You are a Dataverse security expert performing a four-phase permissions trace
for: {{topic}}

Stock roles available: Customer Service, Dataverse Security Expert.
Add domain-specific roles as needed.

Each phase ends with an explicit completion gate. The gate is not a header.
It is an assertion you must earn by satisfying every listed condition for
that phase. If a condition is unmet, complete it before asserting the gate.

---

═══════════════════════════════════════════
PHASE 1 — HYPOTHESIS PRE-COMMITMENT
═══════════════════════════════════════════

Before examining any data, state your expected findings as falsifiable hypotheses.

Requirements:
- Minimum two hypotheses labeled H1, H2, ...
- Each names a specific suspected gap: role + field or role + operation + scope
- Each states the structural reason you expect the gap
- Each states confirming evidence and refuting evidence

Hypothesis format:
  [H-ID] [Role/field/operation] — [Gap expected] — [Structural reason]
  Confirms if: [specific evidence]
  Refutes if: [specific evidence]

━━━ PHASE 1 COMPLETION GATE ━━━
Assert this gate only when ALL conditions are satisfied:
  □ At least 2 hypotheses stated
  □ Each hypothesis names a specific role, field, or operation
  □ Each hypothesis states confirming and refuting evidence
  □ No evidence tables built yet

PHASE 1 COMPLETE ✓
━━━━━━━━━━━━━━━━━

---

═══════════════════════════════════════════
PHASE 2 — FIELD-LEVEL AND RECORD SCOPE EVIDENCE
═══════════════════════════════════════════

Build two evidence tables. Assign Gap IDs (G-series) to any gap at first
occurrence. These identifiers must travel unchanged through Phase 3 and Phase 4.

TABLE 1 — Field-Level Security by Role
Columns: Field | Default | Role | FLS Override | Gap ID | H-Flag |
Inertia: What breaks if this restriction is removed?

Requirements:
- Every field carrying sensitive data or differing by role has a row
- Specific field names and specific role names — not category descriptions
- Gap ID assigned at first occurrence for any misconfiguration
- Inertia column populated with a specific counterfactual for ≥1 row
- H-Flag set to H1/H2/... or N/A with reason

TABLE 2 — Record Access Scope by Role
Columns: Role | Scope (Own/BU/Parent BU/Org) | Enforcement Mechanism |
Gap ID | H-Flag | Inertia: What change would widen this scope beyond intent?

Requirements:
- Every security role has a row
- Scope and enforcement mechanism both named — not inferred
- Inertia column populated with a specific counterfactual for ≥1 row

━━━ PHASE 2 COMPLETION GATE ━━━
Assert this gate only when ALL conditions are satisfied:
  □ TABLE 1 contains ≥1 row per sensitive or role-differing field
  □ TABLE 1 Inertia column populated for ≥1 row
  □ TABLE 2 contains a row per security role
  □ TABLE 2 Inertia column populated for ≥1 row
  □ All Phase 2 gaps assigned G-series identifiers at first occurrence
  □ No Phase 3 escalation tables built yet

PHASE 2 COMPLETE ✓
━━━━━━━━━━━━━━━━━

---

═══════════════════════════════════════════
PHASE 3 — ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS
═══════════════════════════════════════════

Build four evidence tables. Carry all Phase 2 gap identifiers. Assign new
G-series identifiers for gaps first discovered here.

TABLE 3 — Role-Operation Matrix
Columns: Role | Create | Read | Update | Delete | Assign | Share |
Domain-Specific Operations | H-Flag

Requirement: Every role maps to every relevant operation. H-Flag populated.

TABLE 4 — Privilege Escalation Paths
Columns: Vector | Path Description | Roles Involved | Gap ID | H-Flag |
Inertia: What condition enables this escalation?

Required vectors (cover all four or provide null-finding with justification):
  1. Record reassignment
  2. Team promotion or membership elevation
  3. Sharing rule bypass
  4. Impersonation or delegation

Null-finding format (when no path found for a vector):
  Vector: [name] | Path: NONE | Controls examined: [specific] | Why it holds: [reason]

Requirement: Inertia column populated for ≥1 non-null row.

TABLE 5 — Sharing Rule Conflicts
Columns: Rule Name/Type | Baseline Role | Widened Access | Conflict |
Gap ID | H-Flag | Inertia: What rule change closes this widening?

TABLE 6 — Team Membership Gaps
Columns: Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag

Null-finding (if no team gap found):
  Name the teams examined and explain why membership is correct.

━━━ PHASE 3 COMPLETION GATE ━━━
Assert this gate only when ALL conditions are satisfied:
  □ TABLE 3: every role maps to every relevant operation
  □ TABLE 4: all four escalation vectors addressed (path found or null-finding given)
  □ TABLE 4 Inertia column populated for ≥1 row
  □ TABLE 5 and TABLE 6 complete
  □ All Phase 3 gaps assigned G-series identifiers

Then commit the gap inventory:

GAP INVENTORY (committed before Phase 3 closes):
[G-01] — [one-line description] — first seen: [TABLE X, row Y]
[G-02] — [one-line description] — first seen: [TABLE X, row Y]
... (all gaps from Phase 2 and Phase 3)

This inventory is final. Phase 4 may not introduce a gap identifier absent here.

  □ Gap inventory committed with all G-series identifiers from Phases 2 and 3
  □ No Phase 4 content written yet

PHASE 3 COMPLETE ✓
━━━━━━━━━━━━━━━━━

---

═══════════════════════════════════════════
PHASE 4 — FINDINGS, REMEDIATION, AND RISK SUMMARY
═══════════════════════════════════════════

4a. Hypothesis Resolution
For each H1, H2, ...:
  [H-ID]: Confirmed / Refuted / Modified
  Evidence: [Table name, row identifier]
  Delta from expectation: [what changed from original hypothesis]

4b. Null-Finding Accountability
For any Phase 3 table where no gap was found: name specific controls examined
and provide a one-sentence justification. "None identified" fails this check.

4c. Remediation per Gap
For each gap in the inventory:
  [G-ID] | Risk: High/Medium/Low | Remediation: [specific action, role, field]
  
  "Tighten security" or "review configuration" are not specific actions.

4d. TABLE 7 — Risk-Ranked Summary
Columns: Gap ID | Description | Source Table | Risk | Justification |
Phase 2 Origin? (Yes/No — if Yes: confirm 4-location chain)

Requirements:
  - Every row has a G-ID from the inventory
  - No new G-IDs
  - For Phase 2-origin gaps: Justification column confirms the four-location
    chain: Phase 2 table row → Phase 3 table → gap inventory → this row

━━━ PHASE 4 COMPLETION GATE ━━━
Assert this gate only when ALL conditions are satisfied:
  □ All hypotheses resolved with table/row citation
  □ All null-finding sections include specific controls examined
  □ All gaps have concrete remediation actions
  □ TABLE 7 contains only gap IDs from the inventory
  □ Phase 2-origin gaps show four-location chain in TABLE 7

PHASE 4 COMPLETE ✓
━━━━━━━━━━━━━━━━━
```

---

## V-04 — Combined: Conversational Register + Prominent Inertia Framing

**Axes:** Phrasing register (conversational, second-person) + Inertia framing (dedicated inertia sections, not just columns)
**Hypothesis:** Conversational phrasing reduces mechanical template-filling behavior; elevating inertia from a table column to a named analytical section forces genuine counterfactual reasoning rather than pro-forma "what breaks" entries.

---

```
You're doing a permissions trace for: {{topic}}

Your lens: Customer Service operations lead and Dataverse security expert.
You know this model has gaps — every model does. Your job is to find them,
understand why they exist, and explain what holds the current configuration
in place even when it's wrong.

That last part matters. For every significant access control you examine,
ask: what would actually break if this were changed? Who depends on this
misconfiguration? What would resist a fix? That's the inertia question, and
it makes the difference between a security audit and a permissions story.

---

START HERE: What do you expect to find?

Before you look at a single role or table, write down what you expect to be
broken. Be specific — not "there might be FLS gaps" but "AccountNumber is
probably visible to Customer Service reps who don't need it because the default
Dataverse FLS policy allows read on all standard fields."

Write at least two hypotheses:

H1: [Specific role] can [operation] on [field/record type] when they shouldn't.
    You expect this because: [structural reason]
    You'd know you're right if: [confirming evidence]
    You'd know you're wrong if: [refuting evidence]

H2: [Same structure]

These hypotheses drive everything that follows. Every table you build is
evidence for or against them. Every gap you name will trace back here.

PHASE 1 COMPLETE

---

WHAT CAN EACH ROLE SEE AT THE FIELD LEVEL?

Build the field-level security table. Flag anything that looks off with a
Gap ID (G-01, G-02, ...) assigned at first occurrence.

TABLE 1 — Field-Level Security by Role
| Field | Default | Role | FLS Override | Gap ID | H-Flag |

After you build it, sit with the "Status Quo Inertia" question for the
most interesting row:

**Status Quo Inertia — FLS**
Pick the gap or restriction that concerns you most. Answer:
- Who currently benefits from this configuration (correctly or not)?
- What would break — operationally, technically, organizationally — if you
  fixed this today?
- What pressure keeps this gap open?

This isn't a hypothetical. Name the specific actors and systems involved.

---

WHAT RECORDS CAN EACH ROLE ACCESS?

TABLE 2 — Record Access Scope by Role
| Role | Scope | Enforcement | Gap ID | H-Flag |

After the table:

**Status Quo Inertia — Record Scope**
For the most surprising scope assignment you found: what business process
currently relies on this scope being what it is? What would break if scope
were narrowed to Own-only? Who would complain and why?

PHASE 2 COMPLETE

---

WHAT CAN EACH ROLE DO?

TABLE 3 — Role-Operation Matrix
| Role | Create | Read | Update | Delete | Assign | Share | Domain Ops | H-Flag |

---

WHERE ARE THE ESCALATION PATHS?

Check all four vectors. For each one, either name the path or name why it
doesn't exist:

1. Record reassignment — can a user in Role A reassign a record to gain Role B scope?
2. Team promotion — does joining a team grant unintended org-wide access?
3. Sharing rule bypass — does any sharing rule widen access past the role baseline?
4. Impersonation/delegation — can any service account or delegated access create
   a scope mismatch?

TABLE 4 — Privilege Escalation Paths
| Vector | Path | Roles | Gap ID | H-Flag |

**Status Quo Inertia — Escalation**
For the most dangerous escalation path you found: what would an attacker need
to know or do to trigger it? What legitimate workflow currently uses the same
mechanism? That's why it's still open.

TABLE 5 — Sharing Rule Conflicts
| Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag |

TABLE 6 — Team Membership Gaps
| Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag |

If you found no conflict in TABLE 5 or no gap in TABLE 6, don't just skip it —
tell me what you looked at and why it came up clean.

GAP INVENTORY — everything you've found so far:
[G-01] — [description] — [table, row]
[G-02] ...

After this inventory, no new gap IDs. Phase 4 consolidates — it doesn't discover.

PHASE 3 COMPLETE

---

WHAT DID YOU ACTUALLY FIND?

**Hypothesis verdict**
For each H1, H2: Confirmed / Refuted / Modified.
What did you expect? What did you find? What table row proved it?

**Where the nulls came from**
If you found no gap in a section, name the controls you checked and explain
in one sentence why they held. Every null result needs a reason, not just an absence.

**What to fix and in what order**

For each gap:
  [G-ID] — Risk: High/Medium/Low — Fix: [specific action, naming role and field]

TABLE 7 — Risk-Ranked Summary
| Gap ID | Description | Source Table | Risk | Justification |

No new gaps here. For any gap that started in Phase 2 (FLS or scope table),
confirm in the Justification column that it appears in all four places:
Phase 2 table → Phase 3 table → gap inventory → this row.

**The two things to fix first, and why those two.**

PHASE 4 COMPLETE
```

---

## V-05 — Combined: Adversarial-First Role Sequence + Structural Competitor Inertia

**Axes:** Role sequence (lead with highest-privilege / most dangerous role) + Inertia framing (framed as "structural competitor" — the current config is a competitor defending a position, not a neutral baseline)
**Hypothesis:** Treating the current access configuration as an adversary defending a position shifts the analyst from describing what is to interrogating why it persists — making C-18/C-19 inertia columns emerge from first principles and making privilege escalation paths feel like the main event rather than an appendix.

---

```
You are a Dataverse security expert performing a red-team-informed permissions
trace for: {{topic}}

Lens: You are the most dangerous legitimate user in this system. You have the
broadest permissions the security model allows. You know where the boundaries
are because you've tested them. Now trace the model from that vantage point
outward to find where it fails.

The current access configuration is not a neutral baseline. It is a
structural competitor: a set of decisions, habits, and constraints that
actively resists change. Every inertia question asks: what does this
configuration defend, and why is that defense load-bearing? Some defenses
are legitimate. Some are accidental. Both kinds need naming.

---

PHASE 1 — THREAT HYPOTHESES

Lead with the two access patterns most likely to be exploited.

These are not descriptions of what exists. They are hypotheses about what
a sophisticated user with legitimate access could abuse — and why the model
as designed creates the opportunity.

H1: [Specific role + vector] — [Abuse path] — [Why the model creates this]
    Confirms if: [specific evidence in role matrix or escalation table]
    Refutes if: [specific control found to be correctly configured]

H2: [Same structure]

Optional H3+: Add if you identify a third plausible abuse path.

These hypotheses frame all four phases. Every table you build is evidence
for or against a hypothesis. Every gap not connected to a hypothesis by
Phase 4 demands an explanation.

PHASE 1 COMPLETE

---

PHASE 2 — FIELD-LEVEL AND SCOPE EVIDENCE (Viewed from the Threat Hypotheses)

Examine FLS and record scope through the lens of H1 and H2. What do those
hypotheses require to be true at the field and scope level?

TABLE 1 — Field-Level Security by Role
Columns: Field | Default | Role | FLS Override | Gap ID | H-Flag |
Structural Competitor: What does this configuration defend, and is that defense legitimate?

Instructions:
- Start with the fields most relevant to H1 and H2.
- A legitimate defense: "AccountNumber FLS restricts Customer Service read
  because it's used in billing disputes — widening access creates fraud risk."
- An accidental defense: "CasePriority is readable by all roles because FLS
  was never configured — the default holds by inertia, not by design."
- Label each row's Structural Competitor entry as "Legitimate" or "Accidental."
- Assign Gap IDs to any Accidental or Missing restriction at first occurrence.
- H-Flag: tie to H1/H2 or mark N/A.

TABLE 2 — Record Access Scope by Role
Columns: Role | Scope | Enforcement | Gap ID | H-Flag |
Structural Competitor: What org process depends on this scope — and what breaks if it tightens?

Instructions:
- Start with the highest-scope role. Trace outward to more restricted roles.
- For each scope, identify whether the scope is by design (documented enforcement
  mechanism) or by default (no explicit restriction).
- Label each Structural Competitor entry with the dependency that holds the
  scope in place.

PHASE 2 COMPLETE

---

PHASE 3 — ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS

Start with the highest-privilege role. Trace downward to least-privileged.
This order matters: escalation paths often begin at the top.

TABLE 3 — Role-Operation Matrix
Columns: Role | Create | Read | Update | Delete | Assign | Share | Domain Ops | H-Flag

Order rows: highest privilege first. Mark over-permissive cells with Gap IDs.

TABLE 4 — Privilege Escalation Paths
Cover all four vectors. Each vector is either a confirmed path with a gap ID
or a cleared vector with a null-finding.

Columns: Vector | Path | Roles | Gap ID | H-Flag |
Structural Competitor: What legitimate workflow uses this same mechanism?

Required vectors:
1. Record reassignment
2. Team promotion/membership elevation
3. Sharing rule bypass
4. Impersonation or delegation

Null-finding format:
  Vector: [name] | Path: NONE | Control examined: [specific] | Why it holds: [reason]

For each confirmed path, populate the Structural Competitor column:
What legitimate workflow currently uses the same mechanism that enables this
escalation? That's what makes the fix expensive.

TABLE 5 — Sharing Rule Conflicts
Columns: Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag |
Structural Competitor: What access need does this widening legitimately satisfy?

TABLE 6 — Team Membership Gaps
Columns: Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag

GAP INVENTORY (committed before Phase 3 closes):
[G-01] — [description] — [table/row] — [H-connection: H1/H2/independent]
[G-02] ...

No new gap identifiers may appear in Phase 4.

PHASE 3 COMPLETE

---

PHASE 4 — ADVERSARIAL ASSESSMENT AND REMEDIATION

4a. Hypothesis Verdicts
For each H1, H2, ...:
  Verdict: Confirmed / Refuted / Modified
  Resolving evidence: [table name, row]
  What the structural competitor was defending: [the org dependency that kept
  this gap open — legitimate or accidental]

4b. Null-Finding Accountability
For any table with no gap found: name controls examined, explain why they held.
One sentence minimum per null result.

4c. Remediation — Addressing the Structural Competitor
For each gap, the fix must name not just the action but the structural
resistance it will encounter:

  [G-ID] | Risk: H/M/L | Fix: [specific action, role, field]
  Resistance: [what org dependency, workflow, or habit will push back on this fix]

4d. TABLE 7 — Risk-Ranked Summary
Columns: Gap ID | Description | Source | Risk | Justification |
Competitor Resistance (High/Medium/Low)

Requirements:
- Only gap IDs from the inventory
- For Phase 2-origin gaps: Justification confirms four-location chain
  (Phase 2 table → Phase 3 table → inventory → this row)
- Competitor Resistance column: rate how hard this gap is to close given
  legitimate org dependencies

Closing statement: Name the single gap where the structural competitor is
strongest — the fix that is technically obvious but organizationally expensive.
That is where the real work is.

PHASE 4 COMPLETE
```

---

## Variation Summary

| ID | Axis / Axes | Core Bet |
|----|-------------|----------|
| V-01 | Role sequence: Gap-first | Hypothesis-first ordering makes H-flag columns feel native to the evidence layer rather than retrofitted |
| V-02 | Output format: Prose-anchored | Narrative wrapping forces explicit reasoning at null-finding sites; tables become evidence, not endpoints |
| V-03 | Lifecycle emphasis: Maximally explicit gates | Multi-condition completion gates create self-verification checkpoints that reduce premature gate assertion |
| V-04 | Conversational register + Prominent inertia sections | Second-person voice reduces template behavior; elevating inertia to named sections drives genuine counterfactual reasoning |
| V-05 | Adversarial-first role sequence + Structural competitor inertia | Leading with highest-privilege role and framing inertia as organizational resistance surfaces escalation paths as main event, not appendix |
