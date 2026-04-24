---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 14
rubric: crew-roles-rubric-v8-2026-03-17.md
---

# crew-roles -- Variate R14

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

**Baseline**: R13 V-05 (ES-1 + ES-2 + CONVERGENCE SUMMARY combined, demonstrating C-28 and C-29).
R13 V-05 structure: 7 phases; Phase 2 AUDIT ITERATION LOG with CONVERGENCE SUMMARY (Q1-FINAL /
Q2-FINAL / Q3-FINAL); Phase 3 FRAME FILL from CONVERGENCE SUMMARY slots; Phase 4 FRAME CONFIRM;
Phase 5 PRE-WRITE SCOPE AUDIT (planning table, SCOPE AUDIT PASS gate); Phase 6 WRITE ROLE FILES
(inertia-advocate verify questions carry 5-mode annotations with TERM NOT IN QUESTION TEXT as fifth
mode); Phase 7 VERIFICATION GATE (7 checks: registry table, orphan refs, scope gradient + CHECK 3B
binding, vocab coverage, frame match, CHECK 6 five-mode annotation gate, CHECK 7 replacement
provenance). C-28 (fifth annotation failure mode) and C-29 (scope plan-to-write binding) are now
formalized in v8 -- all R14 variations treat them as baseline.

**Gaps identified in R13 V-05 against v8 criteria**:

- **Gap-1 -- No simplify imperative gate (C-06)**: Phase 6 instructs that simplify items are
  imperatives, but no named CHECK verifies this after writing. A simplify item phrased as a
  question (`"Consider whether X is necessary?"`) or a noun phrase (`"Scope reduction"`) passes
  Phase 7 unchallenged. The earliest detection surface is a human reader noticing the format error.

- **Gap-2 -- No perspective diversity gate (C-08)**: Phase 5 planning table has a Perspective
  column (`product`, `technical`, `inertia`, `domain`). Phase 6 says "minimum 3 roles; at least 3
  distinct perspective categories." But Phase 7 has no named CHECK that audits the perspective
  column for >= 3 distinct values. The scope gradient check (CHECK 3) is structurally analogous and
  has an explicit gate; perspective diversity has no equivalent.

- **Gap-3 -- No vocab plan-to-write binding (C-11 planning surface)**: Phase 5 planning table
  does not include which vocab term will anchor each role's expertise.relevance. CHECK 4 (vocab
  coverage) in Phase 7 audits the written files, but there is no planning-phase declaration of
  which vocab term is assigned to which role. A role that silently selects any Phase 1 term during
  writing passes CHECK 4 without accountability to a planned selection -- analogous to the scope
  drift C-29 closed.

**R14 variation axes**:
- V-01 (single): Role sequence -- inertia-advocate written first; all Q-answers, frame, and
  annotations locked before any other role; non-inertia roles consume FRAME CONFIRM as a fixed
  context signal
- V-02 (single): Output format -- Phase 5 planning table gains Planned-Vocab-Term column;
  CHECK 4 becomes a two-part check (4A: coverage, 4B: plan-to-write binding row-by-row)
- V-03 (single): Lifecycle emphasis -- inline per-role LENS AUDIT in Phase 6, emitted immediately
  after each role's verify and simplify fields are written, before moving to the next role
- V-04 (combined): Role sequence + Output format (inertia-first + vocab-plan binding)
- V-05 (combined): Output format + Lifecycle emphasis (vocab-plan binding + inline lens audit)

---

## V-01

**Axis**: Role sequence -- inertia-advocate written first (single axis)
**Hypothesis**: R13 V-05 writes roles in an unspecified order during Phase 6. The inertia-advocate
has the highest structural coupling: it depends on Phase 2 CONVERGENCE SUMMARY (for verify
annotations), Phase 4 FRAME CONFIRM (for frame verbatim match), and Phase 5 scope binding (for
cross-team scope). Non-inertia roles depend only on Phase 1 vocab terms and Phase 5 scope. Writing
inertia-advocate first locks the most constrained role before any other file exists, preventing
scope drift in non-inertia roles from creating pressure to silently re-scope the inertia-advocate
to restore gradient (a failure path under C-29). Writing non-inertia roles after the inertia role
also means Phase 5 scope diversity is partially satisfied before the first non-inertia file is
written -- the inertia-advocate's cross-team scope is already on record, so non-inertia roles only
need to supply the gradient delta. This removes the "I'll fix the gradient in CHECK 3" fallback
because the gradient is partially established by the first file written.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 -- DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets written; each bucket non-empty; each term has a row identifier;
         minimum 3 terms total

Read the input. Extract domain terms and assign each to exactly one of three named buckets. Each
term receives a permanent row identifier (`CS-N`, `MC-N`, `UH-N`) and a source phrase:

```
## Domain Vocabulary

Current-System Terms:
  [CS-1] {term}: "{source phrase from input}"
  [CS-2] {term}: "{source phrase from input}"

Migration-Cost Terms:
  [MC-1] {term}: "{source phrase from input}"

User-Habit Terms:
  [UH-1] {term}: "{source phrase from input}"
```

Assignment rules:
- Each term belongs to exactly one bucket; no term may appear in two buckets
- If any bucket is empty, extend by inference; label `[inferred]` with basis:
  "inferred from {X} because {reason}"
- Row identifiers are permanent: do not renumber; replacement terms in Phase 2 must cite their
  Phase 1 row -- if a term has no row, add it to Phase 1 before using it as a replacement

**Exit condition met**: three non-empty buckets; each term has a row identifier; minimum 3 terms.

---

### Phase 2 -- INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG + CONVERGENCE SUMMARY

**Entry**: Phase 1 complete
**Exit**: convergence declared; CONVERGENCE SUMMARY written with Q1-FINAL/Q2-FINAL/Q3-FINAL;
         all ATTEMPT blocks preserved; each replacement cites Phase 1 row

Answer three questions, citing Phase 1 row identifiers:

`Q1: [answer] [vocab: {CS-N} -- {term}]` (draw from Current-System Terms)
`Q2: [answer] [vocab: {MC-N} -- {term}]` (draw from Migration-Cost Terms)
`Q3: [answer] [vocab: {UH-N} -- {term}]` (draw from User-Habit Terms)

Open iteration log:

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|
| Q1 | {CS-N} | {term}    | Current-System  | YES/NO       |
| Q2 | {MC-N} | {term}    | Migration-Cost  | YES/NO       |
| Q3 | {UH-N} | {term}    | User-Habit      | YES/NO       |

ALL YES -> `ATTEMPT 1 RESULT: ALL YES -- Phase 2 convergence achieved.`

Any NO -> `ATTEMPT 1 RESULT: BLOCKED -- Q{N} row shows NO.`
Record replacement:
```
Replacement:
  Q{N} term "{old-term}" [{old-row-id}]
  -> "{new-term}" [{new-row-id}]
  Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"
```
Prior ATTEMPT blocks are not deleted. Continue until convergence.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES. {N} attempt(s) required.`
`Replacement provenance: [all replacements cite Phase 1 rows]` or `[no replacements made]`

After convergence, write the CONVERGENCE SUMMARY:

```
## Convergence Summary

Q1-FINAL: [verbatim convergence Q1 answer] [vocab: {CS-N} -- {term}]
Q2-FINAL: [verbatim convergence Q2 answer] [vocab: {MC-N} -- {term}]
Q3-FINAL: [verbatim convergence Q3 answer] [vocab: {UH-N} -- {term}]
```

Phase 3 Frame Fill and Phase 6 verify annotations consume from Q1-FINAL/Q2-FINAL/Q3-FINAL only.
Do not trace through iteration log entries to locate convergence answers.

**Exit condition met**: convergence declared; CONVERGENCE SUMMARY present; all blocks preserved;
replacements carry Phase 1 citations.

---

### Phase 3 -- FRAME FILL

**Entry**: Phase 2 complete (CONVERGENCE SUMMARY present)
**Exit**: completed frame string written with source citations; all slot-binding checks YES

The inertia-advocate `orientation.frame` uses this template:

```
Teams using [Q1 current system] have [Q2 migration cost] invested. Ask whether this change
is worth [Q3 user habit] disruption before committing.
```

Fill each slot from its designated CONVERGENCE SUMMARY answer:

```
## Frame Fill

Q1 slot <- CONVERGENCE SUMMARY Q1-FINAL: [verbatim Q1-FINAL answer]
Q2 slot <- CONVERGENCE SUMMARY Q2-FINAL: [verbatim Q2-FINAL answer]
Q3 slot <- CONVERGENCE SUMMARY Q3-FINAL: [verbatim Q3-FINAL answer]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding verification:
- Q1 slot <- Q1-FINAL answer (not Q2, not Q3): YES/NO
- Q2 slot <- Q2-FINAL answer (not Q1, not Q3): YES/NO
- Q3 slot <- Q3-FINAL answer (not Q1, not Q2): YES/NO

All three must be YES. A cross-slot binding is a blocking error.

**Exit condition met**: frame complete; source citations present; all slot-binding checks YES.

---

### Phase 4 -- FRAME CONFIRM

**Entry**: Phase 3 complete (all slot-binding checks YES)
**Exit**: FRAME CONFIRM statement present with verbatim Phase 3 paste

```
## Frame Confirm

FRAME CONFIRM: The inertia-advocate orientation.frame I will write first in Phase 6 is:
"{paste Phase 3 completed frame string -- character-for-character, including all punctuation}"
```

Rules:
- Paste verbatim -- do not paraphrase, rephrase, or summarize
- If you cannot reproduce the Phase 3 output exactly, return to Phase 3 and regenerate
- This string is binding: Phase 6 inertia-advocate `orientation.frame` must match exactly;
  Phase 7 CHECK 5 validates the match

**Exit condition met**: FRAME CONFIRM statement present with verbatim Phase 3 paste.

---

### Phase 5 -- PRE-WRITE SCOPE AUDIT

**Entry**: Phase 4 complete
**Exit**: planning table shows >= 2 distinct scope values; SCOPE AUDIT PASS declared

Before writing any role file, build the role plan:

| Planned Role        | Perspective | Scope      | Justification           |
|---------------------|-------------|------------|-------------------------|
| inertia-advocate    | inertia     | cross-team | status quo spans domain |
| pm                  | product     | {scope}    | {one reason from input} |
| architect           | technical   | {scope}    | {one reason from input} |
| {domain-specialist} | domain      | {scope}    | from Phase 1 vocabulary |

Add domain-specialist rows as needed. Scope definitions: `team`, `cross-team`, `org`.

**SCOPE AUDIT**: List distinct scope values. Gate: at least 2 distinct values.
If only 1: revise 1-2 roles. State changes. Confirm count >= 2.
`SCOPE AUDIT PASS -- scope values: [list]`

Scope values in this table are binding for Phase 6. Any deviation during writing must be corrected
or returned to Phase 5 with justification before proceeding. Writing blocked until scope audit
passes.

---

### Phase 6 -- WRITE ROLE FILES (INERTIA-ADVOCATE FIRST)

**Entry**: Phase 5 complete (scope audit passed)
**Exit**: all role files written; inertia-advocate written first and frame matches Phase 4;
         verify questions have 5-mode-valid annotations with terms in question body;
         every `expertise.relevance` references a Phase 1 term; scope matches Phase 5 table

Write each role to `.roles/{area}/{role-slug}.md`. All 5 fields required.
**Write the inertia-advocate first.** Non-inertia roles are written after inertia-advocate is
complete and committed.

**Step 1 -- Write inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use the FRAME CONFIRM string from Phase 4 verbatim
- `orientation.verify`: exactly 3 questions; BOTH conditions required per question:
  1. Carries a vocab-term annotation citing CONVERGENCE SUMMARY answers:
     - Q1: `{question?} [Q: Q1 -- vocab: {CS-N} -- {term-from-Q1-FINAL}]`
     - Q2: `{question?} [Q: Q2 -- vocab: {MC-N} -- {term-from-Q2-FINAL}]`
     - Q3: `{question?} [Q: Q3 -- vocab: {UH-N} -- {term-from-Q3-FINAL}]`
     - The `{term}` in each annotation must match the vocabulary term in the Q-FINAL answer
  2. The question text body contains the annotation `{term}` verbatim as a substring
     -- the term must appear in the question body, not only in the annotation tag
     -- correct: `"Has the team accounted for {term} costs?" [Q: Q2 -- vocab: MC-1 -- {term}]`
     -- incorrect: `"Has the team planned for this transition?" [Q: Q2 -- vocab: MC-1 -- {term}]`
- `orientation.simplify`: 2+ imperatives; each item begins with an imperative verb
- `expertise.relevance`: reference Q1-FINAL row identifier + at least one other Phase 1 term
- `scope`: cross-team (from Phase 5 table)
- `collaborates_with`: pm

**Step 2 -- Confirm inertia-advocate written**:
```
INERTIA-ADVOCATE WRITTEN: frame matches Phase 4 FRAME CONFIRM -- YES/NO
If NO: rewrite before proceeding to Step 3.
```

**Step 3 -- Write remaining roles** (pm, architect, domain-specialist(s)):

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative verb: action}
  - {Imperative verb: action}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing at least one Phase 1 row-identified term}

## scope
{value from Phase 5 planning table -- do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

Minimum 3 roles total (including inertia-advocate); at least 3 distinct perspective categories.

**Exit condition met**: inertia-advocate written first; all files written; frame matches Phase 4;
each verify question has valid annotation AND term in question body; every expertise.relevance
contains a Phase 1 term; scope values match Phase 5 table.

---

### Phase 7 -- VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 7 checks declare PASS; GATE RESULT declared before delivery

**DELIVERY IS BLOCKED. Complete all 7 checks in order. Each must declare PASS before the next
opens. Fix defects before proceeding.**

---

**CHECK 1 -- Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. All cells filled. Role names match file stems exactly.
`CHECK 1: PASS` or `CHECK 1: FAIL -- [issue]`

---

**CHECK 2 -- Orphan Reference Resolution**

For every `collaborates_with` value: does a file with that name exist in this registry?
Flag: `{name} [UNRESOLVED]`. Add missing role or remove reference. State action.
Gate: zero unresolved references.
`CHECK 2: PASS` or `CHECK 2: FAIL -- [action taken]`

---

**CHECK 3 -- Scope Gradient + Binding**

Part A -- Gradient: list distinct scope values from written files; gate >= 2.
`CHECK 3A: PASS -- scope values: [list]` or `CHECK 3A: FAIL -- [action taken]`

Part B -- Binding (after 3A PASS): compare Phase 5 planned scope to Phase 6 written scope per role:

| Role | Phase 5 Planned | Phase 6 Written | Match? |
|------|-----------------|-----------------|--------|

Flag: `[{role}: planned {A}, written {B} -- SCOPE BINDING MISMATCH]`
For each mismatch: (a) rewrite file to match plan, or (b) return to Phase 5, amend plan,
re-run scope audit, then re-write. State action. Gate: zero mismatches.

`CHECK 3: PASS` or `CHECK 3: FAIL -- [action taken]`

---

**CHECK 4 -- Vocabulary Coverage**

For each role's `expertise.relevance`: references a Phase 1 term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise; state term added.
Gate: all roles pass.
`CHECK 4: PASS` or `CHECK 4: FAIL -- [revisions made]`

---

**CHECK 5 -- Frame Confirm Match**

Compare the inertia-advocate `orientation.frame` against the Phase 4 FRAME CONFIRM string:

`Phase 4 FRAME CONFIRM: "{paste Phase 4 string}"`
`Inertia-advocate frame: "{paste Phase 6 frame value}"`

Gate: strings are identical, character-for-character.
If different: flag `[FRAME MISMATCH]`. Rewrite to match Phase 4 FRAME CONFIRM exactly.
`CHECK 5: PASS -- strings match` or `CHECK 5: FAIL -- [FRAME MISMATCH; rewritten]`

---

**CHECK 6 -- Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions, emit all applicable flags in order:

1. `[MISSING ANNOTATION]` -- no `[Q: QN -- vocab: ...]` tag present
2. `[Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
3. `[TERM MISMATCH: annotation says "{term-A}", CONVERGENCE SUMMARY Q{N}-FINAL recorded "{term-B}"]`
4. `[ROW-ID MISMATCH: annotation says {row-A}, CONVERGENCE SUMMARY Q{N}-FINAL used {row-B}]`
5. `[TERM NOT IN QUESTION TEXT: annotation term "{term}" not found in question body]`

Each failure mode is independently emitted before the next is checked. A question may produce
multiple flags. Revise; confirm all 5 checks clear for all 3 questions.

Gate: all 3 verify questions pass all 5 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL -- [revisions made]`

---

**CHECK 7 -- Replacement Provenance Audit**

For each replacement recorded in Phase 2's iteration log: does the record contain a Phase 1 row
citation (`{new-row-id} = "{term}" in Phase 1 {bucket}: "{source phrase}"`)? Can that row
identifier be found in Phase 1 output?

Flag: `Q{N} replacement "{old-term}" -> "{new-term}" [MISSING PHASE-1 CITATION]`
For each flagged: locate in Phase 1 or re-run Phase 2 with a term that exists in Phase 1.

Gate: every replacement cites a verifiable Phase 1 row, or no replacements were made.
`CHECK 7: PASS` or `CHECK 7: FAIL -- [revisions made]`

---

All 7 checks declared PASS -> `GATE RESULT: PASS` -- **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(Phase 5 table updated; CHECK 3B binding re-run; CHECK 6 re-run if inertia verify modified)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4; inertia-advocate re-written first with new frame and annotations; term-in-body condition applies)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5 and CHECK 3B)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-02

**Axis**: Output format -- augmented Phase 5 planning table with Planned-Vocab-Term column +
CHECK 4B plan-to-write vocab binding (single axis)
**Hypothesis**: R13 V-05 Phase 5 planning table has columns: Planned Role, Perspective, Scope,
Justification. CHECK 4 in Phase 7 audits whether each role's written expertise.relevance contains
any Phase 1 term -- a set-membership check. But there is no planning-phase declaration of which
specific vocab term is assigned to which role. A role can silently select any Phase 1 term during
writing and pass CHECK 4, regardless of what the planning context implied. This is structurally
identical to the scope drift that C-29 closed: Phase 5 planned a scope value, Phase 6 wrote a
different one, CHECK 3 (aggregate) passed because gradient still existed. The fix is to add a
Planned-Vocab-Term column to Phase 5, requiring the planner to name the specific Phase 1 term that
will anchor each role's expertise.relevance before writing begins. CHECK 4 then splits: CHECK 4A
confirms all roles have a vocab term (existing), CHECK 4B compares Phase 5 planned-vocab to Phase 6
written-vocab row-by-row and flags `[{role}: planned vocab "{planned-term}", written vocab
"{written-term}" -- VOCAB BINDING MISMATCH]`. This closes the planning-to-execution gap for C-11
exactly as CHECK 3B closes it for C-09.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 -- DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets written; each bucket non-empty; each term has a row identifier;
         minimum 3 terms total

Read the input. Extract domain terms and assign each to exactly one of three named buckets. Each
term receives a permanent row identifier (`CS-N`, `MC-N`, `UH-N`) and a source phrase:

```
## Domain Vocabulary

Current-System Terms:
  [CS-1] {term}: "{source phrase from input}"

Migration-Cost Terms:
  [MC-1] {term}: "{source phrase from input}"

User-Habit Terms:
  [UH-1] {term}: "{source phrase from input}"
```

- Each term belongs to exactly one bucket; row identifiers are permanent; no renumbering
- Empty buckets: extend by inference; label `[inferred]` with basis
- Replacement terms in Phase 2 must have Phase 1 rows; add first if absent

**Exit condition met**: three non-empty buckets; each term has a row identifier; minimum 3 terms.

---

### Phase 2 -- INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG + CONVERGENCE SUMMARY

**Entry**: Phase 1 complete
**Exit**: convergence declared; CONVERGENCE SUMMARY with Q1-FINAL/Q2-FINAL/Q3-FINAL present;
         all ATTEMPT blocks preserved; each replacement cites Phase 1 row

Answer three questions, citing Phase 1 row identifiers:

`Q1: [answer] [vocab: {CS-N} -- {term}]` (draw from Current-System Terms)
`Q2: [answer] [vocab: {MC-N} -- {term}]` (draw from Migration-Cost Terms)
`Q3: [answer] [vocab: {UH-N} -- {term}]` (draw from User-Habit Terms)

Open iteration log:

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|
| Q1 | {CS-N} | {term}    | Current-System  | YES/NO       |
| Q2 | {MC-N} | {term}    | Migration-Cost  | YES/NO       |
| Q3 | {UH-N} | {term}    | User-Habit      | YES/NO       |

ALL YES -> `ATTEMPT 1 RESULT: ALL YES -- Phase 2 convergence achieved.`

Any NO -> `ATTEMPT 1 RESULT: BLOCKED -- Q{N} row shows NO.`
Record replacement:
```
Replacement:
  Q{N} term "{old-term}" [{old-row-id}]
  -> "{new-term}" [{new-row-id}]
  Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"
```
Prior ATTEMPT blocks are not deleted. Continue until convergence.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES. {N} attempt(s) required.`

After convergence, write the CONVERGENCE SUMMARY:

```
## Convergence Summary

Q1-FINAL: [verbatim convergence Q1 answer] [vocab: {CS-N} -- {term}]
Q2-FINAL: [verbatim convergence Q2 answer] [vocab: {MC-N} -- {term}]
Q3-FINAL: [verbatim convergence Q3 answer] [vocab: {UH-N} -- {term}]
```

Phase 3 and Phase 6 consume from Q1-FINAL/Q2-FINAL/Q3-FINAL only.

**Exit condition met**: convergence declared; CONVERGENCE SUMMARY present; all blocks preserved;
replacements carry Phase 1 citations.

---

### Phase 3 -- FRAME FILL

**Entry**: Phase 2 complete
**Exit**: completed frame string written; all slot-binding checks YES

```
## Frame Fill

Q1 slot <- CONVERGENCE SUMMARY Q1-FINAL: [verbatim]
Q2 slot <- CONVERGENCE SUMMARY Q2-FINAL: [verbatim]
Q3 slot <- CONVERGENCE SUMMARY Q3-FINAL: [verbatim]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding: Q1<-Q1-FINAL, Q2<-Q2-FINAL, Q3<-Q3-FINAL -- all YES required. Cross-slot blocking.

**Exit condition met**: frame complete; all slot-binding checks YES.

---

### Phase 4 -- FRAME CONFIRM

**Entry**: Phase 3 complete
**Exit**: FRAME CONFIRM statement present with verbatim Phase 3 paste

```
## Frame Confirm

FRAME CONFIRM: "{paste Phase 3 completed frame string -- character-for-character}"
```

Verbatim paste only. If unable, return to Phase 3 and regenerate.

**Exit condition met**: FRAME CONFIRM statement present.

---

### Phase 5 -- PRE-WRITE SCOPE + VOCAB AUDIT

**Entry**: Phase 4 complete
**Exit**: planning table shows >= 2 distinct scope values AND each role has a named Planned-Vocab-
         Term; SCOPE AUDIT PASS and VOCAB PLAN COMPLETE both declared

Build the extended role plan. Each row requires a Planned-Vocab-Term: the specific Phase 1 row
identifier and term that will appear in this role's `expertise.relevance` when written in Phase 6.

| Planned Role        | Perspective | Scope      | Planned-Vocab-Term       | Justification           |
|---------------------|-------------|------------|--------------------------|-------------------------|
| inertia-advocate    | inertia     | cross-team | {CS-N}: {term}           | Q1-FINAL anchor         |
| pm                  | product     | {scope}    | {row-id}: {term}         | {one reason from input} |
| architect           | technical   | {scope}    | {row-id}: {term}         | {one reason from input} |
| {domain-specialist} | domain      | {scope}    | {row-id}: {term}         | from Phase 1 vocabulary |

Rules for Planned-Vocab-Term:
- Must be a Phase 1 row identifier + term (e.g., `MC-1: re-routing-cost`)
- Each row should prefer a distinct vocab term; overlap is permitted if the domain is narrow
- The inertia-advocate's planned vocab term must cite the Q1-FINAL row identifier

Add domain-specialist rows as needed. Scope definitions: `team`, `cross-team`, `org`.

**SCOPE AUDIT**: List distinct scope values. Gate: at least 2 distinct values.
`SCOPE AUDIT PASS -- scope values: [list]`

**VOCAB PLAN COMPLETE**: Confirm every role row has a Planned-Vocab-Term with a valid Phase 1
row identifier. If any row is missing: assign from Phase 1 before proceeding.
`VOCAB PLAN COMPLETE -- all roles have planned vocab terms`

Writing blocked until SCOPE AUDIT PASS and VOCAB PLAN COMPLETE are both declared.

---

### Phase 6 -- WRITE ROLE FILES

**Entry**: Phase 5 complete (scope audit passed; vocab plan complete)
**Exit**: all role files written; scope values match Phase 5 table; vocab terms match Phase 5
         Planned-Vocab-Term column; inertia-advocate frame matches Phase 4;
         verify questions have 5-mode-valid annotations with terms in question body

Write each role to `.roles/{area}/{role-slug}.md`. All 5 fields required.

**For non-inertia roles** -- consume Planned-Vocab-Term from Phase 5 table for expertise.relevance:

```markdown
# {Role Name}

## orientation
frame: {one sentence}
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative verb: action}
  - {Imperative verb: action}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing the Phase 5 Planned-Vocab-Term for this role by row identifier}

## scope
{value from Phase 5 planning table -- do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use Phase 4 FRAME CONFIRM string verbatim
- `orientation.verify`: exactly 3 questions; BOTH conditions required per question:
  1. Carries annotation: `{question?} [Q: QN -- vocab: {row-id} -- {term-from-QN-FINAL}]`
  2. Question text body contains the annotation `{term}` verbatim as a substring
- `orientation.simplify`: 2+ imperatives; each begins with an imperative verb
- `expertise.relevance`: reference Phase 5 Planned-Vocab-Term row identifier (Q1-FINAL row)
  plus at least one other Phase 1 term
- `scope`: cross-team (from Phase 5 table)
- `collaborates_with`: pm

Minimum 3 roles total; at least 3 distinct perspective categories.

**Exit condition met**: all files written; scope and vocab match Phase 5 table; frame matches
Phase 4; annotations valid; all terms in question bodies.

---

### Phase 7 -- VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 7 checks declare PASS; GATE RESULT declared

**DELIVERY IS BLOCKED. Complete all 7 checks in order.**

---

**CHECK 1 -- Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. All cells filled. Role names match file stems.
`CHECK 1: PASS` or `CHECK 1: FAIL -- [issue]`

---

**CHECK 2 -- Orphan Reference Resolution**

Flag unresolved `collaborates_with` values. Gate: zero unresolved.
`CHECK 2: PASS` or `CHECK 2: FAIL -- [action taken]`

---

**CHECK 3 -- Scope Gradient + Binding**

Part A -- Gradient: list distinct values; gate >= 2.
`CHECK 3A: PASS -- scope values: [list]`

Part B -- Binding: compare Phase 5 planned scope to Phase 6 written scope per role:

| Role | Phase 5 Planned | Phase 6 Written | Match? |
|------|-----------------|-----------------|--------|

Flag: `[{role}: planned {A}, written {B} -- SCOPE BINDING MISMATCH]`
Resolve by rewriting or returning to Phase 5 with justification. Gate: zero mismatches.
`CHECK 3: PASS` or `CHECK 3: FAIL -- [action taken]`

---

**CHECK 4 -- Vocabulary Coverage + Binding**

Part A -- Coverage: for each role's `expertise.relevance`, does it reference a Phase 1 term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise. Gate: all roles pass.
`CHECK 4A: PASS` or `CHECK 4A: FAIL -- [revisions made]`

Part B -- Binding (after 4A PASS): compare Phase 5 Planned-Vocab-Term to Phase 6 written vocab
term per role. Extract the Phase 1 row identifier actually used in each expertise.relevance:

| Role | Phase 5 Planned-Vocab-Term | Phase 6 Written-Vocab-Term | Match? |
|------|---------------------------|---------------------------|--------|

Flag: `[{role}: planned vocab "{planned-term}", written vocab "{written-term}" -- VOCAB BINDING MISMATCH]`
For each mismatch: (a) rewrite expertise.relevance to use the planned term, or (b) return to
Phase 5 and update Planned-Vocab-Term with justification before rewriting. State action.
Gate: zero mismatches.

`CHECK 4: PASS` or `CHECK 4: FAIL -- [action taken]`

---

**CHECK 5 -- Frame Confirm Match**

Compare Phase 4 FRAME CONFIRM to Phase 6 inertia-advocate frame. Character-for-character.
Flag: `[FRAME MISMATCH]`. Rewrite to match.
`CHECK 5: PASS -- strings match` or `CHECK 5: FAIL -- [FRAME MISMATCH; rewritten]`

---

**CHECK 6 -- Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions, emit all applicable flags in order:

1. `[MISSING ANNOTATION]` -- no `[Q: QN -- vocab: ...]` tag
2. `[Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
3. `[TERM MISMATCH: annotation says "{term-A}", CONVERGENCE SUMMARY Q{N}-FINAL recorded "{term-B}"]`
4. `[ROW-ID MISMATCH: annotation says {row-A}, CONVERGENCE SUMMARY Q{N}-FINAL used {row-B}]`
5. `[TERM NOT IN QUESTION TEXT: annotation term "{term}" not found in question body]`

Each failure mode independently emitted. Revise until all 5 checks clear for all 3 questions.
`CHECK 6: PASS` or `CHECK 6: FAIL -- [revisions made]`

---

**CHECK 7 -- Replacement Provenance Audit**

Flag: `Q{N} replacement "{old}" -> "{new}" [MISSING PHASE-1 CITATION]`
Gate: every replacement cites verifiable Phase 1 row, or no replacements made.
`CHECK 7: PASS` or `CHECK 7: FAIL -- [revisions made]`

---

All 7 checks declared PASS -> `GATE RESULT: PASS` -- **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(Phase 5 table extended with Planned-Vocab-Term; CHECK 3B + CHECK 4B binding re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4; Phase 5 Planned-Vocab-Term for inertia row updated; term-in-body applies)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5 and CHECK 3B)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-03

**Axis**: Lifecycle emphasis -- inline per-role LENS AUDIT in Phase 6 (single axis)
**Hypothesis**: R13 V-05 Phase 6 instructs that simplify items are imperatives and verify items
end in `?`. But no named CHECK in Phase 7 validates this. A simplify item written as a noun phrase
(`"Scope reduction for team-level changes"`) or a passive construction (`"Dependencies should be
minimized"`) passes all 7 checks. The lens format constraint is stated in Phase 6 instructions but
not enforced by any gate. Adding an inline LENS AUDIT block immediately after each role's verify
and simplify fields are written -- before moving to the next role -- creates a per-role detection
surface rather than a terminal check. The inline audit emits:
`[{role} simplify item {N}: "{item}" -- NOT AN IMPERATIVE]` if the item does not begin with an
imperative verb, and `[{role} verify item {N}: "{item}" -- MISSING ? TERMINATOR]` if the item does
not end in `?`. Fixing in-line (per role, before writing the next role) eliminates cascading lens
errors across multiple roles and makes Phase 6 self-correcting rather than error-accumulating.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 -- DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets written; each bucket non-empty; each term has a row identifier;
         minimum 3 terms total

Read the input. Extract domain terms and assign each to exactly one of three named buckets. Each
term receives a permanent row identifier (`CS-N`, `MC-N`, `UH-N`) and a source phrase:

```
## Domain Vocabulary

Current-System Terms:
  [CS-1] {term}: "{source phrase from input}"

Migration-Cost Terms:
  [MC-1] {term}: "{source phrase from input}"

User-Habit Terms:
  [UH-1] {term}: "{source phrase from input}"
```

- Each term belongs to exactly one bucket; row identifiers are permanent; no renumbering
- Empty buckets: extend by inference; label `[inferred]` with basis
- Replacement terms in Phase 2 must have Phase 1 rows; add first if absent

**Exit condition met**: three non-empty buckets; each term has a row identifier; minimum 3 terms.

---

### Phase 2 -- INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG + CONVERGENCE SUMMARY

**Entry**: Phase 1 complete
**Exit**: convergence declared; CONVERGENCE SUMMARY with Q1-FINAL/Q2-FINAL/Q3-FINAL present;
         all ATTEMPT blocks preserved; each replacement cites Phase 1 row

`Q1: [answer] [vocab: {CS-N} -- {term}]` (draw from Current-System Terms)
`Q2: [answer] [vocab: {MC-N} -- {term}]` (draw from Migration-Cost Terms)
`Q3: [answer] [vocab: {UH-N} -- {term}]` (draw from User-Habit Terms)

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|
| Q1 | {CS-N} | {term}    | Current-System  | YES/NO       |
| Q2 | {MC-N} | {term}    | Migration-Cost  | YES/NO       |
| Q3 | {UH-N} | {term}    | User-Habit      | YES/NO       |

ALL YES -> `ATTEMPT 1 RESULT: ALL YES -- Phase 2 convergence achieved.`
Any NO -> `ATTEMPT 1 RESULT: BLOCKED -- Q{N} row shows NO.` Record replacement with Phase 1
citation. Prior blocks not deleted. Continue until convergence.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES.`

```
## Convergence Summary

Q1-FINAL: [verbatim Q1 answer] [vocab: {CS-N} -- {term}]
Q2-FINAL: [verbatim Q2 answer] [vocab: {MC-N} -- {term}]
Q3-FINAL: [verbatim Q3 answer] [vocab: {UH-N} -- {term}]
```

**Exit condition met**: convergence declared; CONVERGENCE SUMMARY present.

---

### Phase 3 -- FRAME FILL

**Entry**: Phase 2 complete
**Exit**: completed frame string written; all slot-binding checks YES

```
## Frame Fill

Q1 slot <- Q1-FINAL: [verbatim]
Q2 slot <- Q2-FINAL: [verbatim]
Q3 slot <- Q3-FINAL: [verbatim]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding: Q1<-Q1-FINAL, Q2<-Q2-FINAL, Q3<-Q3-FINAL -- all YES. Cross-slot blocking.

**Exit condition met**: frame complete; slot-binding YES.

---

### Phase 4 -- FRAME CONFIRM

**Entry**: Phase 3 complete
**Exit**: FRAME CONFIRM present with verbatim Phase 3 paste

```
## Frame Confirm

FRAME CONFIRM: "{paste Phase 3 completed frame string -- character-for-character}"
```

**Exit condition met**: FRAME CONFIRM present.

---

### Phase 5 -- PRE-WRITE SCOPE AUDIT

**Entry**: Phase 4 complete
**Exit**: planning table shows >= 2 distinct scope values; SCOPE AUDIT PASS declared

| Planned Role        | Perspective | Scope      | Justification           |
|---------------------|-------------|------------|-------------------------|
| inertia-advocate    | inertia     | cross-team | status quo spans domain |
| pm                  | product     | {scope}    | {one reason from input} |
| architect           | technical   | {scope}    | {one reason from input} |
| {domain-specialist} | domain      | {scope}    | from Phase 1 vocabulary |

Gate: >= 2 distinct scope values. If only 1: revise 1-2 roles.
`SCOPE AUDIT PASS -- scope values: [list]`

Scope values are binding for Phase 6. Writing blocked until scope audit passes.

---

### Phase 6 -- WRITE ROLE FILES WITH INLINE LENS AUDIT

**Entry**: Phase 5 complete
**Exit**: all role files written with LENS AUDIT PASS declared per role; inertia-advocate frame
         matches Phase 4; verify annotations have 5-mode-valid format with terms in question body;
         every expertise.relevance references a Phase 1 term

Write each role to `.roles/{area}/{role-slug}.md`. **After writing each role's verify and
simplify fields, immediately run the LENS AUDIT for that role before writing the next role.**

**Role writing template:**

```markdown
# {Role Name}

## orientation
frame: {one sentence}
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative verb: action}
  - {Imperative verb: action}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing at least one Phase 1 row-identified term}

## scope
{value from Phase 5 planning table -- do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**LENS AUDIT (run immediately after writing each role's orientation fields):**

```
LENS AUDIT -- {role-name}:

verify items:
  [{N}] "{item}" -- ends in ? YES/NO
  [{N}] "{item}" -- ends in ? YES/NO
  ...

simplify items:
  [{N}] "{item}" -- begins with imperative verb? YES/NO
  [{N}] "{item}" -- begins with imperative verb? YES/NO
  ...
```

For each NO:
- verify item: `[{role} verify item {N}: "{item}" -- MISSING ? TERMINATOR]`
  Rewrite as a question ending in `?` before proceeding.
- simplify item: `[{role} simplify item {N}: "{item}" -- NOT AN IMPERATIVE]`
  Rewrite to begin with an imperative verb (e.g., Remove, Collapse, Defer, Enforce) before
  proceeding.

`LENS AUDIT {role-name}: PASS` (all items pass) or `LENS AUDIT {role-name}: FAIL -- [rewrites made]`

Do not write the next role until LENS AUDIT PASS is declared for the current role.

**Additional requirements for the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: use Phase 4 FRAME CONFIRM string verbatim
- `orientation.verify`: exactly 3 questions; BOTH conditions per question:
  1. Carries annotation: `{question?} [Q: QN -- vocab: {row-id} -- {term-from-QN-FINAL}]`
  2. Question text body contains annotation `{term}` verbatim as substring
- `orientation.simplify`: 2+ imperatives (LENS AUDIT will verify imperative format)
- `expertise.relevance`: Q1-FINAL row identifier + at least one other Phase 1 term
- `scope`: cross-team; `collaborates_with`: pm

Minimum 3 roles total; at least 3 distinct perspective categories.

**Exit condition met**: all files written; each role has LENS AUDIT PASS; frame matches Phase 4;
annotations valid with terms in question bodies; expertise.relevance has Phase 1 terms.

---

### Phase 7 -- VERIFICATION GATE

**Entry**: Phase 6 complete (all LENS AUDIT PASS declared)
**Exit**: all 7 checks declare PASS; GATE RESULT declared

**DELIVERY IS BLOCKED. Complete all 7 checks in order.**

---

**CHECK 1 -- Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. Role names match file stems.
`CHECK 1: PASS` or `CHECK 1: FAIL -- [issue]`

---

**CHECK 2 -- Orphan Reference Resolution**

Flag unresolved `collaborates_with`. Gate: zero unresolved.
`CHECK 2: PASS` or `CHECK 2: FAIL -- [action taken]`

---

**CHECK 3 -- Scope Gradient + Binding**

Part A -- Gradient: list distinct values; gate >= 2.
`CHECK 3A: PASS -- scope values: [list]`

Part B -- Binding: Phase 5 planned vs Phase 6 written per role:

| Role | Phase 5 Planned | Phase 6 Written | Match? |
|------|-----------------|-----------------|--------|

Flag: `[{role}: planned {A}, written {B} -- SCOPE BINDING MISMATCH]` Gate: zero mismatches.
`CHECK 3: PASS` or `CHECK 3: FAIL -- [action taken]`

---

**CHECK 4 -- Vocabulary Coverage**

Flag: `{role-name} [NO VOCAB TERM]`. Revise. Gate: all pass.
`CHECK 4: PASS` or `CHECK 4: FAIL -- [revisions made]`

---

**CHECK 5 -- Frame Confirm Match**

Phase 4 FRAME CONFIRM vs Phase 6 frame. Character-for-character. Flag `[FRAME MISMATCH]`.
`CHECK 5: PASS` or `CHECK 5: FAIL -- [FRAME MISMATCH; rewritten]`

---

**CHECK 6 -- Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions, emit all applicable flags in order:

1. `[MISSING ANNOTATION]`
2. `[Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
3. `[TERM MISMATCH: annotation says "{term-A}", CONVERGENCE SUMMARY Q{N}-FINAL recorded "{term-B}"]`
4. `[ROW-ID MISMATCH: annotation says {row-A}, CONVERGENCE SUMMARY Q{N}-FINAL used {row-B}]`
5. `[TERM NOT IN QUESTION TEXT: annotation term "{term}" not found in question body]`

Each failure mode independently emitted. Gate: all 3 questions pass all 5 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL -- [revisions made]`

---

**CHECK 7 -- Replacement Provenance Audit**

Flag missing Phase 1 citations on Phase 2 replacements. Gate: all replacements cited or none made.
`CHECK 7: PASS` or `CHECK 7: FAIL -- [revisions made]`

---

All 7 checks PASS -> `GATE RESULT: PASS` -- **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(LENS AUDIT required for new role's verify and simplify fields; CHECK 3B re-run)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4; inertia re-written with LENS AUDIT; term-in-body condition applies)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5 and CHECK 3B)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-04

**Axis**: Role sequence + Output format -- inertia-first writing + augmented Phase 5 planning
table with Planned-Vocab-Term column + CHECK 4B vocab binding (two-axis combination: V-01 + V-02)
**Hypothesis**: V-01 establishes inertia-advocate-first writing: the most structurally coupled role
is written before any other, locking frame, annotations, and Q-answers as a fixed context before
non-inertia roles are written. V-02 extends Phase 5 with a Planned-Vocab-Term column and adds
CHECK 4B row-by-row vocab binding, closing the planning-to-execution gap for C-11 exactly as
CHECK 3B closes it for C-09. These two axes target different artifacts: V-01 governs role write
order (sequencing); V-02 governs planning table content and post-write binding (format + check).
They do not create mutual dependencies -- the inertia-first sequence does not affect the vocab
binding table, and the vocab binding table does not affect write order. The expected interaction:
writing inertia-advocate first forces Q-FINAL terms to be actively used in question bodies before
any Planned-Vocab-Term assignments are made for other roles, reducing the risk that the planning
table selects terms that were implicitly "used up" by inertia-advocate annotation authoring.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 -- DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets written; each bucket non-empty; each term has a row identifier;
         minimum 3 terms total

```
## Domain Vocabulary

Current-System Terms:
  [CS-1] {term}: "{source phrase from input}"

Migration-Cost Terms:
  [MC-1] {term}: "{source phrase from input}"

User-Habit Terms:
  [UH-1] {term}: "{source phrase from input}"
```

- Each term belongs to exactly one bucket; row identifiers permanent; no renumbering
- Empty buckets: extend by inference; label `[inferred]` with basis
- Replacement terms in Phase 2 must have Phase 1 rows; add first if absent

**Exit condition met**: three non-empty buckets; each term has row identifier; minimum 3 terms.

---

### Phase 2 -- INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG + CONVERGENCE SUMMARY

**Entry**: Phase 1 complete
**Exit**: convergence declared; CONVERGENCE SUMMARY with Q1-FINAL/Q2-FINAL/Q3-FINAL present

`Q1: [answer] [vocab: {CS-N} -- {term}]` (Current-System Terms)
`Q2: [answer] [vocab: {MC-N} -- {term}]` (Migration-Cost Terms)
`Q3: [answer] [vocab: {UH-N} -- {term}]` (User-Habit Terms)

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|
| Q1 | {CS-N} | {term}    | Current-System  | YES/NO       |
| Q2 | {MC-N} | {term}    | Migration-Cost  | YES/NO       |
| Q3 | {UH-N} | {term}    | User-Habit      | YES/NO       |

ALL YES -> convergence. Any NO -> record replacement with Phase 1 citation; retry. Prior blocks
not deleted.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES.`

```
## Convergence Summary

Q1-FINAL: [verbatim Q1 answer] [vocab: {CS-N} -- {term}]
Q2-FINAL: [verbatim Q2 answer] [vocab: {MC-N} -- {term}]
Q3-FINAL: [verbatim Q3 answer] [vocab: {UH-N} -- {term}]
```

Phase 3 and Phase 6 consume from CONVERGENCE SUMMARY only.

**Exit condition met**: convergence declared; CONVERGENCE SUMMARY present.

---

### Phase 3 -- FRAME FILL

**Entry**: Phase 2 complete
**Exit**: completed frame string; all slot-binding checks YES

```
Q1 slot <- Q1-FINAL: [verbatim]
Q2 slot <- Q2-FINAL: [verbatim]
Q3 slot <- Q3-FINAL: [verbatim]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding: Q1<-Q1-FINAL, Q2<-Q2-FINAL, Q3<-Q3-FINAL -- all YES. Cross-slot blocking.

---

### Phase 4 -- FRAME CONFIRM

**Entry**: Phase 3 complete
**Exit**: FRAME CONFIRM present

```
FRAME CONFIRM: The inertia-advocate orientation.frame I will write first in Phase 6 is:
"{paste Phase 3 completed frame -- character-for-character}"
```

---

### Phase 5 -- PRE-WRITE SCOPE + VOCAB AUDIT

**Entry**: Phase 4 complete
**Exit**: planning table shows >= 2 distinct scope values; each role has Planned-Vocab-Term;
         SCOPE AUDIT PASS and VOCAB PLAN COMPLETE both declared

| Planned Role        | Perspective | Scope      | Planned-Vocab-Term | Justification           |
|---------------------|-------------|------------|--------------------|-------------------------|
| inertia-advocate    | inertia     | cross-team | {CS-N}: {term}     | Q1-FINAL anchor         |
| pm                  | product     | {scope}    | {row-id}: {term}   | {one reason from input} |
| architect           | technical   | {scope}    | {row-id}: {term}   | {one reason from input} |
| {domain-specialist} | domain      | {scope}    | {row-id}: {term}   | from Phase 1 vocabulary |

Planned-Vocab-Term rules:
- Must be a valid Phase 1 row identifier + term
- Inertia row must cite Q1-FINAL row identifier

**SCOPE AUDIT**: >= 2 distinct scope values. If only 1: revise.
`SCOPE AUDIT PASS -- scope values: [list]`

**VOCAB PLAN COMPLETE**: every row has a Planned-Vocab-Term with valid Phase 1 row identifier.
`VOCAB PLAN COMPLETE -- all roles have planned vocab terms`

Writing blocked until both declared.

---

### Phase 6 -- WRITE ROLE FILES (INERTIA-ADVOCATE FIRST)

**Entry**: Phase 5 complete
**Exit**: inertia-advocate written first; all role files written; scope and vocab match Phase 5;
         frame matches Phase 4; annotations 5-mode-valid; terms in question bodies

**Step 1 -- Write inertia-advocate first** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: Phase 4 FRAME CONFIRM string verbatim
- `orientation.verify`: 3 questions; per question:
  1. Annotation: `{question?} [Q: QN -- vocab: {row-id} -- {term-from-QN-FINAL}]`
  2. Term in question body: annotation `{term}` appears verbatim in question text
- `orientation.simplify`: 2+ imperatives beginning with imperative verbs
- `expertise.relevance`: Phase 5 Planned-Vocab-Term row for inertia row + one other Phase 1 term
- `scope`: cross-team; `collaborates_with`: pm

**Step 2 -- Confirm inertia-advocate written**:
```
INERTIA-ADVOCATE WRITTEN: frame matches Phase 4 FRAME CONFIRM -- YES/NO
If NO: rewrite before Step 3.
```

**Step 3 -- Write remaining roles** consuming Planned-Vocab-Term from Phase 5 for expertise.relevance:

```markdown
# {Role Name}

## orientation
frame: {one sentence}
verify:
  - {question?}
  - {question?}
simplify:
  - {Imperative: action}
  - {Imperative: action}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing Phase 5 Planned-Vocab-Term row identifier for this role}

## scope
{value from Phase 5 planning table -- do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

Minimum 3 roles; at least 3 distinct perspective categories.

---

### Phase 7 -- VERIFICATION GATE

**Entry**: Phase 6 complete
**Exit**: all 7 checks PASS; GATE RESULT declared

**DELIVERY IS BLOCKED.**

---

**CHECK 1 -- Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |

One row per role. Role names match file stems.
`CHECK 1: PASS` or `CHECK 1: FAIL -- [issue]`

---

**CHECK 2 -- Orphan Reference Resolution**

Flag unresolved `collaborates_with`. Gate: zero.
`CHECK 2: PASS` or `CHECK 2: FAIL -- [action taken]`

---

**CHECK 3 -- Scope Gradient + Binding**

3A: list distinct values; gate >= 2.
3B: Phase 5 planned vs Phase 6 written per role -- flag `[{role}: planned {A}, written {B} -- SCOPE BINDING MISMATCH]`; gate: zero mismatches.
`CHECK 3: PASS` or `CHECK 3: FAIL -- [action taken]`

---

**CHECK 4 -- Vocabulary Coverage + Binding**

4A: every expertise.relevance has Phase 1 term -- flag `[NO VOCAB TERM]`; gate: all pass.

4B (after 4A PASS): Phase 5 Planned-Vocab-Term vs Phase 6 written vocab per role:

| Role | Phase 5 Planned-Vocab-Term | Phase 6 Written-Vocab-Term | Match? |
|------|---------------------------|---------------------------|--------|

Flag: `[{role}: planned vocab "{planned-term}", written vocab "{written-term}" -- VOCAB BINDING MISMATCH]`
Resolve by rewriting or returning to Phase 5 with justification. Gate: zero mismatches.

`CHECK 4: PASS` or `CHECK 4: FAIL -- [action taken]`

---

**CHECK 5 -- Frame Confirm Match**

Phase 4 FRAME CONFIRM vs Phase 6 inertia-advocate frame. Character-for-character.
`CHECK 5: PASS` or `CHECK 5: FAIL -- [FRAME MISMATCH; rewritten]`

---

**CHECK 6 -- Verify-Question Vocab-Term Citation Coverage**

For each of the inertia-advocate's 3 verify questions, emit all applicable flags:

1. `[MISSING ANNOTATION]`
2. `[Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
3. `[TERM MISMATCH: annotation says "{term-A}", CONVERGENCE SUMMARY Q{N}-FINAL recorded "{term-B}"]`
4. `[ROW-ID MISMATCH: annotation says {row-A}, CONVERGENCE SUMMARY Q{N}-FINAL used {row-B}]`
5. `[TERM NOT IN QUESTION TEXT: annotation term "{term}" not found in question body]`

Gate: all 3 questions pass all 5 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL -- [revisions made]`

---

**CHECK 7 -- Replacement Provenance Audit**

Flag missing Phase 1 citations. Gate: all cited or none made.
`CHECK 7: PASS` or `CHECK 7: FAIL -- [revisions made]`

---

All 7 PASS -> `GATE RESULT: PASS` -- **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(Phase 5 extended with Planned-Vocab-Term; CHECK 3B + CHECK 4B re-run; new role written after existing inertia-advocate)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4; inertia re-written first; new verify with term-in-body)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5 and CHECK 3B)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-05

**Axis**: Output format + Lifecycle emphasis -- augmented Phase 5 planning table (Planned-Vocab-Term
column + CHECK 4B) + inline per-role LENS AUDIT in Phase 6 (two-axis combination: V-02 + V-03)
**Hypothesis**: V-02 closes the C-11 planning-to-execution gap by adding a Planned-Vocab-Term column
to Phase 5 and a row-by-row CHECK 4B binding audit in Phase 7. V-03 closes the C-06 simplify
imperative gap by adding an inline LENS AUDIT that runs per role during Phase 6, catching format
errors before the terminal gate. These two axes target different structural gaps at different phases:
V-02 operates at the planning surface (Phase 5) and the post-write check surface (CHECK 4B, Phase 7);
V-03 operates at the writing surface (Phase 6 inline). They are non-overlapping and non-conflicting.
The expected interaction: the inline LENS AUDIT creates a natural pause after each role's
orientation section is written -- this is the same moment the writer would confirm that expertise
.relevance uses the Planned-Vocab-Term. The combination allows a single inline audit block to check
both lens format (LENS AUDIT) and vocab binding (planned vs written) per role, consolidating two
per-role quality gates into one structured inline block. V-05 tests whether this consolidation
reduces Phase 6 ceremony relative to running them separately while preserving both detection surfaces.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**7 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 -- DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: three named buckets written; each bucket non-empty; each term has a row identifier;
         minimum 3 terms total

```
## Domain Vocabulary

Current-System Terms:
  [CS-1] {term}: "{source phrase from input}"

Migration-Cost Terms:
  [MC-1] {term}: "{source phrase from input}"

User-Habit Terms:
  [UH-1] {term}: "{source phrase from input}"
```

- Each term in exactly one bucket; row identifiers permanent; no renumbering
- Empty buckets: extend by inference; label `[inferred]` with basis
- Replacement terms in Phase 2 must have Phase 1 rows; add first if absent

**Exit condition met**: three non-empty buckets; each term has row identifier; minimum 3 terms.

---

### Phase 2 -- INERTIA PRE-CHARACTERIZATION + AUDIT ITERATION LOG + CONVERGENCE SUMMARY

**Entry**: Phase 1 complete
**Exit**: convergence declared; CONVERGENCE SUMMARY with Q1-FINAL/Q2-FINAL/Q3-FINAL present;
         all ATTEMPT blocks preserved; each replacement cites Phase 1 row

`Q1: [answer] [vocab: {CS-N} -- {term}]` (Current-System Terms)
`Q2: [answer] [vocab: {MC-N} -- {term}]` (Migration-Cost Terms)
`Q3: [answer] [vocab: {UH-N} -- {term}]` (User-Habit Terms)

**AUDIT ATTEMPT 1:**

| Q  | Row ID | Term Used | Expected Bucket | Match YES/NO |
|----|--------|-----------|-----------------|--------------|
| Q1 | {CS-N} | {term}    | Current-System  | YES/NO       |
| Q2 | {MC-N} | {term}    | Migration-Cost  | YES/NO       |
| Q3 | {UH-N} | {term}    | User-Habit      | YES/NO       |

ALL YES -> `ATTEMPT 1 RESULT: ALL YES -- convergence achieved.`
Any NO -> `ATTEMPT 1 RESULT: BLOCKED.` Record replacement with Phase 1 citation. Retry. Prior
blocks not deleted.

`AUDIT CONVERGENCE: ATTEMPT {N} ALL YES.`

```
## Convergence Summary

Q1-FINAL: [verbatim Q1 answer] [vocab: {CS-N} -- {term}]
Q2-FINAL: [verbatim Q2 answer] [vocab: {MC-N} -- {term}]
Q3-FINAL: [verbatim Q3 answer] [vocab: {UH-N} -- {term}]
```

Phase 3 and Phase 6 consume from CONVERGENCE SUMMARY only.

**Exit condition met**: convergence declared; CONVERGENCE SUMMARY present.

---

### Phase 3 -- FRAME FILL

**Entry**: Phase 2 complete
**Exit**: completed frame string; all slot-binding checks YES

```
Q1 slot <- Q1-FINAL: [verbatim]
Q2 slot <- Q2-FINAL: [verbatim]
Q3 slot <- Q3-FINAL: [verbatim]

Completed frame:
"Teams using [filled Q1] have [filled Q2] invested. Ask whether this change is
worth [filled Q3] disruption before committing."
```

Slot-binding: Q1<-Q1-FINAL, Q2<-Q2-FINAL, Q3<-Q3-FINAL -- all YES. Cross-slot blocking.

**Exit condition met**: frame complete; slot-binding YES.

---

### Phase 4 -- FRAME CONFIRM

**Entry**: Phase 3 complete
**Exit**: FRAME CONFIRM present

```
FRAME CONFIRM: "{paste Phase 3 completed frame -- character-for-character}"
```

Verbatim only. If unable: return to Phase 3, regenerate.

**Exit condition met**: FRAME CONFIRM present.

---

### Phase 5 -- PRE-WRITE SCOPE + VOCAB AUDIT

**Entry**: Phase 4 complete
**Exit**: planning table shows >= 2 distinct scope values; each role has Planned-Vocab-Term;
         SCOPE AUDIT PASS and VOCAB PLAN COMPLETE both declared

| Planned Role        | Perspective | Scope      | Planned-Vocab-Term | Justification           |
|---------------------|-------------|------------|--------------------|-------------------------|
| inertia-advocate    | inertia     | cross-team | {CS-N}: {term}     | Q1-FINAL anchor         |
| pm                  | product     | {scope}    | {row-id}: {term}   | {one reason from input} |
| architect           | technical   | {scope}    | {row-id}: {term}   | {one reason from input} |
| {domain-specialist} | domain      | {scope}    | {row-id}: {term}   | from Phase 1 vocabulary |

Planned-Vocab-Term: valid Phase 1 row identifier + term. Inertia row must cite Q1-FINAL row.

**SCOPE AUDIT**: >= 2 distinct scope values.
`SCOPE AUDIT PASS -- scope values: [list]`

**VOCAB PLAN COMPLETE**: every row has Planned-Vocab-Term with valid Phase 1 row identifier.
`VOCAB PLAN COMPLETE`

Writing blocked until both declared.

---

### Phase 6 -- WRITE ROLE FILES WITH INLINE ROLE AUDIT

**Entry**: Phase 5 complete
**Exit**: all role files written; each has ROLE AUDIT PASS; scope matches Phase 5; inertia-
         advocate frame matches Phase 4; annotations 5-mode-valid with terms in question bodies

Write each role to `.roles/{area}/{role-slug}.md`. After completing each role file, run the
ROLE AUDIT for that role before proceeding to the next.

**Role writing template:**

```markdown
# {Role Name}

## orientation
frame: {one sentence}
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative verb: action}
  - {Imperative verb: action}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing Phase 5 Planned-Vocab-Term row identifier for this role}

## scope
{value from Phase 5 planning table -- do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**ROLE AUDIT (run after completing each role, before writing the next):**

```
ROLE AUDIT -- {role-name}:

lens check:
  verify items:
    [{N}] "{item}" -- ends in ? YES/NO
  simplify items:
    [{N}] "{item}" -- begins with imperative verb? YES/NO

vocab binding:
  Phase 5 Planned-Vocab-Term: {row-id}: {term}
  Phase 6 expertise.relevance contains: {row-id or "none found"}
  Match: YES/NO

scope binding:
  Phase 5 planned scope: {scope}
  Phase 6 written scope: {scope}
  Match: YES/NO
```

For each LENS CHECK NO:
- `[{role} verify item {N}: "{item}" -- MISSING ? TERMINATOR]` -> rewrite as question
- `[{role} simplify item {N}: "{item}" -- NOT AN IMPERATIVE]` -> rewrite to begin with imperative verb

For VOCAB BINDING NO:
- `[{role}: planned vocab "{planned}", written vocab "{written}" -- VOCAB BINDING MISMATCH]`
- Rewrite expertise.relevance to use planned term, or return to Phase 5 and update with
  justification before proceeding

For SCOPE BINDING NO:
- `[{role}: planned {planned}, written {written} -- SCOPE BINDING MISMATCH]`
- Rewrite scope field or return to Phase 5 with justification

`ROLE AUDIT {role-name}: PASS` or `ROLE AUDIT {role-name}: FAIL -- [rewrites made, re-auditing]`

Re-run ROLE AUDIT after each rewrite. Do not write the next role until ROLE AUDIT PASS.

**Additional requirements for the inertia-advocate** (`.roles/{area}/inertia-advocate.md`):

- `orientation.frame`: Phase 4 FRAME CONFIRM verbatim
- `orientation.verify`: 3 questions; each requires:
  1. Annotation: `{question?} [Q: QN -- vocab: {row-id} -- {term-from-QN-FINAL}]`
  2. Annotation `{term}` appears verbatim in question body (not only in tag)
- `orientation.simplify`: 2+ imperatives (ROLE AUDIT checks imperative format)
- `expertise.relevance`: Phase 5 inertia Planned-Vocab-Term + one other Phase 1 term
- `scope`: cross-team; `collaborates_with`: pm

Minimum 3 roles; at least 3 distinct perspective categories.

---

### Phase 7 -- VERIFICATION GATE

**Entry**: Phase 6 complete (all ROLE AUDIT PASS declared)
**Exit**: all 7 checks PASS; GATE RESULT declared

**DELIVERY IS BLOCKED. Run all 7 checks in order.**

Note: CHECK 3B and CHECK 4B were both enforced inline during Phase 6 ROLE AUDIT. Phase 7 runs
them again as a terminal confirmation -- inline audits are per-role gates, not delivery gates.

---

**CHECK 1 -- Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |

One row per role. Role names match file stems.
`CHECK 1: PASS` or `CHECK 1: FAIL -- [issue]`

---

**CHECK 2 -- Orphan Reference Resolution**

Flag unresolved `collaborates_with`. Gate: zero.
`CHECK 2: PASS` or `CHECK 2: FAIL -- [action taken]`

---

**CHECK 3 -- Scope Gradient + Binding**

3A: distinct values; gate >= 2. `CHECK 3A: PASS`

3B: Phase 5 planned vs Phase 6 written per role:

| Role | Phase 5 Planned | Phase 6 Written | Match? |

Flag mismatches. Gate: zero. `CHECK 3: PASS` or `CHECK 3: FAIL -- [action taken]`

---

**CHECK 4 -- Vocabulary Coverage + Binding**

4A: every expertise.relevance has Phase 1 term. Gate: all pass. `CHECK 4A: PASS`

4B: Phase 5 Planned-Vocab-Term vs Phase 6 written vocab per role:

| Role | Phase 5 Planned-Vocab-Term | Phase 6 Written-Vocab-Term | Match? |

Flag mismatches. Gate: zero. `CHECK 4: PASS` or `CHECK 4: FAIL -- [action taken]`

---

**CHECK 5 -- Frame Confirm Match**

Phase 4 FRAME CONFIRM vs Phase 6 inertia frame. Character-for-character.
`CHECK 5: PASS` or `CHECK 5: FAIL -- [FRAME MISMATCH; rewritten]`

---

**CHECK 6 -- Verify-Question Vocab-Term Citation Coverage**

For each inertia-advocate verify question, emit all applicable flags:

1. `[MISSING ANNOTATION]`
2. `[Q-NUMBER MISMATCH: annotation says Q{N}, content references Q{M} dimension]`
3. `[TERM MISMATCH: annotation says "{term-A}", CONVERGENCE SUMMARY Q{N}-FINAL recorded "{term-B}"]`
4. `[ROW-ID MISMATCH: annotation says {row-A}, CONVERGENCE SUMMARY Q{N}-FINAL used {row-B}]`
5. `[TERM NOT IN QUESTION TEXT: annotation term "{term}" not found in question body]`

Gate: all 3 questions pass all 5 checks.
`CHECK 6: PASS` or `CHECK 6: FAIL -- [revisions made]`

---

**CHECK 7 -- Replacement Provenance Audit**

Flag missing Phase 1 citations. Gate: all cited or none made.
`CHECK 7: PASS` or `CHECK 7: FAIL -- [revisions made]`

---

All 7 PASS -> `GATE RESULT: PASS` -- **Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(Phase 5 extended with Planned-Vocab-Term; new role goes through ROLE AUDIT including lens + vocab + scope binding; CHECK 3B + CHECK 4B re-run in Phase 7)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phases 2-4; inertia re-written with ROLE AUDIT; term-in-body condition applies to new verify questions)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 5 and CHECK 3B; also re-triggers ROLE AUDIT scope binding for affected roles)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 7)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`
