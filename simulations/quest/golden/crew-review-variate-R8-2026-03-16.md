---
skill: quest-variate
skill_target: crew-review
date: 2026-03-16
round: 8
rubric: crew-review-rubric-v7-2026-03-16.md
---

# crew-review -- Variate R8

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis combinations (V-04, V-05).

**R8 design target**: R7 V-05 achieved a perfect 155.0 score under rubric v7. The two
newest criteria -- C-24 (criterion-check table in VALIDATE phase) and C-25 (anti-patterns
on every schema column) -- were both satisfied simultaneously for the first time. However,
the criterion-check table in V-05 R7 covers C-11 through C-23. C-24 and C-25 are not in
the table -- they postdate the table's design. This creates a meta-completeness gap: the
validator does not verify the two newest criteria it was written to satisfy. R8 targets
three new excellence patterns:

- V-01: Criterion-check self-inclusion (single axis) -- extends the VALIDATE phase
  criterion-check table to include C-24 and C-25 as explicit rows. The table now verifies
  every aspirational criterion through the current rubric version, including the two
  criteria that govern the table itself. Hypothesis: a criterion-check table that stops at
  C-23 passes C-24 but misses a deeper meta-completeness property -- a table that includes
  C-24 and C-25 is self-verifying and achieves rubric-version completeness.

- V-02: Per-slot synthesis coverage contract (single axis) -- changes the R3 synthesis
  requirement from "name at least one convergence or conflict" to per-slot mandatory
  verdict: every slot must appear in synthesis with an explicit convergence, conflict, or
  unique verdict. Hypothesis: the current synthesis contract allows technically-passing but
  thin synthesis (one convergence stated, all other slots silent). A per-slot coverage
  contract forces exhaustive cross-role analysis and surfaces a new rubric pattern:
  synthesis completeness as a slot-anchored obligation, not a minimum-count requirement.

- V-03: Role selection evidence chain with verbatim field quotes (single axis) -- changes
  the manifest "selected because [reason]" prose to a typed selection contract: each
  non-challenger slot entry must include a verbatim quote of that role's
  `expertise.relevance` field from the registry file. Hypothesis: prose selection
  justification is unverifiable and role-independent. A verbatim field quote creates a
  traceable selection chain tied directly to the role file's own definition of relevance,
  making fabricated or recalled selections falsifiable.

**R8 single-axis targets (C-26, C-27, C-28 candidates):**
- V-01 -> C-26: Criterion-check table covers ALL aspirational criteria through the current
  rubric version (self-complete coverage, including criteria about the table itself).
- V-02 -> C-27: Synthesis provides per-slot convergence/conflict/unique verdict for every
  slot in the manifest -- exhaustive slot-anchored synthesis.
- V-03 -> C-28: Role selection justification in the slot manifest includes verbatim
  `expertise.relevance` quote from the registry file for each non-challenger slot.

---

## V-01

**Axis**: Lifecycle emphasis -- criterion-check self-inclusion
**Hypothesis**: V-05 R7's criterion-check table covers C-11 through C-23. Under rubric v7,
C-24 and C-25 are aspirational criteria that the table is designed to satisfy but does not
explicitly verify. A criterion-check table that includes rows for C-24 and C-25 achieves
rubric-version completeness: the table verifies every aspirational criterion, including the
two criteria that define what the table itself must contain. This is the minimal change to
V-05 R7 that closes the meta-completeness gap.

---

You are running `/crew-review`.

This skill executes in five lifecycle phases. The output schema -- including a Slot column
and a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. PHASE 4 validates the draft matrix before final render.

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

**Synthesis output contract**: synthesis MUST reference slot numbers when naming convergences
or conflicts. "Slot [N] and Slot [M] both find..." Role-name-only references do not satisfy
this contract.

**AMEND output contract**: options targeting specific findings MUST use slot numbers.
`--amend rerun:slot[N]`, `--amend add:slot[N+1]:[role-name]`.

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

Collect all rows into draft matrix. Do not write final output -- PHASE 4 validates first.

---

### PHASE 4 -- VALIDATE

**Entry**: all rows collected (PHASE 3 exit)
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

Write a criterion-check table before writing the final matrix:

| Criterion | Description | Status | Evidence in this draft |
|-----------|-------------|--------|------------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N and Slot M..."] |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions in schema table] |

If any designed-to-satisfy criterion scores NO: return to the relevant phase and revise.
PARTIAL: note the gap and proceed.

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

**R3** Cross-role synthesis (required -- must satisfy synthesis output contract):
Reference slot numbers. "Slot [N] and Slot [M] both find [shared concern]." Name at least
one convergence or conflict. Slot-gap rows count as findings for convergence detection. If
absent: `No cross-role signal detected -- findings are non-overlapping.`

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-02

**Axis**: Output format -- per-slot synthesis coverage contract
**Hypothesis**: The current synthesis contract (R3: "name at least one convergence or
conflict") allows technically-passing but thin synthesis. A single convergence stated once
satisfies the contract, leaving all other slots unaddressed. A per-slot synthesis coverage
contract changes the obligation from minimum-count to exhaustive slot-anchored verdicts:
every slot in the manifest must appear in synthesis with a declared outcome (converged,
conflicted, or unique). This produces richer cross-role analysis and surfaces a new rubric
pattern: synthesis completeness as a slot-coverage property, not a count property.

---

You are running `/crew-review`.

This skill executes in five lifecycle phases. The output schema -- including a Slot column
and a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. PHASE 4 validates the draft matrix before final render.

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

**Synthesis output contract -- per-slot coverage (replaces minimum-count contract)**:
Synthesis MUST reference slot numbers. For every slot in the manifest (including
slot-gap escalation rows), state one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict. A synthesis that names one convergence and leaves other
slots unaddressed does not satisfy this contract. Slot-gap escalation rows (1a, 1b, ...)
count as addressable slots.

**AMEND output contract**: options targeting specific findings MUST use slot numbers.
`--amend rerun:slot[N]`, `--amend add:slot[N+1]:[role-name]`.

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

Collect all rows into draft matrix. Do not write final output -- PHASE 4 validates first.

---

### PHASE 4 -- VALIDATE

**Entry**: all rows collected (PHASE 3 exit)
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

Write a criterion-check table before writing the final matrix:

| Criterion | Description | Status | Evidence in this draft |
|-----------|-------------|--------|------------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N and Slot M..."] |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions in schema table] |

If any designed-to-satisfy criterion scores NO: return to the relevant phase and revise.
PARTIAL: note the gap and proceed.

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

**R3** Cross-role synthesis -- per-slot coverage (required):
For every slot in the manifest (including slot-gap escalation rows), state exactly one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict before synthesis is complete. Slot-gap escalation rows
(1a, 1b, ...) are addressable slots. A synthesis that names one convergence and leaves
other slots without a verdict does not satisfy this contract.

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-03

**Axis**: Role sequence -- role selection evidence chain with verbatim field quotes
**Hypothesis**: The current slot manifest requires "selected because [reason tied to
artifact]" -- unverifiable prose that could be fabricated or recalled from memory. A typed
selection contract requiring verbatim `expertise.relevance` field quotes from the registry
file creates a falsifiable selection chain: if the quoted value is not present in the role
file, the selection is invalid. This mirrors the registry's own definition of relevance
rather than the executor's paraphrase of it. The hypothesis is that verbatim field quoting
produces a traceable, verifiable selection mechanism that surfaces a new rubric pattern:
role selection grounded in evidence from the registry file itself, not from the executor's
interpretation of it.

---

You are running `/crew-review`.

This skill executes in five lifecycle phases. The output schema -- including a Slot column
and a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. PHASE 4 validates the draft matrix before final render.

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

**Synthesis output contract**: synthesis MUST reference slot numbers when naming convergences
or conflicts. "Slot [N] and Slot [M] both find..." Role-name-only references do not satisfy
this contract.

**AMEND output contract**: options targeting specific findings MUST use slot numbers.
`--amend rerun:slot[N]`, `--amend add:slot[N+1]:[role-name]`.

---

### Slot manifest (declare before PHASE 1)

Before any phase executes, write and commit the slot manifest. Non-challenger slot entries
MUST include a verbatim `expertise.relevance` quote from the role's registry file --
not a paraphrase, not a summary, not a recalled description:

```
Slot manifest -- crew-review
Depth: [standard | deep]
Artifact type: [inferred from artifact]

Slot 1:  [challenger-role-name] (archetype: challenger)
Slot 2:  [role-name] (archetype: [type])
         expertise.relevance (verbatim): "[exact text from [role-name].md expertise.relevance field]"
         selected because: [1-sentence mapping from verbatim quote to artifact type]
Slot 3:  [role-name] (archetype: [type])
         expertise.relevance (verbatim): "[exact text from [role-name].md expertise.relevance field]"
         selected because: [1-sentence mapping from verbatim quote to artifact type]
...
```

**Selection validation rule**: A non-challenger slot entry that does not include a verbatim
`expertise.relevance` quote is invalid. The manifest may not be committed until all
non-challenger entries carry verbatim quotes. A "selected because" sentence without the
verbatim quote does not satisfy this contract.

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
**L5** Verify manifest selection evidence: for each non-challenger slot, confirm the
  verbatim `expertise.relevance` quote matches the text in the role file. If a quote
  does not match: `ERROR: [role-name] verbatim quote mismatch -- manifest invalid.` Halt.

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked and manifest verified)
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
  intersects the artifact type. Target 2-4. Verbatim `expertise.relevance` already in
  manifest -- reference manifest entry rather than re-selecting.
- `--depth deep`: all non-Slot-1 roles per manifest.

**D2** Execute each slot in manifest order. For each slot:
1. Lens cell: "As a [role], I care about [specific concern from this role's `lens.verify`]."
   Check against Lens column anti-pattern exclusion. Not a generic restatement.
2. Findings cell: name a specific artifact surface. No abstract observations. No repeating
   a finding already raised by a lower-numbered slot.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where in the artifact.

Collect all rows into draft matrix. Do not write final output -- PHASE 4 validates first.

---

### PHASE 4 -- VALIDATE

**Entry**: all rows collected (PHASE 3 exit)
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

Write a criterion-check table before writing the final matrix:

| Criterion | Description | Status | Evidence in this draft |
|-----------|-------------|--------|------------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N and Slot M..."] |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions in schema table] |

If any designed-to-satisfy criterion scores NO: return to the relevant phase and revise.
PARTIAL: note the gap and proceed.

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

**R3** Cross-role synthesis (required -- must satisfy synthesis output contract):
Reference slot numbers. "Slot [N] and Slot [M] both find [shared concern]." Name at least
one convergence or conflict. Slot-gap rows count as findings for convergence detection. If
absent: `No cross-role signal detected -- findings are non-overlapping.`

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-04

**Axes**: Lifecycle emphasis + Output format (criterion-check self-inclusion + per-slot
synthesis coverage contract)
**Hypothesis**: V-01 closes the meta-completeness gap in the criterion-check table by
adding C-24 and C-25 as explicit rows. V-02 changes synthesis from minimum-count to
per-slot exhaustive coverage. These two changes are structurally independent: C-24/C-25 are
properties of PHASE 4; per-slot synthesis is a property of PHASE 5 R3. The hypothesis is
that combining them introduces no interference and produces two simultaneously-satisfied
new patterns: a self-complete criterion-check table AND an exhaustive slot-anchored synthesis.

---

You are running `/crew-review`.

This skill executes in five lifecycle phases. The output schema -- including a Slot column
and a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. PHASE 4 validates the draft matrix before final render.

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

**Synthesis output contract -- per-slot coverage**:
Synthesis MUST reference slot numbers. For every slot in the manifest (including
slot-gap escalation rows), state one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict. A synthesis that names one convergence and leaves other
slots unaddressed does not satisfy this contract.

**AMEND output contract**: options targeting specific findings MUST use slot numbers.
`--amend rerun:slot[N]`, `--amend add:slot[N+1]:[role-name]`.

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

Collect all rows into draft matrix. Do not write final output -- PHASE 4 validates first.

---

### PHASE 4 -- VALIDATE

**Entry**: all rows collected (PHASE 3 exit)
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

Write a criterion-check table before writing the final matrix. This table covers ALL
aspirational criteria through the current rubric version (v7), including C-24 and C-25:

| Criterion | Description | Status | Evidence in this draft |
|-----------|-------------|--------|------------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N and Slot M..."] |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions in schema table] |

If any designed-to-satisfy criterion scores NO: return to the relevant phase and revise.
PARTIAL: note the gap and proceed.

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

**R3** Cross-role synthesis -- per-slot coverage (required):
For every slot in the manifest (including slot-gap escalation rows), state exactly one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict before synthesis is complete. Slot-gap escalation rows
(1a, 1b, ...) are addressable slots. A synthesis that names one convergence and leaves
other slots without a verdict does not satisfy this contract.

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-05

**Axes**: Lifecycle emphasis + Output format + Role sequence + Phrasing register
(criterion-check self-inclusion + per-slot synthesis + verbatim selection evidence chain
+ severity calibration protocol -- maximal combination)
**Hypothesis**: Three structural patterns from R8 single-axis variations (V-01, V-02, V-03)
target independent components of the skill: V-01 targets PHASE 4 meta-completeness, V-02
targets PHASE 5 synthesis coverage, V-03 targets pre-PHASE-1 manifest evidence. A fourth
new pattern -- severity calibration protocol -- adds a pre-execution severity contract that
maps finding type to expected severity range before any row is written. This is analogous
to how the output schema declares column contracts before execution: severity calibration
declares the interpretive contract for severity before assignment begins. The four patterns
are structurally independent and hypothesized to be additive: all four can coexist in one
variation without interference, and their combination reveals a new excellence pattern --
C-29 candidate: pre-execution severity calibration grounds HIGH/MEDIUM/LOW in an explicit
artifact-type-aware classification, not in per-row ad-hoc judgment.

---

You are running `/crew-review`.

This skill executes in five lifecycle phases. The output schema -- including a Slot column
and a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. A severity calibration protocol grounds severity assignments before
any phase executes. PHASE 4 validates the draft matrix before final render.

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
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory; assignments are grounded in the severity calibration protocol declared below | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM"); NOT: severity assignments that contradict the calibration protocol without stated exception |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

**Synthesis output contract -- per-slot coverage**:
Synthesis MUST reference slot numbers. For every slot in the manifest (including
slot-gap escalation rows), state one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict.

**AMEND output contract**: options targeting specific findings MUST use slot numbers.
`--amend rerun:slot[N]`, `--amend add:slot[N+1]:[role-name]`.

---

### Severity calibration protocol (declared before execution)

Before any phase executes, the severity calibration grounds severity assignment in
artifact-type-aware rules. The calibration is not a post-hoc label -- it is a pre-execution
classification contract that severity assignments in all phases must follow.

**Default calibration (overridden by artifact-type-specific rules below):**

| Condition | Default severity |
|-----------|-----------------|
| Finding blocks a commitment decision -- artifact cannot be used as-is | HIGH |
| Finding requires a specific action before artifact is usable | MEDIUM |
| Finding improves quality but does not block or condition use | LOW |

**Artifact-type-specific calibration overrides** (apply when artifact type is identified):
- Specification: missing required sections = HIGH; ambiguous non-key terms = LOW
- Proposal: missing option count (fewer than 3 options) = HIGH; missing recommendation rationale = MEDIUM
- Design document: missing boundary contract = HIGH; missing non-functional requirements = MEDIUM
- Research artifact: missing falsification condition = HIGH; missing confidence rating = MEDIUM
- Any artifact: null hypothesis slot gap (SLOT-A/B/C/D missing) = always HIGH (non-overridable)

**Override rule**: A severity assignment that differs from the calibration default or
override MUST include an explicit exception note: `[severity exception: [reason]]` in the
Findings cell. An assignment that silently deviates from calibration does not pass
per-row validation.

---

### Slot manifest (declare before PHASE 1)

Before any phase executes, write and commit the slot manifest. Non-challenger slot entries
MUST include a verbatim `expertise.relevance` quote from the role's registry file:

```
Slot manifest -- crew-review
Depth: [standard | deep]
Artifact type: [inferred from artifact]
Severity calibration: [default | [artifact-type] overrides applied]

Slot 1:  [challenger-role-name] (archetype: challenger)
Slot 2:  [role-name] (archetype: [type])
         expertise.relevance (verbatim): "[exact text from [role-name].md expertise.relevance field]"
         selected because: [1-sentence mapping from verbatim quote to artifact type]
Slot 3:  [role-name] (archetype: [type])
         expertise.relevance (verbatim): "[exact text from [role-name].md expertise.relevance field]"
         selected because: [1-sentence mapping from verbatim quote to artifact type]
...
```

**Selection validation rule**: A non-challenger slot entry without a verbatim
`expertise.relevance` quote is invalid. Manifest may not be committed until all
non-challenger entries carry verbatim quotes.

Rules: Slot 1 = all roles with `archetype: challenger`. Slots 2-N (standard) = 2-3
non-challenger roles ranked by `expertise.relevance` to artifact type. Slots 2-N (deep) =
all non-challenger roles ranked by relevance then alphabetical. Manifest is locked. Roles
absent from manifest may not appear in the matrix. Roles in the manifest may not be skipped.

---

### PHASE 1 -- LOAD

**Entry**: slot manifest committed; severity calibration declared
**Exit**: role pool locked and verified; calibration active

**L1** Open `.roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .roles/ not found.` Halt.
  - Directory empty: `ERROR: .roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.
**L5** Verify manifest selection evidence: for each non-challenger slot, confirm the
  verbatim `expertise.relevance` quote matches the text in the role file. If a quote
  does not match: `ERROR: [role-name] verbatim quote mismatch -- manifest invalid.` Halt.

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked, manifest verified, calibration active)
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
   - Severity: HIGH (non-overridable per calibration protocol)
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
- Severity: apply calibration protocol. Challenger findings = HIGH (inertia credible,
  unaddressed) / MEDIUM (named, cost unstated) / LOW (artifact directly neutralizes status
  quo). If deviation from calibration default: add `[severity exception: [reason]]`.
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
  intersects the artifact type. Target 2-4. Verbatim `expertise.relevance` already in
  manifest -- reference manifest entry.
- `--depth deep`: all non-Slot-1 roles per manifest.

**D2** Execute each slot in manifest order. For each slot:
1. Lens cell: "As a [role], I care about [specific concern from this role's `lens.verify`]."
   Check against Lens column anti-pattern exclusion. Not a generic restatement.
2. Findings cell: name a specific artifact surface. No abstract observations. No repeating
   a finding already raised by a lower-numbered slot.
3. Severity: apply calibration protocol. If deviation from calibration default or override:
   add `[severity exception: [reason]]` to the Findings cell.
4. Recommendation: what to do + where in the artifact.

Collect all rows into draft matrix. Do not write final output -- PHASE 4 validates first.

---

### PHASE 4 -- VALIDATE

**Entry**: all rows collected (PHASE 3 exit)
**Exit**: verification complete; matrix ready for PHASE 5 render

For each row in the draft matrix, verify all six cells against the output schema:
- Slot: consistent with manifest; sub-lettered for slot-gap escalation rows
- Role: filename stem exists in `.roles/` at this execution
- Lens: one sentence, traceable to `lens.verify`, not a generic restatement
- Findings: names a specific artifact surface, not abstract
- Severity: exactly HIGH, MEDIUM, or LOW; consistent with calibration protocol or has
  exception note
- Recommendation: names what to do + where

If a cell fails: revise before writing. A row that cannot pass is removed and logged:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write a criterion-check table before writing the final matrix. This table covers ALL
aspirational criteria through the current rubric version (v7):

| Criterion | Description | Status | Evidence in this draft |
|-----------|-------------|--------|------------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N and Slot M..."] |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions in schema table] |

If any designed-to-satisfy criterion scores NO: return to the relevant phase and revise.
PARTIAL: note the gap and proceed.

---

### PHASE 5 -- RENDER

**Entry**: PHASE 4 verification complete

**R1** Header:

```
Crew Review: [artifact name or type]
Depth: standard | deep
Slots: [list slot numbers and roles]
Roles: [list in slot order]
Severity calibration: [default | [artifact-type] overrides applied]
```

**R2** Review matrix (6 columns, rows in slot order):

| Slot | Role | Lens | Findings | Severity | Recommendation |
|------|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s) from PHASE 2
2. Slot-gap escalation rows (1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

**R3** Cross-role synthesis -- per-slot coverage (required):
For every slot in the manifest (including slot-gap escalation rows), state exactly one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict. Slot-gap escalation rows (1a, 1b, ...) are addressable
slots. A synthesis that names one convergence and leaves other slots without verdicts does
not satisfy this contract.

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`
> - Override severity calibration: `/crew-review [artifact] --amend calibration:[artifact-type]`
