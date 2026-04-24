---
skill: quest-variate
skill_target: crew-review
date: 2026-03-16
round: 10
rubric: crew-review-rubric-v9-2026-03-16.md
---

# crew-review -- Variate R10

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis combinations (V-04, V-05).

**R10 design target**: V-01 R9 scored 161.25/162.5 under rubric v9 -- the only gap is C-27
PARTIAL (1.25 instead of 2.5). V-01 R9's criterion-check table includes C-26 and C-27 rows,
and the C-27 row carries a conditional remediation: "If C-27 = NO: revise R3 synthesis so
every slot receives a verdict before proceeding." This earns C-28 PASS and C-26 PASS. But
R3 text itself only says "name at least one convergence or conflict" -- the table's force-
function creates revision pressure, not a guaranteed per-slot coverage contract. C-27 = PARTIAL
because the minimum-count R3 text remains technically present even when the remediation loop
was satisfied. V-02 R9 scored 157.5/162.5: explicit per-slot contract in R3 achieves C-27
PASS, but criterion-check table stops at C-25 (fails C-26 and C-28 under v9).

Under v9, C-28 is now an aspirational criterion. The v9 criterion-check table must include
C-26, C-27, AND C-28 as rows (C-26 requires self-referential completeness through the current
rubric version). Additionally, C-28 requires every row to carry conditional remediation --
not just the C-27 row.

**R10 axes to probe:**

- V-01: Direct triple-close (single axis: Lifecycle emphasis) -- V-01 R9 plus: (a) R3
  gets V-02's explicit per-slot coverage contract, (b) criterion-check table extends to C-28,
  (c) every criterion-check row carries a specific "If NO:" remediation instruction embedded
  in the table via a 5th column.

- V-02: Extended V-02 (single axis: Output format) -- V-02 R9 plus: criterion-check table
  extends from C-25 to C-28 with full per-row remediation. R3 keeps V-02's explicit per-slot
  contract unchanged.

- V-03: Synthesis as named intermediate phase (single axis: Lifecycle emphasis, variant) --
  introduces PHASE 3.5 -- SYNTHESIZE between REVIEW and VALIDATE with its own gate G2. G2
  closure predicate: every slot in manifest has exactly one verdict. G2 enforces per-slot
  coverage structurally before VALIDATE runs, not through a text contract. A potential C-29
  candidate: synthesis lifecycle isolation.

- V-04: V-01 + V-02 R10 merged (two-axis: Lifecycle + Output format) -- per-slot contract
  in both the output schema section AND R3 text, plus criterion-check table through C-28 with
  5-column remediation.

- V-05: V-04 + verbatim expertise.relevance quotes (three-axis: Lifecycle + Output format +
  Role sequence) -- adds V-03 R9's verbatim manifest requirement and L5 verification step.

**R10 single-axis predictions:**
- V-01 -> C-26 PASS (table through C-28), C-27 PASS (explicit R3 contract), C-28 PASS
  (5-column table, per-row remediation). Predicted: 162.5/162.5
- V-02 -> C-27 PASS (V-02 R9 R3 contract), C-26 PASS (table through C-28), C-28 PASS
  (per-row remediation). Predicted: 162.5/162.5
- V-03 -> C-27 PASS via G2 structural gate, C-26 and C-28 via table. Predicted: 162.5/162.5
  plus possible C-29 candidate signal

**R10 two-axis predictions:**
- V-04 -> 162.5/162.5 via dual enforcement path (schema section + R3 text)
- V-05 -> 162.5/162.5 plus verbatim quote chain pattern

---

## V-01

**Axis**: Lifecycle emphasis -- direct triple-close: explicit R3 per-slot contract + v9
self-referential criterion-check table (through C-28) + 5-column per-row remediation
**Hypothesis**: V-01 R9 got C-27 PARTIAL because the criterion-check table's C-27 row created
revision pressure but R3 text remained minimum-count ("name at least one convergence or
conflict"). The force-function route succeeded in triggering a revision when C-27 = NO, but
the R3 text that survives after revision is not required to cover every slot -- only "at
least one." Replacing R3's minimum-count contract with V-02 R9's explicit per-slot coverage
contract eliminates the ambiguity: every slot must receive a verdict, and the criterion-check
table's C-27 row now scores YES against a guaranteed output. Additionally, under v9 the
criterion-check table requires a C-28 row (self-referential completeness through the current
rubric version). The 5-column table format embeds "Remediation if NO" as a named structural
column, satisfying C-28 at the design level rather than via a footer instruction. Predicted
score: 162.5/162.5.

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
aspirational criteria through the current rubric version (v9), including C-26, C-27, and
C-28 themselves. A table that stops at C-27 fails C-26 under v9. Every row carries a
"Remediation if NO" column -- execute any NO instruction before proceeding to PHASE 5:

| Criterion | Description | Status | Evidence in this draft | Remediation if NO |
|-----------|-------------|--------|------------------------|-------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] | Return to PHASE 2 C2-C4; attempt all 4 slots; escalate each unfilled slot to a dedicated matrix row |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] | Return to the row(s) with missing or generic Lens; rewrite from this role's `lens.verify` field |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] | Add output schema table before execution and reference it in this PHASE 4 gate |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] | Rename the challenger section to "PHASE 2 -- CHALLENGE" at the same heading level as REVIEW |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] | Return to PHASE 2 C4; produce one dedicated HIGH-severity matrix row for each unfilled slot |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] | Add G1 OPEN/CLOSED states and a "Domain review does not begin until G1 transitions to CLOSED" statement |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] | Remove any inline annotations; replace with full 6-column matrix rows at 1a/1b/1c/1d positions |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] | Add NOT: exclusions to the Lens and Findings column definitions in the output schema table |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] | Add explicit OPEN/CLOSED state labels and enumerate at least 2 closure conditions under the G1 predicate |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] | Add explicit "Do not embed..." and "Do not append..." prohibitions inside the escalation rule text |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N and Slot M..."] | Add Slot as the first matrix column; revise synthesis to use "Slot [N] and Slot [M]..." |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] | Rename the validation section to "PHASE 4 -- VALIDATE" at the same heading level as PHASE 2 and PHASE 3 |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] | Move the criterion-check table inside the PHASE 4 -- VALIDATE section |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions in schema table] | Add NOT: exclusion cells to all columns in the output schema table that lack them |
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v9, including C-26, C-27, and C-28 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28 rows present in this table] | Add rows for any missing aspirational criteria including C-26, C-27, and C-28 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [R3 synthesis addresses each slot by number with a verdict] | Return to PHASE 5 R3; for every slot without a verdict, write one of: "Slot [N] converged with...", "Slot [N] conflicts with...", or "Slot [N] is unique: ..." |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a "Remediation if NO" column with a specific action] | Add a "Remediation if NO" column to this table with specific return-to-phase instructions for every row that lacks one |

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

**R3** Cross-role synthesis -- per-slot coverage (required -- must satisfy synthesis output
contract declared above):
For every slot in the manifest (including slot-gap escalation rows), state exactly one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict before synthesis is complete. A synthesis that names one
convergence and leaves other slots without a verdict does not satisfy this contract.

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-02

**Axis**: Output format -- V-02 R9 extended with v9 self-referential criterion-check table
(through C-28) and full per-row remediation
**Hypothesis**: V-02 R9 achieved C-27 PASS via explicit per-slot coverage contract in R3 but
failed C-26 and C-28 because its criterion-check table stopped at C-25. Under v9, C-26
requires the table to include C-26, C-27, AND C-28 as rows (self-referential completeness
through the current rubric version). V-02 R10 carries forward V-02 R9's per-slot R3 contract
unchanged and extends the criterion-check table to C-28 with a 5-column format (adding
"Remediation if NO" column). The enforcement path for C-27 is the R3 text (same as R9 V-02);
the enforcement path for C-26 and C-28 is the extended table. V-02 R10 tests whether the
two-source design (direct R3 contract + extended self-referential table) achieves 162.5/162.5
starting from a different R9 base than V-01. Predicted score: 162.5/162.5.

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
aspirational criteria through the current rubric version (v9). A table that stops at C-25
fails C-26 under v9. Every row includes a "Remediation if NO" column:

| Criterion | Description | Status | Evidence in this draft | Remediation if NO |
|-----------|-------------|--------|------------------------|-------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] | Return to PHASE 2 C2-C4; attempt all 4 slots; produce a dedicated escalation row for each unfilled slot |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] | Rewrite failing Lens cells from this role's `lens.verify` field; a restatement of the role name does not satisfy |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] | Add the output schema table before execution and reference it explicitly in this PHASE 4 validation step |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] | Add "PHASE 2 -- CHALLENGE" as a named header at the same level as PHASE 3 -- REVIEW |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] | Return to PHASE 2 C4; each unfilled slot requires its own dedicated HIGH-severity matrix row |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] | Add the G1 OPEN/CLOSED state machine and the explicit domain-review blocking statement |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] | Replace any inline annotations with full 6-column matrix rows labeled 1a, 1b, 1c, 1d |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] | Add NOT: exclusion language to the Lens and Findings column definitions in the output schema |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] | Add OPEN/CLOSED labels and enumerate at least 2 conditions in the G1 closure predicate |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] | Insert explicit prohibition statements ("Do not embed...", "Do not append...") inside the C4 rule text |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N and Slot M..."] | Add Slot as the leftmost matrix column and revise R3 synthesis to reference "Slot [N]" explicitly |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] | Rename the validation section "PHASE 4 -- VALIDATE" at the same heading level as PHASE 2 and PHASE 3 |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] | Move the criterion-check table to inside the PHASE 4 -- VALIDATE section |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions in schema table] | Add NOT: exclusion cells to all 6 schema columns that lack one |
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v9, including C-26, C-27, and C-28 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28 rows present in this table] | Add the missing rows (including C-26, C-27, C-28) before proceeding; a table that stops at C-25 fails C-26 |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [R3 synthesis covers each slot number with one verdict] | Return to PHASE 5 R3; write exactly one of "Slot [N] converged with...", "conflicts with...", or "is unique: ..." for each slot without a verdict |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a populated "Remediation if NO" column] | Add "Remediation if NO" as a 5th column to this table and fill in a specific return-to-phase instruction for every row |

Execute any NO instruction before writing the final matrix.
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

**R3** Cross-role synthesis -- per-slot coverage (required):
For every slot in the manifest (including slot-gap escalation rows), state exactly one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict. A synthesis that names one convergence and leaves other
slots without a verdict does not satisfy this contract.

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-03

**Axis**: Lifecycle emphasis (variant) -- synthesis as named intermediate phase (PHASE 3.5 --
SYNTHESIZE) with its own gate G2
**Hypothesis**: In all prior variations, cross-role synthesis is a PHASE 5 RENDER step (R3).
Synthesis quality is enforced by contract text ("every slot must receive a verdict") and by
the criterion-check table's C-27 row. Both enforcement mechanisms are declarative -- they
specify the obligation but do not prevent a non-compliant output from reaching RENDER. A
named PHASE 3.5 -- SYNTHESIZE with a gate G2 changes this: synthesis becomes a lifecycle
phase that must complete before VALIDATE runs, and G2 closure requires per-slot coverage as
a condition -- not a contract to check in retrospect. G2 tracks manifest slot count vs.
synthesized slot count. G2 will not close until every slot has exactly one verdict. This is
a structural guarantee for C-27, not a verification guarantee. A potential C-29 candidate:
synthesis lifecycle isolation -- the gate-enforced synthesis phase. Criterion-check table
still extends through C-28 with 5-column remediation.

---

You are running `/crew-review`.

This skill executes in six lifecycle phases. The output schema -- including a Slot column
and a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. PHASE 3.5 synthesizes cross-role findings before PHASE 4 validates.

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

Collect all rows into draft matrix. Do not write final output -- PHASE 3.5 synthesizes next.

---

### PHASE 3.5 -- SYNTHESIZE

**Entry**: all rows collected (PHASE 3 exit)
**Gate G2** -- synthesis coverage gate

**G2 state: OPEN.** PHASE 4 is blocked.

**G2 closure predicate** -- G2 transitions from OPEN to CLOSED when ALL hold:
1. Every slot in the manifest (including slot-gap escalation rows 1a, 1b, ...) has received
   exactly one synthesis verdict.
2. The synthesis verdict count equals the manifest slot count.
3. No slot appears twice; no slot is absent; no verdict is unresolved ("see above", "TBD",
   "same as Slot [N]" without explicit convergence language).
4. Each verdict uses exactly one of the three forms:
   - `Slot [N] converged with Slot [M]: both find [shared concern].`
   - `Slot [N] conflicts with Slot [M]: [tension description].`
   - `Slot [N] is unique: [finding not overlapping with any other slot].`

**PHASE 4 does not begin until G2 transitions to CLOSED.**

---

**S1** For each slot in the manifest (in slot number order), examine all matrix rows with
that slot number against all other slots' findings.

**S2** Write one verdict per slot using exactly one of the three verdict forms above.

**S3** Track coverage: record each slot number as synthesized when its verdict is written.

**S4** Verify G2 closure predicate. All 4 conditions true?

Write: `[G2: CLOSED -- [N] of [N] manifest slots synthesized]`

**G2 state: CLOSED.** Proceed to PHASE 4.

---

### PHASE 4 -- VALIDATE

**Entry**: G2 is CLOSED (PHASE 3.5 exit)
**Exit**: verification complete; matrix and synthesis ready for PHASE 5 render

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
aspirational criteria through the current rubric version (v9). Every row includes a
"Remediation if NO" column:

| Criterion | Description | Status | Evidence in this draft | Remediation if NO |
|-----------|-------------|--------|------------------------|-------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] | Return to PHASE 2 C2-C4; attempt all 4 slots; escalate unfilled slots to dedicated matrix rows |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] | Rewrite failing Lens cells from each role's `lens.verify` field |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] | Add output schema table before execution and reference it in PHASE 4 |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] | Add "PHASE 2 -- CHALLENGE" header at the same level as PHASE 3 |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] | Return to PHASE 2 C4; produce one dedicated HIGH-severity row per unfilled slot |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] | Add G1 state machine and domain-review blocking statement |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] | Replace inline annotations with full 6-column matrix rows at 1a/1b positions |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] | Add NOT: exclusion text to Lens and Findings column definitions |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 conditions listed for G1] | Add OPEN/CLOSED labels and at least 2 enumerated closure conditions under G1 |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] | Insert "Do not embed..." and "Do not append..." inside the C4 escalation rule body |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N..."] | Add Slot as leftmost matrix column; revise synthesis to use "Slot [N]" references |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] | Rename validation section "PHASE 4 -- VALIDATE" at the same heading level |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] | Move criterion-check table into the PHASE 4 -- VALIDATE section |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions] | Add NOT: exclusion cells to all schema columns that lack one |
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v9, including C-26, C-27, and C-28 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28 rows present in this table] | Add rows for C-26, C-27, C-28 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [G2 closed with N/N slots synthesized] | Return to PHASE 3.5; G2 cannot close until every slot has a verdict -- address each missing slot |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a populated "Remediation if NO" column] | Add "Remediation if NO" column to this table with specific instructions for every row lacking one |

Execute any NO instruction before writing the final matrix.
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

**R3** Cross-role synthesis (render from PHASE 3.5 output -- G2 guaranteed coverage):
Render the per-slot verdicts produced and verified in PHASE 3.5. Every slot is already
covered by G2 closure. Do not add new verdicts; do not omit any verdict from PHASE 3.5.

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-04

**Axes**: Lifecycle emphasis + Output format -- V-01 + V-02 R10 merged; dual enforcement via
synthesis output contract in both the schema section and R3 text
**Hypothesis**: V-01 and V-02 R10 both target 162.5/162.5 via structurally complementary
paths: V-01 grounds the per-slot obligation in R3 text; V-02 grounds it in the output schema
section. V-04 carries both: the output schema section declares the per-slot coverage contract
(as in V-02 R9 and V-02 R10) AND R3 text restates the same contract (as in V-01 R10). The
criterion-check table uses the 5-column format through C-28. The two-location synthesis
declaration tests whether having the contract in both the schema section and R3 reduces
C-27 failure probability to near-zero by ensuring no code path can reach RENDER without
encountering the per-slot obligation. Predicted score: 162.5/162.5.

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

**Synthesis output contract -- per-slot coverage** (binding in both this schema declaration
and in PHASE 5 R3): synthesis MUST reference slot numbers. For every slot in the manifest
(including slot-gap escalation rows), state exactly one of:
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
aspirational criteria through the current rubric version (v9). Every row includes a
"Remediation if NO" column:

| Criterion | Description | Status | Evidence in this draft | Remediation if NO |
|-----------|-------------|--------|------------------------|-------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] | Return to PHASE 2 C2-C4; attempt all 4 slots; produce a dedicated escalation row for each unfilled slot |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] | Rewrite failing Lens cells from the role's `lens.verify` field |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] | Add output schema table before execution; reference in this PHASE 4 gate |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] | Add "PHASE 2 -- CHALLENGE" header at the same level as PHASE 3 |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] | Return to PHASE 2 C4; one dedicated HIGH row per unfilled slot |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] | Add G1 state machine and domain-review blocking statement |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column entries] | Replace inline annotations with full 6-column rows at 1a/1b positions |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens, Findings column anti-patterns cited] | Add NOT: exclusions to Lens and Findings column definitions in the schema table |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] | Add OPEN/CLOSED labels and 2+ enumerated G1 closure conditions |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] | Insert "Do not embed..." and "Do not append..." prohibitions inside C4 |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N..."] | Add Slot as leftmost matrix column; revise synthesis to use "Slot [N]" |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] | Rename validation "PHASE 4 -- VALIDATE" at the same heading level |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] | Move this table inside the PHASE 4 -- VALIDATE section |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions] | Add NOT: exclusion cells to all schema columns that lack them |
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v9, including C-26, C-27, and C-28 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28 rows present in this table] | Add rows for any missing aspirational criteria through v9 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [R3 synthesis covers each manifest slot number with one verdict] | Return to PHASE 5 R3; write exactly one verdict ("Slot [N] converged...", "conflicts...", or "is unique: ...") for each slot without one |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a populated "Remediation if NO" column] | Add "Remediation if NO" column and fill in a specific action for every row that lacks one |

Execute any NO instruction before writing the final matrix.
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

**R3** Cross-role synthesis -- per-slot coverage (required -- must satisfy synthesis output
contract declared in the schema section above):
For every slot in the manifest (including slot-gap escalation rows), state exactly one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict. A synthesis that names one convergence and leaves other
slots without a verdict does not satisfy this contract.

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---

## V-05

**Axes**: Lifecycle emphasis + Output format + Role sequence -- V-04 R10 plus verbatim
`expertise.relevance` quote in manifest and L5 verification step (V-03 R9 pattern)
**Hypothesis**: V-04 achieves dual-location synthesis enforcement and full criterion-check
self-reference through C-28. V-03 R9 introduced a verbatim `expertise.relevance` quote
in the slot manifest as a falsifiable selection chain. The quote must exactly match the
registry file text; L5 verifies before execution proceeds. In V-05, all three patterns
coexist: (1) dual synthesis obligation in schema section and R3; (2) self-referential
criterion-check table through C-28 with 5-column remediation; (3) verbatim manifest quote
with L5 verification. The question V-05 answers: does verbatim quote enforcement interact
with or conflict with the other two patterns, or do all three coexist cleanly? If all three
coexist without structural tension, V-05 is the most complete design produced in this series.
Predicted score: 162.5/162.5 plus the verbatim quote pattern available for C-29 extraction.

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

**Synthesis output contract -- per-slot coverage** (binding in both this schema declaration
and in PHASE 5 R3): synthesis MUST reference slot numbers. For every slot in the manifest
(including slot-gap escalation rows), state exactly one of:
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
- Role: filename stem exists in `.roles/` at this execution
- Lens: one sentence, traceable to `lens.verify`, not a generic restatement
- Findings: names a specific artifact surface, not abstract
- Severity: exactly HIGH, MEDIUM, or LOW
- Recommendation: names what to do + where

If a cell fails: revise before writing. A row that cannot pass is removed and logged:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write a criterion-check table before writing the final matrix. This table covers ALL
aspirational criteria through the current rubric version (v9). Every row includes a
"Remediation if NO" column:

| Criterion | Description | Status | Evidence in this draft | Remediation if NO |
|-----------|-------------|--------|------------------------|-------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] | Return to PHASE 2 C2-C4; attempt all 4 slots; produce one dedicated escalation row per unfilled slot |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] | Rewrite failing Lens cells from each role's `lens.verify` field |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] | Add output schema table before execution; reference it in PHASE 4 |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] | Add "PHASE 2 -- CHALLENGE" header at the same level as PHASE 3 |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] | Return to PHASE 2 C4; produce one dedicated HIGH row per unfilled slot |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] | Add G1 state machine and domain-review blocking statement |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column entries] | Replace inline annotations with full 6-column matrix rows at 1a/1b positions |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens, Findings column anti-patterns cited] | Add NOT: exclusion language to Lens and Findings column definitions |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] | Add OPEN/CLOSED labels and enumerate 2+ G1 closure conditions |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] | Insert "Do not embed..." and "Do not append..." inside C4 |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N..."] | Add Slot as leftmost matrix column; revise synthesis to use "Slot [N]" references |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] | Rename validation "PHASE 4 -- VALIDATE" at the same heading level |
| C-24 | Criterion-check table embedded in VALIDATE phase | [YES/NO/PARTIAL] | [this table is present inside PHASE 4] | Move this table inside the PHASE 4 -- VALIDATE section |
| C-25 | Every schema column carries an anti-pattern exclusion | [YES/NO/PARTIAL] | [all 6 columns have NOT: exclusions] | Add NOT: exclusion cells to all schema columns that lack one |
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v9, including C-26, C-27, and C-28 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28 rows present in this table] | Add missing criterion rows including C-26, C-27, C-28 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [R3 synthesis covers each manifest slot number with one verdict] | Return to PHASE 5 R3; write one verdict per slot for every slot without one |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a populated "Remediation if NO" column] | Add "Remediation if NO" column and fill in a specific instruction for every row lacking one |

Execute any NO instruction before writing the final matrix.
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

**R3** Cross-role synthesis -- per-slot coverage (required -- must satisfy synthesis output
contract declared in the schema section above):
For every slot in the manifest (including slot-gap escalation rows), state exactly one of:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

Every slot must receive a verdict. A synthesis that names one convergence and leaves other
slots without a verdict does not satisfy this contract.

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`
