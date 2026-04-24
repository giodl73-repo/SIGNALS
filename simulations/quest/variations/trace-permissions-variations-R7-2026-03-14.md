Written to `simulations/quest/variations/trace-permissions-variations-R7-2026-03-14.md`.

---

## trace-permissions R7 -- Variation Set Summary

Five complete variations targeting the 170-pt ceiling (C-21/C-22/C-23 added):

| ID | Axis | Core Structural Bet |
|----|------|---------------------|
| **V-01** | Lifecycle emphasis (gate-centric) | All three new mechanisms embedded in the gate scaffolding as primary structure -- compliance assembles forward, no Phase 4 retrospective classification needed |
| **V-02** | Role sequence / output format (field-centric + forward origin tagging) | Phase 2 gaps tagged "(P2)" at discovery; TABLE 7 Phase Origin reads from pre-classified data rather than inspecting back through tables |
| **V-03** | Output format (compressed scaffolding) | Same structural requirements, ~40% fewer words -- tests which requirements were load-bearing vs. decorative prose |
| **V-04** | Conversational register + column-bound inertia (R6 V-04 fix) | Keeps second-person voice; moves inertia back into per-row columns (fixing the R6 C-18/C-19 failure); adds all three new criteria |
| **V-05** | Adversarial-first + Structural Competitor + C-21/C-22/C-23 | Upgrades R6 V-05: adds explicit Phase 3 carry-forward (fixing the C-20 partial), gate checklists, source-locked inventory, and inline origin chain while preserving the adversarial framing |

Key structural decisions in R7:
- **C-23**: All variations put the four-location chain inline in the Phase Origin column itself -- not in the Justification column. V-01/V-03/V-05 use positional notation (`T1/row -> T4/r2 -> INV/G-01 -> T7/r1`); V-02 uses the `(P2)` tag to make Phase 2-origin gaps mechanically distinguishable before TABLE 7; V-04 explains the design choice to the CS-lead persona.
- **C-22**: All variations include `first seen: [TABLE X, row Y]` in inventory entries. V-05 adds the H-connection field as a fourth inventory component.
- **C-21**: All variations use □-checklist gates with >=3 conditions per gate. V-03 (compressed) uses the shortest checklists; V-05 uses the longest (7 conditions on the Phase 4 gate).
le, field, or operation
  □ Each hypothesis states both confirming and refuting evidence
  □ No evidence tables built yet

PHASE 1 COMPLETE
━━━━━━━━━━━━━━━━━

---

═══════════════════════════════════════════
PHASE 2 -- FIELD-LEVEL AND RECORD SCOPE EVIDENCE
═══════════════════════════════════════════

Build two evidence tables. Assign Gap IDs (G-series) to any gap at first
occurrence. Every identifier assigned here travels unchanged through Phase 3
and Phase 4.

TABLE 1 -- Field-Level Security by Role
Columns: Field | Default | Role | FLS Override | Gap ID | H-Flag |
Inertia: What breaks if this restriction is removed?

Requirements:
- Every field carrying sensitive data or differing by role has a row
- Specific field names and specific role names -- not category descriptions
- Gap ID assigned at first occurrence for any misconfiguration
- Inertia column populated with a specific counterfactual for >=1 row
- H-Flag tied to H1/H2/... or N/A with brief reason

TABLE 2 -- Record Access Scope by Role
Columns: Role | Scope (Own/BU/Parent BU/Org) | Enforcement Mechanism |
Gap ID | H-Flag | Inertia: What change would widen this scope beyond intent?

Requirements:
- Every security role has a row
- Scope and enforcement mechanism both named -- not inferred
- Inertia column populated with a specific counterfactual for >=1 row

━━━ PHASE 2 COMPLETION GATE ━━━
Assert PHASE 2 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 1 contains >=1 row per sensitive or role-differing field
  □ TABLE 1 Inertia column populated for >=1 row (specific counterfactual, not "N/A")
  □ TABLE 2 contains a row per security role
  □ TABLE 2 Inertia column populated for >=1 row
  □ All Phase 2 gaps assigned G-series identifiers at first occurrence
  □ No Phase 3 tables built yet

PHASE 2 COMPLETE
━━━━━━━━━━━━━━━━━

---

═══════════════════════════════════════════
PHASE 3 -- ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS
═══════════════════════════════════════════

Build four evidence tables. Carry all Phase 2 gap identifiers -- each G-series
identifier assigned in Phase 2 must appear in at least one Phase 3 table row.
Assign new G-series identifiers (continuing the sequence) for gaps first
discovered here.

TABLE 3 -- Role-Operation Matrix
Columns: Role | Create | Read | Update | Delete | Assign | Share |
Domain-Specific Operations | H-Flag

Requirement: Every role maps to every relevant operation. H-Flag populated.

TABLE 4 -- Privilege Escalation Paths
Columns: Vector | Path Description | Roles Involved | Gap ID | H-Flag |
Inertia: What condition enables this escalation?

Required vectors -- cover all four or provide null-finding:
  1. Record reassignment
  2. Team promotion or membership elevation
  3. Sharing rule bypass
  4. Impersonation or delegation

Null-finding format:
  Vector: [name] | Path: NONE | Controls examined: [specific] | Why it holds: [reason]

Requirement: Inertia column populated for >=1 non-null row.

TABLE 5 -- Sharing Rule Conflicts
Columns: Rule Name/Type | Baseline Role | Widened Access | Conflict |
Gap ID | H-Flag | Inertia: What rule change closes this widening?

TABLE 6 -- Team Membership Gaps
Columns: Team | Expected Members | Gap Scenario | Combined Permission Risk |
Gap ID | H-Flag

Null-finding (if no team gap found): Name the teams examined; explain in one
sentence why membership is correct.

━━━ PHASE 3 COMPLETION GATE ━━━
Assert PHASE 3 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 3: every role maps to every relevant operation; H-Flag populated
  □ TABLE 4: all four escalation vectors addressed (path found or null-finding given)
  □ TABLE 4 Inertia column populated for >=1 non-null row
  □ TABLE 5 complete with Inertia column
  □ TABLE 6 complete (gap found or null-finding with teams named)
  □ All Phase 2 gap identifiers appear in >=1 Phase 3 table row

Then commit the source-locked gap inventory. Each entry must include the
source table and row at commit time -- this binding is permanent and must
not require Phase 4 back-tracing to reconstruct:

GAP INVENTORY (committed before Phase 3 closes):
[G-01] -- [one-line description] -- first seen: [TABLE 1, FieldName row]
[G-02] -- [one-line description] -- first seen: [TABLE X, row Y]
... (all gaps from Phase 2 and Phase 3; no omissions)

  □ Gap inventory committed with all G-series identifiers
  □ Every entry includes "first seen: [TABLE X, row Y]" -- no entry omits source
  □ No Phase 4 content written yet

PHASE 3 COMPLETE
━━━━━━━━━━━━━━━━━

---

═══════════════════════════════════════════
PHASE 4 -- FINDINGS, REMEDIATION, AND RISK SUMMARY
═══════════════════════════════════════════

4a. Hypothesis Resolution
For each H1, H2, ...:
  [H-ID]: Confirmed / Refuted / Modified
  Evidence: [Table name, row identifier -- be specific]
  Delta: [what changed from the original hypothesis]

4b. Null-Finding Accountability
For any Phase 3 table where no gap was found: name the specific controls
examined; provide a one-sentence justification. "None identified" alone fails.

4c. Remediation per Gap
For each gap in the inventory:
  [G-ID] | Risk: High / Medium / Low | Remediation: [specific action: role + field + operation]

"Tighten security" or "review configuration" without naming the exact role,
field, or operation do not pass.

4d. TABLE 7 -- Risk-Ranked Summary
Columns: Gap ID | Description | Risk (H/M/L) | Justification |
Phase Origin [P3 | P2: T#/row -> T#/row -> INV/G-NN -> T7/rN]

Phase Origin column rules:
- Phase 3-origin gaps: enter "P3"
- Phase 2-origin gaps: enter the four-location chain inline, not in Justification:
    "P2: T1/[row] -> T[N]/[row] -> INV/G-[NN] -> T7/r[N]"
  Example: "P2: T1/AccountNumber -> T4/r2 -> INV/G-01 -> T7/r1"
- The chain must be verifiable by inspection of the table alone

Requirements:
- Every row has a G-ID from the Phase 3 inventory
- No new G-IDs in TABLE 7
- Phase Origin column populated for every row

━━━ PHASE 4 COMPLETION GATE ━━━
Assert PHASE 4 COMPLETE only when ALL conditions are satisfied:
  □ All hypotheses resolved with specific table/row citation
  □ All null-finding sections name specific controls examined
  □ All gaps have concrete remediation (role + field + operation named)
  □ TABLE 7 contains only G-IDs from the Phase 3 inventory
  □ TABLE 7 Phase Origin column populated for every row
  □ Every Phase 2-origin gap shows full inline chain in Phase Origin column
  □ No new gap IDs introduced in Phase 4

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## V-02 -- Single Axis: Role Sequence (Field-Centric Discovery with Forward Origin Tagging)

**Axis:** Role sequence / discovery order
**Hypothesis:** Organizing Phase 2 with fields as the primary analytical dimension -- rather than roles -- causes Phase 2-origin gaps to carry their origin classification forward automatically. When each TABLE 1 row is definitionally a Phase 2 artifact, the Phase Origin column in TABLE 7 fills from pre-classified data rather than requiring retrospective inspection. C-23 becomes a propagation operation rather than a classification operation.

---

```
You are a Dataverse security expert performing a permissions trace for: {{topic}}

Stock roles: Customer Service, Dataverse Security Expert. Add domain-specific
roles as needed.

SEQUENCE DESIGN: This trace runs field-centric before role-centric. Phase 2
begins with the fields that carry the most risk -- what they expose, to whom,
and under what FLS configuration. Roles emerge as the dimension that
differentiates field access, not as the primary organizing unit. Phase 3
runs the role-operation matrix and escalation analysis with field-level
findings already in hand.

Every gap is tagged with its discovery phase at first occurrence.
Phase 2-origin gaps carry the tag "(P2)" on their Gap ID through all tables.
Phase 3-origin gaps carry no special tag -- absence of "(P2)" means Phase 3 origin.

---

PHASE 1 -- HYPOTHESIS PRE-COMMITMENT

Before building any tables, commit to your expected findings. Lead with
field-level hypotheses first (what fields are improperly exposed), then
escalation hypotheses (what paths exist to elevate privilege).

H1: [Field or field group] -- [Role that has improper access] -- [Why FLS default allows it]
    Confirms if: [specific FLS table evidence]
    Refutes if: [specific FLS control found]

H2: [Escalation vector] -- [Roles involved] -- [Structural reason the path exists]
    Confirms if: [specific escalation table evidence]
    Refutes if: [specific control found blocking it]

Add H3+ for any additional hypotheses.

━━━ PHASE 1 COMPLETION GATE ━━━
Assert PHASE 1 COMPLETE only when ALL conditions are satisfied:
  □ At least 2 hypotheses stated: >=1 field-level, >=1 escalation
  □ Each hypothesis names specific field(s) or vector and specific roles
  □ Each hypothesis states confirming and refuting evidence
  □ No tables built yet

PHASE 1 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 2 -- FIELD-LEVEL AND RECORD SCOPE EVIDENCE

TABLE 1 is field-primary: each row is one field, with columns for each role.
Phase 2-origin gaps receive a Gap ID with "(P2)" suffix: G-01(P2), G-02(P2), ...

TABLE 1 -- Field Exposure Map
Columns: Field | Sensitivity (High/Med/Low) | [Role A] FLS | [Role B] FLS |
... [all roles] ... | Gap ID (with P2 tag if gap) | H-Flag |
Inertia: What breaks if the least-restrictive role's access is narrowed?

Instructions:
- One row per sensitive field or field differing by role
- For each role column: enter the FLS configuration (Read/Edit/None/Default)
- If any role has more access than data sensitivity warrants, assign a Gap ID
  with "(P2)" tag at first occurrence
- Inertia column: answer for the most sensitive gap row; "N/A" requires
  a one-sentence justification
- H-Flag: tie to H1/H2 or "N/A -- [reason]"

TABLE 2 -- Record Access Scope by Role
Columns: Role | Scope (Own/BU/Parent BU/Org) | Enforcement | Gap ID (with P2 tag) |
H-Flag | Inertia: What org change would widen this scope?

Instructions:
- One row per security role, widest scope first
- Scope and enforcement mechanism both named
- If scope exceeds what the role's function requires, assign a Gap ID with "(P2)" tag
- Inertia column populated for >=1 row

━━━ PHASE 2 COMPLETION GATE ━━━
Assert PHASE 2 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 1 covers all sensitive or role-differing fields; one row per field
  □ TABLE 1 Inertia column populated for >=1 gap row (specific counterfactual)
  □ TABLE 2 covers all security roles; one row per role
  □ TABLE 2 Inertia column populated for >=1 row
  □ All Phase 2 gaps carry "(P2)" suffix on their G-series identifier
  □ No Phase 3 tables built yet

PHASE 2 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 3 -- ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS

Build four tables. Carry all Phase 2 gap identifiers -- each G-ID with "(P2)"
tag must appear in at least one Phase 3 table row to establish the Phase 3 link.
New gaps discovered here receive standard G-series IDs without the "(P2)" tag.

TABLE 3 -- Role-Operation Matrix
Columns: Role | Create | Read | Update | Delete | Assign | Share |
Domain Ops | Gap ID (if over-permissive) | H-Flag

Requirement: Every role maps to every relevant operation. H-Flag populated per row.

TABLE 4 -- Privilege Escalation Paths
Columns: Vector | Path | Roles | Gap ID | H-Flag |
Inertia: What condition enables or sustains this escalation?

Required vectors (all four; null-finding required if no path found):
  1. Record reassignment
  2. Team promotion or membership elevation
  3. Sharing rule bypass
  4. Impersonation or delegation

Null-finding format:
  Vector: [name] | Path: NONE | Controls examined: [specific] | Why it holds: [reason]

Inertia column populated for >=1 non-null path row.

For any P2-tagged gap that surfaces as an escalation vector: reference its
Gap ID (with "(P2)" tag) in TABLE 4 to establish the Phase 3 analytical link.

TABLE 5 -- Sharing Rule Conflicts
Columns: Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag |
Inertia: What rule change closes this widening?

TABLE 6 -- Team Membership Gaps
Columns: Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag

Null-finding if no team gap: name teams examined; explain why membership is correct.

━━━ PHASE 3 COMPLETION GATE ━━━
Assert PHASE 3 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 3: every role maps to every relevant operation
  □ TABLE 4: all four vectors addressed (path or null-finding)
  □ TABLE 4 Inertia populated for >=1 non-null row
  □ TABLE 5 complete; Inertia column present
  □ TABLE 6 complete (gap or null-finding with teams named)
  □ All P2-tagged Gap IDs appear in >=1 Phase 3 table row

Then commit the source-locked gap inventory:

GAP INVENTORY (committed before Phase 3 closes):
[G-01(P2)] -- [description] -- first seen: [TABLE 1, FieldName row]
[G-02(P2)] -- [description] -- first seen: [TABLE 2, RoleName row]
[G-03]     -- [description] -- first seen: [TABLE 4, Vector row]
... (all gaps; "(P2)" tag present on Phase 2-origin entries)

  □ Inventory committed; every G-series ID present with description and source
  □ Every entry includes "first seen: [TABLE X, row]"
  □ Phase 2-origin entries carry "(P2)" tag consistently

PHASE 3 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 4 -- FINDINGS, REMEDIATION, AND RISK SUMMARY

4a. Hypothesis Resolution
For each H1, H2, ...:
  [H-ID]: Confirmed / Refuted / Modified
  Evidence: [Table name, row]
  Delta: [what changed from original expectation]

4b. Null-Finding Accountability
For any Phase 3 table where no gap was found: name specific controls examined;
one-sentence justification. "None identified" fails.

4c. Remediation per Gap
  [G-ID] | Risk: H/M/L | Remediation: [specific: role + field + operation]

4d. TABLE 7 -- Risk-Ranked Summary
Columns: Gap ID | Description | Risk | Justification |
Phase Origin [P3 | P2: T#/row -> T#/row -> INV/entry -> T7/rN]

Phase Origin column rules:
- Standard G-IDs (no "(P2)" tag): enter "P3"
- P2-tagged G-IDs: enter the four-location chain. The "(P2)" tag makes origin
  mechanically detectable; the chain confirms the four links:
    "P2: T1/[field] -> T[N]/[row] -> INV/G-NN(P2) -> T7/r[N]"
- The chain must be readable from the column alone -- no cross-reference needed

Requirements:
- Every row has a G-ID from the inventory
- No new G-IDs
- Phase Origin column populated for every row

━━━ PHASE 4 COMPLETION GATE ━━━
Assert PHASE 4 COMPLETE only when ALL conditions are satisfied:
  □ All hypotheses resolved with table/row citations
  □ Null-finding sections name specific controls
  □ All remediations name role + field + operation
  □ TABLE 7 contains only inventory G-IDs
  □ Phase Origin column populated for every TABLE 7 row
  □ Every P2-tagged gap shows inline four-location chain in Phase Origin column
  □ No new G-IDs in Phase 4

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## V-03 -- Single Axis: Output Format (Compressed Scaffolding)

**Axis:** Output format (maximum density, minimum prose scaffolding)
**Hypothesis:** Structural compliance mechanisms (C-21 gate checklists, C-22 source-locked inventory, C-23 origin column) survive prompt compression because they are specified by rule rather than by example. A prompt with half the prose footprint of V-01 can achieve the same structural properties if each rule is stated precisely and once. Compression reveals which requirements were load-bearing vs. decorative.

---

```
Dataverse security expert. Permissions trace for: {{topic}}
Roles: Customer Service, Dataverse Security Expert (add domain roles as needed).

RULE: Each phase closes with a completion gate. The gate is a □-checklist --
not a header. Assert COMPLETE only after every □ is verifiable in the output
above it. Unmet conditions block gate assertion.

---

PHASE 1 -- HYPOTHESES

State >=2 falsifiable hypotheses before any table. Label H1, H2, ...
Each must name a specific role/field/operation, state the structural reason,
and state confirming evidence + refuting evidence.

PHASE 1 GATE:
  □ >=2 H-labeled hypotheses, each with role/field/op, reason, confirm, refute
  □ No tables built

PHASE 1 COMPLETE

---

PHASE 2 -- FLS AND RECORD SCOPE

TABLE 1 -- Field-Level Security by Role
| Field | Default | Role | FLS Override | Gap ID | H-Flag | Inertia: What breaks if removed? |
- All sensitive/role-differing fields have rows
- Gap IDs (G-series) assigned at first occurrence
- Inertia: >=1 row populated with specific counterfactual

TABLE 2 -- Record Access Scope
| Role | Scope | Enforcement | Gap ID | H-Flag | Inertia: What widens this scope? |
- All security roles have rows
- Scope + enforcement both named
- Inertia: >=1 row populated

PHASE 2 GATE:
  □ TABLE 1: >=1 row/field; Inertia >=1 row; Gap IDs at first occurrence
  □ TABLE 2: >=1 row/role; Inertia >=1 row
  □ No TABLE 3-6 built

PHASE 2 COMPLETE

---

PHASE 3 -- ROLE-OPERATION MATRIX AND ESCALATION

Carry all Phase 2 Gap IDs into >=1 Phase 3 table row each.
New gaps here get continuing G-series IDs.

TABLE 3 -- Role-Operation Matrix
| Role | Create | Read | Update | Delete | Assign | Share | Domain Ops | H-Flag |
All roles x all relevant operations; H-Flag per row.

TABLE 4 -- Privilege Escalation Paths
| Vector | Path | Roles | Gap ID | H-Flag | Inertia: What enables this? |
Cover all 4 vectors: (1) record reassignment (2) team promotion (3) sharing rule bypass
(4) impersonation/delegation. For each with no path: name the control; explain why it holds.
Inertia: >=1 non-null row populated.

TABLE 5 -- Sharing Rule Conflicts
| Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag | Inertia: What closes this? |

TABLE 6 -- Team Membership Gaps
| Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag |
No gap found: name teams examined + one-sentence justification.

PHASE 3 GATE:
  □ TABLE 3: all roles x all ops; H-Flag populated
  □ TABLE 4: all 4 vectors (path or named null-finding); Inertia >=1 row
  □ TABLE 5 and TABLE 6 complete
  □ All Phase 2 Gap IDs appear in >=1 Phase 3 row

Commit inventory before gate asserts:

GAP INVENTORY:
[G-NN] -- [description] -- first seen: [TABLE X, row Y]
(all gaps; every entry includes source table and row)

  □ Inventory complete; every entry has G-ID + description + "first seen: TABLE X, row Y"

PHASE 3 COMPLETE

---

PHASE 4 -- FINDINGS AND SUMMARY

4a. Hypothesis Resolution
Each H-ID: Confirmed / Refuted / Modified | Evidence: [table, row] | Delta: [what changed]

4b. Null-Finding Accountability
Each Phase 3 table with no gap: name controls examined + one-sentence justification.

4c. Remediation
Each gap: [G-ID] | Risk: H/M/L | Remediation: [specific: role + field + operation]

4d. TABLE 7 -- Risk-Ranked Summary
| Gap ID | Description | Risk | Justification | Phase Origin |

Phase Origin column:
- Phase 3 gap: "P3"
- Phase 2 gap: "P2: T[N]/[row] -> T[N]/[row] -> INV/G-NN -> T7/r[N]" (inline chain)

PHASE 4 GATE:
  □ All hypotheses resolved with table/row citations
  □ All null-findings name specific controls
  □ All remediations: role + field + operation named
  □ TABLE 7: only inventory G-IDs; Phase Origin column populated every row
  □ Phase 2-origin gaps: full inline chain in Phase Origin column (not in Justification)
  □ No new G-IDs

PHASE 4 COMPLETE
```

---

## V-04 -- Combined: Conversational Register + Column-Bound Inertia (R6 V-04 Fix) + C-21/C-22/C-23

**Axes:** Phrasing register (conversational, second-person) + Inertia framing (column-bound, not post-table sections)
**Hypothesis:** R6 V-04 failed C-18 and C-19 because "Status Quo Inertia" sections answered a per-table question rather than a per-row question, making it impossible to satisfy the column-bound criterion. This variation keeps the conversational register but puts inertia back in the table columns where it belongs -- one counterfactual cell per row. Combined with C-21 gate checklists, C-22 source-locked inventory, and C-23 origin-classified TABLE 7, this tests whether second-person framing can carry full structural compliance.

---

```
You're doing a permissions trace for: {{topic}}

You're playing two roles: a Customer Service operations lead who knows which
fields matter in day-to-day case work, and a Dataverse security expert who
knows where RBAC configurations go wrong. These two perspectives should
disagree at least once -- the CS lead wants access; the security expert says
the access model doesn't support it.

One rule before you start: every phase ends with a gate that lists specific
conditions you have to satisfy before moving on. The gate isn't a label --
it's a checklist. Work through every box before you call the phase done.

---

Before you look at any data, what do you expect to find?

Pick the two security gaps most likely to exist in {{topic}}'s access model
and commit to them before you build a single table. Be specific about which
role, which field or operation, and why the model as designed would produce
this gap. Generic predictions like "there may be FLS issues" don't count.

H1: [Specific role] [has access to / can perform] [specific field / operation]
    [when they shouldn't, because ...]
    You'd know you're right if: [specific evidence]
    You'd know you're wrong if: [specific control found]

H2: [Same structure]

These two hypotheses are the backbone of everything that follows. Every table
you build is evidence for or against one of them. If you find a gap that
connects to neither hypothesis, add H3 -- but don't retroactively rewrite H1
and H2 to absorb it.

Gate -- Phase 1:
  □ 2+ hypotheses committed with H-labels
  □ Each names a specific role AND specific field or operation
  □ Each states confirming evidence and refuting evidence
  □ No tables started

PHASE 1 COMPLETE

---

What can each role actually see at the field level?

Build TABLE 1. Every row is one field. If a field is accessible to any role
that doesn't need it, assign a Gap ID (G-01, G-02, ...) right there -- at
the row where you found it.

TABLE 1 -- Field-Level Security by Role
| Field | Default | Role | FLS Override | Gap ID | H-Flag |
  What breaks if this restriction is tightened or removed? |

For the Inertia column: answer per row. The CS lead perspective is useful
here -- "tightening this would break the case escalation workflow because..."
is exactly the kind of answer that makes the inertia real. At minimum, one
row needs a specific answer; all other rows need either a real answer or an
explicit "no operational dependency -- safe to restrict."

Now record scope:

TABLE 2 -- Record Access Scope by Role
| Role | Scope (Own/BU/Parent BU/Org) | Enforcement | Gap ID | H-Flag |
  What org change or configuration drift would widen this scope? |

Highest-scope role first. For each scope, name the mechanism that enforces it
-- not "configured correctly" but the actual Dataverse control. If the only
thing keeping a scope at BU level is convention rather than enforcement,
that's a gap worth flagging.

Gate -- Phase 2:
  □ TABLE 1 covers all sensitive or role-differing fields; >=1 Inertia cell populated
  □ TABLE 2 covers all security roles; >=1 Inertia cell populated
  □ All Phase 2 gaps have G-series IDs assigned at the row of first discovery
  □ No Phase 3 tables started

PHASE 2 COMPLETE

---

Now the operation matrix and escalation analysis.

Carry your Phase 2 gap IDs forward. Any G-ID from Phase 2 needs to appear
somewhere in Phase 3 -- if a field-level gap has no escalation implication,
it still gets referenced in TABLE 4 or TABLE 5 as a vector input.

TABLE 3 -- Role-Operation Matrix
| Role | Create | Read | Update | Delete | Assign | Share | Domain Ops | H-Flag |

Call out anything in this matrix that surprises you from the CS operations
perspective -- a role that can delete records it shouldn't be able to, or
a role that lacks an operation it needs for its stated function.

Check all four escalation vectors. For each one, either describe the path
or explain why it doesn't exist:

TABLE 4 -- Privilege Escalation Paths
| Vector | Path | Roles | Gap ID | H-Flag |
  What condition in the current config makes this path possible or impossible? |

The four vectors:
1. Record reassignment -- can a user get wider scope by reassigning?
2. Team promotion -- does joining a team grant unintended org-wide access?
3. Sharing rule bypass -- does any sharing rule blow past the role baseline?
4. Impersonation/delegation -- can a service account create a scope mismatch?

For each vector with no path: don't skip it -- write one sentence naming
the control you checked and why it holds. "None found" is not an answer.

TABLE 5 -- Sharing Rule Conflicts
| Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag |
  What legitimate access need does this widening serve? |

TABLE 6 -- Team Membership Gaps
| Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag |

If you found no conflicts in TABLE 5 or no gaps in TABLE 6, name what you
looked at and why it came up clean.

Then lock the gap inventory. After this, no new gap IDs:

GAP INVENTORY (all gaps, closed before this phase ends):
[G-NN] -- [what it is] -- first seen: [TABLE X, row Y]
(source table and row are part of the entry -- not recoverable by back-tracing)

Gate -- Phase 3:
  □ TABLE 3: all roles x all operations; H-Flag on every row
  □ TABLE 4: all 4 vectors addressed (path or explicit null-finding)
  □ TABLE 4 Inertia column: >=1 non-null row populated
  □ TABLE 5 and TABLE 6 complete
  □ All Phase 2 G-IDs appear in >=1 Phase 3 table row
  □ Gap inventory committed; every entry includes "first seen: TABLE X, row Y"

PHASE 3 COMPLETE

---

What did you actually find?

Hypothesis verdicts -- be honest about what the evidence said:
For each H1, H2, ...: Confirmed / Refuted / Modified
  What table and row resolved it? What did you expect vs. what did you find?

Where gaps came up empty:
For any table where you found nothing: name the controls you examined and
explain in one sentence why they held. Every null needs a reason.

What to fix, in order:
For each gap in the inventory:
  [G-ID] -- Risk: High / Medium / Low -- Fix: [specific: role, field, operation]

Don't write "tighten security." Write the exact FLS change, the exact role,
and the exact field. The CS operations lead needs to know what breaks when
you fix it; the security expert needs to know exactly what to configure.

TABLE 7 -- Risk-Ranked Summary
| Gap ID | Description | Risk | Justification | Phase Origin |

Phase Origin column:
- Phase 3 gap: "P3"
- Phase 2 gap: write the four-location chain inline in this column (not in Justification):
    "P2: T[N]/[field] -> T[N]/r[N] -> INV/G-NN -> T7/r[N]"
  The CS operations lead shouldn't need to flip back through three tables to
  understand where a field-level gap originated. The chain goes in the column.

Gate -- Phase 4:
  □ Every hypothesis has a verdict with table/row citation
  □ Every null-finding section names specific controls + one-sentence justification
  □ Every remediation names role + field + operation (no vague guidance)
  □ TABLE 7 contains only G-IDs from the inventory; Phase Origin populated every row
  □ Phase 2-origin gaps: full inline chain in Phase Origin (not delegated to Justification)
  □ No new G-IDs introduced in Phase 4

PHASE 4 COMPLETE
```

---

## V-05 -- Combined: Adversarial-First Role Sequence + Structural Competitor Inertia + C-21/C-22/C-23

**Axes:** Role sequence (highest-privilege first, adversarial lens) + Inertia framing (Structural Competitor -- org dependencies defending misconfiguration)
**Hypothesis:** R6 V-05 scored 153/155 -- a C-20 partial caused by the absence of an explicit Phase 3 carry-forward instruction for Phase 2 gaps that don't manifest as escalation paths. This variation adds that instruction, upgrades the Phase 3 gate to include C-21 multi-condition checklists, reformats the gap inventory for C-22 source locking, and upgrades TABLE 7 for C-23 inline origin classification. The Structural Competitor inertia framing is preserved -- it proved in R6 that domain-reframed counterfactual columns satisfy C-18/C-19. The adversarial role sequence is preserved. Only the structural compliance mechanisms are upgraded.

---

```
You are a Dataverse security expert performing a red-team-informed permissions
trace for: {{topic}}

Lens: You are the most privileged legitimate user in this system. You know
where the boundaries are. You're now examining the model from that vantage
point outward to find where it fails.

The current access configuration is not a neutral baseline. It is a
structural competitor: a set of decisions, habits, and enforcement gaps that
actively resist change. Every analytical table includes a Structural Competitor
column that asks -- what does this configuration defend, and is that defense
load-bearing? Some defenses are legitimate and expensive to change. Some are
accidental and should be trivial to close. Both kinds need naming.

Each phase closes with a multi-condition gate. Assert the gate only when every
□ condition is satisfied in the output above it.

---

PHASE 1 -- THREAT HYPOTHESES

Lead with the two access patterns most likely to be exploited by a legitimate
user with broad permissions. These are hypotheses about abuse paths, not
descriptions of what exists.

H1: [Specific role + vector] -- [Abuse path] -- [Why the current model creates this]
    Confirms if: [specific role matrix or escalation table evidence]
    Refutes if: [specific control found correctly configured]

H2: [Same structure]

Add H3+ for any additional plausible abuse path.

━━━ PHASE 1 COMPLETION GATE ━━━
Assert PHASE 1 COMPLETE only when ALL conditions are satisfied:
  □ >=2 hypotheses with H-labels
  □ Each names a specific role AND a specific vector or field
  □ Each states confirming evidence and refuting evidence
  □ No tables built

PHASE 1 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 2 -- FIELD-LEVEL AND SCOPE EVIDENCE (Structural Competitor Lens)

Examine FLS and record scope through the lens of H1 and H2. For each row,
ask: what does this configuration defend, and is that defense legitimate?

TABLE 1 -- Field-Level Security by Role
Columns: Field | Default | Role | FLS Override | Gap ID | H-Flag |
Structural Competitor: What does this configuration defend -- legitimate or accidental?

Instructions:
- Start with fields most relevant to H1 and H2
- Legitimate defense example: "AccountNumber FLS restricts CS read because
  billing disputes require field-level audit -- widening creates fraud risk"
- Accidental defense example: "CasePriority readable by all roles because FLS
  was never configured -- the default holds by inertia, not by design"
- Label each Structural Competitor entry: "Legitimate: [dependency]" or
  "Accidental: [no documented design reason]"
- Assign Gap IDs with first occurrence for any Accidental or Missing restriction
- H-Flag: tie to H1/H2 or "N/A -- [reason]"

TABLE 2 -- Record Access Scope by Role
Columns: Role | Scope | Enforcement | Gap ID | H-Flag |
Structural Competitor: What org process depends on this scope -- what breaks if tightened?

Instructions:
- Highest-scope role first; trace outward to most restricted
- For each scope: is it by design (documented mechanism) or by default (no explicit restriction)?
- Structural Competitor column: name the business process or workflow dependency
  that holds the scope in place; classify as "Designed" or "Default"
- Gap ID assigned at first occurrence for any Default scope that exceeds function

━━━ PHASE 2 COMPLETION GATE ━━━
Assert PHASE 2 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 1 covers all sensitive or role-differing fields
  □ TABLE 1 Structural Competitor: every row has a classification (Legitimate or Accidental)
  □ TABLE 1 Structural Competitor: >=1 row has a specific dependency named (not just a label)
  □ TABLE 2 covers all security roles; widest scope first
  □ TABLE 2 Structural Competitor: every row has Designed or Default classification
  □ All Phase 2 gaps assigned G-series IDs at first occurrence
  □ No Phase 3 tables built

PHASE 2 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 3 -- ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS

Start with the highest-privilege role. Trace downward to least-privileged.
Escalation paths often originate at the top; this ordering keeps the most
dangerous configurations in view before analyzing what they enable.

Carry all Phase 2 gap identifiers into Phase 3. Every G-series ID from Phase 2
must appear in at least one Phase 3 table row. Phase 2 FLS gaps that are not
escalation vectors still appear in TABLE 3 or TABLE 5 as scope contributors.

New gaps discovered here receive continuing G-series IDs.

TABLE 3 -- Role-Operation Matrix
Columns: Role | Create | Read | Update | Delete | Assign | Share |
Domain Ops | Gap ID (if over-permissive) | H-Flag

Order rows: highest privilege first. Mark over-permissive cells with Gap IDs.

TABLE 4 -- Privilege Escalation Paths
Columns: Vector | Path | Roles | Gap ID | H-Flag |
Structural Competitor: What legitimate workflow uses this same mechanism?

Cover all four vectors. Each is either a confirmed path or a cleared vector:
  1. Record reassignment
  2. Team promotion or membership elevation
  3. Sharing rule bypass
  4. Impersonation or delegation

Null-finding format (when no path found):
  Vector: [name] | Path: NONE | Control examined: [specific] | Why it holds: [reason]

For every confirmed path: populate the Structural Competitor column with the
legitimate workflow that uses the same mechanism. This is why the gap is
expensive to close. A path without a legitimate workflow analog should be
treated as higher risk -- there is no org dependency defending the gap.

TABLE 5 -- Sharing Rule Conflicts
Columns: Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag |
Structural Competitor: What access need does this widening legitimately serve?

TABLE 6 -- Team Membership Gaps
Columns: Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag

Null-finding if no team gap: name the teams examined; explain why membership is correct.

━━━ PHASE 3 COMPLETION GATE ━━━
Assert PHASE 3 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 3: all roles x all operations; highest-privilege role first
  □ TABLE 4: all 4 vectors (confirmed path or named null-finding)
  □ TABLE 4 Structural Competitor column: >=1 confirmed path row populated
  □ TABLE 5 complete with Structural Competitor column
  □ TABLE 6 complete (gap or null-finding with teams named)
  □ All Phase 2 G-IDs appear in >=1 Phase 3 table row

Then commit the source-locked gap inventory:

GAP INVENTORY (committed before Phase 3 closes):
[G-NN] -- [description] -- first seen: [TABLE X, row Y] -- [H1/H2/independent]

Every entry must include:
- The persistent G-ID
- A one-line description
- "first seen: [TABLE X, row Y]" -- the source binding is part of the record
- H-connection: which hypothesis it addresses, or "independent" if none

This inventory is final. Source provenance is locked at commit time.

  □ Inventory committed; every entry has G-ID + description + source + H-connection
  □ No Phase 4 content written yet

PHASE 3 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 4 -- ADVERSARIAL ASSESSMENT AND REMEDIATION

4a. Hypothesis Verdicts
For each H1, H2, ...:
  Verdict: Confirmed / Refuted / Modified
  Resolving evidence: [table name, row]
  Structural competitor finding: [what org dependency was or wasn't defending this gap]

4b. Null-Finding Accountability
For any table with no gap found: name controls examined; one sentence per null result.

4c. Remediation -- Addressing the Structural Competitor
For each gap, the fix must name both the technical action and the org resistance:
  [G-ID] | Risk: H/M/L | Fix: [specific: role + field + operation]
  Resistance: [what workflow, habit, or dependency will push back on this fix]

4d. TABLE 7 -- Risk-Ranked Summary
Columns: Gap ID | Description | Risk | Justification |
Phase Origin [P3 | P2: T#/row -> T#/row -> INV/G-NN -> T7/rN] |
Competitor Resistance (High/Medium/Low)

Phase Origin column:
- Phase 3-origin gaps: "P3"
- Phase 2-origin gaps: inline four-location chain in this column (not in Justification):
    "P2: T1/[field] -> T[N]/r[N] -> INV/G-[NN] -> T7/r[N]"
  The Structural Competitor column already names what defends the gap; the
  Phase Origin column names where it was discovered. Both are first-class columns.

Competitor Resistance column:
- Rate how hard the gap is to close given legitimate org dependencies
- High: a core workflow depends on the misconfiguration
- Medium: a non-critical workflow benefits from it
- Low: no legitimate dependency; gap persists by default only

Closing: Name the single gap where Competitor Resistance is highest -- the
fix that is technically obvious but organizationally expensive.

━━━ PHASE 4 COMPLETION GATE ━━━
Assert PHASE 4 COMPLETE only when ALL conditions are satisfied:
  □ All hypotheses resolved with table/row citation and structural competitor finding
  □ All null-finding sections name specific controls + one-sentence justification
  □ All remediations name role + field + operation AND the org resistance
  □ TABLE 7 contains only G-IDs from the inventory
  □ Phase Origin column populated for every row; Phase 2-origin gaps show inline chain
  □ Competitor Resistance column populated for every row
  □ Closing statement names the highest-resistance gap
  □ No new G-IDs introduced in Phase 4

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## Variation Summary

| ID | Axis / Axes | Core Bet |
|----|-------------|----------|
| V-01 | Lifecycle emphasis: gate-centric with C-21/C-22/C-23 as primary structure | When all three new mechanisms are embedded in the gate scaffolding itself, compliance is mechanical and forward-assembling rather than requiring Phase 4 retrospective work |
| V-02 | Role sequence / output format: field-centric discovery with forward origin tagging | Tagging Phase 2 gaps with "(P2)" suffix at discovery makes C-23 a propagation operation rather than a classification operation -- TABLE 7 Phase Origin column reads from pre-tagged data |
| V-03 | Output format: compressed scaffolding | Structural mechanisms survive compression when stated precisely and once; compression reveals which requirements are load-bearing vs. decorative |
| V-04 | Conversational register + column-bound inertia (R6 V-04 fixed) + C-21/C-22/C-23 | Second-person voice can carry full structural compliance when inertia is column-bound per row rather than a post-table section selecting one interesting case |
| V-05 | Adversarial-first + Structural Competitor inertia + C-21/C-22/C-23 upgrade | R6 V-05 upgraded: explicit Phase 3 carry-forward fixes the C-20 partial; gate checklists, source-locked inventory, and inline origin chain complete the three new criteria while preserving the adversarial framing's strength |
