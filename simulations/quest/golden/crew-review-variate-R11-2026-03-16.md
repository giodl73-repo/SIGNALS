---
skill: quest-variate
skill_target: crew-review
date: 2026-03-16
round: 11
rubric: crew-review-rubric-v10-2026-03-16.md
---

# crew-review -- Variate R11

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis combinations (V-04, V-05).

**R11 design target**: Under v10, V-01/V-02 R10 score 167.5 (C-29 PASS, C-30 PASS;
C-31 FAIL, C-32 FAIL -- no PHASE 3.5 present). V-03 R10 was designed for C-31/C-32 but
its G2 predicate says "PHASE 4 does not begin until G2 transitions to CLOSED" -- the rubric
requires "AMEND does not begin until G2 transitions to CLOSED" (mirror of G1's "Domain review
does not begin until G1 transitions to CLOSED"). The parallel chain is:

  C-15: challenger as named phase --> C-17: G1 blocks domain review
  C-31: synthesis as named phase  --> C-32: G2 blocks AMEND

V-03 R10's G2 blocks VALIDATE (wrong downstream target). R11 fixes this: all five variations
include PHASE 3.5 -- SYNTHESIZE with G2 state "AMEND does not begin until G2 transitions to
CLOSED." The criterion-check table is extended to 21 rows covering C-26 through C-32.

**Predicted R11 scores under v10**:
- V-01: C-29 PASS + C-30 PASS + C-31 PASS + C-32 PASS = 162.5 + 10.0 = **172.5/172.5**
- V-02: same structural guarantee = **172.5/172.5**
- V-03: same + inertia synthesis emphasis = **172.5/172.5**
- V-04: same + dual-location synthesis = **172.5/172.5**
- V-05: same + verbatim quote chain = **172.5/172.5**

**R11 axes:**

- V-01: Lifecycle emphasis (single axis) -- V-01 R10 base + PHASE 3.5 SYNTHESIZE with G2
  blocking AMEND. Criterion-check table extended to C-32. Minimal structural addition;
  cleanest path to 172.5.

- V-02: Output format (single axis) -- synthesis output declared as a typed 3-column
  synthesis schema (Slot | Verdict Type | Statement). G2 closure verified against synthesis
  table row count. C-30's "typed schema" discipline applied to synthesis output itself.

- V-03: Inertia framing (single axis) -- PHASE 2 makes the status-quo inertia framing
  explicit as the primary challenger lens. PHASE 3.5 synthesis must produce a verdict for
  Slot 1 (inertia) that names its convergence or conflict with domain slots. G2 closure
  condition explicitly includes Slot 1.

- V-04: Lifecycle + Output format (two-axis) -- V-01 + V-02 merged; synthesis contract
  declared in schema section AND enforced by G2 in PHASE 3.5; synthesis typed table output.

- V-05: Lifecycle + Output format + Role sequence (three-axis) -- V-04 + verbatim
  `expertise.relevance` quotes in manifest + L5 registry verification.

**R11 single-axis predictions:**
- V-01 -> C-31 PASS (PHASE 3.5 named), C-32 PASS (G2 blocks AMEND). Predicted: 172.5/172.5
- V-02 -> C-31 PASS (PHASE 3.5 named), C-32 PASS (G2 blocks AMEND). Synthesis table adds
  typed output schema parallel. Predicted: 172.5/172.5
- V-03 -> C-31 PASS (PHASE 3.5 named), C-32 PASS (G2 blocks AMEND). Inertia axis does not
  weaken any criterion. Predicted: 172.5/172.5

**R11 two-axis predictions:**
- V-04 -> 172.5/172.5 via dual synthesis enforcement path
- V-05 -> 172.5/172.5 plus verbatim quote chain; strongest C-01/C-06 evidence

---

## V-01

**Axis**: Lifecycle emphasis -- direct PHASE 3.5 integration
**Hypothesis**: All R10 V-01 mechanisms are preserved. The single gap is C-31/C-32: R10 V-01
has no named synthesis phase and no G2 gate. Adding PHASE 3.5 -- SYNTHESIZE with G2 state
"AMEND does not begin until G2 transitions to CLOSED" closes both. The criterion-check table
is extended from 17 rows (through C-28) to 21 rows (through C-32), with per-row remediation
in every added row. C-29 PASS (exhaustive -- all 21 rows carry remediation). C-30 PASS (typed
5-column header). C-31 PASS (PHASE 3.5 header at same level as PHASE 3). C-32 PASS (AMEND
blocked by G2). Predicted: 172.5/172.5.

---

You are running `/crew-review`.

This skill executes in six lifecycle phases. The output schema -- including a Slot column
and a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. PHASE 3.5 synthesizes cross-role signals and gates AMEND before
PHASE 4 validates. PHASE 4 validates the draft matrix before final render.

---

### Output schema (declared before execution)

The review artifact is a 6-column matrix. All column contracts are binding. The per-row
validation gate in PHASE 4 enforces every cell against these contracts.

| Column | Type -- valid | Anti-pattern excluded |
|--------|--------------|----------------------|
| Slot | integer or sub-lettered integer -- Slot 1 = challenger bracket; 1a/1b/1c/1d = slot-gap escalation rows in slot-letter order; 2, 3, ... = domain roles in manifest order | NOT: absent Slot cells; NOT: non-integer labels; NOT: Slot values that conflict with the manifest |
| Role | string -- filename stem from `.roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not present in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern traceable to this role's `lens.verify`]." | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns not traceable to this role's `lens.verify` field; NOT: multi-sentence declarations; NOT: absent Lens cells; NOT: Lens cells that merely restate the role name |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: observations naming only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

**AMEND output contract**: options targeting specific findings MUST use slot numbers.
`--amend rerun:slot[N]`, `--amend add:slot[N+1]:[role-name]`.
AMEND does not begin until PHASE 3.5 G2 transitions to CLOSED.

---

### Slot manifest (declare before PHASE 1)

Before any phase executes, write and commit the slot manifest:

```
Slot manifest -- crew-review
Depth: [standard | deep]
Artifact type: [inferred from artifact]

Slot 1:  [challenger-role-name] (archetype: challenger)
Slot 2:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
Slot 3:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
...
```

Rules: Slot 1 = all roles with `archetype: challenger`. Slots 2-N (standard) = 2-3
non-challenger roles ranked by `expertise.relevance` to artifact type. Slots 2-N (deep) =
all non-challenger roles ranked by relevance then alphabetical. Manifest is locked. Roles
absent from manifest may not appear in the matrix. Roles in the manifest may not be skipped.

---

### PHASE 1 -- LOAD

**Entry**: slot manifest committed
**Exit**: role pool locked and verified

**L1** Open `.roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .roles/ not found.` Halt.
  - Directory empty: `ERROR: .roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked)
**Gate G1** -- challenger bracket gate

**G1 state: OPEN.** Domain review is blocked.

**G1 closure predicate** -- G1 transitions from OPEN to CLOSED when ALL hold:
1. All Slot 1 roles have run.
2. The null hypothesis 4-slot form has been attempted for each Slot 1 role.
3. For every slot that could not be filled: a dedicated, separate 6-column matrix row exists
   in the draft output, validated against the output schema above, Severity = HIGH.
4. No unfilled slot was silently omitted, collapsed into another slot, or approximated with
   a generic placeholder ("some cost", "the existing workflow", "the current process").

**Domain review does not begin until G1 transitions to CLOSED.**

---

**C1** Identify all Slot 1 roles (all roles with `archetype: challenger`).

**C2** For each Slot 1 role, fill the null hypothesis 4-slot form:

```
SLOT-A: We currently do [______] instead of building this.
SLOT-B: The cost of that alternative is [______].
SLOT-C: The switching cost to adopt this artifact is [______].
SLOT-D: This artifact is worth acting on only if [______].
```

**C3** Fill each slot from artifact content or inferable workspace context.

**C4** Slot-to-row escalation rule -- mandatory, applies to each slot individually:

When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position in the 4-slot form.
2. Produce a **separate, dedicated matrix row** -- a full 6-column row following the output
   schema:
   - Slot: `1[letter]` (1a for SLOT-A gap, 1b for SLOT-B gap, etc.)
   - Role: `[challenger-role-name]`
   - Lens: "As a [role], I care about null hypothesis completeness -- SLOT-[letter] is
     missing from the artifact."
   - Findings: "SLOT-[letter] gap: [slot label] not stated in the artifact. Null hypothesis
     is incomplete without this field."
   - Severity: HIGH
   - Recommendation: "State [slot requirement] explicitly in [artifact section] before
     this artifact proceeds to domain review."
3. **Do not embed this finding as a sentence within the challenger row's Findings cell.**
   A sentence inside another row's Findings cell is not a dedicated row. A dedicated row
   is a full 6-column entry in the matrix. Anything else does not satisfy G1 closure
   condition 3.
4. **Do not append this as a note or comment below the challenger row.** An appended note
   is not a matrix row. It does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled slots = two separate rows.
6. Apply per-row validation gate (PHASE 4 contract) before writing this row.

**C5** Challenger primary row:
- Slot: 1
- Lens: "As a [role], I care about [specific concern from this role's `lens.verify`]."
- Findings: the filled/attempted 4-slot form plus the challenger's primary concern.
- Severity: HIGH (inertia credible, unaddressed) / MEDIUM (named, cost unstated) /
  LOW (artifact directly neutralizes status quo).
- Recommendation: one concrete action naming what to do and where.
- Apply per-row validation gate before writing.

**C6** Verify G1 closure predicate. All 4 conditions true?

Write: `[G1: CLOSED -- conditions 1-4 verified]`

**G1 state: CLOSED.** Proceed to PHASE 3.

---

### PHASE 3 -- REVIEW

**Entry**: G1 is CLOSED (PHASE 2 exit)

**D1** Depth selection:
- Standard (default): from non-Slot-1 roles, select those whose `expertise.relevance`
  intersects the artifact type. Target 2-4. Document each: "[role]: selected because [reason]."
- `--depth deep`: all non-Slot-1 roles per manifest.

**D2** Execute each slot in manifest order. For each slot:
1. Lens cell: "As a [role], I care about [specific concern from this role's `lens.verify`]."
   Check against Lens column anti-pattern exclusion. Not a generic restatement.
2. Findings cell: name a specific artifact surface. No abstract observations. No repeating
   a finding already raised by a lower-numbered slot.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where in the artifact.

Collect all rows into draft matrix. Do not write final output -- PHASE 3.5 synthesizes first.

---

### PHASE 3.5 -- SYNTHESIZE

**Entry**: PHASE 3 exit (all domain rows collected)
**Gate G2** -- synthesis gate

**G2 state: OPEN.** AMEND is blocked.

**G2 closure predicate** -- G2 transitions from OPEN to CLOSED when ALL hold:
1. Every slot in the manifest (including slot-gap escalation rows 1a/1b/1c/1d) has been
   assigned exactly one verdict.
2. Each verdict is one of: converged, conflicted, or unique.
3. No slot is omitted, merged with another, or assigned more than one verdict.
4. Every verdict statement references slot numbers.

**AMEND does not begin until G2 transitions to CLOSED.**

---

**S1** For every slot in the manifest (Slot 1 through Slot N, including any slot-gap
escalation rows), assign exactly one verdict:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

**S2** Check G2 predicate. Every slot assigned exactly one verdict?

Write: `[G2: CLOSED -- [N] slots in manifest, [N] verdicts assigned]`

**G2 state: CLOSED.** Proceed to PHASE 4.

---

### PHASE 4 -- VALIDATE

**Entry**: G2 is CLOSED (PHASE 3.5 exit)
**Exit**: verification complete; matrix ready for PHASE 5 render

For each row in the draft matrix, verify all six cells against the output schema:
- Slot: consistent with manifest; sub-lettered for slot-gap escalation rows
- Role: filename stem exists in `.roles/` at this execution
- Lens: one sentence, traceable to `lens.verify`, not a generic restatement
- Findings: names a specific artifact surface, not abstract
- Severity: exactly HIGH, MEDIUM, or LOW
- Recommendation: names what to do + where

If a cell fails: revise before writing. A row that cannot pass is removed and logged:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write the criterion-check table below before writing the final matrix. This table covers ALL
aspirational criteria through the current rubric version (v10), including C-26 through C-32
themselves. A table that stops before C-32 fails C-26 under v10. Every row carries a
"Remediation if NO" column -- execute any NO instruction before proceeding to PHASE 5:

| Criterion | Description | Status | Evidence in this draft | Remediation if NO |
|-----------|-------------|--------|------------------------|-------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] | Return to PHASE 2 C2-C4; attempt all 4 slots; escalate each unfilled slot to a dedicated matrix row |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] | Return to each row with missing or generic Lens; rewrite from this role's `lens.verify` field |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] | Add output schema table before execution; reference it in this PHASE 4 gate |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] | Rename the challenger section to "PHASE 2 -- CHALLENGE" at the same heading level as PHASE 3 |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] | Return to PHASE 2 C4; produce one dedicated HIGH-severity matrix row for each unfilled slot |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] | Add G1 OPEN/CLOSED states and "Domain review does not begin until G1 transitions to CLOSED" statement |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] | Remove any inline annotations; replace with full 6-column matrix rows at 1a/1b/1c/1d positions |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] | Add NOT: exclusions to the Lens and Findings column definitions in the output schema table |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] | Add explicit OPEN/CLOSED state labels and enumerate at least 2 closure conditions under the G1 predicate |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] | Add explicit "Do not embed..." and "Do not append..." prohibitions inside the escalation rule text |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N and Slot M..."] | Add Slot as the first matrix column; revise synthesis to use "Slot [N] and Slot [M]..." |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] | Rename the validation section to "PHASE 4 -- VALIDATE" at the same heading level as PHASE 2 and PHASE 3 |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] | Move the criterion-check table inside the PHASE 4 -- VALIDATE section |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions in schema table] | Add NOT: exclusion cells to all columns in the output schema table that lack them |
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v10, including C-26 through C-32 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28, C-29, C-30, C-31, C-32 rows present in this table] | Add rows for any missing aspirational criteria including C-26 through C-32 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [G2 closed: [N]/[N] slots assigned verdicts in PHASE 3.5] | Return to PHASE 3.5; G2 cannot close until every slot has exactly one verdict -- assign a verdict to each missing slot |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a "Remediation if NO" column with a specific action] | Add a "Remediation if NO" column entry to every row that lacks one |
| C-29 | Exhaustive criterion-failure remediation coverage -- every row, not just at least one | [YES/NO/PARTIAL] | [all 21 rows in this table carry a populated Remediation if NO cell] | Ensure every row has a specific, actionable remediation instruction -- no row may be empty or generic |
| C-30 | Criterion-check table presented as typed 5-column schema with dedicated "Remediation if NO" column | [YES/NO/PARTIAL] | [column header reads: Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO] | Reformat table as typed 5-column schema with "Remediation if NO" as the 5th named header column |
| C-31 | Synthesis declared as a named discrete execution phase (PHASE 3.5 SYNTHESIZE) | [YES/NO/PARTIAL] | [PHASE 3.5 -- SYNTHESIZE header present at same heading level as PHASE 3 and PHASE 4] | Add PHASE 3.5 -- SYNTHESIZE as a named section heading between PHASE 3 and PHASE 4; move synthesis execution into it |
| C-32 | Synthesis phase gate G2 has formal exit condition blocking AMEND until synthesis closes | [YES/NO/PARTIAL] | [G2 OPEN/CLOSED states present + "AMEND does not begin until G2 transitions to CLOSED" statement in PHASE 3.5] | Add G2 state machine with OPEN/CLOSED labels and enumerated closure predicate; add explicit "AMEND does not begin until G2 transitions to CLOSED" blocking statement |

Execute all NO instructions before writing the final matrix.
PARTIAL: note the gap in the Evidence cell and proceed.

---

### PHASE 5 -- RENDER

**Entry**: PHASE 4 verification complete

**R1** Header:

```
Crew Review: [artifact name or type]
Depth: standard | deep
Slots: [list slot numbers and roles]
Roles: [list in slot order]
```

**R2** Review matrix (6 columns, rows in slot order):

| Slot | Role | Lens | Findings | Severity | Recommendation |
|------|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s) from PHASE 2
2. Slot-gap escalation rows (1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

**R3** Cross-role synthesis (render from PHASE 3.5 G2-verified output):

Copy the synthesis verdicts produced in PHASE 3.5 S1. Every slot already has exactly one
verdict assigned under G2 closure. Render each verdict in slot-number order:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-02

**Axis**: Output format -- synthesis output as typed 3-column synthesis schema
**Hypothesis**: V-01 R11 declares per-slot synthesis verdicts as prose statements. An
alternative output format treats synthesis output as a typed schema table parallel to the
review matrix: Slot | Verdict Type | Statement. G2 closure verifies against the synthesis
table's row count vs. manifest slot count (table completeness check, same pattern as PHASE 4
validates against output schema). The typed synthesis table makes C-30's "typed schema with
dedicated column" discipline apply to synthesis output itself, not just the criterion-check
table. Predicted: 172.5/172.5. Variation-specific signal: typed synthesis schema as a
potential C-33 candidate (schema discipline applied to every phase output, not just the
review matrix and criterion-check table).

---

You are running `/crew-review`.

This skill executes in six lifecycle phases. Two typed schemas govern output: the 6-column
review matrix schema and the 3-column synthesis schema. Both are declared before execution
begins. PHASE 3.5 produces the synthesis table and gates AMEND. PHASE 4 validates the
draft matrix before final render.

---

### Output schemas (declared before execution)

**Review matrix schema** -- 6-column typed table. All column contracts are binding. The
per-row validation gate in PHASE 4 enforces every cell against these contracts.

| Column | Type -- valid | Anti-pattern excluded |
|--------|--------------|----------------------|
| Slot | integer or sub-lettered integer -- Slot 1 = challenger bracket; 1a/1b/1c/1d = slot-gap escalation rows in slot-letter order; 2, 3, ... = domain roles in manifest order | NOT: absent Slot cells; NOT: non-integer labels; NOT: Slot values that conflict with the manifest |
| Role | string -- filename stem from `.roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not present in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern traceable to this role's `lens.verify`]." | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns not traceable to this role's `lens.verify` field; NOT: multi-sentence declarations; NOT: absent Lens cells; NOT: Lens cells that merely restate the role name |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: observations naming only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

**Synthesis schema** -- 3-column typed table produced in PHASE 3.5. Every manifest slot
receives exactly one row. G2 closure verifies row count equals slot count.

| Column | Type -- valid | Anti-pattern excluded |
|--------|--------------|----------------------|
| Slot | integer or slot-letter -- must match manifest slot number exactly | NOT: absent Slot cells; NOT: slot numbers not in manifest; NOT: merged or grouped entries ("Slots 2-3") |
| Verdict Type | enum -- exactly `converged`, `conflicted`, or `unique` | NOT: freestyle labels; NOT: absent cells; NOT: combinations |
| Statement | string -- `Slot [N] converged with Slot [M]: both find [shared concern].` OR `Slot [N] conflicts with Slot [M]: [tension description].` OR `Slot [N] is unique: [finding not overlapping with any other slot].` | NOT: statements that do not reference slot numbers; NOT: generic observations without a named finding |

**AMEND output contract**: options targeting specific findings MUST use slot numbers.
`--amend rerun:slot[N]`, `--amend add:slot[N+1]:[role-name]`.
AMEND does not begin until PHASE 3.5 G2 transitions to CLOSED.

---

### Slot manifest (declare before PHASE 1)

Before any phase executes, write and commit the slot manifest:

```
Slot manifest -- crew-review
Depth: [standard | deep]
Artifact type: [inferred from artifact]

Slot 1:  [challenger-role-name] (archetype: challenger)
Slot 2:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
Slot 3:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
...
```

Rules: Slot 1 = all roles with `archetype: challenger`. Slots 2-N (standard) = 2-3
non-challenger roles ranked by `expertise.relevance` to artifact type. Slots 2-N (deep) =
all non-challenger roles ranked by relevance then alphabetical. Manifest is locked. Roles
absent from manifest may not appear in the matrix. Roles in the manifest may not be skipped.

---

### PHASE 1 -- LOAD

**Entry**: slot manifest committed
**Exit**: role pool locked and verified

**L1** Open `.roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .roles/ not found.` Halt.
  - Directory empty: `ERROR: .roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked)
**Gate G1** -- challenger bracket gate

**G1 state: OPEN.** Domain review is blocked.

**G1 closure predicate** -- G1 transitions from OPEN to CLOSED when ALL hold:
1. All Slot 1 roles have run.
2. The null hypothesis 4-slot form has been attempted for each Slot 1 role.
3. For every slot that could not be filled: a dedicated, separate 6-column matrix row exists
   in the draft output, validated against the review matrix schema above, Severity = HIGH.
4. No unfilled slot was silently omitted, collapsed into another slot, or approximated with
   a generic placeholder ("some cost", "the existing workflow", "the current process").

**Domain review does not begin until G1 transitions to CLOSED.**

---

**C1** Identify all Slot 1 roles (all roles with `archetype: challenger`).

**C2** For each Slot 1 role, fill the null hypothesis 4-slot form:

```
SLOT-A: We currently do [______] instead of building this.
SLOT-B: The cost of that alternative is [______].
SLOT-C: The switching cost to adopt this artifact is [______].
SLOT-D: This artifact is worth acting on only if [______].
```

**C3** Fill each slot from artifact content or inferable workspace context.

**C4** Slot-to-row escalation rule -- mandatory, applies to each slot individually:

When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position in the 4-slot form.
2. Produce a **separate, dedicated matrix row** -- a full 6-column row following the review
   matrix schema:
   - Slot: `1[letter]` (1a for SLOT-A gap, 1b for SLOT-B gap, etc.)
   - Role: `[challenger-role-name]`
   - Lens: "As a [role], I care about null hypothesis completeness -- SLOT-[letter] is
     missing from the artifact."
   - Findings: "SLOT-[letter] gap: [slot label] not stated in the artifact. Null hypothesis
     is incomplete without this field."
   - Severity: HIGH
   - Recommendation: "State [slot requirement] explicitly in [artifact section] before
     this artifact proceeds to domain review."
3. **Do not embed this finding as a sentence within the challenger row's Findings cell.**
   A sentence inside another row's Findings cell is not a dedicated row. A dedicated row
   is a full 6-column entry in the matrix. Anything else does not satisfy G1 closure
   condition 3.
4. **Do not append this as a note or comment below the challenger row.** An appended note
   is not a matrix row. It does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled slots = two separate rows.
6. Apply per-row validation gate (PHASE 4 contract) before writing this row.

**C5** Challenger primary row:
- Slot: 1
- Lens: "As a [role], I care about [specific concern from this role's `lens.verify`]."
- Findings: the filled/attempted 4-slot form plus the challenger's primary concern.
- Severity: HIGH (inertia credible, unaddressed) / MEDIUM (named, cost unstated) /
  LOW (artifact directly neutralizes status quo).
- Recommendation: one concrete action naming what to do and where.
- Apply per-row validation gate before writing.

**C6** Verify G1 closure predicate. All 4 conditions true?

Write: `[G1: CLOSED -- conditions 1-4 verified]`

**G1 state: CLOSED.** Proceed to PHASE 3.

---

### PHASE 3 -- REVIEW

**Entry**: G1 is CLOSED (PHASE 2 exit)

**D1** Depth selection:
- Standard (default): from non-Slot-1 roles, select those whose `expertise.relevance`
  intersects the artifact type. Target 2-4. Document each: "[role]: selected because [reason]."
- `--depth deep`: all non-Slot-1 roles per manifest.

**D2** Execute each slot in manifest order. For each slot:
1. Lens cell: "As a [role], I care about [specific concern from this role's `lens.verify`]."
   Check against Lens column anti-pattern exclusion. Not a generic restatement.
2. Findings cell: name a specific artifact surface. No abstract observations. No repeating
   a finding already raised by a lower-numbered slot.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where in the artifact.

Collect all rows into draft matrix. Do not write final output -- PHASE 3.5 synthesizes first.

---

### PHASE 3.5 -- SYNTHESIZE

**Entry**: PHASE 3 exit (all domain rows collected)
**Gate G2** -- synthesis gate

**G2 state: OPEN.** AMEND is blocked.

**G2 closure predicate** -- G2 transitions from OPEN to CLOSED when ALL hold:
1. The synthesis table (3-column: Slot | Verdict Type | Statement) contains exactly one
   row for every slot in the manifest, including slot-gap escalation rows 1a/1b/1c/1d.
2. Every row's Verdict Type is exactly `converged`, `conflicted`, or `unique`.
3. Every row's Statement follows the synthesis schema format and references slot numbers.
4. No slot appears more than once in the synthesis table.

**AMEND does not begin until G2 transitions to CLOSED.**

---

**S1** For every slot in the manifest (Slot 1 through Slot N, including any slot-gap
escalation rows), produce one row in the synthesis table:

| Slot | Verdict Type | Statement |
|------|-------------|-----------|
| [N] | converged | `Slot [N] converged with Slot [M]: both find [shared concern].` |
| [N] | conflicted | `Slot [N] conflicts with Slot [M]: [tension description].` |
| [N] | unique | `Slot [N] is unique: [finding not overlapping with any other slot].` |

**S2** Check G2 predicate. Synthesis table row count equals manifest slot count?

Write: `[G2: CLOSED -- [N] manifest slots, [N] synthesis table rows; all verdict types valid]`

**G2 state: CLOSED.** Proceed to PHASE 4.

---

### PHASE 4 -- VALIDATE

**Entry**: G2 is CLOSED (PHASE 3.5 exit)
**Exit**: verification complete; matrix ready for PHASE 5 render

For each row in the draft matrix, verify all six cells against the review matrix schema:
- Slot: consistent with manifest; sub-lettered for slot-gap escalation rows
- Role: filename stem exists in `.roles/` at this execution
- Lens: one sentence, traceable to `lens.verify`, not a generic restatement
- Findings: names a specific artifact surface, not abstract
- Severity: exactly HIGH, MEDIUM, or LOW
- Recommendation: names what to do + where

If a cell fails: revise before writing. A row that cannot pass is removed and logged:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write the criterion-check table below before writing the final matrix. This table covers ALL
aspirational criteria through the current rubric version (v10), including C-26 through C-32
themselves. A table that stops before C-32 fails C-26 under v10. Every row carries a
"Remediation if NO" column -- execute any NO instruction before proceeding to PHASE 5:

| Criterion | Description | Status | Evidence in this draft | Remediation if NO |
|-----------|-------------|--------|------------------------|-------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] | Return to PHASE 2 C2-C4; attempt all 4 slots; escalate each unfilled slot to a dedicated matrix row |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] | Return to each row with missing or generic Lens; rewrite from this role's `lens.verify` field |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [review matrix schema present / PHASE 4 validates before write] | Add output schema table before execution; reference it in this PHASE 4 gate |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] | Rename the challenger section to "PHASE 2 -- CHALLENGE" at the same heading level as PHASE 3 |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] | Return to PHASE 2 C4; produce one dedicated HIGH-severity matrix row for each unfilled slot |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] | Add G1 OPEN/CLOSED states and "Domain review does not begin until G1 transitions to CLOSED" statement |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] | Remove any inline annotations; replace with full 6-column matrix rows at 1a/1b/1c/1d positions |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] | Add NOT: exclusions to the Lens and Findings column definitions in the review matrix schema |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] | Add explicit OPEN/CLOSED state labels and enumerate at least 2 closure conditions under the G1 predicate |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] | Add explicit "Do not embed..." and "Do not append..." prohibitions inside the escalation rule text |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present in review matrix / synthesis table uses "Slot N..."] | Add Slot as the first matrix column; synthesis table uses "Slot [N]" in every Statement |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] | Rename the validation section to "PHASE 4 -- VALIDATE" at the same heading level as PHASE 2 and PHASE 3 |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] | Move the criterion-check table inside the PHASE 4 -- VALIDATE section |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 review matrix columns + all 3 synthesis schema columns have NOT: exclusions] | Add NOT: exclusion cells to all schema columns that lack them |
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v10, including C-26 through C-32 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28, C-29, C-30, C-31, C-32 rows present in this table] | Add rows for any missing aspirational criteria including C-26 through C-32 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [synthesis table: [N] rows for [N] manifest slots; G2 closed] | Return to PHASE 3.5; G2 cannot close until every slot has one synthesis table row -- produce missing rows |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a "Remediation if NO" column with a specific action] | Add a specific return-to-phase instruction to every row that lacks one |
| C-29 | Exhaustive criterion-failure remediation coverage -- every row, not just at least one | [YES/NO/PARTIAL] | [all 21 rows in this table carry a populated Remediation if NO cell] | Ensure every row has a specific, actionable remediation instruction -- no row may be empty or generic |
| C-30 | Criterion-check table presented as typed 5-column schema with dedicated "Remediation if NO" column | [YES/NO/PARTIAL] | [column header reads: Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO] | Reformat table as typed 5-column schema with "Remediation if NO" as the 5th named header column |
| C-31 | Synthesis declared as a named discrete execution phase (PHASE 3.5 SYNTHESIZE) | [YES/NO/PARTIAL] | [PHASE 3.5 -- SYNTHESIZE header present at same heading level as PHASE 3 and PHASE 4] | Add PHASE 3.5 -- SYNTHESIZE as a named section heading between PHASE 3 and PHASE 4; move synthesis execution into it |
| C-32 | Synthesis phase gate G2 has formal exit condition blocking AMEND until synthesis closes | [YES/NO/PARTIAL] | [G2 OPEN/CLOSED states present + "AMEND does not begin until G2 transitions to CLOSED" statement in PHASE 3.5] | Add G2 state machine with OPEN/CLOSED labels; add explicit "AMEND does not begin until G2 transitions to CLOSED" blocking statement |

Execute all NO instructions before writing the final matrix.
PARTIAL: note the gap in the Evidence cell and proceed.

---

### PHASE 5 -- RENDER

**Entry**: PHASE 4 verification complete

**R1** Header:

```
Crew Review: [artifact name or type]
Depth: standard | deep
Slots: [list slot numbers and roles]
Roles: [list in slot order]
```

**R2** Review matrix (6 columns, rows in slot order):

| Slot | Role | Lens | Findings | Severity | Recommendation |
|------|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s) from PHASE 2
2. Slot-gap escalation rows (1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

**R3** Cross-role synthesis (render from PHASE 3.5 G2-verified synthesis table):

Render the synthesis table produced in PHASE 3.5. Row order: slot number ascending.

| Slot | Verdict Type | Statement |
|------|-------------|-----------|

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-03

**Axis**: Inertia framing -- status-quo challenger made explicit in PHASE 3.5 synthesis
**Hypothesis**: The challenger bracket (PHASE 2) establishes the inertia competitor. But
synthesis in R10 treats Slot 1 the same as domain slots -- it may receive "unique" without
ever naming what the inertia implies for domain slots. Strengthening inertia framing in
PHASE 3.5 requires the synthesis step to produce a verdict for Slot 1 that names whether the
inertia finding is reinforced or defeated by each domain slot. G2 closure condition 1
explicitly names Slot 1 (inertia/challenger) as a required entry. This makes the status-quo
challenger a primary synthesis node rather than just a first-phase reviewer. Predicted:
172.5/172.5. Variation-specific signal: inertia-synthesis integration as a potential C-33
candidate (synthesis verdict for Slot 1 must name inertia implications for domain slots).

---

You are running `/crew-review`.

This skill executes in six lifecycle phases. The output schema -- including a Slot column
and a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. PHASE 3.5 synthesizes cross-role signals with explicit inertia-domain
reconciliation and gates AMEND. PHASE 4 validates the draft matrix before final render.

---

### Output schema (declared before execution)

The review artifact is a 6-column matrix. All column contracts are binding. The per-row
validation gate in PHASE 4 enforces every cell against these contracts.

| Column | Type -- valid | Anti-pattern excluded |
|--------|--------------|----------------------|
| Slot | integer or sub-lettered integer -- Slot 1 = challenger bracket; 1a/1b/1c/1d = slot-gap escalation rows in slot-letter order; 2, 3, ... = domain roles in manifest order | NOT: absent Slot cells; NOT: non-integer labels; NOT: Slot values that conflict with the manifest |
| Role | string -- filename stem from `.roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not present in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern traceable to this role's `lens.verify`]." | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns not traceable to this role's `lens.verify` field; NOT: multi-sentence declarations; NOT: absent Lens cells; NOT: Lens cells that merely restate the role name |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: observations naming only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

**AMEND output contract**: options targeting specific findings MUST use slot numbers.
`--amend rerun:slot[N]`, `--amend add:slot[N+1]:[role-name]`.
AMEND does not begin until PHASE 3.5 G2 transitions to CLOSED.

---

### Slot manifest (declare before PHASE 1)

Before any phase executes, write and commit the slot manifest:

```
Slot manifest -- crew-review
Depth: [standard | deep]
Artifact type: [inferred from artifact]

Slot 1:  [challenger-role-name] (archetype: challenger) -- inertia competitor: [what teams
         currently do instead of adopting this artifact]
Slot 2:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
Slot 3:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
...
```

Rules: Slot 1 = all roles with `archetype: challenger`. The inertia competitor field names
the status-quo alternative identified during PHASE 2. Slots 2-N (standard) = 2-3
non-challenger roles ranked by `expertise.relevance` to artifact type. Slots 2-N (deep) =
all non-challenger roles ranked by relevance then alphabetical. Manifest is locked. Roles
absent from manifest may not appear in the matrix. Roles in the manifest may not be skipped.

---

### PHASE 1 -- LOAD

**Entry**: slot manifest committed
**Exit**: role pool locked and verified

**L1** Open `.roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .roles/ not found.` Halt.
  - Directory empty: `ERROR: .roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked)
**Gate G1** -- challenger bracket gate

**G1 state: OPEN.** Domain review is blocked.

The challenger is the status-quo inertia advocate: the role that argues for continuing
current practice over adopting this artifact. Every null hypothesis form tests whether the
artifact is worth displacing existing behavior. Domain review cannot assess value without
first naming what value must exceed.

**G1 closure predicate** -- G1 transitions from OPEN to CLOSED when ALL hold:
1. All Slot 1 roles have run.
2. The null hypothesis 4-slot form has been attempted for each Slot 1 role.
3. For every slot that could not be filled: a dedicated, separate 6-column matrix row exists
   in the draft output, validated against the output schema above, Severity = HIGH.
4. No unfilled slot was silently omitted, collapsed into another slot, or approximated with
   a generic placeholder ("some cost", "the existing workflow", "the current process").

**Domain review does not begin until G1 transitions to CLOSED.**

---

**C1** Identify all Slot 1 roles (all roles with `archetype: challenger`).

**C2** For each Slot 1 role, fill the null hypothesis 4-slot form:

```
SLOT-A: We currently do [______] instead of building this.
SLOT-B: The cost of that alternative is [______].
SLOT-C: The switching cost to adopt this artifact is [______].
SLOT-D: This artifact is worth acting on only if [______].
```

SLOT-A names the inertia competitor (what teams currently do). This forms the basis for
PHASE 3.5 synthesis: domain slots will converge with or conflict against this inertia.

**C3** Fill each slot from artifact content or inferable workspace context.

**C4** Slot-to-row escalation rule -- mandatory, applies to each slot individually:

When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position in the 4-slot form.
2. Produce a **separate, dedicated matrix row** -- a full 6-column row following the output
   schema:
   - Slot: `1[letter]` (1a for SLOT-A gap, 1b for SLOT-B gap, etc.)
   - Role: `[challenger-role-name]`
   - Lens: "As a [role], I care about null hypothesis completeness -- SLOT-[letter] is
     missing from the artifact."
   - Findings: "SLOT-[letter] gap: [slot label] not stated in the artifact. Null hypothesis
     is incomplete without this field."
   - Severity: HIGH
   - Recommendation: "State [slot requirement] explicitly in [artifact section] before
     this artifact proceeds to domain review."
3. **Do not embed this finding as a sentence within the challenger row's Findings cell.**
   A sentence inside another row's Findings cell is not a dedicated row. A dedicated row
   is a full 6-column entry in the matrix. Anything else does not satisfy G1 closure
   condition 3.
4. **Do not append this as a note or comment below the challenger row.** An appended note
   is not a matrix row. It does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled slots = two separate rows.
6. Apply per-row validation gate (PHASE 4 contract) before writing this row.

**C5** Challenger primary row:
- Slot: 1
- Lens: "As a [role], I care about [specific concern from this role's `lens.verify`]."
- Findings: the filled/attempted 4-slot form plus the challenger's primary concern.
- Severity: HIGH (inertia credible, unaddressed) / MEDIUM (named, cost unstated) /
  LOW (artifact directly neutralizes status quo).
- Recommendation: one concrete action naming what to do and where.
- Apply per-row validation gate before writing.

**C6** Verify G1 closure predicate. All 4 conditions true?

Write: `[G1: CLOSED -- conditions 1-4 verified]`

**G1 state: CLOSED.** Proceed to PHASE 3.

---

### PHASE 3 -- REVIEW

**Entry**: G1 is CLOSED (PHASE 2 exit)

**D1** Depth selection:
- Standard (default): from non-Slot-1 roles, select those whose `expertise.relevance`
  intersects the artifact type. Target 2-4. Document each: "[role]: selected because [reason]."
- `--depth deep`: all non-Slot-1 roles per manifest.

**D2** Execute each slot in manifest order. For each slot:
1. Lens cell: "As a [role], I care about [specific concern from this role's `lens.verify`]."
   Check against Lens column anti-pattern exclusion. Not a generic restatement.
2. Findings cell: name a specific artifact surface. No abstract observations. No repeating
   a finding already raised by a lower-numbered slot.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where in the artifact.

Collect all rows into draft matrix. Do not write final output -- PHASE 3.5 synthesizes first.

---

### PHASE 3.5 -- SYNTHESIZE

**Entry**: PHASE 3 exit (all domain rows collected)
**Gate G2** -- synthesis gate

**G2 state: OPEN.** AMEND is blocked.

**G2 closure predicate** -- G2 transitions from OPEN to CLOSED when ALL hold:
1. Slot 1 (challenger/inertia) has received a verdict that explicitly names its relationship
   to at least one domain slot's finding.
2. Every remaining slot in the manifest (including slot-gap escalation rows 1a/1b/1c/1d)
   has been assigned exactly one verdict.
3. Each verdict is one of: converged, conflicted, or unique.
4. Every verdict statement references slot numbers.

**AMEND does not begin until G2 transitions to CLOSED.**

---

**S1** Begin with Slot 1 (inertia/challenger). Its verdict must name how the domain's
findings address or fail to address the inertia identified in SLOT-A of the null hypothesis:
- `Slot 1 converged with Slot [M]: both find that [shared concern about the inertia].`
- `Slot 1 conflicts with Slot [M]: Slot 1 finds [inertia concern] but Slot [M] finds [counter].`
- `Slot 1 is unique: [inertia concern raised by Slot 1 is not reflected in any domain slot].`

**S2** For every remaining slot in the manifest (Slots 2-N, including slot-gap escalation
rows), assign exactly one verdict:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

**S3** Check G2 predicate. Slot 1 verdict explicitly names inertia relationship? Every slot
assigned exactly one verdict?

Write: `[G2: CLOSED -- [N] slots in manifest, [N] verdicts assigned; Slot 1 inertia verdict present]`

**G2 state: CLOSED.** Proceed to PHASE 4.

---

### PHASE 4 -- VALIDATE

**Entry**: G2 is CLOSED (PHASE 3.5 exit)
**Exit**: verification complete; matrix ready for PHASE 5 render

For each row in the draft matrix, verify all six cells against the output schema:
- Slot: consistent with manifest; sub-lettered for slot-gap escalation rows
- Role: filename stem exists in `.roles/` at this execution
- Lens: one sentence, traceable to `lens.verify`, not a generic restatement
- Findings: names a specific artifact surface, not abstract
- Severity: exactly HIGH, MEDIUM, or LOW
- Recommendation: names what to do + where

If a cell fails: revise before writing. A row that cannot pass is removed and logged:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write the criterion-check table below before writing the final matrix. This table covers ALL
aspirational criteria through the current rubric version (v10), including C-26 through C-32
themselves. A table that stops before C-32 fails C-26 under v10. Every row carries a
"Remediation if NO" column -- execute any NO instruction before proceeding to PHASE 5:

| Criterion | Description | Status | Evidence in this draft | Remediation if NO |
|-----------|-------------|--------|------------------------|-------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] | Return to PHASE 2 C2-C4; attempt all 4 slots; escalate each unfilled slot to a dedicated matrix row |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] | Return to each row with missing or generic Lens; rewrite from this role's `lens.verify` field |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] | Add output schema table before execution; reference it in this PHASE 4 gate |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] | Rename the challenger section to "PHASE 2 -- CHALLENGE" at the same heading level as PHASE 3 |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] | Return to PHASE 2 C4; produce one dedicated HIGH-severity matrix row for each unfilled slot |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] | Add G1 OPEN/CLOSED states and "Domain review does not begin until G1 transitions to CLOSED" statement |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] | Remove any inline annotations; replace with full 6-column matrix rows at 1a/1b/1c/1d positions |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] | Add NOT: exclusions to the Lens and Findings column definitions in the output schema table |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] | Add explicit OPEN/CLOSED state labels and enumerate at least 2 closure conditions under the G1 predicate |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] | Add explicit "Do not embed..." and "Do not append..." prohibitions inside the escalation rule text |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N and Slot M..."] | Add Slot as the first matrix column; revise synthesis to use "Slot [N] and Slot [M]..." |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] | Rename the validation section to "PHASE 4 -- VALIDATE" at the same heading level as PHASE 2 and PHASE 3 |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] | Move the criterion-check table inside the PHASE 4 -- VALIDATE section |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions in schema table] | Add NOT: exclusion cells to all columns in the output schema table that lack them |
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v10, including C-26 through C-32 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28, C-29, C-30, C-31, C-32 rows present in this table] | Add rows for any missing aspirational criteria including C-26 through C-32 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [G2 closed: [N]/[N] slots assigned verdicts; Slot 1 inertia verdict present] | Return to PHASE 3.5; G2 cannot close until every slot has exactly one verdict -- assign a verdict to each missing slot |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a "Remediation if NO" column with a specific action] | Add a specific return-to-phase instruction to every row that lacks one |
| C-29 | Exhaustive criterion-failure remediation coverage -- every row, not just at least one | [YES/NO/PARTIAL] | [all 21 rows in this table carry a populated Remediation if NO cell] | Ensure every row has a specific, actionable remediation instruction -- no row may be empty or generic |
| C-30 | Criterion-check table presented as typed 5-column schema with dedicated "Remediation if NO" column | [YES/NO/PARTIAL] | [column header reads: Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO] | Reformat table as typed 5-column schema with "Remediation if NO" as the 5th named header column |
| C-31 | Synthesis declared as a named discrete execution phase (PHASE 3.5 SYNTHESIZE) | [YES/NO/PARTIAL] | [PHASE 3.5 -- SYNTHESIZE header present at same heading level as PHASE 3 and PHASE 4] | Add PHASE 3.5 -- SYNTHESIZE as a named section heading between PHASE 3 and PHASE 4 |
| C-32 | Synthesis phase gate G2 has formal exit condition blocking AMEND until synthesis closes | [YES/NO/PARTIAL] | [G2 OPEN/CLOSED states present + "AMEND does not begin until G2 transitions to CLOSED" statement in PHASE 3.5] | Add G2 state machine with OPEN/CLOSED labels; add explicit "AMEND does not begin until G2 transitions to CLOSED" blocking statement |

Execute all NO instructions before writing the final matrix.
PARTIAL: note the gap in the Evidence cell and proceed.

---

### PHASE 5 -- RENDER

**Entry**: PHASE 4 verification complete

**R1** Header:

```
Crew Review: [artifact name or type]
Depth: standard | deep
Slots: [list slot numbers and roles]
Roles: [list in slot order]
Inertia competitor: [status-quo alternative named in PHASE 2 SLOT-A]
```

**R2** Review matrix (6 columns, rows in slot order):

| Slot | Role | Lens | Findings | Severity | Recommendation |
|------|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s) from PHASE 2
2. Slot-gap escalation rows (1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

**R3** Cross-role synthesis (render from PHASE 3.5 G2-verified output):

Copy the synthesis verdicts produced in PHASE 3.5 S1-S2. Slot 1 verdict appears first and
names the inertia relationship. Remaining slots follow in slot-number order:
- `Slot 1 [verdict]: [inertia relationship to domain findings].`
- `Slot [N] [verdict]: [shared concern / tension / unique finding].`

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-04

**Axis**: Lifecycle + Output format (two-axis)
**Hypothesis**: V-01 R11 declares synthesis per-slot contract in the AMEND output contract
section ("AMEND does not begin until PHASE 3.5 G2 transitions to CLOSED"). V-02 R11 moves
synthesis to a typed 3-column schema. Merging both creates three independent enforcement
paths for C-27: (1) schema section AMEND contract, (2) PHASE 3.5 G2 predicate and gate,
(3) synthesis typed table completeness check at G2 closure. This is the dual-location
pattern from V-04 R10 extended to a triple-location pattern. The synthesis typed schema
(from V-02) also provides a second typed schema alongside the review matrix, strengthening
C-25/C-30 evidence (typed column discipline applied to synthesis output). Predicted:
172.5/172.5. Variation-specific signal: triple-location synthesis enforcement as a potential
structural design principle.

---

You are running `/crew-review`.

This skill executes in six lifecycle phases. Two typed schemas govern output: the 6-column
review matrix schema and the 3-column synthesis schema. Both are declared before execution.
The synthesis contract is binding in all three locations where it appears: the schema
declaration, the PHASE 3.5 G2 predicate, and the synthesis table completeness check.
PHASE 4 validates the draft matrix before final render.

---

### Output schemas (declared before execution)

**Review matrix schema** -- 6-column typed table. All column contracts are binding. The
per-row validation gate in PHASE 4 enforces every cell against these contracts.

| Column | Type -- valid | Anti-pattern excluded |
|--------|--------------|----------------------|
| Slot | integer or sub-lettered integer -- Slot 1 = challenger bracket; 1a/1b/1c/1d = slot-gap escalation rows in slot-letter order; 2, 3, ... = domain roles in manifest order | NOT: absent Slot cells; NOT: non-integer labels; NOT: Slot values that conflict with the manifest |
| Role | string -- filename stem from `.roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not present in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern traceable to this role's `lens.verify`]." | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns not traceable to this role's `lens.verify` field; NOT: multi-sentence declarations; NOT: absent Lens cells; NOT: Lens cells that merely restate the role name |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: observations naming only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

**Synthesis schema** -- 3-column typed table produced in PHASE 3.5. This contract is binding
in both this schema declaration and in PHASE 3.5 S1. Every manifest slot receives exactly
one row. G2 closure verifies row count equals slot count.

| Column | Type -- valid | Anti-pattern excluded |
|--------|--------------|----------------------|
| Slot | integer or slot-letter -- must match manifest slot number exactly | NOT: absent Slot cells; NOT: slot numbers not in manifest; NOT: merged or grouped entries ("Slots 2-3") |
| Verdict Type | enum -- exactly `converged`, `conflicted`, or `unique` | NOT: freestyle labels; NOT: absent cells; NOT: combinations |
| Statement | string -- `Slot [N] converged with Slot [M]: both find [shared concern].` OR `Slot [N] conflicts with Slot [M]: [tension description].` OR `Slot [N] is unique: [finding not overlapping with any other slot].` | NOT: statements that do not reference slot numbers; NOT: generic observations without a named finding |

**AMEND output contract**: options targeting specific findings MUST use slot numbers.
`--amend rerun:slot[N]`, `--amend add:slot[N+1]:[role-name]`.
AMEND does not begin until PHASE 3.5 G2 transitions to CLOSED. The synthesis schema
contract is binding: every slot must have a synthesis table row before AMEND is available.

---

### Slot manifest (declare before PHASE 1)

Before any phase executes, write and commit the slot manifest:

```
Slot manifest -- crew-review
Depth: [standard | deep]
Artifact type: [inferred from artifact]

Slot 1:  [challenger-role-name] (archetype: challenger)
Slot 2:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
Slot 3:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
...
```

Rules: Slot 1 = all roles with `archetype: challenger`. Slots 2-N (standard) = 2-3
non-challenger roles ranked by `expertise.relevance` to artifact type. Slots 2-N (deep) =
all non-challenger roles ranked by relevance then alphabetical. Manifest is locked. Roles
absent from manifest may not appear in the matrix. Roles in the manifest may not be skipped.

---

### PHASE 1 -- LOAD

**Entry**: slot manifest committed
**Exit**: role pool locked and verified

**L1** Open `.roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .roles/ not found.` Halt.
  - Directory empty: `ERROR: .roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked)
**Gate G1** -- challenger bracket gate

**G1 state: OPEN.** Domain review is blocked.

**G1 closure predicate** -- G1 transitions from OPEN to CLOSED when ALL hold:
1. All Slot 1 roles have run.
2. The null hypothesis 4-slot form has been attempted for each Slot 1 role.
3. For every slot that could not be filled: a dedicated, separate 6-column matrix row exists
   in the draft output, validated against the review matrix schema above, Severity = HIGH.
4. No unfilled slot was silently omitted, collapsed into another slot, or approximated with
   a generic placeholder ("some cost", "the existing workflow", "the current process").

**Domain review does not begin until G1 transitions to CLOSED.**

---

**C1** Identify all Slot 1 roles (all roles with `archetype: challenger`).

**C2** For each Slot 1 role, fill the null hypothesis 4-slot form:

```
SLOT-A: We currently do [______] instead of building this.
SLOT-B: The cost of that alternative is [______].
SLOT-C: The switching cost to adopt this artifact is [______].
SLOT-D: This artifact is worth acting on only if [______].
```

**C3** Fill each slot from artifact content or inferable workspace context.

**C4** Slot-to-row escalation rule -- mandatory, applies to each slot individually:

When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position in the 4-slot form.
2. Produce a **separate, dedicated matrix row** -- a full 6-column row following the review
   matrix schema:
   - Slot: `1[letter]` (1a for SLOT-A gap, 1b for SLOT-B gap, etc.)
   - Role: `[challenger-role-name]`
   - Lens: "As a [role], I care about null hypothesis completeness -- SLOT-[letter] is
     missing from the artifact."
   - Findings: "SLOT-[letter] gap: [slot label] not stated in the artifact. Null hypothesis
     is incomplete without this field."
   - Severity: HIGH
   - Recommendation: "State [slot requirement] explicitly in [artifact section] before
     this artifact proceeds to domain review."
3. **Do not embed this finding as a sentence within the challenger row's Findings cell.**
   A sentence inside another row's Findings cell is not a dedicated row. A dedicated row
   is a full 6-column entry in the matrix. Anything else does not satisfy G1 closure
   condition 3.
4. **Do not append this as a note or comment below the challenger row.** An appended note
   is not a matrix row. It does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled slots = two separate rows.
6. Apply per-row validation gate (PHASE 4 contract) before writing this row.

**C5** Challenger primary row:
- Slot: 1
- Lens: "As a [role], I care about [specific concern from this role's `lens.verify`]."
- Findings: the filled/attempted 4-slot form plus the challenger's primary concern.
- Severity: HIGH (inertia credible, unaddressed) / MEDIUM (named, cost unstated) /
  LOW (artifact directly neutralizes status quo).
- Recommendation: one concrete action naming what to do and where.
- Apply per-row validation gate before writing.

**C6** Verify G1 closure predicate. All 4 conditions true?

Write: `[G1: CLOSED -- conditions 1-4 verified]`

**G1 state: CLOSED.** Proceed to PHASE 3.

---

### PHASE 3 -- REVIEW

**Entry**: G1 is CLOSED (PHASE 2 exit)

**D1** Depth selection:
- Standard (default): from non-Slot-1 roles, select those whose `expertise.relevance`
  intersects the artifact type. Target 2-4. Document each: "[role]: selected because [reason]."
- `--depth deep`: all non-Slot-1 roles per manifest.

**D2** Execute each slot in manifest order. For each slot:
1. Lens cell: "As a [role], I care about [specific concern from this role's `lens.verify`]."
   Check against Lens column anti-pattern exclusion. Not a generic restatement.
2. Findings cell: name a specific artifact surface. No abstract observations. No repeating
   a finding already raised by a lower-numbered slot.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where in the artifact.

Collect all rows into draft matrix. Do not write final output -- PHASE 3.5 synthesizes first.

---

### PHASE 3.5 -- SYNTHESIZE

**Entry**: PHASE 3 exit (all domain rows collected)
**Gate G2** -- synthesis gate

**G2 state: OPEN.** AMEND is blocked.

**G2 closure predicate** -- G2 transitions from OPEN to CLOSED when ALL hold:
1. The synthesis table contains exactly one row for every slot in the manifest, including
   slot-gap escalation rows 1a/1b/1c/1d.
2. Every synthesis table row's Verdict Type is exactly `converged`, `conflicted`, or `unique`.
3. Every synthesis table row's Statement follows the synthesis schema format and references
   slot numbers.
4. No slot appears more than once in the synthesis table.

**AMEND does not begin until G2 transitions to CLOSED.**

---

**S1** For every slot in the manifest (Slot 1 through Slot N, including any slot-gap
escalation rows), produce one row in the synthesis table following the synthesis schema
declared above:

| Slot | Verdict Type | Statement |
|------|-------------|-----------|
| [N] | [converged / conflicted / unique] | [slot-numbered statement] |

**S2** Check G2 predicate. Synthesis table row count equals manifest slot count? All rows
conform to synthesis schema?

Write: `[G2: CLOSED -- [N] manifest slots, [N] synthesis table rows; all verdict types and
statements valid against synthesis schema]`

**G2 state: CLOSED.** Proceed to PHASE 4.

---

### PHASE 4 -- VALIDATE

**Entry**: G2 is CLOSED (PHASE 3.5 exit)
**Exit**: verification complete; matrix ready for PHASE 5 render

For each row in the draft matrix, verify all six cells against the review matrix schema:
- Slot: consistent with manifest; sub-lettered for slot-gap escalation rows
- Role: filename stem exists in `.roles/` at this execution
- Lens: one sentence, traceable to `lens.verify`, not a generic restatement
- Findings: names a specific artifact surface, not abstract
- Severity: exactly HIGH, MEDIUM, or LOW
- Recommendation: names what to do + where

If a cell fails: revise before writing. A row that cannot pass is removed and logged:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write the criterion-check table below before writing the final matrix. This table covers ALL
aspirational criteria through the current rubric version (v10), including C-26 through C-32
themselves. A table that stops before C-32 fails C-26 under v10. Every row carries a
"Remediation if NO" column -- execute any NO instruction before proceeding to PHASE 5:

| Criterion | Description | Status | Evidence in this draft | Remediation if NO |
|-----------|-------------|--------|------------------------|-------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] | Return to PHASE 2 C2-C4; attempt all 4 slots; escalate each unfilled slot to a dedicated matrix row |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] | Return to each row with missing or generic Lens; rewrite from this role's `lens.verify` field |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [review matrix schema present / PHASE 4 validates before write] | Add output schema table before execution; reference it in this PHASE 4 gate |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] | Rename the challenger section to "PHASE 2 -- CHALLENGE" at the same heading level as PHASE 3 |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] | Return to PHASE 2 C4; produce one dedicated HIGH-severity matrix row for each unfilled slot |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] | Add G1 OPEN/CLOSED states and "Domain review does not begin until G1 transitions to CLOSED" statement |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] | Remove any inline annotations; replace with full 6-column matrix rows at 1a/1b/1c/1d positions |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] | Add NOT: exclusions to the Lens and Findings column definitions in the review matrix schema |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] | Add explicit OPEN/CLOSED state labels and enumerate at least 2 closure conditions under the G1 predicate |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] | Add explicit "Do not embed..." and "Do not append..." prohibitions inside the escalation rule text |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present in review matrix and synthesis table / all synthesis statements use "Slot N..."] | Add Slot as the first column in both schemas; synthesis statements use "Slot [N]" in every entry |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] | Rename the validation section to "PHASE 4 -- VALIDATE" at the same heading level as PHASE 2 and PHASE 3 |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] | Move the criterion-check table inside the PHASE 4 -- VALIDATE section |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 review matrix columns + all 3 synthesis schema columns have NOT: exclusions] | Add NOT: exclusion cells to all schema columns that lack them |
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v10, including C-26 through C-32 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28, C-29, C-30, C-31, C-32 rows present in this table] | Add rows for any missing aspirational criteria including C-26 through C-32 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [G2 closed: synthesis table [N] rows for [N] manifest slots; all verdict types and statements valid] | Return to PHASE 3.5; G2 cannot close until synthesis table has one row per slot -- produce missing rows |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a "Remediation if NO" column with a specific action] | Add a specific return-to-phase instruction to every row that lacks one |
| C-29 | Exhaustive criterion-failure remediation coverage -- every row, not just at least one | [YES/NO/PARTIAL] | [all 21 rows in this table carry a populated Remediation if NO cell] | Ensure every row has a specific, actionable remediation instruction -- no row may be empty or generic |
| C-30 | Criterion-check table presented as typed 5-column schema with dedicated "Remediation if NO" column | [YES/NO/PARTIAL] | [column header reads: Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO] | Reformat table as typed 5-column schema with "Remediation if NO" as the 5th named header column |
| C-31 | Synthesis declared as a named discrete execution phase (PHASE 3.5 SYNTHESIZE) | [YES/NO/PARTIAL] | [PHASE 3.5 -- SYNTHESIZE header present at same heading level as PHASE 3 and PHASE 4] | Add PHASE 3.5 -- SYNTHESIZE as a named section heading between PHASE 3 and PHASE 4 |
| C-32 | Synthesis phase gate G2 has formal exit condition blocking AMEND until synthesis closes | [YES/NO/PARTIAL] | [G2 OPEN/CLOSED states present + "AMEND does not begin until G2 transitions to CLOSED" statement in PHASE 3.5] | Add G2 state machine with OPEN/CLOSED labels; add explicit "AMEND does not begin until G2 transitions to CLOSED" blocking statement |

Execute all NO instructions before writing the final matrix.
PARTIAL: note the gap in the Evidence cell and proceed.

---

### PHASE 5 -- RENDER

**Entry**: PHASE 4 verification complete

**R1** Header:

```
Crew Review: [artifact name or type]
Depth: standard | deep
Slots: [list slot numbers and roles]
Roles: [list in slot order]
```

**R2** Review matrix (6 columns, rows in slot order):

| Slot | Role | Lens | Findings | Severity | Recommendation |
|------|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s) from PHASE 2
2. Slot-gap escalation rows (1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

**R3** Cross-role synthesis (render from PHASE 3.5 G2-verified synthesis table):

Render the synthesis table produced in PHASE 3.5 S1. Row order: slot number ascending.

| Slot | Verdict Type | Statement |
|------|-------------|-----------|

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-05

**Axis**: Lifecycle + Output format + Role sequence (three-axis)
**Hypothesis**: V-04 R11 provides dual schema enforcement and PHASE 3.5 + G2. Adding the
verbatim `expertise.relevance` quote pattern (from V-05 R10) with L5 registry verification
creates the strongest possible selection chain: role selection is not just documented as a
reason but proven via verbatim field citation verified before execution. L5 halts on quote
mismatch, making the manifest a falsifiable selection artifact. This is a potential C-33
candidate from R10's excellence signals: "verbatim field citation as selection evidence proof."
Under v10 all 32 criteria pass; L5 strengthens C-01 and C-06 beyond requirement. Predicted:
172.5/172.5.

---

You are running `/crew-review`.

This skill executes in six lifecycle phases. Two typed schemas govern output: the 6-column
review matrix schema and the 3-column synthesis schema. Both are declared before execution.
The manifest includes verbatim `expertise.relevance` quotes from registry files for all
non-challenger slots; L5 verifies these quotes before execution proceeds. The synthesis
contract is binding in the schema declaration, in PHASE 3.5 G2, and in the synthesis table.
PHASE 4 validates the draft matrix before final render.

---

### Output schemas (declared before execution)

**Review matrix schema** -- 6-column typed table. All column contracts are binding. The
per-row validation gate in PHASE 4 enforces every cell against these contracts.

| Column | Type -- valid | Anti-pattern excluded |
|--------|--------------|----------------------|
| Slot | integer or sub-lettered integer -- Slot 1 = challenger bracket; 1a/1b/1c/1d = slot-gap escalation rows in slot-letter order; 2, 3, ... = domain roles in manifest order | NOT: absent Slot cells; NOT: non-integer labels; NOT: Slot values that conflict with the manifest |
| Role | string -- filename stem from `.roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not present in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern traceable to this role's `lens.verify`]." | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns not traceable to this role's `lens.verify` field; NOT: multi-sentence declarations; NOT: absent Lens cells; NOT: Lens cells that merely restate the role name |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: observations naming only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

**Synthesis schema** -- 3-column typed table produced in PHASE 3.5. This contract is binding
in both this schema declaration and in PHASE 3.5 S1. Every manifest slot receives exactly
one row. G2 closure verifies row count equals slot count.

| Column | Type -- valid | Anti-pattern excluded |
|--------|--------------|----------------------|
| Slot | integer or slot-letter -- must match manifest slot number exactly | NOT: absent Slot cells; NOT: slot numbers not in manifest; NOT: merged or grouped entries ("Slots 2-3") |
| Verdict Type | enum -- exactly `converged`, `conflicted`, or `unique` | NOT: freestyle labels; NOT: absent cells; NOT: combinations |
| Statement | string -- `Slot [N] converged with Slot [M]: both find [shared concern].` OR `Slot [N] conflicts with Slot [M]: [tension description].` OR `Slot [N] is unique: [finding not overlapping with any other slot].` | NOT: statements that do not reference slot numbers; NOT: generic observations without a named finding |

**AMEND output contract**: options targeting specific findings MUST use slot numbers.
`--amend rerun:slot[N]`, `--amend add:slot[N+1]:[role-name]`.
AMEND does not begin until PHASE 3.5 G2 transitions to CLOSED. The synthesis schema
contract is binding: every slot must have a synthesis table row before AMEND is available.

---

### Slot manifest (declare before PHASE 1)

Before any phase executes, write and commit the slot manifest:

```
Slot manifest -- crew-review
Depth: [standard | deep]
Artifact type: [inferred from artifact]

Slot 1:  [challenger-role-name] (archetype: challenger)
Slot 2:  [role-name] (archetype: [type]) -- expertise.relevance: "[verbatim text from
         role file's expertise.relevance field]"
Slot 3:  [role-name] (archetype: [type]) -- expertise.relevance: "[verbatim text from
         role file's expertise.relevance field]"
...
```

Rules: Slot 1 = all roles with `archetype: challenger`. For each non-challenger slot, copy
the verbatim `expertise.relevance` field value from the role file -- do not paraphrase or
summarize. Slots 2-N (standard) = 2-3 non-challenger roles ranked by `expertise.relevance`
intersection with artifact type. Slots 2-N (deep) = all non-challenger roles ranked by
relevance then alphabetical. Manifest is locked after L5 verification. Roles absent from
manifest may not appear in the matrix. Roles in the manifest may not be skipped.

---

### PHASE 1 -- LOAD

**Entry**: slot manifest committed
**Exit**: role pool locked, manifest verbatim quotes verified

**L1** Open `.roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .roles/ not found.` Halt.
  - Directory empty: `ERROR: .roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.
**L5** For each non-challenger slot in the manifest, verify the `expertise.relevance` quote
  matches the registry file exactly (character-for-character). If a quote does not match:
  `ERROR: [role-name] verbatim expertise.relevance quote mismatch -- manifest invalid. Halt.`
  Manifest is locked only after all L5 verifications pass.

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked, manifest verified)
**Gate G1** -- challenger bracket gate

**G1 state: OPEN.** Domain review is blocked.

**G1 closure predicate** -- G1 transitions from OPEN to CLOSED when ALL hold:
1. All Slot 1 roles have run.
2. The null hypothesis 4-slot form has been attempted for each Slot 1 role.
3. For every slot that could not be filled: a dedicated, separate 6-column matrix row exists
   in the draft output, validated against the review matrix schema above, Severity = HIGH.
4. No unfilled slot was silently omitted, collapsed into another slot, or approximated with
   a generic placeholder ("some cost", "the existing workflow", "the current process").

**Domain review does not begin until G1 transitions to CLOSED.**

---

**C1** Identify all Slot 1 roles (all roles with `archetype: challenger`).

**C2** For each Slot 1 role, fill the null hypothesis 4-slot form:

```
SLOT-A: We currently do [______] instead of building this.
SLOT-B: The cost of that alternative is [______].
SLOT-C: The switching cost to adopt this artifact is [______].
SLOT-D: This artifact is worth acting on only if [______].
```

**C3** Fill each slot from artifact content or inferable workspace context.

**C4** Slot-to-row escalation rule -- mandatory, applies to each slot individually:

When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position in the 4-slot form.
2. Produce a **separate, dedicated matrix row** -- a full 6-column row following the review
   matrix schema:
   - Slot: `1[letter]` (1a for SLOT-A gap, 1b for SLOT-B gap, etc.)
   - Role: `[challenger-role-name]`
   - Lens: "As a [role], I care about null hypothesis completeness -- SLOT-[letter] is
     missing from the artifact."
   - Findings: "SLOT-[letter] gap: [slot label] not stated in the artifact. Null hypothesis
     is incomplete without this field."
   - Severity: HIGH
   - Recommendation: "State [slot requirement] explicitly in [artifact section] before
     this artifact proceeds to domain review."
3. **Do not embed this finding as a sentence within the challenger row's Findings cell.**
   A sentence inside another row's Findings cell is not a dedicated row. A dedicated row
   is a full 6-column entry in the matrix. Anything else does not satisfy G1 closure
   condition 3.
4. **Do not append this as a note or comment below the challenger row.** An appended note
   is not a matrix row. It does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled slots = two separate rows.
6. Apply per-row validation gate (PHASE 4 contract) before writing this row.

**C5** Challenger primary row:
- Slot: 1
- Lens: "As a [role], I care about [specific concern from this role's `lens.verify`]."
- Findings: the filled/attempted 4-slot form plus the challenger's primary concern.
- Severity: HIGH (inertia credible, unaddressed) / MEDIUM (named, cost unstated) /
  LOW (artifact directly neutralizes status quo).
- Recommendation: one concrete action naming what to do and where.
- Apply per-row validation gate before writing.

**C6** Verify G1 closure predicate. All 4 conditions true?

Write: `[G1: CLOSED -- conditions 1-4 verified]`

**G1 state: CLOSED.** Proceed to PHASE 3.

---

### PHASE 3 -- REVIEW

**Entry**: G1 is CLOSED (PHASE 2 exit)

**D1** Depth selection:
- Standard (default): verbatim `expertise.relevance` quotes already in L5-verified manifest --
  reference manifest entries directly. Target 2-4 non-challenger roles. Non-challenger roles
  absent from manifest may not run.
- `--depth deep`: all non-Slot-1 roles per L5-verified manifest.

**D2** Execute each slot in manifest order. For each slot:
1. Lens cell: "As a [role], I care about [specific concern from this role's `lens.verify`]."
   Check against Lens column anti-pattern exclusion. Not a generic restatement.
2. Findings cell: name a specific artifact surface. No abstract observations. No repeating
   a finding already raised by a lower-numbered slot.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where in the artifact.

Collect all rows into draft matrix. Do not write final output -- PHASE 3.5 synthesizes first.

---

### PHASE 3.5 -- SYNTHESIZE

**Entry**: PHASE 3 exit (all domain rows collected)
**Gate G2** -- synthesis gate

**G2 state: OPEN.** AMEND is blocked.

**G2 closure predicate** -- G2 transitions from OPEN to CLOSED when ALL hold:
1. The synthesis table contains exactly one row for every slot in the manifest, including
   slot-gap escalation rows 1a/1b/1c/1d.
2. Every synthesis table row's Verdict Type is exactly `converged`, `conflicted`, or `unique`.
3. Every synthesis table row's Statement follows the synthesis schema format and references
   slot numbers.
4. No slot appears more than once in the synthesis table.

**AMEND does not begin until G2 transitions to CLOSED.**

---

**S1** For every slot in the manifest (Slot 1 through Slot N, including any slot-gap
escalation rows), produce one row in the synthesis table following the synthesis schema:

| Slot | Verdict Type | Statement |
|------|-------------|-----------|
| [N] | [converged / conflicted / unique] | [slot-numbered statement] |

**S2** Check G2 predicate. Synthesis table row count equals manifest slot count? All rows
conform to synthesis schema?

Write: `[G2: CLOSED -- [N] manifest slots, [N] synthesis table rows; all rows valid against
synthesis schema; L5-verified manifest used]`

**G2 state: CLOSED.** Proceed to PHASE 4.

---

### PHASE 4 -- VALIDATE

**Entry**: G2 is CLOSED (PHASE 3.5 exit)
**Exit**: verification complete; matrix ready for PHASE 5 render

For each row in the draft matrix, verify all six cells against the review matrix schema:
- Slot: consistent with manifest; sub-lettered for slot-gap escalation rows
- Role: filename stem exists in `.roles/` at this execution
- Lens: one sentence, traceable to `lens.verify`, not a generic restatement
- Findings: names a specific artifact surface, not abstract
- Severity: exactly HIGH, MEDIUM, or LOW
- Recommendation: names what to do + where

If a cell fails: revise before writing. A row that cannot pass is removed and logged:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write the criterion-check table below before writing the final matrix. This table covers ALL
aspirational criteria through the current rubric version (v10), including C-26 through C-32
themselves. A table that stops before C-32 fails C-26 under v10. Every row carries a
"Remediation if NO" column -- execute any NO instruction before proceeding to PHASE 5:

| Criterion | Description | Status | Evidence in this draft | Remediation if NO |
|-----------|-------------|--------|------------------------|-------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] | Return to PHASE 2 C2-C4; attempt all 4 slots; escalate each unfilled slot to a dedicated matrix row |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] | Return to each row with missing or generic Lens; rewrite from this role's `lens.verify` field |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [review matrix schema present / PHASE 4 validates before write] | Add output schema table before execution; reference it in this PHASE 4 gate |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] | Rename the challenger section to "PHASE 2 -- CHALLENGE" at the same heading level as PHASE 3 |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] | Return to PHASE 2 C4; produce one dedicated HIGH-severity matrix row for each unfilled slot |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] | Add G1 OPEN/CLOSED states and "Domain review does not begin until G1 transitions to CLOSED" statement |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] | Remove any inline annotations; replace with full 6-column matrix rows at 1a/1b/1c/1d positions |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] | Add NOT: exclusions to the Lens and Findings column definitions in the review matrix schema |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] | Add explicit OPEN/CLOSED state labels and enumerate at least 2 closure conditions under the G1 predicate |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] | Add explicit "Do not embed..." and "Do not append..." prohibitions inside the escalation rule text |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present in review matrix and synthesis table / all synthesis statements use "Slot N..."] | Add Slot as the first column in both schemas; synthesis statements use "Slot [N]" in every entry |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] | Rename the validation section to "PHASE 4 -- VALIDATE" at the same heading level as PHASE 2 and PHASE 3 |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] | Move the criterion-check table inside the PHASE 4 -- VALIDATE section |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 review matrix columns + all 3 synthesis schema columns have NOT: exclusions] | Add NOT: exclusion cells to all schema columns that lack them |
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v10, including C-26 through C-32 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28, C-29, C-30, C-31, C-32 rows present in this table] | Add rows for any missing aspirational criteria including C-26 through C-32 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [G2 closed: synthesis table [N] rows for [N] manifest slots; all rows valid against synthesis schema] | Return to PHASE 3.5; G2 cannot close until synthesis table has one row per slot -- produce missing rows |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a "Remediation if NO" column with a specific action] | Add a specific return-to-phase instruction to every row that lacks one |
| C-29 | Exhaustive criterion-failure remediation coverage -- every row, not just at least one | [YES/NO/PARTIAL] | [all 21 rows in this table carry a populated Remediation if NO cell] | Ensure every row has a specific, actionable remediation instruction -- no row may be empty or generic |
| C-30 | Criterion-check table presented as typed 5-column schema with dedicated "Remediation if NO" column | [YES/NO/PARTIAL] | [column header reads: Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO] | Reformat table as typed 5-column schema with "Remediation if NO" as the 5th named header column |
| C-31 | Synthesis declared as a named discrete execution phase (PHASE 3.5 SYNTHESIZE) | [YES/NO/PARTIAL] | [PHASE 3.5 -- SYNTHESIZE header present at same heading level as PHASE 3 and PHASE 4] | Add PHASE 3.5 -- SYNTHESIZE as a named section heading between PHASE 3 and PHASE 4 |
| C-32 | Synthesis phase gate G2 has formal exit condition blocking AMEND until synthesis closes | [YES/NO/PARTIAL] | [G2 OPEN/CLOSED states present + "AMEND does not begin until G2 transitions to CLOSED" statement in PHASE 3.5] | Add G2 state machine with OPEN/CLOSED labels; add explicit "AMEND does not begin until G2 transitions to CLOSED" blocking statement |

Execute all NO instructions before writing the final matrix.
PARTIAL: note the gap in the Evidence cell and proceed.

---

### PHASE 5 -- RENDER

**Entry**: PHASE 4 verification complete

**R1** Header:

```
Crew Review: [artifact name or type]
Depth: standard | deep
Slots: [list slot numbers and roles]
Roles: [list in slot order with verbatim expertise.relevance quotes]
```

**R2** Review matrix (6 columns, rows in slot order):

| Slot | Role | Lens | Findings | Severity | Recommendation |
|------|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s) from PHASE 2
2. Slot-gap escalation rows (1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

**R3** Cross-role synthesis (render from PHASE 3.5 G2-verified synthesis table):

Render the synthesis table produced in PHASE 3.5 S1. Row order: slot number ascending.

| Slot | Verdict Type | Statement |
|------|-------------|-----------|

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## Predicted Scores (v10 rubric)

| Variation | Axis | Essential | Recommended | Aspirational | Total | Golden? |
|-----------|------|-----------|-------------|--------------|-------|---------|
| V-01 | Lifecycle (PHASE 3.5 + G2 direct) | 60/60 | 60/60 | 52.5/52.5 | **172.5** | YES |
| V-02 | Output format (synthesis typed schema) | 60/60 | 60/60 | 52.5/52.5 | **172.5** | YES |
| V-03 | Inertia framing (Slot 1 synthesis explicit) | 60/60 | 60/60 | 52.5/52.5 | **172.5** | YES |
| V-04 | Lifecycle + Output format | 60/60 | 60/60 | 52.5/52.5 | **172.5** | YES |
| V-05 | Three-axis (+ verbatim quotes + L5) | 60/60 | 60/60 | 52.5/52.5 | **172.5** | YES |

**Key C-31/C-32 evidence by variation:**

| Variation | C-31 evidence | C-32 evidence |
|-----------|--------------|---------------|
| V-01 | PHASE 3.5 -- SYNTHESIZE header between PHASE 3 and PHASE 4 | G2 OPEN/CLOSED + "AMEND does not begin until G2 transitions to CLOSED" |
| V-02 | PHASE 3.5 -- SYNTHESIZE header; synthesis schema declared at same level | G2 closure checks synthesis table row count; AMEND blocked |
| V-03 | PHASE 3.5 -- SYNTHESIZE with Slot 1 inertia requirement | G2 OPEN/CLOSED + AMEND blocked; Slot 1 inertia verdict required for closure |
| V-04 | PHASE 3.5 -- SYNTHESIZE; synthesis contract in three locations | G2 OPEN/CLOSED + AMEND blocked; synthesis schema contract binds AMEND |
| V-05 | PHASE 3.5 -- SYNTHESIZE; L5-verified manifest used in synthesis | G2 OPEN/CLOSED + AMEND blocked; L5 verification is prerequisite for the synthesis manifest |

**Critical design fix from R10**: V-03 R10 said "PHASE 4 does not begin until G2 transitions
to CLOSED." The C-32 criterion mirrors C-17: G1 blocks domain review (PHASE 3), so G2 must
block AMEND (the post-render command interface), not PHASE 4. All R11 variations use the
correct downstream target: "AMEND does not begin until G2 transitions to CLOSED."

---

## Excellence Signals

Patterns from R11 that extend the R10 excellence signals:

**Pattern 6: G2 downstream target correction** (all R11 variations)
The correct parallel chain is G1 blocks PHASE 3 (domain review) / G2 blocks AMEND (amendment
commands). V-03 R10's G2 blocked PHASE 4 (validation), which was the wrong target -- it
blocked the next phase rather than the post-render command interface. C-32 is explicit:
"blocks AMEND until synthesis closes." R11 corrects this in all five variations. This is not
a new criterion; it is the correct implementation of C-32 that R10 only partially achieved.

**Pattern 7: Typed synthesis schema parallel to review matrix schema** (V-02, V-04, V-05)
The review matrix has a typed 6-column schema. Applying the same typed schema discipline to
synthesis output (3 columns: Slot | Verdict Type | Statement) produces a second schema
artifact governed by the same correctness-by-construction principle as C-30. G2 closure
verifies synthesis table completeness against manifest slot count -- a table-level predicate
rather than a prose verification. Potential C-33 candidate: typed schema discipline applied
to every phase output that produces a structured artifact.

**Pattern 8: Inertia node as synthesis anchor** (V-03 only)
The challenger bracket (PHASE 2) identifies the inertia competitor. V-03's PHASE 3.5
requires Slot 1's synthesis verdict to explicitly name the inertia competitor's relationship
to domain findings. Synthesis is not just cross-slot signal aggregation; it is
inertia-resolution. Potential C-33 candidate: synthesis verdict for Slot 1 must name
inertia implications for domain slots (not just "unique" without naming the inertia dimension).

**Pattern 9: Triple-location synthesis enforcement** (V-04, V-05)
V-04 R10 had dual-location synthesis obligation (schema section + R3 text). V-04 R11 has
three independent enforcement locations: (1) AMEND output contract in schema section,
(2) PHASE 3.5 G2 predicate and gate, (3) synthesis typed table completeness check at G2
closure. No execution path reaches AMEND without encountering the synthesis obligation.
This is the "exhaustive enforcement path coverage" principle generalized: from C-25
(exhaustive anti-pattern coverage) to C-29 (exhaustive remediation coverage) to here
(exhaustive synthesis enforcement path coverage).

**Pattern 10: Verbatim field citation in synthesis manifest** (V-05 only)
V-05's L5 verification extends from manifest to synthesis: the G2 closure note references
"L5-verified manifest used." The selection chain (verbatim quote -> L5 verification ->
G2-verified synthesis) creates an end-to-end provenance chain from registry file to final
synthesis verdict. This is the strongest possible C-01/C-06 evidence: role selection is
not paraphrased but cited, not recalled but verified.

---

```json
{"top_score_predicted": 172.5, "all_essential_pass": true, "critical_fix": "G2 downstream target corrected from PHASE 4 to AMEND -- C-32 requires AMEND blocking not VALIDATE blocking", "new_patterns": ["G2 downstream target correction: AMEND not VALIDATE (C-32 literal requirement)", "typed synthesis schema parallel to review matrix schema -- schema discipline applied to every structured phase output", "Slot 1 inertia as required synthesis anchor -- synthesis verdict for challenger slot must name inertia implications", "triple-location synthesis enforcement: schema AMEND contract + G2 predicate + synthesis table row count check", "verbatim field citation in synthesis manifest with L5 provenance chain from registry to synthesis verdict"]}
```
