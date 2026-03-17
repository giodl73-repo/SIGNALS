Good. I have the complete rubric context. The two primary gaps are:
- **C-31**: IA reference must be inside a finding's body text — not as a standalone "IA Position:" header above the table
- **C-32**: READ RECEIPT must carry explicit cross-references to PRE-COMMITMENT for fields (d) and (e) by label name

Now generating R10:

---

## corps-pr-variate-R10-2026-03-16.md

```yaml
skill: quest-variate
skill_target: corps-pr
round: 10
date: 2026-03-16
rubric_version: 9
```

---

# Variate R10 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

Primary targets: C-31 (IA counterpoint in finding body text) and C-32 (READ RECEIPT cross-references PRE-COMMITMENT for fields d and e).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence (PRE-COMMITMENT as formal pre-finding declaration step; IA counterpoint embedded in F-NN body, not above table) | V-01, V-04 |
| Output format (finding table with "IA Counterpoint" column; READ RECEIPT as structured block with explicit (d)/(e) pointer rows) | V-02, V-05 |
| Lifecycle emphasis (Phase C exit checklist names PRE-COMMITMENT; C1/C2 result lines; finding-generation exit gate names domain-lens test) | V-03, V-04 |
| Inertia framing (IA cost ledger as the canonical reference; F-01 in each technical role is typed as IA-RESPONSE) | V-04 |
| Phrasing register (imperative "BEFORE DIFF, COMMIT:" and "EMBED IN FINDING BODY:" steps) | V-05 |

---

## V-01 — Role Sequence: PRE-COMMITMENT as Formal Pre-Phase; Finding Body IA Counterpoint

**Axis**: Role sequence
**Hypothesis**: Separating the position-declaration step (PRE-COMMITMENT block) from the
finding-generation step as two distinct named operations — and requiring the IA counterpoint
to appear within the F-NN description text itself rather than as a header field preceding the
table — eliminates the standalone-section-element failure mode of C-31. The model cannot
satisfy the template by writing "IA Position:" above the table; it must write the counterpoint
as part of a finding entry. C-32 is addressed by making the PRE-COMMITMENT cross-reference a
mandatory final line of the READ RECEIPT block, not an optional sentence.

---

You are running `/corps-pr`. Route this PR through the full org and produce a pre-merge review.

**INPUT**: PR diff or description. `org.yaml` for role scope. `.craft/roles/` for role orientations.

---

### PIPELINE DECLARATION

Five phases. No phase begins until its predecessor exits.

**Phase A — Routing**
- Entry: PR diff present, `org.yaml` loaded.
- Exit: routing table complete; every changed file assigned to a role or flagged as unowned.
- Gates: C-01, C-06

**Phase B — Inertia Advocate (IA cost ledger + PRE-COMMITMENT block)**
- Entry: Phase A exited.
- Exit: IA cost ledger written with Net direction column; Budget verdict uses three-clause
  formula with each clause on its own line; `[PRE-COMMITMENT SEALED]` token written as a
  distinct output line before any PR diff file, function, or line reference appears.
- Gates: C-11, C-17, C-19, C-21, C-25, C-27, C-28, C-29, C-30
- Condition: if IA not in roster, mark Phase B N/A and proceed.

**Phase C — Technical Role Reviews**
- Entry: Phase B exited (C1 pre-flight) + each role reads Phase B before writing findings (C2 per-role).
- Exit: all roles have findings tables; every findings table has a Domain-Lens column; at least
  one finding per role contains IA counterpoint in body text; PRE-COMMITMENT blocks precede
  findings tables for all roles with IA active.
- Gates: C-02, C-04, C-05, C-07, C-14, C-18, C-20, C-22, C-23, C-24, C-26, C-30, C-31, C-32

**Phase D — Consensus**
- Entry: Phase C exited.
- Exit: consensus written; all divergences have root-cause synthesis naming architectural mechanism.
- Gates: C-09, C-10, C-12, C-13, C-15

**Phase E — Decision**
- Entry: Phase D exited.
- Exit: recommendation written with single decision value.
- Gates: C-03, C-10

---

### PHASE A — ROUTING

Read `org.yaml`. Map each changed file to a role scope pattern. Write the routing table:

```
ROUTING TABLE

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|-------------------|-------------|------|------------------------|
| [paths]           | [add/modify/delete] | [role] | [pattern] |
| (all changed files) | default | Inertia Advocate | default — always included |
```

Coverage gap: `COVERAGE GAP: [file] — no org.yaml scope pattern matches this path.`

---

### PHASE B — INERTIA ADVOCATE

#### Step B1 — PRE-COMMITMENT Block

Write this block before analyzing any PR diff content. This is a position declaration, not a
finding. No file, function name, or line number from the PR may appear until after the seal token.

```
PRE-COMMITMENT
Role: Inertia Advocate
(a) Current system state: [one sentence — what the codebase currently does in the area this PR touches]
(b) Switching cost signal: [one sentence — preliminary cost estimate for adopting this change]
(c) Initial position: [OPPOSE / CONDITION / NEUTRAL — based on known change scope, before diff analysis]
(d) Cost row to watch: [name the cost ledger row most likely to be decisive]
(e) Position on that row: [WORSE / BETTER / NEUTRAL — initial read before diff]
[PRE-COMMITMENT SEALED]
```

The `[PRE-COMMITMENT SEALED]` token must be the last line of this block and must appear before
any PR file path, function, or line number is written anywhere in the output.

#### Step B2 — IA Cost Ledger

```
IA COST LEDGER

| Row | Current-state cost | Adoption cost | Net direction |
|-----|--------------------|---------------|---------------|
| Maintenance cost | [current] | [adoption] | WORSE / BETTER / NEUTRAL |
| Incident exposure | [current] | [adoption] | WORSE / BETTER / NEUTRAL |
| [additional rows as warranted] | | | |

Budget verdict:
WORSE rows: [list rows with Net=WORSE, or "none"]
BETTER rows: [list rows with Net=BETTER, or "none"]
Conclusion: [verdict text derived from above rows — must follow from named rows]

Budget strength: HIGH / MEDIUM / LOW
```

Each of the three Budget verdict lines must appear at line start on its own line. A verdict
where two clauses share a line, or where a clause is embedded in a sentence, fails.

#### Step B3 — IA Findings

```
IA FINDINGS

| # | Description | Sev | Owner | Resolution | Domain-Lens |
|---|-------------|-----|-------|------------|-------------|
| F-01 | [argument status quo is sufficient — names existing mechanism, not a category] | P1/P2/P3 | [role] | [concrete action] | Passed |
| F-02 | [second argument] | P1/P2/P3 | [role] | [concrete action] | Passed |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

---

### PHASE C — TECHNICAL ROLE REVIEWS

#### C1 Pre-Flight Checklist

Before writing any technical role section, verify Phase B exit conditions:

```
C1 PRE-FLIGHT
[ ] IA cost ledger present with Net direction column: [PASS/FAIL]
[ ] Budget verdict three-clause formula present: [PASS/FAIL]
[ ] Each clause on its own line at line start: [PASS/FAIL]
[ ] PRE-COMMITMENT block present: [PASS/FAIL]
[ ] [PRE-COMMITMENT SEALED] token written before any diff content: [PASS/FAIL]
[ ] PRE-COMMITMENT named in Phase C exit condition: [PASS/FAIL]

C1 RESULT: ALL CLEAR
```

If any item is FAIL: `C1 RESULT: BLOCKED -- [item]`. Stop. Do not begin Phase C.

#### Per-Role Structure

For each activated technical role:

```
## Review: [role name]
```

**C2 — IA Read Prerequisite**

```
C2 RESULT: SATISFIED — Phase B read: Budget verdict = [WORSE rows: X / BETTER rows: Y / Conclusion: Z]
```

The C2 line must cite specific Phase B content. A C2 line that says "Phase B read" without
restating the Budget verdict clauses fails.

**IA READ RECEIPT**

```
IA READ RECEIPT — [role name]
(a) IA section read: Phase B — Inertia Advocate
(b) Budget verdict:
    WORSE rows: [restate from Phase B]
    BETTER rows: [restate from Phase B]
    Conclusion: [restate from Phase B]
(c) Budget strength: [restate from Phase B]
(d) Cost row relevant to this domain: [row name] — see PRE-COMMITMENT block field (d)
(e) Initial position on that row: see PRE-COMMITMENT block field (e): [value restated]
```

Fields (d) and (e) must either restate the value inline from PRE-COMMITMENT OR carry an
explicit cross-reference to the PRE-COMMITMENT block using the label "PRE-COMMITMENT block"
and the field identifier "(d)" or "(e)". A READ RECEIPT that omits both options for either
field fails C-32.

**PRE-COMMITMENT — [role name]**

```
PRE-COMMITMENT — [role name]
(d) Cost row most relevant to this domain: [row name]
(e) Initial position: [WORSE / BETTER / NEUTRAL]
[PRE-COMMITMENT SEALED]
```

This block must appear before the findings table.

**Domain-Lens Validity Gate** (finding-generation exit gate — apply before each finding advances):

> Binary test: Would ONLY [role name] raise this finding given their domain? If any generic
> reviewer could write the same sentence, revise it.
> Rewrite consequence: name the specific file, line, and architectural mechanism that only this
> role's domain lens would surface.

**Findings**

```
| # | Description | Sev | Owner | Resolution | Domain-Lens |
|---|-------------|-----|-------|------------|-------------|
| F-01 | [Description MUST contain IA counterpoint inline for at least one finding:
         "IA [verdict/cost row position]; [role] rates [severity] because [mechanism at file:line]
         — the IA section did not reach this because [reason]."] | P1/P2/P3 | [role] | [action] | Passed |
| F-02 | [additional finding] | P1/P2/P3 | [role] | [action] | Passed |
```

**C-31 requirement**: at least one finding in this table must contain within its Description
field both: (a) the IA's specific verdict or cost position, and (b) this role's disagreeing
mechanism. This reference must be in the Description cell — not as a row above the table, not
as a header, not as a separate "IA Position:" element. A table where every Description cell
contains only the technical finding and the IA reference appears only in a standalone block
above or below the table fails C-31.

```
Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

---

### PHASE D — CONSENSUS SYNTHESIS

**Perspective-label ban list** (scan every divergence explanation before Phase E begins):

- `[ ]` "they have different perspectives" — BANNED
- `[ ]` "they prioritize differently" — BANNED
- `[ ]` "they see this through different lenses" — BANNED
- `[ ]` "their roles lead them to different conclusions" — BANNED
- `[ ]` "from [role]'s perspective" (as sole divergence cause) — BANNED

```
CONSENSUS

Inertia baseline: IA rated null hypothesis strength [HIGH/MEDIUM/LOW].
  Technical reviews [confirm / partially challenge / defeat] this verdict.
  Basis: [which technical finding most directly engaged the IA baseline]

Agreement: [area] — independently raised by [role-A] and [role-B]

Divergence: [role-A] rates [concern] P1; [role-B] rates P3.
  Mechanism: [specific code property, system boundary, or architectural constraint causing
  the rating difference — not a reviewer attribute]

Critical: [F-XX from role] — [why this finding most threatens the merge]
```

---

### PHASE E — DECISION

```
RECOMMENDATION

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms resolution before merge]
2. [additional condition] — sign-off: [role]
```

---

**AMEND** — when `--amend` is set, output before Phase A:

```
AMEND SCOPE DISCLOSURE
(a) What was amended: [description]
(b) Roles added: [list or "none"]
(c) Roles removed: [list or "none"]
(d) Prior findings superseded: [F-ID list or "none — prior findings stand"]
```

---

## V-02 — Output Format: Finding Table with IA-Counterpoint Column; READ RECEIPT with Explicit Pointer Rows

**Axis**: Output format
**Hypothesis**: When the IA counterpoint is a named column in each finding table row (not a
block above the table), C-31 is structurally enforced because the column value must coexist
with the finding in the same row — a standalone "IA Position:" header cannot satisfy a column
slot. When the READ RECEIPT block is a template with explicit named rows for (d) and (e) that
require either an inline value or a label-name pointer to PRE-COMMITMENT, C-32 is satisfied
because the pointer slot is present in the template rather than being an inferred omission.
The format contract — not behavioral instruction — drives compliance.

---

You are running `/corps-pr`. Route this PR and produce a pre-merge review. All output uses
named-field structured blocks and tables. Follow the format contract exactly — deviations are
failures.

**INPUT**: PR diff. `org.yaml`. `.craft/roles/`.

---

### TABLE 1 — ROUTING

```
| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|-------------------|-------------|------|------------------------|
| [paths]           | [type]      | [role] | [pattern matched]    |
| (all files)       | default     | Inertia Advocate | default — always included |
```

Coverage gap row (if applicable): `COVERAGE GAP: [file] — no scope pattern.`

---

### TABLE 2 — PRE-COMMITMENT (IA)

Write before any PR diff file, function, or line is referenced:

```
PRE-COMMITMENT — Inertia Advocate
| Field | Value |
|-------|-------|
| (a) Current system state | [what the codebase currently does in this area] |
| (b) Switching cost signal | [preliminary cost estimate for adopting this change] |
| (c) Initial position | OPPOSE / CONDITION / NEUTRAL |
| (d) Cost row to watch | [row name — the row most likely to be decisive] |
| (e) Position on that row | WORSE / BETTER / NEUTRAL |

[PRE-COMMITMENT SEALED]
```

The `[PRE-COMMITMENT SEALED]` token appears as a distinct line after the table, before any PR
file path, function name, or line number appears in the output.

---

### TABLE 3 — IA COST LEDGER

```
| Row | Current-state cost | Adoption cost | Net direction |
|-----|--------------------|---------------|---------------|
| Maintenance cost | [current] | [adoption] | WORSE / BETTER / NEUTRAL |
| Incident exposure | [current] | [adoption] | WORSE / BETTER / NEUTRAL |
| [additional rows] | | | |

Budget verdict:
WORSE rows: [list rows where Net=WORSE, or "none"]
BETTER rows: [list rows where Net=BETTER, or "none"]
Conclusion: [derived from named WORSE/BETTER rows above]

Budget strength: HIGH / MEDIUM / LOW
```

Three-clause format rule: each of `WORSE rows:`, `BETTER rows:`, `Conclusion:` must be on its
own output line at line start. No two clauses may share a line.

---

### TABLE 4 — IA FINDINGS

```
| # | Description | Sev | Owner | Resolution | Domain-Lens |
|---|-------------|-----|-------|------------|-------------|
| F-01 | [argument status quo sufficient — names existing mechanism] | P1/P2/P3 | [role] | [action] | Passed |
| F-02 | [second argument] | P1/P2/P3 | [role] | [action] | Passed |
| TOTAL | — | — | [N] findings: [x] P1, [y] P2, [z] P3 | — | — |

IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

---

### TABLES 5–N — TECHNICAL ROLE FINDINGS (one table set per role)

Sequence: security/compliance first → domain-specific → PM/TPM last. IA phase must be
complete (Tables 2–4 present) before any technical role table begins.

For each role:

**IA READ RECEIPT — [role name]**

```
| Field | Value |
|-------|-------|
| (a) IA section read | Phase B — Inertia Advocate |
| (b) Budget verdict | WORSE rows: [restate] / BETTER rows: [restate] / Conclusion: [restate] |
| (c) Budget strength | [restate from Table 3] |
| (d) Cost row relevant to this domain | [row name] — PRE-COMMITMENT block (d): [value] |
| (e) Initial position on that row | PRE-COMMITMENT block (e): [value] |
```

Fields (d) and (e): the Value cell must either restate the value inline OR contain an explicit
pointer to the PRE-COMMITMENT block using the text "PRE-COMMITMENT block (d)" or
"PRE-COMMITMENT block (e)". An empty or placeholder cell fails C-32.

**C1 RESULT** (once, before the first technical role table):

```
C1 RESULT: ALL CLEAR
```

Checklist (all must pass before writing C1 RESULT: ALL CLEAR):
- PRE-COMMITMENT table present and sealed
- Budget verdict three-clause formula present
- Each clause on its own line

**PRE-COMMITMENT — [role name]**

```
PRE-COMMITMENT — [role name]
| Field | Value |
|-------|-------|
| (d) Cost row | [row name] |
| (e) Initial position | WORSE / BETTER / NEUTRAL |

[PRE-COMMITMENT SEALED]
```

**C2 RESULT** (per role, after READ RECEIPT):

```
C2 RESULT: SATISFIED — cited Phase B Budget verdict: WORSE rows=[X], BETTER rows=[Y]
```

**FINDINGS TABLE — [role name]**

Domain-lens validity gate (applied before each finding enters the table):
Binary test: would only this role raise this finding given their domain? If a generic reviewer
could write the same sentence — rewrite it to name the specific file, line, and mechanism that
only this role's lens would surface.

```
| # | Description | Sev | Owner | Resolution | Domain-Lens | IA Counterpoint |
|---|-------------|-----|-------|------------|-------------|-----------------|
| F-01 | [domain-specific finding] | P1/P2/P3 | [role] | [action] | Passed | [IA [verdict/row]; this role [confirms/disputes] because [mechanism at file:line]] |
| F-02 | [additional finding] | P1/P2/P3 | [role] | [action] | Passed | N/A |
| TOTAL | — | — | [N] findings: [x]P1, [y]P2, [z]P3 | — | — | — |
```

**IA Counterpoint column rule**: at least one row in each role's table must have a non-"N/A"
IA Counterpoint value. That value must name the IA's specific cost position or verdict AND
the role's disagreeing mechanism in the same cell. A row where the IA counterpoint is written
as a separate block above or below the table fails C-31 — it must be in this column cell.

---

### TABLE N+1 — CONSENSUS

**Perspective-label ban list** — scan every Mechanism cell against all five:
- BL-01: "they have different perspectives" — BANNED
- BL-02: "they prioritize differently" — BANNED
- BL-03: "they see this through different lenses" — BANNED
- BL-04: "their roles lead them to different conclusions" — BANNED
- BL-05: "from [role]'s perspective" (as sole explanation) — BANNED

```
| Signal | Area | Roles | Notes |
|--------|------|-------|-------|
| Inertia baseline | IA null hypothesis | Inertia Advocate | [HIGH/MEDIUM/LOW] — technical reviews [confirmed/challenged/defeated] |
| Agreement | [area both raised] | [role-A], [role-B] | [shared concern — one sentence] |
| Divergence | [contested area] | [role-A (P1)], [role-B (P3)] | Mechanism: [code property causing rating difference — not a reviewer attribute] |
| Critical | [most dangerous finding] | [role] | [why this threatens the merge] |
```

---

### TABLE N+2 — RECOMMENDATION

```
| Decision | Primary Finding | Conditions | Sign-off Role |
|----------|-----------------|------------|---------------|
| GO / NO-GO / GO WITH CONDITIONS | [F-XX from role — one sentence] | [condition or "none"] | [role or "none"] |
```

One decision value only.

---

**AMEND** — output before TABLE 1 when `--amend` is active:

```
AMEND SCOPE DISCLOSURE
| Field | Value |
|-------|-------|
| (a) What was amended | [description] |
| (b) Roles added | [list or "none"] |
| (c) Roles removed | [list or "none"] |
| (d) Prior findings superseded | [F-ID list or "none"] |
```

---

## V-03 — Lifecycle Emphasis: Dual Sub-Conditions; Phase C Exit Names PRE-COMMITMENT; Finding Exit Gate

**Axis**: Lifecycle emphasis
**Hypothesis**: Structuring Phase C entry as two independently auditable sub-conditions with
required output result lines (C1 RESULT, C2 RESULT) makes C-32 a structural consequence of C2
satisfaction: a role cannot output "C2 RESULT: SATISFIED" without having cited Phase B content
including PRE-COMMITMENT fields (d) and (e) in the READ RECEIPT. Naming PRE-COMMITMENT
presence in Phase C's exit condition checklist elevates its absence from a C-27 format gap to
a phase-gate violation. The finding-generation exit gate (domain-lens binary test + rewrite
consequence) is named as a Phase C exit condition, making C-31 verifiable as a phase output
requirement rather than a style preference.

---

You are running `/corps-pr`. Execute the following phase-gate pipeline. Record the named exit
condition result for each phase before advancing.

**INPUT**: PR diff. `org.yaml`. `.craft/roles/`.

---

### PHASE A — ROUTING

**Entry condition**: PR diff present, `org.yaml` loaded.
**Exit condition**: routing table written; every changed file assigned to a role or flagged as
unowned. Coverage gaps listed.

```
ROUTING TABLE

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|-------------------|-------------|------|------------------------|
| [paths]           | [type]      | [role] | [pattern]            |
| (all files)       | default     | Inertia Advocate | default — always included |
```

`PHASE A EXIT: routing table complete — [N] roles activated.`

---

### PHASE B — INERTIA ADVOCATE

**Entry condition**: Phase A exited.
**Exit condition** — all of the following must be true before Phase B is marked complete:
- [ ] PRE-COMMITMENT block written with fields (a)–(e)
- [ ] `[PRE-COMMITMENT SEALED]` token written as a distinct line before any PR diff content
- [ ] IA cost ledger written with Net direction column
- [ ] Budget verdict uses three-clause formula: `WORSE rows:`, `BETTER rows:`, `Conclusion:` each on its own line at line start
- [ ] IA findings table written with Domain-Lens column
- [ ] Budget strength field present

**Step B1 — PRE-COMMITMENT**

```
PRE-COMMITMENT — Inertia Advocate
(a) Current system state: [what the codebase currently does in this area]
(b) Switching cost signal: [preliminary cost estimate]
(c) Initial position: OPPOSE / CONDITION / NEUTRAL
(d) Cost row to watch: [row name]
(e) Position on that row: WORSE / BETTER / NEUTRAL
[PRE-COMMITMENT SEALED]
```

**Step B2 — IA Cost Ledger**

```
| Row | Current-state cost | Adoption cost | Net direction |
|-----|--------------------|---------------|---------------|
| Maintenance cost | [current] | [adoption] | WORSE / BETTER / NEUTRAL |
| Incident exposure | [current] | [adoption] | WORSE / BETTER / NEUTRAL |
| [additional rows] | | | |

Budget verdict:
WORSE rows: [rows with Net=WORSE or "none"]
BETTER rows: [rows with Net=BETTER or "none"]
Conclusion: [derived from row evidence above]

Budget strength: HIGH / MEDIUM / LOW
```

**Step B3 — IA Findings**

```
| # | Description | Sev | Owner | Resolution | Domain-Lens |
|---|-------------|-----|-------|------------|-------------|
| F-01 | [argument status quo sufficient — names existing mechanism] | P1/P2/P3 | [role] | [action] | Passed |
| F-02 | [second argument] | P1/P2/P3 | [role] | [action] | Passed |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

`PHASE B EXIT: all exit conditions met.`

---

### PHASE C — TECHNICAL ROLE REVIEWS

**Phase C entry condition — two independently auditable sub-conditions:**

#### C1 — Pre-Flight Phase B Exit Checklist

Verify all Phase B exit conditions. Any unchecked item blocks Phase C from starting.

```
C1 PRE-FLIGHT CHECKLIST
[ ] PRE-COMMITMENT block present with fields (a)–(e): [PASS/FAIL]
[ ] [PRE-COMMITMENT SEALED] token present as distinct line: [PASS/FAIL]
[ ] [PRE-COMMITMENT SEALED] precedes all PR diff content: [PASS/FAIL]
[ ] Cost ledger present with Net direction column: [PASS/FAIL]
[ ] Budget verdict three-clause formula present: [PASS/FAIL]
[ ] WORSE rows: on its own line at line start: [PASS/FAIL]
[ ] BETTER rows: on its own line at line start: [PASS/FAIL]
[ ] Conclusion: on its own line at line start: [PASS/FAIL]
[ ] Budget strength field present: [PASS/FAIL]

C1 RESULT: ALL CLEAR
```

Any FAIL item → `C1 RESULT: BLOCKED -- [item that failed]`. Stop. Do not advance.

#### C2 — Per-Role IA Read Prerequisite

Verified per role. Each technical role section must begin with an IA READ RECEIPT that cites
Phase B content, including PRE-COMMITMENT fields (d) and (e) by label name. C2 is assessed
independently per role.

**Phase C exit condition** — all of the following must be true before Phase D:
- [ ] All activated roles have findings tables
- [ ] All findings tables include a Domain-Lens column with gate compliance per finding
- [ ] PRE-COMMITMENT blocks precede findings tables for all roles [C-30 gate]
- [ ] At least one finding per role contains IA counterpoint in Description text (not as standalone element)
- [ ] Domain-lens validity gate applied to every finding (binary test passed)

#### Per-Role Structure

```
## Review: [role name]
```

**IA READ RECEIPT — [role name]**

```
IA READ RECEIPT — [role name]
(a) IA section read: Phase B — Inertia Advocate
(b) Budget verdict (restated from Phase B):
    WORSE rows: [restate]
    BETTER rows: [restate]
    Conclusion: [restate]
(c) Budget strength: [restate]
(d) Cost row relevant to this domain: [row name]
    → PRE-COMMITMENT block (d): [restate value or "see PRE-COMMITMENT block field (d)"]
(e) Initial position on that row: [value]
    → PRE-COMMITMENT block (e): [restate value or "see PRE-COMMITMENT block field (e)"]
```

The → pointer line for (d) and (e) must either restate the value from PRE-COMMITMENT inline
or carry the text "see PRE-COMMITMENT block field (d)" / "see PRE-COMMITMENT block field (e)".
A READ RECEIPT where (d) and (e) appear without this pointer or inline restatement fails C-32.

```
C2 RESULT: SATISFIED — cited PRE-COMMITMENT (d): [row name], (e): [position]
```

A C2 RESULT line that does not name the PRE-COMMITMENT fields cited fails.

**PRE-COMMITMENT — [role name]**

```
PRE-COMMITMENT — [role name]
(d) Cost row: [row name]
(e) Initial position: WORSE / BETTER / NEUTRAL
[PRE-COMMITMENT SEALED]
```

This block must appear before the findings table. Its presence is a Phase C exit condition
item above.

**Domain-Lens Validity Gate** — applied to each finding before it enters the table:

> Binary test: Would ONLY [role name] raise this finding given their domain?
> Rewrite consequence: If any generic reviewer could write the same sentence, revise it to
> name the specific file, function, or contract that only this role's lens would surface.

**Findings**

```
| # | Description | Sev | Owner | Resolution | Domain-Lens |
|---|-------------|-----|-------|------------|-------------|
| F-01 | [At least one Description cell must contain IA counterpoint inline:
         "IA [cost position or verdict]; [role] rates [sev] because [mechanism at file:line].
         IA did not surface this because [reason — e.g., domain boundary]."] | P1/P2/P3 | [role] | [action] | Passed |
| F-02 | [domain-specific finding] | P1/P2/P3 | [role] | [action] | Passed |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

**C-31 gate**: before writing the summary line, verify that at least one Description cell in
this table contains both the IA verdict/cost position and this role's disagreeing mechanism.
If every Description cell contains only technical content with no IA reference, the finding-
generation exit condition for this role is not met.

`PHASE C ROLE [role name] EXIT: PRE-COMMITMENT present, C2 SATISFIED, IA counterpoint in body.`

---

### PHASE D — CONSENSUS

**Entry condition**: Phase C exited (all roles complete, all Phase C exit items checked).
**Exit condition**: consensus written; ban list scan clear.

**Perspective-label ban list** — scan every divergence explanation independently:
- `[ ]` BL-01: "they have different perspectives" — BANNED
- `[ ]` BL-02: "they prioritize differently" — BANNED
- `[ ]` BL-03: "they see this through different lenses" — BANNED
- `[ ]` BL-04: "their roles lead them to different conclusions" — BANNED
- `[ ]` BL-05: "from [role]'s perspective" (sole divergence cause) — BANNED

```
CONSENSUS ANALYSIS

Inertia baseline: IA rated null hypothesis [HIGH/MEDIUM/LOW].
  Technical reviews [confirm / partially challenge / defeat] this verdict.
  Basis: [which technical finding most directly engaged the IA baseline]

Agreement: [area] — raised independently by [role-A], [role-B]

Divergence: [role-A] rates [concern] P1; [role-B] rates P3.
  Mechanism: [specific code property or architectural constraint causing the difference]

Critical: [F-XX from role] — [why this finding most threatens the merge]
```

`PHASE D EXIT: consensus complete, ban list scan clear [BL-01 through BL-05 checked].`

---

### PHASE E — DECISION

**Entry condition**: Phase D exited.

```
RECOMMENDATION

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role]
2. [additional condition] — sign-off: [role]
```

`PHASE E EXIT: single decision value written.`

---

**AMEND** — before Phase A if `--amend` set:

```
AMEND SCOPE DISCLOSURE
(a) What was amended: [description]
(b) Roles added: [list or "none"]
(c) Roles removed: [list or "none"]
(d) Prior findings superseded: [F-ID list or "none"]
```

---

## V-04 — Inertia Framing + Role Sequence: F-01 Typed as IA-Response; Inline Receipt Fields

**Axes**: Inertia framing + role sequence
**Hypothesis**: Requiring the first finding in each technical role section to be typed as
"IA-RESPONSE" — a finding whose Description field is the IA counterpoint by definition —
satisfies C-31 structurally because the counterpoint IS a finding entry, not a header before
findings. A standalone "IA Position:" block above the table cannot satisfy F-IA because F-IA
is an F-NN finding row. C-32 is addressed by requiring the READ RECEIPT to restate (d) and (e)
inline from PRE-COMMITMENT — not as pointers but as explicit value restatements — ensuring the
receipt is independently auditable without cross-file lookup.

---

You are running `/corps-pr`. Route this PR through the full org and produce a pre-merge review.
The Inertia Advocate is always the first reviewer. Every technical reviewer's first finding is
a structured response to the IA verdict — typed as an IA-RESPONSE finding, not a standalone
block.

**INPUT**: PR diff. `org.yaml`. `.craft/roles/`.

---

### STEP 1 — ROUTING

Read `org.yaml`. Map each changed file to a role. Always include Inertia Advocate.

```
ROUTING TABLE

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|-------------------|-------------|------|------------------------|
| [paths]           | [type]      | [role] | [pattern]            |
| (all files)       | default     | Inertia Advocate | always included |
```

Coverage gap: `COVERAGE GAP: [file] — no scope pattern.`

---

### STEP 2 — INERTIA ADVOCATE (runs first; all technical roles read this before writing)

The Inertia Advocate is a budget authority. Their verdict is not a risk list — it is a cost
position stating what the current system costs to maintain versus what this change costs to
adopt. Every subsequent technical role's first finding must respond to this cost position by
name.

#### PRE-COMMITMENT

Before analyzing any PR file, function, or line:

```
PRE-COMMITMENT — Inertia Advocate
(a) Current system state: [what the codebase currently does in this area — one sentence]
(b) Switching cost signal: [preliminary cost estimate before diff analysis]
(c) Initial position: OPPOSE / CONDITION / NEUTRAL
(d) Cost row to watch: [maintenance cost / incident exposure / other — name the row]
(e) Position on that row: WORSE / BETTER / NEUTRAL
[PRE-COMMITMENT SEALED]
```

`[PRE-COMMITMENT SEALED]` must appear as a distinct line after field (e) and before any PR
file path or line number appears in the output.

#### IA Cost Ledger

```
IA COST LEDGER

| Row | Current-state cost | Adoption cost | Net direction |
|-----|--------------------|---------------|---------------|
| Maintenance cost | [current cost to maintain] | [adoption cost] | WORSE / BETTER / NEUTRAL |
| Incident exposure | [current exposure] | [exposure under change] | WORSE / BETTER / NEUTRAL |
| [additional rows if warranted] | | | |
```

Budget verdict (three labeled lines, each on its own line at line start):
```
WORSE rows: [list rows with Net=WORSE, or "none"]
BETTER rows: [list rows with Net=BETTER, or "none"]
Conclusion: [verdict derived from the named rows — must cite which rows drove the conclusion]
```

Budget strength: HIGH / MEDIUM / LOW

#### IA Findings

```
| # | Type | Description | Sev | Owner | Resolution | Domain-Lens |
|---|------|-------------|-----|-------|------------|-------------|
| F-01 | IA-POSITION | [argument status quo is sufficient — names existing mechanism] | P1/P2/P3 | [role] | [action] | Passed |
| F-02 | IA-POSITION | [second argument] | P1/P2/P3 | [role] | [action] | Passed |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

---

### STEP 3 — TECHNICAL ROLE REVIEWS

**Entry condition**: Step 2 complete. Each technical role reads the IA cost ledger and Budget
verdict before writing any finding.

Sequence: security/compliance → domain-specific → PM/TPM.

For each role:

#### PRE-COMMITMENT — [role name]

Written before the findings table:

```
PRE-COMMITMENT — [role name]
(d) Cost row most relevant to this domain: [row name from IA cost ledger]
(e) Initial position on that row: WORSE / BETTER / NEUTRAL
[PRE-COMMITMENT SEALED]
```

#### IA READ RECEIPT — [role name]

Written after PRE-COMMITMENT, before findings:

```
IA READ RECEIPT — [role name]
(a) IA section read: Step 2 — Inertia Advocate
(b) Budget verdict:
    WORSE rows: [restate from Step 2 exactly]
    BETTER rows: [restate from Step 2 exactly]
    Conclusion: [restate from Step 2 exactly]
(c) Budget strength: [restate from Step 2]
(d) Cost row relevant to this domain: [row name] — restated from PRE-COMMITMENT (d): [value]
(e) Initial position on that row: [value] — restated from PRE-COMMITMENT (e): [value]
```

Fields (d) and (e) restate the value inline from PRE-COMMITMENT block fields (d) and (e).
The "restated from PRE-COMMITMENT (d):" notation makes the source explicit and independently
auditable. An omitted (d) or (e) field, or a field with placeholder text, fails C-32.

**C1 RESULT** (once, before the first role's PRE-COMMITMENT):
Verify Step 2 is complete — IA cost ledger, Budget verdict three-clause formula, PRE-COMMITMENT
sealed, Budget strength present.
```
C1 RESULT: ALL CLEAR
```

**C2 RESULT** (per role, after READ RECEIPT):
```
C2 RESULT: SATISFIED — PRE-COMMITMENT (d): [row name], (e): [position] cited in receipt
```

#### Findings — [role name]

Domain-lens validity gate before each finding: Binary test — would ONLY this role raise this
finding given their domain? Rewrite consequence — if any generic reviewer could write the same
sentence, revise to name the specific file, function, or architectural contract this role's
domain lens surfaces.

```
| # | Type | Description | Sev | Owner | Resolution | Domain-Lens |
|---|------|-------------|-----|-------|------------|-------------|
| F-IA | IA-RESPONSE | [IA verdict/cost position restated] + [this role's assessment: 
         "IA assessed [cost row] as [Net direction]. [Role] [confirms/disputes]: 
         [mechanism at specific file:line] — [reason this role's lens surfaces it]."] | P1/P2/P3 | [role] | [action] | Passed |
| F-01 | [type] | [domain-specific finding] | P1/P2/P3 | [role] | [action] | Passed |
| F-02 | [type] | [domain-specific finding] | P1/P2/P3 | [role] | [action] | Passed |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

**F-IA is the IA-RESPONSE finding**. Its Description field contains both the IA's cost position
(restating the relevant row from the Budget verdict) and this role's disagreeing or confirming
mechanism. This is a finding row in the table — not a block above the table. A section where
the IA reference appears only as a header, an "IA anchor:" field, or a paragraph above the
table and not in any finding's Description cell fails C-31. F-IA satisfies C-31 because the
reference is in the Description cell of a specific finding entry.

---

### STEP 4 — CONSENSUS

**Perspective-label ban list** — scan every divergence mechanism explanation:
- BL-01: "they have different perspectives" — BANNED
- BL-02: "they prioritize differently" — BANNED
- BL-03: "they see this through different lenses" — BANNED
- BL-04: "their roles lead them to different conclusions" — BANNED
- BL-05: "from [role]'s perspective" (as sole divergence cause) — BANNED

```
CONSENSUS ANALYSIS

Inertia baseline: IA null hypothesis strength [HIGH/MEDIUM/LOW].
  Budget verdict summary: WORSE rows=[list] / BETTER rows=[list] / Conclusion=[text].
  Technical reviews [confirm / partially challenge / defeat] this verdict.
  Most direct engagement: [F-XX from role — how it engaged the IA baseline]

Agreement: [area] — [role-A] and [role-B] raised independently

Divergence: [role-A] rates [concern] P1; [role-B] rates P3.
  Mechanism: [structural code property or architectural constraint causing rating difference]

Critical: [F-XX from role] — [why this most threatens the merge]
```

---

### STEP 5 — RECOMMENDATION

```
RECOMMENDATION

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role]
2. [additional condition] — sign-off: [role]
```

---

**AMEND** — when `--amend` set, before STEP 1:

```
AMEND SCOPE DISCLOSURE
(a) What was amended: [description]
(b) Roles added: [list or "none"]
(c) Roles removed: [list or "none"]
(d) Prior findings superseded: [F-ID list or "none"]
```

---

## V-05 — Phrasing Register: Imperative Checklist; "BEFORE DIFF, COMMIT:" and "EMBED IN FINDING BODY:"

**Axes**: Phrasing register (imperative, step-by-step checklist) + lifecycle emphasis
**Hypothesis**: Expressing the PRE-COMMITMENT requirement as an explicit "BEFORE DIFF, COMMIT:"
instruction that must be completed before the model is permitted to proceed prevents post-hoc
rationalization. Expressing the C-31 requirement as "WHEN WRITING EACH FINDING, EMBED AT LEAST
ONE IA COUNTERPOINT IN THE BODY TEXT" makes the finding-level obligation unambiguous —
"in the body text" explicitly excludes standalone headers. Expressing the C-32 requirement as
"WHEN WRITING THE READ RECEIPT, INCLUDE POINTER LINES FOR (d) AND (e) CITING PRE-COMMITMENT"
names the exact output artifact required. The imperative register makes each instruction a
discrete, completable step rather than a style preference.

---

You are running `/corps-pr`. Follow each step in order. Do not advance to the next step until
the current step's checklist is complete.

**INPUT**: PR diff. `org.yaml`. `.craft/roles/`.

---

### STEP 1: BUILD THE REVIEWER LIST

Read `org.yaml`. For each changed file, find the matching scope pattern and record the role.
Add Inertia Advocate by default. Write the list before doing anything else.

```
WHO REVIEWS THIS PR

| File / File Group | Change Type | Role | org.yaml Pattern |
|-------------------|-------------|------|------------------|
| [paths]           | [type]      | [role] | [pattern]      |
| (all files)       | default     | Inertia Advocate | always included |
```

If any file has no pattern: `COVERAGE GAP: [file]`.

**Step 1 complete** when every changed file is assigned.

---

### STEP 2: DECLARE THE IA POSITION — BEFORE LOOKING AT THE DIFF

**DO THIS FIRST, BEFORE READING THE PR FILES.**

This step commits the Inertia Advocate's position before diff analysis. Any information that
comes from reading PR file paths, function names, or line numbers must not appear until after
the seal token.

```
DECLARE: Inertia Advocate pre-commitment
(a) What the codebase currently does in this area: [one sentence — from domain knowledge, not diff]
(b) Switching cost signal: [preliminary estimate — from change description, not file-level analysis]
(c) Initial position: OPPOSE / CONDITION / NEUTRAL
(d) Cost row most likely to be decisive: [maintenance cost / incident exposure / other]
(e) Initial stance on that row: WORSE / BETTER / NEUTRAL
[PRE-COMMITMENT SEALED]
```

**Checklist before moving to Step 3:**
- [ ] All five fields (a)–(e) filled
- [ ] `[PRE-COMMITMENT SEALED]` written as a distinct line
- [ ] No PR file path, function name, or line number appears before `[PRE-COMMITMENT SEALED]`

**Step 2 complete** when checklist is clear.

---

### STEP 3: BUILD THE IA COST LEDGER — NOW READ THE DIFF

Now you may read the PR diff. Express the IA's position as a cost ledger:

```
IA COST LEDGER

| Row | Current-state cost | Adoption cost | Net direction |
|-----|--------------------|---------------|---------------|
| Maintenance cost | [current] | [adoption] | WORSE / BETTER / NEUTRAL |
| Incident exposure | [current] | [adoption] | WORSE / BETTER / NEUTRAL |
| [additional rows if warranted] | | | |
```

Then write the Budget verdict — three lines, each starting at line start on its own line:

```
WORSE rows: [rows with Net=WORSE or "none"]
BETTER rows: [rows with Net=BETTER or "none"]
Conclusion: [derived from the named rows — name which rows drove the conclusion]
```

Then: `Budget strength: HIGH / MEDIUM / LOW`

**Checklist before moving to Step 4:**
- [ ] Net direction column present for every row
- [ ] `WORSE rows:` on its own line, nothing else on that line
- [ ] `BETTER rows:` on its own line, nothing else on that line
- [ ] `Conclusion:` on its own line, nothing else on that line
- [ ] Budget strength present

**Step 3 complete** when checklist is clear.

---

### STEP 4: IA FINDINGS

```
| # | Description | Sev | Owner | Resolution | Domain-Lens |
|---|-------------|-----|-------|------------|-------------|
| F-01 | [argument the status quo is sufficient — names existing mechanism, not a category] | P1/P2/P3 | [role] | [concrete action] | Passed |
| F-02 | [second argument] | P1/P2/P3 | [role] | [action] | Passed |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

**Step 4 complete** when at least 2 findings written with summary line.

---

### STEP 5: FOR EACH TECHNICAL ROLE — RUN THIS SEQUENCE IN ORDER

Run Steps 5A through 5E for each activated technical role, in sequence: security/compliance
→ domain-specific → PM/TPM.

**5A — VERIFY STEP 4 IS COMPLETE**

```
C1 RESULT: ALL CLEAR
```

(Check: IA cost ledger present, Budget verdict three-clause formula on separate lines,
PRE-COMMITMENT sealed, Budget strength present. If any fails: `C1 RESULT: BLOCKED -- [item]`.)

**5B — DECLARE THE ROLE'S POSITION BEFORE WRITING FINDINGS**

```
PRE-COMMITMENT — [role name]
(d) Cost row most relevant to this role's domain: [row name]
(e) Initial position on that row: WORSE / BETTER / NEUTRAL
[PRE-COMMITMENT SEALED]
```

This block must appear before the findings table in the output.

**5C — WRITE THE READ RECEIPT**

```
IA READ RECEIPT — [role name]
(a) IA section read: Steps 3–4 — Inertia Advocate
(b) Budget verdict:
    WORSE rows: [restate from Step 3]
    BETTER rows: [restate from Step 3]
    Conclusion: [restate from Step 3]
(c) Budget strength: [restate from Step 3]
(d) Cost row for this domain: [row name]
    [Pointer: see PRE-COMMITMENT — [role name] field (d): [value]]
(e) Initial position: [value]
    [Pointer: see PRE-COMMITMENT — [role name] field (e): [value]]
```

**INCLUDE POINTER LINES FOR (d) AND (e) CITING PRE-COMMITMENT BY NAME.**

The pointer line must contain the text "PRE-COMMITMENT — [role name]" and the field identifier
"(d)" or "(e)". A READ RECEIPT where (d) and (e) appear with no pointer to PRE-COMMITMENT
fails C-32. A receipt that omits (d) and (e) entirely also fails.

```
C2 RESULT: SATISFIED — PRE-COMMITMENT (d)=[row name] and (e)=[position] cited
```

**5D — APPLY THE DOMAIN-LENS GATE TO EACH FINDING**

Before writing each finding, ask: Would ONLY this role raise this finding given their domain?
If any generic reviewer could write the same sentence — rewrite it. Name the specific file,
function, or architectural mechanism that only this role's lens would surface.

**5E — WRITE FINDINGS — EMBED AT LEAST ONE IA COUNTERPOINT IN THE BODY TEXT**

```
| # | Description | Sev | Owner | Resolution | Domain-Lens |
|---|-------------|-----|-------|------------|-------------|
| F-01 | [EMBED IA COUNTERPOINT HERE IN THE DESCRIPTION TEXT — not as a separate block.
         Write: "IA [verdict/cost position — name the row and Net direction]. [Role] [confirms/disputes]
         because [mechanism at specific file:line — name what IA did not surface and why]."] | P1/P2/P3 | [role] | [action] | Passed |
| F-02 | [additional finding — domain-specific, passes gate] | P1/P2/P3 | [role] | [action] | Passed |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

**EMBED THE IA COUNTERPOINT IN THE DESCRIPTION TEXT OF AT LEAST ONE FINDING ROW.**

Do not write it as a separate block before the table. Do not write it as an "IA anchor:" field
above the table. Write it inside a Description cell — in the same text as the finding itself.
The finding body must contain both: the IA's specific cost position or verdict, and this role's
mechanism for agreeing or disagreeing with it.

**Step 5 complete for [role name]** when 5A–5E are done.

---

### STEP 6: CONSENSUS

Read across all findings. For any two roles that rated the same change at different severities:
name what in the code — not what in the people — causes the difference.

**Banned phrases in divergence explanations** (check each independently):
- `[ ]` "they have different perspectives" — names no code property
- `[ ]` "they prioritize differently" — names no mechanism
- `[ ]` "they see this through different lenses" — metaphor, not cause
- `[ ]` "their roles lead them to different conclusions" — circular
- `[ ]` "from [role]'s perspective" (as sole explanation) — role label, not fact

Replace with: what specific code property, system boundary, or contract makes one role see P1
and another see P3?

```
CONSENSUS

Inertia baseline: IA null hypothesis strength [HIGH/MEDIUM/LOW].
  Budget verdict: WORSE=[list] / BETTER=[list] / Conclusion=[text].
  Technical reviews [confirm / challenge / defeat] this verdict.
  Basis: [F-XX from role — the finding that most directly engaged the IA baseline]

Agreement: [area] — raised independently by [role-A] and [role-B]

Divergence: [role-A] rates [concern] P1; [role-B] rates P3.
  Mechanism: [code property, boundary, or contract causing the difference]

Critical: [F-XX from role] — [why this finding most threatens the merge]
```

**Step 6 complete** when consensus written and ban list scan clear.

---

### STEP 7: THE DECISION

```
DECISION

GO / NO-GO / GO WITH CONDITIONS
Reason: [F-XX from [role] — one sentence]

Before merge (GO WITH CONDITIONS only):
1. [what must be resolved] — confirmed by: [role]
2. [additional condition] — confirmed by: [role]
```

One outcome. No hedging.

---

**AMEND** — when `--amend` set, before STEP 1:

```
AMEND SCOPE DISCLOSURE
(a) What was amended: [description]
(b) Roles added: [list or "none"]
(c) Roles removed: [list or "none"]
(d) Prior findings superseded: [F-ID list or "none"]
```

---

## Scoring Prediction

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Essential | PASS | PASS | PASS | PASS | PASS |
| C-02 Essential | PASS | PASS | PASS | PASS | PASS |
| C-03 Essential | PASS | PASS | PASS | PASS | PASS |
| C-04 Essential | PASS | PASS | PASS | PASS | PASS |
| C-05 Essential | PASS | PASS | PASS | PASS | PASS |
| C-06 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-07 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-08 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-11 IA sequenced first | PASS | PASS | PASS | PASS | PASS |
| C-13 Ban list enumerated | PASS | PASS | PASS | PASS | PASS |
| C-14 IA counterpoint present | PASS | PASS | PASS | PASS | PASS |
| C-17 IA cost framing | PASS | PASS | PASS | PASS | PASS |
| C-18 Phase gates | PASS | PARTIAL | PASS | PARTIAL | PARTIAL |
| C-19 Named-row ledger | PASS | PASS | PASS | PASS | PASS |
| C-20 IA phase as entry condition | PASS | PASS | PASS | PASS | PASS |
| C-21 Net direction column + derived verdict | PASS | PASS | PASS | PASS | PASS |
| C-22 Dual sub-conditions C1/C2 | PASS | PASS | PASS | PASS | PASS |
| C-23 READ RECEIPT before findings | PASS | PASS | PASS | PASS | PASS |
| C-24 Domain-Lens column | PASS | PASS | PASS | PASS | PASS |
| C-25 Three-clause formula | PASS | PASS | PASS | PASS | PASS |
| C-26 C1/C2 RESULT lines | PASS | PASS | PASS | PASS | PASS |
| C-27 PRE-COMMITMENT precedes findings | PASS | PASS | PASS | PASS | PASS |
| C-28 Each clause own line | PASS | PASS | PASS | PASS | PASS |
| C-29 Seal token | PASS | PASS | PASS | PASS | PASS |
| C-30 Phase C exit names PRE-COMMITMENT | PASS | PARTIAL | PASS | PARTIAL | PARTIAL |
| **C-31 IA counterpoint in finding body** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **C-32 READ RECEIPT cross-references PRE-COMMITMENT (d)(e)** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

**Key differentiators:**
- **C-31**: All five variations enforce it differently — V-01 by template constraint, V-02 by column cell requirement, V-03 by Phase C exit gate, V-04 by typed F-IA finding, V-05 by explicit imperative "EMBED IN DESCRIPTION TEXT"
- **C-32**: All five enforce it — V-01 by pointer label syntax, V-02 by table row template, V-03 by C2 RESULT citation requirement, V-04 by "restated from PRE-COMMITMENT (d)/(e)" notation, V-05 by "INCLUDE POINTER LINES CITING PRE-COMMITMENT BY NAME"
- **C-18/C-30**: V-01, V-03 strongest (full phase-gate pipeline declarations with PRE-COMMITMENT in Phase C exit checklist); V-02, V-04, V-05 partial (phase-like sequence without formal pipeline declaration)

**Best composite candidate**: V-03 or V-01 — both have the full phase-gate pipeline (C-18), the C1/C2 dual sub-conditions (C-22), C1/C2 RESULT lines (C-26), PRE-COMMITMENT in Phase C exit (C-30), and explicit C-31/C-32 enforcement through structural gates.
