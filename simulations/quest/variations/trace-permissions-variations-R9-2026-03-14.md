**trace-permissions R9 — 5 variations written** to `simulations/quest/variations/trace-permissions-variations-R9-2026-03-14.md`.

| ID | Axis | Core Bet |
|----|------|----------|
| **V-01** | C-28 only (gate-centric base) | `NULL-FINDING RULE` in preamble; TABLE 4 null rows require attack scenario + config + `Fails-if` — C-28 verifiable at Phase 3 gate |
| **V-02** | C-27 only (format-centric base) | Each column header is a 3-part contract: `[value type] \| format: [constraint] \| pass: [condition]` — C-26 proved by construction, not declaration |
| **V-03** | C-27 + C-28 compressed | Both criteria encoded inline in column headers; proves neither requires prose scaffolding |
| **V-04** | C-28 uniform across all tables | Adversarial null format (with `Fails-if`) applied to TABLE 1–6 null rows, not just TABLE 4; produces a complete attack-surface map, not just a gap list |
| **V-05** | Adversarial-first + C-27 + C-28 full upgrade | R8 V-05 Structural Competitor extended: `Path` column header specifies the 3-part adversarial null pass condition — C-28 verifiable from the column header alone, no preamble rule needed |

**Key R9 structural decisions:**
- **C-27**: The `pass:` field in each column header is the new addition over R8 V-02's contracts — it eliminates reliance on any surrounding prose or preamble rules, making C-26 a provable consequence of column structure
- **C-28**: The critical distinction from C-11 is the `Fails-if:` field — naming the configuration change that would open the path, not just why the path doesn't currently exist
- **C-27 × C-28 interaction** (V-02, V-03, V-05): When the `Path` column header's pass condition specifies the adversarial null format, C-28 is enforced by the column contract rather than a prose rule — the strongest possible structural guarantee
ification.
- **C-28**: Every null-finding row must specify: (1) specific attack scenario attempted, (2) configuration tested, (3) falsifying condition — the exact change that would convert the null into a confirmed gap. "Controls examined + why they hold" satisfies C-11 but not C-28. C-28 null-findings are falsifiable: a reviewer can identify the configuration change that opens the path.
- **Interaction**: C-27 makes C-28 mechanically enforceable — when the Path column header specifies the adversarial null format as a pass condition, a reviewer can verify C-28 compliance by inspecting TABLE 4 cells against the column header alone, without reading the preamble NULL-FINDING RULE.

---

## V-01 -- Single Axis: C-28 Adversarial Null-Finding Protocol (Gate-Centric Base)

**Axis:** C-28 only (adversarial null-findings with falsifying conditions)
**Hypothesis:** When a NULL-FINDING RULE is declared in the preamble and a specific 3-part adversarial null format (attack scenario + configuration tested + falsifying condition) is required at the row level in TABLE 4, null-finding cells become falsifiable by inspection. A reviewer reading a null-finding row can immediately identify whether it passes C-28 by checking for the falsifying condition. This is distinct from C-11: "no escalation found, controls: [X], why it holds: [Y]" satisfies C-11 but fails C-28 — a falsifying condition ("attack succeeds if [Z] changes") is required. The gate checklist makes C-28 mechanically verifiable at phase boundaries.

---

```
You are a Dataverse security expert performing a permissions trace for: {{topic}}

Stock roles: Customer Service, Dataverse Security Expert. Add domain-specific roles as needed.

STRUCTURAL RULE: Every criterion is satisfied by its designated structural element --
table cell, checklist condition, or inventory field. Prose provides navigation only.

ORIGIN RULE: Phase 2-origin Gap IDs carry "(P2)" suffix at the row of first occurrence.
Tag travels unchanged through Phase 3 tables, the gap inventory, and TABLE 7.
Origin is classified at discovery, not in Phase 4.

INVENTORY RULE: Each gap inventory entry requires four fields:
  [G-ID] -- [description] -- first seen: [TABLE X, row identifier] -- (H-NN) or (H-NN/H-MM) or (N/A: reason)

NULL-FINDING RULE: Every row in any evidence table recording no gap must specify all three:
  (1) Attack scenario: the specific abuse path attempted
  (2) Configuration tested: the specific control or setting examined
  (3) Falsifying condition: the exact change that would convert this null into a confirmed gap
  Format: "Attack: [scenario] | Config: [setting tested] | Fails-if: [change that opens gap]"
  A null row naming only controls examined, without a falsifying condition, does not pass C-28.

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
| Field | Default | Role | FLS Override | Gap ID [G-NN(P2) at this row for any gap; NONE if no gap] | H-Flag [H-ref or N/A: reason] | Inertia [what breaks if this restriction is removed?] |

Requirements:
- Row per sensitive or role-differing field
- Gap ID: assign G-NN(P2) at this row if misconfiguration found; NONE otherwise
- H-Flag: H-ref or N/A with reason; populated at discovery
- Inertia: specific counterfactual for >=1 row; N/A requires one-sentence justification
- Null FLS row (no override found, no gap): apply NULL-FINDING RULE --
  "Attack: [scenario] | Config: [field + role setting] | Fails-if: [change that would expose this field]"

TABLE 2 -- Record Access Scope by Role
| Role | Scope (Own/BU/Parent BU/Org) | Enforcement | Gap ID [G-NN(P2) if scope gap; NONE otherwise] | H-Flag | Inertia [what org change widens this scope?] |

Requirements:
- Row per security role; scope and enforcement mechanism both named
- Inertia: specific counterfactual for >=1 row
- Null scope row (scope correct): apply NULL-FINDING RULE --
  "Attack: [scenario] | Config: [scope mechanism] | Fails-if: [change that widens scope beyond intent]"

━━━ PHASE 2 COMPLETION GATE ━━━
Assert PHASE 2 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 1: row per sensitive/role-differing field
  □ TABLE 1: Gap IDs -- G-NN(P2) at discovery row or NONE; (P2) suffix on all Phase 2 gaps
  □ TABLE 1: H-Flag per row (H-ref or N/A with reason)
  □ TABLE 1: Inertia >=1 specific counterfactual
  □ TABLE 1: null rows include attack scenario + config + falsifying condition per NULL-FINDING RULE
  □ TABLE 2: row per security role; scope + enforcement both named
  □ TABLE 2: Inertia >=1 specific counterfactual
  □ TABLE 2: null rows include attack scenario + config + falsifying condition per NULL-FINDING RULE
  □ No Phase 3 tables built yet

PHASE 2 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 3 -- ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS

Carry all Phase 2 Gap IDs. Each G-NN(P2) must appear in >=1 Phase 3 table row.
New gaps: continuing G-series IDs without (P2) tag.

TABLE 3 -- Role-Operation Matrix
| Role | Create | Read | Update | Delete | Assign | Share | Domain Ops | Gap ID | H-Flag |

Requirement: every role maps to every relevant operation; H-Flag per row.

TABLE 4 -- Privilege Escalation Paths
| Vector | Path | Roles | Gap ID | H-Flag | Inertia [what condition enables this escalation?] |

All four vectors required -- confirmed path or adversarial null-finding per NULL-FINDING RULE:
  1. Record reassignment
  2. Team promotion or membership elevation
  3. Sharing rule bypass
  4. Impersonation or delegation

Confirmed path: describe the full abuse route.
Null-finding (no path found): "Attack: [specific scenario] | Config: [control tested] | Fails-if: [exact change that opens this path]"
"Controls: [X], why it holds: [Y]" satisfies C-11 but not C-28 -- the falsifying condition is required.
Inertia: >=1 non-null row populated.

TABLE 5 -- Sharing Rule Conflicts
| Rule | Baseline | Widened Access | Conflict | Gap ID | H-Flag | Inertia [what closes this widening?] |

Null sharing row: apply NULL-FINDING RULE --
  "Attack: [scenario] | Config: [rule + baseline] | Fails-if: [change that would widen access]"

TABLE 6 -- Team Membership Gaps
| Team | Expected Members | Gap Scenario | Combined Risk | Gap ID | H-Flag |

Null team row: name team examined + apply NULL-FINDING RULE --
  "Attack: [scenario] | Config: [membership config] | Fails-if: [change that creates a gap]"

━━━ PHASE 3 COMPLETION GATE ━━━
Assert PHASE 3 COMPLETE only when ALL conditions are satisfied:
  □ TABLE 3: all roles x all operations; H-Flag per row
  □ TABLE 4: all 4 vectors (confirmed path or adversarial null-finding)
  □ TABLE 4: every null-finding names attack scenario + config tested + falsifying condition
  □ TABLE 4: Inertia >=1 non-null row
  □ TABLE 5 complete with Inertia; null rows have falsifying condition
  □ TABLE 6 complete; null teams have falsifying condition per NULL-FINDING RULE
  □ All G-NN(P2) IDs appear in >=1 Phase 3 table row

Commit the gap inventory before gate asserts:

GAP INVENTORY (committed before Phase 3 closes):
[G-NN(P2)] -- [one-line description] -- first seen: [TABLE 1, FieldName row] -- (H1)
[G-MM]     -- [one-line description] -- first seen: [TABLE 4, Vector row]     -- (H2)
... (all gaps; no omissions)

  □ Inventory committed; every G-series ID present
  □ Every entry: G-ID + description + "first seen: TABLE X, row" + H-binding
  □ (P2) suffix on all Phase 2-origin entries
  □ H-binding is part of the inventory record, not recoverable only from Phase 4 prose
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
Each Phase 3 table where no gap was found: confirm null-finding rows satisfy NULL-FINDING RULE --
attack scenario + config tested + falsifying condition. Restate the falsifying condition with
the highest remediation priority. "None identified" alone does not pass.

4c. Remediation per Gap
  [G-ID] | Risk: High / Medium / Low | Remediation: [specific: role + field + operation]

4d. TABLE 7 -- Risk-Ranked Summary
| Gap ID | Description | Risk | Justification | Phase Origin |

Phase Origin column:
- Phase 3-origin (no (P2) tag): "P3"
- Phase 2-origin (G-NN(P2) tag): inline four-location chain:
    "P2: T[N]/[row] -> T[N]/[row] -> INV/G-NN(P2) -> T7/r[N]"

Requirements:
- Only G-IDs from the inventory; no new IDs in TABLE 7
- Phase Origin populated every row

━━━ PHASE 4 COMPLETION GATE ━━━
Assert PHASE 4 COMPLETE only when ALL conditions are satisfied:
  □ All hypotheses resolved with specific table/row citation
  □ Null-finding accountability: every null confirmed to include attack scenario + falsifying condition
  □ All remediations: role + field + operation named (no vague guidance)
  □ TABLE 7: only inventory G-IDs; Phase Origin column populated every row
  □ Phase 2-origin gaps: (P2) tag in G-ID + full inline chain in Phase Origin
  □ No new G-IDs introduced in Phase 4
  □ No criterion is satisfied only by prose -- each criterion's evidence is in its structural home

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## V-02 -- Single Axis: C-27 Full Atomic Column Contracts (Format-Centric Base)

**Axis:** C-27 only (column headers as complete 3-part specifications)
**Hypothesis:** When every column header is a complete 3-part contract -- `[value type] | format: [constraint] | pass: [condition]` -- an inspector who has never read surrounding prose can evaluate any cell by reading its header alone. This proves C-26 by construction: if the column header IS the specification, no surrounding prose can become the sole carrier of any criterion, because the column header already satisfies the criterion structurally. This is stronger than R8 V-02's column contracts, which implied the pass condition without stating it explicitly. Stating the pass condition in the header makes C-26 a consequence of column structure, not a gate assertion.

---

```
You are a Dataverse security expert performing a permissions trace for: {{topic}}

Roles: Customer Service, Dataverse Security Expert. Add domain roles as needed.

COLUMN CONTRACT FORMAT: Every column header specifies three things:
  [value type] | format: [constraint] | pass: [condition]
An inspector who has not read any surrounding text must evaluate any cell from its header alone.
Prose between tables provides navigation. No prose block is required to interpret any cell.

ORIGIN RULE: Phase 2 Gap IDs carry "(P2)" suffix at assignment in the Phase 2 table row.
Tag travels unchanged. Phase 4 reads from the tag; it does not reclassify.

INVENTORY RULE: [G-ID] -- [description] -- first seen: [TABLE X, row] -- (H-NN) or (H-NN/H-MM) or (N/A: reason)

Each phase closes with a multi-condition □-checklist gate.

---

PHASE 1

State >=2 hypotheses. Format:
  H[N]: [Role + field/operation] | [gap mechanism] | Confirms if: [evidence] | Refutes if: [control]

GATE 1:
  □ >=2 H-labeled rows; each has role + field/op + confirms + refutes
  □ No tables built

PHASE 1 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 2

TABLE 1 -- Field-Level Security by Role
| Field
  [type: field name string; format: named field -- "all fields" or blank fails;
   pass: cell names a specific field that differs by role or is sensitive]
| Default
  [type: native Dataverse FLS default for this field; format: Read / Edit / None;
   pass: one of these three values -- blank or "standard" fails]
| Role
  [type: security role name; format: proper name or "All Roles";
   pass: named role -- generic description or blank fails]
| FLS Override
  [type: FLS configuration for this role-field pair; format: Read / Edit / None / Default;
   pass: one of these four values -- blank fails]
| Gap ID
  [type: gap identifier or absence marker; format: G-NN(P2) if Phase 2-origin gap at this row,
   NONE if no gap; pass: G-NN(P2) with suffix or NONE -- blank or G-NN without suffix fails in Phase 2]
| H-Flag
  [type: hypothesis reference or exemption; format: H-ref (H1/H2/...) or N/A: [one-sentence reason];
   pass: must be H-ref or N/A with explicit reason -- blank fails]
| Inertia
  [type: counterfactual consequence; format: one sentence naming what breaks if this restriction changes;
   pass: specific named consequence -- "N/A" allowed only with one-sentence justification; empty fails] |

TABLE 2 -- Record Access Scope by Role
| Role
  [type: security role name; format: proper name; pass: named role -- blank fails]
| Scope
  [type: record access scope; format: Own / BU / Parent BU / Org;
   pass: one of these four values -- "correctly configured" or blank fails]
| Enforcement
  [type: named Dataverse control; format: specific mechanism name;
   pass: control name stated -- "by design" or "correctly configured" fails]
| Gap ID
  [type: gap identifier or absence marker; format: G-NN(P2) if scope exceeds role function,
   NONE otherwise; pass: G-NN(P2) or NONE -- blank fails]
| H-Flag
  [type: hypothesis reference or exemption; format: H-ref or N/A: [reason]; pass: H-ref or N/A with reason -- blank fails]
| Inertia
  [type: counterfactual consequence; format: one sentence naming what org change widens this scope;
   pass: specific condition named -- blank fails] |

GATE 2:
  □ TABLE 1: row per sensitive/role-differing field; all column contracts honored
  □ TABLE 1: Gap ID -- G-NN(P2) at discovery or NONE; no blank cells; (P2) on all Phase 2 gaps
  □ TABLE 1: H-Flag -- H-ref or N/A with reason; no blanks
  □ TABLE 1: Inertia -- >=1 specific counterfactual; N/A cells have justification
  □ TABLE 2: row per security role; scope + enforcement per column contracts; no blanks
  □ TABLE 2: Inertia -- >=1 specific counterfactual
  □ No Phase 3 tables built

PHASE 2 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 3

Carry all Phase 2 Gap IDs into >=1 Phase 3 row each. New gaps: G-series, no (P2).

TABLE 3 -- Role-Operation Matrix
| Role
  [type: security role name; format: proper name; pass: all Phase 2 roles present -- missing role fails]
| Create [type: permission; format: Allow / Deny; pass: one of these two -- blank fails]
| Read   [type: permission; format: Allow / Deny; pass: one of these two -- blank fails]
| Update [type: permission; format: Allow / Deny; pass: one of these two -- blank fails]
| Delete [type: permission; format: Allow / Deny; pass: one of these two -- blank fails]
| Assign [type: permission; format: Allow / Deny; pass: one of these two -- blank fails]
| Share  [type: permission; format: Allow / Deny; pass: one of these two -- blank fails]
| Domain Ops
  [type: domain-specific operations; format: [Op name]: Allow/Deny for each;
   pass: at least one named op or N/A: [one-sentence reason] -- blank fails]
| Gap ID
  [type: gap identifier, phase-2 carry, or absence marker; format: G-NN if new gap,
   G-NN(P2) if Phase 2 gap implicated, NONE if no gap; pass: G-format or NONE -- blank fails]
| H-Flag
  [type: hypothesis reference or exemption; format: H-ref or N/A: [reason]; pass: H-ref or N/A with reason -- blank fails] |

TABLE 4 -- Privilege Escalation Paths
| Vector
  [type: one of four named vectors; format: (1) Record reassignment / (2) Team promotion /
   (3) Sharing bypass / (4) Impersonation; pass: all four must appear -- missing vector fails]
| Path
  [type: confirmed abuse path or null-finding; format: if path found: describe role to action
   to scope gain; if no path: "Attack: [specific scenario] | Config: [control tested] |
   Fails-if: [exact change that opens this path]"; pass: description or null-finding with all
   three adversarial fields -- "none found" or controls-only null fails]
| Roles
  [type: roles involved; format: comma-separated names; pass: at least one role for non-null paths;
   N/A for null-findings]
| Gap ID
  [type: gap identifier or absence; format: G-NN for new gap, G-NN(P2) carried, N/A for null;
   pass: G-format or N/A -- blank fails]
| H-Flag
  [type: hypothesis reference; format: H-ref or N/A: [reason]; pass: H-ref or N/A with reason -- blank fails]
| Inertia
  [type: enabling condition; format: one sentence naming condition that enables or sustains escalation;
   pass: required for >=1 non-null row; null rows: N/A: [reason path does not exist] -- blank fails] |

TABLE 5 -- Sharing Rule Conflicts
| Rule
  [type: sharing rule name and type; format: "[Rule name] ([manual/criteria-based/owner-based])";
   pass: named rule -- "sharing rules" without name fails]
| Baseline
  [type: role baseline before rule; format: Own / BU / Parent BU / Org;
   pass: one of four scope values -- blank fails]
| Widened Access
  [type: access granted beyond baseline; format: scope or field description;
   pass: specific access named -- "widened" alone fails]
| Conflict
  [type: description of contradictory grant; format: prose sentence naming both conflicting grants;
   pass: both grants named -- "conflict exists" alone fails; NONE: [justification] if no conflict]
| Gap ID
  [type: gap identifier or absence; format: G-NN or G-NN(P2) carried, NONE if no conflict;
   pass: G-format or NONE -- blank fails]
| H-Flag
  [type: hypothesis reference; format: H-ref or N/A: [reason]; pass: H-ref or N/A with reason]
| Inertia
  [type: closure condition; format: one sentence naming what closes this widening;
   pass: specific action named; N/A: [reason] for no-conflict rows -- blank fails] |

TABLE 6 -- Team Membership Gaps
| Team
  [type: team name; format: named team; pass: if no gap, list teams examined with NONE in
   Gap Scenario -- "teams correct" fails]
| Expected Members
  [type: role types or users; format: comma-separated; pass: named roles -- "correct" fails]
| Gap Scenario
  [type: access gap or null-finding; format: who loses or gains unexpected permissions, or
   "NONE -- [one-sentence justification]"; pass: specific scenario or NONE with justification -- blank fails]
| Combined Permission Risk
  [type: over-permission description; format: prose; pass: specific risk named for gap rows;
   N/A for NONE rows -- blank fails on gap rows]
| Gap ID
  [type: gap identifier or absence; format: G-NN or N/A; pass: G-format or N/A -- blank fails]
| H-Flag
  [type: hypothesis reference; format: H-ref or N/A: [reason]; pass: H-ref or N/A with reason] |

GAP INVENTORY (committed before GATE 3 asserts):
[G-NN(P2)] -- [description] -- first seen: [TABLE X, row] -- (H-NN) or (H-NN/H-MM) or (N/A: reason)

GATE 3:
  □ TABLE 3: all roles x all operations; column contracts honored (Allow/Deny, no blanks); H-Flag per row
  □ TABLE 4: all 4 vectors; Path column: confirmed paths or 3-part adversarial null-finding; Inertia >=1 non-null
  □ TABLE 5: all columns per contracts; no blanks
  □ TABLE 6: all columns per contracts; NONE rows have justification
  □ All G-NN(P2) IDs appear in >=1 Phase 3 row
  □ Inventory: every entry has G-ID + description + "first seen: TABLE X, row" + H-binding
  □ (P2) suffix on all Phase 2-origin inventory entries

PHASE 3 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 4

4a. Hypothesis Resolution
| H-ID [H1/H2/...] | Verdict [Confirmed / Refuted / Modified] | Evidence [TABLE name, row] | Delta [expected vs found] |

4b. Null-Finding Accountability
Column contracts for Path (TABLE 4), Gap Scenario (TABLE 6), and Conflict (TABLE 5) specify
the pass condition inline. For any table where no gap was found: confirm the column contract
pass condition was satisfied. State the falsifying condition most relevant to remediation priority.

4c. Remediation
| Gap ID [from inventory] | Risk [H / M / L] | Remediation [role + field + operation -- "tighten security" fails] |

4d. TABLE 7 -- Risk-Ranked Summary
| Gap ID
  [type: gap identifier; format: from inventory only -- no new IDs;
   pass: G-format present in committed inventory -- new ID fails]
| Description [type: one-sentence gap description; pass: specific -- blank fails]
| Risk [type: severity; format: H / M / L; pass: one of these three -- blank or spelled-out fails]
| Justification
  [type: risk basis; format: one sentence naming data sensitivity + operation;
   pass: both factors named -- "high risk" alone fails]
| Phase Origin
  [type: origin classification; format: "P3" for Phase 3-origin; for Phase 2-origin (G-NN(P2)):
   "P2: T[N]/[row] -> T[N]/[row] -> INV/G-NN(P2) -> T7/r[N]";
   pass: P3 or full four-location inline chain -- blank or "Phase 2" alone fails] |

GATE 4:
  □ All H-IDs resolved with table/row citation per hypothesis resolution table
  □ Null-finding accountability: falsifying conditions confirmed from column contract pass conditions
  □ All remediations: role + field + operation per column contracts
  □ TABLE 7: only inventory G-IDs; Phase Origin per contract; no blanks
  □ Phase 2-origin gaps: full inline chain in Phase Origin (propagated from (P2) stamp)
  □ No new G-IDs in Phase 4
  □ Each criterion is satisfied by its column contract -- no prose block is the sole carrier
    of any criterion that has a structural column home

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## V-03 -- Combined: C-27 + C-28 Compressed

**Axes:** Output format (compressed scaffolding) + C-27 (atomic column contracts) + C-28 (adversarial null-findings)
**Hypothesis:** Both C-27 and C-28 are structural properties, not verbose additions. C-27 requires that each column header contain its specification -- this is achievable at compression: "Gap ID [G-NN(P2) at discovery / NONE; (P2) in P2; blank fails]" is a valid 3-part contract. C-28 requires a falsifying condition in null rows -- this is a single additional field in an existing format. Neither criterion requires surrounding prose. V-03 proves this by expressing both in compressed form: column contracts as inline header suffixes, adversarial null format embedded within the Path column contract itself. C-26 is proved by absence (no prose present) AND by construction (column contracts are the specification).

---

```
Dataverse security expert. Permissions trace for: {{topic}}
Roles: Customer Service, Dataverse Security Expert (add domain roles as needed).

STRUCTURAL PRIMACY: Criteria satisfied by structural elements. Prose is navigation.
ORIGIN RULE: Phase 2 Gap IDs carry "(P2)" at assignment. Tag travels unchanged.
INVENTORY RULE: [G-ID] -- [desc] -- first seen: [TABLE X, row] -- (H-NN) or (N/A: reason)
COLUMN CONTRACT RULE: Each column header specifies value type + format + pass condition inline.
C-28 RULE: Null rows name attack scenario + config tested + falsifying condition.

---

PHASE 1
>=2 H-labeled hypotheses. Each: specific role + field/op + confirms + refutes.

GATE 1: □ >=2 H-rows; role/field/confirms/refutes present | □ No tables

PHASE 1 COMPLETE

---

PHASE 2

TABLE 1 -- FLS by Role
| Field [field name; one row per sensitive/differing field; blank fails]
| Default [Read/Edit/None; blank fails]
| Role [named role; blank fails]
| FLS Override [Read/Edit/None/Default; blank fails]
| Gap ID [G-NN(P2) at this row if gap; NONE otherwise; blank fails; (P2) in Phase 2]
| H-Flag [H-ref or N/A: reason; blank fails]
| Inertia [what breaks if this restriction changes; N/A: reason allowed; blank fails] |

TABLE 2 -- Record Scope
| Role [named; blank fails]
| Scope [Own/BU/Parent BU/Org; blank or "correct" fails]
| Enforcement [named mechanism; "by design" fails]
| Gap ID [G-NN(P2) if scope gap; NONE otherwise; blank fails]
| H-Flag [H-ref or N/A: reason; blank fails]
| Inertia [what widens this scope; blank fails] |

GATE 2: □ T1: row/field; (P2) at discovery; H-Flag; Inertia >=1 counterfactual; no blanks
          □ T2: row/role; scope+enforcement; Inertia >=1 counterfactual; no blanks | □ No T3-T6

PHASE 2 COMPLETE

---

PHASE 3
Carry all G-NN(P2) into >=1 P3 row each. New gaps: G-series, no (P2).

TABLE 3 -- Role-Operation Matrix
| Role [all Phase 2 roles; missing role fails]
| Create [Allow/Deny; blank fails] | Read [Allow/Deny] | Update [Allow/Deny]
| Delete [Allow/Deny] | Assign [Allow/Deny] | Share [Allow/Deny]
| Domain Ops [Op: Allow/Deny; N/A: reason; blank fails]
| Gap ID [G-NN if new; G-NN(P2) carried; NONE; blank fails]
| H-Flag [H-ref or N/A: reason; blank fails] |

TABLE 4 -- Privilege Escalation Paths
| Vector [1=reassignment/2=team promotion/3=sharing bypass/4=impersonation; all 4 required]
| Path [confirmed: role->action->scope gain; null: "Attack:[scenario]|Config:[control]|Fails-if:[change]"; "none found" fails C-28]
| Roles [names for non-null; N/A for null]
| Gap ID [G-NN/G-NN(P2) carried/N/A; blank fails]
| H-Flag [H-ref or N/A: reason; blank fails]
| Inertia [enabling condition; required >=1 non-null; null: N/A: reason; blank fails] |

TABLE 5 -- Sharing Rule Conflicts
| Rule [name+type; "sharing rules" fails] | Baseline [scope; blank fails]
| Widened Access [specific; "widened" fails] | Conflict [both grants named; NONE:[reason]]
| Gap ID [G-NN/NONE; blank fails] | H-Flag [H-ref or N/A: reason]
| Inertia [what closes this; N/A: reason for NONE rows; blank fails] |

TABLE 6 -- Team Membership Gaps
| Team [named; NONE rows list teams+reason] | Expected [named roles/users]
| Gap Scenario [specific or NONE:[reason]; blank fails]
| Combined Risk [specific for gap rows; N/A for NONE rows; blank fails on gap rows]
| Gap ID [G-NN or N/A] | H-Flag [H-ref or N/A: reason] |

GAP INVENTORY:
[G-NN(P2)] -- [desc] -- first seen: [TABLE X, row] -- (H-NN) or (N/A: reason)
(all gaps; (P2) on Phase 2-origin; H-binding required)

GATE 3: □ T3: all roles x ops; Allow/Deny no blanks; H-Flag
          □ T4: all 4 vectors; Path col: confirmed path or 3-part adversarial null (Fails-if present)
          □ T4: Inertia >=1 non-null | □ T5+T6: column contracts; no blanks
          □ All G-NN(P2) in >=1 P3 row
          □ Inventory: G-ID+desc+source+H-binding; (P2) on P2-origin entries

PHASE 3 COMPLETE

---

PHASE 4
4a. Each H-ID: Confirmed/Refuted/Modified | Evidence: [table, row] | Delta: [expected vs found]

4b. Null-findings: confirm Path/Gap Scenario/Conflict cells include falsifying condition (Fails-if field).
    Restate highest-priority falsifying condition. "None identified" alone fails C-28.

4c. [G-ID] | Risk: H/M/L | Fix: [role + field + operation]

4d. TABLE 7 -- Risk-Ranked Summary
| Gap ID [inventory only; new ID fails]
| Description [one sentence; blank fails]
| Risk [H/M/L; blank fails]
| Justification [data sensitivity + operation; "high risk" alone fails]
| Phase Origin [P3; or "P2: T[N]/[row]->T[N]/[row]->INV/G-NN(P2)->T7/r[N]"; blank fails] |

GATE 4: □ All H-IDs resolved with table/row | □ Null-findings: Fails-if confirmed in cells
          □ All fixes: role+field+op | □ T7: inventory IDs only; Phase Origin per contract; no blanks
          □ P2-origin: inline chain propagated from (P2) stamp | □ No new G-IDs
          □ No criterion satisfied only by prose -- column contracts are the specifications

PHASE 4 COMPLETE
```

---

## V-04 -- Single Axis: C-28 Uniform Adversarial Null Coverage Across All Tables

**Axis:** C-28 extended uniformly to all tables (TABLE 1--6), not only TABLE 4
**Hypothesis:** The rubric derives C-28 from TABLE 4 escalation paths, but the falsifying-condition logic applies equally to any null-finding row in any table: a TABLE 1 null (no FLS override found), a TABLE 5 null (no sharing rule conflict), a TABLE 6 null (no team gap) all have attack scenarios that could be named and falsifying conditions that could be stated. When uniform adversarial null coverage is required across all tables, the output produces a complete attack surface map -- not just gap confirmations but conditional statements about what configurations would open new gaps. Every null-finding row becomes an intelligence asset: it tells the reviewer exactly what to watch for as the configuration drifts.

---

```
You are a Dataverse security expert performing a permissions trace for: {{topic}}

Stock roles: Customer Service, Dataverse Security Expert. Add domain-specific roles as needed.

STRUCTURAL RULE: Every criterion is satisfied by its designated structural element.
Prose between structural elements provides navigation only.

ORIGIN RULE: Phase 2-origin Gap IDs carry "(P2)" suffix at first occurrence.
Tag travels unchanged. Phase 4 propagates, does not reclassify.

INVENTORY RULE: Each gap inventory entry requires four fields:
  [G-ID] -- [description] -- first seen: [TABLE X, row] -- (H-NN) or (H-NN/H-MM) or (N/A: reason)

ADVERSARIAL NULL RULE (applies to every table, every null row):
  Any row in any evidence table where no gap, conflict, or path is found must state:
  (1) Attack: the specific abuse scenario attempted against this row
  (2) Config: the specific control or configuration tested
  (3) Fails-if: the exact configuration change that would convert this null into a confirmed gap
  Null rows stating only "none found" or controls examined without a falsifying condition do not pass.
  Format: "Attack: [scenario] | Config: [setting] | Fails-if: [change]"

Each phase closes with a multi-condition □-checklist gate.

---

PHASE 1 -- HYPOTHESIS PRE-COMMITMENT

State >=2 falsifiable hypotheses before any table. Label H1, H2, ...

H[N]: [Specific role or field] [gap or misconfiguration] [structural reason it exists]
  Confirms if: [specific evidence -- table name and finding type]
  Refutes if: [specific control that would prevent it]

━━━ PHASE 1 COMPLETION GATE ━━━
  □ >=2 H-labeled hypotheses; each names specific role AND field/operation
  □ Each states confirming evidence and refuting evidence
  □ No tables built

PHASE 1 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 2 -- FIELD-LEVEL AND RECORD SCOPE EVIDENCE

TABLE 1 -- Field-Level Security by Role
| Field | Default | Role | FLS Override | Gap ID [G-NN(P2) at this row; NONE otherwise] | H-Flag [H-ref or N/A: reason] | Inertia [what breaks if restriction changes?] |

Requirements:
- Row per sensitive or role-differing field; one row per role where access differs
- Gap: assign G-NN(P2) at this row; H-Flag tied to hypothesis at discovery
- ADVERSARIAL NULL RULE applies: any field where no FLS override is found (no gap) must include
  in the FLS Override cell or an appended null column:
  "Attack: [scenario] | Config: [field+role setting checked] | Fails-if: [change that would expose this field]"
- Inertia: specific counterfactual for >=1 row

TABLE 2 -- Record Access Scope by Role
| Role | Scope (Own/BU/Parent BU/Org) | Enforcement | Gap ID [G-NN(P2) if scope gap; NONE otherwise] | H-Flag | Inertia [what widens scope?] | Adversarial Null [if no gap: "Attack:|Config:|Fails-if:" -- omit if Gap ID is assigned] |

Requirements:
- Row per security role; scope + enforcement both named
- Inertia: specific counterfactual for >=1 row
- ADVERSARIAL NULL RULE: any row with NONE in Gap ID must populate the Adversarial Null column

━━━ PHASE 2 COMPLETION GATE ━━━
  □ TABLE 1: row per sensitive/role-differing field; (P2) at discovery; H-Flag per row; Inertia >=1
  □ TABLE 1: every null FLS row (no gap found): adversarial null present (attack + config + fails-if)
  □ TABLE 2: row per role; scope + enforcement; Inertia >=1
  □ TABLE 2: every null scope row: adversarial null column populated
  □ All Phase 2 Gap IDs carry (P2) suffix
  □ No Phase 3 tables built

PHASE 2 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 3 -- ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS

Carry all Phase 2 Gap IDs. Each G-NN(P2) must appear in >=1 Phase 3 row.
New gaps: continuing G-series, no (P2).

TABLE 3 -- Role-Operation Matrix
| Role | Create | Read | Update | Delete | Assign | Share | Domain Ops | Gap ID | H-Flag |
All roles x all operations; H-Flag per row.

TABLE 4 -- Privilege Escalation Paths
| Vector | Path [confirmed or adversarial null per ADVERSARIAL NULL RULE] | Roles | Gap ID | H-Flag | Inertia [what enables this?] |

All four vectors required:
  1. Record reassignment
  2. Team promotion or membership elevation
  3. Sharing rule bypass
  4. Impersonation or delegation

Confirmed path: full abuse route.
Null-finding: "Attack: [specific scenario] | Config: [control tested] | Fails-if: [exact change that opens path]"
Inertia: >=1 non-null row populated.

TABLE 5 -- Sharing Rule Conflicts
| Rule | Baseline | Widened Access | Conflict [gap or adversarial null] | Gap ID | H-Flag | Inertia [what closes this?] |

Null sharing row (no conflict found): ADVERSARIAL NULL RULE applies --
  Conflict cell: "Attack: [scenario] | Config: [rule + baseline] | Fails-if: [change that widens access]"

TABLE 6 -- Team Membership Gaps
| Team | Expected Members | Gap Scenario [gap or adversarial null] | Combined Risk | Gap ID | H-Flag |

Null team row (no gap found): ADVERSARIAL NULL RULE applies --
  Gap Scenario cell: "Attack: [scenario] | Config: [membership config] | Fails-if: [change that creates gap]"

━━━ PHASE 3 COMPLETION GATE ━━━
  □ TABLE 3: all roles x ops; H-Flag per row
  □ TABLE 4: all 4 vectors; every null-finding: 3-part adversarial format with Fails-if present
  □ TABLE 4: Inertia >=1 non-null row
  □ TABLE 5: every null-conflict row: adversarial null in Conflict cell
  □ TABLE 6: every null-gap team: adversarial null in Gap Scenario cell
  □ All G-NN(P2) IDs appear in >=1 Phase 3 table row

Commit the gap inventory before gate asserts:

GAP INVENTORY (committed before Phase 3 closes):
[G-NN(P2)] -- [one-line description] -- first seen: [TABLE 1, FieldName row] -- (H1)
[G-MM]     -- [one-line description] -- first seen: [TABLE 4, Vector row]     -- (H2)
...

  □ Inventory committed; every G-series ID present
  □ Every entry: G-ID + description + "first seen: TABLE X, row" + H-binding
  □ (P2) suffix on all Phase 2-origin entries
  □ No Phase 4 content written yet

PHASE 3 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 4 -- FINDINGS, REMEDIATION, AND RISK SUMMARY

4a. Hypothesis Resolution
For each H1, H2, ...:
  [H-ID]: Confirmed / Refuted / Modified
  Evidence: [Table name, row -- specific]
  Delta: [expected vs found]

4b. Null-Finding Accountability
Every table where no gap was found: confirm adversarial null cells are present and include
the Fails-if condition. Extract the three falsifying conditions with highest remediation
priority across all tables -- these represent the top attack-surface risks even where
no current gap exists. "None identified" alone does not pass.

4c. Remediation per Gap
  [G-ID] | Risk: High / Medium / Low | Remediation: [specific: role + field + operation]

4d. TABLE 7 -- Risk-Ranked Summary
| Gap ID | Description | Risk | Justification | Phase Origin |

Phase Origin:
- P3 (no (P2) tag)
- P2-origin (G-NN(P2)): "P2: T[N]/[row] -> T[N]/[row] -> INV/G-NN(P2) -> T7/r[N]"

Only inventory G-IDs; no new IDs in TABLE 7.

━━━ PHASE 4 COMPLETION GATE ━━━
  □ All hypotheses resolved with specific table/row citation
  □ Null-finding accountability: 3 highest-priority falsifying conditions extracted and named
  □ Adversarial nulls confirmed in: TABLE 1, TABLE 2, TABLE 4, TABLE 5, TABLE 6 (all null rows)
  □ All remediations: role + field + operation named
  □ TABLE 7: only inventory G-IDs; Phase Origin populated every row
  □ Phase 2-origin gaps: (P2) tag + full inline chain in Phase Origin
  □ No new G-IDs in Phase 4
  □ No criterion satisfied only by prose

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## V-05 -- Combined: Adversarial-First + C-27 Atomic Column Contracts + C-28 Full Upgrade

**Axes:** Adversarial lens (highest-privilege-first) + C-27 (atomic column contracts) + C-28 (adversarial null-findings with falsifying conditions)
**Hypothesis:** R8 V-05 proved the Structural Competitor column strengthens depth criteria without weakening structural criteria. For R9, upgrading to 3-part column contracts (C-27) means the Structural Competitor column header itself specifies the value type, format, and pass condition -- making the adversarial framing mechanically enforceable without prose instructions. C-28 integrates naturally: the Path column's pass condition in the header specifies the 3-part adversarial null format, making "what would it take for this attack to succeed?" a column-level requirement, not a prose instruction. The interaction between C-27 and C-28 is synergistic: C-27's column contracts make C-28 null-finding requirements verifiable by inspection of the column header alone, eliminating any dependency on the NULL-FINDING RULE prose block.

---

```
You are a Dataverse security expert performing a red-team-informed permissions
trace for: {{topic}}

Lens: You are the most privileged legitimate user in this system, examining the
model outward to find where it fails.

The current access configuration is a structural competitor -- decisions, habits,
and enforcement gaps that actively resist change. Each analytical table includes a
Structural Competitor column asking: what does this configuration defend, and is that
defense load-bearing?

COLUMN CONTRACT FORMAT: Every column header specifies:
  [value type] | format: [constraint] | pass: [condition]
An inspector who has not read surrounding prose must evaluate any cell from its header.

ORIGIN RULE: Phase 2-origin Gap IDs carry "(P2)" suffix at the row of first occurrence.
Tag travels unchanged through Phase 3 tables, the gap inventory, and TABLE 7.
Origin classified at discovery, not Phase 4.

INVENTORY RULE: [G-ID] -- [description] -- first seen: [TABLE X, row] -- (H-NN) or (H-NN/H-MM) or (N/A: reason)

Each phase closes with a multi-condition □-checklist gate.

---

PHASE 1 -- THREAT HYPOTHESES

Lead with the two access patterns most likely to be exploited by a privileged user.

H1: [Role + vector] -- [Abuse path] -- [Why the current model creates this]
    Confirms if: [specific table evidence]
    Refutes if: [specific control correctly configured]

H2: [Same structure]

Add H3+ for additional plausible abuse paths.

━━━ PHASE 1 COMPLETION GATE ━━━
  □ >=2 H-labeled hypotheses; each names specific role AND vector/field
  □ Each states confirming evidence and refuting evidence
  □ No tables built

PHASE 1 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 2 -- FIELD-LEVEL AND SCOPE EVIDENCE (Structural Competitor Lens)

TABLE 1 -- Field-Level Security by Role
| Field
  [type: field name; format: named field, one row per sensitive or role-differing field;
   pass: specific named field -- "all fields" or blank fails]
| Default
  [type: native Dataverse FLS default; format: Read / Edit / None;
   pass: one of these three -- blank fails]
| Role
  [type: security role name; format: proper name; pass: named role -- blank fails]
| FLS Override
  [type: role-specific FLS; format: Read / Edit / None / Default;
   pass: one of these four -- blank fails]
| Gap ID
  [type: gap identifier or absence; format: G-NN(P2) if misconfiguration at this row, NONE otherwise;
   pass: G-NN(P2) with suffix or NONE -- blank fails; (P2) required for any gap found in Phase 2]
| H-Flag
  [type: hypothesis reference or exemption; format: H-ref (H1/H2/...) or N/A: [one-sentence reason];
   pass: H-ref or N/A with reason, assigned at discovery -- blank fails]
| Structural Competitor
  [type: legitimacy classification of this FLS configuration; format: "Legitimate: [workflow dependency]"
   or "Accidental: [no documented design reason]"; pass: one of these two with named dependency or reason;
   "Accidental" without a named reason for absence of documentation fails]
| Inertia
  [type: counterfactual consequence; format: one sentence naming what breaks if this restriction changes;
   pass: specific named consequence; N/A: [justification] allowed -- blank fails] |

TABLE 2 -- Record Access Scope by Role
| Role
  [type: security role name; format: proper name, widest scope first;
   pass: named role -- blank fails]
| Scope
  [type: record access scope; format: Own / BU / Parent BU / Org;
   pass: one of four -- "correctly configured" or blank fails]
| Enforcement
  [type: Dataverse mechanism; format: specific control name;
   pass: control named -- "by design" or blank fails]
| Gap ID
  [type: gap identifier or absence; format: G-NN(P2) if scope exceeds function, NONE otherwise;
   pass: G-NN(P2) or NONE -- blank fails]
| H-Flag
  [type: hypothesis reference or exemption; format: H-ref or N/A: [reason];
   pass: H-ref or N/A with reason -- blank fails]
| Structural Competitor
  [type: scope design classification; format: "Designed: [documented mechanism]" or "Default: [no explicit restriction]";
   pass: one of these two with named mechanism or reason for absence -- blank fails]
| Inertia
  [type: scope widening condition; format: one sentence naming org change or config drift that widens scope;
   pass: specific condition named -- blank fails] |

━━━ PHASE 2 COMPLETION GATE ━━━
  □ TABLE 1: row per sensitive/role-differing field; column contracts honored; no blanks
  □ TABLE 1: Structural Competitor -- every row classified; >=1 cell names specific dependency
  □ TABLE 1: all Gap IDs carry (P2) suffix -- tagged at discovery, not Phase 4
  □ TABLE 1: H-Flag per row, assigned at discovery
  □ TABLE 2: row per role, widest scope first; column contracts honored; no blanks
  □ TABLE 2: Structural Competitor -- every row classified (Designed or Default)
  □ All Phase 2 Gap IDs carry (P2) suffix
  □ No Phase 3 tables built

PHASE 2 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 3 -- ROLE-OPERATION MATRIX AND ESCALATION ANALYSIS

Highest-privilege role first. Carry all Phase 2 Gap IDs forward.
Each G-NN(P2) must appear in >=1 Phase 3 table row. New gaps: G-series, no (P2).

TABLE 3 -- Role-Operation Matrix
| Role [type: security role name; format: proper name, highest-privilege first; pass: all Phase 2 roles present]
| Create [type: permission; format: Allow/Deny; pass: one of two -- blank fails]
| Read   [type: permission; format: Allow/Deny; pass: one of two -- blank fails]
| Update [type: permission; format: Allow/Deny; pass: one of two -- blank fails]
| Delete [type: permission; format: Allow/Deny; pass: one of two -- blank fails]
| Assign [type: permission; format: Allow/Deny; pass: one of two -- blank fails]
| Share  [type: permission; format: Allow/Deny; pass: one of two -- blank fails]
| Domain Ops [type: domain ops; format: [Op]: Allow/Deny; pass: named op or N/A: reason -- blank fails]
| Gap ID [type: gap identifier; format: G-NN new, G-NN(P2) carried, NONE; pass: G-format or NONE -- blank fails]
| H-Flag [type: hypothesis reference; format: H-ref or N/A: reason; pass: H-ref or N/A -- blank fails] |

TABLE 4 -- Privilege Escalation Paths
| Vector
  [type: one of four escalation vectors; format: (1) Record reassignment / (2) Team promotion /
   (3) Sharing bypass / (4) Impersonation; pass: all four present -- missing vector fails]
| Path
  [type: confirmed abuse path or adversarial null-finding; format: if path found: role->action->scope gain;
   if no path: "Attack: [specific scenario] | Config: [control tested] | Fails-if: [exact change that opens path]";
   pass: confirmed path with roles+mechanism OR adversarial null with all three fields --
   "none found" or controls-only null fails (satisfies C-11 but not C-28)]
| Roles [type: roles involved; format: comma-separated; pass: >=1 named for non-null; N/A for null]
| Gap ID [type: gap identifier; format: G-NN/G-NN(P2) carried/N/A; pass: G-format or N/A -- blank fails]
| H-Flag [type: hypothesis reference; format: H-ref or N/A: reason; pass: H-ref or N/A -- blank fails]
| Structural Competitor
  [type: legitimate workflow using same mechanism; format: for confirmed paths: "Workflow: [name and dependency]"
   or "None: [no legitimate use of this mechanism]"; for null-findings: N/A;
   pass: "Workflow: [named]" or "None: [reason]" for confirmed paths -- "N/A" on a confirmed path fails]
| Inertia
  [type: enabling condition; format: one sentence naming condition enabling or sustaining escalation;
   pass: >=1 non-null row populated; null rows: N/A: [why path does not exist] -- blank fails] |

TABLE 5 -- Sharing Rule Conflicts
| Rule [type: sharing rule name+type; format: "[name] ([manual/criteria/owner])"; pass: named -- blank fails]
| Baseline [type: role baseline; format: Own/BU/Parent BU/Org; pass: one of four -- blank fails]
| Widened Access [type: access beyond baseline; format: scope/field desc; pass: specific -- "widened" alone fails]
| Conflict
  [type: conflict description or adversarial null; format: if conflict: prose naming both grants;
   if no conflict: "Attack: [scenario] | Config: [rule+baseline] | Fails-if: [change widening access]";
   pass: conflict prose OR adversarial null with Fails-if -- blank fails]
| Gap ID [type: gap identifier; format: G-NN/G-NN(P2) carried/NONE; pass: G-format or NONE -- blank fails]
| H-Flag [type: hypothesis reference; format: H-ref or N/A: reason; pass: H-ref or N/A -- blank fails]
| Structural Competitor
  [type: legitimate access need served by this sharing rule; format: "Serves: [access need]" or "None: [no documented need]";
   pass: one of these two -- blank fails]
| Inertia [type: closure condition; format: what closes this widening; pass: specific action named -- blank fails] |

TABLE 6 -- Team Membership Gaps
| Team [type: team name; format: named team; pass: if no gap, list teams examined -- "teams correct" fails]
| Expected Members [type: role categories; format: comma-separated; pass: named roles -- "correct" fails]
| Gap Scenario
  [type: gap or adversarial null; format: if gap: who gains excess permissions;
   if no gap: "Attack: [scenario] | Config: [membership config] | Fails-if: [change that creates gap]";
   pass: specific scenario OR adversarial null with Fails-if -- blank fails]
| Combined Permission Risk [type: over-permission; format: specific risk; pass: named for gap rows; N/A for null]
| Gap ID [type: gap identifier; format: G-NN or N/A; pass: G-format or N/A -- blank fails]
| H-Flag [type: hypothesis reference; format: H-ref or N/A: reason; pass: H-ref or N/A -- blank fails] |

━━━ PHASE 3 COMPLETION GATE ━━━
  □ TABLE 3: all roles (highest-privilege first) x all ops; column contracts; H-Flag per row
  □ TABLE 4: all 4 vectors; Path column: confirmed path OR adversarial null with Fails-if; controls-only null fails
  □ TABLE 4: Structural Competitor populated for confirmed paths; Inertia >=1 non-null row
  □ TABLE 5: all columns per contracts; Conflict cell: conflict prose or adversarial null
  □ TABLE 6: all columns per contracts; Gap Scenario: specific or adversarial null with Fails-if
  □ All G-NN(P2) IDs appear in >=1 Phase 3 row

Commit the gap inventory before gate asserts:

GAP INVENTORY (committed before Phase 3 closes):
[G-NN(P2)] -- [description] -- first seen: [TABLE 1, FieldName row] -- (H1)
[G-MM]     -- [description] -- first seen: [TABLE 4, Vector row]     -- (H2)
...

  □ Inventory committed; every G-series ID present
  □ Every entry: G-ID + description + "first seen: TABLE X, row" + H-binding
  □ (P2) on all Phase 2-origin entries
  □ No Phase 4 content written yet

PHASE 3 COMPLETE
━━━━━━━━━━━━━━━━━

---

PHASE 4 -- ADVERSARIAL ASSESSMENT AND REMEDIATION

4a. Hypothesis Verdicts
For each H1, H2, ...:
  Verdict: Confirmed / Refuted / Modified
  Resolving evidence: [table name, row]
  Structural Competitor finding: [what org dependency did or did not defend this gap]

4b. Null-Finding Accountability
Each table where no gap was found: the adversarial null cells include the Fails-if condition.
Extract the highest-priority falsifying condition per table -- the change that would most
immediately convert a null-finding into a confirmed gap. "None found" without a Fails-if
satisfies C-11 but fails C-28.

4c. Remediation -- Addressing the Structural Competitor
  [G-ID] | Risk: H/M/L | Fix: [role + field + operation]
  Competitor Resistance: [workflow, habit, or dependency that will push back on this fix]

4d. TABLE 7 -- Risk-Ranked Summary
| Gap ID [type: gap identifier; format: from inventory only; pass: inventory G-format -- new ID fails]
| Description [type: one-sentence gap; format: prose; pass: specific -- blank fails]
| Risk [type: severity; format: H / M / L; pass: one of three -- spelled-out or blank fails]
| Justification [type: risk basis; format: data sensitivity + operation; pass: both named -- "high risk" alone fails]
| Phase Origin
  [type: origin classification; format: "P3" for Phase 3-origin; for Phase 2-origin (G-NN(P2)):
   "P2: T1/[field] -> T[N]/r[N] -> INV/G-NN(P2) -> T7/r[N]";
   pass: P3 or full four-location chain -- blank or "Phase 2" alone fails]
| Competitor Resistance
  [type: fix resistance level; format: H (core workflow depends on gap) / M (non-critical benefit) /
   L (default only, no legitimate dependency); pass: one of three with basis in 4c -- blank fails] |

━━━ PHASE 4 COMPLETION GATE ━━━
  □ All hypotheses resolved with table/row citation and Structural Competitor finding
  □ Null-finding accountability: Fails-if condition extracted per table; "none found" alone fails C-28
  □ All remediations: role + field + operation AND Competitor Resistance named
  □ TABLE 7: only inventory G-IDs; column contracts honored; no blanks
  □ Phase 2-origin gaps: inline four-location chain in Phase Origin (propagated from (P2) stamp)
  □ Competitor Resistance column populated every row
  □ Closing statement names the highest-resistance gap (technically obvious, organizationally expensive)
  □ No new G-IDs in Phase 4
  □ Each criterion satisfied by its column contract or structural element -- column contracts
    eliminate the need for prose to carry any table-based criterion

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## Variation Summary

| ID | Axis / Axes | Core Bet |
|----|-------------|----------|
| V-01 | C-28 only (adversarial null protocol, gate-centric) | NULL-FINDING RULE in preamble forces adversarial null format in TABLE 4 null rows; gate conditions verify attack scenario + Fails-if present; C-28 mechanically verifiable at Phase 3 gate |
| V-02 | C-27 only (full 3-part atomic column contracts) | Each column header specifies value type + format constraint + pass condition; inspector evaluates any cell from header alone; C-26 proved by construction -- the column IS the specification |
| V-03 | C-27 + C-28 compressed | Both new criteria encoded at maximum compression -- column contracts as inline header suffixes, adversarial null format embedded in Path column pass condition; proves C-27 and C-28 are structural properties requiring no prose |
| V-04 | C-28 uniform adversarial null across all tables | ADVERSARIAL NULL RULE applied to TABLE 1--6; every null row in every table produces a falsifiable Fails-if condition; output is an attack surface map, not just a gap list |
| V-05 | Adversarial-first + C-27 + C-28 full upgrade | R8 V-05 Structural Competitor extended: column headers upgraded to 3-part contracts (C-27) with Structural Competitor and Path column headers specifying the adversarial null pass condition (C-28); C-28 verifiable from TABLE 4 Path column header alone without reading preamble |
