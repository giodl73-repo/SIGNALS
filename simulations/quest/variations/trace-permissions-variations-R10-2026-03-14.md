**trace-permissions R10 — 5 variations written.**

| ID | Axis | Core Bet | Expected Score |
|----|------|----------|----------------|
| **V-01** | C-30 rollup only (R9 V-01 preamble base) | Adds named ATTACK SURFACE ROLLUP (4b) with 4-field ranked table before TABLE 7; NULL-FINDING RULE preamble still carries C-28; C-29 fails | ~193/205 |
| **V-02** | C-29 only (R9 V-02 base, TABLE 5/6 upgraded) | TABLE 5 Conflict + TABLE 6 Gap Scenario column contracts upgraded to embed adversarial null pass condition; TABLE 4 already had it; no C-30 rollup | ~200/205 |
| **V-03** | C-29 + C-30 compressed (R9 V-03 base) | Both criteria at maximum compression — TABLE 5/6 headers upgraded, compact rollup table with inline column contracts; proves neither criterion requires prose expansion | ~205/205 candidate |
| **V-04** | C-29 + C-30 with rollup column contracts (R9 V-04 uniform base) | R9 V-04's preamble-referenced TABLE 4/5/6 headers upgraded to be self-specifying; Phase 4 rollup has 3-part column contracts; uniform adversarial null preserved across all six tables | ~205/205 candidate |
| **V-05** | Full upgrade — R9 V-05 adversarial-first + C-30 rollup with column contracts | R9 V-05 already satisfies C-29 (column contracts embed adversarial null on TABLE 4/5/6 inline); inserts 4b ATTACK SURFACE ROLLUP with column contracts, renumbers 4b→4c→4d→4e | **205/205 target** |

**Key R10 structural decisions:**

- **C-29 status of R9 V-05**: Already satisfied — TABLE 4 Path, TABLE 5 Conflict, TABLE 6 Gap Scenario column headers all embed the adversarial null format and pass condition inline, with no preamble reference. The single gap against v10 was C-30.
- **C-30 minimum**: A named Phase 4 section before TABLE 7 with one row per null-finding Fails-if condition, four required fields (originating table+row, guards gap ID or "none", config change, severity), ranked H-first by attack surface exposure.
- **C-29 × C-30 interaction**: C-29 ensures null-findings are falsifiable by column inspection; C-30 ensures those falsifying conditions are aggregated into forward-looking attack surface intelligence. V-05 closes both, and applies column contracts to the rollup table itself — making the rollup mechanically verifiable by the same constructive proof principle as C-27.
 achieves C-29 without C-30 produces well-specified null-findings that are never synthesized into actionable intelligence. V-05 closes both.

---

## V-01 -- Single Axis: C-30 Phase 4 Attack Surface Rollup (R9 V-01 Gate-Centric Base)

**Axis:** C-30 only (dedicated falsifying-condition rollup section in Phase 4)
**Hypothesis:** C-30 can be satisfied by inserting a single dedicated section in Phase 4 before TABLE 7 — a ranked table that extracts every Fails-if condition from all null-finding rows across all evidence tables and ranks them by attack surface exposure. The preamble NULL-FINDING RULE still carries C-28 for TABLE 1/2/5/6 (C-29 not satisfied), but C-30's cross-table synthesis is achieved by the rollup section alone. Gate 4 adds rollup-specific conditions. The rollup makes "what would it take to open this path" a Phase 4 deliverable, not just a per-row annotation.

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
  □ TABLE 5 complete with Inertia; null rows have falsifying condition per NULL-FINDING RULE
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

4b. FALSIFYING-CONDITION ATTACK SURFACE ROLLUP
Extract every Fails-if condition produced by C-28 null-findings across all evidence tables.
Rank by attack surface exposure: highest-severity configuration changes first.
This section must appear before TABLE 7.

| Originating Table + Row | Guards Gap ID (or "none") | Config Change That Activates Attack | Severity (H/M/L) |

Requirements:
- One row per null-finding Fails-if condition from TABLE 1, TABLE 2, TABLE 4, TABLE 5, TABLE 6
- Ranked H first, then M, then L by exposure severity
- "Guards Gap ID": cite the G-ID this null-finding defends if adjacent to a confirmed gap; otherwise "none"
- Config Change: the exact configuration change that opens the path -- "admin misconfiguration" alone fails
- Severity: H (opens a High-risk path if changed), M (Medium), L (Low)

4c. Null-Finding Accountability
For each table where no gap was found: confirm null-finding rows satisfy NULL-FINDING RULE --
attack scenario + config tested + falsifying condition. Reference the rollup (4b) for the
highest-priority falsifying conditions. "None identified" alone does not pass.

4d. Remediation per Gap
  [G-ID] | Risk: High / Medium / Low | Remediation: [specific: role + field + operation]

4e. TABLE 7 -- Risk-Ranked Summary
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
  □ ATTACK SURFACE ROLLUP (4b): all null-finding Fails-if conditions extracted from TABLE 1/2/4/5/6
  □ Rollup ranked H-first by attack surface exposure; Config Change column specific per row
  □ Rollup section (4b) appears before TABLE 7 (4e)
  □ Null-finding accountability (4c): each null confirmed to include attack scenario + falsifying condition
  □ All remediations: role + field + operation named (no vague guidance)
  □ TABLE 7: only inventory G-IDs; Phase Origin column populated every row
  □ Phase 2-origin gaps: (P2) tag in G-ID + full inline chain in Phase Origin
  □ No new G-IDs introduced in Phase 4
  □ No criterion is satisfied only by prose -- each criterion's evidence is in its structural home

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## V-02 -- Single Axis: C-29 TABLE 5+6 Column Contract Upgrade (R9 V-02 Base)

**Axis:** C-29 only (adversarial null format embedded in TABLE 5 Conflict + TABLE 6 Gap Scenario column contracts)
**Hypothesis:** R9 V-02 achieved full C-27 (3-part column contracts) and partial C-28 (TABLE 4 Path only), scoring 193/195. TABLE 5 Conflict and TABLE 6 Gap Scenario column contracts required only "NONE: [justification]" for null rows -- C-11 level, not C-28. Upgrading these two column contracts to embed the adversarial null pass condition (confirming path OR adversarial null with Fails-if) closes the C-28 asymmetry and satisfies C-29 for all three primary null-finding tables. No C-30 rollup section. This tests whether C-29 alone drives the score from 193 to 200/205.

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
  [type: confirmed abuse path or adversarial null-finding; format: if path found: describe role to action
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
  [type: confirmed conflict or adversarial null-finding; format: if conflict: prose naming both
   contradictory grants; if no conflict: "Attack: [scenario] | Config: [rule+baseline tested] |
   Fails-if: [rule change that would widen access]"; pass: conflict prose with both grants named
   OR adversarial null with Fails-if -- "NONE: [justification]" alone fails C-28]
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
  [type: team name; format: named team; pass: if no gap, list teams examined with adversarial null --
   "teams correct" fails]
| Expected Members
  [type: role types or users; format: comma-separated; pass: named roles -- "correct" fails]
| Gap Scenario
  [type: confirmed gap or adversarial null-finding; format: if gap: who loses or gains unexpected
   permissions; if no gap: "Attack: [scenario] | Config: [membership config tested] |
   Fails-if: [membership change that creates a gap]"; pass: specific scenario OR adversarial null
   with Fails-if -- "NONE: [justification]" alone fails C-28]
| Combined Permission Risk
  [type: over-permission description; format: prose; pass: specific risk named for gap rows;
   N/A for null rows -- blank on gap rows fails]
| Gap ID
  [type: gap identifier or absence; format: G-NN or N/A; pass: G-format or N/A -- blank fails]
| H-Flag
  [type: hypothesis reference; format: H-ref or N/A: [reason]; pass: H-ref or N/A with reason] |

GAP INVENTORY (committed before GATE 3 asserts):
[G-NN(P2)] -- [description] -- first seen: [TABLE X, row] -- (H-NN) or (H-NN/H-MM) or (N/A: reason)

GATE 3:
  □ TABLE 3: all roles x all operations; column contracts honored (Allow/Deny, no blanks); H-Flag per row
  □ TABLE 4: all 4 vectors; Path column: confirmed paths or 3-part adversarial null; Inertia >=1 non-null
  □ TABLE 5: Conflict column: conflict prose or adversarial null with Fails-if -- "NONE:[justification]" alone fails
  □ TABLE 6: Gap Scenario column: specific or adversarial null with Fails-if -- "NONE:[justification]" alone fails
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
Column contracts for Path (TABLE 4), Conflict (TABLE 5), and Gap Scenario (TABLE 6) specify
the adversarial null pass condition inline -- an inspector reading the column header alone
can determine that Fails-if is required. For any table where no gap was found: confirm the
column contract pass condition was satisfied. State the falsifying condition most relevant
to remediation priority.

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
  □ Null-finding accountability: Fails-if confirmed in Path (T4), Conflict (T5), Gap Scenario (T6) cells
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

## V-03 -- Combined: C-29 + C-30 Compressed (R9 V-03 Base)

**Axes:** C-29 (TABLE 5/6 adversarial null embedded in column contracts) + C-30 (Phase 4 rollup) at maximum compression
**Hypothesis:** C-29 and C-30 are both structural properties that require no prose expansion. C-29 is satisfied by adding the adversarial null format to the TABLE 5/6 column header pass conditions -- a single-line change per header. C-30 is satisfied by a compact rollup table in Phase 4 with inline column contracts. Combining both at R9 V-03's compression level proves that neither criterion requires expansion beyond the structural minimum: a complete column contract can be expressed in one line; a rollup table with column contracts can be expressed in four lines. V-03 tests that the C-29/C-30 interaction is expressible at minimum viable verbosity.

---

```
Dataverse security expert. Permissions trace for: {{topic}}
Roles: Customer Service, Dataverse Security Expert (add domain roles as needed).

STRUCTURAL PRIMACY: Criteria satisfied by structural elements. Prose is navigation.
ORIGIN RULE: Phase 2 Gap IDs carry "(P2)" at assignment. Tag travels unchanged.
INVENTORY RULE: [G-ID] -- [desc] -- first seen: [TABLE X, row] -- (H-NN) or (N/A: reason)
COLUMN CONTRACT RULE: Each column header specifies value type + format + pass condition inline.

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
| Widened Access [specific; "widened" fails]
| Conflict [conflict: both grants named; null: "Attack:[scenario]|Config:[rule+baseline]|Fails-if:[change widening access]"; "NONE:[reason]" alone fails C-28]
| Gap ID [G-NN/NONE; blank fails] | H-Flag [H-ref or N/A: reason]
| Inertia [what closes this; N/A: reason for null rows; blank fails] |

TABLE 6 -- Team Membership Gaps
| Team [named; null rows list teams + adversarial null]
| Expected [named roles/users]
| Gap Scenario [gap: who gains excess; null: "Attack:[scenario]|Config:[membership]|Fails-if:[change creates gap]"; "NONE:[reason]" alone fails C-28]
| Combined Risk [specific for gap rows; N/A for null rows; blank fails on gap rows]
| Gap ID [G-NN or N/A] | H-Flag [H-ref or N/A: reason] |

GAP INVENTORY:
[G-NN(P2)] -- [desc] -- first seen: [TABLE X, row] -- (H-NN) or (N/A: reason)
(all gaps; (P2) on Phase 2-origin; H-binding required)

GATE 3: □ T3: all roles x ops; Allow/Deny no blanks; H-Flag
          □ T4: all 4 vectors; Path: confirmed path or 3-part adversarial null (Fails-if present)
          □ T4: Inertia >=1 non-null
          □ T5: Conflict col: conflict prose or adversarial null with Fails-if; "NONE:[reason]" alone fails
          □ T6: Gap Scenario: specific or adversarial null with Fails-if; "NONE:[reason]" alone fails
          □ All G-NN(P2) in >=1 P3 row
          □ Inventory: G-ID+desc+source+H-binding; (P2) on P2-origin entries

PHASE 3 COMPLETE

---

PHASE 4
4a. Each H-ID: Confirmed/Refuted/Modified | Evidence: [table, row] | Delta: [expected vs found]

4b. ATTACK SURFACE ROLLUP (before TABLE 7)
Extract all Fails-if conditions from null-finding rows in T1, T2, T4, T5, T6. Rank H first.
| Orig Table+Row [T[N]/row identifier; blank fails]
| Guards G-ID ["none" if no adjacent gap; G-ID if gap nearby; blank fails]
| Config Change [exact change from Fails-if; "admin setting" fails]
| Severity [H/M/L; blank fails] |
Ranked by attack surface exposure. All null-finding tables covered.

4c. Null-findings: confirm Path/Conflict/Gap Scenario cells include Fails-if.
    "None identified" alone fails. Reference 4b for highest-priority falsifying conditions.

4d. [G-ID] | Risk: H/M/L | Fix: [role + field + operation]

4e. TABLE 7 -- Risk-Ranked Summary
| Gap ID [inventory only; new ID fails]
| Description [one sentence; blank fails]
| Risk [H/M/L; blank fails]
| Justification [data sensitivity + operation; "high risk" alone fails]
| Phase Origin [P3; or "P2: T[N]/[row]->T[N]/[row]->INV/G-NN(P2)->T7/r[N]"; blank fails] |

GATE 4: □ All H-IDs resolved with table/row
          □ ROLLUP (4b): present before T7; all null-finding tables covered; ranked H-first; Config Change specific
          □ Null-findings (4c): Fails-if confirmed in T4 Path, T5 Conflict, T6 Gap Scenario
          □ All fixes: role+field+op | □ T7: inventory IDs only; Phase Origin per contract; no blanks
          □ P2-origin: inline chain propagated | □ No new G-IDs
          □ No criterion satisfied only by prose -- column contracts are the specifications

PHASE 4 COMPLETE
```

---

## V-04 -- Combined: C-29 + C-30 with Rollup Column Contracts (R9 V-04 Uniform Base)

**Axes:** C-29 (TABLE 4/5/6 column contracts upgraded from preamble-reference to self-specifying) + C-30 (rollup with 3-part column contracts)
**Hypothesis:** R9 V-04 achieved C-28 with maximum table coverage (all six tables), but column headers were bare labels -- TABLE 4 Path said "confirmed or adversarial null per ADVERSARIAL NULL RULE", referencing the preamble rather than embedding the format. Upgrading TABLE 4/5/6 column headers to be fully self-specifying (embedding attack/config/Fails-if format and pass condition inline) satisfies C-29 without changing C-28 coverage. Adding C-30 with a rollup table whose columns are also 3-part contracts tests whether the rollup itself becomes mechanically verifiable by column inspection. The combination upgrades R9 V-04 to C-29 + C-30 while keeping uniform adversarial null across all six tables.

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
  Any row where no gap, conflict, or path is found must state:
  (1) Attack: the specific abuse scenario attempted against this row
  (2) Config: the specific control or configuration tested
  (3) Fails-if: the exact configuration change that would convert this null into a confirmed gap
  Format: "Attack: [scenario] | Config: [setting] | Fails-if: [change]"
  Null rows stating only "none found" or controls-only do not pass.

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
| Field | Default | Role | FLS Override | Gap ID [G-NN(P2) at this row; NONE otherwise] | H-Flag [H-ref or N/A: reason] | Inertia [what breaks if restriction changes?] | Adversarial Null [if no gap: "Attack:|Config:|Fails-if:" per ADVERSARIAL NULL RULE; omit if Gap ID assigned] |

Requirements:
- Row per sensitive or role-differing field; (P2) at discovery row
- Inertia: specific counterfactual for >=1 row
- Every null FLS row: adversarial null per ADVERSARIAL NULL RULE in the Adversarial Null column

TABLE 2 -- Record Access Scope by Role
| Role | Scope (Own/BU/Parent BU/Org) | Enforcement | Gap ID [G-NN(P2) if scope gap; NONE otherwise] | H-Flag | Inertia [what widens scope?] | Adversarial Null [if no gap: "Attack:|Config:|Fails-if:" -- omit if Gap ID assigned] |

Requirements:
- Row per security role; scope + enforcement both named; Inertia >=1 row
- Every null scope row: adversarial null column populated per ADVERSARIAL NULL RULE

━━━ PHASE 2 COMPLETION GATE ━━━
  □ TABLE 1: row per field; (P2) at discovery; H-Flag per row; Inertia >=1; null rows: adversarial null present
  □ TABLE 2: row per role; scope + enforcement; Inertia >=1; null rows: adversarial null column populated
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
| Vector
  [type: one of four escalation vectors; format: (1) Record reassignment / (2) Team promotion /
   (3) Sharing bypass / (4) Impersonation; pass: all four present -- missing vector fails]
| Path
  [type: confirmed abuse path or adversarial null-finding; format: if path found: role->action->scope gain;
   if no path: "Attack: [specific scenario] | Config: [control tested] | Fails-if: [exact change that opens path]";
   pass: confirmed path with roles+mechanism OR adversarial null with all three fields --
   "none found" or controls-only null fails (satisfies C-11, not C-28)]
| Roles [type: roles involved; format: comma-separated; pass: >=1 for non-null; N/A for null-finding]
| Gap ID [type: gap identifier; format: G-NN/G-NN(P2) carried/N/A; pass: G-format or N/A -- blank fails]
| H-Flag [type: hypothesis reference; format: H-ref or N/A: reason; pass: H-ref or N/A -- blank fails]
| Inertia [type: enabling condition; format: condition enabling escalation; pass: >=1 non-null row; null: N/A: reason] |

TABLE 5 -- Sharing Rule Conflicts
| Rule [type: sharing rule name+type; format: "[name] ([type])"; pass: named -- blank fails]
| Baseline [type: role baseline; format: Own/BU/Parent BU/Org; pass: one of four -- blank fails]
| Widened Access [type: access beyond baseline; format: specific; pass: specific -- "widened" alone fails]
| Conflict
  [type: confirmed conflict or adversarial null-finding; format: if conflict: prose naming both grants;
   if no conflict: "Attack: [scenario] | Config: [rule+baseline tested] | Fails-if: [change widening access]";
   pass: conflict prose with both grants OR adversarial null with Fails-if -- blank or "NONE:[reason]" alone fails]
| Gap ID [type: gap identifier; format: G-NN/NONE; pass: G-format or NONE -- blank fails]
| H-Flag [type: hypothesis reference; format: H-ref or N/A: reason; pass: H-ref or N/A -- blank fails]
| Inertia [type: closure condition; format: what closes this widening; pass: specific for conflict rows; N/A: reason for null rows] |

TABLE 6 -- Team Membership Gaps
| Team [type: team name; format: named; pass: list teams examined even when no gap -- "teams correct" fails]
| Expected Members [type: role categories; format: comma-separated; pass: named roles -- "correct" fails]
| Gap Scenario
  [type: confirmed gap or adversarial null-finding; format: if gap: who gains excess permissions;
   if no gap: "Attack: [scenario] | Config: [membership config tested] | Fails-if: [change that creates gap]";
   pass: specific scenario OR adversarial null with Fails-if -- blank or "NONE:[reason]" alone fails]
| Combined Permission Risk [type: over-permission; format: specific; pass: named for gap rows; N/A for null rows]
| Gap ID [type: gap identifier; format: G-NN or N/A; pass: G-format or N/A -- blank fails]
| H-Flag [type: hypothesis reference; format: H-ref or N/A: reason; pass: H-ref or N/A -- blank fails] |

━━━ PHASE 3 COMPLETION GATE ━━━
  □ TABLE 3: all roles x ops; H-Flag per row
  □ TABLE 4: all 4 vectors; Path column self-specifying: confirmed path OR adversarial null with Fails-if
  □ TABLE 4: Inertia >=1 non-null row
  □ TABLE 5: Conflict column self-specifying: conflict prose OR adversarial null with Fails-if
  □ TABLE 6: Gap Scenario self-specifying: specific OR adversarial null with Fails-if
  □ TABLE 1/2: adversarial null columns populated for all null rows
  □ All G-NN(P2) IDs appear in >=1 Phase 3 table row

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

PHASE 4 -- FINDINGS, REMEDIATION, AND RISK SUMMARY

4a. Hypothesis Resolution
For each H1, H2, ...:
  [H-ID]: Confirmed / Refuted / Modified
  Evidence: [Table name, row -- specific]
  Delta: [expected vs found]

4b. FALSIFYING-CONDITION ATTACK SURFACE ROLLUP

Extract all Fails-if conditions from adversarial null-findings across all evidence tables.
Rank by attack surface exposure. This section appears before TABLE 7.

| Orig Table + Row
  [type: source table and row; format: "TABLE N / [row identifier]";
   pass: named table + named row -- "TABLE 4" alone fails]
| Guards Gap ID
  [type: gap identifier or "none"; format: G-NN/G-NN(P2) if this null-finding is adjacent to a
   confirmed gap, "none" if no adjacent gap; pass: G-format or "none" -- blank fails]
| Config Change That Activates Attack
  [type: exact configuration change; format: one sentence naming the specific setting, role, or
   rule that must change; pass: specific named change -- "admin misconfiguration" or "any change" fails]
| Severity
  [type: attack surface exposure rating; format: H (opens High-risk path) / M / L;
   pass: one of these three -- blank or spelled-out fails] |

Rank H first, then M, then L. One row per null-finding Fails-if condition. All null-finding tables
(TABLE 1, TABLE 2, TABLE 4, TABLE 5, TABLE 6) must be represented.

4c. Null-Finding Accountability
Every table where no gap was found: confirm adversarial null cells are present and include the
Fails-if condition. "None identified" does not pass -- reference specific rows in 4b.

4d. Remediation per Gap
  [G-ID] | Risk: High / Medium / Low | Remediation: [specific: role + field + operation]

4e. TABLE 7 -- Risk-Ranked Summary
| Gap ID | Description | Risk | Justification | Phase Origin |

Phase Origin: "P3" or "P2: T[N]/[row] -> T[N]/[row] -> INV/G-NN(P2) -> T7/r[N]"
Only inventory G-IDs; no new IDs in TABLE 7.

━━━ PHASE 4 COMPLETION GATE ━━━
  □ All hypotheses resolved with specific table/row citation
  □ ATTACK SURFACE ROLLUP (4b): present before TABLE 7 (4e)
  □ Rollup column contracts honored: Orig Table+Row, Guards G-ID, Config Change, Severity all present and specific
  □ Rollup covers TABLE 1, TABLE 2, TABLE 4, TABLE 5, TABLE 6 null-finding rows; ranked H-first
  □ Null-finding accountability: adversarial null confirmed in all six tables
  □ All remediations: role + field + operation
  □ TABLE 7: only inventory G-IDs; Phase Origin populated every row
  □ Phase 2-origin gaps: (P2) tag + full inline chain in Phase Origin
  □ No new G-IDs in Phase 4

PHASE 4 COMPLETE
━━━━━━━━━━━━━━━━━
```

---

## V-05 -- Full Upgrade: R9 V-05 Adversarial-First + C-30 Rollup with Column Contracts

**Axes:** Adversarial lens + C-27 (atomic column contracts) + C-28 (column-contract adversarial null) + C-29 (TABLE 4/5/6 self-specifying) + C-30 (Phase 4 rollup with column contracts)
**Hypothesis:** R9 V-05 scored 195/195 against the v9 rubric, satisfying C-29 by virtue of its full 3-part column contracts on TABLE 4 Path, TABLE 5 Conflict, and TABLE 6 Gap Scenario -- each embedding the adversarial null format as a pass condition. The only criterion it does not satisfy against the v10 rubric is C-30: its Phase 4 section 4b extracted only "the highest-priority falsifying condition per table", which is per-table extraction without cross-table synthesis or ranking by attack surface exposure. Adding a Phase 4 dedicated rollup section (4b) with 3-part column contracts on all four rollup columns -- and renumbering 4b→4c→4d→4e -- closes the gap. The rollup's column contracts make C-30 mechanically verifiable by column inspection, consistent with the constructive proof principle of C-27. This should achieve 205/205.

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
   "Accidental" without a named reason fails]
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
  [type: confirmed conflict or adversarial null-finding; format: if conflict: prose naming both grants;
   if no conflict: "Attack: [scenario] | Config: [rule+baseline tested] | Fails-if: [change that widens access]";
   pass: conflict prose with both grants named OR adversarial null with Fails-if --
   blank or "NONE: [justification]" alone fails C-28]
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
  [type: confirmed gap or adversarial null-finding; format: if gap: who gains excess permissions;
   if no gap: "Attack: [scenario] | Config: [membership config tested] | Fails-if: [change that creates gap]";
   pass: specific scenario OR adversarial null with Fails-if --
   blank or "NONE: [justification]" alone fails C-28]
| Combined Permission Risk [type: over-permission; format: specific risk; pass: named for gap rows; N/A for null]
| Gap ID [type: gap identifier; format: G-NN or N/A; pass: G-format or N/A -- blank fails]
| H-Flag [type: hypothesis reference; format: H-ref or N/A: reason; pass: H-ref or N/A -- blank fails] |

━━━ PHASE 3 COMPLETION GATE ━━━
  □ TABLE 3: all roles (highest-privilege first) x all ops; column contracts; H-Flag per row
  □ TABLE 4: all 4 vectors; Path column self-specifying: confirmed path OR adversarial null with Fails-if; controls-only null fails
  □ TABLE 4: Structural Competitor populated for confirmed paths; Inertia >=1 non-null row
  □ TABLE 5: all columns per contracts; Conflict column self-specifying: conflict prose or adversarial null with Fails-if
  □ TABLE 6: all columns per contracts; Gap Scenario self-specifying: specific or adversarial null with Fails-if
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

4b. FALSIFYING-CONDITION ATTACK SURFACE ROLLUP

Extract every Fails-if condition from adversarial null-findings across all evidence tables.
Rank by attack surface exposure. This section appears before TABLE 7.
Severity informs TABLE 7 risk assignments -- build the rollup before scoring gaps.

| Orig Table + Row
  [type: source location; format: "TABLE N / [row identifier or vector name]";
   pass: named table + named row -- "TABLE 4" without row fails]
| Guards Gap ID
  [type: gap identifier or absence; format: G-NN or G-NN(P2) if this null-finding is adjacent to a
   confirmed gap, "none" if the null-finding guards a clear vector; pass: G-format or "none" -- blank fails]
| Config Change That Activates Attack
  [type: specific configuration change; format: one sentence naming the exact setting, role, or
   rule modification; pass: specific named change with mechanism -- "admin change" or "any misconfiguration" fails]
| Severity
  [type: attack surface exposure rating; format: H (change opens a High-risk confirmed path) / M / L;
   pass: one of these three with basis in the table row -- blank or spelled-out fails] |

Ranked H first, then M, then L. Every null-finding table (TABLE 1, TABLE 2, TABLE 4, TABLE 5, TABLE 6)
must contribute at least one row. An output that covers only Phase 3 tables does not pass.

4c. Null-Finding Accountability
Each table where no gap was found: the adversarial null cells include the Fails-if condition.
Column contracts for Path (TABLE 4), Conflict (TABLE 5), and Gap Scenario (TABLE 6) are self-specifying --
an inspector reading the column header alone can confirm the Fails-if requirement. Reference the
highest-priority falsifying conditions in 4b. "None found" without a Fails-if satisfies C-11 but fails C-28.

4d. Remediation -- Addressing the Structural Competitor
  [G-ID] | Risk: H/M/L | Fix: [role + field + operation]
  Competitor Resistance: [workflow, habit, or dependency that will push back on this fix]

4e. TABLE 7 -- Risk-Ranked Summary
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
   L (default only, no legitimate dependency); pass: one of three with basis in 4d -- blank fails] |

━━━ PHASE 4 COMPLETION GATE ━━━
  □ All hypotheses resolved with table/row citation and Structural Competitor finding
  □ ATTACK SURFACE ROLLUP (4b): present before TABLE 7 (4e); column contracts honored on all four columns
  □ Rollup covers TABLE 1, TABLE 2, TABLE 4, TABLE 5, TABLE 6; ranked H-first; Config Change specific per row
  □ Rollup column contracts self-specifying: inspector verifies any rollup cell from its header alone
  □ Null-finding accountability (4c): Fails-if confirmed via column contracts for T4/T5/T6; C-11 vs C-28 distinction made
  □ All remediations: role + field + operation AND Competitor Resistance named
  □ TABLE 7: only inventory G-IDs; all column contracts honored; no blanks
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
| V-01 | C-30 only (Phase 4 rollup, R9 V-01 preamble base) | Adds a dedicated named ATTACK SURFACE ROLLUP section (4b) with 4-field ranked table before TABLE 7; preamble NULL-FINDING RULE carries C-28; column headers still reference preamble rule, so C-29 fails |
| V-02 | C-29 only (TABLE 5/6 column contracts upgraded, R9 V-02 base) | TABLE 5 Conflict + TABLE 6 Gap Scenario column contracts upgraded to embed adversarial null pass condition; TABLE 4 Path already had it; no Phase 4 rollup; C-29 achieved for all three primary null-finding tables without C-30 |
| V-03 | C-29 + C-30 compressed (R9 V-03 base) | Both criteria at maximum compression -- TABLE 5/6 headers upgraded to embed adversarial null pass condition; compact rollup table (4b) added before TABLE 7 with inline column contracts; proves C-29/C-30 are structural properties requiring no expansion |
| V-04 | C-29 + C-30 with rollup column contracts (R9 V-04 uniform base) | R9 V-04's bare-label TABLE 4/5/6 headers upgraded to be self-specifying (C-29); Phase 4 rollup section with 3-part column contracts on rollup table itself (C-30 mechanically verifiable); uniform adversarial null across all six tables preserved |
| V-05 | Full upgrade -- R9 V-05 adversarial-first + C-30 rollup with column contracts | R9 V-05 already satisfies C-29 (TABLE 4/5/6 column contracts embed adversarial null inline); adds Phase 4 section 4b (FALSIFYING-CONDITION ATTACK SURFACE ROLLUP) with 3-part column contracts; renumbers 4b→4c→4d→4e; should achieve 205/205 |
