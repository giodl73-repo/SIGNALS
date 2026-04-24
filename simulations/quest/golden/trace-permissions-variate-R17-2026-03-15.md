# trace-permissions Variate — Round 3 (Rubric v3)
**Date:** 2026-03-15
**Rubric:** v3 (C-01 through C-15)
**Round note:** R2 (Round 2) best performers V-02 (107.5) and V-04 (112.5) used compound Admin/CS/Delta blocks; V-03 (100) introduced separate INERTIA/DESIGN remediation paths; V-01 (107.5) introduced protocol-violation framing for uncited severity. This round extracts those three excellence signals as single-axis variations, then combines.
**Target criteria:** C-13 (compound block format — delta as typed rows, never narrative), C-14 (inertia vs design dual remediation track), C-15 (no-judgment mandate — every gap row cites a TR rule; complete coverage, not minimum-bar)
**Prior criteria retained:** C-01–C-12 structurally enforced throughout

---

## Round 3 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format — explicit three-row compound blocks with typed DELTA tokens (C-13 single-axis) | Requiring a named DELTA token per block prevents the model from writing delta as explanatory prose; a sentence in the DELTA row fails the format check before content is evaluated, making the constraint structural rather than stylistic |
| V-02 | Inertia framing — categorization gate before remediation splits INERTIA and DESIGN into distinct fix paths (C-14 single-axis) | Adding a mandatory gate between gap identification and remediation forces the model to label every finding before reaching for a fix; the gate is binary — a finding without a category cannot cross it — making track selection a structural pass/fail condition |
| V-03 | Phrasing register — protocol-violation framing for uncited severity extends C-11 from minimum-bar to full-register coverage (C-15 single-axis) | C-11 requires at least one TR citation; C-15 requires zero uncited cells. Naming a blank TR cell as a "protocol violation" that must be repaired before advancing converts an omission into a blocking condition, which is a different constraint than asking for completeness |
| V-04 | Combined: compound block format (C-13) + no-judgment mandate (C-15) | DELTA tokens in compound blocks carry the observable condition that triggers TR rules; the no-judgment mandate then requires the Gap Register to trace every severity back to a DELTA token. The two constraints form a closed pipeline: observation → token → rule → severity |
| V-05 | Combined: all three (C-13 + C-14 + C-15) on the full v2 scaffold (C-10 ceiling-floor + C-11 trigger-rule + C-12 stock defaults retained) | The five constraints together close every known failure mode: sequence failure (C-10), judgment severity (C-11/C-15), inertia blindness (C-12/C-14), prose delta leakage (C-13). No gap can be identified, classified, or remediated without passing all five structural checks |

---

## V-01 — Output Format: Compound Block Format

**Axis:** Output format — compound block format with typed Admin/CS/Delta rows; delta never written as narrative prose (C-13 single-axis)
**Hypothesis:** Requiring an explicit three-row compound block per entity/field/operation removes the prose-delta escape hatch. "CS cannot write the Salary field because the FLS profile excludes write access" satisfies C-02 informationally but not structurally — the DELTA row must carry a typed token (e.g., `RESTRICTED-WRITE`), making the gap computable by inspection rather than interpretable from a sentence. Format failure is detectable before content is evaluated.

---

You are running a permissions trace signal for: {{topic}}

---

## COMPOUND BLOCK PROTOCOL

All comparative analysis in this trace uses compound blocks. No other format is valid for side-by-side comparison.

**Block structure:**
```
Subject: [Dataverse system name — entity, field, operation, or rule]
ADMIN  | [typed value — list, token, or Y/N cells]
CS     | [typed value — list, token, or Y/N cells]
DELTA  | [typed token(s) — never a sentence]
```

**DELTA row rules:**
- DELTA must be a typed value: a list, a named token, a set of Y/N cells, or the null token `NONE`
- Sentences are not permitted in DELTA. "CS lacks access because…" is a sentence. Replace with `RESTRICTED-READ` or the appropriate token
- DELTA tokens: `MISSING-PROFILE` / `RESTRICTED-READ` / `RESTRICTED-WRITE` / `OVER-EXPOSED` / `SCOPE-NARROWED:[Org→BU]` / `FLS-GAP:[field name]` / `ESCALATION-OPEN` / `TEAM-GAP` / `CONFLICT:[rule name]` / `NONE`
- Multiple tokens: comma-separated in one DELTA row

**Section-open declaration:** Re-state "compound block format active" at the start of Stage 1, Stage 2, and Stage 3 before any entity, field, or rule name appears.

---

## STAGE 1 — CEILING AND FLOOR

Section open — compound block format active.

For each entity {{topic}} operates on, produce one block:

```
Entity: [Dataverse system name]
ADMIN  | OWD: [level / scope]  Privs: [Create/Read/Write/Delete/Assign — Y or N each]  FLS: [profile per sensitive field, or NONE]
CS     | OWD: [level / scope]  Privs: [Create/Read/Write/Delete/Assign — Y or N each]  FLS: [profile per sensitive field, or NONE]
DELTA  | [token list or NONE]
```

**Constraints:**
- Roles named by Dataverse system name (e.g., `Basic User`, `Customer Service Representative`). Display names alone = fail
- OWD: access level (None / Read / Read-Write) AND scope (Organization / Business Unit / Owner) — both required per row
- Sensitive entities (PII, financial, regulated): FLS field entries must appear in ADMIN and CS rows. Entity in scope but absent from Stage 1 = fail
- At least one non-NONE DELTA row required; all-NONE DELTA rows with no subsequent Gap Register = fail

---

## STAGE 2 — FIELD-LEVEL SECURITY DETAIL

Section open — compound block format active.

For each sensitive field that produced a non-NONE DELTA token in Stage 1:

```
Entity.Field: [Dataverse system name]
ADMIN  | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N
CS     | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N
DELTA  | [MISSING-PROFILE / RESTRICTED-READ / RESTRICTED-WRITE / OVER-EXPOSED / NONE]
```

---

## STAGE 3 — GAP REGISTER

Section open — compound block format active.

Gaps originate from DELTA tokens in Stages 1 and 2 only. No gap is inserted here without a source DELTA token.

| Gap ID | Source (Stage/Block) | Entity.Field | DELTA Token(s) | TR Fired | Severity |

**Trigger rules:**
- TR-01: `MISSING-PROFILE` on sensitive field → HIGH
- TR-02: ADMIN OWD = Organization on sensitive entity → HIGH
- TR-03: `TEAM-GAP` + self-addition possible → MEDIUM
- TR-04: `CONFLICT:[rule]` where rule grants beyond OWD → MEDIUM
- TR-05: `ESCALATION-OPEN` → HIGH

Every row needs a TR Fired value. If no TR rule fires → severity = LOW, TR Fired = N/A.

---

## STAGE 4 — ESCALATION PATHS

Section open — compound block format active.

For each HIGH gap, one block:

```
Path: [ID]  Source gap: [Gap ID]
ADMIN  | Role: [system name]  Entry action: [specific action]
CS     | Starting privilege: [privilege]
DELTA  | Elevation: [access reached]  Blocker: [NONE / mechanism name]
```

No path found → DELTA row: `Elevation: NONE. Blocked by: [named mechanism]`. Section may not be empty.

---

## STAGE 5 — SHARING RULE CONFLICTS

Section open — compound block format active.

```
Rule: [Dataverse system name]
ADMIN  | Grants: [source role → target role]  Level: [access]
CS     | Received: [level]  Expected by OWD: [level]
DELTA  | [CONFLICT:[rule name] or NONE]
```

Rule must be named by system name. Abstract references fail.

---

## STAGE 6 — TEAM MEMBERSHIP GAPS

Section open — compound block format active.

```
Team: [name]
ADMIN  | Required role: [system name]  Self-add possible: [YES / NO]  Mechanism: [brief]
CS     | Membership: [IN-TEAM / NOT-IN-TEAM / CONDITIONAL]
DELTA  | [TEAM-GAP or NONE]  Scenario impact: [why it matters here specifically, not generically]
```

---

## STAGE 7 — CROSS-ROLE INTERACTION

Section open — compound block format active.

At least one scenario where a user holds two roles simultaneously:

```
Interaction: [Role A] + [Role B] on [Entity]
ADMIN  | Role A privileges: [list]
CS     | Role B privileges: [list]
DELTA  | Superset privileges exceeding either role alone: [list or NONE]
```

---

## STAGE 8 — REMEDIATION

One block per gap from Stage 3. No gap omitted.

```
Gap: [Gap ID]
ADMIN  | Current state: [value]
CS     | Target state: [value]
DELTA  | Action: Change [privilege / FLS profile / sharing rule / OWD] on [role / field / entity] in [solution location] from [A] to [B]. After fix: [behavioral delta].
```

Generic advice = fail. Named configuration change, location, and behavioral consequence required in every DELTA row.

---

## V-02 — Inertia Framing: Dual Remediation Track

**Axis:** Inertia framing — mandatory categorization gate before remediation; INERTIA and DESIGN gaps use distinct fix formats (C-14 single-axis)
**Hypothesis:** Inserting a gate between gap identification and remediation prevents the uniform-path failure. A finding categorized as INERTIA (platform default, never configured) requires first-time configuration — there is no prior state to revert. A finding categorized as DESIGN (deliberate admin choice) requires reversal — the prior decision must be named before a fix is written. Applying the same remediation format to both categories is a structural failure at the categorization gate, not a quality deficiency.

---

You are running a permissions trace signal for: {{topic}}

---

## CATEGORIZATION PROTOCOL

Before any gap receives a remediation action, it must be categorized.

**INERTIA:** The current state is the platform's out-of-the-box default. No administrator deliberately configured this value. The risk exists because no one acted.

**DESIGN:** An administrator deliberately set this value. The risk exists because the choice was wrong or has become wrong.

**Gate rule:** After the Gap Register is complete, populate the Categorization Table. A gap not in the Categorization Table may not proceed to remediation. This is a gate, not a suggestion.

---

## PHASE 1 — ENTITY AND OWD INVENTORY

For each entity {{topic}} operates on:

| Entity (system name) | OWD Level | OWD Scope | Sensitivity | Category (INERTIA / DESIGN) | Stock Default OWD |

OWD Level: None / Read / Read-Write. OWD Scope: Organization / Business Unit / Owner. Both required — level alone or scope alone = incomplete row.

All roles: Dataverse system names with record scope stated (Organization / Business Unit / Team / User).

---

## PHASE 2 — ROLE PRIVILEGE MAP

For `Customer Service` and the Dataverse security expert role as primary subjects:

| Role (system name) | Entity | Record Scope | Create | Read | Write | Delete | Assign | Category (INERTIA / DESIGN) |

Record scope required per row. Missing = incomplete row.

---

## PHASE 3 — FIELD-LEVEL SECURITY

For each sensitive entity (PII, financial, regulated), for each sensitive field:

| Entity | Field (system name) | FLS Profile (or NONE) | CS Read | CS Write | Admin Read | Admin Write | Category (INERTIA / DESIGN) |

Sensitive entity absent from this table = fail.

---

## PHASE 4 — GAP REGISTER

| Gap ID | Entity.Field | Admin State | CS State | Gap Description | TR Fired | Severity |

Trigger rules:
- TR-01: Sensitive field + FLS Profile = NONE → HIGH
- TR-02: OWD = Organization + sensitive entity → HIGH
- TR-03: Team self-addition possible → MEDIUM
- TR-04: Sharing rule grants beyond OWD → MEDIUM

Every Severity cell: cite the TR rule. Uncited severity = incomplete row.

---

## PHASE 5 — CATEGORIZATION GATE

**Gate: every gap from Phase 4 must appear here before proceeding to Phase 6.**

| Gap ID | Entity.Field | Current State | Category (INERTIA / DESIGN) | Stock Default (INERTIA only) | Admin Decision Context (DESIGN only) |

Missing gap = gate failure. Gap with no category = gate failure. A gap that crosses this gate without a category does not receive a remediation action.

---

## PHASE 6 — DUAL REMEDIATION TRACKS

Process gaps by category. Every gap from Phase 4 appears in exactly one track.

### TRACK A — INERTIA Gaps (default, never configured)

For each INERTIA gap:

`Enable [setting] on [entity/field] in [solution]. First-time configuration — platform default is [stock default from Phase 5]; this has never been changed. After fix: [behavioral delta].`

### TRACK B — DESIGN Gaps (deliberate configuration that is wrong)

For each DESIGN gap:

`Change [setting] on [entity/field] in [solution] from [A] to [B]. This reverses [admin decision context from Phase 5]. After fix: [behavioral delta].`

Applying the same action verb and context sentence format to both tracks = fail. Generic advice = fail. Each gap in exactly one track.

---

## PHASE 7 — ESCALATION PATHS

Chain format: `role → action available → elevated access reached`. Cite TR-05 if the chain qualifies.

No path: name the blocking mechanism explicitly. Do not omit.

---

## PHASE 8 — SHARING RULE CONFLICTS

Name the rule (system name). State granting role, receiving role, access level, expected level per OWD. Generic rule references fail.

---

## PHASE 9 — TEAM MEMBERSHIP GAPS

Name role, team, self-addition possibility, scenario-specific impact. TR-03 fires if self-add is YES.

---

## PHASE 10 — CROSS-ROLE INTERACTION

At least one multi-role scenario. Name both roles, trace combined privileges, state whether the combination opens a new TR condition.

---

## V-03 — Phrasing Register: No-Judgment Mandate

**Axis:** Phrasing register — protocol-violation framing for uncited severity; complete register coverage (C-15 single-axis)
**Hypothesis:** C-11 requires at least one trigger-rule escalation. C-15 requires zero subjective assignments — the entire register must be rule-derived. Framing a blank TR cell as a protocol violation (not a quality note) converts the completeness requirement into a repair condition: the row cannot be advanced until the TR cell is populated or the severity is reclassified to LOW. This structural framing closes the gap between "at least one" and "every row."

---

You are running a permissions trace signal for: {{topic}}

---

## TRIGGER RULE REGISTRY

Complete this section before writing any gap. The registry defines the only legal bases for HIGH and MEDIUM severity. Severity assignments outside this registry are not permitted.

| Rule ID | Condition | Severity | Rationale |
|---------|-----------|----------|-----------|
| TR-01 | Sensitive field (PII / financial / regulated) + FLS Profile = NONE | HIGH | Field directly readable by any holder of entity-level read access |
| TR-02 | OWD = Organization AND entity classified as sensitive | HIGH | Org-scope bypasses all ownership-based restriction |
| TR-03 | Team where self-addition is possible + access granted via team membership | MEDIUM | Role acquires team access without admin approval |
| TR-04 | Sharing rule grants access beyond the receiving role's OWD ceiling | MEDIUM | Sharing overreach persists even after OWD correction |
| TR-05 | Privilege escalation chain terminates at an entity outside the starting role's OWD | HIGH | Path reaches access not reachable through normal role boundaries |

**No-judgment mandate:** A HIGH or MEDIUM assignment not derivable from this table is not permitted. If no rule fires: severity = LOW, TR Fired = N/A. A HIGH or MEDIUM with a blank TR Fired cell is a **protocol violation** — the row must be repaired before the analysis advances.

---

## PHASE 1 — ENTITY AND OWD INVENTORY

For each entity:

| Entity (system name) | OWD Level | OWD Scope | Sensitivity |

OWD Level: None / Read / Read-Write. OWD Scope: Organization / Business Unit / Owner. Both required per row.

---

## PHASE 2 — ROLE PRIVILEGE MAP

Stock roles: `Customer Service` (CS floor) and Dataverse security expert (ceiling reference). Dataverse system names throughout.

| Role (system name) | Entity | Record Scope | Create | Read | Write | Delete | Assign |

Record scope per row: Organization / Business Unit / Team / User.

---

## PHASE 3 — FIELD-LEVEL SECURITY

For each sensitive entity:

| Entity | Sensitive Field (system name) | CS FLS Profile | CS Read | CS Write | Admin FLS Profile | Admin Read | Admin Write |

Sensitive entity absent from this table = fail.

---

## PHASE 4 — GAP REGISTER (no-judgment mandate active)

| Gap ID | Entity.Field | Admin State | CS State | Gap Description | TR Fired | Severity |

**Row completion protocol — apply before writing the next row:**

1. Identify the observable condition (structural, not evaluative)
2. Look up the Trigger Rule Registry — which rule fires, if any?
3. Assign severity from the rule. If no rule fires → Severity = LOW, TR Fired = N/A
4. If Severity = HIGH or MEDIUM: write the rule ID in TR Fired
5. Check: Is TR Fired blank while Severity is HIGH or MEDIUM? → **PROTOCOL VIOLATION — repair this row before continuing**
6. Check: Is the gap description a judgment phrase ("seems risky," "could be a concern," "may allow") rather than an observable condition? → **PROTOCOL VIOLATION — restate as structural observation before continuing**

A register row that cannot satisfy steps 4–6 is blocked. Do not advance to the next row until it is repaired.

---

## PHASE 5 — ESCALATION PATHS

For each HIGH gap: `role → action available → elevated access reached`. State which TR rule (typically TR-05) applies to the path outcome.

No path: name the blocking mechanism. Do not omit this phase.

---

## PHASE 6 — SHARING RULE CONFLICTS

Name the rule by Dataverse system name. State granting role, receiving role, access level, expected level by OWD, and which TR rule fires (if any). Generic rule references fail.

---

## PHASE 7 — TEAM MEMBERSHIP GAPS

Name role, team, self-addition status, scenario impact. If TR-03 fires, state it here.

---

## PHASE 8 — CROSS-ROLE INTERACTION

At least one multi-role scenario. Name both roles, trace combined access, identify whether the combination introduces a new TR condition.

---

## PHASE 9 — REMEDIATION

Per gap: `Change [privilege / FLS profile / sharing rule / OWD] on [role / field / entity] in [solution location] from [A] to [B]. After fix: [behavioral delta].`

Generic advice fails. Reference the TR rule being resolved.

---

## V-04 — Combined: Compound Block Format + No-Judgment Mandate

**Axis:** Output format (C-13) + phrasing register (C-15)
**Hypothesis:** DELTA tokens in compound blocks carry the observable condition that triggers TR rules. The no-judgment mandate then requires every Gap Register row to trace its severity back to a DELTA token from Stage 1 or 2. The two constraints form a closed pipeline: Stage 1/2 DELTA token → TR lookup → Gap Register Severity. A severity assignment that cannot be traced to a DELTA token is both a format failure (C-13) and a judgment violation (C-15). Neither constraint is satisfiable without the other.

---

You are running a permissions trace signal for: {{topic}}

---

## COMPOUND BLOCK PROTOCOL (active throughout all stages)

Every comparative section uses three-row blocks:
```
Subject: [Dataverse system name]
ADMIN  | [typed value]
CS     | [typed value]
DELTA  | [typed token(s) — never a sentence]
```

DELTA tokens: `MISSING-PROFILE` / `RESTRICTED-READ` / `RESTRICTED-WRITE` / `OVER-EXPOSED` / `SCOPE-NARROWED:[from→to]` / `FLS-GAP:[field]` / `ESCALATION-OPEN` / `TEAM-GAP` / `CONFLICT:[rule name]` / `NONE`

Sentences in DELTA rows are not accepted. A sentence in DELTA is a format violation — restate as a token before advancing.

---

## TRIGGER RULE REGISTRY (complete before any entity or gap content — locked after this section)

| Rule ID | Fires When DELTA Contains | Severity |
|---------|--------------------------|----------|
| TR-01 | `MISSING-PROFILE` on sensitive field | HIGH |
| TR-02 | ADMIN OWD = Organization AND entity is sensitive | HIGH |
| TR-03 | `TEAM-GAP` AND self-add = YES | MEDIUM |
| TR-04 | `CONFLICT:[rule]` where rule grants beyond OWD | MEDIUM |
| TR-05 | `ESCALATION-OPEN` | HIGH |

**No-judgment mandate:** Severity in the Gap Register is assigned by looking up the DELTA tokens from the source block against this table. No other severity basis is valid. HIGH or MEDIUM with blank TR Fired = **protocol violation** — repair before advancing.

---

## STAGE 1 — CEILING AND FLOOR ESTABLISHMENT

Section open — compound block format active.

For each entity:
```
Entity: [Dataverse system name]
ADMIN  | OWD: [level/scope]  Privs: [Create/Read/Write/Delete/Assign — Y or N]  FLS: [profile per sensitive field or NONE]
CS     | OWD: [level/scope]  Privs: [Create/Read/Write/Delete/Assign — Y or N]  FLS: [profile per sensitive field or NONE]
DELTA  | [token list or NONE]
```

Roles: system names. OWD: level AND scope both required. Sensitive entities: FLS rows mandatory.

---

## STAGE 2 — FIELD-LEVEL SECURITY DETAIL

Section open — compound block format active.

For each sensitive field with a non-NONE FLS-related token in Stage 1:
```
Entity.Field: [Dataverse system name]
ADMIN  | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N
CS     | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N
DELTA  | [MISSING-PROFILE / RESTRICTED-READ / RESTRICTED-WRITE / OVER-EXPOSED / NONE]
```

---

## STAGE 3 — GAP REGISTER

Gaps sourced from DELTA tokens in Stages 1 and 2 only.

| Gap ID | Source Block | Entity.Field | DELTA Tokens | TR Rule Lookup | Severity |

**For each row:**
1. Copy DELTA tokens from source block
2. Look up tokens against Trigger Rule Registry — list all TR rules that fire
3. Assign highest severity from fired rules. If no rule fires → LOW, TR = N/A
4. HIGH or MEDIUM: TR Rule Lookup must name the rule ID → blank TR with HIGH/MEDIUM = **protocol violation → repair this row**

---

## STAGE 4 — ESCALATION PATHS

Section open — compound block format active.

```
Path: [ID]  Source gap: [Gap ID]
ADMIN  | Role: [system name]  Entry action: [action]
CS     | Starting privilege: [privilege]
DELTA  | Elevation: [access reached or NONE]  Blocker: [NONE / mechanism]  TR: [TR-05 if ESCALATION-OPEN]
```

No path → DELTA: `Elevation: NONE. Blocked by: [mechanism]`. Section cannot be empty.

---

## STAGE 5 — SHARING RULE CONFLICTS

Section open — compound block format active.

```
Rule: [Dataverse system name]
ADMIN  | Grants: [source → target]  Level: [access]
CS     | Received: [level]  Expected by OWD: [level]
DELTA  | [CONFLICT:[rule name] or NONE]  TR: [TR-04 if CONFLICT + beyond OWD]
```

---

## STAGE 6 — TEAM MEMBERSHIP GAPS

Section open — compound block format active.

```
Team: [name]
ADMIN  | Required role: [system name]  Self-add: [YES/NO]  Mechanism: [brief]
CS     | Membership: [IN-TEAM / NOT-IN-TEAM / CONDITIONAL]
DELTA  | [TEAM-GAP or NONE]  TR: [TR-03 if TEAM-GAP + YES]  Scenario impact: [specific, not generic]
```

---

## STAGE 7 — CROSS-ROLE INTERACTION

Section open — compound block format active.

```
Interaction: [Role A] + [Role B] on [Entity]
ADMIN  | Role A privileges: [list]
CS     | Role B privileges: [list]
DELTA  | Superset exceeding either alone: [list or NONE]  New TR conditions: [list or NONE]
```

---

## STAGE 8 — REMEDIATION

One block per gap. TR rule resolved cited per block.

```
Gap: [Gap ID]  TR resolved: [rule ID]
ADMIN  | Current state: [value]
CS     | Target state: [value]
DELTA  | Action: Change [X] on [Y] in [Z] from [A] to [B]. After fix: [behavioral delta].
```

---

## V-05 — Full Protocol: Compound Blocks + Dual Remediation Track + No-Judgment Mandate

**Axis:** Combined — C-13 (compound blocks) + C-14 (inertia/design dual track) + C-15 (no-judgment mandate) on the full v2 scaffold (C-10 ceiling-floor + C-11 trigger-rule + C-12 stock defaults retained)
**Hypothesis:** The v2 scaffold delivered ceiling-floor sequencing (C-10), trigger-rule escalation (C-11), and stock defaults as baseline (C-12). The three v3 constraints slot cleanly on top: C-13 replaces any remaining prose DELTA narration with typed compound block rows; C-14 adds a categorization gate between gap identification and remediation, splitting every fix into INERTIA or DESIGN tracks; C-15 extends the no-judgment mandate from "at least one TR rule" to every Gap Register row. Five constraints close five distinct failure modes: sequence omission, judgment severity, inertia invisibility, prose delta leakage, and partial TR coverage.

---

You are running a permissions trace signal for: {{topic}}

---

## MASTER PROTOCOL — FIVE STRUCTURAL CONSTRAINTS

**P-1 CEILING FIRST (C-10):** Admin ceiling established before any CS access is stated. CS rows always express deltas from the ceiling. CS is never analyzed independently.

**P-2 COMPOUND BLOCKS (C-13):** All comparative sections use Admin / CS / Delta typed rows. DELTA rows carry typed tokens. Sentences in DELTA rows are a format violation.

**P-3 STOCK DEFAULTS AS BASELINE (C-12):** Every OWD, FLS profile, and sharing rule table carries a Stock Default column. No permission is described without stating the platform default.

**P-4 DUAL REMEDIATION TRACKS (C-14):** Every gap is categorized INERTIA or DESIGN before receiving a remediation action. The categorization gate is a blocking check — an uncategorized gap does not proceed.

**P-5 NO-JUDGMENT MANDATE (C-15):** Every HIGH or MEDIUM in the Gap Register cites a named TR rule. Blank TR Fired on a HIGH or MEDIUM row is a protocol violation requiring repair before advancing.

---

## STEP 0 — TRIGGER RULE REGISTRY (locked before any content)

| Rule ID | Fires When | Severity |
|---------|-----------|----------|
| TR-01 | Sensitive field DELTA shows `MISSING-PROFILE` | HIGH |
| TR-02 | ADMIN OWD = Organization + entity is sensitive | HIGH |
| TR-03 | DELTA shows `TEAM-GAP` + self-addition = YES | MEDIUM |
| TR-04 | DELTA shows `CONFLICT:[rule]` + rule grants beyond OWD | MEDIUM |
| TR-05 | DELTA shows `ESCALATION-OPEN` | HIGH |

Severity outside this table is not permitted at HIGH or MEDIUM. Blank TR Fired on HIGH/MEDIUM = protocol violation.

---

## STEP 1 — INERTIA INVENTORY (P-3 + P-4 setup — runs before ceiling)

Label every permission before analysis. This table feeds the categorization gate at Step 6.

| Entity | Setting | Current Value | Stock Default | Category (INERTIA / DESIGN) |

Categorize: OWDs, FLS profiles, sharing rules, role assignments, team memberships. Missing category = fail.

---

## STEP 2 — CEILING ESTABLISHMENT (P-1 + P-2 + P-3)

Section open — compound block format active.

For each entity:
```
Entity: [Dataverse system name]
ADMIN  | OWD: [level/scope]  Privs: [Create/Read/Write/Delete/Assign — Y/N]  FLS: [profile per sensitive field or NONE]  Stock Default OWD: [from Step 1]
CS     | OWD: [level/scope]  Privs: [Create/Read/Write/Delete/Assign — Y/N]  FLS: [profile per sensitive field or NONE]
DELTA  | [typed token list or NONE]
```

System names required. OWD: level AND scope. Sensitive fields: must appear in ADMIN FLS cells. DELTA: tokens, not sentences.

---

## STEP 3 — FIELD-LEVEL SECURITY DETAIL (P-2)

Section open — compound block format active.

For each sensitive field with a non-NONE FLS-related DELTA token in Step 2:
```
Entity.Field: [Dataverse system name]
ADMIN  | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N  Stock Default: [from Step 1]
CS     | FLS Profile: [name or NONE]  Read: Y/N  Write: Y/N
DELTA  | [MISSING-PROFILE / RESTRICTED-READ / RESTRICTED-WRITE / OVER-EXPOSED / NONE]
```

---

## STEP 4 — GAP REGISTER (P-5)

Gaps sourced from DELTA tokens in Steps 2–3 only.

| Gap ID | Source | Entity.Field | DELTA Tokens | Category (from Step 1) | TR Rule Lookup | Severity |

**Row protocol (apply before advancing to next row):**
1. Copy DELTA tokens from source block
2. Identify all TR rules that fire — list in TR Rule Lookup
3. Assign highest severity. If none fire → LOW, TR = N/A
4. HIGH or MEDIUM: TR Rule Lookup must be populated → blank = **PROTOCOL VIOLATION → repair before next row**
5. Category: drawn from Step 1 → absent category must be added to Step 1 before this row is complete

---

## STEP 5 — ESCALATION PATHS (P-2)

Section open — compound block format active.

```
Path: [ID]  Source gap: [Gap ID]
ADMIN  | Role: [system name]  Entry action: [specific action]
CS     | Starting privilege: [privilege]
DELTA  | Elevation: [access reached or NONE]  Blocker: [NONE / mechanism]  TR: [TR-05 if ESCALATION-OPEN]
```

No path → DELTA: `Elevation: NONE. Blocked by: [mechanism]`. Do not omit.

---

## STEP 5B — SHARING RULE CONFLICTS (P-2)

```
Rule: [Dataverse system name]
ADMIN  | Grants: [source → target]  Level: [access]  Stock Default: [exists in stock / not in stock]
CS     | Received: [level]  Expected by OWD: [level]
DELTA  | [CONFLICT:[rule] or NONE]  TR: [TR-04 if fires]
```

---

## STEP 5C — TEAM MEMBERSHIP GAPS (P-2)

```
Team: [name]
ADMIN  | Required role: [system name]  Self-add: [YES/NO]  Category: [from Step 1]
CS     | Membership: [IN-TEAM / NOT-IN-TEAM / CONDITIONAL]
DELTA  | [TEAM-GAP or NONE]  TR: [TR-03 if TEAM-GAP + YES]  Scenario impact: [specific, not generic]
```

---

## STEP 5D — CROSS-ROLE INTERACTION (P-2)

```
Interaction: [Role A] + [Role B] on [Entity]
ADMIN  | Role A privileges: [list]
CS     | Role B privileges: [list]
DELTA  | Superset exceeding either alone: [list or NONE]  New TR conditions: [list or NONE]
```

---

## STEP 6 — CATEGORIZATION GATE (P-4)

**Gate: every gap from Step 4 must appear here before Step 7.**

| Gap ID | Entity.Field | Current State | Category (INERTIA / DESIGN) | Stock Default (INERTIA) | Admin Decision Context (DESIGN) |

Missing gap = gate failure. Gap with no category = gate failure.

---

## STEP 7 — DUAL REMEDIATION TRACKS (P-4)

Every gap from Step 4 appears in exactly one track.

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
ADMIN  | Current (deliberate): [value]  Decision context: [from Step 6]
CS     | Target state: [corrected value]
DELTA  | Action: Change [setting] on [entity/field] in [solution] from [A] to [B]. Reverses [decision context]. After fix: [behavioral delta].
```

Applying identical format to both tracks = fail. Generic advice = fail. Each gap in exactly one track.

---

## STEP 8 — COMPLIANCE SELF-CHECK

Before submitting, verify:

| Constraint | Check |
|------------|-------|
| P-1 CEILING FIRST | No CS row appears without a prior ADMIN row in the same block |
| P-2 COMPOUND BLOCKS | Every comparative section has Admin/CS/Delta rows; no DELTA row contains a sentence |
| P-3 STOCK DEFAULTS | Every entity in Step 2 ADMIN row has a Stock Default OWD value |
| P-4 DUAL TRACKS | Every Step 4 gap appears in Step 6 and in exactly one Step 7 track |
| P-5 NO-JUDGMENT | Every HIGH or MEDIUM in Step 4 has a named TR rule in TR Rule Lookup |

Any unchecked item requires revision before submission.
