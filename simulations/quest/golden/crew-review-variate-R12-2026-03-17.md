---
skill: quest-variate
skill_target: crew-review
date: 2026-03-17
round: 12
rubric: crew-review-rubric-v11-2026-03-17.md
---

# crew-review -- Variate R12

5 complete prompt body variations. Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

**R12 design target**: Under v11, R11 V-01 passes C-33 via `[G2: CLOSED -- [N] slots in manifest, [N] verdicts assigned]`. The rubric confirms: "A gate that says 'G2 closes when N verdicts have been assigned for N loaded slots' satisfies C-33." R11's form satisfies this. R12 explores three distinct C-33 implementation axes -- LOAD binding, typed predicate assertion, and formal variable notation -- to find the strongest form and identify what C-34 might require.

**R12 axes:**

- V-01: Lifecycle emphasis (single axis) -- PHASE 1 LOAD emits `manifest_slot_count = N` as a named variable at step L5. G2 closure predicate condition 1 references this LOAD-bound count by name. G2 write: `[G2: CLOSED -- manifest_slot_count=[N] (PHASE 1 LOAD), verdicts_produced=[N]; N-for-N predicate satisfied]`. Criterion-check table extended to 22 rows (through C-33).

- V-02: Output format (single axis) -- G2 closure check rendered as a typed 3-field predicate assertion block (manifest_slot_count | verdicts_produced | N-for-N status) placed between S1 verdict production and the G2 write. Machine-checkable form is a visible structure, not prose.

- V-03: Phrasing register (single axis) -- G2 predicate uses formal variable-binding notation: `Let K = manifest_slot_count`. G2 closes iff `|{verdicts}| = K`. Mathematical equality replaces narrative "every slot has one verdict."

- V-04: Lifecycle + Output format (two-axis) -- V-01's LOAD binding (step L5) + V-02's typed predicate block. The block explicitly references `manifest_slot_count` bound at PHASE 1 by name.

- V-05: Lifecycle + Output format + Inertia framing (three-axis) -- V-04 + escalation-aware cardinality. PHASE 1 emits `base_slot_count`; PHASE 2 emits `escalation_row_count` after C6. G2 predicate block: `total = base + escalation; verdict_count must equal total`. Strongest C-33 form: the N is not just declared but dynamically computed across two phases.

**Predicted R12 scores under v11:**
- V-01: 175.0/175.0 (C-33 PASS -- LOAD-bound N in G2 write; criterion-check table 22 rows)
- V-02: 175.0/175.0 (C-33 PASS -- typed predicate assertion satisfies machine-checkable form)
- V-03: 175.0/175.0 (C-33 PASS -- formal K=N binding satisfies machine-checkable form)
- V-04: 175.0/175.0 (C-33 dual enforcement: LOAD binding + typed assertion)
- V-05: 175.0/175.0 (C-33 strongest form: escalation-aware total cardinality)

**Variation-specific C-34 signals:**
- V-01: named LOAD binding -- could motivate C-34 (G2 predicate references LOAD-emitted count by variable name, not placeholder)
- V-02: typed predicate as output structure -- could motivate C-34 (predicate assertion is a typed schema with column contracts, same discipline as review matrix and criterion-check table)
- V-03: formal variable binding -- could motivate C-34 (K declared at gate entry, referenced in closure predicate and write statement; consistent scoping)
- V-05: escalation-aware cardinality -- could motivate C-34 (N includes dynamically added escalation rows, not just declared slots; two-phase accumulation)

---

## V-01

**Axis**: Lifecycle emphasis -- PHASE 1 LOAD emits manifest_slot_count as named variable
**Hypothesis**: R11 V-01 satisfies C-33 via `[G2: CLOSED -- [N] slots in manifest, [N] verdicts assigned]` where `[N]` is a template placeholder filled at execution. C-33's definition says "quantified against the LOAD manifest cardinality." The strongest form binds the count at LOAD time as a named variable and references it by name in the G2 predicate. Adding step L5 (`Write: [LOAD: manifest_slot_count = N]`) to PHASE 1 and referencing `manifest_slot_count` explicitly in G2 closure predicate condition 1 and the G2 write makes the binding unambiguous. Criterion-check table extended from 21 rows (through C-32) to 22 rows (through C-33). C-29 evidence updated to "all 22 rows." C-26 evidence updated to include C-33. Predicted: 175.0/175.0.

---

You are running `/crew-review`.

This skill executes in six lifecycle phases. The output schema -- including a Slot column and a Lens column -- is declared before execution begins. Execution order is declared as a numbered slot manifest. PHASE 1 LOAD binds `manifest_slot_count` as a named variable. PHASE 3.5 synthesizes cross-role signals; G2 closure predicate references `manifest_slot_count` by name and gates AMEND. PHASE 4 validates the draft matrix before final render.

---

### Output schema (declared before execution)

The review artifact is a 6-column matrix. All column contracts are binding. The per-row validation gate in PHASE 4 enforces every cell against these contracts.

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

Rules: Slot 1 = all roles with `archetype: challenger`. Slots 2-N (standard) = 2-3 non-challenger roles ranked by `expertise.relevance` to artifact type. Slots 2-N (deep) = all non-challenger roles ranked by relevance then alphabetical. Manifest is locked. Roles absent from manifest may not appear in the matrix. Roles in the manifest may not be skipped.

---

### PHASE 1 -- LOAD

**Entry**: slot manifest committed
**Exit**: role pool locked and verified; manifest_slot_count bound

**L1** Open `.roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .roles/ not found.` Halt.
  - Directory empty: `ERROR: .roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.
**L5** Count slots in the committed manifest (Slot 1 through Slot N, including all declared
  slot-gap escalation rows). Bind this count as `manifest_slot_count`.

Write: `[LOAD: manifest_slot_count = N]`

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked; manifest_slot_count bound)
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
1. Count of synthesis verdicts produced equals `manifest_slot_count` bound at PHASE 1 LOAD
   (N). Every slot in the manifest has exactly one verdict; no slot is omitted or given more
   than one.
2. Each verdict is one of: converged, conflicted, or unique.
3. No slot is merged with another or assigned more than one verdict.
4. Every verdict statement references slot numbers.

**AMEND does not begin until G2 transitions to CLOSED.**

---

**S1** For every slot in the manifest (Slot 1 through Slot N, including any slot-gap
escalation rows), assign exactly one verdict:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

**S2** Check G2 predicate. Verdict count equals `manifest_slot_count` (N)?

Write: `[G2: CLOSED -- manifest_slot_count=[N] (PHASE 1 LOAD), verdicts_produced=[N]; N-for-N predicate satisfied]`

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
aspirational criteria through the current rubric version (v11), including C-26 through C-33
themselves. A table that stops before C-33 fails C-26 under v11. Every row carries a
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
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v11, including C-26 through C-33 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 rows present in this table] | Add rows for any missing aspirational criteria including C-26 through C-33 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [G2 closed: manifest_slot_count=[N] (PHASE 1 LOAD), verdicts_produced=[N]; N-for-N satisfied] | Return to PHASE 3.5; G2 cannot close until verdict count equals manifest_slot_count -- assign a verdict to each missing slot |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a "Remediation if NO" column with a specific action] | Add a specific return-to-phase instruction to every row that lacks one |
| C-29 | Exhaustive criterion-failure remediation coverage -- every row, not just at least one | [YES/NO/PARTIAL] | [all 22 rows in this table carry a populated Remediation if NO cell] | Ensure every row has a specific, actionable remediation instruction -- no row may be empty or generic |
| C-30 | Criterion-check table presented as typed 5-column schema with dedicated "Remediation if NO" column | [YES/NO/PARTIAL] | [column header reads: Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO] | Reformat table as typed 5-column schema with "Remediation if NO" as the 5th named header column |
| C-31 | Synthesis declared as a named discrete execution phase (PHASE 3.5 SYNTHESIZE) | [YES/NO/PARTIAL] | [PHASE 3.5 -- SYNTHESIZE header present at same heading level as PHASE 3 and PHASE 4] | Add PHASE 3.5 -- SYNTHESIZE as a named section heading between PHASE 3 and PHASE 4; move synthesis execution into it |
| C-32 | Synthesis phase gate G2 has formal exit condition blocking AMEND until synthesis closes | [YES/NO/PARTIAL] | [G2 OPEN/CLOSED states present + "AMEND does not begin until G2 transitions to CLOSED" statement in PHASE 3.5] | Add G2 state machine with OPEN/CLOSED labels; add explicit "AMEND does not begin until G2 transitions to CLOSED" blocking statement |
| C-33 | G2 closure predicate is quantified against LOAD manifest cardinality -- N-for-N form | [YES/NO/PARTIAL] | [G2 write references manifest_slot_count=[N] (PHASE 1 LOAD L5); verdicts_produced=[N]; N-for-N predicate satisfied] | Add step L5 to PHASE 1 binding manifest_slot_count; revise G2 closure predicate condition 1 to reference manifest_slot_count by name; revise G2 write to use bound count form |

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
manifest_slot_count: [N] (bound at PHASE 1 LOAD)
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
verdict assigned under G2 closure (N verdicts for manifest_slot_count = N). Render each
verdict in slot-number order:
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

**Axis**: Output format -- G2 closure check as typed 3-field predicate assertion block
**Hypothesis**: R11 V-01 satisfies C-33 via G2 write prose. C-33 says "machine-checkable: verdict count == slot count." An alternative output format makes the machine-checkable form a visible structure: a typed 3-field assertion block placed between S1 verdict production and the G2 write. The block has three named fields -- manifest_slot_count, verdicts_produced, N-for-N status -- parallel to the output schema and criterion-check table pattern. G2 transitions to CLOSED only when the assertion block shows N-for-N: SATISFIED. The assertion block is not prose; it is a typed structure with named fields. If N-for-N: NOT SATISFIED, execution returns to S1 before G2 can close. Predicted: 175.0/175.0. Variation-specific C-34 signal: typed predicate assertion could motivate C-34 ("G2 predicate assertion block has named field contracts with NOT: exclusions, same discipline as review matrix schema columns").

---

You are running `/crew-review`.

This skill executes in six lifecycle phases. The output schema -- including a Slot column and a Lens column -- is declared before execution begins. Execution order is declared as a numbered slot manifest. PHASE 3.5 synthesizes cross-role signals and produces a typed G2 predicate assertion block; G2 transitions to CLOSED only when the block shows N-for-N: SATISFIED. PHASE 4 validates the draft matrix before final render.

---

### Output schema (declared before execution)

The review artifact is a 6-column matrix. All column contracts are binding. The per-row validation gate in PHASE 4 enforces every cell against these contracts.

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
1. The G2 predicate assertion block (written at S2) shows N-for-N: SATISFIED --
   verdicts_produced equals manifest_slot_count.
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

**S2** Produce the G2 predicate assertion block:

```
G2 predicate assertion:
  manifest_slot_count: [N]
  verdicts_produced:   [N]
  N-for-N:             SATISFIED
```

If verdicts_produced does not equal manifest_slot_count, write `N-for-N: NOT SATISFIED`
and return to S1. G2 cannot transition to CLOSED until N-for-N: SATISFIED.

Write: `[G2: CLOSED -- predicate assertion verified; N-for-N: SATISFIED]`

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
aspirational criteria through the current rubric version (v11), including C-26 through C-33
themselves. A table that stops before C-33 fails C-26 under v11. Every row carries a
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
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v11, including C-26 through C-33 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 rows present in this table] | Add rows for any missing aspirational criteria including C-26 through C-33 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [G2 predicate assertion N-for-N: SATISFIED; manifest_slot_count=[N]; verdicts_produced=[N]] | Return to PHASE 3.5 S1; produce missing verdicts; predicate assertion must show N-for-N: SATISFIED before G2 can close |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a "Remediation if NO" column with a specific action] | Add a specific return-to-phase instruction to every row that lacks one |
| C-29 | Exhaustive criterion-failure remediation coverage -- every row, not just at least one | [YES/NO/PARTIAL] | [all 22 rows in this table carry a populated Remediation if NO cell] | Ensure every row has a specific, actionable remediation instruction -- no row may be empty or generic |
| C-30 | Criterion-check table presented as typed 5-column schema with dedicated "Remediation if NO" column | [YES/NO/PARTIAL] | [column header reads: Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO] | Reformat table as typed 5-column schema with "Remediation if NO" as the 5th named header column |
| C-31 | Synthesis declared as a named discrete execution phase (PHASE 3.5 SYNTHESIZE) | [YES/NO/PARTIAL] | [PHASE 3.5 -- SYNTHESIZE header present at same heading level as PHASE 3 and PHASE 4] | Add PHASE 3.5 -- SYNTHESIZE as a named section heading between PHASE 3 and PHASE 4; move synthesis execution into it |
| C-32 | Synthesis phase gate G2 has formal exit condition blocking AMEND until synthesis closes | [YES/NO/PARTIAL] | [G2 OPEN/CLOSED states present + "AMEND does not begin until G2 transitions to CLOSED" statement in PHASE 3.5] | Add G2 state machine with OPEN/CLOSED labels; add explicit "AMEND does not begin until G2 transitions to CLOSED" blocking statement |
| C-33 | G2 closure predicate is quantified against LOAD manifest cardinality -- N-for-N form | [YES/NO/PARTIAL] | [G2 predicate assertion block present at PHASE 3.5 S2; N-for-N: SATISFIED shown; verdicts_produced = manifest_slot_count] | Add typed G2 predicate assertion block (manifest_slot_count \| verdicts_produced \| N-for-N) between S1 and G2 write; G2 cannot close until block shows N-for-N: SATISFIED |

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

Copy the synthesis verdicts produced in PHASE 3.5 S1. G2 predicate assertion confirmed
N-for-N: SATISFIED. Render each verdict in slot-number order:
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

## V-03

**Axis**: Phrasing register -- formal variable-binding notation for G2 predicate
**Hypothesis**: V-01 and V-02 satisfy C-33 via English-language binding and typed assertion
blocks respectively. A third axis is phrasing register: stating the G2 predicate using
formal variable-binding notation (`Let K = manifest_slot_count`) throughout PHASE 3.5. K is
introduced at the gate definition, referenced in the closure predicate, and in the G2 write:
`[G2: CLOSED -- K=[N], |{verdicts}|=[N]; equality K=|{verdicts}| holds]`. The mathematical
equality replaces narrative "every slot has one verdict." The scoping is internally
consistent: K is declared once and used everywhere in PHASE 3.5. Predicted: 175.0/175.0.
Variation-specific C-34 signal: formal variable declaration at gate entry could motivate
C-34 ("K is declared in the gate preamble, before the closure predicate, making the scope
of the variable explicit and separable from the predicate logic").

---

You are running `/crew-review`.

This skill executes in six lifecycle phases. The output schema -- including a Slot column and
a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. PHASE 3.5 synthesizes cross-role signals using formal variable-
binding notation: `Let K = manifest_slot_count`; G2 closes iff `|{verdicts}| = K`. PHASE 4
validates the draft matrix before final render.

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

Let K = count(manifest_slots) -- the total number of slots in the committed manifest,
including any slot-gap escalation rows declared in the manifest.

**G2 state: OPEN.** AMEND is blocked.

**G2 closure predicate** -- G2 transitions from OPEN to CLOSED iff ALL hold:
1. |{synthesis verdicts produced}| = K. Every slot has exactly one verdict; none omitted.
2. Each verdict is one of: converged, conflicted, or unique.
3. No slot appears more than once in the verdict set.
4. Every verdict statement references slot numbers.

**AMEND does not begin until G2 transitions to CLOSED.**

---

**S1** For every slot in the manifest (Slot 1 through Slot N, including any slot-gap
escalation rows), assign exactly one verdict:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

**S2** Verify: `|{verdicts produced}| = K`?

Write: `[G2: CLOSED -- K=[N], |{verdicts}|=[N]; equality K=|{verdicts}| holds; N-for-N predicate satisfied]`

If the equality does not hold, return to S1. G2 cannot transition to CLOSED until
|{verdicts}| = K.

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
aspirational criteria through the current rubric version (v11), including C-26 through C-33
themselves. A table that stops before C-33 fails C-26 under v11. Every row carries a
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
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v11, including C-26 through C-33 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 rows present in this table] | Add rows for any missing aspirational criteria including C-26 through C-33 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [G2 closed: K=[N]; |{verdicts}|=[N]; equality holds] | Return to PHASE 3.5 S1; G2 cannot close until |{verdicts}| = K -- assign a verdict to each missing slot |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a "Remediation if NO" column with a specific action] | Add a specific return-to-phase instruction to every row that lacks one |
| C-29 | Exhaustive criterion-failure remediation coverage -- every row, not just at least one | [YES/NO/PARTIAL] | [all 22 rows in this table carry a populated Remediation if NO cell] | Ensure every row has a specific, actionable remediation instruction -- no row may be empty or generic |
| C-30 | Criterion-check table presented as typed 5-column schema with dedicated "Remediation if NO" column | [YES/NO/PARTIAL] | [column header reads: Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO] | Reformat table as typed 5-column schema with "Remediation if NO" as the 5th named header column |
| C-31 | Synthesis declared as a named discrete execution phase (PHASE 3.5 SYNTHESIZE) | [YES/NO/PARTIAL] | [PHASE 3.5 -- SYNTHESIZE header present at same heading level as PHASE 3 and PHASE 4] | Add PHASE 3.5 -- SYNTHESIZE as a named section heading between PHASE 3 and PHASE 4; move synthesis execution into it |
| C-32 | Synthesis phase gate G2 has formal exit condition blocking AMEND until synthesis closes | [YES/NO/PARTIAL] | [G2 OPEN/CLOSED states present + "AMEND does not begin until G2 transitions to CLOSED" statement in PHASE 3.5] | Add G2 state machine with OPEN/CLOSED labels; add explicit "AMEND does not begin until G2 transitions to CLOSED" blocking statement |
| C-33 | G2 closure predicate is quantified against LOAD manifest cardinality -- N-for-N form | [YES/NO/PARTIAL] | [G2 uses formal variable binding: Let K = count(manifest_slots); G2 write shows K=[N], |{verdicts}|=[N]; equality K=|{verdicts}| holds] | Introduce `Let K = count(manifest_slots)` at PHASE 3.5 gate entry; revise closure predicate condition 1 to `|{verdicts}| = K`; revise G2 write to show K and |{verdicts}| explicitly |

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
K (manifest_slot_count): [N]
```

**R2** Review matrix (6 columns, rows in slot order):

| Slot | Role | Lens | Findings | Severity | Recommendation |
|------|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s) from PHASE 2
2. Slot-gap escalation rows (1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

**R3** Cross-role synthesis (render from PHASE 3.5 G2-verified output):

Copy the synthesis verdicts produced in PHASE 3.5 S1. G2 confirmed |{verdicts}| = K = [N].
Render each verdict in slot-number order:
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

## V-04

**Axis**: Lifecycle + Output format (two-axis)
**Hypothesis**: V-01 binds manifest_slot_count at PHASE 1 LOAD (step L5) and references it
by name in G2 prose. V-02 renders the closure check as a typed assertion block. Merging
both creates two independent C-33 enforcement paths: (1) LOAD-bound variable makes the count
explicit before any synthesis begins, (2) typed assertion block makes the equality check a
visible structure at the moment of G2 closure. The assertion block in V-04 explicitly
references `manifest_slot_count` from PHASE 1 by name, linking the two paths into a single
traceable chain: LOAD emits N -> synthesis produces verdicts -> assertion block checks
verdicts = N -> G2 closes. Predicted: 175.0/175.0.

---

You are running `/crew-review`.

This skill executes in six lifecycle phases. The output schema -- including a Slot column and
a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. PHASE 1 LOAD binds `manifest_slot_count` as a named variable (step
L5). PHASE 3.5 synthesizes cross-role signals; G2 closure check is a typed predicate
assertion block that explicitly references `manifest_slot_count` from PHASE 1 and gates
AMEND. PHASE 4 validates the draft matrix before final render.

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
**Exit**: role pool locked and verified; manifest_slot_count bound

**L1** Open `.roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .roles/ not found.` Halt.
  - Directory empty: `ERROR: .roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.
**L5** Count slots in the committed manifest (Slot 1 through Slot N, including all declared
  slot-gap escalation rows). Bind this count as `manifest_slot_count`.

Write: `[LOAD: manifest_slot_count = N]`

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked; manifest_slot_count = N bound)
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
1. The G2 predicate assertion block (written at S2) shows N-for-N: SATISFIED --
   verdicts_produced equals manifest_slot_count bound at PHASE 1 LOAD.
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

**S2** Produce the G2 predicate assertion block. Reference `manifest_slot_count` from
PHASE 1 LOAD by name:

```
G2 predicate assertion:
  manifest_slot_count: [N]   <-- bound at PHASE 1 LOAD (step L5)
  verdicts_produced:   [N]   <-- count of S1 output above
  N-for-N:             SATISFIED
```

If verdicts_produced does not equal manifest_slot_count, write `N-for-N: NOT SATISFIED`
and return to S1. G2 cannot transition to CLOSED until N-for-N: SATISFIED.

Write: `[G2: CLOSED -- manifest_slot_count=[N] (PHASE 1 LOAD), verdicts_produced=[N]; predicate assertion N-for-N: SATISFIED]`

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
aspirational criteria through the current rubric version (v11), including C-26 through C-33
themselves. A table that stops before C-33 fails C-26 under v11. Every row carries a
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
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v11, including C-26 through C-33 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 rows present in this table] | Add rows for any missing aspirational criteria including C-26 through C-33 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [G2 predicate assertion N-for-N: SATISFIED; manifest_slot_count=[N] (PHASE 1 LOAD); verdicts_produced=[N]] | Return to PHASE 3.5 S1; produce missing verdicts; assertion block must show N-for-N: SATISFIED before G2 can close |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a "Remediation if NO" column with a specific action] | Add a specific return-to-phase instruction to every row that lacks one |
| C-29 | Exhaustive criterion-failure remediation coverage -- every row, not just at least one | [YES/NO/PARTIAL] | [all 22 rows in this table carry a populated Remediation if NO cell] | Ensure every row has a specific, actionable remediation instruction -- no row may be empty or generic |
| C-30 | Criterion-check table presented as typed 5-column schema with dedicated "Remediation if NO" column | [YES/NO/PARTIAL] | [column header reads: Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO] | Reformat table as typed 5-column schema with "Remediation if NO" as the 5th named header column |
| C-31 | Synthesis declared as a named discrete execution phase (PHASE 3.5 SYNTHESIZE) | [YES/NO/PARTIAL] | [PHASE 3.5 -- SYNTHESIZE header present at same heading level as PHASE 3 and PHASE 4] | Add PHASE 3.5 -- SYNTHESIZE as a named section heading between PHASE 3 and PHASE 4; move synthesis execution into it |
| C-32 | Synthesis phase gate G2 has formal exit condition blocking AMEND until synthesis closes | [YES/NO/PARTIAL] | [G2 OPEN/CLOSED states present + "AMEND does not begin until G2 transitions to CLOSED" statement in PHASE 3.5] | Add G2 state machine with OPEN/CLOSED labels; add explicit "AMEND does not begin until G2 transitions to CLOSED" blocking statement |
| C-33 | G2 closure predicate is quantified against LOAD manifest cardinality -- N-for-N form | [YES/NO/PARTIAL] | [PHASE 1 L5 binds manifest_slot_count=[N]; G2 predicate assertion block references it by name; N-for-N: SATISFIED shown] | Add step L5 to PHASE 1 binding manifest_slot_count; add typed G2 predicate assertion block at PHASE 3.5 S2 referencing manifest_slot_count from PHASE 1 by name; G2 cannot close until assertion shows N-for-N: SATISFIED |

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
manifest_slot_count: [N] (bound at PHASE 1 LOAD, step L5)
```

**R2** Review matrix (6 columns, rows in slot order):

| Slot | Role | Lens | Findings | Severity | Recommendation |
|------|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s) from PHASE 2
2. Slot-gap escalation rows (1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

**R3** Cross-role synthesis (render from PHASE 3.5 G2-verified output):

Copy the synthesis verdicts produced in PHASE 3.5 S1. G2 predicate assertion confirmed
manifest_slot_count = verdicts_produced = N; N-for-N: SATISFIED. Render each verdict in
slot-number order:
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

## V-05

**Axis**: Lifecycle + Output format + Inertia framing (three-axis)
**Hypothesis**: V-04 binds manifest_slot_count at LOAD and checks verdicts against it via
typed assertion. The gap: manifest_slot_count counts only slots declared before PHASE 1.
Slot-gap escalation rows (1a/1b/1c/1d) are produced dynamically during PHASE 2 when null
hypothesis slots cannot be filled. V-05 adds escalation-aware cardinality: PHASE 1 emits
`base_slot_count` (declared slots); PHASE 2 emits `escalation_row_count` after C6 closure
(rows produced during challenge); PHASE 3.5 computes `total_manifest_slot_count = base +
escalation` and the G2 assertion block checks verdicts against the total. This is the
strongest C-33 form: N is not just declared but computed across two phases, making the
predicate correct-by-construction against all rows that will appear in the final matrix --
including those dynamically added during inertia challenge. Predicted: 175.0/175.0.
Variation-specific C-34 signal: two-phase cardinality accumulation could motivate C-34
("G2 predicate total is the sum of a LOAD-bound base count and a CHALLENGE-bound escalation
count; the assertion block shows all three values: base, escalation, total").

---

You are running `/crew-review`.

This skill executes in six lifecycle phases. The output schema -- including a Slot column and
a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. PHASE 1 LOAD binds `base_slot_count`. PHASE 2 CHALLENGE emits
`escalation_row_count` after G1 closure. PHASE 3.5 computes `total_manifest_slot_count =
base + escalation`; G2 closure check is a typed predicate assertion block that verifies
verdicts against this total and gates AMEND. PHASE 4 validates the draft matrix before
final render.

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
Note: slot-gap escalation rows (1a/1b/1c/1d) are not declared here -- they are produced
dynamically during PHASE 2 and tracked in `escalation_row_count`.

---

### PHASE 1 -- LOAD

**Entry**: slot manifest committed
**Exit**: role pool locked and verified; base_slot_count bound

**L1** Open `.roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .roles/ not found.` Halt.
  - Directory empty: `ERROR: .roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.
**L5** Count slots declared in the committed manifest (Slot 1 through Slot N; slot-gap
  escalation rows are not yet known and are excluded from this count). Bind as
  `base_slot_count`.

Write: `[LOAD: base_slot_count = N]`

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked; base_slot_count = N bound)
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

Count escalation rows produced during PHASE 2 (all 1a/1b/1c/1d rows written above). Bind
this count as `escalation_row_count`.

Write: `[CHALLENGE: escalation_row_count = E]`

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

Compute: `total_manifest_slot_count = base_slot_count + escalation_row_count`
(base from PHASE 1 LOAD; escalation from PHASE 2 CHALLENGE).

**G2 state: OPEN.** AMEND is blocked.

**G2 closure predicate** -- G2 transitions from OPEN to CLOSED when ALL hold:
1. The G2 predicate assertion block (written at S2) shows N-for-N: SATISFIED --
   verdicts_produced equals total_manifest_slot_count.
2. Each verdict is one of: converged, conflicted, or unique.
3. No slot is omitted, merged with another, or assigned more than one verdict.
4. Every verdict statement references slot numbers.

**AMEND does not begin until G2 transitions to CLOSED.**

---

**S1** For every slot in the manifest (Slot 1 through Slot N, including all slot-gap
escalation rows 1a/1b/1c/1d produced in PHASE 2), assign exactly one verdict:
- `Slot [N] converged with Slot [M]: both find [shared concern].`
- `Slot [N] conflicts with Slot [M]: [tension description].`
- `Slot [N] is unique: [finding not overlapping with any other slot].`

**S2** Produce the G2 predicate assertion block:

```
G2 predicate assertion:
  base_slot_count:           [B]   <-- bound at PHASE 1 LOAD (step L5)
  escalation_row_count:      [E]   <-- bound at PHASE 2 CHALLENGE (step C6)
  total_manifest_slot_count: [N]   <-- B + E
  verdicts_produced:         [N]   <-- count of S1 output above
  N-for-N:                   SATISFIED
```

If verdicts_produced does not equal total_manifest_slot_count, write
`N-for-N: NOT SATISFIED` and return to S1. G2 cannot transition to CLOSED until
N-for-N: SATISFIED.

Write: `[G2: CLOSED -- base=[B]+escalation=[E]=total=[N]; verdicts_produced=[N]; N-for-N: SATISFIED]`

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
aspirational criteria through the current rubric version (v11), including C-26 through C-33
themselves. A table that stops before C-33 fails C-26 under v11. Every row carries a
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
| C-26 | Criterion-check table includes rows for ALL aspirational criteria through v11, including C-26 through C-33 themselves | [YES/NO/PARTIAL] | [C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 rows present in this table] | Add rows for any missing aspirational criteria including C-26 through C-33 before proceeding |
| C-27 | Every slot in the manifest receives an explicit synthesis verdict -- convergence, conflict, or unique | [YES/NO/PARTIAL] | [G2 predicate assertion N-for-N: SATISFIED; total_manifest_slot_count=[N] (base=[B]+escalation=[E]); verdicts_produced=[N]] | Return to PHASE 3.5 S1; assign verdicts to all missing slots including escalation rows 1a/1b/1c/1d; assertion block must show N-for-N: SATISFIED |
| C-28 | Every criterion-check table row carries a conditional remediation instruction | [YES/NO/PARTIAL] | [each row has a "Remediation if NO" column with a specific action] | Add a specific return-to-phase instruction to every row that lacks one |
| C-29 | Exhaustive criterion-failure remediation coverage -- every row, not just at least one | [YES/NO/PARTIAL] | [all 22 rows in this table carry a populated Remediation if NO cell] | Ensure every row has a specific, actionable remediation instruction -- no row may be empty or generic |
| C-30 | Criterion-check table presented as typed 5-column schema with dedicated "Remediation if NO" column | [YES/NO/PARTIAL] | [column header reads: Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO] | Reformat table as typed 5-column schema with "Remediation if NO" as the 5th named header column |
| C-31 | Synthesis declared as a named discrete execution phase (PHASE 3.5 SYNTHESIZE) | [YES/NO/PARTIAL] | [PHASE 3.5 -- SYNTHESIZE header present at same heading level as PHASE 3 and PHASE 4] | Add PHASE 3.5 -- SYNTHESIZE as a named section heading between PHASE 3 and PHASE 4; move synthesis execution into it |
| C-32 | Synthesis phase gate G2 has formal exit condition blocking AMEND until synthesis closes | [YES/NO/PARTIAL] | [G2 OPEN/CLOSED states present + "AMEND does not begin until G2 transitions to CLOSED" statement in PHASE 3.5] | Add G2 state machine with OPEN/CLOSED labels; add explicit "AMEND does not begin until G2 transitions to CLOSED" blocking statement |
| C-33 | G2 closure predicate is quantified against LOAD manifest cardinality -- N-for-N form | [YES/NO/PARTIAL] | [PHASE 1 L5 binds base_slot_count=[B]; PHASE 2 C6 binds escalation_row_count=[E]; G2 assertion: total=[N]=B+E; verdicts=[N]; N-for-N: SATISFIED] | Add step L5 to PHASE 1 binding base_slot_count; add escalation count write at PHASE 2 after C6 binding escalation_row_count; add typed G2 predicate assertion block at PHASE 3.5 S2 computing total=base+escalation and checking verdicts against total |

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
base_slot_count: [B] (PHASE 1 LOAD)
escalation_row_count: [E] (PHASE 2 CHALLENGE)
total_manifest_slot_count: [N] = B + E
```

**R2** Review matrix (6 columns, rows in slot order):

| Slot | Role | Lens | Findings | Severity | Recommendation |
|------|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s) from PHASE 2
2. Slot-gap escalation rows (1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

**R3** Cross-role synthesis (render from PHASE 3.5 G2-verified output):

Copy the synthesis verdicts produced in PHASE 3.5 S1. G2 predicate assertion confirmed
base=[B]+escalation=[E]=total=[N]; verdicts_produced=[N]; N-for-N: SATISFIED. Render each
verdict in slot-number order:
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
