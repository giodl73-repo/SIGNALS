---
skill: quest-variate
skill_target: crew-review
date: 2026-03-16
round: 9
rubric: crew-review-rubric-v8-2026-03-16.md
---

# crew-review -- Variate R9

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis combinations (V-04, V-05).

**R9 design target**: R8 V-01 and V-02 each scored 157.5/160 under rubric v8 -- each
satisfying exactly one of C-26 or C-27 but not both simultaneously. V-04 R8 combined
C-26+C-27 structurally but its criterion-check table header referenced "v7" and contained
rows only through C-25, meaning it failed C-26 (which requires the table to include rows
for C-26 and C-27 themselves -- self-referential completeness under the current rubric
version). R9 targets three new patterns against the v8 rubric:

- V-01: Criterion-check self-referential completeness under v8 (single axis: Lifecycle
  emphasis) -- the criterion-check table explicitly includes rows for C-26 AND C-27
  themselves. A row for C-27 in the table creates a validation obligation: if synthesis is
  minimum-count, C-27 = NO triggers a revision. Hypothesis: including C-26 and C-27 as
  rows in the criterion-check table closes the v8 self-referential gap and acts as a
  force-function toward per-slot synthesis even when R3 text uses the minimum-count
  contract.

- V-02: Explicit per-slot synthesis contract in R3 text (single axis: Output format) --
  changes R3 from "name at least one convergence or conflict" to an explicit per-slot
  coverage contract identical to R8 V-02, but holds the criterion-check table at C-25
  (no C-26/C-27 rows). Hypothesis: explicit R3 text is a more direct enforcement path to
  C-27 than the force-function route in V-01. The two paths are testable independently
  before combining.

- V-03: Verbatim expertise.relevance quote in manifest (single axis: Role sequence) --
  each non-challenger slot entry must include a verbatim `expertise.relevance` field quote
  from the registry file, not a paraphrase. L5 verification step in PHASE 1 checks quotes
  against the actual file text. Hypothesis: verbatim field quoting produces a falsifiable
  selection chain (C-28 candidate) that is traceable, registry-grounded, and detectable
  as a new rubric pattern.

**R9 single-axis targets:**
- V-01 -> C-26 via table force-function; C-27 via revision obligation
- V-02 -> C-27 via explicit R3 contract
- V-03 -> C-28 candidate: verbatim `expertise.relevance` quote in manifest

**R9 two-axis targets:**
- V-04 (Lifecycle + Output format): V-01 + V-02 -- criterion-check table includes C-26/C-27
  rows AND R3 has explicit per-slot synthesis. Belt-and-suspenders for 160/160.
- V-05 (Lifecycle + Output format + Role sequence): V-04 + V-03 -- adds verbatim
  expertise.relevance quotes. Triple combination targeting C-26 + C-27 + C-28 candidate
  simultaneously.

---

## V-01

**Axis**: Lifecycle emphasis -- criterion-check self-referential completeness under v8
**Hypothesis**: R8 V-01 added C-24 and C-25 as rows in the criterion-check table,
satisfying C-26 under the v7 rubric (which defined C-26 as: the table includes rows for
C-24 and C-25 themselves). Under v8, C-26 now requires the table to include rows for
C-26 AND C-27 -- the two criteria that postdate the table's original design. V-01 R8's
table stops at C-25 and therefore fails C-26 under v8. V-01 R9 closes this gap: the
criterion-check table includes rows for C-26 and C-27. Because the table includes a C-27
row with a YES/NO/PARTIAL slot, and C-27 requires per-slot synthesis, a minimum-count
synthesis output would score C-27 = NO, triggering a mandatory revision under the PHASE 4
exit contract. The criterion-check table is the enforcement mechanism: self-referential
completeness creates a validation obligation.

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
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not present in the registry at this execution |
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

**L1** Open `.craft/roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .craft/roles/ not found.` Halt.
  - Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
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
- Role: filename stem exists in `.craft/roles/` at this execution
- Lens: one sentence, traceable to `lens.verify`, not a generic restatement
- Findings: names a specific artifact surface, not abstract
- Severity: exactly HIGH, MEDIUM, or LOW
- Recommendation: names what to do + where

If a cell fails: revise before writing. A row that cannot pass is removed and logged:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write a criterion-check table before writing the final matrix. This table covers ALL
aspirational criteria through the current rubric version (v8), including C-26 and C-27.
A table that stops at C-25 fails C-26. Verify every row -- including C-26 and C-27 -- and
revise any cell or phase that scores NO before proceeding:

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
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v8, including C-26 and C-27 themselves | [YES/NO/PARTIAL] | [C-26 and C-27 rows present in this table] |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [R3 synthesis addresses each slot by number] |

If any criterion scores NO: return to the relevant phase and revise before proceeding.
If C-27 = NO: revise R3 synthesis so every slot receives a convergence, conflict, or unique
verdict before writing the final matrix.
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

**Axis**: Output format -- explicit per-slot synthesis coverage contract in R3
**Hypothesis**: R8 V-02 demonstrated that an explicit per-slot synthesis contract in R3 text
directly satisfied C-27. The enforcement path is clear and model-verifiable without
relying on the criterion-check table's C-27 row to trigger a revision. V-02 R9 holds the
criterion-check table at C-25 (no C-26/C-27 rows) to isolate the axis: does the explicit
R3 per-slot contract satisfy C-27 even when the criterion-check table doesn't include a
C-27 row? This also tests whether C-26 is still achievable when the table is bounded at
C-25 (under v8, it is not -- the table that stops at C-25 fails C-26 because C-26 and C-27
are now aspirational criteria the table does not verify). Isolating this axis predicts
V-02 R9 will score 157.5: C-27 PASS, C-26 FAIL.

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
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not present in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern traceable to this role's `lens.verify`]." | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns not traceable to this role's `lens.verify` field; NOT: multi-sentence declarations; NOT: absent Lens cells; NOT: Lens cells that merely restate the role name |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: observations naming only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

**Synthesis output contract -- per-slot coverage**: synthesis MUST reference slot numbers.
For every slot in the manifest (including slot-gap escalation rows), state exactly one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict. A synthesis that names one convergence and leaves other
slots without a verdict does not satisfy this contract.

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

**L1** Open `.craft/roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .craft/roles/ not found.` Halt.
  - Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
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
- Role: filename stem exists in `.craft/roles/` at this execution
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

**Axis**: Role sequence -- verbatim expertise.relevance quote in manifest
**Hypothesis**: The current slot manifest requires "selected because [reason tied to
artifact]" -- paraphrase that could be fabricated or recalled from memory rather than read
from the registry file. A verbatim `expertise.relevance` field quote creates a falsifiable
selection chain: the quote must exactly match the text in the role file at execution time,
verified by a new L5 step. A paraphrase without the verbatim quote does not satisfy the
manifest commitment contract. This is the C-28 candidate: role selection grounded in
registry evidence, not executor interpretation.

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
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not present in the registry at this execution |
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
         selected because: [1-sentence mapping from verbatim quote to this artifact type]
Slot 3:  [role-name] (archetype: [type])
         expertise.relevance (verbatim): "[exact text from [role-name].md expertise.relevance field]"
         selected because: [1-sentence mapping from verbatim quote to this artifact type]
...
```

**Selection validation rule**: A non-challenger slot entry without a verbatim
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

**L1** Open `.craft/roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .craft/roles/ not found.` Halt.
  - Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.
**L5** Verify manifest selection evidence: for each non-challenger slot, confirm the
  verbatim `expertise.relevance` quote matches the text in the role file exactly. If a
  quote does not match: `ERROR: [role-name] verbatim quote mismatch -- manifest invalid.`
  Halt.

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
- Standard (default): verbatim `expertise.relevance` quotes already in manifest -- reference
  manifest entries. Target 2-4 roles. Non-challenger roles absent from manifest may not run.
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
- Role: filename stem exists in `.craft/roles/` at this execution
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

**Axes**: Lifecycle emphasis + Output format (criterion-check self-referential under v8 +
explicit per-slot synthesis contract)
**Hypothesis**: V-01 makes the criterion-check table self-referential under v8 (C-26 + C-27
rows) and relies on the table's C-27 row to force a revision if synthesis is minimum-count.
V-02 makes per-slot synthesis explicit in R3 text (C-27 direct enforcement path). The two
enforcement mechanisms are structurally independent and can coexist: C-26 is a PHASE 4
property (criterion-check table covers all aspirational criteria through v8 including
itself); C-27 is a PHASE 5 property (every slot receives an explicit verdict). V-04 uses
both -- the explicit R3 per-slot contract plus the criterion-check table that contains a
C-27 row that will score YES if synthesis is exhaustive. This is the belt-and-suspenders
approach to 160/160: enforcement through both the R3 contract text and the PHASE 4
self-verification gate.

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
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not present in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern traceable to this role's `lens.verify`]." | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns not traceable to this role's `lens.verify` field; NOT: multi-sentence declarations; NOT: absent Lens cells; NOT: Lens cells that merely restate the role name |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: observations naming only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

**Synthesis output contract -- per-slot coverage**: synthesis MUST reference slot numbers.
For every slot in the manifest (including slot-gap escalation rows), state exactly one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict. A synthesis that names one convergence and leaves other
slots without a verdict does not satisfy this contract.

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

**L1** Open `.craft/roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .craft/roles/ not found.` Halt.
  - Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
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
- Role: filename stem exists in `.craft/roles/` at this execution
- Lens: one sentence, traceable to `lens.verify`, not a generic restatement
- Findings: names a specific artifact surface, not abstract
- Severity: exactly HIGH, MEDIUM, or LOW
- Recommendation: names what to do + where

If a cell fails: revise before writing. A row that cannot pass is removed and logged:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write a criterion-check table before writing the final matrix. This table covers ALL
aspirational criteria through the current rubric version (v8), including C-26 and C-27.
A table that stops at C-25 fails C-26. Check every row and revise any phase that scores
NO before proceeding:

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
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v8, including C-26 and C-27 themselves | [YES/NO/PARTIAL] | [C-26 and C-27 rows present in this table] |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [R3 synthesis addresses each slot by number with a declared verdict] |

If any criterion scores NO: return to the relevant phase and revise before proceeding.
If C-26 = NO: extend this table with missing criterion rows.
If C-27 = NO: revise R3 synthesis so every slot receives a verdict.
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

**Axes**: Lifecycle emphasis + Output format + Role sequence (criterion-check
self-referential under v8 + explicit per-slot synthesis + verbatim expertise.relevance
quotes)
**Hypothesis**: V-04 achieves C-26+C-27 through both table self-referential completeness
and explicit per-slot synthesis text. V-03 independently tests C-28 (verbatim field
quotes). V-05 combines all three: the verbatim selection evidence in the manifest creates
a fully traceable selection chain from the registry file through the manifest entry into
the executed review. The L5 verification step enforces the quote match at PHASE 1 exit,
before any review runs. Combined with C-26+C-27 from V-04, this variation carries three
structural improvements simultaneously. If V-04 achieves 160/160 on C-26+C-27, V-05
tests whether C-28 (verbatim quotes) can be added without degrading the properties that
V-04 established.

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
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not present in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern traceable to this role's `lens.verify`]." | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns not traceable to this role's `lens.verify` field; NOT: multi-sentence declarations; NOT: absent Lens cells; NOT: Lens cells that merely restate the role name |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: observations naming only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

**Synthesis output contract -- per-slot coverage**: synthesis MUST reference slot numbers.
For every slot in the manifest (including slot-gap escalation rows), state exactly one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict. A synthesis that names one convergence and leaves other
slots without a verdict does not satisfy this contract.

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
         selected because: [1-sentence mapping from verbatim quote to this artifact type]
Slot 3:  [role-name] (archetype: [type])
         expertise.relevance (verbatim): "[exact text from [role-name].md expertise.relevance field]"
         selected because: [1-sentence mapping from verbatim quote to this artifact type]
...
```

**Selection validation rule**: A non-challenger slot entry without a verbatim
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
**Exit**: role pool locked, verified, and manifest evidence confirmed

**L1** Open `.craft/roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .craft/roles/ not found.` Halt.
  - Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.
**L5** Verify manifest selection evidence: for each non-challenger slot, confirm the
  verbatim `expertise.relevance` quote matches the text in the role file exactly. If a
  quote does not match: `ERROR: [role-name] verbatim quote mismatch -- manifest invalid.`
  Halt.

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked, manifest verified)
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
- Standard (default): verbatim `expertise.relevance` quotes already in manifest -- reference
  manifest entries. Target 2-4 roles. Non-challenger roles absent from manifest may not run.
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
- Role: filename stem exists in `.craft/roles/` at this execution
- Lens: one sentence, traceable to `lens.verify`, not a generic restatement
- Findings: names a specific artifact surface, not abstract
- Severity: exactly HIGH, MEDIUM, or LOW
- Recommendation: names what to do + where

If a cell fails: revise before writing. A row that cannot pass is removed and logged:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write a criterion-check table before writing the final matrix. This table covers ALL
aspirational criteria through the current rubric version (v8), including C-26 and C-27.
A table that stops at C-25 fails C-26. Check every row and revise any phase that scores
NO before proceeding:

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
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v8, including C-26 and C-27 themselves | [YES/NO/PARTIAL] | [C-26 and C-27 rows present in this table] |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [R3 synthesis addresses each slot by number with a declared verdict] |

If any criterion scores NO: return to the relevant phase and revise before proceeding.
If C-26 = NO: extend this table with missing criterion rows.
If C-27 = NO: revise R3 synthesis so every slot receives a verdict.
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
