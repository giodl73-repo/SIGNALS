# trace-permissions Variate — Round 8 (rubric v8 — C-29/C-30 target)
**Date:** 2026-03-16
**Rubric:** v8 (C-01 through C-30 — C-29/C-30 added from Round 7 excellence signals)
**Target criteria:** C-29 (verdict-level mechanism cross-audit), C-30 (equivalence clause in prohibition instructions)

**State entering Round 8:**

| Variation | v7 score | Gap under v8 |
|-----------|----------|--------------|
| R7-V-05 (best v7) | 21/21 aspirational criteria | Missing C-29/C-30 (-8.7 pts) = full aspirational miss |
| Reference arch | C-01–C-28 satisfied | C-29 requires output-stated cross-audit; C-30 requires equivalence clause in prohibition instructions |

Round 8 holds the established v7 scaffold (compound blocks, TR Registry, dual remediation, pre-declaration, dedicated closing column, roll-up with restated mechanisms, three-field no-finding format, strict column instruction, composite verdict with mechanism types) and adds C-29/C-30 mechanisms across three single-axis tests and two combined variations.

---

## Round 8 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format — C-29 isolation: CROSS-AUDIT row added to escalation vector block; no equivalence clauses | C-29 requires the output to explicitly assert that the pre-declaration commitment and closing mechanism column entry name the same structural fact. Adding a mandatory CROSS-AUDIT row immediately after the Closing Mechanism column, populated with the exact declaration text, the exact filed mechanism text, and an explicit match confirmation, converts reader-inferred alignment to output-stated alignment. No equivalence clause — C-30 fails by design. Isolated test: +4.35 pts (C-29 only). |
| V-02 | Phrasing register — C-30 isolation: equivalence clauses in all prohibition instructions; no cross-audit row | C-30 requires that prohibition instructions not only name specific disallowed forms but also include a semantic equivalence clause that generalizes beyond the named set. Adding "or any equivalent [form achieving the same prohibited effect]" to the column content exclusivity instruction and the roll-up anti-back-reference instruction converts enumerated prohibitions from exhaustive lists to representative samples. No cross-audit row — C-29 fails by design. Isolated test: +4.35 pts (C-30 only). |
| V-03 | Lifecycle emphasis — C-29 via explicit four-phase vector chain; no equivalence clauses | C-29's cross-audit assertion becomes structural when the vector lifecycle has four mandatory phases — DECLARE, ANALYZE, FILE, AUDIT — and the AUDIT phase is a blocking gate that cannot be omitted. Framing the cross-audit as a lifecycle phase rather than an optional row forces the assertion into every NOT POSSIBLE vector. No equivalence clause — C-30 fails by design. Single-axis test for C-29 via lifecycle framing vs. V-01's format-row framing. |
| V-04 | Combined: C-29 (CROSS-AUDIT row) + C-30 (equivalence clauses) | CROSS-AUDIT rows from V-01 provide the output-stated match assertion; equivalence clauses from V-02 close the prohibition enumeration gap. Both constraints are satisfiable independently — a prompt that adds a CROSS-AUDIT row without equivalence clauses passes C-29 and fails C-30; one that adds equivalence clauses without a CROSS-AUDIT row fails C-29. V-04 tests whether combining them produces interference or compounds cleanly. |
| V-05 | Full protocol: C-29 + C-30 on complete established v7 scaffold | Established v7 scaffold (all C-01–C-28 mechanisms retained) plus C-29 CROSS-AUDIT rows and C-30 equivalence clauses. Compliance self-check extended to cover C-29 and C-30. Tests whether adding both new criteria to the full protocol produces any regression on prior criteria. |

---

## V-01 — Output Format: CROSS-AUDIT Row in Escalation Vector Block

**Axis:** Output format — CROSS-AUDIT row added to escalation vector compound block at every NOT POSSIBLE site (C-29 single-axis)
**Hypothesis:** C-29 fires when the pre-declaration commitment and the closing mechanism column cell name the same structural fact but no explicit output assertion confirms the match — alignment is reader-inferred. A mandatory CROSS-AUDIT row immediately following the Closing Mechanism column entry writes the declaration text, the filed mechanism text, and a match verdict. This makes the alignment assertion observable at a glance, not derivable by comparison. No equivalence clause — C-30 tests whether the prohibition instructions' enumerated forms alone hold without semantic closure.

---

You are running a permissions trace signal for: {{topic}}

---

## TRIGGER RULE REGISTRY

Complete before any entity or gap content. Locked after this section.

| Rule ID | Fires When | Severity |
|---------|-----------|----------|
| TR-01 | Sensitive field DELTA shows `MISSING-PROFILE` | HIGH |
| TR-02 | ADMIN OWD = Organization AND entity is sensitive | HIGH |
| TR-03 | DELTA shows `TEAM-GAP` AND self-addition = YES | MEDIUM |
| TR-04 | DELTA shows `CONFLICT:[rule]` AND rule grants beyond OWD | MEDIUM |
| TR-05 | DELTA shows `ESCALATION-OPEN` | HIGH |

No-judgment mandate: HIGH or MEDIUM without a named TR rule = protocol violation. Repair before advancing.

---

## STEP 0 — INERTIA INVENTORY

Categorize every permission before analysis.

| Entity | Setting | Current Value | Stock Default | Category (INERTIA / DESIGN) |

OWDs, FLS profiles, sharing rules, role assignments, team memberships — all entries required. Missing category = fail.

---

## STEP 1 — CEILING AND FLOOR

Section open — compound block format active.

For each entity:
```
Entity: [Dataverse system name]
ADMIN  | OWD: [level/scope]  Privs: [Create/Read/Write/Delete/Assign — Y/N each]  FLS: [profile per sensitive field or NONE]  Stock Default OWD: [from Step 0]
CS     | OWD: [level/scope]  Privs: [Create/Read/Write/Delete/Assign — Y/N each]  FLS: [profile per sensitive field or NONE]
DELTA  | [typed token list or NONE]
```

DELTA tokens: `MISSING-PROFILE` / `RESTRICTED-READ` / `RESTRICTED-WRITE` / `OVER-EXPOSED` / `SCOPE-NARROWED:[from→to]` / `FLS-GAP:[field]` / `ESCALATION-OPEN` / `TEAM-GAP` / `CONFLICT:[rule name]` / `NONE`

Sentences in DELTA rows = format violation. Roles: Dataverse system names. OWD: level AND scope both required.

Entity closure before advancing:
```
ENTITY [name] | Operations reviewed: [list] | Fields confirmed: [list] | Gaps tallied: [count or NONE]
```
Gap-containing entities: name the gaps tallied. Implicit transition without closure = fail.

---

## STEP 2 — FIELD-LEVEL SECURITY DETAIL

Section open — compound block format active.

For each sensitive field with a non-NONE FLS-related DELTA token in Step 1:
```
Entity.Field: [Dataverse system name]
ADMIN  | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N  Stock Default: [from Step 0]
CS     | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N
DELTA  | [MISSING-PROFILE / RESTRICTED-READ / RESTRICTED-WRITE / OVER-EXPOSED / NONE]
```

---

## STEP 3 — GAP REGISTER

Gaps sourced from DELTA tokens in Steps 1–2 only.

| Gap ID | Source | Entity.Field | DELTA Tokens | Category (Step 0) | TR Rule | Severity |

Row protocol — apply before advancing:
1. Copy DELTA tokens from source block
2. Identify all TR rules that fire
3. Assign highest severity. No rule fires → LOW, TR = N/A
4. HIGH or MEDIUM: TR Rule must be populated → blank = PROTOCOL VIOLATION → repair before next row
5. Category: from Step 0 → missing category requires Step 0 update before this row is complete

---

## STEP 4 — ESCALATION ANALYSIS

### Pre-Declaration Block (before any vector table)

For each Write-capable role, state structural assumptions before analysis:
```
Role: [Dataverse system name]
Pre-declaration:
  - [Assumption 1: structural basis for NOT POSSIBLE on vector type A — e.g., "no criteria-based sharing rule grants cross-BU scope for this OWD setting"]
  - [Assumption 2: structural basis for NOT POSSIBLE on vector type B]
  - [Additional assumptions as needed]
```

A NOT POSSIBLE verdict without a prior matching assumption in this block = contract violation.

### Escalation Vector Table

For each Write-capable role, after the Pre-Declaration block:

| Vector Type | Assumption Declared | Evidence Examined | Verdict | Closing Mechanism | CROSS-AUDIT |
|-------------|--------------------|--------------------|---------|-------------------|-------------|

**Column instructions:**

**Assumption Declared**: Copy the relevant assumption from the Pre-Declaration block for this row's vector type. Must match the declaration above.

**Verdict**: POSSIBLE or NOT POSSIBLE. NOT POSSIBLE without Closing Mechanism = format violation.

**Closing Mechanism** — content exclusivity rule:
- One structural fact only: the specific privilege or configuration state confirmed absent
- Do not write: verdict language ("NOT POSSIBLE because..."), declaration traces ("confirms pre-declared assumption above"), placeholder text ("N/A"), or anything other than the single named structural fact
- POSSIBLE rows: leave this column empty

**CROSS-AUDIT** — mandatory for all NOT POSSIBLE rows:
```
Pre-decl: "[exact text from Assumption Declared column for this row]" | Filed: "[exact text from Closing Mechanism column for this row]" | Match: CONFIRMED
```
If the two texts name different structural facts:
```
Pre-decl: "[text]" | Filed: "[text]" | Match: MISMATCH: [describe the divergence]
```
POSSIBLE rows: leave this column empty.
A NOT POSSIBLE row with a blank CROSS-AUDIT column = format violation — populate before advancing.

### Per-Role Roll-Up

After vector table for each role:
```
Role: [system name]
Vectors assessed: [count] | POSSIBLE: [count] | NOT POSSIBLE: [count]
Composite verdict: [name each NOT POSSIBLE vector's closing mechanism type inline — e.g., "sharing: no criteria-based rule; team: no owner-access team accepts this role; field inheritance: FLS denies write; role hierarchy: BU-only scope"]
Mechanisms cited: [restate each closing mechanism inline — do not write "see table above", "see vector table", "mechanisms in Step 4"]
```

No-finding declaration for all-NOT-POSSIBLE roles:
```
Checked: [vector types examined]  Confirmed: [each structural basis named]  Conclusion: no escalation path from [role].
```

---

## STEP 5 — SHARING RULE CONFLICTS

Section open — compound block format active.

```
Rule: [Dataverse system name]
ADMIN  | Grants: [source → target]  Level: [access]  Stock Default: [exists in stock / not in stock]
CS     | Received: [level]  Expected by OWD: [level]
DELTA  | [CONFLICT:[rule name] or NONE]  TR: [TR-04 if fires]
```

Three-field format for clean rules:
```
Checked: [rule name or rule type]  Confirmed: [access level matches OWD; no cross-BU expansion]  Conclusion: no conflict — [role] sharing rules do not exceed OWD ceiling.
```

---

## STEP 6 — TEAM MEMBERSHIP GAPS

Section open — compound block format active.

```
Team: [name]
ADMIN  | Required role: [system name]  Self-add: [YES/NO]  Category: [from Step 0]
CS     | Membership: [IN-TEAM / NOT-IN-TEAM / CONDITIONAL]
DELTA  | [TEAM-GAP or NONE]  TR: [TR-03 if TEAM-GAP + YES]  Scenario impact: [specific, not generic]
```

Three-field format for no-dependency teams:
```
Checked: [team name]  Confirmed: [role not in team, or self-add blocked by named mechanism]  Conclusion: no team membership gap for [role].
```

---

## STEP 7 — CROSS-ROLE INTERACTION

Section open — compound block format active.

```
Interaction: [Role A] + [Role B] on [Entity]
ADMIN  | Role A privileges: [list]
CS     | Role B privileges: [list]
DELTA  | Superset exceeding either alone: [list or NONE]  New TR conditions: [list or NONE]
```

---

## STEP 8 — CATEGORIZATION GATE

Every gap from Step 3 must appear here before Step 9.

| Gap ID | Entity.Field | Current State | Category (INERTIA / DESIGN) | Stock Default (INERTIA) | Admin Decision Context (DESIGN) |

Missing gap = gate failure. Gap with no category = gate failure.

---

## STEP 9 — DUAL REMEDIATION TRACKS

Every Step 3 gap in exactly one track.

### TRACK A — INERTIA Gaps
```
Gap: [Gap ID]  TR resolved: [rule ID]
ADMIN  | Platform default: [from Step 0]
CS     | Target state: [required value]
DELTA  | Action: Enable [setting] on [entity/field] in [solution]. First-time configuration — platform shipped with [default]. After fix: [behavioral delta].
```

### TRACK B — DESIGN Gaps
```
Gap: [Gap ID]  TR resolved: [rule ID]
ADMIN  | Current (deliberate): [value]  Decision context: [from Step 8]
CS     | Target state: [corrected value]
DELTA  | Action: Change [setting] on [entity/field] in [solution] from [A] to [B]. Reverses [decision context]. After fix: [behavioral delta].
```

Identical action format across tracks = fail. Generic advice = fail. Each gap in exactly one track.

---

## V-02 — Phrasing Register: Equivalence Clauses in Prohibition Instructions

**Axis:** Phrasing register — equivalence clauses added to all prohibition instructions (C-30 single-axis)
**Hypothesis:** C-30 fires when prohibition instructions enumerate specific disallowed forms without a semantic equivalence clause. Round 7 showed V-01's C-27 fail had "not by reference to the table above" as a single parenthetical — one form named, no equivalence. V-03's C-27 pass added "or any equivalent back-reference." Adding equivalence clauses to both the column content exclusivity instruction (C-25) and the roll-up mechanisms-cited field instruction (C-27) converts named prohibitions from exhaustive lists to representative samples: an unlisted synonym that achieves the same prohibited effect is caught by the clause rather than requiring the instruction to enumerate every possible form. No CROSS-AUDIT row — C-29 fails by design; the pre-declaration and mechanism column are both present but their alignment is reader-inferred, not output-stated.

---

You are running a permissions trace signal for: {{topic}}

---

## TRIGGER RULE REGISTRY

| Rule ID | Fires When | Severity |
|---------|-----------|----------|
| TR-01 | Sensitive field DELTA shows `MISSING-PROFILE` | HIGH |
| TR-02 | ADMIN OWD = Organization AND entity is sensitive | HIGH |
| TR-03 | DELTA shows `TEAM-GAP` AND self-addition = YES | MEDIUM |
| TR-04 | DELTA shows `CONFLICT:[rule]` AND rule grants beyond OWD | MEDIUM |
| TR-05 | DELTA shows `ESCALATION-OPEN` | HIGH |

No-judgment mandate: HIGH or MEDIUM without a named TR rule = protocol violation.

---

## PHASE 0 — INERTIA INVENTORY

| Entity | Setting | Current Value | Stock Default | Category (INERTIA / DESIGN) |

All OWDs, FLS profiles, sharing rules, role assignments, team memberships — complete before Phase 1.

---

## PHASE 1 — CEILING AND FLOOR

Section open — compound block format active.

For each entity:
```
Entity: [Dataverse system name]
ADMIN  | OWD: [level/scope]  Privs: [Create/Read/Write/Delete/Assign — Y/N]  FLS: [profile per sensitive field or NONE]  Stock Default OWD: [from Phase 0]
CS     | OWD: [level/scope]  Privs: [Create/Read/Write/Delete/Assign — Y/N]  FLS: [profile per sensitive field or NONE]
DELTA  | [typed token list or NONE]
```

DELTA tokens: `MISSING-PROFILE` / `RESTRICTED-READ` / `RESTRICTED-WRITE` / `OVER-EXPOSED` / `SCOPE-NARROWED:[from→to]` / `FLS-GAP:[field]` / `ESCALATION-OPEN` / `TEAM-GAP` / `CONFLICT:[rule name]` / `NONE`. Sentences in DELTA = violation.

Entity closure:
```
ENTITY [name] | Operations reviewed: [list] | Fields confirmed: [list] | Gaps tallied: [count or NONE]
```

---

## PHASE 2 — FIELD-LEVEL SECURITY DETAIL

For each sensitive field with non-NONE FLS-related token in Phase 1:
```
Entity.Field: [Dataverse system name]
ADMIN  | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N  Stock Default: [from Phase 0]
CS     | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N
DELTA  | [MISSING-PROFILE / RESTRICTED-READ / RESTRICTED-WRITE / OVER-EXPOSED / NONE]
```

---

## PHASE 3 — GAP REGISTER

| Gap ID | Source | Entity.Field | DELTA Tokens | Category (Phase 0) | TR Rule | Severity |

Row protocol: copy DELTA tokens → identify TR rules → assign severity → blank TR on HIGH/MEDIUM = PROTOCOL VIOLATION.

---

## PHASE 4 — ESCALATION ANALYSIS

### Pre-Declaration Block

For each Write-capable role, declare structural assumptions before analysis begins:
```
Role: [Dataverse system name]
Pre-declaration: [name each structural assumption governing NOT POSSIBLE verdicts for this role]
```

### Escalation Vector Table

| Vector Type | Assumption (pre-declared) | Evidence Examined | Verdict | Closing Mechanism |
|-------------|--------------------------|-------------------|---------|-------------------|

**Closing Mechanism column** — content exclusivity rule (with equivalence clause):
- One structural fact only: the specific privilege or configuration state confirmed absent
- Do not write: verdict language ("NOT POSSIBLE because..."), declaration traces ("confirms pre-declared assumption"), placeholder text ("N/A"), or any equivalent form that co-mingles content from another structural site rather than stating the structural fact alone — whether that form is a sentence, a label, a parenthetical phrase, or any other construction that shifts the evidential work to another location
- POSSIBLE rows: leave this column empty

### Per-Role Roll-Up

After vector table:
```
Role: [system name]
Vectors assessed: [count]
Composite verdict: [name each NOT POSSIBLE vector's mechanism type inline]
Mechanisms cited: [restate each closing mechanism inline]
```

**Mechanisms-cited field instruction** — anti-back-reference rule (with equivalence clause):
Do not write: "see table above", "mechanisms cited in Phase 4", "as documented in the vector table", "see vectors above", "consistent with the mechanisms identified earlier", or any equivalent construction that delegates mechanism content to another section rather than restating it here — whether expressed as a direct reference, an indirect pointer, a phrase such as "as noted above," or any paraphrase that instructs the reader to consult another location for the substantive content.

Restate each mechanism inline. Every NOT POSSIBLE vector's closing mechanism must appear in this field.

No-finding format:
```
Checked: [vector types examined]  Confirmed: [structural bases]  Conclusion: no escalation path from [role].
```

---

## PHASE 5 — SHARING RULE CONFLICTS

```
Rule: [Dataverse system name]
ADMIN  | Grants: [source → target]  Level: [access]  Stock Default: [exists in stock / not in stock]
CS     | Received: [level]  Expected by OWD: [level]
DELTA  | [CONFLICT:[rule name] or NONE]  TR: [TR-04 if fires]
```

Three-field clean verdict:
```
Checked: [rule name]  Confirmed: [no expansion beyond OWD]  Conclusion: no conflict for [role].
```

---

## PHASE 6 — TEAM MEMBERSHIP GAPS

```
Team: [name]
ADMIN  | Required role: [system name]  Self-add: [YES/NO]  Category: [from Phase 0]
CS     | Membership: [IN-TEAM / NOT-IN-TEAM / CONDITIONAL]
DELTA  | [TEAM-GAP or NONE]  TR: [TR-03 if fires]  Scenario impact: [specific]
```

Three-field no-dependency verdict:
```
Checked: [team name]  Confirmed: [role not in team or self-add blocked]  Conclusion: no team gap for [role].
```

---

## PHASE 7 — CROSS-ROLE INTERACTION

```
Interaction: [Role A] + [Role B] on [Entity]
ADMIN  | Role A privileges: [list]
CS     | Role B privileges: [list]
DELTA  | Superset exceeding either alone: [list or NONE]  New TR conditions: [list or NONE]
```

---

## PHASE 8 — CATEGORIZATION GATE

Every Phase 3 gap must appear here.

| Gap ID | Entity.Field | Current State | Category (INERTIA / DESIGN) | Stock Default (INERTIA) | Admin Decision Context (DESIGN) |

---

## PHASE 9 — DUAL REMEDIATION TRACKS

### TRACK A — INERTIA
```
Gap: [Gap ID]  TR resolved: [rule ID]
ADMIN  | Platform default: [from Phase 0]
CS     | Target: [required value]
DELTA  | Enable [setting] on [entity/field] in [solution]. First-time configuration. After fix: [delta].
```

### TRACK B — DESIGN
```
Gap: [Gap ID]  TR resolved: [rule ID]
ADMIN  | Current (deliberate): [value]  Decision context: [from Phase 8]
CS     | Target: [corrected value]
DELTA  | Change [setting] from [A] to [B] in [solution]. Reverses [decision context]. After fix: [delta].
```

---

## V-03 — Lifecycle Emphasis: Four-Phase Vector Chain

**Axis:** Lifecycle emphasis — each escalation vector section has four mandatory lifecycle phases (DECLARE / ANALYZE / FILE / AUDIT); AUDIT is a blocking gate that cannot be omitted (C-29 single-axis)
**Hypothesis:** V-01 adds a CROSS-AUDIT row to the compound block — a format-level constraint. V-03 tests whether making the cross-audit a mandatory lifecycle phase, with its own section header and a gate rule, produces the same structural output through a different architectural choice. When the audit is a phase rather than a row, omitting it is a section omission — more structurally visible than a missing row. The AUDIT phase in V-03 carries its own header, its own blocking condition, and explicit "PHASE D cannot be omitted" language. Prediction: AUDIT-as-phase produces equivalent C-29 pass rate to AUDIT-as-row (V-01), but may interact differently with C-20/C-21 because the phase boundaries force declaration and filing into explicit non-overlapping positions. No equivalence clause — C-30 fails by design.

---

You are running a permissions trace signal for: {{topic}}

---

## TRIGGER RULE REGISTRY

| Rule ID | Fires When | Severity |
|---------|-----------|----------|
| TR-01 | `MISSING-PROFILE` on sensitive field | HIGH |
| TR-02 | ADMIN OWD = Organization AND entity is sensitive | HIGH |
| TR-03 | `TEAM-GAP` AND self-addition = YES | MEDIUM |
| TR-04 | `CONFLICT:[rule]` AND rule grants beyond OWD | MEDIUM |
| TR-05 | `ESCALATION-OPEN` | HIGH |

---

## STEP A — INERTIA INVENTORY

| Entity | Setting | Current Value | Stock Default | Category (INERTIA / DESIGN) |

---

## STEP B — CEILING AND FLOOR

Compound block format active throughout.

```
Entity: [Dataverse system name]
ADMIN  | OWD: [level/scope]  Privs: [Y/N each]  FLS: [profile per sensitive field or NONE]  Stock Default: [Step A]
CS     | OWD: [level/scope]  Privs: [Y/N each]  FLS: [profile per sensitive field or NONE]
DELTA  | [token list or NONE]
```

Entity closure: `ENTITY [name] | Ops reviewed: [list] | Fields confirmed: [list] | Gaps: [count or NONE]`

---

## STEP C — FIELD-LEVEL SECURITY

```
Entity.Field: [system name]
ADMIN  | FLS Profile: [name/NONE]  Read: Y/N  Write: Y/N  Stock Default: [Step A]
CS     | FLS Profile: [name/NONE]  Read: Y/N  Write: Y/N
DELTA  | [MISSING-PROFILE / RESTRICTED-READ / RESTRICTED-WRITE / OVER-EXPOSED / NONE]
```

---

## STEP D — GAP REGISTER

| Gap ID | Source | Entity.Field | DELTA Tokens | Category (Step A) | TR Rule | Severity |

HIGH/MEDIUM with blank TR Rule = PROTOCOL VIOLATION.

---

## STEP E — ESCALATION ANALYSIS — FOUR-PHASE VECTOR PROTOCOL

Each escalation vector for each Write-capable role follows four phases. **All four phases are mandatory for NOT POSSIBLE vectors. Omitting PHASE D is a blocking protocol violation — populate before advancing to the next vector.**

```
## Vector: [mechanism type] | Role: [Dataverse system name]

### PHASE A — DECLARE
Structural assumption: [The specific structural fact that, if confirmed, will support a NOT POSSIBLE verdict — e.g., "no criteria-based sharing rule exists that grants cross-BU record access for this OWD setting"]

### PHASE B — ANALYZE
Evidence examined: [configuration state, rule set, or privilege structure inspected]
Verdict: POSSIBLE / NOT POSSIBLE

### PHASE C — FILE
Closing mechanism: [For NOT POSSIBLE: one structural fact — the specific privilege or configuration state confirmed absent. For POSSIBLE: leave this section empty.]

### PHASE D — AUDIT
Declaration (Phase A): "[copy exact text from Phase A structural assumption]"
Mechanism filed (Phase C): "[copy exact text from Phase C closing mechanism]"
Audit result: CONFIRMED — declaration and filed mechanism name the same structural fact.
  [If they name different facts: MISMATCH — [describe the divergence between Phase A and Phase C]]
```

PHASE D is a gate. A NOT POSSIBLE vector with no PHASE D block has not completed the four-phase protocol. Do not advance to the next vector or to the roll-up until PHASE D is written.

### Per-Role Roll-Up (after all vectors for the role)

```
Role: [system name]
Vectors assessed: [count]
Composite verdict: [name each NOT POSSIBLE vector's mechanism type inline]
Mechanisms cited: [restate each closing mechanism inline — do not reference Phase C sections above]
```

No-finding declaration:
```
Checked: [vector types]  Confirmed: [structural bases]  Conclusion: no escalation path from [role].
```

---

## STEP F — SHARING RULE CONFLICTS

```
Rule: [system name]
ADMIN  | Grants: [source → target]  Level: [access]  Stock Default: [Step A]
CS     | Received: [level]  Expected by OWD: [level]
DELTA  | [CONFLICT:[rule] or NONE]  TR: [TR-04 if fires]
```
Three-field clean verdict: `Checked: [rule]  Confirmed: [no expansion]  Conclusion: no conflict for [role].`

---

## STEP G — TEAM MEMBERSHIP GAPS

```
Team: [name]
ADMIN  | Required role: [system name]  Self-add: [YES/NO]  Category: [Step A]
CS     | Membership: [IN-TEAM / NOT-IN-TEAM / CONDITIONAL]
DELTA  | [TEAM-GAP or NONE]  TR: [TR-03 if fires]  Scenario impact: [specific]
```
Three-field no-dependency: `Checked: [team]  Confirmed: [not in team or blocked]  Conclusion: no gap for [role].`

---

## STEP H — CROSS-ROLE INTERACTION

```
Interaction: [Role A] + [Role B] on [Entity]
ADMIN  | Role A: [privs]
CS     | Role B: [privs]
DELTA  | Superset: [list or NONE]  New TR: [list or NONE]
```

---

## STEP I — CATEGORIZATION GATE

| Gap ID | Entity.Field | Current State | Category | Stock Default (INERTIA) | Admin Decision Context (DESIGN) |

---

## STEP J — DUAL REMEDIATION TRACKS

### TRACK A — INERTIA
```
Gap: [ID]  TR resolved: [rule]
ADMIN  | Platform default: [Step A]
CS     | Target: [value]
DELTA  | Enable [setting] on [entity/field] in [solution]. First-time config — shipped with [default]. After fix: [delta].
```

### TRACK B — DESIGN
```
Gap: [ID]  TR resolved: [rule]
ADMIN  | Current (deliberate): [value]  Context: [Step I]
CS     | Target: [value]
DELTA  | Change [setting] from [A] to [B] in [solution]. Reverses [context]. After fix: [delta].
```

---

## V-04 — Combined: CROSS-AUDIT Row + Equivalence Clauses

**Axis:** Output format (C-29 — CROSS-AUDIT row in vector block) + phrasing register (C-30 — equivalence clauses in prohibition instructions)
**Hypothesis:** V-01 showed that a CROSS-AUDIT row added to the vector compound block provides output-stated alignment between declaration and mechanism, satisfying C-29. V-02 showed that equivalence clauses in prohibition instructions close the enumeration gap, satisfying C-30. V-04 tests whether the two constraints compound cleanly. Expected: CROSS-AUDIT rows provide C-29 independently of any prohibition instruction changes; equivalence clauses provide C-30 independently of the CROSS-AUDIT row. Combined, neither constraint should interfere with the other — C-29 operates at the vector level, C-30 operates at the instruction level. A combined prompt should pass both without regression on C-25/C-27 (which the equivalence clauses extend, not replace).

---

You are running a permissions trace signal for: {{topic}}

---

## TRIGGER RULE REGISTRY

| Rule ID | Fires When | Severity |
|---------|-----------|----------|
| TR-01 | `MISSING-PROFILE` on sensitive field | HIGH |
| TR-02 | ADMIN OWD = Organization AND entity is sensitive | HIGH |
| TR-03 | `TEAM-GAP` AND self-addition = YES | MEDIUM |
| TR-04 | `CONFLICT:[rule]` AND rule grants beyond OWD | MEDIUM |
| TR-05 | `ESCALATION-OPEN` | HIGH |

No-judgment mandate: HIGH or MEDIUM without named TR rule = protocol violation.

---

## STEP 0 — INERTIA INVENTORY

| Entity | Setting | Current Value | Stock Default | Category (INERTIA / DESIGN) |

---

## STEP 1 — CEILING AND FLOOR

Compound block format active.

```
Entity: [Dataverse system name]
ADMIN  | OWD: [level/scope]  Privs: [Y/N each]  FLS: [profile per sensitive field or NONE]  Stock Default: [Step 0]
CS     | OWD: [level/scope]  Privs: [Y/N each]  FLS: [profile per sensitive field or NONE]
DELTA  | [token list or NONE]
```

Entity closure: `ENTITY [name] | Ops reviewed: [list] | Fields: [list] | Gaps: [count or NONE]`

---

## STEP 2 — FIELD-LEVEL SECURITY

```
Entity.Field: [system name]
ADMIN  | FLS Profile: [name/NONE]  Read: Y/N  Write: Y/N  Stock Default: [Step 0]
CS     | FLS Profile: [name/NONE]  Read: Y/N  Write: Y/N
DELTA  | [MISSING-PROFILE / RESTRICTED-READ / RESTRICTED-WRITE / OVER-EXPOSED / NONE]
```

---

## STEP 3 — GAP REGISTER

| Gap ID | Source | Entity.Field | DELTA Tokens | Category (Step 0) | TR Rule | Severity |

HIGH/MEDIUM blank TR = PROTOCOL VIOLATION.

---

## STEP 4 — ESCALATION ANALYSIS

### Pre-Declaration Block

```
Role: [Dataverse system name]
Pre-declaration:
  - [Assumption per vector type, stated before analysis — e.g., "no criteria-based sharing rule grants cross-BU scope for this OWD"]
```

### Escalation Vector Table

| Vector Type | Assumption Declared | Evidence | Verdict | Closing Mechanism | CROSS-AUDIT |
|-------------|--------------------|-----------|---------|--------------------|-------------|

**Closing Mechanism column** — content exclusivity rule (with equivalence clause):
- One structural fact only: the specific privilege or configuration state confirmed absent
- Prohibited forms (representative, not exhaustive): verdict language ("NOT POSSIBLE because..."), declaration traces ("confirms pre-declared assumption"), placeholder text ("N/A"), prose sentences re-describing the verdict, co-mingled content from another section — or any equivalent form that places evidential work outside this column rather than stating the structural fact here
- POSSIBLE rows: leave this column empty

**CROSS-AUDIT column** — mandatory for all NOT POSSIBLE rows:
```
Pre-decl: "[exact text from Assumption Declared]" | Filed: "[exact text from Closing Mechanism]" | Match: CONFIRMED
```
Mismatch: `Pre-decl: "[text]" | Filed: "[text]" | Match: MISMATCH: [describe divergence]`
POSSIBLE rows: empty. NOT POSSIBLE row with blank CROSS-AUDIT = format violation.

### Per-Role Roll-Up

```
Role: [system name]
Vectors assessed: [count]
Composite verdict: [name each NOT POSSIBLE vector's mechanism type inline — e.g., "sharing: no criteria-based rule; team: no owner-access team; field: FLS denies write; hierarchy: BU-only scope"]
Mechanisms cited: [restate each closing mechanism inline]
```

**Mechanisms-cited field instruction** — anti-back-reference (with equivalence clause):
Restate each mechanism inline. Prohibited forms (representative, not exhaustive): "see table above", "see vector table", "mechanisms cited in Step 4", "as documented above", "consistent with the mechanisms identified earlier", "see Phase X" — or any equivalent construction that delegates mechanism content to another section rather than restating it here, whether expressed as a direct reference, an indirect pointer, or any paraphrase that instructs the reader to consult another location.

No-finding:
```
Checked: [vector types]  Confirmed: [structural bases]  Conclusion: no escalation path from [role].
```

---

## STEP 5 — SHARING RULE CONFLICTS

```
Rule: [system name]
ADMIN  | Grants: [source → target]  Level: [access]  Stock Default: [Step 0]
CS     | Received: [level]  Expected by OWD: [level]
DELTA  | [CONFLICT:[rule] or NONE]  TR: [TR-04 if fires]
```
Three-field clean: `Checked: [rule]  Confirmed: [no expansion]  Conclusion: no conflict for [role].`

---

## STEP 6 — TEAM MEMBERSHIP GAPS

```
Team: [name]
ADMIN  | Required role: [system name]  Self-add: [YES/NO]  Category: [Step 0]
CS     | Membership: [IN-TEAM / NOT-IN-TEAM / CONDITIONAL]
DELTA  | [TEAM-GAP or NONE]  TR: [TR-03 if fires]  Scenario impact: [specific]
```
Three-field no-dependency: `Checked: [team]  Confirmed: [not in team or blocked]  Conclusion: no gap for [role].`

---

## STEP 7 — CROSS-ROLE INTERACTION

```
Interaction: [Role A] + [Role B] on [Entity]
ADMIN  | Role A: [privs]
CS     | Role B: [privs]
DELTA  | Superset: [list or NONE]  New TR: [list or NONE]
```

---

## STEP 8 — CATEGORIZATION GATE

| Gap ID | Entity.Field | Current State | Category | Stock Default (INERTIA) | Admin Decision Context (DESIGN) |

---

## STEP 9 — DUAL REMEDIATION TRACKS

### TRACK A — INERTIA
```
Gap: [ID]  TR resolved: [rule]
ADMIN  | Platform default: [Step 0]
CS     | Target: [value]
DELTA  | Enable [setting] on [entity/field] in [solution]. First-time config — default was [value]. After fix: [delta].
```

### TRACK B — DESIGN
```
Gap: [ID]  TR resolved: [rule]
ADMIN  | Current (deliberate): [value]  Context: [Step 8]
CS     | Target: [value]
DELTA  | Change [setting] from [A] to [B] in [solution]. Reverses [context]. After fix: [delta].
```

---

## V-05 — Full Protocol: C-29 + C-30 on Complete Established v7 Scaffold

**Axis:** Combined — C-29 (CROSS-AUDIT row) + C-30 (equivalence clauses) on the complete established protocol with all prior criteria (C-01–C-28) retained; compliance self-check extended to cover C-29 and C-30
**Hypothesis:** The v7 scaffold satisfied C-01 through C-28 by composing ceiling-first sequencing, compound blocks, dual remediation tracks, inertia inventory, TR-rule derivation, entity closure parity, multi-vector escalation with pre-declaration, dedicated closing mechanism column with content exclusivity, roll-up with mechanism restatement, anti-back-reference field instruction, three-field no-finding format at all required sites, and composite verdict with mechanism types per vector. V-05 adds C-29 CROSS-AUDIT rows and C-30 equivalence clauses on top without removing any prior constraint. The compliance self-check gains two new rows. Expected: no regression on C-01–C-28 because the additions extend, not modify, existing structural positions; C-29 and C-30 both satisfied by the new rows and instruction clauses.

---

You are running a permissions trace signal for: {{topic}}

---

## MASTER PROTOCOL — SEVEN STRUCTURAL CONSTRAINTS

**P-1 CEILING FIRST:** Admin ceiling established before any CS access is stated per entity. CS rows express deltas from the ceiling.

**P-2 COMPOUND BLOCKS:** All comparative sections use Admin / CS / Delta typed rows. DELTA rows carry typed tokens. Sentences in DELTA = format violation.

**P-3 STOCK DEFAULTS AS BASELINE:** Every OWD, FLS profile, and sharing rule table carries a Stock Default entry. No permission described without stating the platform default.

**P-4 DUAL REMEDIATION TRACKS:** Every gap is categorized INERTIA or DESIGN before remediation. Categorization gate is blocking — uncategorized gap does not proceed.

**P-5 NO-JUDGMENT MANDATE:** Every HIGH or MEDIUM in the Gap Register cites a named TR rule. Blank TR on HIGH/MEDIUM = protocol violation requiring repair.

**P-6 CROSS-AUDIT ASSERTION:** For every NOT POSSIBLE escalation vector where C-20 (pre-declaration) and C-21 (dedicated closing column) are both present, the vector block includes a CROSS-AUDIT row explicitly confirming that the declaration and the filed mechanism name the same structural fact. Reader-inferred alignment is not sufficient — the assertion must be output-stated.

**P-7 EQUIVALENCE CLOSURE:** All prohibition instructions name specific disallowed forms AND include an equivalence clause. The named forms are representative samples, not exhaustive lists. Unlisted synonyms achieving the same prohibited effect are caught by the clause.

---

## STEP 0 — TRIGGER RULE REGISTRY

| Rule ID | Fires When | Severity |
|---------|-----------|----------|
| TR-01 | `MISSING-PROFILE` on sensitive field | HIGH |
| TR-02 | ADMIN OWD = Organization AND entity is sensitive | HIGH |
| TR-03 | `TEAM-GAP` AND self-addition = YES | MEDIUM |
| TR-04 | `CONFLICT:[rule]` AND rule grants beyond OWD | MEDIUM |
| TR-05 | `ESCALATION-OPEN` | HIGH |

No-judgment mandate active. HIGH/MEDIUM without named TR = PROTOCOL VIOLATION.

---

## STEP 1 — INERTIA INVENTORY (P-3 + P-4 setup)

Label every permission before analysis. Feeds categorization gate at Step 8.

| Entity | Setting | Current Value | Stock Default | Category (INERTIA / DESIGN) |

OWDs, FLS profiles, sharing rules, role assignments, team memberships — all included. Missing category = fail.

---

## STEP 2 — CEILING ESTABLISHMENT (P-1 + P-2 + P-3)

Section open — compound block format active.

```
Entity: [Dataverse system name]
ADMIN  | OWD: [level/scope]  Privs: [Create/Read/Write/Delete/Assign — Y/N]  FLS: [profile per sensitive field or NONE]  Stock Default OWD: [Step 1]
CS     | OWD: [level/scope]  Privs: [Create/Read/Write/Delete/Assign — Y/N]  FLS: [profile per sensitive field or NONE]
DELTA  | [typed token list or NONE]
```

DELTA tokens: `MISSING-PROFILE` / `RESTRICTED-READ` / `RESTRICTED-WRITE` / `OVER-EXPOSED` / `SCOPE-NARROWED:[from→to]` / `FLS-GAP:[field]` / `ESCALATION-OPEN` / `TEAM-GAP` / `CONFLICT:[rule name]` / `NONE`. Sentences in DELTA = violation.

Entity closure before advancing (applies to all entities regardless of gap state):
```
ENTITY [name] | Operations reviewed: [list] | Fields confirmed: [list] | Gaps tallied: [count or NONE]
```
Gap-containing entities: name the specific gaps. Implicit transition = fail.

---

## STEP 3 — FIELD-LEVEL SECURITY DETAIL (P-2)

Section open — compound block format active.

```
Entity.Field: [Dataverse system name]
ADMIN  | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N  Stock Default: [Step 1]
CS     | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N
DELTA  | [MISSING-PROFILE / RESTRICTED-READ / RESTRICTED-WRITE / OVER-EXPOSED / NONE]
```

Sensitive entity absent from Step 3 when it appeared in Step 2 = fail.

---

## STEP 4 — GAP REGISTER (P-5)

Gaps sourced from DELTA tokens in Steps 2–3 only. Gaps logged progressively as each entity/field section closes — not consolidated post-trace.

| Gap ID | Source | Entity.Field | DELTA Tokens | Category (Step 1) | TR Rule | Severity |

Row protocol:
1. Copy DELTA tokens from source block
2. Identify TR rules that fire — list all
3. Assign highest severity. No rule fires → LOW, TR = N/A
4. HIGH or MEDIUM: TR Rule populated → blank = PROTOCOL VIOLATION → repair before next row
5. Category: from Step 1 → absent category requires Step 1 update first

---

## STEP 5 — ESCALATION ANALYSIS (P-2 + P-6)

### Pre-Declaration Block (P-6 — before any vector content)

For each Write-capable role:
```
Role: [Dataverse system name]
Pre-declaration:
  - [Vector type A]: [Structural assumption — the specific configuration state or access boundary that will support NOT POSSIBLE if confirmed]
  - [Vector type B]: [Structural assumption]
  - [Additional vectors as needed]
```

Assumptions declared before analysis. NOT POSSIBLE verdict without matching prior declaration = contract violation.

### Escalation Vector Table (P-6)

For each Write-capable role, after the Pre-Declaration block:

| Vector Type | Assumption Declared | Evidence Examined | Verdict | Closing Mechanism | CROSS-AUDIT |
|-------------|--------------------|--------------------|---------|-------------------|-------------|

**Closing Mechanism column instruction (P-7 — equivalence clause active):**
One structural fact only — the specific privilege or configuration state confirmed absent for this vector.
Prohibited forms (representative, not exhaustive): verdict language ("NOT POSSIBLE because..."), declaration traces ("confirms declared assumption above"), placeholder text ("N/A"), prose re-describing the verdict, or any equivalent form that co-mingles content from another structural site, delegates the evidential statement to another section, or requires the reader to look elsewhere to find the structural fact — whether expressed as a sentence, a pointer, a parenthetical, or any other construction.
POSSIBLE rows: leave empty.

**CROSS-AUDIT column instruction (P-6 — mandatory for NOT POSSIBLE rows):**
```
Pre-decl: "[exact text from Assumption Declared column for this row]" | Filed: "[exact text from Closing Mechanism column for this row]" | Match: CONFIRMED
```
If declaration and filed mechanism name different structural facts:
```
Pre-decl: "[text]" | Filed: "[text]" | Match: MISMATCH: [describe the divergence]
```
POSSIBLE rows: leave empty. NOT POSSIBLE row with blank CROSS-AUDIT = format violation — populate before advancing.

Three-field no-finding at escalation no-path site:
```
Checked: [vector types examined]  Confirmed: [each structural basis named]  Conclusion: no escalation path from [role].
```

### Per-Role Roll-Up (after all vectors)

```
Role: [system name]
Vectors assessed: [count] | POSSIBLE: [count] | NOT POSSIBLE: [count]
Composite verdict: [name each NOT POSSIBLE vector's mechanism type inline — e.g., "sharing: no criteria-based rule; team: no owner-access team accepts this role; field inheritance: FLS denies write; role hierarchy: BU-only scope; assignment: no auto-assign broadens access"]
Mechanisms cited: [restate each closing mechanism inline]
```

**Mechanisms-cited field instruction (P-7 — equivalence clause active):**
Restate each closing mechanism inline within this field. Prohibited forms (representative, not exhaustive): "see table above", "see vector table", "mechanisms cited in Step 5", "as documented above", "consistent with mechanisms identified earlier", "see Phase X" — or any equivalent construction that delegates mechanism content to another section rather than restating it here, whether expressed as a direct reference, an indirect pointer, a phrase such as "as noted above" or "per the analysis above," or any paraphrase that directs the reader to another location for the substantive mechanism content.

---

## STEP 6 — SHARING RULE CONFLICTS (P-2)

Section open — compound block format active.

```
Rule: [Dataverse system name]
ADMIN  | Grants: [source → target]  Level: [access]  Stock Default: [exists in stock / not in stock]
CS     | Received: [level]  Expected by OWD: [level]
DELTA  | [CONFLICT:[rule name] or NONE]  TR: [TR-04 if fires]
```

Three-field no-conflict verdict (required per role, not only where conflicts found):
```
Checked: [rule name or rule type examined]  Confirmed: [access level matches OWD ceiling; no cross-BU expansion confirmed]  Conclusion: no conflict — [role] sharing rules do not exceed OWD ceiling.
```

---

## STEP 7 — TEAM MEMBERSHIP GAPS (P-2)

Section open — compound block format active.

```
Team: [name]
ADMIN  | Required role: [system name]  Self-add: [YES/NO]  Category: [from Step 1]
CS     | Membership: [IN-TEAM / NOT-IN-TEAM / CONDITIONAL]
DELTA  | [TEAM-GAP or NONE]  TR: [TR-03 if TEAM-GAP + YES]  Scenario impact: [specific, not generic]
```

Three-field no-dependency verdict:
```
Checked: [team name]  Confirmed: [role not in team, or self-add blocked by named mechanism]  Conclusion: no team membership gap for [role] — [team] does not grant access beyond current OWD.
```

---

## STEP 7B — CROSS-ROLE INTERACTION (P-2)

Section open — compound block format active.

```
Interaction: [Role A] + [Role B] on [Entity]
ADMIN  | Role A privileges: [list]
CS     | Role B privileges: [list]
DELTA  | Superset exceeding either alone: [list or NONE]  New TR conditions: [list or NONE]
```

At least one multi-role scenario required.

---

## STEP 8 — CATEGORIZATION GATE (P-4)

Every gap from Step 4 must appear here before Step 9.

| Gap ID | Entity.Field | Current State | Category (INERTIA / DESIGN) | Stock Default (INERTIA) | Admin Decision Context (DESIGN) |

Missing gap = gate failure. Gap with no category = gate failure. A gap that crosses this gate without a category does not proceed to Step 9.

---

## STEP 9 — DUAL REMEDIATION TRACKS (P-4)

Every Step 4 gap in exactly one track. TR rule resolved cited per entry.

### TRACK A — INERTIA Gaps (platform default, never configured)

```
Gap: [Gap ID]  TR resolved: [rule ID]
ADMIN  | Platform default: [from Step 1]
CS     | Target state: [required value]
DELTA  | Action: Enable [setting] on [entity/field] in [solution]. First-time configuration — platform shipped with [default from Step 1]. After fix: [behavioral delta].
```

### TRACK B — DESIGN Gaps (deliberate configuration that is wrong)

```
Gap: [Gap ID]  TR resolved: [rule ID]
ADMIN  | Current (deliberate): [value]  Decision context: [from Step 8]
CS     | Target state: [corrected value]
DELTA  | Action: Change [setting] on [entity/field] in [solution] from [A] to [B]. Reverses [decision context from Step 8]. After fix: [behavioral delta].
```

Identical action format across tracks = fail. Generic advice = fail. Each gap in exactly one track.

---

## STEP 10 — COMPLIANCE SELF-CHECK

Before submitting, verify all seven structural constraints:

| Constraint | Check |
|------------|-------|
| P-1 CEILING FIRST | No CS row appears without a prior ADMIN row in the same block |
| P-2 COMPOUND BLOCKS | Every comparative section has Admin/CS/Delta rows; no DELTA row contains a sentence |
| P-3 STOCK DEFAULTS | Every entity in Step 2 ADMIN row includes Stock Default OWD; every FLS entry includes Stock Default |
| P-4 DUAL TRACKS | Every Step 4 gap appears in Step 8 and in exactly one Step 9 track |
| P-5 NO-JUDGMENT | Every HIGH or MEDIUM in Step 4 has a named TR rule |
| P-6 CROSS-AUDIT | Every NOT POSSIBLE vector in Step 5 has a populated CROSS-AUDIT column confirming declaration-mechanism match |
| P-7 EQUIVALENCE CLOSURE | Closing Mechanism column instruction includes equivalence clause; Mechanisms-cited field instruction includes equivalence clause |

Any unchecked item requires revision before submission.
