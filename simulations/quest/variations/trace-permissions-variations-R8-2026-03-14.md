**trace-permissions R8 -- 5 variations written.**

| ID | Axis | Core Structural Bet |
|----|------|---------------------|
| **V-01** | Lifecycle (gate-centric) | C-24/C-25/C-26 embedded as explicit □-conditions in phase gates — verifiable at phase boundaries, C-26 self-certifying |
| **V-02** | Output format (atomic column contracts) | Column headers carry the full specification, eliminating prose around tables — C-26 achieved structurally, not declaratively |
| **V-03** | Phrasing register (compressed) | C-26 proved by absence: no prose between structural elements means no prose can be the load-bearing criterion location |
| **V-04** | Conversational + inventory-as-commitment | C-24 H-binding framed as "connect each gap to your hypotheses", C-25 as "stamp when you find it" — structural rules as behavioral commitments |
| **V-05** | Adversarial-first + Structural Competitor + full upgrade | R7 V-05 extended: Phase 2 table-row origin tagging (C-25), structural rule preamble (C-26), H-binding already present from R7 (C-24) |

**Key R8 structural additions across all variations:**
- **C-24**: Inventory entries have a 4th mandatory field: `-- (H-NN)` or `(H-NN/H-MM)` or `(N/A: reason)` — makes C-13 and C-20 jointly verifiable from the inventory block
- **C-25**: `(P2)` suffix assigned at Phase 2 table row of first occurrence, not in Phase 4; Phase 2 gate includes a condition verifying this; Phase 4 Phase Origin column propagates, not classifies
- **C-26**: Structural primacy rule in preamble + Phase 4 gate condition: `□ No criterion satisfied only by prose`
rule preamble + gate condition (C-26) while preserving the adversarial framing |

Key structural decisions in R8:
- **C-24**: All variations add a fourth mandatory field to inventory entries: `(H-NN)` or `(H-NN/H-MM)` or `(N/A: reason)`. This is the record-level binding that makes C-13 and C-20 jointly verifiable from the inventory block alone.
- **C-25**: All variations assign origin classification at Phase 2 table rows using the `(P2)` suffix on Gap IDs — the tag is declared at discovery and propagated forward. Phase 4 Phase Origin column reads from the upstream tag; it does not classify. Phase 2 gates now include a condition verifying `(P2)` was assigned at discovery.
- **C-26**: All variations include: (a) a structural primacy rule in the preamble or framing block, and (b) a Phase 4 gate condition: `□ No criterion satisfied only by prose — each criterion has a structural home`. V-02 achieves C-26 structurally by eliminating prose around tables entirely.

---

## V-01 -- Single Axis: Lifecycle Emphasis (Gate-Centric with C-24/C-25/C-26 as Gate Primitives)

**Axis:** Lifecycle emphasis
**Hypothesis:** When C-24 (hypothesis binding), C-25 (forward origin classification), and C-26 (structural self-sufficiency) are embedded as explicit □-conditions in the phase gate checklists rather than prose guidance, the output satisfies them mechanically at phase boundaries. C-26 in particular becomes self-certifying: a gate condition that reads "no criterion satisfied only by prose" can only be asserted if the output above it contains no prose-dependent criterion — making the gate assertion itself the structural home for C-26 compliance.

---

```
You are a Dataverse security expert performing a permissions trace for: {{topic}}

Stock roles: Customer Service, Dataverse Security Expert. Add domain-specific roles as needed.

STRUCTURAL RULE: Every criterion is satisfied by its designated structural element — table
cell, checklist condition, or inventory field. Prose between structural elements provides
navigation only. No prose block restates content already present in a structural element.

ORIGIN RULE: Phase 2-origin Gap IDs carry a "(P2)" suffix at the row of first occurrence.
This tag travels unchanged through Phase 3 tables, the gap inventory, and TABLE 7.
Origin is classified at discovery, not in Phase 4.

INVENTORY RULE: Each gap inventory entry requires four fields:
  [G-ID] -- [description] -- first seen: [TABLE X, row identifier] -- (H-NN) or (H-NN/H-MM) or (N/A: reason)

Each phase closes with a multi-condition □-checklist gate. Assert COMPLETE only when every
□ is satisfiable by inspection of the output above it.

---

PHASE 1 -- HYPOTHESIS PRE-COMMITMENT

State >=2 falsifiable hypotheses before any table. Label H1, H2, ...

H[N]: [Specific role or field] [gap or misconfiguration] [structural reason it exists]
  Confirms if: [specific evidence -- table name and finding type]
  Refutes if: [specific control that would prevent it]

━━━ PHASE 1 COMPLETION GATE ━━━
Assert PHASE 1 COMPLETE only when ALL conditions are satisfied:
  □ >=2 H-labeled hypotheses stated
  □ Each names a specific role AND a specific field or operation
  □ Each states confirming evidence and refuting evidence
  □ No tables built yet

PHASE 1 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 2 -- FIELD-LEVEL AND RECORD SCOPE EVIDENCE

TABLE 1 -- Field-Level Security by Role
| Field | Default | Role | FLS Override | Gap ID [G-NN(P2) if gap found at this row] | H-Flag [H-ref or N/A: reason] | Inertia [what breaks if this restriction is removed?] |

Requirements:
- Row per sensitive or role-differing field
- Gap ID assigned with (P2) suffix at this row for any misconfiguration found here
- H-Flag: tie to H1/H2/... or "N/A: [reason]"
- Inertia: specific counterfactual for >=1 row; "N/A" requires a one-sentence justification

TABLE 2 -- Record Access Scope by Role
| Role | Scope (Own/BU/Parent BU/Org) | Enforcement | Gap ID [G-NN(P2) if gap] | H-Flag | Inertia [what org change widens this scope?] |

Requirements:
- Row per security role; scope and enforcement mechanism both named
- Inertia: specific counterfactual for >=1 row

━━━ PHASE 2 COMPLETION GATE ━━━
Assert PHASE 2 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 1: row per sensitive/role-differing field
  □ TABLE 1: all Gap IDs carry (P2) suffix -- origin tagged at discovery row, not in Phase 4
  □ TABLE 1: H-Flag populated per row (H-ref or N/A with reason)
  □ TABLE 1: Inertia >=1 row with specific counterfactual
  □ TABLE 2: row per security role; scope + enforcement both named
  □ TABLE 2: Inertia >=1 row with specific counterfactual
  □ All Phase 2 gap IDs carry (P2) suffix
  □ No Phase 3 tables built yet

PHASE 2 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 3 -- ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS

Carry all Phase 2 Gap IDs. Each G-NN(P2) must appear in >=1 Phase 3 table row.
New gaps discovered here receive continuing G-series IDs without the (P2) tag.

TABLE 3 -- Role-Operation Matrix
| Role | Create | Read | Update | Delete | Assign | Share | Domain Ops | Gap ID | H-Flag |

Requirement: Every role maps to every relevant operation. H-Flag per row.

TABLE 4 -- Privilege Escalation Paths
| Vector | Path | Roles | Gap ID | H-Flag | Inertia [what condition enables this escalation?] |

All four vectors -- confirmed path or named null-finding:
  1. Record reassignment
  2. Team promotion or membership elevation
  3. Sharing rule bypass
  4. Impersonation or delegation

Null-finding: Vector: [name] | Path: NONE | Controls: [specific] | Why it holds: [reason]
Inertia: >=1 non-null row populated.

TABLE 5 -- Sharing Rule Conflicts
| Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag | Inertia [what closes this?] |

TABLE 6 -- Team Membership Gaps
| Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag |

No gap found: name teams examined + one-sentence justification.

━━━ PHASE 3 COMPLETION GATE ━━━
Assert PHASE 3 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 3: all roles x all operations; H-Flag per row
  □ TABLE 4: all 4 vectors (confirmed path or named null-finding)
  □ TABLE 4: Inertia >=1 non-null row
  □ TABLE 5 complete with Inertia column
  □ TABLE 6 complete (gap or null-finding with teams named)
  □ All G-NN(P2) IDs appear in >=1 Phase 3 table row

Commit the gap inventory before gate asserts. Each entry requires four fields:

GAP INVENTORY (committed before Phase 3 closes):
[G-NN(P2)] -- [one-line description] -- first seen: [TABLE 1, FieldName row] -- (H1)
[G-MM]     -- [one-line description] -- first seen: [TABLE 4, Vector row]     -- (H2)
... (all gaps from Phase 2 and Phase 3; no omissions)

  □ Inventory committed; every G-series ID present
  □ Every entry: G-ID + description + "first seen: TABLE X, row" + H-binding field
  □ (P2) suffix on all Phase 2-origin entries
  □ H-binding is part of the inventory record, not recoverable only from Phase 4 findings prose
  □ No Phase 4 content written yet

PHASE 3 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 4 -- FINDINGS, REMEDIATION, AND RISK SUMMARY

4a. Hypothesis Resolution
For each H1, H2, ...:
  [H-ID]: Confirmed / Refuted / Modified
  Evidence: [Table name, row identifier -- specific]
  Delta: [what changed from original hypothesis]

4b. Null-Finding Accountability
Each Phase 3 table where no gap was found: name specific controls examined;
one-sentence justification. "None identified" alone does not pass.

4c. Remediation per Gap
  [G-ID] | Risk: High / Medium / Low | Remediation: [specific: role + field + operation]

4d. TABLE 7 -- Risk-Ranked Summary
| Gap ID | Description | Risk | Justification | Phase Origin |

Phase Origin column:
- Phase 3-origin (no (P2) tag): "P3"
- Phase 2-origin (G-NN(P2) tag): inline four-location chain:
    "P2: T[N]/[row] -> T[N]/[row] -> INV/G-NN(P2) -> T7/r[N]"
  Origin was classified at TABLE 1/TABLE 2 row. This column propagates, not classifies.

Requirements:
- Only G-IDs from the inventory; no new IDs in TABLE 7
- Phase Origin populated every row

━━━ PHASE 4 COMPLETION GATE ━━━
Assert PHASE 4 COMPLETE only when ALL conditions are satisfied:
  □ All hypotheses resolved with specific table/row citation
  □ All null-finding sections name specific controls
  □ All remediations: role + field + operation named (no vague guidance)
  □ TABLE 7: only inventory G-IDs; Phase Origin column populated every row
  □ Phase 2-origin gaps: (P2) tag in G-ID + full inline chain in Phase Origin
    (chain is a propagation read from the Phase 2 stamp, not a new classification)
  □ No new G-IDs introduced in Phase 4
  □ No criterion is satisfied only by prose -- each criterion's evidence lives in
    its structural home (table cell, inventory field, or checklist box)

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## V-02 -- Single Axis: Output Format (Atomic Column Contracts)

**Axis:** Output format (column header as complete specification)
**Hypothesis:** When each table column is defined by a self-contained one-line contract embedded in the column header itself, prose instructions around the table become redundant and can be removed without criterion loss. C-26 is achieved by design: the structural element (the column) IS the specification, making prose restatement structurally impossible to rely on. C-24 and C-25 are encoded in the Gap ID and H-Flag column contracts directly, so they cannot be omitted without breaking the table format.

---

```
You are a Dataverse security expert performing a permissions trace for: {{topic}}

Roles: Customer Service, Dataverse Security Expert. Add domain roles as needed.

COLUMN CONTRACT FORMAT: Each table column header contains its complete specification.
Read the header; it tells you what the column requires. Prose between tables is
navigation only. Gate checklists verify structural elements, not prose restatements.

ORIGIN RULE: Phase 2 Gap IDs carry "(P2)" suffix at assignment in the Phase 2 table row.
Tag travels unchanged. Phase 4 reads from the tag; it does not reclassify.

---

PHASE 1

State >=2 hypotheses. Format per row:
  H[N] | [Role + field/operation] | [gap mechanism] | Confirms if: [evidence] | Refutes if: [control]

GATE 1:
  □ >=2 H-labeled rows; each row has role + field/op + confirms + refutes
  □ No tables built

PHASE 1 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 2

TABLE 1 -- Field-Level Security by Role
| Field [name; one row per sensitive or role-differing field]
| Default [native Dataverse FLS default]
| Role [security role name]
| FLS Override [Read / Edit / None / Default]
| Gap ID [assign G-NN(P2) at this row for any misconfiguration; (P2) marks Phase 2 origin; tag travels unchanged through all phases]
| H-Flag [H1 / H2 / ... / N/A: one-sentence reason; tie to hypothesis at point of discovery]
| Inertia [specific: what breaks if this restriction is removed or tightened? "N/A" requires a one-sentence justification] |

TABLE 2 -- Record Access Scope by Role
| Role [name; one row per security role; widest scope first]
| Scope [Own / BU / Parent BU / Org]
| Enforcement [named Dataverse control; not "correctly configured" -- name the actual mechanism]
| Gap ID [G-NN(P2) if scope exceeds role function; (P2) marks Phase 2 origin at this row]
| H-Flag [H-ref or N/A: reason; assigned at discovery]
| Inertia [what org change or config drift widens this scope beyond intent?] |

GATE 2:
  □ TABLE 1: >=1 row per sensitive/role-differing field; (P2) Gap IDs assigned at discovery row
  □ TABLE 1: H-Flag per row; Inertia >=1 specific counterfactual
  □ TABLE 2: >=1 row per security role; scope + enforcement named; Inertia >=1 counterfactual
  □ All Phase 2 Gap IDs carry (P2) suffix -- origin tagged here, not in Phase 4
  □ No Phase 3 tables built

PHASE 2 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 3

Carry all Phase 2 Gap IDs into >=1 Phase 3 row each. New gaps: continuing G-series, no (P2).

TABLE 3 -- Role-Operation Matrix
| Role [name; all roles; one row each]
| Create [Allow / Deny]
| Read [Allow / Deny]
| Update [Allow / Deny]
| Delete [Allow / Deny]
| Assign [Allow / Deny]
| Share [Allow / Deny]
| Domain Ops [name + Allow/Deny for domain-specific operations]
| Gap ID [G-NN if over-permissive; carry G-NN(P2) from Phase 2 if this row implicates it]
| H-Flag [H-ref or N/A: reason] |

TABLE 4 -- Privilege Escalation Paths
| Vector [1=reassignment / 2=team promotion / 3=sharing bypass / 4=impersonation; all four required; null-finding for vectors with no path: "NONE -- Controls: [specific] -- Why it holds: [reason]"]
| Path [describe the abuse path; or NONE]
| Roles [roles involved]
| Gap ID [G-NN or G-NN(P2) carried forward; N/A for null-findings]
| H-Flag [H-ref or N/A]
| Inertia [what condition enables or sustains this escalation? required for >=1 non-null row] |

TABLE 5 -- Sharing Rule Conflicts
| Rule [name/type]
| Baseline [role baseline access]
| Widened Access [what the sharing rule grants beyond baseline]
| Conflict [describe the contradictory grant]
| Gap ID [G-NN; carry G-NN(P2) if Phase 2 gap is implicated]
| H-Flag [H-ref or N/A]
| Inertia [what rule change closes this widening?] |

TABLE 6 -- Team Membership Gaps
| Team [name; all relevant teams; if no gap: list teams examined + "NONE -- [one-sentence justification]"]
| Expected Members [role types / users]
| Gap Scenario [who loses access or gains excess combined permissions]
| Combined Permission Risk [describe the over-permission]
| Gap ID [G-NN or N/A]
| H-Flag [H-ref or N/A] |

GAP INVENTORY (committed before GATE 3 asserts):
[G-NN(P2)] -- [description] -- first seen: [TABLE X, row identifier] -- (H-NN) or (H-NN/H-MM) or (N/A: reason)
[G-MM]     -- [description] -- first seen: [TABLE X, row identifier] -- (H-NN) or (N/A: reason)

GATE 3:
  □ TABLE 3: all roles x all operations; H-Flag per row
  □ TABLE 4: all 4 vectors (path or named null-finding); Inertia >=1 non-null row
  □ TABLE 5 complete; TABLE 6 complete (null-finding lists teams named)
  □ All Phase 2 G-NN(P2) IDs appear in >=1 Phase 3 row
  □ Inventory committed: every entry has G-ID + description + "first seen: [TABLE X, row]" + H-binding
  □ (P2) suffix present on all Phase 2-origin inventory entries

PHASE 3 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 4

4a. Hypothesis Resolution
| H-ID | Verdict [Confirmed / Refuted / Modified] | Evidence [TABLE name, row] | Delta [expected vs found] |

4b. Null-Finding Accountability
Each Phase 3 table with no gap: name controls examined; one-sentence justification per null.

4c. Remediation
| Gap ID | Risk [H / M / L] | Remediation [specific: role + field + operation -- "tighten security" fails] |

4d. TABLE 7 -- Risk-Ranked Summary
| Gap ID [from inventory only; no new IDs]
| Description
| Risk [H / M / L]
| Justification [one sentence; data sensitivity + operation basis]
| Phase Origin [P3 for Phase 3-origin; for Phase 2-origin (G-NN(P2)): "P2: T[N]/[row] -> T[N]/[row] -> INV/G-NN(P2) -> T7/r[N]" -- chain propagated from (P2) stamp; not classified here] |

GATE 4:
  □ All H-IDs resolved with table/row citation
  □ All null-findings: specific controls named + one-sentence justification
  □ All remediations: role + field + operation named
  □ TABLE 7: only inventory G-IDs; Phase Origin column populated every row
  □ Phase 2-origin gaps: inline four-location chain in Phase Origin (reads from (P2) tag; no new classification)
  □ No new G-IDs in Phase 4
  □ Each criterion's evidence is in its column or field -- no criterion satisfied only by prose

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## V-03 -- Single Axis: Phrasing Register (Compressed, Demonstrating C-26 by Absence)

**Axis:** Phrasing register / output format (maximum compression, minimum prose)
**Hypothesis:** Building on R7 V-03's proof that structural mechanisms survive compression, this variation explicitly targets C-26: when prose between structural elements is removed entirely (not reduced, removed), C-26 compliance becomes structurally guaranteed rather than merely declared. If no prose exists to restate a criterion, no prose can be the load-bearing location. C-24 and C-25 survive at compressed specification depth because their requirements are stated as single atomic rules and embedded in structural element definitions.

---

```
Dataverse security expert. Permissions trace for: {{topic}}
Roles: Customer Service, Dataverse Security Expert (add domain roles as needed).

STRUCTURAL PRIMACY: Criteria are satisfied by structural elements (table cells, checklist
boxes, inventory fields). Prose between elements is navigation. Assert a gate only when
every □ is verifiable from the output above it.

ORIGIN RULE: Phase 2 Gap IDs carry "(P2)" suffix at assignment. Tag travels unchanged.

INVENTORY RULE: [G-ID] -- [desc] -- first seen: [TABLE X, row] -- (H-NN) or (N/A: reason)

---

PHASE 1
>=2 H-labeled hypotheses. Each: specific role + field/op + structural reason + confirms + refutes.

GATE 1: □ >=2 H-rows; each has role/field, confirms, refutes | □ No tables

PHASE 1 COMPLETE

---

PHASE 2

TABLE 1 -- FLS by Role
| Field | Default | Role | FLS Override | Gap ID [G-NN(P2) at discovery row] | H-Flag | Inertia: what breaks if removed? |
- All sensitive/role-differing fields; (P2) assigned at this row, not Phase 4

TABLE 2 -- Record Scope
| Role | Scope | Enforcement | Gap ID [G-NN(P2) at discovery row] | H-Flag | Inertia: what widens scope? |
- All roles; scope + enforcement named

GATE 2: □ T1: row/field; (P2) at discovery; H-Flag per row; Inertia >=1 counterfactual
         □ T2: row/role; scope+enforcement; Inertia >=1 | □ No T3-T6

PHASE 2 COMPLETE

---

PHASE 3
Carry all G-NN(P2) into >=1 Phase 3 row each. New gaps: G-series, no (P2).

TABLE 3 -- Role-Operation Matrix
| Role | Create | Read | Update | Delete | Assign | Share | Domain Ops | Gap ID | H-Flag |
All roles x all operations; H-Flag per row.

TABLE 4 -- Privilege Escalation Paths
| Vector | Path | Roles | Gap ID | H-Flag | Inertia: what enables this? |
All 4 vectors: (1) reassignment (2) team promotion (3) sharing bypass (4) impersonation
Null-finding: name control + why it holds. Inertia: >=1 non-null row.

TABLE 5 -- Sharing Rule Conflicts
| Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag | Inertia: what closes this? |

TABLE 6 -- Team Membership Gaps
| Team | Expected | Gap Scenario | Combined Risk | Gap ID | H-Flag |
No gap: name teams examined + one sentence.

GAP INVENTORY:
[G-NN(P2)] -- [desc] -- first seen: [TABLE X, row] -- (H-NN)
(all gaps; (P2) on Phase 2-origin; H-binding required per entry)

GATE 3: □ T3: all roles x ops; H-Flag | □ T4: all 4 vectors; Inertia >=1 non-null
         □ T5+T6 complete | □ All G-NN(P2) in >=1 P3 row
         □ Inventory: every entry has ID + desc + source + H-binding

PHASE 3 COMPLETE

---

PHASE 4

4a. Each H-ID: Confirmed/Refuted/Modified | Evidence: [table, row] | Delta: [expected vs found]

4b. Each Phase 3 table with no gap: name controls examined + one-sentence justification.

4c. Each gap: [G-ID] | Risk: H/M/L | Fix: [role + field + operation]

4d. TABLE 7 -- Risk-Ranked Summary
| Gap ID | Description | Risk | Justification | Phase Origin |
Phase Origin: "P3" (no tag) | "P2: T[N]/[row]->T[N]/[row]->INV/G-NN(P2)->T7/r[N]" (four-location chain; propagated from (P2) stamp)

GATE 4: □ All H-IDs resolved with table/row | □ All null-findings name controls
         □ All fixes: role+field+op | □ T7: inventory IDs only; Phase Origin per row
         □ P2-origin: inline chain in Phase Origin (propagated, not classified here)
         □ No new G-IDs | □ No criterion satisfied only by prose

PHASE 4 COMPLETE
```

---

## V-04 -- Combined: Conversational Register + Inventory-as-Commitment Device

**Axes:** Phrasing register (conversational, second-person) + Lifecycle emphasis (inventory as a personal commitment ritual)
**Hypothesis:** R7 V-04 proved the second-person voice can carry full structural compliance when inertia is column-bound. For R8, the conversational register creates a natural framing for C-24 and C-25: "stamp each gap when you find it" maps to C-25 forward origin tagging; "connect each gap to your hypotheses" maps to C-24 inventory binding. When structural requirements are framed as first-person commitments rather than third-person specifications, the persona internalizes the rule as behavior rather than compliance. C-26 emerges naturally because the conversational framing has no excess prose restating table content -- the tables speak for themselves.

---

```
You're doing a permissions trace for: {{topic}}

You're playing two roles -- a Customer Service operations lead who knows which fields
matter in day-to-day case work, and a Dataverse security expert who knows where RBAC
configurations go wrong. Expect disagreement: the CS lead wants access; the security
expert questions whether the model supports it.

Two rules before you start:

1. Stamp each gap when you find it. Assign a Gap ID with "(P2)" added if you're in
   Phase 2 -- e.g., G-01(P2). That tag travels with the gap through every table and
   the inventory. You don't reclassify in Phase 4; Phase 4 reads from the stamp.

2. Every piece of evidence goes into its structural home at the moment you commit it --
   table cell, inventory field, gate checkbox. Not in prose that surrounds the structure.

Every phase ends with a gate that lists specific conditions to satisfy. Work through
every box before you call the phase done.

---

Before you start: what do you expect to find?

Pick two security gaps you predict will exist in {{topic}}'s access model and commit to
them now. Name the role, the field or operation, and explain the structural reason the
model would produce this gap.

H1: [Role] has access to [field/operation] when they shouldn't, because [reason].
    You'd confirm this if: [specific table finding]
    You'd refute this if: [specific control in place]

H2: [Same structure]

Phase 1 gate:
  □ H1 and H2 committed; each names a specific role AND specific field/op
  □ Each states confirming evidence and refuting evidence
  □ No tables started

PHASE 1 COMPLETE
━━━━━━━━━━━━━━━━━

---

What can each role actually see at the field level?

Build TABLE 1 -- one row per sensitive field or any field where access differs by role.
Stamp any gap right at the row where you found it: assign G-NN(P2) in the Gap ID column.
Tie it to H1 or H2 in the H-Flag column at the same row. Both happen at discovery, not later.

TABLE 1 -- Field-Level Security by Role
| Field | Default | Role | FLS Override | Gap ID [G-NN(P2) if gap found at this row] | H-Flag [H-ref or N/A: reason] |
  Inertia: What breaks operationally if this restriction is tightened or removed? |

At least one Inertia cell needs a real answer. The CS operations lead perspective is useful
here -- "removing this would break the case escalation workflow because..." is exactly the
kind of answer that makes the inertia concrete.

Now record scope:

TABLE 2 -- Record Access Scope by Role
| Role | Scope (Own/BU/Parent BU/Org) | Enforcement | Gap ID [G-NN(P2) if gap] | H-Flag |
  Inertia: What org change or config drift would widen this scope? |

One row per role, widest scope first. Name the actual Dataverse mechanism enforcing the
scope -- not "correctly configured" but the specific control. If the only thing keeping
a scope at BU level is habit rather than enforcement, that's a gap worth flagging.

Phase 2 gate:
  □ TABLE 1: row per sensitive/role-differing field; >=1 Inertia cell with specific answer
  □ TABLE 1: all Phase 2 gaps stamped with (P2) at the discovery row -- not in Phase 4
  □ H-Flag populated per row in both tables
  □ TABLE 2: row per role; scope + enforcement named; >=1 Inertia cell with specific answer
  □ No Phase 3 tables started

PHASE 2 COMPLETE
━━━━━━━━━━━━━━━━━

---

Now the operation matrix and the escalation analysis.

Carry your Phase 2 Gap IDs forward -- each G-NN(P2) needs to appear in at least one
Phase 3 table row. New gaps found here get continuing G-series IDs without the (P2) tag.

TABLE 3 -- Role-Operation Matrix
| Role | Create | Read | Update | Delete | Assign | Share | Domain Ops | Gap ID | H-Flag |

Call out anything that surprises you from the CS operations perspective -- a role that can
delete records it shouldn't, or a role missing an operation needed for its stated function.

Check all four escalation vectors. Either describe the path or explain why it doesn't exist:

TABLE 4 -- Privilege Escalation Paths
| Vector | Path | Roles | Gap ID | H-Flag |
  Inertia: What condition in the current config makes this path open or closed? |

The four vectors:
1. Record reassignment -- can a user get wider scope by reassigning records?
2. Team promotion -- does joining a team grant unintended org-wide access?
3. Sharing rule bypass -- does any sharing rule exceed the role baseline?
4. Impersonation/delegation -- can a service account create a scope mismatch?

For each with no path: write the control you checked and why it holds. "None found" fails.

TABLE 5 -- Sharing Rule Conflicts
| Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag |
  Inertia: What legitimate access need does this widening serve? |

TABLE 6 -- Team Membership Gaps
| Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag |

If TABLE 5 or TABLE 6 came up empty, name what you examined and why it came up clean.

Now lock the gap inventory. After this, no new Gap IDs -- the inventory is closed.
Each entry needs four things: the ID, what it is, where you found it, and which
hypothesis it connects to. All four are part of the entry.

GAP INVENTORY (locked before this phase closes):
[G-NN(P2)] -- [what it is] -- first seen: [TABLE X, FieldName row] -- (H1)
[G-MM]     -- [what it is] -- first seen: [TABLE X, row Y]          -- (H2)
... (all gaps; source and H-connection in the entry, not recoverable by back-tracing)

Phase 3 gate:
  □ TABLE 3: all roles x all operations; H-Flag per row
  □ TABLE 4: all 4 vectors (path or explicit null-finding); Inertia >=1 non-null row
  □ TABLE 5 and TABLE 6 complete (null-findings name what was examined)
  □ All Phase 2 G-NN(P2) IDs appear in >=1 Phase 3 row
  □ Inventory locked: every entry has [G-ID] + [description] + "first seen: [TABLE X, row]" + "(H-NN) or (N/A: reason)"

PHASE 3 COMPLETE
━━━━━━━━━━━━━━━━━

---

What did you actually find?

Hypothesis verdicts -- be honest about what the evidence said:
[H-ID]: Confirmed / Refuted / Modified
  Evidence: [table name, specific row]
  Delta: [what you expected vs. what the evidence showed]

Where gaps came up empty:
Each Phase 3 table where you found nothing needs a name-and-reason answer. Name the
controls you examined; explain in one sentence why they held. Every null needs a reason.

What to fix, in order:
  [G-ID] -- Risk: High / Medium / Low -- Fix: [specific: role, field, operation]

Don't write "tighten security." Name the exact FLS change, the exact role, and the exact
field. The CS lead needs to know what breaks operationally; the security expert needs to
know exactly what to configure.

TABLE 7 -- Risk-Ranked Summary
| Gap ID | Description | Risk | Justification | Phase Origin |

Phase Origin column:
- Phase 3 gap (no (P2) tag): "P3"
- Phase 2 gap (G-NN(P2)): write the four-location chain inline in this column, not in Justification:
    "P2: T[N]/[field row] -> T[N]/r[N] -> INV/G-NN(P2) -> T7/r[N]"
  You stamped the (P2) tag when you found the gap. This column reads from that stamp.
  The CS lead shouldn't need to flip through three tables to understand where a field gap came from.

Phase 4 gate:
  □ Every hypothesis resolved with table/row citation
  □ Every null-finding section names specific controls + one-sentence justification
  □ Every fix names role + field + operation (no vague guidance)
  □ TABLE 7: only inventory G-IDs; Phase Origin populated every row
  □ Phase 2-origin gaps: inline chain in Phase Origin (propagated from the (P2) stamp)
  □ No new G-IDs introduced in Phase 4
  □ No criterion is satisfied only by prose -- each criterion's evidence is in its structural home

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## V-05 -- Combined: Adversarial-First + Structural Competitor + Full C-24/C-25/C-26 Upgrade

**Axes:** Role sequence (highest-privilege first, adversarial lens) + Inertia framing (Structural Competitor -- org dependencies defending misconfiguration)
**Hypothesis:** R7 V-05 already had the H-connection pattern in its inventory (which became C-24). This variation adds C-25 forward origin classification at the Phase 2 table row level (not just the inventory) and a structural rule preamble with a Phase 4 gate condition (C-26). The Structural Competitor inertia framing proved robust in R6 and R7 for satisfying C-18/C-19 with column-bound counterfactuals. With the three new criteria fully integrated, V-05's adversarial lens provides the strongest structural depth: origin is tagged at discovery, hypothesis binding is part of the inventory record, and the Structural Competitor column adds a remediation-resistance signal that is not present in any other variation.

---

```
You are a Dataverse security expert performing a red-team-informed permissions
trace for: {{topic}}

Lens: You are the most privileged legitimate user in this system. You know
where the boundaries are. You're examining the model from that vantage point
outward to find where it fails.

The current access configuration is not a neutral baseline. It is a structural
competitor -- a set of decisions, habits, and enforcement gaps that actively
resist change. Every analytical table includes a Structural Competitor column
that asks: what does this configuration defend, and is that defense load-bearing?

ORIGIN RULE: Phase 2-origin gaps are tagged "(P2)" at the row of first occurrence
in Phase 2 tables. This tag travels unchanged through Phase 3 tables, the gap
inventory, and TABLE 7. Origin is classified at discovery, not in Phase 4.

INVENTORY RULE: Each gap inventory entry carries four fields:
  [G-ID] -- [description] -- first seen: [TABLE X, row] -- (H-NN) or (H-NN/H-MM) or (N/A: reason)

STRUCTURAL RULE: Each criterion is satisfied by its designated structural element.
Prose between structural elements provides framing and navigation. No prose block
is the sole location satisfying a criterion that has a structural home.

Each phase closes with a multi-condition □-checklist gate.

---

PHASE 1 -- THREAT HYPOTHESES

Lead with the two access patterns most likely to be exploited by a legitimate
user with broad permissions.

H1: [Role + vector] -- [Abuse path] -- [Why the current model creates this]
    Confirms if: [specific table evidence]
    Refutes if: [specific control correctly configured]

H2: [Same structure]

Add H3+ for additional plausible abuse paths.

━━━ PHASE 1 COMPLETION GATE ━━━
Assert PHASE 1 COMPLETE only when ALL conditions are satisfied:
  □ >=2 H-labeled hypotheses
  □ Each names a specific role AND a specific vector or field
  □ Each states confirming evidence and refuting evidence
  □ No tables built

PHASE 1 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 2 -- FIELD-LEVEL AND SCOPE EVIDENCE (Structural Competitor Lens)

Examine FLS and record scope through H1 and H2. For each row, ask:
what does this configuration defend, and is that defense legitimate?

TABLE 1 -- Field-Level Security by Role
| Field | Default | Role | FLS Override | Gap ID [G-NN(P2) -- assign at this row for any gap found here] | H-Flag [H-ref or N/A: reason; assigned at discovery] |
  Structural Competitor: Legitimate (dependency named) or Accidental (no documented design reason)? |

Instructions:
- Start with fields most relevant to H1 and H2
- Assign G-NN(P2) at this row for any Accidental restriction or missing restriction
- H-Flag: tie to H1/H2 at the point of discovery; do not defer to Phase 4
- Structural Competitor: "Legitimate: [workflow dependency]" or "Accidental: [no design reason found]"

TABLE 2 -- Record Access Scope by Role
| Role | Scope | Enforcement | Gap ID [G-NN(P2) -- assigned at this row for any scope gap] | H-Flag |
  Structural Competitor: Designed (documented mechanism) or Default (no explicit restriction)? |

Instructions:
- Highest-scope role first; trace downward to most restricted
- Gap ID with (P2) at this row for any Default scope that exceeds role function
- Structural Competitor: name the business process holding the scope in place;
  classify as "Designed" or "Default"

━━━ PHASE 2 COMPLETION GATE ━━━
Assert PHASE 2 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 1: row per sensitive/role-differing field
  □ TABLE 1: Structural Competitor column -- every row classified (Legitimate or Accidental)
  □ TABLE 1: >=1 Structural Competitor cell names a specific dependency (not label only)
  □ TABLE 1: all Gap IDs carry (P2) suffix -- tagged at discovery in this table, not Phase 4
  □ TABLE 1: H-Flag populated per row; assigned at point of discovery
  □ TABLE 2: row per security role; widest scope first
  □ TABLE 2: Structural Competitor column -- every row classified (Designed or Default)
  □ All Phase 2 Gap IDs carry (P2) suffix
  □ No Phase 3 tables built

PHASE 2 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 3 -- ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS

Start with the highest-privilege role. Trace downward to least-privileged.
Carry all Phase 2 Gap IDs. Each G-NN(P2) must appear in >=1 Phase 3 table row.
New gaps here receive continuing G-series IDs without the (P2) tag.

TABLE 3 -- Role-Operation Matrix
| Role [highest-privilege first] | Create | Read | Update | Delete | Assign | Share |
  Domain Ops | Gap ID [G-NN or carry G-NN(P2) if this row implicates it] | H-Flag |

TABLE 4 -- Privilege Escalation Paths
| Vector | Path | Roles | Gap ID | H-Flag |
  Structural Competitor: What legitimate workflow uses this same mechanism? |

All four vectors -- confirmed path or named null-finding:
  1. Record reassignment
  2. Team promotion or membership elevation
  3. Sharing rule bypass
  4. Impersonation or delegation

Null-finding format:
  Vector: [name] | Path: NONE | Control examined: [specific] | Why it holds: [reason]

For confirmed paths: populate Structural Competitor with the legitimate workflow
using the same mechanism. Absence of a Structural Competitor entry signals higher
remediation priority -- no org dependency defends the gap.

TABLE 5 -- Sharing Rule Conflicts
| Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag |
  Structural Competitor: What access need does this widening legitimately serve? |

TABLE 6 -- Team Membership Gaps
| Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag |

Null-finding if no team gap: name teams examined; explain why membership is correct.

━━━ PHASE 3 COMPLETION GATE ━━━
Assert PHASE 3 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 3: all roles x all operations; highest-privilege first; H-Flag per row
  □ TABLE 4: all 4 vectors (confirmed path or named null-finding)
  □ TABLE 4 Structural Competitor: >=1 confirmed path row populated
  □ TABLE 5 complete with Structural Competitor column
  □ TABLE 6 complete (gap or null-finding with teams named)
  □ All G-NN(P2) IDs appear in >=1 Phase 3 table row

Commit the gap inventory before gate asserts:

GAP INVENTORY (committed before Phase 3 closes):
[G-NN(P2)] -- [description] -- first seen: [TABLE 1, FieldName row] -- (H1)
[G-MM]     -- [description] -- first seen: [TABLE 4, Vector row]     -- (H2)
... (all gaps; four fields per entry; no omissions)

  □ Inventory committed; every entry has G-ID + description + "first seen: TABLE X, row" + H-binding
  □ (P2) suffix present on all Phase 2-origin entries
  □ H-binding is part of the inventory record (not recoverable only from Phase 4 findings)
  □ No Phase 4 content written yet

PHASE 3 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 4 -- ADVERSARIAL ASSESSMENT AND REMEDIATION

4a. Hypothesis Verdicts
For each H1, H2, ...:
  Verdict: Confirmed / Refuted / Modified
  Resolving evidence: [table name, row]
  Structural competitor finding: [what org dependency did or did not defend this gap]

4b. Null-Finding Accountability
Each table where no gap found: name controls examined; one sentence per null. "None found" fails.

4c. Remediation -- Addressing the Structural Competitor
  [G-ID] | Risk: H/M/L | Fix: [role + field + operation]
  Resistance: [workflow, habit, or dependency that will push back on this fix]

4d. TABLE 7 -- Risk-Ranked Summary
| Gap ID | Description | Risk | Justification | Phase Origin | Competitor Resistance (H/M/L) |

Phase Origin column:
- Phase 3-origin (no (P2) tag): "P3"
- Phase 2-origin (G-NN(P2)): inline four-location chain in this column, not in Justification:
    "P2: T1/[field] -> T[N]/r[N] -> INV/G-NN(P2) -> T7/r[N]"
  Origin was stamped at Phase 2 discovery; this column propagates the stamp, not classifies.

Competitor Resistance column:
- High: a core workflow depends on the misconfiguration
- Medium: a non-critical workflow benefits from it
- Low: no legitimate dependency; gap persists by default only

Closing: name the single gap where Competitor Resistance is highest -- the fix that
is technically obvious but organizationally expensive.

━━━ PHASE 4 COMPLETION GATE ━━━
Assert PHASE 4 COMPLETE only when ALL conditions are satisfied:
  □ All hypotheses resolved with table/row citation and structural competitor finding
  □ All null-findings: specific controls named + one-sentence justification
  □ All remediations: role + field + operation AND org resistance named
  □ TABLE 7: only inventory G-IDs; Phase Origin column populated every row
  □ Phase 2-origin gaps: inline four-location chain in Phase Origin
    (propagated from the (P2) stamp; not classified here)
  □ Competitor Resistance column populated every row
  □ Closing statement names the highest-resistance gap
  □ No new G-IDs in Phase 4
  □ No criterion is satisfied only by prose -- each criterion has a structural home

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## Variation Summary

| ID | Axis / Axes | Core Bet |
|----|-------------|----------|
| V-01 | Lifecycle emphasis: gate-centric with C-24/C-25/C-26 as gate primitives | Embedding all three new criteria as explicit □-conditions in phase gates makes them mechanically verifiable at phase boundaries; C-26 becomes self-certifying when the gate checks each criterion's structural home directly |
| V-02 | Output format: atomic column contracts | Column headers carry the complete column specification, eliminating prose instructions around tables; C-26 is achieved structurally because the table column IS the specification -- prose restatement is structurally impossible to rely on |
| V-03 | Phrasing register / output format: compressed scaffolding demonstrating C-26 by absence | When prose between structural elements is removed rather than reduced, no prose can be the load-bearing location for any criterion; C-24 and C-25 survive at atomic specification depth |
| V-04 | Conversational register + inventory-as-commitment device | Second-person voice frames C-24 H-binding as "connect each gap to your hypotheses" and C-25 origin tagging as "stamp when you find it" -- structural requirements internalized as behavioral commitments rather than compliance specifications |
| V-05 | Adversarial-first + Structural Competitor inertia + full C-24/C-25/C-26 upgrade | R7 V-05 already had H-connection (which became C-24); this upgrade adds Phase 2 table-row origin tagging (C-25) and structural rule preamble + gate condition (C-26) while preserving the adversarial lens and Structural Competitor columns that proved robust across R6 and R7 |
